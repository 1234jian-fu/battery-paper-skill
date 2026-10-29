#!/usr/bin/env python3
"""Local, standard-library helpers for a battery-paper writing workspace.

No network, package installation, manuscript rewriting, or scientific validation.
Date-based commands require the client/task cutoff via --as-of YYYY-MM-DD.
New projects use a 60-work minimum, 60-work target, rolling five-year policy.
Existing policy records are preserved and explicitly flagged when they need updating.
"""
from __future__ import annotations

import argparse
import calendar
import hashlib
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path
from urllib.parse import unquote, urlsplit

STAGES = {
    "scoped", "evidence_mapped", "sources_mapped", "drafted", "checked",
    "author_accepted", "assembled", "needs_recheck",
}
REQUIRED_FILES = ("project.json", "evidence.json", "sources.json", "decisions.md", "issues.md")
DEFAULT_CORPUS_POLICY = {"minimum": 60, "target": 60, "recent_years": 5}
EVIDENCE_BASES = {"own_observation", "author_provided", "author_confirmed", "own_calculation"}
NO_SOURCE_BASES = EVIDENCE_BASES | {"author_transition", "retained_accepted"}
STRUCTURE_NOTE = "仅检查记录和字段结构，不判断实验真实性、引文准确性、语义保留或科学结论。"


def emit(payload):
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def context_dir(project_dir):
    # Always require an explicit project; the current directory has no special identity.
    project = Path(project_dir).expanduser().resolve()
    return project, project / ".paper-writing"


def nonempty_string(value):
    return isinstance(value, str) and bool(value.strip())


def policy_audit(project):
    recorded = project.get("corpus_policy")
    valid = isinstance(recorded, dict)
    if valid:
        numbers = [recorded.get(key) for key in DEFAULT_CORPUS_POLICY]
        valid = (all(isinstance(value, int) and not isinstance(value, bool) and value > 0
                     for value in numbers) and numbers[1] >= numbers[0])
    compatible = valid and all(recorded.get(key) == value for key, value in DEFAULT_CORPUS_POLICY.items())
    marker = project.get("corpus_policy_override")
    authorized = (isinstance(marker, dict) and marker.get("authorized_by") == "user"
                  and nonempty_string(marker.get("decision_ref")))
    applied = bool(valid and authorized)
    effective = ({key: recorded[key] for key in DEFAULT_CORPUS_POLICY}
                 if applied else dict(DEFAULT_CORPUS_POLICY))
    needs_update = not compatible and not applied
    return {
        "recorded_policy": recorded,
        "required_policy": dict(DEFAULT_CORPUS_POLICY),
        "recorded_policy_numbers_valid": valid,
        "default_policy": dict(DEFAULT_CORPUS_POLICY),
        "effective_policy": effective,
        "effective_policy_source": "authorized_user_override" if applied else "skill_default",
        "policy_override_applied": applied,
        "policy_override_status": "authorized" if applied else "absent" if marker is None else "invalid_or_unusable",
        "needs_policy_update": needs_update,
        "policy_status": "authorized_override" if applied else "needs_policy_update" if needs_update else "current",
        "policy_note": "原政策只读保留；自定政策仅在有效corpus_policy及authorized_by=user、非空decision_ref标记同时存在时生效，工具不会自动迁移。",
    }


def normalize_doi(value):
    text = str(value or "").strip()
    if re.match(r"https?://(?:dx\.)?doi\.org/", text, re.I):
        text = unquote(urlsplit(text).path.lstrip("/"))
    text = re.sub(r"^doi\s*:\s*", "", text, flags=re.I).strip().rstrip(".,;")
    while text.endswith(")") and text.count(")") > text.count("("):
        text = text[:-1]
    return text.casefold()


