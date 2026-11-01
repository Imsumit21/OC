# Grounding Dossier — fs-paid-ua-trueup (injection v3) · contains no prompt, Oracle Event or criterion text


Persona Frederick Stone <frederick.stone@harmonygames.co> (Co-founder, Executive) · horizon Long Horizon · effective_profile `long` (requester-confirmed
`profile_exception`) · universe date 2025-10-01 (clock 2025-10-01T00:00:00Z, `tools/hg_clock.py`) · difficulty mode Medium.
Generator: `support/task_work/fs_ua_trueup/` (`ids.py` deterministic ids, `texts.py` seeded wording, `model.py` statement / receipt
amounts and the derived register, `gen_sql.py` → `task_inputs/01_Universe_Inject.sql`, `build_manifest.py --final` →
`Working_Files/01_Hardness_Manifest.json`). Every value below cites a record id, a service file + JSON pointer, or an SQL line.


## 1.A Structural

| Table (live schema `references/universe_schema_live.json`) | NOT NULL supplied | Base location + pointer · count | 3 base sample ids | Timestamp format · export → column |
|---|---|---|---|---|
| slack.slack_messages | id ts channel_id type text reply_count reply_users_count is_activity_message reactions_json files_json attachments_json created_at metadata_json | slack/messages/C07C2866011/2025-09.json · 687,230 records | C07C2866011/1758313197.701479 · C07C2866011/1757961037.465799 · C07UCC631A6/1757349668.681539 | ts 10.6 digits; created_at ISO-Z with micro; id = sha256(channel/ts)[:32]; thread_ts → thread_ts_legacy |
| gmail.gmail_threads / gmail.gmail_messages | id thread_id user_email | HarmonyGames_Gmail/Services_Data/gmail/threads/*.json · 88,726 threads / 104,480 messages | frederick.stone@harmonygames.co/1843428112007517388 · frederick.stone@harmonygames.co/1830999337380347892 · frederick.stone@harmonygames.co/1839175088393392199 | date ISO-Z, internal_date ms = date; labelIds → label_ids_json; to/cc strings → to_json/cc_json lists; Message-ID in headers_json |
| gcal.gcal_events | event_id calendar_id | gcal/data.json /events · 11,233 | evt_7934d6c78f843013d5d676 · evt_89381fe5a15b802c5652a9 · evt_9fc9ee9622ce63c8d04ed6 | start/end {dateTime: …Z}; one row per attendee calendar, self:true on the owner; ical_uid 32hex@hg4 |
| gdrive.drive_files | id name mime_type | gdrive/data.json /drive_files · 53,866 | d_63fffeb4fab5233ed5bb73 · d_175c0d7bc72ed244b944cb · f_05bedd1540d3e01a90ab16 | modified_time/created_time ISO-Z; shared_with_emails → shared_with_emails_json; owners → owners_json; parents → parents_json |
| gdocs.docs_documents | document_id title | gdocs/data.json /docs_documents · 633 | f_af99b76ff4da59a710edba · f_1be142fdb7a3bfe62f534b · f_00117462881159eceee63e | drive_file_id = document_id; sharing identical to the drive row; revision_id 10 hex |
| gsheets.sheets_spreadsheets / sheets_sheets | spreadsheet_id title / spreadsheet_id sheet_id title | gsheets/data.json /sheets_spreadsheets · 398 (1,553 tabs) | f_00c30de5acd0cf7656c140 · f_00e7008444923e0fe1549c · f_0272f7ef3096043049e9f6 | grid_json 2-D array of str/int/float; sheet_id 0..N-1 |
| contacts.contacts | contact_id first_name last_name | contacts/contacts.json /contacts · 171 (103 token emails, 0 literal external emails) | 655f2fd84c2100fcc45498a1 · 48415476a62c0c1390a7caf9 · d4a339f7f6aafffdc2dabb9a | external people as PERSON_nnnn / PERSON_nnnn_EMAIL tokens, last_name '' |
| confluence.confluence_pages / page_versions | id space_id title body body_format status version created_at updated_at / id page_id number title body created_at | confluence/confluence_working.json /pages · 31, /page_versions · 78 | page_eng_home · page_prod_home · page_analytics_dashboards | varchar ISO-Z; version row 1 per new page (ver_ + 32 hex) |
| linear.linear_comments / linear_issues | id issue_id author_id body is_edited created_at updated_at | linear/data.json /comments · 0 (base), /issues | ENG-2362 · ENG-2361 · ZOM-672 | varchar ISO-Z; comments render through linear_list_comments (Ask_Carriers §6b) |
| trello.trello_cards / trello_actions / trello_boards | id name idBoard idList / id type date | trello/data.json /cards (UA/BD: 40) /actions (UA/BD: 155) /boards | 67c9f58eac1f6b4b5fd3ca73 · 67cf1b506d78ad3c72e02a35 · 67bdf3d8722c229e32622f50 | ids: first 8 hex = Unix seconds; badges → badges_json; data → data_json |


Snowflake is read, not injected: `snowflake.json /tables/0` (ANALYTICS.MARKETING.AD_SPEND_DAILY, 2,590 rows), `/tables/38`
(FINANCE.EXPENSES.FINANCE_LEDGER). GitHub and Slides carry no task record.

## 1.B Entity table

| Entity | Canonical spelling / id | Services (cited) | Value per service | Agreement |
|---|---|---|---|---|
| Leonard Hayes | leonard.hayes@harmonygames.co · EMPLOYEE_0038_SLACK_ID · PERSON_6094_TRELLO_USER_ID · usr_63fffeb4fab5233e | slack C07C2866011/1758313197.701479; trello PERSON_6094_TRELLO_USER_ID; linear ENG-2362 creator | CEO / co-founder; runs the bridge | AGREE |
| Frederick Stone (persona) | frederick.stone@harmonygames.co · EMPLOYEE_0008_SLACK_ID · 4b4a68fc0fec0b254e4f9d8e · user_EMPLOYEE_0008 | slack C07C2866011/1757961037.465799; gmail frederick.stone@harmonygames.co/1813530307529968502 | UA owner ("VP of Marketing" in the Unity ticket) | AGREE (Contacts job differs: S06, excluded) |
| Robert | robert@harmonygames.co · EMPLOYEE_0016_SLACK_ID | slack C07C2866011/1758738920.866139 | co-founder; non-authoritative reply | AGREE |
| Simon Walker | simon.walker@harmonygames.co · usr_eac7fcafa75e4935 · user_STAFF_2 | slack C5ADCB1B7C35/1754064507.032439; confluence user_STAFF_2 | analytics / data engineer | AGREE |
| Meta ad account | Account ID [IDENTIFIER_3125] (907669287942378 in headers) | gmail frederick.stone@harmonygames.co/1843428112007517388; seeded f_4591ef30be4f920ba1ed14 | receipts in Frederick's, Leonard's and Robert's mailboxes | AGREE; Frederick's copies completed by two seeded copies (§S2) |
| Unity — HG account | [SOURCE_ORG_0001] Games Inc ("our real account") | gmail frederick.stone@harmonygames.co/1813530307529968502; seeded STMT 2024-10 … 2025-04 | Domino Delights Oct 2024 – Apr 2025 | AGREE |
| Unity — Calm Play account | Calm Play LLC, Unity org 20067043314233 | slack C07C2866011/1747847918.209079, C07C2866011/1759078905.131549; gmail frederick.stone@harmonygames.co/1839175088393392199 | Zombie Match 3D May – Sep 2025; $1,673.43 stranded Oct 2024 | DISAGREE (designed): support thread calls it the old alpha account; H2 scope includes it (T22) |
| Adjoe | SVC_2836_EMAIL; subjects redact as [USERNAME_14101] | gmail frederick.stone@harmonygames.co/1830999337380347892; slack C07UCC631A6/1757349668.681539 | Apr/May/Jun invoices; Sep campaign not billable | AGREE |
| Outside accountant | PERSON_6098 / PERSON_6098_EMAIL (minted, next free after PERSON_6097) | seeded contacts 049f5555b01fd07b0f9d673c; d_b563e7f1e1608c4d36f3b0, f_0cd1e1402e8052d3d4e903 sharing | viewer on the data room folder and Q4 pack | AGREE |
| Zombie Match 3D / Puzzles vs Zombies / PvZ | zombie_match_3d | confluence page_analytics_dashboards (store name Puzzles vs Zombies); seeded briefs B10 – B12 | one title, three names (trap_catalog K02) | AGREE (alias listed for the human) |
| Domino Delights / Domino Adventures listing | domino_delights | gmail frederick.stone@harmonygames.co/1813530307529968502 (Domino Adventures deprecated); seeded briefs B05 B06 B08 | ADV campaigns = DD on the Domino Adventures store listing | AGREE (T11) |
| ENG-2362 | Implement Deep Link + Campaign Tracking via Singular | linear/data.json /issues ENG-2362 (Todo, created 2025-06-03T05:07:43Z) | cited by page_singular_cost_connectors | AGREE |

## 1.C Voice and realism (speakers, activity, conventions)

| Seeded speaker | activity.json status_at_clock | 3 base messages (quoted) | Length / hours (conventions.json) | Seeded text |
|---|---|---|---|---|
| Leonard Hayes leonard.hayes@harmonygames.co (EMPLOYEE_0038_SLACK_ID) | activity: active_sep_2025 | "I set the budget for Unity campaign to a $1 instead of turning them off completely" (C07C2866011/1758313197.701479); "Fb spend is like $20/day so I’m just gonna let it run for now" (C07C2866011/1758313330.170339); "do you mind turning on iOS Unity retention campaigns?" (C07C2866011/1759184893.748959) | slack.per_person_hours_and_style: p50 47 / p90 133 / p99 689 chars, UTC core 15–02, 50% lower-case starts | hub 20:14Z, amendment 18:05Z (lower-case), Sep 19 mail 22:20Z, K7 comment 18:30Z, H2 doc, packs |
| Robert robert@harmonygames.co (EMPLOYEE_0016_SLACK_ID) | activity: active_sep_2025 | "Just quote Adjoe users" (C07C2866011/1758738920.866139); "Does Apple still let us customize our meta keywords?" (C07C2866011/1758148765.757839); "Also calling BS. I played 8 levels in…" (C07C2866011/1758838629.445759) | p50 42 / p90 121; UTC core 16–04 | one 96-char reply 20:41Z |
| Frederick Stone frederick.stone@harmonygames.co (EMPLOYEE_0008_SLACK_ID) | activity: active_sep_2025 | "So we need two buckets of UA spend…" (C07C2866011/1757961037.465799); "Playable should be expensed to the real UA bucket…" (C07C2866011/1757961129.250809); "Both Unity campaigns (phone and tablet) capped out today…" (C07C2866011/1758060268.307769) | p50 73 / p90 183; UTC core 15–01 | H1 card 17:20Z, DD card 16:05Z, 18 briefs ~17:xxZ, 25 statements (saved 17:xx–22:30Z), DD page |
| Simon Walker simon.walker@harmonygames.co (EMPLOYEE_0037_SLACK_ID) | activity: active_sep_2025 | "On the backend how it works is • Firebase assigns…" (C5ADCB1B7C35/1754064507.032439); "On 0.3.86 the user_id is missing for a lot of players…" (C5ADCB1B7C35/1754072727.080349); "About 50% are missing it on their first begin_level s on .89" (C5ADCB1B7C35/1754073299.820529) | p50 71 / p90 332; UTC core 15–23 | connector page 16:20Z, ENG-2362 comment 17:42Z |


External automated senders follow base tokens: Meta receipts SVC_0521_NAME/SVC_0521_EMAIL with reply-to SVC_0177 (base
frederick.stone@harmonygames.co/1843428112007517388); Adjoe SVC_2836_EMAIL (base frederick.stone@harmonygames.co/1830999337380347892);
Unity: no seeded Unity sender mail. Base "Receipt from Unity Ads" mails (SVC_0231) go to Leonard only (e.g. leonard.hayes@harmonygames.co/1843071417603742140); the six seeded top-up mails are Leonard's forwards of six of them to Frederick, same amounts and org (fixes /injection advisories 1–2). Gmail subjects: base receipt subject
verbatim; internal subject "data room UA numbers" (20 chars, conventions.json gmail.internal_subject_len_chars p25–p50).
Calendar: 30 min (conventions.json gcal.duration_min median 30). Receipt bodies copy the base layout (\r\n, NBSP before USD,
narrow NBSP before AM/PM, "Campaign: NAMEResults: N (Impressions) Amount: $x").

## 1.D Keyword / findability (base hit counts via `tools/hg.py search search <svc> <term> --limit 200`)

| Term | Service | Base hits + pointer | Seeded records / note |
|---|---|---|---|
| "UA spend buckets" | trello | 0 base hit(s) (scan_complete) | NEW TERM — introduced in trello 68c99c40e5d9eb6f3a988838 + 6807be2c1ea290e4382b33be; confluence page_ua_spend_buckets, reached via A1 C07C2866011/1759176840.271025 |
| "UA spend buckets" | confluence | 0 base hit(s) (scan_complete) | NEW TERM — introduced in trello 68c99c40e5d9eb6f3a988838 + 6807be2c1ea290e4382b33be; confluence page_ua_spend_buckets, reached via A1 C07C2866011/1759176840.271025 |
| "true-up" | trello | 0 base hit(s) (scan_complete) | NEW TERM — introduced in trello 68dae1bc8ec7eb683dc15a8d; slack C07C2866011/1759176840.271025 ("true-up card"), reached via A1 C07C2866011/1759176840.271025 |
| "Paid UA close rules" | gdocs | 0 base hit(s) (scan_complete) | NEW TERM — introduced in gdocs f_4591ef30be4f920ba1ed14, reached via A1 C07C2866011/1759176840.271025 |
| "close rules" | gdocs | 0 base hit(s) (scan_complete) | NEW TERM — introduced in gdocs f_4591ef30be4f920ba1ed14; slack C07C2866011/1759176840.271025, reached via A1 C07C2866011/1759176840.271025 |
| "Q4 Board Pack" | gsheets | 0 base hit(s) (scan_complete) | NEW TERM — introduced in gsheets f_0cd1e1402e8052d3d4e903, reached via A1 C07C2866011/1759176840.271025 |
| "Board Pack" | gsheets | 0 base hit(s) (scan_complete) | NEW TERM — introduced in gsheets f_0cd1e1402e8052d3d4e903, f_9f7fb3ec09a20b2b6aa6da, reached via A1 C07C2866011/1759176840.271025 |
| "Data Room" | gdrive | 0 base hit(s) (scan_complete) | NEW TERM — introduced in gdrive d_b563e7f1e1608c4d36f3b0, d_e4fc39bd54316ab8653b4b, reached via A1 C07C2866011/1759176840.271025 |
| "UA test brief" | gdrive | 0 base hit(s) (scan_complete) | NEW TERM — introduced in gdrive d_6930b716ea5b1457adb4a4 + 18 briefs, reached via A1 C07C2866011/1759176840.271025 |
| "Unity Ads statement" | gdrive | 0 base hit(s) (scan_complete) | NEW TERM — introduced in gdrive/gsheets d_3885933a334aef16e40e84 + 25 statements, reached via A1 C07C2866011/1759176840.271025 |
| "UA statements" | gdrive | 0 base hit(s) (scan_complete) | NEW TERM — introduced in gdrive d_3885933a334aef16e40e84, reached via A1 C07C2866011/1759176840.271025 |
| "Singular cost connectors" | confluence | 0 base hit(s) (scan_complete) | NEW TERM — introduced in confluence page_singular_cost_connectors, reached via A1 C07C2866011/1759176840.271025 |
| "Singular" | confluence | 23 base hit(s) (scan_complete), first confluence_working.json /pages/1/body | confluence page_singular_cost_connectors; linear cmt_6b4787a755ac66787e8c |
| "UA bucket review" | gcal | 0 base hit(s) (scan_complete) | NEW TERM — introduced in gcal evt_2f9b60002516e45ff04160; gmail invitation, reached via A1 C07C2866011/1759176840.271025 |
| "accountant" | contacts | 0 base hit(s) (scan_complete) | NEW TERM — introduced in contacts 049f5555b01fd07b0f9d673c, reached via A1 C07C2866011/1759176840.271025 |
| "Receipt from Unity Ads" | gmail | 57 base hit(s) (scan_complete), first threads/00002874.json /messages/0/subject | gmail 6 seeded forwards (base receipts in Leonard's mailbox) |
| "Calm Play" | gmail | 200 base hit(s) (scan incomplete — proves nothing), first threads/00000487.json /messages/0/body | gdocs f_4591ef30be4f920ba1ed14; 18 Calm Play statements |
| "ads receipt" | gmail | 200 base hit(s) (scan incomplete — proves nothing), first threads/00002921.json /messages/0/subject | gmail 17 seeded + 2 copies |
| "meta Invoice" | gmail | 121 base hit(s) (scan_complete), first threads/00000282.json /messages/0/headers/17/value | none seeded |
| "true-up" | slack | 0 base hit(s) (scan_complete) | NEW TERM — introduced in trello 68dae1bc8ec7eb683dc15a8d; slack C07C2866011/1759176840.271025 ("true-up card"), reached via A1 C07C2866011/1759176840.271025 |
| "data room" | slack | 12 base hit(s) (scan_complete), first messages/C04RSEB8K0W/2023-03.json /479/text | slack C07C2866011/1759176840.271025 |
| "buckets" | slack | 111 base hit(s) (scan_complete), first messages/C04S28HSD0U/2023-03.json /471/text | slack C07C2866011/1759176840.271025 |
| "Singular" | linear | 22 base hit(s) (scan_complete), first data.json /issues/1712/title | confluence page_singular_cost_connectors; linear cmt_6b4787a755ac66787e8c |
| "data room UA numbers" | gmail | 0 base hit(s) (scan_complete) | NEW TERM — introduced in gmail frederick.stone@harmonygames.co/1843732571750494737, reached via A1 C07C2866011/1759176840.271025 |
| "DD incent" | trello | 0 base hit(s) (scan_complete) | NEW TERM — introduced in trello 6807be2c1ea290e4382b33be, reached via A1 C07C2866011/1759176840.271025 |
| "Unity Ads statement" | gsheets | 0 base hit(s) (scan_complete) | NEW TERM — introduced in gdrive/gsheets d_3885933a334aef16e40e84 + 25 statements, reached via A1 C07C2866011/1759176840.271025 |

## 1.E Persona reach (scoped records)

| Record | Service | Visibility path | Load-bearing |
|---|---|---|---|
| C07C2866011/1759176840.271025 | slack | member of private #executives C07C2866011 | LB |
| C07C2866011/1759255500.938286 | slack | same channel, thread reply | LB |
| C07C2866011/1759178460.557708 | slack | same channel, thread reply | LB |
| frederick.stone@harmonygames.co/1843732571750494737 | gmail | own mailbox, INBOX | LB |
| f_4591ef30be4f920ba1ed14 | gdocs | shared_with_emails_json includes the persona | LB |
| f_0cd1e1402e8052d3d4e903 | gsheets | shared with the persona | LB |
| f_9f7fb3ec09a20b2b6aa6da | gsheets | shared with the persona | LB |
| d_b563e7f1e1608c4d36f3b0 | gdrive | shared with the persona | LB |
| d_6930b716ea5b1457adb4a4 | gdrive | owned by the persona | LB |
| d_3885933a334aef16e40e84 | gdrive | owned by the persona | LB |
| evt_2f9b60002516e45ff04160 | gcal | persona's calendar, self:true | LB |
| frederick.stone@harmonygames.co/1830999337380347892 | gmail | own mailbox, INBOX (base thread + 2 seeded) | LB |
| frederick.stone@harmonygames.co/1842010914816895400 | gmail | own mailbox, INBOX | LB |
| frederick.stone@harmonygames.co/1843154072371887815 | gmail | own mailbox, INBOX | LB |
| frederick.stone@harmonygames.co/1843244480594183249 | gmail | own mailbox, INBOX | LB |
| frederick.stone@harmonygames.co/1843516837725026041 | gmail | own mailbox, INBOX | LB |
| frederick.stone@harmonygames.co/1843606994289346111 | gmail | own mailbox, INBOX | LB |
| frederick.stone@harmonygames.co/1843697905828235234 | gmail | own mailbox, INBOX | LB |
| frederick.stone@harmonygames.co/1843788314050589285 | gmail | own mailbox, INBOX | LB |
| frederick.stone@harmonygames.co/1843878722273509005 | gmail | own mailbox, INBOX | LB |
| frederick.stone@harmonygames.co/1843969633812798247 | gmail | own mailbox, INBOX | LB |
| frederick.stone@harmonygames.co/1844059853292161439 | gmail | own mailbox, INBOX | LB |
| frederick.stone@harmonygames.co/1844150953574592539 | gmail | own mailbox, INBOX | LB |
| frederick.stone@harmonygames.co/1844241235968886522 | gmail | own mailbox, INBOX | LB |
| frederick.stone@harmonygames.co/1844331958763627407 | gmail | own mailbox, INBOX | LB |
| frederick.stone@harmonygames.co/1844422366986338173 | gmail | own mailbox, INBOX | LB |
| frederick.stone@harmonygames.co/1844513089782197590 | gmail | own mailbox, INBOX | LB |
| frederick.stone@harmonygames.co/1844603498005085849 | gmail | own mailbox, INBOX | LB |
| frederick.stone@harmonygames.co/1844734171545827192 | gmail | own mailbox, INBOX | LB |
| frederick.stone@harmonygames.co/1831357377414065699 | gmail | own mailbox, INBOX (seeded copy) | LB |
| frederick.stone@harmonygames.co/1834164376568289766 | gmail | own mailbox, INBOX (seeded copy) | LB |
| frederick.stone@harmonygames.co/1813907358352348391 | gmail | own mailbox, INBOX (top-up) | LB |
| frederick.stone@harmonygames.co/1819366895124967091 | gmail | own mailbox, INBOX (top-up) | LB |
| frederick.stone@harmonygames.co/1832753288970947639 | gmail | own mailbox, INBOX (top-up) | LB |
| frederick.stone@harmonygames.co/1834226118820623605 | gmail | own mailbox, INBOX (top-up) | LB |
| frederick.stone@harmonygames.co/1838650711081025746 | gmail | own mailbox, INBOX (top-up) | LB |
| frederick.stone@harmonygames.co/1843072786759807900 | gmail | own mailbox, INBOX (top-up) | LB |
| f_6d0c2209baa3ff54633836 | gdocs | owned by the persona (brief B01) | LB |
| f_a5e0147cfc1fba7a9c7349 | gdocs | owned by the persona (brief B02) | LB |
| f_206c42f98afd5fcbd0461a | gdocs | owned by the persona (brief B03) | LB |
| f_5edcf4c37a67ee2561e9e4 | gdocs | owned by the persona (brief B04) | LB |
| f_cc0200cda2a03d6f444916 | gdocs | owned by the persona (brief B05) | LB |
| f_f017eafb1e59601f888460 | gdocs | owned by the persona (brief B06) | LB |
| f_c37d51b92f6c34b520fd73 | gdocs | owned by the persona (brief B07) | LB |
| f_50ffc8312fcfd96d096754 | gdocs | owned by the persona (brief B08) | LB |
| f_9e4be4822ec79ce7ff5d17 | gdocs | owned by the persona (brief B09) | LB |
| f_42ba151c4158922854572a | gdocs | owned by the persona (brief B10) | LB |
| f_a12749c3f0cea9d44061d9 | gdocs | owned by the persona (brief B11) | LB |
| f_298721fb6cb960d796fcbb | gdocs | owned by the persona (brief B12) | LB |
| f_3d2795c2623a50864b2764 | gdocs | owned by the persona (brief B13) | LB |
| f_0a5638d43dd053ed974e21 | gdocs | owned by the persona (brief B14) | LB |
| f_6dcaecd8cb0bdbbb18b945 | gdocs | owned by the persona (brief B15) | LB |
| f_0d60db1d5b484c5afd9792 | gdocs | owned by the persona (brief B16) | LB |
| f_cb32548a078870d1d80dca | gdocs | owned by the persona (brief B17) | LB |
| f_887def6eed0e1b022f7ab0 | gdocs | owned by the persona (brief B18) | LB |
| f_c34b364c50bf4ed59ae6ce | gsheets | owned by the persona (statement 2024-10) | LB |
| f_41bc63b2332620eb08b80a | gsheets | owned by the persona (statement 2024-11) | LB |
| f_4a6e3125ed715725161c86 | gsheets | owned by the persona (statement 2024-12) | LB |
| f_6c15d48fa95f0739fc42da | gsheets | owned by the persona (statement 2025-01) | LB |
| f_f57990a3307dea5aa0af0f | gsheets | owned by the persona (statement 2025-02) | LB |
| f_a4942fdb8f8530b1cc93e0 | gsheets | owned by the persona (statement 2025-03) | LB |
| f_ad44496a3e89c11de71d81 | gsheets | owned by the persona (statement 2025-04) | LB |
| f_1311b8c998f28831b1cf43 | gsheets | owned by the persona (statement cp-2025-04) | LB |
| f_f7564f9413e650dd90cb74 | gsheets | owned by the persona (statement 2025-05) | LB |
| f_66d70cbc162e336d8d9074 | gsheets | owned by the persona (statement 2025-06-01..07) | LB |
| f_26f69b46d45852fb515912 | gsheets | owned by the persona (statement 2025-06-08..14) | LB |
| f_a278aec0da8fbd8f7cd86d | gsheets | owned by the persona (statement 2025-06-15..21) | LB |
| f_3cdb6026a369e505609c3e | gsheets | owned by the persona (statement 2025-06-22..30) | LB |
| f_e923eb578c12cd3aa2b1ff | gsheets | owned by the persona (statement 2025-07-01..07) | LB |
| f_1a3c4303fe9b70a0c5d725 | gsheets | owned by the persona (statement 2025-07-08..14) | LB |
| f_ac8e62864ae33cf47aef61 | gsheets | owned by the persona (statement 2025-07-15..21) | LB |
| f_9a825acb7a3b71cfff45d0 | gsheets | owned by the persona (statement 2025-07-22..31) | LB |
| f_389e010ecc827029d9cdcf | gsheets | owned by the persona (statement 2025-08-01..07) | LB |
| f_057df7adc2e2c887bf9f6f | gsheets | owned by the persona (statement 2025-08-08..14) | LB |
| f_e68b1465f0e0fa85fe2a9a | gsheets | owned by the persona (statement 2025-08-15..21) | LB |
| f_19c380c11615388ff75ce8 | gsheets | owned by the persona (statement 2025-08-22..31) | LB |
| f_e8f75f70da75c40e9d395e | gsheets | owned by the persona (statement 2025-09-01..07) | LB |
| f_09666ca5c83c6a319ece41 | gsheets | owned by the persona (statement 2025-09-08..14) | LB |
| f_76007a5c131f92019df2a0 | gsheets | owned by the persona (statement 2025-09-15..21) | LB |
| f_0c302b9a0529823a0c6209 | gsheets | owned by the persona (statement 2025-09-22..29) | LB |
| C07C2866011/1757961037.465799 | slack | base; member of #executives | LB |
| C07C2866011/1757961129.250809 | slack | base; member of #executives | LB |
| C07C2866011/1758060268.307769 | slack | base; member of #executives | LB |
| C07C2866011/1758313197.701479 | slack | base; member of #executives | LB |
| C07C2866011/1758313330.170339 | slack | base; member of #executives | LB |
| C07C2866011/1757689941.099589 | slack | base; member of #executives | LB |
| C07UCC631A6/1757345931.336429 | slack | base; member of adjoe channel C07UCC631A6 | LB |
| C07UCC631A6/1757346020.196019 | slack | base; member of adjoe channel C07UCC631A6 | LB |
| C07UCC631A6/1757348929.625759 | slack | base; member of adjoe channel C07UCC631A6 | LB |
| C07UCC631A6/1757349668.681539 | slack | base; member of adjoe channel C07UCC631A6 | LB |
| frederick.stone@harmonygames.co/1812262106647207041 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1812839883787768319 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1813049887158875039 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1813379281814151196 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1813460395597065111 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1813570677525296798 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1813727496096729809 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1813825423889664563 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1813904811482385587 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1814042565503776727 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1814211514242959315 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1814959634472648361 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1815692691136620637 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1815861152183775926 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1816079268118375341 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1816331182428132431 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1816920350286580043 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1817043264479181246 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1817180294730550227 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1817681870046929356 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1819776649300869905 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1819888664949792853 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1820007110310927242 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1820132039739740641 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1820486398663099282 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1828481095554769555 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1828641403961142838 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1828942627030969352 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1830495542195061363 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1831122183306732471 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1831236341456877471 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1831376708658054054 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1835778053085762169 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1836836899676941724 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1836905421544429882 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1837801002582336665 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1839693762261954189 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1843428112007517388 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1830999337380347892 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1833810978786310481 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1836438286741039931 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1836528865848810632 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1839518563856917373 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1839175088393392199 | gmail | base; own mailbox | LB |
| frederick.stone@harmonygames.co/1813530307529968502 | gmail | base; own mailbox | LB |
| f_af99b76ff4da59a710edba | gdocs | base; shared with the persona | LB |


Other-mailbox copies the SQL also writes (Leonard's and Arthur's copies of the Sep 19 mail, Leonard's copies of the top-ups and of
the Adjoe contest / credit) are realism copies, never load-bearing; check-sql lists them as NO, as expected. Unscoped records
(Trello, Confluence, Linear, Contacts, Snowflake) need no reach proof. No designed denials (`denied_probes: []`).

`python3 Task_Authoring/tools/persona_view.py check-sql frederick_stone Task_Authoring/task_inputs/01_Universe_Inject.sql --load-bearing <138 ids>`:


```
CHECK-SQL as frederick_stone <frederick.stone@harmonygames.co>
[YES LB] L2 slack.slack_messages insert cd3b1de999ccac1658fa4d0610029f32, C07C2866011/1759176840.271025 - persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES LB] L11 slack.slack_messages insert 6e575abab02d9126badc05e21cc8ba34, C07C2866011/1759178460.557708 - persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES LB] L13 slack.slack_messages insert a4a53eadd0c3a8df945d1eb9d94fe041, C07C2866011/1759255500.938286 - persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[NO] L15 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1843732571750794917 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L19 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAPBs_a7zkwB142iJWh0uGhyL-PG_jggPqaEWc1aINhqFjKBVco@mail.gm - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] L21 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843732571750494737 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L23 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAPBs_a7zkwB142iJWh0uGhyL-PG_jggPqaEWc1aINhqFjKBVco@mail. - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L25 gmail.gmail_threads insert arthur.blake@harmonygames.co/1843732571751030319 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L27 gmail.gmail_messages insert arthur.blake@harmonygames.co/<CAPBs_a7zkwB142iJWh0uGhyL-PG_jggPqaEWc1aINhqFjKBVco@mail.gma - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] L29 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842010914816895400 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L31 gmail.gmail_messages insert frederick.stone@harmonygames.co/<15fa478b-a312-4368-a84d-577a6aa7885a@support.facebook.com - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L33 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843154072371887815 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L35 gmail.gmail_messages insert frederick.stone@harmonygames.co/<ea10aaa6-a5a6-4fb1-a2ff-ca27d6d09deb@support.facebook.com - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L37 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843244480594183249 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L39 gmail.gmail_messages insert frederick.stone@harmonygames.co/<e52f9241-0084-4436-a397-0bb4a9c221a2@support.facebook.com - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L41 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843516837725026041 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L43 gmail.gmail_messages insert frederick.stone@harmonygames.co/<11cbfaec-8b57-4b9f-a425-163b41445ff1@support.facebook.com - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L45 gmail.gmail_messages insert frederick.stone@harmonygames.co/<9df8418c-7834-4abc-a5d1-0e389a9df275@support.facebook.com - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L47 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843606994289346111 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L49 gmail.gmail_messages insert frederick.stone@harmonygames.co/<22a70908-ad5d-4852-a902-4e0ce880ba0c@support.facebook.com - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L51 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843697905828235234 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L53 gmail.gmail_messages insert frederick.stone@harmonygames.co/<7f0f2b0a-8299-451a-a010-87ba8638556d@support.facebook.com - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L55 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843788314050589285 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L57 gmail.gmail_messages insert frederick.stone@harmonygames.co/<c685ee06-9f4b-4331-abd7-061f4fbe9a0f@support.facebook.com - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L59 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843878722273509005 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L61 gmail.gmail_messages insert frederick.stone@harmonygames.co/<9ca34d7a-79d6-4cc0-a29a-55098f9a700c@support.facebook.com - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L63 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843969633812798247 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L65 gmail.gmail_messages insert frederick.stone@harmonygames.co/<934f94ff-202b-4fa2-a87e-ef0ccee2682c@support.facebook.com - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L67 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844059853292161439 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L69 gmail.gmail_messages insert frederick.stone@harmonygames.co/<69610acb-e972-4adc-a3fe-35b3062891ee@support.facebook.com - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L71 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844150953574592539 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L73 gmail.gmail_messages insert frederick.stone@harmonygames.co/<b0e74723-744f-4bf7-a4b3-60982ea72766@support.facebook.com - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L75 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844241235968886522 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L77 gmail.gmail_messages insert frederick.stone@harmonygames.co/<c5daebb4-5408-4a6a-ab93-2fc65764666a@support.facebook.com - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L79 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844331958763627407 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L81 gmail.gmail_messages insert frederick.stone@harmonygames.co/<e6f13b60-9087-4c32-a2e3-ec7e376fb4f9@support.facebook.com - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L83 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844422366986338173 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L85 gmail.gmail_messages insert frederick.stone@harmonygames.co/<140e6d17-2ae9-4082-a211-845eee901657@support.facebook.com - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L87 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844513089782197590 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L89 gmail.gmail_messages insert frederick.stone@harmonygames.co/<d9f7f2c3-7004-4d5f-aa95-c0492d5ec0f7@support.facebook.com - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L91 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844603498005085849 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L93 gmail.gmail_messages insert frederick.stone@harmonygames.co/<30914d8f-c10f-481a-a1c4-a4f2c0529857@support.facebook.com - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L95 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844734171545827192 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L97 gmail.gmail_messages insert frederick.stone@harmonygames.co/<44c21a7d-dafb-4a55-a9ed-64d80f1cfba1@support.facebook.com - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L99 gmail.gmail_threads insert frederick.stone@harmonygames.co/1831357377414065699 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L101 gmail.gmail_messages insert frederick.stone@harmonygames.co/<2cc2aa61-2baf-40de-af8a-a3ccd4e5cec6@support.facebook.com - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L103 gmail.gmail_threads insert frederick.stone@harmonygames.co/1834164376568289766 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L105 gmail.gmail_messages insert frederick.stone@harmonygames.co/<9a17576b-c417-450c-a3c5-2f7ba33ed844@support.facebook.com - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L107 gmail.gmail_threads insert frederick.stone@harmonygames.co/1813907358352348391 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L109 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAPBs_a78U55VbWi4kaCCYxqVH-9f525a7dpfWUOMx-FgzmOpeA@mail. - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L111 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1813907358352084792 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L113 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAPBs_a78U55VbWi4kaCCYxqVH-9f525a7dpfWUOMx-FgzmOpeA@mail.gm - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] L115 gmail.gmail_threads insert frederick.stone@harmonygames.co/1819366895124967091 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L117 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAPBs_a7dusyzQ9wSsBdExO-Brp9vGziPtX5tsWGdWCy2dy3B3Q@mail. - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L119 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1819366895125158359 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L121 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAPBs_a7dusyzQ9wSsBdExO-Brp9vGziPtX5tsWGdWCy2dy3B3Q@mail.gm - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] L123 gmail.gmail_threads insert frederick.stone@harmonygames.co/1832753288970947639 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L125 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAPBs_a7rMNxEXiHy3-GiHKmfXPs-S_2o5iwW204S0xkEG3QYEk@mail. - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L127 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1832753288971239246 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L129 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAPBs_a7rMNxEXiHy3-GiHKmfXPs-S_2o5iwW204S0xkEG3QYEk@mail.gm - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] L131 gmail.gmail_threads insert frederick.stone@harmonygames.co/1834226118820623605 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L133 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAPBs_a7v09ehCzLneG1Sne7cCusp-sv_JOdIK8kRBZHGKn4Zlw@mail. - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L135 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1834226118820193922 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L137 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAPBs_a7v09ehCzLneG1Sne7cCusp-sv_JOdIK8kRBZHGKn4Zlw@mail.gm - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] L139 gmail.gmail_threads insert frederick.stone@harmonygames.co/1838650711081025746 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L141 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAPBs_a7EA0sZoNzaJQSdpgPiVVYG_X0eLCxNKo60xYJOydxXVQ@mail. - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L143 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1838650711081024837 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L145 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAPBs_a7EA0sZoNzaJQSdpgPiVVYG_X0eLCxNKo60xYJOydxXVQ@mail.gm - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] L147 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843072786759807900 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L149 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAPBs_a7HznCoq5yzyS0oaqT1orOp1tj1T3tyqQGdVJJaUM6QaA@mail. - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L151 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1843072786759901225 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L153 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAPBs_a7HznCoq5yzyS0oaqT1orOp1tj1T3tyqQGdVJJaUM6QaA@mail.gm - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] L155 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAPBs_a7tLJ57UFdsCW9u4oM1rRsxY66g4dAx0j84aZj-yzbcn4@mail. - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L157 gmail.gmail_messages insert frederick.stone@harmonygames.co/<01070196aa042300-6aa1f6b0-e3bd-4749-aee8-249ca19c3e2f-000 - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L159 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAPBs_a7tLJ57UFdsCW9u4oM1rRsxY66g4dAx0j84aZj-yzbcn4@mail.gm - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L161 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<01070196aa042300-6aa1f6b0-e3bd-4749-aee8-249ca19c3e2f-00000 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES] L163 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843554523545665376 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L165 gmail.gmail_messages insert frederick.stone@harmonygames.co/<calendar-516760ef-5ed5-4697-a0b7-7779bb9ba7f5@google.com> - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L167 gcal.gcal_events insert evt_e7678efc99ce316f728f5d - persona is an attendee and holds its own copy evt_2f9b60002516e45ff04160 (same ical_uid and start) on frederick.stone@harmonygames.co
[YES LB] L171 gcal.gcal_events insert evt_2f9b60002516e45ff04160 - event is on the persona's own calendar frederick.stone@harmonygames.co
[YES LB] L177 gdrive.drive_files insert d_b563e7f1e1608c4d36f3b0 - file is shared with the persona (shared_with_emails)
[YES] L181 gdrive.drive_files insert d_e4fc39bd54316ab8653b4b - file is shared with the persona (shared_with_emails)
[YES LB] L183 gdrive.drive_files insert d_6930b716ea5b1457adb4a4 - persona owns the file
[YES LB] L185 gdrive.drive_files insert d_3885933a334aef16e40e84 - persona owns the file
[YES LB] L187 gdrive.drive_files insert f_4591ef30be4f920ba1ed14 - file is shared with the persona (shared_with_emails)
[YES LB] L189 gdocs.docs_documents insert f_4591ef30be4f920ba1ed14 - file is shared with the persona (shared_with_emails)
[YES LB] L191 gdrive.drive_files insert f_0cd1e1402e8052d3d4e903 - file is shared with the persona (shared_with_emails)
[YES LB] L193 gsheets.sheets_spreadsheets insert f_0cd1e1402e8052d3d4e903 - file is shared with the persona (shared_with_emails)
[YES LB] L195 gsheets.sheets_sheets insert f_0cd1e1402e8052d3d4e903, f_0cd1e1402e8052d3d4e903#0 - file is shared with the persona (shared_with_emails)
[YES LB] L197 gsheets.sheets_sheets insert f_0cd1e1402e8052d3d4e903, f_0cd1e1402e8052d3d4e903#1 - file is shared with the persona (shared_with_emails)
[YES LB] L199 gsheets.sheets_sheets insert f_0cd1e1402e8052d3d4e903, f_0cd1e1402e8052d3d4e903#2 - file is shared with the persona (shared_with_emails)
[YES LB] L201 gdrive.drive_files insert f_9f7fb3ec09a20b2b6aa6da - file is shared with the persona (shared_with_emails)
[YES LB] L203 gsheets.sheets_spreadsheets insert f_9f7fb3ec09a20b2b6aa6da - file is shared with the persona (shared_with_emails)
[YES LB] L205 gsheets.sheets_sheets insert f_9f7fb3ec09a20b2b6aa6da, f_9f7fb3ec09a20b2b6aa6da#0 - file is shared with the persona (shared_with_emails)
[YES LB] L207 gsheets.sheets_sheets insert f_9f7fb3ec09a20b2b6aa6da, f_9f7fb3ec09a20b2b6aa6da#1 - file is shared with the persona (shared_with_emails)
[YES LB] L209 gdrive.drive_files insert f_6d0c2209baa3ff54633836 - persona owns the file
[YES LB] L211 gdocs.docs_documents insert f_6d0c2209baa3ff54633836 - persona owns the file
[YES LB] L213 gdrive.drive_files insert f_a5e0147cfc1fba7a9c7349 - persona owns the file
[YES LB] L215 gdocs.docs_documents insert f_a5e0147cfc1fba7a9c7349 - persona owns the file
[YES LB] L217 gdrive.drive_files insert f_206c42f98afd5fcbd0461a - persona owns the file
[YES LB] L219 gdocs.docs_documents insert f_206c42f98afd5fcbd0461a - persona owns the file
[YES LB] L221 gdrive.drive_files insert f_5edcf4c37a67ee2561e9e4 - persona owns the file
[YES LB] L223 gdocs.docs_documents insert f_5edcf4c37a67ee2561e9e4 - persona owns the file
[YES LB] L225 gdrive.drive_files insert f_cc0200cda2a03d6f444916 - persona owns the file
[YES LB] L227 gdocs.docs_documents insert f_cc0200cda2a03d6f444916 - persona owns the file
[YES LB] L229 gdrive.drive_files insert f_f017eafb1e59601f888460 - persona owns the file
[YES LB] L231 gdocs.docs_documents insert f_f017eafb1e59601f888460 - persona owns the file
[YES LB] L233 gdrive.drive_files insert f_c37d51b92f6c34b520fd73 - persona owns the file
[YES LB] L235 gdocs.docs_documents insert f_c37d51b92f6c34b520fd73 - persona owns the file
[YES LB] L237 gdrive.drive_files insert f_50ffc8312fcfd96d096754 - persona owns the file
[YES LB] L239 gdocs.docs_documents insert f_50ffc8312fcfd96d096754 - persona owns the file
[YES LB] L241 gdrive.drive_files insert f_9e4be4822ec79ce7ff5d17 - persona owns the file
[YES LB] L243 gdocs.docs_documents insert f_9e4be4822ec79ce7ff5d17 - persona owns the file
[YES LB] L245 gdrive.drive_files insert f_42ba151c4158922854572a - persona owns the file
[YES LB] L247 gdocs.docs_documents insert f_42ba151c4158922854572a - persona owns the file
[YES LB] L249 gdrive.drive_files insert f_a12749c3f0cea9d44061d9 - persona owns the file
[YES LB] L251 gdocs.docs_documents insert f_a12749c3f0cea9d44061d9 - persona owns the file
[YES LB] L253 gdrive.drive_files insert f_298721fb6cb960d796fcbb - persona owns the file
[YES LB] L255 gdocs.docs_documents insert f_298721fb6cb960d796fcbb - persona owns the file
[YES LB] L257 gdrive.drive_files insert f_3d2795c2623a50864b2764 - persona owns the file
[YES LB] L259 gdocs.docs_documents insert f_3d2795c2623a50864b2764 - persona owns the file
[YES LB] L261 gdrive.drive_files insert f_0a5638d43dd053ed974e21 - persona owns the file
[YES LB] L263 gdocs.docs_documents insert f_0a5638d43dd053ed974e21 - persona owns the file
[YES LB] L265 gdrive.drive_files insert f_6dcaecd8cb0bdbbb18b945 - persona owns the file
[YES LB] L267 gdocs.docs_documents insert f_6dcaecd8cb0bdbbb18b945 - persona owns the file
[YES LB] L269 gdrive.drive_files insert f_0d60db1d5b484c5afd9792 - persona owns the file
[YES LB] L271 gdocs.docs_documents insert f_0d60db1d5b484c5afd9792 - persona owns the file
[YES LB] L273 gdrive.drive_files insert f_cb32548a078870d1d80dca - persona owns the file
[YES LB] L275 gdocs.docs_documents insert f_cb32548a078870d1d80dca - persona owns the file
[YES LB] L277 gdrive.drive_files insert f_887def6eed0e1b022f7ab0 - persona owns the file
[YES LB] L279 gdocs.docs_documents insert f_887def6eed0e1b022f7ab0 - persona owns the file
[YES LB] L281 gdrive.drive_files insert f_c34b364c50bf4ed59ae6ce - persona owns the file
[YES LB] L283 gsheets.sheets_spreadsheets insert f_c34b364c50bf4ed59ae6ce - persona owns the file
[YES LB] L285 gsheets.sheets_sheets insert f_c34b364c50bf4ed59ae6ce, f_c34b364c50bf4ed59ae6ce#0 - persona owns the file
[YES LB] L287 gdrive.drive_files insert f_41bc63b2332620eb08b80a - persona owns the file
[YES LB] L289 gsheets.sheets_spreadsheets insert f_41bc63b2332620eb08b80a - persona owns the file
[YES LB] L291 gsheets.sheets_sheets insert f_41bc63b2332620eb08b80a, f_41bc63b2332620eb08b80a#0 - persona owns the file
[YES LB] L293 gdrive.drive_files insert f_4a6e3125ed715725161c86 - persona owns the file
[YES LB] L295 gsheets.sheets_spreadsheets insert f_4a6e3125ed715725161c86 - persona owns the file
[YES LB] L297 gsheets.sheets_sheets insert f_4a6e3125ed715725161c86, f_4a6e3125ed715725161c86#0 - persona owns the file
[YES LB] L299 gdrive.drive_files insert f_6c15d48fa95f0739fc42da - persona owns the file
[YES LB] L301 gsheets.sheets_spreadsheets insert f_6c15d48fa95f0739fc42da - persona owns the file
[YES LB] L303 gsheets.sheets_sheets insert f_6c15d48fa95f0739fc42da, f_6c15d48fa95f0739fc42da#0 - persona owns the file
[YES LB] L305 gdrive.drive_files insert f_f57990a3307dea5aa0af0f - persona owns the file
[YES LB] L307 gsheets.sheets_spreadsheets insert f_f57990a3307dea5aa0af0f - persona owns the file
[YES LB] L309 gsheets.sheets_sheets insert f_f57990a3307dea5aa0af0f, f_f57990a3307dea5aa0af0f#0 - persona owns the file
[YES LB] L311 gdrive.drive_files insert f_a4942fdb8f8530b1cc93e0 - persona owns the file
[YES LB] L313 gsheets.sheets_spreadsheets insert f_a4942fdb8f8530b1cc93e0 - persona owns the file
[YES LB] L315 gsheets.sheets_sheets insert f_a4942fdb8f8530b1cc93e0, f_a4942fdb8f8530b1cc93e0#0 - persona owns the file
[YES LB] L317 gdrive.drive_files insert f_ad44496a3e89c11de71d81 - persona owns the file
[YES LB] L319 gsheets.sheets_spreadsheets insert f_ad44496a3e89c11de71d81 - persona owns the file
[YES LB] L321 gsheets.sheets_sheets insert f_ad44496a3e89c11de71d81, f_ad44496a3e89c11de71d81#0 - persona owns the file
[YES LB] L323 gdrive.drive_files insert f_1311b8c998f28831b1cf43 - persona owns the file
[YES LB] L325 gsheets.sheets_spreadsheets insert f_1311b8c998f28831b1cf43 - persona owns the file
[YES LB] L327 gsheets.sheets_sheets insert f_1311b8c998f28831b1cf43, f_1311b8c998f28831b1cf43#0 - persona owns the file
[YES LB] L329 gdrive.drive_files insert f_f7564f9413e650dd90cb74 - persona owns the file
[YES LB] L331 gsheets.sheets_spreadsheets insert f_f7564f9413e650dd90cb74 - persona owns the file
[YES LB] L333 gsheets.sheets_sheets insert f_f7564f9413e650dd90cb74, f_f7564f9413e650dd90cb74#0 - persona owns the file
[YES LB] L335 gdrive.drive_files insert f_66d70cbc162e336d8d9074 - persona owns the file
[YES LB] L337 gsheets.sheets_spreadsheets insert f_66d70cbc162e336d8d9074 - persona owns the file
[YES LB] L339 gsheets.sheets_sheets insert f_66d70cbc162e336d8d9074, f_66d70cbc162e336d8d9074#0 - persona owns the file
[YES LB] L341 gdrive.drive_files insert f_26f69b46d45852fb515912 - persona owns the file
[YES LB] L343 gsheets.sheets_spreadsheets insert f_26f69b46d45852fb515912 - persona owns the file
[YES LB] L345 gsheets.sheets_sheets insert f_26f69b46d45852fb515912, f_26f69b46d45852fb515912#0 - persona owns the file
[YES LB] L347 gdrive.drive_files insert f_a278aec0da8fbd8f7cd86d - persona owns the file
[YES LB] L349 gsheets.sheets_spreadsheets insert f_a278aec0da8fbd8f7cd86d - persona owns the file
[YES LB] L351 gsheets.sheets_sheets insert f_a278aec0da8fbd8f7cd86d, f_a278aec0da8fbd8f7cd86d#0 - persona owns the file
[YES LB] L353 gdrive.drive_files insert f_3cdb6026a369e505609c3e - persona owns the file
[YES LB] L355 gsheets.sheets_spreadsheets insert f_3cdb6026a369e505609c3e - persona owns the file
[YES LB] L357 gsheets.sheets_sheets insert f_3cdb6026a369e505609c3e, f_3cdb6026a369e505609c3e#0 - persona owns the file
[YES LB] L359 gdrive.drive_files insert f_e923eb578c12cd3aa2b1ff - persona owns the file
[YES LB] L361 gsheets.sheets_spreadsheets insert f_e923eb578c12cd3aa2b1ff - persona owns the file
[YES LB] L363 gsheets.sheets_sheets insert f_e923eb578c12cd3aa2b1ff, f_e923eb578c12cd3aa2b1ff#0 - persona owns the file
[YES LB] L365 gdrive.drive_files insert f_1a3c4303fe9b70a0c5d725 - persona owns the file
[YES LB] L367 gsheets.sheets_spreadsheets insert f_1a3c4303fe9b70a0c5d725 - persona owns the file
[YES LB] L369 gsheets.sheets_sheets insert f_1a3c4303fe9b70a0c5d725, f_1a3c4303fe9b70a0c5d725#0 - persona owns the file
[YES LB] L371 gdrive.drive_files insert f_ac8e62864ae33cf47aef61 - persona owns the file
[YES LB] L373 gsheets.sheets_spreadsheets insert f_ac8e62864ae33cf47aef61 - persona owns the file
[YES LB] L375 gsheets.sheets_sheets insert f_ac8e62864ae33cf47aef61, f_ac8e62864ae33cf47aef61#0 - persona owns the file
[YES LB] L377 gdrive.drive_files insert f_9a825acb7a3b71cfff45d0 - persona owns the file
[YES LB] L379 gsheets.sheets_spreadsheets insert f_9a825acb7a3b71cfff45d0 - persona owns the file
[YES LB] L381 gsheets.sheets_sheets insert f_9a825acb7a3b71cfff45d0, f_9a825acb7a3b71cfff45d0#0 - persona owns the file
[YES LB] L383 gdrive.drive_files insert f_389e010ecc827029d9cdcf - persona owns the file
[YES LB] L385 gsheets.sheets_spreadsheets insert f_389e010ecc827029d9cdcf - persona owns the file
[YES LB] L387 gsheets.sheets_sheets insert f_389e010ecc827029d9cdcf, f_389e010ecc827029d9cdcf#0 - persona owns the file
[YES LB] L389 gdrive.drive_files insert f_057df7adc2e2c887bf9f6f - persona owns the file
[YES LB] L391 gsheets.sheets_spreadsheets insert f_057df7adc2e2c887bf9f6f - persona owns the file
[YES LB] L393 gsheets.sheets_sheets insert f_057df7adc2e2c887bf9f6f, f_057df7adc2e2c887bf9f6f#0 - persona owns the file
[YES LB] L395 gdrive.drive_files insert f_e68b1465f0e0fa85fe2a9a - persona owns the file
[YES LB] L397 gsheets.sheets_spreadsheets insert f_e68b1465f0e0fa85fe2a9a - persona owns the file
[YES LB] L399 gsheets.sheets_sheets insert f_e68b1465f0e0fa85fe2a9a, f_e68b1465f0e0fa85fe2a9a#0 - persona owns the file
[YES LB] L401 gdrive.drive_files insert f_19c380c11615388ff75ce8 - persona owns the file
[YES LB] L403 gsheets.sheets_spreadsheets insert f_19c380c11615388ff75ce8 - persona owns the file
[YES LB] L405 gsheets.sheets_sheets insert f_19c380c11615388ff75ce8, f_19c380c11615388ff75ce8#0 - persona owns the file
[YES LB] L407 gdrive.drive_files insert f_e8f75f70da75c40e9d395e - persona owns the file
[YES LB] L409 gsheets.sheets_spreadsheets insert f_e8f75f70da75c40e9d395e - persona owns the file
[YES LB] L411 gsheets.sheets_sheets insert f_e8f75f70da75c40e9d395e, f_e8f75f70da75c40e9d395e#0 - persona owns the file
[YES LB] L413 gdrive.drive_files insert f_09666ca5c83c6a319ece41 - persona owns the file
[YES LB] L415 gsheets.sheets_spreadsheets insert f_09666ca5c83c6a319ece41 - persona owns the file
[YES LB] L417 gsheets.sheets_sheets insert f_09666ca5c83c6a319ece41, f_09666ca5c83c6a319ece41#0 - persona owns the file
[YES LB] L419 gdrive.drive_files insert f_76007a5c131f92019df2a0 - persona owns the file
[YES LB] L421 gsheets.sheets_spreadsheets insert f_76007a5c131f92019df2a0 - persona owns the file
[YES LB] L423 gsheets.sheets_sheets insert f_76007a5c131f92019df2a0, f_76007a5c131f92019df2a0#0 - persona owns the file
[YES LB] L425 gdrive.drive_files insert f_0c302b9a0529823a0c6209 - persona owns the file
[YES LB] L427 gsheets.sheets_spreadsheets insert f_0c302b9a0529823a0c6209 - persona owns the file
[YES LB] L429 gsheets.sheets_sheets insert f_0c302b9a0529823a0c6209, f_0c302b9a0529823a0c6209#0 - persona owns the file
[YES LB] base slack C07C2866011/1757689941.099589 - base record: message inherits channel: persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES LB] base slack C07C2866011/1757961037.465799 - base record: message inherits channel: persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES LB] base slack C07C2866011/1757961129.250809 - base record: message inherits channel: persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES LB] base slack C07C2866011/1758060268.307769 - base record: message inherits channel: persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES LB] base slack C07C2866011/1758313197.701479 - base record: message inherits channel: persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES LB] base slack C07C2866011/1758313330.170339 - base record: message inherits channel: persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES LB] base slack C07UCC631A6/1757345931.336429 - base record: message inherits channel: persona EMPLOYEE_0008_SLACK_ID is in members of private adjoe-[SOURCE_ORG_0001]
[YES LB] base slack C07UCC631A6/1757346020.196019 - base record: message inherits channel: persona EMPLOYEE_0008_SLACK_ID is in members of private adjoe-[SOURCE_ORG_0001]
[YES LB] base slack C07UCC631A6/1757348929.625759 - base record: thread reply inherits channel: persona EMPLOYEE_0008_SLACK_ID is in members of private adjoe-[SOURCE_ORG_0001]
[YES LB] base slack C07UCC631A6/1757349668.681539 - base record: thread reply inherits channel: persona EMPLOYEE_0008_SLACK_ID is in members of private adjoe-[SOURCE_ORG_0001]
[YES LB] base gdrive f_af99b76ff4da59a710edba - base record: file is shared with the persona (shared_with_emails)
[YES LB] base gmail frederick.stone@harmonygames.co/1812262106647207041 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1812839883787768319 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1813049887158875039 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1813379281814151196 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1813460395597065111 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1813530307529968502 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1813570677525296798 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1813727496096729809 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1813825423889664563 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1813904811482385587 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1814042565503776727 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1814211514242959315 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1814959634472648361 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1815692691136620637 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1815861152183775926 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1816079268118375341 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1816331182428132431 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1816920350286580043 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1817043264479181246 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1817180294730550227 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1817681870046929356 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1819776649300869905 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1819888664949792853 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1820007110310927242 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1820132039739740641 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1820486398663099282 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1828481095554769555 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1828641403961142838 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1828942627030969352 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1830495542195061363 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1831122183306732471 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1831236341456877471 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1831376708658054054 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1833810978786310481 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1835778053085762169 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1836438286741039931 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1836528865848810632 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1836836899676941724 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1836905421544429882 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1837801002582336665 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1839175088393392199 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1839518563856917373 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1839693762261954189 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1842698832158940633 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1843224116132323892 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1843428112007517388 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co

summary: {'YES': 188, 'NO': 18}  unscoped rows (always visible): 15
  gcal.gcal_events: {'YES': 2}
  gdocs.docs_documents: {'YES': 19}
  gdrive.drive_files: {'YES': 50}
  gmail.gmail_messages: {'NO': 10, 'YES': 30}
  gmail.gmail_threads: {'NO': 8, 'YES': 27}
  gsheets.sheets_sheets: {'YES': 30}
  gsheets.sheets_spreadsheets: {'YES': 27}
  slack.slack_messages: {'YES': 3}
verdict: PASS (0 load-bearing rows not visible)
```

## 1.F Collision checks

Identity tokens first: header tokens minted for new external parties —
PERSON_6098 (the accountant; max used PERSON_6097) — and transaction tokens [IDENTIFIER_52803] … [IDENTIFIER_52819] (max used
IDENTIFIER_52802): 0 hits in a full token sweep of HarmonyGames_Gmail, HarmonyGames_Other_Services and HarmonyGames_GitHub
(21,119 distinct PERSON/IDENTIFIER/TAX_ID/SVC tokens). Reference numbers are literal 10-character values in the base shape
(e.g. LSPRPTLFY2 in frederick.stone@harmonygames.co/1836836899676941724); the two copied receipts reuse the base charge's own
[TAX_ID_5752]/[IDENTIFIER_13354] and [TAX_ID_11451]/[IDENTIFIER_25984] (same charge, another mailbox).

Minted record ids (`hg.py search lookup <svc> --ids-file <json> --file <collection> --pointer <array> --key <id>`, plus the
Slack shard and Gmail filename / Message-ID sweeps):

```
('gdrive.drive_files', 50, True, 0, ['matches', 'files_selected', 'files_completed', 'records_checked', 'errors', 'scan_complete', 'persona_filtered', 'scope'])
('gdocs.docs_documents', 19, True, 0, ['matches', 'files_selected', 'files_completed', 'records_checked', 'errors', 'scan_complete', 'persona_filtered', 'scope'])
('gsheets.sheets_spreadsheets', 27, True, 0, ['matches', 'files_selected', 'files_completed', 'records_checked', 'errors', 'scan_complete', 'persona_filtered', 'scope'])
('gcal.gcal_events', 2, True, 0, ['matches', 'files_selected', 'files_completed', 'records_checked', 'errors', 'scan_complete', 'persona_filtered', 'scope'])
('contacts.contacts', 1, True, 0, ['matches', 'files_selected', 'files_completed', 'records_checked', 'errors', 'scan_complete', 'persona_filtered', 'scope'])
('confluence.confluence_pages', 2, True, 0, ['matches', 'files_selected', 'files_completed', 'records_checked', 'errors', 'scan_complete', 'persona_filtered', 'scope'])
('confluence.confluence_page_versions', 2, True, 0, ['matches', 'files_selected', 'files_completed', 'records_checked', 'errors', 'scan_complete', 'persona_filtered', 'scope'])
('linear.linear_comments', 1, True, 0, ['matches', 'files_selected', 'files_completed', 'records_checked', 'errors', 'scan_complete', 'persona_filtered', 'scope'])
('trello.trello_cards', 3, True, 0, ['matches', 'files_selected', 'files_completed', 'records_checked', 'errors', 'scan_complete', 'persona_filtered', 'scope'])
('trello.trello_actions', 4, True, 0, ['matches', 'files_selected', 'files_completed', 'records_checked', 'errors', 'scan_complete', 'persona_filtered', 'scope'])
('slack (C07C2866011 2025-09 shard)', [False, False, False])
('gmail thread files', 35, 'hits', 0, 'none')
('gmail message-id grep hits', 0, 'none')
```

`base_check.py` Check A re-tests uniqueness of every minted id against the full collections (PASS, §Self-review).

## 2 Record ledger

| # | Service | Table | Record id | Manifest element | Carrier | Reach path | Discovery role |
|---|---|---|---|---|---|---|---|
| 1 | slack | slack.slack_messages | C07C2866011/1759176840.271025 | A1 hub; K1 K2 K3 K4 K10 K16; T8 | ● | member of #executives | first link (anchor) |
| 2 | slack | slack.slack_messages | C07C2866011/1759178460.557708 | T13 distractor | ● | member of #executives | decoy |
| 3 | slack | slack.slack_messages | C07C2866011/1759255500.938286 | K6 amendment; T6 v3 | ● | member of #executives | overturning evidence |
| 4 | gmail | gmail.gmail_messages | frederick.stone@harmonygames.co/1843732571750494737 | H2 decoy (superseded v1); T6 v1 | ● | own mailbox (INBOX) | claim met first |
| 5 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1842010914816895400 | cohort; T17 neighbour | ● | own mailbox (INBOX) | late-August charge (Aug 31 3:15 PM PT) |
| 6 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1843154072371887815 | cohort | ● | own mailbox (INBOX) | per-record evidence |
| 7 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1843244480594183249 | cohort | ● | own mailbox (INBOX) | per-record evidence |
| 8 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1843516837725026041 | cohort; T4 duplicate | ● | own mailbox (INBOX) | per-record evidence |
| 9 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1843606994289346111 | cohort | ● | own mailbox (INBOX) | per-record evidence |
| 10 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1843697905828235234 | cohort | ● | own mailbox (INBOX) | per-record evidence |
| 11 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1843788314050589285 | cohort; C5 credit-funded | ● | own mailbox (INBOX) | per-record evidence |
| 12 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1843878722273509005 | cohort; T18 v2 | ● | own mailbox (INBOX) | per-record evidence |
| 13 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1843969633812798247 | cohort | ● | own mailbox (INBOX) | per-record evidence |
| 14 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1844059853292161439 | cohort | ● | own mailbox (INBOX) | per-record evidence |
| 15 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1844150953574592539 | cohort | ● | own mailbox (INBOX) | per-record evidence |
| 16 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1844241235968886522 | cohort | ● | own mailbox (INBOX) | per-record evidence |
| 17 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1844331958763627407 | cohort | ● | own mailbox (INBOX) | per-record evidence |
| 18 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1844422366986338173 | cohort | ● | own mailbox (INBOX) | per-record evidence |
| 19 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1844513089782197590 | cohort | ● | own mailbox (INBOX) | per-record evidence |
| 20 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1844603498005085849 | cohort | ● | own mailbox (INBOX) | per-record evidence |
| 21 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1844734171545827192 | cohort; T12 window edge | ● | own mailbox (INBOX) | boundary charge (Sep 30 4:40 PM PT = 23:40Z, before the freeze) |
| 22 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1831357377414065699 | cohort (copy of base leonard.hayes@harmonygames.co/1831357378751331011) | ● | own mailbox (INBOX) | per-record evidence |
| 23 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1834164376568289766 | cohort (copy of base leonard.hayes@harmonygames.co/1834164377682810022) | ● | own mailbox (INBOX) | per-record evidence |
| 24 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1813907358352348391 | T20 top-up (not spend), forward of base leonard.hayes@harmonygames.co/1813905959739132963 | ● | own mailbox (INBOX) | decoy |
| 25 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1819366895124967091 | T20 top-up (not spend), forward of base leonard.hayes@harmonygames.co/1819365478614689094 | ● | own mailbox (INBOX) | decoy |
| 26 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1832753288970947639 | T20 top-up (not spend), forward of base leonard.hayes@harmonygames.co/1832751922831494579 | ● | own mailbox (INBOX) | decoy |
| 27 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1834226118820623605 | T20 top-up (not spend), forward of base leonard.hayes@harmonygames.co/1834225959907530709 | ● | own mailbox (INBOX) | decoy |
| 28 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1838650711081025746 | T20 top-up (not spend), forward of base leonard.hayes@harmonygames.co/1838649409811811442 | ● | own mailbox (INBOX) | decoy |
| 29 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1843072786759807900 | T20 top-up (not spend), forward of base leonard.hayes@harmonygames.co/1843071417603742140; C5 | ● | own mailbox (INBOX) | decoy |
| 30 | gmail | gmail.gmail_messages | frederick.stone@harmonygames.co/1830999337380347892 | K17; C7 hop 2; T21 v2 (contest) | ● | own mailbox (INBOX) | evidence |
| 31 | gmail | gmail.gmail_messages | frederick.stone@harmonygames.co/1830999337380347892 | K17; C7 hop 3; T21 v2 (credit $1,271.40) | ● | own mailbox (INBOX) | overturning evidence |
| 32 | gmail | gmail.gmail_threads | frederick.stone@harmonygames.co/1843554523545665376 | INT-11 companion of evt_2f9b60002516e45ff04160 | ● | own mailbox (INBOX) | alternate path |
| 33 | gcal | gcal.gcal_events | evt_2f9b60002516e45ff04160 | K8; C6 hop 3; T7 v2 (review day Sep 18) | ● start | own calendar (self:true) | authority date |
| 34 | contacts | contacts.contacts | 049f5555b01fd07b0f9d673c | K9 recipient | ● email | unscoped | write target (recipient) |
| 35 | gdrive | gdrive.drive_files | d_b563e7f1e1608c4d36f3b0 | K10 destination folder | ● folder | shared with persona | destination |
| 36 | gdrive | gdrive.drive_files | d_e4fc39bd54316ab8653b4b | lookalike folder (trap_catalog D01) | ● folder | shared with persona | decoy |
| 37 | gdrive | gdrive.drive_files | d_6930b716ea5b1457adb4a4 | H4 / K5 folder | ● folder | owned by persona | authority home |
| 38 | gdrive | gdrive.drive_files | d_3885933a334aef16e40e84 | K13 folder | ● folder | owned by persona | evidence home |
| 39 | gdocs | gdocs.docs_documents | f_4591ef30be4f920ba1ed14 | H2 authority; K2 K5 K9 K11 K13 K14 K15 K17; T6 v2 | ● body_text | shared with persona | authority |
| 40 | gsheets | gsheets.sheets_spreadsheets | f_0cd1e1402e8052d3d4e903 | H3 destination; K4 header Marketing!A1:H1; T16 v2; write W1 | ● grid | shared with persona | write target |
| 41 | gsheets | gsheets.sheets_spreadsheets | f_9f7fb3ec09a20b2b6aa6da | H3 decoy; T16 v1 | ● grid | shared with persona | decoy |
| 42 | gdocs | gdocs.docs_documents | f_6d0c2209baa3ff54633836 | H4 / K5 brief B01 | ● body_text | owned by persona | authority (per-record) |
| 43 | gdocs | gdocs.docs_documents | f_a5e0147cfc1fba7a9c7349 | H4 / K5 brief B02 | ● body_text | owned by persona | authority (per-record) |
| 44 | gdocs | gdocs.docs_documents | f_206c42f98afd5fcbd0461a | H4 / K5 brief B03 | ● body_text | owned by persona | authority (per-record) |
| 45 | gdocs | gdocs.docs_documents | f_5edcf4c37a67ee2561e9e4 | H4 / K5 brief B04 | ● body_text | owned by persona | authority (per-record) |
| 46 | gdocs | gdocs.docs_documents | f_cc0200cda2a03d6f444916 | H4 / K5 brief B05 (T11) | ● body_text | owned by persona | authority (per-record) |
| 47 | gdocs | gdocs.docs_documents | f_f017eafb1e59601f888460 | H4 / K5 brief B06 (T11) | ● body_text | owned by persona | authority (per-record) |
| 48 | gdocs | gdocs.docs_documents | f_c37d51b92f6c34b520fd73 | H4 / K5 brief B07 (T11) | ● body_text | owned by persona | authority (per-record) |
| 49 | gdocs | gdocs.docs_documents | f_50ffc8312fcfd96d096754 | H4 / K5 brief B08 (T11) | ● body_text | owned by persona | authority (per-record) |
| 50 | gdocs | gdocs.docs_documents | f_9e4be4822ec79ce7ff5d17 | H4 / K5 brief B09 | ● body_text | owned by persona | authority (per-record) |
| 51 | gdocs | gdocs.docs_documents | f_42ba151c4158922854572a | H4 / K5 brief B10 | ● body_text | owned by persona | authority (per-record) |
| 52 | gdocs | gdocs.docs_documents | f_a12749c3f0cea9d44061d9 | H4 / K5 brief B11 | ● body_text | owned by persona | authority (per-record) |
| 53 | gdocs | gdocs.docs_documents | f_298721fb6cb960d796fcbb | H4 / K5 brief B12 | ● body_text | owned by persona | authority (per-record) |
| 54 | gdocs | gdocs.docs_documents | f_3d2795c2623a50864b2764 | H4 / K5 brief B13 | ● body_text | owned by persona | authority (per-record) |
| 55 | gdocs | gdocs.docs_documents | f_0a5638d43dd053ed974e21 | H4 / K5 brief B14 | ● body_text | owned by persona | authority (per-record) |
| 56 | gdocs | gdocs.docs_documents | f_6dcaecd8cb0bdbbb18b945 | H4 / K5 brief B15 | ● body_text | owned by persona | authority (per-record) |
| 57 | gdocs | gdocs.docs_documents | f_0d60db1d5b484c5afd9792 | H4 / K5 brief B16 | ● body_text | owned by persona | authority (per-record) |
| 58 | gdocs | gdocs.docs_documents | f_cb32548a078870d1d80dca | H4 / K5 brief B17 | ● body_text | owned by persona | authority (per-record) |
| 59 | gdocs | gdocs.docs_documents | f_887def6eed0e1b022f7ab0 | H4 / K5 brief B18 | ● body_text | owned by persona | authority (per-record) |
| 60 | gsheets | gsheets.sheets_spreadsheets | f_c34b364c50bf4ed59ae6ce | K13 statement 2024-10 | ● grid | owned by persona | per-record evidence |
| 61 | gsheets | gsheets.sheets_spreadsheets | f_41bc63b2332620eb08b80a | K13 statement 2024-11 | ● grid | owned by persona | per-record evidence |
| 62 | gsheets | gsheets.sheets_spreadsheets | f_4a6e3125ed715725161c86 | K13 statement 2024-12 | ● grid | owned by persona | per-record evidence |
| 63 | gsheets | gsheets.sheets_spreadsheets | f_6c15d48fa95f0739fc42da | K13 statement 2025-01 | ● grid | owned by persona | per-record evidence |
| 64 | gsheets | gsheets.sheets_spreadsheets | f_f57990a3307dea5aa0af0f | K13 statement 2025-02 | ● grid | owned by persona | per-record evidence |
| 65 | gsheets | gsheets.sheets_spreadsheets | f_a4942fdb8f8530b1cc93e0 | K13 statement 2025-03 | ● grid | owned by persona | per-record evidence |
| 66 | gsheets | gsheets.sheets_spreadsheets | f_ad44496a3e89c11de71d81 | K13 statement 2025-04 | ● grid | owned by persona | per-record evidence |
| 67 | gsheets | gsheets.sheets_spreadsheets | f_1311b8c998f28831b1cf43 | K13 statement cp-2025-04 | ● grid | owned by persona | per-record evidence |
| 68 | gsheets | gsheets.sheets_spreadsheets | f_f7564f9413e650dd90cb74 | K13 statement 2025-05 | ● grid | owned by persona | per-record evidence |
| 69 | gsheets | gsheets.sheets_spreadsheets | f_66d70cbc162e336d8d9074 | K13 statement 2025-06-01..07 | ● grid | owned by persona | per-record evidence |
| 70 | gsheets | gsheets.sheets_spreadsheets | f_26f69b46d45852fb515912 | K13 statement 2025-06-08..14 | ● grid | owned by persona | per-record evidence |
| 71 | gsheets | gsheets.sheets_spreadsheets | f_a278aec0da8fbd8f7cd86d | K13 statement 2025-06-15..21 | ● grid | owned by persona | per-record evidence |
| 72 | gsheets | gsheets.sheets_spreadsheets | f_3cdb6026a369e505609c3e | K13 statement 2025-06-22..30 | ● grid | owned by persona | per-record evidence |
| 73 | gsheets | gsheets.sheets_spreadsheets | f_e923eb578c12cd3aa2b1ff | K13 statement 2025-07-01..07 | ● grid | owned by persona | per-record evidence |
| 74 | gsheets | gsheets.sheets_spreadsheets | f_1a3c4303fe9b70a0c5d725 | K13 statement 2025-07-08..14 (C2 hop 3; T9) | ● grid | owned by persona | per-record evidence |
| 75 | gsheets | gsheets.sheets_spreadsheets | f_ac8e62864ae33cf47aef61 | K13 statement 2025-07-15..21 | ● grid | owned by persona | per-record evidence |
| 76 | gsheets | gsheets.sheets_spreadsheets | f_9a825acb7a3b71cfff45d0 | K13 statement 2025-07-22..31 | ● grid | owned by persona | per-record evidence |
| 77 | gsheets | gsheets.sheets_spreadsheets | f_389e010ecc827029d9cdcf | K13 statement 2025-08-01..07 | ● grid | owned by persona | per-record evidence |
| 78 | gsheets | gsheets.sheets_spreadsheets | f_057df7adc2e2c887bf9f6f | K13 statement 2025-08-08..14 | ● grid | owned by persona | per-record evidence |
| 79 | gsheets | gsheets.sheets_spreadsheets | f_e68b1465f0e0fa85fe2a9a | K13 statement 2025-08-15..21 | ● grid | owned by persona | per-record evidence |
| 80 | gsheets | gsheets.sheets_spreadsheets | f_19c380c11615388ff75ce8 | K13 statement 2025-08-22..31 | ● grid | owned by persona | per-record evidence |
| 81 | gsheets | gsheets.sheets_spreadsheets | f_e8f75f70da75c40e9d395e | K13 statement 2025-09-01..07 | ● grid | owned by persona | per-record evidence |
| 82 | gsheets | gsheets.sheets_spreadsheets | f_09666ca5c83c6a319ece41 | K13 statement 2025-09-08..14 | ● grid | owned by persona | per-record evidence |
| 83 | gsheets | gsheets.sheets_spreadsheets | f_76007a5c131f92019df2a0 | K13 statement 2025-09-15..21 (T19) | ● grid | owned by persona | per-record evidence |
| 84 | gsheets | gsheets.sheets_spreadsheets | f_0c302b9a0529823a0c6209 | K13 statement 2025-09-22..29 | ● grid | owned by persona | per-record evidence |
| 85 | confluence | confluence.confluence_pages | page_singular_cost_connectors | K11; C2 hop 1 | ● body | unscoped | evidence (explains the gaps) |
| 86 | confluence | confluence.confluence_pages | page_ua_spend_buckets | H1 decoy; T14 | ● body | unscoped | decoy |
| 87 | linear | linear.linear_comments | cmt_6b4787a755ac66787e8c | K12; C2 hop 2 | ● comment (§6b) | unscoped | evidence |
| 88 | linear | linear.linear_issues | ENG-2362 | companion: updated_at = newest comment | — | unscoped | companion |
| 89 | trello | trello.trello_cards | 6807be2c1ea290e4382b33be | H1 decoy (same board, DD scope); T14 | ● desc | unscoped | decoy |
| 90 | trello | trello.trello_cards | 68c99c40e5d9eb6f3a988838 | H1 authority; K3; C6 hop 1; T7 v1 | ● desc | unscoped | authority |
| 91 | trello | trello.trello_actions | 68d195a805df8c30c455f99c | K7 amendment; C6 hop 2; T7 v3 | ● commentCard | unscoped | overturning evidence |
| 92 | trello | trello.trello_cards | 68dae1bc8ec7eb683dc15a8d | K16 destination; T15; write W4 | ● desc | unscoped | write target |
| 93 | trello | trello.trello_boards | 66da196af476ab78deaa0cef | companion: board dateLastActivity | — | unscoped | companion |


Ledger rows carry the record each manifest element points to; child rows written with them (message rows under each listed
thread, tab rows under each spreadsheet, the drive row of every Doc/Sheet, version rows of each Confluence page, createCard actions,
Leonard's / Arthur's mailbox copies) belong to the listed record. Totals from `sql_lint.py`: 219 INSERT + 2 UPDATE over 10 schemas.

## 3 Findability and discovery-order proofs

| Record | Agent's likely query | Term present (pointer) | Competing base hits / how reached | Chain position |
|---|---|---|---|---|
| C07C2866011/1759176840.271025 | Slack #executives history / search "data room" | "data room", "true-up card" in the hub | the persona is @-mentioned; latest #executives activity before the clock | first link (A1) |
| C07C2866011/1759255500.938286 | the hub thread replies | "one change to the doc" | reply 2 of 2 in the hub thread | overturning |
| f_4591ef30be4f920ba1ed14 | gdocs search "close rules" / list the data room folder | title "Paid UA close rules - data room" | 0 base hits for "Paid UA close rules" (§1.D); folder d_b563e7f1e1608c4d36f3b0 | connecting (H2) |
| frederick.stone@harmonygames.co/1843732571750494737 | gmail search "data room" / "UA numbers" | subject "data room UA numbers" | older (Sep 19); the doc says it replaces it | claim met first (T6 v1) |
| 68c99c40e5d9eb6f3a988838 | trello UA/BD board, search "UA spend buckets" | card name | same-board DD card 6807be2c1ea290e4382b33be meets the same query (decoy) | connecting (H1) |
| page_ua_spend_buckets | confluence search "UA spend buckets" | page title | Confluence searched before Trello in V1 runs (Ask_Carriers §6b) | decoy (T14) |
| 68d195a805df8c30c455f99c | trello card comments | "from the bucket review" | only comment on the card | overturning (T7 v3) |
| evt_2f9b60002516e45ff04160 | gcal search "UA bucket review" | summary | Sep 18 17:00Z on the persona's calendar; INT-11 invitation in the inbox | terminal (date) |
| f_0cd1e1402e8052d3d4e903 | gsheets search "Q4 Board Pack" | title | the Q3 pack f_9f7fb3ec09a20b2b6aa6da meets "Board Pack" | write target (H3) |
| d_6930b716ea5b1457adb4a4 | gdrive search "UA test brief" | folder + 18 titles | 0 base hits (§1.D) | per-record authority (H4) |
| d_3885933a334aef16e40e84 | gdrive search "Unity Ads statement" | folder + 25 titles | 0 base hits (§1.D); named by cmt_6b4787a755ac66787e8c | per-record evidence |
| page_singular_cost_connectors | confluence search "Singular" / "connector" | title "Singular cost connectors" | named by the H2 doc | connecting (C2 hop 1) |
| cmt_6b4787a755ac66787e8c | linear ENG-2362 comments | "Unity Ads cost has never come into Singular" | named by the connector page ("See ENG-2362.") | connecting (C2 hop 2) |
| 68dae1bc8ec7eb683dc15a8d | trello UA/BD Doing list | "Data room - paid UA true-up" | named by the hub | write target (W4) |
| 049f5555b01fd07b0f9d673c | contacts search "accountant" | job "Outside accountant (bookkeeping and tax)" | the only accountant contact | recipient (W3) |
| frederick.stone@harmonygames.co/1830999337380347892 | gmail search Adjoe invoice 04/2025 | base thread + contest + credit | first Adjoe invoice thread | evidence (C7) |


Dynamic-change seeds (claim met first · overturned by · why met first · why decisive):
- Sep 19 rough rules frederick.stone@harmonygames.co/1843732571750494737 · the Sep 26 doc f_4591ef30be4f920ba1ed14 and the Sep 30 reply
  C07C2866011/1759255500.938286 · it is in the inbox under "data room" · the doc says it replaces the 19th; the reply names the one clause it changes.
- H1 card 68c99c40e5d9eb6f3a988838 (phone + tablet Fundraising from Sep 12) · comment 68d195a805df8c30c455f99c + evt_2f9b60002516e45ff04160 ·
  the card is read first · the comment is newer and from the rule owner; the date only exists on the calendar.
- "Fb spend is like $20/day" C07C2866011/1758313330.170339 · the Sep receipts (frederick.stone@harmonygames.co/1843878722273509005 …) ·
  it sits in #executives next to the bucket thread · receipts are the billing record and H2 says use the receipts.
- April Adjoe PDF (base frederick.stone@harmonygames.co/1830999337380347892, attachment) · the May 7 credit reply in the same thread +
  FIN-000499 (snowflake.json /tables/38) · the invoice mail is the first Adjoe hit · H2 says use the ledger amount after any credit.
- Q3 pack f_9f7fb3ec09a20b2b6aa6da · Q4 pack f_0cd1e1402e8052d3d4e903 · the Q3 pack is filled in · the hub names the Q4 pack's Marketing tab.

Hidden authorities: H1 "UA spend buckets" → trello 68c99c40e5d9eb6f3a988838 (decoys page_ua_spend_buckets and 6807be2c1ea290e4382b33be,
scope Domino Delights Apr–Jun, decisive clause "This replaces the DD incent test split from April"); H2 "Paid UA close rules" →
f_4591ef30be4f920ba1ed14 (decoy frederick.stone@harmonygames.co/1843732571750494737: Unity = top-ups, Adjoe = invoice, AppLovin/Google =
Snowflake); H3 "Q4 Board Pack" → f_0cd1e1402e8052d3d4e903 (decoy f_9f7fb3ec09a20b2b6aa6da, no bucket column); H4 "UA test brief" →
d_6930b716ea5b1457adb4a4 (decoy snowflake.json /tables/34 AD_SPEND campaign keys).

## 4 Self-validation

| QC category | Tool-enforced (sql_lint / base_check) | Manual — evidence |
|---|---|---|
| Missing Universe Data | — | every register value is in a persona-readable record (1.E, check-sql PASS); Snowflake unscoped; catalog tools for every write (gsheets_values_update, Slack reply, gmail_send_message, trello_add_comment) |
| Temporal Field | PASS: all seeded times < 2025-10-01T00:00Z; replies after parents; created ≤ updated | dates in text: hub Sep 29 cites H2 (Sep 26), H1 (Sep 16), Q4 pack (Sep 29 19:30Z), true-up card (19:45Z); K7 (Sep 22) after evt_2f9b60002516e45ff04160 (Sep 18); last statement export saved Sep 30 22:30Z with rows to Sep 29 |
| Cross-service Referential | PASS: channels, users, threads, calendars, cards, pages, ENG-2362 resolve; Docs/Sheets sharing = Drive rows | the same amount in every service: $1,271.40 / $10,733.60 in the Adjoe thread only (fact_check); $81,169 = 81,168.77 rounded (snowflake.json /tables/0); ENG-2362 cited by page_singular_cost_connectors is the Singular ticket |
| Quantitative / Reconciliation | PASS: Slack reply counters (hub reply_count 2, latest_reply 1759255500.938286); Trello badges (H1 comments 1) | statement Total rows equal their daily rows (model.py); receipt line amounts sum to the billed amount (model.register checks: 0 mismatches); Adjoe 12,005.00 − 1,271.40 = 10,733.60 |
| State / Lifecycle | PASS: ENG-2362 Todo, updated_at bumped to the comment (2025-08-13T17:42:00Z) | no status contradicted: the true-up card is open on Doing; the H1 card Doing; Unity budget $1 Sep 19 → $150/campaign Sep 29 22:48Z mirrored by statement days (no spend Sep 20 – 28) |
| Identifier / Format | PASS: Slack sha ids; Gmail mailbox/RFC Message-ID + numeric thread ids; f_/d_ + 22 hex; evt_ + ical 32hex@hg4; Trello time-prefixed ids | emails copied from roster/base; tokens minted next-free (1.F) |
| Semantic / Category | — | titles match content ("Unity Ads statement - Calm Play - 2025-09-15..21"); one name per entity except the listed aliases (PvZ / Puzzles vs Zombies / Zombie Match 3D) |
| Other | — | voice per 1.C; rules state principles, never totals (fact_check: no register total in any seeded row) |

## 5 Lazy-solver pass on the implemented records

| Shortcut tried | What it yields | Why it fails / fix |
|---|---|---|
| Quote Snowflake | 81,168.77 (snowflake.json /tables/0) | register 114,873.12: Unity $0 and Meta May – Sep missing (T8, C1) |
| Hub + rules only, no per-record reads | rules | amounts live only in 57 receipt threads, 25 statements, 18 briefs (cohort) |
| One gdrive search for statements, read 1–2 | partial Unity | each statement is its own spreadsheet (25 calls); no total across statements exists in any seeded row |
| gmail search "ads receipt" + batch read | all Meta bodies | accepted cost (0.3/thread); still needs per-charge payment method + reference number |
| Read the H1 card only | tablet Fundraising all Sep | K7 comment + calendar date (T7) |
| Read the doc, not the thread | Adjoe by wire month (May in Jul, June dropped) | Sep 30 reply (T6) |
| Search "Unity" in mail | Calm Play alert + support thread + top-ups | statements are the spend (T20, T22) |

No seeded row states a register value, a bucket total or the gap list (`fact_check` declares none and the model totals appear nowhere in the SQL).

## 6 Intended disagreements

| Disagreement | Records | Why realistic | What resolves it |
|---|---|---|---|
| Snowflake $81,169 vs the register | C07C2866011/1759176840.271025; snowflake.json /tables/0 | Leonard quotes the warehouse; the Aug 14 connector page explains Singular misses Unity cost and Meta since May | the register from the sources (R12 gap list) |
| Sep 19 rules vs Sep 26 doc vs Sep 30 reply | frederick.stone@harmonygames.co/1843732571750494737; f_4591ef30be4f920ba1ed14; C07C2866011/1759255500.938286 | a draft then a write-up then one amendment | newest wins clause by clause |
| H1 card vs tablet comment | 68c99c40e5d9eb6f3a988838; 68d195a805df8c30c455f99c | the review changed the tablet bucket | comment + review date Sep 18 |
| "$20/day" vs the Sep receipts | C07C2866011/1758313330.170339; frederick.stone@harmonygames.co/1843878722273509005 | a CEO's rough figure | receipts (H2) |
| Adjoe April PDF $12,005.00 vs ledger $10,733.60 | frederick.stone@harmonygames.co/1830999337380347892; snowflake.json /tables/38 FIN-000499 | Leonard contests 2,401 invoiced vs 1,923 Singular installs; partial credit $1,271.40 on May 7 | ledger amount (H2) |
| Q3 pack vs Q4 pack format | f_9f7fb3ec09a20b2b6aa6da; f_0cd1e1402e8052d3d4e903 | last quarter's template | the hub names the Q4 pack |
| DD bucket card / page vs Sep card | 6807be2c1ea290e4382b33be; page_ua_spend_buckets; 68c99c40e5d9eb6f3a988838 | a spring test with its own split | Sep card: "This replaces the DD incent test split" |
| Robert's "Singular number" | C07C2866011/1759178460.557708 | a co-founder's shortcut | no authority over the close |
| Snowflake Meta Oct – Apr ≠ receipts | snowflake.json /tables/0; frederick.stone@harmonygames.co/1812262106647207041 | connector page: modelled from installs across accounts | H2 "Use the receipts, even where Snowflake shows something else" |
| Calm Play "alpha account" (Oct 2024) vs H2 scope | frederick.stone@harmonygames.co/1813530307529968502; f_4591ef30be4f920ba1ed14 | ZM3D moved onto Calm Play in May 2025 (C07C2866011/1747847918.209079) | H2 scope names the Calm Play account |

## 7 Constraints for the prompt brief

| Anchor | May be named (noun phrases only) | Record |
|---|---|---|
| A1 | Leonard's paid UA true-up request; the data room UA number; the Oct 14 board; the last twelve months | C07C2866011/1759176840.271025 |

| Destination (V3: the prompt names it) | Record |
|---|---|
| Marketing tab of the Q4 board pack | f_0cd1e1402e8052d3d4e903 |
| reply in Leonard's #executives thread | C07C2866011/1759176840.271025 |
| the true-up card | 68dae1bc8ec7eb683dc15a8d |
| our outside accountant | 049f5555b01fd07b0f9d673c |


Never named in the prompt: the close-rules doc or its location, the UA/BD bucket card, the review date, the briefs, the statements,
Calm Play, the top-ups, the credit-funded charge, the duplicate receipts, Adjoe's credit or September reply, the connector page,
ENG-2362, the Sep 30 amendment, any id, any rule clause or the root cause (V3 §8: no trap hints, riddles or answer-key clauses).
Deadline: the Oct 14 board (after the freeze; allowed as a deadline). Deliverables: register rows + gap list in the Marketing tab;
per-bucket totals as a thread reply and a true-up card comment; the sheet link by mail to the accountant. Times: Pacific, with UTC
beside them when the day differs (V3 §10); no seeded charge changes day between zones except base frederick.stone@harmonygames.co/1820007110310927242.

## 8 Fact sheet

| Key | Value | Kind | Must appear in / home |
|---|---|---|---|
| Snowflake paid UA (Oct 2024-Sep 2025) | 81,169 | amount | C07C2866011/1759176840.271025 |
| fundraising bucket start | Sep 12 | date | 68c99c40e5d9eb6f3a988838 |
| Meta ad account | 3125 | id | f_4591ef30be4f920ba1ed14 |
| UA bucket review | Sep 18, 2025 | date | consistency only |
| Adjoe April credit | 1,271.40 | amount | frederick.stone@harmonygames.co/1830999337380347892; leonard.hayes@harmonygames.co/1830999337374111635 |
| Adjoe April total after credit | 10,733.60 | amount | frederick.stone@harmonygames.co/1830999337380347892; leonard.hayes@harmonygames.co/1830999337374111635 |
| Sep 19 Meta charge paid with advertising credit | 61.40 | amount | frederick.stone@harmonygames.co/1843788314050589285; frederick.stone@harmonygames.co/1843788314050589285 |
| Sep 30 Meta charge (4:40 PM PT) | 57.85 | amount | frederick.stone@harmonygames.co/1844734171545827192; frederick.stone@harmonygames.co/1844734171545827192 |
| Unity statement total Calm Play Sep 15-21 | 1,456.04 | amount | f_76007a5c131f92019df2a0; f_76007a5c131f92019df2a0 |
| Unity statement total Calm Play Jul 8-14 | 858.30 | amount | f_1a3c4303fe9b70a0c5d725; f_1a3c4303fe9b70a0c5d725 |

`python3 Task_Authoring/tools/fact_check.py Task_Authoring/task_inputs/01_Universe_Inject.sql --manifest Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.json --no-leak`:

```
FACT CHECK: PASS — 180 text-bearing rows, 10 declared facts, 8 declared superseded records
Errors: none
Warnings (3):
  line 105: gmail.gmail_messages frederick.stone@harmonygames.co/<9a17576b-c417-450c-a3c5-2f7ba33ed844@support.facebook.com>: [value_drift] 'amount' carries 25 different amounts across rows: '$186.40' (line 43, row frederick.stone@harmonygames.co/<11cbfaec-8b57-4b9f-a425-163b41445ff1@support.facebook.com>, +1); '$162.40' (line 31, row frederick.stone@harmonygames.co/<15fa478b-a312-4368-a84d-577a6aa7885a@support.facebook.com>); '$141.85' (line 31, row frederick.stone@harmonygames.co/<15fa478b-a312-4368-a84d-577a6aa7885a@support.facebook.com>); '$128.90' (line 31, row frederick.stone@harmonygames.co/<15fa478b-a312-4368-a84d-577a6aa7885a@support.facebook.com>) — supersession (declare it in traps[].version_records / facts) or drift?
  line 105: gmail.gmail_messages frederick.stone@harmonygames.co/<9a17576b-c417-450c-a3c5-2f7ba33ed844@support.facebook.com>: [value_drift] 'billed' carries 19 different amounts across rows: '$186.40' (line 43, row frederick.stone@harmonygames.co/<11cbfaec-8b57-4b9f-a425-163b41445ff1@support.facebook.com>, +1); '$486.30' (line 31, row frederick.stone@harmonygames.co/<15fa478b-a312-4368-a84d-577a6aa7885a@support.facebook.com>); '$0.11' (line 35, row frederick.stone@harmonygames.co/<ea10aaa6-a5a6-4fb1-a2ff-ca27d6d09deb@support.facebook.com>); '$0.07' (line 39, row frederick.stone@harmonygames.co/<e52f9241-0084-4436-a397-0bb4a9c221a2@support.facebook.com>) — supersession (declare it in traps[].version_records / facts) or drift?
  line 105: gmail.gmail_messages frederick.stone@harmonygames.co/<9a17576b-c417-450c-a3c5-2f7ba33ed844@support.facebook.com>: [value_drift] 'tax' carries 19 different amounts across rows: '$186.40' (line 43, row frederick.stone@harmonygames.co/<11cbfaec-8b57-4b9f-a425-163b41445ff1@support.facebook.com>, +1); '$486.30' (line 31, row frederick.stone@harmonygames.co/<15fa478b-a312-4368-a84d-577a6aa7885a@support.facebook.com>); '$0.11' (line 35, row frederick.stone@harmonygames.co/<ea10aaa6-a5a6-4fb1-a2ff-ca27d6d09deb@support.facebook.com>); '$0.07' (line 39, row frederick.stone@harmonygames.co/<e52f9241-0084-4436-a397-0bb4a9c221a2@support.facebook.com>) — supersession (declare it in traps[].version_records / facts) or drift?
```

Warning disposition: the three `value_drift` warnings group different charges under a shared word ("amount", "billed", "tax"); each receipt is its own charge, not a restated fact (frederick.stone@harmonygames.co/1843516837725026041 vs frederick.stone@harmonygames.co/1842010914816895400).

## 9 Facts for the human

### 9.1 Records

| Locator | Base / seeded | Fact (values, actors, UTC) | Reach path | Role | Re-verify? |
|---|---|---|---|---|---|
| C07C2866011/1759176840.271025 | seeded | Leonard, 2025-09-29T20:14:00Z (1:14 PM PT): asks for the real paid UA number Oct 1 – Sep 30; quotes Snowflake $81,169; rules doc, UA/BD buckets, Q4 pack Marketing tab, reply here + true-up card | #executives member | anchor A1 | no |
| C07C2866011/1759178460.557708 | seeded | Robert, 2025-09-29T20:41:00Z: use the Singular number | #executives member | decoy | no |
| C07C2866011/1759255500.938286 | seeded | Leonard, 2025-09-30T18:05:00Z: Adjoe in the month the invoice is for; rest stands | #executives member | overturning evidence | no |
| frederick.stone@harmonygames.co/1843732571750494737 | seeded | Leonard → Frederick + Arthur, 2025-09-19T22:20:00Z: Meta receipts, Unity top-ups, Adjoe invoice, AppLovin/Google Snowflake | own INBOX | claim met first | no |
| f_4591ef30be4f920ba1ed14 | seeded | Leonard, modified 2025-09-26T21:05:00Z: rules (scope incl. Calm Play; Meta receipts/credit/duplicates/PT month; Unity statements; Adjoe ledger + wire month; AppLovin/Google ledger split by game; titles from briefs; gap list; accountant, no new sharing) | shared | authority (H2) | no |
| 68c99c40e5d9eb6f3a988838 | seeded | Frederick, 2025-09-16T17:20:00Z: Fundraising = UK iOS Unity phone + tablet and Meta ZM_UK from Sep 12; bucket by day spent; replaces the April DD split | unscoped | authority (H1) | no |
| 68d195a805df8c30c455f99c | seeded | Leonard, 2025-09-22T18:30:00Z: tablet back to Real UA from the day of the review | unscoped | overturning evidence | no |
| evt_2f9b60002516e45ff04160 | seeded | UA bucket review 2025-09-18 17:00–17:30Z (10:00–10:30 AM PT), organizer Leonard, Frederick accepted | own calendar | authority date | no |
| 6807be2c1ea290e4382b33be | seeded | Frederick, 2025-04-22T16:05:00Z: DD incent test Apr – Jun, Adjoe + AppLovin Fundraising | unscoped | decoy | no |
| page_ua_spend_buckets | seeded | Frederick, 2025-04-24T17:10:00Z: same DD split | unscoped | decoy | re-verify after regeneration |
| page_singular_cost_connectors | seeded | Simon, 2025-08-14T16:20:00Z: Adjoe/AppLovin/Google yes; Meta partly (modelled; lost access in May); Unity no (installs only, see ENG-2362) | unscoped | evidence | re-verify after regeneration |
| cmt_6b4787a755ac66787e8c | seeded | Simon on ENG-2362, 2025-08-13T17:42:00Z: Unity cost never in Singular; real spend on the statements for both accounts | unscoped | evidence | no |
| f_0cd1e1402e8052d3d4e903 | seeded | Q4 Board Pack - Oct 14, Leonard, created 2025-09-29T19:30:00Z; Marketing!A1:H1 = Month, Network, Title, Bucket, Spend (USD), Credit used (USD), Net cost (USD), Source | shared (Frederick, Arthur, accountant) | write target | no |
| f_9f7fb3ec09a20b2b6aa6da | seeded | Q3 Board Pack - Jul 16 (Q2 lines from Snowflake, no bucket column) | shared | decoy | no |
| d_b563e7f1e1608c4d36f3b0 | seeded | folder Data Room - Bridge 2025 (Leonard; shared Frederick, Arthur, accountant) | shared | destination folder | no |
| 68dae1bc8ec7eb683dc15a8d | seeded | Leonard, 2025-09-29T19:45:00Z, Doing, member Frederick | unscoped | write target | no |
| 049f5555b01fd07b0f9d673c | seeded | PERSON_6098, Outside accountant (bookkeeping and tax), PERSON_6098_EMAIL | unscoped | recipient | no |
| frederick.stone@harmonygames.co/1830999337380347892 | base + 2 seeded | May 2 invoice 04/2025 (PDF); May 4 'Payment initiated'; May 5 contest (invoice 2,401 installs vs Singular 1,923); May 7 credit → April total $10,733.60 | own INBOX | evidence | no |
| C07UCC631A6/1757345931.336429 | base | Leonard 2025-09-08: a campaign turned on we didn't approve | adjoe channel member | claim met first | no |
| C07UCC631A6/1757349668.681539 | base | Adjoe rep (thread reply): not responsible for the cost | adjoe channel member | overturning evidence | no |
| snowflake.json /tables/38 FIN-000499 FIN-000529 FIN-000555 | base | Adjoe Apr −10,733.60, May −20,537.92, Jun −14,930.02 | unscoped | evidence | no |
| snowflake.json /tables/38 FIN-000500 FIN-000530 FIN-000556 FIN-000579 FIN-000599 | base | AppLovin Apr 799.85, May 1,564.82, Jun 1,947.39, Jul 1,838.38, Aug 75.80 | unscoped | evidence | no |
| snowflake.json /tables/38 FIN-000333 … FIN-000501 | base | Google UAC Oct 74.31, Nov 101.87, Dec 130.99, Jan 56.55, Feb 25.56, Mar 31.00, Apr 12.51 | unscoped | evidence | no |
| snowflake.json /tables/0 | base | AD_SPEND_DAILY: Unity $0 every month; no Meta May – Sep; AppLovin Jun DD 1,904.81 + ZM 42.58, Jul DD 1,816.55 + ZM 21.83; TTM 81,168.77 | unscoped | gap check + split | re-verify after regeneration |
| frederick.stone@harmonygames.co/1842010914816895400 | seeded | Meta receipt 2025-08-31 15:15 PT (2025-08-31T22:15:00Z): $486.30 (card, ref QZ7HN4PFY2); covers Aug 18, 2025, 12:00 AM – Aug 31, 2025, 3:14 PM; ZM_UK_StaticA $162.40; ZM_UK_StaticB $141.85; ZM_UK_StaticC $128.90; ZM_UK_CPE_CopyAds $53.15 | own INBOX | per-record evidence | no |
| frederick.stone@harmonygames.co/1843154072371887815 | seeded | Meta receipt 2025-09-13 06:05 PT (2025-09-13T13:05:00Z): $0.11 (advertising credit); covers Sep 12, 2025, 12:00 AM – Sep 12, 2025, 11:59 PM; ZM_UK_CPE_CopyAds $0.11 | own INBOX | per-record evidence | no |
| frederick.stone@harmonygames.co/1843244480594183249 | seeded | Meta receipt 2025-09-14 06:02 PT (2025-09-14T13:02:00Z): $0.07 (advertising credit); covers Sep 13, 2025, 12:00 AM – Sep 13, 2025, 11:59 PM; ZM_UK_CPE_CopyAds $0.07 | own INBOX | per-record evidence | no |
| frederick.stone@harmonygames.co/1843516837725026041 | seeded | Meta receipt 2025-09-17 06:11 PT (2025-09-17T13:11:00Z): $186.40 (card, ref M4RKD8XFY2); covers Sep 16, 2025, 12:00 AM – Sep 16, 2025, 11:59 PM; ZM_UK_Retention_iOS $186.40; duplicate notification (same ref + transaction id) | own INBOX | per-record evidence | no |
| frederick.stone@harmonygames.co/1843606994289346111 | seeded | Meta receipt 2025-09-18 06:04 PT (2025-09-18T13:04:00Z): $142.15 (card, ref T9WQ2LHFY2); covers Sep 17, 2025, 12:00 AM – Sep 17, 2025, 11:59 PM; ZM_UK_Retention_iOS $142.11; ZM_UK_CPE_CopyAds $0.04 | own INBOX | per-record evidence | no |
| frederick.stone@harmonygames.co/1843697905828235234 | seeded | Meta receipt 2025-09-19 06:09 PT (2025-09-19T13:09:00Z): $118.70 (card, ref V6PJN3XEY2); covers Sep 18, 2025, 12:00 AM – Sep 18, 2025, 11:59 PM; ZM_UK_Retention_iOS $118.70 | own INBOX | per-record evidence | no |
| frederick.stone@harmonygames.co/1843788314050589285 | seeded | Meta receipt 2025-09-20 06:06 PT (2025-09-20T13:06:00Z): $61.40 (advertising credit); covers Sep 19, 2025, 12:00 AM – Sep 19, 2025, 11:59 PM; ZM_UK_Retention_iOS $61.40 | own INBOX | per-record evidence | no |
| frederick.stone@harmonygames.co/1843878722273509005 | seeded | Meta receipt 2025-09-21 06:03 PT (2025-09-21T13:03:00Z): $27.35 (card, ref R2YHK7DFY2); covers Sep 20, 2025, 12:00 AM – Sep 20, 2025, 11:59 PM; ZM_UK_Retention_iOS $27.35 | own INBOX | per-record evidence | no |
| frederick.stone@harmonygames.co/1843969633812798247 | seeded | Meta receipt 2025-09-22 06:08 PT (2025-09-22T13:08:00Z): $24.80 (card, ref W8LC5QNFY2); covers Sep 21, 2025, 12:00 AM – Sep 21, 2025, 11:59 PM; ZM_UK_Retention_iOS $24.80 | own INBOX | per-record evidence | no |
| frederick.stone@harmonygames.co/1844059853292161439 | seeded | Meta receipt 2025-09-23 06:02 PT (2025-09-23T13:02:00Z): $31.15 (card, ref F3VTZ9JEY2); covers Sep 22, 2025, 12:00 AM – Sep 22, 2025, 11:59 PM; ZM_UK_Retention_iOS $31.15 | own INBOX | per-record evidence | no |
| frederick.stone@harmonygames.co/1844150953574592539 | seeded | Meta receipt 2025-09-24 06:10 PT (2025-09-24T13:10:00Z): $26.40 (card, ref K5NBQ2WFY2); covers Sep 23, 2025, 12:00 AM – Sep 23, 2025, 11:59 PM; ZM_UK_Retention_iOS $26.40 | own INBOX | per-record evidence | no |
| frederick.stone@harmonygames.co/1844241235968886522 | seeded | Meta receipt 2025-09-25 06:05 PT (2025-09-25T13:05:00Z): $29.95 (card, ref H7DRX4CFY2); covers Sep 24, 2025, 12:00 AM – Sep 24, 2025, 11:59 PM; ZM_UK_Retention_iOS $29.95 | own INBOX | per-record evidence | no |
| frederick.stone@harmonygames.co/1844331958763627407 | seeded | Meta receipt 2025-09-26 06:07 PT (2025-09-26T13:07:00Z): $33.10 (card, ref P9GSM6TFY2); covers Sep 25, 2025, 12:00 AM – Sep 25, 2025, 11:59 PM; ZM_UK_Retention_iOS $33.10 | own INBOX | per-record evidence | no |
| frederick.stone@harmonygames.co/1844422366986338173 | seeded | Meta receipt 2025-09-27 06:04 PT (2025-09-27T13:04:00Z): $25.60 (card, ref B4KWH8NEY2); covers Sep 26, 2025, 12:00 AM – Sep 26, 2025, 11:59 PM; ZM_UK_Retention_iOS $25.60 | own INBOX | per-record evidence | no |
| frederick.stone@harmonygames.co/1844513089782197590 | seeded | Meta receipt 2025-09-28 06:06 PT (2025-09-28T13:06:00Z): $22.45 (card, ref J6QZC3RFY2); covers Sep 27, 2025, 12:00 AM – Sep 27, 2025, 11:59 PM; ZM_UK_Retention_iOS $22.45 | own INBOX | per-record evidence | no |
| frederick.stone@harmonygames.co/1844603498005085849 | seeded | Meta receipt 2025-09-29 06:03 PT (2025-09-29T13:03:00Z): $28.70 (card, ref N2XLV5PFY2); covers Sep 28, 2025, 12:00 AM – Sep 28, 2025, 11:59 PM; ZM_UK_Retention_iOS $28.70 | own INBOX | per-record evidence | no |
| frederick.stone@harmonygames.co/1844734171545827192 | seeded | Meta receipt 2025-09-30 16:40 PT (2025-09-30T23:40:00Z): $57.85 (card, ref L8TRJ7KFY2); covers Sep 29, 2025, 12:00 AM – Sep 30, 2025, 4:39 PM; ZM_UK_Retention_iOS $57.85 | own INBOX | per-record evidence | no |
| frederick.stone@harmonygames.co/1831357377414065699 | seeded copy of Leonard's mailbox thread 1831357378751331011 | Meta receipt 2025-05-06T01:01:35-07:00: $136.50, ref [TAX_ID_5752]; PvZ_iOS_US_Tutorial $58.29; PvZ_iOS_US_Adv_Install $78.21 | own INBOX | per-record evidence | no |
| frederick.stone@harmonygames.co/1834164376568289766 | seeded copy of Leonard's mailbox thread 1834164377682810022 | Meta receipt 2025-06-06T00:37:38-07:00: $143.06, ref [TAX_ID_11451]; PvZ_iOS_US_Adv_Install $42.57; PvZ_iOS_US_Tutorial $100.49 | own INBOX | per-record evidence | no |
| frederick.stone@harmonygames.co/1813907358352348391 | seeded | Leonard's forward 2024-10-25T17:21:00Z of his base Unity receipt dated Oct 25, 2024 9:58 AM PT ([SOURCE_ORG_0001] Games Inc.) $2,000 — prepaid, not spend | own INBOX | decoy (T20) | no |
| frederick.stone@harmonygames.co/1819366895124967091 | seeded | Leonard's forward 2024-12-24T23:38:00Z of his base Unity receipt dated Dec 24, 2024 3:15 PM PT ([SOURCE_ORG_0001] Games Inc.) $2,000 — prepaid, not spend | own INBOX | decoy (T20) | no |
| frederick.stone@harmonygames.co/1832753288970947639 | seeded | Leonard's forward 2025-05-21T17:49:00Z of his base Unity receipt dated May 21, 2025 10:27 AM PT ([SOURCE_ORG_0001] Games Inc.) $1,000 — prepaid, not spend | own INBOX | decoy (T20) | no |
| frederick.stone@harmonygames.co/1834226118820623605 | seeded | Leonard's forward 2025-06-06T23:59:00Z of his base Unity receipt dated Jun 6, 2025 4:56 PM PT ([SOURCE_ORG_0001] Games Inc.) $1,000.00 — prepaid, not spend | own INBOX | decoy (T20) | no |
| frederick.stone@harmonygames.co/1838650711081025746 | seeded | Leonard's forward 2025-07-25T20:06:00Z of his base Unity receipt dated Jul 25, 2025 12:45 PM PT ([SOURCE_ORG_0001] Games Inc.) $1,000.00 — prepaid, not spend | own INBOX | decoy (T20) | no |
| frederick.stone@harmonygames.co/1843072786759807900 | seeded | Leonard's forward 2025-09-12T15:33:00Z of his base Unity receipt dated Sep 12, 2025 8:11 AM PT ([SOURCE_ORG_0001] Games Inc.) $1,000.00 — prepaid, not spend | own INBOX | decoy (T20) | no |
| f_6d0c2209baa3ff54633836 | seeded | brief B01 2024-10-10: DD iOS AU NZ CA broad → Domino Delights; campaigns Node_iOS_AU_NZ_CA_Broad_AEM_1011 | owned | authority (H4) | no |
| f_a5e0147cfc1fba7a9c7349 | seeded | brief B02 2024-10-06: DD Argentina Spanish test → Domino Delights; campaigns Node_iOS_AR_Spanish_1007, Node_Android_AR_Spanish_1008, Node_iOS_AR_Broad_AEM_AR_Spanish_1009 | owned | authority (H4) | no |
| f_206c42f98afd5fcbd0461a | seeded | brief B03 2024-10-06: Advantage+ trial → Domino Delights; campaigns Advantage+ app campaign 10/06/2024 | owned | authority (H4) | no |
| f_5edcf4c37a67ee2561e9e4 | seeded | brief B04 2024-10-19: DD iOS tutorial-complete test → Domino Delights; campaigns NM_DominoDelights_iOS_AU-CA-NZ_TutComplete_1021, NM_DominoDelights_iOS_AU_NZ_BAU_TutComplete_1028 | owned | authority (H4) | no |
| f_cc0200cda2a03d6f444916 | seeded | brief B05 2024-11-06: Android Philippines test → Domino Delights; campaigns Node_Android_PH_Installs_1106, Node_Android_PH_BAU_1109, Node_Android_PH_ADV_TutComplete_1114, Node_Android_PH_BAU_1114 | owned | authority (H4) | no |
| f_f017eafb1e59601f888460 | seeded | brief B06 2024-11-17: Android Nordics → Domino Delights; campaigns Node_Android_DK-SW-FI-NL_ADV_TutComplete_1119, Node_Android_DK-SW-FI-NL_BAU_1119 | owned | authority (H4) | no |
| f_c37d51b92f6c34b520fd73 | seeded | brief B07 2024-12-04: Creative A/B test → Domino Delights; campaigns Creative_AB_Test | owned | authority (H4) | no |
| f_50ffc8312fcfd96d096754 | seeded | brief B08 2024-12-30: Android CA and AU NZ re-test → Domino Delights; campaigns Android_CA_ADV_TutComplete, Android_AU_NZ_ADV_TutComplete | owned | authority (H4) | no |
| f_9e4be4822ec79ce7ff5d17 | seeded | brief B09 2025-04-02: iOS CA tutorial complete → Domino Delights; campaigns iOS_CA_ADV_TutComplete | owned | authority (H4) | no |
| f_42ba151c4158922854572a | seeded | brief B10 2025-04-08: PvZ Android Nordics → Zombie Match 3D; campaigns PvZ_Android_DK-SW-FI-NL_Adv_Install - Copy | owned | authority (H4) | no |
| f_a12749c3f0cea9d44061d9 | seeded | brief B11 2025-04-08: PvZ iOS US → Zombie Match 3D; campaigns PvZ_iOS_US_Adv_Install, PvZ_iOS_US_Tutorial | owned | authority (H4) | no |
| f_298721fb6cb960d796fcbb | seeded | brief B12 2025-06-09: PvZ iOS UK install → Zombie Match 3D; campaigns PVZ_iOS_UK_Install | owned | authority (H4) | no |
| f_3d2795c2623a50864b2764 | seeded | brief B13 2025-06-13: Zombie test 2 → Zombie Match 3D; campaigns ZombieTest2_A, ZombieTest2_B, ZombieTest2_A_UK, ZombieTest2_B_UK | owned | authority (H4) | no |
| f_0a5638d43dd053ed974e21 | seeded | brief B14 2025-06-14: ZM video CPI test → Zombie Match 3D; campaigns ZM_vidCPI_cat, ZM_vidCPI_barrel, ZM_vidCPI_couch | owned | authority (H4) | no |
| f_6dcaecd8cb0bdbbb18b945 | seeded | brief B15 2025-07-06: ZM UK video CPI test → Zombie Match 3D; campaigns ZM_UK_vidCPI_football, ZM_UK_vidCPI_cat, ZM_UK_vidCPI_cheer | owned | authority (H4) | no |
| f_0d60db1d5b484c5afd9792 | seeded | brief B16 2025-07-15: ZM UK statics → Zombie Match 3D; campaigns ZM_UK_StaticA, ZM_UK_StaticB, ZM_UK_StaticC | owned | authority (H4) | no |
| f_cb32548a078870d1d80dca | seeded | brief B17 2025-07-06: ZM UK copy ads → Zombie Match 3D; campaigns ZM_UK_CPE_CopyAds | owned | authority (H4) | no |
| f_887def6eed0e1b022f7ab0 | seeded | brief B18 2025-09-11: ZM UK retention iOS → Zombie Match 3D; campaigns ZM_UK_Retention_iOS | owned | authority (H4) | no |
| f_c34b364c50bf4ed59ae6ce | seeded | Unity statement HG account 2024-10, saved 2024-11-03T18:10:00Z: total $1,584.94 | owned | per-record evidence | no |
| f_41bc63b2332620eb08b80a | seeded | Unity statement HG account 2024-11, saved 2024-12-02T17:40:00Z: total $6,537.06 | owned | per-record evidence | no |
| f_4a6e3125ed715725161c86 | seeded | Unity statement HG account 2024-12, saved 2025-01-03T18:05:00Z: total $1,992.77 | owned | per-record evidence | no |
| f_6c15d48fa95f0739fc42da | seeded | Unity statement HG account 2025-01, saved 2025-02-03T17:55:00Z: total $3,350.17 | owned | per-record evidence | no |
| f_f57990a3307dea5aa0af0f | seeded | Unity statement HG account 2025-02, saved 2025-03-03T18:20:00Z: total $489.09 | owned | per-record evidence | no |
| f_a4942fdb8f8530b1cc93e0 | seeded | Unity statement HG account 2025-03, saved 2025-04-02T17:35:00Z: total $539.63 | owned | per-record evidence | no |
| f_ad44496a3e89c11de71d81 | seeded | Unity statement HG account 2025-04, saved 2025-05-02T17:50:00Z: total $109.68 | owned | per-record evidence | no |
| f_1311b8c998f28831b1cf43 | seeded | Unity statement Calm Play 2025-04, saved 2025-05-02T17:52:00Z: total $1,184.77 | owned | per-record evidence | no |
| f_f7564f9413e650dd90cb74 | seeded | Unity statement Calm Play 2025-05, saved 2025-06-02T18:00:00Z: total $958.27 | owned | per-record evidence | no |
| f_66d70cbc162e336d8d9074 | seeded | Unity statement Calm Play 2025-06-01..07, saved 2025-06-09T17:15:00Z: total $499.61 | owned | per-record evidence | no |
| f_26f69b46d45852fb515912 | seeded | Unity statement Calm Play 2025-06-08..14, saved 2025-06-16T17:20:00Z: total $733.45 | owned | per-record evidence | no |
| f_a278aec0da8fbd8f7cd86d | seeded | Unity statement Calm Play 2025-06-15..21, saved 2025-06-23T17:10:00Z: total $1,016.70 | owned | per-record evidence | no |
| f_3cdb6026a369e505609c3e | seeded | Unity statement Calm Play 2025-06-22..30, saved 2025-07-01T17:25:00Z: total $1,131.36 | owned | per-record evidence | no |
| f_e923eb578c12cd3aa2b1ff | seeded | Unity statement Calm Play 2025-07-01..07, saved 2025-07-08T17:05:00Z: total $872.86 | owned | per-record evidence | no |
| f_1a3c4303fe9b70a0c5d725 | seeded | Unity statement Calm Play 2025-07-08..14, saved 2025-07-15T17:30:00Z: total $858.30 | owned | per-record evidence | no |
| f_ac8e62864ae33cf47aef61 | seeded | Unity statement Calm Play 2025-07-15..21, saved 2025-07-22T17:12:00Z: total $844.26 | owned | per-record evidence | no |
| f_9a825acb7a3b71cfff45d0 | seeded | Unity statement Calm Play 2025-07-22..31, saved 2025-08-01T17:18:00Z: total $1,290.24 | owned | per-record evidence | no |
| f_389e010ecc827029d9cdcf | seeded | Unity statement Calm Play 2025-08-01..07, saved 2025-08-08T17:22:00Z: total $1,220.27 | owned | per-record evidence | no |
| f_057df7adc2e2c887bf9f6f | seeded | Unity statement Calm Play 2025-08-08..14, saved 2025-08-15T17:08:00Z: total $1,252.46 | owned | per-record evidence | no |
| f_e68b1465f0e0fa85fe2a9a | seeded | Unity statement Calm Play 2025-08-15..21, saved 2025-08-22T17:14:00Z: total $1,789.79 | owned | per-record evidence | no |
| f_19c380c11615388ff75ce8 | seeded | Unity statement Calm Play 2025-08-22..31, saved 2025-09-01T17:26:00Z: total $2,474.30 | owned | per-record evidence | no |
| f_e8f75f70da75c40e9d395e | seeded | Unity statement Calm Play 2025-09-01..07, saved 2025-09-08T17:11:00Z: total $139.83 | owned | per-record evidence | no |
| f_09666ca5c83c6a319ece41 | seeded | Unity statement Calm Play 2025-09-08..14, saved 2025-09-15T17:16:00Z: total $1,588.77 (Fundraising $1,449.60, Real UA $139.17) | owned | per-record evidence | no |
| f_76007a5c131f92019df2a0 | seeded | Unity statement Calm Play 2025-09-15..21, saved 2025-09-22T17:09:00Z: total $1,456.04 (Fundraising $1,246.00, Real UA $210.04) | owned | per-record evidence | no |
| f_0c302b9a0529823a0c6209 | seeded | Unity statement Calm Play 2025-09-22..29, saved 2025-09-30T22:30:00Z: total $225.86 (Fundraising $35.00, Real UA $190.86) | owned | per-record evidence | no |

### 9.2 Derived ground truth (`model.py register()`, from the records above; for the human's Oracle Events and rubric)

| Month | Network | Title | Bucket | Spend (USD) | Credit used (USD) | Net cost (USD) | Source | Records |
|---|---|---|---|---|---|---|---|---|
| 2024-10 | Google UAC | Domino Delights | Real UA | 74.31 | 0.00 | 74.31 | FINANCE_LEDGER FIN-000333 | snowflake.json /tables/38 FIN-000333 |
| 2024-10 | Meta | Domino Delights | Real UA | 7,016.00 | 0.00 | 7,016.00 | Meta receipts (account ending 3125) | frederick.stone@harmonygames.co/1812262106647207041; frederick.stone@harmonygames.co/1812839883787768319; frederick.stone@harmonygames.co/1813049887158875039; frederick.stone@harmonygames.co/1813379281814151196; frederick.stone@harmonygames.co/1813460395597065111; frederick.stone@harmonygames.co/1813570677525296798; frederick.stone@harmonygames.co/1813727496096729809; frederick.stone@harmonygames.co/1813825423889664563; frederick.stone@harmonygames.co/1813904811482385587; frederick.stone@harmonygames.co/1814042565503776727; frederick.stone@harmonygames.co/1814211514242959315 |
| 2024-10 | Unity Ads | Domino Delights | Real UA | 1,584.94 | 0.00 | 1,584.94 | Unity statements (HG account) | f_c34b364c50bf4ed59ae6ce |
| 2024-11 | Google UAC | Domino Delights | Real UA | 101.87 | 0.00 | 101.87 | FINANCE_LEDGER FIN-000361 | snowflake.json /tables/38 FIN-000361 |
| 2024-11 | Meta | Domino Delights | Real UA | 6,357.55 | 0.00 | 6,357.55 | Meta receipts (account ending 3125) | frederick.stone@harmonygames.co/1814959634472648361; frederick.stone@harmonygames.co/1815692691136620637; frederick.stone@harmonygames.co/1815861152183775926; frederick.stone@harmonygames.co/1816079268118375341; frederick.stone@harmonygames.co/1816331182428132431; frederick.stone@harmonygames.co/1816920350286580043; frederick.stone@harmonygames.co/1817043264479181246; frederick.stone@harmonygames.co/1817180294730550227 |
| 2024-11 | Unity Ads | Domino Delights | Real UA | 6,537.06 | 0.00 | 6,537.06 | Unity statements (HG account) | f_41bc63b2332620eb08b80a |
| 2024-12 | Google UAC | Domino Delights | Real UA | 130.99 | 0.00 | 130.99 | FINANCE_LEDGER FIN-000389 | snowflake.json /tables/38 FIN-000389 |
| 2024-12 | Meta | Domino Delights | Real UA | 3,453.82 | 0.00 | 3,453.82 | Meta receipts (account ending 3125) | frederick.stone@harmonygames.co/1817681870046929356; frederick.stone@harmonygames.co/1819776649300869905; frederick.stone@harmonygames.co/1819888664949792853; frederick.stone@harmonygames.co/1820007110310927242 |
| 2024-12 | Unity Ads | Domino Delights | Real UA | 1,992.77 | 0.00 | 1,992.77 | Unity statements (HG account) | f_4a6e3125ed715725161c86 |
| 2025-01 | Google UAC | Domino Delights | Real UA | 56.55 | 0.00 | 56.55 | FINANCE_LEDGER FIN-000417 | snowflake.json /tables/38 FIN-000417 |
| 2025-01 | Meta | Domino Delights | Real UA | 1,619.71 | 0.00 | 1,619.71 | Meta receipts (account ending 3125) | frederick.stone@harmonygames.co/1820132039739740641; frederick.stone@harmonygames.co/1820486398663099282 |
| 2025-01 | Unity Ads | Domino Delights | Real UA | 3,350.17 | 0.00 | 3,350.17 | Unity statements (HG account) | f_6c15d48fa95f0739fc42da |
| 2025-02 | Google UAC | Domino Delights | Real UA | 25.56 | 0.00 | 25.56 | FINANCE_LEDGER FIN-000445 | snowflake.json /tables/38 FIN-000445 |
| 2025-02 | Unity Ads | Domino Delights | Real UA | 489.09 | 0.00 | 489.09 | Unity statements (HG account) | f_f57990a3307dea5aa0af0f |
| 2025-03 | Google UAC | Domino Delights | Real UA | 31.00 | 0.00 | 31.00 | FINANCE_LEDGER FIN-000472 | snowflake.json /tables/38 FIN-000472 |
| 2025-03 | Unity Ads | Domino Delights | Real UA | 539.63 | 0.00 | 539.63 | Unity statements (HG account) | f_a4942fdb8f8530b1cc93e0 |
| 2025-04 | Adjoe | Domino Delights | Real UA | 10,733.60 | 0.00 | 10,733.60 | FINANCE_LEDGER FIN-000499 | snowflake.json /tables/38 FIN-000499 |
| 2025-04 | AppLovin | Domino Delights | Real UA | 799.85 | 0.00 | 799.85 | FINANCE_LEDGER FIN-000500 | snowflake.json /tables/38 FIN-000500 |
| 2025-04 | Google UAC | Domino Delights | Real UA | 12.51 | 0.00 | 12.51 | FINANCE_LEDGER FIN-000501 | snowflake.json /tables/38 FIN-000501 |
| 2025-04 | Meta | Domino Delights | Real UA | 1,597.65 | 0.09 | 1,597.56 | Meta receipts (account ending 3125) | frederick.stone@harmonygames.co/1828481095554769555; frederick.stone@harmonygames.co/1828641403961142838; frederick.stone@harmonygames.co/1828942627030969352; frederick.stone@harmonygames.co/1830495542195061363 |
| 2025-04 | Meta | Zombie Match 3D | Real UA | 700.29 | 0.00 | 700.29 | Meta receipts (account ending 3125) | frederick.stone@harmonygames.co/1828481095554769555; frederick.stone@harmonygames.co/1828641403961142838; frederick.stone@harmonygames.co/1828942627030969352; frederick.stone@harmonygames.co/1830495542195061363 |
| 2025-04 | Unity Ads | Domino Delights | Real UA | 109.68 | 0.00 | 109.68 | Unity statements (HG account) | f_ad44496a3e89c11de71d81 |
| 2025-04 | Unity Ads | Zombie Match 3D | Real UA | 1,184.77 | 0.00 | 1,184.77 | Unity statements (Calm Play) | f_1311b8c998f28831b1cf43 |
| 2025-05 | Adjoe | Domino Delights | Real UA | 20,537.92 | 0.00 | 20,537.92 | FINANCE_LEDGER FIN-000529 | snowflake.json /tables/38 FIN-000529 |
| 2025-05 | AppLovin | Domino Delights | Real UA | 1,564.82 | 0.00 | 1,564.82 | FINANCE_LEDGER FIN-000530 | snowflake.json /tables/38 FIN-000530 |
| 2025-05 | Meta | Domino Delights | Real UA | 17.99 | 0.00 | 17.99 | Meta receipts (account ending 3125) | frederick.stone@harmonygames.co/1831122183306732471; frederick.stone@harmonygames.co/1831236341456877471; frederick.stone@harmonygames.co/1831357377414065699; frederick.stone@harmonygames.co/1831376708658054054 |
| 2025-05 | Meta | Zombie Match 3D | Real UA | 2,318.85 | 0.00 | 2,318.85 | Meta receipts (account ending 3125) | frederick.stone@harmonygames.co/1831122183306732471; frederick.stone@harmonygames.co/1831236341456877471; frederick.stone@harmonygames.co/1831357377414065699; frederick.stone@harmonygames.co/1831376708658054054 |
| 2025-05 | Unity Ads | Zombie Match 3D | Real UA | 958.27 | 0.00 | 958.27 | Unity statements (Calm Play) | f_f7564f9413e650dd90cb74 |
| 2025-06 | Adjoe | Domino Delights | Real UA | 14,930.02 | 0.00 | 14,930.02 | FINANCE_LEDGER FIN-000555 | snowflake.json /tables/38 FIN-000555 |
| 2025-06 | AppLovin | Domino Delights | Real UA | 1,904.81 | 0.00 | 1,904.81 | FINANCE_LEDGER FIN-000556 split by AD_SPEND_DAILY game | snowflake.json /tables/38 FIN-000556 split by AD_SPEND_DAILY game |
| 2025-06 | AppLovin | Zombie Match 3D | Real UA | 42.58 | 0.00 | 42.58 | FINANCE_LEDGER FIN-000556 split by AD_SPEND_DAILY game | snowflake.json /tables/38 FIN-000556 split by AD_SPEND_DAILY game |
| 2025-06 | Meta | Zombie Match 3D | Real UA | 1,043.06 | 0.00 | 1,043.06 | Meta receipts (account ending 3125) | frederick.stone@harmonygames.co/1834164376568289766; frederick.stone@harmonygames.co/1835778053085762169 |
| 2025-06 | Unity Ads | Zombie Match 3D | Real UA | 3,381.12 | 0.00 | 3,381.12 | Unity statements (Calm Play) | f_66d70cbc162e336d8d9074; f_26f69b46d45852fb515912; f_a278aec0da8fbd8f7cd86d; f_3cdb6026a369e505609c3e |
| 2025-07 | AppLovin | Domino Delights | Real UA | 1,816.55 | 0.00 | 1,816.55 | FINANCE_LEDGER FIN-000579 split by AD_SPEND_DAILY game | snowflake.json /tables/38 FIN-000579 split by AD_SPEND_DAILY game |
| 2025-07 | AppLovin | Zombie Match 3D | Real UA | 21.83 | 0.00 | 21.83 | FINANCE_LEDGER FIN-000579 split by AD_SPEND_DAILY game | snowflake.json /tables/38 FIN-000579 split by AD_SPEND_DAILY game |
| 2025-07 | Meta | Zombie Match 3D | Real UA | 1,832.06 | 0.00 | 1,832.06 | Meta receipts (account ending 3125) | frederick.stone@harmonygames.co/1836836899676941724; frederick.stone@harmonygames.co/1836905421544429882; frederick.stone@harmonygames.co/1837801002582336665 |
| 2025-07 | Unity Ads | Zombie Match 3D | Real UA | 3,865.66 | 0.00 | 3,865.66 | Unity statements (Calm Play) | f_e923eb578c12cd3aa2b1ff; f_1a3c4303fe9b70a0c5d725; f_ac8e62864ae33cf47aef61; f_9a825acb7a3b71cfff45d0 |
| 2025-08 | AppLovin | Zombie Match 3D | Real UA | 75.80 | 0.00 | 75.80 | FINANCE_LEDGER FIN-000599 | snowflake.json /tables/38 FIN-000599 |
| 2025-08 | Meta | Zombie Match 3D | Real UA | 1,160.58 | 0.00 | 1,160.58 | Meta receipts (account ending 3125) | frederick.stone@harmonygames.co/1839693762261954189; frederick.stone@harmonygames.co/1842010914816895400 |
| 2025-08 | Unity Ads | Zombie Match 3D | Real UA | 6,736.82 | 0.00 | 6,736.82 | Unity statements (Calm Play) | f_389e010ecc827029d9cdcf; f_057df7adc2e2c887bf9f6f; f_e68b1465f0e0fa85fe2a9a; f_19c380c11615388ff75ce8 |
| 2025-09 | Meta | Zombie Match 3D | Fundraising | 816.23 | 61.63 | 754.60 | Meta receipts (account ending 3125) | frederick.stone@harmonygames.co/1843154072371887815; frederick.stone@harmonygames.co/1843244480594183249; frederick.stone@harmonygames.co/1843428112007517388; frederick.stone@harmonygames.co/1843516837725026041; frederick.stone@harmonygames.co/1843606994289346111; frederick.stone@harmonygames.co/1843697905828235234; frederick.stone@harmonygames.co/1843788314050589285; frederick.stone@harmonygames.co/1843878722273509005; frederick.stone@harmonygames.co/1843969633812798247; frederick.stone@harmonygames.co/1844059853292161439; frederick.stone@harmonygames.co/1844150953574592539; frederick.stone@harmonygames.co/1844241235968886522; frederick.stone@harmonygames.co/1844331958763627407; frederick.stone@harmonygames.co/1844422366986338173; frederick.stone@harmonygames.co/1844513089782197590; frederick.stone@harmonygames.co/1844603498005085849; frederick.stone@harmonygames.co/1844734171545827192 |
| 2025-09 | Unity Ads | Zombie Match 3D | Fundraising | 2,730.60 | 0.00 | 2,730.60 | Unity statements (Calm Play) | f_e8f75f70da75c40e9d395e; f_09666ca5c83c6a319ece41; f_76007a5c131f92019df2a0; f_0c302b9a0529823a0c6209 |
| 2025-09 | Unity Ads | Zombie Match 3D | Real UA | 679.90 | 0.00 | 679.90 | Unity statements (Calm Play) | f_e8f75f70da75c40e9d395e; f_09666ca5c83c6a319ece41; f_76007a5c131f92019df2a0; f_0c302b9a0529823a0c6209 |


Totals (net): Fundraising $3,485.20 · Real UA $111,387.92 · all $114,873.12 (Snowflake
$81,168.77). Gap list (spent, Snowflake $0): Meta 2025-05, Meta 2025-06, Meta 2025-07, Meta 2025-08, Meta 2025-09, Unity Ads 2024-10, Unity Ads 2024-11, Unity Ads 2024-12, Unity Ads 2025-01, Unity Ads 2025-02, Unity Ads 2025-03, Unity Ads 2025-04, Unity Ads 2025-05, Unity Ads 2025-06, Unity Ads 2025-07, Unity Ads 2025-08, Unity Ads 2025-09 (17 network-months). Duplicate
notifications dropped: frederick.stone@harmonygames.co/1830495542195061363, frederick.stone@harmonygames.co/1831122183306732471, frederick.stone@harmonygames.co/1831236341456877471 + the seeded frederick.stone@harmonygames.co/1843516837725026041. Zone-dependent charge:
frederick.stone@harmonygames.co/1820007110310927242 (Dec 31 2024 5:13 PM PST = Jan 1 01:13 UTC; both months fair). Adjoe Sep: no cost
(C07UCC631A6/1757349668.681539; a $0 row or no row). Unity Sep 30 is not on any statement before the freeze (export saved Sep 30 22:30Z).
Fair-reading tolerances the rubric must accept (V3 §9): rounded or exact cents; the Dec 31 charge in Dec or Jan; tablet from Sep 18 or
Sep 19 (no tablet spend on Sep 18); Adjoe Sep as $0 or omitted; register rows may merge or split same-key rows.

## 10 Integrations and companions

| Service | INT id | Companion seeded | Reason |
|---|---|---|---|
| gcal | INT-11 | yes: invitation mail frederick.stone@harmonygames.co/1843554523545665376 | organizer notified the attendee; the date also sits in that subject (alternate path) |
| gdrive | INT-13 | none | none seeded: a share DM is optional realism and no requirement reads it; the shares themselves are on the Drive rows |
| linear | INT-03 INT-04 INT-05 | none | the comment names no PR; Frederick is not subscribed to ENG-2362 |
| trello | INT-21 | none | integrations.json: no Trello → Slack integration exists |
| slack | INT-22 | none | none seeded: INT-22 mails are optional notifications; the hub itself is the record (C07C2866011/1759176840.271025) |
| gmail | — | gmail: none (no integration originates in Gmail) | — |
| confluence / contacts / gdocs / gsheets | — | none in integrations.json | — |

## 11 Touched-data census and coherence hazards

Touched records: the hub thread; #executives Sep 12 – 30 UA messages (C07C2866011/1757689941.099589 … C07C2866011/1759186080.203099);
the adjoe channel thread C07UCC631A6/1757346020.196019; 57 receipt threads; 6 top-ups; the Adjoe invoice threads; 19 revenue lookalikes
(T1–T3); the Unity Support and Singular-alert threads; ENG-2362; the UA/BD board (Doing list); both Confluence spaces' home pages
(parents); Leonard's and Frederick's Drive roots; AD_SPEND_DAILY, FINANCE_LEDGER; Frederick's Sep 18 calendar.

| Hazard (coherence_hazards.json) | Category | Intersects | Disposition |
|---|---|---|---|
| T02 | temporal | two-message receipt threads; Dec 31 2024 zone | folded in (T4/T5; both months accepted) |
| T07 | temporal | base records after the freeze (Oct 1 Adjoe mail, frederick.stone@harmonygames.co/1845217497507372901 Oct 6 receipt) | excluded: outside the window; nothing cites them |
| T08 | temporal | seeded Confluence authors | excluded: Simon and Frederick active_sep_2025 |
| S06 | semantic | Contacts job titles (175c0d7bc72ed244b944cb90) | excluded: neither modified nor cited |
| R04 | referential | Slack links to Google files | avoided: seeded messages name documents by title |
| R08 | referential | Gmail invitations vs calendar instances | companion seeded (INT-11) with one GCal row per attendee |
| Q05 | quantitative | ledger cash vs MONTHLY_BURN | excluded: only marketing_ua rows read |
| Q08 | quantitative | warehouse/ledger vs billing sources | dated_claim: hub claim + connector page explanation; no warehouse/ledger field modified |
| Q09 | quantitative | AD_SPEND_DAILY vs AD_SPEND vs UA_SPEND_UNIFIED_V2 | checked clean (snowflake.json /tables/0, /tables/34, /tables/3) |
| L08 | state/lifecycle | ENG-2362 updated_at vs comment | companion: updated_at bumped to 2025-08-13T17:42:00Z (SQL UPDATE) |
| L11 | state/lifecycle | UA/BD Done list closed (66da196af476ab78deaa0cf8) | avoided: seeded cards on Doing |
| L14 | state/lifecycle | June Adjoe booked (FIN-000555) vs Aug 4 reminder | dated explanation: the ledger books from Singular per month (connector page); register has no paid column |
| I03 | identifier/format | mailbox filename aliases | excluded: seeded ids use the roster address |
| I10 | identifier/format | Linear numbering | avoided: comment on base ENG-2362, no minted issue |
| I17 | identifier/format | Leonard's Trello id is a token | folded in: seeded actions use PERSON_6094_TRELLO_USER_ID |
| X03 | other | redacted vendor [USERNAME_14101] = Adjoe | folded in: sender SVC_2836 + adjoe channel identify it |

Sibling-defect sweep (state/lifecycle): every other #executives Unity budget change (C07C2866011/1733193039.806859 Dec 3 "$1";
C07C2866011/1732820975.715029 Nov 28 back to $400) is mirrored by the HG statements (no Dec 4 – 24 rows; Nov 28 rows resume); no
other Trello card on UA/BD mentions buckets (trello/data.json /cards, 40 on the board); the connector page names ENG-2362, and no other
Singular ticket says Unity cost is missing (title/description search: only ENG-2363, a splash-screen bug). People status: Frederick, Leonard, Robert, Simon are
active_sep_2025 (activity.json); nobody's presence decides a rule.

## 12 Platform follow-ups

- ○ carriers: none load-bearing (no GCal description, Slides notes, Drive content_text, Contacts description or Slack file).
- Confluence pages page_singular_cost_connectors and page_ua_spend_buckets: re-verify after regeneration.
- Slack thread encoding (thread_parent_id = parent row id, thread_ts_legacy = parent ts) follows the sample task; confirm the hub
  thread renders its two replies in the Opus pre-check.
- `hardness_gate.py` RecordText reads a base Gmail message (mailbox/RFC Message-ID) through `hg.py files`, which returns the invoice
  PDF path first for thread 1830999337380347892; T21's base version is therefore cited by file pointer
  (`gmail:threads/frederick@harmonygames.co_1830999337380347892.json /messages/1`). Tool bug, no data impact.
- No `call_budget` row is conditional on unverified behaviour.

## 13 Self-review

### Tool outputs (verbatim, final run)

`python3 Task_Authoring/tools/sql_lint.py Task_Authoring/task_inputs/01_Universe_Inject.sql`:

```
schemas touched (10): confluence, contacts, gcal, gdocs, gdrive, gmail, gsheets, linear, slack, trello
rows by schema: {'slack': 3, 'gmail': 75, 'gcal': 2, 'contacts': 1, 'gdrive': 50, 'gdocs': 19, 'gsheets': 57, 'confluence': 4, 'linear': 2, 'trello': 8}  total rows: 221  ops: {'insert': 219, 'update': 2}
errors: 0  warnings: 11
  warn  line 31: gmail.gmail_messages.date = 2025-08-31T22:15:00Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 35: gmail.gmail_messages.date = 2025-09-13T13:05:00Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 39: gmail.gmail_messages.date = 2025-09-14T13:02:00Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 57: gmail.gmail_messages.date = 2025-09-20T13:06:00Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 61: gmail.gmail_messages.date = 2025-09-21T13:03:00Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 85: gmail.gmail_messages.date = 2025-09-27T13:04:00Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 89: gmail.gmail_messages.date = 2025-09-28T13:06:00Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 431: confluence statement — unscoped and rarely opened by agents: make sure another record points here
  warn  line 435: confluence statement — unscoped and rarely opened by agents: make sure another record points here
  warn  line 437: confluence statement — unscoped and rarely opened by agents: make sure another record points here
  warn  line 439: confluence statement — unscoped and rarely opened by agents: make sure another record points here
```

Warning dispositions: weekend ×7 — automated Meta receipts arrive daily including weekends (base precedent: Sat Apr 26 2025
frederick.stone@harmonygames.co/1830495542195061363, Sun Oct 13 2024 frederick.stone@harmonygames.co/1812839883787768319);
disposition kept. Confluence ×4 — "unscoped and rarely opened": both pages are pointed to (the H2 doc names the connector page;
"UA spend buckets" search reaches the decoy page); disposition kept.

`python3 Task_Authoring/tools/base_check.py Task_Authoring/task_inputs/01_Universe_Inject.sql`:

```
BASE CHECK (/injection A + C, static): PASS  — 219 inserts, 2 updates
Check A — records, references, IDs: PASS
Check C — dates and relationships: PASS
  note: gsheets.sheets_sheets: no base-reference rules (checked by sql_lint only)
```

`python3 Task_Authoring/tools/hardness_gate.py Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.json Task_Authoring/task_inputs/01_Universe_Inject.sql`:

```
HARDNESS GATE (long): PASS
  [ok] effective_profile: effective_profile 'long' for 'Long Horizon' → thresholds 'long'
  [ok] sql_lint_clean: 0 lint error(s) — run tools/sql_lint.py
  [ok] base_consistency: /injection-style checks vs the base universe: A 0 finding(s), C 0 finding(s), 0 warning(s) — run tools/base_check.py --manifest
  [ok] persona_reach: 91 load-bearing seeded ids for frederick_stone (8 in unscoped services = visible, 83 judged by persona_view check-sql); not provably visible: none
  [ok] fact_consistency: fact_check: 0 error(s) (10 declared facts), 3 drift warning(s); first: none — run tools/fact_check.py --manifest --no-leak
  [ok] hazard_scope: 0 pre-existing hazard(s) among task-touched records; state/lifecycle or referential without a verified resolution: none
  [ok] services_injected: 10 schemas injected (confluence, contacts, gcal, gdocs, gdrive, gmail, gsheets, linear, slack, trello); need ≥ 10
  [ok] rows: 219 INSERTed rows (UPDATE companions not counted; 221 rows in all); need ≥ 120
  [ok] services_carrying_weight: 11 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: schemas injected but absent from the design: none
  [ok] seeded_ids_exist_in_sql: 126 seeded ids cited; missing from SQL: none
  [ok] anchors: 1 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 17 fragments; need ≥ 12
  [ok] ask_fragment_services: 11 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 15 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 13 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 116; need ≥ 30 (source-defined: True)
  [ok] evidence_surfaces: 3 surfaces over 3 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 54; need ≥ 30
  [ok] call_budget: unconditional (verified) floor 104 of 104 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 100 (Long Horizon; plan ~600 for headroom)
  [ok] call_budget_spread: 11 services in budget; largest share outside the per-record phase 19% (≤ 50%)
  [ok] traps: 22 traps across 11 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 10 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 5 supersessions (3 with versions in ≥ 2 services, 2 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: 5 trap(s) with version_records; the records' own timestamps (SQL created_at/ts/date/updated_at, or the base record) must be strictly increasing in the listed order (oldest first); bad: none
  [ok] distractors: 6 distractors of 5 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 12 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 7 chains with 7 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] hidden_authorities: 4 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 1 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 19 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 13 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 4 writes over 4 services; each must depend on findings
```

### /injection Checks A–C walk (`Evals/0_Injection_Quality_Eval.md`)

| Check | Verdict | Evidence |
|---|---|---|
| Inventory | PASS | 219 INSERT + 2 UPDATE (linear.linear_issues ENG-2362 updated_at; trello.trello_boards 66da196af476ab78deaa0cef dateLastActivity); no DELETE, no upsert |
| Check A — references (incl. archived/history) | PASS | channels C07C2866011 (not archived), board 66da196af476ab78deaa0cef + list 66da196af476ab78deaa0cf7 (open), ENG-2362, page_eng_home / page_prod_home, Drive roots d_63fffeb4fab5233ed5bb73 / d_175c0d7bc72ed244b944cb, base thread 1830999337380347892 (both mailboxes) |
| Check A — uniqueness over the full collection | PASS | 1.F lookups scan_complete, 0 hits; Slack (channel, ts) absent from the 2025-09 shard; Gmail thread numbers and Message-IDs absent from all thread files |
| Check A — ownership / membership / shares | PASS | Gmail copies only in sender/To/Cc mailboxes; GCal rows on organizer + attendee calendars; Docs/Sheets sharing = Drive rows; shares name roster people + PERSON_6098_EMAIL |
| Check A — ID contracts | PASS | Slack sha ids, Trello time-prefixed ids, f_/d_ + 22 hex, evt_ + 22 hex, ical 32hex@hg4, ver_ + 32 hex |
| Check B — structure, literal JSON, generated / NOT NULL | PASS | sql_lint 0 errors; every *_json literal parses; text_fts / body_text_fts never written |
| Check C — dates | PASS | latest seeded time 2025-09-30T23:40:00Z (frederick.stone@harmonygames.co/1844734171545827192); replies after parents; created ≤ updated |
| Check C — parent/reply, statuses, counts | PASS | hub reply_count 2 = SQL replies; H1 badges comments 1; ENG-2362 Todo with no completed_at |
| Check C — amounts, claimed updates, superseding records | PASS | statement totals = their rows; receipt lines = billed amounts; Adjoe 12,005.00 − 1,271.40 = 10,733.60; supersession chronology PASS (hardness_gate) |

### Counter-readings

| Category | Counter-reading (strongest argument it FAILS) | Evidence that resolves it | Verdict |
|---|---|---|---|
| Temporal | the hub (Sep 29 20:14Z) cites a Q4 pack created the same afternoon — could read as planted | f_0cd1e1402e8052d3d4e903 created 19:30Z, true-up card 68dae1bc8ec7eb683dc15a8d 19:45Z, hub after both | PASS |
| Temporal | the last Unity export says 'to date' yet the month is complete | export saved 2025-09-30T22:30Z (f_0c302b9a0529823a0c6209), rows through Sep 29; Sep 30 noted as unreported in §9.2 | PASS |
| Semantic / Category | the Calm Play statements look like the old alpha account the support thread describes | H2 scope line (f_4591ef30be4f920ba1ed14) + C07C2866011/1752552226.101149 | PASS |
| Cross-service Referential | the accountant's email is a token, not a real address, while the doc says 'she' | base convention: 0 literal external emails in 171 contacts; contacts:049f5555b01fd07b0f9d673c | PASS |
| Cross-service Referential | Frederick's copies of the May 6 / Jun 6 receipts duplicate base rows | different mailbox (Leonard's leonard.hayes@harmonygames.co/1831357378751331011); same ref [TAX_ID_5752] = same charge, new Message-ID | PASS |
| Quantitative | Unity Sep 13 statement spend ($622) vs warehouse installs (GB 71) implies an odd CPI | the statements carry no installs; Leonard 'we are spending $600/day' C07C2866011/1757793700.777559 | PASS |
| Quantitative | HG Unity Nov 2024 ($6.5K) is far above Singular's 238 installs | Slack claims ~250 installs/day at $4.69 (C07C2866011/1732989503.467909); pre-existing Singular gap, Q08 dated_claim | PASS |
| Quantitative | the warehouse Meta Oct–Apr ≠ receipts | connector page Meta row (page_singular_cost_connectors) + H2 'even where Snowflake shows something else' | PASS |
| State / Lifecycle | Unity budget set to $1 on Sep 19 yet campaigns could still bill | no UK retention rows Sep 20 – 28 (f_76007a5c131f92019df2a0, f_0c302b9a0529823a0c6209); $150/campaign from Sep 29 22:48Z (C07C2866011/1759186080.203099) | PASS |
| State / Lifecycle | sibling defect: another budget change not mirrored | Dec 3 '$1' (C07C2866011/1733193039.806859) → no HG rows Dec 4 – 24 (f_4a6e3125ed715725161c86); Nov 22 iOS paused → no iOS rows Nov 22 – 27 (f_41bc63b2332620eb08b80a) | PASS |
| Identifier / Format | minted tokens could collide with base redactions | 1.F sweep: PERSON_6098, IDENTIFIER_52803 … unused (max PERSON_6097 / IDENTIFIER_52802) | PASS |
| Temporal | v4: a brief dated after its campaign was first billed (/prompt DR5) | all 18 briefs swept against the first receipt or ad-approval mail naming each campaign; B16 now 2025-07-15 vs receipt Jul 15–17 (frederick.stone@harmonygames.co/1839693762261954189), B08 2024-12-30 vs Dec 30 – Jan 2 (frederick.stone@harmonygames.co/1820132039739740641); no 'Started:' line | PASS |
| Semantic / Category | v4: the connector page and the ledger's own comment describe FINANCE_LEDGER differently (/prompt DR6) | page now says amounts come from the Singular cost and that operating rows are dated to month end, true of every in-window operating row (snowflake.json /tables/38); no 'booked from' claim (page_singular_cost_connectors) | PASS |
| Cross-service Referential | v4: seeded Unity top-up mails duplicate base receipts with other amounts (/injection advisory 1) | each is Leonard's forward of a base receipt, quoting it (leonard.hayes@harmonygames.co/1843071417603742140 → frederick.stone@harmonygames.co/1843072786759807900); same amount and org; residual: the forward carries no PDF although the newer receipts mention one | PASS |
| People status | Frederick's Confluence user is is_active false | updated_at 2025-10-25 (after the freeze; Oct 24 layoffs); active_sep_2025 at the clock (activity.json) | PASS |
| Other | the rules doc reads as an answer key | principles only; no total, month list or outcome (fact_check: no register value in any seeded row); f_4591ef30be4f920ba1ed14 | PASS |
| Designed disagreement (Snowflake total) | the $81,169 vs register gap is an unintended inconsistency | dated human claim (C07C2866011/1759176840.271025) + dated explanation (page_singular_cost_connectors, Aug 14) | designed |
| Designed disagreement (rules versions) | three rule versions contradict each other | each later version names what it replaces (f_4591ef30be4f920ba1ed14 'replaces the rough rules'; C07C2866011/1759255500.938286 'one change') | designed |
| Designed disagreement (tablet) | card and comment disagree with no dated owner | comment by the rule owner's co-founder after the Sep 18 review (68d195a805df8c30c455f99c, evt_2f9b60002516e45ff04160) | designed |
| Designed disagreement ($20/day) | Leonard's figure could be right for later days | receipts after Sep 20 average ~$27/day (frederick.stone@harmonygames.co/1843878722273509005 …), Sep 16 – 19 far higher | designed |
| Designed disagreement (Adjoe PDF) | two Adjoe amounts with no resolution | dated credit reply May 7 in frederick.stone@harmonygames.co/1830999337380347892 = FIN-000499 | designed |
| Designed disagreement (Q3 vs Q4 pack) | two board packs, either could be the destination | the hub names the Q4 pack (C07C2866011/1759176840.271025); the Q3 pack is dated Jul 15 | designed |
| Designed disagreement (DD split) | the April DD split still governs Apr – Jun | Sep card: 'This replaces the DD incent test split from April' (68c99c40e5d9eb6f3a988838) | designed |
| Designed disagreement (Robert) | a co-founder's instruction is authoritative | Leonard owns the request (C07C2866011/1759176840.271025); Robert's reply carries no rule (C07C2866011/1759178460.557708) | designed |
| Designed disagreement (Meta warehouse) | receipts may be incomplete, so Snowflake should fill Feb/Mar | no account-3125 receipt exists in any mailbox for Feb – Mar 2025 (§1.B sweep); H2 'even where Snowflake shows something else' | designed |
| Designed disagreement (Calm Play) | the support thread says Calm Play is the old alpha account | Oct 2024 thread (frederick.stone@harmonygames.co/1813530307529968502) predates the May 2025 move (C07C2866011/1747847918.209079) | designed |

### Re-verified facts
Re-read from the sources in this stage: base receipt amounts / refs (38 threads, `model.base_receipts()` over the Gmail export), the two
Leonard-only receipts (leonard.hayes@harmonygames.co/1831357378751331011 $136.50, leonard.hayes@harmonygames.co/1834164377682810022
$143.06), FINANCE_LEDGER rows FIN-000333 … FIN-000599, AD_SPEND_DAILY by channel × game × month, the Unity Support thread
($1,673.43, $234.07), the Calm Play and top-up messages in #executives, ENG-2362 (Todo, created 2025-06-03T05:07:43Z), the UA/BD
board (lists, 40 cards, idShort max 40), Frederick's Sep 18 calendar (no 17:00Z conflict).

Unresolved: (1) the honest call minimum is 104 against V3's 100 — measured at the Opus pre-check; (2) no red team ran on the v3
injection (the local endpoint is unavailable; recommended, not required for injection); (3) Unity Sep 30 spend is on no statement
before the freeze — the register reflects the statements (H2), the human's rubric must accept it with or without a note.

```
STAGE GATE injection: PASS — Task_Authoring-2/task_inputs · 01_Universe_Inject.sql#c983da3d0a7d · 01_Hardness_Manifest.json#8b6e3c18def2 · 01_Grounding_Dossier.md#84d01f840c36 · blocking 0 · warnings 0 · checks 28
[PASS] structure.outputs: 3 output(s) present: 01_Universe_Inject.sql, 01_Hardness_Manifest.json, 01_Grounding_Dossier.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json)
[PASS] chain.scenario: upstream 'scenario' PASS pasted and current (01_Scenario_Design.md#23e3fa08eb19, 01_Hardness_Manifest.draft.json#0b36d392118d)
[PASS] structure.sections: 17 required sections present and non-empty (01_Grounding_Dossier.md)
[PASS] structure.placeholders: no placeholders in 01_Grounding_Dossier.md
[PASS] evidence.entity: 12/12 items carry a source pointer (min 90%)
[PASS] evidence.keyword: 26/26 items carry a source pointer (min 100%)
[PASS] evidence.persona_reach: 136/136 items carry a source pointer (min 100%)
[PASS] evidence.record_ledger: 93/93 items carry a source pointer (min 100%)
[PASS] evidence.facts_for_human: 135/135 items carry a source pointer (min 100%)
[PASS] tool.sql_lint: sql_lint re-run matches the paste: errors 0, warnings 11, rows 221
[PASS] review.warning_dispositions: every sql_lint warning class dispositioned (weekend×7, confluence statement — unscoped and rare×4)
[PASS] tool.base_check: base_check pasted PASS; re-run PASS
[PASS] tool.hardness_gate: hardness_gate (SQL) pasted PASS; re-run PASS
[PASS] structure.design_delta: final manifest keeps all 64 draft ids
[PASS] tool.check_sql_pasted: persona_view check-sql --load-bearing output pasted with verdict PASS
[PASS] reach.injection: 137 scoped load-bearing ids YES for frederick_stone
[PASS] structure.facts_declared: manifest declares 10 load-bearing fact(s) in `facts`
[PASS] tool.fact_check: fact_check --no-leak pasted PASS; re-run PASS
[PASS] kb.coherence_hazards: coherence audit cites 15 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 4 seeded speakers each cited with activity.json status; conventions.json cited
[PASS] kb.integrations: companions listed per integrations.json (7 INT ids, services ['confluence', 'contacts', 'gcal', 'gdocs', 'gdrive', 'gmail', 'gsheets', 'linear', 'slack', 'trello'])
[PASS] boundary.anchor_naming: 2 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 25 evidenced counter-readings (of 26 found; need ≥ 17) in 01_Grounding_Dossier.md
[PASS] review.coverage: self-review addresses all 9 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```
