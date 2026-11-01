## RUBRIC EVALUATION REPORT

### Task: Server-side beta sign-off for Zombie Match 3D: build the 17-ticket register in Arthur's sign-off folder, move the 15 not-on-prod tickets back to Todo with comments, reply to Arthur in the DM, and share the register with Leonard
### Persona: Douglas - Software Engineer
### Total Rubrics: 52 (Outcome: 52, Process: 0)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Run mode: FULL (first run; no saved row ledger). Reviewers: F1 (main session), F2 and F3 (independent full reviewers), deep-recheck passes R1–R7.

## Fix List

Copy these into the rubric. New rows go at the end, after R52, so existing row numbers stay the same. Every fix went through fix-check round(s) as marked.

- **R1**: the file-type lock rejects a valid Doc-table register. New title: "The Agent saves the server sign-off register inside Arthur's Drive folder 'ZM Beta sign-off' (d_69fcebc484d472907b0b5c), as a file of any type". In the justification, replace "The sheet title is left to the Agent." with: "Neither the prompt nor the card fixes a file type, so a Google Sheet, a Google Doc with a table or another file all pass; the title is left to the Agent." (checked, 2 rounds)
- **R3, R24, R34, R44** (justification), **R12** (justification): "the contractor" has no record behind it. Write "PERSON_2967_GITHUB_USERNAME's inline review comment" and "its only Approve is PERSON_2967_GITHUB_USERNAME's, not Arthur's". Wording only, not scored. (checked, 2 rounds for R12/R34; 1 round for R3/R24/R44)
- **R10, R11**: weight 3 → **5** (multi-source: R10 needs rollback, redeploy, Approve timing and freeze; R11 needs Linear, the Trello card comment and the deploy log). (checked, R10 2 rounds, R11 1 round)
- **R15**: weight 3 → **1** (#52 is stated word for word in ZOM-503's comment). Append to the justification: "Weight 1: the PR is stated word for word in ZOM-503's own comment." (checked, 1 round)
- **R23** (justification only): replace "Tickets may be named by key or title." with "Tickets are counted by their ZOM keys, the way Arthur names them in his reply-all." This keeps it consistent with the per-ticket DM rows. (checked, 2 rounds)
- **R34–R40, R42**: weight 3 → **5**, matching R3–R9 and R14 for the same tickets. (checked, 2 rounds; R42 1 round)
- **R43**: bundles 15 comment writes and their content. New title: "The Agent adds a new comment to exactly 15 ZOM tickets". New justification: "Card rule 5: 'goes back to Todo with a comment saying which change still has to go out'. 15 register tickets are not on prod. This is the wrong-target guard for comments: ZOM-499 and ZOM-510 are Done but on prod, and ZOM-547/ZOM-553 were taken off by Arthur. What each comment says is graded in the per-ticket comment rows." Weight 5. (checked, 2 rounds)
- **R44–R51**: weight 3 → **5**, matching R3–R9 and R12. **R51**: also append to the justification "; a comment saying #52 needs Arthur's Approve and a redeploy also passes." (checked, R51 2 rounds; R44–R50 1 round)
- **R52** (justification only): its justification is wider than the title. Replace it with: "Card rule 5; #41's 2025-09-03 prod deploy does not count because its Approve came afterwards, and the doc says to redeploy. Wording is left to the Agent; a comment saying #41 needs a redeploy to prod also passes." (checked, 2 rounds)
- **New R53–R57** (register on-prod column, which makes it exhaustive, so the over-five spot-check group goes away): "The Agent marks ZOM-336 as N (not on prod) in the on-prod column of the server sign-off register" (weight 3). The same title for ZOM-518 (3), ZOM-435 (3), ZOM-557 (3) and ZOM-256 (5). (checked, 1–2 rounds)
- **New R58–R63** (missing DM facts): "The Agent names ZOM-336 to Arthur in the DM reply as a ticket not on prod" (weight 3). The same title for ZOM-392 (3), ZOM-518 (3), ZOM-550 (5), ZOM-435 (3) and ZOM-256 (5). (checked, 1–2 rounds)
- **New R64–R69** (missing Todo moves): "The Agent moves ZOM-336 from Done to Todo" (weight 3). The same title for ZOM-503 (5), ZOM-518 (3), ZOM-435 (3), ZOM-557 (3) and ZOM-256 (5). (checked, 2 rounds)
- **New R70–R75** (missing comments):
  - "The Agent comments on ZOM-336 that match3d-backend#40 still has to go out to prod" (3)
  - "The Agent comments on ZOM-518 that match3d-backend#43 still has to go out to prod" (3)
  - "The Agent comments on ZOM-550 that match3d-backend#50 still has to go out to prod" (5)
  - "The Agent comments on ZOM-435 that match3d-backend#51 still has to go out to prod" (3)
  - "The Agent comments on ZOM-557 that match3d-backend#54 still has to go out to prod" (3)
  - "The Agent comments on ZOM-256 that the algo levels 2.0 level pack import still has to go out to prod" (5)
  (checked, 2 rounds)
- **New R76** (Process, weight 1; the one missing ordering check): "The Agent shares the server sign-off register with Leonard only after the register is already in the Drive folder where it ends up". It grades only the order: saving into the folder and then sharing passes, while creating the file elsewhere, sharing it and then moving it fails. R1 grades the folder and R20 grades the share. (checked, 3 rounds)

The justification and evidence text for every new row is in the downloadable candidate. Each one cites the ticket comment, the PR comments or reviews, the deploy-log row and card rule 5 it relies on.


---

### Phase 1: Structural Validation
- Five-field completeness: 52 of 52 (title, category, weight, justification, evidence all present; weights 1/3/5; category Outcome).
- Category distribution: Outcome 52, Process 0.
- Requirement coverage: 53 of 71 required outcomes covered. The 18 not covered are per-ticket writes and DM facts listed under Phase 3.
- Code checks (`hg_rubric_lint.py`): 0 hits.

### Phase 2: Per-Rubric Quality
| Row | Issue | Type | Severity |
|---|---|---|---|
| R1 | "as a Google Sheet" rejects a valid register saved as a Google Doc table (or another file) in the right folder | overly_specific | Major |
| R43 | One row grades 15 separate comment writes plus each comment's content ("each saying …"), and ties the count to the Todo move | non_atomic | Major |
| R43 | "which change still has to go out" is not defined by any title for ZOM-336, 518, 550, 435, 557 or 256 | not_self_contained | Major (same row, counted once) |
| R52 | Justification "the row grades only that #41 is named" is wider than the title | not_self_contained | Major |
| R8–R14 | Register on-prod column has 12 spot checks (R3–R14); the cap is five per group | duplicate (OVERLAP_GROUP) | Moderate (one group) |
| R33, R43 | R43 only counts tickets "moved back to Todo", so one missed move fails R33 and R43 together | duplicate (OVERLAP_GROUP) | Moderate (one group) |

Atomicity decomposition: every row is one result except R43 (15 comment writes + content + the Todo-move condition). R1's "as a Google Sheet" is a lock on the one save result, recorded as overly specific rather than a second result.
Over-specificity triage: R1 overly_specific; all other rows valid.

### Phase 3: Set-Level Quality
- Coverage gaps (18, each Major `missing_coverage`):
  - DM reply naming the ticket as not on prod: ZOM-336, ZOM-392, ZOM-518, ZOM-550, ZOM-435, ZOM-256 (R23 is only a count; R24–R32 name 9 of the 15).
  - Comment saying which change still has to go out: ZOM-336 (#40), ZOM-518 (#43), ZOM-550 (#50), ZOM-435 (#51), ZOM-557 (#54), ZOM-256 (algo levels 2.0 level pack import). These comments carry different facts, so they cannot be sampled.
  - Move from Done to Todo: ZOM-336, ZOM-503, ZOM-518, ZOM-435, ZOM-557, ZOM-256. The scope checklist says "State changes and other writes get one row per target the same way".
- Process audit: no Process rows. One ordering dependency the prompt states has no Process row: "handle what he asked for once the register is in the folder" (share after the register is in the folder). Process Rubrics is NON-FAIL 3 (`missing_process_checks: 1`).
- Duplicates / overlap / cascade groups: G_ONPROD_CAP (R8–R14, the samples beyond five), G_TODO_CASCADE (R33, R43).
- Spot-check groups: register on-prod column, 12 samples (over the cap of five; volume row R2 present); register server-change column, 5 samples (R15–R19; volume row R2 present).
- Wrong-target guards: R33 (moves) and R43 after the fix (comments) are valid bare count guards, because real decoys exist (ZOM-499 and ZOM-510 are Done but on prod; ZOM-547 and ZOM-553 were taken off by Arthur).
- Weights: 19 rows are one level off. R10 (ZOM-499 Y: rollback, redeploy, approval and freeze check) and R11 (ZOM-510 Y: Linear, Trello and deploy log) should be 5. R15 (#52 is stated word for word in ZOM-503's comment) should be 1. The move rows R34–R40 and R42, and the comment rows R44–R51, should be 5 to match the register and DM rows for the same tickets (R3–R9, R12, R14, R24–R31 are 5).
- OE cross-check: every row maps to OE steps; no OE conflicts. OE 33 creates a Google Sheet, which is one valid path; the rubric must also accept other file types.
- Contradictions: none. R22's 2 plus R23's 15 equals R2's 17.

### Phase 4: Issue Tally
| Severity | Count | % | Fails when | Status |
|---|---|---|---|---|
| Major | 21 (3 rows + 18 missing outcomes) | 40.4% | any | FAIL |
| Moderate | 2 (overlap groups) | 3.8% | any | FAIL |
| Minor | 0 | 0% | ≥ 5% | PASS |

### Phase 5: Scoring
| Sub-Dimension | Score | Justification |
|---|---|---|
| Overall Rubric Quality | 1 | Major issues on R1, R43, R52 and 18 missing outcomes; two Moderate overlap groups |
| Criteria Weights | 2 | 19 of 52 rows (37%) one level off |
| Rubric Category Balance | 5 | 52 Outcome rows |
| Process Rubrics | 3 | One missing ordering check the prompt states (share once the register is in the folder) |
| Agent-Centric Phrasing | 5 | Every title starts "The Agent" with an action; no tool names |
| Negative Criteria | 5 | No prohibition titles; every row fails an Agent that does nothing |
| Predicted All-Fail gate | PASS | No row is predicted to fail every run |

**Lowest Sub-Dimension:** Overall Rubric Quality - 1 - missing per-ticket coverage for six of the 15 not-on-prod tickets, plus R1, R43 and R52.
**Summary:** Every value the rubric states is correct against the records: the 17-ticket scope, 2 on prod and 15 not, each import link, and the freeze and rollback outcomes. The rubric fails on coverage. Four not-on-prod tickets (ZOM-336, ZOM-518, ZOM-435, ZOM-256) have no row in any output, and six comments, six moves and six DM facts have no row of their own. It also fails on R1's file-type lock, R43's bundled comment row, R52's widening justification and weight consistency.

### Issues Found
| # | Row | Issue | Severity | Type |
|---|---|---|---|---|
| 1 | R1 | Google Sheet lock rejects a valid register | Major | overly_specific |
| 2 | R43 | 15 comment writes and their content in one row, tied to the Todo move | Major | non_atomic |
| 3 | R43 | Content per ticket not defined by any title for six tickets | Major | not_self_contained |
| 4 | R52 | Justification wider than the title | Major | not_self_contained |
| 5–10 | — | DM facts for ZOM-336, 392, 518, 550, 435, 256 | Major | missing_coverage |
| 11–16 | — | Comments for ZOM-336, 518, 550, 435, 557, 256 | Major | missing_coverage |
| 17–22 | — | Todo moves for ZOM-336, 503, 518, 435, 557, 256 | Major | missing_coverage |
| 23 | R8–R14 | Register on-prod spot checks over the cap of five | Moderate | duplicate |
| 24 | R33, R43 | Shared Todo-move condition | Moderate | duplicate |
| — | R10, R11, R15, R34–R40, R42, R44–R51 | Weights one level off | Criteria Weights | weight |
| — | set | One missing Process ordering check | Process NON-FAIL | missing process |

### Recommended Fixes
Every fix below is in the candidate rubric (76 rows). Each was checked by `hg_rubric_ledger.py fixcheck` (title cap of 120 words; no bundled_writes or scope_tail), by `hg_rubric_lint.py` (0 hits), by a self-check including the opposite-pair test, and by deep-recheck passes R1–R7 on the changed and new rows and their siblings.
1. R1: remove the Google Sheet lock (checked, 2 rounds: fixcheck, lint, R1–R7).
2. R43: reduce it to the bare comment guard "exactly 15 ZOM tickets" (checked, 2 rounds).
3. R52: drop "the row grades only that #41 is named" (checked, 2 rounds).
4. Add R58–R63 (DM), R64–R69 (moves) and R70–R75 (comments) for the 18 missing outcomes (checked, 1–2 rounds).
5. Add R53–R57 so all 17 register on-prod cells are graded, which clears the over-five spot-check group (checked, 1–2 rounds).
6. Weights: R10, R11, R34–R40, R42, R44–R51 → 5; R15 → 1 (checked, 1–2 rounds).
7. Add Process row R76 for the "once the register is in the folder" order (checked, 3 rounds; rounds 1 and 2 reworded it to avoid both an overlap with R1 and a version that was too easy to pass).
8. Wording only: R3, R12, R24, R34, R44 "contractor" → the login; R23 and R51 justifications aligned with their siblings (checked).

## All Findings

### R1
- **overly_specific (Major)**. Raised by F1, F2, F3, R1, R3 and R7 (R7 called it non-atomic; merged, because the file type is a lock on the one save result, and one fix cures both). Evidence: the prompt says "Put the register in the beta sign-off folder". Card 68dabfe9bc2e8b969782e22d rule 2 says "One row per ticket: ticket, server change(s), on prod (Y/N)" and rule 6 says "The register goes in the sign-off folder named on the ZM Beta page in Confluence". No record fixes a file type ("The sheet goes in the client QA folder" is on Oliver's client card only), and prompt-report fork F21 says the rubric must accept a Sheet or a Doc table. Witness: a Google Doc with a 17-row table saved in d_69fcebc484d472907b0b5c fails R1. Fix: Fix List R1.

### R3, R12, R24, R34, R44 (wording, not scored)
- These justifications call PERSON_2967_GITHUB_USERNAME "the contractor". The GitHub user record (/users/27) shows only "PERSON_2967_NAME", and no record calls this user a contractor. Raised by F2, F3 (unsure) and R2. It changes no grading, so it is a wording fix only. Fix: name the login instead.

### R8–R14 (group G_ONPROD_CAP)
- **duplicate, OVERLAP_GROUP (Moderate)**. Raised by F1, F2, F3 and R4. R3–R14 are 12 spot checks of the register's on-prod column, and R2 is the volume row. Rubric Writing §8 and the local override allow "at most five samples per group", and rows beyond five form one overlap group. The five unsampled cells include the hardest edges: ZOM-518 (deployed with no Approve), ZOM-557 (rolled back) and ZOM-256 (import only). Fix: make the column exhaustive with the five new register rows (Fix List R53–R57). Exhaustive per-ticket coverage is not sampling, so the cap no longer applies. Cutting R3–R14 down to five would also cure the cap, but it would leave those edges ungraded.

### R10, R11, R15, R34–R40, R42, R44–R51 (Criteria Weights)
- R10: expected 5, authored 3. Needs #44's rollback and redeploy comments, the Approve timing and author, the freeze date, and the doc rule. That is the same source mix as R12 and R14 (both 5). Raised by F3 and R4.
- R11: expected 5, authored 3. A three-service join: the Linear comment, the Trello card comment that counts imports, and the deploy log's prod target. Raised by F3.
- R15: expected 1, authored 3. "match3d-backend#52" is stated word for word in ZOM-503's comment. Raised by F1, F2, F3 and R4.
- R34–R40, R42: expected 5, authored 3. Each move needs the same multi-source not-on-prod reasoning that R3–R9 and R14 weight 5. Raised by F2, F3 and R4.
- R44–R51: expected 5, authored 3. Naming the change still to go out means separating the on-prod PR from the dev-only import or freeze deploy, the same reasoning R3–R9 and R12 weight 5. Raised by F2 and R4. R41 and R52 (ZOM-392, 3) stay consistent with R13.

### R33, R43 (group G_TODO_CASCADE)
- **duplicate, OVERLAP_GROUP (Moderate)**. Raised by F2. R43 counts only tickets "moved back to Todo", so one missed move fails both R33 and R43. Fix: the R43 rewrite drops the Todo condition.

### R43
- **non_atomic (Major)**. Raised by F1, F2, F3, R3, R4, R5 and R7. "adds a new comment to exactly 15 ZOM tickets moved back to Todo, each saying which change still has to go out" bundles 15 separate comment writes and their content, and joins them to the Todo move. Scope checklist: never "comments on each of …" or "every / all" over separate writes. Fix: Fix List R43, which keeps it as the bare wrong-target guard. Real decoys exist: ZOM-499 and ZOM-510 are Done but on prod, and ZOM-547 and ZOM-553 were taken off. The per-ticket content moves to R44–R52 and R64–R69.
- **not_self_contained (Major, same row)**. Raised by F2, F3 and R6. No title says what the comment must name for ZOM-336, 518, 550, 435, 557 or 256. The same fix cures it.

### R52
- **not_self_contained (Major)**. Raised by F3 and R6. The justification says "the row grades only that #41 is named", which would pass a comment saying "#41 is on prod" that the title rejects. Fix: Fix List R52 (justification only).

### Missing outcomes (rows: none)
- **DM reply facts (6 × Major missing_coverage)**: ZOM-336, ZOM-392, ZOM-518, ZOM-550, ZOM-435, ZOM-256. Raised by F1, F2, F3, R3 and R6 (R4 offered a sampling-cap reading). Arthur asked "how many tickets are on prod and which ones aren't" (D05QQF7V404/1759266764.508127). Which tickets are not on prod is the core answer, and the scope checklist requires "one row per independent fact" of a message. R23 is a count only, so a reply that swaps ZOM-336 for ZOM-499 passes every row. Fix: Fix List R58–R63.
- **Ticket comments (6 × Major)**: ZOM-336 (#40, dev only), ZOM-518 (#43, no Approve), ZOM-550 (#50, freeze without Arthur's Approve), ZOM-435 (#51, dev only), ZOM-557 (#54, rolled back), ZOM-256 (level pack import, dev only). Raised by F1, F2, F3, R3 and R4. Card rule 5: "with a comment saying which change still has to go out". Each comment carries different facts, so it needs its own row with no cap. Fix: Fix List R70–R75.
- **Todo moves (6 × Major)**: ZOM-336, ZOM-503, ZOM-518, ZOM-435, ZOM-557, ZOM-256. Raised by F2, F3 and R3. F1 and R4 first read R34–R42 as a sampled template group over the cap of five. That reading was not taken: the scope checklist's sentence for state changes, "State changes and other writes get one row per target the same way", requires a row per target, and its template-sampling exception names comments only. Fix: Fix List R64–R69.

### Process (non-failing)
- One missing ordering check the prompt states: "please handle what he asked for once the register is in the folder". Raised by F3. Process Rubrics is NON-FAIL 3. Fix: Fix List R76 (a new Process row, final wording after 3 check rounds).

### Worth a look (not scored)
- The evidence fields cite SQL line numbers that look wrong if you count lines with `wc -l`. They match when you count stray carriage returns inside the file's Gmail bodies as line breaks: each cited number is the INSERT line just above the record. Only R1's "SQL L6", R1/R33–R43's "SQL L57" and the doc's "SQL L15" point at the section-header comment one line above the INSERT (raised by F2 and R2). Optional tidy-up.
- R1's weight could be argued as 5 (card rule 6 → Confluence page → Drive, past the decoy client-QA folder). F2 and F3 were unsure; it stays 3 (limited reconciliation).
- R16–R19 could be argued as 1, because each import is stated in one record. That claim was rejected for R17 and R18 because the import link is not in the ticket itself: the Agent has to trace from the ticket to the PR review or the Confluence reply.
- Card rule 5 says "Same ticket, no new ones". No row can guard against new tickets without passing an idle Agent (the Negative Criteria override), and no record holds a decoy, so it stays uncovered by design.
- Oliver asked in #zombie-match3d for the server list. The prompt report (fork F22) says the prompt doesn't incorporate that request, so it is neither required nor a decoy.

- Unchanged rows R13, R14, R22 and R33 cite "SQL L15" and "SQL L57", which are section banners one line above the INSERT (fix-check round 2). Optional tidy-up; the record IDs are correct. In the changed rows the candidate already uses L16 and L58.

### Rejected findings
- R5 DR1–DR4 and F3-15 (R2, R22, R23, R33 overly broad as counts): count rows are allowed volume controls and wrong-target guards (rubric_sampling: "one criterion checking the volume of the output (its exact count or total)"; scope checklist: "one bare count row on that write kind with no id list"). For R22, Arthur asked for "how many", and a right count over a wrong pair needs two cancelling errors, which is very unlikely under QC B11.
- R6 DR1 and F3-13 (R23 not self-contained): R23 is a count predicate by design. The real gap, six unnamed tickets, is scored as the six DM missing outcomes.
- F3-16 (register cell pairs as cascades): Eval 3 §3.3 says "A row that fails only because its own artifact was never created … does not embed a shared condition".
- R4 DR5 (one cascade group over every row that shares the derivation): Eval 3 §3.3 says "Rows that merely share a likely model root cause are not a group".
- R4 DR6 (R21 duplicates the content rows): Eval 3 §3.3 lists "a write row plus its content row" as not duplicates. R21 also grades the channel ID and thread choice.
- R4 DR11 (R17, R18 weight 1): the import link is not in the ticket, so this is tracing, not a single-source lookup.
- F2-26 and fix-check round 2 DR4 (R44–R49, R51 accept a comment that also calls the on-prod PR outstanding): QC B11 says don't flag "when the accepted invalid paths are very unlikely". #38, #39, #42 and #46 have clean prod comments with prior Approves.
- F2-28 (Process row for the DM after the work): Eval 3 says to raise missing Process "only when the prompt contains that dependency". The prompt asks for the DM's content ("what he asked for"), not its timing.
- F2-27 and R2 DR4–DR7 (line numbers): see Worth a look. The record IDs are right and the lines match the file's own line breaks.
- R2 DR1–DR3 (contractor label): kept as a non-scored wording fix, because it is not acceptance-bearing.


## Deep Recheck

Passes: R1–R7, Opus 5.5 (claude-opus-5-5), each blind to the main review. They ran alongside independent full reviewers F2 and F3. Fix-check rounds: round 1 (R1–R7 each separately on 50 changed and new rows), round 2 (R1–R7 on the rows revised in round 1), round 3 (R1–R7 on R76 and its siblings).

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| R1 | 52 rows | 1 | 1 |
| R2 | 52 rows | 7 | 0 (3 kept as a non-scored wording fix) |
| R3 | 52 rows | 15 | 15 |
| R4 | 52 rows | 12 | 7 |
| R5 | 52 rows | 5 | 1 (merged into R43) |
| R6 | 52 rows | 3 | 2 |
| R7 | 52 rows | 2 | 2 (R1 merged) |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| R1-DR1 | R1 | R1 "as a Google Sheet" | Card 68dabfe9bc2e8b969782e22d rules 2 and 6; prompt "Put the register in the beta sign-off folder" | Overly specific | overly_specific | CONFIRMED | No record fixes a file type |
| R2-DR1–3 | R2 | R3/R12/R24 "the contractor's" | github /users/27 "PERSON_2967_NAME" | Incorrect | wording | REJECTED | Not acceptance-bearing; kept as a non-scored wording fix |
| R2-DR4–7 | R2 | Evidence "SQL L96", "L156", "L854" | 01_Universe_Inject.sql with splitlines numbering | Incorrect | evidence pointer | REJECTED | The lines match the file's own line breaks (carriage returns inside Gmail bodies); record IDs are correct |
| R3-DR1–6 | R3 | Missing moves ZOM-336/503/518/435/557/256 | Card rule 5 | Missing coverage | missing_coverage | CONFIRMED | "State changes and other writes get one row per target the same way" |
| R3-DR7–12 | R3 | Missing comments ZOM-336/518/550/435/557/256 | Card rule 5; #40/#43/#50/#51/#54 PR comments; deploy log | Missing coverage | missing_coverage | CONFIRMED | Distinct content per comment; never sampled |
| R3-DR13 | R3 | R23 count only; R24–R32 cover 9 of 15 | D05QQF7V404/1759266764.508127 | Missing coverage | missing_coverage | CONFIRMED | Six DM facts, one per ticket |
| R3-DR14 | R3 | R43 "each saying …" | Card rule 5 | Atomic | non_atomic | CONFIRMED | Bundled writes |
| R3-DR15 | R3 | R1 "as a Google Sheet" | Prompt, card | Beyond prompt | overly_specific | CONFIRMED | Duplicate of R1-DR1 |
| R4-DR1 | R4 | R3–R14 12 samples | Card rule 2 | Sampling cap | duplicate | CONFIRMED | Group G_ONPROD_CAP |
| R4-DR2–4 | R4 | DM, move and comment samples | Card rule 5; DM ask | Sampling cap | duplicate | REJECTED | Scored as missing coverage instead (one row per write and per message fact) |
| R4-DR5 | R4 | Cross-row cascade over the shared derivation | Reply-all L97 | Cascade | duplicate | REJECTED | §3.3: rows that merely share a root cause are not a group |
| R4-DR6 | R4 | R21 delivery row | DM | Duplicate | duplicate | REJECTED | §3.3: a write row plus its content row is not a duplicate |
| R4-DR7 | R4 | R10 weight 3 | #44 c_3/c_4/rev_3; freeze evt | Weights | weight | CONFIRMED | Expected 5 |
| R4-DR8–9 | R4 | R34–R40, R42; R44–R51 weight 3 | #38/#39/#46 review comments; deploy log | Weights | weight | CONFIRMED | Expected 5, matching R3–R9, R12, R14 |
| R4-DR10 | R4 | R15 weight 3 | cmt_c95585f37ce6708a9ec4 | Weights | weight | CONFIRMED | Expected 1 |
| R4-DR11 | R4 | R17, R18 weight 3 | #46#rc_1; comment_zm_beta_oct10_c2 | Weights | weight | REJECTED | The link is not in the ticket; this is tracing, not a single-source lookup |
| R4-DR12 | R4 | All rows Outcome | 09_Rubrics.json | Process | none | REJECTED | Informational |
| R5-DR1–4 | R5 | R2, R22, R23, R33 counts | Card, DM | Overly broad | overly_broad | REJECTED | Allowed volume rows and wrong-target guards |
| R5-DR5 | R5 | R43 | Card rule 5 | Overly broad | non_atomic | CONFIRMED | Merged into R43's non_atomic finding |
| R6-DR1 | R6 | R23 "exactly 15 tickets" | R23 justification list | Self-contained | not_self_contained | REJECTED | A count predicate by design; the gap is scored as six DM missing outcomes |
| R6-DR2 | R6 | R43 "which change still has to go out" | Card rule 5 | Self-contained | not_self_contained | CONFIRMED | Same row as non_atomic |
| R6-DR3 | R6 | R52 "the row grades only that #41 is named" | R52 justification | Self-contained | not_self_contained | CONFIRMED | Justification wider than the title |
| R7-DR1 | R7 | R43 | Card rule 5 | Atomic | non_atomic | CONFIRMED | Bundled writes |
| R7-DR2 | R7 | R1 format plus location | Card rule 6 | Atomic | overly_specific | CONFIRMED | Merged into R1-DR1 |

Effect on verdict: unchanged. The confirmed findings were merged into the scoring record before it was saved. Overall Rubric Quality 1, Criteria Weights 2, Process 3. Verdict FAIL, score 1.

Platform defects: none.

### FINAL VERDICT: FAIL
Score: 1
Execution status: COMPLETE
Review policy: rubric-revision-v10
Review mode: AUDIT
Reviewed JSON SHA-256: 1244870fbf2ce40fa9482abaef1f9c8db43458b115fb5d2e78edc0885a290d93
Review context SHA-256: 2fe807852684d415a6518c97b0339117cda4767cf84cf5e7c253b182be6caac4
Scoring record SHA-256: a506ccb8cd20fbc303b3a662c194b8d314712d0235be6b2705dc7a9681a09ccc
Eval version: task-quality-v1
Eval release SHA-256: 633dfebccbcb03e248f19b8115a04a1c41d0059abccdb332a1cb20957b2b3ddc
Gate tier: localized
Coverage ratio: 53/71
Repairs: See findings
Evaluator model: Opus 5.5 (claude-opus-5-5)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Next action: Apply the Fix List (the checked candidate rubric has 76 rows), then send /rubric again.
Evidence limits: None
