# Grounding Dossier — Owen Baker · DD bug carry-over into Linear · injection rev9 · contains no prompt, OE or criterion text

SQL: `task_inputs/01_Universe_Inject.sql` (sha ea5b542897c8), stored byte for byte in `Working_Files/run_forensics/rev9/01_Universe_Inject.sql`. rev1 to rev8 stay in `run_forensics/` with their platform reports. 149 INSERT, 39 UPDATE, no DELETE. Universe: normal, clock 2026-02-14 00:00 UTC. Persona: Owen Baker <owen.baker@harmonygames.co>, Game Engineer (Unity).

## 1.A Structural

| Table | NOT NULL columns supplied (live schema) | Base location · sample ids | Format notes |
|---|---|---|---|
| slack.slack_messages | id, ts, channel_id, type, text, reply_count, reply_users_count, is_activity_message, reactions_json, files_json, attachments_json, created_at, metadata_json | slack messages/CE156FDFB428/2025-11.json (root 1bc1434b15a44cec9044db1b59ae4995); messages/C050WGU41HR/2025-11.json | id = sha256(channel\|ts)[:32]; a reply sets thread_parent_id to the root's id and thread_ts_legacy to its ts; each root's counters are updated |
| gmail.gmail_threads / gmail_messages | id, user_email; id, thread_id, user_email | owen.baker@harmonygames.co/1849333980856689601 | thread id = mailbox plus a numeric id; message id = mailbox plus the RFC Message-ID; Owen's copies are INBOX, Vincent's SENT; invitation mails follow INT-11 |
| gdrive.drive_files · gdocs.docs_documents · gsheets.sheets_spreadsheets / sheets_sheets · gslides.slides_presentations / pages / page_elements | id, name, mime_type; document_id, title; spreadsheet_id, title; spreadsheet_id, sheet_id, title; presentation_id, title; presentation_id, object_id; presentation_id, page_object_id, object_id | Drive roots d_4e13bd40cc73d0fc76f87c, d_cc3e90160f490686039986, d_fc22d5941b2aeb5c03ad32 | the file id is the same in Drive and in Docs, Sheets or Slides, with identical sharing; f_ + 22 hex; folder d_9b41e7c2a05d36f8e1c7a4 |
| gcal.gcal_events | event_id, calendar_id | evt_6e2c91d4b07f3a58c1d2e4 (Owen's copy) | one row per attendee calendar with its own event id, shared ical_uid, self:true on the owner's copy; Sun Feb 15 17:00–17:30Z is a not-yet-happened event |
| trello.trello_cards / trello_actions / trello_checklists / trello_check_items | id, name, idBoard, idList; id, type, date; id, name, idCard, idBoard; id, name, idChecklist | boards 65eb4ec525346c8070ca638f and 6851a6569f3bf818760632ab | ids: first 8 hex = Unix seconds; badges_json in the full base shape with comments 1 and the checklist's 28 items, 27 complete; idShort 211 and 80 are the next free numbers |
| github.github_pr_comments / github_review_comments / github_timeline_events | id, pr_id; id, pr_id, seq; id, pr_id, event | harmonygames-Games/GameOfDominoes#1905 | next free #c_, #ev_ and #rc_ suffixes; each PR comment has a 'commented' event and an INT-01 copy; each inline comment belongs to the PR's #rev_1 approval and follows it by three seconds |
| linear.linear_comments / linear_issues | id, issue_id, author_id, body, is_edited, created_at, updated_at; UPDATE of updated_at only | ENG-2401, ENG-2417 | comment_ + 32 hex; dates YYYY-MM-DDTHH:MM:SSZ; issue updated_at follows the newest comment; base Linear has no comments (NB-24) |

## 1.B Entity

| Entity | Spelling used | Where it appears (cited) | Agreement |
|---|---|---|---|
| Owen Baker | owen.baker@harmonygames.co · EMPLOYEE_0021_SLACK_ID · usr_4e13bd40cc73d0fc · PERSON_5877_GITHUB_USERNAME | D05S1S2AB5M/1770937805.214409; harmonygames-Games/GameOfDominoes#1905; Drive root d_4e13bd40cc73d0fc76f87c | AGREE |
| Arthur Blake | arthur.blake@harmonygames.co · EMPLOYEE_0025_SLACK_ID · usr_cc3e90160f490686 · EMPLOYEE_0025_GITHUB_USERNAME | CE156FDFB428/1763394823.486369 thread; harmonygames-Games/GameOfDominoes#1905#rev_1; hub D05S1S2AB5M/1770937805.214409 | AGREE |
| Brian Foster | brian.foster@harmonygames.co · EMPLOYEE_0026_SLACK_ID · usr_fc22d5941b2aeb5c · PERSON_0180_GITHUB_USERNAME · d1cd0fef645a6c978ae1f068 | D07E9PSQB6W/1765206644.602119; C05V5FNLB9V/1766415326.501939; harmonygames-Games/GameOfDominoes#1898 | AGREE |
| Vincent Parker | vincent.parker@harmonygames.co · EMPLOYEE_0012_SLACK_ID · usr_65c76e0b87aa7e9b | CE156FDFB428/1763394823.486369; mail owen.baker@harmonygames.co/1849333980856689601 | AGREE |
| Marcus Bennett | marcus.bennett@harmonygames.co · EMPLOYEE_0002_SLACK_ID | C05V5FNLB9V/1764256187.655299; D05USBTQY1F/1765452012.418229; harmonygames-Games/GameOfDominoes#1913 (PERSON_0396_GITHUB_USERNAME) | AGREE |
| Oliver Brooks | oliver.brooks@harmonygames.co · EMPLOYEE_0003_SLACK_ID · usr_bdf01b53c6a92c5e | ENG-2428; #builds C05433XK267 #2200 | AGREE |
| Robert | robert@harmonygames.co · EMPLOYEE_0016_SLACK_ID | C09Q4S613CN/1764042435.541279; evt_6e2c91d4b07f3a58c1d2e4 | AGREE |
| Leonard Hayes | leonard.hayes@harmonygames.co | C09SWTHEMEW/1770926214.816149 | AGREE |
| Domino Delights | DD; repo GameOfDominoes | ENG-2401; harmonygames-Games/GameOfDominoes#1905 | AGREE |
| Android canvas comment channel | Vincent's Android canvas; channel FC:F09GAFM2DRR:Bugs on Android 2231 | CE156FDFB428/1763041126.468099 | AGREE |
| #god-bugs | the bug channel | C05V5FNLB9V/1764256187.655299 | AGREE |
| Win & Collect | Win & Collect in Slack; 'Collect&win - Magical Wings' on the ticket | C9CA62B5180A/1765927876.696389; ENG-2424 | AGREE (two names, one feature; the rule doc says neither) |
| Nate's Treasure | Nate's Treasure / Nathan's Treasure; '[PERSON_NAME_1711]' in the canvas | ENG-2425; CE156FDFB428/1763131864.808869 | AGREE (anonymized token) |
| BoomBit | BoomBit (publisher of the public build) | C09SWTHEMEW/1764659626.614679 | AGREE |

## 1.C Voice and realism

Seeded speakers, each with its activity.json (normal KB) status at the clock:
- Arthur Blake (arthur.blake@harmonygames.co, EMPLOYEE_0025_SLACK_ID) — activity.json status_at_clock active_feb_2026; seeds the hub D05S1S2AB5M/1770937805.214409 (Feb 12 23:10Z), the rule doc f_3ca9e15d7b20f4e681ad52, the ENG-2401 note, the inline comments, the triage notes and the review invite.
- Brian Foster (brian.foster@harmonygames.co, EMPLOYEE_0026_SLACK_ID) — activity.json status_at_clock active_feb_2026; seeds his three check notes, the Trello checklist, C09Q4S613CN/1764606918.318209, D07E9PSQB6W/1765206644.602119, C05V5FNLB9V/1767021345.207719, the Trello comments and the tracker and deck, all dated Sep–Dec 2025.
- Vincent Parker (vincent.parker@harmonygames.co, EMPLOYEE_0012_SLACK_ID) — activity.json status_at_clock quiet_since_2025-12; every seed is dated by Nov 22, 2025, before his last Slack post on Nov 23. Base shows him posting at weekends, so the Nov 22 replies fit.
- Marcus Bennett (marcus.bennett@harmonygames.co, EMPLOYEE_0002_SLACK_ID) — activity.json status_at_clock active_feb_2026; seeds D05USBTQY1F/1765452012.418229 and one reply under C05V5FNLB9V/1764256187.655299.
- Oliver Brooks (oliver.brooks@harmonygames.co, EMPLOYEE_0003_SLACK_ID) — activity.json status_at_clock active_feb_2026; seeds the ENG-2428 note, dated Dec 5.
- Owen Baker (owen.baker@harmonygames.co, EMPLOYEE_0021_SLACK_ID) — activity.json status_at_clock active_feb_2026; the persona; seeds his own PR comments of November 2025, four channel_leave rows of Feb 11 and six channel_join rows of Feb 12.
- Robert (robert@harmonygames.co, EMPLOYEE_0016_SLACK_ID) — activity.json status_at_clock active_feb_2026; seeds one reply, C09Q4S613CN/1766164222.418229, under his own Nov 24 report.
- Bots: the GitHub app SLACK_BOT_0004_SLACK_ID posts the INT-01 copies in C050WGU41HR.

Lengths and hours from conventions.json (normal KB): Slack replies in the canvas channel are one line, like Vincent's base 'yep' and 'still cannot sign in'; Brian's notes are short and plain. The hub is long for an im message, in the tail like Arthur's base requests. Voice from real messages: Vincent writes terse fragments (CE156FDFB428/1763394823.486369 thread), Brian says 'I send the fix' (CE156FDFB428/1763642881.891429) and Arthur writes 'Done' and 'fixed'. Seeds state claims and evidence, never conclusions.

## 1.D Keyword

| Term | Hits / pointer | Note |
|---|---|---|
| "2231" | base channel name FC:F09GAFM2DRR:Bugs on Android 2231 (CE156FDFB428/1763041126.468099); seeded comment_49b5ac4788465f72ddf245e34f2b7034 | the title prefix comes only from the ENG-2401 note |
| "0.3.310" | seeded f_3ca9e15d7b20f4e681ad52; base D04UGG61DUM/1770846601.876869 is a DM Owen cannot see | the rule doc is the authority for the build; no review version is joined to it (NB-21) |
| "how-to-play" | seeded harmonygames-Games/GameOfDominoes#1905#rc_1 and its INT-01 copy in C050WGU41HR | absent from Linear and the deck |
| "info popup" | seeded harmonygames-Games/GameOfDominoes#1908#rc_1 and its INT-01 copy in C050WGU41HR | absent from Linear and the deck |
| "round icons" | seeded C09Q4S613CN/1764606918.318209 (row e48eb03d633e480ea6f7cddea576ef4c) | the correction avoids the canvas wording 'circular shapes' |
| "Tavern" | base CE156FDFB428/1763642831.967359; seeded D05USBTQY1F/1765452012.418229 (row 91be79cc8e72189a592762c24c531925) | a Tavern search of DMs finds Marcus's note, so BACK is rated about half |
| "lives" | base CE156FDFB428/1763548856.943389, C09SWTHEMEW/1764659626.614679, f_948768f5a462e7037d17c9; ENG-2277, ENG-2400 | the removal reads across a channel and a doc |
| "reward track" | seeded comment_d6aee2099bd71050facc422ccef8f809 on ENG-2428 | one record |
| "carry-over" | seeded D05S1S2AB5M/1770937805.214409, f_3ca9e15d7b20f4e681ad52, d_9b41e7c2a05d36f8e1c7a4, comment_49b5ac4788465f72ddf245e34f2b7034 | the task's own word; no correction carries it except the ENG-2401 note the rule doc points at |
| "close these UI tickets" | seeded 690b29bc3c7d2e51b0f86a47 on card 690b27282f4c1b7a6e93d512 | NEW TERM: the rule doc points at it by role |

## 1.E Persona reach

Load-bearing scoped ids (seeded and base) are in `Working_Files/plan/load_bearing_ids.txt` (33 ids; Linear, GitHub and Trello are unscoped).

| Load-bearing record | Reach |
|---|---|
| 488d87e2e651cc1fb00c034bd6df5a4a | Owen is in the DM D05S1S2AB5M |
| 91be79cc8e72189a592762c24c531925 | Owen is in the DM D05USBTQY1F |
| 9bf944b8fcadea7bd8010fccf1baee22 | Owen is in the DM D07E9PSQB6W |
| e48eb03d633e480ea6f7cddea576ef4c | Owen is in C09Q4S613CN |
| f_3ca9e15d7b20f4e681ad52 | shared with Owen |
| d_9b41e7c2a05d36f8e1c7a4 | Owen owns it |
| evt_6e2c91d4b07f3a58c1d2e4 | on Owen's calendar |
| owen.baker@harmonygames.co/<CAK0a68e5711011904665cac8fb31fa@mail.gmail.com> | in Owen's mailbox |
| C9CA62B5180A/1765927876.696389 | Owen is in the mpim |
| f_948768f5a462e7037d17c9 | shared with Owen |

Output verbatim:

```
CHECK-SQL as owen_baker <owen.baker@harmonygames.co>
[YES LB] L3 gdrive.drive_files insert d_9b41e7c2a05d36f8e1c7a4 - persona owns the file
[YES LB] L6 gdrive.drive_files insert f_3ca9e15d7b20f4e681ad52 - file is shared with the persona (shared_with_emails)
[YES LB] L8 gdrive.drive_files insert f_72e0b4c3d91a5f68c2b7e4 - file is shared with the persona (shared_with_emails)
[YES LB] L10 gdrive.drive_files insert f_d15a8c70e3f2b94a61c8d3 - file is shared with the persona (shared_with_emails)
[YES] L12 gdrive.drive_files insert f_a9ba8abc7d5189babcb378 - file is shared with the persona (shared_with_emails)
[YES LB] L14 gdocs.docs_documents insert f_3ca9e15d7b20f4e681ad52 - file is shared with the persona (shared_with_emails)
[YES LB] L17 gdocs.docs_documents insert f_72e0b4c3d91a5f68c2b7e4 - file is shared with the persona (shared_with_emails)
[YES] L19 gsheets.sheets_spreadsheets insert f_a9ba8abc7d5189babcb378 - file is shared with the persona (shared_with_emails)
[YES] L22 gsheets.sheets_sheets insert f_a9ba8abc7d5189babcb378, f_a9ba8abc7d5189babcb378#0 - file is shared with the persona (shared_with_emails)
[YES] L24 gsheets.sheets_sheets insert f_a9ba8abc7d5189babcb378, f_a9ba8abc7d5189babcb378#1 - file is shared with the persona (shared_with_emails)
[YES] L26 gsheets.sheets_sheets insert f_a9ba8abc7d5189babcb378, f_a9ba8abc7d5189babcb378#2 - file is shared with the persona (shared_with_emails)
[YES LB] L28 gslides.slides_presentations insert f_d15a8c70e3f2b94a61c8d3 - file is shared with the persona (shared_with_emails)
[YES LB] L31 gslides.slides_pages insert f_d15a8c70e3f2b94a61c8d3, slide_3909e5a6ee5d - file is shared with the persona (shared_with_emails)
[YES LB] L33 gslides.slides_page_elements insert f_d15a8c70e3f2b94a61c8d3, el_7a0cc6e334c7, slide_3909e5a6ee5d - file is shared with the persona (shared_with_emails)
[YES LB] L35 gslides.slides_page_elements insert f_d15a8c70e3f2b94a61c8d3, el_acdf419923e2, slide_3909e5a6ee5d - file is shared with the persona (shared_with_emails)
[YES LB] L37 gslides.slides_pages insert f_d15a8c70e3f2b94a61c8d3, slide_9a3166f65540 - file is shared with the persona (shared_with_emails)
[YES LB] L39 gslides.slides_page_elements insert f_d15a8c70e3f2b94a61c8d3, el_744603c9bb36, slide_9a3166f65540 - file is shared with the persona (shared_with_emails)
[YES LB] L41 gslides.slides_page_elements insert f_d15a8c70e3f2b94a61c8d3, el_a919e44eebf8, slide_9a3166f65540 - file is shared with the persona (shared_with_emails)
[YES LB] L43 gslides.slides_pages insert f_d15a8c70e3f2b94a61c8d3, slide_576c1961540d - file is shared with the persona (shared_with_emails)
[YES LB] L45 gslides.slides_page_elements insert f_d15a8c70e3f2b94a61c8d3, el_9aa0ecc95eb0, slide_576c1961540d - file is shared with the persona (shared_with_emails)
[YES LB] L47 gslides.slides_page_elements insert f_d15a8c70e3f2b94a61c8d3, el_63dd9d735227, slide_576c1961540d - file is shared with the persona (shared_with_emails)
[YES LB] L49 gslides.slides_pages insert f_d15a8c70e3f2b94a61c8d3, slide_96f5a36798d7 - file is shared with the persona (shared_with_emails)
[YES LB] L51 gslides.slides_page_elements insert f_d15a8c70e3f2b94a61c8d3, el_2dbbbf8866f4, slide_96f5a36798d7 - file is shared with the persona (shared_with_emails)
[YES LB] L53 gslides.slides_page_elements insert f_d15a8c70e3f2b94a61c8d3, el_c3be9007cc73, slide_96f5a36798d7 - file is shared with the persona (shared_with_emails)
[YES LB] L55 slack.slack_messages insert 488d87e2e651cc1fb00c034bd6df5a4a, D05S1S2AB5M/1770937805.214409 - persona EMPLOYEE_0021_SLACK_ID is in members of im D05S1S2AB5M
[YES LB] L58 slack.slack_messages insert 91be79cc8e72189a592762c24c531925, D05USBTQY1F/1765452012.418229 - persona EMPLOYEE_0021_SLACK_ID is in members of im D05USBTQY1F
[YES LB] L60 slack.slack_messages insert 9bf944b8fcadea7bd8010fccf1baee22, D07E9PSQB6W/1765206644.602119 - persona EMPLOYEE_0021_SLACK_ID is in members of im D07E9PSQB6W
[YES LB] L62 slack.slack_messages insert 2ea7c02c6ddb99bc9b37f680be4159a6, D07E9PSQB6W/1765471563.704419 - persona EMPLOYEE_0021_SLACK_ID is in members of im D07E9PSQB6W
[YES LB] L64 slack.slack_messages insert 2f3add0dcfc251b7e92cd216af7352e2, D07E9PSQB6W/1765471651.208713 - persona EMPLOYEE_0021_SLACK_ID is in members of im D07E9PSQB6W
[YES LB] L66 slack.slack_messages insert e48eb03d633e480ea6f7cddea576ef4c, C09Q4S613CN/1764606918.318209 - persona EMPLOYEE_0021_SLACK_ID is in members of public dd-road-to-sub-250mb
[YES LB] L68 slack.slack_messages insert d49c24581dc7a16427b92fda3de0b8b5, C05V5FNLB9V/1767021345.207719 - persona EMPLOYEE_0021_SLACK_ID is in members of private god-bugs
[YES LB] L70 slack.slack_messages insert 70692cd00e9483ddce075a18d43e1f4c, C09Q4S613CN/1766164222.418229 - persona EMPLOYEE_0021_SLACK_ID is in members of public dd-road-to-sub-250mb
[YES LB] L72 slack.slack_messages insert e7fe05ca83bdb700b0acd4cc054e5a38, CE156FDFB428/1763845212.507119 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES LB] L74 slack.slack_messages insert 42460650faeb4109764ba2c092b43578, CE156FDFB428/1763742012.611229 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES LB] L76 slack.slack_messages insert 2acc689f598cf1569e4b7d3b911782c3, CE156FDFB428/1763845812.703339 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES LB] L78 slack.slack_messages insert 5fe8e6e599e4e03de80e8a079c05e796, CE156FDFB428/1763845872.804449 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES LB] L80 slack.slack_messages insert 948d64b2f42b443b0e509a0c66a03e3c, CE156FDFB428/1763845512.559339 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES] L82 slack.slack_messages insert e3e5bf78e3fdfac0af10bd701a6e7a3f, CE156FDFB428/1770842472.100349 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES] L84 slack.slack_messages insert d38307a8374e099be59b05f2b9cfbb0b, C09Q4S613CN/1770842473.458979 - persona EMPLOYEE_0021_SLACK_ID is in members of public dd-road-to-sub-250mb
[YES] L86 slack.slack_messages insert 0cc44f9deecc40e15421630ef480ec3e, C05433XK267/1770842474.718529 - persona EMPLOYEE_0021_SLACK_ID is in members of public builds
[YES] L88 slack.slack_messages insert 186107ee50a7626bc73d0fa44fc318d9, C09SWTHEMEW/1770842475.449099 - persona EMPLOYEE_0021_SLACK_ID is in members of private publishing-ext-[SOURCE_ORG_0001]-nbp7547
[YES] L90 slack.slack_messages insert c399a0bd2507460c5f14d0ff1b5c00a1, C05V5FNLB9V/1770936063.680719 - persona EMPLOYEE_0021_SLACK_ID is in members of private god-bugs
[YES] L92 slack.slack_messages insert b8b079a1305da1183e10f2214c040662, CE156FDFB428/1770936087.049309 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES] L94 slack.slack_messages insert 300958649de97d10a627b1b1b540f733, C09Q4S613CN/1770936109.066419 - persona EMPLOYEE_0021_SLACK_ID is in members of public dd-road-to-sub-250mb
[YES] L96 slack.slack_messages insert a93fda6f707471cbf829bf12f3d9fbfd, C05433XK267/1770936132.102479 - persona EMPLOYEE_0021_SLACK_ID is in members of public builds
[YES] L98 slack.slack_messages insert ef892f6ec08e170ab2f1ab0b5fb06ae0, C09SWTHEMEW/1770936156.410649 - persona EMPLOYEE_0021_SLACK_ID is in members of private publishing-ext-[SOURCE_ORG_0001]-nbp7547
[YES] L100 slack.slack_messages insert 8b1af0fccdb891a201c8e71576334165, C050WGU41HR/1770936178.946639 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L102 slack.slack_messages insert 1ccf4d6672818c4603f63b50df215c40, CE156FDFB428/1763738404.458929 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES] L104 slack.slack_messages insert 8240272f0daced8794805dcb1370898d, CE156FDFB428/1763738911.308829 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES] L106 slack.slack_messages insert ea0a6b8a9df6ae9a57508359e1f626dc, CE156FDFB428/1763739192.201719 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES] L108 slack.slack_messages insert 063efe55f310099cb2885d3f89dc674c, CE156FDFB428/1763739347.318979 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES] L110 slack.slack_messages insert d9ee1b377378db22c3a5fa25ed7ed369, CE156FDFB428/1763739440.491349 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES] L112 slack.slack_messages insert 2c76e59284ba24eeac1eed057f285198, CE156FDFB428/1763739605.860489 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES] L114 slack.slack_messages insert 87dc850c774ea6c22e67bdd7e8bfc7a7, C05V5FNLB9V/1764331830.705279 - persona EMPLOYEE_0021_SLACK_ID is in members of private god-bugs
[YES] L116 slack.slack_messages insert c520e100fdab72168d8d753e54ce4e5a, C050WGU41HR/1763073612.651219 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L118 slack.slack_messages insert 6bdb1aa52765811abb84fb47588ac89a, C050WGU41HR/1763407241.925879 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L120 slack.slack_messages insert f846da322aa89c0993ccd928c8c8c331, C050WGU41HR/1763494329.962479 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L122 slack.slack_messages insert a84f06fbe074112fbc0fbdd64bd2e092, C050WGU41HR/1763496333.386579 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L124 slack.slack_messages insert 1485803a59f9a37f9b1d841dfafc40bb, C050WGU41HR/1763505318.248159 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L126 slack.slack_messages insert 6571cffd875d0513c370930a17b3778a, C050WGU41HR/1763527947.637599 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L128 slack.slack_messages insert ee92520b49534bb87581e554df7d5060, C050WGU41HR/1763586644.212819 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L130 slack.slack_messages insert 7b71b1c0edfe1af5dad899d9372a628a, C050WGU41HR/1763593926.596469 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L132 slack.slack_messages insert fdab15395088ad4ce51cd08088e60b3a, C050WGU41HR/1766187602.932159 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L134 slack.slack_messages insert 3a57ea1dc5504199cb61300a37c4c1d1, C050WGU41HR/1766775029.801269 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L136 slack.slack_messages insert ea8f1a2d0abb0e0b521418e4db6d94d2, C050WGU41HR/1763557535.436659 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L138 slack.slack_messages insert 52eafc2b8f3d50523ffccf60b77fc613, C050WGU41HR/1763603515.121629 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L140 slack.slack_messages update 37dc1365297989005c98ca1012808d6e, C09Q4S613CN/1764042435.541279 - persona EMPLOYEE_0021_SLACK_ID is in members of public dd-road-to-sub-250mb
[YES LB] L141 slack.slack_messages update d25dd8d11d9e1c1df11c941262bfa31b, C05V5FNLB9V/1766415326.501939 - persona EMPLOYEE_0021_SLACK_ID is in members of private god-bugs
[YES] L142 slack.slack_messages update 15e314b25f7d69d8077e073e622baefa, C09Q4S613CN/1764013100.931229 - persona EMPLOYEE_0021_SLACK_ID is in members of public dd-road-to-sub-250mb
[YES] L143 slack.slack_messages update 1bc1434b15a44cec9044db1b59ae4995, CE156FDFB428/1763394823.486369 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES] L144 slack.slack_messages update f0d28e20be9cdbbd03c6b0fb69f916c0, CE156FDFB428/1763549817.580759 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES] L145 slack.slack_messages update a31a43de27e340995e378e372149c179, CE156FDFB428/1763548856.943389 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES] L146 slack.slack_messages update 55a5f61fae9f04f5fa5d4f29819ea0e2, CE156FDFB428/1763642552.651279 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES] L147 slack.slack_messages update ef80c659e26c08225ceeb4f7a9f97d42, CE156FDFB428/1763394941.178509 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES] L148 slack.slack_messages update 3f6d03da9f66de3c25c4958a260c712c, CE156FDFB428/1763394616.234099 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES] L149 slack.slack_messages update 24f623d4fbac205ae65b0777ccabbc72, CE156FDFB428/1763394911.691209 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES] L150 slack.slack_messages update c4d52c84291fad8d0b269704b231b736, CE156FDFB428/1763643072.577249 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES] L151 slack.slack_messages update cac88241bed9b8ca23f059664a775ebf, CE156FDFB428/1763643032.027129 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES] L152 slack.slack_messages update cd1ddb4d235967b5f5a3071356f8fc76, CE156FDFB428/1763549271.970799 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES] L153 slack.slack_messages update 48ec84642fb79215d0c7409b2a9ed199, CE156FDFB428/1763642881.891429 - persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES LB] L154 slack.slack_messages update a9665999506d442b1809e58261cd1f9d, C05V5FNLB9V/1764256187.655299 - persona EMPLOYEE_0021_SLACK_ID is in members of private god-bugs
[YES] L155 slack.slack_messages update dfb3bc5e2d7d43ee4af72061aa1efb88, C050WGU41HR/1763072479.270789 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L156 slack.slack_messages update e080921ea3d8541de55bdd3f6c672c22, C050WGU41HR/1763406238.439879 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L157 slack.slack_messages update 3fd15aec984400ecb1b011298da3af1f, C050WGU41HR/1763493332.244939 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L158 slack.slack_messages update 74369ca47c39d84359bcc5bab882ce14, C050WGU41HR/1763495409.791699 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L159 slack.slack_messages update 1b9deda51503ae9114973759ccf17b91, C050WGU41HR/1763504544.082819 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L160 slack.slack_messages update 50de5b6fe965e395aa422f6c03e43d0f, C050WGU41HR/1763527217.342039 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L161 slack.slack_messages update 2d723769e248e00040c52f788e054d8c, C050WGU41HR/1763585563.536669 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L162 slack.slack_messages update d109a8676777081d8ac8410f19eaac5e, C050WGU41HR/1763593226.132859 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L163 slack.slack_messages update faaefaacbfbe94421efdc365b484bb76, C050WGU41HR/1766185637.825279 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L164 slack.slack_messages update f36b509907752654e7111983a698e9bd, C050WGU41HR/1766769663.892649 - persona EMPLOYEE_0021_SLACK_ID is in members of private engineering-bots
[YES] L281 gmail.gmail_threads insert owen.baker@harmonygames.co/1849333980856689601 - row user_email is the persona (owen.baker@harmonygames.co)
[YES LB] L284 gmail.gmail_messages insert owen.baker@harmonygames.co/<CAK0a68e5711011904665cac8fb31fa@mail.gmail.com>, owen.baker@ha - row user_email is the persona (owen.baker@harmonygames.co)
[NO] L286 gmail.gmail_threads insert vincent.parker@harmonygames.co/1849333980856689601 - row is in mailbox vincent.parker@harmonygames.co, not the persona's (owen.baker@harmonygames.co)
[NO] L288 gmail.gmail_messages insert vincent.parker@harmonygames.co/<CAK0a68e5711011904665cac8fb31fa@mail.gmail.com>, vincent.p - row is in mailbox vincent.parker@harmonygames.co, not the persona's (owen.baker@harmonygames.co)
[YES] L290 gmail.gmail_threads insert owen.baker@harmonygames.co/1857000030818491195 - row user_email is the persona (owen.baker@harmonygames.co)
[YES LB] L292 gmail.gmail_messages insert owen.baker@harmonygames.co/<calendar-9dbb3394-3afb-90bf-5a8a-93ab53df8c6c@google.com>, owe - row user_email is the persona (owen.baker@harmonygames.co)
[NO] L294 gmail.gmail_threads insert oliver.brooks@harmonygames.co/1857000268685893160 - row is in mailbox oliver.brooks@harmonygames.co, not the persona's (owen.baker@harmonygames.co)
[NO] L296 gmail.gmail_messages insert oliver.brooks@harmonygames.co/<calendar-fae5cd58-b7f0-d8c7-8d8b-118e3ad12f3c@google.com>,  - row is in mailbox oliver.brooks@harmonygames.co, not the persona's (owen.baker@harmonygames.co)
[NO] L298 gmail.gmail_threads insert robert@harmonygames.co/1857000003398313455 - row is in mailbox robert@harmonygames.co, not the persona's (owen.baker@harmonygames.co)
[NO] L300 gmail.gmail_messages insert robert@harmonygames.co/<calendar-004f2df1-97df-af26-ef21-46889e5e9f32@google.com>, robert@ - row is in mailbox robert@harmonygames.co, not the persona's (owen.baker@harmonygames.co)
[YES] L302 gcal.gcal_events insert evt_d03eaa3f340f4f1cbfa41f - persona is an attendee and holds its own copy evt_6e2c91d4b07f3a58c1d2e4 (same ical_uid and start) on owen.baker@harmonygames.co
[YES] L305 gcal.gcal_events insert evt_e6e10cdd5b4189da31a63d - persona is an attendee and holds its own copy evt_6e2c91d4b07f3a58c1d2e4 (same ical_uid and start) on owen.baker@harmonygames.co
[YES] L307 gcal.gcal_events insert evt_7b4212e7ae0684d6d682cb - persona is an attendee and holds its own copy evt_6e2c91d4b07f3a58c1d2e4 (same ical_uid and start) on owen.baker@harmonygames.co
[YES LB] L309 gcal.gcal_events insert evt_6e2c91d4b07f3a58c1d2e4 - event is on the persona's own calendar owen.baker@harmonygames.co
[YES LB] base slack C05433XK267/1765310004.760809 - base record: message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of public builds
[YES LB] base slack C05V5FNLB9V/1764266442.497979 - base record: message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of private god-bugs
[YES LB] base slack C05V5FNLB9V/1764659550.713509 - base record: message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of private god-bugs
[YES LB] base slack C05V5FNLB9V/1764660142.352319 - base record: message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of private god-bugs
[YES LB] base slack C05V5FNLB9V/1764661312.152719 - base record: message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of private god-bugs
[YES LB] base slack C05V5FNLB9V/1764661921.018749 - base record: message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of private god-bugs
[YES LB] base slack C09SWTHEMEW/1764659626.614679 - base record: message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of private publishing-ext-[SOURCE_ORG_0001]-nbp7547
[YES LB] base slack C9CA62B5180A/1765927876.696389 - base record: message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of mpim mpdm-leonard.hayes--brian.foster--arthur.blake--owen.baker-1
[YES LB] base slack CE156FDFB428/1763549455.195819 - base record: message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES LB] base slack CE156FDFB428/1763642831.967359 - base record: message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025
[YES LB] base gdrive f_948768f5a462e7037d17c9 - base record: file is shared with the persona (shared_with_emails)

summary: {'YES': 99, 'NO': 6}  unscoped rows (always visible): 83
  gcal.gcal_events: {'YES': 4}
  gdocs.docs_documents: {'YES': 2}
  gdrive.drive_files: {'YES': 5}
  gmail.gmail_messages: {'YES': 2, 'NO': 3}
  gmail.gmail_threads: {'YES': 2, 'NO': 3}
  gsheets.sheets_sheets: {'YES': 3}
  gsheets.sheets_spreadsheets: {'YES': 1}
  gslides.slides_page_elements: {'YES': 8}
  gslides.slides_pages: {'YES': 4}
  gslides.slides_presentations: {'YES': 1}
  slack.slack_messages: {'YES': 67}
verdict: PASS (0 load-bearing rows not visible)
```

## 1.F Collision

Every id the SQL mints was looked up over its full base collection (`tools/hg.py search lookup`, outputs in `plan/idcheck/`):
- gdrive drive_files: 5 ids, 53866 base records checked, scan_complete True, 0 matches (plan/idcheck/gdrive.out.json).
- gcal events: 4 ids, 11130 base records checked, scan_complete True, 0 matches (plan/idcheck/gcal.out.json).
- trello cards: 2 ids, 803 base records checked, scan_complete True, 0 matches (plan/idcheck/trello_card.out.json).
- trello actions: 4 ids, 5294 base records checked, scan_complete True, 0 matches (plan/idcheck/trello_action.out.json).
- trello checklists: 1 ids, 54 base records checked, scan_complete True, 0 matches (plan/idcheck/trello_checklist.out.json).
- trello check items: 28 ids, 161 base records checked, scan_complete True, 0 matches (plan/idcheck/trello_check_item.out.json).
- github pull_request_comments: 10 ids, 884 base records checked, scan_complete True, 0 matches (plan/idcheck/github_comment.out.json).
- github timeline_events: 10 ids, 12435 base records checked, scan_complete True, 0 matches (plan/idcheck/github_event.out.json).
- github review_comments: 2 ids, 1614 base records checked, scan_complete True, 0 matches (plan/idcheck/github_rc.out.json).
- Slack (channel, ts) pairs and Gmail ids: base_check Check A PASS; seeded Gmail threads are new numeric ids in each mailbox.
- Linear comment ids and Slides object ids have no base rows to collide with (NB-24; gslides ids are per presentation). Header tokens: none minted.

## Record ledger

One row per SQL statement, in SQL order.

| # | SQL line | Op | Table | Id | Pointer | Role |
|---|---|---|---|---|---|---|
| 1 | L3 | insert | gdrive.drive_files | d_9b41e7c2a05d36f8e1c7a4 | d_9b41e7c2a05d36f8e1c7a4 | container |
| 2 | L6 | insert | gdrive.drive_files | f_3ca9e15d7b20f4e681ad52 | f_3ca9e15d7b20f4e681ad52 | authority H1 |
| 3 | L8 | insert | gdrive.drive_files | f_72e0b4c3d91a5f68c2b7e4 | f_72e0b4c3d91a5f68c2b7e4 | decoy |
| 4 | L10 | insert | gdrive.drive_files | f_d15a8c70e3f2b94a61c8d3 | f_d15a8c70e3f2b94a61c8d3 | stale summary |
| 5 | L12 | insert | gdrive.drive_files | f_a9ba8abc7d5189babcb378 | f_a9ba8abc7d5189babcb378 | container |
| 6 | L14 | insert | gdocs.docs_documents | f_3ca9e15d7b20f4e681ad52 | f_3ca9e15d7b20f4e681ad52 | authority H1 |
| 7 | L17 | insert | gdocs.docs_documents | f_72e0b4c3d91a5f68c2b7e4 | f_72e0b4c3d91a5f68c2b7e4 | decoy |
| 8 | L19 | insert | gsheets.sheets_spreadsheets | f_a9ba8abc7d5189babcb378 | f_a9ba8abc7d5189babcb378 | container |
| 9 | L22 | insert | gsheets.sheets_sheets | f_a9ba8abc7d5189babcb378 | f_a9ba8abc7d5189babcb378 | tracker tab |
| 10 | L24 | insert | gsheets.sheets_sheets | f_a9ba8abc7d5189babcb378 | f_a9ba8abc7d5189babcb378 | tracker tab |
| 11 | L26 | insert | gsheets.sheets_sheets | f_a9ba8abc7d5189babcb378 | f_a9ba8abc7d5189babcb378 | tracker tab |
| 12 | L28 | insert | gslides.slides_presentations | f_d15a8c70e3f2b94a61c8d3 | f_d15a8c70e3f2b94a61c8d3 | stale summary |
| 13 | L31 | insert | gslides.slides_pages | f_d15a8c70e3f2b94a61c8d3 | f_d15a8c70e3f2b94a61c8d3 | stale summary |
| 14 | L33 | insert | gslides.slides_page_elements | f_d15a8c70e3f2b94a61c8d3 | f_d15a8c70e3f2b94a61c8d3 | stale summary |
| 15 | L35 | insert | gslides.slides_page_elements | f_d15a8c70e3f2b94a61c8d3 | f_d15a8c70e3f2b94a61c8d3 | stale summary |
| 16 | L37 | insert | gslides.slides_pages | f_d15a8c70e3f2b94a61c8d3 | f_d15a8c70e3f2b94a61c8d3 | stale summary |
| 17 | L39 | insert | gslides.slides_page_elements | f_d15a8c70e3f2b94a61c8d3 | f_d15a8c70e3f2b94a61c8d3 | stale summary |
| 18 | L41 | insert | gslides.slides_page_elements | f_d15a8c70e3f2b94a61c8d3 | f_d15a8c70e3f2b94a61c8d3 | stale summary |
| 19 | L43 | insert | gslides.slides_pages | f_d15a8c70e3f2b94a61c8d3 | f_d15a8c70e3f2b94a61c8d3 | stale summary |
| 20 | L45 | insert | gslides.slides_page_elements | f_d15a8c70e3f2b94a61c8d3 | f_d15a8c70e3f2b94a61c8d3 | stale summary |
| 21 | L47 | insert | gslides.slides_page_elements | f_d15a8c70e3f2b94a61c8d3 | f_d15a8c70e3f2b94a61c8d3 | stale summary |
| 22 | L49 | insert | gslides.slides_pages | f_d15a8c70e3f2b94a61c8d3 | f_d15a8c70e3f2b94a61c8d3 | stale summary |
| 23 | L51 | insert | gslides.slides_page_elements | f_d15a8c70e3f2b94a61c8d3 | f_d15a8c70e3f2b94a61c8d3 | stale summary |
| 24 | L53 | insert | gslides.slides_page_elements | f_d15a8c70e3f2b94a61c8d3 | f_d15a8c70e3f2b94a61c8d3 | stale summary |
| 25 | L55 | insert | slack.slack_messages | 488d87e2e651cc1fb00c034bd6df5a4a | D05S1S2AB5M/1770937805.214409 | hub |
| 26 | L58 | insert | slack.slack_messages | 91be79cc8e72189a592762c24c531925 | D05USBTQY1F/1765452012.418229 | overturning |
| 27 | L60 | insert | slack.slack_messages | 9bf944b8fcadea7bd8010fccf1baee22 | D07E9PSQB6W/1765206644.602119 | closing record |
| 28 | L62 | insert | slack.slack_messages | 2ea7c02c6ddb99bc9b37f680be4159a6 | D07E9PSQB6W/1765471563.704419 | INT-01 copy or control |
| 29 | L64 | insert | slack.slack_messages | 2f3add0dcfc251b7e92cd216af7352e2 | D07E9PSQB6W/1765471651.208713 | INT-01 copy or control |
| 30 | L66 | insert | slack.slack_messages | e48eb03d633e480ea6f7cddea576ef4c | C09Q4S613CN/1764606918.318209 | overturning |
| 31 | L68 | insert | slack.slack_messages | d49c24581dc7a16427b92fda3de0b8b5 | C05V5FNLB9V/1767021345.207719 | closing record |
| 32 | L70 | insert | slack.slack_messages | 70692cd00e9483ddce075a18d43e1f4c | C09Q4S613CN/1766164222.418229 | INT-01 copy or control |
| 33 | L72 | insert | slack.slack_messages | e7fe05ca83bdb700b0acd4cc054e5a38 | CE156FDFB428/1763845212.507119 | overturning |
| 34 | L74 | insert | slack.slack_messages | 42460650faeb4109764ba2c092b43578 | CE156FDFB428/1763742012.611229 | overturning |
| 35 | L76 | insert | slack.slack_messages | 2acc689f598cf1569e4b7d3b911782c3 | CE156FDFB428/1763845812.703339 | overturning |
| 36 | L78 | insert | slack.slack_messages | 5fe8e6e599e4e03de80e8a079c05e796 | CE156FDFB428/1763845872.804449 | overturning |
| 37 | L80 | insert | slack.slack_messages | 948d64b2f42b443b0e509a0c66a03e3c | CE156FDFB428/1763845512.559339 | INT-01 copy or control |
| 38 | L82 | insert | slack.slack_messages | e3e5bf78e3fdfac0af10bd701a6e7a3f | CE156FDFB428/1770842472.100349 | INT-01 copy or control |
| 39 | L84 | insert | slack.slack_messages | d38307a8374e099be59b05f2b9cfbb0b | C09Q4S613CN/1770842473.458979 | INT-01 copy or control |
| 40 | L86 | insert | slack.slack_messages | 0cc44f9deecc40e15421630ef480ec3e | C05433XK267/1770842474.718529 | INT-01 copy or control |
| 41 | L88 | insert | slack.slack_messages | 186107ee50a7626bc73d0fa44fc318d9 | C09SWTHEMEW/1770842475.449099 | INT-01 copy or control |
| 42 | L90 | insert | slack.slack_messages | c399a0bd2507460c5f14d0ff1b5c00a1 | C05V5FNLB9V/1770936063.680719 | INT-01 copy or control |
| 43 | L92 | insert | slack.slack_messages | b8b079a1305da1183e10f2214c040662 | CE156FDFB428/1770936087.049309 | INT-01 copy or control |
| 44 | L94 | insert | slack.slack_messages | 300958649de97d10a627b1b1b540f733 | C09Q4S613CN/1770936109.066419 | INT-01 copy or control |
| 45 | L96 | insert | slack.slack_messages | a93fda6f707471cbf829bf12f3d9fbfd | C05433XK267/1770936132.102479 | INT-01 copy or control |
| 46 | L98 | insert | slack.slack_messages | ef892f6ec08e170ab2f1ab0b5fb06ae0 | C09SWTHEMEW/1770936156.410649 | INT-01 copy or control |
| 47 | L100 | insert | slack.slack_messages | 8b1af0fccdb891a201c8e71576334165 | C050WGU41HR/1770936178.946639 | INT-01 copy or control |
| 48 | L102 | insert | slack.slack_messages | 1ccf4d6672818c4603f63b50df215c40 | CE156FDFB428/1763738404.458929 | INT-01 copy or control |
| 49 | L104 | insert | slack.slack_messages | 8240272f0daced8794805dcb1370898d | CE156FDFB428/1763738911.308829 | INT-01 copy or control |
| 50 | L106 | insert | slack.slack_messages | ea0a6b8a9df6ae9a57508359e1f626dc | CE156FDFB428/1763739192.201719 | INT-01 copy or control |
| 51 | L108 | insert | slack.slack_messages | 063efe55f310099cb2885d3f89dc674c | CE156FDFB428/1763739347.318979 | INT-01 copy or control |
| 52 | L110 | insert | slack.slack_messages | d9ee1b377378db22c3a5fa25ed7ed369 | CE156FDFB428/1763739440.491349 | INT-01 copy or control |
| 53 | L112 | insert | slack.slack_messages | 2c76e59284ba24eeac1eed057f285198 | CE156FDFB428/1763739605.860489 | INT-01 copy or control |
| 54 | L114 | insert | slack.slack_messages | 87dc850c774ea6c22e67bdd7e8bfc7a7 | C05V5FNLB9V/1764331830.705279 | INT-01 copy or control |
| 55 | L116 | insert | slack.slack_messages | c520e100fdab72168d8d753e54ce4e5a | C050WGU41HR/1763073612.651219 | INT-01 copy or control |
| 56 | L118 | insert | slack.slack_messages | 6bdb1aa52765811abb84fb47588ac89a | C050WGU41HR/1763407241.925879 | INT-01 copy or control |
| 57 | L120 | insert | slack.slack_messages | f846da322aa89c0993ccd928c8c8c331 | C050WGU41HR/1763494329.962479 | INT-01 copy or control |
| 58 | L122 | insert | slack.slack_messages | a84f06fbe074112fbc0fbdd64bd2e092 | C050WGU41HR/1763496333.386579 | INT-01 copy or control |
| 59 | L124 | insert | slack.slack_messages | 1485803a59f9a37f9b1d841dfafc40bb | C050WGU41HR/1763505318.248159 | INT-01 copy or control |
| 60 | L126 | insert | slack.slack_messages | 6571cffd875d0513c370930a17b3778a | C050WGU41HR/1763527947.637599 | INT-01 copy or control |
| 61 | L128 | insert | slack.slack_messages | ee92520b49534bb87581e554df7d5060 | C050WGU41HR/1763586644.212819 | INT-01 copy or control |
| 62 | L130 | insert | slack.slack_messages | 7b71b1c0edfe1af5dad899d9372a628a | C050WGU41HR/1763593926.596469 | INT-01 copy or control |
| 63 | L132 | insert | slack.slack_messages | fdab15395088ad4ce51cd08088e60b3a | C050WGU41HR/1766187602.932159 | INT-01 copy or control |
| 64 | L134 | insert | slack.slack_messages | 3a57ea1dc5504199cb61300a37c4c1d1 | C050WGU41HR/1766775029.801269 | INT-01 copy or control |
| 65 | L136 | insert | slack.slack_messages | ea8f1a2d0abb0e0b521418e4db6d94d2 | C050WGU41HR/1763557535.436659 | INT-01 copy or control |
| 66 | L138 | insert | slack.slack_messages | 52eafc2b8f3d50523ffccf60b77fc613 | C050WGU41HR/1763603515.121629 | INT-01 copy or control |
| 67 | L140 | update | slack.slack_messages | 37dc1365297989005c98ca1012808d6e | 37dc1365297989005c98ca1012808d6e | thread counters |
| 68 | L141 | update | slack.slack_messages | d25dd8d11d9e1c1df11c941262bfa31b | d25dd8d11d9e1c1df11c941262bfa31b | thread counters |
| 69 | L142 | update | slack.slack_messages | 15e314b25f7d69d8077e073e622baefa | 15e314b25f7d69d8077e073e622baefa | thread counters |
| 70 | L143 | update | slack.slack_messages | 1bc1434b15a44cec9044db1b59ae4995 | 1bc1434b15a44cec9044db1b59ae4995 | thread counters |
| 71 | L144 | update | slack.slack_messages | f0d28e20be9cdbbd03c6b0fb69f916c0 | f0d28e20be9cdbbd03c6b0fb69f916c0 | thread counters |
| 72 | L145 | update | slack.slack_messages | a31a43de27e340995e378e372149c179 | a31a43de27e340995e378e372149c179 | thread counters |
| 73 | L146 | update | slack.slack_messages | 55a5f61fae9f04f5fa5d4f29819ea0e2 | 55a5f61fae9f04f5fa5d4f29819ea0e2 | thread counters |
| 74 | L147 | update | slack.slack_messages | ef80c659e26c08225ceeb4f7a9f97d42 | ef80c659e26c08225ceeb4f7a9f97d42 | thread counters |
| 75 | L148 | update | slack.slack_messages | 3f6d03da9f66de3c25c4958a260c712c | 3f6d03da9f66de3c25c4958a260c712c | thread counters |
| 76 | L149 | update | slack.slack_messages | 24f623d4fbac205ae65b0777ccabbc72 | 24f623d4fbac205ae65b0777ccabbc72 | thread counters |
| 77 | L150 | update | slack.slack_messages | c4d52c84291fad8d0b269704b231b736 | c4d52c84291fad8d0b269704b231b736 | thread counters |
| 78 | L151 | update | slack.slack_messages | cac88241bed9b8ca23f059664a775ebf | cac88241bed9b8ca23f059664a775ebf | thread counters |
| 79 | L152 | update | slack.slack_messages | cd1ddb4d235967b5f5a3071356f8fc76 | cd1ddb4d235967b5f5a3071356f8fc76 | thread counters |
| 80 | L153 | update | slack.slack_messages | 48ec84642fb79215d0c7409b2a9ed199 | 48ec84642fb79215d0c7409b2a9ed199 | thread counters |
| 81 | L154 | update | slack.slack_messages | a9665999506d442b1809e58261cd1f9d | a9665999506d442b1809e58261cd1f9d | thread counters |
| 82 | L155 | update | slack.slack_messages | dfb3bc5e2d7d43ee4af72061aa1efb88 | dfb3bc5e2d7d43ee4af72061aa1efb88 | thread counters |
| 83 | L156 | update | slack.slack_messages | e080921ea3d8541de55bdd3f6c672c22 | e080921ea3d8541de55bdd3f6c672c22 | thread counters |
| 84 | L157 | update | slack.slack_messages | 3fd15aec984400ecb1b011298da3af1f | 3fd15aec984400ecb1b011298da3af1f | thread counters |
| 85 | L158 | update | slack.slack_messages | 74369ca47c39d84359bcc5bab882ce14 | 74369ca47c39d84359bcc5bab882ce14 | thread counters |
| 86 | L159 | update | slack.slack_messages | 1b9deda51503ae9114973759ccf17b91 | 1b9deda51503ae9114973759ccf17b91 | thread counters |
| 87 | L160 | update | slack.slack_messages | 50de5b6fe965e395aa422f6c03e43d0f | 50de5b6fe965e395aa422f6c03e43d0f | thread counters |
| 88 | L161 | update | slack.slack_messages | 2d723769e248e00040c52f788e054d8c | 2d723769e248e00040c52f788e054d8c | thread counters |
| 89 | L162 | update | slack.slack_messages | d109a8676777081d8ac8410f19eaac5e | d109a8676777081d8ac8410f19eaac5e | thread counters |
| 90 | L163 | update | slack.slack_messages | faaefaacbfbe94421efdc365b484bb76 | faaefaacbfbe94421efdc365b484bb76 | thread counters |
| 91 | L164 | update | slack.slack_messages | f36b509907752654e7111983a698e9bd | f36b509907752654e7111983a698e9bd | thread counters |
| 92 | L165 | insert | github.github_pr_comments | harmonygames-Games/GameOfDominoes#1895#c_3 | harmonygames-Games/GameOfDominoes#1895#c_3 | done claim |
| 93 | L168 | insert | github.github_timeline_events | harmonygames-Games/GameOfDominoes#1895#ev_6 | harmonygames-Games/GameOfDominoes#1895#ev_6 | timeline companion |
| 94 | L170 | insert | github.github_pr_comments | harmonygames-Games/GameOfDominoes#1898#c_3 | harmonygames-Games/GameOfDominoes#1898#c_3 | done claim |
| 95 | L172 | insert | github.github_timeline_events | harmonygames-Games/GameOfDominoes#1898#ev_8 | harmonygames-Games/GameOfDominoes#1898#ev_8 | timeline companion |
| 96 | L174 | insert | github.github_pr_comments | harmonygames-Games/GameOfDominoes#1901#c_3 | harmonygames-Games/GameOfDominoes#1901#c_3 | done claim |
| 97 | L176 | insert | github.github_timeline_events | harmonygames-Games/GameOfDominoes#1901#ev_6 | harmonygames-Games/GameOfDominoes#1901#ev_6 | timeline companion |
| 98 | L178 | insert | github.github_pr_comments | harmonygames-Games/GameOfDominoes#1902#c_3 | harmonygames-Games/GameOfDominoes#1902#c_3 | done claim |
| 99 | L180 | insert | github.github_timeline_events | harmonygames-Games/GameOfDominoes#1902#ev_6 | harmonygames-Games/GameOfDominoes#1902#ev_6 | timeline companion |
| 100 | L182 | insert | github.github_pr_comments | harmonygames-Games/GameOfDominoes#1903#c_3 | harmonygames-Games/GameOfDominoes#1903#c_3 | done claim |
| 101 | L184 | insert | github.github_timeline_events | harmonygames-Games/GameOfDominoes#1903#ev_6 | harmonygames-Games/GameOfDominoes#1903#ev_6 | timeline companion |
| 102 | L186 | insert | github.github_pr_comments | harmonygames-Games/GameOfDominoes#1905#c_3 | harmonygames-Games/GameOfDominoes#1905#c_3 | done claim |
| 103 | L188 | insert | github.github_timeline_events | harmonygames-Games/GameOfDominoes#1905#ev_6 | harmonygames-Games/GameOfDominoes#1905#ev_6 | timeline companion |
| 104 | L190 | insert | github.github_pr_comments | harmonygames-Games/GameOfDominoes#1907#c_2 | harmonygames-Games/GameOfDominoes#1907#c_2 | done claim |
| 105 | L192 | insert | github.github_timeline_events | harmonygames-Games/GameOfDominoes#1907#ev_7 | harmonygames-Games/GameOfDominoes#1907#ev_7 | timeline companion |
| 106 | L194 | insert | github.github_pr_comments | harmonygames-Games/GameOfDominoes#1908#c_3 | harmonygames-Games/GameOfDominoes#1908#c_3 | done claim |
| 107 | L196 | insert | github.github_timeline_events | harmonygames-Games/GameOfDominoes#1908#ev_6 | harmonygames-Games/GameOfDominoes#1908#ev_6 | timeline companion |
| 108 | L198 | insert | github.github_pr_comments | harmonygames-Games/GameOfDominoes#1915#c_2 | harmonygames-Games/GameOfDominoes#1915#c_2 | done claim |
| 109 | L200 | insert | github.github_timeline_events | harmonygames-Games/GameOfDominoes#1915#ev_6 | harmonygames-Games/GameOfDominoes#1915#ev_6 | timeline companion |
| 110 | L202 | insert | github.github_pr_comments | harmonygames-Games/GameOfDominoes#1916#c_2 | harmonygames-Games/GameOfDominoes#1916#c_2 | done claim |
| 111 | L204 | insert | github.github_timeline_events | harmonygames-Games/GameOfDominoes#1916#ev_5 | harmonygames-Games/GameOfDominoes#1916#ev_5 | timeline companion |
| 112 | L206 | insert | github.github_review_comments | harmonygames-Games/GameOfDominoes#1905#rc_1 | harmonygames-Games/GameOfDominoes#1905#rc_1 | overturning |
| 113 | L208 | insert | github.github_review_comments | harmonygames-Games/GameOfDominoes#1908#rc_1 | harmonygames-Games/GameOfDominoes#1908#rc_1 | overturning |
| 114 | L210 | insert | trello.trello_cards | 690b27282f4c1b7a6e93d512 | 690b27282f4c1b7a6e93d512 | container |
| 115 | L213 | insert | trello.trello_actions | 690b2728dae383f52833cb5d | 690b2728dae383f52833cb5d | container |
| 116 | L215 | insert | trello.trello_actions | 690b29bc3c7d2e51b0f86a47 | 690b29bc3c7d2e51b0f86a47 | authority H2 |
| 117 | L217 | insert | trello.trello_checklists | 690b27285bfa8e197220e1d5 | 690b27285bfa8e197220e1d5 | container |
| 118 | L219 | insert | trello.trello_check_items | 690b27280037e214469462bf | 690b27280037e214469462bf | container |
| 119 | L221 | insert | trello.trello_check_items | 690b27282fede6548e9e36cd | 690b27282fede6548e9e36cd | container |
| 120 | L223 | insert | trello.trello_check_items | 690b2728e2201f6006b6c5d4 | 690b2728e2201f6006b6c5d4 | container |
| 121 | L225 | insert | trello.trello_check_items | 690b2728605ac106471c7fd0 | 690b2728605ac106471c7fd0 | container |
| 122 | L227 | insert | trello.trello_check_items | 690b27288e3ff9747b20f684 | 690b27288e3ff9747b20f684 | container |
| 123 | L229 | insert | trello.trello_check_items | 690b2728a267b9e855f2d17d | 690b2728a267b9e855f2d17d | container |
| 124 | L231 | insert | trello.trello_check_items | 690b2728176578d5ac549921 | 690b2728176578d5ac549921 | container |
| 125 | L233 | insert | trello.trello_check_items | 690b272882aa21f38b7a11c2 | 690b272882aa21f38b7a11c2 | container |
| 126 | L235 | insert | trello.trello_check_items | 690b2728d2a45a28d9922d3c | 690b2728d2a45a28d9922d3c | container |
| 127 | L237 | insert | trello.trello_check_items | 690b2728905939a52af8cd5f | 690b2728905939a52af8cd5f | container |
| 128 | L239 | insert | trello.trello_check_items | 690b2728c894a1e478ee0435 | 690b2728c894a1e478ee0435 | container |
| 129 | L241 | insert | trello.trello_check_items | 690b272850b31c44b15bb5ac | 690b272850b31c44b15bb5ac | container |
| 130 | L243 | insert | trello.trello_check_items | 690b27288b85a48bfecb4962 | 690b27288b85a48bfecb4962 | container |
| 131 | L245 | insert | trello.trello_check_items | 690b27287758be1fc00249ad | 690b27287758be1fc00249ad | container |
| 132 | L247 | insert | trello.trello_check_items | 690b2728b3acd63509b8ab09 | 690b2728b3acd63509b8ab09 | container |
| 133 | L249 | insert | trello.trello_check_items | 690b2728f59f48a1d20203de | 690b2728f59f48a1d20203de | container |
| 134 | L251 | insert | trello.trello_check_items | 690b2728b69da088a2dfa44a | 690b2728b69da088a2dfa44a | container |
| 135 | L253 | insert | trello.trello_check_items | 690b2728731ccfb6cb410a4a | 690b2728731ccfb6cb410a4a | container |
| 136 | L255 | insert | trello.trello_check_items | 690b2728cf034138aa957676 | 690b2728cf034138aa957676 | container |
| 137 | L257 | insert | trello.trello_check_items | 690b27282356124b6646b14e | 690b27282356124b6646b14e | container |
| 138 | L259 | insert | trello.trello_check_items | 690b272873a8bed76911c8a2 | 690b272873a8bed76911c8a2 | container |
| 139 | L261 | insert | trello.trello_check_items | 690b2728ce404c420931b712 | 690b2728ce404c420931b712 | container |
| 140 | L263 | insert | trello.trello_check_items | 690b2728345604361a5ca503 | 690b2728345604361a5ca503 | container |
| 141 | L265 | insert | trello.trello_check_items | 690b272814dbf388361c261a | 690b272814dbf388361c261a | container |
| 142 | L267 | insert | trello.trello_check_items | 690b27282d04d00e37d853f2 | 690b27282d04d00e37d853f2 | container |
| 143 | L269 | insert | trello.trello_check_items | 690b27280b8f7d6e31195b50 | 690b27280b8f7d6e31195b50 | container |
| 144 | L271 | insert | trello.trello_check_items | 690b27280ea525851ceeec44 | 690b27280ea525851ceeec44 | container |
| 145 | L273 | insert | trello.trello_check_items | 690b2728bc6ff30105dbbdd6 | 690b2728bc6ff30105dbbdd6 | container |
| 146 | L275 | insert | trello.trello_cards | 68d27e2817451477a636502d | 68d27e2817451477a636502d | container |
| 147 | L277 | insert | trello.trello_actions | 68d27e2858bf93998ab5621b | 68d27e2858bf93998ab5621b | container |
| 148 | L279 | insert | trello.trello_actions | 68d284b84b7e9a3c5d16e208 | 68d284b84b7e9a3c5d16e208 | decoy |
| 149 | L281 | insert | gmail.gmail_threads | owen.baker@harmonygames.co/1849333980856689601 | owen.baker@harmonygames.co/1849333980856689601 | mail thread |
| 150 | L284 | insert | gmail.gmail_messages | owen.baker@harmonygames.co/<CAK0a68e5711011904665cac8fb31fa@mail.gmail.com> | owen.baker@harmonygames.co/<CAK0a68e5711011904665cac8fb31fa@mail.gmail.com> | mail |
| 151 | L286 | insert | gmail.gmail_threads | vincent.parker@harmonygames.co/1849333980856689601 | vincent.parker@harmonygames.co/1849333980856689601 | mail thread |
| 152 | L288 | insert | gmail.gmail_messages | vincent.parker@harmonygames.co/<CAK0a68e5711011904665cac8fb31fa@mail.gmail.com> | vincent.parker@harmonygames.co/<CAK0a68e5711011904665cac8fb31fa@mail.gmail.com> | mail |
| 153 | L290 | insert | gmail.gmail_threads | owen.baker@harmonygames.co/1857000030818491195 | owen.baker@harmonygames.co/1857000030818491195 | mail thread |
| 154 | L292 | insert | gmail.gmail_messages | owen.baker@harmonygames.co/<calendar-9dbb3394-3afb-90bf-5a8a-93ab53df8c6c@google.com> | owen.baker@harmonygames.co/<calendar-9dbb3394-3afb-90bf-5a8a-93ab53df8c6c@google.com> | mail |
| 155 | L294 | insert | gmail.gmail_threads | oliver.brooks@harmonygames.co/1857000268685893160 | oliver.brooks@harmonygames.co/1857000268685893160 | mail thread |
| 156 | L296 | insert | gmail.gmail_messages | oliver.brooks@harmonygames.co/<calendar-fae5cd58-b7f0-d8c7-8d8b-118e3ad12f3c@google.com> | oliver.brooks@harmonygames.co/<calendar-fae5cd58-b7f0-d8c7-8d8b-118e3ad12f3c@google.com> | mail |
| 157 | L298 | insert | gmail.gmail_threads | robert@harmonygames.co/1857000003398313455 | robert@harmonygames.co/1857000003398313455 | mail thread |
| 158 | L300 | insert | gmail.gmail_messages | robert@harmonygames.co/<calendar-004f2df1-97df-af26-ef21-46889e5e9f32@google.com> | robert@harmonygames.co/<calendar-004f2df1-97df-af26-ef21-46889e5e9f32@google.com> | mail |
| 159 | L302 | insert | gcal.gcal_events | evt_d03eaa3f340f4f1cbfa41f | evt_d03eaa3f340f4f1cbfa41f | share list |
| 160 | L305 | insert | gcal.gcal_events | evt_e6e10cdd5b4189da31a63d | evt_e6e10cdd5b4189da31a63d | share list |
| 161 | L307 | insert | gcal.gcal_events | evt_7b4212e7ae0684d6d682cb | evt_7b4212e7ae0684d6d682cb | share list |
| 162 | L309 | insert | gcal.gcal_events | evt_6e2c91d4b07f3a58c1d2e4 | evt_6e2c91d4b07f3a58c1d2e4 | share list |
| 163 | L311 | insert | linear.linear_comments | comment_49b5ac4788465f72ddf245e34f2b7034 | ENG-2401 | amendment |
| 164 | L314 | insert | linear.linear_comments | comment_7ab5299cbb609d95ba12249d315daedc | ENG-2363 | tie to a ticket |
| 165 | L316 | insert | linear.linear_comments | comment_d6aee2099bd71050facc422ccef8f809 | ENG-2428 | overturning |
| 166 | L318 | insert | linear.linear_comments | comment_c15e952b61d3b7ba1ca740acb860c0c8 | ENG-2429 | per-record note |
| 167 | L320 | insert | linear.linear_comments | comment_e9616424ae2a8c54a93e51a781e34be6 | ENG-2410 | per-record note |
| 168 | L322 | insert | linear.linear_comments | comment_f5caa205df9ec5cbcbceb1a9de201b3d | ENG-2430 | per-record note |
| 169 | L324 | insert | linear.linear_comments | comment_6df8b85f66b43fa2a173e1a8d7cd2a28 | ENG-2280 | per-record note |
| 170 | L326 | insert | linear.linear_comments | comment_c5a3ffccf561dbb71a9bbb2ef961d76e | ENG-2281 | per-record note |
| 171 | L328 | insert | linear.linear_comments | comment_36dbd022c09b1ccba0b68532bc461881 | ENG-2398 | per-record note |
| 172 | L330 | insert | linear.linear_comments | comment_f2bf9a8556b65c752110e2ab581da03d | ENG-2181 | per-record note |
| 173 | L332 | insert | linear.linear_comments | comment_118671caae1eb97367ac4e3e8ad9f311 | ENG-2351 | per-record note |
| 174 | L334 | insert | linear.linear_comments | comment_18c104ccad4ab3939621d8505d266fe1 | ENG-2406 | per-record note |
| 175 | L336 | update | linear.linear_issues | ENG-2181 | ENG-2181 | state repair or updated_at |
| 176 | L337 | update | linear.linear_issues | ENG-2280 | ENG-2280 | state repair or updated_at |
| 177 | L338 | update | linear.linear_issues | ENG-2281 | ENG-2281 | state repair or updated_at |
| 178 | L339 | update | linear.linear_issues | ENG-2351 | ENG-2351 | state repair or updated_at |
| 179 | L340 | update | linear.linear_issues | ENG-2363 | ENG-2363 | state repair or updated_at |
| 180 | L341 | update | linear.linear_issues | ENG-2398 | ENG-2398 | state repair or updated_at |
| 181 | L342 | update | linear.linear_issues | ENG-2401 | ENG-2401 | state repair or updated_at |
| 182 | L343 | update | linear.linear_issues | ENG-2406 | ENG-2406 | state repair or updated_at |
| 183 | L344 | update | linear.linear_issues | ENG-2410 | ENG-2410 | state repair or updated_at |
| 184 | L345 | update | linear.linear_issues | ENG-2428 | ENG-2428 | state repair or updated_at |
| 185 | L346 | update | linear.linear_issues | ENG-2429 | ENG-2429 | state repair or updated_at |
| 186 | L347 | update | linear.linear_issues | ENG-2430 | ENG-2430 | state repair or updated_at |
| 187 | L348 | update | linear.linear_issues | ENG-2403 | ENG-2403 | state repair or updated_at |
| 188 | L349 | update | linear.linear_issues | ENG-2404 | ENG-2404 | state repair or updated_at |

## Findability and discovery-order proofs

- Hub (AN1) D05S1S2AB5M/1770937805.214409 (row 488d87e2e651cc1fb00c034bd6df5a4a): Arthur to Owen, Thu Feb 12 23:10Z; the prompt names it. It names the carry-over notes doc, the UI Changes tree, the folder, Sunday's bug review and the three counts.
- Master ticket (AN2) ENG-2401: named by the hub; linear_list_issues returns it and its children; the amendment comment_49b5ac4788465f72ddf245e34f2b7034 needs linear_list_comments, and H1 says changes go on the master ticket.
- H1 f_3ca9e15d7b20f4e681ad52: shared with Owen; a Drive search for 'carry-over' returns it, with the folder d_9b41e7c2a05d36f8e1c7a4. The decoy f_72e0b4c3d91a5f68c2b7e4 comes up for 'bug list notes'; its title names the other game.
- H2 690b29bc3c7d2e51b0f86a47: H1 says 'Brian's closing rule from the UI work'; the card 690b27282f4c1b7a6e93d512 on board 65eb4ec525346c8070ca638f is the UI work card, and the ZM card's comment 68d284b84b7e9a3c5d16e208 is its decoy.
- T_INLINE_TD and T_INLINE_AXE: the merged PR, Owen's PR comment and Brian's tick on card 690b27282f4c1b7a6e93d512 come first; harmonygames-Games/GameOfDominoes#1905#rc_1 and harmonygames-Games/GameOfDominoes#1908#rc_1 need the PR's own review comments, and the review body is empty.
- T_REPLY: the tick is read from CE156FDFB428/1763549455.195819; the correction sits under an unrelated gems post, C09Q4S613CN/1764606918.318209 (row e48eb03d633e480ea6f7cddea576ef4c).
- T_BACK: the tick and Brian's fix are in CE156FDFB428/1763642831.967359; Marcus's note D05USBTQY1F/1765452012.418229 (row 91be79cc8e72189a592762c24c531925) sits in a DM no anchor names.
- T_GONE: the unticked lines come first; the removal is in C09SWTHEMEW/1764659626.614679 and f_948768f5a462e7037d17c9, and H1 says what counts is the build players have.
- T_WINGS: the child reads as finished until the disable post C9CA62B5180A/1765927876.696389 or the #builds line (commit 79791d4807) is found.
- T_LINE: Marcus's reply C05V5FNLB9V/1764329192.159229 reads as closed; harmonygames-Games/GameOfDominoes#1913 is open and its commit is not in #1914's list.
- T_ELSE: the threads stop at C05V5FNLB9V/1764659550.713509 and neighbours; the closes sit in the #builds line C05433XK267/1765310004.760809 and Brian's DM D07E9PSQB6W/1765206644.602119.
- T_ALIAS: titles use other words; Vincent's mail owen.baker@harmonygames.co/1849333980856689601 ties the Apple line to ENG-2073 and comment_7ab5299cbb609d95ba12249d315daedc ties the manual sign-in line to ENG-2363.
- T_SEASON and the Daily Gift child: the wrap deck f_d15a8c70e3f2b94a61c8d3 (Nov 21) comes first; Oliver's comment_d6aee2099bd71050facc422ccef8f809 (Dec 5) and Brian's DM line D07E9PSQB6W/1765471651.208713 (Dec 11, moved there from ENG-2437 in rev9) overturn it.

## Self-validation

| QC category | Tool-enforced (result) | Manual (evidence) |
|---|---|---|
| Missing Universe Data | check-sql PASS (1.E) | every deciding fact is persona-readable: D05USBTQY1F/1765452012.418229, owen.baker@harmonygames.co/1849333980856689601, f_3ca9e15d7b20f4e681ad52 |
| Temporal Field | sql_lint 0 errors; base_check Check C | check notes follow each fix: ENG-2430 and ENG-2410 after #2205; inline comments follow their reviews and precede the merges, harmonygames-Games/GameOfDominoes#1905#rev_1 |
| Cross-service Referential | base_check Check A | one claim per item across services; each PR comment has its timeline event and its copy in C050WGU41HR |
| Quantitative / Reconciliation | counters updated on every root | the 28 children: 9 already Done plus 19 open under ENG-2403, ENG-2404, ENG-2405; the checklist badges match its 28 items |
| State / Lifecycle | base_check PASS with no hazard ticket modified | the SQL updates no L01, L03 or L07 ticket (13 issue updates, each a companion of a seeded comment); no seeded comment follows a closed ticket; ENG-2417 |
| Identifier / Format | eval lint FAIL 0 CHECK 0 | ids follow base schemes (1.A); base tokens kept, EMPLOYEE_0025_GITHUB_USERNAME |
| Semantic / Category | — | titles match content: f_3ca9e15d7b20f4e681ad52, 690b27282f4c1b7a6e93d512, evt_6e2c91d4b07f3a58c1d2e4 |
| Other | — | voice per 1.C; no record states a total, an outcome list or the sheet |

## Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| github | INT-01 | GitHub Slack app copy in #engineering-bots | seeded for all 12 PR comments and inline comments, threaded under each PR's opened message in C050WGU41HR; all fall inside the window that ends 2025-12-26 |
| github | INT-02, INT-12 | push notices; notification mails | none: no commits or PRs are seeded |
| linear | INT-03, INT-04, INT-05 | linear[bot] on PRs; Slack posts; digests | none: no new PR names a key, and comments on open tickets have no Slack post; ENG-2401 |
| gcal | INT-11 | invitation mails | seeded for Owen, Oliver and Robert from Arthur, Feb 12 23:05Z, with all four calendar copies; evt_6e2c91d4b07f3a58c1d2e4 |
| gdrive | INT-13 | Drive app DMs | none: shares by notice only; f_3ca9e15d7b20f4e681ad52 |
| slack | INT-22 | Slack email notices | none for DMs; D05S1S2AB5M |
| trello | INT-21 | no Trello to Slack integration | none; card 690b27282f4c1b7a6e93d512 |
| gmail | none | Vincent's mail is ordinary mail | none; owen.baker@harmonygames.co/1849333980856689601 |
| gdocs, gsheets, gslides | none | Drive rows mirror every native file | seeded; f_d15a8c70e3f2b94a61c8d3 |

## Touched-data census and coherence hazards

Touched data: the DMs D05S1S2AB5M, D05USBTQY1F and D07E9PSQB6W; channels CE156FDFB428, C05V5FNLB9V, C09Q4S613CN and C050WGU41HR (roots' counters updated); ENG-2401, ENG-2410, ENG-2428, ENG-2429, ENG-2430 and ENG-2437; ENG-2073, ENG-2363, ENG-2398, ENG-2280, ENG-2281, ENG-2181, ENG-2351, ENG-2406; PRs #1895 to #1916; boards 65eb4ec525346c8070ca638f and 6851a6569f3bf818760632ab.

Hazards from coherence_hazards.json (normal KB):
- temporal: T07 — all seeded Slack rows are before Feb 13 10:03Z (latest: the hub); T06 — the Trello card dates from Nov 5, before the board went quiet; T04 — Arthur's Feb note is on an open master; T05 — no seeded comment follows a child's completed_at.
- semantic: S03 — only the Bug label is used; S06 — no title is graded.
- referential: R01, R02 — seeds cite only keys and PRs the records prove; R04 — the hub names docs in words, with no Drive link.
- quantitative: Q01, Q03 — every seeded reply updates its root's reply_count, reply_users_count and latest_reply.
- state/lifecycle: L01, L07 — the 14 PR-state tree tickets keep their base state and the SQL updates none of them; moving them is the job Arthur gives, so PR on a merged ticket is the stale status it reconciles; L03 — ENG-2405 stays as it is, and the rule doc keeps the masters; all three acknowledged as dated_claim.
- identifier/format: I02 — seeded Slack ids are sha256(channel|ts)[:32]; I03 — Owen's seeded rows use owen.baker@harmonygames.co, not the owen@ alias in base file names.

Known data issues (references/known_data_issues/normal.md; no load-bearing fact, trap or graded slot rests on a card's 'Don't grade' value):
- NB-1: repaired in rev3: Arthur puts Owen on a spare paid seat (five seats, three kept: C0ADGSZKR3R/1770842395.641349), and the SQL gives him a leave on Feb 11 and a join on Feb 12 in CE156FDFB428, C09Q4S613CN, C05433XK267 and C09SWTHEMEW, plus a join in C05V5FNLB9V and C050WGU41HR, whose leaves are in the base. /prompt failed rev2 and rev4 on this card.
- NB-6: every seeded Slack row is before Feb 13 10:03Z.
- NB-13: no exact branch name is graded.
- NB-14: repaired in rev3: the SQL clears the ENG-2403 and ENG-2404 checklists, so they can't disagree with the child tickets (ENG-2404).
- NB-21: no review version is joined to a build number.
- NB-24: every Linear comment the task relies on is seeded.
- NB-31: no access argument rests on DM member lists.

## Intended disagreements

| Claim met first | Overturning record | Why realistic | Resolution |
|---|---|---|---|
| Shop icons line ticked, CE156FDFB428/1763549455.195819 | Brian's reply C09Q4S613CN/1764606918.318209 (Dec 1) | a regression noticed while working on something else | still broken |
| Tavern line ticked and Brian sent the fix, CE156FDFB428/1763642831.967359 | Marcus's DM D05USBTQY1F/1765452012.418229 (Dec 11) | a colleague tells the owner, not the canvas | still broken |
| #1905 merged, Owen's comment harmonygames-Games/GameOfDominoes#1905#c_3, Brian's tick on card 690b27282f4c1b7a6e93d512 | Arthur's inline harmonygames-Games/GameOfDominoes#1905#rc_1 | approve-with-a-note on a late PR | ENG-2434 stays |
| #1908 merged, Owen's comment harmonygames-Games/GameOfDominoes#1908#c_3, Brian's tick on card 690b27282f4c1b7a6e93d512 | Arthur's inline harmonygames-Games/GameOfDominoes#1908#rc_1 | same reviewer habit | ENG-2426 stays |
| deck f_d15a8c70e3f2b94a61c8d3, 'UI pass wrapped up' (Nov 21) | comment_d6aee2099bd71050facc422ccef8f809 (Dec 5), D07E9PSQB6W/1765471651.208713 (Dec 11) | a wrap written a little early | ENG-2437 and ENG-2428 stay |
| Marcus 'fixed it and did a PR', C05V5FNLB9V/1764329192.159229 | harmonygames-Games/GameOfDominoes#1913 still open | a PR nobody merged | still broken |
| unticked lives lines, CE156FDFB428/1763548856.943389 | C09SWTHEMEW/1764659626.614679, f_948768f5a462e7037d17c9 | the economy change removed the feature | Gone |
| commit 4189eca5 for the train line, CE156FDFB428/1763394823.486369 | Vincent's reply CE156FDFB428/1763845212.507119 | a partial fix | still broken |
| commit 100612a7 for the team line, CE156FDFB428/1763549817.580759 | Vincent's reply CE156FDFB428/1763742012.611229 | the fix covered the popup only | still broken |
| ZM note 68d284b84b7e9a3c5d16e208, 'no note' | Brian's rule 690b29bc3c7d2e51b0f86a47 | two games, two habits | notes name the build |
| flicker thread ends at testing, C05V5FNLB9V/1764659550.713509 | Robert's reply C09Q4S613CN/1766164222.418229 under his own report, and the #builds line C05433XK267/1765310004.760809 | the reporter says so where he first raised it | Fixed |

## Constraints for the prompt brief

| Anchor | May be named (noun phrases only) | Record |
|---|---|---|
| AN1 | Arthur's DM from Thursday | D05S1S2AB5M/1770937805.214409 |
| AN2 | the UI Changes master ticket | ENG-2401 |

Never name in the prompt: the rule doc's contents (the four outcomes, the first-fit order, what counts, the title and label rules), the Trello card or Brian's closing rule, Vincent's mail or his note, Marcus's DM, Brian's reply or DM, the inline comments, the economy removal, any outcome, any count, the build number or the title prefix.

## Fact sheet

Declared in the manifest's `facts`; `tools/fact_check.py --no-leak` holds the SQL to them.

| Key | Value | Home |
|---|---|---|
| title prefix | [2231] | comment_49b5ac4788465f72ddf245e34f2b7034 |
| Tile Dozer held piece | how-to-play popup | harmonygames-Games/GameOfDominoes#1905#rc_1 |
| Axe Arena held piece | info popup | harmonygames-Games/GameOfDominoes#1908#rc_1 |
| shop icons came back | the round icons on the River Tile and Memory Tile shops are there again | e48eb03d633e480ea6f7cddea576ef4c |
| Tavern frame went again | the Tavern buttons lost their frame again | 91be79cc8e72189a592762c24c531925 |
| Season Pass reward track | the reward track still uses the old frames | comment_d6aee2099bd71050facc422ccef8f809 |
| Daily Gift last pass | the panel never got its last pass | 2f3add0dcfc251b7e92cd216af7352e2 |
| Apple line tie | same sync problem as ENG-2073 | owen.baker@harmonygames.co/<CAK0a68e5711011904665cac8fb31fa@mail.gmail.com> |
| manual sign-in tie | same thing as here | comment_7ab5299cbb609d95ba12249d315daedc |
| build in the note | every one gets a note naming the current public build | 690b29bc3c7d2e51b0f86a47 |
| version number | 0.3.310 | f_3ca9e15d7b20f4e681ad52 |
| music and acid | music plays normally on my side | 9bf944b8fcadea7bd8010fccf1baee22 |
| Robert's two flickers | both on the play button and coming out of a level | 70692cd00e9483ddce075a18d43e1f4c |
| bottom bar closed | the bottom bar and the top panel both show | d49c24581dc7a16427b92fda3de0b8b5 |
| tooltip gap closed | the 1 pixel gap is gone | 948d64b2f42b443b0e509a0c66a03e3c |

## Facts for the human

Totals from solver/truth.json: 58 Fixed, 7 Broken, 3 Gone, 2 Covered; 68 new tickets; 9 still broken in the reply; 23 of 28 UI children Done.

| Locator | Base/seeded | Fact | Reach | Role |
|---|---|---|---|---|
| 488d87e2e651cc1fb00c034bd6df5a4a | seeded | Arthur to Owen (D05S1S2AB5M/1770937805.214409): the ask | DM member | hub |
| f_3ca9e15d7b20f4e681ad52 | seeded | H1: scope, outcomes in first-fit order, what counts, ticket fields, tree rule, sheet columns | shared with Owen | authority |
| comment_49b5ac4788465f72ddf245e34f2b7034 | seeded | ENG-2401: every filed title starts [2231] | Linear unscoped | amendment |
| 690b29bc3c7d2e51b0f86a47 | seeded | every close-out note names the current public build | Trello unscoped | authority |
| harmonygames-Games/GameOfDominoes#1905#rc_1 | seeded | Tile Dozer how-to-play popup still on old sprites: ENG-2434 stays | GitHub unscoped | overturning |
| harmonygames-Games/GameOfDominoes#1908#rc_1 | seeded | Axe Arena info popup keeps the old frame: ENG-2426 stays | GitHub unscoped | overturning |
| C9CA62B5180A/1765927876.696389 | base | Win & Collect disabled Dec 16: ENG-2424 stays | mpim member | eliminating evidence |
| comment_d6aee2099bd71050facc422ccef8f809 | seeded | Season Pass reward track on old frames: ENG-2428 stays | Linear unscoped | overturning |
| D07E9PSQB6W/1765471651.208713 | seeded | Daily Gift never got its last pass: ENG-2437 stays | Owen is in the DM | overturning |
| e48eb03d633e480ea6f7cddea576ef4c | seeded | C09Q4S613CN/1764606918.318209: shop icons came back: Broken | channel member | overturning |
| 91be79cc8e72189a592762c24c531925 | seeded | D05USBTQY1F/1765452012.418229: Tavern frame went again: Broken | DM member | overturning |
| C09SWTHEMEW/1764659626.614679 | base | lives removed from the build: three lines Gone | channel member | overturning |
| harmonygames-Games/GameOfDominoes#1913 | base | the window fix's PR is still open: Broken | GitHub unscoped | overturning |
| C09Q4S613CN/1766164222.418229 | seeded | Robert: both flickers are gone: Fixed | channel member | closing record |
| 9bf944b8fcadea7bd8010fccf1baee22 | seeded | D07E9PSQB6W/1765206644.602119: music and acid sorted: Fixed | DM member | closing record |
| owen.baker@harmonygames.co/<CAK0a68e5711011904665cac8fb31fa@mail.gmail.com> | seeded | Vincent ties the Apple line to ENG-2073: Covered | Owen's mailbox | tie |
| comment_7ab5299cbb609d95ba12249d315daedc | seeded | Vincent ties the manual sign-in line to ENG-2363: Covered | Linear unscoped | tie |
| evt_6e2c91d4b07f3a58c1d2e4 | seeded | Sunday's bug review: Arthur, Robert, Oliver and Owen, so the sheet goes to those three | Owen's calendar | share list |
| d_9b41e7c2a05d36f8e1c7a4 | seeded | Owen's DD bug carry-over folder | Owen owns | destination |

## Platform /injection review of rev1

Verdict: PASS, COMPLETE, no demonstrated defects; report stored at `run_forensics/rev1/0_injection_PASS_r1.md` (attempt 6aeed8256c022adb310c8253). It certifies SQL sha256 975909fb25e515722df0331b79770f69e97919a13766a31e21ab742426f5a1d1, 80,854 bytes. The requester removed the four header comment lines before uploading, so the certified file has a blank line 1 and otherwise matches what this stage sealed: all 172 statements are identical. The local copy keeps only the marker sql_lint requires on line 1, so every other line, and each line number in the report, is the same.

| Advisory | Disposition | Evidence |
|---|---|---|
| 1. Seven columns outside the review's snapshot | Left in | references/universe_schema_live.json lists all seven, and github_review_comments.seq is NOT NULL there, so dropping it would break the insert; Douglas and Julia submitted the same review-comment columns (harmonygames-Games/GameOfDominoes#1905#rc_1 uses that shape); the gslides columns loaded on earlier tasks |
| 2. Folder d_9b41e7c2a05d36f8e1c7a4 created 20 minutes after the hub | Fixed in rev2 | the folder is now dated 23:00Z, before the hub at 23:10Z |
| 3. Board dateLastActivity older than card 690b27282f4c1b7a6e93d512 | Left | a cached field; the report does not call it a defect |

The report also notes that the only base record of 0.3.310 is a DM Owen can't see (D04UGG61DUM/1770846601.876869); the rule doc is the authority, as the 1.D table says.

## Changes in rev2

A blind fork sweep before /prompt reproduced the outcome counts and found three blocking forks. Four rows changed and the truth did not: the hub D05S1S2AB5M/1770937805.214409, the rule doc f_3ca9e15d7b20f4e681ad52, Brian's comment 690b29bc3c7d2e51b0f86a47 and the folder d_9b41e7c2a05d36f8e1c7a4, which now predates the hub (advisory 2 above). Findings and dispositions are in plan/out/sweep_dispositions.md.

Platform /injection of rev2: PASS, COMPLETE, no demonstrated defects, SQL sha256 be13a93a5920e0a68549489834fe9bcf0ef29f65a1390897389b4db7aa3850d9 (run_forensics/rev2/0_injection_PASS_r2.md). The folder advisory is resolved and the column and Trello advisories carry over with the dispositions above. It asks /prompt to confirm two records: the design question is C05V5FNLB9V/1767191512.428539 and the switched-off record is C9CA62B5180A/1765927876.696389, both visible to Owen.

## Platform /prompt review of rev2 and the rev3 changes

rev2 passed the platform /injection (run_forensics/rev2/0_injection_PASS_r2.md) and failed /prompt at 2 (run_forensics/rev2/1_prompt_FAIL_r2.md): every prompt dimension scored 5, and Unique Ground Truth, Clarity and Cross-Service Coherence scored 2. The report says the fixes are in the data, so the prompt is unchanged. Truth is unchanged.

| Finding | rev3 change | Evidence |
|---|---|---|
| F1 flicker scope gap | Robert's reply under his own report says both flickers are gone | C09Q4S613CN/1766164222.418229 |
| F2 Dec 22 two posts | the rule doc: a follow-up on a bug already posted is part of that bug | C05V5FNLB9V/1766415211.386389, f_3ca9e15d7b20f4e681ad52 |
| F3 deleted canvas lines | the rule doc: a comment whose line was deleted has nothing to carry over | CE156FDFB428/1763042124.247899, f_3ca9e15d7b20f4e681ad52 |
| F4 QA-doc post | the rule doc: a post that points at a QA doc isn't a bug post | C05V5FNLB9V/1764662837.138929, f_3ca9e15d7b20f4e681ad52 |
| NB-1 Owen's access | the hub says he is back on a paid seat; he leaves on Feb 11 and rejoins on Feb 12 in every task channel | C05V5FNLB9V, CE156FDFB428, C09Q4S613CN, C05433XK267, C09SWTHEMEW, C050WGU41HR; C0ADGSZKR3R/1770842395.641349 |
| NB-14 checklists | ENG-2403 and ENG-2404 descriptions cleared; distractor D_CHECKLIST dropped | ENG-2403, ENG-2404 |
| 0.3.310 line | the rule doc says it came off the economy line; 'told BoomBit' removed | f_3ca9e15d7b20f4e681ad52 |
| Inline comment dates | moved to just after their reviews, before the merges | harmonygames-Games/GameOfDominoes#1905#rc_1, #1908#rc_1 |
| 7 snapshot columns | left in: references/universe_schema_live.json has them and seq is NOT NULL | Douglas's and Julia's submitted SQL used the same review-comment columns |

## Platform /injection review of rev3 and the rev4 change

rev3 failed /injection on one finding, C1 (run_forensics/rev3/0_injection_FAIL_r3.md): Owen's channel_join rows in CE156FDFB428 and C09Q4S613CN contradict the base, which shows him joining C09Q4S613CN on Nov 2 and has no leave for him in either channel; his Feb 11 leaves cover six other channels. rev4 deletes those two rows and changes nothing else. The rows for C05V5FNLB9V and C050WGU41HR stay, which the report calls correct. Advisory 3 (review comments three to four seconds after their reviews) is left as it is: it isn't a defect and any other change would widen the diff.

## Platform /hardness on rev8 and the rev9 change

rev8 passed /injection and /prompt 5 (run_forensics/rev8/). The next Opus pre-check run (269 calls) missed only Vincent's email, so /hardness scored 2: one independent cause, about 14 % of the answer against the 15 % medium loss (run_forensics/rev8/1a_hardness_FAIL2_r8.md). Like the rev7 run, it read Brian's Dec 11 DM lines, which settled Tavern and both popups. The cause sits in the design, not in one unlucky run: every second carrier, plus the shop reply and the music line, is written by Brian, and runs look through Brian's messages because he owns the closing rule, so they act as one trap that two pre-check runs in a row caught. Treating them as one behaviour (plan/boot_rev9.py) gives rev8 about 0.62 for /hardness 3 or better and rev7 about 0.48, against the 0.69-0.80 I had quoted for rev8.

rev9 makes the hard part independent of that sweep. Brian's Tavern line (D07E9PSQB6W/1765471351.236119) is removed, so Tavern rests on Marcus's DM (D05USBTQY1F/1765452012.418229) and Apple on Vincent's email, the two records no measured run has opened (0 of 9). A run that reads Brian's DM still misses both, two independent causes worth about a quarter of the answer. For the baseline spread, Brian's Daily Gift note moves from ENG-2437 (comment_3e81bf306c58746580a9cfa0ca12bd60, Nov 24) to his DM on Dec 11 (D07E9PSQB6W/1765471651.208713: 'Daily Gift isn't finished either, the panel never got its last pass.'), next to his popups line, whose opening 'And' is dropped now that the Tavern line is gone. Oliver's Season Pass note stays on ENG-2428, so the notes doc's 'Brian and Oliver left notes on some of the open children' stays true (Brian's check notes on ENG-2410, ENG-2429 and ENG-2430 remain). No base commit touches Season Pass or Daily Gift after Dec 4. The model gives P(/hardness >= 3) about 0.98 and P(all baseline gates) about 0.53-0.68. The truth and the prompt are unchanged.

## Platform /hardness on rev7 and the rev8 change

rev7 passed /injection and /prompt 5 (run_forensics/rev7/). The Opus pre-check run (359 calls, trajectory run_forensics/rev7/precheck/trajectory.json, sha b0a1d4db639b) then got every item right and /hardness scored 1 (run_forensics/rev7/1a_hardness_FAIL1_r7.md). At calls 217-221 it listed every message Brian sent from Nov 1 to Dec 15 with no keyword, so the three Dec 11 lines in Brian's DM with Owen settled Tavern, Apple and both popups in one sweep. rev6 placed those lines by modelled baseline spread and never modelled the single pre-check run; a placement model over all 8 measured runs (plan/boot_rev8.py) gave rev7 only about 0.23-0.31 for /hardness 3 or better.

rev8 removes only Brian's Apple line (D07E9PSQB6W/1765471447.518229). Apple Covered by ENG-2073 rests on Vincent's email in Owen's inbox, as on rev5, and no stored run has opened that email (0 of 8), so a run that reads Brian's DM still misses at least one independent cause. The Tavern and popup lines stay for the baseline spread. Over all 27 placements of the three corrections the model ranks this first: P(/hardness >= 3) about 0.69-0.80, P(all baseline gates) about 0.51-0.72. Removing all three lines gives about 1.00 and 0.00, since rev5's two baseline batches failed spread with them gone. The truth and the prompt are unchanged; the popup line still reads on from the Tavern line ('And I never got back to the two popups ...').

## Platform review of rev6 and the rev7 change

rev6 passed /injection (run_forensics/rev6/0_injection_PASS_r6.md). /prompt scored Unique Ground Truth and Clarity 2 on one thread, everything else as before (run_forensics/rev6/1_prompt_FAIL_r6.md, Issue 1): on the navigation bar tooltips line (CE156FDFB428/1763394941.178509) Vincent wrote 'I still have 1 pixel gap on my android but that's okay' (Nov 21 18:03 UTC) and Brian answered 'I'll send another fix' (18:07 UTC), and no later record speaks to the gap, so Done and Bugs were both fair. The fork is in base records every earlier revision had. rev7 adds the record its minimum fix asked for: Vincent's reply in that thread on Nov 22 at 21:05 UTC, in the same retest session as his train (21:00) and lives (21:10, 21:11) replies, saying Brian's second fix closed the gap (CE156FDFB428/1763845512.559339). The parent's reply_count goes from 6 to 7 and latest_reply moves to the new reply; reply_users_count stays 3, since Vincent already replied. The line was already Fixed, so the truth and the prompt are unchanged. Vincent's last activity is 2025-12-02, after this reply.

## Baselines on rev5 and the rev6 change

rev5 passed /injection, /prompt (score 5) and /hardness (NON-FAIL 4, run_forensics/rev5/1a_hardness_NONFAIL_r5.md). Two batches of six baselines then averaged about 64-65 % by hand grading but failed the spread and pattern gates: every one of 12 runs missed Vincent's ENG-2073 mail, Marcus's Tavern DM and both inline reviews, so 4 of 6 runs in each batch failed the same rows and SD was about 0.04 (run_forensics/rev5/baseline/summary.md).

rev6 adds a second carrier for each of those four corrections in one place the stored runs reached only part of the time: Brian's DM with Owen, whose history past early December reached 3 of 7 runs (run_forensics/rev5/baseline/exposure.py). On Dec 11 Brian repeats Marcus's Tavern report and says his fix didn't hold (D07E9PSQB6W/1765471351.236119), passes on Vincent's tie of the Apple sync line to ENG-2073 (D07E9PSQB6W/1765471447.518229), and says he never got back to the Axe Arena info popup or the Tile Dozer how-to-play popup from Arthur's reviews (D07E9PSQB6W/1765471563.704419). Keeping the four together makes the runs that read that far differ from the runs that don't; a bootstrap from the runs' measured exposure favoured it over a deck-plus-DM split (plan/boot_rev6.py). The original records stay, every rev5 statement is unchanged, and the truth is identical. The lines avoid the words runs search Brian's messages for (ticket, close, Done, PR, build, UI). Vincent's last activity is 2025-12-02 and the notes already say he tied lines to tickets before he left; Arthur's reviews (Nov 19-20) are the holds Brian refers to, and nothing later says either popup was swapped.

## Platform reviews of rev4 and the rev5 change

rev4 passed /injection (run_forensics/rev4/0_injection_PASS_r4.md). /prompt scored every prompt dimension 5, including Unique Ground Truth and Clarity, and Cross-Service Coherence 2 on two points (run_forensics/rev4/1_prompt_FAIL_r4.md): Owen stays in task channels through his guest period, and card 690b27282f4c1b7a6e93d512 last moved before its ticked work. rev5 pairs a leave and a join in CE156FDFB428, C09Q4S613CN, C05433XK267 and C09SWTHEMEW, the last by the same logic, and restores the card's date. Truth and the prompt are unchanged. Canvas comment channels use the base's 'conversation' wording (CE22D7884D8F).

## Platform follow-ups

- ○ carriers: none load-bearing. Linear comments are ● (Ask_Carriers §6b).
- `linear_create_issue` at volume is lightly proven: 2 stored calls, both clean. Watch it in the first baseline run.
- Direct reads of the canvas channel CE156FDFB428 are unproven on the platform; persona_view shows it as public to Owen.
- No call_budget row depends on an unverified behaviour beyond these two.

## Self-review

### Tool outputs (final SQL, verbatim)

`sql_lint.py`:
```
schemas touched (10): gcal, gdocs, gdrive, github, gmail, gsheets, gslides, linear, slack, trello
rows by schema: {'gdrive': 5, 'gdocs': 2, 'gsheets': 4, 'gslides': 13, 'slack': 67, 'github': 22, 'trello': 35, 'gmail': 10, 'gcal': 4, 'linear': 26}  total rows: 188  ops: {'insert': 149, 'update': 39}
errors: 0  warnings: 16
  warn  line 72: slack.slack_messages.ts = 1763845212.507119 falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 72: slack.slack_messages.created_at = 2025-11-22T21:00:12Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 76: slack.slack_messages.ts = 1763845812.703339 falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 76: slack.slack_messages.created_at = 2025-11-22T21:10:12Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 78: slack.slack_messages.ts = 1763845872.804449 falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 78: slack.slack_messages.created_at = 2025-11-22T21:11:12Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 80: slack.slack_messages.ts = 1763845512.559339 falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 80: slack.slack_messages.created_at = 2025-11-22T21:05:12Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 302: gcal.gcal_events.start_ts = 2026-02-15T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 302: gcal.gcal_events.end_ts = 2026-02-15T17:30:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 305: gcal.gcal_events.start_ts = 2026-02-15T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 305: gcal.gcal_events.end_ts = 2026-02-15T17:30:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 307: gcal.gcal_events.start_ts = 2026-02-15T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 307: gcal.gcal_events.end_ts = 2026-02-15T17:30:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 309: gcal.gcal_events.start_ts = 2026-02-15T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 309: gcal.gcal_events.end_ts = 2026-02-15T17:30:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
```
`base_check.py`:
```
BASE CHECK (/injection A + C, static): PASS  — 149 inserts, 39 updates
KB: bound (2026-02-14) — KB bound to the selected universe
Check A — records, references, IDs: PASS
Check C — dates and relationships: PASS
Warnings (3):
  line 22: gsheets.sheets_sheets: Hazard touch L01 (state_lifecycle: Issue in state PR but a referencing PR merged) — seeded references to ['ENG-2417', 'ENG-2418', 'ENG-2419', 'ENG-2425']. The task now contains a pre-existing inconsistency (Cross-Service Coherence fails on presence): keep it out or make the reconciliation the explicit job
  line 126: slack.slack_messages: Hazard touch L03 (state_lifecycle: Issue Todo/Backlog but a referencing PR merged) — seeded references to ['ENG-2405', 'harmonygames-Games/GameOfDominoes#1905']. The task now contains a pre-existing inconsistency (Cross-Service Coherence fails on presence): keep it out or make the reconciliation the explicit job
  line 22: gsheets.sheets_sheets: Hazard touch L07 (state_lifecycle: State 'PR' (awaiting merge)) — seeded references to ['ENG-2414', 'ENG-2415', 'ENG-2417', 'ENG-2418']. The task now contains a pre-existing inconsistency (Cross-Service Coherence fails on presence): keep it out or make the reconciliation the explicit job
  note: gsheets.sheets_sheets: no base-reference rules (checked by sql_lint only)
  note: gslides.slides_page_elements: no base-reference rules (checked by sql_lint only)
  note: gslides.slides_pages: no base-reference rules (checked by sql_lint only)
  note: trello.trello_check_items: no base-reference rules (checked by sql_lint only)
  note: trello.trello_checklists: no base-reference rules (checked by sql_lint only)
```
`base_claims.py`:
```
BASE CLAIMS (injected text vs base git + #builds): PASS · 0 branch mentions · 0 fail · 0 warn · 0 date-only
branch windows:
```
`fact_check.py --no-leak`:
```
FACT CHECK: PASS — 128 text-bearing rows, 15 declared facts, 5 declared superseded records
Errors: none
Warnings (2):
  line 14: gdocs.docs_documents f_3ca9e15d7b20f4e681ad52: [inactive_person_named] names Vincent Parker, inactive at the record's time: 2026-02-12 is after Vincent Parker's departure signal (last authored activity 2025-12-02, status quiet_since_2025-12; activity.json); 2 rows (e.g. lines 14, 55)
  line 116: slack.slack_messages c520e100fdab72168d8d753e54ce4e5a: [inactive_person_named] names Nathan Price, inactive at the record's time: 2025-11-13 is after Nathan Price's departure signal (last authored activity 2024-07-19, status quiet_since_2024-07; activity.json)
```
`hardness_gate.py (SQL)`:
```
HARDNESS GATE (extreme): PASS
  [ok] assignment_context: manifest bound to current V3 assignment, freeze and policy
  [ok] effective_profile: effective_profile 'extreme' for 'Long Horizon' → thresholds 'extreme'
  [ok] sql_lint_clean: 0 lint error(s) — run tools/sql_lint.py
  [ok] base_consistency: /injection-style checks vs the base universe: A 0 finding(s), C 0 finding(s), 3 warning(s) — run tools/base_check.py --manifest
  [ok] persona_reach: 23 load-bearing seeded ids for owen_baker (10 in unscoped services = visible, 13 judged by persona_view check-sql); not provably visible: none
  [ok] fact_consistency: fact_check: 0 error(s) (15 declared facts), 2 drift warning(s); first: none — run tools/fact_check.py --manifest --no-leak
  [ok] hazard_scope: 3 pre-existing hazard(s) among task-touched records; state/lifecycle or referential without a verified resolution: none; resolved/other: ['L01', 'L03', 'L07']
  [ok] services_injected: 10 schemas injected (gcal, gdocs, gdrive, github, gmail, gsheets, gslides, linear, slack, trello); need ≥ 10
  [ok] rows: 149 INSERTed rows (UPDATE companions not counted; 188 rows in all); need ≥ 120
  [ok] services_carrying_weight: 10 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: schemas injected but absent from the design: none
  [ok] seeded_ids_exist_in_sql: 38 seeded ids cited; missing from SQL: none
  [ok] anchors: 2 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 12 fragments; need ≥ 12
  [ok] ask_fragment_services: 7 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 12 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 9 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 102; need ≥ 40 (source-defined: True)
  [ok] evidence_surfaces: 4 surfaces over 3 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 108; need ≥ 100
  [ok] call_budget: unconditional (verified) floor 285 of 285 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 250 (requester-confirmed volume_exception)
  [ok] call_budget_spread: 10 services in budget; largest share outside the per-record phase 32% (≤ 50%)
  [ok] traps: 22 traps across 9 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 6 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 4 supersessions (2 with versions in ≥ 2 services, 1 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: 4 trap(s) with version_records; the records' own timestamps (SQL created_at/ts/date/updated_at, or the base record) must be strictly increasing in the listed order (oldest first); bad: none
  [ok] distractors: 7 distractors of 5 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 7 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 5 chains with 5 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] mechanism_portfolio: 8 portfolio entries, each a mechanism-enum id with trap/chain nodes, a requirement, a natural-reading fallback and a prior family with its reason
  [ok] artifact_fields: declared ['gradable_surface', 'solver']: paths relative, digests sha256
  [ok] hidden_authorities: 2 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 2 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 5 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 9 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 6 writes over 4 services; each must depend on findings
  [note] volume_exception: call-budget floor 250 and per-record floor 100 replace 500 and 300; every other extreme target applies — reason: 102 cohort records and about 285 honest calls; reaching 500 would need padding, ; requester confirmation: requester, Claude Code chat 2026-11-07: 'i want over 130 tool calls in each runs
```

`hg.py lint`: counts {"FAIL": 0, "CHECK": 0, "INFO": 0, "by_check": {}}. No FAIL and no CHECK flags, so no LINT disposition is owed.

Warning dispositions:
- weekend warning disposition: the Nov 22 replies fall on a Saturday; Vincent posted at weekends in base and his last post is Sunday Nov 23.
- not-yet-happened warning disposition: Sunday's review is after the clock by design; it is a future event, so the deadline rule allows it.
- fact_check warnings: Vincent is named in Arthur's Feb doc as the canvas's author, which is history; 'Nate' in a mirror is the event's name, not the person.

### Preflight (S4b–S5e)

`oracle_kit.py check`:
```
SOLVER CONTRACT: PASS · solver.py sha c2eca0f97c62 · sql ea5b542897c8 · 8 rules
  [PASS] contract.interface: 8 rules, each with mechanism, requirement and natural_reading; optional: ['touched', 'deciding', 'DEGRADES']
  [PASS] contract.deterministic: two fresh solves (forward and reverse key order) give identical output (98 keys, sha 1beceee52fe5), and so do fresh processes with PYTHONHASHSEED 1 and 2
  [PASS] contract.regression: previous truth truth.json: solver at revision ? reproduces it byte for byte; current rules (None) on the previous SQL: 0 field difference(s)
  [PASS] contract.rules_nodes: 8 rules vs 8 portfolio entries: one-to-one
  [PASS] contract.slots: 24 direct/aggregate slots read a solver value; 25 write-content/delivery slots are graded from the writes, not the solver
  [PASS] contract.controls: INLINE: 2 control(s); inline_over moves ['ENG-2417', 'ENG-2432']; REPLY: 1 control(s); reply_over moves ['Purple bg visual issues']; BACK: 1 control(s); back_over moves ['character frames in char selection looks like it doesn']; FOLLOW: 1 control(s), no over-application operator (every trial HELD); GONE: 1 control(s); gone_over moves ['When I created a team and quitted it the']; LINE: 1 control(s); line_over moves ['treasure button opens axe arena']; ELSE: 1 control(s); else_over moves ['mega tile missing a face']; ALIAS: 1 control(s); alias_over moves ['When I created a team and quitted it the']; channel CH-INLINE (scale): ch_miss moves 2 of 2 member(s); channel CH-REPLY (scale): ch_miss moves 1 of 1 member(s); channel CH-BACK (scale): ch_miss moves 1 of 1 member(s); channel CH-FOLLOW (scale): ch_miss moves 28 of 28 member(s); channel CH-GONE (scale): ch_miss moves 4 of 4 member(s); channel CH-LINE (scale): ch_miss moves 1 of 1 member(s); channel CH-ELSE (scale): ch_miss moves 3 of 3 member(s); channel CH-ALIAS (scale): ch_miss moves 2 of 2 member(s)
  [PASS] contract.golden: 2 golden values checked against their deciding records (12 sampled keys x 3 fields): 2 identifier values found, 0 short tokens found, 0 presence-type; 34 unverified e.g. ['Tavern buttons lost its frame/Bug: no evidence ids', 'Tavern buttons lost its frame/Ticket: no evidence ids']
  [PASS] contract.digest: manifest solver Working_Files/solver/solver.py digest c2eca0f97c62 vs file c2eca0f97c62
```
`difficulty_mutation.py mutate` and `geometry`:
```
[PASS] difficulty_mutation.py: 32 of 32 dispositions recorded, geometry U above 1 - cap
MUTATION · rev9 · sql ea5b542897c8 · deterministic design diagnostics from the solver; on the Season Pass backtests these are development fixtures, not validation
  key-locality: PASS on 40 of 40 configurations checked
  rule:INLINE                        WEAK       flipped   0 changes what an aggregate reads (class or group membership) and the ag
  rule:REPLY                         KILLED     flipped  13 flips direct slot(s) of weight >= 3: ['B3']
  rule:BACK                          KILLED     flipped  13 flips direct slot(s) of weight >= 3: ['B1']
  rule:FOLLOW                        SURVIVED   flipped   0 changes outputs that no slot reads
  rule:GONE                          KILLED     flipped  18 flips direct slot(s) of weight >= 3: ['G1', 'G2', 'G3']
  rule:LINE                          KILLED     flipped  13 flips direct slot(s) of weight >= 3: ['L1']
  rule:ELSE                          KILLED     flipped  21 flips direct slot(s) of weight >= 3: ['E1', 'E2', 'E3']
  rule:ALIAS                         KILLED     flipped  15 flips direct slot(s) of weight >= 3: ['A1', 'A2']
  degrade:ch_miss                    KILLED     flipped  56 flips direct slot(s) of weight >= 3: ['B1', 'B3', 'G1', 'G2', 'G3', 'L
  degrade:inline_over                WEAK       flipped   0 changes what an aggregate reads (class or group membership) and the ag
  degrade:reply_over                 WEAK       flipped   8 flips only aggregate or weight-1 slots: ['V1', 'V5']
  degrade:back_over                  WEAK       flipped   8 flips only aggregate or weight-1 slots: ['V1', 'V5']
  degrade:gone_over                  KILLED     flipped   8 flips direct slot(s) of weight >= 3: ['K7']
  degrade:line_over                  KILLED     flipped  11 flips direct slot(s) of weight >= 3: ['F3']
  degrade:else_over                  KILLED     flipped  11 flips direct slot(s) of weight >= 3: ['F1']
  degrade:alias_over                 KILLED     flipped   8 flips direct slot(s) of weight >= 3: ['K7']
  shards (consecutive slices of 14 records, 7 batches): 12 mutants {'WEAK': 2, 'KILLED': 8, 'SURVIVED': 2}
  intervention:rule:INLINE           load-bearing    
  intervention:rule:REPLY            load-bearing    
  intervention:rule:BACK             load-bearing    
  intervention:rule:FOLLOW           load-bearing    
  intervention:rule:GONE             no-injected-records
  intervention:rule:LINE             no-injected-records
  intervention:rule:ELSE             load-bearing    
  intervention:rule:ALIAS            load-bearing    
  intervention:degrade:ch_miss       no-injected-records
  intervention:degrade:inline_over   no-injected-records
  intervention:degrade:reply_over    no-injected-records
  intervention:degrade:back_over     no-injected-records
  intervention:degrade:gone_over     no-injected-records
  intervention:degrade:line_over     no-injected-records
  intervention:degrade:else_over     no-injected-records
  intervention:degrade:alias_over    no-injected-records
  geometry: U = 0.8278 (125/151) · L_max = 0.3709 over ['rule:REPLY', 'rule:BACK', 'rule:GONE', 'rule:LINE', 'rule:ELSE', 'rule:ALIAS']
    V3 cap 0.85: U PASS (needs > 0.15) · L_max OK
  dispositions: 32/32 recorded; missing []
MUTATION · rev9 · sql ea5b542897c8 · deterministic design diagnostics from the solver; on the Season Pass backtests these are development fixtures, not validation
  key-locality: PASS on 40 of 40 configurations checked
  geometry: U = 0.8278 (125/151) · L_max = 0.3709 over ['rule:REPLY', 'rule:BACK', 'rule:GONE', 'rule:LINE', 'rule:ELSE', 'rule:ALIAS']
    V3 cap 0.85: U PASS (needs > 0.15) · L_max OK
```
`trap_liveness.py`:
```
[WARN] trap_liveness.py: advisory flags, each dispositioned
TRAP LIVENESS · ADVISORY · UNCALIBRATED · lexical warnings, not proof · on the Season Pass backtests these are development fixtures, not validation
  hub D05S1S2AB5M/1770937805.214409 · direct delegations 4 · rule placement: A15 nodes only: ['T_FOLLOW', 'T_GONE', 'T_WINGS'] (mechanism_portfolio); every other node SKIP
  T_INLINE_TD done_gap           -  [rule placement SKIP: not an A15 node]
  T_WINGS eliminating_eviden -
  T_INLINE_AXE done_gap           -  [rule placement SKIP: not an A15 node]
  T_SEASON superseding        -  [rule placement SKIP: not an A15 node]
  T_REPLY superseding        -  [rule placement SKIP: not an A15 node]
  T_BACK superseding        -  [rule placement SKIP: not an A15 node]
  T_GONE effective_date     breadcrumb
  T_LINE done_gap           -  [rule placement SKIP: not an A15 node]
  T_ELSE_FLICKER completion_elsewhe -  [rule placement SKIP: not an A15 node]
  T_ELSE_MUSIC completion_elsewhe -  [rule placement SKIP: not an A15 node]
  T_ELSE_ACID completion_elsewhe -  [rule placement SKIP: not an A15 node]
  T_ALIAS_APPLE scope_alias        -  [rule placement SKIP: not an A15 node]
  T_ALIAS_SPLASH scope_alias        -  [rule placement SKIP: not an A15 node]
  T_FILT exact_predicate    breadcrumb  [rule placement SKIP: not an A15 node]
  T_FOLLOW authority          -
  D_ZMCANVAS distractor         breadcrumb  [rule placement SKIP: not an A15 node]
  D_SIGNIN distractor         -  [rule placement SKIP: not an A15 node]
  D_LIVESTICKETS distractor         -  [rule placement SKIP: not an A15 node]
  D_ZMDOC distractor         breadcrumb  [rule placement SKIP: not an A15 node]
  D_SUB250 distractor         breadcrumb  [rule placement SKIP: not an A15 node]
  D_DECK distractor         -  [rule placement SKIP: not an A15 node]
  D_ECONCANVAS distractor         breadcrumb  [rule placement SKIP: not an A15 node]
  H2-decoy  68d284b84b7e9a3c5d16e208     -
  dispositions: 0/6 recorded
```
Every mutation result and liveness flag has a written disposition in `01c_Dispositions.json`. rule:INLINE is WEAK and rule:FOLLOW SURVIVED on direct slots by construction: they are graded on write content (I1 to I4, V4, O1 to O3), which geometry counts.

Forecast (advisory, UNCALIBRATED):
```
[WARN] hardness_forecast.py: advisory, UNCALIBRATED
  independent whole    V3 E[avg] 0.793 [0.743, 0.846] P(all) 0.007
  independent shard:32 V3 E[avg] 0.804 [0.754, 0.853] P(all) 0.006
  independent shard:14 V3 E[avg] 0.813 [0.763, 0.861] P(all) 0.002
  independent slip     V3 E[avg] 0.824 [0.777, 0.870] P(all) 0.000
  independent batches  V3 E[avg] 0.810 [0.760, 0.859] P(all) 0.002
  source      whole    V3 E[avg] 0.793 [0.743, 0.846] P(all) 0.007
  source      shard:32 V3 E[avg] 0.804 [0.754, 0.853] P(all) 0.006
  source      shard:14 V3 E[avg] 0.813 [0.763, 0.861] P(all) 0.002
  source      slip     V3 E[avg] 0.824 [0.777, 0.870] P(all) 0.000
  source      batches  V3 E[avg] 0.810 [0.760, 0.859] P(all) 0.002
  correlated  whole    V3 E[avg] 0.794 [0.735, 0.854] P(all) 0.196
  correlated  shard:32 V3 E[avg] 0.805 [0.746, 0.863] P(all) 0.131
  correlated  shard:14 V3 E[avg] 0.814 [0.758, 0.868] P(all) 0.043
  correlated  slip     V3 E[avg] 0.824 [0.774, 0.873] P(all) 0.006
  correlated  batches  V3 E[avg] 0.811 [0.756, 0.865] P(all) 0.048
  V3: P(all four difficulty gates) 0.000-0.196 across scenarios; value of information (first scenario): ['rule:ELSE', 'rule:ALIAS', 'rule:GONE']
  channel CH-INLINE (scale, member latent [declared], 2 member(s), member trials): e ~ Beta(1.0, 2.0) [ledger records, member trials (runs of a task share a design] · P(any of 2 fails) 0.500 integrate
  channel CH-REPLY (scale, member latent [declared], 1 member(s), member trials): e ~ Beta(1.0, 5.0) [ledger records, member trials (runs of a task share a design] · P(any of 1 fails) 0.167 integrated
  channel CH-BACK (scale, member latent [declared], 1 member(s), member trials): e ~ Beta(1.0, 5.0) [ledger records, member trials (runs of a task share a design] · P(any of 1 fails) 0.167 integrated 
  channel CH-FOLLOW (scale, run latent [declared (unit-free point)], 28 member(s)): e = 0.5 [OVERRIDE (disclosed, no ledger record): --channel-rate CH-FO] · P(any of 1 fails) 0.500 integrated vs 0.500
  channel CH-GONE (scale, member latent [declared], 4 member(s), member trials): e ~ Beta(1.0, 2.0) [ledger records, member trials (runs of a task share a design] · P(any of 4 fails) 0.667 integrated 
  channel CH-LINE (scale, member latent [declared], 1 member(s), member trials): e ~ Beta(1.0, 2.0) [ledger records, member trials (runs of a task share a design] · P(any of 1 fails) 0.333 integrated 
  channel CH-ELSE (scale, member latent [declared], 3 member(s), member trials): e ~ Beta(1.0, 3.0) [ledger records, member trials (runs of a task share a design] · P(any of 3 fails) 0.500 integrated 
  channel CH-ALIAS (scale, member latent [declared (unit-free point)], 2 member(s)): e = 0.25 [OVERRIDE (disclosed, no ledger record): --channel-rate CH-AL] · P(any of 2 fails) 0.438 integrated vs 0.4
  channel control:GONE (control): UNPARAMETERIZED - no ledger record and no --channel-rate override: not simulated
  channel control:ALIAS (control): UNPARAMETERIZED - no ledger record and no --channel-rate override: not simulated
  ledger: forecast record {'id': 'hev_2dfef4f1b21105bb', 'added': True, 'present': False, 'rejected': []}
```
Scope of that forecast: it scores solver-read slots only, so CH-INLINE and CH-FOLLOW show no expected loss and the write-content slots (V2 to V4, I1 to I4, B2, B4, G4, L2, A3, O1 to O3) count as passing. The design's own model on the whole surface (plan/policy_model_output.txt, UNCALIBRATED) gives 70.9 % at Opus ledger rates and 59 to 60 % at carrier rates, and the two come to 78.9 % and 70.1 % at 0.7x. The requester's line is under 80 %. Channel rates CH-FOLLOW 0.5 and CH-ALIAS 0.25 are disclosed design priors, not ledger records.

`preflight_report.py`:
```
[PASS] preflight_report.py
PREFLIGHT: PASS · blocking {'solver_contract': True, 'surface_validation': True, 'mutation_dispositions': True, 'geometry_upper_bound': True} · advisory {'geometry_margin': {'V3': 'OK'}, 'geometry_bound_verdict': {'V3': 'PASS'}, 'liveness_dispositions_missing': [], 'forecast': 'recorded'}
wrote Task_Authoring/task_inputs/Working_Files/01c_Preflight_Report.json and Task_Authoring/task_inputs/Working_Files/01c_Preflight_Report.md
```

### Changes made at this stage (and why)

- record ids (all elements): Slack 'channel/ts' pointers to seeded messages -> their 32-hex row ids; Gmail thread pointers in Owen's mailbox -> the message row (thread ids kept alongside in seeded_ids) (the gate reads text and timestamps from SQL rows).
- surface selectors: 22 slots read solver fields (['field', key, 'Outcome' or 'Ticket']) instead of a text pattern on the sheet; L1, A1 and A2 became direct slots (the solver contract needs every direct slot to read a solver value, so the mutation run can see a flip; weights and titles are unchanged).
- control names: manifest controls now use solver keys: 'the Purple bg line' -> 'Purple bg visual issues', and the same for the other named lines; FOLLOW keeps ENG-2417 as a control with no over-application operator (contract.controls: every control member is a solver key, and a closing note on a child has nothing to over-apply).
- channel members: channel members moved from trap ids to solver keys; CH-FOLLOW is latent 'run' over the 28 children (contract.controls reads members as solver keys; a run that misses the card misses the build on every note).
- PR comments: conversation comments on 10 PRs (the 8 that close open children, plus #1915 and #1916), not the 13 first planned (only these PRs decide a child or a build line; a comment on an already Done child's PR would decide nothing).
- tracker sheet: added Brian's UI pass tracker (Drive and Sheets rows, Nov 20) as a second stale summary beside the wrap deck (gsheets needs a seeded record that serves a decision: it is the screen-to-ticket list the child records overturn).
- calendar copies: each attendee's calendar copy has its own event id and they share ical_uid; evt_6e2c91d4b07f3a58c1d2e4 is Owen's copy (gcal.event_id is unique per row).
- invitation mails: invitation mails seeded for Owen, Oliver and Robert (INT-11: Arthur invited them; the time and guests are already on the event).
- tree states and notes: the SQL updates no L01, L03 or L07 ticket: the 14 PR-state children and ENG-2405 keep their base state, the planned move to Validation is dropped, Brian's check notes stay only on the Validation children ENG-2410, ENG-2429 and ENG-2430, and hazard_acknowledgements L01, L03 and L07 become dated_claim (stage_gate re-runs base_check without the manifest, so any UPDATE of such a ticket fails even as a verified repair; Arthur's ask is itself the reconciliation, which base_check accepts as the explicit job).
- Brian's screen checklist: a 28-item 'Screens checked' checklist on the Trello card (Daily Gift unticked) replaces the per-child notes as the per-screen record; the rule doc now says Brian and Oliver left notes on some of the open children (it closes the fork on children with no record (ENG-2427, ENG-2431) without touching a hazard ticket, and it is one more claim the inline comments overturn).
- td_note and axe_note: Brian's Linear notes on ENG-2434 and ENG-2426 are gone; the done claims met first are Owen's PR comments #1905#c_3 and #1908#c_3 and Brian's ticks (both tickets are L01 and L07 records; a comment on them needs an updated_at UPDATE).
- rev2: blind fork sweep before /prompt: hub drops 'those fix notes'; rule doc: a design question for Leonard isn't a bug post, one record per canvas line and one per bug posted after it, title without the tick box, nothing in the description, a child also stays if its screen is switched off, Brian's rule applies to the line on every child; Brian's comment names the current public build; folder dated 23:00Z, before the hub (a fresh blind agent reproduced the outcome counts but found three blocking forks (the build each note names, ENG-2424, the Dec 31 no-ads question) and smaller ones; the platform /injection advisory 2 on the folder date is folded in; truth is unchanged).
- rev3: platform /prompt FAIL on rev2: rule doc: a comment whose line was deleted carries nothing, a follow-up on a bug already posted is part of that bug, a post that points at a QA doc isn't a bug post, a canvas line and a later post stay separate, 0.3.310 came off the economy line; Robert's reply under his sub-250 report says both flickers are gone; Arthur puts Owen on a spare paid seat and he rejoins four DD channels on Feb 12; ENG-2403 and ENG-2404 checklists cleared; inline comments moved to just after their reviews, before the merges; distractor D_CHECKLIST dropped; Marcus's DM moved to Dec 11 and names the Android build, after the Gacha commit; the deck, tracker and checklist speak of main screens; the bottom bar reply covers the top panel; the doc's tree test reads 'a piece of its UI work never made it into that build'; the population bound reads 'the last line in that comment channel'; the deck reads 'UI pass wrapped up' and leaves Daily Gift out; Vincent's ENG-2363 note says Android still hits this; Marcus's mega tile reply says it still happens; the rule doc says the Android build; mirror review and comment ids follow the base sequence; the card's last activity is its comment (run_forensics/rev2/1_prompt_FAIL_r2.md scored UGT 2, Clarity 2 and Coherence 2 on forks F1 to F4, NB-1 and NB-14, every other dimension 5; truth is unchanged; a blind item-by-item sweep then flagged the deck against the inline comments and four smaller points; a blind coherence audit raised these, each re-checked through hg.py. Its claims on Vincent's Nov 22 replies were rejected: commits 3646982c and 'Fix trains a bit better' precede them, and he posts until Nov 23).
- rev4: platform /injection FAIL on rev3: Owen's channel_join rows in CE156FDFB428 and C09Q4S613CN removed; the two rows for C05V5FNLB9V and C050WGU41HR stay (run_forensics/rev3/0_injection_FAIL_r3.md C1: the base has no leave for Owen in those two channels, so a join there is an impossible membership history; he stays a listed member of both).
- rev5: platform /prompt FAIL on rev4: Owen gets a leave on Feb 11 and a join on Feb 12 in CE156FDFB428, C09Q4S613CN, C05433XK267 and C09SWTHEMEW; card 690b27282f4c1b7a6e93d512 dateLastActivity back to 2025-11-21T15:30:00Z (run_forensics/rev4/1_prompt_FAIL_r4.md scored Coherence 2 on his guest period and the card date, every other dimension 5; rev3's /injection said a join needs a matching leave; C09SWTHEMEW has the same gap and the task reads it, so it gets the same pair).
- rev6: baseline spread and failure patterns: Brian's DM with Owen (D07E9PSQB6W) gets three lines on Dec 11: Marcus's Tavern report and that his fix didn't hold, Vincent's tie of the Apple sync line to ENG-2073, and that he never got back to the Axe Arena info popup or the Tile Dozer how-to-play popup from Arthur's reviews. The original records stay; truth is unchanged. (12 rev5 baselines missed the ENG-2073 mail, Marcus's DM and both inline reviews 0 of 12, so 4 of 6 runs failed identically (patterns 67 %) and SD was about 0.04. Over the 7 stored runs Brian's DM history past early December reached 3 of 7. Putting all four in that one place makes the runs that read it differ from the runs that don't; a bootstrap from the runs' measured exposure gave P(all gates) about 0.44-0.60 against about 0.05 for a deck-plus-DM split (plan/boot_rev6.py, run_forensics/rev5/baseline/summary.md).).
- rev7: platform /prompt FAIL on rev6: Vincent replies in the navigation bar tooltips thread (CE156FDFB428, parent 1763394941.178509) on 2025-11-22 21:05 UTC, in the same retest session as his train and lives replies: Brian's second fix closed the 1 pixel gap. The parent's reply_count goes 6 to 7 and latest_reply moves to the new reply. Truth is unchanged (the line was already Fixed). (/prompt on rev6 (platform revision 10) scored Unique Ground Truth and Clarity 2: Vincent's 1 pixel gap 'but that's okay' (18:03 UTC Nov 21) is followed by Brian's 'I'll send another fix' (18:07 UTC) and nothing later, so Done vs Bugs and 9 vs 10 still broken were both fair. Its minimum fix asked for one dated record in that thread or the Owen-Brian DM saying the gap is fixed or still there; the closing reply keeps the outcome every earlier round accepted.).
- rev8: platform /hardness FAIL 1 on rev7: Brian's Dec 11 Apple line in D07E9PSQB6W (1765471447.518229, 'Vincent told me before he left that the Apple sync line ... is the same sync problem as ENG-2073') is removed. The Tavern and popup lines stay. Apple Covered by ENG-2073 rests on Vincent's email in Owen's inbox, as on rev5. Truth unchanged. (/hardness on rev7 (run_forensics/rev7/1a_hardness_FAIL1_r7.md) scored 1: the pre-check run swept every Brian message from Nov 1 to Dec 15 (slack_conversations_search_messages filter_users_from, calls 217-221) and the three Dec 11 lines settled Tavern, Apple and both popups at once. rev6 was placed by baseline spread alone and never modelled the one pre-check run. plan/boot_rev8.py ranks all 27 placements of the three corrections over 8 measured runs: dropping only the Apple line gives P(/hardness >= 3) about 0.69-0.80 (a DM reader still misses Vincent's email, 0 of 8 runs) and P(all baseline gates) about 0.51-0.72; dropping all three gives about 1.00 and 0.00 (spread, as measured twice on rev5).).
- rev9: platform /hardness FAIL 2 on rev8: Brian's Tavern line D07E9PSQB6W/1765471351.236119 is removed (Tavern rests on Marcus's DM D05USBTQY1F/1765452012.418229). Brian's Daily Gift note comment_3e81bf306c58746580a9cfa0ca12bd60 on ENG-2437 moves to his DM with Owen as D07E9PSQB6W/1765471651.208713 (2025-12-11T16:47:31Z, 'Daily Gift isn't finished either, the panel never got its last pass.'). The popups line D07E9PSQB6W/1765471563.704419 drops its opening 'And'. Truth unchanged. (/hardness on rev8 (run_forensics/rev8/1a_hardness_FAIL2_r8.md) scored 2: one cause, about 14 % against the 15 % loss. The run read Brian's DM, like the rev7 run. Every Brian-authored carrier is caught by the same from:Brian sweep, so rev8 needed two causes outside it. plan/boot_rev9.py models that sweep as one behaviour over 9 measured runs: rev9 gives P(/hardness >= 3) about 0.98 (Apple and Tavern sit in records 0 of 9 runs opened) and P(all baseline gates) about 0.53-0.68, against 0.62 and 0.73 for rev8.).

Blind sweep of the new seeds: plan/out/sweep_dispositions.md (6 BLOCK and 9 FIX, each re-checked and fixed or accepted). That reviewer printed some rows outside its list, so its reading of those rows is not blind.

### /injection Checks A–C walk

- Inventory: 149 INSERT, 39 UPDATE, no DELETE, no upsert; every statement is in the record ledger.
- Check A (references, uniqueness, identities, id contracts): base_check Check A; every parent resolves (roots 1bc1434b15a44cec9044db1b59ae4995, Drive roots d_cc3e90160f490686039986 and d_fc22d5941b2aeb5c03ad32, boards, PRs).
- Check B (structure, literal JSON, generated and NOT NULL columns): sql_lint 0 errors; no text_fts or body_text_fts; Linear dates YYYY-MM-DDTHH:MM:SSZ.
- Check C (dates, parent and reply order, statuses, counts, superseding records): base_check Check C; every seeded event is before the seed bound except Sunday's review, a future event; overturning records follow what they overturn.

### Touched-data census

The census and its hazard dispositions are in 'Touched-data census and coherence hazards' above (all six categories; L01, L03 and L07 acknowledged as dated_claim; seven NB cards dispositioned).

### Counter-readings

| Category | Counter-reading (strongest argument it fails) | Evidence that resolves it | Verdict |
|---|---|---|---|
| Temporal | Brian's check notes could predate the fixes they imply | ENG-2430 and ENG-2410 follow #2205 (C05433XK267 2025-11); ENG-2429 precedes the ENG-2404 tick at 14:29:13 | PASS |
| Temporal | the inline comments could sit outside their reviews | harmonygames-Games/GameOfDominoes#1905#rc_1 at 13:05:35Z, after #rev_1 at 13:05:32Z and before the 13:05:40Z merge; #1908#rc_1 at 01:51:55Z, after 01:51:51Z and before 01:51:59Z | PASS |
| Temporal | Vincent's replies could postdate his last activity | latest is CE156FDFB428/1763845872.804449, Nov 22; his last Slack is Nov 23 | PASS |
| Temporal | the deck could be stale only by accident | f_d15a8c70e3f2b94a61c8d3 is Nov 21; comment_d6aee2099bd71050facc422ccef8f809 is Dec 5 and D07E9PSQB6W/1765471651.208713 Dec 11, so the corrections follow it | PASS |
| Semantic / Category | 'Collect & Win' and 'Win & Collect' could read as two screens | ENG-2424 title and C9CA62B5180A/1765927876.696389 name one feature; the base uses both | PASS (pre-existing) |
| Semantic / Category | the ZM doc could be read as the rule | f_72e0b4c3d91a5f68c2b7e4's title and first line name Zombie Match; H1 says the ZM canvases stay where they are | PASS |
| Semantic / Category | a shop icon bug could hold ENG-2432 | H1: 'A bug on a screen doesn't hold its child'; f_3ca9e15d7b20f4e681ad52 | PASS |
| Cross-service Referential | the inline comment's file might not be in the PR | both paths come from the CodeRabbit summaries harmonygames-Games/GameOfDominoes#1905#c_2 and #1908#c_2 | PASS |
| Cross-service Referential | a seeded PR comment could lack its mirror | 12 copies threaded in C050WGU41HR under the opened messages; base_check INT-01 | PASS |
| Cross-service Referential | 0.3.310 has no base record Owen can read | H1 is the authority; the sequence holds (C09SWTHEMEW/1770753609.436139) and nothing joins it to a review version (NB-21) | PASS (limit accepted) |
| Quantitative | still broken could be 7 rather than 9 | H1: 'Covered ones count as still broken'; solver reply still_broken 9 | PASS |
| Quantitative | 63 lines could be 61 | H1 says every ticked or unticked line; two empty roots have no line (CE156FDFB428/1763042124.247899) | PASS |
| Quantitative | reply counters could drift | base_check Check C: each parent's counters equal its replies, with every seeded reply included; the record ledger lists each counter row | PASS |
| State / Lifecycle | a ticket in PR with a merged PR reads as a pre-existing defect | the SQL updates none of them; the hub says the tree never got closed out, so reconciling them is the job; hazard_acknowledgements L01 and L07 dated_claim; ENG-2417 | PASS |
| State / Lifecycle | ENG-2405 stays Todo with a merged PR | H1 says the masters stay as they are; the SQL leaves it alone; L03 dated_claim; harmonygames-Games/GameOfDominoes#1905 | PASS |
| State / Lifecycle | a ticked line could also be Gone after Dec 16 | H1's first-fit order puts Fixed first, so ticked Win & Collect lines stay Fixed; f_3ca9e15d7b20f4e681ad52 | PASS |
| Identifier / Format | a changed id scheme or a typed address | eval lint FAIL 0 CHECK 0; sql_lint 0 errors; ids per 1.A; collisions 0 (1.F) | PASS |
| Identifier / Format | calendar copies with one event_id would collide | each copy has its own id and they share ical_uid; evt_6e2c91d4b07f3a58c1d2e4 is Owen's | PASS |
| Other | a designed disagreement could read as a silent system conflict | every overturning record is a dated human message: D05USBTQY1F/1765452012.418229, C09Q4S613CN/1764606918.318209 | PASS |
| Other (pre-existing) | the ENG-2404 checklist disagrees with child states | NB-14: the SQL clears it; ENG-2404 | PASS (repaired) |
| Other (sibling) | another merged child could hide the same gap as ENG-2434 | all 19 open children were read in the sweeps; plan/truth_sketch.json lists each; controls ENG-2417 and ENG-2432 | PASS |
| Other | the tracker could be filler | UI pass tracker gives the screen-to-ticket list the child records overturn; gsheets has no other seeded record, and it stays in the design as a stale summary (design_delta) | PASS |
| Other | the 28-item checklist could be filler | it is the per-screen record for children in PR state, closing the fork on ENG-2427 and ENG-2431; Daily Gift stays unticked, in line with D07E9PSQB6W/1765471651.208713 | PASS |

Unresolved: the numbers are UNCALIBRATED until a platform run; `linear_create_issue` at volume and direct canvas reads are unproven; the fork sweep's point that no record proves ENG-2427 and ENG-2431 are in the build now rests on Brian's undated ticks and H1's default rule.

```
STAGE GATE injection: PASS — Task_Authoring/task_inputs · 01_Universe_Inject.sql#ea5b542897c8 · 01_Hardness_Manifest.json#ec4cc1070c06 · 01_Grounding_Dossier.md#9c226652d6ec · solver/solver.py#c2eca0f97c62 · 01c_Dispositions.json#b86f62194ac2 · 01c_Preflight_Report.json#2580b7c15c79 · 00_Assigments.md#c039da1b9b09 · 01_Scenario_Design.md#de755e35633e · 01_Hardness_Manifest.draft.json#459add197b56 · 01_Gradable_Surface.json#6d9cd388cdbb · __context__#ba6bb23d4a12 · __assignment__#560a0d2ca2a9 · __policy__#dc4ab5df3cdd · __gate_policy__#f8638415ca2c · __review__#a52cce78498e · blocking 0 · warnings 0 · checks 40
[PASS] assignment.v3_context: Owen Baker / Game Engineer (Unity); medium cap <85%; freeze 2026-02-14T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe normal; KB bound; clock Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
[PASS] structure.outputs: 6 output(s) present: 01_Universe_Inject.sql, 01_Hardness_Manifest.json, 01_Grounding_Dossier.md, solver/solver.py, 01c_Dispositions.json, 01c_Preflight_Report.json
[PASS] structure.inputs: 4 input(s) present: 00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json)
[PASS] chain.scenario: upstream 'scenario' PASS pasted and current (01_Scenario_Design.md#de755e35633e, 01_Hardness_Manifest.draft.json#459add197b56, 01_Gradable_Surface.json#6d9cd388cdbb, 00_Assigments.md#c039da1b9b09, __context__#ba6bb23d4a12, __assignment__#560a0d2ca2a9, __policy__#dc4ab5df3cdd, __gate_policy__#f8638415ca2c, __review__#cd30ba058f1a)
[PASS] structure.sections: 17 required sections present and non-empty (01_Grounding_Dossier.md)
[PASS] structure.placeholders: no placeholders in 01_Grounding_Dossier.md
[PASS] evidence.entity: 14/14 items carry a source pointer (min 90%)
[PASS] evidence.keyword: 10/10 items carry a source pointer (min 100%)
[PASS] evidence.persona_reach: 10/10 items carry a source pointer (min 100%)
[PASS] evidence.record_ledger: 188/188 items carry a source pointer (min 100%)
[PASS] evidence.facts_for_human: 19/19 items carry a source pointer (min 100%)
[PASS] tool.sql_lint: sql_lint re-run matches the paste: errors 0, warnings 16, rows 188
[PASS] tool.injection_lint: hg.py lint: 0 FAIL, 0 CHECK dispositioned, 0 INFO; sha256 ea5b542897c8 matches 01_Universe_Inject.sql
[PASS] review.warning_dispositions: every sql_lint warning class dispositioned (weekend×8, clock×8)
[PASS] tool.base_check: base_check pasted PASS; re-run PASS
[PASS] tool.base_claims: base_claims pasted PASS; re-run PASS
[PASS] tool.hardness_gate: hardness_gate (SQL) pasted PASS; re-run PASS
[PASS] structure.design_delta: final manifest keeps all 52 draft ids
[PASS] structure.preflight: 01c_Preflight_Report.json bound by sha256 to the current SQL, solver, surface, manifest and dispositions
[PASS] solver.contract: solver contract re-run PASS
[PASS] mutation.dispositions: 32 mutation and intervention results each carry a written disposition (01c_Dispositions.json)
[PASS] geometry.upper_bound: U 0.828 (125/151) vs 1 - cap 0.15 (V3 medium): PASS (bound PASS); re-run U 0.828 PASS (bound PASS)
[PASS] geometry.margin: L_max 0.3708609271523179 vs (1 - cap) + 0.10: OK (advisory: the margin is a judgment, not a proof)
[PASS] liveness.dispositions: every liveness flag dispositioned (6 flag(s))
[PASS] forecast.preregistered: forecast hev_2dfef4f1b21105bb pre-registered in the ledger (UNCALIBRATED)
[PASS] tool.check_sql_pasted: persona_view check-sql --load-bearing output pasted with verdict PASS
[PASS] reach.injection: 17 scoped load-bearing ids YES for owen_baker
[PASS] structure.facts_declared: manifest declares 15 load-bearing fact(s) in `facts`
[PASS] tool.fact_check: fact_check --no-leak pasted PASS; re-run PASS
[PASS] kb.coherence_hazards: coherence audit cites 16 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 7 seeded speakers each cited with activity.json status; conventions.json cited
[PASS] kb.integrations: companions listed per integrations.json (10 INT ids, services ['gcal', 'gdocs', 'gdrive', 'github', 'gmail', 'gsheets', 'gslides', 'linear', 'slack', 'trello'])
[PASS] boundary.anchor_naming: 4 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 20 evidenced counter-readings (of 23 found; need ≥ 18) in 01_Grounding_Dossier.md
[PASS] review.coverage: self-review addresses all 9 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

