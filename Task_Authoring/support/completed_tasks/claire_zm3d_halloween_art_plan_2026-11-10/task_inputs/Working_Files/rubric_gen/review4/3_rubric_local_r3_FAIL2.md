## RUBRIC EVALUATION REPORT

### Task: ZM3D Halloween art plan: calls, owners and dates for 62 live surfaces, a plan doc and tracker, 58 ART ticket comments, assignments, new store tickets and a thread reply
### Persona: Claire Morgan - Art Lead
### Total Rubrics: 183 (Outcome: 183, Process: 0)

Run mode: DELTA (`hg_rubric_ledger.py plan`). 6 target rows reviewed in full, 6 locked as checked fixes, 171 locked.

## Fix List

The candidate is `Evals/task_inputs/fixcheck/rubric_candidate.json` (181 rows). Row numbers below are your rubric's. Copy each whole row from the candidate, and delete R42 and R170. After those deletions, old R43 to R169 become R42 to R168, and old R171 to R183 become R169 to R181. Every row not listed stays as it is.

- R23, R24 (locked, not scored, optional): The Accept line counts tracker rows, so a tracker with several tabs can fail it. Copy the Accept line: "exactly 14 surfaces carry the call Halloween version in the tracker; a surface on several tabs counts once." R24 is the same with 10 and Skip. (checked)
- R25 (locked, not scored, optional): The same Accept fix with 36 and Refresh first. The evidence also says "the 31 running tickets"; 41 running tickets predate the swap, and 31 is the working ones. Copy the evidence. (revised after check)
- R41: Same "ad rows" wording as R42. Copy the Accept line: "exactly 30 ads carry a final due date on or before Oct 10, 2025, in any date form; an ad on several tabs counts once." (revised after check)
- R42: Delete. It is the mirror count of R41, so one ad on the wrong side of the line fails both, and its Accept line counts rows. R41 stays as the one count row on that column. (revised after check)
- R47: The Accept line counts rows, and the call in the title makes a wrong call fail this owner row. Copy: "The Agent names Marcus Bennett (or Marcus) as the maker or owner on exactly 42 ads in its tracker, apart from ART-806, ART-811, ART-813, ART-820, ART-821, ART-822, ART-824, ART-842, ART-844 and ART-849", with the new Accept line. (checked)
- R169: R169 and R170 are mirror counts, and a Skip guard needs only one row. Copy: "The Agent comments a final due date on or before Oct 15, 2025 on exactly 48 ad tickets, every ticket in ART-793 to ART-835 and ART-840 to ART-854 except ART-806, ART-811, ART-813, ART-820, ART-821, ART-822, ART-824, ART-842, ART-844 and ART-849 (any date form)". (revised after check)
- R170: Delete; R169 now does its job. This also ends the "ART tickets" problem, where a date on a new store ticket counted. (revised after check)
- R171: Keep the title; it stays the one wrong-target row for assignment. Copy the evidence, which adds the Trello comment, cmt_art831_2 and Robert's reply. (revised after check)
- R172: An extra ART-849 failed this row and R171 together. Copy: "The Agent assigns exactly 6 ad tickets to Julia Lawson (julia.lawson@harmonygames.co): ART-825, ART-826, ART-827, ART-828, ART-829 and ART-830, apart from ART-849", with the new evidence. (revised after check)
- R173: The bare count passes with 4 wrong tickets. Copy: "The Agent assigns exactly 42 ad tickets to Marcus Bennett (marcus.bennett@harmonygames.co) out of ART-793 to ART-835 and ART-840 to ART-854, apart from ART-806, ART-811, ART-813, ART-820, ART-821, ART-822, ART-824, ART-825, ART-826, ART-827, ART-828, ART-829, ART-830, ART-842, ART-844 and ART-849", with the new evidence. (revised after check)

Your rows carry the text the last Fix List gave, and you copied it correctly. R170 to R173 are defects in that text, and R42 and R47 are older wording last run's review did not catch.

---

### Phase 1: Structural Validation
- Five-field completeness: 183 of 183
- Category distribution: Outcome 183, Process 0
- Requirement coverage: 183 of 183 outcomes (R171 now holds one, so the count drops from 184)
- Code checks: `hg_rubric_lint.py` returned 0 hits on the rubric and 0 on the final candidate.

