# Plan — `/create-goal` skill (session goal before `/create-scenario`)

Written 2026-11-01 for oracle review before implementation. Status: implemented the same day. §11 records the oracle's
round-1 findings and what changed; §12 records the Opus 5.5 hardness guide's verification and incorporation; §13 the
implementation review; §14 the guide's move into the bundle; §15 the commit-time check. Where §3–§9 differ from the
files, the files and §11–§15 govern (for example, the generator
lives in `scripts/`, the word limits are 520 (warning) and 560 (ceiling), and there is no `--allow-existing-design`).

## 1. Purpose

A user pastes a platform assignment into a task folder's `00_Assigments.md`, then wants to start a **fresh session**
that analyses the task and stops before `/create-scenario`. Today the user writes that session's opening `/goal` by hand.
It tends to be long, to point at the wrong folder, and to omit the lessons in `learnings`. `/create-goal <task folder>`
generates that goal from the task's assigned inputs and the workspace state: short, tailored and copy-ready.

Reference output: the goal hand-written for `Task_Authoring/task_inputs6adfee3beedd90eb176361ac` (Leonard Hayes,
Executive · Corporate Ops · Authoring · Long Horizon · Hard · Feb 14, 2026), reproduced in §9. The generator should
reproduce it for that folder (with one fix: no pronoun for the persona, §5.6).

## 2. Verified constraints (evidence)

| # | Fact | Evidence |
|---|---|---|
| C1 | A skill is a folder `Task_Authoring/skills/<name>/SKILL.md` with `name` / `description` front matter; `setup/install.py --target both` links every `skills/*/SKILL.md` into `.claude/skills/` and `.agents/skills/` (relative symlinks, conflict-safe, idempotent) | `setup/install.py:34-64`; `.claude/skills/*` links; `tests/test_skill_registration.py` (fixture trees, not the real skill list) |
| C2 | `__gate_policy__` in every stage-gate PASS block is sha256 over **all `Task_Authoring/tools/*.py`**; any new or changed file there makes every task's pasted gate blocks stale (e.g. robert rev 7) | `tools/stage_gate.py:527-534` |
| C3 | The task context's `policy_hash` is the digest of `references/v3_policy.json` only | `tools/task_context.py:26,395,425` |
| C4 | Tools default to `Task_Authoring/task_inputs`; `--task-dir` or `TASK_AUTHORING_TASK_DIR` selects another folder; the assignment template still prints `--task-dir Task_Authoring/task_inputs` | `tools/hg.py:86`; `tools/runtime_context.py:126`; `README.md:72-88`; `task_inputs6adf…/00_Assigments.md:40` |
| C5 | `task_context.py --task-dir X [--require-source]` without `--write` validates the assignment against roster and policy and prints the context JSON; exit 2 = assignment fail, 1 = source blocked; nothing is written | `tools/task_context.py:385-425`, `main()` |
| C6 | `Evals/tools/hg_store_input.py list` is read-only (fingerprints, no writes); today it reports `universe_intake.state SELECTED`, key `synthcut` (Oct 1, 2025) and another task's `task-details`/SQL/prompt | `Evals/tools/hg_store_input.py:286-330`; run 2026-11-01 |
| C7 | Commit hook: eval paths are path components `eval*`, `bench*`, `metric(s)`/`score(s)`, `result(s)`, `.eval.`; none of the planned paths match → `verify` tier `code` | `.git/hooks/pre-commit:22-28,134-146` |
| C8 | Other sessions are editing `Task_Authoring/tools/` and created `Task_Authoring/generators/` today; `README.md`, `skills/`, `setup/`, `tests/`, `.claude/`, `.agents/` are clean in git | `git status` 2026-11-01 |
| C9 | Persona "today" and weekday are in the context (`universe.persona_today`, `persona_today_weekday`); the date comes from the assignment, never from the Evals store; there is no default | `00_Task_Context.json`; `setup/GEN_EXECUTION.md` §0a |
| C10 | Difficulty: caps Easy 90 / Medium 85 / Hard 70 (strict), < 5 full passes, population SD 0.1–0.3, ≥ 2 failure patterns; design target E[avg] ≤ cap − 8 (82 / 77 / 62) and P(all gates) ≥ 0.5 before any SQL | `00_Assigments.md` V3 block; `setup/GEN_EXECUTION.md:263,289`; `playbooks/12_Difficulty.md:41`; `playbooks/01_Scenario_Design.md:125-126`; `plans/V3_Opus55_Difficulty_Plan.md:242` |
| C11 | Long Horizon → extreme profile (≥ 500 designed calls, ≥ 300 per-record); `volume_exception` may lower only those two minima (never below 100); Normal Horizon → 60–100 | `setup/GEN_EXECUTION.md` §3a |
| C12 | Task Skill is a hard gate; "If Authoring is assigned, require a real authored artifact, not a chat message"; Business Function's worst score is 3 when the work fits another function at least as well | `Evals/references/rules/scoring.json:128-152` |
| C13 | Open-ended work needs "objective acceptance boundaries"; the passage that rules out reading B must be a prompt sentence or a persona-readable record | `Evals/1_Prompt_Eval.md:602-665` |
| C14 | Sibling tasks: `task_inputs` (Robert, `robert-vendor-schedule`, normal), `task_inputs2` (Julia, `dd-2025-closeout`, synth-cut), `task_inputs3` (Arthur, `sunset-first-delivery-plan`, normal, with `00_Pre_Scenario_Analysis.md`); slug = first line of `01_Scenario_Design.md` | files on disk |

