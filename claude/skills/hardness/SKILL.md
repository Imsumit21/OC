---
name: hardness
description: "Assess Opus difficulty from one unhinted run: judge Opus directly, or predict Opus difficulty from a Haiku fallback using transfer checks. Inputs are the exact prompt, optional injection SQL and prompt reference files. Report PASS, NON-FAIL or FAIL. Use /hardness in chat or with a task folder."
---

# Hardness: choose the eval from the submitted run

Be a **ruthlessly thorough, evidence-based grader**. Apply the **Ruthless
grading standard** in `Evals/WORKFLOW.md`: actively challenge acceptance,
substantiate findings, and preserve this stage's scope, evidence limits and
scoring rules.

Follow `Evals/INPUTS.md`: run `python3 Evals/tools/hg_store_input.py list`, save
newly supplied inputs and read relevant saved contents. New versions replace
their own key; omitted inputs stay saved. Reuse them before asking again.

Inputs: exact prompt, one unhinted trajectory JSON, optional injection SQL (or
explicit no injection), and reference files used by the prompt, if any. No
OE, rubric, verifier, calibration batch or second run is required.
Save runs under the actual model: `save opus --source "<run.json>"` or
`save haiku --source "<run.json>"` with `Evals/tools/hg_store_input.py`.
Keep separate `Evals/task_inputs/opus/trajectory.json` and
`Evals/task_inputs/haiku/trajectory.json`; preserve raw bytes and provenance.

Treat a single run submitted for this `/hardness` review or in an intake reply
as the user's selection. Route by its actual model even if the other model has
an older saved entry. Without a current selection, read `hardness_intake` and
prefer matching unhinted Opus, then Haiku if Opus is unavailable. A newly submitted
Opus run becomes the saved default. When only Haiku is supplied, use it without requesting
backfill. Confirm actual model, unhinted status and task/source match from the
export/context; filenames and input keys do not establish model identity.
Resolve NEEDS_ATTENTION, SOURCE_SUPPLIED or conflicting labels before silently
skipping a candidate. A demonstrably ineligible run can be excluded with a reason.
Never choose the worst run or combine runs; ask only about a material ambiguity.

## Load exactly one eval

Choose automatically from the selected run's confirmed model, without asking
the user to choose an evaluation mode:

| Run model | Read in full | Mode |
|---|---|---|
| Opus | `Evals/1A_Hardness_Eval.md` | `OPUS_OBSERVED` |
| Haiku | `Evals/1B_Haiku_Prediction_Eval.md` | `HAIKU_TO_OPUS` |

Load only the matching eval, not both. The selected eval contains its evidence,
scoring, limits and report instructions. If model identity is unresolved, resolve
it before selecting a scored path. Never relabel the trajectory or inherit an
earlier model's score. This is one `/hardness` command, not separate user commands.

If the Haiku cohort-sweep check applies, use `WORKFLOW.md`'s `horizon-tiers-v1`
and the shared horizon guide: 500+ calls belongs to Super Long Horizon, not
Long Horizon. Call volume alone never establishes predicted or observed difficulty.

If injection intake is unresolved, ask with other missing inputs: **Injection
SQL (optional): does this task use any? If yes, paste or attach it; if not, say
no injection.** Save the explicit answer with `hg_store_input.py no-injection`.
Ask for prompt reference files only when needed and not already supplied. Save
partial inputs, then wait for unresolved intake; do not fabricate a report.

For explicit task-folder mode only, use the selected eval's structural preflight
with `/hardness "<task>" [--trajectory "<run.json>"]`. Existing invalid preferred
inputs remain issues; indexed integrity takes precedence over file-only routing.

Read EXECUTION, ENVIRONMENT, UNIVERSE_MAP and SEARCH once per current version.
Use `python3 Evals/tools/hg_reference.py guide hardness` for applicable shared
WORKFLOW/scoring sections instead of duplicate reads. Use local sources and
supplied files; preserve persona/ACL, authority, capability and source-version
checks. Never replay commands, execute SQL, use workplace connectors or launch
models from the review. HOLD never prevents obtaining a run needed for assessment.

Both paths apply `WORKFLOW.md`'s `prompt-incorporation-v1` contract: only the
prompt and incorporated instructions establish requirements. Exclude apparent
failures caused only by unmentioned handbook/policy rules from observed Opus
difficulty and Haiku-to-Opus prediction. Reassess older requirement maps before reuse.

Both paths use `model-aware-v3`, PASS / NON-FAIL / FAIL, and the same fixed report:
`Evals/task_inputs/reports/1a_hardness.md`. Save via
`python3 Evals/tools/hg_write_output.py hardness --source "<completed-report.md>"`
and return the path after verification. Preserve earlier reports as history.

Search helpers under `Evals/SEARCH.md` automatically validate matching bundled
indexes on first use and reuse complete raw-record results across supported
services when their request/source/manifest/helper versions match. No additional
user command is needed. Cache hits supply source evidence only; apply every
current input, SQL, persona/ACL, evidence and grading requirement as written.

For several already located records, use
`python3 Evals/tools/hg_search.py get-many --request <reads.json> --compact`
with SEARCH's request format. Finish required pages and retain each item's
errors; selected reads do not prove collection-wide absence or full history.
Targeted batch queries use verified offsets when efficient; broad queries keep
one shared scan. These routes preserve every required grading check.

For already known source services/schema tables, combine the complete reference
views with `hg_reference.py guide hardness --services <service> ... --tables <table> ...`;
omit unneeded flags and avoid repeating the corresponding standalone reads.
Under SEARCH.md, individual record checks survive display-ID/order changes when
their evidence scope and dependencies match. `lookup` automatically uses a
verified prepared identity index where available, with complete-scan fallback.
These helpers reuse evidence only; complete all current grading checks.
