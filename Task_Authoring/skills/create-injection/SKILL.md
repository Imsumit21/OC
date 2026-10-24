---
name: create-injection
description: "Implement the /create-scenario design as injection SQL for the HarmonyGames universe: ≥ 10 of 13 schemas, ≥ 120 rows, asks and evidence spread over ≥ 10 containers, hidden authorities with decoys, cohort surfaces, traps and supersessions, cited grounding dossier, findability and persona-reach proof. Runs tools/sql_lint.py, tools/base_check.py and tools/hardness_gate.py against the SQL (all must PASS) and records a Self-review (GEN_EXECUTION §6a). Use /create-injection after /create-scenario. Writes Task_Authoring/task_inputs/01_Universe_Inject.sql + 01_Grounding_Dossier.md + final 01_Hardness_Manifest.json. Never executes SQL; never writes to Evals/, claude/ or HarmonyGames_*."
---

# Universe injection SQL + grounding dossier (01)

Resolve this file through any symlink to locate `<bundle>/skills/<name>/SKILL.md`.
The bundle's parent is the workspace. Read `<bundle>/setup/GEN_EXECUTION.md` first, then follow the playbook
`Task_Authoring/playbooks/01_Universe_Injection.md` in full. Write only under
`Task_Authoring/task_inputs/`; never write to `Evals/`, `claude/` or `HarmonyGames_*`,
and never execute SQL.

## Inputs

First run `python3 Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source`.
Use the shared `Working_Files/00_Task_Context.json` (all eight assigned fields,
registered shared data source and assigned freeze). Both dates use the same local
data; validate relied-on record dates and earlier state before grounding. V3
changed-topic rules govern over older Evals text. The existing Long→extreme and
Normal design limits remain local policy; Eval Portal is handled by the user.

Upstream slots in `Task_Authoring/task_inputs/`: `00_Assigments.md`, `01_Scenario_Design.md`, `01_Hardness_Manifest.draft.json` (the draft from `/create-scenario`). Nothing from later stages (reference files, error/async configuration, hardening report) — a hardening pass is revision N+1 and re-runs this stage's gate. If a required one is
missing, stop and name it. Ground every fact through `Task_Authoring/tools/hg.py search` and
apply the persona ACL yourself (search does not).
Universe KB (playbook S1/S4): seeded speakers from `references/universe_kb/activity.json`, lengths/hours/title and branch patterns from `conventions.json`, companions from `integrations.json`, the touched-data census against `coherence_hazards.json`. Declare every load-bearing fact in the manifest's `facts` (per-record facts with `home_ids`); `tools/fact_check.py --no-leak` verifies them. Prove reach with `tools/persona_view.py check-sql <persona> <sql> --load-bearing <ids>`.

## Output
`task_inputs/01_Universe_Inject.sql`, `task_inputs/Working_Files/01_Grounding_Dossier.md` and the final `task_inputs/Working_Files/01_Hardness_Manifest.json` (every draft id kept or listed in `design_delta`; same `effective_profile`; verbatim `delegation_quote`s; `version_records` in the records' real time order; hazard acknowledgements with a verified `resolution`). Linear comments are a ● load-bearing carrier (`Ask_Carriers.md` §6b); anchors are named by noun phrases of ≤ 6 words in the dossier's anchor-name table.

## Stage gate (blocking)
Run `python3 Task_Authoring/tools/stage_gate.py injection Task_Authoring/task_inputs --paste`. Handoff is blocked until it prints `STAGE GATE <stage>: PASS`; `--paste` writes that output into the Self-review, and the next stage's gate refuses an upstream artifact without a current PASS block. It checks structure and freshness, evidence pointers, pasted tool outputs (re-run and compared), persona reach, universe-KB use and the self-review's counter-readings. Fix the artifact; never edit the gate's output.

## Deliver
Report the output path(s), the `sql_lint.py`, `base_check.py`, `fact_check.py`, `persona_view.py check-sql`, `hardness_gate.py` and `stage_gate.py injection` verdicts verbatim, any blocking findings, the Self-review (playbook S7: `/injection` Checks A–C walk, touched-data census, one counter-reading per QC coherence category incl. pre-existing and sibling defects, warning dispositions), and the next step: paste the SQL into `/injection`; then `/create-error-async` (optional) and `/create-prompt-writing`.
