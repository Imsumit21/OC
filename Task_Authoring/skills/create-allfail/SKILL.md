---
name: create-allfail
description: "Find every rubric that failed all completed baseline rollouts on a HarmonyGames task, decide valid vs invalid from the trajectories, and write both the evidence workbook and the screen-ready justification file the platform saves as its all-fail input. Use /create-allfail once the baseline verifier results exist. Writes <task_dir>/11_AF_Justification.md and 11_Baseline_AllFail_Justifications.md."
---

# All-fail rubric analysis (11)

**Task folder (required).** `<task_dir>` in this skill and its playbook is the task folder given as this command's
argument, for example `/create-allfail Task_Authoring/task_inputsRobert`. If no folder is given and
`TASK_AUTHORING_TASK_DIR` is unset, stop and ask which folder; never guess and never fall back to a default. Pass
the same folder as `--task-dir` to every tool. A new task has its own named folder
(`Task_Authoring/task_inputs<Label>`), not a bare `Task_Authoring/task_inputs`, so two tasks never share one.

Resolve this file through any symlink to locate `<bundle>/skills/<name>/SKILL.md`.
The bundle's parent is the workspace. Read `<bundle>/setup/GEN_EXECUTION.md` first, then follow the playbook
`Task_Authoring/playbooks/11_AllFail_Analysis.md` in full. Write only under
`<task_dir>/`; never write to `Evals/`, `claude/` or `HarmonyGames_*`,
and never execute SQL.

Authorship (GEN_EXECUTION §2): the repository preserves model drafting/revision as a local exception to official V3 human authorship.

## Inputs

First run `python3 Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source`.
Use the shared `Working_Files/00_Task_Context.json` (all eight assigned fields,
registered shared data source and assigned freeze). The assigned universe date selects the universe (GEN_EXECUTION § 0a): Feb 14, 2026 → normal, Oct 1, 2025 → synth-cut. Read only that universe, apply its state rules and clock, and stop if the date is missing — there is no default. Validate relied-on record dates and earlier state before grounding. V3
changed-topic rules govern over older Evals text. The existing Long→extreme and
Normal design limits remain local policy; Eval Portal is handled by the user.

Upstream slots in `<task_dir>/`: `10_Baseline_Verifier_Results.md`, `07_Baseline_Trajectories/`, `09_Rubrics.json`, `04_Prompt.txt`, `00_Assigments.md`, `03_Error_Async_Config.txt`, `01_Universe_Inject.sql` (or "no injection"); `08_OE_Writing_Ledger.md` and `08_Oracle_Events.md` are leads only. If a required one is
missing, stop and name it. Empty or template verifier output means the verifier has not run — stop; it is not a set of errored rollouts.
Parse and bind with `python3 Task_Authoring/tools/difficulty_stats.py --build …` (playbook Step 1); the build stopping is a blocking finding. Ground every fact through `Task_Authoring/tools/hg.py search` and
apply the persona ACL yourself (search does not).

## Output

Two files from one analysis.

1. `<task_dir>/11_AF_Justification.md` (or `NONE`): one verdict per all-fail (VALID · INVALID — rubric · INVALID — environment · JUDGE ERROR · UNRESOLVED; invalid only when the defect causes the failure — including `unobservable` deciding evidence, a rejected fair alternative and a row an idle Agent passes), justifications for VALID rows, the tally, the `--invalid` / `--judge-correction` hand-off line, and the **Self-review** section (playbook; GEN_EXECUTION §6a). Keep the baseline verifier's `Clock:` line wherever its results are quoted.

2. `<task_dir>/11_Baseline_AllFail_Justifications.md`: the screen-ready file and the artifact the platform saves under its `all-fail` input key (the store names it `11_Baseline_AllFail_Justifications.txt`). Header line `# Baseline All-Fail Justifications`, one intro sentence giving the completed count, the all-fail count and how many are valid, then one `##` section per VALID all-fail whose heading is the criterion title copied verbatim from `09_Rubrics.json`, and exactly one paragraph per section: 200 to 1,400 characters, first sentence at most 220 characters and naming the expected figure, no em or en dash, no local file name. A row that is invalid, a judge error or unresolved gets no section; a `Not justified:` line names it instead. When nothing failed every run, the file holds the header and a sentence saying so. The paragraph is the same text as the workbook's `Justification (VALID only)` line, so the two files cannot drift.

A forecast's `P(fails all six)` is workload, not an all-fail verdict or a block: decide each rubric on the trajectory evidence and the rubric defect.

## Stage gate (blocking)
Run `python3 Task_Authoring/tools/stage_gate.py allfail <task_dir> --paste`. Handoff is blocked until it prints `STAGE GATE <stage>: PASS`; `--paste` writes that output into the Self-review, and the next stage's gate refuses an upstream artifact without a current PASS block. It checks structure and freshness, evidence pointers, pasted tool outputs (re-run and compared), persona reach, universe-KB use, the self-review's counter-readings, and the `baseline.*` checks on the screen file (header, one section per VALID row with verbatim titles, one 200 to 1,400 character paragraph each, a short first sentence that names a figure, figures that appear in that row's evidence, no em or en dash, no local file name, invalid rows named as not justified). Fix the artifact; never edit the gate's output.

## Deliver
Report both paths, the paragraph for each all-fail rubric (this is the text for the Rate All-Fail Rubrics screen, and the file is what the platform saves under its `all-fail` key), any blocking findings, and the next step: enter justifications on the Rate All-Fail Rubrics screen; fix any invalid criterion (Claude, Codex or the human) and re-run the verifier; then `/create-difficulty`.
