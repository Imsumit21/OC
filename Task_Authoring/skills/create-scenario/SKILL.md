---
name: create-scenario
description: "Design an extremely hard HarmonyGames task before any SQL: storyline from the Scenario Atlas, persona reach census, cohort spine with shortcut audit (≥ 500 necessary calls, plan ~600, over ≥ 10 services), 2–4 hidden authorities with decoys, asks spread over ≥ 12 fragments in ≥ 7 services, ≥ 3 independent chains, ≥ 12 traps, QC rails, then tools/hardness_gate.py --design and an optional Red team. Use /create-scenario first, once 00_Assigments.md is filled. Writes Task_Authoring/task_inputs/Working_Files/01_Scenario_Design.md + the draft manifest 01_Hardness_Manifest.draft.json. Designs only — never drafts prompt, Oracle Event or criterion text."
---

# Scenario design + hardness manifest (01, first step)

Resolve this file through any symlink to locate `<bundle>/skills/<name>/SKILL.md`.
The bundle's parent is the workspace. Read `<bundle>/setup/GEN_EXECUTION.md` first (§ 3a hardness targets), then
`Task_Authoring/references/Hardness_Mastery.md`, then follow the playbook
`Task_Authoring/playbooks/01_Scenario_Design.md` in full. Write only under
`Task_Authoring/task_inputs/`; never write to `Evals/`, `claude/` or `HarmonyGames_*`,
and never execute SQL.

This command designs the scenario, the records and the difficulty; the prompt, Oracle Events and rubric criteria are written later (Claude, Codex or the human — GEN_EXECUTION §2).

## Inputs

First run `python3 Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source`.
Use the shared `Working_Files/00_Task_Context.json` (all eight assigned fields,
registered shared data source and assigned freeze). Both dates use the same local
data; validate relied-on record dates and earlier state before grounding. V3
changed-topic rules govern over older Evals text. The existing Long→extreme and
Normal design limits remain local policy; Eval Portal is handled by the user.

`Task_Authoring/task_inputs/00_Assigments.md` (exact eight-field V3 paste) and its shared normalized context. Resolve the assigned persona and role before choosing work. References are leads until verified against the context's supported snapshot. Ground every fact through `Task_Authoring/tools/hg.py search` / `records` and apply persona ACL (search does not).

## Output
`task_inputs/Working_Files/01_Scenario_Design.md` and the draft manifest `task_inputs/Working_Files/01_Hardness_Manifest.draft.json` (with `horizon`, the resolved `effective_profile` and, for a requester-confirmed extreme design on a Normal Horizon, `profile_exception`); `task_inputs/Working_Files/01b_Redteam_Review.md` + `.second.md`.

## Checks
- `python3 Task_Authoring/tools/hardness_gate.py Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.draft.json --design` → PASS. The profile comes from the manifest's `effective_profile` (Long Horizon → extreme; Normal → normal unless the requester confirms extreme, recorded in `profile_exception`); a disagreeing `--profile` fails.
- Manifest contract (`references/Hardness_Manifest_Spec.md`): verbatim `delegation_quote` per fragment, `requirement_ids` (no orphan requirement), `names_authorities` (no orphan authority), surface `requirement` + `decides` (no manufactured columns), `decoy_scope` or a superseded decoy, `root_cause` from the `Hardness_Mastery.md` mechanism enum, conditional budget rows counting 0, designed denials as `denied_probes` with YES alternates, anchors named by noun phrases of ≤ 6 words.
- Lazy-solver pass (playbook S9) with every leak fixed.
- Coherence audit (playbook S1: seven QC categories over everything a correct run opens, plus the sibling-defect sweep) and the coherence rail (S8), each row dispositioned.
- Self-review (playbook S9, GEN_EXECUTION §6a) recorded in section 12; write the scenario role review in `Working_Files/00_V3_Authoring_Evidence.json` (Guide schema), binding assigned role, sources and design artifact hash. Record counter-readings, gate output and unresolved items.
- Persona census `tools/persona_view.py reach`, storyline on `references/universe_kb/` (timeline, cohorts, trap_catalog ids), coherence audit against `coherence_hazards.json`, active speakers from `activity.json`, identity traps from `tools/entity.py collisions` (playbook S0–S1).
- Required: `python3 Task_Authoring/tools/redteam_review.py --mode redteam --dual --in <design> --in <manifest> --out Task_Authoring/task_inputs/Working_Files/01b_Redteam_Review.md` (two independent reviewers); never print the proxy key.

## Stage gate (blocking)
Run `python3 Task_Authoring/tools/stage_gate.py scenario Task_Authoring/task_inputs --paste`. Handoff is blocked until it prints `STAGE GATE <stage>: PASS`; `--paste` writes that output into the Self-review, and the next stage's gate refuses an upstream artifact without a current PASS block. It checks structure and freshness, evidence pointers, pasted tool outputs (re-run and compared), persona reach, universe-KB use and the self-review's counter-readings. Fix the artifact; never edit the gate's output.

## Deliver
Report the storyline, services (natural vs injected), cohort × surfaces, authorities, chains, call-budget total, the gate verdict verbatim and the red-team status. Next: `/create-injection`.
