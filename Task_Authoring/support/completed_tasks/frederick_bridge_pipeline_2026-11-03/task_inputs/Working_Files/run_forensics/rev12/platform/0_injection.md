# Injection Data-Integrity Review (Eval 0)

Review version: `injection-static-v2`
Evidence contract: `stage-evidence-v1`
Review time: 2026-11-03T01:17Z (actual)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Mode: chat review, attempt 6ae4e299a13034b7eb8305f8 (static, SQL not executed)

## 1. Scope and inputs

| Input | Value |
|---|---|
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` (input revision 26, from chat attachment `01_Universe_Inject (15).sql`), 167,306 bytes, SHA-256 `69db98aed17f40cbcbbfad417b7eb21a118dffdbb63b798cf8322ddac226182b`. Replaces `01_Universe_Inject (14).sql` (SHA `75b6cb2a…0fee`, last reviewed PASS/COMPLETE), so that report no longer applies. |
| Diff from v14 | 162 statements vs 173; 155 byte-identical to v14. Changed/new (7): line 3 header comment ("147 INSERT, 13 UPDATE", matches the parse); line 83 #executives post `4921f321…` back to a standalone message (as in v13); line 106 new group-DM post `c5657466…` ("Paul's out…"); lines 108/110 Arthur/Leonard Slack messages turned into their own thread (parent `3cddf83c…`, reply `301ad67f…`), re-worded; lines 309/311 two new ZOM-567 comments (NCsoft, Brightwater); line 313 Dentsu comment `sequence` 2 → 4. Removed (18): #executives reply `7fe55f30…` (v14 line 85); UPDATE of base Slack parent `c891232a…` (v14 line 111); Karthic's and Arthur's Bridge Round emails, 8 rows across four mailboxes, and their 4 thread-snippet UPDATEs (v14 lines 171–190). |
| Assignment (context only) | Frederick Stone, Co-founder; not graded here |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Eval | `Evals/0_Injection_Quality_Eval.md` `e034019b8ec450437509a73dd3bae2d303b57561b0f67fcc1e5d19266f663eff` |
| Shared workflow | WORKFLOW `ee4cd8e1…cd5d` via `hg_reference.py guide injection --services slack linear gmail --tables slack.slack_messages linear.linear_comments` |
| Schema snapshot | `references/schema/injection.json` `31dcb2b43feca8e5…` (unverified, provisional) |
| ID contracts | `references/schema/id_contracts.json` `fc4711ef07667333…` |
| Lint | `hg_injection_lint.py` `a8226e2a69425355…`, version `injection-lint-v1` |
| Roster / ACL | roster.json `3f2174513f639e37…`, acl.md `e9bca2b35f98d5ef…` (identity checks only) |
| Known data issues | `guidelines/known_data_issues.md` `29b89d856c454124…` (SC-10 handled in the sheet by line 31, unchanged) |

Input/authority issues: none for this stage. SQL comments are evidence of intent only; none addresses a grader or mentions tool calls, pass rate or gates.

## 2. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, base manifest, review version | NEW, done (saved as input revision 26 before review) |
| Run lint; resolve every flag | NEW, done (0 FAIL, 0 CHECK, 0 INFO) |
| Inventory every statement and affected record | NEW, done: 162 statements (BEGIN, 147 INSERT, 13 UPDATE, COMMIT), ledger §5; each matched to v14 by exact content; removed v14 statements listed |
| Check A | NEW for the 7 changed/new statements and for dangling references from the 18 removed ones; REUSED for 155 byte-identical rows (§11): PASS |
| Check B | NEW: independent column/value count over all 147 INSERTs (0 mismatches), duplicate-key check, changed-row schema comparison; REUSED for byte-identical rows: PASS (provisional snapshot advisory) |
| Check C | NEW for changed/new statements and the base/injected records they relate to; REUSED for byte-identical rows: PASS |
| Report coverage, findings, limits, one verdict | NEW, done |

## 3. Lint result

`hg_injection_lint.py` on SHA `69db98ae…182b`, universe synthcut, clock 2025-10-01T07:00Z. Base files loaded: contacts, slack users, trello, gmail users, linear, confluence. Rows: 147 INSERT, 13 UPDATE (slack_messages 14 insert + 1 update; gmail_threads 31 insert + 9 update; gmail_messages 40 insert; gcal_events 14; linear_issues 1; linear_comments 4; contacts 4; plus Drive/Docs/Sheets/Slides/Trello rows unchanged).

Flags: **none** (FAIL 0, CHECK 0, INFO 0). Checks A–C were still run in full.

## 4. Source coverage (new checks in this run)

| Check | Source / pointer | Coverage | Result |
|---|---|---|---|
| New/changed Slack ids `c5657466…`, `3cddf83c…`, `301ad67f…` | slack `messages/*/*.json` (`lookup --key id`, `--no-cache`) | 4,840 files, 610,468 records, scan complete, 0 errors | 0 base matches; each id once among the SQL's INSERT keys |
| Slack ts `1759251900.863415`, `1759274400.518306`, `1759276080.094417` | same (`lookup --key ts`) | complete | 0 base matches. ts → UTC: 17:05:00Z, 23:20:00Z, 23:48:00Z on 2025-09-30, each equal to the row's `created_at` |
| Channels | slack `channels.json` /525, /108 | 948 records, complete | `D05S58U4SAK`: group DM (`is_im` true), members `EMPLOYEE_0008`, `EMPLOYEE_0038` (Leonard), `PERSON_6089`, `U04UP2L1RUY`, `U05SFR4E7RR`, not archived; Leonard already posts there at lines 102/104. `C0880U9751A` = `zombie-match3d`, private, members include `EMPLOYEE_0025` (Arthur) and `EMPLOYEE_0038` (Leonard) |
| Base thread shape | slack `messages/C0880U9751A/2025-09.json` (473 records) | full file | Base parents carry `thread_ts` = own ts, `reply_count`/`reply_users_count`/`latest_reply` filled; replies carry `thread_ts` = parent ts and `reply_count` 0; standalone posts `thread_ts` null. Line 108 (parent: own ts, 1/1, latest = line 110 ts), line 110 (reply: parent ts, 0/0) and lines 83/106 (standalone: NULL, 0/0) match |
| Former parent `c891232a…` (no longer updated) | same file /463 | full record + text search of the file | Base: "I just released 0.3.49 on IOS", `reply_count` 0, `thread_ts` null. Nothing in v15 references `c891232a…` (grep), so the base row stays self-consistent |
| Removed records | SQL text | full | `7fe55f30…`, `<CAz_RUxJ…>` and `<CAU8zEO-…>` appear nowhere in v15; the four base Bridge Round threads get no UPDATE, so their snippets stay at the base latest message |
| Linear comment ids `lc_4369758f577612cdb63b3457`, `lc_5e2ff140afff06e3a78e2fe1` | linear `data.json` (`/comments` exact check; text search of the whole file) | `/comments` holds 0 records (base has no Linear comments); text search complete | 0 matches; the four `lc_` ids in the SQL are distinct |
| ZOM-567, author | linear `data.json` `/issues` (3,687 records), `/users/35` | complete | ZOM-567 absent from base (highest ZOM number 566); created at line 305 before its comments. `usr_cc3e90160f490686` = arthur.blake@harmonygames.co |
| NCsoft "Sep 19 call" (line 309) | slack search "NCsoft"/"NC soft" (complete); gcal search "NCsoft" (complete) | full | Base supports it: Leonard 2025-09-17 18:40Z in #executives "Friday second round of NCSOFT, Monday … t-accelerate"; `EMPLOYEE_0008` 2025-09-19 14:13Z "Confirming I'll skip the NCSoft demo"; `EMPLOYEE_0016` 2025-09-19 16:02Z "just finished a round 2 with NC Soft". First call Sep 10 (gcal events /5522 etc.). Anel Ceman is the NCsoft contact in the base pipeline sheet (gsheets `data.json`, one line match; also the SQL's line-31 sheet row) |
| Brightwater / Ilse Marrow (line 311) | SQL lines 207–245, 276–282, 318; gmail search "Brightwater" (81,404 files, complete, 0 base matches) | full | Ilse Marrow exists only as injected: contact (line 318, Principal, Brightwater Games Fund, `PERSON_9904_EMAIL`), Sep 25 meeting, Leonard's follow-up and her 09-26 15:05Z reply. "Added Sep 26" fits after the Sep 25 meeting |
| Play internal-test links in base mail | gmail search "apps/internaltest" | 81,404 files, complete | 28 hits in 7 threads: 2023–2024 threads and the 09-22 Bridge Round message to Karthic. No base email sends NCsoft, Brightwater or Dentsu a Play link or reports Android working, so nothing contradicts "nobody on it has android yet" |
| NCsoft in base mail | gmail search "NCsoft" | stopped at its 200-match limit after 41,947 files (incomplete) | Hits are the 2025 strategic-investment thread and newsletters; none about builds. Supplementary only; the complete "apps/internaltest" scan covers the material question |
| Cache note | — | — | Two cached lookups returned "Source, manifest or helper changed during operation"; reruns with `--no-cache` and direct reads completed. No evidence relies on the failed calls |

## 5. Operation ledger

Every statement in execution order (current SQL line numbers; for INSERTs the VALUES line). Changed/new rows were verified fresh (§4, §6–§8). Byte-identical rows reuse the v14 report's ledger (which chains to v13–v10), with their v14 line. The whole script was re-parsed in this run.

| SQL line | Table | Op | Record / target | Change vs v14 | Verification | Result |
|---|---|---|---|---|---|---|
| 5 | — | BEGIN | `—` | unchanged (byte-identical to v14 line 5) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 8 | gdrive.drive_files | INSERT | `f_8d2c47a91e05b3f6d7c418` | unchanged (byte-identical to v14 line 8) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 10 | gdrive.drive_files | INSERT | `f_3b9e61c04d7a52e8f1a6c2` | unchanged (byte-identical to v14 line 10) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 12 | gdrive.drive_files | INSERT | `d_5e8a1c3f9b07d2e64a1b93` | unchanged (byte-identical to v14 line 12) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 14 | gdrive.drive_files | INSERT | `f_c61a0e93b7d24f58a2e917` | unchanged (byte-identical to v14 line 14) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 16 | gdrive.drive_files | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 16) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 18 | gdrive.drive_files | INSERT | `f_6e1d93a0c4b72f85d39a0e` | unchanged (byte-identical to v14 line 18) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 21 | gdocs.docs_documents | INSERT | `f_8d2c47a91e05b3f6d7c418` | unchanged (byte-identical to v14 line 21) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 23 | gdocs.docs_documents | INSERT | `f_3b9e61c04d7a52e8f1a6c2` | unchanged (byte-identical to v14 line 23) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 25 | gdocs.docs_documents | INSERT | `f_c61a0e93b7d24f58a2e917` | unchanged (byte-identical to v14 line 25) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 28 | gsheets.sheets_spreadsheets | INSERT | `f_6e1d93a0c4b72f85d39a0e` | unchanged (byte-identical to v14 line 28) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 30 | gsheets.sheets_sheets | INSERT | `f_6e1d93a0c4b72f85d39a0e` | unchanged (byte-identical to v14 line 30) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 31 | gsheets.sheets_sheets | UPDATE | `spreadsheet_id = 'f_48247af79428823c3cac92' AND sheet_id = 0` | unchanged (byte-identical to v14 line 31) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 34 | gslides.slides_presentations | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 34) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 36 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 36) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 38 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 38) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 40 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 40) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 42 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 42) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 44 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 44) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 46 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 46) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 48 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 48) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 50 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 50) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 52 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 52) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 54 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 54) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 56 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 56) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 58 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 58) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 60 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 60) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 62 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 62) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 64 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 64) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 66 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 66) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 68 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 68) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 70 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 70) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 72 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 72) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 74 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 74) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 76 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 76) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 78 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 78) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 80 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v14 line 80) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 83 | slack.slack_messages | INSERT | `4921f321db5d08f936aac24a6a1d2af8` | **CHANGED** vs v14: standalone again (`thread_ts_legacy` NULL, `reply_count`/`reply_users_count` 0, `latest_reply` NULL); byte-identical to v13 line 83 | NEW (base standalone shape: `thread_ts` null, counts 0); id/ts uniqueness REUSED (v14 report §4, complete Slack scan) | PASS |
| 85 | slack.slack_messages | INSERT | `7fef94264090696760180223fc8265e7` | unchanged (byte-identical to v14 line 87) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 87 | slack.slack_messages | INSERT | `20924cc7f5176991d8a97a8eafb291d0` | unchanged (byte-identical to v14 line 89) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 89 | slack.slack_messages | INSERT | `19e1e65d5952f075e8492867c6bcd472` | unchanged (byte-identical to v14 line 91) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 91 | slack.slack_messages | INSERT | `800870c56bda852a57dfa06cb4fd63e6` | unchanged (byte-identical to v14 line 93) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 93 | slack.slack_messages | INSERT | `1a68c2da0f36fc25489d3d9bbe9ccc32` | unchanged (byte-identical to v14 line 95) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 95 | slack.slack_messages | INSERT | `c183280a284440a6ca6cdbb5270c9139` | unchanged (byte-identical to v14 line 97) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 97 | slack.slack_messages | INSERT | `398502c0596e5347cc297f61eaefbd50` | unchanged (byte-identical to v14 line 99) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 99 | slack.slack_messages | INSERT | `229090ba6b316b667d1a6451b0297a47` | unchanged (byte-identical to v14 line 101) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 100 | slack.slack_messages | UPDATE | `id = '99aa913348bb05e6eda8daa06d37fc2a'` | unchanged (byte-identical to v14 line 102) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 102 | slack.slack_messages | INSERT | `99b22482ddd77dd01b451afb39014839` | unchanged (byte-identical to v14 line 104) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 104 | slack.slack_messages | INSERT | `f7261dd1b05eb2da3b81fe7d8cde2854` | unchanged (byte-identical to v14 line 106) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 106 | slack.slack_messages | INSERT | `c5657466a4af062ceef9f7c3285aeb74` | **NEW**: Leonard DM post "Paul's out…" in group DM `D05S58U4SAK`, 2025-09-30T17:05Z (moved from the #executives thread reply `7fe55f30…`, which is removed) | NEW (id/ts lookup, channel membership, chronology) | PASS |
| 108 | slack.slack_messages | INSERT | `3cddf83c394676d8b72c0c20ed58f520` | **CHANGED**: was a reply under `c891232a…`; now a thread parent (`thread_parent_id` NULL, `thread_ts_legacy` = own ts, `reply_count` 1, `reply_users_count` 1, `latest_reply` `1759276080.094417`); text now names Karthic, the 3 Dentsu folks, Anel's two at NCsoft and Ilse from Brightwater | NEW | PASS |
| 110 | slack.slack_messages | INSERT | `301ad67f082965686f35a9484aa25b0a` | **CHANGED**: now a reply to `3cddf83c…` (`thread_ts_legacy` `1759274400.518306`); text "…so I can tell Karthic, Ryo-san and the others" | NEW | PASS |
| 113 | trello.trello_actions | INSERT | `68c64270d660c977c4696986` | unchanged (byte-identical to v14 line 114) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 115 | trello.trello_actions | INSERT | `68db03b86054eff7e8e92474` | unchanged (byte-identical to v14 line 116) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 116 | trello.trello_cards | UPDATE | `id = '68c5a49e8491a9d7faf869d0'` | unchanged (byte-identical to v14 line 117) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 118 | trello.trello_cards | INSERT | `68c99e98737744bd966aed24` | unchanged (byte-identical to v14 line 119) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 120 | trello.trello_actions | INSERT | `68c99e98647b81be91f207f2` | unchanged (byte-identical to v14 line 121) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 121 | trello.trello_boards | UPDATE | `id = '640643a3fd8f3ca308d9318e'` | unchanged (byte-identical to v14 line 122) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 124 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844623441920000059` | unchanged (byte-identical to v14 line 125) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 126 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.com>` | unchanged (byte-identical to v14 line 127) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 128 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844623441920000061` | unchanged (byte-identical to v14 line 129) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 130 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.com>` | unchanged (byte-identical to v14 line 131) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 132 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844623441920000062` | unchanged (byte-identical to v14 line 133) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 134 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.com>` | unchanged (byte-identical to v14 line 135) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 136 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844724419788800011` | unchanged (byte-identical to v14 line 137) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 138 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>` | unchanged (byte-identical to v14 line 139) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 140 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844724419788800013` | unchanged (byte-identical to v14 line 141) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 142 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>` | unchanged (byte-identical to v14 line 143) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 144 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844724419788800014` | unchanged (byte-identical to v14 line 145) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 146 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>` | unchanged (byte-identical to v14 line 147) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 148 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844724419788800015` | unchanged (byte-identical to v14 line 149) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 150 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>` | unchanged (byte-identical to v14 line 151) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 152 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844162278195200024` | unchanged (byte-identical to v14 line 153) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 154 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CACJhvEE55qdWXuKC3BWlscoxBKrLUWavLQ3cpTJ@mail.gmail.com>` | unchanged (byte-identical to v14 line 155) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 156 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844354293432320031` | unchanged (byte-identical to v14 line 157) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 158 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAiKDPIoVSAFUBccUSRRBTi6dsmJdhof2EzteoIx@mail.gmail.com>` | unchanged (byte-identical to v14 line 159) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 160 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844610859008000037` | unchanged (byte-identical to v14 line 161) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 162 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAP6Gn2LV490e3El5rBDCgCItvhOdc7S6Wpb8nNq@mail.gmail.com>` | unchanged (byte-identical to v14 line 163) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 164 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844610859008000039` | unchanged (byte-identical to v14 line 165) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 166 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAP6Gn2LV490e3El5rBDCgCItvhOdc7S6Wpb8nNq@mail.gmail.com>` | unchanged (byte-identical to v14 line 167) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 167 | gmail.gmail_threads | UPDATE | `id = 'leonard.hayes@harmonygames.co/1844610859008000039'` | unchanged (byte-identical to v14 line 168) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 169 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAH2UMEfxg69PBVI7YxuPTO9uXYBOEfsCOfTEzpB@mail.gmail.com>` | unchanged (byte-identical to v14 line 170) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 171 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844318935449600041` | unchanged (byte-identical to v14 line 192) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 173 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_lp6f26Gm0Vi7deiv8pmy@mail.gmail.com>` | unchanged (byte-identical to v14 line 194) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 175 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844318935449600043` | unchanged (byte-identical to v14 line 196) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 177 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_lp6f26Gm0Vi7deiv8pmy@mail.gmail.com>` | unchanged (byte-identical to v14 line 198) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 179 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844294398771200045` | unchanged (byte-identical to v14 line 200) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 181 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@mail.gmail.com>` | unchanged (byte-identical to v14 line 202) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 183 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844294398771200047` | unchanged (byte-identical to v14 line 204) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 185 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@mail.gmail.com>` | unchanged (byte-identical to v14 line 206) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 187 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844294398771200048` | unchanged (byte-identical to v14 line 208) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 189 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@mail.gmail.com>` | unchanged (byte-identical to v14 line 210) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 191 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844294398771200049` | unchanged (byte-identical to v14 line 212) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 193 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@mail.gmail.com>` | unchanged (byte-identical to v14 line 214) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 194 | gmail.gmail_threads | UPDATE | `id = 'frederick.stone@harmonygames.co/1844294398771200045'` | unchanged (byte-identical to v14 line 215) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 196 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>` | unchanged (byte-identical to v14 line 217) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 197 | gmail.gmail_threads | UPDATE | `id = 'leonard.hayes@harmonygames.co/1844294398771200047'` | unchanged (byte-identical to v14 line 218) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 199 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>` | unchanged (byte-identical to v14 line 220) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 200 | gmail.gmail_threads | UPDATE | `id = 'robert@harmonygames.co/1844294398771200048'` | unchanged (byte-identical to v14 line 221) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 202 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>` | unchanged (byte-identical to v14 line 223) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 203 | gmail.gmail_threads | UPDATE | `id = 'arthur.blake@harmonygames.co/1844294398771200049'` | unchanged (byte-identical to v14 line 224) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 205 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>` | unchanged (byte-identical to v14 line 226) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 207 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844276782694400053` | unchanged (byte-identical to v14 line 228) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 209 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>` | unchanged (byte-identical to v14 line 230) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 211 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844276782694400055` | unchanged (byte-identical to v14 line 232) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 213 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>` | unchanged (byte-identical to v14 line 234) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 215 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844276782694400056` | unchanged (byte-identical to v14 line 236) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 217 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>` | unchanged (byte-identical to v14 line 238) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 219 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844276782694400057` | unchanged (byte-identical to v14 line 240) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 221 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>` | unchanged (byte-identical to v14 line 242) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 222 | gmail.gmail_threads | UPDATE | `id = 'frederick.stone@harmonygames.co/1844276782694400053'` | unchanged (byte-identical to v14 line 243) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 224 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>` | unchanged (byte-identical to v14 line 245) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 225 | gmail.gmail_threads | UPDATE | `id = 'leonard.hayes@harmonygames.co/1844276782694400055'` | unchanged (byte-identical to v14 line 246) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 227 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>` | unchanged (byte-identical to v14 line 248) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 228 | gmail.gmail_threads | UPDATE | `id = 'robert@harmonygames.co/1844276782694400056'` | unchanged (byte-identical to v14 line 249) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 230 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>` | unchanged (byte-identical to v14 line 251) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 231 | gmail.gmail_threads | UPDATE | `id = 'arthur.blake@harmonygames.co/1844276782694400057'` | unchanged (byte-identical to v14 line 252) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 233 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>` | unchanged (byte-identical to v14 line 254) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 235 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843992534712320061` | unchanged (byte-identical to v14 line 256) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 237 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-2b67d1aa-cbdd-d816-22c3-d5ace6cf900b@google.com>` | unchanged (byte-identical to v14 line 258) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 239 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1843992534712320063` | unchanged (byte-identical to v14 line 260) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 241 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-c82c189b-c33c-a6e0-5e43-def7d943af26@google.com>` | unchanged (byte-identical to v14 line 262) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 243 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1843992534712320064` | unchanged (byte-identical to v14 line 264) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 245 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-44faeeb8-a4b0-dae2-c4eb-4d2fda67b29b@google.com>` | unchanged (byte-identical to v14 line 266) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 247 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843718101401600063` | unchanged (byte-identical to v14 line 268) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 249 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-2d8383e3-21d5-e958-783a-c960b5e98416@google.com>` | unchanged (byte-identical to v14 line 270) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 251 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1843718101401600065` | unchanged (byte-identical to v14 line 272) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 253 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-010d9a7c-8101-ee76-3333-bfb1ce826d3a@google.com>` | unchanged (byte-identical to v14 line 274) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 255 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1843718101401600066` | unchanged (byte-identical to v14 line 276) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 257 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-9d6c5aee-50ea-1d96-5cd0-dcef1de61254@google.com>` | unchanged (byte-identical to v14 line 278) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 259 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844620925337600069` | unchanged (byte-identical to v14 line 280) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 261 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-fb0024cc-3ec0-8309-fa11-9a9c8d3a1092@google.com>` | unchanged (byte-identical to v14 line 282) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 263 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844620925337600071` | unchanged (byte-identical to v14 line 284) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 265 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-34e4ed6d-59c6-2518-30fe-38f76d64f540@google.com>` | unchanged (byte-identical to v14 line 286) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 267 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844620925337600072` | unchanged (byte-identical to v14 line 288) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 269 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-b1816210-d8e8-b7e1-bec3-161d17c275ca@google.com>` | unchanged (byte-identical to v14 line 290) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 271 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844724105216000067` | unchanged (byte-identical to v14 line 292) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 273 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-297f69c9-ad63-fafd-14c3-70dbf78756f3@google.com>` | unchanged (byte-identical to v14 line 294) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 276 | gcal.gcal_events | INSERT | `evt_2f86b0d4c9e17a35b64e0d` | unchanged (byte-identical to v14 line 297) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 278 | gcal.gcal_events | INSERT | `evt_b511d4619c6f46ee63959b` | unchanged (byte-identical to v14 line 299) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 280 | gcal.gcal_events | INSERT | `evt_8bd5e929463b854ec0ad13` | unchanged (byte-identical to v14 line 301) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 282 | gcal.gcal_events | INSERT | `evt_ca908a712455521f1f8b43` | unchanged (byte-identical to v14 line 303) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 284 | gcal.gcal_events | INSERT | `evt_7d3e19b04a6c25f8e1b9a0` | unchanged (byte-identical to v14 line 305) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 286 | gcal.gcal_events | INSERT | `evt_99df25b554cac93e2926fd` | unchanged (byte-identical to v14 line 307) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 288 | gcal.gcal_events | INSERT | `evt_671dce00bcb85abb3e355e` | unchanged (byte-identical to v14 line 309) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 290 | gcal.gcal_events | INSERT | `evt_d65aa89778c3ebfa5d97b2` | unchanged (byte-identical to v14 line 311) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 292 | gcal.gcal_events | INSERT | `evt_9c41e7a2d05b38f6e1a7c4` | unchanged (byte-identical to v14 line 313) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 294 | gcal.gcal_events | INSERT | `evt_75d8a0687ea57b663a40b0` | unchanged (byte-identical to v14 line 315) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 296 | gcal.gcal_events | INSERT | `evt_6b2e94d0c17a3f58e9d2b1` | unchanged (byte-identical to v14 line 317) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 298 | gcal.gcal_events | INSERT | `evt_9ba121a353c889190ae6d2` | unchanged (byte-identical to v14 line 319) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 300 | gcal.gcal_events | INSERT | `evt_07843a430fe8e936bf3cda` | unchanged (byte-identical to v14 line 321) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 302 | gcal.gcal_events | INSERT | `evt_6aa4a42052090c05f4afe6` | unchanged (byte-identical to v14 line 323) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 305 | linear.linear_issues | INSERT | `ZOM-567` | unchanged (byte-identical to v14 line 326) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 307 | linear.linear_comments | INSERT | `lc_94eb35d962cfbdd31e1bd496` | unchanged (byte-identical to v14 line 328) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 309 | linear.linear_comments | INSERT | `lc_4369758f577612cdb63b3457` | **NEW**: ZOM-567 comment seq 2, NCsoft (2 accounts from Anel's team, after the Sep 19 call), TestFlight + Play added Sep 22, 2025-09-30T17:45Z | NEW | PASS |
| 311 | linear.linear_comments | INSERT | `lc_5e2ff140afff06e3a78e2fe1` | **NEW**: ZOM-567 comment seq 3, Brightwater (Ilse Marrow), TestFlight + Play added Sep 26, 2025-09-30T18:05Z | NEW | PASS |
| 313 | linear.linear_comments | INSERT | `lc_b549f3057640a5eb08f7581e` | **CHANGED**: Dentsu comment, `sequence` 2 → 4; all other values unchanged | NEW | PASS |
| 316 | contacts.contacts | INSERT | `e3a91c07d5b48f26a0c7e314` | unchanged (byte-identical to v14 line 333) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 318 | contacts.contacts | INSERT | `b72f0d6e19c3a84e5d21f9a0` | unchanged (byte-identical to v14 line 335) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 320 | contacts.contacts | INSERT | `5d0e8b31f7a29c64e1b0d3a8` | unchanged (byte-identical to v14 line 337) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 322 | contacts.contacts | INSERT | `a4c2e9f07b31d85e6c0f1b29` | unchanged (byte-identical to v14 line 339) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |
| 323 | — | COMMIT | `—` | unchanged (byte-identical to v14 line 340) | REUSED (v14 report ledger, chained to v13–v10) + lint whole-script parse NEW | PASS |

Removed from v14 (no longer executed): v14 line 85 INSERT Slack `7fe55f3086c1b6bcdb5dec66b00cff56`; v14 line 111 UPDATE Slack `c891232a8b395a701268cff14cffd883` (counters); v14 lines 172/174/176/178 INSERT `<CAz_RUxJqfvgfKAkYtz-r7Yoht-mPT7mOKAMrJNp@mail.gmail.com>` (Frederick, Leonard, Robert, Arthur); v14 lines 179/182/185/188 UPDATE snippets on base threads `frederick.stone@…/1842283406259093714`, `leonard.hayes@…/1842282783388831849`, `robert@…/1842283406290252813`, `arthur.blake@…/1842283406345050279`; v14 lines 181/184/187/190 INSERT `<CAU8zEO-shvUXQVk4-lQPDj5ihq08pcABtHRrtUv@mail.gmail.com>` (four mailboxes). The v14 versions of lines 83, 108, 110 and the Dentsu comment are replaced by the rows above with the same keys.

UPDATEs in v15 (13): all byte-identical to v14 (lines 31, 100, 167 and the Trello/Gmail updates); before/after values as recorded in the v14 report.

## 6. Check A: records, references and IDs

- **New keys don't collide.** Slack `c5657466…` (and the re-shaped `3cddf83c…`/`301ad67f…`) and their ts values: none in the complete base (610,468 records). Linear `lc_4369758f…`, `lc_5e2ff140…`: base has no Linear comments and no text match. No duplicate INSERT key within the SQL (the repeated Slides `presentation_id` values are the parent column of page/element rows, unchanged and verified before).
- **References resolve.** `301ad67f…` → `3cddf83c…` (inserted just before, same channel). The new comments → ZOM-567 (line 305). DM `D05S58U4SAK` and channel `C0880U9751A` exist and hold the posting users. Removing the `c891232a…` UPDATE and the Gmail rows leaves no reference to anything that isn't inserted or in the base.
- **One account per person.** Leonard `EMPLOYEE_0038_SLACK_ID`, Arthur `EMPLOYEE_0025_SLACK_ID` / `usr_cc3e90160f490686` (arthur.blake). No new person or account.
- **ID contracts.** No Gmail `history_id` or Drive `content_path` touched by the changes.
- **Byte-identical rows.** Reused PASS (§11).

## 7. Check B: SQL structure and supported schema rules

- One BEGIN/COMMIT block, 162 statements. Independent count: all 147 INSERTs have matching column and value counts (Slack 18/18, Linear comments 9/9). Quotes balanced (`Paul''s`, `can''t`, `Anel''s`, `it''s`).
- JSON columns: Slack list columns `'[]'`, `metadata_json` `'{}'`. Linear `created_at`/`updated_at` written `YYYY-MM-DDTHH:MM:SSZ`. No `text_fts`/`body_text_fts`. Lint `json_shape`, `missing_required`, `generated_column`, `text_time_format`: nothing.
- **Provisional snapshot comparison:** Slack columns MATCH. `linear_comments.sequence` is NOT COVERED by the snapshot; it was already used by the unchanged comment rows (Advisory 1).

## 8. Check C: dates, relationships and consistency

- **Clock.** New/changed event timestamps: Slack 2025-09-30T17:05Z, 23:20Z, 23:48Z; Linear comments 17:45Z, 18:05Z, 18:40Z. All before 2025-10-01T07:00Z; the latest event in the script is still 23:48Z.
- **Chronology.** ZOM-567 created 17:10Z; comments seq 1–4 at 17:25, 17:45, 18:05, 18:40Z, in order; issue `updated_at` 18:40Z = latest comment. Slack reply 23:48Z after its 23:20Z parent. Leonard's DM (17:05Z = 10:05 AM PT) "he wrote me this morning" follows Paul's 14:55Z (7:55 AM PT) email to him (line 169).
- **Thread state.** `3cddf83c…` counters (1 reply, 1 user, latest `1759276080.094417`) match its one reply. `4921f321…` is standalone with zero counters and no remaining reply. `c891232a…` keeps its base zero counters with no injected reply.
- **Cross-record agreement.** Arthur's 23:20Z Slack ("the investor tester list … never got attached to the internal track, so nobody on it has android yet (Karthic, the 3 Dentsu folks, Anel's two at NCsoft and Ilse from Brightwater), whatever the Linear log says") names exactly the ZOM-567 entries: T-Accelerate/Karthic, NCsoft 2 accounts from Anel's team, Brightwater/Ilse Marrow, Dentsu 3 accounts. The Linear log (Arthur, 17:25–18:40Z) says the Play adds landed; Arthur's own later Slack corrects it: a later correction, not a structural contradiction. The NCsoft "Sep 19 call" and Karthic "Sep 22" dates agree with the base Slack schedule; Leonard's base 09-22 email sent Karthic the TestFlight invite and Play link. No base or injected record says any of these testers has Android working. Leonard's "so I can tell Karthic, Ryo-san and the others" fits the wider list. Paul: the 09-19 #executives post (in) is superseded by his 09-30 email and Leonard's DM (out); nothing later says he's in.
- **Grader-facing text.** None; all new text is in-story.
- **Known issues.** No changed record builds on a Snowflake or Confluence conflict. SC-10 fix (line 31) unchanged.
- **Byte-identical rows.** Reused PASS (§11).

## 9. Findings

No demonstrated defects. Advisories (don't block this stage):

1. **Columns not in the schema snapshot (Check B, provisional, unchanged).** `slides_pages.notes`, `slides_page_elements.table_json` and `.ordinal`, and `linear_comments.sequence` (now in four comment rows) appear in neither the snapshot nor the base exports. If a platform table lacks one, that INSERT fails and the script rolls back. Smallest fix: drop those columns and values, or confirm the script loads on the platform.
2. **New external address for the Makers Fund guest (Check A/C, advisory, unchanged).** The Oct 8 invites use `PERSON_9905_EMAIL` for "Michael Cheung"; the only base Makers Fund correspondent is `PERSON_3773_EMAIL`. No record settles whether they're the same person, so this isn't a defect.

The v14 Advisory 3 (Robert's Bridge Round subject text) no longer applies: those rows were removed.

Notes for later stages (not injection findings): the Android correction now lives only in Arthur's 09-30 23:20Z Slack thread in #zombie-match3d (against ZOM-567); the email confirmation from Karthic/Arthur is gone. Paul's "out" now sits in his 09-30 email to Leonard (Leonard's mailbox only) and Leonard's post in group DM `D05S58U4SAK`. Whether Frederick can see these and whether they settle the answer is for `/prompt` and `/hardness`.

## 10. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | New Slack and Linear keys checked against complete base collections and the SQL: 0 collisions. Parents, channels, issue and author resolve; removed rows leave no dangling references. Byte-identical rows reuse the v14 PASS. |
| B — SQL structure and supported schema rules | PASS | 147/147 INSERTs with matching counts; JSON and Linear date formats valid; no generated columns. `linear_comments.sequence` and three Slides columns not covered by the snapshot: advisory. Not live-certified. |
| C — Dates, relationships and consistency | PASS | All new timestamps before the clock; replies follow parents; Slack counters match; Linear log order consistent; Slack correction agrees with the ZOM-567 entries and base schedule. No grader-facing text. |

Outside certification scope (disclosed, not gates): live execution and current database compatibility (including the four columns), search ranking, Agent visibility and persona access, task difficulty.

## 11. Stage ownership and reuse

Reused evidence (stage-evidence-v1), from `Evals/task_inputs/reports/0_injection.md` as it stood before this rerun, SHA-256 `048229e8ce83a0ad95eb3230f57ec5d5d664684560aaaf3fbde40cddc57d8752` (injection-static-v2, PASS/COMPLETE, SQL `75b6cb2a…0fee`), which chained to the v13 (`456d7442…`), v12, v11 and v10 reviews for rows unchanged then:

| Item | Source ledger / check | Dependencies verified unchanged |
|---|---|---|
| Checks A–C for the 155 statements byte-identical to v14 | previous §4–§8, §11 | exact-content match of each statement to v14 (§5); universe manifest `da2f4cf0…aac1a`; Eval 0 `e034019b…`; schema snapshot `31dcb2b4…`; id_contracts `fc4711ef…`; lint `a8226e2a…`; roster `3f217451…`; acl `e9bca2b3…`; known issues `29b89d85…`; WORKFLOW `ee4cd8e1…`; clock 2025-10-01T07:00Z |
| Uniqueness of `4921f321…` id and ts `1758303600.418207` (line 83) | previous §4 (complete Slack scan, 610,468 records) | same manifest; row now byte-identical to v13 line 83 |

`/prompt` may reuse these static checks only while all of these hold: SQL SHA-256 `69db98aed17f40cbcbbfad417b7eb21a118dffdbb63b798cf8322ddac226182b`, universe manifest `da2f4cf0…aac1a`, schema snapshot `31dcb2b4…`, id_contracts `fc4711ef…`, Eval 0 `e034019b…`, clock 2025-10-01T07:00Z. `/prompt` still owns discoverability and persona access. This SQL changed, so earlier /prompt, /hardness, /oe and /rubric results are outdated; run them again in that order.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt, then /hardness (with a fresh run on this SQL), /oe and /rubric. Advisories 1–2 are optional; any change makes a new SQL version that needs /injection again.

Evidence limits: Static review only. Live load, current database compatibility (including the four snapshot-uncovered columns), Agent visibility and difficulty are outside scope. The supplementary Gmail "NCsoft" search stopped at its match limit (the complete "apps/internaltest" scan covers the material check). The identity of the base Makers Fund correspondent `PERSON_3773` can't be determined from the records (Advisory 2).
