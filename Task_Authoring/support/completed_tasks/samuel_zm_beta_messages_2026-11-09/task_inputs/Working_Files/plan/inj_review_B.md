# Injection static review: Check B (SQL structure and supported schema rules)

**Check B result: PASS.** 147 of 147 statements checked, none sampled. 0 demonstrated defects. 1 provisional advisory group (7 columns). 4 observations that break no supported rule.

| Field | Value |
|---|---|
| SQL | `Task_Authoring/task_inputsK/01_Universe_Inject.sql` |
| sha256 | `0c1cf21627d5d9fb6303127c005cbaab216522c5ba1bf25a1e04573a44d24dad` (re-confirmed at the end of the review) |
| Review version | `injection-static-v2` |
| Universe and clock | synth-cut, Oct 1, 2025; 2025-10-01 07:00 UTC |
| Scope | Check B only. Checks A and C belong to other reviewers. |
| Definitions used | `Evals/references/schema/injection.json` (unverified snapshot, 58 tables), `id_contracts.json`, `Evals/0_Injection_Quality_Eval.md`. `Task_Authoring/references/universe_schema_live.json` was used for comparison only. |
| SQL executed | No. Nothing outside this file was edited. |

Line numbers point at the `INSERT` or `UPDATE` keyword. For INSERTs, `VALUES` is on the next line.

## Demonstrated defects

None.

## Per-table summary

"Assignments" counts each column-to-value pair across all rows. It totals 1,978, which equals the literal count from the tokenizer. No column shows a MISMATCH: where a column is in both references, type, nullability and default are identical.

| Table | INSERT | UPDATE | SQL lines | Assignments | injection.json | Live reference |
|---|---:|---:|---|---:|---|---|
| gdrive.drive_files | 3 | 0 | 7-11 | 39 | MATCH 39 | MATCH 39 |
| gdocs.docs_documents | 1 | 0 | 14 | 11 | MATCH 11 | MATCH 11 |
| gsheets.sheets_spreadsheets | 1 | 0 | 17 | 8 | MATCH 8 | MATCH 8 |
| gsheets.sheets_sheets | 1 | 0 | 19 | 7 | MATCH 7 | MATCH 7 |
| gslides.slides_presentations | 1 | 0 | 22 | 9 | MATCH 9 | MATCH 9 |
| gslides.slides_pages | 1 | 0 | 24 | 5 | MATCH 4, NOT COVERED 1 (`notes`) | MATCH 5 |
| gslides.slides_page_elements | 2 | 0 | 26-28 | 24 | MATCH 20, NOT COVERED 4 (`table_json`, `ordinal`) | MATCH 24 |
| slack.slack_messages | 6 | 2 | 31-43 | 115 | MATCH 115 | MATCH 115 |
| trello.trello_actions | 3 | 0 | 46-52 | 21 | MATCH 21 | MATCH 21 |
| trello.trello_cards | 0 | 3 | 48, 51, 54 | 5 | MATCH 5 | MATCH 5 |
| gmail.gmail_threads | 4 | 0 | 56-70 | 16 | MATCH 16 | MATCH 16 |
| gmail.gmail_messages | 5 | 0 | 58-72 | 110 | MATCH 110 | MATCH 110 |
| gcal.gcal_events | 2 | 0 | 75-77 | 46 | MATCH 46 | MATCH 46 |
| github.github_review_comments | 1 | 0 | 80 | 12 | MATCH 11, NOT COVERED 1 (`seq`) | MATCH 12 |
| github.github_reviews | 1 | 0 | 82 | 8 | MATCH 7, NOT COVERED 1 (`seq`) | MATCH 8 |
| linear.linear_team_memberships | 4 | 0 | 85-91 | 16 | MATCH 16 | MATCH 16 |
| linear.linear_issues | 34 | 2 | 93-159, 295-296 | 922 | MATCH 922 | MATCH 922 |
| linear.linear_comments | 67 | 0 | 161-293 | 603 | MATCH 536, NOT COVERED 67 (`sequence`) | MATCH 603 |
| linear.linear_teams | 0 | 1 | 297 | 1 | NOT COVERED 1 (`issue_counter`) | MATCH 1 |
| **Total (19 tables)** | **137** | **8** | | **1,978** | **MATCH 1,903, NOT COVERED 75** | **MATCH 1,978** |

Plus `BEGIN` (line 5) and `COMMIT` (line 298), for 147 statements.

## Results by rule

