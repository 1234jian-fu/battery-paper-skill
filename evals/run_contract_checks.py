#!/usr/bin/env python3
"""Black-box, standard-library-only CLI contract probes; all data are synthetic.

This runner never imports paper_workbench or its unit-test factories. Every
project and writable input lives in a TemporaryDirectory outside the repository.
Expected values belong to evals.json; this file returns observed CLI results and
byte/directory comparisons. It neither grades its own output nor accesses a URL.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "paper_workbench.py"
FIXTURES = Path(__file__).resolve().parent / "fixtures"
AS_OF = "2026-10-30"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def source(number, **changes):
    item = read_json(FIXTURES / "source-template.json")
    item.update(source_id=f"SYNTHETIC-SRC-{number:03}", unique_work_id=f"synthetic-work-{number:03}")
    item.update(changes)
    return item


def snapshot(root):
    """Detect created/removed directories as well as changed file bytes."""
    return {
        str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else "DIRECTORY"
        for path in root.rglob("*")
    }


class Probe:
    def __init__(self, root):
        self.root = root
        self.project = root / "合成项目_SYNTHETIC"
        self.project.mkdir()
        self.context = self.project / ".paper-writing"
        self.read_only_results = []

    def cli(self, command, *args, readonly=True):
        before = snapshot(self.root)
        env = dict(os.environ, PYTHONUTF8="1", PYTHONDONTWRITEBYTECODE="1")
        proc = subprocess.run(
            [sys.executable, "-B", "-X", "utf8", str(SCRIPT), command, *map(str, args)],
            cwd=self.root, env=env, capture_output=True, encoding="utf-8", timeout=30,
            check=False,
        )
        if readonly:
            self.read_only_results.append(before == snapshot(self.root))
        raw = proc.stdout.strip() or proc.stderr.strip()
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            data = {"unparsed_output": raw}
        return {"exit": proc.returncode, "data": data}

    def init(self, name="SYNTHETIC ONLY"):
        return self.cli("init", "--project-dir", self.project, "--name", name, readonly=False)

    def prepare(self):
        result = self.init()
        if result["exit"] != 0:
            raise RuntimeError(f"Fixture initialization failed: {result}")

    def save_sources(self, items):
        write_json(self.context / "sources.json", {"schema_version": 1, "items": items})

    def corpus(self, as_of=AS_OF):
        return self.cli("corpus", "--project-dir", self.project, "--as-of", as_of)

    def set_project(self, **changes):
        path = self.context / "project.json"
        project = read_json(path)
        project.update(changes)
        write_json(path, project)

    def delivery_fixture(self):
        self.save_sources([source(1), source(2)])
        write_json(self.context / "evidence.json", {"schema_version": 1, "items": [
            {"evidence_id": "SYNTHETIC-E1", "description": "Synthetic only"},
            {"evidence_id": "SYNTHETIC-E2", "description": "Synthetic only"},
        ]})
        return read_json(FIXTURES / "delivery.json")

    def delivery(self, payload):
        path = self.root / "synthetic-delivery.json"
        write_json(path, payload)
        return self.cli("delivery-check", "--project-dir", self.project, "--file", path)


def initialization(probe):
    first = probe.init()
    evidence = read_json(probe.context / "evidence.json")
    sources = read_json(probe.context / "sources.json")
    initial_policy = read_json(probe.context / "project.json")["corpus_policy"]
    probe.set_project(corpus_policy={"minimum": 50, "target": 60, "recent_years": 5})
    (probe.context / "drafts" / "accepted.txt").write_text("SYNTHETIC keep exact\n", encoding="utf-8")
    before = snapshot(probe.root)
    second = probe.init("MUST NOT REPLACE")
    unchanged = before == snapshot(probe.root)
    (probe.context / "issues.md").unlink()
    before_missing = snapshot(probe.root)
    repaired = probe.init("MUST NOT REPLACE")
    after_missing = snapshot(probe.root)
    return {
        "first": first, "initial_policy": initial_policy,
        "initial_evidence_count": len(evidence["items"]), "initial_source_count": len(sources["items"]),
        "second": second, "second_preserves_all": unchanged, "repair": repaired,
        "repair_preserves_existing": all(after_missing.get(key) == value for key, value in before_missing.items()),
        "repair_added_paths": sorted(set(after_missing) - set(before_missing)),
    }


def threshold(probe):
    probe.prepare()
    probe.set_project(required_figure_tasks=["SYNTHETIC-F1", "SYNTHETIC-F2"])
    probe.save_sources([source(n) for n in range(1, 60)])
    before = probe.corpus()
    probe.save_sources([source(n) for n in range(1, 61)])
    after = probe.corpus()
    return {"at_59": before, "at_60": after}


def dates(probe):
    probe.prepare()
    probe.save_sources([
        source(1, publication_date="2021-10-30"),
        source(2, publication_date="2026-10-30"),
        source(3, publication_date="2021-10-29"),
        source(4, publication_date="2026-10-31"),
        source(5, publication_date="2021"),
        source(6, publication_date="2025"),
        source(7, publication_date="2026-10"),
        source(8, first_online_date="2020-01-01", publication_date="2025-01-01"),
        source(9, first_online_date="not-a-date", publication_date="2025-01-01"),
    ])
    current = probe.corpus()
    legacy = probe.cli("sources", "--project-dir", probe.project, "--query", "synthetic", "--as-of", AS_OF, "--include-legacy", "--limit", "20")
    recent = probe.cli("sources", "--project-dir", probe.project, "--query", "synthetic", "--as-of", AS_OF, "--limit", "20")
    leap = probe.corpus("2024-02-29")
    return {"current": current, "recent": recent, "legacy": legacy, "leap": leap}


def identities(probe):
    probe.prepare()
    rows = []
    for n in range(1, 31):
        alias = source(n + 30, unique_work_id=f"synthetic-work-{n:03}")
        if n % 2:
            alias["doi"] = f"doi:10.99999/synthetic-{n}"
        rows.extend([source(n, doi=f"https://doi.org/10.99999/SYNTHETIC-{n}"),
                     alias])
    probe.save_sources(rows)
    aliases = probe.corpus()
    probe.save_sources(list(reversed(rows)))
    reversed_aliases = probe.corpus()
    probe.save_sources([source(n, source_id="SYNTHETIC-DUPLICATE") for n in range(1, 61)])
    duplicate_ids = probe.corpus()
    probe.save_sources([
        source(1), source(2, source_type="review"), source(3, read_scope=["abstract"]),
        source(4, exact_locations=[]), source(5, fit_reason=True),
    ])
    invalid = probe.corpus()
    return {"aliases": aliases, "reversed_aliases": reversed_aliases, "duplicate_ids": duplicate_ids, "invalid": invalid}


def policies(probe):
    probe.prepare()
    probe.save_sources([source(n) for n in range(1, 61)])
    probe.set_project(corpus_policy={"minimum": 80, "target": 80, "recent_years": 5})
    unapproved = probe.corpus()
    probe.set_project(corpus_policy_override={"authorized_by": "user", "decision_ref": "SYNTHETIC evaluation authorization; not real author acceptance"})
    approved = probe.corpus()
    return {"unapproved": unapproved, "approved": approved}


def delivery(probe):
    probe.prepare()
    original = probe.delivery_fixture()
    good = probe.delivery(original)
    lost_space = copy.deepcopy(original)
    lost_space["paragraphs"][0]["text"] = "Alpha. Beta.\n"
    changed_order = copy.deepcopy(original)
    changed_order["sentences"][0]["order"] = 1
    changed_order["sentences"][1]["order"] = 2
    missing_evidence = copy.deepcopy(original)
    missing_evidence["sentences"][2]["evidence_ids"] = ["SYNTHETIC-UNKNOWN"]
    missing_source = copy.deepcopy(original)
    missing_source["sentences"][0]["source_ids"] = ["SYNTHETIC-UNKNOWN"]
    return {
        "good": good, "lost_space": probe.delivery(lost_space), "changed_order": probe.delivery(changed_order),
        "missing_evidence": probe.delivery(missing_evidence), "missing_source": probe.delivery(missing_source),
    }


def count(probe):
    path = probe.root / "synthetic-count.txt"
    path.write_bytes((FIXTURES / "count.txt").read_bytes())
    prose = probe.cli("count", "--file", path, "--start-marker", "<PROSE>", "--end-marker", "</PROSE>")
    caption = probe.cli("count", "--file", path, "--start-marker", "<CAPTION>", "--end-marker", "</CAPTION>")
    one_marker = probe.cli("count", "--file", path, "--start-marker", "<PROSE>")
    repeated_path = probe.root / "synthetic-repeat.txt"
    repeated_path.write_text("<PROSE>one<PROSE>two</PROSE>", encoding="utf-8")
    repeated = probe.cli("count", "--file", repeated_path, "--start-marker", "<PROSE>", "--end-marker", "</PROSE>")
    return {"prose": prose, "caption": caption, "one_marker": one_marker, "repeated_markers": repeated}


def readonly(probe):
    probe.prepare()
    payload = probe.delivery_fixture()
    delivery_path = probe.root / "synthetic-final.json"
    write_json(delivery_path, payload)
    text_path = probe.root / "synthetic-final.txt"
    text_path.write_text("SYNTHETIC unchanged.", encoding="utf-8")
    before = snapshot(probe.root)
    results = [
        probe.cli("status", "--project-dir", probe.project),
        probe.cli("check", "--project-dir", probe.project),
        probe.corpus(),
        probe.cli("sources", "--project-dir", probe.project, "--query", "synthetic", "--as-of", AS_OF),
        probe.cli("count", "--file", text_path),
        probe.cli("delivery-check", "--project-dir", probe.project, "--file", delivery_path),
    ]
    return {"exit_codes": [item["exit"] for item in results], "command_count": len(results),
            "entire_tree_unchanged": before == snapshot(probe.root)}


CASES = {func.__name__: func for func in (initialization, threshold, dates, identities, policies, delivery, count, readonly)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", choices=sorted(CASES), required=True)
    parser.add_argument("--json", action="store_true", help="Accepted for evaluation harness compatibility; output is always JSON")
    args = parser.parse_args()
    try:
        with tempfile.TemporaryDirectory(prefix="battery_synthetic_contract_") as directory:
            probe = Probe(Path(directory))
            result = CASES[args.case](probe)
            result["read_only_commands"] = len(probe.read_only_results)
            result["all_read_only_commands_unchanged"] = all(probe.read_only_results)
            result["synthetic_only"] = True
        print(json.dumps(result, ensure_ascii=True, indent=2))
        return 0
    except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as exc:
        print(json.dumps({"runner_error": str(exc)}, ensure_ascii=True))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
