---
name: create-prompt-writing
description: "Prepare, draft and check a HarmonyGames prompt. Default: a structured brief (assignment fit, pinned final state, facts to discover, must-not-appear list, levers). With 'draft': write 04_Prompt.txt from the brief in the persona's voice. With 'check': a lint of 04_Prompt.txt (model- or human-written) against the brief and the universe, with suggested wording. Writes Task_Authoring/task_inputs/Working_Files/04_Prompt_Writing_Brief.md, Task_Authoring/task_inputs/04_Prompt.txt or 04_Prompt_Check.md."
---

# Prompt writing: brief (prep) and prompt check (04)

Resolve this file through any symlink to locate `<bundle>/skills/<name>/SKILL.md`.
The bundle's parent is the workspace. Read `<bundle>/setup/GEN_EXECUTION.md` first, then follow the playbook
`Task_Authoring/playbooks/04_Prompt_Writing.md` in full. Write only under
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

Upstream slots in `Task_Authoring/task_inputs/`: `00_Assigments.md`, `01_Grounding_Dossier.md`, `01_Universe_Inject.sql`, `03_Error_Async_Config.txt`, `02_Reference_Files_Manifest.md`; check mode also `04_Prompt.txt` (the human's prompt, exactly as it will be submitted). If a required one is
missing, stop and name it. Ground every fact through `Task_Authoring/tools/hg.py search` and
apply the persona ACL yourself (search does not).
Persona view: prove each discovery-map fact is findable with `tools/persona_view.py search <persona> <service> "<natural query>"` (brief §5a) and visible with `persona_view.py can-see`; pin name traps with `tools/entity.py collisions` / `resolve` (brief §10).
Final outcomes: brief §4b records every fair reading and accepted result; 08 and 09 reuse it. Supply outcome reviews for prompt-writing and prompt-check plus the assigned-role review for prompt-check in `Working_Files/00_V3_Authoring_Evidence.json` (Guide schema). Write a clean ordinary request with no riddle, trap hint or answer-key clause. Tier targets remain Long→extreme / Normal→normal, certified separately from the assigned mode cap.

## Output
brief mode: `task_inputs/Working_Files/04_Prompt_Writing_Brief.md` · draft mode: `task_inputs/04_Prompt.txt` · check mode: `task_inputs/Working_Files/04_Prompt_Check.md`.

Check mode runs C1–C24 with V3 changed-topic overrides: role implausibility fails; business-function/competency/task-skill mismatches alone do not. Accept every fair reading and clean spelling; report evidence gaps explicitly. Both modes end with the playbook's self-review and sidecar artifact bindings.

## Stage gate (blocking)
Run `python3 Task_Authoring/tools/stage_gate.py prompt-writing Task_Authoring/task_inputs --paste` (prep) or `… prompt-check …` (check mode). Handoff is blocked until it prints `STAGE GATE <stage>: PASS`; `--paste` writes that output into the Self-review, and the next stage's gate refuses an upstream artifact without a current PASS block. It checks structure and freshness, evidence pointers, the §4b canonical outcome (brief), the tier's hardness certificate (`tier.hardness`, check), pasted tool outputs (re-run and compared), persona reach, universe-KB use, and the self-review's counter-readings. Fix the artifact; never edit the gate's output.

## Deliver
Report the output path(s), any blocking findings, and the next step: brief → `/create-prompt-writing draft` (or the human writes `04_Prompt.txt`) · check → fix and re-check, then `/injection` + `/prompt` as a pair. A `/prompt` FAIL is fatal.
