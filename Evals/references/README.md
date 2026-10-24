# Bundled evaluation references

All required local references are inside `Evals/` and `claude/`. Read this index
with `Evals/WORKFLOW.md` and `Evals/ENVIRONMENT.md`. Those shared contracts and
the selected numbered Eval contain the current procedure and explicit policy
overrides. No external guide, template or sample folder is required. The three sibling
base folders in `../UNIVERSE_MAP.md` supply universe data for direct search.

| Reference | Purpose and when to read |
|---|---|
| `source_layout.json` | Export filenames and array pointers for direct navigation; use `hg_reference.py routes`. Not a SQL schema or a guarantee that data is present. |
| `search_indexes/manifest.json` and indexed artifacts | Helper-managed prepared record offsets for GitHub/GDrive/Linear/Snowflake. Include in uploads; the helper validates them automatically. Do not dump these machine artifacts into the evaluation context. |
| `rules/scoring.json` | Existing scored dimensions, error labels and thresholds; read the selected stage's dimensions. |
| `rules/oracle_events.md` | OE completeness/accuracy scoring and evidence record for `/oe`; replaces the active golden stage. |
| `rules/scoring_notes.md` | Interpret scored dimensions, stage overrides and evidence limits. |
| `rules/task_categories.md` | Six business-function categories; use when reviewing assignment fit. |
| `rules/common_errors.md` | Prompt and rubric common-errors checklist; the deep recheck passes at the end of `/prompt` and `/rubric` fill it. |
| `rules/deep_recheck.md` | The deep recheck that ends `/prompt`, `/oe` and `/rubric`: one blind pass per common fail, the main-session check, and the `## Deep Recheck` section that holds the final verdict. |
| `rules/coherent_record.md` | The coherent_record atomicity exception and the consistency contract (coverage before critique, reproducible counts, direction of authority, stable revisions, score binding) under `rubric-revision-v9`. |
| `rules/long_horizon.md` | Long Horizon tier guidance, cohort coverage, necessary work, context injection and the large audit-table exception; use when applicable. |
| `rules/all_failing.md` | Diagnose an all-failing criterion when actual run evidence exists. |
| `persona/roster.json` and `persona/acl.md` | The user's 17-person roster and existing read-access rules. |
| `tools/catalog.json` | Supplied tool names and parameters for all 13 services plus gateway; use for declared task-agent capabilities, not local search commands. |
| `schema/injection.json` and `schema/README.md` | Existing injection database schema snapshot and its verification limits. |
| `schema/snowflake.json` and `schema/README.md` | Explicit Snowflake service table definitions from the supplied universe archive. |

Rubric evaluation rules live in `Evals/3_Rubrics_Eval.md`; rubric generation is
retired. `/hint` was removed on 2026-09-26; `Evals/Authoring_Workflow.md` records that no stage authors artifacts.
Project guidelines, the QC spec and the QC rating form live in `Evals/Docs/` (see `Evals/Docs/README.md`).
Company facts, relationships, scenarios and source records come from the
selected local archive and applicable task attachments. The roster does not
expand when additional contacts appear there.

No raw sample corpus is bundled. `../1B_Haiku_Prediction_Eval.md` is the Haiku-only prediction eval;
Opus reviews load `../1A_Hardness_Eval.md` instead. The former
`rules/opus_failure_patterns.md` and `rules/hardness_calibration.md` remain
historical records, not active scoring dependencies or task requirements.
Apply other sample-comparison checks only to samples explicitly supplied for
the current review. With none supplied, mark that comparison not applicable
without blocking other checks or claiming corpus-wide originality.

The manifests record reference provenance and verification limits. Original
source filenames in manifests describe provenance, not files required at runtime.

The shared `schema/` folder contains files for different databases. The injection
snapshot describes the backing database targeted by universe-edit SQL. The
Snowflake snapshot describes analytical tables exposed through that service.
Other service exports contain record shapes but no equivalent explicit table
definitions, so they were not converted into invented SQL schemas.

Use `../SEARCH.md` for local search commands and `universe_manifest.json` for
archive provenance, service locations, and extracted coverage.

`rules/rubric_checks.md`: mandatory v10 evidence-linked scoring checks for
evaluation-only AUDIT; complements `rules/review_scoring.md`.
