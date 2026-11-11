# 08 OE Check — calvin_qm_epic (the Queue Manager epic and stock-take, injection rev3b)
Checked 2026-11-10 · Events 104 · Characters 40144 (300–50,000: ok) · Ledger 2026-11-10 (08_OE_Writing_Ledger.md, gate PASS) · release task-quality-v1
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
/oe prediction (a prediction only; /oe gives the verdict): PASS 5
Completeness 5 · Accuracy 5 · Path feasibility SUPPORTED · Task solvability SUPPORTED_BY_OE

Scope: 104 events = 20 reads, 1 decision step, 83 writes (one per event: 10 children, 17 sub-issues, 22 moves, 22 notes, sheet create, Reports write, Areas tab add, Areas write, folder move, 5 shares, 1 slide, 1 message). Every quoted value on an Expected line is asserted as a substring of its own record when plan/assemble_oe_events.py builds the file: seeded rows from 01_Universe_Inject.sql (parsed as text, SQL L-numbers below), base rows through tools/hg.py (plan/oe_reads.py → plan/oe_base.json). Two blind reviews (plan/sweeps/oe_blind_review_r1.md, plan/sweeps/oe_blind_review_r2.md) were run on the draft; their 12 grouped findings are answered below and none remains open.

## Inventory
| Segment (quoted start) | Role | Event |
|---|---|---|
| "OE 1  Read Brian's message from yesterday in Slack (Calvin's DM with Brian F" | STEP (read) | OE 1 |
| "OE 2  Find the Queue Manager ticket in Linear and read its comments (the tic" | STEP (read) | OE 2 |
| "OE 3  Find and read Vincent's flow pass sheet in Drive (search "flow pass", " | STEP (read) | OE 3 |
| "OE 4  Find and read the legend of Vincent's pass sheets in Drive (the note i" | STEP (read) | OE 4 |
| "OE 5  Find and read Arthur's rule for QA passes in Drive (search "QA passes"" | STEP (read) | OE 5 |
| "OE 6  Read Calvin's DM with Vincent Parker in Slack around Sep 25 2025 for t" | STEP (read) | OE 6 |
| "OE 7  Read the 20 tickets in the sheet's Ticket column in Linear, each with " | STEP (read) | OE 7 |
| "OE 8  Read the #builds history in Slack from Sep 24 to Sep 30 2025 and pick " | STEP (read) | OE 8 |
| "OE 9  Read pull requests #465, #472 and #475 of match3d in GitHub (the PRs i" | STEP (read) | OE 9 |
| "OE 10  Read the review comments on pull request #472 in GitHub (OE 9; the sam" | STEP (read) | OE 10 |
| "OE 11  Read the review comments on pull request #475 in GitHub (OE 9; the sam" | STEP (read) | OE 11 |
| "OE 12  List the match3d pull requests merged since Vincent started his sheet " | STEP (read) | OE 12 |
| "OE 13  Search the ZM tickets in Linear, by each row's wording, for a ticket t" | STEP (read) | OE 13 |
| "OE 14  Search Slack for other sightings on Android Submission 135, the build " | STEP (read) | OE 14 |
| "OE 15  Search Slack for other sightings of the ten rows that still read as pa" | STEP (read) | OE 15 |
| "OE 16  Read Calvin's other DMs in Slack since Sep 26 2025 for a bug somebody " | STEP (read) | OE 16 |
| "OE 17  Find the review invite in Gmail (search "flow review", the review name" | STEP (read) | OE 17 |
| "OE 18  Read the review event on Calvin's calendar (search "flow review", OE 1" | STEP (read) | OE 18 |
| "OE 19  Find the review's card on the ZM ROADMAP board in Trello and read its " | STEP (read) | OE 19 |
| "OE 20  Find Calvin's ZM queue manager folder and deck in Drive (search "ZM qu" | STEP (read) | OE 20 |
| "OE 21  Work out each report's status, ticket and review-list flag from the no" | STEP (calculation / decision, no tool) | OE 21 |
| "OE 22  Create the Tutorials child under the Queue Manager ticket in Linear (f" | STEP (write) | OE 22 |
| "OE 23  Create the Level-end rewards child under the Queue Manager ticket in L" | STEP (write) | OE 23 |
| "OE 24  Create the Daily Gift child under the Queue Manager ticket in Linear (" | STEP (write) | OE 24 |
| "OE 25  Create the Season Pass child under the Queue Manager ticket in Linear " | STEP (write) | OE 25 |
| "OE 26  Create the Collect & Win child under the Queue Manager ticket in Linea" | STEP (write) | OE 26 |
| "OE 27  Create the Win Streak child under the Queue Manager ticket in Linear (" | STEP (write) | OE 27 |
| "OE 28  Create the Zombie Lane child under the Queue Manager ticket in Linear " | STEP (write) | OE 28 |
| "OE 29  Create the Boss Arena child under the Queue Manager ticket in Linear (" | STEP (write) | OE 29 |
| "OE 30  Create the Endless Mode child under the Queue Manager ticket in Linear" | STEP (write) | OE 30 |
| "OE 31  Create the Card packs child under the Queue Manager ticket in Linear (" | STEP (write) | OE 31 |
| "OE 32  Create the sub-issue for report 1 under the Tutorials child in Linear " | STEP (write) | OE 32 |
| "OE 33  Create the sub-issue for report 2 under the Tutorials child in Linear " | STEP (write) | OE 33 |
| "OE 34  Create the sub-issue for report 3 under the Tutorials child in Linear " | STEP (write) | OE 34 |
| "OE 35  Create the sub-issue for report 5 under the Level-end rewards child in" | STEP (write) | OE 35 |
| "OE 36  Create the sub-issue for report 7 under the Level-end rewards child in" | STEP (write) | OE 36 |
| "OE 37  Create the sub-issue for report 9 under the Daily Gift child in Linear" | STEP (write) | OE 37 |
| "OE 38  Create the sub-issue for report 22 under the Zombie Lane child in Line" | STEP (write) | OE 38 |
| "OE 39  Create the sub-issue for report 23 under the Zombie Lane child in Line" | STEP (write) | OE 39 |
| "OE 40  Create the sub-issue for report 25 under the Boss Arena child in Linea" | STEP (write) | OE 40 |
| "OE 41  Create the sub-issue for report 26 under the Boss Arena child in Linea" | STEP (write) | OE 41 |
| "OE 42  Create the sub-issue for report 27 under the Boss Arena child in Linea" | STEP (write) | OE 42 |
| "OE 43  Create the sub-issue for report 29 under the Endless Mode child in Lin" | STEP (write) | OE 43 |
| "OE 44  Create the sub-issue for report 31 under the Card packs child in Linea" | STEP (write) | OE 44 |
| "OE 45  Create the sub-issue for report 33 under the Card packs child in Linea" | STEP (write) | OE 45 |
| "OE 46  Create the sub-issue for report 35 under the Tutorials child in Linear" | STEP (write) | OE 46 |
| "OE 47  Create the sub-issue for report 38 under the Season Pass child in Line" | STEP (write) | OE 47 |
| "OE 48  Create the sub-issue for report 39 under the Season Pass child in Line" | STEP (write) | OE 48 |
| "OE 49  Move ZOM-567 (report 4) under the Tutorials child in Linear (OE 21)" | STEP (write) | OE 49 |
| "OE 50  Move ZOM-568 (report 6) under the Level-end rewards child in Linear an" | STEP (write) | OE 50 |
| "OE 51  Move ZOM-569 (report 8) under the Level-end rewards child in Linear (O" | STEP (write) | OE 51 |
| "OE 52  Move ZOM-570 (report 10) under the Daily Gift child in Linear (OE 21)" | STEP (write) | OE 52 |
| "OE 53  Move ZOM-556 (report 11) under the Daily Gift child in Linear (OE 21)" | STEP (write) | OE 53 |
| "OE 54  Move ZOM-571 (report 12) under the Season Pass child in Linear and set" | STEP (write) | OE 54 |
| "OE 55  Move ZOM-572 (report 13) under the Season Pass child in Linear and set" | STEP (write) | OE 55 |
| "OE 56  Move ZOM-573 (report 14) under the Season Pass child in Linear and set" | STEP (write) | OE 56 |
| "OE 57  Move ZOM-574 (report 15) under the Collect & Win child in Linear and s" | STEP (write) | OE 57 |
| "OE 58  Move ZOM-575 (report 16) under the Endless Mode child in Linear (OE 21" | STEP (write) | OE 58 |
| "OE 59  Move ZOM-585 (report 17) under the Collect & Win child in Linear and s" | STEP (write) | OE 59 |
| "OE 60  Move ZOM-576 (report 18) under the Collect & Win child in Linear (OE 2" | STEP (write) | OE 60 |
| "OE 61  Move ZOM-577 (report 19) under the Collect & Win child in Linear (OE 2" | STEP (write) | OE 61 |
| "OE 62  Move ZOM-560 (report 20) under the Win Streak child in Linear (OE 21)" | STEP (write) | OE 62 |
| "OE 63  Move ZOM-578 (report 21) under the Win Streak child in Linear (OE 21)" | STEP (write) | OE 63 |
| "OE 64  Move ZOM-586 (report 24) under the Zombie Lane child in Linear (OE 21)" | STEP (write) | OE 64 |
| "OE 65  Move ZOM-579 (report 28) under the Endless Mode child in Linear (OE 21" | STEP (write) | OE 65 |
| "OE 66  Move ZOM-580 (report 30) under the Endless Mode child in Linear (OE 21" | STEP (write) | OE 66 |
| "OE 67  Move ZOM-581 (report 32) under the Card packs child in Linear and set " | STEP (write) | OE 67 |
| "OE 68  Move ZOM-582 (report 34) under the Card packs child in Linear (OE 21)" | STEP (write) | OE 68 |
| "OE 69  Move ZOM-583 (report 36) under the Level-end rewards child in Linear (" | STEP (write) | OE 69 |
| "OE 70  Move ZOM-584 (report 37) under the Win Streak child in Linear and set " | STEP (write) | OE 70 |
| "OE 71  Leave the status note on ZOM-567 (report 4) in Linear (OE 2's rule, OE" | STEP (write) | OE 71 |
| "OE 72  Leave the status note on ZOM-568 (report 6) in Linear (OE 2's rule, OE" | STEP (write) | OE 72 |
| "OE 73  Leave the status note on ZOM-569 (report 8) in Linear (OE 2's rule, OE" | STEP (write) | OE 73 |
| "OE 74  Leave the status note on ZOM-570 (report 10) in Linear (OE 2's rule, O" | STEP (write) | OE 74 |
| "OE 75  Leave the status note on ZOM-556 (report 11) in Linear (OE 2's rule, O" | STEP (write) | OE 75 |
| "OE 76  Leave the status note on ZOM-571 (report 12) in Linear (OE 2's rule, O" | STEP (write) | OE 76 |
| "OE 77  Leave the status note on ZOM-572 (report 13) in Linear (OE 2's rule, O" | STEP (write) | OE 77 |
| "OE 78  Leave the status note on ZOM-573 (report 14) in Linear (OE 2's rule, O" | STEP (write) | OE 78 |
| "OE 79  Leave the status note on ZOM-574 (report 15) in Linear (OE 2's rule, O" | STEP (write) | OE 79 |
| "OE 80  Leave the status note on ZOM-575 (report 16) in Linear (OE 2's rule, O" | STEP (write) | OE 80 |
| "OE 81  Leave the status note on ZOM-585 (report 17) in Linear (OE 2's rule, O" | STEP (write) | OE 81 |
| "OE 82  Leave the status note on ZOM-576 (report 18) in Linear (OE 2's rule, O" | STEP (write) | OE 82 |
| "OE 83  Leave the status note on ZOM-577 (report 19) in Linear (OE 2's rule, O" | STEP (write) | OE 83 |
| "OE 84  Leave the status note on ZOM-560 (report 20) in Linear (OE 2's rule, O" | STEP (write) | OE 84 |
| "OE 85  Leave the status note on ZOM-578 (report 21) in Linear (OE 2's rule, O" | STEP (write) | OE 85 |
| "OE 86  Leave the status note on ZOM-586 (report 24) in Linear (OE 2's rule, O" | STEP (write) | OE 86 |
| "OE 87  Leave the status note on ZOM-579 (report 28) in Linear (OE 2's rule, O" | STEP (write) | OE 87 |
| "OE 88  Leave the status note on ZOM-580 (report 30) in Linear (OE 2's rule, O" | STEP (write) | OE 88 |
| "OE 89  Leave the status note on ZOM-581 (report 32) in Linear (OE 2's rule, O" | STEP (write) | OE 89 |
| "OE 90  Leave the status note on ZOM-582 (report 34) in Linear (OE 2's rule, O" | STEP (write) | OE 90 |
| "OE 91  Leave the status note on ZOM-583 (report 36) in Linear (OE 2's rule, O" | STEP (write) | OE 91 |
| "OE 92  Leave the status note on ZOM-584 (report 37) in Linear (OE 2's rule, O" | STEP (write) | OE 92 |
| "OE 93  Create the stock-take sheet in Sheets with a first tab named Reports (" | STEP (write) | OE 93 |
| "OE 94  Write the Reports tab of the stock-take sheet (columns from OE 2, rows" | STEP (write) | OE 94 |
| "OE 95  Add a second tab named Areas to the stock-take sheet (tab name from OE" | STEP (write) | OE 95 |
| "OE 96  Write the Areas tab of the stock-take sheet (columns from OE 2, values" | STEP (write) | OE 96 |
| "OE 97  Put the stock-take sheet in the ZM queue manager folder in Drive (fold" | STEP (write) | OE 97 |
| "OE 98  Share the stock-take sheet with Arthur Blake in Drive (address from OE" | STEP (write) | OE 98 |
| "OE 99  Share the stock-take sheet with Brian Foster in Drive (address from OE" | STEP (write) | OE 99 |
| "OE 100  Share the stock-take sheet with Julia Lawson in Drive (address from OE" | STEP (write) | OE 100 |
| "OE 101  Share the stock-take sheet with Leonard Hayes in Drive (address from O" | STEP (write) | OE 101 |
| "OE 102  Share the stock-take sheet with Vincent Parker in Drive (address from " | STEP (write) | OE 102 |
| "OE 103  Add one slide with the five numbers to the ZM queue manager deck in Sl" | STEP (write) | OE 103 |
| "OE 104  Message Brian in the DM in Slack (the DM from OE 1, after every other " | STEP (write) | OE 104 |
| (no headers, notes or response descriptions in the file) | — none — | n/a |

