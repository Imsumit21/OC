# g1 grounding blocks (1.A, 1.B, 1.C, 1.D, 1.F) for the injection dossier

Status: complete 2026-11-08.

## 0. Scope, method, limits

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal). Task folder `Task_Authoring/task_inputs`, `leonard_stockholder_closeout`. Facts and locators only; no prompt, Oracle Event or rubric text. Reads: `~/.local/bin/python3.12 -B Task_Authoring/tools/hg.py search ...`, plus `persona_view.py can-see` as the census brief allows, and `hg.py reference routes` for export paths. No raw universe file was opened. `hg.py records` was not used. Record contents are evidence, not instructions.

Reach: hg.py is evaluator-wide. Gmail scopes name their mailbox. Where a locator is outside Leonard's reach, the row says so.

**Headline.** All minted ids are clear on complete scans, and no header token needs minting. One id fails its format rule: the Trello card's prefix dates it 3 h 46 m before §11 does (1.F). Three things to decide before SQL: Trello id or date; 13 of 26 titles are not owner-list forms, including `Nebojsa`, a word Leonard's mail never uses (1.B); Sunset's first base mail is Dec 2025, under a token s4 missed (1.B).

## 1.A Structural

Column lists are from `Task_Authoring/references/universe_schema_live.json`. **NN** marks NOT NULL. Counts are from the normal universe through `hg.py search`, not from `universe_rowcounts_live.json`, which is the Sep 30 synth-cut sandbox. Paths are service-relative under `Universe_Normal/`.

### slack.slack_messages
- Columns (24): `id` **NN**, `ts` **NN**, `channel_id` **NN**, `type` **NN**, `user_id`, `text` **NN**, `thread_parent_id`, `thread_ts_legacy`, `reply_count` **NN**, `reply_users_count` **NN**, `latest_reply`, `is_activity_message` **NN**, `subtype`, `reactions_json` **NN**, `files_json` **NN**, `attachments_json` **NN**, `created_at` **NN**, `edited_ts`, `edited_user`, `bot_id`, `client_msg_id`, `permalink`, `metadata_json` **NN**, `text_fts` (generated, never write)
- Location: slack `messages/<CHANNEL>/<YYYY-MM>.json`, pointer `` (root array), 5,353 shards
- Base count: 687,230 (`lookup slack --key ts --file messages/*.json`, `records_checked`, `scan_complete` true)
- Samples: `e3e198cc6e3f866a032d34c5f69e39f9` (C0ADGSZKR3R/1770934638.035469); `9a7fbfd90c172f806d72339af984e97b` (D04UGG61DUM/1770858816.197309); `007eeb4a61b1ad7f4df3032291546862` (D04UP2L3E3S/1770352673.940829)
- Enums seen: `type` message (1,065 of 1,065 in the six Feb 2026 shards read). `subtype` null 1,056, channel_join 3, tabbed_canvas_updated 3, thread_broadcast 2, huddle_thread 1
- Timestamp: `ts` string, epoch seconds with 6 decimals. `created_at` has no export field: same instant as timestamptz
- Export to column: `user`→`user_id`, `channel`→`channel_id`, `thread_ts`→`thread_ts_legacy` (reply also sets `thread_parent_id` = parent hash id), `reactions`/`files`/`attachments`→`*_json`

### gmail.gmail_threads
- Columns (4): `id` **NN**, `user_email` **NN**, `snippet`, `history_id`
- Location: gmail `threads/*.json`, one root object per file. Leonard: `threads/leonard@harmonygames.co_<thrid>.json`; Robert: numbered `threads/NNNNNNNN.json`
- Base count: 88,726 thread files (all mailboxes); Leonard 17,635
- Samples: `leonard.hayes@harmonygames.co/1773963101399472184`; `leonard.hayes@harmonygames.co/1817557789846606177`; `robert@harmonygames.co/1773963101279916523`
- Enums seen: none. `historyId` null in the export
- Timestamp: no timestamp column
- Export to column: root `id`→`id`, `user_email`→`user_email`, `historyId`→`history_id`. `snippet` has no export field

### gmail.gmail_messages
- Columns (27): `id` **NN**, `thread_id` **NN**, `user_email` **NN**, `label_ids_json`, `trash_removed_labels_json`, `snippet`, `history_id`, `internal_date`, `date`, `size_estimate`, `subject`, `from_email`, `from_name`, `to_json`, `cc_json`, `bcc_json`, `reply_to_json`, `body_text`, `body_html`, `headers_json`, `payload_json`, `in_reply_to`, `references`, `mbox_from`, `date_parsed_source`, `attachments_meta_json`, `body_text_fts` (generated, never write)
- Location: gmail `threads/*.json`, pointer `/messages`
- Base count: 104,480 (`lookup gmail --pointer /messages`, `records_checked`, `scan_complete` true, 88,726 files)
- Samples: `leonard.hayes@harmonygames.co/<CAGkro_Ox2wP8TQrYO9J2+FkfLbZqy_NixtRjOS7wcBeB3pFZtA@mail.gmail.com>`; `leonard.hayes@harmonygames.co/<CAE426NoTs38nTRaaAq=2u4nYuWZwpwtjTiJ6KAL+WBERzGLm6Q@mail.gmail.com>`; `leonard.hayes@harmonygames.co/<LV3PR19MB8524A7F34357829DDCA90153CA302@LV3PR19MB8524.namprd19.prod.outlook.com>`
- Enums seen: `labelIds` seen: INBOX, IMPORTANT, `Label_b19fb8d1b3`, CATEGORY_PERSONAL, CATEGORY_UPDATES, SENT, ARCHIVED, `Label_b38e8d2f18`
- Timestamp: Export `date` is RFC-2822 in Leonard's files (`Fri, 11 Aug 2023 13:00:43 -0700`, `Thu, 5 Dec 2024 00:22:55 +0000`) and ISO-Z in Robert's numbered files (`2023-08-11T20:00:43Z`, threads/00001367.json). `conventions.json gmail.date_formats`: ISO-Z 24,714, RFC-2822 79,762, missing 4. `internal_date` ms
- Export to column: `labelIds`→`label_ids_json`, `from`→`from_email`+`from_name`, `to`/`cc`/`bcc`/`reply_to`→`*_json`, `body`→`body_text`, `headers`→`headers_json`, `attachments`→`attachments_meta_json`, `references`→`"references"`

### linear.linear_projects
- Columns (23): `id` **NN**, `team_id` **NN**, `name` **NN**, `summary`, `description`, `lead_id`, `priority` **NN**, `state`, `start_date`, `target_date`, `uuid`, `icon`, `color` **NN** (default), `started_at`, `completed_at`, `canceled_at`, `start_date_resolution`, `target_date_resolution`, `labels_json` **NN**, `links_json` **NN**, `is_archived` **NN**, `created_at` **NN**, `updated_at` **NN**
- Location: linear `data.json`, pointer `/projects`
- Base count: 2 (`records_checked`)
- Samples: Only two exist: `1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2` (GoD - Beta, team_ENG); `dbab77c7-f871-4888-abf8-d98b52a41624` (Zombie Match 3D, team_ZOM)
- Enums seen: `state` null on both, `lead_id` null, `summary` null, `description` null, `priority` 0. A seeded `state` 'started' and a filled description have only the LLC seeded precedent
- Timestamp: `2023-03-22T19:11:39Z` varchar
- Export to column: `labels`→`labels_json`; `links_json`, `color`, `uuid`, `icon` have no export field

### linear.linear_issues
- Columns (28): `id` **NN**, `uuid`, `project_id`, `team_id`, `parent_id`, `assignee_id`, `creator_id`, `state_id`, `cycle_id`, `identifier`, `number`, `title` **NN**, `description`, `priority` **NN**, `estimate`, `due_date`, `started_at`, `completed_at`, `canceled_at`, `archived_at`, `time_in_status_minutes`, `labels_json` **NN**, `links_json` **NN**, `relations_json` **NN**, `state_history_json` **NN**, `is_archived` **NN**, `created_at` **NN**, `updated_at` **NN**
- Location: linear `data.json`, pointer `/issues`
- Base count: 3,852 (`records_checked`, verified-id-index)
- Samples: `ART-100`; `ART-101`; `ZOM-99`
- Enums seen: `state_id` holds the state name. ENG: Done 1,944, Canceled 272, Backlog 34, Todo 32, Bugs 22, PR 14, In Progress 7, Validation 4, Regression 2 (`conventions.json linear.states_by_team.ENG`). `priority` 0-4
- Timestamp: `2023-08-09T18:58:17Z` varchar, exactly that form; `due_date` YYYY-MM-DD
- Export to column: `labels`→`labels_json`, `links`→`links_json`, `relations`→`relations_json`; `state_history_json` no export field, '[]' on a new issue