## 3. Files

| File | Role |
|---|---|
| `Task_Authoring/skills/create-goal/SKILL.md` | the skill: flow, rules, report |
| `Task_Authoring/skills/create-goal/build_goal.py` | deterministic generator and self-check (stdlib only); lives in the skill folder, not `tools/` (C2) |
| `Task_Authoring/skills/create-goal/goal_rules.json` | curated per-skill, per-function and per-competency lines and the fixed design rules, each with source citations (`path` + exact `contains` phrase) |
| `Task_Authoring/tests/test_create_goal.py` | unit tests on fixture task folders plus a drift test on the real sources |
| `Task_Authoring/README.md` | one command-table row; "All 11 skill folders" → 12; the stage-gate sentence notes that `/create-goal` has no stage |
| `.claude/skills/create-goal`, `.agents/skills/create-goal` | created by `setup/install.py --target both` (C1) |

Not changed: `tools/` (C2), `stage_gate.py` (no new stage), `Evals/`, `claude/`, universe folders, other task folders,
the Evals input store.

## 4. Inputs (all read-only) and fail-closed rules

1. Task folder: from the user's message; else `TASK_AUTHORING_TASK_DIR`; if neither and more than one `task_inputs*`
   folder exists, `build_goal.py --list` prints each folder's persona, assignment and design status and the skill asks.
2. Context: `python3 Task_Authoring/tools/task_context.py --task-dir <dir> --require-source` (no `--write`, C5). Exit
   2 or 1 → stop and report the tool's message (no date default, C9).