**The claim that the rubric is byte-identical to the last candidate: not true as stated, and true in content.** The saved file is 167,920 bytes, SHA-256 46ba6397; the last candidate was 170,115 bytes, SHA-256 801bcef4. The file was reformatted: 1-space JSON indent and a trailing newline, not 2-space with none. Parsed, all 183 rows match in order in all five fields, and re-serialising the candidate with a 1-space indent and a newline reproduces the saved bytes exactly. So nothing else changed, and the plan's 6 edited rows are the 6 marked `revised` and its 6 checked-fix rows are the 6 marked `checked`.

**Values.** I rebuilt all 58 tickets from a static parse of the saved SQL, not from the OE, the rubric or the facts extract: campaigns from the ticket comments, less the two cuts Frederick took off iOS UK tablet, then the deadlines and Leonard's split. The result is 10 Skip, 48 working, 30 due Oct 10, 18 due Oct 15, 6 Julia, 42 Marcus, and calls of 36, 12 and 10. It matches the extract with 0 differences, and it matches every value on the 12 changed rows. A script checked the 106 comment rows, R6 to R10, R32 to R40 and R43 to R46 against it with no mismatch. Every quote and record id in the 12 changed rows' evidence exists in the SQL. Pass R2 recounted separately and found no wrong value in any title.

### Phase 2: Per-Rubric Quality

Issues are listed under Issues Found. Target rows R42, R47, R170, R171, R172 and R173 had the full review. The six checked-fix rows had a fact review only, and it found no factual error.

Atomicity: each target row grades one result. Named sets on R171 and R172 are scope conditions the flow allows; see Z1 and Notes for QM.

Over-specificity triage: `overly_specific` on R42, R47, R170; `overly_broad` on R173; the rest valid.

### Phase 3: Set-Level Quality
- Coverage gaps: none scored.
- Scope checklist: doc and tracker create, R1, R21. Shares, R48 to R59 with guards R60, R61. Comments, R63 to R168 with guards R62, R169, R170. Assign, R171 to R178. New tickets, R179, R180 with guard R181. Slack reply, R182, R183.
- Process audit: 0 of 0. The prompt holds no ordering dependency an Outcome cannot see.
- Duplicates / overlap / cascade groups: four, listed as C4 to C7. All four involve a target row. The same mirror pattern on R23, R24 and R25 alone is locked and goes to Notes for QM.
- Spot-check groups: tracker call 5 samples with R23 to R25; tracker due 4 with R41, R42; tracker owner 4 with R47; assign 5 with R171 to R173. Each group has a count control; the number of controls is part of C4 and C5.
- Contradictions: none. Final-reply test: ACCEPT, no row grades the reply. OE cross-check: every row maps to OE steps, 0 unmapped, 0 conflicts.

### Phase 4: Issue Tally
| Severity | Count | % | Fails when | Status |
|---|---|---|---|---|
| Major | 4 | 2.2 | any | FAIL |
| Moderate | 4 | 2.2 | any | FAIL |
| Minor | 0 | 0 | over 10% | none |

### Phase 5: Scoring
| Sub-Dimension | Score | Justification |
|---|---|---|
| Overall Rubric Quality | 2 | 4 rows at Major (R42, R47, R170, R173) and 4 overlap groups at Moderate |
| Criteria Weights | 5 | All 183 rows at the expected weight |
| Rubric Category Balance | 5 | 183 Outcome rows |
| Process Rubrics | 5 | No Process rows, none needed |
| Agent-Centric Phrasing | 5 | Every title opens with The Agent and names no tool |
| Negative Criteria | 5 | No prohibition title; every row fails an idle Agent |
| Predicted All-Fail gate | PASS | 0 rows predicted |

**Lowest Sub-Dimension:** Overall Rubric Quality - 2 - Major issues on four rows, and four overlap groups.
**Summary:** Every value is right, and all seven findings from last run are fixed. The rubric fails on acceptance wording and on count rows that overlap, not on facts. The main defects are Accept lines that count tracker rows where the title counts ads, and a Marcus row whose bare count passes with 4 wrong tickets.

