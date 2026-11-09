# Grounding Dossier — samuel_zm_beta_messages · injection rev6 · contains no prompt, OE or criterion text

Persona: Samuel Turner <samuel.turner@harmonygames.co>, Game Designer. Universe: synth-cut, clock 2025-10-01T07:00Z, seed bound 2025-10-01T00:00:00Z (Tue Sep 30 17:00 PT). SQL: 143 INSERT, 11 UPDATE, 10 schemas.

## 1.A Structural

Columns checked against `references/universe_schema_live.json`; NOT NULL columns marked !; shapes copied from the sibling records named here.

| Table | Columns used (NOT NULL marked) | Location and sample ids | Notes |
|---|---|---|---|
| slack.slack_messages | id!, ts!, channel_id!, text, thread_parent_id, thread_ts_legacy, reply_count, created_at | messages/C08R8CHB0QL/2025-09.json (C08R8CHB0QL/1759159849.386619), messages/D06UFE81RF0/2025-09.json (D06UFE81RF0/1759163970.141449) | id = the first 32 hex of the sha256 of channel, a pipe and ts; replies keep the root's id in thread_parent_id |
| gmail.gmail_threads / gmail_messages | id!, user_email!; id!, thread_id!, user_email! | threads/samuel@harmonygames.co_1836006988541924555.json (samuel.turner@harmonygames.co/1836006988541924555), threads/samuel@harmonygames.co_1831218752991293223.json | thread id = (ms<<20)+bits; one row per mailbox copy; GitHub and calendar mails copy those base messages' fields |
| gdrive.drive_files / gdocs / gsheets / gslides | id!, name!, mime_type!; document_id; spreadsheet_id; presentation_id | gdrive data.json d_63fffeb4fab5233ed5bb73, d_65c76e0b87aa7e9b84d1df (owners' roots) | f_ + 22 hex; same id across Drive and the native row; identical sharing |
| gcal.gcal_events | event_id!, calendar_id! | gcal data.json, Samuel's calendar samuel.turner@harmonygames.co | one row per attendee calendar, self:true on the owner's copy; status cancelled as on 1,033 base events |
| linear.linear_issues / linear_comments / linear_team_memberships / linear_teams | id!, title!, priority!, labels_json!, links_json!, relations_json!, state_history_json!, is_archived!, created_at!, updated_at!; id!, issue_id!, author_id!, body!, is_edited!, created_at!, updated_at!; id!, team_id!, user_id!, created_at! | linear data.json DES-312, ZOM-542, ZOM-556; tmem_team_DES_usr_63fffeb4fab5233e | state_id holds the state name; state_history_json an empty JSON array on new issues; cmt_ + 20 hex (no base comments exist) |
| trello.trello_actions / trello_cards (UPDATE) | id, type, date, idMemberCreator, idBoard, idCard, data_json | trello data.json 6851a769c65dc0017a227bb7, 68d1eb90bef538c7c5c5599d, action 6859879792d832a1e5c9f024 | id's first 8 hex = the action's Unix seconds; badges_json full shape |
| github.github_review_comments / github_reviews | id!, pr_id!, seq! | github data.json harmonygames-Games/match3d#248#rc_17, harmonygames-Games/match3d#248#rev_6 | next id rc_18; diff_hunk is the real hunk from rc_16, the last revision before the comment, up to the commented line; line, position, commit_id null as on every base row |

## 1.B Entity

| Entity | Spelling used | Where it appears (cited) | Agreement |
|---|---|---|---|
| Samuel Turner | samuel.turner@harmonygames.co | slack EMPLOYEE_0004_SLACK_ID in D06L58XCVKK/1750138057.452159; author of harmonygames-Games/match3d#248; Drive root d_caafeec2804b3a67ce46aa; Linear usr_caafeec2804b3a67 | AGREE |
| Leonard Hayes | leonard.hayes@harmonygames.co | slack EMPLOYEE_0038_SLACK_ID in D06L58XCVKK/1750138057.452159; Linear usr_63fffeb4fab5233e; Trello PERSON_6094_TRELLO_USER_ID; owner of f_dc45e0e5a8b8635c1b82b2 | AGREE |
| Vincent Parker | vincent.parker@harmonygames.co | slack EMPLOYEE_0012_SLACK_ID in D06UFE81RF0/1759164108.051389; Linear usr_65c76e0b87aa7e9b; owner of f_8eb8c04713ff6a6ef4a265 | AGREE |
| Robert | robert@harmonygames.co | slack EMPLOYEE_0016_SLACK_ID in D06KPMDV2JZ/1752162738.497679; Linear usr_Robert | AGREE |
| Arthur Blake | arthur.blake@harmonygames.co | slack EMPLOYEE_0025_SLACK_ID in D06KV30TPL4/1750979784.704799; GitHub EMPLOYEE_0025_GITHUB_USERNAME, harmonygames-Games/match3d#248#rev_6; Linear usr_cc3e90160f490686 | AGREE |
| Martin Walsh | martin.walsh@harmonygames.co | slack EMPLOYEE_0033_SLACK_ID in C08R8CHB0QL/1759159849.386619; Linear usr_51f5f16d46e8cf55 | AGREE |
| Brian Foster, Calvin Price, Julia Lawson, Oliver Brooks, Owen Baker | roster addresses | slack EMPLOYEE_0026, 0006, 0005, 0003, 0021 in C0880U9751A/1759189361.525409's channel members; Linear usr_fc22d5941b2aeb5c, usr_49b9dfa5208d400d, usr_8140f09bf9f1b94c, usr_bdf01b53c6a92c5e, usr_4e13bd40cc73d0fc | AGREE |
| Zombie Match 3D | 'Zombie Match' on the sheet title, match3d in GitHub, zombie_match_3d in the warehouse | f_a325dd4af80afc5994d5dc, harmonygames-Games/match3d#248, wh USER_COHORT_RETENTION | AGREE |
| Win & Collect / Collect & Win | row 7 says Win & Collect; DES-313 says Collect & Win | f_a325dd4af80afc5994d5dc, page_liveops_calendar ('Same feature as Win & Collect on Domino Delights, under a different name'), DES-313 | DISAGREE (designed, T5) |
| Boss Arena / Infinite HP Boss Mode | Boss Arena in Linear and tickets; the BETA list card says Infinite HP Boss Mode | ZOM-550, ZOM-553, ZOM-562; Trello BETA: Oct 10 list 6851a674975da1fe76e70d93 | AGREE (same feature, base naming) |
| Daily gift / Daily Login / login calendar | ZOM-556 and ZOM-432 say daily gift; the card says Daily Login; row 12 says Login Calendar | ZOM-556, f_a325dd4af80afc5994d5dc, Trello July 18 list 6851a669fb9904d6d136b037 | AGREE (base naming, one feature) |
| Endless, Zombie Lane, Plague Race | as on the live-ops page | page_liveops_calendar, ZOM-517, ZOM-555, ZOM-459 | AGREE |
| Axe Arena, Streak Fever, Nathan's Treasure Hunt | sheet rows; Domino Delights events on the live-ops page; Axe Arena card on Oct 21 | page_liveops_calendar, 6851a7a6c31a93809acded72, C05KNDCHAAG/1758558164.541689 | AGREE |
| Hourly Coins / Hourly Collection | row 2 says Hourly Coins; the Backlog card says Hourly Collection | f_a325dd4af80afc5994d5dc, 68c45bba5d2c25a3a5c26a8c | AGREE (one feature, Backlog) |
| Store builds | Android 0.3.127, iOS 0.3.40 | C0880U9751A/1758643365.607149 (Arthur, Sep 23: required versions) | AGREE |

No roster person is renamed or re-titled. 'Nathan' appears only in the base feature name Nathan's Treasure Hunt, never as a person (fact_check warning dispositioned in the fact sheet).

## 1.C Voice and realism

Seeded speakers, each with its activity.json (synth-cut KB) status at the clock:
- Leonard Hayes (leonard.hayes@harmonygames.co) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: hub, the two line changes, the freeze note, the list rename, the rule doc, the parent and row tickets.
- Vincent Parker (vincent.parker@harmonygames.co) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: QA note, pass log, ticket comments, the DM reply, the channel post.
- Robert (robert@harmonygames.co) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: the ask decision, asks.
- Arthur Blake (arthur.blake@harmonygames.co) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: inline comment, ticket notes.
- Brian Foster (brian.foster@harmonygames.co) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: opinion post, asks.
- Calvin Price (calvin.price@harmonygames.co) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: the Collect & Win ticket, an ask.
- Julia Lawson (julia.lawson@harmonygames.co) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: asks.
- Martin Walsh (martin.walsh@harmonygames.co) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: an ask.
- Oliver Brooks (oliver.brooks@harmonygames.co) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: an ask.
- Owen Baker (owen.baker@harmonygames.co) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: asks.
- Douglas (douglas@harmonygames.co) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds: a comment ask on ZOM-563, which he is assigned.

Lengths and hours from conventions.json (synth-cut KB): slack.length_chars_by_channel_type private p50 51 / p90 156; the seeded one-liners run 60–180 characters and only the hub is long, as a request should be. slack.per_person_hours_and_style: Leonard's core UTC window 15–02, Robert's 14–03, Brian's 12–21, Vincent's 10–19. Every seeded post sits inside its author's window except Vincent's DM reply at 19:40Z, 40 minutes past it on a day he was still in that DM at 18:52Z (D06UFE81RF0/1759171978.790219). linear.states_by_team: DES has 1 In Review and 216 Done in the base; 26 In Review tickets is a visible rise, explained by a batch review under one parent.

Real messages used as voice references:
- Leonard Hayes: "Played 50 levels on 0.3.35 - no major bugs " (C0880U9751A/1757468100.342529) · "I played 50 levels on ipad and 190 levels on iphone since yesterday" (C0880U9751A/1757561459.538129) · "ios build is the best we have had so far" (C0880U9751A/1757561468.193799)
- Vincent Parker: "yeah it should be fixed .<https://harmonygamesgroup.Slack.com/archives/C08R27X0EAH/p1757332040735639>" (C0880U9751A/1757418078.005449) · "Thank you! Remaining ones are not blocker. Can you fix them in a separate branch for now?" (C0880U9751A/1757447035.630449) · "Sure but remaining are not blockers for today. " (C0880U9751A/1757447837.158399)
- Robert: "what levels are hardcoded right now? Can you check? Or can I check somewhere?" (C0880U9751A/1756938765.961369) · "Need to find a way to expose this to us" (C0880U9751A/1756938770.142759) · "so.. what level is it loading from anyways?" (C0880U9751A/1756939901.116369)
- Brian Foster: "We should set these tutorial panels to be visible only once" (C0880U9751A/1758216621.873139)
- Arthur Blake: "That most likely means nothing changed on those objects" (C0880U9751A/1757020274.320379) · "Do they already have MeshColliders?" (C0880U9751A/1757020284.760899) · "Are you getting errors when you update the object list?" (C0880U9751A/1757020485.136389)
- Calvin Price: "I haven't worked on the editor" (C08R27X0EAH/1756749679.654999) · "I sent a PR, is not merged yet" (C08R27X0EAH/1757998397.350669) · "I sent a PR, is not merged yet" (C08R27X0EAH/1758004594.680929)
- Julia Lawson: "No I don't dare :smile:" (C0880U9751A/1757009163.675589) · "No, if yours are working for sure we can just use these" (C0880U9751A/1757011652.972019) · "Yeah I did a second difficulty reduction for the level" (C0880U9751A/1758218113.761459)
- Oliver Brooks: "I'm almost finishing zombie lane issues" (C0880U9751A/1757446973.162829) · "at the start of level 18" (C0880U9751A/1757538645.309739) · "you mean the ftue with the effects popup?" (C0880U9751A/1757616585.405509)

Leonard writes plain, lower-stakes Slack and full sentences when asking for a deliverable; Arthur's ticket notes are one clause, lower case, as his base Slack is; Vincent's are short status lines. No seeded line is tidy prose in a casual channel, and no em dashes are used.

## 1.D Keyword

| Term | Hits / pointer | Note |
|---|---|---|
| "PN sheet / Push Notifications Zombie Match" | f_a325dd4af80afc5994d5dc | found by title words; Leonard's Slack link uses a Google-native id (R04) |
| "Collect & Win" | page_liveops_calendar | the name map; Linear search hits DES-313 |
| "Boss Arena" | ZOM-550, ZOM-553, ZOM-562 | the ask lives on ZOM-542 whose title says home screen |
| "daily gift" | ZOM-556, ZOM-432 | the ask is a comment on the bug |
| "permission" | D06KPMDV2JZ/1752162738.497679, C08R27X0EAH/1755084279.518809 | older dated claims met first; Robert's Sep 29 post is the latest |
| "rollover" | f_a325dd4af80afc5994d5dc | sheet rows; Arthur's comment harmonygames-Games/match3d#248#rc_18 and its mail in samuel.turner@harmonygames.co/1836006988541924555 |
| "NotificationManager" | harmonygames-Games/match3d#248 | the client file; Arthur's ticket notes name it |
| "0.3.127" | C0880U9751A/1758643365.607149 | Arthur's required versions |
| "message rule" | NEW TERM — introduced in f_dc45e0e5a8b8635c1b82b2 | reached through the hub 6fd96f3c3977cee8345e685d31cbc177 or its delegations |
| "Phone message checks" | NEW TERM — introduced in f_8eb8c04713ff6a6ef4a265 | reached through the hub 6fd96f3c3977cee8345e685d31cbc177 or its delegations |
| "Lapsed ladder review" | NEW TERM — introduced in evt_b56d5b19baa0a573da4553 | reached through the hub 6fd96f3c3977cee8345e685d31cbc177 or its delegations |
| "Beta readiness" | NEW TERM — introduced in f_de7a1ae20201816a67750d | reached through the hub 6fd96f3c3977cee8345e685d31cbc177 or its delegations |
| "Beta player messages" | NEW TERM — introduced in DES-314 | reached through the hub 6fd96f3c3977cee8345e685d31cbc177 or its delegations |
| "Your Squad Needs You Back" | NEW TERM — introduced in d2b16907dc8c10fe5052805751097b58 | reached through the hub 6fd96f3c3977cee8345e685d31cbc177 or its delegations |
| "5-minute timers build" | NEW TERM — introduced in 4a5ee02518ff2fbeacaef2fc6d5a9ef9 | reached through the hub 6fd96f3c3977cee8345e685d31cbc177 or its delegations |
| "Held tickets" | NEW TERM — introduced in 68dae8c7d95e24b55b69bf80 | reached through the hub 6fd96f3c3977cee8345e685d31cbc177 or its delegations |
| "Full Ammo" | NEW TERM — introduced in 363d61ffd3daeb6972a01cdb92db9520 | reached through the hub 6fd96f3c3977cee8345e685d31cbc177 or its delegations |
| "Your Squad Is Waiting" | NEW TERM — introduced in evt_f2c03e69f50acf62c9d1c3 | reached through the hub 6fd96f3c3977cee8345e685d31cbc177 or its delegations |
| "Lapsed copy check" | NEW TERM — introduced in evt_f2c03e69f50acf62c9d1c3 | reached through the hub 6fd96f3c3977cee8345e685d31cbc177 or its delegations |
| "teammate sends you lives" | NEW TERM — introduced in cmt_eabac5435f2b3a575aad | reached through the hub 6fd96f3c3977cee8345e685d31cbc177 or its delegations |
| "infinite lives are about to run out" | NEW TERM — introduced in cmt_e2e2926a2080ca53c4ea | reached through the hub 6fd96f3c3977cee8345e685d31cbc177 or its delegations |

## 1.E Persona reach

Load-bearing scoped ids (seeded and base) written to `Working_Files/plan/load_bearing_scoped.txt`; output verbatim. Linear, Trello and GitHub are unscoped, so their ids are not in that list (Evals/references/persona/acl.md).

```
CHECK-SQL as samuel_turner <samuel.turner@harmonygames.co>
[YES LB] L6 gdrive.drive_files insert f_dc45e0e5a8b8635c1b82b2 - file is shared with the persona (shared_with_emails)
[YES LB] L9 gdrive.drive_files insert f_de7a1ae20201816a67750d - file is shared with the persona (shared_with_emails)
[YES LB] L11 gdrive.drive_files insert f_8eb8c04713ff6a6ef4a265 - file is shared with the persona (shared_with_emails)
[YES LB] L13 gdocs.docs_documents insert f_dc45e0e5a8b8635c1b82b2 - file is shared with the persona (shared_with_emails)
[YES LB] L16 gsheets.sheets_spreadsheets insert f_8eb8c04713ff6a6ef4a265 - file is shared with the persona (shared_with_emails)
[YES LB] L19 gsheets.sheets_sheets insert f_8eb8c04713ff6a6ef4a265, f_8eb8c04713ff6a6ef4a265#0 - file is shared with the persona (shared_with_emails)
[YES LB] L21 gslides.slides_presentations insert f_de7a1ae20201816a67750d - file is shared with the persona (shared_with_emails)
[YES LB] L24 gslides.slides_pages insert f_de7a1ae20201816a67750d, slide_7cbfbffe1b54 - file is shared with the persona (shared_with_emails)
[YES LB] L26 gslides.slides_page_elements insert f_de7a1ae20201816a67750d, el_b78f5cefad1f, slide_7cbfbffe1b54 - file is shared with the persona (shared_with_emails)
[YES LB] L28 gslides.slides_page_elements insert f_de7a1ae20201816a67750d, el_9ecdf1278098, slide_7cbfbffe1b54 - file is shared with the persona (shared_with_emails)
[YES LB] L30 slack.slack_messages insert 394f73aa43aa303a755bc81b2cf43840, C0880U9751A/1758909739.853209 - persona EMPLOYEE_0004_SLACK_ID is in members of private zombie-match3d
[YES LB] L33 slack.slack_messages insert 37c5701a1780374401d295e86884f276, C0880U9751A/1759167608.326578 - persona EMPLOYEE_0004_SLACK_ID is in members of private zombie-match3d
[YES LB] L35 slack.slack_messages insert 09aae609aa744fb23288c7dcbac9926c, C0880U9751A/1759170096.924778 - persona EMPLOYEE_0004_SLACK_ID is in members of private zombie-match3d
[YES LB] L37 slack.slack_messages insert d2b16907dc8c10fe5052805751097b58, C08R8CHB0QL/1759169129.445834 - persona EMPLOYEE_0004_SLACK_ID is in members of public zombie-art
[YES LB] L39 slack.slack_messages update a3e78e820b9f880ef4e3d941562110df, C08R8CHB0QL/1759159849.386619 - persona EMPLOYEE_0004_SLACK_ID is in members of public zombie-art
[YES LB] L40 slack.slack_messages insert 4a5ee02518ff2fbeacaef2fc6d5a9ef9, D06UFE81RF0/1759174846.723833 - persona EMPLOYEE_0004_SLACK_ID is in members of im D06UFE81RF0
[YES LB] L42 slack.slack_messages update c42902df5f54c75c1a6e3529cd25121c, D06UFE81RF0/1759163970.141449 - persona EMPLOYEE_0004_SLACK_ID is in members of im D06UFE81RF0
[YES] L43 slack.slack_messages insert 363d61ffd3daeb6972a01cdb92db9520, C0880U9751A/1759245146.720608 - persona EMPLOYEE_0004_SLACK_ID is in members of private zombie-match3d
[YES LB] L45 slack.slack_messages insert 6fd96f3c3977cee8345e685d31cbc177, D06L58XCVKK/1759264851.763895 - persona EMPLOYEE_0004_SLACK_ID is in members of im D06L58XCVKK
[YES LB] L60 gmail.gmail_threads insert samuel.turner@harmonygames.co/1843335316636662321 - row user_email is the persona (samuel.turner@harmonygames.co)
[YES LB] L63 gmail.gmail_messages insert samuel.turner@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com>, s - row user_email is the persona (samuel.turner@harmonygames.co)
[NO] L65 gmail.gmail_threads insert vincent.parker@harmonygames.co/1843335316636098078 - row is in mailbox vincent.parker@harmonygames.co, not the persona's (samuel.turner@harmonygames.co)
[NO] L67 gmail.gmail_messages insert vincent.parker@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com>,  - row is in mailbox vincent.parker@harmonygames.co, not the persona's (samuel.turner@harmonygames.co)
[YES] L69 gmail.gmail_messages insert samuel.turner@harmonygames.co/<[SOURCE_ORG_0001]-Games/match3d/pull/248/review/2963610417@ - row user_email is the persona (samuel.turner@harmonygames.co)
[YES] L71 gmail.gmail_threads insert samuel.turner@harmonygames.co/1844079259288333361 - row user_email is the persona (samuel.turner@harmonygames.co)
[YES] L73 gmail.gmail_messages insert samuel.turner@harmonygames.co/<calendar-811bec31-daa2-c3e0-fc2e-c5ac9baf27a2@google.com>,  - row user_email is the persona (samuel.turner@harmonygames.co)
[YES] L75 gmail.gmail_threads insert samuel.turner@harmonygames.co/1844248505745845006 - row user_email is the persona (samuel.turner@harmonygames.co)
[YES LB] L77 gmail.gmail_messages insert samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com>,  - row user_email is the persona (samuel.turner@harmonygames.co)
[YES] L79 gmail.gmail_threads insert samuel.turner@harmonygames.co/1844638201676793623 - row user_email is the persona (samuel.turner@harmonygames.co)
[YES] L81 gmail.gmail_messages insert samuel.turner@harmonygames.co/<calendar-0faf8717-bf12-6508-09c5-078a904a8076@google.com>,  - row user_email is the persona (samuel.turner@harmonygames.co)
[YES LB] L83 gcal.gcal_events insert evt_b56d5b19baa0a573da4553 - event is on the persona's own calendar samuel.turner@harmonygames.co
[YES] L86 gcal.gcal_events insert evt_8cad40bb558f994b74576a - persona is an attendee and holds its own copy evt_b56d5b19baa0a573da4553 (same ical_uid and start) on samuel.turner@harmonygames.co
[YES] L88 gcal.gcal_events insert evt_f2c03e69f50acf62c9d1c3 - event is on the persona's own calendar samuel.turner@harmonygames.co
[YES] L90 gcal.gcal_events insert evt_bbc253a99f21bfbaa87a7c - persona is an attendee and holds its own copy evt_f2c03e69f50acf62c9d1c3 (same ical_uid and start) on samuel.turner@harmonygames.co
[YES LB] base slack C08R27X0EAH/1755084279.518809 - base record: thread reply inherits channel: persona EMPLOYEE_0004_SLACK_ID is in members of private zombie-bugs
[YES LB] base slack C08R27X0EAH/1758291802.756889 - base record: thread reply inherits channel: persona EMPLOYEE_0004_SLACK_ID is in members of private zombie-bugs
[YES LB] base slack D06KPMDV2JZ/1752162738.497679 - base record: message inherits channel: persona EMPLOYEE_0004_SLACK_ID is in members of im D06KPMDV2JZ
[YES LB] base gdrive d_caafeec2804b3a67ce46aa - base record: persona owns the file
[YES LB] base gdrive f_a325dd4af80afc5994d5dc - base record: file is shared with the persona (shared_with_emails)

summary: {'YES': 32, 'NO': 2}  unscoped rows (always visible): 120
  gcal.gcal_events: {'YES': 4}
  gdocs.docs_documents: {'YES': 1}
  gdrive.drive_files: {'YES': 3}
  gmail.gmail_messages: {'YES': 5, 'NO': 1}
  gmail.gmail_threads: {'YES': 4, 'NO': 1}
  gsheets.sheets_sheets: {'YES': 1}
  gsheets.sheets_spreadsheets: {'YES': 1}
  gslides.slides_page_elements: {'YES': 2}
  gslides.slides_pages: {'YES': 1}
  gslides.slides_presentations: {'YES': 1}
  slack.slack_messages: {'YES': 9}
verdict: PASS (0 load-bearing rows not visible)
```

- D06L58XCVKK — Samuel's DM with Leonard (im member) LB; seeded hub 6fd96f3c3977cee8345e685d31cbc177 (D06L58XCVKK/1759264851.763895).
- D06UFE81RF0 — Samuel's DM with Vincent LB; seeded reply 4a5ee02518ff2fbeacaef2fc6d5a9ef9 under D06UFE81RF0/1759163970.141449.
- C0880U9751A — #zombie-match3d, Samuel a member LB; seeded 37c5701a1780374401d295e86884f276, its reply 09aae609aa744fb23288c7dcbac9926c, 394f73aa43aa303a755bc81b2cf43840.
- C08R8CHB0QL — #zombie-art, Samuel a member LB; seeded reply d2b16907dc8c10fe5052805751097b58 under C08R8CHB0QL/1759159849.386619.
- Samuel's mailbox LB: samuel.turner@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com>, the GitHub mail in samuel.turner@harmonygames.co/1836006988541924555, samuel.turner@harmonygames.co/<calendar-811bec31-daa2-c3e0-fc2e-c5ac9baf27a2@google.com>, samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com>.
- Drive LB: f_dc45e0e5a8b8635c1b82b2, f_de7a1ae20201816a67750d, f_8eb8c04713ff6a6ef4a265 are shared with Samuel; f_a325dd4af80afc5994d5dc is shared with him in the base; d_caafeec2804b3a67ce46aa is his root.
- Calendar LB: evt_b56d5b19baa0a573da4553 is Samuel's own copy (self:true).
- Unscoped: DES-314, DES-313 to DES-345, ZOM-542, ZOM-556, ZOM-563, ZOM-483, cmt_f1b8a109dfa70cdc4565, cmt_2b519285937e7fa79453, cmt_eabac5435f2b3a575aad, cmt_e2e2926a2080ca53c4ea, 6851a769c65dc0017a227bb7, 68d1eb90bef538c7c5c5599d, 68dae8c7d95e24b55b69bf80, harmonygames-Games/match3d#248#rc_18.
- No designed denial: denied_probes is empty; other people's mailbox and calendar copies are companions, never evidence (evt_b56d5b19baa0a573da4553 is cited by Samuel's own copy).

