# Grounding Dossier — calvin_qm_epic · injection rev2 · contains no prompt, OE or criterion text

Persona: Calvin Price <calvin.price@harmonygames.co>, Game Engineer (Unity VFX). Universe: synth-cut, clock 2025-10-01T07:00Z, seed bound 2025-10-01T00:00:00Z (Tue Sep 30 17:00 PT). SQL: 129 INSERT, 11 UPDATE, 10 schemas. Every base read at this stage went through `tools/hg.py`; one directory listing of the mail export's file names was made by mistake to learn the thread file naming and is disclosed in the Self-review.

## 1.A Structural

Columns checked against `references/universe_schema_live.json`; NOT NULL columns marked !; shapes copied from the sibling records named here.

| Table | Columns used (NOT NULL marked) | Location and sample ids | Notes |
|---|---|---|---|
| slack.slack_messages | id!, ts!, channel_id!, text, thread_parent_id, thread_ts_legacy, reply_count, attachments_json, created_at | messages/D0770ET6WBW/2025-09.json (D0770ET6WBW/1759173978.039839), messages/C08R27X0EAH/2025-09.json (C08R27X0EAH/1757939514.864549), messages/C093LEZGF6J/2025-09.json (C093LEZGF6J/1759247580.373799) | id = the first 32 hex of the sha256 of channel, a pipe and ts; replies keep the root's id in thread_parent_id; GitHub-app copies have empty text and one attachment, as base copies do |
| gmail.gmail_threads / gmail_messages | id!, user_email!; id!, thread_id!, user_email! | threads/calvin@harmonygames.co_1842050583560498707.json (an invitation), threads/calvin@harmonygames.co_1844639618018823785.json (GitHub mails for harmonygames-Games/match3d#472), threads/calvin@harmonygames.co_1844705205220700048.json (harmonygames-Games/match3d#475) | thread id = (ms<<20)+bits; one row per mailbox copy; the two GitHub mails join the base PR threads and copy the base approval mails' From, To, Cc and Reply-To |
| gdrive.drive_files / gdocs / gsheets / gslides | id!, name!, mime_type!; document_id; spreadsheet_id; presentation_id | gdrive data.json d_49b9dfa5208d400d9b3937, d_65c76e0b87aa7e9b84d1df, d_cc3e90160f490686039986 (the three owners' roots) | f_ + 22 hex, folders d_; same id across Drive and the native row; identical sharing |
| gcal.gcal_events | event_id!, calendar_id! | gcal data.json evt_f0684c020204a8d22f7dc3 (Calvin's copy of Engineering Focused Weekly Planning) | one row per attendee calendar, attendees sorted by email, self:true on the owner's copy, shared ical_uid |
| linear.linear_issues / linear_comments | id!, title!, priority!, labels_json!, links_json!, relations_json!, state_history_json!, is_archived!, created_at!, updated_at!; id!, issue_id!, author_id!, body!, is_edited!, created_at!, updated_at! | linear data.json ZOM-556, ZOM-560, ZOM-566 (Vincent's and Brian's latest tickets) | state_id holds the state name (Todo, In Validation); keys rise with filing time, ZOM-566 is the last base key (2025-09-30T16:26:02Z); the base has no comments |
| trello.trello_cards / trello_actions / trello_boards (UPDATE) | id!, name!, idBoard!, idList!; id, type, date, idMemberCreator, idBoard, idCard, data_json | trello data.json cards 68c45c2bba569a224e81425d and 6851ab4165575ba2c16a6f05 (Backlog list), actions 68dc0eb3b933d6e0e75dad34, 68c45d98cdb68a952ccaa070 | an id's first 8 hex = its Unix seconds; one updateCard per changed field with the old value under old; idShort 80 is the board's next number (79 is its highest) |
| github.github_reviews / github_review_comments / github_pr_comments / github_timeline_events | id!, pr_id!, seq!; id!, pr_id!, seq!; id!, pr_id!; id!, pr_id!, event! | github data.json harmonygames-Games/match3d#472#rev_1, harmonygames-Games/match3d#465#rc_1, harmonygames-Games/match3d#473#c_1, harmonygames-Games/match3d#473#ev_4 | next ids rev_2, rc_1, c_2, ev_5; line, position and commit_id null as on every base review comment |

## 1.B Entity

| Entity | Spelling used | Where it appears (cited) | Agreement |
|---|---|---|---|
| Calvin Price | calvin.price@harmonygames.co | slack EMPLOYEE_0006_SLACK_ID in D0770ET6WBW/1759173608.518609; GitHub PERSON_0003_GITHUB_USERNAME, author of harmonygames-Games/match3d#465, harmonygames-Games/match3d#472, harmonygames-Games/match3d#475 (shown as calvin.price in C093LEZGF6J/1759185399.395419); Linear usr_49b9dfa5208d400d, assignee of ZOM-543; Drive root d_49b9dfa5208d400d9b3937 | AGREE |
| Brian Foster | brian.foster@harmonygames.co | slack EMPLOYEE_0026_SLACK_ID in D0770ET6WBW/1758808795.588519; Linear usr_fc22d5941b2aeb5c, creator of ZOM-543 and ZOM-566 | AGREE |
| Vincent Parker | vincent.parker@harmonygames.co | slack EMPLOYEE_0012_SLACK_ID in D06UPGF5PQV/1758820544.160399; Linear usr_65c76e0b87aa7e9b, creator of ZOM-556 and ZOM-560; Drive root d_65c76e0b87aa7e9b84d1df | AGREE |
| Arthur Blake | arthur.blake@harmonygames.co | GitHub EMPLOYEE_0025_GITHUB_USERNAME, harmonygames-Games/match3d#472#rev_1 and harmonygames-Games/match3d#475#rev_1 (shown as arthur.blake in C093LEZGF6J/1759247580.373799); slack EMPLOYEE_0025_SLACK_ID in C0880U9751A/1759189361.525409; Drive root d_cc3e90160f490686039986 | AGREE |
| Leonard Hayes | leonard.hayes@harmonygames.co | Trello PERSON_6094_TRELLO_USER_ID, actions 68dc0eb3b933d6e0e75dad34 and 68c451221ebabaf255a7d17f on ZM ROADMAP; slack EMPLOYEE_0038_SLACK_ID in C0880U9751A/1759182908.627389; sender 'leonard hayes' of base invitations | AGREE |
| Oliver Brooks | oliver.brooks@harmonygames.co | GitHub EMPLOYEE_0003_GITHUB_USERNAME, author and merger of harmonygames-Games/match3d#473 (shown as oliver.brooks in C093LEZGF6J/1759246868.802449); slack EMPLOYEE_0003_SLACK_ID in C08R27X0EAH/1759254098.279269; Linear usr_bdf01b53c6a92c5e | AGREE |
| Marcus Bennett | marcus.bennett@harmonygames.co | slack EMPLOYEE_0002_SLACK_ID in D05U73FNDDL/1759156446.484629; the artist, one of three Marcuses in the roster, used only by Slack id | AGREE |
| Robert | robert@harmonygames.co | slack EMPLOYEE_0016_SLACK_ID in C0880U9751A/1759187344.387499 | AGREE |
| Owen Baker, Samuel Turner, Julia Lawson | roster addresses | Linear usr_4e13bd40cc73d0fc (assignee of ZOM-566), usr_caafeec2804b3a67 (assignee of ZOM-560); julia.lawson@harmonygames.co on base invitations (gmail threads/calvin@harmonygames.co_1842050583560498707.json) | AGREE |
| Collect & Win / Win&Collect / collect&win | Collect & Win in the sheet, the card and Brian's note; the PR title says Win&Collect (harmonygames-Games/match3d#472), Brian's chat says collect&win (D0770ET6WBW/1758730948.999939) | harmonygames-Games/match3d#472, D0770ET6WBW/1758730948.999939, Trello card 6851a7abf7876721472dba99 (Win and Collect) | AGREE (one feature, base naming varies) |
| Queue Manager | ZOM-543 'Queue Manager'; Calvin's folder and deck 'ZM queue manager' | ZOM-543, harmonygames-Games/match3d#465, Trello card 68c453cd0ff184d95550bc58 | AGREE |
| Builds | job name and number as in #builds: 'iOS Internal #1718', 'Android #1984', 'Android Submission #135' | C05433XK267/1758817549.151639, C05433XK267/1758838918.332289, C05433XK267/1759263189.219529; Calvin's own form 'Match 3D iOS Internal - #1718' in D06UPGF5PQV/1758817744.353289 | AGREE |
| ZOM vs ENG keys | only ZOM keys are seeded | ENG-2069 (a Domino Delights queue ticket) is a decoy only | AGREE |

No roster person is renamed or re-titled. Thomas, Thomas Baker and Oscar Bennett do not appear; Frederick Stone's GitHub login is not used.

## 1.C Voice and realism

Seeded speakers, each with its activity.json (synth-cut KB) status at the clock:
- Brian Foster (brian.foster@harmonygames.co) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: the DM, the earlier line about the review, the note on ZOM-543, one ticket comment.
- Vincent Parker (vincent.parker@harmonygames.co) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: the pass sheet and legend, 18 tickets and their first notes, the two ties, two DM lines, the thread reply.
- Arthur Blake (arthur.blake@harmonygames.co) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: two inline review comments, the two build notes.
- Leonard Hayes (leonard.hayes@harmonygames.co) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: the review card and its actions, the calendar event and its mails.
- Oliver Brooks (oliver.brooks@harmonygames.co) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: the line on his own PR, two ticket replies.
- Marcus Bennett (marcus.bennett@harmonygames.co) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: two DM lines.
- Robert (robert@harmonygames.co) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: one channel post.
- Owen Baker (owen.baker@harmonygames.co) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: two ticket replies.
- Samuel Turner (samuel.turner@harmonygames.co) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: one ticket reply.
- Calvin Price (calvin.price@harmonygames.co) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: owner of the seeded folder and deck; no seeded message.
- SLACK_BOT_0004_SLACK_ID — the GitHub Slack app (integrations.json INT-01), not a person; seeds: three comment copies in #zombie-prs.
- SVC_0248_EMAIL — GitHub's notification sender (integrations.json INT-12), not a person; seeds: two mails in the base PR threads.

Lengths and hours from conventions.json (synth-cut KB): slack.length_chars_by_channel_type and slack.per_person_hours_and_style. Core UTC windows: Brian 12–21, Vincent 10–19, Marcus 10–20, Robert 14–03, Arthur 15–01, Leonard 15–02, Oliver 14–01, Owen 15–00, Samuel 15–00. Every seeded record sits inside its author's window except Vincent's sheet save at 19:30Z, his line to Calvin at 19:33Z and his thread reply at 21:20Z; the base has him posting at 21:36Z on Sep 24 (the report behind sheet rows 1 and 2). linear.title_prefixes_by_team: ZOM titles carry no prefix, and Vincent's base titles are plain sentences (ZOM-556, ZOM-560). github.pr_title_patterns is not used: no PR is seeded. gcal.duration_min: 30 minutes, the base's most common length. gmail.internal_subject_len_chars is not used: the only seeded mails are system mails whose subjects follow integrations.json INT-11 and INT-12.

Real messages used as voice references:
- Brian Foster: "We talked with [PERSON_NAME_0050], the input blocker is not a problem right now. Probably we need to check that after adding collect&amp;win to queuemanager" (D0770ET6WBW/1758808795.588519) · "When  users kills the app, they see coin animation again" (D0770ET6WBW/1758808900.412489) · "Hello! I don't have any time to test today. But I'll test it tomorrow" (D0770ET6WBW/1759173857.856219)
- Vincent Parker: "Looks ok to me" (D06UPGF5PQV/1758820544.160399) · "Boss arena as well" (D06UPGF5PQV/1758820551.265839) · "i think we should squeeze in the fix for that issue if it's an easy fix. annoying and players can see that for 10 times in a day if they make it that far." (C08R27X0EAH/1757939514.864549)
- Marcus Bennett: "ok so i pushed a modifications on the prefab on my branch, Marcus/EndlessMode_Vfx" (D05U73FNDDL/1759156446.484629) · "cuz i'm done with the bar itself" (D05U73FNDDL/1759161289.715329) · "hopefully we are not gona have any conflicts right?" (D05U73FNDDL/1759161340.563009)
- Robert: "Android" (C0880U9751A/1759248076.284779) · "I didn't look at it by pubs." (C0880U9751A/1759248130.580729)
- Arthur Blake: "we haven't merged it yet. I'll let you know" (C0880U9751A/1759189361.525409) · "Seems important" (harmonygames-Games/match3d#390#rc_6) · "This is intentional as I want it to simulate more when timescale is high." (harmonygames-Games/match3d#395#rc_4)
- Oliver Brooks: "will work on this asap" (C08R27X0EAH/1759254098.279269) · "well, we'll see what happens after we move 2 or 3 features to Addressables" (C08R27X0EAH/1758919518.529979) · "I can have a look and let you know" (C0880U9751A/1758235859.966389)
- Leonard Hayes: "I just released 0.3.49 on IOS" (C0880U9751A/1759182908.627389)
- Samuel Turner: "I added it to main. Please update your branch, and if it's not showing, restart Unity" (C0880U9751A/1756928762.675329)
- Owen Baker: "I created a doc for the endpoints I'm going to need for CollectAndWin event, please give it a look when you have a chance:" (C0880U9751A/1756161484.791409)

Brian opens with a separate 'Hello!' line and writes plain full sentences; Marcus writes lower-case bursts; Vincent writes short status lines; Arthur's review comments are one or two short sentences. Vincent files tickets in bursts in the base (six between 14:44Z and 15:21Z on Sep 22, ZOM-556 to ZOM-561), so 18 tickets in two hours on Sep 30 follow his habit. No em dashes are used.

## 1.D Keyword

| Term | Hits / pointer | Note |
|---|---|---|
| "Queue Manager" | ZOM-543; harmonygames-Games/match3d#465; Trello card 68c453cd0ff184d95550bc58 | the ticket the note sits on; ENG-2069 is the Domino Delights namesake (decoy) |
| "flow review" | NEW TERM — introduced in 345e6d1a65b0b15ec2914567ad11d583, 68daad83bacf52c6ea7e1593, calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com>, evt_342a813cb7765d4a6fce8d | reached from Brian's DM ('Thursday's flow review', 'the review invite') and his note ('the agenda of Thursday's review') |
| "flow pass" | NEW TERM — introduced in f_cb40955893624e1acb8500 | reached from Brian's DM; a Drive or Sheets search on the words returns the sheet |
| "QA passes" | NEW TERM — introduced in f_6d0326fa006b136f1bbf82 and f_ea7517885d11570b54bf13 | reached from Brian's note; a Docs search returns both, the decoy differs on the game |
| "1718" | C05433XK267/1758817549.151639, D06UPGF5PQV/1758817744.353289 | the build Calvin names in the chat; its #builds post gives the branch |
| "Submission 135" / "#135" | C05433XK267/1759263189.219529; seeded b156fdcd5fd89b8362d0e5fcf24975d1 and a40824773b7cad9681d141b916a5f558 | the newer main build both later reports name |
| "pass icon" | D06UPGF5PQV/1758721951.996909 (Vincent, Sep 24, about the icon's VFX: decoy); seeded 806f4a67a847d4d47e3e5674760aa630, ZOM-571, harmonygames-Games/match3d#472#rc_1 | three different things share the words; the sheet row is the restart, Marcus's report is the glow |
| "daily gift" | ZOM-556, ZOM-432 | ZOM-432 is the artwork frame (decoy); Vincent's tie is on ZOM-556 |
| "freezer" | ZOM-560 | the abandoned pack ticket; Vincent's tie is on it |
| "Addressables" | harmonygames-Games/match3d#473; C08R27X0EAH/1758919518.529979 | Oliver's merged PR; his seeded line is its second conversation comment |
| "stock-take" | NEW TERM — introduced in 446ba45665ed73d2f06caca6963c6ffc | Brian's word for the deliverable |

## 1.E Persona reach

Load-bearing scoped ids written to `Working_Files/plan/load_bearing_scoped.txt`; output verbatim. Linear, Trello and GitHub are unscoped, so their ids are not in that list (Evals/references/persona/acl.md).

```
CHECK-SQL as calvin_price <calvin.price@harmonygames.co>
[YES LB] L6 gdrive.drive_files insert f_cb40955893624e1acb8500 - file is shared with the persona (shared_with_emails)
[YES LB] L9 gdrive.drive_files insert f_d3a1aa5976285aac98ffda - file is shared with the persona (shared_with_emails)
[YES LB] L11 gdrive.drive_files insert f_6d0326fa006b136f1bbf82 - file is shared with the persona (shared_with_emails)
[YES LB] L13 gdrive.drive_files insert f_ea7517885d11570b54bf13 - file is shared with the persona (shared_with_emails)
[YES LB] L15 gdrive.drive_files insert d_36cdb0374c4aad3b8bf741 - persona owns the file
[YES LB] L17 gdrive.drive_files insert f_637e63ae6c1b4a7eb016aa - persona owns the file
[YES LB] L19 gdocs.docs_documents insert f_d3a1aa5976285aac98ffda - file is shared with the persona (shared_with_emails)
[YES LB] L22 gdocs.docs_documents insert f_6d0326fa006b136f1bbf82 - file is shared with the persona (shared_with_emails)
[YES LB] L24 gdocs.docs_documents insert f_ea7517885d11570b54bf13 - file is shared with the persona (shared_with_emails)
[YES LB] L26 gsheets.sheets_spreadsheets insert f_cb40955893624e1acb8500 - file is shared with the persona (shared_with_emails)
[YES LB] L29 gsheets.sheets_sheets insert f_cb40955893624e1acb8500, f_cb40955893624e1acb8500#0 - file is shared with the persona (shared_with_emails)
[YES LB] L31 gslides.slides_presentations insert f_637e63ae6c1b4a7eb016aa - persona owns the file
[YES LB] L34 gslides.slides_pages insert f_637e63ae6c1b4a7eb016aa, slide_0cf752b9ec2f - persona owns the file
[YES LB] L36 gslides.slides_page_elements insert f_637e63ae6c1b4a7eb016aa, el_a59d866f862d, slide_0cf752b9ec2f - persona owns the file
[YES LB] L38 gslides.slides_page_elements insert f_637e63ae6c1b4a7eb016aa, el_79f2674deaf2, slide_0cf752b9ec2f - persona owns the file
[YES LB] L40 gslides.slides_pages insert f_637e63ae6c1b4a7eb016aa, slide_47694f562fb2 - persona owns the file
[YES LB] L42 gslides.slides_page_elements insert f_637e63ae6c1b4a7eb016aa, el_9c8354459689, slide_47694f562fb2 - persona owns the file
[YES LB] L44 gslides.slides_page_elements insert f_637e63ae6c1b4a7eb016aa, el_c8dcb6ec1c74, slide_47694f562fb2 - persona owns the file
[YES LB] L46 gslides.slides_pages insert f_637e63ae6c1b4a7eb016aa, slide_1eecf7b303fd - persona owns the file
[YES LB] L48 gslides.slides_page_elements insert f_637e63ae6c1b4a7eb016aa, el_0e6881c40b0e, slide_1eecf7b303fd - persona owns the file
[YES LB] L50 gslides.slides_page_elements insert f_637e63ae6c1b4a7eb016aa, el_d02d78e7f5dc, slide_1eecf7b303fd - persona owns the file
[YES LB] L52 gslides.slides_pages insert f_637e63ae6c1b4a7eb016aa, slide_5ef06204f9c1 - persona owns the file
[YES LB] L54 gslides.slides_page_elements insert f_637e63ae6c1b4a7eb016aa, el_fa451ae62a67, slide_5ef06204f9c1 - persona owns the file
[YES LB] L56 gslides.slides_page_elements insert f_637e63ae6c1b4a7eb016aa, el_5d0ae0441e73, slide_5ef06204f9c1 - persona owns the file
[YES LB] L58 slack.slack_messages insert 345e6d1a65b0b15ec2914567ad11d583, D0770ET6WBW/1759164072.337219 - persona EMPLOYEE_0006_SLACK_ID is in members of im D0770ET6WBW
[YES] L61 slack.slack_messages insert bafc679369bbc96d67013c80ab1dfca6, D0770ET6WBW/1759264784.871309 - persona EMPLOYEE_0006_SLACK_ID is in members of im D0770ET6WBW
[YES LB] L63 slack.slack_messages insert 446ba45665ed73d2f06caca6963c6ffc, D0770ET6WBW/1759264805.214409 - persona EMPLOYEE_0006_SLACK_ID is in members of im D0770ET6WBW
[YES] L65 slack.slack_messages insert ffb75fdf46c3d39f1db0e6f21ccacab3, D06UPGF5PQV/1758883277.402889 - persona EMPLOYEE_0006_SLACK_ID is in members of im D06UPGF5PQV
[YES] L67 slack.slack_messages insert cfee08a826c7257605f848684ff2324a, D06UPGF5PQV/1759260806.118549 - persona EMPLOYEE_0006_SLACK_ID is in members of im D06UPGF5PQV
[YES LB] L69 slack.slack_messages insert 806f4a67a847d4d47e3e5674760aa630, D05U73FNDDL/1759252212.611349 - persona EMPLOYEE_0006_SLACK_ID is in members of im D05U73FNDDL
[YES] L71 slack.slack_messages insert bb5dd8751a108f2f60ae5643ff7507f0, D05U73FNDDL/1759252231.208739 - persona EMPLOYEE_0006_SLACK_ID is in members of im D05U73FNDDL
[YES LB] L73 slack.slack_messages insert b156fdcd5fd89b8362d0e5fcf24975d1, C08R27X0EAH/1759267212.418339 - persona EMPLOYEE_0006_SLACK_ID is in members of private zombie-bugs
[YES] L75 slack.slack_messages update 90084203fa44a059e22d0d1c59ae85c4, C08R27X0EAH/1757939514.864549 - persona EMPLOYEE_0006_SLACK_ID is in members of private zombie-bugs
[YES LB] L76 slack.slack_messages insert a40824773b7cad9681d141b916a5f558, C08R27X0EAH/1759268652.552719 - persona EMPLOYEE_0006_SLACK_ID is in members of private zombie-bugs
[YES] L78 slack.slack_messages update 51696f3621eb437b78c6fa36088720cd, C08R27X0EAH/1757467270.178829 - persona EMPLOYEE_0006_SLACK_ID is in members of private zombie-bugs
[YES] L79 slack.slack_messages insert ecf80487a68281b5eb011679ad0e5004, C0880U9751A/1759185627.317849 - persona EMPLOYEE_0006_SLACK_ID is in members of private zombie-match3d
[YES LB] L81 slack.slack_messages insert 66dd5332dde5b7312c0ae201c285a323, C093LEZGF6J/1759246932.447309 - persona EMPLOYEE_0006_SLACK_ID is in members of public zombie-prs
[YES] L83 slack.slack_messages update d05a2f8a3c4ada2d6b91c809e04222dc, C093LEZGF6J/1759246868.802449 - persona EMPLOYEE_0006_SLACK_ID is in members of public zombie-prs
[YES LB] L84 slack.slack_messages insert 8e02c1142dfdd380c577a14bc366ee1d, C093LEZGF6J/1759247622.208419 - persona EMPLOYEE_0006_SLACK_ID is in members of public zombie-prs
[YES] L86 slack.slack_messages update 61f686b8a8b6c164b14aff6b5b1897bf, C093LEZGF6J/1759185399.395419 - persona EMPLOYEE_0006_SLACK_ID is in members of public zombie-prs
[YES LB] L87 slack.slack_messages insert 69700214ac2e727feec1d08d2b873218, C093LEZGF6J/1759248592.611579 - persona EMPLOYEE_0006_SLACK_ID is in members of public zombie-prs
[YES] L89 slack.slack_messages update 1389e3c51eeac40d0019f335f34550e4, C093LEZGF6J/1759247948.371729 - persona EMPLOYEE_0006_SLACK_ID is in members of public zombie-prs
[YES] L102 gcal.gcal_events insert evt_0e5a1e82445aa0f1f7e4b9 - persona is an attendee and holds its own copy evt_342a813cb7765d4a6fce8d (same ical_uid and start) on calvin.price@harmonygames.co
[YES] L105 gcal.gcal_events insert evt_179a33943df19c4e1f2052 - persona is an attendee and holds its own copy evt_342a813cb7765d4a6fce8d (same ical_uid and start) on calvin.price@harmonygames.co
[YES] L107 gcal.gcal_events insert evt_c3ec08f90f9c924e8c0674 - persona is an attendee and holds its own copy evt_342a813cb7765d4a6fce8d (same ical_uid and start) on calvin.price@harmonygames.co
[YES] L109 gcal.gcal_events insert evt_8dc57df95b8a3423520abd - persona is an attendee and holds its own copy evt_342a813cb7765d4a6fce8d (same ical_uid and start) on calvin.price@harmonygames.co
[YES] L111 gcal.gcal_events insert evt_89cc304cc82c81fc30abcb - persona is an attendee and holds its own copy evt_342a813cb7765d4a6fce8d (same ical_uid and start) on calvin.price@harmonygames.co
[YES LB] L113 gcal.gcal_events insert evt_342a813cb7765d4a6fce8d - event is on the persona's own calendar calvin.price@harmonygames.co
[YES] L115 gmail.gmail_threads insert calvin.price@harmonygames.co/1844614963135476249 - row user_email is the persona (calvin.price@harmonygames.co)
[YES LB] L118 gmail.gmail_messages insert calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com>, c - row user_email is the persona (calvin.price@harmonygames.co)
[YES] L120 gmail.gmail_threads insert calvin.price@harmonygames.co/1844710525108434561 - row user_email is the persona (calvin.price@harmonygames.co)
[YES LB] L122 gmail.gmail_messages insert calvin.price@harmonygames.co/<calendar-f2b39cd5-884e-2def-a4d7-d41d80d4c55b@google.com>, c - row user_email is the persona (calvin.price@harmonygames.co)
[NO] L124 gmail.gmail_threads insert vincent.parker@harmonygames.co/1844614963134675497 - row is in mailbox vincent.parker@harmonygames.co, not the persona's (calvin.price@harmonygames.co)
[NO] L126 gmail.gmail_messages insert vincent.parker@harmonygames.co/<calendar-bb830870-1845-b709-820d-db5ca3233174@google.com>, - row is in mailbox vincent.parker@harmonygames.co, not the persona's (calvin.price@harmonygames.co)
[NO] L128 gmail.gmail_threads insert vincent.parker@harmonygames.co/1844710525108550630 - row is in mailbox vincent.parker@harmonygames.co, not the persona's (calvin.price@harmonygames.co)
[NO] L130 gmail.gmail_messages insert vincent.parker@harmonygames.co/<calendar-5c092c9e-9cc6-a8d4-f609-c777def9599d@google.com>, - row is in mailbox vincent.parker@harmonygames.co, not the persona's (calvin.price@harmonygames.co)
[NO] L132 gmail.gmail_threads insert brian.foster@harmonygames.co/1844614963135138801 - row is in mailbox brian.foster@harmonygames.co, not the persona's (calvin.price@harmonygames.co)
[NO] L134 gmail.gmail_messages insert brian.foster@harmonygames.co/<calendar-6c9eab69-d1e0-cf85-0006-87c8c5c5d486@google.com>, b - row is in mailbox brian.foster@harmonygames.co, not the persona's (calvin.price@harmonygames.co)
[NO] L136 gmail.gmail_threads insert brian.foster@harmonygames.co/1844710525109022287 - row is in mailbox brian.foster@harmonygames.co, not the persona's (calvin.price@harmonygames.co)
[NO] L138 gmail.gmail_messages insert brian.foster@harmonygames.co/<calendar-02a3fe02-166c-a0c1-6359-2ecb046471be@google.com>, b - row is in mailbox brian.foster@harmonygames.co, not the persona's (calvin.price@harmonygames.co)
[NO] L140 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844614963134787882 - row is in mailbox julia.lawson@harmonygames.co, not the persona's (calvin.price@harmonygames.co)
[NO] L142 gmail.gmail_messages insert julia.lawson@harmonygames.co/<calendar-fc4cf5c7-ebb2-24d9-33a3-88a114504137@google.com>, j - row is in mailbox julia.lawson@harmonygames.co, not the persona's (calvin.price@harmonygames.co)
[NO] L144 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844710525108618407 - row is in mailbox julia.lawson@harmonygames.co, not the persona's (calvin.price@harmonygames.co)
[NO] L146 gmail.gmail_messages insert julia.lawson@harmonygames.co/<calendar-1f8e4494-259c-8839-1a9c-f9d88a15a894@google.com>, j - row is in mailbox julia.lawson@harmonygames.co, not the persona's (calvin.price@harmonygames.co)
[NO] L148 gmail.gmail_threads insert arthur.blake@harmonygames.co/1844614963134486883 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (calvin.price@harmonygames.co)
[NO] L150 gmail.gmail_messages insert arthur.blake@harmonygames.co/<calendar-f5906aec-0d16-89b0-9b38-62ac2462ad84@google.com>, a - row is in mailbox arthur.blake@harmonygames.co, not the persona's (calvin.price@harmonygames.co)
[NO] L152 gmail.gmail_threads insert arthur.blake@harmonygames.co/1844710525108836806 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (calvin.price@harmonygames.co)
[NO] L154 gmail.gmail_messages insert arthur.blake@harmonygames.co/<calendar-fcb975d6-36c7-90b6-6490-0661d848001a@google.com>, a - row is in mailbox arthur.blake@harmonygames.co, not the persona's (calvin.price@harmonygames.co)
[YES LB] L156 gmail.gmail_messages insert calvin.price@harmonygames.co/<[SOURCE_ORG_0001]-Games/match3d/pull/472/review/3285698310@g - row user_email is the persona (calvin.price@harmonygames.co)
[YES LB] L158 gmail.gmail_messages insert calvin.price@harmonygames.co/<[SOURCE_ORG_0001]-Games/match3d/pull/475/review/3285755391@g - row user_email is the persona (calvin.price@harmonygames.co)

summary: {'YES': 54, 'NO': 16}  unscoped rows (always visible): 70
  gcal.gcal_events: {'YES': 6}
  gdocs.docs_documents: {'YES': 3}
  gdrive.drive_files: {'YES': 6}
  gmail.gmail_messages: {'YES': 4, 'NO': 8}
  gmail.gmail_threads: {'YES': 2, 'NO': 8}
  gsheets.sheets_sheets: {'YES': 1}
  gsheets.sheets_spreadsheets: {'YES': 1}
  gslides.slides_page_elements: {'YES': 8}
  gslides.slides_pages: {'YES': 4}
  gslides.slides_presentations: {'YES': 1}
  slack.slack_messages: {'YES': 18}
verdict: PASS (0 load-bearing rows not visible)
```

- D0770ET6WBW — Calvin's DM with Brian (im member) LB; seeded 446ba45665ed73d2f06caca6963c6ffc (D0770ET6WBW/1759264805.214409) and 345e6d1a65b0b15ec2914567ad11d583 (D0770ET6WBW/1759164072.337219).
- D05U73FNDDL — Calvin's DM with Marcus LB; seeded 806f4a67a847d4d47e3e5674760aa630 (D05U73FNDDL/1759252212.611349).
- D06UPGF5PQV — Calvin's DM with Vincent LB; base D06UPGF5PQV/1758817744.353289 and D06UPGF5PQV/1758820544.160399.
- C08R27X0EAH — #zombie-bugs, Calvin a member LB; seeded reply b156fdcd5fd89b8362d0e5fcf24975d1 under C08R27X0EAH/1757939514.864549.
- C0880U9751A — #zombie-match3d, Calvin a member LB; seeded ecf80487a68281b5eb011679ad0e5004, Robert's sighting on the older build Android #2006. The reply a40824773b7cad9681d141b916a5f558 sits under C08R27X0EAH/1757467270.178829 in #zombie-bugs.
- C05433XK267 — #builds, Calvin a member LB; base posts C05433XK267/1758817549.151639 and C05433XK267/1759263189.219529.
- Calvin's mailbox LB: calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com>, calvin.price@harmonygames.co/<calendar-f2b39cd5-884e-2def-a4d7-d41d80d4c55b@google.com>.
- Drive LB: f_cb40955893624e1acb8500, f_d3a1aa5976285aac98ffda, f_6d0326fa006b136f1bbf82 and f_ea7517885d11570b54bf13 are shared with Calvin; d_36cdb0374c4aad3b8bf741 and f_637e63ae6c1b4a7eb016aa are his own.
- Calendar LB: evt_342a813cb7765d4a6fce8d is Calvin's own copy (self:true).
- Unscoped: ZOM-543 with Brian's note, ZOM-556, ZOM-560, ZOM-567 to ZOM-584, harmonygames-Games/match3d#465, harmonygames-Games/match3d#472, harmonygames-Games/match3d#473, harmonygames-Games/match3d#475, harmonygames-Games/match3d#472#rc_1, harmonygames-Games/match3d#475#rc_1, harmonygames-Games/match3d#473#c_2, Trello card 68daad83bacf52c6ea7e1593.
- No designed denial for evt_342a813cb7765d4a6fce8d: denied_probes is empty. The invitation copies in four other mailboxes and the five other calendar copies are companions, never evidence; the event and both mails are cited by Calvin's own copies.

## 1.F Collision

base_check Check A compares every minted id against the full base collections (output in the Self-review, PASS). Scheme by service:
- linear: ZOM-567 to ZOM-584: base ZOM ends at ZOM-566 (2025-09-30T16:26:02Z); 27 comment ids are comment_ + 32 hex and the base has 0 comments.
- slack: 13 seeded (channel, ts) pairs: no base message in those channels at those ts (messages/D0770ET6WBW/2025-09.json, messages/D06UPGF5PQV/2025-09.json, messages/D05U73FNDDL/2025-09.json, messages/C08R27X0EAH/2025-09.json, messages/C0880U9751A/2025-09.json, messages/C093LEZGF6J/2025-09.json).
- gmail: thread ids and calendar Message-IDs minted per seeded time and mailbox; the two GitHub review numbers 3285698310 and 3285755391 sit just under the base approvals' 3285702920 and 3285759222 in the same threads.
- trello: card 68daad83bacf52c6ea7e1593 and actions 68daad83bacf52c6ea7ee56b, 68daadb6fbc085cc55324705, 68dc11bd3f45a368c395dca8, 68dc11dceb76ad640995fd98: first 8 hex are each record's own seconds; idShort 80 is unused on board 6851a6569f3bf818760632ab.
- drive/calendar: f_cb40955893624e1acb8500, f_d3a1aa5976285aac98ffda, f_6d0326fa006b136f1bbf82, f_ea7517885d11570b54bf13, f_637e63ae6c1b4a7eb016aa, d_36cdb0374c4aad3b8bf741, evt_342a813cb7765d4a6fce8d: sha-derived, 0 base hits (lookup run at the scenario stage, `plan/out/id_collisions.txt`, and Check A here).
- github: harmonygames-Games/match3d#472#rc_1, harmonygames-Games/match3d#475#rc_1, harmonygames-Games/match3d#472#rev_2, harmonygames-Games/match3d#475#rev_2, harmonygames-Games/match3d#473#c_2, harmonygames-Games/match3d#473#ev_5: base ids end at rev_1, no rc, c_1 and ev_4 on those PRs.
- Header tokens: none minted; PERSON_6094_TRELLO_USER_ID, PERSON_6092_TRELLO_USERNAME, SLACK_BOT_0004_SLACK_ID, SVC_0248, SVC_3649, SVC_0613, SVC_5111 (with the alias each base approval mail carries) and SVC_0842 are the base tokens those records use. Body tokens: [PERSON_NAME_0043] is Julia's own token as base invitations in her mailbox end; [PERSON_NAME_0029] and [SOURCE_ORG_0001] are copied inside base PR titles and mail subjects.

## Record ledger

One row per SQL statement, in SQL order.

| # | SQL line | Table | Id | Manifest element | Carrier | Reach | Discovery role |
|---|---|---|---|---|---|---|---|
| 1 | L6 | gdrive.drive_files | f_cb40955893624e1acb8500 | K2, T_BACK, T_BACK_TICKET, T_BRANCH, T_REOPEN, T_REOPEN_TICKET | ● | shared with Calvin | claim met first |
| 2 | L9 | gdrive.drive_files | f_d3a1aa5976285aac98ffda | K6 | ● | shared with Calvin | connecting |
| 3 | L11 | gdrive.drive_files | f_6d0326fa006b136f1bbf82 | H1, K3, T_BRANCH | ● | shared with Calvin | authority |
| 4 | L13 | gdrive.drive_files | f_ea7517885d11570b54bf13 | D_DDRULE, H1 decoy | ● | shared with Calvin | decoy |
| 5 | L15 | gdrive.drive_files | d_36cdb0374c4aad3b8bf741 | K5 | ● | owner | connecting |
| 6 | L17 | gdrive.drive_files | f_637e63ae6c1b4a7eb016aa | K19 | ● | owner | connecting |
| 7 | L19 | gdocs.docs_documents | f_d3a1aa5976285aac98ffda | K6 | ● | shared with Calvin | connecting |
| 8 | L22 | gdocs.docs_documents | f_6d0326fa006b136f1bbf82 | H1, K3, T_BRANCH | ● | shared with Calvin | authority |
| 9 | L24 | gdocs.docs_documents | f_ea7517885d11570b54bf13 | D_DDRULE, H1 decoy | ● | shared with Calvin | decoy |
| 10 | L26 | gsheets.sheets_spreadsheets | f_cb40955893624e1acb8500 | K2, T_BACK, T_BACK_TICKET, T_BRANCH, T_REOPEN, T_REOPEN_TICKET | ● | shared with Calvin | claim met first |
| 11 | L29 | gsheets.sheets_sheets | f_cb40955893624e1acb8500#Flow pass | K2, T_BACK, T_BACK_TICKET, T_BRANCH, T_REOPEN, T_REOPEN_TICKET | ● | shared with Calvin | connecting |
| 12 | L31 | gslides.slides_presentations | f_637e63ae6c1b4a7eb016aa | K19 | ● | owner | connecting |
| 13 | L34 | gslides.slides_pages | f_637e63ae6c1b4a7eb016aa#slide_0cf752b9ec2f | K19 | ● | shared with Calvin | connecting |
| 14 | L36 | gslides.slides_page_elements | f_637e63ae6c1b4a7eb016aa#el_a59d866f862d | K19 | ● | shared with Calvin | connecting |
| 15 | L38 | gslides.slides_page_elements | f_637e63ae6c1b4a7eb016aa#el_79f2674deaf2 | K19 | ● | shared with Calvin | connecting |
| 16 | L40 | gslides.slides_pages | f_637e63ae6c1b4a7eb016aa#slide_47694f562fb2 | K19 | ● | shared with Calvin | connecting |
| 17 | L42 | gslides.slides_page_elements | f_637e63ae6c1b4a7eb016aa#el_9c8354459689 | K19 | ● | shared with Calvin | connecting |
| 18 | L44 | gslides.slides_page_elements | f_637e63ae6c1b4a7eb016aa#el_c8dcb6ec1c74 | K19 | ● | shared with Calvin | connecting |
| 19 | L46 | gslides.slides_pages | f_637e63ae6c1b4a7eb016aa#slide_1eecf7b303fd | K19 | ● | shared with Calvin | connecting |
| 20 | L48 | gslides.slides_page_elements | f_637e63ae6c1b4a7eb016aa#el_0e6881c40b0e | K19 | ● | shared with Calvin | connecting |
| 21 | L50 | gslides.slides_page_elements | f_637e63ae6c1b4a7eb016aa#el_d02d78e7f5dc | K19 | ● | shared with Calvin | connecting |
| 22 | L52 | gslides.slides_pages | f_637e63ae6c1b4a7eb016aa#slide_5ef06204f9c1 | K19 | ● | shared with Calvin | connecting |
| 23 | L54 | gslides.slides_page_elements | f_637e63ae6c1b4a7eb016aa#el_fa451ae62a67 | K19 | ● | shared with Calvin | connecting |
| 24 | L56 | gslides.slides_page_elements | f_637e63ae6c1b4a7eb016aa#el_5d0ae0441e73 | K19 | ● | shared with Calvin | connecting |
| 25 | L58 | slack.slack_messages | 345e6d1a65b0b15ec2914567ad11d583 | H2 decoy, T_GATE | ● | channel or DM member | claim met first |
| 26 | L61 | slack.slack_messages | bafc679369bbc96d67013c80ab1dfca6 | AN1 companion (greeting) | ● | channel or DM member | connecting |
| 27 | L63 | slack.slack_messages | 446ba45665ed73d2f06caca6963c6ffc | AN1 | ● | channel or DM member | first link |
| 28 | L65 | slack.slack_messages | ffb75fdf46c3d39f1db0e6f21ccacab3 | R1 context (the pass starts on the 26th) | ● | channel or DM member | connecting |
| 29 | L67 | slack.slack_messages | cfee08a826c7257605f848684ff2324a | R4 context (tickets filed from the sheet) | ● | channel or DM member | connecting |
| 30 | L69 | slack.slack_messages | 806f4a67a847d4d47e3e5674760aa630 | K8, T_FILT | ● | channel or DM member | connecting (report outside the sheet) |
| 31 | L71 | slack.slack_messages | bb5dd8751a108f2f60ae5643ff7507f0 | T_FILT companion (second line) | ● | channel or DM member | connecting |
| 32 | L73 | slack.slack_messages | b156fdcd5fd89b8362d0e5fcf24975d1 | K13, T_REOPEN | ● | channel or DM member | overturning |
| 33 | L75 | slack.slack_messages (UPDATE) | 90084203fa44a059e22d0d1c59ae85c4 | companion (counters or updated_at of a base parent) | ● | channel or DM member | connecting |
| 34 | L76 | slack.slack_messages | a40824773b7cad9681d141b916a5f558 | K18, T_BACK | ● | channel or DM member | overturning |
| 35 | L78 | slack.slack_messages (UPDATE) | 51696f3621eb437b78c6fa36088720cd | companion (counters or updated_at of a base parent) | ● | channel or DM member | connecting |
| 36 | L79 | slack.slack_messages | ecf80487a68281b5eb011679ad0e5004 | D_OLDBUILD | ● | channel or DM member | connecting |
| 37 | L81 | slack.slack_messages | 66dd5332dde5b7312c0ae201c285a323 | T_ELSE companion (INT-01) | ● | channel or DM member | connecting |
| 38 | L83 | slack.slack_messages (UPDATE) | d05a2f8a3c4ada2d6b91c809e04222dc | companion (counters or updated_at of a base parent) | ● | channel or DM member | connecting |
| 39 | L84 | slack.slack_messages | 8e02c1142dfdd380c577a14bc366ee1d | T_INLINE companion (INT-01) | ● | channel or DM member | connecting |
| 40 | L86 | slack.slack_messages (UPDATE) | 61f686b8a8b6c164b14aff6b5b1897bf | companion (counters or updated_at of a base parent) | ● | channel or DM member | connecting |
| 41 | L87 | slack.slack_messages | 69700214ac2e727feec1d08d2b873218 | T_INLINE_PACK companion (INT-01) | ● | channel or DM member | connecting |
| 42 | L89 | slack.slack_messages (UPDATE) | 1389e3c51eeac40d0019f335f34550e4 | companion (counters or updated_at of a base parent) | ● | channel or DM member | connecting |
| 43 | L90 | trello.trello_cards | 68daad83bacf52c6ea7e1593 | H2, K4, T_GATE | ● | unscoped | authority |
| 44 | L93 | trello.trello_actions | 68daad83bacf52c6ea7ee56b | H2, T_GATE | ● | unscoped | connecting |
| 45 | L95 | trello.trello_actions | 68daadb6fbc085cc55324705 | T_GATE (first description) | ● | unscoped | connecting |
| 46 | L97 | trello.trello_actions | 68dc11bd3f45a368c395dca8 | T_GATE (rename to Thursday) | ● | unscoped | connecting |
| 47 | L99 | trello.trello_actions | 68dc11dceb76ad640995fd98 | H2, K4, T_GATE | ● | unscoped | overturning |
| 48 | L101 | trello.trello_boards (UPDATE) | 6851a6569f3bf818760632ab | companion (counters or updated_at of a base parent) | ● | unscoped | connecting |
| 49 | L102 | gcal.gcal_events | evt_0e5a1e82445aa0f1f7e4b9 | K7, T_SHARE (attendee copy) | ● (summary, attendees, time; description ○) | attendee copy (companion) | connecting |
| 50 | L105 | gcal.gcal_events | evt_179a33943df19c4e1f2052 | K7, T_SHARE (attendee copy) | ● (summary, attendees, time; description ○) | attendee copy (companion) | connecting |
| 51 | L107 | gcal.gcal_events | evt_c3ec08f90f9c924e8c0674 | K7, T_SHARE (attendee copy) | ● (summary, attendees, time; description ○) | attendee copy (companion) | connecting |
| 52 | L109 | gcal.gcal_events | evt_8dc57df95b8a3423520abd | K7, T_SHARE (attendee copy) | ● (summary, attendees, time; description ○) | attendee copy (companion) | connecting |
| 53 | L111 | gcal.gcal_events | evt_89cc304cc82c81fc30abcb | K7, T_SHARE (attendee copy) | ● (summary, attendees, time; description ○) | attendee copy (companion) | connecting |
| 54 | L113 | gcal.gcal_events | evt_342a813cb7765d4a6fce8d | K7, T_SHARE | ● (summary, attendees, time; description ○) | own calendar | connecting |
| 55 | L115 | gmail.gmail_threads | calvin.price@harmonygames.co/1844614963135476249 | K20, T_GATE, D_OLDINVITE | ● | own mailbox | connecting |
| 56 | L118 | gmail.gmail_messages | calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com> | D_OLDINVITE, H2 decoy, T_GATE | ● | own mailbox | claim met first |
| 57 | L120 | gmail.gmail_threads | calvin.price@harmonygames.co/1844710525108434561 | K20, T_GATE, D_OLDINVITE | ● | own mailbox | connecting |
| 58 | L122 | gmail.gmail_messages | calvin.price@harmonygames.co/<calendar-f2b39cd5-884e-2def-a4d7-d41d80d4c55b@google.com> | K20, T_GATE, T_SHARE | ● | own mailbox | connecting |
| 59 | L124 | gmail.gmail_threads | vincent.parker@harmonygames.co/1844614963134675497 | K20 companion (INT-11 copy in another attendee's mailbox) | ● | not Calvin's (companion copy) | connecting |
| 60 | L126 | gmail.gmail_messages | vincent.parker@harmonygames.co/<calendar-bb830870-1845-b709-820d-db5ca3233174@google.com> | K20 companion (INT-11 copy in another attendee's mailbox) | ● | not Calvin's (companion copy) | connecting |
| 61 | L128 | gmail.gmail_threads | vincent.parker@harmonygames.co/1844710525108550630 | K20 companion (INT-11 copy in another attendee's mailbox) | ● | not Calvin's (companion copy) | connecting |
| 62 | L130 | gmail.gmail_messages | vincent.parker@harmonygames.co/<calendar-5c092c9e-9cc6-a8d4-f609-c777def9599d@google.com> | K20 companion (INT-11 copy in another attendee's mailbox) | ● | not Calvin's (companion copy) | connecting |
| 63 | L132 | gmail.gmail_threads | brian.foster@harmonygames.co/1844614963135138801 | K20 companion (INT-11 copy in another attendee's mailbox) | ● | not Calvin's (companion copy) | connecting |
| 64 | L134 | gmail.gmail_messages | brian.foster@harmonygames.co/<calendar-6c9eab69-d1e0-cf85-0006-87c8c5c5d486@google.com> | K20 companion (INT-11 copy in another attendee's mailbox) | ● | not Calvin's (companion copy) | connecting |
| 65 | L136 | gmail.gmail_threads | brian.foster@harmonygames.co/1844710525109022287 | K20 companion (INT-11 copy in another attendee's mailbox) | ● | not Calvin's (companion copy) | connecting |
| 66 | L138 | gmail.gmail_messages | brian.foster@harmonygames.co/<calendar-02a3fe02-166c-a0c1-6359-2ecb046471be@google.com> | K20 companion (INT-11 copy in another attendee's mailbox) | ● | not Calvin's (companion copy) | connecting |
| 67 | L140 | gmail.gmail_threads | julia.lawson@harmonygames.co/1844614963134787882 | K20 companion (INT-11 copy in another attendee's mailbox) | ● | not Calvin's (companion copy) | connecting |
| 68 | L142 | gmail.gmail_messages | julia.lawson@harmonygames.co/<calendar-fc4cf5c7-ebb2-24d9-33a3-88a114504137@google.com> | K20 companion (INT-11 copy in another attendee's mailbox) | ● | not Calvin's (companion copy) | connecting |
| 69 | L144 | gmail.gmail_threads | julia.lawson@harmonygames.co/1844710525108618407 | K20 companion (INT-11 copy in another attendee's mailbox) | ● | not Calvin's (companion copy) | connecting |
| 70 | L146 | gmail.gmail_messages | julia.lawson@harmonygames.co/<calendar-1f8e4494-259c-8839-1a9c-f9d88a15a894@google.com> | K20 companion (INT-11 copy in another attendee's mailbox) | ● | not Calvin's (companion copy) | connecting |
| 71 | L148 | gmail.gmail_threads | arthur.blake@harmonygames.co/1844614963134486883 | K20 companion (INT-11 copy in another attendee's mailbox) | ● | not Calvin's (companion copy) | connecting |
| 72 | L150 | gmail.gmail_messages | arthur.blake@harmonygames.co/<calendar-f5906aec-0d16-89b0-9b38-62ac2462ad84@google.com> | K20 companion (INT-11 copy in another attendee's mailbox) | ● | not Calvin's (companion copy) | connecting |
| 73 | L152 | gmail.gmail_threads | arthur.blake@harmonygames.co/1844710525108836806 | K20 companion (INT-11 copy in another attendee's mailbox) | ● | not Calvin's (companion copy) | connecting |
| 74 | L154 | gmail.gmail_messages | arthur.blake@harmonygames.co/<calendar-fcb975d6-36c7-90b6-6490-0661d848001a@google.com> | K20 companion (INT-11 copy in another attendee's mailbox) | ● | not Calvin's (companion copy) | connecting |
| 75 | L156 | gmail.gmail_messages | calvin.price@harmonygames.co/<[SOURCE_ORG_0001]-Games/match3d/pull/472/review/3285698310@github.com> | T_INLINE companion (INT-12) | ● | own mailbox | connecting |
| 76 | L158 | gmail.gmail_messages | calvin.price@harmonygames.co/<[SOURCE_ORG_0001]-Games/match3d/pull/475/review/3285755391@github.com> | T_INLINE_PACK companion (INT-12) | ● | own mailbox | connecting |
| 77 | L160 | github.github_reviews | harmonygames-Games/match3d#472#rev_2 | T_INLINE container | ● | unscoped | connecting |
| 78 | L163 | github.github_review_comments | harmonygames-Games/match3d#472#rc_1 | K10, T_INLINE | ● | unscoped | overturning |
| 79 | L165 | github.github_pull_requests (UPDATE) | harmonygames-Games/match3d#472 | companion (counters or updated_at of a base parent) | ● | unscoped | connecting |
| 80 | L166 | github.github_reviews | harmonygames-Games/match3d#475#rev_2 | T_INLINE_PACK container | ● | unscoped | connecting |
| 81 | L168 | github.github_review_comments | harmonygames-Games/match3d#475#rc_1 | K16, T_INLINE_PACK | ● | unscoped | overturning |
| 82 | L170 | github.github_pull_requests (UPDATE) | harmonygames-Games/match3d#475 | companion (counters or updated_at of a base parent) | ● | unscoped | connecting |
| 83 | L171 | github.github_pr_comments | harmonygames-Games/match3d#473#c_2 | K11, T_ELSE | ● | unscoped | overturning |
| 84 | L173 | github.github_timeline_events | harmonygames-Games/match3d#473#ev_5 | T_ELSE companion (timeline) | ● | unscoped | connecting |
| 85 | L175 | linear.linear_issues | ZOM-567 | cohort (sheet row 4), T_STATE | ● | unscoped | connecting |
| 86 | L178 | linear.linear_issues | ZOM-568 | T_BODY, T_STATE | ● | unscoped | connecting |
| 87 | L180 | linear.linear_issues | ZOM-569 | cohort (sheet row 8), T_STATE | ● | unscoped | connecting |
| 88 | L182 | linear.linear_issues | ZOM-570 | cohort (sheet row 10), T_STATE | ● | unscoped | connecting |
| 89 | L184 | linear.linear_issues | ZOM-571 | T_INLINE, T_STATE | ● | unscoped | connecting |
| 90 | L186 | linear.linear_issues | ZOM-572 | T_ELSE, T_STATE | ● | unscoped | connecting |
| 91 | L188 | linear.linear_issues | ZOM-573 | T_ELSE, T_STATE | ● | unscoped | connecting |
| 92 | L190 | linear.linear_issues | ZOM-574 | T_INLINE, T_STATE | ● | unscoped | connecting |
| 93 | L192 | linear.linear_issues | ZOM-575 | cohort (sheet row 16), T_STATE | ● | unscoped | connecting |
| 94 | L194 | linear.linear_issues | ZOM-576 | cohort (sheet row 18), T_STATE | ● | unscoped | connecting |
| 95 | L196 | linear.linear_issues | ZOM-577 | cohort (sheet row 19), T_STATE | ● | unscoped | connecting |
| 96 | L198 | linear.linear_issues | ZOM-578 | cohort (sheet row 21), T_STATE | ● | unscoped | connecting |
| 97 | L200 | linear.linear_issues | ZOM-579 | cohort (sheet row 28), T_STATE | ● | unscoped | connecting |
| 98 | L202 | linear.linear_issues | ZOM-580 | cohort (sheet row 30), T_STATE | ● | unscoped | connecting |
| 99 | L204 | linear.linear_issues | ZOM-581 | T_INLINE_PACK, T_STATE | ● | unscoped | connecting |
| 100 | L206 | linear.linear_issues | ZOM-582 | cohort (sheet row 34), T_STATE | ● | unscoped | connecting |
| 101 | L208 | linear.linear_issues | ZOM-583 | cohort (sheet row 36), T_STATE | ● | unscoped | connecting |
| 102 | L210 | linear.linear_issues | ZOM-584 | T_ELSE, T_STATE | ● | unscoped | connecting |
| 103 | L212 | linear.linear_issues | ZOM-585 | T_REOPEN_TICKET, T_STATE | ● | unscoped | connecting |
| 104 | L214 | linear.linear_issues | ZOM-586 | T_BACK_TICKET | ● | unscoped | connecting |
| 105 | L216 | linear.linear_comments | comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 | K1, T_FIELDS | ● (§6b) | unscoped | connecting |
| 106 | L218 | linear.linear_comments | comment_b3c560833d151268202546002e7613cf on ZOM-556 | K12, T_ALIAS_GIFT | ● (§6b) | unscoped | overturning |
| 107 | L220 | linear.linear_comments | comment_9f28b3d8d66bd04e3f7fc46bc6ed1ea9 on ZOM-560 | K15, T_ALIAS_STREAK | ● (§6b) | unscoped | overturning |
| 108 | L222 | linear.linear_comments | comment_9f8c7854801872ee16fa715063068883 on ZOM-567 | cohort evidence surface (comments of ZOM-567) | ● (§6b) | unscoped | connecting |
| 109 | L224 | linear.linear_comments | comment_a4cc96d8b7ec4c4b4e7376d08682db26 on ZOM-567 | cohort evidence surface (comments of ZOM-567) | ● (§6b) | unscoped | connecting |
| 110 | L226 | linear.linear_comments | comment_78b3bbfd642fcddb7784200bf9a38586 on ZOM-568 | cohort evidence surface (comments of ZOM-568) | ● (§6b) | unscoped | connecting |
| 111 | L228 | linear.linear_comments | comment_21325ccb0fe2dfeb0a19950788d03922 on ZOM-569 | cohort evidence surface (comments of ZOM-569) | ● (§6b) | unscoped | connecting |
| 112 | L230 | linear.linear_comments | comment_062192746d6b79d78445f5875195704c on ZOM-570 | cohort evidence surface (comments of ZOM-570) | ● (§6b) | unscoped | connecting |
| 113 | L232 | linear.linear_comments | comment_0382ec127c135a8e78e6e46d3ae6bde7 on ZOM-571 | cohort evidence surface (comments of ZOM-571) | ● (§6b) | unscoped | connecting |
| 114 | L234 | linear.linear_comments | comment_e35e1ebcdec657d5843c772b8d536b20 on ZOM-572 | cohort evidence surface (comments of ZOM-572) | ● (§6b) | unscoped | connecting |
| 115 | L236 | linear.linear_comments | comment_53122feda2890ba1d869dcac7bfd31e7 on ZOM-573 | cohort evidence surface (comments of ZOM-573) | ● (§6b) | unscoped | connecting |
| 116 | L238 | linear.linear_comments | comment_a69eb9036d70dd58c0419fb714dc539d on ZOM-574 | cohort evidence surface (comments of ZOM-574) | ● (§6b) | unscoped | connecting |
| 117 | L240 | linear.linear_comments | comment_b9543ec84a98f626f839056f2742d981 on ZOM-574 | cohort evidence surface (comments of ZOM-574) | ● (§6b) | unscoped | connecting |
| 118 | L242 | linear.linear_comments | comment_12e3443c29edbf826058ef6de747dd3a on ZOM-575 | cohort evidence surface (comments of ZOM-575) | ● (§6b) | unscoped | connecting |
| 119 | L244 | linear.linear_comments | comment_50cf911b05625950a80c7a90de50b5f3 on ZOM-576 | cohort evidence surface (comments of ZOM-576) | ● (§6b) | unscoped | connecting |
| 120 | L246 | linear.linear_comments | comment_e142e3bc8298e098262130e653cd1cb5 on ZOM-577 | cohort evidence surface (comments of ZOM-577) | ● (§6b) | unscoped | connecting |
| 121 | L248 | linear.linear_comments | comment_fbf3c978c1bcb83cacd26e8765b3652d on ZOM-577 | cohort evidence surface (comments of ZOM-577) | ● (§6b) | unscoped | connecting |
| 122 | L250 | linear.linear_comments | comment_c3fc01c06c5484e9d1ec7b747c0bca39 on ZOM-578 | cohort evidence surface (comments of ZOM-578) | ● (§6b) | unscoped | connecting |
| 123 | L252 | linear.linear_comments | comment_d8ffc9176107fc6cb1964cfe9aa119d7 on ZOM-578 | cohort evidence surface (comments of ZOM-578) | ● (§6b) | unscoped | connecting |
| 124 | L254 | linear.linear_comments | comment_ad0cfb6f62f59c58b63d200cad118497 on ZOM-579 | cohort evidence surface (comments of ZOM-579) | ● (§6b) | unscoped | connecting |
| 125 | L256 | linear.linear_comments | comment_b30f1b7163d9eacac5be034d5cf3ada9 on ZOM-580 | cohort evidence surface (comments of ZOM-580) | ● (§6b) | unscoped | connecting |
| 126 | L258 | linear.linear_comments | comment_c757724005e45903d91d6a340d34bab9 on ZOM-581 | cohort evidence surface (comments of ZOM-581) | ● (§6b) | unscoped | connecting |
| 127 | L260 | linear.linear_comments | comment_d4c24b928744272d1b8ab8e05f04c5aa on ZOM-582 | cohort evidence surface (comments of ZOM-582) | ● (§6b) | unscoped | connecting |
| 128 | L262 | linear.linear_comments | comment_c1260bb5e2f487f140864352f77ae1c5 on ZOM-582 | cohort evidence surface (comments of ZOM-582) | ● (§6b) | unscoped | connecting |
| 129 | L264 | linear.linear_comments | comment_4c2e27e88093aa1454c6074a2dc20db9 on ZOM-583 | cohort evidence surface (comments of ZOM-583) | ● (§6b) | unscoped | connecting |
| 130 | L266 | linear.linear_comments | comment_044b3c340de2ab29acc6b9f9e0713b29 on ZOM-583 | cohort evidence surface (comments of ZOM-583) | ● (§6b) | unscoped | connecting |
| 131 | L268 | linear.linear_comments | comment_d647c4d85dbcc41d2fa8e5796611d0f3 on ZOM-584 | cohort evidence surface (comments of ZOM-584) | ● (§6b) | unscoped | connecting |
| 132 | L270 | linear.linear_comments | comment_95e17b12aea5d7fbf136c9bb0e3399aa on ZOM-585 | cohort evidence surface (comments of ZOM-585) | ● (§6b) | unscoped | connecting |
| 133 | L272 | linear.linear_comments | comment_e7acb32a7937001d44d70c20083ebf1d on ZOM-585 | cohort evidence surface (comments of ZOM-585) | ● (§6b) | unscoped | connecting |
| 134 | L274 | linear.linear_comments | comment_5f530dc138f29bec3080eb175df98921 on ZOM-585 | K21, T_REOPEN_TICKET | ● (§6b) | unscoped | overturning |
| 135 | L276 | linear.linear_comments | comment_e8db330d780764f61abc7e8a6b0166ee on ZOM-586 | cohort evidence surface (comments of ZOM-586) | ● (§6b) | unscoped | connecting |
| 136 | L278 | linear.linear_comments | comment_54ce9965c98adad1af9182104e47c7a0 on ZOM-586 | cohort evidence surface (comments of ZOM-586) | ● (§6b) | unscoped | connecting |
| 137 | L280 | linear.linear_comments | comment_16aff20eceb0906dc0509214c2973635 on ZOM-586 | K22, T_BACK_TICKET | ● (§6b) | unscoped | overturning |
| 138 | L282 | linear.linear_issues (UPDATE) | ZOM-543 | AN2 | ● | unscoped | first link |
| 139 | L283 | linear.linear_issues (UPDATE) | ZOM-556 | companion (counters or updated_at of a base parent) | ● | unscoped | connecting |
| 140 | L284 | linear.linear_issues (UPDATE) | ZOM-560 | companion (counters or updated_at of a base parent) | ● | unscoped | connecting |

## Findability and discovery-order proofs

- Hub AN1 446ba45665ed73d2f06caca6963c6ffc (D0770ET6WBW/1759264805.214409): the newest message from Brian in Calvin's DM with him; first link. AN2 ZOM-543: found by its title; Brian's note is its only comment.
- Authority H1 f_6d0326fa006b136f1bbf82: the note says 'Arthur's rule for QA passes'; a Docs or Drive search for 'QA passes' returns it and the decoy f_ea7517885d11570b54bf13, which differs on the game (Domino Delights hotfixes).
- Authority H2 68daad83bacf52c6ea7e1593: the note says 'the agenda of Thursday's review'; a Trello search for 'flow review' returns it; decoys met first are Brian's own line 345e6d1a65b0b15ec2914567ad11d583 in the anchor chat and the first invitation calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com>.
- T_BRANCH: claim met first: 'ok, chat' on sheet rows 1, 2 and 25 with D06UPGF5PQV/1758820544.160399; overturned by the branch on C05433XK267/1758817549.151639 read against f_6d0326fa006b136f1bbf82; decisive because the legend sends the reader to the chat and the chat names the build.
- T_INLINE: claim met first: Fix #472 on row 12, harmonygames-Games/match3d#472 merged, ZOM-571 In Validation; overturned by harmonygames-Games/match3d#472#rc_1, also in Calvin's mailbox (calvin.price@harmonygames.co/<[SOURCE_ORG_0001]-Games/match3d/pull/472/review/3285698310@github.com>) and in #zombie-prs (8e02c1142dfdd380c577a14bc366ee1d).
- T_INLINE_PACK: claim met first: Fix #475 on row 32, harmonygames-Games/match3d#475 merged, ZOM-581 In Validation; overturned by harmonygames-Games/match3d#475#rc_1, also calvin.price@harmonygames.co/<[SOURCE_ORG_0001]-Games/match3d/pull/475/review/3285755391@github.com> and 69700214ac2e727feec1d08d2b873218.
- T_REOPEN: claim met first: nr on a main build on row 9; overturned by b156fdcd5fd89b8362d0e5fcf24975d1 (Sep 30 21:20Z) under C08R27X0EAH/1757939514.864549; found by Vincent's recent posts or the words 'Submission 135'.
- T_BACK: claim met first: ok on a main build on row 29; overturned by a40824773b7cad9681d141b916a5f558 (Sep 30 21:44Z); found by the channel's recent history or 'endless'.
- T_ELSE: claim met first: blank Fix cells on rows 13 and 38 and ZOM-572 in Todo; overturned by harmonygames-Games/match3d#473#c_2 on harmonygames-Games/match3d#473, also 66dd5332dde5b7312c0ae201c285a323.
- T_FILT: the note's sentence about a bug told in a DM since the 26th; 806f4a67a847d4d47e3e5674760aa630 is the only such report in Calvin's DMs from Sep 26 to 30.
- T_ALIAS_GIFT / T_ALIAS_STREAK: claim met first: blank Ticket cells on rows 11 and 20; overturned by comment_b3c560833d151268202546002e7613cf on ZOM-556 and comment_9f28b3d8d66bd04e3f7fc46bc6ed1ea9 on ZOM-560.
- T_GATE: claim met first: calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com> (Sep 29 16:05Z) and 345e6d1a65b0b15ec2914567ad11d583 (Sep 29 16:41Z); overturned by 68dc11dceb76ad640995fd98 (Sep 30 17:22Z) on card 68daad83bacf52c6ea7e1593.

## Self-validation

| QC category | Tool-enforced (result) | Manual (evidence) |
|---|---|---|
| Missing Universe Data | check-sql PASS (1.E) | every deciding fact persona-readable: f_6d0326fa006b136f1bbf82, C05433XK267/1758817549.151639, harmonygames-Games/match3d#472#rc_1, harmonygames-Games/match3d#475#rc_1, b156fdcd5fd89b8362d0e5fcf24975d1, a40824773b7cad9681d141b916a5f558, harmonygames-Games/match3d#473#c_2, 806f4a67a847d4d47e3e5674760aa630, comment_b3c560833d151268202546002e7613cf, comment_9f28b3d8d66bd04e3f7fc46bc6ed1ea9, 68daad83bacf52c6ea7e1593 |
| Temporal Field | sql_lint 0 errors; base_check Check C PASS | the sheet's last change (19:30Z) is after every build it cites (C05433XK267/1759257787.502039 finished 18:43Z); both later reports follow C05433XK267/1759263189.219529 (20:13Z); Arthur's comments follow his approvals harmonygames-Games/match3d#472#rev_1 and harmonygames-Games/match3d#475#rev_1; ZOM-567 to ZOM-584 follow ZOM-566 |
| Cross-service Referential | base_check Check A PASS | the event's time and guests agree across six calendar rows and ten mails; each GitHub comment has its #zombie-prs copy, and Arthur's two also their mail in the base thread |
| Quantitative | reply counters updated on five base parents | C08R27X0EAH/1757939514.864549 goes from 11 replies to 12 and C08R27X0EAH/1757467270.178829 from 4 to 5, repliers unchanged; the #zombie-prs parents gain one reply each; the sheet has 38 numbered rows |
| State / Lifecycle | no seeded ticket is Done; In Validation tickets carry started_at | ZOM-571, ZOM-576 and ZOM-581 are In Validation because Vincent was told a merged PR had them; the card sits on an open list |
| Identifier / Format | eval lint FAIL 0 CHECK 0 | ids follow base schemes (1.A, 1.F) |
| Semantic / Category | — | titles match content: f_cb40955893624e1acb8500, f_d3a1aa5976285aac98ffda, f_6d0326fa006b136f1bbf82, f_ea7517885d11570b54bf13, f_637e63ae6c1b4a7eb016aa; the review card is a planning card on the roadmap board's Backlog list, next to other undated items |
| Other | — | voice per 1.C; no record states a status, a count or the answer |

## Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| github | INT-01 | Slack copy of each comment in #zombie-prs | seeded: 8e02c1142dfdd380c577a14bc366ee1d, 69700214ac2e727feec1d08d2b873218, 66dd5332dde5b7312c0ae201c285a323, each a reply under its PR's opened message with the parent's counters updated; all three fall inside the match3d window, which ends 2025-09-30T22:33Z |
| github | INT-12 | GitHub mail to the PR author | seeded for Arthur's two comments in the base threads: calvin.price@harmonygames.co/<[SOURCE_ORG_0001]-Games/match3d/pull/472/review/3285698310@github.com>, calvin.price@harmonygames.co/<[SOURCE_ORG_0001]-Games/match3d/pull/475/review/3285755391@github.com>; none for harmonygames-Games/match3d#473#c_2, since Calvin's mailbox holds no thread for harmonygames-Games/match3d#473 |
| github | INT-02, INT-23 | push notices, CodeRabbit | none: no commit and no bot comment is seeded |
| linear | INT-03, INT-04, INT-05 | PR comment, Slack posts, mail digests | none: no PR names a seeded key; the base has no Slack post for ZOM-556 to ZOM-566 beyond links people paste; digests are aggregate |
| gcal | INT-11 | invitation and update mails | seeded for evt_342a813cb7765d4a6fce8d: calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com> and calvin.price@harmonygames.co/<calendar-f2b39cd5-884e-2def-a4d7-d41d80d4c55b@google.com> in Calvin's mailbox, and copies for Vincent, Brian, Julia and Arthur; none in the organizer's own mailbox |
| gdrive | INT-13 | Drive share DMs and mails | none: Calvin's mailbox holds nine share notices in all and none after March 2025, so shares of f_cb40955893624e1acb8500 and f_6d0326fa006b136f1bbf82 without a notice follow the base |
| slack | INT-22 | Slack mail digests | none (D0770ET6WBW/1759264805.214409) |
| trello | INT-21 | none exists | none (68daad83bacf52c6ea7e1593) |
| jenkins | INT-06 | #builds posts | none seeded: every build cited is a base post |
| gdocs, gsheets, gslides | not integration sources | — | none |

## Touched-data census and coherence hazards

Touched data: 446ba45665ed73d2f06caca6963c6ffc, ZOM-543, f_cb40955893624e1acb8500 and its legend, tickets ZOM-556, ZOM-560, ZOM-567 to ZOM-584, decoys ZOM-432 and ENG-2069; harmonygames-Games/match3d#465, harmonygames-Games/match3d#472, harmonygames-Games/match3d#473, harmonygames-Games/match3d#475 with their bodies, reviews, comments and timelines; #builds posts for the 16 builds the sheet and the chats name (C05433XK267/1758817549.151639, C05433XK267/1758737279.948339, C05433XK267/1759173858.825639, C05433XK267/1759263189.219529 and the twelve main builds in `solver/solver.py`); Calvin's DMs with Brian, Vincent, Marcus and Julia from Sep 23 to 30 (D0770ET6WBW/1758808795.588519, D06UPGF5PQV/1758817744.353289, D05U73FNDDL/1759161394.516899, D05HYDTG5TJ/1756838837.147599); #zombie-bugs thread C08R27X0EAH/1757939514.864549 and the tutorial skip thread C08R27X0EAH/1758903616.346579; #zombie-match3d from Sep 29; the #zombie-prs threads C093LEZGF6J/1759185399.395419, C093LEZGF6J/1759246868.802449 and C093LEZGF6J/1759247948.371729; Calvin's GitHub mail threads for harmonygames-Games/match3d#472 and harmonygames-Games/match3d#475; ZM ROADMAP's Backlog list 68c451221ebabaf255a7d16b and cards 68c453cd0ff184d95550bc58 and 6851a7abf7876721472dba99; Vincent's Bug Checklist canvas CF4EDAF93359/1759236624.010909 and the Collect & Win canvas C3DD99314033/1758897445.985019, which Brian's note leaves as they are.

Hazards from coherence_hazards.json:
- temporal: T01 — the two seeded reviews add no 'reviewed' timeline event, as base reviews' events carry no time or actor to copy; T06 — the card's dateLastActivity equals its last action, and the board's is moved to it; T02 not touched: no thread file is read for order.
- semantic: S01 — no seeded record cites an ENG key for ZOM work; S02 — the epic's children stay in the ZOM team.
- referential: R07 — every seeded GitHub comment has its #zombie-prs copy; R08 — both invitation mails have their calendar rows; R03 — the two GitHub mails keep the base threads' redacted subjects; R04 — no seeded text links a Google file.
- quantitative: Q01, Q02, Q03 — the five base parents' reply_count, reply_users_count and latest_reply are updated with the seeded replies (C08R27X0EAH/1757939514.864549, C08R27X0EAH/1757467270.178829, C093LEZGF6J/1759185399.395419, C093LEZGF6J/1759246868.802449, C093LEZGF6J/1759247948.371729); Q11 — the six calendar copies agree field for field.
- state/lifecycle: L09, L10 — harmonygames-Games/match3d#473 merged with no review and harmonygames-Games/match3d#465 with bot reviews only, which is base truth and not relied on beyond their merged state; L03 — statuses rest on Brian's rule, never on a ticket state as proof of shipping; L06 — ZOM-543 stays In Progress and no parent is Done over an open child; L08 — every seeded assignee is active at the clock.
- identifier/format: I08 — the #zombie-prs copies show real logins (arthur.blake, oliver.brooks) while GitHub rows keep the tokens, as in the base; I09 — the copies keep the unredacted org as the base copies of these three PRs do; I16 — Trello ids encode their own time; I10 — no seeded Linear author uses an irregular user id.

Known data issues (references/known_data_issues/synthcut.md; no load-bearing fact, trap or graded slot rests on a card's 'Don't grade' value):
- SC-6: no mail from Brian is seeded or read; his copy of the invitation is a companion sent by Leonard.
- SC-7: channel membership is used only for reach, never graded.
- SC-13: the BETA list and its name are not touched; the card is on Backlog and the review's date comes from the card and the invitation.
- SC-14: no card's complete flag is read; the Queue Manager card's tick is a decoy the statuses never use.
- SC-15: ZOM-521, ZOM-526 and ZOM-528 are not reports and not touched.
- SC-16: ZOM-564, ZOM-513, ZOM-514 and ZOM-563 are not reports; no ticket state is proof of shipping, and the three state changes follow the status worked out from the records.
- SC-18: PR #477 is not cited.
- SC-19: no telemetry version is matched to a build; branches come from #builds posts.
- SC-22: time_in_status_minutes is NULL on every seeded ticket and never read.
- SC-38: no Season Pass ship date is used; the Season Pass rows rest on re-tests and PRs.
- SC-56: no commit title is quoted; builds are matched by job and number.
- SC-57: no post in #zm-collect-win is seeded or required.
- SC-67: build #1621 is not cited.
- SC-68: Boss Arena rows rest on re-tests, not on when the mode reached production.
- SC-70: time zones come from the calendar and base invitation subjects, never from Slack.

## Intended disagreements

| Claim met first | Overturning record | Why realistic | Resolution |
|---|---|---|---|
| 'ok, chat' on rows 1, 2 and 25 of f_cb40955893624e1acb8500 and Vincent's ok in D06UPGF5PQV/1758820544.160399 | the #builds post C05433XK267/1758817549.151639 (a feature-branch build) read against f_6d0326fa006b136f1bbf82 | a tester says ok on the build the dev handed him | Brian's note: a pass counts only on a build Arthur's rule counts |
| Fix #472 on row 12 and ZOM-571 In Validation | Arthur's review comment harmonygames-Games/match3d#472#rc_1 | a tester writes down the PR he was told and the reviewer sees the diff | the note asks whether a fix is in main; the reviewer says it is not in that PR |
| Fix #475 on row 32 and ZOM-581 In Validation | Arthur's review comment harmonygames-Games/match3d#475#rc_1 | same | same |
| nr on row 9 of f_cb40955893624e1acb8500 | Vincent's reply b156fdcd5fd89b8362d0e5fcf24975d1 | a tester mentions a relapse where he happens to be writing | Arthur's note: a pass stands until somebody sees the bug again on a main build made after the one it passed on |
| ok on row 29 of f_cb40955893624e1acb8500 | Robert's post a40824773b7cad9681d141b916a5f558 | a founder reports what he saw while playing the submission build | same sentence |
| blank Fix on rows 13 and 38, ZOM-572 Todo | Oliver's line harmonygames-Games/match3d#473#c_2 on harmonygames-Games/match3d#473 | a dev notes on his own PR what else it carries, and QA's list does not know | the note asks whether a fix is in main; the dev says on his own merged PR that it is |
| Brian's line 345e6d1a65b0b15ec2914567ad11d583 and the first invitation calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com>: Collect & Win and Daily Gift, Friday | the changed card 68daad83bacf52c6ea7e1593 (68dc11dceb76ad640995fd98) and calvin.price@harmonygames.co/<calendar-f2b39cd5-884e-2def-a4d7-d41d80d4c55b@google.com> | a review is moved and its agenda changed by its organizer | the note names Leonard's review card |
| f_ea7517885d11570b54bf13: a pass on the dev's branch build is enough | f_6d0326fa006b136f1bbf82: for ZM only main builds count | two notes by the same lead for two games | the game: the task is ZM |

## Constraints for the prompt brief

| Anchor | May be named (noun phrases only) | Record |
|---|---|---|
| AN1 | Brian's message from yesterday; Brian's DM | 446ba45665ed73d2f06caca6963c6ffc |
| AN2 | the Queue Manager ticket; ZOM-543 | ZOM-543 |

Never name in the prompt: Brian's note or any of its sentences, the pass sheet's legend, Arthur's doc, Leonard's card or Trello, the invitation mails, #builds or any build number, any PR number or review comment, Vincent's thread reply, Robert's post, Oliver's comment, Marcus or his report, ZOM-556 or ZOM-560, any status, count or area. Deliverable kinds: Linear child issues, sub-issues, moves, notes and state changes; one Google Sheet in Calvin's folder, shared; one slide in Calvin's deck; one Slack reply in Brian's DM. No deadline is graded; the review is on Thu Oct 2.

## Fact sheet

| Key | Value | Kind | Home / must appear in |
|---|---|---|---|
| which builds count for a pass | a QA pass only counts on a build of the main branch | status | f_6d0326fa006b136f1bbf82 |
| review on #472 | That one isn't in this diff | status | harmonygames-Games/match3d#472#rc_1, calvin.price@harmonygames.co/<[SOURCE_ORG_0001]-Games/match3d/pull/472/review/3285698310@github.com>, 8e02c1142dfdd380c577a14bc366ee1d |
| review on #475 | Don't see the pack sound stop anywhere in here | status | harmonygames-Games/match3d#475#rc_1, calvin.price@harmonygames.co/<[SOURCE_ORG_0001]-Games/match3d/pull/475/review/3285755391@github.com>, 69700214ac2e727feec1d08d2b873218 |
| pass popup is back | the pass popup came up on top of the gift again | status | b156fdcd5fd89b8362d0e5fcf24975d1 |
| home intro is back | the home intro animation played again every single time | status | a40824773b7cad9681d141b916a5f558 |
| Oliver's merged fixes | this also has the fix for the pass start popup coming back after every level and for the pass bar filling before the tokens land | status | harmonygames-Games/match3d#473#c_2, 66dd5332dde5b7312c0ae201c285a323 |
| Marcus's report | the pass icon glow stays on after i claimed everything | status | 806f4a67a847d4d47e3e5674760aa630 |
| review areas | Collect & Win, Level-end rewards | status | 68daad83bacf52c6ea7e1593, 68dc11dceb76ad640995fd98 |
| tie to the gift ticket | Saw this one myself in my home screen pass on 1727 | status | comment_b3c560833d151268202546002e7613cf |
| tie to the freezer ticket | Still there on Android 1984 in my home screen pass | status | comment_9f28b3d8d66bd04e3f7fc46bc6ed1ea9 |

```
FACT CHECK: PASS — 109 text-bearing rows, 10 declared facts, 5 declared superseded records
Errors: none
Warnings (1):
  line 126: gmail.gmail_messages vincent.parker@harmonygames.co/<calendar-bb830870-1845-b709-820d-db5ca3233174@google.com>: [value_drift] 'meeting 'zm home screen flow review'' carries 2 different dates across rows: '2025-10-02 18:00Z (event start)' (line 102, row evt_0e5a1e82445aa0f1f7e4b9, +10); 'Fri Oct 3, 2025 (invitation)' (line 126, row vincent.parker@harmonygames.co/<calendar-bb830870-1845-b709-820d-db5ca3233174@google.com>, +3) — supersession (declare it in trapsnone.version_records / facts) or drift?
```

Warning disposition: the value_drift warning compares the event's start (Thu Oct 2) with the first invitation's Fri Oct 3. That difference is the designed move of the review, recorded by the updated invitation and the changed card; every mailbox copy of each mail carries the same date.

Solver totals (`solver/truth.json`): 39 reports (38 sheet rows and 1 raised outside it): Passed 10, Waiting on QA 9, Waiting on a fix 20; 0 clear area of 10; 7 on the review list; 22 held by an existing ticket and 17 new sub-issues; 8 existing tickets change state.

| Area | Reports | Open | Status |
|---|---|---|---|
| Tutorials | 5 | 3 | Open |
| Level-end rewards | 5 | 3 | Open |
| Daily Gift | 3 | 3 | Open |
| Season Pass | 5 | 5 | Open |
| Collect & Win | 4 | 4 | Open |
| Win Streak | 3 | 3 | Open |
| Zombie Lane | 3 | 1 | Open |
| Boss Arena | 3 | 1 | Open |
| Endless Mode | 4 | 4 | Open |
| Card packs | 4 | 2 | Open |

| Report | Area | Status | Ticket | Review list | Ticket state (as found → to set) |
|---|---|---|---|---|---|
| Back to back tutorials at level 16-17 only play the first one | Tutorials | Waiting on QA | new sub-issue | No | — → In Validation |
| Card upgrade tutorial never shows after the Zombie Lane one | Tutorials | Waiting on QA | new sub-issue | No | — → In Validation |
| Quest tutorial arrow points at the wrong tab after the last panel closes | Tutorials | Passed | new sub-issue | No | — → Done |
| Win streak tutorial at level 20 freezes the home screen | Tutorials | Waiting on a fix | ZOM-567 | No | Todo → Todo |
| Coin animation plays again after killing and reopening the app | Level-end rewards | Passed | new sub-issue | No | — → Done |
| Level-end coins fly while the pre-level panel is already open | Level-end rewards | Waiting on QA | ZOM-568 | Yes | Todo → In Validation |
| Reward count-up is skipped when tapping fast on play | Level-end rewards | Passed | new sub-issue | No | — → Done |
| Stars from the level fly to the wrong corner on tablets | Level-end rewards | Waiting on a fix | ZOM-569 | Yes | Todo → Todo |
| Season pass popup comes up on top of the daily gift when both are due | Daily Gift | Waiting on a fix | new sub-issue | No | — → Todo |
| Daily gift calendar opens before the level-end coins finish | Daily Gift | Waiting on a fix | ZOM-570 | No | Todo → Todo |
| Daily gift day counter keeps going after a skipped day | Daily Gift | Waiting on a fix | ZOM-556 | No | Todo → Todo |
| Season pass icon animation restarts every time a panel closes | Season Pass | Waiting on a fix | ZOM-571 | No | In Validation → Todo |
| Season pass start popup shows again after every level until it is claimed | Season Pass | Waiting on QA | ZOM-572 | No | Todo → In Validation |
| Season pass reward claim animation plays twice when coming back from the shop | Season Pass | Waiting on QA | ZOM-573 | No | Todo → In Validation |
| Event bar starts filling while the daily gift popup is still open | Collect & Win | Waiting on a fix | ZOM-574 | Yes | In Validation → Todo |
| Endless unlock banner shows again after coming back from a level | Endless Mode | Waiting on a fix | ZOM-575 | No | Todo → Todo |
| Reward animation waits too long before the event bar fills | Collect & Win | Waiting on a fix | ZOM-585 | Yes | In Validation → Todo |
| Event panel opens over the level-end rewards on first unlock | Collect & Win | Waiting on QA | ZOM-576 | Yes | In Validation → In Validation |
| Event progress popup opens before the level-end coins finish | Collect & Win | Waiting on a fix | ZOM-577 | Yes | Todo → Todo |
| Win streak freezer from the abandoned pack never shows up on the home screen | Win Streak | Waiting on a fix | ZOM-560 | No | Todo → Todo |
| Streak counter jumps by two after a win when other panels are waiting | Win Streak | Waiting on a fix | ZOM-578 | No | Todo → Todo |
| Zombie Lane reward animation plays under the home buttons | Zombie Lane | Passed | new sub-issue | No | — → Done |
| Zombie Lane panel opens twice after claiming | Zombie Lane | Passed | new sub-issue | No | — → Done |
| Lane progress bar animates from zero every time | Zombie Lane | Waiting on a fix | ZOM-586 | No | Todo → Todo |
| Boss arena tutorial does not play when another tutorial is queued before it | Boss Arena | Waiting on QA | new sub-issue | No | — → In Validation |
| Boss arena unlock popup shows behind the level-end rewards | Boss Arena | Passed | new sub-issue | No | — → Done |
| Arena entry button can be tapped during the reward animation | Boss Arena | Passed | new sub-issue | No | — → Done |
| Endless unlock banner overlaps the daily gift | Endless Mode | Waiting on a fix | ZOM-579 | No | Todo → Todo |
| Coming back from Endless replays the home intro animation | Endless Mode | Waiting on a fix | new sub-issue | No | — → Todo |
| Endless reward chest opens before the coins land | Endless Mode | Waiting on a fix | ZOM-580 | No | Todo → Todo |
| Tap to collect prompt is missing when a pack opens after a level | Card packs | Passed | new sub-issue | No | — → Done |
| Pack opening sound keeps playing on the home screen after the pack closes | Card packs | Waiting on a fix | ZOM-581 | No | In Validation → Todo |
| Last pack does not show its cards before closing | Card packs | Passed | new sub-issue | No | — → Done |
| Pack count on the home button only updates after a restart | Card packs | Waiting on a fix | ZOM-582 | No | Todo → Todo |
| Tutorial hand stays on screen after the last panel closes | Tutorials | Passed | new sub-issue | No | — → Done |
| Level-end rewards do not show at all right after an app update | Level-end rewards | Waiting on a fix | ZOM-583 | Yes | Todo → Todo |
| Win streak freezer popup opens behind the season pass popup | Win Streak | Waiting on QA | ZOM-584 | No | Todo → In Validation |
| Pass progress bar fills before the tokens arrive | Season Pass | Waiting on QA | new sub-issue | No | — → In Validation |
| Pass icon glow stays on after everything is claimed | Season Pass | Waiting on a fix | new sub-issue | No | — → Todo |

## Facts for the human

| Locator | Base/seeded | Fact | Reach | Role |
|---|---|---|---|---|
| 446ba45665ed73d2f06caca6963c6ffc | seeded | Brian to Calvin, 2025-09-30T20:40:05Z (D0770ET6WBW/1759264805.214409): the ask, the sheet, the share, the slide and the five numbers to send back | DM member | anchor |
| comment_faaa792418a942cd40be046d8d217a7d on ZOM-543 | seeded | Brian's note, 2025-09-30T20:25:37Z: the ten areas, what counts as a report, the three statuses, the ticket rule, the state mapping, Clear and Open, the review list, the sheet's tabs and columns | unscoped | delegation |
| f_cb40955893624e1acb8500 | seeded | Vincent's 'ZM home screen flow pass', 38 rows (#, Area, What happens, Found on, Ticket, Fix, Re-test), last changed 2025-09-30T19:30:52Z | shared | requirement, claims met first |
| f_d3a1aa5976285aac98ffda | seeded | Vincent's 'How to read my pass sheets', 2025-09-26T10:31:08Z: ok, nr, again, 'ok, chat', and that Fix is the PR he was told | shared | format |
| f_6d0326fa006b136f1bbf82 | seeded | Arthur's 'ZM builds and QA passes', 2025-09-12T22:29:41Z: a QA pass only counts on a build of the main branch | shared | authority H1 |
| f_ea7517885d11570b54bf13 | seeded | Arthur's 'DD hotfix builds and QA passes', 2025-07-10T15:49:27Z: a branch-build pass is enough for DD hotfixes | shared | decoy of H1 |
| 68daad83bacf52c6ea7e1593 | seeded | Leonard's card on ZM ROADMAP, Backlog list: 'ZM home screen flow review - Thu Oct 2', areas Collect & Win and Level-end rewards; changed 2025-09-30T17:22:36Z (action 68dc11dceb76ad640995fd98); first version Fri Oct 3 with Collect & Win and Daily Gift | unscoped | authority H2 |
| 345e6d1a65b0b15ec2914567ad11d583 | seeded | Brian to Calvin, 2025-09-29T16:41:12Z (D0770ET6WBW/1759164072.337219): Friday, collect&win and daily gift first | DM member | claim met first (T_GATE) |
| calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com> | seeded | Invitation from Leonard, 2025-09-29T16:05:14Z: Fri Oct 3, 12pm to 12:30pm CST; description names Collect & Win and Daily Gift | own mailbox | claim met first (T_GATE), decoy |
| calvin.price@harmonygames.co/<calendar-f2b39cd5-884e-2def-a4d7-d41d80d4c55b@google.com> | seeded | Updated invitation with note, 2025-09-30T17:24:09Z: Thu Oct 2, 12pm to 12:30pm CST; 'Moved up a day. Agenda is on the roadmap card, I changed it.' | own mailbox | evidence (T_GATE), recipient list |
| evt_342a813cb7765d4a6fce8d | seeded | Calvin's copy of the event, Thu Oct 2 2025 18:00 to 18:30 UTC; attendees Leonard (organizer), Brian, Arthur, Julia, Vincent, Calvin | own calendar | recipient list (T_SHARE) |
| harmonygames-Games/match3d#472#rc_1 | seeded | Arthur on harmonygames-Games/match3d#472, 2025-09-30T15:53:40Z: the season pass icon restart is not in this diff, only the Collect & Win wait | unscoped | overturning (T_INLINE) |
| harmonygames-Games/match3d#475#rc_1 | seeded | Arthur on harmonygames-Games/match3d#475, 2025-09-30T16:09:50Z: the pack sound stop is nowhere in it | unscoped | overturning (T_INLINE_PACK) |
| harmonygames-Games/match3d#473#c_2 | seeded | Oliver on his own harmonygames-Games/match3d#473, 2025-09-30T15:42:10Z: it also has the fix for the pass start popup coming back and for the pass bar filling before the tokens land | unscoped | overturning (T_ELSE) |
| 8e02c1142dfdd380c577a14bc366ee1d, 69700214ac2e727feec1d08d2b873218, 66dd5332dde5b7312c0ae201c285a323 | seeded | the GitHub app's copies of those three comments in #zombie-prs, each under its PR's opened message | channel member | alternate path |
| b156fdcd5fd89b8362d0e5fcf24975d1 | seeded | Vincent under C08R27X0EAH/1757939514.864549, 2025-09-30T21:20:12Z: on Android Submission 135 the pass popup came up on top of the gift again | channel member | overturning (T_REOPEN) |
| a40824773b7cad9681d141b916a5f558 | seeded | Robert under C08R27X0EAH/1757467270.178829 in #zombie-bugs, 2025-09-30T21:44:12Z: on Android Submission 135 the home intro animation played again every time after Endless | channel member | overturning (T_BACK) |
| 806f4a67a847d4d47e3e5674760aa630 | seeded | Marcus to Calvin, 2025-09-30T17:10:12Z: on that day's main build the pass icon glow stays on after everything is claimed | DM member | report outside the sheet (T_FILT) |
| comment_b3c560833d151268202546002e7613cf on ZOM-556 | seeded | Vincent, 2025-09-30T18:05:21Z: saw it again in his home screen pass on 1727, the day counter keeps going after a skipped day | unscoped | overturning (T_ALIAS_GIFT) |
| comment_9f28b3d8d66bd04e3f7fc46bc6ed1ea9 on ZOM-560 | seeded | Vincent, 2025-09-30T18:08:48Z: still there on Android 1984, the freezer from the abandoned pack never shows on home | unscoped | overturning (T_ALIAS_STREAK) |
| ZOM-567 to ZOM-584 | seeded | Vincent's 18 tickets of Sep 30 16:43Z to 18:44Z, one per sheet row with a key; ZOM-571, ZOM-576 and ZOM-581 In Validation, the rest Todo; each has his note and six have a reply | unscoped | evidence, write targets |
| d_36cdb0374c4aad3b8bf741 | seeded | Calvin's folder 'ZM queue manager' in his Drive root | owner | write target |
| f_637e63ae6c1b4a7eb016aa | seeded | Calvin's deck 'ZM queue manager', four slides, shared with Brian | owner | write target |
| ZOM-543 | base | Queue Manager, In Progress, assigned to Calvin, created by Brian 2025-09-15 | unscoped | anchor, write target |
| ZOM-556 | base | 'When the daily gift is skipped, it doesn't reset to 0.', Todo, Vincent, 2025-09-22 | unscoped | evidence (T_ALIAS_GIFT) |
| ZOM-560 | base | 'The abandoned pack win streak freezer reward is not granted.', Todo, Vincent, 2025-09-22 | unscoped | evidence (T_ALIAS_STREAK) |
| D06UPGF5PQV/1758817744.353289 | base | Calvin to Vincent, Sep 25 16:29Z: 'Match 3D iOS Internal - #1718 already tested' | DM member | evidence (T_BRANCH) |
| D06UPGF5PQV/1758820544.160399 | base | Vincent, Sep 25 17:15Z: 'Looks ok to me', then 'Boss arena as well' | DM member | claim met first (T_BRANCH) |
| C05433XK267/1758817549.151639 | base | Match3D iOS Internal #1718, built from Calvin's QueueManager branch | channel member | overturning (T_BRANCH) |
| C05433XK267/1759263189.219529 | base | Match3D Android Submission #135, built from main, Sep 30 20:13Z | channel member | evidence (T_REOPEN, T_BACK) |
| harmonygames-Games/match3d#465 | base | merged 2025-09-25T22:15:51Z; coin replay and queued tutorials | unscoped | evidence (rows 1, 2, 5, 25) |
| harmonygames-Games/match3d#472 | base | merged 2025-09-30T15:53:04Z; the Collect & Win wait | unscoped | evidence (rows 12, 17, 18) |
| harmonygames-Games/match3d#473 | base | Oliver's Addressables/sp, merged by him 2025-09-30T15:41:20Z | unscoped | evidence (rows 13, 38) |
| harmonygames-Games/match3d#475 | base | merged 2025-09-30T16:09:15Z; card pack open and close flow | unscoped | evidence (rows 31, 32, 33) |
| D0770ET6WBW/1758808795.588519 | base | Brian, Sep 25: the input blocker is not a problem right now | DM member | evidence (T_PARK) |
| D05HYDTG5TJ/1756838837.147599 | base | Julia's point about Calvin's tickets | DM member | evidence (T_FIELDS) |

## Platform follow-ups

- ○ carrier: the event's description ('Agenda is on the roadmap card.') is supporting only; the areas are on the card and the attendee list is in attendees_json. Nothing graded rests on a description.
- Confirm in the pre-check that Slack tools return the attachment text of #builds posts (the branch of C05433XK267/1758817549.151639) and of the #zombie-prs copies; Ask_Carriers says Slack tools return attachments.
- Confirm that `linear_list_comments` returns the seeded notes and that no list call returns comments in bulk.
- Confirm that `github_get_pull_request_comments` returns the two review comments and that the reviews list shows the COMMENTED review with an empty body.
- Forecast blind spot: in exact mode the forecast never fails write-content slots, so its E[avg] overstates the pass rate; the design-mode view is reported beside it under Preflight.
- Pre-check: confirm counted calls exceed 130 and that no run shows `model_refusal_fallback`.
- No independent red team ran (REDTEAM_* unset; fallback recorded in the scenario design section 13); blind fork and coherence sweeps on this SQL are recorded below.

## Self-review

### Tool outputs (final SQL, verbatim)

```
schemas touched (10): gcal, gdocs, gdrive, github, gmail, gsheets, gslides, linear, slack, trello
rows by schema: {'gdrive': 6, 'gdocs': 3, 'gsheets': 2, 'gslides': 13, 'slack': 18, 'trello': 6, 'gcal': 6, 'gmail': 22, 'github': 8, 'linear': 56}  total rows: 140  ops: {'insert': 129, 'update': 11}
errors: 0  warnings: 12
  warn  line 102: gcal.gcal_events.start_ts = 2025-10-02T18:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 102: gcal.gcal_events.end_ts = 2025-10-02T18:30:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 105: gcal.gcal_events.start_ts = 2025-10-02T18:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 105: gcal.gcal_events.end_ts = 2025-10-02T18:30:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 107: gcal.gcal_events.start_ts = 2025-10-02T18:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 107: gcal.gcal_events.end_ts = 2025-10-02T18:30:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 109: gcal.gcal_events.start_ts = 2025-10-02T18:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 109: gcal.gcal_events.end_ts = 2025-10-02T18:30:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 111: gcal.gcal_events.start_ts = 2025-10-02T18:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 111: gcal.gcal_events.end_ts = 2025-10-02T18:30:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 113: gcal.gcal_events.start_ts = 2025-10-02T18:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 113: gcal.gcal_events.end_ts = 2025-10-02T18:30:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
```

```
BASE CHECK (/injection A + C, static): PASS  — 129 inserts, 11 updates
KB: bound (2025-10-01) — KB bound to the selected universe
Check A — records, references, IDs: PASS
Check C — dates and relationships: PASS
  note: gsheets.sheets_sheets: no base-reference rules (checked by sql_lint only)
  note: gslides.slides_page_elements: no base-reference rules (checked by sql_lint only)
  note: gslides.slides_pages: no base-reference rules (checked by sql_lint only)
```

```
BASE CLAIMS (injected text vs base git + #builds): PASS · 0 branch mentions · 0 fail · 0 warn · 0 date-only
branch windows:
```

```
HARDNESS GATE (extreme): PASS
  [ok] assignment_context: manifest bound to current V3 assignment, freeze and policy
  [ok] effective_profile: effective_profile 'extreme' for 'Long Horizon' → thresholds 'extreme'
  [ok] sql_lint_clean: 0 lint error(s) — run tools/sql_lint.py
  [ok] base_consistency: /injection-style checks vs the base universe: A 0 finding(s), C 0 finding(s), 0 warning(s) — run tools/base_check.py --manifest
  [ok] persona_reach: 34 load-bearing seeded ids for calvin_price (20 in unscoped services = visible, 14 judged by persona_view check-sql); not provably visible: none
  [ok] fact_consistency: fact_check: 0 error(s) (10 declared facts), 1 drift warning(s); first: none — run tools/fact_check.py --manifest --no-leak
  [ok] hazard_scope: 0 pre-existing hazard(s) among task-touched records; state/lifecycle or referential without a verified resolution: none
  [ok] services_injected: 10 schemas injected (gcal, gdocs, gdrive, github, gmail, gsheets, gslides, linear, slack, trello); need ≥ 10
  [ok] rows: 129 INSERTed rows (UPDATE companions not counted; 140 rows in all); need ≥ 120
  [ok] services_carrying_weight: 10 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: schemas injected but absent from the design: none
  [ok] seeded_ids_exist_in_sql: 81 seeded ids cited; missing from SQL: none
  [ok] anchors: 2 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 21 fragments; need ≥ 12
  [ok] ask_fragment_services: 10 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 20 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 9 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 49; need ≥ 40 (source-defined: True)
  [ok] evidence_surfaces: 4 surfaces over 4 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 53; need ≥ 40
  [ok] call_budget: unconditional (verified) floor 201 of 201 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 180 (requester-confirmed volume_exception)
  [ok] call_budget_spread: 10 services in budget; largest share outside the per-record phase 29% (≤ 50%)
  [ok] traps: 27 traps across 9 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 7 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 6 supersessions (5 with versions in ≥ 2 services, 1 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: 6 trap(s) with version_records; the records' own timestamps (SQL created_at/ts/date/updated_at, or the base record) must be strictly increasing in the listed order (oldest first); bad: none
  [ok] distractors: 10 distractors of 7 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 10 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 6 chains with 6 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] mechanism_portfolio: 8 portfolio entries, each a mechanism-enum id with trap/chain nodes, a requirement, a natural-reading fallback and a prior family with its reason
  [ok] artifact_fields: declared ['gradable_surface', 'solver']: paths relative, digests sha256
  [ok] hidden_authorities: 2 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 1 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 16 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 9 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 7 writes over 5 services; each must depend on findings
  [note] volume_exception: call-budget floor 180 and per-record floor 40 replace 500 and 300; every other extreme target applies — reason: 49 cohort records and about 200 honest calls; reaching 500 would need padding, w; requester confirmation: requester, Claude Code chat 2026-11-10: 'i want over 130 tool calls in each runs
```

hg.py lint: counts FAIL 0, CHECK 0, INFO 0; no CHECK line to disposition.

sql_lint warning class 'on/after the clock' (12 lines, gcal.gcal_events start_ts and end_ts): the review is a meeting planned for Thu Oct 2 18:00Z, a not-yet-happened event; its created and updated stamps are Sep 29 and Sep 30, and nothing treats it as held.

### Preflight (S4b–S5e)

```
SOLVER CONTRACT: PASS · solver.py sha 337c6a63f446 · sql 479b8441f52e · 8 rules
  [PASS] contract.interface: 8 rules, each with mechanism, requirement and natural_reading; optional: ['touched', 'deciding', 'DEGRADES']
  [PASS] contract.deterministic: two fresh solves (forward and reverse key order) give identical output (40 keys, sha 60d5e78fb252), and so do fresh processes with PYTHONHASHSEED 1 and 2
  [PASS] contract.regression: no previous revision supplied (first revision)
  [PASS] contract.rules_nodes: 8 rules vs 8 portfolio entries: one-to-one
  [PASS] contract.slots: 32 direct/aggregate slots read a solver value; 31 write-content/delivery slots are graded from the writes, not the solver
  [PASS] contract.controls: BRANCH: 3 control(s); branch_over moves ['Coin animation plays again after killing and reopening the app', 'Last pack does not show its cards before closing', 'Tap to collect prompt is missing when a pack opens after a level']; INLINE: 1 control(s); inline_over moves ['Event panel opens over the level-end rewards on first unlock']; REOPEN: 2 control(s); reopen_over moves ['Arena entry button can be tapped during the reward animation', 'Reward count-up is skipped when tapping fast on play']; BACK: 2 control(s); back_over moves ['Zombie Lane panel opens twice after claiming', 'Zombie Lane reward animation plays under the home buttons']; ELSE: 2 control(s); else_over moves ['Endless reward chest opens before the coins land', 'Event progress popup opens before the level-end coins finish']; FILT: 1 control(s); filt_over moves ["Pass icon VFX remark in Vincent's chat"]; ALIAS: 2 control(s); alias_over moves ['Back to back tutorials at level 16-17 only play the first one', 'Pass progress bar fills before the tokens arrive']; GATE: 2 control(s); gate_over moves ['Endless unlock banner overlaps the daily gift', 'Streak counter jumps by two after a win when other panels are waiting']; channel CH-BRANCH (scale): miss_branch moves 3 of 3 member(s); channel CH-INLINE (scale): miss_inline moves 3 of 3 member(s); channel CH-REOPEN (scale): miss_reopen moves 2 of 2 member(s); channel CH-BACK (scale): miss_back moves 2 of 2 member(s); channel CH-ELSE (scale): miss_else moves 5 of 5 member(s); channel CH-FILT (scale): miss_filt moves 1 of 1 member(s); channel CH-ALIAS (scale): miss_alias moves 2 of 2 member(s); channel CH-GATE (scale): miss_gate moves 6 of 6 member(s)
  [PASS] contract.golden: 19 golden values checked against their deciding records (12 sampled keys x 5 fields): 19 identifier values found, 0 short tokens found, 0 presence-type; 41 unverified e.g. ['Back to back tutorials at level 16-17 only play the first one/Report: no evidence ids', 'Back to back tutorials at level 16-17 only play the first one/Ticket: no evidence ids']
  [PASS] contract.digest: manifest solver Working_Files/solver/solver.py digest 337c6a63f446 vs file 337c6a63f446
```

```
MUTATION · rev1 · sql 479b8441f52e · deterministic design diagnostics from the solver; on the Season Pass backtests these are development fixtures, not validation
  key-locality: PASS on 48 of 48 configurations checked
  rule:BRANCH                        KILLED     flipped  15 flips direct slot(s) of weight >= 3: ['B1', 'B2', 'B3']
  rule:INLINE                        KILLED     flipped  15 flips direct slot(s) of weight >= 3: ['I1', 'I4', 'I6']
  rule:REOPEN                        KILLED     flipped  15 flips direct slot(s) of weight >= 3: ['R1', 'R4', 'R6']
  rule:BACK                          KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['K1B', 'K4B']
  rule:ELSE                          KILLED     flipped  25 flips direct slot(s) of weight >= 3: ['E5', 'E6', 'E7', 'E1', 'E2']
  rule:FILT                          KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['F1', 'F3']
  rule:ALIAS                         KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['A1', 'A2']
  rule:GATE                          KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['G1', 'G2']
  degrade:branch_over                KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['K6', 'K7']
  degrade:inline_over                KILLED     flipped   5 flips direct slot(s) of weight >= 3: ['K8']
  degrade:reopen_over                KILLED     flipped   5 flips direct slot(s) of weight >= 3: ['K14']
  degrade:back_over                  SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:else_over                  KILLED     flipped   3 flips direct slot(s) of weight >= 3: ['K3']
  degrade:filt_over                  SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:alias_over                 SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:gate_over                  SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:miss_branch                KILLED     flipped  15 flips direct slot(s) of weight >= 3: ['B1', 'B2', 'B3']
  degrade:miss_inline                KILLED     flipped  15 flips direct slot(s) of weight >= 3: ['I1', 'I4', 'I6']
  degrade:miss_reopen                KILLED     flipped  15 flips direct slot(s) of weight >= 3: ['R1', 'R4', 'R6']
  degrade:miss_back                  KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['K1B', 'K4B']
  degrade:miss_else                  KILLED     flipped  25 flips direct slot(s) of weight >= 3: ['E5', 'E6', 'E7', 'E1', 'E2']
  degrade:miss_filt                  KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['F1', 'F3']
  degrade:miss_alias                 KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['A1', 'A2']
  degrade:miss_gate                  KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['G1', 'G2']
  shards (consecutive slices of 14 records, 3 batches): 20 mutants {'KILLED': 15, 'EQUIVALENT': 4, 'SURVIVED': 1}
  intervention:rule:BRANCH           load-bearing    
  intervention:rule:INLINE           load-bearing    
  intervention:rule:REOPEN           load-bearing    
  intervention:rule:BACK             load-bearing    
  intervention:rule:ELSE             load-bearing    
  intervention:rule:FILT             load-bearing    
  intervention:rule:ALIAS            load-bearing    
  intervention:rule:GATE             load-bearing    
  intervention:degrade:branch_over   no-injected-records
  intervention:degrade:inline_over   no-injected-records
  intervention:degrade:reopen_over   no-injected-records
  intervention:degrade:back_over     no-injected-records
  intervention:degrade:else_over     no-injected-records
  intervention:degrade:filt_over     no-injected-records
  intervention:degrade:alias_over    no-injected-records
  intervention:degrade:gate_over     no-injected-records
  intervention:degrade:miss_branch   no-injected-records
  intervention:degrade:miss_inline   no-injected-records
  intervention:degrade:miss_reopen   no-injected-records
  intervention:degrade:miss_back     no-injected-records
  intervention:degrade:miss_else     no-injected-records
  intervention:degrade:miss_filt     no-injected-records
  intervention:degrade:miss_alias    no-injected-records
  intervention:degrade:miss_gate     no-injected-records
  geometry: U = 0.8927 (233/261) · L_max = 0.4215 over ['rule:BRANCH', 'rule:INLINE', 'rule:REOPEN', 'rule:BACK', 'rule:ELSE', 'rule:FILT', 'rule:ALIAS', 'rule:GATE']
    V3 cap 0.70: U PASS (needs > 0.30) · L_max OK
  dispositions: 0/48 recorded; missing ['rule:BRANCH', 'rule:INLINE', 'rule:REOPEN', 'rule:BACK', 'rule:ELSE', 'rule:FILT', 'rule:ALIAS', 'rule:GATE'] ...
```

```
TRAP LIVENESS · ADVISORY · UNCALIBRATED · lexical warnings, not proof · on the Season Pass backtests these are development fixtures, not validation
  hub 446ba45665ed73d2f06caca6963c6ffc · direct delegations 6 · rule placement: SKIP for every node: the mechanism_portfolio declares no A15 node
  T_BRANCH done_gap           -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_INLINE done_gap           breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_INLINE_PACK done_gap           breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_REOPEN superseding        -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_BACK superseding        -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_ELSE completion_elsewhe breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_BODY completion_elsewhe breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_REOPEN_TICKET superseding        breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_BACK_TICKET superseding        breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_FILT exact_predicate    -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_ALIAS_GIFT scope_alias        breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_ALIAS_STREAK scope_alias        breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_GATE effective_date     -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_PARK superseding        -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_SHARE authority          breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_FIELDS authority          breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_STATE stale_summary      breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  D_DDRULE distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  D_QMCARD distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  D_SKIP distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  D_ICONVFX distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  D_CANVAS distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  D_COINDM distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  D_432 distractor         breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  D_OLDINVITE distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  D_OLDBUILD distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  D_DDQUEUE distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  dispositions: 0/12 recorded
```

```
HARDNESS FORECAST · UNCALIBRATED · advisory · model claude-opus-5-5 · rev1 · model outputs, not measurements; the Season Pass backtests are development fixtures, not validation
  rule:BRANCH                                  family done_gap                                 Beta(3.0, 4.0) mean 0.43 n_eff 5.0 records 7
  rule:INLINE                                  family done_gap                                 Beta(3.0, 4.0) mean 0.43 n_eff 5.0 records 7
  rule:REOPEN                                  family superseding                              Beta(1.0, 6.0) mean 0.14 n_eff 5.0 records 12
  rule:BACK                                    family superseding                              Beta(1.0, 6.0) mean 0.14 n_eff 5.0 records 12
  rule:ELSE                                    family completion_elsewhere                     Beta(1.0, 5.0) mean 0.17 n_eff 4.0 records 4
  rule:FILT                                    family exact_predicate                          Beta(2.0, 5.0) mean 0.29 n_eff 5.0 records 6
  rule:ALIAS                                   family scope_alias                              Beta(1.0, 5.0) mean 0.17 n_eff 4.0 records 4
  rule:GATE                                    family authority                                Beta(1.0, 5.0) mean 0.17 n_eff 4.0 records 4
  independent whole    V3 E[avg] 0.828 [0.781, 0.874] P(all) 0.000
  independent shard:32 V3 E[avg] 0.850 [0.808, 0.891] P(all) 0.000
  independent shard:14 V3 E[avg] 0.876 [0.838, 0.911] P(all) 0.000
  independent slip     V3 E[avg] 0.892 [0.853, 0.927] P(all) 0.000
  independent batches  V3 E[avg] 0.871 [0.832, 0.907] P(all) 0.000
  source      whole    V3 E[avg] 0.828 [0.781, 0.874] P(all) 0.000
  source      shard:32 V3 E[avg] 0.850 [0.808, 0.891] P(all) 0.000
  source      shard:14 V3 E[avg] 0.876 [0.838, 0.911] P(all) 0.000
  source      slip     V3 E[avg] 0.892 [0.853, 0.927] P(all) 0.000
  source      batches  V3 E[avg] 0.871 [0.832, 0.907] P(all) 0.000
  correlated  whole    V3 E[avg] 0.828 [0.760, 0.894] P(all) 0.006
  correlated  shard:32 V3 E[avg] 0.851 [0.796, 0.901] P(all) 0.000
  correlated  shard:14 V3 E[avg] 0.877 [0.835, 0.917] P(all) 0.000
  correlated  slip     V3 E[avg] 0.893 [0.856, 0.927] P(all) 0.000
  correlated  batches  V3 E[avg] 0.872 [0.826, 0.915] P(all) 0.000
  V3: P(all four difficulty gates) 0.000-0.006 across scenarios; value of information (first scenario): ['rule:BRANCH', 'rule:INLINE', 'rule:REOPEN']
  channel CH-BRANCH (scale, member latent [declared], 3 member(s), member trials): e ~ Beta(1.0, 5.0) [ledger records, member trials (runs of a task share a design] · P(any of 3 fails) 0.375 integrated vs 0.421 plug-in · expected loss alone 0.0099 · UNCALIBRATED
  channel CH-INLINE (scale, member latent [declared], 3 member(s), member trials): e ~ Beta(1.0, 5.0) [ledger records, member trials (runs of a task share a design] · P(any of 3 fails) 0.375 integrated vs 0.421 plug-in · expected loss alone 0.0099 · UNCALIBRATED
  channel CH-REOPEN (scale, member latent [declared], 2 member(s), member trials): e ~ Beta(1.0, 6.0) [ledger records, member trials (runs of a task share a design] · P(any of 2 fails) 0.250 integrated vs 0.265 plug-in · expected loss alone 0.0074 · UNCALIBRATED
  channel CH-BACK (scale, member latent [declared], 2 member(s), member trials): e ~ Beta(1.0, 6.0) [ledger records, member trials (runs of a task share a design] · P(any of 2 fails) 0.250 integrated vs 0.265 plug-in · expected loss alone 0.0050 · UNCALIBRATED
  channel CH-ELSE (scale, member latent [declared], 5 member(s), member trials): e ~ Beta(1.0, 5.0) [ledger records, member trials (runs of a task share a design] · P(any of 5 fails) 0.500 integrated vs 0.598 plug-in · expected loss alone 0.0151 · UNCALIBRATED
  channel CH-FILT (scale, member latent [declared], 1 member(s), member trials): e ~ Beta(1.0, 2.0) [ledger records, member trials (runs of a task share a design] · P(any of 1 fails) 0.333 integrated vs 0.333 plug-in · expected loss alone 0.0126 · UNCALIBRATED
  channel CH-ALIAS (scale, member latent [declared (unit-free point)], 2 member(s)): e = 0.2 [OVERRIDE (disclosed, no ledger record): --channel-rate CH-AL] · P(any of 2 fails) 0.360 integrated vs 0.360 plug-in · expected loss alone 0.0075 · UNCALIBRATED · OVERRIDE
  channel CH-GATE (scale, member latent [declared], 6 member(s), member trials): e ~ Beta(1.0, 4.0) [ledger records, member trials (runs of a task share a design] · P(any of 6 fails) 0.600 integrated vs 0.738 plug-in · expected loss alone 0.0080 · UNCALIBRATED
  channel control:BRANCH (control, member latent [rate unit], 3 member(s), member trials): e ~ Beta(1.0, 6.0) [ledger records, member trials (runs of a task share a design] · P(any of 3 fails) 0.333 integrated vs 0.370 plug-in · expected loss alone 0.0057 · UNCALIBRATED
  channel control:INLINE (control, member latent [rate unit], 1 member(s), member trials): e ~ Beta(1.0, 6.0) [ledger records, member trials (runs of a task share a design] · P(any of 1 fails) 0.143 integrated vs 0.143 plug-in · expected loss alone 0.0030 · UNCALIBRATED
  channel control:REOPEN (control, member latent [rate unit], 2 member(s), member trials): e ~ Beta(1.0, 10.0) [ledger records, member trials (runs of a task share a design] · P(any of 2 fails) 0.167 integrated vs 0.174 plug-in · expected loss alone 0.0016 · UNCALIBRATED
  channel control:BACK (control, member latent [rate unit], 2 member(s), member trials): e ~ Beta(1.0, 10.0) [ledger records, member trials (runs of a task share a design] · P(any of 2 fails) 0.167 integrated vs 0.174 plug-in · expected loss alone 0.0000 · UNCALIBRATED
  channel control:ELSE (control, member latent [rate unit], 2 member(s), member trials): e ~ Beta(1.0, 5.0) [ledger records, member trials (runs of a task share a design] · P(any of 2 fails) 0.286 integrated vs 0.306 plug-in · expected loss alone 0.0018 · UNCALIBRATED
  channel control:ALIAS (control, member latent [rate unit], 2 member(s), member trials): e ~ Beta(1.0, 2.0) [ledger records, member trials (runs of a task share a design] · P(any of 2 fails) 0.500 integrated vs 0.556 plug-in · expected loss alone 0.0000 · UNCALIBRATED
  channel control:GATE (control, member latent [rate unit], 2 member(s), member trials): e ~ Beta(1.0, 5.0) [ledger records, member trials (runs of a task share a design] · P(any of 2 fails) 0.286 integrated vs 0.306 plug-in · expected loss alone 0.0000 · UNCALIBRATED
  channel control:FILT (control): UNPARAMETERIZED - no ledger record and no --channel-rate override: not simulated
  slots most at risk (independent whole; P(fail) / P(fails all six) - all-fail justification workload, never a block): B2 0.52/0.07, B1 0.52/0.06, B3 0.52/0.06, F1 0.52/0.08, F3 0.52/0.08, I1 0.52/0.06, I4 0.52/0.06, I6 0.52/0.06
wrote Task_Authoring/task_inputs/Working_Files/01c_Forecast.json
```

Forecast, read with care (UNCALIBRATED): this exact view cannot fail write-content slots, which hold most of the weight, so its E[avg] is the optimistic end; the scenario-stage design view (`plan/out/forecast.txt`) and the requester-target model (`plan/policy_model_output.txt`) model the declared mechanisms over every slot. Only the pre-check can say which is closer.

Geometry: U passes the V3 cap and L_max clears the margin; the composed view counts direct slots only, while much of the weight is in write-content slots.

### Changes made at this stage (and why)

- record ids (all elements): Slack channel/ts pointers to seeded messages became the messages' 32-hex row ids. the gate reads text and timestamps from SQL rows, and a Slack row is keyed by its id.
- companion records: added at implementation: a Hello! line before Brian's DM, Marcus's second line, two lines from Vincent to Calvin about his pass, a COMMENTED review row and a GitHub notification mail for each of Arthur's two inline comments, the #zombie-prs copies of the three GitHub comments, invitation mail copies in four other attendees' mailboxes, the card's create, first description and rename actions, and one or two notes on each of Vincent's 18 tickets. each follows a base habit read at this stage: Brian and Marcus write in short bursts; Calvin's mailbox already holds GitHub's mails for #472 and #475, including Arthur's approvals with no comment in them, so his inline comments are separate reviews with their own mails; the GitHub app copies every match3d comment to #zombie-prs; the tickets' comment surface is the per-ticket read the cohort declares.
- rev2 (after the platform /hardness FAIL 2 on rev1): Brian's note is cut back to plain definitions; the sentence that a later sighting ends a pass moved into Arthur's doc; Vincent's and Robert's come-backs are replies under their own older threads in #zombie-bugs; Robert's sighting on the older build Android #2006 is new; rows 18 and 34 carry a re-test before and after their fix merged. Design section 14 has the intake.

### Blind sweeps on this SQL

Two independent agents read only the SQL and the base through `tools/hg.py` (no design, manifest, solver or plan): a fork sweep that solved the task row by row (`plan/sweeps/fork_sweep_inj.md`) and a coherence sweep (`plan/sweeps/coherence_sweep_inj.md`). Dispositions:

| Finding | Source file | Disposition with evidence |
|---|---|---|
| Row 18: 'only the Collect & Win wait' could limit #472 to row 17 (blocking) | plan/sweeps/fork_sweep_inj.md | Fixed. harmonygames-Games/match3d#472#rc_1 now reads 'That one isn't in this diff, the two Collect & Win ones are', in the GitHub row, its #zombie-prs copy and its mail |
| Row 25: #465 says nothing about the boss arena tutorial replaying, and base chats put that work on Oliver's side (blocking) | plan/sweeps/fork_sweep_inj.md | Fixed. Row 25 is now a queued-tutorial report, which is what harmonygames-Games/match3d#465 says it fixes; Brian's note says the PR 'has to be merged, and if the review on it says a fix is not in there, it is not', so no reading of PR prose is asked for; the exclusions now name only things that are not on the sheet |
| Marcus's glow could be read as row 12 | plan/sweeps/fork_sweep_inj.md | Fixed. His second line in D05U73FNDDL says the animation itself is fine, it is just the glow |
| Leonard's card also named Daily Gift | plan/sweeps/fork_sweep_inj.md | Fixed. The card's description lists only the two areas; the Daily Gift remark moved to the note in the updated invitation, evt_342a813cb7765d4a6fce8d |
| Vincent said he opened tickets for the open ones while three open rows have none | plan/sweeps/fork_sweep_inj.md | Fixed. His line in D06UPGF5PQV now says the keys are in the sheet where he opened one |
| 'newer build' across jobs | plan/sweeps/fork_sweep_inj.md | Fixed. The note says 'on a build made after that one'; C05433XK267/1759263189.219529 is later than both re-test builds |
| Share list could leave Leonard out | plan/sweeps/fork_sweep_inj.md | Fixed. Brian's DM says 'everyone on the review invite, Leonard too' |
| Vincent 'waiting for a main build' although #1754 and #1757 existed (blocking) | plan/sweeps/coherence_sweep_inj.md | Fixed. His notes on ZOM-571, ZOM-576 and ZOM-581 now say 'Not re-tested yet'; C05433XK267/1759248081.891639 |
| Calvin's deck (23 Sep) said Collect & Win was already in the queue (blocking) | plan/sweeps/coherence_sweep_inj.md | Fixed. The slide says 'Collect & Win is next'; base D0770ET6WBW/1758730948.999939 |
| Arthur's comments predated his approvals though numbered after them | plan/sweeps/coherence_sweep_inj.md | Fixed. Both are posted after the approval and merge (15:53:40Z, 16:09:50Z), so rev_2 follows rev_1 on harmonygames-Games/match3d#472 and harmonygames-Games/match3d#475, and each PR's updated_at moves with it |
| Brian named the review before its card and invitation existed | plan/sweeps/coherence_sweep_inj.md | Fixed. His line is now 29 Sep 16:41Z, after the invitation; D0770ET6WBW |
| Arthur's two docs were two sentences each | plan/sweeps/coherence_sweep_inj.md | Fixed in part. Both carry a little more of his own working notes; f_6d0326fa006b136f1bbf82. No base record states another rule for ZM |
| Brian's note and DM are longer than his chat lines | plan/sweeps/coherence_sweep_inj.md | Accepted. A lead's instruction on his own ticket (ZOM-543 has a long description by him); the DM is preceded by his usual separate greeting. Splitting the anchor would spread the ask over records the prompt cannot name |
| Slack copy of Oliver's comment: the KB shows few human conversation comments on match3d | plan/sweeps/coherence_sweep_inj.md | Accepted. INT-01 says comments are copied and the base copies CodeRabbit's conversation comment on harmonygames-Games/match3d#473 (C093LEZGF6J/1759246877.582979) |
| ZOM-572 filed Todo after Oliver's comment | plan/sweeps/coherence_sweep_inj.md | Accepted as designed: Vincent files from his sheet; the note makes Oliver's line on harmonygames-Games/match3d#473 count |
| Minor format points: issue-comment number, card slug, createCard id, Julia's guest line, slide layout | plan/sweeps/coherence_sweep_inj.md | Fixed: number 3352803412 sits between the base neighbours; slug says thu-oct-2; the createCard id shares the card id's first 20 hex; the guest line uses her base token; slides are BLANK with TEXT_BOX elements. Not changed: mails keep no .ics attachment row and no phone block, as the archived tasks' accepted invitations do |
| Fork sweep totals | plan/sweeps/fork_sweep_inj.md | The independent solve gave 12 Passed, 6 Waiting on QA, 21 Waiting on a fix, 1 clear area, 6 on the review list, the same tickets for rows 11 and 20 (ZOM-556, ZOM-560), the same three state changes and the same share list as `solver/truth.json` |

### /injection Checks A–C walk

- Inventory: 129 INSERT, 11 UPDATE, 0 DELETE, no upserts; tables {'gdrive.drive_files': 6, 'gdocs.docs_documents': 3, 'gsheets.sheets_spreadsheets': 1, 'gsheets.sheets_sheets': 1, 'gslides.slides_presentations': 1, 'gslides.slides_pages': 4, 'gslides.slides_page_elements': 8, 'slack.slack_messages': 18, 'trello.trello_cards': 1, 'trello.trello_actions': 4, 'trello.trello_boards': 1, 'gcal.gcal_events': 6, 'gmail.gmail_threads': 10, 'gmail.gmail_messages': 12, 'github.github_reviews': 2, 'github.github_review_comments': 2, 'github.github_pull_requests': 2, 'github.github_pr_comments': 1, 'github.github_timeline_events': 1, 'linear.linear_issues': 23, 'linear.linear_comments': 33}.
- Check A (references and IDs): PASS: every channel, user, issue, PR, thread, calendar, board, list and folder resolves (base_check Check A); uniqueness over the full collections (1.F); ownership, membership and shares give Calvin reach (check-sql PASS).
- Check B (structure): PASS: sql_lint 0 errors; every *_json column is literal JSON; NOT NULL columns supplied; generated *_fts columns never written; camelCase Trello columns and "index" quoted.
- Check C (dates, parents, statuses, counts): PASS: every seeded timestamp is before 2025-10-01T00:00Z except the planned meeting's start and end; replies after their parents; four base parents' counters updated; In Validation tickets have started_at and no ticket is Done; the card's badges and dateLastActivity follow its actions; ZOM-543, ZOM-556 and ZOM-560 take their newest comment's time as updated_at.

### Touched-data census

See 'Touched-data census and coherence hazards' above: six hazard categories covered and SC-6, 7, 13, 14, 15, 16, 18, 19, 22, 38, 56, 57, 67, 68, 70 dispositioned.

### Counter-readings

| Category | Counter-reading (strongest argument it FAILS) | Evidence that resolves it | Verdict |
|---|---|---|---|
| Temporal | the sheet cites builds or PRs that did not exist when it was last saved | saved 2025-09-30T19:30:52Z; the newest build it cites is C05433XK267/1759257787.502039 (18:43Z) and the newest PR harmonygames-Games/match3d#475 (opened 15:59Z) | holds |
| Temporal | the later reports name a build that was not out yet | C05433XK267/1759263189.219529 finished 20:13Z; b156fdcd5fd89b8362d0e5fcf24975d1 is 21:20Z and a40824773b7cad9681d141b916a5f558 21:44Z, after an hour of play | holds |
| Temporal | tickets ZOM-567 and up are dated before the base's last ticket | ZOM-566 is 2025-09-30T16:26:02Z; ZOM-567 is 16:43Z and keys rise with time to ZOM-584 at 18:44Z | holds |
| Temporal | Brian's DM says Thursday's review while the invitation says Friday | the card and the updated invitation calvin.price@harmonygames.co/<calendar-f2b39cd5-884e-2def-a4d7-d41d80d4c55b@google.com> moved it to Thursday at 17:22Z to 17:24Z; the DM is 20:40Z | holds |
| Semantic / Category | a review meeting does not belong on a roadmap board's Backlog list | the list holds undated items Leonard keeps (cards 68c45c2bba569a224e81425d, 6851ab4165575ba2c16a6f05); Leonard runs this board alone (actions 68dc0eb3b933d6e0e75dad34) | holds |
| Semantic / Category | 'pass icon' means three things (the VFX remark, the restart, the glow) | the sheet row is the restart (ZOM-571), Marcus's report is the glow (806f4a67a847d4d47e3e5674760aa630), and Vincent's Sep 24 remark D06UPGF5PQV/1758721951.996909 is in his chat, which the note leaves out | holds |
| Cross-service Referential | Arthur's comments contradict the base approval mails, which show no comment | they are separate COMMENTED reviews (harmonygames-Games/match3d#472#rev_2, harmonygames-Games/match3d#475#rev_2) posted after the approvals and merges, each with its own mail in the same base thread | holds |
| Cross-service Referential | the PR bodies say the fix is in | harmonygames-Games/match3d#472's body and walkthrough name only the Collect & Win wait and the reward VFX flow; harmonygames-Games/match3d#475's name the tap prompt, the close sequence and the last pack, never sound | holds |
| Cross-service Referential | the Slack copies and the GitHub rows differ | each copy carries the comment's text with & written as &amp;, the PR's title and the author's real login, as base copies do | holds |
| Quantitative | the sheet's row count or the areas disagree with the note | 38 numbered rows; the note lists ten areas and every row's Area is one of them | holds |
| Quantitative | thread counters disagree after the seeded replies | four UPDATEs set reply_count, reply_users_count and latest_reply on the base parents | holds |
| State / Lifecycle | best argument the In Validation tickets are unintended: ZOM-571 and ZOM-581 say a fix is waiting for QA while the review says it is not in the PR | the state is Vincent's dated claim from what he was told (his note on each ticket says so); Arthur's review is the PR's own record, and the note says the review wins | holds (designed, T_INLINE, T_STATE) |
| State / Lifecycle | best argument the Todo on ZOM-572 is unintended: Oliver said the fix is merged an hour before Vincent filed it | Vincent files from his sheet and does not read GitHub; the note makes the dev's line on his merged PR count | holds (designed, T_ELSE) |
| State / Lifecycle | best argument rows 9 and 29 are unintended: the sheet says passed and a later message says it is back | each later message names a newer main build and is by the tester or a founder; the note's own sentence resolves it | holds (designed, T_REOPEN, T_BACK) |
| State / Lifecycle | best argument the 'ok, chat' rows are unintended: QA said ok and the dev considered it done | C05433XK267/1758817549.151639 is a branch build and f_6d0326fa006b136f1bbf82 says such a pass has to be done again after the merge; harmonygames-Games/match3d#465 merged later that day | holds (designed, T_BRANCH) |
| State / Lifecycle | best argument the two review lists are unintended: Brian says Daily Gift, the card says Level-end rewards | the card was changed a day after Brian's line by the review's organizer, the updated invitation says so, and Brian's later note defers to the card | holds (designed, T_GATE) |
| State / Lifecycle | Leonard ticked the Queue Manager card on Sep 30, so the epic is finished | the tick marks the feature as merged (68c453cd0ff184d95550bc58, 16:40Z); ZOM-543 is In Progress and Brian's DM, four hours later, asks for the stock-take | holds |
| Identifier / Format | the GitHub mail ids and review numbers are invented | they follow the base pattern and sit just under the approvals' numbers in the same threads | holds |
| Identifier / Format | Julia's invitation subject ends with a name token | base invitations in her mailbox end with ([PERSON_NAME_0043]) (threads/jlawson@harmonygames.co_1834845385842461999.json) | holds |
| People status | a seeded speaker had left or was away | activity.json: all nine seeded speakers are active_sep_2025_quiet_in_oct (1.C); no seeded record names Victor Barnes | holds |
| Other | the notes on Vincent's tickets read as filler | each is the per-ticket record Brian's note makes a reader check (whether a dev named a merged PR); two say a fix exists but no PR, which keeps those rows Waiting on a fix | holds |
| Other | Brian's note reads as a rubric | it is a lead's instruction on his own ticket in his words; it names no record's location, no build and no count | holds |

Unresolved: Whether Slack search indexes attachment text (the branch names in #builds, the #zombie-prs copies) is unverified until the pre-check. The under-60 % target rests on mechanisms whose landing rates are priors, not measurements (UNCALIBRATED). One directory listing of the mail export's thread file names was made outside `tools/hg.py` at this stage, to learn the naming; no record content was read that way and every fact was read through the helper. The fixes made after the two blind sweeps were not swept again.

```
STAGE GATE injection: PASS — Task_Authoring/task_inputs · 01_Universe_Inject.sql#479b8441f52e · 01_Hardness_Manifest.json#bffb088156a7 · 01_Grounding_Dossier.md#88526f435b5f · solver/solver.py#337c6a63f446 · 01c_Dispositions.json#818f309bd758 · 01c_Preflight_Report.json#6bb345bafeb1 · 00_Assigments.md#a8cc00ce24ff · 01_Scenario_Design.md#cd79a4e0e490 · 01_Hardness_Manifest.draft.json#b79d491b46aa · 01_Gradable_Surface.json#e2392bcc269e · __context__#7be566a0936c · __assignment__#d644f7ef43f6 · __policy__#dc4ab5df3cdd · __gate_policy__#5b7d4d20094d · __review__#e8f09c674b67 · blocking 0 · warnings 1 · checks 42
[PASS] assignment.v3_context: Calvin Price / Game Engineer (Unity VFX); hard cap <70%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 6 output(s) present: 01_Universe_Inject.sql, 01_Hardness_Manifest.json, 01_Grounding_Dossier.md, solver/solver.py, 01c_Dispositions.json, 01c_Preflight_Report.json
[PASS] structure.inputs: 4 input(s) present: 00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json)
[PASS] chain.scenario: upstream 'scenario' PASS pasted and current (01_Scenario_Design.md#cd79a4e0e490, 01_Hardness_Manifest.draft.json#b79d491b46aa, 01_Gradable_Surface.json#e2392bcc269e, 00_Assigments.md#a8cc00ce24ff, __context__#7be566a0936c, __assignment__#d644f7ef43f6, __policy__#dc4ab5df3cdd, __gate_policy__#071e93f4073b, __review__#773c40d918b0)
[PASS] structure.sections: 17 required sections present and non-empty (01_Grounding_Dossier.md)
[PASS] structure.placeholders: no placeholders in 01_Grounding_Dossier.md
[PASS] evidence.entity: 13/13 items carry a source pointer (min 90%)
[PASS] evidence.keyword: 11/11 items carry a source pointer (min 100%)
[PASS] evidence.persona_reach: 11/11 items carry a source pointer (min 100%)
[PASS] evidence.record_ledger: 140/140 items carry a source pointer (min 100%)
[PASS] evidence.facts_for_human: 36/36 items carry a source pointer (min 100%)
[PASS] tool.sql_lint: sql_lint re-run matches the paste: errors 0, warnings 12, rows 140
[PASS] tool.injection_lint: hg.py lint: 0 FAIL, 0 CHECK dispositioned, 0 INFO; sha256 479b8441f52e matches 01_Universe_Inject.sql
[PASS] review.warning_dispositions: every sql_lint warning class dispositioned (clock×12)
[PASS] tool.base_check: base_check pasted PASS; re-run PASS
[PASS] tool.base_claims: base_claims pasted PASS; re-run PASS
[PASS] tool.hardness_gate: hardness_gate (SQL) pasted PASS; re-run PASS
[PASS] structure.design_delta: final manifest keeps all 67 draft ids
[PASS] structure.preflight: 01c_Preflight_Report.json bound by sha256 to the current SQL, solver, surface, manifest and dispositions
[PASS] solver.contract: solver contract re-run PASS
[PASS] mutation.dispositions: 48 mutation and intervention results each carry a written disposition (01c_Dispositions.json)
[PASS] geometry.upper_bound: U 0.893 (233/261) vs 1 - cap 0.30 (V3 hard): PASS (bound PASS); re-run U 0.893 PASS (bound PASS)
[PASS] geometry.margin: L_max 0.421455938697318 vs (1 - cap) + 0.10: OK (advisory: the margin is a judgment, not a proof)
[PASS] liveness.dispositions: every liveness flag dispositioned (12 flag(s))
[WARN] forecast.preregistered: forecast recorded: pre-register it with tools/hardness_forecast.py --preregister before the platform run (advisory)
[PASS] tool.check_sql_pasted: persona_view check-sql --load-bearing output pasted with verdict PASS
[PASS] reach.injection: 26 scoped load-bearing ids YES for calvin_price
[PASS] structure.facts_declared: manifest declares 10 load-bearing fact(s) in `facts`
[PASS] tool.fact_check: fact_check --no-leak pasted PASS; re-run PASS
[PASS] kb.coherence_hazards: coherence audit cites 22 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 9 seeded speakers each cited with activity.json status; conventions.json cited
[PASS] kb.integrations: companions listed per integrations.json (12 INT ids, services ['gcal', 'gdocs', 'gdrive', 'github', 'gmail', 'gsheets', 'gslides', 'linear', 'slack', 'trello'])
[PASS] boundary.anchor_naming: 4 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 15 evidenced counter-readings (of 23 found; need ≥ 15) in 01_Grounding_Dossier.md
[PASS] review.coverage: self-review addresses all 9 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] readiness.context: explicit task/revision and current upstream evidence verified
[PASS] readiness.hardness_review: current evidenced review; deferred: []
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

