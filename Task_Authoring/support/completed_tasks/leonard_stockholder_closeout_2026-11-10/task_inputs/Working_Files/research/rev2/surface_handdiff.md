# Pre-check run: hand-graded surface diff (rev1p run vs current surface)

Graded 2026-11-08 by hand. The automatic grade (`run_forensics/rev1p/precheck.surface_grades.json`, 65/234 = 27.8%) is a decoder artifact: it found `register_kind NATIVE_SHEET` with `rows: 0` because the run wrote three tabs (`Holders!A1`, `Summary!A1`, `'KPMG 2025-12-31'!A1`). It also matched `fileId` where the run's calls carry `file_id`, and it read `link` selectors as "the deliverable links the shared sheet". No slot that the automatic grader passed fails by hand. 57 slots it failed are MET.

## 1. Inputs and method

- Run: `06_PreCheck_Trajectory/trajectory.json` (sha256 f059ce83…, 957 events, Opus 5.5, 237 calls). Writes come from `run_forensics/rev1p/precheck/precheck/writes.json` (67 writes) and were checked against the result events in the trajectory.
- Truth: `Working_Files/solver/truth.json`. I re-derived it with `oracle_kit.truth(solver, sql_text)`, which parses the SQL and does not run it. The current SQL (fd51afbf63aa) reproduces truth.json exactly.
- Surface: `Working_Files/01_Gradable_Surface.json`, 96 slots, total weight 234. Weights exist, so the score below is weighted.
- Grading rule: a slot is MET when the written value or content matches the truth meaning of the slot title and fact. Regexes guide the reading but do not decide it. For example, a cell join or a recipient-only name does not fail a slot.
- Linear state ids come from event 759: `state_f5f67279df1a52c2` = Todo, `state_f71945f4d2e95895` = Done, `state_7e56143481a65571` = Canceled.

## 2. SQL drift between the run's platform SQL and the current SQL

- The platform /hardness report names the run's SQL as `bc72db9c31e9…` (74,125 B). That exact file is not stored locally. The nearest copy is `run_forensics/rev1p/01_Universe_Inject.sql` (6f3b1899…, 74,274 B, 149 B larger). It agrees with every platform-era record the run quoted: KPMG's single clarification on item 2, the "Last written contact I have before Feb: Nov 6, 2025" comments, and the "Feb 12 Board position thread" wording in the notes.
- What the current SQL (101,094 B) adds or changes:
  - **ADV pointers (new).** Leonard's Jan 14 note in #executives ("the ledger has 3,051,879 seed preferred … the owner list counts the advisor options in with the stock"). KPMG's follow-up now opens "our prior-year file has 6,000,000 common and 3,051,879 Series Seed". The draft sheet gets a note that the list's percentages leave out the option pool.
  - **KPMG follow-up.** It now has three clarifications instead of one: a terminated line counts only what had vested, and item 4 asks about financing and the wind-down.
  - **Board.** Robert's reply-all on the Board position thread ("That leaves Leonard and me on the board"), and Collins's contact job becomes "left the board May 2025".
  - **Notes doc.** The Griffin reply becomes reply-all and asks for their vote. The doc adds "counts go by rows" and "Carta over any date in the letters". "Notice route: the email we have, unless a document says otherwise" becomes "Messages go to the email on each holder's issue".
  - **Linear.** Every issue gets an `Email:` description. The comments become "Last mail with that address before Feb" with new dates. ENG-2447 and ENG-2460 are retitled.
  - Smaller edits: the legal intake drops the formal-notice item, slide text changes, and workers-comp mail is edited.
