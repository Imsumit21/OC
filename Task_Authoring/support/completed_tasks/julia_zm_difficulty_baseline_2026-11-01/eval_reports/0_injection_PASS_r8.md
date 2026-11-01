# /injection: injection data-integrity review

## 1. Scope

| Field | Value |
|---|---|
| Review | `/injection`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode |
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`. reused_evidence: rows byte-identical to revision 20 keep the prior `0_injection.md` results (sha256 `29da238a53a68eda243c56ebf752b09054baadfbc2dd2a6e8ac094fee61ad182`, §4 ledger and §6), which carry per-row provenance back through revisions 17, 14, 12, 11, 9 and earlier. See §3. |
| Actual review date | 2026-10-31T04:02Z (UTC) |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut`, hg4-synth-sep30cut v16. `universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a`, unchanged |
| Input | `Evals/task_inputs/01_Universe_Inject.sql`, 89,187 bytes, 345 physical lines, sha256 `52c581f442c120a641e1dc1c7f6b8dd9e4ad089fd9faf5e1a87b7710b4bfba43` (input revision 22, attached as `01_Universe_Inject (12).sql`) |
| Prior SQL compared | revision 20, sha256 `6972a450…858b` (upload `(11)`, PASS). `diff`: only lines 58 (Trello card `desc`) and 66 (updateCard `data.card.desc`) differ. Both make the same edit to rule 5: "; where a write-up and the build disagree, go by the build." becomes ". For when a new player gets their starting tier, where a write-up and the build disagree, go by the build. For which games promotion and demotion look at, write it the way ZOM-42 words it." Every other line, including the header and all keys, is byte-identical. The 70 bare CR bytes inside the Gmail bodies (lines 81–107, CRLF line endings) are unchanged. |
| Assignment (context only) | Julia Lawson, Product Manager; Product; Engineering Ops; Retrieval; long-horizon |
| References | WORKFLOW.md `ee4cd8e1…cd5d`; Eval 0 `e034019b…3eff`; known_base_issues.md `79b20289…3a7b`; schema/injection.json `31dcb2b4…5151` (unverified snapshot); id_contracts.json `fc4711ef…4682`; ENVIRONMENT.md `4ffb2b5f…e165`; SEARCH.md `cab83c61…a45c`; lint `a8226e2a…448b`. All re-hashed; same as the prior review. |
| Lint | `hg_injection_lint.py` (injection-lint-v1) on sha256 `52c581f4…a43`: 167 statements (BEGIN, 164 INSERT incl. linear_comments 110, 1 UPDATE, COMMIT); 0 FAIL / 0 CHECK / 0 INFO |

Manifest note: the review version, evidence contract, input hash and source provenance above stand in for the injection entry of `input_manifest.json` (`review_version: injection-static-v2`). This portal allows writes under `reports/` only through the report writer.

## 2. Input and authority issues

- The attached file differed from saved revision 20, so it was saved as revision 22 of the injection input before review.
- The SQL is substantive and parses in full. It makes no Confluence or Snowflake writes.
- Line numbers are physical (`\n`) lines of each statement's VALUES row.

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; hash, base manifest, review version | NEW, done |
| Run lint; resolve every flag | NEW: 0 flags. Checks A–C still run below. |
| Inventory every statement and target | NEW for the 2 changed rows. REUSED (prior report §4) for the byte-identical rows, same line numbers. Statement map re-derived (`grep`), matches the prior ledger. Full ledger in §4. |
| Check A: references, IDs, collisions | No key added or changed (diff). Changed rows keep ids `68daca5871dba40417a00383` / `68dbe36f4b2b4fffb7525fde`. REUSED complete collision results for every key. PASS |
| Check B: SQL structure, supported schema rules | NEW whole-file parse via lint. NEW literal parse of lines 58 and 66: 18/18 and 7/7 columns/values; line 66 `data_json` (E-string unescaped) parses as a JSON object. PASS |
| Check C: dates, relationships, consistency | NEW for the changed text: line 58 desc = line 66 `card.desc`, compared against base ZOM-42 (`/issues/3485`), ZOM-199 (`/issues/3243`), ZOM-303 (`/issues/3358`), the deck text (line 37), Blake's mail and reply (lines 81–107), Leonard's DM and reply (44, 50), the card comment (68) and the checklist items (72, 74). PASS |
| Coverage, findings, limits, one verdict | NEW, below |

Reuse basis (stage-evidence-v1): reused rows are byte-identical in the SQL. The base manifest, WORKFLOW, Eval 0, known_base_issues, schema snapshot, id contracts and fixed clock are unchanged. The edit changes no key, timestamp or reference, so the earlier collision and chronology results still hold.

## 4. Operation ledger

Lines refer to `01_Universe_Inject.sql` (revision 22). REUSED rows are byte-identical to revision 20 and keep that report's results.