def window_for(as_of, years=5):
    if not as_of:
        raise ValueError("Provide the client/task cutoff with --as-of YYYY-MM-DD; no system-date fallback is used")
    if not isinstance(as_of, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", as_of):
        raise ValueError("--as-of must use the explicit YYYY-MM-DD format")
    if not isinstance(years, int) or isinstance(years, bool) or years < 1:
        raise ValueError("recent_years must be positive")
    last = date.fromisoformat(as_of)
    first_year = last.year - years
    first = last.replace(year=first_year, day=min(last.day, calendar.monthrange(first_year, last.month)[1]))
    return first, last


def publication_interval(item):
    raw = item.get("first_online_date") or item.get("publication_date") or item.get("year")
    token = str(raw or "").strip()
    try:
        if re.fullmatch(r"\d{4}", token):
            year = int(token)
            return date(year, 1, 1), date(year, 12, 31), "year", token
        if re.fullmatch(r"\d{4}-\d{2}", token):
            year, month = map(int, token.split("-"))
            return date(year, month, 1), date(year, month, calendar.monthrange(year, month)[1]), "month", token
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", token):
            day = date.fromisoformat(token)
            return day, day, "day", token
    except ValueError:
        pass
    return None, None, "unknown", token


def recency_status(item, first, last):
    start, end, precision, token = publication_interval(item)
    if start is None:
        status = "date_unknown"
    elif end < first:
        status = "outside_window"
    elif start > last:
        status = "future_publication"
    elif start >= first and end <= last:
        status = "within_window"
    else:
        status = "needs_date_verification"
    return {"status": status, "publication_date": token, "precision": precision,
            "date_verified": item.get("publication_date_verified") is True}


def source_identity(item):
    doi = normalize_doi(item.get("doi"))
    if doi and re.fullmatch(r"10\.\d{4,9}/\S+", doi):
        return "doi:" + doi
    return "work:" + item["unique_work_id"] if nonempty_string(item.get("unique_work_id")) else None


def canonical_work_identities(records):
    """Join DOI/work-ID aliases without discarding either explicit identity."""
    parents, aliases = {}, []

    def find(token):
        parents.setdefault(token, token)
        if parents[token] != token:
            parents[token] = find(parents[token])
        return parents[token]

    for item in records:
        tokens = []
        doi = normalize_doi(item.get("doi"))
        if doi and re.fullmatch(r"10\.\d{4,9}/\S+", doi):
            tokens.append("doi:" + doi)
        if nonempty_string(item.get("unique_work_id")):
            tokens.append("work:" + item["unique_work_id"])
        aliases.append(tokens)
        for token in tokens:
            find(token)
        if len(tokens) == 2:
            left, right = find(tokens[0]), find(tokens[1])
            parents[max(left, right)] = min(left, right)
    return [find(tokens[0]) if tokens else None for tokens in aliases]


def valid_locations(value):
    return nonempty_string(value) or (isinstance(value, list) and bool(value)
                                     and all(nonempty_string(location) for location in value))


def source_qualification(item, first, last):
    recent = recency_status(item, first, last)
    reasons = []
    if not nonempty_string(item.get("source_id")):
        reasons.append("missing_source_id")
    if not source_identity(item):
        reasons.append("missing_verified_work_identity")
    if "unique_work_id" in item and not nonempty_string(item["unique_work_id"]):
        reasons.append("invalid_unique_work_id")
    if item.get("source_type") not in {"primary_research", "methods_research"}:
        reasons.append("not_identified_as_primary_research")
    if item.get("bibliographic_status") != "verified":
        reasons.append("bibliography_not_verified")
    if item.get("publication_role") in {"correction", "erratum", "retraction", "preprint"} or item.get("is_correction"):
        reasons.append("not_a_separate_formal_primary_work")
    if recent["status"] != "within_window":
        reasons.append(recent["status"])
    if not recent["date_verified"] or not nonempty_string(item.get("date_source_url")):
        reasons.append("publication_date_not_source_verified")
    if item.get("date_basis") not in {"publisher_first_online", "publisher_formal_publication"}:
        reasons.append("formal_first_publication_basis_missing")
    if item.get("topical_fit") not in {"direct", "shared_test"} or not nonempty_string(item.get("fit_reason")):
        reasons.append("task_fit_not_established")
    scopes = item.get("read_scope", [])
    scopes = [scopes] if isinstance(scopes, str) else scopes
    if (not isinstance(scopes, list) or
            not any(scope in {"relevant_body", "full_main_text", "full_main_and_SI"}
                    for scope in scopes if isinstance(scope, str))):
        reasons.append("relevant_original_body_not_recorded_as_read")
    for key in ("exact_locations", "chinese_meaning", "source_paragraph_move", "source_data_expression"):
        valid = valid_locations(item.get(key)) if key == "exact_locations" else nonempty_string(item.get(key))
        if not valid:
            reasons.append("missing_" + key)
    return recent, reasons


def init_context(args):
    project, context = context_dir(args.project_dir)
    if not project.is_dir():
        raise ValueError("Explicit --project-dir must name an existing directory")
    context.mkdir(exist_ok=True)
    timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
    files = {
        "project.json": {
            "schema_version": 1, "project_name": args.name, "domain": args.domain,
            "language": "zh-CN", "mode": "figure", "current_stage": "scoped",
            "current_task": "", "next_action": "读取当前作者要求和素材，确定本次范围",
            "protected_sections": [], "terminology": [], "section_states": {},
            "source_paths": [], "updated_at": timestamp,
            "corpus_policy": dict(DEFAULT_CORPUS_POLICY), "required_figure_tasks": [],
        },
        "evidence.json": {"schema_version": 1, "items": []},
        "sources.json": {"schema_version": 1, "items": []},
        "decisions.md": "# 作者决定与确认记录\n\n按日期记录位置、作者意见、采用方式、版本和依据。仅作者明确接受的内容标记为确认稿。\n",
        "issues.md": "# 待核查问题\n\n| ID | 问题及来源 | 影响范围 | 依赖级别 | 回答/核查 | 状态 |\n|---|---|---|---|---|---|\n",
    }
    created, preserved = [], []
    for filename, payload in files.items():
        target = context / filename
        try:
            with target.open("x", encoding="utf-8", newline="\n") as handle:
                handle.write(json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
                             if isinstance(payload, dict) else payload)
            created.append(filename)
        except FileExistsError:
            preserved.append(filename)
    (context / "drafts").mkdir(exist_ok=True)
    existing = read_json(context / "project.json")
    if not isinstance(existing, dict):
        raise ValueError("Existing project.json must contain an object; it has been preserved")
    emit({"context": ".paper-writing", "project_name": existing.get("project_name"),
          "created": created, "preserved": preserved, **policy_audit(existing),
          "note": "仅补充缺失文件；既有文件和原稿未覆盖；空白记录未继承任何项目实验事实或旧文献库。"})


def show_status(args):
    _, context = context_dir(args.project_dir)
    project = read_json(context / "project.json")
    if not isinstance(project, dict):
        raise ValueError("project.json must contain an object")
    result = {key: project.get(key) for key in (
        "project_name", "domain", "current_task", "mode", "current_stage",
        "next_action", "protected_sections", "terminology", "section_states", "updated_at",
    )}
    result.update(policy_audit(project))
    result["context"] = ".paper-writing"
    result["records_to_read"] = [".paper-writing/" + name for name in REQUIRED_FILES if name != "project.json"]
    result["note"] = "概要只用于接续，写作前仍需查看相应记录和当前素材。"
    emit(result)


def project_sources(project_dir):
    _, context = context_dir(project_dir)
    data = read_json(context / "sources.json")
    if not isinstance(data, dict) or not isinstance(data.get("items"), list):
        raise ValueError("Expected sources.json object with an items array")
    if any(not isinstance(item, dict) for item in data["items"]):
        raise ValueError("Every sources.items entry must be an object")
    return data["items"]


def query_sources(args):
    _, context = context_dir(args.project_dir)
    project = read_json(context / "project.json")
    if not isinstance(project, dict):
        raise ValueError("Expected project.json object")
    audit = policy_audit(project)
    records = project_sources(args.project_dir)
    terms = [term.casefold() for term in re.findall(r"[\w+-]+", args.query, flags=re.UNICODE)]
    if not terms:
        raise ValueError("Provide at least one query term")
    if args.limit < 1:
        raise ValueError("--limit must be positive")
    first, last = window_for(args.as_of, audit["effective_policy"]["recent_years"])
    ranked, recency_counts, query_matches = [], {}, 0
    for item in records:
        title = str(item.get("title", "")).casefold()
        tags = item.get("tags", [])
        tags = " ".join(str(tag) for tag in tags) if isinstance(tags, list) else str(tags)
        tags = tags.casefold()
        rest = " ".join(str(item.get(key, "")) for key in (
            "source_id", "doi", "journal", "source_paragraph_move", "source_data_expression", "source_location",
        )).casefold()
        score = sum(4 * int(term in title) + 3 * int(term in tags) + int(term in rest) for term in terms)
        if score:
            query_matches += 1
            recent, reasons = source_qualification(item, first, last)
            recency_counts[recent["status"]] = recency_counts.get(recent["status"], 0) + 1
            if args.include_legacy or recent["status"] == "within_window":
                ranked.append((score, item, recent, reasons))
    ranked.sort(key=lambda row: (-row[0], str(row[1].get("source_id", ""))))
    selected = []
    for score, item, recent, reasons in ranked[:args.limit]:
        selected.append({key: item.get(key) for key in (
            "source_id", "title", "doi", "journal", "year", "official_url", "tags", "read_scope",
            "exact_locations", "source_paragraph_move", "source_data_expression",
        )} | {"match_score": score, "recency": recent,
              "qualified_by_record": not reasons, "qualification_reasons": reasons})
    emit({"index": ".paper-writing/sources.json", "query": args.query, **audit,
          "query_matches_before_date_filter": query_matches,
          "window": {"from": first.isoformat(), "through": last.isoformat()},
          "recency_counts": recency_counts, "include_legacy": args.include_legacy,
          "matches": len(ranked), "results": selected,
          "note": "只搜索显式项目的sources.json，不使用捆绑旧索引。匹配不是新检索、实际核读或60篇达标证明；具体引用须重开来源。"})


def corpus_status(args):
    _, context = context_dir(args.project_dir)
    project = read_json(context / "project.json")
    if not isinstance(project, dict):
        raise ValueError("Expected project.json object")
    records = project_sources(args.project_dir)
    audit = policy_audit(project)
    minimum, target, years = (audit["effective_policy"][key] for key in ("minimum", "target", "recent_years"))
    first, last = window_for(args.as_of, years)
    errors = []
    checked_record_ids({"items": records}, "sources.json", "source_id", errors, allow_duplicate_works=True)
    required_tasks = project.get("required_figure_tasks", [])
    required_task_ids = checked_task_ids(required_tasks, "project.json: required_figure_tasks", errors)
    candidate_ids, relevant_ids, qualified_ids, mapped_tasks = set(), set(), set(), set()
    diagnostics, all_ids = [], []
    for item, identity in zip(records, canonical_work_identities(records)):
        if identity:
            all_ids.append(identity)
        recent, reasons = source_qualification(item, first, last)
        if identity and recent["status"] == "within_window":
            candidate_ids.add(identity)
        if (identity and item.get("source_type") in {"primary_research", "methods_research"}
                and item.get("topical_fit") in {"direct", "shared_test"} and nonempty_string(item.get("fit_reason"))):
            relevant_ids.add(identity)
        qualified = not reasons
        duplicate_qualified = qualified and identity in qualified_ids
        if qualified:
            qualified_ids.add(identity)
            tasks = item.get("linked_figure_tasks", [])
            if isinstance(tasks, list):
                mapped_tasks.update(task for task in tasks if nonempty_string(task))
        diagnostics.append({"source_id": item.get("source_id"), "identity": identity,
                            "recency": recent, "qualified_record": qualified,
                            "duplicate_qualified_record": duplicate_qualified, "reasons": reasons})
    count = len(qualified_ids)
    baseline_status = "structure_errors" if errors else "target_met_by_record" if count >= target else "baseline_incomplete"
    missing_tasks = sorted(required_task_ids - mapped_tasks)
    mapping_status = "structure_errors" if errors else "not_specified" if not required_tasks else "incomplete" if missing_tasks else "complete_by_record"
    emit({"context": ".paper-writing", "as_of_date": last.isoformat(),
          "window": {"from": first.isoformat(), "through": last.isoformat()}, **audit,
          "records_discovered": len(records), "unique_identified_works": len(set(all_ids)),
          "duplicate_identity_records": len(all_ids) - len(set(all_ids)),
          "date_eligible_candidates": len(candidate_ids), "topically_relevant_primary_works": len(relevant_ids),
          "qualified_read_baseline": count, "gap_to_minimum": max(0, minimum-count),
          "gap_to_target": max(0, target-count), "baseline_status": baseline_status,
          "status": "structure_errors" if errors else "needs_policy_update" if audit["needs_policy_update"] else baseline_status,
          "record_structure_ok": not errors, "errors": errors,
          "recorded_figure_tasks": sorted(mapped_tasks),
          "figure_mapping": {"status": mapping_status, "required": required_tasks, "missing": missing_tasks},
          "records": diagnostics,
          "note": "按输出effective_policy对记录资格和日期统计，不证明实际阅读、语义契合或科学正确。结构错误时不得用于达标。旧索引、摘要和二级卡片本身不能计作已核读基底；图任务充分性须人工检查。"})
    return 0 if not errors else 1


def count_text(args):
    raw = Path(args.file).read_text(encoding="utf-8-sig")
    if bool(args.start_marker) != bool(args.end_marker):
        raise ValueError("Use both --start-marker and --end-marker, or neither")
    selected = raw
    if args.start_marker:
        if raw.count(args.start_marker) != 1 or raw.count(args.end_marker) != 1:
            raise ValueError("Each requested marker must occur exactly once")
        first = raw.index(args.start_marker) + len(args.start_marker)
        last = raw.index(args.end_marker)
        if last < first:
            raise ValueError("End marker precedes start marker")
        selected = raw[first:last]
    emit({
        "file_name": Path(args.file).name,
        "selection": "marker-delimited" if args.start_marker else "entire plain-text file",
        "characters_without_whitespace": len(re.sub(r"\s", "", selected)),
        "han_characters": len(re.findall(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\U00020000-\U0002fa1f]", selected)),
        "english_lexical_words": len(re.findall(r"[A-Za-z]+(?:['’\-][A-Za-z]+)*", selected)),
        "paragraphs": len([part for part in re.split(r"\n\s*\n", selected.strip()) if part.strip()]),
        "selected_text_sha256": hashlib.sha256(selected.encode("utf-8")).hexdigest(),
        "counting_rule": "字符数含英文、数字、标点；去空白。英文词数只计拉丁字母词；Markdown未自动剥离，正文与图注请分别选择。",
    })


def checked_task_ids(value, label, errors):
    if not isinstance(value, list):
        errors.append(label + " must be an array")
        return set()
    result = set()
    for index, task in enumerate(value):
        if not nonempty_string(task):
            errors.append(f"{label}[{index}] must be a nonempty string")
        else:
            result.add(task)
    return result


def checked_record_ids(data, filename, id_key, errors, allow_duplicate_works=False):
    if not isinstance(data, dict):
        errors.append(f"{filename}: expected object")
        return set()
    rows = data.get("items")
    if not isinstance(rows, list):
        errors.append(f"{filename}: items must be an array")
        return set()
    seen, dois, work_ids = set(), set(), set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            errors.append(f"{filename}: items[{index}] must be an object")
            continue
        identifier = row.get(id_key)
        if not nonempty_string(identifier):
            errors.append(f"{filename}: items[{index}] needs nonempty string {id_key}")
        elif identifier in seen:
            errors.append(f"{filename}: duplicate {id_key} {identifier}")
        else:
            seen.add(identifier)
        if filename == "sources.json":
            doi = normalize_doi(row.get("doi"))
            if doi and doi in dois and not allow_duplicate_works:
                errors.append(f"sources.json: duplicate DOI {doi}; combine usage in one source card")
            if doi:
                dois.add(doi)
            if "unique_work_id" in row:
                work_id = row["unique_work_id"]
                if not nonempty_string(work_id):
                    errors.append(f"sources.json: items[{index}] unique_work_id must be a nonempty string")
                elif work_id in work_ids and not allow_duplicate_works:
                    errors.append("sources.json: duplicate unique_work_id " + work_id + "; combine usage in one source card")
                else:
                    work_ids.add(work_id)
            for key in ("fit_reason", "exact_locations", "chinese_meaning", "source_paragraph_move", "source_data_expression"):
                if key in row:
                    valid = valid_locations(row[key]) if key == "exact_locations" else nonempty_string(row[key])
                    if not valid:
                        errors.append(f"sources.json: items[{index}] {key} needs nonempty text of the expected type")
            if "linked_figure_tasks" in row:
                checked_task_ids(row["linked_figure_tasks"], f"sources.json: items[{index}] linked_figure_tasks", errors)
    return seen


def check_context(args):
    _, context = context_dir(args.project_dir)
    errors, warnings, objects = [], [], {}
    for name in REQUIRED_FILES:
        target = context / name
        if not target.exists():
            errors.append(f"Missing {name}")
            continue
        if name.endswith(".json"):
            try:
                objects[name] = read_json(target)
                if not isinstance(objects[name], dict):
                    errors.append(f"{name}: expected object")
            except (ValueError, OSError) as exc:
                errors.append(f"{name}: {type(exc).__name__}; unable to read JSON")
    project = objects.get("project.json", {})
    audit = policy_audit(project) if isinstance(project, dict) else policy_audit({})
    if isinstance(project, dict):
        for key in ("schema_version", "project_name", "domain", "current_stage", "protected_sections", "terminology"):
            if key not in project:
                errors.append(f"project.json: missing {key}")
        if project.get("current_stage") not in STAGES:
            errors.append("project.json: unsupported current_stage")
        version = project.get("schema_version")
        if not isinstance(version, int) or isinstance(version, bool) or version < 1:
            errors.append("project.json: schema_version must be a positive integer")
        for key in ("project_name", "domain"):
            if not nonempty_string(project.get(key)):
                errors.append(f"project.json: {key} must be a nonempty string")
        checked_task_ids(project.get("required_figure_tasks", []), "project.json: required_figure_tasks", errors)
        for key in ("protected_sections", "terminology", "source_paths"):
            if key in project and not isinstance(project[key], list):
                errors.append(f"project.json: {key} must be an array")
        if not isinstance(project.get("section_states", {}), dict):
            errors.append("project.json: section_states must be an object")
        else:
            for name, state in project.get("section_states", {}).items():
                stage = state.get("stage") if isinstance(state, dict) else state
                if stage not in STAGES:
                    errors.append(f"section_states.{name}: unsupported stage")
        if not project.get("current_task"):
            warnings.append("current_task is not yet recorded")
        if not (context / "drafts").is_dir():
            warnings.append("drafts directory is absent")
    if audit["needs_policy_update"]:
        warnings.append("needs_policy_update: recorded policy does not explicitly match 60/60/5")
    for filename, id_key in (("evidence.json", "evidence_id"), ("sources.json", "source_id")):
        if filename in objects:
            checked_record_ids(objects[filename], filename, id_key, errors)
    emit({"context": ".paper-writing", "ok": not errors,
          "status": "structure_errors" if errors else audit["policy_status"],
          **audit, "errors": errors, "warnings": warnings, "note": STRUCTURE_NOTE})
    return 0 if not errors else 1


def delivery_check(args):
    """Rebuild exact paragraphs from final sentence text, then check record references."""
    _, context = context_dir(args.project_dir)
    data = read_json(args.file)
    if not isinstance(data, dict):
        raise ValueError("Delivery file must contain an object")
    errors, warnings = [], []
    evidence_ids = checked_record_ids(read_json(context / "evidence.json"), "evidence.json", "evidence_id", errors)
    source_ids = checked_record_ids(read_json(context / "sources.json"), "sources.json", "source_id", errors)
    sentences, paragraphs = data.get("sentences"), data.get("paragraphs")
    if not isinstance(sentences, list) or not isinstance(paragraphs, list):
        raise ValueError("Delivery object requires sentences and paragraphs arrays")
    if not sentences or not paragraphs:
        errors.append("Delivery sentences and paragraphs must both be nonempty")
    paragraph_map, ordered_paragraphs = {}, []
    for index, row in enumerate(paragraphs):
        label = f"paragraphs[{index}]"
        if not isinstance(row, dict):
            errors.append(label + ": expected object")
            continue
        pid, text = row.get("paragraph_id"), row.get("text")
        if not nonempty_string(pid):
            errors.append(label + ": needs nonempty string paragraph_id")
            continue
        if pid in paragraph_map:
            errors.append(label + ": duplicate paragraph_id " + pid)
            continue
        if not isinstance(text, str):
            errors.append(label + ": text must be a string")
            continue
        if not text.strip():
            errors.append(label + ": final paragraph text must contain non-whitespace content")
        paragraph_map[pid] = text
        ordered_paragraphs.append(pid)
    seen_sentences, orders, grouped = set(), set(), {}
    for index, row in enumerate(sentences):
        label = f"sentences[{index}]"
        if not isinstance(row, dict):
            errors.append(label + ": expected object")
            continue
        sid, pid, order, text = (row.get(key) for key in ("sentence_id", "paragraph_id", "order", "text"))
        if not nonempty_string(sid):
            errors.append(label + ": needs nonempty stable sentence_id")
        elif re.search(r"\s", sid):
            errors.append(label + ": stable sentence_id must not contain whitespace")
        elif sid in seen_sentences:
            errors.append(label + ": duplicate sentence_id " + sid)
        else:
            seen_sentences.add(sid)
        valid_pid = nonempty_string(pid)
        if not valid_pid or pid not in paragraph_map:
            errors.append(label + ": paragraph_id does not reference a listed paragraph")
        valid_order = isinstance(order, int) and not isinstance(order, bool) and order > 0
        if not valid_order:
            errors.append(label + ": order must be a positive integer")
        elif valid_pid and (pid, order) in orders:
            errors.append(label + ": duplicate order in paragraph " + pid)
        elif valid_pid:
            orders.add((pid, order))
        if not nonempty_string(text):
            errors.append(label + ": final text must be a nonempty string")
        elif valid_pid and valid_order:
            grouped.setdefault(pid, []).append((order, text))
        for key, known in (("evidence_ids", evidence_ids), ("source_ids", source_ids)):
            refs = row.get(key)
            if not isinstance(refs, list):
                errors.append(label + ": " + key + " must be an array (may be empty)")
                continue
            seen_refs = set()
            for ref in refs:
                if not nonempty_string(ref):
                    errors.append(label + ": " + key + " entries must be nonempty strings")
                elif ref in seen_refs:
                    errors.append(label + ": duplicate reference in " + key + ": " + ref)
                else:
                    seen_refs.add(ref)
                    if ref not in known:
                        errors.append(label + ": unknown " + key + " reference " + ref)
        basis = row.get("basis")
        if isinstance(row.get("source_ids"), list) and not row["source_ids"]:
            if not isinstance(basis, str) or basis not in NO_SOURCE_BASES:
                errors.append(label + ": empty source_ids requires an allowed basis: " + ", ".join(sorted(NO_SOURCE_BASES)))
            elif basis == "retained_accepted" and not nonempty_string(row.get("basis_ref")):
                errors.append(label + ": retained_accepted without sources requires nonempty basis_ref to an accepted record")
        if isinstance(basis, str) and basis in EVIDENCE_BASES:
            refs = row.get("evidence_ids")
            if (not isinstance(refs, list) or not refs or
                    not all(nonempty_string(ref) and ref in evidence_ids for ref in refs)):
                errors.append(label + ": " + basis + " requires nonempty valid evidence_ids")
    comparisons = []
    for pid in ordered_paragraphs:
        rows = grouped.get(pid, [])
        rebuilt = "".join(text for _, text in sorted(rows, key=lambda row: row[0]))
        expected = paragraph_map[pid]
        match = bool(rows) and rebuilt == expected
        if not rows:
            errors.append("paragraph " + pid + ": no sentences reference this paragraph")
        elif not match:
            errors.append("paragraph " + pid + ": exact final-text mismatch")
        mismatch_at = next((i for i, (left, right) in enumerate(zip(rebuilt, expected)) if left != right), None)
        if mismatch_at is None and len(rebuilt) != len(expected):
            mismatch_at = min(len(rebuilt), len(expected))
        comparisons.append({"paragraph_id": pid, "sentence_count": len(rows), "exact_match": match,
                            "rebuilt_characters": len(rebuilt), "paragraph_characters": len(expected),
                            "first_difference_index_zero_based": mismatch_at,
                            "rebuilt_sha256": hashlib.sha256(rebuilt.encode("utf-8")).hexdigest(),
                            "paragraph_sha256": hashlib.sha256(expected.encode("utf-8")).hexdigest()})
    if "propositions" in data:
        if not isinstance(data["propositions"], list):
            errors.append("Optional propositions must be an array for human meaning review")
        else:
            warnings.append("propositions are retained for human review; their meaning and preservation are not machine-validated")
    emit({"file_name": Path(args.file).name, "ok": not errors,
          "status": "delivery_structure_consistent" if not errors else "delivery_structure_errors",
          "sentence_count": len(sentences), "paragraph_count": len(paragraphs),
          "comparisons": comparisons, "errors": errors, "warnings": warnings,
          "assembly_rule": "Group by paragraph_id; sort positive order ascending; concatenate final text with no inserted separator. Punctuation, internal/edge spaces, and newlines are compared exactly.",
          "id_rule": "sentence_id must be a nonempty unique string; authors retain the same ID across revisions. Cross-version stability is not inferred from one delivery file.",
          "reference_rule": "Every evidence_ids/source_ids entry must resolve to the project records. Many-to-many references are allowed. Empty source_ids requires an allowed basis. own_observation, author_provided, author_confirmed, and own_calculation require nonempty valid evidence_ids; author_transition may omit evidence; retained_accepted requires basis_ref when source_ids is empty.",
          "note": STRUCTURE_NOTE + "正文和记录均未改写；basis_ref仅检查非空，不核定接受事实。"})
    return 0 if not errors else 1


def make_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest="command", required=True)
    init = subs.add_parser("init", help="Create only missing explicit-project records; preserve existing policy and files")
    init.add_argument("--project-dir", required=True)
    init.add_argument("--name", required=True)
    init.add_argument("--domain", default="待定位")
    init.set_defaults(handler=init_context)
    status = subs.add_parser("status", help="Read project status and explicitly report needs_policy_update")
    status.add_argument("--project-dir", required=True)
    status.set_defaults(handler=show_status)
    sources = subs.add_parser("sources", help="Search the explicit project's sources.json; no bundled source index")
    sources.add_argument("--project-dir", required=True)
    sources.add_argument("--query", required=True)
    sources.add_argument("--limit", type=int, default=5)
    sources.add_argument("--as-of", required=True, help="Client/task cutoff date YYYY-MM-DD; never inferred from the system clock")
    sources.add_argument("--include-legacy", action="store_true", help="Show historical/date-uncertain project entries for navigation only")
    sources.set_defaults(handler=query_sources)
    corpus = subs.add_parser("corpus", help="Audit recorded baseline using the 60/60/5 default or an explicitly authorized policy")
    corpus.add_argument("--project-dir", required=True)
    corpus.add_argument("--as-of", required=True, help="Client/task cutoff date YYYY-MM-DD; inclusive five-year window")
    corpus.set_defaults(handler=corpus_status)
    count = subs.add_parser("count", help="Count text or a uniquely delimited prose/caption region")
    count.add_argument("--file", required=True)
    count.add_argument("--start-marker")
    count.add_argument("--end-marker")
    count.set_defaults(handler=count_text)
    check = subs.add_parser("check", help="Read-only record structure check; never validates science or rewrites manuscripts")
    check.add_argument("--project-dir", required=True)
    check.set_defaults(handler=check_context)
    delivery = subs.add_parser("delivery-check", help="Check exact final sentence-to-paragraph assembly and existing record IDs",
        description="Read-only delivery JSON check. Required: sentences=[{sentence_id,paragraph_id,order,text,evidence_ids:[],source_ids:[]}], paragraphs=[{paragraph_id,text}]. Sort sentences per paragraph by positive integer order and concatenate text without adding spaces. Empty source_ids needs basis=own_observation|author_provided|author_confirmed|own_calculation|author_transition|retained_accepted. Observation, author, and calculation bases require nonempty valid evidence_ids; author_transition may omit evidence; retained_accepted needs nonempty basis_ref. Text must contain non-whitespace content; original edge spaces are preserved in exact comparison. Optional propositions=[] is for human meaning review only. Many-to-many evidence/source links are supported; semantics and cross-version ID stability are not inferred.")
    delivery.add_argument("--project-dir", required=True)
    delivery.add_argument("--file", required=True, help="Delivery JSON; sentences.text must be the final delivered text")
    delivery.set_defaults(handler=delivery_check)
    return parser


def main():
    args = make_parser().parse_args()
    try:
        result = args.handler(args)
        return result if isinstance(result, int) else 0
    except (ValueError, OSError, TypeError, OverflowError) as exc:
        # Avoid leaking local absolute paths in shareable diagnostics.
        message = "Unable to read or write a requested local file" if isinstance(exc, OSError) else str(exc)
        print(json.dumps({"error": message}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
