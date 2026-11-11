# /injection — static data-integrity review

Review version: `injection-static-v2` · Evidence contract: `stage-evidence-v1`
Review time: 2026-11-09 (local session)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Universe: `Universe_SynthCut` (source hg4-synth-sep30cut v16)

### FINAL VERDICT: PASS

Execution status: COMPLETE

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Evaluator model: Claude Opus 5.5 (claude-opus-5-5), default effort, with four parallel read-only subagents (Check A; Check C messaging; Check C docs/drive/contacts; time-order Part 2)

Next action: Proceed to /prompt. Strongly recommended before submission (advisory, not a Check A FAIL under Eval 0): change the Slack id at L881 from `9c4e7a1d03b85f26e1a4d70c5b2f9e38` to `a4721db4ba861c926965546ca48efbd9` (= sha256('C090N54TG79|1758819012.336518')[:32]) so it follows the pattern every other injected and base Slack id follows, and so the authoring gate `base_check.py` passes.

Evidence limits: Static review only. No live execution or deployment compatibility. The L884 subselect relies on the database-assigned id of a base row that has no exported `id` (runtime limit). Search ranking, Agent visibility and task difficulty are outside this stage.

## Inputs and provenance

| Item | Value |
|---|---|
| SQL | `Evals/task_inputs/01_Universe_Inject.sql` (saved input rev 16; identical to `Task_Authoring/task_inputs/01_Universe_Inject.sql`) |
| SQL sha256 | `3a98aa36aaddb72cfe833311ca57760c002aef26929d3a82ccba309ed247b52d` (363,957 bytes) |
| Origin | rev9: adds Leonard's #zombie-design coaching rule (2025-09-25T16:50:12Z) |
| Universe date | saved `02_Universe_Date.txt` sha256 `189e2ac6…` → synthcut |
| Schema used | Evals bundled snapshot (provisional) + `Task_Authoring/references/universe_schema_live.json` (2026-10-04 platform export) |
| Tools | `hg_injection_lint.py` (injection-lint-v1); `Task_Authoring/tools/sql_lint.py`; `base_check.py`; `time_order_check.py`; Evals `hg_search.py lookup/get-many`, `hg_records.py` |

## Operation ledger

538 statements, `BEGIN` (L2) … `COMMIT` (last line), no ON CONFLICT, no DELETE. 531 INSERT rows (one tuple per statement), 5 UPDATEs.

| Service/table | Op | Rows | IDs / targets | Result |
|---|---|---|---|---|
| gdrive.drive_files | INSERT | 86 | 82 Docs, 3 Sheets, 1 Slides; parents = 15 base folders | A/B/C PASS |
| gdocs.docs_documents | INSERT | 82 | drive_file_id = matching Drive row | PASS |
| gsheets.sheets_spreadsheets / sheets_sheets | INSERT | 3 / 4 | incl. `f_43bc35baf77fd59f4e57b8` (ZM audience sessions), `f_cadae9f611d82d56ac02c3` (QA matrix), KPI sheet | PASS |
| gslides presentations / pages / elements | INSERT | 1 / 3 / 3 | `f_a087f049d271e9aa9f567f` | PASS |
| gcal.gcal_events | INSERT | 2 | organizer + attendee copies, ical_uid `4b728ac5…@hg4` | PASS (INT-11 advisory) |
| gmail.gmail_threads / gmail_messages | INSERT | 40 / 42 | all new threads; 14 existing mailboxes | PASS |
| linear.linear_issues / linear_comments | INSERT | 81 / 81 | ZOM-567…647 (base max ZOM-566), team_ZOM | PASS |
| github.github_reviews / review_comments | INSERT | 1 / 1 | `match3d#476#rev_3`, `#rc_27` (seq 3 / 27) | PASS |
| github.github_pull_requests | UPDATE L857 | 1 | `harmonygames-Games/match3d#476` updated_at 19:03:57Z → 20:10:26Z | PASS |
| trello.trello_cards / trello_actions | INSERT | 1 / 1 | card `68dc0acf1815df76ed9b887d` (idShort 80, board max 79), createCard | PASS |
| slack.slack_messages | INSERT | 17 | L862–L890, L902, L904 | PASS (L880 id advisory) |
| slack.slack_messages | UPDATE L892–895 | 4 | parents `c53936d6…`, `e6a91393…`, D05GU6L0XFH@1758901945.292269, `637fc98b…` | PASS (counters recounted) |
| contacts.contacts | INSERT | 82 | 80 session players + Ayşe Polat, Daniel Hughes | PASS |

Full per-row coverage is in the subagent outputs (scratch `checkA/`, `checkC1/`, `checkC2/`, `ptr/`); no row was sampled away.

## Lint flags and resolutions

| Flag | Line | Resolution |
|---|---|---|
| CHECK unknown_column `github.github_review_comments.seq` | 856 | Keep. Live export lists `seq` NOT NULL, no default; dropping it would fail the insert. |
| INFO `gslides.slides_pages.notes`, `slides_page_elements.table_json`, `.ordinal`, `linear.linear_comments.sequence` | 350, 352, 692 | Confirmed live, nullable. Advisory only. |
| INFO `github.github_reviews.seq` | 854 | Confirmed live NOT NULL; keep. |
| sql_lint warn: UPDATE not keyed on id | 894 | Predicate `channel_id='D05GU6L0XFH' AND ts='1758901945.292269'` matches exactly one base row (slack/messages/D05GU6L0XFH/2025-09.json idx 453), which has no exported `id`. Acceptable. |
| base_check FAIL: Slack id contract | 880/881 | See Check A advisory. Not a listed `id_contracts.json` contract, so not an Eval 0 FAIL. |
| base_check warn INT-11: no invitation mail for 'Friday at Claire's' | 361 | Integration realism, not a data-integrity defect under Eval 0. Optional: add invitation copies or record an integration exception. |

