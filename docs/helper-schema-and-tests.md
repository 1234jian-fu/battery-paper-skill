# Helper record schema and executed checks

All examples and test fixtures here are **SYNTHETIC**. They are not real literature,
experimental facts, author acceptance, or scientific verification.

The helper uses only Python's standard library. Its checks do not establish that
research was actually read, that evidence is genuine, that prose preserves meaning,
or that a scientific conclusion is correct. No manuscript is rewritten.

## Project initialization

`init --project-dir <explicit-existing-dir> --name <name>` creates only missing files:

- `.paper-writing/project.json`
- `.paper-writing/evidence.json`
- `.paper-writing/sources.json`
- `.paper-writing/decisions.md`
- `.paper-writing/issues.md`
- `.paper-writing/drafts/`

Both evidence and source `items` arrays start empty. The new policy is
`{"minimum":60,"target":60,"recent_years":5}`. Existing files and policies remain
byte-for-byte unchanged. Missing or different policy records report
`needs_policy_update`. Updating them requires an explicit recorded author decision.

`corpus` audits the 60/60/5 standard and reports the recorded policy separately.
It does not adopt or rewrite that policy. A legacy policy blocks the overall
`target_met_by_record` status even when the counted records reach 60.

`corpus` and `sources` require an explicit `--as-of YYYY-MM-DD` supplied by the
client/task. There is no system-clock fallback. The rolling window is inclusive
from cutoff minus five calendar years through cutoff; the lower boundary clamps
February 29 when necessary. A year or month date qualifies only when the complete
date interval lies within that window. Overlaps require date verification.

## Evidence and source shapes

Both files require an object with `items`. Minimal ID structure accepted by `check`:

```json
{
  "schema_version": 1,
  "items": [
    {"evidence_id": "SYNTHETIC-EV-1", "observation": "Synthetic structural fixture only"}
  ]
}
```

`source_id` substitutes for `evidence_id` in `sources.json`. This minimal source
shape does **not** qualify for the reading baseline. Each ID must be a nonempty
unique string. A recorded DOI is normalized for duplicate detection. Authors may
add locators, file paths, evidence boundaries, and other project fields; this helper
does not validate their scientific content.

A complete synthetic source shape that passes the recorded qualification checks:

```json
{
  "schema_version": 1,
  "items": [
    {
      "source_id": "SYNTHETIC-SRC-1",
      "unique_work_id": "synthetic-not-a-real-work-1",
      "title": "SYNTHETIC TEST ONLY; not a real publication",
      "source_type": "primary_research",
      "bibliographic_status": "verified",
      "publication_date": "2025-06-01",
      "publication_date_verified": true,
      "date_source_url": "https://example.invalid/synthetic-only",
      "date_basis": "publisher_first_online",
      "topical_fit": "direct",
      "fit_reason": "Synthetic test field; no scientific fit is claimed",
      "read_scope": ["relevant_body"],
      "exact_locations": ["SYNTHETIC section 1"],
      "chinese_meaning": "合成测试记录，不代表真实阅读",
      "source_paragraph_move": "SYNTHETIC argument move",
      "source_data_expression": "SYNTHETIC expression, no real data",
      "linked_figure_tasks": ["SYNTHETIC-FIG-1"]
    }
  ]
}
```

An identifiable syntactically valid DOI can substitute for `unique_work_id`.
Accepted research types are `primary_research` and `methods_research`.
Accepted fit values are `direct` and `shared_test` with a nonempty `fit_reason`.
Accepted body-read scopes are `relevant_body`, `full_main_text`, and
`full_main_and_SI`; a string or array is accepted. Abstract, secondary-card,
old-index, and `prior_read_scope` fields alone do not qualify. Accepted date bases
are `publisher_first_online` and `publisher_formal_publication`, with a verified
date and nonempty date-source URL. Corrections, errata, retractions, and preprints
are excluded. Qualifications are record assertions, not independently verified facts.

`sources --project-dir <dir> --query <terms> --as-of <date>` searches only that
project's `.paper-writing/sources.json`. It has no bundled historical index.

## Delivery shape

```json
{
  "schema_version": 1,
  "sentences": [
    {
      "sentence_id": "SYNTHETIC-S1",
      "paragraph_id": "SYNTHETIC-P1",
      "order": 1,
      "text": "First synthetic sentence. ",
      "evidence_ids": ["SYNTHETIC-EV-1"],
      "source_ids": ["SYNTHETIC-SRC-1"]
    },
    {
      "sentence_id": "SYNTHETIC-S2",
      "paragraph_id": "SYNTHETIC-P1",
      "order": 2,
      "text": "Second synthetic sentence.",
      "evidence_ids": [],
      "source_ids": [],
      "basis": "retained_accepted",
      "basis_ref": "SYNTHETIC acceptance record version 1; not real acceptance"
    }
  ],
  "paragraphs": [
    {"paragraph_id": "SYNTHETIC-P1", "text": "First synthetic sentence. Second synthetic sentence."}
  ],
  "propositions": [
    {"proposition_id": "SYNTHETIC-PROP-1", "text": "Human meaning-review fixture only", "sentence_ids": ["SYNTHETIC-S1"]}
  ]
}
```

`delivery-check --project-dir <dir> --file <delivery.json>` groups the final
`sentences[].text` by `paragraph_id`, sorts by positive integer `order`, and
concatenates without inserting separators. The result must exactly equal the
matching `paragraphs[].text`. Punctuation, Unicode, internal/edge spaces, and
newlines are not normalized. Sentence and paragraph IDs must be unique; sentence
IDs must also be nonempty strings without whitespace. Authors retain those IDs
across revisions; a single-file check cannot infer cross-version stability.

Every evidence/source ID in a sentence must resolve to the existing project's
`evidence_id`/`source_id`. Many-to-many arrays are supported. Empty `source_ids`
requires `basis` of `own_observation`, `author_transition`, or `retained_accepted`.
For `retained_accepted`, nonempty `basis_ref` is also required; the helper checks
only that the reference text exists, not whether acceptance actually occurred.
Optional `propositions` must be an array and are left for human meaning review.

Exit codes: `0` completed check/no structural errors; `1` structural errors;
`2` invalid arguments, unreadable files, or unusable input. A policy-migration
warning is reported in JSON without changing files and does not itself use code 1.

## Actual executed tests

Executed with the installed Python 3.14 interpreter, with `BATTERY_SKILL_DIR` set
to the new skill directory:

```powershell
$env:BATTERY_SKILL_DIR = '<skill-dir>'
py -3.14 -X utf8 './test_paper_workbench.py'
```

Final run: **22 tests, 0 failures, 0 errors; 7.657 seconds**. The machine-readable
`test_summary.json` records results without local absolute paths. The tests cover
the 59/60 threshold; all five-year boundaries, future dates, date precision, and
leap day; normalized duplicate DOI counting; abstract/legacy-card exclusions;
empty fact-free initialization; preservation of existing files and old policies;
explicit project/date arguments; project-source querying; read-only checking;
text-region counting; exact delivery reconstruction; stale sentence tables,
punctuation and internal-space mismatches; ID resolution and uniqueness;
many-to-many references; and no-source acceptance-record handling.

Temporary directories are created beside this test file and removed after each
test. No network or external libraries are used. The test source is portable via
`BATTERY_SKILL_DIR` or a repository containing `battery-paper-skill/scripts/`.
