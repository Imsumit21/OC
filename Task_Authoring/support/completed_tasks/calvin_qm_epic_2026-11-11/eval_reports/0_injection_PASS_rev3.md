# /injection — Injection data-integrity review

### FINAL VERDICT: PASS

Execution status: COMPLETE

Evaluator model: Claude Opus 5.5 (claude-opus-5-5), effort 15/low

Next action: Proceed to /prompt. The SQL changed, so /prompt, /hardness, /oe and /rubric results from earlier SQL versions are outdated and must be run again in that order.

Evidence limits: Static review only. The SQL was not executed or deployed. The bundled backing-schema snapshot is unverified, and six columns the SQL writes are NOT COVERED by it (advisory, see Check B). Uniqueness was checked against the local synth-cut base plus this SQL, not the live database. Agent visibility, task discoverability and difficulty are outside this stage.

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

---

## 1. Scope and provenance

| Item | Value |
|---|---|
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`. Changed and new statements were checked NEW. Unchanged statements are REUSED from the previous injection review (SQL `ee46405a157d6eb3…`, PASS, 2026-11-10T10:59Z). The diff below confirms their text is byte-identical, and the universe manifest, schema snapshot, id_contracts and WORKFLOW hashes are unchanged. |
| Mode | Chat review, attempt 6aed9d01e894b802ca6d6d03 |
| Review time | 2026-11-10T14:17Z |
| Assignment (platform record) | Calvin Price, Game Engineer (Unity VFX); Engineering / Engineering Ops / Analysis and synthesis; long-horizon; hard |
| SQL input | `Evals/task_inputs/01_Universe_Inject.sql` (108,903 bytes; sha256 `e64595826ab61866e96c8e3d7ee9cf5a8585ee68ece089aeed99468f14b6c787`), saved as revision 8 from the attachment `01_Universe_Inject (3).sql` |
| Previous version | sha256 `ee46405a157d6eb3423da8b51c4f2f42164b60409dc4d82c74b8c770938ec5e8` (PASS); replaced |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); `Evals/references/universes/synthcut/universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` (unchanged) |
| Schema snapshot | `Evals/references/schema/injection.json` sha256 `31dcb2b43feca8e5…` (unverified, unchanged) |
| ID contracts | `Evals/references/schema/id_contracts.json` sha256 `fc4711ef07667333…` (unchanged) |
| WORKFLOW | sha256 `d5702ee24b3995a9…` (unchanged) |
| Base sources read this run | linear `data.json` (/users, /issues, /comments); github `data.json` `/pull_requests/2377` (PR #472); gdrive `data.json` /drive_users; slack `messages/C05433XK267/2025-09.json` (#builds) |

## 2. Lint (`hg_injection_lint.py`, injection-lint-v1)

142 statements (BEGIN, 129 INSERT, 11 UPDATE, COMMIT), matching the SQL header (129 INSERT, 11 UPDATE). Base lists loaded: slack/users, trello, gmail/users, github, linear, contacts, confluence_working.
**Flags: FAIL 0, CHECK 0, INFO 0.** Nothing to resolve. Checks A–C were still run.

## 3. Changes from the previous version (diff)

Net +7 INSERTs: +2 Linear issues, +6 Linear comments, −1 Linear comment. UPDATE count unchanged (one existing UPDATE gained a column).

| # | SQL line | Table | Change | Check |
|---|---|---|---|---|
| D1 | 3 | header comment | 122 INSERT → 129 INSERT | Matches lint count |
| D2 | 8, 10, 21, 28 | gdrive.drive_files `f_cb4095…` (sheet), `f_d3a1aa…` (legend doc); gdocs `f_d3a1aa…`; gsheets `f_cb4095…` | `oliver.brooks@harmonygames.co` added as reader in `shared_with` and `permissions_json` | Oliver is a base Drive user (`/drive_users/16`); the Drive, Docs and Sheets share lists match on both files |
| D3 | 30 | gsheets.sheets_sheets "Flow pass" | Row 15 Fix "" → "#472"; row 17 Ticket "" → "ZOM-585", Re-test "ok iOS Internal #1754" → "ok iOS Internal #1757"; row 24 Found on "iOS Internal #1745" → "#1750", Ticket → "ZOM-586", Re-test "ok Android #2010" → "nr iOS Internal #1757" | Grid parses; 41 rows; 7 columns each; values agree with Linear (Check C) |
| D4 | 82, 172 | Slack bot reply `66dd5332…` (#zombie-prs) + `github_pr_comments #473#c_2` | Oliver's comment now lists four fixes (pass start popup, pass bar, claim animation twice after shop, freezer popup behind pass popup) | Same text in both records |
| D5 | 85, 157, 164 | Slack bot reply `8e02c114…`, Gmail notification to Calvin, `github_review_comments #472#rc_1` | Arthur's comment now says the season pass icon restart and the event bar under the gift popup are not in #472; the other two Collect & Win items are | Same text in all three (Slack `&amp;` escaping is normal); Gmail `size_estimate` 3588 → 3649 = +61, exactly the text length change |
| D6 | 165 | github.github_pull_requests #472 UPDATE | Now also sets `body`: base body with " (this also holds the pre-level panel until the level-end coins have landed)" added to the first line | Rest of body byte-identical to base `/pull_requests/2377`; `updated_at` 15:53:40Z unchanged (after merge at 15:53:04Z) |
| D7 | 189, removed comment | linear ZOM-573 | Comment `comment_d77a1d24…` ("I have this one on my branch…") removed; `updated_at` 18:06:34Z → 17:21:12Z | = remaining latest comment (seq 1, 17:21:12Z); no other record mentions the removed comment |
| D8 | 191, 241 | linear ZOM-574 + `comment_b9543ec8…` | Assignee Owen Baker → Calvin Price (`usr_49b9dfa5208d400d`); state Todo → In Validation; `started_at` 17:26:12Z; `updated_at` 17:29:33Z; comment now Vincent, seq 2, 17:29:33Z, "I was told #472 has it. Not re-tested yet." | Seq 1 is 17:28:40Z; `updated_at` = latest comment; same pattern as ZOM-571/576/581 |
| D9 | 212–215 | linear.linear_issues ZOM-585, ZOM-586 | NEW (see ledger) | IDs unused in base |
| D10 | 270–281 | linear.linear_comments ×6 | NEW, on ZOM-585 and ZOM-586 (see ledger) | IDs unused |

