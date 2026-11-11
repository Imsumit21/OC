## OE EVALUATION REPORT

### Task: Zombie Match 3D Halloween plan: call, owner and date for every live store surface and ad, plan doc and tracker shared with the review, ticket comments, assignments, store tickets and a thread reply
### Persona: Claire Morgan - Art Lead (claire.morgan@harmonygames.co)

Inputs reviewed: `Evals/task_inputs/08_Oracle_Events.md` (161 events), `04_Prompt.txt`, `00_Task_Assigned_Inputs.md`, `01_Universe_Inject.sql` (read as an overlay, never executed), universe date Oct 1, 2025 (synth-cut). No error-async input is saved, and the six baseline runs show no forced error and no async job.

### Phase 1: Structure & Alignment
- Derived critical path: read Leonard's message; find the review attendees; fix the population (Unity tab 56, Archive 4 out, ART-826 and ART-831 off the sheet); read the calendar, deck, three Frederick mails and his later Slack reply; read every serving ticket's notes; find the newer captures, the turned-down test, the stale end cards, the baked ART-809 master, the store exports, the icon decision and the statics cover; work out calls, dates and makers; create and fill the doc and tracker; share both with six people; comment 58 tickets; assign 48; open 2 store tickets; reply in the thread.
- Segments: 161 STEP, 0 CONTEXT, 0 RESPONSE_DESCRIPTION, 0 NON_ACTION.
- Coverage ledger: 22 requirements, each with a chain that begins at the saved prompt.

### Phase 2: Accuracy
| Step | Field | Result | Evidence |
|---|---|---|---|
| OE 1 | all | VERIFIED | SQL Slack row: ts 1759269913.882683, channel C06DJBJL798, all quoted asks; #zombie_marketing is private and Claire is a member (channels.json) |
| OE 2 | all | VERIFIED | SQL gcal row on Claire's calendar: 2025-10-02T16:00:00Z, six other attendees |
| OE 3 to OE 5 | all | VERIFIED | SQL sheet rows: 4 store surfaces, 56 Unity rows (all pairs matched by script), 4 Archive rows; shared with Claire as reader |
| OE 6, OE 7 | all | VERIFIED | SQL Doc body and slide text, word for word; one name hit each in Claire's view |
| OE 8 | all | VERIFIED | 62 injected tickets; newest base ART ticket is ART-792, created Aug 26; run 2 returned the same 62, hasNextPage false |
| OE 9, OE 26 | all | VERIFIED | SQL Trello actions; member 4b4a68fc0fec0b254e4f9d8e is Frederick Stone in the base; `trello_search` covers comment text by default |
| OE 10 to OE 14 | all | VERIFIED | 65 quoted bodies matched by script to the comment on the same ticket, 58 tickets |
| OE 15 to OE 18 | all | VERIFIED | Base mailbox holds no Frederick mail (846 Claire threads scanned); three injected copies; run tool result shows 3 |
| OE 19 to OE 25, OE 28, OE 30 | all | VERIFIED | SQL and base Slack rows, Claire's membership of each conversation, rank of each hit inside the default newest-first page |
| OE 27 | all | VERIFIED | Base thread: Frederick 12:40 PM PT with marcus.bennett_9-16_blur-VEED.mp4, 15 replies, Marcus's two zip files |
| OE 29 | all | VERIFIED | 11 PNG rows under the Store folder; no iPad file |
| OE 31 to OE 36 | all | VERIFIED | Calls, dates and makers recomputed by script from the records: 10 Skip, 12 Halloween version, 36 Refresh first, 30 on Oct 10, 18 on Oct 15, 6 Julia, 42 Marcus; every list identical to the OE |
| OE 37 | all | VERIFIED | Base Linear users and team; marcus.lee@harmonygames.co exists as a separate user |
| OE 38 to OE 52 | all | VERIFIED | Cataloged create and share tools; `gdrive_share_file` accepts role commenter; addresses match the attendee list |
| OE 53 to OE 110 | all | VERIFIED | Each ticket's call and date matched by script; 58 distinct tickets, equal to the serving set |
| OE 111 to OE 158 | all | VERIFIED | 48 distinct tickets, equal to the working set; makers match |
| OE 159 to OE 161 | all | VERIFIED | `linear_create_issue` takes assignee and dueDate; `slack_send_message` takes thread_ts; both link sources confirmed by tool result |

