# 08 OE Check — Douglas beta server register (dg-beta-server-signoff)
Checked 2026-10-27 · Events 66 · Characters 28064 (300–50,000: ok) · Ledger 2026-10-27 (08_OE_Writing_Ledger.md, oe-writing gate PASS)
/oe prediction (a prediction only; /oe gives the verdict): PASS 5
Completeness 5 · Accuracy 5 · Path feasibility SUPPORTED · Task solvability SUPPORTED_BY_OE

Clock: 2025-10-01T00:00:00Z (00_Assigments.md). Every record time in the events is on or before Sep 30 2025 21:12:44 UTC; the go/no-go (Oct 2) and the beta (Oct 10) appear only as quoted future dates, never as done.

## Inventory
All 66 segments are STEP events; no CONTEXT, RESPONSE_DESCRIPTION or NON_ACTION segment. Reads OE 1–13, 15–31; calculations OE 14 and OE 32; writes OE 33, 34, 36–66 (one write per event); status lookup OE 35.

| Segment (quoted start) | Role | Event |
|---|---|---|
| "Read Arthur's sign-off ask in Douglas's Slack DM with Arthur" | STEP | OE 1 |
| "Find the beta card on the ZM ROADMAP Trello board and open i" | STEP | OE 2 |
| "Read the comment on that card (Trello card actions / comment" | STEP | OE 3 |
| "Open the ZM Beta page in Confluence named by rule 6 (Conflue" | STEP | OE 4 |
| "Read the comments on that page (Confluence page comments of " | STEP | OE 5 |
| "Find Arthur's sign-off folder in Drive (Drive search "ZM Bet" | STEP | OE 6 |
| "Read the match3d-backend prod deploys doc named by rule 3 (D" | STEP | OE 7 |
| "Find the server freeze on Douglas's calendar (Google Calenda" | STEP | OE 8 |
| "Read both tabs of Douglas's deploy log (Drive search "deploy" | STEP | OE 9 |
| "Find Leonard's go/no-go email in Douglas's Gmail (Gmail sear" | STEP | OE 10 |
| "Open that whole thread (Gmail thread douglas@harmonygames.co" | STEP | OE 11 |
| "List the ZOM team's Done tickets in Linear and keep those co" | STEP | OE 12 |
| "Read the comments on each of the 73 tickets to find which fi" | STEP | OE 13 |
| "Work out the register's ticket set from rule 1, the card com" | STEP | OE 14 |
| "Find the backend repository in GitHub (repository search "ma" | STEP | OE 15 |
| "Check whether match3d-backend#38 (ZOM-459) is on prod: read " | STEP | OE 16 |
| "Check whether match3d-backend#39 (ZOM-509) is on prod: read " | STEP | OE 17 |
| "Check whether match3d-backend#40 (ZOM-336) is on prod: read " | STEP | OE 18 |
| "Check whether match3d-backend#41 (ZOM-392) is on prod: read " | STEP | OE 19 |
| "Check whether match3d-backend#42 (ZOM-503 (first change)) is" | STEP | OE 20 |
| "Check whether match3d-backend#43 (ZOM-518) is on prod: read " | STEP | OE 21 |
| "Check whether match3d-backend#44 (ZOM-499) is on prod: read " | STEP | OE 22 |
| "Check whether match3d-backend#45 (ZOM-531) is on prod: read " | STEP | OE 23 |
| "Check whether match3d-backend#46 (ZOM-537) is on prod: read " | STEP | OE 24 |
| "Check whether match3d-backend#47 (ZOM-444) is on prod: read " | STEP | OE 25 |
| "Check whether match3d-backend#48 (ZOM-487) is on prod: read " | STEP | OE 26 |
| "Check whether match3d-backend#50 (ZOM-550) is on prod: read " | STEP | OE 27 |
| "Check whether match3d-backend#51 (ZOM-435) is on prod: read " | STEP | OE 28 |
| "Check whether match3d-backend#52 (ZOM-503 (second change)) i" | STEP | OE 29 |
| "Check whether match3d-backend#54 (ZOM-557) is on prod: read " | STEP | OE 30 |
| "Check who the reviewer EMPLOYEE_0025_GITHUB_USERNAME is, for" | STEP | OE 31 |
| "Decide each register row from rules 2 to 4, the doc, the fre" | STEP | OE 32 |
| "Create the register as a Google Sheet inside the "ZM Beta si" | STEP | OE 33 |
| "Share the register with Leonard, as his email asked (Drive s" | STEP | OE 34 |
| "Look up the ZOM team's workflow states in Linear to find Tod" | STEP | OE 35 | Todo exists for team ZOM beside 7 other states | linear data.json via hg.py: team_ZOM issue state_id values Done, Todo, Backlog, Canceled, In Progress, Duplicate, In Validation, Regression | 8 state names as listed (no raw id claimed) | Match |
| "Move ZOM-336 back to Todo, per rule 5 (Linear update of ZOM-" | STEP | OE 36 |
| "Comment on ZOM-336 with the change still to go out, per rule" | STEP | OE 37 |
| "Move ZOM-392 back to Todo, per rule 5 (Linear update of ZOM-" | STEP | OE 38 |
| "Comment on ZOM-392 with the change still to go out, per rule" | STEP | OE 39 |
| "Move ZOM-503 back to Todo, per rule 5 (Linear update of ZOM-" | STEP | OE 40 |
| "Comment on ZOM-503 with the change still to go out, per rule" | STEP | OE 41 |
| "Move ZOM-518 back to Todo, per rule 5 (Linear update of ZOM-" | STEP | OE 42 |
| "Comment on ZOM-518 with the change still to go out, per rule" | STEP | OE 43 | ZOM-518 comment: #43 had no Approve; with the freeze on it now needs Arthur's Approve before redeploy | harmonygames-Games/match3d-backend#43 (L355 prod: 2025-09-04 12:50 UTC; only review #43#rev_1 COMMENTED); doc f_470ae81236d5bd39045dc1 freeze clause (L15); evt_0f489eb7fb46ada9660881 start 2025-09-26 22:00 UTC | matches the doc at the clock | Match |
| "Move ZOM-550 back to Todo, per rule 5 (Linear update of ZOM-" | STEP | OE 44 |
| "Comment on ZOM-550 with the change still to go out, per rule" | STEP | OE 45 |
| "Move ZOM-435 back to Todo, per rule 5 (Linear update of ZOM-" | STEP | OE 46 |
| "Comment on ZOM-435 with the change still to go out, per rule" | STEP | OE 47 |
| "Move ZOM-557 back to Todo, per rule 5 (Linear update of ZOM-" | STEP | OE 48 |
| "Comment on ZOM-557 with the change still to go out, per rule" | STEP | OE 49 |
| "Move ZOM-256 back to Todo, per rule 5 (Linear update of ZOM-" | STEP | OE 50 |
| "Comment on ZOM-256 with the change still to go out, per rule" | STEP | OE 51 |
| "Move ZOM-487 back to Todo, per rule 5 (Linear update of ZOM-" | STEP | OE 52 |
| "Comment on ZOM-487 with the change still to go out, per rule" | STEP | OE 53 |
| "Move ZOM-537 back to Todo, per rule 5 (Linear update of ZOM-" | STEP | OE 54 |
| "Comment on ZOM-537 with the change still to go out, per rule" | STEP | OE 55 |
| "Move ZOM-444 back to Todo, per rule 5 (Linear update of ZOM-" | STEP | OE 56 |
| "Comment on ZOM-444 with the change still to go out, per rule" | STEP | OE 57 |
| "Move ZOM-531 back to Todo, per rule 5 (Linear update of ZOM-" | STEP | OE 58 |
| "Comment on ZOM-531 with the change still to go out, per rule" | STEP | OE 59 |
| "Move ZOM-459 back to Todo, per rule 5 (Linear update of ZOM-" | STEP | OE 60 |
| "Comment on ZOM-459 with the change still to go out, per rule" | STEP | OE 61 |
| "Move ZOM-509 back to Todo, per rule 5 (Linear update of ZOM-" | STEP | OE 62 |
| "Comment on ZOM-509 with the change still to go out, per rule" | STEP | OE 63 |
| "Move ZOM-436 back to Todo, per rule 5 (Linear update of ZOM-" | STEP | OE 64 |
| "Comment on ZOM-436 with the change still to go out, per rule" | STEP | OE 65 |
| "Reply to Arthur in Douglas's DM with Arthur with what he ask" | STEP | OE 66 |