| Line(s) | Table / op | Record(s) | Key values checked | Base evidence | Verif. | Result |
|---|---|---|---|---|---|---|
| 3 | comment | header | "164 INSERT (one row each), 1 UPDATE" | lint: 164 INSERT, 1 UPDATE | NEW (lint) | PASS (accurate; comments are not data) |
| 5 / 345 | BEGIN / COMMIT | one transaction | all statements commit or roll back together | — | NEW (lint parse) | Structure OK |
| 8–14 | gdrive.drive_files ×4 | folder "ZM Difficulty", agenda doc, enrage sheet, tiers deck | unchanged | prior §4 | REUSED | PASS |
| 17 | gdocs.docs_documents | `f_9ec79682…` | non-empty body_text | prior §4 | REUSED | PASS |
| 20–26 | gsheets spreadsheet + 3 sheets | `f_0ba93ae0…` | unchanged | prior §4 | REUSED | PASS |
| 29–41 | gslides presentation, 3 pages, 3 elements | `f_048bf5e6…` (line 37: starting tier "first 10 levels; 90 or more", promotion "80% or more over the last 10 attempts", demotion "4 losses in a row") | unchanged | prior §4 | REUSED | PASS (advisory A2) |
| 44, 46, 48, 50, 52 | slack.slack_messages ×5 | Leonard DM parent (with the starting-tier question), Brian 09-29, Vincent 09-30, Leonard reply 20:07:18Z, Arthur 09-03 | unchanged | prior §4 | REUSED | PASS |
| 54 / 55 | slack bot reply + parent UPDATE | `5313e8da…`, `1c181040…` reply_count 2→3 | unchanged | prior §4 | REUSED | PASS |
| 58 | trello.trello_cards INSERT (**changed**) | `68daca5871dba40417a00383` | Only `desc` changes: rule 5's last sentence is split into a starting-tier clause ("go by the build") and a promotion/demotion clause ("write it the way ZOM-42 words it"). 18 columns / 18 values; id, list, `dateLastActivity` 2025-09-30T16:20:11Z and badges unchanged | Decoded desc is 2,379 chars (was 2,249) and equals line 66 `card.desc` exactly. Apostrophes doubled (`Robert''s`, `doesn''t`) | NEW (desc) | PASS |
| 60, 62, 64 | trello createCard, DD card #211, createCard | `68daca58…`, `683dbef4…` | unchanged | prior §4 | REUSED | PASS (advisory A3) |
| 66 | trello.trello_actions updateCard 2025-09-30T14:04:31Z (**changed**) | `68dbe36f4b2b4fffb7525fde` | 7 columns / 7 values. `data_json` parses as a JSON object; `card.desc` = line 58 desc; `old.desc` unchanged ("…Rules go here once Blake has confirmed what's in the store builds."); id, type, date, actor, board, card unchanged | The update still comes after the 13:26:05Z reply mail and before the 15:41:55Z comment and the 16:20:11Z checklist | NEW (JSON + desc) | PASS |
| 68 | trello commentCard 15:41:55Z | `68dbfa43…` ("adding to rule 1 … rest of the card stands") | unchanged | prior §4 | REUSED | PASS |
| 70 / 72 / 74 / 76 | trello checklist, 2 check items (rule 6, rule 7 changes), addChecklistToCard | `68dc033b…` | unchanged; neither item touches rule 5 | prior §4 | REUSED | PASS |
| 79–107 | gmail threads ×5 + messages ×10 | "store builds for monday" (09:12:44Z) and reply (13:26:05Z, "starting tier check in the build is cpm > 90, not >= 90") | unchanged | prior §4 | REUSED | PASS |
| 110–118 | gcal.gcal_events ×5 | "ZM difficulty tuning" 2025-10-06 (plan field) | unchanged | prior §4 | REUSED | PASS |
| 121 / 123 | github PR comment `#401#c_2` + timeline `#401#ev_7` | 2025-08-25T17:02:28Z | unchanged | prior §4 | REUSED | PASS (advisory A5) |
| 126–344 | linear.linear_comments ×110 | `cmt_*` on ZOM-23 … ZOM-495, including the ZOM-281 `tiers:` note at line 226 | unchanged | prior §4 (line 226 new-key scan in r20: base `/comments` 0 records, complete; unique among the 110 SQL ids) | REUSED | PASS (A1, A4) |

## 5. Lint flags and resolutions

| Flag | Resolution |
|---|---|
| (none) | 0 FAIL / 0 CHECK / 0 INFO. Checks A–C still run below. |

