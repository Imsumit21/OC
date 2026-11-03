# Injection Data-Integrity Review (Eval 0)

Review version: `injection-static-v2`
Evidence contract: `stage-evidence-v1`
Review time: 2026-11-02T09:48Z (actual)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Mode: chat review, attempt 6ae4e299a13034b7eb8305f8 (static, SQL not executed)

## 1. Scope and inputs

| Input | Value |
|---|---|
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` (input revision 11, from chat attachment `01_Universe_Inject (9).sql`), 132,888 bytes, SHA-256 `8481894430080319e947ad672ca3cd9ddfd9e40af102edafed975e0aaadcc0be`. Replaces `01_Universe_Inject (7).sql` (SHA `3ba2b413…7f87`, last reviewed PASS), so that report no longer applies. |
| Diff from the previous version | Header count 149 → 150 INSERT. Template doc body rewritten (Passed rule: phone-pass sentence removed; "partner writing from their own address / check contacts" sentence removed; Latest Status sentence reworded), 3,018 → 2,685 chars with style runs re-indexed. Slack: Leonard's "drop notes from my phone calls" post (`3f2d8f04…`) **removed**; Treo VC text now "pinged me again"; Play Ventures correction adds "the \"discussing\" Robert heard via Applovin doesn't change that"; the Sciplay reply moves from the #bridge-pitch thread `73c2247f…` (reply `cf10d4f7…` and its parent UPDATE **removed**) to a new reply `229090ba…` in #executives under base message `99aa9133…` plus its parent UPDATE; **new** Leonard→Fred DMs `99b22482…` (Anton 40 → 25) and `f7261dd1…` (Anton signed); **new** #zombie-match3d thread `3cddf83c…` (Arthur: Play tester list never attached) + reply `301ad67f…` (Leonard). Trello card idShort 466 → 456 (card, url and 3 actions). Gmail: Fred's copy of Anton's "SAFE amount" email **removed** (thread `…023` + message); Leonard's copy re-keyed to thread `…024` and Fred dropped from Cc. Arthur's two calendar-invite emails now render in Eastern Time. Linear Dentsu comment now "TestFlight added Sep 26, Play internal track added Sep 26 (investor tester list)". All other rows byte-identical. |
| Assignment (context only) | Frederick Stone, Co-founder; not graded here |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Eval | `Evals/0_Injection_Quality_Eval.md` `e034019b8ec450437509a73dd3bae2d303b57561b0f67fcc1e5d19266f663eff` |
| Shared workflow | `hg_reference.py guide injection` (WORKFLOW `ee4cd8e1…`), with slack/trello/gmail routes and schema tables slack_messages, trello_cards, gmail_messages, gmail_threads, docs_documents |
| Schema snapshot | `references/schema/injection.json` `31dcb2b43feca8e5…` (unverified, provisional) |
| ID contracts | `references/schema/id_contracts.json` `fc4711ef07667333…` |
| Lint | `hg_injection_lint.py` `a8226e2a69425355…`, version `injection-lint-v1` |
| Roster / ACL | roster.json `3f2174513f639e37…`, acl.md `e9bca2b35f98d5ef…` (identity checks only) |

Input/authority issues: none. SQL comment lines (1–4 and section banners) are evidence of intent only; none addresses a grader or mentions tool calls, pass rate or gates. The header count (150 INSERT, 11 UPDATE) matches the parsed SQL.

## 2. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, base manifest, review version | NEW, done (saved as input revision 11 before review) |
| Run lint; resolve every flag | NEW, done (0 FAIL, 0 CHECK, 0 INFO) |
| Inventory every statement and affected record | NEW, done: 163 statements (BEGIN, 150 INSERT, 11 UPDATE, COMMIT), 161 row operations, ledger §5; 19 removed/replaced prior rows listed in §1 |
| Check A | NEW for changed rows, REUSED for byte-identical rows (§11): PASS |
| Check B | NEW (whole script): PASS (provisional snapshot advisory) |
| Check C | NEW for changed rows, REUSED for byte-identical rows: PASS |
| Report coverage, findings, limits, one verdict | NEW, done |

Independent static parse of all 163 statements (whole script, fresh): column/value counts match on every INSERT; every `*_json` value parses; no `_fts` column set; Slack `ts` = `created_at` on all 12 messages and `metadata_json = '{}'`; no event timestamp after the clock (only the Oct 6 gcal start/end plan fields are later); Gmail `snippet` = body prefix, `internal_date` = `date` = Date header, Subject header = subject and Cc header ⇔ `cc_json` on all 36 messages; all 28 thread snippets equal their latest message's snippet (including the 8 UPDATEs); doc style runs contiguous on all 3 docs; no duplicate primary keys within the SQL; no duplicate Slack (channel, ts).

## 3. Lint result

`hg_injection_lint.py` on SHA `84818944…be`, universe synthcut, clock 2025-10-01T07:00Z. Base files loaded: contacts, slack users, trello, gmail users, linear, confluence. Rows parsed: 150 INSERT, 11 UPDATE across 25 tables.

Flags: **none** (FAIL 0, CHECK 0, INFO 0). Nothing to resolve. Checks A–C were still run in full.

## 4. Source coverage (new checks in this run)

| Check | Source / pointer | Coverage | Result |
|---|---|---|---|
| New Slack ids (5) + thread parent | `lookup slack --file 'messages/*.json' --key id` | 4,840 files, 610,468 messages, scan complete, 0 errors | 5 new ids: 0 matches. Parent `99aa913348bb05e6eda8daa06d37fc2a` at `slack/messages/C07C2866011/2025-09.json` `/1171` |
| Slack ts collisions | `C07C2866011`, `D05S58U4SAK`, `C0880U9751A` `2025-09.json` read in full | 3 files | none of the 5 new ts values present |
| Slack users / channels | `users.json`, `channels.json` | complete | EMPLOYEE_0008 = Frederick Stone, 0016 = Robert, 0025 = Arthur Blake, 0038 = Leonard Hayes. #executives `C07C2866011` members incl. 0016/0025/0038; #zombie-match3d `C0880U9751A` incl. 0025/0038; `D05S58U4SAK` is an IM whose messages are only 0038 and 0008 (Aug: 148/79, Sep: 121/70) |
| Thread-parent convention | `C07C2866011/2025-09.json` parents with replies (e.g. `22ec8339…`, `842b8156…`) | sampled to confirm format only | base parents carry `thread_ts` = own ts, so the UPDATE's `thread_ts_legacy = '1759196326.309469'` and row 59's self ts match |
| Trello idShort 456 | trello `data.json` `/cards` (803) and `/actions` (5,252) | complete | no card with idShort 456 (or 466); board `640643a3…318e` has 449 cards, max idShort 455; no action carries idShort 456 |
| Gmail thread `leonard.hayes@…/1844162278195200024` | `grep -rlF` over all `gmail/threads/*.json` | 81,404 files | 0 files; id >> 20 = 1758730200000 = message internal_date (base id convention) |
| Arthur's time zone | gcal `/calendars` (arthur.blake primary); Arthur-mailbox base invites (150 files containing "Invitation:") | complete for calendars; invites grep | `time_zone: America/New_York`; invites render "Eastern Time - New York" 107×, Pacific 11×. Robert's base invites render Pacific 79× (unchanged PT rows consistent) |
| Facts behind changed text | base #bridge-pitch `2025-09.json` (Treo, Play Ventures, Applovin, Sciplay), `D04UC0UEN2V/2025-09.json`, `C07C2866011/2025-09.json`, `C0880U9751A/2025-09.json`; Gmail `00015209` and all 10 files containing `PERSON_3242_EMAIL` | read | see §8 |
| Reference integrity of removed rows | grep of saved SQL for removed ids (`…023`, `…025`, `3f2d8f04…`, `cf10d4f7…`) and for "phone", "ring a bell", "check contacts", "own address", "drop notes" | whole SQL | no remaining reference |
| Reused coverage | previous report §4 (Drive, Docs/Sheets/Slides, slide object ids, Trello other ids, Linear, Contacts, Calendar, other Gmail ids, investor list, Initial Capital/Mattel/T-Accelerate/Dentsu facts) | see §11 | unchanged |

## 5. Operation ledger

All 161 row operations in execution order (line = statement start; BEGIN line 5, COMMIT at end). Parents come before children. Rows marked **changed/new** were checked fresh against the base; the rest are byte-identical to the previous version.

| # | Line | Table | Op | Record / target | Key values | Check result |
|---|---|---|---|---|---|---|
| 1 | 7 | gdrive.drive_files | INSERT | `f_8d2c47a91e05b3f6d7c418` | Board pre-read - fundraising section | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 2 | 9 | gdrive.drive_files | INSERT | `f_3b9e61c04d7a52e8f1a6c2` | Board pre-read - fundraising section (Oct 14) | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 3 | 11 | gdrive.drive_files | INSERT | `d_5e8a1c3f9b07d2e64a1b93` | Board - Oct 14 2025 | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 4 | 13 | gdrive.drive_files | INSERT | `f_c61a0e93b7d24f58a2e917` | README - Oct 14 board materials | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 5 | 15 | gdrive.drive_files | INSERT | `f_a47d0e2c95b18f63e2c0d5` | HG BoD Oct 14 2025 (draft) | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 6 | 17 | gdrive.drive_files | INSERT | `f_6e1d93a0c4b72f85d39a0e` | Bridge angels | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 7 | 20 | gdocs.docs_documents | INSERT | `f_8d2c47a91e05b3f6d7c418` | Board pre-read - fundraising section | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 8 | 22 | gdocs.docs_documents | INSERT | `f_3b9e61c04d7a52e8f1a6c2` | Board pre-read - fundraising section (Oct 14) | **changed/new:** readable, body 2,685 chars; 10 style runs contiguous 0–2,685; HEADING_2 runs on the 4 section titles; Drive row line 9 in SQL |
| 9 | 24 | gdocs.docs_documents | INSERT | `f_c61a0e93b7d24f58a2e917` | README - Oct 14 board materials | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 10 | 27 | gsheets.sheets_spreadsheets | INSERT | `f_6e1d93a0c4b72f85d39a0e` | Bridge angels | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 11 | 29 | gsheets.sheets_sheets | INSERT | `f_6e1d93a0c4b72f85d39a0e` | Angels | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 12 | 32 | gslides.slides_presentations | INSERT | `f_a47d0e2c95b18f63e2c0d5` | HG BoD Oct 14 2025 (draft) | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 13 | 34 | gslides.slides_pages | INSERT | `?` |  | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 14 | 36 | gslides.slides_page_elements | INSERT | `?` | Harmony Games Board Meeting | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 15 | 38 | gslides.slides_page_elements | INSERT | `?` | October 14, 2025 (draft) | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 16 | 40 | gslides.slides_pages | INSERT | `?` |  | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 17 | 42 | gslides.slides_page_elements | INSERT | `?` | Agenda | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 18 | 44 | gslides.slides_page_elements | INSERT | `?` | Q3 recap / Zombie Match 3D alpha / Engine / T | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 19 | 46 | gslides.slides_pages | INSERT | `?` |  | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 20 | 48 | gslides.slides_page_elements | INSERT | `?` | Q3 recap | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 21 | 50 | gslides.slides_page_elements | INSERT | `?` | Domino Delights: publisher sear byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 22 | 52 | gslides.slides_pages | INSERT | `?` |  | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 23 | 54 | gslides.slides_page_elements | INSERT | `?` | Zombie Match 3D | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 24 | 56 | gslides.slides_page_elements | INSERT | `?` | Alpha metrics (Robert to fill) | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 25 | 58 | gslides.slides_pages | INSERT | `?` |  | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 26 | 60 | gslides.slides_page_elements | INSERT | `?` | Engine | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 27 | 62 | gslides.slides_page_elements | INSERT | `?` | What shipped in Q3 (Arthur to fill) | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 28 | 64 | gslides.slides_pages | INSERT | `?` |  | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 29 | 66 | gslides.slides_page_elements | INSERT | `?` | Team | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 30 | 68 | gslides.slides_page_elements | INSERT | `?` | Headcount and contractors (Leonard to fill) | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 31 | 70 | gslides.slides_pages | INSERT | `?` |  | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 32 | 72 | gslides.slides_page_elements | INSERT | `?` | Runway | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 33 | 74 | gslides.slides_page_elements | INSERT | `?` | Cash and burn (Leonard to fill) | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 34 | 76 | gslides.slides_pages | INSERT | `?` |  | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 35 | 78 | gslides.slides_page_elements | INSERT | `?` | Options | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 36 | 80 | gslides.slides_page_elements | INSERT | `?` | Bridge / co-dev / engine deals | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 37 | 82 | gslides.slides_pages | INSERT | `?` |  | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 38 | 84 | gslides.slides_page_elements | INSERT | `?` | Fundraising | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 39 | 86 | gslides.slides_page_elements | INSERT | `?` | Bridge round, pipeline as of Sep  byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 40 | 88 | gslides.slides_pages | INSERT | `?` |  | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 41 | 90 | gslides.slides_page_elements | INSERT | `?` | Asks for the board | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 42 | 92 | gslides.slides_page_elements | INSERT | `?` | Intros, especially games funds and strategics | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 43 | 94 | gslides.slides_pages | INSERT | `?` |  | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 44 | 96 | gslides.slides_page_elements | INSERT | `?` | Appendix | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 45 | 98 | gslides.slides_page_elements | INSERT | `?` | Investor FAQ (link) | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 46 | 100 | gslides.slides_pages | INSERT | `?` |  | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 47 | 102 | gslides.slides_page_elements | INSERT | `?` | Thank you | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 48 | 105 | slack.slack_messages | INSERT | `4921f321db5d08f936aac24a6a1d2af8` | C07C2866011 EMPLOYEE_0038 2025-09-19T17:40:00Z | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 49 | 107 | slack.slack_messages | INSERT | `7fef94264090696760180223fc8265e7` | C07C2866011 EMPLOYEE_0025 2025-09-29T18:00:00Z | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 50 | 109 | slack.slack_messages | INSERT | `19e1e65d5952f075e8492867c6bcd472` | C096HFA5Z8W EMPLOYEE_0038 2025-09-03T23:31:00Z | **changed/new:** text only ("pinged me again"); base #bridge-pitch 2025-09-03T23:19Z lists "Treeo VC (inbound b2b AI, Leonard responded on linkedin)"; id/ts unchanged |
| 51 | 111 | slack.slack_messages | INSERT | `800870c56bda852a57dfa06cb4fd63e6` | C096HFA5Z8W EMPLOYEE_0038 2025-09-09T18:20:00Z | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 52 | 113 | slack.slack_messages | INSERT | `1a68c2da0f36fc25489d3d9bbe9ccc32` | C096HFA5Z8W EMPLOYEE_0038 2025-09-08T21:05:00Z | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 53 | 115 | slack.slack_messages | INSERT | `c183280a284440a6ca6cdbb5270c9139` | C096HFA5Z8W EMPLOYEE_0038 2025-09-25T16:20:00Z | **changed/new:** text only; base #bridge-pitch Robert 2025-09-25T00:30–01:45Z: "… from Applovin said … is aware that you reached out" / "Play Ventures" / "discussing"; correction posted later (16:20Z) |
| 54 | 117 | slack.slack_messages | INSERT | `398502c0596e5347cc297f61eaefbd50` | C096HFA5Z8W EMPLOYEE_0038 2025-09-26T22:50:00Z | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 55 | 119 | slack.slack_messages | INSERT | `229090ba6b316b667d1a6451b0297a47` | C07C2866011 EMPLOYEE_0016 2025-09-30T16:06:00Z, reply to 99aa9133… | **changed/new:** new id (lookup 610,468, 0 hits); Robert member of #executives; ts = created_at; reply follows parent (01:38:46Z) |
| 56 | 121 | slack.slack_messages | UPDATE | `99aa913348bb05e6eda8daa06d37fc2a` | reply_count = 1, reply_users_count = 1, latest_reply = '1759248360.377 | **changed/new:** target exists (/1171 in C07C2866011/2025-09.json, Leonard, a16z post); base reply_count 0, thread_ts null; thread_ts_legacy = own ts matches base parent convention |
| 57 | 122 | slack.slack_messages | INSERT | `99b22482ddd77dd01b451afb39014839` | D05S58U4SAK EMPLOYEE_0038 2025-09-24T16:25:00Z | **changed/new:** new id; DM is Leonard–Fred (EMPLOYEE_0008 = Frederick Stone); ts unused; follows Anton email 16:10Z |
| 58 | 124 | slack.slack_messages | INSERT | `f7261dd1b05eb2da3b81fe7d8cde2854` | D05S58U4SAK EMPLOYEE_0038 2025-09-26T19:15:00Z | **changed/new:** new id; same DM; ts unused; follows DocuSign Completed 19:02Z |
| 59 | 126 | slack.slack_messages | INSERT | `3cddf83c394676d8b72c0c20ed58f520` | C0880U9751A EMPLOYEE_0025 2025-09-30T23:20:00Z | **changed/new:** new id; Arthur member of #zombie-match3d; parent thread fields self-consistent (reply_count 1, latest_reply = row 60 ts) |
| 60 | 128 | slack.slack_messages | INSERT | `301ad67f082965686f35a9484aa25b0a` | C0880U9751A EMPLOYEE_0038 2025-09-30T23:48:00Z, reply to 3cddf83c… | **changed/new:** new id; Leonard member; reply follows parent; thread_parent_id/ts_legacy match row 59 |
| 61 | 131 | trello.trello_actions | INSERT | `68c64270d660c977c4696986` | commentCard 2025-09-14T04:20:00Z | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 62 | 133 | trello.trello_cards | UPDATE | `68c5a49e8491a9d7faf869d0` | badges_json = '{"attachments": 0, "attachmentsByType": {"trello": {"bo | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 63 | 134 | trello.trello_boards | UPDATE | `640643a3fd8f3ca308d9318e` | "dateLastActivity" = '2025-09-27T17:30:24Z' | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 64 | 135 | trello.trello_cards | INSERT | `68d8193cf451863621c88a2a` | Board Deck - Oct 14 idShort 456 | **changed/new:** idShort 456 unused (board 640643a3…318e max 455; 0 base cards or actions with 456); url uses 456 |
| 65 | 137 | trello.trello_actions | INSERT | `68d8193c164e823ac3ae735d` | createCard 2025-09-27T17:05:00Z | **changed/new:** data.card.idShort 456 = card |
| 66 | 139 | trello.trello_checklists | INSERT | `68d81ae0bac8fd292e6606f8` | Sections | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 67 | 141 | trello.trello_check_items | INSERT | `68d81ae032fe8d64dbd262c7` | Fundraising - Fred | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 68 | 143 | trello.trello_check_items | INSERT | `68d81ae087c12c3d08c79ff8` | Product - Robert | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 69 | 145 | trello.trello_check_items | INSERT | `68d81ae05ac90637e942026c` | Engine - Arthur | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 70 | 147 | trello.trello_check_items | INSERT | `68d81ae07d46d8fe71f4ba98` | Runway and options - Leonard | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 71 | 149 | trello.trello_actions | INSERT | `68d81ae0459a87b4efb4b1e3` | addChecklistToCard 2025-09-27T17:12:00Z | **changed/new:** data.card.idShort 456 = card |
| 72 | 151 | trello.trello_actions | INSERT | `68d81f30a6c94e2b7d05e1f4` | commentCard 2025-09-27T17:30:24Z | **changed/new:** data.card.idShort 456 = card |
| 73 | 154 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844623441920000059` | Fred - for the 14th could you just email | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 74 | 156 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rp…` | 2025-09-29T18:20:00Z from robert@harmonygames.co: board pipeline | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 75 | 158 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844623441920000061` | Fred - for the 14th could you just email | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 76 | 160 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB…` | 2025-09-29T18:20:00Z from robert@harmonygames.co: board pipeline | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 77 | 162 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844623441920000062` | Fred - for the 14th could you just email | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 78 | 164 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-…` | 2025-09-29T18:20:00Z from robert@harmonygames.co: board pipeline | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 79 | 166 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844724419788800011` | Fred, I'm flying to LA tomorrow morning  | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 80 | 168 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU…` | 2025-09-30T21:05:00Z from leonard.hayes@harmonygames.co: Oct 14 board pre-read - fundraising sect | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 81 | 170 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844724419788800013` | Fred, I'm flying to LA tomorrow morning  | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 82 | 172 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5H…` | 2025-09-30T21:05:00Z from leonard.hayes@harmonygames.co: Oct 14 board pre-read - fundraising sect | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 83 | 174 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844724419788800014` | Fred, I'm flying to LA tomorrow morning  | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 84 | 176 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0z…` | 2025-09-30T21:05:00Z from leonard.hayes@harmonygames.co: Oct 14 board pre-read - fundraising sect | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 85 | 178 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844724419788800015` | Fred, I'm flying to LA tomorrow morning  | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 86 | 180 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hf…` | 2025-09-30T21:05:00Z from leonard.hayes@harmonygames.co: Oct 14 board pre-read - fundraising sect | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 87 | 182 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844162278195200024` | Leonard, Had another look at my numbers. | **changed/new:** new id, 0 hits in 81,404 Gmail thread files; id>>20 = 1758730200000 = message internal_date |
| 88 | 184 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CACJhvEE55qdWXuKC3BWlsco…` | 2025-09-24T16:10:00Z from PERSON_9901_EMAIL: SAFE amount | **changed/new:** message id unchanged (checked before); cc removed in cc_json and headers; thread_id = row 87 |
| 89 | 186 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844354293432320031` | Hello Frederick Stone, All signers compl | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 90 | 188 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAiKDPIoVSAFUBccUSRRBT…` | 2025-09-26T19:02:00Z from SVC_1302_EMAIL: Completed: Complete with docusign: Harmo | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 91 | 190 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844610859008000037` | Hi Paul, Gentle nudge on the SAFE in Doc | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 92 | 192 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAP6Gn2LV490e3El5rBDCg…` | 2025-09-29T15:00:00Z from leonard.hayes@harmonygames.co: SAFE in DocuSign | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 93 | 194 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844610859008000039` | Hi Paul, Gentle nudge on the SAFE in Doc | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 94 | 196 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAP6Gn2LV490e3El5rBDCgCI…` | 2025-09-29T15:00:00Z from leonard.hayes@harmonygames.co: SAFE in DocuSign | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 95 | 198 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844318935449600041` | Leonard, Thanks again for the session on | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 96 | 200 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_lp…` | 2025-09-26T09:40:00Z from PERSON_9903_EMAIL: Harmony Games bridge | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 97 | 202 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844318935449600043` | Leonard, Thanks again for the session on | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 98 | 204 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_lp6f…` | 2025-09-26T09:40:00Z from PERSON_9903_EMAIL: Harmony Games bridge | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 99 | 206 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844294398771200045` | Leonard-san, Thank you for the offer. Pl | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 100 | 208 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4k…` | 2025-09-26T03:10:00Z from PERSON_5221_EMAIL: Zombie Match 3D access | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 101 | 210 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844294398771200047` | Leonard-san, Thank you for the offer. Pl | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 102 | 212 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4kix…` | 2025-09-26T03:10:00Z from PERSON_5221_EMAIL: Zombie Match 3D access | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 103 | 214 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844294398771200048` | Leonard-san, Thank you for the offer. Pl | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 104 | 216 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4kixWZOsz42…` | 2025-09-26T03:10:00Z from PERSON_5221_EMAIL: Zombie Match 3D access | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 105 | 218 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844294398771200049` | Leonard-san, Thank you for the offer. Pl | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 106 | 220 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4kixW…` | 2025-09-26T03:10:00Z from PERSON_5221_EMAIL: Zombie Match 3D access | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 107 | 222 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1844294398771200045` | snippet = 'Koji-san, Ryo-san and team, Thank you for sending your emai | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 108 | 223 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CA0tK15jPm2APp9fC951nD…` | 2025-09-26T17:20:00Z from leonard.hayes@harmonygames.co: Re: Zombie Match 3D access | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 109 | 225 | gmail.gmail_threads | UPDATE | `leonard.hayes@harmonygames.co/1844294398771200047` | snippet = 'Koji-san, Ryo-san and team, Thank you for sending your emai | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 110 | 226 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CA0tK15jPm2APp9fC951nDe6…` | 2025-09-26T17:20:00Z from leonard.hayes@harmonygames.co: Re: Zombie Match 3D access | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 111 | 228 | gmail.gmail_threads | UPDATE | `robert@harmonygames.co/1844294398771200048` | snippet = 'Koji-san, Ryo-san and team, Thank you for sending your emai | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 112 | 229 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpC…` | 2025-09-26T17:20:00Z from leonard.hayes@harmonygames.co: Re: Zombie Match 3D access | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 113 | 231 | gmail.gmail_threads | UPDATE | `arthur.blake@harmonygames.co/1844294398771200049` | snippet = 'Koji-san, Ryo-san and team, Thank you for sending your emai | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 114 | 232 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67…` | 2025-09-26T17:20:00Z from leonard.hayes@harmonygames.co: Re: Zombie Match 3D access | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 115 | 234 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844276782694400053` | Hi Ilse, Thanks for the time this mornin | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 116 | 236 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq_…` | 2025-09-25T22:30:00Z from leonard.hayes@harmonygames.co: Harmony Games - follow up | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 117 | 238 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844276782694400055` | Hi Ilse, Thanks for the time this mornin | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 118 | 240 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2…` | 2025-09-25T22:30:00Z from leonard.hayes@harmonygames.co: Harmony Games - follow up | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 119 | 242 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844276782694400056` | Hi Ilse, Thanks for the time this mornin | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 120 | 244 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a…` | 2025-09-25T22:30:00Z from leonard.hayes@harmonygames.co: Harmony Games - follow up | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 121 | 246 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844276782694400057` | Hi Ilse, Thanks for the time this mornin | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 122 | 248 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-…` | 2025-09-25T22:30:00Z from leonard.hayes@harmonygames.co: Harmony Games - follow up | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 123 | 250 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1844276782694400053` | snippet = 'Thanks Leonard. I''ll brief the partners and come back to y | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 124 | 251 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3…` | 2025-09-26T15:05:00Z from PERSON_9904_EMAIL: Re: Harmony Games - follow up | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 125 | 253 | gmail.gmail_threads | UPDATE | `leonard.hayes@harmonygames.co/1844276782694400055` | snippet = 'Thanks Leonard. I''ll brief the partners and come back to y | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 126 | 254 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GS…` | 2025-09-26T15:05:00Z from PERSON_9904_EMAIL: Re: Harmony Games - follow up | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 127 | 256 | gmail.gmail_threads | UPDATE | `robert@harmonygames.co/1844276782694400056` | snippet = 'Thanks Leonard. I''ll brief the partners and come back to y | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 128 | 257 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFF…` | 2025-09-26T15:05:00Z from PERSON_9904_EMAIL: Re: Harmony Games - follow up | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 129 | 259 | gmail.gmail_threads | UPDATE | `arthur.blake@harmonygames.co/1844276782694400057` | snippet = 'Thanks Leonard. I''ll brief the partners and come back to y | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 130 | 260 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSy…` | 2025-09-26T15:05:00Z from PERSON_9904_EMAIL: Re: Harmony Games - follow up | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 131 | 262 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843992534712320061` | Ilse Marrow and Leonard Hayes Thursday S | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 132 | 264 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-2b67d1aa-cbdd…` | 2025-09-22T19:12:00Z from leonard.hayes@harmonygames.co: Invitation: Ilse Marrow and Leonard Haye | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 133 | 266 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1843992534712320063` | Ilse Marrow and Leonard Hayes Thursday S | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 134 | 268 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-c82c189b-c33c-a6e0-5e4…` | 2025-09-22T19:12:00Z from leonard.hayes@harmonygames.co: Invitation: Ilse Marrow and Leonard Haye | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 135 | 270 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1843992534712320064` | Ilse Marrow and Leonard Hayes Thursday S | **changed/new:** snippet = message snippet; ET wording |
| 136 | 272 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-44faeeb8-a4b0-da…` | 2025-09-22T19:12:00Z from leonard.hayes@harmonygames.co: Invitation: Ilse Marrow and Leonard Haye | **changed/new:** ET wording matches Arthur's calendar (America/New_York) and his base invites (107 Eastern, 11 Pacific); 11:30–12:15 EDT = 15:30–16:15Z = gcal rows |
| 137 | 274 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843718101401600063` | PERSON_5487_NAME and Leonard Hayes Tuesd | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 138 | 276 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-2d8383e3-21d5…` | 2025-09-19T18:30:00Z from leonard.hayes@harmonygames.co: Invitation: PERSON_5487_NAME and Leonard | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 139 | 278 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1843718101401600065` | PERSON_5487_NAME and Leonard Hayes Tuesd | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 140 | 280 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-010d9a7c-8101-ee76-333…` | 2025-09-19T18:30:00Z from leonard.hayes@harmonygames.co: Invitation: PERSON_5487_NAME and Leonard | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 141 | 282 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1843718101401600066` | PERSON_5487_NAME and Leonard Hayes Tuesd | **changed/new:** snippet = message snippet; ET wording |
| 142 | 284 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-9d6c5aee-50ea-1d…` | 2025-09-19T18:30:00Z from leonard.hayes@harmonygames.co: Invitation: PERSON_5487_NAME and Leonard | **changed/new:** 12pm–12:45pm EDT = 16:00–16:45Z = gcal rows; Arthur's calendar America/New_York |
| 143 | 286 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844724105216000067` | Board pre-read review - fundraising Mond | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 144 | 288 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-297f69c9-ad63…` | 2025-09-30T21:00:00Z from leonard.hayes@harmonygames.co: Invitation: Board pre-read review - fund | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 145 | 291 | gcal.gcal_events | INSERT | `evt_2f86b0d4c9e17a35b64e0d` | frederick.stone: Ilse Marrow and Leonard Hayes 2025-09-25T15:30:00Z–16:15:00Z | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 146 | 293 | gcal.gcal_events | INSERT | `evt_b511d4619c6f46ee63959b` | leonard.hayes: Ilse Marrow and Leonard Hayes 2025-09-25T15:30:00Z–16:15:00Z | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 147 | 295 | gcal.gcal_events | INSERT | `evt_8bd5e929463b854ec0ad13` | robert: Ilse Marrow and Leonard Hayes 2025-09-25T15:30:00Z–16:15:00Z | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 148 | 297 | gcal.gcal_events | INSERT | `evt_ca908a712455521f1f8b43` | arthur.blake: Ilse Marrow and Leonard Hayes 2025-09-25T15:30:00Z–16:15:00Z | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 149 | 299 | gcal.gcal_events | INSERT | `evt_7d3e19b04a6c25f8e1b9a0` | frederick.stone: PERSON_5487_NAME and Leonard H 2025-09-23T16:00:00Z–16:45:00Z | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 150 | 301 | gcal.gcal_events | INSERT | `evt_99df25b554cac93e2926fd` | leonard.hayes: PERSON_5487_NAME and Leonard H 2025-09-23T16:00:00Z–16:45:00Z | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 151 | 303 | gcal.gcal_events | INSERT | `evt_671dce00bcb85abb3e355e` | robert: PERSON_5487_NAME and Leonard H 2025-09-23T16:00:00Z–16:45:00Z | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 152 | 305 | gcal.gcal_events | INSERT | `evt_d65aa89778c3ebfa5d97b2` | arthur.blake: PERSON_5487_NAME and Leonard H 2025-09-23T16:00:00Z–16:45:00Z | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 153 | 307 | gcal.gcal_events | INSERT | `evt_9c41e7a2d05b38f6e1a7c4` | frederick.stone: Board pre-read review - fundra 2025-10-06T16:00:00Z–16:45:00Z | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 154 | 309 | gcal.gcal_events | INSERT | `evt_75d8a0687ea57b663a40b0` | leonard.hayes: Board pre-read review - fundra 2025-10-06T16:00:00Z–16:45:00Z | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 155 | 312 | linear.linear_issues | INSERT | `ZOM-567` | Investor testers on ZM internal tracks 2025-09-30T17:10:00Z | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 156 | 314 | linear.linear_comments | INSERT | `lc_94eb35d962cfbdd31e1bd496` | T-Accelerate (Karthic): TestFlight and P 2025-09-30T17:25:00Z | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 157 | 316 | linear.linear_comments | INSERT | `lc_b549f3057640a5eb08f7581e` | Dentsu (3 accounts from Ryo-san, came in 2025-09-30T18:40:00Z | **changed/new:** Arthur's comment; superseded later by his row 59 Slack post (23:20Z), which names ZOM-567 |
| 158 | 319 | contacts.contacts | INSERT | `e3a91c07d5b48f26a0c7e314` | Edith Vane, PERSON_9903_EMAIL | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 159 | 321 | contacts.contacts | INSERT | `b72f0d6e19c3a84e5d21f9a0` | Ilse Marrow, PERSON_9904_EMAIL | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 160 | 323 | contacts.contacts | INSERT | `5d0e8b31f7a29c64e1b0d3a8` | Karthic R, PERSON_3242_EMAIL | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |
| 161 | 325 | contacts.contacts | INSERT | `a4c2e9f07b31d85e6c0f1b29` | Ryo Ishikawa, PERSON_5221_EMAIL | byte-identical to prior version; facts reused (§11); clock, structure and in-SQL duplicates rechecked |

Removed relative to the previous version (no longer applied): Slack `3f2d8f04b29a78808033543c740bb669` (Leonard's notes post), Slack reply `cf10d4f7f88143dc7ab976df27513790` and the UPDATE of base `73c2247f4a31f32d10b3068ecd1d13ac` (which therefore stays at base reply_count 0), Gmail thread `frederick.stone@…/1844162278195200023` + its message, Gmail thread `leonard.hayes@…/1844162278195200025` (re-keyed to `…024`).

## 6. Check A: records, references and IDs

- **References resolve.** New Slack authors are existing accounts: Robert (0016) in #executives, Arthur (0025) and Leonard (0038) in #zombie-match3d, Leonard in the Leonard–Fred DM `D05S58U4SAK`. The UPDATE target `99aa9133…` exists (base reply_count 0, thread_ts null) and gets exactly one reply in the SQL, matching `reply_count = 1, reply_users_count = 1, latest_reply = '1759248360.377105'`. Row 60's `thread_parent_id`/`thread_ts_legacy` point at row 59, inserted earlier. Trello actions reference the card inserted earlier; Leonard's Gmail message references thread `…024`, inserted just before it.
- **No collisions.** 5 new Slack ids: 0 of 610,468 (complete lookup). New ts values absent from their channel files. Trello idShort 456 unused board-wide (max 455), which also makes it the next number. Gmail thread `…024` absent from all 81,404 thread files. Removed rows free their keys; nothing in the SQL still references them. No duplicate keys within the SQL.
- **ID contracts.** Gmail `history_id` NULL on every thread; no Drive row sets `content_path`; new Slack ids are 32-hex like the base.
- **Readable Drive files.** The 3 Google Docs have non-empty `body_text` (432 / 2,685 / 285 chars).
- **One account per person.** No new accounts or contacts in this version; all new rows use existing people's accounts.

## 7. Check B: SQL structure and supported schema rules

- One BEGIN/COMMIT block. Every INSERT names its columns and has one VALUES row of matching length (lint and independent parse, 161 rows). The 11 UPDATEs use primary-key predicates.
- No `_fts` column set. Linear dates use `YYYY-MM-DDTHH:MM:SSZ`; `state_history_json = '[]'` on ZOM-567. All `*_json` values parse with base shapes; the 5 new Slack rows use `metadata_json '{}'` and list-shaped reactions/files/attachments.
- Rewritten template doc: 10 style runs contiguous 0–2,685 = `len(body_text)`; HEADING_2 runs cover exactly "Who goes in the table", "Status, as of end of day Tue Sep 30 (Pacific)", "Money" and "Build access" (each ending in a newline).
- **Provisional snapshot comparison:** MATCH for every column used, except four columns the snapshot doesn't cover (unchanged): `gslides.slides_pages.notes` (all NULL), `gslides.slides_page_elements.table_json` (all NULL) and `.ordinal`, `linear.linear_comments.sequence`. Advisory only (Advisory 1).

## 8. Check C: dates, relationships and consistency

- **Clock.** Every event timestamp is at or before 2025-10-01T07:00Z. Latest: Leonard's #zombie-match3d reply 2025-09-30T23:48Z (16:48 PT). Only plan fields are later (Oct 6 gcal start/end, Trello due 2025-10-14).
- **Treo VC (row 50).** "pinged me again on LinkedIn": base #bridge-pitch 2025-09-03T23:19Z already lists "Treeo VC (inbound b2b AI, Leonard responded on linkedin)", so a repeat ping at 23:31Z the same day is consistent.
- **Play Ventures (row 53).** The added clause cites base messages: Robert in #bridge-pitch 2025-09-25T00:30Z "… from Applovin said … is aware that you reached out", 00:30:20Z "Play Ventures", 01:45Z "\"discussing\"", and Leonard 02:31Z. The correction (16:20Z) comes after them and agrees with base `D04UC0UEN2V` 2025-09-15 "Play (rejected …)".
- **Sciplay (rows 55–56).** Robert's reply "Sciplay's out too" (2025-09-30T16:06Z = 09:06 PT, "this morning") threads under Leonard's base 01:38Z post about not getting into a16z speedrun, so "too" fits. Base Sciplay context (Sep 12 outreach, Sep 15 "before sciplay meeting let's chat") has no later Sciplay answer to conflict with. Removing the old #bridge-pitch reply leaves base `73c2247f…` unchanged.
- **Anton (rows 57–58, 87–88).** Anton emails only Leonard (Cc removed in `cc_json` and headers) on 09-24 16:10Z: $25K, not 40. Leonard's DM to Fred at 16:25Z relays it; DocuSign Completed for "Harmony Games SAFE - Anton Bernstein.pdf" reaches Fred 09-26 19:02Z; Leonard's "Anton signed the 25 one" follows at 19:15Z. The Sep 19 #executives post and the Bridge angels sheet (modified 09-20) still show $40K. That is earlier context the later records correct, not a contradiction. Fred's copy of the email no longer exists, and no other record claims Fred received it.
- **Investor build access (rows 59–60, 157).** Arthur's Linear comment (09-30 18:40Z) says Dentsu's Play internal track was "added Sep 26 (investor tester list)", consistent with Ryo's 09-26 03:10Z email and Leonard's 09-26 17:20Z "Invites … are out to all three of you". Arthur's later Slack post (23:20Z) corrects that: the tester list was never attached to the internal track, so Karthic and the 3 Dentsu testers have no Android yet, though ZOM-567 lists them as added. Leonard's reply (23:48Z) follows it. It is a dated correction by the same author, and it names the record it overrides. Base Gmail has nothing after Leonard's 09-22 links to Karthic (`00015209`, last message 2025-09-22T17:40Z; the other 9 Karthic files end by 09-18), so no base record shows Android access working.
- **Calendar invites in Arthur's mailbox (rows 135–136, 141–142).** "11:30am – 12:15pm Eastern Time" and "12pm – 12:45pm Eastern Time" equal the gcal rows (15:30–16:15Z, 16:00–16:45Z), match Arthur's calendar zone (America/New_York) and match how his base invites render. Fred's and Robert's copies stay in PT, matching their base invite rendering.
- **Trello idShort (rows 64–65, 71–72).** Card idShort, url and all three actions' `data.card.idShort` agree on 456.
- **Template doc (row 8).** The removed sentences are not referenced anywhere else in the SQL. The remaining rules cite only existing things (the Sep 3 kickoff, SVB catch-ups, the investor list's Latest Status column, #bridge-pitch, a16z speedrun, Arthur's tester tracking). Nothing postdates the doc's modified time (2025-09-26T18:41Z) as a past event.
- **Unchanged records.** Chronology, encodings and base agreement for byte-identical rows are reused from the previous review (§11).
- **Grader-facing text.** None. Every new or changed text is in a persona's voice. Nothing addresses a solver or grader or describes the test.

## 9. Findings

No demonstrated defects. Remaining advisory (does not block this stage):

1. **Columns not in the schema snapshot (Check B, provisional, unchanged).** `slides_pages.notes` (all NULL), `slides_page_elements.table_json` (all NULL) and `.ordinal`, and `linear_comments.sequence` appear in neither the snapshot nor the base exports. If a platform table lacks any of them, that INSERT fails and BEGIN/COMMIT rolls back the whole script. No task content depends on them. Smallest fix: drop those four columns and their values, or confirm the script loads on the platform.

## 10. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | All actors, channels, thread parents and UPDATE targets resolve. The 5 new Slack ids, Trello idShort 456 and Gmail thread `…024` don't collide in complete scans. Removed rows leave no dangling references. No ID-contract breaks. Drive files readable. |
| B — SQL structure and supported schema rules | PASS | Structure, JSON shapes, required columns, generated columns, Linear formats and doc style runs are valid. Four columns the snapshot doesn't cover are advisory. Not live-certified. |
| C — Dates, relationships and consistency | PASS | All event times are before the clock. The new and changed Slack, Gmail, Trello, Linear and doc records agree with base Slack, Gmail and the calendar, or are dated corrections the records support. |

Outside certification scope (disclosed, not gates): live execution and current database compatibility (including the four columns), search ranking, Agent visibility and persona access, task difficulty.

## 11. Stage ownership and reuse

Reused evidence (stage-evidence-v1), from `Evals/task_inputs/reports/0_injection.md` as it stood before this rerun, SHA-256 `03e42301b001ea7ec198aa7f44d5190d10d397726cb6655ce75705605cece4aa` (injection-static-v2, PASS/COMPLETE, SQL `3ba2b413…7f87`):

| Item | Source ledger / check | Dependencies verified unchanged |
|---|---|---|
| Collision results for byte-identical rows (Drive, Docs/Sheets/Slides, slide object ids, Trello ids other than idShort, Linear issue/comment ids, Calendar ids/ical_uids, other Gmail ids, 4 contacts, Slack ids of unchanged messages) | previous §4 | universe manifest `da2f4cf0…aac1a`; those ids byte-identical; in-SQL duplicate check rerun on all 161 rows |
| Calendar overlaps and event times | previous §4/§8 | manifest; gcal rows byte-identical |
| Base agreement for unchanged rows (investor list, Initial Capital, 1AM Gaming, Mattel, Hiro, DocuSign, Paul Heydon, Edith Vane, Ilse Marrow, Ryo / Dentsu identity, T-Accelerate comment, ZOM-567, Trello comments, slides) | previous §4/§8 | manifest; those SQL rows byte-identical |

Eval 0, schema snapshot, id_contracts, lint, roster and ACL hashes equal those recorded in the previous report.

`/prompt` may reuse these static checks only while all of these hold: SQL SHA-256 `8481894430080319e947ad672ca3cd9ddfd9e40af102edafed975e0aaadcc0be`, universe manifest `da2f4cf0…aac1a`, schema snapshot `31dcb2b4…`, id_contracts `fc4711ef…`, Eval 0 `e034019b…`, clock 2025-10-01T07:00Z. `/prompt` still owns discoverability and persona access. This SQL changed, so earlier /prompt and /hardness results are outdated; run /prompt, /hardness, /oe and /rubric again in that order.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt, then /hardness (with a fresh run on this SQL), /oe and /rubric. Optionally drop the four snapshot-uncovered columns (Advisory 1) first; that is a new SQL version that needs /injection again.

Evidence limits: Static review only; live load, current database compatibility (incl. four snapshot-uncovered columns), Agent visibility and difficulty are outside scope.
