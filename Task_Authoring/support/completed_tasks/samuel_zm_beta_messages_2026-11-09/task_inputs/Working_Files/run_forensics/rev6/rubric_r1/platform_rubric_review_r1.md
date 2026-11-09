## RUBRIC EVALUATION REPORT

### Task: Beta phone-message calls for Zombie Match (calls sheet, one-page note, ticket comments and moves, new tickets, checklist, asker emails, counts DM)
### Persona: Samuel Turner - Game Designer
### Total Rubrics: 143 (Outcome: 142, Process: 1)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

## Fix List

Copy each fix as written. Row numbers are your current rubric's; "cand." numbers are positions in the corrected rubric after the inserts and deletes. Every fix below passed lint, fixcheck and all seven check passes (R1–R7) on the changed rows and their siblings.

- **R3 (add a row after it)** — no row grades the Message column; a sheet with blank Message cells passes everything.
  Fix: add "The Agent enters Lapsed 1 day (or the PN sheet's "Has not played in 24 hours", any wording naming that message) in the Message column of the DES-316 row of its calls sheet" (Outcome, weight 1). (cand. R4: checked, 1 round)
- **R12 (add a row after it)** — once the sheet Hold/Drop counts go (see R41/R42), no Call cell covers DES-344, the one Drop that is "covered by another message".
  Fix: add "The Agent enters Drop in the Call column of the DES-344 (Lapsed 14 days) row of its calls sheet" (Outcome, weight 5). (cand. R14: checked, 2 rounds)
- **R15, R16** — wording: "fails test 6, seen on both iOS and Android" reads as if it was seen on both (not scored).
  Fix: replace "that it fails test 6, seen on both iOS and Android" with "that it fails test 6, as Vincent has yet to see it arrive on both iOS and Android". (cand. R17: checked, 1 round; cand. R18: checked, 1 round)
- **R19** — closed list rejects naming the covering message by its sheet name or headline.
  Fix: "The Agent records in the What's missing column of the DES-344 (Lapsed 14 days) row of its calls sheet that another message already covers it (naming Lapsed 7 days, DES-317, the weekly batch, the PN sheet's "Has not played in seven days.", or its line "They’ve Taken Over… Can You Stop Them?" or "Your Squad Is Waiting")". (cand. R21: checked, 2 rounds)
- **R25** — What's missing has six ordinary spot checks (R20–R25); the cap is five.
  Fix: delete R25. (checked, 1 round)
- **R33** — weight 3 for copying the key of the Agent's own new ticket (mechanical, like R32).
  Fix: weight 1; justification "Lookup: the key of the Agent's own new ticket for this ask (not ZOM-563)." (cand. R34: checked, 2 rounds)
- **R38** — a sheet with N/A or a dash in the 34 non-Go rows follows the rule but fails "exactly two rows"; also cascades with R40.
  Fix: "The Agent keeps its Final headline entries to the rows it calls Go in its calls sheet (a blank cell, a dash or N/A on the other rows counts as no entry)" (weight 1). (cand. R39: checked, 2 rounds)
- **R39** — same as R38 for String change.
  Fix: "The Agent keeps its String change entries to the rows it calls Go in its calls sheet (a blank cell, a dash or N/A on the other rows counts as no entry)" (weight 1). (cand. R40: checked, 2 rounds)
- **R41, R42** — sheet Hold/Drop counts cascade with R40 (one wrong call fails two counts); the sheet is not asked for counts.
  Fix: delete both (R40 stays as the Go guard; the calls are graded on every ticket comment; the new DES-344 Call row above replaces the Drop coverage). (checked, 2 rounds)
- **R51** — grades both that the note lists the message as a client-scheduled Hold and the reason (a verdict and its reason are separate rows).
  Fix: replace with two rows: "The Agent names Lives recharged (or DES-315, When lives are recharged, or Full Ammo Reloaded!) in its one-page note as a message the client already schedules that is still a Hold" and "The Agent gives test 6 as the reason Lives recharged (or DES-315, When lives are recharged, or Full Ammo Reloaded!) is held in its one-page note (naming test 6, or saying Vincent has yet to see it arrive on both iOS and Android, that Vincent Parker's tick is off, or that it failed to arrive on iOS 0.3.49)" (both weight 5). (cand. R50: checked, 3 rounds; cand. R51: checked, 3 rounds)
