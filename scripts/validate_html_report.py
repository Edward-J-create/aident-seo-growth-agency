#!/usr/bin/env python3
"""Validate portability and native interaction invariants for an SEO HTML report."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import tempfile
from html.parser import HTMLParser
from pathlib import Path


CSS_URL_RE = re.compile(r"url\(\s*(['\"]?)([^)'\"]+)\1\s*\)", re.IGNORECASE)
SCRIPT_RE = re.compile(r"<script(?:\s[^>]*)?>([\s\S]*?)</script>", re.IGNORECASE)


class ReportParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tabs: list[dict[str, str]] = []
        self.panels: list[dict[str, str]] = []
        self.asset_refs: list[tuple[str, str, str]] = []
        self.external_stylesheets: list[str] = []
        self.forbidden_tags: list[str] = []
        self.title_depth = 0
        self.title_text: list[str] = []
        self.meta_description = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        values = {key.lower(): (value or "") for key, value in attrs}
        if tag == "button" and values.get("role") == "tab":
            self.tabs.append(values)
        if values.get("role") == "tabpanel":
            self.panels.append(values)
        if tag in {"iframe", "object", "embed"}:
            self.forbidden_tags.append(tag)
        if tag == "title":
            self.title_depth += 1
        if tag == "meta" and values.get("name", "").lower() == "description":
            self.meta_description = values.get("content", "").strip()
        if tag == "link" and "stylesheet" in values.get("rel", "").lower():
            self.external_stylesheets.append(values.get("href", ""))
        for attr in ("src", "poster", "data"):
            if attr in values:
                self.asset_refs.append((tag, attr, values[attr]))

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title" and self.title_depth:
            self.title_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.title_depth:
            self.title_text.append(data)


def check_javascript(html: str, errors: list[str], warnings: list[str]) -> None:
    scripts = SCRIPT_RE.findall(html)
    if not scripts:
        errors.append("No inline JavaScript found for native tab interaction")
        return
    node = shutil.which("node")
    if not node:
        warnings.append("Node.js unavailable; inline JavaScript syntax was not checked")
        return
    for index, script in enumerate(scripts, start=1):
        with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8") as handle:
            handle.write(script)
            handle.flush()
            result = subprocess.run([node, "--check", handle.name], capture_output=True, text=True)
        if result.returncode:
            errors.append(f"Inline script {index} failed syntax check: {result.stderr.strip()}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    path = args.report.resolve()
    if not path.is_file():
        parser.error(f"Report not found: {path}")

    html = path.read_text(encoding="utf-8")
    parsed = ReportParser()
    parsed.feed(html)
    errors: list[str] = []
    warnings: list[str] = []

    tab_ids = [item.get("id", "") for item in parsed.tabs]
    controls = [item.get("aria-controls", "") for item in parsed.tabs]
    panel_ids = [item.get("id", "") for item in parsed.panels]
    labelled_by = [item.get("aria-labelledby", "") for item in parsed.panels]
    if not parsed.tabs:
        errors.append("No native role=tab buttons found")
    if len(tab_ids) != len(set(tab_ids)) or "" in tab_ids:
        errors.append("Tab IDs must be present and unique")
    if len(panel_ids) != len(set(panel_ids)) or "" in panel_ids:
        errors.append("Panel IDs must be present and unique")
    if len(controls) != len(set(controls)) or "" in controls:
        errors.append("Every tab must control one unique panel")
    if sorted(controls) != sorted(panel_ids):
        errors.append(f"Tab/panel mapping mismatch: controls={controls}, panels={panel_ids}")
    if sorted(labelled_by) != sorted(tab_ids):
        errors.append("Every panel must be labelled by its matching tab")
    selected = [item for item in parsed.tabs if item.get("aria-selected") == "true"]
    if len(selected) != 1:
        errors.append(f"Expected exactly one initially selected tab, found {len(selected)}")

    title = "".join(parsed.title_text).strip()
    if not title:
        errors.append("Document title is missing")
    if not parsed.meta_description:
        errors.append("Meta description is missing")
    if parsed.forbidden_tags:
        errors.append(f"Forbidden embedded viewer tags found: {sorted(set(parsed.forbidden_tags))}")
    if parsed.external_stylesheets:
        errors.append(f"External stylesheets found: {parsed.external_stylesheets}")

    for tag, attr, value in parsed.asset_refs:
        if value and not value.startswith("data:"):
            errors.append(f"Non-embedded asset reference: <{tag} {attr}=\"{value}\">")
    for match in CSS_URL_RE.finditer(html):
        value = match.group(2).strip()
        if not value.startswith(("data:", "#")):
            errors.append(f"Non-embedded CSS asset: {value}")

    forbidden_literals = {
        "skill-asset://": "Unbuilt skill asset URL",
        "file://": "Local file URI",
        "codex://": "Codex-only URI",
        "visualization-container": "Codex visualization wrapper",
        "--codex": "Codex runtime theme variable",
    }
    lowered = html.lower()
    for literal, label in forbidden_literals.items():
        if literal in lowered:
            errors.append(f"{label} found: {literal}")
    marker = re.search(r"\{\{[A-Z][A-Z0-9_. -]{1,80}\}\}", html)
    if marker:
        errors.append(f"Unexpanded template marker found: {marker.group(0)}")
    if "@media print" not in lowered:
        warnings.append("No print stylesheet detected")
    if "prefers-reduced-motion" not in lowered:
        warnings.append("No reduced-motion rule detected")

    check_javascript(html, errors, warnings)

    if warnings:
        for warning in warnings:
            print(f"WARN: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"FAIL: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    size_mb = path.stat().st_size / (1024 * 1024)
    print(f"PASS: {path}")
    print(f"Tabs/panels: {len(parsed.tabs)}/{len(parsed.panels)}; size: {size_mb:.2f} MiB; external assets: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
