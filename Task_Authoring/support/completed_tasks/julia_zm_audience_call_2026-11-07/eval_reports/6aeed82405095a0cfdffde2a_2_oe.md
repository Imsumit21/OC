## OE EVALUATION REPORT

### Task: Julia closes out Leonard's friend-session audience read (80 logged sessions plus Owen's 2 late ones) and posts the keep/hold call on the cards-earlier change
### Persona: Julia Lawson - Product Manager

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Inputs: `08_Oracle_Events.md` (137 OEs, SHA-256 `bfaddd6d…5a741`, saved from the attachment to this /oe message), `04_Prompt.txt` (`c3da944d…`), the platform assignment, `01_Universe_Inject.sql` (`ffec30c8…`, read as an overlay, never executed). No error/async config or reference files. Evidence contract stage-evidence-v1: every value below was rechecked from the SQL and the base exports in this review (NEW); the /prompt report was used only for its requirement-authority ruling, which this review reassessed and agrees with.

### Phase 1: Structure & Alignment
- Derived critical path (from the prompt, Leonard's 2025-09-30 request, the roadmap card and the feedback note, before reading the OEs):
  1. Read Leonard's request; read the feedback note and Leonard's four later posts on it (game industry, relation, coaching, gate doc), the gate doc, and his 1943 build reply.
  2. Find the card (memo contents, "memo goes in Julia's folder with her log note"), the log note (close-out states, late forms), the criteria deck, the workbook (Log, Register).
  3. Build the session set: 80 tickets ZOM-568–647 with phones (comments), notes docs (build, age, relation), form mails (Marcus resend; Claire's later coaching mail), Owen's 2 late Sep 28 sessions, Brian's Kadıköy DM, contacts' jobs, Vincent's SM-A546E matrix pass (not ZOM-567's editor-only Vision Bot green).
  4. Decide counted/not counted (37 not counted: 11 game industry, 13 coached, 13 dev build 1943; 45 counted), compute the lead (casual 27 at 3.83 vs RPG 18 at 3.50, gap 0.33 → hold), panel 3.33, retention 10.47%.
  5. Writes: Register (82 rows), memo in Julia's root folder, 43 Done + 37 Canceled, thread reply "hold", post to Brian that the work does not go on.
- Segments: 137 STEP, 0 CONTEXT, 0 RESPONSE_DESCRIPTION, 0 NON_ACTION.
- Requirement authority (prompt-incorporation-v1): incorporated are Leonard's request ("his message says what he needs") and, through it, the roadmap card; the feedback note is named by the prompt. Julia's log note and deck, Leonard's amendments, the gate doc and the other records answer those asks as facts. **Not incorporated:** Robert's 2025-09-26 DM ("put a re-run note on it") and the log note's "Any form that comes in after this batch gets a ticket and a log row". Nothing in the prompt or the request asks for re-run notes, new tickets or Log rows.

### Phase 2: Accuracy

Every OE was checked against the records. All values match; the only defects are steps that present optional writes as required.

| Step | Field | Result | Evidence |
|---|---|---|---|
| OE 1–4 | all | VERIFIED | Leonard's request (SQL L889, ts 1759266627.418203, 21:10 UTC = 2:10 PM PT); feedback note (base #zombie-design 2025-09 /537, 05:01 UTC Sep 22); Robert's Monday post (/731, 18:52 UTC); Leonard's four top-level posts L873/L877/L879/L881, times and quotes exact |
| OE 5 | all | VERIFIED | Gate doc (L174), created 2025-09-24T15:12:40Z = 8:12 AM PT, shared with Julia; all five quotes exact |
| OE 6–9 | all | VERIFIED | Card "Cards earlier: waiting on the audience read" (L859, Backlog, last activity 16:52 UTC = 9:52 AM PT); log note L176 in `d_8140f09bf9f1b94cb8ee2d` (Julia's root folder, gdrive /drive_files/11673) with the deck and workbook; log-note and deck quotes exact |
| OE 10–11 | all | VERIFIED | Log tab: header + 80 rows ZOM-568…647, first row exact; Register header only. 80 issues all Todo, assignee Julia, every description "Coaching: none reported"; ZOM-567 not a session ticket |
| OE 12 | expected | VERIFIED | Counted all 80 comments: 13 Samsung exactly as listed (Galaxy S24, SM-A546E, SM-S921B, Galaxy S23 FE, Galaxy A54, Galaxy S22, Galaxy A15, Galaxy A35, SM-A346E, SM-S911B, SM-A155F, Galaxy S23, SM-A256E); 67 iPhone/Pixel/Redmi/OnePlus |
| OE 13 | expected | VERIFIED | 80 notes docs; ages 26–44; Brian's 9 "Kadıköy ekibi" with Host and "Coaching: none"; build 0.3.127 (1943) on exactly ZOM-577–586, 632, 637, 645 |
| OE 14–16 | all | VERIFIED | Claire form 21:00 UTC = 2:00 PM PT; Marcus resend "Same sessions as before."; Owen's reply 20:40 UTC (values exact; no ticket/Log row for the two); Claire's Sep 29 mail 10:02 UTC = 3:02 AM PT, her 13 tickets ZOM-607–619; it is the newest Claire mail in Julia's mailbox (only other is from 2023) |
| OE 17–19 | all | VERIFIED | Kadıköy DM (L869/L871); Leonard's 1943 reply L883 under Julia's Sep 22 post; contacts: Alper Koçak "QA tester, console games publisher" (ZOM-598), Arda Keskin "Live ops producer, mobile games studio" (ZOM-622), Brian's 9 no job, 71 others outside games, no base duplicates |
| OE 20–23 | all | VERIFIED | Vincent's #zombie-bugs post 15:12 UTC and 8:14 link reply; matrix row SM-A546E / yes / 0.3.127 (127) / PASS; ZOM-567 Done 17:10 UTC = 10:10 AM PT; Arthur's PR #476 "Vision bot" review comment exact |
| OE 24 | all | VERIFIED (read) | Robert's DM reply L885 under "Can you check if it's item specific?" (base D05GU6L0XFH /453). The read is accurate; the rule it carries is not incorporated (see OE 41–53) |
| OE 25–28 | all | VERIFIED | Panel mail 09:14 UTC = 2:14 AM PT, ratings exact; Leonard's void rule L875; Robert's retention rule L887; KPI note and rows exact (last week 2025-09-08, D7 mean 8.63) |
| OE 29 | expected | VERIFIED | Snowflake USER_COHORT_RETENTION (/tables/10/rows): 16 zombie_match_3d rows 2025-07-28…2025-09-15 with d14_ret, 2,607 installs, Σ installs×d7 = 27,297.69 → 10.47%. KPI sheet 14 rows, 2,267 installs → 10.59%. Accept-either is a both-fair context figure (decision_forks: BOTH_FAIR_FIGURE) |
| OE 30–32 | expected | VERIFIED | 30/9 = 3.33; 37 not counted (11/13/13), 45 counted; casual 27, 103.5, 3.83; RPG 18, 63, 3.50; gap 0.33 → hold |
| OE 33, 34, 35, 36, 37, 97, 98 | action | **MINOR** | Tickets, phone comments, Log rows and Done states for Owen's two sessions rest only on the log note's late-form line, which no ask incorporates. Values are right; the steps must be labelled optional |
| OE 38 | dependencies | **MINOR** | The Register's ticket cell for Owen's two sessions leans on "the two new tickets" from optional OE 33/34 |
| OE 39–40 | all | VERIFIED | Memo contents match the card; Julia's folder is `d_8140f09bf9f1b94cb8ee2d`, and `gdrive_move_file` exists |
| OE 41–53 | action | **MINOR** | Re-run notes on the 13 dev-build tickets rest only on Robert's DM, which no ask incorporates. Observers (Robert ×10, Douglas ×2, Frederick Stone ×1) are right |
| OE 54–96, 99–135 | all | VERIFIED | 43 Done and 37 Canceled match the counting exactly (log note "counted goes to Done, not counted goes to Canceled") |
| OE 136–137 | all | VERIFIED | Thread ts 1759266627.418203 in C090N54TG79; Brian (EMPLOYEE_0026) is a #zombie-design member |

Numeric observability: every figure comes from a value the tools return (sheet cells, ticket fields, mail bodies, Snowflake rows) plus a stated calculation (OE 29, 30, 32). Date/time: all records are before the clock. Act-vs-defer (bounded): checked the 147 Slack channels and DMs Julia belongs to, from Sep 22 to the clock. I looked for messages containing "defer", "hold off", "not yet", "wait", "as-is", "leave open" or "keep open" together with a ticket, session, register, memo, cards-earlier, tutorial or close word. I also checked every injected Slack message and mail, and Julia's 253 base mail threads for the ticket ids, "friend session", "cards earlier" and "audience read". Nothing defers the close-out, the reply or the post. Persona ACL: every scoped read is Julia's, shared with her, in her mailbox or in a channel/DM she is in.

### Format & Standardization
No shape defects. Every OE is numbered, has one action, names its service (or says "no tool" for a calculation), and has an Expected: line.

### Phase 3: Completeness
| Requirement | Covered by | Result |
|---|---|---|
| Find Leonard's request | OE 1 | COVERED |
| Feedback note and Leonard's amendments | OE 2, 4, 5, 18 | COVERED |
| Monday change / tutorial and level-order work | OE 3 | COVERED |
| Memo contents (card) and destination (folder with log note) | OE 6, 7 | COVERED |
| Session population (80 + Owen's 2; resend not doubled) | OE 8, 10, 11, 14, 15 | COVERED |
| Deciding facts per session, Samsung pass, Vision Bot decoy | OE 12, 13, 16, 17, 19–23 | COVERED |
| Lead criteria and decision | OE 9, 31, 32 | COVERED |
| Panel and retention context | OE 25–30 | COVERED |
| Fill the Register | OE 38 | COVERED |
| Write the memo and put it in Julia's folder | OE 39, 40 | COVERED |
| Close out the session tickets | OE 8, 54–96, 99–135 | COVERED |
| Reply with keep or hold | OE 136 | COVERED |
| Tell Brian | OE 137 | COVERED |
- Path feasibility: SUPPORTED. Task solvability: SUPPORTED_BY_OE.
- Outcome-first mapping: every write (OE 38–40, 54–96, 99–137) and the decision steps (OE 30–32) map to Outcome rows on the Register, memo, ticket states, reply and post. The reads need no Process rows. OEs 33–37, 41–53, 97 and 98 must not become rubric rows unless the data is changed to incorporate them.

### Issues Found
| # | Step | Issue | Component | Effect |
|---|---|---|---|---|
| 1 | OE 41–53 | Thirteen re-run-note comments are presented as required. They rest only on Robert's 2025-09-26 DM ("put a re-run note on it so the observer runs it again"), which neither the prompt nor Leonard's request incorporates. | Accuracy (Minor) | NON-FAIL 3. Following them is harmless, but rubric rows built from them would be Incorrect (Major) at /rubric |
| 2 | OE 33, 34, 35, 36, 37, 97, 98 | Creating tickets, phone comments, Log rows and Done states for Owen's two late sessions is presented as required. It rests only on the log note's "Any form that comes in after this batch gets a ticket and a log row when I see it", which no ask incorporates. The prompt asks for the Register, not the Log. | Accuracy (Minor) | NON-FAIL 3 |
| 3 | OE 38 | "the two new tickets among them" ties the Register's ticket cell for Owen's sessions to the optional OE 33/34 | Accuracy (Minor) | NON-FAIL 3 |
| 4 | OE 35, 36 | "in the batch's form" overstates one format: the batch comments vary ("on an iPhone 15", "phone was an iPhone 14", "phone: iPhone 13", "device for this one: iPhone 13") | Accuracy (Minor) | NON-FAIL 3 |
| 5 | OE 136 | "after every other write except OE 137" adds an ordering no record requires | Accuracy (Minor) | NON-FAIL 3 |

No missing step, no wrong value, no non-action or final-response event, no shape defect. The OE 29 accept-either retention figure (10.47% / 10.59%) is a both-fair context figure, not a decision fork.

### Recommended Fixes
1. **OE 41–53 and OE 24: mark them optional, or settle them in the data.** Easiest: start each of OE 24 and OE 41–53 with "(optional, not graded)" and make sure no rubric row requires a re-run note. If you want re-run notes graded, a record Leonard or Julia already relies on has to call for them: a line in the log note or on the roadmap card saying not-counted sessions are handled the way Robert set out. Then rerun /injection, /prompt, /hardness, /oe and /rubric. Ready-to-paste wording for OE 41 if you keep it as optional (OE 42–53 follow the same pattern with their own ticket and observer: ZOM-578–586 Robert, ZOM-632 and ZOM-637 Douglas, ZOM-645 Frederick Stone):
   > OE 41 (optional, not graded) Leave a re-run note on ZOM-577 in Linear, because the session was dropped for a technical reason. Robert's DM to Julia asks for this but nothing in the request does. Expected: a comment on ZOM-577 saying it ran on build 0.3.127 (1943), which Leonard says "never went through a store", so Robert can run it again.
2. **OE 33–37, 97, 98: mark them optional.** Start each with "(optional, not graded)". They are a sensible way to follow Julia's own log note, but the prompt asks for the Register, not new tickets or Log rows. To grade them, the request or the card would have to point to the log note's handling of late forms (then rerun /injection onward).
3. **OE 38: accept either ticket cell for Owen's two sessions.** Ready-to-paste Expected line:
   > Expected: 82 rows, one per session, columns ticket, audience, stars, verdict, reason. Not counted, with its reason: ZOM-568 to ZOM-576, ZOM-598 and ZOM-622 (works in games); ZOM-607 to ZOM-619 (coached); ZOM-577 to ZOM-586, ZOM-632, ZOM-637 and ZOM-645 (dev build 0.3.127 (1943)). Counted: the other 43 tickets, including the 13 Samsung sessions, plus Owen Baker's two Sun Sep 28 sessions (Ayşe Polat, casual, 5; Daniel Hughes, RPG, 1.5). Their ticket cell holds the new ticket key if one was created, or a pointer to Owen's Sep 30 mail if not.
4. **OE 35, 36:** replace "in the batch's form" with "naming the phone (the batch has no single wording)". Expected values stay "iPhone 15" (Ayşe Polat) and "Pixel 8" (Daniel Hughes).
5. **OE 136:** drop "after every other write except OE 137", or say it is only a suggested order.
6. **Optional, not scored (data wording).** The recheck's O3 pass read the gate doc's "A pass covers a device only if it ran on that device" as covering only SM-A546E. That reading would flip the call to keep. The doc's next sentence settles it ("Once there is a pass, it covers all the Samsung sessions in the read."), and /prompt settled it the same way. If you ever edit the SQL anyway, rewording that sentence to "a pass on any Samsung phone covers every Samsung session" would remove the doubt. Any SQL change means rerunning /injection, /prompt, /hardness, /oe and /rubric.

These are OE-only edits. If you change only the OEs, send `/oe` again, then `/rubric`, because /rubric reads the OEs. /injection, /prompt and /hardness don't read the OEs, so their passes still count. If you change the SQL to make the re-run notes or late-form tickets graded, send `/injection`, `/prompt`, `/hardness`, `/oe`, `/rubric` in that order.

### Readability (advice only, no score impact)
- The set is strong on readability: actual values written out, traps called out (Vision Bot is not a phone pass in OE 23; Marcus's resend in OE 14; Claire's later mail in OE 16), and record names given in plain words.
- OEs 54–135 are 82 one-line state changes. That is fine for the count, but a short note on OE 54 and OE 99 saying "the full lists come from OE 31" would help a reviewer.
- OE 31's Expected line packs four groups into one paragraph. Splitting it into one line per group (game industry 11, coached 13, dev build 13, counted 45) would make it easier to check.

## Deep Recheck

Passes: O1, O2, O3, Opus 5.5 (claude-opus-5-5) subagents at this session's effort, each blind to the main review (O3 also without the OE file). Their results were checked only after the main review record was saved.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| O1 | 137 OEs | 5 | 2 |
| O2 | 24 prompt requirements, 137 OEs | 0 | 0 |
| O3 | 5 open instructions, 173 items | 3 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | O1 | OE 29 "Vincent's note allows quoting either source, so either figure is fair." | USER_COHORT_RETENTION 16 rows → 10.47%; KPI sheet 14 rows → 10.59% | Decision fork | Accuracy | REJECTED | Meets the both-fair figure test: one memo context figure differs, both values come from persona-visible operands, and the call, writes, destinations and recipients are the same. Vincent's note covers quoting "off the warehouse or off this sheet". The only difference is the 2025-09-15 cohort, whose D14 cells are a platform defect (FD-3785). The /prompt report also says "Accept either". Recorded as BOTH_FAIR_FIGURE |
| DR2 | O1 | OE 29 "16 rows, cohort weeks 2025-07-28 to 2025-09-15" | USER_COHORT_RETENTION 2025-09-15 d14_ret 5.83 / 7.17 | Platform | PLATFORM:FD-3785 | REJECTED | Known platform defect; not scored against the task |
| DR3 | O1 | OE 33–37 "Create a ticket for Owen's casual session", "in the batch's form" | Log note "Any form that comes in after this batch gets a ticket and a log row"; ZOM-569 "phone was an iPhone 14", ZOM-570 "phone: iPhone 13" | Unrequested writes | Accuracy | CONFIRMED | Matches the main review's MINOR on OE 33–37, 97, 98. OE 35/36 expected_data set MINOR for "the batch's form" |
| DR4 | O1 | OE 108 "Move ZOM-577 to Canceled" vs re-run note OE 41 | Robert DM "Dropped for anything else, no re-run, it just gets closed" | Decision fork | Accuracy | REJECTED | The log note settles every not-counted ticket: "Close-out when the read is done: counted goes to Done, not counted goes to Canceled." Robert's DM names no ticket state, and the prompt doesn't incorporate it |
| DR5 | O1 | OE 136 "after every other write except OE 137" | Leonard L889 "reply here with keep or hold" | Unstated ordering | Accuracy | CONFIRMED | No record requires the order; S136 dependencies set MINOR |
| DR6 | O3 | M166 / M20–M74 Samsung rows: per-device reading of "A pass covers a device only if it ran on that device" | Gate doc (SQL L174) | Set membership | Accuracy | REJECTED | The same doc's next sentence speaks to exactly this case: "Once there is a pass, it covers all the Samsung sessions in the read." Vincent's SM-A546E row is a clean on-device pass of store build 0.3.127 (127), so all 13 Samsung sessions count (call: hold) |
| DR7 | O3 | M26 / M108 ZOM-593 "Galaxy A54" fork | Gate doc (SQL L174) | Set membership | Accuracy | REJECTED | Same sentence: the pass covers all Samsung sessions whatever the model |
| DR8 | O3 | G3 M163–M164 "new ticket + Log row" treated as required | Log note (SQL L176) | Required writes | Completeness | REJECTED | Not a graded requirement: neither the prompt nor Leonard's request incorporates the late-form line. OEs 33–37, 97 and 98 cover it anyway and are asked to be labelled optional |

Effect on verdict: unchanged. The two confirmed findings add Minor items (OE 35/36, OE 136); Accuracy stays 3 and Completeness stays 5.

O3 inventory (after the main-session check):
- G1: fill the Register tab | ZM audience sessions / Register | 82 items (M1–M82) | Covered by: OE 31, 38. O3's Samsung verdicts under the per-device reading were rejected (DR6); the 13 Samsung sessions count.
- G2: close out the session tickets | Linear ZOM-568–ZOM-647 | 80 items (M83–M162) | Covered by: OE 54–96 (43 Done), 99–135 (37 Canceled)
- G3: late-form ticket and Log row | Linear / Log tab | 2 items (M163–M164) | Covered by: OE 33–37, 97, 98 (optional, not graded)
- G4: memo contents and location | Google Doc in Julia's folder | 4 items (M167–M170) | Covered by: OE 39, 40 (inputs OE 25–32)
- G5: reply and tell Brian | Slack #zombie-design | 2 items (M171–M172) | Covered by: OE 136, 137
- Call and decoy | criteria deck, gate doc, ZOM-567 | 3 items (M165, M166, M173) | Covered by: OE 32, 21, 22–23
Scope: G1 (82 rows) and G2 (80 tickets) each cover more than 15 items. The prompt names both ("the register tab", "the session tickets") and the OEs list every item, so nothing is missing.

Platform defects: PLATFORM:FD-3785 (USER_COHORT_RETENTION 2025-09-15 D14 cells filled before the window closes; memo context figure only, both values accepted).

### FINAL VERDICT: NON-FAIL
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Score: 3
Execution status: COMPLETE
Completeness score: 5
Accuracy score: 3
Path feasibility: SUPPORTED
Task solvability: SUPPORTED_BY_OE
Prompt follow-up: NONE
Review policy: oracle-events-v2
Reviewed OE SHA-256: bfaddd6d2fc438ac31a713e734d7bed9302f5676a09dfea0e0a71b7179e5a741
Review context SHA-256: 71eb5c8ad0e41cb873c5b1dc8bc3beafb091d6db7a451421421f5ea347b0c7e6
OE record SHA-256: 9d618c4f70cf3eecf3354c5b3b16021ba9bb8b8824586437d276b384391293e0
Eval version: task-quality-v1
Eval release SHA-256: 56292d5d69c9e3fcb2ecc44ea7b0fb5a8fdf3e7aa1026fa9da6fb9472960e631
Evaluator model: Opus 5.5 (claude-opus-5-5), session effort
Next action: Label OE 24, 33–37, 41–53, 97 and 98 optional (not graded), fix OE 35/36/38/136 as above, then send /oe again (and /rubric after it)
Evidence limits: Static universe, SQL overlay and tool-catalog evidence; no live writes executed. Snowflake rows read once with hg_search (not loaded whole); the record cites the KPI sheet and Robert's rule plus a recorded calculation for the warehouse figure.