**Numeric observability (2.3A).** Every time on an Expected line is a Pacific rendering of a UTC timestamp, recorded in the ledger. Counts are recomputed, not copied: 4 + 56 + 2 = 62 rows; 14 + 36 + 2 + 10 = 62 calls; 31 + 1 + 4 = 36 Refresh first; 30 + 18 = 48 working ads; 6 + 42 = 48 makers. All 843 values and 3 absence words on Expected lines are ledgered, with none left over.

**Date and time (2.5).** Every source record is dated before the clock. Oct 2, Oct 10, Oct 15, Oct 16, Oct 17 and Oct 22 are future plan dates and are shown as future. All weekday names match the calendar.

**Act-vs-defer (2.6).** No write rests on a proposed resolution or system suggestion. Bounded search: the 78 Slack conversations Claire belongs to plus the overlay, Sep 8 to the clock, messages naming a ticket, Halloween, creatives, end cards, store art or retention campaigns, for "defer", "hold off", "not yet", "wait", "as-is", "as is" and "accept": 0 hits in 2,688 messages. Her mailbox holds no base thread on Halloween. Leonard's "maybe we swap the icon around the 24th?" is a question the calendar answers, and OE 6 and OE 38 handle it.

**Persona reach.** Every Slack read sits in a conversation listing Claire as a member. The sheet, Doc, deck, folder tree and files all list her in `shared_with_emails_json`. Gmail and GCal reads use her own copies. Linear and Trello are unscoped.

### Format & Standardization
No shape defects. Every OE is numbered, has one action, names its service, and has an Expected: line.

### Phase 3: Completeness
| Requirement | Covered by | Result |
|---|---|---|
| Read Leonard's ask | OE 1 | COVERED |
| Find who is on the review | OE 2 | COVERED |
| Fix the population of what is live | OE 3, 4, 5, 8, 9, 13 | COVERED |
| Release calendar | OE 6 | COVERED |
| Seasonal direction | OE 7 | COVERED |
| Notes for every serving ad | OE 10 to OE 14 | COVERED |
| UA plan and later changes | OE 15 to OE 19 | COVERED |
| Statics cover | OE 20, OE 21 | COVERED |
| Newer captures | OE 22 | COVERED |
| Existing Halloween ad art and whether it ships | OE 23 to OE 25 | COVERED |
| Stale end cards and baked master | OE 26, OE 27 | COVERED |
| Existing store art and the ticket rule | OE 28 to OE 30 | COVERED |
| Every call | OE 31, 32, 33, 36 | COVERED |
| Who makes what by when | OE 34 to OE 37 | COVERED |
| Plan doc | OE 38 | COVERED |
| Tracker | OE 39, OE 40 | COVERED |
| Share both files for comment | OE 41 to OE 52 | COVERED |
| Comment all 58 ads | OE 53 to OE 110 | COVERED |
| Assign all 48 working ads | OE 111 to OE 158 | COVERED |
| New store tickets | OE 159, OE 160 | COVERED |
| Thread reply with both links | OE 161 | COVERED |
- Path feasibility: SUPPORTED. Task solvability: SUPPORTED_BY_OE. Data and access, tool capability, preconditions and completion are all supported; 221 tool nodes passed the catalog checks with no unresolved item.
- Injected errors and async waits (3.5): none saved and none seen in the six runs, so no recovery event is needed.
- Prohibited actions (3.4): the prompt forbids nothing, and no step takes an action the prompt reserves for Claire.
- Outcome-first mapping: all 161 steps map to Outcome. Reads and calculations are proved by the doc, tracker, comments, assignees, tickets and reply they feed. No Process row is needed.

**Pre-verdict sweep (4.0)**

