# Injection Data-Integrity Review — `/injection`

Review version: `injection-static-v2`
Evidence contract: `stage-evidence-v1` (reused_evidence: none — all checks NEW)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

## 1. Scope

| Item | Value |
|---|---|
| Review | Chat/attachment review, portal attempt 6ad90ea979eb9e5d89f8879f, audit mode |
| Actual review time | 2026-10-26T15:44Z |
| Universe | `Universe_SynthCut` — hg4-synth-sep30cut v16; `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` (archive SHA-256 `d04f295b…fb0c`) |
| Reviewed input | `Evals/task_inputs/01_Universe_Inject.sql` (input revision 3, attached as `01_Universe_Inject.sql`), 173,315 bytes, SHA-256 `f48302c6acecb4bcec64c6f75b077bfba7f82ae842f747cc56d83377f83a71f1` |
| Assignment (context only) | Douglas — Software Engineer; Engineering / Engineering Ops / Retrieval / long-horizon / medium |
| Rules | `Evals/0_Injection_Quality_Eval.md` SHA-256 `b1ea752a…3d3a`; WORKFLOW.md SHA-256 `ee4cd8e1…fcd5d`; scoring.json SHA-256 `5e0bed76…00c3`; schema snapshot `injection.json` SHA-256 `31dcb2b4…5151`; `id_contracts.json` SHA-256 `fc4711ef…d4682` |
| Lint | `hg_injection_lint.py` `injection-lint-v1`, universe synthcut, clock 2025-10-01T07:00:00Z |
| Evaluator | Session model Opus 5.5 (claude-opus-5-5) |

### Input manifest entry (recorded here)

`hg_write_output.py` has no `input_manifest` key, and this review may write under `reports/` only through that writer. So the injection manifest entry is recorded in this report instead of a separate `input_manifest.json`:

```json
{"injection": {"review_version": "injection-static-v2", "evidence_contract": "stage-evidence-v1",
  "inputs": {"01_Universe_Inject.sql": {"sha256": "f48302c6acecb4bcec64c6f75b077bfba7f82ae842f747cc56d83377f83a71f1", "bytes": 173315, "input_revision": 3}},
  "universe_manifest_sha256": "da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a",
  "reused_evidence": []}}
```

### Base sources read (SHA-256)

| Source (under `Universe_SynthCut/`) | SHA-256 | Use |
|---|---|---|
| `SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json` | `ee578c91…7538` | users, repositories, PRs, branches, commits, PR commits, reviews, PR comments, timeline events (full collections) |
| `…Other_Services/Services_Data/linear/data.json` | `b49ec9e8…b4d` | issues (3,687), users (41), comments (0) |
| `…Other_Services/Services_Data/trello/data.json` | `6ba242f4…e3f` | boards, lists, members, cards (803), actions (5,252) |
| `…Other_Services/Services_Data/gdrive/data.json` | `05147aa2…d72` | drive_files (53,631), drive_users (25) |
| `…Other_Services/Services_Data/gdocs/data.json` | `1b53998d…c21` | docs_documents (595) |
| `…Other_Services/Services_Data/gsheets/data.json` | `a9cc229c…28f` | sheets_spreadsheets (356) |
| `…Other_Services/Services_Data/gcal/data.json` | `4f093d89…51e` | events (10,395), calendars (38) |
| `…Other_Services/Services_Data/confluence/confluence_working.json` | `d3f13938…37f0` | pages (30), spaces (4), users (37), page_versions (58) |
| `…Other_Services/Services_Data/slack/channels.json`, `users.json`, `messages/*/*.json` | `3cca0f7e…6cc`, `6aac5103…dc` | channel membership, user identity, all message files (id/ts collisions) |
| `SynthCut_HarmonyGames_Gmail/Services_Data/gmail/users.json`, `threads/*.json` (81,404 files) | `9a90b6bf…403` | mailboxes; exact-string scan of every thread file |

## 2. Input / authority issues

- Only input for this stage is the SQL, which was supplied and saved. No missing inputs.
- The SQL header comments (`-- Are you planning to inject? Yes`, persona/services summary, "Literal values only; parents before children; re-apply this exact SQL before every agent run") are author notes. None addresses a solver or grader, or mentions tool calls or pass rate. The header's count claim (402 INSERT, 2 UPDATE) matches the parse.
- The schema snapshot is unverified and does not cover Confluence tables. Snapshot comparisons below are provisional advisories (schema README).

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, base manifest, review version | NEW — done |
| Run `hg_injection_lint.py`; resolve every flag | NEW — 0 FAIL / 0 CHECK / 0 INFO |
| Inventory every statement and affected record | NEW — 406 statements: BEGIN, 402 single-row INSERT, 2 UPDATE, COMMIT (ledger §8) |
| Check A — references, collisions, ID contracts, readable Drive files, one account per person | NEW — PASS |
| Check B — SQL structure and supported schema rules | NEW — PASS (provisional snapshot advisories listed) |
| Check C — dates, relationships, consistency | NEW — PASS |
| Report coverage, findings, limits, one verdict | NEW — done |

## 4. Lint flags and resolution

`counts: FAIL 0, CHECK 0, INFO 0`; statements 406 (begin 1, insert 402, update 2, commit 1); unparsed: none. Base files loaded by lint: confluence, slack users, trello, gmail users, github, linear, contacts. Checks run: future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape. No flags to resolve. A clean lint was not treated as a PASS; checks A–C below were done in full.

## 5. Checks A–C

| Check | Result | Evidence |
|---|---|---|
| A — Records, references and IDs | PASS | Every referenced actor, parent and target resolves; every new key is free in the full relevant base collection and unique within the SQL. Details below. |
| B — SQL structure and supported schema rules | PASS | All 402 INSERTs are single-row with matching column/value counts, no duplicate columns, no ON CONFLICT or trailing clauses; inside BEGIN/COMMIT; no generated columns set; Linear text timestamps are `YYYY-MM-DDTHH:MM:SSZ`; no NOT NULL column left out; JSON columns have the base shape. Snapshot gaps are advisory only (below). |
| C — Dates, relationships and consistency | PASS | Every event timestamp is at or before 2025-09-30T21:12:44Z, earlier than the clock (2025-10-01T07:00Z). Parent/child order holds. GitHub threads are internally consistent. Linear comments precede each issue's base completion/update, or come with a matching update. Cross-service facts agree. Details below. |

### Check A detail