## 1.F Collision

base_check Check A compares every minted id against the full base collections (output in the Self-review, PASS). Scheme by service:
- linear: DES-313 to DES-345: base DES ends at DES-312 (linear data.json, 3,687 synth-cut issues read in full); 36 issues carry cmt_ + 20 hex comment ids and the base has 0 comments.
- slack: 7 seeded (channel, ts) pairs, ids 394f73aa43aa303a755bc81b2cf43840, 37c5701a1780374401d295e86884f276, 09aae609aa744fb23288c7dcbac9926c, d2b16907dc8c10fe5052805751097b58, 4a5ee02518ff2fbeacaef2fc6d5a9ef9, 363d61ffd3daeb6972a01cdb92db9520, 6fd96f3c3977cee8345e685d31cbc177: no base message in those channels at those ts (messages/C0880U9751A/2025-09.json, messages/C08R8CHB0QL/2025-09.json, messages/D06UFE81RF0/2025-09.json, messages/D06L58XCVKK/2025-09.json).
- gmail: thread ids and RFC Message-IDs minted per seeded time; the GitHub message id samuel.turner@harmonygames.co/<[SOURCE_ORG_0001]-Games/match3d/pull/248/review/2963610417@github.com> is a new review number between the base review mails 2963243580 and 2963696884.
- trello: 68dae8c7d95e24b55b69bf80, 68d415a716abcb84070a8e2a, 68dc20c6d5fbf6ab70025295: first 8 hex are the action's own seconds.
- drive/calendar: f_dc45e0e5a8b8635c1b82b2, f_de7a1ae20201816a67750d, f_8eb8c04713ff6a6ef4a265, evt_b56d5b19baa0a573da4553, evt_f2c03e69f50acf62c9d1c3: sha-derived, 0 base hits.
- github: harmonygames-Games/match3d#248#rc_18 and harmonygames-Games/match3d#248#rev_7: base ids on this PR end at rc_17 and rev_6.
- Header tokens: none minted; PERSON_6094_TRELLO_USER_ID, SVC_0248, SVC_3649, SVC_0613, SVC_5111 and SVC_0842 are the base tokens those mails use. Body tokens: none minted.

## Record ledger

One row per SQL statement, in SQL order.

