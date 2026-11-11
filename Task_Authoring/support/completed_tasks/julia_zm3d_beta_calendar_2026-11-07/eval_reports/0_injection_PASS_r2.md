# Injection data-integrity review: Eval 0

## 1. Scope

| Field | Value |
|---|---|
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1` (base facts reused from the previous `injection-static-v2` report for byte-identical statements; every changed statement checked new) |
| Mode | Chat review, audit (attempt 6aea4c1e9b621f28dc3a5332) |
| Review time | 2026-11-05 |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` (unchanged since the previous review) |
| Input | `Evals/task_inputs/01_Universe_Inject.sql` (injection revision 4), 59,958 bytes, SHA-256 `25070fda5e8c02ecf5903582ed936389fce5651f94ac93bd6a36133f717acc06` (attachment to the /injection message) |
| Previous version | SHA-256 `7112c82b87ac845490f08738cc14aaf2d9f373148b348d1beec833169439351a` (FAIL: F1–F3) |
| Schema snapshot | `Evals/references/schema/injection.json` SHA-256 `31dcb2b43feca8e5c7cb67f37973f819c9b9774f12f8b15cb7da89ecd74c5151` (unverified snapshot, provisional; unchanged) |
| Lint | `hg_injection_lint.py` injection-lint-v1 |

## 2. Input / authority issues

- SQL comments mention a dossier and a `universe_schema_live.json`; neither was supplied. The comments are treated as statements of intent, not as evidence.
- No grader-facing text and no comments about padding, tool calls or pass rate (lint and manual read).

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, manifest and version | NEW, done |
| Diff against the previously reviewed SQL | NEW, done: only lines 27, 38, 49, 55–56, 58, 64–65, 67, 73, 75, 110 changed and line 137 was replaced by lines 137–138; every other line is byte-identical |
| Run lint; resolve every flag | NEW, done (0 flags) |
| Inventory every statement | NEW, done (110 statements: 76 INSERT, 34 UPDATE; no DELETE, upsert or conflict clause) |
| Check A | NEW for changed statements, REUSED for identical ones: PASS |
| Check B | NEW (whole file, lint) + REUSED: PASS (snapshot mismatches advisory) |
| Check C | NEW for changed statements and the three earlier defects, REUSED for identical ones: PASS |
| Report coverage, findings, limits, verdict | done |

## 4. Lint

`hg_injection_lint.py` ran on SHA `25070fda…acc06` against universe synthcut, clock 2025-10-01T07:00:00Z, loading slack/users, gmail/users, github, linear, trello, contacts and confluence. Counts: FAIL 0, CHECK 0, INFO 0. Checks run: future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape. Nothing to resolve. A clean lint is not a PASS, so checks A–C were completed.

## 5. Operation ledger

Statement numbers follow execution order. Statement 38 is new in this version, so statements from the old 38 onward are shifted by one compared with the previous report. "REUSED" rows are byte-identical to the previous version; their base facts came from complete scans against the same universe manifest, schema snapshot and clock (reuse conditions 1–4 of `stage-evidence-v1` hold).