- **R52** — grades both that the note lists the message as a client-scheduled Hold and the reason (a verdict and its reason are separate rows).
  Fix: replace with two rows: "The Agent names Plague Race (or DES-319, or Plague Race Is On!) in its one-page note as a message the client already schedules that is still a Hold" and "The Agent gives test 6 as the reason Plague Race (or DES-319, or Plague Race Is On!) is held in its one-page note (naming test 6, or saying Vincent has yet to see it arrive on both iOS and Android, that the iOS pass was on the 5-minute timers build, or that it never showed up on the real iOS build)" (both weight 5). (cand. R52: checked, 3 rounds; cand. R53: checked, 3 rounds)
- **R53** — grades both that the note lists the message as a client-scheduled Hold and the reason (a verdict and its reason are separate rows).
  Fix: replace with two rows: "The Agent names Weekly Leaderboard reset (or DES-320, or Weekly Rankings Reset!) in its one-page note as a message the client already schedules that is still a Hold" and "The Agent gives test 5 as the reason Weekly Leaderboard reset (or DES-320, or Weekly Rankings Reset!) is held in its one-page note (naming test 5, or saying it fires on the wrong day, or that it counts from the last session and misses the weekly reset)" (both weight 5). (cand. R54: checked, 3 rounds; cand. R55: checked, 3 rounds)
- **R54** — grades both that the note lists the message as a client-scheduled Hold and the reason (a verdict and its reason are separate rows).
  Fix: replace with two rows: "The Agent names Finish first mission (or DES-318, Finish first tutorial, or Finish Your First Mission!) in its one-page note as a message the client already schedules that is still a Hold" and "The Agent gives test 4 as the reason Finish first mission (or DES-318, Finish first tutorial, or Finish Your First Mission!) is held in its one-page note (naming test 4, or saying it can't reach its players, or that its players below level 20 haven't had our own ask, which runs after level 20)" (both weight 5). (cand. R56: checked, 3 rounds; cand. R57: checked, 3 rounds)
- **R92** — count guard carries an id range, which bundles 32 comment writes.
  Fix: "The Agent leaves call comments on exactly 32 existing Design tickets". (cand. R95: checked, 1 round)
- **R94, R99, R100** — eight per-ticket Backlog samples; the cap is five.
  Fix: delete R94, R99 and R100 (R93, R95, R96, R97, R101 stay unchanged). (checked, 1 round)
- **R104** — id range in the volume row.
  Fix: "The Agent moves exactly 24 existing tickets to Backlog". (cand. R104: checked, 2 rounds)
- **R105** — id range in the volume row.
  Fix: "The Agent moves exactly 6 existing tickets to Canceled". (cand. R105: checked, 1 round)
- **R106** — id range; keep it only as the bare guard for the Go tickets (they stay as they are).
  Fix: "The Agent changes the state of exactly 30 existing tickets". (cand. R106: checked, 2 rounds)
- **R107** — id range, never says which 24 tickets, and no single ticket's assignee is checked; weight should match R104.
  Fix: "The Agent clears the assignee on exactly 24 existing tickets" (weight 5), plus three new rows: "The Agent clears the assignee on DES-313 (Win & Collect start)" (weight 5), "The Agent clears the assignee on DES-315 (Lives recharged)" (weight 5), "The Agent clears the assignee on DES-329 (Endless weekly result)" (weight 3). (cand. R107: checked, 2 rounds; cand. R108: checked, 2 rounds; cand. R109: checked, 2 rounds; cand. R110: checked, 2 rounds)
- **R114** — one row bundles four ticket writes.
  Fix: replace with four rows (weight 3 each): "The Agent files its new ticket for the ask on ZOM-542 (Boss Arena attempts refilled) in Backlog with no assignee"; "The Agent files its new ticket for the ask on ZOM-556 (Daily gift about to reset) in Backlog with no assignee"; "The Agent files its new ticket for the ask on ZOM-563 (Teammate sent lives) in Backlog with no assignee"; "The Agent files its new ticket for the ask on ZOM-483 (Infinite lives ending) in Backlog with no assignee". (cand. R117: checked, 1 round; cand. R118: checked, 1 round; cand. R119: checked, 1 round; cand. R120: checked, 1 round)
