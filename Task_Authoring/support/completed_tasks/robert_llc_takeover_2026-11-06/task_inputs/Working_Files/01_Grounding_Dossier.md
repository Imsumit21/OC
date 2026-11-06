# Grounding Dossier — Robert · LLC take-over plan for Combo Fighter · injection rev4 · contains no prompt, OE or criterion text

SQL: `task_inputs/01_Universe_Inject.sql` (stored byte for byte in `Working_Files/run_forensics/rev4/01_Universe_Inject.sql`. Earlier revisions are kept with their reviews, truth, solver, manifest and dossier: rev1 and rev2 in `run_forensics/rev1/` and `run_forensics/rev2/` (both passed /injection; rev2 failed /prompt, `run_forensics/rev2/1_prompt_FAIL_r2.md`), and rev3 in `run_forensics/rev3/` (passed /injection and /prompt at 5, failed /hardness at 2: `run_forensics/rev3/precheck/1a_hardness_FAIL_r3.md`, `Working_Files/01a_Hardening_Report.md`)), built by `Working_Files/plan/build_sql.py` from the certified design (`01_Scenario_Design.md`, draft manifest, surface) and the planned wording in `plan/wording.json`; final manifest by `plan/build_final_manifest.py`; solver `Working_Files/solver/solver.py` (truth `solver/truth.json`); this file by `plan/assemble_dossier.py`; every tool output below by `plan/run_checks.sh`. Universe normal (hg4-2026-08-31), seed bound and eval clock 2026-02-14T00:00:00Z (Fri Feb 13, 4:00 PM PT); Robert's today is Saturday Feb 14, 2026; the Slack export ends Feb 13 10:03 UTC (NB-6) and every seeded Slack row is earlier. 136 INSERT + 3 UPDATE statements over 10 schemas (gdrive, gdocs, gsheets, gslides, slack, trello, gmail, gcal, github, linear). Snowflake and Confluence are read, never written. Every probability here is UNCALIBRATED.

## 1.A Structural

