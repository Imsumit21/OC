## RUBRIC EVALUATION REPORT

### Task: Claire Morgan's Zombie Match 3D Halloween art plan (plan doc, tracker, ART ticket comments and assignees, store-art tickets, thread reply)
### Persona: Claire Morgan - Art Lead
### Total Rubrics: 217 (Outcome: 217, Process: 0)

## Fix List

Row numbers are your current rubric's. "checked" fixes passed lint, the fix checker and the deep-recheck passes. "revised after check" rows still drew a confirmed problem after 3 rounds plus a restructure, so they need your own rewrite.

- **R4, R5** (plan doc Reuse): "Reuse" is never defined in the prompt or titles. Copy: `The Agent states in its plan doc that the iPhone 6.5" set, meaning its existing Halloween version is used as is, is Reuse (in any wording with that meaning)` (same for the Google Play phone set). (checked)
- **R6, R7, R8** (plan doc "36 / 12 / 10 of the 58 ads", total or exact list): the exact-list branch bundles 36, 12 or 10 separate ad calls in one row (Major non_atomic); "Refresh first" in R6 is undefined (Major). **This row needs your own rewrite.** Open problem: a total or an unnamed list lets the wrong ads through, a stated rule lets a run pass without working out a single ad, and naming one ad rejects a valid plan doc that gives rules plus counts. Settle first which form the plan doc must use for ad calls. If it must name each ad's call, grade one hard ad per call by name (ART-831 Refresh first, ART-808 Halloween version, ART-811 Skip). If counts are enough, make the count the only accepted form. (revised after check)
- **R9** (Oct 10 rule or exact 30-ad list): same list bundling (Major). **This row needs your own rewrite.** Open problem: a single-ad check on ART-793 that accepts a stated rule lets a run that copies Frederick's two lines ("Android US phone Oct 10 / iOS UK Oct 15") pass without placing ads on both campaigns. Name the dual-campaign case explicitly, or require the ad by name. (revised after check)
- **R10** (Oct 15 rule or exact 18-ad list): same list bundling (Major), and weight 3 where the rule needs mail + Slack + campaigns (5). Copy: `The Agent gives ART-805 (barrel marketing2 4:5, which runs only on iOS UK phone) a due date of Oct 15, 2025 in its plan doc, directly or through a stated rule that iOS UK ads, or ads with new work off Android US phone, are due that day (any date form; a date from Oct 11 to Oct 14, 2025 also passes)`, weight 3. (checked)
- **R15** (Julia on "the ad statics"): the title never says which ads are the statics. Copy: `The Agent names Julia Lawson (or Julia) in its plan doc as the maker or owner of the Halloween work on the ad statics (as the ad statics, ad stills, stills, static ads or statics, or by naming her for the julia static ads ART-825 to ART-830)` (checked)
- **R22** (tracker volume row): keep it as the one volume row, naming the set. Copy: `The Agent lists the 58 live ads ART-793 to ART-835 and ART-840 to ART-854 in its tracker, each with a Halloween call (on one tab or several; rows it adds for the four paused Archive creatives ART-836 to ART-839 are not counted)` (checked)
- **R23, R24, R40, R57, R164, R215**: delete. Each counts separate items or writes ("exactly 14 / 10 / 30", "comments on exactly 58", "assignee on exactly 48", "exactly two store surfaces"). Every item already has its own row. (checked)
- **R25**: `The Agent marks the app icon as Halloween version in its tracker (in any wording with that meaning; marking Martin's Sep 17 concept as the icon fails)` (checked)
- **R26**: add ` (in any wording with that meaning)` at the end. (checked)
- **R27, R28**: `The Agent marks the iPhone 6.5" set as Reuse, meaning its existing Halloween version is used as is, in its tracker (in any wording with that meaning)` (same for the Google Play phone set). (checked)
- **R31, R32, R33**: replace ` as Refresh first in its tracker` with ` as Refresh first, meaning re-captured, re-rendered or re-cut before its Halloween pass, in its tracker (in any wording with that meaning)`. In R32's justification, drop "; the static's place on the list is graded by the tracker's surface count". (checked)
- **R34**: `The Agent marks ART-808 (cheer fastcouch 9:16) as Halloween version in its tracker (in any wording with that meaning; calling Marcus's existing cheer fastcouch Halloween cut done or Reuse fails)` (checked)
- **R35**: add ` (in any wording with that meaning)` at the end. (checked)
- **The 36 "Refresh first" comment rows** (R58, R60, R64, R68, R70, R72, R74, R76, R78, R80, R85, R89, R91, R94, R97, R99, R112, R115, R117, R119, R121, R123, R125, R127, R129, R131, R133, R135, R137, R139, R142, R145, R147, R149, R151, R154): replace `Halloween call is Refresh first (in any wording with that meaning)` with `Halloween call is Refresh first, meaning re-captured, re-rendered or re-cut before its Halloween pass (in any wording with that meaning)`. (checked)
- **R87, R101**: add `; calling Marcus's existing cheer fastcouch Halloween cut done or Reuse fails` inside the closing parenthesis. (checked)
- **R213**: `The Agent opens a new ART ticket to make a new Halloween app icon (a ticket to finish or ship Martin's Sep 17 concept as the icon fails)` (checked)
- **New rows, iPhone 6.5" set due date** (missing in plan doc and tracker): **This row needs your own rewrite.** Arthur's calendar: "new iOS screenshots go up with the Oct 17 submission and are due by the same Oct 16 12:00 PT cut". Accept Oct 16, 2025 or earlier, OR "goes up with the Oct 17 submission" (or its Oct 22 live date); keep "any day" failing. (revised after check)
- **New plan-doc volume row(s)** for whichever plan-doc spot checks you keep: **This row needs your own rewrite.** "Through stated rules that cover them" cannot be graded from the title and lets a blanket rule pass. Accept per-ad coverage, or a rule only when the plan doc ties it to the tickets it covers. (revised after check)
- **R10, R44, R179, R185 weights**: only R10 is off (handled above). R44, R179 and R185 stay as authored.