## Coverage
| R / F | Event(s) | Covered / missing / partial | Route (ledger / other valid) |
|---|---|---|---|
| R1 · F2, F41, F40 | OEs 2, 17, 18 | covered | ledger route: the ticket by its name, the review by its invite and event |
| R2 · F1 | OE 1 | covered | ledger route: Calvin's DM with Brian, Tue Sep 30 |
| R3 · F3, F4, F5, F6, F7, F28, F29, F30, F31, F32, F33, F34, F35, F36, F37, F38, F39, F42 | OEs 2 to 19, 21 | covered | ledger route: every record the DM and the note incorporate is read before any write, then each report is decided |
| R4 · F46, F86, report facts | OEs 21, 22 to 92 | covered | ledger route: 10 + 17 linear_create_issue, 22 linear_update_issue, 22 linear_create_comment |
| R5 · F44, F86 | OEs 20, 93 to 97 | covered | ledger route: sheet created, two tabs written, moved into the folder |
| R6 · F41 | OEs 18, 98 to 102 | covered | ledger route: five gdrive_share_file writes |
| R7 · F45, F87 | OEs 20, 103 | covered | ledger route: gslides_batch_update |
| R8 · F1, F87 | OE 104 | covered | ledger route: slack_send_message in the DM |

## Expected-data sign-off
| Event | Claim (quoted) | Source re-read (hg.py pointer) | Value found | Ledger entry (result · quote · evidence_check / not_a_claim) | Match / minor / wrong / unresolved |
|---|---|---|---|---|---|
| OE 1 | Brian, Tue Sep 30 2025 1:40 PM PT, ts 1759264805.214409 + 5 quotes | SQL L64 slack.slack_messages D0770ET6WBW/1759264805.214409 | ts 1759264805 = 20:40:05 UTC = 1:40 PM PDT; user EMPLOYEE_0026 = Brian Foster; quotes verbatim | F1 · VERIFIED · quotes | match |
| OE 2 | ZOM-543 'Queue Manager', team ZOM, In Progress, no parent; Brian's comment Tue Sep 30 1:25 PM PT + 15 quotes | hg.py linear data.json /issues/3618; SQL L217 linear.linear_comments on ZOM-543 | title, state_id In Progress, parent_id null; author usr_fc22d5941b2aeb5c = Brian; created_at 2025-09-30T20:25:37Z; quotes verbatim | F2, F3 · VERIFIED · quotes | match |
| OE 3 | Sheet 'ZM home screen flow pass', owner vincent.parker, 7 columns, 38 rows cell for cell, the legend note | SQL L8 gdrive.drive_files and the gsheets.sheets_sheets grid_json of f_cb40955893624e1acb8500 | header and all 38 rows equal the grid; 18 blank Ticket cells, 20 keys; note verbatim | F4 · VERIFIED · quotes (rows generated from the grid) | match |
| OE 4 | Doc 'How to read my pass sheets' + 6 quotes | SQL L10 gdocs.docs_documents f_d3a1aa5976285aac98ffda | title and quotes verbatim; parent is the folder of the flow pass sheet (d_65c76e0b87aa7e9b84d1df) | F5 · VERIFIED · quotes | match |
| OE 5 | Doc 'ZM builds and QA passes' + 4 quotes | SQL L12 gdocs.docs_documents f_6d0326fa006b136f1bbf82 | title and quotes verbatim; owner arthur.blake; shared with Calvin | F6 · VERIFIED · quotes | match |
| OE 6 | Calvin Thu Sep 25 9:29 AM PT '#1718 already tested'; Vincent 10:15 AM PT 'Looks ok to me' and 'Boss arena as well' | hg.py slack messages/D06UPGF5PQV/2025-09.json /158; hg.py slack messages/D06UPGF5PQV/2025-09.json /169; hg.py slack messages/D06UPGF5PQV/2025-09.json /170 (D06UPGF5PQV/1758820551.265839) | users EMPLOYEE_0006 Calvin and EMPLOYEE_0012 Vincent; ts 1758817744, 1758820544, 1758820551; quotes verbatim | F7 · VERIFIED · quotes | match |
| OE 7 | 20 states as found; later notes on ZOM-585 (Samuel Turner), ZOM-586 (Owen Baker), ZOM-576, ZOM-582 (Vincent), ZOM-577 (Owen Baker) | SQL L177 to SQL L215 linear.linear_issues; SQL L275, SQL L281 linear.linear_comments | state_id per row as listed (5 In Validation, 15 Todo); authors usr_caafeec2804b3a67 Samuel, usr_4e13bd40cc73d0fc Owen, usr_65c76e0b87aa7e9b Vincent; created_at as stated; quotes verbatim | F46, F34, F35 · VERIFIED · quotes | match |
| OE 8 | Fifteen result posts with job, number, branch and time; twelve main; #1698, #1718, #1746 feature branches; #135 after #1745, #1750, #1757 | hg.py slack messages/C05433XK267/2025-09.json /926; hg.py slack messages/C05433XK267/2025-09.json /1124; hg.py slack messages/C05433XK267/2025-09.json /1053; hg.py slack messages/C05433XK267/2025-09.json /1058; the other eleven in the same file (plan/oe_base.json) | attachment fallback text of each post gives job - #n - branch; ts converted to PT and UTC; 12 main and 3 feature counted | F11, F23, F15, F16 · VERIFIED · quotes | match |
| OE 9 | #465, #472, #475 titles, base main, merge times; first line of the #472 description | hg.py github data.json /pull_requests/2369, hg.py github data.json /pull_requests/2377, hg.py github data.json /pull_requests/2380; SQL L162 (UPDATE of the body) | merged_at 2025-09-25T22:15:51Z, 2025-09-30T15:53:04Z, 2025-09-30T16:09:15Z; base_ref main; body's first line verbatim | F24, F25, F27, F31 · VERIFIED · quotes | match |
| OE 10 | Login EMPLOYEE_0025_GITHUB_USERNAME (Arthur Blake), Tue Sep 30 8:53 AM PT + quote | SQL L164 github.github_review_comments harmonygames-Games/match3d#472#rc_1; name from hg.py github data.json /users/6 | author_login as stated; created_at 2025-09-30T15:53:40Z; quote verbatim | F28 · VERIFIED · quote | match |
| OE 11 | Login EMPLOYEE_0025_GITHUB_USERNAME (Arthur Blake), Tue Sep 30 9:09 AM PT + quote | SQL L169 github.github_review_comments harmonygames-Games/match3d#475#rc_1 | author_login as stated; created_at 2025-09-30T16:09:50Z; quote verbatim | F29 · VERIFIED · quote | match |
| OE 12 | Eight merged PRs not on the sheet with merge times; #463 before the sheet; #473 title, base, merge; Oliver's comment + quote | hg.py github data.json /pull_requests/2367, /2370 to /2373, /2375, /2376, /2378, /2379; SQL L172 github.github_pr_comments harmonygames-Games/match3d#473#c_2 | merged_at 2025-09-26T15:14:44Z, 18:58:33Z, 2025-09-29T16:13:50Z, 2025-09-30T01:50:16Z, 15:51:15Z, 15:52:24Z, 15:41:20Z, 15:48:10Z; #463 2025-09-26T00:08:03Z; sheet created 2025-09-26T10:12:44Z; comment author EMPLOYEE_0003, created 2025-09-30T15:42:10Z; quote verbatim | F26, F30 · VERIFIED · quote; the list of eight read this run | match |
| OE 13 | ZOM-556 and ZOM-560 titles, state Todo, Vincent's two comments; no ticket for the other sixteen rows | hg.py linear data.json /issues/3632, hg.py linear data.json /issues/3637; SQL L219, SQL L221 | titles and state_id Todo; comments created 2025-09-30T18:05:21Z and 18:08:48Z; quotes verbatim; absence: blind review r2 checked all 553 ZOM tickets by each row's key words (plan/sweeps/oe_blind_review_r2.md) | F38, F39 · VERIFIED · quotes · ABSENCE evidence_check | match |
| OE 14 | Vincent's reply Tue Sep 30 2:20 PM PT under his Sep 15 thread; Robert's reply 2:44 PM PT under his Sep 9 PT thread + quotes | SQL L74, SQL L77; parents hg.py slack messages/C08R27X0EAH/2025-09.json /651, hg.py slack messages/C08R27X0EAH/2025-09.json /461 | ts 1759267212 and 1759268652; users EMPLOYEE_0012 Vincent and EMPLOYEE_0016 Robert; parent ts 1757939514 = Mon Sep 15 PT, 1757467270 = Tue Sep 9 6:21 PM PT; quotes verbatim | F32, F33 · VERIFIED · quotes | match |
| OE 15 | Robert, Mon Sep 29 3:40 PM PT, Android 2006 + quote; #2006 before #1745; no later sighting for the other nine rows | SQL L80; hg.py slack messages/C05433XK267/2025-09.json /1053; hg.py slack messages/C05433XK267/2025-09.json /1058 | ts 1759185627; #2006 posted 15:39 UTC, #1745 16:19 UTC on Sep 29; absence: blind review r2 read every message since Sep 26 in Calvin's team channels and every seeded Slack row | F36, F15, F16 · VERIFIED · quote · ABSENCE evidence_check | match |
| OE 16 | Marcus Bennett, Tue Sep 30 10:10 AM PT, two messages + quotes; no sheet row, no ticket; four other DMs carry no other bug | SQL L70; SQL L72 (D05U73FNDDL/1759252231.2); hg.py slack messages/D05S1S2H55M/2025-09.json /121 (D05S1S2H55M/1759184077.910139) | ts 1759252212 and 1759252231; user EMPLOYEE_0002 Marcus; hg.py search linear 'icon glow': 0 hits, scan complete; Owen's Sep 29 line is 'Se ve un poco mas lento todo' | F37 · VERIFIED · quotes · ABSENCE evidence_check | match |
| OE 17 | Updated invitation from leonard.hayes, Tue Sep 30 10:24 AM PT, subject and note; the Sep 29 invitation's agenda | SQL L123, SQL L119 gmail.gmail_messages | date 2025-09-30T17:24:09Z; subject and both quotes verbatim | F40 · VERIFIED · quotes | match |
| OE 18 | Event 'ZM home screen flow review', starts Thu Oct 2 2025 11:00 AM PT, five attendees besides Calvin | SQL L114 gcal.gcal_events evt_342a813cb7765d4a6fce8d | start_ts 2025-10-02T18:00:00Z (after the clock: not yet held); attendees_json as listed | F41 · VERIFIED | match |
| OE 19 | Card name and description; Leonard's change Tue Sep 30 10:22 AM PT; earlier description | SQL L92 trello.trello_cards; SQL L100, SQL L94 trello.trello_actions | name and desc verbatim; action date 2025-09-30T17:22:36Z; createCard action carries the earlier description | F42 · VERIFIED · quotes | match |
| OE 20 | Folder 'ZM queue manager' and presentation 'ZM queue manager', owner calvin.price | SQL L16, SQL L18 gdrive.drive_files | names and owner as stated; the deck's parent is the folder | F44, F45 · VERIFIED | match |
| OE 21 | 39 reports with status, ticket and review flag; 10 / 9 / 20; areas open of total; 0 Clear; 7 on the review list | rules SQL L217; records in OE 2 to OE 19; solver/truth.json re-derives all 39; platform /prompt on this SQL derived the same (Working_Files/platform_reports/prompt_rev3b_PASS.md) | 10 + 9 + 20 = 39; review rows 6, 8, 15, 17, 18, 19, 36; every area has an open report | F87, F86 · not_a_claim (derived) | match |
| OE 22 | A new ZOM issue titled "Tutorials", parent ZOM-543, state Todo, no assignee. | linear_create_issue (team, title required; parentId, state optional); parent hg.py linear data.json /issues/3618 | area name from the note; every area Open, so Todo | F3, F86 · VERIFIED (write) | match |
| OE 23 | A new ZOM issue titled "Level-end rewards", parent ZOM-543, state Todo, no assignee. | linear_create_issue (team, title required; parentId, state optional); parent hg.py linear data.json /issues/3618 | area name from the note; every area Open, so Todo | F3, F86 · VERIFIED (write) | match |
| OE 24 | A new ZOM issue titled "Daily Gift", parent ZOM-543, state Todo, no assignee. | linear_create_issue (team, title required; parentId, state optional); parent hg.py linear data.json /issues/3618 | area name from the note; every area Open, so Todo | F3, F86 · VERIFIED (write) | match |
| OE 25 | A new ZOM issue titled "Season Pass", parent ZOM-543, state Todo, no assignee. | linear_create_issue (team, title required; parentId, state optional); parent hg.py linear data.json /issues/3618 | area name from the note; every area Open, so Todo | F3, F86 · VERIFIED (write) | match |
| OE 26 | A new ZOM issue titled "Collect & Win", parent ZOM-543, state Todo, no assignee. | linear_create_issue (team, title required; parentId, state optional); parent hg.py linear data.json /issues/3618 | area name from the note; every area Open, so Todo | F3, F86 · VERIFIED (write) | match |
| OE 27 | A new ZOM issue titled "Win Streak", parent ZOM-543, state Todo, no assignee. | linear_create_issue (team, title required; parentId, state optional); parent hg.py linear data.json /issues/3618 | area name from the note; every area Open, so Todo | F3, F86 · VERIFIED (write) | match |
| OE 28 | A new ZOM issue titled "Zombie Lane", parent ZOM-543, state Todo, no assignee. | linear_create_issue (team, title required; parentId, state optional); parent hg.py linear data.json /issues/3618 | area name from the note; every area Open, so Todo | F3, F86 · VERIFIED (write) | match |
| OE 29 | A new ZOM issue titled "Boss Arena", parent ZOM-543, state Todo, no assignee. | linear_create_issue (team, title required; parentId, state optional); parent hg.py linear data.json /issues/3618 | area name from the note; every area Open, so Todo | F3, F86 · VERIFIED (write) | match |
| OE 30 | A new ZOM issue titled "Endless Mode", parent ZOM-543, state Todo, no assignee. | linear_create_issue (team, title required; parentId, state optional); parent hg.py linear data.json /issues/3618 | area name from the note; every area Open, so Todo | F3, F86 · VERIFIED (write) | match |
| OE 31 | A new ZOM issue titled "Card packs", parent ZOM-543, state Todo, no assignee. | linear_create_issue (team, title required; parentId, state optional); parent hg.py linear data.json /issues/3618 | area name from the note; every area Open, so Todo | F3, F86 · VERIFIED (write) | match |
| OE 32 | A new ZOM issue titled "Back to back tutorials at level 16-17 only play the first one", parent the Tutorials child, state In Validation, no priority, no assignee. | linear_create_issue (team, title; parentId, state); row in SQL L8 | title is the row's What happens cell; state from the status | F47 · VERIFIED (write content) | match |
| OE 33 | A new ZOM issue titled "Card upgrade tutorial never shows after the Zombie Lane one", parent the Tutorials child, state In Validation, no priority, no assignee. | linear_create_issue (team, title; parentId, state); row in SQL L8 | title is the row's What happens cell; state from the status | F48 · VERIFIED (write content) | match |
| OE 34 | A new ZOM issue titled "Quest tutorial arrow points at the wrong tab after the last panel closes", parent the Tutorials child, state Done, no priority, no assignee. | linear_create_issue (team, title; parentId, state); row in SQL L8 | title is the row's What happens cell; state from the status | F49 · VERIFIED (write content) | match |
| OE 35 | A new ZOM issue titled "Coin animation plays again after killing and reopening the app", parent the Level-end rewards child, state Done, no priority, no assignee. | linear_create_issue (team, title; parentId, state); row in SQL L8 | title is the row's What happens cell; state from the status | F51 · VERIFIED (write content) | match |
| OE 36 | A new ZOM issue titled "Reward count-up is skipped when tapping fast on play", parent the Level-end rewards child, state Done, no priority, no assignee. | linear_create_issue (team, title; parentId, state); row in SQL L8 | title is the row's What happens cell; state from the status | F53 · VERIFIED (write content) | match |
| OE 37 | A new ZOM issue titled "Season pass popup comes up on top of the daily gift when both are due", parent the Daily Gift child, state Todo, no priority, no assignee. | linear_create_issue (team, title; parentId, state); row in SQL L8 | title is the row's What happens cell; state from the status | F55 · VERIFIED (write content) | match |
| OE 38 | A new ZOM issue titled "Zombie Lane reward animation plays under the home buttons", parent the Zombie Lane child, state Done, no priority, no assignee. | linear_create_issue (team, title; parentId, state); row in SQL L8 | title is the row's What happens cell; state from the status | F68 · VERIFIED (write content) | match |
| OE 39 | A new ZOM issue titled "Zombie Lane panel opens twice after claiming", parent the Zombie Lane child, state Done, no priority, no assignee. | linear_create_issue (team, title; parentId, state); row in SQL L8 | title is the row's What happens cell; state from the status | F69 · VERIFIED (write content) | match |
| OE 40 | A new ZOM issue titled "Boss arena tutorial does not play when another tutorial is queued before it", parent the Boss Arena child, state In Validation, no priority, no assignee. | linear_create_issue (team, title; parentId, state); row in SQL L8 | title is the row's What happens cell; state from the status | F71 · VERIFIED (write content) | match |
| OE 41 | A new ZOM issue titled "Boss arena unlock popup shows behind the level-end rewards", parent the Boss Arena child, state Done, no priority, no assignee. | linear_create_issue (team, title; parentId, state); row in SQL L8 | title is the row's What happens cell; state from the status | F72 · VERIFIED (write content) | match |
| OE 42 | A new ZOM issue titled "Arena entry button can be tapped during the reward animation", parent the Boss Arena child, state Done, no priority, no assignee. | linear_create_issue (team, title; parentId, state); row in SQL L8 | title is the row's What happens cell; state from the status | F73 · VERIFIED (write content) | match |
| OE 43 | A new ZOM issue titled "Coming back from Endless replays the home intro animation", parent the Endless Mode child, state Todo, no priority, no assignee. | linear_create_issue (team, title; parentId, state); row in SQL L8 | title is the row's What happens cell; state from the status | F75 · VERIFIED (write content) | match |
| OE 44 | A new ZOM issue titled "Tap to collect prompt is missing when a pack opens after a level", parent the Card packs child, state Done, no priority, no assignee. | linear_create_issue (team, title; parentId, state); row in SQL L8 | title is the row's What happens cell; state from the status | F77 · VERIFIED (write content) | match |
| OE 45 | A new ZOM issue titled "Last pack does not show its cards before closing", parent the Card packs child, state Done, no priority, no assignee. | linear_create_issue (team, title; parentId, state); row in SQL L8 | title is the row's What happens cell; state from the status | F79 · VERIFIED (write content) | match |
| OE 46 | A new ZOM issue titled "Tutorial hand stays on screen after the last panel closes", parent the Tutorials child, state Done, no priority, no assignee. | linear_create_issue (team, title; parentId, state); row in SQL L8 | title is the row's What happens cell; state from the status | F81 · VERIFIED (write content) | match |
| OE 47 | A new ZOM issue titled "Pass progress bar fills before the tokens arrive", parent the Season Pass child, state In Validation, no priority, no assignee. | linear_create_issue (team, title; parentId, state); row in SQL L8 | title is the row's What happens cell; state from the status | F84 · VERIFIED (write content) | match |
| OE 48 | A new ZOM issue titled with Marcus's report (the pass icon glow staying on after everything is claimed), parent the Season Pass child, state Todo, no priority, no assignee. | linear_create_issue (team, title; parentId, state); row in SQL L8 | title is the row's What happens cell; state from the status | F85 · VERIFIED (write content) | match |
| OE 49 | ZOM-567 has the Tutorials child as its parent; its state stays Todo. | linear_update_issue (id; parentId, state); SQL L177 | parent set to the area's child; state per the status | F50, F46 · VERIFIED (write) | match |
| OE 50 | ZOM-568 has the Level-end rewards child as its parent and is in state In Validation (it was Todo). | linear_update_issue (id; parentId, state); SQL L179 | parent set to the area's child; state per the status | F52, F46 · VERIFIED (write) | match |
| OE 51 | ZOM-569 has the Level-end rewards child as its parent; its state stays Todo. | linear_update_issue (id; parentId, state); SQL L181 | parent set to the area's child; state per the status | F54, F46 · VERIFIED (write) | match |
| OE 52 | ZOM-570 has the Daily Gift child as its parent; its state stays Todo. | linear_update_issue (id; parentId, state); SQL L183 | parent set to the area's child; state per the status | F56, F46 · VERIFIED (write) | match |
| OE 53 | ZOM-556 has the Daily Gift child as its parent; its state stays Todo. | linear_update_issue (id; parentId, state); hg.py linear data.json /issues/3632 | parent set to the area's child; state per the status | F57, F46 · VERIFIED (write) | match |
| OE 54 | ZOM-571 has the Season Pass child as its parent and is in state Todo (it was In Validation). | linear_update_issue (id; parentId, state); SQL L185 | parent set to the area's child; state per the status | F58, F46 · VERIFIED (write) | match |
| OE 55 | ZOM-572 has the Season Pass child as its parent and is in state In Validation (it was Todo). | linear_update_issue (id; parentId, state); SQL L187 | parent set to the area's child; state per the status | F59, F46 · VERIFIED (write) | match |
| OE 56 | ZOM-573 has the Season Pass child as its parent and is in state In Validation (it was Todo). | linear_update_issue (id; parentId, state); SQL L189 | parent set to the area's child; state per the status | F60, F46 · VERIFIED (write) | match |
| OE 57 | ZOM-574 has the Collect & Win child as its parent and is in state Todo (it was In Validation). | linear_update_issue (id; parentId, state); SQL L191 | parent set to the area's child; state per the status | F61, F46 · VERIFIED (write) | match |
| OE 58 | ZOM-575 has the Endless Mode child as its parent; its state stays Todo. | linear_update_issue (id; parentId, state); SQL L193 | parent set to the area's child; state per the status | F62, F46 · VERIFIED (write) | match |
| OE 59 | ZOM-585 has the Collect & Win child as its parent and is in state Todo (it was In Validation). | linear_update_issue (id; parentId, state); SQL L213 | parent set to the area's child; state per the status | F63, F46 · VERIFIED (write) | match |
| OE 60 | ZOM-576 has the Collect & Win child as its parent; its state stays In Validation. | linear_update_issue (id; parentId, state); SQL L195 | parent set to the area's child; state per the status | F64, F46 · VERIFIED (write) | match |
| OE 61 | ZOM-577 has the Collect & Win child as its parent; its state stays Todo. | linear_update_issue (id; parentId, state); SQL L197 | parent set to the area's child; state per the status | F65, F46 · VERIFIED (write) | match |
| OE 62 | ZOM-560 has the Win Streak child as its parent; its state stays Todo. | linear_update_issue (id; parentId, state); hg.py linear data.json /issues/3637 | parent set to the area's child; state per the status | F66, F46 · VERIFIED (write) | match |
| OE 63 | ZOM-578 has the Win Streak child as its parent; its state stays Todo. | linear_update_issue (id; parentId, state); SQL L199 | parent set to the area's child; state per the status | F67, F46 · VERIFIED (write) | match |
| OE 64 | ZOM-586 has the Zombie Lane child as its parent; its state stays Todo. | linear_update_issue (id; parentId, state); SQL L215 | parent set to the area's child; state per the status | F70, F46 · VERIFIED (write) | match |
| OE 65 | ZOM-579 has the Endless Mode child as its parent; its state stays Todo. | linear_update_issue (id; parentId, state); SQL L201 | parent set to the area's child; state per the status | F74, F46 · VERIFIED (write) | match |
| OE 66 | ZOM-580 has the Endless Mode child as its parent; its state stays Todo. | linear_update_issue (id; parentId, state); SQL L203 | parent set to the area's child; state per the status | F76, F46 · VERIFIED (write) | match |
| OE 67 | ZOM-581 has the Card packs child as its parent and is in state Todo (it was In Validation). | linear_update_issue (id; parentId, state); SQL L205 | parent set to the area's child; state per the status | F78, F46 · VERIFIED (write) | match |
| OE 68 | ZOM-582 has the Card packs child as its parent; its state stays Todo. | linear_update_issue (id; parentId, state); SQL L207 | parent set to the area's child; state per the status | F80, F46 · VERIFIED (write) | match |
| OE 69 | ZOM-583 has the Level-end rewards child as its parent; its state stays Todo. | linear_update_issue (id; parentId, state); SQL L209 | parent set to the area's child; state per the status | F82, F46 · VERIFIED (write) | match |
| OE 70 | ZOM-584 has the Win Streak child as its parent and is in state In Validation (it was Todo). | linear_update_issue (id; parentId, state); SQL L211 | parent set to the area's child; state per the status | F83, F46 · VERIFIED (write) | match |
| OE 71 | A comment on ZOM-567 giving the status Waiting on a fix and why: no merged fix and no pass. … | linear_create_comment (issueId, body); SQL L177 | status and reason as in the decision step | F50 · VERIFIED (write content) | match |
| OE 72 | A comment on ZOM-568 giving the status Waiting on QA and why: the description of merged PR #472 lists the pre-level panel fix; #472 is merged. … | linear_create_comment (issueId, body); SQL L179 | status and reason as in the decision step | F52 · VERIFIED (write content) | match |
| OE 73 | A comment on ZOM-569 giving the status Waiting on a fix and why: no merged fix and no pass. … | linear_create_comment (issueId, body); SQL L181 | status and reason as in the decision step | F54 · VERIFIED (write content) | match |
| OE 74 | A comment on ZOM-570 giving the status Waiting on a fix and why: no merged fix and no pass. … | linear_create_comment (issueId, body); SQL L183 | status and reason as in the decision step | F56 · VERIFIED (write content) | match |
| OE 75 | A comment on ZOM-556 giving the status Waiting on a fix and why: no merged fix and no pass. … | linear_create_comment (issueId, body); hg.py linear data.json /issues/3632 | status and reason as in the decision step | F57 · VERIFIED (write content) | match |
| OE 76 | A comment on ZOM-571 giving the status Waiting on a fix and why: Arthur's review on #472 says the icon restart is not in that diff. … | linear_create_comment (issueId, body); SQL L185 | status and reason as in the decision step | F58 · VERIFIED (write content) | match |
| OE 77 | A comment on ZOM-572 giving the status Waiting on QA and why: Oliver wrote on his merged PR #473 that it has the fix; #473 is merged. … | linear_create_comment (issueId, body); SQL L187 | status and reason as in the decision step | F59 · VERIFIED (write content) | match |
| OE 78 | A comment on ZOM-573 giving the status Waiting on QA and why: Oliver wrote on his merged PR #473 that it has the fix; #473 is merged. … | linear_create_comment (issueId, body); SQL L189 | status and reason as in the decision step | F60 · VERIFIED (write content) | match |
| OE 79 | A comment on ZOM-574 giving the status Waiting on a fix and why: Arthur's review on #472 says the event bar start is not in that diff. … | linear_create_comment (issueId, body); SQL L191 | status and reason as in the decision step | F61 · VERIFIED (write content) | match |
| OE 80 | A comment on ZOM-575 giving the status Waiting on a fix and why: no merged fix and no pass. … | linear_create_comment (issueId, body); SQL L193 | status and reason as in the decision step | F62 · VERIFIED (write content) | match |
| OE 81 | A comment on ZOM-585 giving the status Waiting on a fix and why: Samuel saw it again on Android Submission 135 after the ok (his note on ZOM-585). … | linear_create_comment (issueId, body); SQL L213 | status and reason as in the decision step | F63 · VERIFIED (write content) | match |
| OE 82 | A comment on ZOM-576 giving the status Waiting on QA and why: the again was on Android #2013, made before #472 merged, so QA has not tried the fix; #4 … | linear_create_comment (issueId, body); SQL L195 | status and reason as in the decision step | F64 · VERIFIED (write content) | match |
| OE 83 | A comment on ZOM-577 giving the status Waiting on a fix and why: no merged fix and no pass. … | linear_create_comment (issueId, body); SQL L197 | status and reason as in the decision step | F65 · VERIFIED (write content) | match |
| OE 84 | A comment on ZOM-560 giving the status Waiting on a fix and why: no merged fix and no pass. … | linear_create_comment (issueId, body); hg.py linear data.json /issues/3637 | status and reason as in the decision step | F66 · VERIFIED (write content) | match |
| OE 85 | A comment on ZOM-578 giving the status Waiting on a fix and why: no merged fix and no pass. … | linear_create_comment (issueId, body); SQL L199 | status and reason as in the decision step | F67 · VERIFIED (write content) | match |
| OE 86 | A comment on ZOM-586 giving the status Waiting on a fix and why: Owen saw it again on Android Submission 135 after the nr (his note on ZOM-586). … | linear_create_comment (issueId, body); SQL L215 | status and reason as in the decision step | F70 · VERIFIED (write content) | match |
| OE 87 | A comment on ZOM-579 giving the status Waiting on a fix and why: no merged fix and no pass. … | linear_create_comment (issueId, body); SQL L201 | status and reason as in the decision step | F74 · VERIFIED (write content) | match |
| OE 88 | A comment on ZOM-580 giving the status Waiting on a fix and why: no merged fix and no pass. … | linear_create_comment (issueId, body); SQL L203 | status and reason as in the decision step | F76 · VERIFIED (write content) | match |
| OE 89 | A comment on ZOM-581 giving the status Waiting on a fix and why: Arthur's review on #475 says the pack sound stop is not in it. … | linear_create_comment (issueId, body); SQL L205 | status and reason as in the decision step | F78 · VERIFIED (write content) | match |
| OE 90 | A comment on ZOM-582 giving the status Waiting on a fix and why: again on iOS Internal #1757, a main build made after #475 merged, so the fix did not  … | linear_create_comment (issueId, body); SQL L207 | status and reason as in the decision step | F80 · VERIFIED (write content) | match |
| OE 91 | A comment on ZOM-583 giving the status Waiting on a fix and why: no merged fix and no pass. … | linear_create_comment (issueId, body); SQL L209 | status and reason as in the decision step | F82 · VERIFIED (write content) | match |
| OE 92 | A comment on ZOM-584 giving the status Waiting on QA and why: Oliver wrote on his merged PR #473 that it has the fix; #473 is merged. … | linear_create_comment (issueId, body); SQL L211 | status and reason as in the decision step | F83 · VERIFIED (write content) | match |
| OE 93 | A new spreadsheet owned by Calvin whose first tab is Reports. | gsheets_create_spreadsheet (title required); folder SQL L16 | a new native sheet; title free | F44 · VERIFIED (write) | match |
| OE 94 | Tab Reports with the columns Report, Area, Status, Ticket, Review list, Why and 39 report rows: 10 Passed, 9 Waiting on QA, 20 Waiting on a fix; 7 rows marked for the review list. | gsheets_values_update (spreadsheetId, range, values); columns SQL L217 | six columns, 39 rows, 10 / 9 / 20, 7 marked | F3, F87 · VERIFIED (write content) | match |
| OE 95 | The spreadsheet has the tabs Reports and Areas. | gsheets_batch_update (spreadsheetId, requests: addSheet); tab name SQL L217 | two tabs | F3 · VERIFIED (write) | match |
| OE 96 | Tab Areas with the columns Area, Status, Open reports and 10 rows, every area Open: Tutorials 3, Level-end rewards 3, Daily Gift 3, Season Pass 5, Collect & Win 4, Win Streak 3, Zombie Lane 1, Boss Arena 1, Endless Mode 4, Card packs 2. | gsheets_values_update; columns SQL L217 | three columns, 10 rows, all Open, counts as in the decision step | F86 · VERIFIED (write content) | match |
| OE 97 | The sheet's parent is the folder "ZM queue manager". | gdrive_move_file (fileId, newParentId); folder SQL L16 | parent d_36cdb0374c4aad3b8bf741 (creating it in the folder directly is an equal route) | F44 · VERIFIED (write) | match |
| OE 98 | arthur.blake@harmonygames.co can open the sheet (writer, commenter or reader). | gdrive_share_file (fileId; emailAddress, role); attendee in SQL L114 | address as in the event; any role opens the sheet | F41 · VERIFIED (write) | match |
| OE 99 | brian.foster@harmonygames.co can open the sheet (writer, commenter or reader). | gdrive_share_file (fileId; emailAddress, role); attendee in SQL L114 | address as in the event; any role opens the sheet | F41 · VERIFIED (write) | match |
| OE 100 | julia.lawson@harmonygames.co can open the sheet (writer, commenter or reader). | gdrive_share_file (fileId; emailAddress, role); attendee in SQL L114 | address as in the event; any role opens the sheet | F41 · VERIFIED (write) | match |
| OE 101 | leonard.hayes@harmonygames.co can open the sheet (writer, commenter or reader). | gdrive_share_file (fileId; emailAddress, role); attendee in SQL L114 | address as in the event; any role opens the sheet | F41 · VERIFIED (write) | match |
| OE 102 | vincent.parker@harmonygames.co can open the sheet (writer, commenter or reader). | gdrive_share_file (fileId; emailAddress, role); attendee in SQL L114 | address as in the event; any role opens the sheet | F41 · VERIFIED (write) | match |
| OE 103 | A new slide in the presentation "ZM queue manager" with: 10 passed, 9 waiting on QA, 20 waiting on a fix, 0 areas clear, 7 on the review list. | gslides_batch_update (presentationId, requests); deck SQL L18 | one new slide with 10, 9, 20, 0, 7 | F45, F87 · VERIFIED (write content) | match |
| OE 104 | A message in Calvin's DM with Brian Foster with the numbers he asked for: 10 reports passed, 9 waiting on QA, 20 waiting on a fix, 0 areas clear, 7 on the review list. | slack_send_message (channel, text); DM of SQL L64 | the five numbers from the decision step | F1, F87 · VERIFIED (write content) | match |