| # | Check | Finding |
|---|---|---|
| 1 | One wrong count, ID, channel or tool | PASS |
| 2 | One required write missing | PASS |
| 3 | One fact in expected data with no retrieving step | PASS |
| 4 | One act-vs-defer conflict | PASS |
| 5 | One non-action or final-response event | PASS |
| 6 | One prompt-forbidden write | PASS |
| 7 | One missing recovery/wait event for an injected error | PASS |

### Issues Found
| # | Step | Issue | Component | Effect |
|---|---|---|---|---|
| None | | No missing step, wrong step, minor imprecision, non-action, final-response event or shape defect was found | | |

**Note for the author, not an OE defect and no score effect.** The injected iPhone export names say 1242x2688 (OE 29), while ART-774 (March) and Martin's Jul 21 files say 1284 × 2778. Both older records predate Leonard's Sep 3 "right asset size" request. The size of the set live since Sep 17 cannot be read, and Leonard's Sep 30 "whatever is already exported is done" settles the Reuse call. A run that flags the size to Claire is still correct, so no rubric row should mark it down.

### Recommended Fixes
None required. There are no issues, so this report proposes no replacement OE text.

### Readability (advice only, no score impact)
- The set reads sentence-first: the goal comes first, the values are written out, and traps are called out (OE 25, OE 26, OE 33, OE 35). No step reads like a bare list of queries.
- OE 4 and OE 10 to OE 14 are long single lines. They are correct and easy to check by script, but slower to read. Grouping tickets by capture build would make them easier to scan.

## Deep Recheck

Passes: O1, O2, O3, Opus 5.5 inherited from this session with xhigh effort requested, each blind to the main review. O3 was not given the OE file.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| O1 | 161 events | 0 | 0 |
| O2 | 161 events | 0 | 0 |
| O3 | 84 inventory lines, 5 marked not fully settled | 5 | 0 gaps; 83 lines confirmed and matched to OEs, M76 rejected |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | O3 | M18: "the thread does not record whether the live file was ever swapped" | `slack/messages/C06DJBJL798/2025-08.json`, ts 1755117538.514179: "can start with this video and we’ll do others without music" | O3 inventory | Completeness | REJECTED | Not a gap. OE 27 and OE 33 read both sides. A scan of Claire's conversations from Aug 13 to the clock shows no no-music 9:16 replacing the cut, and the ticket points to this thread while its sibling cuts say "SFX only" |
| DR2 | O3 | M63: "the records fix no upload date" | SQL Doc body: "upload any day and allow 1 day for review" | O3 inventory | Completeness | REJECTED | Not a gap. OE 36 and OE 40 say the same: an owner and no fixed date |
| DR3 | O3 | M64: "the calendar does not say whether the Google Play listing icon counts as a listing graphic" | SQL Doc body: "Oct 17 submission: the last build that can carry Halloween changes." and "icon and screenshots back to normal" | O3 inventory | Completeness | REJECTED | Not a gap. One icon piece has one due date, set by the build route, and the same calendar treats the icon as a submission item. OE 6, OE 36 and OE 38 cover it |
| DR4 | O3 | M74: "a Fri Oct 3 finish versus the Oct 16 morning is not settled" | SQL Slack row c50f7403ef0b0cdda1d261760cebd86f: "store art stays with me" | O3 inventory | Completeness | REJECTED | Not a gap. No record sets an earlier date, so the merge cut in OE 36 is the due date. The working day is Martin's to choose |
| DR5 | O3 | M76: "ZM3D_Halloween_iPhone65_01_1242x2688.png" against "1284 × 2778 pixels" | Linear ART-774; `slack/messages/C08R8CHB0QL/2025-07.json` file "iPhone 6.5-inch_ 1284 × 2778 - 1.jpg"; `slack/messages/C06DJBJL798/2025-09.json`: "right asset size"; SQL Slack row b041f2ed8617697746dec5437e9b5e20: "whatever is already exported is done" | O3 inventory | Completeness | REJECTED | The records do not confirm a needed fix. Both 1284 × 2778 records predate the Sep 3 re-export, whose Drive folder holds no files in this export and is not shared with Claire. Leonard's later message settles the call, and size changes no call, owner or date. Passed on as a note above |

