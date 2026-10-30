---
name: create-humantime
description: "Build the human-time worksheet for a HarmonyGames task: manual sub-tasks with persona-view measured volumes, anchored rates, dead ends, workarounds and writes, minutes that add up to the hours figure, and a tier cross-check that is reported, never tuned. Use /create-humantime right after the prompt is written (refresh after Oracle Events and after the baseline). Writes Task_Authoring/task_inputs/Working_Files/05_Human_Time_Worksheet.md."
---

# Human time worksheet (06)

Resolve this file through any symlink to locate `<bundle>/skills/<name>/SKILL.md`.
The bundle's parent is the workspace. Read `<bundle>/setup/GEN_EXECUTION.md` first, then follow the playbook
`Task_Authoring/playbooks/05_Human_Time_Estimate.md` in full. Its gates are hard gates. Write only under
`Task_Authoring/task_inputs/`. Never write to `Evals/`, `claude/` or `HarmonyGames_*`, and
never execute SQL.

## Inputs

First run `python3 Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source`.
Use the shared `Working_Files/00_Task_Context.json` (all eight assigned fields,
registered shared data source and assigned freeze). Both dates use the same local
data; validate relied-on record dates and earlier state before grounding. V3
changed-topic rules govern over older Evals text. The existing Long→extreme and
Normal design limits remain local policy; Eval Portal is handled by the user.

Required in `Task_Authoring/task_inputs/`: `04_Prompt.txt` and `00_Assigments.md` (tier and persona).
If either is missing, stop and name it.

Also read, when present: `01_Grounding_Dossier.md`, `01_Hardness_Manifest.json`, `04_Prompt_Writing_Brief.md`,
`03_Error_Async_Config.txt` and `02_Reference_Files_Manifest.md`.

On refresh, add `08_Oracle_Events.md`, `08_OE_Writing_Ledger.md`, `07_Baseline_Trajectories/` and
`12_Difficulty_Stats.txt`.

Measure every volume through `Task_Authoring/tools/hg.py search`, and apply the persona ACL
yourself (search does not).

## Output
`task_inputs/Working_Files/05_Human_Time_Worksheet.md`: hours, the sub-task table (kind, volume, rate, minutes),
the tier check, the character count and the **Self-review** (playbook section, GEN_EXECUTION §6a).
It contains no paragraph written to be retyped. Channel/control evidence is not a deliverable: it must not add sub-tasks, volumes or minutes.

## Stage gate (blocking)
Run `python3 Task_Authoring/tools/stage_gate.py humantime Task_Authoring/task_inputs --paste`. Handoff is blocked until it prints `STAGE GATE <stage>: PASS`; `--paste` writes that output into the Self-review, and the next stage's gate refuses an upstream artifact without a current PASS block. It checks structure and freshness, evidence pointers, pasted tool outputs (re-run and compared), persona reach, universe-KB use and the self-review's counter-readings. Fix the artifact; never edit the gate's output.

## Deliver
Report:
- the output path;
- the hours;
- any tier trigger, with the re-measurement;
- any blocking finding.

Next step: the human types the estimate on Screen 25. The field is required and blocks pasting and
copying. Then run the Opus 5.5 pre-check on the platform, then `/hardness`.
