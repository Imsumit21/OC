---
name: create-reference-files
description: "Author reference files for a HarmonyGames task when the scenario needs an attachment. Build native export/download shapes in a flat folder, grounded in facts valid at the assigned freeze, readable, not pre-solving, with fair outcomes and incorporation recorded. Use after /create-error-async. Writes Task_Authoring/task_inputs/02_Reference_Files/ and its manifest; never writes to Evals/, claude/ or HarmonyGames_*."
---

# Reference files (02, optional)

Resolve this file through any symlink to locate `<bundle>/skills/<name>/SKILL.md`.
The bundle's parent is the workspace. Read `<bundle>/setup/GEN_EXECUTION.md` first, then follow the playbook
`Task_Authoring/playbooks/02_Reference_Files.md` in full. Its gates are hard gates. Write only under
`Task_Authoring/task_inputs/`. Never write to `Evals/`, `claude/` or `HarmonyGames_*`, and
never execute SQL.

## Inputs

First run `python3 Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source`.
Use the shared `Working_Files/00_Task_Context.json` (all eight assigned fields,
registered shared data source and assigned freeze). The assigned universe date selects the universe (GEN_EXECUTION § 0a): Feb 14, 2026 → normal, Oct 1, 2025 → synth-cut. Read only that universe, apply its state rules and clock, and stop if the date is missing — there is no default. Validate relied-on record dates and earlier state before grounding. V3 changed-topic rules govern over older Evals text. The existing Long→extreme and Normal design limits remain local policy; Eval Portal is handled by the user.

Every file fact must be true in the selected universe and dated at or before its seed bound; a Drive file the agent must read needs body text or real bytes at `content_path` `<owner_email>/<path>`, and no deciding fact may live only in a Gmail or Slack attachment (A-26, A-08/B-07, B-19).

Required in `Task_Authoring/task_inputs/`: `00_Assigments.md`, `01_Grounding_Dossier.md` and
`01_Universe_Inject.sql`. If one is missing, stop and name it.

Also read, when present: `01_Hardness_Manifest.json` and `03_Error_Async_Config.txt` (the files must
not name async targets).

Use `references/Native_Artifact_Anatomy.md`, §M plus the source service's section. Ground every fact
through `Task_Authoring/tools/hg.py search`, and apply the persona ACL yourself.

## Output
- `task_inputs/02_Reference_Files/`: flat, task files only, the template README deleted. Leave it empty when there are none.
- `task_inputs/Working_Files/02_Reference_Files_Manifest.md`: outside the folder, including the **Self-review** (playbook, GEN_EXECUTION §6a).

## Stage gate (blocking)
Run `python3 Task_Authoring/tools/stage_gate.py reference-files Task_Authoring/task_inputs --paste`. Handoff is blocked until it prints `STAGE GATE <stage>: PASS`; `--paste` writes that output into the Self-review, and the next stage's gate refuses an upstream artifact without a current PASS block. It checks structure and freshness, evidence pointers, pasted tool outputs (re-run and compared), persona reach, universe-KB use and the self-review's counter-readings. Fix the artifact; never edit the gate's output.

## Deliver
Report:
- the file list (format, role, incorporated or not);
- the deliberate inaccuracies and what overturns each;
- the constraints for the brief;
- any blocking finding.

Upload the same flat folder on both screens, or skip both when there are none. After the pre-check,
paste the run-time `ls /app/artifact` into the manifest. Supply the files with `/prompt`,
`/hardness`, `/oe` and `/rubric`.

Next: `/create-prompt-writing`.