3. Saved context `Working_Files/00_Task_Context.json`: missing or `context_hash` different → note only ("the fresh
   session's first skill writes it").
4. Evals store: `hg_store_input.py list` → `universe_intake` and the `task-details` sha256 versus this folder's
   `00_Assigments.md`. Unreadable → note "store state unknown"; never write to it.
5. Siblings: every other `Task_Authoring/task_inputs*/` with a readable `Working_Files/00_Task_Context.json` → persona,
   competency, skill, universe; slug from the first line of `Working_Files/01_Scenario_Design.md` when present.
   Archived tasks are ignored.
6. Pre-scenario analyses: other folders' `Working_Files/00_Pre_Scenario_Analysis.md`, ranked same universe +
   competency > same universe > other; at most one cited.
7. `learnings` at the workspace root: highest `## N.` section and checklist item, to cite "§1–N".
8. `goal_rules.json`: every `contains` phrase must occur in its `path`; drift → exit 3 naming the stale citation.
9. Existing design: `Working_Files/01_Scenario_Design.md` in this folder → exit 4 ("this task already has a scenario;
   use `/create-scenario --revise`"), unless `--allow-existing-design`.

## 5. The goal (template; ≤ 480 words, hard stop at 520)

Blocks, in order; `[if …]` lines are conditional:

1. `/goal Author the HarmonyGames task in <abs task dir>/ (other paths below are relative to <workspace>) so it scores 5
   on every platform eval (/injection, /prompt, /hardness, /oe, /rubric in Evals/ and claude/skills/) and passes
   /create-difficulty on the first six baselines.`
2. `Assignment: <persona> (<role>) · <BF> · <competency> · <skill> · <horizon> · <Mode> · <universe label>
   (<persona first name>'s "today" is <weekday> <d Mon>). Difficulty gate: six Opus 5.5 runs, average < <cap> %,
   < 5 full passes, population SD 0.1–0.3, ≥ 2 failure patterns.`
3. Setup:
   - `[if dir ≠ Task_Authoring/task_inputs]` The tools default to `Task_Authoring/task_inputs/` (<that folder's
     persona>'s task). Export TASK_AUTHORING_TASK_DIR to this folder, pass it to every tool, and read "task_inputs/" in
     the skills as this folder.
   - `[if store universe ≠ task universe, or store task-details ≠ this assignment]` The Evals input store holds another
     task (<store label>). Leave it alone until you run an Evals skill; then save this task's inputs and select <label>
     first.
   - Write only in this folder. Never edit Evals/, claude/, Task_Authoring/tools/, the universe folders or other task
     folders, and never execute SQL.
4. Read: `learnings (§1–<N> and the checklists)`, `Task_Authoring/skills/`, `Task_Authoring/references/Scenario_Atlas.md`
   `[if an analysis exists]`, and `<path>` (<persona>'s task: gate table, precedents, Opus behaviour, volume floor;
   re-check it before reusing).
5. Design rules from past failures (fixed text from `goal_rules.json`, values filled in):
   1. UGT: `<skill line>`. Apply every rule sentence to every item, and make no completeness claims.
   2. Fit: the work must read as `<BF meaning>` more clearly than any other function (a 3 otherwise), inside
      `<competency>` (`<focus>`).
   3. /injection: check every seeded entity across the whole universe, and date each seed after the base events it
      relies on.
   4. /hardness: Robert rev 6 scored 1 because Opus 5.5 reads everything a hub names, scripts sweeps and applies stated
      rules. Put deciding facts where a natural run won't look, keep every trap live, state no precedence rule, and use
      ≥ 4 independent channels with graded findability. Before SQL, score whole policies and single misses on the real
      surface; target E[avg] ≤ `<cap − 8>` % and P(all gates) ≥ 0.5.
   5. `<Persona first name>` owns every write target, and every graded write has a trigger `<persona first name>` owns.
   6. Design scenario, injection and prompt together, so every OE and rubric row can quote its expected value.
6. `This session is analysis only. Write Working_Files/00_Pre_Scenario_Analysis.md [in <sibling>'s shape]:` what a 5
   needs at each gate; `<first name>`'s reach at the clock; 2–3 storylines with a recommendation `[, distinct from
   <persona>'s (<slug>) …]` (same-universe siblings only); the UGT, hardness and volume plans; my decisions: the
   storyline; `[Long Horizon]` a volume exception (GEN_EXECUTION §3a) if ≥ 500 necessary calls aren't reachable — never
   pad; any review waiver. `Then stop and tell me to run /create-scenario.`
7. `[--note "…"]` user-supplied standing decisions, appended verbatim under "Also:" (e.g. "skip red team and
   methodology; record the waiver").

Per-skill UGT lines (`goal_rules.json`):

| Skill | Line | Sources |
|---|---|---|
| Retrieval | every graded value is read from records the persona can open; populations, units and the as-of time are defined there, so careful readings converge on one value | Taxonomy Retrieval; Eval 1 §2.1 |
| Analysis and Synthesis | every finding (figure, reconciliation, diagnosis) follows from incorporated rules and data with its basis stated, so two careful runs reach the same result | Taxonomy Analysis; Eval 1 §2.1 |
| Planning and Decision Support | a contested choice among record-grounded options, explicit tradeoffs and a dated, owned course of action; order, dates and owners are contents, each fixed by a prompt sentence or a persona-readable record; an open recommendation only inside a stated boundary | scoring.json Task Skill; Eval 1 §2.1; `task_inputs3` analysis §2 |
| Authoring | a real artifact (document, sheet, deck or email), not a chat reply; its required contents a closed set fixed by the prompt or a record the persona can open; wording free, facts exact | scoring.json Task Skill ("require a real authored artifact"); Eval 1 §2.1 ("objective acceptance boundaries") |
| Actions | every created or updated record has a fixed target, fields and values from incorporated sources; act versus defer is never left open | Taxonomy Actions; Eval 1 §2.1 ("act-versus-defer decisions") |

Function meanings come from `Evals/references/rules/task_categories.md` (assignment label → row: Executive → Founders /
Exec / Strategy, etc.; an unknown label prints as given with a warning). Competency focus comes from
`Task_Authoring/references/Taxonomy_V2_Step_Map.md` (Corporate Ops → "Fundraising, board, legal/contracts, vendor, HR").

### 5.6 Self-checks on the generated text (exit 5 on failure)

Word count ≤ 520 (warn above 480); no `<`/`{` placeholder left; every repo path in the goal exists; no pronoun for the
persona (name or "the persona" only); the current folder is not listed as a sibling; the store line appears iff C6's
mismatch rule fires; the TASK_AUTHORING_TASK_DIR line appears iff the folder is not the default; the volume decision
appears iff the profile is extreme.

## 6. Output

- `Working_Files/00_Session_Goal.md`: a provenance header (generated at, generator sha256, `goal_rules.json` sha256,
  context hash, store state, learnings section count, word count) and the goal in one fenced block. Overwritten on each
  run; no gate reads it; it is not a platform slot.
- stdout: the goal, then a `FACTS` JSON line (folder, assignment, siblings, store, analysis cited, checks), then
  `CREATE-GOAL: PASS` or the failing check.

## 7. SKILL.md flow

1. Resolve the task folder (§4.1). Read only; do not run `task_context.py --write` (the fresh session's first skill
   does), do not touch the Evals store.
2. `python3 Task_Authoring/skills/create-goal/build_goal.py --task-dir <dir> [--note …]`.
3. On PASS, show the goal in one copy-ready code block, then up to five lines on what was tailored (non-default folder,
   store mismatch, siblings, analysis cited) and the output path. On failure, report the check and stop; never hand-edit
   the goal to get past a check.
4. Next step for the user: paste the goal into a fresh session; that session writes the pre-scenario analysis and stops;
   then run `/create-scenario` there.

## 8. Tests and verification

- `tests/test_create_goal.py` (unittest, temp fixture folders, the store injected as a JSON file via
  `--store-json` so no real store is read):
  Leonard-like (Authoring, Hard, Long, non-default folder, store mismatch) → setup lines, Authoring line, 70 % / 62 %,
  volume decision, siblings; default folder + matching store → neither setup line; Planning + Medium + Normal + synth-cut
  → planning line, 85 % / 77 %, no volume decision, weekday Wednesday; missing date → exit 2; existing design → exit 4;
  a drifted citation → exit 3; word budget; no pronoun.
- Drift test on the real repo: every `goal_rules.json` citation resolves.
- Smoke: run on the four real folders and diff the Leonard output against §9.
- Existing tests: `python3 -m unittest discover -s Task_Authoring/tests`.
- Gate: stage only the new files and README, `verify` tier `code` (C7); report `verified_by` and fallbacks.

## 9. Reference goal (Leonard folder, as hand-written; "he" already replaced by "Leonard")

```text
/goal Author the HarmonyGames task in /Users/sumitkumar/Source/Outlier/OC/Task_Authoring/task_inputs6adfee3beedd90eb176361ac/ (other paths below are relative to /Users/sumitkumar/Source/Outlier/OC) so it scores 5 on every platform eval (/injection, /prompt, /hardness, /oe, /rubric in Evals/ and claude/skills/) and passes /create-difficulty on the first six baselines.

Assignment: Leonard Hayes (Co-founder & Creative Director) · Executive · Corporate Ops · Authoring · Long Horizon · Hard · Feb 14, 2026 (normal universe; Leonard's "today" is Saturday 14 Feb). Difficulty gate: six Opus 5.5 runs, average < 70 %, < 5 full passes, population SD 0.1–0.3, ≥ 2 failure patterns.

Setup
- The tools default to Robert's task_inputs/. Export TASK_AUTHORING_TASK_DIR to this folder, pass it to every tool, and read "task_inputs/" in the skills as this folder.
- The Evals date store holds Oct 1, 2025 from another task. Re-select Feb 14, 2026 before any Evals skill.
- Write only in this folder. Never edit Evals/, claude/, Task_Authoring/tools/, the universe folders or other task folders, and never execute SQL.

Read: learnings (§1–44 and the checklists), Task_Authoring/skills/, Task_Authoring/references/Scenario_Atlas.md, and task_inputs3/Working_Files/00_Pre_Scenario_Analysis.md (Arthur's task: gate table, precedents, Opus behaviour, volume floor; re-check it before reusing).

Design rules from past failures
1. UGT: Authoring needs a real artifact, not a chat reply. Its required contents must be a closed set fixed by the prompt or by a record Leonard can open; wording is free, facts are exact. Apply every rule sentence to every item, and make no completeness claims.
2. /injection: check every seeded entity across the whole universe, and date each seed after the base events it relies on.
3. /hardness (Robert rev 6 scored 1): Opus 5.5 reads everything a hub names, scripts sweeps and applies stated rules. Put deciding facts where a natural run won't look, keep every trap live, state no precedence rule, and use ≥ 4 independent channels with graded findability. Before SQL, score whole policies and single misses on the real surface; target E[avg] ≤ 62 % and P(all gates) ≥ 0.5.
4. Leonard owns every write target, and every graded write has a trigger Leonard owns.
5. Design scenario, injection and prompt together, so every OE and rubric row can quote its expected value.

This session is analysis only. Write Working_Files/00_Pre_Scenario_Analysis.md in task_inputs3's shape:
- what a 5 needs at each gate
- Leonard's reach at the clock
- 2–3 storylines with a recommendation, distinct from Robert's (vendor creditor schedule) and Arthur's (Sunset data delivery)
- the UGT, hardness and volume plans
- my decisions: the storyline; a volume exception like task_inputs3's if ≥ 500 necessary calls aren't reachable (never pad); any review waiver
Then stop and tell me to run /create-scenario.
```

The template in §5 differs from this text in three ways: a "Fit" rule (business function and competency) is added,
the Evals-store line says to leave the store alone until an Evals skill runs (learnings §37), and siblings are named by
their design slug.

## 10. Questions for the oracle

1. Is the skill folder the right home for the generator, given C2 (tools hash) and C8 (concurrent edits)?
2. Deterministic template versus a model-written goal from a brief: which gives fewer stale or wrong goals?
3. Read-only context (no `--write`) — any downstream problem?
4. Existing design → refuse (exit 4) or produce a `--revise`-flavoured goal?
5. Is anything in §5 wrong, risky or missing for a 5/5 path (UGT, alignment, hardness, difficulty)? Anything that
   would push the fresh session to over-constrain the scenario or conflict with the skills' own rules?
6. Word budget 480/520: right size for "brief"?
7. Is the citation-drift check (exit 3) worth its brittleness?
8. Any risk to other tasks or sessions not covered by C2–C8?

## 11. Oracle review, round 1 (GPT-6.1 Sol, session `ses_e6b9f1260ffeKqv2ePWYCG3GWg`): REVISE, then implemented

| # | Finding (tag) | What changed |
|---|---|---|
| 1 | Blanket hardness lines ("state no precedence rule", "put deciding facts where a natural run won't look") contradict the playbook (MUST) | Replaced by "keep authority clear and incorporated and answers out of hubs and checklists, so difficulty survives complete retrieval"; Robert's run is described as one run (later dropped for the guide, §12) |
| 2 | Universal constraints overstated (MUST) | Skill lines accept fixed or bounded outcomes; "claim completeness only with a census"; rows trace to incorporated facts; ownership limited to Drive, Docs and Sheets, with an authorized trigger and proven write access for every write |
| 3 | Execution boundary (MUST) | Goal separates task files from helper caches and ledger tools, starts with GEN_EXECUTION and `task_context.py --write --require-source`, searches through `hg.py`, forbids prompt, OE and rubric text, and leaves the Evals store alone; the skill states its own exceptions (no `--write`, no stage gate, read-only store) |
| 4 | Isolation (MUST) | Bytecode off for the script and every helper; inherited `TASK_AUTHORING_TASK_DIR` removed; `Working_Files` must be a real folder inside the task; atomic write; `--stdout-only`; a `WARN` when another session's files are present |
| 5 | Self-checks must accept valid output (MUST) | Brace tokens, not punctuation; input paths must exist, the output path must stay inside the task; both cases tested |
| 6 | Difficulty summary (SHOULD) | 3 channels, 4 for Hard; gate line points at `playbooks/12_Difficulty.md`; forecasts UNCALIBRATED |
| 7 | Existing design (SHOULD) | Exit 4 names the stage reached and the hardening route; no bypass flag |
| 8 | Citation checks (SHOULD) | Required lines fail closed (exit 3), optional lines drop with a `WARN`; each citation has a kind; documented as a presence check, not a semantic one |
| 9 | Shared git index (MUST) | Nothing staged or committed: the index holds another session's staged `Task_Authoring/generators/` files |

## 12. Opus 5.5 hardness guide (`hardness update.md`), verified and incorporated 2026-11-01

The user added `hardness update.md` at the workspace root: the platform's "Making a Task Hard for Opus 5.5 (Hardness
v2)", built on 46 tasks, 270 runs and 2,843 graded rows. Its data cannot be checked here; its rules were checked
against the gates and this workspace's own Opus 5.5 run.

Agrees with the sources:

- Caps 90/85/70 strict, six runs, weighted average (`v3_policy.json`; `playbooks/12_Difficulty.md`).
- Volume, steps, services and clean totals don't lower scores (GEN_EXECUTION §3a; `Hardness_Mastery.md` §0; Robert rev 6:
  about 800 calls, `/hardness` 1).
- Same-place corrections are caught (learnings §28: a trap is not live when the decoy and its correction come back
  in the same call). This updates A14 ("replies never opened"), which was measured on Opus 4.8.
- Rules stay out of the prompt (`Docs/11_V3_Changes.md`; learnings §1).
- Injected data must reach the agent's tools (learnings §26, §32).
- One condition per row, end state rather than route, no duplicated downstream rows, and tolerance only for calculated
  figures (`Evals/3_Rubrics_Eval.md` §2.2, §2.10, §2.12; counts stay exact).

Corrected before use:

1. **"Put weight 5 on the trap rows" / "raise the weight".** `3_Rubrics_Eval.md` §2.12: "Weight the work for that
   atomic result, never business importance"; weight 5 is multi-source reconciliation. The goal says each miss must flip
   a multi-source row, weight 5 by kind of work, never raised.
2. **Deterministic 6/6 misses.** Every worked example is a 6/6 miss. If every run fails the same rows, QC's
   failure-signature rule ("Need >=2 distinct signatures and no single signature >50% of failing rollouts";
   `QC_Spec_Doc_Latest.csv`) and the SD band 0.1–0.3 fail (learnings §29). The goal adds a spread rule: vary findability.
3. **Worked examples.** They are real tasks that use this universe's people and channels (one turns on a ticket comment
   from Leonard; "Netflix" has 226 Slack hits Leonard can see; "Gustaf" has no Contacts entry, so some example entities
   were seeded by those tasks). The goal points at the trap types only.
4. **Guard rows.** Trap 9 grades that the agent "leaves those items alone", and Part 6 adds "a guard row" for an item
   left unchanged. `3_Rubrics_Eval.md` §2.9: "A row an agent passes by doing nothing fails Negative Criteria however
   it's worded". The goal says no row may pass by doing nothing (grade the positive result that leaves the item out).
   Found by the implementation review (§13).

Not applicable here: "a task with no mode is treated as Medium" (`task_context.py` refuses a missing mode), and "the
pre-check is an early warning, not a verdict" (true of the final verdict, but `/hardness` on the pre-check HOLDs at
1–2: `Evals/1A_Hardness_Eval.md`).

