## RUBRIC EVALUATION REPORT

### Task: ZM3D Halloween art plan: calls, owners and dates for 62 live surfaces, a plan doc and tracker, 58 ART ticket comments, assignments, new store tickets and a thread reply
### Persona: Claire Morgan - Art Lead
### Total Rubrics: 221 (Outcome: 221, Process: 0)

Run mode: DELTA (`hg_rubric_ledger.py plan`). 2 target rows reviewed in full (R60 re-checked, R167 edited), 219 locked.

## Fix List

The candidate is `Evals/task_inputs/fixcheck/rubric_candidate.json` (221 rows). Copy R60 from it. Every other row stays as it is.

- R60: A run that ends right can still fail this row, because it counts every ART ticket that got a call comment and a comment cannot be removed. Copy the title: "The Agent posts comments carrying a Halloween call on exactly 58 of the tickets ART-793 to ART-854 (a call its own later comment on that ticket withdraws is not counted), all of them in ART-793 to ART-835 and ART-840 to ART-854". Copy the new Accept line in the evidence. The justification, weight and category do not change. (checked)

Your R60 carries the text the first run's Fix List gave, and you copied it correctly; the defect is in that text. R167 passes, and all three findings on it from last run are fixed.

---

### Phase 1: Structural Validation
- Five-field completeness: 221 of 221
- Category distribution: Outcome 221, Process 0
- Requirement coverage: 221 of 221 outcomes
- Code checks: `hg_rubric_lint.py` returned 0 hits on the rubric and 0 on the candidate.

**The claim that all 221 rows match the last candidate in all five fields, with no other change: true.** Before this run replaced it, the candidate had the same SHA-256 as the saved rubric, 3a0ab605, and the same 192,085 bytes. Parsed, 0 fields differ across 221 rows. The plan agrees: only R167 differs from the rows the ledger recorded, and R167 is the row `fix_status.json` marked `revised`. I cannot prove from here that the candidate file was untouched after the last run wrote it. Its other 220 rows match the ledger's hashes.

**Values.** I rebuilt the ticket set from a static parse of the saved SQL, not from the OE, the rubric or the facts extract. The result: 62 tickets, 4 on the Archive tab, 56 on Unity, ART-826 and ART-831 off the sheet, 58 serving. Reading each ticket's Unity lines and taking the two cuts off iOS UK tablet per Frederick's Sep 29 mail gives 10 Skip, 48 working, 30 due Oct 10 and 18 due Oct 15. The deck's rule gives calls of 36, 12 and 10. A script then compared this with all 58 call rows, 48 due rows, 48 assign rows and the 9 tracker sample rows, including each ticket's name in the title: 0 mismatches. Every serving ticket has a call row, every working ticket has a due row and an assign row, and no Skip ticket has either. The facts extract matches the rebuild with 0 differences on call, due and owner. Base Linear holds no ART-793 or later (complete scan of `/issues`, max ART number 792). No existing comment on the 10 Skip tickets holds a due date, so R167's 'in a comment' can only reach what the Agent wrote. Every quote and record id in R60 and R167 was found in the SQL.

### Phase 2: Per-Rubric Quality

| Row | Issue | Type | Severity |
|---|---|---|---|
| R60 | Fails a run that ends right, on two paths | overly_specific | Major |

Atomicity decomposition: R60 grades one write kind and one scope condition. R167 grades one write kind and one scope condition, the ten Skip tickets. The named set and range are scope conditions under the scope checklist, 'as a count or scope condition on the required write ("comments on exactly these 6 tickets")'. Both blind R7 runs returned none but called this a judgment; see Notes for QM.

Over-specificity triage: `overly_specific` on R60; R167 valid.

R167 row checks: title-only self-contained (ranges, carve-outs and all 10 tickets are in the title); affirmative, and the pre-scan hit 'is not counted' is a counting rule, not a graded prohibition; do-nothing test rejects ('comments due dates in ART-793 to ART-835 and ART-840 to ART-854'); valid case accepts a run that corrects 'due Oct 15' on ART-811 and a Skip comment naming the Oct 12 campaign end; weight 5 stands, since the 10 need every ticket's campaigns read against two mails.

