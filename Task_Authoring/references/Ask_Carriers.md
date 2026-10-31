# Ask & Evidence Carriers — all 13 HarmonyGames services

> Where an ask, rule or fact can be injected, how the agent's tools surface it, what a per-item read costs, which bulk calls collapse volume, and exact-column SQL skeletons. Produced 2026-10-03 by a full read of the schema (updated to the live 144-table platform export on 2026-10-04 — §0a), the 298-tool catalog and every service export. Used by `playbooks/01_Scenario_Design.md` and `playbooks/01_Universe_Injection.md`; summarised in `Hardness_Mastery.md` §2 and §5.
> Compiled from the older Feb 14 export; reference-only for both universes until re-verified against the selected universe. Lines tagged [normal-only] do not exist on Oct 1 (synth-cut). Read the selected universe's records before mirroring any shape, count or ID here.
> **Rule of precedence:** put load-bearing facts only in carriers marked ● (base-data precedent). ○ carriers (no base rows, or unverified rendering) may hold supporting detail; confirm their rendering in the Opus pre-check trajectory before a criterion depends on them.

**Labels used throughout:**
- **[V]** I checked it against the real exports, the schema or the catalog.
- **[C]** The catalog shows only the tool name and its parameters. It has no descriptions, defaults or output schemas.
- **[U]** Unverified or inferred. Confirm it before relying on it. Section 7 gives a SELECT to run in Universe Explorer for each one.

**Workspace root:** the folder that holds `Evals/`, `claude/`, `Task_Authoring/` and the selected universe's folder (`Universe_Normal/Normal_HarmonyGames_*` for Feb 14, 2026; `Universe_SynthCut/SynthCut_HarmonyGames_*` for Oct 1, 2025). Below, `<U>/<P>_HarmonyGames_*` means that universe folder and prefix (`Universe_Normal/Normal_…` or `Universe_SynthCut/SynthCut_…`).

**Sources read:**
- `Task_Authoring/references/universe_schema_live.json` (144 tables, platform export 2026-10-04 — the only schema of record; new NOT NULL columns without defaults: `linear_projects.links_json`, `linear_users.is_admin`, `linear_users.is_guest`; never write the generated `*_fts` columns)
- `Evals/references/schema/{injection.json, snowflake.json, README.md}`
- `Evals/references/tools/catalog.json` (298 tools)
- `Evals/references/universes/<normal|synthcut>/{source_layout.json, universe_manifest.json}` (for the selected universe)
- `Evals/SEARCH.md`
- `Evals/references/persona/acl.md`
- `Evals/references/rules/hardness_calibration.md` (the only recorded run evidence about tool behaviour)
- `Task_Authoring/references/{Native_Artifact_Anatomy.md, persona_roster_v2.json, Docs/03,04,09,12, Taxonomy_V2_Step_Map.md}`
- `Task_Authoring/tools/{sql_lint.py, hardness_gate.py}`
- Every service export: streamed, sharded or loaded according to size. Snowflake was read by byte range using `Evals/references/universes/<normal|synthcut>/search_indexes/snowflake-snowflake.json`. Gsheets was stream-decoded.

---

## 0. Ten things the engine must know first

1. **Only four columns in all 144 tables have defaults** [V, live export]: `public._changelog.id` (nextval) and `.timestamp` (now()), `linear.linear_projects.color`, and `slack.slack_scheduled_messages.reply_broadcast` (false). Every other NOT NULL column must be given a literal value.

2. **Some IDs can be derived exactly** [V]:
   - **Slack message `id`** = `sha256(channel_id + "|" + ts).hexdigest()[:32]`. This held for 29,947 of 29,948 sampled messages.
   - **Trello `id`** is a 24-hex ObjectId whose first 8 hex digits are the creation time in Unix seconds. This held for 5,245 of 5,294 actions; the exceptions are Welcome-Board template rows. Mint Trello IDs from the record's own timestamp.

3. **Slack thread replies are invisible to channel history** [V, run evidence]. `slack_read_channel` returns thread parents only (hardness_calibration.md, run call 20: 50 messages, zero replies). The observed page ceiling is about 50 messages. A 100-message read overflowed at 71,224 characters and spilled to a file.

4. **Base data has zero rows in several carrier tables** [V]: Linear comments, GitHub issues, tags and releases, gcal event `description`/`location`, slides `notes`, contacts `description`, slack `files.content_inline`/`preview`, and `drive_files.content_text`, which is not even exported. Injecting into these creates carriers that have no precedent in the base data. That is both a realism risk and an unverified-rendering risk.

5. **Storage is one copy per reader** [V]:
   - **Gmail:** one row per mailbox. Each copy has its own `<mailbox>/<RFC-id>` message ID and its own `<mailbox>/<19-digit>` thread ID.
   - **GCal:** one event row per attendee calendar, with `self: true` on the calendar owner (11,233 of 11,233).
   - A persona can only see a copy whose `user_email` or `calendar_id` is the persona.

6. **The Google trio mirrors Drive** [V]. The Docs, Sheets and Slides ID equals the `gdrive.drive_files.id` (`f_`+22 hex), and the sharing fields are identical (633 of 633 docs). Files use `f_`, folders use `d_`. Native_Artifact_Anatomy wrongly says Drive files use `d_`.

7. **Snowflake data lives in `snowflake.wh_<db>__<schema>__<table>`**, with UPPERCASE column names that must be double-quoted [V]. Export rows use lowercase keys, so do not copy keys from the export.

8. **Postgres quoting:**
   - Reserved words that must be quoted: `"references"` (gmail), `"primary"` (gcal), `"desc"` (trello).
   - All Trello camelCase columns must be quoted (`"idBoard"`, `"idList"`, `"dateLastActivity"`, `"idMemberCreator"`, `"idShort"`, `"idMembers_json"`, …).
   - All Snowflake `wh_` columns must be quoted.

9. **Some personas are unreachable without injection** [V]:
   - **Tim Steudler** (`UBF5AB53C96`) belongs to 0 Slack channels, has no Gmail mailbox and has no Drive root.
   - *Not a reach gap, but a lookalike trap:* **Marcus Bennett** has his own mailbox `marcus.bennett@harmonygames.co`. Marcus Lee (`marcus.lee@harmonygames.co`) and a mononym Trello member "Marcus" (`c48a210d5c5a4b59231c6873`) share his first name, and `marcus@harmonygames.co` does not exist in either universe.
   - **Simon Walker** has no Drive root folder.

10. **The catalog has no pagination defaults** [C]. The only measured limit is the Slack page of about 50. The async `*_submit_*` → `*_get_job_status` → `*_get_job_result` pattern costs at least 3 calls, and when a wait is configured the instant search tool is disabled.

---

## 0a. Live schema additions (platform export 2026-10-04)

The per-service table lists below were first written from an older 128-table snapshot. The
live schema (`references/universe_schema_live.json`, 144 tables) **adds** the following; nothing
was dropped or retyped. `!` = NOT NULL without a default (must be supplied on INSERT).

**New tables (16):**
- `contacts.contact_group_members`: membership_id!, group_id!, contact_id!
- `contacts.contact_groups`: group_id!, name!, owner_email, created_at, updated_at
- `gcal.gcal_acl_rules`: calendar_id!, rule_id!, scope_type!, scope_value!, role!
- `gcal.gcal_calendar_list`: user_email!, calendar_id!, deleted, color_id, hidden, selected, summary_override, default_reminders_json, notification_settings_json
- `github.github_check_runs`: id!, repo_id!, head_sha!, name!, status!, conclusion, started_at, completed_at, details_url, external_id, output_title, output_summary, output_text, app_slug, seq, sim_duration_seconds, sim_conclusion
- `github.github_ci`: id!, repo_id!, name!, duration_seconds!, conclusion!, position
- `github.github_commit_statuses`: id!, repo_id!, sha!, state!, context!, description, target_url, creator_login, created_at, updated_at, seq
- `github.github_issue_types`: id!, org!, node_id, name!, description, color, is_enabled, created_at, updated_at, seq
- `github.github_reactions`: id!, subject_type!, subject_id!, content!, user_login, created_at
- `github.github_teams`: id!, org!, name!, slug!, description, member_logins_json, seq
- `linear.linear_issue_relations`: id!, issue_id!, related_issue_id!, type!, created_at, updated_at
- `linear.linear_pending_uploads`: asset_id!, issue_id!, filename!, content_type!, size!, title, subtitle, created_at, content_b64
- `linear.linear_project_members`: id!, project_id!, user_id!, created_at!
- `linear.linear_project_teams`: id!, project_id!, team_id!, created_at!
- `linear.linear_workspace`: id!, name!, url_key!, created_at
- `slack.slack_meta`: key!, value!

**New columns on existing tables (32):**
- `confluence.confluence_page_versions`: synthesized (boolean)
- `contacts.contacts`: source (character varying)
- `gdocs.docs_documents`: text_style_runs_json (text)
- `github.github_issues`: state_reason (character varying), milestone_number (integer), duplicate_of_number (integer), parent_issue_number (integer), sub_issue_position (integer)
- `github.github_pull_requests`: maintainer_can_modify (boolean), requested_team_slugs_json (text)
- `github.github_review_comments`: pull_request_review_id (character varying), side (character varying), start_line (integer), start_side (character varying), subject_type (character varying)
- `linear.linear_attachments`: title (text), subtitle (text), asset_url (text), content_b64 (text), created_at (character varying)
- `linear.linear_issues`: uuid (character varying)
- `linear.linear_projects`: uuid (character varying), icon (character varying), color (character varying), started_at (character varying), completed_at (character varying), canceled_at (character varying), start_date_resolution (character varying), target_date_resolution (character varying), links_json! (text)
- `linear.linear_users`: is_admin! (boolean), is_guest! (boolean)

**Generated columns (never INSERT/UPDATE them):** `slack.slack_messages.text_fts`, `gmail.gmail_messages.body_text_fts`.

## 1. Cross-cutting rules

### Clock and latest base activity

The clock is 2026-02-14T00:00:00Z, a Saturday. The last weekday is 2026-02-13. [normal-only values below] For Oct 1, 2025 (synth-cut) the seed bound is 2025-10-01T00:00:00Z = Tuesday, September 30, 2025, 5:00 PM PT; the eval clock is 2025-10-01T07:00:00Z (Wednesday, October 1, 2025); the persona's today is Wednesday, October 1, 2025 and yesterday is Tuesday, September 30. No seeded event timestamp may pass the selected universe's seed bound; only plan fields (due, scheduled start/end, deadline) may be later. Latest base activity by service [normal-only — the Feb values below; read the Oct 1 universe for its own coverage]:

| Service | Latest base activity |
|---|---|
| Slack | reply ts 1770977006 = 2026-02-13T10:03:26Z |
| GitHub | PR updated 2026-02-13T21:59:05Z |
| Confluence | 2026-02-12T14:40:30Z |
| GCal | latest start 2026-02-12T16:30Z |
| Gmail | 2026-02-12 (sample) |
| Linear | updated 2026-01-28 |
| Trello | 2025-11-13 (the boards have gone quiet) |

### Read scoping

- **[V] `Evals/references/persona/acl.md` (2026-10-17 update, citing QC Rating Form V12; access matrix unchanged from 2026-09-27):**
  - Scoped services: Gmail, Slack, GCal, Drive, Docs, Sheets and Slides. Lists, searches and by-ID reads are all filtered, and a denied read returns "not found".
  - Unscoped services: Contacts, GitHub, Trello, Linear, Confluence and Snowflake.
  - **Attachments (2026-10-17):** Gmail attachment reads return no bytes, and Slack file records carry no content (`content_path` and `content_inline` are null on all base records). Linear and Drive-family attachments ship real content; Trello ships bytes for 42 of its 106. Never place a load-bearing fact inside a Gmail or Slack attachment.
- **Conflict:** the Spec-V2 docs (`Task_Authoring/references/Docs/4_Persona ACL Policy - V2.md`, dated 2026-09-26) still call Confluence and Snowflake "unclassified, verify from the persona's view". Treat them as unscoped but verify in the pre-check.
- Writes are never ACL-governed.

### Persona ID map [V]

Marcus Bennett has a GCal calendar and his own Gmail mailbox (`marcus.bennett@harmonygames.co`).

