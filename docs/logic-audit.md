# Logic audit and corrections

Date: 2026-10-29. The audit used isolated **synthetic** records and requests.
No manuscript, experimental dataset, literature PDF or local path is published.

## Confirmed issues and minimal fixes

| Issue | Reproduction before correction | Corrected behavior |
|---|---|---|
| Study identity versus source-card identity | Thirty synthetic works, each represented by DOI/no-DOI aliases sharing a work ID, counted as sixty. Repeated source IDs could also hide behind a corpus count. | Transitive alias aggregation counts thirty works; duplicate source IDs block readiness and report structural errors. |
| Incomplete or invalid records | Whitespace and wrong-type reading fields could qualify; numeric task IDs could be coerced into strings; whitespace-only prose could be accepted. | Reading/ID types are checked, invalid records cannot establish readiness, task IDs are not coerced, and blank prose is rejected. |
| Author-provided methods and computations | A legitimate methods candidate using author_confirmed was rejected for lacking an external paper source. | author_provided, author_confirmed and own_calculation are allowed with valid evidence records. Author methods are not mislabeled as measured observations. T-method and T-result are distinguished. |
| Explicit author policy changes | An author-requested eighty-work policy still reported the default sixty-work gap. | A valid explicit user decision marker activates the recorded policy. At sixty works, an eighty-work target has a gap of twenty. Unmarked legacy policies still require migration. |
| Publication timing | A newer publication/issue date could override an explicitly older first-online date. | first_online_date controls recency; a later issue date cannot make the work recent. |
| English source-mapping wording | One sentence could be interpreted as requiring an external source ID for every final sentence. | External sources are linked only when applicable; original transitions, own evidence, author methods and accepted prose do not require invented source quotations. |

## Check scope made explicit

JSON-internal sentence/paragraph equality is different from checking the actual
Markdown, Word or displayed prose. The helper does not parse those artifacts.
The final delivered text must be compared separately before claiming full
consistency. A basis label or a passed structural check does not prove scientific
support, faithful meaning or an actual author decision.

## Executed validation

- A read-only rules review examined the entrypoint and all eight reference files;
  a follow-up review closed the English-source wording conflict.
- Forty new CLI probes exposed record and delivery boundary failures.
- The original twenty-two unit tests were preserved. Twenty-eight targeted
  regressions were added. **All fifty tests passed.**
- The frozen probe commands and the methods delivery were rerun after correction:
  forty-one CLI calls, with eleven explicit post-fix expectations checked.
  Input fixture files were unchanged.
- The methods scenario retained its missing-parameter boundaries, no-search
  scope and introduction protection. Its four author-confirmed sentences now
  pass delivery checking; both paragraphs match exactly.

The tests do not constitute a sixty-paper real-literature writing exercise,
scientific peer review, or manuscript-to-Word validation. Those paths still
need task-specific source access, evidence and artifact checks in actual use.
