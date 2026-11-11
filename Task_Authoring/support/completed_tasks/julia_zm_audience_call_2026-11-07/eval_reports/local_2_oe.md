## OE EVALUATION REPORT

### Task: Julia settles Leonard's "cards earlier" audience call from the friend sessions: fills the Register tab, writes and files the memo, closes out the session tickets, replies in Leonard's thread with keep or hold and tells Brian in #zombie-design whether the tutorial and level order work goes on
### Persona: Julia Lawson - Product Manager (julia.lawson@harmonygames.co)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Inputs: OEs `Evals/task_inputs/08_Oracle_Events.md` rev4 (137 OEs, sha256 `7f0aa81e…`, identical to `Task_Authoring/task_inputs/08_Oracle_Events.md`); prompt `04_Prompt.txt` (sha256 `c3da944d…`); assignment `00_Task_Assigned_Inputs.md` (Product / Julia Lawson / Marketing and GTM / Analysis and synthesis / long-horizon, medium); injection SQL `01_Universe_Inject.sql` rev9 (sha256 `3a98aa36…`, read, never executed). Reference files: none. Friction: none, so no recovery or wait events are needed (3.5).

What changed since the last review (rev3, local PASS 5; the portal /oe gave it NON-FAIL 3): rev4 applies the portal's fixes and nothing else. Diffed against the rev3 segments in the previous record:
- 21 OEs now start with "(optional, not graded)": OE 24 (Robert's re-run rule), OE 33–37 (Owen's two late tickets, their phone comments, the two Log rows), OE 41–53 (13 re-run notes), OE 97–98 (closing Owen's new tickets). OE 24 and OE 33 also say why.
- OE 31 drops its three re-run clauses. OE 38 drops "re-run", names the build "0.3.127 (1943)", lists Owen's two sessions and accepts either a new key or a pointer to Owen's Sep 30 mail in their ticket cell. OE 35/36 drop "in the batch's form" and expect the bare phone. OE 136 drops "after every other write except OE 137".
- The other 110 OEs are byte-identical to rev3. Prompt, SQL, universe, clock and catalog are unchanged.

Method: the 27 changed OEs were checked again against the SQL (NEW). The 110 unchanged OEs keep their verified source anchors from the rev3 record (REUSED: same SQL, prompt, universe, clock and catalog; the helper rehashes every anchor on save). Their requirement mapping was reassessed under `prompt-incorporation-v1`, as the contract requires before reusing an older ledger. Record: `Evals/task_inputs/reports/drafts/oe_review_record.json` (137 steps, 26 coverage entries, 291 value-ledger entries covering all 468 Expected-line values and 8 absence claims; validator: 0 unledgered, 0 unresolved).

### Phase 1: Structure & Alignment
- Derived critical path (independent of the OEs, 26 requirements under `prompt-incorporation-v1`): find Leonard's ask (thread, three-way call, keep/hold mapping); read the feedback note, Robert's Monday post and Leonard's four updates (game industry, friends, coaching, gate doc); read the gate doc (Samsung pass, dev builds, Samsung device group); read the roadmap card (memo contents and folder); read Julia's log note (close-out: counted to Done, not counted to Canceled) and the criteria deck (observer label stands, mean stars, at least 6, gap under 0.25 is no clear lead); enumerate the 80 logged sessions and Owen's 2 late ones; per session get phone, build, age, relation, job and coaching; find the Samsung pass (QA matrix) and rule out Vision Bot; get panel and retention context; decide 82 sessions; compute the call; then write 82 Register rows, the memo in Julia's folder, 80 ticket states, the thread reply and the Brian post.
- Excluded as unincorporated (Task requirement authority): Robert's DM rule "put a re-run note on it so the observer runs it again" (SQL L885) and the log note's "Any form that comes in after this batch gets a ticket and a log row when I see it." (L176). The prompt, Leonard's ask (L889, "his message says what he needs") and the roadmap card (L859, "what goes in it is on the roadmap card") ask for neither. The card points to the log note only for the folder ("memo goes in Julia's folder with her log note"), and "a reference used for facts does not incorporate all its rules". The log note's close-out line is different: the prompt says "close out the session tickets" and that line defines close-out for those same tickets, so it stays.
- Segments: 137 STEP (21 of them labelled optional, not graded), 0 CONTEXT, 0 RESPONSE_DESCRIPTION, 0 NON_ACTION.
- Incorporation chain: prompt → Leonard's ask (L889) → roadmap card (L859) → Julia's folder (L176). Leonard's updates to the feedback note (L873, L877, L879, L881) and his 1943 reply (L883) are incorporated by "the ones that came out of his feedback note"; the gate doc (L174) through his Sep 24 update; the Register header (L342) through "fill in the register tab".

### Phase 2: Accuracy

All 137 OEs are clean on all six fields.

| Step | Field | Result | Evidence |
|---|---|---|---|
| OE 24 | action | VERIFIED (optional) | Correctly labelled optional. Its new sentence ("Neither the prompt nor Leonard's request asks for re-run notes") holds: neither text mentions re-runs; the rule is only in Robert's DM thread reply (L885, ts 1758913471.205816 under D05GU6L0XFH 1758901945.292269). No graded OE cites OE 24 any more. |
| OE 31 | expected_data, dependencies | VERIFIED | Only the re-run clauses are gone. Recomputed from raw SQL: 37 not counted (game industry 11: ZOM-568..576, 598, 622; coached 13: ZOM-607..619; dev build 13: ZOM-577..586, 632, 637, 645), no session in two groups; 45 counted (43 tickets + Owen's 2). Cites only earlier OEs (2, 4, 5, 12, 13, 15–19, 21–23). |
| OE 33, 34, 37 | action | VERIFIED (optional) | Correctly labelled optional: late-form tickets and Log rows rest only on the log note's general line (L176). Values unchanged from rev3 and still verified against Owen's reply (L434) and the batch shape (L576). |
| OE 35, 36 | parameters, expected_data | VERIFIED (optional) | "the batch has no single wording" holds. Julia's 80 phone comments use nine forms: "on an iPhone 15" (ZOM-568, L694), "phone was an iPhone 14" (ZOM-569), "phone: iPhone 13" (ZOM-570), "device for this one: iPhone 13" (ZOM-571), "iPhone 14" (ZOM-573), and others. "iPhone 15" and "Pixel 8" are Owen's words for Ayşe Polat and Daniel Hughes (L434). |
| OE 38 | information, expected_data, dependencies | VERIFIED | Header (L342): "Register: one row per session", "ticket", "audience", "stars", "verdict", "reason". Groups and reasons match the recompute; the 13 dev-build notes docs read "Build: 0.3.127 (1943)" (e.g. L196 Robert - 01). Owen: "Day: Sun Sep 28", "1. Ayşe Polat … casual, 5 stars", "2. Daniel Hughes … RPG, 1.5 stars"; his mail is 2025-09-30T20:40:00Z (Tue Sep 30, 1:40 PM PT). The ticket cell no longer needs the optional OE 33/34, so a run that skips them can still fill all 82 rows. |
| OE 41–53, 97, 98 | action | VERIFIED (optional) | Correctly labelled optional. Values unchanged from rev3: the 13 dev-build tickets and their observers (Robert ×10, Douglas ×2, Frederick Stone ×1); Owen's sessions count, so Done if the ticket exists. |
| OE 136 | dependencies | VERIFIED | The ordering clause no record required is gone; thread_ts 1759266627.418203 (Leonard's top-level post in C090N54TG79) unchanged. |
| OE 1–23, 25–30, 32, 39, 40, 54–96, 99–135, 137 | all | VERIFIED (REUSED anchors) | Byte-identical to rev3; anchors and the per-session recompute carried over on the same SQL, universe and catalog. Requirement mapping reassessed: none of these graded OEs rests on an unincorporated rule. The close-out states come from the log note the prompt's "close out the session tickets" uses; the memo contents and folder from the card; the panel and retention methods resolve the card's "the panel and retention as context". |

Numeric observability (2.3A): unchanged; every figure is tool-visible at the stated precision (Snowflake d7_ret to 2 decimals, star values as typed, sheet cells as strings). Derived figures: casual 27 counted, 103.5 stars, mean 3.83; RPG 18 counted, 63 stars, mean 3.50; gap 0.33; panel 30/9 = 3.33; D7 10.47% (warehouse) or 10.59% (KPI sheet). Act-vs-defer (2.6): the bounded search from the earlier rounds still applies to the unchanged SQL and universe (Julia's Slack channels and DMs and her mailbox, Sep 22 to the clock, terms "defer", "hold off", "not yet", "wait", "as-is", "leave open" and the ticket, workbook, memo and call names). No write rests on a deferred decision; the only "hold" is Leonard's own mapping. Date/time (2.5): every expected event is before the clock; the latest is Leonard's ask, 2025-09-30T21:10:27Z.

### Format & Standardization
- No shape defects. Every OE is numbered, does one thing (a read, a calculation or a single write), names its service or says "no tool", gives the record and filters, and has an Expected: line. The "(optional, not graded)" prefix is a label, not a second action. OE 7, 17, 18 and 20 pair a search with the read of what it finds, which is one discovery. No arrow chains or JSON.

### Phase 3: Completeness

| Requirement | Covered by | Result |
|---|---|---|
| C01 Leonard's ask | OE 1 | COVERED |
| C02–C05 Feedback note, Monday post, Leonard's updates, gate doc | OE 2, 3, 4, 5 | COVERED |
| C06 Roadmap card | OE 6 | COVERED |
| C07–C08 Folder and log note (close-out states), criteria deck | OE 7, 8, 9 | COVERED |
| C09–C11 Population, phones, notes docs | OE 10, 11, 12, 13 | COVERED |
| C12 Forms incl. Owen's two late sessions | OE 14, 15 | COVERED |
| C13–C16 Coaching, game industry, build 1943, Samsung pass vs Vision Bot | OE 16, 17, 19, 18, 20–23 | COVERED |
| C18–C19 Panel, retention | OE 25, 26, 30; 27, 28, 29 | COVERED |
| C20–C21 Verdicts, call | OE 31, 32 | COVERED |
| C24 Register, 82 rows | OE 38 | COVERED |
| C25–C26 Memo, in Julia's folder | OE 39, 40 | COVERED |
| C27 Close out the 80 session tickets | OE 54–96 (43 Done), OE 99–135 (37 Canceled) | COVERED |
| C29 Thread reply to Leonard | OE 136 | COVERED |
| C30 Tell Brian in #zombie-design | OE 137 | COVERED |

C17, C22, C23 and C28 of the rev3 ledger (Robert's rule, Owen's tickets with phone comments, Log rows, re-run notes) were dropped as requirements. They rest only on the two unincorporated lines above. The OEs that describe them stay in the set, correctly labelled optional, and nothing graded depends on them.

- Path feasibility: SUPPORTED. Task solvability: SUPPORTED_BY_OE. Every read is Julia-visible (#zombie-design, #zombie-bugs, her DMs with Brian and Robert, her mailbox, files she owns or is shared on; Linear, Trello, GitHub, Contacts, Snowflake unscoped). Every graded write has a cataloged tool (`gsheets_values_update`/`gsheets_values_append`, `gdocs_create_document`, `gdrive_move_file`, `linear_update_issue`, `slack_send_message` with `thread_ts`). Graded path nodes no longer depend on optional ones (OE 31 dropped OE 24; OE 38 dropped OE 33, 34 and 37).
- Outcome-first mapping: OE 38, 39, 40, 54–96, 99–135, 136 and 137 map to Outcome (sheet, doc, folder, ticket state, Slack end state). OEs 30–32 are checked through the Register verdicts, ticket states, memo figures and the call. The reads need no Process criterion. The 21 optional OEs map to NONE: no criterion should require them, and a run that does them should not be penalised. Rubric notes: grade OE 40 on where the memo ends up, not on a move call (d_8140f09bf9f1b94cb8ee2d is Julia's root Drive folder, so a new doc may already sit there); accept retention 10.47% or 10.59% (OE 29); accept either a new key or a pointer to Owen's mail in his two Register rows (OE 38); do not grade when OE 136 is posted relative to the other writes.

### Issues Found
None. The portal's 21 Accuracy items on rev3 (unincorporated writes presented as required, "in the batch's form", the OE 136 ordering) are all fixed in rev4.

### Recommended Fixes
None required.

### Readability (advice only, no score impact)
- The set reads goal-first, writes out the values and calls out the traps (OE 21–23 on Vision Bot vs the matrix, OE 31 on each exclusion, OE 29 on the two retention sources). The optional label leads each optional OE and OE 24 and OE 33 say why, which reads clearly. The 97 one-line write OEs are repetitive but map cleanly onto per-ticket Outcome rubrics.

## Deep Recheck

Passes: O1, O2, O3, Opus 5.5 (claude-opus-5-5), fresh for rev4, each blind to the main review (O3 also without the OE file). O1 disclosed that one broad grep over `Evals/` printed a few lines from `reports/`; it did not open those files and returned no scored finding, so its result was kept.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| O1 | 137 OEs | 1 (platform) | 0 |
| O2 | 25 requirements, 137 OEs | 0 | 0 |
| O3 | 4 open instructions, 173 items | 2 | 0; 166 items covered by graded OEs, 7 by optional OEs |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | O1 | "16 rows, cohort weeks 2025-07-28 to 2025-09-15, 2,607 installs … 10.47%" (OE 29) | Snowflake USER_COHORT_RETENTION 2025-09-15 rows carry d14_ret 5.83 / 7.17 before the 14-day window closes | 2.3A | PLATFORM:FD-3785 | REJECTED | Known platform defect, not scored. The OE's arithmetic is right, and OE 29 accepts 10.59% from the KPI sheet as well. |
| DR2 | O3 | Samsung fork: Reading A, a pass covers only the model it ran on, so 11 Samsung sessions are not counted and the call flips to keep | SQL L174 gate doc: "Once there is a pass, it covers all the Samsung sessions in the read." "Samsung is the one device group we check here" | O3 inventory | Completeness - session verdicts | REJECTED | The gate doc settles it in its own words: one pass covers all the Samsung sessions in the read. This is the same fork earlier rounds rejected; task-level ambiguity belongs to /prompt. |
| DR3 | O3 | M92–M101, M147, M152, M160 re-run notes; M163–M166 tickets and Log rows for Owen's two sessions, listed under "close out the session tickets" | SQL L885 Robert DM "put a re-run note on it"; L176 log note "Any form that comes in after this batch gets a ticket and a log row when I see it." | O3 inventory | Completeness - required writes | REJECTED | Not required under prompt-incorporation-v1. Both rules come from records the prompt chain does not incorporate: the card cites the log note only for the folder, and the close-out line defines Done/Canceled only. O2 reached the same conclusion on its own. The items are still covered by OE 24, 33–37, 41–53, 97 and 98, labelled optional. |

Effect on verdict: unchanged from the main review; Completeness 5, Accuracy 5. Scores are in the scoring table.

- G1: "fill in the register tab" (one row per session) | ZM audience sessions / Register | 82 items (M1–M82) | Covered by: OE 38 (verdicts from OE 31)
- G2: "close out the session tickets" (Done / Canceled) | Linear ZOM-568..ZOM-647 | 80 state items (M83–M162) | Covered by: OE 54–96 (43 Done), OE 99–135 (37 Canceled)
- G3: optional, unincorporated: re-run notes (13 in M92–M160), Owen's two new tickets with phone comments and Done (M163–M164), two Log rows (M165–M166) | Linear, Log tab | 17 items | Covered by: OE 41–53, 33–36, 97–98, 37 (optional, not graded)
- G4: memo call, numbers, panel, retention, destination | Drive, Julia's folder | 7 items (M167–M173) | Covered by: OE 39, 40 (figures from OE 29, 30, 32)
Scope: "fill in the register tab" (82 items) and "close out the session tickets" (80 items) each cover more than 15 confirmed items. The prompt names the tab and the tickets, and the OEs list every item, so each group is covered.

Platform defects: PLATFORM:FD-3785 (USER_COHORT_RETENTION: the 2025-09-15 cohort carries d14_ret before its window closes). Context figure only; OE 29 accepts 10.47% or 10.59%.

### FINAL VERDICT: PASS
Score: 5
Execution status: COMPLETE
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Completeness score: 5
Accuracy score: 5
Path feasibility: SUPPORTED
Task solvability: SUPPORTED_BY_OE
Prompt follow-up: NONE
Review policy: oracle-events-v2
Reviewed OE SHA-256: 7f0aa81e586aa5acab40efa7f3783908d634838bc1520ac89605af67c57981ee
Review context SHA-256: 045eaa62e0952844eb42d2b4fd271e32f26138dd7104f0c2ed4c9e5e3bbc4010
OE record SHA-256: 1bc2c7af4e65dd3b2e3229af0b1821bc4e9239e11b7c5d3289ca987f7fec68dd
Eval version: task-quality-v1
Eval release SHA-256: 3d51ac2867d2ce85946d4723cd9ad17c6a16d285f36ae548758157568b052b06
Evaluator model: Opus 5.5 (claude-opus-5-5)
Next action: Review complete; proceed to /rubric. No criterion should require OE 24, 33–37, 41–53, 97 or 98. Grade the memo's end location; accept 10.47% or 10.59%, either a new key or a mail pointer in Owen's Register rows, and any timing of OE 136.
Evidence limits: Static universe, SQL overlay and catalog evidence; no live writes or runtime calls. Search ranking (for example whether a Slack search surfaces the DM thread reply in OE 24) is not observable locally.
