---
name: create-goal
description: "Build the copy-ready /goal for a fresh session that starts a HarmonyGames task before /create-scenario. Reads one task folder's assignment through task_context.py (no --write), the other task folders, the learnings file and the Evals input store (read-only), and prints a short goal tailored to the persona, business function, competency, task skill, horizon, difficulty mode and universe date; the fresh session then writes Working_Files/00_Pre_Scenario_Analysis.md and stops before /create-scenario. Use /create-goal <task folder> right after the assignment is pasted. Writes only <task>/Working_Files/00_Session_Goal.md; no stage gate."
---

# Session goal (before /create-scenario)

Resolve this file through any symlink to locate `<bundle>/skills/<name>/SKILL.md`.
The bundle's parent is the workspace. Read `<bundle>/setup/GEN_EXECUTION.md` § 0a (task date and universe) and § 1
(write boundary). Write only `<task>/Working_Files/00_Session_Goal.md`. Never write to `Evals/`, `claude/`, the
universe folders or another task folder, never edit `Task_Authoring/tools/`, and never execute SQL.

This command prepares a session; it designs, grounds and certifies nothing. The goal names no storyline, trap or
answer: the fresh session finds those.

## Exceptions to the bundle's flow (deliberate)

- **No `task_context.py --write`.** The generator recomputes the context read-only (`task_context.py --task-dir <dir>
  --require-source`), so a folder another session is using is never rewritten. The goal tells the fresh session to run
  `--write --require-source` before grounding.
- **No stage gate.** `stage_gate.py` has no goal stage. Adding one, or any file under `Task_Authoring/tools/`, would
  change the gate-policy digest that every task's pasted PASS blocks carry (`tools/stage_gate.py` `virtual_digests`).
  The generator runs its own self-checks instead.
- **Evals input store: read, never written.** `hg_store_input.py list` runs with bytecode off, only to warn when the
  store holds another task or date. The task date always comes from the assignment (GEN_EXECUTION § 0a), never from
  the store; eval intake stays with the user.

## Inputs

1. The task folder, from the user's message (`/create-goal Task_Authoring/<folder>`). If none is given and
   `TASK_AUTHORING_TASK_DIR` is unset, run `--list` and ask which folder; never guess.
2. Its `00_Assigments.md` with all eight V3 fields. A missing date or a roster mismatch stops the run (exit 2); there is
   no default date.
3. Any standing decisions the user states for the new session (for example "skip red team and methodology; record the
   waiver"): pass each verbatim with `--note`.

## Run

```sh
python3 -B Task_Authoring/skills/create-goal/scripts/build_goal.py --task-dir <task folder> [--note "<decision>"]...
python3 -B Task_Authoring/skills/create-goal/scripts/build_goal.py --list
```

Before writing, check the folder's `Working_Files/` for files you did not expect (research notes, drafts): if another
session is already working there, add `--stdout-only`, which prints the goal and writes nothing. The script also
reports such files as a `WARN` line.

The goal is tailored from records only: the eight fields, the persona's "today" and weekday, the difficulty gate and
the design target for the mode (cap − 8), the call floor and the volume decision for the horizon, the task-skill UGT
line and the function and competency fit line (`goal_rules.json`), the `TASK_AUTHORING_TASK_DIR` line when the folder
is not `Task_Authoring/task_inputs`, the Evals-store line unless the store holds this task with an intact file on this
date, up to three same-universe sibling designs to stay distinct from (same competency first; folders with no design
have no storyline yet and are not named), the closest existing pre-scenario analysis and the learnings section range.

## Hardness guide

`Task_Authoring/references/Docs/13_Hardness_V2_Opus55.md` is the platform's Opus 5.5 hardness guide (46 tasks, 270
runs), kept verbatim. Its trap types and its Part 7 checks enter the goal's hardness rule and the analysis deliverable.
Four of its rules are adapted to the gates here (plan § 12):

- **Weight 5 follows the work.** The guide says to put weight 5 on trap rows and to raise a weight if a miss flips
  none. `Evals/3_Rubrics_Eval.md` § 2.12 weights the work of the atomic result, never its importance. So each miss must
  flip a row that is multi-source work, and no weight is raised to make a trap count.
- **Identical runs fail.** Every worked example is a 6/6 miss. If every run fails the same rows, the
  failure-signature rule (≥ 2 signatures, none over half; QC spec) and the SD band (0.1–0.3) fail. The goal therefore
  asks for traps of different findability.
- **No do-nothing rows.** Trap 9 grades that the agent "leaves those items alone", and Part 6 adds a guard row for an
  item left unchanged. `Evals/3_Rubrics_Eval.md` § 2.9 fails any row an agent passes by doing nothing, so the goal
  says no row may pass that way: grade the positive result that leaves the item out.
- **Types, not examples.** The worked examples are real tasks that use this universe's people and channels (one turns
  on a ticket comment from Leonard, another on rules in #executives), so the goal points at the trap types only.

The guide's lines are required like any other: if the file is renamed, moved or loses a cited phrase, the run stops
with exit 3. Update the paths and phrases in `goal_rules.json`, and re-read the four adaptations against the new text.

## Exit codes

| Code | Meaning | Then |
|---|---|---|
| 0 | PASS | deliver |
| 2 | the assignment or the universe source is not usable | report the tool's message; the user fixes `00_Assigments.md` or installs the universe |
| 3 | a required line's cited phrase is missing from its source, or the function, competency or skill has no entry | report it; update `goal_rules.json` and re-read the wording against the source |
| 4 | the task already has a scenario design | report the stage it reached; `/create-goal` only starts a task before `/create-scenario` |
| 5 | the goal failed a self-check (the draft is printed to stderr) | fix the input or `goal_rules.json`; never hand-edit the goal past a check |
| 6 | the task folder or the output path is not usable, the goal file cannot be written, or a `--note` is blank | report it; nothing is left half-written |

## Self-checks (built in)

Words (tokens with a letter or digit; a path is one word): the generated text fails above 560, and the whole goal,
`--note` text included, warns above 520. No unresolved template field or other brace token; no pronoun for the
persona; every input path the goal names exists; the analysis output stays inside the task folder; the
`TASK_AUTHORING_TASK_DIR` line, the store line and the volume decision appear exactly when their condition holds; the
folder never lists itself as a sibling.

The citation check proves only that each cited phrase still exists in its source, not that the rule is still right.
Whenever `goal_rules.json` or one of its sources changes, re-read the affected lines against the source; a substantive
wording change gets an independent review (`Task_Authoring/plans/Create_Goal_Skill_Plan_2026-11-01.md` § 11–13).

## Deliver

1. The goal in one copy-ready code block, exactly as printed.
2. Up to five lines: the output path (or "stdout only"); what was tailored (non-default folder, store state, siblings
   named, analysis cited, hardness guide used); the word count and any `WARN` line.
3. Next step for the user: open a fresh session at the workspace root and paste the goal. It writes
   `Working_Files/00_Pre_Scenario_Analysis.md`, lists the decisions it needs and stops. Take the decisions, then run
   `/create-scenario` in that session.

The goal is for the authoring session only. None of its rules or wording belongs in the task's `04_Prompt.txt`.
