# 01 Grounding Dossier: julia_zm_audience_read (rev1) · contains no prompt, Oracle Event or criterion text

Persona Julia Lawson <julia.lawson@harmonygames.co> (Product Manager) · Long Horizon · `effective_profile: extreme` with the requester's `volume_exception` (260/160, unchanged) · universe synth-cut, seed bound 2025-10-01T00:00:00Z, Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC). SQL `task_inputs/01_Universe_Inject.sql`, final manifest `Working_Files/01_Hardness_Manifest.json`, solver `Working_Files/solver/solver.py`. Every total below is read from `solver/truth.json`. Times are UTC.

**Truth (from truth.json).** 60 sessions: 17 counted, 43 not counted (13 coached, 11 device, 9 game industry, 10 build). Casual n 9 mean 3.833; RPG n 8 mean 3.375; gap 0.458; lead casual; decision hold. Re-run notes 21. Panel 3.33 over 9 (void player 8). Retention D7 9.09 install-weighted over 47 rows.

## 1.A Structural

| Table | Columns used (schema of record `references/universe_schema_live.json`) | Base sample ids | Rows seeded |
|---|---|---|---|
| slack.slack_messages | id = sha256(channel|ts)[:32], ts, channel_id, type, user_id, text, thread_parent_id, reply_count, reply_users_count, latest_reply, created_at | C090N54TG79/1758517286.431379; C090N54TG79/1758581651.167799 | 13 inserts, 4 updates |
| gmail.gmail_threads | id = mailbox/numeric thread id, user_email, snippet | leonard.hayes@harmonygames.co/1843922088670958384 | 36 inserts |
| gmail.gmail_messages | id = mailbox/RFC Message-ID, thread_id, label_ids_json, internal_date = date, from_email, to_json, body_text, headers_json | leonard.hayes@harmonygames.co/1843922088670958384 | 36 inserts |
| gdrive.drive_files | id f_ + 22 hex, parents_json, owner_email, shared_with_emails_json, modified_time | f_89fadbc54660c9881d8cf9; d_8140f09bf9f1b94cb8ee2d | 65 inserts |
| gdocs.docs_documents | document_id = drive id, body_text, drive_file_id, same sharing as the Drive row | f_89fadbc54660c9881d8cf9 | 62 inserts |
| gsheets.sheets_spreadsheets | spreadsheet_id = drive id, owner_email, modified_time | seeded f_43bc35baf77fd59f4e57b8, shape from base sheets in gsheets data.json | 2 inserts |
| gsheets.sheets_sheets | spreadsheet_id, sheet_id, title, grid_json | seeded f_43bc35baf77fd59f4e57b8 tabs Log and Register | 3 inserts |
| gslides.slides_presentations | presentation_id = drive id, revision_id | seeded f_a087f049d271e9aa9f567f | 1 inserts |
| gslides.slides_pages | presentation_id, object_id slide_ + 12 hex, index | seeded f_a087f049d271e9aa9f567f | 3 inserts |
| gslides.slides_page_elements | page_object_id, object_id el_ + 12 hex, kind TEXT_BOX, text | seeded f_a087f049d271e9aa9f567f | 3 inserts |
| gcal.gcal_events | event_id evt_ + 22 hex per calendar, ical_uid 32 hex@hg4, start_ts/end_ts and json twins, attendees_json | evt_b371a24b8dad3a2cd9f432; evt_f08d0e87c8c7aafe580d42 | 2 inserts |
| linear.linear_issues | id = identifier, team_id, state_id, created_at, started_at, completed_at, updated_at, state_history_json empty list | ZOM-559; ZOM-566 | 61 inserts |
| linear.linear_comments | id cmt_ + 20 hex, issue_id, author_id, body, created_at | base has none; injected rows ride on Ask_Carriers §6b | 61 inserts |
| github.github_review_comments | id = pr#rc_n, pr_id, author_login, path, diff_hunk, line/position/commit_id null as on all 26 base rows, seq | harmonygames-Games/match3d#476#rc_26 | 1 inserts |
| github.github_reviews | id = pr#rev_n, state, body, submitted_at, seq | harmonygames-Games/match3d#476#rev_2 | 1 inserts |
| github.github_pull_requests | updated_at only (UPDATE) | harmonygames-Games/match3d#476 | 0 inserts, 1 updates |
| trello.trello_cards | id, name, "idBoard", "idList", "desc", "idShort", badges_json, "dateLastActivity" | 6851a6569f3bf818760632ab (board) | 1 inserts |
| trello.trello_actions | id, type createCard, "idMemberCreator", data_json | 6851a6569f3bf818760632ab (board) | 1 inserts |

Totals from `sql_lint`: 352 inserted rows, 5 updates, 10 schemas. Slack timestamps are six decimals; Gmail dates follow the mailbox's shape; Linear dates are `YYYY-MM-DDTHH:MM:SSZ`.

## 1.B Entity

| Entity | Spelling / id | Services (cited) | Agreement |
|---|---|---|---|
| Julia Lawson | julia.lawson@harmonygames.co; Slack EMPLOYEE_0005_SLACK_ID; Linear usr_8140f09bf9f1b94c; Trello 793af7ca6940bf18eb516c75 | owner of f_43bc35baf77fd59f4e57b8; C090N54TG79/1758553214.330914 | AGREE |
| Leonard Hayes | leonard.hayes@harmonygames.co; Slack EMPLOYEE_0038_SLACK_ID; Trello PERSON_6094_TRELLO_USER_ID | C090N54TG79/1758517286.431379; owner of f_748d26e760e54651eaa0d8 | AGREE |
| Robert | robert@harmonygames.co; Slack EMPLOYEE_0016_SLACK_ID; Linear usr_Robert | C090N54TG79/1759176983.189479; D05GU6L0XFH/1758913471.205816 | AGREE (I10 id shape kept) |
| Brian Foster | brian.foster@harmonygames.co; Slack EMPLOYEE_0026_SLACK_ID; no Gmail (SC-6) | D076RBM29JS/1758659012.418207; f_524278b67bfa30dde78699 | AGREE |
| Vincent Parker | vincent.parker@harmonygames.co; Linear usr_65c76e0b87aa7e9b | ZOM-567; cmt_38b3cc50dceda37f40f5 | AGREE |
| Arthur Blake | arthur.blake@harmonygames.co; GitHub EMPLOYEE_0025_GITHUB_USERNAME | harmonygames-Games/match3d#476#rc_27; C05433XK267/1758803475.436309 (Blake/visionBot) | AGREE; owner of the job, not the CLI author (Samuel Turner's commits) |
| Claire Morgan | claire.morgan@harmonygames.co; full name on every form (P01: GitHub mononym Claire) | julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>; evt_da65644831bc088267263d | AGREE |
| Marcus Bennett | marcus.bennett@harmonygames.co; full name on the form (S04) | ZOM-598 | AGREE |
| Martin Walsh | martin.walsh@harmonygames.co; distinct from Martin Lewis | ZOM-626 | AGREE |
| Zombie Match 3D / Puzzles vs. Zombies | app lineage K02; ZM in seeded text; vendor subject keeps the old name | julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com> | AGREE (designed dual naming, listed for the human) |
| Build ids | 0.3.38 (38) and 0.3.40 (40) iOS; 0.3.127 (127) Android; 0.3.127 (1943) non-store | C0880U9751A/1758643365.607149; C05433XK267/1758575557.575349 | AGREE |
| Vision Bot run #15 | Success, Sep 25 12:31Z, branch Blake/visionBot, no PR yet | C05433XK267/1758803475.436309; harmonygames-Games/match3d#476 | DISAGREE (designed: dated claim cmt_38b3cc50dceda37f40f5, overturned by rc_27) |
| Coached gathering | form says no coaching; Claire's later mail says she took them through it | julia.lawson@harmonygames.co/<CAefcc9dd45170efad4834318d398795bc1db8@mail.gmail.com>; julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com> | DISAGREE (designed: same author, later mail) |
| ZOM-n vs ENG-n | ZOM-567 to ZOM-627 are seeded; ENG twins unrelated (N01) | ZOM-567 | AGREE (task names ZOM only) |

## 1.C Voice and realism

Lengths, hours and style follow `references/universe_kb/conventions.json` (`slack.length_chars_by_channel_type`, `slack.per_person_hours_and_style`, `gmail.internal_subject_len_chars`, `linear.title_prefixes_by_team`). Status from `references/universe_kb/activity.json`, build per-universe-v1, clock 2025-10-01T07:00:00Z. Samples were read through `hg.py records` in this session from messages/C0880U9751A and messages/C08R27X0EAH.

| Speaker | status_at_clock | Real samples (pointer) | Seeded rows |
|---|---|---|---|
| leonard.hayes@harmonygames.co | active_sep_2025_quiet_in_oct (activity.json) | C0880U9751A/1757468100.342529 "Played 50 levels on 0.3.35 - no major bugs "; C0880U9751A/1757561459.538129 "I played 50 levels on ipad and 190 levels on iphone since yesterday"; C0880U9751A/1757561468.193799 "ios build is the best we have had so far" | C090N54TG79/1758554405.774120, C090N54TG79/1759266627.418203, 68dc0acf1815df76ed9b887d, julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com> |
| robert@harmonygames.co | active_sep_2025_quiet_in_oct (activity.json) | C0880U9751A/1756938765.961369 "what levels are hardcoded right now? Can you check? Or can I check somewhere?"; C0880U9751A/1756938770.142759 "Need to find a way to expose this to us"; C0880U9751A/1756939901.116369 "so.. what level is it loading from anyways?" | D05GU6L0XFH/1758913471.205816, C090N54TG79/1759167008.881274, julia.lawson@harmonygames.co/<CA01dc2d92371c7bfa63e451026f81fffed801@mail.gmail.com> |
| julia.lawson@harmonygames.co | active_sep_2025_quiet_in_oct (activity.json) | C0880U9751A/1757009163.675589 "No I don't dare :smile:"; C0880U9751A/1757011652.972019 "No, if yours are working for sure we can just use these"; C0880U9751A/1757062878.243419 "It's all good, [PERSON_NAME_0120]. Thank you very much :[USERNAME_26053]:" | C090N54TG79/1758553214.330914, C0880U9751A/1758555040.262718, ZOM-568 comment cmt_2fbcaf2d990d8b4e9c0d |
| brian.foster@harmonygames.co | active_sep_2025_quiet_in_oct (activity.json) | C0880U9751A/1758216621.873139 "We should set these tutorial panels to be visible only once"; C0880U9751A/1754286903.240279 "I'll test it today"; C0880U9751A/1754316473.926929 "I tested 3 times, it works great! Thank you" | D076RBM29JS/1758659012.418207, f_524278b67bfa30dde78699 |
| vincent.parker@harmonygames.co | active_sep_2025_quiet_in_oct (activity.json) | C0880U9751A/1757401488.171809 "There is a pr called something like [PERSON_NAME_0120]/physics material etc"; C0880U9751A/1757447035.630449 "Thank you! Remaining ones are not blocker. Can you fix them in a separate branch for now?"; C0880U9751A/1757447837.158399 "Sure but remaining are not blockers for today. " | cmt_38b3cc50dceda37f40f5, ZOM-567, F-VINCENT mail |
| arthur.blake@harmonygames.co | active_sep_2025_quiet_in_oct (activity.json) | C0880U9751A/1757020274.320379 "That most likely means nothing changed on those objects"; C0880U9751A/1757020284.760899 "Do they already have MeshColliders?"; C0880U9751A/1757020485.136389 "Are you getting errors when you update the object list?" | harmonygames-Games/match3d#476#rc_27, F-ARTHUR mail |
| claire.morgan@harmonygames.co | active_sep_2025_quiet_in_oct (activity.json) | C0880U9751A/1757420853.613709 "I see, it will be deleted with script right? Im not touching anything at the moment"; C08R27X0EAH/1758527811.664279 "I might have broke these juices, I will simply reuploud these objects if that's ok?" | julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>, julia.lawson@harmonygames.co/<CAefcc9dd45170efad4834318d398795bc1db8@mail.gmail.com>, evt_da65644831bc088267263d |
| marcus.bennett@harmonygames.co | active_sep_2025_quiet_in_oct (activity.json) | C0880U9751A/1757576067.326989 "Or u just say the liquid itself doesn't look good"; C0880U9751A/1757576091.862099 "În that case we can change the liquid impact [USERNAME_19058]."; C0880U9751A/1758126786.731309 "i wouild choose sprite atlases than baked spline animations" | F-MARCUS mail, ZOM-598 |
| oliver.brooks@harmonygames.co | active_sep_2025_quiet_in_oct (activity.json) | C0880U9751A/1757446973.162829 "I'm almost finishing zombie lane issues"; C0880U9751A/1757538645.309739 "at the start of level 18"; C0880U9751A/1757538880.168519 "the effects popup can be tested on the branch: [USERNAME_24960]/effects-popup" | F-OLIVER mails, ZOM-587 |
| owen.baker@harmonygames.co | active_sep_2025_quiet_in_oct (activity.json) | no short post in the two channels read; author's mail shape kept sparse | F-OWEN mails, ZOM-590 |
| samuel.turner@harmonygames.co | active_sep_2025_quiet_in_oct (activity.json) | C0880U9751A/1756923723.288489 "I will take a look"; C0880U9751A/1756924272.867929 "Currently, only 2 are loaded. What's the name of the other pack?"; C0880U9751A/1756927996.690299 "Is '[USERNAME_42313]' the name of the pack that is missing?" | F-SAMUEL mails, ZOM-593 |
| calvin.price@harmonygames.co | active_sep_2025_quiet_in_oct (activity.json) | C0880U9751A/1754616568.936979 "Okay sure.. we can use the same track and try to extend it or can try a new one as well. Let me do some test"; C0880U9751A/1754633160.681069 "There're 2 proposal I currently have.. not sure if that's the current mood, but let me know.. I'm creating 2 builds for them in game"; C0880U9751A/1754635562.126829 "I also tried lowering a little bit the VFX in game on those builds.. it sounded too loud" | F-CALVIN mails, ZOM-596 |
| martin.walsh@harmonygames.co | active_sep_2025_quiet_in_oct (activity.json) | C0880U9751A/1755187217.442559 "Yes I started to do something..."; C08R27X0EAH/1754571465.718649 "The number of the level after 100 is to big we need to fit it in the bin like this:"; C08R27X0EAH/1755515274.301499 "It's 1676 Normal" | F-MARTIN mail, ZOM-626 |
| douglas@harmonygames.co | active_sep_2025_quiet_in_oct (activity.json) | C0880U9751A/1756937991.025709 "yeah, hardcoded in the server configuration"; C0880U9751A/1754497182.330999 "I’m back, checking the bots’ configuration right now"; C08R27X0EAH/1757207354.615309 "Solved, try again please" | F-DOUGLAS mail, ZOM-625 |
| frederick.stone@harmonygames.co | active_sep_2025_quiet_in_oct (activity.json) | no short post sampled in the two channels read; co-founder, form mail kept short like the other hosts' | Frederick Stone form mail (2025-09-30T09:22:05Z), ZOM-640..ZOM-647 Docs |

GitHub speaker CodeRabbit (PERSON_6026_GITHUB_USERNAME, I07) is a bot, named by content (SC-50); it is not in activity.json. Posting hours: Leonard's ask at 21:10Z and card at 16:52Z sit in his afternoon band; Claire's mail at 10:02Z is morning in Turkey; rev7 adds Douglas's notes Docs dated Sun Sep 28 (the Sat Sep 27 sessions, written up the next morning) and moves his form mail to Mon Sep 29; no mail or Slack record falls on Sep 27 or 28. Julia and Brian write Turkish together in D076RBM29JS, which is why K4 is Turkish. Comment line `on a iPhone 15` keeps Julia's second-language slip; it is voice, not a typing defect to fix.

## 1.D Keyword

