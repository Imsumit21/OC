---
name: create-prompt-writing
description: "Prepare, draft and check a HarmonyGames prompt. Default: a structured brief (assignment fit, pinned final state, facts to discover, must-not-appear list, levers). With 'draft': write 04_Prompt.txt from the brief in the persona's voice. With 'check': a lint of 04_Prompt.txt (model- or human-written) against the brief and the universe, with suggested wording. Writes <task_dir>/Working_Files/04_Prompt_Writing_Brief.md, <task_dir>/04_Prompt.txt or 04_Prompt_Check.md."
---

# Prompt writing: brief (prep) and prompt check (04)

**Task folder (required).** `<task_dir>` in this skill and its playbook is the task folder given as this command's
argument, for example `/create-prompt-writing Task_Authoring/task_inputsRobert`. If no folder is given and
`TASK_AUTHORING_TASK_DIR` is unset, stop and ask which folder; never guess and never fall back to a default. Pass
the same folder as `--task-dir` to every tool. A new task has its own named folder
(`Task_Authoring/task_inputs<Label>`), not a bare `Task_Authoring/task_inputs`, so two tasks never share one.

Resolve this file through any symlink to locate `<bundle>/skills/<name>/SKILL.md`.
The bundle's parent is the workspace. Read `<bundle>/setup/GEN_EXECUTION.md` first, then follow the playbook
`Task_Authoring/playbooks/04_Prompt_Writing.md` in full. Write only under
`<task_dir>/`; never write to `Evals/`, `claude/` or `HarmonyGames_*`,
and never execute SQL.

Authorship (GEN_EXECUTION §2): the repository preserves model drafting/revision as a local exception to official V3 human authorship.

## Inputs

First run `python3 Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source`.
Use the shared `Working_Files/00_Task_Context.json` (all eight assigned fields,
registered shared data source and assigned freeze). The assigned universe date selects the universe (GEN_EXECUTION § 0a): Feb 14, 2026 → normal, Oct 1, 2025 → synth-cut. Read only that universe, apply its state rules and clock, and stop if the date is missing — there is no default. Validate relied-on record dates and earlier state at the seed bound (`freeze_utc`) before grounding; persona dates are Pacific, "today" comes from `universe.persona_today`, and each report carries `universe.clock_line` as its `Clock:` line. V3
changed-topic rules govern over older Evals text. The existing Long→extreme and
Normal design limits remain local policy; Eval Portal is handled by the user.