## Checks

| Check | Result | Evidence |
|---|---|---|
| A — Records, references and IDs | PASS | **Collisions:** checked in full against base: Drive 86 vs 53,631; Docs 82 vs 595; Sheets 3 vs 356; Slides 1/3/3 vs 132/2,309/2,231; GCal 2 vs 10,395; Gmail 40 threads vs 81,404 and 42 messages vs 95,164; Linear 81 vs 3,687; GitHub rev_3/rc_27 vs 2,230/1,387; Trello vs 803/5,252, shortLink unused; Slack 17 vs 610,468, no (channel, ts) collision; Contacts 82 vs 170. No duplicates within the SQL. **References:** all resolve: users and channel membership, thread parents (3 base, 1 SQL L904→L902), Linear users and issues, Drive parents owned by the file owner, mailboxes, PR #476, Trello board/list/members, calendars. All 5 UPDATE targets match exactly one row. **ID contracts:** Gmail history_id is NULL; no content_path is used. **Readability:** every Drive file has non-empty Docs body, Sheets grid or Slides elements. **Identity:** one account per person; authors match signatures and owners; the 82 contacts duplicate no base person (8 share only a first or last name, with different other names). **Advisory:** L881 Slack id `9c4e7a1d03b85f26e1a4d70c5b2f9e38` ≠ sha256('C090N54TG79\|1758819012.336518')[:32] = `a4721db4ba861c926965546ca48efbd9`. The other 16 injected Slack ids and 2,709/2,709 base ids in C090N54TG79 follow the pattern. It isn't a listed contract, so it doesn't fail; fix recommended. |
| B — SQL structure and supported schema rules | PASS | Single BEGIN…COMMIT. 531 tuples, each with value count = column count. No duplicate columns or SET assignments. Every table/column exists in the live export, and every NOT NULL no-default column is supplied (incl. `github_reviews.seq`, `github_review_comments.seq`). No NULL into NOT NULL, no generated/`_fts` columns, no Confluence/Snowflake writes. All `*_json` literals parse. Linear dates are all `YYYY-MM-DDTHH:MM:SSZ`. Booleans and numerics are typed correctly. One scalar subselect (L884 thread_parent_id); its target is unique in base. Snapshot comparison: MATCH except the INFO/CHECK columns above, which the live export confirms. |
| C — Dates, relationships and consistency | PASS | **Timestamps:** every event timestamp ≤ clock; the latest is Slack `b07f1e10` at 2025-09-30T21:10:27Z. Slack ts = created_at. Gmail internal_date, date and header agree. **Chronology:** replies follow parents. Slack counters recount exactly: 3/2, 16/3, 2/2, 30/1, plus the new parent 1/1. Gmail replies (L433/L439) follow the Sep 26 message in the same thread and mailbox. Linear: issue created ≤ comment ≤ updated for all 81 pairs. PR review/comment fall inside the PR and updated_at is raised. Trello card id time = dateLastActivity = createCard. GCal end > start. **Mirroring:** Docs/Sheets/Slides owner, sharing, visibility and dates mirror Drive. **Facts:** 80/80 log rows ↔ notes docs ↔ ZOM-568…647 agree on date, observer, audience and stars. Form emails ↔ session counts total 80. KPI sheet 45/45 rows match Snowflake USER_COHORT_RETENTION. Builds 0.3.127 (1943) and Vision Bot #15 match base #ci. Leonard's quoted feedback note matches base C090N54TG79 ts 1758517286.431379. **Supported stale/superseded records:** the KPI simple mean 8.63 is narrowed by Vincent's note. Claire's "no coaching" form is corrected by her L507 mail and covered by the rev9 rule. Owen's late sessions are covered by Julia's L176 note. Build 1943 is flagged by L883. Brian's Kadıköy sessions are superseded by his DM and the L876 rule. **Time-order:** Part 1 (automatic forward references) PASS. Part 2 covered all 35 descriptive pointers: 11 resolve to earlier records (e.g. L858 "her log note" → `f_c691d577b8f837eb4f9eaa` 16:24Z vs card 16:52Z; L888 "the roadmap card" → card 16:52Z vs post 21:10Z; L862–880 "the feedback note" → base 09-22T05:01Z; L902 "the thread" → QA sheet 14:40Z vs post 15:12Z). 24 are generic or in-game card/deck/board wording, and none points forward. **Grader-facing text:** none. The only SQL comment is L1 `-- Are you planning to inject? Yes`. |

Pre-existing base context (not introduced): PR #476 has 8 "reviewed" timeline events against 2 reviews; two C0880U9751A parents carry reply_users_count that disagrees with their replies; Marcus and Arthur "left on Sep 11" refers to a channel exit only (both active in Sep per activity data).

## Fixes

No demonstrated defect. Recommended (advisory):
1. L881: replace id `9c4e7a1d03b85f26e1a4d70c5b2f9e38` with `a4721db4ba861c926965546ca48efbd9`.
2. Optional: INT-11 invitation-mail copies for gcal 'Friday at Claire's' (L361), or a recorded integration exception.

## Stage evidence for reuse

Reusable by /prompt while the SQL hash stays `3a98aa36…`: record existence, IDs, references, dates and cross-record facts above. Any SQL edit (including fix 1) invalidates this hash. Fix 1 only changes one id that has no foreign references, so a rerun needs only Check A on that row plus the lint, sql_lint and base_check.
