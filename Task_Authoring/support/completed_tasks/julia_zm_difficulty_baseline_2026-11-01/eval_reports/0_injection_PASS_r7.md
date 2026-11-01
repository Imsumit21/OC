# /injection: injection data-integrity review

## 1. Scope

| Field | Value |
|---|---|
| Review | `/injection`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode |
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`. reused_evidence: rows byte-identical to revision 14 keep the prior `0_injection.md` results (§4 ledger and §6), which carried per-row provenance back through revisions 12, 11, 9 and earlier. See §3. |
| Actual review date | 2026-10-30 (UTC) |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut`, hg4-synth-sep30cut v16. `universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a`, unchanged |
| Input | `Evals/task_inputs/01_Universe_Inject.sql`, 88,468 bytes, 343 physical lines, sha256 `10c1ee9238d42bf41259cdb6afdeb728f93246abd2ab65f56275d75b4cf3ce18` (input revision 17, attached as `01_Universe_Inject (10).sql`) |
| Prior SQL compared | revision 14, sha256 `a58a5d1e…958a3` (upload `(9)`, PASS). Diff: header comment count 158 → 163 INSERT; line 44 (Leonard DM parent) reply_count 0→1, reply_users_count 0→1, latest_reply NULL→`1759262838.442871`; **new** line 50 (Slack thread reply); line 58 (Trello card) `dateLastActivity` 15:41:55Z → 16:20:11Z and badge `checkItems` 0→2; **new** lines 70–76 (Trello checklist, 2 check items, addChecklistToCard action). Every other row is byte-identical (verified by range diff: old 1–49 = new 1–49 except lines 3 and 44; old 50–66 = new 52–68 except the card; old 67–333 = new 77–343). |
| Assignment (context only) | Julia Lawson, Product Manager; Product; Engineering Ops; Retrieval; long-horizon |
| References | WORKFLOW.md `ee4cd8e1…cd5d`; Eval 0 `e034019b…3eff`; known_base_issues.md `79b20289…3a7b`; schema/injection.json `31dcb2b4…5151` (unverified snapshot); id_contracts.json `fc4711ef…4682`; ENVIRONMENT.md `4ffb2b5f…e165`; SEARCH.md `cab83c61…a45c`. All unchanged from the prior review (re-hashed). |
| Lint | `hg_injection_lint.py` (injection-lint-v1) on sha256 `10c1ee92…ce18`: BEGIN, 163 INSERT, 1 UPDATE, COMMIT; 0 FAIL / 0 CHECK / 0 INFO |

Manifest note: the review version, evidence contract, input hash and source provenance above stand in for the injection entry of `input_manifest.json` (`review_version: injection-static-v2`). This portal allows writes under `reports/` only through the report writer.

## 2. Input and authority issues

- The attached file differed from saved revision 14, so it was saved as revision 17 of the injection input before review.
- The SQL is substantive and parses in full. It makes no Confluence or Snowflake writes.
- Line numbers below are physical (`\n`) lines of the VALUES row for each statement. Some unchanged Gmail bodies contain bare `\r`, so text-mode readers that translate newlines count more lines; this changes nothing in the data.

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; hash, base manifest, review version | NEW, done |
| Run lint; resolve every flag | NEW: 0 flags. Checks A–C still run below. |
| Inventory every statement and target | NEW for the 6 changed/new rows and the header. REUSED (prior report §4) for byte-identical rows, line numbers remapped. Full ledger in §4. |
| Check A: references, IDs, collisions | NEW for 5 new keys (Slack message, Trello checklist, 2 check items, 1 action) with complete scans, plus actor, parent, channel, card and Linear references. Unchanged keys: REUSED complete results. PASS |
| Check B: SQL structure, supported schema rules | NEW whole-file parse via lint; NEW column/value counts and JSON parse for changed/new rows against the schema snapshot. PASS |
| Check C: dates, relationships, consistency | NEW for every changed fact: thread counters, timestamps vs ID prefixes and clock, card badge vs checklist, card dateLastActivity vs latest action, the six excluded tickets vs base Linear, checklist changes vs card rules and every other SQL record. PASS |
| Coverage, findings, limits, one verdict | NEW, below |

Reuse basis (stage-evidence-v1): reused rows are byte-identical in the SQL. The base manifest, WORKFLOW, Eval 0, known_base_issues, schema snapshot, id contracts and the fixed clock are unchanged. The new rows add keys but change no existing key, so earlier collision results stay valid; the new keys were scanned fresh, including against the other proposed rows.