| Table | NOT NULL columns supplied (live schema) | Base location · sample ids | Format notes |
|---|---|---|---|
| slack.slack_messages | id, ts, channel_id, type, text, reply_count, reply_users_count, is_activity_message, reactions_json, files_json, attachments_json, created_at, metadata_json | slack/messages/D04V95AAAHW/2026-02.json (root bc4bc3d0e2a0ea6ae92cb2a9712e8f76 = D04V95AAAHW/1770056235.480619); slack/messages/C05433XK267/2026-01.json /1236 (Jenkins job post 859c1e0166850fd72ed8d767ddf32fe7) | id = sha256(channel|ts)[:32]; ts 6 decimals; a reply carries thread_parent_id + thread_ts_legacy and its root's reply_count / reply_users_count / latest_reply are updated (Q01–Q03); Jenkins posts are SLACK_BOT_0005_SLACK_ID with text '' and one attachment (color, fallback, fields[0].value) |
| gmail.gmail_threads / gmail_messages | id, user_email; id, thread_id, user_email | gmail threads/00014520.json (robert@harmonygames.co/1836972401494127045, App Store rejection); leonard.hayes@harmonygames.co/1855983949220444975 (dbt receipt) | thread id = mailbox/((ms << 20) + 20 bits); message id = mailbox/ + the RFC Message-ID; one copy per seeded mailbox (sender SENT, recipients INBOX); internal_date = date in ms; App Store mail from SVC_4131_EMAIL with the base labels (INBOX, CATEGORY_UPDATES, Label_ad4e31dc09, Label_aeb79a643f) |
| gdrive.drive_files · gdocs.docs_documents · gsheets.sheets_spreadsheets / sheets_sheets · gslides.slides_presentations / pages / page_elements | id, name, mime_type; document_id, title; spreadsheet_id, title; spreadsheet_id, sheet_id, title; presentation_id, title; presentation_id, object_id; presentation_id, page_object_id, object_id | gdrive data.json /drive_files/0 (d_00003b5dc5d1e91bd4bd6f, parent d_63fffeb4fab5233ed5bb73 = Leonard's root); /drive_files/107 (parent d_9f7ba94f7526d54d8482ba = Robert's root); gslides f_0281d5b83f931db7fff2be (TEXT_BOX elements 9144000 × 5143500) | f_/d_ + 22 hex; identical owner and sharing on the Drive row and the native row; Docs body_text with TITLE / NORMAL_TEXT style runs; Google-native files carry no content_path |
| gcal.gcal_events | event_id, calendar_id | gcal data.json (11,130 events, plan/idcheck/gcal.out.json) | one row per attendee calendar (self:true on the owner's copy), shared ical_uid 32 hex @hg4; evt_ + 22 hex; Mon Feb 16 18:00–18:45Z is a not-yet-happened event |
| trello.trello_cards / trello_actions | id, name, idBoard, idList; id, type, date | trello data.json board 640643a3fd8f3ca308d9318e (449 cards, last idShort 455; last activity 2025-11-12, card 688c4d14c312a27fa2747e40) | ids: first 8 hex = Unix seconds (I16); full badges_json shape; createCard action with board/card/list data |
| github.github_pull_requests / branches / commits / pull_request_commits / timeline_events | id, repo_id, number; id, repo_id, name; sha, repo_id; id, pr_id, commit_sha; id, pr_id, event | github data.json /pull_requests/1046 (harmonygames-Games/GameOfDominoes#1916, merged by EMPLOYEE_0025_GITHUB_USERNAME, html_url null), /branches/981 (arthur.blake/boombitWithEcon), /timeline_events/4725–4726 (merged, closed) | PR id = repo#number; events #ev_n; commit sha 40 hex |
| linear.linear_projects / linear_issues / linear_comments | id, team_id, name, priority, labels_json, links_json, is_archived, created_at, updated_at; id, title, priority, labels_json, links_json, relations_json, state_history_json, is_archived, created_at, updated_at; id, issue_id, author_id, body, is_edited, created_at, updated_at | linear data.json /issues/2377 (ENG-2437, newest ENG), /issues/509 (ART-705, state 'Backlog'), /projects (2 base projects) | id = identifier = ENG-2438…ENG-2474; state names as ids; Backlog carries no lifecycle stamp; comment ids comment_ + 32 hex (§6b ● carrier); linear_project_teams / _members are not writable (sql_lint) |

## 1.B Entity

| Entity | Spelling used | Where it appears (cited) | Agreement |
|---|---|---|---|
| Robert | robert@harmonygames.co · EMPLOYEE_0016_SLACK_ID · usr_Robert | C0ADGSZKR3R/1770839322.836779 (Soundly canceled); Drive root d_9f7ba94f7526d54d8482ba; deck f_7d2c9e7822e87b92a11759 | AGREE |
| Leonard Hayes | leonard.hayes@harmonygames.co · EMPLOYEE_0038_SLACK_ID · usr_63fffeb4fab5233e · PERSON_6094_TRELLO_USER_ID | C0ADGSZKR3R/1770933601.686309; hub D04UP2L3E3S/1770961200.890407; ground rules f_1e468a9d69ea0f0a2001f5; card 698e6548aa9516b76c4ab475 | AGREE |
| Arthur Blake ('Blake') | arthur.blake@harmonygames.co · EMPLOYEE_0025_SLACK_ID · usr_cc3e90160f490686 · EMPLOYEE_0025_GITHUB_USERNAME | C0ADGSZKR3R/1770937232.664809 (KubLLC card); DM D04V95AAAHW/1770952200.665739; PR harmonygames-Games/GameOfDominoes#1917; Jenkins 'Arthur Blake' C05433XK267/1769619277.508249 | AGREE (I03: his base thread files use the blake@ alias) |
| Sunset | Sunset (the firm buying the data and running the sale) | C0ADGSZKR3R/1770859962.210719; C07C2866011/1770839126.382429 (liquidates laptops, build machines) | AGREE |
| the LLC / KubLLC card | the founders' LLC; Arthur's 'Kub card' | C0ADGSZKR3R/1770937232.664809 ('my KubLLC card'); Arthur's mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> ('my Kub card') | AGREE (short form) |
| Calm Play LLC | Calm Play LLC | C04UEQVDVB7/1701383740.580749 (fully owned by Harmony Games); C04UEQVDVB7/1703492127.063049; note comment_ffcbb4c79467be3bdd75a1dd3b8da04f | DISAGREE (a stale suggestion the ground rules' vehicle sentence overrules; rev4: a control row, EXC purged) |
| Combo Fighter | Combo Fighter (CF) | C07C2866011/1770084297.911029; C09UHHN6PFZ/1770404397.819789; ENG-2438; deck f_7d2c9e7822e87b92a11759 | AGREE |
| Domino Delights | Domino Delights (DD; repo GameOfDominoes) | C0ADGSZKR3R/1770789534.434749; snowflake tables/12 game_id domino_delights; ENG-2439; harmonygames-Games/GameOfDominoes#1917 | AGREE |
| Zombie Match 3D | Zombie Match (ZM; 'Puzzles vs Zombies' until July 2025) | C07C2866011/1752548116.304169 (transfer); confluence page_aws_infra (one account for dev and prod); ENG-2440 | AGREE |
| BoomBit | BoomBit (publishing test on DD) | C09SWTHEMEW/1770725775.479449; C09SWTHEMEW/1770977006.104929 (test stopped Feb 13) | AGREE |
| VO campaign | the CF VO campaign, $100/day | C09UHHN6PFZ/1770404397.819789, C09UHHN6PFZ/1770404445.795829, C07C2866011/1770489896.754049; status C09UHHN6PFZ/1770938400.370665; deck f_7d2c9e7822e87b92a11759 | DISAGREE (designed: 'both campaigns live' Feb 7 vs 'only the CF VO campaign' Feb 12) |
| Metabase / dbt | Metabase, dbt (dbt is [USERNAME_30019] in #winddown, NB-12) | C0ADGSZKR3R/1770933903.645709; C0ADGSZKR3R/1770937232.664809; dbt receipt leonard.hayes@harmonygames.co/1855983949220444975 ($100); mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> | AGREE (the seeded mail spells dbt out) |
| GitHub | GitHub team plan | C0ADGSZKR3R/1770933450.410449 (keep until data is sold, then transfer); mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> ($48 now that copilot is off) | AGREE |
| Kapwing | Kapwing ([PERSON_NAME_20852] in Arthur's #winddown line, NB-12) | C0ADGSZKR3R/1770933450.410449 ('Kapwing (Blake)'); C0ADGSZKR3R/1770937188.477219; notice blake@harmonygames.co_1856962040028188034.json; note comment_8c69b5b90f9f6c03a0a168d25e6b75bd | AGREE (the note spells it out) |
| layer.ai | layer.ai ('layer' in #winddown) | C09UHHN6PFZ/1770837702.167889 (access until March 3rd); C0ADGSZKR3R/1770837793.168589 | AGREE |
| Helpshift | Helpshift | C0ADGSZKR3R/1770789534.434749 (off DD and ZM before Feb 28th); checklist C0ADGSZKR3R/1770933450.410449 | AGREE (NB-5 date never used) |
| Figma | Figma | C0ADGSZKR3R/1770859313.592649 (good until September 11th); C0ADGSZKR3R/1770933601.686309; note comment_3a8e425288db648883caa9b699488f6f | AGREE |
| build machines | the Android and Apple build machines | C04UEQVDVB7/1700755756.051439 (HG orders them, 2023); C07C2866011/1770839126.382429; note comment_7a0dea6299c7963e9a3e673996bd47fe | AGREE |
| REVENUE_DAILY | ANALYTICS.MONETIZATION.REVENUE_DAILY ('the warehouse's daily revenue table') | snowflake snowflake.json /tables/12; /tables/13 (REVENUE_DAILY_V2, same January sums); ground rules f_1e468a9d69ea0f0a2001f5 | AGREE |
| AWS guide | AWS Infrastructure Guide (page_aws_infra) | confluence_working.json /pages/2 (Fargate Phoenix + Nakama ~$650/mo); note comment_a317e10875adb686553e43989c1bab61 | AGREE |
| Jenkins DD iOS Submission | DD iOS Submission #218 | C05433XK267/1769619277.508249 (#216), C05433XK267 2026-01 /1238 (#217, last base job); seeded C05433XK267/1770932400.314774, C05433XK267/1770932970.616709 | AGREE |
| PR #1917 | GameOfDominoes#1917 'Replace Helpshift with support email' | harmonygames-Games/GameOfDominoes#1917; base #1916 = harmonygames-Games/GameOfDominoes#1916 (Dec 26, 2025); note comment_7f8d7a9d959ca264f47b0e21d76416d1 | AGREE (new; #1916 is the last base PR) |
| LLC take-over project | Linear project 'LLC take-over' (team_ENG) with ENG-2438…ENG-2474 | 0fa95761-d59b-4ff4-a8a3-15df3210ca6e; base max ENG-2437 (linear data.json /issues/2377) | AGREE (new) |
| founders' board | Trello 'Harmony Games' board, To Do list | 640643a3fd8f3ca308d9318e, list 640643a3fd8f3ca308d93195; card 698e6548aa9516b76c4ab475 | AGREE |
| ground rules doc | 'LLC ground rules (Combo Fighter and whatever else we take)' | f_1e468a9d69ea0f0a2001f5 | AGREE (new) |
| notes doc | 'LLC notes (Monday)' | f_a7af6f358dd5648c11a608 | DISAGREE (designed: superseded by the ground rules) |
| draft sheet | 'LLC 90 days (draft)' | f_d996e4c434ce160dc52596 | DISAGREE (designed: stale numbers, layout source) |
| Robert's deck | 'Combo Fighter: next 90 days' | f_7d2c9e7822e87b92a11759 | AGREE |
| Monday call | 'LLC: decide', Mon Feb 16 10:00–10:45 PT | evt_f5f279f282d20ec86bb8e5 (Robert's copy); evt_c82c0965b68d959ee4241b (Leonard's) | AGREE (new) |

Robert's Linear id is the base's 'usr_Robert' (I10); Arthur's GitHub login is the token EMPLOYEE_0025_GITHUB_USERNAME (I08). No roster person is renamed or re-titled; no new header token is minted (SVC_4131_EMAIL is App Store Connect's base sender).

## 1.C Voice and realism

Seeded speakers, each with its activity.json (normal KB) status at the clock:
- Leonard Hayes (leonard.hayes@harmonygames.co, EMPLOYEE_0038_SLACK_ID) — activity.json status_at_clock active_feb_2026; seeds the hub D04UP2L3E3S/1770961200.890407 (Feb 13 05:40Z = Thu 21:40 PT), the #prototype status C09UHHN6PFZ/1770938400.370665 (Feb 12 23:20Z), 29 issue notes (Feb 13 00:24–01:16Z), the docs f_1e468a9d69ea0f0a2001f5 and f_a7af6f358dd5648c11a608, the draft f_d996e4c434ce160dc52596, the card 698e6548aa9516b76c4ab475, the split mail robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com> and the Monday event; last base post C0ADGSZKR3R/1770937460.360699 (Feb 12 23:04Z).
- Arthur Blake (arthur.blake@harmonygames.co, EMPLOYEE_0025_SLACK_ID) — activity.json status_at_clock active_feb_2026; seeds the DM reply D04V95AAAHW/1770952200.665739 (Feb 13 03:10Z = Thu 22:10 ET), 8 issue notes (Feb 13 00:55–01:37Z), the billing mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> (02:35Z) and PR harmonygames-Games/GameOfDominoes#1917 (opened 18:05Z, merged 21:10Z Feb 12); last base post C0ADGSZKR3R/1770937232.664809 (Feb 12 23:00Z).
- Robert (robert@harmonygames.co, EMPLOYEE_0016_SLACK_ID) — activity.json status_at_clock active_feb_2026; seeds only his Feb 8 deck f_7d2c9e7822e87b92a11759 (Robert's base #prototype posts run to C09UHHN6PFZ/1770923166.200169, Feb 12).
- Bots and services (not personas, no activity.json entry): Jenkins SLACK_BOT_0005_SLACK_ID (base #builds poster, C05433XK267/1769619277.508249), App Store Connect SVC_4131_EMAIL (base INT-08 sender, threads/00014520.json).

Lengths, hours and titles from conventions.json (normal KB): slack.length_chars_by_channel_type im p50 38 / p90 ~105 / p99 well above 600 — the hub (~610 characters) sits in the im tail like Leonard's long base DMs (D04UP2L3E3S/1770876340.333289 runs ~300) and his #winddown drafts (C0ADGSZKR3R/1770673717.808759); Arthur's DM reply (~120) and Leonard's #prototype reply (~150, private p90 155) are ordinary. slack.per_person_hours_and_style: Leonard's core 80% UTC window 15–02 and Arthur's 15–01; the #prototype status (23:20Z) and the issue notes (00:24–01:37Z) fall inside them, while the hub (05:40Z) and Arthur's DM (03:10Z) are late-evening posts in each author's 20% tail, like Leonard's base 05:58Z #winddown post C0ADGSZKR3R/1770789534.434749 in the same week. gmail.internal_subject_len_chars p50 42: 'LLC money' and 'billing moved to my card' are short like Leonard's base subjects; gcal.duration_min p50 30 / p75 45: the Monday call is 45 minutes; linear.title_prefixes_by_team ENG: titles with no prefix dominate — the issue titles are plain item names; github.pr_title_patterns 'free text' and branch_patterns 'name/description' — 'Replace Helpshift with support email' and arthur.blake/supportEmail follow them.

Voice from real messages: Leonard writes lower-case, run-on Slack lines and fragments ('I'll keep Intuit for now', C0ADGSZKR3R/1770839688.408909; 'we have time for Carta renewal so I'm not gonna really touch that', C0ADGSZKR3R/1770932858.658179); Arthur is terse ('coderabbit is cancelled', C0ADGSZKR3R/1770936655.574079; 'cursor and [PERSON_NAME_20852] cancelled', C0ADGSZKR3R/1770937188.477219). The seeded notes and messages keep those registers; the docs are short plain-sentence notes like Leonard's base #winddown lists.

## 1.D Keyword

| Term | Hits / pointer | Note |
|---|---|---|
| "Helpshift" | base C0ADGSZKR3R/1770789534.434749, C0ADGSZKR3R/1770673717.808759; seeded PR harmonygames-Games/GameOfDominoes#1917 | Feb 28 comes from Leonard's line, not the vendor ack (NB-5) |
| "layer" / "layer.ai" | base C09UHHN6PFZ/1770837702.167889, C0ADGSZKR3R/1770837793.168589; seeded reply C09UHHN6PFZ/1770923700.470906 (rev4) | access until March 3rd; the reply says CF's concept art is only there and asks Robert to pull it out |
| "jenkins" | base #builds C05433XK267 Jenkins posts; seeded robert@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com> (rev4) and Arthur's ENG-2446 note | the email's second paragraph carries CF's account at $62 now |
| "KubLLC" / "Kub card" | base C0ADGSZKR3R/1770937232.664809; seeded robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> | Arthur's own card |
| "Calm Play" | base C04UEQVDVB7/1701383740.580749, C04UEQVDVB7/1703492127.063049; seeded comment_ffcbb4c79467be3bdd75a1dd3b8da04f | an older-channel search returns the subsidiary posts |
| "VO campaign" / "campaign" | base C09UHHN6PFZ/1770404397.819789, C07C2866011/1770489896.754049; seeded C09UHHN6PFZ/1770938400.370665 | in no list; a #prototype or #executives read finds it |
| "REVENUE_DAILY" | snowflake snowflake.json /tables/12 (2,284 rows; January sums DD 183.11, CF 7.36, ZM 0.00) | the ground rules call it 'the warehouse's daily revenue table' |
| "Fargate" / "Nakama" | confluence_working.json /pages/2 | the cost note behind ZM's hosting (Fargate ~$650 + Aurora ~$420) |
| "boombitWithEcon" | base C05433XK267 2026-01 /1237 (Blake/boombitWithEcon); github /branches/981 (arthur.blake/boombitWithEcon) | NB-13 form difference; no branch is graded |
| "LLC ground rules" | NEW TERM — introduced in f_1e468a9d69ea0f0a2001f5 | reached via the hub ('the ground rules doc') |
| "LLC take-over" | NEW TERM — introduced in 0fa95761-d59b-4ff4-a8a3-15df3210ca6e | reached via the hub ('the LLC project in linear') |
| "LLC: what we take from HG" | NEW TERM — introduced in 698e6548aa9516b76c4ab475 | reached via the ground rules ('the LLC card on our board') |
| "LLC 90 days (draft)" | NEW TERM — introduced in f_d996e4c434ce160dc52596 | reached via the hub ('my draft from Tuesday') |
| "LLC notes" | NEW TERM — introduced in f_a7af6f358dd5648c11a608 | reached by a Drive search for 'LLC' (the H1 decoy) |
| "LLC money" | NEW TERM — introduced in robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com> | reached via the hub ('I'll email you how we split the money') |
| "$140" (DD prod account) | NEW TERM — introduced in D04V95AAAHW/1770952200.665739 | a DM search for 'prod account' / 'Domino' / 'month' returns it |
| "$248" | NEW TERM — introduced in robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> | a mail search for 'metabase' / 'dbt' / 'github' / 'billing' returns it |
| "$62" (CF's account) | NEW TERM — introduced in robert@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com> (rev4; ENG-2445's note now says ~$95) | a mail search for 'jenkins', 'backend', 'AWS' or from:arthur returns it |
| "concept art" | NEW TERM — introduced in C09UHHN6PFZ/1770923700.470906 (rev4) | a Slack search for 'layer.ai' returns the post it replies to |
| "without a mail account set up it does nothing" | NEW TERM — introduced in robert@harmonygames.co/<136285951.151027292.1770967800000@email.apple.com> | the App Store notice; a mail search for 'Domino Delights' or 'submission' returns it |
| "#218" / "Replace Helpshift with support email" | NEW TERM — introduced in C05433XK267/1770932970.616709, harmonygames-Games/GameOfDominoes#1917 | #builds and GitHub |
| "LLC: decide" | NEW TERM — introduced in evt_f5f279f282d20ec86bb8e5 | the Monday call |

Base controls for the seeded searches: 'Domino' in D04V95AAAHW returns only base git-debugging messages before the seeded reply; 'Kub' returns only C0ADGSZKR3R/1770937232.664809 in base Slack; 'support email' has no base hit in Robert's mailbox (the base DD mails are TestFlight and review notices).

## 1.E Persona reach

Load-bearing scoped ids (seeded and base) written to `Working_Files/plan/load_bearing_ids.txt` (39 ids; Linear, GitHub, Trello, Snowflake and Confluence are unscoped); output verbatim:

```
CHECK-SQL as robert <robert@harmonygames.co>
[YES LB] L6 gdrive.drive_files insert f_1e468a9d69ea0f0a2001f5 - file is shared with the persona (shared_with_emails)
[YES LB] L9 gdrive.drive_files insert f_a7af6f358dd5648c11a608 - file is shared with the persona (shared_with_emails)
[YES LB] L11 gdrive.drive_files insert f_d996e4c434ce160dc52596 - file is shared with the persona (shared_with_emails)
[YES LB] L13 gdrive.drive_files insert f_7d2c9e7822e87b92a11759 - persona owns the file
[YES LB] L15 gdocs.docs_documents insert f_1e468a9d69ea0f0a2001f5 - file is shared with the persona (shared_with_emails)
[YES LB] L18 gdocs.docs_documents insert f_a7af6f358dd5648c11a608 - file is shared with the persona (shared_with_emails)
[YES LB] L20 gsheets.sheets_spreadsheets insert f_d996e4c434ce160dc52596 - file is shared with the persona (shared_with_emails)
[YES LB] L23 gsheets.sheets_sheets insert f_d996e4c434ce160dc52596, f_d996e4c434ce160dc52596#0 - file is shared with the persona (shared_with_emails)
[YES LB] L25 gslides.slides_presentations insert f_7d2c9e7822e87b92a11759 - persona owns the file
[YES LB] L28 gslides.slides_pages insert f_7d2c9e7822e87b92a11759, slide_886d78971206 - persona owns the file
[YES LB] L30 gslides.slides_page_elements insert f_7d2c9e7822e87b92a11759, el_7e281c2d6d42, slide_886d78971206 - persona owns the file
[YES LB] L32 gslides.slides_pages insert f_7d2c9e7822e87b92a11759, slide_05405983565d - persona owns the file
[YES LB] L34 gslides.slides_page_elements insert f_7d2c9e7822e87b92a11759, el_4f79d571a8ab, slide_05405983565d - persona owns the file
[YES LB] L36 gslides.slides_pages insert f_7d2c9e7822e87b92a11759, slide_34827ed9cf24 - persona owns the file
[YES LB] L38 gslides.slides_page_elements insert f_7d2c9e7822e87b92a11759, el_c30917bbd73c, slide_34827ed9cf24 - persona owns the file
[YES LB] L40 slack.slack_messages insert 9ed17488702e4bf387cc012f7bb0a509, C05433XK267/1770932400.314774 - persona EMPLOYEE_0016_SLACK_ID is in members of public builds
[YES LB] L43 slack.slack_messages insert 85bc96b0aa43bb455a58da9d8b63c060, C05433XK267/1770932970.616709 - persona EMPLOYEE_0016_SLACK_ID is in members of public builds
[YES LB] L45 slack.slack_messages insert 6908b2f17c379e809aafa6b2b169f4bf, C09UHHN6PFZ/1770938400.370665 - persona EMPLOYEE_0016_SLACK_ID is in members of private prototype
[YES LB] L47 slack.slack_messages update 73ec270a3d07eb8d8488384898be079e, C09UHHN6PFZ/1770404397.819789 - persona EMPLOYEE_0016_SLACK_ID is in members of private prototype
[YES LB] L48 slack.slack_messages insert 103ed629eef6bb64a30ab49eb5c8fe40, C09UHHN6PFZ/1770923700.470906 - persona EMPLOYEE_0016_SLACK_ID is in members of private prototype
[YES LB] L50 slack.slack_messages update bdb4f7af824ec3819acdf5fc3cc480ea, C09UHHN6PFZ/1770837702.167889 - persona EMPLOYEE_0016_SLACK_ID is in members of private prototype
[YES LB] L51 slack.slack_messages insert ad623a2f0d4387109d108e767b174609, D04V95AAAHW/1770952200.665739 - persona EMPLOYEE_0016_SLACK_ID is in members of im D04V95AAAHW
[YES LB] L53 slack.slack_messages update bc4bc3d0e2a0ea6ae92cb2a9712e8f76, D04V95AAAHW/1770056235.480619 - persona EMPLOYEE_0016_SLACK_ID is in members of im D04V95AAAHW
[YES LB] L54 slack.slack_messages insert 6257a3c4456db0bd2aeb872619d7a364, D04UP2L3E3S/1770961200.890407 - persona EMPLOYEE_0016_SLACK_ID is in members of im D04UP2L3E3S
[NO] L61 gmail.gmail_threads insert arthur.blake@harmonygames.co/1856975772057961391 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (robert@harmonygames.co)
[NO] L64 gmail.gmail_messages insert arthur.blake@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com>, ar - row is in mailbox arthur.blake@harmonygames.co, not the persona's (robert@harmonygames.co)
[YES] L66 gmail.gmail_threads insert robert@harmonygames.co/1856975772058401508 - row user_email is the persona (robert@harmonygames.co)
[YES LB] L68 gmail.gmail_messages insert robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com>, robert@h - row user_email is the persona (robert@harmonygames.co)
[NO] L70 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1856975772058497766 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (robert@harmonygames.co)
[NO] L72 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (robert@harmonygames.co)
[NO] L74 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1856989298688254292 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (robert@harmonygames.co)
[NO] L76 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (robert@harmonygames.co)
[YES] L78 gmail.gmail_threads insert robert@harmonygames.co/1856989298688559716 - row user_email is the persona (robert@harmonygames.co)
[YES LB] L80 gmail.gmail_messages insert robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com>, robert@h - row user_email is the persona (robert@harmonygames.co)
[NO] L82 gmail.gmail_threads insert arthur.blake@harmonygames.co/1856989298688898804 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (robert@harmonygames.co)
[NO] L84 gmail.gmail_messages insert arthur.blake@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com>, ar - row is in mailbox arthur.blake@harmonygames.co, not the persona's (robert@harmonygames.co)
[NO] L86 gmail.gmail_threads insert arthur.blake@harmonygames.co/1856982378087055316 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (robert@harmonygames.co)
[NO] L88 gmail.gmail_messages insert arthur.blake@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com>, ar - row is in mailbox arthur.blake@harmonygames.co, not the persona's (robert@harmonygames.co)
[YES] L90 gmail.gmail_threads insert robert@harmonygames.co/1856982378087295205 - row user_email is the persona (robert@harmonygames.co)
[YES LB] L92 gmail.gmail_messages insert robert@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com>, robert@h - row user_email is the persona (robert@harmonygames.co)
[NO] L94 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1856982378087236711 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (robert@harmonygames.co)
[NO] L96 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (robert@harmonygames.co)
[YES] L98 gmail.gmail_threads insert robert@harmonygames.co/1856994331853686118 - row user_email is the persona (robert@harmonygames.co)
[YES LB] L100 gmail.gmail_messages insert robert@harmonygames.co/<136285951.151027292.1770967800000@email.apple.com>, robert@harmony - row user_email is the persona (robert@harmonygames.co)
[NO] L102 gmail.gmail_threads insert arthur.blake@harmonygames.co/1856994331852829558 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (robert@harmonygames.co)
[NO] L104 gmail.gmail_messages insert arthur.blake@harmonygames.co/<375944835.858142191.1770967800457@email.apple.com>, arthur.b - row is in mailbox arthur.blake@harmonygames.co, not the persona's (robert@harmonygames.co)
[NO] L106 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1856994331852922225 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (robert@harmonygames.co)
[NO] L108 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<883960163.410554888.1770967800220@email.apple.com>, leonard - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (robert@harmonygames.co)
[YES] L110 gmail.gmail_threads insert robert@harmonygames.co/1856987728970293624 - row user_email is the persona (robert@harmonygames.co)
[YES LB] L112 gmail.gmail_messages insert robert@harmonygames.co/<calendar-0b12e6f6-3c7e-3b05-f505-2adb8396bfb5@google.com>, robert@ - row user_email is the persona (robert@harmonygames.co)
[NO] L114 gmail.gmail_threads insert arthur.blake@harmonygames.co/1856987728969768237 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (robert@harmonygames.co)
[NO] L116 gmail.gmail_messages insert arthur.blake@harmonygames.co/<calendar-cbc32ea4-0175-61ec-2b3e-574fee3f8bbc@google.com>, a - row is in mailbox arthur.blake@harmonygames.co, not the persona's (robert@harmonygames.co)
[YES] L118 gcal.gcal_events insert evt_c82c0965b68d959ee4241b - persona is an attendee and holds its own copy evt_f5f279f282d20ec86bb8e5 (same ical_uid and start) on robert@harmonygames.co
[YES LB] L121 gcal.gcal_events insert evt_f5f279f282d20ec86bb8e5 - event is on the persona's own calendar robert@harmonygames.co
[YES] L123 gcal.gcal_events insert evt_949ab837443564b6be0edf - persona is an attendee and holds its own copy evt_f5f279f282d20ec86bb8e5 (same ical_uid and start) on robert@harmonygames.co
[YES LB] base slack C04UEQVDVB7/1701383740.580749 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private admin_foundersonly
[YES LB] base slack C04UEQVDVB7/1703492127.063049 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private admin_foundersonly
[YES LB] base slack C05KNDCHAAG/1770839984.194409 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private company-internal
[YES LB] base slack C05KNDCHAAG/1770842137.835489 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private company-internal
[YES LB] base slack C07C2866011/1770084297.911029 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private executives
[YES LB] base slack C07C2866011/1770489896.754049 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private executives
[YES LB] base slack C07C2866011/1770612982.268919 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private executives
[YES LB] base slack C07C2866011/1770850800.723979 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private executives
[YES LB] base slack C09UHHN6PFZ/1770404445.795829 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private prototype
[YES LB] base slack C09UHHN6PFZ/1770845002.610529 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private prototype
[YES LB] base slack C0ADGSZKR3R/1770680984.725779 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] base slack C0ADGSZKR3R/1770682219.100789 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] base slack C0ADGSZKR3R/1770789534.434749 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] base slack C0ADGSZKR3R/1770859313.592649 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] base slack C0ADGSZKR3R/1770932709.222409 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] base slack C0ADGSZKR3R/1770933450.410449 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] base slack C0ADGSZKR3R/1770933601.686309 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] base slack C0ADGSZKR3R/1770933903.645709 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] base slack C0ADGSZKR3R/1770937232.664809 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] base slack D07H86MV4DN/1770873696.684969 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of im D07H86MV4DN

summary: {'YES': 37, 'NO': 18}  unscoped rows (always visible): 84
  gcal.gcal_events: {'YES': 3}
  gdocs.docs_documents: {'YES': 2}
  gdrive.drive_files: {'YES': 4}
  gmail.gmail_messages: {'NO': 9, 'YES': 5}
  gmail.gmail_threads: {'NO': 9, 'YES': 5}
  gsheets.sheets_sheets: {'YES': 1}
  gsheets.sheets_spreadsheets: {'YES': 1}
  gslides.slides_page_elements: {'YES': 3}
  gslides.slides_pages: {'YES': 3}
  gslides.slides_presentations: {'YES': 1}
  slack.slack_messages: {'YES': 9}
verdict: PASS (0 load-bearing rows not visible)
```

- D04UP2L3E3S — Robert's DM with Leonard (im, Robert in members) LB: the hub D04UP2L3E3S/1770961200.890407 (row 6257a3c4456db0bd2aeb872619d7a364).
- D04V95AAAHW — Robert's DM with Arthur (im) LB: Arthur's reply D04V95AAAHW/1770952200.665739 (row ad623a2f0d4387109d108e767b174609) under the base root D04V95AAAHW/1770056235.480619.
- C09UHHN6PFZ — #prototype, Robert a member LB: Leonard's status C09UHHN6PFZ/1770938400.370665 (row 6908b2f17c379e809aafa6b2b169f4bf) under C09UHHN6PFZ/1770404397.819789; base C09UHHN6PFZ/1770404445.795829, C09UHHN6PFZ/1770837702.167889, C09UHHN6PFZ/1770845002.610529.
- C05433XK267 — #builds, Robert a member LB: Jenkins C05433XK267/1770932400.314774, C05433XK267/1770932970.616709.
- C0ADGSZKR3R — #winddown, Robert a member LB: C0ADGSZKR3R/1770933450.410449, C0ADGSZKR3R/1770933601.686309, C0ADGSZKR3R/1770933903.645709, C0ADGSZKR3R/1770937232.664809, C0ADGSZKR3R/1770680984.725779, C0ADGSZKR3R/1770682219.100789, C0ADGSZKR3R/1770789534.434749, C0ADGSZKR3R/1770859313.592649, C0ADGSZKR3R/1770932709.222409.
- C07C2866011 — #executives, Robert a member LB: C07C2866011/1770612982.268919, C07C2866011/1770850800.723979, C07C2866011/1770489896.754049; C04UEQVDVB7 (#admin_foundersonly) LB: C04UEQVDVB7/1701383740.580749, C04UEQVDVB7/1703492127.063049.
- Robert's mailbox (INBOX copies, user_email robert@harmonygames.co) LB: robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com> (thread robert@harmonygames.co/1856989298688559716), robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> (thread robert@harmonygames.co/1856975772058401508), robert@harmonygames.co/<136285951.151027292.1770967800000@email.apple.com> (thread robert@harmonygames.co/1856994331853686118), invitation robert@harmonygames.co/<calendar-0b12e6f6-3c7e-3b05-f505-2adb8396bfb5@google.com>.
- Drive: f_1e468a9d69ea0f0a2001f5, f_a7af6f358dd5648c11a608 and f_d996e4c434ce160dc52596 are Leonard's, shared with Robert (shared_with_emails); f_7d2c9e7822e87b92a11759 is Robert's own; the write target is Robert's root d_9f7ba94f7526d54d8482ba LB.
- Calendar: Robert's own copy evt_f5f279f282d20ec86bb8e5 (self:true) LB.
- Unscoped (visible to all): the project 0fa95761-d59b-4ff4-a8a3-15df3210ca6e, ENG-2438…ENG-2474 and their 37 notes, the card 698e6548aa9516b76c4ab475, PR harmonygames-Games/GameOfDominoes#1917, snowflake ANALYTICS.MONETIZATION.REVENUE_DAILY, confluence page_aws_infra.
- No designed denial: denied_probes is empty; evidence is always Robert's own copy (for example robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com>), and Leonard's and Arthur's mailbox and calendar copies are companions, never evidence.

## 1.F Collision

Every id the SQL mints was looked up over its full base collection (`tools/hg.py search lookup`, outputs in `plan/idcheck/`):
- gdrive (drive_files): 4 ids, 53866 base records checked, scan_complete True, 0 matches (plan/idcheck/gdrive.out.json).
- gcal (events): 3 ids, 11130 base records checked, scan_complete True, 0 matches (plan/idcheck/gcal.out.json).
- trello_card (cards): 1 ids, 803 base records checked, scan_complete True, 0 matches (plan/idcheck/trello_card.out.json).
- trello_action (actions): 1 ids, 5294 base records checked, scan_complete True, 0 matches (plan/idcheck/trello_action.out.json).
- linear_issue (issues): 37 ids, 3852 base records checked, scan_complete True, 0 matches (plan/idcheck/linear_issue.out.json).
- linear_project (projects): 1 ids, 2 base records checked, scan_complete True, 0 matches (plan/idcheck/linear_project.out.json).
- github_pr (pull_requests): 1 ids, 2629 base records checked, scan_complete True, 0 matches (plan/idcheck/github_pr.out.json).
- github_branch (branches): 1 ids, 2011 base records checked, scan_complete True, 0 matches (plan/idcheck/github_branch.out.json).
- github_commit (commits): 2 ids, 12687 base records checked, scan_complete True, 0 matches (plan/idcheck/github_commit.out.json).
- github_event (timeline_events): 2 ids, 12435 base records checked, scan_complete True, 0 matches (plan/idcheck/github_event.out.json).
- slack (messages/*/*.json): 5 ids, 687230 base records checked, scan_complete True, 0 matches (plan/idcheck/slack.out.json).
- gmail_msg (threads/*.json /messages): 11 ids, 104480 base records checked, scan_complete True, 0 matches (plan/idcheck/gmail_msg.out.json).
- gmail thread ids (single-object thread files cannot be array-looked-up): each of the 11 numeric thread ids searched over all mail — 11 of 11 with 0 matches, scan_complete True, 88728 thread files each (plan/idcheck/gmail_thread_search.txt); base_check Check A full-collection uniqueness PASS.
- Linear comment ids (comment_ + 32 hex) and Slides object ids (slide_/el_ + 12 hex) have no base rows to collide with (NB-24: the Linear export has no comments; gslides ids are per-presentation).
- Slack (channel, ts) pairs: base_check Check A PASS on the four channels' month files; the hub ts 1770961200.890407 is the only D04UP2L3E3S message after Feb 12 16:36Z.
- Header tokens: none minted (SVC_4131_EMAIL, SLACK_BOT_0005_SLACK_ID, EMPLOYEE_00NN ids are base identities used for their own people/services). Body tokens: '[PERSON_NAME_0054]' (Robert's greeting token in base App Store mail, threads/00014520.json) and a new '[IDENTIFIER_n]' submission id, as in the base template.

## Record ledger

One row per SQL statement (inserts and the three companion updates), in SQL order.

| # | SQL line | Table | Id | Pointer | Manifest element | Carrier | Reach | Discovery role |
|---|---|---|---|---|---|---|---|---|
| 1 | L6 | gdrive.drive_files | f_1e468a9d69ea0f0a2001f5 | f_1e468a9d69ea0f0a2001f5 | C2 / C8 / H1 / K2 / T2 | ● | Drive owner or share | authority |
| 2 | L9 | gdrive.drive_files | f_a7af6f358dd5648c11a608 | f_a7af6f358dd5648c11a608 | H1 decoy / T1 | ● | Drive owner or share | decoy |
| 3 | L11 | gdrive.drive_files | f_d996e4c434ce160dc52596 | f_d996e4c434ce160dc52596 | K4 / T1 / T8 | ● | Drive owner or share | claim met first |
| 4 | L13 | gdrive.drive_files | f_7d2c9e7822e87b92a11759 | f_7d2c9e7822e87b92a11759 | C5 / T16 / T3 | ● | Drive owner or share | overturning |
| 5 | L15 | gdocs.docs_documents | f_1e468a9d69ea0f0a2001f5 | f_1e468a9d69ea0f0a2001f5 | C2 / C8 / H1 / K2 / T2 | ● | Drive owner or share | authority |
| 6 | L18 | gdocs.docs_documents | f_a7af6f358dd5648c11a608 | f_a7af6f358dd5648c11a608 | H1 decoy / T1 | ● | Drive owner or share | decoy |
| 7 | L20 | gsheets.sheets_spreadsheets | f_d996e4c434ce160dc52596 | f_d996e4c434ce160dc52596 | K4 / T1 / T8 | ● | Drive owner or share | claim met first |
| 8 | L23 | gsheets.sheets_sheets | f_d996e4c434ce160dc52596#0 | f_d996e4c434ce160dc52596#0 | K4 / T1 / T8 | ● | Drive owner or share | connecting |
| 9 | L25 | gslides.slides_presentations | f_7d2c9e7822e87b92a11759 | f_7d2c9e7822e87b92a11759 | C5 / T16 / T3 | ● | Drive owner or share | overturning |
| 10 | L28 | gslides.slides_pages | f_7d2c9e7822e87b92a11759#slide_886d78971206 | f_7d2c9e7822e87b92a11759#slide_886d78971206 | C5 / T16 / T3 | ● | Drive owner or share | overturning |
| 11 | L30 | gslides.slides_page_elements | f_7d2c9e7822e87b92a11759#el_7e281c2d6d42 | f_7d2c9e7822e87b92a11759#el_7e281c2d6d42 | C5 / T16 / T3 | ● | Drive owner or share | overturning |
| 12 | L32 | gslides.slides_pages | f_7d2c9e7822e87b92a11759#slide_05405983565d | f_7d2c9e7822e87b92a11759#slide_05405983565d | C5 / T16 / T3 | ● | Drive owner or share | overturning |
| 13 | L34 | gslides.slides_page_elements | f_7d2c9e7822e87b92a11759#el_4f79d571a8ab | f_7d2c9e7822e87b92a11759#el_4f79d571a8ab | C5 / T16 / T3 | ● | Drive owner or share | overturning |
| 14 | L36 | gslides.slides_pages | f_7d2c9e7822e87b92a11759#slide_34827ed9cf24 | f_7d2c9e7822e87b92a11759#slide_34827ed9cf24 | C5 / T16 / T3 | ● | Drive owner or share | overturning |
| 15 | L38 | gslides.slides_page_elements | f_7d2c9e7822e87b92a11759#el_c30917bbd73c | f_7d2c9e7822e87b92a11759#el_c30917bbd73c | C5 / T16 / T3 | ● | Drive owner or share | overturning |
| 16 | L40 | slack.slack_messages | 9ed17488702e4bf387cc012f7bb0a509 | 9ed17488702e4bf387cc012f7bb0a509 | companion | ● | member (C05433XK267) | connecting |
| 17 | L43 | slack.slack_messages | 85bc96b0aa43bb455a58da9d8b63c060 | 85bc96b0aa43bb455a58da9d8b63c060 | companion | ● | member (C05433XK267) | connecting |
| 18 | L45 | slack.slack_messages | 6908b2f17c379e809aafa6b2b169f4bf | 6908b2f17c379e809aafa6b2b169f4bf | C5 / T16 / T3 | ● | member (C09UHHN6PFZ) | overturning |
| 19 | L47 | slack.slack_messages (UPDATE) | 73ec270a3d07eb8d8488384898be079e | 73ec270a3d07eb8d8488384898be079e | companion | ● | member (root UPDATE) | companion (root reply counters) |
| 20 | L48 | slack.slack_messages | 103ed629eef6bb64a30ab49eb5c8fe40 | 103ed629eef6bb64a30ab49eb5c8fe40 | C7 / K13 / T7 | ● | member (C09UHHN6PFZ) | overturning |
| 21 | L50 | slack.slack_messages (UPDATE) | bdb4f7af824ec3819acdf5fc3cc480ea | bdb4f7af824ec3819acdf5fc3cc480ea | companion | ● | member (root UPDATE) | companion (root reply counters) |
| 22 | L51 | slack.slack_messages | ad623a2f0d4387109d108e767b174609 | ad623a2f0d4387109d108e767b174609 | C1 / C2 / T1 | ● | member (D04V95AAAHW) | overturning |
| 23 | L53 | slack.slack_messages (UPDATE) | bc4bc3d0e2a0ea6ae92cb2a9712e8f76 | bc4bc3d0e2a0ea6ae92cb2a9712e8f76 | companion | ● | member (root UPDATE) | companion (root reply counters) |
| 24 | L54 | slack.slack_messages | 6257a3c4456db0bd2aeb872619d7a364 | 6257a3c4456db0bd2aeb872619d7a364 | K1 | ● | member (D04UP2L3E3S) | first link (anchor AN1) |
| 25 | L56 | trello.trello_cards | 698e6548aa9516b76c4ab475 | 698e6548aa9516b76c4ab475 | C7 / K6 / T7 | ● | unscoped | connecting |
| 26 | L59 | trello.trello_actions | 698e65489a4031a95d3ce53e | 698e65489a4031a95d3ce53e | companion | ● | unscoped | connecting |
| 27 | L61 | gmail.gmail_threads | arthur.blake@harmonygames.co/1856975772057961391 | arthur.blake@harmonygames.co/1856975772057961391 | companion | ● | other mailbox (companion) | companion copy |
| 28 | L64 | gmail.gmail_messages | arthur.blake@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> | arthur.blake@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> | companion | ● | other mailbox (companion) | companion copy |
| 29 | L66 | gmail.gmail_threads | robert@harmonygames.co/1856975772058401508 | robert@harmonygames.co/1856975772058401508 | T4 | ● | Robert's mailbox | connecting |
| 30 | L68 | gmail.gmail_messages | robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> | robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> | C3 / T4 | ● | Robert's mailbox | overturning |
| 31 | L70 | gmail.gmail_threads | leonard.hayes@harmonygames.co/1856975772058497766 | leonard.hayes@harmonygames.co/1856975772058497766 | companion | ● | other mailbox (companion) | companion copy |
| 32 | L72 | gmail.gmail_messages | leonard.hayes@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> | leonard.hayes@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> | companion | ● | other mailbox (companion) | companion copy |
| 33 | L74 | gmail.gmail_threads | leonard.hayes@harmonygames.co/1856989298688254292 | leonard.hayes@harmonygames.co/1856989298688254292 | companion | ● | other mailbox (companion) | companion copy |
| 34 | L76 | gmail.gmail_messages | leonard.hayes@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com> | leonard.hayes@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com> | companion | ● | other mailbox (companion) | companion copy |
| 35 | L78 | gmail.gmail_threads | robert@harmonygames.co/1856989298688559716 | robert@harmonygames.co/1856989298688559716 | H3 / K5 / T10 | ● | Robert's mailbox | authority |
| 36 | L80 | gmail.gmail_messages | robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com> | robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com> | H3 / K5 / T10 | ● | Robert's mailbox | authority |
| 37 | L82 | gmail.gmail_threads | arthur.blake@harmonygames.co/1856989298688898804 | arthur.blake@harmonygames.co/1856989298688898804 | companion | ● | other mailbox (companion) | companion copy |
| 38 | L84 | gmail.gmail_messages | arthur.blake@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com> | arthur.blake@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com> | companion | ● | other mailbox (companion) | companion copy |
| 39 | L86 | gmail.gmail_threads | arthur.blake@harmonygames.co/1856982378087055316 | arthur.blake@harmonygames.co/1856982378087055316 | companion | ● | other mailbox (companion) | companion copy |
| 40 | L88 | gmail.gmail_messages | arthur.blake@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com> | arthur.blake@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com> | companion | ● | other mailbox (companion) | companion copy |
| 41 | L90 | gmail.gmail_threads | robert@harmonygames.co/1856982378087295205 | robert@harmonygames.co/1856982378087295205 | T19 | ● | Robert's mailbox | connecting |
| 42 | L92 | gmail.gmail_messages | robert@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com> | robert@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com> | C8 / T19 | ● | Robert's mailbox | overturning |
| 43 | L94 | gmail.gmail_threads | leonard.hayes@harmonygames.co/1856982378087236711 | leonard.hayes@harmonygames.co/1856982378087236711 | companion | ● | other mailbox (companion) | companion copy |
| 44 | L96 | gmail.gmail_messages | leonard.hayes@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com> | leonard.hayes@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com> | companion | ● | other mailbox (companion) | companion copy |
| 45 | L98 | gmail.gmail_threads | robert@harmonygames.co/1856994331853686118 | robert@harmonygames.co/1856994331853686118 | T5 | ● | Robert's mailbox | connecting |
| 46 | L100 | gmail.gmail_messages | robert@harmonygames.co/<136285951.151027292.1770967800000@email.apple.com> | robert@harmonygames.co/<136285951.151027292.1770967800000@email.apple.com> | C4 / T5 | ● | Robert's mailbox | overturning |
| 47 | L102 | gmail.gmail_threads | arthur.blake@harmonygames.co/1856994331852829558 | arthur.blake@harmonygames.co/1856994331852829558 | companion | ● | other mailbox (companion) | companion copy |
| 48 | L104 | gmail.gmail_messages | arthur.blake@harmonygames.co/<375944835.858142191.1770967800457@email.apple.com> | arthur.blake@harmonygames.co/<375944835.858142191.1770967800457@email.apple.com> | companion | ● | other mailbox (companion) | companion copy |
| 49 | L106 | gmail.gmail_threads | leonard.hayes@harmonygames.co/1856994331852922225 | leonard.hayes@harmonygames.co/1856994331852922225 | companion | ● | other mailbox (companion) | companion copy |
| 50 | L108 | gmail.gmail_messages | leonard.hayes@harmonygames.co/<883960163.410554888.1770967800220@email.apple.com> | leonard.hayes@harmonygames.co/<883960163.410554888.1770967800220@email.apple.com> | companion | ● | other mailbox (companion) | companion copy |
| 51 | L110 | gmail.gmail_threads | robert@harmonygames.co/1856987728970293624 | robert@harmonygames.co/1856987728970293624 | companion | ● | Robert's mailbox | connecting |
| 52 | L112 | gmail.gmail_messages | robert@harmonygames.co/<calendar-0b12e6f6-3c7e-3b05-f505-2adb8396bfb5@google.com> | robert@harmonygames.co/<calendar-0b12e6f6-3c7e-3b05-f505-2adb8396bfb5@google.com> | companion | ● | Robert's mailbox | companion (INT-11 invitation) |
| 53 | L114 | gmail.gmail_threads | arthur.blake@harmonygames.co/1856987728969768237 | arthur.blake@harmonygames.co/1856987728969768237 | companion | ● | other mailbox (companion) | companion copy |
| 54 | L116 | gmail.gmail_messages | arthur.blake@harmonygames.co/<calendar-cbc32ea4-0175-61ec-2b3e-574fee3f8bbc@google.com> | arthur.blake@harmonygames.co/<calendar-cbc32ea4-0175-61ec-2b3e-574fee3f8bbc@google.com> | companion | ● | other mailbox (companion) | companion copy |
| 55 | L118 | gcal.gcal_events | evt_c82c0965b68d959ee4241b | evt_c82c0965b68d959ee4241b | K11 | ● (summary, time, attendees; description ○) | other calendar (companion) | companion copy |
| 56 | L121 | gcal.gcal_events | evt_f5f279f282d20ec86bb8e5 | evt_f5f279f282d20ec86bb8e5 | K11 | ● (summary, time, attendees; description ○) | Robert's calendar (self) | connecting |
| 57 | L123 | gcal.gcal_events | evt_949ab837443564b6be0edf | evt_949ab837443564b6be0edf | companion | ● (summary, time, attendees; description ○) | other calendar (companion) | companion copy |
| 58 | L125 | github.github_pull_requests | harmonygames-Games/GameOfDominoes#1917 | harmonygames-Games/GameOfDominoes#1917 | C4 / T5 | ● | unscoped | connecting |
| 59 | L128 | github.github_branches | harmonygames-Games/GameOfDominoes:arthur.blake/supportEmail | harmonygames-Games/GameOfDominoes#1917 | companion | ● | unscoped | connecting |
| 60 | L130 | github.github_commits | d67e7d0277db893512d589e28ded199e5177b1c6 | harmonygames-Games/GameOfDominoes#1917 | companion | ● | unscoped | connecting |
| 61 | L132 | github.github_commits | e1f05eabfc9ed3f2579d0f16e9fa281858268bda | harmonygames-Games/GameOfDominoes#1917 | companion | ● | unscoped | connecting |
| 62 | L134 | github.github_pull_request_commits | harmonygames-Games/GameOfDominoes#1917#c_0 | harmonygames-Games/GameOfDominoes#1917 | companion | ● | unscoped | connecting |
| 63 | L136 | github.github_timeline_events | harmonygames-Games/GameOfDominoes#1917#ev_1 | harmonygames-Games/GameOfDominoes#1917 | companion | ● | unscoped | connecting |
| 64 | L138 | github.github_timeline_events | harmonygames-Games/GameOfDominoes#1917#ev_2 | harmonygames-Games/GameOfDominoes#1917 | companion | ● | unscoped | connecting |
| 65 | L140 | linear.linear_projects | 0fa95761-d59b-4ff4-a8a3-15df3210ca6e | team_ENG | K3 | ● | unscoped | first link (anchor AN2) |
| 66 | L143 | linear.linear_issues | ENG-2438 | ENG-2438 | cohort: Combo Fighter | ● | unscoped | cohort record |
| 67 | L145 | linear.linear_comments | comment_2bd90ac9c9ce19c08895c119c9e2f3a1 | ENG-2438 | cohort note: Combo Fighter | ● (§6b) | unscoped | connecting (the item's own note) |
| 68 | L147 | linear.linear_issues | ENG-2439 | ENG-2439 | cohort: Domino Delights | ● | unscoped | cohort record |
| 69 | L149 | linear.linear_comments | comment_6ec1dd4689e56e10303263a92d5b7d2a | ENG-2439 | cohort note: Domino Delights | ● (§6b) | unscoped | connecting (the item's own note) |
| 70 | L151 | linear.linear_issues | ENG-2440 | ENG-2440 | cohort: Zombie Match | ● | unscoped | cohort record |
| 71 | L153 | linear.linear_comments | comment_d6c4df6b6324e146cf95c0c24be9e8f7 | ENG-2440 | cohort note: Zombie Match | ● (§6b) | unscoped | connecting (the item's own note) |
| 72 | L155 | linear.linear_issues | ENG-2441 | ENG-2441 | cohort: Domino Delights production account (AWS) | ● | unscoped | cohort record |
| 73 | L157 | linear.linear_comments | comment_c1664b356a8441e581cebdfecc39d09d | ENG-2441 | C1 / T1 / cohort note: Domino Delights production account (AWS) | ● (§6b) | unscoped | claim met first |
| 74 | L159 | linear.linear_issues | ENG-2442 | ENG-2442 | cohort: Domino Delights dev account (AWS) | ● | unscoped | cohort record |
| 75 | L161 | linear.linear_comments | comment_c32445f461c7fae20774dccf9593dbc8 | ENG-2442 | cohort note: Domino Delights dev account (AWS) | ● (§6b) | unscoped | connecting (the item's own note) |
| 76 | L163 | linear.linear_issues | ENG-2443 | ENG-2443 | cohort: Zombie Match account (AWS) | ● | unscoped | cohort record |
| 77 | L165 | linear.linear_comments | comment_a317e10875adb686553e43989c1bab61 | ENG-2443 | cohort note: Zombie Match account (AWS) | ● (§6b) | unscoped | connecting (the item's own note) |
| 78 | L167 | linear.linear_issues | ENG-2444 | ENG-2444 | cohort: Analytics pipeline account (AWS) | ● | unscoped | cohort record |
| 79 | L169 | linear.linear_comments | comment_c1bb860b536a20f7ffe89f31443b1b86 | ENG-2444 | cohort note: Analytics pipeline account (AWS) | ● (§6b) | unscoped | connecting (the item's own note) |
| 80 | L171 | linear.linear_issues | ENG-2445 | ENG-2445 | cohort: Combo Fighter backend and auth stacks (AWS) | ● | unscoped | cohort record |
| 81 | L173 | linear.linear_comments | comment_d7d8b2ded8a9c92fceed304abda87342 | ENG-2445 | C8 / T19 / cohort note: Combo Fighter backend and auth stacks (AWS) | ● (§6b) | unscoped | claim met first |
| 82 | L175 | linear.linear_issues | ENG-2446 | ENG-2446 | cohort: Build machines | ● | unscoped | cohort record |
| 83 | L177 | linear.linear_comments | comment_7a0dea6299c7963e9a3e673996bd47fe | ENG-2446 | C8 / cohort note: Build machines | ● (§6b) | unscoped | connecting (the item's own note) |
| 84 | L179 | linear.linear_issues | ENG-2447 | ENG-2447 | cohort: Metabase | ● | unscoped | cohort record |
| 85 | L181 | linear.linear_comments | comment_53482e2398959d50dc774b5e4a921c3d | ENG-2447 | C3 / T4 / cohort note: Metabase | ● (§6b) | unscoped | claim met first |
| 86 | L183 | linear.linear_issues | ENG-2448 | ENG-2448 | cohort: dbt | ● | unscoped | cohort record |
| 87 | L185 | linear.linear_comments | comment_473bc9e0ac123becac17dbacd838b73e | ENG-2448 | cohort note: dbt | ● (§6b) | unscoped | connecting (the item's own note) |
| 88 | L187 | linear.linear_issues | ENG-2449 | ENG-2449 | cohort: GitHub | ● | unscoped | cohort record |
| 89 | L189 | linear.linear_comments | comment_def5ce95998f963949dea6aa472e263f | ENG-2449 | cohort note: GitHub | ● (§6b) | unscoped | connecting (the item's own note) |
| 90 | L191 | linear.linear_issues | ENG-2450 | ENG-2450 | cohort: Singular | ● | unscoped | cohort record |
| 91 | L193 | linear.linear_comments | comment_e422844e1fee1bd5700467a3c2bcbdd8 | ENG-2450 | cohort note: Singular | ● (§6b) | unscoped | connecting (the item's own note) |
| 92 | L195 | linear.linear_issues | ENG-2451 | ENG-2451 | cohort: AppsFlyer | ● | unscoped | cohort record |
| 93 | L197 | linear.linear_comments | comment_8f9257643146016aad03d280b325282b | ENG-2451 | cohort note: AppsFlyer | ● (§6b) | unscoped | connecting (the item's own note) |
| 94 | L199 | linear.linear_issues | ENG-2452 | ENG-2452 | cohort: Google Analytics | ● | unscoped | cohort record |
| 95 | L201 | linear.linear_comments | comment_17c00e145364f71740a299e868acb9f6 | ENG-2452 | cohort note: Google Analytics | ● (§6b) | unscoped | connecting (the item's own note) |
| 96 | L203 | linear.linear_issues | ENG-2453 | ENG-2453 | cohort: Figma | ● | unscoped | cohort record |
| 97 | L205 | linear.linear_comments | comment_3a8e425288db648883caa9b699488f6f | ENG-2453 | cohort note: Figma | ● (§6b) | unscoped | connecting (the item's own note) |
| 98 | L207 | linear.linear_issues | ENG-2454 | ENG-2454 | C7 / cohort: layer.ai | ● | unscoped | cohort record |
| 99 | L209 | linear.linear_comments | comment_3f50781a558dfa9fb3255d5f9c74d4d1 | ENG-2454 | cohort note: layer.ai | ● (§6b) | unscoped | claim met first |
| 100 | L211 | linear.linear_issues | ENG-2455 | ENG-2455 | cohort: Soundly | ● | unscoped | cohort record |
| 101 | L213 | linear.linear_comments | comment_238a566b5bb7fac32eabbe7db0fe729c | ENG-2455 | cohort note: Soundly | ● (§6b) | unscoped | connecting (the item's own note) |
| 102 | L215 | linear.linear_issues | ENG-2456 | ENG-2456 | cohort: Kapwing | ● | unscoped | cohort record |
| 103 | L217 | linear.linear_comments | comment_8c69b5b90f9f6c03a0a168d25e6b75bd | ENG-2456 | cohort note: Kapwing | ● (§6b) | unscoped | connecting (the item's own note) |
| 104 | L219 | linear.linear_issues | ENG-2457 | ENG-2457 | cohort: Cursor | ● | unscoped | cohort record |
| 105 | L221 | linear.linear_comments | comment_6d9a7697f03e8ebec935efe9c6462fa7 | ENG-2457 | cohort note: Cursor | ● (§6b) | unscoped | connecting (the item's own note) |
| 106 | L223 | linear.linear_issues | ENG-2458 | ENG-2458 | cohort: CodeRabbit | ● | unscoped | cohort record |
| 107 | L225 | linear.linear_comments | comment_28b91f876262c04cd670515d3dc0bb1d | ENG-2458 | cohort note: CodeRabbit | ● (§6b) | unscoped | connecting (the item's own note) |
| 108 | L227 | linear.linear_issues | ENG-2459 | ENG-2459 | cohort: Unity Pro | ● | unscoped | cohort record |
| 109 | L229 | linear.linear_comments | comment_ce75598b67b6bd27af977a93416b316d | ENG-2459 | cohort note: Unity Pro | ● (§6b) | unscoped | connecting (the item's own note) |
| 110 | L231 | linear.linear_issues | ENG-2460 | ENG-2460 | cohort: Zapier | ● | unscoped | cohort record |
| 111 | L233 | linear.linear_comments | comment_16b0938c67dfbd4835546ec86ef90c7c | ENG-2460 | cohort note: Zapier | ● (§6b) | unscoped | connecting (the item's own note) |
| 112 | L235 | linear.linear_issues | ENG-2461 | ENG-2461 | cohort: Helpshift | ● | unscoped | cohort record |
| 113 | L237 | linear.linear_comments | comment_fa730ebd8ddbad87b79902525a3e54e1 | ENG-2461 | cohort note: Helpshift | ● (§6b) | unscoped | connecting (the item's own note) |
| 114 | L239 | linear.linear_issues | ENG-2462 | ENG-2462 | cohort: Domino Delights player support | ● | unscoped | cohort record |
| 115 | L241 | linear.linear_comments | comment_7f8d7a9d959ca264f47b0e21d76416d1 | ENG-2462 | C4 / T5 / cohort note: Domino Delights player support | ● (§6b) | unscoped | claim met first |
| 116 | L243 | linear.linear_issues | ENG-2463 | ENG-2463 | cohort: Slack | ● | unscoped | cohort record |
| 117 | L245 | linear.linear_comments | comment_a7b40e52bcb007837a4db4d5b7ed035a | ENG-2463 | cohort note: Slack | ● (§6b) | unscoped | connecting (the item's own note) |
| 118 | L247 | linear.linear_issues | ENG-2464 | ENG-2464 | cohort: Google Workspace | ● | unscoped | cohort record |
| 119 | L249 | linear.linear_comments | comment_dbe6caf3f2c67506e21a9c2956454876 | ENG-2464 | cohort note: Google Workspace | ● (§6b) | unscoped | connecting (the item's own note) |
| 120 | L251 | linear.linear_issues | ENG-2465 | ENG-2465 | cohort: Linear | ● | unscoped | cohort record |
| 121 | L253 | linear.linear_comments | comment_e2fedacbbbb8dc282d867f5339d8feb2 | ENG-2465 | cohort note: Linear | ● (§6b) | unscoped | connecting (the item's own note) |
| 122 | L255 | linear.linear_issues | ENG-2466 | ENG-2466 | cohort: Deel | ● | unscoped | cohort record |
| 123 | L257 | linear.linear_comments | comment_3a33e2aba4b2faaa16df959db07bcfc4 | ENG-2466 | cohort note: Deel | ● (§6b) | unscoped | connecting (the item's own note) |
| 124 | L259 | linear.linear_issues | ENG-2467 | ENG-2467 | cohort: Gusto | ● | unscoped | cohort record |
| 125 | L261 | linear.linear_comments | comment_5768cc5c5fcd81a9678acad18e0df43d | ENG-2467 | cohort note: Gusto | ● (§6b) | unscoped | connecting (the item's own note) |
| 126 | L263 | linear.linear_issues | ENG-2468 | ENG-2468 | cohort: Intuit | ● | unscoped | cohort record |
| 127 | L265 | linear.linear_comments | comment_33d0671cf04080950a6dfbda009786c4 | ENG-2468 | cohort note: Intuit | ● (§6b) | unscoped | connecting (the item's own note) |
| 128 | L267 | linear.linear_issues | ENG-2469 | ENG-2469 | cohort: Carta | ● | unscoped | cohort record |
| 129 | L269 | linear.linear_comments | comment_1179f13abea9dbf2b6f2efa69341a825 | ENG-2469 | cohort note: Carta | ● (§6b) | unscoped | connecting (the item's own note) |
| 130 | L271 | linear.linear_issues | ENG-2470 | ENG-2470 | cohort: Apple developer account | ● | unscoped | cohort record |
| 131 | L273 | linear.linear_comments | comment_c7be2f4808bcda66cf9fbaf1cb05c352 | ENG-2470 | cohort note: Apple developer account | ● (§6b) | unscoped | connecting (the item's own note) |
| 132 | L275 | linear.linear_issues | ENG-2471 | ENG-2471 | cohort: Google Play developer account | ● | unscoped | cohort record |
| 133 | L277 | linear.linear_comments | comment_8ad59204fdc7684a99cfc40a5a0b2555 | ENG-2471 | cohort note: Google Play developer account | ● (§6b) | unscoped | connecting (the item's own note) |
| 134 | L279 | linear.linear_issues | ENG-2472 | ENG-2472 | cohort: Calm Play LLC | ● | unscoped | cohort record |
| 135 | L281 | linear.linear_comments | comment_ffcbb4c79467be3bdd75a1dd3b8da04f | ENG-2472 | cohort note: Calm Play LLC | ● (§6b) | unscoped | claim met first |
| 136 | L283 | linear.linear_issues | ENG-2473 | ENG-2473 | cohort: Unity Ads balance | ● | unscoped | cohort record |
| 137 | L285 | linear.linear_comments | comment_07e7f077926a112c521177e769276644 | ENG-2473 | cohort note: Unity Ads balance | ● (§6b) | unscoped | connecting (the item's own note) |
| 138 | L287 | linear.linear_issues | ENG-2474 | ENG-2474 | cohort: Playable vendor | ● | unscoped | cohort record |
| 139 | L289 | linear.linear_comments | comment_39bd0d5ecdece2f5bf9639ff5cdfebac | ENG-2474 | cohort note: Playable vendor | ● (§6b) | unscoped | connecting (the item's own note) |

## Findability and discovery-order proofs

- Hub (AN1) D04UP2L3E3S/1770961200.890407 (row 6257a3c4456db0bd2aeb872619d7a364): Leonard → Robert, Thu Feb 12 21:40 PT; the prompt names it ('Leonard's DM'); the newest message in D04UP2L3E3S. First link.
- Project (AN2) 0fa95761-d59b-4ff4-a8a3-15df3210ca6e 'LLC take-over': named by the hub ('the LLC project in linear'); linear_list_projects returns it; its 37 issues by linear_list_issues (titles and states only; no comment text in bulk, Ask_Carriers §6b).
- Ground rules H1 f_1e468a9d69ea0f0a2001f5: the hub names 'the ground rules doc'; a Drive search for 'ground rules' or 'LLC' returns it and the older decoy f_a7af6f358dd5648c11a608 ('LLC notes', Feb 10: 'DD and ZM both come with CF. Servers about $1k a month'), which differs on the take test and the hosting figure.
- Warehouse H2 snowflake ANALYTICS.MONETIZATION.REVENUE_DAILY: the ground rules name 'the warehouse's daily revenue table'; snowflake_list_tables shows REVENUE_DAILY (and REVENUE_DAILY_V2, same January sums); the decoy is BoomBit's campaign update C09SWTHEMEW/1770725775.479449 (retention and installs for its own test: decoy_scope issuer).
- Split email H3 robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com> (thread robert@harmonygames.co/1856989298688559716): the hub says 'I'll email you how we split the money'; a mail search for 'LLC' or 'split' returns it; the competing hit is Leonard's January pro forma cap table C07C2866011/1768417784.194359 (equity, not the LLC's running cost).
- T1 CORR: claim met first — #winddown C0ADGSZKR3R/1770680984.725779 (~$1k) and C0ADGSZKR3R/1770682219.100789 (300), the notes doc and draft (f_a7af6f358dd5648c11a608, f_d996e4c434ce160dc52596) and Leonard's issue note comment_c1664b356a8441e581cebdfecc39d09d; overturned by Arthur's DM reply D04V95AAAHW/1770952200.665739 (Feb 13 03:10Z, $140 from March) under the Feb 2 git-debugging root D04V95AAAHW/1770056235.480619: met first because #winddown is read by every run and the DM reply is threaded under an unrelated root; decisive because the costing rule takes 'what it bills now, going by whoever runs it' (Arthur runs the AWS accounts).
- T2 AUTH: the take test (ground rules) needs January income per game; only REVENUE_DAILY gives it (DD 183.11, ZM 0.00); Slack offers 'We make way less than $1K' (C0ADGSZKR3R/1770686243.781429), which decides nothing against $140.
- T3/T16 FILT: the campaign is in no list (not in the project, the checklist or the keep list); C09UHHN6PFZ/1770404445.795829 ($100/day, Feb 6) and C07C2866011/1770489896.754049 (both live, Feb 7) are met in channel history; Leonard's status C09UHHN6PFZ/1770938400.370665 (Feb 12, a reply under the Feb 6 root) says only the VO campaign is still on, $100/day capped at $3,000 a month on his card till the end of Feb, moving to 'our new company's card from March' (rev4: no record that carries the campaign uses the project word the rev3 run searched first); Robert's deck f_7d2c9e7822e87b92a11759 carries the same $100/day line.
- T4 COMPLETE: claim met first — Leonard's #winddown action items C0ADGSZKR3R/1770933903.645709 (~$300 for Metabase and dbt) and his issue note comment_53482e2398959d50dc774b5e4a921c3d ('about $300 a month with dbt, more or less'); Arthur's #winddown line C0ADGSZKR3R/1770937232.664809 moves the payer; his mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> (Feb 13 02:35Z) gives $248 carried through May; found by a mail search for any of the three tools.
- T5 DONE: claim — Arthur's note comment_7f8d7a9d959ca264f47b0e21d76416d1 ('done ... merged in #1917') and the merged PR harmonygames-Games/GameOfDominoes#1917; overturned by the App Store notice robert@harmonygames.co/<136285951.151027292.1770967800000@email.apple.com> (Feb 13 07:30Z: the support option only opens an email draft and does nothing without a mail account — the support-email build's behaviour), tied to the support-email build by Jenkins C05433XK267/1770932970.616709 (#218, 'Replace Helpshift with support email'); met first because the note sits on the issue and the notice among Robert's App Store mail. Rev4: the project description's Done rule ('Done if ... the LLC takes it and nothing is left to do on it') makes a missed notice flip ENG-2462 to Done instead of Todo with Arthur.
- Calm Play (control row; rev4 purged EXC, which the rev3 pre-check showed was never live): Leonard's note on ENG-2472 ('Calm Play could just be our LLC') is overruled by the ground rules' 'The LLC is the new one Blake and I are setting up for the three of us' and 'anything Harmony Games owns comes to it only through Sunset's sale'; C04UEQVDVB7/1701383740.580749 and C04UEQVDVB7/1703492127.063049 (2023: fully owned subsidiary) agree.
- T7 DATE (rev4): Leonard's ENG-2454 note comment_3f50781a558dfa9fb3255d5f9c74d4d1 says only 'cancelled it on the 11th', so the item reads as closed; C09UHHN6PFZ/1770837702.167889 (Feb 11: layer.ai access until March 3rd) and Leonard's reply under it C09UHHN6PFZ/1770923700.470906 (Feb 12 19:15Z: 'the CF character concept art is only in layer.ai, can you pull it out yourself before then? the art goes with CF, there's nothing on the layer account for our new company to take, it just lapses', the parent's thread fields updated) give the step and its owner; the card 698e6548aa9516b76c4ab475 keeps an item's own deadline (export by Mar 3) and the ground rules bring a game's art over. A Slack search for 'layer.ai' returns the post (the only Feb 2026 hit) and the thread. GitHub: the checklist C0ADGSZKR3R/1770933450.410449 (keep until the data is sold, then transfer).
- T19 STACKS (rev4): claim met first — Arthur's ENG-2445 note comment_d7d8b2ded8a9c92fceed304abda87342 (Feb 13 00:58Z: CF's own account about $95 a month on HG's AWS bill), read by every run that opens the issue comments; overturned by Arthur's email robert@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com> (thread robert@harmonygames.co/1856982378087295205, Feb 13 04:20Z, 'jenkins', to Robert, cc Leonard), second paragraph: he shut down the extra copy of CF's backend still running from the January redeploy, so CF's account bills $62 a month now. The costing rule takes what it bills now from whoever runs it. Found by a mail search for 'jenkins', 'backend', 'AWS' or Arthur's address, or by reading Robert's Feb 13 mail; its snippet covers only the first paragraph (the build boxes).
- T10 split: the pro forma post C07C2866011/1768417784.194359 and the $25K post C07C2866011/1767730784.379929 are met by a 'split' or 'founders' search; the split email robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com> (Feb 13) is the rule.
- T17 GitHub: C05KNDCHAAG/1770842137.835489 (Feb 11, repos to the LLC) is met first; the later checklist C0ADGSZKR3R/1770933450.410449 (Feb 12) keeps GitHub under HG until the data is sold (L13: dated claim).

## Self-validation

| QC category | Tool-enforced (result) | Manual (evidence) |
|---|---|---|
| Missing Universe Data | check-sql PASS (1.E) | every deciding fact persona-readable: D04V95AAAHW/1770952200.665739, robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com>, robert@harmonygames.co/<136285951.151027292.1770967800000@email.apple.com>, C09UHHN6PFZ/1770938400.370665, REVENUE_DAILY (unscoped), C04UEQVDVB7/1701383740.580749, C09UHHN6PFZ/1770837702.167889 |
| Temporal Field | sql_lint 0 errors; base_check Check C PASS | text dates agree: the hub (Thu night) says 'my draft from Tuesday' = f_d996e4c434ce160dc52596 (Tue Feb 10 10:30 PT) and 'Monday's call' = evt_f5f279f282d20ec86bb8e5 (Mon Feb 16); the deck (Feb 8) follows the campaign's creation (Feb 6); the project (23:24Z) and issues precede the card (23:42Z), which precedes the ground rules (23:46Z); the PR merges (21:10Z) before the build (21:40Z) and the store notice (Feb 13 07:30Z); every issue note follows its issue's created_at |
| Cross-service Referential | base_check Check A PASS | one figure per item across services: $140 only in D04V95AAAHW/1770952200.665739; $62 only in comment_d7d8b2ded8a9c92fceed304abda87342; $248 only in robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> (fact_check --no-leak); #1917 in the note, the PR and the Jenkins change line |
| Quantitative / Reconciliation | reply counters updated on D04V95AAAHW/1770056235.480619 and C09UHHN6PFZ/1770404397.819789 (reply_count 1, reply_users_count 1, latest_reply = the seeded ts) | $248 = 100 + 100 + 48 (Arthur's mail; base dbt receipt $100 leonard.hayes@harmonygames.co/1855983949220444975); $3,000 a month = the cap on $100/day in Leonard's status (C09UHHN6PFZ/1770404445.795829 for the daily budget); no total is seeded |
| State / Lifecycle | the 37 issues are Backlog without stamps; the PR is closed + merged with merged and closed events | statuses agree with #winddown: cancelled Soundly, Cursor, CodeRabbit, Kapwing, Zapier, layer (C0ADGSZKR3R/1770839322.836779, C0ADGSZKR3R/1770937188.477219, C0ADGSZKR3R/1770936655.574079, C0ADGSZKR3R/1770933450.410449, C0ADGSZKR3R/1770837793.168589); kept Deel, Gusto, Intuit, Linear (C0ADGSZKR3R/1770933601.686309) |
| Identifier / Format | eval lint FAIL 0 CHECK 0 | ids follow base schemes (1.A); roster addresses in every seeded row; base tokens kept (usr_Robert I10, EMPLOYEE_0025_GITHUB_USERNAME I08) |
| Semantic / Category | — | titles match content (f_1e468a9d69ea0f0a2001f5, 698e6548aa9516b76c4ab475, 0fa95761-d59b-4ff4-a8a3-15df3210ca6e, evt_f5f279f282d20ec86bb8e5); one name per item (the issue titles are the plan's item names) |
| Other | — | voice per 1.C; no record states a decision, a total, a share or the plan |

## Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| gcal | INT-11 | invitation mails | seeded for Robert (robert@harmonygames.co/<calendar-0b12e6f6-3c7e-3b05-f505-2adb8396bfb5@google.com>) and Arthur from Leonard, with all three calendar copies (R08 match) |
| jenkins → slack | INT-06 | #builds job start + result posts | seeded as a pair for DD iOS Submission #218 (C05433XK267/1770932400.314774, C05433XK267/1770932970.616709); base builds continue to Feb 12 |
| app store connect → gmail | INT-08 | review mail | the seeded notice robert@harmonygames.co/<136285951.151027292.1770967800000@email.apple.com> is itself the INT-08 family ('We noticed an issue with your submission.') |
| github → slack | INT-01, INT-02, INT-20 | GitHub app mirror / push posts | none: the GameOfDominoes mirror window ends 2025-12-26 (integrations.json); declared in integration_exceptions for harmonygames-Games/GameOfDominoes#1917 |
| github → gmail | INT-12 | notification mails | none (optional companion; Arthur opened and merged #1917 himself); declared |
| coderabbit → github | INT-23 | CodeRabbit summary comment | none on #1917 (optional; CodeRabbit cancelled Feb 12 22:50Z, C0ADGSZKR3R/1770936655.574079); declared |
| linear | INT-03, INT-04, INT-05 | linear[bot] PR comment / Slack DM / digests | none: #1917 names no Linear key; the workspace went to guests Feb 11 (C09UHHN6PFZ/1770842566.250369) |
| gdrive | INT-13 | Drive Slack-app share DM | none for f_1e468a9d69ea0f0a2001f5, f_a7af6f358dd5648c11a608, f_d996e4c434ce160dc52596, f_7d2c9e7822e87b92a11759; declared |
| slack | INT-22 | Slack e-mail notifications | none (DMs between full members; no base notification mail for D04UP2L3E3S or D04V95AAAHW in Feb) |
| trello | INT-21 | no Trello→Slack integration | none (the card 698e6548aa9516b76c4ab475 posts nowhere) |
| gdocs, gsheets, gslides | none | Drive rows mirror every native file (owner, shared_with) | seeded |

## Touched-data census and coherence hazards

Touched data: the hub DM D04UP2L3E3S (Feb 12–13); Robert's DM with Arthur D04V95AAAHW (root D04V95AAAHW/1770056235.480619, counters updated); #prototype C09UHHN6PFZ (Feb 6–12: C09UHHN6PFZ/1770404397.819789 counters updated, C09UHHN6PFZ/1770404445.795829, C09UHHN6PFZ/1770837702.167889, C09UHHN6PFZ/1770842566.250369, C09UHHN6PFZ/1770845002.610529, C09UHHN6PFZ/1770844309.583109); #winddown C0ADGSZKR3R (Feb 9–12, every line a correct run reads: checklist, keep list, action items, cancellations); #executives C07C2866011 (Jan 6, Jan 14, Feb 3–11); #admin_foundersonly C04UEQVDVB7 (2023 Calm Play posts); #builds C05433XK267 (Jan 28 #216/#217, Feb 12); #boombit C09SWTHEMEW (Feb 10–13); Robert's mailbox (the three seeded threads, the invitation, base App Store mail threads/00014520.json); the four Drive files; the founders' board 640643a3fd8f3ca308d9318e; the project and ENG-2438…ENG-2474; GameOfDominoes (#1916, branches/981, #1917); snowflake REVENUE_DAILY / REVENUE_DAILY_V2; confluence page_aws_infra; Arthur's mailbox only for the cross-check of Kapwing (blake@harmonygames.co_1856962040028188034.json) and the GitHub receipts.

Hazards from coherence_hazards.json (normal KB):
- temporal: T07 — no seeded #prototype message is dated Feb 13 (the status is Feb 12 23:20Z; rev4's layer.ai reply Feb 12 19:15Z, after the channel's last base message that day, /726 at 19:08Z) and none points at a missing artifact; T06 — the card's dateLastActivity equals its only action (createCard, Feb 12 23:42Z); T02 none in scope — every seeded mail thread has one message.
- semantic: S04 — Arthur's GitHub login is the base token, no display name is written; S06 none in scope — no contact is created or edited.
- referential: R04 — the hub names the docs in words, no Drive link (Google-native link ids never equal f_ ids); R07 — no PR comment is seeded on #1917, whose repo's mirror window ended Dec 26; R08 — the seeded invitation mails have their three calendar rows.
- quantitative: Q01/Q02/Q03 — all three seeded thread replies update their roots' reply_count, reply_users_count and latest_reply (rev4 adds Leonard's layer.ai post bdb4f7af824ec3819acdf5fc3cc480ea); Q07 — the AWS figures quoted different ways (~$1k vs others) are the older versions of T1, overturned by Arthur's dated $140, and (rev4) CF's ~$95 on ENG-2445 is the older version of T19, overturned by Arthur's dated $62 (no base record states a CF account figure; base deploy notes D04UY3DQJE5 2026-01 show the CF backend on us-west-1 and then us-east-1); Q09 — REVENUE_DAILY and REVENUE_DAILY_V2 agree on the January sums (DD 183.11, CF 7.36, ZM 0.00); Q10/Q11 — the mailbox copies and calendar copies of each seeded message/event are identical.
- state/lifecycle: L13 — C05KNDCHAAG/1770842137.835489 is cited only as a dated claim (hazard_acknowledgements L13 dated_claim) and the SQL modifies no L13 record; L08 none in scope — the seeded issues are unassigned; L09 — #1917 is merged without a review, like base GameOfDominoes merges (e.g. #1916's only review event has an empty actor, /timeline_events/4724).
- identifier/format: I02 — every seeded Slack id is sha256(channel|ts)[:32]; I03 — Arthur's base thread files use the blake@ alias and every seeded row uses arthur.blake@harmonygames.co; I08/I10 — base tokens EMPLOYEE_0025_GITHUB_USERNAME and usr_Robert are kept; I16 — the Trello ids encode their action time (698e6728 = 2026-02-12T23:50Z).

Known data issues (references/known_data_issues/normal.md, read for every touched record; no load-bearing fact, trap or graded slot rests on a card's 'Don't grade' value):
- NB-1: only full members (Leonard, Robert, Arthur) post in #prototype and #winddown after Feb 11 20:40Z (rev4's layer.ai reply is Leonard's); nothing grades channel access.
- NB-2: no AWS or hosting figure comes from the P&L sheet or the ledger: DD's $140 and CF's $95 / $62 are Arthur's own statements about his accounts.
- NB-5: Helpshift's Feb 28 comes from Leonard's line C0ADGSZKR3R/1770789534.434749, never from the vendor's acknowledgement date.
- NB-6: every seeded Slack row is before Feb 13 10:03Z (latest: the hub at 05:40Z); BoomBit's stop C09SWTHEMEW/1770977006.104929 (10:03Z) is cited only as context.
- NB-8: no Helpshift payment count is used.
- NB-9: Combo Fighter's Android status is never graded.
- NB-11: the CF GDD is not used for ads or status.
- NB-12: dbt ([USERNAME_30019]) and Kapwing ([PERSON_NAME_20852]) are graded only from records that spell them out (Arthur's mail, his Kapwing note, the checklist).
- NB-13: no branch name is graded (Jenkins 'Blake/boombitWithEcon' vs GitHub 'arthur.blake/boombitWithEcon').
- NB-15: pay is out of scope by the ground rules ('Pay for anyone who stays on is a separate conversation').
- NB-16: Arthur's DM names no database engine.
- NB-19: the Unity Ads balance comes from Leonard's line C09UHHN6PFZ/1770845002.610529, not AD_SPEND_DAILY.
- NB-21: no review version is joined to a build number.
- NB-24: every Linear comment the task relies on is seeded.
- NB-26: Combo Fighter's sales are not graded (its $7.36 January income only enters the AUTH over-application operator).
- NB-29: no time window starts at the shutdown decision.
- NB-31: reach in the DMs is argued from the two founders' membership, never graded.

## Intended disagreements

| Claim met first | Overturning record | Why realistic | Resolution |
|---|---|---|---|
| DD's production account ~$1k (C0ADGSZKR3R/1770680984.725779), 'easy to get to 300' (C0ADGSZKR3R/1770682219.100789), repeated in comment_c1664b356a8441e581cebdfecc39d09d, f_a7af6f358dd5648c11a608, f_d996e4c434ce160dc52596 | Arthur's DM reply D04V95AAAHW/1770952200.665739 (Feb 13 03:10Z): down to $140 a month, what it bills from March | the engineer trims the account and tells his co-founder in their DM | DD hosting $140; DD passes the take test |
| Metabase + dbt ~$300 (C0ADGSZKR3R/1770933903.645709; comment_53482e2398959d50dc774b5e4a921c3d) | Arthur's mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> (Feb 13 02:35Z): $248 on his Kub card, carried through May | he moved the billing the night before and says so by mail | Founder rows; Arthur's cash = a third less $248 |
| Arthur's 'done ... merged in #1917' (comment_7f8d7a9d959ca264f47b0e21d76416d1) and the merged PR harmonygames-Games/GameOfDominoes#1917 | the App Store notice robert@harmonygames.co/<136285951.151027292.1770967800000@email.apple.com> (Feb 13 07:30Z) on build #218 (C05433XK267/1770932970.616709) | a merge is not a release; review rejects the build | the support build still has to ship before Feb 28 |
| 'Calm Play could just be our LLC' (comment_ffcbb4c79467be3bdd75a1dd3b8da04f) | the ground rules f_1e468a9d69ea0f0a2001f5 ('The LLC is the new one ...'); C04UEQVDVB7/1701383740.580749, C04UEQVDVB7/1703492127.063049 (2023: fully owned subsidiary of Harmony Games) | a founder floats an old entity before the rules are written | Calm Play stays with HG and Sunset's sale (control row in rev4) |
| CF's own account about $95 a month (Arthur's ENG-2445 note comment_d7d8b2ded8a9c92fceed304abda87342, 00:58Z) | Arthur's email robert@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com> (04:20Z): the extra backend copy shut down, $62 a month now | the engineer trims a second account the same night and mentions it while reporting the Jenkins move | CF stacks $62 (rev4, T19) |
| 'cancelled it on the 11th' (Leonard's ENG-2454 note comment_3f50781a558dfa9fb3255d5f9c74d4d1) | C09UHHN6PFZ/1770837702.167889 (access until March 3rd) and Leonard's reply C09UHHN6PFZ/1770923700.470906 (CF's concept art is only in layer.ai; Robert to pull it out) | a cancelled tool still holds the only copy of some art | Robert exports the art by Mar 3 (rev4, T7) |
| 'I will keep both campaigns live' (C07C2866011/1770489896.754049) | Leonard's status C09UHHN6PFZ/1770938400.370665 (Feb 12): only the CF VO campaign is still on | the install campaign is paused a week later | one campaign, $3,000 a month cap, on the LLC from March |
| 'DD and ZM both come with CF. Servers about $1k a month' (f_a7af6f358dd5648c11a608, Feb 10) | the ground rules f_1e468a9d69ea0f0a2001f5 (Feb 12 23:40Z): the take test; cost at what it bills now | notes from Monday replaced by a rules doc two days later | ZM stays with HG; DD comes over |
| Leonard's draft rows (f_d996e4c434ce160dc52596, Feb 10): DD servers ~1000, Metabase + dbt ~300, Figma LLC | the later notes: D04V95AAAHW/1770952200.665739, robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com>, comment_3a8e425288db648883caa9b699488f6f | a Tuesday draft kept only for its layout | the layout is kept, the numbers are not |
| C05KNDCHAAG/1770842137.835489 (Feb 11: repos to the LLC) | C0ADGSZKR3R/1770933450.410449 (Feb 12: keep GitHub under HG until the data is sold, then transfer) | the plan firms up after the data deal | the GitHub transfer waits for the data sale |
| the January funding posts C07C2866011/1767730784.379929 and C07C2866011/1768417784.194359 | Leonard's split email robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com> (Feb 13) | an old equity discussion vs the LLC's running-cost rule | a third each, carried costs count toward it |

## Constraints for the prompt brief

| Anchor | May be named (noun phrases only) | Record |
|---|---|---|
| AN1 | Leonard's DM; Leonard's message from Thursday night | D04UP2L3E3S/1770961200.890407 |
| AN2 | the LLC project in Linear; the LLC take-over project | 0fa95761-d59b-4ff4-a8a3-15df3210ca6e |

Never name in the prompt: the ground rules' contents (the take test, the costing rule, the vehicle rule, the window, pay), the warehouse or REVENUE_DAILY, the split rule, the Trello card or its moving rule, Arthur's DM or mail, the App Store notice, the Jenkins build, PR #1917, the VO campaign, Calm Play, layer.ai or CF's art, the Jenkins email or CF's stacks figure, any item, figure, decision, date, owner, share or count. Deadlines: Robert's today is Sat Feb 14, 2026; the call is Mon Feb 16 (Leonard's 'we decide on Monday's call'). Deliverable kinds: one plan sheet in Robert's Drive laid out like Leonard's draft and shared with Leonard and Arthur; a call (comment) and a state on each project issue; a new issue for anything the project lacks; one reply in Leonard's DM thread with what Robert would do and what it costs each founder a month.

## Fact sheet

| Key | Value | Kind | Home / must appear in |
|---|---|---|---|
| Domino's prod account | $140 | amount | ad623a2f0d4387109d108e767b174609 |
| CF's own account bills | $62 | amount | arthur.blake@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com>, robert@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com>, leonard.hayes@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com> |
| backend and auth stacks run | $95 | amount | comment_d7d8b2ded8a9c92fceed304abda87342 |
| layer art | the CF character concept art is only in layer.ai | status | 103ed629eef6bb64a30ab49eb5c8fe40 |
| campaign card move | moves to our new company's card from March | status | 6908b2f17c379e809aafa6b2b169f4bf |
| so $248 a month | $248 | amount | arthur.blake@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com>, robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com>, leonard.hayes@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> |
| Arthur's carried billing | I'll carry those through May | status | arthur.blake@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com>, robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com>, leonard.hayes@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> |
| split rule | each of the three of us carries a third of what the LLC costs a month | status | leonard.hayes@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com>, robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com>, arthur.blake@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com> |
| take test | covers what its own hosting bills now, whatever we said about them before | status | f_1e468a9d69ea0f0a2001f5 |
| plan window | The plan runs March 1 to May 31 | status | f_1e468a9d69ea0f0a2001f5 |
| own deadline rule | Anything that already has its own deadline keeps it | status | 698e6548aa9516b76c4ab475 |
| store rejection | on a device without a mail account set up it does nothing | status | robert@harmonygames.co/<136285951.151027292.1770967800000@email.apple.com>, arthur.blake@harmonygames.co/<375944835.858142191.1770967800457@email.apple.com>, leonard.hayes@harmonygames.co/<883960163.410554888.1770967800220@email.apple.com> |
| support done claim | Helpshift is out of DD (merged in #1917) | status | comment_7f8d7a9d959ca264f47b0e21d76416d1 |
| campaign status | that's what it runs at from March | status | 6908b2f17c379e809aafa6b2b169f4bf |
| Calm Play note | Calm Play could just be our LLC | status | comment_ffcbb4c79467be3bdd75a1dd3b8da04f |
| ZM account | nobody trimmed it | status | comment_a317e10875adb686553e43989c1bab61 |
| Kapwing | Pro runs to Feb 25 | status | comment_8c69b5b90f9f6c03a0a168d25e6b75bd |
| Figma | it stays HG's and just lapses then | status | comment_3a8e425288db648883caa9b699488f6f |
| build machines | they go with the laptops in Sunset's sale | status | comment_7a0dea6299c7963e9a3e673996bd47fe |
| support change | Replace Helpshift with support email | status | harmonygames-Games/GameOfDominoes#1917 |

Clause facts use the `status` kind (exact match); amounts use `amount`. Output verbatim:

```
FACT CHECK: PASS — 111 text-bearing rows, 20 declared facts, 18 declared superseded records
Errors: none
```

Solver totals (`solver/truth.json`): 38 items; LLC 7, Founder 3, HG 28; LLC cash $3,202 a month (DD hosting 140 + CF stacks 62 + VO campaign 3,000); carried by Arthur $248 (Metabase 100 + dbt 100 + GitHub 48); monthly cost $3,450; a third $1,150.00; cash each month: Leonard $1,150.00, Robert $1,150.00, Arthur $902.00; over March–May the LLC's cash is $9,606.

## Facts for the human

| Locator | Base/seeded | Fact | Reach | Role |
|---|---|---|---|---|
| 6257a3c4456db0bd2aeb872619d7a364 | seeded | Leonard → Robert, 2026-02-13T05:40Z (D04UP2L3E3S/1770961200.890407): the ask (decide what the LLC takes if Sunset can't sell it, March–May cost, who pays; the ground rules; the sheet like his Tuesday draft in Robert's Drive shared with Blake and him; a call on each issue; the split by email; reply here; Monday's call) | DM member | authority (hub, anchor AN1) |
| f_1e468a9d69ea0f0a2001f5 | seeded | Leonard, 2026-02-12T23:46:00Z, 'LLC ground rules (Combo Fighter and whatever else we take)': vehicle rule (HG-owned things through Sunset's sale; services move their billing), window Mar 1–May 31, the take test (January income from the warehouse's daily revenue table covers what its own hosting bills now, whatever we said before; CF either way; a game brings its accounts and player support), costing rule (what it bills now, by whoever runs it), keep/cancel decisions in #winddown stay decided, pay out of scope; only monthly bills, no one-offs or yearly fees, moves on the LLC card | shared with Robert | authority H1 |
| f_a7af6f358dd5648c11a608 | seeded | Leonard, 2026-02-09T23:55:00Z, 'LLC notes (Monday)': Calm Play could hold it; DD and ZM come with CF; servers about $1k a month | shared with Robert | decoy (H1, older version) |
| f_d996e4c434ce160dc52596 | seeded | Leonard, 2026-02-10T18:30Z, 'LLC 90 days (draft)': header Item · Game · Decision · Monthly cost · Paid by · Next step · Owner · By; rows CF, DD servers (~1000, Blake: maybe 300), Metabase + dbt (~300), Figma | shared with Robert | layout source; stale numbers (T8) |
| f_7d2c9e7822e87b92a11759 | seeded | Robert, 2026-02-08T03:00:00Z, 'Combo Fighter: next 90 days': run the VO campaign at $100/day (~$3k a month) through May; no playables beyond the one in production until D1 is over 35% | Robert owns | evidence (campaign rate) |
| 698e6548aa9516b76c4ab475 | seeded | Leonard, 2026-02-12T23:42:00Z, 'LLC: what we take from HG' (founders' board, To Do): Robert makes the call; whoever runs an item moves it; through Sunset's sale → when the sale closes; own deadline keeps it; everything else by March 1 | unscoped | authority (dates and owners) |
| 0fa95761-d59b-4ff4-a8a3-15df3210ca6e | seeded | Leonard, 2026-02-12T23:24:00Z, Linear project 'LLC take-over' (team_ENG): one issue per thing the LLC might take from HG or pay for; comment the call; Done if a founder pays it himself through May (even if HG still owns it) or if the LLC takes it and nothing is left to do; Todo (assign the mover) if the LLC takes it and something is still to do; Canceled if it stays with HG (rev4 wording) | unscoped | first link (anchor AN2); DONE's state flip |
| ENG-2438 | seeded | ENG-2438…ENG-2474: 37 candidate issues in Backlog, created 2026-02-12T23:25–23:37Z, each with one owner note (2026-02-13T00:24–01:37Z) | unscoped | cohort |
| comment_c1664b356a8441e581cebdfecc39d09d | seeded | Leonard on ENG-2441: 'about $1k a month, Blake thinks he can get it to $300' | unscoped | claim met first (T1) |
| ad623a2f0d4387109d108e767b174609 | seeded | Arthur → Robert, 2026-02-13T03:10Z (D04V95AAAHW/1770952200.665739), reply under the Feb 2 root D04V95AAAHW/1770056235.480619: Domino's prod account is down to $140 a month, one small task and the db at its floor; that's what it bills from March | DM member | overturning (T1) |
| comment_d7d8b2ded8a9c92fceed304abda87342 | seeded | Arthur on ENG-2445 (00:58Z): CF's own account (its auth and backend stacks) runs about $95 a month on HG's AWS bill; CF no longer calls ZM's phoenix api | unscoped | claim met first (T19) |
| robert@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com> | seeded | Arthur → Robert, cc Leonard, 2026-02-13T04:20Z, 'jenkins' (thread robert@harmonygames.co/1856982378087295205): the Jenkins jobs moved to his own machine, the build boxes are HG's; second paragraph: the extra copy of CF's backend shut down, CF's own account bills $62 a month now, still on HG's AWS bill till March | Robert's INBOX | overturning (T19) |
| comment_a317e10875adb686553e43989c1bab61 | seeded | Arthur on ENG-2443: ZM's account still runs phoenix, its nakama and the aurora cluster, nobody trimmed it; it bills every month on HG's AWS bill | unscoped | evidence (ZM hosting) |
| snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY | base | January 2026 SUM(total_revenue_usd): domino_delights 183.11 (IAP 68.84 + ads 114.27), combo_fighter 7.36, zombie_match_3d 0.00 (186 rows); REVENUE_DAILY_V2 agrees | unscoped | authority H2 |
| confluence:page_aws_infra | base | AWS guide (Dec 31, 2025): DD dev/prod accounts, ZM one account, analytics account; Fargate (Phoenix + Nakama) ~$650/mo | unscoped | evidence (ZM hosting) |
| comment_53482e2398959d50dc774b5e4a921c3d | seeded | Leonard on ENG-2447: about $300 a month with dbt, more or less | unscoped | claim met first (T4) |
| C0ADGSZKR3R/1770937232.664809 | base | Arthur, Feb 12 23:00Z: moving github, dbt and Metabase to his KubLLC card | #winddown member | connecting (T4) |
| robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> | seeded | Arthur → Robert, Leonard, 2026-02-13T02:35Z, 'billing moved to my card' (thread robert@harmonygames.co/1856975772058401508): Metabase $100 base, dbt $100, GitHub $48 team plan now that copilot is off, $248 a month, carried through May as his part | Robert's INBOX | overturning (T4) |
| robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com> | seeded | Leonard → Robert, cc Arthur, 2026-02-13T06:10Z, 'LLC money' (thread robert@harmonygames.co/1856989298688559716): each of the three carries a third of the LLC's monthly cost March–May; what one already pays counts toward his third; put the three shares on the sheet per month | Robert's INBOX | authority H3 |
| 6908b2f17c379e809aafa6b2b169f4bf | seeded | Leonard, 2026-02-12T23:20Z (C09UHHN6PFZ/1770938400.370665), reply under C09UHHN6PFZ/1770404397.819789: only the CF VO campaign is still on (install one paused), $100/day capped at $3,000 a month, on his card till the end of Feb, moving to 'our new company's card from March' (rev4: no 'LLC', no 'barely billing') | #prototype member | overturning (T16) · campaign (T3) |
| C09UHHN6PFZ/1770404445.795829 | base | Leonard, Feb 6: VO campaign budget $100/day | #prototype member | evidence (T3) |
| comment_7f8d7a9d959ca264f47b0e21d76416d1 | seeded | Arthur on ENG-2462: done, support goes to the email address and Helpshift is out of DD (merged in #1917) | unscoped | claim (T5) |
| harmonygames-Games/GameOfDominoes#1917 | seeded | Arthur's PR 'Replace Helpshift with support email', opened 2026-02-12T18:05Z, merged 21:10Z into arthur.blake/boombitWithEcon | unscoped | claim support (T5) |
| 85bc96b0aa43bb455a58da9d8b63c060 | seeded | Jenkins, 2026-02-12T21:49:30Z (C05433XK267/1770932970.616709): DD iOS Submission #218 on Blake/boombitWithEcon succeeded; change 'Replace Helpshift with support email' (start post C05433XK267/1770932400.314774 at 21:40Z) | #builds member | connecting (T5) |
| robert@harmonygames.co/<136285951.151027292.1770967800000@email.apple.com> | seeded | App Store Review → Robert, 2026-02-13T07:30Z, 'We noticed an issue with your submission.' (thread robert@harmonygames.co/1856994331853686118): Domino Delights, Guideline 1.5 — the support option only opens an email draft and does nothing on a device without a mail account; asks for a support URL or another in-app contact | Robert's INBOX | overturning (T5) |
| C0ADGSZKR3R/1770789534.434749 | base | Leonard, Feb 11: Helpshift cancels without a hassle; DD and ZM must be off it before Feb 28th | #winddown member | evidence (the support deadline) |
| comment_ffcbb4c79467be3bdd75a1dd3b8da04f | seeded | Leonard on ENG-2472: 'Calm Play could just be our LLC, it already has the Singular org and its own Apple team' | unscoped | stale claim (control row; EXC purged in rev4) |
| C04UEQVDVB7/1701383740.580749 | base | Nov 30, 2023: Calm Play is an LLC fully owned by Harmony Games (also C04UEQVDVB7/1703492127.063049, Dec 25, 2023) | #admin_foundersonly member | agrees with the ground rules (control) |
| comment_3f50781a558dfa9fb3255d5f9c74d4d1 | seeded | Leonard on ENG-2454 (00:37Z): 'cancelled it on the 11th' (rev4: no art caveat) | unscoped | claim met first (T7) |
| C09UHHN6PFZ/1770837702.167889 | base | Leonard, Feb 11: layer.ai cancelled, access until March 3rd (tags EMPLOYEE_0033); rev4 updates its thread fields | #prototype member | evidence (T7) |
| 103ed629eef6bb64a30ab49eb5c8fe40 | seeded | Leonard, 2026-02-12T19:15Z (C09UHHN6PFZ/1770923700.470906), reply under it: '<@EMPLOYEE_0016_SLACK_ID> the CF character concept art is only in layer.ai, can you pull it out yourself before then? the art goes with CF, there's nothing on the layer account for our new company to take, it just lapses' | #prototype member | overturning (T7) |
| C0ADGSZKR3R/1770933450.410449 | base | Leonard, Feb 12 21:57Z: the subscription checklist (github: keep until the data is sold, then transfer; Slack down to 3; Google archive Feb 15; Kapwing, cursor, coderabbit Blake's) | #winddown member | evidence (T7, T17, controls) |
| C0ADGSZKR3R/1770933601.686309 | base | Leonard, Feb 12 22:00Z: keep Deel, Gusto, Intuit; Figma can't charge before renewal; Linear kept during transition | #winddown member | evidence (controls) |
| evt_f5f279f282d20ec86bb8e5 | seeded | Mon 2026-02-16 18:00–18:45Z 'LLC: decide' (Leonard organizer; Robert and Arthur invited; created 2026-02-13T05:45Z), Robert's copy | Robert's calendar (self) | destination (K11) |
| robert@harmonygames.co/<calendar-0b12e6f6-3c7e-3b05-f505-2adb8396bfb5@google.com> | seeded | INT-11 invitation for the Monday call | Robert's INBOX | companion |

## Platform /injection review of rev1 and the rev2 changes

rev1 (SQL sha256 7573eb1a6bca, attempt 6adfee3b47f7621feba5b96c) passed `injection-static-v2` with Checks A, B and C PASS and no demonstrated defect (`run_forensics/rev1/0_injection_PASS_r1.md`). Its advisories and what rev2 does with each:
- A-1 (cosmetic): zero-length style run on the notes doc f_a7af6f358dd5648c11a608. Fixed in rev2: the doc is titled 'LLC notes (Monday)' and the note is its body (the one-line note had become a 155-character title).
- A-2: branch arthur.blake/boombitWithEcon keeps its head after the #1917 merge; base-consistent (R05, base heads are not advanced). Kept.
- A-3 (realism): Arthur's $140 reply D04V95AAAHW/1770952200.665739 sits under an unrelated Feb 2 root. Kept: it is the CORR trap's designed placement (thread-reply hiding).
- A-4/A-5/A-6 (for /prompt): the App Store rejection robert@harmonygames.co/<136285951.151027292.1770967800000@email.apple.com> as the only reading of the support item; Calm Play's 'could' note against the ground rules f_1e468a9d69ea0f0a2001f5; ZM's 'well over $1k a month' (rev2: 'it bills every month', no figure) against $0.00 January income. Each is settled by a later dated record and was re-tested by the second blind fork sweep (plan/sweep_dispositions.md).
- A-7 (NB-13): no exact branch name is graded.

rev2 (SQL sha256 edf1fd903611, the same attempt) passed `injection-static-v2` again with Checks A, B and C PASS and no demonstrated defect (`run_forensics/rev2/0_injection_PASS_r2.md`): A-1 resolved, A-2/A-3/A-5/A-7 reused, A-4 clearer (the rejection names the email-only support that #1917 shipped). Updated A-6: no injected record states ZM's hosting figure. The take-test call does not depend on it: ENG-2443 says the account bills every month, and ZM's January income in snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY is 0.00, so no bill is covered (for the prompt brief). The platform changelog export (`task_inputs/02_Changelog.json`) shows all 131 rev2 statements applied (129 INSERT, 2 UPDATE) with the rev2 wording.

## Platform /prompt review of rev2 and the rev3 changes

rev2 passed `injection-static-v2` a third time (`run_forensics/rev2/0_injection_PASS_r2_resubmit.md`), but the paired `/prompt` review (`run_forensics/rev2/1_prompt_FAIL_r2.md`, prompt sha256 ccd229a59a17) scored Unique Ground Truth and Clarity 2 and every other dimension 5. Dataset similarity passed (nearest 0.776, same scenario). Its decision sweep settled 35 of the 37 issues by record and matched solver/truth.json on every call, cost and share; three Linear writes had no settling record. rev3 settles each one with a dated record and leaves the prompt unchanged:
- F1 (a new issue for the VO campaign): the project description said 'One issue per thing the LLC might take from HG', and the campaign is on Leonard's card, not HG's. rev3: the project 0fa95761-d59b-4ff4-a8a3-15df3210ca6e reads 'One issue per thing the LLC might take from HG or pay for'. The LLC pays the campaign from March (C09UHHN6PFZ/1770938400.370665), so the plan row needs an issue and the prompt's 'the project should match the sheet' asks for it.
- F2 (ENG-2451 AppsFlyer assignee): the card's 'Whoever runs an item today moves it' named nobody for a new service. rev3: Leonard's note ends 'I'll set CF up on it', so the issue is assigned to Leonard.
- F3 (ENG-2452 Google Analytics state): Arthur's mail said CF's BigQuery/Firebase 'are on the free tier' once the data is out, which read as a later move to the LLC. rev3: Leonard's note reads 'stays under HG until the data is extracted, nothing for the LLC to take or pay', and Arthur's mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> says they 'cost nothing after that, so there's nothing there for the LLC'. The issue is Canceled.
- Optional realism note (Eval 0 A-3, not scored): Arthur's $140 reply stays threaded under the Feb 2 root, the CORR trap's designed placement.
A third blind fork sweep on the rev3 records (fresh agent, no answer key) reproduced the plan, the totals and every Linear write, and F1–F3 came back settled. Two readings it left open are settled in rev3 too: Arthur's ENG-2446 note adds 'so the LLC doesn't need them' (the build boxes, even if Sunset can't sell them), and Leonard's Helpshift note adds 'CF was never on it, its support is the contact on its store listing and that moves with the game' (no separate CF player-support line). The rest were already settled by records (plan/sweep_dispositions.md).

## Platform /hardness review of rev3 and the rev4 changes

rev3 passed `/injection` and `/prompt` (every dimension 5), but `/hardness` scored 2 (FAIL, too easy; `run_forensics/rev3/precheck/1a_hardness_FAIL_r3.md`). One platform Opus 5.5 run (168 counted calls) got about 96 % right. `/create-hardening` MODE B (`Working_Files/01a_Hardening_Report.md`) found these causes:
- DONE landed but changed only wording: the store notice was fetched as a snippet.
- DATE landed but was minor: the layer.ai date was never seen.
- CORR, AUTH, FILT and COMPLETE leaked:
  - the campaign record carried the project word the run searched first;
  - the ground rules pointed the run to the owner and to the table;
  - a base lead led to Arthur's mail.
- EXC was never live.
`/create-scenario --revise` (design-2, gate PASS) chose four Hardness v2 moves and one purge. This revision implements them and leaves the truth and the prompt unchanged:
- RB1 (FILT): Leonard's status C09UHHN6PFZ/1770938400.370665 drops 'LLC' and 'barely billing': the campaign 'moves to our new company's card from March', 'so count it as its own line in what we pay each month'.
- RB2 (DONE): the project description 0fa95761-d59b-4ff4-a8a3-15df3210ca6e tests Done first, 'if one of us pays it himself through May (even if HG still owns it) or if the LLC takes it and nothing is left to do on it'. A missed store notice now flips ENG-2462 to Done instead of Todo with Arthur.
- RB4 (DATE): ENG-2454's note is only 'cancelled it on the 11th'. The art and its owner move into Leonard's reply C09UHHN6PFZ/1770923700.470906 under the base access-date post, with the parent's thread fields updated.
- RB5 (STACKS, new): ENG-2445's note gives Arthur's ~$95 before his trim. His later email robert@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com> ('jenkins', 04:20Z) says in its second paragraph that CF's account bills $62 now.
- EXC purged: Calm Play is a control row decided by the ground rules. Dropping their vehicle sentence would have reopened a /prompt fork.

Independent reviews before sealing:
- An hg.py-only fallback red team of the design delta (`Working_Files/01b_Redteam_Fallback_rev4.md`) found four majors, all fixed before this SQL: the campaign's payer and state, GitHub Done vs Canceled, and 'barely billing' vs 'bills now'.
- A blind fork sweep of the rev4 records is in 'Blind sweeps' below.

## Platform follow-ups

- ○ carriers: the Monday event's description ('Robert's plan sheet. We agree what we take and the shares.') is supporting only; nothing graded rests on it. Linear comments are ● (§6b), so no follow-up is needed for the 37 notes.
- Snowflake and Confluence figures (REVENUE_DAILY January sums; the AWS guide's cost note) are re-verified after any data regeneration (`plan/run_checks.sh`, solver JAN_INCOME / ZM_HOSTING).
- No call_budget row depends on an unverified behaviour.

## Self-review

### Tool outputs (final SQL, verbatim)

`sql_lint.py`:
```
schemas touched (10): gcal, gdocs, gdrive, github, gmail, gsheets, gslides, linear, slack, trello
rows by schema: {'gdrive': 4, 'gdocs': 2, 'gsheets': 2, 'gslides': 7, 'slack': 9, 'trello': 2, 'gmail': 28, 'gcal': 3, 'github': 7, 'linear': 75}  total rows: 139  ops: {'insert': 136, 'update': 3}
errors: 0  warnings: 6
  warn  line 118: gcal.gcal_events.start_ts = 2026-02-16T18:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 118: gcal.gcal_events.end_ts = 2026-02-16T18:45:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 121: gcal.gcal_events.start_ts = 2026-02-16T18:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 121: gcal.gcal_events.end_ts = 2026-02-16T18:45:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 123: gcal.gcal_events.start_ts = 2026-02-16T18:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 123: gcal.gcal_events.end_ts = 2026-02-16T18:45:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
```
sql_lint warning disposition (clock class, 6 warnings): the three copies of the Monday call start and end on Feb 16, after the clock — a not-yet-happened event (a deadline-type plan field, GEN_EXECUTION §0a), allowed.

`hg.py lint` (the eval's hg_injection_lint, with base data):
```
hg_injection_lint (base data): counts {'FAIL': 0, 'CHECK': 0, 'INFO': 0, 'by_check': {}}; flags: 0; info: 0
```
LINT: counts FAIL 0, CHECK 0, INFO 0 — no CHECK to disposition (the earlier grader_language CHECK on the project description's 'Todo when' wording was fixed by rewording, see design_delta).

`base_check.py`:
```
BASE CHECK (/injection A + C, static): PASS  — 136 inserts, 3 updates
KB: bound (2026-02-14) — KB bound to the selected universe
Check A — records, references, IDs: PASS
Check C — dates and relationships: PASS
  note: github.github_branches: no base-reference rules (checked by sql_lint only)
  note: github.github_commits: no base-reference rules (checked by sql_lint only)
  note: github.github_pull_request_commits: no base-reference rules (checked by sql_lint only)
  note: gsheets.sheets_sheets: no base-reference rules (checked by sql_lint only)
  note: gslides.slides_page_elements: no base-reference rules (checked by sql_lint only)
  note: gslides.slides_pages: no base-reference rules (checked by sql_lint only)
  note: linear.linear_projects: no base-reference rules (checked by sql_lint only)
```
`base_claims.py`:
```
BASE CLAIMS (injected text vs base git + #builds): PASS · 0 branch mentions · 0 fail · 0 warn · 0 date-only
branch windows:
```
`hardness_gate.py` (final manifest + SQL):
```
HARDNESS GATE (extreme): PASS
  [ok] assignment_context: manifest bound to current V3 assignment, freeze and policy
  [ok] effective_profile: effective_profile 'extreme' for 'Long Horizon' → thresholds 'extreme'
  [ok] sql_lint_clean: 0 lint error(s) — run tools/sql_lint.py
  [ok] base_consistency: /injection-style checks vs the base universe: A 0 finding(s), C 0 finding(s), 0 warning(s) — run tools/base_check.py --manifest
  [ok] persona_reach: 32 load-bearing seeded ids for robert (14 in unscoped services = visible, 18 judged by persona_view check-sql); not provably visible: none
  [ok] fact_consistency: fact_check: 0 error(s) (20 declared facts), 0 drift warning(s); first: none — run tools/fact_check.py --manifest --no-leak
  [ok] hazard_scope: 1 pre-existing hazard(s) among task-touched records; state/lifecycle or referential without a verified resolution: none; resolved/other: ['L13']
  [ok] services_injected: 10 schemas injected (gcal, gdocs, gdrive, github, gmail, gsheets, gslides, linear, slack, trello); need ≥ 10
  [ok] rows: 136 INSERTed rows (UPDATE companions not counted; 139 rows in all); need ≥ 120
  [ok] services_carrying_weight: 12 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: schemas injected but absent from the design: none
  [ok] seeded_ids_exist_in_sql: 51 seeded ids cited; missing from SQL: none
  [ok] anchors: 2 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 13 fragments; need ≥ 12
  [ok] ask_fragment_services: 7 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 13 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 11 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 40; need ≥ 40 (source-defined: True)
  [ok] evidence_surfaces: 3 surfaces over 3 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 69; need ≥ 60
  [ok] call_budget: unconditional (verified) floor 190 of 190 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 150 (requester-confirmed volume_exception)
  [ok] call_budget_spread: 11 services in budget; largest share outside the per-record phase 28% (≤ 50%)
  [ok] traps: 18 traps across 7 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 7 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 5 supersessions (4 with versions in ≥ 2 services, 3 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: 7 trap(s) with version_records; the records' own timestamps (SQL created_at/ts/date/updated_at, or the base record) must be strictly increasing in the listed order (oldest first); bad: none
  [ok] distractors: 6 distractors of 6 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 9 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 7 chains with 6 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] mechanism_portfolio: 7 portfolio entries, each a mechanism-enum id with trap/chain nodes, a requirement, a natural-reading fallback and a prior family with its reason
  [ok] artifact_fields: declared ['gradable_surface', 'solver']: paths relative, digests sha256
  [ok] hidden_authorities: 3 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 1 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 11 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 11 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 5 writes over 4 services; each must depend on findings
  [note] volume_exception: call-budget floor 150 and per-record floor 60 replace 500 and 300; every other extreme target applies — reason: 38 graded items (37 candidate issues and one outside charge); the per-issue read; requester confirmation: requester, Claude Code chat 2026-11-05: 'i want over 130 tool calls in each runs
```

### Preflight (S4b–S5e)

`oracle_kit.py check`:
```
SOLVER CONTRACT: PASS · solver.py sha f8392ca56fc2 · sql f1a290ced176 · 7 rules
  [PASS] contract.interface: 7 rules, each with mechanism, requirement and natural_reading; optional: ['touched', 'deciding', 'DEGRADES']
  [PASS] contract.deterministic: two fresh solves (forward and reverse key order) give identical output (38 keys, sha 7e33afdcc74f), and so do fresh processes with PYTHONHASHSEED 1 and 2
  [PASS] contract.regression: previous truth truth.json: solver at revision ? reproduces it byte for byte; current rules (None) on the previous SQL: 0 field difference(s)
  [PASS] contract.rules_nodes: 7 rules vs 7 portfolio entries: one-to-one
  [PASS] contract.slots: 9 direct/aggregate slots read a solver value; 16 write-content/delivery slots are graded from the writes, not the solver
  [PASS] contract.controls: CORR: 1 control(s); corr_over moves ['Combo Fighter backend and auth stacks (AWS)']; AUTH: 1 control(s); auth_over moves ['Combo Fighter']; FILT: 2 control(s); filt_over moves ['Playable vendor', 'Unity Ads balance']; COMPLETE: 1 control(s); complete_over moves ['Build machines']; DONE: 1 control(s); done_over moves ['Helpshift']; DATE: 1 control(s); date_over moves ['AppsFlyer']; STACKS: 1 control(s); stacks_over moves ['Domino Delights production account (AWS)']; channel CH-CORR (scale): ch_miss moves 3 of 3 member(s); channel CH-AUTH (scale): ch_miss moves 3 of 3 member(s); channel CH-FILT (scale): ch_miss moves 1 of 1 member(s); channel CH-COMPLETE (scale): ch_miss moves 3 of 3 member(s); channel CH-DONE (scale): ch_miss moves 1 of 1 member(s); channel CH-DATE (scale): ch_miss moves 2 of 2 member(s); channel CH-STACKS (scale): ch_miss moves 1 of 1 member(s)
  [PASS] contract.golden: 9 golden values checked against their deciding records (8 sampled keys x 7 fields): 7 identifier values found, 2 short tokens found, 0 presence-type; 47 unverified e.g. ['Combo Fighter/Game: no evidence ids', 'Combo Fighter/Monthly cost: no evidence ids']
  [PASS] contract.digest: manifest solver Working_Files/solver/solver.py digest f8392ca56fc2 vs file f8392ca56fc2
```
`difficulty_mutation.py mutate` (tail) and `geometry`:
```
MUTATION · rev4 · sql f1a290ced176 · deterministic design diagnostics from the solver; on the Season Pass backtests these are development fixtures, not validation
  key-locality: PASS on 39 of 39 configurations checked
  rule:CORR                          KILLED     flipped   8 flips direct slot(s) of weight >= 3: ['G2']
  rule:AUTH                          KILLED     flipped  11 flips direct slot(s) of weight >= 3: ['G2', 'G3']
  rule:FILT                          WEAK       flipped   3 flips only aggregate or weight-1 slots: ['V1']
  rule:COMPLETE                      KILLED     flipped   8 flips direct slot(s) of weight >= 3: ['I1']
  rule:DONE                          SURVIVED   flipped   0 changes outputs that no slot reads
  rule:DATE                          SURVIVED   flipped   0 changes outputs that no slot reads
  rule:STACKS                        SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:corr_over                  SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:auth_over                  WEAK       flipped   4 flips only aggregate or weight-1 slots: ['G1', 'V1']
  degrade:filt_over                  WEAK       flipped   3 flips only aggregate or weight-1 slots: ['V1']
  degrade:complete_over              WEAK       flipped   0 changes what an aggregate reads (class or group membership) and the ag
  degrade:done_over                  SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:stacks_over                SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:date_over                  SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:ch_miss                    KILLED     flipped  13 flips direct slot(s) of weight >= 3: ['G2', 'G3', 'I1']
  shards (consecutive slices of 14 records, 3 batches): 10 mutants {'KILLED': 3, 'WEAK': 3, 'SURVIVED': 4}
  intervention:rule:CORR             load-bearing    
  intervention:rule:AUTH             load-bearing    
  intervention:rule:FILT             load-bearing    
  intervention:rule:COMPLETE         load-bearing    
  intervention:rule:DONE             load-bearing    
  intervention:rule:DATE             load-bearing    
  intervention:rule:STACKS           load-bearing    
  intervention:degrade:corr_over     no-injected-records
  intervention:degrade:auth_over     no-injected-records
  intervention:degrade:filt_over     no-injected-records
  intervention:degrade:complete_over no-injected-records
  intervention:degrade:done_over     no-injected-records
  intervention:degrade:stacks_over   no-injected-records
  intervention:degrade:date_over     no-injected-records
  intervention:degrade:ch_miss       no-injected-records
  geometry: U = 0.8701 (67/77) · L_max = 0.2078 over ['rule:AUTH', 'rule:COMPLETE']
    V3 cap 0.90: U PASS (needs > 0.10) · L_max OK
  dispositions: 0/30 recorded; missing ['rule:CORR', 'rule:AUTH', 'rule:FILT', 'rule:COMPLETE', 'rule:DONE', 'rule:DATE', 'rule:STACKS', 'degrade:corr_over'] ...
```
```
MUTATION · rev4 · sql f1a290ced176 · deterministic design diagnostics from the solver; on the Season Pass backtests these are development fixtures, not validation
  key-locality: PASS on 39 of 39 configurations checked
  geometry: U = 0.8701 (67/77) · L_max = 0.2078 over ['rule:AUTH', 'rule:COMPLETE']
    V3 cap 0.90: U PASS (needs > 0.10) · L_max OK
```
`trap_liveness.py` (SQL):
```
TRAP LIVENESS · ADVISORY · UNCALIBRATED · lexical warnings, not proof · on the Season Pass backtests these are development fixtures, not validation
  hub D04UP2L3E3S/1770961200.890407 · direct delegations 6 · rule placement: SKIP for every node: the mechanism_portfolio declares no A15 node
  T1   superseding        breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T2   exact_predicate    breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T3   exact_predicate    breadcrumb, order  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T4   completion_elsewhe breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T5   done_gap           -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T7   exact_predicate    -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T8   stale_summary      order, self-advertising  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T9   distractor         breadcrumb, order  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T10  superseding        -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T16  superseding        breadcrumb, order  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T17  superseding        -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T18  distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T11  distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T12  distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T13  distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T14  near_miss_mention  -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T15  distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T19  superseding        -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  dispositions: 0/11 recorded
```
`hardness_forecast.py forecast --preregister` (tail) and `preflight_report.py`:
```
  channel CH-DATE (scale, member latent [declared (unit-free point)], 2 member(s)): e = 0.55 [OVERRIDE (disclosed, no ledger record): --channel-rate CH-DA] · P(any of 2 fails) 0.797 integrated vs 0.797 plug-in · expected loss alone 0.0000 · UNCALIBRATED · OVERRIDE
  channel CH-STACKS (scale, member latent [declared], 1 member(s), member trials): e ~ Beta(1.0, 5.0) [ledger records, member trials (runs of a task share a design] · P(any of 1 fails) 0.167 integrated vs 0.167 plug-in · expected loss alone 0.0000 · UNCALIBRATED
  channel control:CORR (control, member latent [rate unit], 1 member(s), member trials): e ~ Beta(1.0, 7.0) [ledger records, member trials (runs of a task share a design] · P(any of 1 fails) 0.125 integrated vs 0.125 plug-in · expected loss alone 0.0000 · UNCALIBRATED
  channel control:COMPLETE (control, member latent [rate unit], 1 member(s), member trials): e ~ Beta(1.0, 3.0) [ledger records, member trials (runs of a task share a design] · P(any of 1 fails) 0.250 integrated vs 0.250 plug-in · expected loss alone 0.0000 · UNCALIBRATED
  channel control:DONE (control, member latent [rate unit], 1 member(s), member trials): e ~ Beta(1.0, 3.0) [ledger records, member trials (runs of a task share a design] · P(any of 1 fails) 0.250 integrated vs 0.250 plug-in · expected loss alone 0.0000 · UNCALIBRATED
  channel control:STACKS (control, member latent [rate unit], 1 member(s), member trials): e ~ Beta(1.0, 7.0) [ledger records, member trials (runs of a task share a design] · P(any of 1 fails) 0.125 integrated vs 0.125 plug-in · expected loss alone 0.0000 · UNCALIBRATED
  channel control:AUTH (control): UNPARAMETERIZED - no ledger record and no --channel-rate override: not simulated
  channel control:FILT (control): UNPARAMETERIZED - no ledger record and no --channel-rate override: not simulated
  channel control:DATE (control): UNPARAMETERIZED - no ledger record and no --channel-rate override: not simulated
  slots most at risk (independent whole; P(fail) / P(fails all six) - all-fail justification workload, never a block): V1 0.75/0.21, G2 0.69/0.20, G3 0.56/0.10, I1 0.40/0.04, G1 0.00/0.00, I2 0.00/0.00, I3 0.00/0.00, I4 0.00/0.00
  ledger: forecast record {'id': 'hev_82f1150ec1778af9', 'added': True, 'present': False, 'rejected': (none)}
wrote Task_Authoring/task_inputs/Working_Files/01c_Forecast.json
```
```
PREFLIGHT: PASS · blocking {'solver_contract': True, 'surface_validation': True, 'mutation_dispositions': True, 'geometry_upper_bound': True} · advisory {'geometry_margin': {'V3': 'OK'}, 'geometry_bound_verdict': {'V3': 'PASS'}, 'liveness_dispositions_missing': (none), 'forecast': 'recorded'}
wrote Task_Authoring/task_inputs/Working_Files/01c_Preflight_Report.json and Task_Authoring/task_inputs/Working_Files/01c_Preflight_Report.md
```
Forecast (UNCALIBRATED, advisory), two views.
- Solver-based, exact: pre-registered for rev4 as hev_82f1150ec1778af9. Earlier records: rev3 hev_61e8a1a72c32da82, rev3 posterior after the pre-check hev_51611d00e3779d1d, rev2 hev_7365758e94d10201, rev1 hev_c47baade19a93a88. Its tail is above. It never fails write-content slots (51 of the 77 weight points: the plan and reply text and the new issue), so only the direct slots move.
- Design view (plan/policy_scores.txt; design forecast hev_c2e614ebc388cb63): E[avg] is 64.4 % at the rev4 design rates (rho 0.30) and 84.4 % at 0.4x those rates. P(one run catches every trap) is about 0.035, and no pair of misses stays at or above 85 %.
- Channel rates come from Opus 5.5 ledger records of each family, except CH-DATE: its family has one verdict record (hev_3d96146a0a8b19a5, the rev3 pre-check), so it carries a disclosed design rate of 0.55 (plan/policy_scores.py). CH-EXC is gone.

Every mutation result, channel degrade, intervention and liveness flag has a written disposition in `Working_Files/01c_Dispositions.json`. preflight {report, digest} is not written back into the final manifest: the report binds the manifest by sha256, so writing its digest there would make the report stale (the archived bridge and Q4 tasks did the same).

### Changes made at this stage (and why)

- K11 locator: evt_c82c0965b68d959ee4241b (Leonard's copy) -> evt_f5f279f282d20ec86bb8e5 (Robert's own calendar copy); Leonard's and Arthur's copies share ical_uid — reach is proven on the persona's own copy
- record ids (all elements): Slack 'channel/ts' pointers to seeded messages -> their 32-hex row ids; Gmail thread pointers in Robert's mailbox -> the message row that carries the text (thread ids kept alongside in seeded_ids) — the gate reads text and timestamps from SQL rows: a Slack message row is keyed by its id, a Gmail thread row holds only a snippet
- linear project links: no linear_project_teams / linear_project_members rows (planned: team link and three members) — not among the 64 writable tables (Injection Schema Guideline 2026-10-22, sql_lint); the project keeps team_id and lead_id
- #1917 branches: merged into Blake/boombitWithEcon (head Blake/supportEmail; the branches table row is arthur.blake/supportEmail, the base's NB-13 form split), not develop; Jenkins #218 builds 'Blake/boombitWithEcon'; a merge commit row follows the base merge shape (commits/4580) — base DD submissions build from that branch (#builds 2026-01 /1236-/1238; GitHub branches/981); #1916 also targeted a feature branch, not develop
- store notice wording: subject 'We noticed an issue with your submission.' and Apple's review template (App Name, Submission ID, the guideline item) — the base INT-08 rejection family in Robert's mailbox (threads/00013785.json, 00014520.json)
- deck line 2: 'Keep the video campaign ...' -> 'Run the VO campaign at $100/day (~$3k a month) through May', dated Feb 8 03:00Z; playables line -> 'No playables beyond the one in production until D1 is over 35%' — the deck first predated the campaign (C09UHHN6PFZ/1770404397.819789, Feb 6); 'VO' is event/value optimization, not video (C09UHHN6PFZ/1770404397.819789, C07C2866011/1770438169.228649); Robert pushed one playable that week (C07C2866011/1770264360.331789)
- project description: 'Todo when ...' -> 'move it to Todo if ...' (same states and rule) — eval lint grader_language (state_rules) on the 'Todo when' phrasing
- blind fork sweep (rev1): settled by dated records: campaign capped at $3,000 a month and moving to the LLC from March; the split mail counts what a founder already pays inside 'what the LLC costs'; GitHub's org stays HG's while Arthur pays the bill; the build boxes go with Sunset's sale and CF's Jenkins job moves to Arthur's machine; AppsFlyer free tier from March; CF on Unity Personal; DD owner Leonard and no BoomBit status claim; ground rules: hosting 'bills now', a game brings its accounts and player support, monthly bills only, the LLC is for the three of us; CF stacks and DD prod are on HG's AWS bill till March — a blind fork sweep of Robert-visible records found readings no record settled (plan/sweep_dispositions.md); the truth is unchanged
- blind coherence sweep (rev1): VO (event-optimization) campaign, not 'video'; Leonard's status names only the Meta campaigns, says Meta barely bills the VO one while it learns and that it runs at $100/day capped at $3,000 a month from March; deck dated Feb 8 with the playables line reworded; project (23:24Z) and issues before the card (23:42Z) before the ground rules (23:46Z); notes doc Feb 9 23:55Z; GitHub back to the $48 plan after dropping the extra seat (Feb 3 receipt $52 + Copilot $38), bills move 'from the next bill'; CF's own account (auth, nakama, backend) no longer calls ZM's phoenix; ZM's account 'well over $1k a month'; Slack note 'three paid members'; the Metabase note drops 'needs a payer'; the hub drops its opening 'ok,'; App Review mail copied to all three founders; Arthur's invitation in EST with his display name; PR refs Blake/… with a merge commit row — a blind coherence sweep of every seeded claim against the full base (plan/sweep_dispositions.md); each finding re-checked through hg.py
- rev2: notes doc title (platform /injection rev1 advisory A-1): the notes doc is 'LLC notes (Monday)' with its text as the body (it was one line, so the whole note became the title and the body run was empty) — the platform /injection review of rev1 (PASS, run_forensics/rev1/0_injection_PASS_r1.md) flagged the zero-length style run; the 155-character title was unnatural
- rev2: coherence re-check: ZM's account note drops 'well over $1k a month' (it bills every month); Arthur's and Leonard's App Review copies greet them by name with their base labels; the Metabase note reads 'more or less'; layer.ai 'character source art'; 'the build boxes at my place are HG's'; project start_date 2026-02-12 — the coherence reviewer's re-check of the rev2 wording (HG's whole AWS line is $1,485 in Jan and Feb 2026, snowflake FINANCE.EXPENSES.MONTHLY_BURN; plan/sweep_dispositions.md)
- rev2: second blind fork sweep: the App Review item describes the email-draft support option doing nothing without a mail account (only the #218 support-email build has it); Arthur moves 'our jenkins jobs' (CF and DD); ENG-2445 names the auth and backend stacks only; Arthur's mail counts GitHub as his 'like the other two' and puts CF's BigQuery/Firebase on the free tier once the data's out; Leonard's status adds 'so count it in what the LLC costs' — a second blind fork sweep of the rev2 records (fresh agent, no answer key) reproduced the plan and totals and listed the readings still open; truth unchanged (plan/sweep_dispositions.md)
- rev3: platform /prompt forks F1-F3: the project description's scope reads 'One issue per thing the LLC might take from HG or pay for' (the VO campaign the LLC pays from March is in scope and gets an issue); Leonard's AppsFlyer note ends 'I'll set CF up on it' (he moves it); Leonard's Google Analytics note adds 'nothing for the LLC to take or pay'; Arthur's mail says BigQuery and Firebase 'cost nothing after that, so there's nothing there for the LLC' — the platform /prompt review of rev2 (run_forensics/rev2/1_prompt_FAIL_r2.md) scored UGT 2 on three Linear-write forks no record settled: a new issue for the VO campaign, ENG-2451's assignee and ENG-2452's state; truth unchanged
- rev3: third blind fork sweep: Arthur's ENG-2446 note adds 'so the LLC doesn't need them' (the build boxes even if Sunset can't sell them); Leonard's Helpshift note adds 'CF was never on it, its support is the contact on its store listing and that moves with the game' (no separate CF player-support line) — a third blind fork sweep of the rev3 records (fresh agent, no answer key) reproduced the plan, totals and every Linear write; these two readings were the only ones the records left open that the platform's own sweep had not already settled; truth unchanged (plan/sweep_dispositions.md)
- rev4: platform /hardness FAIL 2 on rev3 (RB1, RB2, RB4, RB5): Leonard's VO status drops the project word ('moves to our new company's card from March', 'count it in what CF costs us each month', no 'barely billing'); the project description decides by who pays first ('to Done if one of us pays it himself through May (even if HG still owns it) or if the LLC takes it and nothing is left to do on it; to Todo if the LLC takes it and something is still to do ...; to Canceled if it stays with HG'); ENG-2454's note says only 'cancelled it on the 11th' and a Leonard reply under the base layer.ai post (C09UHHN6PFZ/1770837702.167889, Feb 12 19:15Z, parent thread fields updated) says the CF character concept art is only in layer.ai and asks Robert to pull it out himself; ENG-2445's note gives Arthur's ~$95 before his trim and a new Arthur email 'jenkins' (Feb 13 04:20Z, to Robert, cc Leonard) says in its second paragraph that CF's account bills $62 a month now; mechanism EXC, trap T6, chain C6, channel CH-EXC and surface slots R1, R5, L2 leave the design (scenario design-2) — one platform Opus 5.5 pre-check on rev3 got about 96 % right (run_forensics/rev3/precheck, 01a_Hardening_Report.md): the campaign was found by a search for the project word, the layer.ai caveat sat on the issue note every run reads, CF's figure was on the issue note, and the store-notice miss changed only wording; EXC was never live; truth unchanged (LLC 7 / Founder 3 / HG 28, $3,450)
- rev4: fallback red team RT4-1..RT4-12: the campaign's bill visibly moves; Done is tested first with 'pays it himself through May (even if HG still owns it)'; 'the build boxes are HG's'; 'just its live stacks'; 'concept art', 'layer.ai' and 'pull it out yourself'; the reply at 19:15Z after the channel's last base message that day — an independent hg.py-only reviewer of the rev4 changes found four majors (campaign payer and state, GitHub Done vs Canceled, 'barely billing' vs 'bills now') and minor coherence points (01b_Redteam_Fallback_rev4.md); all fixed, truth unchanged
- rev4: fourth blind fork sweep: Leonard's layer.ai reply ends 'it goes with CF, the account itself just lapses'; his campaign status ends 'so count it as its own line in what we pay each month'; his Calm Play note on ENG-2472 moves to Feb 12 23:41Z, before the ground rules (23:46Z) — a blind fork sweep of the rev4 records (fresh agent, no answer key) reproduced the plan, totals and Linear writes and left layer.ai's state open (Canceled vs Todo), the campaign's own row weak and the Calm Play note later than the rules; truth unchanged (plan/sweep_dispositions.md)
- rev4: fifth blind fork sweep: Leonard's layer.ai reply now ends 'the art goes with CF, there's nothing on the layer account for our new company to take, it just lapses' (no 'LLC' keyword, so an 'LLC' Slack search still misses it) — a focused blind re-sweep of the rev4 forks for the prompt check (04_Prompt_Check.md finding 1) still rated ENG-2454's state OPEN (Todo/Robert vs Canceled); the clause makes Canceled the only reading under the project rule 'to Todo if the LLC takes it'; truth unchanged (plan/sweep_dispositions.md, fifth sweep)
- issue notes: one owner note per issue (37 comments): the nine planned notes verbatim plus 28 routine notes that restate base facts (plan/build_sql.py NOTES) — the design's per-record surface: each issue's own status lives in its note
- hazard_acknowledgements L13: resolution excluded -> dated_claim — T17 cites C05KNDCHAAG/1770842137.835489 as a dated claim; 'excluded' requires an uncited record (hardness_gate hazard_scope)
- Earlier (rev1): scenario re-certified before this stage closed: surface V1 gained COMPLETE and EXC (the solver showed both move the LLC row count), controls and over-application operators became exact solver keys, channels became solver-shaped (scale, ch_miss), and the native wording (App Store template, deck line, project description, Jenkins texts) moved into the scenario builder; `stage_gate.py scenario` PASS re-pasted.

### /injection Checks A–C walk

- Inventory: 136 INSERT, 3 UPDATE (the three root counter updates), no DELETE, no upsert; every statement in the record ledger.
- Check A (references, uniqueness, identities, id contracts): PASS — base_check Check A; every parent resolves (Slack roots bc4bc3d0e2a0ea6ae92cb2a9712e8f76, 73ec270a3d07eb8d8488384898be079e and bdb4f7af824ec3819acdf5fc3cc480ea, Drive roots d_63fffeb4fab5233ed5bb73 and d_9f7ba94f7526d54d8482ba, board 640643a3fd8f3ca308d9318e and list 640643a3fd8f3ca308d93195, team_ENG, Linear users usr_63fffeb4fab5233e / usr_Robert / usr_cc3e90160f490686, repo harmonygames-Games/GameOfDominoes, branch arthur.blake/boombitWithEcon); ids unique over full collections (1.F); one account per person per service.
- Check B (structure, literal JSON, generated / NOT NULL columns): PASS — sql_lint 0 errors; no text_fts / body_text_fts; every *_json column holds literal JSON; Linear dates YYYY-MM-DDTHH:MM:SSZ; state_history_json an empty JSON array.
- Check C (dates, parent/reply, statuses, counts, claimed updates, superseding records): PASS — base_check Check C; every seeded event before the seed bound except the Monday call (plan field); replies after their roots; issue notes after their issues; PR opened < merged < build < notice; superseding records are later than what they supersede (version_records sorted, hardness_gate PASS).

### Touched-data census

The census and its hazard dispositions are in 'Touched-data census and coherence hazards' above (all six categories; L13 acknowledged as dated_claim; 16 NB cards dispositioned).

### Counter-readings

| Category | Counter-reading (strongest argument it fails) | Evidence that resolves it | Verdict |
|---|---|---|---|
| Temporal | the hub cites 'my draft from Tuesday' and 'Monday's call', which could be the wrong days | draft f_d996e4c434ce160dc52596 created Tue Feb 10 18:30Z; event evt_f5f279f282d20ec86bb8e5 Mon Feb 16 18:00Z, created Feb 13 05:45Z before the hub's split mail | PASS |
| Temporal | the ground rules point at the Trello card and the card at the Linear project, which could postdate them | project 2026-02-12T23:24:00Z, issues from 2026-02-12T23:25:00Z, card 2026-02-12T23:42:00Z, ground rules 2026-02-12T23:46:00Z (each after what it cites) | PASS |
| Temporal | Robert's deck could predate the VO campaign it budgets | deck f_7d2c9e7822e87b92a11759 2026-02-08T03:00:00Z, after the campaign's creation C09UHHN6PFZ/1770404397.819789 (Feb 6) and Leonard's 'keep both campaigns live' C07C2866011/1770489896.754049 | PASS |
| Temporal | the App Store notice could be about the 19:56Z BoomBit build, not the support build | #218 starts 21:40Z after the merge (21:10Z) and its change line is the support change (C05433XK267/1770932970.616709); BoomBit's build C09SWTHEMEW/1770926214.816149 is about interstitials | PASS |
| Semantic / Category | 'Kub card' vs 'KubLLC card' could read as two cards | C0ADGSZKR3R/1770937232.664809 ('my KubLLC card') and the mail's 'my Kub card' are the same author and payer | PASS (short form) |
| Semantic / Category | 'the warehouse's daily revenue table' could mean REVENUE_DAILY_V2 or AD_REVENUE | snowflake /tables/12 vs /tables/13 give the same January sums; netting Apple's 30 % on IAP still leaves $162.46 > $140 | PASS |
| Cross-service Referential | the GitHub branch name differs between Jenkins and GitHub | NB-13 pattern (C05433XK267 2026-01 /1237 vs github /branches/981); no branch is graded | PASS (pre-existing, not graded) |
| Cross-service Referential | Arthur's $48 GitHub plan disagrees with base receipts of $86 | base receipts include Copilot $38; the mail says 'now that copilot is off' (gmail blake@harmonygames.co GitHub receipts) | PASS |
| Cross-service Referential | Arthur's $48 GitHub plan disagrees with the Feb 3 receipt ($52 Team Plan + $38 Copilot) | gmail threads/blake@harmonygames.co_1856132203079406675.json; the mail says 'back to the $48 team plan now that I dropped the extra seat and copilot is off' (Jan 3 receipt: $48) | PASS |
| Cross-service Referential | Combo Fighter's client calls ZM's Phoenix API, so ZM's account staying with HG breaks CF | confluence /pages/8 (Dec 31, 2025); Arthur's ENG-2445 note (Feb 13): CF's own account (auth and backend stacks; D04UY3DQJE5 2026-01 deploy notes; the note does not name Nakama, which Confluence says CF doesn't use) and 'CF stopped calling ZM's phoenix api' | PASS |
| Semantic / Category | 'VO campaign' could be read as a video campaign, or Leonard's status could ignore the Unity playable test | VO = event/value optimization (C09UHHN6PFZ/1770404397.819789, C07C2866011/1770438169.228649); the status names only the Meta campaigns and says the Unity test uses up the $100 left there (C09UHHN6PFZ/1770845845.148039) | PASS |
| Quantitative | the ZM hosting has no exact figure, so '$0 covers $0' could keep ZM | Arthur's ENG-2443 note: phoenix, nakama and aurora untrimmed, billing every month on HG's AWS bill (HG's whole AWS line is $1,485 in Jan and Feb 2026, snowflake.FINANCE.EXPENSES.MONTHLY_BURN); any bill exceeds the 0.00 January income | PASS |
| Quantitative | two live campaigns would make the line ~$6k | C07C2866011/1770489896.754049 is superseded by C09UHHN6PFZ/1770938400.370665 (only the VO campaign) | PASS |
| State / Lifecycle | Kapwing 'cancelled' has no Robert-visible record (the checklist shows [-]) | Arthur's note comment_8c69b5b90f9f6c03a0a168d25e6b75bd matches Kapwing's notice blake@harmonygames.co_1856962040028188034.json (Feb 12 22:56Z) and C0ADGSZKR3R/1770937188.477219 | PASS |
| State / Lifecycle | the analytics pipeline being turned off conflicts with keeping Metabase for CF data | CF's events go through Firebase (C07C2866011/1770298939.402129: 'the default in_app_purchase sent by Firebase'); the Firebase/BigQuery/dbt/Metabase stack (C04UEQVDVB7/1706816838.694319) is separate from the Kinesis/Glue account (page_aws_infra) | PASS |
| State / Lifecycle | #1917 merged after the Feb 9 shutdown decision reads as work after the announcement (L13) | hazard_acknowledgements L13 dated_claim; base Combo-Fighters#37 merges Feb 13; the support move is part of the wind-down (C0ADGSZKR3R/1770789534.434749) | PASS |
| Identifier / Format | a hand-typed address or a changed id scheme | eval lint FAIL 0 CHECK 0; sql_lint 0 errors; roster emails only; ids per 1.A; collisions 0 (1.F) | PASS |
| Identifier / Format | usr_Robert breaks the usr_<16hex> scheme | base Linear user id, I10 (linear data.json /users) | PASS (pre-existing) |
| People status | Leonard or Arthur act after leaving channels (NB-1) | both stay full members (C0ADGSZKR3R/1770842402.772039 'keep maybe the three of us'); activity.json active_feb_2026 | PASS |
| Other | a designed disagreement reads as two silent system fields | each overturning record is a dated human message or a vendor notice (T1, T4, T5, T6, T16 in Intended disagreements) | PASS |
| Other (designed T1) | best argument the $1k/$140 clash is an unintended inconsistency | Arthur's later DM D04V95AAAHW/1770952200.665739 says the account was trimmed ('down to $140 … one small task and the db at its floor'), after his own Feb 10 'I think I can get the cost down' (C0ADGSZKR3R/1770682200.870289) | designed |
| Other (designed T4) | best argument the ~$300 vs $248 clash is unintended | Arthur's mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> explains the drop (extra Metabase seats removed, Copilot off) | designed |
| Other (designed T5) | best argument the done note vs the rejection is unintended | the rejection robert@harmonygames.co/<136285951.151027292.1770967800000@email.apple.com> is later and describes the email-draft support option that only the #218 build has; Jenkins #218 ties it to the change | designed |
| Other (control, rev4) | best argument the Calm Play note is a fact, not a mistake, now that EXC is purged | the ground rules f_1e468a9d69ea0f0a2001f5 name 'the new one Blake and I are setting up'; C04UEQVDVB7/1701383740.580749 and C04UEQVDVB7/1703492127.063049 are explicit founders' records; the note says 'could', a suggestion | PASS |
| Temporal (rev4) | the layer.ai reply could predate its root or show Robert ignoring a mention | C09UHHN6PFZ/1770923700.470906 is Feb 12 19:15Z, a day after the root C09UHHN6PFZ/1770837702.167889 and after the channel's last base message that day (C09UHHN6PFZ 2026-02 /726, 19:08Z); the root's thread fields are updated | PASS |
| Temporal (rev4) | the Jenkins email could contradict Arthur's own ENG-2446 note | the note (01:07Z) says he will move the jobs; the email robert@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com> (04:20Z, 11:20pm ET) says he moved them 'tonight'; both say the boxes are HG's | PASS |
| Quantitative (rev4, designed T19) | best argument $95 vs $62 is an unintended inconsistency | the same owner's later email robert@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com> says why: the extra copy of CF's backend from the January redeploy was shut down; base deploy notes D04UY3DQJE5 2026-01 /18-/26 show two backend endpoints (us-west-1, then us-east-1) | designed |
| Semantic / Category (rev4) | 'our new company's card' could mean Sunset or Arthur's KubLLC | the ground rules f_1e468a9d69ea0f0a2001f5 call the LLC 'the new one Blake and I are setting up for the three of us'; Leonard's status C09UHHN6PFZ/1770938400.370665 says the campaign is on his card only till the end of Feb | PASS |
| State / Lifecycle (rev4) | the new Done rule could make GitHub Canceled (HG owns the org) or the campaign Done (on Leonard's card) | the rule tests Done first and says 'pays it himself through May (even if HG still owns it)'; Arthur carries GitHub through May (robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com>); the campaign leaves Leonard's card in March (C09UHHN6PFZ/1770938400.370665); red team RT4-2, RT4-4 | PASS |
| Other (designed T7, rev4) | best argument the art-export step is hidden, not discoverable | the reply C09UHHN6PFZ/1770923700.470906 names 'layer.ai', @-mentions Robert and sits under the item's own access-date post (the only Feb 2026 'layer.ai' hit); the ground rules bring a game's art over | designed |
| Other (designed T16) | best argument 'both campaigns' still holds | C09UHHN6PFZ/1770938400.370665 is five days later and says the install one is paused | designed |
| Other (designed notes/draft) | best argument the notes doc or draft is the authority | the hub names 'the ground rules doc' and only the draft's layout; f_1e468a9d69ea0f0a2001f5 is two days newer | designed |
| Other (designed T17) | best argument the repos move to the LLC now | C0ADGSZKR3R/1770933450.410449 (a day later) keeps GitHub under HG until the data is sold | designed |
| Other (designed T10) | best argument the January funding posts set the split | they are about equity before the shutdown; the split mail robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com> is the LLC's rule | designed |

Lazy-solver pass on the implemented records (first hits, no threads, bulk shortcuts, stop at the first conclusion): it reads the hub, #winddown and the project's issue list and notes; takes DD's hosting from the issue note (~$1k / $300, so DD fails the take test), Metabase + dbt at ~$300 as LLC cash, CF's stacks at the issue note's ~$95, layer.ai as closed, Arthur's 'done' as finished (ENG-2462 Done), every step by Mar 1, and never finds the campaign, the DM reply, Arthur's two mails, the layer.ai reply, the store notice or the warehouse. It scores 14.3 % on the rev4 surface (plan/policy_scores.txt, first policy); no implemented record hands it a deciding value (fact_check --no-leak PASS: $140, $62 and $248 each live only in their home rows).

Re-verified this stage through hg.py (not carried from notes): REVENUE_DAILY January sums and the IAP/ads split; REVENUE_DAILY_V2; the AWS guide text; the App Store rejection template; Jenkins job numbering (#216, #217) and branch; PR #1916 and branches/981; Linear users and the newest ENG issue; Trello board, last idShort and member ids; the #winddown checklist, keep list and action items; #prototype Feb 11 lines; Leonard's $3,750 and $100 lines; the CF backend lines (C09UHHN6PFZ 2026-01 'I'll start backend', Feb 6 'Blake's backend').

Blind sweeps (before sealing):
- rev1: a fork sweep and a coherence sweep. Their dispositions, with base pointers, are in `Working_Files/plan/sweep_dispositions.md`.
- rev2 and rev3: two more fork sweeps.
- rev4: a fresh agent with no answer key, hg.py only, Robert-visible records, Linear writes first. It reproduced the solver independently:
  - DD in at $183.11 against $140, ZM out;
  - CF's stacks at $62 from Arthur's Jenkins email over his $95 note;
  - ENG-2462 Todo/Arthur from the App Store notice;
  - Metabase, dbt and GitHub Done;
  - a new campaign issue, Todo/Leonard;
  - $3,450 a month, $1,150 each, and Arthur $902.
- What the rev4 sweep left open, and how each was handled:
  - layer.ai's state (OPEN): fixed in two steps. The fourth sweep's fix ('the account itself just lapses') still left it open to a fifth, focused re-sweep run for the prompt check; the reply now ends 'the art goes with CF, there's nothing on the layer account for our new company to take, it just lapses', so the issue is Canceled and the export step stays on the sheet.
  - The campaign's own row (WEAK): fixed with 'count it as its own line'.
  - The Calm Play note dated after the rules (WEAK): fixed. It is now dated before them.
  - DD support's By date (WEAK): the rubric accepts Feb 15–28.
  - DD's assignee (WEAK): settled as in rev3.
  - Its PR #1917 'merged=None' was a rendering artefact of its dump; the SQL inserts merged = true.
- rev4, fifth sweep (2026-11-06, focused on the six items rev4 touched, fresh agent, no answer key): every value matched the solver; ENG-2454's state was the only OPEN fork (fixed above); GitHub, ENG-2462, CF stacks and the campaign were WEAK with a record beating each; Jenkins gets no line (`plan/sweep_dispositions.md`).
- Before sealing the design: an independent fallback red team of the rev4 design delta (`01b_Redteam_Fallback_rev4.md`).

Unresolved:
- Opus 5.5 landing rates remain UNCALIBRATED priors (n_eff 1–4); one run per family at most for DONE and DATE.
- The two forecast views disagree by construction (see above).
- The rev4 sweep's fixes (layer.ai reply, campaign line, Calm Play note time) were not re-swept by a fresh agent; each is a one-sentence record change re-checked here through hg.py.

```
STAGE GATE injection: PASS — Task_Authoring/task_inputs · 01_Universe_Inject.sql#f1a290ced176 · 01_Hardness_Manifest.json#3d5b59a8bb48 · 01_Grounding_Dossier.md#1188624c21da · solver/solver.py#f8392ca56fc2 · 01c_Dispositions.json#b39eba46053e · 01c_Preflight_Report.json#c43f18f375cc · 00_Assigments.md#97be9960492b · 01_Scenario_Design.md#e791f8bc1662 · 01_Hardness_Manifest.draft.json#c9b02d5f4a26 · 01_Gradable_Surface.json#ecfd436788e5 · __context__#226493b2011a · __assignment__#b4220a529c0a · __policy__#dc4ab5df3cdd · __gate_policy__#f8638415ca2c · __review__#ee46d7814b64 · blocking 0 · warnings 0 · checks 40
[PASS] assignment.v3_context: Robert / Co-founder & Creative Director; easy cap <90%; freeze 2026-02-14T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe normal; KB bound; clock Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
[PASS] structure.outputs: 6 output(s) present: 01_Universe_Inject.sql, 01_Hardness_Manifest.json, 01_Grounding_Dossier.md, solver/solver.py, 01c_Dispositions.json, 01c_Preflight_Report.json
[PASS] structure.inputs: 4 input(s) present: 00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json)
[PASS] chain.scenario: upstream 'scenario' PASS pasted and current (01_Scenario_Design.md#e791f8bc1662, 01_Hardness_Manifest.draft.json#c9b02d5f4a26, 01_Gradable_Surface.json#ecfd436788e5, 00_Assigments.md#97be9960492b, __context__#226493b2011a, __assignment__#b4220a529c0a, __policy__#dc4ab5df3cdd, __gate_policy__#f8638415ca2c, __review__#c87336eaacce)
[PASS] structure.sections: 17 required sections present and non-empty (01_Grounding_Dossier.md)
[PASS] structure.placeholders: no placeholders in 01_Grounding_Dossier.md
[PASS] evidence.entity: 29/29 items carry a source pointer (min 90%)
[PASS] evidence.keyword: 22/22 items carry a source pointer (min 100%)
[PASS] evidence.persona_reach: 11/11 items carry a source pointer (min 100%)
[PASS] evidence.record_ledger: 139/139 items carry a source pointer (min 100%)
[PASS] evidence.facts_for_human: 35/35 items carry a source pointer (min 100%)
[PASS] tool.sql_lint: sql_lint re-run matches the paste: errors 0, warnings 6, rows 139
[PASS] tool.injection_lint: hg.py lint: 0 FAIL, 0 CHECK dispositioned, 0 INFO; sha256 f1a290ced176 matches 01_Universe_Inject.sql
[PASS] review.warning_dispositions: every sql_lint warning class dispositioned (clock×6)
[PASS] tool.base_check: base_check pasted PASS; re-run PASS
[PASS] tool.base_claims: base_claims pasted PASS; re-run PASS
[PASS] tool.hardness_gate: hardness_gate (SQL) pasted PASS; re-run PASS
[PASS] structure.design_delta: final manifest keeps all 54 draft ids
[PASS] structure.preflight: 01c_Preflight_Report.json bound by sha256 to the current SQL, solver, surface, manifest and dispositions
[PASS] solver.contract: solver contract re-run PASS
[PASS] mutation.dispositions: 30 mutation and intervention results each carry a written disposition (01c_Dispositions.json)
[PASS] geometry.upper_bound: U 0.870 (67/77) vs 1 - cap 0.10 (V3 easy): PASS (bound PASS); re-run U 0.870 PASS (bound PASS)
[PASS] geometry.margin: L_max 0.2077922077922078 vs (1 - cap) + 0.10: OK (advisory: the margin is a judgment, not a proof)
[PASS] liveness.dispositions: every liveness flag dispositioned (11 flag(s))
[PASS] forecast.preregistered: forecast hev_82f1150ec1778af9 pre-registered in the ledger (UNCALIBRATED)
[PASS] tool.check_sql_pasted: persona_view check-sql --load-bearing output pasted with verdict PASS
[PASS] reach.injection: 47 scoped load-bearing ids YES for robert
[PASS] structure.facts_declared: manifest declares 20 load-bearing fact(s) in `facts`
[PASS] tool.fact_check: fact_check --no-leak pasted PASS; re-run PASS
[PASS] kb.coherence_hazards: coherence audit cites 24 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 2 seeded speakers each cited with activity.json status; conventions.json cited
[PASS] kb.integrations: companions listed per integrations.json (14 INT ids, services ['gcal', 'gdocs', 'gdrive', 'github', 'gmail', 'gsheets', 'gslides', 'linear', 'slack', 'trello'])
[PASS] boundary.anchor_naming: 4 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 30 evidenced counter-readings (of 35 found; need ≥ 18) in 01_Grounding_Dossier.md
[PASS] review.coverage: self-review addresses all 9 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

