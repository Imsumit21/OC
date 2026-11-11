# /injection — static data-integrity review

Review version: `injection-static-v2` · Evidence contract: `stage-evidence-v1`

## 1. Scope

| Item | Value |
|---|---|
| Review | Chat run. The user named `Task_Authoring/task_inputs/01_Universe_Inject.sql`, saved as rev7 of the task SQL. It answers the portal /prompt UGT 2 failure: nothing in the universe settled whether the feedback note's "gamer friends" excludes sessions whose notes-doc relation is family, neighbor or classmate. |
| Mode | Audit (static). The SQL was never executed and the base exports are unchanged. |
| Review time | 2026-11-08 |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16). Manifest `Evals/references/universes/synthcut/universe_manifest.json` sha256 `a09c3b91…` (unchanged) |
| Saved SQL | `Evals/task_inputs/01_Universe_Inject.sql`, 714 lines, sha256 `16f9657c587a0b1e8821585cb0288a64e071594d84eea875e5e6a8d7269df68e`. It is byte-identical to `Task_Authoring/task_inputs/01_Universe_Inject.sql`. |
| Previous review | `injection-static-v2` PASS / COMPLETE on SQL sha256 `49d83af2b21d700d84efa0acecb598ad32ec9ae7ba03d7d160981b7ded9cbb61` (rev6, 712 lines). |
| Assignment (context only) | Julia Lawson, Product Manager; long-horizon; medium |
| References (hashes unchanged) | `Evals/0_Injection_Quality_Eval.md` (c1a50cb2…), `Evals/WORKFLOW.md` (05a5e45e…), `id_contracts.json` (fc4711ef…), schema snapshot, live schema/constraint export (provisional) |

## 2. Change proof and evidence reuse

- **Exact edit set (NEW).** `diff` of the rev6 SQL (`49d83af2…`, 712 lines) against rev7 (`16f9657c…`, 714 lines) shows exactly these hunks and nothing else:
  - Line 166, `gdocs.docs_documents` "ZM session notes - Robert - 06": `Age: 45` → `Age: 44`.
  - Line 202, "ZM session notes - Marcus Bennett - 03" (ZOM-600): `Age: 25` → `Age: 26`.
  - Line 222, "ZM session notes - Claire Morgan - 04": `Age: 45` → `Age: 44`.
  - Line 254, "ZM session notes - Martin Walsh - 01": `Age: 45` → `Age: 44`.
  - Each age edit keeps the body length, so every style-run offset in those rows is unchanged. No other column in those rows changed.
  - Lines 698–699 (new): a top-level `slack.slack_messages` row `676eb4bb7c6fde75e63edf27ad453971`, ts `1758818538.552913`, created_at 2025-09-25T16:42:18.552913Z, user EMPLOYEE_0038 (Leonard), channel C090N54TG79, no thread parent: "on the feedback note: friends just means people you know. family, neighbours and old classmates count the same, as long as they’re in the 25–45 band and don’t work in games. that goes for sessions already run too".
  - Line 701 (was 699): Leonard's reply `d7122186…` gains one appended sentence: ". 0.3.127 (127) on android and 0.3.38 / 0.3.40 on ios all went through the store, those are fine". The id, ts, thread parent, created_at and every other column are unchanged.
- Every line after 697 moves down by 2. Lines 1–697 are otherwise byte-identical.
- **REUSED.** Every other ledger row and Check A/B/C result from the rev6 report. Each depends only on SQL bytes outside the changed rows, the unchanged universe manifest and the unchanged reference hashes. Line references after 697 are renumbered (+2).
- **NEW.** The diff proof, the lint rerun, the authoring `base_check.py` and `sql_lint.py` reruns, the time-order rerun, and Checks A–C for lines 166, 202, 222, 254, 698–699 and 701.

## 3. Lint (`hg_injection_lint.py`, injection-lint-v1) — NEW

