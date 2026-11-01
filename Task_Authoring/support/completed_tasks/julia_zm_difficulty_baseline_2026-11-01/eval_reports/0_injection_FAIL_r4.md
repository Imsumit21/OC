# /injection: injection data-integrity review

## 1. Scope

| Field | Value |
|---|---|
| Review | `/injection`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode |
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`. reused_evidence: rows byte-identical to revision 9 come from the prior `0_injection.md` (sha256 `152735a67202fce6425b5a2b3ed58ed4b709438c1df4368eb3eb02302652b8d2`, §4 ledger and §6). That report itself carried per-row reuse with stated provenance back through revisions 7 and earlier. See §3. |
| Actual review date | 2026-10-30 (15:05 UTC) |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut`, hg4-synth-sep30cut v16. `Evals/references/universes/synthcut/universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a`, unchanged |
| Input | `Evals/task_inputs/01_Universe_Inject.sql`, 85,955 bytes, sha256 `66af19275cf8125320547f848b235ae205179a8b1d8b03aa75680a6f39780dfd` (input revision 11, attached to this /injection message as `01_Universe_Inject (6).sql`) |
| Prior SQL compared | revision 9, sha256 `99b35b05…b168` (upload `(5)`). Diff: 4 changed lines, same line numbers, no IDs changed. Line 22: sheet Live tab drops the Mailman, Mayor2 and "PartyGirl (both VarC versions)" rows. Line 26: History row 2025-09-02 changes from "VarC values set (this tab: Live)" to "Live tab copied from the VarC prefabs in main". Lines 56 and 64: card 80 rule 4 changes "a later ticket's closing note" to "another ticket's closing note". Every other byte is identical. |
| Assignment (context only) | Julia Lawson, Product Manager; Product; Engineering Ops; Retrieval; long-horizon |
| References | WORKFLOW.md `ee4cd8e1…cd5d`; Eval 0 `e034019b…3eff`; known_base_issues.md `79b20289…7a7b`; schema snapshot unchanged (unverified). All unchanged from the prior review. |
| Lint | `hg_injection_lint.py` on sha256 `66af1927…80dfd`: 161 statements (BEGIN, 158 INSERT, 1 UPDATE, COMMIT), 0 FAIL / 0 CHECK / 0 INFO |

Manifest note: the review version, evidence contract, input hash and source provenance above stand in for the injection entry of `input_manifest.json`. This portal allows writes under `reports/` only through the report writer.

## 2. Input and authority issues

- The attached file differed from saved revision 9, so it was saved as revision 11 of the injection input before review.
- The SQL is substantive and parses in full. It makes no Confluence or Snowflake writes.
- Line numbers are physical lines (`grep -n`/`diff`).
- New base evidence corrects an earlier inference. The local match3d git history is a rewrite: base `commit_map` maps PR #401's original head `616d96b045ce…` to local `6a4d8ba57e`. The base PR #401 record says `changed_files: 16`, and its CodeRabbit comment (`/pull_request_comments`, `#401#c_1`) lists 15 prefabs plus `Monster.cs`, including `VarC-Mailman`, `VarC-Mayor2`, `VarC-PartyGirl` and `VarC-PartyGirl-50HP`. The local commit `6a4d8ba57e` lists only 12 files and omits exactly those four, and those four prefabs are cut at 10,240 bytes in both the working tree and the git objects. So the local commit lists cannot show that #401 left them unchanged. The earlier /prompt finding that "no commit ever set split enrage values" on them rests on that artifact.

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; hash, base manifest, review version | NEW, done |
| Run lint; resolve every flag | NEW: 0 flags. Checks A–C still run below. |
| Inventory every statement and target | NEW for the 4 changed rows. REUSED (prior report §4) for byte-identical rows. Full ledger in §4. |
| Check A: references, IDs, collisions | NEW for the changed rows' targets (no new or changed keys). REUSED collision results for every key, since all keys are byte-identical. PASS |
| Check B: SQL structure, supported schema rules | NEW whole-file parse via lint. NEW literal parse of the changed rows: line 22 grid 11×4, line 26 grid 5×3, 7 columns each; the card desc on line 56 is exactly equal to line 64 `card.desc` after unescaping. PASS (advisories carried) |
| Check C: dates, relationships, consistency | NEW for every changed fact, checked against match3d main history (first-parent), the prefab blobs at each relevant commit, base PR #401/#417 records and every SQL row mentioning enrage or Replaced. **FAIL** (C1), with one PENDING item (C2) |
| Coverage, findings, limits, one verdict | NEW, below |

