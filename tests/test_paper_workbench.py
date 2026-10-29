"""Portable standard-library tests. All fixtures are SYNTHETIC, not real literature.

Set BATTERY_SKILL_DIR to the skill directory, or place the skill at a parent
directory's battery-paper-skill/ path. Temporary fixtures stay beside this file.
No network or package installation is used. No scientific claims are validated.
"""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True


def find_script():
    configured = os.environ.get("BATTERY_SKILL_DIR")
    if configured:
        candidate = Path(configured) / "scripts" / "paper_workbench.py"
        if candidate.is_file():
            return candidate
        raise RuntimeError("BATTERY_SKILL_DIR must contain scripts/paper_workbench.py")
    for parent in Path(__file__).resolve().parents:
        for relative in ("battery-paper-skill/scripts/paper_workbench.py", "scripts/paper_workbench.py"):
            candidate = parent / relative
            if candidate.is_file():
                return candidate
    raise RuntimeError("Set BATTERY_SKILL_DIR or place battery-paper-skill beside the repository tests")


SCRIPT = find_script()
SPEC = importlib.util.spec_from_file_location("synthetic_battery_workbench", SCRIPT)
WORKBENCH = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(WORKBENCH)
AS_OF = "2026-10-29"


def synthetic_source(number=1, **updates):
    """A fabricated record solely for structural tests; it is not a real paper."""
    item = {
        "source_id": f"SYNTHETIC-SRC-{number:03}",
        "unique_work_id": f"synthetic-not-real-work-{number:03}",
        "title": f"SYNTHETIC TEST RECORD {number}; not real literature",
        "source_type": "primary_research", "bibliographic_status": "verified",
        "publication_date": "2025-06-01", "publication_date_verified": True,
        "date_source_url": "https://example.invalid/synthetic-not-real-literature",
        "date_basis": "publisher_first_online", "topical_fit": "direct",
        "fit_reason": "Synthetic fixture only; no scientific fit is claimed",
        "read_scope": ["relevant_body"], "exact_locations": ["SYNTHETIC section 1"],
        "chinese_meaning": "合成测试记录，不代表真实阅读或文献",
        "source_paragraph_move": "SYNTHETIC argument move",
        "source_data_expression": "SYNTHETIC expression; no real data",
        "tags": ["synthetic"], "linked_figure_tasks": ["SYNTHETIC-FIG-1"],
    }
    item.update(updates)
    return item


class WorkbenchTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="synthetic_battery_", dir=Path(__file__).resolve().parent)
        self.root = Path(self.temp.name)
        self.project = self.root / "synthetic_project_not_real_research"
        self.project.mkdir()
        self.context = self.project / ".paper-writing"
        code, payload = self.cli("init", "--project-dir", self.project, "--name", "SYNTHETIC PROJECT ONLY")
        self.assertEqual(code, 0, payload)

    def tearDown(self):
        self.temp.cleanup()

    def cli(self, *arguments):
        env = dict(os.environ, PYTHONUTF8="1", PYTHONDONTWRITEBYTECODE="1")
        result = subprocess.run([sys.executable, "-X", "utf8", str(SCRIPT), *map(str, arguments)],
                                capture_output=True, text=True, encoding="utf-8", env=env, cwd=self.root)
        stream = result.stdout.strip() or result.stderr.strip()
        try:
            payload = json.loads(stream)
        except ValueError:
            payload = {"raw": stream}
        return result.returncode, payload

    def load(self, filename):
        return json.loads((self.context / filename).read_text(encoding="utf-8"))

    def save(self, filename, payload):
        (self.context / filename).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    def save_sources(self, items):
        self.save("sources.json", {"schema_version": 1, "items": items})

    def corpus(self):
        code, payload = self.cli("corpus", "--project-dir", self.project, "--as-of", AS_OF)
        self.assertEqual(code, 0, payload)
        return payload

    def prepare_delivery(self):
        self.save("evidence.json", {"schema_version": 1, "items": [
            {"evidence_id": "SYNTHETIC-EV-1", "observation": "Fabricated test observation only"},
            {"evidence_id": "SYNTHETIC-EV-2", "observation": "Fabricated test observation only"},
        ]})
        self.save_sources([synthetic_source(1), synthetic_source(2)])
        return {
            "schema_version": 1,
            "sentences": [
                {"sentence_id": "SYNTHETIC-S2", "paragraph_id": "SYNTHETIC-P1", "order": 2,
                 "text": "Second synthetic sentence.", "evidence_ids": ["SYNTHETIC-EV-1", "SYNTHETIC-EV-2"],
                 "source_ids": ["SYNTHETIC-SRC-001", "SYNTHETIC-SRC-002"]},
                {"sentence_id": "SYNTHETIC-S1", "paragraph_id": "SYNTHETIC-P1", "order": 1,
                 "text": "First synthetic sentence. ", "evidence_ids": ["SYNTHETIC-EV-1"],
                 "source_ids": ["SYNTHETIC-SRC-001"]},
                {"sentence_id": "SYNTHETIC-S3", "paragraph_id": "SYNTHETIC-P2", "order": 1,
                 "text": "合成观察。", "evidence_ids": ["SYNTHETIC-EV-2"],
                 "source_ids": [], "basis": "own_observation"},
            ],
            "paragraphs": [
                {"paragraph_id": "SYNTHETIC-P1", "text": "First synthetic sentence. Second synthetic sentence."},
                {"paragraph_id": "SYNTHETIC-P2", "text": "合成观察。"},
            ],
            "propositions": [{"proposition_id": "SYNTHETIC-PROP-1", "text": "Human review fixture only"}],
        }

    def check_delivery(self, payload):
        path = self.root / "synthetic_delivery.json"
        path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        return self.cli("delivery-check", "--project-dir", self.project, "--file", path)

    def snapshot(self):
        return {str(path.relative_to(self.project)): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in self.project.rglob("*") if path.is_file()}

    def test_init_is_empty_and_has_explicit_60_policy(self):
        self.assertEqual(self.load("project.json")["corpus_policy"], {"minimum": 60, "target": 60, "recent_years": 5})
        self.assertEqual(self.load("evidence.json")["items"], [])
        self.assertEqual(self.load("sources.json")["items"], [])
        self.assertEqual(set(path.name for path in self.context.iterdir()),
                         {"project.json", "evidence.json", "sources.json", "decisions.md", "issues.md", "drafts"})
        combined = "\n".join(path.read_text(encoding="utf-8") for path in self.context.iterdir() if path.is_file())
        self.assertNotIn("publication_date", combined)
        self.assertNotIn("SYNTHETIC-SRC", combined)
        self.assertNotIn("10.", combined)

    def test_init_preserves_every_existing_file_and_old_policy(self):
        project = self.load("project.json")
        project["corpus_policy"] = {"minimum": 50, "target": 60, "recent_years": 5}
        self.save("project.json", project)
        self.save_sources([synthetic_source()])
        (self.context / "drafts" / "synthetic_accepted.txt").write_text("KEEP EXACT SYNTHETIC TEXT", encoding="utf-8")
        before = self.snapshot()
        code, result = self.cli("init", "--project-dir", self.project, "--name", "DO NOT REPLACE")
        self.assertEqual(code, 0)
        self.assertEqual(result["created"], [])
        self.assertTrue(result["needs_policy_update"])
        self.assertEqual(result["policy_status"], "needs_policy_update")
        self.assertEqual(self.snapshot(), before)

    def test_init_only_adds_a_missing_file(self):
        (self.context / "issues.md").unlink()
        before = self.snapshot()
        code, result = self.cli("init", "--project-dir", self.project, "--name", "DO NOT REPLACE")
        self.assertEqual(code, 0)
        self.assertEqual(result["created"], ["issues.md"])
        after = self.snapshot()
        self.assertTrue(all(after[key] == value for key, value in before.items()))

    def test_no_implicit_current_project_or_as_of(self):
        for arguments in (("init", "--name", "SYNTHETIC"),
                          ("corpus", "--project-dir", self.project),
                          ("sources", "--project-dir", self.project, "--query", "synthetic")):
            self.assertEqual(self.cli(*arguments)[0], 2)
        with self.assertRaises(ValueError):
            WORKBENCH.window_for(None)
        with self.assertRaises(ValueError):
            WORKBENCH.window_for("20261029")

    def test_59_is_incomplete_and_60_meets_record_threshold(self):
        self.save_sources([synthetic_source(number) for number in range(1, 60)])
        first = self.corpus()
        self.assertEqual((first["qualified_read_baseline"], first["gap_to_minimum"], first["status"]),
                         (59, 1, "baseline_incomplete"))
        self.save_sources([synthetic_source(number) for number in range(1, 61)])
        second = self.corpus()
        self.assertEqual((second["qualified_read_baseline"], second["gap_to_minimum"], second["status"]),
                         (60, 0, "target_met_by_record"))

    def test_old_50_policy_is_reported_not_implicitly_upgraded(self):
        project = self.load("project.json")
        project["corpus_policy"]["minimum"] = 50
        self.save("project.json", project)
        self.save_sources([synthetic_source(number) for number in range(1, 51)])
        before = self.snapshot()
        result = self.corpus()
        self.assertEqual(result["status"], "needs_policy_update")
        self.assertEqual(result["recorded_policy"]["minimum"], 50)
        self.assertEqual(result["gap_to_minimum"], 10)
        for command in ("status", "check"):
            code, payload = self.cli(command, "--project-dir", self.project)
            self.assertEqual(code, 0)
            self.assertTrue(payload["needs_policy_update"])
        self.assertEqual(self.snapshot(), before)

    def test_missing_policy_is_reported(self):
        project = self.load("project.json")
        project.pop("corpus_policy")
        self.save("project.json", project)
        self.assertEqual(self.corpus()["status"], "needs_policy_update")

    def test_exact_rolling_boundaries_future_and_precision(self):
        first, last = WORKBENCH.window_for(AS_OF)
        self.assertEqual((first.isoformat(), last.isoformat()), ("2021-10-29", AS_OF))
        cases = {
            "2021-10-28": "outside_window", "2021-10-29": "within_window",
            "2026-10-29": "within_window", "2026-10-30": "future_publication",
            "2021-10": "needs_date_verification", "2021": "needs_date_verification",
            "2026-10": "needs_date_verification", "2026": "needs_date_verification",
            "2022": "within_window", "2026-09": "within_window",
            "2027": "future_publication", "2020": "outside_window",
            "2026-02-30": "date_unknown", "unknown": "date_unknown",
        }
        for token, expected in cases.items():
            with self.subTest(date=token):
                self.assertEqual(WORKBENCH.recency_status({"publication_date": token}, first, last)["status"], expected)
        self.assertEqual(WORKBENCH.window_for("2024-02-29")[0].isoformat(), "2019-02-28")

    def test_date_source_and_formal_basis_are_required(self):
        self.save_sources([
            synthetic_source(1, publication_date_verified=False),
            synthetic_source(2, date_source_url=""),
            synthetic_source(3, date_basis="synthetic_unverified_year"),
            synthetic_source(4, publication_date="2026-10-30"),
            synthetic_source(5, publication_date="2021-10-28"),
            synthetic_source(6, publication_date="2021-10"),
            synthetic_source(7, publication_date="2021-10-29"),
        ])
        self.assertEqual(self.corpus()["qualified_read_baseline"], 1)

    def test_duplicate_doi_normalization_counts_once_and_check_flags_it(self):
        # Deliberately fabricated DOI strings; these are not real publications.
        self.save_sources([
            synthetic_source(1, doi="https://doi.org/10.99999/SYNTHETIC-NOT-A-REAL-PAPER"),
            synthetic_source(2, doi="doi: 10.99999/synthetic-not-a-real-paper."),
        ])
        result = self.corpus()
        self.assertEqual((result["qualified_read_baseline"], result["duplicate_identity_records"]), (1, 1))
        self.assertTrue(result["records"][1]["duplicate_qualified_record"])
        code, result = self.cli("check", "--project-dir", self.project)
        self.assertEqual(code, 1)
        self.assertTrue(any("duplicate DOI" in item for item in result["errors"]))

    def test_abstracts_legacy_cards_and_old_seed_count_cannot_qualify(self):
        items = [synthetic_source(1, read_scope=["abstract_only"]),
                 synthetic_source(2, read_scope=["secondary_card"]),
                 synthetic_source(3, read_scope=["seed_index"]),
                 synthetic_source(4, source_type="review"),
                 synthetic_source(5, bibliographic_status="unverified"),
                 synthetic_source(6, publication_role="preprint")]
        legacy = synthetic_source(7)
        legacy["prior_read_scope"] = ["full_main_text"]
        legacy.pop("read_scope")
        items.append(legacy)
        self.save_sources(items)
        self.assertEqual(self.corpus()["qualified_read_baseline"], 0)
        self.save_sources([])
        result = self.corpus()
        self.assertEqual((result["qualified_read_baseline"], result["gap_to_minimum"]), (0, 60))

    def test_sources_searches_project_records_and_respects_client_window(self):
        self.save_sources([synthetic_source(1), synthetic_source(2, publication_date="2020-01-01")])
        code, result = self.cli("sources", "--project-dir", self.project, "--query", "synthetic", "--as-of", AS_OF)
        self.assertEqual(code, 0)
        self.assertEqual((result["index"], result["matches"]), (".paper-writing/sources.json", 1))
        code, result = self.cli("sources", "--project-dir", self.project, "--query", "synthetic", "--as-of", AS_OF, "--include-legacy")
        self.assertEqual(code, 0)
        self.assertEqual(result["matches"], 2)

    def test_check_is_read_only_and_disclaims_scientific_validation(self):
        (self.project / "synthetic_manuscript.txt").write_text("Synthetic manuscript must stay exact.  ", encoding="utf-8")
        before = self.snapshot()
        code, result = self.cli("check", "--project-dir", self.project)
        self.assertEqual(code, 0)
        self.assertTrue(result["ok"])
        self.assertIn("不判断", result["note"])
        self.assertEqual(self.snapshot(), before)

    def test_check_detects_duplicate_evidence_and_source_ids(self):
        self.save("evidence.json", {"items": [{"evidence_id": "SYNTHETIC-E1"}, {"evidence_id": "SYNTHETIC-E1"}]})
        self.save_sources([synthetic_source(1), synthetic_source(2, source_id="SYNTHETIC-SRC-001")])
        code, result = self.cli("check", "--project-dir", self.project)
        self.assertEqual(code, 1)
        self.assertTrue(any("duplicate evidence_id" in error for error in result["errors"]))
        self.assertTrue(any("duplicate source_id" in error for error in result["errors"]))

    def test_count_preserves_explicit_region_and_counts_only_that_region(self):
        path = self.root / "synthetic_count.txt"
        path.write_text("excluded\n<START>中文 ABC 12.<END>excluded", encoding="utf-8")
        code, result = self.cli("count", "--file", path, "--start-marker", "<START>", "--end-marker", "<END>")
        self.assertEqual(code, 0)
        self.assertEqual((result["han_characters"], result["english_lexical_words"]), (2, 1))
        self.assertEqual(result["selected_text_sha256"], hashlib.sha256("中文 ABC 12.".encode()).hexdigest())

    def test_delivery_orders_final_text_exactly_and_allows_many_to_many(self):
        payload = self.prepare_delivery()
        before = self.snapshot()
        code, result = self.check_delivery(payload)
        self.assertEqual(code, 0, result)
        self.assertTrue(result["ok"])
        self.assertTrue(all(row["exact_match"] for row in result["comparisons"]))
        self.assertTrue(any("human review" in item for item in result["warnings"]))
        self.assertEqual(self.snapshot(), before)

    def test_delivery_detects_punctuation_and_internal_space_misalignment(self):
        original = self.prepare_delivery()
        for replacement in ("First synthetic sentence! Second synthetic sentence.",
                            "First synthetic sentence.  Second synthetic sentence.",
                            "First synthetic sentence.Second synthetic sentence."):
            payload = copy.deepcopy(original)
            payload["paragraphs"][0]["text"] = replacement
            code, result = self.check_delivery(payload)
            self.assertEqual(code, 1)
            self.assertFalse(result["comparisons"][0]["exact_match"])
            self.assertIsNotNone(result["comparisons"][0]["first_difference_index_zero_based"])

    def test_delivery_detects_stale_sentence_table_or_wrong_paragraph(self):
        original = self.prepare_delivery()
        for mutation in ("stale", "paragraph", "omitted"):
            payload = copy.deepcopy(original)
            if mutation == "stale":
                payload["sentences"][0]["text"] = "Stale synthetic text."
            elif mutation == "paragraph":
                payload["sentences"][0]["paragraph_id"] = "SYNTHETIC-P2"
            else:
                payload["sentences"].pop()
            self.assertEqual(self.check_delivery(payload)[0], 1)

    def test_delivery_requires_unique_stable_sentence_ids_and_orders(self):
        original = self.prepare_delivery()
        for mutation in ("duplicate_id", "empty_id", "spaced_id", "duplicate_order", "bad_order"):
            payload = copy.deepcopy(original)
            if mutation == "duplicate_id":
                payload["sentences"][0]["sentence_id"] = "SYNTHETIC-S1"
            elif mutation == "empty_id":
                payload["sentences"][0]["sentence_id"] = ""
            elif mutation == "spaced_id":
                payload["sentences"][0]["sentence_id"] = "SYNTHETIC S2"
            elif mutation == "duplicate_order":
                payload["sentences"][0]["order"] = 1
            else:
                payload["sentences"][0]["order"] = True
            self.assertEqual(self.check_delivery(payload)[0], 1)

    def test_delivery_requires_existing_evidence_and_source_ids(self):
        original = self.prepare_delivery()
        for key in ("evidence_ids", "source_ids"):
            payload = copy.deepcopy(original)
            payload["sentences"][0][key] = ["SYNTHETIC-UNKNOWN-ID"]
            code, result = self.check_delivery(payload)
            self.assertEqual(code, 1)
            self.assertTrue(any("unknown " + key in error for error in result["errors"]))

    def test_delivery_empty_source_basis_and_accepted_record_reference(self):
        original = self.prepare_delivery()
        for basis in ("own_observation", "author_transition", "retained_accepted"):
            payload = copy.deepcopy(original)
            payload["sentences"][2]["basis"] = basis
            if basis == "retained_accepted":
                self.assertEqual(self.check_delivery(payload)[0], 1)
                payload["sentences"][2]["basis_ref"] = "SYNTHETIC accepted record, version 1; not a real acceptance"
            self.assertEqual(self.check_delivery(payload)[0], 0)
        for bad_basis in (None, "literature_guess", ""):
            payload = copy.deepcopy(original)
            payload["sentences"][2]["basis"] = bad_basis
            self.assertEqual(self.check_delivery(payload)[0], 1)

    def test_delivery_unnamed_or_orphan_paragraph_is_detected(self):
        original = self.prepare_delivery()
        payload = copy.deepcopy(original)
        payload["sentences"][0]["paragraph_id"] = "SYNTHETIC-UNKNOWN-P"
        self.assertEqual(self.check_delivery(payload)[0], 1)
        payload = copy.deepcopy(original)
        payload["paragraphs"].append({"paragraph_id": "SYNTHETIC-ORPHAN", "text": "Unmapped synthetic paragraph."})
        self.assertEqual(self.check_delivery(payload)[0], 1)


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(WorkbenchTest)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    summary = {
        "fixture_notice": "All fixtures are SYNTHETIC; no real literature, project facts, or scientific validation.",
        "runner": "Python standard-library unittest; no installed dependencies or network",
        "tests_run": result.testsRun, "failures": len(result.failures), "errors": len(result.errors),
        "successful": result.wasSuccessful(),
        "command_template": "BATTERY_SKILL_DIR=<skill-dir> python -X utf8 test_paper_workbench.py",
    }
    (Path(__file__).resolve().parent / "test_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    raise SystemExit(0 if result.wasSuccessful() else 1)