## Coverage
| R / F | Event(s) | Covered / missing / partial | Route (ledger / other valid) |
|---|---|---|---|
| R1 ask (F1) | OE 1 | Covered | ledger |
| R2 in-scope set (F2, F3, F8, F11, F12, F13, F14) | OE 2, 3, 9, 10, 11, 12, 13, 14 | Covered (population derived before the filter: 73 → 17) | ledger |
| R3 server changes and on prod (F5–F8, F16–F31) | OE 4, 5, 7, 8, 9, 15, 16–30, 31, 32 | Covered (every PR of the 17 tickets, all three GitHub surfaces; freeze identity via OE 31) | ledger |
| R4 register in the folder (F4, F10, F31) | OE 4, 6, 33 | Covered (folder pinned by the page; one create-in-folder write) | ledger; create + move + update is another valid route |
| R5 DM reply (F1, F32) | OE 66 | Covered | ledger |
| R6 Todo + comment on the 15 (F2, F15, F31) | OE 35, 36–65 | Covered (15 moves, 15 comments, one write each) | ledger |
| R7 share with Leonard (F9, F11) | OE 10, 11, 34 | Covered (after OE 33, as the email asks) | ledger |

## Expected-data sign-off
| Event | Claim (quoted) | Source re-read (hg.py pointer) | Value found | Match / minor / wrong / unresolved |
|---|---|---|---|---|
| OE 1 | Arthur's ask, 2:12 PM PT, newest in the DM | 01_Universe_Inject.sql L49, D05QQF7V404/1759266764.508127; DM shard D05QQF7V404/2025-09.json last base ts 1758730042 | text and time as quoted | Match |
| OE 2 | Card rules 1–6, 1 comment; client card on the same list | 01_Universe_Inject.sql L57 (desc, badges comments 1), L62 (client card); trello 68dabfe9bc2e8b969782e22d | rules verbatim; comments 1 | Match |
| OE 3 | Comment Sep 30 8:05 AM PT, imports count | 01_Universe_Inject.sql L66; trello 68dbf1b73eba0ba580f67a6e | text and time as quoted | Match |
| OE 4 | Page body, author user_EMPLOYEE_0025, created Sep 29 17:15 UTC | 01_Universe_Inject.sql L30; page_zm_beta_oct10; run-1 confluence_search result | body and created_at as quoted | Match |
| OE 5 | Two comments: user_EMPLOYEE_0003 10:12 UTC; reply user_EMPLOYEE_0025 11:03 UTC | 01_Universe_Inject.sql L34, L36; comment_zm_beta_oct10_c2 on page_zm_beta_oct10 | authors, parent and text as quoted | Match |
| OE 6 | Folder ZM Beta sign-off, owner Arthur, 3 writers; client QA folder Douglas reader | 01_Universe_Inject.sql L6, L9; d_69fcebc484d472907b0b5c, d_d71300168ca5dffa4db8b3 | owner and roles as stated | Match |
| OE 7 | Doc rules (prod branch, prod:, prior non-author Approve, rollback, imports, freeze) | 01_Universe_Inject.sql L15 body_text; f_470ae81236d5bd39045dc1 | every clause in body_text | Match |
| OE 8 | Freeze event starts 22:00 UTC Sep 26, description | 01_Universe_Inject.sql L156; evt_0f489eb7fb46ada9660881; run-5 gcal_search_events result (description) | start/end/organizer as stated | Match |
| OE 9 | Prod deploys row 1 and last row; 9 Console & imports rows | 01_Universe_Inject.sql L21, L23 grid_json; f_78bedc46245090a160d2dd | all rows as listed | Match |
| OE 10 | from:leonard results include Leonard's Sep 30 message in thread 1844721277206562572 | 01_Universe_Inject.sql L68, L71; douglas@harmonygames.co/1844721277206562572 (from leonard.hayes@harmonygames.co) | present in the mailbox | Match |
| OE 11 | Thread of 2 messages, both bodies | 01_Universe_Inject.sql L71, L96; douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> | bodies, senders, times as quoted | Match |
| OE 12 | 73 tickets after the cut; ZOM-459 in, ZOM-461 out, ZOM-457 parent | linear data.json /issues (recomputed: 73, equals cohort.json), /issues/3587, /3589, /3591 | 73; boundary times as stated | Match |
| OE 13 | One comment per ticket; 18 name a server change; 53 others none | 01_Universe_Inject.sql L735–L880 (77 linear_comments; base comments 0); cmt_0b9e52e7a05129c16301 … cmt_b4c2115bb1a33be756ae (hg.py: linear data.json comments length 0) | fragments are substrings; 18 + ZOM-436 + ZOM-457 + 53 = 73 | Match |
| OE 14 | 17-ticket set | Derived from L57, L66, L96 and L735–L880 (ledger F14); ZOM-436 via douglas@harmonygames.co/1844721277206562572; ZOM-547, ZOM-553 out | 17 as listed | Match |
| OE 15 | harmonygames-Games/match3d-backend | hg.py search github "match3d-backend": data.json /repositories/11/full_name | match | Match |
| OE 16 | #38: author, reviews, prod:/rollback:/dev comments, inline comments, verdict | 01_Universe_Inject.sql L195–L211; harmonygames-Games/match3d-backend#38 (script cross-check of every date, review state and author) | all match | Match |
| OE 17 | #39: author, reviews, prod:/rollback:/dev comments, inline comments, verdict | 01_Universe_Inject.sql L227–L243; harmonygames-Games/match3d-backend#39 (script cross-check of every date, review state and author) | all match | Match |
| OE 18 | #40: author, reviews, prod:/rollback:/dev comments, inline comments, verdict | 01_Universe_Inject.sql L259–L271; harmonygames-Games/match3d-backend#40 (script cross-check of every date, review state and author) | all match | Match |
| OE 19 | #41: author, reviews, prod:/rollback:/dev comments, inline comments, verdict | 01_Universe_Inject.sql L285–L299; harmonygames-Games/match3d-backend#41 (script cross-check of every date, review state and author) | all match | Match |
| OE 20 | #42: author, reviews, prod:/rollback:/dev comments, inline comments, verdict | 01_Universe_Inject.sql L315–L329; harmonygames-Games/match3d-backend#42 (script cross-check of every date, review state and author) | all match | Match |
| OE 21 | #43: author, reviews, prod:/rollback:/dev comments, inline comments, verdict | 01_Universe_Inject.sql L345–L357; harmonygames-Games/match3d-backend#43 (script cross-check of every date, review state and author) | all match | Match |
| OE 22 | #44: author, reviews, prod:/rollback:/dev comments, inline comments, verdict | 01_Universe_Inject.sql L371–L391; harmonygames-Games/match3d-backend#44 (script cross-check of every date, review state and author) | all match | Match |
| OE 23 | #45: author, reviews, prod:/rollback:/dev comments, inline comments, verdict | 01_Universe_Inject.sql L413–L429; harmonygames-Games/match3d-backend#45 (script cross-check of every date, review state and author) | all match | Match |
| OE 24 | #46: author, reviews, prod:/rollback:/dev comments, inline comments, verdict | 01_Universe_Inject.sql L447–L463; harmonygames-Games/match3d-backend#46 (script cross-check of every date, review state and author) | all match | Match |
| OE 25 | #47: author, reviews, prod:/rollback:/dev comments, inline comments, verdict | 01_Universe_Inject.sql L479–L493; harmonygames-Games/match3d-backend#47 (script cross-check of every date, review state and author) | all match | Match |
| OE 26 | #48: author, reviews, prod:/rollback:/dev comments, inline comments, verdict | 01_Universe_Inject.sql L509–L523; harmonygames-Games/match3d-backend#48 (script cross-check of every date, review state and author) | all match | Match |
| OE 27 | #50: author, reviews, prod:/rollback:/dev comments, inline comments, verdict | 01_Universe_Inject.sql L569–L585; harmonygames-Games/match3d-backend#50 (script cross-check of every date, review state and author) | all match | Match |
| OE 28 | #51: author, reviews, prod:/rollback:/dev comments, inline comments, verdict | 01_Universe_Inject.sql L603–L619; harmonygames-Games/match3d-backend#51 (script cross-check of every date, review state and author) | all match | Match |
| OE 29 | #52: author, reviews, prod:/rollback:/dev comments, inline comments, verdict | 01_Universe_Inject.sql L637–L651; harmonygames-Games/match3d-backend#52 (script cross-check of every date, review state and author) | all match | Match |
| OE 30 | #54: author, reviews, prod:/rollback:/dev comments, inline comments, verdict | 01_Universe_Inject.sql L697–L713; harmonygames-Games/match3d-backend#54 (script cross-check of every date, review state and author) | all match | Match |
| OE 31 | EMPLOYEE_0025_GITHUB_USERNAME = Arthur Blake | trajectory-run-4.json github_get_user result (name Arthur Blake, arthur.blake@harmonygames.co) for the reviewer login on harmonygames-Games/match3d-backend#46#rev_2 (L461) | match | Match |
| OE 32 | 17 rows, 2 Y (ZOM-499, ZOM-510), 15 N | Derived (ledger F31); doc L15, freeze L156, log L23, amendments L36, L96, L211, L243, L463; ZOM-499 (linear data.json via hg.py: state Done at the clock) | recomputed per PR and import | Match |
| OE 33 | Register file in d_69fcebc484d472907b0b5c, 17 rows | gdrive_create_file (name, content, parentId, driveMimeType); folder d_69fcebc484d472907b0b5c (L6, Douglas writer) | feasible write; rows = OE 32 | Match |
| OE 34 | Leonard commenter on the file | gdrive_share_file (fileId, emailAddress, role, type); douglas@harmonygames.co/1844721277206562572 body | role commenter as asked | Match |
| OE 35 | Todo exists for team ZOM beside 7 other states | linear data.json via hg.py: team_ZOM issue state_id values Done, Todo, Backlog, Canceled, In Progress, Duplicate, In Validation, Regression | 8 state names as listed (no raw id claimed) | Match |
| OE 36 | ZOM-336 Done → Todo | linear_update_issue (id, state); state_5599a57e03a35620; ledger F31; ZOM-336 (linear data.json via hg.py: state Done at the clock) | N row, state Done at the clock | Match |
| OE 37 | ZOM-336 comment naming the change still to go out | linear_create_comment (issueId, body); ledger F31; ZOM-336 (linear data.json via hg.py: state Done at the clock) | change matches OE 32 | Match |
| OE 38 | ZOM-392 Done → Todo | linear_update_issue (id, state); state_5599a57e03a35620; ledger F31; ZOM-392 (linear data.json via hg.py: state Done at the clock) | N row, state Done at the clock | Match |
| OE 39 | ZOM-392 comment naming the change still to go out | linear_create_comment (issueId, body); ledger F31; ZOM-392 (linear data.json via hg.py: state Done at the clock) | change matches OE 32 | Match |
| OE 40 | ZOM-503 Done → Todo | linear_update_issue (id, state); state_5599a57e03a35620; ledger F31; ZOM-503 (linear data.json via hg.py: state Done at the clock) | N row, state Done at the clock | Match |
| OE 41 | ZOM-503 comment naming the change still to go out | linear_create_comment (issueId, body); ledger F31; ZOM-503 (linear data.json via hg.py: state Done at the clock) | change matches OE 32 | Match |
| OE 42 | ZOM-518 Done → Todo | linear_update_issue (id, state); state_5599a57e03a35620; ledger F31; ZOM-518 (linear data.json via hg.py: state Done at the clock) | N row, state Done at the clock | Match |
| OE 43 | ZOM-518 comment: #43 had no Approve; with the freeze on it now needs Arthur's Approve before redeploy | harmonygames-Games/match3d-backend#43 (L355 prod: 2025-09-04 12:50 UTC; only review #43#rev_1 COMMENTED); doc f_470ae81236d5bd39045dc1 freeze clause (L15); evt_0f489eb7fb46ada9660881 start 2025-09-26 22:00 UTC | matches the doc at the clock | Match |
| OE 44 | ZOM-550 Done → Todo | linear_update_issue (id, state); state_5599a57e03a35620; ledger F31; ZOM-550 (linear data.json via hg.py: state Done at the clock) | N row, state Done at the clock | Match |
| OE 45 | ZOM-550 comment naming the change still to go out | linear_create_comment (issueId, body); ledger F31; ZOM-550 (linear data.json via hg.py: state Done at the clock) | change matches OE 32 | Match |
| OE 46 | ZOM-435 Done → Todo | linear_update_issue (id, state); state_5599a57e03a35620; ledger F31; ZOM-435 (linear data.json via hg.py: state Done at the clock) | N row, state Done at the clock | Match |
| OE 47 | ZOM-435 comment naming the change still to go out | linear_create_comment (issueId, body); ledger F31; ZOM-435 (linear data.json via hg.py: state Done at the clock) | change matches OE 32 | Match |
| OE 48 | ZOM-557 Done → Todo | linear_update_issue (id, state); state_5599a57e03a35620; ledger F31; ZOM-557 (linear data.json via hg.py: state Done at the clock) | N row, state Done at the clock | Match |
| OE 49 | ZOM-557 comment naming the change still to go out | linear_create_comment (issueId, body); ledger F31; ZOM-557 (linear data.json via hg.py: state Done at the clock) | change matches OE 32 | Match |
| OE 50 | ZOM-256 Done → Todo | linear_update_issue (id, state); state_5599a57e03a35620; ledger F31; ZOM-256 (linear data.json via hg.py: state Done at the clock) | N row, state Done at the clock | Match |
| OE 51 | ZOM-256 comment naming the change still to go out | linear_create_comment (issueId, body); ledger F31; ZOM-256 (linear data.json via hg.py: state Done at the clock) | change matches OE 32 | Match |
| OE 52 | ZOM-487 Done → Todo | linear_update_issue (id, state); state_5599a57e03a35620; ledger F31; ZOM-487 (linear data.json via hg.py: state Done at the clock) | N row, state Done at the clock | Match |
| OE 53 | ZOM-487 comment naming the change still to go out | linear_create_comment (issueId, body); ledger F31; ZOM-487 (linear data.json via hg.py: state Done at the clock) | change matches OE 32 | Match |
| OE 54 | ZOM-537 Done → Todo | linear_update_issue (id, state); state_5599a57e03a35620; ledger F31; ZOM-537 (linear data.json via hg.py: state Done at the clock) | N row, state Done at the clock | Match |
| OE 55 | ZOM-537 comment naming the change still to go out | linear_create_comment (issueId, body); ledger F31; ZOM-537 (linear data.json via hg.py: state Done at the clock) | change matches OE 32 | Match |
| OE 56 | ZOM-444 Done → Todo | linear_update_issue (id, state); state_5599a57e03a35620; ledger F31; ZOM-444 (linear data.json via hg.py: state Done at the clock) | N row, state Done at the clock | Match |
| OE 57 | ZOM-444 comment naming the change still to go out | linear_create_comment (issueId, body); ledger F31; ZOM-444 (linear data.json via hg.py: state Done at the clock) | change matches OE 32 | Match |
| OE 58 | ZOM-531 Done → Todo | linear_update_issue (id, state); state_5599a57e03a35620; ledger F31; ZOM-531 (linear data.json via hg.py: state Done at the clock) | N row, state Done at the clock | Match |
| OE 59 | ZOM-531 comment naming the change still to go out | linear_create_comment (issueId, body); ledger F31; ZOM-531 (linear data.json via hg.py: state Done at the clock) | change matches OE 32 | Match |
| OE 60 | ZOM-459 Done → Todo | linear_update_issue (id, state); state_5599a57e03a35620; ledger F31; ZOM-459 (linear data.json via hg.py: state Done at the clock) | N row, state Done at the clock | Match |
| OE 61 | ZOM-459 comment naming the change still to go out | linear_create_comment (issueId, body); ledger F31; ZOM-459 (linear data.json via hg.py: state Done at the clock) | change matches OE 32 | Match |
| OE 62 | ZOM-509 Done → Todo | linear_update_issue (id, state); state_5599a57e03a35620; ledger F31; ZOM-509 (linear data.json via hg.py: state Done at the clock) | N row, state Done at the clock | Match |
| OE 63 | ZOM-509 comment naming the change still to go out | linear_create_comment (issueId, body); ledger F31; ZOM-509 (linear data.json via hg.py: state Done at the clock) | change matches OE 32 | Match |
| OE 64 | ZOM-436 Done → Todo | linear_update_issue (id, state); state_5599a57e03a35620; ledger F31; ZOM-436 (linear data.json via hg.py: state Done at the clock) | N row, state Done at the clock | Match |
| OE 65 | ZOM-436 comment naming the change still to go out | linear_create_comment (issueId, body); ledger F31; ZOM-436 (linear data.json via hg.py: state Done at the clock) | change matches OE 32 | Match |
| OE 66 | DM reply with 2 of 17 on prod and the 15 keys | slack_send_message (channel, text); D05QQF7V404/1759266764.508127 | matches OE 32 | Match |

