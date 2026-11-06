# Structural map — live schema vs base exports

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Universe: `Universe_SynthCut` (from `hg.py universe`)
Columns: `Task_Authoring/references/universe_schema_live.json`. **No column in any table below is
NOT NULL — all 18 target tables are fully nullable (0 NOT NULL columns in the whole live schema).**
Counts read from base exports via `hgget.py` / `hg.py search get`.

## linear.linear_issues
- Columns (28, all NULL): id, uuid, project_id, team_id, parent_id, assignee_id, creator_id, state_id, cycle_id, identifier, number, title, description, priority, estimate, due_date, started_at, completed_at, canceled_at, archived_at, time_in_status_minutes, labels_json, links_json, relations_json, state_history_json, is_archived, created_at, updated_at
- Export: `linear data.json` → `/issues`; **3687 rows**; sample ids `ART-100`, `ART-101`, `ZOM-99`
- state_id values (workflow *names*, not ids): Done 3058, Canceled 372, Todo 113, Backlog 75, In Progress 21, Bugs 16, In Review 12, Duplicate 9, Team Epic 4, Regression 4, In Validation 3
- team_id: team_ENG 2270, team_ART 597, team_ZOM 553, team_DES 247, team_EPI 20 · priority 0–4 · is_archived true 977 / false 2710 · parent_id set on 1201 · labels non-empty 2964 · description NULL 1040
- Timestamp format (varchar, ISO): `2023-08-09T18:58:17Z` (created_at), `2023-12-04T17:40:48Z` (updated_at/completed_at)
- Mapping: `labels`→labels_json, `links`→links_json, `relations`→relations_json · **absent from export**: uuid, state_history_json (remain NULL) · `id` == `identifier` · quirk: `creator_id` sometimes a name, e.g. `usr_Victor Barnes`

## linear.linear_comments
- Columns (9, all NULL): id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence
- Export: `linear data.json` → `/comments`; **0 rows** (empty list; `comments` key exists). No enums/timestamps observable.
- Mapping: not observable — no rows. Comments are not a usable surface; use descriptions/attachments instead.

## linear.linear_users
- Columns (10, all NULL): id, email, name, display_name, avatar_url, is_active, is_admin, is_guest, created_at, updated_at
- Export: `linear data.json` → `/users`; **41 rows**; sample ids `usr_05f0a0d12f2ad71f`, `usr_175c0d7bc72ed244`, `usr_1e2a0240767eb09b`
- All is_active true (0 inactive). name/display_name are usually the email address itself.
- Timestamp format: `2023-03-22T19:11:39Z`
- Mapping: direct 1:1 · absent from export: is_admin, is_guest. Sibling `linear_teams` (`/teams`, 5: team_ART/DES/ENG/EPI/ZOM) resolves `team_id`.

## slack.slack_messages
- Columns (24, all NULL): id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, reply_count, reply_users_count, latest_reply, is_activity_message, subtype, reactions_json, files_json, attachments_json, created_at, edited_ts, edited_user, bot_id, client_msg_id, permalink, metadata_json, text_fts
- Export: `slack messages/<CHANNEL>/<YYYY-MM>.json`, one array per shard. `hg.py search files slack messages/` → **total_matching_paths 4840** shards (20 shown, truncated), 9+ channel dirs. Sample shard `messages/C08R27X0EAH/2025-09.json` = **1097 rows**; sample ids `5dce1db5a252dc8c64ebc8ef7a641456`
- Shard row keys: id, ts, type, user, text, channel, thread_ts, reply_count, reply_users_count, latest_reply, is_activity_message, subtype, reactions, files, attachments
- type: `message` 1097/1097 · subtype: null 1074, `tabbed_canvas_updated` 11, `bot_message` 7, `thread_broadcast` 5 · 805 rows carry thread data (thread_ts/reply_count)
- ts format (varchar, epoch string): `1756749452.263229`; latest_reply same shape `1756770610.901469`
- Mapping: `user`→user_id, `channel`→channel_id, `thread_ts`→thread_parent_id, `reactions`→reactions_json, `files`→files_json, `attachments`→attachments_json · absent in sample: created_at (derived from ts), edited_ts/edited_user, bot_id, client_msg_id, permalink, metadata_json

## slack.slack_channels
- Columns (14, all NULL): id, name, is_channel, is_private, is_im, is_mpim, is_archived, is_general, num_members, topic, purpose, created_ts, creator_id, members_json
- Export: `slack channels.json` (top-level **list**); **948 rows**; decode `mpdm-calvin.price--robert--arthur.blake--leonard.hayes-1`
- Flags: is_channel 157/791, is_private 307/641, is_im 574/374, is_mpim 217/731, is_archived 90/858, is_general 1/947 · num_members 1–38
- Timestamp format: `created` is the literal string `"0.000000"` on the sampled rows (no real creation time)
- Mapping: `created`→created_ts (double precision), `creator`→creator_id (NULL on 820/948), `members`→members_json (employee tokens like `EMPLOYEE_0016_SLACK_ID`)