---

### Phase 1: Structural Validation
- Five-field completeness: 217 of 217
- Category distribution: Outcome 217, Process 0
- Requirement coverage: 228 of 230 outcomes (the missing two are the iPhone 6.5" set's due date in the plan doc and the tracker)

### Phase 2: Per-Rubric Quality
| Row | Issue | Type | Severity |
|---|---|---|---|
| R57, R164, R215 | Count over separate writes | non_atomic | Major |
| R23, R24, R40 | Counts beyond the one tracker volume row | non_atomic | Major |
| R6, R7, R8, R9, R10 | "or as a list of exactly ART-…" bundles 36/12/10/30/18 per-ad results | non_atomic | Major |
| R4, R5, R6, R10, R31–R33 and 36 comment rows | "Refresh first" / "Reuse" accepted "in any wording with that meaning" but never defined | not_self_contained | Major |
| R15 | "the ad statics" undefined | not_self_contained | Major |
| R25, R34, R87, R101, R213 | Label alone passes a run that builds on Martin's rejected icon concept or calls Marcus's rejected test done | overly_broad | Minor |
| R7, R22, R25–R28, R31–R35, R6, R8 | Wording preference without "(in any wording…)" or with a count/label | harmless_specificity | Minor |

Atomicity: every comment, assignment, share, ticket and reply row is one write and one fact. The bundles are the count rows and the exact-list branches.
Over-specificity triage: no row rejects a record-backed valid answer once the conflicts below are settled.

### Phase 3: Set-Level Quality
- Coverage gaps: iPhone 6.5" set due date (plan doc, tracker).
- Process audit: 0 Process rows; none needed.
- Duplicates / cascade: the count rows overlap their per-item rows (already Major, so no extra group).
- Spot-check groups: tracker calls (5 samples), dates (4), owners (4); R22 is the volume row.

### Phase 4: Issue Tally
| Severity | Count | % | Fails when | Status |
|---|---|---|---|---|
| Major | 55 (53 rows + 2 missing outcomes) | 25.3% | any | FAIL |
| Moderate | 0 | 0% | any | — |
| Minor | 10 | 4.6% | ≥ 5% | — |

### Phase 5: Scoring
| Sub-Dimension | Score | Justification |
|---|---|---|
| Overall Rubric Quality | 1 | Major non_atomic, not_self_contained and missing_coverage |
| Criteria Weights | 4 | 1 of 217 rows one level off (R10) |
| Rubric Category Balance | 5 | All Outcome |
| Process Rubrics | 5 | None needed |
| Agent-Centric Phrasing | 5 | Every title starts "The Agent", no tool names |
| Negative Criteria | 5 | No prohibition or do-nothing row |
| Predicted All-Fail gate | PASS | None predicted |

**Lowest Sub-Dimension:** Overall Rubric Quality - 1 - Major count/list bundling and undefined call labels.
**Summary:** Every value in the rubric matches the records: 36 Refresh first, 12 Halloween version, 10 Skip, 30 due Oct 10, 18 due Oct 15, 48 assignees, the four store calls and the six review attendees. The rubric fails on structure: count rows over separate writes, exact-list branches in the plan-doc rows, and call labels it never defines. It also misses the iPhone 6.5" set's Oct 16 date.

## All Findings

- **R57, R164, R215** · Major non_atomic · F1, F2, F3, R4, R7. These rows count separate writes. Eval 3 §2.2 and count-bundle-v1: "A count over separate writes or items … Major even beside per-item rows". Fix: delete.
- **R23, R24, R40** · Major non_atomic · F1, F2, F3, R7, R1. These are counts over tracker items beyond the volume row R22 (Rubric Writing §8: "Add one criterion checking the volume of the output"). Fix: delete.
- **R6, R7, R8** · Major non_atomic · F1, F2, F3, R7. The list branch is a filtered list (Eval 3 §2.2: "asserts each member's status and is split"). A doc with 35 right and 1 wrong fails, while "36" alone passes. Fix: rewrite yourself (see Fix List).
- **R9, R10** · Major non_atomic · F1, F2, F3, R7. The list branch bundles 30 and 18 due dates. Fix: R10 is checked; R9 needs your own rewrite.
- **"Refresh first" rows and R4/R5 "Reuse"** · Major not_self_contained · F2, R6. The deck's meaning ("Refresh first: re-capture, re-render or re-cut before any seasonal pass"; "Reuse: it already has a seasonal version, use that one") is only in the evidence. Fix: the definitions in the Fix List.
- **R15** · Major not_self_contained · R6. Only the ticket titles show which ads are statics ('julia 1:1 (1:1 static)' …). Fix: checked.
- **iPhone 6.5" set due date** · Major missing_coverage (plan doc and tracker) · R3, F3. Release calendar f_fdd6d2d2f4a4d2f5b908fb: "new iOS screenshots go up with the Oct 17 submission and are due by the same Oct 16 12:00 PT cut." Fix: new rows; needs your own rewrite.
- **R25, R34, R87, R101, R213** · Minor overly_broad · R5. Robert C08R8CHB0QL/1758127951.679146: "Nice for an event, but not for the app icon". C08R8CHB0QL/1759248337.170599: "We can't ship these, they need doing again from the Sep 16 one". Fix: the "…fails" clauses (checked).
- **Tracker call rows, R7, R22** · Minor harmless_specificity · F1, F3, R1. They lack the "(in any wording with that meaning)" their siblings carry. R22 also fails a tracker that lists the paused Archive rows. Fix: checked.
- **R10 weight** · one level off (expected 5) · F2. Fixed by the single-ad restructure at weight 3.

### Worth a look (not scored)
- The domain-wide share route (`gdrive_share_file` type/domain) on R45–R56. A commenter share to harmonygames.co gives every reviewer comment access but names no one (F2, F3).
- Oct 10 rows accept any earlier October date, while Oct 15 rows accept only Oct 11–15. This is settled below; consider saying why in the evidence.
- "Both links" in the prompt could be read as the two store tickets (F3). /prompt passed it; the two Drive deliverables are the natural reading.

### Rejected findings
- R1: the Oct 15 rows reject an earlier date. Settled by Frederick's reply C0880U9751A/1759275738.984915, "iOS UK stays on the 15th", which sets a tier. Widening the window would let a flat Oct 10 schedule pass (R5).
- R5: R11–R14 store dates inside Martin's Oct 6–15 vacation. Martin's post sets no deadline, so narrowing has no proof (R1).
- F3: weight 1 for R44; and R4: weight 5 for R179/R185. Kept as authored for consistency with sibling owner and assignment rows (R43, R165+) and the same tickets' due-date rows.
- F2: Oct 15 per-ticket weights to 5. Frederick's mail alone sets "every Halloween ad … by Wed Oct 15"; the Slack reply changes only Android US phone ads.
- F3: ticket links in the thread reply. Leonard's "post the links here" doesn't say which links, and the prompt narrows it to "both links".
- R4 (fix checks): R22 overlaps its samples. Eval 3 §3.3: "Not duplicates: … a spot-check group's one output-volume row versus its samples".
- R3 (fix checks): separate volume rows for tracker dates and owners. Rubric Writing §8 asks for one volume criterion per output; R22 is the tracker's.
- R5 (first pass) on R213. Later accepted in the fix check and fixed.

## Deep Recheck

Seven blind passes (R1–R7) ran on all 217 rows alongside full reviewers F2 and F3. Each cited record was opened before a finding was accepted:

- R2 found no factual error.
- R3 found no gap on the original rubric's writes.
- R6 confirmed the "Refresh first" and R15 self-containment gaps.
- R7 confirmed every count and list bundle.
- R4 found the two assignment weights (rejected above).
- R5 found the overly broad label rows.
- R1 found the Oct 15 window point (rejected above) and the R22 Archive point (Minor).

Then came four fix-check rounds with all seven passes, on the changed rows and their siblings. They confirmed the iPhone 6.5" coverage gap and the R4/R5 "Reuse" gap, which are added to the scoring record. They left eight rows as "needs your own rewrite": R6–R9, the two plan-doc volume rows and the two iPhone rows.

### FINAL VERDICT: FAIL
Score: 1
Execution status: COMPLETE
Review policy: rubric-revision-v10
Review mode: AUDIT
Reviewed JSON SHA-256: 6e8624c28ac6afd18e800b6390a1bb2bcd6b3eb3f51651c4e121a431b19a10df
Review context SHA-256: adc42d25910b71824389b7b5956a01e8abcc244d99beb0869a137b4c0405de5f
Scoring record SHA-256: c71bcb536ae3c6d597a94f2d679ba66ac1c394069836d7c98021ed18ae373990
Eval version: task-quality-v1
Eval release SHA-256: b9281224e0e101faab431b7e10f928a29b8c6f02ebd52037b8aaa26ca5f9fc8c
Gate tier: localized
Coverage ratio: 228/230
Repairs: See findings
Evaluator model: Opus 5.5 (claude-opus-5-5)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Next action: Apply the Fix List (delete six count rows, add the call definitions, rewrite R6–R9 and add the iPhone 6.5" date rows yourself), then send /rubric again.
Evidence limits: None