Quotes: every quoted string of 6+ characters in 08_Oracle_Events.md was matched by script against the parsed SQL rows (base_check.parse_sql over 01_Universe_Inject.sql, sha256 2131bbeff16b) or the base export (hg.py: "Algo Level Issues" linear data.json /issues/3587); 0 unmatched. Every PR event's dates, review states, reviewers and authors were cross-checked by script against the github rows of that PR; 0 mismatches. Pacific times recomputed at UTC−7 (PDT).

## Findings
| # | Severity | Component | Event | Quoted span | Rule (Eval § / source) | What is wrong | Evidence (ledger fact + source pointer) |
|---|---|---|---|---|---|---|---|
| 1 | ADVISORY | Readability | OE 10 | The results include Leonard's Sep 30 message | Eval 4.1A | No ranking claim any more (the /oe round-1 evidence limits named search ranking as not runtime-observed); OE 11 opens the thread by id | F9; douglas@harmonygames.co/1844721277206562572 (L68, L71) |
| 2 | ADVISORY | Readability | OE 25 | Whether #47 counts turns on who EMPLOYEE_0025_GITHUB_USERNAME is (OE 31). | Eval 3.2 | Points forward to OE 31 for the reviewer's identity; ZOM-444's value does not depend on it | F25; harmonygames-Games/match3d-backend#47 |
| 3 | ADVISORY | Route | OE 33 | create one Google Sheets file with the "ZM Beta sign-off" folder as its parent | Eval 3.1 | One route shown; creating the sheet, moving it and writing rows is equally valid and is not missing | F10, F31; d_69fcebc484d472907b0b5c |

