# Grounding Dossier — frederick_dd_publishing · injection rev2 · contains no prompt, OE or criterion text

SQL: `task_inputs/01_Universe_Inject.sql` (stored byte for byte in `Working_Files/run_forensics/rev2/01_Universe_Inject.sql`; rev1 and its platform reviews stay in `run_forensics/rev1/`), built by `Working_Files/plan/build_sql.py` from the certified design (`01_Scenario_Design.md`, draft manifest, surface); final manifest by `plan/build_final_manifest.py`; solver `Working_Files/solver/solver.py` (truth `solver/truth.json`); this file by `plan/assemble_dossier.py`. Universe synth-cut, seed bound 2025-10-01T00:00:00Z (Tue Sep 30 17:00 PT), eval clock 2025-10-01T07:00:00Z; Frederick's today is Wed Oct 1, 2025. 144 INSERT + 32 UPDATE statements over 10 schemas. Every probability here is UNCALIBRATED.

## 1.A Structural

| Table | NOT NULL columns supplied (live schema) | Base location · sample ids | Format notes |
|---|---|---|---|
| gmail.gmail_threads / gmail_messages | id, user_email; id, thread_id, user_email, label_ids_json, internal_date, date | gmail/threads/frederick@harmonygames.co_1830012626042968381.json (thread_id frederick.stone@harmonygames.co/1830012626042968381) | mailbox-prefixed ids; Message-ID in the row id; CRLF bodies; to_json holds name and address strings |
| slack.slack_messages | id, ts, channel_id, type, text, reply_count, reply_users_count, is_activity_message, reactions_json, files_json, attachments_json, created_at, metadata_json | slack/messages/C07C2866011/2025-09.json (root 330b95fd38236b4e7192e24f272685b4) | id = sha256(channel|ts)[:32]; replies carry thread_parent_id and thread_ts_legacy; root counters updated |
| gdrive.drive_files / gdocs.docs_documents / gsheets / gslides | id, name, mime_type; document_id, title; spreadsheet_id, title; presentation_id, object_id | gdrive/data.json d_175c0d7bc72ed244b944cb (Frederick's root) | f_/d_ + 22 hex; style_runs_json covers the title line and headings |
| gcal.gcal_events | event_id, calendar_id | gcal/data.json (10,395 events checked, plan/id_checks_sql.out.json) | one row per attendee calendar held by staff, self:true on the owner's copy; evt_ + 22 hex; ical_uid 32 hex @hg4 |
| linear.linear_comments / linear_issues | comment id, issue_id, author_id, body, is_edited; issue updated_at | linear/data.json ENG-2362 (Todo, assignee Arthur) | lc_ + 24 hex; the base comments collection is empty (0 records), so the row follows Ask_Carriers §6b |
| trello.trello_cards / trello_actions / trello_boards | id, name, idBoard, idList; id, type, date | trello/data.json board 66da196af476ab78deaa0cef (UA/BD), list 670015c2ecd45b634d5eec81 (BD Follow Up) | 24 hex with the action time in the first 8; idShort 41–43 after base max 40; badges match comment counts |
| contacts.contacts | contact_id, first_name, last_name | contacts/contacts.json (170 contacts) | 24 hex ids; sparse like the base (job, email) |

## 1.B Entity

| Entity | Spelling used | Where it appears (cited) | Agreement |
|---|---|---|---|
| Frederick Stone | frederick.stone@harmonygames.co (roster; base files use the frederick@ alias, I03) | slack EMPLOYEE_0008_SLACK_ID in C07C2866011; mailbox frederick.stone@harmonygames.co/1844732284109533347; Drive root d_175c0d7bc72ed244b944cb | AGREE |
| Leonard Hayes | leonard.hayes@harmonygames.co | slack EMPLOYEE_0038_SLACK_ID (C07C2866011/1756140953.197759); hub sender frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com>; owner of f_5e355d03f6eb6a4e866ead | AGREE |
| Robert | robert@harmonygames.co | slack EMPLOYEE_0016_SLACK_ID (C07C2866011/1759176900.065118, C07C2866011/1758909900.662794) | AGREE |
| Arthur Blake | arthur.blake@harmonygames.co | linear usr_cc3e90160f490686 (ENG-2362, lc_674982ffdca63f854ec6f591); slack EMPLOYEE_0025_SLACK_ID (C07C2866011/1759251900.005166) | AGREE |
| ESG Law | partner PERSON_2694 (base engagement frederick.stone@harmonygames.co/1841636073974841484) | seeded note frederick.stone@harmonygames.co/<CA9raR_pqldShsvOhd5Uwxoj8zJh2-tzH0UJ5JLd@mail.gmail.com> | AGREE |
| Appodeal | Appodeal | base frederick.stone@harmonygames.co/1830012626042968381, frederick.stone@harmonygames.co/1829687508014442264 | AGREE |
| Rayking Game | Rayking Game | base frederick.stone@harmonygames.co/1842348778705877030, D05S58U4SAK/1757009185.631739; seeded DM D05S58U4SAK/1757090400.829462 | AGREE |
| Homa, NCsoft, Tilting Point | as in the base | C096HFA5Z8W/1758210489.170809, C07C2866011/1757516293.887729, frederick.stone@harmonygames.co/1842443183462721250 | AGREE (named out of scope by f_5e355d03f6eb6a4e866ead) |
| Oakline Games | Oakline Games · Marek Sobol | f_27cac0eed300cc33eeb4fd | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Tallwater Games | Tallwater Games · Paola Duarte | f_e8cb875d5b7c8d9972d259 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Sunfold Mobile | Sunfold Mobile · Lena Fischer | f_8ddfb9901891eb8e9dcab8 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Harbor Lane Games | Harbor Lane Games · Diego Reyes | f_d72e8b34e7496f0de668bc | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Wavecrest Play | Wavecrest Play · Sofia Lindqvist | f_a6a5647f977d4638b2b8b1 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Copperleaf Games | Copperleaf Games · Jonas Weber | 495d71a7e14dfaa68cac26fc4a6c4e03 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Redwood Arcade | Redwood Arcade · Mei Tanaka | lc_674982ffdca63f854ec6f591 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Moonrail Studios | Moonrail Studios · Anika Rao | f_464839da025a0a01f53979 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Northglow Publishing | Northglow Publishing · Callum Ross | f_3eccf6e0bb63955dc51e27 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Pinegrove Games | Pinegrove Games · Elena Petrova | f_5f3ef4a4760d18e696a41a | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Fernhollow Media | Fernhollow Media · Rhys Morgan | frederick.stone@harmonygames.co/1842077918822912178 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Quietbay Games | Quietbay Games · Nadia Haddad | frederick.stone@harmonygames.co/1842077918822894896 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Slatewood Mobile | Slatewood Mobile · Yuki Sato | frederick.stone@harmonygames.co/1842077918823167383 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Ironbridge Interactive | Ironbridge Interactive · Tessa Hale | frederick.stone@harmonygames.co/1842077918822812534 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Tidewell Studios | Tidewell Studios · Omar Khalil | frederick.stone@harmonygames.co/1842077918822727407 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Marlin Play | Marlin Play · Greta Holm | frederick.stone@harmonygames.co/1842077918823060205 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Kitebridge Games | Kitebridge Games · Ivo Novak | frederick.stone@harmonygames.co/1842077918823167536 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Orchard Lane Games | Orchard Lane Games | frederick.stone@harmonygames.co/1842077918822627795 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Summit Mobile | Summit Mobile | frederick.stone@harmonygames.co/1842077918822746195 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Silverlake Mobile | Silverlake Mobile | frederick.stone@harmonygames.co/1842077918822773098 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Cedarbrook Play | Cedarbrook Play | frederick.stone@harmonygames.co/1842077918822506013 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Foxglove Games | Foxglove Games | frederick.stone@harmonygames.co/1842077918822804025 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Riverstone Interactive | Riverstone Interactive | frederick.stone@harmonygames.co/1842077918823170401 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Bellwether Arcade | Bellwether Arcade | frederick.stone@harmonygames.co/1842077918822759281 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Kestrel Group | Kestrel | signature frederick.stone@harmonygames.co/1842077918822811962, contact 5373edb55ca853d6052ecce5, post C07C2866011/1759176900.065118 | AGREE (new entity; its first-word hits are newsletter noise, plan/name_census.log) |

Frederick's GitHub display name 'Ryan' (S04) is avoided: no GitHub record is touched. No roster person is renamed or re-titled.

## 1.C Voice and realism

Seeded speakers, each with its activity.json (synth-cut KB) status at the clock:
- Leonard Hayes (leonard.hayes@harmonygames.co, EMPLOYEE_0038_SLACK_ID) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds dated Sep 25–30 2025 (C096HFA5Z8W/1758915000.867092, frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com>, f_5e355d03f6eb6a4e866ead).
- Robert (robert@harmonygames.co, EMPLOYEE_0016_SLACK_ID) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds Sep 26 and Sep 29 2025 (C07C2866011/1758909900.662794, C07C2866011/1759176900.065118).
- Arthur Blake (arthur.blake@harmonygames.co, EMPLOYEE_0025_SLACK_ID) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds Sep 26 and Sep 30 2025 (C069FF9Q57S/1758912000.686342, lc_674982ffdca63f854ec6f591, C07C2866011/1759251900.005166).
- Frederick Stone (frederick.stone@harmonygames.co, EMPLOYEE_0008_SLACK_ID) — activity.json status_at_clock active_sep_2025_quiet_in_oct; his seeded outreach mail (May 6 to Sep 24), DM D05S58U4SAK/1757090400.829462 and card comments 68dbfe80ef9c41b4f4fa8fe9, 68dabd6800e271eb0608d2d6.
- External senders (each publisher's own address, plain names in the signature) and PERSON_2694_EMAIL (ESG partner, base) are not personas.

Lengths and hours from conventions.json (synth-cut KB): slack.length_chars_by_channel_type private p50 51 / p90 156 / p99 615; the seeded lines run 95–290 characters, below p99. slack.per_person_hours_and_style core UTC windows: Arthur 15–01, and Leonard's and Robert's windows cover 15–02 and 16–04: every seeded post falls inside its author's window (Leonard 16:20Z; Robert 18:05Z, 20:15Z; Arthur 17:05Z, 18:32Z, 18:40Z). gmail.internal_subject_len_chars p50 42: 'DD publishing: what I need for Monday' is 37. gcal.duration_min p50 30: the three publisher calls are 30 minutes.

Voice from real messages: Leonard's mail is full sentences signed 'Leonard'; Robert's Slack is short and blunt; Arthur states what he checked. Founders call Frederick 'Fred' in Slack and mail.

## 1.D Keyword

| Term | Hits / pointer | Note |
|---|---|---|
| "Appodeal" | base frederick.stone@harmonygames.co/1830012626042968381 | waiting on us |
| "Rayking" | base frederick.stone@harmonygames.co/1842348778705877030, D05S58U4SAK/1757009185.631739 | waiting on us; Frederick's Sep 4 message is an unsent draft |
| "ESG" | base frederick.stone@harmonygames.co/1841636073974841484 (engagement); seeded frederick.stone@harmonygames.co/1844620296192667598 | the licence date |
| "non-mobile" | base C07C2866011/1756140953.197759, f_26e1f9a86761e35049192a | the rights position |
| "D30 ARPI" | base D05S58U4SAK/1758736747.409459 | the $0.50 figure |
| "DD publishing" | NEW TERM — introduced in d_6fc54be60d1377e340a5b5, 68dab660c900179df4f5f92d, f_5e355d03f6eb6a4e866ead, frederick.stone@harmonygames.co/1844732284109533347 | reached from the hub frederick.stone@harmonygames.co/1844732284109533347 or its delegations |
| "ground rules" | NEW TERM — introduced in f_5e355d03f6eb6a4e866ead | reached from the hub frederick.stone@harmonygames.co/1844732284109533347 or its delegations |
| "outreach sheet" | NEW TERM — introduced in f_fd467bd2ae0c6d4f3bd2bc | reached from the hub frederick.stone@harmonygames.co/1844732284109533347 or its delegations |
| "Licence paper timing" | NEW TERM — introduced in frederick.stone@harmonygames.co/1844620296192667598 | reached from the hub frederick.stone@harmonygames.co/1844732284109533347 or its delegations |
| "Oakline Games" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842077918822838564 | 0 base hits (plan/name_census.json) |
| "Tallwater Games" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842077918823428620 | 0 base hits (plan/name_census.json) |
| "Sunfold Mobile" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842077918823258769 | 0 base hits (plan/name_census.json) |
| "Harbor Lane Games" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842077918823445589 | 0 base hits (plan/name_census.json) |
| "Wavecrest Play" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842077918823344908 | 0 base hits (plan/name_census.json) |
| "Copperleaf Games" | NEW TERM — introduced in 495d71a7e14dfaa68cac26fc4a6c4e03 | 0 base hits (plan/name_census.json) |
| "Redwood Arcade" | NEW TERM — introduced in lc_674982ffdca63f854ec6f591 | 0 base hits (plan/name_census.json) |
| "Moonrail Studios" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842077918822811962 | 0 base hits (plan/name_census.json) |
| "Northglow Publishing" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842077918822429064 | 0 base hits (plan/name_census.json) |
| "Pinegrove Games" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842077918823323729 | 0 base hits (plan/name_census.json) |
| "Fernhollow Media" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842077918822912178 | 0 base hits (plan/name_census.json) |
| "Quietbay Games" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842077918822894896 | 0 base hits (plan/name_census.json) |
| "Slatewood Mobile" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842077918823167383 | 0 base hits (plan/name_census.json) |
| "Ironbridge Interactive" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842077918822812534 | 0 base hits (plan/name_census.json) |
| "Tidewell Studios" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842077918822727407 | 0 base hits (plan/name_census.json) |
| "Marlin Play" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842077918823060205 | 0 base hits (plan/name_census.json) |
| "Kitebridge Games" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842077918823167536 | 0 base hits (plan/name_census.json) |
| "Orchard Lane Games" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842077918822627795 | 0 base hits (plan/name_census.json) |
| "Summit Mobile" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842077918822746195 | 0 base hits (plan/name_census.json) |
| "Silverlake Mobile" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842077918822773098 | 0 base hits (plan/name_census.json) |
| "Cedarbrook Play" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842077918822506013 | 0 base hits (plan/name_census.json) |
| "Foxglove Games" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842077918822804025 | 0 base hits (plan/name_census.json) |
| "Riverstone Interactive" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842077918823170401 | 0 base hits (plan/name_census.json) |
| "Bellwether Arcade" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842077918822759281 | 0 base hits (plan/name_census.json) |

Name census with a positive control: plan/name_census.json counts every seeded company name over the base services; exact names are clean and the positive control Balancy is found. First-word counts ('Harbor', 'Redwood', 'Summit') overcount and are not used.

## 1.E Persona reach

Load-bearing ids written to `Working_Files/plan/load_bearing.txt` (20 ids, the services check-sql reads); output verbatim:

```
CHECK-SQL as frederick_stone <frederick.stone@harmonygames.co>
[YES LB] L6 gdrive.drive_files insert d_6fc54be60d1377e340a5b5 - persona owns the file
[YES LB] L9 gdrive.drive_files insert f_5e355d03f6eb6a4e866ead - file is shared with the persona (shared_with_emails)
[YES] L11 gdrive.drive_files insert f_21203dbcdf780cc07c76cb - persona owns the file
[YES LB] L13 gdrive.drive_files insert f_fd467bd2ae0c6d4f3bd2bc - persona owns the file
[YES LB] L15 gdrive.drive_files insert f_4b3ef3dcf76258a6fda5cd - persona owns the file
[YES LB] L17 gdrive.drive_files insert f_27cac0eed300cc33eeb4fd - file is shared with the persona (shared_with_emails)
[YES LB] L19 gdrive.drive_files insert f_e8cb875d5b7c8d9972d259 - file is shared with the persona (shared_with_emails)
[YES LB] L21 gdrive.drive_files insert f_8ddfb9901891eb8e9dcab8 - file is shared with the persona (shared_with_emails)
[YES LB] L23 gdrive.drive_files insert f_d72e8b34e7496f0de668bc - file is shared with the persona (shared_with_emails)
[YES LB] L25 gdrive.drive_files insert f_a6a5647f977d4638b2b8b1 - file is shared with the persona (shared_with_emails)
[YES LB] L27 gdrive.drive_files insert f_464839da025a0a01f53979 - file is shared with the persona (shared_with_emails)
[YES LB] L29 gdrive.drive_files insert f_3eccf6e0bb63955dc51e27 - file is shared with the persona (shared_with_emails)
[YES LB] L31 gdrive.drive_files insert f_5f3ef4a4760d18e696a41a - file is shared with the persona (shared_with_emails)
[YES LB] L33 gdocs.docs_documents insert f_5e355d03f6eb6a4e866ead - file is shared with the persona (shared_with_emails)
[YES] L36 gdocs.docs_documents insert f_21203dbcdf780cc07c76cb - persona owns the file
[YES LB] L38 gdocs.docs_documents insert f_27cac0eed300cc33eeb4fd - file is shared with the persona (shared_with_emails)
[YES LB] L40 gdocs.docs_documents insert f_e8cb875d5b7c8d9972d259 - file is shared with the persona (shared_with_emails)
[YES LB] L42 gdocs.docs_documents insert f_8ddfb9901891eb8e9dcab8 - file is shared with the persona (shared_with_emails)
[YES LB] L44 gdocs.docs_documents insert f_d72e8b34e7496f0de668bc - file is shared with the persona (shared_with_emails)
[YES LB] L46 gdocs.docs_documents insert f_a6a5647f977d4638b2b8b1 - file is shared with the persona (shared_with_emails)
[YES LB] L48 gdocs.docs_documents insert f_464839da025a0a01f53979 - file is shared with the persona (shared_with_emails)
[YES LB] L50 gdocs.docs_documents insert f_3eccf6e0bb63955dc51e27 - file is shared with the persona (shared_with_emails)
[YES LB] L52 gdocs.docs_documents insert f_5f3ef4a4760d18e696a41a - file is shared with the persona (shared_with_emails)
[YES LB] L54 gsheets.sheets_spreadsheets insert f_fd467bd2ae0c6d4f3bd2bc - persona owns the file
[YES LB] L57 gsheets.sheets_sheets insert f_fd467bd2ae0c6d4f3bd2bc, f_fd467bd2ae0c6d4f3bd2bc#0 - persona owns the file
[YES LB] L59 gslides.slides_presentations insert f_4b3ef3dcf76258a6fda5cd - persona owns the file
[YES LB] L62 gslides.slides_pages insert f_4b3ef3dcf76258a6fda5cd, slide_13e87746ab47 - persona owns the file
[YES LB] L64 gslides.slides_page_elements insert f_4b3ef3dcf76258a6fda5cd, el_ef15ab848617, slide_13e87746ab47 - persona owns the file
[YES LB] L66 gslides.slides_page_elements insert f_4b3ef3dcf76258a6fda5cd, el_98d08c30253f, slide_13e87746ab47 - persona owns the file
[YES LB] L68 gslides.slides_pages insert f_4b3ef3dcf76258a6fda5cd, slide_57bcd1eccbff - persona owns the file
[YES LB] L70 gslides.slides_page_elements insert f_4b3ef3dcf76258a6fda5cd, el_0dc8d22f6a62, slide_57bcd1eccbff - persona owns the file
[YES LB] L72 gslides.slides_page_elements insert f_4b3ef3dcf76258a6fda5cd, el_e8c33936e097, slide_57bcd1eccbff - persona owns the file
[YES] L74 slack.slack_messages insert bda432db3ac81bf7f0c8903f0465ec9d, D05S58U4SAK/1757090400.829462 - persona EMPLOYEE_0008_SLACK_ID is in members of im D05S58U4SAK
[YES LB] L77 slack.slack_messages insert f55bd27436eb285a15d833648b922e9b, C096HFA5Z8W/1758915000.867092 - persona EMPLOYEE_0008_SLACK_ID is in members of private bridge-pitch
[YES] L79 slack.slack_messages update 0f6848b39af117c741af520ce5204eac, C096HFA5Z8W/1758147530.732569 - persona EMPLOYEE_0008_SLACK_ID is in members of private bridge-pitch
[YES LB] L80 slack.slack_messages insert 495d71a7e14dfaa68cac26fc4a6c4e03, C07C2866011/1758909900.662794 - persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES] L82 slack.slack_messages update aaec7171d897e134a22b41511467f646, C07C2866011/1758736960.824899 - persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES] L83 slack.slack_messages insert e64606893af9f4316891a357ec26a691, C069FF9Q57S/1758912000.686342 - persona EMPLOYEE_0008_SLACK_ID is in members of private analytics
[YES LB] L85 slack.slack_messages insert e44da6a468e7795a1b5853cfb0763aaf, C07C2866011/1759176900.065118 - persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES LB] L87 slack.slack_messages insert 0230b2df24ec829928fe1c55ad6185bf, C07C2866011/1759251900.005166 - persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES] L89 slack.slack_messages update 330b95fd38236b4e7192e24f272685b4, C07C2866011/1757345405.134829 - persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES] L108 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844732284109533347 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L111 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L113 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1844732284109416443 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L115 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES] L117 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844620296192667598 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L119 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CA9raR_pqldShsvOhd5Uwxoj8zJh2-tzH0UJ5JLd@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L121 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1844620296192385890 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L123 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CA9raR_pqldShsvOhd5Uwxoj8zJh2-tzH0UJ5JLd@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES] L125 gmail.gmail_threads update frederick.stone@harmonygames.co/1844620296192667598 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L126 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAP16wHs998luhyUQ3U3Bw_EguUS8xoTcGPbTVkR@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L128 gmail.gmail_threads update leonard.hayes@harmonygames.co/1844620296192385890 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L129 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAP16wHs998luhyUQ3U3Bw_EguUS8xoTcGPbTVkR@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES] L131 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842077918822838564 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L133 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAP2WDhxJLWVtG1NwcQSex7RGOfppi_U-g7sPCUP@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L135 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918822838564 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L136 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAM3LRAoD9ONdfZj1I_sK0kims9xkE8Z1wOKb9Bn@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L138 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918822838564 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L139 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAybuYiHDdC_1wq0wp32aITdzH-XuQAf6p028lBn@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L141 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842077918823428620 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L143 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CA_SUmrrUxKRZgwUJ7meq3wa1t0gv8lmaNA0AxqE@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L145 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918823428620 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L146 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAUAdeLf4img2MU7lpgaNQ7TUA8UscrZnOFrPzIM@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L148 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918823428620 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L149 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAdmUC104qnASUKfUGKvpnAlXv_5wTuk1nbrDq5R@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L151 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918823428620 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L152 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CATuOaB7ct5kwVWnJ1DYeY416ze49ozfCKLoQBLU@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L154 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842077918823258769 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L156 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAtGdlTBzxQgaYAq5caC-g9PRVoQ_94tAGP52kGI@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L158 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918823258769 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L159 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CA0P8idnP7zRdjtJ2lZBnVlK7c0qGPVJyWzEFNPi@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L161 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842077918823445589 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L163 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAqKllUzAFyNNaZir2SXAEkgeBG_nocow3ehOVtT@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L165 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918823445589 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L166 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAxaKI6sCYMsA4x-jJTOPegatOG93dhOM2IkBkZu@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L168 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918823445589 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L169 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CA7reXRO7A3L9v6OJ5jXK8wXV15hu6VOhaVXoVco@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L171 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918823445589 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L172 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAC883mb0pClouiq2O2H9_P4Yze_j83KmdBQ6rWF@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L174 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842077918823344908 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L176 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CACrJqyP5OVwohR--W7V7Ex6TJmh9HG7Z0UF3sOA@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L178 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918823344908 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L179 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CACs-ibscXxR5QzGFBfPnzJ4aKlDhRIaVEm0l6Y1@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L181 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918823344908 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L182 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAJ_9MoUdsZwMeFbIbezY1sX5upWrJ6NdBLHSQPM@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L184 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918823344908 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L185 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAYPBDL8-vDU_A1uNN4jJK0hCOrcgEGOpfZycr3-@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L187 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842077918822811962 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L189 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAYSOqxN-_aUSJmf23f8gNLe_UHTMcczaivVgnAR@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L191 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918822811962 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L192 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAF7NPNtft83IuPHD4RNvOHVVaSAKUuupaHGK9xF@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L194 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918822811962 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L195 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CA78kSmFAWgUotExWHSn2Dio0jQnI8OSC7eg0dAa@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L197 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918822811962 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L198 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAkAeFrhFWVvHmJEvrJwVpghdSomcBTh00_HZVe2@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L200 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842077918822429064 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L202 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAdwjksxsuJJOcLFSccInoI7aryKcwPx4O6ob5S1@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L204 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918822429064 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L205 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAlXwp5pu0sE1OUziqIpHh8xJz9bPkMraUoIgVCi@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L207 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842077918823323729 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L209 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CACoVq8Ky0haUCZWFtFypRUxkNMJWdC9dTejgVGH@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L211 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918823323729 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L212 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAoasKjUeOpKv0bVxBcuYgNGpAnPyqgPN2YFDm6A@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L214 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842077918822912178 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L216 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAMpr5OcX5NXYR_NYkpn-7mUVL8Sy2Uws8zJQlwd@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L218 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918822912178 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L219 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CA4HMxbTQ3f0dBkdaaG1Ae76fyocZlknsjKVhJ9R@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L221 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842077918822894896 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L223 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAn2ND39zPOi_-9NgZglavLwi60VcJC-9htn__VB@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L225 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918822894896 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L226 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CA8vx_4jNxXdrEo7iNZuLeBKFt_2TSRx_W-uHDeK@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L228 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842077918823167383 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L230 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAY2P49nMwKwieqM8UJErDshyJ3dboYaOkcqoLVt@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L232 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918823167383 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L233 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CATyMO43tqibSWcOd9NXSC8J2ynq1EsQqFHG7zU_@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L235 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842077918822812534 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L237 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CA2Z26MATHdprW0fJr3aBy50lPtqHy8mFzhVvTph@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L239 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918822812534 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L240 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAd_cLOeha5s8T9MxyhMpU8SqfxR99myL6d_XJwC@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L242 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842077918822727407 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L244 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CA4rE7_gd0Maxhae81hliQBOphGPfsKRYKl1zEhs@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L246 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918822727407 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L247 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CABfR1GT5_5Tlu8IKfBsSvYd0hDMc3HJO9f9fXdM@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L249 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842077918823060205 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L251 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAgc-22Ffk7EEQt7iAZ6TfnRKjehq3d_rrHRWkw4@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L253 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918823060205 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L254 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CA9DvG_MtLDt4FJu0RaAYoF6WtnP--Yyluv-Ul4r@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L256 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842077918823167536 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L258 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAI3ko-q07278dY9RYnBJkq6gowuWqjtWuqzRMIi@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L260 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918823167536 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L261 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAozTwdLEuSV1xBSSDwo79l6NXXjAZ74IDmbvVaH@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L263 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842077918822627795 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L265 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAthsveRLmc8kD8nIk91_T_usnG3RnDAog3nyG0C@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L267 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842077918822746195 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L269 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CA2JlxL00XVM6JnIjNrzzVGFxUYr_EK2JWpolBy_@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L271 gmail.gmail_threads update frederick.stone@harmonygames.co/1842077918822746195 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L272 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAVCa1kwMOk0Nk1hOEyoQFgpptDIeEJmjn5Tu8aS@summitmobile.io> - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L274 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842077918822773098 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L276 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAZTUQuC3dVbDRjvKFN9FpiSJP5_rnPT2OSo4NL-@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L278 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842077918822506013 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L280 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CA_SDWWIN5thiywOT41t7qZCbGPAIwSX-rYRRU0b@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L282 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842077918822804025 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L284 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAkwm_uqp3-570V3SRqpxaE1KWy0JFpqMaOA_mRZ@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L286 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842077918823170401 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L288 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAiok9sGZgcpDbXkB-5t5j7hf5IfbUCuB6NWUX65@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L290 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842077918822759281 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L292 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CALyaIXhq7TwAhD0KMN8spxLroVeHjvRZPOGWBEa@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L294 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844346617856625779 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L296 gmail.gmail_messages insert frederick.stone@harmonygames.co/<calendar-e8098c73-3048-61d6-3b65-e2a140abb87a@google.com> - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L298 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844732284109731502 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L300 gmail.gmail_messages insert frederick.stone@harmonygames.co/<calendar-faae36ae-44fe-1770-7d36-36361beb20b0@google.com> - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L302 gmail.gmail_threads insert robert@harmonygames.co/1844732284109187692 - row is in mailbox robert@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L304 gmail.gmail_messages insert robert@harmonygames.co/<calendar-1a05ea6c-8c31-ad9e-5b7c-e50e7f38101c@google.com>, robert@ - row is in mailbox robert@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L306 gmail.gmail_threads insert arthur.blake@harmonygames.co/1844732284108819059 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L308 gmail.gmail_messages insert arthur.blake@harmonygames.co/<calendar-71404a73-f308-e554-ef7c-92f53a65935a@google.com>, a - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] L310 gcal.gcal_events insert evt_43fda04cd11b9d58a05161 - event is on the persona's own calendar frederick.stone@harmonygames.co
[YES] L313 gcal.gcal_events insert evt_c6d68c2a6f110765c48b9b - persona is an attendee and holds its own copy evt_43fda04cd11b9d58a05161 (same ical_uid and start) on frederick.stone@harmonygames.co
[YES] L315 gcal.gcal_events insert evt_d6905d9d5497d6a83a9a56 - event is on the persona's own calendar frederick.stone@harmonygames.co
[YES] L317 gcal.gcal_events insert evt_48e63a8c7304cf9432fb46 - event is on the persona's own calendar frederick.stone@harmonygames.co
[YES] L319 gcal.gcal_events insert evt_881d3e07c598b2205a7ff3 - event is on the persona's own calendar frederick.stone@harmonygames.co
[YES] L321 gcal.gcal_events insert evt_8512c7a6aa483d8aeb6a7d - persona is an attendee and holds its own copy evt_881d3e07c598b2205a7ff3 (same ical_uid and start) on frederick.stone@harmonygames.co
[YES] L323 gcal.gcal_events insert evt_b0d8daa048f918be523cb0 - persona is an attendee and holds its own copy evt_881d3e07c598b2205a7ff3 (same ical_uid and start) on frederick.stone@harmonygames.co
[YES] L325 gcal.gcal_events insert evt_cb02d2cef6eb1d6bd4cd0b - persona is an attendee and holds its own copy evt_881d3e07c598b2205a7ff3 (same ical_uid and start) on frederick.stone@harmonygames.co

summary: {'YES': 153, 'NO': 10}  unscoped rows (always visible): 13
  gcal.gcal_events: {'YES': 8}
  gdocs.docs_documents: {'YES': 10}
  gdrive.drive_files: {'YES': 13}
  gmail.gmail_messages: {'YES': 52, 'NO': 5}
  gmail.gmail_threads: {'YES': 52, 'NO': 5}
  gsheets.sheets_sheets: {'YES': 1}
  gsheets.sheets_spreadsheets: {'YES': 1}
  gslides.slides_page_elements: {'YES': 4}
  gslides.slides_pages: {'YES': 2}
  gslides.slides_presentations: {'YES': 1}
  slack.slack_messages: {'YES': 9}
verdict: PASS (0 load-bearing rows not visible)
```

- C07C2866011 — #executives, Frederick a member LB; seeded C07C2866011/1759176900.065118 and replies C07C2866011/1758909900.662794, C07C2866011/1759251900.005166.
- C096HFA5Z8W — #bridge-pitch, Frederick a member LB; seeded reply C096HFA5Z8W/1758915000.867092.
- C069FF9Q57S — #analytics, Frederick a member; seeded pointer C069FF9Q57S/1758912000.686342.
- D05S58U4SAK — Frederick's DM with Leonard LB; seeded D05S58U4SAK/1757090400.829462.
- Frederick's mailbox: the hub frederick.stone@harmonygames.co/1844732284109533347, the ESG thread frederick.stone@harmonygames.co/1844620296192667598 and every publisher thread (Facts for the human) are INBOX or SENT copies in frederick.stone@harmonygames.co LB.
- Drive: d_6fc54be60d1377e340a5b5, f_fd467bd2ae0c6d4f3bd2bc, f_4b3ef3dcf76258a6fda5cd and f_21203dbcdf780cc07c76cb are Frederick-owned; f_5e355d03f6eb6a4e866ead and every term sheet are shared with him LB.
- Calendar: evt_43fda04cd11b9d58a05161, evt_d6905d9d5497d6a83a9a56, evt_48e63a8c7304cf9432fb46 and evt_881d3e07c598b2205a7ff3 are Frederick's own copies (self:true) LB.
- Unscoped services (Linear, Trello, Contacts; check-sql doesn't read them, plan/load_bearing.txt leaves them out): ENG-2362, lc_674982ffdca63f854ec6f591, 68dab660c900179df4f5f92d, 68d5913004a98be3b4c45408, 68d598387dea3e7fe85e3a0a, 68dbfe80ef9c41b4f4fa8fe9, 5373edb55ca853d6052ecce5. Frederick's reach on the UA/BD board is in `00_PreScenario/cansee_anchors.txt`.
- No designed denial: denied_probes is empty; every load-bearing mail is Frederick's own copy (frederick.stone@harmonygames.co/1844732284109533347), and other people's mailbox and calendar copies are companions, never evidence.

## 1.F Collision

Every id the SQL mints was looked up over its full base collection (`tools/hg.py records --request plan/id_checks_sql.json`, `hg.py search lookup`):
- drive: 53631 base records checked, scan_complete True, 0 matches (plan/id_checks_sql.out.json).
- gcal: 10395 base records checked, scan_complete True, 0 matches (plan/id_checks_sql.out.json).
- trello_cards: 803 base records checked, scan_complete True, 0 matches (plan/id_checks_sql.out.json).
- trello_actions: 5252 base records checked, scan_complete True, 0 matches (plan/id_checks_sql.out.json).
- contacts: 170 base records checked, scan_complete True, 0 matches (plan/id_checks_sql.out.json).
- linear_comments: 0 base records checked, scan_complete True, 0 matches (plan/id_checks_sql.out.json).
- slack: the 6 seeded message ids over messages/*/*.json — 4840 of 4840 files, 610468 records, scan_complete True, 0 hits (plan/slack_lookup.out.json).
- gmail: thread ids (mailbox/((ms << 20) + bits)) and RFC Message-IDs are minted per seeded time; base_check Check A (full-collection uniqueness through its base caches) PASS, see Self-review.
- Body tokens: none minted. PERSON_2694 is reused only for the ESG partner.

## Record ledger

One row per SQL statement (inserts and the companion updates), in SQL order.

| # | SQL line | Table | Id | Manifest element | Carrier | Reach | Discovery role |
|---|---|---|---|---|---|---|---|
| 1 | L6 | gdrive.drive_files | d_6fc54be60d1377e340a5b5 | A3 / K5 | ● | Drive owner or share | write target (anchor A3) |
| 2 | L9 | gdrive.drive_files | f_5e355d03f6eb6a4e866ead | H1 / K1 / K3 / T13 / T9 | ● | Drive owner or share | overturning |
| 3 | L11 | gdrive.drive_files | f_21203dbcdf780cc07c76cb | H1 decoy / T21 | ● | Drive owner or share | decoy |
| 4 | L13 | gdrive.drive_files | f_fd467bd2ae0c6d4f3bd2bc | K2 | ● | Drive owner or share | connecting |
| 5 | L15 | gdrive.drive_files | f_4b3ef3dcf76258a6fda5cd | K10 / T8 | ● | Drive owner or share | connecting |
| 6 | L17 | gdrive.drive_files | f_27cac0eed300cc33eeb4fd | cohort terms: Oakline Games | ● | Drive owner or share | connecting (per-publisher evidence) |
| 7 | L19 | gdrive.drive_files | f_e8cb875d5b7c8d9972d259 | T2 / cohort terms: Tallwater Games | ● | Drive owner or share | claim met first |
| 8 | L21 | gdrive.drive_files | f_8ddfb9901891eb8e9dcab8 | T7 / cohort terms: Sunfold Mobile | ● | Drive owner or share | claim met first |
| 9 | L23 | gdrive.drive_files | f_d72e8b34e7496f0de668bc | cohort terms: Harbor Lane Games | ● | Drive owner or share | connecting (per-publisher evidence) |
| 10 | L25 | gdrive.drive_files | f_a6a5647f977d4638b2b8b1 | cohort terms: Wavecrest Play | ● | Drive owner or share | connecting (per-publisher evidence) |
| 11 | L27 | gdrive.drive_files | f_464839da025a0a01f53979 | cohort terms: Moonrail Studios | ● | Drive owner or share | connecting (per-publisher evidence) |
| 12 | L29 | gdrive.drive_files | f_3eccf6e0bb63955dc51e27 | T6 / cohort terms: Northglow Publishing | ● | Drive owner or share | connecting (per-publisher evidence) |
| 13 | L31 | gdrive.drive_files | f_5f3ef4a4760d18e696a41a | T14 / cohort terms: Pinegrove Games | ● | Drive owner or share | connecting (per-publisher evidence) |
| 14 | L33 | gdocs.docs_documents | f_5e355d03f6eb6a4e866ead | H1 / K1 / K3 / T13 / T9 | ● | Drive owner or share | overturning |
| 15 | L36 | gdocs.docs_documents | f_21203dbcdf780cc07c76cb | H1 decoy / T21 | ● | Drive owner or share | decoy |
| 16 | L38 | gdocs.docs_documents | f_27cac0eed300cc33eeb4fd | cohort terms: Oakline Games | ● | Drive owner or share | connecting (per-publisher evidence) |
| 17 | L40 | gdocs.docs_documents | f_e8cb875d5b7c8d9972d259 | T2 / cohort terms: Tallwater Games | ● | Drive owner or share | claim met first |
| 18 | L42 | gdocs.docs_documents | f_8ddfb9901891eb8e9dcab8 | T7 / cohort terms: Sunfold Mobile | ● | Drive owner or share | claim met first |
| 19 | L44 | gdocs.docs_documents | f_d72e8b34e7496f0de668bc | cohort terms: Harbor Lane Games | ● | Drive owner or share | connecting (per-publisher evidence) |
| 20 | L46 | gdocs.docs_documents | f_a6a5647f977d4638b2b8b1 | cohort terms: Wavecrest Play | ● | Drive owner or share | connecting (per-publisher evidence) |
| 21 | L48 | gdocs.docs_documents | f_464839da025a0a01f53979 | cohort terms: Moonrail Studios | ● | Drive owner or share | connecting (per-publisher evidence) |
| 22 | L50 | gdocs.docs_documents | f_3eccf6e0bb63955dc51e27 | T6 / cohort terms: Northglow Publishing | ● | Drive owner or share | connecting (per-publisher evidence) |
| 23 | L52 | gdocs.docs_documents | f_5f3ef4a4760d18e696a41a | T14 / cohort terms: Pinegrove Games | ● | Drive owner or share | connecting (per-publisher evidence) |
| 24 | L54 | gsheets.sheets_spreadsheets | f_fd467bd2ae0c6d4f3bd2bc | K2 | ● | Drive owner or share | connecting |
| 25 | L57 | gsheets.sheets_sheets | f_fd467bd2ae0c6d4f3bd2bc#Outreach | K2 | ● | Drive owner or share | connecting |
| 26 | L59 | gslides.slides_presentations | f_4b3ef3dcf76258a6fda5cd | K10 / T8 | ● | Drive owner or share | connecting |
| 27 | L62 | gslides.slides_pages | f_4b3ef3dcf76258a6fda5cd#slide_13e87746ab47 | K10 / T8 | ● | Drive owner or share | connecting |
| 28 | L64 | gslides.slides_page_elements | f_4b3ef3dcf76258a6fda5cd#el_ef15ab848617 | K10 / T8 | ● | Drive owner or share | connecting |
| 29 | L66 | gslides.slides_page_elements | f_4b3ef3dcf76258a6fda5cd#el_98d08c30253f | K10 / T8 | ● | Drive owner or share | connecting |
| 30 | L68 | gslides.slides_pages | f_4b3ef3dcf76258a6fda5cd#slide_57bcd1eccbff | K10 / T8 | ● | Drive owner or share | connecting |
| 31 | L70 | gslides.slides_page_elements | f_4b3ef3dcf76258a6fda5cd#el_0dc8d22f6a62 | K10 / T8 | ● | Drive owner or share | connecting |
| 32 | L72 | gslides.slides_page_elements | f_4b3ef3dcf76258a6fda5cd#el_e8c33936e097 | K10 / T8 | ● | Drive owner or share | connecting |
| 33 | L74 | slack.slack_messages | bda432db3ac81bf7f0c8903f0465ec9d | T12 | ● | channel or DM member | connecting |
| 34 | L77 | slack.slack_messages | f55bd27436eb285a15d833648b922e9b | K9 / T8 | ● | channel or DM member | connecting |
| 35 | L79 | slack.slack_messages (UPDATE) | 0f6848b39af117c741af520ce5204eac | companion | ● | channel or DM member | companion (counters / snippet) |
| 36 | L80 | slack.slack_messages | 495d71a7e14dfaa68cac26fc4a6c4e03 | K11 / T4 | ● | channel or DM member | connecting |
| 37 | L82 | slack.slack_messages (UPDATE) | aaec7171d897e134a22b41511467f646 | companion | ● | channel or DM member | companion (counters / snippet) |
| 38 | L83 | slack.slack_messages | e64606893af9f4316891a357ec26a691 | K13 / T5 | ● | channel or DM member | connecting |
| 39 | L85 | slack.slack_messages | e44da6a468e7795a1b5853cfb0763aaf | T3 | ● | channel or DM member | connecting |
| 40 | L87 | slack.slack_messages | 0230b2df24ec829928fe1c55ad6185bf | T1 | ● | channel or DM member | connecting |
| 41 | L89 | slack.slack_messages (UPDATE) | 330b95fd38236b4e7192e24f272685b4 | companion | ● | channel or DM member | companion (counters / snippet) |
| 42 | L90 | trello.trello_cards | 68d5913004a98be3b4c45408 | T10 | ● | unscoped service | connecting |
| 43 | L93 | trello.trello_actions | 68d591301a22988efe387ad0 | companion | ● | unscoped service | connecting |
| 44 | L95 | trello.trello_actions | 68dabd6800e271eb0608d2d6 | T1 | ● | unscoped service | connecting |
| 45 | L97 | trello.trello_cards | 68d598387dea3e7fe85e3a0a | K8 / T10 / T7 | ● | unscoped service | connecting |
| 46 | L99 | trello.trello_actions | 68d59838d15e4b33136f7d16 | companion | ● | unscoped service | connecting |
| 47 | L101 | trello.trello_actions | 68dbfe80ef9c41b4f4fa8fe9 | K8 / T7 | ● | unscoped service | overturning |
| 48 | L103 | trello.trello_cards | 68dab660c900179df4f5f92d | A2 / H3 / K4 | ● | unscoped service | first link |
| 49 | L105 | trello.trello_actions | 68dab6601ab74f77950572c9 | companion | ● | unscoped service | connecting |
| 50 | L107 | trello.trello_boards (UPDATE) | 66da196af476ab78deaa0cef | companion | ● | unscoped service | companion (counters / snippet) |
| 51 | L108 | gmail.gmail_threads | frederick.stone@harmonygames.co/1844732284109533347 | companion | ● | Frederick's mailbox | connecting |
| 52 | L111 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com> | A1 | ● | Frederick's mailbox | first link |
| 53 | L113 | gmail.gmail_threads | leonard.hayes@harmonygames.co/1844732284109416443 | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 54 | L115 | gmail.gmail_messages | leonard.hayes@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com> | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 55 | L117 | gmail.gmail_threads | frederick.stone@harmonygames.co/1844620296192667598 | K6 / T9 | ● | Frederick's mailbox | connecting |
| 56 | L119 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CA9raR_pqldShsvOhd5Uwxoj8zJh2-tzH0UJ5JLd@mail.gmail.com> | K6 / T9 | ● | Frederick's mailbox | connecting |
| 57 | L121 | gmail.gmail_threads | leonard.hayes@harmonygames.co/1844620296192385890 | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 58 | L123 | gmail.gmail_messages | leonard.hayes@harmonygames.co/<CA9raR_pqldShsvOhd5Uwxoj8zJh2-tzH0UJ5JLd@mail.gmail.com> | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 59 | L125 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1844620296192667598 | K6 / T9 | ● | Frederick's mailbox | companion (counters / snippet) |
| 60 | L126 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAP16wHs998luhyUQ3U3Bw_EguUS8xoTcGPbTVkR@mail.gmail.com> | K6 / T9 | ● | Frederick's mailbox | overturning |
| 61 | L128 | gmail.gmail_threads (UPDATE) | leonard.hayes@harmonygames.co/1844620296192385890 | companion | ● | other mailbox | companion (counters / snippet) |
| 62 | L129 | gmail.gmail_messages | leonard.hayes@harmonygames.co/<CAP16wHs998luhyUQ3U3Bw_EguUS8xoTcGPbTVkR@mail.gmail.com> | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 63 | L131 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842077918822838564 | T1 / cohort: Oakline Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 64 | L133 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAP2WDhxJLWVtG1NwcQSex7RGOfppi_U-g7sPCUP@mail.gmail.com> | T1 / cohort: Oakline Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 65 | L135 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918822838564 | T1 / cohort: Oakline Games | ● | Frederick's mailbox | companion (counters / snippet) |
| 66 | L136 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAM3LRAoD9ONdfZj1I_sK0kims9xkE8Z1wOKb9Bn@mail.gmail.com> | T1 / cohort: Oakline Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 67 | L138 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918822838564 | T1 / cohort: Oakline Games | ● | Frederick's mailbox | companion (counters / snippet) |
| 68 | L139 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAybuYiHDdC_1wq0wp32aITdzH-XuQAf6p028lBn@mail.gmail.com> | T1 / cohort: Oakline Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 69 | L141 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842077918823428620 | cohort: Tallwater Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 70 | L143 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CA_SUmrrUxKRZgwUJ7meq3wa1t0gv8lmaNA0AxqE@mail.gmail.com> | cohort: Tallwater Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 71 | L145 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918823428620 | cohort: Tallwater Games | ● | Frederick's mailbox | companion (counters / snippet) |
| 72 | L146 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAUAdeLf4img2MU7lpgaNQ7TUA8UscrZnOFrPzIM@mail.gmail.com> | cohort: Tallwater Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 73 | L148 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918823428620 | cohort: Tallwater Games | ● | Frederick's mailbox | companion (counters / snippet) |
| 74 | L149 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAdmUC104qnASUKfUGKvpnAlXv_5wTuk1nbrDq5R@mail.gmail.com> | cohort: Tallwater Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 75 | L151 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918823428620 | cohort: Tallwater Games | ● | Frederick's mailbox | companion (counters / snippet) |
| 76 | L152 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CATuOaB7ct5kwVWnJ1DYeY416ze49ozfCKLoQBLU@mail.gmail.com> | cohort: Tallwater Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 77 | L154 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842077918823258769 | cohort: Sunfold Mobile | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 78 | L156 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAtGdlTBzxQgaYAq5caC-g9PRVoQ_94tAGP52kGI@mail.gmail.com> | cohort: Sunfold Mobile | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 79 | L158 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918823258769 | cohort: Sunfold Mobile | ● | Frederick's mailbox | companion (counters / snippet) |
| 80 | L159 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CA0P8idnP7zRdjtJ2lZBnVlK7c0qGPVJyWzEFNPi@mail.gmail.com> | cohort: Sunfold Mobile | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 81 | L161 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842077918823445589 | cohort: Harbor Lane Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 82 | L163 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAqKllUzAFyNNaZir2SXAEkgeBG_nocow3ehOVtT@mail.gmail.com> | cohort: Harbor Lane Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 83 | L165 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918823445589 | cohort: Harbor Lane Games | ● | Frederick's mailbox | companion (counters / snippet) |
| 84 | L166 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAxaKI6sCYMsA4x-jJTOPegatOG93dhOM2IkBkZu@mail.gmail.com> | cohort: Harbor Lane Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 85 | L168 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918823445589 | cohort: Harbor Lane Games | ● | Frederick's mailbox | companion (counters / snippet) |
| 86 | L169 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CA7reXRO7A3L9v6OJ5jXK8wXV15hu6VOhaVXoVco@mail.gmail.com> | cohort: Harbor Lane Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 87 | L171 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918823445589 | cohort: Harbor Lane Games | ● | Frederick's mailbox | companion (counters / snippet) |
| 88 | L172 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAC883mb0pClouiq2O2H9_P4Yze_j83KmdBQ6rWF@mail.gmail.com> | cohort: Harbor Lane Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 89 | L174 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842077918823344908 | cohort: Wavecrest Play | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 90 | L176 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CACrJqyP5OVwohR--W7V7Ex6TJmh9HG7Z0UF3sOA@mail.gmail.com> | cohort: Wavecrest Play | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 91 | L178 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918823344908 | cohort: Wavecrest Play | ● | Frederick's mailbox | companion (counters / snippet) |
| 92 | L179 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CACs-ibscXxR5QzGFBfPnzJ4aKlDhRIaVEm0l6Y1@mail.gmail.com> | cohort: Wavecrest Play | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 93 | L181 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918823344908 | cohort: Wavecrest Play | ● | Frederick's mailbox | companion (counters / snippet) |
| 94 | L182 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAJ_9MoUdsZwMeFbIbezY1sX5upWrJ6NdBLHSQPM@mail.gmail.com> | cohort: Wavecrest Play | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 95 | L184 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918823344908 | cohort: Wavecrest Play | ● | Frederick's mailbox | companion (counters / snippet) |
| 96 | L185 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAYPBDL8-vDU_A1uNN4jJK0hCOrcgEGOpfZycr3-@mail.gmail.com> | cohort: Wavecrest Play | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 97 | L187 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842077918822811962 | T3 / cohort: Moonrail Studios | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 98 | L189 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAYSOqxN-_aUSJmf23f8gNLe_UHTMcczaivVgnAR@mail.gmail.com> | T3 / cohort: Moonrail Studios | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 99 | L191 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918822811962 | T3 / cohort: Moonrail Studios | ● | Frederick's mailbox | companion (counters / snippet) |
| 100 | L192 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAF7NPNtft83IuPHD4RNvOHVVaSAKUuupaHGK9xF@mail.gmail.com> | T3 / cohort: Moonrail Studios | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 101 | L194 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918822811962 | T3 / cohort: Moonrail Studios | ● | Frederick's mailbox | companion (counters / snippet) |
| 102 | L195 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CA78kSmFAWgUotExWHSn2Dio0jQnI8OSC7eg0dAa@mail.gmail.com> | T3 / cohort: Moonrail Studios | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 103 | L197 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918822811962 | T3 / cohort: Moonrail Studios | ● | Frederick's mailbox | companion (counters / snippet) |
| 104 | L198 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAkAeFrhFWVvHmJEvrJwVpghdSomcBTh00_HZVe2@mail.gmail.com> | T3 / cohort: Moonrail Studios | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 105 | L200 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842077918822429064 | cohort: Northglow Publishing | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 106 | L202 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAdwjksxsuJJOcLFSccInoI7aryKcwPx4O6ob5S1@mail.gmail.com> | cohort: Northglow Publishing | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 107 | L204 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918822429064 | cohort: Northglow Publishing | ● | Frederick's mailbox | companion (counters / snippet) |
| 108 | L205 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAlXwp5pu0sE1OUziqIpHh8xJz9bPkMraUoIgVCi@mail.gmail.com> | cohort: Northglow Publishing | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 109 | L207 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842077918823323729 | cohort: Pinegrove Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 110 | L209 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CACoVq8Ky0haUCZWFtFypRUxkNMJWdC9dTejgVGH@mail.gmail.com> | cohort: Pinegrove Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 111 | L211 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918823323729 | cohort: Pinegrove Games | ● | Frederick's mailbox | companion (counters / snippet) |
| 112 | L212 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAoasKjUeOpKv0bVxBcuYgNGpAnPyqgPN2YFDm6A@mail.gmail.com> | cohort: Pinegrove Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 113 | L214 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842077918822912178 | cohort: Fernhollow Media | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 114 | L216 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAMpr5OcX5NXYR_NYkpn-7mUVL8Sy2Uws8zJQlwd@mail.gmail.com> | cohort: Fernhollow Media | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 115 | L218 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918822912178 | cohort: Fernhollow Media | ● | Frederick's mailbox | companion (counters / snippet) |
| 116 | L219 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CA4HMxbTQ3f0dBkdaaG1Ae76fyocZlknsjKVhJ9R@mail.gmail.com> | cohort: Fernhollow Media | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 117 | L221 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842077918822894896 | cohort: Quietbay Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 118 | L223 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAn2ND39zPOi_-9NgZglavLwi60VcJC-9htn__VB@mail.gmail.com> | cohort: Quietbay Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 119 | L225 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918822894896 | cohort: Quietbay Games | ● | Frederick's mailbox | companion (counters / snippet) |
| 120 | L226 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CA8vx_4jNxXdrEo7iNZuLeBKFt_2TSRx_W-uHDeK@mail.gmail.com> | cohort: Quietbay Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 121 | L228 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842077918823167383 | cohort: Slatewood Mobile | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 122 | L230 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAY2P49nMwKwieqM8UJErDshyJ3dboYaOkcqoLVt@mail.gmail.com> | cohort: Slatewood Mobile | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 123 | L232 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918823167383 | cohort: Slatewood Mobile | ● | Frederick's mailbox | companion (counters / snippet) |
| 124 | L233 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CATyMO43tqibSWcOd9NXSC8J2ynq1EsQqFHG7zU_@mail.gmail.com> | cohort: Slatewood Mobile | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 125 | L235 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842077918822812534 | cohort: Ironbridge Interactive | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 126 | L237 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CA2Z26MATHdprW0fJr3aBy50lPtqHy8mFzhVvTph@mail.gmail.com> | cohort: Ironbridge Interactive | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 127 | L239 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918822812534 | cohort: Ironbridge Interactive | ● | Frederick's mailbox | companion (counters / snippet) |
| 128 | L240 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAd_cLOeha5s8T9MxyhMpU8SqfxR99myL6d_XJwC@mail.gmail.com> | cohort: Ironbridge Interactive | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 129 | L242 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842077918822727407 | cohort: Tidewell Studios | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 130 | L244 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CA4rE7_gd0Maxhae81hliQBOphGPfsKRYKl1zEhs@mail.gmail.com> | cohort: Tidewell Studios | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 131 | L246 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918822727407 | cohort: Tidewell Studios | ● | Frederick's mailbox | companion (counters / snippet) |
| 132 | L247 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CABfR1GT5_5Tlu8IKfBsSvYd0hDMc3HJO9f9fXdM@mail.gmail.com> | cohort: Tidewell Studios | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 133 | L249 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842077918823060205 | cohort: Marlin Play | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 134 | L251 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAgc-22Ffk7EEQt7iAZ6TfnRKjehq3d_rrHRWkw4@mail.gmail.com> | cohort: Marlin Play | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 135 | L253 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918823060205 | cohort: Marlin Play | ● | Frederick's mailbox | companion (counters / snippet) |
| 136 | L254 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CA9DvG_MtLDt4FJu0RaAYoF6WtnP--Yyluv-Ul4r@mail.gmail.com> | cohort: Marlin Play | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 137 | L256 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842077918823167536 | cohort: Kitebridge Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 138 | L258 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAI3ko-q07278dY9RYnBJkq6gowuWqjtWuqzRMIi@mail.gmail.com> | cohort: Kitebridge Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 139 | L260 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918823167536 | cohort: Kitebridge Games | ● | Frederick's mailbox | companion (counters / snippet) |
| 140 | L261 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAozTwdLEuSV1xBSSDwo79l6NXXjAZ74IDmbvVaH@mail.gmail.com> | cohort: Kitebridge Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 141 | L263 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842077918822627795 | cohort: Orchard Lane Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 142 | L265 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAthsveRLmc8kD8nIk91_T_usnG3RnDAog3nyG0C@mail.gmail.com> | cohort: Orchard Lane Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 143 | L267 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842077918822746195 | T11 / cohort: Summit Mobile | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 144 | L269 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CA2JlxL00XVM6JnIjNrzzVGFxUYr_EK2JWpolBy_@mail.gmail.com> | T11 / cohort: Summit Mobile | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 145 | L271 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842077918822746195 | T11 / cohort: Summit Mobile | ● | Frederick's mailbox | companion (counters / snippet) |
| 146 | L272 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAVCa1kwMOk0Nk1hOEyoQFgpptDIeEJmjn5Tu8aS@summitmobile.io> | T11 / cohort: Summit Mobile | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 147 | L274 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842077918822773098 | cohort: Silverlake Mobile | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 148 | L276 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAZTUQuC3dVbDRjvKFN9FpiSJP5_rnPT2OSo4NL-@mail.gmail.com> | cohort: Silverlake Mobile | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 149 | L278 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842077918822506013 | cohort: Cedarbrook Play | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 150 | L280 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CA_SDWWIN5thiywOT41t7qZCbGPAIwSX-rYRRU0b@mail.gmail.com> | cohort: Cedarbrook Play | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 151 | L282 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842077918822804025 | cohort: Foxglove Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 152 | L284 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAkwm_uqp3-570V3SRqpxaE1KWy0JFpqMaOA_mRZ@mail.gmail.com> | cohort: Foxglove Games | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 153 | L286 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842077918823170401 | cohort: Riverstone Interactive | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 154 | L288 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAiok9sGZgcpDbXkB-5t5j7hf5IfbUCuB6NWUX65@mail.gmail.com> | cohort: Riverstone Interactive | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 155 | L290 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842077918822759281 | cohort: Bellwether Arcade | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 156 | L292 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CALyaIXhq7TwAhD0KMN8spxLroVeHjvRZPOGWBEa@mail.gmail.com> | cohort: Bellwether Arcade | ● | Frederick's mailbox | connecting (per-publisher evidence) |
| 157 | L294 | gmail.gmail_threads | frederick.stone@harmonygames.co/1844346617856625779 | companion | ● | Frederick's mailbox | connecting |
| 158 | L296 | gmail.gmail_messages | frederick.stone@harmonygames.co/<calendar-e8098c73-3048-61d6-3b65-e2a140abb87a@google.com> | companion | ● | Frederick's mailbox | companion (INT-11 invitation) |
| 159 | L298 | gmail.gmail_threads | frederick.stone@harmonygames.co/1844732284109731502 | companion | ● | Frederick's mailbox | connecting |
| 160 | L300 | gmail.gmail_messages | frederick.stone@harmonygames.co/<calendar-faae36ae-44fe-1770-7d36-36361beb20b0@google.com> | companion | ● | Frederick's mailbox | companion (INT-11 invitation) |
| 161 | L302 | gmail.gmail_threads | robert@harmonygames.co/1844732284109187692 | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 162 | L304 | gmail.gmail_messages | robert@harmonygames.co/<calendar-1a05ea6c-8c31-ad9e-5b7c-e50e7f38101c@google.com> | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 163 | L306 | gmail.gmail_threads | arthur.blake@harmonygames.co/1844732284108819059 | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 164 | L308 | gmail.gmail_messages | arthur.blake@harmonygames.co/<calendar-71404a73-f308-e554-ef7c-92f53a65935a@google.com> | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 165 | L310 | gcal.gcal_events | evt_43fda04cd11b9d58a05161 | K7 / T2 | ● (summary, attendees, time; description ○) | Frederick's calendar (self) | overturning |
| 166 | L313 | gcal.gcal_events | evt_c6d68c2a6f110765c48b9b | companion | ● (summary, attendees, time; description ○) | other calendar | companion copy (another attendee's mailbox or calendar) |
| 167 | L315 | gcal.gcal_events | evt_d6905d9d5497d6a83a9a56 | companion | ● (summary, attendees, time; description ○) | Frederick's calendar (self) | connecting |
| 168 | L317 | gcal.gcal_events | evt_48e63a8c7304cf9432fb46 | companion | ● (summary, attendees, time; description ○) | Frederick's calendar (self) | connecting |
| 169 | L319 | gcal.gcal_events | evt_881d3e07c598b2205a7ff3 | companion | ● (summary, attendees, time; description ○) | Frederick's calendar (self) | connecting |
| 170 | L321 | gcal.gcal_events | evt_8512c7a6aa483d8aeb6a7d | companion | ● (summary, attendees, time; description ○) | other calendar | companion copy (another attendee's mailbox or calendar) |
| 171 | L323 | gcal.gcal_events | evt_b0d8daa048f918be523cb0 | companion | ● (summary, attendees, time; description ○) | other calendar | companion copy (another attendee's mailbox or calendar) |
| 172 | L325 | gcal.gcal_events | evt_cb02d2cef6eb1d6bd4cd0b | companion | ● (summary, attendees, time; description ○) | other calendar | companion copy (another attendee's mailbox or calendar) |
| 173 | L327 | linear.linear_comments | ENG-2362 comment lc_674982ffdca63f854ec6f591 | K12 / T5 | ● (§6b) | unscoped service | connecting |
| 174 | L330 | linear.linear_issues (UPDATE) | ENG-2362 | companion | ● | unscoped service | companion (counters / snippet) |
| 175 | L331 | contacts.contacts | 5373edb55ca853d6052ecce5 | K15 / T3 | ● (email, job) | unscoped service | connecting |
| 176 | L334 | contacts.contacts | 1d6fd505d2fea08fa0f26c6e | K15 | ● (email, job) | unscoped service | connecting |

## Findability and discovery-order proofs

- Hub (A1) frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com> in frederick.stone@harmonygames.co/1844732284109533347: Leonard → Frederick, Sep 30 23:10Z; a gmail search for 'DD publishing' or 'Monday' returns it first (newest). First link.
- Ground rules H1 f_5e355d03f6eb6a4e866ead: the hub names 'the ground rules doc'; a Drive or Docs search for 'ground rules' returns it; the competing hit is Frederick's co-dev doc f_21203dbcdf780cc07c76cb (decoy, co-dev only, not DD). Shared with Frederick directly; Leonard's parent folder isn't needed.
- Rights H2: the rule doc names 'the position from the August sync'; a search for 'non-mobile' or 'rights' returns the sync doc f_26e1f9a86761e35049192a and Leonard's post C07C2866011/1756140953.197759.
- Card H3 68dab660c900179df4f5f92d: the hub names 'the DD publishing card on the UA/BD board'; a board read lists it on BD Follow Up.
- T1 DONE: claim met first — Marek's mail frederick.stone@harmonygames.co/<CAybuYiHDdC_1wq0wp32aITdzH-XuQAf6p028lBn@mail.gmail.com> (wire sent Sep 29) and Frederick's card comment 68dabd6800e271eb0608d2d6; overturned by Arthur's reply 0230b2df24ec829928fe1c55ad6185bf (Sep 30) under the Sep 8 banker root, found by a Slack search on 'SVB', 'first-look' or a read of the #executives thread.
- T2 CORR: claim met first — Tallwater's term sheet f_e8cb875d5b7c8d9972d259 ($60,000); overturned by the note past the agenda on evt_43fda04cd11b9d58a05161, read with the event's full description.
- T3 ALIAS: claim met first — Moonrail's term sheet f_464839da025a0a01f53979; overturned by Robert's post e44da6a468e7795a1b5853cfb0763aaf ('Kestrel' only), joined through Anika's signature in frederick.stone@harmonygames.co/1842077918822811962 and contact 5373edb55ca853d6052ecce5.
- T4 FILT: Copperleaf's offer sits in Robert's reply 495d71a7e14dfaa68cac26fc4a6c4e03 under the Sep 24 70 % D1 root; it isn't on the sheet or in Frederick's inbox; a Slack search for 'publisher', 'advance' or 'installs' or a read of that thread finds it.
- T5 FILT: Redwood's offer sits in the comment lc_674982ffdca63f854ec6f591 on ENG-2362, behind Arthur's #analytics pointer e64606893af9f4316891a357ec26a691, which says 'a publisher' and names the ticket.
- T6, T14 EXC: Northglow's and Pinegrove's term sheets f_3eccf6e0bb63955dc51e27, f_5f3ef4a4760d18e696a41a take non-mobile rights or the code; the rule doc's 'Out on rights' line points at the August position.
- T7 INPUT: claim met first — Sunfold's term sheet f_8ddfb9901891eb8e9dcab8 (50,000); overturned by Frederick's comment 68dbfe80ef9c41b4f4fa8fe9 on the card 'F/up with Lena' 68d598387dea3e7fe85e3a0a, reached by reading the list and joining Lena to Sunfold through the sheet.
- T8 FOLLOW: Leonard's reply f55bd27436eb285a15d833648b922e9b under the Sep 17 Matthew root in #bridge-pitch; the rule doc's last line carries it; the outreach sheet's 'What we sent' column picks the recipients.
- T9 DATE: the rule doc says Oct 31 unless the lawyers give a later date; ESG's mail frederick.stone@harmonygames.co/<CA9raR_pqldShsvOhd5Uwxoj8zJh2-tzH0UJ5JLd@mail.gmail.com> and Leonard's reply frederick.stone@harmonygames.co/<CAP16wHs998luhyUQ3U3Bw_EguUS8xoTcGPbTVkR@mail.gmail.com> ('License paper timing') set Nov 14.
- T10: the two existing cards 68d5913004a98be3b4c45408, 68d598387dea3e7fe85e3a0a are named for people. T11: Summit's auto-ack sits in frederick.stone@harmonygames.co/1842077918822746195. T12: Frederick's Sep 4 Rayking message in frederick.stone@harmonygames.co/1842348778705877030 is an unsent draft; his seeded DM bda432db3ac81bf7f0c8903f0465ec9d says they still owe an answer.

## Self-validation

| QC category | Tool-enforced (result) | Manual (evidence) |
|---|---|---|
| Missing Universe Data | check-sql PASS (1.E) | every deciding fact is persona-readable: 0230b2df24ec829928fe1c55ad6185bf, evt_43fda04cd11b9d58a05161, e44da6a468e7795a1b5853cfb0763aaf, 495d71a7e14dfaa68cac26fc4a6c4e03, lc_674982ffdca63f854ec6f591, 68dbfe80ef9c41b4f4fa8fe9, frederick.stone@harmonygames.co/<CA9raR_pqldShsvOhd5Uwxoj8zJh2-tzH0UJ5JLd@mail.gmail.com>, f55bd27436eb285a15d833648b922e9b |
| Temporal Field | sql_lint 0 errors; base_check Check C PASS | text dates agree: the rule doc (Mon Sep 29) says Monday's talk = Oct 6, the event evt_881d3e07c598b2205a7ff3; Arthur's Sep 30 'next week' is Oct 6–10; ESG's Nov 14 follows its Nov 7 arbitration |
| Cross-service Referential | base_check Check A PASS | one name and amount per publisher across thread, term sheet and sheet; Lena Fischer and Anika Rao match their Contacts rows |
| Quantitative | reply counters updated on the three base roots; Trello badges match comments | every value comes from solver/truth.json; keep value re-read from the warehouse by the blind reviewer |
| State / Lifecycle | ENG-2362 stays Todo with Arthur | the comment is a note on his own open ticket; 68dab660c900179df4f5f92d is an open card |
| Identifier / Format | eval lint FAIL 0 CHECK 0 | ids follow base schemes (1.A); roster addresses in every seeded row (I03) |
| Semantic / Category | — | titles match content (f_5e355d03f6eb6a4e866ead, 68dab660c900179df4f5f92d, f_21203dbcdf780cc07c76cb) |
| Other | — | voice per 1.C; no record states a decision, a total or the model |

## Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| gcal | INT-11 | invitation mails | seeded: the Monday execs event (Frederick, Robert, Arthur; Leonard organizes) and the Tallwater call (Frederick). Frederick organized the Harbor Lane and Wavecrest calls himself with one outside guest, so no invitation lands in a HarmonyGames mailbox: declared in integration_exceptions (no_notify), the same shape the base shows |
| linear | INT-03, INT-04, INT-05 | linear[bot] PR comment / Slack DM / mail digest | none: ENG-2362 has no PR; Arthur comments on his own issue (no notification to Frederick) |
| gdrive | INT-13 | Drive Slack app share DM | none: the term sheets and f_5e355d03f6eb6a4e866ead are shared by name; the base share DMs are not universal, and no fact rests on one |
| slack | INT-22 | Slack e-mail notifications | none: Frederick's base mailbox holds almost no such threads |
| trello | INT-21 | no Trello→Slack integration | none (68dab660c900179df4f5f92d posts nowhere) |
| gmail, gdocs, gsheets, gslides, contacts | not integration sources | — | none |

## Touched-data census and coherence hazards

Touched data: the hub frederick.stone@harmonygames.co/1844732284109533347 and copies; the rule doc f_5e355d03f6eb6a4e866ead and decoy f_21203dbcdf780cc07c76cb; the DD publishing folder d_6fc54be60d1377e340a5b5 with the outreach sheet f_fd467bd2ae0c6d4f3bd2bc and eight term sheets; the one-pager f_4b3ef3dcf76258a6fda5cd; the UA/BD board 66da196af476ab78deaa0cef (list 670015c2ecd45b634d5eec81, cards 68dab660c900179df4f5f92d, 68d5913004a98be3b4c45408, 68d598387dea3e7fe85e3a0a); #executives (roots C07C2866011/1757345405.134829, C07C2866011/1758736960.824899, posts C07C2866011/1756140953.197759, C07C2866011/1756251167.453019, C07C2866011/1757516293.887729, C07C2866011/1756261199.570279); #bridge-pitch (root C096HFA5Z8W/1758147530.732569, posts C096HFA5Z8W/1757542591.718649, C096HFA5Z8W/1758210489.170809); #analytics; DM D05S58U4SAK (D05S58U4SAK/1758736747.409459, D05S58U4SAK/1758735778.095599, D05S58U4SAK/1758736827.548589, D05S58U4SAK/1758736842.534589, D05S58U4SAK/1757009185.631739); ENG-2362; the warehouse table ANALYTICS.MONETIZATION.REVENUE_DAILY; the sync doc f_26e1f9a86761e35049192a; Frederick's Publishing Partners f_10dfa1b4236a7c35dcb632 and Biz Dev Notes f_0d17fc08eddaf231cf7f28; the Appodeal and Rayking threads frederick.stone@harmonygames.co/1830012626042968381, frederick.stone@harmonygames.co/1842348778705877030; Tilting Point's ack frederick.stone@harmonygames.co/1842443183462721250; the board note frederick.stone@harmonygames.co/1830890312657338682; every publisher thread.

Hazards from coherence_hazards.json:
- temporal: T02 — seeded threads run in date order (base_check Check C); the base Rayking thread keeps its own order and no seed is appended to it.
- semantic: S04 (Frederick's GitHub 'Ryan') avoided — no GitHub record touched; other semantic hazards: none in scope.
- cross-service referential: R04 avoided — seeded Slack names documents by title, never by link; R08 — seeded meetings carry invitation copies, except the two declared no_notify calls.
- quantitative: Q01, Q03 — the three seeded replies update reply_count, reply_users_count and latest_reply on their roots (hazard_acknowledgements dated_claim); Q09 — the rule doc names one table, and V2 mirrors it; Q10 — one identical body per mailbox copy.
- state/lifecycle: L08 — ENG-2362 is assigned to Arthur, active at the clock; other lifecycle hazards: none in scope.
- identifier/format: I03 — seeded rows use the roster address frederick.stone@harmonygames.co; I04 — RFC-2822 dates; I15 — seeded docs keep one title in Drive and Docs; I16 — Trello ids encode their action time.

Known data issues (references/known_data_issues/synthcut.md, read for every touched record; no load-bearing fact, trap or graded slot rests on a card's 'Don't grade' value):
- SC-1 (installs in the warehouse): excluded; monthly installs are publisher commitments.
- SC-35, SC-3 (warehouse revenue against P&L workbooks): excluded; Frederick can open none of the P&L workbooks, and the keep value reads one named table.
- SC-17 (ad-revenue payouts per network): excluded; keep value uses total_revenue_usd, never a network figure.
- SC-3, SC-5, SC-73 (runway, burn, cash balance): excluded; no deliverable asks for them.
- SC-39, SC-63 (Singular and Griffin lines in the sync doc): excluded; only the rights line of f_26e1f9a86761e35049192a is cited.
- SC-6 (vendor mail from brian.foster@): excluded; no vendor mail is on the path.
- SC-49, SC-54 (Frederick's founder status and pay): no row grades either.
- SC-9, SC-10, SC-33, SC-34 (investor sheet rows): investor work is out of scope.

## Intended disagreements

| Claim met first | Overturning record | Why realistic | Resolution |
|---|---|---|---|
| Marek's mail frederick.stone@harmonygames.co/<CAybuYiHDdC_1wq0wp32aITdzH-XuQAf6p028lBn@mail.gmail.com> and card comment 68dabd6800e271eb0608d2d6: the $10,000 went out Sep 29 | Arthur's reply 0230b2df24ec829928fe1c55ad6185bf (Sep 30): it never hit the account | a wire can bounce on a wrong beneficiary; the sender reports sending, the bank reports receipt | Banked means in the SVB account (rule doc): $0; the resend lands in October |
| Tallwater's term sheet f_e8cb875d5b7c8d9972d259: $60,000 | note on evt_43fda04cd11b9d58a05161: $40,000 now | publishers revise terms on calls and nobody reissues the paper at once | use the latest terms, wherever they are (rule doc) |
| Sunfold's term sheet f_8ddfb9901891eb8e9dcab8: 50,000 installs | Frederick's comment 68dbfe80ef9c41b4f4fa8fe9: 30,000 | a budget cut told by phone lands on a follow-up card | use the latest terms |
| Moonrail's term sheet f_464839da025a0a01f53979 | Robert's post e44da6a468e7795a1b5853cfb0763aaf: Kestrel froze signings | a parent's call reaches one founder, who names the parent | Withdrawn (first that fits); Anika's signature and Contacts join the names |
| the rule doc f_5e355d03f6eb6a4e866ead: sign Oct 31 | ESG's note frederick.stone@harmonygames.co/<CA9raR_pqldShsvOhd5Uwxoj8zJh2-tzH0UJ5JLd@mail.gmail.com> and Leonard frederick.stone@harmonygames.co/<CAP16wHs998luhyUQ3U3Bw_EguUS8xoTcGPbTVkR@mail.gmail.com>: Nov 14 | counsel's calendar moves a planning date | the rule doc says use the lawyers' date |
| Northglow's and Pinegrove's offers have the highest 12-month values | the August position C07C2866011/1756140953.197759, f_26e1f9a86761e35049192a | publishers ask for more than a founder has said they'd give | Out on rights sits above Live in the rule doc |
| the Apr 30 board note frederick.stone@harmonygames.co/1830890312657338682: paid-traffic numbers | Leonard's Sep 24 organic figure D05S58U4SAK/1758736747.409459 | a founder picks the planning figure | the rule doc sets $0.50 |
| Frederick's Sep 4 message in frederick.stone@harmonygames.co/1842348778705877030 looks like a reply | its Drafts label; his DM bda432db3ac81bf7f0c8903f0465ec9d: we still owe them an answer | drafts sit unsent | Waiting on us |
| Summit's mail in frederick.stone@harmonygames.co/1842077918822746195 looks like an answer | the rule doc's No reply line | auto-acks are common | No reply |

## Constraints for the prompt brief

| Anchor | May be named (noun phrases only) | Record |
|---|---|---|
| A1 | Leonard's email from yesterday | frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com> |
| A2 | the DD publishing card | 68dab660c900179df4f5f92d |
| A3 | my DD publishing folder | d_6fc54be60d1377e340a5b5 |

Never name in the prompt: the rule doc's rules, the rights position, any publisher, Copperleaf's or Redwood's route, ENG-2362, Kestrel, the SVB reply, the Tallwater note, the Sunfold comment, the Nov 14 date, the organic figure or Leonard's standing line.

## Fact sheet

| Key | Value | Kind | Home / must appear in |
|---|---|---|---|
| Oakline wire returned | never hit the account | status | 0230b2df24ec829928fe1c55ad6185bf |
| Tallwater advance | The advance is $40,000 now | status | evt_43fda04cd11b9d58a05161, evt_c6d68c2a6f110765c48b9b |
| Kestrel freeze | frozen every outside signing | status | e44da6a468e7795a1b5853cfb0763aaf |
| Copperleaf terms | 28% of net | status | 495d71a7e14dfaa68cac26fc4a6c4e03 |
| Redwood terms | 24% of net | status | lc_674982ffdca63f854ec6f591 |
| Sunfold installs | only commit 30,000 installs a month | status | 68dbfe80ef9c41b4f4fa8fe9 |
| signing date | Nov 14 | date | frederick.stone@harmonygames.co/<CA9raR_pqldShsvOhd5Uwxoj8zJh2-tzH0UJ5JLd@mail.gmail.com>, frederick.stone@harmonygames.co/<CAP16wHs998luhyUQ3U3Bw_EguUS8xoTcGPbTVkR@mail.gmail.com> |
| organic figure line | hears the organic figure from us | status | f55bd27436eb285a15d833648b922e9b |
| Northglow grant | all digital storefronts and platforms | status | f_3eccf6e0bb63955dc51e27 |
| Pinegrove grant | full source code and build pipeline | status | f_5f3ef4a4760d18e696a41a |
| model sheet name | DD publishing model | status | f_5e355d03f6eb6a4e866ead |

```
FACT CHECK: PASS — 107 text-bearing rows, 11 declared facts, 5 declared superseded records
Errors: none
Warnings (2):
  line 38: gdocs.docs_documents f_27cac0eed300cc33eeb4fd: [value_drift] 'advance' carries 2 different amounts across rows: '$40,000' (line 310, row evt_43fda04cd11b9d58a05161, +1); '$10,000' (line 38, row f_27cac0eed300cc33eeb4fd) — supersession (declare it in traps[].version_records / facts) or drift?
  line 126: gmail.gmail_messages frederick.stone@harmonygames.co/<CAP16wHs998luhyUQ3U3Bw_EguUS8xoTcGPbTVkR@mail.gmail.com>: [value_drift] 'signing' carries 2 different dates across rows: 'Nov 14' (line 126, row frederick.stone@harmonygames.co/<CAP16wHs998luhyUQ3U3Bw_EguUS8xoTcGPbTVkR@mail.gmail.com>, +1); 'Oct 31' (line 126, row frederick.stone@harmonygames.co/<CAP16wHs998luhyUQ3U3Bw_EguUS8xoTcGPbTVkR@mail.gmail.com>, +1) — supersession (declare it in traps[].version_records / facts) or drift?
```

fact_check drift warnings: each compares different publishers' amounts or the two dated signing dates; both are intended (a per-publisher value, and a superseded date declared in T9). No fix needed.

Solver totals (`solver/truth.json`): 26 publishers; {'Live': 7, 'No reply': 7, 'Out on rights': 2, 'Passed': 6, 'Waiting on us': 3, 'Withdrawn': 1}; first pick Copperleaf Games, 67200 over 12 months, 32000 in Q4; banked 0; keep value 12723.96; contacts to add 14; new cards 15, card comments 2, reminders 7, organic notes 3, nudges 7.

## Facts for the human

| Locator | Base/seeded | Fact | Reach | Role |
|---|---|---|---|---|
| frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com> | seeded | Leonard → Frederick, 2025-09-30T23:10Z, 'DD publishing: what I need for Monday': the model, the card, Contacts, the reply | Frederick's mailbox | first link (A1) |
| f_5e355d03f6eb6a4e866ead | seeded | Leonard, Sep 29: who's in, status order, valuing, Q4 cash, keep value, first pick, reminders, layout | shared with Frederick | authority H1 |
| f_21203dbcdf780cc07c76cb | seeded | Frederick, Sep 19: co-dev terms, not DD | Frederick owns | decoy |
| 68dab660c900179df4f5f92d | seeded | Leonard, Sep 29: checklists, follow-up cards, nudges | unscoped | authority H3 |
| f_fd467bd2ae0c6d4f3bd2bc | seeded | Frederick, Sep 24: 24 publishers with what each got | Frederick owns | population |
| f_4b3ef3dcf76258a6fda5cd | seeded | May one-pager with paid-traffic numbers | Frederick owns | evidence (T8) |
| d_6fc54be60d1377e340a5b5 | seeded | Frederick's DD publishing folder | Frederick owns | write target (A3) |
| 0230b2df24ec829928fe1c55ad6185bf | seeded | Arthur, Sep 30, reply under the banker root: the first-look never hit the account | #executives member | overturning (T1) |
| 495d71a7e14dfaa68cac26fc4a6c4e03 | seeded | Robert, Sep 26, reply under the 70 % D1 root: Copperleaf's offer | #executives member | cohort (T4) |
| e44da6a468e7795a1b5853cfb0763aaf | seeded | Robert, Sep 29: Kestrel froze outside signings | #executives member | overturning (T3) |
| f55bd27436eb285a15d833648b922e9b | seeded | Leonard, Sep 26, reply under the Matthew root: the organic figure note | #bridge-pitch member | standing rule (T8) |
| e64606893af9f4316891a357ec26a691 | seeded | Arthur, Sep 26: a publisher's tech lead, notes on ENG-2362 | #analytics member | pointer (T5) |
| bda432db3ac81bf7f0c8903f0465ec9d | seeded | Frederick → Leonard, Sep 5: we still owe them an answer | DM member | evidence (T12) |
| lc_674982ffdca63f854ec6f591 | seeded | Arthur, Sep 26: Redwood's offer pasted on ENG-2362 | unscoped | cohort (T5) |
| 68dbfe80ef9c41b4f4fa8fe9 | seeded | Frederick, Sep 30: Sunfold commits 30,000 | unscoped | overturning (T7) |
| 68dabd6800e271eb0608d2d6 | seeded | Frederick, Sep 29: Marek says the money went out | unscoped | claim met first (T1) |
| evt_43fda04cd11b9d58a05161 | seeded | Sep 29 Tallwater call, note: advance is $40,000 now | Frederick's calendar | overturning (T2) |
| evt_d6905d9d5497d6a83a9a56 | seeded | Sep 26 Harbor Lane call, no change | Frederick's calendar | control |
| evt_48e63a8c7304cf9432fb46 | seeded | Sep 25 Wavecrest call, terms as sent | Frederick's calendar | control |
| evt_881d3e07c598b2205a7ff3 | seeded | Oct 6 execs event | Frederick's calendar | context |
| frederick.stone@harmonygames.co/<CA9raR_pqldShsvOhd5Uwxoj8zJh2-tzH0UJ5JLd@mail.gmail.com> | seeded | ESG partner, Sep 29: earliest signature Nov 14 | Frederick's mailbox | overturning (T9) |
| frederick.stone@harmonygames.co/<CAP16wHs998luhyUQ3U3Bw_EguUS8xoTcGPbTVkR@mail.gmail.com> | seeded | Leonard, Sep 30: Nov 14 is the signing date | Frederick's mailbox | overturning (T9) |
| 5373edb55ca853d6052ecce5 | seeded | Contacts: Anika Rao, Partnerships, Kestrel Group | unscoped | alias join (T3) |
| 1d6fd505d2fea08fa0f26c6e | seeded | Contacts: Lena Fischer, Sunfold Mobile | unscoped | skip (R10) |
| C07C2866011/1756140953.197759 | base | Leonard, Aug 25: keep code, IP and non-mobile rights | #executives member | authority H2 |
| f_26e1f9a86761e35049192a | base | Executives Biweekly Sync, Aug 28: the same sentence | shared with Frederick | authority H2 |
| D05S58U4SAK/1758736747.409459 | base | Sep 24: $0.50 D30 ARPI | DM member | input (R4) |
| frederick.stone@harmonygames.co/1830012626042968381 | base | Appodeal's last message, May 21, no terms | Frederick's mailbox | cohort: Waiting on us |
| frederick.stone@harmonygames.co/1842348778705877030 | base | Rayking's mail with Frederick's unsent draft | Frederick's mailbox | cohort: Waiting on us |
| snowflake.wh_analytics__monetization__revenue_daily | base | DD total_revenue_usd: {'2025-07': 2078.33, '2025-08': 721.55, '2025-09': 381.11} | unscoped | input (keep value) |
| frederick.stone@harmonygames.co/1842077918822838564 | seeded | Oakline Games thread: Live | Frederick's mailbox | evidence (cohort) |
| f_27cac0eed300cc33eeb4fd | seeded | Oakline Games term sheet: 30% of net to Harmony Games, $30,000 advance ($10,000 first-look payme | shared with Frederick | evidence (cohort terms) |
| frederick.stone@harmonygames.co/1842077918823428620 | seeded | Tallwater Games thread: Live | Frederick's mailbox | evidence (cohort) |
| f_e8cb875d5b7c8d9972d259 | seeded | Tallwater Games term sheet: 25% of net to Harmony Games, $60,000 advance net 30 from signature, 30 | shared with Frederick | evidence (cohort terms) |
| frederick.stone@harmonygames.co/1842077918823258769 | seeded | Sunfold Mobile thread: Live | Frederick's mailbox | evidence (cohort) |
| f_8ddfb9901891eb8e9dcab8 | seeded | Sunfold Mobile term sheet: 30% of net to Harmony Games, $20,000 advance net 45 from signature, 50 | shared with Frederick | evidence (cohort terms) |
| frederick.stone@harmonygames.co/1842077918823445589 | seeded | Harbor Lane Games thread: Live | Frederick's mailbox | evidence (cohort) |
| f_d72e8b34e7496f0de668bc | seeded | Harbor Lane Games term sheet: 20% of net to Harmony Games, $25,000 advance net 60 from signature, 25 | shared with Frederick | evidence (cohort terms) |
| frederick.stone@harmonygames.co/1842077918823344908 | seeded | Wavecrest Play thread: Live | Frederick's mailbox | evidence (cohort) |
| f_a6a5647f977d4638b2b8b1 | seeded | Wavecrest Play term sheet: 22% of net to Harmony Games, $15,000 advance net 60 from signature, 15 | shared with Frederick | evidence (cohort terms) |
| frederick.stone@harmonygames.co/1842077918822811962 | seeded | Moonrail Studios thread: Withdrawn | Frederick's mailbox | evidence (cohort) |
| f_464839da025a0a01f53979 | seeded | Moonrail Studios term sheet: 26% of net to Harmony Games, $30,000 advance net 30 from signature, 35 | shared with Frederick | evidence (cohort terms) |
| frederick.stone@harmonygames.co/1842077918822429064 | seeded | Northglow Publishing thread: Out on rights | Frederick's mailbox | evidence (cohort) |
| f_3eccf6e0bb63955dc51e27 | seeded | Northglow Publishing term sheet: 35% of net to Harmony Games, $50,000 advance net 30 from signature, 60 | shared with Frederick | evidence (cohort terms) |
| frederick.stone@harmonygames.co/1842077918823323729 | seeded | Pinegrove Games thread: Out on rights | Frederick's mailbox | evidence (cohort) |
| f_5f3ef4a4760d18e696a41a | seeded | Pinegrove Games term sheet: 30% of net to Harmony Games, $40,000 advance net 30 from signature, 45 | shared with Frederick | evidence (cohort terms) |
| frederick.stone@harmonygames.co/1842077918822912178 | seeded | Fernhollow Media thread: Passed | Frederick's mailbox | evidence (cohort) |
| frederick.stone@harmonygames.co/1842077918822894896 | seeded | Quietbay Games thread: Passed | Frederick's mailbox | evidence (cohort) |
| frederick.stone@harmonygames.co/1842077918823167383 | seeded | Slatewood Mobile thread: Passed | Frederick's mailbox | evidence (cohort) |
| frederick.stone@harmonygames.co/1842077918822812534 | seeded | Ironbridge Interactive thread: Passed | Frederick's mailbox | evidence (cohort) |
| frederick.stone@harmonygames.co/1842077918822727407 | seeded | Tidewell Studios thread: Passed | Frederick's mailbox | evidence (cohort) |
| frederick.stone@harmonygames.co/1842077918823060205 | seeded | Marlin Play thread: Passed | Frederick's mailbox | evidence (cohort) |
| frederick.stone@harmonygames.co/1842077918823167536 | seeded | Kitebridge Games thread: Waiting on us | Frederick's mailbox | evidence (cohort) |
| frederick.stone@harmonygames.co/1842077918822627795 | seeded | Orchard Lane Games thread: No reply | Frederick's mailbox | evidence (cohort) |
| frederick.stone@harmonygames.co/1842077918822746195 | seeded | Summit Mobile thread: No reply | Frederick's mailbox | evidence (cohort) |
| frederick.stone@harmonygames.co/1842077918822773098 | seeded | Silverlake Mobile thread: No reply | Frederick's mailbox | evidence (cohort) |
| frederick.stone@harmonygames.co/1842077918822506013 | seeded | Cedarbrook Play thread: No reply | Frederick's mailbox | evidence (cohort) |
| frederick.stone@harmonygames.co/1842077918822804025 | seeded | Foxglove Games thread: No reply | Frederick's mailbox | evidence (cohort) |
| frederick.stone@harmonygames.co/1842077918823170401 | seeded | Riverstone Interactive thread: No reply | Frederick's mailbox | evidence (cohort) |
| frederick.stone@harmonygames.co/1842077918822759281 | seeded | Bellwether Arcade thread: No reply | Frederick's mailbox | evidence (cohort) |

## Blind sweeps

Three fresh agents, in three passes, read the records with no design, solver or manifest, each told to read only through `tools/hg.py` and `tools/persona_view.py`, and each report is kept in `plan/sweep/`.

**Blind solve (`blind_fork_sweep.md`).** Its independent table matched the solver on every publisher and value: first pick Copperleaf, $67,200 and $32,000 in Q4, $0 banked, keep value $12,723.96, Live 7, Withdrawn 1, Out on rights 2, Passed 6, Waiting on us 3, No reply 7. It found five forks, none moving the first pick, its values or Banked. Each is settled by wording in a record:

| Fork | Fix | Record |
|---|---|---|
| F1 where the notes live | 'left in your Gmail drafts'; the card says the same for nudges | standing line, DD publishing card |
| F2 the Sep 24 lead | 'never made it onto your sheet' | hub |
| F3 'still Live' before the word existed | 'still has an offer in with us', and the line moves to Sep 26, after the four term sheets | standing line |
| F4 'before we sit down' had passed | 'before we go any further with them' | standing line |
| F5 reminders per offer or per date | 'One for each Live offer ... named for the publisher' | rule doc |

Its weakest settled call, Oakline's Q4 cash, is settled too: Arthur's reply now says the resend will land in October. Its realism notes led to per-publisher reply wording, term sheets laid out line by line, and distinct control-call notes. Accepted as designed: the offers sit where they do because that placement is the trap (Robert's relay, Arthur's ticket, the replies under older roots).

**Coherence sweep (`coherence_sweep.md`): 1 BLOCKER, 6 FIX, 14 NOTE.**

| Finding | Disposition |
|---|---|
| B1 Appodeal row said nothing was sent | fixed: 'we applied', 'Intake form (DAU, ARPDAU)'; status unchanged |
| F1 'Live' before the rule doc | fixed (above) |
| F2 'live in the US' after the global release | fixed: tranche 1 sends moved to May 5 and 6, before 18:50Z |
| F3 'founders' event includes Frederick | fixed: 'DD publishing: execs' |
| F4 British spelling from US writers | fixed: license, called |
| F5 word-for-word replies | fixed: every reply has its own wording |
| F6 sheet note against Tilting Point | fixed: 'approached about DD publishing' |
| N6, N7 unsupported Zombie Match claims | fixed: the co-dev doc says not DD; the rule doc drops the game name |
| N11 'Monday's talk' dated on a Monday; 3-day first-look | fixed: 'next Monday's'; 5 days |
| N12 sheet stamped before tranche 3 | fixed: modified 21:30Z |
| N1–N5, N8–N10, N13, N14 | no change: each reads as silence, fits the base, or is harmless |

It also confirmed each time claim (a16z Sep 30 01:37Z, the Turkish fund Sep 29 21:50Z, the sync position, the $0.50 note, the tranche, the lead, ENG-2362, the Oct 6 slot) and the three warehouse month sums. Not covered: GitHub and a Snowflake-wide name scan.

**Second blind pass on the fixed records (`blind_fork_sweep_2.md`).** Same first pick, values, Banked and status counts, and 0 genuine forks. Its one reading that could move the pick (ignoring phone changes because Live says 'in writing') is closed by 'calls included' in the rule doc. Its minor flags: fixed the card's 'named F/up with plus the publisher's name', added Frederick as a member of the DD publishing card, and marked Rayking's first contact 'Sep 4, 2025 (to me)'. Accepted: all eight term sheets share one layout.

## Platform /injection review of rev1

Attempt 6aed99b31c89eba1436ef322 (`injection-static-v2`, stored in `run_forensics/rev1/platform_injection_review.md`) reviewed rev1 (sha256 e6aa859bea5f, the SQL here byte for byte): FINAL VERDICT: PASS. Lint 0 FAIL, 0 CHECK, 0 INFO; Checks A, B and C PASS; no demonstrated defects. No advisory changes the SQL, because any SQL edit voids this PASS:
- Advisory 1 (slides_pages.notes, slides_page_elements.table_json and ordinal, linear_comments.sequence not in the unverified snapshot): kept. The same four columns loaded on the frederick_q4_commitments rev2 platform changelog.
- Advisory 2 (external term sheets with a parent in Frederick's private folder): kept as a simplification; check-sql shows each is shared with him (1.E). Whether a run finds them is checked at /prompt and the pre-check.
- Advisory 3 (publisher thread numbers decode to Sep 1): information only; thread ids have no listed contract.
- Advisory 4 (Robert's and Arthur's cited mail and Robert's call have no record of their own): deliberate, the offers are Slack-only and Linear-only; visibility is a /prompt question.
- Advisory 5 (Robert's and Arthur's invite copies say PDT): cosmetic, kept.

## Platform /prompt review of rev1 and the rev2 change

Attempt 6aed99b31c89eba1436ef322 (`run_forensics/rev1/platform_prompt_review.md`) reviewed prompt bed2b497fa1e on rev1: FINAL VERDICT: FAIL, Score 2. Unique Ground Truth 2 and Clarity 2 came from one fork; every other dimension scored 5, the dataset gate was distinct at 0.599, and Cross-Service Coherence was 5. The fork: the rule doc's last line said what Leonard had said about what goes out to publishers 'still applies', which could be read as a limit on content rather than as three notes owed in this job.
- Fixed in rev2: the last line of f_5e355d03f6eb6a4e866ead now says 'Fred, the notes I asked you for on what goes out to publishers still aren't done, so do those as part of this too.' The doc (Sep 29) follows the ask (f55bd27436eb285a15d833648b922e9b, Sep 26), and nothing else in Leonard's Slack with Frederick asks for notes to publishers (hg.py searches of D05S58U4SAK and C096HFA5Z8W), so the line has one referent. Recipients and wording stay in the Slack line.
- Also in rev2: the outreach sheet's note moved from a row under the table to a cell beside the header of f_fd467bd2ae0c6d4f3bd2bc. The platform reports counted it as a 25th sheet row and said 27 publishers, though their own lists name 26.
- Not taken (optional, no score effect): removing the four unsnapshotted columns, which loaded on the Q4 platform changelog; emptying the term sheets' parents_json, which would change where a run finds them.
- The prompt text doesn't change. Truth doesn't change in any field (oracle_kit regression against the rev1 SQL and truth). Rev2 needs /injection, then /prompt, then /hardness again.

## Platform follow-ups

- ○ carrier: the Tallwater note is on a calendar description (evt_43fda04cd11b9d58a05161), past 150 characters. L6 stays open: the Opus pre-check must show a run can read it with a full event read. Linear comment lc_674982ffdca63f854ec6f591 is ● (Ask_Carriers §6b).
- `trello_create_card` on the UA/BD board and the checklist writes on 68dab660c900179df4f5f92d are unproven until the pre-check.
- Warehouse revenue isn't compared cell by cell with the P&L: Frederick can't open those workbooks, so no deliverable rests on that comparison.
- The forecast's exact mode doesn't fail write-content slots; read its E[avg] as an upper view.
- No independent red team ran (REDTEAM_* unset; fallback recorded in the scenario design §13).

## Self-review

### Tool outputs (final SQL, verbatim)

`tools/sql_lint.py`:
```
schemas touched (10): contacts, gcal, gdocs, gdrive, gmail, gsheets, gslides, linear, slack, trello
rows by schema: {'gdrive': 13, 'gdocs': 10, 'gsheets': 2, 'gslides': 7, 'slack': 9, 'trello': 9, 'gmail': 114, 'gcal': 8, 'linear': 2, 'contacts': 2}  total rows: 176  ops: {'insert': 144, 'update': 32}
errors: 0  warnings: 8
  warn  line 319: gcal.gcal_events.start_ts = 2025-10-06T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 319: gcal.gcal_events.end_ts = 2025-10-06T18:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 321: gcal.gcal_events.start_ts = 2025-10-06T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 321: gcal.gcal_events.end_ts = 2025-10-06T18:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 323: gcal.gcal_events.start_ts = 2025-10-06T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 323: gcal.gcal_events.end_ts = 2025-10-06T18:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 325: gcal.gcal_events.start_ts = 2025-10-06T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 325: gcal.gcal_events.end_ts = 2025-10-06T18:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
```

sql_lint warning disposition (8 warnings, one class — on/after the clock): the four copies of the Oct 6 'DD publishing: execs' event carry future start and end plan fields, a not-yet-happened meeting created Sep 30; nothing after the seed bound is treated as completed.

`tools/base_check.py`:
```
BASE CHECK (/injection A + C, static): PASS  — 144 inserts, 32 updates
KB: bound (2025-10-01) — KB bound to the selected universe
Check A — records, references, IDs: PASS
Check C — dates and relationships: PASS
Warnings (2):
  line 315: gcal.gcal_events: meeting 30f44011dd4c930bf394e789ce5bbf20@hg4 'Harbor Lane call' has 1 attendee(s) but no invitation mail ('Invitation: Harbor Lane call @ …') in any attendee mailbox — INT-11 base: 836/941 meetings with attendees have one (2298/2974 attendee mailboxes); add the copies or declare integration_exceptions [{record_id, reason: 'no_notify: …'}]
  line 317: gcal.gcal_events: meeting 850b316226236edc02527182107f9227@hg4 'Wavecrest call' has 1 attendee(s) but no invitation mail ('Invitation: Wavecrest call @ …') in any attendee mailbox — INT-11 base: 836/941 meetings with attendees have one (2298/2974 attendee mailboxes); add the copies or declare integration_exceptions [{record_id, reason: 'no_notify: …'}]
  note: gsheets.sheets_sheets: no base-reference rules (checked by sql_lint only)
  note: gslides.slides_page_elements: no base-reference rules (checked by sql_lint only)
  note: gslides.slides_pages: no base-reference rules (checked by sql_lint only)
```

base_check (run with the final manifest): the INT-11 exceptions for the Harbor Lane and Wavecrest calls are declared notes (no_notify: Frederick organized both; the only other attendee is external). The note lines for gsheets and gslides say those tables have no base-reference rules; sql_lint covers them.

`tools/base_claims.py`:
```
BASE CLAIMS (injected text vs base git + #builds): PASS · 0 branch mentions · 0 fail · 0 warn · 0 date-only
branch windows:
```

`tools/hardness_gate.py` (final manifest + SQL):
```
HARDNESS GATE (extreme): PASS
  [ok] assignment_context: manifest bound to current V3 assignment, freeze and policy
  [ok] effective_profile: effective_profile 'extreme' for 'Long Horizon' → thresholds 'extreme'
  [ok] sql_lint_clean: 0 lint error(s) — run tools/sql_lint.py
  [ok] base_consistency: /injection-style checks vs the base universe: A 0 finding(s), C 0 finding(s), 0 warning(s) — run tools/base_check.py --manifest
  [ok] persona_reach: 34 load-bearing seeded ids for frederick_stone (8 in unscoped services = visible, 26 judged by persona_view check-sql); not provably visible: none
  [ok] fact_consistency: fact_check: 0 error(s) (11 declared facts), 2 drift warning(s); first: none — run tools/fact_check.py --manifest --no-leak
  [ok] hazard_scope: 0 pre-existing hazard(s) among task-touched records; state/lifecycle or referential without a verified resolution: none
  [ok] services_injected: 10 schemas injected (contacts, gcal, gdocs, gdrive, gmail, gsheets, gslides, linear, slack, trello); need ≥ 10
  [ok] rows: 144 INSERTed rows (UPDATE companions not counted; 176 rows in all); need ≥ 120
  [ok] services_carrying_weight: 11 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: schemas injected but absent from the design: none
  [ok] seeded_ids_exist_in_sql: 54 seeded ids cited; missing from SQL: none
  [ok] anchors: 3 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 15 fragments; need ≥ 12
  [ok] ask_fragment_services: 11 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 15 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 13 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 26; need ≥ 24 (source-defined: True) (requester-confirmed cohort_exception)
  [ok] evidence_surfaces: 5 surfaces over 5 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 69; need ≥ 60
  [ok] call_budget: unconditional (verified) floor 203 of 203 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 180 (requester-confirmed volume_exception)
  [ok] call_budget_spread: 10 services in budget; largest share outside the per-record phase 41% (≤ 50%)
  [ok] traps: 21 traps across 11 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 8 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 4 supersessions (4 with versions in ≥ 2 services, 1 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: 4 trap(s) with version_records; the records' own timestamps (SQL created_at/ts/date/updated_at, or the base record) must be strictly increasing in the listed order (oldest first); bad: none
  [ok] distractors: 7 distractors of 7 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 10 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 8 chains with 8 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] mechanism_portfolio: 8 portfolio entries, each a mechanism-enum id with trap/chain nodes, a requirement, a natural-reading fallback and a prior family with its reason
  [ok] artifact_fields: declared ['gradable_surface', 'solver']: paths relative, digests sha256
  [ok] hidden_authorities: 3 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 2 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 14 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 13 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 8 writes over 5 services; each must depend on findings
  [note] volume_exception: call-budget floor 180 and per-record floor 60 replace 500 and 300; every other extreme target applies except the cohort floor below — reason: 26 publishers and 10 sets of terms; mail and calendars are bulk-readable, so hon; requester confirmation: task author in chat on 2026-11-06: 'my task is a long horizon task soo i want ov
  [note] cohort_exception: cohort floor 24 replaces 40; surfaces, surface services, why_no_bulk and short_circuit still apply — reason: no natural 40-record publisher cohort exists; padding it would add always-pass r; requester confirmation: task author in chat on 2026-11-06: 'my task is a long horizon task soo i want ov
```

`tools/hg.py lint` (the eval's hg_injection_lint, base data): counts {'FAIL': 0, 'CHECK': 0, 'INFO': 0, 'by_check': {}}. LINT: no CHECK flag to disposition; no INFO.

### Preflight (S4b–S5e)

```
SOLVER CONTRACT: PASS · solver.py sha 92f94f353626 · sql f6eb3512dffa · 8 rules
  [PASS] contract.interface: 8 rules, each with mechanism, requirement and natural_reading; optional: ['touched', 'deciding', 'DEGRADES']
  [PASS] contract.deterministic: two fresh solves (forward and reverse key order) give identical output (28 keys, sha c269faa81692), and so do fresh processes with PYTHONHASHSEED 1 and 2
  [PASS] contract.regression: previous truth truth.json: solver at revision ? reproduces it byte for byte; current rules (None) on the previous SQL: 0 field difference(s)
  [PASS] contract.rules_nodes: 8 rules vs 8 portfolio entries: one-to-one
  [PASS] contract.slots: 32 direct/aggregate slots read a solver value; 40 write-content/delivery slots are graded from the writes, not the solver
  [PASS] contract.controls: DONE: 1 control(s); done_over moves ['Tallwater Games']; CORR: 1 control(s); corr_over moves ['Harbor Lane Games']; ALIAS: 1 control(s); alias_over moves ['Wavecrest Play']; FILT: 2 control(s); filt_over moves ['Homa']; EXC: 1 control(s); exc_over moves ['Sunfold Mobile']; INPUT: 1 control(s); input_over moves ['Oakline Games']; DATE: 1 control(s); date_over moves ['Sunfold Mobile']; FOLLOW: 1 control(s); follow_over moves ['Oakline Games']; channel CH-DONE (scale): ch_done moves 1 of 1 member(s); channel CH-CORR (scale): ch_corr moves 1 of 1 member(s); channel CH-ALIAS (scale): ch_alias moves 1 of 1 member(s); channel CH-FILT1 (scale): ch_filt1 moves 1 of 1 member(s); channel CH-FILT2 (scale): ch_filt2 moves 1 of 1 member(s); channel CH-EXC (scale): ch_exc moves 2 of 2 member(s); channel CH-INPUT (scale): ch_input moves 1 of 1 member(s); channel CH-DATE (scale): ch_date moves 2 of 2 member(s); channel CH-FOLLOW (scale): ch_follow moves 3 of 3 member(s); channel CH-SLIP (scale): fails surface slots ['S_live_PA', 'S_live_PG', 'S_passed_1', 'S_silent_1', 'V12_Harbor']
  [PASS] contract.golden: 12 golden values checked against their deciding records (12 sampled keys x 5 fields): 12 identifier values found, 0 short tokens found, 0 presence-type; 48 unverified e.g. ['Copperleaf Games/Advance: no evidence ids', 'Copperleaf Games/Monthly installs: no evidence ids']
  [PASS] contract.digest: manifest solver Working_Files/solver/solver.py digest 92f94f353626 vs file 92f94f353626
```

```
MUTATION · rev2 · sql f6eb3512dffa · deterministic design diagnostics from the solver; on the Season Pass backtests these are development fixtures, not validation
  key-locality: PASS on 49 of 49 configurations checked
  rule:DONE                          WEAK       flipped   5 flips only aggregate or weight-1 slots: ['VQ_Oakline']
  rule:CORR                          KILLED     flipped  13 flips direct slot(s) of weight >= 3: ['A_adv_PB']
  rule:ALIAS                         KILLED     flipped   5 flips direct slot(s) of weight >= 3: ['S_out_PC']
  rule:FILT                          KILLED     flipped  26 flips direct slot(s) of weight >= 3: ['S_in_PH', 'S_in_PI', 'A_adv_PH'
  rule:EXC                           KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['S_out_PD', 'S_out_PJ']
  rule:INPUT                         KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['A_com_PE']
  rule:DATE                          WEAK       flipped  10 flips only aggregate or weight-1 slots: ['VQ_Harbor', 'VQ_Wavecrest']
  rule:FOLLOW                        WEAK       flipped   0 changes what an aggregate reads (class or group membership) and the ag
  degrade:done_over                  WEAK       flipped   3 flips only aggregate or weight-1 slots: ['VQ_Tallwater']
  degrade:corr_over                  SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:alias_over                 KILLED     flipped  11 flips direct slot(s) of weight >= 3: ['S_live_PG']
  degrade:filt_over                  WEAK       flipped   0 changes what an aggregate reads (class or group membership) and the ag
  degrade:exc_over                   KILLED     flipped  13 flips direct slot(s) of weight >= 3: ['A_com_PE']
  degrade:input_over                 WEAK       flipped   3 flips only aggregate or weight-1 slots: ['V12_Oakline']
  degrade:date_over                  WEAK       flipped   3 flips only aggregate or weight-1 slots: ['VQ_Sunfold']
  degrade:follow_over                WEAK       flipped   0 changes what an aggregate reads (class or group membership) and the ag
  degrade:ch_done                    WEAK       flipped   5 flips only aggregate or weight-1 slots: ['VQ_Oakline']
  degrade:ch_corr                    KILLED     flipped  13 flips direct slot(s) of weight >= 3: ['A_adv_PB']
  degrade:ch_alias                   KILLED     flipped   5 flips direct slot(s) of weight >= 3: ['S_out_PC']
  degrade:ch_filt1                   KILLED     flipped  13 flips direct slot(s) of weight >= 3: ['S_in_PH', 'A_adv_PH']
  degrade:ch_filt2                   KILLED     flipped  13 flips direct slot(s) of weight >= 3: ['S_in_PI', 'A_adv_PI']
  degrade:ch_exc                     KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['S_out_PD', 'S_out_PJ']
  degrade:ch_input                   KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['A_com_PE']
  degrade:ch_date                    WEAK       flipped  10 flips only aggregate or weight-1 slots: ['VQ_Harbor', 'VQ_Wavecrest']
  degrade:ch_follow                  WEAK       flipped   0 changes what an aggregate reads (class or group membership) and the ag
  shards (consecutive slices of 14 records, 2 batches): 8 mutants {'WEAK': 3, 'KILLED': 5}
  intervention:rule:DONE             load-bearing    
  intervention:rule:CORR             no-injected-records
  intervention:rule:ALIAS            load-bearing    
  intervention:rule:FILT             load-bearing    
  intervention:rule:EXC              load-bearing    
  intervention:rule:INPUT            load-bearing    
  intervention:rule:DATE             load-bearing    
  intervention:rule:FOLLOW           load-bearing    
  intervention:degrade:done_over     no-injected-records
  intervention:degrade:corr_over     no-injected-records
  intervention:degrade:alias_over    no-injected-records
  intervention:degrade:filt_over     no-injected-records
  intervention:degrade:exc_over      no-injected-records
  intervention:degrade:input_over    no-injected-records
  intervention:degrade:date_over     no-injected-records
  intervention:degrade:follow_over   no-injected-records
  intervention:degrade:ch_done       no-injected-records
  intervention:degrade:ch_corr       no-injected-records
  intervention:degrade:ch_alias      no-injected-records
  intervention:degrade:ch_filt1      no-injected-records
  intervention:degrade:ch_filt2      no-injected-records
  intervention:degrade:ch_exc        no-injected-records
  intervention:degrade:ch_input      no-injected-records
  intervention:degrade:ch_date       no-injected-records
  intervention:degrade:ch_follow     no-injected-records
  geometry: U = 0.6405 (155/242) · L_max = 0.3264 over ['rule:DONE', 'rule:CORR', 'rule:ALIAS', 'rule:FILT', 'rule:EXC', 'rule:INPUT', 'rule:DATE']
    V3 cap 0.85: U PASS (needs > 0.15) · L_max OK
  dispositions: 50/50 recorded; missing: none
```

```
MUTATION · rev2 · sql f6eb3512dffa · deterministic design diagnostics from the solver; on the Season Pass backtests these are development fixtures, not validation
  key-locality: PASS on 49 of 49 configurations checked
  geometry: U = 0.6405 (155/242) · L_max = 0.3264 over ['rule:DONE', 'rule:CORR', 'rule:ALIAS', 'rule:FILT', 'rule:EXC', 'rule:INPUT', 'rule:DATE']
    V3 cap 0.85: U PASS (needs > 0.15) · L_max OK
```

```
TRAP LIVENESS · ADVISORY · UNCALIBRATED · lexical warnings, not proof · on the Season Pass backtests these are development fixtures, not validation
  hub frederick.stone@harmonygames.co/<CAY2swo8Vt78l2VvRPI7Ywn-45Te8GyWBcazV7hy@mail.gmail.com> · direct delegations 3 · rule placement: A15 nodes only: ['C5', 'C8', 'T14', 'T6', 'T8'] (mechanism_portfolio); every other node SKIP
  T1   done_gap           -  [rule placement SKIP: not an A15 node]
  T2   superseding        -  [rule placement SKIP: not an A15 node]
  T3   scope_alias        -  [rule placement SKIP: not an A15 node]
  T4   exact_predicate    -  [rule placement SKIP: not an A15 node]
  T5   exact_predicate    -  [rule placement SKIP: not an A15 node]
  T6   authority          -
  T7   superseding        -  [rule placement SKIP: not an A15 node]
  T8   synthesis_omission -
  T9   effective_date     -  [rule placement SKIP: not an A15 node]
  T10  reuse_exclusion    -  [rule placement SKIP: not an A15 node]
  T11  near_miss_mention  -  [rule placement SKIP: not an A15 node]
  T12  tool_surface       -  [rule placement SKIP: not an A15 node]
  T13  superseding        -  [rule placement SKIP: not an A15 node]
  T14  authority          -
  T15  distractor         -  [rule placement SKIP: not an A15 node]
  T16  distractor         -  [rule placement SKIP: not an A15 node]
  T17  distractor         -  [rule placement SKIP: not an A15 node]
  T18  distractor         -  [rule placement SKIP: not an A15 node]
  T19  distractor         -  [rule placement SKIP: not an A15 node]
  T20  distractor         -  [rule placement SKIP: not an A15 node]
  T21  distractor         breadcrumb  [rule placement SKIP: not an A15 node]
  dispositions: 0/1 recorded
```

Mutation dispositions (`01c_Dispositions.json`, 50 of 50): rules CORR, ALIAS, FILT, EXC and INPUT are KILLED and live; DONE, DATE and FOLLOW are WEAK in the tool's terms but live, since their slots are aggregates or write-content slots it can't read. Over-application operators: alias_over and exc_over are KILLED; done_over, filt_over, input_over, date_over and follow_over are weak-accepted control trials; corr_over SURVIVED and is weak-accepted because Harbor Lane's Advance has no slot, and adding one would add an always-pass row. Channel operators are live. Interventions: seven rules are load-bearing; CORR's `no-injected-records` is a tool limit on gcal row ids, checked by hand (without the event row the solver gives Tallwater 60000, 60000, 60000); the 17 operator interventions have no single row by design.

Geometry: see the block above; U is above 1 − 0.85 for the Medium cap and key-locality passes, so U is exact. L_max is advisory. Liveness: one flag (T21 breadcrumb), weak-accepted in `01c_Dispositions.json`: the hub's delegation to the ground rules is the fairness link, and T21 is the co-dev decoy.

Forecast: see `01c_Forecast.json` and the pasted `plan/forecast_injection.txt` lines below. It's UNCALIBRATED. For rev2 FOLLOW's rate falls from 0.50 to 0.35, because the rule doc now says the notes are owed. Exact mode never fails a write-content slot, so its E[avg] is an upper view. The scenario's design-mode forecast `hev_49facf6ed134c068` counts those consequences: E[avg] 0.62–0.65, P(all) 0.476–0.680. The requester's targets (over 130 calls in every run, average under 80 %) can only be checked on the Opus pre-check.

```
  independent whole    V3 E[avg] 0.768 [0.736, 0.802] P(all) 0.002
  independent shard:32 V3 E[avg] 0.768 [0.736, 0.801] P(all) 0.001
  independent shard:14 V3 E[avg] 0.768 [0.736, 0.801] P(all) 0.001
  independent slip     V3 E[avg] 0.794 [0.763, 0.826] P(all) 0.000
  independent batches  V3 E[avg] 0.768 [0.736, 0.801] P(all) 0.002
  source      whole    V3 E[avg] 0.768 [0.736, 0.802] P(all) 0.002
  source      shard:32 V3 E[avg] 0.768 [0.736, 0.801] P(all) 0.001
  source      shard:14 V3 E[avg] 0.768 [0.736, 0.801] P(all) 0.001
  source      slip     V3 E[avg] 0.794 [0.763, 0.826] P(all) 0.000
  source      batches  V3 E[avg] 0.768 [0.736, 0.801] P(all) 0.002
  correlated  whole    V3 E[avg] 0.768 [0.716, 0.822] P(all) 0.218
  correlated  shard:32 V3 E[avg] 0.768 [0.717, 0.820] P(all) 0.214
  correlated  shard:14 V3 E[avg] 0.768 [0.717, 0.820] P(all) 0.214
  correlated  slip     V3 E[avg] 0.795 [0.752, 0.838] P(all) 0.040
  correlated  batches  V3 E[avg] 0.768 [0.716, 0.822] P(all) 0.215
  V3: P(all four difficulty gates) 0.000-0.218 across scenarios; value of information (first scenario): ['rule:DONE', 'rule:CORR', 'rule:ALIAS']
  ledger: forecast record {'id': 'hev_ee095ca0efd8cddb', 'added': True, 'present': False, 'rejected': none}
```

`tools/preflight_report.py --forecast 01c_Forecast.json`:
```
PREFLIGHT: PASS · blocking {'solver_contract': True, 'surface_validation': True, 'mutation_dispositions': True, 'geometry_upper_bound': True} · advisory {'geometry_margin': {'V3': 'OK'}, 'geometry_bound_verdict': {'V3': 'PASS'}, 'liveness_dispositions_missing': none, 'forecast': 'recorded'}
wrote Task_Authoring/task_inputs/Working_Files/01c_Preflight_Report.json and Task_Authoring/task_inputs/Working_Files/01c_Preflight_Report.md
```

### Changes made at this stage (and why)

- Gradable surface: text-selector slots moved from aggregate or direct to `write_content` (a text selector can't read a solver value), and the scenario gate was re-sealed. No slot id or weight changed.
- Scenario builder: writes only when run as a script, so the solver and SQL builder can import it without touching certified files.
- Solver contract: each channel has its own operator, because Tallwater, Harbor Lane and Wavecrest each sit on two channels. Moonrail is in FOLLOW's touched set, because a missed Kestrel join makes it owed a note.
- Manifest: `design_delta` lists the row ids, controls and channels, and the K1, K3 and T13 record pointers. Harbor Lane and Wavecrest calls are declared `no_notify` in `integration_exceptions`.
- Records changed after the blind sweeps: see Blind sweeps. The solver's truth didn't change in any field.

### /injection Checks A–C walk

- Inventory: 144 INSERT, 32 UPDATE, 0 DELETE, no upserts; tables {'contacts.contacts': 2, 'gcal.gcal_events': 8, 'gdocs.docs_documents': 10, 'gdrive.drive_files': 13, 'gmail.gmail_messages': 57, 'gmail.gmail_threads': 57, 'gsheets.sheets_sheets': 1, 'gsheets.sheets_spreadsheets': 1, 'gslides.slides_page_elements': 4, 'gslides.slides_pages': 2, 'gslides.slides_presentations': 1, 'linear.linear_comments': 1, 'linear.linear_issues': 1, 'slack.slack_messages': 9, 'trello.trello_actions': 5, 'trello.trello_boards': 1, 'trello.trello_cards': 3}. PASS.
- Check A (references and IDs): every channel, user, issue, thread, calendar, board, list and folder resolves (base_check Check A PASS); in_reply_to and references point at earlier seeded messages; every minted id has 0 base hits (1.F); owners and shares are roster addresses or the publisher's own address. PASS.
- Check B (structure): sql_lint 0 errors; every *_json column is literal JSON; NOT NULL columns supplied; generated columns never written; camelCase Trello columns quoted. PASS.
- Check C (dates, parents, statuses, counts): all seeded timestamps ≤ 2025-10-01T00:00Z except the Oct 6 event's plan fields; replies after their parents; root counters match; statuses unchanged. PASS.

### Touched-data census

See 'Touched-data census and coherence hazards' above: six hazard categories covered, each with cited hazards or 'none in scope', and the cards SC-1, SC-3, SC-5, SC-6, SC-9, SC-10, SC-17, SC-33, SC-34, SC-35, SC-39, SC-49, SC-54, SC-63, SC-73 dispositioned.

### Counter-readings

| Category | Counter-reading (strongest argument it FAILS) | Evidence that resolves it | Verdict |
|---|---|---|---|
| Temporal | the hub (Sep 30 23:10Z) says a16z didn't happen, but the rejection letter is dated Oct 1 | Slack C07C2866011/1759196253.935149, Sep 30 01:37Z: 'That means that we didn't get in'; the Oct 1 letter is 'expected rejection'. The hub cites the Sep 30 news, not the letter | PASS |
| Temporal | the rule doc's line about the notes could point at something posted after it | f55bd27436eb285a15d833648b922e9b is Sep 26 19:30Z, before the doc (Sep 29 16:00Z) | PASS |
| Temporal | the May mails say live in the US after the global release | the sends now run May 5 to May 6 17:50Z, before C05KNDCHAAG/1746557417.594259 (May 6 18:50Z), following the Biz Dev Notes template f_0d17fc08eddaf231cf7f28 | PASS (fixed) |
| Temporal | the Oct 6 event is after the clock | evt_881d3e07c598b2205a7ff3 is a plan field created Sep 30; nothing after the bound is treated as done | PASS |
| Semantic / Category | 'the four of us' and a 'founders' event clash with the base's founders sync, which leaves Frederick out | the event is now 'DD publishing: execs' (evt_881d3e07c598b2205a7ff3), matching evt_189fe218303982c1d78e99; no row grades founder status (SC-49) | PASS (fixed) |
| Semantic / Category | the co-dev doc could read as ground rules for DD | f_21203dbcdf780cc07c76cb says co-dev talks only, not DD; the hub names the ground rules doc | PASS |
| Semantic / Category | the outreach sheet says Appodeal came to us, though Frederick applied | f_fd467bd2ae0c6d4f3bd2bc now says 'we applied' and 'Intake form (DAU, ARPDAU)', matching frederick.stone@harmonygames.co/1830012626042968381 | PASS (fixed) |
| Cross-service Referential | the sheet note says unlisted Partners-doc names weren't approached, but Tilting Point got a UA form | it now says 'approached about DD publishing' (f_fd467bd2ae0c6d4f3bd2bc); the rule doc scopes the form out; frederick.stone@harmonygames.co/1842443183462721250 | PASS (fixed) |
| Cross-service Referential | Anika's Contacts row says Kestrel Group and her thread says Moonrail | the signature in frederick.stone@harmonygames.co/1842077918822811962 says 'Moonrail Studios, a Kestrel Group studio'; contact 5373edb55ca853d6052ecce5 | PASS |
| Cross-service Referential | Arthur's #analytics pointer says a tech lead at a publisher without naming one | e64606893af9f4316891a357ec26a691 names ENG-2362, whose comment lc_674982ffdca63f854ec6f591 names Mei Tanaka of Redwood Arcade | PASS |
| Quantitative | Oakline's Q4 cash could be $20,000 if the resend isn't counted | 0230b2df24ec829928fe1c55ad6185bf now says it'll land in October; the rule doc counts what lands Oct 1 to Dec 31 | PASS (fixed) |
| Quantitative | the keep value's months could disagree with another table | the rule doc names one table; REVENUE_DAILY and its V2 agree (Q09); three independent reads gave 2,078.33, 721.55 and 381.11 | PASS |
| Quantitative | reply counters on the three roots could disagree with the export (Q01) | the UPDATE rows set 5/2, 9/1 and 3/3 with latest_reply equal to the seeded ts; the coherence sweep re-read each root | PASS |
| State / Lifecycle | Marek's 'sent' and Arthur's 'never hit' are two live statuses | intended: 0230b2df24ec829928fe1c55ad6185bf is a dated human report that follows frederick.stone@harmonygames.co/<CAybuYiHDdC_1wq0wp32aITdzH-XuQAf6p028lBn@mail.gmail.com> and explains the bounce; the rule doc defines Banked | PASS |
| State / Lifecycle | Tallwater's sheet and the call note are two live advances | the note on evt_43fda04cd11b9d58a05161 says 'not the number in the term sheet'; the rule doc says use the latest terms | PASS |
| State / Lifecycle | Sunfold's sheet and the comment are two live commitments | 68dbfe80ef9c41b4f4fa8fe9 says 'not the 50,000 in the term sheet' | PASS |
| State / Lifecycle | Moonrail's sheet still looks open | e44da6a468e7795a1b5853cfb0763aaf says whatever they had on the table is off; the join is the signature and 5373edb55ca853d6052ecce5 | PASS |
| State / Lifecycle | Oct 31 and Nov 14 are two live dates | the rule doc defers to the lawyers; frederick.stone@harmonygames.co/<CAP16wHs998luhyUQ3U3Bw_EguUS8xoTcGPbTVkR@mail.gmail.com> says 'not Oct 31' | PASS |
| State / Lifecycle | Northglow and Pinegrove are simply the best offers | the rule doc's status order puts Out on rights above Live; C07C2866011/1756140953.197759 | PASS |
| State / Lifecycle | the organic figure and the board note's paid numbers are two live inputs | the rule doc fixes $0.50 from D05S58U4SAK/1758736747.409459; frederick.stone@harmonygames.co/1830890312657338682 predates it | PASS |
| State / Lifecycle | Frederick's Sep 4 message to Rayking reads as sent | it carries the Drafts label in frederick.stone@harmonygames.co/1842348778705877030; bda432db3ac81bf7f0c8903f0465ec9d says we still owe them an answer | PASS |
| State / Lifecycle | Summit answered | the only message back in frederick.stone@harmonygames.co/1842077918822746195 is from noreply@ with an automatic-reply subject; the rule doc excludes it | PASS |
| Identifier / Format | seeded mail uses frederick.stone@ while base files use the frederick@ alias (I03) | all seeded rows use the roster address, and base thread rows carry the same address inside the file | PASS |
| Other | the corrections read as silent system fields | each overturning record is authored, dated and worded as a human report (Arthur, Robert, Frederick, ESG, Leonard) | PASS |
| Other | publisher replies read as templates | every reply is now its own wording; the coherence sweep's F5 and the blind sweep's note drove this | PASS (fixed) |
| People status | a rule rests on someone who has left | Leonard, Robert, Arthur and Frederick are active at the clock (activity.json); the rule rests on no roster fact | PASS |

People status: everyone a rule depends on is active at the clock (Leonard, Robert, Arthur, Frederick per activity.json; ESG Law is external); no Snowflake roster or Confluence headcount line is used.

Unresolved: no independent red-team review (fallback recorded); channel landing rates are analogs from completed Frederick tasks (UNCALIBRATED); the calendar-description route and writes on the UA/BD board await the pre-check.

```
STAGE GATE injection: PASS — Task_Authoring/task_inputs · 01_Universe_Inject.sql#f6eb3512dffa · 01_Hardness_Manifest.json#550c4fbf3aad · 01_Grounding_Dossier.md#9c0a597a75ac · solver/solver.py#92f94f353626 · 01c_Dispositions.json#c3c88b75e591 · 01c_Preflight_Report.json#85aeea3b5432 · 00_Assigments.md#b715c1dcdbe1 · 01_Scenario_Design.md#e6f4b48f11e9 · 01_Hardness_Manifest.draft.json#70c5ac3229a5 · 01_Gradable_Surface.json#7e68f34657e8 · __context__#ec895c36b5f1 · __assignment__#a95625679300 · __policy__#dc4ab5df3cdd · __gate_policy__#f8638415ca2c · __review__#938b3fc22f77 · blocking 0 · warnings 0 · checks 40
[PASS] assignment.v3_context: Frederick Stone / Co-founder; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 6 output(s) present: 01_Universe_Inject.sql, 01_Hardness_Manifest.json, 01_Grounding_Dossier.md, solver/solver.py, 01c_Dispositions.json, 01c_Preflight_Report.json
[PASS] structure.inputs: 4 input(s) present: 00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json)
[PASS] chain.scenario: upstream 'scenario' PASS pasted and current (01_Scenario_Design.md#e6f4b48f11e9, 01_Hardness_Manifest.draft.json#70c5ac3229a5, 01_Gradable_Surface.json#7e68f34657e8, 00_Assigments.md#b715c1dcdbe1, __context__#ec895c36b5f1, __assignment__#a95625679300, __policy__#dc4ab5df3cdd, __gate_policy__#f8638415ca2c, __review__#d0a6485ae7d0)
[PASS] structure.sections: 17 required sections present and non-empty (01_Grounding_Dossier.md)
[PASS] structure.placeholders: no placeholders in 01_Grounding_Dossier.md
[PASS] evidence.entity: 32/33 items carry a source pointer (min 90%); unsourced e.g. L35: 'Redwood Arcade | Redwood Arcade · Mei Tanaka | lc_674982ffdca63f854ec6f591 | AGREE (new en'
[PASS] evidence.keyword: 33/33 items carry a source pointer (min 100%)
[PASS] evidence.persona_reach: 9/9 items carry a source pointer (min 100%)
[PASS] evidence.record_ledger: 176/176 items carry a source pointer (min 100%)
[PASS] evidence.facts_for_human: 60/60 items carry a source pointer (min 100%)
[PASS] tool.sql_lint: sql_lint re-run matches the paste: errors 0, warnings 8, rows 176
[PASS] tool.injection_lint: hg.py lint: 0 FAIL, 0 CHECK dispositioned, 0 INFO; sha256 f6eb3512dffa matches 01_Universe_Inject.sql
[PASS] review.warning_dispositions: every sql_lint warning class dispositioned (clock×8)
[PASS] tool.base_check: base_check pasted PASS; re-run PASS
[PASS] tool.base_claims: base_claims pasted PASS; re-run PASS
[PASS] tool.hardness_gate: hardness_gate (SQL) pasted PASS; re-run PASS
[PASS] structure.design_delta: final manifest keeps all 63 draft ids
[PASS] structure.preflight: 01c_Preflight_Report.json bound by sha256 to the current SQL, solver, surface, manifest and dispositions
[PASS] solver.contract: solver contract re-run PASS
[PASS] mutation.dispositions: 50 mutation and intervention results each carry a written disposition (01c_Dispositions.json)
[PASS] geometry.upper_bound: U 0.640 (155/242) vs 1 - cap 0.15 (V3 medium): PASS (bound PASS); re-run U 0.640 PASS (bound PASS)
[PASS] geometry.margin: L_max 0.32644628099173556 vs (1 - cap) + 0.10: OK (advisory: the margin is a judgment, not a proof)
[PASS] liveness.dispositions: every liveness flag dispositioned (1 flag(s))
[PASS] forecast.preregistered: forecast hev_ee095ca0efd8cddb pre-registered in the ledger (UNCALIBRATED)
[PASS] tool.check_sql_pasted: persona_view check-sql --load-bearing output pasted with verdict PASS
[PASS] reach.injection: 59 scoped load-bearing ids YES for frederick_stone
[PASS] structure.facts_declared: manifest declares 11 load-bearing fact(s) in `facts`
[PASS] tool.fact_check: fact_check --no-leak pasted PASS; re-run PASS
[PASS] kb.coherence_hazards: coherence audit cites 13 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 4 seeded speakers each cited with activity.json status; conventions.json cited
[PASS] kb.integrations: companions listed per integrations.json (7 INT ids, services ['contacts', 'gcal', 'gdocs', 'gdrive', 'gmail', 'gsheets', 'gslides', 'linear', 'slack', 'trello'])
[PASS] boundary.anchor_naming: 6 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 25 evidenced counter-readings (of 27 found; need ≥ 16) in 01_Grounding_Dossier.md
[PASS] review.coverage: self-review addresses all 9 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