| # | SQL line | Table | Id | Manifest element | Carrier | Reach | Discovery role |
|---|---|---|---|---|---|---|---|
| 1 | L6 | gdrive.drive_files | f_dc45e0e5a8b8635c1b82b2 | H1, K2, T3, T8 | ● | shared with the persona | claim met first |
| 2 | L9 | gdrive.drive_files | f_de7a1ae20201816a67750d | T10 | ● | shared with the persona | evidence |
| 3 | L11 | gdrive.drive_files | f_8eb8c04713ff6a6ef4a265 | T16, T4 | ● | shared with the persona | claim met first |
| 4 | L13 | gdocs.docs_documents | f_dc45e0e5a8b8635c1b82b2 | H1, K2, T3, T8 | ● | shared with the persona | claim met first |
| 5 | L16 | gsheets.sheets_spreadsheets | f_8eb8c04713ff6a6ef4a265 | T16, T4 | ● | shared with the persona | claim met first |
| 6 | L19 | gsheets.sheets_sheets | f_8eb8c04713ff6a6ef4a265#Beta | T16, T4 | ● | shared with the persona | evidence |
| 7 | L21 | gslides.slides_presentations | f_de7a1ae20201816a67750d | T10 | ● | shared with the persona | evidence |
| 8 | L24 | gslides.slides_pages | f_de7a1ae20201816a67750d#slide_7cbfbffe1b54 | T10 | ● | shared with the persona | evidence |
| 9 | L26 | gslides.slides_page_elements | f_de7a1ae20201816a67750d#el_b78f5cefad1f | T10 | ● | shared with the persona | evidence |
| 10 | L28 | gslides.slides_page_elements | f_de7a1ae20201816a67750d#el_9ecdf1278098 | T10 | ● | shared with the persona | evidence |
| 11 | L30 | slack.slack_messages | 394f73aa43aa303a755bc81b2cf43840 | T12 | ● | persona in channel | evidence |
| 12 | L33 | slack.slack_messages | 37c5701a1780374401d295e86884f276 | K9, T3, T9 | ● | persona in channel | overturning |
| 13 | L35 | slack.slack_messages | 09aae609aa744fb23288c7dcbac9926c | T3 | ● | persona in channel | evidence |
| 14 | L37 | slack.slack_messages | d2b16907dc8c10fe5052805751097b58 | K11, T2 | ● | persona in channel | claim met first |
| 15 | L39 | slack.slack_messages (UPDATE) | a3e78e820b9f880ef4e3d941562110df | companion: reply counters (Q01) | ● | persona in channel | companion |
| 16 | L40 | slack.slack_messages | 4a5ee02518ff2fbeacaef2fc6d5a9ef9 | T4 | ● | persona in channel | overturning |
| 17 | L42 | slack.slack_messages (UPDATE) | c42902df5f54c75c1a6e3529cd25121c | companion: reply counters (Q01) | ● | persona in channel | companion |
| 18 | L43 | slack.slack_messages | 363d61ffd3daeb6972a01cdb92db9520 | K21, T16 | ● | persona in channel | overturning |
| 19 | L45 | slack.slack_messages | 6fd96f3c3977cee8345e685d31cbc177 | A1, K1 | ● | persona in channel | first link |
| 20 | L47 | trello.trello_actions | 68d41578905712b474fbc0ca | cohort | ● | unscoped | evidence |
| 21 | L50 | trello.trello_cards (UPDATE) | 6851a769c65dc0017a227bb7 | companion: card badge and activity (T06) | ● | unscoped | companion |
| 22 | L51 | trello.trello_actions | 68d415a716abcb84070a8e2a | K6 | ● | unscoped | evidence |
| 23 | L53 | trello.trello_cards (UPDATE) | 6851a769c65dc0017a227bb7 | companion: card badge and activity (T06) | ● | unscoped | companion |
| 24 | L54 | trello.trello_actions | 68dae8c7d95e24b55b69bf80 | H3, K10, T8 | ● | unscoped | overturning |
| 25 | L56 | trello.trello_cards (UPDATE) | 68d1eb90bef538c7c5c5599d | companion: card badge and activity (T06) | ● | unscoped | companion |
| 26 | L57 | trello.trello_actions | 68dc20c6d5fbf6ab70025295 | cohort | ● | unscoped | evidence |
| 27 | L59 | trello.trello_boards (UPDATE) | 6851a6569f3bf818760632ab | companion: card badge and activity (T06) | ● | unscoped | companion |
| 28 | L60 | gmail.gmail_threads | samuel.turner@harmonygames.co/1843335316636662321 | H2, K8, T4 | ● | persona mailbox | authority |
| 29 | L63 | gmail.gmail_messages | samuel.turner@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com> | H2, K8, T4 | ● | persona mailbox | authority |
| 30 | L65 | gmail.gmail_threads | vincent.parker@harmonygames.co/1843335316636098078 | thread row of the message below | ● | sender's copy (companion, not evidence) | evidence |
| 31 | L67 | gmail.gmail_messages | vincent.parker@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com> | H2, K8, T4 | ● | sender's copy (companion, not evidence) | evidence |
| 32 | L69 | gmail.gmail_messages | samuel.turner@harmonygames.co/<[SOURCE_ORG_0001]-Games/match3d/pull/248/review/2963610417@github.com> | T1 companion INT-12 | ● | persona mailbox | companion |
| 33 | L71 | gmail.gmail_threads | samuel.turner@harmonygames.co/1844079259288333361 | thread row of the message below | ● | persona mailbox | evidence |
| 34 | L73 | gmail.gmail_messages | samuel.turner@harmonygames.co/<calendar-811bec31-daa2-c3e0-fc2e-c5ac9baf27a2@google.com> | T7 companion INT-11 | ● | persona mailbox | companion |
| 35 | L75 | gmail.gmail_threads | samuel.turner@harmonygames.co/1844248505745845006 | thread row of the message below | ● | persona mailbox | evidence |
| 36 | L77 | gmail.gmail_messages | samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com> | T7 companion INT-11 | ● | persona mailbox | companion |
| 37 | L79 | gmail.gmail_threads | samuel.turner@harmonygames.co/1844638201676793623 | thread row of the message below | ● | persona mailbox | evidence |
| 38 | L81 | gmail.gmail_messages | samuel.turner@harmonygames.co/<calendar-0faf8717-bf12-6508-09c5-078a904a8076@google.com> | cohort | ● | persona mailbox | evidence |
| 39 | L83 | gcal.gcal_events | evt_b56d5b19baa0a573da4553 | K16, T7 | ● (summary, attendees, time, status; description ○) | persona calendar | evidence |
| 40 | L86 | gcal.gcal_events | evt_8cad40bb558f994b74576a | T7 | ● (summary, attendees, time, status; description ○) | organizer's copy (companion) | evidence |
| 41 | L88 | gcal.gcal_events | evt_f2c03e69f50acf62c9d1c3 | K20, T2, T7 | ● (summary, attendees, time, status; description ○) | persona calendar | overturning |
| 42 | L90 | gcal.gcal_events | evt_bbc253a99f21bfbaa87a7c | T7 | ● (summary, attendees, time, status; description ○) | organizer's copy (companion) | evidence |
| 43 | L92 | github.github_review_comments | harmonygames-Games/match3d#248#rc_18 | K12, T1 | ● | unscoped | evidence |
| 44 | L95 | github.github_reviews | harmonygames-Games/match3d#248#rev_7 | cohort | ● | unscoped | evidence |
| 45 | L97 | linear.linear_team_memberships | tmem_team_DES_usr_49b9dfa5208d400d | write access for R6 on DES-314 | ● | unscoped | evidence |
| 46 | L100 | linear.linear_team_memberships | tmem_team_DES_usr_caafeec2804b3a67 | write access for R6 on DES-314 | ● | unscoped | evidence |
| 47 | L102 | linear.linear_team_memberships | tmem_team_DES_usr_51f5f16d46e8cf55 | write access for R6 on DES-314 | ● | unscoped | evidence |
| 48 | L104 | linear.linear_team_memberships | tmem_team_DES_usr_bdf01b53c6a92c5e | write access for R6 on DES-314 | ● | unscoped | evidence |
| 49 | L106 | linear.linear_issues | DES-313 | T5, cohort: Win & Collect start | ● | unscoped | evidence |
| 50 | L108 | linear.linear_issues | DES-314 | K4, K4 parent | ● | unscoped | evidence |
| 51 | L110 | linear.linear_issues | DES-315 | cohort: Lives recharged | ● | unscoped | evidence |
| 52 | L112 | linear.linear_issues | DES-316 | cohort: Lapsed 1 day | ● | unscoped | evidence |
| 53 | L114 | linear.linear_issues | DES-317 | T2, cohort: Lapsed 7 days | ● | unscoped | claim met first |
| 54 | L116 | linear.linear_issues | DES-318 | cohort: Finish first mission | ● | unscoped | evidence |
| 55 | L118 | linear.linear_issues | DES-319 | cohort: Plague Race | ● | unscoped | evidence |
| 56 | L120 | linear.linear_issues | DES-320 | cohort: Weekly Leaderboard reset | ● | unscoped | evidence |
| 57 | L122 | linear.linear_issues | DES-321 | cohort: Quests rollover | ● | unscoped | evidence |
| 58 | L124 | linear.linear_issues | DES-322 | cohort: Login Calendar update | ● | unscoped | evidence |
| 59 | L126 | linear.linear_issues | DES-323 | cohort: Season Pass start | ● | unscoped | evidence |
| 60 | L128 | linear.linear_issues | DES-324 | cohort: Hourly Coins | ● | unscoped | evidence |
| 61 | L130 | linear.linear_issues | DES-325 | cohort: Nathan's Treasure Hunt | ● | unscoped | evidence |
| 62 | L132 | linear.linear_issues | DES-326 | cohort: Streak Fever | ● | unscoped | evidence |
| 63 | L134 | linear.linear_issues | DES-327 | cohort: Axe Arena | ● | unscoped | evidence |
| 64 | L136 | linear.linear_issues | DES-328 | cohort: Endless entries back | ● | unscoped | evidence |
| 65 | L138 | linear.linear_issues | DES-329 | cohort: Endless weekly result | ● | unscoped | evidence |
| 66 | L140 | linear.linear_issues | DES-330 | cohort: Boss Arena open | ● | unscoped | evidence |
| 67 | L142 | linear.linear_issues | DES-331 | cohort: Boss Arena last hours | ● | unscoped | evidence |
| 68 | L144 | linear.linear_issues | DES-332 | cohort: Season Pass last 48 hours | ● | unscoped | evidence |
| 69 | L146 | linear.linear_issues | DES-333 | cohort: Season Pass premium nudge | ● | unscoped | evidence |
| 70 | L148 | linear.linear_issues | DES-334 | cohort: Plague Race last hour | ● | unscoped | evidence |
| 71 | L150 | linear.linear_issues | DES-335 | cohort: Plague Race result | ● | unscoped | evidence |
| 72 | L152 | linear.linear_issues | DES-336 | cohort: Zombie Lane reward ready | ● | unscoped | evidence |
| 73 | L154 | linear.linear_issues | DES-337 | cohort: Achievement reward waiting | ● | unscoped | evidence |
| 74 | L156 | linear.linear_issues | DES-338 | cohort: Daily chest ready | ● | unscoped | evidence |
| 75 | L158 | linear.linear_issues | DES-339 | cohort: Free shop coins ready | ● | unscoped | evidence |
| 76 | L160 | linear.linear_issues | DES-340 | cohort: Support reply waiting | ● | unscoped | evidence |
| 77 | L162 | linear.linear_issues | DES-341 | cohort: New levels added | ● | unscoped | evidence |
| 78 | L164 | linear.linear_issues | DES-342 | cohort: Lapsed 3 days | ● | unscoped | evidence |
| 79 | L166 | linear.linear_issues | DES-343 | cohort: Lapsed 30 days | ● | unscoped | evidence |
| 80 | L168 | linear.linear_issues | DES-344 | T7, cohort: Lapsed 14 days | ● | unscoped | evidence |
| 81 | L170 | linear.linear_issues | DES-345 | cohort: Comeback gift | ● | unscoped | evidence |
| 82 | L172 | linear.linear_comments | cmt_7c6c022293a0505fbf85 | cohort: Win & Collect start | ● (§6b) | unscoped | evidence |
| 83 | L174 | linear.linear_comments | cmt_cb634ee40df2ae6c6022 | cohort: Win & Collect start | ● (§6b) | unscoped | evidence |
| 84 | L176 | linear.linear_comments | cmt_2395189dfd5e7d5c1e88 | cohort: Lives recharged | ● (§6b) | unscoped | evidence |
| 85 | L178 | linear.linear_comments | cmt_51e018b23e18c2f680cd | T16, cohort: Lives recharged | ● (§6b) | unscoped | claim met first |
| 86 | L180 | linear.linear_comments | cmt_d6bf99cc8b3e926c2569 | cohort: Lapsed 1 day | ● (§6b) | unscoped | evidence |
| 87 | L182 | linear.linear_comments | cmt_5ab75e0ee96e70745960 | cohort: Lapsed 1 day | ● (§6b) | unscoped | evidence |
| 88 | L184 | linear.linear_comments | cmt_f64ebdf08bef6b136513 | cohort: Lapsed 7 days | ● (§6b) | unscoped | evidence |
| 89 | L186 | linear.linear_comments | cmt_e4bb9fe925b86f52cf55 | cohort: Lapsed 7 days | ● (§6b) | unscoped | evidence |
| 90 | L188 | linear.linear_comments | cmt_886fb8b04e3b6ba66b57 | cohort: Finish first mission | ● (§6b) | unscoped | evidence |
| 91 | L190 | linear.linear_comments | cmt_f4960d3c073493b6bfc6 | T3, cohort: Finish first mission | ● (§6b) | unscoped | evidence |
| 92 | L192 | linear.linear_comments | cmt_10ae5518084785a96cfc | cohort: Plague Race | ● (§6b) | unscoped | evidence |
| 93 | L194 | linear.linear_comments | cmt_fd950c410ed25c447c02 | T4, cohort: Plague Race | ● (§6b) | unscoped | claim met first |
| 94 | L196 | linear.linear_comments | cmt_9338bb2c286a6c207792 | cohort: Plague Race | ● (§6b) | unscoped | evidence |
| 95 | L198 | linear.linear_comments | cmt_f1b42e3a7c9cfa136439 | cohort: Weekly Leaderboard reset | ● (§6b) | unscoped | evidence |
| 96 | L200 | linear.linear_comments | cmt_f76672cf21387ec1eeab | T1, cohort: Weekly Leaderboard reset | ● (§6b) | unscoped | evidence |
| 97 | L202 | linear.linear_comments | cmt_4aa525e0162ec9ef15f6 | cohort: Quests rollover | ● (§6b) | unscoped | evidence |
| 98 | L204 | linear.linear_comments | cmt_7b184259cfbb33052325 | cohort: Quests rollover | ● (§6b) | unscoped | evidence |
| 99 | L206 | linear.linear_comments | cmt_8531c2616065b39e5c26 | cohort: Login Calendar update | ● (§6b) | unscoped | evidence |
| 100 | L208 | linear.linear_comments | cmt_5acbc1a3f111af34e7ac | cohort: Login Calendar update | ● (§6b) | unscoped | evidence |
| 101 | L210 | linear.linear_comments | cmt_3dabe2da836af3cc9ba8 | cohort: Season Pass start | ● (§6b) | unscoped | evidence |
| 102 | L212 | linear.linear_comments | cmt_181bcd11a979359893fb | cohort: Season Pass start | ● (§6b) | unscoped | evidence |
| 103 | L214 | linear.linear_comments | cmt_144462e04c0e02c19d02 | cohort: Hourly Coins | ● (§6b) | unscoped | evidence |
| 104 | L216 | linear.linear_comments | cmt_8c9ab0f70f9ab1dc5d5f | cohort: Hourly Coins | ● (§6b) | unscoped | evidence |
| 105 | L218 | linear.linear_comments | cmt_4478b09dc764fe7e1cd1 | cohort: Nathan's Treasure Hunt | ● (§6b) | unscoped | evidence |
| 106 | L220 | linear.linear_comments | cmt_64fc795e9c80b7c68a7e | cohort: Nathan's Treasure Hunt | ● (§6b) | unscoped | evidence |
| 107 | L222 | linear.linear_comments | cmt_84609a55e9bb01533c18 | cohort: Streak Fever | ● (§6b) | unscoped | evidence |
| 108 | L224 | linear.linear_comments | cmt_5d85e7a910a89f7e0eeb | cohort: Streak Fever | ● (§6b) | unscoped | evidence |
| 109 | L226 | linear.linear_comments | cmt_5a45fa6ed829ce69c092 | cohort: Axe Arena | ● (§6b) | unscoped | evidence |
| 110 | L228 | linear.linear_comments | cmt_842c9cb4757414e145d3 | cohort: Axe Arena | ● (§6b) | unscoped | evidence |
| 111 | L230 | linear.linear_comments | cmt_55c7d795dc967c39c6a5 | cohort: Endless entries back | ● (§6b) | unscoped | evidence |
| 112 | L232 | linear.linear_comments | cmt_c6f09d1660c6a174811f | cohort: Endless entries back | ● (§6b) | unscoped | evidence |
| 113 | L234 | linear.linear_comments | cmt_6e27d2eb839bbc66a95a | cohort: Endless weekly result | ● (§6b) | unscoped | evidence |
| 114 | L236 | linear.linear_comments | cmt_9d5748e1540a9588ceb9 | cohort: Endless weekly result | ● (§6b) | unscoped | evidence |
| 115 | L238 | linear.linear_comments | cmt_c6a61568172ef0ebb990 | cohort: Boss Arena open | ● (§6b) | unscoped | evidence |
| 116 | L240 | linear.linear_comments | cmt_e4ac33987005778b372e | cohort: Boss Arena open | ● (§6b) | unscoped | evidence |
| 117 | L242 | linear.linear_comments | cmt_d9f2d461e083b4a65263 | cohort: Boss Arena last hours | ● (§6b) | unscoped | evidence |
| 118 | L244 | linear.linear_comments | cmt_e1c7ebcf5aa9ee4b4a8c | cohort: Boss Arena last hours | ● (§6b) | unscoped | evidence |
| 119 | L246 | linear.linear_comments | cmt_e911c52cf054cb3ed19b | cohort: Season Pass last 48 hours | ● (§6b) | unscoped | evidence |
| 120 | L248 | linear.linear_comments | cmt_44a1117f30fbb476c28c | cohort: Season Pass last 48 hours | ● (§6b) | unscoped | evidence |
| 121 | L250 | linear.linear_comments | cmt_2456f47526183e4e1161 | cohort: Season Pass premium nudge | ● (§6b) | unscoped | evidence |
| 122 | L252 | linear.linear_comments | cmt_ff7c43f0633261872ec7 | cohort: Season Pass premium nudge | ● (§6b) | unscoped | evidence |
| 123 | L254 | linear.linear_comments | cmt_abb99f26dc3013206909 | cohort: Plague Race last hour | ● (§6b) | unscoped | evidence |
| 124 | L256 | linear.linear_comments | cmt_521d7e03d14d535f1d5b | cohort: Plague Race last hour | ● (§6b) | unscoped | evidence |
| 125 | L258 | linear.linear_comments | cmt_83e42df52254cf27fe4d | cohort: Plague Race result | ● (§6b) | unscoped | evidence |
| 126 | L260 | linear.linear_comments | cmt_fda157bae8336585356a | cohort: Plague Race result | ● (§6b) | unscoped | evidence |
| 127 | L262 | linear.linear_comments | cmt_546a8f6d521e2d00dc28 | cohort: Zombie Lane reward ready | ● (§6b) | unscoped | evidence |
| 128 | L264 | linear.linear_comments | cmt_b55d6a0b35ae5242ffd4 | cohort: Zombie Lane reward ready | ● (§6b) | unscoped | evidence |
| 129 | L266 | linear.linear_comments | cmt_cd8081a714a205760ce7 | cohort: Achievement reward waiting | ● (§6b) | unscoped | evidence |
| 130 | L268 | linear.linear_comments | cmt_4feec391e19bb4a4a16a | cohort: Achievement reward waiting | ● (§6b) | unscoped | evidence |
| 131 | L270 | linear.linear_comments | cmt_b770ad38987fc947c65f | cohort: Daily chest ready | ● (§6b) | unscoped | evidence |
| 132 | L272 | linear.linear_comments | cmt_32da06fe646ada57c7fa | cohort: Daily chest ready | ● (§6b) | unscoped | evidence |
| 133 | L274 | linear.linear_comments | cmt_e0e37d68814e1eae6002 | cohort: Free shop coins ready | ● (§6b) | unscoped | evidence |
| 134 | L276 | linear.linear_comments | cmt_aa68a0b0ee32e8e24c58 | cohort: Free shop coins ready | ● (§6b) | unscoped | evidence |
| 135 | L278 | linear.linear_comments | cmt_a6c862db8697a973afc7 | cohort: Support reply waiting | ● (§6b) | unscoped | evidence |
| 136 | L280 | linear.linear_comments | cmt_31db977b4adf091259da | cohort: Support reply waiting | ● (§6b) | unscoped | evidence |
| 137 | L282 | linear.linear_comments | cmt_904474dee7687823b700 | cohort: New levels added | ● (§6b) | unscoped | evidence |
| 138 | L284 | linear.linear_comments | cmt_96b8c0e10b3d2b20a982 | cohort: New levels added | ● (§6b) | unscoped | evidence |
| 139 | L286 | linear.linear_comments | cmt_1443f47829522f8bb44e | cohort: Lapsed 3 days | ● (§6b) | unscoped | evidence |
| 140 | L288 | linear.linear_comments | cmt_af799d5941e425ad3e53 | cohort: Lapsed 3 days | ● (§6b) | unscoped | evidence |
| 141 | L290 | linear.linear_comments | cmt_fe5087128f529fdbb69f | cohort: Lapsed 30 days | ● (§6b) | unscoped | evidence |
| 142 | L292 | linear.linear_comments | cmt_58672546fb6435495753 | cohort: Lapsed 30 days | ● (§6b) | unscoped | evidence |
| 143 | L294 | linear.linear_comments | cmt_fd99936084694fa6d973 | cohort: Lapsed 14 days | ● (§6b) | unscoped | evidence |
| 144 | L296 | linear.linear_comments | cmt_8c95a627941e0b32e091 | cohort: Comeback gift | ● (§6b) | unscoped | evidence |
| 145 | L298 | linear.linear_comments | cmt_13477aa8d1468ae11c9d | cohort: Comeback gift | ● (§6b) | unscoped | evidence |
| 146 | L300 | linear.linear_comments | cmt_e2e2926a2080ca53c4ea | K19, T6, cohort: ZOM-483 | ● (§6b) | unscoped | evidence |
| 147 | L302 | linear.linear_comments | cmt_f1b8a109dfa70cdc4565 | K13, T6, cohort: ZOM-542 | ● (§6b) | unscoped | evidence |
| 148 | L304 | linear.linear_comments | cmt_2b519285937e7fa79453 | K14, T6, cohort: ZOM-556 | ● (§6b) | unscoped | evidence |
| 149 | L306 | linear.linear_comments | cmt_eabac5435f2b3a575aad | K18, T6, cohort: ZOM-563 | ● (§6b) | unscoped | evidence |
| 150 | L308 | linear.linear_issues (UPDATE) | ZOM-542 | companion: relation back and updated_at | ● | unscoped | companion |
| 151 | L309 | linear.linear_issues (UPDATE) | ZOM-556 | companion: relation back and updated_at | ● | unscoped | companion |
| 152 | L310 | linear.linear_issues (UPDATE) | ZOM-563 | companion: relation back and updated_at | ● | unscoped | companion |
| 153 | L311 | linear.linear_issues (UPDATE) | ZOM-483 | companion: relation back and updated_at | ● | unscoped | companion |
| 154 | L312 | linear.linear_teams (UPDATE) | team_DES | companion: team counter for R6 | ● | unscoped | companion |