| # | Rule | Result | Evidence |
|---|---|---|---|
| 1 | Statement structure | PASS | Independent tokenizer: 147 statements, no tail, 0 quoting problems. A second scanner of different design also finds 147 semicolons outside literals and comments, with 0 stray quotes or backslashes left. Every INSERT has one row and equal column and value counts. No duplicate columns or assignments. `BEGIN` is first and `COMMIT` last, one of each. No `DO`, `$$`, `SELECT`, `DELETE`, `ON CONFLICT` or `RETURNING`. Literals are only strings (1,283), `E''` strings (7), numbers (181), `NULL` (393) and `false` (114). No casts and no function calls. |
| 1a | `E''` escapes | PASS | 7 `E''` strings, on lines 15, 59, 63, 65, 69, 73 and 81, use only `\n`, `\r` and `''`. No plain string contains a backslash. No NUL or stray control characters. File is valid UTF-8 with LF endings and no BOM at its start. |
| 2 | Identifier quoting | PASS | `"references"` (a reserved word) is quoted. `"index"` is quoted too, though Postgres does not require it. `"idMemberCreator"`, `"idBoard"`, `"idCard"`, `"dueComplete"` and `"dateLastActivity"` are quoted and match the schema spelling exactly. No unquoted identifier is mixed case or on the Postgres reserved list. `position`, `type`, `date`, `text`, `number`, `line` and `sequence` are legal unquoted as column names. |
| 3 | Columns exist | PASS | See the table above. |
| 3a | NOT NULL coverage | PASS | Every NOT NULL column with no default is supplied, in both references. No NULL goes into a NOT NULL column. This includes `seq` on both GitHub rows, which is NOT NULL in the live reference. |
| 3b | Generated columns | PASS | `slack_messages.text_fts` and `gmail_messages.body_text_fts` are never written. They are the only generated columns in the touched tables. No identity columns. |
| 4 | JSON | PASS | 231 `*_json` assignments: 227 parse under a strict parser that rejects duplicate keys and NaN, and 4 are `NULL` (`table_json` x2, `original_start_json` x2). Shape comparison is below. |
| 5 | Linear dates | PASS | 248 non-null Linear dates are all exactly `YYYY-MM-DDTHH:MM:SSZ`, including UPDATE lines 295-296. `due_date` is `NULL` on all rows. All 34 new issues carry `state_history_json = '[]'`. |
| 6 | Types | PASS | Booleans are bare `false`. Integers are unquoted and in range. 38 `timestamptz` values are valid. Every Slack `ts`, `thread_ts_legacy` and `latest_reply` is a string matching `NNNNNNNNNN.NNNNNN`, and each `created_at` equals its `ts` to the microsecond. Each Gmail `internal_date` equals its `date` in milliseconds and matches the `Date` header. No written column is declared float (N/A). No value exceeds a `max_length` in the live reference. |
| 7 | UPDATE statements | PASS | See the UPDATE table below. |
| 8 | Statement order | PASS | 114 parent references checked with 0 failures: docs, sheets and slides after `drive_files`; sheet after spreadsheet; page after presentation; elements after page; messages after their thread; replies after their parent; 32 child issues after DES-314; comments after their issue. The other parents already exist in the base: 2 Slack roots, 1 Gmail thread, ZOM-542, ZOM-556. |
| - | Eval linter | PASS | `hg.py lint`: 0 FAIL, 0 CHECK, 0 INFO, over 147 statements and the same hash. |

### UPDATE statements

All predicates are `id = '<literal>'`. The snapshot defines no primary keys, so `id` was confirmed as the unique key by scanning the base. Each target matches exactly one row. No statement repeats a column, and the two updates on one card (lines 48 and 51) set different columns.

| Line | Table | Target | Columns set | Base rows matched | Scan |
|---:|---|---|---|---:|---|
| 39 | slack_messages | `a3e78e820b9f880ef4e3d941562110df` | reply_count, reply_users_count, latest_reply | 1 | all 610,468 messages |
| 42 | slack_messages | `c42902df5f54c75c1a6e3529cd25121c` | same, plus thread_ts_legacy | 1 | all 610,468 messages |
| 48 | trello_cards | `6851a769c65dc0017a227bb7` | "dueComplete" | 1 | all 803 cards |
| 51 | trello_cards | `6851a769c65dc0017a227bb7` | badges_json, "dateLastActivity" | 1 | all 803 cards |
| 54 | trello_cards | `68d1eb90bef538c7c5c5599d` | badges_json, "dateLastActivity" | 1 | all 803 cards |
| 295 | linear_issues | `ZOM-542` | relations_json, updated_at | 1 | all 3,687 issues |
| 296 | linear_issues | `ZOM-556` | relations_json, updated_at | 1 | all 3,687 issues |
| 297 | linear_teams | `team_DES` | issue_counter | 1 | all 5 teams |

Writable tables: neither the eval nor the schema files state a list. The CB guideline (`08_Injection_Schema_Guideline_2026-10-22.md`) has a template for all 19 touched tables.

### JSON shape against base rows

