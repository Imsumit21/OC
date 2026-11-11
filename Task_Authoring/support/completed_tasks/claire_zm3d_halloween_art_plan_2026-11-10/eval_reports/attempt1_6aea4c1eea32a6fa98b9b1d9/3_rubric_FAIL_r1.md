## RUBRIC EVALUATION REPORT

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

### Task: Claire plans the Halloween art for Zombie Match 3D's store pages and the 58 running Unity ads from Leonard's #zombie_marketing ask: a call, maker and due date for each, a plan doc and tracker shared with the review, a comment on each ad's ART ticket, assignments, new store-art tickets and a thread reply with both links.
### Persona: Claire Morgan - Art Lead
### Total Rubrics: 221 (Outcome: 221, Process: 0)

Run mode: FULL (first run). Reviewers: F1 (this session), F2 and F3 (independent full reviewers), plus deep-recheck passes R1–R7.

## Fix List

Row numbers are from your current rubric. Each fix below passed `fixcheck` (title cap, bundling, decision forks), lint (0 hits) and the R1–R7 fix-check passes, including the opposite-pair test.

| Row(s) | What's wrong | Fix to copy | Mark |
|---|---|---|---|
| R9 | Weight 3, but the Oct 10 rule joins Frederick's mail, his later Slack reply and each ad's campaigns. That's the same work R36, R37, R40 and the Oct 10 comment rows carry at 5 | Set weight to 5 | checked |
| R15 | "maker or owner" also matches the original maker on the tickets | "The Agent names Julia Lawson (or Julia) in its plan doc as the maker or owner of the Halloween work on the ad statics" | checked |
| R22 | A count joined to a range restriction (set-equality over 58 tracker rows) | "The Agent lists exactly 58 ads with a Halloween call in its tracker (on one tab or several)" | checked |
| R41, R42 | "maker or owner" passes a tracker that copies the tickets' "Made by Julia Lawson" | "The Agent names Julia Lawson (or Julia) as the maker or owner of the Halloween work on ART-825 (julia 1:1) in its tracker" (same for ART-826 (julia 4:5)) | checked |
| R45 | A count joined to a 10-ticket "apart from" list, which reads two ways. Every rewording as a count failed with your other tracker counts on a single error (a miscalled Skip ad or a missing ART-826) | Delete it. R22 stays as the tracker's volume control, and R41–R44 remain the maker spot checks | checked |
| R58, R59 | "Exactly 6 people" fails a valid extra share (to Julia, say). The prompt has no "only" and the records hold no share decoy | Delete both. R46–R57 cover every required share | checked |
| R60 | 58 comment writes bundled with a range restriction | "The Agent posts comments carrying a Halloween call on exactly 58 existing ART tickets". Evidence "Accept:": count ART tickets that existed before the run, whichever they are; a second comment on one ticket adds nothing | checked |
| R167 | A write joined to "only on tickets other than" 10 tickets, so an Agent that does nothing passes (Negative Criteria) | Delete it. R60's fix is the one guard on the comment write. The Skip call rows (R87, R96, R99, R112–R114, R117, R144, R147, R156) grade those tickets | checked |
| R168 | The same pattern over 14 tickets | "The Agent sets an assignee on exactly 48 existing ART tickets". Evidence "Accept:": counted whichever tickets they are; a new store ticket isn't counted | checked |
| R187, R188, R190–R193, R202–R204, R208, R209, R211 | Weight 1. Assigning these also needs the needs-new-work check, which you weight 3 on R169–R186, R189 and R200 | Set weight to 3 | checked |
| R218 | "names the iPad set" passes a ticket that only mentions it | "The Agent opens a new ART ticket to make the Halloween iPad 12.9\" set" | checked |
| R219 | "only for surfaces other than …, in any number of tickets": zero passes, so it's an idle-passes negative | "The Agent opens new ART tickets for exactly two store surfaces in total (in any number of tickets)". Evidence "Accept:": count each surface the new tickets cover once, whichever they are | checked |

---

