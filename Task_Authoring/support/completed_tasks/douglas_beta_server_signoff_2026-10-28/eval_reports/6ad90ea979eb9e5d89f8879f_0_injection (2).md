# Injection Data-Integrity Review — `/injection`

Review version: `injection-static-v2`
Evidence contract: `stage-evidence-v1` (reused_evidence: none; every check is NEW)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

## 1. Scope

| Item | Value |
|---|---|
| Review | Chat/attachment review, portal attempt 6ad90ea979eb9e5d89f8879f, audit mode (rerun after the contributor's revision) |
| Actual review time | 2026-10-26T17:29Z |
| Universe | `Universe_SynthCut`, hg4-synth-sep30cut v16; `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Reviewed input | `Evals/task_inputs/01_Universe_Inject.sql` (input revision 6, attached as `01_Universe_Inject (3).sql`), 171,485 bytes, 826 lines, SHA-256 `5918bcb0e3eb29dbd0066537ff99a2f9ae5eb7198202d5dd136718570c8f15a7` |
| Previous version | revision 4, SHA-256 `99128292…c544c` (prior report PASS). The edit invalidates the prior ledger, so every check below was rerun on revision 6. |
| Rules | Eval 0 SHA-256 `b1ea752a…723d3a`; WORKFLOW.md `ee4cd8e1…04fcd5d`; scoring.json `5e0bed76…0600c3`; schema snapshot `injection.json` `31dcb2b4…4c5151`; `id_contracts.json` `fc4711ef…9ed4682` (all unchanged since the prior report) |
| Lint | `hg_injection_lint.py` `injection-lint-v1` (SHA-256 `a8226e2a…fc5448b`), universe synthcut, clock 2025-10-01T07:00:00Z |
| Evaluator | Opus 5 (claude-opus-5-5) |

### Input manifest entry (recorded here)

`hg_write_output.py` has no `input_manifest` key, and this review writes under `reports/` only through that writer, so the injection manifest entry is recorded here:

```json
{"injection": {"review_version": "injection-static-v2", "evidence_contract": "stage-evidence-v1",
  "inputs": {"01_Universe_Inject.sql": {"sha256": "5918bcb0e3eb29dbd0066537ff99a2f9ae5eb7198202d5dd136718570c8f15a7", "bytes": 171485, "input_revision": 6}},
  "universe_manifest_sha256": "da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a",
  "reused_evidence": []}}
```

### Changes from revision 4

| # | Change | Rows |
|---|---|---|
| 1 | Header count comment 402 → 404 INSERT (2 UPDATE unchanged) | comment |
| 2 | Sheet `f_78bedc46245090a160d2dd`, "Console & imports": "Zombie Lane rewards sheet v7" → "Zombie Lane rewards" | 1 `sheets_sheets` row |
| 3 | `page_dd_launch_server_signoff` body: "Register: the DD launch sheet." → "Douglas keeps the deploy list." (page and version bodies still identical) | 1 page + 1 version row |
| 4 | Trello card `68dac311754b38be05be7ea9` desc: "since the Aug 15 build" → "since Aug 15" | 1 card row |
| 5 | **New** commit `c219e8c3375700625d4371dc4adb6a519ace58aa` (match3d-backend), "Teams: push lives refresh to client (cherry picked from #52)", authored 2025-09-30T18:05:00Z, committed_date NULL, PERSON_5760 author/committer, parents `[]` | +1 `github_commits` (line 661) |
| 6 | **New** branch `harmonygames-Games/match3d-backend:prod`, head `c219e8c3…`, protected false, is_default false | +1 `github_branches` (line 663) |
| 7 | ZOM-457 comment `cmt_a50779a56d1833aec20b` (2025-08-25T11:46:02Z): "fixed in the client, in Android 0.3.103. nothing needed in match3d-backend" → "parent for the algo level bugs, the fixes are on the child tickets" | 1 `linear_comments` row |
| 8 | ZOM-510 comment `cmt_0f256875faad3cad9843`: "…sheet v7 import on the backend" → "fix is the Zombie Lane rewards import on the backend" | 1 `linear_comments` row |

No existing ID, and no existing statement's relative order, changed. The two new rows sit between the #52/#53 GitHub blocks.

### Base sources read (manifest SHA-256 as returned by the record helper)

| Source (under `Universe_SynthCut/`) | Manifest SHA-256 | Coverage |
|---|---|---|
| `SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json` | `ee578c91…377538` | repositories 15, users 46, PRs 2,475, branches 1,824, commits 11,226, PR commits 13,048, PR comments 687, review comments 1,387, reviews 2,230, timeline events 11,406 (all scans complete) |
| `…Other_Services/Services_Data/linear/data.json` | `b49ec9e8…953b4d` | issues 3,687, users 41, comments 0 (complete) |
| `…Other_Services/Services_Data/trello/data.json` | `6ba242f4…907e3f` | boards 5, lists 47, members 42, cards 803, actions 5,252 |
| `…Other_Services/Services_Data/gdrive/data.json` | `05147aa2…e51e72` | drive_files 53,631, drive_users 25 |
| `…Other_Services/Services_Data/gdocs/data.json` / `gsheets/data.json` | `1b53998d…6edac21` / `a9cc229c…e0a28f` | docs 595, spreadsheets 356 |
| `…Other_Services/Services_Data/gcal/data.json` | `4f093d89…c4f51e` | calendars 38, events 10,395 |
| `…Other_Services/Services_Data/confluence/confluence_working.json` | `d3f13938…f937f0` | spaces 4, pages 30, users 37, page_versions 58 |
| `…Other_Services/Services_Data/slack/channels.json`, `users.json`, `messages/*.json` | `3cca0f7e…26cc`, `6aac5103…75dc` | channels 948, users 218; 4,840 message files / 610,468 messages for id and ts collisions |
| `SynthCut_HarmonyGames_Gmail/Services_Data/gmail/users.json`, `threads/*.json` | `9a90b6bf…ec3e403` | 27 mailboxes; exact-string scan of all 81,404 thread files |

## 2. Input / authority issues

- The SQL is the only input for this stage. Revision 6 was saved and read in full. No inputs are missing.
- Header comments (`-- Are you planning to inject? Yes`, persona/services summary, "Literal values only; parents before children; re-apply this exact SQL before every agent run") are author notes. None addresses a solver or grader or mentions tool calls or pass rate. The header's count claim (404 INSERT, 2 UPDATE) matches the parse.
- The schema snapshot is unverified and does not cover the Confluence tables, so snapshot comparisons are provisional.
- Helper note: the first `hg_records.py` calls returned `Source manifest changed during read` (a file-stat change on first read). Retries completed with `scan_complete: true` and no errors on every check used below.
- 33 lone `\r` bytes inside Gmail `E''` body strings are unchanged from revision 4. They are string content, not statement breaks. Ledger line numbers are counted on `\n` only.

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, base manifest, review version | NEW, done |
| Run `hg_injection_lint.py`; resolve every flag | NEW, 0 FAIL / 0 CHECK / 0 INFO |
| Inventory every statement and affected record | NEW, 408 statements: BEGIN, 404 single-row INSERT, 2 UPDATE, COMMIT (ledger §8) |
| Check A: references, collisions, ID contracts, readable Drive files, one account per person | NEW, PASS |
| Check B: SQL structure and supported schema rules | NEW, PASS (provisional snapshot advisories listed) |
| Check C: dates, relationships, consistency | NEW, PASS |
| Report coverage, findings, limits, one verdict | NEW, done |

## 4. Lint flags and resolution

`counts: FAIL 0, CHECK 0, INFO 0`. Statements 408 (begin 1, insert 404, update 2, commit 1); unparsed: none. Base files loaded: confluence, slack users, trello, gmail users, github, linear, contacts. Checks run: future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape. There is nothing to resolve. The clean lint was not treated as a PASS; checks A–C were done in full.

## 5. Checks A–C

| Check | Result | Evidence |
|---|---|---|
| A: Records, references and IDs | PASS | Every referenced actor, parent, channel, board/list, calendar, issue, branch head and UPDATE target resolves. Every new key, including the new commit SHA and the `prod` branch id/name, is free in the full relevant base collection and unique within the SQL. |
| B: SQL structure and supported schema rules | PASS | 404 single-row INSERTs with equal column/value counts, no duplicate columns and no trailing/ON CONFLICT clauses, inside BEGIN…COMMIT. No generated column is set. Linear text times are `YYYY-MM-DDTHH:MM:SSZ`. No NOT NULL column is omitted. Every `*_json` literal parses and has the base shape. Snapshot gaps are advisory only. |
| C: Dates, relationships and consistency | PASS | The latest event timestamp is 2025-09-30T21:12:44Z, before the 2025-10-01T07:00Z clock. The new prod branch and cherry-pick commit agree with the #52 merge, the latest `prod:` PR comment, the deploy doc and the deploy sheet. The edited Linear, Sheet, Confluence and Trello texts introduce no contradiction. |

### Check A detail

- **GitHub**: repo `harmonygames-Games/match3d-backend` exists. Its base PRs are #1–#35, so the injected #37–#54 collide with none. Full-collection checks found 0 collisions for 18 PR ids; 19 branch ids and 19 branch names (incl. `prod`); 19 commit SHAs (incl. `c219e8c3…`); 18 PR-commit ids; 40 comment ids (also checked against `/review_comments`); 37 review ids; and 131 timeline ids. There are no duplicates inside the SQL. All 6 logins resolve in `/users`:
  - `PERSON_5760_GITHUB_USERNAME` (name "Douglas", douglas@harmonygames.co)
  - `PERSON_2967_GITHUB_USERNAME`
  - `EMPLOYEE_0025_GITHUB_USERNAME` (Arthur Blake)
  - `EMPLOYEE_0012_GITHUB_USERNAME` (Vincent Parker)
  - `PERSON_6026_GITHUB_USERNAME` (coderabbit org)
  - `SVC_0321_GITHUB_USERNAME` (bot)

  Every PR `head_sha` is an injected commit.
  - **New `prod` branch**: the base repo has 37 branches and none is named `prod`. Its default branch is `main` (the new row sets `is_default` false, so main stays default). The head SHA `c219e8c3…` is the injected commit at line 661, which executes before the branch at line 663 (parent before child).
  - **New commit**: author and committer use `PERSON_5760_NAME` / `PERSON_5760_EMAIL`, the form used by most of Douglas's base commits. It uses the same login, so there is no second account. `committed_date` NULL matches the base (all 114 of Douglas's base commits have NULL). `parent_shas_json '[]'` matches the base (0 of 114 list parents). The commit is in no PR-commit list. It is a direct commit on `prod`, which is consistent with a cherry-pick outside a PR.
  - `merge_commit_sha` is NULL on all 18 PRs, which matches the base (0 of 2,475 populate it). The injected `merged` timeline events carry `data.commit_id` values absent from `/commits`, as do 2,276 of the 2,351 distinct base values. That is the base pattern, not a broken reference.
- **Linear**: all 79 comment `issue_id` targets and both UPDATE targets (`ZOM-535`, `ZOM-504`) exist. Base issue `id` equals `identifier`, so `WHERE id = 'ZOM-…'` matches. All 11 `author_id` values resolve in `/users`. Base `/comments` is empty (scan complete), so the 79 comment ids cannot collide; they are unique in the SQL.
- **Slack**: `C0880U9751A` (#zombie-match3d, 25 members) and DM `D05QQF7V404` exist. The authors are `EMPLOYEE_0031_SLACK_ID` (Douglas), `EMPLOYEE_0025_SLACK_ID` (Arthur Blake) and `EMPLOYEE_0003_SLACK_ID` (Oliver Brooks). Re-checked this run: each author is in the member list of every channel they post in (9 of 9). A `lookup` over all 4,840 message files (610,468 messages) found 0 id and 0 ts matches for the 9 messages.
- **Trello**: board `6851a6569f3bf818760632ab` (ZM ROADMAP), list `6851a674975da1fe76e70d93` (BETA: Oct 10, on that board) and member `2162c1ba310341bf318f48b7` (Arthur Blake) exist. Card ids, shortLinks (`twZVoQXy`, `ZWabErQX`) and the 3 action ids are free. Base cards have NULL `shortLink`/`shortUrl`, as do the injected rows. The board's highest idShort is 79, so 80 and 81 are free.
- **Drive/Docs/Sheets**: parents `d_cc3e90160f490686039986`, `d_bdf01b53c6a92c5e167c65` and `d_cd7849ec043ab3da107f8c` are the root folders of Arthur, Oliver and Douglas, matching each item's owner. The 4 new Drive ids, the doc id and the spreadsheet id are free, and every sharing email is a Drive user. On readability:
  - The Google Doc has a `docs_documents` row with a body.
  - The Sheet has a spreadsheet row and 2 sheet rows with grid data. The sheets key is composite (`spreadsheet_id`, `sheet_id` 0/1), not a duplicate.
  - The folders need no content.
- **Confluence**: `space_OPS`, parent `page_ops_home` and author `user_EMPLOYEE_0025` (Arthur Blake) exist. The 2 page ids, 2 titles and 2 version ids are free.
- **Gmail**: mailboxes douglas, oliver.brooks, arthur.blake and leonard.hayes exist in `users.json`. An exact-string scan of all 81,404 thread files found no hit for the six thread numbers or either Message-ID. `history_id` is NULL on all 6 threads, which satisfies the contract.
- **Calendar**: all 5 calendars exist. The 5 event ids and the shared iCalUID are free.
- **One account per person**: no account is created in any service, and the lint's `identities` check passed.

### Check B detail

- An independent per-statement parse found 404 INSERTs, each with one VALUES tuple, column count equal to value count, no duplicate column names and nothing after the tuple. Both UPDATEs have a literal `WHERE id = '…'`. The whole script is wrapped in BEGIN … COMMIT.
- Supported platform rules:
  - `slack.slack_messages.text_fts` is not set.
  - Linear `created_at`/`updated_at` and the UPDATE values use `YYYY-MM-DDTHH:MM:SSZ`.
  - There is no new `linear_issues` row.
  - All `*_json` literals parse, and their shapes match the snapshot.
  - The new branch's `protected`/`is_default` are booleans, and the new commit's `parent_shas_json` is a JSON list.
- NOT NULL coverage: no INSERT omits a NOT NULL, no-default, non-generated column of the snapshot. The new commit's NULL `committed_date` is a nullable column.
- Case-exact column comparison against the snapshot (quoted camelCase Trello columns such as `"idBoard"` and `"dateLastActivity"` match exactly):

| Table | Column in SQL | Snapshot |
|---|---|---|
| `github.github_reviews` | `seq` | NOT COVERED |
| `linear.linear_comments` | `sequence` | NOT COVERED |
| `confluence.confluence_pages`, `confluence.confluence_page_versions` | all | table not in snapshot |
| all other affected tables/columns (17 tables, incl. the new branch and commit rows) | n/a | MATCH |

  A column missing from an unverified snapshot is advisory, not a defect.

### Check C detail

- **Fixed clock**: the latest event timestamp is Slack `1e5d5d2b…` at 2025-09-30T21:12:44Z. The new commit is 2025-09-30T18:05:00Z. Future dates appear only as plans inside text (go/no-go Thu Oct 2, beta Oct 10).
- **New prod branch and cherry-pick (revision 6)**. The sequence is:
  1. PR #52 approved 2025-09-22 14:50 and merged 15:05.
  2. The cherry-pick commit "(cherry picked from #52)" at 2025-09-30 18:05.
  3. The PR `prod:` comment "2025-09-30 18:16 UTC, zm-api:57".

  That 18:16 deploy is the latest prod/rollback event in the injected data (the earlier rollback of #54 was 2025-09-28 03:10), so a `prod` head equal to the #52 pick is consistent. The deploy doc `f_470ae81236d5bd39045dc1` ("Prod runs from the prod branch: … cherry-pick it onto prod") and the Prod deploys tab ("2025-08-25 11:52 beta prod cut: prod branch from main (#37, #38)") now point to a branch that exists. Base `page_cicd_pipeline` (Mar 2025: long-lived feature branches, deploy run by hand) does not contradict a prod branch. The branch exists only in the injected data. No base record says match3d-backend has no prod branch, and the base branch list has no `prod`, so this is new state, not a conflict.
- **GitHub internal consistency** (programmatic check over 18 PRs, 0 issues):
  - Commit authored ≤ PR created.
  - Reviews and comments come after PR creation.
  - `updated_at` = latest review/comment/merge.
  - `merged_at` = `closed_at`, state closed.
  - Each review has exactly one matching `reviewed` event (actor, time, state, commit).
  - Each comment has one `commented` event.
  - `merged`/`closed` events match `merged_by` and time.
  - `review_requested` is raised by the author and never targets the author.
  - Review `seq` runs 1…n in time order, and event ids run 1…n.
  - Branch head = PR head = PR-commit row; review `commit_id` = head SHA; no self-review.
- **Deploy log vs PR `prod:` comments**: all 7 Prod deploys rows (2025-08-25 → 2025-09-10, zm-api:41–47) match the PR comments' time, PRs, task definition and deployer. Task-definition numbers rise with time through zm-api:57 (2025-09-30 18:16), including both rollbacks. The sheet's `modified_time` (2025-09-11 16:35) follows its last row.
- **ZOM-457 comment (revision 6)**: ZOM-457 "Algo Level Issues" is the parent of ZOM-456, ZOM-458, ZOM-459 and ZOM-461, so "parent for the algo level bugs, the fixes are on the child tickets" matches the base hierarchy. The comment (11:46:02Z) precedes the issue's `completed_at` (2025-08-25T11:53:20Z). This also removes the old "nothing needed in match3d-backend" wording.
- **ZOM-510 comment and Console & imports row (revision 6)**: the comment (2025-09-11 16:45) "fix is the Zombie Lane rewards import on the backend" agrees with the sheet row (prod import 2025-09-08 16:45, "Zombie Lane rewards") and precedes ZOM-510's completion (16:49:06). The string "v7" no longer appears anywhere in the SQL.
- **DD launch page (revision 6)**: the page and version bodies are identical. "Douglas keeps the deploy list." is May 2025 context and conflicts with nothing in the base or the injected data.
- **Trello card desc (revision 6)**: "since Aug 15" is a wording-only change with the same meaning.
- **Linear**: all 77 comments on Done issues fall between the issue's `created_at` and its `completed_at`/`updated_at`. The ZOM-535 (Todo) and ZOM-504 (Backlog) comments come after their base `updated_at`, and the UPDATEs set `updated_at` to exactly those comment times. Comments that cite a PR come after that PR's merge.
- **Slack**: every `ts` equals `created_at`. Thread parent `81531d5f…` has `thread_ts_legacy` = its own ts (base pattern), `reply_count` 2, `reply_users_count` 2 and `latest_reply` = the last reply's ts. The replies follow the parent and carry its ts.
- **Trello**: ObjectId timestamps equal the stated times (cards 17:20:41 and 17:34:09 = their createCard dates; the comment action at 2025-09-30T15:05:27Z = card 80's `dateLastActivity`).
- **Gmail/Calendar**: `internal_date` = `date` for all 6 messages. The sender has a SENT copy and recipients have INBOX copies. Calendar copies satisfy created 09-22 ≤ updated 09-23 ≤ start 2025-09-26T22:00Z < end.
- **Drive**: the client and server QA folders (2025-09-29 17:05:02Z, 17:12:30Z) exist before the Confluence ZM Beta page (17:15) and the client card (17:34) that reference them. The deploy doc (2025-06-01T18:30Z) follows base PR #2 "Created new env for production" (merged 2025-06-01T17:54:03Z).
- **Unapproved merges** (#40 and #43 have no approval; #41 and #47 were approved after merge): this follows observed base practice (base match3d-backend #4, #6 and #7 merged without approval).
- **Stale or misleading statements kept as supported context**: Douglas's 09-22 DM, Oliver's 09-27 "all the server fixes … are on prod now", and the May 2025 Domino Delights page. Later or more authoritative records contradict each one, which Eval 0 allows.

## 6. Findings

No demonstrated defect in A, B or C. The revision-6 edits (new `prod` branch, cherry-pick commit, four text changes) passed every check.

Advisories (optional; none changes the verdict):

1. **Cherry-pick author date (realism only)**: `git cherry-pick` normally keeps the original author date (the #52 commit, 2025-09-22) and records the pick time as the committer date. Here `authored_date` is the pick time (2025-09-30T18:05Z) and `committed_date` is NULL, which follows the base convention of NULL `committed_date`. This is not a demonstrated inconsistency. If a solver may compare the dates, keep it as is. Optionally, put the #52 time in the message or leave the row unchanged.
2. **Snapshot columns not covered** (Check B, provisional): `seq` (github_reviews) and `sequence` (linear_comments). If the platform load rejects either column, drop it from every INSERT of that table.
3. **Confluence tables not in the snapshot**: column names can't be compared offline. Disclosed limit only.

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

## 8. Operation ledger (all 406 row operations, execution order)

BEGIN at line 5 and COMMIT at line 826 wrap these rows. Line = the line where the statement starts. "PASS" means every check listed for that row passed (§5 details).

| # | Line | Table | Op | Record / target | Key values | Checks |
|---|---|---|---|---|---|---|
| 1 | 7 | `gdrive.drive_files` | INSERT | `d_69fcebc484d472907b0b5c` | parent d_cc3e90160f490686039986, owner arthur.blake@harmonygames.co, created 2025-09-29T17:12:30Z | A parent/owner/sharing resolve, id free; C time: PASS |
| 2 | 9 | `gdrive.drive_files` | INSERT | `d_d71300168ca5dffa4db8b3` | parent d_bdf01b53c6a92c5e167c65, owner oliver.brooks@harmonygames.co, created 2025-09-29T17:05:02Z | A parent/owner/sharing resolve, id free; C time: PASS |
| 3 | 11 | `gdrive.drive_files` | INSERT | `f_470ae81236d5bd39045dc1` | parent d_cd7849ec043ab3da107f8c, owner douglas@harmonygames.co, created 2025-06-01T18:30:00Z | A parent/owner/sharing resolve, id free; C time: PASS |
| 4 | 13 | `gdrive.drive_files` | INSERT | `f_78bedc46245090a160d2dd` | parent d_cd7849ec043ab3da107f8c, owner douglas@harmonygames.co, created 2025-08-25T12:05:00Z | A parent/owner/sharing resolve, id free; C time: PASS |
| 5 | 16 | `gdocs.docs_documents` | INSERT | `f_470ae81236d5bd39045dc1` | drive_file_id same; body 1399 chars | A id free; readable body: PASS |
| 6 | 19 | `gsheets.sheets_spreadsheets` | INSERT | `f_78bedc46245090a160d2dd` | modified 2025-09-11T16:35:00Z | A id free; C rows/modified: PASS |
| 7 | 21 | `gsheets.sheets_sheets` | INSERT | `f_78bedc46245090a160d2dd` | sheet 0 'Prod deploys' | A id free; C rows/modified: PASS |
| 8 | 23 | `gsheets.sheets_sheets` | INSERT | `f_78bedc46245090a160d2dd` | sheet 1 'Console & imports' | A id free; C rows/modified: PASS |
| 9 | 26 | `confluence.confluence_pages` | INSERT | `page_dd_launch_server_signoff` | page_ops_home, author user_EMPLOYEE_0025, 2025-05-12T15:04:00Z | A space/parent/author resolve, id+title free: PASS |
| 10 | 28 | `confluence.confluence_page_versions` | INSERT | `ver_2ee4eb6acd67b53fc1013166dab4c1b5` | page_dd_launch_server_signoff, author user_EMPLOYEE_0025, 2025-05-12T15:04:00Z | A space/parent/author resolve, id+title free: PASS |
| 11 | 30 | `confluence.confluence_pages` | INSERT | `page_zm_beta_oct10` | page_ops_home, author user_EMPLOYEE_0025, 2025-09-29T17:15:00Z | A space/parent/author resolve, id+title free: PASS |
| 12 | 32 | `confluence.confluence_page_versions` | INSERT | `ver_338613da12d5a29e3e4947118c87f7ea` | page_zm_beta_oct10, author user_EMPLOYEE_0025, 2025-09-29T17:15:00Z | A space/parent/author resolve, id+title free: PASS |
| 13 | 35 | `slack.slack_messages` | INSERT | `3a2e99ef807fc28ef39b8d6973a44427` | C0880U9751A, EMPLOYEE_0003_SLACK_ID, ts 1748450537.204611, thread_ts None, parent None | A channel/member, id+ts free; C ts=created_at, thread: PASS |
| 14 | 37 | `slack.slack_messages` | INSERT | `9ba4f3770f458826c7503e1aa0992acc` | C0880U9751A, EMPLOYEE_0025_SLACK_ID, ts 1758295268.611352, thread_ts None, parent None | A channel/member, id+ts free; C ts=created_at, thread: PASS |
| 15 | 39 | `slack.slack_messages` | INSERT | `f5dde99eaea0ac1773ca37e48871cb60` | D05QQF7V404, EMPLOYEE_0031_SLACK_ID, ts 1758571837.284511, thread_ts None, parent None | A channel/member, id+ts free; C ts=created_at, thread: PASS |
| 16 | 41 | `slack.slack_messages` | INSERT | `10613025eb309bac6e0fb32438625484` | C0880U9751A, EMPLOYEE_0003_SLACK_ID, ts 1758991212.775031, thread_ts None, parent None | A channel/member, id+ts free; C ts=created_at, thread: PASS |
| 17 | 43 | `slack.slack_messages` | INSERT | `42f263bfce69ae5a4ef068383ae66c4a` | C0880U9751A, EMPLOYEE_0003_SLACK_ID, ts 1759253506.093318, thread_ts None, parent None | A channel/member, id+ts free; C ts=created_at, thread: PASS |
| 18 | 45 | `slack.slack_messages` | INSERT | `1e5d5d2bf50901f0d7376627d6f539e8` | D05QQF7V404, EMPLOYEE_0025_SLACK_ID, ts 1759266764.508127, thread_ts None, parent None | A channel/member, id+ts free; C ts=created_at, thread: PASS |
| 19 | 47 | `slack.slack_messages` | INSERT | `81531d5f36d48a5d2028a22405aed65e` | C0880U9751A, EMPLOYEE_0031_SLACK_ID, ts 1758937233.118904, thread_ts 1758937233.118904, parent None | A channel/member, id+ts free; C ts=created_at, thread: PASS |
| 20 | 49 | `slack.slack_messages` | INSERT | `33339417b07ab83542fc971a41320a36` | C0880U9751A, EMPLOYEE_0025_SLACK_ID, ts 1758938751.402267, thread_ts 1758937233.118904, parent 81531d5f36d48a5d2028a22405aed65e | A channel/member, id+ts free; C ts=created_at, thread: PASS |
| 21 | 51 | `slack.slack_messages` | INSERT | `bde0c0ff791441e66d57cdb2de8f0f51` | C0880U9751A, EMPLOYEE_0031_SLACK_ID, ts 1758938832.553908, thread_ts 1758937233.118904, parent 81531d5f36d48a5d2028a22405aed65e | A channel/member, id+ts free; C ts=created_at, thread: PASS |
| 22 | 54 | `trello.trello_cards` | INSERT | `68dabfe9bc2e8b969782e22d` | idShort 80, list 6851a674…, lastActivity 2025-09-30T15:05:27Z | A board/list/member, id+shortLink+idShort free; C ObjectId time: PASS |
| 23 | 56 | `trello.trello_actions` | INSERT | `68dabfe93a26ef2186dcec1c` | createCard 2025-09-29T17:20:41Z card 68dabfe9bc2e8b969782e22d | A board/list/member, id+shortLink+idShort free; C ObjectId time: PASS |
| 24 | 58 | `trello.trello_cards` | INSERT | `68dac311754b38be05be7ea9` | idShort 81, list 6851a674…, lastActivity 2025-09-29T17:34:09Z | A board/list/member, id+shortLink+idShort free; C ObjectId time: PASS |
| 25 | 60 | `trello.trello_actions` | INSERT | `68dac311a286768d02a6385d` | createCard 2025-09-29T17:34:09Z card 68dac311754b38be05be7ea9 | A board/list/member, id+shortLink+idShort free; C ObjectId time: PASS |
| 26 | 62 | `trello.trello_actions` | INSERT | `68dbf1b73eba0ba580f67a6e` | commentCard 2025-09-30T15:05:27Z card 68dabfe9bc2e8b969782e22d | A board/list/member, id+shortLink+idShort free; C ObjectId time: PASS |
| 27 | 65 | `gmail.gmail_threads` | INSERT | `douglas@harmonygames.co/1844719216755416739` | history_id NULL | A mailbox, thread/msg free, history_id NULL; C date=internal_date: PASS |
| 28 | 67 | `gmail.gmail_messages` | INSERT | `douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com>` | INBOX, 2025-09-30T19:42:18Z, from arthur.blake@harmonygames.co | A mailbox, thread/msg free, history_id NULL; C date=internal_date: PASS |
| 29 | 69 | `gmail.gmail_threads` | INSERT | `oliver.brooks@harmonygames.co/1844719216754885141` | history_id NULL | A mailbox, thread/msg free, history_id NULL; C date=internal_date: PASS |
| 30 | 71 | `gmail.gmail_messages` | INSERT | `oliver.brooks@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com>` | INBOX, 2025-09-30T19:42:18Z, from arthur.blake@harmonygames.co | A mailbox, thread/msg free, history_id NULL; C date=internal_date: PASS |
| 31 | 73 | `gmail.gmail_threads` | INSERT | `arthur.blake@harmonygames.co/1844719216755483955` | history_id NULL | A mailbox, thread/msg free, history_id NULL; C date=internal_date: PASS |
| 32 | 75 | `gmail.gmail_messages` | INSERT | `arthur.blake@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com>` | SENT, 2025-09-30T19:42:18Z, from arthur.blake@harmonygames.co | A mailbox, thread/msg free, history_id NULL; C date=internal_date: PASS |
| 33 | 77 | `gmail.gmail_threads` | INSERT | `douglas@harmonygames.co/1844721277206562572` | history_id NULL | A mailbox, thread/msg free, history_id NULL; C date=internal_date: PASS |
| 34 | 79 | `gmail.gmail_messages` | INSERT | `douglas@harmonygames.co/<CAreN_3nXHn9vq-8FWgVQEC3_2hxsSjSNZRkPtWB@mail.gmail.com>` | INBOX, 2025-09-30T20:15:03Z, from leonard.hayes@harmonygames.co | A mailbox, thread/msg free, history_id NULL; C date=internal_date: PASS |
| 35 | 81 | `gmail.gmail_threads` | INSERT | `arthur.blake@harmonygames.co/1844721277207387678` | history_id NULL | A mailbox, thread/msg free, history_id NULL; C date=internal_date: PASS |
| 36 | 83 | `gmail.gmail_messages` | INSERT | `arthur.blake@harmonygames.co/<CAreN_3nXHn9vq-8FWgVQEC3_2hxsSjSNZRkPtWB@mail.gmail.com>` | INBOX, 2025-09-30T20:15:03Z, from leonard.hayes@harmonygames.co | A mailbox, thread/msg free, history_id NULL; C date=internal_date: PASS |
| 37 | 85 | `gmail.gmail_threads` | INSERT | `leonard.hayes@harmonygames.co/1844721277206833296` | history_id NULL | A mailbox, thread/msg free, history_id NULL; C date=internal_date: PASS |
| 38 | 87 | `gmail.gmail_messages` | INSERT | `leonard.hayes@harmonygames.co/<CAreN_3nXHn9vq-8FWgVQEC3_2hxsSjSNZRkPtWB@mail.gmail.com>` | SENT, 2025-09-30T20:15:03Z, from leonard.hayes@harmonygames.co | A mailbox, thread/msg free, history_id NULL; C date=internal_date: PASS |
| 39 | 90 | `gcal.gcal_events` | INSERT | `evt_b6eda0097a341f225ad5d2` | cal arthur.blake@harmonygames.co, 2025-09-26T22:00:00Z–22:30, created 2025-09-22T14:02:00Z | A calendar, id+iCalUID free; C created≤updated≤start: PASS |
| 40 | 92 | `gcal.gcal_events` | INSERT | `evt_0f489eb7fb46ada9660881` | cal douglas@harmonygames.co, 2025-09-26T22:00:00Z–22:30, created 2025-09-22T14:02:00Z | A calendar, id+iCalUID free; C created≤updated≤start: PASS |
| 41 | 94 | `gcal.gcal_events` | INSERT | `evt_e3c3cd6a8dec19d0e7b123` | cal oliver.brooks@harmonygames.co, 2025-09-26T22:00:00Z–22:30, created 2025-09-22T14:02:00Z | A calendar, id+iCalUID free; C created≤updated≤start: PASS |
| 42 | 96 | `gcal.gcal_events` | INSERT | `evt_5e9adacd9af476a6402dfa` | cal owen.baker@harmonygames.co, 2025-09-26T22:00:00Z–22:30, created 2025-09-22T14:02:00Z | A calendar, id+iCalUID free; C created≤updated≤start: PASS |
| 43 | 98 | `gcal.gcal_events` | INSERT | `evt_bbe10af026c7f633387e2d` | cal vincent.parker@harmonygames.co, 2025-09-26T22:00:00Z–22:30, created 2025-09-22T14:02:00Z | A calendar, id+iCalUID free; C created≤updated≤start: PASS |
| 44 | 101 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#37` | #37 by PERSON_5760_GITHUB_USERNAME, created 2025-08-21T15:20:00Z, merged 2025-08-25T09:10:00Z, merge_commit_sha NULL | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 45 | 103 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:algo-levels-spawn-points-from-the-server` | head d96ec79123 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 46 | 105 | `github.github_commits` | INSERT | `d96ec79123c2d518760e6b9a2ccc6433f931c488` | PERSON_5760_GITHUB_USERNAME / PERSON_5760_NAME, 2025-08-21T15:00:00Z, parents [] | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 47 | 107 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#37#c_0` | match3d-backend#37 → d96ec79123 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 48 | 109 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#37#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-08-21T15:22:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 49 | 111 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#37#c_2` | PERSON_2967_GITHUB_USERNAME, 2025-08-25T11:52:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 50 | 113 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#37#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED, 2025-08-21T15:26:00Z, seq 1 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 51 | 115 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#37#rev_2` | PERSON_2967_GITHUB_USERNAME APPROVED, 2025-08-25T09:00:00Z, seq 2 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 52 | 117 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#37#ev_1` | review_requested, PERSON_5760_GITHUB_USERNAME, 2025-08-21T15:20:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 53 | 119 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#37#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-08-21T15:22:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 54 | 121 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#37#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-08-21T15:26:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 55 | 123 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#37#ev_4` | reviewed, PERSON_2967_GITHUB_USERNAME, 2025-08-25T09:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 56 | 125 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#37#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-08-25T09:10:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 57 | 127 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#37#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-08-25T09:10:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 58 | 129 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#37#ev_7` | commented, PERSON_2967_GITHUB_USERNAME, 2025-08-25T11:52:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 59 | 131 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#38` | #38 by PERSON_5760_GITHUB_USERNAME, created 2025-08-22T15:10:00Z, merged 2025-08-25T09:30:00Z, merge_commit_sha NULL | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 60 | 133 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:plague-race-count-algo-levels` | head b1388ff2f8 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 61 | 135 | `github.github_commits` | INSERT | `b1388ff2f8d945f005ea87b236afbab0c14e6e64` | PERSON_5760_GITHUB_USERNAME / PERSON_5760_NAME, 2025-08-22T14:50:00Z, parents [] | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 62 | 137 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#38#c_0` | match3d-backend#38 → b1388ff2f8 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 63 | 139 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#38#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-08-22T15:12:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 64 | 141 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#38#c_2` | PERSON_2967_GITHUB_USERNAME, 2025-08-25T11:52:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 65 | 143 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#38#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED, 2025-08-22T15:16:00Z, seq 1 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 66 | 145 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#38#rev_2` | PERSON_2967_GITHUB_USERNAME APPROVED, 2025-08-25T09:20:00Z, seq 2 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 67 | 147 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#38#ev_1` | review_requested, PERSON_5760_GITHUB_USERNAME, 2025-08-22T15:10:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 68 | 149 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#38#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-08-22T15:12:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 69 | 151 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#38#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-08-22T15:16:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 70 | 153 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#38#ev_4` | reviewed, PERSON_2967_GITHUB_USERNAME, 2025-08-25T09:20:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 71 | 155 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#38#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-08-25T09:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 72 | 157 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#38#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-08-25T09:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 73 | 159 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#38#ev_7` | commented, PERSON_2967_GITHUB_USERNAME, 2025-08-25T11:52:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 74 | 161 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#39` | #39 by PERSON_2967_GITHUB_USERNAME, created 2025-08-29T13:00:00Z, merged 2025-09-02T15:40:00Z, merge_commit_sha NULL | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 75 | 163 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:trophy-path-container-headlines-config` | head 48153d42da | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 76 | 165 | `github.github_commits` | INSERT | `48153d42da95f5824fe53b669b0ab027f2cfe9a0` | PERSON_2967_GITHUB_USERNAME / PERSON_2967_NAME, 2025-08-29T12:40:00Z, parents [] | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 77 | 167 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#39#c_0` | match3d-backend#39 → 48153d42da | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 78 | 169 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#39#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-08-29T13:02:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 79 | 171 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#39#c_2` | PERSON_2967_GITHUB_USERNAME, 2025-09-02T17:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 80 | 173 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#39#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED, 2025-08-29T13:06:00Z, seq 1 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 81 | 175 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#39#rev_2` | PERSON_5760_GITHUB_USERNAME APPROVED, 2025-09-02T15:20:00Z, seq 2 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 82 | 177 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#39#ev_1` | review_requested, PERSON_2967_GITHUB_USERNAME, 2025-08-29T13:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 83 | 179 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#39#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-08-29T13:02:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 84 | 181 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#39#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-08-29T13:06:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 85 | 183 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#39#ev_4` | reviewed, PERSON_5760_GITHUB_USERNAME, 2025-09-02T15:20:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 86 | 185 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#39#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-02T15:40:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 87 | 187 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#39#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-02T15:40:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 88 | 189 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#39#ev_7` | commented, PERSON_2967_GITHUB_USERNAME, 2025-09-02T17:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 89 | 191 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#40` | #40 by PERSON_2967_GITHUB_USERNAME, created 2025-09-01T10:15:00Z, merged 2025-09-02T18:20:00Z, merge_commit_sha NULL | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 90 | 193 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:items-make-the-cooler-a-usable-item` | head 334b4ed82b | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 91 | 195 | `github.github_commits` | INSERT | `334b4ed82b283bca22b8f218f389a9c834789745` | PERSON_2967_GITHUB_USERNAME / PERSON_2967_NAME, 2025-09-01T09:55:00Z, parents [] | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 92 | 197 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#40#c_0` | match3d-backend#40 → 334b4ed82b | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 93 | 199 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#40#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-01T10:17:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 94 | 201 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#40#c_2` | PERSON_2967_GITHUB_USERNAME, 2025-09-02T18:40:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 95 | 203 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#40#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED, 2025-09-01T10:21:00Z, seq 1 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 96 | 205 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#40#ev_1` | review_requested, PERSON_2967_GITHUB_USERNAME, 2025-09-01T10:15:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 97 | 207 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#40#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-01T10:17:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 98 | 209 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#40#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-01T10:21:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 99 | 211 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#40#ev_4` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-02T18:20:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 100 | 213 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#40#ev_5` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-02T18:20:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 101 | 215 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#40#ev_6` | commented, PERSON_2967_GITHUB_USERNAME, 2025-09-02T18:40:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 102 | 217 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#41` | #41 by PERSON_5760_GITHUB_USERNAME, created 2025-09-01T19:40:00Z, merged 2025-09-03T16:00:00Z, merge_commit_sha NULL | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 103 | 219 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:algo-levels-100-seed-endpoint` | head 61e10e32a9 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 104 | 221 | `github.github_commits` | INSERT | `61e10e32a992a316e9f01836c6d1d12fff65868a` | PERSON_5760_GITHUB_USERNAME / PERSON_5760_NAME, 2025-09-01T19:20:00Z, parents [] | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 105 | 223 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#41#c_0` | match3d-backend#41 → 61e10e32a9 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 106 | 225 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#41#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-01T19:42:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 107 | 227 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#41#c_2` | PERSON_5760_GITHUB_USERNAME, 2025-09-03T16:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 108 | 229 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#41#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED, 2025-09-01T19:46:00Z, seq 1 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 109 | 231 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#41#rev_2` | PERSON_2967_GITHUB_USERNAME APPROVED, 2025-09-03T18:05:00Z, seq 2 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 110 | 233 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#41#ev_1` | review_requested, PERSON_5760_GITHUB_USERNAME, 2025-09-01T19:40:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 111 | 235 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#41#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-01T19:42:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 112 | 237 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#41#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-01T19:46:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 113 | 239 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#41#ev_4` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-03T16:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 114 | 241 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#41#ev_5` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-03T16:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 115 | 243 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#41#ev_6` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-03T16:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 116 | 245 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#41#ev_7` | reviewed, PERSON_2967_GITHUB_USERNAME, 2025-09-03T18:05:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 117 | 247 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#42` | #42 by PERSON_5760_GITHUB_USERNAME, created 2025-09-03T15:00:00Z, merged 2025-09-05T16:00:00Z, merge_commit_sha NULL | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 118 | 249 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:teams-ack-lives-gift` | head 250e1846dd | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 119 | 251 | `github.github_commits` | INSERT | `250e1846dd3f0770eddcb32a8ba25d32a5c33260` | PERSON_5760_GITHUB_USERNAME / PERSON_5760_NAME, 2025-09-03T14:40:00Z, parents [] | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 120 | 253 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#42#c_0` | match3d-backend#42 → 250e1846dd | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 121 | 255 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#42#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-03T15:02:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 122 | 257 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#42#c_2` | PERSON_5760_GITHUB_USERNAME, 2025-09-08T17:18:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 123 | 259 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#42#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED, 2025-09-03T15:06:00Z, seq 1 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 124 | 261 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#42#rev_2` | PERSON_2967_GITHUB_USERNAME APPROVED, 2025-09-05T15:30:00Z, seq 2 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 125 | 263 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#42#ev_1` | review_requested, PERSON_5760_GITHUB_USERNAME, 2025-09-03T15:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 126 | 265 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#42#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-03T15:02:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 127 | 267 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#42#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-03T15:06:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 128 | 269 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#42#ev_4` | reviewed, PERSON_2967_GITHUB_USERNAME, 2025-09-05T15:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 129 | 271 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#42#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-05T16:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 130 | 273 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#42#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-05T16:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 131 | 275 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#42#ev_7` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-08T17:18:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 132 | 277 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#43` | #43 by PERSON_2967_GITHUB_USERNAME, created 2025-09-04T11:10:00Z, merged 2025-09-04T12:30:00Z, merge_commit_sha NULL | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 133 | 279 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:inventory-drop-non-card-items-from-equip` | head 7d24459d13 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 134 | 281 | `github.github_commits` | INSERT | `7d24459d1307b6ab594e52cdc5633d002a08d54b` | PERSON_2967_GITHUB_USERNAME / PERSON_2967_NAME, 2025-09-04T10:50:00Z, parents [] | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 135 | 283 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#43#c_0` | match3d-backend#43 → 7d24459d13 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 136 | 285 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#43#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-04T11:12:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 137 | 287 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#43#c_2` | PERSON_2967_GITHUB_USERNAME, 2025-09-04T12:50:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 138 | 289 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#43#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED, 2025-09-04T11:16:00Z, seq 1 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 139 | 291 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#43#ev_1` | review_requested, PERSON_2967_GITHUB_USERNAME, 2025-09-04T11:10:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 140 | 293 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#43#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-04T11:12:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 141 | 295 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#43#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-04T11:16:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 142 | 297 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#43#ev_4` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-04T12:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 143 | 299 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#43#ev_5` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-04T12:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 144 | 301 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#43#ev_6` | commented, PERSON_2967_GITHUB_USERNAME, 2025-09-04T12:50:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 145 | 303 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#44` | #44 by PERSON_2967_GITHUB_USERNAME, created 2025-09-04T22:00:00Z, merged 2025-09-08T15:30:00Z, merge_commit_sha NULL | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 146 | 305 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:profile-other-players-profile-v2` | head b3ca856157 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 147 | 307 | `github.github_commits` | INSERT | `b3ca856157e0fffa2ae28e9701ef4872205bc6f8` | PERSON_2967_GITHUB_USERNAME / PERSON_2967_NAME, 2025-09-04T21:40:00Z, parents [] | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 148 | 309 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#44#c_0` | match3d-backend#44 → b3ca856157 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 149 | 311 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#44#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-04T22:02:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 150 | 313 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#44#c_2` | PERSON_5760_GITHUB_USERNAME, 2025-09-08T17:18:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 151 | 315 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#44#c_3` | PERSON_2967_GITHUB_USERNAME, 2025-09-20T02:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 152 | 317 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#44#c_4` | PERSON_2967_GITHUB_USERNAME, 2025-09-22T17:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 153 | 319 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#44#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED, 2025-09-04T22:06:00Z, seq 1 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 154 | 321 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#44#rev_2` | PERSON_5760_GITHUB_USERNAME CHANGES_REQUESTED, 2025-09-05T16:00:00Z, seq 2 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 155 | 323 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#44#rev_3` | PERSON_5760_GITHUB_USERNAME APPROVED, 2025-09-08T15:10:00Z, seq 3 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 156 | 325 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#44#ev_1` | review_requested, PERSON_2967_GITHUB_USERNAME, 2025-09-04T22:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 157 | 327 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#44#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-04T22:02:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 158 | 329 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#44#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-04T22:06:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 159 | 331 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#44#ev_4` | reviewed, PERSON_5760_GITHUB_USERNAME, 2025-09-05T16:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 160 | 333 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#44#ev_5` | reviewed, PERSON_5760_GITHUB_USERNAME, 2025-09-08T15:10:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 161 | 335 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#44#ev_6` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-08T15:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 162 | 337 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#44#ev_7` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-08T15:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 163 | 339 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#44#ev_8` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-08T17:18:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 164 | 341 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#44#ev_9` | commented, PERSON_2967_GITHUB_USERNAME, 2025-09-20T02:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 165 | 343 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#44#ev_10` | commented, PERSON_2967_GITHUB_USERNAME, 2025-09-22T17:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 166 | 345 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#45` | #45 by PERSON_5760_GITHUB_USERNAME, created 2025-09-08T15:10:00Z, merged 2025-09-10T16:00:00Z, merge_commit_sha NULL | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 167 | 347 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:inventory-keep-equipped-slots-across-ses` | head 46dc449026 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 168 | 349 | `github.github_commits` | INSERT | `46dc449026428308b2f3e48d0b88f039153a9aed` | PERSON_5760_GITHUB_USERNAME / PERSON_5760_NAME, 2025-09-08T14:50:00Z, parents [] | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 169 | 351 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#45#c_0` | match3d-backend#45 → 46dc449026 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 170 | 353 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#45#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-08T15:12:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 171 | 355 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#45#c_2` | PERSON_5760_GITHUB_USERNAME, 2025-09-10T18:20:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 172 | 357 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#45#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED, 2025-09-08T15:16:00Z, seq 1 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 173 | 359 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#45#rev_2` | PERSON_2967_GITHUB_USERNAME CHANGES_REQUESTED, 2025-09-09T17:00:00Z, seq 2 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 174 | 361 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#45#rev_3` | PERSON_2967_GITHUB_USERNAME APPROVED, 2025-09-10T15:10:00Z, seq 3 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 175 | 363 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#45#ev_1` | review_requested, PERSON_5760_GITHUB_USERNAME, 2025-09-08T15:10:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 176 | 365 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#45#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-08T15:12:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 177 | 367 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#45#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-08T15:16:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 178 | 369 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#45#ev_4` | reviewed, PERSON_2967_GITHUB_USERNAME, 2025-09-09T17:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 179 | 371 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#45#ev_5` | reviewed, PERSON_2967_GITHUB_USERNAME, 2025-09-10T15:10:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 180 | 373 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#45#ev_6` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-10T16:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 181 | 375 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#45#ev_7` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-10T16:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 182 | 377 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#45#ev_8` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-10T18:20:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 183 | 379 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#46` | #46 by PERSON_5760_GITHUB_USERNAME, created 2025-09-09T15:30:00Z, merged 2025-09-09T19:50:00Z, merge_commit_sha NULL | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 184 | 381 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:economy-september-adjustments` | head 9bdbc503b5 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 185 | 383 | `github.github_commits` | INSERT | `9bdbc503b5894db868b678fc822b2b70994af699` | PERSON_5760_GITHUB_USERNAME / PERSON_5760_NAME, 2025-09-09T15:10:00Z, parents [] | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 186 | 385 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#46#c_0` | match3d-backend#46 → 9bdbc503b5 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 187 | 387 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#46#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-09T15:32:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 188 | 389 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#46#c_2` | PERSON_5760_GITHUB_USERNAME, 2025-09-09T20:29:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 189 | 391 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#46#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED, 2025-09-09T15:36:00Z, seq 1 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 190 | 393 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#46#rev_2` | EMPLOYEE_0025_GITHUB_USERNAME APPROVED, 2025-09-09T19:40:00Z, seq 2 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 191 | 395 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#46#ev_1` | review_requested, PERSON_5760_GITHUB_USERNAME, 2025-09-09T15:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 192 | 397 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#46#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-09T15:32:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 193 | 399 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#46#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-09T15:36:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 194 | 401 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#46#ev_4` | reviewed, EMPLOYEE_0025_GITHUB_USERNAME, 2025-09-09T19:40:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 195 | 403 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#46#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-09T19:50:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 196 | 405 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#46#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-09T19:50:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 197 | 407 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#46#ev_7` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-09T20:29:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 198 | 409 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#47` | #47 by PERSON_2967_GITHUB_USERNAME, created 2025-09-11T17:00:00Z, merged 2025-09-12T19:00:00Z, merge_commit_sha NULL | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 199 | 411 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:analytics-log-endless-start-on-the-serve` | head a0bdcab8e1 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 200 | 413 | `github.github_commits` | INSERT | `a0bdcab8e1b7b11ba1f04fec44b5c7bbd8d9a5d5` | PERSON_2967_GITHUB_USERNAME / PERSON_2967_NAME, 2025-09-11T16:40:00Z, parents [] | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 201 | 415 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#47#c_0` | match3d-backend#47 → a0bdcab8e1 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 202 | 417 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#47#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-11T17:02:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 203 | 419 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#47#c_2` | PERSON_2967_GITHUB_USERNAME, 2025-09-27T16:20:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 204 | 421 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#47#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED, 2025-09-11T17:06:00Z, seq 1 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 205 | 423 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#47#rev_2` | EMPLOYEE_0025_GITHUB_USERNAME APPROVED, 2025-09-27T16:05:00Z, seq 2 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 206 | 425 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#47#ev_1` | review_requested, PERSON_2967_GITHUB_USERNAME, 2025-09-11T17:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 207 | 427 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#47#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-11T17:02:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 208 | 429 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#47#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-11T17:06:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 209 | 431 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#47#ev_4` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-12T19:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 210 | 433 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#47#ev_5` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-12T19:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 211 | 435 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#47#ev_6` | reviewed, EMPLOYEE_0025_GITHUB_USERNAME, 2025-09-27T16:05:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 212 | 437 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#47#ev_7` | commented, PERSON_2967_GITHUB_USERNAME, 2025-09-27T16:20:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 213 | 439 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#48` | #48 by PERSON_2967_GITHUB_USERNAME, created 2025-09-15T13:00:00Z, merged 2025-09-16T15:40:00Z, merge_commit_sha NULL | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 214 | 441 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:boss-arena-infinite-hp-event-config` | head e299996667 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 215 | 443 | `github.github_commits` | INSERT | `e2999966670177f4f4644569bf44541e7806eea6` | PERSON_2967_GITHUB_USERNAME / PERSON_2967_NAME, 2025-09-15T12:40:00Z, parents [] | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 216 | 445 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#48#c_0` | match3d-backend#48 → e299996667 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 217 | 447 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#48#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-15T13:02:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 218 | 449 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#48#c_2` | PERSON_5760_GITHUB_USERNAME, 2025-09-16T16:35:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 219 | 451 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#48#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED, 2025-09-15T13:06:00Z, seq 1 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 220 | 453 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#48#rev_2` | PERSON_5760_GITHUB_USERNAME APPROVED, 2025-09-16T15:20:00Z, seq 2 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 221 | 455 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#48#ev_1` | review_requested, PERSON_2967_GITHUB_USERNAME, 2025-09-15T13:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 222 | 457 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#48#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-15T13:02:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 223 | 459 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#48#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-15T13:06:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 224 | 461 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#48#ev_4` | reviewed, PERSON_5760_GITHUB_USERNAME, 2025-09-16T15:20:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 225 | 463 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#48#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-16T15:40:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 226 | 465 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#48#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-16T15:40:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 227 | 467 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#48#ev_7` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-16T16:35:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 228 | 469 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#49` | #49 by PERSON_5760_GITHUB_USERNAME, created 2025-09-16T19:00:00Z, merged 2025-09-17T15:30:00Z, merge_commit_sha NULL | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 229 | 471 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:boss-arena-mirror-balance-values` | head 1a12a54aec | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 230 | 473 | `github.github_commits` | INSERT | `1a12a54aec100ae0603bed4310dc12f3ec431aec` | PERSON_5760_GITHUB_USERNAME / PERSON_5760_NAME, 2025-09-16T18:40:00Z, parents [] | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 231 | 475 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#49#c_0` | match3d-backend#49 → 1a12a54aec | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 232 | 477 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#49#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-16T19:02:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 233 | 479 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#49#c_2` | PERSON_5760_GITHUB_USERNAME, 2025-09-18T16:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 234 | 481 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#49#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED, 2025-09-16T19:06:00Z, seq 1 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 235 | 483 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#49#rev_2` | PERSON_2967_GITHUB_USERNAME APPROVED, 2025-09-17T15:10:00Z, seq 2 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 236 | 485 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#49#ev_1` | review_requested, PERSON_5760_GITHUB_USERNAME, 2025-09-16T19:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 237 | 487 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#49#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-16T19:02:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 238 | 489 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#49#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-16T19:06:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 239 | 491 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#49#ev_4` | reviewed, PERSON_2967_GITHUB_USERNAME, 2025-09-17T15:10:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 240 | 493 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#49#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-17T15:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 241 | 495 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#49#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-17T15:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 242 | 497 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#49#ev_7` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-18T16:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 243 | 499 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#50` | #50 by PERSON_2967_GITHUB_USERNAME, created 2025-09-18T15:00:00Z, merged 2025-09-19T15:30:00Z, merge_commit_sha NULL | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 244 | 501 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:boss-arena-don-t-take-a-life-on-a-win` | head 789f238dc3 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 245 | 503 | `github.github_commits` | INSERT | `789f238dc36a0e3c363244a78144494fa406c839` | PERSON_2967_GITHUB_USERNAME / PERSON_2967_NAME, 2025-09-18T14:40:00Z, parents [] | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 246 | 505 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#50#c_0` | match3d-backend#50 → 789f238dc3 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 247 | 507 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#50#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-18T15:02:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 248 | 509 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#50#c_2` | PERSON_2967_GITHUB_USERNAME, 2025-09-27T14:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 249 | 511 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#50#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED, 2025-09-18T15:06:00Z, seq 1 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 250 | 513 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#50#rev_2` | PERSON_5760_GITHUB_USERNAME APPROVED, 2025-09-19T15:10:00Z, seq 2 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 251 | 515 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#50#rev_3` | EMPLOYEE_0025_GITHUB_USERNAME COMMENTED, 2025-09-29T14:50:00Z, seq 3 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 252 | 517 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#50#ev_1` | review_requested, PERSON_2967_GITHUB_USERNAME, 2025-09-18T15:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 253 | 519 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#50#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-18T15:02:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 254 | 521 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#50#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-18T15:06:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 255 | 523 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#50#ev_4` | reviewed, PERSON_5760_GITHUB_USERNAME, 2025-09-19T15:10:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 256 | 525 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#50#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-19T15:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 257 | 527 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#50#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-19T15:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 258 | 529 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#50#ev_7` | commented, PERSON_2967_GITHUB_USERNAME, 2025-09-27T14:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 259 | 531 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#50#ev_8` | reviewed, EMPLOYEE_0025_GITHUB_USERNAME, 2025-09-29T14:50:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 260 | 533 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#51` | #51 by PERSON_5760_GITHUB_USERNAME, created 2025-09-18T20:00:00Z, merged 2025-09-19T22:00:00Z, merge_commit_sha NULL | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 261 | 535 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:trophy-path-ignore-duplicate-claim-reque` | head e737b6e606 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 262 | 537 | `github.github_commits` | INSERT | `e737b6e6064a0e19d4ab43a383826bc7d1e2e98e` | PERSON_5760_GITHUB_USERNAME / PERSON_5760_NAME, 2025-09-18T19:40:00Z, parents [] | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 263 | 539 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#51#c_0` | match3d-backend#51 → e737b6e606 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 264 | 541 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#51#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-18T20:02:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 265 | 543 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#51#c_2` | PERSON_5760_GITHUB_USERNAME, 2025-09-19T22:20:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 266 | 545 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#51#c_3` | EMPLOYEE_0012_GITHUB_USERNAME, 2025-09-22T09:14:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 267 | 547 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#51#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED, 2025-09-18T20:06:00Z, seq 1 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 268 | 549 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#51#rev_2` | PERSON_2967_GITHUB_USERNAME APPROVED, 2025-09-19T21:30:00Z, seq 2 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 269 | 551 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#51#ev_1` | review_requested, PERSON_5760_GITHUB_USERNAME, 2025-09-18T20:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 270 | 553 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#51#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-18T20:02:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 271 | 555 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#51#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-18T20:06:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 272 | 557 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#51#ev_4` | reviewed, PERSON_2967_GITHUB_USERNAME, 2025-09-19T21:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 273 | 559 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#51#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-19T22:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 274 | 561 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#51#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-19T22:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 275 | 563 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#51#ev_7` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-19T22:20:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 276 | 565 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#51#ev_8` | commented, EMPLOYEE_0012_GITHUB_USERNAME, 2025-09-22T09:14:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 277 | 567 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#52` | #52 by PERSON_5760_GITHUB_USERNAME, created 2025-09-22T12:10:00Z, merged 2025-09-22T15:05:00Z, merge_commit_sha NULL | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 278 | 569 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:teams-push-lives-refresh-to-client` | head 9caa48b0aa | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 279 | 571 | `github.github_commits` | INSERT | `9caa48b0aaac58c23661589a23c048e37bafbfed` | PERSON_5760_GITHUB_USERNAME / PERSON_5760_NAME, 2025-09-22T11:50:00Z, parents [] | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 280 | 573 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#52#c_0` | match3d-backend#52 → 9caa48b0aa | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 281 | 575 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#52#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-22T12:12:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 282 | 577 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#52#c_2` | PERSON_5760_GITHUB_USERNAME, 2025-09-30T18:16:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 283 | 579 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#52#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED, 2025-09-22T12:16:00Z, seq 1 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 284 | 581 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#52#rev_2` | PERSON_2967_GITHUB_USERNAME APPROVED, 2025-09-22T14:50:00Z, seq 2 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 285 | 583 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#52#ev_1` | review_requested, PERSON_5760_GITHUB_USERNAME, 2025-09-22T12:10:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 286 | 585 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#52#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-22T12:12:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 287 | 587 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#52#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-22T12:16:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 288 | 589 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#52#ev_4` | reviewed, PERSON_2967_GITHUB_USERNAME, 2025-09-22T14:50:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 289 | 591 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#52#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-22T15:05:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 290 | 593 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#52#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-22T15:05:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 291 | 595 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#52#ev_7` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-30T18:16:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 292 | 597 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#53` | #53 by PERSON_5760_GITHUB_USERNAME, created 2025-09-22T16:00:00Z, merged 2025-09-23T15:30:00Z, merge_commit_sha NULL | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 293 | 599 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:boss-arena-mirror-refill-and-nuke-values` | head 51677370b7 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 294 | 601 | `github.github_commits` | INSERT | `51677370b7a345efc26e88b7576890fa5c7d0419` | PERSON_5760_GITHUB_USERNAME / PERSON_5760_NAME, 2025-09-22T15:40:00Z, parents [] | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 295 | 603 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#53#c_0` | match3d-backend#53 → 51677370b7 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 296 | 605 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#53#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-22T16:02:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 297 | 607 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#53#c_2` | PERSON_5760_GITHUB_USERNAME, 2025-09-24T16:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 298 | 609 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#53#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED, 2025-09-22T16:06:00Z, seq 1 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 299 | 611 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#53#rev_2` | PERSON_2967_GITHUB_USERNAME APPROVED, 2025-09-23T15:15:00Z, seq 2 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 300 | 613 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#53#ev_1` | review_requested, PERSON_5760_GITHUB_USERNAME, 2025-09-22T16:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 301 | 615 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#53#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-22T16:02:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 302 | 617 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#53#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-22T16:06:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 303 | 619 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#53#ev_4` | reviewed, PERSON_2967_GITHUB_USERNAME, 2025-09-23T15:15:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 304 | 621 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#53#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-23T15:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 305 | 623 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#53#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-23T15:30:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 306 | 625 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#53#ev_7` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-24T16:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 307 | 627 | `github.github_pull_requests` | INSERT | `harmonygames-Games/match3d-backend#54` | #54 by PERSON_5760_GITHUB_USERNAME, created 2025-09-22T18:00:00Z, merged 2025-09-23T16:00:00Z, merge_commit_sha NULL | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 308 | 629 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:login-streak-count-days-in-player-timezo` | head d0a473f060 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 309 | 631 | `github.github_commits` | INSERT | `d0a473f0607318375786577d523bf5972f502c2c` | PERSON_5760_GITHUB_USERNAME / PERSON_5760_NAME, 2025-09-22T17:40:00Z, parents [] | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 310 | 633 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/match3d-backend#54#c_0` | match3d-backend#54 → d0a473f060 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 311 | 635 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#54#c_1` | PERSON_6026_GITHUB_USERNAME, 2025-09-22T18:02:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 312 | 637 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#54#c_2` | PERSON_5760_GITHUB_USERNAME, 2025-09-24T19:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 313 | 639 | `github.github_pr_comments` | INSERT | `harmonygames-Games/match3d-backend#54#c_3` | PERSON_5760_GITHUB_USERNAME, 2025-09-28T03:10:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 314 | 641 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#54#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED, 2025-09-22T18:06:00Z, seq 1 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 315 | 643 | `github.github_reviews` | INSERT | `harmonygames-Games/match3d-backend#54#rev_2` | PERSON_2967_GITHUB_USERNAME APPROVED, 2025-09-23T15:20:00Z, seq 2 | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 316 | 645 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#54#ev_1` | review_requested, PERSON_5760_GITHUB_USERNAME, 2025-09-22T18:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 317 | 647 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#54#ev_2` | commented, SVC_0321_GITHUB_USERNAME, 2025-09-22T18:02:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 318 | 649 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#54#ev_3` | reviewed, PERSON_6026_GITHUB_USERNAME, 2025-09-22T18:06:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 319 | 651 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#54#ev_4` | reviewed, PERSON_2967_GITHUB_USERNAME, 2025-09-23T15:20:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 320 | 653 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#54#ev_5` | merged, PERSON_5760_GITHUB_USERNAME, 2025-09-23T16:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 321 | 655 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#54#ev_6` | closed, PERSON_5760_GITHUB_USERNAME, 2025-09-23T16:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 322 | 657 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#54#ev_7` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-24T19:00:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 323 | 659 | `github.github_timeline_events` | INSERT | `harmonygames-Games/match3d-backend#54#ev_8` | commented, PERSON_5760_GITHUB_USERNAME, 2025-09-28T03:10:00Z | A ids/SHA free, logins resolve; C PR-internal chronology: PASS |
| 324 | 661 | `github.github_commits` | INSERT | `c219e8c3375700625d4371dc4adb6a519ace58aa` | PERSON_5760_GITHUB_USERNAME / PERSON_5760_NAME, 2025-09-30T18:05:00Z, parents [] | A SHA free, login resolves; C after #52 merge, before prod comment: PASS |
| 325 | 663 | `github.github_branches` | INSERT | `harmonygames-Games/match3d-backend:prod` | head c219e8c337, protected false, not default | A id/name free, head SHA resolves; C head = latest prod cherry-pick: PASS |
| 326 | 666 | `linear.linear_comments` | INSERT | `cmt_0b9e52e7a05129c16301` | ZOM-459, usr_cc3e90160f490686, 2025-08-25T11:40:00Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 327 | 668 | `linear.linear_comments` | INSERT | `cmt_a50779a56d1833aec20b` | ZOM-457, usr_65c76e0b87aa7e9b, 2025-08-25T11:46:02Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 328 | 670 | `linear.linear_comments` | INSERT | `cmt_d08125bf464ffe16ff64` | ZOM-447, usr_cc3e90160f490686, 2025-08-25T09:58:20Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 329 | 672 | `linear.linear_comments` | INSERT | `cmt_aa3a4b36e887c4d668a4` | ZOM-474, usr_65c76e0b87aa7e9b, 2025-08-25T09:23:20Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 330 | 674 | `linear.linear_comments` | INSERT | `cmt_9ab4df8400bed355857e` | ZOM-470, usr_caafeec2804b3a67, 2025-08-25T11:09:26Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 331 | 676 | `linear.linear_comments` | INSERT | `cmt_52185b2931cef92943d3` | ZOM-464, usr_c77c50cc15c5342d, 2025-09-02T10:34:58Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 332 | 678 | `linear.linear_comments` | INSERT | `cmt_9e73c35e85bd1e054a56` | ZOM-497, usr_caafeec2804b3a67, 2025-09-02T12:32:48Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 333 | 680 | `linear.linear_comments` | INSERT | `cmt_3dcb72194895e1b92230` | ZOM-486, usr_65c76e0b87aa7e9b, 2025-09-02T10:27:27Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 334 | 682 | `linear.linear_comments` | INSERT | `cmt_98486e4ab765193640da` | ZOM-495, usr_cc3e90160f490686, 2025-09-02T12:51:23Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 335 | 684 | `linear.linear_comments` | INSERT | `cmt_088a84d96b94ef39674a` | ZOM-496, usr_65c76e0b87aa7e9b, 2025-09-02T12:35:27Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 336 | 686 | `linear.linear_comments` | INSERT | `cmt_6a00a703fed52e7c11fe` | ZOM-501, usr_caafeec2804b3a67, 2025-09-02T11:44:42Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 337 | 688 | `linear.linear_comments` | INSERT | `cmt_18cc4fec19f0d669b9aa` | ZOM-485, usr_65c76e0b87aa7e9b, 2025-09-02T11:30:37Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 338 | 690 | `linear.linear_comments` | INSERT | `cmt_1aff31775b961e6129d4` | ZOM-466, usr_49b9dfa5208d400d, 2025-09-02T13:08:01Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 339 | 692 | `linear.linear_comments` | INSERT | `cmt_45367ccda4895c792313` | ZOM-332, usr_7fe31e7ec8199618, 2025-09-03T15:35:41Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 340 | 694 | `linear.linear_comments` | INSERT | `cmt_6208df52348b4ffc8b30` | ZOM-127, usr_7fe31e7ec8199618, 2025-09-03T13:44:46Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 341 | 696 | `linear.linear_comments` | INSERT | `cmt_f916fc632f4d7a220a9a` | ZOM-265, usr_7fe31e7ec8199618, 2025-09-03T13:59:24Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 342 | 698 | `linear.linear_comments` | INSERT | `cmt_bbbd0687c4431af35535` | ZOM-338, usr_7fe31e7ec8199618, 2025-09-03T14:23:13Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 343 | 700 | `linear.linear_comments` | INSERT | `cmt_96aafd5ba312028e7391` | ZOM-340, usr_7fe31e7ec8199618, 2025-09-03T15:29:40Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 344 | 702 | `linear.linear_comments` | INSERT | `cmt_c69a63ac9dbd4826b955` | ZOM-335, usr_7fe31e7ec8199618, 2025-09-03T13:31:13Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 345 | 704 | `linear.linear_comments` | INSERT | `cmt_877095d931428f1536df` | ZOM-336, usr_7fe31e7ec8199618, 2025-09-03T15:50:00Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 346 | 706 | `linear.linear_comments` | INSERT | `cmt_860e5862211fe64ac0da` | ZOM-331, usr_7fe31e7ec8199618, 2025-09-03T13:54:27Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 347 | 708 | `linear.linear_comments` | INSERT | `cmt_aac3d150bafe119754f8` | ZOM-339, usr_7fe31e7ec8199618, 2025-09-03T13:27:18Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 348 | 710 | `linear.linear_comments` | INSERT | `cmt_bbc8084b40022773292c` | ZOM-337, usr_7fe31e7ec8199618, 2025-09-03T13:36:44Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 349 | 712 | `linear.linear_comments` | INSERT | `cmt_6f75f609688a3ed60aba` | ZOM-502, usr_65c76e0b87aa7e9b, 2025-09-04T08:31:02Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 350 | 714 | `linear.linear_comments` | INSERT | `cmt_4362bbdda4049c5dd30d` | ZOM-476, usr_65c76e0b87aa7e9b, 2025-09-04T09:31:52Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 351 | 716 | `linear.linear_comments` | INSERT | `cmt_d02aec11deff05b555cc` | ZOM-392, usr_cc3e90160f490686, 2025-09-04T10:20:00Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 352 | 718 | `linear.linear_comments` | INSERT | `cmt_112afca3ef67b713a9e7` | ZOM-509, usr_bdf01b53c6a92c5e, 2025-09-04T10:15:00Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 353 | 720 | `linear.linear_comments` | INSERT | `cmt_99069485a5f5d5eb9ce3` | ZOM-518, usr_65c76e0b87aa7e9b, 2025-09-04T12:55:00Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 354 | 722 | `linear.linear_comments` | INSERT | `cmt_0f256875faad3cad9843` | ZOM-510, usr_bdf01b53c6a92c5e, 2025-09-11T16:45:00Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 355 | 724 | `linear.linear_comments` | INSERT | `cmt_57ce6f9bc61a928159ce` | ZOM-519, usr_c77c50cc15c5342d, 2025-09-11T14:17:24Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 356 | 726 | `linear.linear_comments` | INSERT | `cmt_bc49540005814cc8f0e1` | ZOM-256, usr_63fffeb4fab5233e, 2025-09-11T16:48:00Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 357 | 728 | `linear.linear_comments` | INSERT | `cmt_58afcdd4871aac77a852` | ZOM-540, usr_65c76e0b87aa7e9b, 2025-09-12T16:04:38Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 358 | 730 | `linear.linear_comments` | INSERT | `cmt_81278f65a6828964fd37` | ZOM-531, usr_65c76e0b87aa7e9b, 2025-09-15T15:01:00Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 359 | 732 | `linear.linear_comments` | INSERT | `cmt_f3fd31480ea0ad163b4c` | ZOM-512, usr_65c76e0b87aa7e9b, 2025-09-15T12:28:15Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 360 | 734 | `linear.linear_comments` | INSERT | `cmt_92b95a95aa3414a22c89` | ZOM-537, usr_cd7849ec043ab3da, 2025-09-15T15:05:00Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 361 | 736 | `linear.linear_comments` | INSERT | `cmt_32c3a18150bf06ad3a12` | ZOM-444, usr_bdf01b53c6a92c5e, 2025-09-15T15:06:00Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 362 | 738 | `linear.linear_comments` | INSERT | `cmt_9f00cd5152233dc95ff4` | ZOM-515, usr_65c76e0b87aa7e9b, 2025-09-15T12:20:20Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 363 | 740 | `linear.linear_comments` | INSERT | `cmt_a413bcc2401d50df1cc6` | ZOM-493, usr_49b9dfa5208d400d, 2025-09-15T14:47:44Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 364 | 742 | `linear.linear_comments` | INSERT | `cmt_5933eeaa473e3376dc0a` | ZOM-491, usr_49b9dfa5208d400d, 2025-09-15T14:08:56Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 365 | 744 | `linear.linear_comments` | INSERT | `cmt_dd19ad17ac459bc0f50e` | ZOM-463, usr_49b9dfa5208d400d, 2025-09-15T15:09:56Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 366 | 746 | `linear.linear_comments` | INSERT | `cmt_f0049fd2ef671c2b95d1` | ZOM-383, usr_cc3e90160f490686, 2025-09-15T13:46:52Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 367 | 748 | `linear.linear_comments` | INSERT | `cmt_7c7780e6f01e8b2c5103` | ZOM-436, usr_bdf01b53c6a92c5e, 2025-09-17T15:08:39Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 368 | 750 | `linear.linear_comments` | INSERT | `cmt_22a38511a35757459956` | ZOM-421, usr_49b9dfa5208d400d, 2025-09-17T15:26:01Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 369 | 752 | `linear.linear_comments` | INSERT | `cmt_2419c07aa4f77f4a3536` | ZOM-525, usr_49b9dfa5208d400d, 2025-09-17T12:55:28Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 370 | 754 | `linear.linear_comments` | INSERT | `cmt_92867e48f99e1dfd8ba3` | ZOM-523, usr_49b9dfa5208d400d, 2025-09-17T14:08:11Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 371 | 756 | `linear.linear_comments` | INSERT | `cmt_edbbbb8c0b8ced6e4401` | ZOM-524, usr_49b9dfa5208d400d, 2025-09-17T15:36:52Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 372 | 758 | `linear.linear_comments` | INSERT | `cmt_b197d27aaaba58c9b89f` | ZOM-499, usr_49b9dfa5208d400d, 2025-09-17T15:44:00Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 373 | 760 | `linear.linear_comments` | INSERT | `cmt_93d0e4f86d854d279b99` | ZOM-478, usr_49b9dfa5208d400d, 2025-09-17T15:22:09Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 374 | 762 | `linear.linear_comments` | INSERT | `cmt_9a6e40246a899fc380bc` | ZOM-547, usr_65c76e0b87aa7e9b, 2025-09-17T16:01:00Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 375 | 764 | `linear.linear_comments` | INSERT | `cmt_2d985b12de71739e6b82` | ZOM-511, usr_c77c50cc15c5342d, 2025-09-17T15:19:00Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 376 | 766 | `linear.linear_comments` | INSERT | `cmt_41e71e303718899c0d3c` | ZOM-487, usr_65c76e0b87aa7e9b, 2025-09-17T16:09:00Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 377 | 768 | `linear.linear_comments` | INSERT | `cmt_ad7d4901835f513674cd` | ZOM-530, usr_bdf01b53c6a92c5e, 2025-09-18T16:04:18Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 378 | 770 | `linear.linear_comments` | INSERT | `cmt_7cea4a71e9934e0c587c` | ZOM-500, usr_bdf01b53c6a92c5e, 2025-09-19T13:42:00Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 379 | 772 | `linear.linear_comments` | INSERT | `cmt_a5d743a4487fb4aad196` | ZOM-527, usr_49b9dfa5208d400d, 2025-09-19T15:27:52Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 380 | 774 | `linear.linear_comments` | INSERT | `cmt_2e0b9655e5d932f6b7e1` | ZOM-550, usr_65c76e0b87aa7e9b, 2025-09-19T16:10:00Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 381 | 776 | `linear.linear_comments` | INSERT | `cmt_8dbc7c9e3101efc08508` | ZOM-435, usr_bdf01b53c6a92c5e, 2025-09-22T13:49:00Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 382 | 778 | `linear.linear_comments` | INSERT | `cmt_6cdfde887dc9d5875a19` | ZOM-434, usr_bdf01b53c6a92c5e, 2025-09-22T13:26:18Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 383 | 780 | `linear.linear_comments` | INSERT | `cmt_d9d13434b3b6cdbe8c09` | ZOM-507, usr_bdf01b53c6a92c5e, 2025-09-22T12:08:03Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 384 | 782 | `linear.linear_comments` | INSERT | `cmt_bcb9a5974b2de811c2af` | ZOM-169, usr_bdf01b53c6a92c5e, 2025-09-22T14:20:59Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 385 | 784 | `linear.linear_comments` | INSERT | `cmt_c95585f37ce6708a9ec4` | ZOM-503, usr_4e13bd40cc73d0fc, 2025-09-22T15:08:00Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 386 | 786 | `linear.linear_comments` | INSERT | `cmt_80ecf3a45d73d6e13170` | ZOM-473, usr_65c76e0b87aa7e9b, 2025-09-22T14:17:06Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 387 | 788 | `linear.linear_comments` | INSERT | `cmt_cdd62a5e38fdf8d59a57` | ZOM-419, usr_fc22d5941b2aeb5c, 2025-09-22T14:55:01Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 388 | 790 | `linear.linear_comments` | INSERT | `cmt_09ce815cd0da097ee561` | ZOM-239, usr_65c76e0b87aa7e9b, 2025-09-22T12:38:16Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 389 | 792 | `linear.linear_comments` | INSERT | `cmt_445caf64da6e5d8fb2af` | ZOM-506, usr_49b9dfa5208d400d, 2025-09-22T13:45:31Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 390 | 794 | `linear.linear_comments` | INSERT | `cmt_9e4897d4fa0c8f01b3c1` | ZOM-538, usr_c77c50cc15c5342d, 2025-09-23T12:56:12Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 391 | 796 | `linear.linear_comments` | INSERT | `cmt_fb8aec8f0d94d5dadc69` | ZOM-112, usr_c77c50cc15c5342d, 2025-09-23T12:23:48Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 392 | 798 | `linear.linear_comments` | INSERT | `cmt_6df7394cf11eed76b50c` | ZOM-558, usr_caafeec2804b3a67, 2025-09-23T11:56:35Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 393 | 800 | `linear.linear_comments` | INSERT | `cmt_361d1945d189b0587159` | ZOM-536, usr_caafeec2804b3a67, 2025-09-30T09:47:04Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 394 | 802 | `linear.linear_comments` | INSERT | `cmt_68b41719f7d3ea9ff0fe` | ZOM-498, usr_caafeec2804b3a67, 2025-09-30T10:38:37Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 395 | 804 | `linear.linear_comments` | INSERT | `cmt_dbd1c3ba1c96a97fdc3f` | ZOM-555, usr_bdf01b53c6a92c5e, 2025-09-30T11:21:15Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 396 | 806 | `linear.linear_comments` | INSERT | `cmt_c2bad7e49457b4f6c558` | ZOM-553, usr_65c76e0b87aa7e9b, 2025-09-30T12:38:00Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 397 | 808 | `linear.linear_comments` | INSERT | `cmt_e850768746208eefe527` | ZOM-557, usr_bdf01b53c6a92c5e, 2025-09-30T12:39:00Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 398 | 810 | `linear.linear_comments` | INSERT | `cmt_b4c2115bb1a33be756ae` | ZOM-561, usr_65c76e0b87aa7e9b, 2025-09-30T10:27:27Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 399 | 812 | `linear.linear_comments` | INSERT | `cmt_7777dfa66681d9a8aa7a` | ZOM-461, usr_cc3e90160f490686, 2025-08-25T11:45:00Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 400 | 814 | `linear.linear_comments` | INSERT | `cmt_b3046e62e82ef09c3139` | ZOM-480, usr_65c76e0b87aa7e9b, 2025-08-25T10:14:32Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 401 | 816 | `linear.linear_comments` | INSERT | `cmt_43d06395046a31ca5a99` | ZOM-479, usr_65c76e0b87aa7e9b, 2025-08-25T09:52:01Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 402 | 818 | `linear.linear_comments` | INSERT | `cmt_be76fa616764ca440ae2` | ZOM-489, usr_bdf01b53c6a92c5e, 2025-08-25T08:30:50Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 403 | 820 | `linear.linear_comments` | INSERT | `cmt_b61f9c6d82a6b4cf9455` | ZOM-535, usr_65c76e0b87aa7e9b, 2025-09-30T14:44:39Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 404 | 822 | `linear.linear_issues` | UPDATE | `ZOM-535` | SET updated_at = 2025-09-30T14:44:39Z WHERE id = 'ZOM-535' | A target exists; C updated_at = comment time > base updated_at: PASS |
| 405 | 823 | `linear.linear_comments` | INSERT | `cmt_c4fb570f231f9c8d8cd2` | ZOM-504, usr_65c76e0b87aa7e9b, 2025-09-30T14:37:05Z | A issue/author resolve, id free; C vs issue created/completed/updated: PASS |
| 406 | 825 | `linear.linear_issues` | UPDATE | `ZOM-504` | SET updated_at = 2025-09-30T14:37:05Z WHERE id = 'ZOM-504' | A target exists; C updated_at = comment time > base updated_at: PASS |

## 9. Stage dependencies for reuse

`/prompt` may reuse these static checks only while all of the following are unchanged:

- SQL SHA-256 `5918bcb0e3eb29dbd0066537ff99a2f9ae5eb7198202d5dd136718570c8f15a7`
- synth-cut universe manifest `da2f4cf0…ac1a` and the base manifests in §1
- `injection.json` `31dcb2b4…5151`
- `id_contracts.json` `fc4711ef…d4682`
- Eval 0 `b1ea752a…3d3a`
- the fixed clock 2025-10-01 07:00 UTC

Any SQL edit invalidates the whole ledger. The saved `/prompt` report predates this SQL revision and must be rerun. Prompt-specific incorporation, discoverability, persona access and solvability are not covered here.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt (rerun /prompt; the saved /prompt report predates this SQL revision)

Evidence limits: No required static check is unresolved. Outside scope: live deployment and current DB compatibility (`seq`, `sequence` and both Confluence tables are not in the unverified schema snapshot), Slack thread_ts_legacy platform mapping, Agent visibility, task difficulty.