| # | Table | Op | Record / target | Key values | Check result | Basis |
|---|---|---|---|---|---|---|
| 1 | slack.slack_messages | INSERT | `8b090dec…` DM D05SD5QLG94 | Frederick Stone (EMPLOYEE_0008) to Julia, 2025-09-30T20:20:00Z | ID unique (610,468 msgs); members; ts = created_at | REUSED |
| 2 | slack.slack_messages | INSERT | `2e75e232…` reply in C08R8CHB0QL | Robert (EMPLOYEE_0016), 2025-09-18T16:40Z; parent `9025d428…` | Parent in same channel; reply after parent; member | REUSED |
| 3 | slack.slack_messages | INSERT | `58d06bd5…` reply in DM D05GU6L0XFH | Robert, 2025-09-30T22:10Z; parent `c5431028…` | Parent exists; reply after parent; members. Advisory A5 | REUSED |
| 4 | slack.slack_messages | INSERT | `fa3eee2c…` C0880U9751A | Vincent Parker (EMPLOYEE_0012), 2025-09-30T20:50:12Z | Member; ID unique | REUSED |
| 5–6 | slack.slack_messages | UPDATE | `9025d428…`, `c5431028…` | reply_count 0→1 each | Base reply counts 0, so +1 correct | REUSED |
| 7–12 | gmail threads/messages | INSERT ×6 | thread `…/1844470925517303296` (Brian, Julia, Frederick) | Brian Foster, 2025-09-22T09:12Z; bodies now "Wed Oct 29" | IDs unique (complete thread scan); internal_date = date; history_id NULL. **F1 fixed**: 2025-10-29 is a Wednesday | NEW (text) / REUSED (IDs) |
| 13–18 | gmail threads/messages | INSERT ×6 | thread `…/1844835127305531392` | Brian, 2025-09-26T07:40Z; "moves from Wed Oct 29 to Fri Oct 31, 10:00 Istanbul time … two extra days" | IDs unique; In-Reply-To/References → 7–12. **F1 fixed**: Wed→Fri is two days. Advisories A2, A3 | NEW (text) / REUSED (IDs) |
| 19–22 | gcal.gcal_events | INSERT ×4 | `evt_9a4c…`, `evt_5c1e…`, `evt_a72f…`, `evt_1d6b…` | Release 2025-10-08 15:00–16:00Z; created 09-24, updated 09-26 | IDs unique (10,395 events); start/end are plan fields. Advisory A7 | REUSED |
| 23 | gdrive.drive_files | INSERT | `d_5f2c8e1b…` folder "ZM Live Ops" | parent `d_8140f09b…` (Julia root) | ID/name unique; parent exists | REUSED |
| 24 | gdrive.drive_files | INSERT | `f_7c3e91a4…` "working rules" doc | Frederick owner, Julia reader | ID unique | REUSED |
| 25 | gdocs.docs_documents | INSERT | `f_7c3e91a4…` | body 2,515 chars (ASCII), body unchanged; style_runs replaced | **F2 fixed**: TITLE 0–43 = "ZM3D beta live-ops calendar - working rules"; HEADING_2 163–181 "Span and time base", 424–429 "Scope", 611–629 "When a beat starts", 1098–1109 "Held or not", 1596–1604 "One-offs", 1797–1808 "Still to do", 2026–2035 "Push copy", 2352–2364 "Config locks". Every run starts and ends at a line boundary and covers exactly a heading line | NEW |
| 26–33 | drive_files + slides presentation/pages/elements | INSERT | `f_2b9d4e7a…` "ZM3D beta UA plan", 3 slides | Frederick, 2025-09-23 | IDs unique; readable | REUSED |
| 34–37 | drive_files + sheets_spreadsheets + sheets_sheets ×2 | INSERT | `f_e4a17c90…` | Julia owner, Frederick reader | IDs unique; parent from #23 | REUSED |
| 38 | github.github_reviews | INSERT | `harmonygames-Games/match3d#470#rev_10` | EMPLOYEE_0025 (Arthur Blake), COMMENTED, body '', submitted 2025-09-30T16:04:12Z, seq 10 | **New.** ID absent from all 2,230 base reviews (`lookup`, scan complete); last base #470 review is `rev_9` (`/reviews/2176`, APPROVED 15:51:06Z), so rev_10 is the next number; PR exists; same column shape as #43 and #47 | NEW |
| 39 | github.github_review_comments | INSERT | `#470#rc_10` → review `#470#rev_10` | 2025-09-30T16:04:12Z | ID absent from 1,387 base review comments (scan complete). **F3 fixed**: comment and its review share the same instant, matching the base pattern | NEW |
| 40–41 | github timeline + PR UPDATE | INSERT/UPDATE | `#470#ev_9`; PR updated_at 15:51:15Z→16:04:12Z | | ID unique; moves forward | REUSED |
| 42–45 | github reviews / review_comments / timeline / PR | INSERT/UPDATE | `#370#rev_1`, `#370#rc_1`, `#370#ev_5`; updated_at →2025-09-30T19:48:33Z | | IDs unique; consistent | REUSED |
| 46–49 | same for #438 | INSERT/UPDATE | `#438#rev_4`, `#438#rc_74`, `#438#ev_9`; →20:41:17Z | | IDs unique; consistent | REUSED |
| 50–52 | pr_comments / timeline / PR #454 | INSERT/UPDATE | `#454#c_4`, `#454#ev_6` | Marcus Bennett (PERSON_0396) | Unique; fits release notes | REUSED |
| 53–55 | pr_comments / timeline / PR #471 | INSERT/UPDATE | `#471#c_18`, `#471#ev_8` | Samuel Turner | Unique | REUSED |
| 56–65 | slack.slack_messages INSERT ×5 + UPDATE ×5 | bot mirrors in C093LEZGF6J | parents `c2b9c903`(16→17), `d648cbe9`(2→3), `2f138acf`(78→79), `ef414467`(3→4), `da3fe08c`(7→8) | ts = GitHub created_at | Parents/ts match; counts +1 correct; IDs unique. Advisory A4 | REUSED |
| 66–108 | linear.linear_comments INSERT ×22 + linear_issues UPDATE ×21 | 22 ZOM issues (ZOM-78 … ZOM-566) | 10 authors | Issues/authors exist; sequence 1 free; updated_at moves forward; ZOM-387 correctly not bumped | REUSED |
| 109 | trello.trello_actions | INSERT | `68dac820…` commentCard | Brian Foster, 2025-09-29T17:55:44Z | ID unique; card/board/list/member exist | REUSED |
| 110 | trello.trello_cards | UPDATE | `6851a724…` | badges.comments 1→2; dateLastActivity →2025-09-29 | Consistent | REUSED |

