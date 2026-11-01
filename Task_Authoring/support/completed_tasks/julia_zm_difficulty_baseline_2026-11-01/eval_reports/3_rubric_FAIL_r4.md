## RUBRIC EVALUATION REPORT

### Task: ZM difficulty baseline register (sheet with Tickets and Rules in force tabs, folder, four shares, nine Linear comments, DM reply to Leonard)
### Persona: Julia Lawson - Product Manager
### Total Rubrics: 73 (Outcome: 72, Process: 1)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Review mode FULL (run 1 under rubric-flow-v2): the injection SQL and the OE changed since the last passing version, so every row was reviewed again. Three independent full reviews (F1 this session, F2, F3) plus deep-recheck passes R1–R7 ran on all 73 rows. Every fix below was checked in up to four fix-check rounds (lint, title cap and all seven passes on the changed rows and their siblings).

## Fix List

Row numbers are your current rubric's. "New row" lines are added right after the row named. Copy the text exactly; each fix is marked with its check result.

- **R5**: the parenthetical lets the eleven left-off tickets stay on the Tickets tab as "Excluded" rows and still pass. **This row needs your own rewrite.** Open problem: the row must say plainly where a list of the left-off tickets may appear without counting. Four check rounds went back and forth between "a separately headed block on the Tickets tab is fine" and "any left-off rows on the Tickets tab break Leonard's 'leave them off the list'", and a grader can't tell which tickets are "left off" from the titles alone. Decide by layout: for example, count every ticket row on the Tickets tab toward the 23, and let a list of left-off tickets sit only in a note or on another tab. Keep weight 5. (revised after check, needs your own rewrite)
- **R7** (wording only, not scored): the justification leaves out the ZOM-312 cut. Use: "Multi-source: Blake's mail, the closing notes and both cuts of editor tickets: Leonard's reply D05HB64NMQU/1759267002.665190 takes ZOM-162, 163 and 201 off and Blake's 'not tiers' comment harmonygames-Games/match3d#265#rc_7 keeps ZOM-312 off, leaving ZOM-173, 200, 277 and 315 as Editor only." (checked)
- **R24**: bundles three columns in one row. Delete it; R25, R26 and R27 already need each column with a value. (checked)
- **New row after R27** (Robert's "leave it blank if it never got done" has no row): "The Agent marks ZOM-280 as never done in the done-day column of the Tickets tab of the ZM difficulty baseline register (ZOM-280 was never marked done; a cell with no date passes: empty, a dash, N/A or a never-done note; any date, including its 2025-06-20 cancel date, fails)", Outcome, weight 1. (checked)
- **R28**: "levels played" in the pass list also lets the deck's "first 10 levels played" through, and the weight is one level high. Title: "The Agent states on the Rules in force tab of the ZM difficulty baseline register that a new player's starting tier is set once they have played 10 games (passes: wording that counts 10 games, attempts or plays, or a count of levels that says losses or replays count, with or without a CPM average over the first 10 levels beside it; fails: a count of levels with nothing saying losses or replays count ('after the first 10 levels', 'after the first 10 levels played', 'after 10 levels'), 'after level 10', 'once level 10 is cleared', or only a CPM average over the first 10 levels with no timing)". Weight 3; justification starts "Comparison:". Copy the same pass/fail text into the evidence. (checked)
- **New row after R29** (no row says where everyone else starts): "The Agent states on the Rules in force tab of the ZM difficulty baseline register that new players who miss the tier 1 threshold start on tier 0", Outcome, weight 1. (checked)
- **New row after R47** (the ZOM-199 comment's timing correction has no row): "The Agent adds a new comment on Linear issue ZOM-199 saying the build sets the starting tier once a player has played 10 games (passes: wording that counts 10 games, attempts or plays, or a count of levels that says losses or replays count; fails: a count of levels with nothing saying losses or replays count, 'after level 10' or 'once level 10 is cleared')", Outcome, weight 3. (checked)
- **R49–R55**: each row grades two parts of one comment from different sources (the "not in the store builds" status and the two build numbers). Replace each row with two rows, shown for ZOM-173 (R49); do the same for ZOM-200 (R50), ZOM-277 (R51), ZOM-202 (R52), ZOM-280 (R53), ZOM-315 (R54) and ZOM-293 (R55): (a) "The Agent adds a new comment on Linear issue ZOM-173 saying its change is not in the store builds players have today", weight 3, justification "Interpretation: …"; (b) "The Agent names the store builds iOS 0.3.49 and Android 0.3.133 in its new comment on Linear issue ZOM-173", weight 1, justification "Lookup: Leonard's reply under the ask … 'put the two builds in the comment (ios 0.3.49 and android 0.3.133)'". (checked)
- **R69**: bundles four keys plus "exactly", and repeats R65–R68. Delete it; R65–R68 grade each key and R59's count of 4 rejects a fifth. (checked)
- **R71**: same "levels played" gap and weight as R28. Title: "The Agent tells Leonard in its DM reply that a new player's starting tier is set once they have played 10 games" followed by the same pass/fail parenthetical as R28. Weight 3. (checked)

The full candidate (81 rows) with every fix applied is the one checked (R6's justification note is under Worth a look); the ledger keeps these fixes, so copying them exactly locks them next run.

### Phase 1: Structural Validation
- Five-field completeness: 73 of 73. Outcome 72, Process 1 (R73). Weights are all 1, 3 or 5.
- Code checks (`hg_rubric_lint.py`): 0 hits on the rubric and 0 on the checked candidate.
- Requirement coverage: 86 of 89 outcomes covered (3 missing: M1, M2, M3).
- Facts: the register was rebuilt from the full team ZOM issue list (33 title matches up to Aug 31, 2 Duplicates), the five `tiers:` notes and every cut (ZOM-30/49/50/161/262/275, ZOM-162/163/201/250, ZOM-258, ZOM-312 via PR 265, ZOM-295 via PR 271): 23 tickets, 15 Live, 4 Editor only, 3 Not shipped, 1 Replaced. Every expected value in the rows matches the records (Linear states, ZOM-293 assignee Robert and priority 4, ZOM-200 completed 2025-06-13T01:17:38Z, the Live-tab enrage values, the invite, TierManager.cs `totalGames == 10` and `cpm > 90.0f`). The reviewer's fact extract was rebuilt for SQL revision 48.

### Phase 2: Per-Rubric Quality
| Row | Issue | Type | Severity |
|---|---|---|---|
| R24 | Three columns in one row; also redundant with R25–R27 | non_atomic | Major |
| R49–R55 | "Not in the store builds" status and the two build numbers in one row | non_atomic | Major |
| R69 | Four keys plus "exactly" in one row | non_atomic | Major |
| R65–R69 | R69 repeats each key row | duplicate (overlap group) | Moderate |
| R5 | Left-off tickets can stay listed as unstatused rows | overly_broad | Minor |
| R28, R71 | "levels played" lets the deck's "first 10 levels played" pass | overly_broad | Minor |

- Atomicity: R20 (status plus replacing ticket of one register row) and R41 (one Live-tab row with the three uncopied monsters) are one-record groupings. The build pair "iOS 0.3.49 and Android 0.3.133" is one tool output (Leonard's reply and Blake's mail each state both), so the fixed build rows keep the pair together.
- Over-specificity triage: no row rejects a valid answer. R27 accepts both the Pacific and the UTC day, as Eval 3 §2.11 requires.

### Phase 3: Set-Level Quality
- Coverage gaps: M1 (the ZOM-199 comment's timing correction: Blake says "ZOM-199 says >= 90 after the first 10 levels" and the check "runs when a player's 10th game ends"; R47 grades only the threshold), M2 (Robert: "leave it blank if it never got done"; no row), M3 (where players below the tier 1 threshold start: ZOM-42 "rest stays in tier 0"; no row).
- Scope checklist: 9 comment targets each have a row; the EO/NS comments carry two parts and need two rows each (R49–R55). Share rows R42–R45 with guard R46 (decoy: the Domino card's "Share it with Brian and Vincent"); comment guard R56 (decoys: ZOM-162/163/201/250, ZOM-42); Slack guard R72 (decoy: Vincent's #zombie-design request). No scope tails.
- Process audit: R73 is valid (only the order of the reply after the register's create/move); no ordering check missing.
- Duplicates / overlap: R65–R69 group; R24 redundant with R25–R27.
- Spot checks: Live status 5 samples (R8–R12) plus the counts R5/R6; enrage values 3 samples (R36–R38) plus volume R40; one or two samples per copied Linear column plus the row count R5.
- OE cross-check: every row maps to an OE step; no conflicts. The OE already has the three missing outcomes (OE 28 blank done days, OE 30 "everyone else stays on tier 0", OE 36 the 10th-game timing).

### Phase 4: Issue Tally
| Severity | Count | % | Fails when | Status |
|---|---|---|---|---|
| Major | 12 (9 rows + 3 missing outcomes) | 16.4% | any | FAIL |
| Moderate | 1 (R65–R68 group) | 1.4% | any | FAIL |
| Minor | 3 (R5, R28, R71) | 4.1% | ≥ 5% | under |

### Phase 5: Scoring
| Sub-Dimension | Score | Justification |
|---|---|---|
| Overall Rubric Quality | 1 | Major non-atomic rows, three missing outcomes and one overlap group |
| Criteria Weights | 4 | R28 and R71 one level high (2 of 73, 2.7%) |
| Rubric Category Balance | 5 | 72 Outcome, 1 Process |
| Process Rubrics | 5 | R73 valid; none missing |
| Agent-Centric Phrasing | 5 | Every title "The Agent …"; no tool names |
| Negative Criteria | 5 | No prohibition or absence-only row; guards reject an idle Agent |
| Predicted All-Fail gate | PASS | none |

**Lowest Sub-Dimension:** Overall Rubric Quality - 1 - bundled rows (R24, R49–R55, R69) and three ungraded requirements.
**Summary:** The ticket set, statuses, counts and rules are all correct for the new injection. The rubric fails on structure: three kinds of bundled rows, three requirements from Robert, Blake and the card with no row, and the "levels played" gap that a previous fix had closed. Every fix is in the Fix List and passed the fix-check rounds.

## All Findings

**R5** · overly_broad · Minor · F2, F3, R3, R5 (fix round 1). "(left-off tickets listed without one of these statuses are not counted)" lets a Tickets tab keep the eleven left-off tickets as "Excluded" rows; Leonard: "leave the analytics and tutorial tickets off the list", "take 162, 163, 201 and 250 off the list too"; notes doc "leave ZOM-258 off the list". Fix: needs your own rewrite (see Fix List R5); the checked rounds could not settle whether a separately headed block on the Tickets tab should pass, and a neutral block is ungradable without the left-off keys.

**R24** · non_atomic · Major · F1, F2, F3, R7 (plus duplicate, F2, F3). Three columns that can each be present or missing. Fix: delete.

**After R27** · missing_coverage (M2) · Major · F2, F3, R3. Robert, CAFC495E4006/1759229513.774912: "the day it got marked done, pacific time (leave it blank if it never got done)"; ZOM-280 has `completed_at` null and `canceled_at` 2025-06-20T23:38:27Z. Fix: the new row.

**R28, R71** · overly_broad · Minor · F3, R5. The pass list holds "levels played" and the fail list "after the first 10 levels", so "after the first 10 levels played" (deck slide: "average CPM over the first 10 levels") matches both; the prompt report's fork K is that distinct-levels reading. A previous checked fix had removed "levels played" and added that phrase to the fail list. Fix: Fix List R28/R71.

**R28, R71** · weight 5 → 3 · F3. Blake's reply states the build timing in one sentence ("it runs when a player's 10th game ends, wins and losses both counted"), so the work is the same comparison as R29 (weight 3).

**After R29** · missing_coverage (M3) · Major · R3. Card rule 5 asks for the starting tier as the build has it; ZOM-42: "rest stays in tier 0"; Blake: "90 exactly stays on tier 0". Fix: the new row (worded so it doesn't repeat R29's threshold).

**After R47** · missing_coverage (M1) · Major · F2, F3, R3. Card rule 6: "comment on that ticket with what the build does"; Blake: "ZOM-199 says >= 90 after the first 10 levels" and the check "runs when a player's 10th game ends, wins and losses both counted". Fix: the new row.

**R49–R55** · non_atomic · Major · R7 (F2 and F3 listed it as unsure). The comment has two parts from different sources: the status (checklist "saying the change isn't in the store builds", decided by each ticket's closing note or Linear state and Blake's reply) and the builds (Leonard: "put the two builds in the comment (ios 0.3.49 and android 0.3.133) so people can see what you checked against"). The builds don't set the status, so the status-plus-citation exception doesn't apply (Eval 3 §2.2, QC …db9). Side not taken: "the builds are a qualifier of one claim"; Leonard asks for them as a separate addition. Fix: two rows per ticket.

**R69** · non_atomic · Major · F2, F3, R7; **R65–R69** overlap group · Moderate · F2, F3, R4. Leaving out ZOM-200 fails R66 and R69 together; a fifth key is already caught by R59's "4". Side not taken: F2's bare "lists exactly four keys" guard, because R59 already rejects the all-inclusive answer (Eval 3 §3.1). Fix: delete.

**R6, R7** · wording, not scored (QC B12) · F2, F3, R2. The justification arithmetic leaves out ZOM-258 (R6) and ZOM-312 (R7); the titles' 15 and 4 are right. Fix: Fix List R7; R6 under Worth a look.

### Worth a look (not scored)
- R6 justification (wording): it should name only the cuts that remove would-be Live tickets: Leonard's six analytics and tutorial tickets, ZOM-250 (his Sep 30 21:16 UTC reply), ZOM-258 (the notes doc) and ZOM-295 (PR 271 'not tiers'). ZOM-162, 163, 201 and 312 would have been Editor only, so they don't change the Live count. A rewrite listing every cut was checked and drew this point (R2, round 4), so reword it yourself if you want it tidy.
- Robert's "three things after status": no row grades column position. The prompt report's fork AG found the placement immaterial (both "after status"), and R24's deletion leaves position ungraded. Add a position row only if you want it graded.
- R44 accepts Leonard's access as owner of the ZM Difficulty folder; whether the Drive tool shows inherited access to the judge is unconfirmed (F2, F3).
- R43 weight 5 vs R45 weight 3 (F2, F3): R43 traces three records (rule 7, the checklist change, Leonard's later reply), R45 two; both weights fit their work.
- R35 "any other stated amount fails": ZOM-303's example ("that level will load the tier 0 version") is a one-tier drop, so it passes.
- Evidence for R8, R12–R19 and R21–R23 cites "team ZOM issues … and their closing notes" rather than comment IDs (F2); carried from earlier runs.
- R59 justification "Sep 30 21:16 reply" gives a UTC time without a zone (R2, fix round 1); grading unaffected.
- Unsampled Live cells rest on the counts, so an exactly offsetting swap would pass (sampling limit, R3 and R5).

### Rejected findings
- R40 not self-contained (R6): the title states the count of 10 and the counting rule, which the judge applies to the Agent's own rows; a volume control needs only its exact count (rubric_sampling.md).
- R27 should reject the UTC day (R5, R3 fix round 3): Local Override "when an instant falls on different PT and UTC days, a row grading the day accepts both".
- Tab-name cascade over R5–R27 / R28–R41 (F2): each content row must name its destination, R2/R3 define the accepted tab names as sibling titles, and a row whose tab was never made fails only because its own artifact is missing (Eval 3 §3.3).
- Build rows "iOS and Android in one row" (R7, fix round 1): both builds come from one tool output (Leonard's reply, Blake's mail), the same_tool_output exception in Eval 3 §2.2.

### Recommended Fixes
Every fix is in the Fix List with its mark. Checks run on the candidate (81 rows): `hg_rubric_ledger.py fixcheck` PASS (no title over 120 words, no bundled_writes or scope_tail hit), `hg_rubric_lint.py` 0 hits, self-check against Eval 3 §2 and the opposite-pair test, and R1–R7 on the changed rows and their siblings.
- Round 1 (all changed rows): clean except R5's carve-out (now in scope) and the new ZOM-280 done-day row (passed a run with no done-day column). Round 2: R5 bundled "each with a status" and left the note/block boundary unclear; the done-day row's closed list. Round 3: the done-day row's "where the done tickets show their done day" was a second claim; R5's evidence said "fails" instead of "counts toward the total". Round 4 (after restructure): the done-day row came back clean; R5 still drew a boundary finding (R5, R6), so it is marked "needs your own rewrite".
- Marks: R7 justification, the R28/R71 rewrites, the tier-0 row, the ZOM-199 timing row and the 14 rows replacing R49–R55: checked in round 1. The ZOM-280 done-day row: checked in round 4 after restructure. R24 and R69 deletions: checked (no pass found lost coverage). R5: revised after check, needs your own rewrite.

## Deep Recheck

Passes: R1, R2, R3, R4, R5, R6, R7, Opus 5.5 (claude-opus-5-5), session effort, each blind to the main review. FULL scope: all 73 rows; R4 compared every pair and R3 checked whole-rubric coverage. Full reviewers F2 and F3 ran alongside; their findings are merged in All Findings.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| R1 | 73 rows | 0 | 0 |
| R2 | 73 rows | 2 | 0 |
| R3 | 73 rows | 5 | 3 |
| R4 | 73 rows | 3 | 1 |
| R5 | 73 rows | 3 | 2 |
| R6 | 73 rows | 1 | 0 |
| R7 | 73 rows | 9 | 9 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | R2 | R6 justification "drops ZOM-295, which leaves 15 Live" | notes doc f_f494073fc667097c3c2c6b "leave ZOM-258 off the list" | §4 | wording | REJECTED | Title value 15 is right; supporting-field wording (QC B12), noted with a fix |
| DR2 | R2 | R7 justification "takes four tickets off the list, leaving ZOM-173, 200, 277 and 315" | harmonygames-Games/match3d#265#rc_7 | §4 | wording | REJECTED | Title value 4 is right; wording fix in the Fix List |
| DR1 | R3 | R47 "…strictly above 90 (> 90)…" | Blake's reply "it runs when a player's 10th game ends … ZOM-199 says >= 90 after the first 10 levels" | scope checklist | missing_coverage | CONFIRMED | M1 |
| DR2 | R3 | (no row) | Robert CAFC495E4006/1759229513.774912 "leave it blank if it never got done" | §4 | missing_coverage | CONFIRMED | M2 |
| DR3 | R3 | R24 evidence "in any order and position" | Robert "three things after status please" | §4 | missing_coverage | REJECTED | Prompt report fork AG: placement immaterial; listed under Worth a look |
| DR4 | R3 | R29 "…tier 1 only when their average CPM is above 90…" | ZOM-42 "rest stays in tier 0" | §4 | missing_coverage | CONFIRMED | M3 |
| DR5 | R3 | R5 "(left-off tickets listed without one of these statuses are not counted)" | D05HB64NMQU/1759262838.442871 "leave … off the list" | §4 | overly_broad | CONFIRMED | Merged with F2-7, F3-7 |
| DR1 | R4 | R69 "names exactly ZOM-173, ZOM-200, ZOM-277 and ZOM-315…" | D05HB64NMQU/1759262838.442871 | §7.7 | duplicate | CONFIRMED | Overlap group R65–R69 |
| DR2 | R4 | R69 weight 3 | R59 weight 5 | §7.9 | weight | REJECTED | Moot: R69 is deleted |
| DR3 | R4 | R49–R55 justification "Multi-source" at weight 3 | checklist 68dc033bf7d24e86b8a9cc67 | §7.9 | wording | REJECTED | Weight 3 fits; the split rows relabel the work kind |
| DR1 | R5 | R27 "(… the UTC day 2025-06-13 also passes)" | ZOM-200 completed_at 2025-06-13T01:17:38Z | §4 | overly_broad | REJECTED | Local Override: a row grading a day whose PT and UTC days differ accepts both |
| DR2 | R5 | R28 "…levels played…" | deck "average CPM over the first 10 levels" | §4 | overly_broad | CONFIRMED | Pass and fail lists collide |
| DR3 | R5 | R71 "…levels played…" | same | §4 | overly_broad | CONFIRMED | Same as DR2 |
| DR1 | R6 | R40 "exactly 10 monster entries…" | Live tab f_0ba93ae0238d9ed4178212 | §4 | not_self_contained | REJECTED | Count and counting rule are in the title; volume control (rubric_sampling.md) |
| DR1 | R7 | R24 "a column each for … assignee, … done … and … priority" | Robert CAFC495E4006/1759229513.774912 | §7.4 | non_atomic | CONFIRMED | Three columns |
| DR2 | R7 | R69 "names exactly ZOM-173, ZOM-200, ZOM-277 and ZOM-315…" | closing notes cmt_bb9c4deb176b2c894ca6, cmt_b0aa45d307c981ce4487, cmt_98027df98af6fb30b763 | §7.4 | non_atomic | CONFIRMED | Filtered list plus exclusivity |
| DR3–DR9 | R7 | R49–R55 "…not in the store builds iOS 0.3.49 and Android 0.3.133…" | Leonard D05HB64NMQU/1759262838.442871 "put the two builds in the comment" | §7.4 | non_atomic | CONFIRMED | Status and builds from different sources |

Effect on verdict: Overall Rubric Quality FAIL (12 Major, 1 Moderate, 3 Minor); Criteria Weights NON-FAIL 4 (R28, R71); other dimensions unchanged.

Platform defects: none

### FINAL VERDICT: FAIL
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Score: 1
Execution status: COMPLETE
Review policy: rubric-revision-v10
Review mode: AUDIT
Reviewed JSON SHA-256: 45a9dacc2597c627334b8d4979a72b5e3e4f40a3257bddcfbf07928c7aadc93c
Review context SHA-256: 5e40396020855d7506f1541a3c99d9f68fea3da9760b1abb84cd98394d7fd6f7
Scoring record SHA-256: 2fa1c5c9f4b09781f72e94450a7822b7fe1892d570105d55068baa737527bafe
Eval version: task-quality-v1
Eval release SHA-256: 0040c6a5569823fe6d06951d448cd21bd669f1615bfb9557e176cd2d4b299c2e
Gate tier: localized
Coverage ratio: 86/89
Repairs: See findings
Evaluator model: Opus 5.5 (claude-opus-5-5), session effort
Next action: Apply the Fix List (rewrite R5 yourself), save the new rubric and send /rubric again
Evidence limits: None