## Findability and discovery-order proofs

- Hub A1 6fd96f3c3977cee8345e685d31cbc177 (D06L58XCVKK/1759264851.763895): the newest message in Leonard and Samuel's DM; the prompt names it; first link.
- Rule doc H1 f_dc45e0e5a8b8635c1b82b2: the hub says 'the message rule doc'; a Docs or Drive search for 'message rule' returns it; decoy f_ffbe775ff72a994c5d6b7c (GTM - Beta, Domino Delights 2024) differs on the game.
- QA note H2 samuel.turner@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com>: the rule doc says 'his QA note'; Gmail search 'phone messages' or from Vincent returns it; decoy page_release_checklist is the whole-build submission list.
- Freeze H3 68dae8c7d95e24b55b69bf80 on 68d1eb90bef538c7c5c5599d: the rule doc says 'unless the roadmap says otherwise'; Trello search 'Held tickets' or reading the BETA list's card descriptions; decoy 68c451141c69fb8af1b4568e is for bug tickets.
- T1 DONE: claim met first: Status Ready on f_a325dd4af80afc5994d5dc, DES-320 Done with Vincent's cmt_f76672cf21387ec1eeab, harmonygames-Games/match3d#248#rev_6 APPROVED; overturned by harmonygames-Games/match3d#248#rc_18 (Jun 26) and the schedule in the same hunk; decisive because the rule's test 5 asks for the day and the row says rollover.
- T2 CORR: claim met first: the June line on row 5 and DES-317; overturned by d2b16907dc8c10fe5052805751097b58 (Sep 29 18:05Z) under C08R8CHB0QL/1759159849.386619; a search for 'taken over' finds it.
- T3 DEP: claim met first: LIVE and Ready on row 6, Vincent's cmt_f4960d3c073493b6bfc6; overturned by the join of the row's Level 20 trigger, the reach sentence in f_dc45e0e5a8b8635c1b82b2 and 37c5701a1780374401d295e86884f276.
- T4 QA: claim met first: cmt_fd950c410ed25c447c02 and f_8eb8c04713ff6a6ef4a265; overturned by 4a5ee02518ff2fbeacaef2fc6d5a9ef9 (Sep 29 19:40Z) under D06UFE81RF0/1759163970.141449 with samuel.turner@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com>.
- T5 ALIAS: claim met first: no child of DES-314 for row 7; overturned by page_liveops_calendar and DES-313.
- T6 FILT: DES-330 relates to ZOM-542 and DES-338 to ZOM-556 in linear_list_issues; the asks are cmt_f1b8a109dfa70cdc4565 and cmt_2b519285937e7fa79453.
- T7 BUILT: claim met first: DES-344 reads as new; overturned by the batch in harmonygames-Games/match3d#248 and samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com>.
- T8 FOLLOW: claim met first: the rule doc's last sentence; overturned by 68dae8c7d95e24b55b69bf80 (Sep 29, after the doc's Sep 26).
- T9: claim met first: D06KPMDV2JZ/1752162738.497679, C08R27X0EAH/1755084279.518809; overturned by 37c5701a1780374401d295e86884f276.

## Self-validation

| QC category | Tool-enforced (result) | Manual (evidence) |
|---|---|---|
| Missing Universe Data | check-sql PASS (1.E) | every deciding fact persona-readable: harmonygames-Games/match3d#248#rc_18, d2b16907dc8c10fe5052805751097b58, 37c5701a1780374401d295e86884f276, 4a5ee02518ff2fbeacaef2fc6d5a9ef9, cmt_f1b8a109dfa70cdc4565, cmt_2b519285937e7fa79453, samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com>, 68dae8c7d95e24b55b69bf80, 363d61ffd3daeb6972a01cdb92db9520, evt_f2c03e69f50acf62c9d1c3, cmt_eabac5435f2b3a575aad, cmt_e2e2926a2080ca53c4ea |
| Temporal Field | sql_lint 0 errors; base_check Check C PASS | harmonygames-Games/match3d#248#rc_18 (Jun 26 20:58Z) precedes rev_6 and the merge; the rule doc (Sep 26) precedes the freeze (Sep 29) that amends it; the hub (Sep 30) is last |
| Cross-service Referential | base_check Check A PASS | Arthur's required versions C0880U9751A/1758643365.607149 match cmt_f76672cf21387ec1eeab; DES-330/ZOM-542 and DES-338/ZOM-556 relate both ways |
| Quantitative | reply counters and Trello badges updated | the deck's six equals the six Ready rows on f_a325dd4af80afc5994d5dc; C08R8CHB0QL/1759159849.386619 goes from 3 replies to 4 |
| State / Lifecycle | six Done tickets have completed_at after their last comment | DES-314 stays In Progress with open children (L06 excluded); no comment on a closed ticket |
| Identifier / Format | eval lint FAIL 0 CHECK 0 | ids follow base schemes (1.A, 1.F) |
| Semantic / Category | — | titles match content: f_dc45e0e5a8b8635c1b82b2, f_8eb8c04713ff6a6ef4a265, evt_b56d5b19baa0a573da4553, f_de7a1ae20201816a67750d |
| Other | — | voice per 1.C; no record states a call, a total or the plan |

## Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| github | INT-01 | Slack copy of the inline comment | none: harmonygames-Games/match3d#248#rc_18 (Jun 26) predates the match3d window that opens Jun 30 (integrations.json) |
| github | INT-12 | GitHub mail to Samuel | seeded in the base PR thread: samuel.turner@harmonygames.co/<[SOURCE_ORG_0001]-Games/match3d/pull/248/review/2963610417@github.com> |
| github | INT-23 | CodeRabbit | none: a human comment |
| linear | INT-03, INT-04, INT-05 | PR comment, Slack, mail notifications | none: the base has 0 Linear comments and no notification for them (Ask_Carriers §6b) |
| gcal | INT-11 | invitation and cancellation mails | seeded for evt_b56d5b19baa0a573da4553: samuel.turner@harmonygames.co/<calendar-811bec31-daa2-c3e0-fc2e-c5ac9baf27a2@google.com>, samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com> |
| gdrive | INT-13 | Drive share DMs | none: f_dc45e0e5a8b8635c1b82b2 and f_8eb8c04713ff6a6ef4a265 follow the base pattern of owner shares with no DM |
| slack | INT-22 | Slack mail digests | none (D06L58XCVKK/1759264851.763895) |
| trello | INT-21 | none exists | none (68dae8c7d95e24b55b69bf80) |
| gdocs, gsheets, gslides, gmail | not integration sources | — | none |

## Touched-data census and coherence hazards

