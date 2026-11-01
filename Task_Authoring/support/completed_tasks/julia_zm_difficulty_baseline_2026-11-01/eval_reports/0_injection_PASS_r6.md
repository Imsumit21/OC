# /injection: injection data-integrity review

## 1. Scope

| Field | Value |
|---|---|
| Review | `/injection`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode |
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`. reused_evidence: rows byte-identical to revision 12 come from the prior `0_injection.md` (§4 ledger and §6), which carried per-row provenance back through revisions 11, 9 and earlier. See §3. |
| Actual review date | 2026-10-30 (UTC) |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut`, hg4-synth-sep30cut v16. `universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a`, unchanged |
| Input | `Evals/task_inputs/01_Universe_Inject.sql`, 86,342 bytes, 334 `\n`-split fields (333 physical lines + trailing newline), sha256 `a58a5d1e61b32432ff8a931fc5e55f957b11ab54d0e813f9a9bffdcde99958a3` (input revision 14, attached as `01_Universe_Inject (9).sql`; byte-identical to upload `(8)`) |
| Prior SQL compared | revision 12, sha256 `e0df1fbb…a5fa` (upload `(7)`, PASS). Diff: 4 changed lines, same line numbers, no IDs, keys, columns or timestamps changed. Line 22: last Live-tab label "(both VarC versions)" → "(incl. PartyGirl 50HP)". Lines 56 and 64: Trello card desc rule 5 gains "Copy its Live tab as it stands: a monster it hasn't copied yet goes on the tab as not copied yet, don't work numbers out from anywhere else." Line 66: Trello comment gains "written out (ATK on its own doesn't)". |
| Assignment (context only) | Julia Lawson, Product Manager; Product; Engineering Ops; Retrieval; long-horizon |
| References | WORKFLOW.md `ee4cd8e1…cd5d`; Eval 0 `e034019b…3eff`; known_base_issues.md `79b20289…3a7b`; schema/injection.json `31dcb2b4…5151` (unverified snapshot); id_contracts.json `fc4711ef…4682`; ENVIRONMENT.md `4ffb2b5f…e165`; SEARCH.md `cab83c61…a45c`. All unchanged from the prior review (full hashes re-computed). |
| Lint | `hg_injection_lint.py` (injection-lint-v1) on sha256 `a58a5d1e…958a3`: BEGIN, 158 INSERT, 1 UPDATE, COMMIT; 0 FAIL / 0 CHECK / 0 INFO |

Manifest note: the review version, evidence contract, input hash and source provenance above stand in for the injection entry of `input_manifest.json` (`review_version: injection-static-v2`). This portal allows writes under `reports/` only through the report writer.

## 2. Input and authority issues

- The attached file differed from saved revision 12, so it was saved as revision 14 of the injection input before review.
- The SQL is substantive and parses in full. It makes no Confluence or Snowflake writes.
- No git binary is installed on this review machine. The match3d repo was read with a read-only pure-Python pack reader (idx lookup + delta resolution, no writes to `.git`), plus the checked-out working tree (`refs/heads/main` = `0ff577550e`).

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; hash, base manifest, review version | NEW, done |
| Run lint; resolve every flag | NEW: 0 flags. Checks A–C still run below. |
| Inventory every statement and target | NEW for the 4 changed rows. REUSED (prior report §4) for byte-identical rows. Full ledger in §4. |
| Check A: references, IDs, collisions | NEW for the changed rows' references (prefab names, Linear titles). No key added or changed, so REUSED complete collision results. PASS |
| Check B: SQL structure, supported schema rules | NEW whole-file parse via lint; NEW literal parse of changed rows (line 22 grid 12×4; line 64 and 66 JSON `data` parse; quote escaping intact). PASS (advisories carried) |
| Check C: dates, relationships, consistency | NEW for every changed fact: card desc parity (56 vs 64), Live-tab label vs repo prefabs at `09bf633d8b` and `0ff577550e`, comment clarification vs full base Linear issue titles and every SQL row mentioning PartyGirl / not copied / ATK / attack power. PASS |
| Coverage, findings, limits, one verdict | NEW, below |

