# Manual Commands — copy-paste equivalents (V3 assignments)

In Codex, invoke the authoring skills as `$create-*` with the same arguments as
the `/create-*` examples below; in OpenCode, the `/create-*` commands work as written
(`.opencode/commands/`). Run shell commands from the workspace root;
path conventions are in `setup/GEN_EXECUTION.md`.

Use these when the `/create-*` skills are not installed, or to steer a step by hand.
Each prompt is the manual equivalent of one command; the playbook it names is the
source of truth. Run order and loop-backs: `How_To_Author_A_Task.md`.

**Stage gate after every command.** Each prompt below ends with its `tools/stage_gate.py <stage>` run: handoff is
blocked until it prints PASS, `--paste` writes the PASS block into the artifact's Self-review, and the next
stage's gate refuses an upstream artifact without a current block (`setup/GEN_EXECUTION.md` § 6b).

The repository preserves model drafting (GEN_EXECUTION § 2), an explicit exception
to official V3 human authorship. Hardening goes through the universe after unfair
criteria are corrected and regraded; existing extreme/normal targets remain local
design choices. The user handles Eval Portal, including review proof uploads.

---

## 0 · Assignment (no command)

Copy `Task_Authoring/references/Tasks_Template/.` into `Task_Authoring/task_inputs/`,
paste the eight-field assignment exactly into `00_Assigments.md` (including role,
difficulty mode and universe date), then run:

```sh
python3 Task_Authoring/tools/task_context.py --task-dir Task_Authoring/task_inputs --write
python3 Task_Authoring/tools/task_context.py --task-dir Task_Authoring/task_inputs --write --require-source
```

Every manual command below first uses the shared `Working_Files/00_Task_Context.json`
and rechecks `--require-source` before grounding. The assigned universe date selects
the universe (GEN_EXECUTION § 0a): Feb 14, 2026 → normal, Oct 1, 2025 → synth-cut.
Read only that universe, apply its state rules and clock, and stop if the date is
missing — there is no default. The seed bound scopes facts, seeded timestamps and
completed events; later events cannot be treated as completed, and later-edited
bodies need dated earlier evidence.
Use `--task-dir <task_dir>` consistently for another workspace. Keep the role/outcome
reviews and per-criterion source/variant evidence in
`Working_Files/00_V3_Authoring_Evidence.json`; schema and artifact-hash command are
in `How_To_Author_A_Task.md`.

For a nondefault task, pass `--task-dir <task_dir>` to every direct tool command,
or set `TASK_AUTHORING_TASK_DIR` for that shell. `stage_gate.py` retains its
positional task directory and propagates context to child checks. Normalizing a
context file does not change the shell environment; also replace the artifact
paths in the manual prompts below with that task workspace's paths.

