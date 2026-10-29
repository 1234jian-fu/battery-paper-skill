# Validation scope

This package is a generalized battery-paper writing skill. It contains no user manuscript, experimental dataset, literature PDFs, credentials, or local project snapshot.

## Structure and helper checks

- The installed skill passed the available skill-creator structural validator.
- The portable repository helper tests were actually executed: **22 tests, zero failures or errors**.
- The tests cover the recorded 60-work threshold, date boundaries and precision, duplicate-source counting, non-overwriting initialization, legacy-policy warnings, ID resolution, and exact sentence-to-paragraph consistency.
- Internal documentation links and UTF-8 files were checked.
- The public package was checked for local absolute paths, credential-like tokens, and unintended manuscript/data files; no such content was selected for publication.

All test records are **synthetic**. Record assertions do not establish actual source reading, scientific relevance, or scientific validity. A passed delivery check establishes exact text/ID structure, not faithful meaning.

## Independent behavioral trials

Two agents independently read and used the skill in isolated synthetic workspaces. They were given only a realistic task and its raw input files, not an intended answer.

1. **Sulfide solid-state battery outline:** with only four figure-group descriptions, produced scoped figure/paragraph duties, preserved the requested contact-evolution → impedance → device-performance thread, and retained the introduction lock. It did not invent figures, numbers, source quotations, or completed literature reading.
2. **Hard-carbon English evidence correction:** corrected a direction error against a supplied table, retained the defined material name and hyphen, and removed unsupported electronic-conductivity and all-operating-condition conclusions. The sentence table, final paragraph, JSON, and separate prose file were actually checked for consistency; delivery-check returned exact_match=true.

These trials exercise task scoping, transfer to different battery directions, evidence boundaries, and final delivery consistency. They are not external expert peer review, experimental validation, a 60-paper corpus, or a test of journal acceptance. Full literature retrieval and manuscript-to-Word assembly were not exercised in these trials.

## Reproduce helper checks

From the repository root:

~~~text
python -X utf8 -m unittest discover -s tests -p "test_*.py" -v
~~~

No external Python packages or network are needed for the helper tests. Source-paper research and document operations use whichever authorized tools are available in the host environment.
