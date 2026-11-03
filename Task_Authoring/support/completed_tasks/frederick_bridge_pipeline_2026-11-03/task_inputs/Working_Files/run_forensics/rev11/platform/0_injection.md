# Injection Data-Integrity Review (Eval 0)

Review version: `injection-static-v2`
Evidence contract: `stage-evidence-v1`
Review time: 2026-11-02T22:15Z (actual)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Mode: chat review, attempt 6ae4e299a13034b7eb8305f8 (static, SQL not executed)

## 1. Scope and inputs

| Input | Value |
|---|---|
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` (input revision 23, from chat attachment `01_Universe_Inject (14).sql`), 186,435 bytes, SHA-256 `75b6cb2ac45350d2560210daff4e96a3ff3982630259d8eadf94141524260fee`. Replaces `01_Universe_Inject (13).sql` (SHA `c999829d…ecba`, last reviewed PASS/COMPLETE), so that report no longer applies. |
| Diff from the previous version | 173 statements vs 162. 155 statements byte-identical to v13. Changed: line 3 header comment ("153 INSERT, 18 UPDATE", matches the parse); line 83 #executives post `4921f321…` turned into a thread parent; line 85 new reply `7fe55f30…` ("Paul's out…"); lines 108/110 Slack replies `3cddf83c…`/`301ad67f…` re-worded (Karthic removed); lines 168/170 Paul Heydon's SAFE reply rewritten (now backs out, 09-30 14:55Z, Leonard's mailbox only, new Message-ID); lines 172–190 new: Karthic's reply and Arthur Blake's answer on the base "Bridge Round" thread in four mailboxes, plus four thread-snippet UPDATEs. Removed from v13: Paul's "signed" reply in Frederick's and Leonard's mailboxes (Message-ID `<CAA_lm07…>`) and the two snippet UPDATEs that went with it (v13 lines 166–171). |
| Assignment (context only) | Frederick Stone, Co-founder; not graded here |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Eval | `Evals/0_Injection_Quality_Eval.md` `e034019b8ec450437509a73dd3bae2d303b57561b0f67fcc1e5d19266f663eff` |
| Shared workflow | WORKFLOW `ee4cd8e1…cd5d` via `hg_reference.py guide injection --services slack gmail --tables slack.slack_messages gmail.gmail_threads gmail.gmail_messages`; scoring.json `c14873e6…e5bc` |
| Schema snapshot | `references/schema/injection.json` `31dcb2b43feca8e5…` (unverified, provisional) |
| ID contracts | `references/schema/id_contracts.json` `fc4711ef07667333…` |
| Lint | `hg_injection_lint.py` `a8226e2a69425355…`, version `injection-lint-v1` |
| Roster / ACL | roster.json `3f2174513f639e37…`, acl.md `e9bca2b35f98d5ef…` (identity checks only) |
| Known data issues | `guidelines/known_data_issues.md` `29b89d856c454124…` (SC-10 already resolved in the sheet by line 31, unchanged) |

Input/authority issues: none for this stage. SQL comments are evidence of intent only; none addresses a grader or mentions tool calls, pass rate or gates.

## 2. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, base manifest, review version | NEW, done (saved as input revision 23 before review) |
| Run lint; resolve every flag | NEW, done (0 FAIL, 0 CHECK, 0 INFO) |
| Inventory every statement and affected record | NEW, done: 173 statements (BEGIN, 153 INSERT, 18 UPDATE, COMMIT), ledger §5; each statement matched to v13 by exact content |
| Check A | NEW for the 18 changed/added statements; REUSED for 155 byte-identical rows (§11): PASS |
| Check B | NEW for changed/added statements and whole-script lint parse; REUSED for byte-identical rows: PASS (provisional snapshot advisory) |
| Check C | NEW for changed/added statements and the injected/base records they relate to; REUSED for byte-identical rows: PASS |
| Report coverage, findings, limits, one verdict | NEW, done |

## 3. Lint result

`hg_injection_lint.py` on SHA `75b6cb2a…0fee`, universe synthcut, clock 2025-10-01T07:00Z. Base files loaded: contacts, slack users, trello, gmail users, linear, confluence. Rows parsed: 153 INSERT, 18 UPDATE (including slack_messages 14 insert + 2 update; gmail_threads 31 insert + 13 update; gmail_messages 48 insert; gcal_events 14; linear_issues 1; linear_comments 2; contacts 4).

Flags: **none** (FAIL 0, CHECK 0, INFO 0). Nothing to resolve. Checks A–C were still run in full.

## 4. Source coverage (new checks in this run)

| Check | Source / pointer | Coverage | Result |
|---|---|---|---|
| Base Bridge Round threads (4 mailboxes) | gmail `threads/frederick@harmonygames.co_1842283406259093714.json`, `threads/leonard@harmonygames.co_1842282783388831849.json`, `threads/00015209.json` (Robert), `threads/blake@harmonygames.co_1842283406345050279.json` | `search-many` over all 81,404 gmail thread files, scan complete, 0 errors; all 7 messages of each thread read | Each thread exists once with id = the SQL `thread_id` and `user_email` = the SQL mailbox. Latest message in each: `<CAPBs_a4Nc7raF3Ox7owAzBzWDdRtn_zf0CPzuPeBrmL=rTd8cA@mail.gmail.com>`, 2025-09-22 10:40:07 -0700 (17:40:07Z), Leonard → `PERSON_3242` (Karthic), cc `PERSON_4420`, `PERSON_5203`, Robert, Frederick, Arthur. Body: "We already sent a testflight invite to your email … For Android, you should be able to download it here: https://play.google.com/apps/internaltest/… let us know if you run into any issues" |
| Karthic's reply (lines 172–178) | same threads; contact line 337 (`Karthic R`, T-Accelerate Capital, `PERSON_3242_EMAIL`) | full records | `In-Reply-To`/`References` = the 09-22 message above, which exists in all four mailboxes. Reply-all: To Leonard, cc the same five recipients as the parent (the sender drops out). Subject "Re: Bridge Round for [SOURCE_ORG_0001]?" = the subject in the Frederick, Leonard and Arthur copies. Sender token `PERSON_3242_EMAIL` = the base address Karthic uses in this thread (message 2, 2025-09-17) and the injected contact |
| Arthur's answer (lines 181–190) | same | full statements | `In-Reply-To`/`References` = Karthic's new Message-ID; To Karthic, cc Leonard + the other four (reply-all). Labels: `SENT` in Arthur's own mailbox, INBOX in the other three, as in the SQL's other reply chains |
| New Gmail Message-IDs `<CAz_RUxJqfvgfKAkYtz-r7Yoht-mPT7mOKAMrJNp@…>`, `<CAU8zEO-shvUXQVk4-lQPDj5ihq08pcABtHRrtUv@…>`, `<CAH2UMEfxg69PBVI7YxuPTO9uXYBOEfsCOfTEzpB@…>` | same scan | complete | 0 base matches. Each `<mailbox>/<Message-ID>` key appears once among the SQL's 153 INSERT keys (duplicate-key check over all inserts: none) |
| Paul's SAFE reply (line 170) and thread UPDATE (line 168) | SQL lines 165, 167 (Leonard thread `…/1844610859008000039` and nudge `<CAP6Gn2L…>`) | full statements | Thread created earlier in the SQL (line 165) before the UPDATE (168). `In-Reply-To`/`References` = the nudge (2025-09-29T15:00Z). Reply 2025-09-30T14:55Z: `internal_date` 1759244100000 = `date` = header "Tue, 30 Sep 2025 14:55:00 +0000". Snippet UPDATE = the new message's snippet |
| Removed v13 records | SQL text | full | `<CAA_lm07…>` appears nowhere in v14; Frederick's thread `…/1844610859008000037` keeps only the nudge (lines 161/163) and its snippet is the nudge text, so nothing points at a removed row |
| Slack thread `4921f321…` / reply `7fe55f30…` (lines 83, 85) | slack `channels.json` (`C07C2866011` = `executives`, not archived), `users.json`; all `messages/*/*.json` | 4,840 files, 610,468 records, complete | `EMPLOYEE_0038_SLACK_ID` = Leonard Hayes, a member of #executives. Neither id nor ts `1759251900.863415` nor thread_ts `1758303600.418207` occurs in the base. Parent counters: `reply_count` 1, `reply_users_count` 1 (one author, 0038), `latest_reply` = reply ts, `thread_ts_legacy` = own ts (base convention, verified in the v13 run) |
| Slack replies `3cddf83c…`, `301ad67f…` (lines 108, 110) | same keys and parent as v13; parent UPDATE (line 111) byte-identical | text-only change | Keys, parent `c891232a…`, timestamps and counters unchanged from the verified v13 rows; only `text` differs |
| Linear log ZOM-567 (lines 326–330) | SQL | full statements | "T-Accelerate (Karthic): TestFlight and Play internal track both added Sep 22"; "Dentsu … Play internal track added Sep 26 (investor tester list)". The later Gmail (09-30 10:20Z/20:05Z) and Slack (23:20Z) say Android access never worked because the tester list wasn't attached to the track |
| Paul references across the SQL | lines 30, 31, 83, 85, 161–170 | full | Sheet (line 30, "in", $50K) and the 09-19 #executives post (line 83) are earlier; Paul's 09-30 14:55Z email and Leonard's 09-30 17:05Z thread reply say he is out. No record after 09-30 14:55Z says he is in |
| Reused coverage | previous report §4–§8, §11 (all byte-identical rows) | see §11 | unchanged |

## 5. Operation ledger

Every statement in execution order (current SQL line numbers; for multi-line INSERTs, the VALUES line). Rows marked NEW were verified fresh (§4, §6–§8). Byte-identical rows reuse the v13 ledger (which chains to v12, v11 and v10), with their v13 line given. The whole script was re-parsed by the lint in this run.

| SQL line | Table | Op | Record / target | Change vs v13 | Verification | Result |
|---|---|---|---|---|---|---|
| 5 | — | BEGIN | `—` | unchanged (byte-identical to v13 line 5) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 8 | gdrive.drive_files | INSERT | `f_8d2c47a91e05b3f6d7c418` | unchanged (byte-identical to v13 line 8) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 10 | gdrive.drive_files | INSERT | `f_3b9e61c04d7a52e8f1a6c2` | unchanged (byte-identical to v13 line 10) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 12 | gdrive.drive_files | INSERT | `d_5e8a1c3f9b07d2e64a1b93` | unchanged (byte-identical to v13 line 12) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 14 | gdrive.drive_files | INSERT | `f_c61a0e93b7d24f58a2e917` | unchanged (byte-identical to v13 line 14) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 16 | gdrive.drive_files | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 16) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 18 | gdrive.drive_files | INSERT | `f_6e1d93a0c4b72f85d39a0e` | unchanged (byte-identical to v13 line 18) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 21 | gdocs.docs_documents | INSERT | `f_8d2c47a91e05b3f6d7c418` | unchanged (byte-identical to v13 line 21) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 23 | gdocs.docs_documents | INSERT | `f_3b9e61c04d7a52e8f1a6c2` | unchanged (byte-identical to v13 line 23) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 25 | gdocs.docs_documents | INSERT | `f_c61a0e93b7d24f58a2e917` | unchanged (byte-identical to v13 line 25) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 28 | gsheets.sheets_spreadsheets | INSERT | `f_6e1d93a0c4b72f85d39a0e` | unchanged (byte-identical to v13 line 28) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 30 | gsheets.sheets_sheets | INSERT | `f_6e1d93a0c4b72f85d39a0e` | unchanged (byte-identical to v13 line 30) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 31 | gsheets.sheets_sheets | UPDATE | `spreadsheet_id=f_48247af79428823c3cac92` | unchanged (byte-identical to v13 line 31) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 34 | gslides.slides_presentations | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 34) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 36 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 36) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 38 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 38) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 40 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 40) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 42 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 42) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 44 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 44) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 46 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 46) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 48 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 48) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 50 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 50) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 52 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 52) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 54 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 54) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 56 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 56) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 58 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 58) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 60 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 60) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 62 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 62) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 64 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 64) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 66 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 66) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 68 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 68) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 70 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 70) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 72 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 72) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 74 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 74) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 76 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 76) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 78 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 78) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 80 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v13 line 80) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 83 | slack.slack_messages | INSERT | `4921f321db5d08f936aac24a6a1d2af8` | **changed/added in v14** | NEW (§4, §6–§8) | PASS |
| 85 | slack.slack_messages | INSERT | `7fe55f3086c1b6bcdb5dec66b00cff56` | **changed/added in v14** | NEW (§4, §6–§8) | PASS |
| 87 | slack.slack_messages | INSERT | `7fef94264090696760180223fc8265e7` | unchanged (byte-identical to v13 line 85) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 89 | slack.slack_messages | INSERT | `20924cc7f5176991d8a97a8eafb291d0` | unchanged (byte-identical to v13 line 87) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 91 | slack.slack_messages | INSERT | `19e1e65d5952f075e8492867c6bcd472` | unchanged (byte-identical to v13 line 89) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 93 | slack.slack_messages | INSERT | `800870c56bda852a57dfa06cb4fd63e6` | unchanged (byte-identical to v13 line 91) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 95 | slack.slack_messages | INSERT | `1a68c2da0f36fc25489d3d9bbe9ccc32` | unchanged (byte-identical to v13 line 93) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 97 | slack.slack_messages | INSERT | `c183280a284440a6ca6cdbb5270c9139` | unchanged (byte-identical to v13 line 95) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 99 | slack.slack_messages | INSERT | `398502c0596e5347cc297f61eaefbd50` | unchanged (byte-identical to v13 line 97) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 101 | slack.slack_messages | INSERT | `229090ba6b316b667d1a6451b0297a47` | unchanged (byte-identical to v13 line 99) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 102 | slack.slack_messages | UPDATE | `id=99aa913348bb05e6eda8daa06d37fc2a` | unchanged (byte-identical to v13 line 100) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 104 | slack.slack_messages | INSERT | `99b22482ddd77dd01b451afb39014839` | unchanged (byte-identical to v13 line 102) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 106 | slack.slack_messages | INSERT | `f7261dd1b05eb2da3b81fe7d8cde2854` | unchanged (byte-identical to v13 line 104) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 108 | slack.slack_messages | INSERT | `3cddf83c394676d8b72c0c20ed58f520` | **changed/added in v14** | NEW (§4, §6–§8) | PASS |
| 110 | slack.slack_messages | INSERT | `301ad67f082965686f35a9484aa25b0a` | **changed/added in v14** | NEW (§4, §6–§8) | PASS |
| 111 | slack.slack_messages | UPDATE | `id=c891232a8b395a701268cff14cffd883` | unchanged (byte-identical to v13 line 109) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 114 | trello.trello_actions | INSERT | `68c64270d660c977c4696986` | unchanged (byte-identical to v13 line 112) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 116 | trello.trello_actions | INSERT | `68db03b86054eff7e8e92474` | unchanged (byte-identical to v13 line 114) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 117 | trello.trello_cards | UPDATE | `id=68c5a49e8491a9d7faf869d0` | unchanged (byte-identical to v13 line 115) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 119 | trello.trello_cards | INSERT | `68c99e98737744bd966aed24` | unchanged (byte-identical to v13 line 117) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 121 | trello.trello_actions | INSERT | `68c99e98647b81be91f207f2` | unchanged (byte-identical to v13 line 119) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 122 | trello.trello_boards | UPDATE | `id=640643a3fd8f3ca308d9318e` | unchanged (byte-identical to v13 line 120) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 125 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844623441920000059` | unchanged (byte-identical to v13 line 123) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 127 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.com>` | unchanged (byte-identical to v13 line 125) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 129 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844623441920000061` | unchanged (byte-identical to v13 line 127) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 131 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.com>` | unchanged (byte-identical to v13 line 129) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 133 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844623441920000062` | unchanged (byte-identical to v13 line 131) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 135 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.com>` | unchanged (byte-identical to v13 line 133) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 137 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844724419788800011` | unchanged (byte-identical to v13 line 135) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 139 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>` | unchanged (byte-identical to v13 line 137) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 141 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844724419788800013` | unchanged (byte-identical to v13 line 139) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 143 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>` | unchanged (byte-identical to v13 line 141) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 145 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844724419788800014` | unchanged (byte-identical to v13 line 143) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 147 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>` | unchanged (byte-identical to v13 line 145) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 149 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844724419788800015` | unchanged (byte-identical to v13 line 147) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 151 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>` | unchanged (byte-identical to v13 line 149) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 153 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844162278195200024` | unchanged (byte-identical to v13 line 151) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 155 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CACJhvEE55qdWXuKC3BWlscoxBKrLUWavLQ3cpTJ@mail.gmail.com>` | unchanged (byte-identical to v13 line 153) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 157 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844354293432320031` | unchanged (byte-identical to v13 line 155) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 159 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAiKDPIoVSAFUBccUSRRBTi6dsmJdhof2EzteoIx@mail.gmail.com>` | unchanged (byte-identical to v13 line 157) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 161 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844610859008000037` | unchanged (byte-identical to v13 line 159) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 163 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAP6Gn2LV490e3El5rBDCgCItvhOdc7S6Wpb8nNq@mail.gmail.com>` | unchanged (byte-identical to v13 line 161) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 165 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844610859008000039` | unchanged (byte-identical to v13 line 163) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 167 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAP6Gn2LV490e3El5rBDCgCItvhOdc7S6Wpb8nNq@mail.gmail.com>` | unchanged (byte-identical to v13 line 165) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 168 | gmail.gmail_threads | UPDATE | `id=leonard.hayes@harmonygames.co/1844610859008000039` | **changed/added in v14** | NEW (§4, §6–§8) | PASS |
| 170 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAH2UMEfxg69PBVI7YxuPTO9uXYBOEfsCOfTEzpB@mail.gmail.com>` | **changed/added in v14** | NEW (§4, §6–§8) | PASS |
| 172 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAz_RUxJqfvgfKAkYtz-r7Yoht-mPT7mOKAMrJNp@mail.gmail.com>` | **changed/added in v14** | NEW (§4, §6–§8) | PASS |
| 174 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAz_RUxJqfvgfKAkYtz-r7Yoht-mPT7mOKAMrJNp@mail.gmail.com>` | **changed/added in v14** | NEW (§4, §6–§8) | PASS |
| 176 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAz_RUxJqfvgfKAkYtz-r7Yoht-mPT7mOKAMrJNp@mail.gmail.com>` | **changed/added in v14** | NEW (§4, §6–§8) | PASS |
| 178 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAz_RUxJqfvgfKAkYtz-r7Yoht-mPT7mOKAMrJNp@mail.gmail.com>` | **changed/added in v14** | NEW (§4, §6–§8) | PASS |
| 179 | gmail.gmail_threads | UPDATE | `id=frederick.stone@harmonygames.co/1842283406259093714` | **changed/added in v14** | NEW (§4, §6–§8) | PASS |
| 181 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAU8zEO-shvUXQVk4-lQPDj5ihq08pcABtHRrtUv@mail.gmail.com>` | **changed/added in v14** | NEW (§4, §6–§8) | PASS |
| 182 | gmail.gmail_threads | UPDATE | `id=leonard.hayes@harmonygames.co/1842282783388831849` | **changed/added in v14** | NEW (§4, §6–§8) | PASS |
| 184 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAU8zEO-shvUXQVk4-lQPDj5ihq08pcABtHRrtUv@mail.gmail.com>` | **changed/added in v14** | NEW (§4, §6–§8) | PASS |
| 185 | gmail.gmail_threads | UPDATE | `id=robert@harmonygames.co/1842283406290252813` | **changed/added in v14** | NEW (§4, §6–§8) | PASS |
| 187 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAU8zEO-shvUXQVk4-lQPDj5ihq08pcABtHRrtUv@mail.gmail.com>` | **changed/added in v14** | NEW (§4, §6–§8) | PASS |
| 188 | gmail.gmail_threads | UPDATE | `id=arthur.blake@harmonygames.co/1842283406345050279` | **changed/added in v14** | NEW (§4, §6–§8) | PASS |
| 190 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAU8zEO-shvUXQVk4-lQPDj5ihq08pcABtHRrtUv@mail.gmail.com>` | **changed/added in v14** | NEW (§4, §6–§8) | PASS |
| 192 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844318935449600041` | unchanged (byte-identical to v13 line 173) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 194 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_lp6f26Gm0Vi7deiv8pmy@mail.gmail.com>` | unchanged (byte-identical to v13 line 175) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 196 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844318935449600043` | unchanged (byte-identical to v13 line 177) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 198 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_lp6f26Gm0Vi7deiv8pmy@mail.gmail.com>` | unchanged (byte-identical to v13 line 179) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 200 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844294398771200045` | unchanged (byte-identical to v13 line 181) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 202 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@mail.gmail.com>` | unchanged (byte-identical to v13 line 183) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 204 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844294398771200047` | unchanged (byte-identical to v13 line 185) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 206 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@mail.gmail.com>` | unchanged (byte-identical to v13 line 187) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 208 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844294398771200048` | unchanged (byte-identical to v13 line 189) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 210 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@mail.gmail.com>` | unchanged (byte-identical to v13 line 191) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 212 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844294398771200049` | unchanged (byte-identical to v13 line 193) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 214 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@mail.gmail.com>` | unchanged (byte-identical to v13 line 195) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 215 | gmail.gmail_threads | UPDATE | `id=frederick.stone@harmonygames.co/1844294398771200045` | unchanged (byte-identical to v13 line 196) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 217 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>` | unchanged (byte-identical to v13 line 198) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 218 | gmail.gmail_threads | UPDATE | `id=leonard.hayes@harmonygames.co/1844294398771200047` | unchanged (byte-identical to v13 line 199) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 220 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>` | unchanged (byte-identical to v13 line 201) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 221 | gmail.gmail_threads | UPDATE | `id=robert@harmonygames.co/1844294398771200048` | unchanged (byte-identical to v13 line 202) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 223 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>` | unchanged (byte-identical to v13 line 204) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 224 | gmail.gmail_threads | UPDATE | `id=arthur.blake@harmonygames.co/1844294398771200049` | unchanged (byte-identical to v13 line 205) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 226 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>` | unchanged (byte-identical to v13 line 207) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 228 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844276782694400053` | unchanged (byte-identical to v13 line 209) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 230 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>` | unchanged (byte-identical to v13 line 211) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 232 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844276782694400055` | unchanged (byte-identical to v13 line 213) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 234 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>` | unchanged (byte-identical to v13 line 215) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 236 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844276782694400056` | unchanged (byte-identical to v13 line 217) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 238 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>` | unchanged (byte-identical to v13 line 219) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 240 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844276782694400057` | unchanged (byte-identical to v13 line 221) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 242 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>` | unchanged (byte-identical to v13 line 223) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 243 | gmail.gmail_threads | UPDATE | `id=frederick.stone@harmonygames.co/1844276782694400053` | unchanged (byte-identical to v13 line 224) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 245 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>` | unchanged (byte-identical to v13 line 226) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 246 | gmail.gmail_threads | UPDATE | `id=leonard.hayes@harmonygames.co/1844276782694400055` | unchanged (byte-identical to v13 line 227) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 248 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>` | unchanged (byte-identical to v13 line 229) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 249 | gmail.gmail_threads | UPDATE | `id=robert@harmonygames.co/1844276782694400056` | unchanged (byte-identical to v13 line 230) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 251 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>` | unchanged (byte-identical to v13 line 232) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 252 | gmail.gmail_threads | UPDATE | `id=arthur.blake@harmonygames.co/1844276782694400057` | unchanged (byte-identical to v13 line 233) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 254 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>` | unchanged (byte-identical to v13 line 235) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 256 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843992534712320061` | unchanged (byte-identical to v13 line 237) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 258 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-2b67d1aa-cbdd-d816-22c3-d5ace6cf900b@google.com>` | unchanged (byte-identical to v13 line 239) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 260 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1843992534712320063` | unchanged (byte-identical to v13 line 241) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 262 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-c82c189b-c33c-a6e0-5e43-def7d943af26@google.com>` | unchanged (byte-identical to v13 line 243) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 264 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1843992534712320064` | unchanged (byte-identical to v13 line 245) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 266 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-44faeeb8-a4b0-dae2-c4eb-4d2fda67b29b@google.com>` | unchanged (byte-identical to v13 line 247) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 268 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843718101401600063` | unchanged (byte-identical to v13 line 249) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 270 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-2d8383e3-21d5-e958-783a-c960b5e98416@google.com>` | unchanged (byte-identical to v13 line 251) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 272 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1843718101401600065` | unchanged (byte-identical to v13 line 253) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 274 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-010d9a7c-8101-ee76-3333-bfb1ce826d3a@google.com>` | unchanged (byte-identical to v13 line 255) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 276 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1843718101401600066` | unchanged (byte-identical to v13 line 257) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 278 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-9d6c5aee-50ea-1d96-5cd0-dcef1de61254@google.com>` | unchanged (byte-identical to v13 line 259) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 280 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844620925337600069` | unchanged (byte-identical to v13 line 261) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 282 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-fb0024cc-3ec0-8309-fa11-9a9c8d3a1092@google.com>` | unchanged (byte-identical to v13 line 263) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 284 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844620925337600071` | unchanged (byte-identical to v13 line 265) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 286 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-34e4ed6d-59c6-2518-30fe-38f76d64f540@google.com>` | unchanged (byte-identical to v13 line 267) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 288 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844620925337600072` | unchanged (byte-identical to v13 line 269) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 290 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-b1816210-d8e8-b7e1-bec3-161d17c275ca@google.com>` | unchanged (byte-identical to v13 line 271) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 292 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844724105216000067` | unchanged (byte-identical to v13 line 273) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 294 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-297f69c9-ad63-fafd-14c3-70dbf78756f3@google.com>` | unchanged (byte-identical to v13 line 275) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 297 | gcal.gcal_events | INSERT | `evt_2f86b0d4c9e17a35b64e0d` | unchanged (byte-identical to v13 line 278) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 299 | gcal.gcal_events | INSERT | `evt_b511d4619c6f46ee63959b` | unchanged (byte-identical to v13 line 280) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 301 | gcal.gcal_events | INSERT | `evt_8bd5e929463b854ec0ad13` | unchanged (byte-identical to v13 line 282) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 303 | gcal.gcal_events | INSERT | `evt_ca908a712455521f1f8b43` | unchanged (byte-identical to v13 line 284) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 305 | gcal.gcal_events | INSERT | `evt_7d3e19b04a6c25f8e1b9a0` | unchanged (byte-identical to v13 line 286) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 307 | gcal.gcal_events | INSERT | `evt_99df25b554cac93e2926fd` | unchanged (byte-identical to v13 line 288) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 309 | gcal.gcal_events | INSERT | `evt_671dce00bcb85abb3e355e` | unchanged (byte-identical to v13 line 290) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 311 | gcal.gcal_events | INSERT | `evt_d65aa89778c3ebfa5d97b2` | unchanged (byte-identical to v13 line 292) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 313 | gcal.gcal_events | INSERT | `evt_9c41e7a2d05b38f6e1a7c4` | unchanged (byte-identical to v13 line 294) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 315 | gcal.gcal_events | INSERT | `evt_75d8a0687ea57b663a40b0` | unchanged (byte-identical to v13 line 296) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 317 | gcal.gcal_events | INSERT | `evt_6b2e94d0c17a3f58e9d2b1` | unchanged (byte-identical to v13 line 298) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 319 | gcal.gcal_events | INSERT | `evt_9ba121a353c889190ae6d2` | unchanged (byte-identical to v13 line 300) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 321 | gcal.gcal_events | INSERT | `evt_07843a430fe8e936bf3cda` | unchanged (byte-identical to v13 line 302) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 323 | gcal.gcal_events | INSERT | `evt_6aa4a42052090c05f4afe6` | unchanged (byte-identical to v13 line 304) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 326 | linear.linear_issues | INSERT | `ZOM-567` | unchanged (byte-identical to v13 line 307) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 328 | linear.linear_comments | INSERT | `lc_94eb35d962cfbdd31e1bd496` | unchanged (byte-identical to v13 line 309) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 330 | linear.linear_comments | INSERT | `lc_b549f3057640a5eb08f7581e` | unchanged (byte-identical to v13 line 311) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 333 | contacts.contacts | INSERT | `e3a91c07d5b48f26a0c7e314` | unchanged (byte-identical to v13 line 314) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 335 | contacts.contacts | INSERT | `b72f0d6e19c3a84e5d21f9a0` | unchanged (byte-identical to v13 line 316) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 337 | contacts.contacts | INSERT | `5d0e8b31f7a29c64e1b0d3a8` | unchanged (byte-identical to v13 line 318) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 339 | contacts.contacts | INSERT | `a4c2e9f07b31d85e6c0f1b29` | unchanged (byte-identical to v13 line 320) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |
| 340 | — | COMMIT | `—` | unchanged (byte-identical to v13 line 321) | REUSED (v13 ledger, chained to v12/v11/v10) + lint whole-script parse NEW | PASS |

Removed from v13 (no longer executed): v13 line 166 UPDATE `frederick.stone@…/1844610859008000037` snippet; v13 line 168 INSERT `frederick.stone@…/<CAA_lm07dfuR9zTKG5Xh1lma8QW1_dNi4pJJcvpJ@mail.gmail.com>`; v13 line 169 UPDATE `leonard.hayes@…/1844610859008000039` snippet (replaced by line 168 with new text); v13 line 171 INSERT `leonard.hayes@…/<CAA_lm07…>`. The earlier versions of lines 83, 108 and 110 are replaced by the rows above with the same keys.

Before/after for the UPDATEs that are new in v14:

- Line 168, `gmail.gmail_threads` `leonard.hayes@…/1844610859008000039` (inserted at 165): `snippet` nudge text → "Leonard, Sorry, I've thought about it more and I have to back out of this one…" (= line 170's snippet).
- Lines 179/182/185/188, `gmail.gmail_threads` base threads `…/1842283406259093714`, `…/1842282783388831849`, `…/1842283406290252813`, `…/1842283406345050279`: `snippet` → "Hi Karthic, Sorry about that, and thanks for flagging it…" (= the latest message, Arthur's 09-30 20:05Z answer). Only `snippet` changes; `history_id` is untouched.

## 6. Check A: records, references and IDs

- **New keys don't collide.** Slack `7fe55f30…` and the 9 new Gmail message rows (3 Message-IDs across their mailboxes): none exists in the complete base collections (§4), and every INSERT key in the SQL is unique.
- **References resolve.** The four base Bridge Round threads exist with the exact ids and mailboxes the SQL uses, and the parent message `<CAPBs_a4Nc7…>` is in each of them. Arthur's answer replies to Karthic's new message, inserted earlier in the script. Paul's reply targets the nudge in Leonard's thread (line 167). Slack reply `7fe55f30…` points at `4921f321…` (line 83, same channel, inserted just before). All UPDATE targets exist when they run.
- **One account per person.** Karthic uses the base token `PERSON_3242_EMAIL`, the same as in the base thread and the injected contact. Arthur and Leonard use their own harmonygames.co mailboxes and Slack ids. Paul keeps the single token `PERSON_9902_EMAIL`. No second account.
- **ID contracts.** No new Gmail thread rows; the UPDATEs don't touch `history_id`. No Drive `content_path` involved.
- **Byte-identical rows.** References, collisions, Drive readability and one account per person: reused PASS (§11).

## 7. Check B: SQL structure and supported schema rules

- One BEGIN/COMMIT block, 173 statements. Changed/added INSERTs have matching column and value counts (Slack 18/18; Gmail messages 22/22) and end with `;`. The new UPDATEs have valid `SET` lists and primary-key predicates. Escaped quotes (`Paul''s`, `can''t`, `it''s`) are balanced; E-strings carry `\r\n` as in the SQL's other Gmail bodies.
- JSON columns parse with the base shapes: Slack list columns and `metadata_json` `'{}'`; Gmail `label_ids_json`, `to_json`, `cc_json`, `bcc_json`, `reply_to_json`, `headers_json`, `attachments_meta_json` lists. `text_fts` and `body_text_fts` are not set. Lint `json_shape`, `missing_required` and `generated_column` found nothing.
- **Provisional snapshot comparison:** every column in the new or changed statements is in the snapshot and no NOT NULL column without a default is omitted: MATCH. The four uncovered columns from unchanged rows are as before (Advisory 1).

## 8. Check C: dates, relationships and consistency

- **Clock.** New event timestamps: Gmail 2025-09-30T10:20Z (Karthic), 14:55Z (Paul), 20:05Z (Arthur); Slack 2025-09-30T17:05Z (`1759251900.863415` = `created_at`). All before 2025-10-01T07:00Z. The latest event timestamp in the script is still 2025-09-30T23:48Z. `internal_date` equals `date` and the Date header for every new Gmail row.
- **Chronology.** Karthic (09-30 10:20Z) replies to Leonard's 09-22 17:40Z message, the latest in the thread; Arthur (20:05Z) answers after him. Paul (14:55Z = 7:55 AM PT) replies after the 09-29 nudge; Leonard's Slack "he wrote me this morning" (17:05Z = 10:05 AM PT) follows it the same morning. The Slack reply is 11 days after its 09-19 parent, which is fine.
- **Thread state.** #executives parent counters match its single reply. Gmail snippets equal each thread's latest message after the script (Arthur's answer in the four Bridge Round threads; Paul's reply in Leonard's SAFE thread; the nudge in Frederick's SAFE thread, which no longer gets Paul's reply). The nudge cc'd Frederick, and Paul answers Leonard only, so Frederick's copy correctly ends at the nudge.
- **Cross-record agreement.** The four copies of each new message are identical except mailbox fields. Karthic's message fits the base thread: Leonard sent a TestFlight invite and a Play internal-test link on 09-22. "iOS works, Android isn't available for my account" agrees with Arthur's answer (the tester list was never attached to the track), the re-worded Slack reply ("the 3 Dentsu folks still have no android access either … iOS is fine for all three") and Leonard's "so I can tell Ryo-san" (Karthic has already been answered by email). ZOM-567 says the Play adds landed (Sep 22 / Sep 26); the later email and Slack say the list wasn't attached. That's a later correction of an earlier log, not a structural contradiction. Paul's reversal supersedes the earlier sheet row and 09-19 post; nothing later says he is in.
- **Grader-facing text.** None. All new text is in-story correspondence.
- **Known issues.** No new record builds on a Snowflake or Confluence conflict. The SC-10 fix (line 31) is unchanged.
- **Byte-identical rows.** Clock, chronology and base agreement: reused PASS (§11).

## 9. Findings

No demonstrated defects. Advisories (don't block this stage):

1. **Columns not in the schema snapshot (Check B, provisional, unchanged).** `slides_pages.notes`, `slides_page_elements.table_json` and `.ordinal`, and `linear_comments.sequence` appear in neither the snapshot nor the base exports. If a platform table lacks any of them, that INSERT fails and the whole script rolls back. Smallest fix: drop those four columns and their values, or confirm the script loads on the platform.
2. **New external address for the Makers Fund guest (Check A/C, advisory, unchanged).** The Oct 8 invites use `PERSON_9905_EMAIL` for "Michael Cheung". The only base Makers Fund correspondent is `PERSON_3773_EMAIL` (`PERSON_3773_NAME`). No record says whether that is Michael Cheung, so this isn't a defect.
3. **Subject text in Robert's copy (Check C, cosmetic, new).** In Robert's base thread (`threads/00015209.json`) the subject reads "Bridge Round for Harmony Games?", while the other three mailboxes read "[SOURCE_ORG_0001]". Lines 176/187 use "[SOURCE_ORG_0001]" in Robert's copy too. Threading is by `thread_id`, so nothing breaks; this difference already exists in the base. Using "Re: Bridge Round for Harmony Games?" in Robert's two rows would match his thread exactly; it's optional.

The v13 Advisory 3 (Paul's "signed" claim with no Completed notice) no longer applies: that message was removed and Paul now backs out.

Notes for later stages (not injection findings): the Android-access correction now sits in three places (Karthic/Arthur email on the base Bridge Round thread, Arthur's Slack reply under the iOS-release post, and ZOM-567 saying the adds landed). Paul's status is now decided by his 09-30 email and Leonard's #executives thread reply, against the earlier sheet and post. Whether these are findable and settle the answer one way is for `/prompt` and `/hardness`.

## 10. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | New Slack and Gmail keys checked against complete base collections (610,468 Slack records; 81,404 Gmail thread files) and the SQL: 0 collisions. Base threads, parent Message-ID and UPDATE targets resolve. Authors are the right people/channel members; Karthic and Paul each use one token. Byte-identical rows reuse the v13 PASS. |
| B — SQL structure and supported schema rules | PASS | Column/value counts match. JSON valid with base shapes. Snapshot MATCH for new/changed columns; no generated columns set; no NOT NULL omissions. Four uncovered columns from unchanged rows remain advisory. Not live-certified. |
| C — Dates, relationships and consistency | PASS | New event timestamps before the clock. Replies follow parents. Slack counters and Gmail snippets match the new state. Removed rows leave no dangling references. No introduced contradiction; no grader-facing text. |

Outside certification scope (disclosed, not gates): live execution and current database compatibility (including the four columns), search ranking, Agent visibility and persona access, task difficulty.

## 11. Stage ownership and reuse

Reused evidence (stage-evidence-v1), from `Evals/task_inputs/reports/0_injection.md` as it stood before this rerun, SHA-256 `456d744230d01862cf8086313ab7c9b9ec01bb1a27de6538b06b0eba6cc2ad9c` (injection-static-v2, PASS/COMPLETE, SQL `c999829d…ecba`), which chained to the v12 (`a34c7de3…f885`), v11 (`ccd975b6…3a64`) and v10 reviews for rows unchanged then:

| Item | Source ledger / check | Dependencies verified unchanged |
|---|---|---|
| Checks A–C for the 155 statements byte-identical to v13 (ids/collisions, membership/identity, structure, JSON shapes, chronology, base agreement, Drive/Docs/Sheets/Slides/Slack/Trello/Linear/Gmail/Calendar/Contacts relationships, the line-31 SC-10 sheet fix, Slack parent `c891232a…` counters) | previous §4–§8, §11 | exact-content match of each statement to v13 (§5); universe manifest `da2f4cf0…aac1a`; Eval 0 `e034019b…`; schema snapshot `31dcb2b4…`; id_contracts `fc4711ef…`; lint `a8226e2a…`; roster `3f217451…`; acl `e9bca2b3…`; known issues `29b89d85…`; WORKFLOW `ee4cd8e1…`; clock 2025-10-01T07:00Z (all equal to the previous report) |
| Uniqueness of earlier new keys | previous §4/§6 | collections unchanged (same manifest); the v14 keys were checked separately against base and SQL (§4) |

`/prompt` may reuse these static checks only while all of these hold: SQL SHA-256 `75b6cb2ac45350d2560210daff4e96a3ff3982630259d8eadf94141524260fee`, universe manifest `da2f4cf0…aac1a`, schema snapshot `31dcb2b4…`, id_contracts `fc4711ef…`, Eval 0 `e034019b…`, clock 2025-10-01T07:00Z. `/prompt` still owns discoverability and persona access. This SQL changed, so earlier /prompt, /hardness, /oe and /rubric results are outdated; run /prompt, /hardness, /oe and /rubric again in that order.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt, then /hardness (with a fresh run on this SQL), /oe and /rubric. Advisories 1–3 are optional; any change makes a new SQL version that needs /injection again.

Evidence limits: Static review only. Live load, current database compatibility (including the four snapshot-uncovered columns), Agent visibility and difficulty are outside scope. The identity of the base Makers Fund correspondent `PERSON_3773` can't be determined from the records (Advisory 2).