Its traps against `Hardness_Mastery.md`'s mechanism codes (for S5a): 1 "done" with a missing part → A6 + A13;
2 correction elsewhere → A9/A11 + A13; 3 rule-required write → A15/A21; 4 dates and dependencies → A4/A10/A17;
5 exception in older records → A12/A15; 6 aliases → A7/A8; 7 items outside the filter → A2/A5/A17; 8 wrong inputs to a
total → A1/A11; 9 work already done → A8/A10. Robert rev 7's members map to traps 2, 8 and 9 (not yet measured).

In the goal: the hardness rule takes the trap types (optional clause, `v2_traps`) plus the weight and do-nothing rules
(required), the spread rule is new and required, the injection rule asks for tool visibility, and the deliverable asks
for the Part 7 checks (optional, `v2_checks`). The guide is git-ignored, so both guide clauses are optional and drop
with one `WARN` if it is missing (superseded by §14: the guide is now tracked and both clauses are required). The goal grew from 450 to 513 words for the Leonard task; the limits moved to 520
(warning) and 560 (ceiling on the generated text) so that store, sibling and path variants cannot fail a valid run.

## 13. Implementation review, round 1 (`reviewer`, GPT-6.1 Sol, session `ses_e6b78b7e9ffeUYl3Wh66z7upAn`): FAIL, fixed

