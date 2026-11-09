## RUBRIC EVALUATION REPORT

- Attempt: 6aed9d01a1cb8067d8ac7dee (chat /rubric, run 3, DELTA mode)
- Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
- Inputs: rubric `09_Rubrics (3).json` (195 rows), prompt, assignment, injection SQL (rev 6), Oracle Events (rev 10)

### Task: Stockholder/option-holder close-out (holder sheet, investor letter, 14 holder note drafts, Linear states and comments, Griffin heads-up, #winddown reply, KPMG confirmation)
### Persona: Leonard Hayes - Co-founder & Creative Director
### Total Rubrics: 195 (Outcome: 194, Process: 1)

## Fix List

| Row | What is wrong | Fix to copy | Mark |
|---|---|---|---|
| 2 | One row grades seven separate old Sheet1 rows (non-atomic). It names only the first, so once the Notes cell is gone a judge can't tell which rows were old (not self-contained). A run that writes labels over the old rows' Notes cells and keeps their Nov 2024 figures can still pass (overly broad). | **Replace row 2 with one row per old Sheet1 row.** Five of the seven are checked (rows 197–201 below, added at the end). **The Griffin row (row 2) needs your own rewrite.** The open problem: the old "GRIFFIN GAMING PARTNERS 2,746,693" line merges both funds. A run can reuse it as one fund's row, as a row naming both funds, or beside the other fund's own row. Every wording we tried either failed a correct reuse or made the row also grade the side fund's row, which R4 and R28 already check. | revised after check |
| new 196 | Part of the row-2 split: the old "[PERSON_NAME_0038] 127,162" row (ENG-2462). | **This row needs your own rewrite.** The open problem: ENG-2462 has no share row, so a reused old row that still shows 127,162 goes ungraded unless this row grades it. But a closed list ("nothing or 0") fails correct renderings such as "lapsed" or "expired". Grading the holding here also fails R51 together with this row when a run treats ES-17 as live. | revised after check |
| new 197 | Part of the row-2 split | The Agent deletes or clears the draft sheet's old row "[PERSON_NAME_11362] 86,470" (marked "copied from the Nov 2024 list"), writes other sheet content over its holder name and figure, or turns that row into ENG-2447's one row by writing on it its ENG id or one of the labels Nothing, Already told, Covered, Closing, Last day or Closing and last day, right or wrong | checked |
| new 198 | Part of the row-2 split | Same form for "[PERSON_NAME_0089] [PERSON_NAME_25152] 81,383" and ENG-2440 | checked |
| new 199 | Part of the row-2 split | Same form for "TOR Capital Limited 50,865" and ENG-2448 | checked |
| new 200 | Part of the row-2 split | Same form for "PERSON_3941_NAME [PERSON_NAME_0127] 31,536" and ENG-2446 | checked |
| new 201 | Part of the row-2 split | Same form for "PERSON_1287_NAME 31,536" and ENG-2449 | checked |

For rows 197–201: weight 1, Outcome. Justification: "Lookup: the old row is visible in Sheet1 of the draft, and the notes say to finish that draft with one row per issue." Evidence: Sheet1 of f_5ecaa967db3adcfa440b09 (that row's cells), plus the notes' "Finish my draft one…", "One row per issue on the sheet…" and "Labels for the sheet: …". Accept: the old row is deleted or cleared; or any other sheet content is written over its holder name and figure; or the row itself becomes that issue's one row on the sheet (whether its label and figure are right is graded by the holder's own label and share rows). Fails: the old row left as it is; only its Notes cell changed, with no ENG id or label; or kept beside a second row for that issue.

**Simpler alternative (upstream):** make the draft sheet (SQL line 22) hold only its header row, re-run /injection and /prompt, then delete row 2. That route needs no new rows at all, and the owner-list trap still lives in the Linear comments ("Nov 2024 owner list: …"). The SQL change outdates every earlier pass that read it, so send /injection, /prompt, /hardness, /oe and /rubric again, in that order.

---

### Phase 1: Structural Validation
- Five-field completeness: 195 of 195. Outcome 194, Process 1. Weights all 1/3/5.
- Requirement coverage: 201 of 201 outcomes. Row 2's seven old rows are counted as seven outcomes; the authored denominator stays 195.

### Phase 2–3 summary (target rows 2–8, 53, 84, 178–180)
- **Facts:** every value in the target rows is re-bound to its record.
  - Rows 3–8: the purchaser schedule gives 2,662,255 and 84,438. Owner-list figure minus grant: 81,383 − 30,518 = 50,865; 31,536 − 6,104 = 25,432; 86,470 − 61,038 = 25,432.
  - Row 53: 9,051,879 + 164,114 = 9,215,993.
  - Rows 178–180: every added name is found in its cited thread. ES-15's are in Carta digests 1813700131573811805 and 1813881602779637554, holder mail 1801054030196213239 and invite 1800824149233468611. ES-16's are in notice 1847333318158821452, threads 1805972621079109235 and 1805453551522119612, and option list 1782034095239486005. ES-17's are in digest 1813700131573811805 and invite 1788274927802139924.
  - No mismatch.