## Pre-verdict sweep
| Eval 4.0 check (7) | Result |
|---|---|
| 1 One wrong count/ID/channel/tool | None: 73, 17, 18, 53, 2/15 recomputed; ids from tool output (state_5599a57e03a35620, thread 1844721277206562572) |
| 2 One missing write | None: register (OE 33), share (OE 34), 15 moves, 15 comments, DM (OE 66) |
| 3 One Expected fact with no retrieving event | None after the fixes listed in the Self-review (unread Slack traps and identity labels removed) |
| 4 One act-vs-defer conflict | None: ledger §C defer search complete; #50 "ship it after go/no-go" defers a deploy, no event deploys |
| 5 One non-action or final-response event | None |
| 6 One prompt-forbidden write | None: every write traces to a prompt span (ledger §C); no reply to Leonard's email, no new ticket |
| 7 One missing recovery/wait event | Not applicable: Friction none (03_Error_Async_Config.txt) |

## Advisory (no effect on the prediction)
| Event | Note |
|---|---|
| OE 13 | Long Expected line (18 fragments); kept because each fragment decides a register row |
| OE 16–30 | One event per PR; a reviewer may prefer them grouped, /oe does not score redundancy |

## Tally
Blocking 0 (incomplete 0 · inaccurate 0 · length 0) · moderate 0 (non-action 0 · final-response 0 · format 0) · minor 0 · unresolved 0 · advisory 3