## gmail.gmail_threads
- Columns (4, all NULL): id, user_email, snippet, history_id
- Export: `gmail threads/<user>_<threaddigits>.json`, one object per file. `hg.py search files gmail threads/` → **total_matching_paths 81404** (20 shown, truncated)
- Sample file `threads/vincent@harmonygames.co_1843647875236076464.json` → `{id, messages:[1], user_email}`; id **`vincent.parker@harmonygames.co/1843647875236076464`**
- Mapping: file object keys `id`→id, `user_email`→user_email · snippet and history_id are not in the export (NULL) · quirk: the filename truncates the mailbox at `@` (`vincent@…` vs id `vincent.parker@…`)
- Timestamps: none at thread level.

## gmail.gmail_messages
- Columns (27, all NULL): id, thread_id, user_email, label_ids_json, trash_removed_labels_json, snippet, history_id, internal_date, date, size_estimate, subject, from_email, from_name, to_json, cc_json, bcc_json, reply_to_json, body_text, body_html, headers_json, payload_json, in_reply_to, references, mbox_from, date_parsed_source, attachments_meta_json, body_text_fts
- Export: nested at `/messages` inside each thread file (no standalone file). **Not globally enumerable cheaply** (81404 thread shards, ≥1 message each); sample thread carries 1 message.
- Sample message id: `vincent.parker@harmonygames.co/<dgTv2AULAN2Ou0_cjrtPAZlfP5MG4PxZbHbQ4n9ZCQ.1758239626@mail.notion.so>`, subject `Notion 3.0: Agents`, labelIds `["INBOX","Label_b19fb8d1b3","CATEGORY_PROMOTIONS"]`
- Date format (RFC 2822 string): `Thu, 18 Sep 2025 23:53:46 +0000`
- Mapping: `body`→body_text, `labelIds`→label_ids_json, `from`→from_email + from_name, `to`→to_json, `cc`→cc_json, `bcc`→bcc_json, `reply_to`→reply_to_json, `headers`→headers_json, `attachments`→attachments_meta_json, `internal_date_ms`→internal_date (bigint), `date_parsed`→date, `date`→date_parsed_source · absent: snippet, history_id, body_html, payload_json, size_estimate, trash_removed_labels_json · recipients normalized to placeholders (`PERSON_2859_EMAIL`)

## gcal.gcal_events
- Columns (24, all NULL): event_id, calendar_id, summary, description, location, start_ts, end_ts, start_json, end_json, organizer_email, creator_email, attendees_json, status, visibility, transparency, rrule_json, recurring_event_id, original_start_json, sequence, created, updated, hangout_link, ical_uid, extras_json
- Export: `gcal data.json` → `/events`; **10395 rows** (also `/calendars` 38); sample ids `evt_00009bfb80dabb15aa5bb5`, `evt_0009cee7e23fd431e0b4a9`, `evt_00112478dd1b12806338c6`
- status: confirmed 9362, cancelled 1033 · transparency: opaque 10395 · visibility: absent from export (all NULL) · recurringEventId: 0 (rrule always `[]`)
- Timestamp format: `2024-11-18T17:29:37Z` (created/updated); start/end are objects `{"dateTime":"2024-11-18T17:30:00Z"}` (only shape seen: `dateTime`, 10395/10395)
- Mapping: `start`→start_ts + start_json, `end`→end_ts + end_json, `rrule`→rrule_json, `attendees`→attendees_json · absent: description, location, visibility, recurring_event_id, original_start_json, extras_json · calendar_id is an owner mailbox (leonard.hayes@ 1382, robert@ 1133…)

## gdrive.drive_files
- Columns (22, all NULL): id, name, mime_type, parents_json, owner_email, shared_with_emails_json, shared_roles_json, visibility_role, shared_groups_json, visibility, owners_json, modified_time, created_time, size, trashed, starred, content_path, web_view_link, icon_link, description, drive_id, content_text
- Export: `gdrive data.json` → `/drive_files`; **53631 rows**; sample ids `d_00003b5dc5d1e91bd4bd6f`, `d_0008c1666ca74384986ee6`, `d_0009d0527fc79b7b0c0516`
- mime_type: application/json 27029, folder 23257, text/markdown 1074, text/plain 599, google-apps.document 595, pdf 409, google-apps.spreadsheet 356, text/csv 172
- visibility: private 53497, domain 92, anyone 42 · trashed 0/53631 · size NULL on folders
- Timestamp format: `2025-09-11T15:16:33Z`
- Mapping: `parents`→parents_json, `shared_with_emails`→shared_with_emails_json, `owners`→owners_json · absent: shared_roles_json, shared_groups_json, visibility_role, drive_id, content_text