Reuse basis (stage-evidence-v1): reused rows are byte-identical in the SQL. The base manifest, WORKFLOW, Eval 0 and schema hashes and the fixed clock are unchanged. No key changed, so collision results stay valid. Changed content was re-checked against complete base records, not reused.

## 4. Operation ledger

Lines refer to `01_Universe_Inject.sql` (revision 11). Repo paths are relative to `Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/root/harmonygames-Games/match3d/`. Git was read only (`log`, `show`, `merge-base`, `rev-list`) with fsmonitor disabled.

| Line(s) | Table / op | Record(s) | Key values checked | Base evidence | Verif. | Result |
|---|---|---|---|---|---|---|
| 5 / 333 | BEGIN / COMMIT | one transaction | all statements commit or roll back together | — | NEW (lint parse) | Structure OK |
| 8 | gdrive.drive_files INSERT | folder `d_96489e1e00a56685625939` "ZM Difficulty" | parent Leonard's root; Julia writer; created 2025-06-13 | prior §4 line 8 | REUSED | PASS |
| 10 | gdrive.drive_files INSERT | doc `f_9ec79682ff351aa466364a` | created 09-29, modified 09-30 | prior §4 line 10 | REUSED | PASS |
| 12 | gdrive.drive_files INSERT | sheet `f_0ba93ae0238d9ed4178212` "ZM monster enrage" | owner Julia; created 2025-08-26T17:40:12Z; **modified 2025-09-02T19:12:40Z** | prior §4 line 12 (ID); modified time used in C1 | REUSED / NEW compare | PASS as a record; its modified time is evidence for C1 |
| 14 | gdrive.drive_files INSERT | slides `f_048bf5e69f8e7f1a659a5c` | owner robert@, created 2025-06-16 | prior §4 line 14 | REUSED | PASS |
| 17 | gdocs.docs_documents INSERT | `f_9ec79682…` | non-empty body_text | prior §4 line 17 | REUSED | PASS |
| 20 | gsheets.sheets_spreadsheets INSERT | `f_0ba93ae0…` | created 08-26T17:40:12Z, updated 2025-09-02T19:12:40Z (same as line 12) | prior §4 lines 20–26 | REUSED / NEW compare | PASS |
| 22 | gsheets.sheets_sheets INSERT (**changed**) | sheet 0 "Live" | 7 values; grid 11×4. Rows: Bikekid .25/.25, Boxer .5/.4, Cheerleader .6/.4, Chef .5/.5, FootballPlayer .6/.4, Karen .4/.4, Magician ×3 .2/.2, Mayor1 .5/.5, Plumber ×2 .3/.3, "MonsterBase (default for any monster without its own value)" .8/.8; hp 0 | Current blobs: every one of these 11 rows matches the prefab's `enrageSpeedPercentage`/`enrageDamagePercentage` (MonsterBase.prefab 0.8/0.8). The removed monsters are discussed under C1/C2 | NEW | Values PASS against the current main; see C1, C2 |
| 24 | gsheets sheet 1 "Next pass" | proposals | unchanged | prior §4 lines 20–26 | REUSED | PASS |
| 26 | gsheets.sheets_sheets INSERT (**changed**) | sheet 2 "History" | grid 5×3. Rows: 06-19 "enrage hp boost switched off" Blake; 08-09 "base enrage 0.6 -> 0.8 (MonsterBase)" Robert; 08-25 "speed and damage split into separate values" match3d#401; **09-02 "Live tab copied from the VarC prefabs in main" Julia** | main as of 2025-09-02T19:12:40Z = first-parent `52b20ea2eb` (Merge PR #398, 2025-09-02T16:19:15Z). Its VarC values: Bikekid .25/.25, Boxer .6/.6, Cheerleader .6/.6, Karen .6/.6, Magician ×3 .6/.6; Chef, FootballPlayer, Mayor1, Plumber ×2 have no override. The Live-tab values come from `476a02949b` "Monster speeds and damages final adjustment", which first reaches main through first-parent `6eaf71b6e5` "Merge pull request #417" at 2025-09-05T21:15:53-07:00 (base PR #417 merged_at 2025-09-06T04:15:53Z) | NEW | **FAIL (C1)** |
| 29–41 | gslides presentation, 3 pages, 3 elements | `f_048bf5e6…` | IDs absent from base; line 41's stale ZOM-254 "+25%" text is flagged as old by line 50 | prior §4 lines 29–41 | REUSED | PASS (advisory A2) |
| 44–50 | slack.slack_messages INSERT ×4 | Leonard DM 09-30; Brian 09-29; Vincent 09-30; Arthur 09-03 | IDs absent (610,468 messages); authors are channel members. Line 50 (09-03): "values are per monster. julia keeps the numbers" | prior §4 lines 44–50 | REUSED / NEW consistency | PASS |
| 52 / 53 | slack bot reply + parent UPDATE | `5313e8da…`, `1c181040…` reply_count 2→3 | unchanged since revision 9 | prior §4 lines 52–53 | REUSED | PASS |
| 56 | trello.trello_cards INSERT (**changed**) | `68daca5871dba40417a00383` | Rule 4 now: "Replaced: only when another ticket's closing note says it replaces this one". The desc on line 56 is exactly equal to line 64 `card.desc` (string comparison after unescaping) | The only SQL closing note with "replaces" is line 216 (ZOM-282 → ZOM-254). Base Linear has no comments (prior scan) | NEW | PASS. Former advisory A6 is resolved: "another" no longer depends on creation vs close order |
| 58 / 60 / 62 | trello createCard, DD card #211, createCard | `68daca58…`, `683dbef4…` | unchanged | prior §4 lines 58–62 | REUSED | PASS (advisory A3) |
| 64 | trello.trello_actions INSERT (**changed**) | `68dbe36f4b2b4fffb7525fde` updateCard 2025-09-30T14:04:31Z | data_json parses as an object; only rule 4 in `card.desc` changed; ordering unchanged | prior §4 line 64 | NEW content / REUSED key | PASS |
| 66 | trello commentCard | `68dbfa43…` | unchanged | prior §4 line 66 | REUSED | PASS |
| 69–97 | gmail threads ×5 + messages ×10 | "store builds for monday" and reply | unchanged. Store builds "cut from main on Sep 26" (so the #417 values are in them) | prior §4 lines 69–97 | REUSED | PASS |
| 99–108 | gcal.gcal_events ×5 | "ZM difficulty tuning" 2025-10-06 (plan field) | unchanged | prior §4 lines 99–108 | REUSED | PASS |
| 111 / 113 | github PR comment `#401#c_2` + timeline `#401#ev_7` | 2025-08-25T17:02:28Z | unchanged | prior §4 lines 111, 113 | REUSED | PASS (advisory A5) |
| 194, 216, 254 | linear.linear_comments | ZOM-254, ZOM-282 (closing note "this replaces the blunder 2.0 boost from ZOM-254"), ZOM-315 | unchanged | prior §4 lines 194, 216, 254 | REUSED | PASS |
| 115–331 (others) | linear.linear_comments INSERT ×106 | `cmt_*` on ZOM-23 … ZOM-495 | formats, NOT NULL, authors, chronology | prior §4 lines 115–331 | REUSED | PASS (advisories A1, A4) |

## 5. Lint flags and resolutions

| Flag | Resolution |
|---|---|
| (none) | 0 FAIL / 0 CHECK / 0 INFO. Checks A–C still run below. |

## 6. Checks A–C

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A: Records, references and IDs | **PASS** | No key was added or changed, and every key is byte-identical to revision 9, so its complete collision results carry over. Every monster left in the Live tab has a VarC prefab in base. Rule 4's single matching closing note (line 216) targets real tickets ZOM-282 and ZOM-254. |
| B: SQL structure and supported schema rules | **PASS** | 161 statements parse. In the changed rows, column counts match their lists (7, 7, 18, 7); both grid_json values parse (11×4, 5×3); the E-string desc unescapes cleanly and equals the updateCard copy. Provisional advisories A1/A2 carried. |
| C: Dates, relationships and consistency | **FAIL** | C1 (demonstrated): the new History row dates a copy "from the VarC prefabs in main" to 2025-09-02, and the sheet was last modified then (line 12/20 `2025-09-02T19:12:40Z`), but main at that time held different values. Those values reached main on 2025-09-06 via PR #417. C2 (PENDING): the Live tab plus the "copied from main" row implies that Mailman, Mayor2 and PartyGirl fall back to MonsterBase 0.8/0.8, while base PR #401 changed exactly those prefabs and their contents are unreadable. All event timestamps are before 2025-10-01 07:00 UTC. No grader-facing text in the changed rows. |

## 7. Findings

**C1: FAIL (Check C, introduced incompatible fact).** SQL line 26, sheet `f_0ba93ae0238d9ed4178212` History tab, row `["2025-09-02", "Live tab copied from the VarC prefabs in main", "Julia"]`, together with the sheet's modified time `2025-09-02T19:12:40Z` (lines 12, 20).
- Evidence: main at 2025-09-02T19:12:40Z is first-parent `52b20ea2eb` (Merge PR #398, 2025-09-02T16:19:15Z). Its VarC prefabs hold Boxer 0.6/0.6, Cheerleader 0.6/0.6, Karen 0.6/0.6 and Magician ×3 0.6/0.6, and Chef, FootballPlayer, Mayor1 and Plumber ×2 have no own value. The Live tab instead shows Boxer .5/.4, Cheerleader .6/.4, Karen .4/.4, Magician .2/.2, Chef .5/.5, FootballPlayer .6/.4, Mayor1 .5/.5 and Plumber .3/.3. These are the values of `476a02949b`, whose first main-line ancestor is `6eaf71b6e5` "Merge pull request #417" (base PR #417 merged_at 2025-09-06T04:15:53Z). A tab last edited on 09-02 cannot have been copied from main and still show values main only got on 09-06.
- Effect: the record the task names as the enrage authority ("your monster enrage sheet has the numbers") has a dated provenance claim the repo history contradicts. The previous wording ("VarC values set") made no claim about main.
- Smallest fix (either one): (a) move the History row to a date on or after 2025-09-06 (for example `2025-09-08`) and set the sheet's modified/updated time on lines 12 and 20 to the same day or later (still before 2025-09-30). No other row depends on 09-02, and Arthur's 09-03 Slack line ("julia keeps the numbers") still reads fine. Or (b) reword the 09-02 row so it no longer says the values were copied from main.

**C2: PENDING (Check C, material consistency not reconcilable from the bundle).** SQL line 22 now omits Mailman, Mayor2 and PartyGirl. With line 26's "copied from the VarC prefabs in main" and the row label "MonsterBase (default for any monster without its own value)", the sheet asserts those prefabs have no override and run at 0.8/0.8.
- Evidence against confirming this: base PR #401 "Split enrage parameter into separate ones" has `changed_files: 16`, and its CodeRabbit comment lists `VarC-Mailman`, `VarC-Mayor2`, `VarC-PartyGirl` and `VarC-PartyGirl-50HP` among the changed prefabs. All 7 readable VarC prefabs that #401 changed (Bikekid, Boxer, Cheerleader, Karen, Magician ×3) gained their own speed/damage overrides in it. VarC-PartyGirl visibly carries the same old `enragePercentage: 0.6` override that those prefabs had before #401. The four blobs are cut at 10,240 bytes, before any split field, and the local rewrite commit drops them from #401's file list.
- Why PENDING and not FAIL: their actual values cannot be read, so neither 0.8/0.8 nor any specific override is demonstrated. The earlier 0.4/0.4, 0.4/0.6 and 0.4/0.3 rows were equally unverifiable.
- Smallest fix: make the sheet say nothing checkable about these four. For example, add a row such as `["Mailman, Mayor2, PartyGirl (both VarC versions)", "not copied yet", "not copied yet", "0"]`, or narrow the MonsterBase label to "MonsterBase (base prefab)". Then keep the OEs and rubric off enrage values for those four monsters (a /prompt, /oe and /rubric concern).

**Advisories (not failures):**
- A5 carried: PR #401's base text ("fully removes health-enrage functionality") vs line 111's "nothing has called it since june" is a supported dead-code reading, not a contradiction.
- A6 resolved by the "another ticket" wording.
- A7 is superseded by C2. The truncation is now material because of the "copied from main" claim and the #401 file list.
- A1–A4 carried unchanged: `linear.linear_comments.sequence` is absent from the snapshot; gslides `notes`/`table_json`/`ordinal` are absent from the snapshot; DD decoy card #211 sits in a June 2024 list; plus the minor items listed in earlier reports.
- Base-data check: none of the listed synth-cut conflicts (SC-1 to SC-3) touch this SQL, and the SQL makes no Snowflake or Confluence writes.

## 8. Next action and downstream

Fix C1 (date or wording of the History row, with the sheet's modified time if the date moves) and C2 (stop the sheet implying values for Mailman, Mayor2 and PartyGirl), then send `/injection` again. Because the SQL changed, every earlier pass that read it is outdated. After /injection passes, rerun `/prompt`, `/hardness`, `/oe` and `/rubric` in order.

### FINAL VERDICT: FAIL

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: PARTIAL

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Correct SQL line 26 (date it 2025-09-06 or later and move lines 12/20 modified times to match, or drop "copied from main"). Make line 22 stop implying 0.8/0.8 for Mailman, Mayor2 and PartyGirl. Then send /injection again.

Evidence limits: Static review only. No SQL was executed, and live database compatibility is not certified. The schema snapshot is unverified (A1, A2). C2 stays PENDING because the VarC-Mailman, VarC-Mayor2, VarC-PartyGirl and VarC-PartyGirl-50HP blobs are cut at 10,240 bytes in both the working tree and the git objects. Rows byte-identical to revision 9 reuse the prior review's per-row checks under stage-evidence-v1, including Gmail collision coverage over 81,404 thread files and Slack coverage over 610,468 messages.
