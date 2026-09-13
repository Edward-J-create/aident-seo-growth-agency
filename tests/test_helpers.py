"""Synthetic, offline regression tests. No accounts or SEO providers are contacted."""

from __future__ import annotations

import csv
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


keywords = module("normalize_keywords")
builder = module("build_standalone_report")


class KeywordTests(unittest.TestCase):
    def test_numbers_preserve_missing_and_zero(self):
        for value in ("", "N/A", "null", "-", "nan", "Infinity"):
            self.assertIsNone(keywords.parse_number(value), value)
        self.assertEqual(keywords.parse_number("0"), 0)
        self.assertEqual(keywords.parse_number("1.2k"), 1200)

    def test_missing_metrics_are_not_zero_scores(self):
        row = {name: "" for name in keywords.ALIASES}
        keywords.add_scores([row])
        self.assertEqual(row["priority_score"], "")
        self.assertIn("not scored", row["score_status"])
        row["kd"] = "100"
        keywords.add_scores([row])
        self.assertEqual(row["priority_score"], "0.0")
        self.assertIn("partial", row["score_status"])

    def test_cli_merges_duplicates_but_not_markets(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.csv"
            out = Path(directory) / "out.csv"
            source.write_text(
                "keyword,country,language,volume,source\n"
                "Example term,US,en,,synthetic\n"
                " example   TERM ,US,en,0,synthetic\n"
                "Example term,GB,en,,synthetic\n",
                encoding="utf-8",
            )
            result = subprocess.run([sys.executable, str(ROOT / "scripts/normalize_keywords.py"), str(source), str(out)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            with out.open(encoding="utf-8", newline="") as handle:
                rows = {row["country"]: row for row in csv.DictReader(handle)}
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows["US"]["duplicate_rows_merged"], "2")
            self.assertEqual(rows["US"]["volume"], "0")
            self.assertEqual(rows["GB"]["volume"], "")


class PageMapTests(unittest.TestCase):
    def run_map(self, rows):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "pages.csv"
            source.write_text("page_id,page_type,proposed_url,primary_keyword,phase,status,parent_id,h1\n" + rows, encoding="utf-8")
            return subprocess.run([sys.executable, str(ROOT / "scripts/validate_page_map.py"), str(source)], capture_output=True, text=True)

    def test_valid_map(self):
        result = self.run_map("home,home,https://example.com/,brand,P0,keep,,Brand\nproduct,product,https://example.com/product,product,P1,create,home,Product\n")
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_duplicate_ownership_is_rejected(self):
        result = self.run_map("one,page,https://example.com/one,term,P0,keep,,One\ntwo,page,https://example.com/two,TERM,P1,create,,Two\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("primary keyword", result.stdout)

    def test_missing_parent_is_rejected(self):
        result = self.run_map("one,page,https://example.com/one,term,P0,keep,absent,One\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("does not exist", result.stdout)

    def test_redirect_requires_destination_note(self):
        result = self.run_map("old,page,https://example.com/old,term,P0,redirect,,Old\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("canonical_or_redirect_note", result.stdout)


class StandaloneTests(unittest.TestCase):
    def test_embed_local_asset_and_preserve_citation(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            (base / "shape.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg"/>', encoding="utf-8")
            html = '<img src="shape.svg"><a href="https://example.com/source">Source</a>'
            rendered, embedded = builder.inline_assets(html, base)
            self.assertIn("data:image/svg+xml;base64,", rendered)
            self.assertIn('href="https://example.com/source"', rendered)
            self.assertEqual(len(embedded), 1)

    def test_remote_assets_rejected(self):
        with self.assertRaises(ValueError):
            builder.inline_assets('<img src="https://example.com/image.png">', ROOT)

    def test_skill_asset_traversal_rejected(self):
        with self.assertRaises(ValueError):
            builder.resolve_asset("skill-asset://../SKILL.md", ROOT)

    def test_bad_tab_mapping_fails_report_validator(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "broken.html"
            path.write_text('<html><head><title>Test</title><meta name="description" content="Synthetic test"></head><body><button id="tab-a" role="tab" aria-controls="missing" aria-selected="true">A</button><section id="panel-a" role="tabpanel" aria-labelledby="tab-a"></section><script>void 0;</script></body></html>', encoding="utf-8")
            result = subprocess.run([sys.executable, str(ROOT / "scripts/validate_html_report.py"), str(path)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("mapping mismatch", result.stdout)


if __name__ == "__main__":
    unittest.main()
