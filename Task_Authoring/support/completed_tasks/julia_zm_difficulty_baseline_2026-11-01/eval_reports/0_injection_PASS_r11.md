# /injection: injection data-integrity review

## 1. Scope

| Field | Value |
|---|---|
| Review | `/injection`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode |
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`. reused_evidence: rows byte-identical to revision 28 keep the prior `0_injection.md` results (r28 §4 ledger and §6, which carry per-row provenance back through revisions 25, 22, 20, 17, 14, 12, 11, 9 and earlier). See §3. |
| Actual review date | 2026-10-31 (UTC) |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut`, hg4-synth-sep30cut v16, unchanged |
| Input | `Evals/task_inputs/01_Universe_Inject.sql`, 96,048 bytes, 363 physical lines, sha256 `dd7536cdea3f183a85f4fb6c669ff59a4b8b094972ae1954278adacc790f521c` (input revision 30, attached as `01_Universe_Inject (15).sql`) |
| Prior SQL compared | revision 28, sha256 `cd185b05…95` (upload `(14)`, hash re-verified, PASS). `diff`: **only line 58 changed** (text of Leonard's DM thread reply `5f6ed4d5…`). Every other line is byte-identical, so line numbers are unchanged. |
| Assignment (context only) | Julia Lawson, Product Manager; Product; Engineering Ops; Retrieval; long-horizon |
| References | WORKFLOW.md `ee4cd8e1…`; Eval 0 `e034019b…`; known_base_issues.md `79b20289…`; schema/injection.json `31dcb2b4…` (unverified snapshot); id_contracts.json `fc4711ef…`; ENVIRONMENT.md `4ffb2b5f…`; SEARCH.md `cab83c61…`; lint `a8226e2a…`. All re-hashed and unchanged from the r28 review. |
| Lint | `hg_injection_lint.py` (injection-lint-v1) on sha256 `dd7536cd…1c`: 177 statements (BEGIN, 172 INSERT, 3 UPDATE, COMMIT); 0 FAIL / 0 CHECK / 0 INFO |

Manifest note: the review version, evidence contract, input hash and source provenance above stand in for the injection entry of `input_manifest.json` (`review_version: injection-static-v2`). This portal allows writes under `reports/` only through the report writer.

## 2. Input and authority issues

- The attached file differed from saved revision 28, so it was saved as revision 30 of the injection input before review.
- The SQL is substantive and parses in full. It makes no Confluence or Snowflake writes.
- Line numbers are physical (`\n`) lines.

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; hash, base manifest, review version | NEW, done |
| Run lint; resolve every flag | NEW: 0 flags. Checks A–C still run below. |
| Inventory every statement and target | NEW for line 58. REUSED (r28 report §4) for byte-identical rows (full-file `diff`; line numbers unchanged). |
| Check A: references, IDs, collisions | Line 58 keeps the same id, channel, author and parent as r28 (only `text` changed), so its complete collision scan and references from r28 still apply. REUSED complete results for the other keys. PASS |
| Check B: SQL structure, supported schema rules | NEW whole-file parse (lint) plus a column/value count for line 58. PASS (advisory G1 carried) |
| Check C: dates, relationships, consistency | NEW for the changed text against the other instruction layers. PASS |
| Coverage, findings, limits, one verdict | NEW, below |

Reuse basis (stage-evidence-v1): reused rows are byte-identical in the SQL. The base manifest, WORKFLOW, Eval 0, known_base_issues, schema snapshot, id contracts and fixed clock are unchanged. The edit changes no key, timestamp, author, channel or thread field, so the earlier collision, reference and chronology results still hold.

## 4. Operation ledger

Lines refer to `01_Universe_Inject.sql` (revision 30).

| Line(s) | Table / op | Record(s) | Key values checked | Base evidence | Verif. | Result |
|---|---|---|---|---|---|---|
| 3 | comment | header | "172 INSERT (one row each), 3 UPDATE" | lint: 172 INSERT, 3 UPDATE | NEW | PASS (accurate; comments are not data) |
| 5 / 363 | BEGIN / COMMIT | one transaction | all statements commit or roll back together | — | NEW (lint) | Structure OK |
| 8–16 | gdrive.drive_files ×5 | folder, agenda doc, notes doc, enrage sheet, tiers deck | unchanged | r28 §4 | REUSED | PASS |
| 19, 21 | gdocs.docs_documents ×2 | agenda, "notes for monday" | unchanged | r28 §4 | REUSED | PASS |
| 24–30 | gsheets spreadsheet + 3 sheets | `f_0ba93ae0…` | unchanged | r28 §4 | REUSED | PASS |
| 33–45 | gslides presentation, pages, elements | `f_048bf5e6…` | unchanged | r28 §4 | REUSED | PASS (A2) |
| 48, 50, 52, 54, 60 | slack.slack_messages ×5 | Leonard DM request `6f773865…`, Vincent, Brian, Leonard reply `33c941fa…`, Arthur `6995ba10…` | unchanged | r28 §4 | REUSED | PASS |
| 56 | slack.slack_messages INSERT | `914b21ab…` Julia's 9/29 DM thread parent | unchanged | r28 §4 | REUSED | PASS |
| **58** | slack.slack_messages INSERT (**text changed**) | `5f6ed4d5ae1a0a04b616af6d6d2dda43`, ts `1759267002.665190`, `D05HB64NMQU`, EMPLOYEE_0038 (Leonard), reply to `914b21ab…`. New text: "one more for the baseline: take 162, 163, 201 and 250 off the list too. just those four, on top of the ones i already left off. no comments on them either. and scratch brian editing, robert will fix rows in the session. comment access is enough for brian" | 18/18 cols/values (lint parse + hand count); no apostrophes, so no escaping needed. id, ts, channel, user, thread_parent_id, thread_ts_legacy, counts, created_at `2025-09-30T21:16:42.665190Z` unchanged from r28 | r28: id absent from complete Slack `messages/*.json` scan (4,840 files, 610,468 records); channel is an IM with both authors as members; no ts collision. ZOM-162/163/201/250 exist in Linear `/issues` (team_ZOM, Done) | NEW (text) / REUSED (keys) | PASS |
| 62 / 63 | slack bot reply + parent UPDATE (#401 thread) | `5313e8da…`, `1c181040…` | unchanged | r28 §4 | REUSED | PASS |
| 65 / 66 | slack bot reply + parent UPDATE (#265 thread) | `1491582c…`, `6a42cb69…` | unchanged | r28 §4 | REUSED | PASS |
| 69–89 | trello card, actions, DD card, checklist + items, attachment | `68daca58…` etc. | unchanged | r28 §4 | REUSED | PASS (A3, G3) |
| 92–120 | gmail threads ×5 + messages ×10 | unchanged | r28 §4 | REUSED | PASS |
| 123–131 | gcal.gcal_events ×5 | "ZM difficulty tuning" etc. | unchanged | r28 §4 | REUSED | PASS |
| 134 / 136 | github PR #401 comment `#c_2` + timeline `#ev_7` | unchanged | r28 §4 | REUSED | PASS (A5) |
| 137 | github.github_pull_requests UPDATE | `match3d#401` `updated_at` → 2025-08-25T17:02:28Z | unchanged | r28 §4 | REUSED | PASS |
| 139 / 141 | github review rev_8 + review comment rc_7 on PR #265 | unchanged | r28 §4 | REUSED | PASS (G1, G2) |
| 144–362 | linear.linear_comments ×110 | `cmt_*` on ZOM-23 … ZOM-495 (incl. closing notes on ZOM-162/163/201/250 at 186, 188, 200, 220) | unchanged | r28 §4 | REUSED | PASS (A1, A4) |

## 5. Lint flags and resolutions

| Flag | Resolution |
|---|---|
| (none) | 0 FAIL / 0 CHECK / 0 INFO. Checks A–C still run below. |

## 6. Checks A–C

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A: Records, references and IDs | **PASS** | No new or changed keys: line 58 keeps id `5f6ed4d5…` (absent from the complete r28 Slack scan, defined once in the SQL), channel `D05HB64NMQU`, author EMPLOYEE_0038 = Leonard Hayes (existing account) and parent `914b21ab…` (line 56). The four keys the text names (ZOM-162, 163, 201, 250) exist in Linear `/issues`. No ID contracts apply. Unchanged keys keep their earlier complete collision results. |
| B: SQL structure and supported schema rules | **PASS** | All 177 statements parse (lint). Line 58 is still 18 columns / 18 values; JSON text fields `'[]'`/`'{}'` match the snapshot shapes; `text_fts` not set. **Advisory G1 carried** (off-snapshot GitHub columns on lines 139/141). |
| C: Dates, relationships and consistency | **PASS** | **Clock/thread:** timestamps unchanged (2025-09-30T21:16:42Z, before 2025-10-01 07:00Z; reply follows its parent at 2025-09-29T21:38:52Z). **"on top of the ones i already left off":** Leonard's earlier left-offs are ZOM-258 (his notes doc, line 21, 9/30 15:51:58Z) and ZOM-30/49/50/161/262/275 (his DM reply, line 54, 9/30 20:07:18Z). Both come before this 21:16:42Z reply, and none overlap the four new keys, so "on top of" is accurate and the exclusions add up without conflict. **"just those four":** the list is now closed. It no longer calls the four "the level editor tickets", which removes the r28 D6 ambiguity (ZOM-173 and other editor-related tickets are not excluded). **"no comments on them either":** consistent. The four are off the register, so the checklist rule-6 change (line 83: Editor only / Not shipped tickets get a comment) doesn't reach them. Their injected historical closing notes (lines 186, 188, 200, 220) are past activity, not register comments, and don't conflict. **Brian:** "scratch brian editing … comment access is enough for brian" is unchanged from r28 and still a later correction of checklist item line 85 by the same owner. **Grader-facing text:** none (persona DM voice). **Base-data conflicts:** SC-1 to SC-3 untouched; no Snowflake or Confluence writes. |

## 7. Findings

No demonstrated defects and no unresolved required checks.

**Advisories (not failures):**
- **D6 resolved:** "just those four" makes the exclusion an explicit closed list. ZOM-173 (editor set count) and ZOM-45 stay in scope if they otherwise qualify. Leonard's 20:07 ask for "the keys of … the editor only ones" still has content after the four leave (for example ZOM-173, ZOM-277, ZOM-315 per their injected notes). /oe and /rubric should recompute that list and the per-status counts without ZOM-162/163/201/250 (and without ZOM-258 and 30/49/50/161/262/275).
- **D7 carried, downstream for /prompt:** this instruction sits in a thread reply under Julia's own 9/29 DM, not in Leonard's 9/30 request thread, so /prompt should confirm it is discoverable. Final instruction layers: card → checklist (Brian edit, rule-6 comment change) → notes doc (ZOM-258 out, Arthur view) → DM reply 20:07 (analytics/tutorial tickets out) → DM reply 21:16 (ZOM-162/163/201/250 out, Brian comment not edit). Final sharing: Robert edit, Brian comment, Arthur view, others per rule 7.
- **G1, G2, G3, D1–D5 and A1–A5 carried** unchanged from r28/r25.

## 8. Next action and downstream

Proceed to `/prompt`. Because the SQL changed, every earlier pass that read it is outdated. Rerun `/prompt`, `/hardness`, `/oe` and `/rubric` in that order.

Stage dependencies for reuse: this result depends on SQL sha256 `dd7536cd…1c`, the synth-cut manifest, the r28 dependencies (Slack `messages/*.json` id scan, `messages/D05HB64NMQU/*.json`, `channels.json`, `users.json`; GitHub `data.json`; Linear `data.json` `/issues`), the r25 dependencies for reused rows, and the reference hashes in §1.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt, then /hardness, /oe and /rubric, since the SQL changed.

Evidence limits: Static review only. No SQL was executed, and live database compatibility and Agent visibility are not certified. The schema snapshot is unverified (G1 carried). Rows byte-identical to revision 28 reuse the prior review's per-row checks under stage-evidence-v1. The single changed row (line 58) changes only message text; its key and thread fields keep their r28 complete scans.