Touched data: 6fd96f3c3977cee8345e685d31cbc177, f_dc45e0e5a8b8635c1b82b2, f_a325dd4af80afc5994d5dc (all four tabs), f_8eb8c04713ff6a6ef4a265, samuel.turner@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com>, tickets DES-313 to DES-345, ZOM-542, ZOM-556, ZOM-397, ZOM-366, ZOM-471, ZOM-539; ZM ROADMAP lists 6851a674975da1fe76e70d93, 6851a677e090018224fb8c7f, 68c451221ebabaf255a7d16b and cards 6851a769c65dc0017a227bb7, 68d1eb90bef538c7c5c5599d, 6851a7a6c31a93809acded72, 68c45bba5d2c25a3a5c26a8c; harmonygames-Games/match3d#248 with its review comments; page_liveops_calendar; the Sep 15 week of USER_COHORT_RETENTION; #zombie-bugs and #zombie-match3d around the ask point (C08R27X0EAH/1755084279.518809, C08R27X0EAH/1758238811.686629, C08R27X0EAH/1758239520.618939).

Hazards from coherence_hazards.json:
- temporal: T06 — both Trello comments update dateLastActivity (companions); T02 not touched: no thread file is read for order.
- semantic: S01 — no row depends on ENG keys cited for ZOM work.
- referential: R03 — no row reads a redacted GitHub subject; R04 — no row depends on a Google-native link; R07 — no #zombie-prs copy of harmonygames-Games/match3d#248#rc_18, declared under Integrations.
- quantitative: Q01 — the seeded replies update the roots' reply_count, reply_users_count and latest_reply (C08R8CHB0QL/1759159849.386619, D06UFE81RF0/1759163970.141449).
- state/lifecycle: L06 — DES-314 is never Done; L03 — calls rest on the rule tests, never on a ticket state as proof of shipping; L08 — no seeded ticket is assigned to a quiet person.
- identifier/format: I14 — the sheet's owner is a Resource id, so it is never a write target; I15 — the Drive name keeps .xlsx; I16 — Trello ids encode their action time.

Known data issues (references/known_data_issues/synthcut.md; no load-bearing fact, trap or graded slot rests on a card's 'Don't grade' value):
- SC-7: channel lists: membership is used only for reach, never graded.
- SC-13: the list is named BETA: Oct 10: no date is graded, only 'on the BETA list'.
- SC-14: no complete flag is read.
- SC-16: no ticket state is proof of shipping; seeded DES tickets only.
- SC-19: no telemetry version matching; the store versions come from Arthur's Sep 23 post.
- SC-28: the note uses the warehouse's Sep 15 week, never the OKR page.
- SC-36: no invite or channel list is graded.
- SC-38: Season Pass rests on nothing being scheduled, never on a ship date.
- SC-57: no post in #zm-collect-win.
- SC-68: only 'in the beta' is used for Boss Arena, from the BETA list.
- SC-70: no timezone is graded.

## Intended disagreements

| Claim met first | Overturning record | Why realistic | Resolution |
|---|---|---|---|
| Weekly Leaderboard reset Ready on f_a325dd4af80afc5994d5dc, DES-320 Done, Vincent saw it (cmt_f76672cf21387ec1eeab) | Arthur's inline comment harmonygames-Games/match3d#248#rc_18 and the schedule in the hunk | a reviewer approves with a caveat and the ticket closes on delivery alone | rule test 5: the day matters |
| June line on row 5 and DES-317 | Leonard's reply d2b16907dc8c10fe5052805751097b58 | founders drop copy changes under whatever thread they are in | the rule's latest-line sentence |
| LIVE and Ready on row 6; Vincent's cmt_f4960d3c073493b6bfc6 | 37c5701a1780374401d295e86884f276 with the reach sentence in f_dc45e0e5a8b8635c1b82b2 | a message works on a device set up by hand and never reaches a real new player | rule test 4 |
| Vincent's pass cmt_fd950c410ed25c447c02 and f_8eb8c04713ff6a6ef4a265 | Vincent's reply 4a5ee02518ff2fbeacaef2fc6d5a9ef9 with samuel.turner@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com> | a tester corrects himself where he happens to be talking | the later reply and the QA note |
| Row 7 with no child under DES-314 | DES-313 with page_liveops_calendar | a ticket filed before the batch, under the game's own name | the hub's 'under whatever name' |
| DES-344 reads as new work | harmonygames-Games/match3d#248 and samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com> | an ask from someone who has not read the schedule | the rule's covered clause |
| The rule doc: Hold tickets go back to Todo (f_dc45e0e5a8b8635c1b82b2) | Leonard's card note 68dae8c7d95e24b55b69bf80 | a process rule amended where the roadmap lives | the doc's own 'unless the roadmap says otherwise' |
| Robert's Jul 10 level 20 move, variant C's level 13 and Vincent's 'at the start of app' on iOS (D06KPMDV2JZ/1752162738.497679, C08R27X0EAH/1755084279.518809, C08R27X0EAH/1758291802.756889) | Robert's Sep 29 post 37c5701a1780374401d295e86884f276 and Arthur's reply 09aae609aa744fb23288c7dcbac9926c | an ask point that moved during testing, and a launch popup that Unity shows on its own | the latest post; the reply explains the iOS popup |
| The deck's six Ready (f_de7a1ae20201816a67750d) and Brian's post (394f73aa43aa303a755bc81b2cf43840) | The rule doc f_dc45e0e5a8b8635c1b82b2: neither status column decides | summaries repeat a sheet nobody has revisited | the rule |

## Constraints for the prompt brief

| Anchor | May be named (noun phrases only) | Record |
|---|---|---|
| A1 | Leonard's DM from yesterday; Leonard's DM | 6fd96f3c3977cee8345e685d31cbc177 |
| A2 | the Zombie Match PN sheet; the PN sheet | f_a325dd4af80afc5994d5dc |
| A3 | my Drive folder | d_caafeec2804b3a67ce46aa |

Never name in the prompt: the rule doc's tests or sentences, the QA note or the pass log, Robert's post, Leonard's reply under Martin's post, Vincent's DM reply, Arthur's inline comment, the freeze comment, the cancelled review, the off-parent tickets or Collect & Win, or any count.

## Fact sheet

| Key | Value | Kind | Home / must appear in |
|---|---|---|---|
| Arthur's rollover note | isn't tied to the rollover | status | harmonygames-Games/match3d#248#rc_18, samuel.turner@harmonygames.co/<[SOURCE_ORG_0001]-Games/match3d/pull/248/review/2963610417@github.com> |
| final line for the seven-day message | Your Squad Is Waiting | status | evt_f2c03e69f50acf62c9d1c3, evt_bbc253a99f21bfbaa87a7c |
| interim line for the seven-day message | Your Squad Needs You Back | status | d2b16907dc8c10fe5052805751097b58 |
| Lives recharged pass withdrawn | taking my tick off Full Ammo | status | 363d61ffd3daeb6972a01cdb92db9520 |
| teammate lives ask | when a teammate sends you lives | status | cmt_eabac5435f2b3a575aad |
| infinite lives ask | infinite lives are about to run out | status | cmt_e2e2926a2080ca53c4ea |
| permission ask for the beta build | leaving our own ask after level 20 | status | 37c5701a1780374401d295e86884f276 |
| what switches messages on | only schedules once our own ask has run | status | 09aae609aa744fb23288c7dcbac9926c |
| what counts as seen | Seen only counts on a store build | status | samuel.turner@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com>, vincent.parker@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com> |
| race pass withdrawn | 5-minute timers build | status | 4a5ee02518ff2fbeacaef2fc6d5a9ef9 |
| roadmap freeze | Held tickets sit in Backlog | status | 68dae8c7d95e24b55b69bf80, 68d1eb90bef538c7c5c5599d |
| day 14 already covered | day 14 is already covered | status | samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com> |
| Boss Arena ask | once the daily Boss Arena attempts refill | status | cmt_f1b8a109dfa70cdc4565 |
| daily gift ask | the evening before the daily gift streak resets | status | cmt_2b519285937e7fa79453 |
| comeback gift scope | version 2 idea | status | cmt_13477aa8d1468ae11c9d |
| race timing | Daily is fine for this one | status | cmt_9338bb2c286a6c207792 |
| reach test | the settings toggle doesn't count | status | f_dc45e0e5a8b8635c1b82b2 |
| emoji rule | Emoji don't count as a different line | status | f_dc45e0e5a8b8635c1b82b2 |
| stale deck count | 6 Ready on the PN sheet | status | f_de7a1ae20201816a67750d |

```
FACT CHECK: PASS — 130 text-bearing rows, 19 declared facts, 9 declared superseded records
Errors: none
Warnings (1):
  line 130: linear.linear_issues DES-325: [inactive_person_named] names Nathan Price, inactive at the record's time: 2025-09-23 is after Nathan Price's departure signal (last authored activity 2024-07-19, status quiet_since_2024-07; activity.json)
```

Warning disposition: DES-325's title and description name the base feature Nathan's Treasure Hunt (row 8 of the sheet), not the person; no person named Nathan acts in any seeded record.

Solver totals (`solver/truth.json`): 43 keys looked at; 36 on the plan (Go 2, Hold 28, Drop 6); 7 off the plan.

## Facts for the human

| Locator | Base/seeded | Fact | Reach | Role |
|---|---|---|---|---|
| 6fd96f3c3977cee8345e685d31cbc177 | seeded | Leonard to Samuel, 2025-09-30T20:40:51Z: the ask, the seven columns, the writes and the counts back | DM member | anchor |
| f_dc45e0e5a8b8635c1b82b2 | seeded | Leonard, 2025-09-26T17:10:54Z: 'Beta message rule', six ordered tests and the Go, Drop and Hold definitions | shared | authority H1 |
| samuel.turner@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com> | seeded | Vincent to Samuel, Oliver, Owen, 2025-09-15T13:05:48Z: seen only counts on a store build; names the pass log | mailbox | authority H2 |
| f_8eb8c04713ff6a6ef4a265 | seeded | Vincent's Phone message checks: six built messages, the build of each pass; every row gives both builds; last changed 2025-09-24T15:00Z | shared | claim met first (T4) |
| 68dae8c7d95e24b55b69bf80 | seeded | Leonard, in the description of 68d1eb90bef538c7c5c5599d, 2025-09-29T20:15:03Z: held tickets sit in Backlog, unassigned | unscoped | authority H3, overturning (T8) |
| 68dc20c6d5fbf6ab70025295 | seeded | Leonard renames the BETA list, 2025-09-30T18:26:14Z: BETA: Sep 30 to BETA: Oct 10 | unscoped | settles SC-13 |
| 37c5701a1780374401d295e86884f276 | seeded | Robert in #zombie-match3d, 2025-09-29T17:40:08Z: our own ask stays after level 20; the Unity popup at launch on iOS stays as it is | channel member | overturning (T9), evidence (T3) |
| 09aae609aa744fb23288c7dcbac9926c | seeded | Arthur, reply under it, 2025-09-29T18:21:36Z: the popup switches nothing on; NotificationManager only schedules once our own ask has run or the player switches it on from settings, on both platforms | channel member | evidence (T3) |
| d2b16907dc8c10fe5052805751097b58 | seeded | Leonard under C08R8CHB0QL/1759159849.386619, 2025-09-29T18:05:29Z: an interim seven-day line | channel member | convincing answer (T2) |
| evt_f2c03e69f50acf62c9d1c3 | seeded | Leonard's note on the copy check, 2025-09-30T17:02:41Z: the final seven-day line | attendee | overturning (T2) |
| 4a5ee02518ff2fbeacaef2fc6d5a9ef9 | seeded | Vincent under D06UFE81RF0/1759163970.141449, 2025-09-29T19:40:46Z: the race iPhone was on the timers build; on 0.3.40 it never showed up | DM member | overturning (T4) |
| 363d61ffd3daeb6972a01cdb92db9520 | seeded | Vincent in #zombie-match3d, 2025-09-30T15:12:26Z: Full Ammo did not show on 0.3.49, he takes his tick off it | channel member | overturning (T16) |
| cmt_eabac5435f2b3a575aad | seeded | Douglas on ZOM-563, 2025-09-30T18:22:14Z: a message when a teammate sends lives, needs the server | unscoped | cohort member outside the filter (T6) |
| cmt_e2e2926a2080ca53c4ea | seeded | Calvin on ZOM-483, 2025-09-26T16:41:28Z: a reminder before infinite lives run out, local timer | unscoped | cohort member outside the filter (T6) |
| harmonygames-Games/match3d#248#rc_18 | seeded | Arthur on harmonygames-Games/match3d#248, 2025-06-26T20:58:14Z: counts seven days from the last leave, not tied to the rollover | unscoped | overturning (T1) |
| samuel.turner@harmonygames.co/1836006988541924555 | seeded row in a base thread | GitHub mail of that comment, 2025-06-26T20:58Z, Message-ID review/2963610417 | mailbox | companion |
| evt_b56d5b19baa0a573da4553 | seeded | Cancelled 'Lapsed ladder review', Leonard and Samuel, updated 2025-09-25T15:00:33Z | own calendar | evidence (T7) |
| samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com> | seeded | Cancellation mail with Leonard's note: day 14 is already covered | mailbox | evidence (T7) |
| f_de7a1ae20201816a67750d | seeded | Leonard's Beta readiness deck, 2025-09-19T18:30:26Z: six Ready | shared | decoy (T10) |
| 394f73aa43aa303a755bc81b2cf43840 | seeded | Brian, 2025-09-26T18:02:19Z: send all the Ready ones | channel member | decoy (T12) |
| DES-314 | seeded | Leonard's parent ticket, 32 children | unscoped | evidence (K4) |
| DES-313 | seeded | Calvin's ticket, Sep 17, no parent, says Collect & Win | unscoped | evidence (T5) |
| cmt_f1b8a109dfa70cdc4565 | seeded | Brian on ZOM-542, 2025-09-26T13:27:41Z: the Boss Arena reminder ask | unscoped | evidence (T6) |
| cmt_2b519285937e7fa79453 | seeded | Julia on ZOM-556, 2025-09-26T14:08:12Z: the daily gift reminder ask | unscoped | evidence (T6) |
| f_a325dd4af80afc5994d5dc | base | PNs Beta tab: 14 rows, six Ready, last changed 2025-06-23T07:02:43Z | shared | evidence (K3) |
| harmonygames-Games/match3d#248 | base | the client schedule: lives, first-mission, one day, the weekly batch of four, the weekly leaderboard batch, the daily race | unscoped | evidence (T1, T7) |
| page_liveops_calendar | base | Collect & Win is Win & Collect under another name; Plague Race, Zombie Lane and Endless live; Axe Arena, Streak Fever and Nathan's Treasure Hunt are Domino Delights | unscoped | evidence (T5) |
| D06KPMDV2JZ/1752162738.497679 | base | Robert, Jul 10: move the ask to level 20 | DM member | claim met first (T9) |
| C08R27X0EAH/1755084279.518809 | base | variant C asks at level 13 | channel member | claim met first (T9) |
| C05KNDCHAAG/1758558164.541689 | base | Axe Arena postponed, Sep 22 | channel member | evidence |
| C0880U9751A/1758643365.607149 | base | Arthur, Sep 23: required versions Android 0.3.127, iOS 0.3.40 | channel member | evidence |
| wh_USER_COHORT_RETENTION (ANALYTICS.GAME_EVENTS.USER_COHORT_RETENTION, snowflake.json /tables/10) | base | zombie_match_3d, week 2025-09-15: iOS D1 31.65, D7 9.28; Android D1 37.86, D7 10.68 | unscoped | evidence (K17) |

