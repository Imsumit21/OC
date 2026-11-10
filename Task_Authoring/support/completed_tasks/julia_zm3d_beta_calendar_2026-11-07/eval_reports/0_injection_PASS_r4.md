# Injection data-integrity review: Eval 0

## 1. Scope

| Field | Value |
|---|---|
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`; nothing reused (almost every statement changed from the previously reviewed SQL, so the whole file was checked new against the base) |
| Mode | Chat review, audit (attempt 6aea4c1e9b621f28dc3a5332) |
| Review time | 2026-11-06 |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Input | `Evals/task_inputs/01_Universe_Inject.sql` (injection revision 9, uploaded as `01_Universe_Inject (5).sql`), 59,622 bytes, SHA-256 `0e8c8ad83f3be435db1f9268f114c916f52293993eb687a55b34005015f9f815` (attachment to the /injection message) |
| Previous version | SHA-256 `3afbf7cbbdb7611dad909cfc7244829642e03e136b66c5c555fe77d28570dd63` (PASS / COMPLETE); that report is superseded |
| Schema snapshot | `Evals/references/schema/injection.json` SHA-256 `31dcb2b43feca8e5c7cb67f37973f819c9b9774f12f8b15cb7da89ecd74c5151` (unverified snapshot, provisional) |
| ID contracts | `Evals/references/schema/id_contracts.json` SHA-256 `fc4711ef07667333c1cf2a417279826f0432539195f7acdfacfa86e9d9ed4682` |
| Lint | `hg_injection_lint.py` injection-lint-v1 |

## 2. Input / authority issues

- SQL comments mention a dossier and `universe_schema_live.json`; neither was supplied. Treated as statements of intent, not evidence. Line 6 ("Re-apply this exact SQL before every agent run") is operational and is not about tool calls, pass rate or gates.
- No padding comments. Grader-facing text: lint found none; the manual read of every injected text field also found none (see Check C).

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, manifest and version | NEW, done (revision 9 saved and hash verified) |
| Run lint; resolve every flag | NEW, done (0 flags) |
| Inventory every statement | NEW, done: 96 statements (71 INSERT, 25 UPDATE; no DELETE, upsert or ON CONFLICT). Every INSERT has matching column/value counts; every UPDATE has a single-row WHERE on the primary key; no duplicate assignments |
| Check A | NEW: PASS |
| Check B | NEW: PASS (snapshot mismatches advisory) |
| Check C | NEW: PASS |
| Report coverage, findings, limits, verdict | done |

## 4. Lint

`hg_injection_lint.py` ran on SHA `0e8c8ad8…f815` against universe synthcut, clock 2025-10-01T07:00:00Z, loading slack/users, gmail/users, github, linear, trello, contacts and confluence. Counts: FAIL 0, CHECK 0, INFO 0 (checks: future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape). Nothing to resolve. A clean lint is not a PASS, so checks A–C were done in full.

## 5. Operation ledger (all 96 statements, execution order)

Paths are relative to the synth-cut service folders. Base absence checks were complete scans (Gmail: 81,404 thread files / 95,164 messages, `scan_complete: true`; gdocs 595, gslides 132, gsheets 356 records, `scan_complete: true`; Slack: every month file of the five channels touched; GitHub, Linear, Trello, GCal, Drive: full collections loaded).

| # | SQL line | Table | Op | Key | Before/after & references | Source checked | Result |
|---|---|---|---|---|---|---|---|
| 1 | 11 | slack.slack_messages | INSERT | `bca784379e7dbca9e64e79a64dfefbba` | D05SD5QLG94 · EMPLOYEE_0008_SLACK_ID · ts 1759263617.418209 · parent — | slack/messages/<ch>/2025-0*.json | PASS |
| 2 | 13 | slack.slack_messages | INSERT | `890dc27f56e8501bd7590ffdfc231057` | D05SD5QLG94 · EMPLOYEE_0008_SLACK_ID · ts 1759263878.305129 · parent bca784379e7dbca9e64e79a64dfefbba | slack/messages/<ch>/2025-0*.json | PASS |
| 3 | 15 | slack.slack_messages | INSERT | `933cee9f6464a80e4b1f05259b595b20` | C08R8CHB0QL · EMPLOYEE_0016_SLACK_ID · ts 1758213623.552919 · parent 9025d428af1f551a20e303c3acbc545b | slack/messages/<ch>/2025-0*.json | PASS |
| 4 | 17 | slack.slack_messages | INSERT | `669d15f685f158633e56302160957f1e` | D05GU6L0XFH · EMPLOYEE_0016_SLACK_ID · ts 1759270241.638119 · parent — | slack/messages/<ch>/2025-0*.json | PASS |
| 5 | 19 | slack.slack_messages | INSERT | `b5f2955c2e154efc6835946ecfe1758e` | C0880U9751A · EMPLOYEE_0012_SLACK_ID · ts 1759265412.481909 · parent — | slack/messages/<ch>/2025-0*.json | PASS |
| 6 | 21 | slack.slack_messages | UPDATE | `9025d428af1f551a20e303c3acbc545b` | SET thread_ts_legacy=1758121809.236839, reply_count=1, reply_users_count=1, latest_reply=1758213623.552919 | slack/messages/<ch>/2025-0*.json | PASS |
| 7 | 23 | gmail.gmail_threads | INSERT | `brian.foster@harmonygames.co/1843954828968110017` | brian.foster@harmonygames.co ·  | gmail/threads/*.json | PASS |
| 8 | 24 | gmail.gmail_messages | INSERT | `brian.foster@harmonygames.co/<CAPT--p4sBC8XnaA7qBDMtZkWqJPiXP0MT3deOQGPusOZhHF+vo@mail.gmail.com>` | brian.foster@harmonygames.co · 2025-09-22T09:12:41+00:00 | gmail/threads/*.json#/messages | PASS |
| 9 | 34 | gmail.gmail_threads | INSERT | `julia.lawson@harmonygames.co/1843954828968533812` | julia.lawson@harmonygames.co ·  | gmail/threads/*.json | PASS |
| 10 | 35 | gmail.gmail_messages | INSERT | `julia.lawson@harmonygames.co/<CAPT--p4sBC8XnaA7qBDMtZkWqJPiXP0MT3deOQGPusOZhHF+vo@mail.gmail.com>` | julia.lawson@harmonygames.co · 2025-09-22T09:12:41+00:00 | gmail/threads/*.json#/messages | PASS |
| 11 | 45 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843954828968789474` | frederick.stone@harmonygames.co ·  | gmail/threads/*.json | PASS |
| 12 | 46 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAPT--p4sBC8XnaA7qBDMtZkWqJPiXP0MT3deOQGPusOZhHF+vo@mail.gmail.com>` | frederick.stone@harmonygames.co · 2025-09-22T09:12:41+00:00 | gmail/threads/*.json#/messages | PASS |
| 13 | 56 | gmail.gmail_threads | INSERT | `brian.foster@harmonygames.co/1844311412965607905` | brian.foster@harmonygames.co ·  | gmail/threads/*.json | PASS |
| 14 | 57 | gmail.gmail_messages | INSERT | `brian.foster@harmonygames.co/<CAPT--p4a5fY9wd6vr+8JtjFXfffkxQOCEUYsuqSPy9HbQJu3Fs@mail.gmail.com>` | brian.foster@harmonygames.co · 2025-09-26T07:40:26+00:00 | gmail/threads/*.json#/messages | PASS |
| 15 | 65 | gmail.gmail_threads | INSERT | `julia.lawson@harmonygames.co/1844311412966040123` | julia.lawson@harmonygames.co ·  | gmail/threads/*.json | PASS |
| 16 | 66 | gmail.gmail_messages | INSERT | `julia.lawson@harmonygames.co/<CAPT--p4a5fY9wd6vr+8JtjFXfffkxQOCEUYsuqSPy9HbQJu3Fs@mail.gmail.com>` | julia.lawson@harmonygames.co · 2025-09-26T07:40:26+00:00 | gmail/threads/*.json#/messages | PASS |
| 17 | 74 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844311412966288046` | frederick.stone@harmonygames.co ·  | gmail/threads/*.json | PASS |
| 18 | 74 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAPT--p4a5fY9wd6vr+8JtjFXfffkxQOCEUYsuqSPy9HbQJu3Fs@mail.gmail.com>` | frederick.stone@harmonygames.co · 2025-09-26T07:40:26+00:00 | gmail/threads/*.json#/messages | PASS |
| 19 | 82 | gcal.gcal_events | INSERT | `evt_9a4c2e7f1b3d58e06c7a2f` | cal douglas@harmonygames.co · 2025-10-08 15:00:00+00–16:00 · ical 3f8e1c6a…@hg4 | gcal/data.json#/events | PASS |
| 20 | 84 | gcal.gcal_events | INSERT | `evt_5c1e83a7d94b02f6c8e31a` | cal julia.lawson@harmonygames.co · 2025-10-08 15:00:00+00–16:00 · ical 3f8e1c6a…@hg4 | gcal/data.json#/events | PASS |
| 21 | 86 | gcal.gcal_events | INSERT | `evt_a72f4d9e0c1b58d3e6f40b` | cal owen.baker@harmonygames.co · 2025-10-08 15:00:00+00–16:00 · ical 3f8e1c6a…@hg4 | gcal/data.json#/events | PASS |
| 22 | 88 | gcal.gcal_events | INSERT | `evt_1d6b9a03e5c27f84b0d92c` | cal frederick.stone@harmonygames.co · 2025-10-08 15:00:00+00–16:00 · ical 3f8e1c6a…@hg4 | gcal/data.json#/events | PASS |
| 23 | 90 | gdrive.drive_files | INSERT | `d_5f2c8e1b7a94d03c6e2b58` | ZM Live Ops · folder · owner julia.lawson@harmonygames.co · parent ["d_8140f09bf9f1b94cb8ee2d"] | gdrive/data.json#/drive_files | PASS |
| 24 | 92 | gdrive.drive_files | INSERT | `f_7c3e91a4d2b85f60e1a9c4` | ZM3D beta live-ops calendar - working rules.docx · document · owner frederick.stone@harmonygames.co · parent ["d_175c0d7bc72ed244b944cb"] | gdrive/data.json#/drive_files | PASS |
| 25 | 93 | gdocs.docs_documents | INSERT | `f_7c3e91a4d2b85f60e1a9c4` | document_id, title, owner_email, shared_with_emails_json | gdocs/data.json#/docs_documents | PASS |
| 26 | 113 | gdrive.drive_files | INSERT | `f_2b9d4e7a1c63f08d5e7b21` | ZM3D beta UA plan · presentation · owner frederick.stone@harmonygames.co · parent ["d_175c0d7bc72ed244b944cb"] | gdrive/data.json#/drive_files | PASS |
| 27 | 114 | gslides.slides_presentations | INSERT | `f_2b9d4e7a1c63f08d5e7b21` | presentation_id, title, owner_email, shared_with_emails_json | gslides/data.json | PASS |
| 28 | 115 | gslides.slides_pages | INSERT | `f_2b9d4e7a1c63f08d5e7b21` | presentation_id, object_id, index, layout | (new presentation) | PASS |
| 29 | 116 | gslides.slides_page_elements | INSERT | `f_2b9d4e7a1c63f08d5e7b21` | presentation_id, page_object_id, object_id, kind | (new presentation) | PASS |
| 30 | 119 | gslides.slides_pages | INSERT | `f_2b9d4e7a1c63f08d5e7b21` | presentation_id, object_id, index, layout | (new presentation) | PASS |
| 31 | 120 | gslides.slides_page_elements | INSERT | `f_2b9d4e7a1c63f08d5e7b21` | presentation_id, page_object_id, object_id, kind | (new presentation) | PASS |
| 32 | 126 | gslides.slides_pages | INSERT | `f_2b9d4e7a1c63f08d5e7b21` | presentation_id, object_id, index, layout | (new presentation) | PASS |
| 33 | 127 | gslides.slides_page_elements | INSERT | `f_2b9d4e7a1c63f08d5e7b21` | presentation_id, page_object_id, object_id, kind | (new presentation) | PASS |
| 34 | 130 | gdrive.drive_files | INSERT | `f_e4a17c90b3d25f6a8c1d73` | ZM3D Beta Live-Ops Calendar.xlsx · spreadsheet · owner julia.lawson@harmonygames.co · parent ["d_5f2c8e1b7a94d03c6e2b58"] | gdrive/data.json#/drive_files | PASS |
| 35 | 131 | gsheets.sheets_spreadsheets | INSERT | `f_e4a17c90b3d25f6a8c1d73` | spreadsheet_id, title, owner_email, shared_with_emails_json | gsheets/data.json#/sheets_spreadsheets | PASS |
| 36 | 132 | gsheets.sheets_sheets | INSERT | `f_e4a17c90b3d25f6a8c1d73` | spreadsheet_id, sheet_id, title, index | (new spreadsheet) | PASS |
| 37 | 133 | gsheets.sheets_sheets | INSERT | `f_e4a17c90b3d25f6a8c1d73` | spreadsheet_id, sheet_id, title, index | (new spreadsheet) | PASS |
| 38 | 138 | github.github_review_comments | INSERT | `harmonygames-Games/match3d#470#rc_10` | harmonygames-Games/match3d#470 · EMPLOYEE_0025_GITHUB_USERNAME · 2025-09-30T15:51:06Z | github/data.json#/review_comments | PASS |
| 39 | 140 | github.github_reviews | INSERT | `harmonygames-Games/match3d#468#rev_3` | harmonygames-Games/match3d#468 · EMPLOYEE_0025_GITHUB_USERNAME · 2025-09-29T15:36:41Z | github/data.json#/reviews | PASS |
| 40 | 141 | github.github_review_comments | INSERT | `harmonygames-Games/match3d#468#rc_38` | harmonygames-Games/match3d#468 · EMPLOYEE_0025_GITHUB_USERNAME · 2025-09-29T15:36:41Z | github/data.json#/review_comments | PASS |
| 41 | 142 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d#468#ev_6` | harmonygames-Games/match3d#468 · reviewed · None | github/data.json#/timeline_events | PASS |
| 42 | 144 | slack.slack_messages | INSERT | `73bc730c620936feba3dcfbba00e2745` | C093LEZGF6J · SLACK_BOT_0004_SLACK_ID · ts 1759247468.897619 · parent c2b9c90355cf8c2c4326ab19d3a24f79 | slack/messages/<ch>/2025-0*.json | PASS |
| 43 | 146 | slack.slack_messages | UPDATE | `c2b9c90355cf8c2c4326ab19d3a24f79` | SET reply_count=17, latest_reply=1759247478.371389 | slack/messages/<ch>/2025-0*.json | PASS |
| 44 | 148 | github.github_review_comments | INSERT | `harmonygames-Games/match3d#472#rc_1` | harmonygames-Games/match3d#472 · EMPLOYEE_0025_GITHUB_USERNAME · 2025-09-30T15:52:58Z | github/data.json#/review_comments | PASS |
| 45 | 150 | slack.slack_messages | INSERT | `65564543e4bc8dd707a177aada2337a3` | C093LEZGF6J · SLACK_BOT_0004_SLACK_ID · ts 1759247580.842719 · parent 61f686b8a8b6c164b14aff6b5b1897bf | slack/messages/<ch>/2025-0*.json | PASS |
| 46 | 152 | slack.slack_messages | UPDATE | `61f686b8a8b6c164b14aff6b5b1897bf` | SET reply_count=4, latest_reply=1759247586.958099 | slack/messages/<ch>/2025-0*.json | PASS |
| 47 | 154 | slack.slack_messages | INSERT | `78aa8ed77c0bd7b8a3fad227b22bc3fb` | C093LEZGF6J · SLACK_BOT_0004_SLACK_ID · ts 1759160203.696979 · parent 4b7c41278397b56b36e9b2f8a820c454 | slack/messages/<ch>/2025-0*.json | PASS |
| 48 | 156 | slack.slack_messages | UPDATE | `4b7c41278397b56b36e9b2f8a820c454` | SET reply_count=42, latest_reply=1759162433.383449 + attachments_json (Reviewers field only) | slack/messages/<ch>/2025-0*.json | PASS |
| 49 | 161 | linear.linear_comments | INSERT | `cmt_zom429_1` | ZOM-429 · usr_cd7849ec043ab3da · 2025-09-16T18:12:04Z · seq 1 | linear/data.json#/comments (0 base rows), /users | PASS |
| 50 | 163 | linear.linear_comments | INSERT | `cmt_zom556_1` | ZOM-556 · usr_65c76e0b87aa7e9b · 2025-09-24T15:20:38Z · seq 1 | linear/data.json#/comments (0 base rows), /users | PASS |
| 51 | 164 | linear.linear_issues | UPDATE | `ZOM-556` | SET updated_at=2025-09-24T15:20:38Z | linear/data.json#/issues | PASS |
| 52 | 166 | linear.linear_comments | INSERT | `cmt_zom565_1` | ZOM-565 · usr_c77c50cc15c5342d · 2025-09-29T14:34:12Z · seq 1 | linear/data.json#/comments (0 base rows), /users | PASS |
| 53 | 167 | linear.linear_issues | UPDATE | `ZOM-565` | SET updated_at=2025-09-29T14:34:12Z | linear/data.json#/issues | PASS |
| 54 | 169 | linear.linear_comments | INSERT | `cmt_zom543_1` | ZOM-543 · usr_49b9dfa5208d400d · 2025-09-30T16:20:37Z · seq 1 | linear/data.json#/comments (0 base rows), /users | PASS |
| 55 | 170 | linear.linear_issues | UPDATE | `ZOM-543` | SET updated_at=2025-09-30T16:20:37Z | linear/data.json#/issues | PASS |
| 56 | 172 | linear.linear_comments | INSERT | `cmt_zom526_1` | ZOM-526 · usr_fc22d5941b2aeb5c · 2025-09-24T17:30:35Z · seq 1 | linear/data.json#/comments (0 base rows), /users | PASS |
| 57 | 173 | linear.linear_comments | INSERT | `cmt_zom526_2` | ZOM-526 · usr_fc22d5941b2aeb5c · 2025-09-26T15:40:50Z · seq 2 | linear/data.json#/comments (0 base rows), /users | PASS |
| 58 | 174 | linear.linear_comments | INSERT | `cmt_zom526_3` | ZOM-526 · usr_49b9dfa5208d400d · 2025-09-30T16:24:19Z · seq 3 | linear/data.json#/comments (0 base rows), /users | PASS |
| 59 | 175 | linear.linear_issues | UPDATE | `ZOM-526` | SET updated_at=2025-09-30T16:24:19Z | linear/data.json#/issues | PASS |
| 60 | 177 | linear.linear_comments | INSERT | `cmt_zom552_1` | ZOM-552 · usr_bdf01b53c6a92c5e · 2025-09-26T15:45:23Z · seq 1 | linear/data.json#/comments (0 base rows), /users | PASS |
| 61 | 178 | linear.linear_issues | UPDATE | `ZOM-552` | SET updated_at=2025-09-26T15:45:23Z | linear/data.json#/issues | PASS |
| 62 | 180 | linear.linear_comments | INSERT | `cmt_zom534_1` | ZOM-534 · usr_cd7849ec043ab3da · 2025-09-25T16:35:04Z · seq 1 | linear/data.json#/comments (0 base rows), /users | PASS |
| 63 | 181 | linear.linear_issues | UPDATE | `ZOM-534` | SET updated_at=2025-09-25T16:35:04Z | linear/data.json#/issues | PASS |
| 64 | 183 | linear.linear_comments | INSERT | `cmt_zom432_1` | ZOM-432 · usr_49b9dfa5208d400d · 2025-09-24T16:10:28Z · seq 1 | linear/data.json#/comments (0 base rows), /users | PASS |
| 65 | 184 | linear.linear_comments | INSERT | `cmt_zom432_2` | ZOM-432 · usr_caafeec2804b3a67 · 2025-09-30T21:07:26Z · seq 2 | linear/data.json#/comments (0 base rows), /users | PASS |
| 66 | 185 | linear.linear_issues | UPDATE | `ZOM-432` | SET state_id=Done, completed_at=2025-09-30T21:07:26Z, updated_at=2025-09-30T21:07:26Z | linear/data.json#/issues | PASS |
| 67 | 187 | linear.linear_comments | INSERT | `cmt_zom78_1` | ZOM-78 · usr_175c0d7bc72ed244 · 2025-09-30T18:15:14Z · seq 1 | linear/data.json#/comments (0 base rows), /users | PASS |
| 68 | 188 | linear.linear_issues | UPDATE | `ZOM-78` | SET updated_at=2025-09-30T18:15:14Z | linear/data.json#/issues | PASS |
| 69 | 190 | linear.linear_comments | INSERT | `cmt_zom465_1` | ZOM-465 · usr_c77c50cc15c5342d · 2025-09-26T18:10:01Z · seq 1 | linear/data.json#/comments (0 base rows), /users | PASS |
| 70 | 191 | linear.linear_comments | INSERT | `cmt_zom465_2` | ZOM-465 · usr_c77c50cc15c5342d · 2025-09-30T18:05:02Z · seq 2 | linear/data.json#/comments (0 base rows), /users | PASS |
| 71 | 192 | linear.linear_issues | UPDATE | `ZOM-465` | SET updated_at=2025-09-30T18:05:02Z | linear/data.json#/issues | PASS |
| 72 | 194 | linear.linear_comments | INSERT | `cmt_zom344_1` | ZOM-344 · usr_c77c50cc15c5342d · 2025-09-16T16:20:28Z · seq 1 | linear/data.json#/comments (0 base rows), /users | PASS |
| 73 | 195 | linear.linear_issues | UPDATE | `ZOM-344` | SET state_id=Done, completed_at=2025-09-16T16:20:28Z, updated_at=2025-09-16T16:20:28Z | linear/data.json#/issues | PASS |
| 74 | 197 | linear.linear_comments | INSERT | `cmt_zom442_1` | ZOM-442 · usr_bdf01b53c6a92c5e · 2025-09-19T15:10:51Z · seq 1 | linear/data.json#/comments (0 base rows), /users | PASS |
| 75 | 198 | linear.linear_issues | UPDATE | `ZOM-442` | SET updated_at=2025-09-19T15:10:51Z | linear/data.json#/issues | PASS |
| 76 | 200 | linear.linear_comments | INSERT | `cmt_zom471_1` | ZOM-471 · usr_caafeec2804b3a67 · 2025-09-17T16:45:30Z · seq 1 | linear/data.json#/comments (0 base rows), /users | PASS |
| 77 | 201 | linear.linear_issues | UPDATE | `ZOM-471` | SET updated_at=2025-09-17T16:45:30Z | linear/data.json#/issues | PASS |
| 78 | 203 | linear.linear_comments | INSERT | `cmt_zom504_1` | ZOM-504 · usr_65c76e0b87aa7e9b · 2025-09-22T15:30:39Z · seq 1 | linear/data.json#/comments (0 base rows), /users | PASS |
| 79 | 204 | linear.linear_issues | UPDATE | `ZOM-504` | SET updated_at=2025-09-22T15:30:39Z | linear/data.json#/issues | PASS |
| 80 | 206 | linear.linear_comments | INSERT | `cmt_zom517_1` | ZOM-517 · usr_Robert · 2025-09-18T17:40:54Z · seq 1 | linear/data.json#/comments (0 base rows), /users | PASS |
| 81 | 207 | linear.linear_issues | UPDATE | `ZOM-517` | SET updated_at=2025-09-18T17:40:54Z | linear/data.json#/issues | PASS |
| 82 | 209 | linear.linear_comments | INSERT | `cmt_zom521_1` | ZOM-521 · usr_49b9dfa5208d400d · 2025-09-26T17:25:02Z · seq 1 | linear/data.json#/comments (0 base rows), /users | PASS |
| 83 | 210 | linear.linear_comments | INSERT | `cmt_zom521_2` | ZOM-521 · usr_49b9dfa5208d400d · 2025-09-30T16:27:38Z · seq 2 | linear/data.json#/comments (0 base rows), /users | PASS |
| 84 | 211 | linear.linear_issues | UPDATE | `ZOM-521` | SET updated_at=2025-09-30T16:27:38Z + description (two items unticked) | linear/data.json#/issues | PASS |
| 85 | 220 | linear.linear_comments | INSERT | `cmt_zom542_1` | ZOM-542 · usr_caafeec2804b3a67 · 2025-09-22T18:40:21Z · seq 1 | linear/data.json#/comments (0 base rows), /users | PASS |
| 86 | 221 | linear.linear_issues | UPDATE | `ZOM-542` | SET updated_at=2025-09-22T18:40:21Z | linear/data.json#/issues | PASS |
| 87 | 223 | linear.linear_comments | INSERT | `cmt_zom544_1` | ZOM-544 · usr_65c76e0b87aa7e9b · 2025-09-29T15:35:50Z · seq 1 | linear/data.json#/comments (0 base rows), /users | PASS |
| 88 | 224 | linear.linear_issues | UPDATE | `ZOM-544` | SET updated_at=2025-09-29T15:35:50Z | linear/data.json#/issues | PASS |
| 89 | 226 | linear.linear_comments | INSERT | `cmt_zom546_1` | ZOM-546 · usr_4e13bd40cc73d0fc · 2025-09-24T19:00:57Z · seq 1 | linear/data.json#/comments (0 base rows), /users | PASS |
| 90 | 227 | linear.linear_issues | UPDATE | `ZOM-546` | SET updated_at=2025-09-24T19:00:57Z | linear/data.json#/issues | PASS |
| 91 | 229 | linear.linear_comments | INSERT | `cmt_zom549_1` | ZOM-549 · usr_65c76e0b87aa7e9b · 2025-09-26T16:50:46Z · seq 1 | linear/data.json#/comments (0 base rows), /users | PASS |
| 92 | 230 | linear.linear_issues | UPDATE | `ZOM-549` | SET updated_at=2025-09-26T16:50:46Z | linear/data.json#/issues | PASS |
| 93 | 232 | linear.linear_comments | INSERT | `cmt_zom566_1` | ZOM-566 · usr_4e13bd40cc73d0fc · 2025-09-30T19:40:47Z · seq 1 | linear/data.json#/comments (0 base rows), /users | PASS |
| 94 | 233 | linear.linear_issues | UPDATE | `ZOM-566` | SET state_id=In Progress, started_at=2025-09-30T17:20:13Z, updated_at=2025-09-30T19:40:47Z | linear/data.json#/issues | PASS |
| 95 | 235 | trello.trello_actions | INSERT | `68dac8204f1e9a3b7c2d5e61` | id, type, date, idmembercreator | trello/data.json#/actions | PASS |
| 96 | 237 | trello.trello_cards | UPDATE | `68c452a03006277f55d9dc96` | badges_json, datelastactivity | trello/data.json#/cards | PASS |
## 6. Check A: records, references and IDs: PASS

**Actors (one account per person, author resolves to the named person).**
- Slack: `EMPLOYEE_0008` = Frederick Stone, `EMPLOYEE_0016` = Robert, `EMPLOYEE_0012` = Vincent Parker, `SLACK_BOT_0004` = GitHub bot (users.json). Membership: D05SD5QLG94 lists EMPLOYEE_0005 (Julia) and 0008; D05GU6L0XFH lists 0005 and 0016; #zombie-art C08R8CHB0QL has 0016; #zombie-match3d C0880U9751A has 0012; #zombie-prs C093LEZGF6J has SLACK_BOT_0004.
- Gmail: brian.foster@, julia.lawson@, frederick.stone@ all have mailboxes (users.json). Label `Label_b19fb8d1b3` exists (name "Opened"), matching the "Opened" entry in each X-Gmail-Labels header that carries it.
- GitHub: `EMPLOYEE_0025_GITHUB_USERNAME` = Arthur Blake (users). The Slack mirrors credit `arthur.blake`, matching.
- Linear: all ten author ids exist: usr_cd7849… douglas@, usr_65c76e… vincent.parker@, usr_c77c50… marcus.bennett@, usr_49b9df… calvin.price@, usr_fc22d5… brian.foster@, usr_bdf01b… oliver.brooks@, usr_caafee… samuel.turner@, usr_175c0d… frederick.stone@, usr_Robert robert@, usr_4e13bd… owen.baker@. Only one Robert account exists in Linear.
- Trello: `PERSON_6094_TRELLO_USER_ID` = Leonard Hayes (members), who also created this card.
- GCal: the four calendars exist (douglas@, julia.lawson@, owen.baker@, frederick.stone@, all primary). Drive: Julia and Frederick are drive_users; parents `d_8140f09bf9f1b94cb8ee2d` and `d_175c0d7bc72ed244b944cb` are their own root folders.

**Parents and targets.**
- Slack thread parents exist with these base values: `9025d428…` (#zombie-art, Martin Walsh's Halloween post, ts 1758121809.236839, 0 replies); `c2b9c903…` (#470 opened, 16 bot replies, latest 1759247478.371389); `61f686b8…` (#472 opened, 3 replies, latest 1759247586.958099); `4b7c4127…` (#468 opened, 41 replies, latest 1759162433.383449).
- GitHub PRs #468, #470, #471, #472 and #475 exist (all merged). Review refs `#470#rev_9` (Arthur, APPROVED 2025-09-30T15:51:06Z) and `#472#rev_1` (Arthur, APPROVED 15:52:58Z) exist; `#468#rev_3` is created in the same SQL before its comment.
- Linear: all 21 target issues exist (ZOM-78, 344, 429, 432, 442, 465, 471, 504, 517, 521, 526, 534, 542, 543, 544, 546, 549, 552, 556, 565, 566). The issues named in comment text also exist: ZOM-528 and ZOM-541 (In Progress), PR #471 (ZOM-498/536, "updated Daily Gift sprite configuration"), PR #475 (body "Adding card pack animation").
- Trello: card `68c452a03006277f55d9dc96`, board `6851a6569f3bf818760632ab` (ZM ROADMAP) and list `6851a674975da1fe76e70d93` exist.
- Gdocs/gslides/gsheets child rows point at drive files inserted earlier in the SQL; slides page elements point at pages inserted just before them.

**New keys: no collisions.**
- Slack: 8 new message ids and their channel ts are absent from every month file of their channels; no two new rows share a ts.
- Gmail: 6 message ids absent (complete scan); the numeric thread ids 1843954828968…/1844311412965…/1844311412966… appear nowhere in the 81,404 thread files.
- GCal: 4 event ids and the ical_uid are absent from the 10,395 events. One event_id per calendar with a shared ical_uid matches the base pattern (802 shared iCal UIDs).
- Drive: 4 ids absent from the 53,631 drive_files; the sheet's web_view_link id is unused. The document, presentation and spreadsheet ids are absent from gdocs, gslides and gsheets.
- GitHub: `#470#rc_10` follows rc_1–rc_9, `#468#rc_38` follows rc_1–rc_37, `#468#rev_3` follows rev_1–2, `#468#ev_6` follows ev_1–5, and `#472#rc_1` is the first comment on #472. None exist in reviews, review_comments, timeline_events or pull_request_comments. The three discussion ids in the mirrors (r2391980467, r2391985983, r2388843617) appear nowhere else.
- Linear: the base comments array is empty (0 rows), so the 26 new `cmt_*` ids cannot collide. They are unique within the SQL, and each issue's sequence numbers run from 1.
- Trello: action `68dac8204f1e9a3b7c2d5e61` is absent from the 5,252 actions.

**Listed ID contracts and Drive readability.** Gmail history_id is NULL on every thread and message. No Drive row sets content_path, so the `<owner_email>/<path>` contract doesn't apply. The Google Doc has a docs_documents row with non-empty body_text (2,807 chars). The spreadsheet has sheets_spreadsheets plus two sheets_sheets rows, and the presentation has slides_presentations plus 3 pages and 3 text elements, so all are served through their services. The folder needs no content.

## 7. Check B: SQL structure and supported schema rules: PASS

- The whole file tokenizes with no unparsed statements. Column and value counts match on all 71 INSERT rows. Every UPDATE names its target by primary key and has no duplicate assignments.
- Generated columns: neither `slack_messages.text_fts` nor `gmail_messages.body_text_fts` is set.
- Linear text dates are all `YYYY-MM-DDTHH:MM:SSZ`, with no casts, offsets or `now()`. Linear INSERTs are comments only, and every NOT NULL column without a default is given (id, issue_id, author_id, body, is_edited, created_at, updated_at). No new issue is inserted, so `state_history_json` isn't needed.
- JSON columns: every `*_json` literal parses, with the snapshot shapes: Slack reactions/files/attachments are arrays and metadata is `'{}'`; gcal start/end are objects and attendees/rrule are arrays; Drive parents/shared/owners are arrays; style_runs_json is an array; trello data_json and the GitHub timeline data_json are objects; sheets grid_json is a 2-D array.
- Docs `style_runs_json` offsets match body_text exactly (TITLE 0–43 "ZM3D beta live-ops calendar - working rules"; the eight HEADING_2 runs cover "Span and time base" … "Config locks").
- Slack `4b7c4127…` attachments_json: the replacement equals the base attachment exactly except `fields[0].value`, where Reviewers adds `<@EMPLOYEE_0025_SLACK_ID>`. The HTML-escaped button value is preserved byte for byte.
- Provisional snapshot comparison (advisory A1, not a gate): these columns used in the SQL are NOT COVERED by the snapshot: gcal `extras_json`; drive `drive_id`; gslides `notes`, `table_json`, `ordinal`; github review_comments `pull_request_review_id`, `side`, `start_line`, `start_side`, `subject_type`, `seq` and reviews `seq`; linear_comments `sequence`. All other columns MATCH. The snapshot is unverified, so live acceptance of these columns is a disclosed compatibility limit, not a defect.

## 8. Check C: dates, relationships and consistency: PASS

**Clock.** The latest event timestamp is 2025-09-30T22:10:41Z (Robert's DM). The latest Linear event is 2025-09-30T21:07:26Z (ZOM-432 closed), and the latest Drive/Docs modification is 2025-09-30 06:38:27+00. All are before 2025-10-01T07:00Z. The only later values are plan fields (the GCal release on 2025-10-08 15:00–16:00Z) and future dates mentioned in text.

**Timestamps agree.** Every Slack `ts` equals its `created_at` to the microsecond. Gmail internal_date 1758532361000 / 1758872426000 equal the `date` values (09:12:41Z / 07:40:26Z), and the `+0300` Date headers (12:12:41 / 10:40:26) are the same instants. GCal "18:00-19:00 Istanbul time" = 15:00–16:00Z (UTC+3). Weekday names match the calendar: Mon Oct 6, Wed Oct 8, Mon Oct 13, Wed Oct 29, Fri Oct 31, Sat Nov 1, Sun Nov 2 (2025).

**Thread math.** For parent `9025d428`: 0 → 1 reply, latest = Robert's reply 1758213623.552919 (Sep 18, after the Sep 17 parent), thread_ts set to its own ts as on other base parents. For `c2b9c903`: 16 → 17, and the new mirror at 1759247468.897619 sits before the existing latest (…478.371389), so latest stays correct. The same holds for `61f686b8` (3 → 4; new 1759247580.84 < latest …586.96) and `4b7c4127` (41 → 42; new 1759160203.70 < latest 1759162433.38). Every reply in those threads is from the bot, so reply_users_count stays 1. The new DM thread has parent reply_count 1 and latest = the reply ts.

**GitHub ↔ Slack mirrors.** Each mirror lands 2 s after its comment (attachment ts 1759247466 / 1759247578 / 1759160201 = comment created_at). Each lands before the existing "Review approved" mirror (1759247469.35 / 1759247580.37), and every comment is before its PR's merge: #470 15:51:15Z, #472 15:53:04Z, #468 2025-09-29T16:13:50Z. Mirror text equals the GitHub body (with `&amp;` escaping). `#468#ev_6` follows the base "reviewed" pattern (actor '', created_at NULL, data commit_id), and its commit `648e2c7b…` is #468's head_sha. The paths used exist among each PR's base review-comment paths (CollectAndWinMainScreenController.cs on #470, GameLoader.cs on #468) or fit the PR scope (RewardVFXManager.cs on #472, a 3-file reward-VFX change).

**Linear history.** Every comment is after its issue's created_at. Every UPDATE moves updated_at forward from the base value (for example ZOM-78 2025-04-26 → 09-30, ZOM-432 07-23 → 09-30). ZOM-429 isn't updated because its base updated_at (09-22) is already after the new 09-16 comment. ZOM-432 (Todo → Done 09-30 21:07Z) and ZOM-344 (Todo → Done 09-16) carry completed_at equal to the closing comment. ZOM-566 started_at 17:20:13Z falls between its creation (16:26:02Z) and its first comment (19:40:47Z). Comments citing PRs come after those merges: #472 merged 15:53Z before ZOM-526 cmt 3 at 16:24Z; #475 merged 16:09Z before ZOM-521 cmt 2 at 16:27Z; #471 merged 15:52Z before ZOM-432 cmt 2 at 21:07Z. Marcus's ZOM-465 note that Collect & Win "came in after my note" fits #468 merging Sep 29, after his Sep 26 note.

**Facts checked against the base (no introduced contradiction).**
- Frederick's DM excludes four PNs Beta rows. Base gsheets spreadsheet `f_a325dd4af80afc5994d5dc` ("Push Notifications Zombie Match", shared with Julia and Frederick), tab "PNs Beta", has exactly those rows: Hourly Coins (row 2), Nathan's Treasure Hunt (8), Streak Fever (10) and Axe Arena (11). The brief's "Login Calendar row" is row 12. The brief's "translated tab is the old Domino set" matches tab "PN BETA Translated" (Domino Adventures, Tiledozer, River Rush copy).
- The brief's Collect & Win windows (Mon-Tue, Wed-Thu, Fri-Sun, shared) and "Season Pass seasons open on the 1st at 00:00 UTC" agree with Confluence "Live-Ops Event Calendar & Planning" and "ZM3D Season Pass — Spec". Arthur's "Collect & Win server windows still on DEV" agrees with the calendar page's "not yet live".
- The Halloween approval and withdrawal come from Robert. Confluence Season Pass spec: "Owner: Robert (Product)", so "Product … his later word" in the brief resolves to a real person.
- "Submission builds from today, iOS 50 and Android 135" (Sep 30) follows the base releases (Android 0.3.133 on Sep 28, iOS 0.3.49 released Sep 29). The UA deck's "stores approve the Sep 30 builds" and the "Unity retention campaigns are a separate budget" line match Frederick's base Slack ("We are only running the retention campaigns").
- The ZOM-521 checklist edit unticks "Tokens traveling to live-ops" and "Claimed Cards traveling to inventory". It now agrees with children ZOM-526/ZOM-528 (still In Progress), Brian's ZOM-526 comment ("Unticked this one on the master ticket") and Calvin's comments.
- Trello action data names the list "BETA: Sep 30". That matches the list's last rename action (2025-09-12) and every later base action (63 through 2025-09-30). Card badges match the base except comments 0 → 1, and dateLastActivity moves forward (09-12 → 09-29).
- Planned layered corrections, each a later dated record by the same owner or authority: Brian's Sep 26 mail replacing his Sep 22 date; Robert's Sep 30 withdrawal of his Sep 18 approval; Vincent's Sep 30 prod re-test against Douglas's Sep 16 ZOM-429 note; Samuel's Sep 30 closure of ZOM-432 after Calvin's Sep 24 note. These are supported stale-vs-newer readings, not contradictions.

**Grader-facing text (manual).** No text addresses a solver or grader or describes the test. Frederick's "Two things the brief does not spell out" is the requester clarifying his own brief to Julia in a DM, and Robert's "my later word on this one is the one that counts" is his own statement in a DM. Both are in-world. Decided: not grader-facing.

## 9. Base-data advisories for /prompt (not defects of this SQL)

- **SC-13 (Trello list name):** the base list is still named 'BETA: Oct 10'. The injected action uses 'BETA: Sep 30' like every base action and doesn't depend on the list name. Keep the beta date out of grading via the list name.
- **SC-15 (ZOM-521 checklist):** this SQL fixes the base mismatch in Linear (an injectable service). /prompt should still check that the task grades the child states rather than an old reading of the checklist.
- **SC-38 (Season Pass ship date and analytics, watch):** the injected ZOM-552 comment keeps analytics In Progress, consistent with the base. Keep the Season Pass ship date out of grading.
- **SC-22:** ZOM-344 and ZOM-432 become Done while `time_in_status_minutes` stays as in the base (NULL). Don't grade durations from that field.
- **Snowflake/Confluence:** the injected brief agrees with the two Confluence pages above. No listed Snowflake or Confluence conflict is built on.
- **ZOM-471 comment:** "In the thread this came from Leonard said we do not need it" refers to an unexported source thread. Nothing in the base contradicts it, and it can't be confirmed either. If an answer depends on it, /prompt should treat it as Samuel's word only.

## 10. Findings and fixes

No demonstrated defects. No repair needed.

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | Every actor, parent and target resolved; complete-scope collision checks found none; Gmail history_id contract met; every Drive file readable through its service (section 6) |
| B — SQL structure and supported schema rules | PASS | Counts, WHERE clauses, JSON shapes, Linear formats, NOT NULL columns and generated columns all clean. Snapshot NOT COVERED columns are advisory A1 (section 7) |
| C — Dates, relationships and consistency | PASS | All events before the clock; reply counts and latest_reply correct; mirrors and merges ordered; facts agree with base Sheets, Confluence, GitHub, Linear and Trello; no grader-facing text (section 8) |

## 11. Source and check dependencies (for reuse by /prompt)

- SQL SHA-256 `0e8c8ad8…f815`; manifest `da2f4cf0…a1a`; schema snapshot `31dcb2b4…151`; ID contracts `fc4711ef…682`; clock 2025-10-01T07:00:00Z.
- Base sources read: slack users.json and channels.json, plus messages for D05SD5QLG94, C08R8CHB0QL, D05GU6L0XFH, C0880U9751A and C093LEZGF6J (all months); gmail users.json, labels.json and threads/* (complete id scans); gcal, gdrive, gdocs, gslides and linear data.json; github data.json; trello data.json; gsheets data.json (id scan; spreadsheet index 220 tabs 1–2); confluence pages 20 and 27.
- Reused evidence: none.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt

Evidence limits: Static scope only. Live deploy compatibility is unverified (the bundled schema snapshot lacks several columns this SQL uses, advisory A1). Search ranking, Agent visibility and task difficulty are outside this review.
