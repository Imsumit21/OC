# Write-capability catalog for Claire's Halloween ask

Scope: `Evals/references/tools/catalog.json` (298 tools, names + parameters only),
`Evals/references/tools/manifest.json` (14 exports, 13 services + gateway),
`Evals/references/tools/README.md`, `Evals/references/persona/acl.md`,
`Evals/ENVIRONMENT.md`. Universe synth-cut (Oct 1 2025 clock), persona Claire Morgan
(`claire.morgan@harmonygames.co`, Art Lead).

Parent ask: Leonard's seeded Slack message `C06DJBJL798/1759269913.882683` in
#zombie_marketing. Deliverables a–f are (a) plan doc, (b) tracker sheet, (c) one
comment per ad's ART ticket with Halloween call + due date, (d) assign the ad to its
maker, (e) new ART tickets for the Halloween icon and Halloween iPad set, (f) reply
in Leonard's thread with the links before Thu Oct 2.

Read this with the two limits the export states about itself:

- The export declares **names, parameter types and required/optional status only**.
  No descriptions, no output schemas, no nested-object definitions, no enums.
- `manifest.json` says `"runtime_verified": false`. Nothing in **this task's**
  inputs records an observed write. The only workspace precedent is an older
  task's report
  (`Evals/task_inputs/reports/drafts/prompt_history/1_prompt-*.md`, "Write paths,
  tabs, channel, card … VERIFIED, no fail"), which marks `gsheets_values_update`,
  `linear_create_issue`, `gmail_send_message`, `slack_conversations_add_message`
  and `trello_add_comment` as exercised — but that is a different universe and a
  different workbook, and it says nothing about `gdrive_share_file` or `dueDate`,
  for which no recorded call exists anywhere in `Evals/`. So **SUPPORTED** below
  means "the catalog declares a parameter that can express it", not "a run has
  proved it on this data". Anything that depends on a value the catalog does not
  enumerate is marked UNVERIFIED even when a tool exists.

Persona write access is not the constraint: `Evals/references/persona/acl.md`
("Persona ACL does not govern writes") and the QC Rating Form V12 note both say
writes are not blocked by ACL. Claire's reach (`01_Grounding_Dossier.md` §1.B) is
Slack, Linear, Gmail (incl. the `claire@` file alias), GCal and the Drive family.

---

## 0. MCP servers

**None.** `catalog.json` and `manifest.json` contain no server field and no
`mcp` token (`grep -c mcp` on both = 0); the sole `get_time` tool is the gateway
export. `Evals/references/tools/README.md` states local search runs through
`Evals/tools/hg_search.py`, "not MCP". There is therefore **no MCP server name a
prompt could leak**, and no `mcp__*` naming convention applies to this task.

---

## 1. Deliverable (a) — plan doc Claire owns, shared so the team can comment

| Step | Tool | Parameters (verbatim) | Status |
|---|---|---|---|
| Create the doc with its text | `gdocs_create_document` | `title` **required** (string); `bodyText` optional (string \| null); `driveFileId` optional (string \| null) | **SUPPORTED** — `bodyText` is a declared optional, so create-with-content is a single call. Whether `bodyText` accepts markdown/plain text and how headings land is **not** declared. |
| Later edits / formatting | `gdocs_batch_update` | `documentId` **required**; `requests` **required** (array) | **SUPPORTED** for the call; the request objects are Google Docs `batchUpdate` shapes (insertText, updateTextStyle, …) and the export declares no nesting, so any specific request body is **UNVERIFIED**. |
| Put it in a folder | `gdrive_move_file` | `fileId` **required**; `newParentId` **required**; `oldParentId` optional (string \| null) | **SUPPORTED** — needed because `gdocs_create_document` has **no** parent/folder parameter; it lands in the acting user's My Drive root. |
| Share so the team can comment | `gdrive_share_file` | `fileId` **required**; `emailAddress` optional (string \| null); `role` optional (string); `type` optional (string); `domain` optional (string \| null) | **UNVERIFIED** — the parameters exist but the catalog enumerates no values for `role` or `type`. Google's API uses `role: "commenter"` with `type: "user"` (per person) or `type: "domain"` + `domain` (whole org). Neither value nor the `type` vocabulary is declared or observed here. **`role: "reader"` does not allow commenting.** |
| Rename / set description | `gdrive_update_file_metadata` | `fileId` **required**; `name` optional; `description` optional; `starred` optional | SUPPORTED (declared). |
| Verify | `gdocs_get_document_text` | `documentId` **required** | SUPPORTED. |

Notes and risks:

- **There is no Google Docs comment tool.** The gdocs set is exactly
  create / delete / get / get_text / search / batch_update / health. "Shared so the
  team can comment" is a *permission* statement; the comments themselves happen in
  the Doc UI and are out of the agent's surface. A prompt must not ask the agent to
  "comment on the doc" or to read doc comments.
- `gdocs_create_document` does not declare what it returns. If the run must then
  share or move it, the id has to come from the create response or from
  `gdocs_search_documents` (`query`, `fullText`, `pageSize`, `pageToken`). Treat
  "create → share" chaining as UNVERIFIED at the output-shape level even though
  both tools exist.
- Alternative single call: `gdrive_create_file` (`name` **required**, `content`
  **required**, `mimeType` optional, `parentId` optional, `driveMimeType` optional
  (string \| null), `description` optional). It *can* carry initial content and a
  parent in one call, and `driveMimeType` is the only field that could plausibly
  convert the upload into a native Google Doc. Whether that conversion works is
  **UNVERIFIED**; prefer `gdocs_create_document` for a doc the team must comment on.

## 2. Deliverable (b) — tracker Google Sheet Claire owns, shared

| Step | Tool | Parameters (verbatim) | Status |
|---|---|---|---|
| Create the spreadsheet | `gsheets_create_spreadsheet` | `title` **required**; `initialSheetTitle` optional (string); `driveFileId` optional (string \| null) | **SUPPORTED** (no folder parameter — same My-Drive-root note as above). |
| Write the header + rows | `gsheets_values_update` | `spreadsheetId` **required**; `range` **required** (string); `values` **required** (array) | **SUPPORTED**. No `valueInputOption` / `majorDimension` is declared, so whether strings land RAW or USER_ENTERED (and whether `2025-10-15` becomes a date) is **UNVERIFIED** — keep graded values as text in the sheet and let the rubric read the cell text. |
| Append instead of overwrite | `gsheets_values_append` | `spreadsheetId` **required**; `range` **required**; `values` **required** (array) | SUPPORTED (declared). |
| Tabs, formats, widths | `gsheets_batch_update` | `spreadsheetId` **required**; `requests` **required** (array) | SUPPORTED for the call; request nesting **UNVERIFIED**. |
| Share | `gdrive_share_file` | as above | **UNVERIFIED** (role/type enums). |
| Verify | `gsheets_values_get` / `gsheets_values_batch_get` / `gsheets_get_spreadsheet` / `gdrive_read_sheet_range` / `gdrive_list_sheets` | `spreadsheetId`+`range`; `spreadsheetId`+`ranges`; `spreadsheetId`+`includeGridData`; `spreadsheetId`+`sheetIndex` | SUPPORTED. |

`01_Grounding_Dossier.md` §write-paths and `01_Scenario_Design.md` both assume
`gsheets_values_update` for this write and 2 `gdrive_share_file` calls total (doc +
sheet), one per file.

## 3. Deliverable (c) — one comment per ad's ART ticket (call, due date)

| Step | Tool | Parameters (verbatim) | Status |
|---|---|---|---|
| Add the call to one ticket | `linear_create_comment` | `issueId` **required** (string); `body` **required** (string); `parentId` optional (string \| null) | **SUPPORTED**, one issue per call. `issueId` type is a bare string; the seeded tickets carry `ART-793`-style ids, so the key is the identifier, not a uuid (matches `01_Grounding_Dossier.md` §1.A "linear /issues (id)"). |
| Read existing comments | `linear_list_comments` | `issueId` **required**; `limit` optional (integer); `cursor` optional (string \| null) | SUPPORTED — no bulk/list-all endpoint, so coverage is per ticket. |
| Read the ticket | `linear_get_issue` | `id` **required**; `maxDescriptionChars` optional (integer \| null) | SUPPORTED. |
| Finder | `linear_list_issues` / `linear_submit_list_issues` | `query`, `team`, `project`, `assignee`, `parentId`, `state`, `label`, `cycle`, `includeArchived`, `orderBy`, `limit`, `cursor`, `createdAt`, `updatedAt`, `maxDescriptionChars` | SUPPORTED; `team` + `query` is how the ART catalogue is enumerated. |

**No bulk comment tool exists.** `linear_create_comment` takes exactly one
`issueId`; there is no `issueIds` array and no batch-comment endpoint anywhere in
the 298 tools. 58 serving ads ⇒ 58 separate calls (plus updates and issue
creates). `01_Scenario_Design.md` row 20 already treats this as the reason the
run's floor is ~192 calls.

**Due date.** If a due date must be a *field* (not prose in the comment), it is
`linear_update_issue.dueDate` — see §5. Writing it as text inside the comment body
is always SUPPORTED and is the safer graded surface, because the field's date
format is not declared.

## 4. Deliverable (d) — assign the ad to its maker

| Step | Tool | Parameters (verbatim) | Status |
|---|---|---|---|
| Set the assignee | `linear_update_issue` | `id` **required** (string); `title`, `description`, `assignee`, `project`, `parentId`, `priority`, `state`, `dueDate`, `estimate`, `cycle`, `labels`, `links` all optional | **SUPPORTED** for `assignee` as the design's `usr_c77c50cc15c5342d` / `usr_51f5f16d46e8cf55` ids. |
| Resolve a maker to an id | `linear_get_user` (`query` **required**) / `linear_list_users` (`query`, `team`, `includeDisabled`, `orderBy`, `limit`, `cursor`) | as listed | SUPPORTED — this is the declared route from a name to a `usr_…` id, and it also surfaces the decoys (three Marcuses; `usr_Robert` is not `usr_16hex`). |
| Read back | `linear_get_issue` (`id`) | | SUPPORTED. |

`assignee` is typed `string | null` with **no** enum or description. See §7
question 2 for whether a name/email is accepted.

## 5. Deliverable (e) — new ART tickets (Halloween icon, Halloween iPad set)

| Tool | Parameters (verbatim) | Status |
|---|---|---|
| `linear_create_issue` | `team` **required** (string); `title` **required** (string); `description` optional (string \| null); `assignee` optional (string \| null); `project` optional; `parentId` optional; `priority` optional (integer); `state` optional (string \| null); `dueDate` optional (string \| null); `cycle` optional; `labels` optional (array \| null); `links` optional (array \| null) | **SUPPORTED** — `team` = ART (the team key/name; `linear_get_team`/`linear_list_teams` take `query` to confirm it), `assignee` = Martin's `usr_51f5f16d46e8cf55` (icon, stills — dossier §1.B), `dueDate` available. `labels` element shape (names vs ids) is **UNVERIFIED**; a prompt should not require labels. |

## 6. Deliverable (f) — reply in Leonard's #zombie_marketing thread

| Step | Tool | Parameters (verbatim) | Status |
|---|---|---|---|
| Reply in the thread | `slack_send_message` | `channel` **required** (string); `text` **required** (string); `thread_ts` optional (string \| null); `user` optional (string \| null) | **SUPPORTED** — `thread_ts` is the thread parent ts (`1759269913.882683`), `channel` the channel id (`C06DJBJL798`). |
| Alternate reply path | `slack_conversations_add_message` | `channel_id` **required**; `payload` **required** (string); `content_type` optional (string); `thread_ts` optional (string \| null); `user_id` optional (string \| null) | Tool exists; **UNVERIFIED** in substance — the body goes in a `payload` string whose JSON shape and `content_type` vocabulary are undeclared. Prefer `slack_send_message`. |
| Read the thread first | `slack_read_thread` (`channel`, `thread_ts`, `limit`, `cursor`, `include_activity_messages`) / `slack_conversations_replies` (`channel_id`, `thread_ts`, …) | as listed | SUPPORTED. |
| Scheduler (not needed) | `slack_schedule_message` | `channel` **required**; `text` **required**; `post_at` **required** (integer); `user` optional; `thread_ts` optional | Exists; would only fit if the reply had to be deferred. |

`channel` for both Slack writers is a bare string with no declared
id-vs-name rule; the design and dossier both use the id, so a prompt should give
the channel by name and let the run resolve it. Note `C06DJBJL798` is a **private**
channel (`01_Grounding_Dossier.md` §1.A) and Claire is a member (dossier Check A),
so posting is in-bounds; a private channel does mean `slack_search_public` will not
find the thread — `slack_read_thread` on the known ts is the route.

## 7. The four direct questions

1. **Can Claire set a Linear due date on an existing issue?** Yes —
   `linear_update_issue` declares `dueDate` (optional, `string | null`) alongside
   `id`. No format is declared and no run has exercised it, so treat the *field*
   write as SUPPORTED-but-untested and the *comment text* as the reliable carrier.
2. **Does `linear_update_issue` take an assignee by name/email or by id?**
   It takes `assignee` as an opaque `string | null`; the catalog does not say
   which. The workspace's own design pins the `usr_…` ids, and `linear_list_users`/
   `linear_get_user` exist to resolve a person to that id — so **by id is the
   verified-by-shape route; name/email acceptance is UNVERIFIED**. (Cross-env
   rubric text in `Evals/references/rules/rubric_qc_cases.json` tolerates an email
   or `"me"` for a Linear-family `save_issue`, and another case checks a
   `user_…` id — both belong to a different property-management environment, so
   they are precedent, not proof.)
3. **Is there a bulk comment tool?** No. `linear_create_comment(issueId, body,
   parentId)` is single-issue; no `issueIds` parameter exists on any Linear tool,
   and no other service can write Linear comments.
4. **Is there a Drive tool that creates a doc with initial content in one call?**
   Yes, two candidates: `gdocs_create_document(title, bodyText)` — declared and
   preferred; and `gdrive_create_file(name, content, …, driveMimeType)` — a
   generic upload that may or may not yield a native Doc (UNVERIFIED). Neither
   takes a folder, so a folder placement is a separate `gdrive_move_file`.

---

## 8. Vocabulary the prompt must never use

Rule: a HarmonyGames prompt describes the work, not the API. Never name a tool,
never name a parameter, never say "call"/"endpoint"/"MCP". Service and product
names are fine ("Slack", "Linear", "Google Doc", "sheet", "thread", "ticket",
"assignee", "due date"); tool names and camel_case/snake_case parameter names are
not. `manifest.json` exposes 298 tool names across 13 services, all of which are
off-limits, including the read-only ones (naming a read tool tells the agent which
route to take).

### 8.1 Tool names by service (all forbidden)

- **slack (32):** `slack_add_reaction, slack_channels_list, slack_conversations_add_message, slack_conversations_edit_message, slack_conversations_history, slack_conversations_replies, slack_conversations_search_messages, slack_create_conversation, slack_get_conversation, slack_get_job_result, slack_get_job_status, slack_get_message_metadata, slack_get_reactions, slack_health, slack_list_channel_members, slack_list_drafts, slack_list_files, slack_list_scheduled_messages, slack_read_channel, slack_read_file, slack_read_thread, slack_read_user_profile, slack_remove_reaction, slack_schedule_message, slack_search_channels, slack_search_emojis, slack_search_public, slack_search_public_and_private, slack_search_users, slack_send_message, slack_send_message_draft, slack_submit_search`
- **gmail (33):** `gmail_archive_thread, gmail_batch_modify_message_labels, gmail_create_draft, gmail_create_label, gmail_delete_draft, gmail_delete_label, gmail_delete_message, gmail_delete_thread, gmail_get_attachment, gmail_get_job_result, gmail_get_job_status, gmail_get_label, gmail_get_message, gmail_get_messages_batch, gmail_get_profile, gmail_get_thread, gmail_health, gmail_list_drafts, gmail_list_labels, gmail_list_messages, gmail_list_threads, gmail_list_users, gmail_modify_message_labels, gmail_modify_thread_labels, gmail_reply_to_message, gmail_search_messages, gmail_send_draft, gmail_send_message, gmail_submit_search_messages, gmail_trash_message, gmail_trash_thread, gmail_untrash_message, gmail_untrash_thread`
- **gcal (12):** `gcal_create_event, gcal_delete_event, gcal_freebusy_query, gcal_get_calendar, gcal_get_event, gcal_health, gcal_list_calendars, gcal_list_events, gcal_patch_event, gcal_respond_to_event, gcal_search_events, gcal_update_event`
- **gdrive (21):** `gdrive_create_file, gdrive_create_folder, gdrive_delete_file, gdrive_get_file_metadata, gdrive_get_file_path, gdrive_get_job_result, gdrive_get_job_status, gdrive_health, gdrive_list_folder, gdrive_list_recent_files, gdrive_list_sheets, gdrive_move_file, gdrive_read_file, gdrive_read_sheet_range, gdrive_restore_from_trash, gdrive_search, gdrive_share_file, gdrive_submit_search, gdrive_trash_file, gdrive_update_file_content, gdrive_update_file_metadata`
- **gdocs (7):** `gdocs_batch_update, gdocs_create_document, gdocs_delete_document, gdocs_get_document, gdocs_get_document_text, gdocs_health, gdocs_search_documents`
- **gsheets (10):** `gsheets_batch_update, gsheets_create_spreadsheet, gsheets_delete_spreadsheet, gsheets_get_spreadsheet, gsheets_health, gsheets_search_spreadsheets, gsheets_values_append, gsheets_values_batch_get, gsheets_values_get, gsheets_values_update`
- **gslides (8):** `gslides_batch_update, gslides_create_presentation, gslides_delete_presentation, gslides_get_page, gslides_get_presentation, gslides_get_presentation_text, gslides_health, gslides_search_presentations`
- **linear (28):** `linear_create_comment, linear_create_issue, linear_create_project, linear_create_team, linear_create_user, linear_delete_issue, linear_delete_project, linear_get_attachment, linear_get_attachments, linear_get_issue, linear_get_job_result, linear_get_job_status, linear_get_project, linear_get_team, linear_get_user, linear_health, linear_list_comments, linear_list_cycles, linear_list_issue_labels, linear_list_issue_statuses, linear_list_issues, linear_list_projects, linear_list_teams, linear_list_users, linear_show_data, linear_submit_list_issues, linear_update_issue, linear_update_project`
- **trello (41):** `trello_add_comment, trello_add_label_to_card, trello_add_member_to_card, trello_archive_card, trello_archive_list, trello_create_board, trello_create_card, trello_create_check_item, trello_create_checklist, trello_create_label, trello_create_list, trello_delete_board, trello_delete_card, trello_delete_list, trello_get_attachment, trello_get_attachments, trello_get_board, trello_get_board_actions, trello_get_board_members, trello_get_card, trello_get_card_actions, trello_get_cards_in_list, trello_get_cards_on_board, trello_get_checklist, trello_get_checklists_on_board, trello_get_comments, trello_get_job_result, trello_get_job_status, trello_get_labels_on_board, trello_get_lists, trello_get_member, trello_get_member_cards, trello_health, trello_list_boards, trello_move_card, trello_search, trello_submit_search, trello_update_board, trello_update_card, trello_update_check_item, trello_update_list`
- **contacts (9):** `contacts_add_new_contact, contacts_delete_contact, contacts_edit_contact, contacts_get_contact, contacts_get_contacts, contacts_get_current_user_details, contacts_health, contacts_search_contacts, contacts_show_data`
- **github (57):** `github_add_issue_comment, github_add_reply_to_pull_request_comment, github_compare_commits, github_create_branch, github_create_issue, github_create_label, github_create_or_update_file, github_create_pull_request, github_create_pull_request_review, github_delete_branch, github_delete_file, github_delete_label, github_get_blame, github_get_commit, github_get_commit_files, github_get_file_contents, github_get_file_history, github_get_issue, github_get_issue_comments, github_get_job_result, github_get_job_status, github_get_label, github_get_latest_release, github_get_me, github_get_pull_request, github_get_pull_request_comments, github_get_pull_request_commits, github_get_pull_request_files, github_get_pull_request_reviews, github_get_pull_request_status, github_get_pull_request_timeline, github_get_release_by_tag, github_get_repository, github_get_repository_tree, github_get_tag, github_get_user, github_health, github_list_branches, github_list_commits, github_list_issues, github_list_labels, github_list_pull_requests, github_list_releases, github_list_repository_collaborators, github_list_tags, github_merge_pull_request, github_push_files, github_search_code, github_search_commits, github_search_issues, github_search_pull_requests, github_search_repositories, github_search_users, github_submit_search_code, github_update_issue, github_update_label, github_update_pull_request`
- **confluence (29):** `confluence_add_comment, confluence_add_label, confluence_create_page, confluence_create_space, confluence_delete_comment, confluence_delete_page, confluence_get_current_user, confluence_get_job_result, confluence_get_job_status, confluence_get_page, confluence_get_page_children, confluence_get_page_diff, confluence_get_page_history, confluence_get_page_version, confluence_get_space, confluence_get_user, confluence_health, confluence_list_attachments, confluence_list_comments, confluence_list_labels, confluence_list_pages, confluence_list_spaces, confluence_list_users, confluence_restore_page_version, confluence_search, confluence_search_user, confluence_submit_search, confluence_update_comment, confluence_update_page`
- **snowflake (10):** `snowflake_describe_table, snowflake_execute_query, snowflake_get_job_result, snowflake_get_job_status, snowflake_health, snowflake_list_databases, snowflake_list_schemas, snowflake_list_tables, snowflake_query_history, snowflake_submit_query`
- **gateway (1):** `get_time` (present in the export, never called by the evaluator).

### 8.2 Distinctive parameter names by service (all forbidden)

- **slack:** `channel, channel_id, channel_types, content_type, creator, cursor, exclude_archived, file_id, filter_date_after, filter_date_before, filter_date_during, filter_date_on, filter_in_channel, filter_in_im_or_mpim, filter_threads_only, filter_users_from, filter_users_with, include_activity_messages, include_private, is_im, is_private, job_id, limit, max_bytes, message_ts, name, new_ts, payload, post_at, query, search_query, shift_subsequent, sort, text, thread_ts, ts, user, user_id, user_ids`
- **gmail:** `add_label_ids, attachment_id, background_color, bcc, body, cc, draft_id, format, include_spam_trash, job_id, label_id, label_ids, label_list_visibility, limit, max_results, message_id, message_ids, message_list_visibility, name, offset, page_token, query, remove_label_ids, reply_all, subject, text_color, thread_id, to, user_email`
- **gcal:** `attendeeEmail, calendarId, calendarIds, comment, event, eventId, hardDelete, maxResults, pageToken, patch, q, responseStatus, showDeleted, singleEvents, timeMax, timeMin`
- **gdrive:** `content, description, domain, driveMimeType, emailAddress, exportMimeType, fileId, folderId, fullText, includeTrashed, job_id, length, limit, mimeType, modifiedAfter, modifiedBefore, name, newParentId, offset, oldParentId, pageSize, pageToken, parentId, query, role, sheetIndex, spreadsheetId, starred, type`
- **gdocs:** `bodyText, documentId, driveFileId, fullText, pageSize, pageToken, query, requests, title`
- **gsheets:** `driveFileId, includeGridData, initialSheetTitle, pageSize, pageToken, query, range, ranges, requests, spreadsheetId, title, values`
- **gslides:** `driveFileId, pageObjectId, pageSize, pageToken, presentationId, query, requests, title`
- **linear:** `assignee, attachmentId, body, createdAt, cursor, cycle, description, dueDate, email, estimate, id, includeArchived, includeDisabled, issueId, job_id, key, label, labels, lead, limit, links, maxDescriptionChars, member, name, orderBy, parentId, priority, project, query, startDate, state, summary, targetDate, team, title, updatedAt`
- **trello:** `attachmentId, before, boardId, boards_limit, cardId, cards_filter, cards_limit, checkItemId, checked, checklistId, closed, color, desc, due, dueComplete, filter, idBoard, idBoards, idCard, idLabels, idList, idMembers, idOrganization, job_id, labelId, limit, listId, memberId, modelTypes, name, offset, organizationId, pos, query, since, state, text`
- **contacts:** `address, age, city_living, contact_id, country, cursor, description, email, first_name, gender, job, last_name, limit, nationality, phone, query, status, updates`
- **github:** `assignees, author, base, body, branch, color, commentId, commit_message, commit_title, content, description, direction, draft, event, files, follow_renames, from_branch, head, include_patch, issue_number, job_id, labels, limit, merge_method, message, name, new_name, offset, order, owner, page, path, perPage, pullNumber, query, recursive, ref, repo, sha, since, sort, state, tag, title, tree_sha, until, username`
- **confluence:** `authorId, body, bodyFormat, comment_id, cql, description, from_version, includeArchived, job_id, key, label, limit, name, offset, page_id, parentId, prefix, query, space, status, text, title, to_version, type, version`
- **snowflake:** `database, job_id, limit, offset, schema, sql, table`

(Verbatim, de-duplicated per service from `Evals/references/tools/catalog.json`.)

### 8.3 Phrasing the prompt can safely use

Safe: "a plan document you own", "a tracker sheet", "share it so the team can
comment", "leave a comment on each ad's ticket with its call and the date it's
due", "assign it to whoever is making it", "open two tickets on the art team",
"reply in my thread", "drop the links in the thread", "before Thursday's review",
ticket keys (`ART-793`), people by name, channel name `#zombie_marketing`, the
date, and the two maker names.

Unsafe: any `gdocs_*`/`gsheets_*`/`linear_*`/`slack_*`/`gdrive_*` name; any of the
parameter names above; "`commenter`", "`type: user`", "`thread_ts`", "`issueId`",
"`spreadsheetId`", "`documentId`", "`dueDate`", "`assignee`", "`bodyText`",
"`values`", "MCP", "tool", "endpoint", "batch update", "call the API".
Also avoid requiring a shared Drive **folder**, a Linear **label**, a **project**,
or a **state** name — none of those is needed by the ask and each adds an
unverified enum.

---

## 9. Residual capability risks for the prompt writer

1. **Share role.** "Shared so they can comment" needs `role: commenter`; the enum
   is undeclared. Do not let a rubric require the literal role string or a
   specific `type`; grade that each file is shared with the review attendees
   (or the team) and readable by them, whichever route the run takes.
2. **Document output shape.** `gdocs_create_document` declares no return, so
   "create then share/move" needs the id from the response or a follow-up search.
   Do not require a specific folder placement unless a folder id is reachable.
3. **Sheet value typing.** No `valueInputOption`; date-like cells may normalise.
   Keep the graded calls and due dates as unambiguous text.
4. **No doc comments, no bulk comments, no comments on sheets.** The graded
   surface for (c) must be Linear ticket comments, one per ad.
5. **Deadline source is a calendar read**, not a write: the Oct 2 review event
   (`evt_d947bf7cd910549b674b1f`, 16:00–16:30Z) is already on Claire's calendar
   copy; no `gcal_*` write is part of this ask.
6. **Volume is inherent.** 58 serving ads ⇒ ≥ 58 `linear_create_comment` calls,
   plus `linear_update_issue` per assignment and 2 `linear_create_issue`; the
   catalog offers no shortcut, which is why the ask is expensive rather than wide.