### Phase 3: Set-Level Quality
- Coverage gaps: none scored. Old gaps are under Notes for QM.
- Scope checklist: doc and tracker create, R1, R21. Shares, R46 to R57 with guards R58, R59. Comments, R61 to R166 with guards R60, R167. Assign, R169 to R216 with guard R168. New tickets, R217, R218 with guard R219. Slack reply, R220, R221. No write kind lacks a target row or a wrong-target row.
- Process audit: 0 of 0. The prompt holds no ordering dependency an Outcome cannot see.
- Duplicates / overlap / cascade groups: none. The R60 and R167 group from last run is closed. A dated comment on ART-836 now fails R60 alone, and a due date on a Skip ticket fails R167 alone.
- Spot-check groups: tracker call 5 samples, tracker due 4, tracker owner 4, each with a count control.
- Contradictions: none. R60 needs a comment on Skip tickets and R167 keeps dates off them, and OE 66 does both. Final-reply test: ACCEPT, no row grades the reply. OE cross-check: every row maps to OE steps, 0 unmapped, 0 conflicts.

### Phase 4: Issue Tally
| Severity | Count | % | Fails when | Status |
|---|---|---|---|---|
| Major | 1 | 0.5 | any | FAIL |
| Moderate | 0 | 0 | any | none |
| Minor | 0 | 0 | over 10% | none |

### Phase 5: Scoring
| Sub-Dimension | Score | Justification |
|---|---|---|
| Overall Rubric Quality | 2 | R60 at Major (overly_specific) |
| Criteria Weights | 5 | All 221 rows at the expected weight |
| Rubric Category Balance | 5 | 221 Outcome rows |
| Process Rubrics | 5 | No Process rows, none needed |
| Agent-Centric Phrasing | 5 | Every title opens with The Agent and names no tool |
| Negative Criteria | 5 | No prohibition title; every row fails an idle Agent |
| Predicted All-Fail gate | PASS | 0 rows predicted |

**Lowest Sub-Dimension:** Overall Rubric Quality - 2 - one Major issue on R60.
**Summary:** Every value is right and R167 is clean, so the rubric fails on one row's acceptance wording, not on facts. R60 counts a comment on the Agent's own new store ticket and a call the Agent has withdrawn, which R167 and R168 already leave out. The path is narrow and the fix is one clause, but any Major fails under the thresholds.

### Issues Found
| # | Row | Issue | Severity | Type |
|---|---|---|---|---|
| D1 | R60 | Two paths end right and still fail. (1) All 58 ad comments are right and the Agent also comments 'Halloween version, due Oct 16' on the new app icon ticket, a value R11, R12 and R25 accept: 59 ART tickets, one outside the ranges. R217 and R218 require those tickets, and nothing in the prompt limits comments on them. (2) A run posts a call on ART-836, reads the description 'Paused on Sep 15, see the Archive tab.' and posts a correction. The catalog has only linear_create_comment and linear_list_comments, so the first comment stays. R167 now passes the same correction. | Major | overly_specific |

Eval 2.7: 'if a valid prompt-authorized alternative exists that the row would fail', `overly_specific`. Both shapes were scored Major on sibling rows before: C2 on the old R170 for a new store ticket, and B4 and last run's R167 finding for a self-correcting run. R167's and R168's Accept lines already keep store tickets out.

### Recommended Fixes
1. D1: Set the count over the tickets ART-793 to ART-854, so a new store ticket is outside it, and add the same withdrawal clause R167 has. Keep the ranges: a swap of ART-836 for ART-826 still fails, and so does a 59th ticket in the population. The Accept line follows. Mark: checked. Checks passed: `hg_rubric_lint.py` with 0 hits, a self-check of R60 against every rule in `rubric_flow_v2.md` Fixes step 1, and one R1-R7 run on the candidate (R3 whole rubric, R4 against all rows). No pass confirmed a finding on the fix.

**Fix check results.** R1, R2, R5, R6 and R7 returned none on R60. R1, R5 and R6 each listed the store-ticket or withdrawn-call path as now passing. R3 returned two findings on the Reuse sets, neither involving R60; they go to Notes for QM on Z7. R4 returned the count-row cascade again, rejected on Z3, and held R60's weight at 5.