### Issues Found
| # | Row | Issue | Severity | Type |
|---|---|---|---|---|
| C1 | R42, R47 | The titles count ads and the Accept lines count ad rows. R22 allows 'one tab or several'. A tracker with one tab per campaign has the right 18 ads on 27 rows and the right 42 on 72, so it passes the titles and fails the Accept lines. R1 proposed Minor; the decision rule makes a rejected valid answer Major. | Major | overly_specific |
| C2 | R170 | 'ART tickets' counts a new store ticket. All 18 ad comments right plus 'due Oct 15' on the new iPad ticket, a date R13 and R14 accept, makes 19. Narrow reach: an unrequested comment, dated inside Martin's vacation. The decision rule has no reach test, and B3 to B5 were scored the same way. | Major | overly_specific |
| C3 | R173 | Bare count, no ticket named. Marcus on ART-811 and ART-813 and off ART-808 and ART-816 gives 42 + 2 - 2 = 42, two designed traps, one miss each. | Major | overly_broad |
| C4 | R171, R172, R173 | R171's 48 is R172's 6 plus R173's 42, each with an exact scope. ART-849 to Julia fails R171 and R172 on one exclusion; ART-806 to Marcus fails R171 and R173. | Moderate | duplicate |
| C5 | R41, R42 | Mirror counts on one tracker date column. ART-793 dated Oct 15 gives 29 and 19 and fails both. | Moderate | duplicate |
| C6 | R169, R170 | The same split on the ticket comments. | Moderate | duplicate |
| C7 | R24, R25, R47 | R47's population is the call column. ART-793 marked Skip with Marcus kept on the row has a right owner cell, yet R47 fails with R24 and R25. | Moderate | duplicate |

Rows count once at their highest severity. R173, R42, R170 and R47 count at Major, so each group contributes one Moderate through its remaining rows.

### Recommended Fixes
Every fix is in the candidate and marked in the Fix List. Checks passed: `hg_rubric_lint.py` on the candidate, a self-check of each changed row, and one R1-R7 run on the first candidate's changed rows (R3 whole rubric, R4 against all rows).

1. C1: Count ads, once each, on R47; R42 goes with C5.
2. C2: The merged R169 lists its tickets, so store tickets drop out.
3. C3: Name the 42 as a closed population on R173. Not one of them can be swapped out and still pass.
4. C4: Keep R171 as the only row that fails a wrong-target write, and scope R172 and R173 so an extra ticket does not count there. A witness table on the revised rows gave: ART-849 to Julia, ART-806 to Marcus, ART-806 to Frederick and ART-836 to Martin each fail R171 alone; Martin on ART-825 fails R172 alone; Martin on ART-832 fails R173 alone. An unassigned ticket fails R171 and its person row, which is a write row plus its content row.
5. C5: Delete R42. R41 remains with four samples.
6. C6: Merge R169 and R170 into one named guard with the Oct 15 bound.
7. C7: Define R47's population by ticket id, not by call. This also closes the trap pair on that row: it now counts 40.

Non-failing repairs, no tally: the citation gaps R2 found on R42, R47, R170, R171, R172 and R173, and on R25 and R41 in the fix check. No value is wrong; the evidence omits a record the count depends on. Row R25's 'running' is a wording error a judge would read correctly (QC Appendix B12).

**Fix check results.** R1-R7 ran once on the first candidate (9 changed rows) and raised 22 findings: 9 taken up, 13 not. The first candidate had deleted old R171; R3 showed that left no row failing a third person on a Skip or Archive ticket, which was a regression I introduced, so old R171 is back and R172 and R173 changed instead. R42 was first rewritten as a 48 count, and R4 and R5 showed that still left a smaller cascade, so it is deleted. R169 gained its ticket set and date bound. Revised rows had lint and a self-check again, not a second R1-R7 run, as the flow says, so run 4 reviews them. R23, R24 and R47 are `checked`; R25, R41, R169, R171, R172 and R173 are `revised after check`.

| Pass | Findings | Taken up | Not taken | Main outcome |
|---|---|---|---|---|
| R1 | 0 | 0 | 0 | None on 9 rows |
| R2 | 5 | 4 | 1 | No wrong title value; citation and wording repairs on R25, R41, R172; R23 to Notes |
| R3 | 4 | 1 | 3 | Third-person guard restored; the rest Z6, Z7 and Notes |
| R4 | 5 | 1 | 4 | Residual cascade on nested R41 and R42; R23 to R25 to Notes; the rest Z3, Z10 |
| R5 | 7 | 2 | 5 | R42 dropped, R169 names its set; the rest Z2 and the 'very unlikely' exception |
| R6 | 1 | 1 | 0 | R169 gained its date bound |
| R7 | 0 | 0 | 0 | None, with a judgment note on named sets; see Notes for QM |

## Changes Since Last Run

**Row counts.** Locked 171. Locked checked fix 6 (R174 to R178, R181). Edited 6 (R42, R47, R170 to R173). New 0. Re-checked 0. Removed 6 by the ledger's count, but no row is gone: the helper lists the old text of the six checked-fix rows as removed.

