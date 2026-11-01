## RUBRIC EVALUATION REPORT

### Task: ZM difficulty baseline register (sheet with Tickets and Rules in force tabs, folder, shares, Linear comments, DM reply to Leonard)
### Persona: Julia Lawson - Product Manager
### Total Rubrics: 68 (Outcome: 67, Process: 1)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Review mode DELTA (run 2). The ledger plan locked 11 unchanged passing rows and 7 copied checked fixes, and gave a full review to 50 edited or new rows. Reviewers: this session plus deep-recheck passes R1–R7 on the target rows. The fixes then went through three fix-check rounds of R1–R7.

## Fix List

Copy these rows from the checked candidate rubric. Everything else stays as you submitted it.

- **R24** (Rules in force tab, starting-tier timing): the pass and fail lists don't settle the write-ups' level count. A run that copies the deck ("average CPM over the first 10 levels") as "after the first 10 levels" can pass. Card rule 5 says go by the build, which counts games, wins plus losses. Replace the title with: "The Agent states on the Rules in force tab of the ZM difficulty baseline register that a new player's starting tier is set once they have played 10 games (passes: wording that counts 10 games, attempts or plays, or a count of levels that says losses or replays count, with or without a CPM average over the first 10 levels beside it; fails: a count of levels with nothing saying losses or replays count ('after the first 10 levels', 'after the first 10 levels played', 'after 10 levels'), 'after level 10', 'once level 10 is cleared', or only a CPM average over the first 10 levels with no timing)". Copy the same Accept/Fail text into its evidence. Keep weight 5. (checked)
- **R25** (strictly above 90): "'>= 90' fails" can be read against Blake's own rules-tab line, "cpm > 90, not >= 90". Replace the title with: "The Agent states on the Rules in force tab of the ZM difficulty baseline register that a new player starts on tier 1 only when their average CPM is above 90 (any wording that the threshold is strictly above 90 passes, with or without saying the build does not use >= 90; giving the threshold as '90 or more' or '>= 90' fails)". Keep weight 3. (checked)
- **R36** (10 valued enrage entries): weight 3 is one level high. The Live tab already holds exactly 10 valued rows with the Magician and Plumber variants merged, so copying it is a lookup, the same as R32–R34 and R37. Set weight 1 and keep the title. (checked)
- **R66** (DM reply, starting-tier timing): the same gap as R24. Replace the title with: "The Agent tells Leonard in its DM reply that a new player's starting tier is set once they have played 10 games (passes: wording that counts 10 games, attempts or plays, or a count of levels that says losses or replays count, with or without a CPM average over the first 10 levels beside it; fails: a count of levels with nothing saying losses or replays count ('after the first 10 levels', 'after the first 10 levels played', 'after 10 levels'), 'after level 10', 'once level 10 is cleared', or only a CPM average over the first 10 levels with no timing)". Copy the Accept/Fail text into its evidence. Keep weight 5. (checked)

### Phase 1: Structural Validation
- Five-field completeness: 68 of 68. Outcome 67, Process 1 (R68). Weights are all 1, 3 or 5.
- Code checks (`hg_rubric_lint.py`): 0 hits on the submitted rubric and 0 on the candidate.
- Requirement coverage: 68 of 68 outcomes covered. The six gaps from the last run are now closed by R22 (title column), R37 (not copied yet), R42 (share guard), R50/R51 (ZOM-315 and ZOM-293 comments) and R67 (Slack guard).

### Phase 2: Per-Rubric Quality
| Row | Issue | Type | Severity |
|---|---|---|---|
| R24, R66 | The "levels played" allowance and the narrow fail list (level 10 only) let the deck's "after the first 10 levels" timing pass | overly_broad | Minor |
| R25 | The fail form "'>= 90'" can be read against a correct line that negates it ("cpm > 90, not >= 90") | harmless_specificity | Minor |

Atomicity: every target row grades one result. R20 (status plus replacing ticket), R32–R34 (speed and damage of one Live-tab row) and R37 (one Live-tab row) are one-record cases. R26 and R29 keep their thresholds with the windows, as qualifiers of one metric.
Over-specificity: no row rejects a valid answer. Facts checked: all titles, ticket keys, statuses, counts (24 / 16 / 4 / 3 / 1, 9 comments, 10 enrage entries, 3 shares besides Leonard), the ZOM-254 and ZOM-282 titles, ZOM-280 Canceled, the enrage values and the share roles match the records.

