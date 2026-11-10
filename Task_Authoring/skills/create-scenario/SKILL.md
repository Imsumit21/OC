---
name: create-scenario
description: "Design an extremely hard HarmonyGames task before any SQL: storyline from the Scenario Atlas, persona reach census, cohort spine with shortcut audit (≥ 500 necessary calls, plan ~600, over ≥ 10 services), 2–4 hidden authorities with decoys, asks spread over ≥ 12 fragments in ≥ 7 services, ≥ 3 independent chains, ≥ 12 traps, a mechanism portfolio with ledger priors, the gradable surface, QC rails, then tools/hardness_gate.py --design and a dual Red team (or a recorded fallback). --revise first takes in /create-hardening MODE B verdicts. Use /create-scenario first, once 00_Assigments.md is filled. Writes <task_dir>/Working_Files/01_Scenario_Design.md + 01_Hardness_Manifest.draft.json + 01_Gradable_Surface.json. Designs only — never drafts prompt, Oracle Event or criterion text."
---

# Scenario design + hardness manifest (01, first step)

**Task folder (required).** `<task_dir>` in this skill and its playbook is the task folder given as this command's
argument, for example `/create-scenario Task_Authoring/task_inputsRobert`. If no folder is given and
`TASK_AUTHORING_TASK_DIR` is unset, stop and ask which folder; never guess and never fall back to a default. Pass
the same folder as `--task-dir` to every tool. A new task has its own named folder
(`Task_Authoring/task_inputs<Label>`), not a bare `Task_Authoring/task_inputs`, so two tasks never share one.