### Phase 1: Structural Validation
- Five-field completeness: 221 of 221 rows; all categories valid, all weights 1, 3 or 5
- Category distribution: Outcome 221, Process 0
- Requirement coverage: 227 of 227 outcomes (the six bundled rows each carry two outcomes)
- Code checks: `hg_rubric_lint.py` flagged `bundled_writes` on R45 and R60. R60 grades a write, so it is a finding. R45 grades tracker cells, which fall under the table rule; it is still a finding, on other grounds (see R45).

### Phase 2: Per-Rubric Quality

**Facts.** I recomputed every call, due date and maker from the records:
- the injected ART-793 to ART-854 tickets and their comments
- Robert's deck
- Frederick's three mails and his Sep 30 reply in #zombie-match3d
- the two Trello comments, the Store folder, the Halloween store export thread and the review invite

The 58 call rows, 48 due-date rows and 48 assignee rows all match. So do the plan-doc lists in R6–R10 (36 Refresh first / 12 Halloween version / 10 Skip; 30 due Oct 10 / 18 due Oct 15) and the totals 14, 10, 30, 42 and 58. The R2 deep-recheck pass found no incorrect value either.

| Row | Issue | Type | Severity |
|---|---|---|---|
| R60 | 58 comment writes in one row, plus a range restriction | non_atomic | Major |
| R167 | A write joined to "only on tickets other than" 10 tickets; an Agent that does nothing passes | non_atomic (+ Negative Criteria) | Major |
| R168 | The same pattern over 14 tickets | non_atomic (+ Negative Criteria) | Major |
| R219 | "only for surfaces other than …, in any number of tickets" | non_atomic (+ Negative Criteria) | Major |
| R22 | A count joined to range membership (set equality over 58 rows) | non_atomic | Major |
| R45 | A count joined to a 10-ticket "apart from" list (two readings) | non_atomic (+ overly_broad) | Major |
| R58, R59 | "exactly 6 people" fails a valid extra share; no share decoy in the records | overly_specific | Major |
| R218 | "names" the iPad set rather than "to make" it | overly_broad | Minor |
| R15, R41, R42 | "maker or owner" matches the tickets' original "Made by Julia Lawson" | overly_broad | Minor |

Atomicity: every other row is one of the following: one ticket and one value, one share, one total, or one plan-level rule with its cohort. R9 and R10 are rules; their lists are another way of stating the same rule.

Agent-centric: every title starts with "The Agent" plus an action, and none names a tool. Vague exemplars: none. Dates: all inside the window and consistent with the Oct 1, 2025 clock.

### Phase 3: Set-Level Quality
- **Coverage gaps:** none. Every required write has its own row: plan-doc and tracker content, 12 shares, 58 call comments, 48 due-date comments, 48 assignments, 2 store tickets and both thread links.
- **Process audit:** there are no Process rows and none are needed; the thread links prove the files existed first.
- **Duplicates, overlaps and cascades:** none scored. The complementary call counts (R6–R8) and the per-column tracker totals (R22/R40) share a root cause, but each grades a different total (Eval 3 §3.3).
- **Spot-check groups:** all within the cap of five.
  - Tracker calls: samples R31–R35; controls R23/R24; store rows graded directly.
  - Tracker dates: samples R36–R39; control R40.
  - Tracker makers: samples R41–R44.
  - Comments and assignments are not sampled; each ticket has its own row.
- **Wrong-target guards:** real decoys exist for:
  - comments and assignments: the Archive tickets ART-836 to ART-839 ("Paused on Sep 15/19", Canceled) and the 10 Skip ads
  - store tickets: Leonard says "no tickets needed for those"
  - shares: none
- **OE cross-check:** every row maps to its OE write step (OE 38–40, 41–52, 53–110, 111–158, 159–161). No conflicts.

### Phase 4: Issue Tally
| Severity | Count | % | Fails when | Status |
|---|---|---|---|---|
| Major | 8 rows | 3.6% | any | FAIL |
| Moderate | 0 | 0% | any | OK |
| Minor | 4 rows | 1.8% | ≥ 5% | OK |

Weights: 13 rows are one level off (5.9%): R9 (3 → 5), and R187, R188, R190–R193, R202–R204, R208, R209 and R211 (1 → 3).

