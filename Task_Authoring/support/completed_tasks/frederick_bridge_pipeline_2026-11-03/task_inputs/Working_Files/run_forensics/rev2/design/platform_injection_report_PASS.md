# Injection Data-Integrity Review (Eval 0)

Review version: `injection-static-v2`
Evidence contract: `stage-evidence-v1`
Review time: 2026-11-01T20:15Z (actual)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Mode: chat review, attempt 6ae4e299a13034b7eb8305f8 (static, SQL not executed)

## 1. Scope and inputs

| Input | Value |
|---|---|
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` (revision 5, from chat attachment `01_Universe_Inject (4).sql`), 128,778 bytes, SHA-256 `b2bfda86002c267c8bb3a6043acccf557931d1d62bc045a6ba0c32f1a72e6539`. Replaces revision 4 (`0b6812c5…`), so the earlier injection report no longer applies. |
| Assignment (context only) | Frederick Stone, Co-founder; Executive / Corporate Ops / Retrieval / long-horizon (not graded here) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Eval | `Evals/0_Injection_Quality_Eval.md` `e034019b8ec450437509a73dd3bae2d303b57561b0f67fcc1e5d19266f663eff` |
| Shared workflow | WORKFLOW.md `ee4cd8e1…fcd5d` (guide view); scoring.json `c14873e6…89e5bc` |
| Schema snapshot | `references/schema/injection.json` `31dcb2b43feca8e5c7cb67f37973f819c9b9774f12f8b15cb7da89ecd74c5151` (unverified, provisional) |
| ID contracts | `references/schema/id_contracts.json` `fc4711ef07667333c1cf2a417279826f0432539195f7acdfacfa86e9d9ed4682` |
| Lint | `hg_injection_lint.py` `a8226e2a…448b`, version `injection-lint-v1` |
| Roster / ACL | roster.json `3f217451…84575`, acl.md `e9bca2b3…8c9f` (identity checks only) |

Input/authority issues: none. SQL lines 1–4 are comments, read as evidence of intent only. Line 4 ("re-apply this exact SQL before every agent run") is a setup note inside a comment. It isn't text in any injected record and says nothing about tool calls, pass rate or gates.

## 2. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, base manifest, review version | NEW, done (revision 5 saved before review) |
| Run lint; resolve every flag | NEW, done (0 FAIL, 0 CHECK, 0 INFO) |
| Inventory every statement and affected record | NEW, done: 155 statements (BEGIN, 143 INSERT, 10 UPDATE, COMMIT), 153 row operations, ledger §5 |
| Check A | NEW, PASS |
| Check B | NEW, PASS (provisional snapshot advisory) |
| Check C | NEW, PASS (advisories) |
| Report coverage, findings, limits, one verdict | NEW, done |

No evidence was reused from the earlier report: every check was rerun against this SQL version.

## 3. Lint result

`hg_injection_lint.py` on SHA `b2bfda86…6539`, universe synthcut, clock 2025-10-01T07:00Z. Checks run: future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape. Base files loaded: contacts.json, slack/users.json, trello/data.json, gmail/users.json, linear/data.json, confluence_working.json.

Flags: **none** (FAIL 0, CHECK 0, INFO 0). Nothing to resolve. A clean lint was not treated as a pass; checks A–C below were run in full.

## 4. Source coverage

| Check | Source / pointer | Coverage | Result |
|---|---|---|---|
| Drive ids (6 new) + 2 parents | gdrive `data.json` `/drive_files` field `id` | 53,631 records, scan complete | New ids absent; parents `d_175c0d7bc72ed244b944cb` (/drive_files/2060, Fred's root) and `d_63fffeb4fab5233ed5bb73` (/drive_files/9030, Leonard's root) exist |
| Docs / Sheets / Slides ids | gdocs `/docs_documents` document_id (595), gsheets `/sheets_spreadsheets` (356), gslides `/slides_presentations` (132) | complete | no collisions |
| Trello card / idShort / shortLink | trello `/cards` (803) | complete | `68c5a49e…69d0` exists (/cards/801, "Existing Investor Update", idShort 455, comments 0, checkItems 0); `68d8193c…8a2a`, idShort 466, shortLink `Qa5QbkDO` absent |
| Trello actions / checklists / check items | `/actions` (5,252), `/checklists` (54), `/check_items` (161) | complete | no collisions |
| Trello member / board / list | `/members` (42), `/boards` (5), `/lists` (47) | complete | `PERSON_6094_TRELLO_USER_ID` = Leonard Hayes (/members/2); board `640643a3…318e` (/boards/1); list `640643a3…3196` "Doing" (/lists/4) |
| Linear issue / user / team / comments | linear `data.json` `/issues` identifier+id (3,687), `/users` (41), `/teams` (5), `/comments` (0); plus grep of full linear export incl. `root/` | complete | ZOM-567 absent (ZOM-566 is latest, /issues/3643, created 2025-09-30T16:26:02Z); `usr_cc3e90160f490686` = arthur.blake (/users/35); `team_ZOM` (/teams/4); comment ids absent anywhere |
| Contacts ids / emails / names | contacts `/contacts` (170) | complete | 3 new contact_ids absent; no existing contact has PERSON_3242/9901–9904/5487/5282/5221/2581/5584 or SVC_1302 email, or first name Karthic/Anton/Paul/Edith/Ilse |
| Calendar events / ical_uid | gcal `/events` (10,395) | complete | 10 event_ids and 3 ical_uids absent |
| Slack users / channels | slack `users.json` (218), `channels.json` (948) | complete | EMPLOYEE_0016 = Robert, 0025 = Arthur Blake, 0038 = Leonard Hayes; C07C2866011 = #executives, C096HFA5Z8W = #bridge-pitch; all three users are members of both |
| Slack message ids + thread parent | grep of all `slack/messages/*/*.json` | complete | 4 new ids absent; parent `73c2247f…13ac` found only in `C096HFA5Z8W/2025-09.json` (Leonard, ts 1757716998.377299, reply_count 0) |
| Gmail thread ids (29) and message ids (37); identity tokens | streaming pass over all 81,404 `gmail/threads/*.json` | 81,404 files, 0 read errors | 0 thread-id and 0 message-id collisions. PERSON_9901–9904: 0 hits anywhere in Gmail (also 0 in Slack, gcal, contacts, Trello). "Anton Bernstein", "Heydon", "Edith Vane", "Ilse Marrow", "Brightwater": 0 hits |
| Identity of reused external tokens | Gmail threads `frederick@…_1842283406259093714.json` (T-Accelerate), `frederick@…_1843473831194478743.json` + `00015338.json` (Dentsu), `frederick@…_1842278425320449096.json` + `leonard@…_1842278433020808799.json` (Hiro), `00013372.json` (DocuSign) | full threads read | PERSON_3242 = "karthic R", T-Accelerate; PERSON_5221 = 石川 遼 (Ryo), PERSON_5584 = 田端 剛治 (Koji), PERSON_2581 = 小川 浩史, all Dentsu; PERSON_5487 = Leonard's Hiro intro addressee, PERSON_5282 = Hiro Investment Director; SVC_1302 = DocuSign sender ("Completed: Complete with docusign: …") |
| Referenced list | gdrive `/drive_files` name search "Game Investor" | complete | "Game Investor List - Harmony Games 2025.xlsx" exists (/drive_files/31887), so the text reference in Leonard's email and the template resolves (visibility is a /prompt question) |
| Known base issues | `Evals/references/known_base_issues.md`, `guidelines/known_data_issues.md` | read | SQL touches no Snowflake/Confluence data and builds on no listed conflict |

## 5. Operation ledger

All 153 row operations in execution order (statement order = SQL line order; BEGIN at line 5, COMMIT at the end). Every parent is created before its children.

| # | Line | Table | Op | Record / target | Key values | Check result |
|---|---|---|---|---|---|---|
| 1 | 7 | gdrive.drive_files | INSERT | `f_8d2c47a91e05b3f6d7c418` | Board pre-read - fundraising section (document), parent d_63fffeb4fab5233ed5bb73, owner leonard.hayes, created 2025-07-08T18:00:00Z | new id, no collision; parent resolves |
| 2 | 9 | gdrive.drive_files | INSERT | `f_3b9e61c04d7a52e8f1a6c2` | Board pre-read - fundraising section (Oct 14) (document), parent d_63fffeb4fab5233ed5bb73, owner leonard.hayes, created 2025-09-26T18:00:00Z | new id, no collision; parent resolves |
| 3 | 11 | gdrive.drive_files | INSERT | `d_5e8a1c3f9b07d2e64a1b93` | Board - Oct 14 2025 (folder), parent d_175c0d7bc72ed244b944cb, owner frederick.stone, created 2025-09-26T18:20:00Z | new id, no collision; parent resolves |
| 4 | 13 | gdrive.drive_files | INSERT | `f_c61a0e93b7d24f58a2e917` | README - Oct 14 board materials (document), parent d_5e8a1c3f9b07d2e64a1b93, owner leonard.hayes, created 2025-09-26T18:30:00Z | new id, no collision; parent resolves |
| 5 | 15 | gdrive.drive_files | INSERT | `f_a47d0e2c95b18f63e2c0d5` | HG BoD Oct 14 2025 (draft) (presentation), parent d_63fffeb4fab5233ed5bb73, owner leonard.hayes, created 2025-09-27T17:00:00Z | new id, no collision; parent resolves |
| 6 | 17 | gdrive.drive_files | INSERT | `f_6e1d93a0c4b72f85d39a0e` | Bridge angels (spreadsheet), parent d_63fffeb4fab5233ed5bb73, owner leonard.hayes, created 2025-09-19T17:52:00Z | new id, no collision; parent resolves |
| 7 | 20 | gdocs.docs_documents | INSERT | `f_8d2c47a91e05b3f6d7c418` | Board pre-read - fundraising section, body 432 chars, style runs contiguous to 432 | readable; Drive row in SQL |
| 8 | 22 | gdocs.docs_documents | INSERT | `f_3b9e61c04d7a52e8f1a6c2` | Board pre-read - fundraising section (Oct 14), body 1708 chars, style runs contiguous to 1708 | readable; Drive row in SQL |
| 9 | 24 | gdocs.docs_documents | INSERT | `f_c61a0e93b7d24f58a2e917` | README - Oct 14 board materials, body 285 chars, style runs contiguous to 285 | readable; Drive row in SQL |
| 10 | 27 | gsheets.sheets_spreadsheets | INSERT | `f_6e1d93a0c4b72f85d39a0e` | Bridge angels | new; Drive row in SQL |
| 11 | 29 | gsheets.sheets_sheets | INSERT | `f_6e1d93a0c4b72f85d39a0e#0` | tab Angels, 3 grid rows | parent in SQL |
| 12 | 32 | gslides.slides_presentations | INSERT | `f_a47d0e2c95b18f63e2c0d5` | HG BoD Oct 14 2025 (draft) | new; Drive row in SQL |
| 13 | 34 | gslides.slides_pages | INSERT | `slide_b4c21ca913ab` | index 0 | unique in new deck |
| 14 | 36 | gslides.slides_page_elements | INSERT | `el_6825f973029b` | on slide_b4c21ca913ab: Harmony Games Board Meeting | unique in new deck |
| 15 | 38 | gslides.slides_page_elements | INSERT | `el_cffa02683868` | on slide_b4c21ca913ab: October 14, 2025 (draft) | unique in new deck |
| 16 | 40 | gslides.slides_pages | INSERT | `slide_256dc0474f7c` | index 1 | unique in new deck |
| 17 | 42 | gslides.slides_page_elements | INSERT | `el_72151261faca` | on slide_256dc0474f7c: Agenda | unique in new deck |
| 18 | 44 | gslides.slides_page_elements | INSERT | `el_ca7b40076cd7` | on slide_256dc0474f7c: Q3 recap / Zombie Match 3D alpha / Engin | unique in new deck |
| 19 | 46 | gslides.slides_pages | INSERT | `slide_fd6dbd079420` | index 2 | unique in new deck |
| 20 | 48 | gslides.slides_page_elements | INSERT | `el_90fbf6fd9c1b` | on slide_fd6dbd079420: Q3 recap | unique in new deck |
| 21 | 50 | gslides.slides_page_elements | INSERT | `el_ef5243814e8f` | on slide_fd6dbd079420: Domino Delights: publisher search
Zombie | unique in new deck |
| 22 | 52 | gslides.slides_pages | INSERT | `slide_bb11abfc5fad` | index 3 | unique in new deck |
| 23 | 54 | gslides.slides_page_elements | INSERT | `el_69587907b898` | on slide_bb11abfc5fad: Zombie Match 3D | unique in new deck |
| 24 | 56 | gslides.slides_page_elements | INSERT | `el_6ca8bffe4445` | on slide_bb11abfc5fad: Alpha metrics (Robert to fill) | unique in new deck |
| 25 | 58 | gslides.slides_pages | INSERT | `slide_cb3f0884f833` | index 4 | unique in new deck |
| 26 | 60 | gslides.slides_page_elements | INSERT | `el_0c72e8ba6af7` | on slide_cb3f0884f833: Engine | unique in new deck |
| 27 | 62 | gslides.slides_page_elements | INSERT | `el_1e212bf4628e` | on slide_cb3f0884f833: What shipped in Q3 (Arthur to fill) | unique in new deck |
| 28 | 64 | gslides.slides_pages | INSERT | `slide_a56932e4c738` | index 5 | unique in new deck |
| 29 | 66 | gslides.slides_page_elements | INSERT | `el_5da52b8348b0` | on slide_a56932e4c738: Team | unique in new deck |
| 30 | 68 | gslides.slides_page_elements | INSERT | `el_4f7f04b6e984` | on slide_a56932e4c738: Headcount and contractors (Leonard to fi | unique in new deck |
| 31 | 70 | gslides.slides_pages | INSERT | `slide_c9c7eed73bb9` | index 6 | unique in new deck |
| 32 | 72 | gslides.slides_page_elements | INSERT | `el_b45885b83bf9` | on slide_c9c7eed73bb9: Runway | unique in new deck |
| 33 | 74 | gslides.slides_page_elements | INSERT | `el_ed13f88ca45b` | on slide_c9c7eed73bb9: Cash and burn (Leonard to fill) | unique in new deck |
| 34 | 76 | gslides.slides_pages | INSERT | `slide_329b5dfcb888` | index 7 | unique in new deck |
| 35 | 78 | gslides.slides_page_elements | INSERT | `el_09521ac10bd5` | on slide_329b5dfcb888: Options | unique in new deck |
| 36 | 80 | gslides.slides_page_elements | INSERT | `el_d65f0ea436c8` | on slide_329b5dfcb888: Bridge / co-dev / engine deals | unique in new deck |
| 37 | 82 | gslides.slides_pages | INSERT | `slide_68eecd4f5f2a` | index 8 + notes | unique in new deck |
| 38 | 84 | gslides.slides_page_elements | INSERT | `el_b87125dbf11e` | on slide_68eecd4f5f2a: Fundraising | unique in new deck |
| 39 | 86 | gslides.slides_page_elements | INSERT | `el_6548686fe965` | on slide_68eecd4f5f2a: Bridge round, pipeline as of Sep 30
Firm | unique in new deck |
| 40 | 88 | gslides.slides_pages | INSERT | `slide_98d06d32c8d6` | index 9 | unique in new deck |
| 41 | 90 | gslides.slides_page_elements | INSERT | `el_154065e277bc` | on slide_98d06d32c8d6: Asks for the board | unique in new deck |
| 42 | 92 | gslides.slides_page_elements | INSERT | `el_ee461e258b77` | on slide_98d06d32c8d6: Intros, especially games funds and strat | unique in new deck |
| 43 | 94 | gslides.slides_pages | INSERT | `slide_fcf2cb38bf31` | index 10 | unique in new deck |
| 44 | 96 | gslides.slides_page_elements | INSERT | `el_8ee884c1e93b` | on slide_fcf2cb38bf31: Appendix | unique in new deck |
| 45 | 98 | gslides.slides_page_elements | INSERT | `el_34bc96464df6` | on slide_fcf2cb38bf31: Investor FAQ (link) | unique in new deck |
| 46 | 100 | gslides.slides_pages | INSERT | `slide_5c7db3c42932` | index 11 | unique in new deck |
| 47 | 102 | gslides.slides_page_elements | INSERT | `el_ef3226341cb0` | on slide_5c7db3c42932: Thank you | unique in new deck |
| 48 | 105 | slack.slack_messages | INSERT | `4921f321db5d08f936aac24a6a1d2af8` | C07C2866011 EMPLOYEE_0038_SLACK_ID ts 1758303600.418207 = 2025-09-19T17:40:00.000000Z | new id; author is channel member; ts = created_at |
| 49 | 107 | slack.slack_messages | INSERT | `7fef94264090696760180223fc8265e7` | C07C2866011 EMPLOYEE_0025_SLACK_ID ts 1759168800.117903 = 2025-09-29T18:00:00.000000Z | new id; author is channel member; ts = created_at |
| 50 | 109 | slack.slack_messages | INSERT | `3f2d8f04b29a78808033543c740bb669` | C096HFA5Z8W EMPLOYEE_0016_SLACK_ID ts 1759161600.226431 = 2025-09-29T16:00:00.000000Z | new id; author is channel member; ts = created_at |
| 51 | 111 | slack.slack_messages | INSERT | `cf10d4f7f88143dc7ab976df27513790` | C096HFA5Z8W EMPLOYEE_0016_SLACK_ID ts 1759184040.552871 = 2025-09-29T22:14:00.000000Z, reply to 73c2247f… | new id; author is channel member; ts = created_at |
| 52 | 113 | slack.slack_messages | UPDATE | `73c2247f4a31f32d10b3068ecd1d13ac` | reply_count 0→1, reply_users_count 1, latest_reply 1759184040.552871, thread_ts_legacy = own ts | target exists (C096HFA5Z8W/2025-09.json), base reply_count 0 |
| 53 | 115 | trello.trello_actions | INSERT | `68c64270d660c977c4696986` | commentCard 2025-09-14T04:20:00Z on card 68c5a49e…, by Leonard | new; id hex time = date |
| 54 | 117 | trello.trello_cards | UPDATE | `68c5a49e8491a9d7faf869d0` | badges.comments 0→1 (rest identical), dateLastActivity 2025-09-13T17:06:40Z→2025-09-14T04:20:00Z | target /cards/801 exists |
| 55 | 118 | trello.trello_cards | INSERT | `68d8193cf451863621c88a2a` | Board Deck - Oct 14, list Doing, idShort 466, due 2025-10-14T16:00:00Z (plan), badges checkItems 4 / comments 1 | new id/idShort/shortLink, no collision |
| 56 | 120 | trello.trello_actions | INSERT | `68d8193c164e823ac3ae735d` | createCard 2025-09-27T17:05:00Z on card 68d8193c…, by Leonard | new; id hex time = date |
| 57 | 122 | trello.trello_checklists | INSERT | `68d81ae0bac8fd292e6606f8` | Sections | new; card in SQL |
| 58 | 124 | trello.trello_check_items | INSERT | `68d81ae032fe8d64dbd262c7` | Fundraising - Fred | new; checklist in SQL |
| 59 | 126 | trello.trello_check_items | INSERT | `68d81ae087c12c3d08c79ff8` | Product - Robert | new; checklist in SQL |
| 60 | 128 | trello.trello_check_items | INSERT | `68d81ae05ac90637e942026c` | Engine - Arthur | new; checklist in SQL |
| 61 | 130 | trello.trello_check_items | INSERT | `68d81ae07d46d8fe71f4ba98` | Runway and options - Leonard | new; checklist in SQL |
| 62 | 132 | trello.trello_actions | INSERT | `68d81ae0459a87b4efb4b1e3` | addChecklistToCard 2025-09-27T17:12:00Z on card 68d8193c…, by Leonard | new; id hex time = date |
| 63 | 134 | trello.trello_actions | INSERT | `68d81f30a6c94e2b7d05e1f4` | commentCard 2025-09-27T17:30:24Z on card 68d8193c…, by Leonard | new; id hex time = date |
| 64 | 137 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844623441920000059` | Fred - for the 14th could you just email the  | new; no collision; id time = first message |
| 65 | 139 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAdKLID2b1N4D6wzcwD-r…` | 2025-09-29T18:20:00Z from robert@harmonygames.co: board pipeline | new; date = internal_date = Date header |
| 66 | 141 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844623441920000061` | Fred - for the 14th could you just email the  | new; no collision; id time = first message |
| 67 | 143 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAdKLID2b1N4D6wzcwD-r…` | 2025-09-29T18:20:00Z from robert@harmonygames.co: board pipeline | new; date = internal_date = Date header |
| 68 | 145 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844623441920000062` | Fred - for the 14th could you just email the  | new; no collision; id time = first message |
| 69 | 147 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAdKLID2b1N4D6wzcwD-r…` | 2025-09-29T18:20:00Z from robert@harmonygames.co: board pipeline | new; date = internal_date = Date header |
| 70 | 149 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844724419788800011` | Fred, I'm flying to LA tomorrow morning for t | new; no collision; id time = first message |
| 71 | 151 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAxDeR9CSc9iEY-zACLQa…` | 2025-09-30T21:05:00Z from leonard.hayes@harmonygames.co: Oct 14 board pre-read - fundraising section | new; date = internal_date = Date header |
| 72 | 153 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844724419788800013` | Fred, I'm flying to LA tomorrow morning for t | new; no collision; id time = first message |
| 73 | 155 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAxDeR9CSc9iEY-zACLQa…` | 2025-09-30T21:05:00Z from leonard.hayes@harmonygames.co: Oct 14 board pre-read - fundraising section | new; date = internal_date = Date header |
| 74 | 157 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844724419788800014` | Fred, I'm flying to LA tomorrow morning for t | new; no collision; id time = first message |
| 75 | 159 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAxDeR9CSc9iEY-zACLQa…` | 2025-09-30T21:05:00Z from leonard.hayes@harmonygames.co: Oct 14 board pre-read - fundraising section | new; date = internal_date = Date header |
| 76 | 161 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844724419788800015` | Fred, I'm flying to LA tomorrow morning for t | new; no collision; id time = first message |
| 77 | 163 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAxDeR9CSc9iEY-zACLQa…` | 2025-09-30T21:05:00Z from leonard.hayes@harmonygames.co: Oct 14 board pre-read - fundraising section | new; date = internal_date = Date header |
| 78 | 165 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844162278195200023` | Leonard, Had another look at my numbers. I ca | new; no collision; id time = first message |
| 79 | 167 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CACJhvEE55qdWXuKC3BWl…` | 2025-09-24T16:10:00Z from PERSON_9901_EMAIL: SAFE amount | new; date = internal_date = Date header |
| 80 | 169 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844162278195200025` | Leonard, Had another look at my numbers. I ca | new; no collision; id time = first message |
| 81 | 171 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CACJhvEE55qdWXuKC3BWl…` | 2025-09-24T16:10:00Z from PERSON_9901_EMAIL: SAFE amount | new; date = internal_date = Date header |
| 82 | 173 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844354293432320031` | Hello Frederick Stone, All signers completed  | new; no collision; id time = first message |
| 83 | 175 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAiKDPIoVSAFUBccUSRRB…` | 2025-09-26T19:02:00Z from SVC_1302_EMAIL: Completed: Complete with docusign: Harmony Ga | new; date = internal_date = Date header |
| 84 | 177 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844610859008000037` | Hi Paul, Gentle nudge on the SAFE in DocuSign | new; no collision; id time = first message |
| 85 | 179 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAP6Gn2LV490e3El5rBDC…` | 2025-09-29T15:00:00Z from leonard.hayes@harmonygames.co: SAFE in DocuSign | new; date = internal_date = Date header |
| 86 | 181 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844610859008000039` | Hi Paul, Gentle nudge on the SAFE in DocuSign | new; no collision; id time = first message |
| 87 | 183 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAP6Gn2LV490e3El5rBDC…` | 2025-09-29T15:00:00Z from leonard.hayes@harmonygames.co: SAFE in DocuSign | new; date = internal_date = Date header |
| 88 | 185 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844318935449600041` | Leonard, Thanks again for the session on Tues | new; no collision; id time = first message |
| 89 | 187 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_l…` | 2025-09-26T09:40:00Z from PERSON_9903_EMAIL: Harmony Games bridge | new; date = internal_date = Date header |
| 90 | 189 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844318935449600043` | Leonard, Thanks again for the session on Tues | new; no collision; id time = first message |
| 91 | 191 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_l…` | 2025-09-26T09:40:00Z from PERSON_9903_EMAIL: Harmony Games bridge | new; date = internal_date = Date header |
| 92 | 193 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844294398771200045` | Leonard-san, Thank you for the offer. Please  | new; no collision; id time = first message |
| 93 | 195 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4…` | 2025-09-26T03:10:00Z from PERSON_5221_EMAIL: Zombie Match 3D access | new; date = internal_date = Date header |
| 94 | 197 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844294398771200047` | Leonard-san, Thank you for the offer. Please  | new; no collision; id time = first message |
| 95 | 199 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4…` | 2025-09-26T03:10:00Z from PERSON_5221_EMAIL: Zombie Match 3D access | new; date = internal_date = Date header |
| 96 | 201 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844294398771200048` | Leonard-san, Thank you for the offer. Please  | new; no collision; id time = first message |
| 97 | 203 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4…` | 2025-09-26T03:10:00Z from PERSON_5221_EMAIL: Zombie Match 3D access | new; date = internal_date = Date header |
| 98 | 205 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844294398771200049` | Leonard-san, Thank you for the offer. Please  | new; no collision; id time = first message |
| 99 | 207 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4…` | 2025-09-26T03:10:00Z from PERSON_5221_EMAIL: Zombie Match 3D access | new; date = internal_date = Date header |
| 100 | 209 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1844294398771200045` | snippet → latest reply | thread inserted earlier in SQL |
| 101 | 210 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CA0tK15jPm2APp9fC951n…` | 2025-09-26T17:20:00Z from leonard.hayes@harmonygames.co: Re: Zombie Match 3D access | new; date = internal_date = Date header |
| 102 | 212 | gmail.gmail_threads | UPDATE | `leonard.hayes@harmonygames.co/1844294398771200047` | snippet → latest reply | thread inserted earlier in SQL |
| 103 | 213 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CA0tK15jPm2APp9fC951n…` | 2025-09-26T17:20:00Z from leonard.hayes@harmonygames.co: Re: Zombie Match 3D access | new; date = internal_date = Date header |
| 104 | 215 | gmail.gmail_threads | UPDATE | `robert@harmonygames.co/1844294398771200048` | snippet → latest reply | thread inserted earlier in SQL |
| 105 | 216 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CA0tK15jPm2APp9fC951n…` | 2025-09-26T17:20:00Z from leonard.hayes@harmonygames.co: Re: Zombie Match 3D access | new; date = internal_date = Date header |
| 106 | 218 | gmail.gmail_threads | UPDATE | `arthur.blake@harmonygames.co/1844294398771200049` | snippet → latest reply | thread inserted earlier in SQL |
| 107 | 219 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CA0tK15jPm2APp9fC951n…` | 2025-09-26T17:20:00Z from leonard.hayes@harmonygames.co: Re: Zombie Match 3D access | new; date = internal_date = Date header |
| 108 | 221 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844276782694400053` | Hi Ilse, Thanks for the time this morning. I' | new; no collision; id time = first message |
| 109 | 223 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq…` | 2025-09-25T22:30:00Z from leonard.hayes@harmonygames.co: Harmony Games - follow up | new; date = internal_date = Date header |
| 110 | 225 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844276782694400055` | Hi Ilse, Thanks for the time this morning. I' | new; no collision; id time = first message |
| 111 | 227 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq…` | 2025-09-25T22:30:00Z from leonard.hayes@harmonygames.co: Harmony Games - follow up | new; date = internal_date = Date header |
| 112 | 229 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844276782694400056` | Hi Ilse, Thanks for the time this morning. I' | new; no collision; id time = first message |
| 113 | 231 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq…` | 2025-09-25T22:30:00Z from leonard.hayes@harmonygames.co: Harmony Games - follow up | new; date = internal_date = Date header |
| 114 | 233 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844276782694400057` | Hi Ilse, Thanks for the time this morning. I' | new; no collision; id time = first message |
| 115 | 235 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq…` | 2025-09-25T22:30:00Z from leonard.hayes@harmonygames.co: Harmony Games - follow up | new; date = internal_date = Date header |
| 116 | 237 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1844276782694400053` | snippet → latest reply | thread inserted earlier in SQL |
| 117 | 238 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b…` | 2025-09-26T15:05:00Z from PERSON_9904_EMAIL: Re: Harmony Games - follow up | new; date = internal_date = Date header |
| 118 | 240 | gmail.gmail_threads | UPDATE | `leonard.hayes@harmonygames.co/1844276782694400055` | snippet → latest reply | thread inserted earlier in SQL |
| 119 | 241 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b…` | 2025-09-26T15:05:00Z from PERSON_9904_EMAIL: Re: Harmony Games - follow up | new; date = internal_date = Date header |
| 120 | 243 | gmail.gmail_threads | UPDATE | `robert@harmonygames.co/1844276782694400056` | snippet → latest reply | thread inserted earlier in SQL |
| 121 | 244 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b…` | 2025-09-26T15:05:00Z from PERSON_9904_EMAIL: Re: Harmony Games - follow up | new; date = internal_date = Date header |
| 122 | 246 | gmail.gmail_threads | UPDATE | `arthur.blake@harmonygames.co/1844276782694400057` | snippet → latest reply | thread inserted earlier in SQL |
| 123 | 247 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b…` | 2025-09-26T15:05:00Z from PERSON_9904_EMAIL: Re: Harmony Games - follow up | new; date = internal_date = Date header |
| 124 | 249 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843992534712320061` | Ilse Marrow and Leonard Hayes Thursday Sep 25 | new; no collision; id time = first message |
| 125 | 251 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-2b67d1aa-cbd…` | 2025-09-22T19:12:00Z from leonard.hayes@harmonygames.co: Invitation: Ilse Marrow and Leonard Hayes @ T | new; date = internal_date = Date header |
| 126 | 253 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1843992534712320063` | Ilse Marrow and Leonard Hayes Thursday Sep 25 | new; no collision; id time = first message |
| 127 | 255 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-c82c189b-c33…` | 2025-09-22T19:12:00Z from leonard.hayes@harmonygames.co: Invitation: Ilse Marrow and Leonard Hayes @ T | new; date = internal_date = Date header |
| 128 | 257 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1843992534712320064` | Ilse Marrow and Leonard Hayes Thursday Sep 25 | new; no collision; id time = first message |
| 129 | 259 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-44faeeb8-a4b…` | 2025-09-22T19:12:00Z from leonard.hayes@harmonygames.co: Invitation: Ilse Marrow and Leonard Hayes @ T | new; date = internal_date = Date header |
| 130 | 261 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843718101401600063` | PERSON_5487_NAME and Leonard Hayes Tuesday Se | new; no collision; id time = first message |
| 131 | 263 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-2d8383e3-21d…` | 2025-09-19T18:30:00Z from leonard.hayes@harmonygames.co: Invitation: PERSON_5487_NAME and Leonard Haye | new; date = internal_date = Date header |
| 132 | 265 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1843718101401600065` | PERSON_5487_NAME and Leonard Hayes Tuesday Se | new; no collision; id time = first message |
| 133 | 267 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-010d9a7c-810…` | 2025-09-19T18:30:00Z from leonard.hayes@harmonygames.co: Invitation: PERSON_5487_NAME and Leonard Haye | new; date = internal_date = Date header |
| 134 | 269 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1843718101401600066` | PERSON_5487_NAME and Leonard Hayes Tuesday Se | new; no collision; id time = first message |
| 135 | 271 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-9d6c5aee-50e…` | 2025-09-19T18:30:00Z from leonard.hayes@harmonygames.co: Invitation: PERSON_5487_NAME and Leonard Haye | new; date = internal_date = Date header |
| 136 | 273 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844724105216000067` | Board pre-read review - fundraising Monday Oc | new; no collision; id time = first message |
| 137 | 275 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-297f69c9-ad6…` | 2025-09-30T21:00:00Z from leonard.hayes@harmonygames.co: Invitation: Board pre-read review - fundraisi | new; date = internal_date = Date header |
| 138 | 278 | gcal.gcal_events | INSERT | `evt_2f86b0d4c9e17a35b64e0d` | frederick.stone: Ilse Marrow and Leonard Hayes 2025-09-25T16:00:00Z–16:45Z | new id; ical_uid shared across copies |
| 139 | 280 | gcal.gcal_events | INSERT | `evt_b511d4619c6f46ee63959b` | leonard.hayes: Ilse Marrow and Leonard Hayes 2025-09-25T16:00:00Z–16:45Z | new id; ical_uid shared across copies |
| 140 | 282 | gcal.gcal_events | INSERT | `evt_8bd5e929463b854ec0ad13` | robert: Ilse Marrow and Leonard Hayes 2025-09-25T16:00:00Z–16:45Z | new id; ical_uid shared across copies |
| 141 | 284 | gcal.gcal_events | INSERT | `evt_ca908a712455521f1f8b43` | arthur.blake: Ilse Marrow and Leonard Hayes 2025-09-25T16:00:00Z–16:45Z | new id; ical_uid shared across copies |
| 142 | 286 | gcal.gcal_events | INSERT | `evt_7d3e19b04a6c25f8e1b9a0` | frederick.stone: PERSON_5487_NAME and Leonard Hayes 2025-09-23T16:00:00Z–16:45Z | new id; ical_uid shared across copies |
| 143 | 288 | gcal.gcal_events | INSERT | `evt_99df25b554cac93e2926fd` | leonard.hayes: PERSON_5487_NAME and Leonard Hayes 2025-09-23T16:00:00Z–16:45Z | new id; ical_uid shared across copies |
| 144 | 290 | gcal.gcal_events | INSERT | `evt_671dce00bcb85abb3e355e` | robert: PERSON_5487_NAME and Leonard Hayes 2025-09-23T16:00:00Z–16:45Z | new id; ical_uid shared across copies |
| 145 | 292 | gcal.gcal_events | INSERT | `evt_d65aa89778c3ebfa5d97b2` | arthur.blake: PERSON_5487_NAME and Leonard Hayes 2025-09-23T16:00:00Z–16:45Z | new id; ical_uid shared across copies |
| 146 | 294 | gcal.gcal_events | INSERT | `evt_9c41e7a2d05b38f6e1a7c4` | frederick.stone: Board pre-read review - fundraising 2025-10-06T16:00:00Z–16:45Z | new id; ical_uid shared across copies |
| 147 | 296 | gcal.gcal_events | INSERT | `evt_75d8a0687ea57b663a40b0` | leonard.hayes: Board pre-read review - fundraising 2025-10-06T16:00:00Z–16:45Z | new id; ical_uid shared across copies |
| 148 | 299 | linear.linear_issues | INSERT | `ZOM-567` | team_ZOM, assignee/creator Arthur, Todo, created 2025-09-30T17:10:00Z, updated 2025-09-30T18:40:00Z | new; follows ZOM-566 (09-30 16:26Z) |
| 149 | 301 | linear.linear_comments | INSERT | `lc_94eb35d962cfbdd31e1bd496` | ZOM-567, Arthur, 2025-09-30T17:25:00Z | new; issue in SQL |
| 150 | 303 | linear.linear_comments | INSERT | `lc_b549f3057640a5eb08f7581e` | ZOM-567, Arthur, 2025-09-30T18:40:00Z | new; issue in SQL |
| 151 | 306 | contacts.contacts | INSERT | `e3a91c07d5b48f26a0c7e314` | Edith Vane, Partner, Hiro Capital, PERSON_9903_EMAIL | new id; email not in base contacts |
| 152 | 308 | contacts.contacts | INSERT | `b72f0d6e19c3a84e5d21f9a0` | Ilse Marrow, Principal, Brightwater Games Fund, PERSON_9904_EMAIL | new id; email not in base contacts |
| 153 | 310 | contacts.contacts | INSERT | `5d0e8b31f7a29c64e1b0d3a8` | Karthic R, T-Accelerate Capital (PXLite fund), PERSON_3242_EMAIL | new id; email not in base contacts |
## 6. Check A: records, references and IDs

- **References resolve.** All Drive parents, the Trello board/list/member, the existing Trello card (UPDATE target), the Linear team and user, both Slack channels, all three Slack authors and the Slack thread parent (UPDATE target) exist in the base (§4). Children inserted by the SQL (docs/sheets/slides rows, slide pages and elements, checklist and check items, Linear comments, Gmail messages and thread-snippet UPDATEs) all reference rows inserted earlier in the same script.
- **No collisions.** All new keys were checked against complete collections: Drive/Docs/Sheets/Slides ids, Trello card id/idShort/shortLink/actions/checklists/check items, Linear identifier/number/comment ids, contact ids, gcal event ids and ical_uids, Slack message ids and Gmail thread and message ids (all 81,404 thread files). Within the SQL there are no duplicates. The 10 calendar copies share 3 ical_uids by design, matching the base pattern (e.g. `b7ccec27…@hg4` on Fred's and Leonard's copies). Mailbox copies of one email share a Message-ID under different per-user ids, as in the base.
- **ID contracts.** Gmail `history_id` is NULL on every thread (allowed). No Drive row sets `content_path`, so the path contract doesn't apply. Formats match the base: `f_`/`d_` + 22 hex for Drive; 24-hex Trello ids whose first 8 hex digits encode the action time exactly (e.g. `68d81f30` = 2025-09-27T17:30:24Z); `user/<thread>` Gmail ids whose thread number encodes the first message's time; 32-hex Slack ids.
- **Readable Drive files.** The 3 Google Docs have docs_documents rows with non-empty `body_text` (432 / 1,708 / 285 chars). The spreadsheet has a sheets row and a grid. The presentation has 12 pages and 23 elements. The folder holds no content.
- **One account per person.** Internal actors use their existing accounts (Leonard, Robert, Arthur, Fred). Reused external tokens map to the same people as in the base (§4). The new tokens PERSON_9901 (Anton Bernstein), 9902 (Paul Heydon), 9903 (Edith Vane, Hiro Capital partner) and 9904 (Ilse Marrow, Brightwater) appear nowhere in the base, so no existing person gets a second identity. Karthic's new contact uses his existing address PERSON_3242, and no other contact holds it. Edith is a new person at an existing firm, not an alias of a base Hiro contact: the Sep 23 invite lists her alongside PERSON_5487.

## 7. Check B: SQL structure and supported schema rules

- Structure: one BEGIN/COMMIT block; every INSERT names its columns and gives one VALUES row of matching length (lint parsed all 153 rows with no INFO). The UPDATEs use primary-key predicates, and each hits exactly one row (base or inserted earlier).
- Generated columns (`text_fts`, `body_text_fts`) are not set. Linear text dates use `YYYY-MM-DDTHH:MM:SSZ`. `state_history_json = '[]'` is present on the new issue. Every NOT NULL column without a default is supplied (lint + independent check against the snapshot's required columns). The JSON columns parse with the base shapes (Slack `metadata_json '{}'`; lists for `*_json` arrays; objects for `badges_json`/`data_json`).
- Docs `style_runs_json` runs are contiguous and end at `len(body_text)` for all three docs, and heading runs cover whole lines.
- **Provisional snapshot comparison:** MATCH for every column used, except four columns the snapshot doesn't cover: `gslides.slides_pages.notes` (12 rows), `gslides.slides_page_elements.table_json` and `.ordinal` (23 rows), and `linear.linear_comments.sequence` (2 rows). The base exports don't carry them either. Under Eval 0 and schema/README this is an advisory, not a defect (Advisory 1).

## 8. Check C: dates, relationships and consistency

- **Clock.** Every event timestamp is at or before 2025-10-01T07:00Z. The latest are Leonard's email at 2025-09-30T21:05Z and the Oct 6 invite at 21:00Z. Only plan fields are later: the Oct 6 2025 16:00–16:45Z review event (created 09-30 21:00Z) and the Trello card due 2025-10-14T16:00Z.
- **Time encodings agree.** Slack `ts` = `created_at` (4/4). Gmail `internal_date` = `date` = `Date` header (37/37). Gmail thread-id time = first message (29/29). Trello id time = action/created time (11/11). Linear comments (17:25Z, 18:40Z) fall between issue created (17:10Z) and updated (18:40Z). Card 455 `dateLastActivity` (09-14 04:20Z) is after its base value (09-13 17:06:40Z). The Slack parent's `reply_count` 0→1 and `latest_reply` match the single new reply. The card badges (checkItems 4, comments 1) match the 4 check items and 1 comment, and the existing card's badges change only `comments` 0→1.
- **Weekdays and local times.** Tue Sep 23, Thu Sep 25, Mon Sep 29, Tue Sep 30 and Mon Oct 6 2025 are all correct weekdays. 9am PDT = 16:00Z on every invite and event. Edith's "session on Tuesday" (sent 09-26 09:40Z) matches the Tue Sep 23 Hiro call, which lists her as a guest. Ilse's "time this morning" email (09-25 22:30Z = 15:30 PT) follows the 9:00–9:45 PT call.
- **Agreement with the base.**
  - Leonard's 09-30 "flying to LA tomorrow morning for the Griffin AGM and the Dentsu meeting" matches the base Dentsu thread (earlier flight on Oct 1, 1:30pm meeting at Griffin) and Leonard's 10-01 00:02Z base invite.
  - The Dentsu "Thank you for the offer" email answers Leonard's base offer of 09-23 PT ("share the best email addresses … and we will add you"). Leonard's "seeing you in LA on Oct 1" matches the base meeting.
  - The T-Accelerate Linear note (TestFlight 09-22) matches base Slack and email on 09-22 ("you added him to testflight already?", "We already sent a testflight invite").
  - The Sep 3 bridge kickoff in the template matches Leonard's base 09-03 emails ("kicking off a $2.5M bridge this week").
  - Hiro was "sent, no response" in base Slack on 09-15. The injected 09-19 invite and 09-23 call come later, so nothing contradicts them.
  - The DocuSign completion uses the base sender (SVC_1302) and subject pattern.
- **Mailbox copies.** Each email has a copy in the mailbox of every internal sender and recipient (SENT for the sender) and nowhere else. Thread-snippet UPDATEs reflect the latest message.
- **Deliberate conflicts are settled by later records:**
  - Angel amounts: Slack and sheet 09-19 ($40K) → Anton's email 09-24 ($25K) → DocuSign completed 09-26.
  - Paul unsigned (nudge 09-29).
  - Leonard 09-26 "Invites … out to all three" → Arthur's Linear note 09-30 "Play internal track not added yet".
  - Robert 09-29 "email the pipeline to the board" → Leonard 09-30 "Let's not".
  - Arthur's Slack 09-29 shortcut → Leonard's 09-30 scope.
  - July template → Oct 14 template.
- **Grader-facing text.** None found. Every injected text is in a persona's voice, and no record addresses a solver or grader or describes the test.
- **Earlier advisories resolved by this version.** The Hiro call is now on the calendars (4 events + 3 invites, 09-23 16:00Z). Ilse's email no longer claims attachments ("I'll send … in a separate email"). The Dentsu account email Leonard and Arthur refer to now exists (09-26 03:10Z, 4 copies).

## 9. Findings

No demonstrated defects. Advisories (none blocks this stage):

1. **Columns not in the schema snapshot (Check B, provisional).** `slides_pages.notes`, `slides_page_elements.table_json`/`ordinal` and `linear_comments.sequence` appear in neither the snapshot nor the base exports. If a platform table lacks any of them, that INSERT fails and BEGIN/COMMIT rolls back the whole injection. The Trello comment ("The notes on slide 9 of the draft deck list the table's columns") depends on `notes`. Smallest fix: confirm the script loads on the platform and the slide notes and Linear comments appear. Or drop `table_json`, `ordinal` and `sequence` (NULL or default-like) and move the slide-9 note text somewhere the tools serve (the slide body or the Trello comment). Whether the Slides tools return speaker notes is a `/prompt` question.
2. **"came in Fri" (Check C, minor wording).** Arthur's ZOM-567 comment (line 303) says the Dentsu accounts "came in Fri". Ryo's email is 2025-09-26T03:10Z, which is Thu Sep 25 20:10 PT (Fri only in Japan). It changes no status, date or build-access fact. Smallest fix: "came in Thursday night", or move the email to Fri PT, e.g. `2025-09-26T16:10:00Z` (keep internal_date, the Date header, the thread-id time and the reply after it consistent).
3. **Leonard double-booked 09-25 9:30–9:45 PT (context).** The injected Ilse call (16:00–16:45Z) overlaps a base 1:1 on Leonard's calendar (`evt_c6d85261f1e1dc58ddf1ad`, 16:30–17:15Z, Leonard needsAction). This is common and not a data defect. Shift the call to 15:30–16:15Z only if you want a clean calendar.
4. **Trello board `dateLastActivity` not bumped (cosmetic).** The board stays at 2025-09-13T17:06:40Z, while the SQL adds activity on 09-14 and 09-27. Only cached metadata is affected.
5. **T-Accelerate Play date (context).** Arthur writes "Play internal track added Sep 23", but base Slack and email on 09-22 already shared the internal-test link. These fit together (the link was shared, the tester was added the next day), so this is not a contradiction.

## 10. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | All actors, parents and targets resolve. New keys don't collide in complete scans (§4). No ID-contract breaks. Drive files are readable. No second accounts. |
| B — SQL structure and supported schema rules | PASS | Structure, JSON shapes, NOT NULL columns, generated columns, Linear formats and doc style runs are valid. Four columns NOT COVERED by the snapshot are advisory (Advisory 1). Not live-certified. |
| C — Dates, relationships and consistency | PASS | All event times are before the clock. Encodings, chronology, counts and cross-record facts agree. Deliberate conflicts are settled by later records. Advisories 2–5 are minor or context. |

Outside certification scope (disclosed, not gates): live execution and current database compatibility (including the four columns), actual search ranking, Agent visibility and persona access (e.g. whether Fred can open the investor list or see slide notes), and task difficulty.

## 11. Stage ownership and reuse

`/prompt` may reuse these static checks only while all of these hold: SQL SHA-256 `b2bfda86002c267c8bb3a6043acccf557931d1d62bc045a6ba0c32f1a72e6539`, universe manifest `da2f4cf0…aac1a`, schema snapshot `31dcb2b4…`, id_contracts `fc4711ef…`, Eval 0 `e034019b…`, clock 2025-10-01T07:00Z. `/prompt` still owns discoverability, persona access, slide-notes visibility (Advisory 1) and investor-list visibility. Any new SQL version needs `/injection` again, then `/prompt`, `/hardness`, `/oe` and `/rubric`.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt. Optionally fix Advisory 2 ("came in Fri") and settle Advisory 1 (the four columns outside the snapshot) before running it.

Evidence limits: Static review only. The schema snapshot is unverified and doesn't cover slides_pages.notes, slides_page_elements.table_json/ordinal or linear_comments.sequence. No live load, tool-visibility or search-ranking checks.