# Rubric flow v2 (rubric-flow-v2)

Goal: run 1 gives the contributor ALL feedback with a fix for every issue; the
contributor fixes once; run 2 confirms. The grading rules, thresholds and Local
Overrides in `3_Rubrics_Eval.md` are unchanged. Only the run flow changes.

## Step A: plan the run (right after intake)

1. If the contributor gives a reason for dismissing a previous finding ("R12 is
   atomic because …"), record it before planning:
   `python3 Evals/tools/hg_rubric_ledger.py dismiss <previous row number> "<reason>"`.
2. If the contributor supplies a `rubric_ledger.json` from another workspace
   (Slack bot ↔ sandbox), save it as `extra:rubric-ledger` and add
   `--ledger <saved path>` to the plan command.
3. Run `python3 Evals/tools/hg_rubric_ledger.py plan`. It prints the mode:

| Mode | When | What to do |
|---|---|---|
| `FULL` | No ledger in this workspace, or the prompt, OE, injection SQL or task details changed | Run 1 below |
| `DELTA` | Same task context; some rows edited, added, removed or previously flagged | Run 2 below |
| `UNCHANGED` | Rubric and task context are byte-identical to the last run | Do not re-review. Say so, restate the previous verdict from the existing report, and stop |

Never choose the mode yourself; use the plan output. `--force-full` is only for an
explicit user request.

## Code checks (both modes, before any reviewer)

Run `python3 Evals/tools/hg_rubric_lint.py` on the saved rubric. Every
`vague_exemplar`, `tool_name`, `schema` and `prohibition_title` hit is a finding
you must record (code does not miss word-list defects, so reviewers need not hunt
for them); `markdown_artifact` and `whitespace` hits are non-failing repairs.
Run it again on every candidate fix (see "Fixes").

## Run 1 (FULL): find everything, with a fix for every issue

1. **Start two independent full reviewers now.** Right after the plan, start
   reviewers F2 and F3 at the same time as background subagents on this skill's
   model. Give each only what a deep-recheck pass gets (`deep_recheck.md`, "Pass
   inputs"), plus `Evals/3_Rubrics_Eval.md`, `Evals/references/rules/rubric_checks.md`,
   `rubric_factual_checks.md`, `rubric_sampling.md`, `rubric_qc_examples.md`, this
   file and `Evals/Docs`. Never give them `Evals/task_inputs/reports/`, your record
   or your findings. Tell each:

   > You are reviewer F<n>, one of three independent full reviewers of this rubric.
   > Apply every check in Phases 1.2–3.7 and 5.1 of `Evals/3_Rubrics_Eval.md`,
   > including the Local Overrides table, the weight rules (QC work-kind
   > definition), the Rubric Writing §8 sampling limits and the scope checklist in
   > `rubric_flow_v2.md`, to every row and to the whole set. Verify facts against
   > the universe with `Evals/tools/hg_search.py`. Your job is completeness:
   > return EVERY issue that has evidence, however small, in one list. Do not save
   > any file, never open `Evals/task_inputs/reports/`, never execute SQL. One line
   > per finding:
   > `F<n>-<k> | row(s) | issue type (Phase 4 tally name) | severity | quoted row text | record path, id and quoted value, or the quoted rule | why it is a defect | suggested fix`.
   > For a weight disagreement give the expected weight and the reference row or
   > work kind. Put anything you suspect but cannot support with evidence on a
   > separate `UNSURE` line. If you find nothing, return `none` and the number of
   > rows checked.

2. **Do your own review (reviewer F1)** through Phase 5.2 as usual, including the
   code checks and the scope checklist below, and save `rubric-score`.
3. **Start R1–R7** (Phase 5.5, `deep_recheck.md`) at the same time. Wait until F2,
   F3 and R1–R7 have all returned. Restart any reviewer that crashes or returns no
   usable list, until it returns one. Never end your turn while a reviewer is
   still running.
4. **Combine every finding into one list. Do not vote.**
   - Merge duplicates: the same row(s) and the same defect, however worded, become
     one entry that lists every reviewer who raised it (for example `F1, F3, R7`).
   - Check each merged finding's evidence by opening the record or rule it cites.
     Reject a finding **only** when (a) the cited record or quote does not exist or
     does not say what the finding claims, (b) it contradicts an explicit QC spec
     rule or Local Override (quote that rule), or (c) it is a duplicate. Disagreeing
     with another reviewer's judgment is not a reason to reject: a finding with a
     concrete quoted basis is accepted. Remember that "Agent …" and "The Agent …"
     titles are both standard.
   - Conflicting findings (one says split R12, another says R12 and R13 overlap):
     decide with the rule or source that settles it (quote it), record the side you
     did not take and why, and give one fix.
   - Add every accepted finding to the scoring record as `issues`,
     `weight_reviews` changes or `predicted_all_fail` entries, save `rubric-score`
     again and let the helper recompute the verdict.
   - Unsupported `UNSURE` items go to `### Worth a look (not scored)`.
5. **Fixes:** follow "Fixes" below for every accepted finding.
6. **Report.** Directly under the report header, add `## Fix List`: one line per
   row to change, in row order: the row, what is wrong in plain words, the fix to
   copy, and its mark (`checked` or `revised after check`). This is what the
   contributor works from; keep it short. Before `## Deep Recheck`, add `## All Findings`: every accepted
   finding grouped by row, each with severity, the reviewers who raised it, the
   evidence and its fix. Then `### Worth a look (not scored)`, then
   `### Rejected findings`, one line each with the reason. `## Deep Recheck` and
   its verdict block stay last.
7. **Save the ledger** with the checked fixes, so run 2 locks them:
   `python3 Evals/tools/hg_rubric_ledger.py write --mode FULL`. It reads
   `fixcheck/rubric_candidate.json` and `fixcheck/fix_status.json` and stops with an
   error if any changed candidate row has no mark.

## Scope checklist (run 1, and run 2 for changed rows)

For every kind of write the prompt or an incorporated instruction asks for
(state changes such as Done or Canceled, reassignment, comments, messages, file
or page writes), confirm the rubric has:
- a row that grades the required targets (directly or by spot checks plus a
  volume row); and
- a row that fails a run doing that write to the wrong targets: out-of-scope
  tickets or records, decoys, other people's items, or extra targets (an exact
  count or scope row usually covers this).

A missing guard is `missing_coverage`. Work through every write kind one by one
and record the result in the requirement ledger; do not rely on a reviewer
noticing.

## Fixes (run 1 and run 2)

Give a fix for every accepted finding; "no fix" is not allowed. A fix may change
as much as it needs to be correct (reword, redesign, split, merge or add rows).

1. **Draft each fix** so it is correct against the data and the prompt, follows
   every rule (title-only self-containment, atomicity including quantifier-compressed
   "every / each / all" titles, overly specific and overly broad, Agent-centric and
   negative-criteria rules, sampling limits, correct QC work-kind weight), and is
   non-regressing (everything the old row covered stays covered; valid answers
   still pass and wrong ones still fail; no new duplicate, overlap or cascade with
   any row; related weights stay consistent). If reviewers disagreed on the
   finding, pick the side the rules support and say why.
2. **Write the candidate rubric**: the current rubric with every fix applied, in
   the same schema, at `Evals/task_inputs/fixcheck/rubric_candidate.json`. List
   what changed with
   `python3 Evals/tools/hg_rubric_ledger.py diff --candidate Evals/task_inputs/fixcheck/rubric_candidate.json`.
3. **Check the fixes once:** run `hg_rubric_lint.py` on the candidate, self-check
   each changed or new row against step 1, and start R1–R7 once, at the same time,
   on the candidate's changed and new rows (R4 against all rows, R3 whole-rubric
   coverage). Give them only the candidate path and the usual pass inputs.