Reuse basis (stage-evidence-v1): reused rows are byte-identical in the SQL. The base manifest, WORKFLOW, Eval 0, known_base_issues, schema snapshot, id contracts and the fixed clock are unchanged. No key or timestamp changed, so collision and chronology results stay valid. Changed content was re-checked against complete base records, not reused.

## 4. Operation ledger

Lines refer to `01_Universe_Inject.sql` (revision 14). Rows marked REUSED are byte-identical to revision 12 and carry that report's results (which in turn carried revision 11 and earlier results with stated provenance). Repo paths are relative to `Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/root/harmonygames-Games/match3d/`; prefabs are under `Assets/Prefabs/Monsters/`.

| Line(s) | Table / op | Record(s) | Key values checked | Base evidence | Verif. | Result |
|---|---|---|---|---|---|---|
| 5 / 333 | BEGIN / COMMIT | one transaction | all statements commit or roll back together | — | NEW (lint parse) | Structure OK |
| 8 | gdrive.drive_files INSERT | folder `d_96489e1e00a56685625939` "ZM Difficulty" | parent Leonard's root; Julia writer; created 2025-06-13 | prior §4 line 8 | REUSED | PASS |
| 10 | gdrive.drive_files INSERT | doc `f_9ec79682ff351aa466364a` | created 09-29, modified 09-30 | prior §4 line 10 | REUSED | PASS |
| 12 | gdrive.drive_files INSERT (**changed**) | sheet `f_0ba93ae0238d9ed4178212` "ZM monster enrage" | owner Julia; created 2025-08-26T17:40:12Z; **modified 2025-09-08T18:21:40Z** (after created, before the clock) | ID collision prior §4 line 12; History row on line 26 has the same date | REUSED key / NEW time | PASS |
| 14 | gdrive.drive_files INSERT | slides `f_048bf5e69f8e7f1a659a5c` | owner robert@, created 2025-06-16 | prior §4 line 14 | REUSED | PASS |
| 17 | gdocs.docs_documents INSERT | `f_9ec79682…` | non-empty body_text | prior §4 line 17 | REUSED | PASS |
| 20 | gsheets.sheets_spreadsheets INSERT (**changed**) | `f_0ba93ae0…` | 8 columns / 8 values; created 08-26T17:40:12Z, modified **2025-09-08T18:21:40Z** (equal to line 12) | schema: `modified_time` timestamptz, nullable | NEW | PASS |
| 22 | gsheets.sheets_sheets INSERT (**changed in r14**) | sheet 0 "Live" | 7 values; grid 12×4 (parsed). Only change: last row label "Mailman, Mayor2, PartyGirl (both VarC versions)" → "Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP)"; values still "not copied yet"/"not copied yet"/0. The 11 numeric rows are byte-identical to r12 | Pack read of `09bf633d8b` (main at the 09-08 copy) and `0ff577550e` (main HEAD, last commit before the clock): `VarC-Mailman.prefab` 7be35aac, `VarC-Mayor2.prefab` d97aabaf, `VarC-PartyGirl.prefab` 725663ff, `VarC-PartyGirl-50HP.prefab` cb079071 exist at both, identical blobs. Working-tree copies of the two PartyGirl prefabs carry only the legacy single `enragePercentage` property (pre-#401 split), consistent with "not copied yet". Numeric rows: prior r12 check vs `09bf633d8b`/`6eaf71b6e5`/`0ff577550e` | NEW (label) / REUSED (numeric rows) | PASS (A8 resolved) |
| 24 | gsheets sheet 1 "Next pass" | proposals (Leonard: 0.3 levels 1–20, 0.8 levels 21+, show boost) | unchanged; names no specific monster | prior §4 lines 20–26 | REUSED | PASS |
| 26 | gsheets.sheets_sheets INSERT (**changed**) | sheet 2 "History" | grid 5×3. Rows: 06-19 "enrage hp boost switched off" Blake; 08-09 "base enrage 0.6 -> 0.8 (MonsterBase)" Robert; 08-25 "speed and damage split into separate values" match3d#401; **09-08 "Live tab copied from the VarC prefabs in main" Julia** | main first-parent at 2025-09-08T18:21:40Z = `09bf633d8b` (PR #416, committed 2025-09-08T16:14:20Z). It contains the #417 values (`6eaf71b6e5`, 2025-09-06T04:15:53Z), and #420/#421/#416 left them unchanged | NEW | PASS (prior C1 resolved) |
| 29–41 | gslides presentation, 3 pages, 3 elements | `f_048bf5e6…` | IDs absent from base; line 41's stale ZOM-254 "+25%" text is flagged as old by line 50 | prior §4 lines 29–41 | REUSED | PASS (advisory A2) |
| 44–50 | slack.slack_messages INSERT ×4 | Leonard DM 09-30; Brian 09-29; Vincent 09-30; Arthur 09-03 | IDs absent (610,468 messages); authors are channel members. Line 50 (09-03): "values are per monster. julia keeps the numbers" (sheet created 08-26, so still consistent) | prior §4 lines 44–50 | REUSED / NEW consistency | PASS |
| 52 / 53 | slack bot reply + parent UPDATE | `5313e8da…`, `1c181040…` reply_count 2→3 | unchanged | prior §4 lines 52–53 | REUSED | PASS |
| 56 | trello.trello_cards INSERT (**changed in r14**) | `68daca5871dba40417a00383` | Rule 5 gains: "Copy its Live tab as it stands: a monster it hasn't copied yet goes on the tab as not copied yet, don't work numbers out from anywhere else." Key, list, board, other text unchanged. Desc now 2,198 chars | Consistent with line 22 (Live tab has exactly one "not copied yet" row) and with the store-builds pointer (main values unchanged 09-08 → clock). Instruction is Leonard → Julia, a work rule, not solver/grader-facing | NEW | PASS |
| 58 / 60 / 62 | trello createCard, DD card #211, createCard | `68daca58…`, `683dbef4…` | unchanged | prior §4 lines 58–62 | REUSED | PASS (advisory A3) |
| 64 | trello.trello_actions INSERT (**changed in r14**) | `68dbe36f4b2b4fffb7525fde` updateCard 2025-09-30T14:04:31Z | JSON `data` parses; decoded `card.desc` is byte-equal to the decoded line 56 desc (checked programmatically); `old.desc` unchanged | line 56 | NEW | PASS |
| 66 | trello commentCard (**changed in r14**) | `68dbfa4362a051efb5e0ae45` 2025-09-30T15:41:55Z | text now "adding to rule 1: attack power in the title counts too, written out (ATK on its own doesn't). enrage tuning leans on those numbers. rest of the card stands." JSON `data` parses after `''` unescape; time after the line 64 update (14:04:31Z) | Base Linear (`linear/data.json` /issues, full scan): titles with "attack power" written out: ZOM-246, -250, -263, -277, -315; ZOM-271 has only "ATK POWER"/"ATK Power". The clarification names a real distinction and contradicts no injected record (only other match: line 254 ZOM-315 comment, "total attack power") | NEW | PASS |
| 69–97 | gmail threads ×5 + messages ×10 | "store builds for monday" and reply | unchanged. Store builds "cut from main on Sep 26" | prior §4 lines 69–97 | REUSED | PASS |
| 99–108 | gcal.gcal_events ×5 | "ZM difficulty tuning" 2025-10-06 (plan field) | unchanged | prior §4 lines 99–108 | REUSED | PASS |
| 111 / 113 | github PR comment `#401#c_2` + timeline `#401#ev_7` | 2025-08-25T17:02:28Z | unchanged | prior §4 lines 111, 113 | REUSED | PASS (advisory A5) |
| 194, 216, 254 | linear.linear_comments | ZOM-254, ZOM-282 (closing note "this replaces the blunder 2.0 boost from ZOM-254"), ZOM-315 | unchanged | prior §4 lines 194, 216, 254 | REUSED | PASS |
| 115–331 (others) | linear.linear_comments INSERT (109 in total, lint count) | `cmt_*` on ZOM-23 … ZOM-495 | formats, NOT NULL, authors, chronology. The two 09-02 comments (ZOM-449, ZOM-495) do not reference the sheet | prior §4 lines 115–331 | REUSED | PASS (advisories A1, A4) |

## 5. Lint flags and resolutions

| Flag | Resolution |
|---|---|
| (none) | 0 FAIL / 0 CHECK / 0 INFO. Checks A–C still run below. |

## 6. Checks A–C

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A: Records, references and IDs | **PASS** | No key was added or changed; all keys are byte-identical to revision 12, so complete collision results carry over (Gmail 81,404 thread files, Slack 610,468 messages, Linear, Trello, Drive, GitHub per prior ledger). The revised label names real prefabs: `VarC-Mailman`, `VarC-Mayor2`, `VarC-PartyGirl` and `VarC-PartyGirl-50HP` all exist in main at `09bf633d8b` and `0ff577550e` with identical blob IDs. |
| B: SQL structure and supported schema rules | **PASS** | All statements parse. Changed rows keep their column counts (7 sheets_sheets, card and action column lists unchanged). Line 22 grid_json parses (12×4); line 64 and line 66 `data` JSON parse after SQL unescaping; the new apostrophes are doubled (`''`) in both the E-string (56, 64) and plain string (66). No generated columns or Linear dates touched. Provisional advisories A1/A2 carried. |
| C: Dates, relationships and consistency | **PASS** | Decoded line 64 `card.desc` equals the decoded line 56 desc exactly. The new rule 5 sentence matches the Live tab, which holds exactly one "not copied yet" row and 11 numeric rows equal to main at the 09-08 copy and at the clock. "(incl. PartyGirl 50HP)" is accurate: PartyGirl has two VarC prefabs, both present at the copy date, and both still use the legacy single `enragePercentage` property. The line 66 clarification draws a real distinction in base Linear titles (written-out "attack power" on ZOM-246/250/263/277/315; only "ATK POWER" on ZOM-271) and conflicts with no injected record. No timestamps changed; all event times remain before 2025-10-01 07:00 UTC. No grader-facing text in changed rows (rule 5 and the comment are Leonard's instructions to Julia). |

## 7. Findings

No demonstrated defects and no unresolved required checks.

**Resolved from the prior review:**
- **A8 (was advisory, wording):** fixed. The label now reads "Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP)", which no longer implies two VarC versions for Mailman and Mayor2.

**Advisories (not failures):**
- Downstream note for /prompt, /oe and /rubric: rule 5 now tells the reader to copy the Live tab as it stands and list un-copied monsters as "not copied yet". Keep OEs and rubric rows aligned with that (no numeric enrage values for Mailman, Mayor2, PartyGirl, PartyGirl-50HP).
- Downstream note: the line 66 clarification means ZOM-271 (title has "ATK POWER" only) is out of scope under rule 1, while ZOM-246/250/263/277/315 are in if created up to Aug 31 (all are June 2025). Check the OEs and rubric match this.
- A5 carried: PR #401's base text vs line 111's "nothing has called it since june" is a supported dead-code reading.
- A1–A4 carried unchanged: `linear.linear_comments.sequence` absent from the snapshot; gslides `notes`/`table_json`/`ordinal` absent from the snapshot; DD decoy card #211 sits in a June 2024 list; plus minor items from earlier reports.
- Base-data check: none of the listed synth-cut conflicts (SC-1 to SC-3) touch this SQL, and the SQL makes no Snowflake or Confluence writes.

## 8. Next action and downstream

Proceed to `/prompt`. Because the SQL changed, every earlier pass that read it is outdated. Rerun `/prompt`, `/hardness`, `/oe` and `/rubric` in that order.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt, then /hardness, /oe and /rubric, since the SQL changed.

Evidence limits: Static review only. No SQL was executed, and live database compatibility and Agent visibility are not certified. The schema snapshot is unverified (A1, A2). Rows byte-identical to revision 12 reuse the prior review's per-row checks under stage-evidence-v1. The repo was read with a pure-Python pack reader because no git binary is installed; blob IDs at both commits were resolved directly from the pack. The SQL asserts no enrage values for the four un-copied prefabs, so their values are not a pending check here.