## 4. Operation ledger

Lines refer to `01_Universe_Inject.sql` (revision 17). REUSED rows are byte-identical to revision 14 and keep that report's results (old line → new line shown where it moved).

| Line(s) | Table / op | Record(s) | Key values checked | Base evidence | Verif. | Result |
|---|---|---|---|---|---|---|
| 3 | comment (**changed**) | header | "163 INSERT (one row each), 1 UPDATE" | `grep` count: 163 INSERT, 1 UPDATE; lint agrees | NEW | PASS (accurate; comments are not data) |
| 5 / 343 | BEGIN / COMMIT | one transaction | all statements commit or roll back together | — | NEW (lint parse) | Structure OK |
| 8–14 | gdrive.drive_files ×4 | folder "ZM Difficulty", agenda doc, enrage sheet, tiers deck | unchanged | prior §4 lines 8–14 | REUSED | PASS |
| 17 | gdocs.docs_documents | `f_9ec79682…` | non-empty body_text | prior §4 line 17 | REUSED | PASS |
| 20–26 | gsheets spreadsheet + 3 sheets (Live, Next pass, History) | `f_0ba93ae0…` | unchanged | prior §4 lines 20–26 | REUSED | PASS |
| 29–41 | gslides presentation, 3 pages, 3 elements | `f_048bf5e6…` | unchanged | prior §4 lines 29–41 | REUSED | PASS (advisory A2) |
| 44 | slack.slack_messages INSERT (**changed**) | parent `6f77386571537f0bd88c959bdc216f94`, Leonard (EMPLOYEE_0038) in DM `D05HB64NMQU`, 2025-09-30T19:48:26Z | reply_count 1, reply_users_count 1, latest_reply `1759262838.442871`. Text unchanged | Exactly one reply in the SQL (line 50), by the same single author; latest_reply equals its ts. Key, text and time REUSED (prior §4 line 44) | NEW (counters) | PASS |
| 46, 48, 52 | slack.slack_messages ×3 | Brian 09-29, Vincent 09-30, Arthur 09-03 | unchanged | prior §4 lines 46–50 | REUSED | PASS |
| 50 | slack.slack_messages INSERT (**new**) | `33c941fae57ba8d1e23bc1dff9ce3e2c`, ts `1759262838.442871`, DM `D05HB64NMQU`, author EMPLOYEE_0038 (Leonard) | thread_parent_id = parent id, thread_ts_legacy = parent ts (same convention as the line 54 bot reply); reply_count 0; created_at `2025-09-30T20:07:18.442871Z` = ts; 18 columns / 18 values; `metadata_json` `'{}'`; JSON arrays `'[]'`; no `text_fts` | `lookup` over all 4,840 Slack message files, 610,468 records: id absent (scan_complete). No `D05HB64NMQU/2025-09.json` in base, so no ts clash in the channel. `channels.json`: `D05HB64NMQU` members include EMPLOYEE_0038 (same channel and author as the parent, REUSED membership result). Text names ZOM-30, 49, 50, 161, 262, 275 as analytics/tutorial tickets: base Linear (`/issues`, 3,687 records, complete) confirms all six (see §6 C) | NEW | PASS |
| 54 / 55 | slack bot reply + parent UPDATE | `5313e8da…`, `1c181040…` reply_count 2→3 | unchanged (old 52/53) | prior §4 lines 52–53 | REUSED | PASS |
| 58 | trello.trello_cards INSERT (**changed**) | `68daca5871dba40417a00383` | Only changes: `dateLastActivity` `2025-09-30T16:20:11Z` (was 15:41:55Z) and badges `checkItems` 2 (was 0), `checkItemsChecked` 0. Desc byte-identical. badges_json parses | Latest action on the card is now the line 76 addChecklistToCard at 16:20:11Z (others: createCard 09-29 18:05:12Z, updateCard 09-30 14:04:31Z, commentCard 15:41:55Z). Two check items, both `incomplete`, matches 2 / 0 | NEW | PASS |
| 60, 62, 64 | trello createCard, DD card #211, createCard | `68daca58…`, `683dbef4…` | unchanged (old 58/60/62) | prior §4 | REUSED | PASS (advisory A3) |
| 66 | trello updateCard 2025-09-30T14:04:31Z | `68dbe36f…` | unchanged (old 64); decoded `card.desc` still equals line 58 desc (desc not changed) | prior §4 line 64 | REUSED | PASS |
| 68 | trello commentCard 2025-09-30T15:41:55Z | `68dbfa43…` | unchanged (old 66) | prior §4 line 66 | REUSED | PASS |
| 70 | trello.trello_checklists INSERT (**new**) | `68dc033bf7d24e86b8a9cc67` "Before Monday" on card `68daca58…`, board `6851a656…`, pos 16384.0 | 5 columns / 5 values; NOT NULL id, name, idCard, idBoard all set; card and board created earlier in the SQL / base | `trello/data.json` `/checklists` (54 records, complete): id absent, no existing checklist on this card. Also absent from `/cards` (803). Base pos convention 16384.0 matches | NEW | PASS |
| 72 / 74 | trello.trello_check_items INSERT ×2 (**new**) | `68dc033ba50fbef6a9b12b19` "rule 6 change: …", `68dc033b1200a66f890affc6` "rule 7 change: Brian gets edit as well …" | 7 columns / 7 values; state `incomplete` (base values: incomplete 119, complete 42); idChecklist = line 70; pos 16384 / 32768; due and idMember NULL (nullable) | `/check_items` (161 records, complete): both ids absent; also absent from `/cards` | NEW | PASS |
| 76 | trello.trello_actions INSERT (**new**) | `68dc033b328def4251f2a731` addChecklistToCard 2025-09-30T16:20:11Z by `PERSON_6094_TRELLO_USER_ID` | 7 columns / 7 values; data_json parses as an object with board, card, checklist (id and name equal lines 58/70) | `/actions` (5,252 records, complete): id absent. `/members`: PERSON_6094 = Leonard Hayes, the same creator as the card's other actions. Base has 26 addChecklistToCard actions with the same board/card/checklist shape (base also carries `_id`, as with the earlier injected actions; advisory only) | NEW | PASS |
| 79–107 | gmail threads ×5 + messages ×10 | "store builds for monday" and reply | unchanged (old 69–97) | prior §4 | REUSED | PASS |
| 110–118 | gcal.gcal_events ×5 | "ZM difficulty tuning" 2025-10-06 (plan field); attendees Leonard, Julia, Robert, Arthur Blake, Brian Foster | unchanged (old 99–108) | prior §4 | REUSED | PASS |
| 121 / 123 | github PR comment `#401#c_2` + timeline `#401#ev_7` | 2025-08-25T17:02:28Z | unchanged (old 111/113) | prior §4 | REUSED | PASS (advisory A5) |
| 126–342 | linear.linear_comments ×109 | `cmt_*` on ZOM-23 … ZOM-495, incl. ZOM-254 / ZOM-282 / ZOM-315 (old 194/216/254 → 204/226/264) | unchanged (old 115–331) | prior §4 | REUSED | PASS (advisories A1, A4) |