## gsheets.sheets_spreadsheets
- Columns (8, all NULL): spreadsheet_id, title, owner_email, shared_with_emails_json, visibility, drive_file_id, created_time, modified_time
- Export: `gsheets data.json` → `/sheets_spreadsheets` (single 327 MB file); **356 rows** (verified by bounded index probing; `/sheets` and `/sheets_sheets` top-level keys do not exist)
- Sample: `f_00c30de5acd0cf7656c140` — `[PERSON_NAME_0067]_s Offer Parameters`; also `/2` = `DDA Simulator`, `/30` = Zombie funnel sheet. spreadsheet_id == drive_file_id; matches 356 `google-apps.spreadsheet` rows in gdrive
- visibility: private/domain/anyone mix (sampled); timestamp format `2023-11-30T00:27:36Z`
- Mapping: `shared_with_emails`→shared_with_emails_json · quirk: `owner_email` is often a placeholder `Resource: 7240535625619857401` (not an address), so join to gdrive owner_email is unreliable

## gsheets.sheets_sheets
- Columns (7, all NULL): spreadsheet_id, sheet_id, title, index, row_count, column_count, grid_json
- Export: **nested** `/sheets_spreadsheets/<i>/sheets/<j>` (no separate top-level array). Global tab count not enumerable cheaply; sampled parents hold 1–6+ tabs. **This is a derived table** — rows are exploded from each parent's `sheets` array.
- Sample: spreadsheet 0 → sheet 0 `Sheet1`, sheet_id 0, index 0, row_count 1004, column_count 27, grid = array of row arrays (`grid[0]` = 27 empty strings) → grid_json
- Enums: none. `index` is 0-based position; `sheet_id` is a per-spreadsheet integer.
- Mapping: parent `spreadsheet_id`→spreadsheet_id, `sheet_id`→sheet_id, `title`→title, `index`→index, `row_count`→row_count, `column_count`→column_count, `grid`→grid_json · note row_count is the declared grid size and exceeds populated rows (many blank rows)

## gdocs.docs_documents
- Columns (12, all NULL): document_id, title, owner_email, shared_with_emails_json, visibility, body_text, style_runs_json, revision_id, drive_file_id, created_time, modified_time, text_style_runs_json
- Export: `gdocs data.json` → `/docs_documents` (**only top-level key**); **595 rows**; sample id `f_00117462881159eceee63e` (`Shortcut`, a 1-line stand-up stub)
- visibility: private 540, domain 35, anyone 20 · document_id == drive_file_id · matches 595 `google-apps.document` rows in gdrive
- Timestamp format: `2023-08-25T18:22:55Z`
- Mapping: `shared_with_emails`→shared_with_emails_json, `style_runs`→style_runs_json · absent: text_style_runs_json · quirk: `owner_email` often the placeholder `Resource: -6481757892984311338`

