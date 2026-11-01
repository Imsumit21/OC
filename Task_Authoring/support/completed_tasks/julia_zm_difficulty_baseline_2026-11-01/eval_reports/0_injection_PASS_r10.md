# /injection: injection data-integrity review

## 1. Scope

| Field | Value |
|---|---|
| Review | `/injection`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode |
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`. reused_evidence: rows byte-identical to revision 25 keep the prior `0_injection.md` results (r25 §4 ledger and §6, which carry per-row provenance back through revisions 22, 20, 17, 14, 12, 11, 9 and earlier). Line numbers are remapped below. See §3. |
| Actual review date | 2026-10-31 (UTC) |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut`, hg4-synth-sep30cut v16, unchanged |
| Input | `Evals/task_inputs/01_Universe_Inject.sql`, 96,059 bytes, 363 physical lines, sha256 `cd185b05da3d1db6fd0222f8a65795265eb1aff028e43039e92b5afd5af59795` (input revision 28, attached as `01_Universe_Inject (14).sql`) |
| Prior SQL compared | revision 25, sha256 `2ee488e2…6a` (upload `(13)`, hash re-verified, PASS). `diff`: header line 3 (counts), **2 new Slack INSERTs** (Julia → Leonard DM thread parent + Leonard's reply), **1 new UPDATE** (`github_pull_requests.updated_at` on match3d#401). Every other row is byte-identical (verified by `diff` of r28 60–136 vs r25 56–132 and r28 138–363 vs r25 133–358). |
| Line remap (old → new) | 1–55 → 1–55 (line 3 changed); 56–132 → 60–136; 133–358 → 138–363. New lines: 56–59, 137. |
| Assignment (context only) | Julia Lawson, Product Manager; Product; Engineering Ops; Retrieval; long-horizon |
| References | WORKFLOW.md `ee4cd8e1…`; Eval 0 `e034019b…`; known_base_issues.md `79b20289…`; schema/injection.json `31dcb2b4…5151` (unverified snapshot); id_contracts.json `fc4711ef…`; ENVIRONMENT.md `4ffb2b5f…`; SEARCH.md `cab83c61…`; lint `a8226e2a…`. All re-hashed and unchanged from the r25 review. |
| Lint | `hg_injection_lint.py` (injection-lint-v1) on sha256 `cd185b05…95`: 177 statements (BEGIN, 172 INSERT, 3 UPDATE, COMMIT); 0 FAIL / 0 CHECK / 0 INFO |

Manifest note: the review version, evidence contract, input hash and source provenance above stand in for the injection entry of `input_manifest.json` (`review_version: injection-static-v2`). This portal allows writes under `reports/` only through the report writer.

## 2. Input and authority issues

- The attached file differed from saved revision 25, so it was saved as revision 28 of the injection input before review.
- The SQL is substantive and parses in full. It makes no Confluence or Snowflake writes.
- Line numbers are physical (`\n`) lines.

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; hash, base manifest, review version | NEW, done |
| Run lint; resolve every flag | NEW: 0 flags. Checks A–C still run below. |
| Inventory every statement and target | NEW for the 3 new rows and the header. REUSED (r25 report §4) for byte-identical rows, with lines remapped (§1). Remap spot-checked at lines 60, 62, 63, 65, 66, 69, 77, 89, 92, 120, 139, 144, 244, 362 and 363, plus full-block `diff`. |
| Check A: references, IDs, collisions | NEW complete scans for the 2 new Slack keys, plus actor/channel/parent/target resolution. REUSED complete collision results for unchanged keys. PASS |
| Check B: SQL structure, supported schema rules | NEW whole-file parse (lint) plus column/value count for the new rows. PASS (advisory G1 carried) |
| Check C: dates, relationships, consistency | NEW for the new records and the PR update, including interaction with the earlier instruction layers. PASS |
| Coverage, findings, limits, one verdict | NEW, below |

Reuse basis (stage-evidence-v1): reused rows are byte-identical in the SQL. The base manifest, WORKFLOW, Eval 0, known_base_issues, schema snapshot, id contracts and fixed clock are unchanged. The new rows add two keys (checked fresh) and update one base PR's `updated_at`; no other existing key, timestamp or reference changes, so the earlier collision and chronology results still hold.

## 4. Operation ledger

Lines refer to `01_Universe_Inject.sql` (revision 28).

| Line(s) | Table / op | Record(s) | Key values checked | Base evidence | Verif. | Result |
|---|---|---|---|---|---|---|
| 3 | comment | header | "172 INSERT (one row each), 3 UPDATE" | lint: 172 INSERT, 3 UPDATE | NEW | PASS (accurate; comments are not data) |
| 5 / 363 | BEGIN / COMMIT | one transaction | all statements commit or roll back together | — | NEW (lint) | Structure OK |
| 8–16 | gdrive.drive_files ×5 | folder, agenda doc, notes doc, enrage sheet, tiers deck | unchanged | r25 §4 | REUSED | PASS |
| 19, 21 | gdocs.docs_documents ×2 | agenda, "notes for monday" | unchanged | r25 §4 | REUSED | PASS |
| 24–30 | gsheets spreadsheet + 3 sheets | `f_0ba93ae0…` | unchanged | r25 §4 | REUSED | PASS |
| 33–45 | gslides presentation, pages, elements | `f_048bf5e6…` | unchanged | r25 §4 | REUSED | PASS (A2) |
| 48, 50, 52, 54, 60 | slack.slack_messages ×5 | Leonard DM request `6f773865…`, Vincent, Brian, Leonard reply `33c941fa…`, Arthur `6995ba10…` | unchanged | r25 §4 (old 48–56) | REUSED | PASS |
| **56** | slack.slack_messages INSERT (**new**) | `914b21ab6448fac2e4b4f8d164bea41a`, ts `1759181932.207413`, `D05HB64NMQU`, EMPLOYEE_0005 (Julia Lawson), "leonard, anything you need from me before monday's tuning session?" | 18/18 cols/values. Thread parent: reply_count 1, reply_users_count 1, latest_reply `1759267002.665190` (= line 58 ts). created_at 2025-09-29T21:38:52.207413Z = ts | Slack `messages/*.json` id scan: absent (4,840 files, 610,468 records, complete). `channels.json`: `D05HB64NMQU` is_im, members include EMPLOYEE_0005 and EMPLOYEE_0038. `users.json`: EMPLOYEE_0005 = Julia Lawson, EMPLOYEE_0038 = Leonard Hayes. Base DM files end at 2025-08 (4,378 messages); no ts collision | NEW | PASS |
| **58** | slack.slack_messages INSERT (**new**) | `5f6ed4d5ae1a0a04b616af6d6d2dda43`, ts `1759267002.665190`, EMPLOYEE_0038 (Leonard), reply to `914b21ab…`. Text: leave ZOM-162/163/201/250 off ("level editor tickets … no comments on them either"); Brian gets comment access instead of edit | 18/18. thread_parent_id = line 56 id, thread_ts_legacy = line 56 ts; reply_count/users 0, latest_reply NULL. created_at 2025-09-30T21:16:42.665190Z = ts | id absent (same complete scan); no ts collision in the DM (base or SQL: other DM ts are `1759261706.530914`, `1759262838.442871`) | NEW | PASS (D6, D7) |
| 62 / 63 | slack bot reply + parent UPDATE (#401 thread) | `5313e8da…`, `1c181040…` | unchanged | r25 §4 (old 58/59) | REUSED | PASS |
| 65 / 66 | slack bot reply + parent UPDATE (#265 thread) | `1491582c…`, `6a42cb69…` | unchanged | r25 §4 (old 61/62) | REUSED | PASS |
| 69–89 | trello card, actions, DD card, checklist + items, attachment | `68daca58…` etc. (line 85 = "rule 7 change: Brian gets edit as well") | unchanged | r25 §4 (old 65–85) | REUSED | PASS (A3, G3) |
| 92–120 | gmail threads ×5 + messages ×10 | unchanged | r25 §4 (old 88–116) | REUSED | PASS |
| 123–131 | gcal.gcal_events ×5 | "ZM difficulty tuning", 2025-10-06 17:00–18:00Z, created 2025-09-29T18:24:51Z | unchanged | r25 §4 (old 119–127) | REUSED | PASS |
| 134 / 136 | github PR #401 comment `#c_2` + timeline `#ev_7`, both 2025-08-25T17:02:28Z | unchanged | r25 §4 (old 130/132) | REUSED | PASS (A5) |
| **137** | github.github_pull_requests UPDATE (**new**) | `harmonygames-Games/match3d#401` `updated_at` 2025-08-25T16:42:14Z → 2025-08-25T17:02:28Z | Target resolves (exactly one record with this id; `/pull_requests` 2,475 records, complete). `updated_at` is a snapshot column. Only `updated_at` changes; state closed, merged, merged_at/closed_at 16:42:14Z untouched | Base #401: created 16:41:49Z, base comment c_1 16:41:56Z, merged/closed 16:42:14Z, base ev_1–ev_5 (last 16:42:14Z); no base reviews or review comments. Latest activity after the SQL is the injected c_2/ev_7 at 17:02:28Z | NEW | PASS |
| 139 / 141 | github review rev_8 + review comment rc_7 on PR #265 | unchanged | r25 §4 (old 134/136) | REUSED | PASS (G1, G2) |
| 144–362 | linear.linear_comments ×110 | `cmt_*` on ZOM-23 … ZOM-495 (ZOM-258 at 226; ZOM-281 `tiers:` note at 244; ZOM-312 closing note at 280) | unchanged | r25 §4 (old 139–357) | REUSED | PASS (A1, A4) |

## 5. Lint flags and resolutions

| Flag | Resolution |
|---|---|
| (none) | 0 FAIL / 0 CHECK / 0 INFO. Checks A–C still run below. |

## 6. Checks A–C

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A: Records, references and IDs | **PASS** | **New keys:** Slack `914b21ab…` and `5f6ed4d5…`, both absent from a complete scan of all 4,840 message files and each defined once in the SQL (`914b21ab…` also appears as line 58's `thread_parent_id`, a valid in-SQL reference). **References:** channel `D05HB64NMQU` exists and both authors are members; EMPLOYEE_0005 = Julia Lawson and EMPLOYEE_0038 = Leonard Hayes (existing accounts, no second account). The UPDATE target `match3d#401` resolves to exactly one PR (the other `number = 401` match is GameOfDominoes#401, a different id). The ZOM keys named in Leonard's text (162, 163, 201, 250) all exist in Linear `/issues` (team_ZOM, Done). **ID contracts:** none apply to the new rows. Unchanged keys keep their earlier complete collision results. |
| B: SQL structure and supported schema rules | **PASS** | All 177 statements parse (lint). Hand counts: both new slack_messages rows 18/18; JSON text fields `'[]'`/`'{}'` parse with the snapshot's shapes; `text_fts` not set. The UPDATE sets `updated_at`, which is in the `github.github_pull_requests` snapshot, with an ISO-8601 Z value like the base. **Advisory G1 carried** (off-snapshot GitHub columns on lines 139/141; see r25). |
| C: Dates, relationships and consistency | **PASS** | **Clock:** new event times 2025-09-29T21:38:52Z and 2025-09-30T21:16:42Z are before 2025-10-01 07:00Z; the PR update value is 2025-08-25. **Thread:** reply follows parent by ~23.6 h; parent's reply_count 1 / reply_users_count 1 / latest_reply match the single reply. **Chronology with other records:** the "ZM difficulty tuning" invite (Oct 6, Monday) was created 2025-09-29T18:24:51Z, before Julia's 21:38:52Z question, so "monday's tuning session" refers to an event Julia already had. Leonard's reply (21:16:42Z on 9/30) is after his request (19:48:26Z), his first follow-up (20:07:18Z), the card update (14:04:31Z), the notes doc (15:51:58Z) and the checklist (16:20:11Z), so it is the latest instruction. Its "scratch brian editing … comment access is enough for brian" supersedes checklist item line 85 ("Brian gets edit as well") by the same owner, later in time; this is a supported later correction, not a contradiction. **Facts:** ZOM-162 "…linked across tiers in level editor", ZOM-163 "Play button in level editor…", ZOM-201 "…stat window… overlay in editor", ZOM-250 "…attack power stats in level editor" are all level-editor tickets, and their injected closing notes (lines 186, 188, 200, 220: "closing. works on the dev build") don't conflict. "no comments on them either" agrees with rule 6 (Editor only/Not shipped stay uncommented) and narrows checklist rule 6's change for these four. **PR #401 UPDATE:** fixes, rather than introduces, a mismatch: the injected comment and timeline event (17:02:28Z) were later than base `updated_at` 16:42:14Z; now `updated_at` equals the latest activity, and a comment after merge on a closed PR is valid. **Grader-facing text:** none (persona DM text). **Base-data conflicts:** SC-1 to SC-3 untouched; no Snowflake or Confluence writes. |

## 7. Findings

No demonstrated defects and no unresolved required checks.

**Advisories (not failures):**
- **D6 (new), downstream for /prompt, /oe and /rubric — list scope ambiguity:** Leonard says "leave the level editor tickets off too (162, 163, 201 and 250)". Other in-scope title matches are also level-editor work: **ZOM-173** "Item Set Count in editor not updating with difficulty tier changes" (Done; its injected note at line 190 says "the set count in the level objects panel"), and ZOM-45 "Expose the ability to mark level difficulty in editor…" (its note says the game reads it at runtime). ZOM-203 is a Duplicate, so it's already out. The explicit key list makes the instruction executable, so this is not a data defect, but a reader could take "the level editor tickets" as a category and also drop ZOM-173. The OEs and rubric should follow the four listed keys. If you want no room for doubt, have Leonard say "just these four" or add ZOM-173 to his list. Also, Leonard's 20:07 reply still asks for "the keys of … the editor only ones". Editor-only candidates remain after the four are removed (for example ZOM-173, ZOM-277, ZOM-315 per their injected notes), so that ask still has content. /oe and /rubric should recompute that list and the per-status counts without the four.
- **D7 (new), downstream for /prompt:** the new instructions sit in a *thread reply* under Julia's own 9/29 DM, not in Leonard's 9/30 request thread. Reading it needs the thread replies of that parent. /prompt should confirm it is discoverable. The instruction layers are now: card → checklist (Brian edit, rule 6 comment change) → Leonard's notes doc (ZOM-258 out, Arthur view) → DM reply 20:07 (analytics/tutorial tickets out) → **DM reply 21:16 (ZOM-162/163/201/250 out, Brian comment not edit)**. /oe and /rubric should reflect the final sharing: Robert edit, Brian comment, Arthur view, others per rule 7.
- **G1, G2, G3, D1–D5 and A1–A5 carried** unchanged from r25 (off-snapshot GitHub columns; rc_7 line/commit cosmetic; attachment without action; notes doc instructions; Blake "not tiers" rule on ZOM-312; prior instruction layering notes).

## 8. Next action and downstream

Proceed to `/prompt`. Because the SQL changed, every earlier pass that read it is outdated. Rerun `/prompt`, `/hardness`, `/oe` and `/rubric` in that order.

Stage dependencies for reuse: this result depends on SQL sha256 `cd185b05…95`, the synth-cut manifest, Slack `messages/*.json` (id scan), `messages/D05HB64NMQU/*.json` (ts check), `channels.json`, `users.json`; GitHub `data.json` (`/pull_requests`, `/pull_request_comments`, `/timeline_events`, `/reviews`, `/review_comments`); Linear `data.json` `/issues`; the r25 dependencies for reused rows; and the reference hashes in §1.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt, then /hardness, /oe and /rubric, since the SQL changed.

Evidence limits: Static review only. No SQL was executed, and live database compatibility and Agent visibility are not certified. The schema snapshot is unverified (G1 carried). Rows byte-identical to revision 25 reuse the prior review's per-row checks under stage-evidence-v1; both new keys had fresh complete collision scans.