Run on sha256 `16f9657c…8df68e`, universe synthcut, clock 2025-10-01T07:00:00Z. 360 statements: BEGIN, 353 INSERT, 5 UPDATE, COMMIT (one INSERT more than rev6). Counts: FAIL 0, CHECK 1, INFO 5. These are the same flags as the previous review. Authoring cross-checks: `Task_Authoring/tools/base_check.py` errors 0 (1 pre-existing gcal warning); `Task_Authoring/tools/sql_lint.py` errors 0 (1 pre-existing warning).

| Flag | Line / record | Resolution |
|---|---|---|
| CHECK `unknown_column` | 676, `github.github_review_comments.seq` | Resolved, no defect (same as rev4–rev6). The column is present in the live export. Keep it. |
| INFO | 270 `gslides.slides_pages.notes`; 272 `slides_page_elements.table_json`, `ordinal`; 552 `linear.linear_comments.sequence` | Confirmed live and nullable. No action. |
| INFO | 674, `github.github_reviews.seq` | Confirmed live, NOT NULL, no default. Supplied (`3`). Keep it. |

The grader_language, padding_comment, future_date, id_contract, identities, drive_unreadable and read_only_service checks all return 0.

## 4. Operation ledger

The order follows the file. Line numbers are statement start lines in rev7 (rev6 + 2 after line 697). "R" means REUSED from the rev6 review, "N" means NEW.

| Lines | Table | Op | Records | Result | V |
|---|---|---|---|---|---|
| 1 | — | `--` comment | `-- Are you planning to inject? Yes` | Standalone line comment outside any statement; not stored. | R |
| 2 | — | BEGIN | single transaction to COMMIT at 714 | — | R |
| 3–131 | gdrive.drive_files | INSERT ×65 | 62 Docs, 2 Sheets, 1 Slides | No collisions with the 53,631 base files. Parents are existing folders owned by the file owner. created ≤ modified. | R |
| 132–255 | gdocs.docs_documents | INSERT ×62 | one per Doc file | No collisions with the 595 base docs. Each row matches its Drive row. body_text is non-empty. Lines 166, 202, 222 and 254 have the age edits (same length): see Checks A–C. | R + N |
| 257–265 | gsheets spreadsheets ×2, sheets ×3 | INSERT | Log, Register, KPI | IDs are new. Drive rows exist. grid_json parses. | R |
| 267–279 | gslides presentation ×1, pages ×3, elements ×3 | INSERT | f_a087f049… | New ID. Children reference rows inserted earlier in this SQL. | R |
| 281–283 | gcal.gcal_events | INSERT ×2 | "Friday at Claire's", Sep 26 17:00–20:00Z | IDs are new. Calendars exist. | R |
| 285–428 | gmail threads ×36 / messages ×36 | INSERT | 18 pairs, Sep 22–30 | No collisions. Users exist. Labels and history_id are consistent. | R |
| 430–551 | linear.linear_issues ×61 | INSERT | ZOM-567 … ZOM-627 | No collision (base max ZOM-566). Team, users and states are valid. | R |
| 552–672 | linear.linear_comments ×61 | INSERT | one per new issue | Parents are inserted earlier. No comment predates its issue. | R |
| 673–676 | github review `…#476#rev_3`, review comment `…#476#rc_27` | INSERT | PR match3d#476 | PR exists. No collision. Timing is after the base reviews. | R |
| 677 | github.github_pull_requests | UPDATE | updated_at → 2025-09-30T20:10:26Z | Target exists. The value is before the clock. | R |
| 678–680 | trello card / action | INSERT | card 68dc0acf…, idShort 80 | IDs are new. idShort = max + 1. Dates agree. | R |
| 682–696, 700, 704–708 | slack.slack_messages | INSERT ×12 | #zombie-design, C0880U9751A, D076RBM29JS, bot | No id or (channel, ts) collision. ts matches created_at. Line 700/701 (`d7122186…`, reply in the C090N54TG79 thread `e6a91393…`) has the appended build sentence: see Checks A–C. | R + N |
| 698 | slack.slack_messages | INSERT ×1 | `676eb4bb…`, top-level in C090N54TG79, Leonard, 2025-09-25T16:42:18Z | New id, unique in base Slack and once in the SQL. No (channel, ts) collision. ts matches created_at. Leonard is a channel member. Top-level, so no thread counter applies. | N |
| 702 | slack.slack_messages | INSERT ×1 | `167dc58a…`, reply in D05GU6L0XFH | Parent subquery on (channel, ts) resolves to the base row. | R |
| 710–713 | slack.slack_messages | UPDATE ×4 | thread counters | Each equals base plus the injected replies. The new top-level post adds no reply; the 711 counter (16, latest_reply `1758819934.612483` = `d7122186…`) is still correct. | R |
| 714 | — | COMMIT | — | — | R |