### Phase 5: Scoring
| Sub-Dimension | Score | Justification |
|---|---|---|
| Overall Rubric Quality | 2 | Major issues on 8 rows |
| Criteria Weights | 4 | 13 of 221 rows one level off, none two levels off |
| Rubric Category Balance | 5 | All Outcome |
| Process Rubrics | 5 | None needed |
| Agent-Centric Phrasing | 5 | All standard "The Agent …" |
| Negative Criteria | 2 | R167, R168 and R219 pass an Agent that does nothing |
| Predicted All-Fail gate | PASS | No row predicted to fail every run |

**Lowest Sub-Dimension:** Overall Rubric Quality and Negative Criteria, both 2. The causes are bundled or idle-pass guard rows and a share-count guard with no decoy behind it.

**Summary:** The values are right throughout. The FAIL comes from how the guard rows are built (R22, R45, R60, R167, R168, R219) and from the "exactly 6 people" share rows. Every issue has a short fix in the Fix List.

### Recommended Fixes
Every fix is in the Fix List above, marked `checked`:
- The weight changes and the R22 and R218 fixes passed in round 1.
- The comment, assignment and store guards (R60, R168, R219) passed in round 3.
- The R15/R41/R42 wording passed in round 4, after their evidence lines were aligned to the new titles.

Each fix passed `fixcheck` (title cap, bundling, decision forks), lint with 0 hits, and every R1–R7 pass on the changed rows and their siblings, including the opposite-pair test.

## All Findings

**R9**: weight 3 should be 5 (F3). The Oct 10 rule joins Gmail, Slack and Linear, as R36, R37, R40 and the Oct 10 comment rows do. Fix: set weight to 5.

**R15, R41, R42** (Minor, overly_broad; F3): ART-825 to ART-830 say "Made by Julia Lawson", so a tracker that copies that column passes even if the Halloween work goes to Martin. Fix: "maker or owner of the Halloween work on …".

**R22** (Major, non_atomic; R7): "exactly 58 ads … all of them in ART-793 to ART-835 and ART-840 to ART-854". The ranges are exactly the 58 running tickets, so the row checks set equality. Witness: a tracker with ART-836 in and ART-826 out still lists 58 ads, so it meets the count and fails the range. Fix: bare count.