## Changes Since Last Run

**Row counts.** Locked 219. Locked checked fix 0. Edited 1 (R167). New 0. Re-checked 1 (R60). Removed 0.

**Previous findings, all fixed.**
- R167 `overly_specific`, a self-correcting run failed: fixed. The title does not count 'a date its own later comment on that ticket withdraws', and the Accept line grades 'after the Agent's last comment on each ticket'.
- R60 and R167 overlap on ART-836 to ART-839: fixed. R167 no longer names those tickets and covers only the two ranges.
- R167 `harmless_specificity`, the justification reaching the dueDate field: fixed. It now says 'A due date left standing in a comment'.

**Dismissals.** None new. The plan lists 113, under old row numbers. The ones filed under 60 and 167 carry the titles of older rows (the old plan-doc share count and the old ART-854 comment), not current R60 and R167, so no recorded dismissal applies to a target row. A1 and A2 stay closed; their rows are locked and unchanged.

**New scored findings.** D1 on R60. This reverses earlier passes, so coherent_record R1 applies. The row's text came from the first run's Fix List. Run 1 left the store-ticket case as an UNSURE note, and run 2 reviewed this wording as a target row, then numbered R62, and scored nothing on these paths. C2 later scored the same store-ticket shape on the old R170, and last run scored the self-correcting shape on R167, so the earlier pass on this row was the mistake. R1 asks for 'a demonstrated earlier mistake and a counterexample'; the counterexample is in D1, and 'A prior reviewer is not an authority that can suppress a real new defect'.

### Notes for QM (not scored)
- **D1, closest call.** The path needs an unrequested comment or a corrected mistake. R1 added that a lenient grader might count ad tickets only. Against scoring it, run 1's X3 used the scope checklist's 'extra targets' to keep exact counts on shares. If QM reads 'extra targets' as reaching the Agent's own new ticket, path 1 falls and path 2 still stands.
- **Named sets and count-plus-range rows.** Both R7 runs returned none but said that if 'Two exceptions stay whole' is a closed list, R60 and R167 become Major `non_atomic`, and R22, R45 and R168 share the form. I relied on the scope checklist and common_errors 7.8. The contributor's note says every count that guards extra targets is now bare. That is not true of R60, whose range holds exactly 58 tickets.
- **R167 has no floor (R5).** A run that dates only ART-793 to ART-805 passes this weight-5 row with no Skip decision made. Rejected on Z1. A count was tried here before and was scored `overly_broad`, because a wrong set lands on 48.
- **Date-only comment on an Archive ticket.** It now fails no row. A comment with the call fails R60. Rejected on Z2 as unlikely.
- **R60 weight (R4).** ART team tickets created since Sep 1 in state Done are exactly the 58, so a Linear filter reaches the set. No record says Done means serving, and base Linear has 488 Done ART tickets. Rejected on Z6; the fix-check R4 held 5.
- **Reuse sets.** R3 raised dates and routes for the iPhone 6.5" and Google Play sets in both rounds, and owners for them in the first; at least seven blind passes have now raised this. OE 36, OE 38 and OE 40 give them a route and no row grades it. If QM reads 'by when' as reaching store go-live, add rows for both sets.
- **Skip rows on the tracker.** R3: a tracker giving the 10 Skip rows Marcus and Oct 15 passes every tracker row. R167 and R168 hold that exclusion on Linear only.
- **Weight on one write kind.** A run that posts no ticket comments fails R60 to R167: 108 rows, weight 412 of 741, 55.6%. This is the A1 and A2 shape, closed earlier.
- **Cross-artifact reach of one miss.** Missing ART-826 or ART-831 fails nine rows each across the plan, tracker, comment and assign rows. Rejected as a group on Z4 and Z5.
- **Outside-range calls.** With the fix, a call on a ticket outside ART-793 to ART-854 is not counted. R5 checked the nearest older tickets; none is an ad.
- **Standing notes.** Julia on the tracker, bare-count cancelling on R40 and R45, and 'Marcus' fitting Marcus Lee are unchanged from the last saved report.
- **Helpers and records.** `hg_rubric_ledger.py` reads a verdict key the record never holds, so the plan shows `previous_verdict: null`. Dismissals stay keyed to old row numbers and are not remapped. The two runs before this one saved no report, so their notes survive only in the scoring records.