## 5. Checks

| Check | Result | Evidence |
|---|---|---|
| A — Records, references and IDs | **PASS** | NEW: `676eb4bb7c6fde75e63edf27ad453971` is unique in base Slack (about 610k messages) and appears once in the SQL; there is no ts collision in C090N54TG79. EMPLOYEE_0038 (Leonard) is a member of C090N54TG79. The builds named in `d7122186…` existed by Sep 25: Android 0.3.127 published Sep 22, iOS 0.3.40 required Sep 23, iOS 0.3.38 submitted Sep 17, Android 1943 built Sep 22 21:12Z. The age edits change no id, owner, parent or sharing value. REUSED: everything else. |
| B — SQL structure and supported schema rules | **PASS** (provisional snapshot) | NEW: the new row uses the same column list as the other Slack inserts (18 columns, 18 values) and NULL thread fields for a top-level post. The appended sentence and the age edits sit inside existing string literals; no unescaped quote is introduced. The age edits keep the body length, so style-run ends still equal the body lengths. The lint parses 360 statements. REUSED: the rest of Check B. |
| C — Dates, relationships and consistency | **PASS** | NEW: the new post's ts 1758818538.552913 equals created_at 2025-09-25T16:42:18.552913Z. It is before `d7122186…` (17:05:34Z) and the clock. Every build named in the appended sentence existed before that reply. The new ages 26 and 44 sit inside the 25–45 band the post and the feedback note state; the sessions' inclusion and the end state are unchanged (hold, 17 Done, 43 Canceled, 21 re-run notes). Time-order check (`Task_Authoring/tools/time_order_check.py`): Part 1, automatic forward references, PASS. Part 2 lists 30 descriptive pointers: the 28 the rev6 report dispositioned (REUSED: 15 OK, 13 not pointers) plus 2 on the new post (line 698). "the feedback note" points to base `/537`, created 2025-09-22T05:01:26Z, before the post: OK. "that goes for sessions already run" is not a pointer. FORWARD 0, UNRESOLVED 0. REUSED: every other row (latest event 2025-09-30T21:10:27Z). No grader-facing text. |

## 6. Findings

There are no demonstrated defects and no unresolved required static checks. The new post settles the feedback note's "friends" against the notes-doc relations; it is timed, owned and placed consistently with the existing thread. The appended build sentence names only builds that existed by Sep 25.

Advisory (unchanged, not a defect): line 1 `-- Are you planning to inject? Yes` is harmless.

## 7. Evidence limits and outside-scope items

- Schema and constraint comparisons are provisional: an unverified snapshot plus the live export.
- No live execution. The line-702 subquery depends on the base parent row being present in the deployed DB, as in rev4–rev6.
- Outside scope: search ranking, task difficulty and Agent visibility (owned by `/prompt` and `/hardness`).

## 8. Next action and downstream impact

Proceed to `/prompt`. This is a current `injection-static-v2` PASS / COMPLETE for SQL sha256 `16f9657c…8df68e`. `/prompt` may reuse it for the static checks while that hash, the universe manifest and the reference hashes above stay unchanged. `/prompt` must recheck sources on lines 166, 202, 222, 254, 698–699 and 701, and any cited line after 697 (+2). Any SQL edit requires an `/injection` rerun.

### FINAL VERDICT: PASS

Execution status: COMPLETE

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Run /prompt on the rev7 SQL.

Evidence limits: Static scope only. Schema comparisons are provisional. No live execution. Checks A–C are NEW for lines 166, 202, 222, 254, 698–699 and 701 and REUSED elsewhere under stage-evidence-v1. The diff in §2 establishes the only changes.
