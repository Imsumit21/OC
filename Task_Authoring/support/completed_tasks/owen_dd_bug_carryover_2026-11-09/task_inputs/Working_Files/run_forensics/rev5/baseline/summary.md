# rev5 baselines: hand grading against solver/truth.json (2026-11-08)

Runs: 07_Baseline_Trajectories/trajectory-run-1 (1).json … run-6 (sha e7771fd5, bbdb8813, a9a067b4, bf1befef, 36dfc9a4, 40acd9f6), all completed, Opus 5.5 (run 2: 2 of 434 assistant messages labelled vertex_ai/global/claude-opus-5-5).
Calls: 258, 347, 338, 266, 257, 321 (average 298).

Misses per run (decode_runs.py plus a title check for the 7 bug-channel posts):
- every run: Apple sync line filed new instead of a note on ENG-2073 (Gmail never searched for it); Tavern filed Done (Marcus DM never opened); ENG-2426 and ENG-2434 moved to Done (no run called the PR reviews/comments tools); reply says 69 new tickets and 25 Done.
- shop icons filed Done: run 3 only (and the pre-check).
- music filed Bugs: runs 1 and 3.

Gradable-surface model (151 weight; the real figure depends on the rubric): r1 65.6 %, r2 66.9 %, r3 58.3 %, r4–r6 66.9 %; average ≈ 65 %; population SD ≈ 0.03; runs 2, 4, 5 and 6 fail identically (67 % of failing runs), so failure patterns are over-concentrated.
surface_grader.py read only 32 sheet rows and scored 12 %; that figure is a decoder fault, not a result.

## Second batch (same rev5 SQL, 2026-11-08; copies in run_forensics/rev5/baseline2/)
Calls 368, 266, 325, 269, 326, 304. Every run again missed Apple → ENG-2073, Tavern, ENG-2426 and ENG-2434; runs 2 and 4 also missed the shop icons; music was right in all six.
Surface model (grade_batch.py): 66.9, 58.3, 66.9, 58.3, 66.9, 66.9 % → average 64.0 %, population SD 0.041, 0 full passes. Patterns: {r1, r3, r5, r6} and {r2, r4}; largest 67 % → over-concentrated. Across 12 runs the four universal misses were caught 0/12; shop 9/12, music 10/12.