## Deep Recheck

Passes: R1, R2, R3, R4, R5, R6, R7, Opus 5.5 (claude-opus-5-5), effort level not reported to this session; subagents started with no model override, so they inherit it, not independently confirmed, each blind to the main review. Target rows only (R3 whole rubric, R4 against all rows). One fix check ran after them on the candidate.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| R1 | 2 rows | 1 | 1 |
| R2 | 2 rows | 0 | 0 |
| R3 | 221 rows | 5 | 1 |
| R4 | 2 rows against all 221 | 4 | 0 |
| R5 | 2 rows | 2 | 0 |
| R6 | 2 rows | 0 | 0 |
| R7 | 2 rows | 0 | 0 |

Rejection grounds, each a quoted rule:
- Z1: Eval 3 Local Overrides, Negative criteria: 'as a condition on a write the Agent must make (an exact count or scope)'. Scope checklist: 'a row that grades the required targets' and, separately, 'a row that fails a run doing that write to the wrong targets'. Eval 2.7: 'Never repair an overly broad row with a count, format or phrasing; name the value.'
- Z2: conflict with last run's overlap finding, settled by Eval 3.3: 'When two or more rows fail on that one error because each embeds the same acceptance condition, record one OVERLAP_GROUP'. R60 holds the Archive exclusion, so naming it on R167 again restores the group. QC B11: 'If the invalid paths that are accepted by the overly permissive criterion are unlikely to occur, do not flag the criterion as overly broad.' Side not taken: R5's 14-ticket scope.
- Z3: Eval 3.3, 'Not duplicates: ... an aggregate control versus its atomic spot checks.' common_errors 7.8: 'With a row for each review that must close, a run that also closes ENG-123 fails it, and so does a run that does nothing.'
- Z4: Eval 3.3, 'Not duplicates: ... the same fact in two prompt-specified deliverables'.
- Z5: Eval 3.3, 'Rows that merely share a likely model root cause are not a group.' R167 and R168 are different writes, and either can fail alone.
- Z6: the finding's own condition, 'so 5 stands if the sheet counts as required'. Leonard's C06DJBJL798/1759269913.882683 says 'the live creatives sheet is what's running', and the prompt says 'take his message and do it all'. QC C20 gives 5 to 'Multi-source reconciliation'.
- Z7: rubric_flow_v2, 'A coverage gap that no change caused goes to `### Notes for QM` unless the prompt states that requirement outright.' None involves a target row. Run 1's X1 holds: 'A finished set has no maker, so no by-when is owed.'

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | R1 | R60 'exactly 58 ART tickets, all of them in' | Prompt 'open ART tickets for any new store art'; OE 36; R167 Accept | 4, 7.2 | overly_specific | CONFIRMED | D1, path 1 |
| DR1 | R3 | Prompt 'who makes what by when'; R4, R27, R219 | f_fdd6d2d2f4a4d2f5b908fb | 4, 7.1 | missing_coverage | REJECTED | Z7; quote exists; Note for QM |
| DR2 | R3 | R5, R28, R219 | f_fdd6d2d2f4a4d2f5b908fb | 4, 7.1 | missing_coverage | REJECTED | Z7; quote exists; Note for QM |
| DR3 | R3 | R18, R19, R29, R30 | C05KNDCHAAG/1759243286.478812 | 4 | missing_coverage | REJECTED | Z7; quote exists; Note for QM |
| DR4 | R3 | R45, R40 | f_5ebf55ad29e815d46243c8 | 4 | missing_coverage | REJECTED | Z7; quote exists; Note for QM |
| DR5 | R3 | R60 title and Accept line | R167 and R168 Accept lines | 4, 7.6 | overly_specific | CONFIRMED | Merged into D1; typed by the Eval 2.7 decision rule, not unauthorized |
| DR1 | R4 | R60 with R61 to R165 | Prompt; weight 412 of 741 recomputed | 5, 7.7 | duplicate | REJECTED | Z3 |
| DR2 | R4 | R60 with R22 | f_02b1968f5e882366fbb883; 68dc65a0f2d7fb28743f5860 | 7.7 | duplicate | REJECTED | Z4 |
| DR3 | R4 | R167 with R168 | Mail 'Unity retention restart' | 7.7 | duplicate | REJECTED | Z5 |
| DR4 | R4 | R60 justification | SQL ART-836 to ART-839 'Canceled' | 7.9 | weight review | REJECTED | Z6; the filter claim is true, see Notes for QM |
| DR1 | R5 | R167 title and Accept line | OE 34; cmt_art805_1 | 4, 7.7 | overly_broad | REJECTED | Z1 |
| DR2 | R5 | R167 'outside those ranges is not counted' | SQL ART-836; Archive tab | 4, 7.7 | overly_broad | REJECTED | Z2 |

