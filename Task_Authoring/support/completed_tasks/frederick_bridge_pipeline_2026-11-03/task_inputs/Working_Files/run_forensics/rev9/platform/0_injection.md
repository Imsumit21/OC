# Injection Data-Integrity Review (Eval 0)

Review version: `injection-static-v2`
Evidence contract: `stage-evidence-v1`
Review time: 2026-11-02T16:20Z (actual)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Mode: chat review, attempt 6ae4e299a13034b7eb8305f8 (static, SQL not executed)

## 1. Scope and inputs

| Input | Value |
|---|---|
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` (input revision 17, from chat attachment `01_Universe_Inject (12).sql`), 164,000 bytes, SHA-256 `a34c7de3860159eaef325dd84118e478686b1f122a090679dd3e462273b5f885`. Replaces `01_Universe_Inject (11).sql` (SHA `4895577e…eef9`, last reviewed PASS/COMPLETE), so that report no longer applies. |
| Diff from the previous version | `diff` v11 → v12, 8 hunks: line 3 header comment ("130 INSERT" → "143 INSERT", matches the parse); Trello block (v11 lines 112–113 → v12 lines 112–119): new comment action, card-455 badge/date update re-valued, new card 456 + its createCard action, board date re-valued; Q4 email body edited in all 4 mailbox copies (lines 136/140/144/148; one sentence + `size_estimate`); 3 Gmail invite threads + 3 messages added (lines 253–264); 4 gcal events added (lines 290–297). Every other statement is byte-identical to v11 (138 of 157). |
| Assignment (context only) | Frederick Stone, Co-founder; not graded here |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Eval | `Evals/0_Injection_Quality_Eval.md` `e034019b8ec450437509a73dd3bae2d303b57561b0f67fcc1e5d19266f663eff` |
| Shared workflow | WORKFLOW `ee4cd8e1…cd5d` via `hg_reference.py guide injection`; routes trello/gmail/gcal/contacts; schema entries `trello.trello_actions`, `trello.trello_cards`, `trello.trello_boards`, `gmail.gmail_threads`, `gmail.gmail_messages`, `gcal.gcal_events` |
| Schema snapshot | `references/schema/injection.json` `31dcb2b43feca8e5…` (unverified, provisional) |
| ID contracts | `references/schema/id_contracts.json` `fc4711ef07667333…` |
| Lint | `hg_injection_lint.py` `a8226e2a69425355…`, version `injection-lint-v1` |
| Roster / ACL | roster.json `3f2174513f639e37…`, acl.md `e9bca2b35f98d5ef…` (identity checks only) |
| Known data issues | `guidelines/known_data_issues.md` `29b89d856c454124…` (SC-10 already resolved in the sheet by line 31, unchanged) |

Input/authority issues: none for this stage. SQL comments are evidence of intent only; none addresses a grader or mentions tool calls, pass rate or gates.

## 2. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, base manifest, review version | NEW, done (saved as input revision 17 before review) |
| Run lint; resolve every flag | NEW, done (0 FAIL, 0 CHECK, 0 INFO) |
| Inventory every statement and affected record | NEW, done: 157 statements (BEGIN, 143 INSERT, 12 UPDATE, COMMIT), ledger §5; each statement matched to v11 by exact content |
| Check A | NEW for the 19 changed/added statements; REUSED for 138 byte-identical rows (§11): PASS |
| Check B | NEW for changed/added statements and whole-script lint parse; REUSED for byte-identical rows: PASS (provisional snapshot advisory) |
| Check C | NEW for changed/added statements and the injected/base records they relate to; REUSED for byte-identical rows: PASS |
| Report coverage, findings, limits, one verdict | NEW, done |

## 3. Lint result

`hg_injection_lint.py` on SHA `a34c7de3…f885`, universe synthcut, clock 2025-10-01T07:00Z. Base files loaded: contacts, slack users, trello, gmail users, linear, confluence. Rows parsed: 143 INSERT, 12 UPDATE (trello_actions 3 insert; trello_cards 1 insert + 1 update; trello_boards 1 update; gmail_threads 31 insert + 8 update; gmail_messages 39 insert; gcal_events 14 insert; others unchanged).

Flags: **none** (FAIL 0, CHECK 0, INFO 0). Nothing to resolve. Checks A–C were still run in full.

## 4. Source coverage (new checks in this run)

| Check | Source / pointer | Coverage | Result |
|---|---|---|---|
| Trello IDs: actions `68db03b86054eff7e8e92474`, `68c99e98647b81be91f207f2`; card `68c99e98737744bd966aed24`; card shortLink `Rk7vQe2W`; `idShort` 456 on board `640643a3…318e` | trello `data.json` `/actions`, `/cards` (full arrays loaded) | complete | 0 collisions. Board's max base `idShort` is 455 → 456 is next. `Rk7vQe2W` appears in no base card URL; each new ID appears once in the SQL |
| Trello references | `/members`, `/lists`, `/boards`, `/cards` | complete | `PERSON_6094_TRELLO_USER_ID` = member "Leonard Hayes" (username `leonard.hayes`), the same creator as base card 455's create/update actions. List `640643a3…3195` = "To Do", list `…3196` = "Doing", both on this board, open. Card URL host `PERSON_6092_TRELLO_USERNAME.com/c/<shortLink>/<idShort>-<slug>` and `shortLink`/`shortUrl` NULL match the base card pattern (e.g. card 455) |
| Trello counters/dates | card 455 base: `comments` 0, `dateLastActivity` 2025-09-13T17:06:40Z; board base `dateLastActivity` 2025-09-13T17:06:40Z (= latest base action on the board) | complete | After the SQL: card 455 has 2 injected comments (09-14, 09-29) → `comments: 2` ✔, `dateLastActivity` 09-29T22:10Z = latest comment ✔; board → 09-29T22:10Z = latest board action ✔; new card `dateLastActivity` = its createCard time 09-16T17:30Z ✔; `pos` 40960 after the one open base To Do card ("Playable Kickoff", 36864) |
| Trello action shape | base createCard/commentCard actions | sampled shape + card 455's two base actions | `data_json` keys (board/card/list, `text`, `textData`) match base createCard/commentCard shape |
| Gmail message IDs (3 new invite messages) | `hg_search.py lookup gmail --file 'threads/*.json' --pointer /messages` | 81,404 files, 95,164 messages, scan complete, 0 errors | 0 matches |
| Gmail thread IDs (`…/1844620925337600069`, `…71`, `…72`) | thread IDs are root fields (lookup's array pointer doesn't apply, 81,404 shape errors, so not used as evidence); `search-many` text search for each numeric part over `threads/*.json` | scan complete, 0 errors | 0 matches; each appears once in the SQL (`…600070` unused anywhere) |
| gcal IDs | gcal `data.json` `/events` (10,395 events, full load) | complete | event_ids `evt_6b2e94d0…`, `evt_9ba121a3…`, `evt_07843a43…`, `evt_6aa4a420…`: 0 collisions; `ical_uid` `a8832552…@hg4`: 0 base matches (shared only by the 4 new copies); Meet code `rnv-oxtq-jdw`: 0 base matches |
| Guest `PERSON_9905_EMAIL` / "Michael Cheung" | search-many "PERSON_9905", "Cheung", "Makers" over gmail threads, contacts, gcal, slack 2025-08/09, trello, gdocs | all scans complete | `PERSON_9905` appears in no base record. "Cheung" only in two unrelated newsletters (Rowan Cheung, Erika Cheung). Base sheet row 34 (Makers Fund): Partner "Michael Cheung", Latest Status "Reached out - no response as of 09/11". Base Makers Fund email thread `00000985` (2023 intro + Leonard's 2025-09-03 bridge reachout) is with `PERSON_3773_NAME <PERSON_3773_EMAIL>`; no base record names that person, so no existing address is shown for Michael Cheung (Advisory 2) |
| Makers Fund status after 09/11 | slack `C096HFA5Z8W/33,89`, `D04UC0UEN2V/6,32` | Makers hits complete for 2025-08/09 | 09-03 "sent", 09-08 "sent, no update", 09-15 "sent, no response". No base record says Makers passed. A meeting invite sent 09-29 is a later development, not a contradiction |
| NCsoft / Anel (new card 456) | sheet row 79; gmail thread `00015231`; gcal `/events/5522,5738,8468,9883` | complete reads | Sheet: NCsoft, Anel Ceman, "Second Pitch", "follow-up engine conversation with them on 09/15". Calendar: first pitch "NCsoft <> …" 2025-09-10 16:00Z. Email: Anel 09-16T06:59Z "I booked the call on Fri" → Leonard 09-19 sends material, video and summary; Anel 09-29/09-30 proposes a Thursday call via Calendly. Card created 09-16T17:30Z "F/up with Anel after the engine deep dive" is a follow-up to-do around that session; no contradicting record |
| Oct 8 invite times | SQL lines 256–264, 291–297 | computed | 2025-10-08 is a Wednesday; 09:00 PDT = 12:00 EDT = 16:00Z, matching `start_ts`/`start_json`; 45 min to 16:45Z. `internal_date` 1759167600000 = 2025-09-29T17:40:00Z = `date` header (Mon 29 Sep) |
| Q4 email edit | `diff` of v11 line 130 vs v12 line 136 (same for 3 other copies) | whole body | Only change: "Whatever the Existing Investor Update card says to do for firms that pass, do that too." → "Then do what I put on the Existing Investor Update card in Trello."; `size_estimate` 1975 → 1954. The four copies stay identical except mailbox fields |
| Reused coverage | previous report §4–§8, §11 (all byte-identical rows) | see §11 | unchanged |

## 5. Operation ledger

Every statement in execution order (current SQL line numbers; for multi-line INSERTs, the VALUES line). Rows marked NEW were verified fresh (§4, §6–§8). Byte-identical rows reuse the v11 ledger (which reused v10's), with their v11 line given. The whole script was re-parsed by the lint in this run.

| SQL line | Table | Op | Record / target | Change vs v11 | Verification | Result |
|---|---|---|---|---|---|---|
| 5 | — | BEGIN | `—` | unchanged (byte-identical to v11 line 5) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 8 | gdrive.drive_files | INSERT | `f_8d2c47a91e05b3f6d7c418` | unchanged (byte-identical to v11 line 8) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 10 | gdrive.drive_files | INSERT | `f_3b9e61c04d7a52e8f1a6c2` | unchanged (byte-identical to v11 line 10) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 12 | gdrive.drive_files | INSERT | `d_5e8a1c3f9b07d2e64a1b93` | unchanged (byte-identical to v11 line 12) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 14 | gdrive.drive_files | INSERT | `f_c61a0e93b7d24f58a2e917` | unchanged (byte-identical to v11 line 14) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 16 | gdrive.drive_files | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v11 line 16) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 18 | gdrive.drive_files | INSERT | `f_6e1d93a0c4b72f85d39a0e` | unchanged (byte-identical to v11 line 18) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 21 | gdocs.docs_documents | INSERT | `f_8d2c47a91e05b3f6d7c418` | unchanged (byte-identical to v11 line 21) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 23 | gdocs.docs_documents | INSERT | `f_3b9e61c04d7a52e8f1a6c2` | unchanged (byte-identical to v11 line 23) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 25 | gdocs.docs_documents | INSERT | `f_c61a0e93b7d24f58a2e917` | unchanged (byte-identical to v11 line 25) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 28 | gsheets.sheets_spreadsheets | INSERT | `f_6e1d93a0c4b72f85d39a0e` | unchanged (byte-identical to v11 line 28) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 30 | gsheets.sheets_sheets | INSERT | `f_6e1d93a0c4b72f85d39a0e` | unchanged (byte-identical to v11 line 30) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 31 | gsheets.sheets_sheets | UPDATE | `spreadsheet_id = 'f_48247af79428823c3cac92' AND sheet_id = 0` | unchanged (byte-identical to v11 line 31) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 34 | gslides.slides_presentations | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v11 line 34) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 36 | gslides.slides_pages | INSERT | `slide_b4c21ca913ab` | unchanged (byte-identical to v11 line 36) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 38 | gslides.slides_page_elements | INSERT | `slide_b4c21ca913ab` | unchanged (byte-identical to v11 line 38) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 40 | gslides.slides_page_elements | INSERT | `slide_b4c21ca913ab` | unchanged (byte-identical to v11 line 40) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 42 | gslides.slides_pages | INSERT | `slide_256dc0474f7c` | unchanged (byte-identical to v11 line 42) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 44 | gslides.slides_page_elements | INSERT | `slide_256dc0474f7c` | unchanged (byte-identical to v11 line 44) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 46 | gslides.slides_page_elements | INSERT | `slide_256dc0474f7c` | unchanged (byte-identical to v11 line 46) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 48 | gslides.slides_pages | INSERT | `slide_fd6dbd079420` | unchanged (byte-identical to v11 line 48) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 50 | gslides.slides_page_elements | INSERT | `slide_fd6dbd079420` | unchanged (byte-identical to v11 line 50) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 52 | gslides.slides_page_elements | INSERT | `slide_fd6dbd079420` | unchanged (byte-identical to v11 line 52) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 54 | gslides.slides_pages | INSERT | `slide_bb11abfc5fad` | unchanged (byte-identical to v11 line 54) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 56 | gslides.slides_page_elements | INSERT | `slide_bb11abfc5fad` | unchanged (byte-identical to v11 line 56) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 58 | gslides.slides_page_elements | INSERT | `slide_bb11abfc5fad` | unchanged (byte-identical to v11 line 58) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 60 | gslides.slides_pages | INSERT | `slide_cb3f0884f833` | unchanged (byte-identical to v11 line 60) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 62 | gslides.slides_page_elements | INSERT | `slide_cb3f0884f833` | unchanged (byte-identical to v11 line 62) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 64 | gslides.slides_page_elements | INSERT | `slide_cb3f0884f833` | unchanged (byte-identical to v11 line 64) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 66 | gslides.slides_pages | INSERT | `slide_a56932e4c738` | unchanged (byte-identical to v11 line 66) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 68 | gslides.slides_page_elements | INSERT | `slide_a56932e4c738` | unchanged (byte-identical to v11 line 68) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 70 | gslides.slides_page_elements | INSERT | `slide_a56932e4c738` | unchanged (byte-identical to v11 line 70) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 72 | gslides.slides_pages | INSERT | `slide_c9c7eed73bb9` | unchanged (byte-identical to v11 line 72) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 74 | gslides.slides_page_elements | INSERT | `slide_c9c7eed73bb9` | unchanged (byte-identical to v11 line 74) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 76 | gslides.slides_page_elements | INSERT | `slide_c9c7eed73bb9` | unchanged (byte-identical to v11 line 76) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 78 | gslides.slides_pages | INSERT | `slide_329b5dfcb888` | unchanged (byte-identical to v11 line 78) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 80 | gslides.slides_page_elements | INSERT | `slide_329b5dfcb888` | unchanged (byte-identical to v11 line 80) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 83 | slack.slack_messages | INSERT | `4921f321db5d08f936aac24a6a1d2af8` | unchanged (byte-identical to v11 line 83) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 85 | slack.slack_messages | INSERT | `7fef94264090696760180223fc8265e7` | unchanged (byte-identical to v11 line 85) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 87 | slack.slack_messages | INSERT | `20924cc7f5176991d8a97a8eafb291d0` | unchanged (byte-identical to v11 line 87) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 89 | slack.slack_messages | INSERT | `19e1e65d5952f075e8492867c6bcd472` | unchanged (byte-identical to v11 line 89) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 91 | slack.slack_messages | INSERT | `800870c56bda852a57dfa06cb4fd63e6` | unchanged (byte-identical to v11 line 91) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 93 | slack.slack_messages | INSERT | `1a68c2da0f36fc25489d3d9bbe9ccc32` | unchanged (byte-identical to v11 line 93) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 95 | slack.slack_messages | INSERT | `c183280a284440a6ca6cdbb5270c9139` | unchanged (byte-identical to v11 line 95) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 97 | slack.slack_messages | INSERT | `398502c0596e5347cc297f61eaefbd50` | unchanged (byte-identical to v11 line 97) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 99 | slack.slack_messages | INSERT | `229090ba6b316b667d1a6451b0297a47` | unchanged (byte-identical to v11 line 99) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 100 | slack.slack_messages | UPDATE | `id = '99aa913348bb05e6eda8daa06d37fc2a'` | unchanged (byte-identical to v11 line 100) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 102 | slack.slack_messages | INSERT | `99b22482ddd77dd01b451afb39014839` | unchanged (byte-identical to v11 line 102) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 104 | slack.slack_messages | INSERT | `f7261dd1b05eb2da3b81fe7d8cde2854` | unchanged (byte-identical to v11 line 104) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 106 | slack.slack_messages | INSERT | `3cddf83c394676d8b72c0c20ed58f520` | unchanged (byte-identical to v11 line 106) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 108 | slack.slack_messages | INSERT | `301ad67f082965686f35a9484aa25b0a` | unchanged (byte-identical to v11 line 108) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 111 | trello.trello_actions | INSERT | `68c64270d660c977c4696986` | unchanged (byte-identical to v11 line 111) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 113 | trello.trello_actions | INSERT | `68db03b86054eff7e8e92474` | CHANGED/ADDED (see §4) | NEW | PASS |
| 114 | trello.trello_cards | UPDATE | `id = '68c5a49e8491a9d7faf869d0'` | CHANGED/ADDED (see §4) | NEW | PASS |
| 116 | trello.trello_cards | INSERT | `68c99e98737744bd966aed24` | CHANGED/ADDED (see §4) | NEW | PASS |
| 118 | trello.trello_actions | INSERT | `68c99e98647b81be91f207f2` | CHANGED/ADDED (see §4) | NEW | PASS |
| 119 | trello.trello_boards | UPDATE | `id = '640643a3fd8f3ca308d9318e'` | CHANGED/ADDED (see §4) | NEW | PASS |
| 122 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844623441920000059` | unchanged (byte-identical to v11 line 116) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 124 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.com>` | unchanged (byte-identical to v11 line 118) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 126 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844623441920000061` | unchanged (byte-identical to v11 line 120) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 128 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.com>` | unchanged (byte-identical to v11 line 122) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 130 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844623441920000062` | unchanged (byte-identical to v11 line 124) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 132 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.com>` | unchanged (byte-identical to v11 line 126) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 134 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844724419788800011` | unchanged (byte-identical to v11 line 128) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 136 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>` | CHANGED/ADDED (see §4) | NEW | PASS |
| 138 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844724419788800013` | unchanged (byte-identical to v11 line 132) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 140 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>` | CHANGED/ADDED (see §4) | NEW | PASS |
| 142 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844724419788800014` | unchanged (byte-identical to v11 line 136) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 144 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>` | CHANGED/ADDED (see §4) | NEW | PASS |
| 146 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844724419788800015` | unchanged (byte-identical to v11 line 140) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 148 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>` | CHANGED/ADDED (see §4) | NEW | PASS |
| 150 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844162278195200024` | unchanged (byte-identical to v11 line 144) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 152 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CACJhvEE55qdWXuKC3BWlscoxBKrLUWavLQ3cpTJ@mail.gmail.com>` | unchanged (byte-identical to v11 line 146) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 154 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844354293432320031` | unchanged (byte-identical to v11 line 148) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 156 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAiKDPIoVSAFUBccUSRRBTi6dsmJdhof2EzteoIx@mail.gmail.com>` | unchanged (byte-identical to v11 line 150) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 158 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844610859008000037` | unchanged (byte-identical to v11 line 152) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 160 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAP6Gn2LV490e3El5rBDCgCItvhOdc7S6Wpb8nNq@mail.gmail.com>` | unchanged (byte-identical to v11 line 154) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 162 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844610859008000039` | unchanged (byte-identical to v11 line 156) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 164 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAP6Gn2LV490e3El5rBDCgCItvhOdc7S6Wpb8nNq@mail.gmail.com>` | unchanged (byte-identical to v11 line 158) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 166 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844318935449600041` | unchanged (byte-identical to v11 line 160) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 168 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_lp6f26Gm0Vi7deiv8pmy@mail.gmail.com>` | unchanged (byte-identical to v11 line 162) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 170 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844318935449600043` | unchanged (byte-identical to v11 line 164) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 172 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_lp6f26Gm0Vi7deiv8pmy@mail.gmail.com>` | unchanged (byte-identical to v11 line 166) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 174 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844294398771200045` | unchanged (byte-identical to v11 line 168) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 176 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@mail.gmail.com>` | unchanged (byte-identical to v11 line 170) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 178 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844294398771200047` | unchanged (byte-identical to v11 line 172) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 180 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@mail.gmail.com>` | unchanged (byte-identical to v11 line 174) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 182 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844294398771200048` | unchanged (byte-identical to v11 line 176) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 184 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@mail.gmail.com>` | unchanged (byte-identical to v11 line 178) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 186 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844294398771200049` | unchanged (byte-identical to v11 line 180) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 188 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@mail.gmail.com>` | unchanged (byte-identical to v11 line 182) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 189 | gmail.gmail_threads | UPDATE | `id = 'frederick.stone@harmonygames.co/1844294398771200045'` | unchanged (byte-identical to v11 line 183) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 191 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>` | unchanged (byte-identical to v11 line 185) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 192 | gmail.gmail_threads | UPDATE | `id = 'leonard.hayes@harmonygames.co/1844294398771200047'` | unchanged (byte-identical to v11 line 186) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 194 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>` | unchanged (byte-identical to v11 line 188) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 195 | gmail.gmail_threads | UPDATE | `id = 'robert@harmonygames.co/1844294398771200048'` | unchanged (byte-identical to v11 line 189) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 197 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>` | unchanged (byte-identical to v11 line 191) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 198 | gmail.gmail_threads | UPDATE | `id = 'arthur.blake@harmonygames.co/1844294398771200049'` | unchanged (byte-identical to v11 line 192) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 200 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>` | unchanged (byte-identical to v11 line 194) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 202 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844276782694400053` | unchanged (byte-identical to v11 line 196) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 204 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>` | unchanged (byte-identical to v11 line 198) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 206 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844276782694400055` | unchanged (byte-identical to v11 line 200) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 208 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>` | unchanged (byte-identical to v11 line 202) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 210 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844276782694400056` | unchanged (byte-identical to v11 line 204) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 212 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>` | unchanged (byte-identical to v11 line 206) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 214 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844276782694400057` | unchanged (byte-identical to v11 line 208) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 216 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>` | unchanged (byte-identical to v11 line 210) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 217 | gmail.gmail_threads | UPDATE | `id = 'frederick.stone@harmonygames.co/1844276782694400053'` | unchanged (byte-identical to v11 line 211) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 219 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>` | unchanged (byte-identical to v11 line 213) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 220 | gmail.gmail_threads | UPDATE | `id = 'leonard.hayes@harmonygames.co/1844276782694400055'` | unchanged (byte-identical to v11 line 214) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 222 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>` | unchanged (byte-identical to v11 line 216) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 223 | gmail.gmail_threads | UPDATE | `id = 'robert@harmonygames.co/1844276782694400056'` | unchanged (byte-identical to v11 line 217) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 225 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>` | unchanged (byte-identical to v11 line 219) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 226 | gmail.gmail_threads | UPDATE | `id = 'arthur.blake@harmonygames.co/1844276782694400057'` | unchanged (byte-identical to v11 line 220) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 228 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>` | unchanged (byte-identical to v11 line 222) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 230 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843992534712320061` | unchanged (byte-identical to v11 line 224) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 232 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-2b67d1aa-cbdd-d816-22c3-d5ace6cf900b@google.com>` | unchanged (byte-identical to v11 line 226) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 234 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1843992534712320063` | unchanged (byte-identical to v11 line 228) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 236 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-c82c189b-c33c-a6e0-5e43-def7d943af26@google.com>` | unchanged (byte-identical to v11 line 230) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 238 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1843992534712320064` | unchanged (byte-identical to v11 line 232) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 240 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-44faeeb8-a4b0-dae2-c4eb-4d2fda67b29b@google.com>` | unchanged (byte-identical to v11 line 234) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 242 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843718101401600063` | unchanged (byte-identical to v11 line 236) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 244 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-2d8383e3-21d5-e958-783a-c960b5e98416@google.com>` | unchanged (byte-identical to v11 line 238) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 246 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1843718101401600065` | unchanged (byte-identical to v11 line 240) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 248 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-010d9a7c-8101-ee76-3333-bfb1ce826d3a@google.com>` | unchanged (byte-identical to v11 line 242) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 250 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1843718101401600066` | unchanged (byte-identical to v11 line 244) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 252 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-9d6c5aee-50ea-1d96-5cd0-dcef1de61254@google.com>` | unchanged (byte-identical to v11 line 246) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 254 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844620925337600069` | CHANGED/ADDED (see §4) | NEW | PASS |
| 256 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-fb0024cc-3ec0-8309-fa11-9a9c8d3a1092@google.com>` | CHANGED/ADDED (see §4) | NEW | PASS |
| 258 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844620925337600071` | CHANGED/ADDED (see §4) | NEW | PASS |
| 260 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-34e4ed6d-59c6-2518-30fe-38f76d64f540@google.com>` | CHANGED/ADDED (see §4) | NEW | PASS |
| 262 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844620925337600072` | CHANGED/ADDED (see §4) | NEW | PASS |
| 264 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-b1816210-d8e8-b7e1-bec3-161d17c275ca@google.com>` | CHANGED/ADDED (see §4) | NEW | PASS |
| 266 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844724105216000067` | unchanged (byte-identical to v11 line 248) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 268 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-297f69c9-ad63-fafd-14c3-70dbf78756f3@google.com>` | unchanged (byte-identical to v11 line 250) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 271 | gcal.gcal_events | INSERT | `evt_2f86b0d4c9e17a35b64e0d` | unchanged (byte-identical to v11 line 253) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 273 | gcal.gcal_events | INSERT | `evt_b511d4619c6f46ee63959b` | unchanged (byte-identical to v11 line 255) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 275 | gcal.gcal_events | INSERT | `evt_8bd5e929463b854ec0ad13` | unchanged (byte-identical to v11 line 257) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 277 | gcal.gcal_events | INSERT | `evt_ca908a712455521f1f8b43` | unchanged (byte-identical to v11 line 259) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 279 | gcal.gcal_events | INSERT | `evt_7d3e19b04a6c25f8e1b9a0` | unchanged (byte-identical to v11 line 261) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 281 | gcal.gcal_events | INSERT | `evt_99df25b554cac93e2926fd` | unchanged (byte-identical to v11 line 263) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 283 | gcal.gcal_events | INSERT | `evt_671dce00bcb85abb3e355e` | unchanged (byte-identical to v11 line 265) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 285 | gcal.gcal_events | INSERT | `evt_d65aa89778c3ebfa5d97b2` | unchanged (byte-identical to v11 line 267) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 287 | gcal.gcal_events | INSERT | `evt_9c41e7a2d05b38f6e1a7c4` | unchanged (byte-identical to v11 line 269) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 289 | gcal.gcal_events | INSERT | `evt_75d8a0687ea57b663a40b0` | unchanged (byte-identical to v11 line 271) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 291 | gcal.gcal_events | INSERT | `evt_6b2e94d0c17a3f58e9d2b1` | CHANGED/ADDED (see §4) | NEW | PASS |
| 293 | gcal.gcal_events | INSERT | `evt_9ba121a353c889190ae6d2` | CHANGED/ADDED (see §4) | NEW | PASS |
| 295 | gcal.gcal_events | INSERT | `evt_07843a430fe8e936bf3cda` | CHANGED/ADDED (see §4) | NEW | PASS |
| 297 | gcal.gcal_events | INSERT | `evt_6aa4a42052090c05f4afe6` | CHANGED/ADDED (see §4) | NEW | PASS |
| 300 | linear.linear_issues | INSERT | `ZOM-567` | unchanged (byte-identical to v11 line 274) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 302 | linear.linear_comments | INSERT | `lc_94eb35d962cfbdd31e1bd496` | unchanged (byte-identical to v11 line 276) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 304 | linear.linear_comments | INSERT | `lc_b549f3057640a5eb08f7581e` | unchanged (byte-identical to v11 line 278) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 307 | contacts.contacts | INSERT | `e3a91c07d5b48f26a0c7e314` | unchanged (byte-identical to v11 line 281) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 309 | contacts.contacts | INSERT | `b72f0d6e19c3a84e5d21f9a0` | unchanged (byte-identical to v11 line 283) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 311 | contacts.contacts | INSERT | `5d0e8b31f7a29c64e1b0d3a8` | unchanged (byte-identical to v11 line 285) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 313 | contacts.contacts | INSERT | `a4c2e9f07b31d85e6c0f1b29` | unchanged (byte-identical to v11 line 287) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |
| 314 | — | COMMIT | `—` | unchanged (byte-identical to v11 line 288) | REUSED (v11/v10 ledger) + lint whole-script parse NEW | PASS |

## 6. Check A: records, references and IDs

- **New keys don't collide.** Trello actions, card id, `idShort` 456 and shortLink; three Gmail threads and three messages; four gcal event_ids and their shared `ical_uid`: none exists in the complete base collections (§4), and each appears exactly once among the SQL's own inserts.
- **References resolve.** Board `640643a3…318e` ("Harmony Games"), lists "To Do" and "Doing", card 455 ("Existing Investor Update") and creator `PERSON_6094_TRELLO_USER_ID` (Leonard Hayes) exist in base Trello. Gmail rows sit in the existing mailboxes of Frederick, Robert and Arthur; organizer and creator `leonard.hayes@harmonygames.co` and all internal attendees are roster users. The two UPDATEs use primary-key predicates on existing rows.
- **One account per person.** No new account for an internal person. The external guest `PERSON_9905_EMAIL` ("Michael Cheung", Makers Fund) is a new address token. No base record links the name Michael Cheung to any address, so a second address for an existing person isn't demonstrated (Advisory 2).
- **ID contracts.** `history_id` NULL on all three new threads (allowed). No Drive `content_path` involved.
- **Byte-identical rows.** References, collisions, Drive readability and one account per person: reused PASS (§11).

## 7. Check B: SQL structure and supported schema rules

- One BEGIN/COMMIT block, 157 statements. Each new or changed INSERT has matching column and value counts (Trello actions 7/7, card 18/18, Gmail messages 22/22, threads 4/4, gcal 23/23) and ends with `;`. The UPDATEs have valid `SET` lists and key predicates.
- JSON columns (`data_json`, `badges_json`, `idMembers_json`, `idLabels_json`, `to_json`/`cc_json`/`bcc_json`/`reply_to_json`, `headers_json`, `attachments_meta_json`, `attendees_json`, `start_json`/`end_json`, `rrule_json`) are valid JSON with the base shapes. Lint `json_shape`, `missing_required` and `generated_column` checks found nothing; `body_text_fts` isn't set.
- **Provisional snapshot comparison:** every column in the new or changed statements is in the snapshot, and none of them omits a NOT NULL column that has no default: MATCH. The four uncovered columns from unchanged rows are as before (Advisory 1).

## 8. Check C: dates, relationships and consistency

- **Clock.** New event timestamps: Trello 2025-09-16T17:30Z, 2025-09-29T22:10Z; Gmail invites 2025-09-29T17:40Z; gcal `created`/`updated` 2025-09-29T17:40Z. All are at or before 2025-10-01T07:00Z. Only the gcal start/end (2025-10-08 16:00–16:45Z) are later, and those are plan fields. The latest event timestamp in the script is still 2025-09-30T23:48Z.
- **Chronology.** Card 456 is created 09-16 (after the 09-10 NCsoft pitch and Anel's 09-16 06:59Z booking note). The 09-29 card-455 comment follows the 09-14 one. The 09-29 invite (17:40Z) precedes the 09-29 Trello comment (22:10Z) that refers to "a call or meeting … on Fred's calendar after Sep 30". Leonard's 09-30 21:05Z email ("Then do what I put on the Existing Investor Update card") comes after both card comments.
- **Cross-record agreement.** The invite email subject, snippet, body and gcal copies agree on title, date, local times (PDT for Fred and Robert, EDT for Arthur), organizer, guest list and Meet link. The four gcal copies share one `ical_uid`, with `self` set on each owner's copy. Trello counters and activity dates match the actions (§4).
- **Base agreement.** No base record contradicts a Makers Fund meeting set up on 09-29: the latest base status is "no response" (Slack 09-15; sheet "as of 09/11"), and no base record says Makers passed. The NCsoft card fits the sheet's "Second Pitch" and the 09-15/09-19 engine-session emails.
- **Grader-facing text.** None. The new comment and email texts are instructions from one persona to another, inside the story.
- **Known issues.** No new record builds on a Snowflake or Confluence conflict. The SC-10 fix (line 31) is unchanged.
- **Byte-identical rows.** Clock, chronology and base agreement: reused PASS (§11).

## 9. Findings

No demonstrated defects. Advisories (don't block this stage):

1. **Columns not in the schema snapshot (Check B, provisional, unchanged).** `slides_pages.notes`, `slides_page_elements.table_json` and `.ordinal`, and `linear_comments.sequence` appear in neither the snapshot nor the base exports. If a platform table lacks any of them, that INSERT fails and the whole script rolls back. Smallest fix: drop those four columns and their values, or confirm the script loads on the platform.
2. **New external address for the Makers Fund guest (Check A/C, advisory).** The Oct 8 invites (lines 256–264, 291–297) use `PERSON_9905_EMAIL` for "Michael Cheung". In the base, the only Makers Fund correspondent is `PERSON_3773_EMAIL` (`PERSON_3773_NAME`), whom Leonard emailed on 2025-09-03 about the bridge. No record says whether that person is Michael Cheung, so this isn't a defect. If you mean the same contact Leonard reached out to, using `PERSON_3773_EMAIL` (and `PERSON_3773_NAME` in the title) would tie the meeting to the base thread. If you keep the new token, the agent can identify the firm only from the event title "Michael Cheung" and the sheet's Partner column.

Note for later stages (not an injection finding): the new 09-29 card-455 comment spells out the grouping, checklist, follow-up-card and "already has a To Do card" / "meeting on Fred's calendar after Sep 30" rules. Card 456 (Anel/NCsoft) and the Oct 8 Makers Fund meeting are the records those exceptions act on. Whether that is too explicit, and whether the persona can see and act on each record, is for `/prompt` and `/hardness`.

## 10. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | All 13 new keys checked against complete base collections and the SQL itself: 0 collisions. Trello board, lists, card 455 and creator resolve. Internal identities are roster users. External guest token is new (Advisory 2). Byte-identical rows reuse the v11 PASS. |
| B — SQL structure and supported schema rules | PASS | Column/value counts match. JSON is valid with base shapes. Snapshot MATCH for all new/changed columns, no generated columns set, no NOT NULL omissions. Four uncovered columns from unchanged rows remain advisory. Not live-certified. |
| C — Dates, relationships and consistency | PASS | All new event timestamps at or before the clock; only Oct 8 start/end are later (plan fields). Chronology holds. Trello counters and dates match. Invite copies agree. No base contradiction for Makers Fund or NCsoft. No grader-facing text. |

Outside certification scope (disclosed, not gates): live execution and current database compatibility (including the four columns), search ranking, Agent visibility and persona access, task difficulty.

## 11. Stage ownership and reuse

Reused evidence (stage-evidence-v1), from `Evals/task_inputs/reports/0_injection.md` as it stood before this rerun, SHA-256 `ccd975b6a2ff352e86292bb8afa44eeafbb262ae6dadccce3b8946a0a60b3a64` (injection-static-v2, PASS/COMPLETE, SQL `4895577e…eef9`), which in turn reused the v10 review (`c2750b9f…0e4b`) for rows unchanged then:

| Item | Source ledger / check | Dependencies verified unchanged |
|---|---|---|
| Checks A–C for the 138 statements byte-identical to v11 (ids/collisions, membership/identity, structure, JSON shapes, chronology, base agreement, Slides/Docs/Sheets/Slack/Linear/Gmail/Calendar relationships, the line-31 SC-10 sheet fix) | previous §4–§8, §11 | exact-content match of each statement to v11 (§5); universe manifest `da2f4cf0…aac1a`; Eval 0 `e034019b…`; schema snapshot `31dcb2b4…`; id_contracts `fc4711ef…`; lint `a8226e2a…`; roster `3f217451…`; acl `e9bca2b3…`; known issues `29b89d85…`; clock 2025-10-01T07:00Z (all equal to the previous report) |
| Uniqueness of earlier new keys | previous §4/§6 | collections unchanged (same manifest); the new keys were checked separately against both base and SQL (§4) |

`/prompt` may reuse these static checks only while all of these hold: SQL SHA-256 `a34c7de3860159eaef325dd84118e478686b1f122a090679dd3e462273b5f885`, universe manifest `da2f4cf0…aac1a`, schema snapshot `31dcb2b4…`, id_contracts `fc4711ef…`, Eval 0 `e034019b…`, clock 2025-10-01T07:00Z. `/prompt` still owns discoverability and persona access. This SQL changed, so earlier /prompt, /hardness, /oe and /rubric results are outdated; run /prompt, /hardness, /oe and /rubric again in that order.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt, then /hardness (with a fresh run on this SQL), /oe and /rubric. Optionally address Advisory 1 or 2 first; either change makes a new SQL version that needs /injection again.

Evidence limits: Static review only. Live load, current database compatibility (including the four snapshot-uncovered columns), Agent visibility and difficulty are outside scope. Gmail thread-ID uniqueness rests on a complete text search for each ID's numeric part, because thread IDs are file-root fields that the array lookup can't address. The identity of the base Makers Fund correspondent `PERSON_3773` can't be determined from the records (Advisory 2).
