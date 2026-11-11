# Calvin Price: Queue Manager ticket turned into an epic (submitted 2026-11-11)

| Field | Value |
|---|---|
| Persona | Calvin Price (Game Engineer, Unity VFX) |
| Horizon | Long Horizon |
| Assignment | Engineering / Engineering Ops / Analysis and synthesis |
| Difficulty mode | hard (cap: average under 70%) |
| Universe | Oct 1, 2025 (synth-cut, freeze 2025-10-01T00:00:00Z, clock 07:00 UTC) |
| Requester targets | more than 130 counted calls in every run; average under 70% (aim 65%); largest failure pattern at most 50% |

**`task_inputs/`** is the full slot folder as submitted, diff-verified against the original (49 MB). Notes on what it holds:
- `06_PreCheck_Trajectory/trajectory.json` is the rev2 pre-check (it is byte-identical to `Working_Files/run_forensics/rev2/precheck_trajectory.json`). The rev3b pre-check trajectory was not saved locally.
- `07_Baseline_Trajectories/` holds six runs; `Run1_trajectory.json` at the top level is a separate export and differs from `trajectory-run-1.json`.
- `Working_Files/run_forensics/` holds the SQL of rev1, rev2 and rev3, the rev1 pre-check forensics, the rev2 runs, and the rev3 baseline and rubric builds.
- `Working_Files/12_difficulty_input.json` and `12_Verifier_Binding_Receipt.json` exist; `12_Difficulty_Stats.txt` was never written (`/create-difficulty` was not finished).
- The portal proof table in `00_Assigments.md` was left blank.

**`eval_reports/`** holds every platform report, named by stage, verdict and revision or round:

| File | What it reviewed |
|---|---|
| `0_injection_PASS_rev1.md`, `_rev2.md`, `_rev3.md`, `_rev3b.md` | every revision passed |
| `1_prompt_PASS_rev1.md`, `_rev2.md`, `1_prompt_NONFAIL_rev3.md`, `1_prompt_PASS_rev3b.md` | rev3 was NON-FAIL 3 (an invented diff hunk on a seeded review comment); the rest PASS 5 |
| `1a_hardness_FAIL2_rev1.md`, `1a_hardness_NONFAIL_rev2.md`, `1a_hardness_NONFAIL4_rev3b.md` | FAIL 2, NON-FAIL 3, NON-FAIL 4 |
| `2_oe_PASS_rev3b.md` | the 104-event set, passed first time |
| `3_rubric_FAIL_r1.md`, `3_rubric_FAIL_r2.md`, `3_rubric_PASS_r3.md` | the 121-row first draft afbc830d0cbb, then f03edcef1022 (184 rows), then b19500a5cc7b |

**`work/calvin_qm_epic/`** holds copies of the builders from `task_inputs/Working_Files/plan/`, plus the solver and the blind sweeps:
- **Scenario and SQL:** `reports.py` (the 39-report truth), `build_scenario.py`, `assemble_design.py`, `build_reviews.py`, `build_sql.py`, `build_final_manifest.py`, `write_dispositions.py`, `assemble_dossier.py`, `build_reviews_inj.py`, `policy_model.py`, and the `run_*.sh` wrappers.
- **Hardening:** `build_hardening.py`, `build_hardening_report.py`.
- **Brief, prompt check, human time:** `build_brief.py`, `build_reviews_brief.py`, `build_prompt_check.py`, `measure_humantime.py`, `build_humantime.py`.
- **OEs:** `oe_reads.py`, `oe_defer.py`, `assemble_oe_ledger.py`, `assemble_oe_events.py`, `assemble_oe_check.py`.
- **Rubric:** `apply_fixlist.py` (parses the /rubric Fix List out of the report), `rubric_final.json`, `rubric_rows.py` (a loader), `assemble_rubric_draft.py`, `assemble_rubric_plan.py`, `build_rubric_extra.py`, `assemble_rubric_check.py`, `build_reviews_rubric.py`, `shortcut_ok.txt`.
- **Baselines and all-fail:** `baseline_extract.py`, `baseline_grade.py`, `build_allfail.py`.
- **`sweeps/`:** the blind fork and coherence sweeps for each revision, two OE blind reviews and one rubric blind review.
- **`solver/`:** `solver.py` and `truth.json`.

Older builder versions (`*.v1`, `*.rev1`, `*.rev2`) stay in `task_inputs/Working_Files/plan/out/`.

## Final state
- **Injection SQL:** sha256 479b8441f52e (rev3b). Friction: none. No reference files. /injection passed on every revision.
- **Prompt:** sha256 edefd55c0ff5, 80 words, unchanged from rev1 to rev3b. It asks for Brian's set-up of the Queue Manager ticket (ZOM-543) as an epic before Thursday's flow review:
  - the children and report lines in Linear;
  - the stock-take sheet in Calvin's ZM queue manager folder, shared with everyone on the review invite;
  - a slide with the numbers in his queue manager deck;
  - a message to Brian in their DM with the numbers he wants back.
