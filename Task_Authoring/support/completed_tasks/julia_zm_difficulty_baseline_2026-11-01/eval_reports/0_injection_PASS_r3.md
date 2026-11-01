# /injection — Injection data-integrity review

## 1. Scope

| Field | Value |
|---|---|
| Review | `/injection`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode |
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`. reused_evidence: rows byte-identical to revision 7, taken from the prior `0_injection.md` (sha256 `2a3bfcf59bfe30437afc81cc3d1b0e52d34427d878ba529adb0dc57fd10b0a1f`, §4 ledger and §6), which carried earlier per-row reuse with the same provenance. See §3. |
| Actual review date | 2026-10-30 (14:20 UTC) |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut`, hg4-synth-sep30cut v16. `Evals/references/universes/synthcut/universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a`, the same as in the prior review |
| Input | `Evals/task_inputs/01_Universe_Inject.sql`, 86,060 bytes, sha256 `99b35b05c5224ea5c7342964e5807613f0a6891550d8d42b6920e9e0a8cfb168` (input revision 9, attached to this /injection message as `01_Universe_Inject (5).sql`) |
| Prior SQL compared | revision 7, sha256 `3242b0a3…e080` (still present as upload `(4)`). Diff: 7 changed lines, same line numbers, no IDs changed: 22 (sheet Live tab), 26 (sheet History tab), 52 (Slack GitHub-bot reply), 56 (Trello card 80 desc, rule 4), 64 (updateCard `card.desc`, rule 4), 111 (GitHub PR #401 comment body), 216 (Linear ZOM-282 closing comment body). Every other byte is identical. |
| Assignment (context only) | Julia Lawson, Product Manager; Product; Engineering Ops; Retrieval; long-horizon |
| References | WORKFLOW.md sha256 `ee4cd8e1…cd5d`; Eval 0 `e034019b…3eff`; scoring.json `c14873e6…e5bc`; schema injection.json `31dcb2b4…5151` (unverified snapshot); known_base_issues.md `79b20289…7a7b`. All unchanged from the prior review. |
| Lint | `hg_injection_lint.py` injection-lint-v1 on sha256 `99b35b05…b168`: 161 statements (BEGIN, 158 INSERT, 1 UPDATE, COMMIT), 0 unparsed. 0 FAIL / 0 CHECK / 0 INFO |

Manifest note: the review version, evidence contract, input hash and source provenance above take the place of the injection entry of `input_manifest.json`. This portal allows writes under `reports/` only through the report writer.

## 2. Input and authority issues

- The attached file differed from saved revision 7, so it was saved as revision 9 of the injection input before review.
- The SQL is substantive and parses in full. No Confluence or Snowflake writes.
- Line numbers below are physical lines (`grep -n`/`diff`). Ten lines contain an embedded CR inside Gmail bodies (unchanged since revision 7), so tools that also split on CR count higher numbers.

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; hash, base manifest, review version | NEW, done |
| Run lint; resolve every flag | NEW: 0 flags. Checks A–C done. |
| Inventory every statement and target | NEW for the 7 changed rows. REUSED (prior report §4) for byte-identical rows. Full ledger in §4. |
| Check A: references, IDs, collisions | NEW for changed rows' actors and targets (no new or changed keys). REUSED collision results for every key (all keys byte-identical). PASS |
| Check B: SQL structure, supported schema rules | NEW whole-file parse via lint, plus literal parse of all 7 changed rows. PASS (advisories carried) |
| Check C: dates, relationships, consistency | NEW for every changed fact against base Linear (ZOM-254, ZOM-280, ZOM-282, ZOM-294, ZOM-295), base GitHub (PR #401, its comment `c_1`, `Monster.cs`, 17 monster prefabs) and every other SQL row that mentions enrage, HP or Replaced. PASS |
| Coverage, findings, limits, one verdict | NEW, below |

Reuse basis (stage-evidence-v1): reused rows are byte-identical in SQL; base manifest, WORKFLOW, Eval 0, scoring and schema hashes and the fixed clock are unchanged. No key changed, so collision results stay valid. Changed content was re-checked against complete base records, not reused.

## 4. Operation ledger

Lines refer to `01_Universe_Inject.sql` (revision 9). Base paths are relative to `Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/` (Linear) or `Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/` (GitHub).

| Line(s) | Table / op | Record(s) | Key values checked | Base evidence | Verif. | Result |
|---|---|---|---|---|---|---|
| 5 / 333 | BEGIN / COMMIT | one transaction | all statements commit or roll back together | — | NEW (lint parse) | Structure OK |
| 8 | gdrive.drive_files INSERT | folder `d_96489e1e00a56685625939` "ZM Difficulty" | parent Leonard's root; Julia writer; created 2025-06-13 | prior §4 line 8 | REUSED | PASS |
| 10 | gdrive.drive_files INSERT | doc `f_9ec79682ff351aa466364a` | created 09-29, modified 09-30 | prior §4 line 10 | REUSED | PASS |
| 12 | gdrive.drive_files INSERT | sheet `f_0ba93ae0238d9ed4178212` "ZM monster enrage" | owner Julia; created 08-26 | prior §4 line 12 | REUSED | PASS |
| 14 | gdrive.drive_files INSERT | slides `f_048bf5e69f8e7f1a659a5c` | owner robert@, created 2025-06-16 | prior §4 line 14 | REUSED | PASS |
| 17 | gdocs.docs_documents INSERT | `f_9ec79682…` | non-empty body_text | prior §4 line 17 | REUSED | PASS |
| 20 | gsheets spreadsheet | `f_0ba93ae0…` | — | prior §4 lines 20–26 | REUSED | PASS |
| 22 | gsheets.sheets_sheets INSERT (**changed**) | sheet 0 "Live" | 7 values; grid_json parses: 14 rows × 4 cols. Header now "enrage speed / enrage damage / enrage hp". Rows: Bikekid .25/.25, Boxer .5/.4, Cheerleader .6/.4, Chef .5/.5, FootballPlayer .6/.4, Karen .4/.4, Magician ×3 .2/.2, Mailman .4/.4, Mayor1 .5/.5, Mayor2 .4/.6, PartyGirl ×2 .4/.3, Plumber ×2 .3/.3, MonsterBase .8/.8; hp 0 everywhere | Prefab files exist for every row: `root/harmonygames-Games/match3d/Assets/Prefabs/Monsters/VarC-*.prefab` (Magician, -20HP, -30HP; PartyGirl, -50HP; Plumber, -80HP; Mayor1; Mayor2; Mailman; Bikekid; Boxer; Cheerleader; Chef; FootballPlayer; Karen) and `MonsterBase.prefab`. Readable `enrageSpeedPercentage`/`enrageDamagePercentage` values match the sheet in all 11 readable rows. Mailman, Mayor2 and both PartyGirl prefabs are cut at 10,240 bytes in the export before any new enrage field, so their values are not readable (A7). | NEW | PASS |
| 24 | gsheets sheet 1 "Next pass" | proposals | unchanged | prior §4 lines 20–26 | REUSED | PASS |
| 26 | gsheets.sheets_sheets INSERT (**changed**) | sheet 2 "History" | grid_json parses: 5 rows × 3 cols. New first row "2025-06-19 enrage hp boost switched off, Blake"; 08-25 row now "speed and damage split into separate values, match3d#401" | ZOM-282 (`/issues/3335`): assignee Arthur Blake, started 2025-06-19T19:49:22Z, "only increases speed and monster attack damage but NOT HP". PR #401 merged 2025-08-25T16:42:14Z, "Split enrage parameter into separate ones". All History dates before the clock. | NEW | PASS |
| 29–41 | gslides presentation, 3 pages, 3 elements | `f_048bf5e6…`, `slide_*`, `el_*` | IDs absent from base; line 41 deck text "+25% walk speed, +25% damage, +25% max HP (ZOM-254…)" is stale ZOM-254 spec, flagged as old by line 50 | prior §4 lines 29–41 | REUSED / NEW consistency | PASS (advisory A2) |
| 44–50 | slack.slack_messages INSERT ×4 | Leonard DM 09-30 19:48:26Z; Brian 09-29 22:31:17Z; Vincent 09-30 16:12Z; Arthur 09-03 15:22:09Z | IDs absent (610,468 messages); authors are channel members. Line 50 ("enrage adds speed and damage only (split since match3d#401), hp doesn't change, and the values are per monster") agrees with new lines 22, 26, 111, 216. Line 46 ("+50% speed and damage for every monster like 282 says") remains stale context, contradicted by line 50, PR #401 and the sheet | prior §4 lines 44–50 | REUSED / NEW consistency | PASS |
| 52 | slack.slack_messages INSERT (**changed**) | `5313e8da22604987e53ba497dc709655`, GitHub bot reply in thread `1c181040…` | 18 columns; attachments_json parses as a list; metadata_json `{}`. Attachment `text` equals line 111 body exactly; attachment `ts` 1756141348 = 2025-08-25T17:02:28Z = line 111 `created_at`; message ts 1756141351.508113 = created_at 17:02:31.508113Z | ID unchanged (prior collision check over 610,468 messages) | NEW content / REUSED key | PASS |
| 53 | slack UPDATE parent | `1c181040…` reply_count 2→3 | unchanged | prior §4 lines 52–53 | REUSED | PASS |
| 56 | trello.trello_cards INSERT (**changed**) | `68daca5871dba40417a00383` "Difficulty baseline (Julia)" | Rule 4 now: "Replaced: only when a later ticket's closing note says it replaces this one. Name that ticket. Nothing else makes a ticket Replaced…". E-string escaping parses; desc equals line 64 `card.desc` (exact string comparison: match) | Only one closing note in the SQL says "replaces" (line 216, ZOM-282 → ZOM-254); base Linear has no comments. ZOM-282 created 2025-06-19 after ZOM-254 created 2025-06-12 | NEW | PASS (advisory A6) |
| 58 | trello.trello_actions INSERT | `68daca5845e48874fb98e25a` createCard 2025-09-29T18:05:12Z | unchanged | prior §4 line 58 | REUSED | PASS |
| 60 / 62 | DD card #211 + createCard | `683dbef4…` | 2025-06-02 | prior §4 lines 60, 62 | REUSED | PASS (advisory A3) |
| 64 | trello.trello_actions INSERT (**changed**) | `68dbe36f4b2b4fffb7525fde` updateCard 2025-09-30T14:04:31Z | data_json parses as an object (7 columns); only `card.desc` changed, to the line 56 text; `old.desc` unchanged; date still after Blake's 13:26:05Z reply and before Leonard's 15:41:55Z comment | prior §4 line 64 (ID, date, ordering) | NEW content / REUSED key | PASS |
| 66 | trello.trello_actions INSERT | `68dbfa4362a051efb5e0ae45` commentCard 2025-09-30T15:41:55Z | unchanged; does not mention rule 4 | prior §4 line 66 | REUSED | PASS |
| 69–97 | gmail threads ×5 + messages ×10 | "store builds for monday" and reply | unchanged; no enrage, HP or Replaced text | prior §4 lines 69–97 | REUSED | PASS |
| 99–108 | gcal.gcal_events ×5 | "ZM difficulty tuning" 2025-10-06 (plan field) | unchanged | prior §4 lines 99–108 | REUSED | PASS |
| 111 | github.github_pr_comments INSERT (**changed**) | `harmonygames-Games/match3d#401#c_2`, Arthur Blake | 6 columns. Body: "this gives enrage speed and damage their own values, they shared one since ZOM-282. also drops the old EnrageHealth method, nothing has called it since june". 2025-08-25T17:02:28Z, after merge 16:42:14Z | PR #401 (`/pull_requests`, scan complete over 2,475): title "Split enrage parameter into separate ones"; comment `c_1` (`/pull_request_comments/581`): "Replaced `enragePercentage` with `enrageSpeedPercentage` and `enrageDamagePercentage`… Removed `EnrageHealth(float)`". Current `Monster.cs` lines 86–88, 612–640: only speed and damage enrage. ZOM-282 Done 2025-06-21 ("NOT HP") | NEW | PASS (advisory A5) |
| 113 | github.github_timeline_events INSERT | `#401#ev_7` commented 2025-08-25T17:02:28Z | equals line 111 time | prior §4 line 113 | REUSED / NEW compare | PASS |
| 194 | linear.linear_comments INSERT | `cmt_9698eebaf0663ba1f7da` on ZOM-254, Vincent Parker, 2025-06-23T09:08:05Z "checked on the dev build, blunder enrages the monsters on the board now" | before ZOM-254 completed_at 09:26:05Z. Still true after ZOM-282 (enrage still adds speed and damage) | prior §4 lines 115–331; base `/issues/3304` | REUSED / NEW consistency | PASS |
| 216 | linear.linear_comments INSERT (**changed**) | `cmt_912bdd42ad5c8d51521f` on ZOM-282, author `usr_cc3e90160f490686` | 9 columns; dates `2025-06-21T01:09:19Z` (base format). Body: "closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the hp part was switched off on the 19th. speed and damage still share one value" | Author = arthur.blake@ (`/users`, scan complete over 41), the ZOM-282 assignee. ZOM-282 (`/issues/3335`): created 06-19T05:23:06Z, started 06-19T19:49:22Z, completed 06-21T01:17:19Z, so the comment comes before completion. ZOM-254 (`/issues/3304`) "Blunder Mechanic 2.0 enrages zombies instead of HP penalty", +25% speed/damage/max HP. ZOM-280 (Canceled 06-18): "just not increase HP… Only speed and damage". PR #401 split on 08-25 matches "still share one value" | NEW | PASS (advisory A6) |
| 254 | linear.linear_comments INSERT | `cmt_98027df98af6fb30b763` on ZOM-315 | unchanged | prior §4 line 254 | REUSED | PASS |
| 115–331 (others) | linear.linear_comments INSERT ×106 | `cmt_*` on ZOM-23 … ZOM-495 | formats, NOT NULL, authors, chronology | prior §4 lines 115–331 | REUSED | PASS (advisories A1, A4) |

## 5. Lint flags and resolutions

| Flag | Resolution |
|---|---|
| (none) | 0 FAIL / 0 CHECK / 0 INFO. Checks A–C still run below. |

## 6. Checks A–C

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A: Records, references and IDs | **PASS** | No key added or changed; every key is byte-identical to revision 7, so its complete collision results carry over. Changed rows' actors resolve: ZOM-282 comment author `usr_cc3e90160f490686` = Arthur Blake (ZOM-282 assignee), PR comment author `EMPLOYEE_0025_GITHUB_USERNAME` = Arthur Blake, as before. Targets ZOM-282, ZOM-254 and PR #401 exist in base (complete scans). Every monster named in the sheet has a VarC prefab in the base repo. |
| B: SQL structure and supported schema rules | **PASS** | 161 statements parse. Changed rows: column counts match their lists (7, 7, 18, 18, 7, 6, 9); both grid_json values parse (14×4, 5×3); Slack attachments_json is a list and metadata_json `{}`; Trello data_json is an object; the E-string desc unescapes cleanly; Linear dates are `YYYY-MM-DDTHH:MM:SSZ`. Provisional advisories A1/A2 carried. |
| C: Dates, relationships and consistency | **PASS** | The new HP story is consistent across the SQL and the base: HP boost switched off 06-19 (History tab, ZOM-282 note; ZOM-282 started 06-19 with "NOT HP"; ZOM-280 cancelled with the same fix) → speed and damage share one value (ZOM-282 note; Brian's stale "+50%… like 282 says") → split on 08-25 (PR #401, History tab, line 111, line 50) → per-monster values (sheet; 11 of 11 readable prefab rows match). The card's new rule 4 has exactly one matching closing note (ZOM-282 → ZOM-254), and ZOM-282 was created after ZOM-254. Card desc = updateCard `card.desc`; Slack bot text = GitHub comment; all timestamps before 2025-10-01 07:00 UTC. No grader-facing text in changed rows. |

## 7. Findings

No failures.

**Advisories (not failures):**
- A5 (new). PR #401's base CodeRabbit text says it "fully removes health-enrage functionality" and draws "Health enrage path removed" inside `SetEnrage`, and the PR body says enraged monsters "retain their base health". The new line 111 says nothing has called `EnrageHealth` since June. The base also says "Removed `EnrageHealth(float)` and all health-enrage references/comments", and ZOM-282 is Done on 06-21 with "NOT HP", so dead-code removal is a supported reading. This is not a demonstrated contradiction. Keep the rubric and OEs off claims about the exact day HP stopped in the build beyond what lines 26/216 state.
- A6 (new, for /prompt). ZOM-282 (created 06-19, done 06-21) replaces ZOM-254, which was created earlier (06-12) but closed later (06-23). "A later ticket" holds by creation date but not by close date. /prompt should check that rule 4 reads unambiguously.
- A7 (new). The export truncates `VarC-Mailman`, `VarC-Mayor2`, `VarC-PartyGirl` and `VarC-PartyGirl-50HP` at 10,240 bytes, so their enrage values (sheet: .4/.4, .4/.6, .4/.3) cannot be checked against code. This is an evidence limit, not a defect. If the Agent can read repo files, it will see the same truncation.
- A1–A4 carried unchanged: `linear.linear_comments.sequence` is not in the snapshot (dropping it is safest); gslides `notes`/`table_json`/`ordinal` columns are absent from the snapshot; DD decoy card #211 sits in a June 2024 list; minor items listed in the prior report.
- Base-data check: none of the listed synth-cut conflicts (SC-1 to SC-3) touch this SQL; no Snowflake or Confluence writes.

## 8. Next action and downstream

Static injection checks are complete. Because the SQL changed, every earlier pass that read it is outdated: rerun `/prompt`, then `/hardness`, `/oe` and `/rubric` in order.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Run /prompt on this SQL revision, then /hardness, /oe and /rubric.

Evidence limits: Static review only. No SQL was executed, and live database compatibility is not certified. The schema snapshot is unverified (advisories A1, A2). Four prefab blobs are truncated in the export (A7). Rows byte-identical to revision 7 reuse the prior review's per-row checks under stage-evidence-v1, including its Gmail collision coverage over 81,404 thread files and its Slack coverage over 610,468 messages.
