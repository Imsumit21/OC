# Robert: wind-down account close-out register (submitted 2026-10-30)

Persona Robert (Co-founder & Creative Director, robert@harmonygames.co) · Long Horizon · Executive / Corporate Ops / Planning and Decision Support · difficulty mode easy · env hg4-with-gsuite-bundle-1174 · universe hg4-2026-08-31 · universe date Feb 14, 2026 00:00 UTC · platform task 6adfee3f27ce6ca81b457137.

`task_inputs/` is the full slot folder as submitted. `work/rb_winddown_closeout/` holds the ID minting and the SQL / manifest / dossier / OE builders (moved from `support/task_work/`). `work/scratch_scoring/` holds the rubric generator and check-report scripts (`rubplan/draft.py`, `rubplan/report.py`, `rubplan/rows.json`), the baseline replay (`replay/extract.py`, `replay/score6.py`, `replay/runs.json`), and the /rubric r1 Fix List applier and 136-row replay (`r3/apply.py`, `r3/grade136.py`, `r3/af.py`). `eval_reports/` holds every platform eval report (/injection, /prompt, /hardness, /oe, /rubric).

## Final state
- Injection SQL `01_Universe_Inject.sql` sha256 fc9bc388ee2a, 120 INSERTs. Friction: none.
- Prompt (520 chars, Robert's voice): own Leonard's account close-out register, share it with Leonard and Arthur, settle each Linear issue, reply in Leonard's thread with the two monthly totals and the clashes.
- Oracle Events: 70 events (revision 26); /oe took 9 rounds (FAIL, then NON-FAIL rounds with one early PASS before later revisions) and ended PASS 5 (`_2_oe (8).md`). /injection: 10 rounds, final PASS (`_0_injection (9).md`); /prompt: 8 rounds, final NON-FAIL (`_1_prompt (7).md`); /hardness NON-FAIL. Late rounds hinged on OE 21: Gmail attachment reads return no bytes (the Singular invoice amounts are PDF-only) and the reviewer's own "two invoice mails" count was wrong (four).
- Rubric: 136 rows (135 Outcome, 1 Process), weight 500; /rubric FAIL 1 (115 rows) → PASS 5 after applying the Fix List verbatim plus my own R90 split (`_3_rubric (1).md`, sha 944d4889…).
- Baselines (6/6 completed): weighted 85.6 / 85.0 / 86.6 / 81.6 / 92.4 / 83.2 → average 85.7% (passes the QC < 90% gate, misses the Evals < 75% and the author's < 80% targets), pass@1 0/6, SD 0.034 (below 0.1), 6 failure patterns, counted calls 116–143 (avg 130). 5 all-fail rows (R37, R62, R70, R117, R118), all VALID: no run read CodeRabbit's bot notice on PR 38 (11_AF_Justification.md).

## Key answers
- Register: 25 rows (28 Linear issues ENG-2438–ENG-2466, no ENG-2445; Intuit ENG-2450 merged into QuickBooks ENG-2449; iPostal, Lucidchart, Google Ads left off as cancelled before Feb 9; ElevenLabs added from the costs-tab Sound line). Totals 6,706.49 (every row) and 1,249.04 (Keep + Hold). Shared with Leonard and Arthur as editors.
- Linear: 7 Done (Unity, Helpshift, Soundly, CodeRabbit, Cursor, Zapier, Kapwing), 4 Canceled (Intuit, iPostal, Lucidchart, Google Ads), 17 left open, a comment on all 28 (what happens + by when).
- Hidden confirmations: Unity (Arthur's #executives note relaying the account manager), Cursor (Arthur's #prototype reply), CodeRabbit (GitHub bot comment on harmonygames-Games/Combo-Fighters PR 38).
- Reply in thread C0ADGSZKR3R/1771003267.448213 with the two totals and two clashes: the Slack free-plan / guest cut vs Sunset's paid plan, and the Google archive after Feb 15 vs Sunset's keep-every-account.

## Lessons carried forward
- Difficulty: ~100 of the rows passed in every run; only the hidden confirmations (Unity, CodeRabbit, Cursor) and the Slack clash discriminated. Hide more independent facts on different surfaces before baselines, or the average lands in the mid-80s with a flat SD.
- /oe: never make an OE read a Gmail attachment; verify every count with a full scan, even in the reviewer's suggested fix.
- /rubric: split each comment into a "what happens" row and a "by when" row (including "nothing is due" rows for Closed/Moved/no-card Keep issues); replace "(or a clear equivalent)" with explicit passing labels where a decoy label exists; "say where" rows must accept the vendor's own confirmation and must not embed the status; add guards only where a real decoy exists; one Process row for "settle … and then reply"; ≤ 5 samples per spot-check group even counting the exceptions.
- Local gate: diversity.authority_share fails structurally when one Linear project governs every row (same as Douglas and Frederick); it does not affect the platform.
