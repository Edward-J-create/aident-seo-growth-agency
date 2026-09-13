#!/usr/bin/env python3
"""Validate a brand SEO page-map CSV for ownership and architecture conflicts."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


REQUIRED = {"page_id", "page_type", "proposed_url", "primary_keyword", "phase", "status"}
ALLOWED_PHASES = {"P0", "P1", "P2", "BACKLOG", "HOLD"}
ALLOWED_STATUSES = {"keep", "improve", "create", "consolidate", "redirect", "noindex", "retire"}


def key(value: str | None) -> str:
    return re.sub(r"\s+", " ", (value or "").strip()).casefold()


def url_key(value: str) -> str:
    value = value.strip()
    if not value:
        return ""
    parts = urlsplit(value)
    path = re.sub(r"/{2,}", "/", parts.path or "/")
    if path != "/":
        path = path.rstrip("/")
    return urlunsplit((parts.scheme.casefold(), parts.netloc.casefold(), path, parts.query, ""))


def split_ids(value: str) -> list[str]:
    return [part.strip() for part in re.split(r"[|;,]", value or "") if part.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("page_map_csv", type=Path)
    args = parser.parse_args()

    with args.page_map_csv.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = set(reader.fieldnames or [])
        missing = sorted(REQUIRED - fields)
        if missing:
            print(f"ERROR: missing columns: {', '.join(missing)}")
            return 2
        rows = list(reader)

    errors: list[str] = []
    warnings: list[str] = []
    by_id: dict[str, int] = {}
    by_url: defaultdict[str, list[str]] = defaultdict(list)
    by_keyword: defaultdict[str, list[str]] = defaultdict(list)
    by_title: defaultdict[str, list[str]] = defaultdict(list)

    for line, row in enumerate(rows, start=2):
        page_id = (row.get("page_id") or "").strip()
        label = page_id or f"line {line}"
        if not page_id:
            errors.append(f"line {line}: blank page_id")
        elif page_id in by_id:
            errors.append(f"line {line}: duplicate page_id '{page_id}' (first at line {by_id[page_id]})")
        else:
            by_id[page_id] = line

        proposed_url = url_key(row.get("proposed_url") or "")
        status = key(row.get("status"))
        if not proposed_url and status not in {"retire"}:
            errors.append(f"{label}: proposed_url is blank")
        if proposed_url:
            by_url[proposed_url].append(label)

        primary = key(row.get("primary_keyword"))
        if primary and status not in {"noindex", "retire", "redirect"}:
            by_keyword[primary].append(label)

        phase = (row.get("phase") or "").strip().upper()
        if phase not in ALLOWED_PHASES:
            warnings.append(f"{label}: unrecognized phase '{phase}'")
        if status not in ALLOWED_STATUSES:
            warnings.append(f"{label}: unrecognized status '{row.get('status', '')}'")
        if status in {"redirect", "consolidate"} and not (row.get("canonical_or_redirect_note") or "").strip():
            errors.append(f"{label}: {status} requires canonical_or_redirect_note")

        title = key(row.get("title"))
        if title:
            by_title[title].append(label)
            if len((row.get("title") or "").strip()) > 65:
                warnings.append(f"{label}: title exceeds 65 characters; review likely truncation")
        meta = (row.get("meta_description") or "").strip()
        if len(meta) > 165:
            warnings.append(f"{label}: meta description exceeds 165 characters; review likely truncation")
        h1 = (row.get("h1") or "").strip()
        if not h1 and status not in {"redirect", "retire"}:
            warnings.append(f"{label}: H1 is blank")

    for value, labels in by_url.items():
        if len(labels) > 1:
            errors.append(f"duplicate proposed_url '{value}' owned by {', '.join(labels)}")
    for value, labels in by_keyword.items():
        if len(labels) > 1:
            errors.append(f"primary keyword '{value}' owned by {', '.join(labels)}")
    for value, labels in by_title.items():
        if len(labels) > 1:
            warnings.append(f"duplicate title '{value}' used by {', '.join(labels)}")

    ids = set(by_id)
    for row in rows:
        page_id = (row.get("page_id") or "").strip() or "unknown"
        parent = (row.get("parent_id") or "").strip()
        if parent and parent not in ids:
            errors.append(f"{page_id}: parent_id '{parent}' does not exist")
        for target in split_ids(row.get("internal_link_targets") or ""):
            if target not in ids and not target.startswith(("http://", "https://")):
                warnings.append(f"{page_id}: internal_link_target '{target}' is not a page_id or absolute URL")

    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARNING: {message}")
    print(f"Checked {len(rows)} pages: {len(errors)} errors, {len(warnings)} warnings.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