Static review (the reviewer could not run Python); the questions on rule semantics, the guide corrections, the
registries and other sessions passed. Findings and fixes:

| Severity | Finding | Fix |
|---|---|---|
| Major | Tests required the git-ignored guide | Compose tests use a fixture guide holding exactly the cited phrases; the drift test checks guide phrases only where the file exists; a test asserts every guide-backed line is optional |
| Minor | Store match trusted the recorded sha256 without `integrity` | Match only `integrity == "OK"`; distinct texts for no task details, damaged details, another task, another date, unreadable store; tested |
| Minor | `--note` whitespace collapsed | Notes kept exactly as given; blank notes exit 6; CLI test |
| Minor | Paths with spaces broke the command and the path check | `--task-dir` shell-quoted; known paths checked whole and counted as one word; CLI test on a spaced folder |
| Minor | Write failures escaped as exit 1 | Every `OSError` while writing becomes exit 6 with the temp file removed; directory-at-output, symlinked-output and failed-replace tests |
| Note | Standalone do-nothing rows (trap 9) | Fourth correction in §12 |

Found while fixing: a folder with no design was named as a storyline to stay distinct from ("Leonard's (no design
yet)"), so only designed siblings are named, at most three, same competency first.

Round 2 (same session): FAIL on two Minor edge cases, both fixed. The copy block's fence is now one backtick longer
than any backtick run in the goal, since verbatim notes may contain fences (multiline-note CLI test). Unindexed task
details from an earlier bundle (`unindexed_local_inputs`, `hg_store_input.py`) are reported as this or another task's
details, not as "no task details" (`StoreTests`). 37 skill tests, 95 in all, pass.