## Platform follow-ups

- ○ carrier: none load-bearing. The cancelled event evt_b56d5b19baa0a573da4553 has no description, as on every base event; samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com> and the source carry the fact.
- Relations on DES-330 and DES-338 must be seen rendering in linear_list_issues in the pre-check (B1 depends on it).
- `linear_show_data` and the list query's scope are unverified: confirm in the pre-check that neither returns comments in bulk.
- Forecast blind spot: in exact mode the forecast never fails write-content slots, so its E[avg] overstates the pass rate; the design-mode view is reported beside it under Preflight.
- Pre-check: confirm counted calls exceed 130 per run and that no run shows `model_refusal_fallback`.
- No independent red team ran (REDTEAM_* unset; fallback recorded in the scenario design §13; blind fork and coherence sweeps recorded below).

## Self-review

### Tool outputs (final SQL, verbatim)

```
schemas touched (10): gcal, gdocs, gdrive, github, gmail, gsheets, gslides, linear, slack, trello
rows by schema: {'gdrive': 3, 'gdocs': 1, 'gsheets': 2, 'gslides': 4, 'slack': 9, 'trello': 8, 'gmail': 11, 'gcal': 4, 'github': 2, 'linear': 110}  total rows: 154  ops: {'insert': 143, 'update': 11}
errors: 0  warnings: 0
```

```
BASE CHECK (/injection A + C, static): PASS  — 143 inserts, 11 updates
KB: bound (2025-10-01) — KB bound to the selected universe
Check A — records, references, IDs: PASS
Check C — dates and relationships: PASS
  note: gsheets.sheets_sheets: no base-reference rules (checked by sql_lint only)
  note: gslides.slides_page_elements: no base-reference rules (checked by sql_lint only)
  note: gslides.slides_pages: no base-reference rules (checked by sql_lint only)
  note: linear.linear_team_memberships: no base-reference rules (checked by sql_lint only)
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
  [ok] persona_reach: 31 load-bearing seeded ids for samuel_turner (17 in unscoped services = visible, 14 judged by persona_view check-sql); not provably visible: none
  [ok] fact_consistency: fact_check: 0 error(s) (19 declared facts), 1 drift warning(s); first: none — run tools/fact_check.py --manifest --no-leak
  [ok] hazard_scope: 0 pre-existing hazard(s) among task-touched records; state/lifecycle or referential without a verified resolution: none
  [ok] services_injected: 10 schemas injected (gcal, gdocs, gdrive, github, gmail, gsheets, gslides, linear, slack, trello); need ≥ 10
  [ok] rows: 143 INSERTed rows (UPDATE companions not counted; 154 rows in all); need ≥ 120
  [ok] services_carrying_weight: 12 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: schemas injected but absent from the design: none
  [ok] seeded_ids_exist_in_sql: 61 seeded ids cited; missing from SQL: none
  [ok] anchors: 3 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 21 fragments; need ≥ 12
  [ok] ask_fragment_services: 11 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 21 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 9 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 43; need ≥ 40 (source-defined: True)
  [ok] evidence_surfaces: 4 surfaces over 4 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 77; need ≥ 75
  [ok] call_budget: unconditional (verified) floor 202 of 202 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 200 (requester-confirmed volume_exception)
  [ok] call_budget_spread: 12 services in budget; largest share outside the per-record phase 19% (≤ 50%)
  [ok] traps: 16 traps across 7 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 6 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 5 supersessions (4 with versions in ≥ 2 services, 4 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: 5 trap(s) with version_records; the records' own timestamps (SQL created_at/ts/date/updated_at, or the base record) must be strictly increasing in the listed order (oldest first); bad: none
  [ok] distractors: 6 distractors of 6 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 10 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 9 chains with 8 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] mechanism_portfolio: 9 portfolio entries, each a mechanism-enum id with trap/chain nodes, a requirement, a natural-reading fallback and a prior family with its reason
  [ok] artifact_fields: declared ['gradable_surface', 'solver']: paths relative, digests sha256
  [ok] hidden_authorities: 3 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 2 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 12 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 9 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 9 writes over 7 services; each must depend on findings
  [note] volume_exception: call-budget floor 200 and per-record floor 75 replace 500 and 300; every other extreme target applies — reason: 36 real messages; mail, channels and sheets are bulk-readable, so honest necessa; requester confirmation: task author in chat on 2026-11-04 set the horizon target at 'over 130 tool calls
```

hg.py lint: counts FAIL 0, CHECK 0, INFO 0; no CHECK line to disposition. sql_lint warnings: none.

### Preflight (S4b–S5e)

```
SOLVER CONTRACT: PASS · solver.py sha a1ac742c0f47 · sql 6d162cfd1032 · 9 rules
  [PASS] contract.interface: 9 rules, each with mechanism, requirement and natural_reading; optional: ['touched', 'deciding', 'DEGRADES']
  [PASS] contract.deterministic: two fresh solves (forward and reverse key order) give identical output (43 keys, sha 48a18dbd5aa9), and so do fresh processes with PYTHONHASHSEED 1 and 2
  [PASS] contract.regression: no previous revision supplied (first revision)
  [PASS] contract.rules_nodes: 9 rules vs 9 portfolio entries: one-to-one
  [PASS] contract.slots: 19 direct/aggregate slots read a solver value; 38 write-content/delivery slots are graded from the writes, not the solver
  [PASS] contract.controls: DONE: 1 control(s); done_over moves ['Lapsed 1 day']; CORR: 1 control(s); corr_over moves ['Lapsed 1 day']; DEP: 1 control(s); dep_over moves ['Lapsed 1 day']; QA: 1 control(s); qa_over moves ['Lapsed 7 days']; PULL: 1 control(s); pull_over moves ['Lapsed 1 day']; ALIAS: 1 control(s); alias_over moves ['Season Pass start']; FILT: 1 control(s); filt_over moves ['Plague Race red dot']; BUILT: 1 control(s); built_over moves ['Lapsed 30 days']; FOLLOW: 1 control(s); follow_over moves ['Axe Arena']; channel CH-DONE (scale): ch_miss moves 1 of 1 member(s); channel CH-CORR (scale): ch_miss moves 1 of 1 member(s); channel CH-DEP (scale): ch_miss moves 1 of 1 member(s); channel CH-QA (scale): ch_miss moves 1 of 1 member(s); channel CH-PULL (scale): ch_miss moves 1 of 1 member(s); channel CH-ALIAS (scale): ch_miss moves 1 of 1 member(s); channel CH-FILT (scale): ch_miss moves 4 of 4 member(s); channel CH-BUILT (scale): ch_miss moves 1 of 1 member(s); channel CH-FOLLOW (scale): ch_miss moves 3 of 3 member(s); channel CH-SLIP (scale): fails surface slots ['K2', 'K3', 'K5', 'K6', 'K9', 'K14', 'K15', 'X17', 'X20']
  [PASS] contract.golden: 21 golden values checked against their deciding records (12 sampled keys x 6 fields): 21 identifier values found, 0 short tokens found, 0 presence-type; 51 unverified e.g. ['Weekly Leaderboard reset/Message: no evidence ids', "Weekly Leaderboard reset/What's missing: no evidence ids"]
  [PASS] contract.digest: manifest solver Working_Files/solver/solver.py digest a1ac742c0f47 vs file a1ac742c0f47
```

```
MUTATION · rev1 · sql 6d162cfd1032 · deterministic design diagnostics from the solver; on the Season Pass backtests these are development fixtures, not validation
  key-locality: PASS on 43 of 43 configurations checked
  rule:DONE                          KILLED     flipped   5 flips direct slot(s) of weight >= 3: ['X1']
  rule:CORR                          KILLED     flipped   5 flips direct slot(s) of weight >= 3: ['X3']
  rule:DEP                           KILLED     flipped   5 flips direct slot(s) of weight >= 3: ['X5']
  rule:QA                            KILLED     flipped   5 flips direct slot(s) of weight >= 3: ['X7']
  rule:PULL                          KILLED     flipped   5 flips direct slot(s) of weight >= 3: ['K1']
  rule:ALIAS                         KILLED     flipped   5 flips direct slot(s) of weight >= 3: ['X9']
  rule:FILT                          KILLED     flipped  20 flips direct slot(s) of weight >= 3: ['X11', 'X12', 'X11b', 'X12b']
  rule:BUILT                         KILLED     flipped   5 flips direct slot(s) of weight >= 3: ['X15']
  rule:FOLLOW                        SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:done_over                  KILLED     flipped   4 flips direct slot(s) of weight >= 3: ['K2']
  degrade:corr_over                  WEAK       flipped   1 flips only aggregate or weight-1 slots: ['K10']
  degrade:dep_over                   KILLED     flipped   4 flips direct slot(s) of weight >= 3: ['K2']
  degrade:qa_over                    KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['X3', 'X16']
  degrade:pull_over                  KILLED     flipped   4 flips direct slot(s) of weight >= 3: ['K2']
  degrade:alias_over                 SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:filt_over                  SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:built_over                 SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:follow_over                SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:ch_miss                    KILLED     flipped  55 flips direct slot(s) of weight >= 3: ['X1', 'X3', 'X5', 'X7', 'K1', 'X
  shards (consecutive slices of 14 records, 4 batches): 11 mutants {'KILLED': 8, 'SURVIVED': 3}
  intervention:rule:DONE             load-bearing    
  intervention:rule:CORR             no-injected-records
  intervention:rule:DEP              load-bearing    
  intervention:rule:QA               load-bearing    
  intervention:rule:PULL             load-bearing    
  intervention:rule:ALIAS            load-bearing    
  intervention:rule:FILT             load-bearing    
  intervention:rule:BUILT            load-bearing    
  intervention:rule:FOLLOW           load-bearing    
  intervention:degrade:done_over     no-injected-records
  intervention:degrade:corr_over     no-injected-records
  intervention:degrade:dep_over      no-injected-records
  intervention:degrade:qa_over       no-injected-records
  intervention:degrade:pull_over     no-injected-records
  intervention:degrade:alias_over    no-injected-records
  intervention:degrade:filt_over     no-injected-records
  intervention:degrade:built_over    no-injected-records
  intervention:degrade:follow_over   no-injected-records
  intervention:degrade:ch_miss       no-injected-records
  geometry: U = 0.8370 (190/227) · L_max = UNSUPPORTED
    V3 cap 0.85: U PASS (needs > 0.15) · L_max UNSUPPORTED
  dispositions: 0/38 recorded; missing ['rule:DONE', 'rule:CORR', 'rule:DEP', 'rule:QA', 'rule:PULL', 'rule:ALIAS', 'rule:FILT', 'rule:BUILT'] ...
```

```
TRAP LIVENESS · ADVISORY · UNCALIBRATED · lexical warnings, not proof · on the Season Pass backtests these are development fixtures, not validation
  hub 6fd96f3c3977cee8345e685d31cbc177 · direct delegations 12 · rule placement: A15 nodes only: ['C8', 'T8'] (mechanism_portfolio); every other node SKIP
  T1   done_gap           -  [rule placement SKIP: not an A15 node]
  T2   superseding        -  [rule placement SKIP: not an A15 node]
  T3   cross_reference_ga breadcrumb  [rule placement SKIP: not an A15 node]
  T4   superseding        -  [rule placement SKIP: not an A15 node]
  T5   scope_alias        breadcrumb  [rule placement SKIP: not an A15 node]
  T6   exact_predicate    breadcrumb  [rule placement SKIP: not an A15 node]
  T7   completion_elsewhe -  [rule placement SKIP: not an A15 node]
  T8   superseding        -
  T9   superseding        -  [rule placement SKIP: not an A15 node]
  T10  distractor         -  [rule placement SKIP: not an A15 node]
  T11  distractor         breadcrumb  [rule placement SKIP: not an A15 node]
  T12  distractor         -  [rule placement SKIP: not an A15 node]
  T13  distractor         -  [rule placement SKIP: not an A15 node]
  T14  distractor         breadcrumb  [rule placement SKIP: not an A15 node]
  T16  superseding        -  [rule placement SKIP: not an A15 node]
  T15  distractor         breadcrumb  [rule placement SKIP: not an A15 node]
  dispositions: 0/6 recorded
```

