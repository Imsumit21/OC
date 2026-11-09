## RUBRIC EVALUATION REPORT

- Attempt: 6aed9d01a1cb8067d8ac7dee (chat /rubric, run 2, DELTA mode)
- Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
- Inputs: rubric `09_Rubrics (2).json` (195 rows), prompt, assignment, injection SQL (rev 6), Oracle Events (rev 10)

### Task: Stockholder/option-holder close-out (holder sheet, investor letter, 14 holder note drafts, Linear states and comments, Griffin heads-up, #winddown reply, KPMG confirmation)
### Persona: Leonard Hayes - Co-founder & Creative Director
### Total Rubrics: 195 (Outcome: 194, Process: 1)

## Fix List

| Row | What is wrong | Fix to copy | Mark |
|---|---|---|---|
| 2–8 | The draft sheet's seven stale "copied from the Nov 2024 list" rows are graded twice: row 2 grades them, and the "Nov 2024 figure … fails" clauses in rows 3–8 fire on the same rows. One miss (leaving the old rows, or updating them in place but keeping an old figure) fails up to seven rows. We tried four ways to fix the wording. Dropping the clauses lets an old figure kept beside the right one pass. Narrowing them to "the same row" fails a correction note. "Given as the holding / naming it as the old figure passes" can't be graded on the stale rows, because their own Notes cell names the figure. Moving the check into row 2 wrongly fails TOR's row (its old 50,865 is also its correct holding). | **This row needs your own rewrite.** The open problem: no wording keeps the stale-row check in one row without either re-creating the cascade or failing a valid sheet. Cleanest route: settle it upstream. Make the draft sheet (SQL line 22) hold only its header row, or only the TOR row. Re-run /injection and /prompt, then delete row 2 and drop the fail clauses from rows 3–8, so each just states the holding. Also check the hint the stale grid gives: it is one of the task's traps, so decide whether you still want it. | revised after check |
| 53 | "a different option total or share total shown beside them fails" also fails a correctly labelled extra figure (KPMG's as-of-Dec-31 243,757 options) | The Agent shows total shares and options outstanding of 9,215,993 on its holder sheet (as that one total, or as 164,114 options shown apart from 9,051,879 shares, the shares given as one figure or as 6,000,000 common plus 3,051,879 Series Seed; another figure given as today's option or share total fails, including the term sheet's 268,772 options) — same change in the Accept text | checked |
| 84 | Weight 5, but the closing line in Calvin's note rests on the same "not yet told" check as rows 79–83 (weight 3); the extension that keeps his line live is graded by rows 21, 41, 71 and 145 | Weight 3. Justification: "Interpretation: no founder has written to Calvin about the closing, so the notes' rule (the closing if they have not been told) puts it in his note." Evidence: add the ENG-2452 comment ('No mail with that address before Feb') and the notes' "Told means …" sentence | checked |
| 178 | Closed name list misses the names Carta and Leonard's mail use for the ES-15 holder | The Agent reports ES-15 (Brian Foster, Brian, [PERSON_NAME_0092], [PERSON_NAME_0093], [PERSON_NAME_2769] [PERSON_NAME_0093], Ömer [PERSON_NAME_0093], Omer [PERSON_NAME_0092] [PERSON_NAME_0008] or [PERSON_NAME_45917] [PERSON_NAME_0093], the names ENG-2460, Carta and Leonard's mail give the holder) at 3,391 options as of December 31, 2025 in its answer to KPMG (by holder name, with or without the ES number; 10,173 fails) | checked |
| 179 | Misses "EMPLOYEE_0032 [PERSON_NAME_0011]" (Carta's ES-16 notice) and the names Leonard's mail gives the cameron@ address | The Agent reports ES-16 ([PERSON_NAME_2768] [PERSON_NAME_0011], EMPLOYEE_0032 [PERSON_NAME_0011], PERSON_0031_NAME, [PERSON_NAME_0120] or [PERSON_NAME_0121], the names Carta and Leonard's mail give the holder, or Cameron, from the ENG-2461 address cameron@harmonygames.co) at 10,384 options as of December 31, 2025 in its answer to KPMG (by holder name, with or without the ES number; 0 or a blank fails) | checked |
| 180 | Misses the names Carta's Oct 23, 2024 digest and Leonard's mail use for the ES-17 holder | The Agent reports ES-17 ([PERSON_NAME_0038], [PERSON_NAME_0036] [PERSON_NAME_0005], [PERSON_NAME_0036] or Ryan, the names ENG-2462, Carta and Leonard's mail give the holder) at 34,439 options as of December 31, 2025 in its answer to KPMG (by holder name, with or without the ES number; 34,409 fails) | checked |

For rows 178–180, update each Accept text to the same name list and add the cited threads to the evidence.


---

### Phase 1: Structural Validation
- Five-field completeness: 195 of 195; Outcome 194, Process 1; weights all 1/3/5.
- Requirement coverage: 195 of 195 (each row one outcome; the one-draft-per-holder gap from run 1 is closed by "a draft of its own" in rows 65–78).

### Phase 2–3 summary (target rows)
- Facts: every value in the 67 target rows was re-bound to its record. Row 53: 9,051,879 shares (6,000,000 + 3,051,879, term sheet) + 164,114 options (60,350 on nine live Carta lines + 103,764 on the four advisor grants) = 9,215,993. Row 179: ENG-2461's address is cameron@harmonygames.co (injection SQL). Rows 3/4/172/173: Leonard's copy of the purchaser schedule (thread 1771880236343640719) shows "[ORGANIZATION_NAME_0151] II, L.P." and "[ORG_NAME_0153] II Side Fund, L.P.". Row 2: Sheet1 of the draft holds exactly seven "copied from the Nov 2024 list" rows. No value mismatch.
- Atomicity: no non-atomic row. Row 53 is one reported total: Sunset asks for one line, "Total shares and options outstanding", and the split form states the same total.
- Acceptance: the fund-name tokens and both readings of Sunset's totals line are accepted. Row 53's fail clause and the KPMG name lists in rows 178–180 reject record-backed answers. The row 126 lint hit ("without saying") is an optional extra, not absence acceptance.
- Overlap: one cascade group (rows 2–8, below).
- Weights: one row one level high (row 84).
- Negative Criteria, Agent-centric phrasing, Process (row 188 meets the three-condition test): clean.

### Phase 4: Issue Tally
| Severity | Rows | Fails when | Status |
|---|---|---|---|
| Major | 4 (rows 53, 178, 179, 180) | any | FAIL |
| Moderate | 1 overlap group (rows 2–8) | any | FAIL |
| Minor | 0 | ≥5% | PASS |

### Phase 5: Scoring
| Sub-Dimension | Score |
|---|---|
| Overall Rubric Quality | 1 |
| Criteria Weights | 4 |
| Rubric Category Balance | 5 |
| Process Rubrics | 5 |
| Agent-Centric Phrasing | 5 |
| Negative Criteria | 5 |
| Predicted All-Fail gate | PASS |

## Changes Since Last Run

- Rows: 108 locked, 20 locked-checked-fix (exact copies of last run's checked fixes), 56 edited, 1 new (row 195), 10 re-checked (rows 16–20, 22–26), 1 removed (old row 54, the separate option total, now inside row 53; your new row 54 is last run's row 196).
- **Previous findings now fixed:** the over-sampled shares, options and last-day columns (now complete: 12, 13 and 9 rows); rows 12–15 (now "with or without the word vested; a vested figure lower than … fails", which closes last run's open rewrite); rows 53/54 (merged row 53 takes Sunset's "Total shares and options outstanding" as one total or as shares and options apart; it is one reported total, so it is atomic); the one-draft-per-holder gap (rows 65–78 "of its own"); rows 112, 118, 157–161, 172, 173, 177, 181, 183 and 188–195 as checked. Row 126's "sold outright" and row 179's "Cameron" are fine as far as they go.
- **Dismissals:** none recorded.
- **New scored findings:** the stale-row cascade, rows 2–8 (Moderate overlap group, R4); row 53's fail clause (Major overly_specific, R1); rows 178, 179 and 180 closed name lists (Major overly_specific, R1 and fix-check R1); row 84 weight one level high (R4).

### Notes for QM (not scored)
- The letter's "Holders" outline section has no row (R3, unchanged gap; last run rejected it because only an absence could grade it).
- Row 92 (locked) still says "31,536 as shares fails" in the draft note, which a correction note naming the old figure could trip.
- Row 181 accepts "Husnu Matthew Collins" and row 177 "Marcus Bennett"; Carta also says "Matthew Collins", and Marcus's display name is "marcus". A judge will very likely read these as the same names.
- ENG-2442's address PERSON_0693_EMAIL appears as the personal address in "patrick"'s signature (thread 1770053656612413311), while Patrick Lewis (ENG-2444) is Covered by the family note. If they are the same person, "at most one note per person" may bite. This is a data question for /prompt, not a rubric value.
- Row 4 (in the stale-row group): a run that copies ENG-2439's combined "2,746,693, both funds on one line" beside 84,438 would pass. Unlikely.

### Rejected findings
- R5 (DR1–DR4, first pass): content rows "on its holder sheet / in its draft note / in its investor letter / in its answer to KPMG" don't repeat the destination. Rejected: §3.1 "Write result vs write content" is the documented split, and the destination is graded by rows 1, 65–78, 115–116 and 169. Embedding it in every content row would create the cascade §3.3 forbids.
- R1 DR1 (row 118 locks the metrics reason): the draft's reason sentence gives two reasons, each with its own row (118 metrics, 119 insolvency). A letter dropping one omits draft content; it isn't a different valid answer.
- R1 DR2 (row 74 bounced address fork): settled by Leonard's Feb 13 notes, written after the Feb 11 bounce in his own mailbox: "Messages go to the email on each holder's issue." Same as last run.
- R4 DR3 (row 71 weight 1): QC weight example "Sending to an address found in Contacts, even when it is the point of the task" is 1.
- Fix-check R7 (row 2 bundles seven rows): rubric_flow_v2 "Spreadsheet rows and cells keep the table spot-check rule"; the first R7 pass judged it one artifact state.
- Fix-check R4 (rows 1/2 cascade on a new-file run): row 2 grades its own write on the draft, which a new-file run never makes. The offered fix ("its sheet carries none of the old rows") is absence acceptance, which fails Negative Criteria (§2.9).
- Fix-check R1 DR6 (round 1, TOR row in place fails row 2's "overwrites"): rewriting the row's cells is an overwrite. This concern resurfaced in round 4 against a different wording, where it held.


## Deep Recheck

Passes: R1, R2, R3, R4, R5, R6, R7 on the 67 target rows (R4 against all 195), Opus 5.5, each blind to the main review. Fix-check: round 1 (seven passes), round 2 (combined seven-topic pass), round 3 (rows 3, 5–8), round 4 after restructure (rows 2–8), plus two rounds on rows 178–180.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| R1 | 67 | 4 | 2 |
| R2 | 67 | 0 | 0 |
| R3 | 195 | 0 | 0 |
| R4 | 67 vs 195 | 3 | 2 |
| R5 | 67 | 4 | 0 |
| R6 | 67 | 0 | 0 |
| R7 | 67 | 0 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | R4 | R2 "seven old rows of the draft sheet" with R3–R8 "… fails" clauses | SQL line 22, Sheet1 of f_5ecaa967db3adcfa440b09 | 3.3 | duplicate | CONFIRMED | Stale rows carry exactly the figures R3–R8 say fail |
| DR2 | R4 | R84 weight 5 | R79–R83 weight 3; R84 justification copies R41's | 2.12 | weight | CONFIRMED | Closing line rests on the untold check |
| DR3 | R4 | R71 weight 1 | QC C18 example | 2.12 | weight | REJECTED | Address lookup is weight 1 |
| DR4 | R1 | R118 metrics reason | DRAFT C0ADGSZKR3R/1770664700.848759 | 2.7 | overly_specific | REJECTED | Both draft reasons have rows |
| DR5 | R1 | R74 issue address | NOTES f_a37b403d5200d4f0a31d31 | 2.8 | masks_decision_fork | REJECTED | Feb 13 notes fix the address |
| DR6 | R1 | R53 "shown beside them fails" | KPMG 1857029474983245439 | 2.7 | overly_specific | CONFIRMED | Labelled as-of figure is true |
| DR7 | R1 | R179 name list | Carta ES-16 1847333318158821452 | 2.10 | overly_specific | CONFIRMED | "EMPLOYEE_0032 [PERSON_NAME_0011]" |
| DR8–11 | R5 | content rows "its holder sheet" etc. | rows 1, 65–78, 115–116, 169 | 3.1 | overly_broad | REJECTED | Write row / content row split |
| FC-R1 | R1 | R178, R180 name lists | Carta digests 1813700131573811805, 1813881602779637554 | 2.10 | overly_specific | CONFIRMED | Second name forms in Carta |

Effect on verdict: Overall Rubric Quality fails on four Major overly_specific rows (53, 178, 179, 180) and one Moderate overlap group (rows 2–8); Criteria Weights NON-FAIL 4 (row 84).

Platform defects: none


### FINAL VERDICT: FAIL
Score: 1
Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
Execution status: COMPLETE
Review policy: rubric-revision-v10
Review mode: AUDIT
Reviewed JSON SHA-256: deca07e55ab0dfd60f661d26bac07550139a3b7caa0b14db49f24cc3c6cd67ab
Review context SHA-256: 2e1e55e6c9a663d4b9397084c34066feafe57bcca4dacefaa2b56f10fa345a7b
Scoring record SHA-256: ede10a08c473c21c0518fac002151eed4d1d2a9c0e53f59f63a9225bc6b7c4aa
Eval version: task-quality-v1
Eval release SHA-256: 56292d5d69c9e3fcb2ecc44ea7b0fb5a8fdf3e7aa1026fa9da6fb9472960e631
Gate tier: localized
Coverage ratio: 195/195
Repairs: See findings
Evaluator model: Opus 5.5 (claude-opus-5-5)
Next action: Apply the checked fixes for rows 53, 84, 178, 179 and 180; settle the stale draft-sheet grid upstream (SQL line 22) and rewrite rows 2–8; then send /injection, /prompt, /hardness, /oe and /rubric again if the SQL changes (only /rubric if it does not)
Evidence limits: None