Round 3 (same session): PASS, no findings (static review; the reviewer could not run Python, the test results are this
session's).

## 14. The guide moved into the bundle (2026-11-01, at the user's request)

`hardness update.md` (workspace root, ignored by `.gitignore:3`) moved byte-identical (sha256 `1a3d599e7808…`) to
`Task_Authoring/references/Docs/13_Hardness_v2_Opus55.md`, beside the platform's other guidance. The folder is tracked,
and no tool hashes or lists its files, so no stage-gate record goes stale. The name follows the folder's numbering and
its recent underscore style.

What changed with it: the goal cites the full path (the self-check now verifies it exists) and refers to "the guide's
Part 7 checks"; `v2_traps` and `v2_checks` are required, so a missing or edited guide stops the run with exit 3; the
tests use the real guide (the fixture is gone) and check that guide-backed lines are required and live under
`Task_Authoring/references/Docs/`; the `hardness_guide` FACTS key is gone; SKILL.md and README.md updated.

Not done: a pointer line in `Task_Authoring/references/Hardness_Mastery.md`. `tools/hardness_ledger.py` seeds ledger
records that cite that file by sha256 and by line number (§0 and §11 rows, `hardness_ledger.py:518–547`); an inserted
line would shift every citation in the append-only ledger and in the seed tables.

## 15. Commit-time check (2026-11-01)

The tests were re-run on the exact tree to be committed: a clean worktree with no `Task_Authoring/task_inputs*` folders
(untracked) and no universe data (git-ignored). That run found a bug the main checkout hid. The default-folder line
named `Task_Authoring/task_inputs/` literally, and the self-check requires every input path the goal names to exist,
so in a fresh checkout without that folder every run for another task folder stopped with exit 5. The line now takes
the folder from the script's default (`default_rel`), which is named but never required to exist, and describes it as
"not present" when it is missing. Two regression tests cover this. The eight CLI tests need the universe data
(`task_context.py --require-source`), so they run only in a checkout that has it.