```
hardness_forecast: DISCLOSED OVERRIDE: --max-k 9 above the default 8 (--allow-max-k 9): exact enumeration of up to 2^9 configurations per record, not the plan's default (§5)
HARDNESS FORECAST · UNCALIBRATED · advisory · model claude-opus-5-5 · rev1 · model outputs, not measurements; the Season Pass backtests are development fixtures, not validation
  rule:DONE                                    family done_gap                                 Beta(2.0, 3.0) mean 0.40 n_eff 3.0 records 4
  rule:CORR                                    family superseding                              Beta(1.0, 4.0) mean 0.20 n_eff 3.0 records 9
  rule:DEP                                     family authority                                Beta(1.0, 4.0) mean 0.20 n_eff 3.0 records 3
  rule:QA                                      family superseding                              Beta(1.0, 4.0) mean 0.20 n_eff 3.0 records 9
  rule:PULL                                    family superseding                              Beta(1.0, 4.0) mean 0.20 n_eff 3.0 records 9
  rule:ALIAS                                   family scope_alias                              Beta(1.0, 3.0) mean 0.25 n_eff 2.0 records 2
  rule:FILT                                    family exact_predicate                          Beta(2.0, 3.0) mean 0.40 n_eff 3.0 records 3
  rule:BUILT                                   family completion_elsewhere                     Beta(1.0, 3.0) mean 0.25 n_eff 2.0 records 2
  rule:FOLLOW                                  family superseding                              Beta(1.0, 4.0) mean 0.20 n_eff 3.0 records 9
  independent whole    V3 E[avg] 0.851 [0.824, 0.880] P(all) 0.000
  independent shard:32 V3 E[avg] 0.851 [0.824, 0.879] P(all) 0.000
  independent shard:14 V3 E[avg] 0.851 [0.823, 0.879] P(all) 0.000
  independent slip     V3 E[avg] 0.865 [0.841, 0.889] P(all) 0.000
  independent batches  V3 E[avg] 0.851 [0.824, 0.880] P(all) 0.000
  source      whole    V3 E[avg] 0.851 [0.824, 0.880] P(all) 0.000
  source      shard:32 V3 E[avg] 0.851 [0.824, 0.879] P(all) 0.000
  source      shard:14 V3 E[avg] 0.851 [0.823, 0.879] P(all) 0.000
  source      slip     V3 E[avg] 0.865 [0.841, 0.889] P(all) 0.000
  source      batches  V3 E[avg] 0.851 [0.824, 0.880] P(all) 0.000
  correlated  whole    V3 E[avg] 0.851 [0.816, 0.886] P(all) 0.004
  correlated  shard:32 V3 E[avg] 0.851 [0.814, 0.886] P(all) 0.004
  correlated  shard:14 V3 E[avg] 0.851 [0.815, 0.887] P(all) 0.004
  correlated  slip     V3 E[avg] 0.865 [0.835, 0.893] P(all) 0.001
  correlated  batches  V3 E[avg] 0.852 [0.816, 0.888] P(all) 0.003
  V3: P(all four difficulty gates) 0.000-0.004 across scenarios; value of information (first scenario): ['rule:DONE', 'rule:CORR', 'rule:DEP']
  channel CH-DONE (scale, member latent [declared (unit-free point)], 1 member(s)): e = 0.1 [OVERRIDE (disclosed, no ledger record): --channel-rate CH-DO] · P(any of 1 fails) 0.100 integrated vs 0.100 plug-in · expected loss alone 0.0023 · UNCALIBRATED · OVERRIDE
  channel CH-CORR (scale, member latent [declared (unit-free point)], 1 member(s)): e = 0.6 [OVERRIDE (disclosed, no ledger record): --channel-rate CH-CO] · P(any of 1 fails) 0.600 integrated vs 0.600 plug-in · expected loss alone 0.0130 · UNCALIBRATED · OVERRIDE
  channel CH-DEP (scale, member latent [declared (unit-free point)], 1 member(s)): e = 0.05 [OVERRIDE (disclosed, no ledger record): --channel-rate CH-DE] · P(any of 1 fails) 0.050 integrated vs 0.050 plug-in · expected loss alone 0.0013 · UNCALIBRATED · OVERRIDE
  channel CH-QA (scale, member latent [declared (unit-free point)], 1 member(s)): e = 0.65 [OVERRIDE (disclosed, no ledger record): --channel-rate CH-QA] · P(any of 1 fails) 0.650 integrated vs 0.650 plug-in · expected loss alone 0.0142 · UNCALIBRATED · OVERRIDE
  channel CH-PULL (scale, member latent [declared (unit-free point)], 1 member(s)): e = 0.6 [OVERRIDE (disclosed, no ledger record): --channel-rate CH-PU] · P(any of 1 fails) 0.600 integrated vs 0.600 plug-in · expected loss alone 0.0130 · UNCALIBRATED · OVERRIDE
  channel CH-ALIAS (scale, member latent [declared (unit-free point)], 1 member(s)): e = 0.1 [OVERRIDE (disclosed, no ledger record): --channel-rate CH-AL] · P(any of 1 fails) 0.100 integrated vs 0.100 plug-in · expected loss alone 0.0023 · UNCALIBRATED · OVERRIDE
  channel CH-FILT (scale, member latent [declared (unit-free point)], 4 member(s)): e = 0.45 [OVERRIDE (disclosed, no ledger record): --channel-rate CH-FI] · P(any of 4 fails) 0.908 integrated vs 0.908 plug-in · expected loss alone 0.0395 · UNCALIBRATED · OVERRIDE
  channel CH-BUILT (scale, member latent [declared (unit-free point)], 1 member(s)): e = 0.05 [OVERRIDE (disclosed, no ledger record): --channel-rate CH-BU] · P(any of 1 fails) 0.050 integrated vs 0.050 plug-in · expected loss alone 0.0013 · UNCALIBRATED · OVERRIDE
  channel CH-FOLLOW (scale, member latent [declared (unit-free point)], 3 member(s)): e = 0.25 [OVERRIDE (disclosed, no ledger record): --channel-rate CH-FO] · P(any of 3 fails) 0.578 integrated vs 0.578 plug-in · expected loss alone 0.0000 · UNCALIBRATED · OVERRIDE
  channel CH-SLIP (scale, member latent [declared (unit-free point)], 0 member(s), slots ['K2', 'K3', 'K5', 'K6', 'K9', 'K14', 'K15', 'X17', 'X20']): e = 0.02 [OVERRIDE (disclosed, no ledger record): --channel-rate CH-SL] · P(any of 0 fails) 0.000 integrated vs 0.000 plug-in · expected loss alone 0.0024 · UNCALIBRATED · OVERRIDE
  channel control:DONE (control, member latent [rate unit], 1 member(s), member trials): e ~ Beta(1.0, 3.0) [ledger records, member trials (runs of a task share a design] · P(any of 1 fails) 0.250 integrated vs 0.250 plug-in · expected loss alone 0.0045 · UNCALIBRATED
  channel control:CORR (control, member latent [rate unit], 1 member(s), member trials): e ~ Beta(1.0, 7.0) [ledger records, member trials (runs of a task share a design] · P(any of 1 fails) 0.125 integrated vs 0.125 plug-in · expected loss alone 0.0006 · UNCALIBRATED
  channel control:DEP (control, member latent [rate unit], 1 member(s), member trials): e ~ Beta(1.0, 3.0) [ledger records, member trials (runs of a task share a design] · P(any of 1 fails) 0.250 integrated vs 0.250 plug-in · expected loss alone 0.0045 · UNCALIBRATED
  channel control:QA (control, member latent [rate unit], 1 member(s), member trials): e ~ Beta(1.0, 7.0) [ledger records, member trials (runs of a task share a design] · P(any of 1 fails) 0.125 integrated vs 0.125 plug-in · expected loss alone 0.0059 · UNCALIBRATED
  channel control:PULL (control, member latent [rate unit], 1 member(s), member trials): e ~ Beta(1.0, 7.0) [ledger records, member trials (runs of a task share a design] · P(any of 1 fails) 0.125 integrated vs 0.125 plug-in · expected loss alone 0.0024 · UNCALIBRATED
  channel control:BUILT (control, member latent [rate unit], 1 member(s), member trials): e ~ Beta(1.0, 3.0) [ledger records, member trials (runs of a task share a design] · P(any of 1 fails) 0.250 integrated vs 0.250 plug-in · expected loss alone 0.0000 · UNCALIBRATED
  channel control:FOLLOW (control, member latent [rate unit], 1 member(s), member trials): e ~ Beta(1.0, 7.0) [ledger records, member trials (runs of a task share a design] · P(any of 1 fails) 0.125 integrated vs 0.125 plug-in · expected loss alone 0.0000 · UNCALIBRATED
  channel control:ALIAS (control): UNPARAMETERIZED - no ledger record and no --channel-rate override: not simulated
  channel control:FILT (control): UNPARAMETERIZED - no ledger record and no --channel-rate override: not simulated
  slots most at risk (independent whole; P(fail) / P(fails all six) - all-fail justification workload, never a block): X3 0.72/0.15, X7 0.72/0.14, K1 0.68/0.11, X11b 0.67/0.13, X12b 0.67/0.12, X11 0.67/0.12, X12 0.66/0.11, K10 0.57/0.09
  ledger: forecast record {'id': 'hev_818f9ceec70850f5', 'added': True, 'present': False, 'rejected': none}
wrote Task_Authoring/task_inputsK/Working_Files/01c_Forecast.json
```

Forecast, read with care (UNCALIBRATED): this exact view cannot fail write-content slots, which hold 115 of the 183 weight, so its E[avg] of about 0.82 and its low P(all) are the optimistic end. The design view in `plan/forecast_output.txt`, which models the declared mechanisms over every slot, gives E[avg] 0.67 and P(all) 0.28 to 0.66. Only the pre-check can say which is closer. Rates are disclosed overrides sourced from stored runs.

Geometry: U passes the V3 cap; L_max is just under the margin and is advisory: the composed view counts direct slots only, while most of the task's weight is in write-content slots, which the design view models.

### Changes made at this stage (and why)

- record ids (all elements): Slack channel/ts pointers to seeded messages became the messages' 32-hex row ids; Vincent's QA note is cited by its message row with the thread kept alongside. the gate reads text and timestamps from SQL rows: a Slack row is keyed by its id, and a Gmail thread row holds only a snippet.
- per-ticket note times: Arthur's pass runs from Sep 25 20:30Z, after the last ask of that day; 24 tickets carry his note in his own words, and the two filed after it do not. ticket numbers rise with filing time, so a ticket filed after Lapsed 14 days cannot have been in a pass that missed Lapsed 14 days.
- K3 delegation: delegated_by_record and delegation_quote now cite Leonard's DM ('every row on the PNs Beta tab'), not the sheet. the sheet does not name itself: the words that delegate it are in the hub, and the gate reads them from the delegating record.
- T2 version_records[0]: base_pointer f_a325dd4af80afc5994d5dc -> gdrive:data.json /drive_files/42750. same record, in the pointer form the gate can read a timestamp from.
- rev2 record wording: Arthur's reply now says messages are scheduled once our own ask has run or the player switches them on from settings; Brian is added to the Beta readiness deck's shares. the /injection review of rev1 failed the unqualified 'only': harmonygames-Games/match3d#263#rc_4 shows the settings toggle calling EnableNotifications with no ask, and Vincent's comment on DES-318 shows a message arriving that way. Brian's post cites the deck he could not open.
- rev4 record wording: the rule doc's string ticket sentence ends 'so open one when you make the call'. an independent read of the prompt found a write-versus-no-write fork: the doc said a line needs a string ticket without saying who files it, and the prompt waives any check-in.
- rev5 record wording: Leonard's DM: the note no longer asks who hears from us once they stop playing; it asks for D1 and D7 with iOS and Android separately, the lapsed reminders the client schedules day by day, and anything the client already schedules that's still a Hold and why. Slot X20 follows it. Leonard's comment on the Rewarded ad ready ticket now says no bonus ad is live today. /prompt failed rev4 on Unique Ground Truth and Cross-Service Coherence (run_forensics/rev4/prompt_report_FAIL.md): Snowflake PUSH_NOTIFICATION_STATS shows weekly Firebase pushes to lapsed players against records saying every message is local, and Snowflake cannot be injected, so the question was removed. Per-platform and settings opt-in forks went with it. A blind sweep (plan/sweep_fork_rev5.md F1) then showed the warehouse's rewarded_video rows touch the rule's live prong, which Leonard's line left to inference; those rows use the rewarded_continue placement, with no bonus placement. No call, count or ticket state changes.
- rev6 hardness moves: Plague Race reads like every other pass and Vincent's reply drops the store build wording; Vincent's channel post takes his pass off Lives recharged (Go 2); Leonard's calendar note replaces his Sep 29 line; the Hold rule moves from a card comment to the card's description; two more comment asks sit outside the parent, one from Douglas; one Trello action renames the list to BETA: Oct 10; the Rewarded ad ready ask is removed. /hardness scored rev5 2 (run_forensics/rev5/hardness_report_FAIL_2.md): 188 calls, about 90% right, one independent cause. /prompt scored Coherence 3 on SC-13. Moves chosen from the run's own call ledger (01a_Hardening_Report.md §5, §10) under the requester's delegation. The blind sweep of rev6 (plan/sweep_fork_rev6.md F1) found AD_IMPRESSION_EVENTS can answer the rule's live-today test for the rewarded ask, the rev4 failure pattern, and Snowflake cannot be injected, so the ask goes; F2 moved Douglas's comment after his Sep 30 prod update, F3 and F4 fixed two timelines.
- rev3 record wording: Leonard's comment on the Rewarded ad ready ticket; Julia's ask says the gift streak is live and is separate from Calvin's chest ping; the rule's in-the-beta test names Zombie Match; the hub says one email per person, apart from Leonard. a blind fork sweep on rev2 (plan/sweep_fork_rev2.md) showed these four could each move Hold or Drop by one or leave the email count open, and /prompt fails on a classification fork no record settles.
- mechanism_portfolio.ALIAS.controls: added Season Pass start as a control member. the draft's over_application already acts on this member; contract.controls needs the operator to move a declared control.
- mechanism_portfolio.FILT.controls: added Plague Race red dot as a control member. the draft's over_application already acts on this member; contract.controls needs the operator to move a declared control.
- Scenario amendment, re-certified: Vincent's pass log joins T4 as its first gsheets version and the tenth injected schema, because it carries the build behind each pass, which test 6 needs; the count slots T1 and T3 moved to write_content because they read the DM, and oracle_kit cannot read a text selector as a solver value; Arthur's GitHub mail joins the base PR thread.
- Blind fork sweep (plan/sweep_fork.md, fresh agent, no design files): 3 High, 8 Medium, 12 Low. Fixed: partial reach (rule test 4 now fails only if none count), a moved phone date (QA note says it is fine), Lives recharged's Rollover cell (Leonard's comment on DES-315), string ticket home, which rows carry a headline, what Audience means, Leonard's own asks (hub says everyone else), two feature overlaps (DES-338 says what it is not; the Trophy Path ask became Achievement reward waiting because the base treats Trophy Path as Zombie Lane). Left as designed: the empty 'or a card' branch of the scope sentence, and the note's lapsed ladder reading.
- Answer-key patterns the sweep flagged: Arthur's 24 notes are now in his own words per ticket with uneven gaps, and the fixed 'X is live.' sentence is gone; only two descriptions keep a plain state line, where no base record shows it.
- Blind coherence sweep (plan/sweep_coherence.md, fresh agent): 2 BLOCKER, 8 MAJOR, 12 MINOR. B1: Robert's post no longer says nothing asks before level 20, because base records show the iOS launch prompt; Arthur's new reply says only our own ask switches messages on, and test 4 says 'our own permission ask'. B2: Leonard reopens the push notifications card before commenting (updateCard action, dueComplete false). M1 action list name set to BETA: Sep 30. M2 the freeze is narrowed so ZOM-566 does not break it. M3 the two off-parent asks move after Arthur's pass. M4 hub wording on tickets and money. M6 DES-341 no longer assumes a last level. M7 Zombie Lane ask reworded and a timer fits. M8 the hunk now comes from rc_16 and rev_7 carries the comment.
- Minor sweep items applied: three more team_DES memberships, ask times inside each author's hours, real seconds on every seeded time, no description on the calendar rows, GitHub mail label and headers as on the base mails, Boss Arena asks on the weekly board, the gift ask after the bug fix, the rule in Leonard's first person, Brian's post now names the deck. Left as designed: corrections placed under unrelated threads (the mechanism), Vincent's first mail to Samuel (authority home), and line 1 of the SQL (required by the platform).
- Rev2, after the local /injection review of rev1 (FAIL, plan/0_injection_report.md): Arthur's reply no longer says 'only' without the settings toggle, because harmonygames-Games/match3d#263#rc_4 calls EnableNotifications from the toggle with no ask; Brian joins the deck's shares because his post cites it. No call or graded value changes.
- Rev3, after a blind fork sweep of rev2 (plan/sweep_fork_rev2.md: Go 3 firm; 1 High, 6 Medium, 16 Low): Leonard's comment on DES-346 settles test 1 against the warehouse's rewarded_video rows; Julia's ask says the streak is live and separate from DES-338; the rule's test names Zombie Match; the hub asks for one email per person. No call or graded value changes. Left to acceptance in brief §4b: the string ticket's state, the note's reading of who hears, and a caveat about the push stats table.
- Surface repair at prompt check, SQL unchanged: a synthetic correct run scored 0.69 because text slots read content only and the ticket key sits in an id parameter, and slack_channel_post takes a literal. Twelve slots now match distinctive wording or a run of state moves, so a correct run scores 0.9945 and a natural-reading run 0.29. X1c, X6c and X8c are local proxies: each Done Hold left behind shortens the run of moves; the rubric must name the ticket. D1 stays strict, because register_parent also needs a share call nothing asks for.
- Rev4, after an independent read of the prompt (plan/prompt_read_independent.md): the rule doc says who files the string ticket. No call or graded value changes.