**Previous findings.** B1 to B7 are all fixed: R171's title no longer names a person, so B1 and B2 close; the Accept lines take address, name or user id (B3) and grade the state after the last assignee write (B4); R181 takes any number of tickets (B5); R172 says ad tickets (B6); R170's justification counts final due dates (B7). Their fix text is what C2, C3 and C4 now find fault with. Row by row, each of the 12 rows matches the candidate.

**Dismissals.** None new. A1 and A2 stay closed; their rows are locked and unchanged.

**Two rulings reversed from last run**, as coherent_record R1 requires, with the earlier error and a counterexample.
- Y5 on R173: last run rejected this count as 'One output-volume criterion per sampled output'. R171 is already that row for the assign output. R173 is the only check of the person on 38 tickets, and last run's own A1 and A2 ruling says spot-check permission is for tables, not separate writes. Counterexample in C3. Y5 still stands for R42 and R47 on the tracker, which is a table.
- Y4 on R171 to R173: last run rejected the overlap by quoting 'removing either row changes the score'. That sentence sits with the write-row and content-row carve-out, and the override's own example of seven content rows would fail it too. Counterexample in C4.

**New scored findings.** C1 to C7.

### Notes for QM (not scored)
- **Named sets, closest call.** R7 raised R171 and R172 as Major `non_atomic`, and I rejected both on Z1. The closest case against that is QC's task ...2ec9b: 'these are three Independent actions, if the agent correctly updated one or two of them it still fail the rubric'. The fix-check R7 returned none but said that if R7's exception list is read as closed, these rows become Major. A bare count is the alternative, and C3 shows why that fails, so QM has to pick which rule wins.
- **Reuse sets.** R3 raised dates for the iPhone 6.5" and Google Play sets again, twice this run; five blind passes have now raised it. OE 36, OE 38 and OE 40 give those sets a date route and no row grades it. If QM reads 'by when' as reaching store go-live, add tracker date rows for both sets.
- **Julia on the tracker.** R3 raised this twice. R43 and R44 sample two statics and no count covers Julia, so a tracker with Martin or nobody on ART-827 to ART-830 passes every row. It sits inside the sampling limit. A Julia count row would close it.
- **R23, R24, R25.** Mirror counts like C5, and bare counts R5 can cancel: 36 - 2 + 2 = 36 is a moderate path. All are locked titles, so they are not scored. One call-volume row would close it. R25 is `revised after check`, so run 4 reviews it in full and this could then score.
- **Dropping R42.** Tracker dates for the 18 Oct 15 ads then rest on R39, R40 and the per-ticket comment rows. That fits 'five samples plus one volume criterion', but it is less coverage than today.
- **R41 and R47.** Bare counts can still cancel on a hand-built swap: ART-812 for ART-830 on R41, and ART-828 for ART-832 on R47. R5 rated both low.
- **R181.** No row fails a run that also opens a new ART ticket for ad work. Old gap, and the prompt does not state it outright.
- **R23 evidence.** The Store tab has no call column, so 2 of the 14 rest on Robert's reply and the Store folder, which R26 and R27 cite and R23 does not.
- **Standing notes from last run.** The R63 to R168 share of the weight, R60 and R61 failing an extra share, and 'Marcus' fitting Marcus Lee are unchanged.
- **Helpers.** `hg_rubric_ledger.py` reads a verdict key the scoring record never holds, so the plan shows `previous_verdict: null`. Its `diff` matches by position and title, so it can label a moved row wrongly.

## Deep Recheck

Passes: R1, R2, R3, R4, R5, R6, R7, Opus 5.5 (claude-opus-5-5), effort level not reported to this session; subagents started with no model override, so they inherit it, not independently confirmed, each blind to the main review. Target rows only (R3 whole rubric, R4 against all rows). One fix check ran after them on the candidate.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| R1 | 6 rows | 3 | 3 |
| R2 | 6 rows | 4 | 4 |
| R3 | 183 rows | 2 | 0 |
| R4 | 6 rows against all 183 | 4 | 4 |
| R5 | 6 rows | 5 | 1 |
| R6 | 6 rows | 5 | 4 |
| R7 | 6 rows | 2 | 0 |

