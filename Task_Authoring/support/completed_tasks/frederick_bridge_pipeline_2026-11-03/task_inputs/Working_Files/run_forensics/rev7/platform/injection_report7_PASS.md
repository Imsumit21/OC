# Injection Data-Integrity Review (Eval 0)

Review version: `injection-static-v2`
Evidence contract: `stage-evidence-v1`
Review time: 2026-11-02T11:54Z (actual)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Mode: chat review, attempt 6ae4e299a13034b7eb8305f8 (static, SQL not executed)

## 1. Scope and inputs

| Input | Value |
|---|---|
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` (input revision 12, from chat attachment `01_Universe_Inject (10).sql`), 126,369 bytes, SHA-256 `efe3cab14874d1daa3ba71900a44a4536537fe46eae947167649ae2032c9c881`. Replaces `01_Universe_Inject (9).sql` (SHA `84818944…cc0be`, last reviewed PASS), so that report no longer applies. |
| Diff from the previous version | Header count 150 → 130 INSERT (11 UPDATE unchanged); header matches the parsed SQL. **Theme renamed from the Oct 14 board pre-read to a Q4 investor update send list**: 5 Drive names, 3 Doc titles/bodies (with re-indexed style runs), the deck title and 15 slide texts. **Removed (20 rows):** 4 slides and their 8 elements (Fundraising, Asks, Appendix, old Thank-you; the deck now has 8 slides, indices 0–7) and the injected Trello card `68d8193c…` with its createCard action, checklist, 4 check items and 2 more actions. **Added (1):** Leonard's #executives note `20924cc7…` (what counts as a new investor). **Changed:** Arthur's #executives text `7fef9426…`; the Trello comment on base card 455 (text only); the board UPDATE's `dateLastActivity` (09-27 → 09-14); Robert's and Leonard's emails (subject, body, snippet, headers) in all copies; Fred's Oct 6 invite email and both gcal rows (now 2pm–2:45pm PT). Every other row is byte-identical to v9. |
| Assignment (context only) | Frederick Stone, Co-founder; not graded here |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Eval | `Evals/0_Injection_Quality_Eval.md` `e034019b8ec450437509a73dd3bae2d303b57561b0f67fcc1e5d19266f663eff` |
| Shared workflow | `hg_reference.py guide injection` (WORKFLOW `ee4cd8e1…`), trello/slack/gcal routes, schema entries for linear_comments, slides_pages, slides_page_elements |
| Schema snapshot | `references/schema/injection.json` `31dcb2b43feca8e5…` (unverified, provisional) |
| ID contracts | `references/schema/id_contracts.json` `fc4711ef07667333…` |
| Lint | `hg_injection_lint.py` `a8226e2a69425355…`, version `injection-lint-v1` |
| Roster / ACL | roster.json `3f2174513f639e37…`, acl.md `e9bca2b35f98d5ef…` (identity checks only) |

Input/authority issues: none for this stage. SQL comment lines (1–4 and section banners) are evidence of intent only; none addresses a grader or mentions tool calls, pass rate or gates. Note for later stages (not an injection finding): the saved prompt still names the "Oct 14 board pre-read", the "Board - Oct 14 2025 folder" and "the numbers he needs for the slide", which no longer exist in this SQL. `/prompt` owns that.

## 2. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, base manifest, review version | NEW, done (saved as input revision 12 before review) |
| Run lint; resolve every flag | NEW, done (0 FAIL, 0 CHECK, 0 INFO) |
| Inventory every statement and affected record | NEW, done: 143 statements (BEGIN, 130 INSERT, 11 UPDATE, COMMIT), ledger §5; 20 removed rows listed in §1 |
| Check A | NEW for changed/added rows, REUSED for byte-identical rows (§11): PASS |
| Check B | NEW (whole script): PASS (provisional snapshot advisory) |
| Check C | NEW for changed/added rows and for every cross-reference into removed rows, REUSED for byte-identical rows: PASS |
| Report coverage, findings, limits, one verdict | NEW, done |

Independent static parse of all 143 statements (whole script, fresh): column/value counts match on every INSERT; every `*_json` value parses; no `_fts` column set; no duplicate primary keys within the SQL; Slack `ts` = `created_at` on all 13 messages and `metadata_json = '{}'`; no event timestamp after the clock (latest 2025-09-30T23:48Z; only gcal start/end on Oct 6 are later, as plan fields); Gmail: `snippet` = body prefix, `internal_date` = `date` = Date header, Subject header = `subject`, To/Cc headers = `to_json`/`cc_json` on all 36 messages; all 28 thread snippets equal their latest message's snippet (including the 8 UPDATEs); thread id >> 20 = first message `internal_date` on all 28; copies of the same Message-ID agree on subject, body, date, sender, recipients and snippet across mailboxes; Doc style runs contiguous and ending at `len(body_text)` on all 3 Docs; Drive name = Doc/Sheet/Slides title on all 5 files.

## 3. Lint result

`hg_injection_lint.py` on SHA `efe3cab1…c881`, universe synthcut, clock 2025-10-01T07:00Z. Base files loaded: contacts, slack users, trello, gmail users, linear, confluence. Rows parsed: 130 INSERT, 11 UPDATE across 17 tables.

Flags: **none** (FAIL 0, CHECK 0, INFO 0). Nothing to resolve. Checks A–C were still run in full.

## 4. Source coverage (new checks in this run)

| Check | Source / pointer | Coverage | Result |
|---|---|---|---|
| New Slack id `20924cc7f5176991d8a97a8eafb291d0` | `lookup slack --file 'messages/*.json'` | 4,840 files, 610,468 messages, scan complete, 0 errors | 0 matches |
| Slack ts `1758911700.336170` | `slack/messages/C07C2866011/2025-09.json` read in full (1,197 messages) | complete for the channel-month | not present; no base message at that second. Same-day and Sep 19/29 #executives context read: nothing about SAFEs, DocuSign or the Q4 update that conflicts |
| Trello base card `68c5a49e8491a9d7faf869d0` | trello `data.json` `/cards/801` (803 cards, complete) | complete | "Existing Investor Update", idShort 455, list `640643a3…93196` "Doing", url shortLink `MfMCBpMm`, `dateLastActivity` 2025-09-13T17:06:40Z, badges comments 0 / checkItems 0 |
| Its actions / checklists | `/actions` (5,252) by idCard; `/checklists` (54) by idCard | complete | 2 base actions (createCard 09-13T17:06:38Z, updateCard 09-13T17:06:40Z, both Leonard) whose `data.card`/`data.list` equal the SQL comment's; 0 checklists |
| Trello board `640643a3fd8f3ca308d9318e` | `/boards/1`; all actions with this idBoard (2,462) | complete | base `dateLastActivity` 2025-09-13T17:06:40Z = latest board action and latest card activity, so the UPDATE to 2025-09-14T04:20Z moves it forward to the comment's date |
| Trello member `PERSON_6094_TRELLO_USER_ID` | `/members/2` | complete | Leonard Hayes |
| Trello action id `68c64270d660c977c4696986` | `/actions` | complete | 0 matches; hex time 0x68c64270 = 2025-09-14T04:20:00Z = action date |
| Removed card `68d8193c…` | `/cards` | complete | not in base, so removing it leaves no base record orphaned |
| Calendar Oct 6 | gcal `data.json` `/events` (all), filtered to Fred's and Leonard's calendars | complete | no other single event on Oct 6 for either; the moved review (21:00–21:45Z) clashes with nothing injected either |
| Investor list Latest Status | gsheets `data.json` `/sheets_spreadsheets/96/sheets/0/grid` column 13 (23 non-empty notes) | complete | every note is dated "as of 09/11" / "before 09/12" or describes a Sep 2025 answer, consistent with the Q4 doc's new "which are all from this round" |
| Oct 14 board / deck placeholders | Slack Sep 2025 search "board meeting", "October 14"; "Boss Arena", "300+ levels" | complete for "board meeting"/"October 14"/"300+ levels"; "Boss Arena" first hits only | base #executives asks for board-meeting windows "October 14–17, 2025"; Match 3D builds list "Infinite boss arena (#424)" in Sep 2025. Nothing contradicts the deck or email |
| Removed-row references | grep of saved SQL for all 20 removed ids, "Board Deck", "466", "456", "pipeline" | whole SQL | 0 remaining references |
| Reused coverage | previous report §4/§11 (Drive/Docs/Sheets/Slides ids, slide object ids, Linear, Contacts, Calendar ids, other Gmail ids, unchanged Slack ids, base agreement for unchanged rows) | see §11 | unchanged |

## 5. Operation ledger

Every statement in execution order. "changed"/"ADDED" rows were verified fresh (NEW); byte-identical rows reuse the v9 ledger (§11) and were re-covered by the fresh whole-script parse in §2.

| SQL line | Table | Op | Record / target | Change vs v9 | Verification | Result |
|---|---|---|---|---|---|---|
| 5 | — | BEGIN | — | unchanged | parse | OK |
| 7 | gdrive.drive_files | INSERT | `f_8d2c47a91e05b3f6d7c418` | changed: renamed "Q3 investor update - send list"; parent base folder | NEW | PASS |
| 9 | gdrive.drive_files | INSERT | `f_3b9e61c04d7a52e8f1a6c2` | changed: renamed "Q4 investor update - send list" | NEW | PASS |
| 11 | gdrive.drive_files | INSERT | `d_5e8a1c3f9b07d2e64a1b93` | changed: folder renamed "Q4 2025 investor update"; owner Fred; parent base folder | NEW | PASS |
| 13 | gdrive.drive_files | INSERT | `f_c61a0e93b7d24f58a2e917` | changed: renamed "README - Q4 investor update"; parent = row 11 | NEW | PASS |
| 15 | gdrive.drive_files | INSERT | `f_a47d0e2c95b18f63e2c0d5` | changed: renamed deck | NEW | PASS |
| 17 | gdrive.drive_files | INSERT | `f_6e1d93a0c4b72f85d39a0e` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 20 | gdocs.docs_documents | INSERT | `f_8d2c47a91e05b3f6d7c418` | changed: new title/body (372 chars), runs contiguous | NEW | PASS |
| 22 | gdocs.docs_documents | INSERT | `f_3b9e61c04d7a52e8f1a6c2` | changed: new title/body (3,073 chars), runs contiguous | NEW | PASS |
| 24 | gdocs.docs_documents | INSERT | `f_c61a0e93b7d24f58a2e917` | changed: new title/body (225 chars), runs contiguous | NEW | PASS |
| 27 | gsheets.sheets_spreadsheets | INSERT | `f_6e1d93a0c4b72f85d39a0e` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 29 | gsheets.sheets_sheets | INSERT | `f_6e1d93a0c4b72f85d39a0e` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 32 | gslides.slides_presentations | INSERT | `f_a47d0e2c95b18f63e2c0d5` | changed: title = Drive name | NEW | PASS |
| 34 | gslides.slides_pages | INSERT | `slide_b4c21ca913ab` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 36 | gslides.slides_page_elements | INSERT | `el_6825f973029b (Harmony Games)` | changed | NEW | PASS |
| 38 | gslides.slides_page_elements | INSERT | `el_cffa02683868 (Q4 2025 update (draft))` | changed | NEW | PASS |
| 40 | gslides.slides_pages | INSERT | `slide_256dc0474f7c` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 42 | gslides.slides_page_elements | INSERT | `el_72151261faca (Highlights)` | changed | NEW | PASS |
| 44 | gslides.slides_page_elements | INSERT | `el_ca7b40076cd7 (Zombie Match 3D alpha numbers )` | changed | NEW | PASS |
| 46 | gslides.slides_pages | INSERT | `slide_fd6dbd079420` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 48 | gslides.slides_page_elements | INSERT | `el_90fbf6fd9c1b (Product)` | changed | NEW | PASS |
| 50 | gslides.slides_page_elements | INSERT | `el_ef5243814e8f (Boss Arena, Season Pass, 300+ )` | changed | NEW | PASS |
| 52 | gslides.slides_pages | INSERT | `slide_bb11abfc5fad` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 54 | gslides.slides_page_elements | INSERT | `el_69587907b898 (Engine)` | changed | NEW | PASS |
| 56 | gslides.slides_page_elements | INSERT | `el_6ca8bffe4445 (What shipped in Q3 (Arthur to )` | changed | NEW | PASS |
| 58 | gslides.slides_pages | INSERT | `slide_cb3f0884f833` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 60 | gslides.slides_page_elements | INSERT | `el_0c72e8ba6af7 (Team)` | changed | NEW | PASS |
| 62 | gslides.slides_page_elements | INSERT | `el_1e212bf4628e (Headcount and contractors (Leo)` | changed | NEW | PASS |
| 64 | gslides.slides_pages | INSERT | `slide_a56932e4c738` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 66 | gslides.slides_page_elements | INSERT | `el_5da52b8348b0 (Bridge round)` | changed | NEW | PASS |
| 68 | gslides.slides_page_elements | INSERT | `el_4f7f04b6e984 (New investors: welcome, with y)` | changed | NEW | PASS |
| 70 | gslides.slides_pages | INSERT | `slide_c9c7eed73bb9` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 72 | gslides.slides_page_elements | INSERT | `el_b45885b83bf9 (Try the game)` | changed | NEW | PASS |
| 74 | gslides.slides_page_elements | INSERT | `el_ed13f88ca45b (Firms in talks get the interna)` | changed | NEW | PASS |
| 76 | gslides.slides_pages | INSERT | `slide_329b5dfcb888` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 78 | gslides.slides_page_elements | INSERT | `el_09521ac10bd5 (Thank you)` | changed | NEW | PASS |
| 81 | slack.slack_messages | INSERT | `4921f321db5d08f936aac24a6a1d2af8` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 83 | slack.slack_messages | INSERT | `7fef94264090696760180223fc8265e7` | changed: Arthur, #executives, text changed; author/channel unchanged | NEW | PASS |
| 85 | slack.slack_messages | INSERT | `20924cc7f5176991d8a97a8eafb291d0` | ADDED: new: Leonard #executives 2025-09-26T18:35Z; id + ts no collision | NEW | PASS |
| 87 | slack.slack_messages | INSERT | `19e1e65d5952f075e8492867c6bcd472` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 89 | slack.slack_messages | INSERT | `800870c56bda852a57dfa06cb4fd63e6` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 91 | slack.slack_messages | INSERT | `1a68c2da0f36fc25489d3d9bbe9ccc32` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 93 | slack.slack_messages | INSERT | `c183280a284440a6ca6cdbb5270c9139` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 95 | slack.slack_messages | INSERT | `398502c0596e5347cc297f61eaefbd50` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 97 | slack.slack_messages | INSERT | `229090ba6b316b667d1a6451b0297a47` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 99 | slack.slack_messages | UPDATE | `id = '99aa913348bb05e6eda8daa06d37fc2a'` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 100 | slack.slack_messages | INSERT | `99b22482ddd77dd01b451afb39014839` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 102 | slack.slack_messages | INSERT | `f7261dd1b05eb2da3b81fe7d8cde2854` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 104 | slack.slack_messages | INSERT | `3cddf83c394676d8b72c0c20ed58f520` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 106 | slack.slack_messages | INSERT | `301ad67f082965686f35a9484aa25b0a` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 109 | trello.trello_actions | INSERT | `68c64270d660c977c4696986` | changed: data_json changed (comment text only); base card 455/list/board resolve; author Leonard | NEW | PASS |
| 111 | trello.trello_cards | UPDATE | `id = '68c5a49e8491a9d7faf869d0'` | unchanged: base card 68c5…69d0: comments 0→1, dateLastActivity 09-13T17:06:40Z→09-14T04:20Z (forward) | NEW (rechecked against base card and actions) | PASS |
| 112 | trello.trello_boards | UPDATE | `id = '640643a3fd8f3ca308d9318e'` | changed: base board: 09-13T17:06:40Z→09-14T04:20Z (forward; base max board action 09-13T17:06:40Z) | NEW | PASS |
| 114 | gmail.gmail_threads | INSERT | `frederick.stone/1844623441920000059` | changed | NEW | PASS |
| 116 | gmail.gmail_messages | INSERT | `frederick.stone/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@ma` | changed | NEW | PASS |
| 118 | gmail.gmail_threads | INSERT | `robert/1844623441920000061` | changed | NEW | PASS |
| 120 | gmail.gmail_messages | INSERT | `robert/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.` | changed | NEW | PASS |
| 122 | gmail.gmail_threads | INSERT | `leonard.hayes/1844623441920000062` | changed | NEW | PASS |
| 124 | gmail.gmail_messages | INSERT | `leonard.hayes/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail` | changed | NEW | PASS |
| 126 | gmail.gmail_threads | INSERT | `frederick.stone/1844724419788800011` | changed | NEW | PASS |
| 128 | gmail.gmail_messages | INSERT | `frederick.stone/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@ma` | changed | NEW | PASS |
| 130 | gmail.gmail_threads | INSERT | `leonard.hayes/1844724419788800013` | changed | NEW | PASS |
| 132 | gmail.gmail_messages | INSERT | `leonard.hayes/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail` | changed | NEW | PASS |
| 134 | gmail.gmail_threads | INSERT | `robert/1844724419788800014` | changed | NEW | PASS |
| 136 | gmail.gmail_messages | INSERT | `robert/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.` | changed | NEW | PASS |
| 138 | gmail.gmail_threads | INSERT | `arthur.blake/1844724419788800015` | changed | NEW | PASS |
| 140 | gmail.gmail_messages | INSERT | `arthur.blake/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.` | changed | NEW | PASS |
| 142 | gmail.gmail_threads | INSERT | `leonard.hayes/1844162278195200024` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 144 | gmail.gmail_messages | INSERT | `leonard.hayes/<CACJhvEE55qdWXuKC3BWlscoxBKrLUWavLQ3cpTJ@mail` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 146 | gmail.gmail_threads | INSERT | `frederick.stone/1844354293432320031` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 148 | gmail.gmail_messages | INSERT | `frederick.stone/<CAiKDPIoVSAFUBccUSRRBTi6dsmJdhof2EzteoIx@ma` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 150 | gmail.gmail_threads | INSERT | `frederick.stone/1844610859008000037` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 152 | gmail.gmail_messages | INSERT | `frederick.stone/<CAP6Gn2LV490e3El5rBDCgCItvhOdc7S6Wpb8nNq@ma` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 154 | gmail.gmail_threads | INSERT | `leonard.hayes/1844610859008000039` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 156 | gmail.gmail_messages | INSERT | `leonard.hayes/<CAP6Gn2LV490e3El5rBDCgCItvhOdc7S6Wpb8nNq@mail` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 158 | gmail.gmail_threads | INSERT | `frederick.stone/1844318935449600041` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 160 | gmail.gmail_messages | INSERT | `frederick.stone/<CAwC4Lcoz_m48Uv82Dq_lp6f26Gm0Vi7deiv8pmy@ma` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 162 | gmail.gmail_threads | INSERT | `leonard.hayes/1844318935449600043` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 164 | gmail.gmail_messages | INSERT | `leonard.hayes/<CAwC4Lcoz_m48Uv82Dq_lp6f26Gm0Vi7deiv8pmy@mail` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 166 | gmail.gmail_threads | INSERT | `frederick.stone/1844294398771200045` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 168 | gmail.gmail_messages | INSERT | `frederick.stone/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@ma` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 170 | gmail.gmail_threads | INSERT | `leonard.hayes/1844294398771200047` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 172 | gmail.gmail_messages | INSERT | `leonard.hayes/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@mail` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 174 | gmail.gmail_threads | INSERT | `robert/1844294398771200048` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 176 | gmail.gmail_messages | INSERT | `robert/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@mail.gmail.` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 178 | gmail.gmail_threads | INSERT | `arthur.blake/1844294398771200049` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 180 | gmail.gmail_messages | INSERT | `arthur.blake/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42FIXgK0ACq@mail.` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 182 | gmail.gmail_threads | UPDATE | `id = 'frederick.stone@harmonygames.co/1844294398771200045'` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 183 | gmail.gmail_messages | INSERT | `frederick.stone/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@ma` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 185 | gmail.gmail_threads | UPDATE | `id = 'leonard.hayes@harmonygames.co/1844294398771200047'` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 186 | gmail.gmail_messages | INSERT | `leonard.hayes/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 188 | gmail.gmail_threads | UPDATE | `id = 'robert@harmonygames.co/1844294398771200048'` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 189 | gmail.gmail_messages | INSERT | `robert/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 191 | gmail.gmail_threads | UPDATE | `id = 'arthur.blake@harmonygames.co/1844294398771200049'` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 192 | gmail.gmail_messages | INSERT | `arthur.blake/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 194 | gmail.gmail_threads | INSERT | `frederick.stone/1844276782694400053` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 196 | gmail.gmail_messages | INSERT | `frederick.stone/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@ma` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 198 | gmail.gmail_threads | INSERT | `leonard.hayes/1844276782694400055` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 200 | gmail.gmail_messages | INSERT | `leonard.hayes/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 202 | gmail.gmail_threads | INSERT | `robert/1844276782694400056` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 204 | gmail.gmail_messages | INSERT | `robert/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 206 | gmail.gmail_threads | INSERT | `arthur.blake/1844276782694400057` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 208 | gmail.gmail_messages | INSERT | `arthur.blake/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 210 | gmail.gmail_threads | UPDATE | `id = 'frederick.stone@harmonygames.co/1844276782694400053'` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 211 | gmail.gmail_messages | INSERT | `frederick.stone/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@ma` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 213 | gmail.gmail_threads | UPDATE | `id = 'leonard.hayes@harmonygames.co/1844276782694400055'` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 214 | gmail.gmail_messages | INSERT | `leonard.hayes/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 216 | gmail.gmail_threads | UPDATE | `id = 'robert@harmonygames.co/1844276782694400056'` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 217 | gmail.gmail_messages | INSERT | `robert/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 219 | gmail.gmail_threads | UPDATE | `id = 'arthur.blake@harmonygames.co/1844276782694400057'` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 220 | gmail.gmail_messages | INSERT | `arthur.blake/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 222 | gmail.gmail_threads | INSERT | `frederick.stone/1843992534712320061` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 224 | gmail.gmail_messages | INSERT | `frederick.stone/<calendar-2b67d1aa-cbdd-d816-22c3-d5ace6cf90` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 226 | gmail.gmail_threads | INSERT | `robert/1843992534712320063` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 228 | gmail.gmail_messages | INSERT | `robert/<calendar-c82c189b-c33c-a6e0-5e43-def7d943af26@google` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 230 | gmail.gmail_threads | INSERT | `arthur.blake/1843992534712320064` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 232 | gmail.gmail_messages | INSERT | `arthur.blake/<calendar-44faeeb8-a4b0-dae2-c4eb-4d2fda67b29b@` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 234 | gmail.gmail_threads | INSERT | `frederick.stone/1843718101401600063` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 236 | gmail.gmail_messages | INSERT | `frederick.stone/<calendar-2d8383e3-21d5-e958-783a-c960b5e984` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 238 | gmail.gmail_threads | INSERT | `robert/1843718101401600065` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 240 | gmail.gmail_messages | INSERT | `robert/<calendar-010d9a7c-8101-ee76-3333-bfb1ce826d3a@google` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 242 | gmail.gmail_threads | INSERT | `arthur.blake/1843718101401600066` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 244 | gmail.gmail_messages | INSERT | `arthur.blake/<calendar-9d6c5aee-50ea-1d96-5cd0-dcef1de61254@` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 246 | gmail.gmail_threads | INSERT | `frederick.stone/1844724105216000067` | changed | NEW | PASS |
| 248 | gmail.gmail_messages | INSERT | `frederick.stone/<calendar-297f69c9-ad63-fafd-14c3-70dbf78756` | changed: invite text = 2pm–2:45pm PT = gcal 267 | NEW | PASS |
| 251 | gcal.gcal_events | INSERT | `evt_2f86b0d4c9e17a35b64e0d` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 253 | gcal.gcal_events | INSERT | `evt_b511d4619c6f46ee63959b` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 255 | gcal.gcal_events | INSERT | `evt_8bd5e929463b854ec0ad13` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 257 | gcal.gcal_events | INSERT | `evt_ca908a712455521f1f8b43` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 259 | gcal.gcal_events | INSERT | `evt_7d3e19b04a6c25f8e1b9a0` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 261 | gcal.gcal_events | INSERT | `evt_99df25b554cac93e2926fd` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 263 | gcal.gcal_events | INSERT | `evt_671dce00bcb85abb3e355e` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 265 | gcal.gcal_events | INSERT | `evt_d65aa89778c3ebfa5d97b2` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 267 | gcal.gcal_events | INSERT | `evt_9c41e7a2d05b38f6e1a7c4` | changed: summary/desc/time changed → Oct 6 21:00–21:45Z (2pm PT); plan field | NEW | PASS |
| 269 | gcal.gcal_events | INSERT | `evt_75d8a0687ea57b663a40b0` | changed: same as 267, Leonard copy | NEW | PASS |
| 272 | linear.linear_issues | INSERT | `ZOM-567` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 274 | linear.linear_comments | INSERT | `lc_94eb35d962cfbdd31e1bd496` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 276 | linear.linear_comments | INSERT | `lc_b549f3057640a5eb08f7581e` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 279 | contacts.contacts | INSERT | `e3a91c07d5b48f26a0c7e314` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 281 | contacts.contacts | INSERT | `b72f0d6e19c3a84e5d21f9a0` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 283 | contacts.contacts | INSERT | `5d0e8b31f7a29c64e1b0d3a8` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 285 | contacts.contacts | INSERT | `a4c2e9f07b31d85e6c0f1b29` | unchanged | REUSED (v9 ledger) + whole-script static parse NEW | PASS |
| 287 | — | COMMIT | — | unchanged | parse | OK |

Removed relative to v9 (no longer in this SQL; nothing remaining references them): slides `slide_68eecd4f5f2a`, `slide_98d06d32c8d6`, `slide_fcf2cb38bf31`, `slide_5c7db3c42932`; elements `el_d65f0ea436c8`, `el_b87125dbf11e`, `el_6548686fe965`, `el_154065e277bc`, `el_ee461e258b77`, `el_8ee884c1e93b`, `el_34bc96464df6`, `el_ef3226341cb0`; Trello card `68d8193cf451863621c88a2a`, actions `68d8193c164e823ac3ae735d`, `68d81ae0459a87b4efb4b1e3`, `68d81f30a6c94e2b7d05e1f4`, checklist `68d81ae0bac8fd292e6606f8`, check items `68d81ae032fe8d64dbd262c7`, `68d81ae087c12c3d08c79ff8`, `68d81ae05ac90637e942026c`, `68d81ae07d46d8fe71f4ba98`.

## 6. Check A: records, references and IDs

- **References resolve.** New Slack author Leonard (`EMPLOYEE_0038`) is a #executives member (`C07C2866011`, reused membership check). The Trello comment's card, list and board are base records and its `data_json` copies their id, idShort 455, name and shortLink exactly as base actions do; its author is Leonard's Trello account. The card and board UPDATE targets exist. README's parent is the folder inserted earlier (row 11); the other Drive parents are unchanged base folders (reused). Gmail messages all reference threads inserted before them.
- **No collisions.** New Slack id: 0 of 610,468 (complete lookup); its ts is absent from its channel-month. Trello action id: 0 of 5,252. Renamed Drive/Docs/Slides rows keep their v9 ids (reused, collision-free). No duplicate keys within the SQL. Removing the injected card and slides frees their keys and leaves no reference behind.
- **ID contracts.** Gmail `history_id` NULL on every thread; no Drive row sets `content_path`; the new Slack id is 32-hex like the base.
- **Readable Drive files.** The 3 Google Docs have non-empty `body_text` (372 / 3,073 / 225 chars); the Sheet and Slides have their content rows.
- **One account per person.** No new accounts in this version; the 4 contacts are unchanged (reused).

## 7. Check B: SQL structure and supported schema rules

- One BEGIN/COMMIT block. Every INSERT names its columns and has one VALUES row of matching length (lint and independent parse, 130 rows). The 11 UPDATEs use primary-key predicates.
- No `_fts` column set. Linear dates use `YYYY-MM-DDTHH:MM:SSZ`; `state_history_json = '[]'` on ZOM-567 (unchanged). All `*_json` values parse with base shapes; the new Slack row uses `metadata_json '{}'` and list-shaped reactions/files/attachments; Trello `data_json` and `badges_json` are objects.
- Docs: style runs contiguous from 0 to `len(body_text)`. Heading runs cover exactly the headings ("Who gets it", "Groups", "Notes"; "Who to look at", "Groups, as of end of day Tue Sep 30 (Pacific)", "Build access", "Sheet"; README title).
- Slides: 8 pages with indices 0–7 and no gaps after the removals; every element's page exists.
- **Provisional snapshot comparison:** MATCH for every column used, except four columns the snapshot doesn't cover (unchanged): `gslides.slides_pages.notes` (all NULL), `gslides.slides_page_elements.table_json` (all NULL) and `.ordinal`, `linear.linear_comments.sequence`. Advisory only (Advisory 1).

## 8. Check C: dates, relationships and consistency

- **Clock.** Every event timestamp is at or before 2025-10-01T07:00Z (latest: Leonard's #zombie-match3d reply 2025-09-30T23:48Z). Only plan fields are later (Oct 6 gcal start/end).
- **New #executives note (row 85, 09-26T18:35Z).** It precedes the Q4 doc's modified time (18:41Z), which points to it ("see my note in #executives on what counts as signed"), so the pointer resolves to an earlier record. It frames Leonard's own Sep 19 post (row 81, "Paul Heydon is in for $50K and Anton … $40K") as not counting, and the DocuSign Completed notice for Anton (Fred's mailbox, 09-26T19:02Z) is the kind of record it names. No contradiction with base #executives that day.
- **Trello (rows 109, 111, 112).** Leonard's 09-14T04:20Z comment comes after the card's creation (09-13T17:06:38Z) and its last base activity. The card UPDATE sets comments 0→1, matching the single injected comment, and keeps checkItems 0 (no checklist is injected now). Card and board `dateLastActivity` move forward to the comment's time. The board's base max action is 09-13T17:06:40Z, so nothing later in base is contradicted. The v9 board value (09-27) belonged to the removed card's actions and is correctly dropped.
- **Emails (rows 116–140).** Robert's 09-29T18:20Z "send it to everyone on the 2025 investor list" (Cc Leonard; copies in Fred, Robert-SENT, Leonard) precedes Leonard's 09-30T21:05Z email, which answers it ("Let's not"). Leonard's email points at things that exist and agree: "your Q4 investor update folder" is the Fred-owned folder (row 11) with the README naming the file; "the Q4 update send list doc" is row 22; "the draft update deck shows what each group gets" is slide 6 (New investors / In talks / Awaiting reply / Keep warm, the same four groups as the doc); "the Existing Investor Update card" holds the Keep-warm comment; "Monday's review on your calendar" is the 21:00Z invite sent five minutes earlier. "Our existing investors are already on my own list" matches the doc's opening line. "The week after the Oct 14 board" fits base #executives asking for board-meeting windows Oct 14–17, 2025. Griffin AGM / Dentsu are unchanged context (reused).
- **Q4 doc (row 22).** Its rules cite only existing things (Sep 3 kickoff, Fred's calendar, SVB catch-ups, the list's Latest Status notes, #bridge-pitch, a16z speedrun, Arthur's tester tracking, the #executives note). The new claim that the Latest Status notes "are all from this round" agrees with the base column: all 23 notes are dated 09/07–09/12 or describe Sep 2025 answers that injected or base September records confirm (e.g. Initial Capital, row 89, 09-09). The Keep-warm group matches the Sep 14 Trello comment. Nothing postdates the doc's modified time as a past event.
- **Q3 doc (row 20, Jul 2025).** It is an older, superseded template ("New investor: anyone who's told us yes with an amount"). The Sep 26 doc and Leonard's Sep 26 note replace that rule in dated records by the same author, so it is supported historical context, not a contradiction.
- **Arthur's #executives text (row 83, 09-29T18:00Z).** "for the Q4 send list I'd just use who Leonard emailed this month" is an opinion from someone the doc and deck were shared with. It asserts no fact that a record contradicts.
- **Calendar (rows 248, 267, 269).** The invite renders "Mon Oct 6, 2025 2pm – 2:45pm Pacific Time" / "(PDT)" = 21:00–21:45Z on both gcal rows. Created/updated 09-30T21:00Z = the invite email's date. Same `ical_uid` on organizer and attendee copies, with consistent `self`/`organizer` flags.
- **README (row 24).** "Leonard picks everything up on Monday Oct 6" matches the review date. "Name the send list 'Q4 update - send list'" names an output that doesn't exist yet. It differs from the template's name ("Q4 investor update - send list"), so it doesn't collide with it.
- **Removed records.** No remaining row mentions the board pre-read, the Board Deck card, idShort 456/466, the fundraising slide or committed/soft-circled totals. Removing them leaves no dangling relationship.
- **Unchanged records.** Chronology, encodings and base agreement for byte-identical rows are reused from the previous review (§11): Anton $40K → $25K DM chain and DocuSign, Play Ventures correction, Sciplay reply and its parent UPDATE, Treo VC, 1AM Gaming, Mattel, Initial Capital, Arthur's Android tester-list correction against ZOM-567, Eastern-time invites in Arthur's mailbox, contacts, Linear.
- **Grader-facing text.** None. Every new or changed text is in a persona's voice; nothing addresses a solver or grader or describes the test.

## 9. Findings

No demonstrated defects. Remaining advisory (does not block this stage):

1. **Columns not in the schema snapshot (Check B, provisional, unchanged).** `slides_pages.notes` (all NULL), `slides_page_elements.table_json` (all NULL) and `.ordinal`, and `linear_comments.sequence` appear in neither the snapshot nor the base exports. If a platform table lacks any of them, that INSERT fails and BEGIN/COMMIT rolls back the whole script. No task content depends on them. Smallest fix: drop those four columns and their values, or confirm the script loads on the platform.

## 10. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | Actors, channels, the Trello card/list/board/member, Drive parents and UPDATE targets resolve. The new Slack id/ts and the Trello action id don't collide in complete scans. The 20 removed rows leave no dangling references. No ID-contract breaks. Drive files are readable. |
| B — SQL structure and supported schema rules | PASS | Structure, JSON shapes, generated columns, Linear formats, Doc style runs and slide indices are valid. Four columns the snapshot doesn't cover are advisory. Not live-certified. |
| C — Dates, relationships and consistency | PASS | All event times are before the clock. The renamed docs, deck, emails, invite, Trello comment and new #executives note point at records that exist and agree, in a consistent order. Trello activity dates move forward from base. Superseded content (Q3 doc, Sep 19 angel post) is replaced by later dated records. |

Outside certification scope (disclosed, not gates): live execution and current database compatibility (including the four columns), search ranking, Agent visibility and persona access, task difficulty.

## 11. Stage ownership and reuse

Reused evidence (stage-evidence-v1), from `Evals/task_inputs/reports/0_injection.md` as it stood before this rerun, SHA-256 `4f686c43a21f278ef70ad1043b37c9596bc7edd7535f6cfd4caecb83b0a8c9d2` (injection-static-v2, PASS/COMPLETE, SQL `84818944…cc0be`):

| Item | Source ledger / check | Dependencies verified unchanged |
|---|---|---|
| Collision results for ids of byte-identical and renamed rows (Drive/Docs/Sheets/Slides ids, remaining slide object ids, Linear issue/comment ids, Calendar ids/ical_uids, Gmail thread/message ids, 4 contacts, 12 unchanged Slack ids) | previous §4/§11 | universe manifest `da2f4cf0…aac1a`; those ids identical in this SQL; in-SQL duplicate check rerun on all 130 rows |
| Membership/identity (Slack channels and authors, D05S58U4SAK, Gmail/Drive accounts) | previous §4/§6 | manifest; roster/ACL hashes; authors unchanged |
| Base agreement for byte-identical rows (Anton chain, DocuSign, Paul Heydon, Play Ventures, Sciplay + parent UPDATE, Treo VC, 1AM Gaming, Mattel, Initial Capital, Ilse Marrow / PERSON_5487 invites in ET/PT, Dentsu/Ryo, ZOM-567 + comments, Arthur's #zombie-match3d correction, contacts) | previous §4/§8 | manifest; those SQL rows byte-identical (diff in §1) |

Eval 0, schema snapshot, id_contracts, lint, roster and ACL hashes equal those recorded in the previous report.

`/prompt` may reuse these static checks only while all of these hold: SQL SHA-256 `efe3cab14874d1daa3ba71900a44a4536537fe46eae947167649ae2032c9c881`, universe manifest `da2f4cf0…aac1a`, schema snapshot `31dcb2b4…`, id_contracts `fc4711ef…`, Eval 0 `e034019b…`, clock 2025-10-01T07:00Z. `/prompt` still owns discoverability and persona access. This SQL changed, so earlier /prompt, /hardness, /oe and /rubric results are outdated; run /prompt, /hardness, /oe and /rubric again in that order.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Update the prompt to the renamed scenario (it still names the Oct 14 pre-read, the "Board - Oct 14 2025" folder and the slide numbers), then run /prompt, /hardness (with a fresh run on this SQL), /oe and /rubric. Optionally drop the four snapshot-uncovered columns (Advisory 1) first; that makes a new SQL version that needs /injection again.

Evidence limits: Static review only. Live load, current database compatibility (incl. the four snapshot-uncovered columns), Agent visibility and difficulty are outside scope.