4. **Mark the result.** A fix with no confirmed finding and no lint hit is
   `(checked)`. A fix that drew one: revise it, re-run lint and the self-check on
   it, and mark it `(revised after check)`; it is not locked in the next run, so the
   next run reviews it. Write the marks to `Evals/task_inputs/fixcheck/fix_status.json`
   as `{"rows": {"<candidate row number>": "checked" | "revised"}}` with an entry for
   every changed and new candidate row; the ledger reads it, so no checked fix is
   missed.
5. In `### Recommended Fixes`, give each fix with its mark and the checks it
   passed.

## Run 2 (DELTA): confirm

Read `Evals/task_inputs/reports/drafts/rubric_delta_plan.json` (every row's
status) and `rubric_delta_carry.json` (locked rows' previous check entries).

1. **Locked rows**: `LOCKED` (passed last run, unchanged) and `LOCKED_CHECKED_FIX`
   (the contributor copied a `(checked)` fix exactly).
   - Copy `LOCKED` rows' `check_rows` and `weight_reviews` from the carry file
     unchanged. For `LOCKED_CHECKED_FIX` rows, write their check entries with a
     fact review only.
   - They fail **only** on a provable factual error: a wrong ticket, number, date,
     name or other value contradicted by a quoted record. Record that as an issue.
   - Anything else you or a reviewer notice on a locked row (atomicity, breadth,
     wording, weight, overlap between locked rows) goes under
     `### Notes for QM (not scored)` with its evidence. It does not change the
     score.
2. **Target rows** (`EDITED`, `NEW`, `RECHECK_FLAGGED`), i.e. rows the
   contributor wrote or changed themselves: full per-row review (Phases 2.1–2.12)
   with fact review and the code checks. These can fail.
   - For each previous finding on a target row, say whether it is fixed.
   - For a recorded dismissal, judge the reason against the QC spec and Local
     Overrides: accept it (the finding closes) or reject it, quoting the rule.
3. **Whole-set checks a change can affect.** Run coverage, the scope checklist,
   duplicates, overlap and cascades, weight consistency, sampling caps and
   contradictions over the full rubric, but score a finding only when it involves
   a target row or a removed row. A coverage gap that no change caused goes to
   `### Notes for QM` unless the prompt states that requirement outright.
4. **Deep recheck on target rows only.** Start R1–R7 at once on the target rows;
   R4 compares them against all rows. Apply step 1 to anything they raise on
   locked rows. F2 and F3 do not run.
5. **Fixes** for scored findings, as in "Fixes".
6. **Report.** Directly under the report header, add `## Fix List` for the scored
   findings (same format as run 1), or "No changes needed" when there are none.
   Before `## Deep Recheck`, add `## Changes Since Last Run`: counts of
   locked, locked-checked-fix, edited, new, re-checked and removed rows; previous
   findings now fixed; dismissals accepted or rejected; new scored findings; then
   `### Notes for QM (not scored)`.
7. **Save the ledger:**
   `python3 Evals/tools/hg_rubric_ledger.py write --mode DELTA --keep-checked`
   (it also picks up this run's new checked fixes from `fix_status.json`).

## What does not change

Every Local Override, threshold and gate in `3_Rubrics_Eval.md`, the schema and
fact checks, and "evaluate this version only; never revise criteria or retry
until PASS".
