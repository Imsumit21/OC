# Injection Data-Integrity Review (Eval 0)

Review version: `injection-static-v2`
Evidence contract: `stage-evidence-v1`
Review time: 2026-11-02T18:13Z (actual)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Mode: chat review, attempt 6ae4e299a13034b7eb8305f8 (static, SQL not executed)

## 1. Scope and inputs

| Input | Value |
|---|---|
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` (input revision 20, from chat attachment `01_Universe_Inject (13).sql`), 167,876 bytes, SHA-256 `c999829d668e9731d7569acdcca1612f3d4ad2099f51515bbf0fdb8b5facecba`. Replaces `01_Universe_Inject (12).sql` (SHA `a34c7de3…f885`, last reviewed PASS/COMPLETE), so that report no longer applies. |
| Diff from the previous version | `diff` v12 → v13, 4 hunks: line 3 header comment ("143 INSERT, 12 UPDATE" → "145 INSERT, 15 UPDATE", matches the parse); line 106 Slack message `3cddf83c…` re-worded and turned from a top-level post (reply_count 1) into a thread reply under base message `c891232a…`; line 108 reply `301ad67f…` re-parented to `c891232a…`; line 109 new UPDATE of base parent `c891232a…` (reply counters); lines 166–171 new: Paul Heydon's reply "Re: SAFE in DocuSign" in Frederick's and Leonard's mailboxes plus two thread-snippet UPDATEs. Every other statement is byte-identical to v12 (155 of 162). |
| Assignment (context only) | Frederick Stone, Co-founder; not graded here |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Eval | `Evals/0_Injection_Quality_Eval.md` `e034019b8ec450437509a73dd3bae2d303b57561b0f67fcc1e5d19266f663eff` |
| Shared workflow | WORKFLOW `ee4cd8e1…cd5d` via `hg_reference.py guide injection --services slack gmail --tables slack.slack_messages gmail.gmail_threads gmail.gmail_messages` |
| Schema snapshot | `references/schema/injection.json` `31dcb2b43feca8e5…` (unverified, provisional) |
| ID contracts | `references/schema/id_contracts.json` `fc4711ef07667333…` |
| Lint | `hg_injection_lint.py` `a8226e2a69425355…`, version `injection-lint-v1` |
| Roster / ACL | roster.json `3f2174513f639e37…`, acl.md `e9bca2b35f98d5ef…` (identity checks only) |
| Known data issues | `guidelines/known_data_issues.md` `29b89d856c454124…` (SC-10 already resolved in the sheet by line 31, unchanged) |

Input/authority issues: none for this stage. SQL comments are evidence of intent only; none addresses a grader or mentions tool calls, pass rate or gates.

## 2. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, base manifest, review version | NEW, done (saved as input revision 20 before review) |
| Run lint; resolve every flag | NEW, done (0 FAIL, 0 CHECK, 0 INFO) |
| Inventory every statement and affected record | NEW, done: 162 statements (BEGIN, 145 INSERT, 15 UPDATE, COMMIT), ledger §5; each statement matched to v12 by exact content |
| Check A | NEW for the 7 changed/added statements; REUSED for 155 byte-identical rows (§11): PASS |
| Check B | NEW for changed/added statements and whole-script lint parse; REUSED for byte-identical rows: PASS (provisional snapshot advisory) |
| Check C | NEW for changed/added statements and the injected/base records they relate to; REUSED for byte-identical rows: PASS |
| Report coverage, findings, limits, one verdict | NEW, done |

## 3. Lint result

`hg_injection_lint.py` on SHA `c999829d…ecba`, universe synthcut, clock 2025-10-01T07:00Z. Base files loaded: contacts, slack users, trello, gmail users, linear, confluence. Rows parsed: 145 INSERT, 15 UPDATE (including gmail_threads 31 insert + 10 update; gmail_messages 41 insert; gcal_events 14; linear_issues 1; linear_comments 2; contacts 4).

Flags: **none** (FAIL 0, CHECK 0, INFO 0). Nothing to resolve. Checks A–C were still run in full.

## 4. Source coverage (new checks in this run)

| Check | Source / pointer | Coverage | Result |
|---|---|---|---|
| Slack thread parent `c891232a8b395a701268cff14cffd883` | slack `messages/C0880U9751A/2025-09.json` `/463` | `search-many` over all 9 channel files, scan complete, 0 errors | Exists once: ts `1759182908.627389` (2025-09-29T21:55:08Z), user `EMPLOYEE_0038_SLACK_ID`, text "I just released 0.3.49 on IOS", `thread_ts` null, `reply_count` 0, `reply_users_count` 0, `latest_reply` null. Its ts appears in no other record in the channel, so it has no base replies |
| Slack reply-counter convention | same file, every parent with `reply_count` > 0 (e.g. `1759211437.306779`: 4 replies by 0008/0016 → `reply_users_count` 2, `thread_ts` = own ts, `latest_reply` = last reply ts) | complete for 2025-09 | `reply_users_count` = distinct reply authors; parent's `thread_ts` = its own ts |
| Slack new/changed IDs `3cddf83c…`, `301ad67f…` | same 9 files | scan complete | 0 base matches; each appears once as an INSERT key in the SQL; no other SQL statement references `3cddf83c…` as a parent or UPDATE target |
| Channel membership | slack `channels.json`, `C0880U9751A` (`zombie-match3d`) | full record | `EMPLOYEE_0025_SLACK_ID` and `EMPLOYEE_0038_SLACK_ID` both members; channel not archived |
| Slack reply timestamps | lines 106, 108 | computed | `1759274400.518306` = 2025-09-30T23:20:00Z = `created_at`; `1759276080.094417` = 23:48:00Z = `created_at`; both after the parent (09-29 21:55Z) and before the clock |
| Linear log the Slack reply corrects | SQL lines 307–311 (`ZOM-567`, comments 09-30 17:25Z and 18:40Z) | full statements | Linear says "Play internal track added Sep 26 (investor tester list)" for Dentsu and "both added Sep 22" for T-Accelerate; the Slack reply (09-30 23:20Z, later) says the Play group was never attached. A later correction of an earlier log, not a structural contradiction |
| Gmail message ID `<CAA_lm07dfuR9zTKG5Xh1lma8QW1_dNi4pJJcvpJ@mail.gmail.com>` | `search-many` gmail `threads/*.json` | 81,404 files, scan complete, 0 errors | 0 base matches; used only for the two mailbox copies (lines 168, 171), each with a distinct `<mailbox>/<Message-ID>` key |
| Gmail threads `…/1844610859008000037`, `…/1844610859008000039` | same scan; SQL lines 159, 163 | complete | 0 base matches; both created earlier in this SQL (lines 159/163) before the UPDATEs at 166/169 |
| Paul Heydon / `PERSON_9902_EMAIL` | same scan ("Heydon", "PERSON_9902"); SQL lines 30, 83, 159–171 | complete | `PERSON_9902` in no base email. "Heydon" hits only inside 4 encoded tracking URLs (Cloudflare, Rippling), not a person. Within the SQL, Paul appears in the Bridge angels sheet (line 30, $50K "in", "docs via docusign next week"), the 09-19 #executives post (line 83) and the SAFE thread; one address token throughout |
| SAFE thread chronology | lines 161–171 | computed | Nudge 2025-09-29T15:00Z (`internal_date` 1759158000000); Paul's reply 2025-09-30T15:40Z (`internal_date` 1759246800000 = `date` = header "Tue, 30 Sep 2025 15:40:00 +0000"). "Signed it last night" = evening of 09-29 PT, after the nudge. `In-Reply-To`/`References` = the nudge's Message-ID; subject "Re: SAFE in DocuSign" |
| DocuSign "Completed" notices | SQL line 157 (Anton only); base gmail (0 `PERSON_9902` hits) | complete | No Completed notice for Paul exists anywhere. The SQL's #executives rule (line 87, 09-26) says a new investor counts only once the Completed notice is in, "them telling us they're in doesn't count" (Advisory 3) |
| Reply-chain convention | other injected replies (lines 196–207, 224–235) | full statements | Same pattern: message inserted per mailbox with In-Reply-To/References headers and columns, thread snippet updated to the latest message |
| Reused coverage | previous report §4–§8, §11 (all byte-identical rows) | see §11 | unchanged |

## 5. Operation ledger

Every statement in execution order (current SQL line numbers; for multi-line INSERTs, the VALUES line). Rows marked NEW were verified fresh (§4, §6–§8). Byte-identical rows reuse the v12 ledger (which chains to v11 and v10), with their v12 line given. The whole script was re-parsed by the lint in this run.

| SQL line | Table | Op | Record / target | Change vs v12 | Verification | Result |
|---|---|---|---|---|---|---|
| 5 | — | BEGIN | `—` | unchanged (byte-identical to v12 line 5) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 8 | gdrive.drive_files | INSERT | `f_8d2c47a91e05b3f6d7c418` | unchanged (byte-identical to v12 line 8) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 10 | gdrive.drive_files | INSERT | `f_3b9e61c04d7a52e8f1a6c2` | unchanged (byte-identical to v12 line 10) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 12 | gdrive.drive_files | INSERT | `d_5e8a1c3f9b07d2e64a1b93` | unchanged (byte-identical to v12 line 12) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 14 | gdrive.drive_files | INSERT | `f_c61a0e93b7d24f58a2e917` | unchanged (byte-identical to v12 line 14) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 16 | gdrive.drive_files | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 16) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 18 | gdrive.drive_files | INSERT | `f_6e1d93a0c4b72f85d39a0e` | unchanged (byte-identical to v12 line 18) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 21 | gdocs.docs_documents | INSERT | `f_8d2c47a91e05b3f6d7c418` | unchanged (byte-identical to v12 line 21) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 23 | gdocs.docs_documents | INSERT | `f_3b9e61c04d7a52e8f1a6c2` | unchanged (byte-identical to v12 line 23) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 25 | gdocs.docs_documents | INSERT | `f_c61a0e93b7d24f58a2e917` | unchanged (byte-identical to v12 line 25) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 28 | gsheets.sheets_spreadsheets | INSERT | `f_6e1d93a0c4b72f85d39a0e` | unchanged (byte-identical to v12 line 28) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 30 | gsheets.sheets_sheets | INSERT | `f_6e1d93a0c4b72f85d39a0e` | unchanged (byte-identical to v12 line 30) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 31 | gsheets.sheets_sheets | UPDATE | `spreadsheet_id=f_48247af79428823c3cac92` | unchanged (byte-identical to v12 line 31) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 34 | gslides.slides_presentations | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 34) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 36 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 36) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 38 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 38) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 40 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 40) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 42 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 42) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 44 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 44) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 46 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 46) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 48 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 48) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 50 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 50) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 52 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 52) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 54 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 54) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 56 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 56) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 58 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 58) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 60 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 60) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 62 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 62) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 64 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 64) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 66 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 66) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 68 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 68) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 70 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 70) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 72 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 72) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 74 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 74) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 76 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 76) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 78 | gslides.slides_pages | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 78) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 80 | gslides.slides_page_elements | INSERT | `f_a47d0e2c95b18f63e2c0d5` | unchanged (byte-identical to v12 line 80) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 83 | slack.slack_messages | INSERT | `4921f321db5d08f936aac24a6a1d2af8` | unchanged (byte-identical to v12 line 83) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 85 | slack.slack_messages | INSERT | `7fef94264090696760180223fc8265e7` | unchanged (byte-identical to v12 line 85) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 87 | slack.slack_messages | INSERT | `20924cc7f5176991d8a97a8eafb291d0` | unchanged (byte-identical to v12 line 87) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 89 | slack.slack_messages | INSERT | `19e1e65d5952f075e8492867c6bcd472` | unchanged (byte-identical to v12 line 89) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 91 | slack.slack_messages | INSERT | `800870c56bda852a57dfa06cb4fd63e6` | unchanged (byte-identical to v12 line 91) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 93 | slack.slack_messages | INSERT | `1a68c2da0f36fc25489d3d9bbe9ccc32` | unchanged (byte-identical to v12 line 93) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 95 | slack.slack_messages | INSERT | `c183280a284440a6ca6cdbb5270c9139` | unchanged (byte-identical to v12 line 95) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 97 | slack.slack_messages | INSERT | `398502c0596e5347cc297f61eaefbd50` | unchanged (byte-identical to v12 line 97) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 99 | slack.slack_messages | INSERT | `229090ba6b316b667d1a6451b0297a47` | unchanged (byte-identical to v12 line 99) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 100 | slack.slack_messages | UPDATE | `id=99aa913348bb05e6eda8daa06d37fc2a` | unchanged (byte-identical to v12 line 100) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 102 | slack.slack_messages | INSERT | `99b22482ddd77dd01b451afb39014839` | unchanged (byte-identical to v12 line 102) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 104 | slack.slack_messages | INSERT | `f7261dd1b05eb2da3b81fe7d8cde2854` | unchanged (byte-identical to v12 line 104) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 106 | slack.slack_messages | INSERT | `3cddf83c394676d8b72c0c20ed58f520` | **changed/added in v13** | NEW (§4, §6–§8) | PASS |
| 108 | slack.slack_messages | INSERT | `301ad67f082965686f35a9484aa25b0a` | **changed/added in v13** | NEW (§4, §6–§8) | PASS |
| 109 | slack.slack_messages | UPDATE | `id=c891232a8b395a701268cff14cffd883` | **changed/added in v13** | NEW (§4, §6–§8) | PASS |
| 112 | trello.trello_actions | INSERT | `68c64270d660c977c4696986` | unchanged (byte-identical to v12 line 111) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 114 | trello.trello_actions | INSERT | `68db03b86054eff7e8e92474` | unchanged (byte-identical to v12 line 113) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 115 | trello.trello_cards | UPDATE | `id=68c5a49e8491a9d7faf869d0` | unchanged (byte-identical to v12 line 114) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 117 | trello.trello_cards | INSERT | `68c99e98737744bd966aed24` | unchanged (byte-identical to v12 line 116) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 119 | trello.trello_actions | INSERT | `68c99e98647b81be91f207f2` | unchanged (byte-identical to v12 line 118) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 120 | trello.trello_boards | UPDATE | `id=640643a3fd8f3ca308d9318e` | unchanged (byte-identical to v12 line 119) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 123 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844623441920000059` | unchanged (byte-identical to v12 line 122) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 125 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.com>` | unchanged (byte-identical to v12 line 124) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 127 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844623441920000061` | unchanged (byte-identical to v12 line 126) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 129 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.com>` | unchanged (byte-identical to v12 line 128) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 131 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844623441920000062` | unchanged (byte-identical to v12 line 130) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 133 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.com>` | unchanged (byte-identical to v12 line 132) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 135 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844724419788800011` | unchanged (byte-identical to v12 line 134) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 137 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>` | unchanged (byte-identical to v12 line 136) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 139 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844724419788800013` | unchanged (byte-identical to v12 line 138) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 141 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>` | unchanged (byte-identical to v12 line 140) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 143 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844724419788800014` | unchanged (byte-identical to v12 line 142) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 145 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>` | unchanged (byte-identical to v12 line 144) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 147 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844724419788800015` | unchanged (byte-identical to v12 line 146) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 149 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>` | unchanged (byte-identical to v12 line 148) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 151 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844162278195200024` | unchanged (byte-identical to v12 line 150) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 153 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CACJhvEE55qdWXuKC3BWlscoxBKrLUWavLQ3cpTJ@mail.gmail.com>` | unchanged (byte-identical to v12 line 152) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 155 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844354293432320031` | unchanged (byte-identical to v12 line 154) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 157 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAiKDPIoVSAFUBccUSRRBTi6dsmJdhof2EzteoIx@mail.gmail.com>` | unchanged (byte-identical to v12 line 156) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 159 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844610859008000037` | unchanged (byte-identical to v12 line 158) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 161 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAP6Gn2LV490e3El5rBDCgCItvhOdc7S6Wpb8nNq@mail.gmail.com>` | unchanged (byte-identical to v12 line 160) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 163 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844610859008000039` | unchanged (byte-identical to v12 line 162) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 165 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAP6Gn2LV490e3El5rBDCgCItvhOdc7S6Wpb8nNq@mail.gmail.com>` | unchanged (byte-identical to v12 line 164) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 166 | gmail.gmail_threads | UPDATE | `id=frederick.stone@harmonygames.co/1844610859008000037` | **changed/added in v13** | NEW (§4, §6–§8) | PASS |
| 168 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAA_lm07dfuR9zTKG5Xh1lma8QW1_dNi4pJJcvpJ@mail.gmail.com>` | **changed/added in v13** | NEW (§4, §6–§8) | PASS |
| 169 | gmail.gmail_threads | UPDATE | `id=leonard.hayes@harmonygames.co/1844610859008000039` | **changed/added in v13** | NEW (§4, §6–§8) | PASS |
| 171 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAA_lm07dfuR9zTKG5Xh1lma8QW1_dNi4pJJcvpJ@mail.gmail.com>` | **changed/added in v13** | NEW (§4, §6–§8) | PASS |
| 173 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844318935449600041` | unchanged (byte-identical to v12 line 166) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 175 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_lp6f26Gm0Vi7deiv8pmy@mail.gmail.com>` | unchanged (byte-identical to v12 line 168) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 177 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844318935449600043` | unchanged (byte-identical to v12 line 170) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 179 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_lp6f26Gm0Vi7deiv8pmy@mail.gmail.com>` | unchanged (byte-identical to v12 line 172) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 181 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844294398771200045` | unchanged (byte-identical to v12 line 174) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 183 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@mail.gmail.com>` | unchanged (byte-identical to v12 line 176) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 185 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844294398771200047` | unchanged (byte-identical to v12 line 178) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 187 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@mail.gmail.com>` | unchanged (byte-identical to v12 line 180) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 189 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844294398771200048` | unchanged (byte-identical to v12 line 182) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 191 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@mail.gmail.com>` | unchanged (byte-identical to v12 line 184) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 193 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844294398771200049` | unchanged (byte-identical to v12 line 186) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 195 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@mail.gmail.com>` | unchanged (byte-identical to v12 line 188) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 196 | gmail.gmail_threads | UPDATE | `id=frederick.stone@harmonygames.co/1844294398771200045` | unchanged (byte-identical to v12 line 189) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 198 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>` | unchanged (byte-identical to v12 line 191) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 199 | gmail.gmail_threads | UPDATE | `id=leonard.hayes@harmonygames.co/1844294398771200047` | unchanged (byte-identical to v12 line 192) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 201 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>` | unchanged (byte-identical to v12 line 194) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 202 | gmail.gmail_threads | UPDATE | `id=robert@harmonygames.co/1844294398771200048` | unchanged (byte-identical to v12 line 195) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 204 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>` | unchanged (byte-identical to v12 line 197) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 205 | gmail.gmail_threads | UPDATE | `id=arthur.blake@harmonygames.co/1844294398771200049` | unchanged (byte-identical to v12 line 198) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 207 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>` | unchanged (byte-identical to v12 line 200) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 209 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844276782694400053` | unchanged (byte-identical to v12 line 202) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 211 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>` | unchanged (byte-identical to v12 line 204) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 213 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844276782694400055` | unchanged (byte-identical to v12 line 206) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 215 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>` | unchanged (byte-identical to v12 line 208) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 217 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844276782694400056` | unchanged (byte-identical to v12 line 210) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 219 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>` | unchanged (byte-identical to v12 line 212) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 221 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844276782694400057` | unchanged (byte-identical to v12 line 214) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 223 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>` | unchanged (byte-identical to v12 line 216) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 224 | gmail.gmail_threads | UPDATE | `id=frederick.stone@harmonygames.co/1844276782694400053` | unchanged (byte-identical to v12 line 217) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 226 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>` | unchanged (byte-identical to v12 line 219) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 227 | gmail.gmail_threads | UPDATE | `id=leonard.hayes@harmonygames.co/1844276782694400055` | unchanged (byte-identical to v12 line 220) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 229 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>` | unchanged (byte-identical to v12 line 222) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 230 | gmail.gmail_threads | UPDATE | `id=robert@harmonygames.co/1844276782694400056` | unchanged (byte-identical to v12 line 223) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 232 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>` | unchanged (byte-identical to v12 line 225) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 233 | gmail.gmail_threads | UPDATE | `id=arthur.blake@harmonygames.co/1844276782694400057` | unchanged (byte-identical to v12 line 226) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 235 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>` | unchanged (byte-identical to v12 line 228) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 237 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843992534712320061` | unchanged (byte-identical to v12 line 230) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 239 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-2b67d1aa-cbdd-d816-22c3-d5ace6cf900b@google.com>` | unchanged (byte-identical to v12 line 232) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 241 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1843992534712320063` | unchanged (byte-identical to v12 line 234) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 243 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-c82c189b-c33c-a6e0-5e43-def7d943af26@google.com>` | unchanged (byte-identical to v12 line 236) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 245 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1843992534712320064` | unchanged (byte-identical to v12 line 238) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 247 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-44faeeb8-a4b0-dae2-c4eb-4d2fda67b29b@google.com>` | unchanged (byte-identical to v12 line 240) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 249 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843718101401600063` | unchanged (byte-identical to v12 line 242) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 251 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-2d8383e3-21d5-e958-783a-c960b5e98416@google.com>` | unchanged (byte-identical to v12 line 244) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 253 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1843718101401600065` | unchanged (byte-identical to v12 line 246) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 255 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-010d9a7c-8101-ee76-3333-bfb1ce826d3a@google.com>` | unchanged (byte-identical to v12 line 248) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 257 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1843718101401600066` | unchanged (byte-identical to v12 line 250) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 259 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-9d6c5aee-50ea-1d96-5cd0-dcef1de61254@google.com>` | unchanged (byte-identical to v12 line 252) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 261 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844620925337600069` | unchanged (byte-identical to v12 line 254) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 263 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-fb0024cc-3ec0-8309-fa11-9a9c8d3a1092@google.com>` | unchanged (byte-identical to v12 line 256) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 265 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844620925337600071` | unchanged (byte-identical to v12 line 258) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 267 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-34e4ed6d-59c6-2518-30fe-38f76d64f540@google.com>` | unchanged (byte-identical to v12 line 260) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 269 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844620925337600072` | unchanged (byte-identical to v12 line 262) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 271 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-b1816210-d8e8-b7e1-bec3-161d17c275ca@google.com>` | unchanged (byte-identical to v12 line 264) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 273 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844724105216000067` | unchanged (byte-identical to v12 line 266) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 275 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-297f69c9-ad63-fafd-14c3-70dbf78756f3@google.com>` | unchanged (byte-identical to v12 line 268) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 278 | gcal.gcal_events | INSERT | `evt_2f86b0d4c9e17a35b64e0d` | unchanged (byte-identical to v12 line 271) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 280 | gcal.gcal_events | INSERT | `evt_b511d4619c6f46ee63959b` | unchanged (byte-identical to v12 line 273) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 282 | gcal.gcal_events | INSERT | `evt_8bd5e929463b854ec0ad13` | unchanged (byte-identical to v12 line 275) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 284 | gcal.gcal_events | INSERT | `evt_ca908a712455521f1f8b43` | unchanged (byte-identical to v12 line 277) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 286 | gcal.gcal_events | INSERT | `evt_7d3e19b04a6c25f8e1b9a0` | unchanged (byte-identical to v12 line 279) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 288 | gcal.gcal_events | INSERT | `evt_99df25b554cac93e2926fd` | unchanged (byte-identical to v12 line 281) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 290 | gcal.gcal_events | INSERT | `evt_671dce00bcb85abb3e355e` | unchanged (byte-identical to v12 line 283) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 292 | gcal.gcal_events | INSERT | `evt_d65aa89778c3ebfa5d97b2` | unchanged (byte-identical to v12 line 285) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 294 | gcal.gcal_events | INSERT | `evt_9c41e7a2d05b38f6e1a7c4` | unchanged (byte-identical to v12 line 287) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 296 | gcal.gcal_events | INSERT | `evt_75d8a0687ea57b663a40b0` | unchanged (byte-identical to v12 line 289) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 298 | gcal.gcal_events | INSERT | `evt_6b2e94d0c17a3f58e9d2b1` | unchanged (byte-identical to v12 line 291) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 300 | gcal.gcal_events | INSERT | `evt_9ba121a353c889190ae6d2` | unchanged (byte-identical to v12 line 293) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 302 | gcal.gcal_events | INSERT | `evt_07843a430fe8e936bf3cda` | unchanged (byte-identical to v12 line 295) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 304 | gcal.gcal_events | INSERT | `evt_6aa4a42052090c05f4afe6` | unchanged (byte-identical to v12 line 297) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 307 | linear.linear_issues | INSERT | `ZOM-567` | unchanged (byte-identical to v12 line 300) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 309 | linear.linear_comments | INSERT | `lc_94eb35d962cfbdd31e1bd496` | unchanged (byte-identical to v12 line 302) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 311 | linear.linear_comments | INSERT | `lc_b549f3057640a5eb08f7581e` | unchanged (byte-identical to v12 line 304) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 314 | contacts.contacts | INSERT | `e3a91c07d5b48f26a0c7e314` | unchanged (byte-identical to v12 line 307) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 316 | contacts.contacts | INSERT | `b72f0d6e19c3a84e5d21f9a0` | unchanged (byte-identical to v12 line 309) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 318 | contacts.contacts | INSERT | `5d0e8b31f7a29c64e1b0d3a8` | unchanged (byte-identical to v12 line 311) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 320 | contacts.contacts | INSERT | `a4c2e9f07b31d85e6c0f1b29` | unchanged (byte-identical to v12 line 313) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |
| 321 | — | COMMIT | `—` | unchanged (byte-identical to v12 line 314) | REUSED (v12 ledger, chained to v11/v10) + lint whole-script parse NEW | PASS |

Before/after for the UPDATEs that are new in v13:

- Line 109, `slack.slack_messages` `c891232a…` (base): `reply_count` 0 → 2, `reply_users_count` 0 → 2 (authors 0025, 0038), `latest_reply` null → `1759276080.094417` (= line 108's ts), `thread_ts_legacy` null → `1759182908.627389` (= own ts).
- Lines 166/169, `gmail.gmail_threads` `…/1844610859008000037`, `…/1844610859008000039` (inserted at 159/163): `snippet` nudge text → "Leonard, Done, signed it last night. Excited to be part of this! Paul" (= the new latest message's snippet).

## 6. Check A: records, references and IDs

- **New keys don't collide.** Slack messages `3cddf83c…` and `301ad67f…` (re-written, same keys as v12) and the two new Gmail message rows: none exists in the complete base collections (§4), and each appears exactly once among the SQL's inserts.
- **References resolve.** Thread parent `c891232a…` is a base message in the same channel `C0880U9751A` with no base replies. The UPDATE targets (line 109 base Slack row; lines 166/169 threads inserted earlier at 159/163) exist at the time they run. Both Gmail rows sit in existing mailboxes (Frederick, Leonard), in threads of the same mailbox.
- **One account per person.** Authors `EMPLOYEE_0025_SLACK_ID` and `EMPLOYEE_0038_SLACK_ID` are existing channel members; no new internal account. `PERSON_9902_EMAIL` is the one token used for Paul Heydon across the whole SQL, and no base record names him, so there's no second address for an existing person.
- **ID contracts.** No new Gmail thread (the UPDATEs leave `history_id` untouched, NULL). No Drive `content_path` involved.
- **Byte-identical rows.** References, collisions, Drive readability and one account per person: reused PASS (§11).

## 7. Check B: SQL structure and supported schema rules

- One BEGIN/COMMIT block, 162 statements. Changed/added INSERTs have matching column and value counts (Slack 18/18 at lines 106 and 108; Gmail messages 22/22 at 168 and 171) and end with `;`. The three new UPDATEs have valid `SET` lists and primary-key predicates.
- JSON columns parse with the base shapes: Slack `reactions_json`/`files_json`/`attachments_json` lists and `metadata_json` `'{}'` (object); Gmail `label_ids_json`, `to_json`, `cc_json`, `bcc_json`, `reply_to_json`, `headers_json`, `attachments_meta_json` lists. `text_fts` and `body_text_fts` are not set. Lint `json_shape`, `missing_required` and `generated_column` found nothing.
- **Provisional snapshot comparison:** every column in the new or changed statements is in the snapshot, and no NOT NULL column without a default is omitted (Slack `reply_count`, `reply_users_count`, `is_activity_message`, `reactions_json`, `files_json`, `attachments_json`, `created_at`, `metadata_json` all given): MATCH. The four uncovered columns from unchanged rows are as before (Advisory 1).

## 8. Check C: dates, relationships and consistency

- **Clock.** New event timestamps: Slack 2025-09-30T23:20Z and 23:48Z; Gmail 2025-09-30T15:40Z. All at or before 2025-10-01T07:00Z. The latest event timestamp in the script is still 2025-09-30T23:48Z.
- **Chronology.** Both Slack replies follow their parent (09-29 21:55Z) and each other. Paul's reply (09-30 15:40Z) follows the nudge (09-29 15:00Z). The Slack correction (09-30 23:20Z) comes after the Linear log entries it contradicts (09-30 17:25Z/18:40Z).
- **Thread state.** Parent counters after the SQL match the replies: 2 replies, 2 distinct authors, `latest_reply` = last reply ts, `thread_ts_legacy` = parent ts, the base convention (§4). The former parent state of `3cddf83c…` (v12: `reply_count` 1, `latest_reply` set) is gone and it is now a plain reply (`reply_count` 0, `latest_reply` NULL), so no orphaned counter remains. Thread snippets equal the latest message's snippet, as in the SQL's other reply chains.
- **Cross-record agreement.** Paul's two mailbox copies are identical except mailbox fields; labels fit each mailbox (INBOX for both, as recipient and CC). The re-worded Slack text keeps the same facts as v12 (Karthic plus 3 Dentsu testers lack Android, iOS fine, fix with tomorrow's push) and still fits ZOM-567's tester list. Paul's claim that he signed doesn't contradict any record: no record says his envelope was voided, declined or still pending after 09-30 15:40Z (Advisory 3).
- **Grader-facing text.** None. "whatever the Linear log says" and "signed it last night" are in-story statements between personas.
- **Known issues.** No new record builds on a Snowflake or Confluence conflict. The SC-10 fix (line 31) is unchanged.
- **Byte-identical rows.** Clock, chronology and base agreement: reused PASS (§11).

## 9. Findings

No demonstrated defects. Advisories (don't block this stage):

1. **Columns not in the schema snapshot (Check B, provisional, unchanged).** `slides_pages.notes`, `slides_page_elements.table_json` and `.ordinal`, and `linear_comments.sequence` appear in neither the snapshot nor the base exports. If a platform table lacks any of them, that INSERT fails and the whole script rolls back. Smallest fix: drop those four columns and their values, or confirm the script loads on the platform.
2. **New external address for the Makers Fund guest (Check A/C, advisory, unchanged).** The Oct 8 invites use `PERSON_9905_EMAIL` for "Michael Cheung". The only base Makers Fund correspondent is `PERSON_3773_EMAIL` (`PERSON_3773_NAME`), whom Leonard emailed 2025-09-03. No record says whether that is Michael Cheung, so this isn't a defect. Using `PERSON_3773_EMAIL` would tie the meeting to the base thread.
3. **Paul's "signed" claim with no Completed notice (Check C, advisory, new).** Line 168/171: Paul says on 09-30 15:40Z "Done, signed it last night". No DocuSign Completed notice for him exists in the SQL or base, while Anton's Completed notice (line 157, 09-26 19:02Z) arrived the same day Leonard reported his signing (line 104). Under the #executives rule (line 87) Paul is therefore not yet a new investor. That is consistent (an envelope can await another signer, or Paul may be mistaken), and the records never contradict it, so it's no defect. If you want the reason to be explicit, a line saying the envelope is still waiting (for example a DocuSign reminder or a note from Leonard) would remove any doubt; it's optional.

Notes for later stages (not injection findings): the Android-access correction is now a thread reply under an iOS-release post (`c891232a…`) rather than a top-level message, and it no longer names ZOM-567 ("whatever the Linear log says"). Paul's reply is a claim-vs-record trap against the line-87 rule. Whether these are findable and settle the answer one way is for `/prompt` and `/hardness`.

## 10. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | New Slack and Gmail keys checked against complete base collections and the SQL: 0 collisions. Thread parent `c891232a…` and UPDATE targets resolve. Authors are channel members; Paul uses one token. Byte-identical rows reuse the v12 PASS. |
| B — SQL structure and supported schema rules | PASS | Column/value counts match. JSON valid with base shapes. Snapshot MATCH for new/changed columns; no generated columns set; no NOT NULL omissions. Four uncovered columns from unchanged rows remain advisory. Not live-certified. |
| C — Dates, relationships and consistency | PASS | New event timestamps at or before the clock. Replies follow parents. Slack thread counters and Gmail snippets match the new state. No introduced contradiction; no grader-facing text. |

Outside certification scope (disclosed, not gates): live execution and current database compatibility (including the four columns), search ranking, Agent visibility and persona access, task difficulty.

## 11. Stage ownership and reuse

Reused evidence (stage-evidence-v1), from `Evals/task_inputs/reports/0_injection.md` as it stood before this rerun, SHA-256 `857c0163a41d781bd3449acf3e17e2e69d6215ba8cb4b4f978b17ab9ec532da8` (injection-static-v2, PASS/COMPLETE, SQL `a34c7de3…f885`), which chained to the v11 (`ccd975b6…3a64`) and v10 reviews for rows unchanged then:

| Item | Source ledger / check | Dependencies verified unchanged |
|---|---|---|
| Checks A–C for the 155 statements byte-identical to v12 (ids/collisions, membership/identity, structure, JSON shapes, chronology, base agreement, Drive/Docs/Sheets/Slides/Slack/Trello/Linear/Gmail/Calendar/Contacts relationships, the line-31 SC-10 sheet fix) | previous §4–§8, §11 | exact-content match of each statement to v12 (§5); universe manifest `da2f4cf0…aac1a`; Eval 0 `e034019b…`; schema snapshot `31dcb2b4…`; id_contracts `fc4711ef…`; lint `a8226e2a…`; roster `3f217451…`; acl `e9bca2b3…`; known issues `29b89d85…`; WORKFLOW `ee4cd8e1…`; clock 2025-10-01T07:00Z (all equal to the previous report) |
| Uniqueness of earlier new keys | previous §4/§6 | collections unchanged (same manifest); the v13 keys were checked separately against base and SQL (§4) |

`/prompt` may reuse these static checks only while all of these hold: SQL SHA-256 `c999829d668e9731d7569acdcca1612f3d4ad2099f51515bbf0fdb8b5facecba`, universe manifest `da2f4cf0…aac1a`, schema snapshot `31dcb2b4…`, id_contracts `fc4711ef…`, Eval 0 `e034019b…`, clock 2025-10-01T07:00Z. `/prompt` still owns discoverability and persona access. This SQL changed, so earlier /prompt, /hardness, /oe and /rubric results are outdated; run /prompt, /hardness, /oe and /rubric again in that order.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt, then /hardness (with a fresh run on this SQL), /oe and /rubric. Advisories 1–3 are optional; any change makes a new SQL version that needs /injection again.

Evidence limits: Static review only. Live load, current database compatibility (including the four snapshot-uncovered columns), Agent visibility and difficulty are outside scope. The identity of the base Makers Fund correspondent `PERSON_3773` can't be determined from the records (Advisory 2).
