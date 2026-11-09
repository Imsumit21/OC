# 08 OE Check — samuel_zm_beta_messages (beta player messages, injection rev6)
Checked 2026-11-05 · Events 135 · Characters 41196 (300–50,000: ok) · Ledger 2026-11-05 · release task-quality-v1

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

/oe prediction (a prediction only; /oe gives the verdict): PASS 5

Completeness 5 · Accuracy 5 · Path feasibility SUPPORTED · Task solvability SUPPORTED_BY_OE

Checked file: task_inputs/08_Oracle_Events.md (sha256 4924949d7fd3), drafted by plan/assemble_oe_events.py. Before this check ran, the draft was revised for the items under Advisory; this report judges the revised file only.

## Inventory

| Segment (quoted start) | Role | Event |
|---|---|---|
| Read Leonard's DM from yesterday in Slack (Samuel's DM with Leonard Ha… | STEP (read) | OE 1 |
| Read the message rule doc in Drive/Docs (search "rule"; doc "Beta mess… | STEP (read) | OE 2 |
| Read the PNs Beta tab of the Zombie Match PN sheet in Sheets (search "… | STEP (read) | OE 3 |
| List the children of DES-314 in Linear (parent DES-314, from OE 1)… | STEP (read) | OE 4 |
| Read the comments on each of those 31 tickets in Linear (one call per … | STEP (read) | OE 5 |
| Find the live-ops page in Confluence (search "Live-Ops"; page "Live-Op… | STEP (read) | OE 6 |
| Find the Collect & Win ticket in Linear (query "Collect")… | STEP (read) | OE 7 |
| Read the comments on DES-313 in Linear (ticket from OE 7)… | STEP (read) | OE 8 |
| List the Linear tickets updated since the day DES-314 opened, to find … | STEP (read) | OE 9 |
| Read the comments on ZOM-542 in Linear (list from OE 9)… | STEP (read) | OE 10 |
| Read the comments on ZOM-556 in Linear (list from OE 9)… | STEP (read) | OE 11 |
| Read the comments on ZOM-563 in Linear (list from OE 9)… | STEP (read) | OE 12 |
| Read the comments on ZOM-483 in Linear (list from OE 9)… | STEP (read) | OE 13 |
| Read the comments on the other 16 tickets from OE 9 in Linear (one cal… | STEP (read) | OE 14 |
| Search Linear for any other ticket about phone messages (queries "noti… | STEP (read) | OE 15 |
| List the ZM ROADMAP board's lists and their cards in Trello… | STEP (read) | OE 16 |
| Tie Boss Arena to the BETA list in Linear (query "Boss Arena")… | STEP (read) | OE 17 |
| Check that achievements and support have shipped in Linear (queries "A… | STEP (read) | OE 18 |
| Read the card "Fix TECH ISSUES" on the BETA list in Trello (its descri… | STEP (read) | OE 19 |
| Read the card comments on ZM ROADMAP in Trello (board actions, filter … | STEP (read) | OE 20 |
| Search Trello for cards about phone messages (searches "notification" … | STEP (read) | OE 21 |
| Find the push notifications card on ZM ROADMAP in Trello (search "Push… | STEP (read) | OE 22 |
| Read the client's notification code in GitHub (repo match3d, main, pat… | STEP (read) | OE 23 |
| Read the review comments on PR #248 in GitHub (repo match3d, PR number… | STEP (read) | OE 24 |
| Read Vincent's QA note in Gmail (search "Phone messages for beta")… | STEP (read) | OE 25 |
| Read Vincent's checks log in Sheets (search "Phone message checks"; ta… | STEP (read) | OE 26 |
| Find Vincent Parker's Slack user (search users "Vincent")… | STEP (read) | OE 27 |
| Search Slack for what Vincent Parker has posted since Sep 1 (query fro… | STEP (read) | OE 28 |
| Read Vincent's Sep 29 reply in Samuel's DM with him in Slack (in the r… | STEP (read) | OE 29 |
| Search Slack for Robert's permission ask call (search "permission ask"… | STEP (read) | OE 30 |
| Read the replies under Robert's post in Slack (thread from OE 30)… | STEP (read) | OE 31 |
| Search Slack for Leonard's change to the seven-day line (search "taken… | STEP (read) | OE 32 |
| Search Samuel's Google Calendar for the lapsed copy check (search "Lap… | STEP (read) | OE 33 |
| Read the cancelled ladder review in Gmail (search "lapsed"; subject "C… | STEP (read) | OE 34 |
| Search Slack for the Axe Arena decision (search "Axe Arena"; #company-… | STEP (read) | OE 35 |
| Read the retention table's columns in Snowflake (describe ANALYTICS.GA… | STEP (read) | OE 36 |
| Query D1 and D7 for the Sep 15 cohort week in Snowflake (ANALYTICS.GAM… | STEP (read) | OE 37 |
| Find Samuel's Drive folder in Drive (list the root)… | STEP (read) | OE 38 |
| Look up each asker in Contacts (names from OEs 4, 7, 10, 11, 12, 13)… | STEP (read) | OE 39 |
| Apply test 1 to all 36 messages: 14 sheet rows, 18 asks under DES-314 … | STEP (analysis) | OE 40 |
| Apply test 2 to the 31 left (Arthur's Linear notes in OE 5, Douglas's … | STEP (analysis) | OE 41 |
| Apply test 3 to the 25 left (the six GitHub scheduling calls in OE 23,… | STEP (analysis) | OE 42 |
| Apply test 4 to the six the client schedules (Slack in OEs 30 and 31, … | STEP (analysis) | OE 43 |
| Apply test 5 to the five left (GitHub in OEs 23 and 24, Linear in OE 5… | STEP (analysis) | OE 44 |
| Apply test 6 to the four left (Gmail in OE 25, Sheets in OE 26, Slack … | STEP (analysis) | OE 45 |
| Settle the Go rows' headlines (GitHub in OE 23, Slack in OE 32, Calend… | STEP (analysis) | OE 46 |
| Count the calls across the Sheets rows and Linear tickets (OEs 40 to 4… | STEP (analysis) | OE 47 |
| Create the string ticket in Linear (team Design, parent DES-314)… | STEP (write) | OE 48 |
| Create the ticket for Boss Arena attempts refilled in Linear (team Des… | STEP (write) | OE 49 |
| Comment the call on the new Boss Arena attempts refilled ticket in Lin… | STEP (write) | OE 50 |
| Create the ticket for Daily gift about to reset in Linear (team Design… | STEP (write) | OE 51 |
| Comment the call on the new Daily gift about to reset ticket in Linear… | STEP (write) | OE 52 |
| Create the ticket for Teammate sent lives in Linear (team Design, pare… | STEP (write) | OE 53 |
| Comment the call on the new Teammate sent lives ticket in Linear… | STEP (write) | OE 54 |
| Create the ticket for Infinite lives ending in Linear (team Design, pa… | STEP (write) | OE 55 |
| Comment the call on the new Infinite lives ending ticket in Linear… | STEP (write) | OE 56 |
| Create the calls sheet in Sheets… | STEP (write) | OE 57 |
| Write the rows to the calls sheet in Sheets (calls from OEs 40 to 46)… | STEP (write) | OE 58 |
| Move the calls sheet into Samuel's Drive folder in Drive (folder from … | STEP (write) | OE 59 |
| Create the one-page team note in Docs… | STEP (write) | OE 60 |
| Move the note into Samuel's Drive folder in Drive (folder from OE 38)… | STEP (write) | OE 61 |
| Create a checklist on the push notifications card in Trello (card from… | STEP (write) | OE 62 |
| Add Lapsed 1 day to the checklist in Trello (OE 62)… | STEP (write) | OE 63 |
| Add Lapsed 7 days to the checklist in Trello (OE 62)… | STEP (write) | OE 64 |
| Comment the call on DES-313 in Linear… | STEP (write) | OE 65 |
| Comment the call on DES-315 in Linear… | STEP (write) | OE 66 |
| Comment the call on DES-316 in Linear… | STEP (write) | OE 67 |
| Comment the call on DES-317 in Linear… | STEP (write) | OE 68 |
| Comment the call on DES-318 in Linear… | STEP (write) | OE 69 |
| Comment the call on DES-319 in Linear… | STEP (write) | OE 70 |
| Comment the call on DES-320 in Linear… | STEP (write) | OE 71 |
| Comment the call on DES-321 in Linear… | STEP (write) | OE 72 |
| Comment the call on DES-322 in Linear… | STEP (write) | OE 73 |
| Comment the call on DES-323 in Linear… | STEP (write) | OE 74 |
| Comment the call on DES-324 in Linear… | STEP (write) | OE 75 |
| Comment the call on DES-325 in Linear… | STEP (write) | OE 76 |
| Comment the call on DES-326 in Linear… | STEP (write) | OE 77 |
| Comment the call on DES-327 in Linear… | STEP (write) | OE 78 |
| Comment the call on DES-328 in Linear… | STEP (write) | OE 79 |
| Comment the call on DES-329 in Linear… | STEP (write) | OE 80 |
| Comment the call on DES-330 in Linear… | STEP (write) | OE 81 |
| Comment the call on DES-331 in Linear… | STEP (write) | OE 82 |
| Comment the call on DES-332 in Linear… | STEP (write) | OE 83 |
| Comment the call on DES-333 in Linear… | STEP (write) | OE 84 |
| Comment the call on DES-334 in Linear… | STEP (write) | OE 85 |
| Comment the call on DES-335 in Linear… | STEP (write) | OE 86 |
| Comment the call on DES-336 in Linear… | STEP (write) | OE 87 |
| Comment the call on DES-337 in Linear… | STEP (write) | OE 88 |
| Comment the call on DES-338 in Linear… | STEP (write) | OE 89 |
| Comment the call on DES-339 in Linear… | STEP (write) | OE 90 |
| Comment the call on DES-340 in Linear… | STEP (write) | OE 91 |
| Comment the call on DES-341 in Linear… | STEP (write) | OE 92 |
| Comment the call on DES-342 in Linear… | STEP (write) | OE 93 |
| Comment the call on DES-343 in Linear… | STEP (write) | OE 94 |
| Comment the call on DES-344 in Linear… | STEP (write) | OE 95 |
| Comment the call on DES-345 in Linear… | STEP (write) | OE 96 |
| Move DES-313 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 97 |
| Move DES-315 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 98 |
| Move DES-318 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 99 |
| Move DES-319 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 100 |
| Move DES-320 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 101 |
| Move DES-321 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 102 |
| Move DES-322 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 103 |
| Move DES-323 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 104 |
| Move DES-324 to Canceled in Linear… | STEP (write) | OE 105 |
| Move DES-325 to Canceled in Linear… | STEP (write) | OE 106 |
| Move DES-326 to Canceled in Linear… | STEP (write) | OE 107 |
| Move DES-327 to Canceled in Linear… | STEP (write) | OE 108 |
| Move DES-328 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 109 |
| Move DES-329 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 110 |
| Move DES-330 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 111 |
| Move DES-331 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 112 |
| Move DES-332 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 113 |
| Move DES-333 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 114 |
| Move DES-334 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 115 |
| Move DES-335 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 116 |
| Move DES-336 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 117 |
| Move DES-337 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 118 |
| Move DES-338 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 119 |
| Move DES-339 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 120 |
| Move DES-340 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 121 |
| Move DES-341 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 122 |
| Move DES-342 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 123 |
| Move DES-343 to Backlog with no assignee in Linear (OE 19)… | STEP (write) | OE 124 |
| Move DES-344 to Canceled in Linear… | STEP (write) | OE 125 |
| Move DES-345 to Canceled in Linear… | STEP (write) | OE 126 |
| Email Brian Foster in Gmail (address from OE 39)… | STEP (write) | OE 127 |
| Email Calvin Price in Gmail (address from OE 39)… | STEP (write) | OE 128 |
| Email Douglas in Gmail (address from OE 39)… | STEP (write) | OE 129 |
| Email Julia Lawson in Gmail (address from OE 39)… | STEP (write) | OE 130 |
| Email Martin Walsh in Gmail (address from OE 39)… | STEP (write) | OE 131 |
| Email Oliver Brooks in Gmail (address from OE 39)… | STEP (write) | OE 132 |
| Email Owen Baker in Gmail (address from OE 39)… | STEP (write) | OE 133 |
| Email Robert in Gmail (address from OE 39)… | STEP (write) | OE 134 |
| Post the counts in Leonard's DM in Slack (the DM from OE 1, after ever… | STEP (write) | OE 135 |

## Coverage

| R / F | Event(s) | Covered / missing / partial | Route (ledger / other valid) |
|---|---|---|---|
| R1 | OE 1 | covered | ledger route: Slack read of the DM |
| R2 | OE 3 | covered | ledger route: the PNs Beta tab |
| R3 | OE 4, OE 7, OE 9, OE 10–OE 15, OE 20, OE 21 | covered | ledger route: children of the parent, Collect & Win, tickets updated since the parent's day, comment asks, and the census of Linear and Trello |
| R4 | OE 2–OE 47 (46 events) | covered | ledger route: each incorporated record read, then the six tests in order |
| R5 | OE 57, OE 58, OE 59 | covered | ledger route: create, write rows, move into the folder (brief 4b accepts created elsewhere and moved) |
| R6 | OE 60, OE 61 | covered | ledger route: create the Doc, move it |
| R7 | OE 62, OE 63, OE 64 | covered | ledger route: a checklist with the two Go items |
| R8 | OE 65–OE 96 (32 events), plus the four new-ticket comments | covered | ledger route: one comment per ticket |
| R9 | OE 97–OE 126 (30 events) | covered | ledger route: 24 to Backlog unassigned, 6 to Canceled |
| R10 | OE 48, and the four create events from OE 49 | covered | ledger route: string ticket and four new tickets |
| R11 | OE 127–OE 134 (8 events) | covered | ledger route: eight sent emails |
| R12 | OE 135 | covered | ledger route: posted in the same DM, last |
| R13 | the whole set | covered | no event pauses for approval |
| F1 | OE 1 | covered | ledger route |
| F2 | OE 2 | covered | ledger route |
| F3 | OE 3 | covered | ledger route |
| F4 | OE 4 | covered | ledger route |
| F5 | OE 25 | covered | ledger route |
| F6 | OE 26 | covered | ledger route |
| F7 | OE 27 | covered | ledger route |
| F8 | OE 28 | covered | ledger route |
| F9 | — | not required | context: dates the build in Vincent's post; his own post carries the fact |
| F10 | OE 29 | covered | ledger route |
| F11 | OE 30 | covered | ledger route |
| F12 | OE 31 | covered | ledger route |
| F13 | — | not required | superseded version, not on the path |
| F14 | — | not required | superseded version, not on the path |
| F15 | — | not required | superseded reading, not on the path |
| F16 | OE 23 | covered | ledger route |
| F17 | OE 23, OE 3 | covered | ledger route |
| F18 | OE 32 | covered | ledger route |
| F19 | OE 33 | covered | ledger route |
| F20 | OE 24 | covered | ledger route |
| F21 | OE 24 | covered | ledger route |
| F22 | OE 34 | covered | ledger route |
| F23 | OE 6 | covered | ledger route |
| F24 | OE 7, OE 8 | covered | ledger route |
| F25 | OE 16 | covered | ledger route |
| F26 | OE 19 | covered | ledger route |
| F27 | OE 35 | covered | ledger route |
| F28 | — | not required | context for the BETA list, which the roadmap read settles |
| F29 | — | not required | context: the log carries the same versions |
| F30 | OE 36, OE 37 | covered | ledger route |
| F31 | OE 22 | covered | ledger route |
| F32 | OE 38 | covered | ledger route |
| F33 | OE 9, OE 14 | covered | ledger route |
| F34 | OE 10 | covered | ledger route |
| F35 | OE 11 | covered | ledger route |
| F36 | OE 12 | covered | ledger route |
| F37 | OE 13 | covered | ledger route |
| F38 | OE 15, OE 21 | covered | ledger route |
| F39 | OE 20 | covered | ledger route |
| F40 | OE 17, OE 18 | covered | ledger route |
| F41 | OE 8, OE 65, OE 97 | covered | ledger route, with the decision in OE 40–OE 46 |
| F42 | OE 5, OE 66, OE 98 | covered | ledger route, with the decision in OE 40–OE 46 |
| F43 | OE 5, OE 67 | covered | ledger route, with the decision in OE 40–OE 46 |
| F44 | OE 5, OE 68 | covered | ledger route, with the decision in OE 40–OE 46 |
| F45 | OE 5, OE 69, OE 99 | covered | ledger route, with the decision in OE 40–OE 46 |
| F46 | OE 5, OE 70, OE 100 | covered | ledger route, with the decision in OE 40–OE 46 |
| F47 | OE 5, OE 71, OE 101 | covered | ledger route, with the decision in OE 40–OE 46 |
| F48 | OE 5, OE 72, OE 102 | covered | ledger route, with the decision in OE 40–OE 46 |
| F49 | OE 5, OE 73, OE 103 | covered | ledger route, with the decision in OE 40–OE 46 |
| F50 | OE 5, OE 74, OE 104 | covered | ledger route, with the decision in OE 40–OE 46 |
| F51 | OE 5, OE 75, OE 105 | covered | ledger route, with the decision in OE 40–OE 46 |
| F52 | OE 5, OE 76, OE 106 | covered | ledger route, with the decision in OE 40–OE 46 |
| F53 | OE 5, OE 77, OE 107 | covered | ledger route, with the decision in OE 40–OE 46 |
| F54 | OE 5, OE 78, OE 108 | covered | ledger route, with the decision in OE 40–OE 46 |
| F55 | OE 5, OE 79, OE 109 | covered | ledger route, with the decision in OE 40–OE 46 |
| F56 | OE 5, OE 80, OE 110 | covered | ledger route, with the decision in OE 40–OE 46 |
| F57 | OE 5, OE 81, OE 111 | covered | ledger route, with the decision in OE 40–OE 46 |
| F58 | OE 5, OE 82, OE 112 | covered | ledger route, with the decision in OE 40–OE 46 |
| F59 | OE 5, OE 83, OE 113 | covered | ledger route, with the decision in OE 40–OE 46 |
| F60 | OE 5, OE 84, OE 114 | covered | ledger route, with the decision in OE 40–OE 46 |
| F61 | OE 5, OE 85, OE 115 | covered | ledger route, with the decision in OE 40–OE 46 |
| F62 | OE 5, OE 86, OE 116 | covered | ledger route, with the decision in OE 40–OE 46 |
| F63 | OE 5, OE 87, OE 117 | covered | ledger route, with the decision in OE 40–OE 46 |
| F64 | OE 5, OE 88, OE 118 | covered | ledger route, with the decision in OE 40–OE 46 |
| F65 | OE 5, OE 89, OE 119 | covered | ledger route, with the decision in OE 40–OE 46 |
| F66 | OE 5, OE 90, OE 120 | covered | ledger route, with the decision in OE 40–OE 46 |
| F67 | OE 5, OE 91, OE 121 | covered | ledger route, with the decision in OE 40–OE 46 |
| F68 | OE 5, OE 92, OE 122 | covered | ledger route, with the decision in OE 40–OE 46 |
| F69 | OE 5, OE 93, OE 123 | covered | ledger route, with the decision in OE 40–OE 46 |
| F70 | OE 5, OE 94, OE 124 | covered | ledger route, with the decision in OE 40–OE 46 |
| F71 | OE 5, OE 95, OE 125 | covered | ledger route, with the decision in OE 40–OE 46 |
| F72 | OE 5, OE 96, OE 126 | covered | ledger route, with the decision in OE 40–OE 46 |
| F73 | OE 39, OE 127 | covered | ledger route |
| F74 | OE 39, OE 128 | covered | ledger route |
| F75 | OE 39, OE 129 | covered | ledger route |
| F76 | OE 39, OE 130 | covered | ledger route |
| F77 | OE 39, OE 131 | covered | ledger route |
| F78 | OE 39, OE 132 | covered | ledger route |
| F79 | OE 39, OE 133 | covered | ledger route |
| F80 | OE 39, OE 134 | covered | ledger route |
| F81 | OE 47 | covered | ledger route |

## Expected-data sign-off

Every quoted span on every Expected line (224 spans) was re-read in this run against the records its own event cites and found verbatim (whitespace-normalised, `&amp;` read as `&`): seeded rows by parsing 01_Universe_Inject.sql again (never executed), base records through hg.py (plan/oe_reads.py, oe_reads2.py, oe_reads3.py). Unquoted values are listed with their source; decisions and write contents are not_a_claim.

| Event | Claim (quoted) | Source re-read (hg.py pointer) | Value found | Ledger entry (result · quote · evidence_check / not_a_claim) | Match / minor / wrong / unresolved |
|---|---|---|---|---|---|
| OE 1 | "The PN sheet says six are Ready and I don't trust that." (+9 more quoted spans re-read) | D06L58XCVKK/1759264851.763895, SQL L45 | found verbatim | F1 · VERIFIED | match |
| OE 2 | "A message is anything the game puts on a player's phone while the game is closed…" (+15 more quoted spans re-read) | f_dc45e0e5a8b8635c1b82b2, SQL L13 | found verbatim | F2 · VERIFIED | match |
| OE 3 | "Revisit once new quests roll out." (+28 more quoted spans re-read) | f_a325dd4af80afc5994d5dc, hg.py gsheets data.json /sheets_spreadsheets/220/sheets/1/grid | found verbatim | F3 · VERIFIED | match |
| OE 4 | "Built in match3d #248." (+3 more quoted spans re-read) | SQL L108 to L170 (linear_issues DES-314 to DES-345), seeded rows | found verbatim | F4 · VERIFIED | match |
| OE 5 | "Who it's for: everyone. Rollover on the sheet is wrong for this one, it goes whe…" (+61 more quoted spans re-read) | SQL L176 to L298 (linear_comments on DES-315 to DES-345) | found verbatim | F4 · VERIFIED | match |
| OE 6 | "Live; algo bug Aug 2025" (+3 more quoted spans re-read) | page_liveops_calendar, hg.py confluence confluence_working.json /pages/27 | found verbatim | F23 · VERIFIED | match |
| OE 7 | "Ping when a Collect & Win window opens" (+1 more quoted spans re-read) | DES-313, SQL L107 | found verbatim | F24 · VERIFIED | match |
| OE 8 | "for players on the event" (+1 more quoted spans re-read) | DES-313, SQL L173, L175 | found verbatim | F24 · VERIFIED | match |
| OE 9 | Besides DES-313, DES-314 and its 31 children, 20 tickets, all Zombie Match 3D: ZOM-112, ZO | hg.py linear data.json /issues key updated_at (scan complete), SQL L308 to L311 | value re-read | F33 · VERIFIED | match |
| OE 10 | "Update home screen and victory score screen for game modes" (+1 more quoted spans re-read) | cmt_f1b8a109dfa70cdc4565, SQL L303, ZOM-542, hg.py linear data.json /issues | found verbatim | F34 · VERIFIED | match |
| OE 11 | "When the daily gift is skipped, it doesn't reset to 0." (+1 more quoted spans re-read) | cmt_2b519285937e7fa79453, SQL L305, ZOM-556, hg.py linear data.json /issues | found verbatim | F35 · VERIFIED | match |
| OE 12 | "Teams' lives, golden frames and names not working on prod env" (+1 more quoted spans re-read) | cmt_eabac5435f2b3a575aad, SQL L307, ZOM-563, hg.py linear data.json /issues | found verbatim | F36 · VERIFIED | match |
| OE 13 | "Infinite lives from new-install are not granted, rewards 30 min in the next sess…" (+1 more quoted spans re-read) | cmt_e2e2926a2080ca53c4ea, SQL L301, ZOM-483, hg.py linear data.json /issues | found verbatim | F37 · VERIFIED | match |
| OE 14 | Each returns an empty comment list. | hg.py linear data.json /comments (empty array), SQL comment rows | value re-read | F33 · VERIFIED | match |
| OE 15 | "notification" (+10 more quoted spans re-read) | hg.py linear data.json /issues (scan complete, 30 'notification' hits) | found verbatim | F38 · VERIFIED | match |
| OE 16 | "BETA: Oct 10" (+11 more quoted spans re-read) | hg.py trello data.json /cards and /lists | found verbatim | F25 · VERIFIED | match |
| OE 17 | "Infinite HP Boss Arena" | ZOM-487, hg.py linear data.json /issues/3558 | found verbatim | F40 · VERIFIED | match |
| OE 18 | "Quest and Achievements UI" (+2 more quoted spans re-read) | ZOM-116, ZOM-363, ZOM-301, hg.py linear data.json /issues | found verbatim | F40 · VERIFIED | match |
| OE 19 | "Until the beta build is out nothing that isn't beta work lands in anyone's Todo.…" | 68dae8c7d95e24b55b69bf80, SQL L54 | found verbatim | F26 · VERIFIED | match |
| OE 20 | "Samuel says 3 days." | hg.py trello data.json /actions type commentCard, 68d415a716abcb84070a8e2a | found verbatim | F39 · VERIFIED | match |
| OE 21 | "[Feature] Push Notifications - Samuel + Leonard" (+9 more quoted spans re-read) | hg.py trello data.json /cards and /boards (scan complete) | found verbatim | F38 · VERIFIED | match |
| OE 22 | "[Feature] Push Notifications - Samuel + Leonard" (+1 more quoted spans re-read) | 6851a769c65dc0017a227bb7, 68d415a716abcb84070a8e2a, SQL L51 | found verbatim | F31 · VERIFIED | match |
| OE 23 | "DailyNotifications(OneDayLapsedTitle, OneDayLapsedMessage, serverToday);" (+9 more quoted spans re-read) | harmonygames-Games/match3d#248, hg.py github data.json /review_comments/599/diff_hunk | found verbatim | F16 · VERIFIED | match |
| OE 24 | "This counts seven days from the day they last left the game, so it isn't tied to…" | harmonygames-Games/match3d#248#rc_18, SQL L92 | found verbatim | F20 · VERIFIED | match |
| OE 25 | "Seen only counts on a store build, on a real iOS device and a real Android devic…" (+3 more quoted spans re-read) | samuel.turner@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com>, SQL L63 | found verbatim | F5 · VERIFIED | match |
| OE 26 | "phone date moved forward" (+3 more quoted spans re-read) | f_8eb8c04713ff6a6ef4a265, SQL L19 | found verbatim | F6 · VERIFIED | match |
| OE 27 | Vincent Parker, user id EMPLOYEE_0012_SLACK_ID. | hg.py slack users.json | value re-read | F7 · VERIFIED | match |
| OE 28 | "on 0.3.49 the Full Ammo one didn't show up after a full refill, tried it twice o…" | C0880U9751A/1759245146.720608, SQL L43 | found verbatim | F8 · VERIFIED | match |
| OE 29 | "also on the race one I passed: that iPhone was still on the 5-minute timers buil…" | D06UFE81RF0/1759174846.723833, SQL L40 | found verbatim | F10 · VERIFIED | match |
| OE 30 | "Permission ask for beta: leaving our own ask after level 20, not pushing it furt…" | C0880U9751A/1759167608.326578, SQL L33 | found verbatim | F11 · VERIFIED | match |
| OE 31 | "that popup doesn't switch anything on btw. NotificationManager only schedules on…" | C0880U9751A/1759170096.924778, SQL L35 | found verbatim | F12 · VERIFIED | match |
| OE 32 | "random one while I'm here: the 'taken over' push reads like we've given up. make…" (+1 more quoted spans re-read) | C08R8CHB0QL/1759169129.445834, SQL L37 | found verbatim | F18 · VERIFIED | match |
| OE 33 | "Went through the lapsed lines with Martin Walsh after this. Final for the 7 day …" (+1 more quoted spans re-read) | evt_f2c03e69f50acf62c9d1c3, SQL L88 | found verbatim | F19 · VERIFIED | match |
| OE 34 | "Cancelled, no need. The weekly one repeats for four weeks, so day 14 is already …" | samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com>, SQL L77 | found verbatim | F22 · VERIFIED | match |
| OE 35 | "We’ve decided to postpone Axe Arena for the beta release." | C05KNDCHAAG/1758558164.541689, hg.py slack messages/C05KNDCHAAG/2025-09.json | found verbatim | F27 · VERIFIED | match |
| OE 36 | "% returning on Day 1" (+1 more quoted spans re-read) | hg.py snowflake.json /tables/10/columns/4 and /5 | found verbatim | F30 · VERIFIED | match |
| OE 37 | Two rows. ios: installs 237, d1_ret 31.65, d7_ret 9.28. android: installs 103, d1_ret 37.8 | snowflake.json /tables/10/rows/236 and /237, hg.py get | value re-read | F30 · VERIFIED | match |
| OE 38 | "samuel.turner@harmonygames.co" | d_caafeec2804b3a67ce46aa, hg.py gdrive data.json /drive_files/18381 | found verbatim | F32 · VERIFIED | match |
| OE 39 | Brian Foster: brian.foster@harmonygames.co; Calvin Price: calvin.price@harmonygames.co; Do | hg.py contacts contacts.json /contacts email fields | value re-read | F80 · VERIFIED | match |
| OE 40 | "A reward on tap is a version 2 idea, it isn't in the beta." (+4 more quoted spans re-read) | hg.py and SQL rows cited by the event's named OEs | found verbatim | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 41 | Six need a server send, so Hold, test 2: Endless weekly result (DES-329); Season Pass prem | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 42 | The client schedules six: Lives recharged, Finish first mission, Lapsed 1 day, Lapsed 7 da | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 43 | "Level 20 not completed" | hg.py and SQL rows cited by the event's named OEs | found verbatim | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 44 | "Daily is fine for this one, there's always a race on." | hg.py and SQL rows cited by the event's named OEs | found verbatim | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 45 | "the lapsed ones are still coming through" | hg.py and SQL rows cited by the event's named OEs | found verbatim | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 46 | "The Horde Is Growing…" (+3 more quoted spans re-read) | hg.py and SQL rows cited by the event's named OEs | found verbatim | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 47 | 36 messages: Go 2, Hold 28, Drop 6. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 48 | "Your Squad Is Waiting" | hg.py and SQL rows cited by the event's named OEs | found verbatim | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 49 | A new ticket for Boss Arena attempts refilled, for players who used their attempts, naming | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 50 | A comment saying Hold, test 3: the client doesn't schedule it yet. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 51 | A new ticket for Daily gift about to reset, for players on a gift streak, naming the ask o | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 52 | A comment saying Hold, test 3: the client doesn't schedule it yet. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 53 | A new ticket for Teammate sent lives, for players on a team, naming the ask on ZOM-563. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 54 | A comment saying Hold, test 2: it needs a server send. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 55 | A new ticket for Infinite lives ending, for players with infinite lives running, naming th | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 56 | A comment saying Hold, test 3: the client doesn't schedule it yet. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 57 | A new native spreadsheet with a name about the beta messages. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 58 | Header Message, Ticket, Call, What's missing, Audience, Final headline, String change, the | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 59 | The sheet's parent is d_caafeec2804b3a67ce46aa. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 60 | A Doc that opens with D1 and D7 for the Sep 15 cohort week: iOS D1 31.65%, D7 9.28%; Andro | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 61 | The Doc's parent is d_caafeec2804b3a67ce46aa. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 62 | A new checklist on card 6851a769c65dc0017a227bb7. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 63 | A check item naming Lapsed 1 day. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 64 | A check item naming Lapsed 7 days. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 65 | A comment on DES-313 (Win & Collect start) saying Hold, test 3: the client doesn't schedul | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 66 | A comment on DES-315 (Lives recharged) saying Hold, test 6: Vincent's tick is off after 0. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 67 | A comment on DES-316 (Lapsed 1 day) saying Go. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 68 | "Your Squad Is Waiting" | hg.py and SQL rows cited by the event's named OEs | found verbatim | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 69 | A comment on DES-318 (Finish first mission) saying Hold, test 4: it can't reach its player | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 70 | A comment on DES-319 (Plague Race) saying Hold, test 6: the iOS pass was on the 5-minute t | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 71 | A comment on DES-320 (Weekly Leaderboard reset) saying Hold, test 5: it fires on the wrong | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 72 | A comment on DES-321 (Quests rollover) saying Hold, test 3: the client doesn't schedule it | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 73 | A comment on DES-322 (Login Calendar update) saying Hold, test 3: the client doesn't sched | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 74 | A comment on DES-323 (Season Pass start) saying Hold, test 3: the client doesn't schedule  | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 75 | A comment on DES-324 (Hourly Coins) saying Drop, test 1: it isn't in the beta. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 76 | A comment on DES-325 (Nathan's Treasure Hunt) saying Drop, test 1: it isn't in the beta. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 77 | A comment on DES-326 (Streak Fever) saying Drop, test 1: it isn't in the beta. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 78 | A comment on DES-327 (Axe Arena) saying Drop, test 1: it isn't in the beta. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 79 | A comment on DES-328 (Endless entries back) saying Hold, test 3: the client doesn't schedu | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 80 | A comment on DES-329 (Endless weekly result) saying Hold, test 2: it needs a server send. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 81 | A comment on DES-330 (Boss Arena open) saying Hold, test 3: the client doesn't schedule it | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 82 | A comment on DES-331 (Boss Arena last hours) saying Hold, test 3: the client doesn't sched | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 83 | A comment on DES-332 (Season Pass last 48 hours) saying Hold, test 3: the client doesn't s | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 84 | A comment on DES-333 (Season Pass premium nudge) saying Hold, test 2: it needs a server se | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 85 | A comment on DES-334 (Plague Race last hour) saying Hold, test 3: the client doesn't sched | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 86 | A comment on DES-335 (Plague Race result) saying Hold, test 2: it needs a server send. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 87 | A comment on DES-336 (Zombie Lane reward ready) saying Hold, test 3: the client doesn't sc | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 88 | A comment on DES-337 (Achievement reward waiting) saying Hold, test 3: the client doesn't  | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 89 | A comment on DES-338 (Daily chest ready) saying Hold, test 3: the client doesn't schedule  | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 90 | A comment on DES-339 (Free shop coins ready) saying Hold, test 3: the client doesn't sched | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 91 | A comment on DES-340 (Support reply waiting) saying Hold, test 2: it needs a server send. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 92 | A comment on DES-341 (New levels added) saying Hold, test 2: it needs a server send. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 93 | A comment on DES-342 (Lapsed 3 days) saying Hold, test 3: the client doesn't schedule it y | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 94 | A comment on DES-343 (Lapsed 30 days) saying Hold, test 3: the client doesn't schedule it  | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 95 | A comment on DES-344 (Lapsed 14 days) saying Drop: Lapsed 7 days already covers it. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 96 | A comment on DES-345 (Comeback gift) saying Drop, test 1: it isn't in the beta. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 97 | DES-313 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 98 | DES-315 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 99 | DES-318 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 100 | DES-319 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 101 | DES-320 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 102 | DES-321 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 103 | DES-322 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 104 | DES-323 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 105 | DES-324 state Canceled. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 106 | DES-325 state Canceled. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 107 | DES-326 state Canceled. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 108 | DES-327 state Canceled. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 109 | DES-328 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 110 | DES-329 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 111 | DES-330 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 112 | DES-331 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 113 | DES-332 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 114 | DES-333 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 115 | DES-334 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 116 | DES-335 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 117 | DES-336 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 118 | DES-337 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 119 | DES-338 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 120 | DES-339 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 121 | DES-340 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 122 | DES-341 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 123 | DES-342 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 124 | DES-343 state Backlog, assignee empty. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 125 | DES-344 state Canceled. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 126 | DES-345 state Canceled. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 127 | A sent email to brian.foster@harmonygames.co saying what happened to their asks: Endless e | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 128 | A sent email to calvin.price@harmonygames.co saying what happened to their asks: Daily che | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 129 | A sent email to douglas@harmonygames.co saying what happened to their asks: Teammate sent  | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 130 | A sent email to julia.lawson@harmonygames.co saying what happened to their asks: Plague Ra | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 131 | A sent email to martin.walsh@harmonygames.co saying what happened to their asks: Free shop | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 132 | A sent email to oliver.brooks@harmonygames.co saying what happened to their asks: Season P | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 133 | A sent email to owen.baker@harmonygames.co saying what happened to their asks: Zombie Lane | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 134 | A sent email to robert@harmonygames.co saying what happened to their asks: Boss Arena open | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |
| OE 135 | A message in that DM saying Go 2, Hold 28, Drop 6. | hg.py and SQL rows cited by the event's named OEs | value re-read | not_a_claim (a value the write creates, or a decision over earlier events) | match |

## Findings

No defect found in the current file: no INCOMPLETE, INACCURATE, MINOR, non-action, final-response or format finding. The independent review's items and the pre-check revisions are recorded under Advisory with their dispositions.

## Pre-verdict sweep

| Eval 4.0 check (7) | Result |
|---|---|
| One wrong count, ID, channel or tool | none: counts recomputed (36 messages, 14 + 18 + 4; Go 2, Hold 28, Drop 6; 31 children; 20 tickets; 13 card comments) from solver/truth.json and the records; every read and write maps to a cataloged tool (Evals/references/tools/catalog.json) |
| One missing write | none: every write family in ledger §C (08_OE_Writing_Ledger.md) has its events, one write per event, OE 48 to OE 135 |
| One Expected fact with no retrieving event | none: each value an Expected line uses is read by that event or an earlier one it names (Coverage rows above) |
| One unledgered Expected value or unbacked absence word | none: 224 quoted spans re-read against each event's own records; absence words are backed by complete scans (F33, F38, F39) |
| One act-vs-defer conflict | none: ledger §C defer search complete (Slack, Gmail, Linear, Trello), Leonard's Sep 30 DM (D06L58XCVKK/1759264851.763895) is the latest instruction |
| One non-action or final-response event | none: no event describes the final response or a thing not done; the Go tickets simply have no move event |
| One prompt-forbidden or reserved write | none: 04_Prompt.txt reserves nothing ('You don't need to run anything by me first'); Leonard gets no email, as the DM says |
| One missing recovery or wait event | none: 03_Error_Async_Config.txt is Friction: none |

## Advisory (no effect on the prediction)

| Event | Note |
|---|---|
| OE 40 | Pre-check revision (independent review #1, confirmed): free shop coins were called a BETA-list item. The shop card is about inventory; DES-339 says 'We already give free coins in the shop.' (SQL L159). The basis now quotes that line, carried in OE 4. |
| OE 40 | Pre-check revision (independent review #2, confirmed): 'the lapsed messages' were called client-scheduled, but DES-342 and DES-343 say 'not in NotificationManager yet'. It now names Lapsed 1 day and Lapsed 7 days in the client and the other three as the same feature; GitHub added to the sources. |
| OE 19 | Pre-check revision (independent review #3, confirmed): Leonard's authorship sits on the updateCard action (SQL L54, trello /members/2), which a card read does not return. See the recheck row: the event no longer states the author. |
| OE 18 | Pre-check revision (independent review #4, confirmed): ZOM-314 says the button 'will be used when' Helpshift is implemented, so it does not show support shipped. ZOM-301 'Helpshift Implementation', Done (linear /issues/3356), now carries Support reply waiting at test 1. |
| OE 40 | Pre-check revision (independent review #5, confirmed): 'the daily login' had no source. DES-322's 'Daily login is already in the game.' (SQL L125) and DES-321's 'Quests are already in production.' now carry those rows. |
| OE 17 | Pre-check revision (independent review #6, confirmed): the heading said the BETA list leaves Boss Arena out; it is on the list. Reworded to tie it to the card. |
| OE 24 | Pre-check revision (independent review #7, #8, #9, confirmed): the PR number now comes from OE 4 ('Built in match3d #248.'); the merged date, which a comments read does not return, is gone; the comment is placed on BatchScheduleWeeklyLeaderboardNotifications, as its diff hunk ends there (SQL L92). |
| OE 27 | Pre-check revision (independent review #10, confirmed): a new event produces Vincent's Slack user id (slack users.json) before the search that uses it. |
| OE 23 | Pre-check revision (independent review #11, #17, #26, confirmed): the separate level-constant event and the level-gate sentence are gone, because test 4 rests on DES-318 and the sheet's Segmentation cell. The four titles now sit behind 'Titles include' and are quoted from the hunk read through hg.py, so no Expected value depends on a repository blob. |
| OE 32 | Pre-check revision (independent review #12, confirmed): a search does not return the parent post, so the Martin Walsh label is gone. |
| OE 3 | Pre-check revision (independent review #13, #14, confirmed): the twin sheet sentence, which no event read, is gone; rows now show the tab's own Details column instead of message names it does not hold. |
| OE 16, OE 6 | Pre-check revision (independent review #15, #16, confirmed): partial rundowns now say 'among others' and 'Among the event rows'. |
| OE 15, OE 21 | Pre-check revision (independent review #18, #19, confirmed): the Linear search now covers three terms, and a new Trello event covers cards, so 'a ticket or a card' is searched on both sides. The reviewer's own sweep of all 3,687 issues and 803 cards found no further ask. |
| OE 37, OE 60 | Pre-check revision (independent review #20, confirmed): percent added. |
| OE 58 | Pre-check revision (independent review #21, #22, confirmed): the row event now covers What's missing on Go and Drop rows, and accepts the sheet's or the ticket's name or a short form. |
| OE 7, OE 8, OE 17, OE 18 | Pre-check revision (independent review #23, a format risk): the find-and-read and multi-lookup events are split. Population reads stay one event each, as gate 14 allows. |
| OE 9 | Independent review #24, kept: updatedAt and orderBy are cataloged parameters of linear_list_issues (Evals/references/tools/linear-tools.json) and the records carry updated_at, but 0 of 27 baseline list calls used them. limit 100 added, since the filtered call returns 53 rows. createdAt behaved as a since filter in run-2. |
| OE 24 | Independent review #25, kept: github_get_pull_request_comments is cataloged but no run called it, so the event also offers the same comment in Samuel's Gmail (SQL L69), a branch that completes the step alone. |
| OE 10 to OE 14 | Independent review note, kept: linear_list_comments was never called on a ZOM ticket in a run. It worked on every DES ticket, and issueId is its one required parameter. |
| OE 49 | Independent review note, kept: linear_create_issue was run with state Todo, not Backlog. state is a cataloged parameter and linear_update_issue reached Backlog in every run. |
| all | Size: 135 events, about 41,000 characters, to be typed by hand (the field blocks pasting). Each write is its own event by the one-write rule. |
| OE 19 | Recheck: trello_get_card_actions, the first fix for review #3, was never called in a run. The event no longer needs it: the author claim is gone, because the roadmap's text is the authority, and the date is the card's dateLastActivity, which trello_get_lists returned in run-5 (event 46). |
| OE 21 | Recheck: three of the six cards are closed, so the event now sets cards_filter all, as every baseline search that returned all seven did; 'reminder' added, 0 hits (scan complete). |
| OE 15 | Recheck: 'phone message' dropped, since it has 0 hits as a phrase and its words would read as unrelated matches; the Expected line reports every query it names. |
| OE 24 | Recheck: the Gmail copy does not name the method, so the batch is now stated as what GitHub shows. The comment text is the same on both routes. |
| OE 36 | Recheck: a query does not return the unit, so a describe event now reads the column comments: d1_ret '% returning on Day 1'. |
| OE 40 | Recheck: Daily chest ready now rests on Arthur's 'the chest timer is local' (SQL L157 and its note), not on Julia's quote about the streak; the source list now names every event it quotes. |

## Tally

Blocking 0 (incomplete 0 · inaccurate 0 · length 0) · moderate 0 (non-action 0 · final-response 0 · format 0) · minor 0 · unresolved 0 · advisory 27

## Self-review

Re-read as the eval: walked Evals/2_Oracle_Events_Eval.md 1.2 (inventory), 1.3 (five fields per STEP), the HARD GATE (no non-action or final-response event), 2.1–2.7 (service, tool, parameters, expected data, visibility, authority, act-vs-defer, format), 3.1–3.6 (completeness) and 4.0 (the sweep above) in order against the file.

Re-verified: every quoted span (224) re-read in this run against its own event's records by plan/assemble_oe_check.py (SQL parsed again, base through hg.py get and search); counts recomputed. No Expected value rests on a repository blob: the client lines and titles are quoted from the PR hunk read through hg.py, and run-5 event 117 shows the same call sites on main (ledger §F 4).

Five fields: every event names its action and service in the heading, its parameters (search text, title, list, path, recipient) in the heading, the information and expected data on its Expected line, and its dependency as an 'OE n' pointer where it needs an earlier value. The eight decision events name the services they draw on.

Independent review: one general-purpose reviewer, given the file, the prompt, the SQL and the rules, but not the ledger, brief, solver, dossier or this report, read the events against the SQL rows and the base through hg.py. It reached the same 36 calls on its own (Go 2, Hold 28, Drop 6), found no missing population member or write and no unauthorised write, and confirmed every quoted string, timestamp and weekday it could reach. It raised 26 items; each was checked against its record, and all are fixed or kept with a reason under Advisory. It then re-read the rewritten events and raised eight small items, none changing a call; all are fixed or kept below.

Path notes: OE 9 rests on the catalog's updatedAt parameter, which no run exercised; OE 24 on github_get_pull_request_comments, which no run called; OE 34 on a mail that appeared in Gmail results in run-3, run-4 and run-5 but that no run opened. Each is a cataloged tool reading a record the persona can see, so the path is SUPPORTED on the catalog and the records, not on a run that took it (ledger §F 1, §F 4); OE 24 also offers Samuel's Gmail copy.

Counter-readings, one per Coverage row and Findings row:

| Item | Counter-reading and resolution (evidence) |
|---|---|
| R1 | Counter-reading — COVERED → best case missing: the DM could be another Leonard message; OE 1 pins the Sep 30 message that names the PN sheet and the job (D06L58XCVKK/1759264851.763895, F1) |
| R2 | Counter-reading — COVERED → best case missing: the sheet could mean every tab or the Domino twin; OE 3 names the PNs Beta tab, which the DM names (F3) |
| R3 | Counter-reading — COVERED → best case missing: the population could stop at the 18 asks under DES-314; OE 9 and the four comment events take in the asks on ZOM-542, ZOM-556, ZOM-563 and ZOM-483, and OE 15 and OE 20 show nothing else is filed (F33, F38, F39) |
| R4 | Counter-reading — COVERED → best case missing: a test could be skipped or read out of order; OE 40 to OE 45 run the six tests in turn, and each count follows from the last (36, 31, 25, 6, 5, 4; F2) |
| R5 | Counter-reading — COVERED → best case missing: the sheet could stay outside the folder; OE 59 moves it into d_caafeec2804b3a67ce46aa (F32) |
| R6 | Counter-reading — COVERED → best case missing: the note could leave out one of the three parts the DM asks for; OE 60 states all three, with four Holds (F30, F16, F81) |
| R7 | Counter-reading — COVERED → best case missing: Holds could go on the checklist; OE 63 and OE 64 add the two Go messages only, and the DM says 'Every Go' (F31) |
| R8 | Counter-reading — COVERED → best case missing: Go tickets could be skipped; the 32 comment events include DES-316 and DES-317, because the DM says 'each ticket' (F1) |
| R9 | Counter-reading — COVERED → best case missing: Hold tickets could go to Todo; OE 19 reads the roadmap note that overrides it, and each Hold event names Backlog with no assignee (F26) |
| R10 | Counter-reading — COVERED → best case missing: Win & Collect could get a new ticket; OE 7 finds DES-313 and the create events cover only the four asks and the string ticket (F24) |
| R11 | Counter-reading — COVERED → best case missing: Douglas could be missed, or Leonard emailed; the eight email events include douglas@harmonygames.co, and the DM says 'apart from me' (F75) |
| R12 | Counter-reading — COVERED → best case missing: the counts could go out before the writes finish; OE 135 is the last event and says so (F81) |
| R13 | Counter-reading — COVERED → best case missing: a step could wait for Samuel's approval; no event does, and the prompt says 'You don't need to run anything by me first' (04_Prompt.txt, F1) |
| F1 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 1 states it, re-read in this run (F1) |
| F2 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 2 states it, re-read in this run (F2) |
| F3 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 3 states it, re-read in this run (F3) |
| F4 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 4 states it, re-read in this run (F4) |
| F5 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 25 states it, re-read in this run (F5) |
| F6 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 26 states it, re-read in this run (F6) |
| F7 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 27 states it, re-read in this run (F7) |
| F8 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 28 states it, re-read in this run (F8) |
| F9 | Counter-reading — NOT REQUIRED → best case required: a reviewer could expect a step for it; resolved: context: dates the build in Vincent's post; his own post carries the fact (F9) |
| F10 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 29 states it, re-read in this run (F10) |
| F11 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 30 states it, re-read in this run (F11) |
| F12 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 31 states it, re-read in this run (F12) |
| F13 | Counter-reading — NOT REQUIRED → best case required: a reviewer could expect a step for it; resolved: superseded version, not on the path (F13) |
| F14 | Counter-reading — NOT REQUIRED → best case required: a reviewer could expect a step for it; resolved: superseded version, not on the path (F14) |
| F15 | Counter-reading — NOT REQUIRED → best case required: a reviewer could expect a step for it; resolved: superseded reading, not on the path (F15) |
| F16 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 23 states it, re-read in this run (F16) |
| F17 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 23 states it, re-read in this run (F17) |
| F18 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 32 states it, re-read in this run (F18) |
| F19 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 33 states it, re-read in this run (F19) |
| F20 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 24 states it, re-read in this run (F20) |
| F21 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 24 states it, re-read in this run (F21) |
| F22 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 34 states it, re-read in this run (F22) |
| F23 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 6 states it, re-read in this run (F23) |
| F24 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 7 states it, re-read in this run (F24) |
| F25 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 16 states it, re-read in this run (F25) |
| F26 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 19 states it, re-read in this run (F26) |
| F27 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 35 states it, re-read in this run (F27) |
| F28 | Counter-reading — NOT REQUIRED → best case required: a reviewer could expect a step for it; resolved: context for the BETA list, which the roadmap read settles (F28) |
| F29 | Counter-reading — NOT REQUIRED → best case required: a reviewer could expect a step for it; resolved: context: the log carries the same versions (F29) |
| F30 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 36 states it, re-read in this run (F30) |
| F31 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 22 states it, re-read in this run (F31) |
| F32 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 38 states it, re-read in this run (F32) |
| F33 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 9 states it, re-read in this run (F33) |
| F34 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 10 states it, re-read in this run (F34) |
| F35 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 11 states it, re-read in this run (F35) |
| F36 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 12 states it, re-read in this run (F36) |
| F37 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 13 states it, re-read in this run (F37) |
| F38 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 15 states it, re-read in this run (F38) |
| F39 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 20 states it, re-read in this run (F39) |
| F40 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 17 states it, re-read in this run (F40) |
| F41 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 8 states it, re-read in this run (F41) |
| F42 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F42) |
| F43 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F43) |
| F44 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F44) |
| F45 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F45) |
| F46 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F46) |
| F47 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F47) |
| F48 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F48) |
| F49 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F49) |
| F50 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F50) |
| F51 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F51) |
| F52 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F52) |
| F53 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F53) |
| F54 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F54) |
| F55 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F55) |
| F56 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F56) |
| F57 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F57) |
| F58 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F58) |
| F59 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F59) |
| F60 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F60) |
| F61 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F61) |
| F62 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F62) |
| F63 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F63) |
| F64 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F64) |
| F65 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F65) |
| F66 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F66) |
| F67 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F67) |
| F68 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F68) |
| F69 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F69) |
| F70 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F70) |
| F71 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F71) |
| F72 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 5 states it, re-read in this run (F72) |
| F73 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 39 states it, re-read in this run (F73) |
| F74 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 39 states it, re-read in this run (F74) |
| F75 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 39 states it, re-read in this run (F75) |
| F76 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 39 states it, re-read in this run (F76) |
| F77 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 39 states it, re-read in this run (F77) |
| F78 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 39 states it, re-read in this run (F78) |
| F79 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 39 states it, re-read in this run (F79) |
| F80 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 39 states it, re-read in this run (F80) |
| F81 | Counter-reading — COVERED → best case missing: the event names the record but not its deciding value; resolved: OE 47 states it, re-read in this run (F81) |

Unresolved: none blocking.

```
STAGE GATE oe-check: PASS — Task_Authoring/task_inputsK · 08_OE_Check.md#1e89ed8b4870 · 08_Oracle_Events.md#9f51886819df · 08_OE_Writing_Ledger.md#4438df7b4046 · __context__#72168f70a409 · __assignment__#3adec6ac02d7 · __policy__#dc4ab5df3cdd · __gate_policy__#115714063000 · __review__#95f1481dfb3c · blocking 0 · warnings 0 · checks 20
[PASS] assignment.v3_context: Samuel Turner / Game Designer; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 08_OE_Check.md
[PASS] structure.inputs: 2 input(s) present: 08_Oracle_Events.md, 08_OE_Writing_Ledger.md
[PASS] structure.fresh: every output newer than its inputs (08_Oracle_Events.md, 08_OE_Writing_Ledger.md)
[PASS] chain.oe-writing: upstream 'oe-writing' PASS pasted and current (08_OE_Writing_Ledger.md#4438df7b4046, 00_Assigments.md#55f6d8057880, 04_Prompt.txt#c3f8859dd772, 01_Grounding_Dossier.md#4aa9b3c38219, 01_Universe_Inject.sql#6d162cfd1032, 03_Error_Async_Config.txt#4a9d7adf67a3, __context__#72168f70a409, __assignment__#3adec6ac02d7, __policy__#dc4ab5df3cdd, __gate_policy__#115714063000, __review__#95f1481dfb3c)
[PASS] structure.sections: 7 required sections present and non-empty (08_OE_Check.md)
[PASS] structure.placeholders: no placeholders in 08_OE_Check.md
[PASS] structure.header_counts: header matches 08_Oracle_Events.md (135 events, 41196 chars)
[PASS] structure.prediction: /oe prediction line present
[PASS] structure.clock: 'Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)' matches the universe
[PASS] evidence.quoted_spans: 0 quoted span(s) verified as exact substrings of 08_Oracle_Events.md
[PASS] evidence.findings_evidence: no rows/items found under 'findings' in 08_OE_Check.md
[PASS] evidence.signoff_reread: 135/135 items carry a source pointer (min 100%)
[PASS] structure.sweep: pre-verdict sweep has 8/7 rows
[PASS] structure.tally: tally Blocking 0 vs 0 BLOCKING findings
[PASS] review.counter_readings: 94 evidenced counter-readings (of 94 found; need ≥ 94) in 08_OE_Check.md
[PASS] review.coverage: self-review addresses all 1 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## Reminders
- The tool-call minimum is measured on the golden run or the 6-rollout average, never on the OE count.
- Any edit to 08_Oracle_Events.md stales this check and any later rubric review: re-run plan/assemble_oe_events.py, then this script, then the gate.
- The platform field blocks pasting: type the file exactly as it stands (sha 4924949d7fd3).
