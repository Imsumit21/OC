---
name: create-hardening
description: "Harden a HarmonyGames universe after a shortcut audit or Opus 5.5 run. MODE A reviews design and SQL; MODE B reads trajectories and write payloads, corrects fairness attribution, compares corrected results with the assigned V3 mode cap and routes universe fixes. Preserves existing extreme/normal design targets. Writes the hardening report, revised SQL/dossier/manifest; prompt defects are reported for the prompt stage."
---

# Hardening: design audit + baseline forensics (01a, advanced)

Resolve this file through any symlink to locate `<bundle>/skills/<name>/SKILL.md`.
The bundle's parent is the workspace. Read `<bundle>/setup/GEN_EXECUTION.md` first, then follow the playbook
`Task_Authoring/playbooks/01a_Hardening.md` in full. Write only under
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

Upstream slots in `Task_Authoring/task_inputs/`: `01_Scenario_Design.md`, `01_Hardness_Manifest.json`, `01_Grounding_Dossier.md`, `01_Universe_Inject.sql`; `04_Prompt.txt` if written; for MODE B also `06_PreCheck_Trajectory/trajectory.json`, `07_Baseline_Trajectories/`, `10_Baseline_Verifier_Results.md`, `12_Difficulty_Stats.txt`. If a required one is
missing, stop and name it. Ground every fact through `Task_Authoring/tools/hg.py search` and
apply the persona ACL yourself (search does not).

## Output
`task_inputs/Working_Files/01a_Hardening_Report.md` (+ a hardened `01_Universe_Inject.sql`).

## Self-review
Before handoff, run the playbook's **Self-review** section (GEN_EXECUTION §6a). Counter-read every LANDED verdict for a tool, fairness, verifier or run cause, and every LEAKED verdict for a trap that was never live. Argue for the neighbouring band. Re-verify the deciding records through `tools/hg.py`.

## Stage gate (blocking)
Run `python3 Task_Authoring/tools/stage_gate.py hardening Task_Authoring/task_inputs --paste`. Handoff is blocked until it prints `STAGE GATE <stage>: PASS`; `--paste` writes that output into the Self-review, and the next stage's gate refuses an upstream artifact without a current PASS block. It checks structure and freshness, evidence pointers, pasted tool outputs (re-run and compared), persona reach, universe-KB use and the self-review's counter-readings. Fix the artifact; never edit the gate's output.

## Deliver
Report the output path(s), the predicted band and raw/clean averages, confounded findings, any blocking findings, and the next step: `/injection` on the hardened SQL; the human revises the prompt for any reported prompt-side defect; re-inject and re-run on the platform.
