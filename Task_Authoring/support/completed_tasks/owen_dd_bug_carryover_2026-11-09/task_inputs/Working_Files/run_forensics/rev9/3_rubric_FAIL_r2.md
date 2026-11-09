## RUBRIC EVALUATION REPORT

### Task: DD bug carry-over from Slack to Linear, UI Changes tree close-out, carry-over sheet and threaded reply to Arthur
### Persona: Owen Baker - Game Engineer (Unity)
### Total Rubrics: 138 (Outcome: 137, Process: 1)

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

## Fix List

Run 2 (DELTA). You applied last run's checked fixes, and the counts, states, ties, build, shares and reply numbers all still match the records. One row still fails.

| Row | What is wrong | Fix to copy | Mark |
|---|---|---|---|
| R3 | The title asks for the first line "after the prefix", so it also requires the [2231] prefix. The prefix comes from a different source (Arthur's ENG-2401 comment), and R1 already grades it on every issue. A run that copies the line exactly but forgets the prefix fails R3 for the wrong reason. | **This row needs your own rewrite.** The row should grade one thing: the words of the flickering issue's title are exactly the post's line "Any idea what might cause this flickering?". The title itself has to say that a [2231] prefix is allowed but not required, and that any spacing or punctuation after it is fine ("[2231] Any idea…", "[2231]Any idea…", "[2231] - Any idea…" and "Any idea…" all pass). The Accept/Reject text must accept exactly what the title says, no more and no less. Paraphrases and added words must still fail. Four drafts failed the check: "includes … word for word" (accepts added words), "exactly, after the [2231] prefix" (rejects "[2231]Any idea…"), the same title with evidence accepting any separator (evidence wider than the title), and "its only words besides the [2231] prefix" (reads as requiring the prefix). | revised after check |

No other row needs to change. Once R3 grades only the title text, with the prefix clearly optional in its title, nothing else in this review fails. The QM notes below are optional and don't affect the score.

---

### Phase 1: Structural Validation
- Five-field completeness: 138 of 138. Categories are valid and weights are 1/3/5.
- Category distribution: Outcome 137, Process 1 (R138).
- Requirement coverage: 139 of 139 outcomes. The extra one is the prefix that R3 embeds.

### Phase 2: Per-Rubric Quality (target rows)
| Row | Issue | Type | Severity |
|---|---|---|---|
| R3 | The first-line title rule and the [2231] prefix ("after the prefix") are checked in one row. They come from two sources and can fail separately. | non_atomic | Major |

Atomicity: every other target row checks one result. R1, R79 and R120 are the volume rows of their spot-check groups (template fields; the 14 moves; the sheet cells), which Rubric Writing §8 allows. R135 is a single total the prompt asks for. Over-specificity: none. Each count row's acceptance search settles every other candidate item (below). Lint: the count_claim/count_bundle hits on R1, R79 and R120 are volume rows. The anon_token hits on R27, R28, R53, R58, R59 and R69 match the source text as shown. The format_lock hit on R46 ("single character") is canvas line text, not a format. The evidence_no_record hit on R138 cites the prompt itself, which is fine for an ordering row.

Acceptance searches:
- **R1 (68):** SETTLED_AGAINST. Searched: 69 canvas roots (63 lines and 6 empty), 7 posts after the last line, Vincent's mail and comment, and the open ENG tickets with Arthur's narrowing comments. The deleted-line comments and the two Covered lines are excluded by the notes.
- **R79 (14):** SETTLED_AGAINST. Brian's shop-icon regression does not hold ENG-2432 or ENG-2433, because the notes say "A bug on a screen doesn't hold its child".
- **R120 (70):** SETTLED_AGAINST. The notes leave out deleted lines, follow-ups, the QA-doc post and the design question.

Previous findings on target rows: all fixed. That covers the R1 count and scope tail, the R2–R7 "every/all" bundles, the "[2231]" cascade on the state rows, the R19 mention and R23 first line, the R28 justification, the R37–R41 reason requirement, the R42 bundle and the folder cascade. It also covers the weights. R88 is now w5, the same as R89, which closes last run's open "needs your own rewrite" item.

### Phase 3: Set-Level Quality
- **Coverage gaps (scored):** none. Two coverage gaps go under Notes for QM: they were already there before this version and the prompt doesn't state them outright.
- **Process audit:** 1 of 1 valid. R138 is the "Then reply" order, which no Outcome row can see.
- **Duplicates, overlap and cascade groups:** none.
  - The old "[2231]" and folder cascades are gone.
  - Volume rows are not duplicates of their samples (Eval 3 §3.3).
  - Rows that share only a likely root cause are not a group: the Tavern line, the Apple tie, the lives line and the tile dozer post each show up in the ticket, sheet and reply rows.
- **Spot-check groups:**
  - Template fields: R1 states the template; R2–R8 are one sample per field.
  - UI moves: R79 is the volume row; R80–R84 are five samples, three of them on the shop-icon trap.
  - Sheet Outcome cells: R120 is the volume row; R127 is the Fixed case, and R122, R125, R126 and R128 cover Broken, unmerged PR, Gone and Covered.
  - Sheet Ticket cells: R121 plus the two Covered ties (R123, R124).
  - Sheet Why cells: R130 and R129.
  - Every group is within the five-sample cap.
- **OE cross-check:** every row maps to its OE steps (OE 1–150). No conflicts.

### Phase 4: Issue Tally
| Severity | Count | % | Fails when | Status |
|---|---|---|---|---|
| Major | 1 (R3) | 0.7% | any | FAIL |
| Moderate | 0 | 0% | any | PASS |
| Minor | 0 | 0% | ≥ 5% | PASS |

### Phase 5: Scoring
| Sub-Dimension | Score | Justification |
|---|---|---|
| Overall Rubric Quality | 1 | One Major: R3 is not atomic |
| Criteria Weights | 5 | All 138 weights match the QC work kind |
| Rubric Category Balance | 5 | 137 Outcome rows |
| Process Rubrics | 5 | R138 is valid |
| Agent-Centric Phrasing | 5 | Every title starts "The Agent" and names no tool |
| Negative Criteria | 5 | No prohibition; an idle Agent fails every row |
| Predicted All-Fail gate | PASS | No row fails every run |

**Lowest Sub-Dimension:** Overall Rubric Quality, 1. R3 also requires the [2231] prefix ("after the prefix").
**Summary:** Last run's fixes all landed, and the values match the records. One row, R3, still checks two things from two sources. It needs your own rewrite along the lines in the Fix List.

### Recommended Fixes
1. R3: revised after check, needs your own rewrite. The draft went through 3 rounds plus a restructure. Each round ran fixcheck, lint, a self-check with the opposite-pair test, and passes R1–R7 on R3 and its siblings (R1, R2, R4–R8, R25). Every round confirmed a new defect in the draft: added words passed, a no-space prefix failed, the evidence was wider than the title, and the prefix read as required. The Fix List states what the rewrite has to do.

## Changes Since Last Run

- **Rows:** 138 in total. 6 locked, 56 locked-checked-fix, 26 edited, 48 new, 2 re-checked (R79, R118). 27 previous rows were removed or replaced by the checked fixes.
- **Previous findings now fixed:**
  - R1 scope tail and count bundle.
  - The R2–R7 template and count bundles.
  - The "[2231]" cascade (R8–R28).
  - R19 mention.
  - R23 first line.
  - R28 justification.
  - The R37–R41 reason requirement.
  - The R42 bundle and the R42/R43 overlap.
  - The folder cascade (R44–R56).
  - The R47 bundle.
  - R57 and R58 breadth.
  - R31 offsetting moves: the ENG-2433 sample is now R82.
  - All 20 weight mismatches.
  - R40/R41 weight parity: R88 is now w5.
- **Dismissals:** none recorded.
- **New scored findings:** R3 non_atomic (Major), found by deep-recheck pass R7.
- **Locked rows:** no factual error or code-check hit.

### Notes for QM (not scored)
- **Done children's lines:** Arthur asks for "a line on every child saying where it landed". On the 23 children that end Done, R95–R117 check the build (0.3.310) but not that the line says "Done". This version reads "where it landed" the same way the last one did (R42 graded the build only), so no change caused the gap. If you want it covered, add one row per child, for example "The Agent states in its comment on ENG-2410 (Shop UI Optimization) that the ticket is Done" (w1).
- **Canvas-line title text:** the notes' title rule is "the line without its tick box, or the first line of the post, as it was written". R3 samples it on a post only; no row samples a canvas line (61 of the 68 issues). This was already a gap last run. An optional sample: "The Agent titles the issue it files for canvas line "offers has no visuals." "offers has no visuals." exactly, without the tick box, after the [2231] prefix if it adds one" (w1).

### Worth a look (not scored)
- **R79 and the masters.** ENG-2403's 15 children all end Done, and a run might close the group too. The notes say "the masters stay as they are", but no required reply or report can carry that, so under count-bundle-v1 this decoy gets no row and it isn't a coverage gap.
- **R84's justification** links Brian's shop-icon regression to the Shop child. Brian's message says "I was back in the shop prefabs today", so that's a fair reading, and the Done outcome is right either way.
- **0.3.305 vs 0.3.310.** Leonard's Feb 10 post calls 0.3.305 the "latest public build". The Feb 12 notes name 0.3.310 and are newer, so 0.3.310 stands, and R90–R116 reject 0.3.305 by name.

### Rejected findings
- **R6-DR1** (R79 not self-contained): R79 is the volume row of the moves group. Rubric Writing §8 asks for "one criterion checking the volume of the output (its exact count or total)"; the five samples name the children.
- **R3-DR2** (nine moves have no row): depends on R79 being removed. R79 stands as the volume row.
- **R3-DR1** (Done-status part of the 23 Done children's lines): moved to Notes for QM. DELTA rule: "A coverage gap that no change caused goes to Notes for QM unless the prompt states that requirement outright."
- **R5-DR1 and R5-DR3** (offsetting sets pass R79 and R1): both are volume rows by design (Rubric Writing §8). Their samples carry the traps.
- **R5-DR2** (masters closed): a decoy no required reply or report can carry gets no row, and that is not missing coverage (Eval 3 §3.1, count-bundle-v1). R79's own predicate, the children moved, is unaffected. Listed under Worth a look.
- **R5-DR4** ("stays open" passes a held child moved backward): no record suggests moving a held child back, so the wrong path is very unlikely (QC B11).
- **R5-DR5** (R135 doesn't require the thread): R134 grades the thread. Repeating it in R135–R137 would make one miss fail four rows (Eval 3 §3.3 cascade).
- **R4-DR1 and R4-DR2** (R1 and R79 duplicate their samples): Eval 3 §3.3 says "Not duplicates: … a spot-check group's one output-volume row versus its samples".
- **R4-DR3 to R4-DR10** (cascades across the build rows, the Apple tie, the manual sign-in tie, Tavern, the tile dozer post, the lives line, the scope count, and sides of event icons): these rows share a likely root cause, not an embedded acceptance condition (Eval 3 §3.3: "Rows that merely share a likely model root cause are not a group"). They are the same fact in separate required deliverables.
- **R4-DR11** (R2 weight 1): the prefix overrides the notes' "title is the line … as it was written" through a later comment the notes point to. That is limited reconciliation, so w3.
- **R1-DR1** ("stays open" wording): the title is a plain-language check that accepts "not complete / not in 0.3.310". A build-only note on a held child is rightly rejected, because the notes say held children stay where they are.
- **R2-DR1** (R84 justification): the record says "shop prefabs", so the reading is not contradicted.
- **R2-DR2:** PLATFORM:FD-2880 (fbe7bdea is only in commit_map). Not scored.

## Deep Recheck

Passes: R1, R2, R3, R4, R5, R6, R7, Opus 5.5 (claude-opus-5-5), each blind to the main review, run on the 76 target rows (R4 against all 138).

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| R1 | 76 | 1 | 0 |
| R2 | 76 | 2 | 0 |
| R3 | 138 | 2 | 0 |
| R4 | 76 | 11 | 0 |
| R5 | 76 | 5 | 0 |
| R6 | 76 | 1 | 0 |
| R7 | 76 | 1 | 1 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | R7 | R3 "after the prefix" | ENG-2401 comment_49b5ac4788465f72ddf245e34f2b7034 'put [2231] at the front'; notes 'the first line of the post, as it was written' | Atomic | non_atomic | CONFIRMED | Two claims from two sources; a prefix-less exact title fails R3 |
| DR1 | R6 | R79 "moves exactly 14 of the 28 UI children" | rubric_sampling.md volume row | Self-contained | not_self_contained | REJECTED | Volume row by design |
| DR1 | R3 | R95–R117 build-only lines | DM 'saying where it landed' | Missing outcome | missing_coverage | REJECTED | Pre-existing reading; Notes for QM (DELTA rule) |
| DR2 | R3 | R79 | rubric_sampling.md | Missing outcome | missing_coverage | REJECTED | Contingent on R79 removal |
| DR1 | R5 | R79 | UI pass tracker f_a9ba8abc7d5189babcb378 | Overly broad | overly_broad | REJECTED | Volume row; samples carry the traps |
| DR2 | R5 | R79 | notes 'the masters stay as they are' | Overly broad | overly_broad | REJECTED | Decoy with no required report (count-bundle-v1) |
| DR3 | R5 | R1 | ENG-2406 comment; Vincent's mail | Overly broad | overly_broad | REJECTED | Volume row |
| DR4 | R5 | R85–R89 "stays open" | ENG-2428 comment | Overly broad | overly_broad | REJECTED | Very unlikely path (QC B11) |
| DR5 | R5 | R135 | D05S1S2AB5M thread | Destination | overly_broad | REJECTED | R134 grades the thread; avoids a cascade |
| DR1–DR10 | R4 | R1, R79, R90–R117, R122–R128, R120 | various | Duplicates | duplicate | REJECTED | Volume vs samples, or a shared root cause only (Eval 3 §3.3) |
| DR11 | R4 | R2 w3 | notes title rule vs ENG-2401 comment | Weights | weight | REJECTED | Limited reconciliation |
| DR1 | R1 | R85–R89 | DM; Trello 690b29bc3c7d2e51b0f86a47 | Overly specific | harmless_specificity | REJECTED | Semantic title accepts any "not done" wording |
| DR1 | R2 | R84 justification | C09Q4S613CN/1764606918.318209 'shop prefabs' | Incorrect | incorrect | REJECTED | The record supports the reading |
| DR2 | R2 | R28 evidence fbe7bdea | commit_map/13584 | Incorrect | platform | REJECTED | PLATFORM:FD-2880 |

Fix check: R3 went through rounds 1–3 and a restructure round (R1–R7 on R3 and its siblings, plus lint and fixcheck each round). Round 1: R1, R2 and R5 found "includes … word for word" accepted added words. Round 2: R1 found the two-string Accept list rejected "[2231]Any idea…". Round 3: R6 found the any-separator evidence wider than the title. Restructure: R4, R6 and R7 found "besides the [2231] prefix" reads as requiring the prefix. Each was CONFIRMED. Result: revised, needs your own rewrite.

Effect on verdict: Overall Rubric Quality FAIL on R3 (non_atomic, Major). The other dimensions are unchanged at 5.

Platform defects: PLATFORM:FD-2880 (commit fbe7bdea is only in commit_map; the Slack #engineering-bots line and git history show it on develop).

### FINAL VERDICT: FAIL
Score: 1
Execution status: COMPLETE
Review policy: rubric-revision-v10
Review mode: AUDIT
Reviewed JSON SHA-256: 9f8ebad8c3e38ffaa983cfe8bf4a5960755b4cfa5aace5fb337b947d3b8f85fc
Review context SHA-256: 3bd303b4554a4d0e6ed731abf3d639f4bbb31e9a3ce71b3a6024e8eecc850a6b
Scoring record SHA-256: a87252e04cbb8a1fd453ed277fe146203407b8bfab674ae6780297cfb985cd7a
Eval version: task-quality-v1
Eval release SHA-256: 56292d5d69c9e3fcb2ecc44ea7b0fb5a8fdf3e7aa1026fa9da6fb9472960e631
Gate tier: localized
Coverage ratio: 139/139
Repairs: See findings
Evaluator model: Opus 5.5 (claude-opus-5-5)
Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
Next action: Rewrite R3 as the Fix List describes (one row grading the title words, with the [2231] prefix optional in the title itself), then send /rubric again.
Evidence limits: None