| Persona | Slack user_id | Gmail mailbox | Drive root folder | Linear user | Trello member | GitHub login | Confluence user | Contact id |
|---|---|---|---|---|---|---|---|---|
| Claire Morgan | EMPLOYEE_0009_SLACK_ID | yes | d_7fe31e7ec81996189e1f14 | usr_7fe31e7ec8199618 | 4bc5d398e54226f344ad3abc | EMPLOYEE_0009_GITHUB_USERNAME | user_EMPLOYEE_0009 | 7fe31e7ec81996189e1f14d6 |
| Marcus Bennett | EMPLOYEE_0002_SLACK_ID | yes | d_c77c50cc15c5342d638ebb | usr_c77c50cc15c5342d | 7a20445f698bc5871ffd17f5 | — | user_EMPLOYEE_0002 | c77c50cc15c5342d638ebb21 |
| Samuel Turner | EMPLOYEE_0004_SLACK_ID | yes | d_caafeec2804b3a67ce46aa | usr_caafeec2804b3a67 | 4ac40f0fbbad94d9e0e2df2a | EMPLOYEE_0004_GITHUB_USERNAME | user_STAFF_18 | caafeec2804b3a67ce46aabb |
| Martin Walsh | EMPLOYEE_0033_SLACK_ID | yes | d_51f5f16d46e8cf55f5ee33 | usr_51f5f16d46e8cf55 | ba9cc333cefad99228d6757d | — | user_EMPLOYEE_0033 | 51f5f16d46e8cf55f5ee337b |
| Simon Walker | EMPLOYEE_0037_SLACK_ID (13 channels) | yes | **—** | usr_eac7fcafa75e4935 | 60eb52a015fd4a1bf8837300 | — | user_STAFF_2 | a126ad1d54296023b4480445 |
| Victor Barnes | EMPLOYEE_0030_SLACK_ID | yes | d_7c929dfbe0e1b0c0d2c7ca | `usr_Victor Barnes` (contains a space) | 904fe5def35c5dddd2037d69 | — | user_EMPLOYEE_0030 | 20d3b9e691397554ea110e60 |
| Brian Foster | EMPLOYEE_0026_SLACK_ID | yes | d_fc22d5941b2aeb5c03ad32 | usr_fc22d5941b2aeb5c | d1cd0fef645a6c978ae1f068 | PERSON_0180_GITHUB_USERNAME | user_EMPLOYEE_0026 | fc22d5941b2aeb5c03ad32fa |
| Calvin Price | EMPLOYEE_0006_SLACK_ID | yes | d_49b9dfa5208d400d9b3937 | usr_49b9dfa5208d400d | ca5bb4c09fbf2a437f04531e | PERSON_0003_GITHUB_USERNAME (also PERSON_2137) | user_STAFF_19 | 49b9dfa5208d400d9b3937ca |
| Owen Baker | EMPLOYEE_0021_SLACK_ID | yes | d_4e13bd40cc73d0fc76f87c | usr_4e13bd40cc73d0fc | 919ee44a0d5157b7839f66a8 | PERSON_5877_GITHUB_USERNAME | user_EMPLOYEE_0021 | 4e13bd40cc73d0fc76f87c7d |
| Vincent Parker | EMPLOYEE_0012_SLACK_ID | yes | d_65c76e0b87aa7e9b84d1df | usr_65c76e0b87aa7e9b | 864e381ee6c844b2a3a7eaf8 | EMPLOYEE_0012_GITHUB_USERNAME | user_EMPLOYEE_0012 | 65c76e0b87aa7e9b84d1df22 |
| Oliver Brooks | EMPLOYEE_0003_SLACK_ID | yes | d_bdf01b53c6a92c5e167c65 | usr_bdf01b53c6a92c5e | 12c4a9dcd2d37a25a8d3b557 | EMPLOYEE_0003_GITHUB_USERNAME | user_EMPLOYEE_0003 | bdf01b53c6a92c5e167c658c |
| Douglas | EMPLOYEE_0031_SLACK_ID | yes | d_cd7849ec043ab3da107f8c | usr_cd7849ec043ab3da | 1c0688ee1d9093f5b978c1db | PERSON_5760_GITHUB_USERNAME | user_EMPLOYEE_0031 | cd7849ec043ab3da107f8c03 |
| Thomas | EMPLOYEE_0018_SLACK_ID | yes | d_4d9a08986fd1fbc9f7932d | usr_4d9a08986fd1fbc9 | ae0d489f73ee6c1df4393924 | — | user_STAFF_3 | 4d9a08986fd1fbc9f7932d24 |
| Frederick Stone | EMPLOYEE_0008_SLACK_ID | yes | d_175c0d7bc72ed244b944cb | usr_175c0d7bc72ed244 | 4b4a68fc0fec0b254e4f9d8e | PERSON_2314_GITHUB_USERNAME (name shows "Ryan") | user_EMPLOYEE_0008 | 175c0d7bc72ed244b944cb90 |
| Robert | EMPLOYEE_0016_SLACK_ID | yes | d_9f7ba94f7526d54d8482ba | usr_Robert | 3d06b73654d0c8940792514c | EMPLOYEE_0016_GITHUB_USERNAME | user_EMPLOYEE_0016 | 5f647df33ba6e92fbd56b05b (is_user) |
| Leonard Hayes | EMPLOYEE_0038_SLACK_ID | yes | d_63fffeb4fab5233ed5bb73 | usr_63fffeb4fab5233e | PERSON_6094_TRELLO_USER_ID | — | user_EMPLOYEE_0038 | 63fffeb4fab5233ed5bb73bf |
| Arthur Blake | EMPLOYEE_0025_SLACK_ID | yes | d_cc3e90160f490686039986 | usr_cc3e90160f490686 | 2162c1ba310341bf318f48b7 | EMPLOYEE_0025_GITHUB_USERNAME | user_EMPLOYEE_0025 | cc3e90160f49068603998654 |
| Julia Lawson | EMPLOYEE_0005_SLACK_ID | yes | d_8140f09bf9f1b94cb8ee2d | usr_8140f09bf9f1b94c | 793af7ca6940bf18eb516c75 | PERSON_0005_GITHUB_USERNAME | user_EMPLOYEE_0005 | 8140f09bf9f1b94cb8ee2dd7 |
| Tim Steudler | UBF5AB53C96 (0 channels) | **NO** | **—** | usr_bf5ab53c966f8ba7 | 29631c8d4796f104144bc1ab | — | user_STAFF_6 | 125371b9326ac40bee6368e6 |

