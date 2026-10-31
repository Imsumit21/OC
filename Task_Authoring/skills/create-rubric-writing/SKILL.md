---
name: create-rubric-writing
description: "Prepare, draft and check rubric criteria. Default: a coverage matrix from the prompt and verified Oracle Events (what must be graded, values a self-contained criterion must name, Outcome vs Process test, weight band by kind of work (1/3/5), format-5 per-row valid_case / do_nothing_case / verbatim OE step / deciding-source reachability, one whole-set final-reply test, and title/distractor/ambiguity/predicted-all-fail flags). With 'draft': write 09_Rubrics.json from the plan. With 'check': a lint of 09_Rubrics.json (model- or human-written) against the plan, the eval lint (hg.py rubric-lint) and every /rubric check, using /rubric's issue types, severities (hg-strict-overrides-v1; overly_broad is Major) and current dimension bands. Both modes end with an adversarial self-review. Writes Task_Authoring/task_inputs/Working_Files/09_Rubric_Writing_Plan.md or 09_Rubric_Check.md."
---

# Rubric writing: coverage plan (prep) and rubric check (09)

Resolve this file through any symlink to locate `<bundle>/skills/<name>/SKILL.md`.
The bundle's parent is the workspace. Read `<bundle>/setup/GEN_EXECUTION.md` first, then follow the playbook
`Task_Authoring/playbooks/09_Rubric_Writing.md` in full. Write only under
`Task_Authoring/task_inputs/`; never write to `Evals/`, `claude/` or `HarmonyGames_*`,
and never execute SQL.

Authorship (GEN_EXECUTION §2): the repository preserves model drafting/revision as a local exception to official V3 human authorship.

## Inputs

First run `python3 Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source`.
Use the shared `Working_Files/00_Task_Context.json` (all eight assigned fields,
registered shared data source and assigned freeze). The assigned universe date selects the universe (GEN_EXECUTION § 0a): Feb 14, 2026 → normal, Oct 1, 2025 → synth-cut. Read only that universe, apply its state rules and clock, and stop if the date is missing — there is no default. Validate relied-on record dates and earlier state before grounding. V3
changed-topic rules govern over older Evals text. The existing Long→extreme and
Normal design limits remain local policy; Eval Portal is handled by the user.

Upstream slots in `Task_Authoring/task_inputs/`: `04_Prompt.txt`, `08_Oracle_Events.md` (required; without an `/oe` PASS the plan is PROVISIONAL per the playbook), `08_OE_Writing_Ledger.md`; check mode also `09_Rubrics.json` (the builder export). If a required one is
missing, stop and name it. Ground every fact through `Task_Authoring/tools/hg.py search` and
apply the persona ACL yourself (search does not).
Re-read every expected value through `tools/hg.py` and record its actual source field, reachable discovery path and `temporal_evidence` in `Working_Files/00_V3_Authoring_Evidence.json` (Guide schema). The assigned universe date selects the universe (GEN_EXECUTION § 0a): Feb 14, 2026 → normal, Oct 1, 2025 → synth-cut. Read only that universe, apply its state rules and clock, and stop if the date is missing — there is no default. Establish mutable earlier state with dated history or independent earlier evidence. Each criterion needs an exact prompt span, stable fact ID, every accepted fair alternative, a `valid_case` it accepts, a `do_nothing_case` it rejects, its verbatim OE step ids and its deciding source's reachability; the same fact in three or more rows fails across deliverables. Human dates use Pacific plus UTC when days differ; accept either unless the prompt requests one. Keep the existing visibility, shortcut and diversity checks; sampled populations use volume/direct-exception rows, never bundled exact-set rows.

## Rules that most often decide the verdict
Keep unchanged title-only, atomicity, affirmative-title, weight 1/3/5, coverage and binary-validity checks. V3 controls fair alternatives, prompt trace, source correctness/reachability, date flexibility and global fact duplication. Fix unfair rows and re-grade before comparing with the assigned mode cap; do not tighten or add rows to depress the average.
Check mode runs `python3 Task_Authoring/tools/hg.py rubric-lint Task_Authoring/task_inputs/09_Rubrics.json` first and resolves every `disguised_negative`, `format_lock`, `anon_token` and `evidence_no_record` hit. Release `task-quality-v1`: scoring record format 5, rubric ledger format 2 (an old ledger forces a FULL review).

§G must cover every slot of `Working_Files/01_Gradable_Surface.json`: a covering row (P-n; C-n in check mode) or a disposition with its reason. A slot with neither, a bare label, a `gap` or a stale line blocks `surface.coverage` (gate 17). A criterion must not grade a control-explained field as a landing; a forecast's P(fails all six) is workload, never a block.

## Output
prep mode: `task_inputs/Working_Files/09_Rubric_Writing_Plan.md` · draft mode: `task_inputs/09_Rubrics.json` · check mode: `task_inputs/Working_Files/09_Rubric_Check.md`.

## Stage gate (blocking)
Run `python3 Task_Authoring/tools/stage_gate.py rubric-writing Task_Authoring/task_inputs --paste` (prep) or `… rubric-check …` (check mode). Handoff is blocked until it prints `STAGE GATE <stage>: PASS`; `--paste` writes that output into the Self-review, and the next stage's gate refuses an upstream artifact without a current PASS block. It checks structure and freshness, evidence pointers, the binary validity gate (check), predicted all-fail = 0, failure diversity, population volume/direct-exception rows, V3 evidence and the shortcut probe (prep), pasted tool outputs (re-run and compared), persona reach, universe-KB use, and the self-review's counter-readings. Fix the artifact; never edit the gate's output.

## Deliver
Report the output path(s), any blocking findings, and the next step: prep → `/create-rubric-writing draft` (or the human writes the criteria), enter them in the Rubric Criteria Builder and export `09_Rubrics.json` · check → fix, then `/rubric`. Every output carries a **Self-review** section (playbook § Self-review; GEN_EXECUTION §6a).