## trello.trello_actions
- Columns (7, all NULL): id, type, date, idMemberCreator, idBoard, idCard, data_json
- Export: `trello data.json` → `/actions`; **5252 rows**; sample ids `535af5816ca07f261e8cd441`
- type counts: updateCard 3989, createCard 751, addMemberToCard 92, updateList 86, commentCard 56, updateCheckItemStateOnCard 53, addAttachmentToCard 48, createList 34, copyCard 34, addChecklistToCard 26, deleteCard 15, updateBoard 14, addMemberToBoard 11, removeMemberFromCard 10, removeChecklistFromCard 6 (+ tail)
- Timestamp format: `2014-01-13T15:43:45Z` on the first row — action dates span the legacy 2014 board through 2025 (cards' `dateLastActivity` is mostly 2024–25), so any "current" reasoning must use the action mix, not a single year
- Mapping: `data`→data_json (holds listBefore/listAfter, card name, text) · idMemberCreator/idBoard/idCard 1:1

## trello.trello_cards
- Columns (20, all NULL): id, name, idBoard, idList, desc, pos, closed, due, dueComplete, idMembers_json, idLabels_json, idShort, shortLink, shortUrl, url, dateLastActivity, cover_json, badges_json, start, idAttachmentCover
- Export: `trello data.json` → `/cards`; **803 rows**; sample ids `535af5816ca07f261e8cd426`, `...8cd428`, `...8cd429`
- closed: true 324 / false 479 · idShort max 455 · boards: 640643a3fd8f3ca308d9318e 449, 65eb4ec525346c8070ca638f 216, 6851a6569f3bf818760632ab 79, 66da196af476ab78deaa0cef 40, 535af5816ca07f261e8cd420 19
- Timestamp format: `dateLastActivity` ISO `2014-04-25T23:53:37Z`; year mix 2024 433, 2025 331, 2023 20, 2014 19 · `due` ISO or null
- Mapping: `idMembers`→idMembers_json, `idLabels`→idLabels_json, `cover`→cover_json, `badges`→badges_json · **`start` and `idAttachmentCover` are absent from the export** (all 803 cards) · sibling `/lists` (47), `/boards` (5), `/members` (42), `/labels` (31), `/checklists` (54), `/check_items` (161), `/attachments` (76)

## contacts.contacts
- Columns (18, all NULL): contact_id, first_name, last_name, is_user, gender, age, nationality, city_living, country, status, job, description, phone, email, address, created_at, updated_at, source
- Export: `contacts contacts.json` → top-level **object** `{contacts:[…], current_user_id:"5f647df33ba6e92fbd56b05b"}`; pointer `/contacts`; **170 rows**; sample ids `d4a339f7f6aafffdc2dabb9a`, `655f2fd84c2100fcc45498a1`, `cnt_1f37af74b039`
- status: `Unknown` 170/170 · gender: `Unknown` 170/170 · is_user true 1 / false 169 · source absent (NULL 170)
- Timestamps: `created_at` / `updated_at` are **absent from the export** → both NULL for all 170
- Mapping: direct 1:1 for the 15 fields present · id shapes mix 24-hex Mongo ids and `cnt_<12 hex>`; the `cnt_` suffix is the first 12 hex chars of the matching linear user id (`usr_05f0a0d12f2ad71f` ↔ `cnt_05f0a0d12f2a`) · names/emails are placeholders (`EMPLOYEE_0032`, `EMPLOYEE_0032_EMAIL`), so contacts cannot be joined to slack/linear by name — only `is_user` + `cnt_` id

## github.github_pull_requests
- Columns (29, all NULL): id, repo_id, number, title, state, merged, draft, locked, maintainer_can_modify, author_login, merged_by_login, body, base_ref, head_ref, base_sha, head_sha, merge_commit_sha, additions, deletions, changed_files, labels_json, assignee_logins_json, requested_reviewer_logins_json, created_at, updated_at, merged_at, closed_at, html_url, requested_team_slugs_json
- Export: `github data.json` → `/pull_requests`; **2475 rows**; sample ids `harmonygames-Games/GameOfDominoes#1`, `#10`, `#100` (`<repo full name>#<number>`)
- state: closed 2468, open 7 · merged true 2353 / false 122 · 15 repositories in `/repositories`
- **max PR number per repo: `harmonygames-Games/match3d` → 477 (477 PRs, dense 1..477); `harmonygames-Games/match3d-backend` → 35 (35 PRs)**
- Timestamp format: `2023-04-12T15:30:19Z`
- Mapping: `labels`→labels_json, `assignee_logins`→assignee_logins_json, `requested_reviewer_logins`→requested_reviewer_logins_json · absent: maintainer_can_modify, merge_commit_sha, requested_team_slugs_json · `repo_id` is the repo **full name** (`harmonygames-Games/match3d`), not a synthetic id

## github.github_reviews
- Columns (8, all NULL): id, pr_id, author_login, state, body, submitted_at, commit_id, seq
- Export: `github data.json` → `/reviews`; **2230 rows**; sample ids `harmonygames-Games/GameOfDominoes#1#rev_1`, `…#rev_2`
- state enum counts: APPROVED 1742, COMMENTED 412, CHANGES_REQUESTED 74, DISMISSED 2
- Timestamp format: `2023-04-12T15:59:38Z`
- Mapping: 1:1 for id, pr_id, author_login, state, body, submitted_at, commit_id · `seq` is not exported (derived from `#rev_N` suffix in id) · `pr_id` is the PR composite id, so reviews join to PRs on `pr_id == pull_requests.id`

## github.github_timeline_events
- Columns (6, all NULL): id, pr_id, event, actor_login, created_at, data_json
- Export: `github data.json` → `/timeline_events`; **11406 rows**; sample ids `harmonygames-Games/GameOfDominoes#1#ev_1`, `…#ev_2`
- event enum counts: review_requested 2590, closed 2485, merged 2353, reviewed 2116, commented 687, head_ref_deleted 483, assigned 194, head_ref_force_pushed 124, labeled 101, cross-referenced 59, mentioned 50, ready_for_review 48, renamed 38, subscribed 18, reopened 17, review_request_removed 13, convert_to_draft 8, unlabeled 6, referenced 4, head_ref_restored 4, base_ref_changed 4, review_dismissed 2, unsubscribed 2
- Timestamp format: `2023-04-12T15:33:29Z`
- Mapping: `data`→data_json (holds reviewer/assignee/label payloads) · id shape `…#ev_N`; `seq` has no column here (only reviews carry one)