All 19 personas have a GCal calendar (`calendar_id` = the persona's email). Victor Barnes departed April 2025 (last Slack 2025-04-15) — cannot review, approve or reply in either universe; his IDs stay valid for historical records only. Slack channel counts: Leonard 293, Robert 224, Arthur 216, Julia 158, Vincent 145, Brian 127, Douglas 124, Marcus Bennett 120, Owen 116, Calvin 108, Frederick 106, Oliver 103, Martin 99, Victor 88, Samuel 85, Claire 81, Thomas 42, Simon 13, Tim 0.

### Friction (Taxonomy step 16) [V]

- **Forced-error picker (18 functions):** slack_send_message, slack_conversations_history, slack_search_public_and_private, gmail_search_messages, gmail_get_message, github_get_file_contents, github_create_issue, github_create_pull_request, github_search_code, linear_create_issue, linear_list_issues, trello_create_card, gdrive_search, gdrive_read_file, gsheets_values_get, gcal_list_events, gdocs_get_document, gslides_get_presentation.
- **Async-wait picker (6 functions):** gmail_submit_search_messages, slack_submit_search, gdrive_submit_search, github_submit_search_code, linear_submit_list_issues, trello_submit_search. The wait is 5–300 s (default 30–35).
- Async affects search only, never fetch, and the instant search is disabled automatically.
- The catalog also has `confluence_submit_search` and `snowflake_submit_query` plus their job tools, but neither is selectable for a configured wait.

### SQL rules

From playbooks/01_Universe_Injection.md and tools/sql_lint.py:
- Literal values only. No NOW() or random().
- Parents are inserted before children, and UPDATEs are keyed on the primary key.
- Confluence and Snowflake are live and unscoped (`service-availability-v1`, still the current policy in `Evals/ENVIRONMENT.md`); give every dependence on them a natural pointer from another record.
- One person, one account per service: each author/creator/identity id must resolve to the person the record names, and a second account for an existing person is a FAIL.
- Every event timestamp at or before the task's seed bound (`freeze_utc` — 2025-10-01T00:00:00Z for Oct 1, 2026-02-14T00:00:00Z for Feb 14); only plan fields (due, scheduled start/end, deadline) may be later.
- Changelogs are retired in the V2 flow (the taxonomy collects only the SQL; Evals no longer reads changelogs).

---

## 2. Per-service sections

### 2.1 Slack (`<U>/<P>_HarmonyGames_Other_Services/Services_Data/slack`)

**(a) Tables (live schema). `!` marks NOT NULL.**
- `slack.slack_messages`, 24 columns:
  - NOT NULL: id!, ts! varchar, channel_id!, type!, text!, reply_count! int, reply_users_count! int, is_activity_message! bool, reactions_json! text, files_json! text, attachments_json! text, created_at! tstz, metadata_json! text.
  - Nullable: user_id, thread_parent_id, thread_ts_legacy, latest_reply, subtype, edited_ts, edited_user, bot_id, client_msg_id, permalink, text_fts (tsvector).
- `slack.slack_channels`, 14 columns:
  - NOT NULL: id!, is_channel!, is_private!, is_im!, is_mpim!, is_archived!, is_general!, num_members! int, created_ts! double, members_json! text.
  - Nullable: name, topic, purpose, creator_id.
- `slack.slack_users`, 10 columns: id!, is_bot!, is_admin!, deleted!, timezone!; nullable name, real_name, display_name, email, avatar_url.
- `slack.slack_files`, 16 columns: id!, name!, size! int, is_public!; nullable title, mimetype, filetype, user_id, channel_id, message_ts, created (bigint), url_private, permalink, preview, content_path, content_inline.
- `slack.slack_drafts`: id!, user_id!, text!, created! bigint, updated! bigint; nullable channel_id, thread_ts.
- `slack.slack_scheduled_messages`: id!, channel_id!, user_id!, text!, post_at! bigint, created! bigint, reply_broadcast! default false; nullable thread_ts.
- `slack.slack_emojis`.

**Base counts [V]:**
- 985 channels: 600 IMs, 217 MPIMs, 98 private channels, 70 public channels. 90 are archived. num_members equals len(members) on 985 of 985.
- 219 users.
- 687,230 message records in 5,353 shards (`messages/<CHANNEL>/<YYYY-MM>.json`). 585,573 have an `id`. The other 101,657 are raw Slack-shaped records (blocks, client_msg_id, no id).
- 14,879 thread parents (thread_ts == ts) and 88,474 replies.
- Text length: median 39 chars, p90 131. 59,958 messages have empty text.
- 53,422 files. `content_inline`, `preview` and `content_path` are null on all of them.

**Sample IDs [V]:**
- Messages: `9d4d8ed8acddc1f4b3953e29e6a56823` (ts 1731890278.557969 in C017C8D7AD41), `80550596f5ef1b263f5d69fbe34e9839` (ts 1767711222.749869), `fff23d88c589c1cea0d4e54c393a3e62`.
- Channels: `C04RYU8TJ8K` (#random), `C017C8D7AD41` (mpdm), `D04TZ84SZRR` (IM).
- Users: `EMPLOYEE_0016_SLACK_ID`, `PERSON_6030_SLACK_ID`, `U0512UQL4E9`.
- Files: `F080TSWCCVD`, `F06UPUMRYMS`, `F08UHUCHZ53`.

**(b) Carriers:**

| Carrier | Shown in export? | Notes |
|---|---|---|
| Top-level message `text` | Yes | |
| Thread reply `text` | Yes | Separate tool surface |
| Channel `topic`, `purpose` | Yes | |
| Reactions (`reactions_json`: names, counts, users) | Yes | Weak carrier: approvals or ✅ signals |
| `attachments_json` (unfurls) | Yes, all `[]` | |
| `files_json` plus `slack_files` (`title`, `preview`, `content_inline`) | Key present but null | New carrier [U] |
| `metadata_json` | Not shown | Read by `slack_get_message_metadata` [U] |
| Drafts (`slack_drafts.text`) | Not exported | Persona-private |
| Scheduled messages (`text`, `post_at`) | Not exported | |
| User profile (names, email, timezone; no title field) | Yes | |
| Edits (`edited_ts`, `edited_user`) | Yes | Only "edited" is visible; the old text is not stored |

**(c) Read tools [C]:**
- Discovery:
  - `slack_channels_list(channel_types!, cursor, limit, sort, exclude_archived)`
  - `slack_search_channels(query!, limit, include_private)`
  - `slack_get_conversation(channel!)`
  - `slack_list_channel_members(channel!, cursor, limit)`
- History (thread parents only [V for read_channel]):
  - `slack_read_channel(channel!, cursor, limit, include_activity_messages)`
  - `slack_conversations_history(channel_id!, cursor, include_activity_messages, limit)`
- Threads:
  - `slack_read_thread(channel!, thread_ts!, limit, cursor, include_activity_messages)`
  - `slack_conversations_replies(channel_id!, thread_ts!, cursor, include_activity_messages, limit: string)`
- Search:
  - `slack_conversations_search_messages(search_query, cursor, limit, filter_date_on, filter_date_during, filter_date_after, filter_date_before, filter_in_channel, filter_in_im_or_mpim, filter_threads_only, filter_users_from, filter_users_with)`
  - `slack_search_public(query!, cursor, limit)`
  - `slack_search_public_and_private(query!, cursor, limit)`
  - Async: `slack_submit_search(query!, cursor, limit)` → `slack_get_job_status(job_id)` → `slack_get_job_result(job_id)`
- Per message: `slack_get_message_metadata(channel!, ts!)`, `slack_get_reactions(channel!, ts!)`
- Files: `slack_list_files(channel, user, limit, cursor)`, `slack_read_file(file_id!, max_bytes)`
- People: `slack_read_user_profile(user!)`, `slack_search_users(query!, limit)`
- Persona-private: `slack_list_drafts(user, channel, limit)`, `slack_list_scheduled_messages(channel, user, limit)`
- `slack_search_emojis`
- Defaults are unknown. The page ceiling is about 50 [V, run evidence].

**(d) Call cost:**
- A channel with M top-level messages and T threads that have replies: ceil(M/50) history calls plus T thread calls. A thread longer than one page needs more calls.
- Each search page costs 1 call, or at least 3 if async.
- Each file costs 1 list plus 1 read. Reactions and metadata cost 1 per message if they are not inline [U].
- Resolving a user ID to a name costs 1 profile call per distinct user.

**(e) Scoping:**
- The persona's Slack ID must be in `slack_channels.members_json`. For an IM, the persona must be a party.
- Whether non-members can read public channels is [U]. Design as if the persona is a member.
- To give the persona reach, UPDATE `members_json` and `num_members` together.

**(f) Integrity [V unless noted]:**
- `drives` in the export carry no readable content for Slack files (`content_path`/`content_inline` null on all base records), so a Slack file is metadata only. Put the fact in the message `text`.
- `channel_id` must reference `slack_channels.id`, and `user_id` must reference `slack_users.id`.
- For a thread:
  - The parent's export `thread_ts` equals its `ts`, and replies carry `thread_ts` = parent ts.
  - Parent `reply_count` equals the number of replies (14,732 of 14,879 parents).
  - Parent `reply_users_count` equals the number of distinct repliers (14,748 of 14,879).
  - Parent `latest_reply` equals the maximum reply ts (14,737 of the 14,826 parents that have replies).
- A reply's ts must be later than its parent's. `created_at` is the ts expressed as a tstz.
- The DB encodes threads in `thread_parent_id` and `thread_ts_legacy`. The export shows only `thread_ts`. Whether `thread_parent_id` holds the parent's id or its ts is [U]; check with SELECT 1 in section 7.
- A file must appear both in `slack_files` (channel_id, message_ts) and inside the message's `files_json`. The export embeds full file objects there.

**(g) Writes [C]:** `slack_send_message(channel, text, thread_ts, user)`, `slack_conversations_add_message`, `slack_conversations_edit_message`, `slack_add_reaction`, `slack_remove_reaction`, `slack_create_conversation`, `slack_schedule_message`, `slack_send_message_draft`.

**(h) Pitfalls:**
- `ts` is a string with exactly 6 decimals and must be unique per channel. Check collisions on (channel, ts), because 101,657 base records have no id.
- Export fields map to columns as follows: `user`→`user_id`, `channel`→`channel_id`, `reactions`/`files`/`attachments`→`*_json`, `created`→`created_ts` (a string like "1677721220.000000"; 246 channels have "0.000000"), `creator`→`creator_id`, `members`→`members_json`.
- `text_fts` is a generated column (2026-10-17 eval rule): never list it in an INSERT or UPDATE — the platform rejects anything but `DEFAULT`. Search still indexes injected rows because the database computes it.

---

### 2.2 Gmail (`<U>/<P>_HarmonyGames_Gmail/Services_Data/gmail`)

**(a) Tables (live schema):**
- `gmail.gmail_messages`, 27 columns:
  - NOT NULL: id!, thread_id!, user_email!.
  - Nullable: label_ids_json, trash_removed_labels_json, snippet, history_id, internal_date (bigint ms), date (tstz), size_estimate, subject, from_email, from_name, to_json, cc_json, bcc_json, reply_to_json, body_text, body_html, headers_json, payload_json, in_reply_to, "references", mbox_from, date_parsed_source, attachments_meta_json, body_text_fts (tsvector).
- `gmail.gmail_threads`: id!, user_email!, snippet, history_id.
- `gmail.gmail_users`: email_address!, name, messages_total, threads_total, history_id, created_at.
- `gmail.gmail_labels`: 11 columns; id! and name! are NOT NULL.
- `gmail.gmail_label_user_counters`: label_id!, user_email!, plus 4 counts.
- `gmail.gmail_attachments`: id! (text), message_id!, filename, mime_type, size (bigint), data_b64.
- There is **no drafts table**.

**Base counts [V]:**
- 28 mailboxes and 36 labels. [normal-only count: synth-cut has 27 mailboxes — `lauren@harmonygames.co` exists only on Feb 14.]
- 88,726 thread files. Filenames are either `NNNNNNNN.json` or `<alias>@harmonygames.co_<thrid>.json`.
- 104,480 messages. 83,850 threads (94.5%) have one message; 271 have 12 or more.
- 9,697 messages carry 10,430 attachments.

**Sample IDs [V]:**
- Messages:
  - `robert@harmonygames.co/<CAMx_T-qp+g840B6RZ8L=LkP9cOUp_0YHLqW_LvjLZNpYe3aSuw@mail.gmail.com>`
  - `marcus.bennett@harmonygames.co/<b7ce4126.EAAABoiBq1sAAAAAAAAAAAU9h9IAAAA6pnMAAAAAAAvpOQBnia2w@mailjet.com>`
  - `SVC_0019_EMAIL/<CADuwL1jvxkoSThZONc3dLmWKSVTWXBTSdZjUz6UgWKCj+T5v-A@mail.gmail.com>`
- Threads: `robert@harmonygames.co/1768521114428228854`, `leonard.hayes@harmonygames.co/1773639741566757840`, `arthur.blake@harmonygames.co/1826526974265913874`.
- Labels: `INBOX`, `CATEGORY_UPDATES`, `Label_b19fb8d1b3`.
- The export attachment id is `att_0001`, numbered per message. The DB `gmail_attachments.id` format is [U].

**(b) Carriers:**
- `subject` and `body_text` (plus `body_html`). Bodies use `\r\n` line endings with `>`-quoted history, so earlier asks can sit in quoted text.
- from, to and cc: who was asked.
- `snippet`.
- User labels.
- **Attachment content** in `gmail_attachments.data_b64`. **Attachment reads return no bytes** to the Agent (2026-10-17 acl note: `no_attachment_root_configured` in the HarmonyGames runs), although the local export keeps the files under `root/attachments/`. Never make a fact depend on a Gmail attachment's content.
- `headers_json` (Date, Message-ID).
- Drafts are not injectable. `gmail_list_drafts` probably reads DRAFT-labelled messages [U].

**(c) Read tools [C]:**
- Mailbox and labels: `gmail_list_users()`, `gmail_get_profile(user_email)`, `gmail_list_labels(user_email)`, `gmail_get_label(label_id, user_email)`.
- Listing: `gmail_list_messages(user_email, label_ids, max_results, page_token, include_spam_trash)`, `gmail_list_threads(…same)`.
- Search: `gmail_search_messages(query!, user_email, max_results, page_token)`. Async: `gmail_submit_search_messages(…)` → `gmail_get_job_status` → `gmail_get_job_result`.
- Reading:
  - `gmail_get_message(message_id!, user_email)`
  - `gmail_get_messages_batch(message_ids[]!, user_email)` — bulk shortcut
  - `gmail_get_thread(thread_id!, user_email, limit, offset, format)` — long threads page
- `gmail_get_attachment(message_id!, attachment_id!, user_email)`, `gmail_list_drafts(limit, user_email)`.
- Query syntax and the default folder are [U]. Another universe's OE QC recorded a search that defaulted to INBOX and missed SENT.

**(d) Call cost:**
- N threads: S search or list pages, plus N `get_thread` calls (more for threads longer than a page), plus 1 per attachment.
- `get_messages_batch` can collapse N message reads into one call, so make attachments or long threads the per-item hooks.

**(e) Scoping:**
- A row is visible only if `user_email` is the persona. The ID prefix must be `persona/` and the thread must be the persona's own thread ID.
- Per-mailbox copies have different thread IDs. Example [V]: one Mandrill message is `leonard.hayes@…/1773639741566757840` in Leonard's mailbox and `robert@…/1773639742140893569` in Robert's.
- The sender's copy is labelled SENT. Recipients' copies are labelled INBOX, plus UNREAD or categories.
- Only Tim Steudler lacks a `gmail_users` row (his email is not a mailbox); every other persona, Marcus Bennett included, has one. For a new mailbox you would also need the row; whether the tools require it is [U].

**(f) Integrity:**
- Insert the `gmail_threads` row for each mailbox before its messages. `message.thread_id` must equal that thread ID, and `user_email` must match.
- A reply needs `in_reply_to` = the parent's RFC Message-ID, `"references"` = the chain, a later `date`, and a "Re: " subject.
- `internal_date` (ms) must equal `date`.
- `history_id` is NULL or a decimal string (digits only, `Evals/references/schema/id_contracts.json`); a label such as `hf_pf_reg_1` breaks every Gmail search.
- `attachments_meta_json` must list the `gmail_attachments` rows.
- `gmail_users.*_total` and `gmail_label_user_counters` are optional to bump [U whether tools read them].

**(g) Writes [C]:** send_message, reply_to_message, create_draft, send_draft, delete_draft, create_label, delete_label, modify_message_labels, modify_thread_labels, batch_modify_message_labels, archive_thread, trash and untrash for messages and threads, delete_message, delete_thread.

**(h) Pitfalls:**
- The export's `to`/`cc` are plain strings (`"leonard hayes" <leonard.hayes@…>, x@y`), but the columns are `*_json` with an [U] shape. Mirror a sibling (SELECT 3).
- The export `date` is a mix of ISO-Z and RFC-2822. `date_parsed` carries an offset, and the meaning of `date_parsed_source` is [U].
- `body_text_fts` is a generated column (2026-10-17 eval rule): never list it in an INSERT or UPDATE — the platform rejects anything but `DEFAULT` and can roll back the whole script. The same holds for Slack `text_fts`.
- Three Marcuses: **Marcus Bennett** (mailbox `marcus.bennett@harmonygames.co`, Slack `EMPLOYEE_0002_SLACK_ID`), **Marcus Lee** (`marcus.lee@harmonygames.co` — Slack `PERSON_2705_SLACK_ID`, Linear `usr_b501f018a4c5319f`, Confluence `user_STAFF_5`, Trello `54b24ad13c96c74bd0376532`, Contacts; no mailbox) and a mononym Trello member "Marcus" (`c48a210d5c5a4b59231c6873`). `marcus@harmonygames.co` exists in neither universe.

---

### 2.3 Google Calendar (`gcal/data.json`)

**(a) Tables (live schema):**
- `gcal.gcal_calendars`: calendar_id!, summary!, owner_email, shared_with_emails_json, visibility, description, time_zone, "primary", access_role, domain_role.
- `gcal.gcal_events`, 24 columns: only event_id! and calendar_id! are NOT NULL. The rest: summary, description, location, start_ts/end_ts (tstz), start_json/end_json, organizer_email, creator_email, attendees_json, status, visibility, transparency, rrule_json, recurring_event_id, original_start_json, sequence, created, updated, hangout_link, ical_uid, extras_json.

**Base counts [V]:**
- 39 calendars, all with `calendar_id` = the owner's email, all private.
- 11,233 events but only 1,059 distinct ical_uids (1,824 uid-plus-start instances). 2,950 carry an rrule and 1,194 are cancelled.
- Every start and end uses `dateTime`.
- The `description`, `location` and `visibility` keys are absent from all 11,233 export events.

**Sample IDs:**
- Events: `evt_00009bfb80dabb15aa5bb5`, `evt_82d34a1be510c8acec2645`, `evt_df0f6717ee34a02f8aff90`. The ID is not hash-derivable; collision-check it.
- ical_uid: `a58a8bb029ac801cd448630ad52461e3@hg4`.

**(b) Carriers:**
- `summary` [V shown].
- **`description`** and `location` [U whether returned; Google-shaped tools usually return them].
- Attendees and response status in `attendees_json`.
- Organizer and creator.
- Start and end: deadlines and ordering.
- rrule, cancelled status, `extras_json` [U].

**(c) Read tools [C]:** `gcal_list_calendars()`, `gcal_get_calendar(calendarId)`, `gcal_list_events(calendarId!, timeMin, timeMax, q, singleEvents, maxResults, pageToken, showDeleted)`, `gcal_search_events(q!, timeMin, timeMax, maxResults)`, `gcal_get_event(calendarId!, eventId!)`, `gcal_freebusy_query(calendarIds[]!, timeMin!, timeMax!)`.

**(d) Call cost:** one list per window page, plus one `get_event` per event if the list omits description or attendee detail [U].

**(e) Scoping:** the persona reads only its own calendar and events it is invited to. The persona's copy must have `calendar_id` = the persona's email and an `attendees_json` entry for the persona with `"self": true`.

**(f) Integrity [V]:**
- Store one row per attendee calendar (1,745 of 1,824 instances have copies equal to the attendee count). All copies share `ical_uid`, and `self` moves to each calendar's owner.
- start < end. created ≤ updated.
- `start_json` takes the form `{"dateTime":"…Z"}`. `rrule_json` is `[]` or `["RRULE:FREQ=WEEKLY;BYDAY=MO,TU,TH;UNTIL=…"]`.

**(g) Writes [C]:** create_event, update_event, patch_event, delete_event, respond_to_event.

**(h) Pitfalls:** `"primary"` is a reserved word. A future date is allowed only for an event scheduled after the clock.

---

### 2.4 Google Drive (`gdrive/data.json`)

**(a) Tables (live schema):**
- `gdrive.drive_files`, 22 columns: id!, name!, mime_type!; nullable parents_json, owner_email, shared_with_emails_json, shared_roles_json, visibility_role, shared_groups_json, visibility, owners_json, modified_time, created_time, size, trashed, starred, content_path, web_view_link, icon_link, description, drive_id, **content_text**.
- `gdrive.drive_users`: id!, email!, display_name!, photo_link.
- `gdrive.drive_sheets`: 0 rows in the export.

**Base counts [V]:**
- 53,866 files: 23,266 `d_` folders and 30,600 `f_` files. The `f_` files are 27,087 JSON, 1,074 markdown, 613 text, 443 PDF, 180 CSV, 8 msword, 633 Docs, 398 Sheets and 164 Slides.
- 25 root folders (empty `parents`), one per owner.
- 30,436 files have content on disk through `content_path`.
- 164 files have a `description`, all of the form "Reconstructed Google Slides sibling from Drive PDF f_… ".

**Sample IDs:**
- Files: `f_7cae0fe8a25e481ffe95b5`, `f_603e29a4a43eb6b9e4943d`, `f_03d2a47737977b13f6b998`.
- Folders: `d_63fffeb4fab5233ed5bb73` (Leonard's root), `d_d3aeaa27d14ab94e08d48a`, `d_dc0792405fe0ace876665c`.
- drive_users: `user_175c0d7bc72e`.

**(b) Carriers:**
- File `name`, `description`, folder path, modified_time.
- **`content_text`.** Content on disk is reached through `content_path`; `content_text` is **not served by Drive reads** on its own (2026-10-17 eval rule). A seeded file must either carry a `content_path` pointing at real bytes or, for a Google Doc, a `docs_documents` row with non-empty `body_text`.
- Sharing lists, since "who can see this" is itself a fact.

**(c) Read tools [C]:**
- `gdrive_search(query, mimeType, parentId, fullText, modifiedAfter, modifiedBefore, includeTrashed, pageSize, pageToken)`, plus the async `gdrive_submit_search`.
- `gdrive_list_folder(folderId, pageSize, pageToken)`, `gdrive_list_recent_files(limit)`.
- `gdrive_get_file_metadata(fileId)`, `gdrive_get_file_path(fileId)`.
- **`gdrive_read_file(fileId, exportMimeType, offset, length)`** — reads page through `offset`/`length`.
- `gdrive_list_sheets(spreadsheetId)`, `gdrive_read_sheet_range(spreadsheetId, sheetIndex)`.

**(d) Call cost:** one search, plus one metadata call, plus ceil(length / page length) reads per file. The default page length is unknown.

**(e) Scoping:**
- The persona must be `owner_email` or appear in `shared_with_emails_json`.
- Whether `visibility` = domain (121 files) or anyone (58 files) grants access is [U].
- Sharing is not inherited in the data [V]: the folder "Show & Tell" is unshared while a doc inside it is shared with 20 people.

**(f) Integrity:**
- `parents_json` must point to an existing `d_` folder; use the persona's root.
- `owners_json` = `[owner_email]` (53,866 of 53,866 [V]).
- A Google-native file needs a matching Docs, Sheets or Slides row with the same ID and the same sharing.
- `content_path` is `<owner_email>/<path>`: no leading `/` and no `root/` prefix (`Evals/references/schema/id_contracts.json`). A file with null `content_path` and empty `content_text` is unreadable and fails the eval; `content_text` alone is not served, and a Google Doc needs a `docs_documents` row with non-empty `body_text`.

**(g) Writes [C]:** create_file, create_folder, update_file_content, update_file_metadata, move_file, share_file, trash_file, restore_from_trash, delete_file.

**(h) Pitfalls:**
- Some `owner_email` values are not emails (`Resource: -6481757892984311338`).
- The shapes of `shared_roles_json`, `visibility_role` and `drive_id` are [U] (SELECT 9).

---

### 2.5 Google Docs (`gdocs/data.json`)

**(a) Tables (live schema):** `gdocs.docs_documents`: document_id!, title!, owner_email, shared_with_emails_json, visibility, body_text, style_runs_json, revision_id, drive_file_id, created_time, modified_time.

**Base counts:** 633 docs, 464 of them with no shares. Visibility: 568 private, 45 domain, 20 anyone.

**Sample IDs:** `f_1be142fdb7a3bfe62f534b`, `f_1a147d85c1cbe0c319af5c`, `f_00117462881159eceee63e`. Revisions are 10 hex digits (`0011746288`, `2ae3425800`, `ac4972b558`).

**(b) Carriers:** `body_text` (median about 5,000 chars), title, headings in `style_runs_json` (`{start, end, named_style, list_id, list_nesting}`), modified_time.

**(c) Read tools [C]:** `gdocs_search_documents(query, fullText, pageSize, pageToken)`, `gdocs_get_document(documentId)`, `gdocs_get_document_text(documentId)`. Neither get call takes a paging parameter, so very long bodies may spill.

**(d) Call cost:** one search plus one read per doc.

**(e) and (f) Scoping and integrity:**
- Drive ACL applies.
- The `drive_files` row needs the same ID, mime `application/vnd.google-apps.document` and identical sharing.
- `drive_file_id` = `document_id`.
- `style_runs` offsets must fall inside `body_text`.

**(g) Writes [C]:** gdocs_create_document, gdocs_batch_update, gdocs_delete_document.

---

### 2.6 Google Sheets (`gsheets/data.json`, 397 MB; stream it)

**(a) Tables (live schema):**
- `gsheets.sheets_spreadsheets`: spreadsheet_id!, title!, owner_email, shared_with_emails_json, visibility, drive_file_id, created_time, modified_time.
- `gsheets.sheets_sheets`: spreadsheet_id!, sheet_id! (int), title!, "index", row_count, column_count, **grid_json** (a 2-D JSON array).

**Base counts [V]:**
- 398 spreadsheets with 1,553 tabs. 235 have a single tab; the maximum is 52.
- Grid cells mix string (1.14M), int, float and bool values.
- `sheet_id` runs 0..N-1.
- `row_count` is padded: for example 1,004 declared rows against 8 real ones. The median is 40 non-empty rows; p90 is 406.

**Sample IDs:** `f_00c30de5acd0cf7656c140`, `f_00e7008444923e0fe1549c`, `f_0272f7ef3096043049e9f6`.

**(b) Carriers:** cell values (numbers and prose, such as Key Assumptions), tab titles, and the choice of which tab holds a fact.

**(c) Read tools [C]:** `gsheets_search_spreadsheets(query, pageSize, pageToken)`, `gsheets_get_spreadsheet(spreadsheetId, includeGridData)`, `gsheets_values_get(spreadsheetId, range)`, `gsheets_values_batch_get(spreadsheetId, ranges[])`, `gdrive_list_sheets`, `gdrive_read_sheet_range(spreadsheetId, sheetIndex)`.

**(d) Call cost:** K tabs cost 1 + K reads, or a single `batch_get` or `get_spreadsheet(includeGridData=true)`. Because of that cheap path, spread facts across different spreadsheets rather than across tabs of one sheet.

**(e) and (f) Scoping and integrity:** the same as Docs, using mime `…spreadsheet`. When a grid is edited, bump `modified_time` on both the spreadsheet row and the drive row.

**(g) Writes [C]:** values_update, values_append, batch_update, create_spreadsheet, delete_spreadsheet.

---

### 2.7 Google Slides (`gslides/data.json`)

**(a) Tables (live schema):**
- `gslides.slides_presentations`: presentation_id!, title!, owner_email, shared_with_emails_json, visibility, drive_file_id, revision_id, created_time, modified_time.
- `gslides.slides_pages`: presentation_id!, object_id!, "index", layout, **notes**.
- `gslides.slides_page_elements`: presentation_id!, page_object_id!, object_id!, kind, text, placeholder_type, x_emu, y_emu, width_emu, height_emu, table_json, ordinal.

**Base counts [V]:**
- 164 decks with 2,910 pages, all with layout BLANK.
- 2,804 TEXT_BOX elements, at most one per page. Text length: median 325, p90 977.
- `notes`, `table_json` and `ordinal` are never present.

**Sample IDs:** decks `f_995453726682ed7d87e5c8`, `f_0281d5b83f931db7fff2be`; pages `slide_cf82ac159869`, `slide_f8fca73952f5`; elements `el_1151940de2ca`, `el_134d308325eb`.

**(b) Carriers:** element text. Speaker notes [U returned; possibly only by `get_page`]. `table_json` [U].

**(c) Read tools [C]:** `gslides_search_presentations(query, pageSize, pageToken)`, `gslides_get_presentation(presentationId)`, `gslides_get_page(presentationId, pageObjectId)`, `gslides_get_presentation_text(presentationId)`.

**(d) Call cost:** one call returns the whole deck. Per-page calls are needed only if notes are page-only [U].

**(e) and (f):** the same as Docs, using mime `…presentation`.

**(g) Writes [C]:** create_presentation, batch_update, delete_presentation.

---

### 2.8 Contacts (`contacts/contacts.json`)

**(a) Table (live schema):** `contacts.contacts`: contact_id!, first_name!, **last_name!** (the export uses '' for 140 contacts), is_user, gender, age, nationality, city_living, country, status, job, description, phone, email, address, created_at, updated_at.

**Base counts [V]:**
- 171 contacts: 165 with 24-hex IDs and 6 with `cnt_`+12 hex.
- `job` is set on 37. **`description` is set on none.** 130 have tokenized emails.
- `current_user_id` = Robert's contact `5f647df33ba6e92fbd56b05b` (is_user = true).

**Sample IDs:** `7fe31e7ec81996189e1f14d6`, `cnt_1f37af74b039`, `9cda7dfa4eb75d2bc7ca76b2`.

**(b) Carriers:** job title, description (new), email, phone, address.

**(c) Read tools [C]:** `contacts_search_contacts(query!, limit, cursor)`, `contacts_get_contacts(limit, cursor)`, `contacts_get_contact(contact_id)`, `contacts_show_data(limit, cursor)`, `contacts_get_current_user_details()`. That last call may return Robert regardless of persona [U].

**(d) Call cost:** one search per person. The whole set can be dumped in a few pages, so Contacts is a weak call generator.

**(e) Scoping:** unscoped.

**(g) Writes [C]:** add_new_contact, edit_contact(contact_id, updates), delete_contact.

---

### 2.9 GitHub (`<U>/<P>_HarmonyGames_GitHub/Services_Data/github`: `data.json` plus git packs under `root/`)

**(a) Tables (live schema; 21 GitHub tables — the 6 added ones are in §0a):**
- `github_repositories`: 24 columns; id!, name!, full_name!, owner_login!.
- `github_pull_requests`: 27 columns; id!, repo_id!, number!.
- `github_pr_comments`: id!, pr_id!, author_login, body, created_at, updated_at.
- `github_reviews`: id!, pr_id!, author_login, state, body, submitted_at, commit_id, **seq!**.
- `github_review_comments`: id!, pr_id!, author_login, body, path, diff_hunk, line, position, commit_id, in_reply_to_id, created_at, **seq!**.
- `github_timeline_events`: id!, pr_id!, event!, actor_login, created_at, data_json.
- `github_commits`: sha!, repo_id!, message, dates, author and committer fields, parent_shas_json.
- `github_pull_request_commits`, `github_branches`, `github_labels`, `github_tags`, `github_releases`, `github_users`, `github_commit_map`.
- `github_issues`: id!, repo_id!, number!, title, state, author_login, body, labels_json, assignee_logins_json, pull_request_id, timestamps.
- There is **no issue-comments table**.

**Base counts [V]:**
- 16 repos and 47 users.
- 2,629 PRs: 2,498 merged, 122 closed unmerged, 9 open. 681 have empty bodies.
- 2,421 reviews: 1,825 APPROVED, 513 COMMENTED, 81 CHANGES_REQUESTED.
- 1,614 review comments. All have null line, position, commit_id and in_reply_to_id.
- 884 PR comments, 12,435 timeline events, 12,687 commits, 20,754 commit_map rows, 2,011 branches, 11 labels.
- **0 issues, 0 tags, 0 releases.**
- Repos are real git packs. Branch and PR SHAs go through `commit_map`.

**Sample IDs:**
- PRs: `harmonygames-Games/GameOfDominoes#1142`, `harmonygames-Games/match3d#23`, `harmonygames-Games/match3d#438`.
- Reviews: `…GameOfDominoes#1305#rev_4`, `…match3d-backend#14#rev_4`.
- Review comments: `…GameOfDominoes#1148#rc_7`, `…match3d#336#rc_5`.
- PR comments: `…GameOfDominoes#1001#c_1`, `…#858#c_2`.
- Timeline events: `…GameOfDominoes#52#ev_2`.
- Branches: `harmonygames-Games/match3d:calvin.price/DailyLogin`.
- Labels: `harmonygames-Games/Combo-Fighters:do not merge`.
- Commits: `1c6c5ca782bc77d53191ae737df53806b76929c6`.

**(b) Carriers:**
- PR title and body.
- PR conversation comments.
- Review state and body.
- Review comment body, path and diff_hunk.
- Timeline `data_json` (renamed, labeled, review_requested).
- Branch names, which embed Linear keys, for example `samuel.turner/ENG1229QuestCollectChapterRewards`.
- Commit messages (metadata only).
- Issues: a new carrier, with ID format [U].
- **Not SQL-injectable:** file contents, tree, blame, compare, commit files and patches. These come from the git packs; the tool data source is [U].

**(c) Read tools [C]:**
- Repos: `github_get_repository`, `github_search_repositories(query!, sort, order, page, perPage)`.
- PR enumeration: `github_list_pull_requests(owner, repo, state, base, head, sort, direction, page, perPage)`, `github_search_pull_requests(query!, owner, repo, page, perPage)`.
- Per PR:
  - `github_get_pull_request(owner, repo, pullNumber)`
  - `github_get_pull_request_comments`, `github_get_pull_request_reviews`. Which tool returns the conversation comments and which returns the review (inline) comments is [U].
  - `github_get_pull_request_files(…, page, perPage)`
  - `github_get_pull_request_commits`, `github_get_pull_request_timeline`, `github_get_pull_request_status`
- Issues: `github_list_issues(owner, repo, state, labels, page, perPage)`, `github_get_issue`, `github_get_issue_comments(…, limit, offset)`, `github_search_issues(query!, page, perPage)`.
- Commits and code:
  - `github_list_commits(…, sha, path, author, since, until, page, perPage)`, `github_get_commit`, `github_get_commit_files(…, include_patch)`, `github_compare_commits`.
  - `github_search_commits`; `github_search_code` plus the async `github_submit_search_code`.
  - `github_get_file_contents`, `github_get_file_history(…, page, perPage)`, `github_get_repository_tree(…, recursive, page, perPage)`, `github_get_blame`.
- Branches, labels, tags and releases: list and get variants.
- People: `github_get_user`, `github_search_users`, `github_list_repository_collaborators`, `github_get_me`.

**(d) Call cost:** each PR costs 5–7 calls (get, comments, reviews, files, commits, timeline, status), plus list or search pages.

**(e) Scoping:** unscoped.

**(f) Integrity [V]:**
- Every PR comment has a timeline `commented` event with the same pr_id and created_at (884 of 884). Bump PR `updated_at`.
- Continue the per-PR ID suffixes (`#c_N`, `#rev_N`, `#rc_N`, `#ev_N`).
- `seq` is NOT NULL but not exported [U semantics].
- `author_login` must exist in `github_users`.
- New issues: bump `repositories.open_issues_count` (0 in base). The issue `number` must not collide with PR numbers [U].

**(g) Writes [C]:** add_issue_comment, add_reply_to_pull_request_comment, create_branch, create_issue, create_label, create_or_update_file, create_pull_request, create_pull_request_review, delete_branch, delete_file, delete_label, merge_pull_request, push_files, update_issue, update_label, update_pull_request.

**(h) Pitfalls:**
- Combo-Fighters and GameOfDominoes use `develop` as the default branch, not `main`.
- Logins are tokenized. Frederick Stone's login is shown with the name "Ryan". The CodeRabbit bot is `PERSON_6026_GITHUB_USERNAME` (type Organization).
- Base `reviewed` timeline events have an empty actor and null created_at.

---

### 2.10 Linear (`linear/data.json`)

**(a) Tables (live schema):**
- `linear.linear_issues`, 27 columns:
  - NOT NULL: id!, title!, priority!, labels_json!, links_json!, relations_json!, **state_history_json!**, is_archived!, created_at! (varchar), updated_at! (varchar).
  - Nullable: project_id, team_id, parent_id, assignee_id, creator_id, state_id, cycle_id, identifier, number, description, estimate, due_date, started_at, completed_at, canceled_at, archived_at, time_in_status_minutes.
- `linear.linear_comments`: id!, issue_id!, author_id!, parent_id, body!, is_edited!, created_at!, updated_at!, sequence.
- `linear_projects`: priority!, labels_json!, is_archived!, and others.
- `linear_teams`, including `issue_counter`.
- `linear_users`, `linear_team_memberships`, `linear_attachments` (keyed on `issue_identifier`).
- `linear_workflow_states`, `linear_issue_labels`, `linear_project_statuses`: not exported.

**Base counts [V]:**
- 5 teams, 42 users, 2 projects (both with null description).
- 3,852 issues. 2,774 have a description (median 138 chars, p90 774). 1,282 have a parent and 236 have relations.
- **`links` is empty and `cycle_id` is null on every issue.**
- **0 comments.**
- 76 memberships and 2,027 attachment blobs. 513 attachments are tagged surface "comment" even though there are no comments.
- `state_id` holds the state name: Done 3,153, Canceled 403, Todo 102, Backlog 92, Bugs 22, In Progress 17, and others.
- Highest issue number per team: ART 792, DES 312, ENG 2437, EPI 28, ZOM 672.

**Sample IDs:**
- Issues: `ENG-1892`, `ART-383`, `ZOM-99`.
- Users: `usr_cc3e90160f490686`, `usr_Robert`, `usr_Victor Barnes` (Victor Barnes departed April 2025, last Slack 2025-04-15 — cannot review, approve or reply in either universe; historical records only).
- Team: `team_ENG`.
- Projects: `1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2`, `dbab77c7-f871-4888-abf8-d98b52a41624`.
- Membership: `tmem_team_ZOM_usr_c77c50cc15c5342d`.
- Attachment: `9740d2d4cd80bcca3d4b88e9`.
- Comment: no base format exists.

**(b) Carriers:**
- Issue description (Markdown).
- **Comments and reply threads** (new).
- Title, labels (sprint names), relations, parent/child links, state, priority, due date and estimate.
- Project description.

**(c) Read tools [C]:**
- Listing: `linear_list_issues(query, team, project, assignee, parentId, state, label, cycle, includeArchived, orderBy, limit, cursor, createdAt, updatedAt, maxDescriptionChars)`, plus the async `linear_submit_list_issues`.
- `linear_get_issue(id!, maxDescriptionChars)`.
- `linear_list_comments(issueId!, limit, cursor)`.
- `linear_get_attachments(issueId)`, `linear_get_attachment`.
- Lookups: `linear_list_issue_statuses`, `linear_list_issue_labels`, `linear_list_cycles`, `linear_list_projects`, `linear_get_project`, `linear_list_teams`, `linear_get_team`, `linear_list_users`, `linear_get_user`.
- **`linear_show_data(limit, cursor)`** — possible bulk shortcut [U].

**(d) Call cost:** N issues with comments cost list pages, plus N `get_issue` calls (if the list truncates descriptions through `maxDescriptionChars`; the default is [U]), plus N `list_comments` calls (more pages for long threads), plus N attachment calls.

**(e) Scoping:** unscoped.

**(f) Integrity:**
- `id` = `identifier` = `<KEY>-<n>`. Use the next free number and bump `issue_counter` [U].
- `team_id` is `team_<KEY>`. `assignee_id` and `creator_id` must exist in `linear_users`.
- Whether `state_id` is a name or a workflow-state ID in the DB is [U] (SELECT 5).
- A comment's `issue_id` is the issue ID, and `parent_id` handles replies.
- Bump the issue's `updated_at` to at least the comment time.

**(g) Writes [C]:** create_comment(issueId, body, parentId), create_issue, update_issue, create_project, update_project, create_team, create_user, delete_issue, delete_project.

**(h) Pitfalls:**
- Text timestamps must be exactly `YYYY-MM-DDTHH:MM:SSZ` and date fields `YYYY-MM-DD` (no space, no `+00:00` offset, no milliseconds, no `::timestamptz`, CAST or `now()`): another form stores but fails the run at load-universe. Every event timestamp at or before the seed bound; `due_date` and other plan fields may be later.
- `state_history_json` is NOT NULL with no default: a new issue needs `'[]'`. `linear_projects.links_json`, `linear_users.is_admin` and `linear_users.is_guest` are also NOT NULL without defaults.
- Do not seed a lone Linear↔GitHub link; playbooks/01_Universe_Injection.md relies on the empty `links` field as real friction.
- Keep the ENG-#### and ZOM-### series separate.

---

### 2.11 Trello (`trello/data.json`)

**(a) Tables (live schema). Quote every camelCase column.**
- `trello.trello_cards`: id!, name!, "idBoard"!, "idList"!, "desc", pos, closed, due, "dueComplete", "idMembers_json", "idLabels_json", "idShort", "shortLink", "shortUrl", url, "dateLastActivity", cover_json, badges_json, start, "idAttachmentCover".
- `trello.trello_actions`: id!, type!, date! (tstz), "idMemberCreator", "idBoard", "idCard", data_json.
- `trello.trello_checklists`: id!, name!, "idCard"!, "idBoard"!, pos.
- `trello.trello_check_items`: id!, name!, state, "idChecklist"!, pos, due, "idMember".
- `trello_lists`, `trello_labels`, `trello_boards` (including "memberIds_json", not exported), `trello_members`, `trello_attachments`, `trello_organizations`.

**Base counts [V]:**
- 5 boards: Harmony Games 449 cards, DD Product Roadmap 216, ZM ROADMAP 79, UA/BD 40, Welcome Board 19 (closed).
- 48 lists and 803 cards. 190 cards have a desc (median 202 chars).
- 5,294 actions, of which only **56 are `commentCard`**.
- 54 checklists and 161 check items (42 complete).
- `shortLink` is null on every card. The last activity is 2025-11-13.

**Sample IDs:**
- Boards: `6851a6569f3bf818760632ab` (ZM ROADMAP), `640643a3fd8f3ca308d9318e`.
- Lists: `68e98c965d88a7f2c3a56edf` ("Nov 5").
- Cards: `67095114e282ba0c0836f55b`, `6851a72836c07bf96717ffd2`.
- Comment actions: `68655f93de2e202c2ad77a76`, `666725edcaae266ae3447d7a`.
- Checklist: `65eb590205929a530f286df5`. Check item: `6855f20fb11687de8c0be3c8`.

**(b) Carriers:**
- Card name and desc.
- Comments (`data_json.text`).
- Checklist names and check items with state.
- Label names. List names, which carry release dates.
- due and dueComplete.
- Card history: `updateCard` actions store old and new values.
- Board desc.

**(c) Read tools [C]:**
- Boards and lists: `trello_list_boards(organizationId)`, `trello_get_board`, `trello_get_lists(boardId, filter)`.
- Cards: `trello_get_cards_on_board(boardId, filter, limit, offset)`, `trello_get_cards_in_list(listId, filter, limit, offset)`, `trello_get_card(cardId)`.
- Comments and history: `trello_get_comments(cardId, limit, offset)`, `trello_get_card_actions(cardId, filter, limit, offset)`, `trello_get_board_actions(boardId, filter, limit, before, since)`.
- Checklists: `trello_get_checklist(checklistId)`, `trello_get_checklists_on_board(boardId)` (bulk).
- Others: `trello_get_labels_on_board`, `trello_get_attachments(cardId)`, `trello_get_member_cards(memberId, filter, limit, offset)`, `trello_get_board_members`.
- Search: `trello_search(query!, modelTypes, idBoards, boards_limit, cards_limit, cards_filter)`, plus the async `trello_submit_search`.

**(d) Call cost:** each card costs `get_card` plus `get_comments`, plus `get_card_actions` if history matters, plus `get_attachments`. Checklists cost 1 per board in bulk, or 1 per checklist.

**(e) Scoping:** unscoped.

**(f) Integrity [V]:**
- Mint IDs whose first 8 hex digits are the record's timestamp in Unix seconds (5,245 of 5,294).
- `badges_json.comments` equals the number of commentCard actions (803 of 803).
- `badges.checkItems` and `badges.checkItemsChecked` equal the check items (803 of 803).
- Bump `"dateLastActivity"`. Use the next free `"idShort"` on the board.
- Comment `data_json` = `{"board":{id,name,shortLink},"card":{id,idShort,name,shortLink},"idCard":…,"list":{id,name},"text":…,"textData":{"emoji":{}}}`.

**(g) Writes [C]:** add_comment, create_card, update_card, move_card, archive_card, delete_card, create_checklist, create_check_item, update_check_item, create_label, add_label_to_card, add_member_to_card, create_list, update_list, archive_list, delete_list, create_board, update_board, delete_board.

**(h) Pitfalls:**
- `"desc"` is a reserved word.
- Leonard's member ID is the token `PERSON_6094_TRELLO_USER_ID`.
- Boards quiet since November 2025 make sudden 2026 activity visible as a recency change.

---

### 2.12 Confluence (`confluence/confluence_working.json`; live, unscoped)

**(a) Tables (live schema). All timestamps are varchar.**
- `confluence_pages`: id!, space_id!, parent_id, title!, body!, body_format!, status!, version! (int), author_id, created_at!, updated_at!.
- `confluence_page_versions`: id!, page_id!, number!, title!, body!, author_id, message, created_at!.
- `confluence_comments`: id!, page_id!, author_id!, parent_id, body!, created_at!, updated_at!.
- `confluence_labels`: id!, page_id!, name!, prefix!, created_at!.
- `confluence_attachments`: 9 columns.
- `confluence_spaces`, `confluence_users`.

**Base counts [V]:** 38 users, 4 spaces (ENG, PROD, COMPANY, OPS), 31 pages (1 archived, 1 draft), 78 versions, 12 comments, 53 labels (all prefix `global`), 10 attachments.

**Sample IDs:**
- Pages: `page_aws_infra`, `page_release_checklist`, `page_quest_postmortem`.
- Versions: `ver_ec0e30e2ff9fd6477c83ecbe0482fdd5`, `ver_page_api_reference_v12`, `ver_va01`.
- Comments: `comment_analytics_integration_c2`.
- Labels: `label_l001`…`label_l053`.
- Attachments: `att_a01`…`att_a10`.
- Users: `user_EMPLOYEE_0025`, `user_STAFF_7`.
- Spaces: `space_OPS`.

**(b) Carriers:**
- Page body in storage XHTML (info, warning and note macros; tables). Real pages run 250–1,125 words.
- **Version history**: earlier bodies plus edit messages. Example message: "Reverted the receipt-validation owner to the Phoenix Game API pending confirmation."
- Threaded comments, labels, page status (current, archived, draft), space description.

**(c) Read tools [C]:**
- Search: `confluence_search(cql, text, space, label, title, limit)`, plus the async `confluence_submit_search`.
- Listing: `confluence_list_pages(space, parentId, status, title, limit, offset)`, `confluence_list_spaces(query, includeArchived, limit, offset)`, `confluence_get_space(query)`.
- Pages: `confluence_get_page(page_id)`, `confluence_get_page_children`.
- History: `confluence_get_page_history(page_id)`, `confluence_get_page_version(page_id, version)`, `confluence_get_page_diff(page_id, from_version, to_version)`.
- Per page: `confluence_list_comments(page_id)`, `confluence_list_labels`, `confluence_list_attachments`.
- People: users list, get and search.

**(d) Call cost:** each page costs get, history and comments, plus up to V−1 version or diff reads. A single diff from v1 to vN is a shortcut.

**(e) Scoping:** unscoped per acl.md; verify in the pre-check. The current agent system prompt lists Confluence (the V1-era one did not); a pointer from another record still helps, since agents rarely open it.

**(f) Integrity [V, 31 of 31]:**
- `page.version` equals the highest version number, and versions run contiguously 1..N.
- The latest version's body and title equal the page's, and its `created_at` equals `page.updated_at`.
- An edit therefore needs an UPDATE to the page and an INSERT of version N+1.
- Comment `parent_id` must reference an existing comment.

**(g) Writes [C]:** create_page, update_page, delete_page, restore_page_version, add_comment, update_comment, delete_comment, add_label, create_space.

---

### 2.13 Snowflake (`snowflake/snowflake.json`, 2.6 GB; read by byte range)

**(a) Tables (live schema):**
- Metadata:
  - `snowflake_databases`: id!, name!, comment, created_at!.
  - `snowflake_schemas`.
  - `snowflake_tables`: id!, schema_id!, name!, table_type!, comment, row_count! int, created_at!, database_name!, schema_name!, physical_name!.
  - `snowflake_columns`: id!, table_id!, name!, data_type!, ordinal!, is_nullable!, comment.
  - `snowflake_query_history`: id!, query_text!, status!, rows_produced!, executed_at!, plus 11 nullable columns.
- Data: 40 tables named `snowflake.wh_<db>__<schema>__<table>`, with all columns UPPERCASE and nullable. Also 9 `wh_information_schema__*` tables.

**Row counts [V, streamed]:**

| Table | Rows |
|---|---|
| AD_SPEND_DAILY | 2,590 |
| AD_SPEND | 2,590 |
| UA_SPEND_UNIFIED_V2 | 2,590 |
| INSTALL_EVENTS | 31,210 |
| INSTALL_ATTRIBUTION | 31,210 |
| DIM_PLAYER | 31,210 |
| SINGULAR_INSTALLS_RAW | 15,600 |
| IAP_TRANSACTIONS | 977 |
| STORE_TRANSACTIONS | 993 |
| APP_STORE_REVIEWS | 1,600 |
| STORE_REVIEWS | 1,600 |
| PUSH_NOTIFICATION_STATS | 150 |
| PLAYER_DAILY_PROGRESS | 183,033 |
| DAILY_ACTIVE_USERS | 1,682 |
| DAILY_METRICS_AGG | 1,682 |
| LEVEL_PERFORMANCE | 5,497 |
| USER_COHORT_RETENTION | 333 |
| REVENUE_DAILY | 2,284 |
| REVENUE_DAILY_V2 | 2,284 |
| MONTHLY_BURN | 239 |
| CASH_BALANCE | 34 |
| HEADCOUNT | 371 |
| PAYROLL_ROSTER | 371 |
| FINANCE_LEDGER | 704 |
| LIVE_EVENT_PERFORMANCE | 827 |
| RESOURCE_FLOW_EVENTS | 1,483,075 |
| VIRTUAL_CURRENCY_LEDGER | 1,483,075 |
| RAW_EVENTS | 807,015 |
| RAW_GAME_EVENTS | 633,747 |
| STG_EVENTS_ENRICHED | 633,747 |
| PROGRESSION_EVENTS | 87,101 |
| STG_PROGRESSION_EVENTS | 87,101 |
| SESSION_LEVEL_EVENTS | 176,206 |
| CLIENT_ERROR_EVENTS | 40,292 |
| AD_IMPRESSION_EVENTS | 53,370 |
| DESIGN_EVENTS | 20,964 |
| AD_REVENUE | 77,373 |
| DIM_DATE | 1,026 |
| DIM_COUNTRY | 10 |
| DIM_DEVICE | 17 |

There are 18 query_history rows, exported with only query_text, status, rows_produced and executed_at. **They have no id.**

**Row primary-key samples:** `EVT-0001`, `REV-0000001`, `TXN-00000001`, `PLR-00096000`, `FIN-000001`, `ROSTER-0001`, `PUSH-0000001`, `INS-0000001`.

**(b) Carriers:**
- Rows to aggregate.
- Free text:
  - `APP_STORE_REVIEWS.REVIEW_TEXT`
  - `STORE_REVIEWS.TITLE` and `BODY`
  - `LIVE_EVENT_PERFORMANCE.FAILURE_NOTE` and `STATUS`
  - `CASH_BALANCE.NOTES`, `DIM_COUNTRY.NOTES`
  - `CLIENT_ERROR_EVENTS.MESSAGE`
  - `FINANCE_LEDGER.COUNTERPARTY`
- JSON columns: REVIEW_META, PLAYER_TRAITS, LEDGER_META, CALC_METADATA, SOURCE_META, DELIVERY_META, STACK_CONTEXT, CUSTOM_FIELDS, and others.
- **Table and column comments.** These are rich caveats, for example AD_SPEND_DAILY's note that no blended CPI is quoted. They are read through describe_table [U].
- **`query_history.query_text`**, read through `snowflake_query_history`.

**(c) Read tools [C]:** `snowflake_list_databases()`, `snowflake_list_schemas(database)`, `snowflake_list_tables(database, schema)`, `snowflake_describe_table(table!)`, `snowflake_execute_query(sql!, limit, offset)`, `snowflake_submit_query(…)` → job status and result, `snowflake_query_history(limit)`.

**(d) Call cost:** one describe per table, and one call per query plus pages through `offset`. A single GROUP BY collapses many lookups, so Snowflake is a weak call generator; its value is that figures must be derived rather than read.

**(e) Scoping:** unscoped per acl.md; verify per persona.

**(f) Integrity:**
- Keep the mirrored tables in step: AD_SPEND, AD_SPEND_DAILY and UA_SPEND_UNIFIED_V2 all have 2,590 rows; REVENUE_DAILY and its _V2 both have 2,284; and RAW_TELEMETRY's derived views are sampled projections of RAW_EVENTS, according to the schema comment.
- Table comments quote counts ("827 runs", "34 closed months"), so update the comment when rows change.
- Bump `snowflake_tables.row_count` [U whether the tools read it].

**(g) Writes:** none dedicated. Treat `execute_query` as read-only [U].

**(h) Pitfalls:**
- Use quoted UPPERCASE columns.
- PAYROLL_ROSTER export rows contain a `title` key that is in neither the column metadata nor the schema.
- Keep mirrored warehouse tables in step; a seeded row needs a pointer from another record.

---

## 3. Tool-surface blind spots: what a bulk or list call does not return

| Service | Bulk or list call | Not returned, so a per-item call is needed | Status |
|---|---|---|---|
| Slack | read_channel / conversations_history | Thread replies, including files posted in replies. Pages hold about 50 messages | V (run) |
| Slack | history | File body (`content_inline`), which needs `read_file`. Possibly metadata and reaction users | U |
| Gmail | search / list_threads / list_messages | Full bodies (likely snippets only); all messages of a long thread (get_thread pages); attachment content (get_attachment) | U (params C) |
| GCal | list_events | Possibly description and attendee detail | U |
| Drive | search / list_folder | File content (read_file, paged by offset and length) | C |
| Docs | search_documents | body_text (get_document) | U |
| Sheets | search / get_spreadsheet (includeGridData=false) | Cell grids (values_get per tab). batch_get and includeGridData=true are shortcuts | C |
| Slides | search_presentations | Text (get_presentation). Notes possibly only through get_page | U |
| Linear | list_issues | Full description when `maxDescriptionChars` truncates; comments (list_comments); attachments | C / U |
| Trello | get_cards_on_board | Comments (get_comments or get_card_actions); check items; edit history | U |
| GitHub | list_pull_requests / search | Body (maybe), comments, reviews, review comments, files, commits, timeline. Each is a separate call | C |
| Confluence | search / list_pages | Body (get_page); old versions (history plus version or diff); comments; labels | C |
| Snowflake | list_tables | Table and column comments (describe_table); rows (execute_query, paged by offset) | U |
| Contacts | search / get_contacts | Probably nothing missing, so cheap | U |

**Cheap paths that cut necessary calls.** Neutralize these by design:
- `gmail_get_messages_batch`
- `gsheets_values_batch_get` and `get_spreadsheet(includeGridData)`
- `gslides_get_presentation_text`
- `trello_get_checklists_on_board`
- `confluence_get_page_diff` from v1 to vN
- `slack_conversations_search_messages` with filters, which may return replies directly [U]
- `linear_show_data` [U]
- `contacts_show_data`
- Snowflake GROUP BY

---

## 4. Per-item call costs and a 500+ call budget model

| Unit of evidence | Minimum necessary calls |
|---|---|
| Slack channel window (M top-level messages, T threads with replies) | ceil(M/50) + T (+ pages per long thread) + files × 1 |
| Gmail thread (n messages, a attachments) | 1 get_thread (+ pages) + a. Search pages are shared; async adds at least 2 per search |
| GCal event set | 1 list per window page + 1 get_event per event [U] |
| Drive file | 1 metadata/path + ceil(size/length) reads |
| Doc | 1 get_document |
| Spreadsheet (K tabs) | 1 metadata + K values_get, or 1 batch read |
| Slide deck | 1 (plus P pages if notes are page-only) |
| Contact | 1 search |
| GitHub PR | 5–7 |
| Linear issue | 1 get_issue + 1 list_comments (+ pages) + 1 attachments |
| Trello card | 1 get_card + 1 get_comments (+ 1 actions + 1 attachments) |
| Confluence page with V versions | 1 get + 1 history + (V−1) version or diff reads + 1 comments + 1 labels |
| Snowflake | 1 describe per table + 1 per query (+ pages) |

**Illustrative allocation for about 600 calls.** hardness_gate.py's extreme profile needs at least 500 (≥ 300 per-record), at least 10 services, no service above 35% of calls; ~600 leaves headroom.

| Service | Allocation | Calls |
|---|---|---|
| Linear | 45 cohort issues × 3 + 4 list pages | ~140 |
| GitHub | 18 PRs × 6 + 6 list/search | ~114 |
| Slack | 5 channels × 4 pages + 30 threads + 6 files + 4 searches | ~60 |
| Trello | 2 boards + 25 cards × 2 + 6 action reads | ~58 |
| Gmail | 4 searches + 30 threads + 8 attachments | ~42 |
| Confluence | 6 pages × (get + history + 2 versions + comments) + 3 searches | ~33 |
| Sheets | 6 spreadsheets × (1 + 3 tabs) | ~24 |
| Snowflake | 6 describes + 16 queries | ~22 |
| Docs | 12 docs + 3 searches | ~15 |
| Drive | 8 metadata + 10 content reads | ~18 |
| GCal | 3 windows + 10 events | ~13 |
| Slides | 4 decks + 6 pages | ~10 |
| Contacts | 8 lookups | ~8 |
| Writes | Linear, Trello, Gmail, Confluence | ~6 |
| **Total** | | **~563** |

The count only counts if each call is necessary. Define the population with a predicate that can only be checked inside each item: a reply, comment, version, tab or attachment. Blocked or repeated calls add nothing (Docs/09 §2), and the tier minimum is measured on the golden run.

---

## 5. Ask and evidence carrier matrix

● = strong carrier with a base-data precedent. ○ = injectable but with no precedent or [U] rendering. – = none.

| Service | Long body text | Replies / comments | Structured status, owner, dates | Lists, checklists, labels | Numbers, grids | Version history | Attachments, file content | People, recipients | Metadata, notes |
|---|---|---|---|---|---|---|---|---|---|
| Slack | ● message text | ● thread replies (separate surface) | ○ (pins / none) | ○ reactions | – | ○ edited_ts only | ○ files content_inline [U] | ● members_json, DMs | ● topic, purpose; ○ metadata_json |
| Gmail | ● body_text and quoted history | ● reply chain (in_reply_to) | ● date, labels | ● user labels | – | – | ● gmail_attachments.data_b64 [U render] | ● from, to, cc per mailbox | ● subject, headers |
| GCal | ○ description [U] | ○ attendee response comment [U] | ● start, end, status, rrule | – | – | ● sequence / updated | – | ● attendees_json | ● summary; ○ location, extras_json |
| Drive | ○ content_text [U] | – | ● modified/created, owner | ● folder path | – | – | ○ content_text [U] | ● shared_with_emails_json | ● name; ○ description |
| Docs | ● body_text | – | ● modified_time | ● headings (style_runs) | – | – (revision_id only) | – | ● sharing | ● title |
| Sheets | ● prose cells | – | ● modified_time | ● tab titles | ● grid_json | – | – | ● sharing | ● title |
| Slides | ● element text | – | ● modified_time | – | ○ table_json [U] | – | – | ● sharing | ○ notes [U] |
| Contacts | ○ description (never set) | – | ○ status | – | – | – | – | ● email, job | ● job |
| GitHub | ● PR body; ○ issue body | ● PR comments, reviews, review comments | ● state, merged, dates, timeline | ● labels, branch names | ○ additions/deletions | ● timeline renamed/labeled | ✗ (git blobs not SQL-injectable) | ● reviewers, assignees | ● title, commit messages |
| Linear | ● description | ○ comments (0 in base) | ● state, priority, due, assignee | ● labels (sprints), relations, parent | ○ estimate | ○ state_history_json [U] | ✗ blobs | ● assignee, creator | ● title, project |
| Trello | ● card desc | ● commentCard actions (56) | ● list position, due, dueComplete | ● checklists, check items, labels | – | ● updateCard old/new | ✗ blobs | ● idMembers | ● card name, list name |
| Confluence | ● storage XHTML body | ● threaded comments | ● status, version | ● labels | ● XHTML tables | ● page_versions plus messages | ○ attachment metadata only | ● author_id | ● title, space |
| Snowflake | ○ REVIEW_TEXT, BODY, FAILURE_NOTE, NOTES | – | ● STATUS, dates | – | ● all rows (aggregation) | – | – | ○ PAYROLL_ROSTER.NAME | ● table and column comments; ● query_history.query_text |

**Containers available for dozens-of-containers spreading:** Slack channels, DMs and threads; Gmail threads (per mailbox); GCal events; Drive folders and files; Docs; spreadsheets and tabs; decks and pages; contacts; repos, PRs, review threads and issues; Linear teams, projects, issues and comment threads; Trello boards, lists, cards, checklists and comments; Confluence spaces, pages, versions and comments; Snowflake tables, row sets, comments and query history.

---

## 6. SQL INSERT skeletons

These use exact schema-qualified names (valid against the live schema). Replace `<…>`. Every event timestamp at or before the task's seed bound (`freeze_utc`: 2025-10-01T00:00:00Z for Oct 1, 2026-02-14T00:00:00Z for Feb 14); only plan fields (due, scheduled start/end, deadline) may be later. Nothing was executed.

```sql
-- ===== SLACK: top-level message (id = sha256('<channel>|<ts>')[:32]) =====
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy,
  reply_count, reply_users_count, latest_reply, is_activity_message, subtype, reactions_json, files_json,
  attachments_json, created_at, metadata_json)
VALUES ('<sha256(C…|1770890400.123456)[:32]>', '1770890400.123456', '<C…>', 'message', 'EMPLOYEE_0026_SLACK_ID',
  '<text>', NULL, NULL, 0, 0, NULL, false, NULL, '[]', '[]', '[]', '2026-02-12T10:00:00.123456Z', '{}');

-- ===== SLACK: thread reply + parent counters (thread_parent_id semantics [U] -> run SELECT 1 first) =====
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy,
  reply_count, reply_users_count, latest_reply, is_activity_message, reactions_json, files_json, attachments_json,
  created_at, metadata_json)
VALUES ('<sha256(C…|<reply_ts>)[:32]>', '<reply_ts>', '<C…>', 'message', '<U…>', '<reply text>',
  '<parent id OR parent ts — per SELECT 1>', '<parent ts>', 0, 0, NULL, false, '[]', '[]', '[]', '<reply ts as tstz>', '{}');
UPDATE slack.slack_messages SET reply_count = <n>, reply_users_count = <distinct repliers>, latest_reply = '<max reply ts>'
  WHERE id = '<parent id>';   -- if parent had no thread before, also set thread_ts_legacy per SELECT 1 pattern

-- ===== SLACK: file with readable content (slack files carry no content: keep facts in message text) =====
INSERT INTO slack.slack_files (id, name, title, mimetype, filetype, size, user_id, channel_id, message_ts, created,
  is_public, url_private, permalink, preview, content_path, content_inline)
VALUES ('F0AB12CD34E', '<name.txt>', '<title>', 'text/plain', 'text', <bytes>, '<U…>', '<C…>', '<message ts>',
  <epoch seconds>, false, NULL, NULL, '<first lines>', NULL, '<full text>');
-- and include the file object in that message's files_json (mirror a base files[] object)

-- ===== SLACK: DM / membership =====
INSERT INTO slack.slack_channels (id, name, is_channel, is_private, is_im, is_mpim, is_archived, is_general,
  num_members, topic, purpose, created_ts, creator_id, members_json)
VALUES ('D0AB1C2D3E4', 'D0AB1C2D3E4', false, false, true, false, false, false, 2, '', '', 1767225600.0, NULL,
  '["EMPLOYEE_0026_SLACK_ID","EMPLOYEE_0016_SLACK_ID"]');
UPDATE slack.slack_channels SET members_json = '<full new JSON list>', num_members = <len> WHERE id = '<C…>';

-- ===== GMAIL: one copy per mailbox (repeat block for sender[SENT] and each recipient[INBOX]) =====
INSERT INTO gmail.gmail_threads (id, user_email, snippet, history_id)
VALUES ('brian.foster@harmonygames.co/<19-digit thrid>', 'brian.foster@harmonygames.co', '<snippet>', NULL);
INSERT INTO gmail.gmail_messages (id, thread_id, user_email, label_ids_json, snippet, internal_date, date,
  size_estimate, subject, from_email, from_name, to_json, cc_json, bcc_json, reply_to_json, body_text, body_html,
  headers_json, in_reply_to, "references", mbox_from, attachments_meta_json)
VALUES ('brian.foster@harmonygames.co/<RFC-Message-ID incl <>>', 'brian.foster@harmonygames.co/<thrid>',
  'brian.foster@harmonygames.co', '["INBOX","UNREAD","CATEGORY_PERSONAL"]', '<snippet>', 1770890400000,
  '2026-02-12T10:00:00Z', <bytes>, 'Re: <subject>', 'robert@harmonygames.co', 'Robert',
  '<to_json — shape per SELECT 3>', '<cc_json>', '[]', '[]', E'<body with \r\n>', NULL,
  '<headers_json per SELECT 3>', '<parent Message-ID or ''''>', '<refs chain or ''''>', NULL, '[]');
INSERT INTO gmail.gmail_attachments (id, message_id, filename, mime_type, size, data_b64)
VALUES ('<id format per SELECT 4>', '<message id>', '<file.csv>', 'text/csv', <bytes>, '<base64>');

-- ===== GCAL: one row per attendee calendar (self:true on owner) =====
INSERT INTO gcal.gcal_events (event_id, calendar_id, summary, description, location, start_ts, end_ts, start_json,
  end_json, organizer_email, creator_email, attendees_json, status, visibility, transparency, rrule_json,
  recurring_event_id, original_start_json, sequence, created, updated, hangout_link, ical_uid, extras_json)
VALUES ('evt_<22hex>', 'brian.foster@harmonygames.co', '<summary>', '<agenda/ask>', NULL,
  '2026-02-17T16:00:00Z', '2026-02-17T16:30:00Z', '{"dateTime":"2026-02-17T16:00:00Z"}',
  '{"dateTime":"2026-02-17T16:30:00Z"}', 'robert@harmonygames.co', 'robert@harmonygames.co',
  '[{"email":"brian.foster@harmonygames.co","organizer":false,"responseStatus":"needsAction","self":true},{"email":"robert@harmonygames.co","organizer":true,"responseStatus":"accepted"}]',
  'confirmed', NULL, 'opaque', '[]', NULL, NULL, 0, '2026-02-11T09:12:00Z', '2026-02-11T09:12:00Z',
  'https://meet.google.com/<xxx-xxxx-xxx>?hs=224', '<32hex>@hg4', NULL);

-- ===== DRIVE: non-native file carrying text =====
INSERT INTO gdrive.drive_files (id, name, mime_type, parents_json, owner_email, shared_with_emails_json, visibility,
  owners_json, modified_time, created_time, size, trashed, starred, content_path, web_view_link, icon_link,
  description, content_text)
VALUES ('f_<22hex>', '<notes.md>', 'text/markdown', '["d_fc22d5941b2aeb5c03ad32"]', 'brian.foster@harmonygames.co',
  '[]', 'private', '["brian.foster@harmonygames.co"]', '<ts>', '<ts>', <bytes>, false, false,
  'brian.foster@harmonygames.co/notes/<notes.md>', NULL, NULL, NULL, NULL);
-- content_path = '<owner_email>/<path>': no leading '/', no 'root/', and real bytes must exist at that path
-- under the selected universe's gdrive root. content_text alone is not served by Drive reads.

-- ===== DOCS (drive row first, identical sharing; body_text must be non-empty or the doc is unreadable) =====
INSERT INTO gdrive.drive_files (id, name, mime_type, parents_json, owner_email, shared_with_emails_json, visibility,
  owners_json, modified_time, created_time, trashed, starred)
VALUES ('f_<22hex>', '<Title>', 'application/vnd.google-apps.document', '["d_<owner root>"]', '<owner>',
  '["brian.foster@harmonygames.co"]', 'private', '["<owner>"]', '<ts>', '<ts>', false, false);
INSERT INTO gdocs.docs_documents (document_id, title, owner_email, shared_with_emails_json, visibility, body_text,
  style_runs_json, revision_id, drive_file_id, created_time, modified_time)
VALUES ('f_<same>', '<Title>', '<owner>', '["brian.foster@harmonygames.co"]', 'private', '<body>',
  '[{"start":0,"end":<n>,"named_style":"TITLE","list_id":null,"list_nesting":0}]', '<10hex>', 'f_<same>', '<ts>', '<ts>');

-- ===== SHEETS (drive row with mime application/vnd.google-apps.spreadsheet first) =====
INSERT INTO gsheets.sheets_spreadsheets (spreadsheet_id, title, owner_email, shared_with_emails_json, visibility,
  drive_file_id, created_time, modified_time)
VALUES ('f_<22hex>', '<title>', '<owner>', '["<persona>"]', 'private', 'f_<same>', '<ts>', '<ts>');
INSERT INTO gsheets.sheets_sheets (spreadsheet_id, sheet_id, title, "index", row_count, column_count, grid_json)
VALUES ('f_<same>', 0, 'HG P&L', 0, 1000, 26, '[["","Cash P&L","2026-01"],["","Mobile revenue (cash in)",12345]]'),
       ('f_<same>', 1, 'Key Assumptions', 1, 1000, 26, '[["<assumption prose>"]]');
UPDATE gsheets.sheets_sheets SET grid_json = '<full new grid>' WHERE spreadsheet_id = '<id>' AND sheet_id = <n>;

-- ===== SLIDES (drive row with mime application/vnd.google-apps.presentation first) =====
INSERT INTO gslides.slides_presentations (presentation_id, title, owner_email, shared_with_emails_json, visibility,
  drive_file_id, revision_id, created_time, modified_time)
VALUES ('f_<22hex>', '<title>', '<owner>', '["<persona>"]', 'private', 'f_<same>', '<10hex>', '<ts>', '<ts>');
INSERT INTO gslides.slides_pages (presentation_id, object_id, "index", layout, notes)
VALUES ('f_<same>', 'slide_<12hex>', 0, 'BLANK', '<speaker notes [U returned]>');
INSERT INTO gslides.slides_page_elements (presentation_id, page_object_id, object_id, kind, text, placeholder_type,
  x_emu, y_emu, width_emu, height_emu, table_json, ordinal)
VALUES ('f_<same>', 'slide_<12hex>', 'el_<12hex>', 'TEXT_BOX', '<slide text>', NULL, 0, 0, 9144000, 5143500, NULL, 0);

-- ===== CONTACTS =====
INSERT INTO contacts.contacts (contact_id, first_name, last_name, is_user, gender, status, job, description, email,
  created_at, updated_at)
VALUES ('cnt_<12hex>', '<First>', '<Last or ''''>', false, 'Unknown', 'Unknown', '<job>', '<fact>', '<email/token>', '<ts>', '<ts>');
UPDATE contacts.contacts SET description = '<fact>', updated_at = '<ts>' WHERE contact_id = '<id>';

-- ===== GITHUB: PR conversation comment (+ required 'commented' timeline event) =====
INSERT INTO github.github_pr_comments (id, pr_id, author_login, body, created_at, updated_at)
VALUES ('harmonygames-Games/match3d#438#c_<next>', 'harmonygames-Games/match3d#438', 'EMPLOYEE_0003_GITHUB_USERNAME',
  '<body>', '2026-02-10T15:04:00Z', '2026-02-10T15:04:00Z');
INSERT INTO github.github_timeline_events (id, pr_id, event, actor_login, created_at, data_json)
VALUES ('harmonygames-Games/match3d#438#ev_<next>', 'harmonygames-Games/match3d#438', 'commented',
  'EMPLOYEE_0003_GITHUB_USERNAME', '2026-02-10T15:04:00Z', '{}');
UPDATE github.github_pull_requests SET updated_at = '2026-02-10T15:04:00Z' WHERE id = 'harmonygames-Games/match3d#438';
-- review + inline review comment (seq NOT NULL, semantics per SELECT 6)
INSERT INTO github.github_reviews (id, pr_id, author_login, state, body, submitted_at, commit_id, seq)
VALUES ('<pr_id>#rev_<next>', '<pr_id>', '<login>', 'CHANGES_REQUESTED', '<body>', '<ts>', NULL, <seq>);
INSERT INTO github.github_review_comments (id, pr_id, author_login, body, path, diff_hunk, line, position, commit_id,
  in_reply_to_id, created_at, seq)
VALUES ('<pr_id>#rc_<next>', '<pr_id>', '<login>', '<body>', 'Assets/Scripts/<Area>/<File>.cs',
  E'@@ -0,0 +1,48 @@\n+<real hunk lines>', NULL, NULL, NULL, NULL, '<ts>', <seq>);
-- issue (no base rows; id format [U])
INSERT INTO github.github_issues (id, repo_id, number, title, state, author_login, body, labels_json,
  assignee_logins_json, pull_request_id, created_at, updated_at, closed_at)
VALUES ('<id per SELECT 6>', 'harmonygames-Games/match3d', <number not used by a PR>, '<title>', 'open', '<login>',
  '<body>', '[]', '[]', NULL, '<ts>', '<ts>', NULL);

-- ===== LINEAR: issue, comment, description edit =====
INSERT INTO linear.linear_issues (id, project_id, team_id, parent_id, assignee_id, creator_id, state_id, cycle_id,
  identifier, number, title, description, priority, estimate, due_date, started_at, completed_at, canceled_at,
  archived_at, time_in_status_minutes, labels_json, links_json, relations_json, state_history_json, is_archived,
  created_at, updated_at)
VALUES ('ENG-2438', '1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2', 'team_ENG', NULL, 'usr_fc22d5941b2aeb5c', 'usr_Robert',
  '<state per SELECT 5, e.g. Todo>', NULL, 'ENG-2438', 2438, '<title>', '<markdown>', 2, NULL, '2026-02-20', NULL,
  NULL, NULL, NULL, NULL, '["Bug"]', '[]', '[{"target":"ENG-2404","type":"relates"}]', '[]',  -- state_history_json: NOT NULL, no default -> '[]' for a new issue
  false, '2026-02-09T14:22:10Z', '2026-02-09T14:22:10Z');
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence)
VALUES ('<new id; no base format — e.g. UUID literal>', 'ENG-2404', 'usr_fc22d5941b2aeb5c', NULL, '<markdown>', false,
  '2026-02-10T11:20:00Z', '2026-02-10T11:20:00Z', 1);
UPDATE linear.linear_issues SET description = '<full new markdown>', updated_at = '2026-02-10T11:20:00Z' WHERE id = 'ENG-2404';

-- ===== TRELLO: comment (+ badges), card, checklist (ids: first 8 hex = unix secs of the record) =====
INSERT INTO trello.trello_actions (id, type, date, "idMemberCreator", "idBoard", "idCard", data_json)
VALUES ('<hex(epoch of date)><16hex>', 'commentCard', '2026-02-09T15:10:22Z', 'd1cd0fef645a6c978ae1f068',
  '6851a6569f3bf818760632ab', '<card id>',
  '{"board":{"id":"6851a6569f3bf818760632ab","name":"ZM ROADMAP","shortLink":"HSqnngwQ"},"card":{"id":"<card id>","idShort":<n>,"name":"<card name>","shortLink":"<8char>"},"idCard":"<card id>","list":{"id":"<list id>","name":"<list name>"},"text":"<comment>","textData":{"emoji":{}}}');
UPDATE trello.trello_cards SET badges_json = '<badges with comments = old+1>', "dateLastActivity" = '2026-02-09T15:10:22Z'
  WHERE id = '<card id>';
INSERT INTO trello.trello_cards (id, name, "idBoard", "idList", "desc", pos, closed, due, "dueComplete",
  "idMembers_json", "idLabels_json", "idShort", "shortLink", "shortUrl", url, "dateLastActivity", cover_json,
  badges_json, start, "idAttachmentCover")
VALUES ('<hex(epoch)><16hex>', '[Feature] <name>', '<board>', '<list>', '<desc>', 147456.0, false, NULL, false,
  '["d1cd0fef645a6c978ae1f068"]', '[]', <next idShort>, NULL, NULL,
  'https://PERSON_6092_TRELLO_USERNAME.com/c/<8char>/<idShort>-<slug>', '<ts>', NULL,
  '{"attachments":0,"attachmentsByType":{"trello":{"board":0,"card":0}},"checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":0,"description":true,"due":null,"dueComplete":false,"externalSource":null,"fogbugz":"","lastUpdatedByAi":false,"location":false,"maliciousAttachments":0,"start":null,"votes":0}',
  NULL, NULL);
INSERT INTO trello.trello_checklists (id, name, "idCard", "idBoard", pos)
VALUES ('<hex(epoch)><16hex>', 'Checklist', '<card>', '<board>', 16384.0);
INSERT INTO trello.trello_check_items (id, name, state, "idChecklist", pos, due, "idMember")
VALUES ('<hex(epoch)><16hex>', '<item text>', 'incomplete', '<checklist>', 16384.0, NULL, NULL);
-- then update card badges_json checkItems / checkItemsChecked

-- ===== CONFLUENCE: page edit = UPDATE page + INSERT version N+1 =====
UPDATE confluence.confluence_pages SET body = '<new storage XHTML>', version = 3, updated_at = '2026-02-11T10:15:00Z'
  WHERE id = 'page_release_checklist';
INSERT INTO confluence.confluence_page_versions (id, page_id, number, title, body, author_id, message, created_at)
VALUES ('ver_<32hex>', 'page_release_checklist', 3, '<same title as page>', '<same new body>', 'user_EMPLOYEE_0026',
  '<edit message>', '2026-02-11T10:15:00Z');
INSERT INTO confluence.confluence_comments (id, page_id, author_id, parent_id, body, created_at, updated_at)
VALUES ('comment_release_checklist_c1', 'page_release_checklist', 'user_EMPLOYEE_0025', NULL, '<p>…</p>', '<ts>', '<ts>');
INSERT INTO confluence.confluence_pages (id, space_id, parent_id, title, body, body_format, status, version, author_id,
  created_at, updated_at)
VALUES ('page_<slug>', 'space_OPS', 'page_ops_home', '<title>', '<xhtml>', 'storage', 'current', 1, 'user_EMPLOYEE_0038', '<ts>', '<ts>');
INSERT INTO confluence.confluence_page_versions (id, page_id, number, title, body, author_id, message, created_at)
VALUES ('ver_<32hex>', 'page_<slug>', 1, '<title>', '<xhtml>', 'user_EMPLOYEE_0038', NULL, '<same ts>');
INSERT INTO confluence.confluence_labels (id, page_id, name, prefix, created_at)
VALUES ('label_l054', 'page_<slug>', '<label>', 'global', '<ts>');

-- ===== SNOWFLAKE (quoted UPPERCASE columns) =====
INSERT INTO snowflake.wh_live_ops__events__live_event_performance ("EVENT_ID","GAME_ID","EVENT_NAME","START_DATE",
  "END_DATE","PARTICIPANTS","COMPLETIONS","COMPLETION_RATE_PCT","AVG_SCORE","REVENUE_GENERATED_USD","STATUS","FAILURE_NOTE")
VALUES ('EVT-0828','zombie_match_3d','Plague Race','2026-02-03','2026-02-05',412,97,23.5,38120,0.00,'degraded','<note>');
INSERT INTO snowflake.wh_analytics__marketing__app_store_reviews ("REVIEW_ID","REVIEW_DATE","TITLE_ID","PLATFORM",
  "COUNTRY_CODE","RATING","REVIEW_TEXT","APP_VERSION","SENTIMENT_SCORE","INCIDENT_RELATED","TOPIC_BUCKET","REVIEW_META")
VALUES ('REV-0001601','2026-02-06','zombie_match_3d','ios','US',1,'<review text>','<ver>',-0.8,true,'<bucket>','{}');
UPDATE snowflake.snowflake_tables SET row_count = 828, comment = '<comment updated to match>' WHERE id = '<id per SELECT 7>';
INSERT INTO snowflake.snowflake_query_history (id, query_text, status, rows_produced, error_message, executed_at,
  user_name, role_name, warehouse_name, database_name, schema_name, query_type, start_time, end_time,
  total_elapsed_time, execution_status)
VALUES ('<id per SELECT 7>', '<SQL text>', 'SUCCESS', <n>, NULL, '2026-02-10T09:00:00Z', NULL, NULL, NULL, 'LIVE_OPS',
  'EVENTS', 'SELECT', NULL, NULL, NULL, NULL);
```

---

## 6b. Verified tool behaviour (Oct 4, from 277 V1 Opus trajectories in the V1 task corpus)

These resolve earlier [U] items; prefer them over any older statement in this file.
- `slack_conversations_search_messages` **returns thread replies** (596 / 2,663 results), and
  filter-only searches (`filter_users_from` + `filter_in_channel`, no query text) work, 50 per
  page with `cursor`. Replies are not a per-record surface against a determined agent.
- `linear_list_issues` items include `parent_id`, `relations`, `links`, `labels`, `description`
  (with `descriptionTruncated` / `descriptionLength`), sometimes `state_history`; **no comments**.
- `linear_list_comments(issueId)` returns injected comments (V1 task ENG-2401) — per issue, no
  bulk alternative.
- `github_search_pull_requests` / `github_search_issues` match title, body or branch by default
  (2,145 / 2,145 items in V1 runs without qualifiers) — **but the `in:comments` qualifier
  searches comment text** (corrected Oct 5 from task-1 Redo runs: `texture in:comments` returns
  a PR whose title, body and branch never mention "texture"). Items carry body, head ref,
  merged_at. PR comments are therefore searchable *and* Slack-mirrored: never a per-record or
  hidden surface.
- Large results are written to a file the agent must read in chunks ("exceeds maximum allowed
  tokens … saved to …").
- **The GitHub Slack app mirrors PR comments and reviews into Slack** (attachment `pretext`
  "Comment on pull request by …", `text` = the comment): GameOfDominoes and
  game-of-dominoes-backend → `#engineering-bots` `C050WGU41HR`; match3d → `#zombie-prs`
  `C093LEZGF6J`. Slack tools return `attachments`. A seeded PR comment/review in these repos
  needs its Slack copy, or GitHub and Slack disagree.
- Slack `attachments_json` is **not** always `[]`: bot integrations (GitHub app, Jenkins
  `#builds`) carry their content in attachments.

## 6a. Record pointers for `tools/hg.py search lookup` / `get` (verified by the first engine test)

| Service file | Array pointer |
|---|---|
| gdrive `data.json` | `/drive_files` (files `f_…`, folders `d_…`), `/drive_users`, `/drive_sheets` |
| gdocs `data.json` | `/docs_documents` |
| gsheets `data.json` | `/sheets_spreadsheets` |
| gslides `data.json` | `/slides_presentations` |
| linear `data.json` | `/issues`, `/comments`, `/users`, `/teams`, `/projects`, `/attachments` |
| trello `data.json` | `/cards`, `/actions`, `/lists`, `/boards` |
| gcal `data.json` | `/events` |
| contacts `contacts.json` | `/contacts` |
| github `data.json` | `/pull_requests`, `/pull_request_comments`, … |

Gmail thread files are one **object** per file, so `lookup` cannot check Gmail ids ("Expected
an array at the record pointer"). Check a minted Gmail id by searching the file names and
contents of all mailboxes (read-only `grep -rl` over `<U>/<P>_HarmonyGames_Gmail/Services_Data/gmail`).
`search` does not report a total hit count when `--limit` truncates: raise `--limit` or
page with `--offset` until `truncated` is false before quoting a count.

## 7. Open items: SELECTs to run in Universe Explorer before relying on [U] encodings

1. **Slack thread columns:**
   `SELECT id, ts, thread_parent_id, thread_ts_legacy, reply_count, latest_reply FROM slack.slack_messages WHERE channel_id='D05GJ141H4J' AND ts IN ('1695835296.690949','1695853779.743379');`
   This is a parent/reply pair taken from the export.
2. **Full-text search columns:**
   `SELECT table_schema, column_name, is_generated, generation_expression FROM information_schema.columns WHERE data_type='tsvector';`
   `SELECT event_object_table, trigger_name FROM information_schema.triggers WHERE event_object_schema IN ('slack','gmail');`
3. **Gmail JSON shapes:**
   `SELECT label_ids_json, to_json, cc_json, headers_json, attachments_meta_json, date_parsed_source FROM gmail.gmail_messages WHERE id='robert@harmonygames.co/<CAMx_T-qp+g840B6RZ8L=LkP9cOUp_0YHLqW_LvjLZNpYe3aSuw@mail.gmail.com>';`
4. **Gmail attachment IDs:** `SELECT id, message_id, filename FROM gmail.gmail_attachments LIMIT 3;`
5. **Linear states and history:**
   `SELECT * FROM linear.linear_workflow_states WHERE team_id='team_ENG';`
   `SELECT state_id, state_history_json FROM linear.linear_issues WHERE id='ENG-1892';`
   `SELECT id, issue_counter FROM linear.linear_teams;`
6. **GitHub seq and issues:**
   `SELECT id, seq FROM github.github_reviews WHERE pr_id='harmonygames-Games/GameOfDominoes#1148' ORDER BY seq;`
   Run the same for `github_review_comments`.
   `SELECT count(*) FROM github.github_issues;`
7. **Snowflake metadata:**
   `SELECT id, name, physical_name, row_count FROM snowflake.snowflake_tables LIMIT 5;`
   `SELECT * FROM snowflake.snowflake_query_history LIMIT 2;`
8. **GCal event columns:** `SELECT attendees_json, start_json, rrule_json, extras_json, description, visibility FROM gcal.gcal_events WHERE event_id='evt_00009bfb80dabb15aa5bb5';`
9. **Drive sharing columns:** `SELECT parents_json, shared_with_emails_json, shared_roles_json, visibility_role, owners_json, content_text IS NULL FROM gdrive.drive_files WHERE id='f_00117462881159eceee63e';`
10. **Trello JSON columns:** `SELECT badges_json, "idMembers_json", cover_json FROM trello.trello_cards WHERE id='6851a6fde24742cce9ad7b1c';`

**Tool rendering to confirm in the first trajectory:**
- Does `slack_read_file` serve `content_inline`?
- Does `gdrive_read_file` serve `content_text`?
- How does `gmail_get_attachment` return `data_b64`?
- Are gcal `description` and slides `notes` returned?
- What is the default for Linear `maxDescriptionChars`?
- Which GitHub comment tool returns which comment table?
- Can public Slack channels be read by non-members?
- Does Drive `domain`/`anyone` visibility grant access?
- What do `contacts_get_current_user_details` and `linear_show_data` return?
- What are the default pagination sizes?