Rejection grounds, each a quoted rule:
- Z1: rubric_flow_v2 scope checklist, 'as a count or scope condition on the required write ("comments on exactly these 6 tickets")'. This also settles the conflict with R5: the rule R7 would apply leaves a bare count, and Eval 2.7 says 'name the value'. The side not taken is in Notes for QM.
- Z2: QC Appendix C2, 'For large audit tables, use overall total checks plus spot checks instead of one rubric per row'; Eval 3.6, 'One output-volume criterion per sampled output (the exact count or total)'.
- Z3: common_errors 7.8, 'A count on a write the Agent must make. With a row for each review that must close, a run that also closes ENG-123 fails it'.
- Z4: Eval 2.2, 'Quantifier, disjunctive or compound phrasing over independently gradable items', which took the person out of R171 as B2. Who gets each ticket is graded on R172 and R173.
- Z5: Eval 2.6, 'Outcome is the default: the final state, what exists, what was sent'. The Accept line states the reading an Outcome title already has.
- Z6: rubric_flow_v2, 'A coverage gap that no change caused goes to `### Notes for QM` unless the prompt states that requirement outright.'
- Z7: rubric_sampling, 'Reviewers record that limit instead of inventing an independent missing-criterion issue for each eligible unsampled cell.'
- Z8: `rubric_review_record.md` is headed 'Historical rubric creation record (retired)' and says 'this document has no operational authority', so its quotes carry no finding.
- Z9: Eval 3.3, 'Not duplicates: ... an aggregate control versus its atomic spot checks.'
- Z10: Eval 3.3, 'Rows that merely share a likely model root cause are not a group', and 'for each plausible single Agent error'.

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | R1 | R42 'exactly 18 ad rows carry' | R22 'on one tab or several'; cmt_art816_1 | 4, 7.2 | overly_specific | CONFIRMED | C1, 27 rows recomputed; raised from the proposed severity by the decision rule |
| DR2 | R1 | R47 'exactly 42 ad rows with' | R22; cmt_art793_1 | 4, 7.2 | overly_specific | CONFIRMED | C1, 72 rows recomputed |
| DR3 | R1 | R170 'exactly 18 ART tickets' | R14; R171 Accept | 4, 7.2 | overly_specific | CONFIRMED | C2 |
| DR1 | R2 | R172 evidence | Trello 68dc65a0f2d7fb28743f5860 | 4 | cited record | CONFIRMED | Non-failing repair; Unity tab lacks ART-826, no value wrong |
| DR2 | R2 | R42, R170 evidence | Trello 68dc65a0f2d7fb28743f5860 | 4 | cited record | CONFIRMED | Non-failing repair |
| DR3 | R2 | R47, R173 evidence | cmt_art831_2 | 4 | cited record | CONFIRMED | Non-failing repair |
| DR4 | R2 | R171 justification | Trello action and cmt_art831_2 | 4 | cited record | CONFIRMED | Non-failing repair |
| DR1 | R3 | Prompt 'who makes what by when' | f_fdd6d2d2f4a4d2f5b908fb | 7.1 | missing_coverage | REJECTED | Z6; Note for QM |
| DR2 | R3 | R43, R44, R47 | ART-827 to ART-830 | 7.1 | missing_coverage | REJECTED | Z7; Note for QM |
| DR1 | R4 | R171, R172, R173, R174, R178 | ART-849, cmt_art849_1 | 5, 7.7 | duplicate | CONFIRMED | C4 on R171 to R173; R174 and R178 out on Z9 |
| DR2 | R4 | R41, R42 | C0880U9751A/1759275738.984915 | 5 | duplicate | CONFIRMED | C5; R37 out on Z9 |
| DR3 | R4 | R169, R170 and 18 due rows | cmt_art805_1 | 5 | duplicate | CONFIRMED | C6 on R169 and R170; the 18 rows out on Z3, and its first quote on Z8 |
| DR4 | R4 | R47, R24, R25 | R47 Accept | 7.7 | duplicate | CONFIRMED | C7 |
| DR1 | R5 | R173 'exactly 42 ad tickets' | cmt_art811_2; C08R8CHB0QL/1759248337.170599 | 4, 7.7 | overly_broad | CONFIRMED | C3, 42 recomputed; reverses Y5 for this row |
| DR2 | R5 | R47 | mail 'Unity retention restart' | 4, 7.7 | overly_broad | REJECTED | Z2; the C7 fix also closes it |
| DR3 | R5 | R42 | 68d6cff0c6568da5d9c8e81f | 4, 7.7 | overly_broad | REJECTED | Z2; R5 rated it low |
| DR4 | R5 | R170 | R170 justification | 4, 7.7 | overly_broad | REJECTED | Z3; every working ticket has its own due row |
| DR5 | R5 | R171 | C06DJBJL798/1759269913.882683 | 7.7 | overly_broad | REJECTED | Z4 |
| DR1 | R6 | R42 Accept | R22 | 7.5 | overly_specific | CONFIRMED | Merged into C1 |
| DR2 | R6 | R47 Accept | R22 | 7.5 | overly_specific | CONFIRMED | Merged into C1 |
| DR3 | R6 | R170 'ART tickets' | R13 Accept | 7.5 | not_self_contained | CONFIRMED | Merged into C2, typed overly_specific as a rejected valid answer |
| DR4 | R6 | R173 'exactly 42 ad tickets' | ART-836 Canceled | 7.5 | not_self_contained | CONFIRMED | Merged into C3 |
| DR5 | R6 | R171 to R173 Accept | catalog linear_update_issue | 7.5 | not_self_contained | REJECTED | Z5 |
| DR1 | R7 | R171 | catalog linear_update_issue; L195 | 7.4 | non_atomic | REJECTED | Z1; its rubric_review_record quotes on Z8 |
| DR2 | R7 | R172 | L320 Trello action | 7.4 | non_atomic | REJECTED | Z1; its rubric_review_record quotes on Z8 |

