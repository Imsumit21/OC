# Injection data-integrity review: Eval 0

## 1. Scope

| Field | Value |
|---|---|
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1` (nothing reused: no prior report) |
| Mode | Chat review, audit (attempt 6aea4c1e9b621f28dc3a5332) |
| Review time | 2026-11-05 |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); archive SHA-256 `d04f295b4c878cce145ad0d77fc5668962b1cb63412fc98f427a0026aeb0fb0c`; `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Input | `Evals/task_inputs/01_Universe_Inject.sql`, 59,686 bytes, SHA-256 `7112c82b87ac845490f08738cc14aaf2d9f373148b348d1beec833169439351a` (attachment to the /injection message) |
| Schema snapshot | `Evals/references/schema/injection.json` SHA-256 `31dcb2b43feca8e5c7cb67f37973f819c9b9774f12f8b15cb7da89ecd74c5151` (unverified snapshot, provisional) |
| Lint | `hg_injection_lint.py` injection-lint-v1 |

## 2. Input / authority issues

- SQL comments mention a dossier and a `universe_schema_live.json`; neither was supplied. The comments are treated as statements of intent, not as evidence.
- No grader-facing text or comments about padding or pass rate were found (see Lint).

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, manifest and version | NEW, done |
| Run lint; resolve every flag | NEW, done (0 flags) |
| Inventory every statement | NEW, done (109 statements: 75 INSERT, 34 UPDATE) |
| Check A | NEW, PASS |
| Check B | NEW, PASS (snapshot mismatches advisory) |
| Check C | NEW, **FAIL** (3 defects) |
| Report coverage, findings, limits, verdict | done |

## 4. Lint

`hg_injection_lint.py` ran on SHA `7112c82b…351a` against universe synthcut with clock 2025-10-01T07:00:00Z. Counts: FAIL 0, CHECK 0, INFO 0. Checks run: future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape. Nothing to resolve. A clean lint is not a PASS, so checks A–C below were run in full.

## 5. Operation ledger

Statement numbers follow execution order (comment-only text excluded). Sources: Slack `slack/{users,channels}.json` and `messages/<ch>/<YYYY-MM>.json`; Gmail `gmail/users.json` and `threads/*.json`; gcal/gdrive/gdocs/gslides/gsheets/linear/trello `data.json`; GitHub `github/data.json`.