## 5. Lint flags and resolutions

| Flag | Resolution |
|---|---|
| (none) | 0 FAIL / 0 CHECK / 0 INFO. Checks A–C still run below. |

## 6. Checks A–C

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A: Records, references and IDs | **PASS** | Five new keys, all absent from complete base scans: Slack message `33c941fa…` (610,468 messages, 4,840 files), Trello checklist `68dc033bf7…` (54 checklists), check items `68dc033ba5…` and `68dc033b12…` (161 check items), action `68dc033b32…` (5,252 actions); the four Trello ids are also absent from `/cards` (803) and distinct from each other and from every other id in the SQL. Trello ids follow the base ObjectId form: their first 8 hex `68dc033b` = 2025-09-30T16:20:11Z, equal to the action date. References resolve: EMPLOYEE_0038 (Leonard) in DM `D05HB64NMQU`; thread parent `6f773865…` (line 44); card `68daca58…` and board `6851a656…`; checklist parent line 70; Trello creator PERSON_6094 = Leonard Hayes. "Brian" in line 74 resolves to Brian Foster, the only Brian on the tuning invite (lines 110–118) and the store builds mail. No new accounts. Unchanged keys keep their earlier complete collision results. |
| B: SQL structure and supported schema rules | **PASS** | All statements parse (lint). New and changed rows match the snapshot's column lists: slack_messages 18/18 (no `text_fts`, `metadata_json` `'{}'`, arrays `'[]'`), trello_checklists 5/5, trello_check_items 7/7, trello_actions 7/7 (`data_json` parses as an object), trello_cards unchanged column list (badges_json parses as an object). NOT NULL columns are set in every new row. Apostrophes are doubled (`don''t`, `isn''t`, `he''ll`). No Linear dates or generated columns touched. Provisional advisories A1/A2 carried. |
| C: Dates, relationships and consistency | **PASS** | **Chronology:** reply 2025-09-30T20:07:18Z follows its parent (19:48:26Z); checklist action 16:20:11Z follows the desc update (14:04:31Z) and comment (15:41:55Z); card dateLastActivity equals the latest card action; everything is before 2025-10-01 07:00 UTC. **Thread counters:** parent reply_count 1 / reply_users_count 1 / latest_reply = the one reply's ts. **Card badges:** checkItems 2, checked 0 = two `incomplete` items. **Six excluded tickets (line 50):** all exist in base Linear and were created before Aug 31, so they really are inside rule 1's title scope. Each matches the reply's description: ZOM-30 "Need to track average blunder … analytics" (label Analytics), ZOM-49 "Add Blunder Count by Level to Analytics", ZOM-50 "Track player skill tier in the left_level event", ZOM-161 "Add difficulty tier assignment for left level event" (label Analytics), ZOM-262 "Tutorial for Blunder Locked User", ZOM-275 "Update FTUE message to reflect Blunder mechanic 2.0 changes". Their SQL comments (one routine closing note each) don't contradict this. **Checklist changes (lines 72/74):** rule 6 and rule 7 changes come after the card text and Leonard's "rest of the card stands" comment (15:41:55Z), and are labelled as changes. No later record restates the old rules: the 19:48 DM points to the card, which now carries the checklist. This is a supported later correction, not a contradiction. **Grader-facing text:** none; the reply and check items are Leonard's instructions to Julia. |

