# Grounding Dossier — fs-account-custody (injection rev 4) · contains no prompt, Oracle Event or criterion text

Persona Frederick Stone <frederick.stone@harmonygames.co> (Co-founder, Executive) · horizon Normal Horizon · effective_profile `normal`
(no exception) · universe date 2025-10-01 (clock 2025-10-01T00:00:00Z, `tools/hg_clock.py`; V3 freeze = Tue Sep 30, 2025 5:00 PM PT) ·
difficulty mode Medium (author target: average under 75%). Generator: `support/task_work/fs_account_custody/` (`mint_ids.py` ids,
`planned_text.json` seeded wording, `build_sql.py` → `task_inputs/01_Universe_Inject.sql`, `build_final_manifest.py` →
`Working_Files/01_Hardness_Manifest.json`). Every value below cites a record id, a service file + JSON pointer, or an SQL line.

## 1.A Structural

| Table (live schema `references/universe_schema_live.json`) | NOT NULL supplied | Base location + pointer · count | 3 base sample ids | Timestamp format · export → column |
|---|---|---|---|---|
| slack.slack_messages | id ts channel_id type text reply_count reply_users_count is_activity_message reactions_json files_json attachments_json created_at metadata_json | slack/messages/D05S58U4SAK/2025-09.json, slack/messages/C07C2866011/2025-09.json · 687,230 records (1.F scan) | D05S58U4SAK/1759170013.491159 · C07C2866011/1759186080.203099 · C07UCC631A6/1757349668.681539 | ts 10.6 digits; created_at ISO-Z with micro; id = sha256('channel\|ts')[:32]; thread_ts → thread_ts_legacy |
| gmail.gmail_threads / gmail_messages | id thread_id user_email | HarmonyGames_Gmail/Services_Data/gmail/threads/*.json · 88,726 thread files | frederick.stone@harmonygames.co/1843428112007517388 · frederick.stone@harmonygames.co/1835153849970828373 · frederick.stone@harmonygames.co/1822440391549486206 | date ISO-Z, internal_date ms = date; labelIds → label_ids_json; Arthur's Message-ID shape `<CAOOpSq6…@mail.gmail.com>` (frederick.stone@harmonygames.co/1822440391549486206) |
| gdrive.drive_files | id name mime_type | gdrive/data.json /drive_files · 53,866 | d_63fffeb4fab5233ed5bb73 · d_175c0d7bc72ed244b944cb · d_cc3e90160f490686039986 | modified/created ISO-Z; shared_with_emails → shared_with_emails_json; owners → owners_json; parents → parents_json; folders d_ + 22 hex |
| gsheets.sheets_spreadsheets / sheets_sheets | spreadsheet_id title / spreadsheet_id sheet_id title | gsheets/data.json · 398 spreadsheets, 1,553 tabs | f_00c30de5acd0cf7656c140 · f_00e7008444923e0fe1549c · f_0272f7ef3096043049e9f6 | grid_json 2-D array; sheet_id = index 0..N-1; same id + sharing as the drive row |
| gdocs.docs_documents | document_id title | gdocs/data.json · 633 | f_1be142fdb7a3bfe62f534b · f_1a147d85c1cbe0c319af5c · f_00117462881159eceee63e | drive_file_id = document_id; style_runs inside body_text; revision_id 10 hex |
| trello.trello_cards / trello_actions | id name idBoard idList / id type date | trello/data.json /cards · 803, /actions · 5,294 (56 commentCard) | 67cf1b506d78ad3c72e02a35 · 670010236b89198587ca45b6 · 68c5a49e8491a9d7faf869d0 | ids: first 8 hex = Unix seconds; badges → badges_json; data → data_json; Harmony Games board 640643a3fd8f3ca308d9318e, idShort max 455, list To Do 640643a3fd8f3ca308d93195 |
| confluence.confluence_pages / page_versions | id space_id title body body_format status version created_at updated_at / id page_id number title body created_at | confluence/confluence_working.json /pages · 31, /page_versions · 78 | page_company_home · page_team_onboarding · page_ops_home | varchar ISO-Z; version 1 row per new page (ver_ + 32 hex); space_COMPANY home page_company_home |

Snowflake is read, not injected: `snowflake.json /tables/35` (ANALYTICS.MONETIZATION.AD_REVENUE; row shape `{date, game_id, platform,
country, network, placement, impressions, revenue_usd, accrued_vs_paid}`, /tables/35/rows/0). Re-aggregated in this stage over the raw
export: 2025-09 admob paid 1,163 rows $38.70; applovin paid 1,761 rows $136.33; meta_audience paid 998 rows $26.15 (2025-08: admob 1,546
rows $64.87). GCal, Slides, Contacts, Linear and GitHub carry no task record.

## 1.B Entity table

| Entity | Canonical spelling / id | Services (cited) | Value per service | Agreement |
|---|---|---|---|---|
| Leonard Hayes | leonard.hayes@harmonygames.co · EMPLOYEE_0038_SLACK_ID · PERSON_6094_TRELLO_USER_ID · user_EMPLOYEE_0038 | slack D05S58U4SAK/1759096868.688389; confluence page_company_home author | CEO / co-founder; YouTube manager, TikTok via Fred's login | AGREE |
| Frederick Stone (persona) | frederick.stone@harmonygames.co · EMPLOYEE_0008_SLACK_ID · Drive root d_175c0d7bc72ed244b944cb | slack D05S58U4SAK/1759170013.491159; gmail frederick.stone@harmonygames.co/1841453218828344296 | UA / marketing co-founder; holder on the marketing accounts | AGREE |
| Arthur Blake | arthur.blake@harmonygames.co · EMPLOYEE_0025_SLACK_ID · Trello 2162c1ba310341bf318f48b7 · Drive root d_cc3e90160f490686039986 | slack C07C2866011/1759252761.127709; gmail frederick.stone@harmonygames.co/1822440391549486206 | co-founder / tech; author of the sweep and the rules | AGREE (no base Trello action by him: counter-reading in Self-review) |
| Robert | robert@harmonygames.co · EMPLOYEE_0016_SLACK_ID | slack C07C2866011/1759264062.753039 | co-founder; Discord admin (C07C2866011/1734154451.509769) | AGREE |
| Node Media LLC | agency, Slack PERSON_0498_SLACK_ID; staff address [EMAIL_126620] | slack C04UEQVDVB7 (2025-01 shard, "Node Media"); C08MCEP1B9B/1727063903.359939; D05S58U4SAK/1734719973.099339 (terminated 2024-12-20); trello 670010236b89198587ca45b6 | partner on Meta (seed f_f7e7c5bf089029cee91175 Partners); unlinked on Google Ads and removed on YouTube 2024-12-20 (seeds) | AGREE |
| Google Ads — Harmony Games, Inc. | 569-350-5790 ("[SOURCE_ORG_0001], Inc." in the masked export) | gmail frederick.stone@harmonygames.co/1835153849970828373; seed f_ab70b02c329d038a72fb9f; seed frederick.stone@harmonygames.co/1844732985606656293 | company account, mail since 2024-09-22 | AGREE (masking hazard X04) |
| Google Ads — Calm Play LLC | 449-481-1590, "Ads funded by Calmplay LLC" | gmail frederick.stone@harmonygames.co/1838369017520543217; frederick.stone@harmonygames.co/1846207913166171315 (canceled Oct 16, after the clock) | ZM3D account, mail since 2024-01-10 (robert@ threads/00002504.json); Leonard and Arthur Admin 2024-01-20, Fred 2024-09-05 | AGREE (T07 excluded) |
| AdMob — active account | pub-3556282811018998 (Leonard's new account; slack C73E02AA3A22/1745467232.203529, gmail leonard@harmonygames.co_1830467552498804662.json) | slack D05S58U4SAK/1756147086.813789 ("It's active and a working account"); gmail frederick.stone@harmonygames.co/1841453218828344296 (Fred admitted Aug 25); seed f_50ff132ac88169019feeca | Leonard owner, Fred admin | AGREE |
| AdMob — deactivated | pub-2341961509332343 | gmail frederick.stone@harmonygames.co/1841349862518331350 (deactivated Aug 24); seed f_4521c272960dd1836a5196 (March sheet) | not in the sweep | DISAGREE (designed, T15) |
| Unity org | Harmony Games Inc, org 20067043314233 | slack C07C2866011/1759078905.131549 (Leonard's Sep 28 campaign link in this org); C07C2866011/1759186080.203099 (iOS budget Sep 29); gmail leonard@harmonygames.co_1844375476012340343.json (prepayment receipt 2025-09-27, Harmony Games Inc); blake@harmonygames.co_1843681663885543164.json (Arthur gets the org's Unity Pro renewal) | Arthur, Robert, Leonard Owner; Fred Manager (seed f_1191b7f8c96419e1f4dc88, filtered to Owners and Managers) | AGREE |
| TikTok | @harmonygames (64 followers), tied to frederick.stone@harmonygames.co | slack D05S58U4SAK/1759160336.370489, D05S58U4SAK/1759170013.491159; D05S58U4SAK/1759155793.573669 (new account on SVC_0009_EMAIL) | recovered Sep 29; second account deleted (seed f_2f0abe2f1f6726fef63f80) | AGREE |
| Adjoe | SVC_2836_EMAIL; channel C07UCC631A6 | slack C07UCC631A6/1757349668.681539 (waiver); gmail frederick.stone@harmonygames.co/1844773822453719122 (Oct 1 invoice disputed, after the clock) | campaign on Sep 1, paused Sep 8 | AGREE |

## 1.C Voice and realism (speakers, activity, conventions)

| Seeded speaker | activity.json status_at_clock | 3 base messages (quoted) | Length / hours (conventions.json) | Seeded text |
|---|---|---|---|---|
| Leonard Hayes leonard.hayes@harmonygames.co (EMPLOYEE_0038_SLACK_ID) | activity: active_sep_2025 | "YouTube says I'm a manager and not the owner and the owner had to do it" (D05S58U4SAK/1759096868.688389); "I turned off the FB campaign" (D05S58U4SAK/1758922541.613439); "we have 2 months left before letting everyone go" (C07C2866011/1758739409.488879) | `slack.per_person_hours_and_style` p50 47 / p90 133, all-lower 0.31, UTC core 15–02 | claim 120 chars 23:05Z; 90-day remark 82 chars 18:43Z; hub 432 chars 22:40Z (the hub is the one long message, as in the base DM D05S58U4SAK/1734719973.099339) |
| Arthur Blake arthur.blake@harmonygames.co (EMPLOYEE_0025_SLACK_ID; Trello 2162c1ba310341bf318f48b7; Gmail sender) | activity: active_sep_2025 | "<!here> don't forget to update zoom. its a zoom meeting" (C07C2866011/1759252761.127709); "Hi [PERSON_NAME_11887], Ok we purchased the enhanced support. Let me know if There are any other steps I need to take." (frederick.stone@harmonygames.co/1810124385239504078); Arthur's Jan 27 mail with a PDF and no body (frederick.stone@harmonygames.co/1822440391549486206) | p50 40 / p90 121, all-lower 0.33, UTC core 15–01; `gmail.internal_subject_len_chars` p50 42 (seeded subject 48) | #executives summary 117 chars 21:10Z; card desc 1,223 chars, numbered (`trello.desc_len` p90 626, p99 2,437); comment 196 chars; email 300 chars 23:21Z |
| Frederick Stone frederick.stone@harmonygames.co | activity: active_sep_2025 | "I reduced Unity bids to $6 and set daily cap at $300 ($150 per campaign)." (C07C2866011/1757957294.669109); "Requested Live Stream Access." (D05S58U4SAK/1759156059.073379); "I think it's recovered." (D05S58U4SAK/1759162506.056959) | p50 73 / p90 183 | no seeded speech; owner of the March logins sheet f_4521c272960dd1836a5196 |

Seeded speakers: Leonard Hayes (active_sep_2025), Arthur Blake (active_sep_2025); Frederick Stone (active_sep_2025) owns one seeded
file. Platform export rows are data, not speech. Trello card prose follows `trello.desc_len` (numbered short lines); Slack DM style
lowercase without sign-off (Leonard's base DM messages D05S58U4SAK/1759093632.123689, D05S58U4SAK/1759102981.352539).

## 1.D Keyword / findability (base hit counts via `tools/hg.py search search <svc> <term> --limit 200`)

| Term | Service | Base hits + pointer | Seeded records / note |
|---|---|---|---|
| "handover rules" | trello | 0 base hit(s) (scan_complete) | NEW TERM — introduced in trello 68dc406c7b0d03e53b334bab + 68dc42f3095ad95194a711ae, reached via A1 D05S58U4SAK/1759272012.507134 |
| "handover rules" | slack | 0 base hit(s) (scan_complete) | NEW TERM — introduced in slack D05S58U4SAK/1759272012.507134 (hub) |
| "handover rules" | gmail | 0 base hit(s) (scan_complete) | NEW TERM — introduced in gmail frederick.stone@harmonygames.co/1844732985606656293, reached via A1 → K2 (card title = subject) |
| "handover" | confluence | 0 base hit(s) (scan_complete) | NEW TERM — none seeded in Confluence; page_company_accounts_access is reached by the card's "Company Accounts & Access page on Confluence" |
| "Company Accounts" | confluence | 0 base hit(s) (scan_complete) | NEW TERM — introduced in confluence page_company_accounts_access, reached via trello 68dc406c7b0d03e53b334bab |
| "Admin sweep" | gdrive | 0 base hit(s) (scan_complete) | NEW TERM — introduced in gdrive d_6cae3483dd469c189a528e, reached via A1 ("arthur's sweep from today") and C07C2866011/1759266627.118342 |
| "sweep" | slack | 118 base hit(s) (scan_complete), first files.json /21836/name | slack C07C2866011/1759266627.118342, D05S58U4SAK/1759272012.507134 (the newest) |
| "Company Ops" | gdrive | 0 base hit(s) (scan_complete) | NEW TERM — introduced in gdrive d_21f9e11d43739eaef26b38, reached via A1 |
| "money still moving" | gdocs | 0 base hit(s) (scan_complete) | NEW TERM — introduced in gdocs f_c612c0e68a27b3330eb46a, reached via trello 68dc406c7b0d03e53b334bab rule 5 |
| "money moving" | slack | 0 base hit(s) (scan_complete) | NEW TERM — only in trello 68dc406c7b0d03e53b334bab and gdocs f_c612c0e68a27b3330eb46a |
| "for the cuts" | slack | 2 base hit(s) (scan_complete), first messages/C050C9EPYKW/2024-05.json /140/text | slack C07C2866011/1758739436.208417 (decoy, newest) |
| "for the cuts" | gdocs | 0 base hit(s) (scan_complete) | NEW TERM — introduced in gdocs f_c612c0e68a27b3330eb46a heading "Money still moving (for the cuts)" |
| "logins" | gdrive | 0 base hit(s) (scan_complete) | NEW TERM — introduced in gdrive f_4521c272960dd1836a5196 "Marketing & UA logins" (decoy T4) |
| "Node Media" | slack | 43 base hit(s) (scan_complete), first messages/C04UEQVDVB7/2025-01.json /1/text | gsheets f_f7e7c5bf089029cee91175 Partners tab (the only seeded outside party) |
| "Node" | trello | 57 base hit(s) (scan_complete), first data.json /cards/372/name | trello 670010236b89198587ca45b6 (base) |
| "Lock up social handles" | trello | 5 base hit(s) (scan_complete), first data.json /cards/671/name | trello 67cf1b506d78ad3c72e02a35 (base, W4 target); named by trello 68dc406c7b0d03e53b334bab rule 7 |
| "admin on meta" | slack | 0 base hit(s) (scan_complete) | NEW TERM — introduced in slack D05S58U4SAK/1759187141.318207 (claim T1) |
| "admob" | gmail | 200 base hit(s) (scan incomplete — proves nothing), first threads/00000412.json /messages/0/body | the deactivation mail frederick.stone@harmonygames.co/1841349862518331350 and the Aug 25 invite frederick.stone@harmonygames.co/1841453218828344296 |

## 1.E Persona reach (scoped records)

| Record | Service | Visibility path | Load-bearing |
|---|---|---|---|
| D05S58U4SAK/1759272012.507134 | slack | im D05S58U4SAK member (EMPLOYEE_0008_SLACK_ID) | LB |
| D05S58U4SAK/1759187141.318207 | slack | im D05S58U4SAK member | LB |
| C07C2866011/1759266627.118342 | slack | private #executives member | LB |
| C07C2866011/1758739436.208417 | slack | private #executives member | LB |
| D05S58U4SAK/1759096868.688389 | slack | im member (base) | LB |
| D05S58U4SAK/1759170013.491159 | slack | im member (base) | LB |
| D05S58U4SAK/1758922541.613439 | slack | im member (base) | LB |
| D05S58U4SAK/1756147086.813789 | slack | im member (base) | LB |
| C07C2866011/1759186080.203099 | slack | #executives member (base) | LB |
| C07C2866011/1759264050.305069 | slack | #executives member (base) | LB |
| C07UCC631A6/1757346020.196019 | slack | adjoe channel member (base) | LB |
| C07UCC631A6/1757347560.891949 | slack | adjoe channel member (base thread reply) | LB |
| C07UCC631A6/1757349668.681539 | slack | adjoe channel member (base thread reply) | LB |
| frederick.stone@harmonygames.co/1844732985606656293 | gmail | own mailbox (INBOX copy) | LB |
| frederick.stone@harmonygames.co/1843428112007517388 | gmail | own mailbox (base) | LB |
| frederick.stone@harmonygames.co/1843223812315546201 | gmail | own mailbox (base) | LB |
| frederick.stone@harmonygames.co/1835153849970828373 | gmail | own mailbox (base) | LB |
| frederick.stone@harmonygames.co/1838369017520543217 | gmail | own mailbox (base) | LB |
| d_6cae3483dd469c189a528e | gdrive | shared with the persona (reader) | LB |
| d_21f9e11d43739eaef26b38 | gdrive | shared with the persona (writer) | LB |
| f_c612c0e68a27b3330eb46a | gdocs | shared with the persona (reader) | LB |
| f_4521c272960dd1836a5196 | gsheets | owned by the persona | LB |
| f_f7e7c5bf089029cee91175 | gsheets | shared (reader) | LB |
| f_ab70b02c329d038a72fb9f | gsheets | shared (reader) | LB |
| f_63b42f52fa11d7df238a4e | gsheets | shared (reader) | LB |
| f_1191b7f8c96419e1f4dc88 | gsheets | shared (reader) | LB |
| f_3996bca752549d3512bfbc | gsheets | shared (reader) | LB |
| f_a552317a929102385c0393 | gsheets | shared (reader) | LB |
| f_50ff132ac88169019feeca | gsheets | shared (reader) | LB |
| f_2f0abe2f1f6726fef63f80 | gsheets | shared (reader) | LB |
| f_fc27672c5bfea8b760b074 | gsheets | shared (reader) | LB |
| f_b89c1c70489f81031bdd4f | gsheets | shared (reader) | LB |
| f_99d66f33c54338e70f5ed2 | gsheets | shared (reader) | LB |
| f_215ff8da73e4173f78515c | gsheets | shared (reader) | LB |
| f_2cecf2f81045ec401feb61 | gsheets | shared (reader) | LB |
| f_5f2f52786dcd8e1168cd40 | gsheets | shared (reader) | LB |
| f_ad393ed61590f2d22c6cd7 | gsheets | shared (reader) | LB |
| f_b463693cd3779d4d25374f | gsheets | shared (reader) | LB |

Unscoped (always visible): trello 68dc406c7b0d03e53b334bab, 68dc42f3095ad95194a711ae, 68dc529406d8087e5a6b8403, 67cf1b506d78ad3c72e02a35,
670010236b89198587ca45b6; confluence page_company_accounts_access; snowflake.json /tables/35. The Cc and sender copies of the
Google Ads email sit in Leonard's and Arthur's mailboxes (ledger rows 11–12); they are not the persona's and not load-bearing
(check-sql NO, expected).

`python3 Task_Authoring/tools/persona_view.py check-sql frederick_stone Task_Authoring/task_inputs/01_Universe_Inject.sql --load-bearing support/task_work/fs_account_custody/out/lb.txt`:

```
CHECK-SQL as frederick_stone <frederick.stone@harmonygames.co>
[YES LB] L2 gdrive.drive_files insert d_6cae3483dd469c189a528e - file is shared with the persona (shared_with_emails)
[YES LB] L7 gdrive.drive_files insert f_f7e7c5bf089029cee91175 - file is shared with the persona (shared_with_emails)
[YES LB] L9 gsheets.sheets_spreadsheets insert f_f7e7c5bf089029cee91175 - file is shared with the persona (shared_with_emails)
[YES LB] L11 gsheets.sheets_sheets insert f_f7e7c5bf089029cee91175, f_f7e7c5bf089029cee91175#0 - file is shared with the persona (shared_with_emails)
[YES LB] L13 gsheets.sheets_sheets insert f_f7e7c5bf089029cee91175, f_f7e7c5bf089029cee91175#1 - file is shared with the persona (shared_with_emails)
[YES LB] L15 gdrive.drive_files insert f_ab70b02c329d038a72fb9f - file is shared with the persona (shared_with_emails)
[YES LB] L17 gsheets.sheets_spreadsheets insert f_ab70b02c329d038a72fb9f - file is shared with the persona (shared_with_emails)
[YES LB] L19 gsheets.sheets_sheets insert f_ab70b02c329d038a72fb9f, f_ab70b02c329d038a72fb9f#0 - file is shared with the persona (shared_with_emails)
[YES LB] L21 gsheets.sheets_sheets insert f_ab70b02c329d038a72fb9f, f_ab70b02c329d038a72fb9f#1 - file is shared with the persona (shared_with_emails)
[YES LB] L23 gdrive.drive_files insert f_63b42f52fa11d7df238a4e - file is shared with the persona (shared_with_emails)
[YES LB] L25 gsheets.sheets_spreadsheets insert f_63b42f52fa11d7df238a4e - file is shared with the persona (shared_with_emails)
[YES LB] L27 gsheets.sheets_sheets insert f_63b42f52fa11d7df238a4e, f_63b42f52fa11d7df238a4e#0 - file is shared with the persona (shared_with_emails)
[YES LB] L29 gsheets.sheets_sheets insert f_63b42f52fa11d7df238a4e, f_63b42f52fa11d7df238a4e#1 - file is shared with the persona (shared_with_emails)
[YES LB] L31 gdrive.drive_files insert f_1191b7f8c96419e1f4dc88 - file is shared with the persona (shared_with_emails)
[YES LB] L33 gsheets.sheets_spreadsheets insert f_1191b7f8c96419e1f4dc88 - file is shared with the persona (shared_with_emails)
[YES LB] L35 gsheets.sheets_sheets insert f_1191b7f8c96419e1f4dc88, f_1191b7f8c96419e1f4dc88#0 - file is shared with the persona (shared_with_emails)
[YES LB] L37 gdrive.drive_files insert f_3996bca752549d3512bfbc - file is shared with the persona (shared_with_emails)
[YES LB] L39 gsheets.sheets_spreadsheets insert f_3996bca752549d3512bfbc - file is shared with the persona (shared_with_emails)
[YES LB] L41 gsheets.sheets_sheets insert f_3996bca752549d3512bfbc, f_3996bca752549d3512bfbc#0 - file is shared with the persona (shared_with_emails)
[YES LB] L43 gdrive.drive_files insert f_a552317a929102385c0393 - file is shared with the persona (shared_with_emails)
[YES LB] L45 gsheets.sheets_spreadsheets insert f_a552317a929102385c0393 - file is shared with the persona (shared_with_emails)
[YES LB] L47 gsheets.sheets_sheets insert f_a552317a929102385c0393, f_a552317a929102385c0393#0 - file is shared with the persona (shared_with_emails)
[YES LB] L49 gdrive.drive_files insert f_50ff132ac88169019feeca - file is shared with the persona (shared_with_emails)
[YES LB] L51 gsheets.sheets_spreadsheets insert f_50ff132ac88169019feeca - file is shared with the persona (shared_with_emails)
[YES LB] L53 gsheets.sheets_sheets insert f_50ff132ac88169019feeca, f_50ff132ac88169019feeca#0 - file is shared with the persona (shared_with_emails)
[YES LB] L55 gdrive.drive_files insert f_2f0abe2f1f6726fef63f80 - file is shared with the persona (shared_with_emails)
[YES LB] L57 gsheets.sheets_spreadsheets insert f_2f0abe2f1f6726fef63f80 - file is shared with the persona (shared_with_emails)
[YES LB] L59 gsheets.sheets_sheets insert f_2f0abe2f1f6726fef63f80, f_2f0abe2f1f6726fef63f80#0 - file is shared with the persona (shared_with_emails)
[YES LB] L61 gdrive.drive_files insert f_fc27672c5bfea8b760b074 - file is shared with the persona (shared_with_emails)
[YES LB] L63 gsheets.sheets_spreadsheets insert f_fc27672c5bfea8b760b074 - file is shared with the persona (shared_with_emails)
[YES LB] L65 gsheets.sheets_sheets insert f_fc27672c5bfea8b760b074, f_fc27672c5bfea8b760b074#0 - file is shared with the persona (shared_with_emails)
[YES LB] L67 gsheets.sheets_sheets insert f_fc27672c5bfea8b760b074, f_fc27672c5bfea8b760b074#1 - file is shared with the persona (shared_with_emails)
[YES LB] L69 gdrive.drive_files insert f_b89c1c70489f81031bdd4f - file is shared with the persona (shared_with_emails)
[YES LB] L71 gsheets.sheets_spreadsheets insert f_b89c1c70489f81031bdd4f - file is shared with the persona (shared_with_emails)
[YES LB] L73 gsheets.sheets_sheets insert f_b89c1c70489f81031bdd4f, f_b89c1c70489f81031bdd4f#0 - file is shared with the persona (shared_with_emails)
[YES LB] L75 gdrive.drive_files insert f_99d66f33c54338e70f5ed2 - file is shared with the persona (shared_with_emails)
[YES LB] L77 gsheets.sheets_spreadsheets insert f_99d66f33c54338e70f5ed2 - file is shared with the persona (shared_with_emails)
[YES LB] L79 gsheets.sheets_sheets insert f_99d66f33c54338e70f5ed2, f_99d66f33c54338e70f5ed2#0 - file is shared with the persona (shared_with_emails)
[YES LB] L81 gdrive.drive_files insert f_215ff8da73e4173f78515c - file is shared with the persona (shared_with_emails)
[YES LB] L83 gsheets.sheets_spreadsheets insert f_215ff8da73e4173f78515c - file is shared with the persona (shared_with_emails)
[YES LB] L85 gsheets.sheets_sheets insert f_215ff8da73e4173f78515c, f_215ff8da73e4173f78515c#0 - file is shared with the persona (shared_with_emails)
[YES LB] L87 gdrive.drive_files insert f_2cecf2f81045ec401feb61 - file is shared with the persona (shared_with_emails)
[YES LB] L89 gsheets.sheets_spreadsheets insert f_2cecf2f81045ec401feb61 - file is shared with the persona (shared_with_emails)
[YES LB] L91 gsheets.sheets_sheets insert f_2cecf2f81045ec401feb61, f_2cecf2f81045ec401feb61#0 - file is shared with the persona (shared_with_emails)
[YES LB] L93 gdrive.drive_files insert f_5f2f52786dcd8e1168cd40 - file is shared with the persona (shared_with_emails)
[YES LB] L95 gsheets.sheets_spreadsheets insert f_5f2f52786dcd8e1168cd40 - file is shared with the persona (shared_with_emails)
[YES LB] L97 gsheets.sheets_sheets insert f_5f2f52786dcd8e1168cd40, f_5f2f52786dcd8e1168cd40#0 - file is shared with the persona (shared_with_emails)
[YES LB] L99 gdrive.drive_files insert f_ad393ed61590f2d22c6cd7 - file is shared with the persona (shared_with_emails)
[YES LB] L101 gsheets.sheets_spreadsheets insert f_ad393ed61590f2d22c6cd7 - file is shared with the persona (shared_with_emails)
[YES LB] L103 gsheets.sheets_sheets insert f_ad393ed61590f2d22c6cd7, f_ad393ed61590f2d22c6cd7#0 - file is shared with the persona (shared_with_emails)
[YES LB] L105 gdrive.drive_files insert f_b463693cd3779d4d25374f - file is shared with the persona (shared_with_emails)
[YES LB] L107 gsheets.sheets_spreadsheets insert f_b463693cd3779d4d25374f - file is shared with the persona (shared_with_emails)
[YES LB] L109 gsheets.sheets_sheets insert f_b463693cd3779d4d25374f, f_b463693cd3779d4d25374f#0 - file is shared with the persona (shared_with_emails)
[YES LB] L111 gdrive.drive_files insert f_4521c272960dd1836a5196 - persona owns the file
[YES LB] L113 gsheets.sheets_spreadsheets insert f_4521c272960dd1836a5196 - persona owns the file
[YES LB] L115 gsheets.sheets_sheets insert f_4521c272960dd1836a5196, f_4521c272960dd1836a5196#0 - persona owns the file
[YES LB] L117 gdrive.drive_files insert f_c612c0e68a27b3330eb46a - file is shared with the persona (shared_with_emails)
[YES LB] L119 gdocs.docs_documents insert f_c612c0e68a27b3330eb46a - file is shared with the persona (shared_with_emails)
[YES LB] L121 gdrive.drive_files insert d_21f9e11d43739eaef26b38 - file is shared with the persona (shared_with_emails)
[YES LB] L123 slack.slack_messages insert cc5882ebce53a9ddd2635b31d837e746, C07C2866011/1758739436.208417 - persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES LB] L125 slack.slack_messages insert d18954e94e8b9caa935704bd676ccffe, D05S58U4SAK/1759187141.318207 - persona EMPLOYEE_0008_SLACK_ID is in members of im D05S58U4SAK
[YES LB] L127 slack.slack_messages insert 1ecb6ef5fa9552cc9fbd4c60f4672909, C07C2866011/1759266627.118342 - persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES LB] L129 slack.slack_messages insert 02847a3cc740c9b657d75f26c3750854, D05S58U4SAK/1759272012.507134 - persona EMPLOYEE_0008_SLACK_ID is in members of im D05S58U4SAK
[YES LB] L141 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844732985606656293 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L143 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAOOpSq6NYC_rzIOrbQLSZpivEB6VyNfx48bLl8VjW0@mail.gmail.co - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L151 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1844732985606651242 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L153 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAOOpSq6NYC_rzIOrbQLSZpivEB6VyNfx48bLl8VjW0@mail.gmail.com> - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L161 gmail.gmail_threads insert arthur.blake@harmonygames.co/1844732985606780348 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L163 gmail.gmail_messages insert arthur.blake@harmonygames.co/<CAOOpSq6NYC_rzIOrbQLSZpivEB6VyNfx48bLl8VjW0@mail.gmail.com>, - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] base slack C07C2866011/1759186080.203099 - base record: message inherits channel: persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES LB] base slack C07C2866011/1759264050.305069 - base record: message inherits channel: persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES LB] base slack C07UCC631A6/1757346020.196019 - base record: message inherits channel: persona EMPLOYEE_0008_SLACK_ID is in members of private adjoe-[SOURCE_ORG_0001]
[YES LB] base slack C07UCC631A6/1757347560.891949 - base record: thread reply inherits channel: persona EMPLOYEE_0008_SLACK_ID is in members of private adjoe-[SOURCE_ORG_0001]
[YES LB] base slack C07UCC631A6/1757349668.681539 - base record: thread reply inherits channel: persona EMPLOYEE_0008_SLACK_ID is in members of private adjoe-[SOURCE_ORG_0001]
[YES LB] base slack D05S58U4SAK/1756147086.813789 - base record: message inherits channel: persona EMPLOYEE_0008_SLACK_ID is in members of im D05S58U4SAK
[YES LB] base slack D05S58U4SAK/1758922541.613439 - base record: message inherits channel: persona EMPLOYEE_0008_SLACK_ID is in members of im D05S58U4SAK
[YES LB] base slack D05S58U4SAK/1759096868.688389 - base record: message inherits channel: persona EMPLOYEE_0008_SLACK_ID is in members of im D05S58U4SAK
[YES LB] base slack D05S58U4SAK/1759170013.491159 - base record: message inherits channel: persona EMPLOYEE_0008_SLACK_ID is in members of im D05S58U4SAK
[YES LB] base gmail frederick.stone@harmonygames.co/1835153849970828373 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1838369017520543217 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1843223812315546201 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1843428112007517388 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co

summary: {'YES': 65, 'NO': 4}  unscoped rows (always visible): 7
  gdocs.docs_documents: {'YES': 1}
  gdrive.drive_files: {'YES': 20}
  gmail.gmail_messages: {'YES': 1, 'NO': 2}
  gmail.gmail_threads: {'YES': 1, 'NO': 2}
  gsheets.sheets_sheets: {'YES': 21}
  gsheets.sheets_spreadsheets: {'YES': 17}
  slack.slack_messages: {'YES': 4}
verdict: PASS (0 load-bearing rows not visible)
```

## 1.F Collision checks

Identity tokens first: the only new body-text token is [EMAIL_912045] (Frederick's personal Google account on the Instagram export):
0 hits across HarmonyGames_Other_Services, HarmonyGames_Gmail and HarmonyGames_GitHub (`grep -rlF`). No new header token is minted;
[EMAIL_126620] is the base token Node gave for access (C08MCEP1B9B/1727689480.986899) and SVC_0009_EMAIL the base group inbox
(D05S58U4SAK/1759155793.573669). New literal values 645-364-1205 (Node MCC, as in the base Google Ads link notices),
@harmonygames.app and the Message-ID stem CAOOpSq6NYC_rzIOrbQLSZ: 0 hits each in the same sweep.

Minted record ids (`hg.py search lookup <svc> --ids-file <json> --file <collection> --pointer <array>`; service, ids, scan_complete,
records checked, hits):

```
gdrive /drive_files                      20 ids  scan_complete True  records 53866  hits 0
trello /cards                             5 ids  scan_complete True  records 803    hits 0
trello /actions                           5 ids  scan_complete True  records 5294   hits 0
trello /checklists                        5 ids  scan_complete True  records 54     hits 0
confluence /pages                         2 ids  scan_complete True  records 31     hits 0
confluence /page_versions                 2 ids  scan_complete True  records 78     hits 0
slack messages/*/*.json (id + ts)         8 ids  scan_complete True  records 687230 hits 0
gmail thread files (3 numeric ids)        0 filename hits over 88,726 files; Message-ID stem 0 hits
```

Sheets and Docs rows reuse their Drive ids (checked under gdrive). Slack (channel, ts): no base message at D05S58U4SAK 1759187141.318207 /
1759272012.507134 or C07C2866011 1759266627.118342 / 1758739436.208417 (read of the 2025-09 shards). Trello idShort 456/457 unused (board max 455).
`base_check.py` Check A re-tests uniqueness against the full collections (PASS, §Self-review).

## 2 Record ledger

| # | Service | Table | Record id | Manifest element | Carrier | Reach path | Discovery role |
|---|---|---|---|---|---|---|---|
| 1 | slack | slack.slack_messages | D05S58U4SAK/1759272012.507134 | A1 hub; K1 K2 K6 K7 | ● | im member | first link (anchor) |
| 2 | slack | slack.slack_messages | D05S58U4SAK/1759187141.318207 | T1 (claim) | ● | im member | claim met first |
| 3 | slack | slack.slack_messages | C07C2866011/1759266627.118342 | T14 (wrong summary); C1 hop 1 | ● | #executives member | claim met first |
| 4 | slack | slack.slack_messages | C07C2866011/1758739436.208417 | H2 decoy; T3 v1 | ● | #executives member | decoy |
| 5 | trello | trello.trello_cards | 68dc406c7b0d03e53b334bab | H1 authority; K2 K5 K8 delegations; C3 C5 hop 1 | ● desc | unscoped | authority |
| 6 | trello | trello.trello_actions | 68dc406ceb6d064fd62b364f | createCard companion of 68dc406c7b0d03e53b334bab; T2 v2 | — | unscoped | companion |
| 7 | trello | trello.trello_cards | 68dc42f3095ad95194a711ae | H1 decoy (team scope); T5 | ● desc | unscoped | decoy |
| 8 | trello | trello.trello_actions | 68dc42f343eb3d733ec11459 | createCard companion of 68dc42f3095ad95194a711ae | — | unscoped | companion |
| 9 | trello | trello.trello_actions | 68dc529406d8087e5a6b8403 | K3 amendment; T2 v3 | ● commentCard | unscoped | overturning evidence |
| 10 | gmail | gmail.gmail_threads + gmail_messages | frederick.stone@harmonygames.co/1844732985606656293 | K4 amendment; C3 hop 2; T2 v4 | ● body | own mailbox | overturning evidence |
| 11 | gmail | gmail.gmail_threads + gmail_messages | leonard.hayes@harmonygames.co/1844732985606651242 | K4 Cc copy | ● | Leonard's mailbox | companion |
| 12 | gmail | gmail.gmail_threads + gmail_messages | arthur.blake@harmonygames.co/1844732985606780348 | K4 sender copy (SENT) | ● | Arthur's mailbox | companion |
| 13 | gdrive | gdrive.drive_files | d_6cae3483dd469c189a528e | K6 cohort container; C4 hop 2 | ● metadata | shared reader | evidence |
| 14 | gsheets | sheets_spreadsheets + sheets_sheets (People, Partners) | f_f7e7c5bf089029cee91175 | cohort Meta; T9; T1 v2 | ● grid | shared reader | per-record evidence |
| 15 | gsheets | sheets (Access, Linked managers) | f_ab70b02c329d038a72fb9f | cohort Google Ads 569; C3 hop 3; T8 | ● grid | shared reader | per-record evidence |
| 16 | gsheets | sheets (Access, Linked managers) | f_63b42f52fa11d7df238a4e | cohort Google Ads 449; T8; T1 | ● grid | shared reader | per-record evidence |
| 17 | gsheets | sheets (Members) | f_1191b7f8c96419e1f4dc88 | cohort Unity; T1 v2 | ● grid | shared reader | per-record evidence |
| 18 | gsheets | sheets (Users) | f_3996bca752549d3512bfbc | cohort AppLovin | ● grid | shared reader | per-record evidence |
| 19 | gsheets | sheets (Users) | f_a552317a929102385c0393 | cohort adjoe; C2 | ● grid | shared reader | per-record evidence |
| 20 | gsheets | sheets (Users) | f_50ff132ac88169019feeca | cohort AdMob; T15; C5 | ● grid | shared reader | per-record evidence |
| 21 | gsheets | sheets (Access) | f_2f0abe2f1f6726fef63f80 | cohort TikTok; T6; T13 | ● grid | shared reader | per-record evidence |
| 22 | gsheets | sheets (Permissions, Removed users) | f_fc27672c5bfea8b760b074 | cohort YouTube; T6 | ● grid | shared reader | per-record evidence |
| 23 | gsheets | sheets (Page admins) | f_b89c1c70489f81031bdd4f | cohort LinkedIn | ● grid | shared reader | per-record evidence |
| 24 | gsheets | sheets (Access) | f_99d66f33c54338e70f5ed2 | cohort X; T14 | ● grid | shared reader | per-record evidence |
| 25 | gsheets | sheets (Access) | f_215ff8da73e4173f78515c | cohort Instagram; T6; T14 | ● grid | shared reader | per-record evidence |
| 26 | gsheets | sheets (Admins) | f_2cecf2f81045ec401feb61 | cohort Discord | ● grid | shared reader | per-record evidence |
| 27 | gsheets | sheets (Users) | f_5f2f52786dcd8e1168cd40 | T10 (out of scope: store) | ● grid | shared reader | decoy |
| 28 | gsheets | sheets (Users) | f_ad393ed61590f2d22c6cd7 | T10 (out of scope: store) | ● grid | shared reader | decoy |
| 29 | gsheets | sheets (Users) | f_b463693cd3779d4d25374f | T10 (out of scope: data tool) | ● grid | shared reader | decoy |
| 30 | gsheets | sheets (Sheet1) | f_4521c272960dd1836a5196 | T4 (stale partial list); C4 hop 1 | ● grid | owned | decoy |
| 31 | gdocs | gdocs.docs_documents + drive row | f_c612c0e68a27b3330eb46a | H2 authority; K5; C2 hop 3; C5 hop 2; T3 v2 | ● body | shared reader | authority |
| 32 | gdrive | gdrive.drive_files | d_21f9e11d43739eaef26b38 | K7 destination; write W2 | ● metadata | shared writer | write target |
| 33 | confluence | confluence_pages + page_versions | page_company_accounts_access | H1 decoy; T2 v1 | ● body | unscoped | decoy (oldest version) |

Ledger rows carry the record each manifest element points to; child rows written with them (the drive row of every Sheet and the Doc,
tab rows under each spreadsheet, the createCard actions, the version row ver_ffb23fbfca7fff13209da81776386b49 of the page, the
three mailbox copies) belong to the listed record. Totals from `sql_lint.py`: 76 INSERT, 0 UPDATE over 7 schemas.

## 3 Findability and discovery-order proofs

| Record | Agent's likely query | Term present (pointer) | Competing base hits / how reached | Chain position |
|---|---|---|---|---|
| D05S58U4SAK/1759272012.507134 | Slack DM history with Leonard / search "handover" | "arthur's handover rules", "sweep", "Company Ops folder" | newest DM message before the clock | first link (A1) |
| 68dc406c7b0d03e53b334bab | trello search "handover rules" / Harmony Games board To Do list | card name "Account handover rules - marketing, UA & socials" | 0 base hits (§1.D); the same search returns the engineering card 68dc42f3095ad95194a711ae | connecting (H1) |
| 68dc529406d8087e5a6b8403 | trello card comments | "socials … never get CLOSE" | only comment on the card; badges comments 1 | overturning (T2 v3) |
| frederick.stone@harmonygames.co/1844732985606656293 | gmail search "handover rules" / "Account handover" | subject = the card's title | 0 base hits (§1.D); arrives after the hub (23:21Z) | overturning (T2 v4) |
| f_c612c0e68a27b3330eb46a | gdocs search "money moving" / "for the cuts" / "cash notes" | heading "Money still moving (for the cuts)" | Slack "for the cuts" first returns the Sep 24 remark C07C2866011/1758739436.208417 | connecting (H2) |
| d_6cae3483dd469c189a528e | gdrive search "sweep" / list folders shared by Arthur | folder "Admin sweep - Sep 30" | 0 base hits; named by C07C2866011/1759266627.118342 ("sweep's in the drive folder") | connecting (cohort) |
| f_f7e7c5bf089029cee91175 | gsheets values_get on the export | tab "Partners": "Node Media LLC … Partner admin" | a first-tab read shows People only | per-record (T9) |
| f_99d66f33c54338e70f5ed2 | gsheets values_get | "no delegates set up" | the drive listing shows the title only | per-record (C1) |
| page_company_accounts_access | confluence search "accounts" / "Company Accounts" | title "Company Accounts & Access" | named by the card ("replace the old Company Accounts & Access page") | decoy (T2 v1) |
| 67cf1b506d78ad3c72e02a35 | trello search "social handles" | base card name | named by the card rule 7 | write target (W4) |
| C07UCC631A6/1757349668.681539 | slack conversations_replies on C07UCC631A6/1757346020.196019 | "you will not be responsible for the cost of those installs" | parent says "it got turned on Sep 1st"; reply only in the thread | eliminating evidence (C2) |
| snowflake.json /tables/35 | snowflake query AD_REVENUE by network, 2025-09 | network admob, accrued_vs_paid paid | named by the doc ("the warehouse has it by network and month") | terminal (C5) |

Dynamic-change seeds (claim met first · overturned by · why met first · why decisive):
- Leonard's claim D05S58U4SAK/1759187141.318207 (Sep 29) · the Sep 30 exports f_f7e7c5bf089029cee91175, f_63b42f52fa11d7df238a4e,
  f_1191b7f8c96419e1f4dc88 · it sits a few messages above the hub in the same DM · the exports are newer and list his roles.
- Arthur's summary C07C2866011/1759266627.118342 · the exports read under card rules 2–4 · it is the newest #executives message about the
  sweep · the exports show X and Instagram with fewer than two company holders and Meta with a partner.
- The 2024 page page_company_accounts_access → card 68dc406c7b0d03e53b334bab → comment 68dc529406d8087e5a6b8403 → email
  frederick.stone@harmonygames.co/1844732985606656293 · each newer record names what it changes and keeps the rest ("Rest of the card
  stands"; "Everything else on the card stands") · the card says it replaces the page.
- The 90-day remark C07C2866011/1758739436.208417 (Sep 24) · the doc f_c612c0e68a27b3330eb46a (modified Sep 30 17:48Z) · a Slack search
  "for the cuts" meets the remark first · the card names Leonard's definition; the doc is his newer, written one.

Hidden authorities: H1 "account handover rules" → trello 68dc406c7b0d03e53b334bab (decoys 68dc42f3095ad95194a711ae, scope engineering /
stores / data tools, decisive clause "My list, not Fred's"; page_company_accounts_access, older version replaced by the card). H2
"money still moving" → gdocs f_c612c0e68a27b3330eb46a (decoy C07C2866011/1758739436.208417, older version by the same author).

## 4 Self-validation

| QC category | Tool-enforced (sql_lint / base_check) | Manual — evidence |
|---|---|---|
| Missing Universe Data | — | every register value is in a persona-readable record (1.E, check-sql PASS); Trello, Confluence, Snowflake unscoped; catalog writes exist: gsheets_create_spreadsheet, gsheets_values_update, gdrive_move_file (d_21f9e11d43739eaef26b38 shared writer), slack_send_message (D05S58U4SAK), trello_create_checklist + trello_create_check_item (67cf1b506d78ad3c72e02a35) |
| Temporal Field | PASS: all seeded times < 2025-10-01T00:00Z (latest 2025-09-30T23:21:09Z, frederick.stone@harmonygames.co/1844732985606656293); created ≤ modified | dates in text: card (20:41Z) says "today's sweep folder" — the folder is 19:50Z and its last export 20:31Z; the hub (22:40Z) postdates card, sweep and folder (22:31Z); the doc heading "September 2025" sits in a doc modified Sep 30; export dates (Node unlinked 2024-12-20) match D05S58U4SAK/1734719973.099339 |
| Cross-service Referential | PASS: channel, board, list, page_company_home, Drive roots resolve; Docs/Sheets sharing = Drive rows | the customer IDs 569-350-5790 / 449-481-1590 are spelled as in the base mails; Node Media LLC as in C04UEQVDVB7 (2025-01 shard); the card cites "Lock up social handles and domain?" exactly as trello 67cf1b506d78ad3c72e02a35 |
| Quantitative / Reconciliation | PASS: Trello badges (68dc406c7b0d03e53b334bab comments 1; 68dc42f3095ad95194a711ae 0) | no seeded figure; AD_REVENUE 2025-09 admob paid $38.70 re-aggregated (snowflake.json /tables/35); TikTok "64 followers" as D05S58U4SAK/1759160336.370489 |
| State / Lifecycle | PASS: no Linear / Confluence edit; page version 1 = body | no status contradicted: Unity campaigns on (C07C2866011/1759186080.203099) while the Unity export shows the Harmony Games Inc org with three Owners; Adjoe paused Sep 8 (C07UCC631A6/1757347560.891949); Google Ads "Enabled campaigns 0" vs UAC last spend 2025-04-10 (snowflake.json /tables/0) |
| Identifier / Format | PASS: Slack sha ids; Gmail mailbox/Message-ID + numeric thread ids; f_/d_ + 22 hex; Trello time-prefixed ids; ver_ + 32 hex | emails copied from the roster; tokens reused from base (1.F) |
| Semantic / Category | — | titles match content ("Unity - Harmony Games Inc org - members"); the folder is "Admin sweep - Sep 30"; one name per entity |
| Other | — | voice per 1.C; rules state principles, never an account's class or action (fact_check: no register value in any seeded row) |

## 5 Lazy-solver pass on the implemented records

| Shortcut tried | What it yields | Why it fails / fix |
|---|---|---|
| Trust Arthur's summary C07C2866011/1759266627.118342 | YouTube + TikTok TRANSFER, everything else KEEP | X, Instagram SINGLE too; Meta REVOKE; two CLOSE |
| Trust Leonard's claim D05S58U4SAK/1759187141.318207 | Meta, Google Ads and Unity are "covered" (KEEP) | his admin is real, but Meta is REVOKE (Node partner) and the Calm Play Google Ads is CLOSE |
| Build from the March sheet f_4521c272960dd1836a5196 | 11 rows incl. PlayableX, Singular, old AdMob | hub: the sweep is the list; Calm Play Google Ads, X, Instagram, Discord missing |
| List the sweep folder and stop at file names | 16 accounts | card rule 1 drops three; roles exist only inside the exports |
| Read first tabs only | Meta COMPANY-HELD → KEEP | Partners tab → OUTSIDE ACCESS (T9) |
| Card description only | dormant socials CLOSE; both Google Ads CLOSE | comment 68dc529406d8087e5a6b8403; email frederick.stone@harmonygames.co/1844732985606656293 |
| Money from Gmail receipts only | AdMob N → CLOSE; Adjoe Y | doc: ad revenue paid counts (AD_REVENUE); waiver reply C07UCC631A6/1757349668.681539 |

No seeded row states a class, an action, a count of TRANSFER rows or the outside party's status (`fact_check` PASS; the facts declared
are identifiers only).

## 6 Intended disagreements

| Disagreement | Records | Why realistic | What resolves it |
|---|---|---|---|
| Leonard's admin claim vs the exports | D05S58U4SAK/1759187141.318207; f_f7e7c5bf089029cee91175 | a CEO who uses the accounts daily assumes he is admin | the Sep 30 exports (newer) |
| Arthur's summary vs the exports | C07C2866011/1759266627.118342; f_99d66f33c54338e70f5ed2 | Arthur forgets the socials Fred set up alone | the exports under the card's rules 2–3 |
| 2024 page vs card vs comment vs email | page_company_accounts_access; 68dc406c7b0d03e53b334bab; 68dc529406d8087e5a6b8403; frederick.stone@harmonygames.co/1844732985606656293 | a 2024 policy, a new rule set, two same-day refinements | newest wins, each names its scope |
| 90-day remark vs cash notes | C07C2866011/1758739436.208417; f_c612c0e68a27b3330eb46a | a quick Slack thought, then a written definition | the doc (newer, same author, named by the card) |
| March logins sheet vs the sweep | f_4521c272960dd1836a5196; d_6cae3483dd469c189a528e | Fred's own stale list from March | the hub names the sweep |
| Deactivated AdMob vs the active one | frederick.stone@harmonygames.co/1841349862518331350; f_50ff132ac88169019feeca | two AdMob publisher accounts exist | different publisher ids; the sweep holds the active one |

## 7 Constraints for the prompt brief

| Anchor | May be named (noun phrases only) | Record |
|---|---|---|
| A1 | Leonard's account handover ask; the account register; the planned layoffs | D05S58U4SAK/1759272012.507134 |

| Destination (V3: the prompt may name it) | Record |
|---|---|
| reply in the DM with Leonard | D05S58U4SAK/1759272012.507134 |
| the Company Ops folder | d_21f9e11d43739eaef26b38 |

Never named in the prompt: the rules card or its board, the comment, Arthur's email, the cash notes doc, the sweep folder's location,
the Partners / Linked managers / Removed users tabs, Node Media, the Adjoe waiver, the warehouse, the AdMob publisher ids, the classes, the actions, the
handles card, any id or the root cause (V3 §8). Deadline: before people are let go (no date). Deliverables: a register Google Sheet
in Company Ops; a DM reply with the TRANSFER count and the outside access; a checklist on the existing handles card. Times: Pacific,
with UTC beside them when the day differs (V3 §10): the hub is Tue Sep 30, 3:40 PM PT (22:40Z); Arthur's email 4:21 PM PT (23:21Z).

## 8 Fact sheet

| Key | Value | Kind | Must appear in / home |
|---|---|---|---|
| Harmony Games, Inc. | 569-350-5790 | id | f_ab70b02c329d038a72fb9f; frederick.stone@harmonygames.co/<CAOOpSq6NYC_rzIOrbQLSZpivEB6VyNfx48bLl8VjW0@mail.gmail.com> |
| Calm Play one (alias Calm Play LLC) | 449-481-1590 | id | frederick.stone@harmonygames.co/<CAOOpSq6NYC_rzIOrbQLSZpivEB6VyNfx48bLl8VjW0@mail.gmail.com> |
| Publisher ID (active AdMob) | pub-3556282811018998 | id | home f_50ff132ac88169019feeca |
| Unlinked / Removed (Node) | 2024-12-20 | date | f_ab70b02c329d038a72fb9f; f_63b42f52fa11d7df238a4e; f_fc27672c5bfea8b760b074 |

`python3 Task_Authoring/tools/fact_check.py Task_Authoring/task_inputs/01_Universe_Inject.sql --manifest Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.json --no-leak`:

```
FACT CHECK: PASS — 71 text-bearing rows, 4 declared facts, 5 declared superseded records
Errors: none
```

## 9 Facts for the human

### 9.1 Records

| Locator | Base / seeded | Fact (values, actors, UTC) | Reach path | Role | Re-verify? |
|---|---|---|---|---|---|
| D05S58U4SAK/1759272012.507134 | seeded | Leonard → Fred, 2025-09-30T22:40:12Z: register of every marketing + UA account Fred is on; holder, money moving, action; rules on the Harmony Games board; the sweep is the list; save in Company Ops; reply with how many marked TRANSFER and any outside access | im member | LB anchor | no |
| D05S58U4SAK/1759187141.318207 | seeded | Leonard, 2025-09-29T23:05:41Z: "i'm admin on meta, google ads and unity already" | im member | LB claim met first | no |
| C07C2866011/1759266627.118342 | seeded | Arthur, 2025-09-30T21:10:27Z: "only youtube and tiktok are on fred alone, everything else already has two of us on it" | #executives member | LB claim met first | no |
| C07C2866011/1758739436.208417 | seeded | Leonard, 2025-09-24T18:43:56Z: "for the cuts list I'd keep anything we've paid in the last 90 days" | #executives member | LB decoy (superseded) | no |
| trello:68dc406c7b0d03e53b334bab | seeded | Arthur, 2025-09-30T20:41:16Z, Harmony Games board / To Do: rules 1–7 (scope, holder, company holder, class, action order, columns, socials checklist on the handles card) | unscoped | authority H1 | no |
| trello:68dc529406d8087e5a6b8403 | seeded | Arthur comment, 2025-09-30T21:58:44Z: socials (YouTube, TikTok, Instagram, X, LinkedIn, Discord) never CLOSE | unscoped | overturning evidence | no |
| trello:68dc42f3095ad95194a711ae | seeded | Arthur, 2025-09-30T20:52:03Z: engineering list (GitHub, AWS, Unity Cloud Build, App Store Connect, Play Console, Singular, Metabase); one Owner fine; KEEP or MOVE | unscoped | decoy | no |
| frederick.stone@harmonygames.co/1844732985606656293 | seeded | Arthur → Fred cc Leonard, 2025-09-30T23:21:09Z: keep Harmony Games, Inc. Google Ads 569-350-5790 (KEEP); Calm Play 449-481-1590 still follows the card | own mailbox | LB overturning evidence | no |
| d_6cae3483dd469c189a528e | seeded | "Admin sweep - Sep 30", owner Arthur, created 19:50Z; 16 exports 19:52–20:31Z | shared reader | LB cohort container | no |
| f_f7e7c5bf089029cee91175 | seeded | Meta Domino Delights ad account 907669287942378: Fred, Robert, Leonard (portfolio), Arthur Admin; Partners: Node Media LLC partner admin since 2024-10-07 | shared reader | LB evidence | no |
| f_ab70b02c329d038a72fb9f | seeded | Google Ads 569-350-5790 Harmony Games, Inc.: Leonard Admin 2024-09-20, Fred Admin 2024-10-07; 0 enabled campaigns; Node unlinked 2024-12-20 | shared reader | LB evidence | no |
| f_63b42f52fa11d7df238a4e | seeded | Google Ads 449-481-1590 Calm Play LLC: Robert, Leonard, Arthur, Fred Admin (added 2024-01-10 / 01-20 / 01-20 / 09-05, as in base Gmail); 0 enabled campaigns; Node (645-364-1205) unlinked 2024-12-20 | shared reader | LB evidence | no |
| f_1191b7f8c96419e1f4dc88 | seeded | Unity Harmony Games Inc org 20067043314233 (Owners and Managers): Arthur, Robert, Leonard Owner; Fred Manager | shared reader | LB evidence | no |
| f_3996bca752549d3512bfbc | seeded | AppLovin: Leonard Admin, Fred Admin | shared reader | LB evidence | no |
| f_a552317a929102385c0393 | seeded | adjoe: Fred Admin, Leonard Admin | shared reader | LB evidence | no |
| f_50ff132ac88169019feeca | seeded | AdMob pub-3556282811018998: Leonard Admin (owner), Fred Admin since 2025-08-25 | shared reader | LB evidence | no |
| f_2f0abe2f1f6726fef63f80 | seeded | TikTok @harmonygames: login frederick.stone@ Admin, Leonard signs in with it; @harmonygames.app deleted 2025-09-29 | shared reader | LB evidence | no |
| f_fc27672c5bfea8b760b074 | seeded | YouTube: Fred Owner 2024-11-21, Leonard Manager 2025-04-27; Removed users: Node Media LLC 2024-12-20 by Fred | shared reader | LB evidence | no |
| f_b89c1c70489f81031bdd4f | seeded | LinkedIn page: Leonard, Fred Super admin | shared reader | LB evidence | no |
| f_99d66f33c54338e70f5ed2 | seeded | X @harmonygames: Fred Owner only | shared reader | LB evidence | no |
| f_215ff8da73e4173f78515c | seeded | Instagram @harmonygames: owner login [EMAIL_912045], Fred's personal gmail | shared reader | LB evidence | no |
| f_2cecf2f81045ec401feb61 | seeded | Discord: Leonard Owner, Fred Admin, Robert Admin (all harmonygames.co) | shared reader | LB evidence | no |
| f_5f2f52786dcd8e1168cd40 | seeded | Play Console Harmony Games, Inc.: Leonard owner + 9 users from the base acceptance mails (Fred 2024-09-22 … EMPLOYEE_0032 2025-09-30) | shared reader | LB decoy (out of scope) | no |
| f_ad393ed61590f2d22c6cd7 | seeded | App Store Connect Harmony Games, Inc. team: Leonard Account Holder 2024-09-25; Fred, Robert, Calvin members (base welcome mails; Vincent and Brian joined the separate Calm Play LLC team) | shared reader | LB decoy (out of scope) | no |
| f_b463693cd3779d4d25374f | seeded | Singular users: Leonard Admin; Robert, Douglas, Fred, Simon Walker (base invites) | shared reader | LB decoy (out of scope) | no |
| f_4521c272960dd1836a5196 | seeded | Fred's "Marketing & UA logins", 2025-03-10: 11 platforms incl. old AdMob pub-2341961509332343, Singular, PlayableX | owned | LB decoy | no |
| f_c612c0e68a27b3330eb46a | seeded | Leonard's "Runway & shutdown cash notes", modified 2025-09-30T17:48Z: money moving = spent, billed or paid out in September 2025 or a campaign still on; ad revenue paid to us counts; a charge the vendor agreed in writing to drop doesn't | shared reader | LB authority H2 | no |
| d_21f9e11d43739eaef26b38 | seeded | "Company Ops", owner Leonard, created 22:31Z, Fred + Arthur writers | shared writer | LB write target | no |
| confluence:page_company_accounts_access | seeded | Leonard, 2024-03-12: one owner + one backup admin; don't close accounts | unscoped | decoy (oldest version) | no |
| trello:67cf1b506d78ad3c72e02a35 | base | "Lock up social handles and domain?" on UA/BD, list ZM 3d Technical Launch / Alpha, no checklist | unscoped | write target (W4) | no |
| trello:670010236b89198587ca45b6 | base | "Access to meta and Google Ad account shared with Node" (2024-10-07) | unscoped | supporting | no |
| C07UCC631A6/1757346020.196019 | base | Leonard, 2025-09-08: Adjoe campaign turned on Sep 1 (6 replies) | adjoe member | LB evidence | no |
| C07UCC631A6/1757347560.891949 | base | Adjoe rep: paused the campaign | adjoe member | LB evidence | no |
| C07UCC631A6/1757349668.681539 | base | Adjoe rep: "you will not be responsible for the cost of those installs" | adjoe member | LB eliminating evidence | no |
| C07C2866011/1759186080.203099 | base | Leonard, 2025-09-29T22:48Z: iOS Unity budget $150/campaign/day | #executives member | LB evidence (Unity Y) | no |
| C07C2866011/1759264050.305069 | base | Fred, 2025-09-30: clicks up 5x on iOS | #executives member | LB evidence (Unity Y) | no |
| D05S58U4SAK/1758922541.613439 | base | Leonard, 2025-09-26: "I turned off the FB campaign" | im member | LB evidence | no |
| D05S58U4SAK/1756147086.813789 | base | Leonard, 2025-08-25: AdMob "It's active and a working account" | im member | LB evidence (T15) | no |
| D05S58U4SAK/1759096868.688389 | base | Leonard: YouTube manager, not owner | im member | LB evidence | no |
| D05S58U4SAK/1759170013.491159 | base | Fred: TikTok tied to frederick.stone@harmonygames.co | im member | LB evidence | no |
| frederick.stone@harmonygames.co/1843428112007517388 | base | Meta receipt 2025-09-16 | own mailbox | LB evidence (Meta Y) | no |
| frederick.stone@harmonygames.co/1843223812315546201 | base | AppLovin payout 2025-09-14 | own mailbox | LB evidence (AppLovin Y) | no |
| frederick.stone@harmonygames.co/1835153849970828373 | base | Google Ads 569-350-5790 "[SOURCE_ORG_0001], Inc." | own mailbox | LB evidence (T8) | no |
| frederick.stone@harmonygames.co/1838369017520543217 | base | Google Ads ad disclosure "Ads funded by Calmplay LLC" | own mailbox | LB evidence (T8) | no |
| frederick.stone@harmonygames.co/1841349862518331350 | base | AdMob pub-2341961509332343 deactivated 2025-08-24 | own mailbox | distractor (T15) | no |
| snowflake.json /tables/35 | base | AD_REVENUE 2025-09: admob paid 1,163 rows $38.70; applovin paid $136.33; meta_audience paid $26.15 | unscoped | evidence (C5) | yes, after regeneration |

### 9.2 Derived ground truth (from the records above; for the human's Oracle Events and rubric)

| Account (export) | Company holders | Class | Money moving | Action |
|---|---|---|---|---|
| Meta (f_f7e7c5bf089029cee91175) | Frederick Stone, Robert, Leonard Hayes, Arthur Blake | OUTSIDE ACCESS (Node Media LLC partner admin) | Y | REVOKE |
| Google Ads 569-350-5790 (f_ab70b02c329d038a72fb9f) | Leonard Hayes, Frederick Stone | COMPANY-HELD | N | KEEP (email frederick.stone@harmonygames.co/1844732985606656293) |
| Google Ads 449-481-1590 (f_63b42f52fa11d7df238a4e) | Robert, Leonard Hayes, Arthur Blake, Frederick Stone | COMPANY-HELD | N | CLOSE |
| Unity (f_1191b7f8c96419e1f4dc88) | Arthur Blake, Robert, Leonard Hayes | COMPANY-HELD | Y | KEEP |
| AppLovin (f_3996bca752549d3512bfbc) | Leonard Hayes, Frederick Stone | COMPANY-HELD | Y | KEEP |
| adjoe (f_a552317a929102385c0393) | Frederick Stone, Leonard Hayes | COMPANY-HELD | N (waiver C07UCC631A6/1757349668.681539) | CLOSE |
| AdMob (f_50ff132ac88169019feeca) | Leonard Hayes, Frederick Stone | COMPANY-HELD | Y (snowflake.json /tables/35) | KEEP |
| TikTok (f_2f0abe2f1f6726fef63f80) | Frederick Stone | SINGLE | N | TRANSFER (comment 68dc529406d8087e5a6b8403) |
| YouTube (f_fc27672c5bfea8b760b074) | Frederick Stone | SINGLE | N | TRANSFER |
| LinkedIn (f_b89c1c70489f81031bdd4f) | Leonard Hayes, Robert, Arthur Blake, Frederick Stone | COMPANY-HELD | N | KEEP |
| X (f_99d66f33c54338e70f5ed2) | Frederick Stone | SINGLE | N | TRANSFER |
| Instagram (f_215ff8da73e4173f78515c) | none | SINGLE | N | TRANSFER |
| Discord (f_2cecf2f81045ec401feb61) | Leonard Hayes, Frederick Stone, Robert | COMPANY-HELD | N | KEEP |

Out of scope (card rule 1): f_5f2f52786dcd8e1168cd40, f_ad393ed61590f2d22c6cd7, f_b463693cd3779d4d25374f; deleted TikTok
@harmonygames.app; ironSource (frederick.stone@harmonygames.co/1837038650805365569, MAX bidder, no export). Totals: REVOKE 1, TRANSFER 4,
KEEP 6, CLOSE 2. Reply: 4 marked TRANSFER; Node Media LLC still has partner admin on the Meta ad account. Checklist on
67cf1b506d78ad3c72e02a35: TikTok, YouTube, X, Instagram. Accept holders by name or address; the money column Y/N.

## 10 Integrations and companions

| Service | INT id (`references/universe_kb/integrations.json`) | Companion seeded | Reason |
|---|---|---|---|
| slack | INT-22 (Slack e-mail notification) | none | the DM D05S58U4SAK carries no notification mails for Frederick in Sep 2025 (base gmail sweep of his mailbox, 2025-09) |
| gdrive | INT-13 (Google Drive Slack app share DM) | none | base shares from Leonard and Arthur to Frederick (e.g. d_63fffeb4fab5233ed5bb73 children) carry no Drive app DM in this window |
| gsheets | INT-13 | none | covered with gdrive |
| gdocs | INT-13 | none | covered with gdrive |
| trello | INT-21 (Trello → Slack) | none | no Trello integration posts in any channel for the Harmony Games board |
| gmail | gmail: none (no integration originates in Gmail) | — | one copy per mailbox: Frederick INBOX, Leonard INBOX (Cc), Arthur SENT |
| confluence | confluence: none in integrations.json | — | — |

## 11 Touched-data census and coherence hazards

Census (every record a correct run opens): the hub DM D05S58U4SAK (Sep 25 – 30 messages incl. D05S58U4SAK/1759187141.318207), #executives
Sep 24 and Sep 29 – 30 (C07C2866011/1758739409.488879, /1759186080.203099, /1759264050.305069, /1759266627.118342), the adjoe thread
C07UCC631A6/1757346020.196019 and its 6 replies, the two seeded cards + comment, the handles card 67cf1b506d78ad3c72e02a35, the Node
card 670010236b89198587ca45b6, the email frederick.stone@harmonygames.co/1844732985606656293, the doc f_c612c0e68a27b3330eb46a, the
sweep folder + 16 exports, the March sheet, page_company_accounts_access, snowflake.json /tables/35, the Meta / AppLovin / Google
Ads / AdMob / Adjoe mails cited in §9.1.

| Hazard id (`coherence_hazards.json`) | Category | Intersects | Disposition |
|---|---|---|---|
| T07 | temporal | post-clock base mails: Adjoe Oct 1 invoice frederick.stone@harmonygames.co/1844773822453719122, Google Ads 449 canceled Oct 16 frederick.stone@harmonygames.co/1846207913166171315 | excluded: not cited; Leonard disputes the Oct 1 invoice citing the agreed removal, which agrees with the waiver; 449 CLOSE agrees with the cancellation |
| T08 | temporal | seeded Confluence page dated 2024-03-12 by Leonard | avoid: Leonard active in Mar 2024 (activity.json); no later edit |
| T06 | temporal | Trello id timestamps | fold in: ids minted from their own seconds (68dc406c = 2025-09-30T20:41:16Z); dateLastActivity = comment time |
| S05 | semantic | Frederick is_founder=false in PAYROLL_ROSTER (snowflake.json /tables/39) | excluded: not read |
| S06 | semantic | Contacts job titles | excluded: not read or modified |
| R04 | cross-service referential | Slack links to Google files carry native ids (C08H78VJG80/1759174925.309129) | avoid: no seeded text carries a Google URL; records are named by title |
| Q08 | quantitative | AD_SPEND_DAILY Unity Sep $0 vs campaigns on (snowflake.json /tables/0; C07C2866011/1759186080.203099) | excluded: AD_SPEND_DAILY neither cited nor modified; Unity Y rests on the switched-on campaign |
| Q09 | quantitative | mirrored warehouse tables (snowflake.json /tables/0, /tables/34) | excluded: not read or modified |
| Q01 | quantitative | reply counters on C07UCC631A6/1757346020.196019 | avoid: no seeded reply (6 base replies) |
| L12 | state/lifecycle | Done-list cards with open checklists | avoid: the handles card 67cf1b506d78ad3c72e02a35 is in "ZM 3d Technical Launch / Alpha", not Done |
| I05 | identifier/format | token mailbox SVC_0009 forwards AppLovin payouts "Dear Leonard Hayes" (frederick.stone@harmonygames.co/1843223812315546201) | fold in: the AppLovin export lists Leonard and Fred as admins |
| I04 | identifier/format | mixed Gmail date forms | avoid: seeded mail uses ISO date + RFC-2822 Date header, as the base |
| I17 | identifier/format | Leonard is a token on Trello (PERSON_6094_TRELLO_USER_ID) | fold in: seeded Trello actions are Arthur's (2162c1ba310341bf318f48b7) |

## 12 Platform follow-ups

- ○ carriers: none load-bearing. Every decisive fact sits in Slack text, a Trello description or comment, a Gmail body, Sheets values,
  a Docs body, a Confluence body or Drive metadata (● carriers, `Ask_Carriers.md` §5).
- Confluence: page_company_accounts_access is a seeded page in a live space; re-verify after any regeneration. sql_lint confluence
  warning ×2 (line 173 / 175, "unscoped and rarely opened"): disposition — the card 68dc406c7b0d03e53b334bab points to the page by name;
  the page is a decoy, not needed for a correct run.
- Snowflake AD_REVENUE (snowflake.json /tables/35) is base data; re-verify the 2025-09 admob paid rows after regeneration.
- Second tabs: whether `gsheets_values_get` without a range returns only the first tab is confirmed in the Opus pre-check (the design
  budgets a read per tab; no budget row is conditional).

## 13 Self-review

### Tool outputs (verbatim, final run)

`python3 Task_Authoring/tools/sql_lint.py Task_Authoring/task_inputs/01_Universe_Inject.sql`:

```
schemas touched (7): confluence, gdocs, gdrive, gmail, gsheets, slack, trello
rows by schema: {'gdrive': 20, 'gsheets': 38, 'gdocs': 1, 'slack': 4, 'trello': 5, 'gmail': 6, 'confluence': 2}  total rows: 76  ops: {'insert': 76}
errors: 0  warnings: 2
  warn  line 171: confluence statement — unscoped and rarely opened by agents: make sure another record points here
  warn  line 173: confluence statement — unscoped and rarely opened by agents: make sure another record points here
