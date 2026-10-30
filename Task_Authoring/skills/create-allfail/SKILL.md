---
name: create-allfail
description: "Find every rubric that failed all completed baseline rollouts on a HarmonyGames task, decide valid vs invalid from the trajectories, draft 1–2 line justifications for valid ones and report invalid ones for the human to fix. Use /create-allfail once the baseline verifier results exist. Writes Task_Authoring/task_inputs/11_AF_Justification.md."
---

# All-fail rubric analysis (11)

Resolve this file through any symlink to locate `<bundle>/skills/<name>/SKILL.md`.
The bundle's parent is the workspace. Read `<bundle>/setup/GEN_EXECUTION.md` first, then follow the playbook
`Task_Authoring/playbooks/11_AllFail_Analysis.md` in full. Write only under
`Task_Authoring/task_inputs/`; never write to `Evals/`, `claude/` or `HarmonyGames_*`,
and never execute SQL.

Authorship (GEN_EXECUTION §2): the repository preserves model drafting/revision as a local exception to official V3 human authorship.

## Inputs

First run `python3 Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source`.
Use the shared `Working_Files/00_Task_Context.json` (all eight assigned fields,
registered shared data source and assigned freeze). Both dates use the same local
data; validate relied-on record dates and earlier state before grounding. V3
changed-topic rules govern over older Evals text. The existing Long→extreme and
Normal design limits remain local policy; Eval Portal is handled by the user.

Upstream slots in `Task_Authoring/task_inputs/`: `10_Baseline_Verifier_Results.md`, `07_Baseline_Trajectories/`, `09_Rubrics.json`, `04_Prompt.txt`, `00_Assigments.md`, `03_Error_Async_Config.txt`, `01_Universe_Inject.sql` (or "no injection"); `08_OE_Writing_Ledger.md` and `08_Oracle_Events.md` are leads only. If a required one is
missing, stop and name it. Empty or template verifier output means the verifier has not run — stop; it is not a set of errored rollouts.
Parse and bind with `python3 Task_Authoring/tools/difficulty_stats.py --build …` (playbook Step 1); the build stopping is a blocking finding. Ground every fact through `Task_Authoring/tools/hg.py search` and
apply the persona ACL yourself (search does not).

## Output
`task_inputs/11_AF_Justification.md` (or `NONE`): one verdict per all-fail (VALID · INVALID — rubric · INVALID — environment · JUDGE ERROR · UNRESOLVED; invalid only when the defect causes the failure), justifications for VALID rows, the tally, the `--invalid` / `--judge-correction` hand-off line, and the **Self-review** section (playbook; GEN_EXECUTION §6a).

A forecast's `P(fails all six)` is workload, not an all-fail verdict or a block: decide each rubric on the trajectory evidence and the rubric defect.

## Stage gate (blocking)
Run `python3 Task_Authoring/tools/stage_gate.py allfail Task_Authoring/task_inputs --paste`. Handoff is blocked until it prints `STAGE GATE <stage>: PASS`; `--paste` writes that output into the Self-review, and the next stage's gate refuses an upstream artifact without a current PASS block. It checks structure and freshness, evidence pointers, pasted tool outputs (re-run and compared), persona reach, universe-KB use and the self-review's counter-readings. Fix the artifact; never edit the gate's output.

## Deliver
Report the output path(s), any blocking findings, and the next step: enter justifications on the Rate All-Fail Rubrics screen; fix any invalid criterion (Claude, Codex or the human) and re-run the verifier; then `/create-difficulty`.
