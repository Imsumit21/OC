# 09 Rubric Check — julia-zm-audience-call (cards earlier audience read, injection rev9)
Checked 2026-11-10 · Criteria 38 (builder minimum 5: ok) · Plan 2026-11-09 (09_Rubric_Writing_Plan.md, P1–P38 map 1:1 to C1–C38)
Clock 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) · Persona Julia Lawson julia.lawson@harmonygames.co · Mode Medium · OE 08_Oracle_Events.md rev4 (/oe PASS 5; OE 24, 33–37, 41–53, 97, 98 optional, not graded)
JSON field map: criterion=`title` · weight=`weight` · category=`category` · justification=`justification` · evidence=`evidence` · schema gate: pass (38 rows, five non-blank fields each, category Outcome, weights in 1/3/5)
Readiness for /rubric: CLEAN — a prediction only; /rubric gives the verdict. Every finding below was fixed in 09_Rubrics.json this session (rubric sha256 ae4bad5e3ba3…); the residual judgment risks are listed under Self-review and none reaches a FAIL band. The stage gate still fails on upstream items outside this stage (chain.rubric-writing via the plan's own failing gate, readiness.evidence); see Self-review.

Lint: `python3 Task_Authoring/tools/hg.py rubric-lint Task_Authoring/task_inputs/09_Rubrics.json` → `{"findings": [], "count": 0}` on the input and again after every edit (0 disguised_negative, format_lock, anon_token, evidence_no_record, vague_exemplar, tool_name, prohibition_title or schema hits).

## Coverage
| Plan row / requirement | Criteria | Covered / gap (omission + wrong-result test) |
|---|---|---|
| "fill in the register tab in my audience sessions workbook": rows, one per session (P1) | C1 | covered: no rows fails; 80 rows (Owen's late two left out, T11) or 84 (duplicates) fails |
| Register verdict volume (P2) | C2 | covered: no verdicts fails; 58 counted (coaching and contacts missed) or 32 fails |
| Register reason volumes by rule (P3, P6, P9) | C3, C6, C9 | covered: no reasons fails; 0 coached (run-4, run-5), 9 game-industry (run-1) fails |
| Register exception verdicts (P4, P7, P10, P12–P15) | C4, C7, C10, C12, C13, C14, C15 | covered: each names its ticket and the verdict; the opposite verdict fails |
| Register reasons, one sample per rule (P5, P8, P11) | C5, C8, C11 | covered: a reason naming another rule, or a counted verdict, fails |
| Owen Baker's late sessions in the read (P16, P17) | C16, C17 | covered: no row, or a not-counted row, fails |
| Routine counted samples (P18–P20) | C18, C19, C20 | covered: a not-counted verdict fails |
| "write the memo he asked for" / "put it in my drive folder" (P21) | C21 | covered: no memo, or a memo outside d_8140f09bf9f1b94cb8ee2d, fails |
| Memo contents set by the card SQL L859: the call (P22) | C22 | covered: no memo, RPG lead or no clear lead fails |
| Memo: the numbers behind the call (P23, P24) | C23, C24 | covered: 3.77 over 28 (run-1), 3.67 over 18 (run-4), 4.11 or 4.18 fails |
| Memo: panel and retention as context (P25, P26) | C25, C26 | covered: 3.10 or a 3 to 3.5 range (run-4) fails; 10.4% (run-3), 9.1% (run-5), 8.63% or a range (run-6) fails |
| "close out the session tickets": state volumes (P27, P28) | C27, C28 | covered: no updates fails; 35 Canceled / 45 Done (run-1) or 13 / 67 (run-5) fails |
| Close-out exceptions and one sample (P29–P34) | C29, C30, C31, C32, C33, C34 | covered: Todo or the opposite state fails |
| "reply to him in his thread with keep or hold" (P35, P36) | C35, C36 | covered: no reply, a DM or a top-level post fails C35; keep (run-1, run-4, run-5) or a maybe fails C36 |
| "tell brian in #zombie-design whether the tutorial and level order work goes on" (P37, P38) | C37, C38 | covered: a DM or no post fails C37; goes on (run-1, run-4, run-5) fails C38 |
| "post and update everything under my name" | every write row | covered: all graded writes are Julia's own (no row grades another actor) |
| Told facts in the final reply | none asked | covered: the prompt asks Julia to be told nothing, so no reply row (final-reply test below) |
Unauthorized criteria: none. No row grades re-run notes, new tickets for Owen's sessions, their Log rows or closing them (OE 24, 33–37, 41–53, 97, 98 optional; binding requirement-authority ruling in the plan header).
OE cross-check (both ways): every C-n maps to the verbatim OE steps in plan §A3 (C1↔OE 10, 11, 14, 15, 38 … C38↔OE 1, 3, 32, 137); every graded write OE (38, 39, 40, 54–96, 99–135, 136, 137) maps to a C-n; no row fails an Agent following the OE (the /oe notes on the memo's end location, either retention source, either key form in Owen's rows and reply timing are honoured in C21, C26, C16, C17, C35). Conflicts: none.
Final-reply test: "Done. Register filled (82 sessions, 45 counted), memo in your folder, 43 tickets Done and 37 Canceled, replied hold in Leonard's thread and told Brian the tutorial and level order work does not go on." → ACCEPT (no row grades the final reply).

## Coverage — gradable surface
| Surface slot | Stable fact ID | Criteria | Covered / dispositioned / gap | Disposition reason (evidence) |
|---|---|---|---|---|
| S-K1a | verdict:K1 | C4 | covered | — |
| S-K1b | reason:K1 | C5 | covered | — |
| S-K3a | verdict:K3:588 | C12 | covered | — |
| S-K3b | verdict:K3:641 | C13 | covered | — |
| S-K4a | verdict:K4 | C7 | covered | — |
| S-K4b | reason:K4 | C8 | covered | — |
| S-K5a | verdict:K5 | C10 | covered | — |
| S-K5b | reason:K5 | C11 | covered | — |
| S-Ga | verdict:G:622 | C14 | covered | — |
| S-Gb | verdict:G:598 | C15 | covered | — |
| S-Ta | late:T1 | — | dispositioned | not incorporated: a new ticket for Owen Baker's late casual session rests only on the log note's late-form line (SQL L176), which nothing the prompt incorporates asks for; /oe rev4 marks OE 33, 35, 37, 97 optional (gate 3). The session itself is graded on the Register in C16 and inside C1, C2, C23 |
| S-Tb | late:T2 | — | dispositioned | not incorporated: as S-Ta for Owen Baker's late RPG session (OE 34, 36, 37, 98 optional; SQL L176). The session itself is graded in C17 and inside C1, C2, C24 |
| S-H1 | audience_lead | C22 | covered | — |
| S-G1 | counted_total | C2 | covered | — |
| S-G2 | means | C23, C24 | covered | — |
| S-DEC | decision_reply | C36 | covered | — |
| S-BRIAN | decision_brian | C38 | covered | — |
| S-ST1 | state_canceled | C27 | covered | — |
| S-ST2 | state_done | C28 | covered | — |
| S-F1 | rerun | — | dispositioned | not incorporated: re-run notes rest only on Robert's DM (SQL L885); neither the prompt, Leonard's ask (SQL L889) nor the card (SQL L859) asks for them; /oe rev4 marks OE 24 and OE 41–53 optional (gate 3) |
| S-D1 | panel | C25 | covered | — |
| S-E1 | retention | C26 | covered | — |
| S-O1 | verdict:ZOM-643 | C18 | covered | — |
| S-O2 | verdict:ZOM-605 | C19 | covered | — |
| S-M1 | memo_exists | C21 | covered | — |
| S-L1 | reply_thread | C35 | covered | — |
Slots 26 · covered 23 · dispositioned 3 (S-Ta, S-Tb, S-F1).
Mechanism share: 57% of the criteria weight (92 of 162: C2, C4, C5, C7, C8, C10, C11, C12, C13, C14, C15, C22, C23, C24, C25, C26, C27, C28, C36, C38), reported, not gated.

## Findings
Every finding was fixed in 09_Rubrics.json this session; the quoted span is the current (fixed) text so it can be located.
| # | Criterion | Quoted span | Rule (source §) | What is wrong | Plan row / ledger fact | `/rubric` type | Severity |
|---|---|---|---|---|---|---|---|
| 1 | C16 | "the player's name need not appear, since the Register has no player column (Ayşe Polat or Ayse Polat both pass where it does)" | Eval 2.1 / 2.7 pattern 4 (supporting field narrower than the title) | Before: evidence read Accept: Ayşe Polat or Ayse Polat, counted. The Register header is ticket / audience / stars / verdict / reason (SQL L342), so no run writes the player's name: all six baseline rows for ZOM-648 omit it (run-1 to run-6). A judge following the evidence fails every valid run, an invalid all-fail. Fixed: acceptance is a counted casual 5-star row beyond ZOM-568 to ZOM-647 keyed by a new ZOM key or a mail pointer; the name is optional | P16 · F19, F117 | overly_specific | Major (fixed) |
| 2 | C3 | "The Agent gives coaching as the reason on exactly 13 excluded rows of the Register tab of 'ZM audience sessions'" | Eval 2.2; playbook gate 15 (no bundled exact-set row; Rubric Writing §7) | Before: the volume title also listed its members (Claire Morgan's Fri Sep 26 sessions, ZOM-607 to ZOM-619), so the count row asserted 13 memberships as well. Fixed: the title grades the count; the members stay in evidence as verification guidance | P3 · F20, F7 | non_atomic | Major (fixed) |
| 3 | C6 | "The Agent gives working in games as the reason on exactly 11 excluded rows of the Register tab of 'ZM audience sessions'" | Eval 2.2; gate 15 | Before: the title listed ZOM-568 to ZOM-576, ZOM-598 and ZOM-622 beside the count (11 memberships). Fixed as finding 2 | P6 · F21, F23, F5 | non_atomic | Major (fixed) |
| 4 | C9 | "The Agent gives build 1943 or a dev (non-store) build as the reason on exactly 13 excluded rows" | Eval 2.2; gate 15; Eval 2.1 (supporting field wider than the title) | Before: the title listed ZOM-577 to ZOM-586, ZOM-632, ZOM-637 and ZOM-645 and named only build 0.3.127 (1943), while the evidence also accepted dev build or non-store build. Fixed: count only, and the title states every accepted reason wording | P9 · F22, F8, F17 | non_atomic | Major (fixed) |
| 5 | C27, C28 | "37 is the not-counted set left after the coaching, game-industry and build 1943 rules are applied" | Eval 2.12 (QC C18–C20); playbook gate 15 (a volume row whose count only the full audit produces is multi-source, 5) | Before: weight 3 with Interpretation: the count follows the verdicts. The 37 / 43 split exists only after the full audit across tickets, notes docs, contacts, mail, Slack and the QA matrix, the same work C2 carries at 5. Fixed: weight 5, Multi-source justification | P27, P28 · F11, F119 | — | Criteria Weights (fixed) |
| 6 | C29, C30, C31, C32, C33 | "Multi-source: ZOM-610's ticket and form say no coaching" | Eval 2.12; sibling consistency (the Register verdict rows C4, C7, C10, C12, C15 decide the same traced records at 5) | Before: weight 3, Interpretation. Each state is decided only by the trap's cross-service trace (Gmail, Slack DM, notes doc, QA matrix, contacts) plus the log note: the justification itself listed three or more sources. Fixed: weight 5, Multi-source justifications naming the sources | P29–P33 · F20, F21, F22, F25, F23, F11 | — | Criteria Weights (fixed) |
| 7 | C5, C8, C11 | "Multi-source: ZOM-613's ticket and Claire's form say no coaching" | Eval 2.12; sibling consistency with C4, C7, C10 | Before: weight 3, Interpretation. The reason for each sampled session comes only from the cross-service join the verdict needs (Claire's mail to the ticket by observer and date; Brian's Turkish DM to the notes doc relation; the notes doc build to Leonard's 1943 reply). Fixed: weight 5, Multi-source justifications. With finding 6, 10 of 38 rows (26%) were one level light, a Criteria Weights FAIL | P5, P8, P11 · F20, F21, F22 | — | Criteria Weights (fixed) |
| 8 | C25, C26 | "Interpretation: Leonard's rule takes a void rating out of the sum and the count" | Task style (weight 3 justification opens with Interpretation: or Comparison:) | Before: both justifications opened with None: Calculation:, a template remnant. Fixed: Interpretation: plus the calculation | P25, P26 | — | note (fixed) |
| 9 | C1 | "exactly 82 session rows under its header (the 80 ticketed sessions plus Owen Baker's two Sun Sep 28 sessions)" | gate 15 (consistency with findings 2–4) | Before: the population scope named the key range ZOM-568 to ZOM-647. The two operands (80 ticketed, Owen's 2) define the count and stay; the key range moved out of the title (it is in evidence) | P1 · F14, F15, F19 | harmless_specificity | Minor (fixed) |

## Overlap groups · Spot-check groups · Predicted all-fail
| Group / row | Members / basis | Shared condition / reason |
|---|---|---|
| Overlap groups | none | Checked: C27 and C28 are not one group (a run that leaves tickets in Todo passes one and fails the other, so removing either changes the score; Eval 3.3). C22, C36, C38, C23, C24 share a likely root cause (a wrong lead), not an embedded acceptance condition, and grade different deliverables (Eval 3.3 "merely share a likely model root cause"). C15 and C33 grade one session on two prompt-required deliverables (Register and Linear), two rows, under the V3 three-row limit |
| Spot-check D1 Register verdicts (82) | volume C1, C2; direct exception rows C4, C7, C10, C12, C13, C14, C15, C16, C17; samples C18 (ordinary Pixel 8a), C19 (edge: same day as the coached gathering), C20 (edge: family relation, same observer as the 1943 drop ZOM-645) | 3 samples (≤ 5) |
| Spot-check D2 Register reasons (37) | volume C3, C6, C9 (one per rule); samples C5, C8, C11 | 3 samples (≤ 5) |
| Spot-check D3 ticket close-out (80) | volume C27, C28; direct exception rows C29, C30, C31, C32, C33; sample C34 (edge: store build from Douglas, who also ran 1943 sessions) | 1 sample (≤ 5) |
| Predicted all-fail | none (0 rows) | Every value re-read this session through hg.py and the SQL; every scoped record is persona-visible (plan §E check-sql PASS); every graded write is cataloged; Friction: none. Baseline cross-check: run-2 passes all 38 rows on its decoded writes. The pre-fix C16 evidence was the only row that could have failed every run; fixed (finding 1) |

## Dimensions
| Dimension | Count / % | Threshold | Status |
|---|---|---|---|
| Overall Rubric Quality | 0 Major, 0 Moderate, 0 Minor after fixes (pre-fix: 4 Major rows C3, C6, C9, C16 and 1 Minor C1) | any Major or Moderate fails; Minor < 5% (2 rows of 38) passes | PASS (predicted) |
| Criteria Weights | 0 rows off after fixes (pre-fix: 10 of 38 = 26% one level light) | ≤ 10% one level off is NON-FAIL 4; margin: up to 3 rows | PASS (predicted; residual: C36, C38 could be read as 5, 2 of 38 = 5.3%, NON-FAIL 4 at worst) |
| Known data issue | 0 rows on a synthcut card (no card covers USER_COHORT_RETENTION, the Register, Linear session tickets or contacts jobs) | any row on a card fails | PASS |
| Category Balance | 38 Outcome / 0 Process | ≥ 1 Outcome, Process ≤ 50% | PASS |
| Process Rubrics | 0 Process rows; 0 genuine ordering dependencies (the prompt joins the asks with commas and 'and'; plan §C) | any invalid Process row or ≥ 2 missing fails | PASS |
| Agent-Centric Phrasing | 38 of 38 titles open "The Agent" + action; 0 tool names in titles | 1 artifact subject or tool name fails | PASS |
| Negative Criteria | 0 prohibition or absence titles; do_nothing_case REJECT 38 of 38 (plan §A3) | any row an idle Agent passes fails | PASS |
| Predicted all-fail | 0 | tolerance 0 | PASS |
| Schema and other repair gates | schema pass; self-containment, atomicity, accuracy, coverage, duplicates, weights, format-5 cases all pass after fixes; no row pair is jointly unsatisfiable | a failure is reported | PASS |
Threshold margin: one Major or Moderate on any row would fail Overall Rubric Quality; Minor issues may reach 1 row (2.6%) before the 5% line.

Changes made to 09_Rubrics.json (before → after):
- C1 title: "(the 80 tickets ZOM-568 to ZOM-647 plus Owen Baker's two Sun Sep 28 sessions)" → "(the 80 ticketed sessions plus Owen Baker's two Sun Sep 28 sessions)".
- C3 title: "… 'ZM audience sessions' (Claire Morgan's Fri Sep 26 sessions, ZOM-607 to ZOM-619)" → "… 'ZM audience sessions'"; evidence now accepts exactly 13 not-counted rows with a coaching reason and names ZOM-607 to ZOM-619 as guidance ("the row grades the count").
- C6 title: "… (ZOM-568 to ZOM-576, ZOM-598 and ZOM-622)" removed; evidence keeps the members as guidance.
- C9 title: "gives build 0.3.127 (1943) as the reason on exactly 13 excluded rows … (ZOM-577 to ZOM-586, ZOM-632, ZOM-637 and ZOM-645)" → "gives build 1943 or a dev (non-store) build as the reason on exactly 13 excluded rows …"; evidence keeps the members as guidance and adds "never went through a store".
- C5, C8, C11, C27, C28, C29, C30, C31, C32, C33: weight 3 → 5; justification "Interpretation: …" → "Multi-source: …" naming the services each decision draws on.
- C16 evidence: "Accept: Ayşe Polat or Ayse Polat, counted; a missing row fails." → a counted casual 5-star row beyond ZOM-568 to ZOM-647 with a new ZOM key or a pointer to Owen's Sep 30 mail; name optional (no player column); adds contact 5ba38e15d02244b525c4e684 (SQL L1027).
- C17 evidence: same form for the RPG 1.5-star row; adds contact e86229d6ca8ce8078f1acfd0 ('Lawyer', SQL L1029).
- C25, C26 justification: "None: Calculation: …" → "Interpretation: …".
Totals: 38 rows, weight 142 → 162; bands 5 ×17 · 3 ×18 · 1 ×3 → 5 ×27 · 3 ×8 · 1 ×3. Titles still open "The Agent"; no em-dash, "e.g.", "such as", "ensure", "correctly", "appropriate" or curly quote in any field (scripted scan); lint 0 findings.

Failure signatures after the changes (six rev9 baseline rollouts in 07_Baseline_Trajectories, written end states decoded this session from each run's write calls: Register values, memo body, memo parent, Slack posts, final Linear states; graded against the changed rows, then checked by hand where a regex was loose):
| Run | Rows failed | Score (weight 162) |
|---|---|---|
| run-1 | C2, C6, C14, C15, C22, C23, C24, C26, C27, C28, C33, C36, C38 (13) | 63.6% |
| run-2 | none | 100.0% |
| run-3 | C26 | 98.1% |
| run-4 | C3, C4, C5, C12, C13, C22, C23, C24, C25, C26, C29, C32, C36, C38 (14) | 61.7% |
| run-5 | C2, C3, C4, C5, C6, C7, C8, C14, C15, C22, C23, C24, C26, C27, C28, C29, C30, C33, C36, C38 (20) | 42.0% |
| run-6 | C26 | 98.1% |
Failing runs 5; patterns: {run-3, run-6} (retention only), run-1, run-4, run-5; largest pattern 2 of 5 = 40% (≤ 45% target). Pairwise differences between distinct patterns: 7 to 19 rows (≥ 2). Pass/fail per row is identical to the plan's pre-change grading (the edits widened C9, C16 and C17 acceptance only where every run already passed, and moved weights, which do not change pass/fail). Average 77.3% (< 85% Medium cap; plan 77.1%); full passes 1 of 6. Trap blocks keep their own rows: K1 C3, C4, C5, C29; K3 C12, C13, C32; K4 C7, C8, C30; K5 C9, C10, C11, C31; G C14, C15, C33; T C1, C16, C17.

## Self-review
**1. Re-read as /rubric** (Phases 1–5, pre-verdict sweep 5.0): one missing requirement — none (Coverage table; the 21 optional OEs have no row by the binding ruling); one phrasing mismatch with the prompt — none ("keep or hold" and "whether the tutorial and level order work goes on" are the prompt's own words in C36, C38); one non-atomic row — C3, C6, C9 (fixed, findings 2–4); one category mislabel — none (all Outcome, every row an end state); one over-specific requirement — C16 (fixed, finding 1); one duplicate or cascade group — none (Overlap section); one vague exemplar — none (lint and scan); one prohibition-only title — none (lexical pre-scan of the 38 titles found no does not / no / not / never / without / leaves / keeps). Calibrated against `Evals/references/rules/rubric_qc_examples.md` rows on do-nothing, LITERAL keys (ZOM keys, contact ids and Slack ts are cited as records) and BOTH_FAIR_FIGURE (C26 accepts 10.47% or 10.59%, `Evals/task_inputs/reports/1_prompt.md` L236).

**3. Re-verified** this session through `Task_Authoring/tools/hg.py` and the SQL (read, never executed):
- `python3 Task_Authoring/tools/hg.py search search snowflake "zombie_match_3d" --pointer /tables/10/rows` (51 rows, scan_complete) then `get-many` on all 51: cohort weeks from 2025-07-24 with d14_ret, both platforms, 16 rows, 2,607 installs, install-weighted D7 10.4709 (C26); all 47 mature rows 9.0885; Sep 15 cohorts dropped 10.5859. KPI sheet grid SQL L346 from 2025-07-24: 14 rows, 2,267 installs, 10.5859; simple mean 9.91; sheet 'D7 mean' 8.63.
- `hg.py search get gdrive --file data.json --pointer /drive_files/11673` → d_8140f09bf9f1b94cb8ee2d is Julia's root folder (owner julia.lawson@harmonygames.co) (C21); log note parent SQL L6.
- `hg.py search get slack --file messages/C090N54TG79/2025-09.json --pointer /731/text` → Robert's Monday post "<@EMPLOYEE_0026_SLACK_ID> will make the changes in the tutorial" (C37, C38); `users.json /14` → Brian Foster, EMPLOYEE_0026_SLACK_ID.
- SQL string checks: L889 Leonard's ask (thread 1759266627.418203, "casual lead means we hold the change", "reply here with keep or hold"); L877, L879, L881, L883 rules; L871 Brian's DM; L508 Claire's mail; L434 Owen's late reply (Ayşe Polat casual 5, Daniel Hughes RPG 1.5, build 0.3.127 (127)); L1027 Ayşe Polat 'Secondary school teacher'; L1029 Daniel Hughes 'Lawyer'; L967 Alper Koçak 'QA tester, console games publisher'; L1015 Arda Keskin 'Live ops producer, mobile games studio'; L174 gate doc; L176 log note close-out line; L342 Register header; L360 deck lead rule; L366–L368 panel stars (30 over 9 = 3.33; 31 over 10 = 3.10); L856 PR 476 rc_27 "no phone in the loop"; L901 matrix SM-A546E PASS 0.3.127 (127); L530 ZOM-567 "Vision Bot run #15"; L859 card text; ticket rows L532–L690 and comments L692–L850 for every key a title names.
- Independent recomputation from the 80 ticket rows, 80 notes docs and the seeded contacts: not counted 13 coached (ZOM-607 to ZOM-619), 11 game industry (ZOM-568 to ZOM-576, ZOM-598, ZOM-622), 13 build 1943 (ZOM-577 to ZOM-586, ZOM-632, ZOM-637, ZOM-645), no session under two rules; counted 43 tickets + Owen's 2 = 45; casual 27 / 103.5 / 3.8333; RPG 18 / 63.0 / 3.5000; tickets 37 Canceled, 43 Done.

**2 and 5. Counter-readings and fixes, one per criterion**
| Check | Verdict | Strongest counter-reading | Resolution | Unresolved |
|---|---|---|---|---|
| C1 | keep (fixed scope wording) | (a) Owen's rows keyed by a mail pointer instead of ZOM-648 / ZOM-649 must pass: the title counts session rows, any key. (b) 80 rows (T11) or a resend duplicate (T7) gives 80 or 83 and fails | count re-verified (80 tickets SQL L532–L690 + 2 in SQL L434); run-1 to run-6 all wrote 82; finding 9 | none |
| C2 | keep | (b) offsetting errors keep 45 (run-4: 13 coached counted, 13 Samsung dropped) | the volume row cannot see it by design; C3, C4, C12, C13 grade the members directly (gate 15); run-4 fails those | none |
| C3 | fixed | (a) a valid run writing "briefed players on how it plays" must pass: title says coaching, evidence lists the paraphrases (Eval 2.10). (b) 13 rows with a coaching reason on the wrong sessions would pass the count | implausible (no other observer reports a walkthrough; SQL L508 covers Claire's Friday only); member list moved to evidence (finding 2) | none |
| C4 | keep | (a) "excluded" or "no" as the verdict word passes. (b) counted on the ticket's "Coaching: none reported" (SQL L610) fails | run-4 and run-5 counted ZOM-607 and fail, as designed (F20) | none |
| C5 | fixed weight | (a) "players were told how it plays first" passes as coaching. Weight: a reviewer could keep 3 (interpretation) | the reason needs Claire's mail joined to ZOM-613 by observer and date (SQL L508, L622) under the Slack rule (SQL L881): multi-source like C4 (finding 7) | none |
| C6 | fixed | (b) 9 rows (contacts never read, run-1) or 2 rows (DM missed) fail the 11 | count re-verified from SQL L871, L967, L1015; member list moved to evidence (finding 3) | none |
| C7 | keep | (b) counted because the notes doc says Coaching: none and age 35 fits (run-5) | fails as designed; Brian's DM SQL L871 is the deciding record (F21) | none |
| C8 | fixed weight | (a) "all at mobile game companies" passes. (b) "not a friend" fails: Leonard's friends rule SQL L879 counts a known group | reason re-verified; weight 5 per finding 7 (DM in Slack + notes doc relation SQL L178 + rule SQL L877) | none |
| C9 | fixed | (a) "dev build, never went through a store" without the number 1943 is valid and was accepted only in evidence before: now in the title. (b) 10 rows (second wave missed) fails | finding 4; build re-verified on 13 notes docs (SQL L196, L200, L306 among them) | none |
| C10 | keep | (b) counted because 0.3.127 matches the store version prefix (T5) | notes doc SQL L200 "Build: 0.3.127 (1943)"; Leonard SQL L883 | none |
| C11 | fixed weight | (a) "never went through a store" alone passes (title now names dev / non-store build). (b) "Redmi Note 13" as a device reason fails (SQL L728) | weight 5 per finding 7 | none |
| C12 | keep | (a) a run counting it while citing Vision Bot still passes: the verdict is graded, not the reasoning | allowed (prompt asks for verdicts); run-4 drops it and fails (F25, SQL L901) | none |
| C13 | keep | (b) "the pass ran on SM-A546E, not SM-A256E" fails | the gate's sentence "it covers all the Samsung sessions in the read" (SQL L174) settles it; /oe DR2 | none |
| C14 | keep | (b) counted because the notes doc shows a 35-year-old friend on 0.3.40 (40) | only the contact job SQL L1015 excludes it; run-1 and run-5 fail as designed | none |
| C15 | keep | (b) counted because console is not the mobile industry | Leonard SQL L877 "Anyone who works in games"; contact SQL L967 | none |
| C16 | fixed | (a) a valid row without the player's name (all six runs, Register has no player column SQL L342) failed the old evidence | finding 1; now passes run-1 to run-6; ticket-cell forms follow the /oe note (2_oe.md L65) | none |
| C17 | keep (evidence aligned) | (b) dropping Daniel Hughes as a low outlier fails: the deck says the observer's label stands (SQL L356) | evidence now matches C16's form; contact SQL L1029 'Lawyer' | none |
| C18 | keep | (b) dropping every Android phone for want of a pass | the gate names only Samsung (SQL L174); Pixel 8a comment SQL L844 | none |
| C19 | keep | (b) dropping all Fri Sep 26 sessions with Claire's | Claire's mail says "Friday at my place" (SQL L508); ZOM-605 observer Samuel Turner (SQL L606) | none |
| C20 | keep | (b) dropping family as not friends | Leonard SQL L879 "family, neighbours and old classmates count the same"; notes doc SQL L334 Relation: family | none |
| C21 | keep | (a) a memo saved as another Drive file type would fail "Google Doc" | plausible-but-unlikely path; every run made a Google Doc (run-1 to run-6); the card says "memo" and Leonard "put it in a memo"; harmless, not changed | none |
| C22 | keep | (b) "casual lead" appearing only in a hypothetical (run-4: "a casual lead would need casual sessions we do not have") | the title grades the memo's call; run-4's call is RPG lead and fails | none |
| C23 | keep | (a) a memo giving 3.83 without "27" could be valid. (b) 3.8 alone matches run-1's 3.77 rounded | the count is an operand of the deck's lead rule ("At least 6 counted sessions per audience", SQL L360) and guards the 3.8 rounding; every run that wrote 3.83 wrote 27 (run-2, run-3, run-6) | none |
| C24 | keep | (b) 3.5 at one decimal could hide 3.58 (run-1, 19 sessions) | the 18 operand rejects it; run-1 fails | none |
| C25 | fixed justification | (a) a memo "Panel: 3.33" without saying 9 players or player 8's void could be read as failing the title's qualifiers | the qualifiers define the figure (one panel number, Leonard SQL L875); 3.3 rounding is guarded by "over 9 players" (Android-only 3.25 also rounds to 3.3, SQL L368); finding 8 | none |
| C26 | fixed justification | (b) 10.5% is accepted, and a run that skips the D14 filter gets 10.51% (18 rows) which also rounds to 10.5% | very unlikely: it needs both the skipped filter and a one-decimal rendering; observed runs wrote two decimals (run-2 10.47%, run-3 10.4%); rejecting a fair 10.5% would be overly_specific under BOTH_FAIR_FIGURE (1_prompt.md L236). Kept (Eval 2.7 B11 exception) | none |
| C27 | fixed weight | weight 3 could be argued as limited reconciliation once verdicts exist | playbook gate 15: a count only the full audit produces is multi-source (5), like C2 (finding 5); 37 re-verified | none |
| C28 | fixed weight | (a) Done on Owen's optional ZOM-648 / ZOM-649 must not count against it | the title's range ZOM-568 to ZOM-647 excludes them; finding 5 | none |
| C29 | fixed weight | the log note mapping alone is one rule (3) | the state is decided by the coaching trace (SQL L508, L881) like C4 (finding 6); run-4 and run-5 fail | none |
| C30 | fixed weight | as C29 | decided by Brian's DM SQL L871 like C7; run-5 fails | none |
| C31 | fixed weight | as C29 | decided by the notes doc build SQL L306 and Leonard SQL L883 like C10 | none |
| C32 | fixed weight | as C29 | decided by the Samsung pass (SQL L764 comment, L174, L901, L856) like C12; run-4 fails | none |
| C33 | fixed weight | as C29 | decided by the contact job SQL L967 like C15; run-1 and run-5 fail | none |
| C34 | keep | (b) Canceled because Douglas's other sessions ran on 1943 | notes doc SQL L292 Build: 0.3.127 (127); routine comparison stays 3 like C18–C20 | none |
| C35 | keep | (a) a reply posted before or after the other writes passes | the /oe note says do not grade timing (2_oe.md L65); thread ts SQL L889 | none |
| C36 | keep (weight 3) | weight: a reviewer applying sibling consistency could expect 5 like C22 | kept as interpretation of Leonard's stated mapping (SQL L889), the call itself graded in C22; residual Criteria Weights risk 2 of 38 = 5.3% → NON-FAIL 4 at worst | weight judgment (C36, C38) |
| C37 | keep | (a) a thread reply in Leonard's thread that tags Brian passes (still in C090N54TG79); a DM D076RBM29JS fails | Leonard: "tell <@EMPLOYEE_0026_SLACK_ID> in this channel" (SQL L889); run-1 to run-6 posted top level | none |
| C38 | keep (weight 3) | (a) "on hold, park it" passes; (b) "goes on" (run-1, run-4, run-5) fails. Weight as C36 | Robert's post /731 names the work; residual weight risk as C36 | weight judgment (C36, C38) |
| re-verified | done | a ledger or plan value taken on trust | every literal above re-read through hg.py or the SQL line this session (item 3) | none |
| Failure signature | 40% | an edit could merge two runs' patterns | re-graded the six decoded end states against the changed rows: pass/fail unchanged, largest pattern {run-3, run-6} 2 of 5 = 40% | retention-only tie (plan Unresolved) |

**4. Recount.** Predicted all-fail from recorded defects: 0 after the C16 fix (before it, C16 and C17's twin form were the only candidates; C17's old evidence did not need the name). Tally from the Findings table (highest severity once): 4 Major rows (C3, C6, C9, C16), 0 Moderate, 1 Minor (C1), 10 weight rows and 2 style notes, all fixed; after fixes 0 / 0 / 0.

**6. Stage gate.** Run with `--paste` below. Upstream items outside this stage, not fixed here by instruction: readiness.evidence (stale upstream attestations on SQL rev7; the SQL must not change), chain.oe-writing and chain.oe-check (OE stages), and chain.rubric-writing, which fails only because the plan's own rubric-writing gate never passed (its blocking lines are those same two OE chain checks, readiness.evidence and diversity.authority_share, whose fix is a Locator-origin correction in the read-only ledger). The plan's §A2 bands for P5, P8, P11, P27–P33 still read 3; 09_Rubrics.json now carries 5 for those rows (plan not edited: it is the prep artifact).

Unresolved:
- Weight judgment on C36 and C38 (interpretation 3 vs inherited 5): at worst Criteria Weights NON-FAIL 4.
- Retention-only signature: runs 3 and 6 share it (40% ≤ 45%); reported, not tuned.
- chain.rubric-writing, chain.oe-writing, chain.oe-check, readiness.evidence: upstream, out of scope (see 6).

V3 sidecar: Working_Files/00_V3_Authoring_Evidence.json gained `rubric_rows` (C1–C38: fact_id, exact prompt span, accepted outcomes, alternatives review, SQL-cited source records with source_value, evidence_path from Leonard's ask C090N54TG79/1759266627.418203, reachability rationale and temporal evidence), `rubric_hash` ae4bad5e3ba3 and `prompt_hash` c3da944d7da5; v3.rubric_evidence and v3.fact_duplication now pass. The earlier `rubric_plan` block is unchanged.

Stage gate (run 2026-11-10, `python3 Task_Authoring/tools/stage_gate.py rubric-check Task_Authoring/task_inputs --paste`; not a PASS, so --paste inserts nothing; the non-PASS lines, quoted for the record):

```text
STAGE GATE rubric-check: FAIL — blocking 2 · warnings 1 · checks 23 (20 PASS incl. validity.rubric, surface.coverage, evidence.quoted_spans, review.counter_readings, v3.rubric_evidence, v3.fact_duplication)
FAIL chain.rubric-writing: 09_Rubric_Writing_Plan.md carries no pasted 'STAGE GATE rubric-writing: PASS' block (upstream: the plan gate fails on chain.oe-writing, chain.oe-check, readiness.evidence, diversity.authority_share)
FAIL readiness.evidence: rubric-writing: current stage attestation missing; historical paste cannot certify new work (upstream attestations on SQL rev7; out of scope)
WARN handoff.pasted: no PASS to paste
```