- **GitHub** (repo `harmonygames-Games/match3d-backend` exists, default branch `main`). Base has PRs #1–#35 only, so injected #37–#54 collide with none (#36 is a numbering gap; no contract). Full-collection checks found 0 collisions for 18 PR ids, 18 branches (by id and repo+name), 18 commit SHAs, 18 PR-commit ids, 40 comment ids, 37 review ids and 131 timeline ids, and 0 duplicates among all injected SHAs. No base child row already points at match3d-backend PR ≥ 36. Logins resolve to base users: `PERSON_5760_GITHUB_USERNAME` (name "Douglas", douglas@harmonygames.co), `PERSON_2967_GITHUB_USERNAME` (the existing second match3d-backend developer: 139 base commits, author of base PRs), `EMPLOYEE_0025_GITHUB_USERNAME` (Arthur Blake), `EMPLOYEE_0012_GITHUB_USERNAME` (Vincent Parker), `PERSON_6026_GITHUB_USERNAME` (coderabbit org) and `SVC_0321_GITHUB_USERNAME` (bot). Every PR `head_sha` is an injected commit. `base_sha`/parent SHAs are absent from base commits, matching base convention (2,411 of 2,475 base PRs have a `base_sha` that is not a base commit).
- **Linear**: all 79 `issue_id` targets and both UPDATE targets (`ZOM-535`, `ZOM-504`) exist. All 11 distinct `author_id` values resolve to base Linear users. Base `/comments` is empty (0 records, scan complete), so the 79 comment ids cannot collide; they are unique within the SQL, one comment per issue, `sequence` 1.
- **Slack**: channel `C0880U9751A` (#zombie-match3d) and DM `D05QQF7V404` exist. Authors `EMPLOYEE_0031_SLACK_ID` (Douglas), `EMPLOYEE_0025_SLACK_ID` (Arthur Blake) and `EMPLOYEE_0003_SLACK_ID` (Oliver Brooks) are members of every channel they post in (the DM lists Arthur and Douglas). A scan of all base message files found 0 id and 0 (channel, ts) collisions for the 9 messages. The two replies point at the injected parent `81531d5f…`.
- **Trello**: board `6851a6569f3bf818760632ab` (ZM ROADMAP), list `6851a674975da1fe76e70d93` (BETA: Oct 10, on that board) and member `2162c1ba310341bf318f48b7` (Arthur Blake) exist. Card ids, shortLinks (`twZVoQXy`, `ZWabErQX`) and 3 action ids are free (803 cards and 5,252 actions scanned). Board idShort max is 79, so 80/81 are free.
- **Drive/Docs/Sheets**: parents `d_cc3e90160f490686039986` (Arthur's root), `d_bdf01b53c6a92c5e167c65` (Oliver's root) and `d_cd7849ec043ab3da107f8c` (Douglas's root) exist. Each injected item's owner is that root's owner. The 4 new Drive ids are free (53,631 files), as are the new doc and spreadsheet ids (595 docs, 356 spreadsheets). Sharing emails all exist as Drive users. Readability: the Google Doc has a `docs_documents` row with a non-empty 1,399-char body; the Google Sheet has a `sheets_spreadsheets` row plus 2 `sheets_sheets` rows with grid data; the two folders need no content. No `content_path` is set, so the Drive content_path contract does not apply.
- **Confluence**: `space_OPS`, parent `page_ops_home` and author `user_EMPLOYEE_0025` (Arthur Blake) exist. New page ids, titles and version ids are free (30 pages, 58 versions).
- **Gmail**: mailboxes douglas, oliver.brooks, arthur.blake and leonard.hayes exist in `users.json`. No thread file exists under any of the six injected thread names, and an exact-string scan of all 81,404 thread files found no hit for the six thread numbers or either Message-ID. `history_id` is NULL on all 6 threads (contract satisfied).
- **Calendar**: all 5 calendars exist; 5 event ids and the shared iCalUID `463338c3…@hg4` are free (10,395 events).
- **One account per person**: no new account is created in any service. Every author resolves to one existing account per service, and the lint `identities` check passed.

### Check B detail

- Structure (static parse with the lint tokenizer plus an independent per-statement count): 402 INSERTs, each one VALUES tuple, column count = value count, 0 duplicate column names, 0 unparsed statements. Both UPDATEs have a literal `WHERE id = '…'`. The script is wrapped in BEGIN … COMMIT.
- Supported platform rules: `slack.slack_messages.text_fts` is not set; Slack `metadata_json` is `'{}'`. Linear `linear_comments.created_at/updated_at` and the UPDATE `updated_at` use `YYYY-MM-DDTHH:MM:SSZ`. No new `linear_issues` row is inserted, so `state_history_json` does not apply. `*_json` columns match the snapshot's array/object shape (lint json_shape: 0 flags).
- NOT NULL coverage (snapshot): no INSERT leaves out a NOT NULL, no-default, non-generated column.
- **Provisional snapshot comparison (advisory, not a defect):**

| Table | Column in SQL | Snapshot |
|---|---|---|
| `github.github_pull_requests` | `maintainer_can_modify`, `requested_team_slugs_json` | NOT COVERED |
| `github.github_reviews` | `seq` | NOT COVERED |
| `linear.linear_comments` | `sequence` | NOT COVERED |
| `gcal.gcal_events` | `extras_json` | NOT COVERED |
| `confluence.confluence_pages`, `confluence.confluence_page_versions` | all | table not in snapshot |
| all other affected tables/columns | — | MATCH |

  The README says a column missing from this unverified snapshot is advisory and does not prove the live table lacks it. It is listed because a missing column would roll back the whole transaction: if the platform load errors on any of these columns, remove that column first.

### Check C detail

- **Fixed clock**: the latest injected event timestamp is Slack `1e5d5d2b…` at 2025-09-30T21:12:44Z (lint future_date: 0). The only future dates are plan facts inside text (go/no-go Oct 2, beta Oct 10). Weekdays check out: Mon Sep 29, Tue Sep 30 (Gmail Date header), Thu Oct 2.
- **GitHub internal consistency** (programmatic, 18 PRs, 0 issues): commit authored < PR created < reviews/comments ≤ `updated_at` (= latest review/comment/merge); `merged_at` = `closed_at`; each review has exactly one matching `reviewed` timeline event (actor, time, state); each comment has a `commented` event (coderabbit comments use bot actor `SVC_0321`, as in all 264 base coderabbit comments); the `merged` event matches merged_by, time and merge commit; `review_requested` matches the requested reviewer and is never the author; review `seq` is chronological; branch head = PR head = PR-commit row; commit parent = PR `base_sha`.
- **Deploy log vs PR `prod:` comments**: all 7 Prod deploys rows (2025-08-25 → 2025-09-10, zm-api:41–47) match the PR comments' time, PRs, task def and deployer (PERSON_2967 / Douglas). Task-definition numbers rise with time through zm-api:57 (2025-09-30 18:16). The sheet's `modified_time` (2025-09-11 16:35) follows its last row (Console & imports, 09-11 16:30).
- **Drive doc vs base**: doc created 2025-06-01T18:30Z, after base PR #2 "Created new env for production" merged 2025-06-01T17:54Z. The doc's statement "since the prod env went up (match3d-backend#2)" is supported. The 2025-05-28 Slack message ("one environment for now") predates PR #2 (opened May 30), so it is valid stale context. The doc's process (manual task-definition update, merge doesn't deploy) agrees with base Confluence `page_cicd_pipeline`, which the doc cites by title and which exists.
- **Unapproved merges** (#40, #43 no approval; #41, #47 approved after merge): base `page_cicd_pipeline` says "required review before merge", but base match3d-backend itself has merges with no prior approval (#4, #6, #7). The injected records follow observed base practice and do not introduce a contradiction.
- **Linear**: each of the 77 comments on Done issues is dated before the issue's base `completed_at` and `updated_at`, and after its `created_at`. The two non-Done targets (ZOM-535 Todo, ZOM-504 Backlog) get comments after their base `updated_at`, and the UPDATEs bump `updated_at` to exactly those comment times. Each comment citing a match3d-backend PR is dated after that PR's merge (for example ZOM-547 16:01 after #49 merged 15:30 the same day; ZOM-503 15:08 after #52 merged 15:05). Linear issue ZOM-518 was created 2025-09-04T10:54Z; its comment (12:55) follows #43's merge (12:30).
- **Slack**: each `ts` equals `created_at`. The thread parent has `reply_count` 2, `reply_users_count` 2 (Arthur, Douglas) and `latest_reply` = last reply ts; replies follow the parent.
- **Trello**: Trello ObjectId timestamps equal the stated times (card 68dabfe9 → 2025-09-29T17:20:41Z = createCard date; 68dac311 → 17:34:09; comment action 68dbf1b7 → 2025-09-30T15:05:27Z = card `dateLastActivity`). `badges.comments` (1 / 0) matches the actions.
- **Gmail/Calendar**: `internal_date` equals `date` for all 6 messages; sender has a SENT copy and recipients/CC have INBOX copies. The freeze event (created 09-22, updated 09-23, start 2025-09-26T22:00Z) reads "Pulled in from Monday", which agrees with Arthur's 09-19 Slack message ("monday the 29th"). The `self` flag is on the calendar owner in each of the 5 copies.
- **Cross-service references**: the Trello card's pointers (deploy log first row, "match3d-backend prod deploys doc", sign-off folder named on the Confluence ZM Beta page) all resolve to injected records with those names. Arthur's email (ZOM-547/553 ↔ #49/#53 mirrors) agrees with the Linear comments and PR titles.
- **Stale or misleading statements kept as supported context, not defects**: Douglas 09-22 DM ("double claim fix is out", "algo seeds on prod since the 3rd"); Oliver 09-27 ("all the server fixes … are on prod now"); and the 2025-05 Domino Delights sign-off page. Each is contradicted by later or more authoritative records, which the eval allows ("a stale statement, later correction or misleading pointer can be valid when the records support that reading").
- **Pre-existing base oddities (context, not caused by SQL)**: DM `D05QQF7V404` is an `is_im` channel with 4 members; base `main` head `a0e4a218…` is not a base commit.

## 6. Findings

No demonstrated defect in A, B or C.

Advisories (optional; none changes the verdict):

1. **Snapshot columns not covered** (Check B, provisional): `maintainer_can_modify`, `requested_team_slugs_json` (github_pull_requests), `seq` (github_reviews), `sequence` (linear_comments), `extras_json` (gcal_events). If the platform load rejects any of them, drop that column from every INSERT of that table. Its values are defaults/NULL or derivable.
2. **Slack thread parent representation**: all 1,209 thread parents in base `C0880U9751A` export `thread_ts` = own ts. Injected parent `81531d5f36d48a5d2028a22405aed65e` (statement at SQL line 47) has `thread_ts_legacy` NULL. How that column maps for parents is undocumented. Setting it to `'1758937233.118904'` would mirror base.
3. **Douglas commit identity fields**: the 9 Douglas-authored injected commits use `author_name 'Douglas'` / `author_email 'douglas@harmonygames.co'` (his GitHub user profile values). His 68 base commits use `PERSON_5760_NAME` / `PERSON_5760_EMAIL`. Same login, so no second account; matching the base form is optional.
4. **GitHub fields the base never populates**: `merge_commit_sha` (base: 0 of 2,475 PRs) and non-empty `parent_shas_json` (base: 0 parent refs). Both point at SHAs absent from the commit table. No listed contract applies; leaving them NULL/`[]` would match base.
5. **Wording/timing nits**: ZOM-510 comment (2025-09-11 16:45) says the v7 rewards sheet "needs" importing, while the deploy log records that import to prod on 2025-09-08 16:45. Readable as naming the fix, not as pending work. The client-QA folder (created 2025-09-29 17:40) is mentioned by the Confluence page (17:15) and client card (17:34) shortly before it exists. Neither is an impossible chronology.

## 7. Evidence limits

- Required static checks: none unresolved.
- Outside certification scope (disclosed, not gates): live execution and deployment success; current database compatibility (the snapshot is unverified and lacks Confluence tables; see advisory 1); undocumented constraints; platform mapping of Slack `thread_ts_legacy`; search ranking; Agent visibility and persona access; task difficulty and discoverability (owned by `/prompt` and `/hardness`).
- Uniqueness is scoped to the local synth-cut base plus the SQL, not the live database.

## 8. Operation ledger (all 404 row operations, execution order)

Statement 1 (line 5) is `BEGIN;` and statement 406 (line 822) is `COMMIT;`. Rows below are statements 2–405. "#" is the row-operation order. Line numbers are the SQL file lines where each statement starts.

| # | Line | Table | Op | Record / target | Key values | Result |
|---|---|---|---|---|---|---|
| 1 | 7 | gdrive.drive_files | INSERT | `d_69fcebc484d472907b0b5c` | 2025-09-29T17:12:30Z | A new id, parent exists, owner = parent owner; C dates <= clock — PASS |
| 2 | 9 | gdrive.drive_files | INSERT | `d_d71300168ca5dffa4db8b3` | 2025-09-29T17:40:02Z | A new id, parent exists, owner = parent owner; C dates <= clock — PASS |
| 3 | 11 | gdrive.drive_files | INSERT | `f_470ae81236d5bd39045dc1` | 2025-06-01T18:30:00Z | A new id, parent exists, owner = parent owner; C dates <= clock — PASS |
| 4 | 13 | gdrive.drive_files | INSERT | `f_78bedc46245090a160d2dd` | 2025-08-25T12:05:00Z | A new id, parent exists, owner = parent owner; C dates <= clock — PASS |
| 5 | 16 | gdocs.docs_documents | INSERT | `f_470ae81236d5bd39045dc1` | 2025-06-01T18:30:00Z | A new id = drive file; C body 1399 chars = style runs — PASS |
| 6 | 19 | gsheets.sheets_spreadsheets | INSERT | `f_78bedc46245090a160d2dd` | 2025-08-25T12:05:00Z | A new id = drive file — PASS |
| 7 | 21 | gsheets.sheets_sheets | INSERT | `f_78bedc46245090a160d2dd / sheet 0 (Prod deploys)` |  | A parent sheet injected earlier; C rows match PR comments — PASS |
| 8 | 23 | gsheets.sheets_sheets | INSERT | `f_78bedc46245090a160d2dd / sheet 1 (Console & imports)` |  | A parent sheet injected earlier; C rows match PR comments — PASS |
| 9 | 26 | confluence.confluence_pages | INSERT | `page_dd_launch_server_signoff` | 2025-05-12T15:04:00Z | A new id, space_OPS + page_ops_home + user_EMPLOYEE_0025 exist — PASS |
| 10 | 28 | confluence.confluence_page_versions | INSERT | `ver_2ee4eb6acd67b53fc1013166dab4c1b5` | 2025-05-12T15:04:00Z | A new id, page injected earlier — PASS |
| 11 | 30 | confluence.confluence_pages | INSERT | `page_zm_beta_oct10` | 2025-09-29T17:15:00Z | A new id, space_OPS + page_ops_home + user_EMPLOYEE_0025 exist — PASS |
| 12 | 32 | confluence.confluence_page_versions | INSERT | `ver_338613da12d5a29e3e4947118c87f7ea` | 2025-09-29T17:15:00Z | A new id, page injected earlier — PASS |
| 13 | 35 | slack.slack_messages | INSERT | `3a2e99ef807fc28ef39b8d6973a44427` | C0880U9751A EMPLOYEE_0003_SLACK_ID 2025-05-28T16:42:17.204611Z | A new id/ts, author is channel member; C ts = created_at — PASS |
| 14 | 37 | slack.slack_messages | INSERT | `9ba4f3770f458826c7503e1aa0992acc` | C0880U9751A EMPLOYEE_0025_SLACK_ID 2025-09-19T15:21:08.611352Z | A new id/ts, author is channel member; C ts = created_at — PASS |
| 15 | 39 | slack.slack_messages | INSERT | `f5dde99eaea0ac1773ca37e48871cb60` | D05QQF7V404 EMPLOYEE_0031_SLACK_ID 2025-09-22T20:10:37.284511Z | A new id/ts, author is channel member; C ts = created_at — PASS |
| 16 | 41 | slack.slack_messages | INSERT | `10613025eb309bac6e0fb32438625484` | C0880U9751A EMPLOYEE_0003_SLACK_ID 2025-09-27T16:40:12.775031Z | A new id/ts, author is channel member; C ts = created_at — PASS |
| 17 | 43 | slack.slack_messages | INSERT | `42f263bfce69ae5a4ef068383ae66c4a` | C0880U9751A EMPLOYEE_0003_SLACK_ID 2025-09-30T17:31:46.093318Z | A new id/ts, author is channel member; C ts = created_at — PASS |
| 18 | 45 | slack.slack_messages | INSERT | `1e5d5d2bf50901f0d7376627d6f539e8` | D05QQF7V404 EMPLOYEE_0025_SLACK_ID 2025-09-30T21:12:44.508127Z | A new id/ts, author is channel member; C ts = created_at — PASS |
| 19 | 47 | slack.slack_messages | INSERT | `81531d5f36d48a5d2028a22405aed65e` | C0880U9751A EMPLOYEE_0031_SLACK_ID 2025-09-27T01:40:33.118904Z | A new id/ts, author is channel member; C ts = created_at — PASS |
| 20 | 49 | slack.slack_messages | INSERT | `33339417b07ab83542fc971a41320a36` | C0880U9751A EMPLOYEE_0025_SLACK_ID 2025-09-27T02:05:51.402267Z | A new id/ts, author is channel member; C ts = created_at — PASS |
| 21 | 51 | slack.slack_messages | INSERT | `bde0c0ff791441e66d57cdb2de8f0f51` | C0880U9751A EMPLOYEE_0031_SLACK_ID 2025-09-27T02:07:12.553908Z | A new id/ts, author is channel member; C ts = created_at — PASS |
| 22 | 54 | trello.trello_cards | INSERT | `68dabfe9bc2e8b969782e22d` |  | A new id/shortLink/idShort; board, list exist — PASS |
| 23 | 56 | trello.trello_actions | INSERT | `68dabfe93a26ef2186dcec1c` | 2025-09-29T17:20:41Z | A new id; Arthur member; C ObjectId time = date — PASS |
| 24 | 58 | trello.trello_cards | INSERT | `68dac311754b38be05be7ea9` |  | A new id/shortLink/idShort; board, list exist — PASS |
| 25 | 60 | trello.trello_actions | INSERT | `68dac311a286768d02a6385d` | 2025-09-29T17:34:09Z | A new id; Arthur member; C ObjectId time = date — PASS |
| 26 | 62 | trello.trello_actions | INSERT | `68dbf1b73eba0ba580f67a6e` | 2025-09-30T15:05:27Z | A new id; Arthur member; C ObjectId time = date — PASS |
| 27 | 65 | gmail.gmail_threads | INSERT | `douglas@harmonygames.co/1844719216755416739` |  | A new thread id, mailbox exists — PASS |
| 28 | 67 | gmail.gmail_messages | INSERT | `douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com>` | 2025-09-30T19:42:18Z | A new msg id; C internal_date = date — PASS |
| 29 | 75 | gmail.gmail_threads | INSERT | `oliver.brooks@harmonygames.co/1844719216754885141` |  | A new thread id, mailbox exists — PASS |
| 30 | 77 | gmail.gmail_messages | INSERT | `oliver.brooks@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com>` | 2025-09-30T19:42:18Z | A new msg id; C internal_date = date — PASS |
| 31 | 85 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844719216755483955` |  | A new thread id, mailbox exists — PASS |
| 32 | 87 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com>` | 2025-09-30T19:42:18Z | A new msg id; C internal_date = date — PASS |
| 33 | 95 | gmail.gmail_threads | INSERT | `douglas@harmonygames.co/1844721277206562572` |  | A new thread id, mailbox exists — PASS |
| 34 | 97 | gmail.gmail_messages | INSERT | `douglas@harmonygames.co/<CAreN_3nXHn9vq-8FWgVQEC3_2hxsSjSNZRkPtWB@mail.gmail.com>` | 2025-09-30T20:15:03Z | A new msg id; C internal_date = date — PASS |
| 35 | 104 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844721277207387678` |  | A new thread id, mailbox exists — PASS |
| 36 | 106 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAreN_3nXHn9vq-8FWgVQEC3_2hxsSjSNZRkPtWB@mail.gmail.com>` | 2025-09-30T20:15:03Z | A new msg id; C internal_date = date — PASS |
| 37 | 113 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844721277206833296` |  | A new thread id, mailbox exists — PASS |
| 38 | 115 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAreN_3nXHn9vq-8FWgVQEC3_2hxsSjSNZRkPtWB@mail.gmail.com>` | 2025-09-30T20:15:03Z | A new msg id; C internal_date = date — PASS |
| 39 | 123 | gcal.gcal_events | INSERT | `evt_b6eda0097a341f225ad5d2` | 2025-09-22T14:02:00Z | A new event id, calendar exists; shared iCalUID new — PASS |
| 40 | 125 | gcal.gcal_events | INSERT | `evt_0f489eb7fb46ada9660881` | 2025-09-22T14:02:00Z | A new event id, calendar exists; shared iCalUID new — PASS |
| 41 | 127 | gcal.gcal_events | INSERT | `evt_e3c3cd6a8dec19d0e7b123` | 2025-09-22T14:02:00Z | A new event id, calendar exists; shared iCalUID new — PASS |
| 42 | 129 | gcal.gcal_events | INSERT | `evt_5e9adacd9af476a6402dfa` | 2025-09-22T14:02:00Z | A new event id, calendar exists; shared iCalUID new — PASS |
| 43 | 131 | gcal.gcal_events | INSERT | `evt_bbe10af026c7f633387e2d` | 2025-09-22T14:02:00Z | A new event id, calendar exists; shared iCalUID new — PASS |
| 44 | 134 | github.github_pull_requests | INSERT | `harmonygames-Games/match3d-backend#37` | 2025-08-21T15:20:00Z | A new #, no base collision; C chronology ok — PASS |
| 45 | 136 | github.github_branches | INSERT | `harmonygames-Games/match3d-backend:algo-levels-spawn-points-from-the-server` |  | A new branch — PASS |
| 46 | 138 | github.github_commits | INSERT | `d96ec79123c2d518760e6b9a2ccc6433f931c488` | 2025-08-21T15:00:00Z | A new sha — PASS |
| 47 | 140 | github.github_pull_request_commits | INSERT | `harmonygames-Games/match3d-backend#37#c_0` |  | A new id; commit injected earlier — PASS |
| 48 | 142 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#37#c_1` | PERSON_6026_GITHUB_USERNAME 2025-08-21T15:22:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 49 | 144 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#37#c_2` | PERSON_2967_GITHUB_USERNAME 2025-08-25T11:52:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 50 | 146 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#37#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED 2025-08-21T15:26:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 51 | 148 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#37#rev_2` | PERSON_2967_GITHUB_USERNAME APPROVED 2025-08-25T09:00:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 52 | 150 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#37#ev_1` | review_requested PERSON_5760_GITHUB_USERNAME 2025-08-21T15:20:00Z | A new id; C matches review/comment/merge — PASS |
| 53 | 152 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#37#ev_2` | commented SVC_0321_GITHUB_USERNAME 2025-08-21T15:22:00Z | A new id; C matches review/comment/merge — PASS |
| 54 | 154 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#37#ev_3` | reviewed PERSON_6026_GITHUB_USERNAME 2025-08-21T15:26:00Z | A new id; C matches review/comment/merge — PASS |
| 55 | 156 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#37#ev_4` | reviewed PERSON_2967_GITHUB_USERNAME 2025-08-25T09:00:00Z | A new id; C matches review/comment/merge — PASS |
| 56 | 158 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#37#ev_5` | merged PERSON_5760_GITHUB_USERNAME 2025-08-25T09:10:00Z | A new id; C matches review/comment/merge — PASS |
| 57 | 160 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#37#ev_6` | closed PERSON_5760_GITHUB_USERNAME 2025-08-25T09:10:00Z | A new id; C matches review/comment/merge — PASS |
| 58 | 162 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#37#ev_7` | commented PERSON_2967_GITHUB_USERNAME 2025-08-25T11:52:00Z | A new id; C matches review/comment/merge — PASS |
| 59 | 164 | github.github_pull_requests | INSERT | `harmonygames-Games/match3d-backend#38` | 2025-08-22T15:10:00Z | A new #, no base collision; C chronology ok — PASS |
| 60 | 166 | github.github_branches | INSERT | `harmonygames-Games/match3d-backend:plague-race-count-algo-levels` |  | A new branch — PASS |
| 61 | 168 | github.github_commits | INSERT | `b1388ff2f8d945f005ea87b236afbab0c14e6e64` | 2025-08-22T14:50:00Z | A new sha — PASS |
| 62 | 170 | github.github_pull_request_commits | INSERT | `harmonygames-Games/match3d-backend#38#c_0` |  | A new id; commit injected earlier — PASS |
| 63 | 172 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#38#c_1` | PERSON_6026_GITHUB_USERNAME 2025-08-22T15:12:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 64 | 174 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#38#c_2` | PERSON_2967_GITHUB_USERNAME 2025-08-25T11:52:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 65 | 176 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#38#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED 2025-08-22T15:16:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 66 | 178 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#38#rev_2` | PERSON_2967_GITHUB_USERNAME APPROVED 2025-08-25T09:20:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 67 | 180 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#38#ev_1` | review_requested PERSON_5760_GITHUB_USERNAME 2025-08-22T15:10:00Z | A new id; C matches review/comment/merge — PASS |
| 68 | 182 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#38#ev_2` | commented SVC_0321_GITHUB_USERNAME 2025-08-22T15:12:00Z | A new id; C matches review/comment/merge — PASS |
| 69 | 184 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#38#ev_3` | reviewed PERSON_6026_GITHUB_USERNAME 2025-08-22T15:16:00Z | A new id; C matches review/comment/merge — PASS |
| 70 | 186 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#38#ev_4` | reviewed PERSON_2967_GITHUB_USERNAME 2025-08-25T09:20:00Z | A new id; C matches review/comment/merge — PASS |
| 71 | 188 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#38#ev_5` | merged PERSON_5760_GITHUB_USERNAME 2025-08-25T09:30:00Z | A new id; C matches review/comment/merge — PASS |
| 72 | 190 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#38#ev_6` | closed PERSON_5760_GITHUB_USERNAME 2025-08-25T09:30:00Z | A new id; C matches review/comment/merge — PASS |
| 73 | 192 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#38#ev_7` | commented PERSON_2967_GITHUB_USERNAME 2025-08-25T11:52:00Z | A new id; C matches review/comment/merge — PASS |
| 74 | 194 | github.github_pull_requests | INSERT | `harmonygames-Games/match3d-backend#39` | 2025-08-29T13:00:00Z | A new #, no base collision; C chronology ok — PASS |
| 75 | 196 | github.github_branches | INSERT | `harmonygames-Games/match3d-backend:trophy-path-container-headlines-config` |  | A new branch — PASS |
| 76 | 198 | github.github_commits | INSERT | `48153d42da95f5824fe53b669b0ab027f2cfe9a0` | 2025-08-29T12:40:00Z | A new sha — PASS |
| 77 | 200 | github.github_pull_request_commits | INSERT | `harmonygames-Games/match3d-backend#39#c_0` |  | A new id; commit injected earlier — PASS |
| 78 | 202 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#39#c_1` | PERSON_6026_GITHUB_USERNAME 2025-08-29T13:02:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 79 | 204 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#39#c_2` | PERSON_2967_GITHUB_USERNAME 2025-09-02T17:30:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 80 | 206 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#39#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED 2025-08-29T13:06:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 81 | 208 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#39#rev_2` | PERSON_5760_GITHUB_USERNAME APPROVED 2025-09-02T15:20:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 82 | 210 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#39#ev_1` | review_requested PERSON_2967_GITHUB_USERNAME 2025-08-29T13:00:00Z | A new id; C matches review/comment/merge — PASS |
| 83 | 212 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#39#ev_2` | commented SVC_0321_GITHUB_USERNAME 2025-08-29T13:02:00Z | A new id; C matches review/comment/merge — PASS |
| 84 | 214 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#39#ev_3` | reviewed PERSON_6026_GITHUB_USERNAME 2025-08-29T13:06:00Z | A new id; C matches review/comment/merge — PASS |
| 85 | 216 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#39#ev_4` | reviewed PERSON_5760_GITHUB_USERNAME 2025-09-02T15:20:00Z | A new id; C matches review/comment/merge — PASS |
| 86 | 218 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#39#ev_5` | merged PERSON_5760_GITHUB_USERNAME 2025-09-02T15:40:00Z | A new id; C matches review/comment/merge — PASS |
| 87 | 220 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#39#ev_6` | closed PERSON_5760_GITHUB_USERNAME 2025-09-02T15:40:00Z | A new id; C matches review/comment/merge — PASS |
| 88 | 222 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#39#ev_7` | commented PERSON_2967_GITHUB_USERNAME 2025-09-02T17:30:00Z | A new id; C matches review/comment/merge — PASS |
| 89 | 224 | github.github_pull_requests | INSERT | `harmonygames-Games/match3d-backend#40` | 2025-09-01T10:15:00Z | A new #, no base collision; C chronology ok — PASS |
| 90 | 226 | github.github_branches | INSERT | `harmonygames-Games/match3d-backend:items-make-the-cooler-a-usable-item` |  | A new branch — PASS |
| 91 | 228 | github.github_commits | INSERT | `334b4ed82b283bca22b8f218f389a9c834789745` | 2025-09-01T09:55:00Z | A new sha — PASS |
| 92 | 230 | github.github_pull_request_commits | INSERT | `harmonygames-Games/match3d-backend#40#c_0` |  | A new id; commit injected earlier — PASS |
| 93 | 232 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#40#c_1` | PERSON_6026_GITHUB_USERNAME 2025-09-01T10:17:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 94 | 234 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#40#c_2` | PERSON_2967_GITHUB_USERNAME 2025-09-02T18:40:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 95 | 236 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#40#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED 2025-09-01T10:21:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 96 | 238 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#40#ev_1` | review_requested PERSON_2967_GITHUB_USERNAME 2025-09-01T10:15:00Z | A new id; C matches review/comment/merge — PASS |
| 97 | 240 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#40#ev_2` | commented SVC_0321_GITHUB_USERNAME 2025-09-01T10:17:00Z | A new id; C matches review/comment/merge — PASS |
| 98 | 242 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#40#ev_3` | reviewed PERSON_6026_GITHUB_USERNAME 2025-09-01T10:21:00Z | A new id; C matches review/comment/merge — PASS |
| 99 | 244 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#40#ev_4` | merged PERSON_5760_GITHUB_USERNAME 2025-09-02T18:20:00Z | A new id; C matches review/comment/merge — PASS |
| 100 | 246 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#40#ev_5` | closed PERSON_5760_GITHUB_USERNAME 2025-09-02T18:20:00Z | A new id; C matches review/comment/merge — PASS |
| 101 | 248 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#40#ev_6` | commented PERSON_2967_GITHUB_USERNAME 2025-09-02T18:40:00Z | A new id; C matches review/comment/merge — PASS |
| 102 | 250 | github.github_pull_requests | INSERT | `harmonygames-Games/match3d-backend#41` | 2025-09-01T19:40:00Z | A new #, no base collision; C chronology ok — PASS |
| 103 | 252 | github.github_branches | INSERT | `harmonygames-Games/match3d-backend:algo-levels-100-seed-endpoint` |  | A new branch — PASS |
| 104 | 254 | github.github_commits | INSERT | `61e10e32a992a316e9f01836c6d1d12fff65868a` | 2025-09-01T19:20:00Z | A new sha — PASS |
| 105 | 256 | github.github_pull_request_commits | INSERT | `harmonygames-Games/match3d-backend#41#c_0` |  | A new id; commit injected earlier — PASS |
| 106 | 258 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#41#c_1` | PERSON_6026_GITHUB_USERNAME 2025-09-01T19:42:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 107 | 260 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#41#c_2` | PERSON_5760_GITHUB_USERNAME 2025-09-03T16:30:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 108 | 262 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#41#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED 2025-09-01T19:46:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 109 | 264 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#41#rev_2` | PERSON_2967_GITHUB_USERNAME APPROVED 2025-09-03T18:05:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 110 | 266 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#41#ev_1` | review_requested PERSON_5760_GITHUB_USERNAME 2025-09-01T19:40:00Z | A new id; C matches review/comment/merge — PASS |
| 111 | 268 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#41#ev_2` | commented SVC_0321_GITHUB_USERNAME 2025-09-01T19:42:00Z | A new id; C matches review/comment/merge — PASS |
| 112 | 270 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#41#ev_3` | reviewed PERSON_6026_GITHUB_USERNAME 2025-09-01T19:46:00Z | A new id; C matches review/comment/merge — PASS |
| 113 | 272 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#41#ev_4` | merged PERSON_5760_GITHUB_USERNAME 2025-09-03T16:00:00Z | A new id; C matches review/comment/merge — PASS |
| 114 | 274 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#41#ev_5` | closed PERSON_5760_GITHUB_USERNAME 2025-09-03T16:00:00Z | A new id; C matches review/comment/merge — PASS |
| 115 | 276 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#41#ev_6` | commented PERSON_5760_GITHUB_USERNAME 2025-09-03T16:30:00Z | A new id; C matches review/comment/merge — PASS |
| 116 | 278 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#41#ev_7` | reviewed PERSON_2967_GITHUB_USERNAME 2025-09-03T18:05:00Z | A new id; C matches review/comment/merge — PASS |
| 117 | 280 | github.github_pull_requests | INSERT | `harmonygames-Games/match3d-backend#42` | 2025-09-03T15:00:00Z | A new #, no base collision; C chronology ok — PASS |
| 118 | 282 | github.github_branches | INSERT | `harmonygames-Games/match3d-backend:teams-ack-lives-gift` |  | A new branch — PASS |
| 119 | 284 | github.github_commits | INSERT | `250e1846dd3f0770eddcb32a8ba25d32a5c33260` | 2025-09-03T14:40:00Z | A new sha — PASS |
| 120 | 286 | github.github_pull_request_commits | INSERT | `harmonygames-Games/match3d-backend#42#c_0` |  | A new id; commit injected earlier — PASS |
| 121 | 288 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#42#c_1` | PERSON_6026_GITHUB_USERNAME 2025-09-03T15:02:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 122 | 290 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#42#c_2` | PERSON_5760_GITHUB_USERNAME 2025-09-08T17:18:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 123 | 292 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#42#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED 2025-09-03T15:06:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 124 | 294 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#42#rev_2` | PERSON_2967_GITHUB_USERNAME APPROVED 2025-09-05T15:30:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 125 | 296 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#42#ev_1` | review_requested PERSON_5760_GITHUB_USERNAME 2025-09-03T15:00:00Z | A new id; C matches review/comment/merge — PASS |
| 126 | 298 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#42#ev_2` | commented SVC_0321_GITHUB_USERNAME 2025-09-03T15:02:00Z | A new id; C matches review/comment/merge — PASS |
| 127 | 300 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#42#ev_3` | reviewed PERSON_6026_GITHUB_USERNAME 2025-09-03T15:06:00Z | A new id; C matches review/comment/merge — PASS |
| 128 | 302 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#42#ev_4` | reviewed PERSON_2967_GITHUB_USERNAME 2025-09-05T15:30:00Z | A new id; C matches review/comment/merge — PASS |
| 129 | 304 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#42#ev_5` | merged PERSON_5760_GITHUB_USERNAME 2025-09-05T16:00:00Z | A new id; C matches review/comment/merge — PASS |
| 130 | 306 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#42#ev_6` | closed PERSON_5760_GITHUB_USERNAME 2025-09-05T16:00:00Z | A new id; C matches review/comment/merge — PASS |
| 131 | 308 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#42#ev_7` | commented PERSON_5760_GITHUB_USERNAME 2025-09-08T17:18:00Z | A new id; C matches review/comment/merge — PASS |
| 132 | 310 | github.github_pull_requests | INSERT | `harmonygames-Games/match3d-backend#43` | 2025-09-04T11:10:00Z | A new #, no base collision; C chronology ok — PASS |
| 133 | 312 | github.github_branches | INSERT | `harmonygames-Games/match3d-backend:inventory-drop-non-card-items-from-equip` |  | A new branch — PASS |
| 134 | 314 | github.github_commits | INSERT | `7d24459d1307b6ab594e52cdc5633d002a08d54b` | 2025-09-04T10:50:00Z | A new sha — PASS |
| 135 | 316 | github.github_pull_request_commits | INSERT | `harmonygames-Games/match3d-backend#43#c_0` |  | A new id; commit injected earlier — PASS |
| 136 | 318 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#43#c_1` | PERSON_6026_GITHUB_USERNAME 2025-09-04T11:12:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 137 | 320 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#43#c_2` | PERSON_2967_GITHUB_USERNAME 2025-09-04T12:50:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 138 | 322 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#43#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED 2025-09-04T11:16:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 139 | 324 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#43#ev_1` | review_requested PERSON_2967_GITHUB_USERNAME 2025-09-04T11:10:00Z | A new id; C matches review/comment/merge — PASS |
| 140 | 326 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#43#ev_2` | commented SVC_0321_GITHUB_USERNAME 2025-09-04T11:12:00Z | A new id; C matches review/comment/merge — PASS |
| 141 | 328 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#43#ev_3` | reviewed PERSON_6026_GITHUB_USERNAME 2025-09-04T11:16:00Z | A new id; C matches review/comment/merge — PASS |
| 142 | 330 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#43#ev_4` | merged PERSON_5760_GITHUB_USERNAME 2025-09-04T12:30:00Z | A new id; C matches review/comment/merge — PASS |
| 143 | 332 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#43#ev_5` | closed PERSON_5760_GITHUB_USERNAME 2025-09-04T12:30:00Z | A new id; C matches review/comment/merge — PASS |
| 144 | 334 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#43#ev_6` | commented PERSON_2967_GITHUB_USERNAME 2025-09-04T12:50:00Z | A new id; C matches review/comment/merge — PASS |
| 145 | 336 | github.github_pull_requests | INSERT | `harmonygames-Games/match3d-backend#44` | 2025-09-04T22:00:00Z | A new #, no base collision; C chronology ok — PASS |
| 146 | 338 | github.github_branches | INSERT | `harmonygames-Games/match3d-backend:profile-other-players-profile-v2` |  | A new branch — PASS |
| 147 | 340 | github.github_commits | INSERT | `b3ca856157e0fffa2ae28e9701ef4872205bc6f8` | 2025-09-04T21:40:00Z | A new sha — PASS |
| 148 | 342 | github.github_pull_request_commits | INSERT | `harmonygames-Games/match3d-backend#44#c_0` |  | A new id; commit injected earlier — PASS |
| 149 | 344 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#44#c_1` | PERSON_6026_GITHUB_USERNAME 2025-09-04T22:02:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 150 | 346 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#44#c_2` | PERSON_5760_GITHUB_USERNAME 2025-09-08T17:18:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 151 | 348 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#44#c_3` | PERSON_2967_GITHUB_USERNAME 2025-09-20T02:00:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 152 | 350 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#44#c_4` | PERSON_2967_GITHUB_USERNAME 2025-09-22T17:30:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 153 | 352 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#44#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED 2025-09-04T22:06:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 154 | 354 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#44#rev_2` | PERSON_5760_GITHUB_USERNAME CHANGES_REQUESTED 2025-09-05T16:00:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 155 | 356 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#44#rev_3` | PERSON_5760_GITHUB_USERNAME APPROVED 2025-09-08T15:10:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 156 | 358 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#44#ev_1` | review_requested PERSON_2967_GITHUB_USERNAME 2025-09-04T22:00:00Z | A new id; C matches review/comment/merge — PASS |
| 157 | 360 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#44#ev_2` | commented SVC_0321_GITHUB_USERNAME 2025-09-04T22:02:00Z | A new id; C matches review/comment/merge — PASS |
| 158 | 362 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#44#ev_3` | reviewed PERSON_6026_GITHUB_USERNAME 2025-09-04T22:06:00Z | A new id; C matches review/comment/merge — PASS |
| 159 | 364 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#44#ev_4` | reviewed PERSON_5760_GITHUB_USERNAME 2025-09-05T16:00:00Z | A new id; C matches review/comment/merge — PASS |
| 160 | 366 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#44#ev_5` | reviewed PERSON_5760_GITHUB_USERNAME 2025-09-08T15:10:00Z | A new id; C matches review/comment/merge — PASS |
| 161 | 368 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#44#ev_6` | merged PERSON_5760_GITHUB_USERNAME 2025-09-08T15:30:00Z | A new id; C matches review/comment/merge — PASS |
| 162 | 370 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#44#ev_7` | closed PERSON_5760_GITHUB_USERNAME 2025-09-08T15:30:00Z | A new id; C matches review/comment/merge — PASS |
| 163 | 372 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#44#ev_8` | commented PERSON_5760_GITHUB_USERNAME 2025-09-08T17:18:00Z | A new id; C matches review/comment/merge — PASS |
| 164 | 374 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#44#ev_9` | commented PERSON_2967_GITHUB_USERNAME 2025-09-20T02:00:00Z | A new id; C matches review/comment/merge — PASS |
| 165 | 376 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#44#ev_10` | commented PERSON_2967_GITHUB_USERNAME 2025-09-22T17:30:00Z | A new id; C matches review/comment/merge — PASS |
| 166 | 378 | github.github_pull_requests | INSERT | `harmonygames-Games/match3d-backend#45` | 2025-09-08T15:10:00Z | A new #, no base collision; C chronology ok — PASS |
| 167 | 380 | github.github_branches | INSERT | `harmonygames-Games/match3d-backend:inventory-keep-equipped-slots-across-ses` |  | A new branch — PASS |
| 168 | 382 | github.github_commits | INSERT | `46dc449026428308b2f3e48d0b88f039153a9aed` | 2025-09-08T14:50:00Z | A new sha — PASS |
| 169 | 384 | github.github_pull_request_commits | INSERT | `harmonygames-Games/match3d-backend#45#c_0` |  | A new id; commit injected earlier — PASS |
| 170 | 386 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#45#c_1` | PERSON_6026_GITHUB_USERNAME 2025-09-08T15:12:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 171 | 388 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#45#c_2` | PERSON_5760_GITHUB_USERNAME 2025-09-10T18:20:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 172 | 390 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#45#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED 2025-09-08T15:16:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 173 | 392 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#45#rev_2` | PERSON_2967_GITHUB_USERNAME CHANGES_REQUESTED 2025-09-09T17:00:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 174 | 394 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#45#rev_3` | PERSON_2967_GITHUB_USERNAME APPROVED 2025-09-10T15:10:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 175 | 396 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#45#ev_1` | review_requested PERSON_5760_GITHUB_USERNAME 2025-09-08T15:10:00Z | A new id; C matches review/comment/merge — PASS |
| 176 | 398 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#45#ev_2` | commented SVC_0321_GITHUB_USERNAME 2025-09-08T15:12:00Z | A new id; C matches review/comment/merge — PASS |
| 177 | 400 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#45#ev_3` | reviewed PERSON_6026_GITHUB_USERNAME 2025-09-08T15:16:00Z | A new id; C matches review/comment/merge — PASS |
| 178 | 402 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#45#ev_4` | reviewed PERSON_2967_GITHUB_USERNAME 2025-09-09T17:00:00Z | A new id; C matches review/comment/merge — PASS |
| 179 | 404 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#45#ev_5` | reviewed PERSON_2967_GITHUB_USERNAME 2025-09-10T15:10:00Z | A new id; C matches review/comment/merge — PASS |
| 180 | 406 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#45#ev_6` | merged PERSON_5760_GITHUB_USERNAME 2025-09-10T16:00:00Z | A new id; C matches review/comment/merge — PASS |
| 181 | 408 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#45#ev_7` | closed PERSON_5760_GITHUB_USERNAME 2025-09-10T16:00:00Z | A new id; C matches review/comment/merge — PASS |
| 182 | 410 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#45#ev_8` | commented PERSON_5760_GITHUB_USERNAME 2025-09-10T18:20:00Z | A new id; C matches review/comment/merge — PASS |
| 183 | 412 | github.github_pull_requests | INSERT | `harmonygames-Games/match3d-backend#46` | 2025-09-09T15:30:00Z | A new #, no base collision; C chronology ok — PASS |
| 184 | 414 | github.github_branches | INSERT | `harmonygames-Games/match3d-backend:economy-september-adjustments` |  | A new branch — PASS |
| 185 | 416 | github.github_commits | INSERT | `9bdbc503b5894db868b678fc822b2b70994af699` | 2025-09-09T15:10:00Z | A new sha — PASS |
| 186 | 418 | github.github_pull_request_commits | INSERT | `harmonygames-Games/match3d-backend#46#c_0` |  | A new id; commit injected earlier — PASS |
| 187 | 420 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#46#c_1` | PERSON_6026_GITHUB_USERNAME 2025-09-09T15:32:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 188 | 422 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#46#c_2` | PERSON_5760_GITHUB_USERNAME 2025-09-09T20:29:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 189 | 424 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#46#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED 2025-09-09T15:36:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 190 | 426 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#46#rev_2` | EMPLOYEE_0025_GITHUB_USERNAME APPROVED 2025-09-09T19:40:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 191 | 428 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#46#ev_1` | review_requested PERSON_5760_GITHUB_USERNAME 2025-09-09T15:30:00Z | A new id; C matches review/comment/merge — PASS |
| 192 | 430 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#46#ev_2` | commented SVC_0321_GITHUB_USERNAME 2025-09-09T15:32:00Z | A new id; C matches review/comment/merge — PASS |
| 193 | 432 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#46#ev_3` | reviewed PERSON_6026_GITHUB_USERNAME 2025-09-09T15:36:00Z | A new id; C matches review/comment/merge — PASS |
| 194 | 434 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#46#ev_4` | reviewed EMPLOYEE_0025_GITHUB_USERNAME 2025-09-09T19:40:00Z | A new id; C matches review/comment/merge — PASS |
| 195 | 436 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#46#ev_5` | merged PERSON_5760_GITHUB_USERNAME 2025-09-09T19:50:00Z | A new id; C matches review/comment/merge — PASS |
| 196 | 438 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#46#ev_6` | closed PERSON_5760_GITHUB_USERNAME 2025-09-09T19:50:00Z | A new id; C matches review/comment/merge — PASS |
| 197 | 440 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#46#ev_7` | commented PERSON_5760_GITHUB_USERNAME 2025-09-09T20:29:00Z | A new id; C matches review/comment/merge — PASS |
| 198 | 442 | github.github_pull_requests | INSERT | `harmonygames-Games/match3d-backend#47` | 2025-09-11T17:00:00Z | A new #, no base collision; C chronology ok — PASS |
| 199 | 444 | github.github_branches | INSERT | `harmonygames-Games/match3d-backend:analytics-log-endless-start-on-the-serve` |  | A new branch — PASS |
| 200 | 446 | github.github_commits | INSERT | `a0bdcab8e1b7b11ba1f04fec44b5c7bbd8d9a5d5` | 2025-09-11T16:40:00Z | A new sha — PASS |
| 201 | 448 | github.github_pull_request_commits | INSERT | `harmonygames-Games/match3d-backend#47#c_0` |  | A new id; commit injected earlier — PASS |
| 202 | 450 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#47#c_1` | PERSON_6026_GITHUB_USERNAME 2025-09-11T17:02:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 203 | 452 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#47#c_2` | PERSON_2967_GITHUB_USERNAME 2025-09-27T16:20:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 204 | 454 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#47#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED 2025-09-11T17:06:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 205 | 456 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#47#rev_2` | EMPLOYEE_0025_GITHUB_USERNAME APPROVED 2025-09-27T16:05:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 206 | 458 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#47#ev_1` | review_requested PERSON_2967_GITHUB_USERNAME 2025-09-11T17:00:00Z | A new id; C matches review/comment/merge — PASS |
| 207 | 460 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#47#ev_2` | commented SVC_0321_GITHUB_USERNAME 2025-09-11T17:02:00Z | A new id; C matches review/comment/merge — PASS |
| 208 | 462 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#47#ev_3` | reviewed PERSON_6026_GITHUB_USERNAME 2025-09-11T17:06:00Z | A new id; C matches review/comment/merge — PASS |
| 209 | 464 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#47#ev_4` | merged PERSON_5760_GITHUB_USERNAME 2025-09-12T19:00:00Z | A new id; C matches review/comment/merge — PASS |
| 210 | 466 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#47#ev_5` | closed PERSON_5760_GITHUB_USERNAME 2025-09-12T19:00:00Z | A new id; C matches review/comment/merge — PASS |
| 211 | 468 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#47#ev_6` | reviewed EMPLOYEE_0025_GITHUB_USERNAME 2025-09-27T16:05:00Z | A new id; C matches review/comment/merge — PASS |
| 212 | 470 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#47#ev_7` | commented PERSON_2967_GITHUB_USERNAME 2025-09-27T16:20:00Z | A new id; C matches review/comment/merge — PASS |
| 213 | 472 | github.github_pull_requests | INSERT | `harmonygames-Games/match3d-backend#48` | 2025-09-15T13:00:00Z | A new #, no base collision; C chronology ok — PASS |
| 214 | 474 | github.github_branches | INSERT | `harmonygames-Games/match3d-backend:boss-arena-infinite-hp-event-config` |  | A new branch — PASS |
| 215 | 476 | github.github_commits | INSERT | `e2999966670177f4f4644569bf44541e7806eea6` | 2025-09-15T12:40:00Z | A new sha — PASS |
| 216 | 478 | github.github_pull_request_commits | INSERT | `harmonygames-Games/match3d-backend#48#c_0` |  | A new id; commit injected earlier — PASS |
| 217 | 480 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#48#c_1` | PERSON_6026_GITHUB_USERNAME 2025-09-15T13:02:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 218 | 482 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#48#c_2` | PERSON_5760_GITHUB_USERNAME 2025-09-16T16:35:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 219 | 484 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#48#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED 2025-09-15T13:06:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 220 | 486 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#48#rev_2` | PERSON_5760_GITHUB_USERNAME APPROVED 2025-09-16T15:20:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 221 | 488 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#48#ev_1` | review_requested PERSON_2967_GITHUB_USERNAME 2025-09-15T13:00:00Z | A new id; C matches review/comment/merge — PASS |
| 222 | 490 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#48#ev_2` | commented SVC_0321_GITHUB_USERNAME 2025-09-15T13:02:00Z | A new id; C matches review/comment/merge — PASS |
| 223 | 492 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#48#ev_3` | reviewed PERSON_6026_GITHUB_USERNAME 2025-09-15T13:06:00Z | A new id; C matches review/comment/merge — PASS |
| 224 | 494 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#48#ev_4` | reviewed PERSON_5760_GITHUB_USERNAME 2025-09-16T15:20:00Z | A new id; C matches review/comment/merge — PASS |
| 225 | 496 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#48#ev_5` | merged PERSON_5760_GITHUB_USERNAME 2025-09-16T15:40:00Z | A new id; C matches review/comment/merge — PASS |
| 226 | 498 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#48#ev_6` | closed PERSON_5760_GITHUB_USERNAME 2025-09-16T15:40:00Z | A new id; C matches review/comment/merge — PASS |
| 227 | 500 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#48#ev_7` | commented PERSON_5760_GITHUB_USERNAME 2025-09-16T16:35:00Z | A new id; C matches review/comment/merge — PASS |
| 228 | 502 | github.github_pull_requests | INSERT | `harmonygames-Games/match3d-backend#49` | 2025-09-16T19:00:00Z | A new #, no base collision; C chronology ok — PASS |
| 229 | 504 | github.github_branches | INSERT | `harmonygames-Games/match3d-backend:boss-arena-mirror-balance-values` |  | A new branch — PASS |
| 230 | 506 | github.github_commits | INSERT | `1a12a54aec100ae0603bed4310dc12f3ec431aec` | 2025-09-16T18:40:00Z | A new sha — PASS |
| 231 | 508 | github.github_pull_request_commits | INSERT | `harmonygames-Games/match3d-backend#49#c_0` |  | A new id; commit injected earlier — PASS |
| 232 | 510 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#49#c_1` | PERSON_6026_GITHUB_USERNAME 2025-09-16T19:02:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 233 | 512 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#49#c_2` | PERSON_5760_GITHUB_USERNAME 2025-09-18T16:00:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 234 | 514 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#49#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED 2025-09-16T19:06:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 235 | 516 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#49#rev_2` | PERSON_2967_GITHUB_USERNAME APPROVED 2025-09-17T15:10:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 236 | 518 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#49#ev_1` | review_requested PERSON_5760_GITHUB_USERNAME 2025-09-16T19:00:00Z | A new id; C matches review/comment/merge — PASS |
| 237 | 520 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#49#ev_2` | commented SVC_0321_GITHUB_USERNAME 2025-09-16T19:02:00Z | A new id; C matches review/comment/merge — PASS |
| 238 | 522 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#49#ev_3` | reviewed PERSON_6026_GITHUB_USERNAME 2025-09-16T19:06:00Z | A new id; C matches review/comment/merge — PASS |
| 239 | 524 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#49#ev_4` | reviewed PERSON_2967_GITHUB_USERNAME 2025-09-17T15:10:00Z | A new id; C matches review/comment/merge — PASS |
| 240 | 526 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#49#ev_5` | merged PERSON_5760_GITHUB_USERNAME 2025-09-17T15:30:00Z | A new id; C matches review/comment/merge — PASS |
| 241 | 528 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#49#ev_6` | closed PERSON_5760_GITHUB_USERNAME 2025-09-17T15:30:00Z | A new id; C matches review/comment/merge — PASS |
| 242 | 530 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#49#ev_7` | commented PERSON_5760_GITHUB_USERNAME 2025-09-18T16:00:00Z | A new id; C matches review/comment/merge — PASS |
| 243 | 532 | github.github_pull_requests | INSERT | `harmonygames-Games/match3d-backend#50` | 2025-09-18T15:00:00Z | A new #, no base collision; C chronology ok — PASS |
| 244 | 534 | github.github_branches | INSERT | `harmonygames-Games/match3d-backend:boss-arena-don-t-take-a-life-on-a-win` |  | A new branch — PASS |
| 245 | 536 | github.github_commits | INSERT | `789f238dc36a0e3c363244a78144494fa406c839` | 2025-09-18T14:40:00Z | A new sha — PASS |
| 246 | 538 | github.github_pull_request_commits | INSERT | `harmonygames-Games/match3d-backend#50#c_0` |  | A new id; commit injected earlier — PASS |
| 247 | 540 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#50#c_1` | PERSON_6026_GITHUB_USERNAME 2025-09-18T15:02:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 248 | 542 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#50#c_2` | PERSON_2967_GITHUB_USERNAME 2025-09-27T14:30:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 249 | 544 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#50#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED 2025-09-18T15:06:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 250 | 546 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#50#rev_2` | PERSON_5760_GITHUB_USERNAME APPROVED 2025-09-19T15:10:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 251 | 548 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#50#rev_3` | EMPLOYEE_0025_GITHUB_USERNAME COMMENTED 2025-09-29T14:50:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 252 | 550 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#50#ev_1` | review_requested PERSON_2967_GITHUB_USERNAME 2025-09-18T15:00:00Z | A new id; C matches review/comment/merge — PASS |
| 253 | 552 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#50#ev_2` | commented SVC_0321_GITHUB_USERNAME 2025-09-18T15:02:00Z | A new id; C matches review/comment/merge — PASS |
| 254 | 554 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#50#ev_3` | reviewed PERSON_6026_GITHUB_USERNAME 2025-09-18T15:06:00Z | A new id; C matches review/comment/merge — PASS |
| 255 | 556 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#50#ev_4` | reviewed PERSON_5760_GITHUB_USERNAME 2025-09-19T15:10:00Z | A new id; C matches review/comment/merge — PASS |
| 256 | 558 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#50#ev_5` | merged PERSON_5760_GITHUB_USERNAME 2025-09-19T15:30:00Z | A new id; C matches review/comment/merge — PASS |
| 257 | 560 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#50#ev_6` | closed PERSON_5760_GITHUB_USERNAME 2025-09-19T15:30:00Z | A new id; C matches review/comment/merge — PASS |
| 258 | 562 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#50#ev_7` | commented PERSON_2967_GITHUB_USERNAME 2025-09-27T14:30:00Z | A new id; C matches review/comment/merge — PASS |
| 259 | 564 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#50#ev_8` | reviewed EMPLOYEE_0025_GITHUB_USERNAME 2025-09-29T14:50:00Z | A new id; C matches review/comment/merge — PASS |
| 260 | 566 | github.github_pull_requests | INSERT | `harmonygames-Games/match3d-backend#51` | 2025-09-18T20:00:00Z | A new #, no base collision; C chronology ok — PASS |
| 261 | 568 | github.github_branches | INSERT | `harmonygames-Games/match3d-backend:trophy-path-ignore-duplicate-claim-reque` |  | A new branch — PASS |
| 262 | 570 | github.github_commits | INSERT | `e737b6e6064a0e19d4ab43a383826bc7d1e2e98e` | 2025-09-18T19:40:00Z | A new sha — PASS |
| 263 | 572 | github.github_pull_request_commits | INSERT | `harmonygames-Games/match3d-backend#51#c_0` |  | A new id; commit injected earlier — PASS |
| 264 | 574 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#51#c_1` | PERSON_6026_GITHUB_USERNAME 2025-09-18T20:02:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 265 | 576 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#51#c_2` | PERSON_5760_GITHUB_USERNAME 2025-09-19T22:20:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 266 | 578 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#51#c_3` | EMPLOYEE_0012_GITHUB_USERNAME 2025-09-22T09:14:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 267 | 580 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#51#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED 2025-09-18T20:06:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 268 | 582 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#51#rev_2` | PERSON_2967_GITHUB_USERNAME APPROVED 2025-09-19T21:30:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 269 | 584 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#51#ev_1` | review_requested PERSON_5760_GITHUB_USERNAME 2025-09-18T20:00:00Z | A new id; C matches review/comment/merge — PASS |
| 270 | 586 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#51#ev_2` | commented SVC_0321_GITHUB_USERNAME 2025-09-18T20:02:00Z | A new id; C matches review/comment/merge — PASS |
| 271 | 588 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#51#ev_3` | reviewed PERSON_6026_GITHUB_USERNAME 2025-09-18T20:06:00Z | A new id; C matches review/comment/merge — PASS |
| 272 | 590 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#51#ev_4` | reviewed PERSON_2967_GITHUB_USERNAME 2025-09-19T21:30:00Z | A new id; C matches review/comment/merge — PASS |
| 273 | 592 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#51#ev_5` | merged PERSON_5760_GITHUB_USERNAME 2025-09-19T22:00:00Z | A new id; C matches review/comment/merge — PASS |
| 274 | 594 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#51#ev_6` | closed PERSON_5760_GITHUB_USERNAME 2025-09-19T22:00:00Z | A new id; C matches review/comment/merge — PASS |
| 275 | 596 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#51#ev_7` | commented PERSON_5760_GITHUB_USERNAME 2025-09-19T22:20:00Z | A new id; C matches review/comment/merge — PASS |
| 276 | 598 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#51#ev_8` | commented EMPLOYEE_0012_GITHUB_USERNAME 2025-09-22T09:14:00Z | A new id; C matches review/comment/merge — PASS |
| 277 | 600 | github.github_pull_requests | INSERT | `harmonygames-Games/match3d-backend#52` | 2025-09-22T12:10:00Z | A new #, no base collision; C chronology ok — PASS |
| 278 | 602 | github.github_branches | INSERT | `harmonygames-Games/match3d-backend:teams-push-lives-refresh-to-client` |  | A new branch — PASS |
| 279 | 604 | github.github_commits | INSERT | `9caa48b0aaac58c23661589a23c048e37bafbfed` | 2025-09-22T11:50:00Z | A new sha — PASS |
| 280 | 606 | github.github_pull_request_commits | INSERT | `harmonygames-Games/match3d-backend#52#c_0` |  | A new id; commit injected earlier — PASS |
| 281 | 608 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#52#c_1` | PERSON_6026_GITHUB_USERNAME 2025-09-22T12:12:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 282 | 610 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#52#c_2` | PERSON_5760_GITHUB_USERNAME 2025-09-30T18:16:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 283 | 612 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#52#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED 2025-09-22T12:16:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 284 | 614 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#52#rev_2` | PERSON_2967_GITHUB_USERNAME APPROVED 2025-09-22T14:50:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 285 | 616 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#52#ev_1` | review_requested PERSON_5760_GITHUB_USERNAME 2025-09-22T12:10:00Z | A new id; C matches review/comment/merge — PASS |
| 286 | 618 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#52#ev_2` | commented SVC_0321_GITHUB_USERNAME 2025-09-22T12:12:00Z | A new id; C matches review/comment/merge — PASS |
| 287 | 620 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#52#ev_3` | reviewed PERSON_6026_GITHUB_USERNAME 2025-09-22T12:16:00Z | A new id; C matches review/comment/merge — PASS |
| 288 | 622 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#52#ev_4` | reviewed PERSON_2967_GITHUB_USERNAME 2025-09-22T14:50:00Z | A new id; C matches review/comment/merge — PASS |
| 289 | 624 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#52#ev_5` | merged PERSON_5760_GITHUB_USERNAME 2025-09-22T15:05:00Z | A new id; C matches review/comment/merge — PASS |
| 290 | 626 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#52#ev_6` | closed PERSON_5760_GITHUB_USERNAME 2025-09-22T15:05:00Z | A new id; C matches review/comment/merge — PASS |
| 291 | 628 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#52#ev_7` | commented PERSON_5760_GITHUB_USERNAME 2025-09-30T18:16:00Z | A new id; C matches review/comment/merge — PASS |
| 292 | 630 | github.github_pull_requests | INSERT | `harmonygames-Games/match3d-backend#53` | 2025-09-22T16:00:00Z | A new #, no base collision; C chronology ok — PASS |
| 293 | 632 | github.github_branches | INSERT | `harmonygames-Games/match3d-backend:boss-arena-mirror-refill-and-nuke-values` |  | A new branch — PASS |
| 294 | 634 | github.github_commits | INSERT | `51677370b7a345efc26e88b7576890fa5c7d0419` | 2025-09-22T15:40:00Z | A new sha — PASS |
| 295 | 636 | github.github_pull_request_commits | INSERT | `harmonygames-Games/match3d-backend#53#c_0` |  | A new id; commit injected earlier — PASS |
| 296 | 638 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#53#c_1` | PERSON_6026_GITHUB_USERNAME 2025-09-22T16:02:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 297 | 640 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#53#c_2` | PERSON_5760_GITHUB_USERNAME 2025-09-24T16:00:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 298 | 642 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#53#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED 2025-09-22T16:06:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 299 | 644 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#53#rev_2` | PERSON_2967_GITHUB_USERNAME APPROVED 2025-09-23T15:15:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 300 | 646 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#53#ev_1` | review_requested PERSON_5760_GITHUB_USERNAME 2025-09-22T16:00:00Z | A new id; C matches review/comment/merge — PASS |
| 301 | 648 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#53#ev_2` | commented SVC_0321_GITHUB_USERNAME 2025-09-22T16:02:00Z | A new id; C matches review/comment/merge — PASS |
| 302 | 650 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#53#ev_3` | reviewed PERSON_6026_GITHUB_USERNAME 2025-09-22T16:06:00Z | A new id; C matches review/comment/merge — PASS |
| 303 | 652 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#53#ev_4` | reviewed PERSON_2967_GITHUB_USERNAME 2025-09-23T15:15:00Z | A new id; C matches review/comment/merge — PASS |
| 304 | 654 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#53#ev_5` | merged PERSON_5760_GITHUB_USERNAME 2025-09-23T15:30:00Z | A new id; C matches review/comment/merge — PASS |
| 305 | 656 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#53#ev_6` | closed PERSON_5760_GITHUB_USERNAME 2025-09-23T15:30:00Z | A new id; C matches review/comment/merge — PASS |
| 306 | 658 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#53#ev_7` | commented PERSON_5760_GITHUB_USERNAME 2025-09-24T16:00:00Z | A new id; C matches review/comment/merge — PASS |
| 307 | 660 | github.github_pull_requests | INSERT | `harmonygames-Games/match3d-backend#54` | 2025-09-22T18:00:00Z | A new #, no base collision; C chronology ok — PASS |
| 308 | 662 | github.github_branches | INSERT | `harmonygames-Games/match3d-backend:login-streak-count-days-in-player-timezo` |  | A new branch — PASS |
| 309 | 664 | github.github_commits | INSERT | `d0a473f0607318375786577d523bf5972f502c2c` | 2025-09-22T17:40:00Z | A new sha — PASS |
| 310 | 666 | github.github_pull_request_commits | INSERT | `harmonygames-Games/match3d-backend#54#c_0` |  | A new id; commit injected earlier — PASS |
| 311 | 668 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#54#c_1` | PERSON_6026_GITHUB_USERNAME 2025-09-22T18:02:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 312 | 670 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#54#c_2` | PERSON_5760_GITHUB_USERNAME 2025-09-24T19:00:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 313 | 672 | github.github_pr_comments | INSERT | `harmonygames-Games/match3d-backend#54#c_3` | PERSON_5760_GITHUB_USERNAME 2025-09-28T03:10:00Z | A new id; author login exists; C timeline pair ok — PASS |
| 314 | 674 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#54#rev_1` | PERSON_6026_GITHUB_USERNAME COMMENTED 2025-09-22T18:06:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 315 | 676 | github.github_reviews | INSERT | `harmonygames-Games/match3d-backend#54#rev_2` | PERSON_2967_GITHUB_USERNAME APPROVED 2025-09-23T15:20:00Z | A new id; non-author/bot login; C timeline pair ok — PASS |
| 316 | 678 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#54#ev_1` | review_requested PERSON_5760_GITHUB_USERNAME 2025-09-22T18:00:00Z | A new id; C matches review/comment/merge — PASS |
| 317 | 680 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#54#ev_2` | commented SVC_0321_GITHUB_USERNAME 2025-09-22T18:02:00Z | A new id; C matches review/comment/merge — PASS |
| 318 | 682 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#54#ev_3` | reviewed PERSON_6026_GITHUB_USERNAME 2025-09-22T18:06:00Z | A new id; C matches review/comment/merge — PASS |
| 319 | 684 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#54#ev_4` | reviewed PERSON_2967_GITHUB_USERNAME 2025-09-23T15:20:00Z | A new id; C matches review/comment/merge — PASS |
| 320 | 686 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#54#ev_5` | merged PERSON_5760_GITHUB_USERNAME 2025-09-23T16:00:00Z | A new id; C matches review/comment/merge — PASS |
| 321 | 688 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#54#ev_6` | closed PERSON_5760_GITHUB_USERNAME 2025-09-23T16:00:00Z | A new id; C matches review/comment/merge — PASS |
| 322 | 690 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#54#ev_7` | commented PERSON_5760_GITHUB_USERNAME 2025-09-24T19:00:00Z | A new id; C matches review/comment/merge — PASS |
| 323 | 692 | github.github_timeline_events | INSERT | `harmonygames-Games/match3d-backend#54#ev_8` | commented PERSON_5760_GITHUB_USERNAME 2025-09-28T03:10:00Z | A new id; C matches review/comment/merge — PASS |
| 324 | 695 | linear.linear_comments | INSERT | `cmt_0b9e52e7a05129c16301` | ZOM-459 2025-08-25T11:40:00Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 325 | 697 | linear.linear_comments | INSERT | `cmt_a50779a56d1833aec20b` | ZOM-457 2025-08-25T11:46:02Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 326 | 699 | linear.linear_comments | INSERT | `cmt_d08125bf464ffe16ff64` | ZOM-447 2025-08-25T09:58:20Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 327 | 701 | linear.linear_comments | INSERT | `cmt_aa3a4b36e887c4d668a4` | ZOM-474 2025-08-25T09:23:20Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 328 | 703 | linear.linear_comments | INSERT | `cmt_9ab4df8400bed355857e` | ZOM-470 2025-08-25T11:09:26Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 329 | 705 | linear.linear_comments | INSERT | `cmt_52185b2931cef92943d3` | ZOM-464 2025-09-02T10:34:58Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 330 | 707 | linear.linear_comments | INSERT | `cmt_9e73c35e85bd1e054a56` | ZOM-497 2025-09-02T12:32:48Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 331 | 709 | linear.linear_comments | INSERT | `cmt_3dcb72194895e1b92230` | ZOM-486 2025-09-02T10:27:27Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 332 | 711 | linear.linear_comments | INSERT | `cmt_98486e4ab765193640da` | ZOM-495 2025-09-02T12:51:23Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 333 | 713 | linear.linear_comments | INSERT | `cmt_088a84d96b94ef39674a` | ZOM-496 2025-09-02T12:35:27Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 334 | 715 | linear.linear_comments | INSERT | `cmt_6a00a703fed52e7c11fe` | ZOM-501 2025-09-02T11:44:42Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 335 | 717 | linear.linear_comments | INSERT | `cmt_18cc4fec19f0d669b9aa` | ZOM-485 2025-09-02T11:30:37Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 336 | 719 | linear.linear_comments | INSERT | `cmt_1aff31775b961e6129d4` | ZOM-466 2025-09-02T13:08:01Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 337 | 721 | linear.linear_comments | INSERT | `cmt_45367ccda4895c792313` | ZOM-332 2025-09-03T15:35:41Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 338 | 723 | linear.linear_comments | INSERT | `cmt_6208df52348b4ffc8b30` | ZOM-127 2025-09-03T13:44:46Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 339 | 725 | linear.linear_comments | INSERT | `cmt_f916fc632f4d7a220a9a` | ZOM-265 2025-09-03T13:59:24Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 340 | 727 | linear.linear_comments | INSERT | `cmt_bbbd0687c4431af35535` | ZOM-338 2025-09-03T14:23:13Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 341 | 729 | linear.linear_comments | INSERT | `cmt_96aafd5ba312028e7391` | ZOM-340 2025-09-03T15:29:40Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 342 | 731 | linear.linear_comments | INSERT | `cmt_c69a63ac9dbd4826b955` | ZOM-335 2025-09-03T13:31:13Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 343 | 733 | linear.linear_comments | INSERT | `cmt_877095d931428f1536df` | ZOM-336 2025-09-03T15:50:00Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 344 | 735 | linear.linear_comments | INSERT | `cmt_860e5862211fe64ac0da` | ZOM-331 2025-09-03T13:54:27Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 345 | 737 | linear.linear_comments | INSERT | `cmt_aac3d150bafe119754f8` | ZOM-339 2025-09-03T13:27:18Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 346 | 739 | linear.linear_comments | INSERT | `cmt_bbc8084b40022773292c` | ZOM-337 2025-09-03T13:36:44Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 347 | 741 | linear.linear_comments | INSERT | `cmt_6f75f609688a3ed60aba` | ZOM-502 2025-09-04T08:31:02Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 348 | 743 | linear.linear_comments | INSERT | `cmt_4362bbdda4049c5dd30d` | ZOM-476 2025-09-04T09:31:52Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 349 | 745 | linear.linear_comments | INSERT | `cmt_d02aec11deff05b555cc` | ZOM-392 2025-09-04T10:20:00Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 350 | 747 | linear.linear_comments | INSERT | `cmt_112afca3ef67b713a9e7` | ZOM-509 2025-09-04T10:15:00Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 351 | 749 | linear.linear_comments | INSERT | `cmt_99069485a5f5d5eb9ce3` | ZOM-518 2025-09-04T12:55:00Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 352 | 751 | linear.linear_comments | INSERT | `cmt_0f256875faad3cad9843` | ZOM-510 2025-09-11T16:45:00Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 353 | 753 | linear.linear_comments | INSERT | `cmt_57ce6f9bc61a928159ce` | ZOM-519 2025-09-11T14:17:24Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 354 | 755 | linear.linear_comments | INSERT | `cmt_bc49540005814cc8f0e1` | ZOM-256 2025-09-11T16:48:00Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 355 | 757 | linear.linear_comments | INSERT | `cmt_58afcdd4871aac77a852` | ZOM-540 2025-09-12T16:04:38Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 356 | 759 | linear.linear_comments | INSERT | `cmt_81278f65a6828964fd37` | ZOM-531 2025-09-15T15:01:00Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 357 | 761 | linear.linear_comments | INSERT | `cmt_f3fd31480ea0ad163b4c` | ZOM-512 2025-09-15T12:28:15Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 358 | 763 | linear.linear_comments | INSERT | `cmt_92b95a95aa3414a22c89` | ZOM-537 2025-09-15T15:05:00Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 359 | 765 | linear.linear_comments | INSERT | `cmt_32c3a18150bf06ad3a12` | ZOM-444 2025-09-15T15:06:00Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 360 | 767 | linear.linear_comments | INSERT | `cmt_9f00cd5152233dc95ff4` | ZOM-515 2025-09-15T12:20:20Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 361 | 769 | linear.linear_comments | INSERT | `cmt_a413bcc2401d50df1cc6` | ZOM-493 2025-09-15T14:47:44Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 362 | 771 | linear.linear_comments | INSERT | `cmt_5933eeaa473e3376dc0a` | ZOM-491 2025-09-15T14:08:56Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 363 | 773 | linear.linear_comments | INSERT | `cmt_dd19ad17ac459bc0f50e` | ZOM-463 2025-09-15T15:09:56Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 364 | 775 | linear.linear_comments | INSERT | `cmt_f0049fd2ef671c2b95d1` | ZOM-383 2025-09-15T13:46:52Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 365 | 777 | linear.linear_comments | INSERT | `cmt_7c7780e6f01e8b2c5103` | ZOM-436 2025-09-17T15:08:39Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 366 | 779 | linear.linear_comments | INSERT | `cmt_22a38511a35757459956` | ZOM-421 2025-09-17T15:26:01Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 367 | 781 | linear.linear_comments | INSERT | `cmt_2419c07aa4f77f4a3536` | ZOM-525 2025-09-17T12:55:28Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 368 | 783 | linear.linear_comments | INSERT | `cmt_92867e48f99e1dfd8ba3` | ZOM-523 2025-09-17T14:08:11Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 369 | 785 | linear.linear_comments | INSERT | `cmt_edbbbb8c0b8ced6e4401` | ZOM-524 2025-09-17T15:36:52Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 370 | 787 | linear.linear_comments | INSERT | `cmt_b197d27aaaba58c9b89f` | ZOM-499 2025-09-17T15:44:00Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 371 | 789 | linear.linear_comments | INSERT | `cmt_93d0e4f86d854d279b99` | ZOM-478 2025-09-17T15:22:09Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 372 | 791 | linear.linear_comments | INSERT | `cmt_9a6e40246a899fc380bc` | ZOM-547 2025-09-17T16:01:00Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 373 | 793 | linear.linear_comments | INSERT | `cmt_2d985b12de71739e6b82` | ZOM-511 2025-09-17T15:19:00Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 374 | 795 | linear.linear_comments | INSERT | `cmt_41e71e303718899c0d3c` | ZOM-487 2025-09-17T16:09:00Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 375 | 797 | linear.linear_comments | INSERT | `cmt_ad7d4901835f513674cd` | ZOM-530 2025-09-18T16:04:18Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 376 | 799 | linear.linear_comments | INSERT | `cmt_7cea4a71e9934e0c587c` | ZOM-500 2025-09-19T13:42:00Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 377 | 801 | linear.linear_comments | INSERT | `cmt_a5d743a4487fb4aad196` | ZOM-527 2025-09-19T15:27:52Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 378 | 803 | linear.linear_comments | INSERT | `cmt_2e0b9655e5d932f6b7e1` | ZOM-550 2025-09-19T16:10:00Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 379 | 805 | linear.linear_comments | INSERT | `cmt_8dbc7c9e3101efc08508` | ZOM-435 2025-09-22T13:49:00Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 380 | 807 | linear.linear_comments | INSERT | `cmt_6cdfde887dc9d5875a19` | ZOM-434 2025-09-22T13:26:18Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 381 | 809 | linear.linear_comments | INSERT | `cmt_d9d13434b3b6cdbe8c09` | ZOM-507 2025-09-22T12:08:03Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 382 | 811 | linear.linear_comments | INSERT | `cmt_bcb9a5974b2de811c2af` | ZOM-169 2025-09-22T14:20:59Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 383 | 813 | linear.linear_comments | INSERT | `cmt_c95585f37ce6708a9ec4` | ZOM-503 2025-09-22T15:08:00Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 384 | 815 | linear.linear_comments | INSERT | `cmt_80ecf3a45d73d6e13170` | ZOM-473 2025-09-22T14:17:06Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 385 | 817 | linear.linear_comments | INSERT | `cmt_cdd62a5e38fdf8d59a57` | ZOM-419 2025-09-22T14:55:01Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 386 | 819 | linear.linear_comments | INSERT | `cmt_09ce815cd0da097ee561` | ZOM-239 2025-09-22T12:38:16Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 387 | 821 | linear.linear_comments | INSERT | `cmt_445caf64da6e5d8fb2af` | ZOM-506 2025-09-22T13:45:31Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 388 | 823 | linear.linear_comments | INSERT | `cmt_9e4897d4fa0c8f01b3c1` | ZOM-538 2025-09-23T12:56:12Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 389 | 825 | linear.linear_comments | INSERT | `cmt_fb8aec8f0d94d5dadc69` | ZOM-112 2025-09-23T12:23:48Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 390 | 827 | linear.linear_comments | INSERT | `cmt_6df7394cf11eed76b50c` | ZOM-558 2025-09-23T11:56:35Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 391 | 829 | linear.linear_comments | INSERT | `cmt_361d1945d189b0587159` | ZOM-536 2025-09-30T09:47:04Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 392 | 831 | linear.linear_comments | INSERT | `cmt_68b41719f7d3ea9ff0fe` | ZOM-498 2025-09-30T10:38:37Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 393 | 833 | linear.linear_comments | INSERT | `cmt_dbd1c3ba1c96a97fdc3f` | ZOM-555 2025-09-30T11:21:15Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 394 | 835 | linear.linear_comments | INSERT | `cmt_c2bad7e49457b4f6c558` | ZOM-553 2025-09-30T12:38:00Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 395 | 837 | linear.linear_comments | INSERT | `cmt_e850768746208eefe527` | ZOM-557 2025-09-30T12:39:00Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 396 | 839 | linear.linear_comments | INSERT | `cmt_b4c2115bb1a33be756ae` | ZOM-561 2025-09-30T10:27:27Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 397 | 841 | linear.linear_comments | INSERT | `cmt_7777dfa66681d9a8aa7a` | ZOM-461 2025-08-25T11:45:00Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 398 | 843 | linear.linear_comments | INSERT | `cmt_b3046e62e82ef09c3139` | ZOM-480 2025-08-25T10:14:32Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 399 | 845 | linear.linear_comments | INSERT | `cmt_43d06395046a31ca5a99` | ZOM-479 2025-08-25T09:52:01Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 400 | 847 | linear.linear_comments | INSERT | `cmt_be76fa616764ca440ae2` | ZOM-489 2025-08-25T08:30:50Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 401 | 849 | linear.linear_comments | INSERT | `cmt_b61f9c6d82a6b4cf9455` | ZOM-535 2025-09-30T14:44:39Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 402 | 851 | linear.linear_issues | UPDATE | `WHERE id = ZOM-535` | updated_at -> 2025-09-30T14:44:39Z | A target exists; C bump = injected comment time — PASS |
| 403 | 852 | linear.linear_comments | INSERT | `cmt_c4fb570f231f9c8d8cd2` | ZOM-504 2025-09-30T14:37:05Z | A new id (base has 0 comments); issue + author exist; C before issue completed/updated — PASS |
| 404 | 854 | linear.linear_issues | UPDATE | `WHERE id = ZOM-504` | updated_at -> 2025-09-30T14:37:05Z | A target exists; C bump = injected comment time — PASS |

## 9. Stage dependencies for reuse

`/prompt` may reuse these static checks only while all of these are unchanged: SQL SHA-256 `f48302c6…71f1`, synth-cut universe manifest `da2f4cf0…ac1a` and the base file hashes in §1, `injection.json` `31dcb2b4…5151`, `id_contracts.json` `fc4711ef…d4682`, Eval 0 `b1ea752a…3d3a`, and the fixed clock 2025-10-01 07:00 UTC. Any SQL edit invalidates the whole ledger. Prompt-specific incorporation, discoverability, persona access and solvability are not covered here.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt

Evidence limits: No required static check unresolved. Outside scope: live deployment and current DB compatibility (five SQL columns and both Confluence tables are not in the unverified schema snapshot), Slack thread_ts_legacy platform mapping, Agent visibility, task difficulty.
