# Injection Data-Integrity Review — `/injection`

Review version: `injection-static-v2`
Evidence contract: `stage-evidence-v1` (NEW checks for every structural, identity, collision, reference and chronology item. Some cross-service text-consistency items are REUSED from the revision-6 report, as listed in §5.)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

## 1. Scope

| Item | Value |
|---|---|
| Review | Chat/attachment review, portal attempt 6ad90ea979eb9e5d89f8879f, audit mode (rerun after the contributor's revision) |
| Actual review time | 2026-10-26T18:44Z |
| Universe | `Universe_SynthCut`, hg4-synth-sep30cut v16; `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Reviewed input | `Evals/task_inputs/01_Universe_Inject.sql` (input revision 7, attached as `01_Universe_Inject (4).sql`), 170,683 bytes, 820 lines, SHA-256 `f5a42cee096292f3b7261a31b89e7b8e345ec48aecbf4c60e6bfcc373740c9c3` |
| Previous version | revision 6, SHA-256 `5918bcb0…8f15a7` (prior report PASS, report SHA-256 `0f3928d70a905eedbbdb4706299c7aeb8d6e7efceff918f07d38f0cb8956af0d`) |
| Rules | Eval 0 `b1ea752a…723d3a`; WORKFLOW.md `ee4cd8e1…04fcd5d`; scoring.json `5e0bed76…0600c3`; schema snapshot `injection.json` `31dcb2b4…4c5151`; `id_contracts.json` `fc4711ef…9ed4682` (all unchanged since the revision-6 report) |
| Lint | `hg_injection_lint.py` `injection-lint-v1` (SHA-256 `a8226e2a…fc5448b`), universe synthcut, clock 2025-10-01T07:00:00Z |
| Evaluator | Opus 5.5 (claude-opus-5-5) |

### Input manifest entry (recorded here)

`hg_write_output.py` has no `input_manifest` key, and this review writes under `reports/` only through that writer, so the injection manifest entry is recorded here:

```json
{"injection": {"review_version": "injection-static-v2", "evidence_contract": "stage-evidence-v1",
  "inputs": {"01_Universe_Inject.sql": {"sha256": "f5a42cee096292f3b7261a31b89e7b8e345ec48aecbf4c60e6bfcc373740c9c3", "bytes": 170683, "input_revision": 7}},
  "universe_manifest_sha256": "da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a",
  "reused_evidence": [{"source_report": "Evals/task_inputs/reports/0_injection.md",
    "source_report_sha256": "0f3928d70a905eedbbdb4706299c7aeb8d6e7efceff918f07d38f0cb8956af0d",
    "items": ["§5 Check C detail: prod branch/cherry-pick sequence", "deploy log vs PR prod: comments", "review/timeline one-to-one matching", "ZOM-457 and ZOM-510 comment text vs base hierarchy/sheet", "DD launch page text", "Trello card desc", "unapproved merges vs base practice", "stale statements as supported context", "§5 Check B snapshot column MATCH/NOT COVERED table"],
    "dependencies_verified_unchanged": "every reused statement is byte-identical between revisions 6 and 7 (diff shows only deletions of 4 statements and the header count line); base source manifests (github ee578c91…377538, linear b49ec9e8…953b4d, gdrive 05147aa2…d51e72, gdocs 1b53998d…edac21, gsheets a9cc229c…e0a28f, confluence d3f13938…f937f0, trello 6ba242f4…907e3f, gcal 4f093d89…c4f51e, slack channels 3cca0f7e…0626cc, users 6aac5103…75dc, gmail users 9a90b6bf…c3e403) equal those in the source report; rule/schema hashes and clock unchanged"}]}}
```

### Changes from revision 6

| # | Change | Rows |
|---|---|---|
| 1 | Header count comment 404 INSERT / 2 UPDATE → 402 INSERT / 0 UPDATE | comment |
| 2 | **Removed** ZOM-535 comment `cmt_b61f9c6d82a6b4cf9455` ("client side fix, nothing needed in match3d-backend. ok on 0.3.132", 2025-09-30T14:44:39Z) | −1 `linear_comments` |
| 3 | **Removed** `UPDATE linear.linear_issues SET updated_at = '2025-09-30T14:44:39Z' WHERE id = 'ZOM-535'` | −1 UPDATE |
| 4 | **Removed** ZOM-504 comment `cmt_c4fb570f231f9c8d8cd2` ("client only, checked on 0.3.132", 2025-09-30T14:37:05Z) | −1 `linear_comments` |
| 5 | **Removed** `UPDATE linear.linear_issues SET updated_at = '2025-09-30T14:37:05Z' WHERE id = 'ZOM-504'` | −1 UPDATE |

No other statement changed. This is the first fix option for Issue 1 in the saved `/prompt` report: ZOM-535 (base Todo) and ZOM-504 (base Backlog) no longer carry fixed-and-verified comments. Their base rows are now untouched.

### Base sources read (manifest SHA-256 as returned by the record helper, this run)

| Source (under `Universe_SynthCut/`) | Manifest SHA-256 | Coverage (all `scan_complete: true`) |
|---|---|---|
| `SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json` | `ee578c91…377538` | repositories 15, users 46, PRs 2,475, branches 1,824, commits 11,226, PR commits 13,048, PR comments 687, review comments 1,387, reviews 2,230, timeline events 11,406 |
| `…Other_Services/Services_Data/linear/data.json` | `b49ec9e8…953b4d` | issues 3,687, users 41, comments 0 |
| `…Other_Services/Services_Data/trello/data.json` | `6ba242f4…907e3f` | boards 5, lists 47, members 42, cards 803, actions 5,252 |
| `…Other_Services/Services_Data/gdrive/data.json` | `05147aa2…d51e72` | drive_files 53,631, drive_users 25 |
| `…/gdocs/data.json` / `…/gsheets/data.json` | `1b53998d…edac21` / `a9cc229c…e0a28f` | docs 595, spreadsheets 356 |
| `…/gcal/data.json` | `4f093d89…c4f51e` | calendars 38, events 10,395 |
| `…/confluence/confluence_working.json` | `d3f13938…f937f0` | spaces 4, pages 30, users 37, page_versions 58 |
| `…/slack/channels.json`, `users.json`, `messages/*.json` | `3cca0f7e…0626cc`, `6aac5103…75dc` | channels 948, users 218; 4,840 message files / 610,468 messages |
| `SynthCut_HarmonyGames_Gmail/Services_Data/gmail/users.json`, `threads/*.json` | `9a90b6bf…c3e403` | 27 mailboxes; `/messages` id check over all 81,404 thread files (95,164 messages); text scan of all 81,404 files for the 6 thread numbers and 2 Message-IDs |

## 2. Input / authority issues

- The SQL is the only input for this stage. Revision 7 was saved and read in full. No inputs are missing.
- Header comments (`-- Are you planning to inject? Yes`, persona/services summary, "Literal values only; parents before children; re-apply this exact SQL before every agent run") are author notes. None addresses a solver or grader or mentions tool calls or pass rate. The header's count (402 INSERT, 0 UPDATE) matches the parse.
- The schema snapshot is unverified and does not cover the Confluence tables, so snapshot comparisons are provisional.
- Helper note: the first `hg_search.py get-many` call and the first `hg_records.py` batch returned `Source manifest changed during the read` on every check (the same first-read behaviour noted in the revision-6 report). Their results were not used. One retry of each completed with `scan_complete: true` and no errors, and only those results are cited. A Gmail thread-id check at the thread-file root failed with "Expected an array at the record pointer", because thread files are single objects. It was replaced by a complete text scan (see §5).
- 33 lone `\r` bytes inside Gmail `E''` body strings are unchanged. They are string content, not statement breaks. Ledger line numbers are counted on `\n` only.

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, base manifest, review version | NEW, done |
| Run `hg_injection_lint.py`; resolve every flag | NEW, 0 FAIL / 0 CHECK / 0 INFO |
| Inventory every statement and affected record | NEW, 404 statements: BEGIN (line 5), 402 single-row INSERT, COMMIT (line 820) (ledger §8) |
| Check A: references, collisions, ID contracts, readable Drive files, one account per person | NEW, PASS |
| Check B: SQL structure and supported schema rules | NEW (snapshot column table REUSED), PASS |
| Check C: dates, relationships, consistency | NEW for chronology and the deletion's effects; text-consistency items REUSED; PASS |
| Report coverage, findings, limits, one verdict | NEW, done |

## 4. Lint flags and resolution

`counts: FAIL 0, CHECK 0, INFO 0`. Statements 404 (begin 1, insert 402, commit 1); unparsed: none. Base files loaded: confluence, slack users, trello, gmail users, github, linear, contacts. Checks run: future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape. Nothing to resolve. The clean lint was not treated as a PASS; checks A–C were done in full.

## 5. Checks A–C

| Check | Result | Evidence |
|---|---|---|
| A: Records, references and IDs | PASS | 46 exact-record checks (all complete). Every referenced repo, login, Linear issue/author, Drive parent/user, Confluence space/parent/author, Trello board/list/member, calendar, Slack channel/user and Gmail mailbox resolves. Every new key is free in the full base collection and unique within the SQL. |
| B: SQL structure and supported schema rules | PASS | 402 single-row INSERTs inside BEGIN…COMMIT, column count = value count, no duplicate columns, no trailing/ON CONFLICT clause, no casts/DEFAULT/`now()`. No UPDATE/DELETE remains. No generated column is set. Linear times are `YYYY-MM-DDTHH:MM:SSZ`. Every `*_json` literal parses. No NOT NULL column is omitted (lint). |
| C: Dates, relationships and consistency | PASS | The latest event timestamp is 2025-09-30T21:12:44.508127Z (Slack, line 45), before 2025-10-01T07:00Z. Nothing remaining references the two removed comments or depends on the removed UPDATEs. All 77 remaining Linear comments sit on Done issues, inside each issue's created→completed window. |

### Check A detail (NEW)

- **GitHub**: repo `harmonygames-Games/match3d-backend` exists. Its 35 base PRs are #1–#35, and PR numbers 37–54 match only in other repos (GameOfDominoes, game-of-dominoes-backend, match3d). 0 collisions for 18 PR ids, 19 branch ids, 19 branch names (incl. `prod`; none of the 37 base branches has these names), 19 commit SHAs, 18 PR-commit ids, 40 comment ids (also checked against `/review_comments`), 37 review ids and 131 timeline ids. All 6 logins resolve in `/users`. Every PR `head_sha`, branch head and review `commit_id` is an injected commit. The new `prod` branch (line 663) points at `c219e8c3…` (line 661), which is inserted first.
  - `base_sha`: the 18 PR `base_sha` values are commit records in neither the base nor the SQL. That is not a broken reference. The snapshot defines `github_pull_requests.base_sha` as nullable `character varying` with no foreign key, and base match3d-backend PRs show the same pattern: of their 2 distinct `base_sha` values, 1 has no `/commits` record (complete scan).
- **Linear**: all 77 comment `issue_id` targets exist (`identifier` and `id` both match). All 11 `author_id` values resolve in `/users`. Base `/comments` is empty (scan complete), so the 77 comment ids cannot collide, and they are unique in the SQL.
- **Slack**: channels `C0880U9751A` (zombie-match3d, 25 members) and `D05QQF7V404` exist. Authors are `EMPLOYEE_0031_SLACK_ID` (douglas@), `EMPLOYEE_0025_SLACK_ID` (arthur.blake@) and `EMPLOYEE_0003_SLACK_ID` (oliver.brooks@). Each author is in the member list of every channel they post in (9 of 9). 0 id and 0 ts matches across all 610,468 base messages. The thread parent `81531d5f…` is the injected line-47 message.
- **Trello**: board `6851a6569f3bf818760632ab` (ZM ROADMAP), list `6851a674975da1fe76e70d93` (BETA: Oct 10) and member `2162c1ba310341bf318f48b7` (Arthur Blake) exist. The 2 card ids and 3 action ids are free. idShort 80/81 exist only on boards `640643a3…` and `65eb4ec5…`, not on ZM ROADMAP.
- **Drive/Docs/Sheets**: parents `d_cc3e9016…`, `d_bdf01b53…` and `d_cd7849ec…` are the root folders of Arthur, Oliver and Douglas, matching each item's owner. The 4 Drive ids, the doc id and the spreadsheet id (checked as both `drive_file_id` and `spreadsheet_id`) are free. Every owner and sharer is a Drive user. On readability:
  - The Google Doc has a `docs_documents` row with a 1,399-character body.
  - The Sheet has a spreadsheet row and 2 sheet rows with grids (8 and 4 rows). The key (`spreadsheet_id`, `sheet_id` 0/1) is composite and unique.
  - The other two items are folders.
- **Confluence**: `space_OPS`, parent `page_ops_home` and author `user_EMPLOYEE_0025` (Arthur Blake) exist. The 2 page ids, 2 titles and 2 version ids are free.
- **Gmail**: the 4 mailboxes (douglas, oliver.brooks, arthur.blake, leonard.hayes) exist. The 6 message ids are free in `/messages` of all 81,404 thread files. A complete text scan of all 81,404 files found no hit for the 6 thread numbers or the 2 Message-IDs. `history_id` is NULL on all 6 threads, which satisfies the contract.
- **Calendar**: all 5 calendars exist. The 5 event ids and the shared iCalUID are free.
- **One account per person**: no account is created in any service, and the lint's `identities` check passed.

### Check B detail

- NEW: an independent static parse found 404 statements: BEGIN, 402 INSERTs, COMMIT. Each INSERT has one VALUES tuple, equal column and value counts, no duplicate columns, and nothing between the tuple and `;`. No literal uses a cast, `DEFAULT` or a function.
- NEW, supported platform rules:
  - `slack.slack_messages.text_fts` and `gmail.gmail_messages.body_text_fts` are not set.
  - All Linear `created_at`/`updated_at` values match `YYYY-MM-DDTHH:MM:SSZ`.
  - There is no `linear_issues` INSERT, so `state_history_json` does not apply.
  - Every `*_json` literal parses, and the lint's `json_shape` check passed.
  - No NOT NULL column is omitted (lint `missing_required`).
- REUSED (revision-6 report §5 Check B; SQL columns are a byte-identical subset and the snapshot is unchanged): the snapshot comparison. `github_reviews.seq` and `linear_comments.sequence` are NOT COVERED. Both Confluence tables are absent from the snapshot. All other affected columns MATCH. These are advisory only.

### Check C detail

- NEW, **fixed clock**: no event timestamp is later than the clock. The latest is Slack `1e5d5d2b…` at 2025-09-30T21:12:44.508127Z. The only fields after it are plan fields or text: calendar events (start 2025-09-26T22:00Z) are in the past, and the go/no-go and Oct 10 beta are mentioned only in text.
- NEW, **effect of the deletion**: no remaining statement mentions ZOM-535, ZOM-504, `cmt_b61f9c6d…` or `cmt_c4fb570f…`. With the UPDATEs gone, those two issues keep their base `updated_at` and states, so nothing injected now conflicts with ZOM-535 (Todo) or ZOM-504 (Backlog). The remaining "0.3.132" mentions are on ZOM-536, ZOM-498, ZOM-555 and ZOM-561, all Done issues.
- NEW, **Linear**: all 77 comments are on issues in state Done. Each comment falls between the issue's `created_at` and its `completed_at`/`updated_at`. Each has `created_at` = `updated_at`, `is_edited` false, `parent_id` NULL and `sequence` 1, with one comment per issue. Every comment that cites `match3d-backend#N` comes after that PR's merge.
- NEW, **GitHub internal consistency** (programmatic, 0 issues):
  - Head commit authored ≤ PR created.
  - Comments, reviews and timeline events fall inside each PR's created→updated window.
  - `merged_at` = `closed_at`, state closed.
  - The `head_ref` branch exists, and branch head = PR head = PR-commit row.
  - Review `commit_id` = head SHA.
- NEW, **Slack**: every `ts` equals `created_at` to the microsecond. Both replies (02:05:51, 02:07:12) follow the parent (01:40:33), and the parent's `latest_reply` equals the last reply's ts.
- NEW, **Trello**: the ObjectId timestamps equal the stated times. The cards were created at 17:20:41 and 17:34:09, matching their createCard actions. The comment action at 2025-09-30T15:05:27Z equals card 80's `dateLastActivity`.
- NEW, **Gmail/Calendar**: `internal_date` = `date` for all 6 messages. Each sender has a SENT copy and each recipient an INBOX copy. All 5 calendar copies have created 09-22 ≤ updated 09-23 ≤ start 2025-09-26T22:00Z < end 22:30Z.
- NEW, **Confluence**: each version body equals its page body. Version 1 timestamps equal page `created_at`.
- REUSED (revision-6 report §5 Check C; statements byte-identical, base manifests unchanged):
  - The prod branch/cherry-pick sequence: #52 merged 2025-09-22 15:05 → cherry-pick 2025-09-30 18:05 → `prod:` comment 18:16 zm-api:57. It agrees with the deploy doc and the Prod deploys tab.
  - The deploy log's 7 rows match the PR `prod:` comments.
  - Reviews and comments each have exactly one matching timeline event.
  - The ZOM-457 comment matches the base parent/child hierarchy, and the ZOM-510 comment matches the Console & imports row.
  - The DD launch page and the Trello card desc introduce no contradiction.
  - Unapproved merges follow base practice (base #4, #6, #7).
  - Douglas's 09-22 DM, Oliver's 09-27 "all the server fixes … are on prod now" and the May 2025 page are stale context, and later records support that reading.

## 6. Findings

No demonstrated defect in A, B or C. Revision 7 only deletes the two ZOM-535/ZOM-504 comments and their UPDATEs and corrects the header count. Nothing remaining depended on them.

Advisories (optional; none changes the verdict):

1. **Cherry-pick author date (realism only)**, carried forward: `authored_date` on `c219e8c3…` is the pick time (2025-09-30T18:05Z), not the #52 author date, and `committed_date` is NULL, as in the base. This is not a demonstrated inconsistency.
2. **Snapshot columns not covered** (Check B, provisional): `github_reviews.seq` and `linear_comments.sequence`. If the platform load rejects either, drop it from every INSERT of that table.
3. **Confluence tables are not in the snapshot**, so their column names can't be compared offline. Disclosed limit only.

## 7. Evidence limits

- Required static checks: none unresolved.
- Outside certification scope (disclosed, not gates):
  - live execution and deployment success
  - current database compatibility (unverified snapshot; `seq`, `sequence` and both Confluence tables are not covered)
  - undocumented constraints
  - platform mapping of Slack `thread_ts_legacy` and of a non-PR branch head
  - search ranking
  - Agent visibility and persona access
  - task difficulty and discoverability (owned by `/prompt` and `/hardness`)
- Uniqueness is scoped to the local synth-cut base plus the SQL, not the live database.

## 8. Operation ledger (all 402 row operations, execution order)

BEGIN at line 5 and COMMIT at line 820 wrap these rows. Line = the line where the statement starts. "PASS" means every check listed for that row passed (§5 details). Removed rows from revision 6 (old ledger #403–#406) no longer exist.

| # | Line | Table | Op | Record / target | Key values | Checks |
|---|---|---|---|---|---|---|
| 1 | 7 | `gdrive.drive_files` | INSERT | `d_69fcebc484d472907b0b5c` | application/vnd.google-apps.folder, arthur.blake@harmonygames.co, 2025-09-29T17:12:30Z | A parent/owner/sharers resolve, id free; readable (folder/doc/sheet rows); C time ≤ clock: PASS |
| 2 | 9 | `gdrive.drive_files` | INSERT | `d_d71300168ca5dffa4db8b3` | application/vnd.google-apps.folder, oliver.brooks@harmonygames.co, 2025-09-29T17:05:02Z | A parent/owner/sharers resolve, id free; readable (folder/doc/sheet rows); C time ≤ clock: PASS |
| 3 | 11 | `gdrive.drive_files` | INSERT | `f_470ae81236d5bd39045dc1` | application/vnd.google-apps.document, douglas@harmonygames.co, 2025-06-01T18:30:00Z | A parent/owner/sharers resolve, id free; readable (folder/doc/sheet rows); C time ≤ clock: PASS |
| 4 | 13 | `gdrive.drive_files` | INSERT | `f_78bedc46245090a160d2dd` | application/vnd.google-apps.spreadsheet, douglas@harmonygames.co, 2025-08-25T12:05:00Z | A parent/owner/sharers resolve, id free; readable (folder/doc/sheet rows); C time ≤ clock: PASS |
| 5 | 16 | `gdocs.docs_documents` | INSERT | `f_470ae81236d5bd39045dc1` | douglas@harmonygames.co, 2025-09-25T16:40:00Z | A drive file in SQL, id free, body non-empty; C ≤ clock: PASS |
| 6 | 19 | `gsheets.sheets_spreadsheets` | INSERT | `f_78bedc46245090a160d2dd` | douglas@harmonygames.co, 2025-09-11T16:35:00Z | A drive file in SQL, id free; C ≤ clock: PASS |
| 7 | 21 | `gsheets.sheets_sheets` | INSERT | `f_78bedc46245090a160d2dd / sheet 0` | Prod deploys | A parent spreadsheet in SQL, composite key unique; B grid JSON list: PASS |
| 8 | 23 | `gsheets.sheets_sheets` | INSERT | `f_78bedc46245090a160d2dd / sheet 1` | Console & imports | A parent spreadsheet in SQL, composite key unique; B grid JSON list: PASS |
| 9 | 26 | `confluence.confluence_pages` | INSERT | `page_dd_launch_server_signoff` | space_OPS, page_ops_home, user_EMPLOYEE_0025, 2025-05-12T15:04:00Z | A space/parent/author resolve, id+title free; C ≤ clock: PASS |
| 10 | 28 | `confluence.confluence_page_versions` | INSERT | `ver_2ee4eb6acd67b53fc1013166dab4c1b5` | page_dd_launch_server_signoff, 1, 2025-05-12T15:04:00Z | A page in SQL, id free, body = page body; C ≤ clock: PASS |
| 11 | 30 | `confluence.confluence_pages` | INSERT | `page_zm_beta_oct10` | space_OPS, page_ops_home, user_EMPLOYEE_0025, 2025-09-29T17:15:00Z | A space/parent/author resolve, id+title free; C ≤ clock: PASS |
| 12 | 32 | `confluence.confluence_page_versions` | INSERT | `ver_338613da12d5a29e3e4947118c87f7ea` | page_zm_beta_oct10, 1, 2025-09-29T17:15:00Z | A page in SQL, id free, body = page body; C ≤ clock: PASS |
| 13 | 35 | `slack.slack_messages` | INSERT | `3a2e99ef807fc28ef39b8d6973a44427` | C0880U9751A, EMPLOYEE_0003_SLACK_ID, 1748450537.204611 | A channel/author (member) resolve, id+ts free; C ts = created_at, thread order: PASS |
| 14 | 37 | `slack.slack_messages` | INSERT | `9ba4f3770f458826c7503e1aa0992acc` | C0880U9751A, EMPLOYEE_0025_SLACK_ID, 1758295268.611352 | A channel/author (member) resolve, id+ts free; C ts = created_at, thread order: PASS |
| 15 | 39 | `slack.slack_messages` | INSERT | `f5dde99eaea0ac1773ca37e48871cb60` | D05QQF7V404, EMPLOYEE_0031_SLACK_ID, 1758571837.284511 | A channel/author (member) resolve, id+ts free; C ts = created_at, thread order: PASS |
| 16 | 41 | `slack.slack_messages` | INSERT | `10613025eb309bac6e0fb32438625484` | C0880U9751A, EMPLOYEE_0003_SLACK_ID, 1758991212.775031 | A channel/author (member) resolve, id+ts free; C ts = created_at, thread order: PASS |
| 17 | 43 | `slack.slack_messages` | INSERT | `42f263bfce69ae5a4ef068383ae66c4a` | C0880U9751A, EMPLOYEE_0003_SLACK_ID, 1759253506.093318 | A channel/author (member) resolve, id+ts free; C ts = created_at, thread order: PASS |
| 18 | 45 | `slack.slack_messages` | INSERT | `1e5d5d2bf50901f0d7376627d6f539e8` | D05QQF7V404, EMPLOYEE_0025_SLACK_ID, 1759266764.508127 | A channel/author (member) resolve, id+ts free; C ts = created_at, thread order: PASS |
| 19 | 47 | `slack.slack_messages` | INSERT | `81531d5f36d48a5d2028a22405aed65e` | C0880U9751A, EMPLOYEE_0031_SLACK_ID, 1758937233.118904 | A channel/author (member) resolve, id+ts free; C ts = created_at, thread order: PASS |
| 20 | 49 | `slack.slack_messages` | INSERT | `33339417b07ab83542fc971a41320a36` | C0880U9751A, EMPLOYEE_0025_SLACK_ID, 1758938751.402267, 81531d5f36d48a5d2028a22405aed65e | A channel/author (member) resolve, id+ts free; C ts = created_at, thread order: PASS |
| 21 | 51 | `slack.slack_messages` | INSERT | `bde0c0ff791441e66d57cdb2de8f0f51` | C0880U9751A, EMPLOYEE_0031_SLACK_ID, 1758938832.553908, 81531d5f36d48a5d2028a22405aed65e | A channel/author (member) resolve, id+ts free; C ts = created_at, thread order: PASS |
| 22 | 54 | `trello.trello_cards` | INSERT | `68dabfe9bc2e8b969782e22d` | 80, 6851a674975da1fe76e70d93, 2025-09-30T15:05:27Z | A board/list resolve, id free, idShort free on board; C ObjectId time: PASS |
| 23 | 56 | `trello.trello_actions` | INSERT | `68dabfe93a26ef2186dcec1c` | createCard, 68dabfe9bc2e8b969782e22d, 2025-09-29T17:20:41Z | A board/card/member resolve, id free; C ObjectId time = date: PASS |
| 24 | 58 | `trello.trello_cards` | INSERT | `68dac311754b38be05be7ea9` | 81, 6851a674975da1fe76e70d93, 2025-09-29T17:34:09Z | A board/list resolve, id free, idShort free on board; C ObjectId time: PASS |
| 25 | 60 | `trello.trello_actions` | INSERT | `68dac311a286768d02a6385d` | createCard, 68dac311754b38be05be7ea9, 2025-09-29T17:34:09Z | A board/card/member resolve, id free; C ObjectId time = date: PASS |
| 26 | 62 | `trello.trello_actions` | INSERT | `68dbf1b73eba0ba580f67a6e` | commentCard, 68dabfe9bc2e8b969782e22d, 2025-09-30T15:05:27Z | A board/card/member resolve, id free; C ObjectId time = date: PASS |
| 27 | 65 | `gmail.gmail_threads` | INSERT | `douglas@harmonygames.co/1844719216755416739` | douglas@harmonygames.co | A mailbox exists, thread no. free; history_id NULL: PASS |
| 28 | 67 | `gmail.gmail_messages` | INSERT | `douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com>` | douglas@harmonygames.co, arthur.blake@harmonygames.co, 2025-09-30T19:42:18Z | A thread in SQL, Message-ID free; C internal_date = date ≤ clock: PASS |
| 29 | 69 | `gmail.gmail_threads` | INSERT | `oliver.brooks@harmonygames.co/1844719216754885141` | oliver.brooks@harmonygames.co | A mailbox exists, thread no. free; history_id NULL: PASS |
| 30 | 71 | `gmail.gmail_messages` | INSERT | `oliver.brooks@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com>` | oliver.brooks@harmonygames.co, arthur.blake@harmonygames.co, 2025-09-30T19:42:18Z | A thread in SQL, Message-ID free; C internal_date = date ≤ clock: PASS |
| 31 | 73 | `gmail.gmail_threads` | INSERT | `arthur.blake@harmonygames.co/1844719216755483955` | arthur.blake@harmonygames.co | A mailbox exists, thread no. free; history_id NULL: PASS |
| 32 | 75 | `gmail.gmail_messages` | INSERT | `arthur.blake@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com>` | arthur.blake@harmonygames.co, arthur.blake@harmonygames.co, 2025-09-30T19:42:18Z | A thread in SQL, Message-ID free; C internal_date = date ≤ clock: PASS |
| 33 | 77 | `gmail.gmail_threads` | INSERT | `douglas@harmonygames.co/1844721277206562572` | douglas@harmonygames.co | A mailbox exists, thread no. free; history_id NULL: PASS |
| 34 | 79 | `gmail.gmail_messages` | INSERT | `douglas@harmonygames.co/<CAreN_3nXHn9vq-8FWgVQEC3_2hxsSjSNZRkPtWB@mail.gmail.com>` | douglas@harmonygames.co, leonard.hayes@harmonygames.co, 2025-09-30T20:15:03Z | A thread in SQL, Message-ID free; C internal_date = date ≤ clock: PASS |
| 35 | 81 | `gmail.gmail_threads` | INSERT | `arthur.blake@harmonygames.co/1844721277207387678` | arthur.blake@harmonygames.co | A mailbox exists, thread no. free; history_id NULL: PASS |
| 36 | 83 | `gmail.gmail_messages` | INSERT | `arthur.blake@harmonygames.co/<CAreN_3nXHn9vq-8FWgVQEC3_2hxsSjSNZRkPtWB@mail.gmail.com>` | arthur.blake@harmonygames.co, leonard.hayes@harmonygames.co, 2025-09-30T20:15:03Z | A thread in SQL, Message-ID free; C internal_date = date ≤ clock: PASS |
| 37 | 85 | `gmail.gmail_threads` | INSERT | `leonard.hayes@harmonygames.co/1844721277206833296` | leonard.hayes@harmonygames.co | A mailbox exists, thread no. free; history_id NULL: PASS |
| 38 | 87 | `gmail.gmail_messages` | INSERT | `leonard.hayes@harmonygames.co/<CAreN_3nXHn9vq-8FWgVQEC3_2hxsSjSNZRkPtWB@mail.gmail.com>` | leonard.hayes@harmonygames.co, leonard.hayes@harmonygames.co, 2025-09-30T20:15:03Z | A thread in SQL, Message-ID free; C internal_date = date ≤ clock: PASS |
| 39 | 90 | `gcal.gcal_events` | INSERT | `evt_b6eda0097a341f225ad5d2` | arthur.blake@harmonygames.co, 2025-09-26T22:00:00Z, 2025-09-22T14:02:00Z | A calendar exists, id free; C created ≤ updated ≤ start < end: PASS |
| 40 | 92 | `gcal.gcal_events` | INSERT | `evt_0f489eb7fb46ada9660881` | douglas@harmonygames.co, 2025-09-26T22:00:00Z, 2025-09-22T14:02:00Z | A calendar exists, id free; C created ≤ updated ≤ start < end: PASS |
| 41 | 94 | `gcal.gcal_events` | INSERT | `evt_e3c3cd6a8dec19d0e7b123` | oliver.brooks@harmonygames.co, 2025-09-26T22:00:00Z, 2025-09-22T14:02:00Z | A calendar exists, id free; C created ≤ updated ≤ start < end: PASS |
| 42 | 96 | `gcal.gcal_events` | INSERT | `evt_5e9adacd9af476a6402dfa` | owen.baker@harmonygames.co, 2025-09-26T22:00:00Z, 2025-09-22T14:02:00Z | A calendar exists, id free; C created ≤ updated ≤ start < end: PASS |
| 43 | 98 | `gcal.gcal_events` | INSERT | `evt_bbe10af026c7f633387e2d` | vincent.parker@harmonygames.co, 2025-09-26T22:00:00Z, 2025-09-22T14:02:00Z | A calendar exists, id free; C created ≤ updated ≤ start < end: PASS |
| 44 | 101 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#37` | 37, closed, PERSON_5760_GITHUB_USERNAME, 2025-08-21T15:20:00Z, 2025-08-25T09:10:00Z | A repo/logins resolve, id/number free, head in SQL; C chronology: PASS |
| 45 | 103 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:algo-levels-spawn-points-from-the-server` | algo-levels-spawn-points-from-the-server, d96ec79123c2d518760e6b9a2ccc6433f931c488 | A id/name free, head commit in SQL: PASS |
| 46 | 105 | `github.github_commits` | INSERT | `d96ec79123c2d518760e6b9a2ccc6433f931c488` | PERSON_5760_GITHUB_USERNAME, 2025-08-21T15:00:00Z | A sha free, login resolves; C ≤ clock: PASS |
| 47 | 107 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#37#c_0` | harmonygames-Games/match3d-backend#37, d96ec79123c2d518760e6b9a2ccc6433f931c488 | A PR+commit in SQL = head, id free: PASS |
| 48 | 109 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#37#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-08-21T15:22:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 49 | 111 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#37#c_2` | PERSON_2967_GITHUB_USERNAME, 2025-08-25T11:52:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 50 | 113 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#37#rev_1` | PERSON_6026_GITHUB_USERNAME, COMMENTED, 2025-08-21T15:26:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 51 | 115 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#37#rev_2` | PERSON_2967_GITHUB_USERNAME, APPROVED, 2025-08-25T09:00:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 52 | 117 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#37#ev_1` | review_requested, PERSON_5760_GITHUB_USERNAME, 2025-08-21T15:20:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 53 | 119 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#37#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-08-21T15:22:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 54 | 121 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#37#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-08-21T15:26:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 55 | 123 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#37#ev_4` | reviewed, PERSON_2967_GITHUB_USERNAME, 2025-08-25T09:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 56 | 125 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#37#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-08-25T09:10:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 57 | 127 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#37#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-08-25T09:10:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 58 | 129 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#37#ev_7` | commented, PERSON_2967_GITHUB_USERNAME, 2025-08-25T11:52:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 59 | 131 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#38` | 38, closed, PERSON_5760_GITHUB_USERNAME, 2025-08-22T15:10:00Z, 2025-08-25T09:30:00Z | A repo/logins resolve, id/number free, head in SQL; C chronology: PASS |
| 60 | 133 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:plague-race-count-algo-levels` | plague-race-count-algo-levels, b1388ff2f8d945f005ea87b236afbab0c14e6e64 | A id/name free, head commit in SQL: PASS |
| 61 | 135 | `github.github_commits` | INSERT | `b1388ff2f8d945f005ea87b236afbab0c14e6e64` | PERSON_5760_GITHUB_USERNAME, 2025-08-22T14:50:00Z | A sha free, login resolves; C ≤ clock: PASS |
| 62 | 137 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#38#c_0` | harmonygames-Games/match3d-backend#38, b1388ff2f8d945f005ea87b236afbab0c14e6e64 | A PR+commit in SQL = head, id free: PASS |
| 63 | 139 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#38#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-08-22T15:12:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 64 | 141 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#38#c_2` | PERSON_2967_GITHUB_USERNAME, 2025-08-25T11:52:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 65 | 143 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#38#rev_1` | PERSON_6026_GITHUB_USERNAME, COMMENTED, 2025-08-22T15:16:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 66 | 145 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#38#rev_2` | PERSON_2967_GITHUB_USERNAME, APPROVED, 2025-08-25T09:20:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 67 | 147 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#38#ev_1` | review_requested, PERSON_5760_GITHUB_USERNAME, 2025-08-22T15:10:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 68 | 149 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#38#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-08-22T15:12:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 69 | 151 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#38#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-08-22T15:16:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 70 | 153 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#38#ev_4` | reviewed, PERSON_2967_GITHUB_USERNAME, 2025-08-25T09:20:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 71 | 155 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#38#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-08-25T09:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 72 | 157 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#38#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-08-25T09:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 73 | 159 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#38#ev_7` | commented, PERSON_2967_GITHUB_USERNAME, 2025-08-25T11:52:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 74 | 161 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#39` | 39, closed, PERSON_2967_GITHUB_USERNAME, 2025-08-29T13:00:00Z, 2025-09-02T15:40:00Z | A repo/logins resolve, id/number free, head in SQL; C chronology: PASS |
| 75 | 163 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:trophy-path-container-headlines-config` | trophy-path-container-headlines-config, 48153d42da95f5824fe53b669b0ab027f2cfe9a0 | A id/name free, head commit in SQL: PASS |
| 76 | 165 | `github.github_commits` | INSERT | `48153d42da95f5824fe53b669b0ab027f2cfe9a0` | PERSON_2967_GITHUB_USERNAME, 2025-08-29T12:40:00Z | A sha free, login resolves; C ≤ clock: PASS |
| 77 | 167 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#39#c_0` | harmonygames-Games/match3d-backend#39, 48153d42da95f5824fe53b669b0ab027f2cfe9a0 | A PR+commit in SQL = head, id free: PASS |
| 78 | 169 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#39#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-08-29T13:02:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 79 | 171 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#39#c_2` | PERSON_2967_GITHUB_USERNAME, 2025-09-02T17:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 80 | 173 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#39#rev_1` | PERSON_6026_GITHUB_USERNAME, COMMENTED, 2025-08-29T13:06:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 81 | 175 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#39#rev_2` | PERSON_5760_GITHUB_USERNAME, APPROVED, 2025-09-02T15:20:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 82 | 177 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#39#ev_1` | review_requested, PERSON_2967_GITHUB_USERNAME, 2025-08-29T13:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 83 | 179 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#39#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-08-29T13:02:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 84 | 181 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#39#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-08-29T13:06:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 85 | 183 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#39#ev_4` | reviewed, PERSON_5760_GITHUB_USERNAME, 2025-09-02T15:20:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 86 | 185 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#39#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-02T15:40:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 87 | 187 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#39#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-02T15:40:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 88 | 189 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#39#ev_7` | commented, PERSON_2967_GITHUB_USERNAME, 2025-09-02T17:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 89 | 191 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#40` | 40, closed, PERSON_2967_GITHUB_USERNAME, 2025-09-01T10:15:00Z, 2025-09-02T18:20:00Z | A repo/logins resolve, id/number free, head in SQL; C chronology: PASS |
| 90 | 193 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:items-make-the-cooler-a-usable-item` | items-make-the-cooler-a-usable-item, 334b4ed82b283bca22b8f218f389a9c834789745 | A id/name free, head commit in SQL: PASS |
| 91 | 195 | `github.github_commits` | INSERT | `334b4ed82b283bca22b8f218f389a9c834789745` | PERSON_2967_GITHUB_USERNAME, 2025-09-01T09:55:00Z | A sha free, login resolves; C ≤ clock: PASS |
| 92 | 197 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#40#c_0` | harmonygames-Games/match3d-backend#40, 334b4ed82b283bca22b8f218f389a9c834789745 | A PR+commit in SQL = head, id free: PASS |
| 93 | 199 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#40#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-01T10:17:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 94 | 201 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#40#c_2` | PERSON_2967_GITHUB_USERNAME, 2025-09-02T18:40:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 95 | 203 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#40#rev_1` | PERSON_6026_GITHUB_USERNAME, COMMENTED, 2025-09-01T10:21:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 96 | 205 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#40#ev_1` | review_requested, PERSON_2967_GITHUB_USERNAME, 2025-09-01T10:15:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 97 | 207 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#40#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-01T10:17:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 98 | 209 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#40#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-01T10:21:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 99 | 211 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#40#ev_4` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-02T18:20:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 100 | 213 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#40#ev_5` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-02T18:20:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 101 | 215 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#40#ev_6` | commented, PERSON_2967_GITHUB_USERNAME, 2025-09-02T18:40:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 102 | 217 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#41` | 41, closed, PERSON_5760_GITHUB_USERNAME, 2025-09-01T19:40:00Z, 2025-09-03T16:00:00Z | A repo/logins resolve, id/number free, head in SQL; C chronology: PASS |
| 103 | 219 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:algo-levels-100-seed-endpoint` | algo-levels-100-seed-endpoint, 61e10e32a992a316e9f01836c6d1d12fff65868a | A id/name free, head commit in SQL: PASS |
| 104 | 221 | `github.github_commits` | INSERT | `61e10e32a992a316e9f01836c6d1d12fff65868a` | PERSON_5760_GITHUB_USERNAME, 2025-09-01T19:20:00Z | A sha free, login resolves; C ≤ clock: PASS |
| 105 | 223 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#41#c_0` | harmonygames-Games/match3d-backend#41, 61e10e32a992a316e9f01836c6d1d12fff65868a | A PR+commit in SQL = head, id free: PASS |
| 106 | 225 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#41#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-01T19:42:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 107 | 227 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#41#c_2` | PERSON_5760_GITHUB_USERNAME, 2025-09-03T16:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 108 | 229 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#41#rev_1` | PERSON_6026_GITHUB_USERNAME, COMMENTED, 2025-09-01T19:46:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 109 | 231 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#41#rev_2` | PERSON_2967_GITHUB_USERNAME, APPROVED, 2025-09-03T18:05:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 110 | 233 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#41#ev_1` | review_requested, PERSON_5760_GITHUB_USERNAME, 2025-09-01T19:40:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 111 | 235 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#41#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-01T19:42:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 112 | 237 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#41#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-01T19:46:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 113 | 239 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#41#ev_4` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-03T16:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 114 | 241 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#41#ev_5` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-03T16:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 115 | 243 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#41#ev_6` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-03T16:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 116 | 245 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#41#ev_7` | reviewed, PERSON_2967_GITHUB_USERNAME, 2025-09-03T18:05:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 117 | 247 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#42` | 42, closed, PERSON_5760_GITHUB_USERNAME, 2025-09-03T15:00:00Z, 2025-09-05T16:00:00Z | A repo/logins resolve, id/number free, head in SQL; C chronology: PASS |
| 118 | 249 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:teams-ack-lives-gift` | teams-ack-lives-gift, 250e1846dd3f0770eddcb32a8ba25d32a5c33260 | A id/name free, head commit in SQL: PASS |
| 119 | 251 | `github.github_commits` | INSERT | `250e1846dd3f0770eddcb32a8ba25d32a5c33260` | PERSON_5760_GITHUB_USERNAME, 2025-09-03T14:40:00Z | A sha free, login resolves; C ≤ clock: PASS |
| 120 | 253 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#42#c_0` | harmonygames-Games/match3d-backend#42, 250e1846dd3f0770eddcb32a8ba25d32a5c33260 | A PR+commit in SQL = head, id free: PASS |
| 121 | 255 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#42#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-03T15:02:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 122 | 257 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#42#c_2` | PERSON_5760_GITHUB_USERNAME, 2025-09-08T17:18:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 123 | 259 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#42#rev_1` | PERSON_6026_GITHUB_USERNAME, COMMENTED, 2025-09-03T15:06:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 124 | 261 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#42#rev_2` | PERSON_2967_GITHUB_USERNAME, APPROVED, 2025-09-05T15:30:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 125 | 263 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#42#ev_1` | review_requested, PERSON_5760_GITHUB_USERNAME, 2025-09-03T15:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 126 | 265 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#42#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-03T15:02:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 127 | 267 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#42#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-03T15:06:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 128 | 269 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#42#ev_4` | reviewed, PERSON_2967_GITHUB_USERNAME, 2025-09-05T15:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 129 | 271 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#42#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-05T16:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 130 | 273 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#42#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-05T16:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 131 | 275 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#42#ev_7` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-08T17:18:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 132 | 277 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#43` | 43, closed, PERSON_2967_GITHUB_USERNAME, 2025-09-04T11:10:00Z, 2025-09-04T12:30:00Z | A repo/logins resolve, id/number free, head in SQL; C chronology: PASS |
| 133 | 279 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:inventory-drop-non-card-items-from-equip` | inventory-drop-non-card-items-from-equip, 7d24459d1307b6ab594e52cdc5633d002a08d54b | A id/name free, head commit in SQL: PASS |
| 134 | 281 | `github.github_commits` | INSERT | `7d24459d1307b6ab594e52cdc5633d002a08d54b` | PERSON_2967_GITHUB_USERNAME, 2025-09-04T10:50:00Z | A sha free, login resolves; C ≤ clock: PASS |
| 135 | 283 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#43#c_0` | harmonygames-Games/match3d-backend#43, 7d24459d1307b6ab594e52cdc5633d002a08d54b | A PR+commit in SQL = head, id free: PASS |
| 136 | 285 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#43#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-04T11:12:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 137 | 287 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#43#c_2` | PERSON_2967_GITHUB_USERNAME, 2025-09-04T12:50:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 138 | 289 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#43#rev_1` | PERSON_6026_GITHUB_USERNAME, COMMENTED, 2025-09-04T11:16:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 139 | 291 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#43#ev_1` | review_requested, PERSON_2967_GITHUB_USERNAME, 2025-09-04T11:10:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 140 | 293 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#43#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-04T11:12:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 141 | 295 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#43#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-04T11:16:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 142 | 297 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#43#ev_4` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-04T12:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 143 | 299 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#43#ev_5` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-04T12:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 144 | 301 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#43#ev_6` | commented, PERSON_2967_GITHUB_USERNAME, 2025-09-04T12:50:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 145 | 303 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#44` | 44, closed, PERSON_2967_GITHUB_USERNAME, 2025-09-04T22:00:00Z, 2025-09-08T15:30:00Z | A repo/logins resolve, id/number free, head in SQL; C chronology: PASS |
| 146 | 305 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:profile-other-players-profile-v2` | profile-other-players-profile-v2, b3ca856157e0fffa2ae28e9701ef4872205bc6f8 | A id/name free, head commit in SQL: PASS |
| 147 | 307 | `github.github_commits` | INSERT | `b3ca856157e0fffa2ae28e9701ef4872205bc6f8` | PERSON_2967_GITHUB_USERNAME, 2025-09-04T21:40:00Z | A sha free, login resolves; C ≤ clock: PASS |
| 148 | 309 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#44#c_0` | harmonygames-Games/match3d-backend#44, b3ca856157e0fffa2ae28e9701ef4872205bc6f8 | A PR+commit in SQL = head, id free: PASS |
| 149 | 311 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#44#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-04T22:02:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 150 | 313 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#44#c_2` | PERSON_5760_GITHUB_USERNAME, 2025-09-08T17:18:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 151 | 315 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#44#c_3` | PERSON_2967_GITHUB_USERNAME, 2025-09-20T02:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 152 | 317 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#44#c_4` | PERSON_2967_GITHUB_USERNAME, 2025-09-22T17:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 153 | 319 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#44#rev_1` | PERSON_6026_GITHUB_USERNAME, COMMENTED, 2025-09-04T22:06:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 154 | 321 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#44#rev_2` | PERSON_5760_GITHUB_USERNAME, CHANGES_REQUESTED, 2025-09-05T16:00:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 155 | 323 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#44#rev_3` | PERSON_5760_GITHUB_USERNAME, APPROVED, 2025-09-08T15:10:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 156 | 325 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#44#ev_1` | review_requested, PERSON_2967_GITHUB_USERNAME, 2025-09-04T22:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 157 | 327 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#44#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-04T22:02:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 158 | 329 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#44#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-04T22:06:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 159 | 331 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#44#ev_4` | reviewed, PERSON_5760_GITHUB_USERNAME, 2025-09-05T16:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 160 | 333 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#44#ev_5` | reviewed, PERSON_5760_GITHUB_USERNAME, 2025-09-08T15:10:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 161 | 335 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#44#ev_6` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-08T15:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 162 | 337 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#44#ev_7` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-08T15:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 163 | 339 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#44#ev_8` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-08T17:18:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 164 | 341 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#44#ev_9` | commented, PERSON_2967_GITHUB_USERNAME, 2025-09-20T02:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 165 | 343 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#44#ev_10` | commented, PERSON_2967_GITHUB_USERNAME, 2025-09-22T17:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 166 | 345 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#45` | 45, closed, PERSON_5760_GITHUB_USERNAME, 2025-09-08T15:10:00Z, 2025-09-10T16:00:00Z | A repo/logins resolve, id/number free, head in SQL; C chronology: PASS |
| 167 | 347 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:inventory-keep-equipped-slots-across-ses` | inventory-keep-equipped-slots-across-ses, 46dc449026428308b2f3e48d0b88f039153a9aed | A id/name free, head commit in SQL: PASS |
| 168 | 349 | `github.github_commits` | INSERT | `46dc449026428308b2f3e48d0b88f039153a9aed` | PERSON_5760_GITHUB_USERNAME, 2025-09-08T14:50:00Z | A sha free, login resolves; C ≤ clock: PASS |
| 169 | 351 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#45#c_0` | harmonygames-Games/match3d-backend#45, 46dc449026428308b2f3e48d0b88f039153a9aed | A PR+commit in SQL = head, id free: PASS |
| 170 | 353 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#45#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-08T15:12:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 171 | 355 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#45#c_2` | PERSON_5760_GITHUB_USERNAME, 2025-09-10T18:20:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 172 | 357 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#45#rev_1` | PERSON_6026_GITHUB_USERNAME, COMMENTED, 2025-09-08T15:16:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 173 | 359 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#45#rev_2` | PERSON_2967_GITHUB_USERNAME, CHANGES_REQUESTED, 2025-09-09T17:00:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 174 | 361 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#45#rev_3` | PERSON_2967_GITHUB_USERNAME, APPROVED, 2025-09-10T15:10:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 175 | 363 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#45#ev_1` | review_requested, PERSON_5760_GITHUB_USERNAME, 2025-09-08T15:10:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 176 | 365 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#45#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-08T15:12:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 177 | 367 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#45#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-08T15:16:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 178 | 369 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#45#ev_4` | reviewed, PERSON_2967_GITHUB_USERNAME, 2025-09-09T17:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 179 | 371 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#45#ev_5` | reviewed, PERSON_2967_GITHUB_USERNAME, 2025-09-10T15:10:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 180 | 373 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#45#ev_6` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-10T16:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 181 | 375 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#45#ev_7` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-10T16:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 182 | 377 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#45#ev_8` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-10T18:20:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 183 | 379 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#46` | 46, closed, PERSON_5760_GITHUB_USERNAME, 2025-09-09T15:30:00Z, 2025-09-09T19:50:00Z | A repo/logins resolve, id/number free, head in SQL; C chronology: PASS |
| 184 | 381 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:economy-september-adjustments` | economy-september-adjustments, 9bdbc503b5894db868b678fc822b2b70994af699 | A id/name free, head commit in SQL: PASS |
| 185 | 383 | `github.github_commits` | INSERT | `9bdbc503b5894db868b678fc822b2b70994af699` | PERSON_5760_GITHUB_USERNAME, 2025-09-09T15:10:00Z | A sha free, login resolves; C ≤ clock: PASS |
| 186 | 385 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#46#c_0` | harmonygames-Games/match3d-backend#46, 9bdbc503b5894db868b678fc822b2b70994af699 | A PR+commit in SQL = head, id free: PASS |
| 187 | 387 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#46#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-09T15:32:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 188 | 389 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#46#c_2` | PERSON_5760_GITHUB_USERNAME, 2025-09-09T20:29:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 189 | 391 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#46#rev_1` | PERSON_6026_GITHUB_USERNAME, COMMENTED, 2025-09-09T15:36:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 190 | 393 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#46#rev_2` | EMPLOYEE_0025_GITHUB_USERNAME, APPROVED, 2025-09-09T19:40:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 191 | 395 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#46#ev_1` | review_requested, PERSON_5760_GITHUB_USERNAME, 2025-09-09T15:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 192 | 397 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#46#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-09T15:32:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 193 | 399 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#46#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-09T15:36:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 194 | 401 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#46#ev_4` | reviewed, EMPLOYEE_0025_GITHUB_USERNAME, 2025-09-09T19:40:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 195 | 403 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#46#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-09T19:50:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 196 | 405 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#46#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-09T19:50:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 197 | 407 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#46#ev_7` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-09T20:29:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 198 | 409 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#47` | 47, closed, PERSON_2967_GITHUB_USERNAME, 2025-09-11T17:00:00Z, 2025-09-12T19:00:00Z | A repo/logins resolve, id/number free, head in SQL; C chronology: PASS |
| 199 | 411 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:analytics-log-endless-start-on-the-serve` | analytics-log-endless-start-on-the-serve, a0bdcab8e1b7b11ba1f04fec44b5c7bbd8d9a5d5 | A id/name free, head commit in SQL: PASS |
| 200 | 413 | `github.github_commits` | INSERT | `a0bdcab8e1b7b11ba1f04fec44b5c7bbd8d9a5d5` | PERSON_2967_GITHUB_USERNAME, 2025-09-11T16:40:00Z | A sha free, login resolves; C ≤ clock: PASS |
| 201 | 415 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#47#c_0` | harmonygames-Games/match3d-backend#47, a0bdcab8e1b7b11ba1f04fec44b5c7bbd8d9a5d5 | A PR+commit in SQL = head, id free: PASS |
| 202 | 417 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#47#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-11T17:02:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 203 | 419 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#47#c_2` | PERSON_2967_GITHUB_USERNAME, 2025-09-27T16:20:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 204 | 421 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#47#rev_1` | PERSON_6026_GITHUB_USERNAME, COMMENTED, 2025-09-11T17:06:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 205 | 423 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#47#rev_2` | EMPLOYEE_0025_GITHUB_USERNAME, APPROVED, 2025-09-27T16:05:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 206 | 425 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#47#ev_1` | review_requested, PERSON_2967_GITHUB_USERNAME, 2025-09-11T17:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 207 | 427 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#47#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-11T17:02:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 208 | 429 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#47#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-11T17:06:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 209 | 431 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#47#ev_4` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-12T19:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 210 | 433 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#47#ev_5` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-12T19:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 211 | 435 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#47#ev_6` | reviewed, EMPLOYEE_0025_GITHUB_USERNAME, 2025-09-27T16:05:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 212 | 437 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#47#ev_7` | commented, PERSON_2967_GITHUB_USERNAME, 2025-09-27T16:20:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 213 | 439 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#48` | 48, closed, PERSON_2967_GITHUB_USERNAME, 2025-09-15T13:00:00Z, 2025-09-16T15:40:00Z | A repo/logins resolve, id/number free, head in SQL; C chronology: PASS |
| 214 | 441 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:boss-arena-infinite-hp-event-config` | boss-arena-infinite-hp-event-config, e2999966670177f4f4644569bf44541e7806eea6 | A id/name free, head commit in SQL: PASS |
| 215 | 443 | `github.github_commits` | INSERT | `e2999966670177f4f4644569bf44541e7806eea6` | PERSON_2967_GITHUB_USERNAME, 2025-09-15T12:40:00Z | A sha free, login resolves; C ≤ clock: PASS |
| 216 | 445 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#48#c_0` | harmonygames-Games/match3d-backend#48, e2999966670177f4f4644569bf44541e7806eea6 | A PR+commit in SQL = head, id free: PASS |
| 217 | 447 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#48#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-15T13:02:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 218 | 449 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#48#c_2` | PERSON_5760_GITHUB_USERNAME, 2025-09-16T16:35:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 219 | 451 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#48#rev_1` | PERSON_6026_GITHUB_USERNAME, COMMENTED, 2025-09-15T13:06:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 220 | 453 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#48#rev_2` | PERSON_5760_GITHUB_USERNAME, APPROVED, 2025-09-16T15:20:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 221 | 455 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#48#ev_1` | review_requested, PERSON_2967_GITHUB_USERNAME, 2025-09-15T13:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 222 | 457 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#48#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-15T13:02:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 223 | 459 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#48#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-15T13:06:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 224 | 461 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#48#ev_4` | reviewed, PERSON_5760_GITHUB_USERNAME, 2025-09-16T15:20:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 225 | 463 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#48#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-16T15:40:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 226 | 465 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#48#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-16T15:40:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 227 | 467 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#48#ev_7` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-16T16:35:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 228 | 469 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#49` | 49, closed, PERSON_5760_GITHUB_USERNAME, 2025-09-16T19:00:00Z, 2025-09-17T15:30:00Z | A repo/logins resolve, id/number free, head in SQL; C chronology: PASS |
| 229 | 471 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:boss-arena-mirror-balance-values` | boss-arena-mirror-balance-values, 1a12a54aec100ae0603bed4310dc12f3ec431aec | A id/name free, head commit in SQL: PASS |
| 230 | 473 | `github.github_commits` | INSERT | `1a12a54aec100ae0603bed4310dc12f3ec431aec` | PERSON_5760_GITHUB_USERNAME, 2025-09-16T18:40:00Z | A sha free, login resolves; C ≤ clock: PASS |
| 231 | 475 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#49#c_0` | harmonygames-Games/match3d-backend#49, 1a12a54aec100ae0603bed4310dc12f3ec431aec | A PR+commit in SQL = head, id free: PASS |
| 232 | 477 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#49#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-16T19:02:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 233 | 479 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#49#c_2` | PERSON_5760_GITHUB_USERNAME, 2025-09-18T16:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 234 | 481 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#49#rev_1` | PERSON_6026_GITHUB_USERNAME, COMMENTED, 2025-09-16T19:06:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 235 | 483 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#49#rev_2` | PERSON_2967_GITHUB_USERNAME, APPROVED, 2025-09-17T15:10:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 236 | 485 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#49#ev_1` | review_requested, PERSON_5760_GITHUB_USERNAME, 2025-09-16T19:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 237 | 487 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#49#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-16T19:02:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 238 | 489 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#49#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-16T19:06:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 239 | 491 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#49#ev_4` | reviewed, PERSON_2967_GITHUB_USERNAME, 2025-09-17T15:10:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 240 | 493 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#49#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-17T15:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 241 | 495 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#49#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-17T15:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 242 | 497 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#49#ev_7` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-18T16:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 243 | 499 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#50` | 50, closed, PERSON_2967_GITHUB_USERNAME, 2025-09-18T15:00:00Z, 2025-09-19T15:30:00Z | A repo/logins resolve, id/number free, head in SQL; C chronology: PASS |
| 244 | 501 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:boss-arena-don-t-take-a-life-on-a-win` | boss-arena-don-t-take-a-life-on-a-win, 789f238dc36a0e3c363244a78144494fa406c839 | A id/name free, head commit in SQL: PASS |
| 245 | 503 | `github.github_commits` | INSERT | `789f238dc36a0e3c363244a78144494fa406c839` | PERSON_2967_GITHUB_USERNAME, 2025-09-18T14:40:00Z | A sha free, login resolves; C ≤ clock: PASS |
| 246 | 505 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#50#c_0` | harmonygames-Games/match3d-backend#50, 789f238dc36a0e3c363244a78144494fa406c839 | A PR+commit in SQL = head, id free: PASS |
| 247 | 507 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#50#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-18T15:02:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 248 | 509 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#50#c_2` | PERSON_2967_GITHUB_USERNAME, 2025-09-27T14:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 249 | 511 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#50#rev_1` | PERSON_6026_GITHUB_USERNAME, COMMENTED, 2025-09-18T15:06:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 250 | 513 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#50#rev_2` | PERSON_5760_GITHUB_USERNAME, APPROVED, 2025-09-19T15:10:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 251 | 515 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#50#rev_3` | EMPLOYEE_0025_GITHUB_USERNAME, COMMENTED, 2025-09-29T14:50:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 252 | 517 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#50#ev_1` | review_requested, PERSON_2967_GITHUB_USERNAME, 2025-09-18T15:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 253 | 519 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#50#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-18T15:02:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 254 | 521 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#50#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-18T15:06:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 255 | 523 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#50#ev_4` | reviewed, PERSON_5760_GITHUB_USERNAME, 2025-09-19T15:10:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 256 | 525 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#50#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-19T15:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 257 | 527 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#50#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-19T15:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 258 | 529 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#50#ev_7` | commented, PERSON_2967_GITHUB_USERNAME, 2025-09-27T14:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 259 | 531 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#50#ev_8` | reviewed, EMPLOYEE_0025_GITHUB_USERNAME, 2025-09-29T14:50:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 260 | 533 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#51` | 51, closed, PERSON_5760_GITHUB_USERNAME, 2025-09-18T20:00:00Z, 2025-09-19T22:00:00Z | A repo/logins resolve, id/number free, head in SQL; C chronology: PASS |
| 261 | 535 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:trophy-path-ignore-duplicate-claim-reque` | trophy-path-ignore-duplicate-claim-reque, e737b6e6064a0e19d4ab43a383826bc7d1e2e98e | A id/name free, head commit in SQL: PASS |
| 262 | 537 | `github.github_commits` | INSERT | `e737b6e6064a0e19d4ab43a383826bc7d1e2e98e` | PERSON_5760_GITHUB_USERNAME, 2025-09-18T19:40:00Z | A sha free, login resolves; C ≤ clock: PASS |
| 263 | 539 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#51#c_0` | harmonygames-Games/match3d-backend#51, e737b6e6064a0e19d4ab43a383826bc7d1e2e98e | A PR+commit in SQL = head, id free: PASS |
| 264 | 541 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#51#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-18T20:02:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 265 | 543 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#51#c_2` | PERSON_5760_GITHUB_USERNAME, 2025-09-19T22:20:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 266 | 545 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#51#c_3` | EMPLOYEE_0012_GITHUB_USERNAME, 2025-09-22T09:14:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 267 | 547 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#51#rev_1` | PERSON_6026_GITHUB_USERNAME, COMMENTED, 2025-09-18T20:06:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 268 | 549 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#51#rev_2` | PERSON_2967_GITHUB_USERNAME, APPROVED, 2025-09-19T21:30:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 269 | 551 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#51#ev_1` | review_requested, PERSON_5760_GITHUB_USERNAME, 2025-09-18T20:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 270 | 553 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#51#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-18T20:02:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 271 | 555 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#51#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-18T20:06:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 272 | 557 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#51#ev_4` | reviewed, PERSON_2967_GITHUB_USERNAME, 2025-09-19T21:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 273 | 559 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#51#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-19T22:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 274 | 561 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#51#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-19T22:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 275 | 563 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#51#ev_7` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-19T22:20:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 276 | 565 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#51#ev_8` | commented, EMPLOYEE_0012_GITHUB_USERNAME, 2025-09-22T09:14:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 277 | 567 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#52` | 52, closed, PERSON_5760_GITHUB_USERNAME, 2025-09-22T12:10:00Z, 2025-09-22T15:05:00Z | A repo/logins resolve, id/number free, head in SQL; C chronology: PASS |
| 278 | 569 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:teams-push-lives-refresh-to-client` | teams-push-lives-refresh-to-client, 9caa48b0aaac58c23661589a23c048e37bafbfed | A id/name free, head commit in SQL: PASS |
| 279 | 571 | `github.github_commits` | INSERT | `9caa48b0aaac58c23661589a23c048e37bafbfed` | PERSON_5760_GITHUB_USERNAME, 2025-09-22T11:50:00Z | A sha free, login resolves; C ≤ clock: PASS |
| 280 | 573 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#52#c_0` | harmonygames-Games/match3d-backend#52, 9caa48b0aaac58c23661589a23c048e37bafbfed | A PR+commit in SQL = head, id free: PASS |
| 281 | 575 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#52#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-22T12:12:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 282 | 577 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#52#c_2` | PERSON_5760_GITHUB_USERNAME, 2025-09-30T18:16:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 283 | 579 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#52#rev_1` | PERSON_6026_GITHUB_USERNAME, COMMENTED, 2025-09-22T12:16:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 284 | 581 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#52#rev_2` | PERSON_2967_GITHUB_USERNAME, APPROVED, 2025-09-22T14:50:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 285 | 583 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#52#ev_1` | review_requested, PERSON_5760_GITHUB_USERNAME, 2025-09-22T12:10:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 286 | 585 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#52#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-22T12:12:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 287 | 587 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#52#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-22T12:16:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 288 | 589 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#52#ev_4` | reviewed, PERSON_2967_GITHUB_USERNAME, 2025-09-22T14:50:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 289 | 591 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#52#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-22T15:05:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 290 | 593 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#52#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-22T15:05:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 291 | 595 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#52#ev_7` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-30T18:16:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 292 | 597 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#53` | 53, closed, PERSON_5760_GITHUB_USERNAME, 2025-09-22T16:00:00Z, 2025-09-23T15:30:00Z | A repo/logins resolve, id/number free, head in SQL; C chronology: PASS |
| 293 | 599 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:boss-arena-mirror-refill-and-nuke-values` | boss-arena-mirror-refill-and-nuke-values, 51677370b7a345efc26e88b7576890fa5c7d0419 | A id/name free, head commit in SQL: PASS |
| 294 | 601 | `github.github_commits` | INSERT | `51677370b7a345efc26e88b7576890fa5c7d0419` | PERSON_5760_GITHUB_USERNAME, 2025-09-22T15:40:00Z | A sha free, login resolves; C ≤ clock: PASS |
| 295 | 603 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#53#c_0` | harmonygames-Games/match3d-backend#53, 51677370b7a345efc26e88b7576890fa5c7d0419 | A PR+commit in SQL = head, id free: PASS |
| 296 | 605 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#53#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-22T16:02:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 297 | 607 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#53#c_2` | PERSON_5760_GITHUB_USERNAME, 2025-09-24T16:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 298 | 609 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#53#rev_1` | PERSON_6026_GITHUB_USERNAME, COMMENTED, 2025-09-22T16:06:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 299 | 611 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#53#rev_2` | PERSON_2967_GITHUB_USERNAME, APPROVED, 2025-09-23T15:15:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 300 | 613 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#53#ev_1` | review_requested, PERSON_5760_GITHUB_USERNAME, 2025-09-22T16:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 301 | 615 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#53#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-22T16:02:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 302 | 617 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#53#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-22T16:06:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 303 | 619 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#53#ev_4` | reviewed, PERSON_2967_GITHUB_USERNAME, 2025-09-23T15:15:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 304 | 621 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#53#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-23T15:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 305 | 623 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#53#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-23T15:30:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 306 | 625 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#53#ev_7` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-24T16:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 307 | 627 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#54` | 54, closed, PERSON_5760_GITHUB_USERNAME, 2025-09-22T18:00:00Z, 2025-09-23T16:00:00Z | A repo/logins resolve, id/number free, head in SQL; C chronology: PASS |
| 308 | 629 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:login-streak-count-days-in-player-timezo` | login-streak-count-days-in-player-timezo, d0a473f0607318375786577d523bf5972f502c2c | A id/name free, head commit in SQL: PASS |
| 309 | 631 | `github.github_commits` | INSERT | `d0a473f0607318375786577d523bf5972f502c2c` | PERSON_5760_GITHUB_USERNAME, 2025-09-22T17:40:00Z | A sha free, login resolves; C ≤ clock: PASS |
| 310 | 633 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#54#c_0` | harmonygames-Games/match3d-backend#54, d0a473f0607318375786577d523bf5972f502c2c | A PR+commit in SQL = head, id free: PASS |
| 311 | 635 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#54#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-22T18:02:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 312 | 637 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#54#c_2` | PERSON_5760_GITHUB_USERNAME, 2025-09-24T19:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 313 | 639 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#54#c_3` | PERSON_5760_GITHUB_USERNAME, 2025-09-28T03:10:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 314 | 641 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#54#rev_1` | PERSON_6026_GITHUB_USERNAME, COMMENTED, 2025-09-22T18:06:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 315 | 643 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#54#rev_2` | PERSON_2967_GITHUB_USERNAME, APPROVED, 2025-09-23T15:20:00Z | A PR in SQL, login resolves, commit = head, id free; C within PR window: PASS |
| 316 | 645 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#54#ev_1` | review_requested, PERSON_5760_GITHUB_USERNAME, 2025-09-22T18:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 317 | 647 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#54#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-22T18:02:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 318 | 649 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#54#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-22T18:06:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 319 | 651 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#54#ev_4` | reviewed, PERSON_2967_GITHUB_USERNAME, 2025-09-23T15:20:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 320 | 653 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#54#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-23T16:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 321 | 655 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#54#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-23T16:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 322 | 657 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#54#ev_7` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-24T19:00:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 323 | 659 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#54#ev_8` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-28T03:10:00Z | A PR in SQL, login resolves, id free; C within PR window: PASS |
| 324 | 661 | `github.github_commits` | INSERT | `c219e8c3375700625d4371dc4adb6a519ace58aa` | PERSON_5760_GITHUB_USERNAME, 2025-09-30T18:05:00Z | A sha free, login resolves; C ≤ clock: PASS |
| 325 | 663 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:prod` | prod, c219e8c3375700625d4371dc4adb6a519ace58aa | A id/name free, head commit in SQL: PASS |
| 326 | 666 | `linear.linear_comments` | INSERT | `cmt_0b9e52e7a05129c16301` | ZOM-459, usr_cc3e90160f490686, 2025-08-25T11:40:00Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 327 | 668 | `linear.linear_comments` | INSERT | `cmt_a50779a56d1833aec20b` | ZOM-457, usr_65c76e0b87aa7e9b, 2025-08-25T11:46:02Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 328 | 670 | `linear.linear_comments` | INSERT | `cmt_d08125bf464ffe16ff64` | ZOM-447, usr_cc3e90160f490686, 2025-08-25T09:58:20Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 329 | 672 | `linear.linear_comments` | INSERT | `cmt_aa3a4b36e887c4d668a4` | ZOM-474, usr_65c76e0b87aa7e9b, 2025-08-25T09:23:20Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 330 | 674 | `linear.linear_comments` | INSERT | `cmt_9ab4df8400bed355857e` | ZOM-470, usr_caafeec2804b3a67, 2025-08-25T11:09:26Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 331 | 676 | `linear.linear_comments` | INSERT | `cmt_52185b2931cef92943d3` | ZOM-464, usr_c77c50cc15c5342d, 2025-09-02T10:34:58Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 332 | 678 | `linear.linear_comments` | INSERT | `cmt_9e73c35e85bd1e054a56` | ZOM-497, usr_caafeec2804b3a67, 2025-09-02T12:32:48Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 333 | 680 | `linear.linear_comments` | INSERT | `cmt_3dcb72194895e1b92230` | ZOM-486, usr_65c76e0b87aa7e9b, 2025-09-02T10:27:27Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 334 | 682 | `linear.linear_comments` | INSERT | `cmt_98486e4ab765193640da` | ZOM-495, usr_cc3e90160f490686, 2025-09-02T12:51:23Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 335 | 684 | `linear.linear_comments` | INSERT | `cmt_088a84d96b94ef39674a` | ZOM-496, usr_65c76e0b87aa7e9b, 2025-09-02T12:35:27Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 336 | 686 | `linear.linear_comments` | INSERT | `cmt_6a00a703fed52e7c11fe` | ZOM-501, usr_caafeec2804b3a67, 2025-09-02T11:44:42Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 337 | 688 | `linear.linear_comments` | INSERT | `cmt_18cc4fec19f0d669b9aa` | ZOM-485, usr_65c76e0b87aa7e9b, 2025-09-02T11:30:37Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 338 | 690 | `linear.linear_comments` | INSERT | `cmt_1aff31775b961e6129d4` | ZOM-466, usr_49b9dfa5208d400d, 2025-09-02T13:08:01Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 339 | 692 | `linear.linear_comments` | INSERT | `cmt_45367ccda4895c792313` | ZOM-332, usr_7fe31e7ec8199618, 2025-09-03T15:35:41Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 340 | 694 | `linear.linear_comments` | INSERT | `cmt_6208df52348b4ffc8b30` | ZOM-127, usr_7fe31e7ec8199618, 2025-09-03T13:44:46Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 341 | 696 | `linear.linear_comments` | INSERT | `cmt_f916fc632f4d7a220a9a` | ZOM-265, usr_7fe31e7ec8199618, 2025-09-03T13:59:24Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 342 | 698 | `linear.linear_comments` | INSERT | `cmt_bbbd0687c4431af35535` | ZOM-338, usr_7fe31e7ec8199618, 2025-09-03T14:23:13Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 343 | 700 | `linear.linear_comments` | INSERT | `cmt_96aafd5ba312028e7391` | ZOM-340, usr_7fe31e7ec8199618, 2025-09-03T15:29:40Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 344 | 702 | `linear.linear_comments` | INSERT | `cmt_c69a63ac9dbd4826b955` | ZOM-335, usr_7fe31e7ec8199618, 2025-09-03T13:31:13Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 345 | 704 | `linear.linear_comments` | INSERT | `cmt_877095d931428f1536df` | ZOM-336, usr_7fe31e7ec8199618, 2025-09-03T15:50:00Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 346 | 706 | `linear.linear_comments` | INSERT | `cmt_860e5862211fe64ac0da` | ZOM-331, usr_7fe31e7ec8199618, 2025-09-03T13:54:27Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 347 | 708 | `linear.linear_comments` | INSERT | `cmt_aac3d150bafe119754f8` | ZOM-339, usr_7fe31e7ec8199618, 2025-09-03T13:27:18Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 348 | 710 | `linear.linear_comments` | INSERT | `cmt_bbc8084b40022773292c` | ZOM-337, usr_7fe31e7ec8199618, 2025-09-03T13:36:44Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 349 | 712 | `linear.linear_comments` | INSERT | `cmt_6f75f609688a3ed60aba` | ZOM-502, usr_65c76e0b87aa7e9b, 2025-09-04T08:31:02Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 350 | 714 | `linear.linear_comments` | INSERT | `cmt_4362bbdda4049c5dd30d` | ZOM-476, usr_65c76e0b87aa7e9b, 2025-09-04T09:31:52Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 351 | 716 | `linear.linear_comments` | INSERT | `cmt_d02aec11deff05b555cc` | ZOM-392, usr_cc3e90160f490686, 2025-09-04T10:20:00Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 352 | 718 | `linear.linear_comments` | INSERT | `cmt_112afca3ef67b713a9e7` | ZOM-509, usr_bdf01b53c6a92c5e, 2025-09-04T10:15:00Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 353 | 720 | `linear.linear_comments` | INSERT | `cmt_99069485a5f5d5eb9ce3` | ZOM-518, usr_65c76e0b87aa7e9b, 2025-09-04T12:55:00Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 354 | 722 | `linear.linear_comments` | INSERT | `cmt_0f256875faad3cad9843` | ZOM-510, usr_bdf01b53c6a92c5e, 2025-09-11T16:45:00Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 355 | 724 | `linear.linear_comments` | INSERT | `cmt_57ce6f9bc61a928159ce` | ZOM-519, usr_c77c50cc15c5342d, 2025-09-11T14:17:24Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 356 | 726 | `linear.linear_comments` | INSERT | `cmt_bc49540005814cc8f0e1` | ZOM-256, usr_63fffeb4fab5233e, 2025-09-11T16:48:00Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 357 | 728 | `linear.linear_comments` | INSERT | `cmt_58afcdd4871aac77a852` | ZOM-540, usr_65c76e0b87aa7e9b, 2025-09-12T16:04:38Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 358 | 730 | `linear.linear_comments` | INSERT | `cmt_81278f65a6828964fd37` | ZOM-531, usr_65c76e0b87aa7e9b, 2025-09-15T15:01:00Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 359 | 732 | `linear.linear_comments` | INSERT | `cmt_f3fd31480ea0ad163b4c` | ZOM-512, usr_65c76e0b87aa7e9b, 2025-09-15T12:28:15Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 360 | 734 | `linear.linear_comments` | INSERT | `cmt_92b95a95aa3414a22c89` | ZOM-537, usr_cd7849ec043ab3da, 2025-09-15T15:05:00Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 361 | 736 | `linear.linear_comments` | INSERT | `cmt_32c3a18150bf06ad3a12` | ZOM-444, usr_bdf01b53c6a92c5e, 2025-09-15T15:06:00Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 362 | 738 | `linear.linear_comments` | INSERT | `cmt_9f00cd5152233dc95ff4` | ZOM-515, usr_65c76e0b87aa7e9b, 2025-09-15T12:20:20Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 363 | 740 | `linear.linear_comments` | INSERT | `cmt_a413bcc2401d50df1cc6` | ZOM-493, usr_49b9dfa5208d400d, 2025-09-15T14:47:44Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 364 | 742 | `linear.linear_comments` | INSERT | `cmt_5933eeaa473e3376dc0a` | ZOM-491, usr_49b9dfa5208d400d, 2025-09-15T14:08:56Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 365 | 744 | `linear.linear_comments` | INSERT | `cmt_dd19ad17ac459bc0f50e` | ZOM-463, usr_49b9dfa5208d400d, 2025-09-15T15:09:56Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 366 | 746 | `linear.linear_comments` | INSERT | `cmt_f0049fd2ef671c2b95d1` | ZOM-383, usr_cc3e90160f490686, 2025-09-15T13:46:52Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 367 | 748 | `linear.linear_comments` | INSERT | `cmt_7c7780e6f01e8b2c5103` | ZOM-436, usr_bdf01b53c6a92c5e, 2025-09-17T15:08:39Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 368 | 750 | `linear.linear_comments` | INSERT | `cmt_22a38511a35757459956` | ZOM-421, usr_49b9dfa5208d400d, 2025-09-17T15:26:01Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 369 | 752 | `linear.linear_comments` | INSERT | `cmt_2419c07aa4f77f4a3536` | ZOM-525, usr_49b9dfa5208d400d, 2025-09-17T12:55:28Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 370 | 754 | `linear.linear_comments` | INSERT | `cmt_92867e48f99e1dfd8ba3` | ZOM-523, usr_49b9dfa5208d400d, 2025-09-17T14:08:11Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 371 | 756 | `linear.linear_comments` | INSERT | `cmt_edbbbb8c0b8ced6e4401` | ZOM-524, usr_49b9dfa5208d400d, 2025-09-17T15:36:52Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 372 | 758 | `linear.linear_comments` | INSERT | `cmt_b197d27aaaba58c9b89f` | ZOM-499, usr_49b9dfa5208d400d, 2025-09-17T15:44:00Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 373 | 760 | `linear.linear_comments` | INSERT | `cmt_93d0e4f86d854d279b99` | ZOM-478, usr_49b9dfa5208d400d, 2025-09-17T15:22:09Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 374 | 762 | `linear.linear_comments` | INSERT | `cmt_9a6e40246a899fc380bc` | ZOM-547, usr_65c76e0b87aa7e9b, 2025-09-17T16:01:00Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 375 | 764 | `linear.linear_comments` | INSERT | `cmt_2d985b12de71739e6b82` | ZOM-511, usr_c77c50cc15c5342d, 2025-09-17T15:19:00Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 376 | 766 | `linear.linear_comments` | INSERT | `cmt_41e71e303718899c0d3c` | ZOM-487, usr_65c76e0b87aa7e9b, 2025-09-17T16:09:00Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 377 | 768 | `linear.linear_comments` | INSERT | `cmt_ad7d4901835f513674cd` | ZOM-530, usr_bdf01b53c6a92c5e, 2025-09-18T16:04:18Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 378 | 770 | `linear.linear_comments` | INSERT | `cmt_7cea4a71e9934e0c587c` | ZOM-500, usr_bdf01b53c6a92c5e, 2025-09-19T13:42:00Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 379 | 772 | `linear.linear_comments` | INSERT | `cmt_a5d743a4487fb4aad196` | ZOM-527, usr_49b9dfa5208d400d, 2025-09-19T15:27:52Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 380 | 774 | `linear.linear_comments` | INSERT | `cmt_2e0b9655e5d932f6b7e1` | ZOM-550, usr_65c76e0b87aa7e9b, 2025-09-19T16:10:00Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 381 | 776 | `linear.linear_comments` | INSERT | `cmt_8dbc7c9e3101efc08508` | ZOM-435, usr_bdf01b53c6a92c5e, 2025-09-22T13:49:00Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 382 | 778 | `linear.linear_comments` | INSERT | `cmt_6cdfde887dc9d5875a19` | ZOM-434, usr_bdf01b53c6a92c5e, 2025-09-22T13:26:18Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 383 | 780 | `linear.linear_comments` | INSERT | `cmt_d9d13434b3b6cdbe8c09` | ZOM-507, usr_bdf01b53c6a92c5e, 2025-09-22T12:08:03Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 384 | 782 | `linear.linear_comments` | INSERT | `cmt_bcb9a5974b2de811c2af` | ZOM-169, usr_bdf01b53c6a92c5e, 2025-09-22T14:20:59Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 385 | 784 | `linear.linear_comments` | INSERT | `cmt_c95585f37ce6708a9ec4` | ZOM-503, usr_4e13bd40cc73d0fc, 2025-09-22T15:08:00Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 386 | 786 | `linear.linear_comments` | INSERT | `cmt_80ecf3a45d73d6e13170` | ZOM-473, usr_65c76e0b87aa7e9b, 2025-09-22T14:17:06Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 387 | 788 | `linear.linear_comments` | INSERT | `cmt_cdd62a5e38fdf8d59a57` | ZOM-419, usr_fc22d5941b2aeb5c, 2025-09-22T14:55:01Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 388 | 790 | `linear.linear_comments` | INSERT | `cmt_09ce815cd0da097ee561` | ZOM-239, usr_65c76e0b87aa7e9b, 2025-09-22T12:38:16Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 389 | 792 | `linear.linear_comments` | INSERT | `cmt_445caf64da6e5d8fb2af` | ZOM-506, usr_49b9dfa5208d400d, 2025-09-22T13:45:31Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 390 | 794 | `linear.linear_comments` | INSERT | `cmt_9e4897d4fa0c8f01b3c1` | ZOM-538, usr_c77c50cc15c5342d, 2025-09-23T12:56:12Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 391 | 796 | `linear.linear_comments` | INSERT | `cmt_fb8aec8f0d94d5dadc69` | ZOM-112, usr_c77c50cc15c5342d, 2025-09-23T12:23:48Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 392 | 798 | `linear.linear_comments` | INSERT | `cmt_6df7394cf11eed76b50c` | ZOM-558, usr_caafeec2804b3a67, 2025-09-23T11:56:35Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 393 | 800 | `linear.linear_comments` | INSERT | `cmt_361d1945d189b0587159` | ZOM-536, usr_caafeec2804b3a67, 2025-09-30T09:47:04Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 394 | 802 | `linear.linear_comments` | INSERT | `cmt_68b41719f7d3ea9ff0fe` | ZOM-498, usr_caafeec2804b3a67, 2025-09-30T10:38:37Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 395 | 804 | `linear.linear_comments` | INSERT | `cmt_dbd1c3ba1c96a97fdc3f` | ZOM-555, usr_bdf01b53c6a92c5e, 2025-09-30T11:21:15Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 396 | 806 | `linear.linear_comments` | INSERT | `cmt_c2bad7e49457b4f6c558` | ZOM-553, usr_65c76e0b87aa7e9b, 2025-09-30T12:38:00Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 397 | 808 | `linear.linear_comments` | INSERT | `cmt_e850768746208eefe527` | ZOM-557, usr_bdf01b53c6a92c5e, 2025-09-30T12:39:00Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 398 | 810 | `linear.linear_comments` | INSERT | `cmt_b4c2115bb1a33be756ae` | ZOM-561, usr_65c76e0b87aa7e9b, 2025-09-30T10:27:27Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 399 | 812 | `linear.linear_comments` | INSERT | `cmt_7777dfa66681d9a8aa7a` | ZOM-461, usr_cc3e90160f490686, 2025-08-25T11:45:00Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 400 | 814 | `linear.linear_comments` | INSERT | `cmt_b3046e62e82ef09c3139` | ZOM-480, usr_65c76e0b87aa7e9b, 2025-08-25T10:14:32Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 401 | 816 | `linear.linear_comments` | INSERT | `cmt_43d06395046a31ca5a99` | ZOM-479, usr_65c76e0b87aa7e9b, 2025-08-25T09:52:01Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |
| 402 | 818 | `linear.linear_comments` | INSERT | `cmt_be76fa616764ca440ae2` | ZOM-489, usr_bdf01b53c6a92c5e, 2025-08-25T08:30:50Z | A issue/author resolve, id free; C issue created ≤ comment ≤ completed/updated (Done): PASS |

## 9. Stage dependencies for reuse

`/prompt` may reuse these static checks only while all of the following are unchanged:

- SQL SHA-256 `f5a42cee096292f3b7261a31b89e7b8e345ec48aecbf4c60e6bfcc373740c9c3`
- synth-cut universe manifest `da2f4cf0…ac1a` and the base manifests in §1
- `injection.json` `31dcb2b4…5151`
- `id_contracts.json` `fc4711ef…d4682`
- Eval 0 `b1ea752a…3d3a`
- the fixed clock 2025-10-01 07:00 UTC

Any SQL edit invalidates the whole ledger. The saved `/prompt` report predates this SQL revision and must be rerun. Prompt-specific incorporation, discoverability, persona access and solvability are not covered here.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt (rerun /prompt; the saved /prompt report predates this SQL revision)

Evidence limits: No required static check unresolved. Outside scope: live execution, current database compatibility (unverified snapshot; `seq`, `sequence` and Confluence tables not covered), search ranking, Agent visibility and task difficulty.
