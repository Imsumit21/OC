---
name: create-hardening
description: "Run the forensics for a HarmonyGames revision after an Opus pre-check or baseline (MODE B; the single owner of run forensics): binds each export to its revision, reads every trajectory and write payload with tools/trajectory_ledger.py, tools/node_verdicts.py and tools/surface_grader.py, dispositions the proposed node verdicts (CONFOUNDED only by hand), corrects fairness attribution, compares corrected results with the assigned V3 mode cap and appends the ledger. A pre-check intake adds a pre-registered posterior forecast and a go / no-go call (advisory). Proposes the purge and routing; /create-scenario --revise decides, /create-injection changes the universe. MODE A moved to /create-scenario and /create-injection. Writes the hardening report and Working_Files/run_forensics/<revision>/; prompt defects are reported for the prompt stage."
---

# Hardening: design audit + baseline forensics (01a, advanced)

Resolve this file through any symlink to locate `<bundle>/skills/<name>/SKILL.md`.
The bundle's parent is the workspace. Read `<bundle>/setup/GEN_EXECUTION.md` first, then follow the playbook
`Task_Authoring/playbooks/01a_Hardening.md` in full. Write only under
`Task_Authoring/task_inputs/` (plus ledger appends through `tools/hardness_ledger.py` and `tools/hardness_forecast.py`,
GEN_EXECUTION §1); never write to `Evals/`, `claude/` or `HarmonyGames_*`, and never execute SQL.

Authorship (GEN_EXECUTION §2): the repository preserves model drafting/revision as a local exception to official V3 human authorship.

## Inputs

First run `python3 Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source`.
Use the shared `Working_Files/00_Task_Context.json` (all eight assigned fields,
registered shared data source and assigned freeze). The assigned universe date selects the universe (GEN_EXECUTION § 0a): Feb 14, 2026 → normal, Oct 1, 2025 → synth-cut. Read only that universe, apply its state rules and clock, and stop if the date is missing — there is no default. Validate relied-on record dates and earlier state before grounding. V3 changed-topic rules govern over older Evals text. The existing Long→extreme and Normal design limits remain local policy; Eval Portal is handled by the user.

Upstream slots in `Task_Authoring/task_inputs/`: `01_Scenario_Design.md`, `01_Hardness_Manifest.json`, `01_Grounding_Dossier.md`, `01_Universe_Inject.sql`; `04_Prompt.txt` if written; `Working_Files/01_Gradable_Surface.json` and `Working_Files/solver/solver.py` (each run is graded with the solver of the revision it is bound to: pass every stored revision, `Working_Files/run_forensics/*/01_Universe_Inject.sql`, with `--sql`; one SQL alone binds nothing, INSUFFICIENT, and `--sole-revision "<reason>"` is for a first revision only); for MODE B also `06_PreCheck_Trajectory/trajectory.json`, `07_Baseline_Trajectories/`, `10_Baseline_Verifier_Results.md`, `12_Difficulty_Stats.txt`. If a required one is
missing, stop and name it. Ground every fact through `Task_Authoring/tools/hg.py search` and
apply the persona ACL yourself (search does not).

## Output
`task_inputs/Working_Files/01a_Hardening_Report.md`, `task_inputs/Working_Files/run_forensics/<revision>/` (call ledgers, decoded writes, subagent briefs, node verdicts, surface grades) and the dispositioned records appended to `support/hardness_ledger/ledger.jsonl` (each keeps model, harness and source). No SQL is written here: universe changes go through `/create-scenario --revise` and `/create-injection`.

## Self-review
Before handoff, run the playbook's **Self-review** section (GEN_EXECUTION §6a). The tools propose: disposition every proposal, review every call in the `review_queue` and list the calls you did not review. Counter-read every LANDED verdict for a tool, fairness, verifier or run cause, and every LEAKED verdict for a trap that was never live. Argue for the neighbouring band. Re-verify the deciding records through `tools/hg.py`. Attribute the new release's FAIL classes: `overly_broad` is Major; a row an idle agent passes (no writes, no answer) is a Negative Criteria FAIL; prompt Contrived includes staged typos, trap hints/riddles, a hidden destination the persona knows, audit-form wording and if-chains; a false premise is universe-specific (departed person acting, business as usual after the Feb 11 shutdown, post-cut objects); Trash/attachment-only/unlinked evidence is `unobservable` (B-09, B-11, B-14, A-26/B-16, A-20). An OE edit stales the rubric review, and `prompt-ugt-v1`/format-4/ledger-1 records force a FULL re-review (A-19, C-13, C-11, C-22); keep every quoted report's `Clock:` line and cite `Evals/references/universes/<key>/universe_manifest.json` (A-28).

Read the control and channel records, not just the rule verdicts: a control member written as the over-application gives is OVER-APPLIED (else HELD) and is never a landing; control-explained `(key, field)` evidence is its own class and cannot land as a rule; a channel is FAILED/HELD/UNOBSERVED per run (a slots-only channel is judged on the surface, an unrecorded deciding model is an unknown decision and never eligible for the go rule); `reference_landed` lands nothing for any non-mechanism item (cascade/`mechanism?`/ambiguous mechanism/control/slip) and reports a contract disagreement when such an item names an ablation. A `control`/`channel` ledger record needs typed provenance (a non-negative integer `deciding_event` or `covered.members` count, a non-empty `deciding_models` list, or `features.deciding_model_unknown: true`) and never enters the priors. A pending `mechanism?` review (`features.pending_review`) is refused until `features.disposed_by` records its disposition; an unexplained landed key stays a trial on that key.

## Stage gate (blocking)
Run `python3 Task_Authoring/tools/stage_gate.py hardening Task_Authoring/task_inputs --paste`. Handoff is blocked until it prints `STAGE GATE <stage>: PASS`; `--paste` writes that output into the Self-review, and the next stage's gate refuses an upstream artifact without a current PASS block. It checks structure and freshness, evidence pointers, pasted tool outputs (re-run and compared), persona reach, universe-KB use and the self-review's counter-readings, and it re-runs the injection checks on the current revision (`revision.injection`). Fix the artifact; never edit the gate's output.

## Deliver
Report the output path(s), each export's revision binding, the predicted band and raw/clean averages, verdict counts with their review coverage, confounded findings, the proposed purge and routing, the ledger record ids, for a pre-check the posterior forecast id and the go / no-go call (UNCALIBRATED), any blocking findings, and the next step: `/create-scenario --revise` dispositions the verdicts and `/create-injection` implements any universe change, then `/injection`; the human revises the prompt for any reported prompt-side defect; re-inject and re-run on the platform.
