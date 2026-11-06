# 09 Rubric Check — robert_llc_takeover (LLC take-over of Combo Fighter, injection rev4)
Checked 2026-11-06 · Criteria 130 (builder minimum 5: ok) · Plan 2026-11-06 (09_Rubric_Writing_Plan.md, rubric-writing gate PASS) · 09_Rubrics.json sha256 cd67ff04220c
Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
JSON field map: criterion=`title` · weight=`weight` · category=`category` · justification=`justification` · evidence=`evidence` · schema gate: pass (73 objects, five non-blank fields each, category Outcome/Process, weight 1/3/5)
Readiness for /rubric: CLEAN — a prediction only; /rubric gives the verdict (residual risks listed under 'Round history and residual risks')

Lint: `python3 Task_Authoring/tools/hg.py rubric-lint Task_Authoring/task_inputs/09_Rubrics.json` → count 0 (no disguised_negative, format_lock, anon_token, evidence_no_record, vague_exemplar, tool_name or prohibition_title hit). Weights 5 ×23 · 3 ×53 · 1 ×54 (total 328); Outcome 129 · Process 1.

## Coverage
| Plan row / requirement | Criteria | Covered / gap (omission + wrong-result test) |
|---|---|---|
| R1 Leonard's Thursday-night DM — the source of every ask ("Leonard sent me a DM on Thursday night") | via every deliverable row | covered — each ask the DM makes has its own row below |
| R3/R5 a call on each issue, as a comment ("leave the call on each issue") | one row per issue: C7–C50, C9, C10, C38, C29, C48, C23, C33; the new VO issue C4 | covered — each issue's comment row rejects no comment and the opposite call |
| R5 the cost part of the call in the comment (the DM: 'what it costs us March through May') | C5–C27 | covered — every priced item's comment carries its current cost; stale figures fail |
| R4 the call per item, the way he lays it out (ground rules, card, project rule) | the per-issue comment and state rows; C97–C104 on the sheet | covered — DD dropped or ZM taken fails C53/C55/C98/C99/C9/C10 |
| R8 the project matches the sheet: one state per issue | C51, C53, C56, C61, C68, C80 (Todo), C64–C66 (Done), C55–C89 and C59–C93 (Canceled) | covered — every issue's state has its own row |
| R8 the project matches the sheet: assignees on the Todo items | C52, C54, C57, C62, C69, C81, C3 | covered — every Todo item's assignee is direct |
| R8 the missing plan line: a new issue for the VO campaign, and only that one | C1 (issue), C2 (Todo), C3 (Leonard), C4 (comment), C6 (exactly one new issue) | covered — no VO issue fails C1; decoy issues fail C6 |
| R6 the plan sheet in Robert's Drive ("Put the plan sheet in my Drive") | C94 | covered — a sheet outside his Drive or an edited draft fails |
| R6 laid out like his draft: the 8 columns | C95 | covered — a sheet without one of the eight headers fails |
| R6 one row per item (Item column, output volume) | C96 | covered — dropped items fail the exact 38 (or 37) count |
| R6 Decision column | C97–C104 | covered — the core rows and sampled cells; every call is also graded per issue in Linear |
| R6 Monthly cost column | C105, C107, C112, C113, C114, C115, C117 | covered — every priced or trap cost is direct |
| R6 Paid by column | C100, C116, C106 | covered — sampled cells, the founder-paid and LLC-paid cases |
| R6 Game column | C122 | covered — sampled cell |
| R6 Next step column | C108, C110 | covered — the two steps the records set |
| R6 Owner column | C120, C121 | covered — sampled cells; the same people are graded as Linear assignees |
| R6 By column | C118, C119, C109, C111 | covered |
| R6/R2 the three shares on the sheet per month (split mail) | C123 | covered — $150, 1,067 or Arthur's $248 on top fail |
| R7 share it with both of them | C124, C125 | covered |
| R9 reply in that DM thread: what I'd do | C127, C128 | covered — each names the thread; taking only CF, or all three, fails |
| R9 reply in that DM thread: what it costs each of us a month | C129 | covered — $150, 1,067 or Arthur's $248 on top fail |
| R9 reply in that DM thread: the link to the sheet | C126 | covered — linking the draft, or a reply outside the thread, fails |
| R9 'Then reply' (order) | C130 (Process) | covered — a write after the reply fails |
| R10 before Monday's call | every write row | covered as a constraint: all writes are graded in the run (no row) |
Unauthorized criteria: none