Internal duplicates: the only repeated leading values are the three Drive file IDs, each used once in `drive_files` and once in its content table (Docs, Slides presentation/pages/elements, Sheets spreadsheet/sheets), which is the expected cross-table link, not a key collision.

## 6. Checks

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | New keys `#470#rev_10` and `#470#rc_10` are absent from the complete GitHub `/reviews` (2,230) and `/review_comments` (1,387) arrays; `rc_10` now references `rev_10`, created earlier in the same script. All other references, actors and keys are byte-identical to the previous review, where every one resolved and every new key was unique across complete scans (Slack 610,468 messages; Gmail threads; gcal; Drive/Docs/Slides/Sheets; GitHub; Linear; Trello). One account per person; listed ID contracts met; Drive files readable. |
| B — SQL structure and supported schema rules | PASS (provisional) | 110 statements parse (lint); column and value counts match; no omitted NOT NULL column; `*_json` literals parse with the expected shape; no generated columns written; Linear dates use `YYYY-MM-DDTHH:MM:SSZ`. The new `github_reviews` row uses the same eight columns as statements 42 and 46. Snapshot comparison: MISMATCH (advisory A1). |
| C — Dates, relationships and consistency | PASS | All event timestamps are at or before 2025-10-01T07:00Z (latest 2025-09-30T22:10Z); only gcal start/end (2025-10-08) are later, as plan fields. All 13 distinct weekday/date pairs in the SQL are correct (Mon Sep 22, Fri Sep 26, Mon Oct 6, Sun Oct 12, Mon Oct 13, Sun Oct 19, Mon Oct 20, Sun Oct 26, Mon Oct 27, Wed Oct 29, Fri Oct 31, Sat Nov 1, Sun Nov 2); "Fri Oct 29" no longer appears. Doc heading runs match their heading lines. Review comment `rc_10` and review `rev_10` share 16:04:12Z, after merge but as a new COMMENTED review, which GitHub allows. Reply counts and parent/child order are correct. No grader-facing text. |

