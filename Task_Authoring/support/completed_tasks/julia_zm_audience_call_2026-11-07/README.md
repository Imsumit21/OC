# Julia: ZM friend-session audience call (archived 2026-11-11)

Persona Julia Lawson (Product Manager) · Long Horizon · Product / Marketing and GTM / Analysis and synthesis · difficulty mode medium (cap ≤ 85%), designed to a Hard (< 70%) target · universe date Oct 1, 2025 (synth-cut, clock 2025-10-01 00:00 PT) · platform attempt 6aeed82405095a0cfdffde2a (id from the eval reports).

Prompt (one paragraph, sha c3da944d7da5): Leonard asked in #zombie-design for the audience call on the friend sessions from his feedback note, to settle the "cards earlier" change. Fill in the Register tab of the 'ZM audience sessions' workbook, write the memo he asked for into Julia's Drive folder, close out the session tickets, reply in his thread with keep or hold (one call, not a maybe) and tell Brian in #zombie-design whether the tutorial and level order work goes on.

## Final state

| Slot | State |
|---|---|
| `01_Universe_Inject.sql` | rev 9 (sha 3a98aa36aadd); local /injection PASS. Rev 9 only adds Leonard's #zombie-design post 9c4e7a1d… ("a coached session doesn't count ... that goes for sessions already run too") after portal /prompt FAIL 2 on Unique Ground Truth |
| `04_Prompt.txt` | portal /prompt NON-FAIL 3, then FAIL 2 (UGT: nothing said coached sessions don't count); fixed in SQL rev 9, prompt unchanged |
| /hardness | rev 6 FAIL 1 (Leonard's request indexed every rule); rev 9 **PASS 5** (Opus observed, 326 calls; it missed only Claire's coaching admission) |
| `08_Oracle_Events.md` | 137 events; local /oe PASS 5, portal NON-FAIL 3 (side-record writes must be "(optional, not graded)") |
| `09_Rubrics.json` | 108 rows, weight 520, sha 7cef263232d2. Local /rubric runs 1-20 FAIL 1 (38/40-row design, R28 retention row never converged); portal AUDIT FAIL 1 (17 Major rows + 78 missing ticket outcomes) → rebuilt to 108 rows (one row per ticket close-out); portal run 2 FAIL 2 on R21 only (backer list) → R21 rewritten; local run 22 PASS 5 |
| `10_Baseline_Verifier_Results.md` | 6/6 completed, 0 full passes, weighted 99.0 / 99.0 / 78.8 / 50.0 / 63.5 / 78.8 = **78.2%** average (medium cap PASS); SD 0.177; 5 failure patterns, largest 2 of 6 (33%); about 336 counted calls per run |
| `11_AF_Justification.md` | NONE: no rubric failed all six runs (R21 retention failed 5, Run 3 gave 10.47%). The portal still required a justification text on the empty all-fail screen |
| `05_Human_Time.md` | 9.5 h (estimate built from the OE volumes; the `/create-humantime` worksheet was not run) |

Local `stage_gate.py difficulty` is FAIL only on the upstream chain (allfail/rubric-check attestations, stale certificates after the Evals release file changed, no platform evidence, readiness config still rev7); every difficulty number passes. The author used the portal as the real check.

## Key answers

82 sessions: 80 Linear tickets ZOM-568..647 plus Owen Baker's two Sun Sep 28 sessions that only arrive in his Sep 30 mail. Not counted: Brian Foster's Kadıköy group ZOM-568..576 (everyone works at game studios), Robert's and Douglas's/Frederick's dev build 1943 sessions (ZOM-577..586, 632, 637, 645), Claire Morgan's 13 coached sessions ZOM-607..619 (her forms say "no coaching"; her later mail admits it), and two players Contacts lists as working in games (ZOM-598 QA tester, ZOM-622 live ops producer). Samsung sessions count (the Sep 29 SM-A546E QA matrix pass covers them). Counted: 27 casual at 3.83 vs 18 RPG at 3.50, gap 0.33, so **casual lead → HOLD** the cards earlier change and tell Brian the tutorial and level order work does not go ahead. Panel figure 3.33 stars per player; D7 retention 10.47% (16 mature cohort rows from 2025-07-24, 2,607 installs) or 10.59% (Vincent's KPI snapshot), both fair. Each single trap missed flips the call to KEEP.

How Opus failed: runs 1-2 got everything except retention (9.1% over 47 cohorts, no cut-off); runs 3 and 6 took Claire's "no coaching" forms at face value; runs 4-5 also missed the game-industry exclusions (run 4 wrongly dropped Samsung sessions too) and called RPG lead.

## Lessons carried forward

1. **The requester's message must not index the rules.** Rev 6 /hardness scored 1 because Leonard's post pointed at every rule. Keep the ask in the requester message and put each rule in one deciding record elsewhere.
2. **Collective labels settle nothing.** "The friend sessions" let /prompt find a UGT fork (are coached sessions in?). Sweep every rule clause against every seeded value before the first /prompt; a rule the scenario relies on must be stated in some record, not implied.
3. **A trap that every run hits needs a correction record that contradicts the obvious one.** Claire's forms say "no coaching"; only her later mail admits it. That single two-place trap produced most of the spread (runs 3-6).
4. **Rubric shape the portal enforces:** one row per graded ticket close-out (the 40-row sampled design got "78 missing outcomes"); no count bundles, no multi-target writes, titles under ~120 words, no exact-value rejects of a fair rounding. Local DELTA runs miss these, so check them by hand before every portal /rubric round.
5. **Retention-style value rows do not converge under strict review.** 20 local rounds on the D7 row each found a new two-reading clause. Accept the two fair figures at two decimals plus a short list of backers, stop after a few rounds, and document the rest for the QM.
6. **Bind the baseline by content.** The first verifier copy graded a different (re-run) batch than `07_Baseline_Trajectories/`; no memo doc id or reply ts matched. Replacing the trajectories with the graded batch and binding by memo doc id (`Working_Files/Verifier_Export_Binding.json`) fixed it. Check this before any analysis.
7. **Read the per-run fail list before calling an all-fail.** An early hand parse claimed R21 failed all six; Run 3 had passed it. Use `difficulty_stats.py` output, not a summary.
8. **Spread from rubric rows, not SQL.** With six traps each flipping the same call, failure-pattern spread came from per-ticket rows and per-figure memo rows (5 patterns, largest 33%).

## Layout

`task_inputs/` the slot as last worked (the stray duplicate `trajectory-run-1.json` at the top level, identical to the pre-check, was dropped; Working_Files holds the design, manifests, solver, run_forensics rev1-rev8, rubric history copies and the baseline binding receipt); `eval_reports/` the portal reports (prompt ×2, hardness ×2, oe ×1, rubric ×2, prefixed with the attempt id) and the local reports (`local_*`: injection, prompt, hardness, oe, rubric run 22, portal-rules review); `work/` the unapplied run-21 rubric candidate.