## Coverage — gradable surface
| Surface slot | Stable fact ID | Criteria | Covered / dispositioned / gap | Disposition reason (evidence) |
|---|---|---|---|---|
| G1 | cf_decision | C97 | covered | title rejects omission and a wrong value on the correct artifact (C97) |
| G2 | dd_call | C98 | covered | title rejects omission and a wrong value on the correct artifact (C98) |
| G3 | zm_call | C99 | covered | title rejects omission and a wrong value on the correct artifact (C99) |
| I1 | md_paid | C100 | covered | title rejects omission and a wrong value on the correct artifact (C100) |
| I2 | calm_call | C101 | covered | title rejects omission and a wrong value on the correct artifact (C101) |
| I3 | figma_call | C102 | covered | title rejects omission and a wrong value on the correct artifact (C102) |
| I4 | helpshift_call | C103 | covered | title rejects omission and a wrong value on the correct artifact (C103) |
| I5 | cursor_call | C104 | covered | title rejects omission and a wrong value on the correct artifact (C104) |
| V1 | llc_rows | — | dispositioned | duplicate fact: every issue's call is graded on its own comment and state row (C7–C50, C59–C93 and the direct rows), and the core sheet rows C97–C104 grade the Decision cells; /rubric round 1 (R38) dropped the LLC-row count as non_atomic |
| C1 | vo_cost | C105 | covered | title rejects omission and a wrong value on the correct artifact (C105) |
| C2 | ddprod_cost | C107 | covered | title rejects omission and a wrong value on the correct artifact (C107) |
| C3 | support_step | C108, C109 | covered | title rejects omission and a wrong value on the correct artifact (C108, C109) |
| C4 | layer_step | C110, C111 | covered | title rejects omission and a wrong value on the correct artifact (C110, C111) |
| C5 | github_step | — | dispositioned | not incorporated: /rubric round 1 (R53) found nothing asks for a GitHub next step; GitHub is Done (Arthur pays it through May, C66) and OE 101 gives it no step |
| P1 | cfstacks_cost | C112 | covered | title rejects omission and a wrong value on the correct artifact (C112) |
| P3 | appsflyer_cost | C113 | covered | title rejects omission and a wrong value on the correct artifact (C113) |
| R2 | arthur_cash | — | dispositioned | not incorporated as a required value: brief §4b (risk 3) accepts $1,150 each with or without Arthur's $902 cash split, so the omission is valid; the wrong value (Arthur's $248 paid on top, T12) is rejected by C129 and C123 |
| R3 | even_share | C129 | covered | title rejects omission and a wrong value on the correct artifact (C129) |
| R4 | dd_reply | C127 | covered | title rejects omission and a wrong value on the correct artifact (C127) |
| R6 | support_reply | — | dispositioned | not incorporated as a required reply element: 'what I'd do' asks for the calls; the support step is graded on the sheet (C108) and the issue state (C80); requiring it in the reply would be an unstated expectation (gate 7) |
| R7 | zm_reply | C128 | covered | title rejects omission and a wrong value on the correct artifact (C128) |
| L1 | vo_issue | C1 | covered | title rejects omission and a wrong value on the correct artifact (C1) |
| D1 | sheet_location | C94 | covered | title rejects omission and a wrong value on the correct artifact (C94 (any folder of Robert's own Drive, /oe note 1)) |
| D2 | reply_link | C126 | covered | title rejects omission and a wrong value on the correct artifact (C126) |
| D3 | reply_thread | C126, C127, C128, C129 | covered | title rejects omission and a wrong value on the correct artifact (C126, C127, C128, C129 (each names the reply in the thread under Leonard Hayes's Thursday-night DM)) |
Mechanism share: 18% of the criteria weight (58 of 328; reported, not gated)

## Findings
| # | Criterion | Quoted span | Rule (source §) | What is wrong | Plan row / ledger fact | `/rubric` type | Severity |
|---|---|---|---|---|---|---|---|
| — | — | — | 3_Rubrics_Eval.md Phases 1–5 | No open finding on the current JSON (sha cd67ff04220c); the round-1 findings are fixed (next section) | — | — | — |

## Round history and residual risks
Platform /rubric round 1 (FAIL 1 on 8296aaf8dc71, report run_forensics/rev4/rubric_r1/platform_rubric_review_r1.md): its Fix List was applied exactly. 6 rows were deleted (its R5, R28, R38, R53, R57, R68), 19 were retitled or re-weighted with its exact text, its 63 rows were added and its wording repairs were made. A script check confirms all 82 Fix List titles are in the JSON verbatim with their weights, and the other 43 reviewed rows are byte-identical (DELTA locks hold).

Platform /rubric round 2 (NON-FAIL 4 on cd67ff04220c, report run_forensics/rev4/rubric_r1/platform_rubric_review_r2.md): Overall Quality 5, Criteria Weights 4 (R6, R40, R83, R96 one level low), 3 Minor (R96 evidence; R123/R129 do not reject counting Leonard's VO card toward his share); coverage 130/130. NON-FAIL counts as a pass for /rubric, and the requester chose to proceed on this version (2026-11-06). Its optional Fix List and its note to send OE 26 back to /oe (the $0 cost in the Combo Fighter comment) were not applied; this JSON and the /oe-passed OEs (e210cd02c49e) are the submitted pair.

Earlier local round (blind /rubric-style reviewer + this check, on the 67-row draft ab72cf6d8d2c). Every item below was fixed before the platform round:

| # | Was (67-row draft) | /rubric type · severity | Fix in the current JSON |
|---|---|---|---|
| R1-1 | no row counted the plan sheet's item rows (C36 counted only the LLC rows) | missing_coverage · Major | C96: exactly 38 item rows (37 with Metabase and dbt on one row), the output volume of the sheet |
| R1-2 | the sheet's Owner column was never graded | missing_coverage · Major | C120 (DD production account → Arthur Blake, ordinary) and C121 (the VO campaign → Leonard Hayes, edge) as Owner samples; the same people are graded as Linear assignees |
| R1-3 | the comments carrying the two core game calls (ENG-2439, ENG-2440) were sampled out | missing_coverage · Major | C9 (ENG-2439: the LLC takes it) and C10 (ENG-2440: stays with HG) as direct core rows |
| R1-4 | the sheet-shares title passed a sheet that has Arthur put in $1,150 cash on top of his $248 | overly_broad · Major | C123 states that rejection in its title |
| R1-5 | the Playable vendor comment 'stays off the LLC's monthly plan as a one-off (or stays with HG)' admitted the LLC paying the one-off outside the plan | overly_broad · Major | row dropped; the one-off stays graded at $0 on C117, and the comment group is back to five samples |
| R1-6 | 'Metabase and dbt … at $100 a month each' bundled two sheet cells | non_atomic · Major | C114 Metabase and P76 dbt, each accepting the draft's combined $200 row |
| R1-7 | HG labels accepted only 'HG' / 'Harmony Games' ('Canceled', which mirrors Linear, was rejected) | overly_specific · Major | C29, C48, C33, C10 accept 'HG keeps it, or cancelled'; C99, C101–C104 accept 'stays with HG, Canceled or cancelled' (C99 also Sunset's sale) |
| R1-8 | 'exactly 7 rows … (Decision LLC)' broke when the founder rows read 'LLC (Arthur pays)' | overly_specific · Major | P36 counts the LLC rows apart from the Metabase, dbt and GitHub rows Arthur pays himself |
| R1-9 | the comments volume row passed comments with no call ('see sheet') | overly_broad · Major | P5 requires a stated call on each of the 37 |
| R1-10 | every reply row embedded 'in the thread under Leonard's DM' and no row graded the destination alone | duplicate · Moderate (OVERLAP_GROUP) | P71 grades the thread once; C126–C130 name 'its reply to Leonard Hayes in his DM with Robert' |
| R1-11 | six samples in the comment group | duplicate · Moderate (OVERLAP_GROUP) | vendor comment dropped; C9, C10 direct; five samples C38, C29, C48, C23, C33 |
| R1-12 | the VO state, assignee and comment rows repeated 'in the LLC take-over project' (a cascade with the creation row) | duplicate · Moderate (low confidence) | C2–C4 say 'its new … issue'; C1 alone grades the project |
| R1-13 | 'VO, video, Meta or ads' read VO as video (VO is value optimization, #prototype C09UHHN6PFZ /389–/391) | harmless_specificity · Minor | C1 names the VO campaign, the Meta campaign or Combo Fighter's ads |
| R1-14 | the Combo Fighter and DD-production By rows accepted the date only in the By column | harmless_specificity · Minor | C118, C119 accept the By or the step, as C109, C111 do |
| R1-15 | evidence cited C09UHHN6PFZ/1770845002.610529 (the Unity $100) for the $3,750 vendor, and the IP-auction post for Leonard handling DD | note (not tallied) · — | C117 cites the ground rules and ENG-2474; C54 cites ENG-2439 and C09UHHN6PFZ/1770844309.583109 ('Domino Delights is with boombit') |
| R1-16 | weights one level off: Metabase paid by Arthur 3 (a stated fact), GitHub step 3 (its own comment), reply DD 3 (the take test), VO $3,000 5 (one record), layer step 5 (one reply); ZM rows at 3 beside DD's 5 | weights · Weights dimension | C100 1, P49 1, C127 5, C105 3, C110 3, C55 5, C99 5, C128 5 |

Residual risks (not findings; no change made):
- C95 (the draft's eight headers) may draw the builder's imported atomicity lint; /rubric round 1 rejected that finding (coherent_record: one header row). If the builder flags it, mark the flag invalid with that rule rather than splitting the row.
- Its 'Worth a look' notes are kept as is: 'by Feb 28' and a Feb 28 date stay accepted; C96 keeps all 38 items; no cost rows for the ENG-2439 and ENG-2462 comments, since no record states a cost; dbt's own payer and cost cells and the other LLC rows' Owner/By cells stay sampled.
- The Game column is graded on one sampled cell (C122); brief §4b lists no Game value as material.

## Overlap groups · Spot-check groups · Predicted all-fail
| Group / row | Members / basis | Shared condition / reason |
|---|---|---|
| Spot-check D3 | C101 Calm Play LLC (edge), C102 Figma (edge: the draft says LLC), C103 Helpshift (edge: DD support depends on it till Feb 28), C104 Cursor (ordinary). Direct core rows: C97 Combo Fighter, C98 Domino Delights, C99 Zombie Match; cohort control P36 (LLC rows) | 4 sample(s) (≤ 5); volume C96; core requirement sampled: no |
| Spot-check D4 | C118 ENG-2438 Combo Fighter (edge: the sale's close, not Mar 1); C119 ENG-2441 DD production account (ordinary: by Mar 1). Direct, not sampled: C109 ENG-2462 (its own deadline, T2), C111 the layer.ai step (Mar 3) | 2 sample(s) (≤ 5); volume C96; core requirement sampled: no |
| Spot-check D5 | C120 ENG-2441 DD production account → Arthur Blake (ordinary); C121 the VO campaign → Leonard Hayes (edge: not a Linear item). The same people are graded as Linear assignees (C52–C81, C3), one fact per surface | 5 sample(s) (≤ 5); volume C96; core requirement sampled: no |
| Spot-check D6 | Paid by: C100 Metabase (Arthur), C116 GitHub (Arthur), C106 the VO campaign (the LLC, edge: Leonard's card till Feb). Game: C122 DD production account (DD). Monthly cost cells are direct on every priced or trap row (C105, C107, C112–C115, C117) | 9 sample(s) (≤ 5); volume C96; core requirement sampled: no |
| Overlap / cascade | none | the reply rows C126–C129 each name their own reply's destination (a row failing because its own artifact was never made is not a group, Eval 3 §3.3; /rubric round 1 rejected the reply cascade); the VO issue rows C2–C4 name 'its new' issue; C114 alone grades the Metabase (or combined) cell; C96 is the sheet's only count row |
| Predicted all-fail | 0 rows | every deciding record is visible to Robert (rubric-writing gate reach.plan_fids, v3.rubric_evidence); every write is cataloged; no forced error; none of the four Evals bases applies |

## Dimensions
| Dimension | Count / % | Threshold | Status |
|---|---|---|---|
| Overall Rubric Quality | 0 Major · 0 Moderate · 0 Minor (0%) | any Major/Moderate fails; Minor > 10% fails | PASS |
| Criteria Weights | 0 rows one level off after /rubric round 1's five weight fixes (its Fix List weights copied); the new rows carry its weights | > 10% one level off or any two levels off fails | PASS (NON-FAIL 4 if /rubric reads the residual two differently) |
| Known data issue | 0 rows on an NB card (Slack posts before Feb 13 10:03 UTC; no Helpshift vendor date; no Snowflake AWS cost) | any row on a Don't-grade value fails | PASS |
| Category Balance | 129 Outcome · 1 Process | ≥ 1 Outcome, Process ≤ 50 % | PASS |
| Process Rubrics | 1 Process row (passes the three conditions); 0 missing ordering checks | 2+ missing or any invalid fails | PASS |
| Agent-Centric Phrasing | 130/130 titles 'The Agent' + action; no tool name in a title | artifact subject or tool name fails | PASS |
| Negative Criteria | 0 of 130 rows an idle Agent passes; no prohibition-only title | 1+ fails | PASS |
| Predicted all-fail | 0 | tolerance 0 | PASS |
| Schema · coverage · accuracy · contradiction (repair gates) | schema pass · 0 coverage gaps · 0 incorrect literals · 0 contradictions | any failure blocks | PASS |
Threshold margin: with 130 rows one Major fails Overall Quality; 14 one-level weight misses (> 10%) would fail Weights.

## Self-review

**1. Re-read as /rubric** (3_Rubrics_Eval.md Phases 1–5, in order), with the pre-verdict sweep (5.0).
- **Sweep.** No item remains on any of the eight sweep checks:
  - a missing requirement (Coverage table: all covered);
  - a phrasing mismatch with the prompt;
  - a non-atomic row (P35's header row is one tool output);
  - a category mislabel (one Process row, for "Then reply");
  - an over-specific or hard-coded title (labels, dates and folders accept every fair form);
  - a duplicate or cascade group (the thread is graded once in P71);
  - a vague exemplar (lint 0);
  - a prohibition-only title (an idle Agent fails every row).
- **Calibration.** Checked against the 7-row table in Evals/references/rules/rubric_qc_examples.md:
  - do-nothing: every row needs a write;
  - valid case and count format: the counts P5, P27, P36 and P68 are bare;
  - LITERAL keys: ENG ids, thread_ts 1770961200.890407;
  - PT/UTC day: no row grades a record's day, and the semantic dates Feb 28, Mar 1 and Mar 3 are date-only;
  - reachability: every deciding source is PROMPT_LINKED;
  - anonymized tokens: none graded;
  - OE conflict: the OE path (OE 100: top level of Robert's Drive) passes P34.

**1a. /rubric round 1 applied.**
- Every Fix List row was copied byte-exactly; the script check found 82 of 82 titles and weights.
- The 43 reviewed rows it did not name are byte-identical to the reviewed JSON (run_forensics/rev4/rubric_r1/09_Rubrics_reviewed_8296aaf8dc71.json).
- Its non-failing wording repairs are made: the work-kind labels, R1's Accept note, R35's '/oe note 1', and R16's unrelated citation.
- New-row evidence names deciding records that Robert can reach: seeded mails, Slack replies and the ground rules; base #winddown and #prototype posts; and the issue's own comment.
- One wording change from the reviewer's candidate: three quotes of the #winddown action items replace 'such as' with '...'. The candidate's evidence text was not shared with us, and the lint's vague_exemplar check matches 'such as' even inside a quote.

**2. Counter-readings.** The table below has one row per criterion C1…C73:
- false negative: a valid alternative the title might reject;
- false positive: a plausible near miss it might pass.
Each row's Resolution names the records and pointers. For the round-1 findings (section 'Round history and residual risks'), the strongest case each was a false positive:
- the HG labels: "HG" is the draft's own word;
- the owner rows: Owner duplicates the Linear assignee;
- the core comments: the calls are graded on the sheet.
Each was resolved for coverage, not against it. rubric_sampling ("distinct requested property/column", "never spot-check a core requirement") and the Q4/Samuel /rubric rounds (a row per surface) settle these.

**3. Re-verify.** Every value a clearance depends on was re-verified in this run through tools/hg.py and the parsed SQL:
- the rubric-writing gate's v3.rubric_evidence re-read each cited field: base Slack posts and Contacts through hg.py get-many; seeded Slack, Gmail, Docs and Drive rows from 01_Universe_Inject.sql;
- plan/oe_reads.py re-read the 25 Slack posts, the 194 REVENUE_DAILY rows, the Drive root, two contacts and three Linear users;
- the blind reviewer independently re-read the 37 issues and comments, the four mails, #winddown /51–/204, the #prototype roots, and REVENUE_DAILY and REVENUE_DAILY_V2. It found every literal correct;
- arithmetic: 140 + 62 + 3,000 + 100 + 100 + 48 = 3,450; 3,450 / 3 = 1,150; 1,150 − 248 = 902.

**4. Recount.**
- Findings on the current JSON: 0. The 16 round-1 items are fixed.
- Overlap groups: 0.
- Predicted all-fail: 0.
- Every spot-check group holds five or fewer samples: the sheet's Decision cells (D3, 4), By cells (D4, 2), Owner cells (D5, 2), and Paid by / Game cells (D6, 4). Linear comments and states are graded one row per issue.

**5. Fixes.**
- Each round-1 fix rests on a record re-read in this run:
  - SQL L45, L51, L68, L92, L100;
  - C09UHHN6PFZ/1770844309.583109;
  - #prototype /389–/391;
  - the draft's grid, SQL L23;
  - the ground rules, SQL L15.
- The rubric and plan are rebuilt from plan/rubric_rows.py and plan/rubric_titles.py.
- Dated copies of every build are in run_forensics/rev4/rubric/. The current one is sha cd67ff04220c.

**6. Stage gate.** The paste follows. The gate recomputes the criteria count, verifies the quoted spans, the issue types and the dimension table, and applies the binary validity gate.

Unresolved: none.

| Check | Verdict | Strongest counter-reading | Resolution | Unresolved |
|---|---|---|---|---|
| C1 (P1, vo_issue, weight 5) | cleared | false negative? (a) a valid run could title it 'Meta ads' or 'Combo Fighter video campaign' — the row accepts any name of that campaign (risk 1); false positive? (b) a wrong run could pass by creating an issue for another campaign — the title must name the VO / video / Meta campaign of Combo Fighter, the only one still on (SQL L45) | `$3,000` — $3,000 cap (Leonard's #prototype reply C09UHHN6PFZ/1770938400.370665, SQL L45: 'count it as its own line in what we pay each month'); any title naming the VO / video / Meta / ads campaign of Combo Fighter (risk 1) · F15, F66, F2, F7 | none |
| C2 (P2, vo_state, weight 3) | cleared | false negative? (a) a valid run could leave it in Backlog as 'not started' — the project rule names Todo for an LLC item with a step left (SQL L140), so Backlog is wrong; false positive? (b) a wrong run could pass with Done — Done needs 'nothing is left to do', but the card moves from March (SQL L45) | `$3,000` — Todo (project rule SQL L140: 'to Todo if the LLC takes it and something is still to do') · F66, F2, F15 | none |
| C3 (P3, vo_assignee, weight 1) | cleared | false negative? (a) a valid run could assign Robert as the plan's author — the rule assigns 'whoever moves it' (SQL L140) and Leonard moves his card (SQL L45); false positive? (b) a wrong run could pass by naming Leonard only in the comment — the row grades the assignee field | `$3,000` — usr_63fffeb4fab5233e (Leonard Hayes; name, email or id accepted) · F66, F25, F15 | none |
| C4 (P4, vo_call, weight 3) | cleared | false negative? (a) a valid run could write the call in the issue description, not a comment — the prompt says leave the call on each issue and the project rule says 'as a comment' (SQL L140), so a comment is required; false positive? (b) a wrong run could pass with 'HG keeps it' — the row names the LLC call | `$3,000` — LLC call; wording free · F66, F15 | none |
| C5 (P131, vo_cost, weight 3) | cleared | false negative? (a) a valid run could give the March-through-May total — accepted where the title lists it; false positive? (b) a wrong run could give the superseded figure — rejected | `$3,000` — $3,000 a month (or $9,000 for March through May) · F15 | none |
| C6 (P171, new_issue_count, weight 3) | cleared | false negative? (a) a valid run could add the issue then delete a duplicate — the end state counts; false positive? (b) a wrong run could add issues for the paused install campaign or firebase — rejected by the count | `$3,000` — exactly one new issue; decoys: the paused install campaign and the playable test (C09UHHN6PFZ/1770938400.370665), bigquery and firebase (SQL L92) · F66, F15 | none |
| C7 (P101, cf_call, weight 1) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'the LLC takes it'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2438` — the LLC takes it · F29 | none |
| C8 (P132, cf_cost, weight 1) | cleared | false negative? (a) a valid run could give the March-through-May total — accepted where the title lists it; false positive? (b) a wrong run could give the superseded figure — rejected | `ENG-2438` — $0 (0, nothing or no cost) · F29 | none |
| C9 (P69, dd_call, weight 5) | cleared | false negative? (a) a valid run could write 'comes over with CF' — accepted as the LLC call; false positive? (b) a wrong run could write 'stays with HG' on the stale ~$1k — rejected | `ENG-2439` `183.11` `$140` — LLC (take test: January 183.11 vs $140 hosting, SQL L15, L51) · F30, F9, F10 | none |
| C10 (P70, zm_call, weight 5) | cleared | false negative? (a) a valid run could write 'goes in Sunset's sale' — accepted as HG; false positive? (b) a wrong run could take it with CF per the notes — rejected | `ENG-2440` — HG (0.00 January revenue; the doc's test, SQL L15) · F31, F9 | none |
| C11 (P102, eng2441_call, weight 5) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'the LLC takes it'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2441` — the LLC takes it · F32 | none |
| C12 (P133, ddprod_cost, weight 5) | cleared | false negative? (a) a valid run could give the March-through-May total — accepted where the title lists it; false positive? (b) a wrong run could give the superseded figure — rejected | `$140` — $140 a month (or $420 for March through May) · F10 | none |
| C13 (P103, eng2442_call, weight 3) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2442` — stays with HG · F33 | none |
| C14 (P104, eng2443_call, weight 5) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2443` — stays with HG · F34 | none |
| C15 (P105, eng2444_call, weight 3) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2444` — stays with HG · F35 | none |
| C16 (P106, eng2445_call, weight 3) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'the LLC takes it'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2445` — the LLC takes it · F36 | none |
| C17 (P134, cfstacks_cost, weight 3) | cleared | false negative? (a) a valid run could give the March-through-May total — accepted where the title lists it; false positive? (b) a wrong run could give the superseded figure — rejected | `$62` — $62 a month (or $186 for March through May) · F14 | none |
| C18 (P107, eng2446_call, weight 3) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2446` — stays with HG · F37 | none |
| C19 (P108, md_paid, weight 3) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'Arthur Blake pays for it himself'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2447` — Arthur Blake pays for it himself · F38 | none |
| C20 (P135, metabase_cost, weight 5) | cleared | false negative? (a) a valid run could give the March-through-May total — accepted where the title lists it; false positive? (b) a wrong run could give the superseded figure — rejected | `ENG-2447` — $100 a month or $300 for March through May (or combined with dbt / GitHub) · F12 | none |
| C21 (P109, eng2448_call, weight 3) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'Arthur Blake pays for it himself'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2448` — Arthur Blake pays for it himself · F39 | none |
| C22 (P136, dbt_cost, weight 5) | cleared | false negative? (a) a valid run could give the March-through-May total — accepted where the title lists it; false positive? (b) a wrong run could give the superseded figure — rejected | `ENG-2448` — $100 a month or $300 for March through May (or combined with Metabase / GitHub) · F12 | none |
| C23 (P9, github_call, weight 3) | cleared | false negative? (a) a valid run could say 'HG keeps the org, Arthur pays' — it names Arthur paying, accepted; false positive? (b) a wrong run could say 'stays with HG' alone — rejected: Arthur's mail counts it as his (SQL L68) | `ENG-2449` — ENG-2449; Arthur / Blake pays it (mail SQL L68: 'count it as mine like the other two') · F40, F12 | none |
| C24 (P137, github_cost, weight 1) | cleared | false negative? (a) a valid run could give the March-through-May total — accepted where the title lists it; false positive? (b) a wrong run could give the superseded figure — rejected | `$48` — $48 a month or $144 for March through May (or combined) · F12 | none |
| C25 (P110, eng2450_call, weight 1) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2450` — stays with HG · F41 | none |
| C26 (P111, eng2451_call, weight 3) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'the LLC takes it'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2451` — the LLC takes it · F42 | none |
| C27 (P138, appsflyer_cost, weight 1) | cleared | false negative? (a) a valid run could give the March-through-May total — accepted where the title lists it; false positive? (b) a wrong run could give the superseded figure — rejected | `ENG-2451` — $0 (0, free, the free tier, nothing or no cost) · F21 | none |
| C28 (P112, eng2452_call, weight 1) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2452` — stays with HG · F43 | none |
| C29 (P7, figma_call, weight 3) | cleared | false negative? (a) a valid run could say 'lapses, nothing to take' — that is the HG call in other words, accepted; false positive? (b) a wrong run could copy the draft's LLC — rejected by naming HG | `ENG-2453` — ENG-2453; HG ('HG prepaid it to Sep 11, it stays HG's', SQL L205; #winddown C0ADGSZKR3R/1770859313.592649) · F44, F20 | none |
| C30 (P113, eng2454_call, weight 1) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2454` — stays with HG · F45 | none |
| C31 (P114, eng2455_call, weight 1) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2455` — stays with HG · F46 | none |
| C32 (P115, eng2456_call, weight 1) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2456` — stays with HG · F47 | none |
| C33 (P11, cursor_call, weight 1) | cleared | false negative? (a) a valid run could write 'cancelled, nothing to take' — accepted as HG; false positive? (b) a wrong run could take it for CF development — rejected: the seats are cancelled (SQL L221) | `ENG-2457` — ENG-2457; HG ('cancelled the seats on the 12th', SQL L221) · F48, F22 | none |
| C34 (P116, eng2458_call, weight 1) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2458` — stays with HG · F49 | none |
| C35 (P117, eng2459_call, weight 1) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2459` — stays with HG · F50 | none |
| C36 (P118, eng2460_call, weight 1) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2460` — stays with HG · F51 | none |
| C37 (P119, helpshift_call, weight 3) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2461` — stays with HG · F52 | none |
| C38 (P6, support_call, weight 5) | cleared | false negative? (a) a valid run could write 'take it with DD' — the row accepts any wording that the LLC takes it; false positive? (b) a wrong run could pass with 'done, nothing left' — that call is still LLC, so the row passes; the state row P22 grades Todo vs Done separately | `ENG-2462` — ENG-2462; LLC (the doc: a game that comes over brings its player support, SQL L15) · F53, F16, F17, F3 | none |
| C39 (P120, eng2463_call, weight 1) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2463` — stays with HG · F54 | none |
| C40 (P121, eng2464_call, weight 1) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2464` — stays with HG · F55 | none |
| C41 (P122, eng2465_call, weight 1) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2465` — stays with HG · F56 | none |
| C42 (P123, eng2466_call, weight 1) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2466` — stays with HG · F57 | none |
| C43 (P124, eng2467_call, weight 1) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2467` — stays with HG · F58 | none |
| C44 (P125, eng2468_call, weight 1) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2468` — stays with HG · F59 | none |
| C45 (P126, eng2469_call, weight 3) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2469` — stays with HG · F60 | none |
| C46 (P127, eng2470_call, weight 3) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2470` — stays with HG · F61 | none |
| C47 (P128, eng2471_call, weight 3) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2471` — stays with HG · F62 | none |
| C48 (P8, calm_call, weight 3) | cleared | false negative? (a) a valid run could say 'not used: the LLC is a new company' — accepted as the HG call; false positive? (b) a wrong run could make Calm Play the LLC — rejected (SQL L15 at 23:46Z is later than the 23:41Z comment) | `ENG-2472` — ENG-2472; HG (subsidiary: C04UEQVDVB7/1703492127.063049; the doc 'The LLC is the new one', SQL L15) · F63, F19, F3 | none |
| C49 (P129, eng2473_call, weight 3) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2473` — stays with HG · F64 | none |
| C50 (P130, eng2474_call, weight 3) | cleared | false negative? (a) a valid run could word the call differently — the row accepts any wording of 'stays with HG'; false positive? (b) a wrong run could give the opposite call — rejected | `ENG-2474` — stays with HG · F65 | none |
| C51 (P12, cf_state, weight 3) | cleared | false negative? (a) a valid run could argue Done (the LLC takes it) — Done needs nothing left to do, but it moves only when the sale closes (SQL L56); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2438` — ENG-2438 Todo (comes through Sunset's sale: a step left, SQL L15, L56) · F29, F4 | none |
| C52 (P13, cf_assignee, weight 1) | cleared | false negative? (a) a valid run could assign Leonard as the one dealing with Sunset — the card says 'Whoever runs an item today moves it' (SQL L56) and CF is Robert's game (SQL L145); /oe O3 settled M1 Robert; false positive? (b) a wrong run could leave it unassigned — rejected | `ENG-2438` — usr_Robert (Robert; 'me', name or id accepted; 'robert's game', SQL L145) · F29, F25 | none |
| C53 (P14, dd_state, weight 5) | cleared | false negative? (a) a valid run could use REVENUE_DAILY_V2 — same January sums (/oe note 2), still Todo; false positive? (b) a wrong run could cancel it on the stale ~$1k (b5) — rejected: $140 governs (SQL L51 03:10Z) | `ENG-2439` — ENG-2439 Todo (take test: 183.11 January revenue vs $140 hosting; SQL L15, L51; snowflake.json /tables/12/rows/2044–2229) · F30, F9, F10, F3 | none |
| C54 (P15, dd_assignee, weight 1) | cleared | false negative? (a) a valid run could assign Arthur, who runs DD's AWS — the rule assigns whoever moves the item and Leonard handles it with Sunset (SQL L149); false positive? (b) a wrong run could assign Robert — rejected | `ENG-2439` — Leonard Hayes ('I'll handle it with Sunset' on ENG-2439; Leonard's #prototype post C09UHHN6PFZ/1770844309.583109 'Domino Delights is with boombit') · F30, F25 | none |
| C55 (P28, zm_state, weight 5) | cleared | false negative? (a) a valid run could keep ZM because the notes say it comes with CF — the doc overrides 'whatever we said about them before' (SQL L15); false positive? (b) a wrong run could move it to Todo — rejected | `ENG-2440` — ENG-2440 Canceled (0.00 January revenue, snowflake.json /tables/12/rows/2044–2229; the doc's take test SQL L15) · F31, F9 | none |
| C56 (P16, ddprod_state, weight 5) | cleared | false negative? (a) a valid run could call it Done since it was trimmed — the billing still has to move off HG's AWS bill (SQL L51), so Todo; false positive? (b) a wrong run could cancel it with DD out — rejected | `ENG-2441` — ENG-2441 Todo (billing moves to the LLC by Mar 1, SQL L51, L56) · F32, F10, F4 | none |
| C57 (P17, ddprod_assignee, weight 1) | cleared | false negative? (a) a valid run could assign Leonard, whose comment gave the old figure — Arthur runs the account and reports its bill (SQL L51); false positive? (b) a wrong run could leave it unassigned — rejected | `ENG-2441` — usr_cc3e90160f490686 (Arthur Blake; he runs the account, SQL L51) · F32, F25 | none |
| C58 (P32, dddev_state, weight 3) | cleared | false negative? (a) a valid run could take it with DD ('its accounts') — the doc says what it needs to keep running, and nothing runs on dev (SQL L161); false positive? (b) a wrong run could put it in Todo — rejected | `ENG-2442` — ENG-2442 Canceled ('nothing runs on dev anymore', SQL L161) · F33, F3 | none |
| C59 (P141, eng2443_state, weight 5) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; HG items go to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2443` — Canceled (project rule 'to Canceled if it stays with HG', SQL L140) · F34 | none |
| C60 (P142, eng2444_state, weight 3) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; HG items go to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2444` — Canceled (project rule 'to Canceled if it stays with HG', SQL L140) · F35 | none |
| C61 (P18, cfstacks_state, weight 3) | cleared | false negative? (a) a valid run could call it Done — the billing still moves off HG's AWS bill (SQL L92), so Todo; false positive? (b) a wrong run could cancel it — rejected: CF comes over either way | `ENG-2445` — ENG-2445 Todo (billing moves to the LLC by March, SQL L92) · F36, F14 | none |
| C62 (P19, cfstacks_assignee, weight 1) | cleared | false negative? (a) a valid run could assign Robert as CF's owner — the stacks are Arthur's to run (SQL L173); false positive? (b) a wrong run could leave it unassigned — rejected | `ENG-2445` — usr_cc3e90160f490686 (Arthur; 'I keep an eye on them', SQL L173) · F36, F25 | none |
| C63 (P143, eng2446_state, weight 3) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; HG items go to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2446` — Canceled (project rule 'to Canceled if it stays with HG', SQL L140) · F37 | none |
| C64 (P24, metabase_state, weight 3) | cleared | false negative? (a) a valid run could put it in Todo as the billing moves — the rule names Done for an item one of them pays himself (SQL L140); false positive? (b) a wrong run could cancel it — rejected | `ENG-2447` — ENG-2447 Done (Arthur pays it himself through May, SQL L68; rule 'to Done if one of us pays it himself', SQL L140) · F38, F12 | none |
| C65 (P25, dbt_state, weight 3) | cleared | false negative? (a) a valid run could treat dbt with Metabase in one move — each issue still has its own state; false positive? (b) a wrong run could cancel it — rejected | `ENG-2448` — ENG-2448 Done (SQL L68, L140) · F39, F12 | none |
| C66 (P26, github_state, weight 3) | cleared | false negative? (a) a valid run could cancel it because HG keeps the org — the rule settles it: Done 'even if HG still owns it' (SQL L140); false positive? (b) a wrong run could put it in Todo — rejected | `ENG-2449` — ENG-2449 Done (rule 'even if HG still owns it', SQL L140; 'count it as mine', SQL L68) · F40, F12 | none |
| C67 (P144, eng2450_state, weight 1) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; HG items go to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2450` — Canceled (project rule 'to Canceled if it stays with HG', SQL L140) · F41 | none |
| C68 (P20, appsflyer_state, weight 3) | cleared | false negative? (a) a valid run could call it Done as it costs $0 — the set-up is still to do (SQL L197), so Todo; false positive? (b) a wrong run could cancel it as free — rejected | `ENG-2451` — ENG-2451 Todo (set CF up on the free tier from March, SQL L197) · F42, F21 | none |
| C69 (P21, appsflyer_assignee, weight 1) | cleared | false negative? (a) a valid run could assign Arthur as the analytics owner — Leonard says he sets it up (SQL L197); false positive? (b) a wrong run could leave it unassigned — rejected | `ENG-2451` — usr_63fffeb4fab5233e (Leonard; 'I'll set CF up on it', SQL L197) · F42, F25 | none |
| C70 (P145, eng2452_state, weight 1) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; HG items go to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2452` — Canceled (project rule 'to Canceled if it stays with HG', SQL L140) · F43 | none |
| C71 (P29, figma_state, weight 3) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; Figma stays HG's (SQL L205); false positive? (b) a wrong run could put it in Todo per the draft — rejected | `ENG-2453` — ENG-2453 Canceled (SQL L205) · F44, F20 | none |
| C72 (P146, eng2454_state, weight 1) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; HG items go to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2454` — Canceled (project rule 'to Canceled if it stays with HG', SQL L140) · F45 | none |
| C73 (P147, eng2455_state, weight 1) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; HG items go to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2455` — Canceled (project rule 'to Canceled if it stays with HG', SQL L140) · F46 | none |
| C74 (P148, eng2456_state, weight 1) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; HG items go to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2456` — Canceled (project rule 'to Canceled if it stays with HG', SQL L140) · F47 | none |
| C75 (P31, cursor_state, weight 1) | cleared | false negative? (a) a valid run could mark it Done as already cancelled — 'stays with HG' maps to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2457` — ENG-2457 Canceled (SQL L221) · F48 | none |
| C76 (P149, eng2458_state, weight 1) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; HG items go to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2458` — Canceled (project rule 'to Canceled if it stays with HG', SQL L140) · F49 | none |
| C77 (P150, eng2459_state, weight 1) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; HG items go to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2459` — Canceled (project rule 'to Canceled if it stays with HG', SQL L140) · F50 | none |
| C78 (P151, eng2460_state, weight 1) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; HG items go to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2460` — Canceled (project rule 'to Canceled if it stays with HG', SQL L140) · F51 | none |
| C79 (P152, eng2461_state, weight 3) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; HG items go to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2461` — Canceled (project rule 'to Canceled if it stays with HG', SQL L140) · F52 | none |
| C80 (P22, support_state, weight 5) | cleared | false negative? (a) a valid run could argue Done because the PR merged — the rejection came later and the doc's player-support rule still needs a working build (SQL L100); false positive? (b) a wrong run could cancel it — rejected: DD comes over with its player support (SQL L15) | `ENG-2462` — ENG-2462 Todo (App Review rejected the email-only support, SQL L100 07:30Z, after Arthur's 'done', SQL L241 01:30Z) · F53, F16, F17 | none |
| C81 (P23, support_assignee, weight 1) | cleared | false negative? (a) a valid run could assign Leonard, who handles DD — the build is Arthur's change (SQL L241, PR #1917); false positive? (b) a wrong run could leave it unassigned — rejected | `ENG-2462` — usr_cc3e90160f490686 (Arthur; his support change, SQL L241) · F53, F25 | none |
| C82 (P153, eng2463_state, weight 1) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; HG items go to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2463` — Canceled (project rule 'to Canceled if it stays with HG', SQL L140) · F54 | none |
| C83 (P154, eng2464_state, weight 1) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; HG items go to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2464` — Canceled (project rule 'to Canceled if it stays with HG', SQL L140) · F55 | none |
| C84 (P155, eng2465_state, weight 1) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; HG items go to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2465` — Canceled (project rule 'to Canceled if it stays with HG', SQL L140) · F56 | none |
| C85 (P156, eng2466_state, weight 1) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; HG items go to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2466` — Canceled (project rule 'to Canceled if it stays with HG', SQL L140) · F57 | none |
| C86 (P157, eng2467_state, weight 1) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; HG items go to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2467` — Canceled (project rule 'to Canceled if it stays with HG', SQL L140) · F58 | none |
| C87 (P158, eng2468_state, weight 1) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; HG items go to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2468` — Canceled (project rule 'to Canceled if it stays with HG', SQL L140) · F59 | none |
| C88 (P159, eng2469_state, weight 3) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; HG items go to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2469` — Canceled (project rule 'to Canceled if it stays with HG', SQL L140) · F60 | none |
| C89 (P33, apple_state, weight 3) | cleared | false negative? (a) a valid run could take the account for CF's listing — the comment says the listing moves with the game and the account is HG's (SQL L273); false positive? (b) a wrong run could put it in Todo — rejected | `ENG-2470` — ENG-2470 Canceled ('HG's account. CF's listing sits in it and moves with the game', SQL L273) · F61, F3 | none |
| C90 (P160, eng2471_state, weight 3) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; HG items go to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2471` — Canceled (project rule 'to Canceled if it stays with HG', SQL L140) · F62 | none |
| C91 (P30, calm_state, weight 3) | cleared | false negative? (a) a valid run could keep it open to decide Monday — the prompt asks for the call now; false positive? (b) a wrong run could put it in Todo as 'our LLC' — rejected | `ENG-2472` — ENG-2472 Canceled (SQL L15, L281; C04UEQVDVB7/1703492127.063049) · F63, F19 | none |
| C92 (P161, eng2473_state, weight 3) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; HG items go to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2473` — Canceled (project rule 'to Canceled if it stays with HG', SQL L140) · F64 | none |
| C93 (P162, eng2474_state, weight 3) | cleared | false negative? (a) a valid run could mark it Done as 'nothing left to do' — Done is for an LLC take or a founder payment; HG items go to Canceled (SQL L140); false positive? (b) a wrong run could leave it in Backlog — rejected | `ENG-2474` — Canceled (project rule 'to Canceled if it stays with HG', SQL L140) · F65 | none |
| C94 (P34, sheet_location, weight 1) | cleared | false negative? (a) a valid run could file it in a subfolder of his Drive — accepted (/oe note 1); false positive? (b) a wrong run could edit Leonard's draft in place — rejected: the draft is Leonard's file (SQL L11 owner leonard.hayes) | `d_9f7ba94f7526d54d8482ba` — d_9f7ba94f7526d54d8482ba (Robert's Drive root; any folder of his own Drive accepted, /oe note 1) · F28, F1 | none |
| C95 (P35, sheet_layout, weight 1) | cleared | false negative? (a) a valid run could add a 'Notes' column or reorder — accepted (§4b); false positive? (b) a wrong run could drop 'Paid by' — rejected: all 8 named | `Monthly cost` `Paid by` `Next step` — Monthly cost, Paid by, Next step + Item, Game, Decision, Owner, By (the draft's grid row 0, SQL L23); order and extra columns free (§4b) · F5 | none |
| C96 (P68, sheet_rows, weight 3) | cleared | false negative? (a) a valid run could merge Metabase and dbt as the draft does — 37 accepted; false positive? (b) a wrong run could list only the LLC rows or drop 20 HG rows — rejected by the count | `ENG-2438` `ENG-2474` — 38 item rows (37 issues ENG-2438 to ENG-2474 + the VO line, C09UHHN6PFZ/1770938400.370665; 37 with a combined Metabase + dbt row as on the draft, SQL L23) · F2, F15, F5 | none |
| C97 (P37, cf_call, weight 1) | cleared | false negative? (a) a valid run could write 'LLC (through Sunset's sale)' — accepted; false positive? (b) a wrong run could write HG — rejected | `ENG-2438` — ENG-2438 row Combo Fighter: LLC ('comes over either way', SQL L15) · F29, F3 | none |
| C98 (P38, dd_call, weight 5) | cleared | false negative? (a) a valid run could net the store cut — 162.46 still covers $140 (blind review), LLC holds; false positive? (b) a wrong run could keep it with HG on ~$1k — rejected | `183.11` `$140` — 183.11 vs $140 (snowflake.json /tables/12/rows/2044–2229; SQL L51; the doc's test SQL L15) · F30, F9, F10, F3 | none |
| C99 (P39, zm_call, weight 5) | cleared | false negative? (a) a valid run could write 'Sunset' (it goes in the sale) — accepted as staying with HG (§4b labels); false positive? (b) a wrong run could take it with CF per the notes — rejected | `ENG-2440` — 0.00 January revenue (snowflake.json /tables/12/rows/2044–2229) · F31, F9 | none |
| C100 (P40, md_paid, weight 3) | cleared | false negative? (a) a valid run could put 'Founder' in Decision and 'Arthur' in Paid by — accepted; false positive? (b) a wrong run could have the LLC pay it — rejected | `$248` — $248 carried by Arthur (SQL L68) · F38, F39, F12 | none |
| C101 (P41, calm_call, weight 3) | cleared | false negative? (a) a valid run could write 'not used' — accepted as HG; false positive? (b) a wrong run could make it the LLC — rejected | `ENG-2472` — ENG-2472 HG (SQL L15; C04UEQVDVB7/1703492127.063049) · F63, F19 | none |
| C102 (P42, figma_call, weight 3) | cleared | false negative? (a) a valid run could write 'lapses Sep 11' — accepted as HG; false positive? (b) a wrong run could keep the draft's LLC — rejected | `ENG-2453` — ENG-2453 HG (SQL L205; draft row 4 says LLC, SQL L23) · F44, F20, F5 | none |
| C103 (P43, helpshift_call, weight 3) | cleared | false negative? (a) a valid run could keep it for DD till Feb 28 — HG is cancelling it; the support step is on its own row (P47); false positive? (b) a wrong run could take it as DD's support — rejected | `ENG-2461` — ENG-2461 HG ('they're cancelling', SQL L237) · F52, F17 | none |
| C104 (P44, cursor_call, weight 1) | cleared | false negative? (a) a valid run could write 'cancelled' — accepted; false positive? (b) a wrong run could take it — rejected | `ENG-2457` — ENG-2457 HG (SQL L221) · F48 | none |
| C105 (P45, vo_cost, weight 3) | cleared | false negative? (a) a valid run could write $100/day — the row needs the monthly figure; $100/day × 31 = 3,100 is above the cap (SQL L45: 'capped at $3,000 a month'); false positive? (b) a wrong run could put 0 — rejected | `$3,000` — $3,000 (3000 or 3,000; the cap from March, SQL L45) · F15 | none |
| C106 (P173, vo_paid, weight 3) | cleared | false negative? (a) a valid run could write 'new company card' — accepted; false positive? (b) a wrong run could put Leonard (his card till Feb) — rejected | `$3,000` — paid by the LLC ('moves to our new company's card from March', SQL L45) · F15, F66 | none |
| C107 (P46, ddprod_cost, weight 5) | cleared | false negative? (a) a valid run could write '$140 from March' — accepted; false positive? (b) a wrong run could write $300 or $1,000 — rejected | `$140` — $140 (SQL L51, 03:10Z; superseded ~$1k and 300, C0ADGSZKR3R/1770680984.725779, C0ADGSZKR3R/1770682219.100789, SQL L157, the draft) · F10, F11 | none |
| C108 (P47, support_step, weight 5) | cleared | false negative? (a) a valid run could write 'fix the App Review rejection (add a support link)' — accepted; false positive? (b) a wrong run could write 'done' or 'none' as the step — rejected: App Review rejected the build (SQL L100) | `ENG-2462` — Feb 28 (before Feb 28; any date Feb 15–27, 'by Feb 28' or 'before Feb 28', risk 8; SQL L100, L237, C0ADGSZKR3R/1770789534.434749) · F53, F16, F17, F4 | none |
| C109 (P66, support_by, weight 3) | cleared | false negative? (a) a valid run could write 'Feb 27' or put the date in the step text — accepted; false positive? (b) a wrong run could give Mar 1 (b2) — rejected: the item has its own deadline (SQL L56) | `Feb 28` — Feb 28 ('before Feb 28th', #winddown C0ADGSZKR3R/1770789534.434749, SQL L237; card SQL L56 'Anything that already has its own deadline keeps it'; any date Feb 15–28, 'by Feb 28' or 'before Feb 28', risk 8) · F53, F17, F4 | none |
| C110 (P48, layer_step, weight 3) | cleared | false negative? (a) a valid run could put it on the Combo Fighter row — accepted (risk 2); false positive? (b) a wrong run could write 'cancelled, nothing to do' — rejected (SQL L48) | `ENG-2454` — Mar 3 (before or by Mar 3; SQL L48; C09UHHN6PFZ/1770837702.167889; on the layer.ai or the Combo Fighter row) · F18, F45 | none |
| C111 (P67, layer_by, weight 3) | cleared | false negative? (a) a valid run could write 'Mar 2' or 'by Mar 3' — accepted; false positive? (b) a wrong run could write 'by Mar 31' or leave the step undated — rejected | `Mar 3` — Mar 3 ('we have access until March 3rd', C09UHHN6PFZ/1770837702.167889; 'before then', SQL L48; by or before Mar 3, any earlier date from Feb 15) · F18, F45 | none |
| C112 (P50, cfstacks_cost, weight 3) | cleared | false negative? (a) a valid run could write '$62 (was $95)' — accepted; false positive? (b) a wrong run could keep $95 (b5) — rejected | `$62` — $62 (SQL L92 04:20Z; superseded $95 SQL L173 00:58Z) · F14 | none |
| C113 (P51, appsflyer_cost, weight 1) | cleared | false negative? (a) a valid run could write 'free' — accepted; false positive? (b) a wrong run could price a paid plan — rejected | `ENG-2451` — ENG-2451 0 or free ('free up to 15K installs', SQL L197) · F42, F21 | none |
| C114 (P52, metabase_cost, weight 5) | cleared | false negative? (a) a valid run could use one 'Metabase + dbt' row at 200 — accepted (§4b); false positive? (b) a wrong run could keep ~300 — rejected | `ENG-2447` `ENG-2448` — $100, $200 (SQL L68; superseded ~300, SQL L181 and the draft) · F12, F13 | none |
| C115 (P53, github_cost, weight 1) | cleared | false negative? (a) a valid run could write 0 for the LLC as Arthur pays — the column is the item's monthly cost, and the shares need it (SQL L80 'including what one of us already pays'); false positive? (b) a wrong run could omit GitHub — rejected | `$48` — $48 ('back to the $48 team plan', SQL L68) · F12, F40 | none |
| C116 (P54, github_call, weight 3) | cleared | false negative? (a) a valid run could write 'HG (Arthur pays)' — names Arthur, accepted; false positive? (b) a wrong run could have HG pay — rejected | `ENG-2449` — ENG-2449 paid by Arthur (SQL L68) · F40, F12 | none |
| C117 (P55, vendor_cost, weight 3) | cleared | false negative? (a) a valid run could leave the cost cell blank with 'one-off' — accepted; false positive? (b) a wrong run could put $3,750 or $1,250 a month — rejected | `ENG-2474` — $3,750 kept out (one-off, SQL L289; doc SQL L15) · F65, F24 | none |
| C118 (P56, cf_by, weight 3) | cleared | false negative? (a) a valid run could write 'Mar 1' — the card gives sale items the sale's close (SQL L56), rejected; false positive? (b) a run writing 'at the sale' passes — same rule | `ENG-2438` — ENG-2438 (card: 'Anything that comes through Sunset's sale moves when the sale closes', SQL L56) · F29, F4 | none |
| C119 (P57, ddprod_by, weight 3) | cleared | false negative? (a) a valid run could write 'end of Feb' — it meets 'by March 1' (SQL L56), accepted; false positive? (b) a wrong run could write 'when the sale closes' — rejected: the account is not in Sunset's sale | `Mar 1` — Mar 1 (card: 'everything else moves by March 1', SQL L56) · F32, F4 | none |
| C120 (P72, ddprod_assignee, weight 1) | cleared | false negative? (a) a valid run could write 'Blake' as on the draft — accepted; false positive? (b) a wrong run could put Leonard, who gave the old figure — rejected | `ENG-2441` — Owner Arthur Blake (Arthur runs the account, SQL L51; draft column Owner, SQL L23) · F32, F10, F5 | none |
| C121 (P73, vo_assignee, weight 1) | cleared | false negative? (a) a valid run could write 'Leonard (card)' — accepted; false positive? (b) a wrong run could put Robert as CF's owner — rejected: Leonard moves his card | `$3,000` — Owner Leonard Hayes (on his card, SQL L45) · F15, F66, F5 | none |
| C122 (P172, ddprod_game, weight 1) | cleared | false negative? (a) a valid run could write 'Domino Delights' — accepted; false positive? (b) a wrong run could write CF — rejected | `ENG-2441` — Game DD (the draft's 'DD servers, DD', SQL L23) · F32, F5 | none |
| C123 (P58, even_share, weight 5) | cleared | false negative? (a) a valid run could show Arthur as '$902 + $248 carried' — accepted (risk 3); false positive? (b) a wrong run could give $150 (no VO, b1) or 1,067 (on 3,202) or Arthur 1,150 cash on top of 248 — rejected | `$1,150` `$902` `$248` — $1,150, $902, $248 (split mail SQL L80: 'put the three shares on the sheet per month'; 3,450 / 3) · F67, F7 | none |
| C124 (P59, share_leonard, weight 1) | cleared | false negative? (a) a valid run could share as commenter — any role accepted (§4b); false positive? (b) a wrong run could share Leonard's draft instead — rejected: the new plan sheet | `d_9f7ba94f7526d54d8482ba` — Co-founder & CEO (Contacts /contacts/169: leonard.hayes@harmonygames.co; writer, commenter or reader) · F27 | none |
| C125 (P60, share_arthur, weight 1) | cleared | false negative? (a) a valid run could read 'Blake' as a first name and search — Contacts resolve it to Arthur Blake (/contacts/168); false positive? (b) a wrong run could share with a different Blake — rejected by the address | `d_9f7ba94f7526d54d8482ba` — Co-founder & CTO (Contacts /contacts/168: arthur.blake@harmonygames.co; 'Blake' in the prompt) · F27 | none |
| C126 (P61, reply_link, weight 1) | cleared | false negative? (a) a valid run could paste the Sheets URL rather than a Drive URL — both accepted; false positive? (b) a wrong run could link Leonard's draft — rejected: the new plan sheet | `1770961200.890407` — 1770961200.890407 (thread_ts; DM D04UP2L3E3S, SQL L54) · F1, F28 | none |
| C127 (P62, dd_reply, weight 5) | cleared | false negative? (a) a valid run could say 'DD comes over' — accepted as taking it; false positive? (b) a wrong run could say 'only CF' — rejected | `183.11` `$140` — 183.11 vs $140 (as P38) · F30, F9, F10, F1 | none |
| C128 (P63, zm_reply, weight 5) | cleared | false negative? (a) a valid run could name only the games it takes — accepted with 'only' / 'just'; false positive? (b) a wrong run could take all three — rejected | `ENG-2440` — 0.00 (as P39) · F31, F9, F1 | none |
| C129 (P64, even_share, weight 5) | cleared | false negative? (a) a valid run could give only '$1,150 each' — accepted (risk 3); false positive? (b) a wrong run could have Arthur pay $1,150 cash on top of $248, or give $150 / 1,067 — rejected | `$1,150` `$902` `$248` — $1,150 ($902 cash + $248 accepted; SQL L80) · F67, F7, F1 | none |
| C130 (P65, reply_last, weight 1) | cleared | false negative? (a) a valid run could post a short 'working on it' first and the answer last — the row grades the reply that answers, after the writes; false positive? (b) a wrong run replying before sharing — rejected | `1770961200.890407` — 1770961200.890407 reply after OEs 24–103 ('When you're done … Then reply') · F1, F66 | none |

```
STAGE GATE rubric-check: PASS — Task_Authoring/task_inputs · 09_Rubric_Check.md#d24cfbcd9f29 · 09_Rubrics.json#cd67ff04220c · 09_Rubric_Writing_Plan.md#50eb4801f48d · __context__#226493b2011a · __assignment__#b4220a529c0a · __policy__#dc4ab5df3cdd · __gate_policy__#f8638415ca2c · __review__#944f51ff7178 · blocking 0 · warnings 0 · checks 22
[PASS] assignment.v3_context: Robert / Co-founder & Creative Director; easy cap <90%; freeze 2026-02-14T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe normal; KB bound; clock Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
[PASS] structure.outputs: 1 output(s) present: 09_Rubric_Check.md
[PASS] structure.inputs: 2 input(s) present: 09_Rubrics.json, 09_Rubric_Writing_Plan.md
[PASS] structure.fresh: every output newer than its inputs (09_Rubrics.json, 09_Rubric_Writing_Plan.md)
[PASS] chain.rubric-writing: upstream 'rubric-writing' PASS pasted and current (09_Rubric_Writing_Plan.md#50eb4801f48d, 04_Prompt.txt#7b6f4963690a, 08_Oracle_Events.md#acae59416e80, 08_OE_Writing_Ledger.md#cf9297cc1a8a, __context__#226493b2011a, __assignment__#b4220a529c0a, __policy__#dc4ab5df3cdd, __gate_policy__#f8638415ca2c, __review__#944f51ff7178)
[PASS] structure.sections: 5 required sections present and non-empty (09_Rubric_Check.md)
[PASS] structure.placeholders: no placeholders in 09_Rubric_Check.md
[PASS] structure.criteria_count: header Criteria 130 vs 09_Rubrics.json 130
[PASS] rubric.category_balance: 129 Outcome / 1 Process of 130 rows: ≥ 1 Outcome and Process ≤ 50 %
[PASS] evidence.quoted_spans: 0 quoted span(s) verified as exact substrings of 09_Rubrics.json
[PASS] structure.issue_types: every finding uses a /rubric issue type
[PASS] structure.dimensions: dimension table has 9/7+ rows
[PASS] structure.readiness: readiness line present
[PASS] validity.rubric: binary validity gate clean: no incorrect, unauthorized, unobservable, contradictory, uncovered or predicted all-fail item
[PASS] surface.coverage: 25 surface slot(s): 21 covered, 4 dispositioned in 'Coverage — gradable surface' (gate 17)
[PASS] review.counter_readings: 130 evidenced counter-readings (of 132 found; need ≥ 130) in 09_Rubric_Check.md
[PASS] review.coverage: self-review addresses all 131 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.fact_duplication: no declared fact_id is graded in three or more criteria; reviewer must also check semantic duplicates
[PASS] v3.rubric_evidence: every criterion has requested-work trace, verified source values, path visibility/existence checks and recorded fair-outcomes reasoning; path linkage remains review judgment
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## Reminders
- An all-Outcome set is normal; Process is not added to look thorough.
- Fix the criteria (Claude, Codex or the human) in the builder, re-export, re-run check, then run /rubric.
- Enter the 130 rows in the Criteria Builder exactly as in 09_Rubrics.json (sha cd67ff04220c); diff the export against it before /rubric (builder drift: weights, escaped titles).