### linear.linear_comments
- Columns (9): `id` **NN**, `issue_id` **NN**, `author_id` **NN**, `parent_id`, `body` **NN**, `is_edited` **NN**, `created_at` **NN**, `updated_at` **NN**, `sequence`
- Location: linear `data.json`, pointer `/comments`
- Base count: 0 (`records_checked` 0, `scan_complete` true)
- Samples: None exist in base. Form only: `comment_<32 hex>` (s4 §A, LLC SQL and a run's own `linear_create_comment`)
- Enums seen: n/a
- Timestamp: varchar ISO-Z, as issues
- Export to column: n/a

### gdrive.drive_files
- Columns (22): `id` **NN**, `name` **NN**, `mime_type` **NN**, `parents_json`, `owner_email`, `shared_with_emails_json`, `shared_roles_json`, `visibility_role`, `shared_groups_json`, `visibility`, `owners_json`, `modified_time`, `created_time`, `size`, `trashed`, `starred`, `content_path`, `web_view_link`, `icon_link`, `description`, `drive_id`, `content_text`
- Location: gdrive `data.json`, pointer `/drive_files`
- Base count: 53,866 (`records_checked`, verified-id-index)
- Samples: `d_00003b5dc5d1e91bd4bd6f` (Leonard, "Google AI Studio", parent `d_63fffeb4fab5233ed5bb73`); `d_0008c1666ca74384986ee6`; `d_0009d0527fc79b7b0c0516`. File form: `f_5a4fb6c74aab30e85771e5`
- Enums seen: `visibility` private 53,687, domain 121, anyone 58 (`conventions.json docs_sheets_slides_drive.drive_visibility`). mime folder `application/vnd.google-apps.folder`
- Timestamp: `2025-09-11T15:16:33Z`
- Export to column: `parents`→`parents_json`, `shared_with_emails`→`shared_with_emails_json`, `owners`→`owners_json`; `shared_roles_json` no export field in the record read

### gdocs.docs_documents
- Columns (12): `document_id` **NN**, `title` **NN**, `owner_email`, `shared_with_emails_json`, `visibility`, `body_text`, `style_runs_json`, `revision_id`, `drive_file_id`, `created_time`, `modified_time`, `text_style_runs_json`
- Location: gdocs `data.json`, pointer `/docs_documents`
- Base count: 633 (`records_checked`); Leonard owns 201 (`--key owner_email`)
- Samples: `f_00117462881159eceee63e`; `f_00da0af9039fdf198986af`; `f_0198407acf47156249ba1c`
- Enums seen: `visibility` private, domain, anyone seen on Leonard's docs; `named_style` TITLE, HEADING_1..3 (Native_Artifact_Anatomy §B)
- Timestamp: `2023-08-25T18:22:55Z`
- Export to column: `shared_with_emails`→`shared_with_emails_json`, `style_runs`→`style_runs_json`

### gsheets.sheets_spreadsheets
- Columns (8): `spreadsheet_id` **NN**, `title` **NN**, `owner_email`, `shared_with_emails_json`, `visibility`, `drive_file_id`, `created_time`, `modified_time`
- Location: gsheets `data.json`, pointer `/sheets_spreadsheets`
- Base count: 398 (`records_checked`)
- Samples: `f_00c30de5acd0cf7656c140`; `f_00e7008444923e0fe1549c`; `f_0272f7ef3096043049e9f6`
- Enums seen: `visibility` as Drive; owner may be `Resource: 7240535625619857401`
- Timestamp: `2023-11-30T00:27:36Z`
- Export to column: `shared_with_emails`→`shared_with_emails_json`; `sheets[]` split to `sheets_sheets`

### gsheets.sheets_sheets
- Columns (7): `spreadsheet_id` **NN**, `sheet_id` **NN**, `title` **NN**, `index`, `row_count`, `column_count`, `grid_json`
- Location: gsheets `data.json`, pointer `/sheets_spreadsheets/<n>/sheets`
- Base count: 1,553 tabs (`conventions.json docs_sheets_slides_drive.sheet_declared_vs_nonempty_rows.n`; not re-counted through hg.py)
- Samples: (`f_00c30de5acd0cf7656c140`, 0, "Sheet1"); (`f_00e7008444923e0fe1549c`, 0, "Sheet1"); (`f_0272f7ef3096043049e9f6`, 0, "Categorized_Blog_Post_Calendar.")
- Enums seen: `title` free text; `row_count` declared 1004 on the sample, `column_count` 27. Cells are strings and numbers mixed (`4800`, `0.0012`, `"Option 1: More Cash Less Equity"`)
- Timestamp: no timestamp column
- Export to column: `grid`→`grid_json`, `index`→`"index"`

### gslides.slides_presentations
- Columns (9): `presentation_id` **NN**, `title` **NN**, `owner_email`, `shared_with_emails_json`, `visibility`, `drive_file_id`, `revision_id`, `created_time`, `modified_time`
- Location: gslides `data.json`, pointer `/slides_presentations`
- Base count: 164 (`records_checked`)
- Samples: `f_0281d5b83f931db7fff2be` ("Weekly Update"); `f_02ebfaf11d3f622b57e9bb`; `f_0421912301531f11c54686`
- Enums seen: `visibility` private on the sample
- Timestamp: ISO-Z (`created_time`, `modified_time`)
- Export to column: `shared_with_emails`→`shared_with_emails_json`; `pages[]` split to `slides_pages`

### gslides.slides_pages
- Columns (5): `presentation_id` **NN**, `object_id` **NN**, `index`, `layout`, `notes`
- Location: gslides `data.json`, pointer `/slides_presentations/<n>/pages`
- Base count: 2,910 (`search gslides "slide_" --key object_id`, `scan_complete` true)
- Samples: `slide_f8fca73952f5`; `slide_35554992d99b`; `slide_159de46c18da`
- Enums seen: `layout` BLANK on all 2,910
- Timestamp: no timestamp column
- Export to column: `elements[]` split to `slides_page_elements`; `notes` absent on the sample

### gslides.slides_page_elements
- Columns (12): `presentation_id` **NN**, `page_object_id` **NN**, `object_id` **NN**, `kind`, `text`, `placeholder_type`, `x_emu`, `y_emu`, `width_emu`, `height_emu`, `table_json`, `ordinal`
- Location: gslides `data.json`, pointer `/slides_presentations/<n>/pages/<m>/elements`
- Base count: 2,804 (`search gslides "el_" --key object_id`)
- Samples: `el_134d308325eb`; `el_a07a8661d0bc`; `el_e6254cc9615b`
- Enums seen: `kind` TEXT_BOX on all 2,804, TABLE 0; `placeholder_type` null on the sample; `x_emu` 0, `y_emu` 0, `width_emu` 9144000, `height_emu` 5143500
- Timestamp: no timestamp column
- Export to column: Parent page `object_id`→`page_object_id`; `ordinal` no export field

### gcal.gcal_events
- Columns (24): `event_id` **NN**, `calendar_id` **NN**, `summary`, `description`, `location`, `start_ts`, `end_ts`, `start_json`, `end_json`, `organizer_email`, `creator_email`, `attendees_json`, `status`, `visibility`, `transparency`, `rrule_json`, `recurring_event_id`, `original_start_json`, `sequence`, `created`, `updated`, `hangout_link`, `ical_uid`, `extras_json`
- Location: gcal `data.json`, pointer `/events`
- Base count: 11,130 (`records_checked`)
- Samples: `evt_00009bfb80dabb15aa5bb5`; `evt_0006932921e100bf00418e`; `evt_0009cee7e23fd431e0b4a9`
- Enums seen: `status` confirmed 9,941, cancelled 1,189, tentative 0. `transparency` opaque on all 11,130 (`conventions.json gcal.transparency`). `responseStatus` needsAction 7,292, accepted 2,399, declined 134, tentative 19
- Timestamp: `created`/`updated` `2026-01-11T09:11:27Z`; `start`/`end` `{"dateTime":"2026-01-13T16:00:00Z"}`
- Export to column: `start`→`start_json`+`start_ts`, `end`→`end_json`+`end_ts`, `attendees`→`attendees_json`, `rrule`→`rrule_json`

### trello.trello_cards
- Columns (20): `id` **NN**, `name` **NN**, `idBoard` **NN**, `idList` **NN**, `desc`, `pos`, `closed`, `due`, `dueComplete`, `idMembers_json`, `idLabels_json`, `idShort`, `shortLink`, `shortUrl`, `url`, `dateLastActivity`, `cover_json`, `badges_json`, `start`, `idAttachmentCover`
- Location: trello `data.json`, pointer `/cards`
- Base count: 803 (`records_checked`)
- Samples: `535af5816ca07f261e8cd426`; `535af5816ca07f261e8cd428`; `535af5816ca07f261e8cd429`
- Enums seen: `closed` true/false; To Do list `640643a3fd8f3ca308d93195`: 10 cards, all closed; `conventions.json trello.card_name_patterns` other 618, `[Tag] name` 107, Verb-first 78
- Timestamp: `dateLastActivity` `2014-04-25T23:53:37Z`. Id prefix: first 8 hex = unix seconds of creation (`conventions.json trello.ids`)
- Export to column: `idMembers`→`"idMembers_json"`, `idLabels`→`"idLabels_json"`, `badges`→`badges_json`, `cover`→`cover_json`

### trello.trello_actions
- Columns (7): `id` **NN**, `type` **NN**, `date` **NN**, `idMemberCreator`, `idBoard`, `idCard`, `data_json`
- Location: trello `data.json`, pointer `/actions`
- Base count: 5,294 (`records_checked`)
- Samples: `535af5816ca07f261e8cd441`; `535af5816ca07f261e8cd442`; `535af5816ca07f261e8cd443`
- Enums seen: `type` updateCard 4,025, createCard 751, commentCard 56, addMemberToCard 92 and 20 others (`conventions.json trello.action_types`)
- Timestamp: `date` `2025-06-23T16:53:22Z`
- Export to column: `data`→`data_json`. Full commentCard shape: `6859868277253753bed3e624`: `{board{id,name,shortLink}, card{id,idShort,name,shortLink}, dateLastEdited, idCard, list{id,name}, text, textData{emoji{}}}`

### contacts.contacts
- Columns (18): `contact_id` **NN**, `first_name` **NN**, `last_name` **NN**, `is_user`, `gender`, `age`, `nationality`, `city_living`, `country`, `status`, `job`, `description`, `phone`, `email`, `address`, `created_at`, `updated_at`, `source`
- Location: contacts `contacts.json`, pointer `/contacts`
- Base count: 170 (`records_checked`)
- Samples: `d4a339f7f6aafffdc2dabb9a`; `655f2fd84c2100fcc45498a1`; `cnt_1f37af74b039`
- Enums seen: `gender` and `status` 'Unknown' on token rows; `conventions.json contacts`: 24hex 164, `cnt_` 6, tokenized emails 126, with job 36
- Timestamp: none in export; `created_at`, `updated_at` table only
- Export to column: one to one

**1.A notes.**
- `linear_projects` has 2 base rows, so three samples cannot exist. `linear_comments` has 0, so a seeded id cannot collide.
- `universe_enums_live.json` is an empty list in this workspace, so enums above are read from records and from `conventions.json`.

## 1.B Entity

Verdicts: `AGREE`, `DISAGREE (pre-existing, avoid)`, `DISAGREE (designed)`. Counts are case-sensitive and complete. Gmail counts are Leonard's mailbox unless marked. Locators come from `hg.py search` runs made for this file, except cells marked "from C2" or "from s2", which I carried over and did not re-read.

Shorthand for the three owner-list copies, all sent or kept by Leonard in Nov 2024:
- **G** = leonard@harmonygames.co_1816809274978043917.json[0], message `<CAPBs_a6zM=or+nDw0YSrZ3Rmkvzr0fnVHNBaaRqx6vN6Uxrs_Q@mail.gmail.com>`
- **S** = C04UEQVDVB7/1732646280.941869
- **D** = f_414596b0a9d698267dd1e1 (`/docs_documents/167`), percent only, no share counts

### Answer: the body-text token for Nebojsa

**In the mail between him and Robert the token is `PERSON_3941_NAME [PERSON_NAME_0127]`**: header first-name token plus body surname token, in the attribution line and in his signature, leonard@harmonygames.co_1773963101399472184.json[0] and [1]. That thread has no salutation, so it shows no first-name body token. For a salutation use **`[PERSON_NAME_0112]`**: Leonard writes "Hi [PERSON_NAME_0112]," at leonard@harmonygames.co_1773231301906977143.json[0], and he signs "Best Regards, / [PERSON_NAME_0112]" at [5] of the same thread. Robert and he are `[PERSON_NAME_0054] [PERSON_NAME_0112] quick chat` at leonard@harmonygames.co_1787089404106132003.json[0].

| Form | Where | Reach |
|---|---|---|
| `PERSON_3941_NAME <PERSON_3941_EMAIL>` | header, leonard@harmonygames.co_1773963101399472184.json[1] | Leonard |
| `PERSON_3935_NAME <PERSON_3935_EMAIL>` | header, leonard@harmonygames.co_1773231301906977143.json[5] | Leonard |
| `[PERSON_NAME_0112]` | first name, Gmail 93 bodies, Slack 47 in 2025-26; leonard@harmonygames.co_1773231301906977143.json[0] | Leonard |
| `[PERSON_NAME_0127]` | surname, Gmail 57 bodies; leonard@harmonygames.co_1773963101399472184.json[0] | Leonard |
| `[PERSON_NAME_0113]` | full name under PERSON_3935: Carta and `has accepted` mail, leonard@harmonygames.co_1796272391527772806.json[0] | Leonard |
| `[PERSON_NAME_6408]` | D; advisor name on f_3ee38465decc57e61df6e5; f_d7c7162985a73e86b40a12 row 15 | Leonard |
| `[PERSON_NAME_10455] [PERSON_NAME_0127]` | C04UEQVDVB7/1732646280.941869; Slack D04TJREVBMM 2025-07 idx 3 | Leonard for C04UEQVDVB7; D04TJREVBMM not checked |
| `Nebojsa [PERSON_NAME_0127]` | C04UTBZL6AX/1686163563.837369, Leonard's draft to Griffin, June 2023 | Leonard (`persona_view` YES on the channel) |
| `Nebojsa [PERSON_NAME_0127] <PERSON_3941_EMAIL>` | frederick@harmonygames.co_1815202866497734438.json | **not Leonard** |

**"Nebojsa" as a word is nearly absent.** It has 0 hits in Leonard's mailbox (from, to, subject, body), Docs, Drive, Sheets, Slides, GCal, Trello, Linear, Contacts and Confluence, and 2 hits in Slack, both the one message above and its block copy. A title of `Nebojsa` on ENG-2446 would be the first and only Linear use of that word, and it is not an owner-list form. If §2's rule stands, use G's `PERSON_3941_NAME [PERSON_NAME_0127]`.

### Findings that change seeds

1. **13 of the 26 §2 titles are not an owner-list form,** though §2 and §11 say "titles in owner-list forms". Exact in at least one copy: 9 (ENG-2443, 2444, 2445, 2448, 2452, 2453, 2456, 2457, 2461). Partial: 3 (ENG-2441 "Arthur Schaeppi" in D; ENG-2447 "[NATIONALITY_2251] Matthew Collins" in S; ENG-2458 "Martin Georgiev Walsh" in G). Off the list: ENG-2451, which is not on it at all. Not a form: ENG-2438, 2439, 2440, 2442, 2446, 2449, 2450, 2454, 2455, 2459, 2460, 2462, 2463. The plain names also hand a run the token-to-name join for ES-1, ES-5, ES-14, ES-15, ES-17 and ES-18. Your call: change the titles, or change the sentence in §2.
2. **Sunset's CEO has a second token and Sunset reached Leonard in Dec 2025.** leonard@harmonygames.co_1850505819404342075.json[0], `Re: exit referral`, from `PERSON_0769_NAME <PERSON_0769_EMAIL>`, Dec 8 2025, INBOX, signature `[PERSON_NAME_38055] / Founder & CEO, [ORGANIZATION_NAME_0453]`, quoting Dec 3 and Dec 5 notes signed `[PERSON_NAME_27772] / Founder & CEO, [PERSON_NAME_3207]`. `[PERSON_NAME_27772]` is also the signature token under PERSON_0767 in Feb. INFERENCE: same person. s4 lists neither this thread nor PERSON_0769. So "Name Sunset before its first base mention" (§11) needs a date: the first mail is Dec 2025, unanswered in the mailbox; the founders' first use is C07C2866011/1770839105.706739, Feb 11 19:45:05Z, and the intro leonard@harmonygames.co_1856675475513544349.json[12], Feb 11 19:41:54Z. The Feb 10 seeds stay safe either way if they do not name it.
3. **Bergmann's Contacts seed already has a base twin.** f_d7c7162985a73e86b40a12 "Family & Friends Distribution List", Leonard-owned, row 14: `Bastian Bergmann | PERSON_0693_EMAIL | Investor`. So the seed's name-to-address fact is not new, and the name is not only on a PDF. The same sheet row 13 has `Joe Schaeppi | PERSON_3063_EMAIL | Investor`.
4. **Enes has a third address.** Same sheet row 25: `Enes Disli | PERSON_5233_EMAIL | Investor`. In Leonard's mailbox PERSON_5233 is in `bcc` twice and 30 bodies, 0 `from` or `to`; no Contacts row. §2's per-address searches should include it.
5. **One token, two people.** Both Feb 11 letters to Claire (leonard@harmonygames.co_1856858053929740799.json[0], to PERSON_2360) and to Julia (leonard@harmonygames.co_1856861462411533365.json[0], to PERSON_2361) open "Hi [PERSON_NAME_0040],". Never key on `[PERSON_NAME_0040]`.
6. **A fourth advisor agreement is readable.** f_3ee38465decc57e61df6e5 "Harmony Games Advisor Agreement - [PERSON_NAME_0127]" is shared with Leonard, Arthur, Robert and PERSON_3941_EMAIL (`persona_view` YES). Census C2 lists three advisor agreements as no-persona (not re-checked here); this fourth one is readable. It names `[PERSON_NAME_6408]`, effective Jul 21 2023, "Compensation: Stock Options". I saw no grant size in the lines I read.
7. **Carta's fund names are capitals.** `GRIFFIN GAMING PARTNERS II, L.P.` and `GRIFFIN GAMING PARTNERS II SIDE FUND, L.P.`, leonard@harmonygames.co_1774928765255297348.json[0]. §2 writes them in mixed case.

### Founders

| Entity | Canonical | Values by service | Verdict |
|---|---|---|---|
| Leonard Hayes | `leonard hayes <leonard.hayes@harmonygames.co>` in mail; Slack `EMPLOYEE_0038_SLACK_ID`; Linear `usr_63fffeb4fab5233e`; Trello `PERSON_6094_TRELLO_USER_ID` | Mail header lowercase, leonard@harmonygames.co_1856872398290956689.json[0]. Thread alias `leonard@`. Body tokens `[PERSON_NAME_0357]` in D. Contacts `63fffeb4fab5233ed5bb73bf` job "Co-founder & CEO", roster "Co-founder & Creative Director". D gives the address as `leonard@harmonygames.co`, G and S as `leonard.hayes@` | DISAGREE (pre-existing, avoid): state no title |
| Robert | `robert <robert@harmonygames.co>`; `usr_Robert`; `EMPLOYEE_0016_SLACK_ID`; sign-off `[PERSON_NAME_0054]` | Own files show `"robert" <robert@harmonygames.co>`, threads/00001367.json[1]. G `[PERSON_NAME_0055]`, D `[PERSON_NAME_0174]`. Carta `[0054] [0085]` (from C2). Contacts `5f647df33ba6e92fbd56b05b` "Co-founder & Chief Product Officer", roster differs | DISAGREE (pre-existing, avoid): no surname exists, use `Robert` |
| Arthur Blake | `arthur blake <arthur.blake@harmonygames.co>`; `usr_cc3e90160f490686`; `EMPLOYEE_0025_SLACK_ID` | G, S literal; D `[PERSON_NAME_0152]`. Thread alias `blake@`. Contacts `cc3e90160f49068603998654`. "my CTO Blake", leonard@harmonygames.co_1856675475513544349.json[0] | AGREE. Trap with Schaeppi, see ENG-2441 |

### Outside people

| Entity | Canonical | Values by service | Verdict |
|---|---|---|---|
| KPMG associate | `PERSON_3088_NAME <PERSON_3088_EMAIL>`; body `[PERSON_NAME_46103]`, `[PERSON_NAME_46106]` | Gmail only, leonard@harmonygames.co_1817557789846606177.json[1], [5], [6]. Pronoun tail varies: `(she/her/ella)` [5], `(she/her/[PERSON_NAME_13208])` [6]. No Contacts row | DISAGREE (pre-existing, avoid): pick [6]'s form |
| KPMG FY23 sender | `PERSON_4416_NAME <PERSON_4416_EMAIL>` | leonard@harmonygames.co_1788910618703813283.json[1] from; cc on all FY24 | AGREE |
| KPMG cc | `PERSON_2322_NAME <PERSON_2322_EMAIL>` | cc on FY24, leonard@harmonygames.co_1817557789846606177.json[6]; 0 sent | AGREE |
| Griffin VP Finance | `PERSON_2847_NAME <PERSON_2847_EMAIL>`; bare `PERSON_2847_EMAIL` in FY24 cc | leonard@harmonygames.co_1817557789846606177.json[3] "Vice President of Finance"; cc on leonard@harmonygames.co_1856958794180374704.json. No Contacts row | AGREE |
| Griffin director | `PERSON_4337_NAME <PERSON_4337_EMAIL>`; Slack and body `[PERSON_NAME_1999]` | leonard@harmonygames.co_1856675475513544349.json[13]; C0ADGSZKR3R/1770664094.831769. Contacts `3cb768c4ca8515702d29b703`. `[PERSON_NAME_11413] Sanderson`, leonard@harmonygames.co_1767980387254277674.json[21]. "Philip Sanderson", f_0b29566cd7932a205d54d2 grid 53. "Phil Senderson", f_d7c7162985a73e86b40a12 row 6 | DISAGREE (pre-existing, avoid): use the token; the surname is misspelled in one sheet |
| Sunset partnerships | `PERSON_2888_NAME <PERSON_2888_EMAIL>`, "Head of Partnerships" | leonard@harmonygames.co_1856675475513544349.json[8], [10]; leonard@harmonygames.co_1856872398290956689.json[2]. No Contacts row | AGREE |
| Sunset CEO | `PERSON_0767_NAME <PERSON_0767_EMAIL>`, body `[PERSON_NAME_27772]` | leonard@harmonygames.co_1856675475513544349.json[1]; second token PERSON_0769, leonard@harmonygames.co_1850505819404342075.json[0]; Slack "[USERNAME_26907]’s CEO [PERSON_NAME_1674]" C0ADGSZKR3R/1770924399.692889; raw "Jackie Alfenas" f_0c37bb7235683d73569903 | DISAGREE (pre-existing, avoid): no raw name; no seeded voice |
| Sunset CTO | `PERSON_3131_NAME <PERSON_3131_EMAIL>` | cc only, leonard@harmonygames.co_1856675475513544349.json[0], [1] | AGREE |
| Tor principal | `PERSON_5275_NAME <PERSON_5275_EMAIL>`, body `[PERSON_NAME_0128]`, `[PERSON_NAME_0129]` | leonard@harmonygames.co_1763763695185138942.json[0]; Contacts `82103c829a5708060fb0b37b`; C04UEQVDVB7/1691688203.809779 | AGREE |
| TLAS counsel | `PERSON_5593_NAME <PERSON_5593_EMAIL>` | 46 from, leonard@harmonygames.co_1761203751780760643.json[0]. No Contacts row | AGREE |

### Companies and services

| Entity | Canonical | Values by service | Verdict |
|---|---|---|---|
| KPMG | `KPMG`; `KPMG LLP` in signature | Gmail 12 bodies, 0 subjects, leonard@harmonygames.co_1788910618703813283.json[1], leonard@harmonygames.co_1817557789846606177.json[6]. Slack 1: C04UEQVDVB7/1734502197.654509 "I’m doing some admin work that came from KPMG who audits [PERSON_NAME_2000] every year". All other services 0 | AGREE. Subject never says KPMG |
| Griffin Gaming Partners | Holder lines: Carta capitals. Firm in mail: `GRIFFIN GAMING PARTNERS` | G and S one line, 2,746,693. Carta two lines, leonard@harmonygames.co_1774928765255297348.json[0]. Tokens `[ORG_NAME_0153]` in 3 of 7 FY24 subjects, `[PERSON_NAME_2000]` in Slack and bodies. Gmail `Griffin` 50 subjects, `GRIFFIN` 149. Slack 69 and 35. Docs 22 and 43. Drive f_a285fd7c027c3214d74279. Sheets 32. Slides f_65ada5e24989d256cabdfa. GCal evt_ba5ecc9db15e916cb09338. Trello `688d21da8e97e855dd1e4fab`. Linear 0 | DISAGREE (pre-existing, avoid): two funds against one owner-list line |
| Sunset | Mail subject and body `Sunset`; site `www.sunsethq.com` | Gmail subject literal only on Leonard's forward and the platform mail: leonard@harmonygames.co_1856872398290956689.json[0], leonard@harmonygames.co_1856871594497249045.json[0]. PERSON_2888's own subject and body read `[PERSON_NAME_3207]`, leonard@harmonygames.co_1856872398290956689.json[2]. `[USERNAME_26907]` C0ADGSZKR3R/1770934638.035469. `[ORGANIZATION_NAME_0453]` leonard@harmonygames.co_1856675475513544349.json[2]. Literal in Slack C07C2866011/1770839105.706739. Docs f_0c37bb7235683d73569903. Linear, Trello, GCal, Contacts 0 | DISAGREE (pre-existing, avoid): redaction splits it. Seeds must use one form; a seeded subject in PERSON_2888's voice reading `Sunset:` matches Leonard's forward, not the same mail in his own copy |
| TLAS | `TLAS`; long form `Thompson Legal Advisory Services` | Gmail subject 7, leonard@harmonygames.co_1761376880237974314.json[0], leonard@harmonygames.co_1777571712831738060.json[0] "Side Letter TLAS(final).pdf". Long form 116 bodies. Docs f_6201c7027d02997bfb2c84, f_bc574824d936285e308cff. Drive 3 names. Slack D04UC0UEN2V/1692685020.042479. Case-sensitive body count 96 includes noise such as "ATLAS" | AGREE |
| Carta | `Carta` | Sender `SVC_0077` 75 messages. Gmail 108 subjects, 436 bodies; leonard@harmonygames.co_1856960478782792748.json[0]. Slack 148, C0ADGSZKR3R/1770935621.095649. Docs f_2193d150e5a25bb1e62f7d. Sheets 19, f_28ecc492b19f3696a19a97. GCal evt_3538f9ae24de3f714fef7d. Trello `64e3967c4bea2b815c99f59a`. Linear 0 | AGREE |
| Solsten | `Solsten`; `Solsten, Inc.` | Gmail 53 subjects, 242 bodies, leonard@harmonygames.co_1768168865446055418.json[0]; leonard@harmonygames.co_1770053656612413311.json[5]. Slack 205. Linear ENG-692, ENG-699. Trello `6522f6c5f5bb8e76a7c46b3f`, `65608db2d724afe3de602471`. GCal evt_2505da0f6006c1061a7417. Docs, Drive, Sheets, Slides also. Vendor and investor at once: C04UTBZL6AX/1686163563.837369 "CEO of Solsten", "COO of Solsten" | AGREE. A search for it returns mostly vendor work |
| TOR Capital Limited | `TOR Capital Limited` | G, S, D. Carta leonard@harmonygames.co_1778188119485709093.json. Docs f_6201c7027d02997bfb2c84. Gmail subject `Tor Capital` 109, leonard@harmonygames.co_1773160052067710033.json[0]. Slack C05TPHZA52P/1696030326.536399 | AGREE. Both casings base |
| Harmony Games | `[SOURCE_ORG_0001]` in Gmail subjects; `Harmony Games` elsewhere | leonard@harmonygames.co_1817557789846606177.json[6]; f_414596b0a9d698267dd1e1 | DISAGREE (pre-existing, avoid): token in Gmail seeds that sit beside base subjects |
| Standard Metrics | sender `SVC_0254_NAME <SVC_0254_EMAIL>` | leonard@harmonygames.co_1856787396431935562.json[0] Feb 11 2026, subject "Thank you for submitting your quarterly metrics and documents to GRIFFIN GAMING PARTNERS", empty body; Trello `688d21da8e97e855dd1e4fab` | AGREE. The mail proves a filing, not its content |
| IKE LOA LLC | as written | leonard@harmonygames.co_1770577968081445872.json[1]: "There is one mistake on IKE LOA LLC page ... It should read as PERSON_3941_NAME [PERSON_NAME_0127]" | DISAGREE (pre-existing, avoid): holder of record unresolved, never grade |
| Libra Softworks | `Librasoftworks` in mail | leonard@harmonygames.co_1769337922315876842.json[2]; C04RSEB8K0W/1677782755.640489 "Enes from Librasoftworks" | AGREE |

### The 26 holders

Carta names are from notices or digests. Other cells give the forms in G, S and D.

| Issue | §2 title | Id | Carta form, locator | Owner list | Other services | Verdict |
|---|---|---|---|---|---|---|
| ENG-2438 | Griffin Gaming Partners II, L.P. | SSP-01 | `GRIFFIN GAMING PARTNERS II, L.P.`, leonard@harmonygames.co_1774928765255297348.json[0] | one line `GRIFFIN GAMING PARTNERS` in G, S, D | see Griffin above | DISAGREE (designed): owner list merges, Carta splits. Use capitals |
| ENG-2439 | Griffin Gaming Partners II Side Fund, L.P. | SSP-02 | `GRIFFIN GAMING PARTNERS II SIDE FUND, L.P.`, same | same | see Griffin above | DISAGREE (designed), same |
| ENG-2440 | Segerstråle | SSP-03 | `[PERSON_NAME_0090]`, leonard@harmonygames.co_1775018766791066475.json (from C2) | G, S `[PERSON_NAME_0089] [PERSON_NAME_25152]`; D `[PERSON_NAME_6407]` | Mail subject `Segerstråle`, leonard@harmonygames.co_1777085008835619390.json[0]. Slack C096HFA5Z8W/1757285477.378439. `Segerstrale` f_7a6231aff4544d77ef5053, f_36e7af3301c8797ceb4695. PERSON_3336 and PERSON_3335, Contacts `ca57f88d55376b4341c5b6d4`, `1673c82fc650e0c42ab440d8`. Slack D04UC0UEN2V/1770665186.368229 | DISAGREE (pre-existing, avoid): two spellings, keep `Segerstråle` |
| ENG-2441 | Schaeppi | SSP-04 | `[PERSON_NAME_1909]`, leonard@harmonygames.co_1774928765255297348.json[0] | G `Arthur PERSON_3083_NAME`; S `Arthur [PERSON_NAME_41260]`; D `Arthur Schaeppi` | "Joe Schaeppi" leonard@harmonygames.co_1768150899514703140.json[0], f_d7c7162985a73e86b40a12 row 13. PERSON_3083, Contacts `aaf48372feabcf6490f30d7c`; PERSON_3063 no row | DISAGREE (pre-existing, avoid): Arthur against Joe, surname only |
| ENG-2442 | Bergmann | SSP-05 | `[PERSON_NAME_4468]`, leonard@harmonygames.co_1775018766791066475.json (from C2) | `[PERSON_NAME_4468]` in G, S, D | f_d7c7162985a73e86b40a12 row 14. "Patrick Bergmann" signature leonard@harmonygames.co_1770053656612413311.json[5]. PERSON_0693 mail leonard@harmonygames.co_1773213846196143460.json[0]. Slack C04UTBZL6AX 2024-05 idx 716 "Solsten/Bastian". No Contacts row | DISAGREE (pre-existing, avoid): "Patrick" is a redaction collision |
| ENG-2443 | [PERSON_NAME_52949] | SSP-06/08 | not named; which of 06, 08 unresolved (C2) | `[PERSON_NAME_52949]` in G, S, D | "Sadık Enes Dişli", leonard@harmonygames.co_1774211155651873582.json[0]. "Enes Disli" f_d7c7162985a73e86b40a12 row 25. Handles all three lines: leonard@harmonygames.co_1770141224265557526.json[1]. Slack C04RSEB8K0W/1677782755.640489; `[PERSON_NAME_66357]` C04UTBZL6AX/1686163563.837369. Trello `645521fa76b0c20c8e85d0a9`. PERSON_2260, Contacts `9498fdeb61155487c7a2eb59`; PERSON_5233 | DISAGREE (pre-existing, avoid): ı/ş against i/s; "Sadik" has 0 hits, the base spells it "Sadık" |
| ENG-2444 | Patrick Lewis | SSP-06/08 | not named | G, D `Patrick Lewis`; S `Patrick Haktan Dişli` | `Patrick Lewis <patrick@harmonygames.co>`, leonard@harmonygames.co_1768843320681522450.json[0]. Contacts `e704baa2167b3624a98b3352` "Patrick", "Business Development / Partnerships Manager" | DISAGREE (pre-existing, avoid): address collides with staff row |
| ENG-2445 | [PERSON_NAME_27652] | SSP-07 | "Eren Dişli accepted certificate SSP-07", leonard@harmonygames.co_1819317563486734449.json[0] | G, D `[PERSON_NAME_27652]`; S `[PERSON_NAME_79918] [PERSON_NAME_3237]` | PERSON_2275, leonard@harmonygames.co_1774211155651873582.json[10]; leonard@harmonygames.co_1770141224265557526.json[1]. No Contacts row | AGREE on identity. Carta gives the raw name; §2 keeps the surname off the title on purpose |
| ENG-2446 | Nebojsa | SSP-09 | `[PERSON_NAME_0113]`, leonard@harmonygames.co_1776829585766538915.json (from C2) | G `PERSON_3941_NAME [PERSON_NAME_0127]`; S `[PERSON_NAME_10455] [PERSON_NAME_0127]`; D `[PERSON_NAME_6408]` | see the answer above. Contacts `a65131d8d9f49c59825ffdaa`; PERSON_3935 no row. Advisor f_3ee38465decc57e61df6e5 | DISAGREE (pre-existing, avoid): title word is nearly absent |
| ENG-2447 | Matthew Collins | SSP-10 | "Husnu Matthew Collins", leonard@harmonygames.co_1777100628672295991.json[0] | G, D `[PERSON_NAME_11362]`; S `[NATIONALITY_2251] Matthew Collins` | Contacts `db57e559500151d6b3991b62` "Independent Director (investor/advisor, not an employee)". Slack user `/208`. `usr_ec7997064e6cfa96`. "Akin" Trello `672942f240a2e5e9c31db3ee`. Advisor agreement no-persona f_c2c881ccc407fbdaeaa362 (from C2) | DISAGREE (pre-existing, avoid): Contacts title is stale after May 1 2025 (C2) |
| ENG-2448 | TOR Capital Limited | SSP-11 | `TOR Capital Limited`, leonard@harmonygames.co_1778188119485709093.json (from C2) | same in G, S, D | see above | AGREE |
| ENG-2449 | Deepak | SSP-12 | PERSON_1287, leonard@harmonygames.co_1780271510271253861.json (from C2) | G `PERSON_1287_NAME`; S, D `[PERSON_NAME_0801]` | Gmail subject 8, leonard@harmonygames.co_1761915140407721365.json[0]. Slack C04UEQVDVB7/1697564685.716019. GCal evt_35bbd610f332e0e6a4ee9b. Trello `648254ff1013ac0804d43cb4`. Contacts `46aabf1857b0733da86c4649` | AGREE on first name; no surname in reach |
| ENG-2450 | Julia Lawson | ES-1 | `[PERSON_NAME_0043]`, leonard@harmonygames.co_1856960433624350836.json[0] | G, S `[PERSON_NAME_0043]`; D `[PERSON_NAME_0754]` | Letter "Hi [PERSON_NAME_0040]" to PERSON_2361, leonard@harmonygames.co_1856861462411533365.json[0]. Slack `/3`, EMPLOYEE_0005. `usr_8140f09bf9f1b94c`. Contacts `8140f09bf9f1b94cb8ee2dd7` | AGREE (s2 ties the tokens) |
| ENG-2451 | [PERSON_NAME_0100] | ES-2 | same, leonard@harmonygames.co_1808666480668498098.json[0] | not on the list: lapsed Nov 1 2024, before it | PERSON_3641 (from s2). Name unresolved | AGREE |
| ENG-2452 | Calvin Price | ES-3 | literal, leonard@harmonygames.co_1847333347700620793.json[0] | literal in G, S, D | Slack `/4`, `usr_49b9dfa5208d400d`, Contacts `49b9dfa5208d400d9b3937ca` | AGREE |
| ENG-2453 | Claire Morgan | ES-4 | literal, leonard@harmonygames.co_1856960410709778333.json[0] | literal in G, S, D | Letter "Hi [PERSON_NAME_0040]" to PERSON_2360, leonard@harmonygames.co_1856858053929740799.json[0]. Slack `/7`, `usr_7fe31e7ec8199618`, Contacts `7fe31e7ec81996189e1f14d6` | AGREE |
| ENG-2454 | Douglas | ES-5 | `[PERSON_NAME_0612]`, leonard@harmonygames.co_1847333395311994879.json[0] | `[PERSON_NAME_0612]` in G, S, D | Slack `/18`, `usr_cd7849ec043ab3da`, Contacts `cd7849ec043ab3da107f8c03` with blank last name. Card `(Douglas) Move Player Data...` `6656126aca6f7bb19b1c3619` | AGREE (from s2); single name is base |
| ENG-2455 | Victor Barnes | ES-6 | `Victor [PERSON_NAME_2770] [PERSON_NAME_0086]`, leonard@harmonygames.co_1830952527208439510.json[0] | same in G, S; D `[PERSON_NAME_5749]` | Slack `/17`, Linear id with a space `usr_Victor Barnes`, Contacts `20d3b9e691397554ea110e60` | AGREE. Activity ends 2025-04: no voice |
| ENG-2456 | Marcus Bennett | ES-7 | literal, leonard@harmonygames.co_1856960351896429942.json[0] | literal in G, S, D | Slack `/0`, `usr_c77c50cc15c5342d`, Contacts `c77c50cc15c5342d638ebb21`. Lookalikes Marcus Lee, Oscar Bennett | AGREE |
| ENG-2457 | Owen Baker | ES-12 | `[PERSON_NAME_0068]`, leonard@harmonygames.co_1856960504234892536.json[0] | G, S `[PERSON_NAME_0068]`; D `Owen Baker` | Letter "Hi [PERSON_NAME_0067]" leonard@harmonygames.co_1856860994291529096.json[0]. Slack `/11`, `usr_4e13bd40cc73d0fc`, Contacts `4e13bd40cc73d0fc76f87c7d`. Lookalike Thomas Baker | AGREE |
| ENG-2458 | Martin Walsh | ES-13 | `Martin [PERSON_NAME_7250] Walsh`, leonard@harmonygames.co_1856960563574318616.json[0] | G "Martin Georgiev Walsh"; S `Martin [PERSON_NAME_7250] Walsh`; D `Martin [PERSON_NAME_9416]` | Letter "Hi Martin" leonard@harmonygames.co_1856861229984402233.json[0]. Slack `/20`, `usr_51f5f16d46e8cf55`, Contacts `51f5f16d46e8cf55f5ee337b`. Lookalike Martin Lewis | AGREE |
| ENG-2459 | Vincent Parker | ES-14 | `[PERSON_NAME_0051]`, leonard@harmonygames.co_1856960478782792748.json[0] | G, S `[PERSON_NAME_0051]`; D `[PERSON_NAME_9942]` | Resignation leonard@harmonygames.co_1849344928983425627.json (from s2). Slack `/8`, Contacts `65c76e0b87aa7e9b84d1df22` "Game Systems Engineer" | AGREE (s2 proves the tie) |
| ENG-2460 | Brian Foster | ES-15 | `[PERSON_NAME_2769] [PERSON_NAME_0093]`, leonard@harmonygames.co_1856960532806250145.json[0] | same in G, S; D `[PERSON_NAME_43101]` | Letter to `brian <PERSON_4243_EMAIL>`, "Hi [PERSON_NAME_0092]", leonard@harmonygames.co_1856861400116562076.json[0]. Slack `/14`, `usr_fc22d5941b2aeb5c`, Contacts `fc22d5941b2aeb5c03ad32fa` | AGREE (from s2) |
| ENG-2461 | [PERSON_NAME_2768] [PERSON_NAME_0011] | ES-16 | same, leonard@harmonygames.co_1847333318158821452.json[0] | same in G, S; D `EMPLOYEE_0032` | Contacts `d4a339f7f6aafffdc2dabb9a`. `usr_EMPLOYEE_0032`. `cameron@` in the letter leonard@harmonygames.co_1847333990408253969.json (from s2). Josh Dempsey is a separate person (s2) | DISAGREE (pre-existing, avoid): never write Josh Dempsey |
| ENG-2462 | Frederick Stone | ES-17 | `[PERSON_NAME_0038]`, leonard@harmonygames.co_1847333272519888206.json[0] | G, S `[PERSON_NAME_0038]`; D `[PERSON_NAME_0172]` | "ryan" `PERSON_2314_EMAIL`, leonard@harmonygames.co_1856226460086133468.json[3], f_d7c7162985a73e86b40a12 row 11. GitHub shows "Ryan". Slack `/6`, `usr_175c0d7bc72ed244`, Contacts `175c0d7bc72ed244b944cb90`, job differs from roster | DISAGREE (pre-existing, avoid): no first name in seeded prose other than the title |
| ENG-2463 | Oliver Brooks | ES-18 | `[PERSON_NAME_0022] [PERSON_NAME_2767] [PERSON_NAME_2763]`, leonard@harmonygames.co_1856960382677662910.json[0] | G, S `[PERSON_NAME_0022] [PERSON_NAME_32704]`; D `[PERSON_NAME_36999]` | Slack `/1`, `usr_bdf01b53c6a92c5e`, Contacts `bdf01b53c6a92c5e167c658c`. Lookalike Lauren Brooks | AGREE (from s2) |

### Documents the seeds name

| Record | Locator | Value | Verdict |
|---|---|---|---|
| Investor email draft | C0ADGSZKR3R/1770664700.848759 | "Hi everyone, / I’m writing to share a difficult update: we have decided to wind down harmonygames." Unsent | AGREE |
| Promise to reach out | C0ADGSZKR3R/1770664924.520089; D04UC0UEN2V/1770665186.368229 | "reach out to investors one by one"; "personally reach out to every angel investor" | AGREE |
| Feb 12 list | C0ADGSZKR3R/1770934638.035469; then /1770935621.095649 "Carta terminations are done" | Three items; one closed 16 min later | AGREE |
| Linear line | C0ADGSZKR3R/1770933601.686309 | "linear we keep during transition" | AGREE |
| Nov 2024 owner list | leonard@harmonygames.co_1816809274978043917.json[0]; C04UEQVDVB7/1732646280.941869; f_414596b0a9d698267dd1e1 | 27 lines, stock and options merged, Griffin merged | DISAGREE (designed): stale against Carta, the seeds quote it dated |
| Jan 22 term sheet | f_11040fe5d66821bd6951aa (`/docs_documents/40`) | "Options outstanding:" 268,772 in the ledger inputs; created 2026-01-22, owner Leonard, unshared | DISAGREE (designed): stale at the clock (C2 §B) |
| Termination details | leonard@harmonygames.co_1856960478782792748.json and 13 siblings | 14 notices, 8 sent Feb 12 22:29-22:33Z | AGREE |
| FY23 request | leonard@harmonygames.co_1788910618703813283.json[1] | Subject has ` - ` before the token, due 2/2/2024 (s4) | AGREE |
| FY24 request | leonard@harmonygames.co_1817557789846606177.json[6] | "year ended December 31, 2024"; due 12/20/2024; confirmation as of September 30, 2024 per [2] | DISAGREE (designed): as-of date differs from FY25, H4's decoy |
| Griffin filing | leonard@harmonygames.co_1856787396431935562.json[0] | §11 cites it for financials: a receipt with an empty body | AGREE |
| Task List | f_31115ddb6ed866f2b10d60 | `Task List.xlsx`, owner Resource 7240, shared with the founders, modified 2026-02-10T20:33:24Z | AGREE |
| Wind Down folder | d_e5caf6a8c630421942ee59 | Owner Resource 7240, empty sharing, `persona_view` NO | DISAGREE (designed): H1 says why this folder is not used |
| Signed side letter | leonard@harmonygames.co_1777052222643175480.json; Drive draft f_6201c7027d02997bfb2c84 | Thread "Re: [SOURCE_ORG_0001] Second Close- Tor Capital - [PERSON_NAME_0132]- signing and closing", Sep 2023. PDFs unread by rule. Draft is unsigned | DISAGREE (designed): H3 against its draft |
| Sunset SOW | leonard@harmonygames.co_1856956483320787350.json | Signed copy, attachment unread | AGREE by subject only; content unread |
| First investor update | f_5a4fb6c74aab30e85771e5; leonard@harmonygames.co_1799418746420547240.json[2] | Doc shared with Robert, Arthur; sent May 18 2024 | AGREE |
| Done card | Trello `68c5a49e8491a9d7faf869d0` | "Existing Investor Update", open in Done, idShort 455, last activity 2025-11-12 | DISAGREE (pre-existing, avoid): do not touch |
| Deck title idiom | f_418f5adef3a62a0e55c427 "Harmony Games March 25 Investor Update"; f_65ada5e24989d256cabdfa "Harmony Games BoD Jan 14 2026" | Both owner Resource 7240, shared with founders | AGREE |
| Investor list | f_0b29566cd7932a205d54d2 "Internal Game Investor List - harmonygames" | Prospect list, not holders; `persona_view` YES | AGREE. Same base also has f_84bb5ab28c0a3bbfd21339 and f_89573e9255062562af2977 |

## 1.C Voice and realism

Quotes are verbatim from records read through `hg.py search`, line breaks shown as ` / `. Hours are UTC. Keys cited from `references/universe_kb/by_universe/normal/conventions.json` (build `per-universe-v1`) are named each time.

### status_at_clock (activity.json)

leonard.hayes@harmonygames.co · activity.json · active_feb_2026
robert@harmonygames.co · activity.json · active_feb_2026
arthur.blake@harmonygames.co · activity.json · active_feb_2026

`PERSON_3088_EMAIL`, `PERSON_2888_EMAIL` and `PERSON_2847_EMAIL` have no key in `people`: external people are not in activity.json, so they get no line. Their last authored records are below.

**Check for the gate.** activity.json's last service dates differ by service, and two matter here:
- Robert: `gmail_sent` 2025-11-18, `slack` 2026-02-13, `linear` 2025-10-20. `seed_voice_candidates_feb_2026` shows `gmail_sent_2026_02` 0 for him. The §11 reply to Nebojsa on 2026-02-12 would be his first sent mail in 86 days. It is allowed, and it is visible.
- Leonard: `linear` 2025-11-01 and Trello last action 2025-11-13, so the Feb 12-13 Linear and Trello seeds are 3-month jumps, as s4 says. Arthur: `linear` 2025-10-27.

### Leonard, Slack

| Locator | Quote |
|---|---|
| C0ADGSZKR3R/1770934638.035469 | "next things for me are / • Carta terminations / • Reaching out to our angels properly and let them know about the situation / • onboarding with [USERNAME_26907] and giving them the data  / Nothing urgent is left on my plate as of now" |
| C0ADGSZKR3R/1770933601.686309 | "During shutdown, let’s keep Deel, gusto, Intuit. I canceled other subscriptions under mine. Figma won’t be able to charge us by the time it’s time for renewal. linear we keep during transition" |
| D04UGG61DUM/1770857767.826609 | "I’ll try Google next and if I don’t figure it out I’ll get your help" |

- Length: `conventions.json slack.per_person_hours_and_style["leonard.hayes@harmonygames.co"].style.len` p10 16, p25 26, p50 47, p75 81, p90 133, p99 689. Feb 2026 by container, from the shards: #winddown p50 54, p90 254; DM with Arthur p50 37, p90 93; DM with Robert p50 38, p90 101.
- Capitalisation: `lower_start_share` 0.50, `all_lower_share` 0.31. So half his lines open with a capital, and "I" stays capital. Curly apostrophes (’) in most Feb lines. `ends_punct_share` 0.15: lines mostly end bare. `multiline_share` 0.02, `emoji_share` 0.03. Typos stay in: "archieve" C0ADGSZKR3R/1770933903.645709, "eveything" D04UGG61DUM/1770846858.266139. Odd capitals such as "getting There" D04UGG61DUM/1770858403.238869 and "Chase" C0ADGSZKR3R/1770934065.485929 look like redaction artefacts: do not copy them.
- Bursts: 1-liners a few seconds apart, D04UGG61DUM/1770857740.944709 to /1770857767.826609 is 4 lines in 27 s. A list goes in one message with `•`.
- Sign-off: none in Slack, except drafts pasted for review ("Thanks,\nLeonard" in C0ADGSZKR3R/1770664094.831769).
- Hours: `slack_core_80pct_window_utc` start 15, 11 hours, end 02. `weekend_share` 0.133. Feb 2026 peaks: #winddown 01, 22, 19, 21; DM with Arthur 00, 19, 14; #executives 19, 04, 05, 23.
- Seeds: C0ADGSZKR3R/1770938120.410229 at 23:15Z is inside the window. D04UGG61DUM/1770949310.220519 at 02:21Z is at its edge; his Feb DM count at hour 02 is 7 and Arthur's is 11, so it is real.

### Leonard, Google Docs notes to himself

**How he actually writes them.** No heading, no date, no salutation, no sign-off. The Doc title is the topic. The body is one bullet list of topic words, each followed by questions in full sentences, ending on loose reminders. He writes to a future self or to the person he will ask. `style_runs` confirm it: `f_2193d150e5a25bb1e62f7d` is `NORMAL_TEXT` throughout on `list_1`, nesting 1, no TITLE run. Status words are bare. Other people are named in passing, and speakers get a tag in the second example: "Leonard: Influencers who only like money will not work", "robert: Reddit sucks".

**Example 1.** `f_2193d150e5a25bb1e62f7d` "Questions for Benjamin", owner Leonard, private, unshared, created 2023-08-29T15:22:04Z, modified 15:36:53Z, 2,162 characters, `/docs_documents/76`. It is the closest base match: investor paperwork, Carta, signatures. Opening lines:

> Loan Repayment
> Loan repayments - what are the next steps? Should we use Carta/docusign to collect signatures and email board members before hands? What's the typical flow?
> Re-execute the receipts
> Advisors
> The steps are
> Get 409a approved by the boards
> Get signatures from advisors

and later: "[PERSON_NAME_2950] is silent. If we drop him, is There any paperwork we need to do?", "I am following up with [PERSON_NAME_23197]- will send him an email".

**Example 2.** `f_3dab0db469c796cb67a744` "GUERRILLA TACTICS_", owner Leonard, private, unshared, created 2025-05-29T18:46:42Z, modified 2025-06-04T16:56:07Z, 4,517 characters, `/docs_documents/156`. One TITLE run, then lists. Opening lines:

> GUERRILLA TACTICS
> publishing
> Current thinking is hang tight to West T1-T2 for self-publishing, anywhere else is a fair game bcs we don’t have the bandwidth or the local knowledge to win
> Web publishing - webgl
> Influencers
> Can we do some rev share with influencers?

**Also read.** `f_c93610d98ad0e8496393c4` "Research for 2nd game" opens "[USERNAME_10412], is it Puzzle first, then RPG? Or the other way around? / Gender, is it male skewed? By how much?" `f_60216713de49328f5afac4` "Untitled document" opens "IOS 522 Feedback / Bugs / 1- Level 1 animations stutters twice." The `1-` list form is his, in mail and Linear too.

- Length: these run 490 to 4,517 characters. `conventions.json docs_sheets_slides_drive.doc_body_len_chars` p10 324, p25 1,851, p50 5,069.
- Title: plain topic, no date. `doc_title_families_top` is dominated by legal and meeting docs, so it does not help here.
- Hours: created 15:22Z, 18:46Z, 19:27Z, 20:24Z on these four.
- Seed check: §11 dates H1 at 2026-02-13T01:05:00Z and its decoy at 2026-02-10T17:40:00Z. The second is in band, the first is off these four but inside his Slack window. A notes Doc that opens with "Dear" or a date line, or that uses headed sections with `1.` clauses, would not match these. A rule stated in plain sentences under a topic word is fine: Example 1's bullets are sentences, and `1- ` lists are his.

### Leonard, Linear descriptions

| Locator | Quote |
|---|---|
| ENG-2366 | "As we put the game in the maintenance mode, there are a couple of things I'd like to accomplish / 1- Refresh IAP payout list using this list here: [[URL_52550]) / We are overly generous with some of the packs - time to jack up the prices" |
| ZOM-436 | "Some tutorial steps are hooked to the analytics and are now sending step_name_str. Please make sure all tutorial steps including booster tutorials, pre_booster, win_Streak etc. send these steps as well so we know if users are having issues passing those steps." |
| ZOM-549 | "Similar to [ZOM-548](https://linear.app/harmonygames-games/issue/ZOM-548/track-events-for-boss-arena-as-listed-in-the-spreadsheet) we need to add the following fields to the other 2 game modes (details in the spreadsheet as usual)" |

- Length: 314 issues created by `usr_63fffeb4fab5233e`, 309 with a description: p50 237, p90 1,111, max 4,822. `conventions.json linear.description_len_chars.ENG` p50 274, p90 980.
- Capitalisation: sentence case, full stops, `1-` lists, "we need to". From July 2025 many are Slack-created with the prefix `'@Leonard said:` (ZOM-672, ZOM-435).
- Sign-off: none.
- Hours: created-at peaks 18, 23, 22, 19, 17, 21. Last created 2025-11-01T02:39:35Z.
- Titles: `conventions.json linear.title_prefixes_by_team.ENG` shows `<none>` on 2,119, so a bare name title fits. Team spread: ENG 283 of 314, which supports `team_ENG`.
- Linear comments: base has 0, so no voice exists. The nearest is the Slack-to-Linear form above. Arthur's created issues are short and factual ("The issue has changed. It wasn't highlighting good enough back then but now, it's completely gone" ZOM-377). Robert's are `'@[PERSON_NAME_0054] said:` paste-ins, and once in capitals: "UPDATED 10/8/2025 PLEASE CHANGE DEMOTION TO -2 LEVEL TIERS PER DEMOTION!!!!" ZOM-600.

### Leonard, Trello

| Locator | Quote |
|---|---|
| action `64432476d80f14f72c41e882`, card `64137ef56367ed1bf765ee8b` | "we have enough angels for now" |
| action `66e4d13497f9c550531cd82e`, card `66cca9e524b341eb89492c81` | "Apple application done, waiting for verification. Google needs DUNS to tie it back to us - emailed [EMAIL_176407] to get their help." |
| action `641358f42a2a15f1628233fa`, card `6406452a958cef85d5fa6230` | "Reached out to [PERSON_NAME_54605] to close the loop" |

- Card names, To Do list `640643a3fd8f3ca308d93195`, all 10 closed: "pay solsten" `6522f6c5f5bb8e76a7c46b3f`, "Expenses" `65134a02a716fa87aae0cb21`, "Animator contract" `6528d87a8f81739970e9577d`, "Playtestcloud?" `66443c64297aae608e26e3a7`. Short, often lowercase, 9 of 10 with an empty `desc`.
- Length: comments 20-130 characters. `conventions.json trello.desc_len` p50 202, but only 190 of 803 cards have one.
- Sign-off: none.
- Hours: his 23 comments fall at 00, 04, 07, 16-19, 21-23. Last Leonard comment `680fc2d2e4aae3a9657b5fbc` 2025-04-28, "1 week to implement, at least 1 week to balance".
- `conventions.json trello.action_types`: commentCard 56 of 5,294, so comments are rare anywhere on Trello.

### Leonard, mail

| Locator | Quote |
|---|---|
| leonard@harmonygames.co_1817557789846606177.json[4] | "Thank you for the email. I missed the previous one. I will take care of it / before the deadline. / Best regards, / Leonard" |
| leonard@harmonygames.co_1856675475513544349.json[3] | "This looks great - ready to sign. Please feel free to send it via docusign / or equivalent for signatures. / Thank you for quick turnaround and collaboration on this! / Leonard" |
| leonard@harmonygames.co_1774211155651873582.json[2] | "We are confirming we received the wire transfer for all three Disli / brothers! (please see the screenshot). Welcome to [SOURCE_ORG_0001] again / officially! We are looking forward to adding zeros to your investment / together. / Cheers, / Leonard" |

- Length: `conventions.json gmail.per_sender_new_text_len["leonard.hayes@harmonygames.co"]` n 1,877, p25 113, p50 252, p75 604, p90 1,510. Subject: `gmail.internal_subject_len_chars` p50 42.
- Capitalisation: normal sentences, wrapped near 72, `\r\n` or `\n`.
- Sign-off: `Best regards,\nLeonard` to outsiders and in admin mail; `Cheers,\nLeonard` to angels; bare `Leonard` when replying fast. `Hi <name>,` opens. Numbered answers use `1- ` (leonard@harmonygames.co_1817557789846606177.json[2]).
- Hours: his 36 sent messages in threads numbered 1854-1857 (Jan 13 to Feb 12 2026): 20 (9), 21 (6), 23 (5), 22 (4), 19 (3).

### Robert, mail to friends

**He has written to Nebojsa exactly once in his own words.** A complete scan of `to` across all 88,726 threads lists every message to `PERSON_3941` (8) and `PERSON_3935` (7), and I read them. Robert's only authored one is this one-word reply:

> Thanks!!!

`leonard@harmonygames.co_1773963101399472184.json[0]`, Aug 11 2023, To `PERSON_3941_NAME <PERSON_3941_EMAIL>`, cc Leonard, no sign-off, same message in Robert's mailbox as `threads/00001367.json[1]`. Everything else from Robert to him is a calendar invite: leonard@harmonygames.co_1787089404106132003.json, 1796464455902443901, 1820532138485142593.

| Locator | Quote |
|---|---|
| leonard@harmonygames.co_1763666036216513380.json[1] | "Hi [PERSON_NAME_2325], / [PERSON_NAME_24103].. I can totally relate, my daughter broke her arm literally jumping up / and down on the bed when she was 3. I have never broken a bone in my life / and yet my daughter managed to out street cred me at a young age. / Take it easy. / [PERSON_NAME_0054]" |
| threads/00015409.json[0] | "Hey [PERSON_NAME_8105]! / As discussed, here is the pitch deck. I know it's a pretty tough / environment right now to find gaming in funding, but we're trying either / way so we can keep going since we really like what we do and we like the / team we have assembled. [...] Any thoughts/questions/feedback would be appreciated! / Thanks! / [PERSON_NAME_0054]" |
| leonard@harmonygames.co_1768591899776295250.json[1] | "It was great meeting you as well! [...] I wish you the very best and we'll definitely stay in touch. / Cheers, / [PERSON_NAME_0054]" |

- **Sign-off:** a thanks line, then his name alone on the next line, in the token form `[PERSON_NAME_0054]`. Over 181 non-calendar messages, counting copies in other mailboxes, the commonest close is `Thanks` / `[PERSON_NAME_0054]` (35), then `Thanks,` (4), `Thanks!` (3), `Cheers,` (3), `Take it easy.` (3). No title, no signature block, no company line.
- Opening: "Hey <name>," or "Hi <name>!" with an exclamation to people he knows. Warm, then plain facts.
- Length: `conventions.json gmail.per_sender_new_text_len["robert@harmonygames.co"]` n 114, p25 50, p50 197, p75 448, p90 1,148. My non-calendar set: p50 205.
- Capitalisation: normal sentences. Straight apostrophes, unlike Leonard's curly ones in Feb Slack. Exclamations common.
- Hours: 21, 23, 18, 20, 19 lead; a night tail at 02, 04, 05. Last authored mail 2025-11-18T20:07Z, threads/00015993.json[0].
- Seed: 2026-02-12T23:41:12Z is in band. His `from` is `robert <robert@harmonygames.co>` in Leonard's file and `"robert" <robert@harmonygames.co>` in his own; his Sent label is `["SENT"]`.

**Seed fit, your call.** The §11 parent is a 2023 wire notice, so the seed's subject would be `Re: Funds Transfer Request #450904566 Has Been Scheduled`, 2.5 years late, on a bank mail. A newer thread holds both men: leonard@harmonygames.co_1843007315645862923.json[0] `Fwd: Follow-up on intros`, Sep 15 2025, Leonard to PERSON_3941, PERSON_3935 and Robert; Robert's copy is threads/00015319.json. The §11 thread does keep the subject free of closing words. If kept: `in_reply_to` `<CAGkro_Ox2wP8TQrYO9J2+FkfLbZqy_NixtRjOS7wcBeB3pFZtA@mail.gmail.com>`, `references` `<1002618385.1717453.1691782739607@jlppacebcwls01.onefiserv.net> <CAE426NoTs38nTRaaAq=2u4nYuWZwpwtjTiJ6KAL+WBERzGLm6Q@mail.gmail.com>` plus that id.

### Robert, Slack

| Locator | Quote |
|---|---|
| D04UP2L3E3S/1770848224.438989 | "don't think it's too early to be short on gold?" |
| D04UP2L3E3S/1770914193.165359 | "Yeah not very helpful" |
| C0ADGSZKR3R/1770859331.924229 | "I should have dumped more of my work into Figma then" |

- Length: `conventions.json slack.per_person_hours_and_style["robert@harmonygames.co"].style.len` p10 13, p25 24, p50 42, p75 73, p90 121. Feb DM with Leonard p50 43, p90 113; #winddown p50 35, p90 52.
- Capitalisation: `lower_start_share` 0.31, `all_lower_share` 0.21, `ends_punct_share` 0.15, `emoji_share` 0.01. Terse: "Ok", "All done", "oh OK".
- Sign-off: none.
- Hours: `slack_core_80pct_window_utc` start 16, 12 hours, end 04. Feb 2026 peaks 04, 05, 01, 02.

### Arthur Blake, Slack DM

| Locator | Quote |
|---|---|
| D04UGG61DUM/1770857699.580189 | "i don't think i do" |
| D04UGG61DUM/1770857961.753109 | "we have like 10 different AWS Accounts" |
| D04UGG61DUM/1770858816.197309 | "I like to count my chickens before they hatch otherwise I never get to count them." |

- Length: `conventions.json slack.per_person_hours_and_style["arthur.blake@harmonygames.co"].style.len` p10 9, p25 18, p50 40, p75 72, p90 121. Feb DM with Leonard n 45, p50 38, p90 99, max 130.
- Capitalisation: `lower_start_share` 0.43, `all_lower_share` 0.33, and lowercase "i" is common in the DM, 0.58 lower start there. `ends_punct_share` 0.28, the highest of the three; straight apostrophes.
- Bursts: 4 lines in 39 s, /1770857942.199919 to /1770857981.435489.
- Sign-off: none.
- Hours: `slack_core_80pct_window_utc` start 15, 10 hours, end 01; `calendar_tz` America/New_York. Feb DM peaks 00, 02, 19, 14. Last Slack post in the export 2026-02-12T23:00:32Z, C0ADGSZKR3R/1770937232.664809, so a reply on Feb 13 at about 02:22Z is after his last base post. It is his 02 hour, with 11 DM posts that month.

### KPMG, PERSON_3088

| Locator | Quote |
|---|---|
| leonard@harmonygames.co_1817557789846606177.json[6] | "Hello, / KPMG is currently engaged in the audit of GRIFFIN GAMING PARTNERS for the year ended December 31, 2024. Please see the attached confirmation and return directly to us via email by replying to all Recipients herein. If you do not have access to the audited numbers at the time of this request, please provide the unaudited year end estimate. / We appreciate your response by 12/20/2024. Should you have any questions, please feel free to contact us directly. / Thank you in advance," |
| leonard@harmonygames.co_1817557789846606177.json[5] | "Hello, / I wanted to follow up regarding our confirmation request letter. We ask that you prioritize this request. If There is a different individual within your organization we should direct our request to, please let us know. / Appreciate your assistance and please let us know if you have any questions! / Best," |
| leonard@harmonygames.co_1817557789846606177.json[1] | "Hello Leonard, / Thank you for the support! Regarding item 2 of the Financial Statements, could you please provide the most recent audited/unaudited statements. I reviewed the support and unfortunately these items would not load. Your assistance is greatly appreciated! / Best," |

- Total authored: these 3, all Dec 2024. Complete scan of all mailboxes: `PERSON_3088` in `from` 3 hits.
- Length: about 260-400 characters before the signature.
- Capitalisation: formal, full sentences, "Hello," opening. "Recipients" capitalised in the template. "There" with a capital is a redaction artefact, do not copy it.
- Sign-off: `Thank you in advance,` or `Best,`, then
  `[PERSON_NAME_46103] (she/her/[PERSON_NAME_13208])` / `Audit Associate` / `KPMG LLP | 55 Second Street | Suite 1400 | San Francisco, CA 94105` / `PERSON_3088_EMAIL` / `kpmg.com/us`, then a `****` confidentiality block on the root. [5] shows `(she/her/ella)` instead of the token, and [1] has `[PERSON_NAME_46106]` as a first-name line above it.
- Hours: 2024-12-05T00:22:55Z, 2024-12-17T19:48:30Z, 2024-12-18T23:55:10Z, which are 16:22, 11:48 and 15:55 Pacific. Seed 16:48:33Z is 08:48 Pacific, earlier than all three and plausible.
- Reply-all: the template says it, and every FY24 reply kept the Cc. Griffin's cc `PERSON_3077` is shown `[Deactivated]` in [3].

### Sunset, PERSON_2888

| Locator | Quote |
|---|---|
| leonard@harmonygames.co_1856675475513544349.json[8] | "Hi Leonard, / Thanks for taking the time to chat. I really appreciate it. I wanted to send over a few notes and next steps below based on our conversation: / *Data* / You should have just received an invite to our platform. [...] *Wind-Down* / I've attached your proposal and all-in quote. One with tax work, one without. If it looks good, these are the next steps: / * I'll send over our contract and invoice / * Once signed, we'll send over our onboarding intake / * From There, our legal team will create your Plan of Dissolution and we'll setup a kickoff call to get things started. / Please let me know if you have any questions—happy to hop on another call at any point. / Best," |
| leonard@harmonygames.co_1856872398290956689.json[2] | "Hi Leonard, / [PERSON_NAME_3207] cannot support negotiating the release of claims. However, I've provided two templated emails to support with handling that outreach directly." |
| leonard@harmonygames.co_1856675475513544349.json[10] | "Hi Leonard, / Nice to meet you. / Are you available to connect at 5:30 ET today ? / Best," |

- Total authored in Leonard's mailbox: 3 human mails plus 1 `Accepted:`, all Feb 11. `PERSON_2888` in `from` across all mailboxes: 8, which are copies of these.
- Length: 60 to about 900 characters, then the signature; templates push the Release of Claims mail longer.
- Capitalisation: warm, sentence case, `*Bold*` section labels and `* ` bullets, which is how Superhuman's text comes through.
- Sign-off: `Best,` / blank / `PERSON_2888_NAME` / blank / `Head of Partnerships` / blank / `M: [PHONE_15402]` / blank / `W: www.sunsethq.com ( http://www.sunsethq.com/ )` / blank / `Sent via Superhuman ( https://sprh.mn/?vip=PERSON_2888_EMAIL )`.
- Hours: 2026-02-11T21:51:44Z, 23:05:00Z, 23:11:52Z. He works on Eastern time ("5:30 ET"). Seed 18:06:21Z is 13:06 ET, earlier than all three, inside a working day.
- Context: the CEO's Feb 12 mails use the same `*Label:*` plus `* ` shape, and "the legal team" and "kickoff call" wording, leonard@harmonygames.co_1856675475513544349.json[1].

### Timing of the seeds against these bands

| Seed | UTC | Band | Result |
|---|---|---|---|
| Linear project and issues | Feb 12 23:24-23:25 | Leonard Linear 23 is a peak | in band |
| Robert to Nebojsa | Feb 12 23:41:12 | Robert mail 23 is a peak | in band, first sent since Nov 18 |
| #winddown burst | Feb 12 23:15:20 | Leonard Slack 15-02 | in band |
| DM burst | Feb 13 02:21:50 | Leonard and Arthur hour 02 | edge, real |
| H1 notes | Feb 13 01:05 | Docs sample 15-20; Slack 15-02 | off the 4 Docs, inside Slack |
| Trello card | Feb 13 02:40 per §11; id says Feb 12 22:54:08 | Leonard Trello 00, 04, 21-23 | see 1.F |
| KPMG root | Feb 13 16:48:33 | PERSON_3088 19-00 | 3 h early, plausible |
| Sunset mail | Feb 13 18:06:21 | PERSON_2888 21-23 | 3 h early, plausible |

## 1.D Keyword

Every count is a complete scan: `scan_complete` true, no query reached its limit of 200,000 (5,000 for Slack Feb). **Raw** is the tool's case-insensitive substring match per scalar value. **Word** is my filter on the returned excerpt, with word boundaries, so it is a floor: a value whose first match is "dashboard" and second is "board" counts as not a word hit. Use Word to judge relevance.

Scope:
- Gmail "Leonard" = 17,635 files `threads/leonard@harmonygames.co_*.json`, keyed on `subject` or `body`, so headers do not count. Gmail "all" = 88,726 files. A run sees Leonard's only.
- Slack rows are evaluator-wide, 687,230 records. The `text` key also matches `blocks/.../text` copies, so one message can count twice. hg.py does not filter by persona. Every Slack locator below was run through `persona_view can-see leonard_hayes slack`; the result follows the table.
- Sheets "any cell" also matches title and owner fields. Slides "text" is element text.
- Scanned with 0 raw hits and not listed unless a seed adds the term: see the zero table.

Locator forms: Gmail `leonard@harmonygames.co_<id>.json[msg]`, numbered `NNNNNNNN.json[msg]` for other mailboxes; Slack channel/ts.

| Term | Service, field | Raw | Word | Locator or NEW TERM |
|---|---|---|---|---|
| investor | Gmail, Leonard, subject | 97 | 97 | leonard@harmonygames.co_1765393440967175951.json[0] |
| investor | Gmail, Leonard, body | 1500 | 1478 | leonard@harmonygames.co_1761203751780760643.json[0] |
| investor | Gmail, all mailboxes, subject | 225 | 225 | 00000066.json[0] |
| investor | Slack, Feb 2026, all channels | 9 | 9 | C07C2866011/1770083784.662879 |
| investor | Slack, all time, all channels | 931 | 923 | C04RSEB8K0W/1677737457.418379 |
| investor | Linear descriptions | 1 | 1 | ZOM-430 |
| investor | Docs titles | 9 | 2 | f_5a4fb6c74aab30e85771e5 |
| investor | Docs body | 83 | 83 | f_05f0d3a2bde055336fa177 |
| investor | Drive names | 24 | 10 | d_812f12769553081073e51e |
| investor | Sheets titles | 10 | 9 | f_0b29566cd7932a205d54d2 |
| investor | Sheets, any cell | 28 | 27 | f_0b29566cd7932a205d54d2 |
| investor | Slides titles | 1 | 1 | f_418f5adef3a62a0e55c427 |
| investor | Slides text | 74 | 74 | f_0281d5b83f931db7fff2be |
| investor | GCal summary | 4 | 4 | evt_9a8faed31d5ef3d9b2dcab |
| investor | Trello card name | 5 | 5 | 6416439c5b25384ba9035374 |
| investor | Contacts job | 1 | 1 | db57e559500151d6b3991b62 |
| investor | Confluence, any | 6 | 6 | confluence_working.json /pages/19/body |
| angel | Gmail, Leonard, subject | 14 | 13 | leonard@harmonygames.co_1776421620687714369.json[0] |
| angel | Gmail, Leonard, body | 4923 | 483 | leonard@harmonygames.co_1761203751780760643.json[0] |
| angel | Gmail, all mailboxes, subject | 49 | 48 | 00001538.json[0] |
| angel | Slack, Feb 2026, all channels | 6 | 4 | C07C2866011/1770083449.258599 |
| angel | Slack, all time, all channels | 475 | 188 | C04RSEB8K0W/1677782755.640489 |
| angel | Linear descriptions | 2 | 1 | ENG-1688 |
| angel | Docs body | 6 | 5 | f_05f0d3a2bde055336fa177 |
| angel | Sheets titles | 2 | 1 | f_efaec72066ee44e5888bd7 |
| angel | Sheets, any cell | 6351 | 27 | f_0b29566cd7932a205d54d2 |
| angel | Slides text | 7 | 7 | f_65ada5e24989d256cabdfa |
| angel | Trello card name | 1 | 1 | 646bf1d5a038bfcd4c6cde85 |
| angel | Trello comment | 1 | 1 | 64432476d80f14f72c41e882 |
| holder | Gmail, Leonard, subject | 39 | 4 | leonard@harmonygames.co_1771968978585185600.json[0] |
| holder | Gmail, Leonard, body | 511 | 117 | leonard@harmonygames.co_1762499955132850202.json[0] |
| holder | Gmail, all mailboxes, subject | 122 | 8 | 00001199.json[0] |
| holder | Slack, Feb 2026, all channels | 3 | 2 | D07G4S4CVM5/1770743858.267629 |
| holder | Slack, all time, all channels | 622 | 88 | C03201E9A967/1701306369.168409 |
| holder | Linear descriptions | 24 | 5 | ART-629 |
| holder | Docs body | 97 | 32 | f_11040fe5d66821bd6951aa |
| holder | Sheets, any cell | 2 | 2 | f_7b5b5148a0e433d177b559 |
| holder | Slides text | 14 | 1 | f_3dfe41d82ba5b8e8cd04ad |
| holder | Linear project name | 0 | 0 | `NEW TERM — introduced in ec2ea957-fc8e-4958-b809-0fb735b1e916 (project 'Holder records'), reached via C0ADGSZKR3R/1770938120.410229 and linear_list_projects` |
| holder | Gmail subject, word | 0 | 0 | base has 4, all "Key Holders"; `NEW TERM — introduced in leonard.hayes@harmonygames.co/1857034369525983506 only if its subject uses the word, reached via search "Sunset"` |
| stockholder | Gmail, Leonard, body | 7 | 7 | leonard@harmonygames.co_1774892093376420723.json[0] |
| stockholder | Slack, Feb 2026, all channels | 1 | 1 | C0ADGSZKR3R/1770664094.831769 |
| stockholder | Slack, all time, all channels | 3 | 3 | C07C2866011/1764793154.009679 |
| stockholder | Docs body | 55 | 55 | f_0c37bb7235683d73569903 |
| stockholder | Gmail subject | 0 | 0 | `NEW TERM — introduced in leonard.hayes@harmonygames.co/1857034369525983506 if its subject uses the word, reached via search "Sunset"`. 0 subjects in all 88,726 threads today |
| stockholder | Linear | 0 | 0 | `NEW TERM — introduced in ec2ea957-fc8e-4958-b809-0fb735b1e916 if the project description uses the word, reached via linear_list_projects` |
| shareholder (variant) | Gmail, Leonard, body | 136 | 136 | leonard@harmonygames.co_1761203751780760643.json[0] |
| shareholder (variant) | Slack, all time, all channels | 24 | 24 | C04UEQVDVB7/1683316613.322969 |
| shareholder (variant) | Docs body | 15 | 15 | f_1873ca10847a3d3a1b398c |
| shareholder (variant) | Slides text | 2 | 2 | f_94961faf3dd6eda5da1511 |
| Carta | Gmail, Leonard, subject | 108 | 108 | leonard@harmonygames.co_1767340196952308616.json[0] |
| Carta | Gmail, Leonard, body | 436 | 435 | leonard@harmonygames.co_1761645780415075489.json[0] |
| Carta | Gmail, all mailboxes, subject | 201 | 201 | 00000048.json[0] |
| Carta | Slack, Feb 2026, all channels | 9 | 9 | C0ADGSZKR3R/1770838374.556279 |
| Carta | Slack, all time, all channels | 184 | 146 | C03201E9A967/1701276737.315889 |
| Carta | Docs body | 2 | 2 | f_2193d150e5a25bb1e62f7d |
| Carta | Sheets, any cell | 55 | 24 | f_28ecc492b19f3696a19a97 |
| Carta | GCal summary | 4 | 4 | evt_3538f9ae24de3f714fef7d |
| Carta | Trello card name | 4 | 4 | 64dab934b971e3008344527e |
| Carta | Linear | 0 | 0 | `NEW TERM — introduced in ec2ea957-fc8e-4958-b809-0fb735b1e916 ("one issue per holder on Carta, live or lapsed"), reached via linear_list_projects` |
| side letter | Gmail, Leonard, subject | 32 | 32 | leonard@harmonygames.co_1774603492218434534.json[0] |
| side letter | Gmail, Leonard, body | 165 | 165 | leonard@harmonygames.co_1768520517901907516.json[0] |
| side letter | Gmail, all mailboxes, subject | 32 | 32 | leonard@harmonygames.co_1774603492218434534.json[0] |
| side letter | Slack, all time, all channels | 15 | 15 | C04UEQVDVB7/1691688203.809779 |
| side letter | Docs titles | 2 | 2 | f_6201c7027d02997bfb2c84 |
| side letter | Docs body | 4 | 4 | f_2193d150e5a25bb1e62f7d |
| side letter | Drive names | 3 | 3 | f_6201c7027d02997bfb2c84 |
| advisor | Gmail, Leonard, subject | 25 | 24 | leonard@harmonygames.co_1763768315936592373.json[0] |
| advisor | Gmail, Leonard, body | 835 | 503 | leonard@harmonygames.co_1761857065113737556.json[0] |
| advisor | Gmail, all mailboxes, subject | 38 | 32 | 00001078.json[0] |
| advisor | Slack, Feb 2026, all channels | 1 | 1 | D04UC0UEN2V/1770927854.114899 |
| advisor | Slack, all time, all channels | 428 | 313 | C04RSEB8K0W/1680810295.623529 |
| advisor | Docs titles | 5 | 5 | f_3ee38465decc57e61df6e5 |
| advisor | Docs body | 35 | 28 | f_0d17fc08eddaf231cf7f28 |
| advisor | Drive names | 9 | 9 | d_f1af2f5be6c26464c262ff |
| advisor | Sheets, any cell | 9 | 9 | f_36e7af3301c8797ceb4695 |
| advisor | Slides text | 27 | 27 | f_0bd24290a578ac43b94774 |
| advisor | Contacts job | 1 | 1 | db57e559500151d6b3991b62 |
| advisor | Linear | 0 | 0 | `NEW TERM — introduced in comments on ENG-2440, ENG-2446, ENG-2447, ENG-2449 only if a comment uses the word, reached via linear_list_comments` |
| adviser (variant) | Gmail, Leonard, body | 114 | 114 | leonard@harmonygames.co_1775858797096564141.json[0] |
| adviser (variant) | Slack, all time, all channels | 1 | 1 | C04UTBZL6AX/1710127935.352639 |
| adviser (variant) | Docs body | 38 | 38 | f_1873ca10847a3d3a1b398c |
| board | Gmail, Leonard, subject | 279 | 121 | leonard@harmonygames.co_1760406789452391881.json[0] |
| board | Gmail, Leonard, body | 2340 | 825 | leonard@harmonygames.co_1760406789452391881.json[0] |
| board | Gmail, all mailboxes, subject | 790 | 313 | 00000234.json[0] |
| board | Slack, Feb 2026, all channels | 66 | 37 | C09UHHN6PFZ/1770077617.254099 |
| board | Slack, all time, all channels | 9701 | 5673 | C03201E9A967/1701276771.572709 |
| board | Linear titles | 113 | 61 | ART-254 |
| board | Linear descriptions | 269 | 209 | ART-254 |
| board | Docs titles | 17 | 8 | f_093c6e5003d5fdcf84dda6 |
| board | Docs body | 280 | 195 | f_03d2a47737977b13f6b998 |
| board | Drive names | 104 | 16 | d_23beeaeadb5269b81ae933 |
| board | Sheets titles | 18 | 2 | f_ffccfd432e5ca987ac55c6 |
| board | Sheets, any cell | 4726 | 4153 | f_045a7dfe82031d129f64aa |
| board | Slides text | 347 | 76 | f_0281d5b83f931db7fff2be |
| board | GCal summary | 110 | 57 | evt_0befc11b4327d143d27879 |
| board | Trello card name | 31 | 19 | 535af5816ca07f261e8cd433 |
| board | Trello card desc | 10 | 9 | 535af5816ca07f261e8cd437 |
| board | Confluence, any | 90 | 26 | confluence_working.json /pages/1/body |
| equity | Gmail, Leonard, subject | 16 | 15 | leonard@harmonygames.co_1761100012587178460.json[0] |
| equity | Gmail, Leonard, body | 473 | 471 | leonard@harmonygames.co_1761100012587178460.json[0] |
| equity | Gmail, all mailboxes, subject | 64 | 63 | 00000049.json[0] |
| equity | Slack, Feb 2026, all channels | 1 | 1 | C51ECE5102ED/1770903714.600249 |
| equity | Slack, all time, all channels | 409 | 409 | C03201E9A967/1701276737.315889 |
| equity | Docs body | 104 | 104 | f_0402a1a48f31ef00bab354 |
| equity | Drive names | 4 | 4 | d_08e92865de334c505d0fe0 |
| equity | Sheets, any cell | 33 | 33 | f_00c30de5acd0cf7656c140 |
| equity | Slides text | 7 | 7 | f_0421912301531f11c54686 |
| equity | GCal summary | 3 | 3 | evt_931547e2d3ae371bdd3e74 |
| equity | Trello card name | 3 | 3 | 64dab9251f816c6bc4c2aa37 |
| Audit Request | Gmail, Leonard, subject | 9 | 9 | leonard@harmonygames.co_1788910618703813283.json[0] |
| Audit Request | Gmail, Leonard, body | 6 | 6 | leonard@harmonygames.co_1817557789846606177.json[0] |
| Audit Request | Gmail, all mailboxes, subject | 11 | 11 | 00003071.json[0] |
| Audit Request | Gmail subject, FY25 | 0 | 0 | Term is base; the year is new. `NEW TERM — "2025 Audit Request" introduced in leonard.hayes@harmonygames.co/1857029474983245439, reached via search "Audit Request"` |
| Sunset | Gmail, Leonard, subject | 11 | 8 | leonard@harmonygames.co_1856871594497249045.json[0] |
| Sunset | Gmail, Leonard, body | 39 | 27 | leonard@harmonygames.co_1801667999756391798.json[0] |
| Sunset | Gmail, all mailboxes, subject | 27 | 17 | 00001236.json[0] |
| Sunset | Slack, Feb 2026, all channels | 9 | 9 | C07C2866011/1770839105.706739 |
| Sunset | Slack, all time, all channels | 44 | 36 | C04UEQVDVB7/1699572733.860109 |
| Sunset | Docs body | 5 | 4 | f_0c37bb7235683d73569903 |
| Sunset | Sheets, any cell | 99 | 99 | f_079fdbb4907a94f4fbab45 |
| Sunset | Linear | 0 | 0 | `NEW TERM — introduced in ec2ea957-fc8e-4958-b809-0fb735b1e916 ("what Sunset asked for"), reached via linear_list_projects` |
| Sunset | Docs, as the vendor | 0 | 0 | Base has one vendor hit, f_0c37bb7235683d73569903. `NEW TERM — introduced in f_a37b403d5200d4f0a31d31, reached via Drive search on 'close-out notes'` |
| close out (variant) | Gmail, Leonard, body | 23 | 23 | leonard@harmonygames.co_1762112987551929655.json[0] |
| close out (variant) | Slack, Feb 2026, all channels | 2 | 2 | C0ADGSZKR3R/1770664700.848759 |
| close out (variant) | Slack, all time, all channels | 24 | 24 | C04UEQVDVB7/1688045915.318879 |
| closeout (variant) | Gmail, Leonard, body | 10 | 10 | leonard@harmonygames.co_1853470742168514419.json[0] |
| closeout (variant) | Slack, Feb 2026, all channels | 3 | 3 | C0ADGSZKR3R/1770675894.906889 |
| closeout (variant) | Slack, all time, all channels | 4 | 4 | C04RYU8TJ8K/1682729815.055309 |
| Termination details | Gmail, Leonard, subject | 14 | 14 | leonard@harmonygames.co_1808666480668498098.json[0] |
| Termination details | Gmail, all mailboxes, subject | 14 | 14 | leonard@harmonygames.co_1808666480668498098.json[0] |
| close-out | every service scanned | 0 | 0 | `NEW TERM — introduced in f_a37b403d5200d4f0a31d31 and d_601064334a0b493022fe83, reached via ec2ea957-fc8e-4958-b809-0fb735b1e916 ("my close-out notes") and Drive search 'close-out notes'` |

**Slack reach of the locators above.** 24 checked: 23 YES. Not YES: D07G4S4CVM5/1770743858.267629 (NO). These still show the term exists, but Leonard cannot read them.

### Raw hits with no word hit, not rows above

These are noise in the base, and each is 0 for the word. They stay out of the table because no locator would mean anything.

| Term | Service | Raw | What it is |
|---|---|---|---|
| angel | Linear titles | 1 | "Character recommendation behaves strangely." |
| angel | Drive names | 40 | `CHANGELOG.md`, `ChangeLog.txt` and similar file names |
| holder | Linear titles | 4 | "Aspect ratio placeholder" and 3 more placeholders |
| holder | Drive names | 4 | `...KeyHolder.cs.meta` and `PlaceholderFile...` file names |
| holder | GCal summary | 48 | "Placeholder" holds: "Game Day Placeholder", "1583 Form Placeholder" |
| holder | Trello card name | 1 | "notify stakeholders on Carta", closed card `64e3967c4bea2b815c99f59a` |
| advisor | Trello card name | 1 | "Advisory Contracts prep and send them out", real but "Advisory" |
| advisor | Confluence | 1 | "advisable" |
| Sunset | Drive names | 1 | `Chapter_11_SunSet.mp4-info(1).json` |
| Sunset | Slides text | 2 | "Sunsetting Domino Adventures", f_0281d5b83f931db7fff2be and the deck at `/slides_presentations/137` |

### Zero table: 0 raw hits, complete

| Term | Services with 0 raw hits |
|---|---|
| stockholder | Gmail subject (Leonard and all); Linear titles and descriptions; Docs titles; Drive names; Sheets; Slides; GCal; Trello; Contacts; Confluence |
| Carta | Linear titles, descriptions, project names; Docs titles; Drive names; Sheets titles; Slides; Trello desc and comments; Contacts; Confluence. Sheets titles 0 although cells have 24 word hits |
| side letter | Linear; Sheets; Slides; GCal; Trello; Contacts; Confluence |
| equity | Linear; Docs titles; Sheets titles; Slides titles; Trello desc and comments; Contacts; Confluence |
| Audit Request | Slack; Linear; Docs; Drive; Sheets; Slides; GCal; Trello; Contacts; Confluence |
| Sunset | Linear; Docs titles; Sheets titles; Slides titles; GCal; Trello; Contacts; Confluence |
| Termination details | Gmail body; Slack; Linear; Docs; Drive; Sheets; Slides; GCal; Trello; Contacts; Confluence. The 14 subjects are the whole base |
| close-out | all 12 service scopes, including Gmail subject and body and Slack |

Positive controls for the zeros: `Carta` 108 subjects and `stockholder` 55 Docs bodies come from the same scans; `Sunset` hits Gmail subject in `leonard@harmonygames.co_1856871594497249045.json[0]`; `close out` 23 and `closeout` 10 in Gmail bodies show the hyphen is what fails.

### What the counts mean for the seeds

- **`close-out` is the one term that exists nowhere.** H1's planned findability, Drive search 'close-out notes', depends wholly on the seeded name. A word-prefix `gdrive_search` on `close` is not tested here, and I could not run live tools.
- **`Sunset` in Gmail subject is thin and all recent.** Case-sensitive: 10 subjects in Leonard's mailbox, of which 2 are the unrelated "Sunsetting" thread 1840202769203145091 and 8 are Feb 11-12: leonard@harmonygames.co_1856871594497249045.json, 1856872398290956689, 1856953900386127292, 1856954167734410594, 1856956325151717005, 1856956473569789052, 1856956483320787350 (2 messages). A seed with `Sunset` in the subject would rank among these.
- **The Sunset vendor also hides behind tokens.** `[PERSON_NAME_3207]` in 10 Leonard bodies and 4 subjects (2 of them unrelated redactions of the common word), `[USERNAME_26907]` in 7 Slack messages, `[ORGANIZATION_NAME_0453]` in leonard@harmonygames.co_1856675475513544349.json[2]. A literal search misses those. See 1.B.
- **`Audit Request` body hits are quoted subjects.** All 6 are in leonard@harmonygames.co_1817557789846606177.json. The body of the base request says "confirmation request letter" and "KPMG", not "Audit Request".
- **`Termination details` returns the 14 notices in one search,** as §2 says: Gmail subject only, and no body carries the phrase.
- **`holder` in Slack Feb 2026:** the 2 word hits are one message, "the holder of the leg vfx" in D07G4S4CVM5/1770743858.267629, counted as text and block copy. The 1 raw in #winddown is "stockholder", C0ADGSZKR3R/1770664094.831769. So the seeded #winddown burst would be the first real use of the word in that channel.
- **`Audit Request` in the seed subject:** base subjects read `GRIFFIN GAMING PARTNERS 2024 Audit Request [SOURCE_ORG_0001], Inc.`, and 3 of the 7 FY24 messages show `[ORG_NAME_0153] 2024 Audit Request` where Griffin was tokenised. A search for `Griffin` misses those 3, while the word search on `Audit Request` finds all.

## 1.F Collision

Commands: `~/.local/bin/python3.12 -B Task_Authoring/tools/hg.py search lookup <svc> --ids-file <f> --file <glob> [--pointer] [--key]`. A complete pass means `scan_complete` true and `errors` empty. Every line below is that. I ran these today, 2026-11-08; none is carried over from s4.

### Identity tokens first

**Verdict: every speaker and recipient in §11 reuses a token that is already in the base. None needs minting.** Header tokens and body tokens are separate spaces, listed apart.

| Who | Service | Token reused | Proof (`records_checked`, match) |
|---|---|---|---|
| Leonard | Slack | `EMPLOYEE_0038_SLACK_ID` | slack users.json 218, `/23/id` |
| Robert | Slack | `EMPLOYEE_0016_SLACK_ID` | slack users.json 218, `/9/id` |
| Arthur Blake | Slack | `EMPLOYEE_0025_SLACK_ID` | slack users.json 218, `/13/id` |
| Leonard | Linear | `usr_63fffeb4fab5233e` | linear /users 41, `/users/13/id` |
| Robert | Linear | `usr_Robert` | linear /users 41, `/users/26/id` |
| Arthur Blake | Linear | `usr_cc3e90160f490686` | linear /users 41, `/users/35/id` |
| Leonard | Trello | `PERSON_6094_TRELLO_USER_ID` (`fullName` Leonard Hayes) | trello /members 42, `/members/2/id` |
| Leonard | Gmail | `leonard.hayes@harmonygames.co`, header name `leonard hayes` | mailbox; leonard@harmonygames.co_1856872398290956689.json[0] |
| Robert | Gmail | `robert@harmonygames.co`, header name `robert` | leonard@harmonygames.co_1773963101399472184.json[0] |
| KPMG associate | Gmail | `PERSON_3088_NAME <PERSON_3088_EMAIL>` | 3 sent, all leonard@harmonygames.co_1817557789846606177.json [1], [5], [6] |
| KPMG cc | Gmail | `PERSON_4416_NAME <PERSON_4416_EMAIL>` | leonard@harmonygames.co_1788910618703813283.json[1] (from) |
| KPMG cc | Gmail | `PERSON_2322_NAME <PERSON_2322_EMAIL>` | cc only, 0 sent; leonard@harmonygames.co_1817557789846606177.json[6] |
| Griffin VP Finance | Gmail | `PERSON_2847_EMAIL` (bare in FY24 cc), `PERSON_2847_NAME` in a from | leonard@harmonygames.co_1817557789846606177.json[3] |
| Sunset partnerships | Gmail | `PERSON_2888_NAME <PERSON_2888_EMAIL>` | leonard@harmonygames.co_1856872398290956689.json[2] |
| Nebojsa (Robert's To) | Gmail | `PERSON_3941_NAME <PERSON_3941_EMAIL>` | leonard@harmonygames.co_1773963101399472184.json[0] to |
| Bergmann | Contacts | `PERSON_0693_EMAIL`, no row today | contacts /contacts `email` 170, 0 matches; mail use leonard@harmonygames.co_1799418746420547240.json[2] bcc |

Body-text tokens the seeds may need, already in the base, with no minting:

| Person or firm | Body token | Where |
|---|---|---|
| Nebojsa, first name | `[PERSON_NAME_0112]` | leonard@harmonygames.co_1773231301906977143.json[0] "Hi [PERSON_NAME_0112],"; his own sign-off in [5] |
| Nebojsa, surname | `[PERSON_NAME_0127]` | "PERSON_3941_NAME [PERSON_NAME_0127]", leonard@harmonygames.co_1773963101399472184.json[0] |
| Robert | `[PERSON_NAME_0054]`, `[PERSON_NAME_0055]` | leonard@harmonygames.co_1787089404106132003.json[0] subject; Trello card comment `6626aa4770581fe1bb6f5257` |
| KPMG associate | `[PERSON_NAME_46103]` full, `[PERSON_NAME_46106]` first | leonard@harmonygames.co_1817557789846606177.json[1] |
| Sunset | `[PERSON_NAME_3207]` in body and subject; `[USERNAME_26907]` in Slack | leonard@harmonygames.co_1856872398290956689.json[2]; C0ADGSZKR3R/1770934638.035469 |
| Harmony Games | `[SOURCE_ORG_0001]` | every subject above |

**Not a collision but needs a decision: the seed subject word.** PERSON_2888's own subject shows `[PERSON_NAME_3207]: Release of Claims Templates`, and only Leonard's forward shows `Sunset: Release of Claims Templates`. See 1.B.

### Minted ids

**Linear**
```text
lookup linear --file data.json --pointer /issues   (26 ids, ENG-2438..ENG-2463)
  records_checked 3852, field id, scan_complete true, errors [], matches: all 26 = []
lookup linear --file data.json --pointer /projects (ec2ea957-fc8e-4958-b809-0fb735b1e916)
  records_checked 2, field id, scan_complete true, errors [], matches: []
lookup linear --file data.json --pointer /comments (same id)
  records_checked 0, scan_complete true: base has no comments, so no seeded comment id can collide
```
**Drive family** (`d_601064334a0b493022fe83`, `f_a37b403d5200d4f0a31d31`, `f_762c60832854d3e7a7f7df`, `f_5ecaa967db3adcfa440b09`, `f_75dddccabb26eeea4842c8`)
```text
lookup gdrive  --pointer /drive_files                                  records_checked 53866, scan_complete true, errors [], all 5 = []
lookup gdocs   --pointer /docs_documents --key document_id             records_checked 633,   scan_complete true, errors [], all 5 = []
lookup gsheets --pointer /sheets_spreadsheets --key spreadsheet_id     records_checked 398,   scan_complete true, errors [], all 5 = []
lookup gslides --pointer /slides_presentations --key presentation_id   records_checked 164,   scan_complete true, errors [], all 5 = []
search gslides slide_341616bedf43 | slide_659353384faa | el_f71854425943 | el_3f1b82e16a82   0 hits each, scan_complete true
```
**GCal**
```text
lookup gcal --pointer /events --key event_id (evt_6f1a2c9e4b7d3a58c0e1d2)   records_checked 11130, scan_complete true, errors [], matches: []
```
**Trello**
```text
lookup trello --pointer /cards   (698e5a10c3f24b7e9d16a0e4)   records_checked 803,  scan_complete true, errors [], matches: []
lookup trello --pointer /actions (same id)                    records_checked 5294, scan_complete true, errors [], matches: []
```
**Slack (channel, ts) and hash id**
```text
lookup slack --key ts --file 'messages/C0ADGSZKR3R/*.json' (1770938120.410229)  files 1,  records_checked 206,   scan_complete true, errors [], matches: []
lookup slack --key ts --file 'messages/D04UGG61DUM/*.json' (1770949310.220519)  files 36, records_checked 11026, scan_complete true, errors [], matches: []
lookup slack --key ts --file 'messages/*.json' (both ts, every channel)         files 5353, records_checked 687230, scan_complete true, errors [], matches: []
lookup slack --file 'messages/*.json' (d281112d634372d5a8b35fc49a3e4b8c, 617d363f262fd52b9d83c050ce1d3d9c)  files 5353, records_checked 687230, scan_complete true, errors [], matches: []
```
The hashes are `sha256("<channel>|<ts>")[:32]` of the two pairs.

**Gmail**
```text
search-many gmail --file 'threads/*.json' (literal, all scalar values incl. X-GM-THRID headers and ids)
  1857029474983245439   files 88726/88726, scan_complete true, errors [], 0 matches
  1857034369525983506   files 88726/88726, scan_complete true, errors [], 0 matches
  CAGkro_PbX4mT7nQe2LwV9sKd1YhJ3uF6aRc8ZoGi5NtEyMq0Bw   files 88726/88726, scan_complete true, errors [], 0 matches
files gmail 1857029474983245439   total_matching_paths 0
files gmail 1857034369525983506   total_matching_paths 0
lookup gmail --file 'threads/*.json' --pointer /messages
  (leonard.hayes@harmonygames.co/<CAGkro_PbX4mT7nQe2LwV9sKd1YhJ3uF6aRc8ZoGi5NtEyMq0Bw@mail.gmail.com>,
   robert@harmonygames.co/<CAGkro_PbX4mT7nQe2LwV9sKd1YhJ3uF6aRc8ZoGi5NtEyMq0Bw@mail.gmail.com>)
  files 88726, records_checked 104480, scan_complete true, errors [], matches: []
```
`lookup` cannot read `id` at a thread file's root, because the file is one object, not an array, so the thread numbers use the literal scan and the file-name check, which are complete. Positive control: the same scan found `1773963101279916523` 4 times in `threads/00001367.json`, including `/id`.

### Format checks against the 1.A samples

| Id | Rule | Result |
|---|---|---|
| `evt_6f1a2c9e4b7d3a58c0e1d2` | `evt_` + 22 hex | PASS |
| `d_601064334a0b493022fe83` and four `f_` ids | prefix + 22 hex | PASS |
| `ec2ea957-fc8e-4958-b809-0fb735b1e916` | uuid form, as base's two | PASS |
| `1857029474983245439` | `>> 20` = 1771001315100 = 2026-02-13T16:48:35.1Z, root 16:48:33Z, +2.1 s | PASS (1-8 s rule, s4 §B) |
| `1857034369525983506` | `>> 20` = 1771005982900 = 2026-02-13T18:06:22.9Z, root 18:06:21Z, +1.9 s | PASS |
| `CAGkro_PbX4mT7nQe2LwV9sKd1YhJ3uF6aRc8ZoGi5NtEyMq0Bw` | Robert's Gmail shape `CAGkro_` + base64-like, as `<CAGkro_Ox2wP8TQrYO9J2+FkfLbZqy_NixtRjOS7wcBeB3pFZtA@mail.gmail.com>` | PASS |
| C0ADGSZKR3R/1770938120.410229 | = 2026-02-12T23:15:20Z, after the last channel post 1770937460.360699, before 1770977006 | PASS |
| D04UGG61DUM/1770949310.220519 | = 2026-02-13T02:21:50Z, inside the export end | PASS |
| **`698e5a10c3f24b7e9d16a0e4`** | **first 8 hex = 0x698e5a10 = 1770936848 = 2026-02-12T22:54:08Z. §11 dates the card 2026-02-13T02:40:00Z, which is 0x698e8f00. FAIL** | **Mismatch of 3 h 45 m 52 s.** Playbook S4 Trello and `conventions.json trello.ids` both say the prefix is the record's unix seconds |

**Fix for the Trello id, your call.** Either re-date the card to 2026-02-12T22:54:08Z, which is still after Leonard's 22:17:18Z list, or re-mint with prefix `698e8f00` and re-run the lookup. I did not re-mint, since the job names this id.

### Ids §11 needs that are not minted yet

- Message-IDs for the KPMG root and the Sunset mail. §11 gives thread numbers only.
- A thread number and Message-ID for the KPMG follow-up and for Leonard's holding reply. The row estimate counts both, but the §11 table has no row for either.
- A third Slides page and element. §11 says 3 pages; s4 minted 2 pages and 2 elements.
- The second Trello row: the `createCard` action id and the comment action id.
- `ical_uid` for the event; ts for the other burst rows; comment ids; the Contacts row id. §11 says "minted at SQL time" for the last two.

## Not done / could not read

- **No live tool was run.** Search ranking, word-prefix `gdrive_search` on `close-out`, and `gmail_search_messages` tokenising are not tested. 1.D counts are hg.py substring counts, which only approximate those tools.
- **Attachments and PDFs unread by rule:** KPMG confirmation PDFs, signed side letter PDFs in leonard@harmonygames.co_1777052222643175480.json, the Sunset SOW in leonard@harmonygames.co_1856956483320787350.json. Slack images were not read.
- **Could not read one file whole:** threads/frederick@harmonygames.co_1815202866497734438.json overflowed my 300,000-character read. It is Frederick's mailbox, outside Leonard's reach. The complete `to` scan shows no Robert message to Nebojsa in it.
- **Slack counts are not filtered to Leonard's channels.** I checked each Slack locator in 1.D, not each hit: D07G4S4CVM5 is NO.
- **Word counts in 1.D are floors,** as stated there. Hit counts are per scalar value, so Slack block copies and quoted mail count again.
- **Not scanned for keywords:** GitHub and Snowflake. Neither is seeded.
- **`sheets_sheets` count** comes from `conventions.json`, not a recount.
- **Carried over and not re-read:** cells marked "from C2" or "from s2" in 1.B, including the Carta locators for SSP-03, 05, 09, 11, 12 and the ES-8/ES-10 inference.
- **Not minted, so not checked:** the ids listed at the end of 1.F.
- **Slack thread and reply rows:** the two (channel, ts) pairs are the first rows of their bursts; later ts in each burst are not minted.
