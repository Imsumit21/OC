## PROMPT EVALUATION REPORT

### Task: Samuel works through Leonard's Sep 30 DM: a call (Go/Hold/Drop) on every PN Beta row and every filed phone-message ask, a new sheet and one-page note in his Drive, ticket comments and moves, a Go checklist on the push notifications card, emails to askers, and the counts back in the DM
### Assigned Persona: Samuel Turner - Game Designer
### Assigned Business Function: Design
### Assigned Competency: Marketing and GTM
### Assigned Task Skill: Retrieval
### Assigned Horizon: long-horizon

**Scope.** Chat review of attempt 6aea332703436a747f8302ec, mode audit, review date 2026-11-04. Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Universe `Universe_SynthCut` (hg4-synth-sep30cut v16), manifest `Evals/references/universes/synthcut/universe_manifest.json`.

| Input | Saved path | SHA-256 |
|---|---|---|
| Prompt | Evals/task_inputs/04_Prompt.txt | 22df2abfec652efab31a87a9cfb74b77632113a98dae00225368f31f29b66ae9 |
| Task details | Evals/task_inputs/00_Task_Assigned_Inputs.md | 600dce16d3f6923ea292ae60c066293120b5e82f0d46a81d142d8a51fdeacb26 |
| Injection SQL | Evals/task_inputs/01_Universe_Inject.sql | 403883334adc37eab71226c88fef04658d9a00382d95fec223ed7be95ab28948 |
| Task date | Evals/task_inputs/02_Universe_Date.txt | 189e2ac63a6fea6f90c0c9ab3dbfb06e0fc8ed7269f82b0d75af728e3b21da5c |
| Error/async config, dynamic context, reference files | none supplied | N/A |


Assignment intake: all five fields read from `00_Task_Assigned_Inputs.md` (Persona Samuel Turner, Business Function Design, Competency Marketing and GTM, Task Skill Retrieval, Task Type long-horizon). Samuel Turner matches roster entry `samuel_turner` (samuel.turner@harmonygames.co, Game Designer, Design).

---

### Injection Gate
- State: CURRENT (reused /injection result)
- Reviewed SQL sha256: 403883334adc37eab71226c88fef04658d9a00382d95fec223ed7be95ab28948  Eval 0 verdict: PASS (injection-static-v2, reviewed 2026-11-04T18:36:29Z)
- Eval 0 findings on records this prompt depends on: none. Advisories (snapshot-absent columns such as `linear_teams.issue_counter`; SC-13 list-name context) change no value the answer is graded on and stay here.

### Dataset Similarity
- Library: refreshed 2026-11-01T20:35Z, age 70.3 h, 270 tasks  Gate: PASS  Nearest tier: distinct
- Nearest neighbours are all distinct (meaning 0.581, 0.569, 0.559; wording ≤ 0.009): the closest are a Marcus Bennett Feb 11 art/video close-out and a Julia Lawson beta go/no-go review. Neither shares the PN-sheet scenario, records or asks. No identical, likely-duplicate or same-scenario neighbour.

---

### Requirement ledger