Universe data install, merge/move and verification are documented in the repo root
`README.md` — [Install the universe data](../../README.md#install-the-universe-data),
[Already unzipped? Move, merge and store the data](../../README.md#already-unzipped-move-merge-and-store-the-data)
and [Verify](../../README.md#verify). The two universe folders are real folders at
the repo root, never edited and git-ignored; a symlink to another disk is refused by
the tools.

Universe helpers:

```sh
python3 Task_Authoring/tools/hg.py universe [show|list]                 # selected universe, clock, folders
python3 -B Task_Authoring/tools/verify_universe_data.py [--universe normal|synthcut] [--sha256]  # data vs source_manifest.json
python3 Task_Authoring/tools/hg.py lint [--sql PATH] [--checks a,b] [--no-base] [--summary]
python3 Task_Authoring/tools/hg.py rubric-lint <rubric.json>
```

`lint` runs the eval's `hg_injection_lint.py` and defaults `--sql` to
`<task_dir>/01_Universe_Inject.sql`; `rubric-lint` runs the eval's
`hg_rubric_lint.py`. Run both beside the local `sql_lint.py` / `hardness_gate.py`.

## 0.25 · Session goal (optional) · `/create-goal`

Prints a short `/goal` for a fresh session that writes `Working_Files/00_Pre_Scenario_Analysis.md` and stops before
`/create-scenario`. It is tailored to the assignment and the workspace state (other task folders, the Evals input store,
`learnings`). It has no stage gate and writes only `Working_Files/00_Session_Goal.md` (nothing with `--stdout-only`):

```sh
python3 -B Task_Authoring/skills/create-goal/scripts/build_goal.py --task-dir <task_dir> [--note "<decision>"] [--stdout-only]
python3 -B Task_Authoring/skills/create-goal/scripts/build_goal.py --list
```

## 0.5 · Scenario design · `/create-scenario`

```
Read Task_Authoring/setup/GEN_EXECUTION.md (§3a hardness targets) and Task_Authoring/references/Hardness_Mastery.md, then follow Task_Authoring/playbooks/01_Scenario_Design.md in full. Using Task_Authoring/task_inputs/00_Assigments.md, references/Scenario_Atlas.md and references/Ask_Carriers.md, write task_inputs/Working_Files/01_Scenario_Design.md and the draft task_inputs/Working_Files/01_Hardness_Manifest.json (format: references/Hardness_Manifest_Spec.md). Design only — no prompt, Oracle Event or criterion text. Paste the persona census from python3 Task_Authoring/tools/persona_view.py reach <persona>; build the storyline, coherence audit, active speakers and traps on references/universe_kb/ (timeline, cohorts, coherence_hazards, activity, trap_catalog, integrations) and python3 Task_Authoring/tools/entity.py collisions. Run python3 Task_Authoring/tools/hardness_gate.py Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.json --design until it passes, do the lazy-solver pass, and run tools/redteam_review.py --mode redteam --dual. Write only under Task_Authoring/. Before handoff run python3 Task_Authoring/tools/stage_gate.py scenario Task_Authoring/task_inputs --paste and fix the artifact until it prints STAGE GATE scenario: PASS.
```

## 1 · Universe injection · `/create-injection`

```
Read Task_Authoring/setup/GEN_EXECUTION.md, then follow Task_Authoring/playbooks/01_Universe_Injection.md in full. Implement task_inputs/Working_Files/01_Scenario_Design.md and its manifest: write task_inputs/01_Universe_Inject.sql, task_inputs/Working_Files/01_Grounding_Dossier.md (including "Facts for the human") and the final task_inputs/Working_Files/01_Hardness_Manifest.json with every planned id replaced by the minted id. Ground everything through Task_Authoring/tools/hg.py search, prove persona reach and findability, seed speakers, text and companions by references/universe_kb/activity.json, conventions.json and integrations.json, declare every load-bearing fact in the manifest's facts, then run sql_lint.py, base_check.py, fact_check.py, persona_view.py check-sql --load-bearing, hardness_gate.py and python3 Task_Authoring/tools/hg.py lint on the manifest + SQL until all pass. Never execute SQL; write only under Task_Authoring/. Before handoff run python3 Task_Authoring/tools/stage_gate.py injection Task_Authoring/task_inputs --paste and fix the artifact until it prints STAGE GATE injection: PASS.
```

## 2 · Error / async friction (optional) · `/create-error-async`

```
Read Task_Authoring/setup/GEN_EXECUTION.md, then follow Task_Authoring/playbooks/03_Error_Async_Config.md. Decide whether friction deepens this task; if so, configure it from the selectable functions, prove the alternate path for every errored function, and record the discovery each async wait depends on. Write task_inputs/03_Error_Async_Config.txt (or the empty config with "Friction: none"). Before handoff run python3 Task_Authoring/tools/stage_gate.py error-async Task_Authoring/task_inputs --paste and fix the artifact until it prints STAGE GATE error-async: PASS.
```

## 3 · Reference files (optional) · `/create-reference-files`

```
Read Task_Authoring/setup/GEN_EXECUTION.md, then follow Task_Authoring/playbooks/02_Reference_Files.md. Only if the scenario genuinely needs an attachment, build task_inputs/02_Reference_Files/ and task_inputs/Working_Files/02_Reference_Files_Manifest.md (outside the folder), mirroring native records from Task_Authoring/references/Native_Artifact_Anatomy.md and citing every fact. Before handoff run python3 Task_Authoring/tools/stage_gate.py reference-files Task_Authoring/task_inputs --paste and fix the artifact until it prints STAGE GATE reference-files: PASS.
```

## 4 · Prompt writing (prep: fact brief) · `/create-prompt-writing`

```
Read Task_Authoring/setup/GEN_EXECUTION.md, then follow brief mode in Task_Authoring/playbooks/04_Prompt_Writing.md. Write task_inputs/Working_Files/04_Prompt_Writing_Brief.md from the assignment, the dossier and the universe. It holds facts, locators and requirements. Before handoff run python3 Task_Authoring/tools/stage_gate.py prompt-writing Task_Authoring/task_inputs --paste and fix the artifact until it prints STAGE GATE prompt-writing: PASS.
```

Then draft `task_inputs/04_Prompt.txt` (ask Claude or Codex: follow draft mode in `playbooks/04_Prompt_Writing.md`) or write it yourself.

## 5 · Prompt check · `/create-prompt-writing check`

```
Read Task_Authoring/setup/GEN_EXECUTION.md, then follow check mode in Task_Authoring/playbooks/04_Prompt_Writing.md. Check task_inputs/04_Prompt.txt against task_inputs/Working_Files/04_Prompt_Writing_Brief.md and the universe, and write task_inputs/Working_Files/04_Prompt_Check.md. Quote spans, name rules and severities, and suggest wording where it helps; check clean spelling, ordinary assigned-role wording, no trap hints/riddles and all fair alternatives; update role/outcome reviews in the V3 sidecar. Before handoff run python3 Task_Authoring/tools/stage_gate.py prompt-check Task_Authoring/task_inputs --paste and fix the artifact until it prints STAGE GATE prompt-check: PASS.
```

## 6 · Human time · `/create-humantime`

```
Read Task_Authoring/setup/GEN_EXECUTION.md, then follow Task_Authoring/playbooks/05_Human_Time_Estimate.md. Build task_inputs/Working_Files/05_Human_Time_Worksheet.md: manual sub-tasks with measured volumes, dead ends and workarounds, durations that add up to the hours figure, and a breakdown that fits 50–2,000 characters. Before handoff run python3 Task_Authoring/tools/stage_gate.py humantime Task_Authoring/task_inputs --paste and fix the artifact until it prints STAGE GATE humantime: PASS.
```

## 7 · Oracle Event writing (prep: fact ledger) · `/create-oe-writing`

```
Read Task_Authoring/setup/GEN_EXECUTION.md, then follow prep mode in Task_Authoring/playbooks/08_Oracle_Event_Writing.md. From task_inputs/04_Prompt.txt, the dossier and the universe, write task_inputs/Working_Files/08_OE_Writing_Ledger.md: requirements traced to the prompt, verified facts with locators and expected data, persona visibility proof, write capability, friction facts, traps and open risks. No event text, no step sequence, no agent-voice sentences. Before handoff run python3 Task_Authoring/tools/stage_gate.py oe-writing Task_Authoring/task_inputs --paste and fix the artifact until it prints STAGE GATE oe-writing: PASS.
```

Then draft `task_inputs/08_Oracle_Events.md` (ask Claude or Codex: follow draft mode in `playbooks/08_Oracle_Event_Writing.md`) or write it yourself, and type the events on the platform.

## 8 · OE check · `/create-oe-writing check`

```
Read Task_Authoring/setup/GEN_EXECUTION.md, then follow check mode in Task_Authoring/playbooks/08_Oracle_Event_Writing.md. Check task_inputs/08_Oracle_Events.md against the ledger and the universe for completeness and accuracy, non-actions and final-response content, and write task_inputs/Working_Files/08_OE_Check.md. Quote spans and name rules; corrected event text may be proposed. Before handoff run python3 Task_Authoring/tools/stage_gate.py oe-check Task_Authoring/task_inputs --paste and fix the artifact until it prints STAGE GATE oe-check: PASS.
```

## 9 · Rubric writing (prep: coverage plan) · `/create-rubric-writing`

```
Read Task_Authoring/setup/GEN_EXECUTION.md, then follow prep mode in Task_Authoring/playbooks/09_Rubric_Writing.md. From the prompt, the Oracle Events, the ledger and the hardness manifest, write task_inputs/Working_Files/09_Rubric_Writing_Plan.md: what must be graded, the final state that proves it, the values a title-only self-contained criterion must name, Outcome vs Process test, kind of work and weight band, the chain/authority/trap that decides each row, predicted all-fail risks (tolerance 0), failure diversity per unit of discovery, a volume row per sampled output plus direct exception rows (no bundled exact-set row), and the title/distractor/ambiguity flags. Run python3 Task_Authoring/tools/shortcut_probe.py <persona> Task_Authoring/task_inputs/Working_Files/09_Rubric_Writing_Plan.md, paste its output under §F and disposition every hit with SHORTCUT-OK: <service> <record> — <reason> (or route the shortcut to the universe). Record each criterion's stable fact ID, exact prompt span, actual source value/discovery path, accepted alternatives and Pacific/UTC date acceptance in the V3 sidecar (Guide schema). No criterion text. Before handoff run python3 Task_Authoring/tools/stage_gate.py rubric-writing Task_Authoring/task_inputs --paste and fix the artifact until it prints STAGE GATE rubric-writing: PASS.
```

Then draft the criteria (ask Claude or Codex: follow draft mode in `playbooks/09_Rubric_Writing.md`) or write them yourself, enter them in the Rubric Criteria Builder and export `task_inputs/09_Rubrics.json`.

## 10 · Rubric check · `/create-rubric-writing check`

```
Read Task_Authoring/setup/GEN_EXECUTION.md, then follow check mode in Task_Authoring/playbooks/09_Rubric_Writing.md. Lint task_inputs/09_Rubrics.json with python3 Task_Authoring/tools/hg.py rubric-lint task_inputs/09_Rubrics.json against the plan, the V3 fair-reading/source/date/duplicate rules plus unchanged V2/Evals checks (Evals/3_Rubrics_Eval.md), tally against the thresholds (any incorrect, unauthorized, unobservable, contradictory, missing-coverage or predicted all-fail item blocks on its own, whatever the tally), and write task_inputs/Working_Files/09_Rubric_Check.md. Quote spans and name rules; update current sidecar hashes and per-row evidence. Correct unfair rows and re-grade before assessing the assigned mode cap; replacement wording may be proposed. Before handoff run python3 Task_Authoring/tools/stage_gate.py rubric-check Task_Authoring/task_inputs --paste and fix the artifact until it prints STAGE GATE rubric-check: PASS.
```

## 11 · All-fail analysis · `/create-allfail`

```
Read Task_Authoring/setup/GEN_EXECUTION.md, then follow Task_Authoring/playbooks/11_AllFail_Analysis.md. From task_inputs/10_Baseline_Verifier_Results.md, the six trajectories and task_inputs/09_Rubrics.json, find every rubric failed by all completed rollouts, decide valid vs invalid with trajectory evidence, draft 1–2 line justifications for valid ones and report invalid ones without rewriting them. Write task_inputs/11_AF_Justification.md. Before handoff run python3 Task_Authoring/tools/stage_gate.py allfail Task_Authoring/task_inputs --paste and fix the artifact until it prints STAGE GATE allfail: PASS.
```

## 12 · Difficulty · `/create-difficulty`

```
Read Task_Authoring/setup/GEN_EXECUTION.md, then follow Task_Authoring/playbooks/12_Difficulty.md. Build task_inputs/Working_Files/12_difficulty_input.json from the verifier results and trajectories, run python3 Task_Authoring/tools/difficulty_stats.py on it, check that any friction fired, and write task_inputs/Working_Files/12_Difficulty_Stats.txt with the gate table and routing. Before handoff run python3 Task_Authoring/tools/stage_gate.py difficulty Task_Authoring/task_inputs --paste and fix the artifact until it prints STAGE GATE difficulty: PASS.
```

## 13 · Release gate (final step before submit)

```
python3 Task_Authoring/tools/stage_gate.py release Task_Authoring/task_inputs --paste
```

It writes `task_inputs/Working_Files/13_Release_Gate.txt` and blocks unless every stage certificate is present and current, one bundle digest (prompt, OEs, rubric JSON, SQL, reference files, error/async config, manifest, assignment + persona) matches every digest a stage recorded, no PROVISIONAL / UNRESOLVED / UNVERIFIED marker remains, the OE check says Task solvability SUPPORTED_BY_OE, the difficulty gates pass and `06_PreCheck_Trajectory/trajectory.json` exists. Fix the owning stage and re-run; submit only on PASS.

## Advanced · Hardening · `/create-hardening`

```
Read Task_Authoring/setup/GEN_EXECUTION.md, then follow Task_Authoring/playbooks/01a_Hardening.md. Choose MODE A (no runs) or MODE B (pre-check or baseline present) from what exists. Write task_inputs/Working_Files/01a_Hardening_Report.md; harden the SQL, dossier and manifest for universe-side fixes and re-pass sql_lint.py and hardness_gate.py; report prompt-side defects for the human and route them to the prompt stage. Before handoff run python3 Task_Authoring/tools/stage_gate.py hardening Task_Authoring/task_inputs --paste and fix the artifact until it prints STAGE GATE hardening: PASS.
```