### /injection Checks A–C walk

- Inventory: 143 INSERT, 11 UPDATE, 0 DELETE, no upserts; tables {'gdrive.drive_files': 3, 'gdocs.docs_documents': 1, 'gsheets.sheets_spreadsheets': 1, 'gsheets.sheets_sheets': 1, 'gslides.slides_presentations': 1, 'gslides.slides_pages': 1, 'gslides.slides_page_elements': 2, 'slack.slack_messages': 9, 'trello.trello_actions': 4, 'trello.trello_cards': 3, 'trello.trello_boards': 1, 'gmail.gmail_threads': 5, 'gmail.gmail_messages': 6, 'gcal.gcal_events': 4, 'github.github_review_comments': 1, 'github.github_reviews': 1, 'linear.linear_team_memberships': 4, 'linear.linear_issues': 37, 'linear.linear_comments': 68, 'linear.linear_teams': 1}.
- Check A (references and IDs): PASS: every channel, user, issue, thread, calendar, board, list and folder resolves (base_check Check A); uniqueness over the full collections (1.F); ownership, membership and shares give Samuel reach (check-sql PASS).
- Check B (structure): PASS: sql_lint 0 errors; every *_json column is literal JSON; NOT NULL columns supplied; generated *_fts columns never written; camelCase Trello columns quoted.
- Check C (dates, parents, statuses, counts): PASS: every seeded timestamp is before 2025-10-01T00:00Z; replies after their parents; both roots' counters updated; Done tickets have completed_at after their last comment and DES-314 stays open; Trello badges follow the comments.

### Touched-data census

See 'Touched-data census and coherence hazards' above: six hazard categories covered and SC-7, 13, 14, 16, 19, 28, 36, 38, 57, 68, 70 dispositioned.

### Counter-readings

| Category | Counter-reading (strongest argument it FAILS) | Evidence that resolves it | Verdict |
|---|---|---|---|
| Temporal | Vincent reports a seven-day message arriving on Sep 24 when the required store versions were set on Sep 23 | f_8eb8c04713ff6a6ef4a265 notes the phone date moved forward on the lapsed and weekly rows; C0880U9751A/1758643365.607149 fixes the versions | holds |
| Temporal | the rule doc (Sep 26) refers to a QA note and a Robert decision that come later or earlier in confusing order | samuel.turner@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com> is Sep 15, before the doc; the doc says the ask is Robert's call and 37c5701a1780374401d295e86884f276 (Sep 29) is his latest post, which the doc does not quote | holds |
| Temporal | Arthur's comment harmonygames-Games/match3d#248#rc_18 predates the row it criticises being tracked | the comment is on the code in harmonygames-Games/match3d#248, Jun 26, before harmonygames-Games/match3d#248#rev_6 at 21:23:25Z; the sheet row existed from Jun 23 (f_a325dd4af80afc5994d5dc) | holds |
| Semantic / Category | Lapsed 7 days and the weekly reminder batch could be two messages, so 'covered' is unclear | the hunk in harmonygames-Games/match3d#248#rc_18 shows one weekly batch with the sheet's headline; row 5 carries the same line | holds |
| Semantic / Category | 'In Review' on 26 DES tickets misdescribes tickets nobody has reviewed | Leonard's parent DES-314 asks for a call on each; they are in review for that call, and the rule sends them back | holds |
| Cross-service Referential | Boss Arena is 'Infinite HP Boss Mode' on the board, so a ticket about Boss Arena may name another feature | ZOM-550 and ZOM-553 use Boss Arena for that mode; the card is on the BETA: Oct 10 list | holds |
| Cross-service Referential | d2b16907dc8c10fe5052805751097b58 sits in #zombie-art under a theme post, so it may not be a real decision | Leonard is the row's owner (D06L58XCVKK/1750138057.452159) and the rule doc names the latest line he has called | holds (designed, T2) |
| Quantitative | the deck's six could be read as six Go | f_de7a1ae20201816a67750d says six Ready on the sheet, and f_a325dd4af80afc5994d5dc has six Ready rows; the rule says neither status column decides | holds |
| Quantitative | C08R8CHB0QL/1759159849.386619's reply counters disagree with the export after the seeded reply | UPDATE sets reply_count 4, reply_users_count 4 and the new latest_reply (Q01) | holds |
| State / Lifecycle | six Done tickets contradict three of them being Holds | Done records that the code shipped and arrived on a device (DES-320, DES-319, DES-318); the rule's tests ask more, and SC-16 says a ticket state is no proof | holds (designed, T1, T3, T4) |
| State / Lifecycle | best argument the race disagreement is unintended: cmt_fd950c410ed25c447c02 and f_8eb8c04713ff6a6ef4a265 say passed while 4a5ee02518ff2fbeacaef2fc6d5a9ef9 says it never showed up | a dated human claim withdrawn by its own author five days later; the QA note states the standard | holds (designed, T4) |
| State / Lifecycle | best argument the freeze is unintended: the rule doc and 68dae8c7d95e24b55b69bf80 give two states for a Hold | the doc says 'unless the roadmap says otherwise' and the note is later, by the same author | holds (designed, T8) |
| State / Lifecycle | best argument the alias is unintended: DES-313 is a stray duplicate of a child that should exist | no child exists; the live-ops page page_liveops_calendar maps the names; the ticket predates the parent | holds (designed, T5) |
| State / Lifecycle | best argument the Lapsed 14 ask is unintended: DES-344 has no note and could be a Hold | samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com> and the batch settle it; the rule's Drop clause names covered messages | holds (designed, T7) |
| State / Lifecycle | best argument the first-mission Hold is unintended: cmt_f4960d3c073493b6bfc6 shows it arrives, so it reaches players | the rule's reach sentence says the settings toggle doesn't count, 37c5701a1780374401d295e86884f276 keeps our own ask after level 20, and 09aae609aa744fb23288c7dcbac9926c says only that ask or the toggle schedules anything | holds (designed, T3) |
| State / Lifecycle | best argument the weekly Hold is unintended: cmt_f76672cf21387ec1eeab shows it arrives on both | the rule's day test: the row says rollover and the code counts from the last leave | holds (designed, T1) |
| State / Lifecycle | best argument the headline change is unintended: DES-317 and d2b16907dc8c10fe5052805751097b58 disagree | the reply is later and by the row's owner; the rule takes the latest line he has called | holds (designed, T2) |
| State / Lifecycle | best argument the deck disagreement is unintended: f_de7a1ae20201816a67750d and the rule differ on what Ready means | the deck repeats a sheet flag; the rule says neither status column decides | holds (designed, T10) |
| State / Lifecycle | best argument the ask-point disagreement is unintended: C08R27X0EAH/1758291802.756889 says iOS asks at launch while 37c5701a1780374401d295e86884f276 says after level 20 | both are true of different things: Arthur's Sep 23 post in #executives (C07C2866011/1758659424.324079) calls the launch prompt Unity's, and 09aae609aa744fb23288c7dcbac9926c says only our own ask switches messages on | holds (designed, T9) |
| Identifier / Format | the GitHub mail id samuel.turner@harmonygames.co/<[SOURCE_ORG_0001]-Games/match3d/pull/248/review/2963610417@github.com> is invented | it follows the base pattern and sits numerically between the two neighbouring review mails in the thread | holds |
| People status | Victor Barnes or another leaver is named, or a seeded speaker had left | activity.json: all ten seeded speakers are active at the clock (1.C); no seeded record names Victor | holds |
| Other | the off-parent asks read as planted | cmt_f1b8a109dfa70cdc4565 and cmt_2b519285937e7fa79453 are one-line asks by a teammate on a ticket about the same feature, the way base work is discussed | holds |
| Cross-service Referential | Robert's post keeps the ask after level 20 while base records say iOS prompts at launch, so test 4 has two answers (sweep B1) | the post now names the launch popup and leaves it; C07C2866011/1758659424.324079 (Arthur) calls it Unity's; the seeded reply says only our own ask schedules anything | holds |
| State / Lifecycle | the push notifications card was marked complete on Jun 30 and takes a Sep 24 comment (sweep B2) | action 6862c0874151cf6318d91742 set it complete; the seeded updateCard reopens it before the comment, and the UPDATE sets dueComplete false | holds |
| Temporal | the off-parent asks quote Arthur before his pass (sweep M3) | both comments now follow his Sep 25 20:30Z pass (L-numbered rows in the ledger) | holds |
| Cross-service Referential | Arthur's reply says scheduling needs our own ask while Vincent's comment on DES-318 shows a message arriving from the settings toggle (rev1 /injection failure) | rev2 names both routes in the reply; harmonygames-Games/match3d#263#rc_4 is the toggle path, and the rule doc says the toggle doesn't count for reach | holds |
| State / Lifecycle | the warehouse shows Zombie Match rewarded_video impressions while DES-346 is a Drop for not being in the beta | Leonard moved the card himself on Sep 23 (action 68d1eb16ac8c64cf8165101d) and his comment says so; the claim is about the roadmap, not the client, so the telemetry doesn't contradict it | holds |

Unresolved: the reviewer of the scenario has not re-read the B5 fix; competency fit stays an open risk for /prompt (most writes are on Linear). Everything else above is closed.

```
STAGE GATE injection: PASS — Task_Authoring/task_inputsK · 01_Universe_Inject.sql#6d162cfd1032 · 01_Hardness_Manifest.json#09ddeab36568 · 01_Grounding_Dossier.md#4aa9b3c38219 · solver/solver.py#a1ac742c0f47 · 01c_Dispositions.json#1e6cb127a339 · 01c_Preflight_Report.json#d1bfc2687c65 · 00_Assigments.md#55f6d8057880 · 01_Scenario_Design.md#a477a8d3015e · 01_Hardness_Manifest.draft.json#ed860637b593 · 01_Gradable_Surface.json#095a6e4fc9df · __context__#72168f70a409 · __assignment__#3adec6ac02d7 · __policy__#dc4ab5df3cdd · __gate_policy__#115714063000 · __review__#95f1481dfb3c · blocking 0 · warnings 1 · checks 39
[PASS] assignment.v3_context: Samuel Turner / Game Designer; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 6 output(s) present: 01_Universe_Inject.sql, 01_Hardness_Manifest.json, 01_Grounding_Dossier.md, solver/solver.py, 01c_Dispositions.json, 01c_Preflight_Report.json
[PASS] structure.inputs: 4 input(s) present: 00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json)
[PASS] chain.scenario: upstream 'scenario' PASS pasted and current (01_Scenario_Design.md#a477a8d3015e, 01_Hardness_Manifest.draft.json#ed860637b593, 01_Gradable_Surface.json#095a6e4fc9df, 00_Assigments.md#55f6d8057880, __context__#72168f70a409, __assignment__#3adec6ac02d7, __policy__#dc4ab5df3cdd, __gate_policy__#115714063000, __review__#8ac0cdb4d008)
[PASS] structure.sections: 17 required sections present and non-empty (01_Grounding_Dossier.md)
[PASS] structure.placeholders: no placeholders in 01_Grounding_Dossier.md
[PASS] evidence.entity: 15/15 items carry a source pointer (min 90%)
[PASS] evidence.keyword: 21/21 items carry a source pointer (min 100%)
[PASS] evidence.persona_reach: 9/9 items carry a source pointer (min 100%)
[PASS] evidence.record_ledger: 154/154 items carry a source pointer (min 100%)
[PASS] evidence.facts_for_human: 32/32 items carry a source pointer (min 100%)
[PASS] tool.sql_lint: sql_lint re-run matches the paste: errors 0, warnings 0, rows 154
[PASS] tool.injection_lint: hg.py lint: 0 FAIL, 0 CHECK dispositioned, 0 INFO; sha256 6d162cfd1032 matches 01_Universe_Inject.sql
[PASS] tool.base_check: base_check pasted PASS; re-run PASS
[PASS] tool.base_claims: base_claims pasted PASS; re-run PASS
[PASS] tool.hardness_gate: hardness_gate (SQL) pasted PASS; re-run PASS
[PASS] structure.design_delta: final manifest keeps all 61 draft ids
[PASS] structure.preflight: 01c_Preflight_Report.json bound by sha256 to the current SQL, solver, surface, manifest and dispositions
[PASS] solver.contract: solver contract re-run PASS
[PASS] mutation.dispositions: 38 mutation and intervention results each carry a written disposition (01c_Dispositions.json)
[PASS] geometry.upper_bound: U 0.837 (190/227) vs 1 - cap 0.15 (V3 medium): PASS (bound PASS); re-run U 0.837 PASS (bound PASS)
[WARN] geometry.margin: L_max None vs (1 - cap) + 0.10: UNSUPPORTED (advisory: the margin is a judgment, not a proof)
[PASS] liveness.dispositions: every liveness flag dispositioned (6 flag(s))
[PASS] forecast.preregistered: forecast hev_818f9ceec70850f5 pre-registered in the ledger (UNCALIBRATED)
[PASS] tool.check_sql_pasted: persona_view check-sql --load-bearing output pasted with verdict PASS
[PASS] reach.injection: 22 scoped load-bearing ids YES for samuel_turner
[PASS] structure.facts_declared: manifest declares 19 load-bearing fact(s) in `facts`
[PASS] tool.fact_check: fact_check --no-leak pasted PASS; re-run PASS
[PASS] kb.coherence_hazards: coherence audit cites 13 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 11 seeded speakers each cited with activity.json status; conventions.json cited
[PASS] kb.integrations: companions listed per integrations.json (10 INT ids, services ['gcal', 'gdocs', 'gdrive', 'github', 'gmail', 'gsheets', 'gslides', 'linear', 'slack', 'trello'])
[PASS] boundary.anchor_naming: 6 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 27 evidenced counter-readings (of 28 found; need ≥ 16) in 01_Grounding_Dossier.md
[PASS] review.coverage: self-review addresses all 9 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

