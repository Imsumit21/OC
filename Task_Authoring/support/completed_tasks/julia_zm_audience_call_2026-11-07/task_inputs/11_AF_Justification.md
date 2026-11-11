# 11 All-Fail Rubric Analysis — Julia Lawson ZM audience read (SQL rev9)

Completed rollouts: 6/6 (excluded: none; no errored export)   Rubric binding: ok (all 108 rows of each "Run #N" block in 10_Baseline_Verifier_Results.md bind one-to-one to the 108 criteria of 09_Rubrics.json by title; every "X/108 criteria passed" header matches its rows)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Mode: medium (assigned; cap < 85%) · Tier: Long Horizon
All-fail rubrics: NONE

No criterion failed in every completed rollout, so the QC dimension "Rubrics — All-Failing Rubrics" is an automatic 5 and there is no verdict block. The closest row is R21 (ZM's D7 retention in the memo, weight 5), which failed in run-1, run-2, run-4, run-5 and run-6 and passed in run-3: the verifier's Run #3 row reads "The memo states 'install-weighted D7 is 10.47%' over 16 mature cohort rows and 2,607 installs", and trajectory-run-3.json carries the memo text "install-weighted D7 is 10.47% (D1 32.26%). That's over 16 mature cohort rows". Every other failing row passed in at least two runs (R2, R3, R17, R19, R23, R24, R64 to R76, R106 and R108 fail in runs 3 to 6 and pass in runs 1 and 2).

Trajectory binding: each verifier Run #N names the memo Google Doc it graded, and that document id is the create-call result in exactly one export: Run #1 06fcdd9b990fb95a151a672c → trajectory-run-1.json, Run #2 400f93bd0958852b74bedd2d → trajectory-run-2.json, Run #3 aad1cb35c9890275e658b5e9 → trajectory-run-3.json, Run #4 16cd9339e9679746 → trajectory-run-4.json, Run #5 d013e43c473ed9d8e1b6496e → trajectory-run-5.json, Run #6 436572f25ff25f7a0329bc90 → trajectory-run-6.json. The reviewed receipt is Working_Files/Verifier_Export_Binding.json; 12_difficulty_input.json was built from it with --revision rev9 (verdict BOUND).

Screen file: task_inputs/11_Baseline_AllFail_Justifications.md (0 sections; Not justified: none)

Summary: valid 0 · invalid 0 (rubric 0, environment 0) · judge errors 0 · unresolved 0 · non-causal defects to fix none
Hand-off to /create-difficulty: --invalid none --judge-correction none

## Self-review

Checks walked: Evals/references/rules/all_failing.md top to bottom (an all-fail is a criterion failing every completed run; with none, there is nothing to classify) and the QC row "Rubrics — All-Failing Rubrics" in references/Docs/QC_Spec_Doc_Latest.csv (no all-fail rows → 5).

Recomputed list independently: a separate parser over the raw verifier copy (not difficulty_stats.py) counted Fail decisions per criterion over the six Run blocks. Headers read 107/108, 107/108, 86/108, 56/108, 70/108 and 86/108, and the row counts match. The most-failed criterion fails 5 of 6 (R21); the intersection of the six failure sets is empty. The calculator's line "All-fail rubrics (completed rollouts, platform view): none" agrees.

Re-verified in the exports, not from notes: R21's pass in run-3 is in trajectory-run-3.json ("install-weighted D7 is 10.47%", 7 occurrences); runs 1, 2 and 6 carry the 9.1% figure the verifier cites for them. The figures were checked in the exports themselves. No universe record is cited for a verdict, so no hg.py lookup was needed.

| Counter-reading | Resolution (evidence) |
|---|---|
| Counter: R21 is an all-fail in substance, since the verifier passed run-3 by mistake and the row is really unreachable | No. trajectory-run-3.json holds the memo text "install-weighted D7 is 10.47% ... over 16 mature cohort rows (weeks of Jul 28 to Sep 15", which is one of the two accepted figures in R21's title in 09_Rubrics.json. The pass is correct, so R21 failed 5 of 6 and is not an all-fail |
| Counter: an errored or empty run would shrink the denominator and turn a 5-of-6 row into an all-fail | No. All six exports end with a success result (difficulty_stats.read_trajectory: 6 completed, 0 errored in 12_difficulty_input.json), and each binds by content to its Run #N (Verifier_Export_Binding.json) |
| Counter: the verifier rows may belong to a different rubric version, so the list would be stale | No. --build stops on any unbound row or criterion without a row. It bound all 108 rows per run to 09_Rubrics.json (sha256 in the receipt's bundle hash), with no warning |

Unresolved: none.