Base hits through `hg.py search search-many` (limit 5 per query, scoped: slack messages/*/2025-0[89].json, gmail threads/*.json, data.json elsewhere). 5 means at least 5.

| Term | Base hits by service | Seeded in / reached via |
|---|---|---|
| "stability gate" | 0 | NEW TERM — introduced in f_748d26e760e54651eaa0d8, reached via C090N54TG79/1758728411.540327 |
| "audience read" | 0 | NEW TERM — introduced in f_a087f049d271e9aa9f567f and 68dc0acf1815df76ed9b887d, reached via the ask C090N54TG79/1759266627.418203 |
| "Kadıköy ekibi" | 0 | NEW TERM — introduced in f_524278b67bfa30dde78699 and D076RBM29JS/1758659012.418207, reached via the notes Docs |
| "1943" | slack 5, gmail 5, gdocs 5, linear 5, github 5, trello 4, gcal 1, gslides 1 | C090N54TG79/1758819934.612483 and 10 notes Docs, f_4ceb107c67c8348b1df02b onward; base job at C05433XK267/1758575557.575349 |
| "no phone in the loop" | 0 | NEW TERM — introduced in harmonygames-Games/match3d#476#rc_27, reached via f_748d26e760e54651eaa0d8 |
| "Vision Bot" | slack 5, gmail 5, gdocs 3, github 5, gslides 2 | ZOM-567; base C05433XK267/1758803475.436309 |
| "friend session" | 0 | NEW TERM — introduced in ZOM-568 titles and f_748d26e760e54651eaa0d8, reached via f_43bc35baf77fd59f4e57b8 |
| "a small thing from Friday" | 0 | NEW TERM — introduced in julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>, reached via a listing of Julia's mail |
| "never went through a store" | 0 | NEW TERM — introduced in C090N54TG79/1758819934.612483 and f_748d26e760e54651eaa0d8, reached via thread replies under C090N54TG79/1758581651.167799 |
| "install-weighted" | 0 | NEW TERM — introduced in C090N54TG79/1759167008.881274, reached via the ask C090N54TG79/1759266627.418203 |
| "re-run note" | 0 | NEW TERM — introduced in D05GU6L0XFH/1758913471.205816, reached via the ask's delegation to Robert |
| "Friday at Claire" | 0 | NEW TERM — introduced in evt_da65644831bc088267263d, reached via Julia's calendar |

## 1.E Persona reach

| Record | Class | Path | Mark |
|---|---|---|---|
| C090N54TG79/1758517286.431379 | slack | Julia is a member | LB |
| 12b40a5b7cc18f7c9fe2d0a9e0e929b4 | slack | Julia is a member | LB |
| 4bd8937a7616a1ba2d6e6151ffc3a492 | slack | Julia is a member | LB |
| e72083b249987542a134098010edd305 | slack | Julia is a member | LB |
| f_a087f049d271e9aa9f567f | drive family | owner or shared_with includes Julia | LB |
| 2c84150a541063a6138e2f5a0cff9f33 | slack | Julia is a member | LB |
| f_748d26e760e54651eaa0d8 | drive family | owner or shared_with includes Julia | LB |
| f_c691d577b8f837eb4f9eaa | drive family | owner or shared_with includes Julia | LB |
| f_43bc35baf77fd59f4e57b8 | drive family | owner or shared_with includes Julia | LB |
| 167dc58affb9902420038f71d0f5af28 | slack | Julia is a member | LB |
| julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com> | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/1843954918097449014 | gmail | Julia's mailbox copy | LB |
| 7b38bd6429ce0f189456ac72af02f210 | slack | Julia is a member | LB |
| 2ca968ace3e14d1a34c535f8a5c0cd6e | slack | Julia is a member | LB |
| d_8140f09bf9f1b94cb8ee2d | drive family | owner or shared_with includes Julia | LB |
| C05433XK267/1758803475.436309 | slack | Julia is a member | LB |
| julia.lawson@harmonygames.co/<CAefcc9dd45170efad4834318d398795bc1db8@mail.gmail.com> | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com> | gmail | Julia's mailbox copy | LB |
| evt_da65644831bc088267263d | gcal | Julia's calendar copy | LB |
| f_524278b67bfa30dde78699 | drive family | owner or shared_with includes Julia | LB |
| 246d6f4a90620e5dafbb06068f450e46 | slack | Julia is a member | LB |
| julia.lawson@harmonygames.co/<CA01dc2d92371c7bfa63e451026f81fffed801@mail.gmail.com> | gmail | Julia's mailbox copy | LB |
| d7122186e361aa99778c65cb1502759d | slack | Julia is a member | LB |
| f_4e21b203a62910bdae0353 | drive family | owner or shared_with includes Julia | LB |
| C090N54TG79/1759176983.189479 | slack | Julia is a member | LB |
| C090N54TG79/1759178344.878219 | slack | Julia is a member | LB |
| C090N54TG79/1759171957.791499 | slack | Julia is a member | LB |
| julia.lawson@harmonygames.co/<CA8db5b364a9d7d3c1946e722aed490d591476@mail.gmail.com> | gmail | Julia's mailbox copy | LB |
| C08R27X0EAH/1758420497.482989 | slack | Julia is a member | LB |
| f_4ceb107c67c8348b1df02b | drive family | owner or shared_with includes Julia | LB |
| f_b66d5288a6d3ca9d4d03b6 | drive family | owner or shared_with includes Julia | LB |
| f_8dab41c358ba484acad83d | drive family | owner or shared_with includes Julia | LB |
| f_abf945213ee8762fbdc083 | drive family | owner or shared_with includes Julia | LB |
| f_36b61fd6f9ef6ec45cf759 | drive family | owner or shared_with includes Julia | LB |
| f_548e4061239f8bbb1ebef1 | drive family | owner or shared_with includes Julia | LB |
| f_3ff040d3a2e345719d4a70 | drive family | owner or shared_with includes Julia | LB |
| f_70e9bf3f18b32fbce7c3d0 | drive family | owner or shared_with includes Julia | LB |
| f_cff26f47141203716f669b | drive family | owner or shared_with includes Julia | LB |
| f_b96fd720b7d4010291329c | drive family | owner or shared_with includes Julia | LB |
| f_f575437ac7c498de7e1db9 | drive family | owner or shared_with includes Julia | LB |
| f_739d61e4b5cb2ed69db3d5 | drive family | owner or shared_with includes Julia | LB |
| f_50d49b0baf64a424fb73a7 | drive family | owner or shared_with includes Julia | LB |
| f_fca92e85c34b7b0d6f950b | drive family | owner or shared_with includes Julia | LB |
| f_d4ac4049ba1892fd91a3bd | drive family | owner or shared_with includes Julia | LB |
| f_28dcffa96acbd33e38ad20 | drive family | owner or shared_with includes Julia | LB |
| f_69208de7d381dc75193b14 | drive family | owner or shared_with includes Julia | LB |
| f_1bccd7e487171e17d051a5 | drive family | owner or shared_with includes Julia | LB |
| f_860c5fa834dda962164827 | drive family | owner or shared_with includes Julia | LB |
| f_cfbab45acc997b0917321e | drive family | owner or shared_with includes Julia | LB |
| f_b00473df1ed377c7ea0a03 | drive family | owner or shared_with includes Julia | LB |
| f_f96134888258f49bf9b411 | drive family | owner or shared_with includes Julia | LB |
| f_7907038d6d8ec99a11f01b | drive family | owner or shared_with includes Julia | LB |
| f_a27c70f8af81a5cfe57b53 | drive family | owner or shared_with includes Julia | LB |
| f_55f2f152df34be6a2ea5d6 | drive family | owner or shared_with includes Julia | LB |
| f_a7950c7698ff9b933a6a7b | drive family | owner or shared_with includes Julia | LB |
| f_a4258d0113946c326f52d3 | drive family | owner or shared_with includes Julia | LB |
| f_de4b874824c91335dfcb67 | drive family | owner or shared_with includes Julia | LB |
| f_75fe047f2040b34355f80a | drive family | owner or shared_with includes Julia | LB |
| f_ffaa152d5c62e39d22cf94 | drive family | owner or shared_with includes Julia | LB |
| f_d9ac7d60efdb8fe313bb6c | drive family | owner or shared_with includes Julia | LB |
| f_e0843c039ea62e1a61179e | drive family | owner or shared_with includes Julia | LB |
| f_f44fee2ed41dd0b0311f41 | drive family | owner or shared_with includes Julia | LB |
| f_4da421425634258e986f3c | drive family | owner or shared_with includes Julia | LB |
| f_6b1f637c9012a167e0f466 | drive family | owner or shared_with includes Julia | LB |
| f_e8018f6e1a4a46020dd321 | drive family | owner or shared_with includes Julia | LB |
| f_156ca006436f0ecac0ccec | drive family | owner or shared_with includes Julia | LB |
| f_6996d570d484f6b4c0f989 | drive family | owner or shared_with includes Julia | LB |
| f_69dc1cbd43ec586d7db4d9 | drive family | owner or shared_with includes Julia | LB |
| f_75130b3e7a11db61a4f6e4 | drive family | owner or shared_with includes Julia | LB |
| f_ef202456330445c2745977 | drive family | owner or shared_with includes Julia | LB |
| f_e295aa601d92bf76146caf | drive family | owner or shared_with includes Julia | LB |
| f_898157c507a362a053135a | drive family | owner or shared_with includes Julia | LB |
| f_15e5a2e226ab3e8994c970 | drive family | owner or shared_with includes Julia | LB |
| f_fbbd9f849a298efec6f7ae | drive family | owner or shared_with includes Julia | LB |
| f_43d2aee7be6a4c16d9ee95 | drive family | owner or shared_with includes Julia | LB |
| f_18a8a68476130a03866485 | drive family | owner or shared_with includes Julia | LB |
| f_61c51adfb98b4dfa709abc | drive family | owner or shared_with includes Julia | LB |
| f_24937bdfc5070d08168595 | drive family | owner or shared_with includes Julia | LB |
| f_de36d4d3f886c05f52dc3f | drive family | owner or shared_with includes Julia | LB |
| f_232c00349f8ad72acd9952 | drive family | owner or shared_with includes Julia | LB |
| f_2c58c7b8fa72b1c6312ce1 | drive family | owner or shared_with includes Julia | LB |
| f_f8712b72a8f7ba2a3eede9 | drive family | owner or shared_with includes Julia | LB |
| f_0ad31b94b4472285773483 | drive family | owner or shared_with includes Julia | LB |
| f_8019f063eeae3d9c721975 | drive family | owner or shared_with includes Julia | LB |
| f_33b9697009de5d63cee67a | drive family | owner or shared_with includes Julia | LB |
| f_2060ffa9cdcfca3b45edd1 | drive family | owner or shared_with includes Julia | LB |
| f_69e935f38bc4f701a82307 | drive family | owner or shared_with includes Julia | LB |
| f_87cdeaa9f63796916b71eb | drive family | owner or shared_with includes Julia | LB |
| julia.lawson@harmonygames.co/<CAbd808e99ae075a1768fb68e9b6520d133fab@mail.gmail.com> | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/<CA44aaa5cd5c2d0378119d16b5250dd63f309a@mail.gmail.com> | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/<CA748f9425b26f35f255ea9bf80873b2bed8a4@mail.gmail.com> | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/<CA0bc4f062a9faedd8054b0e0279fb82c17644@mail.gmail.com> | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/<CA5f548a065eb5efb9731cb60c737492aaf209@mail.gmail.com> | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/<CAb1c036095fc86f88066e4b0d22c5f21fe2c8@mail.gmail.com> | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/<CA02723a70e7ae56e2282af7734b7e44ef3f23@mail.gmail.com> | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/<CA48a7bbb5a0e6beec2ec9409441455990c0db@mail.gmail.com> | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/<CA51381f43e05aa46404914b984a5820296e26@mail.gmail.com> | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/<CA5c7622ee78a0405af6df08f42ed0e35aedd8@mail.gmail.com> | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/<CA60103ff719e6305401dd968c8f2f55f8db09@mail.gmail.com> | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/<CA6e2936ce3ea7f3cad66b7b0d1cac0e913b05@mail.gmail.com> | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/<CA14bc4b41e4b7d4884c51819b961e5ebbc954@mail.gmail.com> | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/1844094591565886237 | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/1844139735908739966 | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/1844151965450762802 | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/1844226064122813574 | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/1844245860188980242 | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/1844255215584092313 | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/1844314577567776575 | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/1844324114366762178 | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/1844334980760275863 | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/1844361729934100115 | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/1844589014025156069 | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/1844598530900183157 | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/1844605722034776031 | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/1844612217962947730 | gmail | Julia's mailbox copy | LB |
| julia.lawson@harmonygames.co/1844675467018824635 | gmail | Julia's mailbox copy | LB |
| b07f1e10112b7661e1d8eaf3b127227f | slack | Julia is a member | LB |
| 4500761ad805eeda66272ec37c91a8ef | slack | Julia is a member | LB |
| D076RBM29JS/1758658884.207315 | slack | Julia is a member | LB |
| C093LEZGF6J/1759258475.735779 | probe | UNVERIFIED-OK: Julia is not a member of the public channel; the mirror only copies the comment. | alternate_evidence_ids: harmonygames-Games/match3d#476, C05433XK267/1758803475.436309 |
| D04UP2L3E3S/1758515667.845849 | probe | DENIAL-INTENDED: Leonard and Robert DM, grounding for the age band only. | alternate_evidence_ids: C090N54TG79/1758517286.431379 |
| C07C2866011 | probe | DENIAL-INTENDED: #executives copy of the note, unused. | alternate_evidence_ids: C090N54TG79/1758517286.431379 |
| leonard.hayes@harmonygames.co/1843922088670958384 | probe | DENIAL-INTENDED: vendor mail in Leonard's mailbox; the seeded forward carries it. | alternate_evidence_ids: C090N54TG79/1758517286.431379 |

GitHub, Linear, Trello, Contacts, Snowflake and Confluence are unscoped, so `harmonygames-Games/match3d#476`, `ZOM-559` and the rest need no check. The 17 sender mailbox copies, Claire's calendar copy and the #zombie-prs mirrors are companions, not evidence, and Julia need not reach them.

`python3 Task_Authoring/tools/persona_view.py check-sql julia_lawson Task_Authoring/task_inputs/01_Universe_Inject.sql --load-bearing Task_Authoring/task_inputs/Working_Files/plan/load_bearing.txt` (verbatim):

```text
CHECK-SQL as julia_lawson <julia.lawson@harmonygames.co>
[YES LB] L3 gdrive.drive_files insert f_748d26e760e54651eaa0d8 - file is shared with the persona (shared_with_emails)
[YES LB] L5 gdrive.drive_files insert f_c691d577b8f837eb4f9eaa - persona owns the file
[YES LB] L7 gdrive.drive_files insert f_a087f049d271e9aa9f567f - persona owns the file
[YES LB] L9 gdrive.drive_files insert f_43bc35baf77fd59f4e57b8 - persona owns the file
[YES LB] L11 gdrive.drive_files insert f_4e21b203a62910bdae0353 - file is shared with the persona (shared_with_emails)
[YES LB] L13 gdrive.drive_files insert f_524278b67bfa30dde78699 - file is shared with the persona (shared_with_emails)
[YES LB] L15 gdrive.drive_files insert f_b66d5288a6d3ca9d4d03b6 - file is shared with the persona (shared_with_emails)
[YES LB] L17 gdrive.drive_files insert f_8dab41c358ba484acad83d - file is shared with the persona (shared_with_emails)
[YES LB] L19 gdrive.drive_files insert f_abf945213ee8762fbdc083 - file is shared with the persona (shared_with_emails)
[YES LB] L21 gdrive.drive_files insert f_36b61fd6f9ef6ec45cf759 - file is shared with the persona (shared_with_emails)
[YES LB] L23 gdrive.drive_files insert f_548e4061239f8bbb1ebef1 - file is shared with the persona (shared_with_emails)
[YES LB] L25 gdrive.drive_files insert f_3ff040d3a2e345719d4a70 - file is shared with the persona (shared_with_emails)
[YES LB] L27 gdrive.drive_files insert f_70e9bf3f18b32fbce7c3d0 - file is shared with the persona (shared_with_emails)
[YES LB] L29 gdrive.drive_files insert f_cff26f47141203716f669b - file is shared with the persona (shared_with_emails)
[YES LB] L31 gdrive.drive_files insert f_4ceb107c67c8348b1df02b - file is shared with the persona (shared_with_emails)
[YES LB] L33 gdrive.drive_files insert f_b96fd720b7d4010291329c - file is shared with the persona (shared_with_emails)
[YES LB] L35 gdrive.drive_files insert f_f575437ac7c498de7e1db9 - file is shared with the persona (shared_with_emails)
[YES LB] L37 gdrive.drive_files insert f_739d61e4b5cb2ed69db3d5 - file is shared with the persona (shared_with_emails)
[YES LB] L39 gdrive.drive_files insert f_50d49b0baf64a424fb73a7 - file is shared with the persona (shared_with_emails)
[YES LB] L41 gdrive.drive_files insert f_fca92e85c34b7b0d6f950b - file is shared with the persona (shared_with_emails)
[YES LB] L43 gdrive.drive_files insert f_d4ac4049ba1892fd91a3bd - file is shared with the persona (shared_with_emails)
[YES LB] L45 gdrive.drive_files insert f_28dcffa96acbd33e38ad20 - file is shared with the persona (shared_with_emails)
[YES LB] L47 gdrive.drive_files insert f_69208de7d381dc75193b14 - file is shared with the persona (shared_with_emails)
[YES LB] L49 gdrive.drive_files insert f_1bccd7e487171e17d051a5 - file is shared with the persona (shared_with_emails)
[YES LB] L51 gdrive.drive_files insert f_860c5fa834dda962164827 - file is shared with the persona (shared_with_emails)
[YES LB] L53 gdrive.drive_files insert f_cfbab45acc997b0917321e - file is shared with the persona (shared_with_emails)
[YES LB] L55 gdrive.drive_files insert f_b00473df1ed377c7ea0a03 - file is shared with the persona (shared_with_emails)
[YES LB] L57 gdrive.drive_files insert f_f96134888258f49bf9b411 - file is shared with the persona (shared_with_emails)
[YES LB] L59 gdrive.drive_files insert f_7907038d6d8ec99a11f01b - file is shared with the persona (shared_with_emails)
[YES LB] L61 gdrive.drive_files insert f_a27c70f8af81a5cfe57b53 - file is shared with the persona (shared_with_emails)
[YES LB] L63 gdrive.drive_files insert f_55f2f152df34be6a2ea5d6 - file is shared with the persona (shared_with_emails)
[YES LB] L65 gdrive.drive_files insert f_a7950c7698ff9b933a6a7b - file is shared with the persona (shared_with_emails)
[YES LB] L67 gdrive.drive_files insert f_a4258d0113946c326f52d3 - file is shared with the persona (shared_with_emails)
[YES LB] L69 gdrive.drive_files insert f_de4b874824c91335dfcb67 - file is shared with the persona (shared_with_emails)
[YES LB] L71 gdrive.drive_files insert f_75fe047f2040b34355f80a - file is shared with the persona (shared_with_emails)
[YES LB] L73 gdrive.drive_files insert f_ffaa152d5c62e39d22cf94 - file is shared with the persona (shared_with_emails)
[YES LB] L75 gdrive.drive_files insert f_d9ac7d60efdb8fe313bb6c - file is shared with the persona (shared_with_emails)
[YES LB] L77 gdrive.drive_files insert f_e0843c039ea62e1a61179e - file is shared with the persona (shared_with_emails)
[YES LB] L79 gdrive.drive_files insert f_f44fee2ed41dd0b0311f41 - file is shared with the persona (shared_with_emails)
[YES LB] L81 gdrive.drive_files insert f_4da421425634258e986f3c - file is shared with the persona (shared_with_emails)
[YES LB] L83 gdrive.drive_files insert f_6b1f637c9012a167e0f466 - file is shared with the persona (shared_with_emails)
[YES LB] L85 gdrive.drive_files insert f_e8018f6e1a4a46020dd321 - file is shared with the persona (shared_with_emails)
[YES LB] L87 gdrive.drive_files insert f_156ca006436f0ecac0ccec - file is shared with the persona (shared_with_emails)
[YES LB] L89 gdrive.drive_files insert f_6996d570d484f6b4c0f989 - file is shared with the persona (shared_with_emails)
[YES LB] L91 gdrive.drive_files insert f_69dc1cbd43ec586d7db4d9 - file is shared with the persona (shared_with_emails)
[YES LB] L93 gdrive.drive_files insert f_75130b3e7a11db61a4f6e4 - file is shared with the persona (shared_with_emails)
[YES LB] L95 gdrive.drive_files insert f_ef202456330445c2745977 - file is shared with the persona (shared_with_emails)
[YES LB] L97 gdrive.drive_files insert f_e295aa601d92bf76146caf - file is shared with the persona (shared_with_emails)
[YES LB] L99 gdrive.drive_files insert f_898157c507a362a053135a - file is shared with the persona (shared_with_emails)
[YES LB] L101 gdrive.drive_files insert f_15e5a2e226ab3e8994c970 - file is shared with the persona (shared_with_emails)
[YES LB] L103 gdrive.drive_files insert f_fbbd9f849a298efec6f7ae - file is shared with the persona (shared_with_emails)
[YES LB] L105 gdrive.drive_files insert f_43d2aee7be6a4c16d9ee95 - file is shared with the persona (shared_with_emails)
[YES LB] L107 gdrive.drive_files insert f_18a8a68476130a03866485 - file is shared with the persona (shared_with_emails)
[YES LB] L109 gdrive.drive_files insert f_61c51adfb98b4dfa709abc - file is shared with the persona (shared_with_emails)
[YES LB] L111 gdrive.drive_files insert f_24937bdfc5070d08168595 - file is shared with the persona (shared_with_emails)
[YES LB] L113 gdrive.drive_files insert f_de36d4d3f886c05f52dc3f - file is shared with the persona (shared_with_emails)
[YES LB] L115 gdrive.drive_files insert f_232c00349f8ad72acd9952 - file is shared with the persona (shared_with_emails)
[YES LB] L117 gdrive.drive_files insert f_2c58c7b8fa72b1c6312ce1 - file is shared with the persona (shared_with_emails)
[YES LB] L119 gdrive.drive_files insert f_f8712b72a8f7ba2a3eede9 - file is shared with the persona (shared_with_emails)
[YES LB] L121 gdrive.drive_files insert f_0ad31b94b4472285773483 - file is shared with the persona (shared_with_emails)
[YES LB] L123 gdrive.drive_files insert f_8019f063eeae3d9c721975 - file is shared with the persona (shared_with_emails)
[YES LB] L125 gdrive.drive_files insert f_33b9697009de5d63cee67a - file is shared with the persona (shared_with_emails)
[YES LB] L127 gdrive.drive_files insert f_2060ffa9cdcfca3b45edd1 - file is shared with the persona (shared_with_emails)
[YES LB] L129 gdrive.drive_files insert f_69e935f38bc4f701a82307 - file is shared with the persona (shared_with_emails)
[YES LB] L131 gdrive.drive_files insert f_87cdeaa9f63796916b71eb - file is shared with the persona (shared_with_emails)
[YES LB] L133 gdrive.drive_files insert f_fedafbc8ff188924c11cdf - file is shared with the persona (shared_with_emails)
[YES LB] L135 gdrive.drive_files insert f_9f64dea295334aaeb23d3f - file is shared with the persona (shared_with_emails)
[YES LB] L137 gdrive.drive_files insert f_08f43656551552686b74df - file is shared with the persona (shared_with_emails)
[YES LB] L139 gdrive.drive_files insert f_178b99f1f6352dc03931ad - file is shared with the persona (shared_with_emails)
[YES LB] L141 gdrive.drive_files insert f_41675dd5d215cf647b240e - file is shared with the persona (shared_with_emails)
[YES LB] L143 gdrive.drive_files insert f_95be113064416cde1e5112 - file is shared with the persona (shared_with_emails)
[YES LB] L145 gdrive.drive_files insert f_44f7b61e9d8309b8591661 - file is shared with the persona (shared_with_emails)
[YES LB] L147 gdrive.drive_files insert f_2146d056bca5ab4f83a715 - file is shared with the persona (shared_with_emails)
[YES LB] L149 gdrive.drive_files insert f_1c70a27482cbcc1ad91ef0 - file is shared with the persona (shared_with_emails)
[YES LB] L151 gdrive.drive_files insert f_e055f907c7c1359b39bec5 - file is shared with the persona (shared_with_emails)
[YES LB] L153 gdrive.drive_files insert f_387c0cfca799142e9b1f9e - file is shared with the persona (shared_with_emails)
[YES LB] L155 gdrive.drive_files insert f_cc21fd5ed63d1475930088 - file is shared with the persona (shared_with_emails)
[YES LB] L157 gdrive.drive_files insert f_aff6380897e0155019b59e - file is shared with the persona (shared_with_emails)
[YES LB] L159 gdrive.drive_files insert f_b651ada1ece0b3633a36a8 - file is shared with the persona (shared_with_emails)
[YES LB] L161 gdrive.drive_files insert f_5e7f8e1e70b5d7b69972a0 - file is shared with the persona (shared_with_emails)
[YES LB] L163 gdrive.drive_files insert f_6d4c2688f5131f1164a74a - file is shared with the persona (shared_with_emails)
[YES LB] L165 gdrive.drive_files insert f_9a47a30e9b8253e094a5de - file is shared with the persona (shared_with_emails)
[YES LB] L167 gdrive.drive_files insert f_ba6a734ddf36318e9bb3f3 - file is shared with the persona (shared_with_emails)
[YES LB] L169 gdrive.drive_files insert f_84973bcd502c4a28c59f95 - file is shared with the persona (shared_with_emails)
[YES LB] L171 gdrive.drive_files insert f_65531765c1a7ccd4d4561a - file is shared with the persona (shared_with_emails)
[YES LB] L173 gdocs.docs_documents insert f_748d26e760e54651eaa0d8 - file is shared with the persona (shared_with_emails)
[YES LB] L175 gdocs.docs_documents insert f_c691d577b8f837eb4f9eaa - persona owns the file
[YES LB] L177 gdocs.docs_documents insert f_524278b67bfa30dde78699 - file is shared with the persona (shared_with_emails)
[YES LB] L179 gdocs.docs_documents insert f_b66d5288a6d3ca9d4d03b6 - file is shared with the persona (shared_with_emails)
[YES LB] L181 gdocs.docs_documents insert f_8dab41c358ba484acad83d - file is shared with the persona (shared_with_emails)
[YES LB] L183 gdocs.docs_documents insert f_abf945213ee8762fbdc083 - file is shared with the persona (shared_with_emails)
[YES LB] L185 gdocs.docs_documents insert f_36b61fd6f9ef6ec45cf759 - file is shared with the persona (shared_with_emails)
[YES LB] L187 gdocs.docs_documents insert f_548e4061239f8bbb1ebef1 - file is shared with the persona (shared_with_emails)
[YES LB] L189 gdocs.docs_documents insert f_3ff040d3a2e345719d4a70 - file is shared with the persona (shared_with_emails)
[YES LB] L191 gdocs.docs_documents insert f_70e9bf3f18b32fbce7c3d0 - file is shared with the persona (shared_with_emails)
[YES LB] L193 gdocs.docs_documents insert f_cff26f47141203716f669b - file is shared with the persona (shared_with_emails)
[YES LB] L195 gdocs.docs_documents insert f_4ceb107c67c8348b1df02b - file is shared with the persona (shared_with_emails)
[YES LB] L197 gdocs.docs_documents insert f_b96fd720b7d4010291329c - file is shared with the persona (shared_with_emails)
[YES LB] L199 gdocs.docs_documents insert f_f575437ac7c498de7e1db9 - file is shared with the persona (shared_with_emails)
[YES LB] L201 gdocs.docs_documents insert f_739d61e4b5cb2ed69db3d5 - file is shared with the persona (shared_with_emails)
[YES LB] L203 gdocs.docs_documents insert f_50d49b0baf64a424fb73a7 - file is shared with the persona (shared_with_emails)
[YES LB] L205 gdocs.docs_documents insert f_fca92e85c34b7b0d6f950b - file is shared with the persona (shared_with_emails)
[YES LB] L207 gdocs.docs_documents insert f_d4ac4049ba1892fd91a3bd - file is shared with the persona (shared_with_emails)
[YES LB] L209 gdocs.docs_documents insert f_28dcffa96acbd33e38ad20 - file is shared with the persona (shared_with_emails)
[YES LB] L211 gdocs.docs_documents insert f_69208de7d381dc75193b14 - file is shared with the persona (shared_with_emails)
[YES LB] L213 gdocs.docs_documents insert f_1bccd7e487171e17d051a5 - file is shared with the persona (shared_with_emails)
[YES LB] L215 gdocs.docs_documents insert f_860c5fa834dda962164827 - file is shared with the persona (shared_with_emails)
[YES LB] L217 gdocs.docs_documents insert f_cfbab45acc997b0917321e - file is shared with the persona (shared_with_emails)
[YES LB] L219 gdocs.docs_documents insert f_b00473df1ed377c7ea0a03 - file is shared with the persona (shared_with_emails)
[YES LB] L221 gdocs.docs_documents insert f_f96134888258f49bf9b411 - file is shared with the persona (shared_with_emails)
[YES LB] L223 gdocs.docs_documents insert f_7907038d6d8ec99a11f01b - file is shared with the persona (shared_with_emails)
[YES LB] L225 gdocs.docs_documents insert f_a27c70f8af81a5cfe57b53 - file is shared with the persona (shared_with_emails)
[YES LB] L227 gdocs.docs_documents insert f_55f2f152df34be6a2ea5d6 - file is shared with the persona (shared_with_emails)
[YES LB] L229 gdocs.docs_documents insert f_a7950c7698ff9b933a6a7b - file is shared with the persona (shared_with_emails)
[YES LB] L231 gdocs.docs_documents insert f_a4258d0113946c326f52d3 - file is shared with the persona (shared_with_emails)
[YES LB] L233 gdocs.docs_documents insert f_de4b874824c91335dfcb67 - file is shared with the persona (shared_with_emails)
[YES LB] L235 gdocs.docs_documents insert f_75fe047f2040b34355f80a - file is shared with the persona (shared_with_emails)
[YES LB] L237 gdocs.docs_documents insert f_ffaa152d5c62e39d22cf94 - file is shared with the persona (shared_with_emails)
[YES LB] L239 gdocs.docs_documents insert f_d9ac7d60efdb8fe313bb6c - file is shared with the persona (shared_with_emails)
[YES LB] L241 gdocs.docs_documents insert f_e0843c039ea62e1a61179e - file is shared with the persona (shared_with_emails)
[YES LB] L243 gdocs.docs_documents insert f_f44fee2ed41dd0b0311f41 - file is shared with the persona (shared_with_emails)
[YES LB] L245 gdocs.docs_documents insert f_4da421425634258e986f3c - file is shared with the persona (shared_with_emails)
[YES LB] L247 gdocs.docs_documents insert f_6b1f637c9012a167e0f466 - file is shared with the persona (shared_with_emails)
[YES LB] L249 gdocs.docs_documents insert f_e8018f6e1a4a46020dd321 - file is shared with the persona (shared_with_emails)
[YES LB] L251 gdocs.docs_documents insert f_156ca006436f0ecac0ccec - file is shared with the persona (shared_with_emails)
[YES LB] L253 gdocs.docs_documents insert f_6996d570d484f6b4c0f989 - file is shared with the persona (shared_with_emails)
[YES LB] L255 gdocs.docs_documents insert f_69dc1cbd43ec586d7db4d9 - file is shared with the persona (shared_with_emails)
[YES LB] L257 gdocs.docs_documents insert f_75130b3e7a11db61a4f6e4 - file is shared with the persona (shared_with_emails)
[YES LB] L259 gdocs.docs_documents insert f_ef202456330445c2745977 - file is shared with the persona (shared_with_emails)
[YES LB] L261 gdocs.docs_documents insert f_e295aa601d92bf76146caf - file is shared with the persona (shared_with_emails)
[YES LB] L263 gdocs.docs_documents insert f_898157c507a362a053135a - file is shared with the persona (shared_with_emails)
[YES LB] L265 gdocs.docs_documents insert f_15e5a2e226ab3e8994c970 - file is shared with the persona (shared_with_emails)
[YES LB] L267 gdocs.docs_documents insert f_fbbd9f849a298efec6f7ae - file is shared with the persona (shared_with_emails)
[YES LB] L269 gdocs.docs_documents insert f_43d2aee7be6a4c16d9ee95 - file is shared with the persona (shared_with_emails)
[YES LB] L271 gdocs.docs_documents insert f_18a8a68476130a03866485 - file is shared with the persona (shared_with_emails)
[YES LB] L273 gdocs.docs_documents insert f_61c51adfb98b4dfa709abc - file is shared with the persona (shared_with_emails)
[YES LB] L275 gdocs.docs_documents insert f_24937bdfc5070d08168595 - file is shared with the persona (shared_with_emails)
[YES LB] L277 gdocs.docs_documents insert f_de36d4d3f886c05f52dc3f - file is shared with the persona (shared_with_emails)
[YES LB] L279 gdocs.docs_documents insert f_232c00349f8ad72acd9952 - file is shared with the persona (shared_with_emails)
[YES LB] L281 gdocs.docs_documents insert f_2c58c7b8fa72b1c6312ce1 - file is shared with the persona (shared_with_emails)
[YES LB] L283 gdocs.docs_documents insert f_f8712b72a8f7ba2a3eede9 - file is shared with the persona (shared_with_emails)
[YES LB] L285 gdocs.docs_documents insert f_0ad31b94b4472285773483 - file is shared with the persona (shared_with_emails)
[YES LB] L287 gdocs.docs_documents insert f_8019f063eeae3d9c721975 - file is shared with the persona (shared_with_emails)
[YES LB] L289 gdocs.docs_documents insert f_33b9697009de5d63cee67a - file is shared with the persona (shared_with_emails)
[YES LB] L291 gdocs.docs_documents insert f_2060ffa9cdcfca3b45edd1 - file is shared with the persona (shared_with_emails)
[YES LB] L293 gdocs.docs_documents insert f_69e935f38bc4f701a82307 - file is shared with the persona (shared_with_emails)
[YES LB] L295 gdocs.docs_documents insert f_87cdeaa9f63796916b71eb - file is shared with the persona (shared_with_emails)
[YES LB] L297 gdocs.docs_documents insert f_fedafbc8ff188924c11cdf - file is shared with the persona (shared_with_emails)
[YES LB] L299 gdocs.docs_documents insert f_9f64dea295334aaeb23d3f - file is shared with the persona (shared_with_emails)
[YES LB] L301 gdocs.docs_documents insert f_08f43656551552686b74df - file is shared with the persona (shared_with_emails)
[YES LB] L303 gdocs.docs_documents insert f_178b99f1f6352dc03931ad - file is shared with the persona (shared_with_emails)
[YES LB] L305 gdocs.docs_documents insert f_41675dd5d215cf647b240e - file is shared with the persona (shared_with_emails)
[YES LB] L307 gdocs.docs_documents insert f_95be113064416cde1e5112 - file is shared with the persona (shared_with_emails)
[YES LB] L309 gdocs.docs_documents insert f_44f7b61e9d8309b8591661 - file is shared with the persona (shared_with_emails)
[YES LB] L311 gdocs.docs_documents insert f_2146d056bca5ab4f83a715 - file is shared with the persona (shared_with_emails)
[YES LB] L313 gdocs.docs_documents insert f_1c70a27482cbcc1ad91ef0 - file is shared with the persona (shared_with_emails)
[YES LB] L315 gdocs.docs_documents insert f_e055f907c7c1359b39bec5 - file is shared with the persona (shared_with_emails)
[YES LB] L317 gdocs.docs_documents insert f_387c0cfca799142e9b1f9e - file is shared with the persona (shared_with_emails)
[YES LB] L319 gdocs.docs_documents insert f_cc21fd5ed63d1475930088 - file is shared with the persona (shared_with_emails)
[YES LB] L321 gdocs.docs_documents insert f_aff6380897e0155019b59e - file is shared with the persona (shared_with_emails)
[YES LB] L323 gdocs.docs_documents insert f_b651ada1ece0b3633a36a8 - file is shared with the persona (shared_with_emails)
[YES LB] L325 gdocs.docs_documents insert f_5e7f8e1e70b5d7b69972a0 - file is shared with the persona (shared_with_emails)
[YES LB] L327 gdocs.docs_documents insert f_6d4c2688f5131f1164a74a - file is shared with the persona (shared_with_emails)
[YES LB] L329 gdocs.docs_documents insert f_9a47a30e9b8253e094a5de - file is shared with the persona (shared_with_emails)
[YES LB] L331 gdocs.docs_documents insert f_ba6a734ddf36318e9bb3f3 - file is shared with the persona (shared_with_emails)
[YES LB] L333 gdocs.docs_documents insert f_84973bcd502c4a28c59f95 - file is shared with the persona (shared_with_emails)
[YES LB] L335 gdocs.docs_documents insert f_65531765c1a7ccd4d4561a - file is shared with the persona (shared_with_emails)
[YES LB] L337 gsheets.sheets_spreadsheets insert f_43bc35baf77fd59f4e57b8 - persona owns the file
[YES LB] L339 gsheets.sheets_sheets insert f_43bc35baf77fd59f4e57b8, f_43bc35baf77fd59f4e57b8#0 - persona owns the file
[YES LB] L341 gsheets.sheets_sheets insert f_43bc35baf77fd59f4e57b8, f_43bc35baf77fd59f4e57b8#1 - persona owns the file
[YES LB] L343 gsheets.sheets_spreadsheets insert f_4e21b203a62910bdae0353 - file is shared with the persona (shared_with_emails)
[YES LB] L345 gsheets.sheets_sheets insert f_4e21b203a62910bdae0353, f_4e21b203a62910bdae0353#0 - file is shared with the persona (shared_with_emails)
[YES LB] L347 gslides.slides_presentations insert f_a087f049d271e9aa9f567f - persona owns the file
[YES LB] L349 gslides.slides_pages insert f_a087f049d271e9aa9f567f, slide_d680691ee9e5 - persona owns the file
[YES LB] L351 gslides.slides_page_elements insert f_a087f049d271e9aa9f567f, el_6ddced6da136, slide_d680691ee9e5 - persona owns the file
[YES LB] L353 gslides.slides_pages insert f_a087f049d271e9aa9f567f, slide_29241137200c - persona owns the file
[YES LB] L355 gslides.slides_page_elements insert f_a087f049d271e9aa9f567f, el_18102c1d9b66, slide_29241137200c - persona owns the file
[YES LB] L357 gslides.slides_pages insert f_a087f049d271e9aa9f567f, slide_1b64c7b03a47 - persona owns the file
[YES LB] L359 gslides.slides_page_elements insert f_a087f049d271e9aa9f567f, el_5b5d50499cb5, slide_1b64c7b03a47 - persona owns the file
[YES] L361 gcal.gcal_events insert evt_960936eab424f7726db95c - persona is an attendee and holds its own copy evt_da65644831bc088267263d (same ical_uid and start) on julia.lawson@harmonygames.co
[YES LB] L363 gcal.gcal_events insert evt_da65644831bc088267263d - event is on the persona's own calendar julia.lawson@harmonygames.co
[YES LB] L365 gmail.gmail_threads insert julia.lawson@harmonygames.co/1843954918097449014 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L367 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L369 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1843954918098117383 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L371 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com>, leo - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES LB] L373 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844094591565886237 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L375 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CA01dc2d92371c7bfa63e451026f81fffed801@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L377 gmail.gmail_threads insert robert@harmonygames.co/1844094591566494759 - row is in mailbox robert@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L379 gmail.gmail_messages insert robert@harmonygames.co/<CA01dc2d92371c7bfa63e451026f81fffed801@mail.gmail.com>, robert@har - row is in mailbox robert@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES LB] L381 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844139735908739966 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L383 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CAbd808e99ae075a1768fb68e9b6520d133fab@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L385 gmail.gmail_threads insert oliver.brooks@harmonygames.co/1844139735909330734 - row is in mailbox oliver.brooks@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L387 gmail.gmail_messages insert oliver.brooks@harmonygames.co/<CAbd808e99ae075a1768fb68e9b6520d133fab@mail.gmail.com>, oli - row is in mailbox oliver.brooks@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES LB] L389 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844151965450762802 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L391 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CA44aaa5cd5c2d0378119d16b5250dd63f309a@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L393 gmail.gmail_threads insert owen.baker@harmonygames.co/1844151965451361163 - row is in mailbox owen.baker@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L395 gmail.gmail_messages insert owen.baker@harmonygames.co/<CA44aaa5cd5c2d0378119d16b5250dd63f309a@mail.gmail.com>, owen.b - row is in mailbox owen.baker@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES LB] L397 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844226064122813574 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L399 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CA748f9425b26f35f255ea9bf80873b2bed8a4@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L401 gmail.gmail_threads insert samuel.turner@harmonygames.co/1844226064123492719 - row is in mailbox samuel.turner@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L403 gmail.gmail_messages insert samuel.turner@harmonygames.co/<CA748f9425b26f35f255ea9bf80873b2bed8a4@mail.gmail.com>, sam - row is in mailbox samuel.turner@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES LB] L405 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844245860188980242 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L407 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CA0bc4f062a9faedd8054b0e0279fb82c17644@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L409 gmail.gmail_threads insert calvin.price@harmonygames.co/1844245860189680279 - row is in mailbox calvin.price@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L411 gmail.gmail_messages insert calvin.price@harmonygames.co/<CA0bc4f062a9faedd8054b0e0279fb82c17644@mail.gmail.com>, calv - row is in mailbox calvin.price@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES LB] L413 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844255215584092313 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L415 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CA5f548a065eb5efb9731cb60c737492aaf209@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L417 gmail.gmail_threads insert marcus.bennett@harmonygames.co/1844255215584474042 - row is in mailbox marcus.bennett@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L419 gmail.gmail_messages insert marcus.bennett@harmonygames.co/<CA5f548a065eb5efb9731cb60c737492aaf209@mail.gmail.com>, ma - row is in mailbox marcus.bennett@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES LB] L421 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844314577567776575 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L423 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CAb1c036095fc86f88066e4b0d22c5f21fe2c8@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L425 gmail.gmail_threads insert oliver.brooks@harmonygames.co/1844314577568386305 - row is in mailbox oliver.brooks@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L427 gmail.gmail_messages insert oliver.brooks@harmonygames.co/<CAb1c036095fc86f88066e4b0d22c5f21fe2c8@mail.gmail.com>, oli - row is in mailbox oliver.brooks@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES LB] L429 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844324114366762178 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L431 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CA02723a70e7ae56e2282af7734b7e44ef3f23@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L433 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CAab474c9390349b2f96626bafff9ff2c5f9cd@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L435 gmail.gmail_threads insert owen.baker@harmonygames.co/1844324114367028910 - row is in mailbox owen.baker@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L437 gmail.gmail_messages insert owen.baker@harmonygames.co/<CA02723a70e7ae56e2282af7734b7e44ef3f23@mail.gmail.com>, owen.b - row is in mailbox owen.baker@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L439 gmail.gmail_messages insert owen.baker@harmonygames.co/<CAab474c9390349b2f96626bafff9ff2c5f9cd@mail.gmail.com>, owen.b - row is in mailbox owen.baker@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES LB] L441 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844334980760275863 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L443 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CA48a7bbb5a0e6beec2ec9409441455990c0db@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L445 gmail.gmail_threads insert samuel.turner@harmonygames.co/1844334980760681071 - row is in mailbox samuel.turner@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L447 gmail.gmail_messages insert samuel.turner@harmonygames.co/<CA48a7bbb5a0e6beec2ec9409441455990c0db@mail.gmail.com>, sam - row is in mailbox samuel.turner@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES LB] L449 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844361729934100115 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L451 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CAefcc9dd45170efad4834318d398795bc1db8@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L453 gmail.gmail_threads insert claire.morgan@harmonygames.co/1844361729934945604 - row is in mailbox claire.morgan@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L455 gmail.gmail_messages insert claire.morgan@harmonygames.co/<CAefcc9dd45170efad4834318d398795bc1db8@mail.gmail.com>, cla - row is in mailbox claire.morgan@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES LB] L457 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844589014025156069 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L459 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CA51381f43e05aa46404914b984a5820296e26@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L461 gmail.gmail_threads insert calvin.price@harmonygames.co/1844589014025497035 - row is in mailbox calvin.price@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L463 gmail.gmail_messages insert calvin.price@harmonygames.co/<CA51381f43e05aa46404914b984a5820296e26@mail.gmail.com>, calv - row is in mailbox calvin.price@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES LB] L465 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844598530900183157 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L467 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CA5c7622ee78a0405af6df08f42ed0e35aedd8@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L469 gmail.gmail_threads insert vincent.parker@harmonygames.co/1844598530900512479 - row is in mailbox vincent.parker@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L471 gmail.gmail_messages insert vincent.parker@harmonygames.co/<CA5c7622ee78a0405af6df08f42ed0e35aedd8@mail.gmail.com>, vi - row is in mailbox vincent.parker@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES LB] L473 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844605722034776031 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L475 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CA60103ff719e6305401dd968c8f2f55f8db09@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L477 gmail.gmail_threads insert arthur.blake@harmonygames.co/1844605722035474235 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L479 gmail.gmail_messages insert arthur.blake@harmonygames.co/<CA60103ff719e6305401dd968c8f2f55f8db09@mail.gmail.com>, arth - row is in mailbox arthur.blake@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES LB] L481 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844612217962947730 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L483 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CA6e2936ce3ea7f3cad66b7b0d1cac0e913b05@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L485 gmail.gmail_threads insert douglas@harmonygames.co/1844612217963668883 - row is in mailbox douglas@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L487 gmail.gmail_messages insert douglas@harmonygames.co/<CA6e2936ce3ea7f3cad66b7b0d1cac0e913b05@mail.gmail.com>, douglas@h - row is in mailbox douglas@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES LB] L489 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844675467018824635 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L491 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CA14bc4b41e4b7d4884c51819b961e5ebbc954@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L493 gmail.gmail_threads insert martin.walsh@harmonygames.co/1844675467019380800 - row is in mailbox martin.walsh@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L495 gmail.gmail_messages insert martin.walsh@harmonygames.co/<CA14bc4b41e4b7d4884c51819b961e5ebbc954@mail.gmail.com>, mart - row is in mailbox martin.walsh@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES] L497 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844318948033312842 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L499 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CA8db5b364a9d7d3c1946e722aed490d591476@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L501 gmail.gmail_threads insert marcus.bennett@harmonygames.co/1844318948033827471 - row is in mailbox marcus.bennett@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L503 gmail.gmail_messages insert marcus.bennett@harmonygames.co/<CA8db5b364a9d7d3c1946e722aed490d591476@mail.gmail.com>, ma - row is in mailbox marcus.bennett@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES] L505 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844592159752803121 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L507 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L509 gmail.gmail_threads insert claire.morgan@harmonygames.co/1844592159753417634 - row is in mailbox claire.morgan@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L511 gmail.gmail_messages insert claire.morgan@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>, cla - row is in mailbox claire.morgan@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES] L513 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844583257342015432 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L515 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CAa9433ba36222cc3d3e09daf60e654acc2f25@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L517 gmail.gmail_threads insert douglas@harmonygames.co/1844583257342535681 - row is in mailbox douglas@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L519 gmail.gmail_messages insert douglas@harmonygames.co/<CAa9433ba36222cc3d3e09daf60e654acc2f25@mail.gmail.com>, douglas@h - row is in mailbox douglas@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES] L521 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844680196096558448 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES LB] L523 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CAc7a9836dd19cd248a2170bad024a9566f61f@mail.gmail.com>, juli - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L525 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844680196096555931 - row is in mailbox frederick.stone@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L527 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAc7a9836dd19cd248a2170bad024a9566f61f@mail.gmail.com>, f - row is in mailbox frederick.stone@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES LB] L862 slack.slack_messages insert 4bd8937a7616a1ba2d6e6151ffc3a492, C090N54TG79/1758553214.330914 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] L864 slack.slack_messages insert 12b40a5b7cc18f7c9fe2d0a9e0e929b4, C090N54TG79/1758554405.774120 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] L866 slack.slack_messages insert 4500761ad805eeda66272ec37c91a8ef, C0880U9751A/1758555040.262718 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-match3d
[YES LB] L868 slack.slack_messages insert 5e2947d9447f26c28b465f4fd64254d3, D076RBM29JS/1758658884.207315 - persona EMPLOYEE_0005_SLACK_ID is in members of im D076RBM29JS
[YES LB] L870 slack.slack_messages insert 246d6f4a90620e5dafbb06068f450e46, D076RBM29JS/1758659012.418207 - persona EMPLOYEE_0005_SLACK_ID is in members of im D076RBM29JS
[YES LB] L872 slack.slack_messages insert 2c84150a541063a6138e2f5a0cff9f33, C090N54TG79/1758728411.540327 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] L874 slack.slack_messages insert 7b38bd6429ce0f189456ac72af02f210, C090N54TG79/1758729919.603185 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] L876 slack.slack_messages insert e72083b249987542a134098010edd305, C090N54TG79/1758733233.117446 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] L878 slack.slack_messages insert ba19de7863a540175f2aeadc12916fa6, C090N54TG79/1758818538.552913 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] L880 slack.slack_messages insert d7122186e361aa99778c65cb1502759d, C090N54TG79/1758819934.612483 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] L882 slack.slack_messages insert 167dc58affb9902420038f71d0f5af28, D05GU6L0XFH/1758913471.205816 - persona EMPLOYEE_0005_SLACK_ID is in members of im D05GU6L0XFH
[YES LB] L884 slack.slack_messages insert 2ca968ace3e14d1a34c535f8a5c0cd6e, C090N54TG79/1759167008.881274 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] L886 slack.slack_messages insert b07f1e10112b7661e1d8eaf3b127227f, C090N54TG79/1759266627.418203 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[UNVERIFIED] L888 slack.slack_messages insert 37d66469c43368f08befb2d6bf0c8d28, C093LEZGF6J/1759263026.184402 - public channel #zombie-prs: persona EMPLOYEE_0005_SLACK_ID is not a member; non-member reads not established (U1)
[YES] L890 slack.slack_messages update c53936d63c93c8ffa0ad1e99526cad73, C090N54TG79/1758691397.679889 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES] L891 slack.slack_messages update e6a91393854458ad70331ef478952136, C090N54TG79/1758581651.167799 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[UNVERIFIED] L892 slack.slack_messages update  - message None not found in SQL or base (U7)
[UNVERIFIED] L893 slack.slack_messages update 637fc98bc66d41b104fe243006fdcf98, C093LEZGF6J/1759258475.735779 - public channel #zombie-prs: persona EMPLOYEE_0005_SLACK_ID is not a member; non-member reads not established (U1)
[YES LB] L894 gdrive.drive_files insert f_cadae9f611d82d56ac02c3 - file is shared with the persona (shared_with_emails)
[YES LB] L896 gsheets.sheets_spreadsheets insert f_cadae9f611d82d56ac02c3 - file is shared with the persona (shared_with_emails)
[YES LB] L898 gsheets.sheets_sheets insert f_cadae9f611d82d56ac02c3, f_cadae9f611d82d56ac02c3#0 - file is shared with the persona (shared_with_emails)
[YES LB] L900 slack.slack_messages insert 3dd0b6d6c52c21cd5bbfcd6d6f5345cd, C08R27X0EAH/1759158757.418562 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-bugs
[YES LB] L902 slack.slack_messages insert 3d8e451a198d5d59b39e60064b590305, C08R27X0EAH/1759158843.902317 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-bugs
[YES LB] base slack C05433XK267/1758803475.436309 - base record: message inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of public builds
[YES LB] base slack C08R27X0EAH/1758420497.482989 - base record: message inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-bugs
[YES LB] base slack C090N54TG79/1758517286.431379 - base record: message inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] base slack C090N54TG79/1759171957.791499 - base record: message inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] base slack C090N54TG79/1759176983.189479 - base record: message inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] base slack C090N54TG79/1759178344.878219 - base record: thread reply inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] base gdrive d_8140f09bf9f1b94cb8ee2d - base record: persona owns the file

summary: {'YES': 242, 'NO': 41, 'UNVERIFIED': 3}  unscoped rows (always visible): 249
  gcal.gcal_events: {'YES': 2}
  gdocs.docs_documents: {'YES': 82}
  gdrive.drive_files: {'YES': 86}
  gmail.gmail_messages: {'YES': 21, 'NO': 21}
  gmail.gmail_threads: {'YES': 20, 'NO': 20}
  gsheets.sheets_sheets: {'YES': 4}
  gsheets.sheets_spreadsheets: {'YES': 3}
  gslides.slides_page_elements: {'YES': 3}
  gslides.slides_pages: {'YES': 3}
  gslides.slides_presentations: {'YES': 1}
  slack.slack_messages: {'YES': 17, 'UNVERIFIED': 3}
verdict: PASS (0 load-bearing rows not visible)
```

## 1.F Collision

Identity tokens: no new external person; every seeded author reuses a base token, so no header or body token is minted. Minted ids were checked through `hg.py records` over the full collection of each service (complete scans, table below). Slack rows and Gmail thread and message ids are covered by `base_check` Check A and `sql_lint`, which test them against the base; Gmail exports are one file per thread, so no single array holds them.

| Service | Ids checked | scan_complete | Base hits |
|---|---|---|---|
| gdrive /drive_files id | 65 | True | 0 |
| gdocs /docs_documents document_id | 62 | True | 0 |
| gcal /events event_id | 2 | True | 0 |
| gcal /events ical_uid | 1 | True | 0 |
| linear /issues identifier | 61 | True | 0 |
| trello /cards id | 1 | True | 0 |
| trello /actions id | 1 | True | 0 |
| github /review_comments id | 2 | True | 0 |
| github /reviews id | 1 | True | 0 |

Slack `(channel, ts)` pairs and row ids (`sha256('<channel>|<ts>')[:32]`, e.g. C090N54TG79/1758819934.612483) pass `sql_lint`; next ids follow the series: `harmonygames-Games/match3d#476#rc_27`, `#rev_3`, ZOM-567 after ZOM-566, idShort 80 on board 6851a6569f3bf818760632ab.

## Record ledger

| # | Service · table | Id | Container | Manifest element | Carrier | Reach | Discovery role |
|---|---|---|---|---|---|---|---|
| 1 | gdrive.drive_files | f_748d26e760e54651eaa0d8 | d_63fffeb4fab5233ed5bb73 | F-DEVICE,F-BUILD,H-GATE | ● | owner or shared_with | connecting |
| 2 | gdrive.drive_files | f_c691d577b8f837eb4f9eaa | d_8140f09bf9f1b94cb8ee2d | F-STATE | ● | owner or shared_with | connecting |
| 3 | gdrive.drive_files | f_a087f049d271e9aa9f567f | d_8140f09bf9f1b94cb8ee2d | F-LEAD,T-AUD,H-AUD | ● | owner or shared_with | connecting |
| 4 | gdrive.drive_files | f_43bc35baf77fd59f4e57b8 | d_8140f09bf9f1b94cb8ee2d | F-REG | ● | owner or shared_with | connecting |
| 5 | gdrive.drive_files | f_4e21b203a62910bdae0353 | d_65c76e0b87aa7e9b84d1df | T-RET | ● | owner or shared_with | connecting |
| 6 | gdrive.drive_files | f_524278b67bfa30dde78699 | d_fc22d5941b2aeb5c03ad32 | T-K4 | ● | owner or shared_with | connecting |
| 7 | gdrive.drive_files | f_b66d5288a6d3ca9d4d03b6 | d_fc22d5941b2aeb5c03ad32 | Drive companion | ● | owner or shared_with | connecting |
| 8 | gdrive.drive_files | f_8dab41c358ba484acad83d | d_fc22d5941b2aeb5c03ad32 | Drive companion | ● | owner or shared_with | connecting |
| 9 | gdrive.drive_files | f_abf945213ee8762fbdc083 | d_fc22d5941b2aeb5c03ad32 | Drive companion | ● | owner or shared_with | connecting |
| 10 | gdrive.drive_files | f_36b61fd6f9ef6ec45cf759 | d_fc22d5941b2aeb5c03ad32 | Drive companion | ● | owner or shared_with | connecting |
| 11 | gdrive.drive_files | f_548e4061239f8bbb1ebef1 | d_fc22d5941b2aeb5c03ad32 | Drive companion | ● | owner or shared_with | connecting |
| 12 | gdrive.drive_files | f_3ff040d3a2e345719d4a70 | d_fc22d5941b2aeb5c03ad32 | Drive companion | ● | owner or shared_with | connecting |
| 13 | gdrive.drive_files | f_70e9bf3f18b32fbce7c3d0 | d_fc22d5941b2aeb5c03ad32 | Drive companion | ● | owner or shared_with | connecting |
| 14 | gdrive.drive_files | f_cff26f47141203716f669b | d_fc22d5941b2aeb5c03ad32 | Drive companion | ● | owner or shared_with | connecting |
| 15 | gdrive.drive_files | f_4ceb107c67c8348b1df02b | d_9f7ba94f7526d54d8482ba | Drive companion | ● | owner or shared_with | connecting |
| 16 | gdrive.drive_files | f_b96fd720b7d4010291329c | d_9f7ba94f7526d54d8482ba | Drive companion | ● | owner or shared_with | connecting |
| 17 | gdrive.drive_files | f_f575437ac7c498de7e1db9 | d_9f7ba94f7526d54d8482ba | Drive companion | ● | owner or shared_with | connecting |
| 18 | gdrive.drive_files | f_739d61e4b5cb2ed69db3d5 | d_9f7ba94f7526d54d8482ba | Drive companion | ● | owner or shared_with | connecting |
| 19 | gdrive.drive_files | f_50d49b0baf64a424fb73a7 | d_9f7ba94f7526d54d8482ba | Drive companion | ● | owner or shared_with | connecting |
| 20 | gdrive.drive_files | f_fca92e85c34b7b0d6f950b | d_9f7ba94f7526d54d8482ba | Drive companion | ● | owner or shared_with | connecting |
| 21 | gdrive.drive_files | f_d4ac4049ba1892fd91a3bd | d_9f7ba94f7526d54d8482ba | Drive companion | ● | owner or shared_with | connecting |
| 22 | gdrive.drive_files | f_28dcffa96acbd33e38ad20 | d_9f7ba94f7526d54d8482ba | Drive companion | ● | owner or shared_with | connecting |
| 23 | gdrive.drive_files | f_69208de7d381dc75193b14 | d_9f7ba94f7526d54d8482ba | Drive companion | ● | owner or shared_with | connecting |
| 24 | gdrive.drive_files | f_1bccd7e487171e17d051a5 | d_9f7ba94f7526d54d8482ba | Drive companion | ● | owner or shared_with | connecting |
| 25 | gdrive.drive_files | f_860c5fa834dda962164827 | d_bdf01b53c6a92c5e167c65 | Drive companion | ● | owner or shared_with | connecting |
| 26 | gdrive.drive_files | f_cfbab45acc997b0917321e | d_bdf01b53c6a92c5e167c65 | Drive companion | ● | owner or shared_with | connecting |
| 27 | gdrive.drive_files | f_b00473df1ed377c7ea0a03 | d_bdf01b53c6a92c5e167c65 | Drive companion | ● | owner or shared_with | connecting |
| 28 | gdrive.drive_files | f_f96134888258f49bf9b411 | d_4e13bd40cc73d0fc76f87c | Drive companion | ● | owner or shared_with | connecting |
| 29 | gdrive.drive_files | f_7907038d6d8ec99a11f01b | d_4e13bd40cc73d0fc76f87c | Drive companion | ● | owner or shared_with | connecting |
| 30 | gdrive.drive_files | f_a27c70f8af81a5cfe57b53 | d_4e13bd40cc73d0fc76f87c | Drive companion | ● | owner or shared_with | connecting |
| 31 | gdrive.drive_files | f_55f2f152df34be6a2ea5d6 | d_caafeec2804b3a67ce46aa | Drive companion | ● | owner or shared_with | connecting |
| 32 | gdrive.drive_files | f_a7950c7698ff9b933a6a7b | d_caafeec2804b3a67ce46aa | Drive companion | ● | owner or shared_with | connecting |
| 33 | gdrive.drive_files | f_a4258d0113946c326f52d3 | d_caafeec2804b3a67ce46aa | Drive companion | ● | owner or shared_with | connecting |
| 34 | gdrive.drive_files | f_de4b874824c91335dfcb67 | d_49b9dfa5208d400d9b3937 | Drive companion | ● | owner or shared_with | connecting |
| 35 | gdrive.drive_files | f_75fe047f2040b34355f80a | d_49b9dfa5208d400d9b3937 | Drive companion | ● | owner or shared_with | connecting |
| 36 | gdrive.drive_files | f_ffaa152d5c62e39d22cf94 | d_c77c50cc15c5342d638ebb | Drive companion | ● | owner or shared_with | connecting |
| 37 | gdrive.drive_files | f_d9ac7d60efdb8fe313bb6c | d_c77c50cc15c5342d638ebb | Drive companion | ● | owner or shared_with | connecting |
| 38 | gdrive.drive_files | f_e0843c039ea62e1a61179e | d_c77c50cc15c5342d638ebb | Drive companion | ● | owner or shared_with | connecting |
| 39 | gdrive.drive_files | f_f44fee2ed41dd0b0311f41 | d_bdf01b53c6a92c5e167c65 | Drive companion | ● | owner or shared_with | connecting |
| 40 | gdrive.drive_files | f_4da421425634258e986f3c | d_bdf01b53c6a92c5e167c65 | Drive companion | ● | owner or shared_with | connecting |
| 41 | gdrive.drive_files | f_6b1f637c9012a167e0f466 | d_4e13bd40cc73d0fc76f87c | Drive companion | ● | owner or shared_with | connecting |
| 42 | gdrive.drive_files | f_e8018f6e1a4a46020dd321 | d_4e13bd40cc73d0fc76f87c | Drive companion | ● | owner or shared_with | connecting |
| 43 | gdrive.drive_files | f_156ca006436f0ecac0ccec | d_caafeec2804b3a67ce46aa | Drive companion | ● | owner or shared_with | connecting |
| 44 | gdrive.drive_files | f_6996d570d484f6b4c0f989 | d_caafeec2804b3a67ce46aa | Drive companion | ● | owner or shared_with | connecting |
| 45 | gdrive.drive_files | f_69dc1cbd43ec586d7db4d9 | d_7fe31e7ec81996189e1f14 | Drive companion | ● | owner or shared_with | connecting |
| 46 | gdrive.drive_files | f_75130b3e7a11db61a4f6e4 | d_7fe31e7ec81996189e1f14 | Drive companion | ● | owner or shared_with | connecting |
| 47 | gdrive.drive_files | f_ef202456330445c2745977 | d_7fe31e7ec81996189e1f14 | Drive companion | ● | owner or shared_with | connecting |
| 48 | gdrive.drive_files | f_e295aa601d92bf76146caf | d_7fe31e7ec81996189e1f14 | Drive companion | ● | owner or shared_with | connecting |
| 49 | gdrive.drive_files | f_898157c507a362a053135a | d_7fe31e7ec81996189e1f14 | Drive companion | ● | owner or shared_with | connecting |
| 50 | gdrive.drive_files | f_15e5a2e226ab3e8994c970 | d_7fe31e7ec81996189e1f14 | Drive companion | ● | owner or shared_with | connecting |
| 51 | gdrive.drive_files | f_fbbd9f849a298efec6f7ae | d_7fe31e7ec81996189e1f14 | Drive companion | ● | owner or shared_with | connecting |
| 52 | gdrive.drive_files | f_43d2aee7be6a4c16d9ee95 | d_7fe31e7ec81996189e1f14 | Drive companion | ● | owner or shared_with | connecting |
| 53 | gdrive.drive_files | f_18a8a68476130a03866485 | d_7fe31e7ec81996189e1f14 | Drive companion | ● | owner or shared_with | connecting |
| 54 | gdrive.drive_files | f_61c51adfb98b4dfa709abc | d_7fe31e7ec81996189e1f14 | Drive companion | ● | owner or shared_with | connecting |
| 55 | gdrive.drive_files | f_24937bdfc5070d08168595 | d_7fe31e7ec81996189e1f14 | Drive companion | ● | owner or shared_with | connecting |
| 56 | gdrive.drive_files | f_de36d4d3f886c05f52dc3f | d_7fe31e7ec81996189e1f14 | Drive companion | ● | owner or shared_with | connecting |
| 57 | gdrive.drive_files | f_232c00349f8ad72acd9952 | d_7fe31e7ec81996189e1f14 | Drive companion | ● | owner or shared_with | connecting |
| 58 | gdrive.drive_files | f_2c58c7b8fa72b1c6312ce1 | d_49b9dfa5208d400d9b3937 | Drive companion | ● | owner or shared_with | connecting |
| 59 | gdrive.drive_files | f_f8712b72a8f7ba2a3eede9 | d_65c76e0b87aa7e9b84d1df | Drive companion | ● | owner or shared_with | connecting |
| 60 | gdrive.drive_files | f_0ad31b94b4472285773483 | d_65c76e0b87aa7e9b84d1df | Drive companion | ● | owner or shared_with | connecting |
| 61 | gdrive.drive_files | f_8019f063eeae3d9c721975 | d_65c76e0b87aa7e9b84d1df | Drive companion | ● | owner or shared_with | connecting |
| 62 | gdrive.drive_files | f_33b9697009de5d63cee67a | d_cc3e90160f490686039986 | Drive companion | ● | owner or shared_with | connecting |
| 63 | gdrive.drive_files | f_2060ffa9cdcfca3b45edd1 | d_cd7849ec043ab3da107f8c | Drive companion | ● | owner or shared_with | connecting |
| 64 | gdrive.drive_files | f_69e935f38bc4f701a82307 | d_51f5f16d46e8cf55f5ee33 | Drive companion | ● | owner or shared_with | connecting |
| 65 | gdrive.drive_files | f_87cdeaa9f63796916b71eb | d_51f5f16d46e8cf55f5ee33 | Drive companion | ● | owner or shared_with | connecting |
| 66 | gdocs.docs_documents | f_748d26e760e54651eaa0d8 | f_748d26e760e54651eaa0d8 | F-DEVICE,F-BUILD,H-GATE | ● | owner or shared_with | evidence |
| 67 | gdocs.docs_documents | f_c691d577b8f837eb4f9eaa | f_c691d577b8f837eb4f9eaa | F-STATE | ● | owner or shared_with | evidence |
| 68 | gdocs.docs_documents | f_524278b67bfa30dde78699 | f_524278b67bfa30dde78699 | T-K4 | ● | owner or shared_with | evidence |
| 69 | gdocs.docs_documents | f_b66d5288a6d3ca9d4d03b6 | f_b66d5288a6d3ca9d4d03b6 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 70 | gdocs.docs_documents | f_8dab41c358ba484acad83d | f_8dab41c358ba484acad83d | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 71 | gdocs.docs_documents | f_abf945213ee8762fbdc083 | f_abf945213ee8762fbdc083 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 72 | gdocs.docs_documents | f_36b61fd6f9ef6ec45cf759 | f_36b61fd6f9ef6ec45cf759 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 73 | gdocs.docs_documents | f_548e4061239f8bbb1ebef1 | f_548e4061239f8bbb1ebef1 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 74 | gdocs.docs_documents | f_3ff040d3a2e345719d4a70 | f_3ff040d3a2e345719d4a70 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 75 | gdocs.docs_documents | f_70e9bf3f18b32fbce7c3d0 | f_70e9bf3f18b32fbce7c3d0 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 76 | gdocs.docs_documents | f_cff26f47141203716f669b | f_cff26f47141203716f669b | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 77 | gdocs.docs_documents | f_4ceb107c67c8348b1df02b | f_4ceb107c67c8348b1df02b | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 78 | gdocs.docs_documents | f_b96fd720b7d4010291329c | f_b96fd720b7d4010291329c | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 79 | gdocs.docs_documents | f_f575437ac7c498de7e1db9 | f_f575437ac7c498de7e1db9 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 80 | gdocs.docs_documents | f_739d61e4b5cb2ed69db3d5 | f_739d61e4b5cb2ed69db3d5 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 81 | gdocs.docs_documents | f_50d49b0baf64a424fb73a7 | f_50d49b0baf64a424fb73a7 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 82 | gdocs.docs_documents | f_fca92e85c34b7b0d6f950b | f_fca92e85c34b7b0d6f950b | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 83 | gdocs.docs_documents | f_d4ac4049ba1892fd91a3bd | f_d4ac4049ba1892fd91a3bd | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 84 | gdocs.docs_documents | f_28dcffa96acbd33e38ad20 | f_28dcffa96acbd33e38ad20 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 85 | gdocs.docs_documents | f_69208de7d381dc75193b14 | f_69208de7d381dc75193b14 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 86 | gdocs.docs_documents | f_1bccd7e487171e17d051a5 | f_1bccd7e487171e17d051a5 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 87 | gdocs.docs_documents | f_860c5fa834dda962164827 | f_860c5fa834dda962164827 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 88 | gdocs.docs_documents | f_cfbab45acc997b0917321e | f_cfbab45acc997b0917321e | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 89 | gdocs.docs_documents | f_b00473df1ed377c7ea0a03 | f_b00473df1ed377c7ea0a03 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 90 | gdocs.docs_documents | f_f96134888258f49bf9b411 | f_f96134888258f49bf9b411 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 91 | gdocs.docs_documents | f_7907038d6d8ec99a11f01b | f_7907038d6d8ec99a11f01b | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 92 | gdocs.docs_documents | f_a27c70f8af81a5cfe57b53 | f_a27c70f8af81a5cfe57b53 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 93 | gdocs.docs_documents | f_55f2f152df34be6a2ea5d6 | f_55f2f152df34be6a2ea5d6 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 94 | gdocs.docs_documents | f_a7950c7698ff9b933a6a7b | f_a7950c7698ff9b933a6a7b | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 95 | gdocs.docs_documents | f_a4258d0113946c326f52d3 | f_a4258d0113946c326f52d3 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 96 | gdocs.docs_documents | f_de4b874824c91335dfcb67 | f_de4b874824c91335dfcb67 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 97 | gdocs.docs_documents | f_75fe047f2040b34355f80a | f_75fe047f2040b34355f80a | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 98 | gdocs.docs_documents | f_ffaa152d5c62e39d22cf94 | f_ffaa152d5c62e39d22cf94 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 99 | gdocs.docs_documents | f_d9ac7d60efdb8fe313bb6c | f_d9ac7d60efdb8fe313bb6c | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 100 | gdocs.docs_documents | f_e0843c039ea62e1a61179e | f_e0843c039ea62e1a61179e | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 101 | gdocs.docs_documents | f_f44fee2ed41dd0b0311f41 | f_f44fee2ed41dd0b0311f41 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 102 | gdocs.docs_documents | f_4da421425634258e986f3c | f_4da421425634258e986f3c | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 103 | gdocs.docs_documents | f_6b1f637c9012a167e0f466 | f_6b1f637c9012a167e0f466 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 104 | gdocs.docs_documents | f_e8018f6e1a4a46020dd321 | f_e8018f6e1a4a46020dd321 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 105 | gdocs.docs_documents | f_156ca006436f0ecac0ccec | f_156ca006436f0ecac0ccec | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 106 | gdocs.docs_documents | f_6996d570d484f6b4c0f989 | f_6996d570d484f6b4c0f989 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 107 | gdocs.docs_documents | f_69dc1cbd43ec586d7db4d9 | f_69dc1cbd43ec586d7db4d9 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 108 | gdocs.docs_documents | f_75130b3e7a11db61a4f6e4 | f_75130b3e7a11db61a4f6e4 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 109 | gdocs.docs_documents | f_ef202456330445c2745977 | f_ef202456330445c2745977 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 110 | gdocs.docs_documents | f_e295aa601d92bf76146caf | f_e295aa601d92bf76146caf | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 111 | gdocs.docs_documents | f_898157c507a362a053135a | f_898157c507a362a053135a | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 112 | gdocs.docs_documents | f_15e5a2e226ab3e8994c970 | f_15e5a2e226ab3e8994c970 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 113 | gdocs.docs_documents | f_fbbd9f849a298efec6f7ae | f_fbbd9f849a298efec6f7ae | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 114 | gdocs.docs_documents | f_43d2aee7be6a4c16d9ee95 | f_43d2aee7be6a4c16d9ee95 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 115 | gdocs.docs_documents | f_18a8a68476130a03866485 | f_18a8a68476130a03866485 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 116 | gdocs.docs_documents | f_61c51adfb98b4dfa709abc | f_61c51adfb98b4dfa709abc | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 117 | gdocs.docs_documents | f_24937bdfc5070d08168595 | f_24937bdfc5070d08168595 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 118 | gdocs.docs_documents | f_de36d4d3f886c05f52dc3f | f_de36d4d3f886c05f52dc3f | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 119 | gdocs.docs_documents | f_232c00349f8ad72acd9952 | f_232c00349f8ad72acd9952 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 120 | gdocs.docs_documents | f_2c58c7b8fa72b1c6312ce1 | f_2c58c7b8fa72b1c6312ce1 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 121 | gdocs.docs_documents | f_f8712b72a8f7ba2a3eede9 | f_f8712b72a8f7ba2a3eede9 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 122 | gdocs.docs_documents | f_0ad31b94b4472285773483 | f_0ad31b94b4472285773483 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 123 | gdocs.docs_documents | f_8019f063eeae3d9c721975 | f_8019f063eeae3d9c721975 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 124 | gdocs.docs_documents | f_33b9697009de5d63cee67a | f_33b9697009de5d63cee67a | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 125 | gdocs.docs_documents | f_2060ffa9cdcfca3b45edd1 | f_2060ffa9cdcfca3b45edd1 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 126 | gdocs.docs_documents | f_69e935f38bc4f701a82307 | f_69e935f38bc4f701a82307 | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 127 | gdocs.docs_documents | f_87cdeaa9f63796916b71eb | f_87cdeaa9f63796916b71eb | cohort surface gdocs (build, age, relation) | ● | owner or shared_with | evidence |
| 128 | gsheets.sheets_spreadsheets | f_43bc35baf77fd59f4e57b8 | f_43bc35baf77fd59f4e57b8 | F-REG | ● | owner or shared_with | first link |
| 129 | gsheets.sheets_sheets | f_43bc35baf77fd59f4e57b8 tab Log | f_43bc35baf77fd59f4e57b8 | F-REG | ● | owner or shared_with | first link |
| 130 | gsheets.sheets_sheets | f_43bc35baf77fd59f4e57b8 tab Register | f_43bc35baf77fd59f4e57b8 | F-REG | ● | owner or shared_with | first link |
| 131 | gsheets.sheets_spreadsheets | f_4e21b203a62910bdae0353 | f_4e21b203a62910bdae0353 | T-RET | ● | owner or shared_with | first link |
| 132 | gsheets.sheets_sheets | f_4e21b203a62910bdae0353 tab KPI | f_4e21b203a62910bdae0353 | T-RET | ● | owner or shared_with | first link |
| 133 | gslides.slides_presentations | f_a087f049d271e9aa9f567f | f_a087f049d271e9aa9f567f | F-LEAD,T-AUD,H-AUD | ● | owner or shared_with | authority |
| 134 | gslides.slides_pages | f_a087f049d271e9aa9f567f slide_d680691ee9e5 | f_a087f049d271e9aa9f567f | F-LEAD,T-AUD,H-AUD | ● | owner or shared_with | authority |
| 135 | gslides.slides_page_elements | f_a087f049d271e9aa9f567f el_6ddced6da136 | f_a087f049d271e9aa9f567f | F-LEAD,T-AUD,H-AUD | ● | owner or shared_with | authority |
| 136 | gslides.slides_pages | f_a087f049d271e9aa9f567f slide_29241137200c | f_a087f049d271e9aa9f567f | F-LEAD,T-AUD,H-AUD | ● | owner or shared_with | authority |
| 137 | gslides.slides_page_elements | f_a087f049d271e9aa9f567f el_18102c1d9b66 | f_a087f049d271e9aa9f567f | F-LEAD,T-AUD,H-AUD | ● | owner or shared_with | authority |
| 138 | gslides.slides_pages | f_a087f049d271e9aa9f567f slide_1b64c7b03a47 | f_a087f049d271e9aa9f567f | F-LEAD,T-AUD,H-AUD | ● | owner or shared_with | authority |
| 139 | gslides.slides_page_elements | f_a087f049d271e9aa9f567f el_5b5d50499cb5 | f_a087f049d271e9aa9f567f | F-LEAD,T-AUD,H-AUD | ● | owner or shared_with | authority |
| 140 | gcal.gcal_events | evt_960936eab424f7726db95c | claire.morgan@harmonygames.co | calendar copy | ○ detail, ● summary and attendees | attendee copy | connecting |
| 141 | gcal.gcal_events | evt_da65644831bc088267263d | julia.lawson@harmonygames.co | T-K1 | ○ detail, ● summary and attendees | attendee copy | connecting |
| 142 | gmail.gmail_threads | julia.lawson@harmonygames.co/1843954918097449014 | julia.lawson@harmonygames.co | F-PANEL | ● | mailbox | container |
| 143 | gmail.gmail_messages | julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com> | julia.lawson@harmonygames.co/1843954918097449014 | F-PANEL,T-PANEL,H-PANEL | ● | Julia's mailbox | evidence |
| 144 | gmail.gmail_threads | leonard.hayes@harmonygames.co/1843954918098117383 | leonard.hayes@harmonygames.co | thread row | ● | mailbox | container |
| 145 | gmail.gmail_messages | leonard.hayes@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com> | leonard.hayes@harmonygames.co/1843954918098117383 | sender copy | ● | sender copy, companion | companion |
| 146 | gmail.gmail_threads | julia.lawson@harmonygames.co/1844094591565886237 | julia.lawson@harmonygames.co | thread row | ● | mailbox | container |
| 147 | gmail.gmail_messages | julia.lawson@harmonygames.co/<CA01dc2d92371c7bfa63e451026f81fffed801@mail.gmail.com> | julia.lawson@harmonygames.co/1844094591565886237 | T-K5 | ● | Julia's mailbox | evidence |
| 148 | gmail.gmail_threads | robert@harmonygames.co/1844094591566494759 | robert@harmonygames.co | thread row | ● | mailbox | container |
| 149 | gmail.gmail_messages | robert@harmonygames.co/<CA01dc2d92371c7bfa63e451026f81fffed801@mail.gmail.com> | robert@harmonygames.co/1844094591566494759 | sender copy | ● | sender copy, companion | companion |
| 150 | gmail.gmail_threads | julia.lawson@harmonygames.co/1844139735908739966 | julia.lawson@harmonygames.co | thread row | ● | mailbox | container |
| 151 | gmail.gmail_messages | julia.lawson@harmonygames.co/<CAbd808e99ae075a1768fb68e9b6520d133fab@mail.gmail.com> | julia.lawson@harmonygames.co/1844139735908739966 | cohort surface gmail | ● | Julia's mailbox | evidence |
| 152 | gmail.gmail_threads | oliver.brooks@harmonygames.co/1844139735909330734 | oliver.brooks@harmonygames.co | thread row | ● | mailbox | container |
| 153 | gmail.gmail_messages | oliver.brooks@harmonygames.co/<CAbd808e99ae075a1768fb68e9b6520d133fab@mail.gmail.com> | oliver.brooks@harmonygames.co/1844139735909330734 | sender copy | ● | sender copy, companion | companion |
| 154 | gmail.gmail_threads | julia.lawson@harmonygames.co/1844151965450762802 | julia.lawson@harmonygames.co | thread row | ● | mailbox | container |
| 155 | gmail.gmail_messages | julia.lawson@harmonygames.co/<CA44aaa5cd5c2d0378119d16b5250dd63f309a@mail.gmail.com> | julia.lawson@harmonygames.co/1844151965450762802 | cohort surface gmail | ● | Julia's mailbox | evidence |
| 156 | gmail.gmail_threads | owen.baker@harmonygames.co/1844151965451361163 | owen.baker@harmonygames.co | thread row | ● | mailbox | container |
| 157 | gmail.gmail_messages | owen.baker@harmonygames.co/<CA44aaa5cd5c2d0378119d16b5250dd63f309a@mail.gmail.com> | owen.baker@harmonygames.co/1844151965451361163 | sender copy | ● | sender copy, companion | companion |
| 158 | gmail.gmail_threads | julia.lawson@harmonygames.co/1844226064122813574 | julia.lawson@harmonygames.co | thread row | ● | mailbox | container |
| 159 | gmail.gmail_messages | julia.lawson@harmonygames.co/<CA748f9425b26f35f255ea9bf80873b2bed8a4@mail.gmail.com> | julia.lawson@harmonygames.co/1844226064122813574 | cohort surface gmail | ● | Julia's mailbox | evidence |
| 160 | gmail.gmail_threads | samuel.turner@harmonygames.co/1844226064123492719 | samuel.turner@harmonygames.co | thread row | ● | mailbox | container |
| 161 | gmail.gmail_messages | samuel.turner@harmonygames.co/<CA748f9425b26f35f255ea9bf80873b2bed8a4@mail.gmail.com> | samuel.turner@harmonygames.co/1844226064123492719 | sender copy | ● | sender copy, companion | companion |
| 162 | gmail.gmail_threads | julia.lawson@harmonygames.co/1844245860188980242 | julia.lawson@harmonygames.co | thread row | ● | mailbox | container |
| 163 | gmail.gmail_messages | julia.lawson@harmonygames.co/<CA0bc4f062a9faedd8054b0e0279fb82c17644@mail.gmail.com> | julia.lawson@harmonygames.co/1844245860188980242 | cohort surface gmail | ● | Julia's mailbox | evidence |
| 164 | gmail.gmail_threads | calvin.price@harmonygames.co/1844245860189680279 | calvin.price@harmonygames.co | thread row | ● | mailbox | container |
| 165 | gmail.gmail_messages | calvin.price@harmonygames.co/<CA0bc4f062a9faedd8054b0e0279fb82c17644@mail.gmail.com> | calvin.price@harmonygames.co/1844245860189680279 | sender copy | ● | sender copy, companion | companion |
| 166 | gmail.gmail_threads | julia.lawson@harmonygames.co/1844255215584092313 | julia.lawson@harmonygames.co | thread row | ● | mailbox | container |
| 167 | gmail.gmail_messages | julia.lawson@harmonygames.co/<CA5f548a065eb5efb9731cb60c737492aaf209@mail.gmail.com> | julia.lawson@harmonygames.co/1844255215584092313 | cohort surface gmail | ● | Julia's mailbox | evidence |
| 168 | gmail.gmail_threads | marcus.bennett@harmonygames.co/1844255215584474042 | marcus.bennett@harmonygames.co | thread row | ● | mailbox | container |
| 169 | gmail.gmail_messages | marcus.bennett@harmonygames.co/<CA5f548a065eb5efb9731cb60c737492aaf209@mail.gmail.com> | marcus.bennett@harmonygames.co/1844255215584474042 | sender copy | ● | sender copy, companion | companion |
| 170 | gmail.gmail_threads | julia.lawson@harmonygames.co/1844314577567776575 | julia.lawson@harmonygames.co | thread row | ● | mailbox | container |
| 171 | gmail.gmail_messages | julia.lawson@harmonygames.co/<CAb1c036095fc86f88066e4b0d22c5f21fe2c8@mail.gmail.com> | julia.lawson@harmonygames.co/1844314577567776575 | cohort surface gmail | ● | Julia's mailbox | evidence |
| 172 | gmail.gmail_threads | oliver.brooks@harmonygames.co/1844314577568386305 | oliver.brooks@harmonygames.co | thread row | ● | mailbox | container |
| 173 | gmail.gmail_messages | oliver.brooks@harmonygames.co/<CAb1c036095fc86f88066e4b0d22c5f21fe2c8@mail.gmail.com> | oliver.brooks@harmonygames.co/1844314577568386305 | sender copy | ● | sender copy, companion | companion |
| 174 | gmail.gmail_threads | julia.lawson@harmonygames.co/1844324114366762178 | julia.lawson@harmonygames.co | thread row | ● | mailbox | container |
| 175 | gmail.gmail_messages | julia.lawson@harmonygames.co/<CA02723a70e7ae56e2282af7734b7e44ef3f23@mail.gmail.com> | julia.lawson@harmonygames.co/1844324114366762178 | cohort surface gmail | ● | Julia's mailbox | evidence |
| 176 | gmail.gmail_threads | owen.baker@harmonygames.co/1844324114367028910 | owen.baker@harmonygames.co | thread row | ● | mailbox | container |
| 177 | gmail.gmail_messages | owen.baker@harmonygames.co/<CA02723a70e7ae56e2282af7734b7e44ef3f23@mail.gmail.com> | owen.baker@harmonygames.co/1844324114367028910 | sender copy | ● | sender copy, companion | companion |
| 178 | gmail.gmail_threads | julia.lawson@harmonygames.co/1844334980760275863 | julia.lawson@harmonygames.co | thread row | ● | mailbox | container |
| 179 | gmail.gmail_messages | julia.lawson@harmonygames.co/<CA48a7bbb5a0e6beec2ec9409441455990c0db@mail.gmail.com> | julia.lawson@harmonygames.co/1844334980760275863 | cohort surface gmail | ● | Julia's mailbox | evidence |
| 180 | gmail.gmail_threads | samuel.turner@harmonygames.co/1844334980760681071 | samuel.turner@harmonygames.co | thread row | ● | mailbox | container |
| 181 | gmail.gmail_messages | samuel.turner@harmonygames.co/<CA48a7bbb5a0e6beec2ec9409441455990c0db@mail.gmail.com> | samuel.turner@harmonygames.co/1844334980760681071 | sender copy | ● | sender copy, companion | companion |
| 182 | gmail.gmail_threads | julia.lawson@harmonygames.co/1844361729934100115 | julia.lawson@harmonygames.co | thread row | ● | mailbox | container |
| 183 | gmail.gmail_messages | julia.lawson@harmonygames.co/<CAefcc9dd45170efad4834318d398795bc1db8@mail.gmail.com> | julia.lawson@harmonygames.co/1844361729934100115 | T-K1 | ● | Julia's mailbox | evidence |
| 184 | gmail.gmail_threads | claire.morgan@harmonygames.co/1844361729934945604 | claire.morgan@harmonygames.co | thread row | ● | mailbox | container |
| 185 | gmail.gmail_messages | claire.morgan@harmonygames.co/<CAefcc9dd45170efad4834318d398795bc1db8@mail.gmail.com> | claire.morgan@harmonygames.co/1844361729934945604 | sender copy | ● | sender copy, companion | companion |
| 186 | gmail.gmail_threads | julia.lawson@harmonygames.co/1844589014025156069 | julia.lawson@harmonygames.co | thread row | ● | mailbox | container |
| 187 | gmail.gmail_messages | julia.lawson@harmonygames.co/<CA51381f43e05aa46404914b984a5820296e26@mail.gmail.com> | julia.lawson@harmonygames.co/1844589014025156069 | cohort surface gmail | ● | Julia's mailbox | evidence |
| 188 | gmail.gmail_threads | calvin.price@harmonygames.co/1844589014025497035 | calvin.price@harmonygames.co | thread row | ● | mailbox | container |
| 189 | gmail.gmail_messages | calvin.price@harmonygames.co/<CA51381f43e05aa46404914b984a5820296e26@mail.gmail.com> | calvin.price@harmonygames.co/1844589014025497035 | sender copy | ● | sender copy, companion | companion |
| 190 | gmail.gmail_threads | julia.lawson@harmonygames.co/1844598530900183157 | julia.lawson@harmonygames.co | thread row | ● | mailbox | container |
| 191 | gmail.gmail_messages | julia.lawson@harmonygames.co/<CA5c7622ee78a0405af6df08f42ed0e35aedd8@mail.gmail.com> | julia.lawson@harmonygames.co/1844598530900183157 | cohort surface gmail | ● | Julia's mailbox | evidence |
| 192 | gmail.gmail_threads | vincent.parker@harmonygames.co/1844598530900512479 | vincent.parker@harmonygames.co | thread row | ● | mailbox | container |
| 193 | gmail.gmail_messages | vincent.parker@harmonygames.co/<CA5c7622ee78a0405af6df08f42ed0e35aedd8@mail.gmail.com> | vincent.parker@harmonygames.co/1844598530900512479 | sender copy | ● | sender copy, companion | companion |
| 194 | gmail.gmail_threads | julia.lawson@harmonygames.co/1844605722034776031 | julia.lawson@harmonygames.co | thread row | ● | mailbox | container |
| 195 | gmail.gmail_messages | julia.lawson@harmonygames.co/<CA60103ff719e6305401dd968c8f2f55f8db09@mail.gmail.com> | julia.lawson@harmonygames.co/1844605722034776031 | cohort surface gmail | ● | Julia's mailbox | evidence |
| 196 | gmail.gmail_threads | arthur.blake@harmonygames.co/1844605722035474235 | arthur.blake@harmonygames.co | thread row | ● | mailbox | container |
| 197 | gmail.gmail_messages | arthur.blake@harmonygames.co/<CA60103ff719e6305401dd968c8f2f55f8db09@mail.gmail.com> | arthur.blake@harmonygames.co/1844605722035474235 | sender copy | ● | sender copy, companion | companion |
| 198 | gmail.gmail_threads | julia.lawson@harmonygames.co/1844612217962947730 | julia.lawson@harmonygames.co | thread row | ● | mailbox | container |
| 199 | gmail.gmail_messages | julia.lawson@harmonygames.co/<CA6e2936ce3ea7f3cad66b7b0d1cac0e913b05@mail.gmail.com> | julia.lawson@harmonygames.co/1844612217962947730 | cohort surface gmail | ● | Julia's mailbox | evidence |
| 200 | gmail.gmail_threads | douglas@harmonygames.co/1844612217963668883 | douglas@harmonygames.co | thread row | ● | mailbox | container |
| 201 | gmail.gmail_messages | douglas@harmonygames.co/<CA6e2936ce3ea7f3cad66b7b0d1cac0e913b05@mail.gmail.com> | douglas@harmonygames.co/1844612217963668883 | sender copy | ● | sender copy, companion | companion |
| 202 | gmail.gmail_threads | julia.lawson@harmonygames.co/1844675467018824635 | julia.lawson@harmonygames.co | thread row | ● | mailbox | container |
| 203 | gmail.gmail_messages | julia.lawson@harmonygames.co/<CA14bc4b41e4b7d4884c51819b961e5ebbc954@mail.gmail.com> | julia.lawson@harmonygames.co/1844675467018824635 | cohort surface gmail | ● | Julia's mailbox | evidence |
| 204 | gmail.gmail_threads | martin.walsh@harmonygames.co/1844675467019380800 | martin.walsh@harmonygames.co | thread row | ● | mailbox | container |
| 205 | gmail.gmail_messages | martin.walsh@harmonygames.co/<CA14bc4b41e4b7d4884c51819b961e5ebbc954@mail.gmail.com> | martin.walsh@harmonygames.co/1844675467019380800 | sender copy | ● | sender copy, companion | companion |
| 206 | gmail.gmail_threads | julia.lawson@harmonygames.co/1844318948033312842 | julia.lawson@harmonygames.co | thread row | ● | mailbox | container |
| 207 | gmail.gmail_messages | julia.lawson@harmonygames.co/<CA8db5b364a9d7d3c1946e722aed490d591476@mail.gmail.com> | julia.lawson@harmonygames.co/1844318948033312842 | T-DUP | ● | Julia's mailbox | evidence |
| 208 | gmail.gmail_threads | marcus.bennett@harmonygames.co/1844318948033827471 | marcus.bennett@harmonygames.co | thread row | ● | mailbox | container |
| 209 | gmail.gmail_messages | marcus.bennett@harmonygames.co/<CA8db5b364a9d7d3c1946e722aed490d591476@mail.gmail.com> | marcus.bennett@harmonygames.co/1844318948033827471 | sender copy | ● | sender copy, companion | companion |
| 210 | gmail.gmail_threads | julia.lawson@harmonygames.co/1844592159752803121 | julia.lawson@harmonygames.co | thread row | ● | mailbox | container |
| 211 | gmail.gmail_messages | julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com> | julia.lawson@harmonygames.co/1844592159752803121 | T-K1 | ● | Julia's mailbox | evidence |
| 212 | gmail.gmail_threads | claire.morgan@harmonygames.co/1844592159753417634 | claire.morgan@harmonygames.co | thread row | ● | mailbox | container |
| 213 | gmail.gmail_messages | claire.morgan@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com> | claire.morgan@harmonygames.co/1844592159753417634 | sender copy | ● | sender copy, companion | companion |
| 214 | linear.linear_issues | ZOM-567 | team_ZOM | T-K3 | ● | unscoped | first link |
| 215 | linear.linear_issues | ZOM-568 | team_ZOM | cohort key | ● | unscoped | first link |
| 216 | linear.linear_issues | ZOM-569 | team_ZOM | cohort key | ● | unscoped | first link |
| 217 | linear.linear_issues | ZOM-570 | team_ZOM | cohort key | ● | unscoped | first link |
| 218 | linear.linear_issues | ZOM-571 | team_ZOM | cohort key | ● | unscoped | first link |
| 219 | linear.linear_issues | ZOM-572 | team_ZOM | cohort key | ● | unscoped | first link |
| 220 | linear.linear_issues | ZOM-573 | team_ZOM | cohort key | ● | unscoped | first link |
| 221 | linear.linear_issues | ZOM-574 | team_ZOM | cohort key | ● | unscoped | first link |
| 222 | linear.linear_issues | ZOM-575 | team_ZOM | cohort key | ● | unscoped | first link |
| 223 | linear.linear_issues | ZOM-576 | team_ZOM | cohort key | ● | unscoped | first link |
| 224 | linear.linear_issues | ZOM-577 | team_ZOM | cohort key | ● | unscoped | first link |
| 225 | linear.linear_issues | ZOM-578 | team_ZOM | cohort key | ● | unscoped | first link |
| 226 | linear.linear_issues | ZOM-579 | team_ZOM | cohort key | ● | unscoped | first link |
| 227 | linear.linear_issues | ZOM-580 | team_ZOM | cohort key | ● | unscoped | first link |
| 228 | linear.linear_issues | ZOM-581 | team_ZOM | cohort key | ● | unscoped | first link |
| 229 | linear.linear_issues | ZOM-582 | team_ZOM | cohort key | ● | unscoped | first link |
| 230 | linear.linear_issues | ZOM-583 | team_ZOM | cohort key | ● | unscoped | first link |
| 231 | linear.linear_issues | ZOM-584 | team_ZOM | cohort key | ● | unscoped | first link |
| 232 | linear.linear_issues | ZOM-585 | team_ZOM | cohort key | ● | unscoped | first link |
| 233 | linear.linear_issues | ZOM-586 | team_ZOM | cohort key | ● | unscoped | first link |
| 234 | linear.linear_issues | ZOM-587 | team_ZOM | cohort key | ● | unscoped | first link |
| 235 | linear.linear_issues | ZOM-588 | team_ZOM | cohort key | ● | unscoped | first link |
| 236 | linear.linear_issues | ZOM-589 | team_ZOM | cohort key | ● | unscoped | first link |
| 237 | linear.linear_issues | ZOM-590 | team_ZOM | cohort key | ● | unscoped | first link |
| 238 | linear.linear_issues | ZOM-591 | team_ZOM | cohort key | ● | unscoped | first link |
| 239 | linear.linear_issues | ZOM-592 | team_ZOM | cohort key | ● | unscoped | first link |
| 240 | linear.linear_issues | ZOM-593 | team_ZOM | cohort key | ● | unscoped | first link |
| 241 | linear.linear_issues | ZOM-594 | team_ZOM | cohort key | ● | unscoped | first link |
| 242 | linear.linear_issues | ZOM-595 | team_ZOM | cohort key | ● | unscoped | first link |
| 243 | linear.linear_issues | ZOM-596 | team_ZOM | cohort key | ● | unscoped | first link |
| 244 | linear.linear_issues | ZOM-597 | team_ZOM | cohort key | ● | unscoped | first link |
| 245 | linear.linear_issues | ZOM-598 | team_ZOM | cohort key | ● | unscoped | first link |
| 246 | linear.linear_issues | ZOM-599 | team_ZOM | cohort key | ● | unscoped | first link |
| 247 | linear.linear_issues | ZOM-600 | team_ZOM | cohort key | ● | unscoped | first link |
| 248 | linear.linear_issues | ZOM-601 | team_ZOM | cohort key | ● | unscoped | first link |
| 249 | linear.linear_issues | ZOM-602 | team_ZOM | cohort key | ● | unscoped | first link |
| 250 | linear.linear_issues | ZOM-603 | team_ZOM | cohort key | ● | unscoped | first link |
| 251 | linear.linear_issues | ZOM-604 | team_ZOM | cohort key | ● | unscoped | first link |
| 252 | linear.linear_issues | ZOM-605 | team_ZOM | cohort key | ● | unscoped | first link |
| 253 | linear.linear_issues | ZOM-606 | team_ZOM | cohort key | ● | unscoped | first link |
| 254 | linear.linear_issues | ZOM-607 | team_ZOM | cohort key | ● | unscoped | first link |
| 255 | linear.linear_issues | ZOM-608 | team_ZOM | cohort key | ● | unscoped | first link |
| 256 | linear.linear_issues | ZOM-609 | team_ZOM | cohort key | ● | unscoped | first link |
| 257 | linear.linear_issues | ZOM-610 | team_ZOM | cohort key | ● | unscoped | first link |
| 258 | linear.linear_issues | ZOM-611 | team_ZOM | cohort key | ● | unscoped | first link |
| 259 | linear.linear_issues | ZOM-612 | team_ZOM | cohort key | ● | unscoped | first link |
| 260 | linear.linear_issues | ZOM-613 | team_ZOM | cohort key | ● | unscoped | first link |
| 261 | linear.linear_issues | ZOM-614 | team_ZOM | cohort key | ● | unscoped | first link |
| 262 | linear.linear_issues | ZOM-615 | team_ZOM | cohort key | ● | unscoped | first link |
| 263 | linear.linear_issues | ZOM-616 | team_ZOM | cohort key | ● | unscoped | first link |
| 264 | linear.linear_issues | ZOM-617 | team_ZOM | cohort key | ● | unscoped | first link |
| 265 | linear.linear_issues | ZOM-618 | team_ZOM | cohort key | ● | unscoped | first link |
| 266 | linear.linear_issues | ZOM-619 | team_ZOM | cohort key | ● | unscoped | first link |
| 267 | linear.linear_issues | ZOM-620 | team_ZOM | cohort key | ● | unscoped | first link |
| 268 | linear.linear_issues | ZOM-621 | team_ZOM | cohort key | ● | unscoped | first link |
| 269 | linear.linear_issues | ZOM-622 | team_ZOM | cohort key | ● | unscoped | first link |
| 270 | linear.linear_issues | ZOM-623 | team_ZOM | cohort key | ● | unscoped | first link |
| 271 | linear.linear_issues | ZOM-624 | team_ZOM | cohort key | ● | unscoped | first link |
| 272 | linear.linear_issues | ZOM-625 | team_ZOM | cohort key | ● | unscoped | first link |
| 273 | linear.linear_issues | ZOM-626 | team_ZOM | cohort key | ● | unscoped | first link |
| 274 | linear.linear_issues | ZOM-627 | team_ZOM | cohort key | ● | unscoped | first link |
| 275 | linear.linear_comments | cmt_38b3cc50dceda37f40f5 | ZOM-567 | T-K3 | ● | unscoped | evidence |
| 276 | linear.linear_comments | cmt_2fbcaf2d990d8b4e9c0d | ZOM-568 | cohort surface linear (device) | ● | unscoped | evidence |
| 277 | linear.linear_comments | cmt_d8dfed654b254845d39d | ZOM-569 | cohort surface linear (device) | ● | unscoped | evidence |
| 278 | linear.linear_comments | cmt_0fb1505315140ffd0b21 | ZOM-570 | cohort surface linear (device) | ● | unscoped | evidence |
| 279 | linear.linear_comments | cmt_3daaaa1034994aa4ffbb | ZOM-571 | cohort surface linear (device) | ● | unscoped | evidence |
| 280 | linear.linear_comments | cmt_03bb699c2fc91f181b46 | ZOM-572 | cohort surface linear (device) | ● | unscoped | evidence |
| 281 | linear.linear_comments | cmt_a23a04387ca0198012f0 | ZOM-573 | cohort surface linear (device) | ● | unscoped | evidence |
| 282 | linear.linear_comments | cmt_f08b62b7ca0d53c09c94 | ZOM-574 | cohort surface linear (device) | ● | unscoped | evidence |
| 283 | linear.linear_comments | cmt_89f50d4a6e25a5a7484e | ZOM-575 | cohort surface linear (device) | ● | unscoped | evidence |
| 284 | linear.linear_comments | cmt_fd248e7d92637605e02e | ZOM-576 | cohort surface linear (device) | ● | unscoped | evidence |
| 285 | linear.linear_comments | cmt_738ed1f9acdb089b1f75 | ZOM-577 | cohort surface linear (device) | ● | unscoped | evidence |
| 286 | linear.linear_comments | cmt_40f8d5b92e1a26b261a3 | ZOM-578 | cohort surface linear (device) | ● | unscoped | evidence |
| 287 | linear.linear_comments | cmt_a7b07495c1aa4e6f0325 | ZOM-579 | cohort surface linear (device) | ● | unscoped | evidence |
| 288 | linear.linear_comments | cmt_fdba422386d3746eb52a | ZOM-580 | cohort surface linear (device) | ● | unscoped | evidence |
| 289 | linear.linear_comments | cmt_7c0c46fda16ac3f2ed1e | ZOM-581 | cohort surface linear (device) | ● | unscoped | evidence |
| 290 | linear.linear_comments | cmt_21840da3225e5fc1302b | ZOM-582 | cohort surface linear (device) | ● | unscoped | evidence |
| 291 | linear.linear_comments | cmt_b3b84bb3817c87487559 | ZOM-583 | cohort surface linear (device) | ● | unscoped | evidence |
| 292 | linear.linear_comments | cmt_4cf4070dd936b4f4b961 | ZOM-584 | cohort surface linear (device) | ● | unscoped | evidence |
| 293 | linear.linear_comments | cmt_a5f7ecf05d2105d008cf | ZOM-585 | cohort surface linear (device) | ● | unscoped | evidence |
| 294 | linear.linear_comments | cmt_1c3a1ff63f39fd874437 | ZOM-586 | cohort surface linear (device) | ● | unscoped | evidence |
| 295 | linear.linear_comments | cmt_407f6362d41c55550dc7 | ZOM-587 | cohort surface linear (device) | ● | unscoped | evidence |
| 296 | linear.linear_comments | cmt_151b207651e5ca7a56e8 | ZOM-588 | cohort surface linear (device) | ● | unscoped | evidence |
| 297 | linear.linear_comments | cmt_2a058d7206e0218dbc42 | ZOM-589 | cohort surface linear (device) | ● | unscoped | evidence |
| 298 | linear.linear_comments | cmt_ad47d5d01226c9a60bd9 | ZOM-590 | cohort surface linear (device) | ● | unscoped | evidence |
| 299 | linear.linear_comments | cmt_474825ce59c2f800f5a7 | ZOM-591 | cohort surface linear (device) | ● | unscoped | evidence |
| 300 | linear.linear_comments | cmt_e8b9465adb7146c7e6db | ZOM-592 | cohort surface linear (device) | ● | unscoped | evidence |
| 301 | linear.linear_comments | cmt_a3a8a262de70dc320ae5 | ZOM-593 | cohort surface linear (device) | ● | unscoped | evidence |
| 302 | linear.linear_comments | cmt_1bb6794c75bc21bcafae | ZOM-594 | cohort surface linear (device) | ● | unscoped | evidence |
| 303 | linear.linear_comments | cmt_87b20b86cf6de56ee7e1 | ZOM-595 | cohort surface linear (device) | ● | unscoped | evidence |
| 304 | linear.linear_comments | cmt_2c9faafb916ff9ae1073 | ZOM-596 | cohort surface linear (device) | ● | unscoped | evidence |
| 305 | linear.linear_comments | cmt_fcdf3cfe923580229ce0 | ZOM-597 | cohort surface linear (device) | ● | unscoped | evidence |
| 306 | linear.linear_comments | cmt_dc7ca8b47de8706b6e7c | ZOM-598 | cohort surface linear (device) | ● | unscoped | evidence |
| 307 | linear.linear_comments | cmt_368072ca42cef83bc753 | ZOM-599 | cohort surface linear (device) | ● | unscoped | evidence |
| 308 | linear.linear_comments | cmt_6e5dbe5a1e3408ca18af | ZOM-600 | cohort surface linear (device) | ● | unscoped | evidence |
| 309 | linear.linear_comments | cmt_3b3da016a7907cd3a406 | ZOM-601 | cohort surface linear (device) | ● | unscoped | evidence |
| 310 | linear.linear_comments | cmt_2d28c3f01afce9b8f2a5 | ZOM-602 | cohort surface linear (device) | ● | unscoped | evidence |
| 311 | linear.linear_comments | cmt_901f9584e12b9fcf5ef6 | ZOM-603 | cohort surface linear (device) | ● | unscoped | evidence |
| 312 | linear.linear_comments | cmt_2d39ffba4125a30149a6 | ZOM-604 | cohort surface linear (device) | ● | unscoped | evidence |
| 313 | linear.linear_comments | cmt_8f4f0a6c5740d2da442c | ZOM-605 | cohort surface linear (device) | ● | unscoped | evidence |
| 314 | linear.linear_comments | cmt_80f3b736b93db842d9ee | ZOM-606 | cohort surface linear (device) | ● | unscoped | evidence |
| 315 | linear.linear_comments | cmt_140ae232fd10cb7bd0e5 | ZOM-607 | cohort surface linear (device) | ● | unscoped | evidence |
| 316 | linear.linear_comments | cmt_ee0bccdedf204bba142a | ZOM-608 | cohort surface linear (device) | ● | unscoped | evidence |
| 317 | linear.linear_comments | cmt_c8685c9d39e8c142912d | ZOM-609 | cohort surface linear (device) | ● | unscoped | evidence |
| 318 | linear.linear_comments | cmt_25c86515f142c86c514e | ZOM-610 | cohort surface linear (device) | ● | unscoped | evidence |
| 319 | linear.linear_comments | cmt_3f0be198f8b4083e21b8 | ZOM-611 | cohort surface linear (device) | ● | unscoped | evidence |
| 320 | linear.linear_comments | cmt_ebd304f3e16dd18dcc77 | ZOM-612 | cohort surface linear (device) | ● | unscoped | evidence |
| 321 | linear.linear_comments | cmt_0144e95b01944398c899 | ZOM-613 | cohort surface linear (device) | ● | unscoped | evidence |
| 322 | linear.linear_comments | cmt_8ec3c656b8cb40d1f7e4 | ZOM-614 | cohort surface linear (device) | ● | unscoped | evidence |
| 323 | linear.linear_comments | cmt_12e8cc55dc1f99b6eb35 | ZOM-615 | cohort surface linear (device) | ● | unscoped | evidence |
| 324 | linear.linear_comments | cmt_c17ddf58226b9cbd5513 | ZOM-616 | cohort surface linear (device) | ● | unscoped | evidence |
| 325 | linear.linear_comments | cmt_2fc57ad10098532b469d | ZOM-617 | cohort surface linear (device) | ● | unscoped | evidence |
| 326 | linear.linear_comments | cmt_66a9a23181dbd441b416 | ZOM-618 | cohort surface linear (device) | ● | unscoped | evidence |
| 327 | linear.linear_comments | cmt_d5c24e9c8f2578eaaaf4 | ZOM-619 | cohort surface linear (device) | ● | unscoped | evidence |
| 328 | linear.linear_comments | cmt_f2c392898a98833cdab0 | ZOM-620 | cohort surface linear (device) | ● | unscoped | evidence |
| 329 | linear.linear_comments | cmt_6f38c428866cecfeae70 | ZOM-621 | cohort surface linear (device) | ● | unscoped | evidence |
| 330 | linear.linear_comments | cmt_47d14bebf67205c792d5 | ZOM-622 | cohort surface linear (device) | ● | unscoped | evidence |
| 331 | linear.linear_comments | cmt_3b6ab6678b8aed457911 | ZOM-623 | cohort surface linear (device) | ● | unscoped | evidence |
| 332 | linear.linear_comments | cmt_6337dbdf51f3e1d85dab | ZOM-624 | cohort surface linear (device) | ● | unscoped | evidence |
| 333 | linear.linear_comments | cmt_c282b81fbbd8e523a68f | ZOM-625 | cohort surface linear (device) | ● | unscoped | evidence |
| 334 | linear.linear_comments | cmt_a8e3d490e505b21d5e8c | ZOM-626 | cohort surface linear (device) | ● | unscoped | evidence |
| 335 | linear.linear_comments | cmt_70b946c43606113d21ff | ZOM-627 | cohort surface linear (device) | ● | unscoped | evidence |
| 336 | github.github_reviews | harmonygames-Games/match3d#476#rev_3 | harmonygames-Games/match3d#476 | T-K3 | ● | unscoped | companion |
| 337 | github.github_review_comments | harmonygames-Games/match3d#476#rc_27 | harmonygames-Games/match3d#476 | F-LIMIT,T-K3 | ● | unscoped | overturning |
| 338 | github.github_pull_requests (UPDATE) | harmonygames-Games/match3d#476 | companion | counters / updated_at | ● | as parent | connecting |
| 339 | trello.trello_cards | 68dc0acf1815df76ed9b887d | 6851a6569f3bf818760632ab | F-MEMO | ● | unscoped | destination |
| 340 | trello.trello_actions | 68dc0acf5d1c8e7ab2f04c19 | 6851a6569f3bf818760632ab | F-MEMO companion | ● | unscoped | destination |
| 341 | slack.slack_messages | C090N54TG79/1758553214.330914 | C090N54TG79 | F-AGE | ● | member | evidence |
| 342 | slack.slack_messages | C090N54TG79/1758554405.774120 | C090N54TG79 | F-AGE | ● | member | evidence |
| 343 | slack.slack_messages | C0880U9751A/1758555040.262718 | C0880U9751A | R0_relay | ● | member | evidence |
| 344 | slack.slack_messages | D076RBM29JS/1758658884.207315 | D076RBM29JS | mirror | ● | member | evidence |
| 345 | slack.slack_messages | D076RBM29JS/1758659012.418207 | D076RBM29JS | T-K4 | ● | member | evidence |
| 346 | slack.slack_messages | C090N54TG79/1758728411.540327 | C090N54TG79 | F-GATE | ● | member | evidence |
| 347 | slack.slack_messages | C090N54TG79/1758729919.603185 | C090N54TG79 | F-PANELDEF,T-PANEL | ● | member | evidence |
| 348 | slack.slack_messages | C090N54TG79/1758733233.117446 | C090N54TG79 | F-INDUSTRY | ● | member | evidence |
| 349 | slack.slack_messages | C090N54TG79/1758819934.612483 | C090N54TG79 | T-K5 | ● | member | evidence |
| 350 | slack.slack_messages | D05GU6L0XFH/1758913471.205816 | D05GU6L0XFH | F-RERUN,T-F | ● | member | evidence |
| 351 | slack.slack_messages | C090N54TG79/1759167008.881274 | C090N54TG79 | F-RET,T-RET | ● | member | evidence |
| 352 | slack.slack_messages | C090N54TG79/1759266627.418203 | C090N54TG79 | ask | ● | member | evidence |
| 353 | slack.slack_messages | C093LEZGF6J/1759263026.184402 | C093LEZGF6J | mirror_rc27 | ● | member | evidence |
| 354 | slack.slack_messages (UPDATE) | c53936d63c93c8ffa0ad1e99526cad73 | companion | counters / updated_at | ● | as parent | connecting |
| 355 | slack.slack_messages (UPDATE) | e6a91393854458ad70331ef478952136 | companion | counters / updated_at | ● | as parent | connecting |
| 356 | slack.slack_messages (UPDATE) | D05GU6L0XFH/1758901945.292269 | companion | counters / updated_at | ● | as parent | connecting |
| 357 | slack.slack_messages (UPDATE) | 637fc98bc66d41b104fe243006fdcf98 | companion | counters / updated_at | ● | as parent | connecting |

## Findability and discovery-order proofs

```
Record:              gdocs.docs_documents · f_748d26e760e54651eaa0d8
Agent's likely query: "stability gate" via gdocs search
Term present:        NEW TERM; 0 base hits
Competing base hits: 0; the title is unique
Chain position:      connecting; named by title in C090N54TG79/1758728411.540327
```
```
Record:              gslides.slides_presentations · f_a087f049d271e9aa9f567f
Agent's likely query: "audience read criteria" via gslides or gdrive search
Term present:        NEW TERM; 0 base hits
Competing base hits: 0
Chain position:      connecting; the ask names it by what it governs
```
```
Record:              gmail.gmail_messages · julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com>
Agent's likely query: "Playtest results" via gmail search
Term present:        subject carries it
Competing base hits: Julia's mailbox holds no other copy
Chain position:      terminal for R10
```
```
Record:              gmail.gmail_messages · julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>
Agent's likely query: listing Julia's mail after Sep 17, or from:claire
Term present:        subject `a small thing from Friday`
Competing base hits: 18 seeded mails sit together; form mail shares the sender
Chain position:      terminal for R1
```
```
Record:              github.github_review_comments · harmonygames-Games/match3d#476#rc_27
Agent's likely query: PR search for Vision Bot, then the inline comments of harmonygames-Games/match3d#476
Term present:        `no phone in the loop` on the job's file
Competing base hits: 26 base review comments on the PR, B03
Chain position:      terminal for R2
```
```
Record:              slack.slack_messages · C090N54TG79/1758819934.612483
Agent's likely query: thread replies under C090N54TG79/1758581651.167799, or "1943" via slack search
Term present:        1943 present; the #builds post is a second fair path
Competing base hits: C05433XK267/1758575557.575349
Chain position:      terminal for R3
```
```
Record:              slack.slack_messages · D076RBM29JS/1758659012.418207
Agent's likely query: history of D076RBM29JS, or "Kadıköy" via slack search
Term present:        the nickname is shared with 9 notes Docs
Competing base hits: 0 base hits for the nickname
Chain position:      terminal for R4
```
```
Record:              slack.slack_messages · D05GU6L0XFH/1758913471.205816
Agent's likely query: Robert's DM with Julia, replies under D05GU6L0XFH/1758901945.292269
Term present:        `re-run note`
Competing base hits: off-topic root, one reply in base
Chain position:      terminal for R8
```
```
Record:              trello.trello_cards · 68dc0acf1815df76ed9b887d
Agent's likely query: "audience read" via trello search on ZM ROADMAP
Term present:        NEW TERM
Competing base hits: no card on the board mentions it
Chain position:      connecting for R12 and R13
```

| Dynamic-change seed | Claim met first | Overturned by | Why met first | Why decisive |
|---|---|---|---|---|
| T-K3 | cmt_38b3cc50dceda37f40f5 at 2025-09-30T16:50:22Z | harmonygames-Games/match3d#476#rc_27 at 2025-09-30T20:10:26Z | the Done ticket and owner's line are met in Linear with the session tickets; the PR note needs an inline-comment read on a PR no ticket names | Arthur Blake's inline note on the file the job runs says the pass comes from editor play mode with no phone involved |
| T-K1 | julia.lawson@harmonygames.co/<CAefcc9dd45170efad4834318d398795bc1db8@mail.gmail.com> at 2025-09-26T21:00:12Z | julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com> at 2025-09-29T10:02:47Z | the log, ticket and form tie out first; the mail shares no vocabulary with the form mails | Claire's Sep 29 mail states what she did before the group played; tickets are a Sep 30 batch transcription of the Sep 26 form, so the mail is the later source |
| T-K4 | f_524278b67bfa30dde78699 at 2025-09-23T09:05:00Z | 246d6f4a90620e5dafbb06068f450e46 at 2025-09-23T20:23:32Z | the Doc is found through the log and Drive; the DM line sits in a Turkish working chat with no shared keyword | Brian's later Turkish line in his DM with Julia says Kadıköy ekibi, the nickname on his Docs, works in games |
| T-K5 | julia.lawson@harmonygames.co/<CA01dc2d92371c7bfa63e451026f81fffed801@mail.gmail.com> at 2025-09-23T22:14:09Z | d7122186e361aa99778c65cb1502759d at 2025-09-25T17:05:34Z | channel reads return parents only; the reply sits under a root the ask does not name | Leonard's thread reply says build 1943 never went through a store, so the store-builds clause applies |
| T-PANEL | C090N54TG79/1758517286.431379 at 2025-09-22T05:01:26Z | julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com> at 2025-09-22T09:14:06Z | on the named path | the forward states one rating void with its reason, and Leonard's panel reply takes a void out of both sum and count |
| T-AUD | gdocs: data.json /docs_documents/328 at 2025-06-19T20:29:04Z | f_a087f049d271e9aa9f567f at 2025-09-24T17:20:00Z | a Docs search for audience returns the GDD; the criteria sit in a deck | the note widens the audience to casual and/or RPG adults, and the audience read criteria deck fixes one label per session and the lead test |
| T-RET | f_4e21b203a62910bdae0353 at 2025-09-24T11:15:08Z | 2ca968ace3e14d1a34c535f8a5c0cd6e at 2025-09-29T17:30:08Z | the KPI tab is a one-call answer in a Sheet shared with Julia | Robert's channel post after Vincent's retention post sets install weighting over mature cohorts, computed from USER_COHORT_RETENTION |

| Hidden authority | Search for its name | Decoy and clause |
|---|---|---|
| H-GATE ZM session stability gate | "stability gate" reaches f_748d26e760e54651eaa0d8 | gdocs: data.json /docs_documents/346, page_qa_runbook: {"dimension": "team", "decoy": "QA team's release checks for store submissions", "task": "product team's friend-session device clearance"} |
| H-AUD ZM audience read criteria | "audience read criteria" reaches f_a087f049d271e9aa9f567f | gdocs: data.json /docs_documents/328: "older entry of a trap version_records" |
| H-PANEL the panel results forward | "Playtest results for Puzzles vs. Zombies" reaches julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com> | C090N54TG79/1758517286.431379: "older entry of a trap version_records" |

## Self-validation table

| QC category | Tool-enforced | Manual evidence |
|---|---|---|
| Missing Universe Data | - | every needed fact exists and is readable (1.E check-sql PASS); write tools listed in design section 10; retention rows read through hg.py, snowflake.USER_COHORT_RETENTION |
| Temporal Field | sql_lint, base_check PASS | gate Doc dated Sep 24 after Bot #8; run #15 Sep 25; no record cites a later one: C090N54TG79/1758728411.540327 follows f_748d26e760e54651eaa0d8; ticket batch Sep 30 after every form |
| Cross-service Referential | base_check Check A PASS | names spelled as in the base; harmonygames-Games/match3d#476#rc_27 on PR harmonygames-Games/match3d#476; mirror text equals the comment |
| Quantitative / Reconciliation | Slack counters updated (4 UPDATEs); Trello badges | log, tickets and Docs tie 60 for 60 (solver reads all three shapes); panel 3.33, retention 9.09, KPI 8.63 recomputed in solver/truth.json; KPI sheet f_4e21b203a62910bdae0353 |
| State / Lifecycle | base_check PASS | ZOM-567 Done with completed_at; comment before close; session tickets Todo; ZOM-559 untouched |
| Identifier / Format | sql_lint PASS | ids per scheme; sender copies carry the same Message-ID as julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com> |
| Semantic / Category | - | Puzzles vs. Zombies dual naming listed for the human (julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com>); board list Backlog fits 68dc0acf1815df76ed9b887d |
| Other | - | voice per 1.C; no record states a total or the call; C090N54TG79/1759266627.418203 states only the mapping |

## Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| slack | INT-22 | mail notices | None seeded; optional. Four roots get counter updates: C090N54TG79/1758691397.679889, C090N54TG79/1758581651.167799, D05GU6L0XFH/1758901945.292269 and C093LEZGF6J/1759258475.735779. The note and Vincent's post stay thread-less (design_delta) |
| gmail | none | gmail: none, no integration has Gmail as its source | Human mail. 17 sender copies with the Message-ID of Julia's copy, e.g. julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>; the forward keeps Leonard's vendor copy (Q10) |
| gcal | INT-11 | invitation mail | Not seeded, no_notify: evt_da65644831bc088267263d and Claire's copy evt_960936eab424f7726db95c in integration_exceptions |
| gdrive | INT-13 | Drive app DMs | None; DM-only and optional. Drive rows mirror each seeded Doc and Sheet, e.g. f_748d26e760e54651eaa0d8 |
| gdocs | none | gdocs: none in the KB | Each seeded Doc has its Drive row and sharing, e.g. f_c691d577b8f837eb4f9eaa |
| gsheets | none | gsheets: none in the KB | Drive row seeded with f_43bc35baf77fd59f4e57b8 and f_4e21b203a62910bdae0353 |
| gslides | none | gslides: none in the KB | Drive row seeded with f_a087f049d271e9aa9f567f |
| github | INT-01, INT-23 | #zombie-prs copy of rc_27 | Seeded under C093LEZGF6J/1759258475.735779 (root reply_count 30); the CodeRabbit reply rc_28 and its mirror are removed in rev2 (review M3); rev_3 in integration_exceptions citing harmonygames-Games/match3d#470#rev_3; rev_4 not seeded (design_delta) |
| github | INT-02, INT-12 | push posts, notification mail | None: no push seeded; mail optional (harmonygames-Games/match3d#476) |
| linear | INT-03 | linear[bot] on PRs that name a key | None: no seeded PR and ZOM-567 is named by no PR |
| linear | INT-04, INT-05 | Slack notices, digest mail | None: not every transition is posted (C0880U9751A/1759236043.004679 is one that was) |
| trello | INT-21 | no Trello bot exists | No Slack post. 68dc0acf1815df76ed9b887d, createCard action and dateLastActivity agree (T06) |
| snowflake | none | snowflake: none, read only | snowflake.USER_COHORT_RETENTION stays base |
| confluence | none | confluence: none, not injected | page_qa_runbook stays as it is |

## Touched-data census and coherence hazards

Matched against `references/universe_kb/coherence_hazards.json`. `hardness_gate` `hazard_scope` reports 0 pre-existing hazards among task-touched records.

| Touched base record | Why a correct run opens it | Hazard id | Disposition |
|---|---|---|---|
| C090N54TG79/1758517286.431379 | the note: rule hub | S03 semantic; R04 referential | one label per session settled by the deck; pointer by title, no constructed link |
| C090N54TG79/1758581651.167799 | K5 root | Q01 quantitative | counters bumped to 16 and 3; latest_reply set |
| C090N54TG79/1758691397.679889 | panel definition root | Q02 quantitative | counters bumped to 3 |
| D05GU6L0XFH/1758901945.292269 | F root, raw-shape row | I01 identifier; I02 identifier | UPDATE keyed on channel and ts; sql_lint warning dispositioned |
| harmonygames-Games/match3d#476 | K3 home | T01 temporal; L09 lifecycle; I07 identifier | undated rows neither modified nor cited; PR stays open; never called merged; author token kept |
| C05433XK267/1758803475.436309 | run #15 | L04 lifecycle | ZOM-567 is referenced by no PR, so L04 does not arise (excluded) |
| ZOM-559 | Samsung bug | L03 lifecycle | stays Todo; no seeded fix |
| evt_f08d0e87c8c7aafe580d42 | Julia's calendar neighbour | Q11 quantitative; R08 referential | base copies untouched; seeded event one row per attendee, no invite mail |
| C090N54TG79/1759176983.189479 | the lean, T-LEAN | semantic: S04 first names | no seed depends on it |
| C090N54TG79/1759171957.791499 | the Sep 29 change | temporal: none beyond T02 on the panel mail | no order claim on the panel thread |
| harmonygames-Games/match3d#466 | T-466 distractor | L10 lifecycle | different change; not cited by any seed |
| f_89fadbc54660c9881d8cf9 | older GDD, T-AUD | semantic: none in scope beyond S03 | older version in version_records |
| page_qa_runbook | H-GATE decoy scope | referential: none in scope | not injected |
| snowflake.USER_COHORT_RETENTION | retention rule | quantitative: none in scope | 51 ZM rows, 47 with a D14 figure; SC-1 family untouched |

Hazard ids by category: temporal T01, T02, T06; semantic S03, S04; referential R01, R03, R04, R06, R07, R08; quantitative Q01, Q02, Q03, Q10, Q11; lifecycle L03, L04, L06, L08, L09, L10; identifier I01, I02, I03, I04, I07, I08, I10, I11, I13, I14, I15, I17. Manifest `hazard_acknowledgements`: T01, L04, Q11, all `excluded`, verified: no statement in the SQL touches those records (5 UPDATEs listed in the ledger). Cards from `known_data_issues/synthcut.md` are dispositioned in design section 1a; SC-8 keeps ZOM-475 out of every rule.

Sibling sweep (design 1a, not repeated): Linear "samsung" hits ENG-1431, ENG-2285, ENG-2324, ENG-383 and ZOM-559; ENG-2324 is Done on the other team's board and no seed cites it.

## Intended disagreements

| Disagreement | Why realistic | Resolved by |
|---|---|---|
| cmt_38b3cc50dceda37f40f5 says run #15 covers the gate; harmonygames-Games/match3d#476#rc_27 says no phone in the loop | a QA owner reads a green job as coverage; the job's owner limits it later the same day | f_748d26e760e54651eaa0d8: a pass covers a device only if it ran on that device |
| julia.lawson@harmonygames.co/<CAefcc9dd45170efad4834318d398795bc1db8@mail.gmail.com> says no coaching; julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com> says she took them through the game first | a friend owns up later in a private mail | same author, later date; tickets only transcribe the form |
| f_524278b67bfa30dde78699 clean label; D076RBM29JS/1758659012.418207 says the group works in games | the forgotten detail comes later in a DM | same author, later, and C090N54TG79/1758733233.117446 |
| julia.lawson@harmonygames.co/<CA01dc2d92371c7bfa63e451026f81fffed801@mail.gmail.com> complete form; C090N54TG79/1758819934.612483 says build 1943 never went through a store | testers pass builds around | Leonard wrote the clause in f_748d26e760e54651eaa0d8; C05433XK267/1758575557.575349 is a non-Submission job |
| f_4e21b203a62910bdae0353 8.63 simple mean; C090N54TG79/1759167008.881274 sets install-weighted | a Sep 24 snapshot predates the rule | newer rule; 9.09 from snowflake.USER_COHORT_RETENTION |
| C090N54TG79/1758517286.431379 panel 3-3.5; julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com> per-player stars with one void | a headline against detail | C090N54TG79/1758729919.603185 |
| f_89fadbc54660c9881d8cf9 male RPG target; f_a087f049d271e9aa9f567f sessions decide | an older GDD | later records, in version_records of T-AUD |

## Constraints for the prompt brief

| Anchor | May be named (noun phrases only) | Record |
|---|---|---|
| A1 | Leonard's feedback note | C090N54TG79/1758517286.431379 |
| A2 | Leonard's keep-or-hold message | C090N54TG79/1759266627.418203 |
| A3 | audience sessions workbook | f_43bc35baf77fd59f4e57b8 |

Never named in the prompt: locations of the hidden authorities, ids, the words valid or audit, any exclusion or root cause (f_748d26e760e54651eaa0d8, f_a087f049d271e9aa9f567f, harmonygames-Games/match3d#476#rc_27). Deadlines: none in a seed. Deliverable kinds: register in f_43bc35baf77fd59f4e57b8, memo in d_8140f09bf9f1b94cb8ee2d, reply in the thread of C090N54TG79/1759266627.418203, 60 state writes on ZOM-568 to ZOM-627, re-run notes, a message to Brian in C090N54TG79. The ask wording now reads "the rules I posted in the channel after my note".

## Fact sheet

| Key | Value | Kind | Must appear in / home ids |
|---|---|---|---|
| Vision Bot run | #15 | id | C090N54TG79/1758517286.431379 |
| ZOM-559 | Todo | status | C090N54TG79/1758517286.431379 |
| non-store build | 1943 | id | f_4ceb107c67c8348b1df02b, f_b96fd720b7d4010291329c, f_f575437ac7c498de7e1db9 and 11 more (rev7 adds f_41675dd5d215cf647b240e, f_e055f907c7c1359b39bec5, f_ba6a734ddf36318e9bb3f3) |
| Kadıköy ekibi | Kadıköy ekibi | id | f_524278b67bfa30dde78699, f_b66d5288a6d3ca9d4d03b6, f_8dab41c358ba484acad83d and 8 more |
| editor play mode limit | no phone in the loop | status | harmonygames-Games/match3d#476#rc_27, 37d66469c43368f08befb2d6bf0c8d28 |
| tie band | 0.25 | amount | f_a087f049d271e9aa9f567f |
| device of ZOM-587 | Galaxy S24 | id | cmt_407f6362d41c55550dc7 |
| device of ZOM-588 | SM-A546E | id | cmt_151b207651e5ca7a56e8, f_cadae9f611d82d56ac02c3 (the QA matrix row) |
| device of ZOM-590 | SM-S921B | id | cmt_ad47d5d01226c9a60bd9 |
| device of ZOM-591 | Galaxy S23 FE | id | cmt_474825ce59c2f800f5a7 |
| device of ZOM-593 | Galaxy A54 | id | cmt_a3a8a262de70dc320ae5 |
| device of ZOM-594 | Galaxy S22 | id | cmt_1bb6794c75bc21bcafae |
| device of ZOM-596 | Galaxy A15 | id | cmt_2c9faafb916ff9ae1073 |
| device of ZOM-601 | Galaxy A35 | id | cmt_3b3da016a7907cd3a406 |
| device of ZOM-603 | SM-A346E | id | cmt_901f9584e12b9fcf5ef6 |
| device of ZOM-606 | SM-S911B | id | cmt_80f3b736b93db842d9ee |
| device of ZOM-620 | SM-A155F | id | cmt_f2c392898a98833cdab0 |
| job of Alper Koçak | QA tester, console games publisher | status | 038b5eb5a30326895cb54756 |
| job of Arda Keskin | Live ops producer, mobile games studio | status | 0810fb8287e489c125fe2cd9 |
| retention cut-off | 2025-07-24 | date | f_4e21b203a62910bdae0353 |

`python3 Task_Authoring/tools/fact_check.py Task_Authoring/task_inputs/01_Universe_Inject.sql --manifest Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.json --no-leak` (verbatim):

```text
FACT CHECK: PASS — 403 text-bearing rows, 20 declared facts, 10 declared superseded records
Errors: none
Warnings (10):
  line 201: gdocs.docs_documents f_739d61e4b5cb2ed69db3d5: [inactive_person_named] names Thomas, inactive at the record's time: 2025-09-23 is after Thomas's departure signal (last authored activity 2025-05-05, status quiet_since_2025-05; activity.json)
  line 229: gdocs.docs_documents f_a7950c7698ff9b933a6a7b: [inactive_person_named] names Matthew Collins, inactive at the record's time: Matthew Collins has no authored activity within ±60 days of 2025-09-25 (status no_authored_activity; activity.json monthly_authored_total) — implausible voice
  line 245: gdocs.docs_documents f_4da421425634258e986f3c: [inactive_person_named] names Peter Lawson, inactive at the record's time: Peter Lawson has no authored activity within ±60 days of 2025-09-26 (status no_authored_activity; activity.json monthly_authored_total) — implausible voice
  line 265: gdocs.docs_documents f_15e5a2e226ab3e8994c970: [inactive_person_named] names rachel, inactive at the record's time: 2025-09-26 is after rachel's departure signal (last authored activity 2024-09-22, status quiet_since_2024-09; activity.json)
  line 275: gdocs.docs_documents f_24937bdfc5070d08168595: [inactive_person_named] names George Miller, inactive at the record's time: 2025-09-26 is after George Miller's departure signal (last authored activity 2025-07-07, status quiet_since_2025-07; activity.json)
  line 315: gdocs.docs_documents f_e055f907c7c1359b39bec5: [inactive_person_named] names Nathan Price, inactive at the record's time: 2025-09-28 is after Nathan Price's departure signal (last authored activity 2024-07-19, status quiet_since_2024-07; activity.json)
  line 201: gdocs.docs_documents f_739d61e4b5cb2ed69db3d5: [ambiguous_name] bare first name 'Thomas' matches several roster entities (Thomas Baker <thomas.baker@harmonygames.co>; Thomas <thomas@harmonygames.co> [persona thomas]) — use the full name or a <@mention>; 1 row(s) (e.g. lines 201)
  line 361: gcal.gcal_events evt_960936eab424f7726db95c: [ambiguous_name] bare first name 'Claire' matches several roster entities (Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]; Claire <github:PERSON_2360_GITHUB_USERNAME>) — use the full name or a <@mention>; 4 row(s) (e.g. lines 361, 363, 507, 511)
  line 415: gmail.gmail_messages julia.lawson@harmonygames.co/<CA5f548a065eb5efb9731cb60c737492aaf209@mail.gmail.com>: [ambiguous_name] bare first name 'Marcus' matches several roster entities (Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]; Marcus Lee <marcus.lee@harmonygames.co>; Marcus <trello:c48a210d5c5a4b59231c6873>) — use the full name or a <@mention>; 4 row(s) (e.g. lines 415, 419, 499, 503)
  line 491: gmail.gmail_messages julia.lawson@harmonygames.co/<CA14bc4b41e4b7d4884c51819b961e5ebbc954@mail.gmail.com>: [ambiguous_name] bare first name 'Martin' matches several roster entities (Martin Lewis <PERSON_0394_EMAIL>; Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]) — use the full name or a <@mention>; 2 row(s) (e.g. lines 491, 495)
```

## Facts for the human

| Locator | Base / seeded | Fact | Reach | Role | Re-verify |
|---|---|---|---|---|---|
| C090N54TG79/1758517286.431379 | base | the note: No coaching, 25–45, ask for friends' reactions | member | authority | no |
| C090N54TG79/1759266627.418203 | seeded | Leonard's ask, Sep 30 21:10:27Z: casual lead hold, RPG lead keep, no clear lead keep | member | write target thread | no |
| C090N54TG79/1758554405.774120 | seeded | 25–45 is an age band | member | evidence | no |
| C090N54TG79/1758733233.117446 | seeded | game-industry people don't count | member | authority | no |
| C090N54TG79/1758728411.540327 | seeded | names the gate Doc by title | member | connecting | no |
| f_748d26e760e54651eaa0d8 | seeded | Samsung is the one group; a pass covers a device only if it ran on it; dev builds do not count | shared with Julia | authority | no |
| f_a087f049d271e9aa9f567f | seeded | observer's label stands; higher mean; at least 6; gap under 0.25 is no clear lead | owner | authority | element text ○ no; ● yes |
| f_c691d577b8f837eb4f9eaa | seeded | counted to Done, not counted to Canceled | owner | authority | no |
| f_43bc35baf77fd59f4e57b8 | seeded | Log 60 rows, Register header | owner | write target | no |
| f_4e21b203a62910bdae0353 | seeded | KPI D7 mean 8.63 over 45 rows | shared with Julia | claim met first | no |
| C090N54TG79/1759167008.881274 | seeded | install-weighted D7, cohorts with a D14 figure, both platforms | member | overturning evidence | no |
| C090N54TG79/1758729919.603185 | seeded | void leaves sum and count | member | authority | no |
| julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com> | seeded | ten ratings, player 8 void; 3.33 over 9 | Julia's mailbox | evidence | no |
| julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com> | seeded | Claire took them through the game before they played, Fri Sep 26, Sep 29 10:02:47Z | Julia's mailbox | overturning evidence | no |
| julia.lawson@harmonygames.co/<CAefcc9dd45170efad4834318d398795bc1db8@mail.gmail.com> | seeded | form: no coaching, Sep 26 21:00:12Z | Julia's mailbox | claim met first | no |
| julia.lawson@harmonygames.co/<CA8db5b364a9d7d3c1946e722aed490d591476@mail.gmail.com> | seeded | re-sent form, same sessions | Julia's mailbox | decoy | no |
| evt_da65644831bc088267263d | seeded | Friday at Claire's, Julia declined | Julia's calendar | evidence | gcal description ○ |
| D076RBM29JS/1758658884.207315 | seeded | Julia asks Brian in Turkish about the sessions he shared that morning (rev2) | member | connecting | no |
| D076RBM29JS/1758659012.418207 | seeded | Kadıköy ekibi works at mobile game companies, Sep 23 20:23:32Z | member | overturning evidence | no |
| C090N54TG79/1758819934.612483 | seeded | android 1943 never went through a store, Sep 25 17:05:34Z | member | overturning evidence | no |
| D05GU6L0XFH/1758913471.205816 | seeded | technical drops get a re-run note, others closed | member | authority | no |
| C05433XK267/1758803475.436309 | base | run #15 Success Sep 25 12:31Z on Blake/visionBot | member | evidence | no |
| C05433XK267/1758575557.575349 | base | Match3D Android #1943 main, a non-Submission job | member | alternate path | no |
| harmonygames-Games/match3d#476#rc_27 | seeded | pass comes from Unity editor play mode, no phone in the loop, Sep 30 20:10:26Z | unscoped | overturning evidence | no |
| cmt_38b3cc50dceda37f40f5 | seeded | Vincent: run #15 covers the device gate, Sep 30 16:50:22Z | unscoped | claim met first | linear comment render ● |
| ZOM-567 | seeded | Done Sep 30 17:10:05Z | unscoped | claim met first | no |
| ZOM-559 | base | Todo, no session blocker | unscoped | decoy | no |
| 68dc0acf1815df76ed9b887d | seeded | what the memo holds; memo goes in Julia's folder | unscoped | authority | no |
| d_8140f09bf9f1b94cb8ee2d | base | Julia's root folder | owner | write target | gdocs parent untested |
| snowflake.USER_COHORT_RETENTION | base | 51 ZM rows; 47 with D14; weighted D7 9.09 | unscoped | evidence | after regeneration |
| ZOM-568 | seeded | 2025-09-22 Brian Foster RPG 5 on iPhone 15, 0.3.38 (38), age 35, Kadıköy ekibi: notcounted (game_industry); Doc f_524278b67bfa30dde78699, comment cmt_2fbcaf2d990d8b4e9c0d | unscoped ticket, shared Doc | evidence | no |
| ZOM-569 | seeded | 2025-09-22 Brian Foster RPG 5 on iPhone 14, 0.3.38 (38), age 30, Kadıköy ekibi: notcounted (game_industry); Doc f_b66d5288a6d3ca9d4d03b6, comment cmt_d8dfed654b254845d39d | unscoped ticket, shared Doc | evidence | no |
| ZOM-570 | seeded | 2025-09-22 Brian Foster RPG 4 on iPhone 13, 0.3.38 (38), age 39, Kadıköy ekibi: notcounted (game_industry); Doc f_8dab41c358ba484acad83d, comment cmt_0fb1505315140ffd0b21 | unscoped ticket, shared Doc | evidence | no |
| ZOM-571 | seeded | 2025-09-22 Brian Foster RPG 5 on iPhone 13, 0.3.38 (38), age 44, Kadıköy ekibi: notcounted (game_industry); Doc f_abf945213ee8762fbdc083, comment cmt_3daaaa1034994aa4ffbb | unscoped ticket, shared Doc | evidence | no |
| ZOM-572 | seeded | 2025-09-22 Brian Foster RPG 5 on iPhone 15, 0.3.38 (38), age 39, Kadıköy ekibi: notcounted (game_industry); Doc f_36b61fd6f9ef6ec45cf759, comment cmt_03bb699c2fc91f181b46 | unscoped ticket, shared Doc | evidence | no |
| ZOM-573 | seeded | 2025-09-22 Brian Foster RPG 4.5 on iPhone 14, 0.3.38 (38), age 33, Kadıköy ekibi: notcounted (game_industry); Doc f_548e4061239f8bbb1ebef1, comment cmt_a23a04387ca0198012f0 | unscoped ticket, shared Doc | evidence | no |
| ZOM-574 | seeded | 2025-09-22 Brian Foster RPG 5 on iPhone 14, 0.3.38 (38), age 31, Kadıköy ekibi: notcounted (game_industry); Doc f_3ff040d3a2e345719d4a70, comment cmt_f08b62b7ca0d53c09c94 | unscoped ticket, shared Doc | evidence | no |
| ZOM-575 | seeded | 2025-09-22 Brian Foster RPG 5 on iPhone 12, 0.3.38 (38), age 44, Kadıköy ekibi: notcounted (game_industry); Doc f_70e9bf3f18b32fbce7c3d0, comment cmt_89f50d4a6e25a5a7484e | unscoped ticket, shared Doc | evidence | no |
| ZOM-576 | seeded | 2025-09-22 Brian Foster RPG 4.5 on iPhone 15, 0.3.38 (38), age 35, Kadıköy ekibi: notcounted (game_industry); Doc f_cff26f47141203716f669b, comment cmt_fd248e7d92637605e02e | unscoped ticket, shared Doc | evidence | no |
| ZOM-577 | seeded | 2025-09-23 Robert casual 2 on Pixel 7, 0.3.127 (1943), age 37, neighbor: notcounted (build), re-run note; Doc f_4ceb107c67c8348b1df02b, comment cmt_738ed1f9acdb089b1f75 | unscoped ticket, shared Doc | evidence | no |
| ZOM-578 | seeded | 2025-09-23 Robert casual 2.5 on Redmi Note 12, 0.3.127 (1943), age 28, friend: notcounted (build), re-run note; Doc f_b96fd720b7d4010291329c, comment cmt_40f8d5b92e1a26b261a3 | unscoped ticket, shared Doc | evidence | no |
| ZOM-579 | seeded | 2025-09-23 Robert casual 3 on OnePlus 11, 0.3.127 (1943), age 31, friend: notcounted (build), re-run note; Doc f_f575437ac7c498de7e1db9, comment cmt_a7b07495c1aa4e6f0325 | unscoped ticket, shared Doc | evidence | no |
| ZOM-580 | seeded | 2025-09-23 Robert casual 2.5 on Pixel 6a, 0.3.127 (1943), age 40, classmate: notcounted (build), re-run note; Doc f_739d61e4b5cb2ed69db3d5, comment cmt_fdba422386d3746eb52a | unscoped ticket, shared Doc | evidence | no |
| ZOM-581 | seeded | 2025-09-23 Robert casual 2 on Redmi 12, 0.3.127 (1943), age 35, friend: notcounted (build), re-run note; Doc f_50d49b0baf64a424fb73a7, comment cmt_7c0c46fda16ac3f2ed1e | unscoped ticket, shared Doc | evidence | no |
| ZOM-582 | seeded | 2025-09-23 Robert casual 2 on Pixel 8, 0.3.127 (1943), age 45, friend: notcounted (build), re-run note; Doc f_fca92e85c34b7b0d6f950b, comment cmt_21840da3225e5fc1302b | unscoped ticket, shared Doc | evidence | no |
| ZOM-583 | seeded | 2025-09-23 Robert casual 2.5 on OnePlus Nord 3, 0.3.127 (1943), age 40, friend: notcounted (build), re-run note; Doc f_d4ac4049ba1892fd91a3bd, comment cmt_b3b84bb3817c87487559 | unscoped ticket, shared Doc | evidence | no |
| ZOM-584 | seeded | 2025-09-23 Robert casual 3.5 on Pixel 7a, 0.3.127 (1943), age 42, family: notcounted (build), re-run note; Doc f_28dcffa96acbd33e38ad20, comment cmt_4cf4070dd936b4f4b961 | unscoped ticket, shared Doc | evidence | no |
| ZOM-585 | seeded | 2025-09-23 Robert casual 2.5 on Redmi Note 13, 0.3.127 (1943), age 28, classmate: notcounted (build), re-run note; Doc f_69208de7d381dc75193b14, comment cmt_a5f7ecf05d2105d008cf | unscoped ticket, shared Doc | evidence | no |
| ZOM-586 | seeded | 2025-09-23 Robert casual 2 on Pixel 8a, 0.3.127 (1943), age 41, neighbor: notcounted (build), re-run note; Doc f_1bccd7e487171e17d051a5, comment cmt_1c3a1ff63f39fd874437 | unscoped ticket, shared Doc | evidence | no |
| ZOM-587 | seeded | 2025-09-23 Oliver Brooks casual 2 on Galaxy S24, 0.3.127 (127), age 31, neighbor: notcounted (device), re-run note; Doc f_860c5fa834dda962164827, comment cmt_407f6362d41c55550dc7 | unscoped ticket, shared Doc | evidence | no |
| ZOM-588 | seeded | 2025-09-23 Oliver Brooks casual 3 on SM-A546E, 0.3.127 (127), age 37, neighbor: notcounted (device), re-run note; Doc f_cfbab45acc997b0917321e, comment cmt_151b207651e5ca7a56e8 | unscoped ticket, shared Doc | evidence | no |
| ZOM-589 | seeded | 2025-09-23 Oliver Brooks RPG 3 on Pixel 7a, 0.3.127 (127), age 33, family: counted; Doc f_b00473df1ed377c7ea0a03, comment cmt_2a058d7206e0218dbc42 | unscoped ticket, shared Doc | evidence | no |
| ZOM-590 | seeded | 2025-09-24 Owen Baker casual 2 on SM-S921B, 0.3.127 (127), age 38, friend: notcounted (device), re-run note; Doc f_f96134888258f49bf9b411, comment cmt_ad47d5d01226c9a60bd9 | unscoped ticket, shared Doc | evidence | no |
| ZOM-591 | seeded | 2025-09-24 Owen Baker casual 2.5 on Galaxy S23 FE, 0.3.127 (127), age 30, neighbor: notcounted (device), re-run note; Doc f_7907038d6d8ec99a11f01b, comment cmt_474825ce59c2f800f5a7 | unscoped ticket, shared Doc | evidence | no |
| ZOM-592 | seeded | 2025-09-24 Owen Baker RPG 3.5 on iPhone 12, 0.3.40 (40), age 32, friend: counted; Doc f_a27c70f8af81a5cfe57b53, comment cmt_e8b9465adb7146c7e6db | unscoped ticket, shared Doc | evidence | no |
| ZOM-593 | seeded | 2025-09-24 Samuel Turner casual 2.5 on Galaxy A54, 0.3.127 (127), age 35, neighbor: notcounted (device), re-run note; Doc f_55f2f152df34be6a2ea5d6, comment cmt_a3a8a262de70dc320ae5 | unscoped ticket, shared Doc | evidence | no |
| ZOM-594 | seeded | 2025-09-24 Samuel Turner casual 3.5 on Galaxy S22, 0.3.127 (127), age 32, friend: notcounted (device), re-run note; Doc f_a7950c7698ff9b933a6a7b, comment cmt_1bb6794c75bc21bcafae | unscoped ticket, shared Doc | evidence | no |
| ZOM-595 | seeded | 2025-09-24 Samuel Turner casual 4 on OnePlus 11, 0.3.127 (127), age 33, friend: counted; Doc f_a4258d0113946c326f52d3, comment cmt_87b20b86cf6de56ee7e1 | unscoped ticket, shared Doc | evidence | no |
| ZOM-596 | seeded | 2025-09-25 Calvin Price casual 2.5 on Galaxy A15, 0.3.127 (127), age 34, family: notcounted (device), re-run note; Doc f_de4b874824c91335dfcb67, comment cmt_2c9faafb916ff9ae1073 | unscoped ticket, shared Doc | evidence | no |
| ZOM-597 | seeded | 2025-09-25 Calvin Price RPG 3 on Pixel 8, 0.3.127 (127), age 40, neighbor: counted; Doc f_75fe047f2040b34355f80a, comment cmt_fcdf3cfe923580229ce0 | unscoped ticket, shared Doc | evidence | no |
| ZOM-598 | seeded | 2025-09-25 Marcus Bennett RPG 3.5 on Pixel 8, 0.3.127 (127), age 42, friend: counted; Doc f_ffaa152d5c62e39d22cf94, comment cmt_dc7ca8b47de8706b6e7c | unscoped ticket, shared Doc | evidence | no |
| ZOM-599 | seeded | 2025-09-25 Marcus Bennett RPG 3.5 on iPhone 14, 0.3.40 (40), age 37, family: counted; Doc f_d9ac7d60efdb8fe313bb6c, comment cmt_368072ca42cef83bc753 | unscoped ticket, shared Doc | evidence | no |
| ZOM-600 | seeded | 2025-09-25 Marcus Bennett casual 4 on iPhone 13, 0.3.40 (40), age 25, family: counted; Doc f_e0843c039ea62e1a61179e, comment cmt_6e5dbe5a1e3408ca18af | unscoped ticket, shared Doc | evidence | no |
| ZOM-601 | seeded | 2025-09-25 Oliver Brooks casual 2 on Galaxy A35, 0.3.127 (127), age 32, family: notcounted (device), re-run note; Doc f_f44fee2ed41dd0b0311f41, comment cmt_3b3da016a7907cd3a406 | unscoped ticket, shared Doc | evidence | no |
| ZOM-602 | seeded | 2025-09-25 Oliver Brooks casual 4 on iPhone 14, 0.3.40 (40), age 38, friend: counted; Doc f_4da421425634258e986f3c, comment cmt_2d28c3f01afce9b8f2a5 | unscoped ticket, shared Doc | evidence | no |
| ZOM-603 | seeded | 2025-09-25 Owen Baker casual 2 on SM-A346E, 0.3.127 (127), age 35, family: notcounted (device), re-run note; Doc f_6b1f637c9012a167e0f466, comment cmt_901f9584e12b9fcf5ef6 | unscoped ticket, shared Doc | evidence | no |
| ZOM-604 | seeded | 2025-09-25 Owen Baker RPG 3.5 on iPhone 15, 0.3.40 (40), age 35, friend: counted; Doc f_e8018f6e1a4a46020dd321, comment cmt_2d39ffba4125a30149a6 | unscoped ticket, shared Doc | evidence | no |
| ZOM-605 | seeded | 2025-09-26 Samuel Turner casual 3.5 on iPhone 14, 0.3.40 (40), age 33, classmate: counted; Doc f_156ca006436f0ecac0ccec, comment cmt_8f4f0a6c5740d2da442c | unscoped ticket, shared Doc | evidence | no |
| ZOM-606 | seeded | 2025-09-26 Samuel Turner casual 2 on SM-S911B, 0.3.127 (127), age 29, family: notcounted (device), re-run note; Doc f_6996d570d484f6b4c0f989, comment cmt_80f3b736b93db842d9ee | unscoped ticket, shared Doc | evidence | no |
| ZOM-607 | seeded | 2025-09-26 Claire Morgan RPG 5 on iPhone 14, 0.3.40 (40), age 29, friend: notcounted (coached); Doc f_69dc1cbd43ec586d7db4d9, comment cmt_140ae232fd10cb7bd0e5 | unscoped ticket, shared Doc | evidence | no |
| ZOM-608 | seeded | 2025-09-26 Claire Morgan RPG 4 on Pixel 7, 0.3.127 (127), age 35, friend: notcounted (coached); Doc f_75130b3e7a11db61a4f6e4, comment cmt_ee0bccdedf204bba142a | unscoped ticket, shared Doc | evidence | no |
| ZOM-609 | seeded | 2025-09-26 Claire Morgan RPG 5 on iPhone 13, 0.3.40 (40), age 39, friend: notcounted (coached); Doc f_ef202456330445c2745977, comment cmt_c8685c9d39e8c142912d | unscoped ticket, shared Doc | evidence | no |
| ZOM-610 | seeded | 2025-09-26 Claire Morgan RPG 4.5 on iPhone 15, 0.3.40 (40), age 45, friend: notcounted (coached); Doc f_e295aa601d92bf76146caf, comment cmt_25c86515f142c86c514e | unscoped ticket, shared Doc | evidence | no |
| ZOM-611 | seeded | 2025-09-26 Claire Morgan RPG 5 on Redmi Note 12, 0.3.127 (127), age 39, friend: notcounted (coached); Doc f_898157c507a362a053135a, comment cmt_3f0be198f8b4083e21b8 | unscoped ticket, shared Doc | evidence | no |
| ZOM-612 | seeded | 2025-09-26 Claire Morgan RPG 4.5 on iPhone 13, 0.3.40 (40), age 42, friend: notcounted (coached); Doc f_15e5a2e226ab3e8994c970, comment cmt_ebd304f3e16dd18dcc77 | unscoped ticket, shared Doc | evidence | no |
| ZOM-613 | seeded | 2025-09-26 Claire Morgan RPG 5 on Pixel 8, 0.3.127 (127), age 33, friend: notcounted (coached); Doc f_fbbd9f849a298efec6f7ae, comment cmt_0144e95b01944398c899 | unscoped ticket, shared Doc | evidence | no |
| ZOM-614 | seeded | 2025-09-26 Claire Morgan RPG 4 on iPhone 14, 0.3.40 (40), age 33, friend: notcounted (coached); Doc f_43d2aee7be6a4c16d9ee95, comment cmt_8ec3c656b8cb40d1f7e4 | unscoped ticket, shared Doc | evidence | no |
| ZOM-615 | seeded | 2025-09-26 Claire Morgan RPG 5 on OnePlus 11, 0.3.127 (127), age 41, friend: notcounted (coached); Doc f_18a8a68476130a03866485, comment cmt_12e8cc55dc1f99b6eb35 | unscoped ticket, shared Doc | evidence | no |
| ZOM-616 | seeded | 2025-09-26 Claire Morgan RPG 4.5 on iPhone 12, 0.3.40 (40), age 44, friend: notcounted (coached); Doc f_61c51adfb98b4dfa709abc, comment cmt_c17ddf58226b9cbd5513 | unscoped ticket, shared Doc | evidence | no |
| ZOM-617 | seeded | 2025-09-26 Claire Morgan RPG 4.5 on iPhone 15, 0.3.40 (40), age 42, friend: notcounted (coached); Doc f_24937bdfc5070d08168595, comment cmt_2fc57ad10098532b469d | unscoped ticket, shared Doc | evidence | no |
| ZOM-618 | seeded | 2025-09-26 Claire Morgan RPG 5 on Pixel 7a, 0.3.127 (127), age 40, friend: notcounted (coached); Doc f_de36d4d3f886c05f52dc3f, comment cmt_66a9a23181dbd441b416 | unscoped ticket, shared Doc | evidence | no |
| ZOM-619 | seeded | 2025-09-26 Claire Morgan RPG 4.5 on iPhone 13, 0.3.40 (40), age 39, friend: notcounted (coached); Doc f_232c00349f8ad72acd9952, comment cmt_d5c24e9c8f2578eaaaf4 | unscoped ticket, shared Doc | evidence | no |
| ZOM-620 | seeded | 2025-09-26 Calvin Price casual 2 on SM-A155F, 0.3.127 (127), age 35, family: notcounted (device), re-run note; Doc f_2c58c7b8fa72b1c6312ce1, comment cmt_f2c392898a98833cdab0 | unscoped ticket, shared Doc | evidence | no |
| ZOM-621 | seeded | 2025-09-26 Vincent Parker casual 3.5 on iPhone 13, 0.3.40 (40), age 39, friend: counted; Doc f_f8712b72a8f7ba2a3eede9, comment cmt_6f38c428866cecfeae70 | unscoped ticket, shared Doc | evidence | no |
| ZOM-622 | seeded | 2025-09-26 Vincent Parker casual 3.5 on iPhone 12, 0.3.40 (40), age 35, friend: counted; Doc f_0ad31b94b4472285773483, comment cmt_47d14bebf67205c792d5 | unscoped ticket, shared Doc | evidence | no |
| ZOM-623 | seeded | 2025-09-26 Vincent Parker RPG 3.5 on Redmi Note 13, 0.3.127 (127), age 29, family: counted; Doc f_8019f063eeae3d9c721975, comment cmt_3b6ab6678b8aed457911 | unscoped ticket, shared Doc | evidence | no |
| ZOM-624 | seeded | 2025-09-26 Arthur Blake RPG 3.5 on iPhone 15, 0.3.40 (40), age 36, friend: counted; Doc f_33b9697009de5d63cee67a, comment cmt_6337dbdf51f3e1d85dab | unscoped ticket, shared Doc | evidence | no |
| ZOM-625 | seeded | 2025-09-26 Douglas casual 4 on Pixel 7, 0.3.127 (127), age 28, classmate: counted; Doc f_2060ffa9cdcfca3b45edd1, comment cmt_c282b81fbbd8e523a68f | unscoped ticket, shared Doc | evidence | no |
| ZOM-626 | seeded | 2025-09-29 Martin Walsh casual 4 on iPhone 13, 0.3.40 (40), age 45, classmate: counted; Doc f_69e935f38bc4f701a82307, comment cmt_a8e3d490e505b21d5e8c | unscoped ticket, shared Doc | evidence | no |
| ZOM-627 | seeded | 2025-09-29 Martin Walsh casual 4 on iPhone 15, 0.3.40 (40), age 37, classmate: counted; Doc f_87cdeaa9f63796916b71eb, comment cmt_70b946c43606113d21ff | unscoped ticket, shared Doc | evidence | no |

## Platform follow-ups

| Follow-up | Record | Note |
|---|---|---|
| Injected Linear comments render | cmt_2fbcaf2d990d8b4e9c0d | 60 devices and Vincent's line ride on `linear_list_comments`; base has none (Ask_Carriers §6b says they render, review m7 asks for a pre-run test) |
| GitHub comment read spill | harmonygames-Games/match3d#476 | about 266–285K characters; a miss caused by the spill alone is CONFOUNDED |
| New Doc lands in the folder | d_8140f09bf9f1b94cb8ee2d | `gdocs_create_document` has no parent parameter; R13 stays ungraded until a run shows the path |
| linear_show_data and maxDescriptionChars | ZOM-568 | the 60-call get_issue row counts 0 until tested |
| Slides element text renders | f_a087f049d271e9aa9f567f | ● carrier by Ask_Carriers; confirm at pre-check |
| GCal copy renders for a declined event | evt_da65644831bc088267263d | ○ for detail; no deciding fact sits there |
| Snowflake figures after regeneration | snowflake.USER_COHORT_RETENTION | 9.09 and the 47 rows |

## rev7 delta (S0r → injection, 2026-11-08)

SQL: `01_Universe_Inject.sql`, stored byte for byte as `run_forensics/rev7/01_Universe_Inject.sql` (sha256 3acbfad93f4a; the stored copy and the task file are compared with `cmp`, equal). rev6 stays at `run_forensics/rev6/01_Universe_Inject.sql`. 535 rows over 11 schemas (adds `contacts.contacts`); no `confluence.*` or `snowflake.*` row; `contacts.contact_groups` and `contact_group_members` are not written (not writable). Every total below comes from `solver/truth.json` (regenerated on this SQL; `run_forensics/rev7/truth.json`), checked by `run_forensics/rev7/solver_check.txt` (OVERALL PASS).

### New and changed facts, each with its record

| Fact | Record (service · id) | Reach | Role |
|---|---|---|---|
| Leonard's ask now holds the asks only: one audience call (casual lead → hold, RPG lead → keep, no clear lead → keep), the memo per the roadmap card, keep or hold in his thread, tell Brian in #zombie-design, current game only | slack · `b07f1e10112b7661e1d8eaf3b127227f` (`C090N54TG79/1759266627.418203`) | member | anchor A2 |
| Gate Doc: "A pass is a clean test run of the build players get. Arthur Blake owns the Vision Bot job and says what its passes do and don't cover."; no closed-ticket line, no Sep 30 update line | gdocs · `f_748d26e760e54651eaa0d8` | shared with Julia | H-GATE, F-QA delegator |
| Vincent's ZOM-567 comment: editor repro and a green Vision Bot run #15, no device claim | linear · `cmt_38b3cc50dceda37f40f5` | unscoped | K3 decoy |
| Vincent's Sep 29 15:12:37Z post in #zombie-bugs: "0.3.127 (127) regression matrix done, all green, sheet in thread"; reply links the sheet | slack · `3dd0b6d6c52c21cd5bbfcd6d6f5345cd`, `3d8e451a198d5d59b39e60064b590305` (`C08R27X0EAH`, Julia a member) | member | R_K3 decider |
| QA matrix sheet: Android current-gen row "SM-A546E, real device yes, 0.3.127 (127), PASS, 2025-09-29"; no "Samsung" or "Galaxy" anywhere | gsheets · `f_cadae9f611d82d56ac02c3` (shared with Julia, reader) | shared | R_K3 decider |
| Base support for the matrix: QA runbook "on real devices, not just the emulator"; "QA posts the completed matrix in #zombie-bugs" | confluence · `page_qa_runbook` (base, read-only) | unscoped | supporting |
| 13 Samsung sessions now count: `ZOM-587`, `ZOM-588`, `ZOM-590`, `ZOM-591`, `ZOM-593`, `ZOM-594`, `ZOM-596`, `ZOM-601`, `ZOM-603`, `ZOM-606`, `ZOM-620`, `ZOM-631`, `ZOM-641` | linear comments (device) | unscoped | truth |
| Julia's contacts hold the 82 players (created 2025-09-22T16:05:31Z, gift codes); two have games jobs: Alper Koçak "QA tester, console games publisher" (`ZOM-598`), Arda Keskin "Live ops producer, mobile games studio" (`ZOM-622`); Brian's nine have no job | contacts · `038b5eb5a30326895cb54756`, `0810fb8287e489c125fe2cd9` | unscoped | R_G decider |
| Log note: "Players are in my contacts so I can send the gift codes."; "Any form that comes in after this batch gets a ticket and a log row when I see it." | gdocs · `f_c691d577b8f837eb4f9eaa` | owner | F-PLAYERS, F-LATE delegator |
| Owen's Sep 30 20:40Z reply in his form thread: two Sun Sep 28 sessions inline (Ayşe Polat, 33, friend, 0.3.40 (40), casual, 5 stars, iPhone 15; Daniel Hughes, RPG, 1.5 stars, Pixel 8 on 0.3.127 (127)); no ticket, Log row or notes Doc | gmail · `julia.lawson@harmonygames.co/<CAab474c9390349b2f96626bafff9ff2c5f9cd@mail.gmail.com>` (+ Owen's SENT copy) | own mailbox | R_T decider |
| Vincent's note on the KPI tab (row 1, above the header): cohorts before the 2025-07-24 transfer are Calm Play's; quote ZM retention on cohort weeks starting on or after 2025-07-24; Robert's method unchanged. Sheet modified 2025-09-30T10:22:41Z | gsheets · `f_4e21b203a62910bdae0353` | shared with Julia | R_E decider |
| Retention under Robert's rule plus the cut-off: 16 rows, 2,607 installs, install-weighted D7 10.47 % (without the cut-off 47 rows, 6,040 installs, 9.09 %) | snowflake · `USER_COHORT_RETENTION` (base, read-only; `solver/base_retention_rows.json`) | unscoped | truth |
| Leonard's relation rule (family, neighbours, old classmates count, 25–45, not in games) row id re-derived | slack · `ba19de7863a540175f2aeadc12916fa6` (`C090N54TG79/1758818538.552913`) | member | F-AGE, F-INDUSTRY |
| 20 more sessions `ZOM-628`..`ZOM-647`: Douglas 12 (Sat Sep 27, form mail Mon 2025-09-29T07:41:17Z, Docs "ZM session notes - Douglas - 02".."13" in `d_cd7849ec043ab3da107f8c`), Frederick Stone 8 (Mon Sep 29, form mail 2025-09-30T09:22:05Z); each with a notes Doc, a device comment and a Log row | linear, gdocs, gdrive, gmail, gsheets `f_43bc35baf77fd59f4e57b8` | shared / own | volume |
| Re-run notes: the 13 build-1943 drops only (`ZOM-577`..`ZOM-586`, `ZOM-632`, `ZOM-637`, `ZOM-645`) | slack · `167dc58affb9902420038f71d0f5af28` | member | truth |
| Truth: 82 sessions, 45 counted, 37 not (game industry 11, build 13, coached 13); casual 27 at 3.8333, RPG 18 at 3.5000, gap 0.3333 → HOLD; each single-rule miss → KEEP (no clear lead) | `solver/truth.json` | — | truth |

Defects fixed during injection (not design changes): Victor Barnes (left April 2025; SC-36; `Evals/ENVIRONMENT.md`) first drafted as the second observer → Douglas; the Douglas form mail's date column (Mon) now matches its Date header, thread id, ticket text and Log; the ZOM-227 comment carrier for the retention correction was dropped (comment after a closed issue, Check C) in favour of the KPI tab note; `contacts.contacts.source` dropped (not in the schema snapshot).

## Self-review

### Tool outputs, verbatim

`python3 Task_Authoring/tools/sql_lint.py Task_Authoring/task_inputs/01_Universe_Inject.sql --task-dir Task_Authoring/task_inputs`:

```text
schemas touched (11): contacts, gcal, gdocs, gdrive, github, gmail, gsheets, gslides, linear, slack, trello
rows by schema: {'gdrive': 86, 'gdocs': 82, 'gsheets': 7, 'gslides': 7, 'gcal': 2, 'gmail': 82, 'linear': 162, 'github': 3, 'trello': 2, 'slack': 20, 'contacts': 82}  total rows: 535  ops: {'insert': 530, 'update': 5}
errors: 0  warnings: 1
  warn  line 892: slack.slack_messages: UPDATE predicate is not keyed on an id column
```

Warning disposition: `UPDATE predicate is not keyed on an id column` at SQL line 710 (rev5 lint output): D05GU6L0XFH/1758901945.292269 is a raw-shape export row with no id field, so an id-keyed UPDATE would match nothing and base_check fails it; channel_id and ts identify the row uniquely. Accepted.

`python3 Task_Authoring/tools/base_check.py Task_Authoring/task_inputs/01_Universe_Inject.sql`:

```text
BASE CHECK (/injection A + C, static): PASS  — 530 inserts, 5 updates
KB: bound (2025-10-01) — KB bound to the selected universe
Check A — records, references, IDs: PASS
Check C — dates and relationships: PASS
Warnings (1):
  line 361: gcal.gcal_events: meeting 4b728ac5dc87a7c18aa933f1195349a1@hg4 'Friday at Claire's' has 1 attendee(s) but no invitation mail ('Invitation: Friday at Claire's @ …') in any attendee mailbox — INT-11 base: 836/941 meetings with attendees have one (2298/2974 attendee mailboxes); add the copies or declare integration_exceptions [{record_id, reason: 'no_notify: …'}]
  note: gsheets.sheets_sheets: no base-reference rules (checked by sql_lint only)
  note: gslides.slides_page_elements: no base-reference rules (checked by sql_lint only)
  note: gslides.slides_pages: no base-reference rules (checked by sql_lint only)
```

`python3 Task_Authoring/tools/base_claims.py Task_Authoring/task_inputs/01_Universe_Inject.sql --task-dir Task_Authoring/task_inputs`:

```text
BASE CLAIMS (injected text vs base git + #builds): PASS · 0 branch mentions · 0 fail · 0 warn · 0 date-only
branch windows:
```

One block, in order: `hardness_gate.py` on the final manifest and SQL; `oracle_kit.py check --task-dir Task_Authoring/task_inputs`; `difficulty_mutation.py mutate --task-dir Task_Authoring/task_inputs --dispositions` (the file's mutation map); `trap_liveness.py --task-dir Task_Authoring/task_inputs --dispositions` (its liveness map); `hardness_v2_check.py --task-dir Task_Authoring/task_inputs`; then, when run, `hardness_forecast.py forecast ... --preregister` (UNCALIBRATED, advisory) and `preflight_report.py`. All verbatim.

```text
HARDNESS GATE (extreme): PASS
  [ok] assignment_context: manifest bound to current V3 assignment, freeze and policy
  [ok] effective_profile: effective_profile 'extreme' for 'Long Horizon' → thresholds 'extreme'
  [ok] sql_lint_clean: 0 lint error(s) — run tools/sql_lint.py
  [ok] base_consistency: /injection-style checks vs the base universe: A 0 finding(s), C 0 finding(s), 0 warning(s) — run tools/base_check.py --manifest
  [ok] persona_reach: 283 load-bearing seeded ids for julia_lawson (167 in unscoped services = visible, 116 judged by persona_view check-sql); not provably visible: none
  [ok] fact_consistency: fact_check: 0 error(s) (20 declared facts), 10 drift warning(s); first: none — run tools/fact_check.py --manifest --no-leak
  [ok] hazard_scope: 0 pre-existing hazard(s) among task-touched records; state/lifecycle or referential without a verified resolution: none
  [ok] services_injected: 11 schemas injected (contacts, gcal, gdocs, gdrive, github, gmail, gsheets, gslides, linear, slack, trello); need ≥ 10
  [ok] rows: 530 INSERTed rows (UPDATE companions not counted; 535 rows in all); need ≥ 120
  [ok] services_carrying_weight: 12 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: schemas injected but absent from the design: none
  [ok] seeded_ids_exist_in_sql: 67 seeded ids cited; missing from SQL: none
  [ok] anchors: 3 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 20 fragments; need ≥ 12
  [ok] ask_fragment_services: 9 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 19 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 14 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 82; need ≥ 40 (source-defined: True)
  [ok] evidence_surfaces: 5 surfaces over 4 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 246; need ≥ 240
  [ok] call_budget: unconditional (verified) floor 358 of 438 planned calls (80 conditional on unverified tool behaviour count 0); need floor ≥ 340 (requester-confirmed volume_exception)
  [ok] call_budget_spread: 13 services in budget; largest share outside the per-record phase 34% (≤ 50%)
  [ok] traps: 16 traps across 8 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 10 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 4 supersessions (3 with versions in ≥ 2 services, 1 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: 7 trap(s) with version_records; the records' own timestamps (SQL created_at/ts/date/updated_at, or the base record) must be strictly increasing in the listed order (oldest first); bad: none
  [ok] distractors: 6 distractors of 5 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 15 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 5 chains with 4 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] mechanism_portfolio: 9 portfolio entries, each a mechanism-enum id with trap/chain nodes, a requirement, a natural-reading fallback and a prior family with its reason
  [ok] artifact_fields: declared ['gradable_surface', 'solver', 'preflight']: paths relative, digests sha256
  [ok] hidden_authorities: 3 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 1 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 8 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 14 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 7 writes over 4 services; each must depend on findings
  [note] call budget: planned total 438, unconditional floor 358 — the conditional rows count once their tool behaviour is verified (then drop conditional_on)
  [note] volume_exception: call-budget floor 340 and per-record floor 240 replace 500 and 300; every other extreme target applies — reason: the honest work is 82 sessions: about 360 necessary calls from real reads and wr; requester confirmation: requester confirmed 2026-11-07 in session; rev7 volume (400+ calls, all 13 servi

SOLVER CONTRACT: PASS · solver.py sha c5cb9c1fd1f2 · sql 3acbfad93f4a · 9 rules
  [PASS] contract.interface: 9 rules, each with mechanism, requirement and natural_reading; optional: ['touched', 'deciding', 'DEGRADES']
  [PASS] contract.deterministic: two fresh solves (forward and reverse key order) give identical output (84 keys, sha c24718c3ea25), and so do fresh processes with PYTHONHASHSEED 1 and 2
  [PASS] contract.regression: no previous revision supplied (first revision)
  [PASS] contract.rules_nodes: 9 rules vs 9 portfolio entries: one-to-one
  [PASS] contract.slots: 10 direct/aggregate slots read a solver value; 16 write-content/delivery slots are graded from the writes, not the solver
  [PASS] contract.controls: R_K1: 3 control(s); over:K1_all_sessions_that_day moves ['ZOM-605', 'ZOM-621', 'ZOM-625']; R_K3: 3 control(s); over:K3_all_android moves ['ZOM-589', 'ZOM-625', 'ZOM-643']; R_K4: 2 control(s); over:K4_any_group_nickname moves ['ZOM-626', 'ZOM-627']; R_K5: 3 control(s); over:K5_all_android moves ['ZOM-597', 'ZOM-623', 'ZOM-643']; R_G: 2 control(s); over:G_any_tech_job moves ['ZOM-590', 'ZOM-633']; R_F: 2 control(s); over:F_rerun_all_notcounted moves ['ZOM-568', 'ZOM-569']; channel scale:verdict (scale): slip:verdict moves 82 of 82 member(s); channel tool_surface:state_writes (tool_surface): fails surface slots ['S-ST1', 'S-ST2']; channel delegation:handling (delegation): fails surface slots ['S-F1']; channel chain:decision (chain): fails surface slots ['S-DEC', 'S-BRIAN']; channel synthesis:context (synthesis): fails surface slots ['S-D1', 'S-E1']
  [PASS] contract.golden: 63 golden values checked against their deciding records (9 sampled keys x 7 fields): 49 identifier values found, 14 short tokens found, 0 presence-type (1 through tools/hg.py records); 0 unverified
  [PASS] contract.digest: manifest solver Working_Files/solver/solver.py digest c5cb9c1fd1f2 vs file c5cb9c1fd1f2

MUTATION · rev7 · sql 3acbfad93f4a · deterministic design diagnostics from the solver; on the Season Pass backtests these are development fixtures, not validation
  key-locality: PASS on 40 of 40 configurations checked
  rule:R_K1                          KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['S-K1a']
  rule:R_K3                          KILLED     flipped  15 flips direct slot(s) of weight >= 3: ['S-K3a', 'S-K3b']
  rule:R_K4                          KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['S-K4a']
  rule:R_K5                          KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['S-K5a']
  rule:R_G                           KILLED     flipped  15 flips direct slot(s) of weight >= 3: ['S-Ga', 'S-Gb']
  rule:R_T                           WEAK       flipped   5 flips only aggregate or weight-1 slots: ['S-G1']
  rule:R_F                           SURVIVED   flipped   0 changes outputs that no slot reads
  rule:R_D                           SURVIVED   flipped   0 changes outputs that no slot reads
  rule:R_E                           SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:over:K1_all_sessions_that_day KILLED     flipped   8 flips direct slot(s) of weight >= 3: ['S-O2']
  degrade:over:K3_all_android        KILLED     flipped  18 flips direct slot(s) of weight >= 3: ['S-K3a', 'S-K3b', 'S-O1']
  degrade:over:K4_any_group_nickname WEAK       flipped   5 flips only aggregate or weight-1 slots: ['S-G1']
  degrade:over:K5_all_android        KILLED     flipped  18 flips direct slot(s) of weight >= 3: ['S-K3a', 'S-K3b', 'S-O1']
  degrade:over:G_any_tech_job        WEAK       flipped   5 flips only aggregate or weight-1 slots: ['S-G1']
  degrade:over:F_rerun_all_notcounted SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:slip:verdict               KILLED     flipped  46 flips direct slot(s) of weight >= 3: ['S-K1a', 'S-K3a', 'S-K3b', 'S-K4
  shards (consecutive slices of 14 records, 6 batches): 21 mutants {'KILLED': 7, 'WEAK': 8, 'SURVIVED': 6}
  intervention:rule:R_K1             load-bearing    
  intervention:rule:R_K3             escaped          FINDING: a record outside the node's closure changed: undeclared coupling
  intervention:rule:R_K4             load-bearing    
  intervention:rule:R_K5             load-bearing    
  intervention:rule:R_G              load-bearing    
  intervention:rule:R_T              load-bearing    
  intervention:rule:R_F              load-bearing    
  intervention:rule:R_D              load-bearing    
  intervention:rule:R_E              load-bearing    
  intervention:degrade:over:K1_all_sessions_that_day no-injected-records
  intervention:degrade:over:K3_all_android no-injected-records
  intervention:degrade:over:K4_any_group_nickname no-injected-records
  intervention:degrade:over:K5_all_android no-injected-records
  intervention:degrade:over:G_any_tech_job no-injected-records
  intervention:degrade:over:F_rerun_all_notcounted no-injected-records
  intervention:degrade:slip:verdict  no-injected-records
  geometry: U = 0.9796 (96/98) · L_max = UNSUPPORTED
    V3 cap 0.85: U PASS (needs > 0.15) · L_max UNSUPPORTED
  dispositions: 32/32 recorded; missing []

TRAP LIVENESS · ADVISORY · UNCALIBRATED · lexical warnings, not proof · on the Season Pass backtests these are development fixtures, not validation
  hub C090N54TG79/1758517286.431379 · direct delegations 5 · rule placement: A15 nodes only: ['T-RET'] (mechanism_portfolio); every other node SKIP
  T-K3 done_gap           breadcrumb  [rule placement SKIP: not an A15 node]
  T-K1 effective_date     -  [rule placement SKIP: not an A15 node]
  T-K4 superseding        breadcrumb  [rule placement SKIP: not an A15 node]
  T-K5 exact_predicate    -  [rule placement SKIP: not an A15 node]
  T-F  cross_reference_ga breadcrumb  [rule placement SKIP: not an A15 node]
  T-PANEL eliminating_eviden -  [rule placement SKIP: not an A15 node]
  T-AUD superseding        breadcrumb  [rule placement SKIP: not an A15 node]
  T-RET superseding        -
  T-559 distractor         -  [rule placement SKIP: not an A15 node]
  T-LEAN distractor         -  [rule placement SKIP: not an A15 node]
  T-466 distractor         -  [rule placement SKIP: not an A15 node]
  T-DUP distractor         -  [rule placement SKIP: not an A15 node]
  T-FTUE distractor         -  [rule placement SKIP: not an A15 node]
  T-S23 distractor         -  [rule placement SKIP: not an A15 node]
  T-G  near_miss_mention  breadcrumb  [rule placement SKIP: not an A15 node]
  T-T  cross_reference_ga -  [rule placement SKIP: not an A15 node]
  dispositions: 5/5 recorded

ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      7 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 7 requirements: {'R1': ['R_K1', 'R_T'], 'R2': ['R_K3'], 'R4': ['R_K4', 'R_G'], 'R3': ['R_K5'], 'R8': ['R_F'], 'R10': ['R_D'], 'R11': ['R_E']}  [Part 5 rule 1]
  FLAG       DECISION_FLIP   6 of 9 rules can flip a weight-5 slot; not: ['R_F', 'R_D', 'R_E']  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     1 weight-5 total(s); 1 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  CLEAN      RULE_IN_PROMPT  no run of 8 resolver words in the prompt  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']

Flags (each needs a written disposition; redesign the difficulty, never weaken a fairness link or raise a weight):
  DECISION_FLIP R_F: rule R_F (A14) can flip slots of weight [3], no weight-5 slot
  DECISION_FLIP R_D: rule R_D (A19) can flip slots of weight [3], no weight-5 slot
  DECISION_FLIP R_E: rule R_E (A15) can flip slots of weight [3], no weight-5 slot

HARDNESS FORECAST · UNCALIBRATED · advisory · model claude-opus-5-5 · rev7 · model outputs, not measurements; the Season Pass backtests are development fixtures, not validation
  rule:R_K1                                    family A13                                      Beta(1.0, 2.0) mean 0.33 n_eff 1.0 records 1
  rule:R_K3                                    family done_gap                                 Beta(1.0, 3.0) mean 0.25 n_eff 2.0 records 2
  rule:R_K4                                    family A18                                      Beta(1.0, 2.0) mean 0.33 n_eff 1.0 records 1
  rule:R_K5                                    family A17                                      Beta(1.0, 2.0) mean 0.33 n_eff 1.0 records 1
  rule:R_G                                     family A13                                      Beta(1.0, 2.0) mean 0.33 n_eff 1.0 records 1
  rule:R_T                                     family A17                                      Beta(1.0, 2.0) mean 0.33 n_eff 1.0 records 1
  rule:R_F                                     family A14                                      Beta(1.0, 2.0) mean 0.33 n_eff 1.0 records 1
  rule:R_E                                     family A15                                      Beta(1.0, 2.0) mean 0.33 n_eff 1.0 records 1
  independent whole    V3 E[avg] 0.750 [0.677, 0.821] P(all) 0.139
  independent shard:32 V3 E[avg] 0.791 [0.733, 0.849] P(all) 0.025
  independent shard:14 V3 E[avg] 0.808 [0.752, 0.862] P(all) 0.020
  independent slip     V3 E[avg] 0.840 [0.787, 0.889] P(all) 0.005
  independent batches  V3 E[avg] 0.800 [0.738, 0.857] P(all) 0.027
  source      whole    V3 E[avg] 0.750 [0.677, 0.821] P(all) 0.139
  source      shard:32 V3 E[avg] 0.791 [0.733, 0.849] P(all) 0.025
  source      shard:14 V3 E[avg] 0.808 [0.752, 0.862] P(all) 0.020
  source      slip     V3 E[avg] 0.840 [0.787, 0.889] P(all) 0.005
  source      batches  V3 E[avg] 0.800 [0.738, 0.857] P(all) 0.027
  correlated  whole    V3 E[avg] 0.751 [0.660, 0.837] P(all) 0.545
  correlated  shard:32 V3 E[avg] 0.793 [0.726, 0.855] P(all) 0.171
  correlated  shard:14 V3 E[avg] 0.808 [0.747, 0.866] P(all) 0.081
  correlated  slip     V3 E[avg] 0.840 [0.789, 0.889] P(all) 0.009
  correlated  batches  V3 E[avg] 0.801 [0.735, 0.862] P(all) 0.117
  V3: P(all four difficulty gates) 0.005-0.545 across scenarios; value of information (first scenario): ['rule:R_K3', 'rule:R_G', 'rule:R_K5']
  channel scale:verdict (scale, member latent [declared], 82 member(s), member trials): e ~ Beta(1.0, 61.0) [ledger records, member trials (runs of a task share a design] · P(any of 82 fails) 0.573 integrated vs 0.736 plug-in · expected loss alone 0.0310 · UNCALIBRATED
  channel tool_surface:state_writes (tool_surface, run latent [declared], 0 member(s), slots ['S-ST1', 'S-ST2'], run trials): e ~ Beta(1.0, 2.0) [ledger records, run trials (runs of a task share a design ef] · P(any of 1 fails) 0.333 integrated vs 0.333 plug-in · expected loss alone 0.0206 · UNCALIBRATED
  channel delegation:handling (delegation, run latent [declared], 0 member(s), slots ['S-F1'], run trials): e ~ Beta(1.0, 2.0) [ledger records, run trials (runs of a task share a design ef] · P(any of 1 fails) 0.333 integrated vs 0.333 plug-in · expected loss alone 0.0103 · UNCALIBRATED
  channel chain:decision (chain, run latent [declared], 0 member(s), slots ['S-DEC', 'S-BRIAN'], run trials): e ~ Beta(1.0, 2.0) [ledger records, run trials (runs of a task share a design ef] · P(any of 1 fails) 0.333 integrated vs 0.333 plug-in · expected loss alone 0.0206 · UNCALIBRATED
  channel synthesis:context (synthesis, run latent [declared], 0 member(s), slots ['S-D1', 'S-E1'], run trials): e ~ Beta(1.0, 2.0) [ledger records, run trials (runs of a task share a design ef] · P(any of 1 fails) 0.333 integrated vs 0.333 plug-in · expected loss alone 0.0206 · UNCALIBRATED
  channel control:R_K1 (control, member latent [rate unit], 3 member(s), member trials): e ~ Beta(1.0, 4.0) [ledger records, member trials (runs of a task share a design] · P(any of 3 fails) 0.429 integrated vs 0.488 plug-in · expected loss alone 0.0283 · UNCALIBRATED
  channel control:R_K3 (control, member latent [rate unit], 3 member(s), member trials): e ~ Beta(1.0, 6.0) [ledger records, member trials (runs of a task share a design] · P(any of 3 fails) 0.333 integrated vs 0.370 plug-in · expected loss alone 0.0213 · UNCALIBRATED
  channel control:R_K4 (control, member latent [rate unit], 2 member(s), member trials): e ~ Beta(1.0, 3.0) [ledger records, member trials (runs of a task share a design] · P(any of 2 fails) 0.400 integrated vs 0.438 plug-in · expected loss alone 0.0199 · UNCALIBRATED
  channel control:R_K5 (control, member latent [rate unit], 3 member(s), member trials): e ~ Beta(1.0, 4.0) [ledger records, member trials (runs of a task share a design] · P(any of 3 fails) 0.429 integrated vs 0.488 plug-in · expected loss alone 0.0284 · UNCALIBRATED
  channel control:R_G (control, member latent [rate unit], 2 member(s), member trials): e ~ Beta(1.0, 4.0) [ledger records, member trials (runs of a task share a design] · P(any of 2 fails) 0.333 integrated vs 0.360 plug-in · expected loss alone 0.0167 · UNCALIBRATED
  channel control:R_F (control): UNPARAMETERIZED - no ledger record and no --channel-rate override: not simulated
  slots most at risk (independent whole; P(fail) / P(fails all six) - all-fail justification workload, never a block): S-G1 0.97/0.83, S-K5a 0.34/0.03, S-K1a 0.34/0.03, S-ST1 0.33/0.04, S-ST2 0.33/0.04, S-Ga 0.33/0.03, S-D1 0.33/0.03, S-E1 0.33/0.03
wrote Task_Authoring\task_inputs\Working_Files\plan\out_rev7\forecast.json

PREFLIGHT: PASS · blocking {'solver_contract': True, 'surface_validation': True, 'mutation_dispositions': True, 'geometry_upper_bound': True} · advisory {'geometry_margin': {'V3': 'UNSUPPORTED'}, 'geometry_bound_verdict': {'V3': 'PASS'}, 'liveness_dispositions_missing': [], 'forecast': 'recorded'}
wrote Task_Authoring\task_inputs\Working_Files\01c_Preflight_Report.json and Task_Authoring\task_inputs\Working_Files\01c_Preflight_Report.md
```

Dispositions for every mutation result, liveness flag and v2 flag are in `Working_Files/01c_Dispositions.json`. DECISION_FLIP on R_F, R_D, R_E is accepted, weights not raised; RULE_IN_PROMPT re-runs at the prompt stage.

### Review findings (01d_SQL_Review.md)

| Finding | Disposition in rev2 | Record |
|---|---|---|
| M1 observers follow a format nobody passed on | fixed: the relay now carries the no-coaching line, the age band, the Doc fields and the mail fields | C0880U9751A/1758555040.262718 |
| M2 Vincent's repro forks K3 | fixed: the line says the repro was in the editor with no Samsung phone | cmt_38b3cc50dceda37f40f5 |
| M3 rc_28 off the base companion shape | fixed: rc_28 and its mirror removed; root reply_count 30; PR updated_at 20:10:26Z | C093LEZGF6J/1759258475.735779 |
| M4 authorities read like an answer key | fixed: gate Doc in plain policy, ZOM-559 a bug-queue note, one scope sentence, Arthur's Vision Bot PR named; log note and card reworded | f_748d26e760e54651eaa0d8 |
| m1 industry rule has no scope for earlier sessions | fixed: adds that it goes for sessions already run | C090N54TG79/1758733233.117446 |
| m2 a/an in device comments | fixed: article rule; the solver reads both forms | cmt_2fbcaf2d990d8b4e9c0d |
| m3 closed ticket is not a pass | fixed: the gate Doc says a closed ticket isn't a pass | f_748d26e760e54651eaa0d8 |
| m4 forward misdescribes the vendor mail | fixed: names both runs and the report links | julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com> |
| m5 Brian's Doc times run backwards | fixed: Docs 01 to 09 ascend from 09:05:00 | f_524278b67bfa30dde78699 |
| m6 K3 shape is a tell | fixed: four content swaps between rounds; K3 is ZOM-587, 588, 590, 591, 593, 594, 596, 601, 603, 606, 620; counts and means unchanged (truth.json) | ZOM-601 |
| m7 the Turkish line is unprompted | fixed: Julia asks first in Turkish | D076RBM29JS/1758658884.207315 |

**Forecast.** rev2 changes per-key truth (which tickets are K3, so the rule controls moved to sessions the truth counts) but no aggregate, no surface slot's expected value and no declared attribution, which are all the design-mode forecast reads. hev_31aeef573fe8aea8 stands; it was not re-registered.

### Reading the numbers honestly

- Mutation: R_K1, R_K3, R_K4, R_K5 are KILLED. R_F, R_D and R_E SURVIVED: on the solver view they never flip a slot, because S-F1, S-D1 and S-E1 are text slots. Each touches only its own 3-weight slot.
- L_max 25/77 understates the design. The tool reads only `field` and `total` selectors, so one block miss shows 10 of the 35 of 77 the surface declares (S-Ka 5, S-Kb 3, S-H1 5, S-G1 5, S-G2 5, S-DEC 3, S-BRIAN 3, S-ST1 3, S-ST2 3). All four misses are 59 of 77 by the same count.
- With the 8 slots reclassed, contract.slots passes, but difficulty_mutation and the solver-mode forecast still read only `field` and `total` selectors: U stays 74/77 and tool L_max 25/77. By declared attributions the four blocks reach 59 of 77 (0.766) and all seven rules 68 of 77 (0.883).
- Forecast hev_31aeef573fe8aea8 supersedes hev_a5bdd23c22790fbd. It is a --design run, the only mode that counts text slots, so it carries no channels. Independent and source: E[avg] 0.430, band 0.307-0.584, P(sd) 0.389, P(patterns) 0.864, P(all) 0.352. Correlated: E[avg] 0.480, band 0.292-0.704, P(sd) 0.563, P(patterns) 0.534, P(all) 0.307.
- Too deterministic: seven slots (S-H1, S-G1, S-G2, S-DEC, S-BRIAN, S-ST1, S-ST2, 27 weight) flip together on any block miss, because all 15 miss sets flip the lead. The ladder is 1.00, then 0.545, 0.442, 0.338, 0.234 by misses. Runs with a miss sit 0.10 apart, so SD clears 0.10 only when a run has no miss, and at flat priors few do (median SD about 0.106, model only).
- Too correlated: one latent across runs (the correlated scenario) halves P(patterns), since every run then misses the same blocks.
- Proposed fair fix, not applied. Findability: raise K1 and K4 find rates to about 0.75, e.g. a form line pointing at the later mail and the nickname explained in Brian's relay; model E[avg] 0.57, P(sd in band) 0.75, against 0.47 and 0.50 at the judged rates. Row spread: raise K5's casual ratings to a mean near 3.45, so a K5 miss alone keeps the casual lead (S-H1, S-DEC, S-BRIAN hold, a 0.69 rung); with both, E[avg] 0.58, P(sd) 0.83. All block misses at 0.25 would give E[avg] 0.64, near the 62 % target. Any rating change must re-run the flip proof.

Flip table from the solver (each row a set of block misses):

| Missed | Counted | Casual n / mean | RPG n / mean | Gap | Lead | Decision |
|---|---|---|---|---|---|---|
| none | 17 | 9 / 3.833 | 8 / 3.375 | 0.458 | casual | hold |
| R_K1 | 30 | 9 / 3.833 | 21 / 4.167 | 0.333 | rpg | keep |
| R_K3 | 28 | 20 / 3.025 | 8 / 3.375 | 0.35 | rpg | keep |
| R_K4 | 26 | 9 / 3.833 | 17 / 4.118 | 0.284 | rpg | keep |
| R_K5 | 27 | 19 / 3.105 | 8 / 3.375 | 0.27 | rpg | keep |
| R_K1, R_K3 | 41 | 20 / 3.025 | 21 / 4.167 | 1.142 | rpg | keep |
| R_K1, R_K4 | 39 | 9 / 3.833 | 30 / 4.35 | 0.517 | rpg | keep |
| R_K1, R_K5 | 40 | 19 / 3.105 | 21 / 4.167 | 1.061 | rpg | keep |
| R_K3, R_K4 | 37 | 20 / 3.025 | 17 / 4.118 | 1.093 | rpg | keep |
| R_K3, R_K5 | 38 | 30 / 2.833 | 8 / 3.375 | 0.542 | rpg | keep |
| R_K4, R_K5 | 36 | 19 / 3.105 | 17 / 4.118 | 1.012 | rpg | keep |
| R_K1, R_K3, R_K4 | 50 | 20 / 3.025 | 30 / 4.35 | 1.325 | rpg | keep |
| R_K1, R_K3, R_K5 | 51 | 30 / 2.833 | 21 / 4.167 | 1.333 | rpg | keep |
| R_K1, R_K4, R_K5 | 49 | 19 / 3.105 | 30 / 4.35 | 1.245 | rpg | keep |
| R_K3, R_K4, R_K5 | 47 | 30 / 2.833 | 17 / 4.118 | 1.284 | rpg | keep |
| R_K1, R_K3, R_K4, R_K5 | 60 | 30 / 2.833 | 30 / 4.35 | 1.517 | rpg | keep |

All 15 miss sets give RPG past the 0.25 band; the smallest wrong gap is 0.27 (R_K5).

### Checks A–C walk (`Evals/0_Injection_Quality_Eval.md`)

| Check | Item | Verdict | Pointer |
|---|---|---|---|
| Inventory | 352 INSERT, 5 UPDATE, no DELETE, no upsert | PASS | SQL L1 header; sql_lint |
| Check A | references resolve, including archived and history records | PASS | base_check Check A; ZOM-559 not touched |
| Check A | uniqueness scoped to the full collection | PASS | 1.F lookups; base_check |
| Check A | ownership, membership, shares | PASS | f_748d26e760e54651eaa0d8 sharing equals its docs row; C090N54TG79 authors are live members |
| Check A | id contracts | PASS | hg.py lint; Message-IDs shared across copies, julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com> |
| Check B | structure, literal JSON, generated and NOT NULL columns | PASS | sql_lint 0 errors; hg.py lint 0 FAIL; `text_fts` never written |
| Check B | `github_reviews.seq` is outside the eval snapshot | PASS with a CHECK | see LINT line below; base rows carry seq |
| Check C | dates and chronology | PASS | base_check Check C; supersession_chronology; no timestamp past the bound (plan/sweep.py) |
| Check C | parent and reply | PASS | C090N54TG79/1758581651.167799 counters; C093LEZGF6J/1759258475.735779 at 30 after rc_28 was removed |
| Check C | statuses, counts, amounts | PASS | ZOM-567 stamps; panel and KPI recomputed in solver/truth.json |
| Check C | claimed updates and superseding records | PASS | version_records strictly increasing |
| Check C | no grader-facing or padding text | PASS | plan/sweep.py avoid lists; every row maps to a manifest element in the ledger |

`hg.py lint` counts: {"FAIL": 0, "CHECK": 1, "INFO": 5, "by_check": {"unknown_column": 1}}.


### Touched-data census

The touched base records and their hazards are in the section **Touched-data census and coherence hazards** above; nothing the SQL updates is a hazard record.

### Counter-readings

| Category | Counter-reading (strongest case it fails) | Evidence | Verdict |
|---|---|---|---|
| Temporal | ticket dates of Sep 30 look newer than Claire's Sep 29 mail, so the correction is older than what it corrects; K3 sessions predate run #15 | f_c691d577b8f837eb4f9eaa says the ticket's own date says nothing about when anything happened; f_748d26e760e54651eaa0d8 says a valid pass clears sessions whatever day they ran | holds |
| Semantic / Category | "casual" and "RPG" are the note's and/or, so one label is invented; a label reads as a re-derivation | f_a087f049d271e9aa9f567f says the observer's label stands (S03) | holds |
| Cross-service referential | the ask said replies under the note before D1; five rule records are top-level, so a thread read finds nothing and F-AGE, F-INDUSTRY, F-GATE containers moved | C090N54TG79/1759266627.418203 now says the rules posted in the channel after the note; design_delta records it; R3 opens "One more for the feedback note" at C090N54TG79/1758733233.117446 | holds |
| Quantitative | three sources tie 60 for 60 on a wrong answer; 9.09 could be 9.05 on a closed-window reading | each transcribes one form; C090N54TG79/1759167008.881274 defines mature as having a D14 figure, 47 rows, snowflake.USER_COHORT_RETENTION | holds |
| State / Lifecycle | pre-existing: ZOM-559 stays Todo while ZOM-567 is Done on the same family; sibling: ENG-2324 Done on Samsung startup | different scopes; f_748d26e760e54651eaa0d8 says ZOM-559 is no session blocker; ENG-2324 is the other team's and no seed cites it (L03) | holds |
| Identifier / Format | F root UPDATE keyed on channel and ts breaks the keyed-on-id rule; Claire's calendar copy has a second event id | raw export row with no id field, D05GU6L0XFH/1758901945.292269; base keeps a distinct event_id per calendar, shared ical_uid 4b728ac5dc87a7c18aa933f1195349a1@hg4 | holds, disclosed |
| People status | Claire, Oliver and Owen never joined #zombie-design, so they never saw the note | R0 relay C0880U9751A/1758555040.262718 reaches all twelve observers; activity.json shows all active at the clock (SC-7 not graded) | holds |
| Other | the designed disagreement reads as two silent system fields | every one is a dated human claim: cmt_38b3cc50dceda37f40f5 against harmonygames-Games/match3d#476#rc_27; no system field carries it | holds |
| Done gap | best argument it is an unintended inconsistency: Arthur never says Samsung, so the note does not overturn Vincent | f_748d26e760e54651eaa0d8: a pass covers a device only if it ran on that device; harmonygames-Games/match3d#476#rc_27 says no phone in the loop | holds; remains the likeliest /prompt challenge |
| Coached mail | best argument it is unintended: the mail never says coaching and a reader could call it harmless | julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com> says she took them through what the cards do and which items to grab, against the note's rule at C090N54TG79/1758517286.431379 | holds |
| Industry line | best argument it is unintended: the line may be about another group | same nickname on f_524278b67bfa30dde78699 and D076RBM29JS/1758659012.418207; 0 base hits for the nickname in 1.D | holds |
| Build reply | best argument it is unintended: `main` in the job name may read as release | C090N54TG79/1758819934.612483 states it outright and Leonard wrote the rule; C05433XK267/1758575557.575349 is only support | holds |
| Retention | best argument it is unintended: a KPI Sheet disagreeing with the warehouse is a data defect | f_4e21b203a62910bdae0353 is a dated snapshot with a stated simple mean; the rule at C090N54TG79/1759167008.881274 is later | holds |
| Panel | best argument it is unintended: the note's 3-3.5 disagrees with 3.33 | 3.33 is inside the note's range; julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com> | holds |
| GDD | best argument it is unintended: GDD target against the deck is a live contradiction | f_89fadbc54660c9881d8cf9 is older and in version_records of T-AUD | holds |
| Keep or hold | the ask's mapping flatters Julia, who opposed the change | C090N54TG79/1759266627.418203 states the mapping; C090N54TG79/1759173561.454829 is only context | holds |
| Volume | the 183 per-record calls clear 160 only by counting 60 writes | volume_exception in 01_Hardness_Manifest.json, disclosed in design section 9; evidence reads are 123 | disclosed |

### Re-verified facts

Read through `hg.py records` in this session (scan_complete true on each check):

- C090N54TG79/1758517286.431379: reply_count 0, text starts 'Team,\n\nPlayer feedback remains weak (3-3.5 stars on Playtestcloud across iOS and Android). The core matching f'
- C090N54TG79/1758581651.167799: reply_count 15, text starts "We should focus on figuring out why it doesn't give them a kick of joy to figure things out. So far, i haven't"
- C090N54TG79/1758691397.679889: reply_count 2, text starts "<@EMPLOYEE_0038_SLACK_ID> what's the audience you requested for play test cloud?"
- C090N54TG79/1759165414.829399: reply_count 0, text starts 'Those are retention for earlier versions based on creative'
- C090N54TG79/1759176983.189479: reply_count 1, text starts "I think we should think about what 0.3.22 had and what we're keeping.\n• Blunder was fine the way it is, but it"
- C05433XK267/1758575557.575349: reply_count 0, text starts 'Match3D Android - #1943 - main Success after 5 min 53 sec (<http://blake.tplinkdns.com:9009/job/Match3D%20Andr'
- C05433XK267/1758803475.436309: reply_count 0, text starts 'Match 3D Vision Bot - #15 - Blake/visionBot Success after 8 min 4 sec (<http://blake.tplinkdns.com:9009/job/Ma'
- D05GU6L0XFH/1758901945.292269: reply_count 1, text starts "Can you check if it's item specific?"
- ZOM-559: state Todo, created 2025-09-22T14:54:46Z
- ZOM-566: state Todo, created 2025-09-30T16:26:02Z
- harmonygames-Games/match3d#476: state open, merged False, updated 2025-09-30T19:03:57Z

### Lazy-solver pass

One broad search per service, first hits, no threads: all 60 count, RPG, keep. That run keeps S-R1, S-M1, S-L1, S-O1, S-O2, so 9 of 77 (design section 12); nothing in the implemented SQL raises it, since the log and tickets carry no verdict.

### rev7 clause sweep (blocking, learnings §61)

Every rule sentence the answer applies, each condition, every value the 82 seeded sessions carry (read from the SQL by `solver.load_state`; ages 26–44, nothing on the 25 or 45 edge).

| Rule sentence (record) | Condition | Values seen | Settling record or "inert" |
|---|---|---|---|
| "25–45 casual and/or RPG gamer friends (not kids)" (note `C090N54TG79/1758517286.431379`) | age 25–45 | 26–44 (min 26 ×1, max 44 ×7) | age band settled by `12b40a5b7cc18f7c9fe2d0a9e0e929b4` ("25–45 years old"); no value on an edge |
| same | "friends" | relation: friend 37, family 15, neighbor 12, classmate 9, Kadıköy ekibi 9 | `ba19de7863a540175f2aeadc12916fa6`: "family, neighbours and old classmates count the same"; Kadıköy ekibi settled by `246d6f4a90620e5dafbb06068f450e46` |
| same | "casual and/or RPG gamer" | audience labels: casual 41, RPG 41 | deck `f_a087f049d271e9aa9f567f`: the observer's label stands |
| same | "not kids" | ages ≥ 26 | inert: no minor anywhere |
| "No coaching, just observe" (note) | coaching | 13 sessions of Claire's Sep 26 gathering; every form says no coaching; Owen's late reply says "no coaching" | Claire's Sep 29 mail `julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>` |
| "game-industry people don't count … sessions already run too" (`e72083b249987542a134098010edd305`) | works in games | jobs in Contacts: 2 games jobs (QA tester, console games publisher; Live ops producer, mobile games studio), 71 non-games jobs (teacher, nurse, radio producer, marketing specialist at a retail bank, …), Brian's 9 with no job | the two games jobs by `038b5eb5a30326895cb54756`, `0810fb8287e489c125fe2cd9`; Brian's group by his DM; "Radio producer", "Journalist", "Marketing …" are not games work: inert (no one reading "works in games" excludes them, and none is in a games company) |
| Gate Doc "Samsung is the one device group … SM-S, SM-A and SM-F" (`f_748d26e760e54651eaa0d8`) | Samsung device | Galaxy S24/S23/S23 FE/S22/A54/A35/A15, SM-A546E, SM-S921B, SM-A346E, SM-S911B, SM-A155F, SM-A256E (13); Pixel, Redmi, OnePlus, iPhone (69) | "Other phones need nothing" in the same Doc |
| Gate Doc "counts once we have a clean pass covering that device … covers all the Samsung sessions" | a pass exists | Vision Bot run #15 (editor), QA matrix row SM-A546E (real device) | matrix `f_cadae9f611d82d56ac02c3` + post `3dd0b6d6c52c21cd5bbfcd6d6f5345cd`; Vision Bot limited by `harmonygames-Games/match3d#476#rc_27` |
| Gate Doc "A pass is a clean test run of the build players get" | build players get | matrix build 0.3.127 (127) on Android, 0.3.40 (40) on iOS | K5 reply `d7122186e361aa99778c65cb1502759d`: 0.3.127 (127) and 0.3.38 / 0.3.40 went through the store |
| Gate Doc "Sessions on dev builds do not count … never went through a store" | build | 0.3.127 (127) 30, 0.3.40 (40) 30, 0.3.38 (38) 9, 0.3.127 (1943) 13 | `d7122186e361aa99778c65cb1502759d` names 1943 as non-store and the other three as store |
| Robert "dropped for a technical reason, device or build … re-run note" (`167dc58affb9902420038f71d0f5af28`) | technical reason | not-counted reasons: build 13, coached 13, game industry 11; device 0 (the Samsung sessions count) | the same DM: "Dropped for anything else, no re-run" |
| Deck lead test (tie band 0.25, per-audience minimum) (`f_a087f049d271e9aa9f567f`) | gap vs 0.25; minimum per side | truth gap 0.3333 (27 v 18); single misses −0.151 … +0.189 | edge margin 0.083 on the truth, ≥ 0.06 on every single miss (`run_forensics/rev7/solver_check.txt`) |
| Log note "Close-out … counted goes to Done, not counted goes to Canceled" (`f_c691d577b8f837eb4f9eaa`) | state per verdict | 45 counted, 37 not counted | inert beyond the verdicts |
| Log note "Any form that comes in after this batch gets a ticket and a log row" | after the batch | Owen's Sep 30 20:40Z reply (2 sessions); every other form is before the batch | the reply's timestamp vs the last batch ticket (`ZOM-647` updated 20:25:34Z) |
| Leonard "a void rating comes out of both the sum and the count" (`7b38bd6429ce0f189456ac72af02f210`) | void | player 8 void in the forward | the forward `julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com>` |
| Robert "install-weighted D7 … mature cohorts … both platforms pooled" + Vincent "cohort weeks starting on or after 2025-07-24" | mature; cut-off | 51 ZM rows; 47 with D14; 16 on or after 2025-07-24 (week 2025-07-21 spans the transfer and is out by "starting on or after") | `2ca968ace3e14d1a34c535f8a5c0cd6e`, `f_4e21b203a62910bdae0353` |

### rev7 time order (learnings §60)

`python3 Task_Authoring/tools/time_order_check.py Task_Authoring/task_inputs/01_Universe_Inject.sql`: Part 1 (automatic forward references) PASS; Part 2, 33 descriptive pointers, worked through: "the card"/"the board"/"the deck" in notes Docs are the game's cards and deck, not records; the log note's "the workbook" (`f_43bc35baf77fd59f4e57b8` created 16:21:47Z) and "this batch" precede it (16:24Z); the card's "her log note" (card 16:52:31Z) follows the note; the ask's "the roadmap card" (21:10Z) follows the card; Vincent's "sheet in thread" (15:12:37Z) is his own reply 86 s later, the base pattern for a post and its thread; the rule posts' "the feedback note" (Sep 22) precede them.

### rev7 counter-readings

| Category | Counter-reading (strongest case it fails) | Evidence | Verdict |
|---|---|---|---|
| People status | an observer who left would void a batch | Victor Barnes replaced by Douglas (`d_cd7849ec043ab3da107f8c`; activity.json quiet_since_2025-12, active at the clock); Frederick Stone quiet_since_2025-10, active at the clock | holds |
| Temporal | Julia's contacts for the late and second-wave players were created Sep 22, before those sessions ran | `038b5eb5a30326895cb54756` created 2025-09-22T16:05:31Z, after Julia's #zombie-match3d call-out asked hosts for their players up front; the gift-code list is built ahead of play | holds, disclosed |
| Cross-service referential | the matrix names SM-A546E, ZOM-588's phone, so it reads as a pass for one phone only | gate Doc "Once there is a pass, it covers all the Samsung sessions in the read" (`f_748d26e760e54651eaa0d8`) | holds |
| Quantitative | 10.47 % could be 10.44 % if week 2025-07-21 is kept | `f_4e21b203a62910bdae0353` says "starting on or after 2025-07-24"; the S-E1 pattern accepts 10.47 and 10.5 only | holds |
| State / Lifecycle | the retention correction first sat on closed ZOM-227 (a comment after Done) | dropped; the KPI tab note carries it; base_check Check C PASS | fixed |
| Identifier / Format | Leonard's relation rule broke the Slack id contract | re-derived to `ba19de7863a540175f2aeadc12916fa6`; base_check Check A PASS | fixed |
| Other | heuristic name warnings on players (Thomas Reid, Matthew Doyle, Peter Langley, Rachel Dunn, George Ellis, Nathan Cole) | fact_check matches first names to roster people; the players are friends of observers with different surnames, named in "Player:" lines only | accepted warning |
| Done gap | Vincent owns both the Done ZOM-567 line and the matrix, so his own records disagree | `cmt_38b3cc50dceda37f40f5` now speaks only to the editor repro and Vision Bot; the matrix is a separate device run | holds |

LINT unknown_column L856: github.github_review_comments seq on harmonygames-Games/match3d#476#rc_27, kept by instruction (base github review rows carry seq and it is NOT NULL in the 2026-10-04 live export; rev6 kept it the same way); evidence harmonygames-Games/match3d#476#rev_2
sql_lint warning L892 (UPDATE keyed on channel_id and ts): the F root `D05GU6L0XFH/1758901945.292269` is a raw export row with no id field (rev4 note), so the predicate cannot be keyed on id
fact_check warnings (10): heuristic first-name and roster matches, dispositioned in the counter-readings above; Claire, Marcus and Martin bare names are rev6 text, unchanged

Unresolved (rev7): the 400+ call ask is met by necessary work only at about 360 (358 planned unconditional; rev6 measured 4.4 calls per session × 82 ≈ 360 + writes), so 400+ needs a run that also reads the routine context; no independent review of the rev7 SQL; Contacts creation date for late players is a disclosed choice.

### Open items

Unresolved:
- SPREAD RISK, stated plainly. On the declared surface the forecast that stands (hev_31aeef573fe8aea8, UNCALIBRATED, flat Beta(1,1) priors for six of seven rules) gives E[avg] 0.43-0.48, far under the requester's 62 % target, P(per_rollout_sd in band) 0.389-0.563 and median SD about 0.106, at the lower edge of 0.10-0.30. Cause: seven slots (27 weight) flip together on any block miss, so runs with a miss sit 0.10 apart. Fair options, not applied: raise K1 and K4 find rates to about 0.75 (model E[avg] 0.57, P(SD) 0.75); raise K5's casual ratings so a K5 miss alone keeps the casual lead (with both, E[avg] 0.58, P(SD) 0.83). Any rating change needs the flip proof re-run.
- Rev3 (sha dee0010e36ec, 2026-11-08) removes the SQL comments on request, keeping only the line-1 marker that sql_lint requires; its statements are byte-identical to rev2, and the solver contract, mutation and preflight were re-run on it. Its pasted tool outputs (sql 1485546c40b9) are superseded: every output pasted above is the rev5 re-run on sql 5b6e01119505. A comment-free copy for pasting is Working_Files/01_Universe_Inject.clean.sql.
- Rev4 (sha fb77a4153f49, 2026-11-08). Defect: Robert's DM reply D05GU6L0XFH/1758913471.205816 (row 167dc58affb9902420038f71d0f5af28, SQL line 701) carried thread_parent_id '8450048848997da8d669cd475badfbd7', the minted sha256('D05GU6L0XFH|1758901945.292269')[:32]. That id exists nowhere: the base root D05GU6L0XFH/1758901945.292269 is a raw-shape export row with no id field (hg.py records, scan_complete true), so the reply pointed at no row. Fix: thread_parent_id is now `(SELECT id FROM slack.slack_messages WHERE channel_id = 'D05GU6L0XFH' AND ts = '1758901945.292269')`, the root's own id by channel and ts, the same key its counter UPDATE (line 710) already uses. The generator emits it (plan/emitters.py slack_parent, for every root in data.RAW_ROOTS); plan/build.py reproduces the hand-edited file byte for byte. plan/parent_check.py checked all four seeded replies against the base row's real id: R4_panel_definition (c53936d63c93c8ffa0ad1e99526cad73), K5_reply (e6a91393854458ad70331ef478952136) and the #zombie-prs rc_27 mirror (637fc98bc66d41b104fe243006fdcf98) match; F_reply was the only defect. sql_lint (0 errors, 1 warning, now line 710) and hg.py lint (FAIL 0, CHECK 1 at L676) accept the subquery value. No other statement, id or quote changed, so the manifest is unchanged; the solver contract, mutation and preflight were re-run on rev4. Stored in run_forensics/rev4/.
- Rev5 (sha 5b6e01119505, 2026-11-08). Relative-time wording made true in both the Pacific frame (evaluator) and Julia's Turkey frame; plan/reltime_scan.py read every seeded statement. Four texts changed, nothing else (diff against run_forensics/rev4): SQL line 683 Julia's question C090N54TG79/1758553214.330914 "quick one on your note from this morning." -> "quick one on your note." (the note C090N54TG79/1758517286.431379 is 2025-09-22T05:01:26Z, Sun Sep 21 10:01 PM PT); line 689 Julia's DM question D076RBM29JS/1758658884.207315 "bu sabah paylaştığın notlara bakıyorum" -> "paylaştığın notlara bakıyorum" (Brian's Docs are 2025-09-23T09:05Z, 02:05 PT and 12:05 TRT); line 705 Leonard's ask C090N54TG79/1759266627.418203 "the cards earlier change from yesterday" -> "the cards earlier change from Monday" (commit b429c2a8 2025-09-29T19:17:46Z and C090N54TG79/1759172166.547199 are Monday in both frames; the ask is Tue 2:10 PM PT but Wed 00:10 TRT); lines 422-428 Claire's mail julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com> (Mon 2025-09-29T10:02:47Z in both frames) "this week was all items for me" -> "last week was all items for me" (same length, so snippet and size_estimate 557 are unchanged). Other hits stay: weekday+date pairs ("Day: Fri Sep 26", ticket titles), the event title "Friday at Claire's", the subject "a small thing from Friday" (last Friday in both frames) and the log note's "one batch today" (note 16:24Z, tickets 17:14Z-19:42Z, all Sep 30 in both frames). No id, row count, quote in the manifest or solver input changed; every check was re-run (run_forensics/rev5/).
- No independent review of rev2 exists; 01d_SQL_Review.md reviewed rev1 and its findings are applied here, not re-reviewed.
- K3 stays the likeliest shared cause and the likeliest /prompt challenge, because Arthur never names Samsung. No run has tested it.
- Platform follow-ups stay open: linear_list_comments on injected rows, the #476 spill, new-Doc parent, linear_show_data, Slides text render.
- Gmail and Slack minted ids rest on base_check and sql_lint, not on a separate complete lookup (1.F).
- The solver reads retention from solver/base_retention_rows.json, a snapshot through hg.py; re-read it after any regeneration.
- The preflight digest in the manifest points at the preflight run before the final one, because the report binds the manifest by sha256.
- The draft manifest keeps its old quotes and planned_records as a design record; design_delta carries every change.

```
STAGE GATE injection: PASS — Task_Authoring\task_inputs · 01_Universe_Inject.sql#3acbfad93f4a · 01_Hardness_Manifest.json#ccaf326dbd28 · 01_Grounding_Dossier.md#854cbb11bc06 · solver/solver.py#c5cb9c1fd1f2 · 01c_Dispositions.json#a93e896d5a19 · 01c_Preflight_Report.json#eb3e617a6933 · 00_Assigments.md#638de5aac707 · 01_Scenario_Design.md#e8967f83db15 · 01_Hardness_Manifest.draft.json#814b8577398a · 01_Gradable_Surface.json#d1ce8485d03c · __context__#50e89bdae5e1 · __assignment__#7709f2a35b0e · __policy__#dc4ab5df3cdd · __gate_policy__#ce51ca16c6f8 · __review__#cb4fae31202a · blocking 0 · warnings 2 · checks 42
[PASS] assignment.v3_context: Julia Lawson / Product Manager; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 6 output(s) present: 01_Universe_Inject.sql, 01_Hardness_Manifest.json, 01_Grounding_Dossier.md, solver/solver.py, 01c_Dispositions.json, 01c_Preflight_Report.json
[PASS] structure.inputs: 4 input(s) present: 00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json)
[PASS] chain.scenario: upstream 'scenario' PASS pasted and current (01_Scenario_Design.md#e8967f83db15, 01_Hardness_Manifest.draft.json#814b8577398a, 01_Gradable_Surface.json#d1ce8485d03c, 00_Assigments.md#638de5aac707, __context__#50e89bdae5e1, __assignment__#7709f2a35b0e, __policy__#dc4ab5df3cdd, __gate_policy__#0d0895ecc6ed, __review__#773e28601092)
[PASS] structure.sections: 17 required sections present and non-empty (01_Grounding_Dossier.md)
[PASS] structure.placeholders: no placeholders in 01_Grounding_Dossier.md
[PASS] evidence.entity: 14/14 items carry a source pointer (min 90%)
[PASS] evidence.keyword: 12/12 items carry a source pointer (min 100%)
[PASS] evidence.persona_reach: 123/123 items carry a source pointer (min 100%)
[PASS] evidence.record_ledger: 357/357 items carry a source pointer (min 100%)
[PASS] evidence.facts_for_human: 90/90 items carry a source pointer (min 100%)
[PASS] tool.sql_lint: sql_lint re-run matches the paste: errors 0, warnings 1, rows 535
[PASS] tool.injection_lint: hg.py lint: 0 FAIL, 1 CHECK dispositioned, 5 INFO; sha256 3acbfad93f4a matches 01_Universe_Inject.sql
[PASS] review.warning_dispositions: every sql_lint warning class dispositioned (slack.slack_messages: UPDATE predicate i×1)
[PASS] tool.base_check: base_check pasted PASS; re-run PASS
[PASS] tool.base_claims: base_claims pasted PASS; re-run PASS
[PASS] tool.hardness_gate: hardness_gate (SQL) pasted PASS; re-run PASS
[PASS] structure.design_delta: final manifest keeps all 61 draft ids
[PASS] structure.preflight: 01c_Preflight_Report.json bound by sha256 to the current SQL, solver, surface, manifest and dispositions
[PASS] solver.contract: solver contract re-run PASS
[PASS] mutation.dispositions: 32 mutation and intervention results each carry a written disposition (01c_Dispositions.json)
[PASS] geometry.upper_bound: U 0.980 (96/98) vs 1 - cap 0.15 (V3 medium): PASS (bound PASS); re-run U 0.980 PASS (bound PASS)
[WARN] geometry.margin: L_max None vs (1 - cap) + 0.10: UNSUPPORTED (advisory: the margin is a judgment, not a proof)
[PASS] liveness.dispositions: every liveness flag dispositioned (5 flag(s))
[WARN] forecast.preregistered: forecast recorded: pre-register it with tools/hardness_forecast.py --preregister before the platform run (advisory)
[PASS] tool.check_sql_pasted: persona_view check-sql --load-bearing output pasted with verdict PASS
[PASS] reach.injection: 118 scoped load-bearing ids YES for julia_lawson; 4 denied/unverified probe(s), not load-bearing, each with YES alternate_evidence_ids
[PASS] structure.facts_declared: manifest declares 20 load-bearing fact(s) in `facts`
[PASS] tool.fact_check: fact_check --no-leak pasted PASS; re-run PASS
[PASS] kb.coherence_hazards: coherence audit cites 34 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 15 seeded speakers each cited with activity.json status; conventions.json cited
[PASS] kb.integrations: companions listed per integrations.json (11 INT ids, services ['contacts', 'gcal', 'gdocs', 'gdrive', 'github', 'gmail', 'gsheets', 'gslides', 'linear', 'slack', 'trello'])
[PASS] boundary.anchor_naming: 6 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 26 evidenced counter-readings (of 27 found; need ≥ 14) in 01_Grounding_Dossier.md
[PASS] review.coverage: self-review addresses all 9 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] readiness.context: explicit task/revision and current upstream evidence verified
[PASS] readiness.hardness_review: current evidenced review; deferred: []
[PASS] handoff.pasted: pasted into the Self-review by --paste
```