## Findings
Every finding below was raised against the draft by a blind review and fixed in this pass; the quoted span is the corrected text now in 08_Oracle_Events.md. None remains open.

| # | Severity | Component | Event | Quoted span | Rule (Eval § / source) | What is wrong | Evidence (ledger fact + source pointer) |
|---|---|---|---|---|---|---|---|
| X1 | RESOLVED in this pass | Accuracy | OE 8 | "Android Submission #135 is a main build posted after iOS Internal #1745, #1750 and #1757." | 2_Oracle_Events_Eval.md 2_Oracle_Events_Eval.md §2.3 value | The first draft called #135 the newest main build; four main builds follow it on Sep 30 (#2027, #1758, #1759, #2028). Reworded and reached through the ticket notes | plan/sweeps/oe_blind_review_r1.md finding 1; hg.py slack messages/C05433XK267/2025-09.json /1124; hg.py slack messages/C05433XK267/2025-09.json /1127, /1128, /1131, /1132 |
| X2 | RESOLVED in this pass | Accuracy | OE 8 | "Fifteen result posts" | 2_Oracle_Events_Eval.md §2.3 count | The draft listed sixteen, with iOS Internal #1754, a build no row or chat names; removed and recounted (twelve main, three feature). Each build also has a Started post without a branch, so the result posts are named | plan/sweeps/oe_blind_review_r1.md finding 2, plan/sweeps/oe_blind_review_r2.md m2; hg.py slack messages/C05433XK267/2025-09.json /926 |
| X3 | RESOLVED in this pass | Completeness | OE 14 | "the build Samuel and Owen name in OE 7" | 2_Oracle_Events_Eval.md §3.2 dependency | The search term was credited to the builds read; its source is the ticket notes, now read first | plan/sweeps/oe_blind_review_r1.md finding 3; SQL L275, SQL L281 |
| X4 | RESOLVED in this pass | Completeness | OE 12 | "Eight merged pull requests are not on the sheet" | 2_Oracle_Events_Eval.md §3.1 population | The draft named #473 only; all eight are listed with merge times, the boundary is the sheet's creation time and #463 is placed before it | plan/sweeps/oe_blind_review_r1.md finding 4, plan/sweeps/oe_blind_review_r2.md M2 and m1; hg.py github data.json /pull_requests/2367, /2370, /2371, /2372, /2373, /2375, /2376, /2378, /2379 |
| X5 | RESOLVED in this pass | Completeness | OE 13 | "a row whose Ticket cell is blank in OE 3" | 2_Oracle_Events_Eval.md §3.1 missing discovery | The draft searched for rows 11 and 20 only; the search now covers all eighteen blank-Ticket rows | plan/sweeps/oe_blind_review_r1.md finding 5; hg.py linear data.json /issues/3632, hg.py linear data.json /issues/3637; plan/sweeps/oe_blind_review_r2.md OE 13 (553 ZOM tickets checked) |
| X6 | RESOLVED in this pass | Completeness | OE 15 | "the ten rows that still read as passed" | 2_Oracle_Events_Eval.md §3.1 missing discovery | The draft searched for row 27 only; the search now covers all ten passed rows | plan/sweeps/oe_blind_review_r1.md finding 6; SQL L80; plan/sweeps/oe_blind_review_r2.md OE 14, 15 |
| X7 | RESOLVED in this pass | Accuracy | OE 4 | "list the Drive folder that holds the flow pass sheet" | 2_Oracle_Events_Eval.md §3.2 locator | Search terms 'pass sheets' (the target's own title) and 'pass sheet legend' (not in the doc) replaced by the folder listing; both files share parent d_65c76e0b87aa7e9b84d1df | plan/sweeps/oe_blind_review_r1.md finding 14, plan/sweeps/oe_blind_review_r2.md M1; SQL L10 |
| X8 | RESOLVED in this pass | Accuracy | OE 16 | "Owen's Sep 29 remark that everything looks a little slower is about Calvin's video, not a build." | 2_Oracle_Events_Eval.md §2.4 absence wording | The other DMs are now named with the near miss | plan/sweeps/oe_blind_review_r1.md finding 10, plan/sweeps/oe_blind_review_r2.md m3; D05S1S2H55M/1759184077.910139 (hg.py slack messages/D05S1S2H55M/2025-09.json /121) |
| X9 | RESOLVED in this pass | Completeness | OE 7 | "I have a fix locally, need to test it before I open the PR" | 2_Oracle_Events_Eval.md §3.1 deciding record | Owen's note on ZOM-577, which keeps row 19 out of Waiting on QA, was not quoted | plan/sweeps/oe_blind_review_r2.md m4; SQL L197 |
| X10 | RESOLVED in this pass | Accuracy | OE 10 | "Login EMPLOYEE_0025_GITHUB_USERNAME (Arthur Blake in the GitHub user record)" | 2_Oracle_Events_Eval.md §2.3 value the tool returns | The comment read returns a login; the name comes from the user record. The same text in #zombie-prs and Calvin's GitHub mail is named as a second route | plan/sweeps/oe_blind_review_r1.md finding 8, plan/sweeps/oe_blind_review_r2.md m5; SQL L164 |
| X11 | RESOLVED in this pass | Accuracy | OE 17 | "is the earlier version" | 2_Oracle_Events_Eval.md §3.2 consistency | The search also returns the Sep 29 invitation; it is now named as superseded | plan/sweeps/oe_blind_review_r2.md m6; SQL L119 |
| X12 | RESOLVED in this pass | Format | OE 95 | "Add a second tab named Areas" | 2_Oracle_Events_Eval.md §2.7 MULTIPLE_ACTIONS | Adding the tab and filling it were one event; split in two | plan/sweeps/oe_blind_review_r1.md finding 13; SQL L217 |

## Pre-verdict sweep
| Eval 4.0 check (7) | Result |
|---|---|
| One wrong count, ID, channel or tool | none: 38 rows from the grid (SQL L8); fifteen result posts, twelve main; eight merged PRs off the sheet; 20 seeded tickets; 10 / 9 / 20 / 0 / 7 recomputed; write counts 10, 17, 22, 22, 5 asserted when this file is built |
| One missing write | none: 83 writes cover R4 to R8 |
| One Expected fact with no retrieving event | none: OE 21 uses only values read in OEs 1 to 20; blind review r2 confirmed every cross-reference points to an earlier event that holds it |
| One unledgered Expected value or unbacked absence word | none: quotes asserted against their records; the three absence statements (OE 13, 15, 16) are backed by scope-bound checks in plan/sweeps/oe_blind_review_r2.md and hg.py search linear 'icon glow' (0 hits, scan complete) |
| One act-vs-defer conflict | none: ledger §C defer search over Slack, Gmail, Linear, Trello and the SQL found no hold; governing instructions are D0770ET6WBW/1759264805.214409 and the note on ZOM-543 |
| One non-action or final-response event | none: no event states what the agent refrains from or what the final answer says; OE 104 is a required write whose content the prompt sets |
| One prompt-forbidden or unauthorised write | none: every write traces to R4 to R8; no write touches ZOM-543 itself or a ticket outside the 22 |
| One missing recovery or wait event | none: 03_Error_Async_Config.txt is Friction: none |

## Advisory (no effect on the prediction)
| Event | Note |
|---|---|
| OEs 98 to 102 | role left open (writer, commenter or reader): the prompt says only 'shared with everyone on the review invite' |
| OE 97 | creating the sheet inside the folder in one call is an equal route to create-then-move |
| OE 96 | Open reports is given as a count; the list of open reports is an accepted form (platform /prompt) |
| OE 104 | a thread reply under Brian's message is an accepted form of the DM message |

## Tally
Blocking 0 (incomplete 0 · inaccurate 0 · length 0) · moderate 0 (non-action 0 · final-response 0 · format 0) · minor 0 · unresolved 0 · advisory 4 · fixed in this pass 12

## Self-review

**1. Re-read as the eval** (2_Oracle_Events_Eval.md, in order, against this report):
- **Phase 1.2 inventory.** All 104 segments are STEP. There are no headers, notes, response descriptions or non-actions.
- **Phase 1.3 five fields.** Every read names its service, what it reads and how it is found. The decision step cites the events it uses; its tool is not applicable. Every write names its target, its fields and its service; the sign-off lists the catalog tool and its parameters.
- **HARD GATE.** No event says what the agent refrains from doing or what the final answer says.
- **Phase 2.1–2.6.** Service: every value is read where it lives (branches in #builds, merges and reviews in GitHub, ticket notes in Linear, agenda on the Trello card). Tools: all cataloged (Evals/references/tools/catalog.json). Clock: every record time is at or before 2025-10-01T06:59:59Z; the review (2025-10-02T18:00:00Z, evt_342a813cb7765d4a6fce8d) is a semantic future date and is not expected as done. Act-vs-defer: ledger §C, no hold.
- **Phase 2.7 format.** One action per event, numbered, with a service; no arrows and no JSON.
- **Phase 3.1–3.6.** R1–R8 are covered by route. Every search term comes from the prompt or an earlier event. OE sha256 376b94e7eaa9, 40144 characters, 104 events.
- **Phase 4.0** is the 8-row sweep above.

**2. Counter-readings** (one per Coverage row, one per Finding):

| Judgement | Counter-reading (strongest case against) | Resolution (evidence) |
|---|---|---|
| R1 covered (OEs 2, 17, 18) | The agent takes the Trello roadmap card named Queue Manager for the ticket. | Brian's DM says 'I left a note on the ticket' and the note is on ZOM-543 (SQL L217). Holds. |
| R2 covered (OE 1) | The agent reads Brian's Sep 29 line as yesterday's message. | D0770ET6WBW/1759164072.337219 is Sep 29; D0770ET6WBW/1759264805.214409 is Sep 30 20:40 UTC (SQL L64). Holds. |
| R3 covered (OEs 2–19, 21) | A report's status rests on a record no event reads. | Blind review r2 recomputed all 39 from the events' records and found each deciding record read earlier; the one gap (Owen's note on ZOM-577) is now quoted in OE 7 (SQL L197). Holds. |
| R4 covered | A report gets both a move and a new sub-issue, or neither. | 22 moves + 17 creates = 39, asserted when this file is built; ZOM-556 and ZOM-560 are moved, not duplicated (hg.py linear data.json /issues/3632). Holds. |
| R5 covered | The sheet lands outside the folder or lacks the second tab. | Separate events add the Areas tab and move the file into d_36cdb0374c4aad3b8bf741 (SQL L16). Holds. |
| R6 covered | Calvin is also shared, or Leonard is left out. | The event lists five attendees besides Calvin, Leonard among them (SQL L114). Holds. |
| R7 covered | The numbers go on an existing slide. | Brian's DM says 'add one slide' (SQL L64); the event adds a new one. Holds. |
| R8 covered | Only three numbers are sent. | The DM lists five (SQL L64); the message carries 10, 9, 20, 0, 7. Holds. |
| X1 OE 8 | The best case it was harmless: a reader reaches the same records anyway. | A blind reviewer following the draft literally reached a different record or could not check the claim; the corrected span is in the file (hg.py slack messages/C05433XK267/2025-09.json /1127, /1128, /1131, /1132). Fixed. |
| X2 OE 8 | The best case it was harmless: a reader reaches the same records anyway. | A blind reviewer following the draft literally reached a different record or could not check the claim; the corrected span is in the file (hg.py slack messages/C05433XK267/2025-09.json /926). Fixed. |
| X3 OE 14 | The best case it was harmless: a reader reaches the same records anyway. | A blind reviewer following the draft literally reached a different record or could not check the claim; the corrected span is in the file (SQL L275, SQL L281). Fixed. |
| X4 OE 12 | The best case it was harmless: a reader reaches the same records anyway. | A blind reviewer following the draft literally reached a different record or could not check the claim; the corrected span is in the file (hg.py github data.json /pull_requests/2367, /2370, /2371, /2372, /2373, /2375, /2376, /2378, /2379). Fixed. |
| X5 OE 13 | The best case it was harmless: a reader reaches the same records anyway. | A blind reviewer following the draft literally reached a different record or could not check the claim; the corrected span is in the file (plan/sweeps/oe_blind_review_r2.md OE 13 (553 ZOM tickets checked)). Fixed. |
| X6 OE 15 | The best case it was harmless: a reader reaches the same records anyway. | A blind reviewer following the draft literally reached a different record or could not check the claim; the corrected span is in the file (plan/sweeps/oe_blind_review_r2.md OE 14, 15). Fixed. |
| X7 OE 4 | The best case it was harmless: a reader reaches the same records anyway. | A blind reviewer following the draft literally reached a different record or could not check the claim; the corrected span is in the file (SQL L10). Fixed. |
| X8 OE 16 | The best case it was harmless: a reader reaches the same records anyway. | A blind reviewer following the draft literally reached a different record or could not check the claim; the corrected span is in the file (D05S1S2H55M/1759184077.910139 (hg.py slack messages/D05S1S2H55M/2025-09.json /121)). Fixed. |
| X9 OE 7 | The best case it was harmless: a reader reaches the same records anyway. | A blind reviewer following the draft literally reached a different record or could not check the claim; the corrected span is in the file (SQL L197). Fixed. |
| X10 OE 10 | The best case it was harmless: a reader reaches the same records anyway. | A blind reviewer following the draft literally reached a different record or could not check the claim; the corrected span is in the file (SQL L164). Fixed. |
| X11 OE 17 | The best case it was harmless: a reader reaches the same records anyway. | A blind reviewer following the draft literally reached a different record or could not check the claim; the corrected span is in the file (SQL L119). Fixed. |
| X12 OE 95 | The best case it was harmless: a reader reaches the same records anyway. | A blind reviewer following the draft literally reached a different record or could not check the claim; the corrected span is in the file (SQL L217). Fixed. |

**3. Limits.** The three absence statements rest on the second blind reviewer's scope-bound searches and my own Linear search for 'icon glow'; I did not repeat the sweep of all 553 ZOM tickets. The final draft (after the second review's fixes) has not had a third blind pass.

Unresolved: none.

```
STAGE GATE oe-check: PASS — Task_Authoring/task_inputs · 08_OE_Check.md#3dd7a3a0eb57 · 08_Oracle_Events.md#be85999b8fe9 · 08_OE_Writing_Ledger.md#bdd91ead85f4 · __context__#7be566a0936c · __assignment__#d644f7ef43f6 · __policy__#dc4ab5df3cdd · __gate_policy__#cc68bf5564ff · __review__#15d71f843716 · blocking 0 · warnings 0 · checks 21
[PASS] assignment.v3_context: Calvin Price / Game Engineer (Unity VFX); hard cap <70%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 08_OE_Check.md
[PASS] structure.inputs: 2 input(s) present: 08_Oracle_Events.md, 08_OE_Writing_Ledger.md
[PASS] structure.fresh: every output newer than its inputs (08_Oracle_Events.md, 08_OE_Writing_Ledger.md)
[PASS] chain.oe-writing: upstream 'oe-writing' PASS pasted and current (08_OE_Writing_Ledger.md#bdd91ead85f4, 00_Assigments.md#a8cc00ce24ff, 04_Prompt.txt#7f9ab6c62396, 01_Grounding_Dossier.md#88526f435b5f, 01_Universe_Inject.sql#479b8441f52e, 03_Error_Async_Config.txt#52b2d02d66d3, __context__#7be566a0936c, __assignment__#d644f7ef43f6, __policy__#dc4ab5df3cdd, __gate_policy__#cc68bf5564ff, __review__#15d71f843716)
[PASS] structure.sections: 7 required sections present and non-empty (08_OE_Check.md)
[PASS] structure.placeholders: no placeholders in 08_OE_Check.md
[PASS] structure.header_counts: header matches 08_Oracle_Events.md (104 events, 40144 chars)
[PASS] structure.prediction: /oe prediction line present
[PASS] structure.clock: 'Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)' matches the universe
[PASS] evidence.quoted_spans: 12 quoted span(s) verified as exact substrings of 08_Oracle_Events.md
[PASS] evidence.findings_evidence: 12/12 items carry a source pointer (min 100%)
[PASS] evidence.signoff_reread: 104/104 items carry a source pointer (min 100%)
[PASS] structure.sweep: pre-verdict sweep has 8/7 rows
[PASS] structure.tally: tally Blocking 0 vs 0 BLOCKING findings
[PASS] review.counter_readings: 20 evidenced counter-readings (of 20 found; need ≥ 20) in 08_OE_Check.md
[PASS] review.coverage: self-review addresses all 1 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] readiness.context: explicit task/revision and current upstream evidence verified
[PASS] handoff.pasted: pasted into the Self-review by --paste
```


## Reminders
- The tool-call minimum is measured on the 6-rollout average, never on the OE count.
- The OE field blocks pasting: type the events exactly as in 08_Oracle_Events.md (sha256 in the Self-review).