### Phase 3: Set-Level Quality
- Coverage: no gaps. The scope checklist found one row per write: 9 comment rows (R43–R51), each naming its ticket and fact; the bare guard R52 (decoy: Leonard's "no comments on them either" for ZOM-162/163/201/250); 4 share rows plus the guard R42 (decoy: the Domino Delights card "Share it with Brian and Vincent"); the DM rows R53–R66 plus the guard R67 (decoy: Vincent's #zombie-design request). There are no bundled writes or scope tails.
- Process audit: R68 is valid. It grades only the order (reply after the register's last create or move), every valid path follows that order, and the final state doesn't show it. No ordering check is missing.
- Duplicates, overlap and cascades: none. Register rows and reply rows are separate deliverables, and the guards are bare counts.
- Spot checks: Live status 5 samples (R8–R12, now including ZOM-42) with the R6 count; enrage values 3 samples with the R36 count, R35 and R37 graded directly; title column 1 sample (R22) with the R5 row count; Linear state R21 and R23.
- OE cross-check: every row maps to an OE step, with no conflicts. OE 26 and OE 41 pass R24, R25, R31, R36, R37 and R66.

### Phase 4: Issue Tally
| Severity | Count | % | Fails when | Status |
|---|---|---|---|---|
| Major | 0 | 0% | any | clear |
| Moderate | 0 | 0% | any | clear |
| Minor | 3 (R24, R25, R66) | 4.4% | ≥ 5% | under |

### Phase 5: Scoring
| Sub-Dimension | Score | Justification |
|---|---|---|
| Overall Rubric Quality | 5 | No Major or Moderate; Minor on 3 of 68 rows (4.4%) |
| Criteria Weights | 4 | 1 of 68 rows one level off (R36, 3 vs 1) |
| Rubric Category Balance | 5 | 67 Outcome, 1 Process |
| Process Rubrics | 5 | R68 valid; none missing |
| Agent-Centric Phrasing | 5 | Every title "The Agent …"; no tool names |
| Negative Criteria | 5 | No prohibition or absence-only row; guards reject an idle Agent |
| Predicted All-Fail gate | PASS | none |

**Lowest Sub-Dimension:** Criteria Weights, 4 (R36).
**Summary:** Every finding from the last run is fixed, and every value matches the records. What's left is the starting-tier timing wording on R24/R66, a small wording risk on R25 and one weight (R36), all with checked fixes.

## Changes Since Last Run

- Rows: 11 locked, 7 locked-checked-fix, 37 edited, 13 new, 0 re-checked, 25 removed. The removed rows are the ones the last Fix List deleted or replaced: the 10 "leaves ZOM-x off" rows, the old tier and enrage rows, the five comment rows now carried as checked copies, the contentless DM row, R71 and R73.
- Previous findings now fixed: the R2 tab bundle (split into R2/R3); the folder weight (R4 = 1); the Negative Criteria fail on the "leaves ZOM-x off" rows (removed, with R5–R7 as count guards); the R20 weight and the ZOM-42 sample (R9); the ZOM-282 title (R20); the threshold and window evidence (R25, R26, R29); the level-drop amount (R31); the enrage-cell weights (R32, R33, R35); the R43 parenthetical; the R40 evidence; the R55–R60 weights; the R58–R64 evidence; the R71 overlap (removed); the six missing outcomes (R22, R37, R42, R50, R51, R67); the missing Process row (R68).
- Previous "needs your own rewrite" rows: R24/R66 no longer contradict themselves, but the deck wording gap remains (fixed above). R36 is now self-contained, but its weight went back to 3 (fixed above). R68 is clean.
- Dismissals: none recorded.
- New scored findings: R24/R66 overly broad (Minor), R25 harmless specificity (Minor, found in fix-check round 1), R36 weight.

### Notes for QM (not scored)
- The R6 justification says the six-ticket cut "leaves 16 Live". 16 needs every cut, so this is loose wording in a supporting field and doesn't change grading.
- R8, R12, R56 and R58–R60 cite the collection "team ZOM issues created up to Aug 31 and their closing notes" rather than the specific comment IDs (for example cmt_ad5c9cc21508c9961089 for ZOM-221). Citing the exact comment would be a repair.
- The R40 folder-owner clause passes a run that never shares with Leonard. That's accepted, because Leonard owns folder d_96489e1e00a56685625939, so he already has access.
- On the fixed R24/R66, a hedged answer that names games and levels together ("after 10 games (the first 10 levels)") could be read against both lists. The fix-check rated this very unlikely, and the title's "played 10 games" core decides it.
- I extended the reviewer-built fact extract with two derived counts: the invitees other than Leonard and Julia, and the one reply conversation. They're used to bind R42 and R67. They're evidence only, not a task input.

### Recommended Fixes
All four fixes are in the Fix List. Fix-check: `hg_rubric_ledger.py fixcheck` and lint were clean on every round. All titles are within 120 words (R24 109, R66 102, R25 63). R1–R7 ran on the changed rows and their siblings (R25, R32–R35, R37 and R43):
- Round 1 confirmed the first R24/R66 draft's two opposite gaps: it was too literal on "played", and its CPM note was too open.
- Round 2 confirmed the "levels played" collision.
- Round 3 came back clean.
- R36 was clean in round 1, and R25 in rounds 2 and 3.

## Deep Recheck

Passes: R1, R2, R3, R4, R5, R6, R7, on Opus 5.5 (claude-opus-5-5), session effort, each blind to the main review. DELTA scope: the 50 target rows, with R4 comparing them against all rows.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| R1 | 50 rows | 0 | 0 |
| R2 | 50 rows | 0 | 0 |
| R3 | 68 rows | 0 | 0 |
| R4 | 50 rows | 3 | 1 |
| R5 | 51 rows | 2 | 2 |
| R6 | 49 rows | 3 | 2 |
| R7 | 50 rows | 0 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| R5-DR1, R5-DR2 | R5 | R24/R66 "any wording that counts 10 games, attempts or levels played passes … ('after level 10', 'once level 10 is cleared') fails" | deck f_048bf5e69f8e7f1a659a5c "average CPM over the first 10 levels"; TierManager.cs "if (totalGames == 10)"; WinHistory.cs "GetTotalWins() + GetTotalLosses()" | Broad | overly_broad | CONFIRMED | The deck's level count isn't failed, and card rule 5 says go by the build |
| R6-DR1, R6-DR2 | R6 | same R24/R66 text | same records | Self-contained | not_self_contained | CONFIRMED | Merged with R5-DR1/2 as overly_broad (QC B11). The title does define the target (10 games played); the gap is that it admits a plausible wrong answer. Not taken: Major not_self_contained |
| R6-DR3 | R6 | R36 "exactly 10 monster entries" | Live tab f_0ba93ae0238d9ed4178212 | Self-contained | not_self_contained | REJECTED | An exact output-volume count needn't name its members (Eval 3 §3.6). MonsterBase is named in sibling R33, and the Mayor1/Mayor2 reading doesn't change the count |
| R4-DR1 | R4 | R36 weight 3 | Live tab: 10 valued rows, variants merged, "Copy its Live tab as it stands" | Weights | weight | CONFIRMED | A literal copy from one source, like R32–R34 and R37 (expected 1) |
| R4-DR2, R4-DR3 | R4 | R24/R66 weight 5 | TierManager.cs, WinHistory.cs, ZOM-42, deck | Weights | weight | REJECTED | Eval 3 §2.12 weighs the work for the result the title names: 10 games played comes only from the build, traced over the write-ups under rule 5 (multi-source). The breadth gap is recorded separately |

Fix-check rounds also confirmed one defect in the submitted rubric: R25's fail form (R1, round 1). It's recorded as Minor harmless_specificity, because R25's first clause still passes the negating line.

Fix-check rejections:
- R5 round 1 asked that R36 count values invented for Mailman/Mayor2/PartyGirl. That would make R36 fail together with R37 on one error, a cascade (the Eval 3 cascading-failure override).
- R1 round 2 and R6 round 2 flagged "average" in R43. Blake's "cpm > 90, not >= 90" satisfies R43's "(> 90)", so no comment is rejected.
- R2 round 3 and R3 round 3 raised hedged games/levels glosses. These are very unlikely paths (QC B11 exception), and R1 and R6 in the same round agreed. R2 round 3 also flagged the CPM-window carve-out. R24 grades only the timing, and failing a window mention would add an unrequested check (Eval 3 §2.7), the opposite defect from the last run.

Effect on verdict: Overall Quality 5 (3 Minor rows, 4.4%), Criteria Weights 4 (R36). Verdict NON-FAIL.

Platform defects: none

### FINAL VERDICT: NON-FAIL
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Score: 4
Execution status: COMPLETE
Review policy: rubric-revision-v10
Review mode: AUDIT
Reviewed JSON SHA-256: 7b568acf935a32ad16bea7c3a892a404a44e6eac4ab796036bca18152e8120b4
Review context SHA-256: 8e38c713e36ab7c1e7ecc44436576c5845e901b904d0ab9166a6bd13696a695c
Scoring record SHA-256: 25f602c93a1cd935e9567851ca240663fe73758667f95f3e2dda3e51e8de831e
Eval version: task-quality-v1
Eval release SHA-256: 0040c6a5569823fe6d06951d448cd21bd669f1615bfb9557e176cd2d4b299c2e
Gate tier: localized
Coverage ratio: 68/68
Repairs: See findings
Evaluator model: Opus 5.5 (claude-opus-5-5), session effort
Next action: Optional: apply the four checked fixes (R24, R25, R36, R66) and send /rubric again for a clean PASS
Evidence limits: None
