---
name: create-injection
description: "Implement the /create-scenario design as injection SQL for the HarmonyGames universe: ≥ 10 of 13 schemas, ≥ 120 rows, asks and evidence spread over ≥ 10 containers, hidden authorities with decoys, cohort surfaces, traps and supersessions, cited grounding dossier, findability and persona-reach proof. Runs tools/sql_lint.py, tools/base_check.py and tools/hardness_gate.py (all must PASS), then the preflight (solver contract, every mutation result dispositioned, geometry able to reach the cap — blocking; liveness and forecast advisory), and records a Self-review (GEN_EXECUTION §6a). Use /create-injection after /create-scenario; revision N+1 is this stage again. Writes Task_Authoring/task_inputs/01_Universe_Inject.sql + 01_Grounding_Dossier.md + final 01_Hardness_Manifest.json + the solver and 01c_Preflight_Report.json. Never executes SQL; never writes to Evals/, claude/ or HarmonyGames_*."
---

# Universe injection SQL + grounding dossier (01)

Resolve this file through any symlink to locate `<bundle>/skills/<name>/SKILL.md`.
The bundle's parent is the workspace. Read `<bundle>/setup/GEN_EXECUTION.md` first, then follow the playbook
`Task_Authoring/playbooks/01_Universe_Injection.md` in full. Write only under
`Task_Authoring/task_inputs/` (plus the forecast's ledger append through its tool, GEN_EXECUTION §1); never write to
`Evals/`, `claude/` or `HarmonyGames_*`, and never execute SQL.

## Inputs

First run `python3 Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source`.
Use the shared `Working_Files/00_Task_Context.json` (all eight assigned fields,
registered shared data source and assigned freeze). Both dates use the same local
data; validate relied-on record dates and earlier state before grounding. V3
changed-topic rules govern over older Evals text. The existing Long→extreme and
Normal design limits remain local policy; Eval Portal is handled by the user.

Upstream slots in `Task_Authoring/task_inputs/`: `00_Assigments.md`, `01_Scenario_Design.md`, `01_Hardness_Manifest.draft.json` (the draft from `/create-scenario`), `Working_Files/01_Gradable_Surface.json` (read only: never rewritten here; expected values and `flipped_by` go into the preflight report). Nothing from later stages (reference files, error/async configuration, hardening report) — a hardening pass is revision N+1 and re-runs this stage's gate. If a required one is
missing, stop and name it. Ground every fact through `Task_Authoring/tools/hg.py search` and
apply the persona ACL yourself (search does not).
Universe KB (playbook S1/S4): seeded speakers from `references/universe_kb/activity.json`, lengths/hours/title and branch patterns from `conventions.json`, companions from `integrations.json`, the touched-data census against `coherence_hazards.json`. Declare every load-bearing fact in the manifest's `facts` (per-record facts with `home_ids`); `tools/fact_check.py --no-leak` verifies them. Prove reach with `tools/persona_view.py check-sql <persona> <sql> --load-bearing <ids>`.

## Output
`task_inputs/01_Universe_Inject.sql`, `task_inputs/Working_Files/01_Grounding_Dossier.md` and the final `task_inputs/Working_Files/01_Hardness_Manifest.json` (every draft id kept or listed in `design_delta`; same `effective_profile`; verbatim `delegation_quote`s; `version_records` in the records' real time order; hazard acknowledgements with a verified `resolution`). Linear comments are a ● load-bearing carrier (`Ask_Carriers.md` §6b); anchors are named by noun phrases of ≤ 6 words in the dossier's anchor-name table. The final manifest also carries the `mechanism_portfolio`, `solver {path, digest}`, `gradable_surface` and `preflight {report, digest}`. Plus `Working_Files/solver/solver.py` (+ `solver/truth.json`; every total in the dossier and in Facts for the human comes from it), `Working_Files/01c_Dispositions.json` and `Working_Files/01c_Preflight_Report.json` (+ `.md`). Store this revision's SQL byte for byte in `Working_Files/run_forensics/<rev>/01_Universe_Inject.sql` (playbook S5e): every later intake binds runs against every stored revision.

## Preflight (playbook S4b–S5e)
- Blocking: the solver declares `RULES[r].controls` (+ `over_application`), `CHANNELS` and `base_route(record_id)` (S4b); `python3 Task_Authoring/tools/oracle_kit.py check --task-dir Task_Authoring/task_inputs [--previous-sql <revision N-1 SQL> --previous-truth <its truth.json>]` → PASS, including `contract.controls` (every declared control member is a solver key; every over-application operator and channel is live) (S4b); `python3 Task_Authoring/tools/difficulty_mutation.py mutate --task-dir Task_Authoring/task_inputs` with a written disposition for every rule, channel degrade and intervention result in `01c_Dispositions.json` (S5b; EQUIVALENT is never auto-labelled FALSE); geometry U > 1 − cap (S5b′), and a non-composable solver's U UNVERIFIED needs a written `geometry.U` disposition.
- Advisory, UNCALIBRATED: the geometry margin L_max; `tools/trap_liveness.py` flags, each with a written disposition (S5c); optional blind probes (S5d); `python3 Task_Authoring/tools/hardness_forecast.py forecast --task-dir Task_Authoring/task_inputs --model <baseline model> --preregister [--channel-rate <channel>=<e>]` (S5e), pre-registered in the ledger before the platform run. A declared channel takes its rate from the model's ledger records of its family; with no record, pass a disclosed `--channel-rate` or the forecast prints UNPARAMETERIZED and does not simulate it.
- Then `python3 Task_Authoring/tools/preflight_report.py --task-dir Task_Authoring/task_inputs [--forecast <forecast.json>]` writes the report, bound by sha256 to the SQL, solver, surface, manifest and dispositions; any later edit to one of them makes it stale.

## Stage gate (blocking)
Run `python3 Task_Authoring/tools/stage_gate.py injection Task_Authoring/task_inputs --paste`. Handoff is blocked until it prints `STAGE GATE <stage>: PASS`; `--paste` writes that output into the Self-review, and the next stage's gate refuses an upstream artifact without a current PASS block. It checks structure and freshness, evidence pointers, pasted tool outputs (re-run and compared), persona reach, universe-KB use and the self-review's counter-readings, plus the preflight: bound to the current files (`structure.preflight`), the solver contract (`solver.contract`, re-run with `--rerun all`, including `contract.controls`), every mutation result, channel degrade and intervention dispositioned (`mutation.dispositions`) and geometry U (`geometry.upper_bound`, re-run; U counts channel degrades and over-application operators); the geometry margin, liveness dispositions and the forecast are WARN only. Fix the artifact; never edit the gate's output.

## Deliver
Report the output path(s), the `sql_lint.py`, `base_check.py`, `fact_check.py`, `persona_view.py check-sql`, `hardness_gate.py`, `oracle_kit.py check` (`contract.controls`), `preflight_report.py` and `stage_gate.py injection` verdicts verbatim, the mutation dispositions, U and L_max per gate view, the liveness flags with their dispositions and the pre-registered forecast id with its P(all gates) range (UNCALIBRATED), any blocking findings, the Self-review (playbook S7: `/injection` Checks A–C walk, touched-data census, one counter-reading per QC coherence category incl. pre-existing and sibling defects, warning dispositions), and the next step: paste the SQL into `/injection`; then `/create-error-async` (optional) and `/create-prompt-writing`.