The prompt incorporates Leonard's Sep 30 DM ("His DM to me from yesterday has the whole job in it ... I need you to do all of it"), which incorporates the "Beta message rule" doc ("make a call on each one using the message rule doc").

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Call on every PNs Beta row + every filed phone-message ask | PN sheet f_a325dd4a… tab "PNs Beta" (14 rows); DES-313…346 (SQL); ZOM-542/ZOM-556 asks (SQL comments); rule doc f_dc45e0e5…; NotificationManager.cs; Slack/mail corrections | DM → sheet → DES-314 children → rule doc → code, QA note, Slack | gsheets_get_spreadsheet, linear_list_issues/get_issue, gdocs read, GitHub file read, slack/gmail reads | Sheet and doc shared with Samuel; DMs/channels he is in; his mailbox; Linear/GitHub/Trello unscoped | 35 rows, each Go/Hold/Drop with reason |
| New sheet in Samuel's Drive folder | Folder d_caafeec2804b3a67ce46aa (Samuel's only folder) | Prompt + DM "your Drive folder" | gsheets_create_spreadsheet, gsheets_values_update, gdrive_move_file | Owner | Sheet with Message, Ticket, Call, What's missing, Audience, Final headline, String change |
| One-page note in same folder | USER_COHORT_RETENTION (Snowflake); Slack/code on who hears; lapsed schedule in code | DM → warehouse | snowflake_execute_query, gdocs_create_document, gdrive_move_file | Snowflake unscoped | D1/D7 Sep 15 cohort week iOS/Android; who hears once they stop; lapsed reminders day by day |
| Comment the call on each ticket and move it | Rule doc state rules; Trello card 79 comment "Held work sits in Backlog, unassigned." | DM → rule doc → roadmap | linear_create_comment, linear_update_issue | Unscoped | Drop → Canceled, Go stays, Hold → Backlog unassigned |
| Ticket for any ask without one, no duplicates; string ticket for changed Go headline | ZOM-542/556 comments; DES-313 (Collect & Win) for the Win & Collect row; Leonard's Sep 29 "Your Squad Needs You Back" | DM, rule doc | linear_create_issue (parentId) | Unscoped | 3 new tickets under DES-314 |
| Go checklist on push notifications card | Card 6851a769c65dc0017a227bb7; Leonard comment "The beta list goes on this card as a checklist." | Prompt + DM | trello_create_checklist, trello_create_check_item | Unscoped | Checklist of Go messages |
| Email each asker except Leonard | Ticket/comment authors (Calvin, Brian, Robert, Oliver, Julia, Owen, Martin) | DES-313…346, ZOM-542/556 | gmail_send_message | Write (outside ACL) | One email per asker about their asks |
| Counts in the same DM | D06L58XCVKK | Prompt + DM | slack_send_message | Member | Go/Hold/Drop counts |

---

### Phase 1: Prompt Structure & Persona

