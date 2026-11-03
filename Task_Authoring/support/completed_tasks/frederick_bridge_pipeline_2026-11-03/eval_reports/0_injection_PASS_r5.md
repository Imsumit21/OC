# Injection Data-Integrity Review (Eval 0)

Review version: `injection-static-v2`
Evidence contract: `stage-evidence-v1`
Review time: 2026-11-02T01:38Z (actual)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Mode: chat review, attempt 6ae4e299a13034b7eb8305f8 (static, SQL not executed)

## 1. Scope and inputs

| Input | Value |
|---|---|
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` (input revision 9, from chat attachment `01_Universe_Inject (7).sql`), 133,264 bytes, SHA-256 `3ba2b413458f437b3bac5c3ebae97ec7009afb6965ef8017341bf5873cca7f87`. Replaces `01_Universe_Inject (6).sql` (SHA `2e2428bc…fea4ae`), so the earlier injection report no longer applies. |
| Diff from the previous version | Line 3 (header: 149 INSERT); line 23 (Oct 14 template doc: accelerator sentence extended, "the program's decision and the feedback that comes with it aren't their answer on the bridge; that has to come on our bridge thread with them or in #bridge-pitch"; style runs shifted, body 2,912 → 3,018); line 45 (agenda slide body now "… / Engine / Team / Runway and options / Fundraising"); lines 113–114 (**new Slack message** in #bridge-pitch, Leonard, Initial Capital, 2025-09-09T18:20Z); line 120 (Mattel Slack reworded to "since the kickoff that's only been an RFP conversation"); lines 233–247 (Ilse follow-up: sentence "I'll send the deck and the puzzle engine doc over in a separate email." removed; snippets and size_estimate 1152 → 1081); line 311 (ZOM-567 description); lines 313/315 (Linear comments: T-Accelerate "TestFlight and Play internal track both added Sep 22"; Dentsu "TestFlight added Sep 26 … their work addresses aren't Google accounts so Play won't take them"); lines 323–324 (**new contact** Ryo Ishikawa, PERSON_5221_EMAIL). Everything else is byte-identical (diff against saved upload `01_Universe_Inject (6).sql`). |
| Assignment (context only) | Frederick Stone, Co-founder; not graded here |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Eval | `Evals/0_Injection_Quality_Eval.md` `e034019b8ec450437509a73dd3bae2d303b57561b0f67fcc1e5d19266f663eff` |
| Shared workflow | `hg_reference.py guide injection` view (WORKFLOW sections + scoring groups), with slack/contacts/linear/gmail routes and schema tables |
| Schema snapshot | `references/schema/injection.json` `31dcb2b43feca8e5…` (unverified, provisional) |
| ID contracts | `references/schema/id_contracts.json` `fc4711ef07667333…` |
| Lint | `hg_injection_lint.py` `a8226e2a69425355…`, version `injection-lint-v1` |
| Roster / ACL | roster.json `3f2174513f639e37…`, acl.md `e9bca2b35f98d5ef…` (identity checks only) |

Input/authority issues: none. SQL comment lines are evidence of intent only; none addresses a grader or mentions tool calls, pass rate or gates. The header count (149 INSERT, 11 UPDATE) matches the parsed SQL.

## 2. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, base manifest, review version | NEW, done (saved as input revision 9 before review) |
| Run lint; resolve every flag | NEW, done (0 FAIL, 0 CHECK, 0 INFO) |
| Inventory every statement and affected record | NEW, done: 162 statements (BEGIN line 5, 149 INSERT, 11 UPDATE, COMMIT line 325), 160 row operations, ledger §5 |
| Check A | NEW, PASS |
| Check B | NEW, PASS (provisional snapshot advisory) |
| Check C | NEW, PASS |
| Report coverage, findings, limits, one verdict | NEW, done |

Independent static parse of all 162 statements: column/value counts match on every INSERT, no duplicate columns, every `*_json` value parses, no event timestamp after the clock, Slack ts = created_at on all 9 messages, doc style runs contiguous, Linear text dates in `YYYY-MM-DDTHH:MM:SSZ`, Gmail snippet = body prefix and internal_date = date on all 37 messages, no duplicate keys within the SQL.

## 3. Lint result

`hg_injection_lint.py` on SHA `3ba2b413…7f87`, universe synthcut, clock 2025-10-01T07:00Z. Base files loaded: contacts, slack users, trello, gmail users, linear, confluence. Tables parsed include contacts.contacts (4 inserts).

Flags: **none** (FAIL 0, CHECK 0, INFO 0). Nothing to resolve. Checks A–C were still run in full.

## 4. Source coverage

| Check | Source / pointer | Coverage | Result |
|---|---|---|---|
| Drive ids (6 new) + 2 parents | gdrive `data.json` `/drive_files` `id` (hg_records) | 53,631 records, complete | New ids absent; parents `d_175c0d7bc72ed244b944cb` (/drive_files/2060, Fred's root) and `d_63fffeb4fab5233ed5bb73` (/drive_files/9030, Leonard's root) exist |
| Docs / Sheets / Slides ids | gdocs `/docs_documents` (595), gsheets `/sheets_spreadsheets` (356), gslides `/slides_presentations` (132), on both `id` and the `*_id` field | complete, 0 errors | no collisions |
| Slide page / element object ids (12 + 23) | reused (§11): exact-string grep of gslides `data.json` | whole file | 0 hits; rows byte-identical except element `el_6548686fe965` text, whose id is unchanged |
| Trello | `/actions` (5,252), `/cards` (803) on `id` and `idShort`, `/checklists` (54), `/check_items` (161), `/boards` (5), `/members` (42), `/lists` (47) | complete | new ids and idShort 466 absent; board `640643a3…318e` (/boards/1), card `68c5a49e…69d0` (/cards/801), member `PERSON_6094_TRELLO_USER_ID` (/members/2, Leonard), list `640643a3…3196` (/lists/4, Doing) exist |
| Linear | `data.json` `/issues` id + identifier (3,687), `/comments` (0), `/users` (41), `/teams` (5) | complete | ZOM-567 and both comment ids absent; `usr_cc3e90160f490686` (/users/35, Arthur) and `team_ZOM` (/teams/4) exist |
| Contacts | `/contacts` (170) on `contact_id` and `email` | complete | 4 new ids and their emails absent (incl. `a4c2e9f0…1b29` / PERSON_5221_EMAIL); no Ryo / Ishikawa / Dentsu contact |
| Calendar | gcal `/events` (10,395) on `event_id`, `id`, `ical_uid`; `/calendars` (38) | complete | 10 event ids and 3 ical_uids absent; 4 calendars exist (/calendars/0, 10, 15, 29). Overlap check reused (§11; events unchanged) |
| Slack ids (9, incl. new `800870c5…63e6`) | `lookup slack --file 'messages/*.json' --key id` | 4,840 files, 610,468 messages, complete, 0 errors | 0 matches; ts `1757442000.492583` absent from all message files (grep) |
| Slack users / channels | `users.json` (218), `channels.json` (948) | complete | EMPLOYEE_0016 (/9), 0025 (/13), 0038 (/23); `C07C2866011` #executives (/75), `C096HFA5Z8W` #bridge-pitch (/135); all three authors are members of both |
| Gmail thread + message ids (46 unique bare ids) | `grep -rlF` over all `gmail/threads/*.json` | 81,404 files | 0 files contain any id |
| Facts in the Slack messages added in revision 8 | base #bridge-pitch `2025-09.json` (420 msgs, read in full); Gmail threads `frederick@…_1842278301421016623`, `leonard@…_1765976911397037431`, `leonard@…_1843348868615219366`, `00015226`, `00015114`; investor list xlsx rows 10, 38, 69, 72 | read | see §8 |
| Investor list | `gdrive/root/Resource: 7240535625619857401/harmonygames Seed Round Pitch/Game Investor List - Harmony Games 2025.xlsx` (/drive_files/31887), sheet1 parsed | full sheet | columns L Status, M Comments, N Latest Status; rows cited in §8 |
| SVB catch-up (doc rule) | gcal `/events` | complete | "SVB/Harmony Games Inc catch up call" 2025-09-05T20:00Z on Fred's, Leonard's and Arthur's calendars |
| Known base issues | `Evals/references/known_base_issues.md`, `guidelines/known_data_issues.md` | read previously, unchanged | SQL touches no Snowflake/Confluence data and builds on no listed conflict |
| Facts in the changed / new rows of this version | Investor list row 17 (Initial Capital); base Slack 2025 scan for Initial Capital / Mattel / T-Accelerate (all channels, 2025-08 and 2025-09 files); Gmail `00015209` (T-Accelerate, Karthic), `00015226` + mailbox copies (Mattel RFP), `00015114` (Mattel, Aug 26), `00015338` + mailbox copies (Dentsu); injected Ryo email (SQL lines 204–219) | read in full | see §8 |
| PERSON_5221 identity | grep of all 81,404 Gmail thread files for `PERSON_5221_EMAIL` | 7 files | all Dentsu threads; header names it 石川 遼 (Ishikawa Ryo), addressed as "Ryo-san" |

## 5. Operation ledger

All 160 row operations in execution order (line = statement start; BEGIN line 5, COMMIT line 325). Parents come before children. Rows marked **(changed in this version)** or **(new in this version)** were checked fresh against the base; other rows are byte-identical to the previous version and their base facts were reused with provenance (§11), while collisions, structure and clock were rechecked on the whole script.

| # | Line | Table | Op | Record / target | Key values | Check result |
|---|---|---|---|---|---|---|
| 1 | 7 | gdrive.drive_files | INSERT | `f_8d2c47a91e05b3f6d7c418` | Board pre-read - fundraising section, parent d_63fffeb4fab5233ed5bb73, owner leonard.hayes, created 2025-07-08T18:00:00Z | new id, no collision; parent resolves |
| 2 | 9 | gdrive.drive_files | INSERT | `f_3b9e61c04d7a52e8f1a6c2` | Board pre-read - fundraising section (Oc…, parent d_63fffeb4fab5233ed5bb73, owner leonard.hayes, created 2025-09-26T18:00:00Z | new id, no collision; parent resolves |
| 3 | 11 | gdrive.drive_files | INSERT | `d_5e8a1c3f9b07d2e64a1b93` | Board - Oct 14 2025, parent d_175c0d7bc72ed244b944cb, owner frederick.stone, created 2025-09-26T18:20:00Z | new id, no collision; parent resolves |
| 4 | 13 | gdrive.drive_files | INSERT | `f_c61a0e93b7d24f58a2e917` | README - Oct 14 board materials, parent d_5e8a1c3f9b07d2e64a1b93, owner leonard.hayes, created 2025-09-26T18:30:00Z | new id, no collision; parent resolves |
| 5 | 15 | gdrive.drive_files | INSERT | `f_a47d0e2c95b18f63e2c0d5` | HG BoD Oct 14 2025 (draft), parent d_63fffeb4fab5233ed5bb73, owner leonard.hayes, created 2025-09-27T17:00:00Z | new id, no collision; parent resolves |
| 6 | 17 | gdrive.drive_files | INSERT | `f_6e1d93a0c4b72f85d39a0e` | Bridge angels, parent d_63fffeb4fab5233ed5bb73, owner leonard.hayes, created 2025-09-19T17:52:00Z | new id, no collision; parent resolves |
| 7 | 20 | gdocs.docs_documents | INSERT | `f_8d2c47a91e05b3f6d7c418` | Board pre-read - fundraising section, body 432 chars, runs contiguous to 432 | readable; Drive row in SQL |
| 8 | 22 | gdocs.docs_documents | INSERT | `f_3b9e61c04d7a52e8f1a6c2` | Board pre-read - fundraising section (Oc…, body 3018 chars, runs contiguous to 3018 | readable; Drive row in SQL **(changed in this version)** |
| 9 | 24 | gdocs.docs_documents | INSERT | `f_c61a0e93b7d24f58a2e917` | README - Oct 14 board materials, body 285 chars, runs contiguous to 285 | readable; Drive row in SQL |
| 10 | 27 | gsheets.sheets_spreadsheets | INSERT | `f_6e1d93a0c4b72f85d39a0e` | Bridge angels | new; parent in SQL |
| 11 | 29 | gsheets.sheets_sheets | INSERT | `f_6e1d93a0c4b72f85d39a0e` | Angels | new; parent in SQL |
| 12 | 32 | gslides.slides_presentations | INSERT | `f_a47d0e2c95b18f63e2c0d5` | HG BoD Oct 14 2025 (draft) | new; Drive row in SQL |
| 13 | 34 | gslides.slides_pages | INSERT | `slide_b4c21ca913ab` | index 0, notes None | unique; id absent from base gslides (reused) |
| 14 | 36 | gslides.slides_page_elements | INSERT | `el_6825f973029b` | on slide_b4c21ca913ab: Harmony Games Board Meeting | unique; id absent from base gslides (reused) |
| 15 | 38 | gslides.slides_page_elements | INSERT | `el_cffa02683868` | on slide_b4c21ca913ab: October 14, 2025 (draft) | unique; id absent from base gslides (reused) |
| 16 | 40 | gslides.slides_pages | INSERT | `slide_256dc0474f7c` | index 1, notes None | unique; id absent from base gslides (reused) |
| 17 | 42 | gslides.slides_page_elements | INSERT | `el_72151261faca` | on slide_256dc0474f7c: Agenda | unique; id absent from base gslides (reused) |
| 18 | 44 | gslides.slides_page_elements | INSERT | `el_ca7b40076cd7` | on slide_256dc0474f7c: Q3 recap / Zombie Match 3D alpha / Engin… | unique; id absent from base gslides (reused) **(changed in this version)** |
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
| 39 | 86 | gslides.slides_page_elements | INSERT | `el_6548686fe965` | on slide_68eecd4f5f2a: Bridge round, pipeline as of Sep 30 / Fi… | unique; id absent from base gslides (reused) |
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
| 51 | 111 | slack.slack_messages | INSERT | `19e1e65d5952f075e8492867c6bcd472` | C096HFA5Z8W EMPLOYEE_0038 2025-09-03T23:31:00.000000Z | new id (lookup 610,468 msgs); member; ts = created_at |
| 52 | 113 | slack.slack_messages | INSERT | `800870c56bda852a57dfa06cb4fd63e6` | C096HFA5Z8W EMPLOYEE_0038 2025-09-09T18:20:00.000000Z | new id (lookup 610,468 msgs); no ts collision; member; ts = created_at **(new in this version)** |
| 53 | 115 | slack.slack_messages | INSERT | `1a68c2da0f36fc25489d3d9bbe9ccc32` | C096HFA5Z8W EMPLOYEE_0038 2025-09-08T21:05:00.000000Z | new id (lookup 610,468 msgs); member; ts = created_at |
| 54 | 117 | slack.slack_messages | INSERT | `c183280a284440a6ca6cdbb5270c9139` | C096HFA5Z8W EMPLOYEE_0038 2025-09-25T16:20:00.000000Z | new id (lookup 610,468 msgs); member; ts = created_at |
| 55 | 119 | slack.slack_messages | INSERT | `398502c0596e5347cc297f61eaefbd50` | C096HFA5Z8W EMPLOYEE_0038 2025-09-26T22:50:00.000000Z | new id (lookup 610,468 msgs); member; ts = created_at **(changed in this version)** |
| 56 | 121 | slack.slack_messages | INSERT | `cf10d4f7f88143dc7ab976df27513790` | C096HFA5Z8W EMPLOYEE_0016 2025-09-29T22:14:00.000000Z, reply to 73c2247f… | new id (lookup 610,468 msgs); member; ts = created_at |
| 57 | 123 | slack.slack_messages | UPDATE | `73c2247f4a31f32d10b3068ecd1d13ac` | reply_count 1, latest_reply 1759184040.552871 | target exists, base reply_count 0 |
| 58 | 125 | trello.trello_actions | INSERT | `68c64270d660c977c4696986` | commentCard 2025-09-14T04:20:00Z card 68c5a49e… | new; id hex time = date |
| 59 | 127 | trello.trello_cards | UPDATE | `68c5a49e8491a9d7faf869d0` | dateLastActivity → 2025-09-14T04:20:00Z | target /cards/801 exists |
| 60 | 128 | trello.trello_boards | UPDATE | `640643a3fd8f3ca308d9318e` | dateLastActivity → 2025-09-27T17:30:24Z | target /boards/1; = latest injected action |
| 61 | 129 | trello.trello_cards | INSERT | `68d8193cf451863621c88a2a` | Board Deck - Oct 14, idShort 466, due 2025-10-14T16:00:00Z (plan) | new id/idShort, no collision |
| 62 | 131 | trello.trello_actions | INSERT | `68d8193c164e823ac3ae735d` | createCard 2025-09-27T17:05:00Z card 68d8193c… | new; id hex time = date |
| 63 | 133 | trello.trello_checklists | INSERT | `68d81ae0bac8fd292e6606f8` | Sections | new; card in SQL |
| 64 | 135 | trello.trello_check_items | INSERT | `68d81ae032fe8d64dbd262c7` | Fundraising - Fred | new; checklist in SQL |
| 65 | 137 | trello.trello_check_items | INSERT | `68d81ae087c12c3d08c79ff8` | Product - Robert | new; checklist in SQL |
| 66 | 139 | trello.trello_check_items | INSERT | `68d81ae05ac90637e942026c` | Engine - Arthur | new; checklist in SQL |
| 67 | 141 | trello.trello_check_items | INSERT | `68d81ae07d46d8fe71f4ba98` | Runway and options - Leonard | new; checklist in SQL |
| 68 | 143 | trello.trello_actions | INSERT | `68d81ae0459a87b4efb4b1e3` | addChecklistToCard 2025-09-27T17:12:00Z card 68d8193c… | new; id hex time = date |
| 69 | 145 | trello.trello_actions | INSERT | `68d81f30a6c94e2b7d05e1f4` | commentCard 2025-09-27T17:30:24Z card 68d8193c… | new; id hex time = date |
| 70 | 148 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844623441920000059` | Fred - for the 14th could you just email the… | new; no collision; id time = first msg |
| 71 | 150 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAdKLID2b1N4D6wzcwD…` | 2025-09-29T18:20:00Z from robert@harmonygames.co: board pipeline | new; date = internal_date = Date hdr; snippet = body prefix |
| 72 | 152 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844623441920000061` | Fred - for the 14th could you just email the… | new; no collision; id time = first msg |
| 73 | 154 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR…` | 2025-09-29T18:20:00Z from robert@harmonygames.co: board pipeline | new; date = internal_date = Date hdr; snippet = body prefix |
| 74 | 156 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844623441920000062` | Fred - for the 14th could you just email the… | new; no collision; id time = first msg |
| 75 | 158 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAdKLID2b1N4D6wzcwD-r…` | 2025-09-29T18:20:00Z from robert@harmonygames.co: board pipeline | new; date = internal_date = Date hdr; snippet = body prefix |
| 76 | 160 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844724419788800011` | Fred, I'm flying to LA tomorrow morning for … | new; no collision; id time = first msg |
| 77 | 162 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAxDeR9CSc9iEY-zACL…` | 2025-09-30T21:05:00Z from leonard.hayes@harmonygames.co: Oct 14 board pre-read - fundraising se… | new; date = internal_date = Date hdr; snippet = body prefix |
| 78 | 164 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844724419788800013` | Fred, I'm flying to LA tomorrow morning for … | new; no collision; id time = first msg |
| 79 | 166 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAxDeR9CSc9iEY-zACLQa…` | 2025-09-30T21:05:00Z from leonard.hayes@harmonygames.co: Oct 14 board pre-read - fundraising se… | new; date = internal_date = Date hdr; snippet = body prefix |
| 80 | 168 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844724419788800014` | Fred, I'm flying to LA tomorrow morning for … | new; no collision; id time = first msg |
| 81 | 170 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5K…` | 2025-09-30T21:05:00Z from leonard.hayes@harmonygames.co: Oct 14 board pre-read - fundraising se… | new; date = internal_date = Date hdr; snippet = body prefix |
| 82 | 172 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844724419788800015` | Fred, I'm flying to LA tomorrow morning for … | new; no collision; id time = first msg |
| 83 | 174 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU…` | 2025-09-30T21:05:00Z from leonard.hayes@harmonygames.co: Oct 14 board pre-read - fundraising se… | new; date = internal_date = Date hdr; snippet = body prefix |
| 84 | 176 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844162278195200023` | Leonard, Had another look at my numbers. I c… | new; no collision; id time = first msg |
| 85 | 178 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CACJhvEE55qdWXuKC3B…` | 2025-09-24T16:10:00Z from PERSON_9901_EMAIL: SAFE amount | new; date = internal_date = Date hdr; snippet = body prefix |
| 86 | 180 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844162278195200025` | Leonard, Had another look at my numbers. I c… | new; no collision; id time = first msg |
| 87 | 182 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CACJhvEE55qdWXuKC3BWl…` | 2025-09-24T16:10:00Z from PERSON_9901_EMAIL: SAFE amount | new; date = internal_date = Date hdr; snippet = body prefix |
| 88 | 184 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844354293432320031` | Hello Frederick Stone, All signers completed… | new; no collision; id time = first msg |
| 89 | 186 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAiKDPIoVSAFUBccUSR…` | 2025-09-26T19:02:00Z from SVC_1302_EMAIL: Completed: Complete with docusign: Har… | new; date = internal_date = Date hdr; snippet = body prefix |
| 90 | 188 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844610859008000037` | Hi Paul, Gentle nudge on the SAFE in DocuSig… | new; no collision; id time = first msg |
| 91 | 190 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAP6Gn2LV490e3El5rB…` | 2025-09-29T15:00:00Z from leonard.hayes@harmonygames.co: SAFE in DocuSign | new; date = internal_date = Date hdr; snippet = body prefix |
| 92 | 192 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844610859008000039` | Hi Paul, Gentle nudge on the SAFE in DocuSig… | new; no collision; id time = first msg |
| 93 | 194 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAP6Gn2LV490e3El5rBDC…` | 2025-09-29T15:00:00Z from leonard.hayes@harmonygames.co: SAFE in DocuSign | new; date = internal_date = Date hdr; snippet = body prefix |
| 94 | 196 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844318935449600041` | Leonard, Thanks again for the session on Tue… | new; no collision; id time = first msg |
| 95 | 198 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq…` | 2025-09-26T09:40:00Z from PERSON_9903_EMAIL: Harmony Games bridge | new; date = internal_date = Date hdr; snippet = body prefix |
| 96 | 200 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844318935449600043` | Leonard, Thanks again for the session on Tue… | new; no collision; id time = first msg |
| 97 | 202 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_l…` | 2025-09-26T09:40:00Z from PERSON_9903_EMAIL: Harmony Games bridge | new; date = internal_date = Date hdr; snippet = body prefix |
| 98 | 204 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844294398771200045` | Leonard-san, Thank you for the offer. Please… | new; no collision; id time = first msg |
| 99 | 206 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAqlOj-B9ZBEdN9-Kft…` | 2025-09-26T03:10:00Z from PERSON_5221_EMAIL: Zombie Match 3D access | new; date = internal_date = Date hdr; snippet = body prefix |
| 100 | 208 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844294398771200047` | Leonard-san, Thank you for the offer. Please… | new; no collision; id time = first msg |
| 101 | 210 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4…` | 2025-09-26T03:10:00Z from PERSON_5221_EMAIL: Zombie Match 3D access | new; date = internal_date = Date hdr; snippet = body prefix |
| 102 | 212 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844294398771200048` | Leonard-san, Thank you for the offer. Please… | new; no collision; id time = first msg |
| 103 | 214 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4kixWZOs…` | 2025-09-26T03:10:00Z from PERSON_5221_EMAIL: Zombie Match 3D access | new; date = internal_date = Date hdr; snippet = body prefix |
| 104 | 216 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844294398771200049` | Leonard-san, Thank you for the offer. Please… | new; no collision; id time = first msg |
| 105 | 218 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4k…` | 2025-09-26T03:10:00Z from PERSON_5221_EMAIL: Zombie Match 3D access | new; date = internal_date = Date hdr; snippet = body prefix |
| 106 | 220 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1844294398771200045` | snippet → latest reply | thread inserted earlier in SQL |
| 107 | 221 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CA0tK15jPm2APp9fC95…` | 2025-09-26T17:20:00Z from leonard.hayes@harmonygames.co: Re: Zombie Match 3D access | new; date = internal_date = Date hdr; snippet = body prefix |
| 108 | 223 | gmail.gmail_threads | UPDATE | `leonard.hayes@harmonygames.co/1844294398771200047` | snippet → latest reply | thread inserted earlier in SQL |
| 109 | 224 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CA0tK15jPm2APp9fC951n…` | 2025-09-26T17:20:00Z from leonard.hayes@harmonygames.co: Re: Zombie Match 3D access | new; date = internal_date = Date hdr; snippet = body prefix |
| 110 | 226 | gmail.gmail_threads | UPDATE | `robert@harmonygames.co/1844294398771200048` | snippet → latest reply | thread inserted earlier in SQL |
| 111 | 227 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjS…` | 2025-09-26T17:20:00Z from leonard.hayes@harmonygames.co: Re: Zombie Match 3D access | new; date = internal_date = Date hdr; snippet = body prefix |
| 112 | 229 | gmail.gmail_threads | UPDATE | `arthur.blake@harmonygames.co/1844294398771200049` | snippet → latest reply | thread inserted earlier in SQL |
| 113 | 230 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CA0tK15jPm2APp9fC951nD…` | 2025-09-26T17:20:00Z from leonard.hayes@harmonygames.co: Re: Zombie Match 3D access | new; date = internal_date = Date hdr; snippet = body prefix |
| 114 | 232 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844276782694400053` | Hi Ilse, Thanks for the time this morning an… | new; no collision; id time = first msg **(changed in this version)** |
| 115 | 234 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAwe90nFO3DL0_sgKjx…` | 2025-09-25T22:30:00Z from leonard.hayes@harmonygames.co: Harmony Games - follow up | new; date = internal_date = Date hdr; snippet = body prefix **(changed in this version)** |
| 116 | 236 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844276782694400055` | Hi Ilse, Thanks for the time this morning an… | new; no collision; id time = first msg **(changed in this version)** |
| 117 | 238 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq…` | 2025-09-25T22:30:00Z from leonard.hayes@harmonygames.co: Harmony Games - follow up | new; date = internal_date = Date hdr; snippet = body prefix **(changed in this version)** |
| 118 | 240 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844276782694400056` | Hi Ilse, Thanks for the time this morning an… | new; no collision; id time = first msg **(changed in this version)** |
| 119 | 242 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1…` | 2025-09-25T22:30:00Z from leonard.hayes@harmonygames.co: Harmony Games - follow up | new; date = internal_date = Date hdr; snippet = body prefix **(changed in this version)** |
| 120 | 244 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844276782694400057` | Hi Ilse, Thanks for the time this morning an… | new; no collision; id time = first msg **(changed in this version)** |
| 121 | 246 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq_…` | 2025-09-25T22:30:00Z from leonard.hayes@harmonygames.co: Harmony Games - follow up | new; date = internal_date = Date hdr; snippet = body prefix **(changed in this version)** |
| 122 | 248 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1844276782694400053` | snippet → latest reply | thread inserted earlier in SQL |
| 123 | 249 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAU-1_oDVchbv0CU8Qh…` | 2025-09-26T15:05:00Z from PERSON_9904_EMAIL: Re: Harmony Games - follow up | new; date = internal_date = Date hdr; snippet = body prefix |
| 124 | 251 | gmail.gmail_threads | UPDATE | `leonard.hayes@harmonygames.co/1844276782694400055` | snippet → latest reply | thread inserted earlier in SQL |
| 125 | 252 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b…` | 2025-09-26T15:05:00Z from PERSON_9904_EMAIL: Re: Harmony Games - follow up | new; date = internal_date = Date hdr; snippet = body prefix |
| 126 | 254 | gmail.gmail_threads | UPDATE | `robert@harmonygames.co/1844276782694400056` | snippet → latest reply | thread inserted earlier in SQL |
| 127 | 255 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9…` | 2025-09-26T15:05:00Z from PERSON_9904_EMAIL: Re: Harmony Games - follow up | new; date = internal_date = Date hdr; snippet = body prefix |
| 128 | 257 | gmail.gmail_threads | UPDATE | `arthur.blake@harmonygames.co/1844276782694400057` | snippet → latest reply | thread inserted earlier in SQL |
| 129 | 258 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3…` | 2025-09-26T15:05:00Z from PERSON_9904_EMAIL: Re: Harmony Games - follow up | new; date = internal_date = Date hdr; snippet = body prefix |
| 130 | 260 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843992534712320061` | Ilse Marrow and Leonard Hayes Thursday Sep 2… | new; no collision; id time = first msg |
| 131 | 262 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-2b67d1aa-c…` | 2025-09-22T19:12:00Z from leonard.hayes@harmonygames.co: Invitation: Ilse Marrow and Leonard Ha… | new; date = internal_date = Date hdr; snippet = body prefix |
| 132 | 264 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1843992534712320063` | Ilse Marrow and Leonard Hayes Thursday Sep 2… | new; no collision; id time = first msg |
| 133 | 266 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-c82c189b-c33c-a6e0-…` | 2025-09-22T19:12:00Z from leonard.hayes@harmonygames.co: Invitation: Ilse Marrow and Leonard Ha… | new; date = internal_date = Date hdr; snippet = body prefix |
| 134 | 268 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1843992534712320064` | Ilse Marrow and Leonard Hayes Thursday Sep 2… | new; no collision; id time = first msg |
| 135 | 270 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-44faeeb8-a4b0…` | 2025-09-22T19:12:00Z from leonard.hayes@harmonygames.co: Invitation: Ilse Marrow and Leonard Ha… | new; date = internal_date = Date hdr; snippet = body prefix |
| 136 | 272 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843718101401600063` | PERSON_5487_NAME and Leonard Hayes Tuesday S… | new; no collision; id time = first msg |
| 137 | 274 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-2d8383e3-2…` | 2025-09-19T18:30:00Z from leonard.hayes@harmonygames.co: Invitation: PERSON_5487_NAME and Leona… | new; date = internal_date = Date hdr; snippet = body prefix |
| 138 | 276 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1843718101401600065` | PERSON_5487_NAME and Leonard Hayes Tuesday S… | new; no collision; id time = first msg |
| 139 | 278 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-010d9a7c-8101-ee76-…` | 2025-09-19T18:30:00Z from leonard.hayes@harmonygames.co: Invitation: PERSON_5487_NAME and Leona… | new; date = internal_date = Date hdr; snippet = body prefix |
| 140 | 280 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1843718101401600066` | PERSON_5487_NAME and Leonard Hayes Tuesday S… | new; no collision; id time = first msg |
| 141 | 282 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-9d6c5aee-50ea…` | 2025-09-19T18:30:00Z from leonard.hayes@harmonygames.co: Invitation: PERSON_5487_NAME and Leona… | new; date = internal_date = Date hdr; snippet = body prefix |
| 142 | 284 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844724105216000067` | Board pre-read review - fundraising Monday O… | new; no collision; id time = first msg |
| 143 | 286 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-297f69c9-a…` | 2025-09-30T21:00:00Z from leonard.hayes@harmonygames.co: Invitation: Board pre-read review - fu… | new; date = internal_date = Date hdr; snippet = body prefix |
| 144 | 289 | gcal.gcal_events | INSERT | `evt_2f86b0d4c9e17a35b64e0d` | frederick.stone: Ilse Marrow and Leonard Hayes 2025-09-25T15:30:00Z–16:15:00Z | new id + ical_uid; no base overlap (reused) |
| 145 | 291 | gcal.gcal_events | INSERT | `evt_b511d4619c6f46ee63959b` | leonard.hayes: Ilse Marrow and Leonard Hayes 2025-09-25T15:30:00Z–16:15:00Z | new id + ical_uid; no base overlap (reused) |
| 146 | 293 | gcal.gcal_events | INSERT | `evt_8bd5e929463b854ec0ad13` | robert: Ilse Marrow and Leonard Hayes 2025-09-25T15:30:00Z–16:15:00Z | new id + ical_uid; no base overlap (reused) |
| 147 | 295 | gcal.gcal_events | INSERT | `evt_ca908a712455521f1f8b43` | arthur.blake: Ilse Marrow and Leonard Hayes 2025-09-25T15:30:00Z–16:15:00Z | new id + ical_uid; no base overlap (reused) |
| 148 | 297 | gcal.gcal_events | INSERT | `evt_7d3e19b04a6c25f8e1b9a0` | frederick.stone: PERSON_5487_NAME and Leonard Hayes 2025-09-23T16:00:00Z–16:45:00Z | new id + ical_uid; no base overlap (reused) |
| 149 | 299 | gcal.gcal_events | INSERT | `evt_99df25b554cac93e2926fd` | leonard.hayes: PERSON_5487_NAME and Leonard Hayes 2025-09-23T16:00:00Z–16:45:00Z | new id + ical_uid; no base overlap (reused) |
| 150 | 301 | gcal.gcal_events | INSERT | `evt_671dce00bcb85abb3e355e` | robert: PERSON_5487_NAME and Leonard Hayes 2025-09-23T16:00:00Z–16:45:00Z | new id + ical_uid; no base overlap (reused) |
| 151 | 303 | gcal.gcal_events | INSERT | `evt_d65aa89778c3ebfa5d97b2` | arthur.blake: PERSON_5487_NAME and Leonard Hayes 2025-09-23T16:00:00Z–16:45:00Z | new id + ical_uid; no base overlap (reused) |
| 152 | 305 | gcal.gcal_events | INSERT | `evt_9c41e7a2d05b38f6e1a7c4` | frederick.stone: Board pre-read review - fundraisin… 2025-10-06T16:00:00Z–16:45:00Z | new id + ical_uid; no base overlap (reused) |
| 153 | 307 | gcal.gcal_events | INSERT | `evt_75d8a0687ea57b663a40b0` | leonard.hayes: Board pre-read review - fundraisin… 2025-10-06T16:00:00Z–16:45:00Z | new id + ical_uid; no base overlap (reused) |
| 154 | 310 | linear.linear_issues | INSERT | `ZOM-567` | team_ZOM, Arthur, Todo, created 2025-09-30T17:10:00Z | new; follows ZOM-566 **(changed in this version)** |
| 155 | 312 | linear.linear_comments | INSERT | `lc_94eb35d962cfbdd31e1bd496` | ZOM-567, 2025-09-30T17:25:00Z | new; issue in SQL **(changed in this version)** |
| 156 | 314 | linear.linear_comments | INSERT | `lc_b549f3057640a5eb08f7581e` | ZOM-567, 2025-09-30T18:40:00Z | new; issue in SQL **(changed in this version)** |
| 157 | 317 | contacts.contacts | INSERT | `e3a91c07d5b48f26a0c7e314` | Edith Vane, PERSON_9903_EMAIL | new id; email not in base contacts |
| 158 | 319 | contacts.contacts | INSERT | `b72f0d6e19c3a84e5d21f9a0` | Ilse Marrow, PERSON_9904_EMAIL | new id; email not in base contacts |
| 159 | 321 | contacts.contacts | INSERT | `5d0e8b31f7a29c64e1b0d3a8` | Karthic R, PERSON_3242_EMAIL | new id; email not in base contacts |
| 160 | 323 | contacts.contacts | INSERT | `a4c2e9f07b31d85e6c0f1b29` | Ryo Ishikawa, PERSON_5221_EMAIL | new id; email not in base contacts (170); matches 石川 遼 in base Dentsu threads **(new in this version)** |

## 6. Check A: records, references and IDs

- **References resolve.** All Drive parents, the Trello board, list, member and existing card (UPDATE targets), the Linear team and user, both Slack channels, all three Slack authors and the Slack thread parent (UPDATE target) exist in the base (§4). The new Slack message's author `EMPLOYEE_0038_SLACK_ID` is Leonard Hayes (users.json) and a member of #bridge-pitch `C096HFA5Z8W` (channels.json). Children reference rows inserted earlier in the script. Each UPDATE uses a primary-key predicate that hits exactly one row.
- **No collisions.** New Slack id `800870c56bda852a57dfa06cb4fd63e6`: 0 matches in 610,468 base messages (complete lookup, 0 errors); its ts appears in no base message file. New contact id `a4c2e9f07b31d85e6c0f1b29` and email PERSON_5221_EMAIL: absent from the 170 base contacts. All other keys rechecked as in §4. No duplicate keys within the SQL (ids per table, Slack ts per channel, contact ids and emails).
- **ID contracts.** Gmail `history_id` NULL on every thread; no Drive row sets `content_path`; the new Slack id is 32-hex like the base.
- **Readable Drive files.** The 3 Google Docs have non-empty `body_text` (432 / 3,018 / 285 chars).
- **One account per person.** The new contact Ryo Ishikawa uses PERSON_5221_EMAIL, the address base Dentsu threads give for 石川 遼 (Ishikawa Ryo, "Ryo-san"); no base contact exists for that address or name, so this adds one contact for an existing external person, not a second account. The new Slack message uses Leonard's existing account.

## 7. Check B: SQL structure and supported schema rules

- One BEGIN/COMMIT block. Every INSERT names its columns and has one VALUES row of matching length (lint and independent parse, 160 rows). The 11 UPDATEs use primary-key predicates.
- No `_fts` column is set. Linear dates use `YYYY-MM-DDTHH:MM:SSZ`; `state_history_json = '[]'` is present on ZOM-567. Every `*_json` value parses; the new Slack row uses `metadata_json '{}'` and list-shaped reactions/files/attachments.
- Doc style runs for the rewritten template: 10 runs, contiguous 0–3,018 = `len(body_text)`; the HEADING_2 runs cover exactly "Who goes in the table", "Status, as of end of day Tue Sep 30 (Pacific)", "Money" and "Build access" (each ending in a newline).
- The new contact row fills `contact_id`, `first_name`, `last_name` (NOT NULL) and nullable fields only.
- **Provisional snapshot comparison:** MATCH for every column used, except four columns the snapshot doesn't cover (unchanged): `gslides.slides_pages.notes` (all NULL), `gslides.slides_page_elements.table_json` (all NULL) and `.ordinal`, `linear.linear_comments.sequence`. Advisory only (Advisory 1).

## 8. Check C: dates, relationships and consistency

- **Clock.** Every event timestamp is at or before 2025-10-01T07:00Z (latest event: Leonard's email 2025-09-30T21:05Z). Only plan fields are later (Oct 6 review events, Trello due 2025-10-14T16:00Z). The new Slack message is dated 2025-09-09T18:20Z; ts `1757442000.492583` = 2025-09-09T18:20:00Z.
- **Initial Capital Slack (new, line 113).** "pinged Initial Capital on LinkedIn about the bridge, they wrote back that they won't lead but might write a small check". Agrees with investor-list row 17 (Initial Capital), Latest Status "They won't lead - would potentially write a small check", a column the template dates to this round ("as of 09/11"); the message predates that. No 2025 base Slack or Gmail mentions Initial Capital, so nothing contradicts the outreach or the answer.
- **Mattel Slack (changed, line 119).** "since the kickoff that's only been an RFP conversation, we haven't pitched them the bridge". Agrees with the base: after Sep 3 the only Mattel mail is the M3 RFP thread (`00015226`: Tim Steudler 09-04, Leonard 09-05, Leonard's decline 09-26 22:28Z, Tim 09-27). Leonard's Aug 26 fundraising-deck email (`00015114`) predates the kickoff, so the earlier "only ever" overstatement (previous Advisory 1) is gone. The Slack post (22:50Z) follows the decline.
- **T-Accelerate Linear comment (changed, line 312).** "TestFlight and Play internal track both added Sep 22". Agrees with Leonard's 2025-09-22 17:40Z email to Karthic (`00015209`): "We already sent a TestFlight invite to your email … For Android, you should be able to download it here: play.google.com/apps/internaltest/…", after Karthic's 09-17 "we're unable to access the game" and Leonard's request for Google/Apple account emails.
- **Dentsu Linear comment (changed, line 314).** "3 accounts from Ryo-san, came in Thursday night: TestFlight added Sep 26 … their work addresses aren't Google accounts so Play won't take them". The injected Ryo email (2025-09-26T03:10Z = Thu Sep 25 20:10 PT, "Please add the three of us with these addresses: PERSON_2581_EMAIL PERSON_5584_EMAIL PERSON_5221_EMAIL") is the source; those are the Dentsu work addresses in base thread `00015338`, which never shows them as Google accounts. TestFlight add (Sep 26) follows the email; the comment (09-30 18:40Z) follows both. It answers Leonard's base 09-24 01:52Z offer ("testflight for iOS or Google Play for Android").
- **ZOM-567 description (changed).** "one comment per firm with the date each add landed": both comments carry add dates. Comments follow the issue's creation (17:10Z) and the issue's updated_at equals the last comment (18:40Z).
- **Ilse follow-up edit (changed, lines 232–246).** Body, message snippets and thread snippets agree in all 4 mailboxes. size_estimate dropped by 71 (1152 → 1081), exactly the length of the removed sentence plus its space (old body 252 chars, new 181). No other record refers to a "separate email" with the deck.
- **Template doc and agenda slide (changed).** The added accelerator sentence references the a16z speedrun process, Leonard's bridge threads and #bridge-pitch, all of which exist; nothing in it postdates the doc's modified time (2025-09-26T18:41Z). The agenda now lists slides in deck order (Q3 recap idx 2, ZM3D alpha 3, Engine 4, Team 5, Runway 6, Fundraising 8; the deals slide 7 isn't named, which is not a contradiction).
- **Unchanged records.** Chronology, encodings and base agreement for byte-identical rows were reused from the previous review (§11).
- **Grader-facing text.** None. Every injected text is in a persona's voice; nothing addresses a solver or grader or describes the test.

## 9. Findings

No demonstrated defects. The previous Mattel advisory is resolved by the rewording. Remaining advisory (does not block this stage):

1. **Columns not in the schema snapshot (Check B, provisional, unchanged).** `slides_pages.notes` (all NULL), `slides_page_elements.table_json` (all NULL) and `.ordinal`, and `linear_comments.sequence` appear in neither the snapshot nor the base exports. If a platform table lacks any of them, that INSERT fails and BEGIN/COMMIT rolls back the whole script. No task content depends on them. Smallest fix: drop those four columns and their values, or confirm the script loads on the platform.

## 10. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | All actors, parents and targets resolve. New Slack id and contact id/email don't collide in complete scans. No ID-contract breaks. Drive files readable. New contact maps to an existing external person with no prior contact. |
| B — SQL structure and supported schema rules | PASS | Structure, JSON shapes, required columns, generated columns, Linear formats and doc style runs valid. Four snapshot-uncovered columns are advisory. Not live-certified. |
| C — Dates, relationships and consistency | PASS | All event times before the clock. The new and changed Slack, Linear, Gmail, doc and slide records agree with base Gmail, Slack, the investor list and the other injected records. |

Outside certification scope (disclosed, not gates): live execution and current database compatibility (including the four columns), search ranking, Agent visibility and persona access, task difficulty.

## 11. Stage ownership and reuse

Reused evidence (stage-evidence-v1), from `Evals/task_inputs/reports/0_injection.md` as it stood before this rerun, SHA-256 `02356fc64a28ab314ada8cd90befd5d14986c4e708fca0879371211b8b53eb1b` (injection-static-v2, PASS/COMPLETE, SQL `2e2428bc…fea4ae`):

| Item | Source ledger / check | Dependencies verified unchanged |
|---|---|---|
| Collision results for byte-identical rows (Drive, Docs/Sheets/Slides, slide object ids, Trello, Linear issue/comment ids, Calendar, Gmail ids, first 3 contacts) | previous §4 | universe manifest `da2f4cf0…aac1a`; those ids byte-identical; in-SQL duplicate check rerun on all 160 rows |
| Calendar overlaps and event times | previous §4/§8 | manifest; gcal rows byte-identical |
| Base agreement for unchanged rows (Treo VC, 1AM Gaming, Play Ventures, Hiro, DocuSign, angels, Sciplay, Trello) | previous §8 | manifest; those SQL rows byte-identical |

`/prompt` may reuse these static checks only while all of these hold: SQL SHA-256 `3ba2b413458f437b3bac5c3ebae97ec7009afb6965ef8017341bf5873cca7f87`, universe manifest `da2f4cf0…aac1a`, schema snapshot `31dcb2b4…`, id_contracts `fc4711ef…`, Eval 0 `e034019b…`, clock 2025-10-01T07:00Z. `/prompt` still owns discoverability and persona access. This SQL changed, so the earlier /prompt pass is outdated; run /prompt, /hardness, /oe and /rubric again in that order.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt, then /hardness, /oe and /rubric. Optionally drop the four snapshot-uncovered columns (Advisory 1) first; that is a new SQL version that needs /injection again.

Evidence limits: Static review only. The schema snapshot is unverified and doesn't cover slides_pages.notes, slides_page_elements.table_json/ordinal or linear_comments.sequence. Base facts for byte-identical rows were reused with provenance (§11). No live load, tool-visibility or search-ranking checks.