All other statements are byte-identical to the previously reviewed version; their ledger rows and results are REUSED (section 4).

## 4. Operation ledger (execution order)

Rows marked NEW were checked in this run. Rows marked REUSED carry the previous review's verified evidence (unchanged statement text, unchanged base manifest).

| # | SQL lines | Table | Op | Record(s) | Key values | Base target / collision result | Status |
|---|---|---|---|---|---|---|---|
| 1 | 7–8 | gdrive.drive_files | INSERT | `f_cb40955893624e1acb8500` "ZM home screen flow pass" (sheet) | owner vincent.parker; parent `d_65c76e0b87aa7e9b84d1df`; shared brian/calvin/leonard/arthur/**oliver**; created 09-26, modified 09-30T19:30:52Z | Parent = Vincent's root; ID unused | REUSED; Oliver share NEW |
| 2 | 9–10 | gdrive.drive_files | INSERT | `f_d3a1aa5976285aac98ffda` "How to read my pass sheets" | owner vincent; same 5 readers | Parent OK; ID unused | REUSED; Oliver share NEW |
| 3 | 11–12 | gdrive.drive_files | INSERT | `f_6d0326fa006b136f1bbf82` "ZM builds and QA passes" | owner arthur.blake | ID unused | REUSED |
| 4 | 13–14 | gdrive.drive_files | INSERT | `f_ea7517885d11570b54bf13` "DD hotfix builds and QA passes" | owner arthur | ID unused | REUSED |
| 5 | 15–16 | gdrive.drive_files | INSERT | `d_36cdb0374c4aad3b8bf741` folder "ZM queue manager" | owner calvin.price; parent Calvin's root | ID unused | REUSED |
| 6 | 17–18 | gdrive.drive_files | INSERT | `f_637e63ae6c1b4a7eb016aa` slides "ZM queue manager" | owner calvin; parent = row 5 | ID unused | REUSED |
| 7–9 | 20–25 | gdocs.docs_documents | INSERT ×3 | `f_d3a1aa…`, `f_6d0326…`, `f_ea7517…` | non-empty bodies; style runs end at body length (430 for the legend doc) | IDs unused | REUSED; `f_d3a1aa…` share list NEW |
| 10 | 27–28 | gsheets.sheets_spreadsheets | INSERT | `f_cb4095…` | drive_file_id = row 1; share list incl. Oliver | ID absent from gsheets | REUSED; share NEW |
| 11 | 29–30 | gsheets.sheets_sheets | INSERT | (`f_cb4095…`, 0) "Flow pass" | header + 38 rows + blank + note; rows 15/17/24 changed | New spreadsheet | NEW (content) |
| 12–24 | 32–57 | gslides presentations/pages/elements | INSERT ×13 | `f_637e63…` | — | Object IDs unused | REUSED |
| 25–36 | 59–80 | slack.slack_messages | INSERT ×10 / UPDATE ×2 | DMs (Brian, Vincent, Marcus); #zombie-bugs replies `b156fdcd…`, `a4082477…` + parent UPDATEs; #zombie-match3d `ecf80487…` | — | Parents, membership, counts, no ID/ts collisions | REUSED |
| 37–38 | 81–83 | slack.slack_messages | INSERT / UPDATE | `66dd5332…` #zombie-prs bot reply "Comment on #473"; parent `d05a2f8a…` 2→3 | 15:42:12Z | Parent exists | REUSED; text NEW (= GitHub #473#c_2) |
| 39–40 | 84–86 | slack.slack_messages | INSERT / UPDATE | `8e02c114…` "Comment on #472"; parent `61f686b8…` → 4 replies | 15:53:42Z | Parent exists; latest moves forward | REUSED; text NEW (= GitHub #472#rc_1) |
| 41–42 | 87–89 | slack.slack_messages | INSERT / UPDATE | `69700214…` (#475); parent `1389e3c5…` | 16:09:52Z | — | REUSED |
| 43–48 | 91–101 | trello card / actions ×4 / board UPDATE | — | `68daad83…` idShort 80 | — | — | REUSED |
| 49–54 | 103–114 | gcal.gcal_events ×6 | INSERT | review meeting 2025-10-02T18:00Z (plan field) | — | — | REUSED |
| 55–74 | 116–155 | gmail threads ×10 / messages ×10 | INSERT | invite + update for 5 people | history_id NULL | — | REUSED |
| 75 | 156–157 | gmail.gmail_messages | INSERT | PR #472 review-comment notification to Calvin | 15:53:59Z; size_estimate 3649; body = new rc_1 text | Message-ID unused | REUSED; body/size NEW |
| 76 | 158–159 | gmail.gmail_messages | INSERT | PR #475 notification | — | — | REUSED |
| 77–84 | 161–174 | github reviews / review_comments / pull_requests / pr_comments / timeline_events | INSERT ×6, UPDATE ×2 | `#472#rc_1` text NEW; **#472 UPDATE now sets body + updated_at 15:53:40Z**; `#473#c_2` text NEW | — | Base PR #472 (`/pull_requests/2377`) body preserved except the added first-line clause | REUSED; D4–D6 NEW |
| 85–104 | 176–215 | linear.linear_issues ×20 | INSERT | ZOM-567 … ZOM-586 | ZOM-573 updated_at 17:21:12Z; ZOM-574 Calvin, In Validation, started 17:26:12Z, updated 17:29:33Z; **ZOM-585** Calvin, creator Vincent, In Validation, created/started 18:49:27Z, updated 21:52:18Z, "Seen on iOS Internal 1750", `state_history_json '[]'`; **ZOM-586** unassigned, Todo, created 18:53:41Z, updated 22:07:44Z, "Seen on iOS Internal 1750" | `lookup` /issues by identifier: ZOM-585, ZOM-586 0 matches (3,687 issues, scan_complete). Numbers rise with created_at (584 18:44:35Z → 585 18:49:27Z → 586 18:53:41Z) | REUSED; ZOM-573/574/585/586 NEW |
| 105–137 | 216–281 | linear.linear_comments ×33 | INSERT | 28 previous − `comment_d77a1d24…` + `comment_b9543ec8…` (rewritten) + 6 new: ZOM-585 seq 1 Vincent 18:50:47Z, seq 2 Vincent 19:14:06Z "ok on iOS Internal 1757", seq 3 Samuel Turner 21:52:18Z "Got this again on Android Submission 135…"; ZOM-586 seq 1 Vincent 18:56:09Z, seq 2 Vincent 19:17:31Z "Can't make it happen on iOS Internal 1757 any more", seq 3 Owen Baker 22:07:44Z "Android Submission 135: … starts from zero again" | — | `lookup` /comments: the 7 new or rewritten IDs 0 matches (base has 0 Linear comments, scan_complete); 33 IDs unique in the SQL; sequences 1-2-3 in time order | NEW for D7, D8, D10; others REUSED |
| 138–140 | 282–284 | linear.linear_issues UPDATE ×3 | ZOM-543, ZOM-556, ZOM-560 updated_at | = latest comment time | Forward | REUSED |

## 5. Checks

| Check | Result | Evidence |
|---|---|---|
| A — Records, references and IDs | PASS | NEW: every Linear actor in changed or new rows exists in base `/users`: Calvin `usr_49b9dfa5208d400d` (/users/6), Owen Baker `usr_4e13bd40cc73d0fc` (/users/8), Vincent `usr_65c76e0b87aa7e9b` (/users/14), Samuel Turner `usr_caafeec2804b3a67` (/users/34), plus the reused `usr_bdf01b53c6a92c5e` and `usr_fc22d5941b2aeb5c`. ZOM-585/586 are unused (complete lookup over 3,687 base issues). The 7 new or rewritten comment IDs are unused (complete lookup; base has none) and unique in the SQL. Oliver's share uses his existing Drive account (`/drive_users/16`), no second account. The PR #472 UPDATE targets an existing record (`/pull_requests/2377`). The state "In Validation" is a base Linear state value (e.g. `/issues/3510`, `/issues/3623`). REUSED: all other actors, parents and collision results. |
| B — SQL structure and schema | PASS (snapshot advisory) | The lint parsed all 142 statements with no missing_required, json_shape, generated_column or text_time_format flag. The new issues use the same 27-column list, `state_history_json '[]'`, JSON-list `labels_json`/`links_json`/`relations_json`, and Linear dates in `YYYY-MM-DDTHH:MM:SSZ`. The new comments use the same 9-column list. The PR body UPDATE is a valid `E''` literal with only `\n` escapes and doubled quotes. The sheet grid is valid JSON. Provisional snapshot comparison unchanged: **NOT COVERED** `gslides.slides_pages.notes`, `gslides.slides_page_elements.table_json` and `.ordinal`, `github.github_reviews.seq`, `github.github_review_comments.seq`, `linear.linear_comments.sequence` (advisory under the schema README). |
| C — Dates, relationships and consistency | PASS | The latest event timestamp is now 2025-09-30T22:07:44Z (ZOM-586 seq 3), before the 2025-10-01 07:00 UTC clock. Builds cited by new or changed records exist as main builds in #builds before use: iOS Internal #1750 (main success, ts `1759197354.452939` = 09-30 01:55:54Z, `/1084`) before ZOM-585/586 creation (18:49Z/18:53Z); iOS Internal #1757 (18:43:07Z) before the 19:14Z/19:17Z comments and the sheet's 19:30:52Z edit; Android Submission #135 (20:13:09Z) before the 21:52Z and 22:07Z comments. The sheet agrees with Linear as of its last edit: row 17 = ZOM-585 (Found #1750, Fix #472, "ok iOS Internal #1757" = seq 2); row 24 = ZOM-586 (Found #1750, "nr iOS Internal #1757" = seq 2); row 15 Fix #472 = ZOM-574's "I was told #472 has it. Not re-tested yet." with a blank Re-test. The later Submission 135 reports post-date the sheet (supported stale context, not a contradiction). Arthur's #472 comment is consistent with the sheet's four #472 rows (12, 15 not in the diff; 17, 18 are). Oliver's four #473 fixes match rows 13, 14, 37, 38, whose Fix cells are blank under the legend ("Blank if nobody told me"). Issue `updated_at` = latest comment on ZOM-573, 574, 585, 586. No grader-facing text and no SQL comment about tool calls or pass rate. No Snowflake or Confluence record is touched or built on. |

## 6. Findings

No demonstrated defects.

Advisories (not failures, no action required for this stage):

1. **Schema snapshot gap (Check B):** the six NOT COVERED columns above (unchanged). If the live platform ever rejects one, the whole transaction rolls back; drop that column if a load error names it.
2. **PR #472 body edited after merge (context):** the body change shares `updated_at` 15:53:40Z with Arthur's review comment, 36 s after the merge. Editing a merged PR's description is possible on GitHub, and there's no `edited` timeline event (base timelines have gaps too). Whether the Agent reads the PR body belongs to /prompt.
3. **GitHub review numbers in email headers (cosmetic, unchanged):** the notification Message-IDs use review numbers lower than the approvals Arthur submitted seconds earlier. No reference breaks and no listed contract applies.
4. **Thread placement (context only, unchanged):** Vincent's Submission 135 reply sits in his 2025-09-15 submission-list thread. The data is consistent; discoverability belongs to /prompt.

## 7. Stage dependencies for reuse (stage-evidence-v1)

- This PASS covers SQL sha256 `e64595826ab61866…` against Universe_SynthCut (manifest `da2f4cf0dcf71025…`), schema snapshot `31dcb2b4…`, id_contracts `fc4711ef…` and the clock 2025-10-01 07:00 UTC.
- Reused evidence: unchanged statements from the review of SQL `ee46405a157d6eb3…` (report `Evals/task_inputs/reports/0_injection.md` sha256 `d2756c231d037a7d…`; byte-identical statement text; same manifest and references).
- Any SQL edit, universe/date change or schema/contract change invalidates it. Because the SQL changed, earlier /prompt, /hardness, /oe and /rubric results (all of which read the injection) are outdated and must be rerun. /prompt can reuse checks A–C for this SQL; it still owns discoverability, persona access and feasibility.
