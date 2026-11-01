# 01 Grounding Dossier — jl-zm-difficulty-baseline (design v6) · contains no prompt, OE or criterion text

Persona Julia Lawson <julia.lawson@harmonygames.co> (Product Manager) · Long Horizon · `effective_profile: long` · clock 2025-10-01T00:00:00Z (the assignment's universe date read as 00:00 UTC; `tools/hg_clock.py`). SQL: `task_inputs/01_Universe_Inject.sql` (built by `support/task_work/jl_difficulty/build_sql.py`; 158 INSERT, 1 UPDATE, 10 schemas). Final manifest: `task_inputs/Working_Files/01_Hardness_Manifest.json` (draft ids kept; four `design_delta` entries).

## 1.A Structural

| Table | Columns used (NOT NULL from `references/universe_schema_live.json`) | Base sample ids | Rows seeded |
|---|---|---|---|
| slack.slack_messages | id, ts, channel_id, type, user_id, text, thread_parent_id, reply_count, attachments_json, created_at | C090N54TG79/1759176983.189479; C093LEZGF6J/1756140119.128149 (GitHub-app mirror shape) | 5 + 1 UPDATE (parent counters 1c181040768a5650a30ad1e68cf1b9b4) |
| trello.trello_cards / trello_actions | id, name, "idBoard", "idList", "desc", "idShort", url, badges_json; actions data_json | trello:68c457c45f9e302837332bf4 (ZM ROADMAP card), its createCard 68c457c45f9e302837332c13 | 2 cards (68daca5871dba40417a00383, 683dbef4e319167a802bd888), 4 actions (createCard ×2, updateCard 68dbe36f4b2b4fffb7525fde 2025-09-30T14:04:31Z, commentCard) |
| gmail.gmail_threads / gmail_messages | id = mailbox + thread id, mailbox + RFC Message-ID; in_reply_to; internal_date = date | gmail:leonard@harmonygames.co_1842219327413774622.json | 5 threads, 10 messages (julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>, julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com> in Julia's mailbox) |
| gdrive.drive_files / gdocs.docs_documents / gsheets.* | f_/d_ + 22 hex; same id and sharing on drive and doc/sheet rows | f_34f0950581934de1278969 (base sheet), d_8140f09bf9f1b94cb8ee2d (Julia's root) | folder d_96489e1e00a56685625939, doc f_9ec79682ff351aa466364a, sheet f_0ba93ae0238d9ed4178212 + 3 tabs |
| gslides.slides_presentations / slides_pages / slides_page_elements | presentation_id = drive f_ id; page object_id slide_ + 12 hex; element el_ + 12 hex, kind TEXT_BOX, 9144000x5143500 | f_44566b6f0e293b4cc3097a (Robert's deck, slide_3d6a2f2461a0 / el_4c7286d51d6f) | f_048bf5e69f8e7f1a659a5c: 3 slides, 3 text boxes |
| gcal.gcal_events | event_id evt_+22 hex per calendar, ical_uid 32hex@hg4, start/end ts + json | evt_f07c2d5d56f5110a888cef (Julia's BoomBit kickoff) | 5 copies (evt_91674a9c23d012a9ac34da on Julia's calendar) |
| github.github_pr_comments / timeline_events | PR id + #c_n, PR id + #ev_n; every comment has a `commented` event | harmonygames-Games/match3d#401#c_1, #401#ev_1 to #ev_6 | harmonygames-Games/match3d#401#c_2, harmonygames-Games/match3d#401#ev_7 |
| linear.linear_comments | id cmt_+20 hex, issue_id, author_id (linear users), body, created_at | base has 0 comments (the `linear/data.json` comments list is empty) | 109 |

## 1.B Entity

| Entity | Spelling / id | Services (cited) | Agreement |
|---|---|---|---|
| Julia Lawson | julia.lawson@harmonygames.co; Slack EMPLOYEE_0005_SLACK_ID; Linear usr_8140f09bf9f1b94c; Trello 793af7ca6940bf18eb516c75 | `entity.py resolve "Julia Lawson"`; owner of f_0ba93ae0238d9ed4178212 | AGREE |
| Arthur Blake ("Blake") | arthur.blake@ (files blake@…); Linear usr_cc3e90160f490686; Confluence user_EMPLOYEE_0025; GitHub EMPLOYEE_0025_GITHUB_USERNAME | C090N54TG79/1756751373.593569 ("Blake"); julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>; harmonygames-Games/match3d#401#c_2 | AGREE |
| Leonard Hayes | leonard.hayes@; Slack EMPLOYEE_0038_SLACK_ID; Trello PERSON_6094_TRELLO_USER_ID; Drive root d_63fffeb4fab5233ed5bb73 | trello:68c457c45f9e302837332c13 (his createCard); D05HB64NMQU/1759261706.530914 | AGREE |
| Brian Foster | brian.foster@; Slack EMPLOYEE_0026_SLACK_ID (member of C090N54TG79) | C090N54TG79/1759185077.402611; evt_6a462dfd25e2f70ed73bcf | AGREE |
| Vincent Parker | vincent.parker@; Slack EMPLOYEE_0012_SLACK_ID (member of C090N54TG79); Linear usr_65c76e0b87aa7e9b | C090N54TG79/1759248760.118527; cmt_9698eebaf0663ba1f7da | AGREE |
| Robert | robert@; Linear usr_Robert; Confluence user_EMPLOYEE_0016 | f_048bf5e69f8e7f1a659a5c; cmt_7f0329231d8b9f6e2d97 | AGREE |
| Zombie Match 3D store builds | iOS 0.3.49 / Android 0.3.133 | C0880U9751A/1759182908.627389 (iOS); C07C2866011/1759075866.111309 (Android; Julia NO); julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> | AGREE |
| Starting tier threshold | > 90 (code, ZOM-42) vs >= 90 (ZOM-199) | ZOM-42, ZOM-199 descriptions; julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com> | DISAGREE (designed: dated reply settles it) |
| PR #401 | harmonygames-Games/match3d#401 "Split enrage parameter into separate ones" merged 2025-08-25T16:42:14Z | github data.json; harmonygames-Games/match3d#401#c_2 | AGREE |
| ZOM-n vs ENG-n | ZOM-199 / ENG-199 twins (N01) | linear data.json | AGREE (task names ZOM only) |

## 1.C Voice and realism

Lengths, hours and style from `references/universe_kb/conventions.json` (`slack.length_chars_by_channel_type`, `slack.per_person_hours_and_style`, `gmail.internal_subject_len_chars`, `linear` one- or two-line comments); seeded speakers with `status_at_clock` from `references/universe_kb/activity.json` (computed for the Feb 2026 clock; every speaker posted in Sep 2025).

| Speaker | status_at_clock | Real samples (pointer) | Seeded rows |
|---|---|---|---|
| leonard.hayes@harmonygames.co | active_feb_2026 (activity.json) | C08R27X0EAH/1756922313.032399 "I think we really need to adjust rage by Friday"; C0880U9751A/1759182908.627389 "I just released 0.3.49 on IOS"; C090N54TG79/1756751169.213249 | D05HB64NMQU/1759261706.530914; card 68daca5871dba40417a00383 + comment 68dbfa4362a051efb5e0ae45; 683dbef4e319167a802bd888; invite; agenda f_9ec79682ff351aa466364a; cmt_74e7511b3cccd02e1209 |
| arthur.blake@harmonygames.co | active_feb_2026 (activity.json) | D05H5QL09PX/1755800367.839589 "I think it just looks at the item it replaced"; D05H5QL09PX/1757434464.819109 "Can you test Android 1804?"; C08R27X0EAH/1756749623.058599 | julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>; julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>; C090N54TG79/1756912929.304417; harmonygames-Games/match3d#401#c_2; 94 Linear notes |
| brian.foster@harmonygames.co | active_feb_2026 (activity.json) | C08R6BF4ENN/1756835318.028769 "Recently I tested the latest Season Pass build"; C08R6BF4ENN/1756999375.251619; C08R6BF4ENN/1757671069.174799 | C090N54TG79/1759185077.402611 |
| vincent.parker@harmonygames.co | quiet_since_2025-12 (activity.json) | C08R27X0EAH/1756922710.548259 "no not at all, I haven't experienced such thing"; C0880U9751A/1750165444.708639; C090N54TG79/1756753434.723599 | C090N54TG79/1759248760.118527; notes on ZOM-246/254/263/274/280 |
| robert@harmonygames.co | active_feb_2026 (activity.json) | C090N54TG79/1756751305.466159; C0880U9751A/1758921802.962539; C090N54TG79/1759176983.189479 | f_048bf5e69f8e7f1a659a5c (Jun 16); notes on ZOM-23, ZOM-288, ZOM-293 |
| oliver.brooks@harmonygames.co | active_feb_2026 (activity.json) | C08R6BF4ENN/1756960785.464819 "Builds for testing SP"; C08R6BF4ENN/1756996117.185929; C08R6BF4ENN/1757646802.623469 | notes on ZOM-49, ZOM-161, ZOM-262, ZOM-275 |
| owen.baker@harmonygames.co | active_feb_2026 (activity.json) | harmonygames-Games/match3d#271 (author); harmonygames-Games/match3d#258 | note on ZOM-295 |
| marcus.bennett@harmonygames.co | active_feb_2026 (activity.json) | C090N54TG79/1756748966.836219 "the new material has 3001 rendering que"; harmonygames-Games/match3d#238 | note on ZOM-258 |

Posting hours: Leonard's ask 19:48Z and card 18:05Z/15:41Z fall in his 14:00–23:00Z band; Blake's mail 09:12Z/13:26Z and notes follow each ticket's own completion time (the base closed those tickets at those hours, several on UTC weekends — see warning dispositions); Brian 22:31Z and Vincent 16:12Z inside their Sep 2025 hours.

## 1.D Keyword

| Term | Base hits | Seeded / reached via |
|---|---|---|
| "difficulty baseline" | NEW TERM — introduced in trello:68daca5871dba40417a00383 and trello:683dbef4e319167a802bd888, reached via the ask D05HB64NMQU/1759261706.530914 | the ask names the card |
| "store builds" | NEW TERM — introduced in julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>, reached via card rule 3 (trello:68daca5871dba40417a00383) | Gmail search |
| "monster enrage" | NEW TERM — introduced in gsheets:f_0ba93ae0238d9ed4178212, reached via card rule 5 | Sheets search |
| "dynamic difficulty" | base: ZOM-42 title; C08GLSV8Z7W (Domino Delights) messages | NEW TERM page title f_048bf5e69f8e7f1a659a5c, reached via card rule 5 |
| "tiers:" (note tag) | NEW TERM — introduced in cmt_735d60b29ce006b58217 and the other 3 tagged notes, reached via card rule 1 | per-ticket comment reads |
| "tuning" | NEW TERM — introduced in gcal:evt_91674a9c23d012a9ac34da and gdocs:f_9ec79682ff351aa466364a, reached via card rule 7 / rule 2 | Calendar / Docs search |

## 1.E Persona reach

| Record | Service | Visibility path | Role |
|---|---|---|---|
| 6f77386571537f0bd88c959bdc216f94 (D05HB64NMQU/1759261706.530914) | slack | Julia is a member of DM D05HB64NMQU | LB anchor |
| 5f6ed4d5ae1a0a04b616af6d6d2dda43 (D05HB64NMQU/1759267002.665190) | slack | same DM; thread reply under Julia's own message | LB (L7) |
| julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> | gmail | Julia's own mailbox copy (INBOX) | LB H2 |
| julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com> | gmail | Julia's own mailbox copy (INBOX), own thread julia.lawson@harmonygames.co/1844695547248825769 (round 5: Blake changed the subject) | LB H2 reply |
| f_0ba93ae0238d9ed4178212 | gsheets | Julia owns it | LB H3 |
| f_9ec79682ff351aa466364a | gdocs | shared with Julia (reader) | LB format |
| d_96489e1e00a56685625939 | gdrive | shared with Julia (writer) | LB destination |
| evt_91674a9c23d012a9ac34da | gcal | Julia's own calendar copy | LB recipients |
| f_048bf5e69f8e7f1a659a5c | gslides | shared with Julia (reader) | LB tier rules (card rule 5) |
| 6995ba10acf2888f04f033b8bbeb5629 (C090N54TG79/1756912929.304417) | slack | Julia is a member of private C090N54TG79 | LB correction |
| 84ff828e81ba52e8969c580f49944394 (C090N54TG79/1759185077.402611) | slack | Julia is a member of private C090N54TG79 | decoy |
| 0282d920d9ff69fefb74a4ae417b0e18 (C090N54TG79/1759248760.118527) | slack | Julia is a member of private C090N54TG79 | distractor |
| 5313e8da22604987e53ba497dc709655 (C093LEZGF6J/1756141351.508113) | slack | UNVERIFIED-OK: integration companion in public #zombie-prs (Julia not a member); alternate_evidence_ids: harmonygames-Games/match3d#401#c_2 | companion, not load-bearing |

`python3 Task_Authoring/tools/persona_view.py check-sql julia_lawson Task_Authoring/task_inputs/01_Universe_Inject.sql --load-bearing <lb ids>` (verbatim):

```
CHECK-SQL as julia_lawson <julia.lawson@harmonygames.co>
[YES LB] L6 gdrive.drive_files insert d_96489e1e00a56685625939 - file is shared with the persona (shared_with_emails)
[YES LB] L9 gdrive.drive_files insert f_9ec79682ff351aa466364a - file is shared with the persona (shared_with_emails)
[YES LB] L11 gdrive.drive_files insert f_f494073fc667097c3c2c6b - file is shared with the persona (shared_with_emails)
[YES LB] L13 gdrive.drive_files insert f_0ba93ae0238d9ed4178212 - persona owns the file
[YES LB] L15 gdrive.drive_files insert f_048bf5e69f8e7f1a659a5c - file is shared with the persona (shared_with_emails)
[YES LB] L17 gdocs.docs_documents insert f_9ec79682ff351aa466364a - file is shared with the persona (shared_with_emails)
[YES LB] L20 gdocs.docs_documents insert f_f494073fc667097c3c2c6b - file is shared with the persona (shared_with_emails)
[YES LB] L22 gsheets.sheets_spreadsheets insert f_0ba93ae0238d9ed4178212 - persona owns the file
[YES LB] L25 gsheets.sheets_sheets insert f_0ba93ae0238d9ed4178212, f_0ba93ae0238d9ed4178212#0 - persona owns the file
[YES LB] L27 gsheets.sheets_sheets insert f_0ba93ae0238d9ed4178212, f_0ba93ae0238d9ed4178212#1 - persona owns the file
[YES LB] L29 gsheets.sheets_sheets insert f_0ba93ae0238d9ed4178212, f_0ba93ae0238d9ed4178212#2 - persona owns the file
[YES LB] L31 gslides.slides_presentations insert f_048bf5e69f8e7f1a659a5c - file is shared with the persona (shared_with_emails)
[YES LB] L34 gslides.slides_pages insert f_048bf5e69f8e7f1a659a5c, slide_cb43e6c53c57 - file is shared with the persona (shared_with_emails)
[YES LB] L36 gslides.slides_page_elements insert f_048bf5e69f8e7f1a659a5c, el_bf0658751368, slide_cb43e6c53c57 - file is shared with the persona (shared_with_emails)
[YES LB] L38 gslides.slides_pages insert f_048bf5e69f8e7f1a659a5c, slide_7329e157cabf - file is shared with the persona (shared_with_emails)
[YES LB] L40 gslides.slides_page_elements insert f_048bf5e69f8e7f1a659a5c, el_d0979892e11a, slide_7329e157cabf - file is shared with the persona (shared_with_emails)
[YES LB] L42 gslides.slides_pages insert f_048bf5e69f8e7f1a659a5c, slide_fc10746fe8c2 - file is shared with the persona (shared_with_emails)
[YES LB] L44 gslides.slides_page_elements insert f_048bf5e69f8e7f1a659a5c, el_0573925c4c2c, slide_fc10746fe8c2 - file is shared with the persona (shared_with_emails)
[YES LB] L46 slack.slack_messages insert cec246a6e43158f200fe144f0dd7039c, CAFC495E4006/1759226461.318204 - persona EMPLOYEE_0005_SLACK_ID is in members of mpim mpdm-robert--leonard.hayes--julia.lawson-1
[YES LB] L49 slack.slack_messages insert abe096ff0b5d7216efbc889e91d6d13a, CAFC495E4006/1759229513.774912 - persona EMPLOYEE_0005_SLACK_ID is in members of mpim mpdm-robert--leonard.hayes--julia.lawson-1
[YES LB] L51 slack.slack_messages insert 6f77386571537f0bd88c959bdc216f94, D05HB64NMQU/1759261706.530914 - persona EMPLOYEE_0005_SLACK_ID is in members of im D05HB64NMQU
[YES LB] L53 slack.slack_messages insert 84ff828e81ba52e8969c580f49944394, C090N54TG79/1759185077.402611 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] L55 slack.slack_messages insert 0282d920d9ff69fefb74a4ae417b0e18, C090N54TG79/1759248760.118527 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] L57 slack.slack_messages insert 33c941fae57ba8d1e23bc1dff9ce3e2c, D05HB64NMQU/1759262838.442871 - persona EMPLOYEE_0005_SLACK_ID is in members of im D05HB64NMQU
[YES LB] L59 slack.slack_messages insert 914b21ab6448fac2e4b4f8d164bea41a, D05HB64NMQU/1759181932.207413 - persona EMPLOYEE_0005_SLACK_ID is in members of im D05HB64NMQU
[YES LB] L61 slack.slack_messages insert 5f6ed4d5ae1a0a04b616af6d6d2dda43, D05HB64NMQU/1759267002.665190 - persona EMPLOYEE_0005_SLACK_ID is in members of im D05HB64NMQU
[YES LB] L63 slack.slack_messages insert 6995ba10acf2888f04f033b8bbeb5629, C090N54TG79/1756912929.304417 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[UNVERIFIED] L65 slack.slack_messages insert 5313e8da22604987e53ba497dc709655, C093LEZGF6J/1756141351.508113 - public channel #zombie-prs: persona EMPLOYEE_0005_SLACK_ID is not a member; non-member reads not established (U1)
[UNVERIFIED] L67 slack.slack_messages update 1c181040768a5650a30ad1e68cf1b9b4, C093LEZGF6J/1756140111.461039 - public channel #zombie-prs: persona EMPLOYEE_0005_SLACK_ID is not a member; non-member reads not established (U1)
[UNVERIFIED] L68 slack.slack_messages insert 1491582caca6e2769404e7b09eac3d55, C093LEZGF6J/1751565015.214669 - public channel #zombie-prs: persona EMPLOYEE_0005_SLACK_ID is not a member; non-member reads not established (U1)
[UNVERIFIED] L70 slack.slack_messages update 6a42cb69b452e0c89f36407f56a3d84b, C093LEZGF6J/1751546520.776819 - public channel #zombie-prs: persona EMPLOYEE_0005_SLACK_ID is not a member; non-member reads not established (U1)
[UNVERIFIED] L71 slack.slack_messages insert f590e554c3b5e1d6b01cc9d1395388eb, C093LEZGF6J/1751591124.205377 - public channel #zombie-prs: persona EMPLOYEE_0005_SLACK_ID is not a member; non-member reads not established (U1)
[UNVERIFIED] L73 slack.slack_messages insert e7977b0f608c8af00f33c4744ab7ea1f, C093LEZGF6J/1751591125.638214 - public channel #zombie-prs: persona EMPLOYEE_0005_SLACK_ID is not a member; non-member reads not established (U1)
[UNVERIFIED] L75 slack.slack_messages update 2e34453f3fc13f34986b9d16b76c4119, C093LEZGF6J/1751588271.756019 - public channel #zombie-prs: persona EMPLOYEE_0005_SLACK_ID is not a member; non-member reads not established (U1)
[YES LB] L99 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844679607844896665 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L102 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>, ju - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L108 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1844679607845770780 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L110 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L116 gmail.gmail_threads insert robert@harmonygames.co/1844679607845885165 - row is in mailbox robert@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L118 gmail.gmail_messages insert robert@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>, robert@h - row is in mailbox robert@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L124 gmail.gmail_threads insert brian.foster@harmonygames.co/1844679607844988891 - row is in mailbox brian.foster@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L126 gmail.gmail_messages insert brian.foster@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>, br - row is in mailbox brian.foster@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L132 gmail.gmail_threads insert arthur.blake@harmonygames.co/1844679607845878519 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L134 gmail.gmail_messages insert arthur.blake@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>, ar - row is in mailbox arthur.blake@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES LB] L140 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844695547248825769 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L142 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>, ju - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L144 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1844695547249175707 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L146 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L148 gmail.gmail_threads insert robert@harmonygames.co/1844695547249391903 - row is in mailbox robert@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L150 gmail.gmail_messages insert robert@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>, robert@h - row is in mailbox robert@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L152 gmail.gmail_threads insert brian.foster@harmonygames.co/1844695547248700828 - row is in mailbox brian.foster@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L154 gmail.gmail_messages insert brian.foster@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>, br - row is in mailbox brian.foster@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L156 gmail.gmail_threads insert arthur.blake@harmonygames.co/1844695547249616481 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L158 gmail.gmail_messages insert arthur.blake@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>, ar - row is in mailbox arthur.blake@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES] L160 gcal.gcal_events insert evt_dd24af1fb48e6c536f48a4 - persona is an attendee and holds its own copy evt_91674a9c23d012a9ac34da (same ical_uid and start) on julia.lawson@harmonygames.co
[YES LB] L163 gcal.gcal_events insert evt_91674a9c23d012a9ac34da - event is on the persona's own calendar julia.lawson@harmonygames.co
[YES] L165 gcal.gcal_events insert evt_56b665fee3295cce4b77d3 - persona is an attendee and holds its own copy evt_91674a9c23d012a9ac34da (same ical_uid and start) on julia.lawson@harmonygames.co
[YES] L167 gcal.gcal_events insert evt_18d9e925bfe0da49dcc9f5 - persona is an attendee and holds its own copy evt_91674a9c23d012a9ac34da (same ical_uid and start) on julia.lawson@harmonygames.co
[YES] L169 gcal.gcal_events insert evt_6a462dfd25e2f70ed73bcf - persona is an attendee and holds its own copy evt_91674a9c23d012a9ac34da (same ical_uid and start) on julia.lawson@harmonygames.co

summary: {'YES': 36, 'UNVERIFIED': 7, 'NO': 16}  unscoped rows (always visible): 128
  gcal.gcal_events: {'YES': 5}
  gdocs.docs_documents: {'YES': 2}
  gdrive.drive_files: {'YES': 5}
  gmail.gmail_messages: {'YES': 2, 'NO': 8}
  gmail.gmail_threads: {'YES': 2, 'NO': 8}
  gsheets.sheets_sheets: {'YES': 3}
  gsheets.sheets_spreadsheets: {'YES': 1}
  gslides.slides_page_elements: {'YES': 3}
  gslides.slides_pages: {'YES': 3}
  gslides.slides_presentations: {'YES': 1}
  slack.slack_messages: {'YES': 9, 'UNVERIFIED': 7}
verdict: PASS (0 load-bearing rows not visible)
```

## 1.F Collision

Every minted id was checked against the full base collection (script in this session over `linear/data.json` comments, `trello/data.json` cards+actions, `gdrive/data.json` drive_files, the GCal export and the Gmail export file names): 0 hits each. Slack `(channel, ts)` pairs are asserted unique in `build_design.py`; PR comment harmonygames-Games/match3d#401#c_2 and event harmonygames-Games/match3d#401#ev_7 continue the base numbering (#c_1, #ev_1 to #ev_6). Identity tokens: no new external person; every author is a base user id.

## Round 7 hardening (two levers on different carriers)

| Change | Records | Why |
|---|---|---|
| Blake's 'not tiers' mark on PR #271 (ZOM-295): an APPROVED review with an empty body (his usual shape: 1,098 of his 1,207 reviews are approvals) and one inline comment on MonsterSpawner.cs: 'not tiers: this is a bug fix, enrage was always meant to clear on refill health and push back. no tier version or enrage number changes here. leave it out when we list tier work' | github harmonygames-Games/match3d#271#rev_2, harmonygames-Games/match3d#271#rc_1; Slack mirrors f590e554c3b5e1d6b01cc9d1395388eb, e7977b0f608c8af00f33c4744ab7ea1f under 2e34453f3fc13f34986b9d16b76c4119 | card rule 1 already says a title match Blake marked 'not tiers' in his review on its PR stays off; ZOM-295's closing note 'merged with match3d#271' points to the PR. Replay over 15 runs: #271's inline comments were fetched by 5 of 15; GitHub comment search does not match review comments ('\"not tiers\" in:comments' returned 0 in run-2 and run-6) |
| Robert's thread reply: 'the day it got marked done, pacific time' | slack abe096ff0b5d7216efbc889e91d6d13a | every run of the round-6 batch and the hardness run wrote the UTC day; completed_at 01:17Z on ZOM-200, ZOM-274, ZOM-282 is the evening before in Pacific time (06-12, 06-20, 06-20); every other done time is between 09:26Z and 23:03Z, same day in both |
| Header comment counts (183 INSERT, 4 UPDATE) | line 3 | counts |

Base check of the new facts: PR #271 (owen.baker, opened 2025-07-04T00:17:49Z) requested Blake's review at 00:36:36Z and was merged by EMPLOYEE_0032 at 13:29:30Z, so a 01:05:22Z review fits. The diff hunk is the PR's own MonsterSpawner.cs change (ResetEnrageCounter, +524,9); the comment makes no code claim beyond 'no tier version or enrage number changes', which the PR's four files (MonsterSpawner.cs, LoseScreen.cs, DebugPanel.cs, PlayerManager.cs) bear out. No seeded or base record treats ZOM-295 as tier work ('tiers:' notes sit on ZOM-221, 281, 300, 305, 378 only). New answer: 23 tickets (Live 15, Editor only 4, Replaced 1, Not shipped 3).

## Round 6 hardening (third hidden thread)

| Change | Records | Why |
|---|---|---|
| Leonard asks Robert in their group chat with Julia what he wants on Julia's list (top level, reply_count 1); Robert answers only in the thread: three Tickets-tab columns after status (Linear assignee, the day it got marked done or blank, Linear priority) | slack CAFC495E4006/1759226461.318204 (cec246a6e43158f200fe144f0dd7039c), CAFC495E4006/1759229513.774912 (abe096ff0b5d7216efbc889e91d6d13a); ids follow sha256(channel and ts) | 22 baseline and hardness runs: every judgement trap was resisted; only thread replies land (about 55% missed). A third thread in a different conversation spreads graded weight so failing runs split |
| Card rule 2: 'Layout as in the session agenda, plus the three things Robert asked for when I asked him in our group chat.' | card 68daca5871dba40417a00383 desc and updateCard action 68dbe36f4b2b4fffb7525fde | names the source (fair pointer); the content stays in the thread |
| Header comment counts updated (179 INSERT, 3 UPDATE) | line 3 | /injection advisory C-1 |

Base check of the new facts (Linear data.json, all 24 register tickets): every ticket has an assignee; completed_at is set for the 21 Done tickets and empty for ZOM-202 (In Progress), ZOM-280 (Canceled) and ZOM-293 (Todo); priority is 1 to 4 on all 24. Group chat CAFC495E4006: members Robert (EMPLOYEE_0016), Leonard (EMPLOYEE_0038), Julia (EMPLOYEE_0005) and PERSON_6089; base history Dec 2024 to Jul 2025, then Nov 2025, so no ts collision in Sep 2025. Robert's reply avoids the words register, column and baseline.

## Round 5 hardening (failure-pattern gate)

| Change | Records | Why |
|---|---|---|
| Blake's reply moves to its own Gmail conversation (he changed the subject to 'editor stuff and ZOM-199, before Monday'; In-Reply-To/References kept) and now carries the level editor / Editor folder / debug menu stripping rule and both ZOM-199 corrections (> 90; checked when the 10th game ends, wins and losses) | 5 mailbox copies of julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>; 5 new gmail_threads rows (id = date ms << 20 + random bits, Gmail's format) | a second carrier independent of Slack threads (A14 Gmail reply): baseline round 5, runs 1/4/6 failed identically (pattern 60%) |
| The first mail keeps only the builds and the Sep 26 cut; its thread snippets now show the first mail | 5 copies of <CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> and their thread rows | the stripping rule lives in one place |
| Card rule 3: 'Blake's store builds mail and his reply to it' | card 68daca5871dba40417a00383 desc and its updateCard action 68dbe36f4b2b4fffb7525fde | incorporates the reply (rule 6 already names it) |
| Leonard's thread reply under the ask adds: name the two builds in the Editor only / Not shipped comments | D05HB64NMQU/1759262838.442871 | per-comment output rule (A21) on the thread carrier |

Code check of every new claim (match3d at the Sep 26 cut): TierManager.cs `totalGames == 10`, `cpm > 90.0f`; WinHistory.cs GetTotalGames = wins + losses; Assets/Scripts/LevelEditor and Assets/Scripts/Debug exist as named. The reply never uses the words 'store' or 'builds', so the 'store builds' search returns only the first mail's thread.

## Record ledger

| # | Service · table | Id | Manifest element | Carrier | Reach | Discovery role |
|---|---|---|---|---|---|---|
| 1 | slack.slack_messages | 6f77386571537f0bd88c959bdc216f94 | A1 / K1 | ● | DM member | first link |
| 1b | slack.slack_messages | cec246a6e43158f200fe144f0dd7039c | K19 / T32 (Leonard's question to Robert, group chat CAFC495E4006, reply_count 1) | ● | group chat member | container |
| 1c | slack.slack_messages | abe096ff0b5d7216efbc889e91d6d13a | K19 / T32 / C15 (Robert's thread reply: assignee, done day, priority) | ● | group chat member | amendment (round 6) |
| 2 | slack.slack_messages | 84ff828e81ba52e8969c580f49944394 | H2 decoy / T7 | ● | channel member | decoy |
| 3 | slack.slack_messages | 0282d920d9ff69fefb74a4ae417b0e18 | T16 | ● | channel member | distractor |
| 4 | slack.slack_messages | 5313e8da22604987e53ba497dc709655 | INT-01 companion of harmonygames-Games/match3d#401#c_2 | ● | UNVERIFIED-OK | companion |
| 5 | trello.trello_cards | 68daca5871dba40417a00383 | H1 / K2 | ● | unscoped | connecting |
| 6 | trello.trello_actions | 68daca5845e48874fb98e25a | T1 v1 | ● | unscoped | connecting |
| 7 | trello.trello_actions | 68dbfa4362a051efb5e0ae45 | K3 / T1 | ● | unscoped | overturning |
| 8 | trello.trello_cards | 683dbef4e319167a802bd888 | H1 decoy / T12 | ● | unscoped | decoy |
| 9 | trello.trello_actions | 683dbef4991df7f0987ddb73 | T12 | ● | unscoped | decoy |
| 10 | gmail.gmail_messages | julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> | H2 / K4 / T7 / T19 | ● | Julia's mailbox | connecting |
| 11 | gmail.gmail_messages | julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com> | K5 / T6 / C5 / C8 | ● | Julia's mailbox | overturning |
| 12 | gmail.gmail_threads | julia.lawson@harmonygames.co/1844679607844896665 | H2 thread (first mail only) | ● | Julia's mailbox | container |
| 12b | gmail.gmail_threads | julia.lawson@harmonygames.co/1844695547248825769 | H2 reply thread (round 5) | ● | Julia's mailbox | container |
| 13 | gsheets.sheets_spreadsheets | f_0ba93ae0238d9ed4178212 | H3 / K6 / T8 / T9 / T11 | ● | Julia owns | authority |
| 14 | gdocs.docs_documents | f_9ec79682ff351aa466364a | K11 | ● | shared | format |
| 15 | gdrive.drive_files | d_96489e1e00a56685625939 | K10 | ● | shared (writer) | write target |
| 16 | gslides.slides_presentations | f_048bf5e69f8e7f1a659a5c | K7 / T6 / T10 / T11 | ● | shared with Julia | claim met first |
| 17 | slack.slack_messages | C090N54TG79/1756912929.304417 | K8 / T11 / C1 | ● | channel member | overturning |
| 18 | gcal.gcal_events | evt_91674a9c23d012a9ac34da | K9 / T13 / C4 | ● | Julia's calendar | connecting |
| 19 | github.github_pr_comments | harmonygames-Games/match3d#401#c_2 | T8 / T21 | ● | unscoped | overturning |
| 19b | github.github_reviews | harmonygames-Games/match3d#271#rev_2 | K20 / T33 (Blake's APPROVED review, empty body) | ● | unscoped | container (round 7) |
| 19c | github.github_review_comments | harmonygames-Games/match3d#271#rc_1 | K20 / T33 / C16 (inline 'not tiers' on MonsterSpawner.cs) | ● | unscoped | amendment (round 7) |
| 19d | slack.slack_messages | f590e554c3b5e1d6b01cc9d1395388eb | INT-01 companion of harmonygames-Games/match3d#271#rev_2 (approval mirror) | ● | UNVERIFIED-OK | companion |
| 19e | slack.slack_messages | e7977b0f608c8af00f33c4744ab7ea1f | INT-01 companion of harmonygames-Games/match3d#271#rc_1 (comment mirror) | ● | UNVERIFIED-OK | companion |
| 20 | linear.linear_comments | cmt_735d60b29ce006b58217 | K13 / C2 (tagged) | ● | unscoped | connecting |
| 21 | linear.linear_comments | cmt_b0aa45d307c981ce4487 | C3 / T5 | ● | unscoped | connecting |
| 22 | linear.linear_comments | cmt_bed381141007e04f1aac | T5 | ● | unscoped | connecting |
| 23 | linear.linear_comments | cmt_bb9c4deb176b2c894ca6 | T15 | ● | unscoped | connecting |
| 24 | linear.linear_comments | cmt_68811c86e67c36e5c2f7 | T15 | ● | unscoped | connecting |
| 25 | linear.linear_comments | cmt_912bdd42ad5c8d51521f | T8 v1 | ● | unscoped | claim met first |
| 26 | linear.linear_comments | 103 further cmt_ ids (`minted_ids.json` LIN_NOTES, e.g. cmt_2c00eb8a6b1fa1796c53) | cohort surface (neutral / decisive) | ● | unscoped | per-record |
| 27 | other rows | the other 4 gmail copies per message, 4 calendar copies, page version, 3 sheet tabs, timeline event harmonygames-Games/match3d#401#ev_7, slack parent UPDATE 1c181040768a5650a30ad1e68cf1b9b4 | companions of the rows above | ● | per row | companion |

## Findability and discovery-order proofs

```
Record:              trello.trello_cards · 68daca5871dba40417a00383
Agent's likely query: "difficulty baseline" via trello search
Term present:        seeded text in the record (planned_text.json)
Competing base hits: decoys share the terms (DD card "Difficulty baseline"; base DD sheet "Parameter Optimization")
Chain position:      first link (named by the ask)
```
```
Record:              gmail.gmail_messages · julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>
Agent's likely query: "store builds" via gmail search
Term present:        seeded text in the record (planned_text.json)
Competing base hits: decoys share the terms (DD card "Difficulty baseline"; base DD sheet "Parameter Optimization")
Chain position:      connecting (card rule 3)
```
```
Record:              gmail.gmail_messages · julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>
Agent's likely query: card rules 3 and 6 name "his reply to it"; gmail search "from:arthur.blake@harmonygames.co" or "ZOM-199" (own thread, subject "editor stuff and ZOM-199, before Monday"; the "store builds" search does not return it)
Term present:        seeded text in the record (planned_text.json)
Competing base hits: decoys share the terms (DD card "Difficulty baseline"; base DD sheet "Parameter Optimization")
Chain position:      terminal (reply to the first message, own Gmail conversation)
```
```
Record:              gsheets.sheets_spreadsheets · f_0ba93ae0238d9ed4178212
Agent's likely query: "monster enrage" via sheets/drive search
Term present:        seeded text in the record (planned_text.json)
Competing base hits: decoys share the terms (DD card "Difficulty baseline"; base DD sheet "Parameter Optimization")
Chain position:      connecting (card rule 5)
```
```
Record:              gslides.slides_presentations · f_048bf5e69f8e7f1a659a5c
Agent's likely query: "dynamic difficulty deck" via slides / drive search
Term present:        seeded text in the record (planned_text.json)
Competing base hits: decoys share the terms (DD card "Difficulty baseline"; base DD sheet "Parameter Optimization")
Chain position:      connecting (card rule 5)
```
```
Record:              gcal.gcal_events · evt_91674a9c23d012a9ac34da
Agent's likely query: "ZM difficulty tuning" via calendar search / list Oct 6
Term present:        seeded text in the record (planned_text.json)
Competing base hits: decoys share the terms (DD card "Difficulty baseline"; base DD sheet "Parameter Optimization")
Chain position:      connecting (card rule 7)
```
```
Record:              gdocs.docs_documents · f_9ec79682ff351aa466364a
Agent's likely query: "ZM difficulty tuning" via docs search
Term present:        seeded text in the record (planned_text.json)
Competing base hits: decoys share the terms (DD card "Difficulty baseline"; base DD sheet "Parameter Optimization")
Chain position:      connecting (card rule 2)
```
Dynamic-change seeds: Brian's summary C090N54TG79/1759185077.402611 (claim met first: #zombie-design is the busiest difficulty channel) → overturned by the store builds mail julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>; the deck's "90 or more" (f_048bf5e69f8e7f1a659a5c) → overturned by Blake's reply julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com> (decisive: it names the code's check); ZOM-282's note cmt_912bdd42ad5c8d51521f (replaces ZOM-254; speed and damage share one value) → harmonygames-Games/match3d#401#c_2 (split into separate values) → the sheet f_0ba93ae0238d9ed4178212. Hidden-authority proofs: H1 by the ask's "difficulty baseline card" (decoy 683dbef4e319167a802bd888 returned by the same query, other game); H2 by "store builds" (decoy C090N54TG79/1759185077.402611 found by a channel search); H3 by "monster enrage" (decoy base gsheets:f_34f0950581934de1278969, other game).

## Self-validation table

| QC category | Tool-enforced | Manual evidence |
|---|---|---|
| Missing Universe Data | — | every needed fact exists and is readable (1.E check-sql PASS); the agent's write tools exist in `Evals/references/tools/catalog.json` |
| Temporal Field | sql_lint/base_check PASS (created ≤ updated, replies after parents, notes before each issue's updated_at) | text dates: "Leonard released it yesterday" in julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> (2025-09-30) = iOS 0.3.49 on 2025-09-29 (C0880U9751A/1759182908.627389); "Sep 26" cut; History tab dates match commit 84780b8d (2025-08-09) and #401 (2025-08-25) |
| Cross-service Referential | base_check Check A PASS | names spelled as in the base (Blake, Leonard, Robert); PR numbers in notes point at the PR meant (facts ZOM-173→match3d#243 … verified by fact_check) |
| Quantitative / Reconciliation | Slack parent counters updated (1c181040768a5650a30ad1e68cf1b9b4 reply_count 3); Trello badges comments 1 | sheet Live values = VarC prefab values at commit 85d1a406 (re-check, `01b_Redteam_Recheck_v3.md` #4) |
| State / Lifecycle | base_check PASS; L03 acknowledged (dated_claim) | ZOM-303 Live in code at the clock (TierManager at 85d1a406); no designed ticket status contradicts its activity |
| Identifier / Format | ids per scheme (sha Slack ids, f_/d_ 22 hex, evt_/ical, #c_/#ev_ continuation, Trello timestamped ids) | emails from the base; Robert's usr_Robert reused |
| Semantic / Category | — | card on list "Oct 21" of ZM ROADMAP; DD card on "March/April" of the Product Roadmap board; titles match content |
| Other | — | voice per 1.C; no record states a status; the reply states a code fact, not a verdict |

## Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| github | INT-01 | Slack mirror in #zombie-prs | seeded: 5313e8da22604987e53ba497dc709655 threaded under #401's opened post; parent counters updated |
| github | INT-01 | Slack mirror in #zombie-prs (round 7) | seeded: f590e554c3b5e1d6b01cc9d1395388eb (approval) and e7977b0f608c8af00f33c4744ab7ea1f (comment) threaded under #271's opened post 2e34453f3fc13f34986b9d16b76c4119; parent reply_count 4 to 6, latest_reply stays the 13:29Z merge post |
| github | INT-03 | linear[bot] PR comment | none: #401's title/branch name no Linear key |
| github | INT-23 | CodeRabbit | none seeded |
| linear | INT-04 | Linear Slack app notifications | none: base has no Linear comments, so no notification precedent |
| linear | INT-05 | Linear e-mail digests | none: same reason |
| gcal | INT-11 | invitation mails | none: `integration_exceptions` no_notify for 26fce3dc380d9da1343bcccc6072f03e@hg4 (base_check warning dispositioned) |
| gdrive / gsheets / gdocs | INT-13 | Drive Slack app DMs | none: DM-only and optional for shares |
| trello | INT-21 | Slack bot posts | none: no Trello integration exists |
| slack | INT-22 | Slack e-mail notifications | none: sparse in the base |
| gmail | — | label counters | not modelled in the base export; none |
| gslides | — | Drive row | the deck's drive_files row with identical sharing |

## Touched-data census and coherence hazards

Census: the 109 candidates and their PRs (#243, #258, #265, #267, #271, #282, #283, #289, #296, #319), #401, ZOM-42/199/254/282/303, the #zombie-design and #zombie-bugs / #zombie-match3d messages the storyline cites, the DD sheet, the ZM ROADMAP and Product Roadmap boards.

Hazards walked from `references/universe_kb/coherence_hazards.json` (all six categories):

| Category | Hazard ids in scope | Disposition |
|---|---|---|
| temporal | T04 (ZOM-282 vs #401), T05 (ZOM-282 closes before ZOM-254), T08 | dated claims (ZOM-282 note; #401 comment); rule 4 orders by creation; authors active |
| semantic_category | S02 (nested parents ZOM-50/ZOM-30), S03 (labels), S08 (page_zm3d_gdd post-clock versions) | children keep own rows; no rule uses labels; page_zm3d_gdd not cited |
| cross_service_referential | R01 (keys in text), R04 (Google ids), R06/R07 (mirrors), R08 (invite mails) | every cited key/PR exists; titles only; #401 mirror seeded; no_notify exception |
| quantitative | Q01 (thread counters), Q10 (copies per mailbox), Q11 (calendar copies) | parent counters updated; identical copies |
| state_lifecycle | L03 (ZOM-292, ZOM-387 Todo with merged PRs), L06 (ZOM-201/ZOM-293), L10 (#244 bot-only reviews) | L03 dated_claim acknowledged in the manifest; L06 folded in; L10 not cited |
| identifier_format | I03 (mailbox aliases), I05 (EMPLOYEE_0032), I08 (token logins), I10 (usr_Robert) | base forms reused |

Warning dispositions: base_check warns on the L03 hazard touch — acknowledged as `dated_claim` (notes before each issue's updated_at; SQL modifies neither issue nor PR); base_check warns on the tuning session's missing invitation mail — `integration_exceptions` no_notify.

## Intended disagreements

| # | Disagreement | Why realistic | Resolved by |
|---|---|---|---|
| 1 | ZOM-199 / the deck say >= 90; the code and ZOM-42 say > 90 | a ticket restating the spec loosely; the code kept the original | Blake's reply julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com> (2025-09-30) |
| 2 | ZOM-282 (06-21) asks +50% to both; #401 (08-25) gives speed and damage separate values | tuning after the mechanic shipped | ZOM-282 note cmt_912bdd42ad5c8d51521f (replaces ZOM-254; hp off since 06-19, commit b511fcbcd5); harmonygames-Games/match3d#401#c_2; card rule 4 (only a closing note saying so makes a ticket Replaced) |
| 3 | Brian's summary: editor bits in the store builds, +50% for every monster | a live-ops engineer's confident recap | julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> (tooling stripped); sheet f_0ba93ae0238d9ed4178212 (per monster) |
| 4 | The deck's +25% blunder line | written from ZOM-254 on Jun 16 | C090N54TG79/1756912929.304417 (2025-09-03); f_0ba93ae0238d9ed4178212 |
| 5 | DD card "Difficulty baseline" | the same rules card idea for the other game, March 2025 | scope: Domino Delights; the ask names the ZM ROADMAP card |

Best argument each is unintended, and why not: (1) two system fields would be a defect — here one is ticket prose and the other the code, and a dated human mail names which governs; (2) a Done ticket with later work — card rule 4 makes only a replacing note count, and #401 only splits numbers; (3) a teammate's summary is a human claim, the mail is later; (4) a stale page is dated and retired by a newer comment; (5) a decoy merely called a decoy would not resolve it — it differs by game scope, stated in its own text.

## Constraints for the prompt brief

| Anchor | May be named (noun phrases only) | Record |
|---|---|---|
| A1 | Leonard's difficulty baseline ask; Leonard's DM; Monday's tuning session | D05HB64NMQU/1759261706.530914 |

Never name: the card, the mail, the sheet, the page, the folder, the agenda, any ticket or PR id, the tag, the > 90 check, the attack-power amendment, any count or status. Deadline: Monday's tuning session (2025-10-06). Deliverable kinds: a register, a reply to Leonard, ticket updates.

## Fact sheet

| Key | Value | Kind | Must appear in | Home ids |
|---|---|---|---|---|
| iOS 0.3.49 | 0.3.49 | version | julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> |  |
| Android 0.3.133 | 0.3.133 | version | julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> |  |
| ZOM-173 | match3d#243 | id | cmt_bb9c4deb176b2c894ca6 | cmt_bb9c4deb176b2c894ca6, cmt_4254c1451d7cbe0d8d2a |
| ZOM-312 | match3d#265 | id | cmt_68811c86e67c36e5c2f7 | cmt_68811c86e67c36e5c2f7 |
| ZOM-292 | match3d#267 | id | cmt_7372203a46c603a31c1e | cmt_7372203a46c603a31c1e |
| ZOM-387 | match3d#319 | id | cmt_8fb73ca1d1757919dee7 | cmt_8fb73ca1d1757919dee7 |
| ZOM-352 | match3d#282 | id | cmt_564774d61032b2468dc9 | cmt_564774d61032b2468dc9 |

`python3 Task_Authoring/tools/fact_check.py … --no-leak` (verbatim):

```
FACT CHECK: PASS — 162 text-bearing rows, 8 declared facts, 12 declared superseded records
Errors: none
```

## Facts for the human

| Locator | Base/seeded | Fact | Reach | Role |
|---|---|---|---|---|
| D05HB64NMQU/1759261706.530914 | seeded | Leonard 2025-09-30T19:48:26Z: baseline before Monday; rules on the difficulty baseline card; reply with counts and when a new player gets the starting tier | DM | anchor |
| linear:cmt_df69e4a92767cbff0000 | seeded | Blake 2025-06-27: 'tiers: closing. checked on the dev build' on ZOM-281 (assigned EMPLOYEE_0032, no card word) -> member, Live | unscoped | per-record (hardening L3) |
| ZOM-42 vs match3d TierManager.cs / WinHistory.cs (base) | base | ZOM-42 and ZOM-199 say 'first 10 level'; the build's starting tier: bucketing at totalGames == 10, GetTotalGames = wins + losses -> after the first 10 games, won or lost, not level 10; CPM > 90 | unscoped | rules / reply fact (hardening L4) |
| trello:68daca5871dba40417a00383 | seeded | rules 1–7 (Leonard 2025-09-29T18:05:12Z; round 5: rule 3 reads 'Blake's store builds mail and his reply to it', in the desc and the 14:04Z updateCard action); comment 68dbfa4362a051efb5e0ae45 2025-09-30T15:41:55Z adds attack power | unscoped | authority |
| D05HB64NMQU/1759262838.442871 | seeded | Leonard 2025-09-30T20:07:18Z, thread reply under the ask: drop ZOM-30, ZOM-49, ZOM-50, ZOM-161 (analytics) and ZOM-262, ZOM-275 (tutorial); the reply also lists the Not shipped and Editor only keys; round 5: the Editor only and Not shipped comments name the two builds (ios 0.3.49, android 0.3.133) | DM | amendment (hardening L1, round 5 L9) |
| trello:68dc033bf7d24e86b8a9cc67 | seeded | checklist "Before Monday" on the card (addChecklistToCard 2025-09-30T16:20:11Z): rule 6 change (a comment on each Editor only and Not shipped ticket), rule 7 change (Brian edits) | unscoped | amendment (hardening L2) |
| D05HB64NMQU/1759267002.665190 | seeded | Leonard 2025-09-30T21:16:42Z, reply in the thread under Julia's 2025-09-29T21:38:52Z DM question ('anything you need from me before monday's tuning session?'): take ZOM-162, ZOM-163, ZOM-201, ZOM-250 off ('just those four, on top of the ones i already left off') with no comments; Brian comment access only (overrides the checklist's rule 7 change, 16:20Z) | DM | amendment (hardening L7) |
| julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> | seeded | Blake 2025-09-30T09:12:44Z: store builds iOS 0.3.49 / Android 0.3.133, cut Sep 26 (round 5: the stripping rule moved to his reply) | Julia's mailbox | authority |
| julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com> | seeded | Blake 2025-09-30T13:26:05Z, reply in its own thread julia.lawson@harmonygames.co/1844695547248825769 (subject 'editor stuff and ZOM-199, before Monday'): level editor (Assets/Scripts/LevelEditor, LevelDesigner panels), Editor folders and the debug menu (Assets/Scripts/Debug) are stripped before shipping, so editor-only tickets never reached players; the code checks cpm > 90 when the 10th game ends (wins and losses), ZOM-199's '>= 90 after the first 10 levels' is wrong | Julia's mailbox | authority + overturning evidence (hardening round 5) |
| gsheets:f_0ba93ae0238d9ed4178212 | seeded | Julia's sheet (modified 2025-09-08, after #417 brought the VarC values to main on 09-06): Live per-monster speed/damage (Boxer 0.5/0.4 … MonsterBase base prefab 0.8/0.8; Mailman, Mayor2, PartyGirl 'not copied yet', copied as is per card rule 5), hp 0 | owner | authority |
| gslides:f_048bf5e69f8e7f1a659a5c | seeded | Robert 2025-06-16: tier rules (90 or more; 80% over 10; 4 losses) and ZOM-254's +25% line | unscoped | claim met first |
| slack:C090N54TG79/1756912929.304417 | seeded | Blake 2025-09-03 in #zombie-design: the deck's blunder line is old; speed and damage per monster, no hp | channel member | overturning evidence |
| gcal:evt_91674a9c23d012a9ac34da | seeded | ZM difficulty tuning 2025-10-06T17:00Z; attendees Leonard, Julia, Robert, Arthur, Brian | Julia's calendar | recipient list |
| gdocs:f_9ec79682ff351aa466364a | seeded | agenda: one sheet, tabs Tickets and Rules in force | shared | format |
| gdrive:d_96489e1e00a56685625939 | seeded | ZM Difficulty folder (Leonard; Julia writer) | shared | write target |
| harmonygames-Games/match3d#401#c_2 | seeded | Blake 2025-08-25: #401 gives speed and damage separate values; drops the unused EnrageHealth method | unscoped | evidence |
| C090N54TG79/1759185077.402611 | seeded | Brian 2025-09-29: everything incl. editor bits in store builds; +50% for every monster | channel | decoy |
| C090N54TG79/1759248760.118527 | seeded | Vincent 2025-09-30: drop the list in #zombie-design | channel | distractor |
| trello:683dbef4e319167a802bd888 | seeded | Domino Delights card, 2025-06-02 | unscoped | decoy |
| linear ZOM-42 | base | full spec: > 90; promotion 80% over up to 10; demotion 4 straight losses or <= 50% over up to 10; record resets | unscoped | authority text |
| linear notes | seeded | 109 notes; tagged "tiers:": ZOM-221, ZOM-300, ZOM-305, ZOM-378 (cmt_735d60b29ce006b58217); members 24 (16 Live, 4 Editor only, 3 Not shipped, 1 Replaced) | unscoped | per-record evidence |

## Platform follow-ups

- Confirm in the Opus pre-check that the seeded Linear notes render through `linear_list_comments` (●, §6b) and that `linear_list_issues`' query does not search comment text (budget `conditional_on`).
- Confirm whether the platform shows the 9 Blake tickets changed after the clock in their pre-clock state (non-members either way).
- Slides: the deck text is in element text (●); confirm it renders through gslides_get_presentation_text in the pre-check.
- No ○ carrier is load-bearing (GCal description unused).

## Self-review

`python3 Task_Authoring/tools/sql_lint.py Task_Authoring/task_inputs/01_Universe_Inject.sql` (verbatim):

```
schemas touched (10): gcal, gdocs, gdrive, github, gmail, gsheets, gslides, linear, slack, trello
rows by schema: {'gdrive': 5, 'gdocs': 2, 'gsheets': 4, 'gslides': 7, 'slack': 16, 'trello': 11, 'gmail': 20, 'gcal': 5, 'github': 7, 'linear': 110}  total rows: 187  ops: {'insert': 183, 'update': 4}
errors: 0  warnings: 19
  warn  line 160: gcal.gcal_events.start_ts = 2025-10-06T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 160: gcal.gcal_events.end_ts = 2025-10-06T18:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 163: gcal.gcal_events.start_ts = 2025-10-06T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 163: gcal.gcal_events.end_ts = 2025-10-06T18:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 165: gcal.gcal_events.start_ts = 2025-10-06T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 165: gcal.gcal_events.end_ts = 2025-10-06T18:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 167: gcal.gcal_events.start_ts = 2025-10-06T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 167: gcal.gcal_events.end_ts = 2025-10-06T18:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 169: gcal.gcal_events.start_ts = 2025-10-06T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 169: gcal.gcal_events.end_ts = 2025-10-06T18:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 216: linear.linear_comments.created_at = 2025-06-21T00:59:55Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 244: linear.linear_comments.created_at = 2025-06-29T00:00:29Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 266: linear.linear_comments.created_at = 2025-06-21T01:02:01Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 270: linear.linear_comments.created_at = 2025-06-21T01:12:34Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 274: linear.linear_comments.created_at = 2025-06-21T00:59:25Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 280: linear.linear_comments.created_at = 2025-06-21T01:00:16Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 288: linear.linear_comments.created_at = 2025-06-21T01:09:19Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 360: linear.linear_comments.created_at = 2025-07-27T20:40:47Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 364: linear.linear_comments.created_at = 2025-08-17T00:24:56Z falls on a weekend (UTC) — business messages should be on weekdays
```

Warning dispositions: clock warnings (gcal start/end 2025-10-06) — a not-yet-happened future meeting, allowed as a deadline; weekend warnings (Linear notes at UTC weekend times) — each note sits minutes before its ticket's own base completion/update time, which the base already records at that hour; no Confluence statement remains (`/injection` F1).

`python3 Task_Authoring/tools/base_check.py Task_Authoring/task_inputs/01_Universe_Inject.sql` (verbatim):

```
BASE CHECK (/injection A + C, static): PASS  — 183 inserts, 4 updates
Check A — records, references, IDs: PASS
Check C — dates and relationships: PASS
Warnings (2):
  line 300: linear.linear_comments: Hazard touch L03 (state_lifecycle: Issue Todo/Backlog but a referencing PR merged) — seeded references to ['ZOM-292', 'ZOM-387']. The task now contains a pre-existing inconsistency (Cross-Service Coherence fails on presence): keep it out or make the reconciliation the explicit job
  line 160: gcal.gcal_events: meeting 26fce3dc380d9da1343bcccc6072f03e@hg4 'ZM difficulty tuning' has 4 attendee(s) but no invitation mail ('Invitation: ZM difficulty tuning @ …') in any attendee mailbox — INT-11 base: 836/941 meetings with attendees have one (2298/2974 attendee mailboxes); add the copies or declare integration_exceptions [{record_id, reason: 'no_notify: …'}]
  note: gsheets.sheets_sheets: no base-reference rules (checked by sql_lint only)
  note: gslides.slides_page_elements: no base-reference rules (checked by sql_lint only)
  note: gslides.slides_pages: no base-reference rules (checked by sql_lint only)
  note: trello.trello_attachments: no base-reference rules (checked by sql_lint only)
  note: trello.trello_check_items: no base-reference rules (checked by sql_lint only)
  note: trello.trello_checklists: no base-reference rules (checked by sql_lint only)
```

`python3 Task_Authoring/tools/hardness_gate.py …/01_Hardness_Manifest.json …/01_Universe_Inject.sql` (verbatim):

```
HARDNESS GATE (long): PASS
  [ok] effective_profile: effective_profile 'long' for 'Long Horizon' → thresholds 'long'
  [ok] sql_lint_clean: 0 lint error(s) — run tools/sql_lint.py
  [ok] base_consistency: /injection-style checks vs the base universe: A 0 finding(s), C 0 finding(s), 1 warning(s) — run tools/base_check.py --manifest
  [ok] persona_reach: 142 load-bearing seeded ids for julia_lawson (125 in unscoped services = visible, 17 judged by persona_view check-sql); not provably visible: none
  [ok] fact_consistency: fact_check: 0 error(s) (8 declared facts), 0 drift warning(s); first: none — run tools/fact_check.py --manifest --no-leak
  [ok] hazard_scope: 1 pre-existing hazard(s) among task-touched records; state/lifecycle or referential without a verified resolution: none; resolved/other: ['L03']
  [ok] services_injected: 10 schemas injected (gcal, gdocs, gdrive, github, gmail, gsheets, gslides, linear, slack, trello); need ≥ 10
  [ok] rows: 183 INSERTed rows (UPDATE companions not counted; 187 rows in all); need ≥ 120
  [ok] services_carrying_weight: 10 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: schemas injected but absent from the design: none
  [ok] seeded_ids_exist_in_sql: 105 seeded ids cited; missing from SQL: none
  [ok] anchors: 1 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 20 fragments; need ≥ 12
  [ok] ask_fragment_services: 10 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 16 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 10 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 110; need ≥ 30 (source-defined: True)
  [ok] evidence_surfaces: 3 surfaces over 2 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 115; need ≥ 30
  [ok] call_budget: unconditional (verified) floor 172 of 175 planned calls (3 conditional on unverified tool behaviour count 0); need floor ≥ 100 (Long Horizon; plan ~600 for headroom)
  [ok] call_budget_spread: 10 services in budget; largest share outside the per-record phase 29% (≤ 50%)
  [ok] traps: 34 traps across 9 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 8 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 12 supersessions (9 with versions in ≥ 2 services, 3 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: 12 trap(s) with version_records; the records' own timestamps (SQL created_at/ts/date/updated_at, or the base record) must be strictly increasing in the listed order (oldest first); bad: none
  [ok] distractors: 6 distractors of 5 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 12 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 16 chains with 9 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] hidden_authorities: 3 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 2 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 17 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 10 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 4 writes over 4 services; each must depend on findings
  [note] call budget: planned total 175, unconditional floor 172 — the conditional rows count once their tool behaviour is verified (then drop conditional_on)
```

**Check A–C walk** (`Evals/0_Injection_Quality_Eval.md`): inventory 183 INSERT / 4 UPDATE (round 7 adds the #271 review, its inline comment, two #zombie-prs mirrors and the parent reply_count UPDATE) (no DELETE, no upsert). Check A (references, uniqueness over the full collections, identities, id contracts): PASS (base_check A; 1.F 0 collisions). Check B (structure, literal JSON, generated/NOT NULL columns): PASS (sql_lint 0 errors; no *_fts column written). Check C (dates, parent/reply, statuses, counts, superseding records): PASS (base_check C; replies after parents; counters updated).

| # | Category | Counter-reading (strongest case it FAILS) | Evidence that resolves it | Verdict |
|---|---|---|---|---|
| 1 | Temporal | Blake's mail says "Leonard released it yesterday" — if the release was on another day it contradicts | C0880U9751A/1759182908.627389 at 2025-09-29T21:55Z; julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> at 2025-09-30T09:12Z | PASS |
| 2 | Semantic / Category | the DD card and the ZM card share the title root "Difficulty baseline" | trello:683dbef4e319167a802bd888 on the Product Roadmap board, text scoped to Domino Delights | PASS |
| 3 | Cross-service Referential | a note cites a PR whose files contradict it | fact_check PASS on ZOM-173→match3d#243 etc.; notes name no file (`01b_Redteam_Recheck_v3.md` R2/R3 fixed) | PASS |
| 4 | Quantitative | the sheet's per-monster values differ from the prefabs | Live tab copied from the VarC prefabs at commit 85d1a406 (re-check #4 values) in gsheets:f_0ba93ae0238d9ed4178212 | PASS |
| 5 | State / Lifecycle | ZOM-292 / ZOM-387 Todo with merged PRs (L03), a sibling of a status defect | notes cmt_7372203a46c603a31c1e, cmt_8fb73ca1d1757919dee7 explain the umbrella tickets; neither is a member | PASS |
| 6 | Identifier / Format | the mirror id or parent update breaks the Slack scheme | 5313e8da22604987e53ba497dc709655 = sha256(C093LEZGF6J|ts)[:32]; parent 1c181040768a5650a30ad1e68cf1b9b4 from the base | PASS |
| 7 | People status | Vincent (quiet_since_2025-12) voiced on Sep 30 | Vincent posts in C08R27X0EAH through Sep 2025 (C08R27X0EAH/1758546048.524829, 2025-09-22) | PASS |
| 8 | Other | the reply reads as stating the answer | julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com> states the code's check, not a register value; the rules row and ZOM-199 comment still need the agent | PASS |
| 9 | Intended disagreement 1 | >= 90 vs > 90 is two silent fields | ZOM-199 prose vs ZOM-42 prose + code; a dated human mail (julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>) names the governing one | PASS |
| 10 | Intended disagreement 2 | ZOM-282 Done, #401 later splits its value | ZOM-282 note cmt_912bdd42ad5c8d51521f (hp off since 06-19, b511fcbcd5) and harmonygames-Games/match3d#401#c_2 | PASS |
| 11 | Intended disagreement 3 | Brian's summary contradicts Robert's Sep 3 per-monster message | Brian is wrong by design; C08R27X0EAH/1756922765.033199 and f_0ba93ae0238d9ed4178212 agree | PASS |
| 12 | Intended disagreement 4 | the deck contradicts Robert's own Jun 19 "+100%" | the deck is dated 2025-06-16, before that change (C0880U9751A/1750370473.240179) | PASS |
| 13 | Intended disagreement 5 | the DD card is a same-scope rival | its text names Domino Delights and ENG tickets; trello:683dbef4e319167a802bd888 | PASS |

Prior `/injection` (attempt 6adfee3ef9092601a61245bb, FAIL): F1 Confluence rows removed — the write-up is the Slides deck f_048bf5e69f8e7f1a659a5c and Blake's correction the Slack message C090N54TG79/1756912929.304417; F2 the DD card re-dated 2025-06-02T15:10:44Z (after #210, 2025-05-27); A1 `sequence` kept — listed in `references/universe_schema_live.json` for linear.linear_comments.

Unresolved: none blocking; platform follow-ups listed above.

```
STAGE GATE injection: PASS — Task_Authoring-2/task_inputs · 01_Universe_Inject.sql#b64bc2f2c6dc · 01_Hardness_Manifest.json#a3264f8b32ac · 01_Grounding_Dossier.md#dfb5e8014ce1 · blocking 0 · warnings 0 · checks 28
[PASS] structure.outputs: 3 output(s) present: 01_Universe_Inject.sql, 01_Hardness_Manifest.json, 01_Grounding_Dossier.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json)
[PASS] chain.scenario: upstream 'scenario' PASS pasted and current (01_Scenario_Design.md#a91532254b57, 01_Hardness_Manifest.draft.json#48595035d225)
[PASS] structure.sections: 17 required sections present and non-empty (01_Grounding_Dossier.md)
[PASS] structure.placeholders: no placeholders in 01_Grounding_Dossier.md
[PASS] evidence.entity: 10/10 items carry a source pointer (min 90%)
[PASS] evidence.keyword: 6/6 items carry a source pointer (min 100%)
[PASS] evidence.persona_reach: 13/13 items carry a source pointer (min 100%)
[PASS] evidence.record_ledger: 34/34 items carry a source pointer (min 100%)
[PASS] evidence.facts_for_human: 21/21 items carry a source pointer (min 100%)
[PASS] tool.sql_lint: sql_lint re-run matches the paste: errors 0, warnings 19, rows 187
[PASS] review.warning_dispositions: every sql_lint warning class dispositioned (clock×10, weekend×9)
[PASS] tool.base_check: base_check pasted PASS; re-run PASS
[PASS] tool.hardness_gate: hardness_gate (SQL) pasted PASS; re-run PASS
[PASS] structure.design_delta: final manifest keeps all 73 draft ids
[PASS] tool.check_sql_pasted: persona_view check-sql --load-bearing output pasted with verdict PASS
[PASS] reach.injection: 16 scoped load-bearing ids YES for julia_lawson; 1 denied/unverified probe(s), not load-bearing, each with YES alternate_evidence_ids
[PASS] structure.facts_declared: manifest declares 8 load-bearing fact(s) in `facts`
[PASS] tool.fact_check: fact_check --no-leak pasted PASS; re-run PASS
[PASS] kb.coherence_hazards: coherence audit cites 21 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 9 seeded speakers each cited with activity.json status; conventions.json cited
[PASS] kb.integrations: companions listed per integrations.json (9 INT ids, services ['gcal', 'gdocs', 'gdrive', 'github', 'gmail', 'gsheets', 'gslides', 'linear', 'slack', 'trello'])
[PASS] boundary.anchor_naming: 2 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 13 evidenced counter-readings (of 13 found; need ≥ 12) in 01_Grounding_Dossier.md
[PASS] review.coverage: self-review addresses all 9 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```