```

Warning dispositions: confluence statement ×2 ("unscoped and rarely opened by agents") — disposition: the rules card names the page; it
is the oldest superseded version (decoy) and no requirement depends on opening it; kept.

`python3 Task_Authoring/tools/base_check.py Task_Authoring/task_inputs/01_Universe_Inject.sql`:

```
BASE CHECK (/injection A + C, static): PASS  — 76 inserts, 0 updates
Check A — records, references, IDs: PASS
Check C — dates and relationships: PASS
  note: gsheets.sheets_sheets: no base-reference rules (checked by sql_lint only)
```

`python3 Task_Authoring/tools/hardness_gate.py Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.json Task_Authoring/task_inputs/01_Universe_Inject.sql`:

```
HARDNESS GATE (normal): PASS
  [ok] effective_profile: effective_profile 'normal' for 'Normal Horizon' → thresholds 'normal'
  [ok] sql_lint_clean: 0 lint error(s) — run tools/sql_lint.py
  [ok] base_consistency: /injection-style checks vs the base universe: A 0 finding(s), C 0 finding(s), 0 warning(s) — run tools/base_check.py --manifest
  [ok] persona_reach: 31 load-bearing seeded ids for frederick_stone (5 in unscoped services = visible, 26 judged by persona_view check-sql); not provably visible: none
  [ok] fact_consistency: fact_check: 0 error(s) (4 declared facts), 0 drift warning(s); first: none — run tools/fact_check.py --manifest --no-leak
  [ok] hazard_scope: 0 pre-existing hazard(s) among task-touched records; state/lifecycle or referential without a verified resolution: none
  [ok] services_injected: 7 schemas injected (confluence, gdocs, gdrive, gmail, gsheets, slack, trello); need ≥ 6
  [ok] rows: 76 INSERTed rows (UPDATE companions not counted; 76 rows in all); need ≥ 50
  [ok] services_carrying_weight: 8 services with a weight_reason; need ≥ 7
  [ok] no_orphan_injection: schemas injected but absent from the design: none
  [ok] seeded_ids_exist_in_sql: 64 seeded ids cited; missing from SQL: none
  [ok] anchors: 1 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 8 fragments; need ≥ 7
  [ok] ask_fragment_services: 5 services carry asks; need ≥ 5
  [ok] ask_fragment_containers: 7 distinct containers; need ≥ 6
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 8 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 13; need ≥ 10 (source-defined: True)
  [ok] evidence_surfaces: 4 surfaces over 4 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 34; need ≥ 25
  [ok] call_budget: unconditional (verified) floor 60 of 60 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 60 and total ≤ 100 (Normal Horizon 50–100)
  [ok] call_budget_spread: 8 services in budget; largest share outside the per-record phase 37% (≤ 40%)
  [ok] traps: 15 traps across 9 families; need ≥ 8 / ≥ 5; unknown family: none
  [ok] trap_independence: traps hit 6 distinct requirements; need ≥ 4 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 3 supersessions (3 with versions in ≥ 2 services, 1 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: 3 trap(s) with version_records; the records' own timestamps (SQL created_at/ts/date/updated_at, or the base record) must be strictly increasing in the listed order (oldest first); bad: none
  [ok] distractors: 4 distractors of 4 types; need ≥ 4 / ≥ 3
  [ok] discovery_order_proofs: 6 traps carry a discovery-order proof; need ≥ 2
  [ok] independent_chains: 5 chains with 5 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 2, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] hidden_authorities: 2 authorities (need ≥ 1), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 0 (need ≥ 0: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 12 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 2
  [ok] requirements: 8 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 4 writes over 4 services; each must depend on findings
```

### /injection Checks A–C walk (`Evals/0_Injection_Quality_Eval.md`)

| Check | Verdict | Evidence |
|---|---|---|
| Inventory | PASS | 76 INSERT, 0 UPDATE, 0 DELETE, no upsert: gdrive 20, gsheets 38, gdocs 1, slack 4, trello 5, gmail 6, confluence 2 |
| Check A — references (incl. archived/history) | PASS | channels D05S58U4SAK and C07C2866011 not archived; board 640643a3fd8f3ca308d9318e + list 640643a3fd8f3ca308d93195 open; page_company_home; Drive roots d_63fffeb4fab5233ed5bb73, d_cc3e90160f490686039986, d_175c0d7bc72ed244b944cb |
| Check A — uniqueness over the full collection | PASS | 1.F lookups scan_complete, 0 hits; Slack (channel, ts) free; Gmail thread numbers and Message-ID free |
| Check A — ownership / membership / shares | PASS | Gmail copies only in sender / To / Cc mailboxes; Docs/Sheets sharing = Drive rows; shares name roster people |
| Check A — ID contracts | PASS | Slack sha ids; Trello time-prefixed ids (68dc406c…, 68dc529406…); f_/d_ + 22 hex; ver_ + 32 hex |
| Check B — structure, literal JSON, generated / NOT NULL | PASS | sql_lint 0 errors; every *_json literal parses; text_fts / body_text_fts never written |
| Check C — dates | PASS | latest seeded time 2025-09-30T23:21:09Z (frederick.stone@harmonygames.co/1844732985606656293); created ≤ modified everywhere |
| Check C — parent/reply, statuses, counts | PASS | no seeded thread reply; H1 badges comments 1 = one commentCard 68dc529406d8087e5a6b8403; dateLastActivity 21:58:44Z |
| Check C — amounts, claimed updates, superseding records | PASS | no seeded amount; supersession chronology PASS (hardness_gate); each amendment names what it keeps |

### Counter-readings

| Category | Counter-reading (strongest argument it FAILS) | Evidence that resolves it | Verdict |
|---|---|---|---|
| Temporal | the card says "today's sweep folder" but could predate the sweep | card 68dc406c7b0d03e53b334bab at 20:41:16Z; folder d_6cae3483dd469c189a528e 19:50Z, last export f_b463693cd3779d4d25374f 20:31Z | PASS |
| Temporal | the 90-day remark (Sep 24) talks of a cuts list before anyone named one | Leonard 19 seconds earlier: "we need to save some cash aside too to close the company properly" (C07C2866011/1758739428.647609) after "2 months left" (C07C2866011/1758739409.488879) | PASS |
| Temporal | Arthur's email arrives after the hub, so Fred could not have known | V3: updates before the freeze count; 23:21:09Z < 2025-10-01T00:00Z; the hub asks for the register, not a deadline before 23:21Z (frederick.stone@harmonygames.co/1844732985606656293) | PASS |
| Semantic / Category | the hub's board name vs the board holding the card | the hub now says "the Harmony Games board", the card's board 640643a3fd8f3ca308d9318e; Trello search "handover rules" reaches the card directly (§1.D) | PASS |
| Semantic / Category | the deleted TikTok account could count as an account in the sweep | export f_2f0abe2f1f6726fef63f80 row status "Deleted 2025-09-29"; card rule 1 "deleted or deactivated before the sweep is off" | PASS |
| Cross-service Referential | Arthur has no base Trello activity yet authors three Trello records | he is a Trello member (trello/data.json /members, 2162c1ba310341bf318f48b7 "Arthur Blake"); Leonard's board is the company board the founders share (C07C2866011/1759252761.127709 shows Arthur active the same day) | PASS |
| Cross-service Referential | Node unlinked from Google Ads 449 although 449 could be a later account | 449-481-1590 mail since 2024-01-10 (robert@ threads/00002504.json; Fred's box from frederick.stone@harmonygames.co/1807948566988412613); Node asked for the Google Ads number 2024-09-23 (C08MCEP1B9B/1727063903.359939) | PASS |
| Cross-service Referential | the Meta export says Fred shared Node 2024-10-07; base never says who | trello 670010236b89198587ca45b6 "Access to meta and Google Ad account shared with Node", dateLastActivity 2024-10-07; Fred ran UA (C07C2866011/1757957294.669109) | PASS |
| Quantitative | AdMob paid revenue in September while the old AdMob account was deactivated for not serving ads | the deactivated id is pub-2341961509332343 (frederick.stone@harmonygames.co/1841349862518331350); Leonard's active account (D05S58U4SAK/1756147086.813789) carries the revenue; AD_REVENUE 2025-09 admob paid $38.70 (snowflake.json /tables/35) | PASS |
| Quantitative | the warehouse shows Unity Sep spend $0 (Q08), so Unity money could read N | doc f_c612c0e68a27b3330eb46a "or a campaign on it is still switched on"; C07C2866011/1759186080.203099 sets $150/campaign/day | PASS |
| State / Lifecycle | Adjoe invoices Sep installs on Oct 1, so money was billed | the invoice is dated Oct 1 (frederick.stone@harmonygames.co/1844773822453719122, after the clock) and disputed as agreed; the waiver C07UCC631A6/1757349668.681539 is written; doc clause on written waivers | PASS |
| State / Lifecycle | sibling defect: another account with an outside holder a run could find first (YouTube, Google Ads, Singular all had Node) | YouTube removed 2024-12-20 (f_fc27672c5bfea8b760b074 tab 2); both Google Ads unlinked 2024-12-20; Singular is out of scope (card rule 1; f_b463693cd3779d4d25374f lists no Node) | PASS |
| State / Lifecycle | the handles card is in a launch list and already done | 67cf1b506d78ad3c72e02a35 in "ZM 3d Technical Launch / Alpha", no checklist, badges checkItems 0 | PASS |
| People status | Robert's Discord admin seat after the cuts | Robert active_sep_2025 (activity.json); the register is pre-cut; Discord KEEP rests on two company holders (f_2cecf2f81045ec401feb61) | PASS |
| Identifier / Format | [EMAIL_912045] could collide with a base redaction | 1.F sweep 0 hits; body-text token space, not a header token | PASS |
| Identifier / Format | the Google Ads email subject has no "Re:" though the design called it a reply | design_delta K4 (01_Hardness_Manifest.json): a reply needs a parent message; the subject equals the card title, so a title search still finds it | PASS |
| Other | the Instagram note "Fred's personal gmail" reads as planted | Arthur annotates his own sweep (TikTok row note f_2f0abe2f1f6726fef63f80); the note states a fact, not the class | PASS |
| Designed disagreement (claim) | Leonard's claim is an unintended inconsistency between Slack and the exports | dated human claim Sep 29 (D05S58U4SAK/1759187141.318207) vs exports dated Sep 30 (f_1191b7f8c96419e1f4dc88) | designed |
| Designed disagreement (summary) | Arthur's summary and his own exports disagree with no resolution | the summary is a casual claim (C07C2866011/1759266627.118342); the card defines holders (68dc406c7b0d03e53b334bab rules 2–3) | designed |
| Designed disagreement (rules versions) | page, card, comment and email contradict each other | each later one names what it replaces or keeps (68dc406c7b0d03e53b334bab "These replace the old Company Accounts & Access page"; 68dc529406d8087e5a6b8403 "Rest of the card stands") | designed |
| Designed disagreement (90 days) | two live money definitions | the card names Leonard's definition; the doc is his newer one (f_c612c0e68a27b3330eb46a modified Sep 30 vs C07C2866011/1758739436.208417 Sep 24) | designed |
| Designed disagreement (March sheet) | Fred's sheet is a second register | dated 2025-03-10 (f_4521c272960dd1836a5196); the hub names the sweep (D05S58U4SAK/1759272012.507134) | designed |
| Designed disagreement (AdMob) | two AdMob accounts, either could be the one | different publisher ids; the active one is in the sweep (f_50ff132ac88169019feeca) and admitted Fred on Aug 25 (frederick.stone@harmonygames.co/1841453218828344296) | designed |

### Revision 2 — /injection review 6ad90e95653f5d56cdc2d881 (FAIL on Check C) and fixes

| Finding | Fix in this SQL | Base evidence re-read |
|---|---|---|
| C-1 Node manager ID 812-604-3397 not in the base | both Linked managers tabs (f_ab70b02c329d038a72fb9f, f_63b42f52fa11d7df238a4e) now say 645-364-1205 | HarmonyGames_Gmail threads/00007026.json, 00007027.json; leonard@harmonygames.co_1810637269809568957.json |
| C-2 449-481-1590 access list omitted Robert and Arthur; Leonard shown Standard; Fred dated 2024-08-20 | Access tab: Robert Admin 2024-01-10, Leonard Admin 2024-01-20, Arthur Admin 2024-01-20, Frederick Admin 2024-09-05 → four company holders, class COMPANY-HELD; no money moving, so the action stays CLOSE (totals unchanged: REVOKE 1 · TRANSFER 5 · KEEP 5 · CLOSE 2) | threads/00002504.json (account in Robert's box 2024-01-10), 00002732.json + 00002735.json (Leonard, Arthur Administrative 2024-01-20), 00006561.json + 00006608.json (Fred Administrative 2024-09-05); 2025-07-04 and 2025-09-17 notices still reach all four, no removal record |
| C-3 569-350-5790 Fred dated 2024-09-20 | Frederick Added 2024-10-07 (Administrative add notice); Leonard 2024-09-20, before his 2024-09-22 invites. Robert and Arthur were invited 2024-09-22 with no acceptance in the base, so they stay off | leonard@harmonygames.co_1812273271350908422.json; leonard@harmonygames.co_1810934379892698305.json |
| Check B advisory: trello_cards `start` / `idAttachmentCover` | both columns dropped from the two card INSERTs (they were NULL) | schema snapshot columns |

Knock-on: Leonard's Sep 29 claim (D05S58U4SAK/1759187141.318207, "admin on meta, google ads and unity") is now half true. Google Ads is
right on both accounts; Meta (Advertiser) and Unity (Manager) are wrong. The trap keeps Meta and Unity, and f_63b42f52fa11d7df238a4e
leaves its seeded_ids (design_delta C1–C3, T1, B1). Counter-reading: "449 COMPANY-HELD makes the Calm Play row easier." It does not.
Its action was CLOSE under either class, and it now also tests rule 2 against four holders, not one.

### Revision 3 — /injection review 6ad90e95653f5d56cdc2d881 rerun on a0d9f276 (FAIL on Check C) and fixes

This time every export row was re-grounded against base Gmail and Slack, not only the flagged rows. A date is kept only where a base record gives it.

| Finding | Fix in this SQL | Base evidence |
|---|---|---|
| C-1 AdMob pub-7795231806614420 invented | AdMob export title and grid now pub-3556282811018998; fact updated | C73E02AA3A22/1745467232.203529; leonard@harmonygames.co_1830467552498804662.json; Fred admin 2025-08-25 frederick@harmonygames.co_1841453218828344296.json |
| C-2 Meta People dates 2023-04-11 impossible | Meta export is the Domino Delights ad account 907669287942378: Fred Admin 2024-10-06, Robert Admin 2024-10-06, Leonard Admin via the portfolio 2024-01-22, Arthur Admin 2025-04-29; Partners tab unchanged | C08MCEP1B9B/1728233888.592579; threads/00007738.json; leonard@harmonygames.co_1788818142336108597.json; frederick@harmonygames.co_1809300661798738059.json; C07C2866011/1745941986.729119 |
| C-3 YouTube / Play Console dates | YouTube Fred Owner 2024-11-21, Leonard Manager 2025-04-27; Play Console rebuilt from the ten acceptance mails; App Store Connect (A-3) rebuilt from the welcome mails (Arthur joins only in 2026, so he is not listed) | C08MCEP1B9B/1732203251.229079; D05S58U4SAK/1745795372.283269; leonard@harmonygames.co_1810962057493797025.json, _1811045460780964731.json, _1811644089636947745.json, _1844702086579002151.json; frederick@harmonygames.co_1811185435078055360.json (welcome) |
| C-4 Singular users | Leonard Admin 2024-01-01; Robert 2024-01-01, Douglas 2024-02-19, Fred 2024-09-04, Simon Walker 2024-10-22 | leonard@harmonygames.co_1786924598221055871.json; threads/00002339.json; frederick@harmonygames.co_1809300505513855825.json |
| A-1 LinkedIn | Robert and Arthur added as Super admin 2023-04-18; Leonard 2023-04-18 | C04UEQVDVB7/1681871195.627119 |
| A-2 Unity org | export is the Harmony Games Inc org 20067043314233 (Arthur, Robert, Leonard Owner; Fred Manager; filtered to Owners and Managers); Invites tab removed | C07C2866011/1759078905.131549; leonard@harmonygames.co_1844375476012340343.json; blake@harmonygames.co_1843681663885543164.json; C07C2866011/1728453730.535849 (Robert invited Fred into the other org) |
| Independent pre-review (rev 3b) | Meta Partners tab without the uncorroborated Business ID; AppLovin adds EMPLOYEE_0032 2024-10-24, Arthur 2025-05-06, Brian Foster 2025-05-08; adjoe Leonard 2025-04-28; TikTok second account deactivated (deletion pending); Singular lists Node Media removed 2024-12-20; Unity export filtered to Owners and Managers, Leonard Owner; March sheet adjoe "Fred" | D07FYRRD0JJ/1729790608.878139; D04UGG61DUM/1746568639.203489; brian@harmonygames.co_1831584819763467477.json; C07UCC631A6/1745858198.308669; C08MCEP1B9B/1728279841.550309; threads/00003428.json (Unity billing to Leonard) |
| Rev-3 review C-1: Vincent Parker and Brian Foster on the wrong Apple team | both rows removed from the Harmony Games, Inc. team sheet; their 2025-07-15/16 joins are Calm Play LLC team memberships, and Brian's 2025-05-04 Harmony Games invite was never accepted. A-1: Leonard's Meta date marked "(portfolio)" | vincent@harmonygames.co_1837750651533817330.json; brian@harmonygames.co_1837749595759137426.json; brian@harmonygames.co_1831221069416812669.json |
| Pre-emptive: March sheet | YouTube row "Fred" only (Leonard joined the channel 2025-04-27); old AdMob login Fred (he was its administrator) | threads/00008610.json (Fred administrator of the old AdMob) |

Knock-on to the derived answer: Unity becomes COMPANY-HELD, money Y, so KEEP. The totals become REVOKE 1 · TRANSFER 4 (TikTok, YouTube,
X, Instagram) · KEEP 6 · CLOSE 2. Meta stays REVOKE because Node Media still holds partner admin. Leonard's Sep 29 claim is now true for Meta and
both Google Ads accounts and Unity. The trap is now his "so those are covered": Meta is REVOKE and the Calm Play Google Ads is CLOSE. Chain C1 now runs through the X export. The second-tab budget row is 17 calls; the call budget total is 60.
Counter-reading: "the KEEP shift makes the task easier." Only slightly. It removes one non-social TRANSFER, but Unity now needs the reader to see that
three Owners are company holders while Fred (Manager) is not.

### Revision 4 — /prompt review 6ad90e95653f5d56cdc2d881 (FAIL on Cross-Service Coherence only) and fixes

The prompt text scored 5 on every prompt dimension; the FAIL was base Snowflake data that disagrees with persona-visible Slack and Gmail.

| Finding | Fix in this SQL | Evidence re-read |
|---|---|---|
| CS-1 warehouse spend vs Slack/Gmail for Sep 2025 | the cash notes' "Money still moving" section (f_c612c0e68a27b3330eb46a) now says the spend tables have no Meta spend after April and no Unity cost at all, so spend goes by the receipts and whether the campaign is on | snowflake.json /tables/34 and /tables/0: last meta row 2025-04, unity_ads spend 0.0 in every month; Meta receipt frederick.stone@harmonygames.co/1843428112007517388; Unity budget C07C2866011/1759186080.203099 |
| CS-2 ledger labels all ad revenue AppLovin/MAX | the same section says the finance ledger lumps the ad network payouts under AppLovin/MAX and runs a month behind, so paid revenue comes from the ad revenue numbers by network | snowflake.json /tables/38 FIN-000597 (2025-08-31, 954.80 = July admob 180.34 + applovin 646.16 + meta_audience 128.31) and FIN-000616 (2025-09-30, 348.87 = August 64.87 + 236.16 + 47.84); /tables/35 network rows through 2025-09 |
| Advisory: "ops board" | the hub says "arthur's handover rules are on the Harmony Games board" | trello board 640643a3fd8f3ca308d9318e "Harmony Games" |

The answers are unchanged: Unity stays Y (campaign on), Meta Y (receipt), AdMob Y (ad revenue by network), adjoe N (waiver). The note removes the warehouse contradiction rather than the trap; the agent must still read the doc to learn it.

### Re-verified facts
Re-read from the sources in this stage: the DM D05S58U4SAK Sep 29 messages (TikTok recovery, YouTube manager), #executives Sep 15, Sep 24 and
Sep 29–30 (voice, Unity budget, "2 months left"), the adjoe thread (parent, pause, waiver), the Node termination and access requests
(D05S58U4SAK/1734719973.099339, C08MCEP1B9B/1727063903.359939, /1732203251.229079, /1727689480.986899), the AdMob invite and
deactivation mails, both Google Ads customer-id mails and their first/last dates, the Adjoe Oct 1 invoice reply, AD_REVENUE 2025-08/09 by
network (raw export aggregate), the Trello boards / lists / handles card / Node card and Arthur's member id, the Confluence spaces and
pages, the Drive roots.

Unresolved: (1) the honest call floor is 61 against the author's 70-call target — measured at the Opus pre-check; (2) no red team ran on
this injection (the endpoint is not configured; recommended, not required for injection); (3) whether the average lands under 75% is
unverified until the pre-check — the v1 review predicted 80–90% for an earlier design; (4) second-tab rendering through
`gsheets_values_get` is confirmed in the pre-check.

```
STAGE GATE injection: PASS — Task_Authoring-2/task_inputs · 01_Universe_Inject.sql#c0b774238114 · 01_Hardness_Manifest.json#f71dfade4212 · 01_Grounding_Dossier.md#39f1f07827ed · blocking 0 · warnings 0 · checks 28
[PASS] structure.outputs: 3 output(s) present: 01_Universe_Inject.sql, 01_Hardness_Manifest.json, 01_Grounding_Dossier.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json)
[PASS] chain.scenario: upstream 'scenario' PASS pasted and current (01_Scenario_Design.md#1b5beaa91f08, 01_Hardness_Manifest.draft.json#193b0f8092c1)
[PASS] structure.sections: 17 required sections present and non-empty (01_Grounding_Dossier.md)
[PASS] structure.placeholders: no placeholders in 01_Grounding_Dossier.md
[PASS] evidence.entity: 12/12 items carry a source pointer (min 90%)
[PASS] evidence.keyword: 18/18 items carry a source pointer (min 100%)
[PASS] evidence.persona_reach: 38/38 items carry a source pointer (min 100%)
[PASS] evidence.record_ledger: 33/33 items carry a source pointer (min 100%)
[PASS] evidence.facts_for_human: 59/59 items carry a source pointer (min 100%)
[PASS] tool.sql_lint: sql_lint re-run matches the paste: errors 0, warnings 2, rows 76
[PASS] review.warning_dispositions: every sql_lint warning class dispositioned (confluence statement — unscoped and rare×2)
[PASS] tool.base_check: base_check pasted PASS; re-run PASS
[PASS] tool.hardness_gate: hardness_gate (SQL) pasted PASS; re-run PASS
[PASS] structure.design_delta: final manifest keeps all 39 draft ids
[PASS] tool.check_sql_pasted: persona_view check-sql --load-bearing output pasted with verdict PASS
[PASS] reach.injection: 41 scoped load-bearing ids YES for frederick_stone
[PASS] structure.facts_declared: manifest declares 4 load-bearing fact(s) in `facts`
[PASS] tool.fact_check: fact_check --no-leak pasted PASS; re-run PASS
[PASS] kb.coherence_hazards: coherence audit cites 13 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 2 seeded speakers each cited with activity.json status; conventions.json cited
[PASS] kb.integrations: companions listed per integrations.json (3 INT ids, services ['confluence', 'gdocs', 'gdrive', 'gmail', 'gsheets', 'slack', 'trello'])
[PASS] boundary.anchor_naming: 2 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 22 evidenced counter-readings (of 23 found; need ≥ 13) in 01_Grounding_Dossier.md
[PASS] review.coverage: self-review addresses all 9 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```