- **Effect on truth.** I ran the solver on the rev1p SQL. Only three fields differ: two Holder strings, which no slot grades, and SUMMARY Directors. For Directors the solver falls back to "Leonard Hayes, Robert, Matthew Collins, Griffin's director", because R_BOARD (Robert's injected reply) is absent. That fallback is the solver's degrade path, not the platform-era answer. The base records still decide it: Collins resigned on May 1, 2025 (Leonard's mail `CAMy0Hx1va…`, which the run listed at event 59), and Griffin's director resigned on Feb 12 (thread 1856958794180374704, which the run read). So B1's truth is still "Leonard Hayes, Robert" in the platform era.
- **ADV truth does not depend on the SQL.** The deciding records are base records:
  - Due Diligence Disclosures `f_6a37227593d0977fdbdd7a` (Leonard's doc) lists the advisor table: 30,518 / 61,038 (Collins) / 6,104 / 6,104, 103,764 in total.
  - The Reset Financing Term Sheet `f_11040fe5d66821bd6951aa` (Jan 22, 2026), Exhibit A "Inputs from ledger", gives Series Seed 3,051,879.
  - The run's 3,155,643 is exactly 3,051,879 + 103,764.

  What the platform era lacked was the three injected pointers, so ADV was harder to find on the platform, but the values are the same. Every slot below is graded against the same values in both eras.

## 3. Writes decoded

| Events | Write |
|---|---|
| 767 | gsheets_batch_update on f_5ecaa967… ("Holder list (draft)", already in close-out folder d_601064334a0b493022fe83): Sheet1 renamed Holders, Summary and 'KPMG 2025-12-31' added, file renamed "Holder sheet" |
| 771 / 780 | Holders!A1: 26 rows ENG-2438…2463 (cols: shares today, vested options today, last day, label, told, note, order, route, remarks); J14:J27 note order |
| 783 | Summary!A1: common 6,000,000; Seed 3,155,643; options now 55,942; label counts 6/4/6/6/2/2; 14 notes; directors; preferred vote ~87% |
| 785 | 'KPMG 2025-12-31'!A1: 12 option lines, 139,993; 9,295,636; events |
| 789 / 794 / 796 | investor letter 4e34ab72… created, "eleven" changed to "ten angel investors", moved into the close-out folder |
| 799 / 801 / 803 | shares (writer): sheet to Robert and to Arthur; letter to Robert |
| 814–852 | 14 gmail_create_draft: 8 option holders (Vincent, Julia, Claire, Brian, Marcus, Owen, Martin, Oliver) and 6 stock notes (Schaeppi, Bergmann, Enes for the family, Collins, TOR, Deepak) |
| 856–906 | 26 linear_update_issue (14 Todo / 6 Done / 6 Canceled; every one matches truth State) |
| 909–931 | 12 linear_create_comment on the 4 told + 2 covered + 6 lapsed issues |
| 936 | Griffin heads-up, reply-all on "Re: Board position" (To Griffin's partner; cc Griffin colleague, Robert, Arthur) |
| 944 / 950 | KPMG reply-all, which reached the sender only; then gmail_send_message on the same thread to the sender + 3 cc |
| 953 | #winddown reply in thread 1770934638.035469: who goes first, Vincent [ES-14], Feb 21 |

Row-level check of the Holders tab against truth: all 26 rows match on Owed, Told, Last day, Options now and Linear State, apart from the four advisor-angel rows. Those rows differ only by their grants. ENG-2440: 81,383 vs 50,865 + 30,518. ENG-2446: 31,536 vs 25,432 + 6,104. ENG-2447: 86,470 vs 25,432 + 61,038. ENG-2449: 31,536 vs 25,432 + 6,104.

## 4. Slot-by-slot grades

"r" = sheet row. "Auto" = the automatic grade. No slot is UNGRADED.

| Slot | W | Grade | Auto | Write event | Written | Truth | Reason |
|---|---|---|---|---|---|---|---|
| K1 | 5 | FAILED | fail | 783 Summary r8; 785 r5; 944/950 | 3,155,643 | 3,051,879 | ADV: owner-list lines booked as stock, +103,764 |
| K2 | 3 | MET | fail | 771 ENG-2438 | 2,662,255 | 2,662,255 | owner-list fund split correctly |
| K3 | 3 | MET | fail | 771 ENG-2439 | 84,438 | 84,438 | Side Fund on its own row |
| K4 | 5 | FAILED | fail | 771 ENG-2447 | 86,470 | 25,432 | ADV: includes Collins's 61,038 grant |
| K5 | 5 | FAILED | fail | 771 ENG-2440 | 81,383 | 50,865 | ADV: includes 30,518 grant |
| K6 | 5 | FAILED | fail | 771 ENG-2446 | 31,536 | 25,432 | ADV: includes 6,104 grant |
| K7 | 5 | FAILED | fail | 771 ENG-2449 | 31,536 | 25,432 | ADV: includes 6,104 grant |
| K8 | 3 | FAILED | fail | 771 ENG-2447 col E | blank; 61,038 nowhere | 61,038 on Collins's row | ADV: grant never separated |
| K13 | 1 | MET | fail | 771 ENG-2448 | 50,865 | 50,865 | plain line |
| K14 | 1 | MET | fail | 771 ENG-2441 | 25,432 | 25,432 | plain line |
| K15 | 1 | MET | fail | 771 ENG-2442 | 25,432 | 25,432 | plain line |
| K16 | 1 | MET | fail | 771 | 26 rows ENG-2438..2463 | 26 truth keys | exact key set |
| P1 | 5 | FAILED | fail | 783 Summary r10; 953 | 55,942 | 159,706 | ADV: 103,764 advisor grants left out |
| P_lapsed_ES2 | 1 | MET | fail | 771 ENG-2451 | Nothing | Nothing | last day 2024-11-01 passed |
| P_lapsed_ES3 | 1 | MET | fail | 771 ENG-2452 | Nothing | Nothing | last day 2026-01-24 passed |
| P_lapsed_ES5 | 1 | MET | fail | 771 ENG-2454 | Nothing | Nothing | last day 2026-01-24 passed |
| P_lapsed_ES6 | 1 | MET | fail | 771 ENG-2455 | Nothing | Nothing | last day 2025-07-16 passed |
| P_lapsed_ES16 | 1 | MET | fail | 771 ENG-2461 | Nothing | Nothing | last day 2026-01-24 passed |
| P_FRED | 3 | MET | fail | 771 ENG-2462 | Nothing | Nothing | last day 2026-01-28 passed |
| P_live_ES-1 | 1 | MET | fail | 771 ENG-2450 | 17,802 | 17,802 | vested only |
| P_live_ES-4 | 1 | MET | fail | 771 ENG-2453 | 4,450 | 4,450 | vested only |
| P_live_ES-7 | 1 | MET | fail | 771 ENG-2456 | 12,875 | 12,875 | vested only |
| P_live_ES-12 | 1 | MET | fail | 771 ENG-2457 | 8,477 | 8,477 | vested only |
| P_live_ES-13 | 1 | MET | fail | 771 ENG-2458 | 2,013 | 2,013 | vested only |
| P_first | 3 | MET | pass | 771 ENG-2459 | 2026-02-21 | 2026-02-21 | earliest live date |
| C_ES14 | 5 | MET | fail | 771 ENG-2459 | Closing and last day | Full note | label synonym |
| C_ES18 | 5 | MET | fail | 771 ENG-2463 | Closing and last day | Full note | label synonym |
| C_DATE | 3 | MET | pass | 783 Summary r17 | Last day: 6 | 6 | count by rows |
| C_SEG | 5 | MET | fail | 771 ENG-2440 | Already told | Already told | Feb 9 DM found |
| C_NEB | 5 | MET | fail | 771 ENG-2446 | Already told | Already told | Robert's Feb 12 mail found |
| C_TOR | 3 | MET | fail | 771 ENG-2448 | Closing | First note | runway warning not counted |
| C_FIRST | 3 | MET | pass | 783 Summary r16 | Closing: 6 | 6 | count by rows |
| TC_ES14 | 3 | MET | fail | 771 ENG-2459 | No | No | no closing message |
| TC_ES18 | 3 | MET | fail | 771 ENG-2463 | No | No | channel post not counted |
| TC_SEG | 3 | MET | fail | 771 ENG-2440 | Yes | Yes | DM |
| TC_NEB | 3 | MET | fail | 771 ENG-2446 | Yes | Yes | Robert's reply |
| TC_TOR | 3 | MET | fail | 771 ENG-2448 | No | No | not told |
| B1 | 5 | MET | fail | 783 Summary r23 | Leonard Hayes, Robert | Leonard Hayes, Robert | both resignations applied |
| B2 | 3 | FAILED | fail | 783 Summary r24; 936 | about 87% (2,746,693 of 3,155,643) | 90.0% | ADV cascade: wrong denominator; "Griffin alone carries" is right |
| L3 | 1 | MET | pass | 789 | "do not expect any cash ... distribution" | no distribution | present |
| L4 | 1 | MET | pass | 789 | Tax papers paragraph | tax / write-off | present |
| L5 | 1 | MET | pass | 789 | "IP and codebase" | IP / codebase | present |
| L2 | 1 | MET | pass | 789 | Sunset runs the dissolution | Sunset | present |
| L6 | 3 | MET | pass | 789 | "the board now consists of me and Robert" | board + Robert | present |
| L8 | 1 | MET | pass | 789 | Options paragraph | option / exercise | present |
| G1 | 1 | MET | fail | 936 | reply-all on Board position thread 1856958794180374704 | reply on that thread | sent; To Griffin partner, cc Robert, Arthur |
| G2 | 3 | MET | pass | 936 | "Written consent, as majority holder of the Series Seed Preferred" | consent / vote | present |
| NC_Schaeppi | 3 | MET | fail | 842 | 25,432 | 25,432 | note states the holding |
| NC_Bergmann | 3 | MET | fail | 844 | 25,432 | 25,432 | note states the holding |
| NC_Deepak | 3 | FAILED | fail | 852 | 31,536 | 25,432 | ADV |
| NC_Collins | 3 | FAILED | fail | 848 | 86,470 | 25,432 | ADV |
| NC_Tor | 3 | MET | pass | 850 | 50,865 | 50,865 | note states the holding |
| F4 | 3 | MET | fail | 771 ENG-2444 | Covered | Covered | family rule applied |
| F5 | 3 | MET | fail | 771 ENG-2445 | Covered | Covered | family rule applied |
| F1 | 5 | MET | fail | 846 | one note to Enes, "covers all three holdings", names Patrick and [27652] | one covering note | present |
| F2 | 3 | MET | pass | 846 | "76,296 shares in total" | 76,296 | present |
| F3 | 3 | MET | pass | 915, 917 | "has always handled this family's investment" | reason comment | present |
| N_COUNT | 3 | MET | fail | 814-852; 783 r21; 953 | 14 drafts | 14 (6 first + 6 date + 2 full) | exact count |
| ND_ES-1 | 1 | MET | fail | 816 | Julia, March 31 | Mar | present |
| ND_ES-4 | 1 | MET | fail | 818 | Claire, March 31 | Mar | present |
| ND_ES-7 | 1 | MET | fail | 822 | Marcus, April 30 | Apr | present |
| ND_ES-12 | 1 | MET | fail | 824 | Owen, April 30 | Apr | present |
| ND_ES-13 | 1 | MET | fail | 826 | Martin, April 30 | Apr | present |
| ND_vol | 1 | MET | fail | 816-826 | 6 date notes | 6 | all six |
| N_Vincent | 5 | MET | fail | 814 | "we have decided to close"; Feb 21 | closing + Feb 21 | present |
| N_Oliver | 3 | MET | fail | 828 | "we have decided to close" | closing | present |
| Q1 | 5 | MET | fail | 818 | "you don't" / "There is nothing you need to do" | no action needed | answers Claire's question |
| A1 | 5 | FAILED | fail | 944, 950 | 139,993 | 243,757 | ADV: 103,764 advisor grants left out |
| A2 | 5 | MET | pass | 944, 950 | 9,295,636 | 9,295,636 | value right only because the 103,764 moved from options to Series Seed and nets out |
| AL_ES-7 | 3 | MET | pass | 944, 950 | 22,889 | 22,889 | full grant, terminated Jan 30 |
| AL_ES-12 | 3 | MET | pass | 944, 950 | 16,277 | 16,277 | full grant |
| AL_ES-1 | 3 | MET | pass | 944, 950 | 17,802 | 17,802 | vested only, terminated Dec 31 |
| AL_ES-14 | 3 | MET | pass | 944, 950 | 1,530 | 1,530 | effective Nov 21 |
| AL_ES-16 | 3 | MET | pass | 944, 950 | 10,384 | 10,384 | open at Dec 31 |
| AL_vol | 1 | FAILED | fail | 944, 950 | 12 lines | 16 lines (12 ES + 4 advisor grants) | ADV cascade; the 12 Carta ES lines are all right |
| A3 | 3 | MET | pass | 944, 950 | 84,438 | 84,438 | each fund shown |
| A9 | 1 | MET | pass | 944, 950 | 6,000,000 | 6,000,000 | present |
| A5 | 3 | MET | pass | 944, 950 | "decided to wind down the company" | later event | present |
| A7 | 1 | MET | fail | 944, 950 | "No financing or issuance of equity." | no new financing | meaning matches; regex wording misses |
| A8 | 1 | MET | fail | 944 then 950 | 944 reached sender only; 950 on-thread to sender + 3 cc | all four recipients | end state right; sender got it twice |
| LC_Seg | 3 | MET | fail | 913 on ENG-2440 | reason given: Leonard's Feb 9 Slack DM | reason comment | present (it also repeats 81,383) |
| LC_Neb | 3 | MET | pass | 919 on ENG-2446 | reason given: Robert's Feb 12 email | reason comment | present (it also repeats 31,536) |
| LC_ES-2 | 1 | MET | pass | 921 | "holds nothing ... lapsed" | reason comment | present |
| LC_ES-3 | 1 | MET | pass | 923 | "holds nothing ... lapsed" | reason comment | present |
| LC_ES-5 | 1 | MET | pass | 925 | "holds nothing ... lapsed" | reason comment | present |
| LC_vol | 1 | MET | fail | 909-931 | 12 comments | 12 no-note issues | exactly the 4 told + 2 covered + 6 lapsed |
| LS_ES-3 | 1 | MET | fail | 884 | Canceled | Canceled | state id 7e56... = Canceled |
| LS_ES-6 | 1 | MET | fail | 890 | Canceled | Canceled | correct |
| LS_ES-12 | 1 | MET | fail | 894 | Todo | Todo | state id f5f6... = Todo |
| LS_vol | 1 | MET | fail | 856-906 | 26 of 26 moved | 26 | every state matches truth |
| D1 | 1 | MET | fail | 767 (renamed in place) | f_5ecaa967... already in d_601064334a0b493022fe83 | close-out folder | already in the folder |
| D2 | 1 | MET | fail | 799, 803 | sheet and letter shared with Robert (writer) | shared | notes give no role; selector's reader role is ungrounded |
| D4 | 1 | MET | fail | 801 | sheet shared with Arthur (writer) | shared | follows the thread change |
| D3 | 1 | MET | fail | 796 | letter moved to d_601064334a0b493022fe83 | close-out folder | present |
| D5 | 1 | MET | fail | 953 | reply in #winddown thread 1770934638.035469 | thread reply | present |
| D6 | 3 | MET | pass | 953 | "Vincent Parker [ES-14] ... Feb 21" | Vincent / Feb 21 | present |

## 5. Hand-corrected score

- **Weighted: 186 / 234 = 79.5%.** That is 84 of 96 slots MET and 12 FAILED (unweighted 87.5%). The automatic grade was 65/234 = 27.8%.
- Sensitivity:
  - AL_vol read as "every Carta ES line" (12/12) instead of "every option line incl. advisor grants": 187/234 = 79.9%.
  - D2/D4 failed for role writer, if a reader role were required: −2 (184/234 = 78.6%). Nothing in the notes or the thread asks for a role, so I keep them MET.
- One run only. Against the V3 medium cap (average below 85%), this single run sits under the cap.

## 6. Weight-5 slots that passed

9 of 16 passed, worth 45 of 80 weight-5 points: **C_ES14, C_ES18, C_SEG, C_NEB, B1, F1, N_Vincent, Q1, A2**. A2 passes only because the misallocation nets out (3,155,643 + 6,000,000 + 139,993 = 9,051,879 + 243,757).
Weight-5 slots that failed: K1, K4, K5, K6, K7, P1, A1. All seven are ADV.

## 7. Root causes of the failed slots

There is **one root cause, ADV**. The run took the Nov 2024 owner-list lines (86,470 / 81,383 / 31,536 / 31,536) as Series Seed stock. It never opened the Due Diligence advisor table (f_6a372275…) or the term sheet's ledger total (f_11040fe5…). It did notice ES-9 (Collins) and ES-11 in a Nov 2023 Carta activity email and wrote that "the Nov 2024 list appears to fold them into per-person totals" (event 835). It still booked those totals as stock, and its final message tells Leonard it treated them that way.

All 12 failed slots (48 weight) are this one cause:

- Per-line stock: K4, K5, K6, K7.
- The grant itself: K8.
- Series Seed total: K1.
- Preferred-vote share: B2 (87% vs 90.0%).
- Options now: P1 (−103,764).
- Options at Dec 31: A1 (−103,764) and AL_vol (4 grant lines missing).
- Note holdings: NC_Collins, NC_Deepak.

There is no second independent cause. Every TOLD, LETTER, FAM, ASOF, ASK and BOARD decision is right.

Off-surface carry-through of the same cause: the ENG-2440 and ENG-2446 comments repeat 81,383 and 31,536; the Griffin heads-up and the KPMG reply state 3,155,643 and about 87%; the #winddown post says 55,942 vested options. Off-surface, unrelated to ADV: 7 of 8 option-holder drafts go to @harmonygames.co work addresses, and TOR's draft goes to TOR's directors. Both are defensible under the platform-era rule "the email we have, unless a document says otherwise". Under the current SQL ("the email on each holder's issue") they would be wrong addresses. No surface slot grades recipients.

## 8. Check of the platform /hardness report

`plateform_reports/6aed9d01a1cb8067d8ac7dee_1a_hardness.md` scored 2 (Easy): every requirement MET, minor gaps G1–G3, and ADV under "Unassessed scope". It said "No grant sizes exist in the data the evaluator or the Agent could find" and that a "2nd Close" supports 3,155,643.

I disagree on ADV. The grant sizes are in the base Due Diligence Disclosures doc, which belongs to Leonard and is shared with Robert and Arthur. The Jan 2026 term sheet's ledger gives 3,051,879. The gap is exactly 103,764. So:

- R1 is not MET: the sheet's stock lines, Series Seed total, options now and preferred share are wrong.
- R7 is partly unmet: the Collins and Deepak notes state wrong holdings.
- R13 is not MET: item 1 Series Seed and item 2 options and lines are wrong. Item 3 (9,295,636) is right, as the report says.

That is one material, independent failure worth about 20% of surface weight, not "no material failure". I agree with its other MET calls (R2–R6, R8–R12, R14) and with G1–G3 as minor.
