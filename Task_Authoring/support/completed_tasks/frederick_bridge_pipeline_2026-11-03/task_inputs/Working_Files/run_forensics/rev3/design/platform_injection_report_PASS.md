# Injection Data-Integrity Review (Eval 0)

Review version: `injection-static-v2`
Evidence contract: `stage-evidence-v1`
Review time: 2026-11-01T20:43Z (actual)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Mode: chat review, attempt 6ae4e299a13034b7eb8305f8 (static, SQL not executed)

## 1. Scope and inputs

| Input | Value |
|---|---|
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` (revision 6, from chat attachment `01_Universe_Inject (5).sql`), 128,916 bytes, SHA-256 `952e12a9ad7a6b887a783b1aa8f8d028fd7807a460d3b5b0c39d0cf5d79985a2`. Replaces revision 5 (`b2bfda86…6539`), so the earlier injection report no longer applies. |
| Diff from revision 5 | Lines 3 (header: 11 UPDATE), 83 (slide 9 notes → NULL), 87 (slide 9 body gains the column list), 118 (**new** board `dateLastActivity` UPDATE), 136 (Trello comment now points to "Slide 9 … lists the table's columns"), 251–261 (Ilse invite emails now 8:30–9:15am PT), 280–286 (Ilse calendar events now 15:30–16:15Z), 305 (Linear comment "came in Thursday night"). All other lines are byte-identical (diff against the saved revision 5 upload, SHA `b2bfda86…6539`). |
| Assignment (context only) | Frederick Stone, Co-founder; Executive / Corporate Ops / Retrieval / long-horizon (not graded here) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Eval | `Evals/0_Injection_Quality_Eval.md` `e034019b8ec450437509a73dd3bae2d303b57561b0f67fcc1e5d19266f663eff` |
| Shared workflow | WORKFLOW.md `ee4cd8e1cc291c3b733bfd53907f073f3c8dcbfbbec4723b978a1e4a504fcd5d` (guide view); scoring.json `c14873e6…89e5bc` |
| Schema snapshot | `references/schema/injection.json` `31dcb2b43feca8e5c7cb67f37973f819c9b9774f12f8b15cb7da89ecd74c5151` (unverified, provisional) |
| ID contracts | `references/schema/id_contracts.json` `fc4711ef07667333c1cf2a417279826f0432539195f7acdfacfa86e9d9ed4682` |
| Lint | `hg_injection_lint.py` `a8226e2a69425355892a51eccf11d4e58876eb41be39d9b6840d4f3b8fc5448b`, version `injection-lint-v1` |
| Roster / ACL | roster.json `3f217451…84575`, acl.md `e9bca2b3…8c9f` (identity checks only) |

Input/authority issues: none. SQL lines 1–4 are comments, read as evidence of intent only. Line 4 ("re-apply this exact SQL before every agent run") is a setup note inside a comment, not text in any injected record, and says nothing about tool calls, pass rate or gates. The header's count (143 INSERT, 11 UPDATE) matches the parsed SQL.

## 2. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, base manifest, review version | NEW, done (revision 6 saved before review) |
| Run lint; resolve every flag | NEW, done (0 FAIL, 0 CHECK, 0 INFO) |
| Inventory every statement and affected record | NEW, done: 156 statements (BEGIN line 5, 143 INSERT, 11 UPDATE, COMMIT line 313), 154 row operations, ledger §5 |
| Check A | NEW, PASS |
| Check B | NEW, PASS (provisional snapshot advisory) |
| Check C | NEW, PASS (advisories) |
| Report coverage, findings, limits, one verdict | NEW, done |

Collision scans, reference resolution, schema comparison, encodings and chronology were all rerun against this SQL. Three base-only facts on records whose SQL text is unchanged were reused with provenance (§11); none of them is a collision or clock check.

## 3. Lint result

`hg_injection_lint.py` on SHA `952e12a9…985a2`, universe synthcut, clock 2025-10-01T07:00Z. Checks run: future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape.

Flags: **none** (FAIL 0, CHECK 0, INFO 0). Nothing to resolve. A clean lint was not treated as a pass; checks A–C below were run in full.

## 4. Source coverage

| Check | Source / pointer | Coverage | Result |
|---|---|---|---|
| Drive ids (6 new) + 2 parents | gdrive `data.json` `/drive_files` field `id` (hg_records) | 53,631 records, scan complete | New ids absent; parents `d_175c0d7bc72ed244b944cb` (/drive_files/2060, Fred's root) and `d_63fffeb4fab5233ed5bb73` (/drive_files/9030, Leonard's root) exist |
| Docs / Sheets / Slides ids | gdocs `/docs_documents` (595), gsheets `/sheets_spreadsheets` (356), gslides `/slides_presentations` (132) | complete (sheets/slides first attempt reported "source changed during the read" while the lazy filesystem fetched the files; rerun complete with 0 errors) | no collisions |
| Slide page / element object ids (12 + 23) | exact-string grep of gslides `data.json` | whole file | 0 hits for every `slide_…` / `el_…` id |
| Trello board / cards / idShort | trello `/boards` (5), `/cards` (803) | complete | board `640643a3…318e` (/boards/1, dateLastActivity 2025-09-13T17:06:40Z); card `68c5a49e…69d0` (/cards/801, "Existing Investor Update", idShort 455, comments 0); `68d8193c…8a2a` and idShort 466 absent; `Qa5QbkDO` in no card. All 803 base cards have shortLink/shortUrl NULL, as the new card does |
| Trello board activity | trello `/actions` (5,252; 2,462 on this board), `/cards` on this board (449) | complete | latest base action 2025-09-13T17:06:40Z (updateCard); max card dateLastActivity 2025-09-13T17:06:40Z; max idShort 455 |
| Trello actions / checklists / check items | `/actions`, `/checklists` (54), `/check_items` (161) | complete | no collisions |
| Trello member / list | `/members`, `/lists` | complete | `PERSON_6094_TRELLO_USER_ID` = Leonard Hayes; list `640643a3…3196` = "Doing" |
| Linear issue / user / team / comments | linear `data.json` `/issues` identifier + id (3,687), `/users` (41), `/teams` (5), `/comments` (0) | complete | ZOM-567 absent (553 ZOM issues, latest ZOM-566 created 2025-09-30T16:26:02Z); `usr_cc3e90160f490686` = arthur.blake; `team_ZOM` exists; comment ids absent |
| Contacts ids / emails / names | contacts `/contacts` (170) | complete | 3 new contact_ids absent; no base contact contains PERSON_3242, PERSON_9901–9904, "Karthic", "Edith" or "Ilse" |
| Calendar events / ical_uid / overlaps | gcal `/events` (10,395) | complete | 10 event_ids and 3 ical_uids absent; 0 non-cancelled base events overlap any injected event on the same calendar |
| Slack users / channels | slack `users.json`, `channels.json` | complete | EMPLOYEE_0016 = Robert, 0025 = Arthur Blake, 0038 = Leonard Hayes; C07C2866011 = #executives, C096HFA5Z8W = #bridge-pitch; all three are members of both |
| Slack message ids + thread parent | grep of all `slack/messages/*/*.json` | complete | 4 new ids absent; parent `73c2247f…13ac` only in `C096HFA5Z8W/2025-09.json` (Leonard, ts 1757716998.377299, reply_count 0, no later message in that file) |
| Gmail thread ids (29) and message ids (37); identity tokens | streaming pass over all `gmail/threads/*.json` | 81,404 files, 0 read errors | 0 thread-id, 0 message-id and 0 raw Message-ID string collisions. PERSON_9901–9904, "Anton Bernstein", "Heydon", "Edith Vane", "Ilse Marrow", "Brightwater": 0 hits |
| Identity of reused external tokens | reused from the revision-5 report §4 (provenance §11) | full threads read then | PERSON_3242 = Karthic R, T-Accelerate; PERSON_5221 = Ryo, Dentsu; PERSON_5487 = Leonard's Hiro intro addressee; PERSON_5282 = Hiro Investment Director; SVC_1302 = DocuSign sender |
| Referenced list | reused from the revision-5 report §4 (provenance §11) | complete then | "Game Investor List - Harmony Games 2025.xlsx" exists (/drive_files/31887) |
| Known base issues | `Evals/references/known_base_issues.md`, `guidelines/known_data_issues.md` | read | SQL touches no Snowflake/Confluence data and builds on no listed conflict |

## 5. Operation ledger

All 154 row operations in execution order (statement order = SQL line order; BEGIN at line 5, COMMIT at line 313). Every parent is created before its children.

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
| 11 | 29 | gsheets.sheets_sheets | INSERT | `f_6e1d93a0c4b72f85d39a0e` | tab Angels, 3 grid rows | parent in SQL |
| 12 | 32 | gslides.slides_presentations | INSERT | `f_a47d0e2c95b18f63e2c0d5` | HG BoD Oct 14 2025 (draft) | new; Drive row in SQL |
| 13 | 34 | gslides.slides_pages | INSERT | `slide_b4c21ca913ab` | index 0, notes NULL | unique; id absent from base gslides |
| 14 | 36 | gslides.slides_page_elements | INSERT | `el_6825f973029b` | on slide_b4c21ca913ab: Harmony Games Board Meeting | unique; id absent from base gslides |
| 15 | 38 | gslides.slides_page_elements | INSERT | `el_cffa02683868` | on slide_b4c21ca913ab: October 14, 2025 (draft) | unique; id absent from base gslides |
| 16 | 40 | gslides.slides_pages | INSERT | `slide_256dc0474f7c` | index 1, notes NULL | unique; id absent from base gslides |
| 17 | 42 | gslides.slides_page_elements | INSERT | `el_72151261faca` | on slide_256dc0474f7c: Agenda | unique; id absent from base gslides |
| 18 | 44 | gslides.slides_page_elements | INSERT | `el_ca7b40076cd7` | on slide_256dc0474f7c: Q3 recap / Zombie Match 3D alpha / Engine / F… | unique; id absent from base gslides |
| 19 | 46 | gslides.slides_pages | INSERT | `slide_fd6dbd079420` | index 2, notes NULL | unique; id absent from base gslides |
| 20 | 48 | gslides.slides_page_elements | INSERT | `el_90fbf6fd9c1b` | on slide_fd6dbd079420: Q3 recap | unique; id absent from base gslides |
| 21 | 50 | gslides.slides_page_elements | INSERT | `el_ef5243814e8f` | on slide_fd6dbd079420: Domino Delights: publisher search / Zombie Ma… | unique; id absent from base gslides |
| 22 | 52 | gslides.slides_pages | INSERT | `slide_bb11abfc5fad` | index 3, notes NULL | unique; id absent from base gslides |
| 23 | 54 | gslides.slides_page_elements | INSERT | `el_69587907b898` | on slide_bb11abfc5fad: Zombie Match 3D | unique; id absent from base gslides |
| 24 | 56 | gslides.slides_page_elements | INSERT | `el_6ca8bffe4445` | on slide_bb11abfc5fad: Alpha metrics (Robert to fill) | unique; id absent from base gslides |
| 25 | 58 | gslides.slides_pages | INSERT | `slide_cb3f0884f833` | index 4, notes NULL | unique; id absent from base gslides |
| 26 | 60 | gslides.slides_page_elements | INSERT | `el_0c72e8ba6af7` | on slide_cb3f0884f833: Engine | unique; id absent from base gslides |
| 27 | 62 | gslides.slides_page_elements | INSERT | `el_1e212bf4628e` | on slide_cb3f0884f833: What shipped in Q3 (Arthur to fill) | unique; id absent from base gslides |
| 28 | 64 | gslides.slides_pages | INSERT | `slide_a56932e4c738` | index 5, notes NULL | unique; id absent from base gslides |
| 29 | 66 | gslides.slides_page_elements | INSERT | `el_5da52b8348b0` | on slide_a56932e4c738: Team | unique; id absent from base gslides |
| 30 | 68 | gslides.slides_page_elements | INSERT | `el_4f7f04b6e984` | on slide_a56932e4c738: Headcount and contractors (Leonard to fill) | unique; id absent from base gslides |
| 31 | 70 | gslides.slides_pages | INSERT | `slide_c9c7eed73bb9` | index 6, notes NULL | unique; id absent from base gslides |
| 32 | 72 | gslides.slides_page_elements | INSERT | `el_b45885b83bf9` | on slide_c9c7eed73bb9: Runway | unique; id absent from base gslides |
| 33 | 74 | gslides.slides_page_elements | INSERT | `el_ed13f88ca45b` | on slide_c9c7eed73bb9: Cash and burn (Leonard to fill) | unique; id absent from base gslides |
| 34 | 76 | gslides.slides_pages | INSERT | `slide_329b5dfcb888` | index 7, notes NULL | unique; id absent from base gslides |
| 35 | 78 | gslides.slides_page_elements | INSERT | `el_09521ac10bd5` | on slide_329b5dfcb888: Options | unique; id absent from base gslides |
| 36 | 80 | gslides.slides_page_elements | INSERT | `el_d65f0ea436c8` | on slide_329b5dfcb888: Bridge / co-dev / engine deals | unique; id absent from base gslides |
| 37 | 82 | gslides.slides_pages | INSERT | `slide_68eecd4f5f2a` | index 8, notes NULL | unique; id absent from base gslides |
| 38 | 84 | gslides.slides_page_elements | INSERT | `el_b87125dbf11e` | on slide_68eecd4f5f2a: Fundraising | unique; id absent from base gslides |
| 39 | 86 | gslides.slides_page_elements | INSERT | `el_6548686fe965` | on slide_68eecd4f5f2a: Bridge round, pipeline as of Sep 30 / Firms o… | unique; id absent from base gslides |
| 40 | 88 | gslides.slides_pages | INSERT | `slide_98d06d32c8d6` | index 9, notes NULL | unique; id absent from base gslides |
| 41 | 90 | gslides.slides_page_elements | INSERT | `el_154065e277bc` | on slide_98d06d32c8d6: Asks for the board | unique; id absent from base gslides |
| 42 | 92 | gslides.slides_page_elements | INSERT | `el_ee461e258b77` | on slide_98d06d32c8d6: Intros, especially games funds and strategics | unique; id absent from base gslides |
| 43 | 94 | gslides.slides_pages | INSERT | `slide_fcf2cb38bf31` | index 10, notes NULL | unique; id absent from base gslides |
| 44 | 96 | gslides.slides_page_elements | INSERT | `el_8ee884c1e93b` | on slide_fcf2cb38bf31: Appendix | unique; id absent from base gslides |
| 45 | 98 | gslides.slides_page_elements | INSERT | `el_34bc96464df6` | on slide_fcf2cb38bf31: Investor FAQ (link) | unique; id absent from base gslides |
| 46 | 100 | gslides.slides_pages | INSERT | `slide_5c7db3c42932` | index 11, notes NULL | unique; id absent from base gslides |
| 47 | 102 | gslides.slides_page_elements | INSERT | `el_ef3226341cb0` | on slide_5c7db3c42932: Thank you | unique; id absent from base gslides |
| 48 | 105 | slack.slack_messages | INSERT | `4921f321db5d08f936aac24a6a1d2af8` | C07C2866011 EMPLOYEE_0038 2025-09-19T17:40:00.000000Z | new id; author is channel member; ts = created_at |
| 49 | 107 | slack.slack_messages | INSERT | `7fef94264090696760180223fc8265e7` | C07C2866011 EMPLOYEE_0025 2025-09-29T18:00:00.000000Z | new id; author is channel member; ts = created_at |
| 50 | 109 | slack.slack_messages | INSERT | `3f2d8f04b29a78808033543c740bb669` | C096HFA5Z8W EMPLOYEE_0016 2025-09-29T16:00:00.000000Z | new id; author is channel member; ts = created_at |
| 51 | 111 | slack.slack_messages | INSERT | `cf10d4f7f88143dc7ab976df27513790` | C096HFA5Z8W EMPLOYEE_0016 2025-09-29T22:14:00.000000Z, reply to 73c2247f… | new id; author is channel member; ts = created_at |
| 52 | 113 | slack.slack_messages | UPDATE | `73c2247f4a31f32d10b3068ecd1d13ac` | reply_count 0→1, reply_users_count 1, latest_reply 1759184040.552871 | target exists (C096HFA5Z8W/2025-09.json), base reply_count 0 |
| 53 | 115 | trello.trello_actions | INSERT | `68c64270d660c977c4696986` | commentCard 2025-09-14T04:20:00Z on card 68c5a49e…, by Leonard | new; id hex time = date |
| 54 | 117 | trello.trello_cards | UPDATE | `68c5a49e8491a9d7faf869d0` | badges.comments 0→1, dateLastActivity 2025-09-13T17:06:40Z→2025-09-14T04:20:00Z | target /cards/801 exists |
| 55 | 118 | trello.trello_boards | UPDATE | `640643a3fd8f3ca308d9318e` | dateLastActivity 2025-09-13T17:06:40Z→2025-09-27T17:30:24Z | target /boards/1 exists; equals latest injected action; no later base activity |
| 56 | 119 | trello.trello_cards | INSERT | `68d8193cf451863621c88a2a` | Board Deck - Oct 14, list Doing, idShort 466, due 2025-10-14T16:00:00Z (plan), dateLastActivity 2025-09-27T17:30:24Z | new id/idShort/shortLink, no collision |
| 57 | 121 | trello.trello_actions | INSERT | `68d8193c164e823ac3ae735d` | createCard 2025-09-27T17:05:00Z on card 68d8193c…, by Leonard | new; id hex time = date |
| 58 | 123 | trello.trello_checklists | INSERT | `68d81ae0bac8fd292e6606f8` | Sections | new; card in SQL |
| 59 | 125 | trello.trello_check_items | INSERT | `68d81ae032fe8d64dbd262c7` | Fundraising - Fred | new; checklist in SQL |
| 60 | 127 | trello.trello_check_items | INSERT | `68d81ae087c12c3d08c79ff8` | Product - Robert | new; checklist in SQL |
| 61 | 129 | trello.trello_check_items | INSERT | `68d81ae05ac90637e942026c` | Engine - Arthur | new; checklist in SQL |
| 62 | 131 | trello.trello_check_items | INSERT | `68d81ae07d46d8fe71f4ba98` | Runway and options - Leonard | new; checklist in SQL |
| 63 | 133 | trello.trello_actions | INSERT | `68d81ae0459a87b4efb4b1e3` | addChecklistToCard 2025-09-27T17:12:00Z on card 68d8193c…, by Leonard | new; id hex time = date |
| 64 | 135 | trello.trello_actions | INSERT | `68d81f30a6c94e2b7d05e1f4` | commentCard 2025-09-27T17:30:24Z on card 68d8193c…, by Leonard | new; id hex time = date |
| 65 | 138 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844623441920000059` | Fred - for the 14th could you just email the … | new; no collision; id time = first message |
| 66 | 140 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAdKLID2b1N4D6wzcwD-r…` | 2025-09-29T18:20:00Z from robert@harmonygames.co: board pipeline | new; date = internal_date = Date header |
| 67 | 142 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844623441920000061` | Fred - for the 14th could you just email the … | new; no collision; id time = first message |
| 68 | 144 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAdKLID2b1N4D6wzcwD-r…` | 2025-09-29T18:20:00Z from robert@harmonygames.co: board pipeline | new; date = internal_date = Date header |
| 69 | 146 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844623441920000062` | Fred - for the 14th could you just email the … | new; no collision; id time = first message |
| 70 | 148 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAdKLID2b1N4D6wzcwD-r…` | 2025-09-29T18:20:00Z from robert@harmonygames.co: board pipeline | new; date = internal_date = Date header |
| 71 | 150 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844724419788800011` | Fred, I'm flying to LA tomorrow morning for t… | new; no collision; id time = first message |
| 72 | 152 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAxDeR9CSc9iEY-zACLQa…` | 2025-09-30T21:05:00Z from leonard.hayes@harmonygames.co: Oct 14 board pre-read - fundraising section | new; date = internal_date = Date header |
| 73 | 154 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844724419788800013` | Fred, I'm flying to LA tomorrow morning for t… | new; no collision; id time = first message |
| 74 | 156 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAxDeR9CSc9iEY-zACLQa…` | 2025-09-30T21:05:00Z from leonard.hayes@harmonygames.co: Oct 14 board pre-read - fundraising section | new; date = internal_date = Date header |
| 75 | 158 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844724419788800014` | Fred, I'm flying to LA tomorrow morning for t… | new; no collision; id time = first message |
| 76 | 160 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAxDeR9CSc9iEY-zACLQa…` | 2025-09-30T21:05:00Z from leonard.hayes@harmonygames.co: Oct 14 board pre-read - fundraising section | new; date = internal_date = Date header |
| 77 | 162 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844724419788800015` | Fred, I'm flying to LA tomorrow morning for t… | new; no collision; id time = first message |
| 78 | 164 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAxDeR9CSc9iEY-zACLQa…` | 2025-09-30T21:05:00Z from leonard.hayes@harmonygames.co: Oct 14 board pre-read - fundraising section | new; date = internal_date = Date header |
| 79 | 166 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844162278195200023` | Leonard, Had another look at my numbers. I ca… | new; no collision; id time = first message |
| 80 | 168 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CACJhvEE55qdWXuKC3BWl…` | 2025-09-24T16:10:00Z from PERSON_9901_EMAIL: SAFE amount | new; date = internal_date = Date header |
| 81 | 170 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844162278195200025` | Leonard, Had another look at my numbers. I ca… | new; no collision; id time = first message |
| 82 | 172 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CACJhvEE55qdWXuKC3BWl…` | 2025-09-24T16:10:00Z from PERSON_9901_EMAIL: SAFE amount | new; date = internal_date = Date header |
| 83 | 174 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844354293432320031` | Hello Frederick Stone, All signers completed … | new; no collision; id time = first message |
| 84 | 176 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAiKDPIoVSAFUBccUSRRB…` | 2025-09-26T19:02:00Z from SVC_1302_EMAIL: Completed: Complete with docusign: Harmony Ga… | new; date = internal_date = Date header |
| 85 | 178 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844610859008000037` | Hi Paul, Gentle nudge on the SAFE in DocuSign… | new; no collision; id time = first message |
| 86 | 180 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAP6Gn2LV490e3El5rBDC…` | 2025-09-29T15:00:00Z from leonard.hayes@harmonygames.co: SAFE in DocuSign | new; date = internal_date = Date header |
| 87 | 182 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844610859008000039` | Hi Paul, Gentle nudge on the SAFE in DocuSign… | new; no collision; id time = first message |
| 88 | 184 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAP6Gn2LV490e3El5rBDC…` | 2025-09-29T15:00:00Z from leonard.hayes@harmonygames.co: SAFE in DocuSign | new; date = internal_date = Date header |
| 89 | 186 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844318935449600041` | Leonard, Thanks again for the session on Tues… | new; no collision; id time = first message |
| 90 | 188 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_l…` | 2025-09-26T09:40:00Z from PERSON_9903_EMAIL: Harmony Games bridge | new; date = internal_date = Date header |
| 91 | 190 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844318935449600043` | Leonard, Thanks again for the session on Tues… | new; no collision; id time = first message |
| 92 | 192 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_l…` | 2025-09-26T09:40:00Z from PERSON_9903_EMAIL: Harmony Games bridge | new; date = internal_date = Date header |
| 93 | 194 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844294398771200045` | Leonard-san, Thank you for the offer. Please … | new; no collision; id time = first message |
| 94 | 196 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4…` | 2025-09-26T03:10:00Z from PERSON_5221_EMAIL: Zombie Match 3D access | new; date = internal_date = Date header |
| 95 | 198 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844294398771200047` | Leonard-san, Thank you for the offer. Please … | new; no collision; id time = first message |
| 96 | 200 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4…` | 2025-09-26T03:10:00Z from PERSON_5221_EMAIL: Zombie Match 3D access | new; date = internal_date = Date header |
| 97 | 202 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844294398771200048` | Leonard-san, Thank you for the offer. Please … | new; no collision; id time = first message |
| 98 | 204 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4…` | 2025-09-26T03:10:00Z from PERSON_5221_EMAIL: Zombie Match 3D access | new; date = internal_date = Date header |
| 99 | 206 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844294398771200049` | Leonard-san, Thank you for the offer. Please … | new; no collision; id time = first message |
| 100 | 208 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAqlOj-B9ZBEdN9-Kfts4…` | 2025-09-26T03:10:00Z from PERSON_5221_EMAIL: Zombie Match 3D access | new; date = internal_date = Date header |
| 101 | 210 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1844294398771200045` | snippet → latest reply | thread inserted earlier in SQL |
| 102 | 211 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CA0tK15jPm2APp9fC951n…` | 2025-09-26T17:20:00Z from leonard.hayes@harmonygames.co: Re: Zombie Match 3D access | new; date = internal_date = Date header |
| 103 | 213 | gmail.gmail_threads | UPDATE | `leonard.hayes@harmonygames.co/1844294398771200047` | snippet → latest reply | thread inserted earlier in SQL |
| 104 | 214 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CA0tK15jPm2APp9fC951n…` | 2025-09-26T17:20:00Z from leonard.hayes@harmonygames.co: Re: Zombie Match 3D access | new; date = internal_date = Date header |
| 105 | 216 | gmail.gmail_threads | UPDATE | `robert@harmonygames.co/1844294398771200048` | snippet → latest reply | thread inserted earlier in SQL |
| 106 | 217 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CA0tK15jPm2APp9fC951n…` | 2025-09-26T17:20:00Z from leonard.hayes@harmonygames.co: Re: Zombie Match 3D access | new; date = internal_date = Date header |
| 107 | 219 | gmail.gmail_threads | UPDATE | `arthur.blake@harmonygames.co/1844294398771200049` | snippet → latest reply | thread inserted earlier in SQL |
| 108 | 220 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CA0tK15jPm2APp9fC951n…` | 2025-09-26T17:20:00Z from leonard.hayes@harmonygames.co: Re: Zombie Match 3D access | new; date = internal_date = Date header |
| 109 | 222 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844276782694400053` | Hi Ilse, Thanks for the time this morning. I'… | new; no collision; id time = first message |
| 110 | 224 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq…` | 2025-09-25T22:30:00Z from leonard.hayes@harmonygames.co: Harmony Games - follow up | new; date = internal_date = Date header |
| 111 | 226 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844276782694400055` | Hi Ilse, Thanks for the time this morning. I'… | new; no collision; id time = first message |
| 112 | 228 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq…` | 2025-09-25T22:30:00Z from leonard.hayes@harmonygames.co: Harmony Games - follow up | new; date = internal_date = Date header |
| 113 | 230 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844276782694400056` | Hi Ilse, Thanks for the time this morning. I'… | new; no collision; id time = first message |
| 114 | 232 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq…` | 2025-09-25T22:30:00Z from leonard.hayes@harmonygames.co: Harmony Games - follow up | new; date = internal_date = Date header |
| 115 | 234 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844276782694400057` | Hi Ilse, Thanks for the time this morning. I'… | new; no collision; id time = first message |
| 116 | 236 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq…` | 2025-09-25T22:30:00Z from leonard.hayes@harmonygames.co: Harmony Games - follow up | new; date = internal_date = Date header |
| 117 | 238 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1844276782694400053` | snippet → latest reply | thread inserted earlier in SQL |
| 118 | 239 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b…` | 2025-09-26T15:05:00Z from PERSON_9904_EMAIL: Re: Harmony Games - follow up | new; date = internal_date = Date header |
| 119 | 241 | gmail.gmail_threads | UPDATE | `leonard.hayes@harmonygames.co/1844276782694400055` | snippet → latest reply | thread inserted earlier in SQL |
| 120 | 242 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b…` | 2025-09-26T15:05:00Z from PERSON_9904_EMAIL: Re: Harmony Games - follow up | new; date = internal_date = Date header |
| 121 | 244 | gmail.gmail_threads | UPDATE | `robert@harmonygames.co/1844276782694400056` | snippet → latest reply | thread inserted earlier in SQL |
| 122 | 245 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b…` | 2025-09-26T15:05:00Z from PERSON_9904_EMAIL: Re: Harmony Games - follow up | new; date = internal_date = Date header |
| 123 | 247 | gmail.gmail_threads | UPDATE | `arthur.blake@harmonygames.co/1844276782694400057` | snippet → latest reply | thread inserted earlier in SQL |
| 124 | 248 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b…` | 2025-09-26T15:05:00Z from PERSON_9904_EMAIL: Re: Harmony Games - follow up | new; date = internal_date = Date header |
| 125 | 250 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843992534712320061` | Ilse Marrow and Leonard Hayes Thursday Sep 25… | new; no collision; id time = first message |
| 126 | 252 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-2b67d1aa-cbd…` | 2025-09-22T19:12:00Z from leonard.hayes@harmonygames.co: Invitation: Ilse Marrow and Leonard Hayes @ T… | new; date = internal_date = Date header |
| 127 | 254 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1843992534712320063` | Ilse Marrow and Leonard Hayes Thursday Sep 25… | new; no collision; id time = first message |
| 128 | 256 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-c82c189b-c33…` | 2025-09-22T19:12:00Z from leonard.hayes@harmonygames.co: Invitation: Ilse Marrow and Leonard Hayes @ T… | new; date = internal_date = Date header |
| 129 | 258 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1843992534712320064` | Ilse Marrow and Leonard Hayes Thursday Sep 25… | new; no collision; id time = first message |
| 130 | 260 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-44faeeb8-a4b…` | 2025-09-22T19:12:00Z from leonard.hayes@harmonygames.co: Invitation: Ilse Marrow and Leonard Hayes @ T… | new; date = internal_date = Date header |
| 131 | 262 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843718101401600063` | PERSON_5487_NAME and Leonard Hayes Tuesday Se… | new; no collision; id time = first message |
| 132 | 264 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-2d8383e3-21d…` | 2025-09-19T18:30:00Z from leonard.hayes@harmonygames.co: Invitation: PERSON_5487_NAME and Leonard Haye… | new; date = internal_date = Date header |
| 133 | 266 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1843718101401600065` | PERSON_5487_NAME and Leonard Hayes Tuesday Se… | new; no collision; id time = first message |
| 134 | 268 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-010d9a7c-810…` | 2025-09-19T18:30:00Z from leonard.hayes@harmonygames.co: Invitation: PERSON_5487_NAME and Leonard Haye… | new; date = internal_date = Date header |
| 135 | 270 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1843718101401600066` | PERSON_5487_NAME and Leonard Hayes Tuesday Se… | new; no collision; id time = first message |
| 136 | 272 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-9d6c5aee-50e…` | 2025-09-19T18:30:00Z from leonard.hayes@harmonygames.co: Invitation: PERSON_5487_NAME and Leonard Haye… | new; date = internal_date = Date header |
| 137 | 274 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844724105216000067` | Board pre-read review - fundraising Monday Oc… | new; no collision; id time = first message |
| 138 | 276 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-297f69c9-ad6…` | 2025-09-30T21:00:00Z from leonard.hayes@harmonygames.co: Invitation: Board pre-read review - fundraisi… | new; date = internal_date = Date header |
| 139 | 279 | gcal.gcal_events | INSERT | `evt_2f86b0d4c9e17a35b64e0d` | frederick.stone: Ilse Marrow and Leonard Hayes 2025-09-25T15:30:00Z–16:15Z | new id; ical_uid absent from base; no base overlap |
| 140 | 281 | gcal.gcal_events | INSERT | `evt_b511d4619c6f46ee63959b` | leonard.hayes: Ilse Marrow and Leonard Hayes 2025-09-25T15:30:00Z–16:15Z | new id; ical_uid absent from base; no base overlap |
| 141 | 283 | gcal.gcal_events | INSERT | `evt_8bd5e929463b854ec0ad13` | robert: Ilse Marrow and Leonard Hayes 2025-09-25T15:30:00Z–16:15Z | new id; ical_uid absent from base; no base overlap |
| 142 | 285 | gcal.gcal_events | INSERT | `evt_ca908a712455521f1f8b43` | arthur.blake: Ilse Marrow and Leonard Hayes 2025-09-25T15:30:00Z–16:15Z | new id; ical_uid absent from base; no base overlap |
| 143 | 287 | gcal.gcal_events | INSERT | `evt_7d3e19b04a6c25f8e1b9a0` | frederick.stone: PERSON_5487_NAME and Leonard Hayes 2025-09-23T16:00:00Z–16:45Z | new id; ical_uid absent from base; no base overlap |
| 144 | 289 | gcal.gcal_events | INSERT | `evt_99df25b554cac93e2926fd` | leonard.hayes: PERSON_5487_NAME and Leonard Hayes 2025-09-23T16:00:00Z–16:45Z | new id; ical_uid absent from base; no base overlap |
| 145 | 291 | gcal.gcal_events | INSERT | `evt_671dce00bcb85abb3e355e` | robert: PERSON_5487_NAME and Leonard Hayes 2025-09-23T16:00:00Z–16:45Z | new id; ical_uid absent from base; no base overlap |
| 146 | 293 | gcal.gcal_events | INSERT | `evt_d65aa89778c3ebfa5d97b2` | arthur.blake: PERSON_5487_NAME and Leonard Hayes 2025-09-23T16:00:00Z–16:45Z | new id; ical_uid absent from base; no base overlap |
| 147 | 295 | gcal.gcal_events | INSERT | `evt_9c41e7a2d05b38f6e1a7c4` | frederick.stone: Board pre-read review - fundraising 2025-10-06T16:00:00Z–16:45Z | new id; ical_uid absent from base; no base overlap |
| 148 | 297 | gcal.gcal_events | INSERT | `evt_75d8a0687ea57b663a40b0` | leonard.hayes: Board pre-read review - fundraising 2025-10-06T16:00:00Z–16:45Z | new id; ical_uid absent from base; no base overlap |
| 149 | 300 | linear.linear_issues | INSERT | `ZOM-567` | team_ZOM, assignee/creator Arthur, Todo, created 2025-09-30T17:10:00Z, updated 2025-09-30T18:40:00Z | new; follows ZOM-566 (09-30 16:26Z) |
| 150 | 302 | linear.linear_comments | INSERT | `lc_94eb35d962cfbdd31e1bd496` | ZOM-567, Arthur, 2025-09-30T17:25:00Z, sequence 1 | new; issue in SQL |
| 151 | 304 | linear.linear_comments | INSERT | `lc_b549f3057640a5eb08f7581e` | ZOM-567, Arthur, 2025-09-30T18:40:00Z, sequence 2 | new; issue in SQL |
| 152 | 307 | contacts.contacts | INSERT | `e3a91c07d5b48f26a0c7e314` | Edith Vane, Partner, Hiro Capital, PERSON_9903_EMAIL | new id; email not in base contacts |
| 153 | 309 | contacts.contacts | INSERT | `b72f0d6e19c3a84e5d21f9a0` | Ilse Marrow, Principal, Brightwater Games Fund, PERSON_9904_EMAIL | new id; email not in base contacts |
| 154 | 311 | contacts.contacts | INSERT | `5d0e8b31f7a29c64e1b0d3a8` | Karthic R, T-Accelerate Capital (PXLite fund), PERSON_3242_EMAIL | new id; email not in base contacts |

## 6. Check A: records, references and IDs

- **References resolve.** All Drive parents, the Trello board (UPDATE target), list, member and existing card (UPDATE target), the Linear team and user, both Slack channels, all three Slack authors and the Slack thread parent (UPDATE target) exist in the base (§4). Children inserted by the SQL (docs/sheets/slides rows, slide pages and elements, checklist and check items, Linear comments, Gmail messages and thread-snippet UPDATEs) reference rows inserted earlier in the same script. Each UPDATE uses a primary-key predicate that hits exactly one row.
- **No collisions.** Every new key was checked against complete collections: Drive/Docs/Sheets/Slides ids and slide object ids, Trello card id/idShort/shortLink/actions/checklists/check items, Linear identifier/id/comment ids, contact ids, gcal event ids and ical_uids, Slack message ids, and Gmail thread and message ids (all 81,404 thread files). No duplicates within the SQL. The 10 calendar copies share 3 ical_uids by design (one per meeting, one copy per attendee), and mailbox copies of one email share a Message-ID under per-user ids, as in the base.
- **idShort 466.** The board's base max is 455 with 449 cards, so idShort already has gaps in the base; skipping 456–465 is consistent with that and collides with nothing.
- **ID contracts.** Gmail `history_id` is NULL on every thread (allowed). No Drive row sets `content_path`. Formats match the base: `f_`/`d_` + 22 hex for Drive; 24-hex Trello ids whose first 8 hex digits encode the creation time exactly (11/11, e.g. `68d81f30` = 2025-09-27T17:30:24Z); `user/<thread>` Gmail thread ids whose number encodes the first message time (29/29); 32-hex Slack ids.
- **Readable Drive files.** The 3 Google Docs have docs_documents rows with non-empty `body_text` (432 / 1,708 / 285 chars). The spreadsheet has a sheets row and a grid. The presentation has 12 pages and 23 elements. The folder holds no content.
- **One account per person.** Internal actors use their existing accounts (Leonard, Robert, Arthur, Fred). Reused external tokens map to the same people as in the base. The new tokens PERSON_9901–9904 appear nowhere in the base, so no existing person gets a second identity. Karthic's new contact uses his existing address PERSON_3242 and no base contact holds it.

## 7. Check B: SQL structure and supported schema rules

- Structure: one BEGIN/COMMIT block; every INSERT names its columns and gives one VALUES row of matching length (lint parsed all 154 rows with no INFO). The 11 UPDATEs use primary-key predicates.
- Generated columns (`text_fts`, `body_text_fts`) are not set (0 occurrences of `_fts`). Linear text dates use `YYYY-MM-DDTHH:MM:SSZ`. `state_history_json = '[]'` is present on the new issue. Every NOT NULL column without a default in the snapshot is supplied on every INSERT (independent check of all 19 affected tables). All `*_json`, `badges_json` and `data_json` values parse, with the base shapes (Slack `metadata_json '{}'`; lists for array columns; objects for badges/data).
- Docs `style_runs_json` runs are contiguous and end at `len(body_text)` for all three docs.
- `trello.trello_boards.dateLastActivity` (new UPDATE, line 118) exists in the snapshot.
- **Provisional snapshot comparison:** MATCH for every column used, except four columns the snapshot doesn't cover: `gslides.slides_pages.notes` (12 rows, now all NULL), `gslides.slides_page_elements.table_json` (23 rows, NULL) and `.ordinal` (23 rows), and `linear.linear_comments.sequence` (2 rows). Under Eval 0 and schema/README this is an advisory, not a defect (Advisory 1).

## 8. Check C: dates, relationships and consistency

- **Clock.** Every event timestamp is at or before 2025-10-01T07:00Z (latest: Leonard's email 2025-09-30T21:05Z, Oct 6 invite 21:00Z). Only plan fields are later: the Oct 6 2025 16:00–16:45Z review events (created 09-30 21:00Z) and the Trello card due 2025-10-14T16:00Z.
- **Changes in this revision, checked fresh.**
  - Ilse call: 8:30–9:15am PDT = 15:30–16:15Z on Thu Sep 25. The 3 invite emails (subject, body, snippet, thread snippet) and the 4 events (`start_ts`/`end_ts` = `start_json`/`end_json`) agree; invite sent 09-22 19:12Z = event `created`. Leonard's "Thanks for the time this morning" (09-25 22:30Z = 3:30pm PT) follows the call. No base event on any of the 4 calendars overlaps it, so the earlier double-booking with `evt_c6d85261f1e1dc58ddf1ad` is gone.
  - Board `dateLastActivity` 2025-09-13T17:06:40Z → 2025-09-27T17:30:24Z moves forward, equals the latest injected board action (commentCard `68d81f30…`) and is later than every base action on the board (latest 2025-09-13T17:06:40Z). It also equals the new card's `dateLastActivity`.
  - Slide 9 / Trello comment: the Fundraising slide is index 8 (9th of 12 pages) and its body element `el_6548686fe965` now lists the table columns, matching "Slide 9 of the draft deck lists the table's columns". Nothing depends on speaker notes any more.
  - "came in Thursday night": Ryo's email is 2025-09-26T03:10Z = Thu Sep 25 8:10pm PT. Correct.
- **Time encodings agree.** Slack `ts` = `created_at` (4/4). Gmail `internal_date` = `date` = `Date` header (37/37). Gmail thread-id time = first message (29/29). Trello id time = action/created time (11/11). Linear comments (17:25Z, 18:40Z) fall between issue created (17:10Z) and updated (18:40Z). Card 455 `dateLastActivity` (09-14 04:20Z) is after its base value. The Slack parent's `reply_count` 0→1 and `latest_reply` match the single new reply (`thread_parent_id` and `thread_ts_legacy` point to the parent). The new card's badges (checkItems 4, comments 1) match its 4 check items and 1 comment.
- **Weekdays and local times.** Tue Sep 23, Thu Sep 25, Mon Sep 29, Tue Sep 30 and Mon Oct 6 2025 are correct weekdays. Hiro call 9–9:45am PDT = 16:00–16:45Z; Oct 6 review 9–9:45am PDT = 16:00–16:45Z.
- **Agreement with the base** (SQL text unchanged from revision 5; facts reused with provenance, §11, and the Dentsu timing rechecked above): Leonard's Oct 1 LA trip matches the base Dentsu thread; the Dentsu account email answers Leonard's base offer; the T-Accelerate TestFlight date matches base Slack/email on 09-22; the Sep 3 bridge kickoff matches Leonard's base 09-03 emails; the Hiro invite/call come after base Slack's 09-15 "sent, no response"; the DocuSign completion uses the base sender and subject pattern.
- **Mailbox copies.** Each email has a copy in the mailbox of every internal sender and recipient and nowhere else (the organizer gets no invite copy). Thread-snippet UPDATEs reflect the latest message.
- **Deliberate conflicts are settled by later records:** angel amounts (Slack/sheet 09-19 $40K → Anton 09-24 $25K → DocuSign completed 09-26); Paul unsigned (nudge 09-29); Leonard 09-26 "Invites … out to all three" → Arthur 09-30 "Play internal track not added yet"; Robert 09-29 "email the pipeline to the board" → Leonard 09-30 "Let's not"; Arthur's Slack 09-29 shortcut → Leonard's 09-30 scope; July template → Oct 14 template.
- **Grader-facing text.** None found. Every injected text is in a persona's voice; no record addresses a solver or grader or describes the test.

## 9. Findings

No demonstrated defects. Revision 5's advisories 2 ("came in Fri"), 3 (Leonard double-booked) and 4 (board `dateLastActivity` not bumped) are resolved, and advisory 1 is narrowed. Remaining advisories (none blocks this stage):

1. **Columns not in the schema snapshot (Check B, provisional).** `slides_pages.notes` (all NULL), `slides_page_elements.table_json` (all NULL) and `.ordinal`, and `linear_comments.sequence` appear in neither the snapshot nor the base exports. If a platform table lacks any of them, that INSERT fails and BEGIN/COMMIT rolls back the whole injection. No task content depends on them any more. Smallest fix, if you want to remove the risk: drop those four columns from the INSERT column lists (and their values), or confirm the script loads on the platform.
2. **T-Accelerate Play date (context).** Arthur writes "Play internal track added Sep 23", while base Slack and email on 09-22 already shared the internal-test link. These fit together (link shared, tester added the next day), so this is not a contradiction.

## 10. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | All actors, parents and targets resolve. New keys don't collide in complete scans (§4). No ID-contract breaks. Drive files are readable. No second accounts. |
| B — SQL structure and supported schema rules | PASS | Structure, JSON shapes, NOT NULL columns, generated columns, Linear formats and doc style runs are valid. Four columns NOT COVERED by the snapshot are advisory (Advisory 1). Not live-certified. |
| C — Dates, relationships and consistency | PASS | All event times are before the clock. Encodings, chronology, counts and cross-record facts agree, including every revision-6 change. Deliberate conflicts are settled by later records. |

Outside certification scope (disclosed, not gates): live execution and current database compatibility (including the four columns), actual search ranking, Agent visibility and persona access (e.g. whether Fred can open the investor list), and task difficulty.

## 11. Stage ownership and reuse

Reused evidence (stage-evidence-v1), all from `Evals/task_inputs/reports/0_injection.md` as it stood before this rerun, SHA-256 `2a970e4ac8411935c005a175dd59fd19cd6bda8b1186e458f6e519cbb1f31e06` (injection-static-v2, PASS/COMPLETE, SQL `b2bfda86…6539`):

| Item | Source ledger / check | Dependencies verified unchanged |
|---|---|---|
| External token identities (PERSON_3242, 5221, 5487, 5282, SVC_1302) | §4 row "Identity of reused external tokens"; Check A | universe manifest `da2f4cf0…aac1a`; Gmail source unchanged; SQL rows using these tokens byte-identical to revision 5 (diff) |
| "Game Investor List - Harmony Games 2025.xlsx" exists (/drive_files/31887) | §4 row "Referenced list" | universe manifest; referencing SQL text unchanged |
| Base agreement facts (Dentsu trip/offer, T-Accelerate 09-22, Sep 3 kickoff, Hiro 09-15, DocuSign pattern) | §8 "Agreement with the base" | universe manifest; the SQL rows involved unchanged except line 305, whose new wording was checked fresh |

`/prompt` may reuse these static checks only while all of these hold: SQL SHA-256 `952e12a9ad7a6b887a783b1aa8f8d028fd7807a460d3b5b0c39d0cf5d79985a2`, universe manifest `da2f4cf0…aac1a`, schema snapshot `31dcb2b4…`, id_contracts `fc4711ef…`, Eval 0 `e034019b…`, clock 2025-10-01T07:00Z. `/prompt` still owns discoverability, persona access and investor-list visibility. Any new SQL version needs `/injection` again, then `/prompt`, `/hardness`, `/oe` and `/rubric`.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt, then /hardness, /oe and /rubric. Optionally drop the four snapshot-uncovered columns (Advisory 1) first; that would be a new SQL version needing /injection again.

Evidence limits: Static review only. The schema snapshot is unverified and doesn't cover slides_pages.notes, slides_page_elements.table_json/ordinal or linear_comments.sequence. Three base-only facts reused with provenance (§11). No live load, tool-visibility or search-ranking checks.