Effect on verdict: unchanged. The first save, from my own review, was FAIL with score 2 on R60; R1 and R3 raised its first path blind, and the second path rests on the main review. No other dimension changed.

Fix check: R1-R7 ran once on the candidate and raised 3 findings, 0 on the fix; R60 is marked checked.

Platform defects: none

### FINAL VERDICT: FAIL
Score: 2
Execution status: COMPLETE
Review policy: rubric-revision-v10
Review mode: AUDIT
Reviewed JSON SHA-256: 3a0ab605ac5fdf4dbd895f6558affb9945111b2498b44275fc5fc2b77f66c71f
Review context SHA-256: aa03927718af690633e0d94eb3d9a039dc13b3ed1bbbcb5254426d809c7a6b38
Scoring record SHA-256: c6f60c7ecb767ac1e8d3a1caa6048a78f83f0adeb6dba6a28e1f71eddb9aef4a
Eval version: task-quality-v1
Eval release SHA-256: c5b89f4c40a7902f968001f1aa6c710d47bf203842455bbe8dbb668ec7c8943b
Gate tier: localized
Coverage ratio: 221/221
Repairs: See findings
Evaluator model: Opus 5.5 (claude-opus-5-5), effort level not reported to this session; subagents started with no model override, so they inherit it, not independently confirmed
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Next action: Copy R60 from the candidate, then re-run /rubric (DELTA).
Evidence limits: Facts: helper comparisons bind to the derived extract extra:halloween-facts; I rebuilt its 58 tickets from the static SQL in this run with 0 differences, but semantic claims are still judgments. Locked rows' check entries are carried unchanged; their values were re-checked by script against the rebuild, and I read their titles but not all their supporting text. Base Slack was searched for the campaign names in Sep 2025 only (0 hits, scan complete). Reachability: every source is recorded PROMPT_LINKED; live search behaviour cannot be tested locally. BOTH_FAIR_FIGURE was not tested, because no saved /prompt report exists in this workspace. Candidate: I cannot prove the earlier candidate file was untouched after the last run wrote it. Docs: this machine has no PDF reader, so I read PDFs through a stdlib text extraction: Rubric Writing in full, Oracle Events section 8, and parts of Universe and Tools and Persona ACL Policy; the Example Task only by keyword. I read the QC Appendix rubric rows and the rubric rows of the rating form, not the Audit Workflow or Examples sheets, and used the local common_errors.md rather than the Common Errors PDF. Reviewers: passes were told to write no file and returned text only, but I cannot prove no file was written. Passes were not given attachments/, inputs.json or fixcheck/ (except the candidate in the fix check), which is less than deep_recheck's full task inputs. R7 also got coherent_record.md. Reported boundary slips: first-round R3 opened a harness-saved copy of its own output under ~/.claude; fix-check R1 read five lines of UNIVERSE_MAP.md; fix-check R5 ran hg_reference.py routes linear; fix-check R3 grepped hg_search.py source. Fix-check R2 reported that the harness attached CLAUDE.md and the MEMORY.md index to its context, and the same index was in mine; I opened no memory note. None reported touching a no-go path otherwise, and each finding was checked against its record here. The harness moved the working directory into a no-go folder partway through; I used absolute paths and read nothing there. As main reviewer I read the earlier scoring records and the last saved report in reports/drafts, and used them for prior rulings only.
