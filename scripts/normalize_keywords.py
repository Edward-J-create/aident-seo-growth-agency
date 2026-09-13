#!/usr/bin/env python3
"""Normalize, deduplicate, and transparently score SEO keyword CSV exports.

Uses only the Python standard library. Missing metrics remain blank and are never
converted to zero. The output is a working file; a human still owns relevance,
intent, SERP-overlap, and page-ownership decisions.
"""

from __future__ import annotations

import argparse
import csv
import math
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path


ALIASES = {
    "keyword": ("keyword", "query", "term", "keywords"),
    "country": ("country", "database", "location"),
    "language": ("language", "lang"),
    "intent": ("intent", "search_intent"),
    "parent_topic": ("parent_topic", "parent topic", "topic"),
    "volume": ("volume", "search_volume", "search volume"),
    "kd": ("kd", "keyword_difficulty", "difficulty"),
    "cpc": ("cpc", "cost_per_click"),
    "business_value": ("business_value", "business value", "bv"),
    "strategic_fit": ("strategic_fit", "strategic fit"),
    "current_gap": ("current_gap", "current gap", "gap_score"),
    "current_url": ("current_url", "current url", "ranking_url"),
    "competitor_url": ("competitor_url", "competitor url"),
    "source": ("source", "data_source", "provider"),
    "retrieved_at": ("retrieved_at", "retrieved", "date"),
}

OUTPUT_FIELDS = [
    "keyword",
    "normalized_keyword",
    "country",
    "language",
    "intent",
    "parent_topic",
    "volume",
    "kd",
    "cpc",
    "business_value",
    "strategic_fit",
    "current_gap",
    "current_url",
    "competitor_url",
    "source",
    "retrieved_at",
    "duplicate_rows_merged",
    "priority_score",
    "score_status",
]


def canonical_header(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")


def find_columns(fieldnames: list[str]) -> dict[str, str]:
    normalized = {canonical_header(name): name for name in fieldnames}
    found = {}
    for target, aliases in ALIASES.items():
        for alias in aliases:
            key = canonical_header(alias)
            if key in normalized:
                found[target] = normalized[key]
                break
    return found


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    value = unicodedata.normalize("NFKC", value)
    return re.sub(r"\s+", " ", value).strip()


def normalized_keyword(value: str) -> str:
    return clean_text(value).casefold()


def parse_number(value: str) -> float | None:
    text = clean_text(value).replace(",", "").replace("$", "").replace("%", "")
    if not text or text.lower() in {"n/a", "na", "null", "none", "-"}:
        return None
    multiplier = 1.0
    if text[-1:].lower() == "k":
        multiplier, text = 1_000.0, text[:-1]
    elif text[-1:].lower() == "m":
        multiplier, text = 1_000_000.0, text[:-1]
    try:
        number = float(text) * multiplier
        return number if math.isfinite(number) else None
    except ValueError:
        return None


def display_number(value: float | None) -> str:
    if value is None:
        return ""
    return str(int(value)) if value.is_integer() else f"{value:.4f}".rstrip("0").rstrip(".")


def row_value(row: dict[str, str], columns: dict[str, str], name: str) -> str:
    column = columns.get(name)
    return clean_text(row.get(column, "")) if column else ""


def completeness(row: dict[str, str], columns: dict[str, str]) -> tuple[int, float]:
    values = [row_value(row, columns, name) for name in ALIASES]
    volume = parse_number(row_value(row, columns, "volume"))
    volume = -1 if volume is None else volume
    return sum(bool(value) for value in values), volume


def merge_group(rows: list[dict[str, str]], columns: dict[str, str]) -> dict[str, str]:
    rows = sorted(rows, key=lambda row: completeness(row, columns), reverse=True)
    merged = {name: row_value(rows[0], columns, name) for name in ALIASES}
    for name in ALIASES:
        if not merged[name]:
            merged[name] = next((row_value(row, columns, name) for row in rows if row_value(row, columns, name)), "")
    sources = sorted({row_value(row, columns, "source") for row in rows if row_value(row, columns, "source")})
    dates = sorted({row_value(row, columns, "retrieved_at") for row in rows if row_value(row, columns, "retrieved_at")})
    merged["source"] = " | ".join(sources)
    merged["retrieved_at"] = " | ".join(dates)
    merged["normalized_keyword"] = normalized_keyword(merged["keyword"])
    merged["duplicate_rows_merged"] = str(len(rows))
    return merged


def clamp(value: float, low: float = 0, high: float = 100) -> float:
    return max(low, min(high, value))


def add_scores(rows: list[dict[str, str]]) -> None:
    volumes = [parse_number(row["volume"]) for row in rows]
    positive = [value for value in volumes if value is not None and value >= 0]
    max_log = max((math.log1p(value) for value in positive), default=0)

    for row in rows:
        components: list[tuple[float, float]] = []
        volume = parse_number(row["volume"])
        if volume is not None and max_log > 0:
            components.append((0.30, 100 * math.log1p(max(volume, 0)) / max_log))
        business_value = parse_number(row["business_value"])
        if business_value is not None:
            components.append((0.30, clamp(business_value / 3 * 100)))
        kd = parse_number(row["kd"])
        if kd is not None:
            components.append((0.20, 100 - clamp(kd)))
        current_gap = parse_number(row["current_gap"])
        if current_gap is not None:
            components.append((0.10, clamp(current_gap)))
        strategic_fit = parse_number(row["strategic_fit"])
        if strategic_fit is not None:
            components.append((0.10, clamp(strategic_fit / 3 * 100 if strategic_fit <= 3 else strategic_fit)))

        available_weight = sum(weight for weight, _ in components)
        if not components:
            row["priority_score"] = ""
            row["score_status"] = "not scored: no numeric inputs"
            continue
        score = sum(weight * value for weight, value in components) / available_weight
        row["priority_score"] = f"{score:.1f}"
        row["score_status"] = "complete" if abs(available_weight - 1.0) < 0.001 else f"partial: {available_weight:.0%} weight available"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("output_csv", type=Path)
    args = parser.parse_args()

    with args.input_csv.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            print("ERROR: input has no header", file=sys.stderr)
            return 2
        columns = find_columns(reader.fieldnames)
        if "keyword" not in columns:
            print("ERROR: expected a keyword/query/term column", file=sys.stderr)
            return 2
        source_rows = list(reader)

    grouped: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    skipped = 0
    for row in source_rows:
        keyword = row_value(row, columns, "keyword")
        if not keyword:
            skipped += 1
            continue
        key = (
            normalized_keyword(keyword),
            row_value(row, columns, "country").casefold(),
            row_value(row, columns, "language").casefold(),
        )
        grouped[key].append(row)

    output = [merge_group(rows, columns) for rows in grouped.values()]
    for row in output:
        for numeric in ("volume", "kd", "cpc", "business_value", "strategic_fit", "current_gap"):
            row[numeric] = display_number(parse_number(row[numeric]))
    add_scores(output)
    def sort_key(row: dict[str, str]) -> tuple[float, str]:
        score = parse_number(row["priority_score"])
        return (-(score if score is not None else -1), row["normalized_keyword"])

    output.sort(key=sort_key)

    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {len(output)} unique keywords; merged {len(source_rows) - skipped - len(output)} duplicates; skipped {skipped} blank rows.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