- **R116** — closed name list misses the headline store builds show today.
  Fix: "The Agent adds Lapsed 7 days (named by DES-317, Lapsed 7 days, the PN sheet's "Has not played in seven days.", Your Squad Is Waiting or They’ve Taken Over… Can You Stop Them?) as an item on a checklist on the Push Notifications card on ZM ROADMAP (6851a769c65dc0017a227bb7)". (cand. R122: checked, 1 round)
- **R139** — guard row carries an identity/exclusion tail.
  Fix: "The Agent sends its emails about the asks to exactly eight people". (cand. R145: checked, 1 round)
- **R143** — its list of writes must include the new assignee clears (sibling of R107).
  Fix: "The Agent posts the counts in Leonard's DM after all of its other writes for the job (the calls sheet, the note, the ticket comments, the ticket moves, the assignee clears, the new tickets, the checklist and the emails), with none of them after the post". (cand. R149: checked, 3 rounds)

Not scored, worth doing: R98, R102, R103 evidence should cite the records that make each ticket a Drop (NotificationManager.cs plus the Gmail cancel note for DES-344, the Hourly Collection card for DES-324, Leonard's DES-345 comment); R6 and R7 justifications copy R4/R5's "Vincent's pass" wording although those Holds rest on PR #248/code (R6) and Robert's Slack post (R7).

---

### Phase 1: Structural Validation
- Five-field completeness: 143 of 143; categories Outcome 142, Process 1; weights all 1/3/5.
- Code checks (`hg_rubric_lint.py`): `bundled_writes` on R92 and R107 (both recorded); `format_lock` "one page" on R44 resolved (the prompt says "one-page note").
- Requirement coverage: 154 of 156 outcomes. Missing: the Message column, and any per-ticket check of the Hold tickets being unassigned.

### Phase 2: Per-Rubric Quality
| Row | Issue | Type | Severity |
|---|---|---|---|
| R92, R104, R105, R106, R107 | Count rows carry an id range ("DES-313 and DES-315 to DES-345"), bundling every write in it | non_atomic | Major |
| R107 | Never says which 24 tickets lose their assignee; any 24 pass | not_self_contained / overly_broad | Major |
| R114 | Four ticket writes and two fields each in one row | non_atomic | Major |
| R139 | Recipient count joined to an identity/exclusion tail | non_atomic | Major |
| R51–R54 | Listing the message as a client-scheduled Hold and its reason in one row | non_atomic | Major |
| R38, R39 | N/A placeholders on non-Go rows follow the rule but fail "exactly two rows" | overly_specific | Major |
| R19 | Closed list rejects naming the covering message by its headline | overly_specific | Major |
| R116 | Closed list omits the store-build headline "They’ve Taken Over… Can You Stop Them?" | overly_specific | Major |

All other rows: values verified against the records (R2 pass and F2/F3 found no incorrect value), Agent-centric, affirmative, one result each.

### Phase 3: Set-Level Quality
- Coverage gaps: Message column (no row grades any Message cell); unassignment has only the bundled count R107, no per-ticket sample.
- Process audit: R143 valid (prompt: "When it's all finished tell him the counts"); no other ordering check missing.
- Overlap / cascade groups: sheet counts R38–R42 (one wrong call fails several); state counts R104/R106/R107; new-ticket counts R113/R114; Backlog move samples R93–R97, R99–R101 (8, cap 5); What's missing samples R20–R25 (6, cap 5).
- Spot-check groups: Call column R10–R14 (R4–R9 are the six "Ready" rows, covered directly); Audience R26–R30; Ticket R32–R33 (R31 alias direct); Canceled R102–R103 (R98 direct). Volume control R3.

### Phase 4: Issue Tally
| Severity | Count | % | Fails when | Status |
|---|---|---|---|---|
| Major | 17 rows + 2 missing outcomes | 13.3% | any | FAIL |
| Moderate | 4 (overlap groups, counted once) | 2.8% | any | FAIL |
| Minor | 0 | 0% | ≥ 5% | — |

### Phase 5: Scoring
| Sub-Dimension | Score | Justification |
|---|---|---|
| Overall Rubric Quality | 1 | 17 Major rows, 2 missing outcomes, 4 Moderate overlap groups |
| Criteria Weights | 4 | 4 of 143 rows one level off (R33 → 1; R38, R39, R107 → 5), none two levels off |
| Rubric Category Balance | 5 | 142 Outcome rows |
| Process Rubrics | 5 | R143 valid |
| Agent-Centric Phrasing | 5 | Every title "The Agent …", no tool names |
| Negative Criteria | 5 | No prohibition or do-nothing row |
| Predicted All-Fail gate | PASS | None predicted |

**Lowest Sub-Dimension:** Overall Rubric Quality - 1 - Major atomicity, over-specificity and coverage defects.
**Summary:** The facts are right throughout (every ID, email, count, call and retention figure checks out), and the per-ticket comment and email rows are well built. The rubric fails on structure: count rows carry id ranges, the note rows bundle each Hold with its reason, R38/R39 and two closed name lists reject valid answers, and the Message column and per-ticket unassigning have no row.

### Issues Found
| # | Row | Issue | Severity | Type |
|---|---|---|---|---|
| 1 | R92 | id range in comment guard | Major | non_atomic |
| 2 | R104 | id range in Backlog count | Major | non_atomic |
| 3 | R105 | id range in Canceled count | Major | non_atomic |
| 4 | R106 | id range in state-change count | Major | non_atomic |
| 5 | R107 | id range; which 24 unstated; any 24 pass | Major | non_atomic, not_self_contained, overly_broad |
| 6 | R114 | four tickets × two fields | Major | non_atomic |
| 7 | R139 | count + identity tail | Major | non_atomic |
| 8–11 | R51, R52, R53, R54 | Hold listing + reason | Major | non_atomic |
| 12–13 | R38, R39 | N/A placeholders rejected | Major | overly_specific |
| 14 | R19 | headline name rejected | Major | overly_specific |
| 15 | R116 | store-build headline rejected | Major | overly_specific |
| 16 | — | Message column ungraded | Major | missing_coverage |
| 17 | — | no per-ticket unassign check | Major | missing_coverage |
| 18 | R38–R42 | sheet count cascade | Moderate | duplicate (overlap group) |
| 19 | R104, R106, R107 | state count cascade | Moderate | duplicate (overlap group) |
| 20 | R113, R114 | new-ticket count overlap | Moderate | duplicate (overlap group) |
| 21 | R93–R97, R99–R101 | 8 Backlog samples, cap 5 | Moderate | duplicate (overlap group) |
| 22 | R20–R25 | 6 What's missing samples, cap 5 | Moderate | duplicate (overlap group) |
| W | R33, R38, R39, R107 | weight one level off | — | Criteria Weights |

### Recommended Fixes
Every fix is in the Fix List above with its mark. All are `checked`: rounds 1–3 ran `hg_rubric_ledger.py fixcheck` (title cap 120 words, no `bundled_writes`/`scope_tail`/`decision_fork`), `hg_rubric_lint.py` on the candidate (only the resolved "one page" format_lock), a self-check, and passes R1–R7 on the changed rows and their siblings with the opposite-pair test. Round 1 changes that drew findings were revised and rechecked: the Backlog samples and volume row stopped bundling the assignee clear (now its own rows), R38/R39 became one restriction, the bare Go-ticket guard R106 came back, DES-344 got a Call row, and the note's name/reason lists were widened to match their sheet siblings. A final round-3 change touched only the four reason rows' justification sentence.

## All Findings

**R19** — Major overly_specific (F3). Rule doc: "then name that message"; NotificationManager.cs WeeklyReminderTitle "They’ve Taken Over… Can You Stop Them? 😱". Fix in Fix List.
**R20–R25** — Moderate overlap group (F2, F3). Five distinct reasons R15–R19 are direct; six more ordinary samples exceed the cap. Fix: delete R25.
**R33** — weight (F2, F3): copying the Agent's own key is weight 1 (like R32).
**R38, R39** — Major overly_specific (R1, F1, F3 unsure). Rule doc: "Final headline and String change are only for Go rows." N/A on non-Go rows is valid. Also in the R38–R42 cascade group (F3, R4) and one level off (F2, F3, R4). Fix in Fix List.
**R40–R42** — Moderate overlap group with R38/R39 (F3, R4): with 36 rows, one wrong call fails two counts. Fix: delete R41, R42.
**R51–R54** — Major non_atomic (F2, F3, R7). Eval 3 §2.2: "A verdict and its reason in one title → independent". DM: "anything the client already schedules that's still a Hold and why". Fix: split.
**R92** — Major non_atomic (F1 lint `bundled_writes`, F2, F3, R7). Scope checklist: "one bare count row on that write kind with no id list".
**R93–R97, R99–R101** — Moderate overlap group (F2, F3): moves to Backlog follow one template; eight samples, cap five. Fix: delete R94, R99, R100.
**R104, R105, R106** — Major non_atomic (F2/F3, R7): id ranges. R104/R106/R107 Moderate cascade (F2, F3, R4). Fix: bare counts; R106 stays as the Go-ticket guard.
**R107** — Major non_atomic (F1 lint, F2, F3, R7), not_self_contained (R6), overly_broad (F3), weight (F2, F3, R4). Fix: bare volume row plus three per-ticket unassign rows.
**R113, R114** — R114 Major non_atomic (F2, F3, R7); R113/R114 Moderate overlap (F2, F3, R4). Fix: four per-ticket Backlog rows.
**R116** — Major overly_specific (F3). Leonard's card comment: "Vincent ticks these as he checks them on the store builds."
**R139** — Major non_atomic (R7). Fix: bare count.
**Missing: Message column** — Major (R3, F3). coherent_record.md C1: "Omitting the whole requested column … is a gap." Fix: new Message row.
**Missing: per-ticket unassign** — Major (F3, F2 unsure). Card: "Held tickets sit in Backlog, unassigned." Fix: R107 split.
**R15, R16, R51, R52 wording** — non-failing (F2, F3). Fix in Fix List.

### Worth a look (not scored)
- R44 "one page": the docs tools return body text, not pages; the judge estimates (F2, F3).
- R46–R49 accept 31.65/31.7/31.6 etc.; whole-percent rounding (32%) would fail (F3).
- R56–R91: the rule says "name the test it failed"; if the call comment must name the test, the comments grade only the call word (F3).
- R92: a summary comment on DES-314 could be read as a 33rd call comment (F2).
- Call column samples skip DES-313's alias row (now DES-344 is added) (F3).

### Rejected findings
- R7: R2 "seven columns" non-atomic — rejected: one header row from one DM sentence (coherent_record.md A1: "Do not demand splitting … A partial-success example … does not cancel this explicit exception").
- R7: R45 section order non-atomic — rejected on the same rule (one ordering requirement of one note from one DM sentence).
- R4: R92 duplicate of R56–R87 — rejected: "This single guard row is not failed as overlap with the per-target rows" (scope checklist); its id-range defect is recorded.
- R4: R140–R142 cascade — rejected: the DM asks for all three numbers ("how many Go, Hold and Drop"), each a separate required fact.
- F3: 19 per-ticket moves missing — rejected: moves to Backlog/Canceled follow one template; scope checklist allows ≤5 samples plus a volume row (cap breach recorded instead).
- F3: Call column 11 samples — rejected: R4–R9 are the six rows the DM says it doesn't trust ("The PN sheet says six are Ready"), covered directly (rubric_sampling.md: core outcomes covered directly); samples R10–R14 = 5.
- Fix rounds: R7 R111–R114 (cand.) state+assignee bundle — rejected: one ticket creation naming its fields is "one row naming every field of one coherent record" (scope checklist). R5 R94 (cand.) ignores ZOM comments — rejected: the original row deliberately set ZOM comments aside and the prompt makes them harmless. R4 round 2 volume/guard overlap — rejected: rubric_sampling.md requires one volume row per template group and the scope checklist allows the bare guard for the Go-ticket decoy. Weight findings on R22/R90/R138 withdrawn after round-1/2 R4: all four comment asks carry the same tracing work, so they stay at 5 like their siblings.

## Deep Recheck

Passes: R1, R2, R3, R4, R5, R6, R7, Opus 5.5 (claude-opus-5-5), each a fresh subagent blind to the main review; full reviewers F2 and F3 ran alongside.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| R1 | 143 rows | 2 | 2 |
| R2 | 143 rows | 0 | 0 |
| R3 | 143 rows | 1 | 1 |
| R4 | 143 rows | 8 | 5 |
| R5 | 143 rows | 0 | 0 |
| R6 | 143 rows | 1 | 1 |
| R7 | 143 rows | 13 | 11 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | R1 | R38 "fills the Final headline column on exactly two rows" | rule doc f_dc45e0e5a8b8635c1b82b2 "Final headline and String change are only for Go rows." | 2.7 | overly_specific | CONFIRMED | N/A placeholders follow the rule |
| DR2 | R1 | R39 "fills the String change column on exactly two rows" | same | 2.7 | overly_specific | CONFIRMED | same |
| DR3 | R3 | DM "one row per message: Message, Ticket, …" | no row grades a Message cell | 3.1 | missing_coverage | CONFIRMED | a blank Message column passes |
| DR4 | R4 | R92 umbrella | scope checklist guard rule | 3.3 | duplicate | REJECTED | guard row exempt; id range recorded as non_atomic |
| DR5 | R4 | R40–R42 counts | DM / rule doc | 3.3 | duplicate | CONFIRMED | one wrong call fails two counts |
| DR6 | R4 | R104–R107 counts | card "Held tickets sit in Backlog, unassigned." | 3.3 | duplicate | CONFIRMED | R106/R107 re-count R104's set |
| DR7 | R4 | R113/R114 | DM "don't make a second one" | 3.3 | duplicate | CONFIRMED | both count the ask tickets |
| DR8 | R4 | R140–R142 | DM "how many Go, Hold and Drop" | 3.3 | duplicate | REJECTED | three separate required facts |
| DR9 | R4 | R22/R90/R138 weight 5 | ZOM-563 cmt_eabac5435f2b3a575aad | 2.12 | weights | REJECTED | same tracing work as sibling comment asks (withdrawn after fix rounds) |
| DR10 | R4 | R107 weight 3 | card | 2.12 | weights | CONFIRMED | same work as R104 |
| DR11 | R4 | R38/R39 weight 3 | R40, R117 | 2.12 | weights | CONFIRMED | count is the Go set |
| DR12 | R6 | R107 "exactly 24 of the tickets" | SQL DES-324/DES-316 assigned | 2.1 | not_self_contained | CONFIRMED | which 24 unstated |
| DR13 | R7 | R2 seven columns | DM sentence | 2.2 | non_atomic | REJECTED | coherent_record A1 |
| DR14 | R7 | R45 order | DM sentence | 2.2 | non_atomic | REJECTED | one ordering requirement |
| DR15 | R7 | R51–R54 | DM "still a Hold and why" | 2.2 | non_atomic | CONFIRMED | verdict + reason |
| DR16 | R7 | R92 | lint bundled_writes | 2.2 | non_atomic | CONFIRMED | id list |
| DR17 | R7 | R104, R105, R106, R107 | id ranges | 2.2 | non_atomic | CONFIRMED | bundled writes |
| DR18 | R7 | R114 | card | 2.2 | non_atomic | CONFIRMED | four tickets, two fields |
| DR19 | R7 | R139 | DM "apart from me" | 2.2 | non_atomic | CONFIRMED | scope tail on guard |

Effect on verdict: the deep recheck confirmed the main findings and added R38/R39 overly_specific, R107 not_self_contained, R139 non_atomic, the Message-column gap and three overlap groups; the score stays FAIL 1.

Platform defects: none (FD-3785 cells in USER_COHORT_RETENTION are not used; the Sep 15 D1/D7 values are mature).

### FINAL VERDICT: FAIL
Score: 1
Execution status: COMPLETE
Review policy: rubric-revision-v10
Review mode: AUDIT
Reviewed JSON SHA-256: 3911b7d5f4de11115d881ad3a1cfc718572501a95fd4a3b99d789f55fa8b80e0
Review context SHA-256: 5bddd4065641003f3c6045f80c97374a6875409f48cda45a7b7e4022817e1444
Scoring record SHA-256: 9bf275c4429bcf198fdbf36f20c900228385c48ece29219e8b0ea8d8f851b7af
Eval version: task-quality-v1
Eval release SHA-256: 81446b85bb68b971bfce06d9d3cf07ad43d923b5702670f206122d1f6d34d53c
Gate tier: localized
Coverage ratio: 154/156
Repairs: See findings
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Evaluator model: Opus 5.5 (claude-opus-5-5)
Next action: Apply the Fix List (copy the checked fixes as written), save the corrected rubric and send /rubric again
Evidence limits: None