- **/prompt:** PASS 5 on rev1, rev2 and rev3b; NON-FAIL 3 on rev3.
- **/hardness:**
  - FAIL 2 on rev1 (172 calls; Brian's note spelled every resolver as a check, so all 8 rules leaked);
  - NON-FAIL 3 on rev2 (170 calls);
  - NON-FAIL 4 on rev3b (167 calls).
- **Oracle Events:** 104 events, 40,144 characters, local sha256 376b94e7eaa9. /oe PASS on the first round.
- **Rubric:** 184 rows (183 Outcome, 1 Process), weight 592 (5 ×85, 3 ×34, 1 ×65), sha256 b19500a5cc7b.
  - **Round 1, FAIL 1** on the 121-row first draft: count rows over separate writes were non-atomic, and 65 outcomes were missing (note reasons, moves, sub-issue parents and titles, child states). The Fix List was applied by script.
  - **Round 2, FAIL 1** on two items: 8 state rows whose evidence Reject clause re-added a condition the new title had dropped, and one weight (3 → 5).
  - **Round 3, PASS 5** on every dimension.
- **Baselines** (rev3b, verifier on b19500a5cc7b, 6 of 6 completed):

  | | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Run 6 |
  |---|---|---|---|---|---|---|
  | Rows passed (of 184) | 134 | 160 | 137 | 143 | 133 | 143 |
  | Weighted pass | 57.8% | 79.7% | 60.3% | 65.4% | 57.6% | 65.4% |
  | Counted calls | 138 | 189 | 140 | 153 | 138 | 147 |

  - Average 64.4%, under the hard cap of 70%. No full passes; 0 errored.
  - SD 0.076 (population), computed here from `12_difficulty_input.json`; the local difficulty stats file was not produced, so no gate verdict is recorded.
  - Failure signatures: five distinct, the largest shared by 2 of 6 runs (runs 4 and 6).
  - Average calls: 151; every run over 130.
- **All-fail:** 24 rows, all marked valid (`11_Baseline_AllFail_Justifications.md`). They are the rows that depend on the pull-request review comments and Oliver's comment.
- **Human time:** 19.25 h, in `Working_Files/05_Human_Time_Worksheet.md`.

## Key answers
- **Population:** 39 reports: Vincent's 38-row flow pass sheet plus Marcus's DM report.
- **Statuses:** 10 Passed, 9 Waiting on QA, 20 Waiting on a fix. 0 clear areas, 7 on the review list.
- **Linear:** 10 area children under ZOM-543; 22 existing tickets and 17 new ones; 8 state changes; a note with status and reason on each moved ticket.
- **What decides the hard rows:**
  - Arthur's inline review comments on #472 and #475 say the fix is not in the diff (rows 12, 15, 32 → Waiting on a fix, Todo).
  - Oliver's comment on merged #473 lists four fixes (rows 13, 14, 37, 38 → Waiting on QA, In Validation).
  - The #472 body carries row 6 in a parenthetical.
  - Two thread replies reopen passes (rows 9 and 29), under Arthur's rule that a pass stands until the bug is seen again on a later main build.
  - Later dev notes on ZOM-585 and ZOM-586 say rows 17 and 24 came back on Submission 135.
  - Controls that stay as they are: the branch-build "ok" (iOS Internal #1718), the sighting on an older build (Android #2006, row 27 stays Passed), and the "again" timing against the #472 merge.

## Lessons carried forward
- **Pull-request review comments and issue comments are a reliable miss for Opus 5.5, but an identical one.** All six runs (and both later pre-checks) read #472, #473 and #475 only as merged PRs named in the sheet's Fix column. That gives a low average and no spread, so pair it with traps that runs catch at different rates.
- **Mixed-rate carriers gave the spread:** thread replies were missed by 3 of 6 runs, Linear notes on the report's own ticket by 5 of 6, the PR body by 2 of 6.
- **Misses must not cancel in the headline numbers.** On rev2 two swaps cancelled, so every run still reported the right totals and scored about 79%. rev3 made each miss move a count.
- **A note that spells each resolver as a check leaks every rule** (rev1, FAIL 2). Keep the hand-over note to plain definitions and let facts settle the rows.
- **A seeded review comment's `diff_hunk` and path must be real lines of that PR's merge diff.** /prompt's deep recheck diffs the repo (rev3, NON-FAIL 3).
- **Check the reviewed SHA before acting on a /rubric report.** Round 1 reviewed the first draft, not the blind-fixed one.
- **When a Fix List retitles a row, rewrite its evidence Reject clause too,** so it says nothing the new title does not (round 2).
- **Per-target rows tripled the rubric** (121 → 184 rows) without moving the average much here (63.4% simulated before, 64.4% after), because the trap rows were split along with the easy ones.