## 6. Checks A–C

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A: Records, references and IDs | **PASS** | The diff changes only text inside lines 58 and 66, with no new keys and no changed ids, actors, boards, lists or cards. Every key keeps its earlier complete collision result (prior report §6 A and its chain), and all of those dependencies are unchanged (manifest, SQL keys). The changed text names ZOM-42 (base `/issues/3485`, exists, Done) and Robert's deck (line 29 presentation, unchanged). |
| B: SQL structure and supported schema rules | **PASS** | All 167 statements parse (lint). Line 58 has 18/18 columns/values and line 66 has 7/7. The E-string escapes decode cleanly, and line 66 `data_json` is a JSON object with `card.desc` equal to the line 58 desc. No generated columns are touched, and no Linear date or `*_json` field changed. Schema comparison stays provisional (A1, A2 carried). |
| C: Dates, relationships and consistency | **PASS** | **Card = action:** desc identical in both rows. No other SQL record restates rule 5: the comment (68) covers rule 1, and the checklist items (72, 74) cover rules 6 and 7. **Starting-tier clause:** a conditional instruction, not a factual claim. The write-ups it names do differ on timing: base ZOM-42 says "assigned after the first 6-7 levels based on CPM, to be defined later" and, in its rule 1, "1st 10 level avg CPM > 90", while the deck (line 37) says "first 10 levels". The clause therefore points at a real, pre-existing difference and asserts nothing false. Blake's reply (line 107) is the only build statement on starting tier (cpm > 90), which matches ZOM-42's "> 90" against ZOM-199's ">= 90". **Promotion/demotion clause:** ZOM-42 words the window as "UP TO THE MOST RECENT 10 attempts" / "the last 10 games played" for promotion and "up to the last 10 games … 50% or lower" for demotion. The deck says "last 10 attempts" for promotion and only "4 losses in a row" for demotion. ZOM-303 (Done) says "win 8 out of last 10 games". No SQL or base record found states a different build behaviour for the game window, so the clause contradicts no record. It also does not conflict with rule 6: Blake's mail and reply flag only ZOM-199's threshold. **Chronology:** no timestamp changed. **Grader-facing text:** none; the new sentences are the card author's instructions to Julia. **Base-data conflicts:** none of SC-1 to SC-3 is touched, and there are no Snowflake or Confluence writes. |

## 7. Findings

No demonstrated defects and no unresolved required checks.

**Advisories (not failures):**
- **D2 (updated for r22), downstream for /prompt, /oe and /rubric:** the card now tells Julia to go by the build for *when* a new player gets the starting tier (and Leonard asks this in line 44). No injected or base record states the build's timing. Blake's mail and reply state only the threshold (cpm > 90), and a bounded base GitHub search (`ZOM-199` 0 hits, complete; `first 10` 2 unrelated hits, complete; `CPM` limit-capped) found no build-side timing statement. The evidence for timing is the deck and ZOM-199's title/description ("first 10 level avg CPM", Done) against ZOM-42's "after the first 6-7 levels … to be defined later". /prompt should decide whether "after the first 10 levels" is the single supported answer before any OE or rubric row requires it.
- **D3 (new in r22), downstream:** "write it the way ZOM-42 words it" for which games promotion and demotion look at. ZOM-42 says "up to the most recent 10 attempts" / "last 10 games played" and also has a demotion rule (win rate 50% or lower over up to the last 10 games, with early exits, and a record reset after each promotion or demotion) that the deck's demotion line omits. /prompt, /oe and /rubric should accept ZOM-42's wording for the window and decide whether the ≤50% demotion rule is expected on the rules tab. Also note that rule 5 opens with "as they work in the store builds today" and then sends this one item to ZOM-42's wording. That is instruction design for /prompt, not a data defect.
- **D1 carried (r20):** ZOM-281 enters scope only through Blake's `tiers:` closing note (line 226). It is Done and a gameplay fix.
- Carried from r17: three instruction layers (card desc → checklist → Leonard's DM reply); the six excluded tickets (ZOM-30, 49, 50, 161, 262, 275); Editor only / Not shipped tickets get a comment; Brian Foster gets edit; possible ZOM-378 "tutorial" ambiguity; Live tab copied as it stands; ZOM-271 out, ZOM-246/250/263/277/315 in.
- A1–A5 carried unchanged (snapshot lacks `linear_comments.sequence` and some gslides columns; DD decoy card #211 in a June 2024 list; PR #401 dead-code reading; injected Trello actions omit base `_id` fields).

## 8. Next action and downstream

Proceed to `/prompt`. Because the SQL changed, every earlier pass that read it is outdated. Rerun `/prompt`, `/hardness`, `/oe` and `/rubric` in that order.

Stage dependencies for reuse: this result depends on SQL sha256 `52c581f4…a43`, synth-cut manifest `da2f4cf0…ac1a`, Linear `data.json` (`/issues`, `/comments`, `/users`), GitHub `data.json` (bounded searches, advisory only), Slack `users.json`, and the reference hashes in §1.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt, then /hardness, /oe and /rubric, since the SQL changed.

Evidence limits: Static review only. No SQL was executed, and live database compatibility and Agent visibility are not certified. The schema snapshot is unverified (A1, A2). Rows byte-identical to revision 20 reuse the prior review's per-row checks under stage-evidence-v1. The edit adds no key, so the earlier complete collision scans still apply.