| # | Table | Op | Record / target | Key values | Check result |
|---|---|---|---|---|---|
| 1 | slack.slack_messages | INSERT | `8b090dec…` DM D05SD5QLG94 | Frederick Stone (EMPLOYEE_0008) to Julia, 2025-09-30T20:20:00Z, top-level | ID unique (610,468 msgs scanned); both are channel members; ts matches created_at |
| 2 | slack.slack_messages | INSERT | `2e75e232…` reply in C08R8CHB0QL | Robert (EMPLOYEE_0016), 2025-09-18T16:40Z; parent `9025d428…` ts 1758121809.236839 | Parent exists in same channel, thread_ts matches; reply after parent; member |
| 3 | slack.slack_messages | INSERT | `58d06bd5…` reply in DM D05GU6L0XFH | Robert, 2025-09-30T22:10Z; parent `c5431028…` ts 1759248350.473459 | Parent exists (Robert, "hardcore players"), reply after parent; members 0005 and 0016 present. Advisory A5 |
| 4 | slack.slack_messages | INSERT | `fa3eee2c…` C0880U9751A | Vincent Parker (EMPLOYEE_0012), 2025-09-30T20:50:12Z | Member; ID unique; "0.3.49" exists in base (#zombie-match3d) |
| 5 | slack.slack_messages | UPDATE | `9025d428…` | reply_count 0→1, users 0→1, latest 1758213600.552913 | Base has 0 replies, so +1 is correct |
| 6 | slack.slack_messages | UPDATE | `c5431028…` | reply_count 0→1, users 0→1, latest 1759270200.638114 | Base has 0 replies, so +1 is correct |
| 7–12 | gmail.gmail_threads / messages | INSERT ×6 | thread `…/1844470925517303296` for Brian, Julia and Frederick | Brian Foster, 2025-09-22T09:12Z, "Fri Oct 29" handoff | Users exist; thread and Message-ID absent from all thread files (complete scan); internal_date = date; history_id NULL is valid. **F1** |
| 13–18 | gmail.gmail_threads / messages | INSERT ×6 | thread `…/1844835127305531392` for Brian, Julia and Frederick | Brian, 2025-09-26T07:40Z, moves handoff to Fri Oct 31 10:00 Istanbul | Unique; In-Reply-To/References point to message 7–12. **F1**; Advisories A2, A3 |
| 19–22 | gcal.gcal_events | INSERT ×4 | `evt_9a4c…`, `evt_5c1e…`, `evt_a72f…`, `evt_1d6b…` on the calendars of Douglas, Julia, Owen and Frederick | Release 2025-10-08 15:00–16:00Z (18:00–19:00 Istanbul); created 09-24, updated 09-26 | Event IDs unique (10,395 events); calendars exist; per-copy shared ical_uid and `self` flag match the base pattern; start/end are plan fields. Advisory A7 |
| 23 | gdrive.drive_files | INSERT | `d_5f2c8e1b…` folder "ZM Live Ops" | Parent `d_8140f09b…` (Julia root), created 2025-08-11 | ID and name unique; parent exists and is owned by Julia |
| 24–25 | gdrive.drive_files + gdocs.docs_documents | INSERT | `f_7c3e91a4…` "working rules" doc | Frederick owns it, Julia is reader, parent is Frederick's root; body 2,515 chars | ID unique in Drive and Docs; readable Google Doc. **F2** |
| 26–33 | drive_files + slides_presentations/pages/elements | INSERT | `f_2b9d4e7a…` "ZM3D beta UA plan", 3 slides | Frederick, 2025-09-23 | IDs unique; readable (Slides row present); weekdays correct |
| 34–37 | drive_files + sheets_spreadsheets + sheets_sheets ×2 | INSERT | `f_e4a17c90…` calendar sheet in the new folder | Julia owns it, Frederick is reader; header-only grids | IDs unique; parent created at #23 |
| 38 | github.github_review_comments | INSERT | `#470#rc_10`, review `#470#rev_9` | Arthur Blake, 2025-09-30T16:04:12Z | ID unique; PR and review exist. **F3** |
| 39–40 | github timeline + PR UPDATE | INSERT/UPDATE | `#470#ev_9`; PR updated_at 15:51:15Z→16:04:12Z | | ID unique; moves forward |
| 41–44 | github reviews / review_comments / timeline / PR | INSERT/UPDATE | `#370#rev_1`, `#370#rc_1`, `#370#ev_5`; PR updated_at 2025-08-13→2025-09-30T19:48:33Z | Arthur, review and comment at the same instant | IDs unique; consistent |
| 45–48 | same for #438 | INSERT/UPDATE | `#438#rev_4`, `#438#rc_74` (73 base comments), `#438#ev_9`; updated_at →20:41:17Z | | IDs unique; consistent |
| 49–51 | pr_comments / timeline / PR #454 | INSERT/UPDATE | `#454#c_4`, `#454#ev_6` | Marcus Bennett (PERSON_0396), PR author | Unique; the PR's release notes list no C&W icon, so the claim fits |
| 52–54 | pr_comments / timeline / PR #471 | INSERT/UPDATE | `#471#c_18`, `#471#ev_8` | Samuel Turner, PR author | Unique; the PR's notes include a "Daily Gift sprite" change |
| 55–64 | slack.slack_messages INSERT ×5 + UPDATE ×5 | bot mirrors in C093LEZGF6J | parents `c2b9c903`(16→17), `d648cbe9`(2→3), `2f138acf`(78→79), `ef414467`(3→4), `da3fe08c`(7→8) | Each ts equals the GitHub created_at | Parents and ts match; base reply counts +1 are correct; bot is a member; IDs unique. Advisory A4 |
| 65–107 | linear.linear_comments INSERT ×22 + linear_issues UPDATE ×21 | 22 ZOM issues (ZOM-78 … ZOM-566) | Authors: Douglas, Vincent, Marcus, Calvin, Brian, Oliver, Frederick, Owen, Samuel, Robert | All issues and authors exist; no base comments on these issues (sequence 1 is free); every updated_at moves forward; ZOM-387 (07-25 comment before 07-27 updated_at) correctly gets no bump; commit f7e971b0 "Endless Mode start screen VFX" (Marcus) and Jenkins build #2023 exist |
| 108 | trello.trello_actions | INSERT | `68dac820…` commentCard | Brian Foster member, 2025-09-29T17:55:44Z (ID timestamp prefix matches) | ID unique; card, board, list and member exist |
| 109 | trello.trello_cards | UPDATE | `6851a724…` | badges.comments 1→2 (other badges preserved); dateLastActivity 2025-06-30→2025-09-29 | Consistent |

## 6. Checks

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | Every referenced actor, channel, parent message, calendar, Drive parent, PR, review, Linear issue/user and Trello card/board/list/member resolves (`hg_records.py`, all scans complete). New keys are absent from their full collections: Slack messages (610,468 records, 4,840 files), Gmail threads/Message-IDs (complete scan of `threads/*.json`), gcal events, Drive files, Docs, Slides, Sheets, GitHub reviews, review comments, PR comments and timeline events, Linear comments, Trello actions. Each actor resolves to the named person with no second account (Slack EMPLOYEE_0008 Frederick, 0016 Robert, 0012 Vincent; GitHub EMPLOYEE_0025 Arthur Blake, PERSON_0396 Marcus Bennett, EMPLOYEE_0004 Samuel Turner; Linear `usr_Robert` = robert@). Listed ID contracts are met (history_id NULL; no content_path). Drive files are readable: Doc with body, Slides and Sheets rows, folder. |
| B — SQL structure and supported schema rules | PASS (provisional) | 109 statements parse; column and value counts match; no NOT NULL column without a default is omitted or set to NULL; every `*_json` literal parses with the expected shape; no generated columns are written; Linear dates use `YYYY-MM-DDTHH:MM:SSZ`. Snapshot comparison: MISMATCH (advisory A1) for columns not in the bundled snapshot. |
| C — Dates, relationships and consistency | **FAIL** | All event timestamps are at or before 2025-10-01T07:00Z (latest 2025-09-30T22:10Z); only the gcal start/end (2025-10-08, plan fields) are later. Slack ts = created_at and Gmail internal_date = date. Reply counts and parent/child order are correct apart from F3. Three introduced defects: F1, F2, F3. |

## 7. Findings

### F1 · Check C · FAIL: impossible weekday/date in Brian Foster's handoff emails

- **Where:** statements 7–12 (lines 27, 38, 49): the bodies say "The config handoff we agreed with Product is for Fri Oct 29 … by end of Fri Oct 29". Statements 13–18 (snippets in all six thread/message rows; bodies at lines 58, 67, 75) say "moves from Fri Oct 29 to Fri Oct 31".
- **Evidence:** 2025-10-29 is a **Wednesday** (Oct 31 is a Friday, and Oct 6, Nov 1 and Nov 2 are correct). The correction's own "two extra days" fits Wed Oct 29 → Fri Oct 31, so "Fri" is the wrong part. Every other weekday/date pair in the SQL is correct (13 checked).
- **Effect:** the committed date the task's config-lock rule depends on contradicts itself. A solver could read it as Wed Oct 29 or as a Friday (Oct 24), and a rubric or OE citing "Oct 29" then rests on an inconsistent record.
- **Smallest fix:** replace "Fri Oct 29" with "Wed Oct 29" in all 12 Gmail rows (the bodies and snippets of both emails, plus the thread snippets of statements 13, 15 and 17).

### F2 · Check C · FAIL: Google Doc heading ranges don't match its text

- **Where:** statement 25, `gdocs.docs_documents` `f_7c3e91a4d2b85f60e1a9c4`, `style_runs_json` (line 92).
- **Evidence:** the TITLE run 0–45 covers "…working rules\nF". The 8 HEADING_2 runs (133–152, 397–402, 570–585, 1055–1067, 1259–1268, 1500–1511, 1731–1741, 1961–1974) cover mid-sentence fragments such as "ay here; the calls ", " diff", " off this calen", " and if he". The actual headings sit at: title 0–43, "Span and time base" 163–181, "Scope" 424–429, "When a beat starts" 611–629, "Held or not" 1098–1109, "One-offs" 1596–1604, "Still to do" 1797–1808, "Push copy" 2026–2035, "Config locks" 2352–2364. The body is ASCII-only, so this is not a UTF-16 or byte offset effect. In the base, all 3,350 heading runs across 595 docs start at a line start.
- **Effect:** a reader that uses the style runs renders headings in the middle of the brief's rule sentences, garbling the document the task treats as the working rules.
- **Smallest fix:** set the runs to the offsets above (TITLE 0–43; HEADING_2 at the eight listed ranges).

### F3 · Check C · FAIL: review comment attached to a review submitted 13 minutes earlier

- **Where:** statement 38, `github.github_review_comments` `harmonygames-Games/match3d#470#rc_10` (line 137), `pull_request_review_id = '#470#rev_9'`, `created_at 2025-09-30T16:04:12Z`.
- **Evidence:** the base review `#470#rev_9` is Arthur Blake's **APPROVED** review submitted at 2025-09-30T15:51:06Z, and the PR merged at 15:51:15Z. On GitHub, a review's inline comments are published when the review is submitted. In the base, every #470 review comment shares its review's instant (rc_8 and rc_9 = rev_8 at 03:44:37Z). A comment created 13 minutes after its review was submitted, and after the merge, cannot belong to that review. Your own statements 41–42 and 45–46 already use the correct pattern: a new COMMENTED review at the same instant as its comment.
- **Smallest fix:** add `github.github_reviews` `harmonygames-Games/match3d#470#rev_10` (EMPLOYEE_0025, COMMENTED, body '', submitted_at 2025-09-30T16:04:12Z, seq 10) and point rc_10's `pull_request_review_id` at it. Keep ev_9, the PR bump and the Slack mirror as they are.

### Advisories (do not affect the verdict)

- **A1 · schema snapshot:** these columns are not in the bundled snapshot: `gcal_events.extras_json`, `drive_files.drive_id`, `slides_pages.notes`, `slides_page_elements.table_json/ordinal`, `github_review_comments.pull_request_review_id/side/start_line/start_side/subject_type/seq`, `github_reviews.seq`, `linear_comments.sequence`. The header says it was checked against a live schema that wasn't supplied. If the live database lacks any of these, the script will not load, so confirm them when you apply it.
- **A2 · Gmail threading:** the reply (13–18) has "Re:" plus In-Reply-To/References but a different thread ID from the original (7–12). Gmail would normally put it in the same thread. Consider reusing thread `1844470925517303296` with two messages per mailbox.
- **A3 · Gmail snippet:** the reply's snippet ("Correction to my Sep 22 mail: the November…") doesn't match how its body starts ("Correction to my Sep 22 mail, Frederick in copy: …").
- **A4 · Slack mirrors (55–63):** subtype `bot_message`, while all 956 base comment mirrors in #zombie-prs have subtype null. The pretext renders authors as `EMPLOYEE_0025_GITHUB_USERNAME`, while base mirrors use handles such as `arthur.blake` and `oliver.brooks`. Neither is an integrity break.
- **A5 · Halloween retraction placement (3):** it is threaded under Robert's unrelated "hardcore players" DM message from Sep 30. Structurally valid. Whether it can be found belongs to `/prompt`.
- **A6 · authority wording (doc #25):** "only with Product latest dated approval … if he takes that back". The approver in the data is Robert (Co-Founder & Creative Director), and Julia is the Product Manager. Hand-off to `/prompt`.
- **A7 · minor shape:** gcal `transparency='transparent'` (base: all `opaque`); `thread_ts_legacy` = ts on top-level message 1 (the base mostly uses null); `commented` timeline events for the new reviews (the base logs reviews as `reviewed`).
- **A8 · known base-data areas (not Snowflake/Confluence; `/prompt` decides dependence):** the injected Linear comments touch areas listed as known issues: SC-15 (ZOM-521 checklist vs open children; comments on ZOM-521/526), SC-38 (Season Pass analytics; comment on ZOM-552) and SC-16 (Linear status as proof of shipping; e.g. ZOM-565 "can close" while Todo). No Snowflake or Confluence record is built on.

## 8. Limits

- Outside the static scope: live execution, deploy-time schema compatibility (see A1), search ranking, Agent visibility and task difficulty.
- No required static check is unresolved.

## 9. Stage dependencies (for reuse)

Base facts verified (complete scans, universe synthcut, manifest SHA above): every referenced ID in the ledger resolves; every new key is unique in its collection; Slack parent reply counts (base) are 0, 0, 16, 2, 78, 3, 7; Linear issues have no base comments; GitHub #470 rev_9 = APPROVED at 15:51:06Z; Trello card comments badge = 1. Fixes F1–F3 change the SQL hash, so `/injection` must be rerun before `/prompt` can rely on this stage.

## 10. Next action

Apply F1–F3, save the new SQL and send `/injection` again. A changed SQL also outdates any earlier `/prompt`, `/hardness`, `/oe` and `/rubric` result.

### FINAL VERDICT: FAIL

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Fix F1 ("Fri Oct 29" to "Wed Oct 29" in all 12 Gmail rows), F2 (doc style_runs offsets) and F3 (give #470#rc_10 its own COMMENTED review at 16:04:12Z), then rerun /injection.

Evidence limits: Static scope only; live deploy compatibility unverified (bundled schema snapshot lacks several columns used, advisory A1).
