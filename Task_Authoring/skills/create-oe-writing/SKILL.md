---
name: create-oe-writing
description: "Prepare, draft and check Oracle Events. Default: a verified fact ledger (value, service, locator, expected data, persona visibility, dependencies, write capability, friction recovery facts). With 'draft': write 08_Oracle_Events.md from the ledger. With 'check': a lint of 08_Oracle_Events.md (model- or human-written) that mirrors /oe (completeness, accuracy, format, path feasibility) and predicts its component scores. Use /create-oe-writing while the baseline runs, and /create-oe-writing check before /oe. Writes Task_Authoring/task_inputs/Working_Files/08_OE_Writing_Ledger.md or 08_OE_Check.md."
---

# Oracle Event writing: fact ledger (prep) and OE check (08)

Resolve this file through any symlink to locate `<bundle>/skills/<name>/SKILL.md`.
The bundle's parent is the workspace. Read `<bundle>/setup/GEN_EXECUTION.md` first, then follow the playbook
`Task_Authoring/playbooks/08_Oracle_Event_Writing.md` in full. Write only under
`Task_Authoring/task_inputs/`; never write to `Evals/`, `claude/` or `HarmonyGames_*`,
and never execute SQL.

Authorship (GEN_EXECUTION §2): the repository preserves model drafting/revision as a local exception to official V3 human authorship.

## Inputs

First run `python3 Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source`.
Use the shared `Working_Files/00_Task_Context.json` (all eight assigned fields,
registered universe source, `universe` block and `freeze_utc` seed bound). The assigned universe date selects the universe (GEN_EXECUTION § 0a): Feb 14, 2026 → normal, Oct 1, 2025 → synth-cut. Read only that universe, apply its state rules and clock, and stop if the date is missing — there is no default. Validate relied-on record dates and earlier state before grounding. V3
changed-topic rules govern over older Evals text. The existing Long→extreme and
Normal design limits remain local policy; Eval Portal is handled by the user.

Upstream slots in `Task_Authoring/task_inputs/`: `04_Prompt.txt` (required), `00_Assigments.md`, `01_Grounding_Dossier.md`, `01_Universe_Inject.sql`, `03_Error_Async_Config.txt`, `02_Reference_Files_Manifest.md`; check mode also `08_OE_Writing_Ledger.md` (run prep first) and `08_Oracle_Events.md`. If a required one is
missing, stop and name it. Ground every fact through `Task_Authoring/tools/hg.py search` and
apply the persona ACL yourself (search does not).
Visibility per fact is proven with `tools/persona_view.py can-see` (base) or `check-sql --load-bearing` (seeded) and the YES lines are pasted under §B; the gate also re-checks every scoped id in §B itself. Every opaque locator carries a Locator origin (`prompt`, an earlier `F-n`, or a natural `search "<query>"` the gate re-runs as the persona). Dates are typed (record time vs semantic future date) before the clock is applied. The act-vs-defer search covers every service governing the entity, with population, pagination and governing version recorded, or it is UNRESOLVED. Every expected value is re-read through `tools/hg.py`.

Eval `task-quality-v1` (`Evals/2_Oracle_Events_Eval.md` §2.4, `Evals/references/rules/oracle_events.md` `expected_values`): label every expected-data line `Expected:`; each ID, event name, field value, channel, SHA, version, figure and date on it is quoted character for character from a cited record — the call site or live record, never a declaration, config or policy file (calibration #7: `quest_completed`, not `quest_completion`); narrative values are `not_a_claim`; an absence claim ("none", "no later commit") needs a scope-bound check of the whole population (calibration #47). The ledger carries one row per Expected value. Every record a rubric row grades needs an OE step with a stable label (the rubric review cites it verbatim; an OE edit makes that review stale). No step reads a Gmail or Slack attachment's content (no bytes are served). A Linear create-issue step must be satisfiable with `state_history_json`; Linear dates are exact `YYYY-MM-DDTHH:MM:SSZ` text. A `BOTH_FAIR_FIGURE` in the prompt report puts both values and their records in the OE. Never cite the placeholder `threads/00000000.json`.

## Output
prep mode: `task_inputs/Working_Files/08_OE_Writing_Ledger.md` · draft mode: `task_inputs/08_Oracle_Events.md` · check mode: `task_inputs/Working_Files/08_OE_Check.md`. Both end with the playbook's **Self-review** (GEN_EXECUTION §6a): counter-readings for every completeness and accuracy judgement, every expected value re-read through `tools/hg.py`.

Check mode must report exactly `Path feasibility SUPPORTED`, `Task solvability SUPPORTED_BY_OE` and `Blocking 0`; `release.oe_solvability` parses those three and blocks on anything else. The fact ledger also carries any control/channel fact that affects the path, and the exact deliverable locations; an OE path that depends on a channel record the agent cannot see is not solvable.

## Stage gate (blocking)
Run `python3 Task_Authoring/tools/stage_gate.py oe-writing Task_Authoring/task_inputs --paste` (prep) or `… oe-check …` (check mode). Handoff is blocked until it prints `STAGE GATE <stage>: PASS`; `--paste` writes that output into the Self-review, and the next stage's gate refuses an upstream artifact without a current PASS block. It checks structure and freshness, evidence pointers, locator provenance and defer-search completeness (prep), pasted tool outputs (re-run and compared), persona reach, universe-KB use and the self-review's counter-readings. Fix the artifact; never edit the gate's output.

## Deliver
Report the output path(s), any blocking findings, the predicted `/oe` result (check mode: completeness, accuracy, overall, path feasibility, task solvability), and the next step: prep → `/create-oe-writing draft` or the human writes `08_Oracle_Events.md` (five fields per event, typed into the platform — the field blocks pasting) · check → fix, then `/oe`.