## 7. Findings

No demonstrated defects. The three defects from the previous review are fixed:

- **F1 (fixed):** "Fri Oct 29" → "Wed Oct 29" in all 12 Gmail rows (15 occurrences, 0 left). The correction's "two extra days" now matches Wed Oct 29 → Fri Oct 31.
- **F2 (fixed):** `docs_documents.style_runs_json` for `f_7c3e91a4d2b85f60e1a9c4` now has TITLE 0–43 and eight HEADING_2 runs that each cover exactly a heading line.
- **F3 (fixed):** `#470#rc_10` now belongs to the new COMMENTED review `#470#rev_10` submitted at the same instant.

### Advisories (do not affect the verdict; carried over, unchanged statements)

- **A1 · schema snapshot:** columns not in the bundled snapshot: `gcal_events.extras_json`, `drive_files.drive_id`, `slides_pages.notes`, `slides_page_elements.table_json/ordinal`, `github_review_comments.pull_request_review_id/side/start_line/start_side/subject_type/seq`, `github_reviews.seq` (now also on statement 38), `linear_comments.sequence`. If the live database lacks any of these, the script won't load.
- **A2 · Gmail threading:** the reply (13–18) has "Re:" and In-Reply-To/References but its own thread ID; Gmail would normally keep it in thread `1844470925517303296`.
- **A3 · Gmail snippet:** the reply's snippet ("Correction to my Sep 22 mail: the November…") differs from how its body starts ("Correction to my Sep 22 mail, Frederick in copy: …").
- **A4 · Slack mirrors (56–64):** subtype `bot_message` and pretext author `EMPLOYEE_0025_GITHUB_USERNAME`, whereas base #zombie-prs mirrors use subtype null and handles like `arthur.blake`.
- **A5 · Halloween retraction placement (3):** threaded under Robert's unrelated "hardcore players" DM message; findability is a `/prompt` question.
- **A6 · authority wording (doc #25):** "Product latest dated approval … if he takes that back": the approver in the data is Robert (Co-Founder & Creative Director), while Julia is the Product Manager. Hand-off to `/prompt`.
- **A7 · minor shape:** gcal `transparency='transparent'` (base all `opaque`); `thread_ts_legacy` = ts on top-level message 1; new reviews logged as `commented` timeline events (base uses `reviewed`), now including `#470#ev_9` alongside `rev_10`.
- **A8 · known base-data areas (not Snowflake/Confluence; `/prompt` decides dependence):** Linear comments touch SC-15 (ZOM-521/526), SC-38 (ZOM-552) and SC-16 (e.g. ZOM-565 "can close" while Todo). No Snowflake or Confluence record is built on.

## 8. Limits

- Outside the static scope: live execution, deploy-time schema compatibility (A1), search ranking, Agent visibility and task difficulty.
- No required static check is unresolved.

## 9. Stage dependencies (for reuse)

SQL SHA `25070fda…acc06`; universe manifest `da2f4cf0…a1a`; schema `31dcb2b4…151`; clock 2025-10-01T07:00Z; lint injection-lint-v1. New facts: `#470#rev_10`/`rc_10` absent from complete GitHub review and review-comment arrays; base #470 reviews end at `rev_9`; doc heading offsets as in statement 25. Reused facts are as recorded in the previous report's section 9 (Slack parent reply counts 0, 0, 16, 2, 78, 3, 7; Linear issues have no base comments; Trello comments badge 1). `/prompt` may rely on this stage for this SQL hash.

## 10. Next action

Proceed to `/prompt`. Because the SQL changed, any earlier `/prompt`, `/hardness`, `/oe` and `/rubric` result is outdated: run them again in that order.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt

Evidence limits: Static scope only; live deploy compatibility unverified (bundled schema snapshot lacks several columns used, advisory A1).