Effect on verdict: changed. The first save, from my own review, was PASS with score 5; I had found none of these. The recheck moved Overall Rubric Quality to FAIL with score 2 on C1 to C7. No other dimension changed.

Fix check: R1-R7 ran once on the candidate and raised 22 findings, 9 taken up and 13 not; six rows are marked revised, see Recommended Fixes.

Platform defects: none

### FINAL VERDICT: FAIL
Score: 2
Execution status: COMPLETE
Review policy: rubric-revision-v10
Review mode: AUDIT
Reviewed JSON SHA-256: 46ba639729a29388345183419c2983bfb9351b427c49228f583e148be33a6d7c
Review context SHA-256: 8a84bbf098f6bf100356f6fe85af201c7112d039603b6b361033ac1e4ae5408c
Scoring record SHA-256: 04b5ed4140ce372e8857f40c11cd2402c01b390b37655a0727223d0c7227902d
Eval version: task-quality-v1
Eval release SHA-256: c5b89f4c40a7902f968001f1aa6c710d47bf203842455bbe8dbb668ec7c8943b
Gate tier: localized
Coverage ratio: 183/183
Repairs: See findings
Evaluator model: Opus 5.5 (claude-opus-5-5), effort level not reported to this session; subagents started with no model override, so they inherit it, not independently confirmed
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Next action: Copy the Fix List rows from the candidate, delete R42 and R170, then re-run /rubric (DELTA).
Evidence limits: Facts: helper comparisons bind to the derived extract extra:halloween-facts; I rebuilt its 58 tickets from the static SQL in this run with 0 differences, but its call, due and owner fields are still reviewer-derived, so each semantic claim is a judgment. Locked rows' check entries are carried unchanged; their values were re-checked by script, and their text was not re-read in full. Reachability: every source is recorded PROMPT_LINKED; live search behaviour cannot be tested locally. Whether linear_update_issue accepts a usr_ id is not established. BOTH_FAIR_FIGURE was not tested, because no saved /prompt report exists in this workspace. Docs: this machine has no PDF reader, so I read Rubric Writing through a stdlib text extraction, skimmed Oracle Events section 8 and the Example Task the same way, and opened Universe and Tools and Persona ACL Policy only at their headers; I read the QC Appendix and excerpts of the rubric rows of the rating form. Reviewers: passes were told to write no file and returned text only, but I cannot prove no file was written. Passes were not given fixcheck/ (except the candidate in the fix check) or attachments/, which is less than deep_recheck's full task inputs, so they could not lean on the derived extract. The fix-check R7 also got the scope checklist section, which deep_recheck does not list; the first R7 had read it unprompted. Reported boundary slips: R2, R5 and R6 read harness-saved copies of their own tool output under ~/.claude; R2 and the fix-check R1 read Slack users.json and channels.json directly, then rechecked through hg_search.py; R5 saw one inputs.json origin string about /injection. R4 and R7 opened files outside their list (rubric_review_record.md, rubric_qc_cases.json, test fixtures, the tool catalog). None reported touching a no-go path, and each finding was checked against its record here. Revised rows have not had a second R1-R7 run.