**Persona:** PASS (5)
- Samuel is the named co-owner of "[Feature] Push Notifications - Samuel + Leonard" and built the Zombie Match notifications (Arthur's June 26 DM: "the ZM ones you just did"). Leonard asks him directly in their DM. Role, voice and access fit; all scoped sources are visible to him.

**Assigned Competency:** PASS (5)
- Deciding what the beta tells players, before UA spend, with D1/D7 retention in the note, is go-to-market player messaging work.

**Assigned Task Skill:** PASS (5)
- Retrieval is the core of the job: every call needs facts gathered from the sheet, tickets, code, the QA email, Slack corrections and the roadmap.

**Business Function:** PASS (5) — Design maps to Product & Design (gameplay/design requirements); player-message design decisions fit.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y — PASS
- Ambiguity: the rules, audiences, headlines and state moves are planted in the DM, rule doc, tickets and roadmap, not the prompt.
- Dynamic Change: Vincent's Sep 29 correction ("my iPhone pass was the 5-minute test build ... on the store build it never came through") overrides his Sep 24 pass; Leonard's Sep 29 "Your Squad Needs You Back" replaces the sheet headline; the Sep 25 calendar-cancel note settles day 14.
- Multi-Source: Sheets, Linear, GitHub code, Gmail, Slack, Trello, GCal, Snowflake, with decoys (deck "6 Ready", Brian's "send all the Ready ones").
- Data seeding: PASS. The prompt is a six-sentence trigger; operating detail lives in records.

**Naturalness:** PASS
- First person, casual, no document formatting, no polished connectives, no enumerated specs, no staged errors.

**Anti-Patterns:**
| Pattern | Status |
|---|---|
| Command List | PASS |
| Bolt-On | PASS (the ticket/email sentence restates DM work on the same job; removing it changes nothing, but it adds no unrelated ask) |
| Pre-Solving | PASS |
| Tool Mention | PASS |

**Diversity:** goes well beyond "investigate + post one Slack message": sheet, doc, ~30 ticket comments and moves, new tickets, a checklist, 7 emails and a DM reply.

---

### Phase 2: Depth Assessment

**Unique Ground Truth:** FAIL (2)

### Unique Ground Truth comparison

Unique Ground Truth: FAIL 2

Basis: The note's required 'who actually hears from us once they stop playing' content has two supported answers: the persona-visible Slack/code records say Zombie Match only sends on-device reminders (no server push), while the warehouse the same note must read holds weekly Zombie Match Firebase pushes to lapsed players through 2025-09-27. No prompt sentence or visible record settles which is true. Two smaller note forks are also open: per-platform versus pooled D1/D7, and whether settings opt-ins count as hearing from us.

Alternative selection: The DM sends the agent to the warehouse for D1/D7 and asks who hears from us once they stop playing; the warehouse's LIVE\_OPS.EVENTS push table is the strongest competing source for that exact question.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Answer from the Slack/code records: only on-device local reminders exist, gated by the game's own ask after level 20. | Same Go/Hold/Drop calls and counts in both readings. | Create the sheet and the one-page note in Samuel's Drive folder, comment and move each ticket, create missing tickets, add the Go checklist to the push notifications card, email each asker except Leonard, post the counts in the DM. | Samuel's Drive folder (d\_caafeec2804b3a67ce46aa); DES tickets; card 6851a769c65dc0017a227bb7; askers' mailboxes; DM D06L58XCVKK. | Sheet with every PNs Beta row plus every filed ask, one call each; note gives Sep 15 cohort week D1/D7 (Android 37.86%/10.68%, iOS 31.65%/9.28%) and says that once players stop playing only those who passed the game's own permission ask after level 20 (or switched notifications on in settings) hear from us, through the game's on-phone reminders on day 1 and days 7, 14, 21 and 28. | DMNOTE (Evals/task\_inputs/01\_Universe\_Inject.sql): "then who actually hears from us once they stop playing, and the lapsed reminders they get day by day"; ARTHUR (Evals/task\_inputs/01\_Universe\_Inject.sql): "NotificationManager only schedules once our own ask has run or they switch it on from settings, on both platforms"; NOPUSH (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/D06KV30TPL4/2025-06.json pointer /41/text): "We aren't using Push notifications yet."; LOCAL (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C08R27X0EAH/2025-09.json pointer /823/text): "All our PNs are local" |
| B | Answer including the warehouse: Zombie Match also sends server pushes to lapsed and all players. | Same Go/Hold/Drop calls and counts in both readings. | Create the sheet and the one-page note in Samuel's Drive folder, comment and move each ticket, create missing tickets, add the Go checklist to the push notifications card, email each asker except Leonard, post the counts in the DM. | Samuel's Drive folder (d\_caafeec2804b3a67ce46aa); DES tickets; card 6851a769c65dc0017a227bb7; askers' mailboxes; DM D06L58XCVKK. | Same sheet and calls; note gives the same D1/D7 but, reading the warehouse's push table next to the retention table, also reports that Zombie Match sends Firebase server pushes: a weekly comeback\_7d winback to the lapsed segment (275 sent on 2025-09-06) plus daily\_reward and new\_levels pushes to all players (latest 2025-09-27), so lapsed players hear from us through server campaigns as well, not only after the level-20 ask. | DMNOTE (Evals/task\_inputs/01\_Universe\_Inject.sql): "then who actually hears from us once they stop playing, and the lapsed reminders they get day by day"; SFPUSH (/tmp/hgp/snowflake\_extract.json): ""audience\_segment": "lapsed""; SFCOMEBACK (/tmp/hgp/snowflake\_extract.json): ""campaign\_key": "comeback\_7d""; SFLAST (/tmp/hgp/snowflake\_extract.json): ""send\_date": "2025-09-27""; RULE (Evals/task\_inputs/01\_Universe\_Inject.sql): "A message is anything the game puts on a player" |
| C | 'D1 and D7 for the Sep 15 cohort week on iOS and Android' read as one pooled figure across both platforms. | Same Go/Hold/Drop calls and counts in both readings. | Create the sheet and the one-page note in Samuel's Drive folder, comment and move each ticket, create missing tickets, add the Go checklist to the push notifications card, email each asker except Leonard, post the counts in the DM. | Samuel's Drive folder (d\_caafeec2804b3a67ce46aa); DES tickets; card 6851a769c65dc0017a227bb7; askers' mailboxes; DM D06L58XCVKK. | Same sheet and calls; the note pools the two platform rows by installs (103 Android + 237 iOS = 340): D1 33.53% and D7 9.70%, instead of Android 37.86%/10.68% and iOS 31.65%/9.28%. | DMCOH (Evals/task\_inputs/01\_Universe\_Inject.sql): "start with D1 and D7 for the Sep 15 cohort week on iOS and Android from the warehouse"; SFCOH (/tmp/hgp/snowflake\_extract.json): ""installs": 237" |
| D | 'who actually hears from us' includes players who turned notifications on in settings, since the client schedules for them. | Same Go/Hold/Drop calls and counts in both readings. | Create the sheet and the one-page note in Samuel's Drive folder, comment and move each ticket, create missing tickets, add the Go checklist to the push notifications card, email each asker except Leonard, post the counts in the DM. | Samuel's Drive folder (d\_caafeec2804b3a67ce46aa); DES tickets; card 6851a769c65dc0017a227bb7; askers' mailboxes; DM D06L58XCVKK. | Same sheet and calls; the note says that once players stop playing, those who passed the game's own ask after level 20 and also those who switched notifications on in settings hear the on-phone reminders, following Arthur's code fact rather than the rule doc's test-4 wording. | ARTHUR (Evals/task\_inputs/01\_Universe\_Inject.sql): "NotificationManager only schedules once our own ask has run or they switch it on from settings, on both platforms"; DMNOTE (Evals/task\_inputs/01\_Universe\_Inject.sql): "then who actually hears from us once they stop playing, and the lapsed reminders they get day by day" |

Explicit option inventory: The prompt has no explicit option list; it incorporates Leonard's DM, whose Go/Hold/Drop labels are calls per message, not alternative outcomes for the note.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "His DM to me from yesterday has the whole job in it"

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| No explicit option list | Reviewed | See candidate readings | See inventory evidence |

Compared alternative: B
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. Newer source: the warehouse rows run to 2025-09-27, later than Arthur's June 26 'not using Push notifications yet' and Leonard's Sep 18 'All our PNs are local', and Arthur's Sep 29 line is about NotificationManager only, so it does not deny server pushes. Authority: the rule doc defines a message as anything the game puts on a player's phone while closed, which covers a server push. Source identity and scope: both speak about Zombie Match. No record says the warehouse rows are wrong or stopped. The note's who-hears content therefore differs with nothing to settle it.
Resolution evidence: ARTHUR (Evals/task\_inputs/01\_Universe\_Inject.sql): "NotificationManager only schedules once our own ask has run or they switch it on from settings, on both platforms"; NOPUSH (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/D06KV30TPL4/2025-06.json pointer /41/text): "We aren't using Push notifications yet."; SFLAST (/tmp/hgp/snowflake\_extract.json): ""send\_date": "2025-09-27""; RULE (Evals/task\_inputs/01\_Universe\_Inject.sql): "A message is anything the game puts on a player"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | The calls and counts come from the rule doc tests and do not depend on server pushes. |
| writes | SAME | Both readings make the same writes. |
| destinations | SAME | Both use the same folder, tickets, card, mailboxes and DM. |
| contents | DIFFERENT | Reading A says only players past the level-20 ask hear on-device reminders; Reading B says lapsed and all players also get weekly server pushes (comeback\_7d, daily\_reward, new\_levels). |

Resolution relevance challenge: Arthur's Sep 29 line covers only the client's local scheduling and his June line predates the warehouse sends, so neither rules out the server pushes; the warehouse is the source the DM tells the agent to read.
Delegation challenge: NOT_CLAIMED. Nothing delegates a choice between the two accounts of who hears from us.
Challenge evidence: DMNOTE (Evals/task\_inputs/01\_Universe\_Inject.sql): "then who actually hears from us once they stop playing, and the lapsed reminders they get day by day"; SFCOMEBACK (/tmp/hgp/snowflake\_extract.json): ""campaign\_key": "comeback\_7d""

Compared alternative: C
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. The DM names both platforms but does not say per platform or combined; the warehouse holds one row per platform, so both a per-platform pair and an installs-weighted pooled pair are derivable and nothing ranks them. Two figures (D1 and D7) change, so this is not a single both-fair figure.
Resolution evidence: DMCOH (Evals/task\_inputs/01\_Universe\_Inject.sql): "start with D1 and D7 for the Sep 15 cohort week on iOS and Android from the warehouse"; SFCOH (/tmp/hgp/snowflake\_extract.json): ""installs": 237"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Calls and counts do not change. |
| writes | SAME | Same writes. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Per-platform 37.86%/10.68% and 31.65%/9.28% versus pooled 33.53%/9.70%. |

Resolution relevance challenge: Neither the DM nor the rule doc says how to report two platforms; the table's per-platform grain does not forbid a combined figure.
Delegation challenge: NOT_CLAIMED. No record delegates the choice.
Challenge evidence: DMCOH (Evals/task\_inputs/01\_Universe\_Inject.sql): "start with D1 and D7 for the Sep 15 cohort week on iOS and Android from the warehouse"

Compared alternative: D
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. The rule doc's 'settings toggle doesn't count' is written for test 4 of a message's call; the note asks who actually hears from us, and Arthur says the client also schedules for players who turned notifications on in settings. Nothing says which standard the note uses.
Resolution evidence: RULE4 (Evals/task\_inputs/01\_Universe\_Inject.sql): "A player only counts once our own permission ask has happened"; ARTHUR (Evals/task\_inputs/01\_Universe\_Inject.sql): "NotificationManager only schedules once our own ask has run or they switch it on from settings, on both platforms"

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Calls and counts do not change. |
| writes | SAME | Same writes. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Reading A excludes settings opt-ins; Reading D includes them. |

Resolution relevance challenge: The rule doc line sits inside test 4 and the DM's note request does not point to it.
Delegation challenge: NOT_CLAIMED. No record delegates the choice.
Challenge evidence: RULE4 (Evals/task\_inputs/01\_Universe\_Inject.sql): "A player only counts once our own permission ask has happened"

Strongest-alternative challenge (B): An agent querying the warehouse for D1/D7 lists LIVE\_OPS.EVENTS (described as 'Live-ops events and push campaigns') and its push table answers the note's who-hears question directly, so Reading B is not a strawman.
Challenge evidence: SFPUSH (/tmp/hgp/snowflake\_extract.json): ""audience\_segment": "lapsed""; DMNOTE (Evals/task\_inputs/01\_Universe\_Inject.sql): "then who actually hears from us once they stop playing, and the lapsed reminders they get day by day"

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.


**Feasibility:** PASS (5)
- Every write has a cataloged tool: gsheets_create_spreadsheet + gsheets_values_update, gdocs_create_document, gdrive_move_file, linear_create_comment / linear_update_issue (state, assignee) / linear_create_issue (parentId), trello_create_checklist + trello_create_check_item, gmail_send_message, slack_send_message, snowflake_execute_query. Design team states Backlog, Todo, Canceled and Done exist in base Linear.
- Data exists for every call (code, QA note, tickets, roadmap, Slack). Dimensional: USER_COHORT_RETENTION has `platform` and `cohort_week`; the Sep 15 week's D7 window closed Sep 28, before the clock. Numeric observability: D1/D7 are stored to two decimals; rendering is an evidence limit only.
- Persona ACL: all scoped reads (PN sheet, rule doc, Phone message checks, Beta readiness deck, DMs D06L58XCVKK / D06UFE81RF0 / D06KV30TPL4, #zombie-match3d, #zombie-art, #zombie-bugs, Samuel's mailbox and calendar) are owned by, shared with or joined by Samuel. No ask points outside his view.

**Persona ACL Reachability:** PASS (5)

**Explicit Tool Mention:** PASS (5)

**Clarity & Specificity:** NON-FAIL (3)
- Writes are the same under every reading. The open forks change only the note's contents (who hears from us, pooled vs per-platform D1/D7, settings opt-ins), so this is minor clarity, not Action Decision Ambiguity. No "I'll" delegation statements.

**Contrived / Unnatural:** PASS (5)
- No timestamps, opaque IDs, trap hints, hidden destinations (folder, card and DM are named), audit-form wording or if-chains.

**Alignment with Today's Date:** PASS (5)
- "yesterday" = Sep 30, 2025; the DM is 2025-09-30T20:40:51Z (13:40 PT). Every injected record is before the clock.

**Originality / Sample Similarity:** N/A — no comparison samples supplied (dataset similarity is reported above).

**Truthfulness:** PASS (5)
- All 8 premises verified (record P1–P8): the spend plan and Leonard's request ("about to put more money behind beta", DM), the Sep 30 DM in D06L58XCVKK, "Push Notifications Zombie Match.xlsx" with tab "PNs Beta", Samuel's folder d_caafeec2804b3a67ce46aa, card "[Feature] Push Notifications - Samuel + Leonard", the DM's ticket and email asks, and "tell me here how many Go, Hold and Drop".

**Tool Use & Cross-service:** PASS (5) — Sheets (rows), Linear (asks, audiences, Arthur's feasibility notes), GitHub (what the client schedules), Slack/Gmail (corrections, QA rule) and Snowflake (D1/D7) each change graded facts; many writes.

**Investigation + Action:** PASS (5) — every write depends on the calls the investigation produces.

**Coherence (Bolt-on):** PASS (5)

---

### Phase 3: Universe Feasibility

**Data Existence:**
- Entities verified: 8 of 8 premises, plus every source the requirement ledger needs.
- All retrievable via MCP: Yes.

**Cross-Service Coherence:** FAIL (2)
- Inconsistency in task-touched data: Cross-service Referential. Snowflake base `LIVE_OPS.EVENTS.PUSH_NOTIFICATION_STATS` has 25 `zombie_match_3d` rows, provider "firebase", status "sent", from 2025-04-12 to 2025-09-27: weekly `comeback_7d` winbacks to the `lapsed` segment (PUSH-0000099, 2025-09-06, 275 sent), plus `daily_reward`, `event_live`, `sale_weekend` and `new_levels` (PUSH-0000105, 2025-09-27, 278 sent to all). Persona-visible records say Zombie Match has no server push: Arthur to Samuel, DM D06KV30TPL4, 2025-06-26: "We aren't using Push notifications yet."; Leonard, #zombie-bugs, 2025-09-18: "PNs don't talk to backend" / "All our PNs are local"; and the injected scenario builds on it (Arthur, Sep 29: "NotificationManager only schedules once our own ask has run or they switch it on from settings, on both platforms"; the "needs a server send" comments on DES-329/333/335/340/341). The match3d repo has only local scheduling.
- Why the task depends on it (base-data-v1): the incorporated DM sends the agent to the warehouse and asks the note for "who actually hears from us once they stop playing, and the lapsed reminders they get day by day". The warehouse table answers that question differently from Slack and the code.
- Known base-data issues (not scored): SC-13 (Trello list "BETA: Oct 10" vs actions "BETA: Sep 30") and SC-14 (beta cards' two complete flags). The task grades neither; keep the rubric and OEs off the beta date and card completion flags. PLATFORM:FD-3785: USER_COHORT_RETENTION fills immature cells (Sep 15 week d14, Sep 22 week d7); the task reads only the mature Sep 15 D1/D7. Keep the rubric off d14 and later cohorts.
- Injection SQL considered: Yes.
- Static integrity evidence: REUSED from 0_injection.md (injection-static-v2 PASS, same SQL hash): ID collisions, structure, channel membership, doubled apostrophes. The P3 recheck independently reconfirmed them.
- Prompt-specific sources, access and configuration: supported; no error/async configuration.

---

### Phase 4: Final Evaluation

**Scoring Table:**

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|---|---|---|---|
| Prompt | Unique Ground Truth | 2 | Note's "who hears from us" has two supported answers (warehouse server pushes vs local-only records); two smaller note forks also open |
| Prompt | Feasibility | 5 | All writes cataloged; all data exists and is observable |
| Prompt | Persona ACL Reachability | 5 | Every scoped read visible to Samuel |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 3 | Same writes under every reading; note contents vary |
| Prompt | Contrived / Unnatural | 5 | Natural short request |
| Prompt | Alignment with Today's Date | 5 | "yesterday" = Sep 30 DM |
| Prompt | Originality / Sample Similarity | N/A | No samples supplied |
| Prompt | Truthfulness | 5 | 8/8 premises verified |
| Prompt | Tool Use & Cross-service | 5 | Each service changes graded facts |
| Prompt | Investigation + Action | 5 | Investigation feeds every write |
| Prompt | Coherence (Bolt-on) | 5 | No unrelated ask |
| Prompt | Persona | 5 | Co-owner of push notifications |
| Prompt | Business Function | 5 | Product & Design |
| Prompt | Assigned Competency | 5 | Beta player messaging / GTM |
| Prompt | Assigned Task Skill | 5 | Retrieval is central |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three dimensions load-bearing; short trigger |
| Universe | Data Exists | 5 | All retrievable |
| Universe | Cross-Service Coherence | 2 | Snowflake push stats vs "all our PNs are local", on a topic the note must answer |

---

### Issues Found:

| # | Issue | Severity | Dimension |
|---|---|---|---|
| 1 | Snowflake PUSH_NOTIFICATION_STATS shows weekly Zombie Match Firebase pushes (incl. comeback_7d to lapsed players, latest 2025-09-27) while Slack and the injected records say every Zombie Match message is local; the note must say who hears from us once they stop playing | Major | Cross-Service Coherence; Unique Ground Truth |
| 2 | "D1 and D7 for the Sep 15 cohort week on iOS and Android" can be read per platform (Android 37.86%/10.68%, iOS 31.65%/9.28%) or pooled by installs (33.53%/9.70%) | Minor | Unique Ground Truth / Clarity |
| 3 | "who actually hears from us" can include or exclude players who turned notifications on in settings (the rule doc's "settings toggle doesn't count" is written for test 4) | Minor | Unique Ground Truth / Clarity |

---

### Recommended Improvements:

1. **Issue 1 (must fix).** Snowflake can't be changed by injection, and a line telling the agent to ignore the warehouse wouldn't fix it. Change the scenario so the note no longer asks a question the warehouse answers differently. The simplest fix is to drop "who actually hears from us once they stop playing, and the lapsed reminders they get day by day" from Leonard's DM in your SQL. Keep the D1/D7 part, which reads USER_COHORT_RETENTION and is clean, and replace the dropped part with something your injected records settle on their own. If you keep a who-hears section, the warehouse rows (comeback_7d to lapsed, new_levels and daily_reward to all, through Sep 27) stay a competing answer, and the rubric and OEs can't grade it.
2. **Issue 2.** In the DM, say whether Leonard wants D1/D7 for each platform or combined.
3. **Issue 3.** If a who-hears statement stays in any form, say in the DM whether players who switched notifications on in settings count.
4. Optional hardening (not scored): the Hold-ticket rule rests on Leonard's Sep 29 card comment "Until the beta build is out ... Held work sits in Backlog, unassigned." It holds today because no record says the beta build is out. If you edit that comment, keep it independent of the beta date (SC-13), so a run can't argue the beta already shipped on Sep 30.

After you change the SQL, send the reviews again in this order: /injection, /prompt, /hardness (and later /oe and /rubric).

---

## Deep Recheck

Passes: P1, P2, P3, P4, Opus 5.5 (claude-opus-5-5), each blind to the main review.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 6 prompt sentences, 11 DM sentences, 22 rule-doc lines | 5 | 2 |
| P2 | 6 prompt sentences, 11 DM sentences, 20 rule-doc requirements | 2 | 1 |
| P3 | 6 prompt sentences, 146 SQL statements | 1 | 0 |
| P4 | 6 prompt sentences | 1 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | P2 | "then who actually hears from us once they stop playing" (DM) | Snowflake PUSH_NOTIFICATION_STATS zombie_match_3d rows (PUSH-0000099 comeback_7d lapsed 275; PUSH-0000105 2025-09-27); #zombie-bugs 1758239520.618939 "All our PNs are local" | §3 / Phase 3.2 | Cross-Service Coherence | CONFIRMED | Opened the Snowflake rows and the Slack message; matches the main review's finding |
| DR2 | P2 | "move the ticket to match" (DM) | Trello action 68dae8c7… "Until the beta build is out ... Held work sits in Backlog, unassigned." | §3 / Phase 3.2 | Cross-Service Coherence | REJECTED | No inconsistency: the comment is conditional on a build release, and no record Samuel can see says the beta build is out (a Sep 30 target is not a release). The comment does not rest on the SC-13 list name |
| DR3 | P1 | "move the ticket to match" (DM) | Rule doc "Hold tickets go back to Todo unless the roadmap says otherwise."; card 79 comment | §2 writes | Unique Ground Truth | REJECTED | Card 79 comment, visible to Samuel (Trello unscoped), says "Held work sits in Backlog, unassigned.", which names held work directly |
| DR4 | P1 | "start with D1 and D7 for the Sep 15 cohort week on iOS and Android from the warehouse" (DM) | USER_COHORT_RETENTION 2025-09-15 android 103/37.86/10.68, ios 237/31.65/9.28 | §2 contents | Unique Ground Truth | CONFIRMED | No sentence picks per-platform or pooled; two figures change, so not a both-fair figure |
| DR5 | P1 | "then who actually hears from us once they stop playing" (DM) | Arthur Sep 29 "...or they switch it on from settings, on both platforms"; rule doc "A player only counts once our own permission ask has happened" | §2 contents | Unique Ground Truth | CONFIRMED | The rule doc line is scoped to test 4; nothing says the note uses it |
| DR6 | P1 | "one row per message: ... Audience ..." (DM) | DES-314 "Add your ask as a child with who it's for in a comment."; DES-315…320 "Who it's for: ..." comments | §2 contents | Clarity | REJECTED | Leonard's DES-314 description and his "Who it's for:" comment on every sheet-row ticket settle where the audience lives; the rule doc says "Audience is who the ask says it's for" |
| DR7 | P1 | "and the lapsed reminders they get day by day" (DM) | PN sheet Type "LAPSED" rows; DES-342 "Could we add a reminder on day 3 between the 1 day and 7 day ones." | §2 contents | Clarity | REJECTED | The sheet's LAPSED type and Leonard's own DES-342 wording use "reminders" for the lapsed series; leaderboard and race messages are their own rows |
| DR8 | P3 | SQL column lists (issue_counter, sequence, seq, notes, table_json, ordinal) | Evals/references/schema/injection.json snapshot | SQL columns | Injection advisory | REJECTED | Already an Eval 0 snapshot advisory; changes no graded value (stays in Injection Gate) |
| DR9 | P4 | "He also wants things done on the tickets and some emails sent, so do those too." | DM 6fd96f3c… | 1.3.2 | Coherence | REJECTED | A restatement of DM work on the same job, not an unrelated ask; no bolt-on |

Effect on verdict: Unique Ground Truth gains two minor note forks (DR4, DR5) on top of the main review's fork; Clarity is 3. Cross-Service Coherence (2) and the overall FAIL are unchanged.

- F1: Note "who hears from us once they stop playing" | Reading A: only players past the level-20 ask hear the on-phone reminders (day 1, then days 7/14/21/28) | Reading B: lapsed and all players also get weekly Firebase pushes (comeback_7d, daily_reward, new_levels) per the warehouse | Missing: a dated record Samuel can see that says the warehouse sends are not Zombie Match player pushes or stopped; Snowflake can't be edited, so drop the ask instead
- F2: Note D1/D7 | Reading A: per platform (Android 37.86%/10.68%, iOS 31.65%/9.28%) | Reading B: pooled by installs (33.53%/9.70%) | Missing: a DM sentence saying per platform or combined
- F3: Note "who actually hears" | Reading A: settings opt-ins excluded (rule doc test 4) | Reading B: settings opt-ins included (Arthur's code fact) | Missing: a DM sentence saying whether settings opt-ins count
- F4: Hold ticket state | Reading A: Backlog, unassigned | Reading B: Todo | Settled by: card 79 comment "Held work sits in Backlog, unassigned."
- F5: Audience source for sheet rows | Reading A: "Who it's for" ticket comments | Reading B: sheet Segmentation column | Settled by: DES-314 "Add your ask as a child with who it's for in a comment." and rule doc "Audience is who the ask says it's for."

Platform defects: PLATFORM:FD-3785 (USER_COHORT_RETENTION immature cells; not read by this task's answer)

### FINAL VERDICT: FAIL

Score: 2

Execution status: COMPLETE

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Evaluator model: Opus 5.5 (claude-opus-5-5), effort level not reported by the runtime

Next action: Edit Leonard's Sep 30 DM in the SQL to drop or replace the "who actually hears from us once they stop playing" section and to say per-platform vs combined D1/D7, then rerun /injection, /prompt, /hardness.

Evidence limits: Snowflake evidence was read from verbatim row extracts of the 2.2 GB export (hash recorded) because the evidence reader cannot load the full file; tool rendering of D1/D7 precision is not established by the catalog.

Reviewed prompt SHA-256: 22df2abfec652efab31a87a9cfb74b77632113a98dae00225368f31f29b66ae9
Review context SHA-256: 0d8e2b46c59ebfb2e42c25770b1f9c31afe7e7b041b408bfca7eacf27e089e74
Prompt record SHA-256: 1543f619407b3b965149ffb6d69867ba87a5af6d8865fc9bb6642a3671ddb3b1
Eval version: task-quality-v1
Eval release SHA-256: a6d0d5849af43fa85dc1c2d9bf598b27771ddcb6c23e39cc14c4eba835fe3225

**Lowest Dimension:** Unique Ground Truth / Cross-Service Coherence - 2 - the warehouse's Zombie Match server-push rows contradict the "all our PNs are local" records on exactly the question the note must answer.

**Summary:** The prompt itself is natural, truthful and fits the assignment. The scenario is strong: rule tests, late corrections and a ticket filed under another name. It fails because the note Leonard asks for has to say who hears from us once they stop playing. The warehouse it must read shows weekly Zombie Match Firebase pushes to lapsed players, while Slack and the injected records say every message is local. Drop that ask from the DM and pin per-platform D1/D7, and the rest stands.