## Self-review
Walked Eval 1.2, 1.3, the HARD GATE, 2.1–2.7, 3.1–3.6 and 4.0 in order against 08_Oracle_Events.md.

Defects found in the first draft during this check and fixed in 08_Oracle_Events.md before this report (each verified against tool output from the baseline trajectories or the SQL):
1. Unobservable creation times removed: card (OE 2), folder (OE 6), doc modified time (OE 7).
2. Unobservable counts removed: "(#80)", "(#81)" idShort, "The page has 2 comments" (OE 4).
3. Author names the tool does not return replaced by returned ids: page and comment authors user_EMPLOYEE_0025 / user_EMPLOYEE_0003 (OE 4, 5); card comment author (OE 3); calendar organizer email (OE 8).
4. Traps about records no event reads removed (Sep 19 freeze message, Sep 22 DM claim, Vincent DM, Oliver's Sep 27 summary) — they were Expected facts with no retrieving event.
5. Exclusive claim removed: "the reply-all is seen only in the thread" (a "go/no-go" search would also return it).
6. GitHub identity labels "(Douglas)", "(the contractor)", "(Arthur)" removed from PR events; the Arthur identity is now produced by OE 31 before OE 32 uses it (dependency order).
7. Confluence search changed to the text search "beta" (a CQL title search on "ZM Beta" returned 0 in run-1).
8. Gmail search event now states only what the search returns; the message bodies moved to the thread read (OE 11).
9. Register creation narrowed to one write (MULTIPLE_ACTIONS risk); "No rows for…" and "Same ticket, no new ticket" removed (NON_ACTION risk).

/oe round 1 (report 6ad90ea979eb9e5d89f8879f_2_oe.md, NON-FAIL, PARTIAL, reviewed OE sha256 3118b9e88a9e…) and the fixes applied:
10. OE 35 UNRESOLVED: the raw state id state_5599a57e03a35620 and type "unstarted" came only from run output. Removed; the event now claims the 8 state names, which match team_ZOM issue states in linear data.json (hg.py).
11. OE 43 MINOR: the ZOM-518 comment named "an Approve from someone other than its author"; at the clock the freeze clause of f_470ae81236d5bd39045dc1 requires Arthur's Approve. Reworded to the reviewer's checked text.
12. Sweep of the same classes over all 66 events. Run-output-only claims: OE 10's "first (newest) result" ranking (named in the report's evidence limits) reworded to "results include"; no other event states a value seen only in run output (OE 31's user record is base GitHub data, verified by the reviewer). Approval-condition claims: OE 41 and OE 45 already say Arthur's Approve; ZOM-336, ZOM-392, ZOM-435, ZOM-557 comments state no approval condition. OE 12 parameters now say the list call has no completion-date filter (catalog linear_list_issues params) and the results are paged, per the readability note.

Re-verified: every quoted value re-read by script from the parsed SQL (0 unmatched); PR facts script-checked per PR (0 mismatches); the 73-ticket population recomputed from linear data.json via hg.py pointers /issues/3587, /3589, /3591; repo via hg.py search github "match3d-backend" (/repositories/11); tool-return shapes from the baseline trajectories (run-1 confluence, run-2 gmail and linear statuses, run-4 github_get_user, run-5 gcal).

| # | Counter-reading | Resolution (evidence) |
|---|---|---|
| 1 | R1 COVERED counter: OE 1 reads "latest messages" but the ask could be missed if the DM has newer ones | The ask is the newest message (DM shard last base ts 1758730042 < 1759266764.508127, L49) |
| 2 | R2 COVERED counter: the population is narrowed before it is derived | OE 12 lists all 73 Done tickets in the window first; OE 13 reads all 73; OE 14 filters (F12, F13) |
| 3 | R2 counter: ZOM-436 enters without a retrieving event | OE 11 quotes the reply-all naming ZOM-436 (L96); OE 13 shows its device-test note (cmt_7c7780e6f01e8b2c5103) |
| 4 | R3 COVERED counter: inline review comments are only on three PRs, so reading them on all 15 is unsupported | Each PR event states the inline result; "No inline review comments" is a tool-observed negative (only #38#rc_1, #39#rc_1, #46#rc_1 exist, L211, L243, L463) |
| 5 | R3 VERIFIED counter: #47's prod deploy inside the freeze should not count | Doc L15: in the freeze the Approve has to be Arthur's; #47#rev_2 by EMPLOYEE_0025_GITHUB_USERNAME at 16:05 precedes prod 16:20 (L493, L489); OE 31 confirms the identity |
| 6 | R3 VERIFIED counter: ZOM-499 is wrong because #44 was rolled back | #44#c_4 "prod: 2025-09-22 17:30 UTC" after the rollback and before the freeze 2025-09-26 22:00 (L385, L156) |
| 7 | R4 COVERED counter: the single-route OE 33 makes the move-then-write route look missing | Eval 3.1: a different valid route is judged under Accuracy, never missing (Finding 3) |
| 8 | R5 COVERED counter: OE 66 is a final-response description | It is a Slack write with the content the ask requires (D05QQF7V404/1759266764.508127), allowed for a required write's Expected line |
| 9 | R6 COVERED counter: the Todo state id is invented | Returned by linear_list_issue_statuses in run-2 (state_5599a57e03a35620, team ZOM) |
| 10 | R7 COVERED counter: the share should go to the folder, or wait for a reply to Leonard | Leonard's email: "share it with me directly. Comment access please" (L71); OE 34 shares the file after OE 33 |
| 11 | Finding 1 counter (false positive?): newest-first ordering makes OE 10 inaccurate | Observed in run-2 (first result is Leonard's message); OE 11 reads the thread by id, so the path holds either way — ADVISORY, not MINOR |
| 12 | Finding 2 counter (should be MINOR): forward reference is a dependency defect | The OE 25 Expected states only observed review/comment facts; the verdict uses OE 31 in OE 32, after it (F25, F31) |
| 13 | Finding 3 counter (should be INCOMPLETE): only one creation route | The listed route completes R4 alone (gdrive_create_file name, content, parentId exist in catalog.json) |
| 14 | MINOR counter on OE 13: "Each ticket has one comment" is an exclusive claim | 77 seeded comments on 77 distinct issues, 73 of them the cohort; base linear comments 0 (data.json comments length 0) |
| 16 | OE 43 counter (fix over-reaches): #43 might also count with any non-author Approve | Doc L15: from the freeze until the beta ships the Approve has to be Arthur's; freeze evt_0f489eb7fb46ada9660881 started 2025-09-26 22:00 UTC, the beta is Oct 10 (page_zm_beta_oct10), so at the clock only Arthur's Approve counts |
| 17 | OE 35 counter (now incomplete): without the state id the move cannot be made | linear_update_issue takes state by name (catalog param state); the /oe report's checked fix drops the id (team_ZOM states by name in linear data.json) |
| 15 | VERIFIED counter on OE 8: the freeze is Monday the 29th | The event (L156) starts Fri Sep 26 22:00 UTC, description "Pulled in from Monday so QA gets the weekend on a frozen prod."; doc L15 points to the calendar |

Unresolved: none.

```
STAGE GATE oe-check: PASS — Task_Authoring-2/task_inputs · 08_OE_Check.md#082cede0afb1 · 08_Oracle_Events.md#e14b83e3c321 · blocking 0 · warnings 0 · checks 17
[PASS] structure.outputs: 1 output(s) present: 08_OE_Check.md
[PASS] structure.inputs: 2 input(s) present: 08_Oracle_Events.md, 08_OE_Writing_Ledger.md
[PASS] structure.fresh: every output newer than its inputs (08_Oracle_Events.md, 08_OE_Writing_Ledger.md)
[PASS] chain.oe-writing: upstream 'oe-writing' PASS pasted and current (08_OE_Writing_Ledger.md#06e620614b2e)
[PASS] structure.sections: 7 required sections present and non-empty (08_OE_Check.md)
[PASS] structure.placeholders: no placeholders in 08_OE_Check.md
[PASS] structure.header_counts: header matches 08_Oracle_Events.md (66 events, 28064 chars)
[PASS] structure.prediction: /oe prediction line present
[PASS] evidence.quoted_spans: 3 quoted span(s) verified as exact substrings of 08_Oracle_Events.md
[PASS] evidence.findings_evidence: 3/3 items carry a source pointer (min 100%)
[PASS] evidence.signoff_reread: 66/66 items carry a source pointer (min 100%)
[PASS] structure.sweep: pre-verdict sweep has 7/7 rows
[PASS] structure.tally: tally Blocking 0 vs 0 BLOCKING findings
[PASS] review.counter_readings: 17 evidenced counter-readings (of 17 found; need ≥ 10) in 08_OE_Check.md
[PASS] review.coverage: self-review addresses all 1 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```