| Column | Shape compared | Result |
|---|---|---|
| linear `relations_json` | `[{"target","type"}]` | Same as base (228 issues with relations) |
| linear `labels_json`, `links_json`, `state_history_json` | `[]` | `state_history_json = '[]'` is what the eval prescribes |
| trello `badges_json` | 16-key object | Same keys and types as 771 base cards. Only `comments` and `dueComplete` differ from the target card's base values. |
| trello `data_json` | `updateCard` and `commentCard` | Exact signature match to base actions (38 and 14 rows) |
| slack `reactions_json`, `files_json`, `attachments_json`, `metadata_json` | `[]`, `[]`, `[]`, `{}` | Same as base |
| gmail `headers_json` | `[{"name","value"}]` | Same as base |
| gmail `label_ids_json`, `attachments_meta_json` | `[str]`, `[]` | Same as base |
| gcal `start_json`, `end_json`, `attendees_json`, `rrule_json` | `{"dateTime"}`, attendee objects, `[]` | Same as base, including the `...Z` time format |
| gdocs `style_runs_json` | run objects | Same keys as base. Last `end` equals body length (1410), as in 138 base docs. |
| gsheets `grid_json` | array of row arrays | Same as base. See O2 on row width. |
| gdrive `parents_json`, `owners_json`, `shared_with_emails_json` | `[str]` | Same as base |

## Provisional-snapshot advisory (not a failure)

**A1. Seven columns are NOT COVERED by `injection.json`, 75 assignments.** All seven exist in the live reference with the listed types. Under Eval 0 and `schema/README.md`, a gap against the snapshot alone is advisory. The CB guideline's column lists omit them too, but those lists also omit `state_history_json`, which the eval requires, so the guideline is not complete enough to decide this.

| Column | Lines | Value written | Live reference | Note |
|---|---|---|---|---|
| `gslides.slides_pages.notes` | 24 | `NULL` | text, nullable | Optional: drop it, no data changes |
| `gslides.slides_page_elements.table_json` | 26, 28 | `NULL` | text, nullable | Optional: drop it, no data changes |
| `gslides.slides_page_elements.ordinal` | 26, 28 | 0, 1 | integer, nullable | Keeps element order |
| `github.github_review_comments.seq` | 80 | 18 | integer, NOT NULL, no default | Keep: omitting it would break the live NOT NULL rule |
| `github.github_reviews.seq` | 82 | 7 | integer, NOT NULL, no default | Keep, same reason |
| `linear.linear_comments.sequence` | 161-293 | 1-3 per issue | integer, nullable | Keeps comment order |
| `linear.linear_teams.issue_counter` | 297 | 346 | integer, nullable | Equals the highest injected DES number |

No change is required.

## Observations (no supported rule broken, not defects)

- **O1. Some JSON shapes are undocumented.** `gdrive.drive_files.shared_roles_json` (lines 7-11) has no base field to compare with; the three rows use `[{"email","role"}]`. Gmail `to_json`, `cc_json`, `bcc_json` and `reply_to_json` hold arrays of `Name <email>` strings, while the export's `to`, `cc`, `bcc` and `reply_to` are plain strings. All values parse and all columns are nullable. Exports are not backing columns under the eval, so this is a disclosed limit.
- **O2. Sheet grid width (line 19).** Rows are 5 wide with `column_count = 26`. Base rows are padded to `column_count` in 1,371 of 1,373 sheets; the other two have `column_count = 0`. The eval bars inferring constraints from stored examples, and `support/examples/sample_task_01` uses the same pattern (1000 x 26, 6 wide). If wanted, pad each row to 26 or set `column_count` to 5.
- **O3. Slides labels not seen in the base (lines 24-28).** `TITLE_AND_BODY`, `SHAPE`, `TITLE` and `BODY` do not occur in the base, which uses only `BLANK`, `TEXT_BOX` and null. These are varchar columns and no enum is defined.
- **O4. Gmail reply columns (lines 58-72).** `in_reply_to`, `"references"` and `mbox_from` are `NULL` on all 5 rows, while all 7,377 sampled base messages carry strings there. On line 64 the row's own `headers_json` has `In-Reply-To` and `References` values. The columns are nullable, so this is not a Check B issue; the Check C reviewer may want to look at it.

## Limits

- No SQL was run and no real Postgres parser was installed, so structure rests on two independently written scanners plus a tokenizer self-test on escaping edge cases. Deployment success is outside this review.
- `injection.json` is an unverified snapshot with no primary keys, foreign keys, enums or check constraints. The live reference was used for comparison only.
- Gmail shape comparison sampled 6,262 of 81,404 thread files (7,377 messages). The thread line 64 attaches to was read directly and exists. Slack, Trello, Linear, gcal, gdrive, gdocs, gsheets, gslides and GitHub comparisons used all base rows.
