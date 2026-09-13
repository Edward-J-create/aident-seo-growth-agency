#!/usr/bin/env python3
"""Inline skill-owned or local HTML assets into one portable HTML file."""

from __future__ import annotations

import argparse
import base64
import mimetypes
import re
import tempfile
from pathlib import Path
from urllib.parse import unquote


SKILL_ROOT = Path(__file__).resolve().parent.parent
SKILL_PREFIX = "skill-asset://"
CSS_URL_RE = re.compile(r"url\(\s*(['\"]?)([^)'\"]+)\1\s*\)", re.IGNORECASE)
ASSET_ATTR_RE = re.compile(
    r"(?P<prefix>\b(?:src|poster)\s*=\s*['\"])(?P<value>[^'\"]+)(?P<suffix>['\"])",
    re.IGNORECASE,
)


def mime_for(path: Path) -> str:
    explicit = {
        ".ttf": "font/ttf",
        ".otf": "font/otf",
        ".woff": "font/woff",
        ".woff2": "font/woff2",
        ".svg": "image/svg+xml",
        ".webp": "image/webp",
    }
    return explicit.get(path.suffix.lower()) or mimetypes.guess_type(path.name)[0] or "application/octet-stream"


def resolve_asset(value: str, input_dir: Path) -> Path | None:
    value = value.strip()
    if value.startswith(("data:", "#", "about:", "blob:")):
        return None
    if value.startswith(("http://", "https://", "//")):
        raise ValueError(f"Remote asset is not allowed in a standalone report: {value}")
    if value.startswith(SKILL_PREFIX):
        candidate = SKILL_ROOT / "assets" / unquote(value[len(SKILL_PREFIX):])
        if not candidate.resolve().is_relative_to((SKILL_ROOT / "assets").resolve()):
            raise ValueError("Skill asset must stay inside the packaged assets directory")
    else:
        candidate = Path(unquote(value))
        if not candidate.is_absolute():
            candidate = input_dir / candidate
    candidate = candidate.resolve()
    if not candidate.is_file():
        raise FileNotFoundError(f"Asset not found: {value} -> {candidate}")
    return candidate


def to_data_uri(path: Path) -> str:
    payload = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_for(path)};base64,{payload}"


def inline_assets(html: str, input_dir: Path) -> tuple[str, list[Path]]:
    embedded: list[Path] = []
    cache: dict[Path, str] = {}

    def uri_for(path: Path) -> str:
        if path not in cache:
            cache[path] = to_data_uri(path)
            embedded.append(path)
        return cache[path]

    def replace_css(match: re.Match[str]) -> str:
        value = match.group(2)
        path = resolve_asset(value, input_dir)
        return match.group(0) if path is None else f'url("{uri_for(path)}")'

    def replace_attr(match: re.Match[str]) -> str:
        value = match.group("value")
        path = resolve_asset(value, input_dir)
        if path is None:
            return match.group(0)
        return f'{match.group("prefix")}{uri_for(path)}{match.group("suffix")}'

    html = CSS_URL_RE.sub(replace_css, html)
    html = ASSET_ATTR_RE.sub(replace_attr, html)
    return html, embedded


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False, suffix=".html") as handle:
        handle.write(text)
        temp_path = Path(handle.name)
    temp_path.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="HTML source file")
    parser.add_argument("--output", type=Path, help="Output path; defaults to <stem>-standalone.html")
    args = parser.parse_args()

    source = args.input.resolve()
    if not source.is_file():
        parser.error(f"Input not found: {source}")
    output = (args.output or source.with_name(f"{source.stem}-standalone.html")).resolve()
    html = source.read_text(encoding="utf-8")
    rendered, embedded = inline_assets(html, source.parent)
    atomic_write(output, rendered)
    size_mb = output.stat().st_size / (1024 * 1024)
    print(f"Built {output}")
    print(f"Embedded {len(embedded)} unique assets; output size {size_mb:.2f} MiB")
    for path in embedded:
        print(f"  - {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
