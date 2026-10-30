# Helper records and check boundaries

All examples are **SYNTHETIC**, not real literature, experiments or author acceptance.
The helper uses only Python's standard library. It does not rewrite manuscripts,
verify source-reading claims, check scientific truth, or prove faithful meaning.

## Initialization and policy

init requires an explicit existing project directory. It creates only missing
.paper-writing/project.json, evidence.json, sources.json, decisions.md, issues.md
and drafts/. Evidence and source items start empty. Existing files stay unchanged.
Resolved context, required-record and drafts paths must stay within the explicit
project; external symlinks/junctions are rejected before record access. Internal
links remain supported. Required records must be files, not same-named directories.

The default corpus_policy is minimum=60, target=60, recent_years=5. An old policy
without an explicit author decision is preserved and flagged needs_policy_update.
To use an author-requested policy, record both valid positive integers
(target must be at least minimum) and a real decision reference:

~~~json
{
  "corpus_policy": {"minimum": 80, "target": 80, "recent_years": 5},
  "corpus_policy_override": {
    "authorized_by": "user",
    "decision_ref": "decisions.md#synthetic-example-of-a-recorded-decision"
  }
}
~~~

The marker is a record assertion, not authentication. Do not create it without an
actual author instruction. Outputs show default_policy, effective_policy and
effective_policy_source. The helper never silently migrates or edits the project.

corpus and sources require client/task --as-of YYYY-MM-DD. Dates are inclusive.
The default window is five calendar years; an explicitly authorized policy may
change it. first_online_date takes precedence over publication_date/issue year;
an invalid explicitly supplied first-online date is not replaced by a newer issue
date. Year/month precision qualifies only when its whole interval is in range.

## Evidence and source IDs

Both JSON files use an object with an items array. IDs are nonempty unique strings:

~~~json
{
  "schema_version": 1,
  "items": [
    {
      "evidence_id": "SYNTHETIC-EV-1",
      "provenance": "author_confirmed",
      "description": "Synthetic method description; not a verified experiment"
    }
  ]
}
~~~

sources.json uses source_id instead. Minimal ID records do not qualify as a read
corpus. Duplicate source_id blocks readiness. Multiple entries for the same study
must not inflate work count: DOI spellings are normalized and shared
unique_work_id joins DOI/no-DOI aliases transitively. Keep one canonical source card
for final use; check flags duplicate work records for consolidation.

Qualification requires a formal original research identity (primary_research or
methods_research), verified bibliography/date, date-source URL and publication
basis, direct/shared_test fit with a nonblank fit_reason, actual relevant-body
reading scope, exact_locations, chinese_meaning, source_paragraph_move and
source_data_expression. DOI or verified unique_work_id identifies the work.

The explanatory fields must be nonblank text; exact_locations may instead be a
nonempty array of nonblank text. unique_work_id, when supplied, must be nonblank
text. A missing field keeps a candidate incomplete; boolean/object/blank values
cannot substitute for completed reading. Task IDs in required_figure_tasks and
linked_figure_tasks must be nonblank strings, never coerced from numbers/objects.

Metadata, abstracts, secondary cards, old indexes and prior_read_scope alone do
not establish current reading. No helper can verify that a user really read the
paper. Figure-tag coverage also does not prove sentence-level mapping is complete.

date_source_url must have HTTP/HTTPS syntax and a host; this is not an online
verification of the page or its authority. Explicit malformed first_online_date
values, including false, 0 and empty containers, remain date_unknown; only absent,
null or empty-string values permit the documented publication-date fallback.
All commands operate locally. sources filters existing records; it does not search
the web, download papers or establish that the recorded papers were read.

## Delivery JSON

~~~json
{
  "sentences": [
    {
      "sentence_id": "SYNTHETIC-S1",
      "paragraph_id": "SYNTHETIC-P1",
      "order": 1,
      "text": "Synthetic preparation description.",
      "evidence_ids": ["SYNTHETIC-EV-1"],
      "source_ids": [],
      "basis": "author_confirmed"
    }
  ],
  "paragraphs": [
    {
      "paragraph_id": "SYNTHETIC-P1",
      "text": "Synthetic preparation description."
    }
  ]
}
~~~

delivery-check groups sentences by paragraph_id, sorts positive integer order,
then concatenates text without adding separators. Punctuation, internal/edge
spaces and newlines are compared exactly. Text must contain non-whitespace
content. Sentence/paragraph IDs must be unique; references resolve to existing
project records. Many-to-many links are supported.

Empty source_ids requires one of:
- own_observation, own_calculation, author_provided, author_confirmed: nonempty,
  valid evidence_ids are required. An author method record is not a measured result.
- author_transition: evidence may be absent for pure organization.
- retained_accepted: a nonblank basis_ref is required when sources are absent;
  the helper cannot verify actual acceptance.

Optional propositions is an array for human review. Basis labels do not prove
scientific support. The check only compares JSON-internal text and references;
it does not automatically extract the final Markdown/Word or browser text.
Compare the actual delivered prose separately before claiming full consistency.

## Commands, exit codes and tests

Run the appropriate subcommand --help for arguments. Exit 0 means no recorded
structural errors; exit 1 means structural errors; exit 2 means unusable input or
arguments. A policy-migration warning does not modify files.

The initial 22 tests remain unchanged. The earlier logic audit added 28 regressions;
the 2026-10-30 local audit added 9 more (59 tests total). All 59 passed on the
audited local revision. See helper-test-summary.json for version and runtime data;
logic-audit.md is the earlier audit. The separate evals/ layer contains 8 black-box
CLI checks and 115 assertions, including independently derived numeric expectations.
Fixtures are synthetic and portable. Reproduce:

~~~text
python -B -X utf8 -m unittest discover -s tests -p "test_*.py" -v
~~~
