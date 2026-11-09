# rev9 baselines: hand grading against solver/truth.json (2026-11-08)

Platform: /injection PASS, /prompt PASS 5 (platform revision 15), /hardness NON-FAIL 3 PROCEED (pre-check 288 calls; missed Apple → ENG-2073 email and Tavern → Marcus DM, ≈26 %, 2 causes). Reports in ../.

Runs: 07_Baseline_Trajectories/trajectory-run-1..6.json (sha 238e31d1, 936e43a9, 9f454ec6, d39e8f0e, a5b95d65, 1d2d0fe5); every run Opus 5.5, success, no errors.
Bound to rev9: every run listed ENG-2437 comments and got [] (the rev8 gift note is gone); r2–r6 read Brian's new Daily Gift line.
Calls: 333, 324, 335, 335, 277, 277 (every run over 130).

Misses (grade_batch.py, detail.py, write-by-write diff):
- every run: Apple filed new (ENG-2440 Broken) instead of a note on ENG-2073; Tavern filed Done (Marcus DM never opened); reply says 69 new tickets.
- r1: also shop icons Done, ENG-2426 and ENG-2434 moved to Done (read Brian's DM only for Nov 13–24, so missed the Dec 11 lines); reply 7 / 69 / 25 of 28. It held ENG-2437 for another reason (commit not on the economy line).
- r3: also shop icons Done (read #dd-road-to-sub-250mb only to Nov 24); reply 7 / 69 / 23.
- r2, r4, r5, r6: no other miss. Their writes are identical item by item (ticket states, child updates, sheet outcomes); only the sheet title, r6's writer role and r4's missing link differ, none graded.

Gates on this batch:
- average: surface model 75.6 %, lean rubric model ≈ 74 % (scores ≈ 60, 78, 73, 78, 78, 78) → under 80 % and the 85 % cap: PASS
- full passes 0: PASS; errored 0: PASS; calls > 130 in every run: PASS
- failure patterns: r2, r4, r5, r6 identical → 4 of 6 = 67 % > 50 %: FAIL whatever the rubric
- SD ≈ 0.067–0.084 < 0.10: FAIL

Why a re-run on the same SQL cannot pass: every run misses Apple and Tavern (that is what passes /hardness), and the items that vary (shop, popups, 23-of-28) weigh only ≈ 15–18 %. The best and worst plausible runs are about 18 points apart, so even a 3/3 split gives SD ≈ 0.09. Enumerating six-run batches over the observed signatures (S0 = Apple+Tavern only, S3 = +shop, S1 = +shop+popups) gives P(all gates) = 0 under a 115-weight rubric, and about 0.1–0.25 even if the rubric weighs Brian's DM items at /hardness's 18 %.
Brian's DM was read past early December by 6 of 7 rev9 runs (pre-check included), so the D cluster is nearly universal too.

## Second batch (same rev9 SQL, 2026-11-08; copies in ../baseline2/)
Runs sha 169f06d5, ccf2c417, 5228a35e, 19091c8f, afdf54fc, f3a71584; all Opus 5.5, success, 0 errors. Calls 328, 338, 341, 290, 286, 246.
- r3, r4, r5: only Apple + Tavern wrong (23 of 28 right).
- r1, r2, r6: Apple + Tavern + ENG-2426 and ENG-2434 moved to Done (reply 25 of 28). Shop icons right in all six.
- Writes identical within each group (write-by-write diff); the groups differ on ENG-2426, ENG-2434 and the 23-of-28 count (3 rubric rows).
Gates: patterns 2, largest 3 of 6 = 50 % → PASS (at the limit; extra rows can only split groups further). Full passes 0, errors 0, calls > 130: PASS. Average: surface 73.8 %, lean rubric ≈ 74–75 %: PASS.
SD: surface 0.070; lean rubric (≈ 115 weight, popups + count = 15) ≈ 0.065; /hardness-style weights ≈ 0.088 → FAIL. This batch is the best split the design allows (3/3 between the two most different signatures), so SD ≥ 0.10 needs the varying weight ≥ 20 % of the rubric (total ≤ 75 with 15 varying), which an honest rubric for this prompt does not reach.