Effect on verdict: unchanged. The record was re-saved with the M18 and M76 evidence on OE 27 and OE 29, and the helper recomputed the same scores.

O3 inventory check: all 58 ad lines (call, maker, date) match the OE comment and assign steps with 0 differences. O3's totals, reached without the OEs, equal the OE totals: Halloween version 14, Refresh first 36, Reuse 2, Skip 10; 30 ads on Oct 10, 18 on Oct 15; Marcus 42, Julia 6; 2 new tickets.

- G1: rule set for the calls | Seasonal deck | 1 item (M1) | Covered by: OE 7
- G2: every ad we're running | Unity tab, ART ticket comments and the records that override them | 58 items (M2–M59) | Covered by: OE 4, OE 8, OE 10–14, OE 18, OE 22, OE 25–27, OE 31–35, OE 53–158
- G3: the store pages | Store tab and Halloween folder | 4 items (M60–M63) | Covered by: OE 3, OE 28–30, OE 36, OE 38, OE 40, OE 159, OE 160
- G4: icon timing | Leonard's ask and the release calendar | 1 item (M64) | Covered by: OE 6, OE 36, OE 38
- G5: due dates and flight | Frederick's mails and Slack reply | 3 items (M65–M67) | Covered by: OE 16, OE 17, OE 19, OE 34
- G6: campaigns, networks and population | Read me, Archive tab, mails, Linear, Snowflake AD_SPEND | 4 items (M68–M71) | Covered by: OE 3, OE 5, OE 8, OE 9, OE 13, OE 16, OE 17, OE 31
- G7: owners | Leonard's ask, Martin's cover, ticket descriptions, calendar | 3 items (M72–M74) | Covered by: OE 20, OE 21, OE 35–37
- G8: store date label | Trello list name and calendar | 1 item (M75) | Covered by: OE 6
- G9: iPhone export size | Export names, ART-774 | 1 item (M76) | Rejected, no fix required (DR5)
- G10: thread reply and review share list | Calendar event, Leonard's thread | 8 items (M77–M84) | Covered by: OE 2, OE 41–52, OE 161

Scope: "Work out the Halloween call for everything that's live today" covers 58 ad items and 4 store surfaces, all with OEs. The prompt reaches the set through the live creatives sheet that Leonard names, and /prompt owns any scoring of that.

Pass conduct: O1 reported opening `Task_Authoring/task_inputsN2/07_Baseline_Trajectories/README.md`, outside its allowed paths, and listing two folders. The main session read the same README. It holds generic rollout instructions and no task facts, so neither review is affected.

Platform defects: none

### FINAL VERDICT: PASS
Score: 5
Execution status: COMPLETE
Completeness score: 5
Accuracy score: 5
Path feasibility: SUPPORTED
Task solvability: SUPPORTED_BY_OE
Prompt follow-up: NONE
Review policy: oracle-events-v2
Reviewed OE SHA-256: 2a1fcd3e4d089445691db386ef66ac3917229add38326aaf99ccfcccec6652c7
Review context SHA-256: 784413b7dfcd84538fb63deafb413254d42ee925c569ef79201daa066bbb2dd2
OE record SHA-256: ee20063a45aef7fa8539e308a746b8c22bd2b577be13adef535a351722f41c4e
Eval version: task-quality-v1
Eval release SHA-256: c5b89f4c40a7902f968001f1aa6c710d47bf203842455bbe8dbb668ec7c8943b
Evaluator model: Opus 5.5 (claude-opus-5-5), effort Unconfirmed (skill requests xhigh)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Next action: Review complete; proceed to the next stage. Keep the iPhone size note in mind when writing rubric rows on the store sets.
Evidence limits: Static universe and tool evidence; SQL read as an overlay and never executed; no live writes executed. Run files and live tool descriptions were used for tool behaviour only. No error-async input is saved; the six runs show no forced error or async job. Search ranks were recomputed locally from Claire's memberships, not run on the live service. The iPhone size of the set live since Sep 17 is not readable.
