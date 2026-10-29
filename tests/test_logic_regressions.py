"""Portable regressions from independent SYNTHETIC-only logic probes.

No real sources, scientific facts, network, or external packages are involved.
Run alongside test_paper_workbench.py with standard-library unittest discovery.
BATTERY_SKILL_DIR may select the skill-under-test; no machine paths are embedded.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

import test_paper_workbench as original

sys.dont_write_bytecode = True
SCRIPT = original.SCRIPT
SPEC = importlib.util.spec_from_file_location("synthetic_regression_workbench", SCRIPT)
WORKBENCH = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(WORKBENCH)
AS_OF = original.AS_OF
synthetic_source = original.synthetic_source


class LogicRegressionTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="synthetic_logic_", dir=Path(__file__).resolve().parent)
        self.root = Path(self.temp.name)
        self.project = self.root / "synthetic_project_not_real_research"
        self.project.mkdir()
        self.context = self.project / ".paper-writing"
        code, payload = self.cli("init", "--project-dir", self.project, "--name", "SYNTHETIC LOGIC REGRESSION")
        self.assertEqual(code, 0, payload)

    def tearDown(self):
        self.temp.cleanup()

    cli = original.WorkbenchTest.cli
    load = original.WorkbenchTest.load
    save = original.WorkbenchTest.save
    save_sources = original.WorkbenchTest.save_sources
    check_delivery = original.WorkbenchTest.check_delivery
    prepare_delivery = original.WorkbenchTest.prepare_delivery
    snapshot = original.WorkbenchTest.snapshot

    def corpus(self):
        return self.cli("corpus", "--project-dir", self.project, "--as-of", AS_OF)

    def policy(self, minimum, target, years, marker=None):
        project = self.load("project.json")
        project["corpus_policy"] = {"minimum": minimum, "target": target, "recent_years": years}
        if marker is not None:
            project["corpus_policy_override"] = marker
        self.save("project.json", project)

    def test_doi_and_work_id_aliases_count_once(self):
        self.save_sources([
            synthetic_source(1, unique_work_id="SYNTHETIC-SAME-WORK", doi="10.99999/synthetic-alias"),
            synthetic_source(2, unique_work_id="SYNTHETIC-SAME-WORK"),
        ])
        code, payload = self.corpus()
        self.assertEqual(code, 0, payload)
        self.assertEqual(payload["qualified_read_baseline"], 1)
        self.assertEqual(payload["duplicate_identity_records"], 1)
        self.assertEqual(payload["records"][0]["identity"], payload["records"][1]["identity"])

    def test_thirty_doi_alias_pairs_do_not_meet_sixty(self):
        items = []
        for number in range(1, 31):
            work = f"SYNTHETIC-WORK-{number}"
            items.extend([synthetic_source(number, unique_work_id=work, doi=f"10.99999/synthetic-{number}"),
                          synthetic_source(number + 30, unique_work_id=work)])
        self.save_sources(items)
        code, payload = self.corpus()
        self.assertEqual(code, 0, payload)
        self.assertEqual((payload["qualified_read_baseline"], payload["gap_to_minimum"]), (30, 30))
        self.assertEqual(payload["status"], "baseline_incomplete")

    def test_alias_aggregation_is_transitive_and_order_independent(self):
        rows = [synthetic_source(1, unique_work_id="SYNTHETIC-WORK-A", doi="10.99999/synthetic-a"),
                synthetic_source(2, unique_work_id="SYNTHETIC-WORK-A", doi="10.99999/synthetic-b"),
                synthetic_source(3, unique_work_id="SYNTHETIC-WORK-B", doi="10.99999/synthetic-b")]
        for records in (rows, list(reversed(rows))):
            self.save_sources(records)
            code, payload = self.corpus()
            self.assertEqual(code, 0, payload)
            self.assertEqual(payload["qualified_read_baseline"], 1)

    def test_duplicate_source_id_cannot_return_target_met(self):
        self.save_sources([synthetic_source(n, source_id="SYNTHETIC-DUPLICATE") for n in range(1, 61)])
        code, payload = self.corpus()
        self.assertEqual(code, 1, payload)
        self.assertEqual(payload["status"], "structure_errors")
        self.assertEqual(payload["baseline_status"], "structure_errors")
        self.assertFalse(payload["record_structure_ok"])
        self.assertTrue(any("duplicate source_id" in error for error in payload["errors"]))

    def test_blank_required_reading_fields_never_qualify(self):
        self.save_sources([synthetic_source(n, fit_reason=" \t", exact_locations=[" "],
                           chinese_meaning="\n", source_paragraph_move=" ", source_data_expression="\t")
                           for n in range(1, 61)])
        code, payload = self.corpus()
        self.assertEqual(code, 1, payload)
        self.assertEqual(payload["qualified_read_baseline"], 0)
        self.assertNotEqual(payload["status"], "target_met_by_record")
        self.assertIn("missing_exact_locations", payload["records"][0]["reasons"])

    def test_wrong_type_required_reading_fields_never_qualify(self):
        self.save_sources([synthetic_source(fit_reason=True, exact_locations=[None], chinese_meaning=1,
                                           source_paragraph_move=True, source_data_expression={"synthetic": 1})])
        code, payload = self.corpus()
        self.assertEqual(code, 1, payload)
        self.assertEqual(payload["qualified_read_baseline"], 0)
        self.assertGreaterEqual(len(payload["errors"]), 5)

    def test_missing_reading_fields_are_incomplete_without_corrupting_search_cards(self):
        row = synthetic_source()
        for key in ("exact_locations", "chinese_meaning", "source_paragraph_move", "source_data_expression"):
            row.pop(key)
        self.save_sources([row])
        code, payload = self.corpus()
        self.assertEqual(code, 0, payload)
        self.assertEqual(payload["qualified_read_baseline"], 0)

    def test_locations_support_text_or_nonempty_text_array(self):
        for locations in ("SYNTHETIC section 1", ["SYNTHETIC section 1", "SYNTHETIC figure 2"]):
            self.save_sources([synthetic_source(exact_locations=locations)])
            code, payload = self.corpus()
            self.assertEqual(code, 0, payload)
            self.assertEqual(payload["qualified_read_baseline"], 1)

    def test_unique_work_id_must_be_nonempty_string_even_with_doi(self):
        for value in (" ", 1, True, {"synthetic": 1}, ["synthetic"]):
            self.save_sources([synthetic_source(unique_work_id=value, doi="10.99999/synthetic")])
            code, payload = self.corpus()
            self.assertEqual(code, 1, payload)
            self.assertEqual(payload["qualified_read_baseline"], 0)
            self.assertIn("invalid_unique_work_id", payload["records"][0]["reasons"])

    def test_valid_doi_may_identify_work_without_optional_work_id(self):
        row = synthetic_source(doi="10.99999/synthetic-doi-only")
        row.pop("unique_work_id")
        self.save_sources([row])
        code, payload = self.corpus()
        self.assertEqual(code, 0, payload)
        self.assertEqual(payload["qualified_read_baseline"], 1)

    def test_figure_task_ids_are_never_string_coerced(self):
        project = self.load("project.json")
        project["required_figure_tasks"] = ["1"]
        self.save("project.json", project)
        for task in (1, True, {"id": "1"}, " ", ""):
            self.save_sources([synthetic_source(linked_figure_tasks=[task])])
            code, payload = self.corpus()
            self.assertEqual(code, 1, payload)
            self.assertNotEqual(payload["figure_mapping"]["status"], "complete_by_record")
            self.assertEqual(payload["figure_mapping"]["missing"], ["1"])

    def test_required_figure_task_types_are_checked_in_check_and_corpus(self):
        for value in ("SYNTHETIC-F1", [1], [""], [{"id": "SYNTHETIC-F1"}]):
            project = self.load("project.json")
            project["required_figure_tasks"] = value
            self.save("project.json", project)
            for command in ("check", "corpus"):
                args = [command, "--project-dir", self.project]
                if command == "corpus":
                    args += ["--as-of", AS_OF]
                code, payload = self.cli(*args)
                self.assertEqual(code, 1, payload)
                self.assertTrue(any("required_figure_tasks" in error for error in payload["errors"]))

    def test_valid_figure_task_mapping_still_works(self):
        project = self.load("project.json")
        project["required_figure_tasks"] = ["SYNTHETIC-FIG-1"]
        self.save("project.json", project)
        self.save_sources([synthetic_source()])
        code, payload = self.corpus()
        self.assertEqual(code, 0, payload)
        self.assertEqual(payload["figure_mapping"]["status"], "complete_by_record")

    def test_check_rejects_wrong_project_field_types(self):
        project = self.load("project.json")
        project.update(schema_version=True, project_name=[], domain=False)
        self.save("project.json", project)
        code, payload = self.cli("check", "--project-dir", self.project)
        self.assertEqual(code, 1, payload)
        self.assertTrue(all(any(key in error for error in payload["errors"])
                            for key in ("schema_version", "project_name", "domain")))

    def test_whitespace_only_paragraph_is_rejected(self):
        payload = self.prepare_delivery()
        payload["sentences"] = [dict(payload["sentences"][0], text=" \t\n", order=1)]
        payload["paragraphs"] = [{"paragraph_id": "SYNTHETIC-P1", "text": " \t\n"}]
        code, result = self.check_delivery(payload)
        self.assertEqual(code, 1, result)
        self.assertFalse(result["ok"])

    def test_actual_edge_spaces_are_preserved_and_checked(self):
        payload = self.prepare_delivery()
        payload["sentences"][1]["text"] = " " + payload["sentences"][1]["text"]
        payload["paragraphs"][0]["text"] = " " + payload["paragraphs"][0]["text"]
        self.assertEqual(self.check_delivery(payload)[0], 0)
        payload["paragraphs"][0]["text"] = payload["paragraphs"][0]["text"].lstrip()
        self.assertEqual(self.check_delivery(payload)[0], 1)

    def test_author_and_calculation_bases_work_with_known_evidence(self):
        for basis in ("own_observation", "author_provided", "author_confirmed", "own_calculation"):
            payload = self.prepare_delivery()
            payload["sentences"][2]["basis"] = basis
            code, result = self.check_delivery(payload)
            self.assertEqual(code, 0, result)

    def test_observation_author_calculation_bases_require_valid_evidence(self):
        for basis in ("own_observation", "author_provided", "author_confirmed", "own_calculation"):
            for refs in ([], ["SYNTHETIC-UNKNOWN"], [" "], None):
                payload = self.prepare_delivery()
                payload["sentences"][2].update(basis=basis, evidence_ids=refs)
                code, result = self.check_delivery(payload)
                self.assertEqual(code, 1, result)
                self.assertTrue(any("evidence_ids" in error for error in result["errors"]))

    def test_transition_may_have_no_evidence_or_sources(self):
        payload = self.prepare_delivery()
        payload["sentences"][2].update(basis="author_transition", source_ids=[], evidence_ids=[])
        self.assertEqual(self.check_delivery(payload)[0], 0)

    def test_retained_accepted_keeps_basis_ref_requirement(self):
        payload = self.prepare_delivery()
        payload["sentences"][2].update(basis="retained_accepted", source_ids=[], evidence_ids=[])
        self.assertEqual(self.check_delivery(payload)[0], 1)
        payload["sentences"][2]["basis_ref"] = "SYNTHETIC acceptance locator only; not a real acceptance"
        self.assertEqual(self.check_delivery(payload)[0], 0)

    def test_authorized_custom_policy_80_uses_20_work_gap_at_60(self):
        self.policy(80, 80, 5, {"authorized_by": "user", "decision_ref": "SYNTHETIC author decision 1"})
        self.save_sources([synthetic_source(n) for n in range(1, 61)])
        before = self.snapshot()
        code, payload = self.corpus()
        self.assertEqual(code, 0, payload)
        self.assertEqual((payload["gap_to_minimum"], payload["gap_to_target"]), (20, 20))
        self.assertEqual(payload["status"], "baseline_incomplete")
        self.assertEqual(payload["effective_policy_source"], "authorized_user_override")
        self.assertEqual(payload["default_policy"]["minimum"], 60)
        self.assertEqual(payload["effective_policy"]["minimum"], 80)
        self.assertFalse(payload["needs_policy_update"])
        self.assertEqual(self.snapshot(), before)

    def test_authorized_lower_policy_can_meet_its_explicit_threshold(self):
        self.policy(2, 2, 5, {"authorized_by": "user", "decision_ref": "SYNTHETIC explicit small test policy"})
        self.save_sources([synthetic_source(1), synthetic_source(2)])
        code, payload = self.corpus()
        self.assertEqual(code, 0, payload)
        self.assertEqual(payload["status"], "target_met_by_record")

    def test_old_50_without_marker_still_uses_default_and_needs_update(self):
        self.policy(50, 60, 5)
        self.save_sources([synthetic_source(n) for n in range(1, 51)])
        code, payload = self.corpus()
        self.assertEqual(code, 0, payload)
        self.assertEqual(payload["status"], "needs_policy_update")
        self.assertEqual(payload["gap_to_minimum"], 10)
        self.assertEqual(payload["effective_policy_source"], "skill_default")
        self.assertEqual(payload["recorded_policy"]["minimum"], 50)

    def test_invalid_override_marker_cannot_silently_change_policy(self):
        for marker in ({"authorized_by": "assistant", "decision_ref": "SYNTHETIC"},
                       {"authorized_by": "user", "decision_ref": " "},
                       {"authorized_by": "user"}, "SYNTHETIC invalid marker"):
            self.policy(2, 2, 5, marker)
            code, payload = self.corpus()
            self.assertEqual(code, 0, payload)
            self.assertEqual(payload["status"], "needs_policy_update")
            self.assertEqual(payload["effective_policy"], WORKBENCH.DEFAULT_CORPUS_POLICY)
            self.assertFalse(payload["policy_override_applied"])

    def test_invalid_policy_numbers_cannot_be_authorized(self):
        marker = {"authorized_by": "user", "decision_ref": "SYNTHETIC"}
        for values in ((80, 60, 5), (True, 60, 5), (0, 60, 5), (60, 60, -1)):
            self.policy(*values, marker)
            code, payload = self.corpus()
            self.assertEqual(code, 0, payload)
            self.assertTrue(payload["needs_policy_update"])
            self.assertFalse(payload["policy_override_applied"])
            self.assertEqual(payload["effective_policy"], WORKBENCH.DEFAULT_CORPUS_POLICY)

    def test_sources_and_corpus_share_effective_recency_window(self):
        self.policy(2, 2, 8, {"authorized_by": "user", "decision_ref": "SYNTHETIC longer window"})
        self.save_sources([synthetic_source(publication_date="2019-06-01")])
        code, corpus = self.corpus()
        self.assertEqual(code, 0, corpus)
        code, sources = self.cli("sources", "--project-dir", self.project, "--query", "synthetic", "--as-of", AS_OF)
        self.assertEqual(code, 0, sources)
        self.assertEqual(sources["window"], corpus["window"])
        self.assertEqual(sources["effective_policy"], corpus["effective_policy"])
        self.assertEqual(sources["effective_policy_source"], "authorized_user_override")
        self.assertEqual(sources["matches"], 1)
        self.assertEqual(corpus["qualified_read_baseline"], 1)

    def test_first_online_date_beats_newer_issue_date(self):
        self.save_sources([synthetic_source(first_online_date="2020-01-01", publication_date="2025-01-01")])
        code, payload = self.corpus()
        self.assertEqual(code, 0, payload)
        self.assertEqual(payload["qualified_read_baseline"], 0)
        self.assertEqual(payload["records"][0]["recency"]["status"], "outside_window")
        self.assertEqual(payload["records"][0]["recency"]["publication_date"], "2020-01-01")
        code, sources = self.cli("sources", "--project-dir", self.project, "--query", "synthetic", "--as-of", AS_OF)
        self.assertEqual(code, 0, sources)
        self.assertEqual(sources["matches"], 0)

    def test_invalid_first_online_date_is_not_replaced_by_newer_issue_date(self):
        first, last, precision, token = WORKBENCH.publication_interval({"first_online_date": "invalid",
                                                                       "publication_date": "2025-01-01"})
        self.assertIsNone(first)
        self.assertIsNone(last)
        self.assertEqual((precision, token), ("unknown", "invalid"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
