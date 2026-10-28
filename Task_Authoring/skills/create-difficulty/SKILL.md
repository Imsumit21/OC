---
name: create-difficulty
description: "Compute assignment-aware V3 baseline gates for a HarmonyGames task: exactly six slots, Opus 5.5 provenance, fewer than five full passes, assigned Easy/Medium/Hard average strictly below 90%/85%/70%, with corrected fair results determining the verdict and raw results preserved. Retain error, spread, failure-pattern and existing horizon checks; map each trajectory to its verifier run by content (tools/trajectory_ledger.py), verify friction and horizon, and route failures through the score-shape table (on a failure: /create-hardening MODE B, then /create-scenario --revise). Scores the pre-registered forecast against the corrected gates (advisory, UNCALIBRATED). Use /create-difficulty after the verifier. Writes Working_Files/12_Difficulty_Stats.txt and 12_difficulty_input.json."
---

# Baseline difficulty & failure patterns (12)

Resolve this file through any symlink to locate `<bundle>/skills/<name>/SKILL.md`.
The bundle's parent is the workspace. Read `<bundle>/setup/GEN_EXECUTION.md` first, then follow the playbook
`Task_Authoring/playbooks/12_Difficulty.md` in full. Write only under
`Task_Authoring/task_inputs/` (plus the forecast score's ledger append through `tools/hardness_forecast.py`,
GEN_EXECUTION §1); never write to `Evals/`, `claude/` or `HarmonyGames_*`, and never execute SQL.

## Inputs
Upstream slots in `Task_Authoring/task_inputs/`: `10_Baseline_Verifier_Results.md`, `07_Baseline_Trajectories/`, `09_Rubrics.json`, `00_Assigments.md`, `03_Error_Async_Config.txt`, `11_AF_Justification.md` (required when any rubric failed every completed run). If a required one is
missing, stop and name it. Read the normalized eight-field assignment before the universe.
Build the matrix with `python3 Task_Authoring/tools/difficulty_stats.py --build … --task-dir Task_Authoring/task_inputs`
plus 11's `--invalid` / `--judge-correction` hand-off. Map each trajectory to its verifier `Run #N` by content, never by
file order: `python3 Task_Authoring/tools/trajectory_ledger.py --task-dir Task_Authoring/task_inputs --sql <rev>=Task_Authoring/task_inputs/01_Universe_Inject.sql --sql <older rev>=Task_Authoring/task_inputs/Working_Files/run_forensics/<older rev>/01_Universe_Inject.sql …`
(one `--sql` per stored revision; the first revision: `--sole-revision "<reason>"`) binds every export to its revision on evidence (one SQL alone is INSUFFICIENT) and reports validity, friction and the counted calls (`difficulty_stats.count_tool_calls`).
Fix unfair rows and re-grade before
judging difficulty. The corrected fair view determines the V3 verdict; the platform view
remains audit evidence. Never switch difficulty mode or use `--legacy-v2` for a V3 task.
Ground every fact through `Task_Authoring/tools/hg.py search` and
apply the persona ACL yourself (search does not).

## Output
`task_inputs/Working_Files/12_difficulty_input.json` and `task_inputs/Working_Files/12_Difficulty_Stats.txt`, including the **Self-review** section (gate numbers recomputed independently; playbook; GEN_EXECUTION §6a).

## Stage gate (blocking)
Run `python3 Task_Authoring/tools/stage_gate.py difficulty Task_Authoring/task_inputs --paste`. Handoff is blocked until it prints `STAGE GATE <stage>: PASS`; `--paste` writes that output into the Self-review, and the next stage's gate refuses an upstream artifact without a current PASS block. It checks structure and freshness, evidence pointers, pasted tool outputs (re-run and compared), persona reach, universe-KB use and the self-review's counter-readings. Fix the artifact; never edit the gate's output.

## Deliver
Report the output path(s), any blocking findings, the pre-registered forecast against the observed corrected gates (scored with `hardness_forecast.py score`; advisory, UNCALIBRATED), and the next step: confirm the platform check only if every gate passes; otherwise `/create-hardening` (MODE B forensics), whose output `/create-scenario --revise` consumes, and the routing in the report.
The user handles Eval Portal submissions and screenshots.
