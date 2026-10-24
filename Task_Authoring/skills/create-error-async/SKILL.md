---
name: create-error-async
description: "Decide whether a HarmonyGames task gets forced tool errors or async search waits (default: Friction: none, since configured friction is realism only and never a difficulty or horizon lever), and if configured make it safe: exact picker values, a consistent mode/rate pair, the alternate path proven, async twins and verifier reads accounted for, and a post-baseline proof. Use /create-error-async after /create-injection. Writes Task_Authoring/task_inputs/03_Error_Async_Config.txt. Never writes to Evals/, claude/ or HarmonyGames_*."
---

# Error injection & async wait config (03, optional)

Resolve this file through any symlink to locate `<bundle>/skills/<name>/SKILL.md`.
The bundle's parent is the workspace. Read `<bundle>/setup/GEN_EXECUTION.md` first, then follow the playbook
`Task_Authoring/playbooks/03_Error_Async_Config.md` in full. Its gates are hard gates. Write only under
`Task_Authoring/task_inputs/`. Never write to `Evals/`, `claude/` or `HarmonyGames_*`, and
never execute SQL.

## Inputs

First run `python3 Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source`.
Use the shared `Working_Files/00_Task_Context.json` (all eight assigned fields,
registered shared data source and assigned freeze). Both dates use the same local
data; validate relied-on record dates and earlier state before grounding. V3
changed-topic rules govern over older Evals text. The existing Long→extreme and
Normal design limits remain local policy; Eval Portal is handled by the user.

Required in `Task_Authoring/task_inputs/`: `00_Assigments.md`, `01_Grounding_Dossier.md` and
`01_Universe_Inject.sql`. If one is missing, stop and name it.

Also read, when present: `01_Hardness_Manifest.json`, `04_Prompt_Writing_Brief.md`, `04_Prompt.txt` and
`02_Reference_Files_Manifest.md`. They show whether discovery is still required and whether
friction is announced anywhere.

Take exact names from `Evals/references/tools/catalog.json`. Prove alternate paths through
`Task_Authoring/tools/hg.py search`, and apply the persona ACL yourself.

## Output
`task_inputs/03_Error_Async_Config.txt` in the template format, with a **Self-review** section
(playbook, GEN_EXECUTION §6a). With no friction, write `Friction: none` and leave every field empty.

## Stage gate (blocking)
Run `python3 Task_Authoring/tools/stage_gate.py error-async Task_Authoring/task_inputs --paste`. Handoff is blocked until it prints `STAGE GATE <stage>: PASS`; `--paste` writes that output into the Self-review, and the next stage's gate refuses an upstream artifact without a current PASS block. It checks structure and freshness, evidence pointers, pasted tool outputs (re-run and compared), persona reach, universe-KB use and the self-review's counter-readings. Fix the artifact; never edit the gate's output.

## Deliver
Report:
- the configured functions with mode/rate/wait, or `Friction: none` with its reason;
- the alternate path and async twin for each errored search;
- the constraints for the brief and the reference files;
- the post-baseline proof checks;
- any blocking finding.

Next: `/create-reference-files` if the scenario needs an attachment, otherwise `/create-prompt-writing`.
Supply the config to `/prompt` only when friction is configured.