Resolve this file through any symlink to locate `<bundle>/skills/<name>/SKILL.md`.
The bundle's parent is the workspace. Read `<bundle>/setup/GEN_EXECUTION.md` first (§ 3a hardness targets), then
`Task_Authoring/references/Hardness_Mastery.md`, then follow the playbook
`Task_Authoring/playbooks/01_Scenario_Design.md` in full. Write only under
`<task_dir>/` (plus the forecast's ledger append through its tool, GEN_EXECUTION §1); never write to
`Evals/`, `claude/` or `HarmonyGames_*`, and never execute SQL.

This command designs the scenario, the records and the difficulty; the prompt, Oracle Events and rubric criteria are written later (Claude, Codex or the human — GEN_EXECUTION §2).

`/create-scenario --revise` (playbook S0r) runs when a `/create-hardening` MODE B report exists for the current revision: take in its node verdicts first (keep · purge · rebuild each one, confirm or assign CONFOUNDED, keep every export bound to the revision it ran on, route each finding) in design section 14, then revise from S5a onward with a `design_delta`.

## Inputs

First run `python3 Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source`.
Use the shared `Working_Files/00_Task_Context.json` (all eight assigned fields,
`universe.key`, the `freeze_utc` seed bound, `source.kb_status`). The assigned universe date selects the universe (GEN_EXECUTION § 0a): Feb 14, 2026 → normal, Oct 1, 2025 → synth-cut. Read only that universe, apply its state rules and clock, and stop if the date is missing — there is no default. Validate relied-on record dates and earlier state at the seed bound before grounding; no seeded event timestamp is after it and nothing after it is treated as completed. V3
changed-topic rules govern over older Evals text. The existing Long→extreme and
Normal design limits remain local policy; Eval Portal is handled by the user.

`<task_dir>/00_Assigments.md` (exact eight-field V3 paste) and its shared normalized context. Resolve the assigned persona and role before choosing work. References are leads until verified against the context's supported snapshot. Ground every fact through `Task_Authoring/tools/hg.py search` / `records` and apply persona ACL (search does not).

## Output
`<task_dir>/Working_Files/01_Scenario_Design.md` and the draft manifest `<task_dir>/Working_Files/01_Hardness_Manifest.draft.json` (with `horizon`, the resolved `effective_profile`, the `mechanism_portfolio` — one entry per future solver rule, each with its natural-reading fallback — and, for a requester-confirmed extreme design on a Normal Horizon, `profile_exception`); the gradable surface `<task_dir>/Working_Files/01_Gradable_Surface.json` (this stage owns it; `/create-injection` never rewrites it); `<task_dir>/Working_Files/01b_Redteam_Review.md` + `.second.md`.

## Checks
- **Known data issues (blocking):** read `references/known_data_issues/<universe>.md` (normal: NB-1–33, synth-cut: SC-1–73). No load-bearing fact, trap, Oracle Event or rubric row may rest on a card's "Don't grade" value; cite every card the task touches, with its disposition, in the coherence audit. Reviewers fail tasks on these cards.
- **No filler for volume** (Reaching the Tool-Call Minimum, 2026-10): padding is a failing error on its own. Never add a record, field, SQL comment, service or step only to raise the call count; volume comes from items that each need their own check, and every item must change the result.
- Universe (playbook S0/S1): record the universe key, label, clock line, seed bound and `shutdown_rules_apply` before any storyline research; candidates must exist in that universe. Synth-cut excludes the six post-cut storylines and anything after 2025-09-30 23:59:59 PT, with no shutdown premise; on normal, business as usual after the Feb 11, 2026 shutdown is a false premise unless the wind-down is acknowledged; Victor Barnes is not active in either universe (`Evals/1_Prompt_Eval.md` §2.3). Storyline census 76 / 70, never 80.
- `python3 Task_Authoring/tools/hardness_gate.py <task_dir>/Working_Files/01_Hardness_Manifest.draft.json --design` → PASS. The profile comes from the manifest's `effective_profile` (Long Horizon → extreme; Normal → normal unless the requester confirms extreme, recorded in `profile_exception`); a disagreeing `--profile` fails.
- Manifest contract (`references/Hardness_Manifest_Spec.md`): verbatim `delegation_quote` per fragment, `requirement_ids` (no orphan requirement), `names_authorities` (no orphan authority), surface `requirement` + `decides` (no manufactured columns), `decoy_scope` or a superseded decoy, `root_cause` from the `Hardness_Mastery.md` mechanism enum, conditional budget rows counting 0, designed denials as `denied_probes` with YES alternates, anchors named by noun phrases of ≤ 6 words.
- Lazy-solver pass (playbook S9) with every leak fixed.
- Coherence audit (playbook S1: seven QC categories over everything a correct run opens, plus the sibling-defect sweep) and the coherence rail (S8), each row dispositioned.
- Self-review (playbook S9, GEN_EXECUTION §6a) recorded in section 12; write the scenario role review in `Working_Files/00_V3_Authoring_Evidence.json` (Guide schema), binding assigned role, sources and design artifact hash. Record counter-readings, gate output and unresolved items.
- Persona census `tools/persona_view.py reach`, storyline on `references/universe_kb/` (timeline, cohorts, trap_catalog ids), coherence audit against `coherence_hazards.json`, active speakers from `activity.json`, identity traps from `tools/entity.py collisions` (playbook S0–S1).
- Mechanism portfolio (playbook S5a): 10–15 grounded candidates, each with its prior from `python3 Task_Authoring/tools/hardness_ledger.py priors --model <assigned baseline model> --family <family>` and the record ids behind it (per model, never pooled; another model's evidence only through a transfer record). Never resolve a liveness flag by removing an incorporation or UGT link.
- Gradable surface (playbook S6b): `python3 Task_Authoring/tools/gradable_surface.py validate --task-dir <task_dir>` → PASS (work-kind weights, ≤ 5 samples per group plus a volume slot, exceptions an incorporated authority singles out, no fact in ≥ 3 slots). The mechanism share is reported, not gated.
- Gradeable at design time: `python3 Task_Authoring/tools/gradable_surface.py gradeable-report --task-dir <task_dir>` → `SURFACE.GRADEABLE PASS` with 0 ungradable slots. Every slot must point at a deliverable and selector the grader decodes (table column, tracker text, `json_text`/`calls` delivery, `tracker_state`, `register_parent`, `share_reader`, `register_keys_exact`, …); a group/tracker slot additionally needs `truth_fields.groups` to name the list field, and a slot the decoder cannot grade is a design defect, not a grader defect.
- Controls and channels: the mechanism portfolio must already declare, per future solver rule, its `controls` and `over_application` (control members and the operator that over-applies the rule to them) and every `CHANNELS` entry (`kind`, `degrade`, `members`, optional `latent`/`family`, or surface `slots` when the solver cannot express the failure). `/create-injection` S4b completes `solver.py` from that portfolio, `contract.controls` checks they are live, geometry U counts the channel degrades and over-application operators, and the forecast models the declared channels (a control trial is evidence, not a forecast input); a channel with no ledger record or disclosed `--channel-rate` is UNPARAMETERIZED, never zero.
- Hardness v2 (Opus 5.5; `Hardness_Mastery.md` §13): at least two of the nine v2 traps as separate cross-source decisions, corrections off the first-read path, and `python3 -B Task_Authoring/tools/hardness_v2_check.py --design --task-dir <task_dir>` (advisory) with a disposition per FLAG and UNRESOLVED (playbook S5, S5b).
- Advisory and UNCALIBRATED: `python3 Task_Authoring/tools/trap_liveness.py --design --task-dir <task_dir>` with a written disposition per flag (S5b); `python3 Task_Authoring/tools/hardness_forecast.py forecast --design --task-dir <task_dir> --model <baseline model> --mechanisms <portfolio ids> --preregister`, its ledger id pasted in section 12 (S9b).
- Required: `python3 Task_Authoring/tools/redteam_review.py --mode redteam --dual --in <design> --in <manifest> --out <task_dir>/Working_Files/01b_Redteam_Review.md` (two independent reviewers); never print the proxy key. `REDTEAM_*` is a precondition: a file holding only the tool's error is not a review. If the review cannot run, record `RED TEAM FALLBACK: <who reviewed instead, how, and why>` in section 13; without it the gate blocks.

## First-pass checks (playbook S0, S2x, S5c)
- **Fit census** (`fit.census`): read `Working_Files/00_Assignment_Fit.json` (`/create-goal` writes it; else `python3 -B Task_Authoring/tools/assignment_fit.py census --task-dir <task_dir> --write`). `FIT WITH LIMITS`: a THIN service holds no anchor and no coin-flip unit. `NO NATURAL COHORT`: build the scenario by injection (S2x). Never skip the task or ask for another persona. Read the persona card (`references/persona_cards/<universe>/<persona_key>.json`) and `references/base_surface_map.json`.
- **Difficulty budget** (`budget.design`): write `Working_Files/01_Difficulty_Budget.json` — two anchors from two causes carrying the mode's loss, at least four independent coin-flip units (find rate 0.35–0.65, each behind a different retrieval habit), each unit flipping two or more rows with one of weight 5, on carriers that produced misses. `python3 -B Task_Authoring/tools/difficulty_budget.py check --task-dir <task_dir>` → PASS; paste `difficulty_budget.py table` into section 6. Judgement traps stay for realism and carry no budget weight. The failure-signature gate comes first; spread second, with its printed chance recorded.
- These are first-pass checks: each prints WARN while its mode in `references/first_pass_policy.json` is `warn` and blocks once the owner sets it to `block` (`python3 -B Task_Authoring/tools/first_pass_controls.py modes`). Fix what they report either way.

## Stage gate (blocking)
Run `python3 Task_Authoring/tools/stage_gate.py scenario <task_dir> --paste`. Handoff is blocked until it prints `STAGE GATE <stage>: PASS`; `--paste` writes that output into the Self-review, and the next stage's gate refuses an upstream artifact without a current PASS block. It checks structure and freshness, evidence pointers, pasted tool outputs (re-run and compared), persona reach, universe-KB use and the self-review's counter-readings, plus the gradable surface (`surface.valid`), the red team or its recorded fallback (`tool.redteam_dual`) and, under `--revise`, the revision intake (`revise.*`); the prior forecast is a WARN only. Fix the artifact; never edit the gate's output.

## Deliver
Report the storyline, services (natural vs injected), cohort × surfaces, authorities, chains, the mechanism portfolio with each prior's record ids, the gradable surface's mechanism share (reported, not gated), call-budget total, the gate verdict verbatim, the red-team status (or the recorded fallback) and the pre-registered forecast id, labelled UNCALIBRATED. Next: `/create-injection`.