- **Atomicity:** row 2 is non-atomic (seven old rows). The other target rows hold one result each.
- **Acceptance:** rows 53 and 178–180 now accept the record-backed answers. The VALUE searches on 178–180 return ACCEPTED.
- **Overlap:** the stale-row cascade group is gone. Rows 3–8 no longer fail on the draft's old rows, so leaving them fails only row 2.
- **Weights:** row 84 is now weight 3 and matches its work.
- **Negative criteria, Agent-centric phrasing, Process:** clean.

### Phase 4: Issue Tally
| Severity | Rows | Fails when | Status |
|---|---|---|---|
| Major | 1 (row 2: non_atomic, not_self_contained) | any | FAIL |
| Moderate | 0 | any | PASS |
| Minor | 0 counted (row 2's overly_broad is absorbed at Major) | ≥5% | PASS |

### Phase 5: Scoring
| Sub-Dimension | Score |
|---|---|
| Overall Rubric Quality | 1 |
| Criteria Weights | 5 |
| Rubric Category Balance | 5 |
| Process Rubrics | 5 |
| Agent-Centric Phrasing | 5 |
| Negative Criteria | 5 |
| Predicted All-Fail gate | PASS |

## Changes Since Last Run

- **Rows:**
  - 183 locked;
  - 1 locked as a copy of a checked fix (row 53);
  - 10 edited (rows 3–8, 84 and 178–180);
  - 1 re-checked because it was flagged last time (row 2);
  - 0 new and 0 removed. Row 53's text changed in place.
- **Previous findings now fixed:**
  - The stale-row cascade, rows 2–8: rows 3–8 dropped their "Nov 2024 figure … fails" clauses, and their evidence now says an old draft row left on the sheet doesn't affect them.
  - Row 53's fail clause (now "another figure given as today's … total fails").
  - Row 84's weight (now 3).
  - The closed name lists in rows 178, 179 and 180 (now every name form the records give).
- **Dismissals:** none recorded.
- **New scored findings:**
  - Row 2, which was re-checked because it was flagged last time, is non-atomic (R7), not self-contained (R6) and overly broad (R5).
  - Last run's fix-check rejected an R7 point on row 2 as "one artifact state". That is the "one closed population" rationale, which Eval 3 §2.2 lists as rejected, so this run confirms the finding.

### Notes for QM (not scored)
- **Row 53 (R7-DR2), locked:** R7 reads "another figure given as today's option or share total fails" as a separate claim. It is a wrong-value clause for the same reported total, and the row is locked with no code-check hit.
- **Row 84 weight (R4-DR1):** R4 proposed 5, by analogy with rows 85–87. Kept at 3, as last run's check found. Calvin's not-told evidence (the ENG-2452 comment "No mail with that address before Feb", and no founder message since) matches rows 79–83. The decoys behind 85–87 (the bounced Feb 11 letter, "All termination letters are sent") are not in his chain.
- **Rows 174/175, locked (R4-DR2):** a wrong Dec 31 option total fails both R174 and R175, since R175 adds 9,051,879 to it. Between the line rows 178–180 and R174/R175 this is an aggregate control against its spot checks, which §3.3 does not count as a duplicate.
- **Founders' rows (R3-DR1):** no row checks that the three founders get no sheet row ("The three of us get no row, only the totals"). This older gap was not caused by this round's edits.
- **Letter "Holders" section (R3-DR2):** the update outline's "Holders, per the Nov 2024 owner list" section still has no letter row. This is unchanged from last run.
- **Wording carried from last run:** row 92 still says "31,536 as shares fails" on the draft note. Row 181 accepts "Husnu Matthew Collins" and row 177 "Marcus Bennett".

### Rejected findings
- **R2-DR1/DR2 (rows 178/180 call thread 1813700131573811805 the "Oct 23, 2024 digest"):** the message's date header is "Wed, 23 Oct 2024 10:27:12 +0000" (subject "Carta activity for Oct. 22, 2024"). The label matches the sent date and the thread id is exact.
- **R4-DR1 (row 84 → 5):** the records R4 cites for the "same check" (the Feb 11 letters post) are not in Calvin's chain. See Notes for QM.
- **R4-DR2 (rows 178–180 cascade into R174/R175):** §3.3 says "an aggregate control versus its atomic spot checks" is not a duplicate. The R174/R175 pair is locked, so it goes to Notes for QM.
- **R3-DR1/DR2:** coverage gaps that no change caused, and the prompt doesn't state them outright, so they go to Notes for QM (rubric_flow_v2, DELTA step 3).

## Deep Recheck

Passes: R1, R2, R3, R4, R5, R6 and R7 on the 12 target rows (R4 against all 195, R3 whole-rubric coverage), Opus 5.5, each blind to the main review. Fix-check on the row-2 split: rounds 1–3 (all seven topics per round), then a restructure checked in round 4. Rows 197–201 came back clean in round 4; rows 2 and 196 kept findings and are marked "needs your own rewrite".

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| R1 | 12 | 0 | 0 |
| R2 | 12 | 2 | 0 |
| R3 | 195 | 2 | 0 |
| R4 | 12 vs 195 | 2 | 0 |
| R5 | 12 | 1 | 1 |
| R6 | 12 | 1 | 1 |
| R7 | 12 | 2 | 1 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | R7 | R2 "overwrites or deletes the seven old rows" | SQL line 22, Sheet1 seven rows | 2.2 | non_atomic | CONFIRMED | Seven separate rows; closed population is a rejected rationale |
| DR2 | R7 | R53 "another figure given as today's … total fails" | Sunset 1857034369525983506 | 2.2 | non_atomic | REJECTED | Locked row, no code-check hit; Note for QM |
| DR3 | R6 | R2 names only the first old row | SQL line 22 | 2.1 | not_self_contained | CONFIRMED | Six holder/figure pairs only in the records |
| DR4 | R5 | R2 "overwrites … the seven old rows" | SQL line 22; OE 39 | 2.7 | overly_broad | CONFIRMED | Labels written over Notes cells, old figures kept, can pass |
| DR5 | R4 | R84 weight 3 | rows 85–87 | 2.12 | weight | REJECTED | Calvin's chain matches 79–83 |
| DR6 | R4 | R178–R180 with R174/R175 | KPMG 1857029474983245439 | 3.3 | duplicate | REJECTED | Aggregate against spot checks |
| DR7 | R2 | R178/R180 "Oct 23, 2024 digest" | thread 1813700131573811805 date header | 2.3 | incorrect | REJECTED | Sent Oct 23, 2024 |
| DR8 | R3 | founders get no row | NOTES f_a37b403d5200d4f0a31d31 | 3.1 | missing_coverage | REJECTED | Older gap; Note for QM |
| DR9 | R3 | letter Holders section | outline f_75dddccabb26eeea4842c8 | 3.1 | missing_coverage | REJECTED | Older gap; Note for QM |
| FC1–4 | round 1 | split rows "a holder's current data" | OE 39; SQL lines 22, 284 | 2.7 | overly_specific | CONFIRMED | Revised in round 2 |
| FC5–9 | round 2 | closed overwrite list; reuse plus duplicate; R196 figure | OE 39; notes | 2.7 | overly_specific | CONFIRMED | Revised in round 3 |
| FC10–12 | round 3 | "its label"; Griffin second fund; R196 | R37; OE 39 | 2.1 | not_self_contained | CONFIRMED | Restructured in round 4 |
| FC13–14 | round 4 | R196 "nothing or 0"; R2 "(a separate row for the other fund is expected)" | Carta 1847333272519888206; ENG-2438 comment | 2.7 | overly_specific | CONFIRMED | Rows 2 and 196 need your own rewrite |

Effect on verdict: Overall Rubric Quality fails on one Major row (row 2: non_atomic and not_self_contained, with Minor overly_broad absorbed). Criteria Weights PASS 5. All other dimensions PASS 5.

Platform defects: none

### FINAL VERDICT: FAIL
Score: 1
Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
Execution status: COMPLETE
Review policy: rubric-revision-v10
Review mode: AUDIT
Reviewed JSON SHA-256: 3e26332066b3477dfb82c4c4b9a1bbffd65f71f0ca74ec697a5eadd1db67580a
Review context SHA-256: 5dbd1fe5d8a83ecf83c2d2552877d5d60f084631be72fc78b3b2abc0d9c8638a
Scoring record SHA-256: 41a038a5b028755985738a8e3d178072681186a190c91f04782c247cc9fcd834
Eval version: task-quality-v1
Eval release SHA-256: 56292d5d69c9e3fcb2ecc44ea7b0fb5a8fdf3e7aa1026fa9da6fb9472960e631
Gate tier: localized
Coverage ratio: 201/201
Repairs: See findings
Evaluator model: Opus 5.5 (claude-opus-5-5)
Next action: Replace row 2 as in the Fix List (or trim SQL line 22 upstream), then send /rubric again
Evidence limits: None