Upstream slots in `<task_dir>/`: `00_Assigments.md`, `01_Grounding_Dossier.md`, `01_Universe_Inject.sql`, `03_Error_Async_Config.txt`, `02_Reference_Files_Manifest.md`; check mode also `04_Prompt.txt` (the human's prompt, exactly as it will be submitted). If a required one is
missing, stop and name it. Ground every fact through `Task_Authoring/tools/hg.py search` and
apply the persona ACL yourself (search does not).
Persona view: prove each discovery-map fact is findable with `tools/persona_view.py search <persona> <service> "<natural query>"` (brief §5a) and visible with `persona_view.py can-see`; pin name traps with `tools/entity.py collisions` / `resolve` (brief §10).
Final outcomes: brief §4b records every fair reading and accepted result; 08 and 09 reuse it. Supply outcome reviews for prompt-writing and prompt-check plus the assigned-role review for prompt-check in `Working_Files/00_V3_Authoring_Evidence.json` (Guide schema). Write a clean ordinary request with no riddle, trap hint, answer-key clause, staged error, audit-form wording or if-chain, and name a destination the persona would know. Every premise holds at the clock: no business as usual after the Feb 11, 2026 shutdown on a Feb 14 task, no departed person acting (Victor since April 2025), nothing first appearing after 2025-09-30 23:59:59 PT on Oct 1. Voice is judged against the role only. At most one reported figure may stay unsettled, and only under `BOTH_FAIR_FIGURE`'s five conditions (the check report then prints "Rubric must accept: X or Y"). Tier targets remain Long→extreme / Normal→normal, certified separately from the assigned mode cap.

The deliverable must be in a shape the grader decodes — tracker text with group lists/tables, a table/CSV-shaped register, a `json_text` write (tickets/summary/mail), or a Slack/Trello post delivered through `json_text`/`calls` — never prose only. Before the pre-check, run `python3 Task_Authoring/tools/gradable_surface.py gradeable-report --task-dir <task_dir>` and spot-decode one realistic deliverable per selector kind; control/channel declarations are universe facts, not prompt hints, so do not leak them.

## Output
brief mode: `<task_dir>/Working_Files/04_Prompt_Writing_Brief.md` · draft mode: `<task_dir>/04_Prompt.txt` · check mode: `<task_dir>/Working_Files/04_Prompt_Check.md`.

Check mode runs C1–C24 with V3 changed-topic overrides: role implausibility fails; a clear competency mismatch or an assigned task skill that is not a real part of the work also fails (C4; Eval 1 hard FAIL), and a business-function mismatch blocks a 5. Accept every fair reading and clean spelling, but an unresolved material fork fails `/prompt`: settle it in data through `/create-injection` and record it in the fork sweep (`tools/coherence_sweep.py`), never with "accept either" or a prompt sentence aimed at the fork; report evidence gaps explicitly. Findings bind release `task-quality-v1`; a `prompt-ugt-v1` record is historical and not reusable. Self-test the text against the 15 `calibration_cases` in `Evals/references/rules/prompt_qc_cases.json` (`staged_errors`, `trap_hint_or_riddle`, `hidden_destination`, `audit_form`, `if_chain`, `false_state_premise`, `ugt_both_fair_figure`) and `prompt_qc_examples.md`. Both modes end with the playbook's self-review and sidecar artifact bindings.

## First-pass checks (brief and check mode)
- **Fork sweep** (`structure.accepted_outcomes`, `sweep.forks`): the gates read `Working_Files/01d_Coherence_Sweep.json`. After the prompt is written, re-run the sweep on the prompt and the SQL together (`coherence_sweep.py candidates`, a cold reviewer from `coherence_sweep.py brief`, then `python3 -B Task_Authoring/tools/coherence_sweep.py check --task-dir <task_dir>`). An open material fork goes back to `/create-injection`.
- **Assignment fit** (`prompt.assignment_fit`): C4 must be clean in `04_Prompt_Check.md`; a clear competency or task-skill mismatch is a `/prompt` hard FAIL.
- These are first-pass checks: each prints WARN while its mode in `references/first_pass_policy.json` is `warn` and blocks once the owner sets it to `block` (`python3 -B Task_Authoring/tools/first_pass_controls.py modes`). Fix what they report either way.

## Stage gate (blocking)
Run `python3 Task_Authoring/tools/stage_gate.py prompt-writing <task_dir> --paste` (prep) or `… prompt-check …` (check mode). Handoff is blocked until it prints `STAGE GATE <stage>: PASS`; `--paste` writes that output into the Self-review, and the next stage's gate refuses an upstream artifact without a current PASS block. It checks structure and freshness, evidence pointers, the §4b canonical outcome (brief), the tier's hardness certificate (`tier.hardness`, check), pasted tool outputs (re-run and compared), persona reach, universe-KB use, and the self-review's counter-readings. Fix the artifact; never edit the gate's output.

## Deliver
Report the output path(s), any blocking findings, and the next step: brief → `/create-prompt-writing draft` (or the human writes `04_Prompt.txt`) · check → fix and re-check, then `/injection` + `/prompt` as a pair. A `/prompt` FAIL is fatal. `/prompt` and `/injection` ask the task date first: answer with the assignment's universe date, never inferred.

## After a platform report (`/prompt`)
Take the report in first: `python3 Task_Authoring/tools/report_intake.py intake <report.md> --task-dir <task_dir>` (it refuses a report that belongs to another task, files it, and flags a new platform release or rule). Then follow the repair protocol in GEN_EXECUTION § 8: paste the report's Fix List text unchanged, never rewrite a row the reviewer passed, re-check only the rows you touched, and sweep every sibling of a defect in the same round. A fork or a contradiction between records is fixed in the universe through `/create-injection`, not with a prompt sentence.