**R45** (Major, non_atomic + overly_broad; F1, F2, F3, R7, lint): "exactly 42 ads … apart from [10 tickets]" can mean "not counting" or "Marcus must not be on them". The two rewordings tried (counting against the tracker's own calls; "all but exactly 6") failed together with R22 and R24 on one error: a missing ART-826 or a miscalled ART-849 (R4, rounds 1–2). Fix: delete the row. R22 is the tracker's volume control and R41–R44 sample the makers.

**R58, R59** (Major, overly_specific; R1, F2, F3): the prompt says "shared with everyone on the review so they can comment", with no "only". The invite evt_d947bf7cd910549b674b1f lists six attendees and no record sets up a share decoy. Sharing with Julia Lawson as well, who makes the six statics, is valid, and both rows fail it. Fix: delete them.

**R60** (Major, non_atomic; F1, F2, F3, R7, lint): 58 comment writes plus a range restriction in one row. Fix: "The Agent posts comments carrying a Halloween call on exactly 58 existing ART tickets".

**R167** (Major, non_atomic + Negative Criteria FAIL; F1, F2, F3, R5, R7): "comments due dates … only on tickets other than ART-806 … ART-849". It is a write joined to a scope restriction, it accepts the 10 tickets by absence, and from the title an idle Agent passes. Fix: delete it. A replacement guard ("a final due date on exactly 48 existing ART tickets") was tried and dropped: it is a second guard on the comment write and failed together with R60 (R4, round 2). The Skip call rows grade those tickets.

**R168** (Major, non_atomic + Negative Criteria FAIL; F1, F2, F3, R5, R7). Fix: "The Agent sets an assignee on exactly 48 existing ART tickets". All 62 ART tickets start unassigned, so the 48 writes are real.

**R187, R188, R190–R193, R202–R204, R208, R209, R211**: weight 1 should be 3 (F2, F3). These tickets say "Made by Marcus Bennett", but assigning them still needs the needs-new-work check. Several of them (ART-817, ART-823, ART-834) also run on Android US tablet, and the "Made by Marcus" Skip tickets ART-820 to ART-824 show that the maker alone doesn't decide. You weight that same work 3 on R169–R186, R189 and R200. Fix: weight 3. I took this side over R4's opposite suggestion (R200 → 1).

**R218** (Minor, overly_broad; F2): "names the Halloween iPad 12.9\" set" passes an upload ticket. Fix: "… to make the Halloween iPad 12.9\" set".

**R219** (Major, non_atomic + Negative Criteria FAIL; F1, F2, F3, R5, R7): "any number of tickets" includes zero. Fix: "The Agent opens new ART tickets for exactly two store surfaces in total (in any number of tickets)". One combined icon + iPad ticket, or a set split across several tickets, still passes.

### Worth a look (not scored)
- **R9/R10 list option.** The list form ("or as a list of exactly … with that date") grades all 30 or 18 ads at once. It is kept because it is just another way to state the one rule, but a plan doc that states the rule plainly is the safer target.
- **Split due dates.** An ad on both Android US phone and iOS UK could be commented "Android US phone copy Oct 10, iOS UK copy Oct 15". The Oct 10 rows read "final due date is Oct 10" and may grade that unevenly.
- **Call labels.** The tracker call rows (R23–R35) don't say "(in any wording with that meaning)" the way the plan-doc rows do. That is fine because Robert's deck slide "Calls for the tracker" defines the four labels, but a tracker using its own wording ("re-cut first") is graded only by meaning.
- **Two quoted sources.** R32's justification says ART-826's place "is graded by the tracker's surface count"; the row that grades it is R22, which counts ads.

### Rejected findings
- **R6 (deep recheck), labels need the deck** (Refresh first / Reuse "in any wording"): rejected. Each title already states the expected value, as QC B3 requires ("All expected values must be embedded directly in the criterion text"), and the labels are plain English.
- **R7, R9/R10 "every ad … or a list" non-atomic**: rejected under Eval 3 §2.2 "Keep with the result they define: qualifiers of one metric (… cohort …); alternative accepted values of one decision". Each row is one plan-level due-date rule.
- **R3 and F3, missing row for when the reused iPhone 6.5" set ships**: rejected. The prompt asks "who makes what by when". The set is already made: Leonard says "whatever is already exported is done", so a row for it would be unauthorized (Eval 3 §2.8).
- **R1, the Oct 11–14 floor on the Oct 15 rows is overly specific** (an earlier date for iOS-only ads should pass): rejected. Frederick's reply says "iOS UK stays on the 15th", so Oct 10 for those ads is the misreading the rows exist to catch. I tried widening the window in the fix check, and R1 and R5 showed it then admitted that wrong answer. Your original wording stays.
- **F3, Oct 11–14 admits the Oct 12 campaign end**: rejected under the QC B11 exception. An Agent dating a working ad by the end of the Android US tablet campaign, which carries no Halloween ads, is very unlikely.
- **R5, R217/R25 pass a ticket for Martin's rejected icon concept**: rejected under QC B11. A run that misses Robert's reply would call the icon Reuse and open no ticket.
- **R5, R9's rule form passes a plan that copies Frederick's two lines**: rejected. The title's "including those also on iOS UK" already requires the overlap ads at Oct 10.
- **R4 and F2, R6–R8 and R22/R40/R45 cascade groups**: rejected under Eval 3 §3.3 ("Rows that merely share a likely model root cause are not a group"). Each row grades a different total. Samples against their control fall under "an aggregate control versus its atomic spot checks".
- **R4, Oct 10 rows over-weighted at 5**: rejected. The Slack correction adds a third service, which is tracing work under C20.
- **R4, R200 should be 1**: rejected in favour of F2's reading (see the weight finding above).

## Deep Recheck

Passes: R1, R2, R3, R4, R5, R6, R7 on Opus 5.5 (claude-opus-5-5), session effort. Each pass was blind to the main review, ran on all 221 rows, and was run alongside the full reviewers F2 and F3.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| R1 | 221 rows | 2 | 1 |
| R2 | 221 rows | 0 | 0 |
| R3 | 221 rows | 1 | 0 |
| R4 | 221 rows | 6 | 0 |
| R5 | 221 rows | 6 | 3 |
| R6 | 221 rows | 2 | 0 |
| R7 | 221 rows | 8 | 6 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | R1 | R58/R59 "shares its plan doc with exactly 6 people" | Prompt "shared with everyone on the review so they can comment"; evt_d947bf7cd910549b674b1f attendees | §4 other allowed answer | overly_specific | CONFIRMED | No "only" and no share decoy, so an extra share to Julia is valid and fails both rows (also F2-9, F3-5) |
| DR2 | R1 | R10, R38, R39, R40 and the Oct 15 comment rows "a final date from Oct 11 to Oct 14, 2025 also passes" | C0880U9751A/1759275738.984915 "iOS UK stays on the 15th" | §4 other allowed answer | overly_specific | REJECTED | Frederick explicitly keeps iOS UK at the 15th, so Oct 10 is the misreading these rows catch. Widening the window failed the fix-check opposite-pair test (R1 and R5, round 1) |
| DR3 | R3 | Missing row for when the reused iPhone 6.5" set ships | Calendar f_fdd6d2d2f4a4d2f5b908fb "new iOS screenshots … due by the same Oct 16 12:00 PT cut" | §4 one line per outcome | missing_coverage | REJECTED | The prompt asks "who makes what by when". Leonard: "whatever is already exported is done". Such a row would be unauthorized (Eval 3 §2.8) |
| DR4 | R4 | Oct 10 comment rows at weight 5, Oct 15 rows at 3 | Slack reply C0880U9751A/1759275738.984915 | §7.9 weights | weight disagreement | REJECTED | The Oct 10 date adds the Slack correction, a third service (C20 tracing). A shared root cause is not a cascade group (§3.3) |
| DR5 | R4 | R6, R7, R8 complementary counts | ART-808 "Re-captured on Sep 16 from Android #1896" | §3.3 cascade | duplicate | REJECTED | Each row grades a different total; rows that only share a root cause are not a group (§3.3) |
| DR6 | R4 | Tracker samples inside count rows | ART-811 comments | §3.3 | duplicate | REJECTED | "Not duplicates: an aggregate control versus its atomic spot checks" (§3.3) |
| DR7 | R4 | R200 weight 3 should be 1 | ART-831 "portrait UA end card (Marcus, Jul 31)" | §7.9 | weight disagreement | REJECTED | Conflicts with F2-8. Assignment needs the needs-new-work check (comparison), which the rubric itself weights 3; took F2's side |
| DR8 | R4 | Julia hand-off concentration; "comparison" rows at 3 | C05KNDCHAAG/1759243286.478812 | §7.9 | advisory | REJECTED | Advisory only; the rubric's 2-source = 3, 3+-source = 5 pattern is applied consistently |
| DR9 | R5 | R168 "sets assignees … only on tickets other than …" | Leonard "assign the ones that need new work" | §4 too broad / do-nothing | non_atomic (Negative) | CONFIRMED | An idle Agent passes the title; merged with the R168 finding |
| DR10 | R5 | R167 "comments due dates … only on tickets other than …" | Prompt "Comment each ad's call and due date" | §4 / do-nothing | non_atomic (Negative) | CONFIRMED | Merged with the R167 finding |
| DR11 | R5 | R219 "(in any number of tickets)" | C08R8CHB0QL/1759247246.453725 | §4 / do-nothing | non_atomic (Negative) | CONFIRMED | Zero tickets passes; merged with the R219 finding |
| DR12 | R5 | R217 / R25 pass Martin's rejected icon concept | C08R8CHB0QL/1758127951.679146 "not for the app icon" | §4 too broad | overly_broad | REJECTED | QC B11 exception: a run that misses Robert's reply calls the icon Reuse and opens no ticket |
| DR13 | R5 | R9 rule branch passes a plan copying Frederick's two lines | C0880U9751A/1759275738.984915 | §4 too broad | overly_broad | REJECTED | The title's "including those also on iOS UK" already requires the overlap ads at Oct 10 |
| DR14 | R6 | Refresh first / Reuse "in any wording with that meaning" (R4, R5, R6, R61 …) | Deck f_5ebf55ad29e815d46243c8 "Calls for the tracker" | §4 title | not_self_contained | REJECTED | QC B3: the expected value is in the title ("Refresh first", "Reuse"), and the labels are plain English |
| DR15 | R7 | R9, R10 "every ad … or as a list of exactly …" | 09_Rubrics.json R9/R10 | §7.4 | non_atomic | REJECTED | Eval 3 §2.2 "Keep with the result they define: qualifiers of one metric (… cohort …); alternative accepted values of one decision" |
| DR16 | R7 | R22 "exactly 58 ads … all of them in ART-793 to ART-835 and ART-840 to ART-854" | Archive tab ART-836..839 | scope checklist | non_atomic | CONFIRMED | Count plus range is set equality over 58 rows |
| DR17 | R7 | R45 "exactly 42 ads … apart from ART-806 …" | R45 evidence; lint bundled_writes | scope checklist | non_atomic | CONFIRMED | Count plus exclusion list, read two ways (also F2 UNSURE) |
| DR18 | R7 | R60 "exactly 58 of the tickets … all of them in …" | lint bundled_writes; Archive tickets | No bundled writes | non_atomic | CONFIRMED | 58 writes plus a range restriction |
| DR19 | R7 | R167 "… only on tickets other than …" | R167 evidence | No bundled writes | non_atomic | CONFIRMED | A write joined to a scope restriction |
| DR20 | R7 | R168 "… only on tickets other than …" | ART-836..839 Canceled | No bundled writes | non_atomic | CONFIRMED | A write joined to a scope restriction |
| DR21 | R7 | R219 "… only for surfaces other than …" | Store folder d_74a7c95c28097dd9777e01 | No bundled writes | non_atomic | CONFIRMED | A write joined to a scope restriction |

Full reviewers F2 and F3 raised the same core findings. They also raised these, which were accepted: weights R187–R211 (F2-8) and R9 (F3-6); R218 overly broad (F2-12); R15, R41, R42, R45 "maker or owner" overly broad (F3-8). These were rejected: the R6–R8 and R22/R40/R45 cascade groups (F2-10, F2-11), the Oct 11–14 window being overly broad (F3-7), and the iPhone-set timing gap (F3-9).

**Fix check:** 4 rounds of R1–R7 ran on the candidate rubric's changed rows and their siblings.
- **Round 1:** R5 and R1 showed that widening the Oct 15 window traded overly specific for overly broad, so it was reverted. R6 found three count-guard notes that were narrower than their titles. R3 showed that deleting R167 left the Skip-date trap unguarded. R1 showed the store guard capped the number of tickets.
- **Round 2:** R4 found that the reworded R45 and the added due-date guard created new cascades. Both were removed: R45 is deleted, and R60 is the single comment guard (one guard per write kind).
- **Round 3:** R5 found R41/R42's evidence lines were looser than their titles. They were aligned.
- **Round 4:** all passes clean on the changed rows. R6 raised that "the ad statics" (R15) and "the video ads" (R16) aren't defined in any title. That was rejected on the same QC B3 basis as DR14: Leonard's split, which the prompt brings in, uses these labels.

Effect on verdict: unchanged by the recheck beyond the confirmed findings above, which are already in the scoring record (FAIL 2).

Platform defects: none

### FINAL VERDICT: FAIL
Score: 2
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Execution status: COMPLETE
Review policy: rubric-revision-v10
Review mode: AUDIT
Reviewed JSON SHA-256: 5801aea6371abed1a1423b0b0a04b25e3620e73a38d03d3de3929c5727add589
Review context SHA-256: 46ddb1be968651e094a67c7649ed2d76b81c6bdc3b4c54e8a6816003abb0ac44
Scoring record SHA-256: 0a86a2536bf84187ac026875dca187949328627a1e72707d62b89b04fc22e9e6
Eval version: task-quality-v1
Eval release SHA-256: 81446b85bb68b971bfce06d9d3cf07ad43d923b5702670f206122d1f6d34d53c
Gate tier: localized
Coverage ratio: 227/227
Repairs: See findings
Evaluator model: Opus 5.5 (claude-opus-5-5)
Next action: Apply the Fix List (reword 8 rows, delete R45, R58, R59 and R167, change 13 weights), save the rubric in your Outlier task and send /rubric again
Evidence limits: None