## 7. Findings

No demonstrated defects and no unresolved required checks.

**Advisories (not failures):**
- **Downstream note for /prompt, /oe and /rubric (new in r17):** the task's instructions now come in three layers: card desc → checklist (16:20) → Leonard's DM reply (20:07). Keep OEs and rubric rows in step with all three:
  - The six tickets ZOM-30, 49, 50, 161, 262 and 275 are left off the register.
  - Editor only and Not shipped tickets now get a comment saying the change isn't in the store builds. The card's "Every other ticket stays as it is" no longer covers them; ZOM-42 still stays as it is.
  - Brian Foster gets edit on the register as well as Robert.
  - Julia's reply lists the keys of the Not shipped and Editor only tickets, with the ticket total and per-status counts.
- **Possible solver ambiguity (for /prompt to judge):** ZOM-378 "Level 1 is removed and creates tutorial order problems" has "tutorial" in its title. It is in scope through Blake's `tiers:` closing note and is not in Leonard's exclusion list. The list in parentheses is explicit, so the data is consistent, but a solver could wrongly drop ZOM-378 as a "tutorial ticket". ZOM-162 (an editor bug) is also in scope and not excluded.
- Carried from earlier reviews: copy the Live tab as it stands (no numeric enrage values for Mailman, Mayor2, PartyGirl, PartyGirl-50HP). ZOM-271 (only "ATK POWER") is out of scope under the line 68 comment; ZOM-246/250/263/277/315 are in.
- A5 carried: PR #401's base text vs line 121's "nothing has called it since june" is a supported dead-code reading.
- A1–A4 carried unchanged: `linear.linear_comments.sequence` absent from the snapshot; gslides `notes`/`table_json`/`ordinal` absent from the snapshot; DD decoy card #211 sits in a June 2024 list; plus minor items from earlier reports. New: injected Trello action `data` omits the `_id` fields base actions carry (as did earlier injected actions); advisory only.
- Base-data check: none of the listed synth-cut conflicts (SC-1 to SC-3) touch this SQL, and the SQL makes no Snowflake or Confluence writes.

## 8. Next action and downstream

Proceed to `/prompt`. Because the SQL changed, every earlier pass that read it is outdated. Rerun `/prompt`, `/hardness`, `/oe` and `/rubric` in that order.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt, then /hardness, /oe and /rubric, since the SQL changed.

Evidence limits: Static review only. No SQL was executed, and live database compatibility and Agent visibility are not certified. The schema snapshot is unverified (A1, A2). Rows byte-identical to revision 14 reuse the prior review's per-row checks under stage-evidence-v1. New keys were checked with complete scans of the relevant base collections.
