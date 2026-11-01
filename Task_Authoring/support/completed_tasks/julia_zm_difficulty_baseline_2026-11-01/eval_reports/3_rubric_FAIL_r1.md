## RUBRIC EVALUATION REPORT

### Task: ZM difficulty baseline register (sheet with Tickets and Rules in force tabs, folder, shares, Linear comments, DM reply to Leonard)
### Persona: Julia Lawson - Product Manager
### Total Rubrics: 73 (Outcome: 73, Process: 0)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Review mode FULL (first run). Reviewers: F1 (this session), F2, F3, deep-recheck passes R1–R7, and four fix-check rounds on the candidate rubric.

## Fix List

Rows are original numbers (R#). The checked candidate rubric (68 rows, C#) is the saved fix file; copy its rows.

- **R2**: bundles two tabs in one row. Split into C2 "…a tab named Tickets (a tab name containing the word Tickets passes)" and C3 "…a tab named Rules in force (a tab name containing the word Rules passes)", w1 each. (checked)
- **R3**: weight 3 for a folder the prompt names. Set w1. (checked)
- **R4**: once R7–R18 are gone this is the only exclusion guard, and a "note" can hide left-off rows. Use C5: "…with exactly 24 ticket rows with a status of Live, Editor only, Replaced or Not shipped (left-off tickets listed without one of these statuses are not counted)". (checked)
- **R4–R6, R59–R63**: evidence names no record. Cite the card, both DM replies, the notes doc, PR #265 rc_7 and the store-builds mail (done in candidate). (checked)
- **R7–R18**: pass when the key is absent ("leaves ZOM-x off"), so an empty or partial Tickets tab passes all 12 (Negative Criteria FAIL). Delete them; the exact counts in R4/R5/R6 are the guard. (checked)
- **R20**: weight 5 for the same work as R19 (w3), and ZOM-42, which card rule 4 names, is not sampled. Replace with C9 "The Agent records the status Live for ZOM-42 on the Tickets tab…", w1. (checked)
- **R31**: "(key or title)" accepts a title no row states. Use C20, which writes out ZOM-282's title. (checked)
- **R33 / R73**: the title requires "with wins and losses both counting" but also passes a bare "10 games", and the evidence lists differ. **Needs your own rewrite** (C24/C66 still fail after 4 rounds). Open problem: the fail phrase "the first 10 levels" also catches correct answers that use it to describe the CPM window ("average CPM of the first 10 levels, set after 10 games played"). Limit the fail list to the timing statement only, and keep "the first 10 levels played" and "after the first 10 games" passing (prompt review P1-DR3).
- **R34**: requires a separate "exactly 90 stays on tier 0" statement, and the evidence is narrower. Use C25 "…starts on tier 1 only when their average CPM is above 90 (any wording that the threshold is strictly above 90 passes; '90 or more' or '>= 90' fails)". (checked)
- **R35 / R38**: the evidence ("Accept: 80% 10") is wider than the title. ZOM-42 itself words the window both ways ("last 10 attempts" and "UP TO THE MOST RECENT 10 attempts"). Use C26 and C29, which accept either wording, both w1. (checked)
- **R40**: "drops one tier" grades an amount that rule 5 ("whether the level drops") never asks for, and OE 26's "yes" fails it. Use C31 "…also drops in difficulty (that level dropping with no amount stated, or by one tier, passes; any other stated amount fails)", w1. Also remove Blake's #zombie-design note from its evidence. (checked)
- **R41, R42, R44**: these copy Live-tab cells, the same work as R43, so set w1. In R44's evidence, replace ZOM-303 with ZOM-282's closing note cmt_912bdd42ad5c8d51521f. (checked)
- **R45**: "copied from the Live tab" checks 7 monsters' values that no row names. **Needs your own rewrite** (C36). Make it a bare count of 10 valued monster entries (VarC splits count as one; Mailman/Mayor2/PartyGirl rows not counted). Don't refer to "valued Live-tab rows", because the prompt and titles never name that sheet.
- **R48**: the evidence drops the folder-owner route the title allows. Make the evidence match the title. (checked)
- **R50**: "(so exactly 90 stays on tier 0)" reads as required content, but the evidence passes without it. Use C43 "…saying the build's starting-tier check is an average CPM strictly above 90 (> 90), with or without mentioning >= 90". (checked)
- **R58**: a contentless reply passes it; R59–R73 already name the DM. Delete it. (checked)
- **R61 / R71**: they overlap on the Editor-only count in the reply. Delete R71, and set R61 to w5 (same work as R6). (checked)
- **R62 → w3, R63 → w3, R64–R66 → w1**: weights that don't match the same work on sibling rows. (checked)
- **R64–R70**: evidence "key in any format" is wider than the title. Use "Accept: 'ZOM-202' Not shipped" and cite records, not "the 24-row register". (checked)
- **Add** C22 "The Agent records ZOM-254's title, Blunder Mechanic 2.0 enrages zombies instead of HP penalty, on the Tickets tab… (any letter case)", w1, because nothing grades the title column. (checked)
- **Add** C23 "…ZOM-280's Linear state as Canceled… (Cancelled also passes)", w1, an edge sample for the Linear state column. (checked)
- **Add** C37 "The Agent lists Mailman, Mayor2 and PartyGirl on the Rules in force tab… with their enrage speed and damage marked as not copied yet (any wording that their values have not been copied yet passes; one combined row or one row per monster passes)", w1, which rule 5 requires. (checked)
- **Add** C42 "The Agent shares the ZM difficulty baseline register with exactly three people other than Leonard Hayes (Julia Lawson, the owner, is not counted)", w1, a guard against the Domino Delights card's "Brian and Vincent". (checked)
- **Add** C50 / C51: comments on ZOM-315 and ZOM-293 "saying its change is missing from the store builds (any wording that the store builds lack the change passes)", w3; both are required by the checklist. (checked)
- **Add** C67 "The Agent posts Slack messages in exactly one Slack channel or DM (several threads or top-level messages in the same DM count as one)", w1, a guard against Vincent's #zombie-design request. (checked)
- **Add a Process row (reply after the register is in the folder)**. **Needs your own rewrite** (C68). The draft "…only after the register is in the ZM Difficulty folder" fails together with R3's folder row when a run misses the folder. Grade only the order: the reply comes after the step that creates or moves the register.

### Phase 1: Structural Validation
- Five-field completeness: 73 of 73; all Outcome; weights 1/3/5.
- Requirement coverage: 74 of 80 outcomes (6 missing: M1–M6 below).

### Phase 2: Per-Rubric Quality
| Row | Issue | Type | Severity |
|---|---|---|---|
| R2 | two tabs in one row | non_atomic | Major |
| R31 | accepts ZOM-282's title, which no title states | not_self_contained | Major |
| R33, R73 | title contradicts itself and its evidence on the wins/losses clause | not_self_contained | Major |
| R34 | separate "exactly 90" clause; evidence narrower | overly_specific + not_self_contained | Major |
| R35, R38 | evidence wider than title | not_self_contained | Major |
| R40 | "one tier" amount not asked; fails OE 26 | overly_specific | Major |
| R45 | values of 7 unnamed monsters | not_self_contained | Major |
| R50 | parenthetical vs evidence | not_self_contained | Major |
| R64–R70 | evidence "key in any format" wider than title | not_self_contained | Major |
| R61, R71 | Editor-only count embedded twice in the reply | duplicate (overlap group) | Moderate |
| R58 | contentless reply passes | overly_broad | Minor |
| R48 | evidence narrower than title (no grading change) | harmless_specificity | Minor |
| R7–R18 | absence-only acceptance ("leaves ZOM-x off") | Negative Criteria dimension | FAIL |

Atomicity: R2 is the only bundle. R31, R41–R43 and the Mailman row are kept whole (one record / one tool output). Thresholds kept with their windows (qualifiers of one metric, Eval 3 §2.2).

### Phase 3: Set-Level Quality
- Coverage gaps: M1 Mailman/Mayor2/PartyGirl "not copied yet" (rule 5); M2 comment on ZOM-315; M3 comment on ZOM-293 (checklist rule 6 change; sampling isn't allowed without a template volume row); M4 title column (rule 2); M5 share guard (Domino Delights card decoy); M6 Slack guard (Vincent's #zombie-design request).
- Process audit: 0 Process rows. One ordering check is genuinely missing (reply after the register is in the folder: "then reply", "reply here when it's in the folder"), which gives Process NON-FAIL 3.
- Duplicates / overlap: one group (R61, R71).
- Spot checks: Live status 5 samples + R5 count (repair: cover ZOM-42); enrage values 3 samples + R45 count; Linear state 1 sample (repair: add a non-Done edge).

### Phase 4: Issue Tally
| Severity | Count | % | Fails when | Status |
|---|---|---|---|---|
| Major | 23 (17 rows + 6 missing) | 31.5% | any | FAIL |
| Moderate | 1 | 1.4% | any | FAIL |
| Minor | 2 | 2.7% | ≥ 5% | under |

### Phase 5: Scoring
| Sub-Dimension | Score | Justification |
|---|---|---|
| Overall Rubric Quality | 1 | 23 Major, 1 Moderate |
| Criteria Weights | 2 | 24 of 73 rows one level off (R3, R7–R17, R20, R38, R40, R41, R42, R44, R61–R66) |
| Rubric Category Balance | 5 | all Outcome |
| Process Rubrics | 3 | one missing ordering check |
| Agent-Centric Phrasing | 5 | every title "The Agent …" |
| Negative Criteria | 1 | R7–R18 |
| Predicted All-Fail gate | PASS | none |

**Lowest Sub-Dimension:** Overall Rubric Quality and Negative Criteria, 1.
**Summary:** All the counts and values match the records (24 rows: 16 Live, 4 Editor only, 3 Not shipped, 1 Replaced; 9 comments; the build's 10 games and > 90). The rubric fails on six missing outcomes, twelve "leaves X off" rows, several titles whose acceptance hangs on supporting fields, and weights.

## All Findings

- **M1 (Major, missing_coverage)**, raised by F1, F2, F3, R3 and R5. Rule 5: "a monster it hasn't copied yet goes on the tab as not copied yet". Live tab row ["Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP)", "not copied yet", …]. R45 only places it "outside the 10". Fix: C37.
- **M2 / M3 (Major)**, raised by F1, F2, F3 and R3. Checklist item 68dc033ba50fbef6a9b12b19 says "the Editor only and Not shipped tickets get a comment too". There are no rows for ZOM-315 (Editor only) or ZOM-293 (Todo). R57 doesn't state the template, so sampling isn't allowed. Fix: C50, C51.
- **M4 (Major)**, raised by F1, F2, F3 and R3. Rule 2 lists "ticket, title, Linear state…", and no row grades a title. Fix: C22.
- **M5 (Major)**, raised by F3. Domino Delights card 683dbef4e319167a802bd888 says "Share it with Brian and Vincent, both can edit", a real extra-target decoy. Fix: C42.
- **M6 (Major)**, raised by R3 (fix round 1). Vincent writes in #zombie-design (C090N54TG79/1759248760.118527): "can you drop it in here too". Fix: C67.
- **R2 (Major, non_atomic)**, raised by F1, R7 and UNSURE in F2/F3. Fix: C2/C3.
- **R7–R18 (Negative Criteria FAIL)**, raised by F2, F3, R6 and the lint (disguised_negative). Absence-only acceptance (Local Override), so a 5-row Tickets tab passes all 12. Fix: delete them; R4 is the count guard.
- **R31 (Major)**, raised by R6. ZOM-282's title appears in no title. Fix: C20.
- **R33 / R73 (Major)**, raised by F2, F3 and R6. Fix: needs your own rewrite (see the Fix List).
- **R34 (Major)**, raised by F2, F3, R6 and R7. Fix: C25.
- **R35 / R38 (Major)**, raised by F3 and R6. Fix: C26/C29.
- **R40 (Major)**, raised by F1, F3 and the OE conflict check. OE 26 says "Level drop after a demotion: yes (ZOM-303)", which fails R40. The records back the OE, so the row is what needs fixing (FIX_ROW). Fix: C31.
- **R45 (Major)**, raised by R6 and R7. Fix: needs your own rewrite (see the Fix List).
- **R50 (Major)**, raised by R6 and R7 (fix rounds). Fix: C43.
- **R64–R70 (Major)**, raised by R6 (fix round 3). Fix: match the evidence to the title.
- **R61/R71 (Moderate)**, raised by F2, F3 and R4. Fix: delete R71.
- **R58 (Minor)**, raised by F2. Fix: delete it.
- **R48 (Minor)**, raised by R6 (fix round). Fix: evidence.
- **Weights (24 rows)**, raised by F2, F3 and R4: R3, R7–R17 (literal list from one message), R20, R38, R40, R41, R42, R44, R61, R62, R63, R64–R66. Fix: as in the Fix List.
- **Missing Process (NON-FAIL 3)**, raised by F1, F2, F3 and R3. Fix: add a Process row (needs your own rewrite; see the Fix List).

### Worth a look (not scored)
- R40/R44 evidence cites records that don't hold the value (Blake's note for the level drop; ZOM-303 for hp). Raised by F2, F3 and R2. These are repairs; grading is unchanged.
- The justifications in R34–R45 end with a copied sentence about "10 levels played", and R1 and R19–R23 repeat sentences. R2 cites "Brief §4b", R59–R63 cite "Gate 6", and R5/R6 have dangling "those six"/"them". Raised by F2 and F3. These are wording repairs, applied in the candidate.
- Live samples: ZOM-42 (named in rule 4) is protected only by the R5 count. Raised by F2, F3 and R3; the candidate swaps it in.
- Unsampled Live cells and the left-off tickets now rest on the counts, so a compensating swap (ZOM-258 in, ZOM-378 out) passes. This is a sampling limit (rubric_sampling.md).
- C61–C64 justifications could cite the store-builds mail. Raised by R4 in round 4.

### Rejected findings
- R7–R18 as a sampling overlap group (F2-6, F3-2): these rows cover every exclusion each source lists, so they aren't samples (rubric_sampling.md: "no automatic row-count threshold … to shrink an otherwise valid exhaustive rubric").
- ZOM-42 as missing_coverage (F2-4, R3-DR4): R5 (exact Live count) and R4 reject both the omission and a wrong status, and a weak sample choice is a repair (rubric_sampling.md). The fix is still provided.
- R48 overly broad (F3-16, R5): folder d_96489e1e00a56685625939 is owned by Leonard, so his access through the folder is the real end state, not a wrong answer.
- "Reply must say it's in the folder" (F3-7, R3-DR6): the ask's "when it's in the folder" is timing, and it's covered by the Process gap.
- Threshold + window splits on R35/R38 (R7): these are qualifiers of one metric (Eval 3 §2.2).
- Speed + damage splits on R41–R43 (R7): components of one tool output may be grouped (QC Appendix).
- "10 levels played" overly broad on R33/R73 (R5): the prompt review (P1-DR3) accepted it, and Eval 3 §1.4 says forks follow the prompt report.
- Cascades from one missed source message (R4: count rows, comment rows): these share a root cause, not an embedded condition (Eval 3 §3.3).
- R57's justification listing the 9 tickets (R6): this is verification guidance (§2.1).
- Supporting-field citations on R40/R44 as Major incorrect (F3-10/11): the title values are right and the correct record is also cited, so grading is unaffected and they're kept as repairs.
- Fix-round items on guards C42/C52/C67 naming targets: the scope checklist prescribes a bare count with no id list.
- C26/C29 "accepts deck wording" (R5 round 3): ZOM-42's own heading reads "Promotion Rules based on win record of last 10 attempts".
- C37 as a three-monster bundle (R7 round 2): it's one Live-tab row, and splitting it would create a cascade.

### Recommended Fixes
The fixes above are each marked with their check result. Fix-check: lint and fixcheck were clean on the candidate. R1–R7 ran on the changed rows and their siblings in rounds 1–4 (round 4 was the restructure check). C24, C36, C66 and C68 are marked revised and need your own rewrite. Every other changed row came back clean in a round.

## Deep Recheck

Passes: R1, R2, R3, R4, R5, R6, R7, on Opus 5.5 (claude-opus-5-5), session effort, each blind to the main review.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| R1 | 73 rows | 0 | 0 |
| R2 | 73 rows | 2 | 2 |
| R3 | 73 rows | 6 | 5 |
| R4 | 73 rows | 13 | 9 |
| R5 | 73 rows | 4 | 1 |
| R6 | 73 rows | 7 | 6 |
| R7 | 73 rows | 8 | 2 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| R2-DR1 | R2 | R40 evidence "Blake's #zombie-design note" | C090N54TG79/1756912929.304417 is about enrage | Incorrect | Supporting field | CONFIRMED | Kept as a repair (title value right) |
| R2-DR2 | R2 | R44 evidence "ZOM-303 description" | ZOM-303 is about demotion | Incorrect | Supporting field | CONFIRMED | Kept as a repair |
| R3-DR1/2 | R3 | checklist rule 6 change | ZOM-315, ZOM-293 | Coverage | missing_coverage | CONFIRMED | M2, M3 |
| R3-DR3 | R3 | rule 5 "not copied yet" | Live tab last row | Coverage | missing_coverage | CONFIRMED | M1 |
| R3-DR4 | R3 | rule 4 "ZOM-42 … stays Live" | ZOM-42 Done | Coverage | missing_coverage | REJECTED | Count controls reject both tests; repair given |
| R3-DR5 | R3 | rule 2 "title" | card 68daca58… | Coverage | missing_coverage | CONFIRMED | M4 |
| R3-DR6 | R3 | "reply here when it's in the folder" | DM 1759261706.530914 | Coverage | Process | CONFIRMED | Process gap (folder-statement part rejected) |
| R4-DR1–3 | R4 | count / comment rows | DM replies, checklist | Cascade | duplicate | REJECTED | Shared root cause (§3.3); R61/R71 part kept |
| R4-DR4–13 | R4 | R3, R7–R17, R20, R38, R40, R61, R62, R63, R64–R66 weights | §7.9 | Weights | weight | CONFIRMED | In weight_reviews |
| R5-DR1 | R5 | R48 folder-owner clause | folder owner leonard.hayes | Broad | overly_broad | REJECTED | Owner access is the real end state |
| R5-DR2/3 | R5 | R33/R73 "10 levels played" | prompt review P1-DR3 | Broad | overly_broad | REJECTED | Prompt report accepted it |
| R5-DR4 | R5 | R45 not-copied row | Live tab | Broad | missing_coverage | CONFIRMED | Merged into M1 |
| R6-DR1 | R6 | R31 "(key or title)" | ZOM-282 title | Self-contained | not_self_contained | CONFIRMED | Issue on R31 |
| R6-DR2 | R6 | R45 "copied from the Live tab" | Live tab | Self-contained | not_self_contained | CONFIRMED | Issue on R45 |
| R6-DR3 | R6 | R57 justification | — | Self-contained | not_self_contained | REJECTED | Verification guidance (§2.1) |
| R6-DR4–6 | R6 | R34, R33, R73 evidence | rows' evidence | Self-contained | not_self_contained | CONFIRMED | Merged |
| R6-DR7 | R6 | R7–R18 idle condition | — | Self-contained | Negative | CONFIRMED | Merged into the Negative finding |
| R7-DR1 | R7 | R2 two tabs | agenda | Atomic | non_atomic | CONFIRMED | Issue on R2 |
| R7-DR2/3 | R7 | R35, R38 threshold + window | ZOM-42 | Atomic | non_atomic | REJECTED | Qualifier of one metric |
| R7-DR4–6 | R7 | R41–R43 speed + damage | Live tab | Atomic | non_atomic | REJECTED | One tool output |
| R7-DR7 | R7 | R45 count + values | Live tab | Atomic | not_self_contained | CONFIRMED | Merged with R6-DR2 |
| R7-DR8 | R7 | R34 "and that exactly 90" | Blake's reply | Atomic | overly_specific | CONFIRMED | Merged into R34 |

Fix-check rounds also confirmed these defects in the original rubric: M6 (R3), R48 (R6), R50 (R6, R7), R64–R70 (R6) and the R44 weight (R4). All are recorded.

Effect on verdict: Overall Quality stays at 1, and Criteria Weights moved to 24 rows off. Verdict unchanged: FAIL.

Platform defects: none

### FINAL VERDICT: FAIL
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Score: 1
Execution status: COMPLETE
Review policy: rubric-revision-v10
Review mode: AUDIT
Reviewed JSON SHA-256: 61d9756d7760475073f2e94a34dd231ba366e3e2b38c6b1f2a5d11329f8d701e
Review context SHA-256: f73a230012d59484ec00144bd767fcc9b65f23c5df7c81f7301b0e3534ab414e
Scoring record SHA-256: 321efe83e9727f344080ac9782e7f5a26a0c24baa6cb6ac1a13dc4b5508e4eb4
Eval version: task-quality-v1
Eval release SHA-256: 0040c6a5569823fe6d06951d448cd21bd669f1615bfb9557e176cd2d4b299c2e
Gate tier: localized
Coverage ratio: 74/80
Repairs: See findings
Evaluator model: Opus 5.5 (claude-opus-5-5), session effort
Next action: Apply the Fix List (rewrite C24/C66, C36 and the Process row yourself), save the new rubric and send /rubric again
Evidence limits: None
