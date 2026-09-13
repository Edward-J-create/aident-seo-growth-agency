#!/usr/bin/env python3
"""Offline package integrity checks; not a comprehensive secret or SEO audit."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
EXCLUDED = {".git", "__pycache__", ".venv", "node_modules", "output"}
TEXT_SUFFIXES = {".md", ".py", ".mjs", ".json", ".yaml", ".yml", ".html", ".svg", ".csv", ".txt"}


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    required = [
        "SKILL.md", "README.md", "README.en.md", "NOTICE.md", "SECURITY.md",
        "CONTRIBUTING.md", "agents/openai.yaml", "assets/html-report-template.html",
        "assets/fonts/manifest.json", "assets/project-brief-template.yaml",
        "assets/source-register-template.csv", "assets/capability-log-template.csv",
        "scripts/normalize_keywords.py", "scripts/validate_page_map.py",
        "scripts/build_standalone_report.py", "scripts/validate_html_report.py",
    ]
    for relative in required:
        if not (root / relative).is_file():
            errors.append(f"Missing required file: {relative}")
    if errors:
        return errors

    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    front = re.match(r"\A---\n(.*?)\n---\n", skill, re.S)
    if not front:
        errors.append("SKILL.md must begin with YAML frontmatter")
    else:
        fields = front.group(1)
        if not re.search(r"^name: brand-seo-growth-workflow$", fields, re.M):
            errors.append("Skill name does not match the published installation name")
        if not re.search(r"^description: .+", fields, re.M):
            errors.append("Skill description is missing")

    # Narrow, deterministic checks for common accidental disclosures, without printing values.
    patterns = [
        ("personal absolute path", re.compile(r"/(?:Users|home)/[A-Za-z0-9_.-]+/")),
        ("GitHub token", re.compile(r"(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,})")),
        ("private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
        ("AWS access key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ]
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if set(relative.parts) & EXCLUDED:
            continue
        if path.is_symlink():
            errors.append(f"Unexpected symlink in distributed package: {relative}")
            continue
        if not path.is_file():
            continue
        if path.name == ".env" or path.name.startswith(".env.") or path.suffix in {".pem", ".key"}:
            errors.append(f"Sensitive file type in package: {relative}")
        if path.suffix not in TEXT_SUFFIXES:
            continue
        content = path.read_text(encoding="utf-8")
        for label, pattern in patterns:
            if pattern.search(content):
                errors.append(f"Potential {label}: {relative} (value suppressed)")
        if path.suffix != ".md":
            continue
        # Validate relative inline Markdown links; external destinations are intentionally offline.
        for raw in re.findall(r"!?\[[^\]]*\]\(([^)\n]+)\)", content):
            target = raw.strip().strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                errors.append(f"Broken/out-of-package link in {relative}: {target}")

    manifest = json.loads((root / "assets/fonts/manifest.json").read_text(encoding="utf-8"))
    font_root = root / "assets/fonts"
    for item in manifest["fonts"]:
        font = font_root / item["file"]
        license_file = font_root / item["license"]
        if not font.is_file():
            errors.append(f"Missing font: {item['family']}")
        elif hashlib.sha256(font.read_bytes()).hexdigest() != item["sha256"]:
            errors.append(f"Font SHA-256 mismatch: {item['family']}")
        if not license_file.is_file() or "SIL OPEN FONT LICENSE" not in license_file.read_text(encoding="utf-8"):
            errors.append(f"Missing/invalid OFL notice: {item['family']}")
    return errors


if __name__ == "__main__":
    issues = validate()
    for issue in issues:
        print(f"ERROR: {issue}")
    print(f"{'FAIL' if issues else 'PASS'}: package integrity, local documentation links, font hashes and basic disclosure checks")
    print("Does not verify live providers, browser rendering, data accuracy or all possible secrets.")
    sys.exit(1 if issues else 0)
