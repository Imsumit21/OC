# Injection Data-Integrity Review (Eval 0)

Review version: `injection-static-v2`
Evidence contract: `stage-evidence-v1`
Review time: 2026-11-01T23:45Z (actual)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Mode: chat review, attempt 6ae4e299a13034b7eb8305f8 (static, SQL not executed)

## 1. Scope and inputs

| Input | Value |
|---|---|
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` (input revision 8, from chat attachment `01_Universe_Inject (6).sql`), 132,556 bytes, SHA-256 `2e2428bc5e49b2a1fb8da994c4fc4db98ac2208db0eb555682b310fc28fea4ae`. Replaces `01_Universe_Inject (5).sql` (SHA `952e12a9…985a2`), so the earlier injection report no longer applies. |
| Diff from the previous version | Line 3 (header: 147 INSERT); line 23 (Oct 14 template doc body rewritten: inclusion, status, angel, accelerator and "us" rules; "Last two-way contact" section removed); line 87 (slide 9 body: "Firms on Fred's sheet", column list without last-contact); lines 112–119 (**4 new Slack messages** in #bridge-pitch: Treo VC, 1AM Gaming, Play Ventures correction, Mattel RFP); line 124 (Trello Keep-warm comment wording); line 144 (Trello slide comment adds "every row, angels included"); lines 231–245 (Leonard's Ilse follow-up: body, snippets, thread snippets and size_estimate 1114→1152). Everything else is byte-identical (diff against the saved upload, SHA `952e12a9…985a2`). |
| Assignment (context only) | Frederick Stone, Co-founder; Executive / Corporate Ops / Retrieval / long-horizon (not graded here) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Eval | `Evals/0_Injection_Quality_Eval.md` `e034019b8ec450437509a73dd3bae2d303b57561b0f67fcc1e5d19266f663eff` |
| Shared workflow | WORKFLOW.md `ee4cd8e1cc291c3b…` (guide view); scoring.json `c14873e614cdcda5…` |
| Schema snapshot | `references/schema/injection.json` `31dcb2b43feca8e5…` (unverified, provisional) |
| ID contracts | `references/schema/id_contracts.json` `fc4711ef07667333…` |
| Lint | `hg_injection_lint.py` `a8226e2a69425355…`, version `injection-lint-v1` |
| Roster / ACL | roster.json `3f2174513f639e37…`, acl.md `e9bca2b35f98d5ef…` (identity checks only) |

Input/authority issues: none. SQL lines 1–4 are comments, read as evidence of intent only. Line 4 ("re-apply this exact SQL before every agent run") is a setup note in a comment, not text in any injected record, and says nothing about tool calls, pass rate or gates. The header's count (147 INSERT, 11 UPDATE) matches the parsed SQL.

## 2. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, base manifest, review version | NEW, done (saved as input revision 8 before review) |
| Run lint; resolve every flag | NEW, done (0 FAIL, 0 CHECK, 0 INFO) |
| Inventory every statement and affected record | NEW, done: 160 statements (BEGIN line 5, 147 INSERT, 11 UPDATE, COMMIT line 321), 158 row operations, ledger §5 |
| Check A | NEW, PASS |
| Check B | NEW, PASS (provisional snapshot advisory) |
| Check C | NEW, PASS (advisories) |
| Report coverage, findings, limits, one verdict | NEW, done |

Collision scans (all services, including the new Slack ids), reference resolution, JSON/structure checks, doc style runs, Gmail encodings and chronology were rerun on this SQL. Base facts for records whose SQL text is byte-identical to the previous version, against the same universe manifest, were reused with provenance (§11).

## 3. Lint result

`hg_injection_lint.py` on SHA `2e2428bc…fea4ae`, universe synthcut, clock 2025-10-01T07:00Z. Checks: future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape. Base files loaded: contacts, slack users, trello, gmail users, linear, confluence.

Flags: **none** (FAIL 0, CHECK 0, INFO 0). Nothing to resolve. Checks A–C were still run in full.

## 4. Source coverage

| Check | Source / pointer | Coverage | Result |
|---|---|---|---|
| Drive ids (6 new) + 2 parents | gdrive `data.json` `/drive_files` `id` (hg_records) | 53,631 records, complete | New ids absent; parents `d_175c0d7bc72ed244b944cb` (/drive_files/2060, Fred's root) and `d_63fffeb4fab5233ed5bb73` (/drive_files/9030, Leonard's root) exist |
| Docs / Sheets / Slides ids | gdocs `/docs_documents` (595), gsheets `/sheets_spreadsheets` (356), gslides `/slides_presentations` (132), on both `id` and the `*_id` field | complete, 0 errors | no collisions |
| Slide page / element object ids (12 + 23) | reused (§11): exact-string grep of gslides `data.json` | whole file | 0 hits; rows byte-identical except element `el_6548686fe965` text, whose id is unchanged |
| Trello | `/actions` (5,252), `/cards` (803) on `id` and `idShort`, `/checklists` (54), `/check_items` (161), `/boards` (5), `/members` (42), `/lists` (47) | complete | new ids and idShort 466 absent; board `640643a3…318e` (/boards/1), card `68c5a49e…69d0` (/cards/801), member `PERSON_6094_TRELLO_USER_ID` (/members/2, Leonard), list `640643a3…3196` (/lists/4, Doing) exist |
| Linear | `data.json` `/issues` id + identifier (3,687), `/comments` (0), `/users` (41), `/teams` (5) | complete | ZOM-567 and both comment ids absent; `usr_cc3e90160f490686` (/users/35, Arthur) and `team_ZOM` (/teams/4) exist |
| Contacts | `/contacts` (170) on `contact_id` and `email` | complete | 3 new ids and their emails absent |
| Calendar | gcal `/events` (10,395) on `event_id`, `id`, `ical_uid`; `/calendars` (38) | complete | 10 event ids and 3 ical_uids absent; 4 calendars exist (/calendars/0, 10, 15, 29). Overlap check reused (§11; events unchanged) |
| Slack ids (8) | `lookup slack --file 'messages/*.json'` | 4,840 files, 610,468 messages, complete | 0 matches; no `ts` collision in `C096HFA5Z8W/2025-09.json` |
| Slack users / channels | `users.json` (218), `channels.json` (948) | complete | EMPLOYEE_0016 (/9), 0025 (/13), 0038 (/23); `C07C2866011` #executives (/75), `C096HFA5Z8W` #bridge-pitch (/135); all three authors are members of both |
| Gmail thread + message ids (46 unique bare ids) | `grep -rlF` over all `gmail/threads/*.json` | 81,404 files | 0 files contain any id |
| Facts in the 4 new Slack messages | base #bridge-pitch `2025-09.json` (420 msgs, read in full); Gmail threads `frederick@…_1842278301421016623`, `leonard@…_1765976911397037431`, `leonard@…_1843348868615219366`, `00015226`, `00015114`; investor list xlsx rows 10, 38, 69, 72 | read | see §8 |
| Investor list | `gdrive/root/Resource: 7240535625619857401/harmonygames Seed Round Pitch/Game Investor List - Harmony Games 2025.xlsx` (/drive_files/31887), sheet1 parsed | full sheet | columns L Status, M Comments, N Latest Status; rows cited in §8 |
| SVB catch-up (doc rule) | gcal `/events` | complete | "SVB/Harmony Games Inc catch up call" 2025-09-05T20:00Z on Fred's, Leonard's and Arthur's calendars |
| Known base issues | `Evals/references/known_base_issues.md`, `guidelines/known_data_issues.md` | read previously, unchanged | SQL touches no Snowflake/Confluence data and builds on no listed conflict |

## 5. Operation ledger

All 158 row operations in execution order (line = statement start; BEGIN line 5, COMMIT line 321). Parents come before children. Rows marked **(changed in this version)** were checked fresh against the base.

| # | Line | Table | Op | Record / target | Key values | Check result |
|---|---|---|---|---|---|---|
| 1 | 7 | gdrive.drive_files | INSERT | `f_8d2c47a91e05b3f6d7c418` | Board pre-read - fundraising section, parent d_63fffeb4fab5233ed5bb73, owner leonard.hayes, created 2025-07-08T18:00:00Z | new id, no collision; parent resolves |
| 2 | 9 | gdrive.drive_files | INSERT | `f_3b9e61c04d7a52e8f1a6c2` | Board pre-read - fundraising section (Oc…, parent d_63fffeb4fab5233ed5bb73, owner leonard.hayes, created 2025-09-26T18:00:00Z | new id, no collision; parent resolves |
| 3 | 11 | gdrive.drive_files | INSERT | `d_5e8a1c3f9b07d2e64a1b93` | Board - Oct 14 2025, parent d_175c0d7bc72ed244b944cb, owner frederick.stone, created 2025-09-26T18:20:00Z | new id, no collision; parent resolves |
| 4 | 13 | gdrive.drive_files | INSERT | `f_c61a0e93b7d24f58a2e917` | README - Oct 14 board materials, parent d_5e8a1c3f9b07d2e64a1b93, owner leonard.hayes, created 2025-09-26T18:30:00Z | new id, no collision; parent resolves |
| 5 | 15 | gdrive.drive_files | INSERT | `f_a47d0e2c95b18f63e2c0d5` | HG BoD Oct 14 2025 (draft), parent d_63fffeb4fab5233ed5bb73, owner leonard.hayes, created 2025-09-27T17:00:00Z | new id, no collision; parent resolves |
| 6 | 17 | gdrive.drive_files | INSERT | `f_6e1d93a0c4b72f85d39a0e` | Bridge angels, parent d_63fffeb4fab5233ed5bb73, owner leonard.hayes, created 2025-09-19T17:52:00Z | new id, no collision; parent resolves |
| 7 | 20 | gdocs.docs_documents | INSERT | `f_8d2c47a91e05b3f6d7c418` | Board pre-read - fundraising section, body 432 chars, runs contiguous to 432 | readable; Drive row in SQL |
| 8 | 22 | gdocs.docs_documents | INSERT | `f_3b9e61c04d7a52e8f1a6c2` | Board pre-read - fundraising section (Oc…, body 2912 chars, runs contiguous to 2912 | readable; Drive row in SQL **(changed in this version)** |
| 9 | 24 | gdocs.docs_documents | INSERT | `f_c61a0e93b7d24f58a2e917` | README - Oct 14 board materials, body 285 chars, runs contiguous to 285 | readable; Drive row in SQL |
| 10 | 27 | gsheets.sheets_spreadsheets | INSERT | `f_6e1d93a0c4b72f85d39a0e` | Bridge angels | new; parent in SQL |
| 11 | 29 | gsheets.sheets_sheets | INSERT | `f_6e1d93a0c4b72f85d39a0e` | Angels | new; parent in SQL |
| 12 | 32 | gslides.slides_presentations | INSERT | `f_a47d0e2c95b18f63e2c0d5` | HG BoD Oct 14 2025 (draft) | new; Drive row in SQL |
| 13 | 34 | gslides.slides_pages | INSERT | `slide_b4c21ca913ab` | index 0, notes None | unique; id absent from base gslides (reused) |
| 14 | 36 | gslides.slides_page_elements | INSERT | `el_6825f973029b` | on slide_b4c21ca913ab: Harmony Games Board Meeting | unique; id absent from base gslides (reused) |
| 15 | 38 | gslides.slides_page_elements | INSERT | `el_cffa02683868` | on slide_b4c21ca913ab: October 14, 2025 (draft) | unique; id absent from base gslides (reused) |
| 16 | 40 | gslides.slides_pages | INSERT | `slide_256dc0474f7c` | index 1, notes None | unique; id absent from base gslides (reused) |
| 17 | 42 | gslides.slides_page_elements | INSERT | `el_72151261faca` | on slide_256dc0474f7c: Agenda | unique; id absent from base gslides (reused) |
| 18 | 44 | gslides.slides_page_elements | INSERT | `el_ca7b40076cd7` | on slide_256dc0474f7c: Q3 recap / Zombie Match 3D alpha / Engin… | unique; id absent from base gslides (reused) |
| 19 | 46 | gslides.slides_pages | INSERT | `slide_fd6dbd079420` | index 2, notes None | unique; id absent from base gslides (reused) |
| 20 | 48 | gslides.slides_page_elements | INSERT | `el_90fbf6fd9c1b` | on slide_fd6dbd079420: Q3 recap | unique; id absent from base gslides (reused) |
| 21 | 50 | gslides.slides_page_elements | INSERT | `el_ef5243814e8f` | on slide_fd6dbd079420: Domino Delights: publisher search / Zomb… | unique; id absent from base gslides (reused) |
| 22 | 52 | gslides.slides_pages | INSERT | `slide_bb11abfc5fad` | index 3, notes None | unique; id absent from base gslides (reused) |
| 23 | 54 | gslides.slides_page_elements | INSERT | `el_69587907b898` | on slide_bb11abfc5fad: Zombie Match 3D | unique; id absent from base gslides (reused) |
| 24 | 56 | gslides.slides_page_elements | INSERT | `el_6ca8bffe4445` | on slide_bb11abfc5fad: Alpha metrics (Robert to fill) | unique; id absent from base gslides (reused) |
| 25 | 58 | gslides.slides_pages | INSERT | `slide_cb3f0884f833` | index 4, notes None | unique; id absent from base gslides (reused) |
| 26 | 60 | gslides.slides_page_elements | INSERT | `el_0c72e8ba6af7` | on slide_cb3f0884f833: Engine | unique; id absent from base gslides (reused) |
| 27 | 62 | gslides.slides_page_elements | INSERT | `el_1e212bf4628e` | on slide_cb3f0884f833: What shipped in Q3 (Arthur to fill) | unique; id absent from base gslides (reused) |
| 28 | 64 | gslides.slides_pages | INSERT | `slide_a56932e4c738` | index 5, notes None | unique; id absent from base gslides (reused) |
| 29 | 66 | gslides.slides_page_elements | INSERT | `el_5da52b8348b0` | on slide_a56932e4c738: Team | unique; id absent from base gslides (reused) |
| 30 | 68 | gslides.slides_page_elements | INSERT | `el_4f7f04b6e984` | on slide_a56932e4c738: Headcount and contractors (Leonard to fi… | unique; id absent from base gslides (reused) |
| 31 | 70 | gslides.slides_pages | INSERT | `slide_c9c7eed73bb9` | index 6, notes None | unique; id absent from base gslides (reused) |
| 32 | 72 | gslides.slides_page_elements | INSERT | `el_b45885b83bf9` | on slide_c9c7eed73bb9: Runway | unique; id absent from base gslides (reused) |
| 33 | 74 | gslides.slides_page_elements | INSERT | `el_ed13f88ca45b` | on slide_c9c7eed73bb9: Cash and burn (Leonard to fill) | unique; id absent from base gslides (reused) |
| 34 | 76 | gslides.slides_pages | INSERT | `slide_329b5dfcb888` | index 7, notes None | unique; id absent from base gslides (reused) |
| 35 | 78 | gslides.slides_page_elements | INSERT | `el_09521ac10bd5` | on slide_329b5dfcb888: Options | unique; id absent from base gslides (reused) |
| 36 | 80 | gslides.slides_page_elements | INSERT | `el_d65f0ea436c8` | on slide_329b5dfcb888: Bridge / co-dev / engine deals | unique; id absent from base gslides (reused) |
| 37 | 82 | gslides.slides_pages | INSERT | `slide_68eecd4f5f2a` | index 8, notes None | unique; id absent from base gslides (reused) |
| 38 | 84 | gslides.slides_page_elements | INSERT | `el_b87125dbf11e` | on slide_68eecd4f5f2a: Fundraising | unique; id absent from base gslides (reused) |
| 39 | 86 | gslides.slides_page_elements | INSERT | `el_6548686fe965` | on slide_68eecd4f5f2a: Bridge round, pipeline as of Sep 30 / Fi… | unique; id absent from base gslides (reused) **(changed in this version)** |
| 40 | 88 | gslides.slides_pages | INSERT | `slide_98d06d32c8d6` | index 9, notes None | unique; id absent from base gslides (reused) |
| 41 | 90 | gslides.slides_page_elements | INSERT | `el_154065e277bc` | on slide_98d06d32c8d6: Asks for the board | unique; id absent from base gslides (reused) |
| 42 | 92 | gslides.slides_page_elements | INSERT | `el_ee461e258b77` | on slide_98d06d32c8d6: Intros, especially games funds and strat… | unique; id absent from base gslides (reused) |
| 43 | 94 | gslides.slides_pages | INSERT | `slide_fcf2cb38bf31` | index 10, notes None | unique; id absent from base gslides (reused) |
| 44 | 96 | gslides.slides_page_elements | INSERT | `el_8ee884c1e93b` | on slide_fcf2cb38bf31: Appendix | unique; id absent from base gslides (reused) |
| 45 | 98 | gslides.slides_page_elements | INSERT | `el_34bc96464df6` | on slide_fcf2cb38bf31: Investor FAQ (link) | unique; id absent from base gslides (reused) |
| 46 | 100 | gslides.slides_pages | INSERT | `slide_5c7db3c42932` | index 11, notes None | unique; id absent from base gslides (reused) |
| 47 | 102 | gslides.slides_page_elements | INSERT | `el_ef3226341cb0` | on slide_5c7db3c42932: Thank you | unique; id absent from base gslides (reused) |
| 48 | 105 | slack.slack_messages | INSERT | `4921f321db5d08f936aac24a6a1d2af8` | C07C2866011 EMPLOYEE_0038 2025-09-19T17:40:00.000000Z | new id (lookup 610,468 msgs); member; ts = created_at |
| 49 | 107 | slack.slack_messages | INSERT | `7fef94264090696760180223fc8265e7` | C07C2866011 EMPLOYEE_0025 2025-09-29T18:00:00.000000Z | new id (lookup 610,468 msgs); member; ts = created_at |
| 50 | 109 | slack.slack_messages | INSERT | `3f2d8f04b29a78808033543c740bb669` | C096HFA5Z8W EMPLOYEE_0016 2025-09-29T16:00:00.000000Z | new id (lookup 610,468 msgs); member; ts = created_at |
| 51 | 111 | slack.slack_messages | INSERT | `19e1e65d5952f075e8492867c6bcd472` | C096HFA5Z8W EMPLOYEE_0038 2025-09-03T23:31:00.000000Z | new id (lookup 610,468 msgs); member; ts = created_at **(changed in this version)** |
| 52 | 113 | slack.slack_messages | INSERT | `1a68c2da0f36fc25489d3d9bbe9ccc32` | C096HFA5Z8W EMPLOYEE_0038 2025-09-08T21:05:00.000000Z | new id (lookup 610,468 msgs); member; ts = created_at **(changed in this version)** |
| 53 | 115 | slack.slack_messages | INSERT | `c183280a284440a6ca6cdbb5270c9139` | C096HFA5Z8W EMPLOYEE_0038 2025-09-25T16:20:00.000000Z | new id (lookup 610,468 msgs); member; ts = created_at **(changed in this version)** |
| 54 | 117 | slack.slack_messages | INSERT | `398502c0596e5347cc297f61eaefbd50` | C096HFA5Z8W EMPLOYEE_0038 2025-09-26T22:50:00.000000Z | new id (lookup 610,468 msgs); member; ts = created_at **(changed in this version)** |
| 55 | 119 | slack.slack_messages | INSERT | `cf10d4f7f88143dc7ab976df27513790` | C096HFA5Z8W EMPLOYEE_0016 2025-09-29T22:14:00.000000Z, reply to 73c2247f… | new id (lookup 610,468 msgs); member; ts = created_at |
| 56 | 121 | slack.slack_messages | UPDATE | `73c2247f4a31f32d10b3068ecd1d13ac` | reply_count 1, latest_reply 1759184040.552871 | target exists, base reply_count 0 |
| 57 | 123 | trello.trello_actions | INSERT | `68c64270d660c977c4696986` | commentCard 2025-09-14T04:20:00Z card 68c5a49e… | new; id hex time = date **(changed in this version)** |
| 58 | 125 | trello.trello_cards | UPDATE | `68c5a49e8491a9d7faf869d0` | dateLastActivity → 2025-09-14T04:20:00Z | target /cards/801 exists |
| 59 | 126 | trello.trello_boards | UPDATE | `640643a3fd8f3ca308d9318e` | dateLastActivity → 2025-09-27T17:30:24Z | target /boards/1; = latest injected action |
| 60 | 127 | trello.trello_cards | INSERT | `68d8193cf451863621c88a2a` | Board Deck - Oct 14, idShort 466, due 2025-10-14T16:00:00Z (plan) | new id/idShort, no collision |
| 61 | 129 | trello.trello_actions | INSERT | `68d8193c164e823ac3ae735d` | createCard 2025-09-27T17:05:00Z card 68d8193c… | new; id hex time = date |
| 62 | 131 | trello.trello_checklists | INSERT | `68d81ae0bac8fd292e6606f8` | Sections | new; card in SQL |
| 63 | 133 | trello.trello_check_items | INSERT | `68d81ae032fe8d64dbd262c7` | Fundraising - Fred | new; checklist in SQL |
| 64 | 135 | trello.trello_check_items | INSERT | `68d81ae087c12c3d08c79ff8` | Product - Robert | new; checklist in SQL |
| 65 | 137 | trello.trello_check_items | INSERT | `68d81ae05ac90637e942026c` | Engine - Arthur | new; checklist in SQL |
| 66 | 139 | trello.trello_check_items | INSERT | `68d81ae07d46d8fe71f4ba98` | Runway and options - Leonard | new; checklist in SQL |
| 67 | 141 | trello.trello_actions | INSERT | `68d81ae0459a87b4efb4b1e3` | addChecklistToCard 2025-09-27T17:12:00Z card 68d8193c… | new; id hex time = date |
| 68 | 143 | trello.trello_actions | INSERT | `68d81f30a6c94e2b7d05e1f4` | commentCard 2025-09-27T17:30:24Z card 68d8193c… | new; id hex time = date **(changed in this version)** |
| 69 | 146 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844623441920000059` | Fred - for the 14th could you just email the… | new; no collision; id time = first msg |
| 70 | 148 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAdKLID2b1N4D6wzcwD…` | 2025-09-29T18:20:00Z from robert@harmonygames.co: board pipeline | new; date = internal_date = Date hdr; snippet = body prefix |
| 71 | 150 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844623441920000061` | Fred - for the 14th could you just email the… | new; no collision; id time = first msg |
| 72 | 152 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR…` | 2025-09-29T18:20:00Z from robert@harmonygames.co: board pipeline | new; date = internal_date = Date hdr; snippet = body prefix |
| 73 | 154 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844623441920000062` | Fred - for the 14th could you just email the… | new; no collision; id time = first msg |
| 74 | 156 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAdKLID2b1N4D6wzcwD-r…` | 2025-09-29T18:20:00Z from robert@harmonygames.co: board pipeline | new; date = internal_date = Date hdr; snippet = body prefix |
| 75 | 158 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844724419788800011` | Fred, I'm flying to LA tomorrow morning for … | new; no collision; id time = first msg |
| 76 | 160 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAxDeR9CSc9iEY-zACL…` | 2025-09-30T21:05:00Z from leonard.hayes@harmonygames.co: Oct 14 board pre-read - fundraising se… | new; date = internal_date = Date hdr; snippet = body prefix |
| 77 | 162 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844724419788800013` | Fred, I'm flying to LA tomorrow morning for … | new; no collision; id time = first msg |
| 78 | 164 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAxDeR9CSc9iEY-zACLQa…` | 2025-09-30T21:05:00Z from leonard.hayes@harmonygames.co: Oct 14 board pre-read - fundraising se… | new; date = internal_date = Date hdr; snippet = body prefix |
| 79 | 166 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844724419788800014` | Fred, I'm flying to LA tomorrow morning for … | new; no collision; id time = first msg |
| 80 | 168 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5K…` | 2025-09-30T21:05:00Z from leonard.hayes@harmonygames.co: Oct 14 board pre-read - fundraising se… | new; date = internal_date = Date hdr; snippet = body prefix |
| 81 | 170 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844724419788800015` | Fred, I'm flying to LA tomorrow morning for … | new; no collision; id time = first msg |
| 82 | 172 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU…` | 2025-09-30T21:05:00Z from leonard.hayes@harmonygames.co: Oct 14 board pre-read - fundraising se… | new; date = internal_date = Date hdr; snippet = body prefix |
| 83 | 174 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844162278195200023` | Leonard, Had another look at my numbers. I c… | new; no collision; id time = first msg |
| 84 | 176 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CACJhvEE55qdWXuKC3B…` | 2025-09-24T16:10:00Z from PERSON_9901_EMAIL: SAFE amount | new; date = internal_date = Date hdr; snippet = body prefix |
| 85 | 178 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844162278195200025` | Leonard, Had another look at my numbers. I c… | new; no collision; id time = first msg |
| 86 | 180 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CACJhvEE55qdWXuKC3BWl…` | 2025-09-24T16:10:00Z from PERSON_9901_EMAIL: SAFE amount | new; date = internal_date = Date hdr; snippet = body prefix |
| 87 | 182 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844354293432320031` | Hello Frederick Stone, All signers completed… | new; no collision; id time = first msg |
| 88 | 184 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAiKDPIoVSAFUBccUSR…` | 2025-09-26T19:02:00Z from SVC_1302_EMAIL: Completed: Complete with docusign: Har… | new; date = internal_date = Date hdr; snippet = body prefix |
| 89 | 186 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844610859008000037` | Hi Paul, Gentle nudge on the SAFE in DocuSig… | new; no collision; id time = first msg |
| 90 | 188 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAP6Gn2LV490e3El5rB…` | 2025-09-29T15:00:00Z from leonard.hayes@harmonygames.co: SAFE in DocuSign | new; date = internal_date = Date hdr; snippet = body prefix |
| 91 | 190 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844610859008000039` | Hi Paul, Gentle nudge on the SAFE in DocuSig… | new; no collision; id time = first msg |
| 92 | 192 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAP6Gn2LV490e3El5rBDC…` | 2025-09-29T15:00:00Z from leonard.hayes@harmonygames.co: SAFE in DocuSign | new; date = internal_date = Date hdr; snippet = body prefix |
| 93 | 194 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844318935449600041` | Leonard, Thanks again for the session on Tue… | new; no collision; id time = first msg |
| 94 | 196 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq…` | 2025-09-26T09:40:00Z from PERSON_9903_EMAIL: Harmony Games bridge | new; date = internal_date = Date hdr; snippet = body prefix |
| 95 | 198 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844318935449600043` | Leonard, Thanks again for the session on Tue… | new; no collision; id time = first msg |
| 96 | 200 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_l…` | 2025-09-26T09:40:00Z from PERSON_9903_EMAIL: Harmony Games bridge | new; date = internal_date = Date hdr; snippet = body prefix |
| 97 | 202 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844294398771200045` | Leonard-san, Thank you for the offer. Please… | new; no collision; id time = first msg |
| 98 | 204 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAqlOj-B9ZBEdN9-Kft…` | 2025-09-26T03:10:00Z from PERSON_5221_EMAIL: Zombie Match 3D access | new; date = internal_date = Date hdr; snippet = body prefix |
| 99 | 206 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844294398771200047` | Leonard-san, Thank you for the offer. Please… | new; no collision; id time = first msg |
| 100 | 208 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4…` | 2025-09-26T03:10:00Z from PERSON_5221_EMAIL: Zombie Match 3D access | new; date = internal_date = Date hdr; snippet = body prefix |
| 101 | 210 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844294398771200048` | Leonard-san, Thank you for the offer. Please… | new; no collision; id time = first msg |
| 102 | 212 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4kixWZOs…` | 2025-09-26T03:10:00Z from PERSON_5221_EMAIL: Zombie Match 3D access | new; date = internal_date = Date hdr; snippet = body prefix |
| 103 | 214 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844294398771200049` | Leonard-san, Thank you for the offer. Please… | new; no collision; id time = first msg |
| 104 | 216 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4k…` | 2025-09-26T03:10:00Z from PERSON_5221_EMAIL: Zombie Match 3D access | new; date = internal_date = Date hdr; snippet = body prefix |
| 105 | 218 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1844294398771200045` | snippet → latest reply | thread inserted earlier in SQL |
| 106 | 219 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CA0tK15jPm2APp9fC95…` | 2025-09-26T17:20:00Z from leonard.hayes@harmonygames.co: Re: Zombie Match 3D access | new; date = internal_date = Date hdr; snippet = body prefix |
| 107 | 221 | gmail.gmail_threads | UPDATE | `leonard.hayes@harmonygames.co/1844294398771200047` | snippet → latest reply | thread inserted earlier in SQL |
| 108 | 222 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CA0tK15jPm2APp9fC951n…` | 2025-09-26T17:20:00Z from leonard.hayes@harmonygames.co: Re: Zombie Match 3D access | new; date = internal_date = Date hdr; snippet = body prefix |
| 109 | 224 | gmail.gmail_threads | UPDATE | `robert@harmonygames.co/1844294398771200048` | snippet → latest reply | thread inserted earlier in SQL |
| 110 | 225 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjS…` | 2025-09-26T17:20:00Z from leonard.hayes@harmonygames.co: Re: Zombie Match 3D access | new; date = internal_date = Date hdr; snippet = body prefix |
| 111 | 227 | gmail.gmail_threads | UPDATE | `arthur.blake@harmonygames.co/1844294398771200049` | snippet → latest reply | thread inserted earlier in SQL |
| 112 | 228 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CA0tK15jPm2APp9fC951nD…` | 2025-09-26T17:20:00Z from leonard.hayes@harmonygames.co: Re: Zombie Match 3D access | new; date = internal_date = Date hdr; snippet = body prefix |
| 113 | 230 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844276782694400053` | Hi Ilse, Thanks for the time this morning an… | new; no collision; id time = first msg **(changed in this version)** |
| 114 | 232 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAwe90nFO3DL0_sgKjx…` | 2025-09-25T22:30:00Z from leonard.hayes@harmonygames.co: Harmony Games - follow up | new; date = internal_date = Date hdr; snippet = body prefix **(changed in this version)** |
| 115 | 234 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844276782694400055` | Hi Ilse, Thanks for the time this morning an… | new; no collision; id time = first msg **(changed in this version)** |
| 116 | 236 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq…` | 2025-09-25T22:30:00Z from leonard.hayes@harmonygames.co: Harmony Games - follow up | new; date = internal_date = Date hdr; snippet = body prefix **(changed in this version)** |
| 117 | 238 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844276782694400056` | Hi Ilse, Thanks for the time this morning an… | new; no collision; id time = first msg **(changed in this version)** |
| 118 | 240 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1…` | 2025-09-25T22:30:00Z from leonard.hayes@harmonygames.co: Harmony Games - follow up | new; date = internal_date = Date hdr; snippet = body prefix **(changed in this version)** |
| 119 | 242 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844276782694400057` | Hi Ilse, Thanks for the time this morning an… | new; no collision; id time = first msg **(changed in this version)** |
| 120 | 244 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq_…` | 2025-09-25T22:30:00Z from leonard.hayes@harmonygames.co: Harmony Games - follow up | new; date = internal_date = Date hdr; snippet = body prefix **(changed in this version)** |
| 121 | 246 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1844276782694400053` | snippet → latest reply | thread inserted earlier in SQL |
| 122 | 247 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAU-1_oDVchbv0CU8Qh…` | 2025-09-26T15:05:00Z from PERSON_9904_EMAIL: Re: Harmony Games - follow up | new; date = internal_date = Date hdr; snippet = body prefix |
| 123 | 249 | gmail.gmail_threads | UPDATE | `leonard.hayes@harmonygames.co/1844276782694400055` | snippet → latest reply | thread inserted earlier in SQL |
| 124 | 250 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b…` | 2025-09-26T15:05:00Z from PERSON_9904_EMAIL: Re: Harmony Games - follow up | new; date = internal_date = Date hdr; snippet = body prefix |
| 125 | 252 | gmail.gmail_threads | UPDATE | `robert@harmonygames.co/1844276782694400056` | snippet → latest reply | thread inserted earlier in SQL |
| 126 | 253 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9…` | 2025-09-26T15:05:00Z from PERSON_9904_EMAIL: Re: Harmony Games - follow up | new; date = internal_date = Date hdr; snippet = body prefix |
| 127 | 255 | gmail.gmail_threads | UPDATE | `arthur.blake@harmonygames.co/1844276782694400057` | snippet → latest reply | thread inserted earlier in SQL |
| 128 | 256 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3…` | 2025-09-26T15:05:00Z from PERSON_9904_EMAIL: Re: Harmony Games - follow up | new; date = internal_date = Date hdr; snippet = body prefix |
| 129 | 258 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843992534712320061` | Ilse Marrow and Leonard Hayes Thursday Sep 2… | new; no collision; id time = first msg |
| 130 | 260 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-2b67d1aa-c…` | 2025-09-22T19:12:00Z from leonard.hayes@harmonygames.co: Invitation: Ilse Marrow and Leonard Ha… | new; date = internal_date = Date hdr; snippet = body prefix |
| 131 | 262 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1843992534712320063` | Ilse Marrow and Leonard Hayes Thursday Sep 2… | new; no collision; id time = first msg |
| 132 | 264 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-c82c189b-c33c-a6e0-…` | 2025-09-22T19:12:00Z from leonard.hayes@harmonygames.co: Invitation: Ilse Marrow and Leonard Ha… | new; date = internal_date = Date hdr; snippet = body prefix |
| 133 | 266 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1843992534712320064` | Ilse Marrow and Leonard Hayes Thursday Sep 2… | new; no collision; id time = first msg |
| 134 | 268 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-44faeeb8-a4b0…` | 2025-09-22T19:12:00Z from leonard.hayes@harmonygames.co: Invitation: Ilse Marrow and Leonard Ha… | new; date = internal_date = Date hdr; snippet = body prefix |
| 135 | 270 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843718101401600063` | PERSON_5487_NAME and Leonard Hayes Tuesday S… | new; no collision; id time = first msg |
| 136 | 272 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-2d8383e3-2…` | 2025-09-19T18:30:00Z from leonard.hayes@harmonygames.co: Invitation: PERSON_5487_NAME and Leona… | new; date = internal_date = Date hdr; snippet = body prefix |
| 137 | 274 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1843718101401600065` | PERSON_5487_NAME and Leonard Hayes Tuesday S… | new; no collision; id time = first msg |
| 138 | 276 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-010d9a7c-8101-ee76-…` | 2025-09-19T18:30:00Z from leonard.hayes@harmonygames.co: Invitation: PERSON_5487_NAME and Leona… | new; date = internal_date = Date hdr; snippet = body prefix |
| 139 | 278 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1843718101401600066` | PERSON_5487_NAME and Leonard Hayes Tuesday S… | new; no collision; id time = first msg |
| 140 | 280 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-9d6c5aee-50ea…` | 2025-09-19T18:30:00Z from leonard.hayes@harmonygames.co: Invitation: PERSON_5487_NAME and Leona… | new; date = internal_date = Date hdr; snippet = body prefix |
| 141 | 282 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844724105216000067` | Board pre-read review - fundraising Monday O… | new; no collision; id time = first msg |
| 142 | 284 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-297f69c9-a…` | 2025-09-30T21:00:00Z from leonard.hayes@harmonygames.co: Invitation: Board pre-read review - fu… | new; date = internal_date = Date hdr; snippet = body prefix |
| 143 | 287 | gcal.gcal_events | INSERT | `evt_2f86b0d4c9e17a35b64e0d` | frederick.stone: Ilse Marrow and Leonard Hayes 2025-09-25T15:30:00Z–16:15:00Z | new id + ical_uid; no base overlap (reused) |
| 144 | 289 | gcal.gcal_events | INSERT | `evt_b511d4619c6f46ee63959b` | leonard.hayes: Ilse Marrow and Leonard Hayes 2025-09-25T15:30:00Z–16:15:00Z | new id + ical_uid; no base overlap (reused) |
| 145 | 291 | gcal.gcal_events | INSERT | `evt_8bd5e929463b854ec0ad13` | robert: Ilse Marrow and Leonard Hayes 2025-09-25T15:30:00Z–16:15:00Z | new id + ical_uid; no base overlap (reused) |
| 146 | 293 | gcal.gcal_events | INSERT | `evt_ca908a712455521f1f8b43` | arthur.blake: Ilse Marrow and Leonard Hayes 2025-09-25T15:30:00Z–16:15:00Z | new id + ical_uid; no base overlap (reused) |
| 147 | 295 | gcal.gcal_events | INSERT | `evt_7d3e19b04a6c25f8e1b9a0` | frederick.stone: PERSON_5487_NAME and Leonard Hayes 2025-09-23T16:00:00Z–16:45:00Z | new id + ical_uid; no base overlap (reused) |
| 148 | 297 | gcal.gcal_events | INSERT | `evt_99df25b554cac93e2926fd` | leonard.hayes: PERSON_5487_NAME and Leonard Hayes 2025-09-23T16:00:00Z–16:45:00Z | new id + ical_uid; no base overlap (reused) |
| 149 | 299 | gcal.gcal_events | INSERT | `evt_671dce00bcb85abb3e355e` | robert: PERSON_5487_NAME and Leonard Hayes 2025-09-23T16:00:00Z–16:45:00Z | new id + ical_uid; no base overlap (reused) |
| 150 | 301 | gcal.gcal_events | INSERT | `evt_d65aa89778c3ebfa5d97b2` | arthur.blake: PERSON_5487_NAME and Leonard Hayes 2025-09-23T16:00:00Z–16:45:00Z | new id + ical_uid; no base overlap (reused) |
| 151 | 303 | gcal.gcal_events | INSERT | `evt_9c41e7a2d05b38f6e1a7c4` | frederick.stone: Board pre-read review - fundraisin… 2025-10-06T16:00:00Z–16:45:00Z | new id + ical_uid; no base overlap (reused) |
| 152 | 305 | gcal.gcal_events | INSERT | `evt_75d8a0687ea57b663a40b0` | leonard.hayes: Board pre-read review - fundraisin… 2025-10-06T16:00:00Z–16:45:00Z | new id + ical_uid; no base overlap (reused) |
| 153 | 308 | linear.linear_issues | INSERT | `ZOM-567` | team_ZOM, Arthur, Todo, created 2025-09-30T17:10:00Z | new; follows ZOM-566 |
| 154 | 310 | linear.linear_comments | INSERT | `lc_94eb35d962cfbdd31e1bd496` | ZOM-567, 2025-09-30T17:25:00Z | new; issue in SQL |
| 155 | 312 | linear.linear_comments | INSERT | `lc_b549f3057640a5eb08f7581e` | ZOM-567, 2025-09-30T18:40:00Z | new; issue in SQL |
| 156 | 315 | contacts.contacts | INSERT | `e3a91c07d5b48f26a0c7e314` | Edith Vane, PERSON_9903_EMAIL | new id; email not in base contacts |
| 157 | 317 | contacts.contacts | INSERT | `b72f0d6e19c3a84e5d21f9a0` | Ilse Marrow, PERSON_9904_EMAIL | new id; email not in base contacts |
| 158 | 319 | contacts.contacts | INSERT | `5d0e8b31f7a29c64e1b0d3a8` | Karthic R, PERSON_3242_EMAIL | new id; email not in base contacts |

## 6. Check A: records, references and IDs

- **References resolve.** All Drive parents, the Trello board, list, member and existing card (UPDATE targets), the Linear team and user, both Slack channels, all three Slack authors and the Slack thread parent (UPDATE target) exist in the base (§4). Children (docs/sheets/slides rows, slide pages and elements, checklist and items, Linear comments, Gmail messages and the 8 thread-snippet UPDATEs) reference rows inserted earlier in the script. Each UPDATE uses a primary-key predicate that hits exactly one row.
- **No collisions.** Every new key was checked against complete collections (§4), including the 4 new Slack ids (610,468 base messages) and all Gmail ids (81,404 thread files). No duplicate keys within the SQL (checked per table for ids, Slack ts, event ids, slide object ids, Trello ids, contact ids and Linear comment ids). The 10 calendar copies share 3 ical_uids by design, and mailbox copies of one email share a Message-ID under per-user ids, as in the base.
- **ID contracts.** Gmail `history_id` is NULL on every thread (allowed). No Drive row sets `content_path`. The new Slack ids are 32-hex like the base.
- **Readable Drive files.** The 3 Google Docs have docs_documents rows with non-empty `body_text` (432 / 2,912 / 285 chars). The spreadsheet has a sheet row; the presentation has 12 pages and 23 elements.
- **One account per person.** The new Slack messages use Leonard's existing account. External tokens are unchanged from the previous version and map to the same people (§11). PERSON_9901–9904 appear nowhere in the base.

## 7. Check B: SQL structure and supported schema rules

- One BEGIN/COMMIT block. Every INSERT names its columns and has one VALUES row of matching length (lint parsed all 158 rows, 0 INFO). The 11 UPDATEs use primary-key predicates.
- No `_fts` column is set (0 occurrences). Linear dates use `YYYY-MM-DDTHH:MM:SSZ`; `state_history_json = '[]'` is present. Lint `missing_required` and `json_shape`: 0 flags. Every `*_json` value parses (independent check of all 158 rows). The 4 new Slack rows use `metadata_json '{}'` and list-shaped reactions/files/attachments, as in the base.
- Doc style runs are contiguous and end at `len(body_text)` for all three docs, including the rewritten template (10 runs, 0–2,912). Its headings fall on line boundaries ("Who goes in the table", "Status, as of end of day Tue Sep 30 (Pacific)", "Money", "Build access").
- **Provisional snapshot comparison:** MATCH for every column used, except four columns the snapshot doesn't cover (unchanged from the previous version): `gslides.slides_pages.notes` (12 rows, all NULL), `gslides.slides_page_elements.table_json` (23 rows, NULL) and `.ordinal` (23 rows), `linear.linear_comments.sequence` (2 rows). Advisory only (Advisory 2).

## 8. Check C: dates, relationships and consistency

- **Clock.** Every event timestamp is at or before 2025-10-01T07:00Z (latest: Leonard's email 2025-09-30T21:05Z and the Oct 6 invite at 21:00Z). Only plan fields are later: the Oct 6 2025 review events and the Trello card due 2025-10-14T16:00Z. The 4 new Slack messages are dated Sep 3 to Sep 26.
- **New Slack messages, checked against the base:**
  - *Treo VC* (09-03 23:31Z, Leonard): "pinged me on LinkedIn this morning, I sent them the deck and the blurb there". Agrees with base Slack 09-08 15:25Z ("Treeo VC (inbound b2b AI, Leonard responded on linkedin)") and investor-list row 69 ("Inbound so we shared the material"). It comes after Leonard's 09-02 22:10Z "reached out to bunch of linkedin inbounds".
  - *1AM Gaming* (09-08 21:05Z): "1AM Gaming is the March Gaming Fund row on our list, they renamed from March Capital. they passed on the re-seed, I forwarded you guys the email". Agrees with the base thread "Intros: … (1amgaming - formerly March Capital)": the MD's 09-08 20:21Z email ("a re-seed/restructuring is not an opportunity we are going to pursue right now for 1AM Gaming") and Leonard's forward to Robert and Fred at 09-08 20:53Z, 12 minutes before the Slack. List row 38 "March Gaming Fund" (Latest Status "They don't do bridge") fits 1AM's 09-05 "We are not doing bridge rounds".
  - *Play Ventures correction* (09-25 16:20Z): "the no I pasted here on the 15th was what they told Griffin, not us … that's why I said they never answered us". Agrees with the base: the 09-15 16:58Z #bridge-pitch paste of "I'm afraid that's not for us…"; Gmail `leonard@…_1843348868615219366` (09-15 16:41Z), where a Griffin investor (griffingp.com signature) forwards Play Ventures' reply to them; and Leonard's 09-23 23:55Z "they didn't respond" and 09-25 01:44Z "They did not even acknowledge us". The correction comes after all of these.
  - *Mattel* (09-26 22:50Z): "told Mattel we're passing on the Barbie RFP". Follows Leonard's base decline to Mattel at 2025-09-26 15:28 PDT (22:28Z), Gmail `00015226`. See Advisory 1 for the rest of that sentence.
- **Rewritten template doc (line 23).** Its factual references exist in the base: the Sep 3 kickoff, the SVB catch-up (09-05, on Fred's calendar), the list's "Latest Status" column with "as of 09/11" notes, IH / Matthew / advisors, Griffin, the a16z speedrun application (09-12) and its 09-18 call. Nothing in it postdates its modified time (2025-09-26T18:41Z). The slide 9 body and the Trello comment on line 144 match the doc's new columns (firm, status, build access, committed, soft-circled; the last-contact column is gone from all three).
- **Ilse follow-up edit.** Body, the message snippets and thread snippets agree in all 4 mailboxes. size_estimate went up by 38, exactly the added text ("and the questions on the bridge round" + space). Gmail checks on all 37 messages: `internal_date` = `date` = Date header, snippet is a body prefix, thread id = user prefix, final thread snippet = latest message snippet (29/29).
- **Unchanged records.** Chronology, encodings and base agreement for the byte-identical rows were reused from the previous review (§11): Slack ts = created_at, Trello id times, Linear comment order, card/board dateLastActivity, Slack reply counts, calendar times and no calendar overlaps, angel-amount and tester sequences settled by later records.
- **Grader-facing text.** None. Every injected text is in a persona's voice; nothing addresses a solver or grader or describes the test.

## 9. Findings

No demonstrated defects. Advisories (none blocks this stage):

1. **Mattel Slack overstates the history (Check C, advisory).** Line 117 (`398502c0…`, Leonard, 09-26): "that was only ever an RFP and partnership conversation, we didn't pitch them the bridge". The base says otherwise about the pre-round history. Leonard's 2025-08-26 email to Mattel (Gmail `00015114`, Fred, Robert and Arthur cc'd) attached the "board-approved fundraising deck" and proposed "(2) discuss a small strategic investment", with "We're kicking off our raise in early September". His 09-08 tracker lists Mattel under "Other Gaming Companies that might participate", and list row 72's Latest Status reads "I need to follow up with them to see if there is interest from investment stand point". Why this isn't a FAIL: there is a supported reading where both are true. No pitch call or meeting took place after the Sep 3 kickoff, everything sent to Mattel since then was RFP mail (09-04, 09-26), and Mattel never took up the investment track. Under the template's own Sep 3 frame, the Slack line and the base agree on Mattel's in-round status. "Only ever" is still literally wrong about August. If Mattel's row is graded, keep rubric rows and OEs on in-round facts, not on Leonard's "only ever". Smallest fix if you want it airtight: reword to something like "we never pitched them the bridge after the kickoff, since then it's only been the RFP". That is a new SQL version, so /injection would need to run again.
2. **Columns not in the schema snapshot (Check B, provisional).** `slides_pages.notes` (all NULL), `slides_page_elements.table_json` (all NULL) and `.ordinal`, and `linear_comments.sequence` appear in neither the snapshot nor the base exports. If a platform table lacks any of them, that INSERT fails and BEGIN/COMMIT rolls back the whole script. No task content depends on them. Smallest fix: drop those four columns and their values from the INSERTs, or confirm the script loads on the platform.
3. **For /prompt (outside this stage).** The template's exclusion sentence ("Service or work-for-hire deals, banks …, RFPs … don't go in") follows the rule about adding firms not on the list. It doesn't say whether an on-list firm whose talks were RFP-only (Mattel, row 72) is dropped or kept as "Not contacted this round". That is a task-clarity question for /prompt, not a data-integrity defect.

## 10. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | All actors, parents and targets resolve. New keys don't collide in complete scans (§4). No ID-contract breaks. Drive files are readable. No second accounts. |
| B — SQL structure and supported schema rules | PASS | Structure, JSON shapes, required columns, generated columns, Linear formats and doc style runs are valid. Four columns not covered by the snapshot are advisory (Advisory 2). Not live-certified. |
| C — Dates, relationships and consistency | PASS | All event times are before the clock. The new Slack messages agree with base Gmail, Slack and the investor list. Encodings and snippets agree. The Mattel wording is an advisory with a supported reading (Advisory 1). |

Outside certification scope (disclosed, not gates): live execution and current database compatibility (including the four columns), search ranking, Agent visibility and persona access, and task difficulty.

## 11. Stage ownership and reuse

Reused evidence (stage-evidence-v1), from `Evals/task_inputs/reports/0_injection.md` as it stood before this rerun, SHA-256 `bcd2718d0d76a60d9fbe22164410ec85c09ff0738b5e74f183480da6c6988a0a` (injection-static-v2, PASS/COMPLETE, SQL `952e12a9…985a2`):

| Item | Source ledger / check | Dependencies verified unchanged |
|---|---|---|
| Slide page/element object ids absent from base gslides | §4 row "Slide page / element object ids"; ledger rows 13–47 | universe manifest `da2f4cf0…aac1a`; ids byte-identical (only el_6548686fe965's text changed) |
| Calendar overlaps (none) and event times | §4 "Calendar events / ical_uid / overlaps"; §8 | manifest; gcal SQL rows byte-identical (diff); ids and ical_uids rechecked fresh |
| External token identities (PERSON_3242, 5221, 5487, 5282, SVC_1302) and Trello board activity / idShort gap facts | §4; Check A | manifest; SQL rows using them byte-identical |
| Base agreement and settled-conflict facts for unchanged rows (Dentsu, T-Accelerate, Hiro, DocuSign, angels, tester adds) | §8 "Agreement with the base", "Deliberate conflicts" | manifest; those SQL rows byte-identical |

`/prompt` may reuse these static checks only while all of these hold: SQL SHA-256 `2e2428bc5e49b2a1fb8da994c4fc4db98ac2208db0eb555682b310fc28fea4ae`, universe manifest `da2f4cf0…aac1a`, schema snapshot `31dcb2b4…`, id_contracts `fc4711ef…`, Eval 0 `e034019b…`, clock 2025-10-01T07:00Z. `/prompt` still owns discoverability, persona access and the Advisory 3 question. This SQL changed, so the earlier /prompt pass is outdated; run /prompt, /hardness, /oe and /rubric again in that order.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt, then /hardness, /oe and /rubric. Optionally reword the Mattel Slack line (Advisory 1) or drop the four snapshot-uncovered columns (Advisory 2) first; either is a new SQL version that needs /injection again.

Evidence limits: Static review only. The schema snapshot is unverified and doesn't cover slides_pages.notes, slides_page_elements.table_json/ordinal or linear_comments.sequence. Base facts for byte-identical rows were reused with provenance (§11). No live load, tool-visibility or search-ranking checks.
