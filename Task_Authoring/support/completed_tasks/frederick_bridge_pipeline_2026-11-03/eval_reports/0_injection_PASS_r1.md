# Injection Data-Integrity Review (Eval 0)

Review version: `injection-static-v2`
Evidence contract: `stage-evidence-v1`
Review time: 2026-11-01T19:15Z (actual)
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Mode: chat review, attempt 6ae4e299a13034b7eb8305f8 (static, SQL not executed)

## 1. Scope and inputs

| Input | Value |
|---|---|
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` (revision 4, from chat attachment `01_Universe_Inject (2).sql`), 106,008 bytes, SHA-256 `0b6812c56fe6876a2c916c8a15138d16c33635b848890d57d4ec058afafc640d`. Replaces revision 3 (unfilled template, `e4229fee…`). |
| Assignment (context only) | Frederick Stone, Co-founder; Executive / Corporate Ops / Retrieval / long-horizon (not graded here) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest `Evals/references/universes/synthcut/universe_manifest.json` SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Eval | `Evals/0_Injection_Quality_Eval.md` `e034019b…6eff` |
| Shared workflow | WORKFLOW.md `ee4cd8e1…fcd5d` (guide view); scoring.json `c14873e6…89e5bc` |
| Schema snapshot | `references/schema/injection.json` `31dcb2b4…5c7cb67` (unverified, provisional) |
| ID contracts | `references/schema/id_contracts.json` `fc4711ef…ed4682` |
| Lint | `hg_injection_lint.py` `a8226e2a…448b`, version `injection-lint-v1` |
| Roster / ACL | roster.json `3f217451…84575`, acl.md `e9bca2b3…8c9f` (identity checks only) |

Input/authority issues: none. The SQL header lines 1–4 are comments (evidence of intent only). Line 4 says "re-apply this exact SQL before every agent run": it is a setup note in a comment, not text in any injected record, and it is not about tool calls, pass rate or gates.

## 2. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, base manifest, review version | NEW, done |
| Run lint; resolve every flag | NEW, done (0 FAIL, 0 CHECK, 0 INFO) |
| Inventory every statement and affected record | NEW, done (135 statements: 129 INSERT, 6 UPDATE, plus BEGIN/COMMIT) |
| Check A: records, references, IDs | NEW, PASS |
| Check B: SQL structure and supported schema rules | NEW, PASS (provisional snapshot advisories listed) |
| Check C: dates, relationships, consistency | NEW, PASS (advisories listed) |
| Report coverage, findings, limits, one verdict | done |

Nothing was reused from an earlier report (no earlier injection report exists for this SQL).

## 3. Lint result

`hg_injection_lint.py` on SHA `0b6812c5…640d`, universe synthcut, clock 2025-10-01T07:00:00Z, all ten checks (future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape), base lookups used (contacts, slack users, trello, gmail users, linear, confluence). Counts: FAIL 0, CHECK 0, INFO 0. No flags to resolve. Checks A–C below were done by hand regardless.

## 4. Source coverage (record checks)

| Collection | Field(s) checked | Records | Complete |
|---|---|---|---|
| gdrive `data.json` `/drive_files` | id (6 new + 2 parents), name | 53,631 | yes |
| gdrive `/drive_users` | email (4 people) | 25 | yes |
| gdocs `/docs_documents` | document_id | all | yes |
| gsheets `/sheets_spreadsheets` | spreadsheet_id | all | yes |
| gslides `/slides_presentations` (+ nested pages/elements) | presentation_id, page object_id, element object_id | 132 presentations | yes |
| slack `messages/*.json` | id; ts | 610,468 (4,840 files) | yes |
| slack `channels.json`, `users.json` | id | 948 / 218 | yes |
| trello `/cards` `/actions` `/checklists` `/check_items` `/boards` `/lists` `/members` | id, idShort, shortLink, idCard | 803 / 5,252 / 54 / 170 / 5 / 47 / 42 | yes |
| gmail `threads/*.json` `/messages` | id (30 new message ids) | 95,164 (81,404 files) | yes |
| gmail thread ids | numeric part of all 26 new thread ids, text scan of every thread file | 81,404 files | yes (0 hits) |
| gmail `users.json` | 4 mailboxes | all | yes |
| gcal `/calendars`, `/events` | calendar_id; event_id; ical_uid | 38 / 10,395 | yes |
| linear `/issues` `/users` `/teams` `/team_memberships` `/comments` | id, identifier, number; user; team | 3,687 issues; `/comments` empty | yes |
| contacts `/contacts` | contact_id, email, first/last name | all | yes |
| Placeholder tokens `PERSON_9901…9904_EMAIL`, `[IDENTIFIER_99011]` | text scan, all Gmail thread files and all other-service files | all | yes (0 hits: new tokens, no clash) |

## 5. Operation ledger (every statement, execution order)

| # | Line | Table | Op | Record | Key values | Source check | Result |
|---|---|---|---|---|---|---|---|
| 1 | 7 | gdrive.drive_files | INSERT | `f_8d2c47a91e05b3f6d7c418` | Board pre-read - fundraising section (document); parent d_63fffeb4fab5233ed5bb73; owner leonard.hayes@harmonygames.co; created 2025-07-08T18:00:00Z, modified 2025-07-10T16:12:00Z | gdrive/data.json /drive_files id (53,631 complete): no collision; parent found | PASS |
| 2 | 9 | gdrive.drive_files | INSERT | `f_3b9e61c04d7a52e8f1a6c2` | Board pre-read - fundraising section (Oct 14) (document); parent d_63fffeb4fab5233ed5bb73; owner leonard.hayes@harmonygames.co; created 2025-09-26T18:00:00Z, modified 2025-09-26T18:41:00Z | gdrive/data.json /drive_files id (53,631 complete): no collision; parent found | PASS |
| 3 | 11 | gdrive.drive_files | INSERT | `d_5e8a1c3f9b07d2e64a1b93` | Board - Oct 14 2025 (folder); parent d_175c0d7bc72ed244b944cb; owner frederick.stone@harmonygames.co; created 2025-09-26T18:20:00Z, modified 2025-09-26T18:20:00Z | gdrive/data.json /drive_files id (53,631 complete): no collision; parent found | PASS |
| 4 | 13 | gdrive.drive_files | INSERT | `f_c61a0e93b7d24f58a2e917` | README - Oct 14 board materials (document); parent d_5e8a1c3f9b07d2e64a1b93; owner leonard.hayes@harmonygames.co; created 2025-09-26T18:30:00Z, modified 2025-09-26T18:33:00Z | gdrive/data.json /drive_files id (53,631 complete): no collision; parent found | PASS |
| 5 | 15 | gdrive.drive_files | INSERT | `f_a47d0e2c95b18f63e2c0d5` | HG BoD Oct 14 2025 (draft) (presentation); parent d_63fffeb4fab5233ed5bb73; owner leonard.hayes@harmonygames.co; created 2025-09-27T17:00:00Z, modified 2025-09-28T04:40:00Z | gdrive/data.json /drive_files id (53,631 complete): no collision; parent found | PASS |
| 6 | 17 | gdrive.drive_files | INSERT | `f_6e1d93a0c4b72f85d39a0e` | Bridge angels (spreadsheet); parent d_63fffeb4fab5233ed5bb73; owner leonard.hayes@harmonygames.co; created 2025-09-19T17:52:00Z, modified 2025-09-20T03:15:00Z | gdrive/data.json /drive_files id (53,631 complete): no collision; parent found | PASS |
| 7 | 20 | gdocs.docs_documents | INSERT | `f_8d2c47a91e05b3f6d7c418` | Board pre-read - fundraising section; body 432 chars; style runs end 432; drive_file_id matches; 2025-07-08T18:00:00Z/2025-07-10T16:12:00Z | gdocs/data.json /docs_documents document_id complete: no collision | PASS |
| 8 | 22 | gdocs.docs_documents | INSERT | `f_3b9e61c04d7a52e8f1a6c2` | Board pre-read - fundraising section (Oct 14); body 1684 chars; style runs end 1684; drive_file_id matches; 2025-09-26T18:00:00Z/2025-09-26T18:41:00Z | gdocs/data.json /docs_documents document_id complete: no collision | PASS |
| 9 | 24 | gdocs.docs_documents | INSERT | `f_c61a0e93b7d24f58a2e917` | README - Oct 14 board materials; body 285 chars; style runs end 285; drive_file_id matches; 2025-09-26T18:30:00Z/2025-09-26T18:33:00Z | gdocs/data.json /docs_documents document_id complete: no collision | PASS |
| 10 | 27 | gsheets.sheets_spreadsheets | INSERT | `f_6e1d93a0c4b72f85d39a0e` | Bridge angels; drive_file_id matches; 2025-09-19T17:52:00Z/2025-09-20T03:15:00Z | gsheets/data.json spreadsheet_id complete: no collision | PASS |
| 11 | 29 | gsheets.sheets_sheets | INSERT | `f_6e1d93a0c4b72f85d39a0e` | sheet 0 'Angels'; grid 3 rows (Paul Heydon 50000, Anton Bernstein 40000) | child of new spreadsheet | PASS |
| 12 | 32 | gslides.slides_presentations | INSERT | `f_a47d0e2c95b18f63e2c0d5` | HG BoD Oct 14 2025 (draft); 2025-09-27T17:00:00Z/2025-09-28T04:40:00Z | gslides/data.json (132 presentations) complete: no collision | PASS |
| 13 | 34 | gslides.slides_pages | INSERT | `slide_b4c21ca913ab` | slide index 0 | all base page object_ids: no collision | PASS |
| 14 | 36 | gslides.slides_page_elements | INSERT | `el_6825f973029b` | on slide_b4c21ca913ab: TITLE 'Harmony Games Board Meeting' | all base element object_ids: no collision | PASS |
| 15 | 38 | gslides.slides_page_elements | INSERT | `el_cffa02683868` | on slide_b4c21ca913ab: BODY 'October 14, 2025 (draft)' | all base element object_ids: no collision | PASS |
| 16 | 40 | gslides.slides_pages | INSERT | `slide_256dc0474f7c` | slide index 1 | all base page object_ids: no collision | PASS |
| 17 | 42 | gslides.slides_page_elements | INSERT | `el_72151261faca` | on slide_256dc0474f7c: TITLE 'Agenda' | all base element object_ids: no collision | PASS |
| 18 | 44 | gslides.slides_page_elements | INSERT | `el_ca7b40076cd7` | on slide_256dc0474f7c: BODY 'Q3 recap / Zombie Match 3D alpha / Engin' | all base element object_ids: no collision | PASS |
| 19 | 46 | gslides.slides_pages | INSERT | `slide_fd6dbd079420` | slide index 2 | all base page object_ids: no collision | PASS |
| 20 | 48 | gslides.slides_page_elements | INSERT | `el_90fbf6fd9c1b` | on slide_fd6dbd079420: TITLE 'Q3 recap' | all base element object_ids: no collision | PASS |
| 21 | 50 | gslides.slides_page_elements | INSERT | `el_ef5243814e8f` | on slide_fd6dbd079420: BODY 'Domino Delights: publisher search / Zombie' | all base element object_ids: no collision | PASS |
| 22 | 52 | gslides.slides_pages | INSERT | `slide_bb11abfc5fad` | slide index 3 | all base page object_ids: no collision | PASS |
| 23 | 54 | gslides.slides_page_elements | INSERT | `el_69587907b898` | on slide_bb11abfc5fad: TITLE 'Zombie Match 3D' | all base element object_ids: no collision | PASS |
| 24 | 56 | gslides.slides_page_elements | INSERT | `el_6ca8bffe4445` | on slide_bb11abfc5fad: BODY 'Alpha metrics (Robert to fill)' | all base element object_ids: no collision | PASS |
| 25 | 58 | gslides.slides_pages | INSERT | `slide_cb3f0884f833` | slide index 4 | all base page object_ids: no collision | PASS |
| 26 | 60 | gslides.slides_page_elements | INSERT | `el_0c72e8ba6af7` | on slide_cb3f0884f833: TITLE 'Engine' | all base element object_ids: no collision | PASS |
| 27 | 62 | gslides.slides_page_elements | INSERT | `el_1e212bf4628e` | on slide_cb3f0884f833: BODY 'What shipped in Q3 (Arthur to fill)' | all base element object_ids: no collision | PASS |
| 28 | 64 | gslides.slides_pages | INSERT | `slide_a56932e4c738` | slide index 5 | all base page object_ids: no collision | PASS |
| 29 | 66 | gslides.slides_page_elements | INSERT | `el_5da52b8348b0` | on slide_a56932e4c738: TITLE 'Team' | all base element object_ids: no collision | PASS |
| 30 | 68 | gslides.slides_page_elements | INSERT | `el_4f7f04b6e984` | on slide_a56932e4c738: BODY 'Headcount and contractors (Leonard to fi' | all base element object_ids: no collision | PASS |
| 31 | 70 | gslides.slides_pages | INSERT | `slide_c9c7eed73bb9` | slide index 6 | all base page object_ids: no collision | PASS |
| 32 | 72 | gslides.slides_page_elements | INSERT | `el_b45885b83bf9` | on slide_c9c7eed73bb9: TITLE 'Runway' | all base element object_ids: no collision | PASS |
| 33 | 74 | gslides.slides_page_elements | INSERT | `el_ed13f88ca45b` | on slide_c9c7eed73bb9: BODY 'Cash and burn (Leonard to fill)' | all base element object_ids: no collision | PASS |
| 34 | 76 | gslides.slides_pages | INSERT | `slide_329b5dfcb888` | slide index 7 | all base page object_ids: no collision | PASS |
| 35 | 78 | gslides.slides_page_elements | INSERT | `el_09521ac10bd5` | on slide_329b5dfcb888: TITLE 'Options' | all base element object_ids: no collision | PASS |
| 36 | 80 | gslides.slides_page_elements | INSERT | `el_d65f0ea436c8` | on slide_329b5dfcb888: BODY 'Bridge / co-dev / engine deals' | all base element object_ids: no collision | PASS |
| 37 | 82 | gslides.slides_pages | INSERT | `slide_68eecd4f5f2a` | slide index 8 with notes (table columns) | all base page object_ids: no collision | PASS |
| 38 | 84 | gslides.slides_page_elements | INSERT | `el_b87125dbf11e` | on slide_68eecd4f5f2a: TITLE 'Fundraising' | all base element object_ids: no collision | PASS |
| 39 | 86 | gslides.slides_page_elements | INSERT | `el_6548686fe965` | on slide_68eecd4f5f2a: BODY 'Bridge round, pipeline as of Sep 30 / Firm' | all base element object_ids: no collision | PASS |
| 40 | 88 | gslides.slides_pages | INSERT | `slide_98d06d32c8d6` | slide index 9 | all base page object_ids: no collision | PASS |
| 41 | 90 | gslides.slides_page_elements | INSERT | `el_154065e277bc` | on slide_98d06d32c8d6: TITLE 'Asks for the board' | all base element object_ids: no collision | PASS |
| 42 | 92 | gslides.slides_page_elements | INSERT | `el_ee461e258b77` | on slide_98d06d32c8d6: BODY 'Intros, especially games funds and strat' | all base element object_ids: no collision | PASS |
| 43 | 94 | gslides.slides_pages | INSERT | `slide_fcf2cb38bf31` | slide index 10 | all base page object_ids: no collision | PASS |
| 44 | 96 | gslides.slides_page_elements | INSERT | `el_8ee884c1e93b` | on slide_fcf2cb38bf31: TITLE 'Appendix' | all base element object_ids: no collision | PASS |
| 45 | 98 | gslides.slides_page_elements | INSERT | `el_34bc96464df6` | on slide_fcf2cb38bf31: BODY 'Investor FAQ (link)' | all base element object_ids: no collision | PASS |
| 46 | 100 | gslides.slides_pages | INSERT | `slide_5c7db3c42932` | slide index 11 | all base page object_ids: no collision | PASS |
| 47 | 102 | gslides.slides_page_elements | INSERT | `el_ef3226341cb0` | on slide_5c7db3c42932: TITLE 'Thank you' | all base element object_ids: no collision | PASS |
| 48 | 105 | slack.slack_messages | INSERT | `4921f321db5d08f936aac24a6a1d2af8` | channel C07C2866011; user EMPLOYEE_0038_SLACK_ID; ts 1758303600.418207 = created_at 2025-09-19T17:40:00.000000Z | slack messages/*.json id + ts (610,468 records, complete): no collision; user is channel member | PASS |
| 49 | 107 | slack.slack_messages | INSERT | `7fef94264090696760180223fc8265e7` | channel C07C2866011; user EMPLOYEE_0025_SLACK_ID; ts 1759168800.117903 = created_at 2025-09-29T18:00:00.000000Z | slack messages/*.json id + ts (610,468 records, complete): no collision; user is channel member | PASS |
| 50 | 109 | slack.slack_messages | INSERT | `3f2d8f04b29a78808033543c740bb669` | channel C096HFA5Z8W; user EMPLOYEE_0016_SLACK_ID; ts 1759161600.226431 = created_at 2025-09-29T16:00:00.000000Z | slack messages/*.json id + ts (610,468 records, complete): no collision; user is channel member | PASS |
| 51 | 111 | slack.slack_messages | INSERT | `cf10d4f7f88143dc7ab976df27513790` | channel C096HFA5Z8W; user EMPLOYEE_0016_SLACK_ID; ts 1759184040.552871 = created_at 2025-09-29T22:14:00.000000Z; reply to 73c2247f4a31f32d10b3068ecd1d13ac | slack messages/*.json id + ts (610,468 records, complete): no collision; user is channel member | PASS |
| 52 | 113 | slack.slack_messages | UPDATE | `73c2247f4a31f32d10b3068ecd1d13ac` | base parent (C096HFA5Z8W/2025-09.json /159, ts 1757716998.377299) reply_count 0→1, reply_users_count 0→1, latest_reply → reply ts; thread_ts_legacy = own ts (matches base parents' thread_ts) | target found; before values read | PASS |
| 53 | 115 | trello.trello_actions | INSERT | `68c64270d660c977c4696986` | commentCard 2025-09-14T04:20:00Z by PERSON_6094_TRELLO_USER_ID on card 68c5a49e8491a9d7faf869d0 | trello /actions id (5,252) complete: no collision; Leonard = PERSON_6094 | PASS |
| 54 | 117 | trello.trello_cards | UPDATE | `68c5a49e8491a9d7faf869d0` | 'Existing Investor Update' (/cards/801): badges identical except comments 0→1; dateLastActivity 2025-09-13T17:06:40Z→2025-09-14T04:20:00Z (= new comment) | target found; before values read | PASS |
| 55 | 118 | trello.trello_cards | INSERT | `68d8193cf451863621c88a2a` | 'Board Deck - Oct 14' list 640643a3fd8f3ca308d93196; idShort 466; due 2025-10-14T16:00:00Z (plan); dateLastActivity 2025-09-27T17:30:24Z | trello /cards id, idShort, shortLink complete: no collision | PASS |
| 56 | 120 | trello.trello_actions | INSERT | `68d8193c164e823ac3ae735d` | createCard 2025-09-27T17:05:00Z by PERSON_6094_TRELLO_USER_ID on card 68d8193cf451863621c88a2a | trello /actions id (5,252) complete: no collision; Leonard = PERSON_6094 | PASS |
| 57 | 122 | trello.trello_checklists | INSERT | `68d81ae0bac8fd292e6606f8` | 'Sections' on card 68d8193cf451863621c88a2a | trello /checklists id complete: no collision | PASS |
| 58 | 124 | trello.trello_check_items | INSERT | `68d81ae032fe8d64dbd262c7` | 'Fundraising - Fred' incomplete | trello /check_items id complete: no collision | PASS |
| 59 | 126 | trello.trello_check_items | INSERT | `68d81ae087c12c3d08c79ff8` | 'Product - Robert' incomplete | trello /check_items id complete: no collision | PASS |
| 60 | 128 | trello.trello_check_items | INSERT | `68d81ae05ac90637e942026c` | 'Engine - Arthur' incomplete | trello /check_items id complete: no collision | PASS |
| 61 | 130 | trello.trello_check_items | INSERT | `68d81ae07d46d8fe71f4ba98` | 'Runway and options - Leonard' incomplete | trello /check_items id complete: no collision | PASS |
| 62 | 132 | trello.trello_actions | INSERT | `68d81ae0459a87b4efb4b1e3` | addChecklistToCard 2025-09-27T17:12:00Z by PERSON_6094_TRELLO_USER_ID on card 68d8193cf451863621c88a2a | trello /actions id (5,252) complete: no collision; Leonard = PERSON_6094 | PASS |
| 63 | 134 | trello.trello_actions | INSERT | `68d81f30a6c94e2b7d05e1f4` | commentCard 2025-09-27T17:30:24Z by PERSON_6094_TRELLO_USER_ID on card 68d8193cf451863621c88a2a | trello /actions id (5,252) complete: no collision; Leonard = PERSON_6094 | PASS |
| 64 | 137 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844623441920000059` | mailbox frederick.stone@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 65 | 139 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.com>` | mailbox frederick.stone@harmonygames.co; 'board pipeline'; from robert@harmonygames.co; 2025-09-29T18:20:00Z = internal_date = Date header; labels INBOX,IMPORTANT,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 66 | 141 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844623441920000061` | mailbox robert@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 67 | 143 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.com>` | mailbox robert@harmonygames.co; 'board pipeline'; from robert@harmonygames.co; 2025-09-29T18:20:00Z = internal_date = Date header; labels SENT | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 68 | 145 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844623441920000062` | mailbox leonard.hayes@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 69 | 147 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.com>` | mailbox leonard.hayes@harmonygames.co; 'board pipeline'; from robert@harmonygames.co; 2025-09-29T18:20:00Z = internal_date = Date header; labels INBOX,IMPORTANT,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 70 | 149 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844724419788800011` | mailbox frederick.stone@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 71 | 151 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>` | mailbox frederick.stone@harmonygames.co; 'Oct 14 board pre-read - fundraising section'; from leonard.hayes@harmonygames.co; 2025-09-30T21:05:00Z = internal_date = Date header; labels INBOX,IMPORTANT,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 72 | 153 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844724419788800013` | mailbox leonard.hayes@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 73 | 155 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>` | mailbox leonard.hayes@harmonygames.co; 'Oct 14 board pre-read - fundraising section'; from leonard.hayes@harmonygames.co; 2025-09-30T21:05:00Z = internal_date = Date header; labels SENT | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 74 | 157 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844724419788800014` | mailbox robert@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 75 | 159 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>` | mailbox robert@harmonygames.co; 'Oct 14 board pre-read - fundraising section'; from leonard.hayes@harmonygames.co; 2025-09-30T21:05:00Z = internal_date = Date header; labels INBOX,IMPORTANT,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 76 | 161 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844724419788800015` | mailbox arthur.blake@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 77 | 163 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>` | mailbox arthur.blake@harmonygames.co; 'Oct 14 board pre-read - fundraising section'; from leonard.hayes@harmonygames.co; 2025-09-30T21:05:00Z = internal_date = Date header; labels INBOX,IMPORTANT,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 78 | 165 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844162278195200023` | mailbox frederick.stone@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 79 | 167 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CACJhvEE55qdWXuKC3BWlscoxBKrLUWavLQ3cpTJ@mail.gmail.com>` | mailbox frederick.stone@harmonygames.co; 'SAFE amount'; from PERSON_9901_EMAIL; 2025-09-24T16:10:00Z = internal_date = Date header; labels INBOX,IMPORTANT,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 80 | 169 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844162278195200025` | mailbox leonard.hayes@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 81 | 171 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CACJhvEE55qdWXuKC3BWlscoxBKrLUWavLQ3cpTJ@mail.gmail.com>` | mailbox leonard.hayes@harmonygames.co; 'SAFE amount'; from PERSON_9901_EMAIL; 2025-09-24T16:10:00Z = internal_date = Date header; labels INBOX,IMPORTANT,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 82 | 173 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844354293432320031` | mailbox frederick.stone@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 83 | 175 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAiKDPIoVSAFUBccUSRRBTi6dsmJdhof2EzteoIx@mail.gmail.com>` | mailbox frederick.stone@harmonygames.co; 'Completed: Complete with docusign: Harmony Games S'; from SVC_1302_EMAIL; 2025-09-26T19:02:00Z = internal_date = Date header; labels INBOX,CATEGORY_UPDATES | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 84 | 177 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844610859008000037` | mailbox frederick.stone@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 85 | 179 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAP6Gn2LV490e3El5rBDCgCItvhOdc7S6Wpb8nNq@mail.gmail.com>` | mailbox frederick.stone@harmonygames.co; 'SAFE in DocuSign'; from leonard.hayes@harmonygames.co; 2025-09-29T15:00:00Z = internal_date = Date header; labels INBOX,IMPORTANT,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 86 | 181 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844610859008000039` | mailbox leonard.hayes@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 87 | 183 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAP6Gn2LV490e3El5rBDCgCItvhOdc7S6Wpb8nNq@mail.gmail.com>` | mailbox leonard.hayes@harmonygames.co; 'SAFE in DocuSign'; from leonard.hayes@harmonygames.co; 2025-09-29T15:00:00Z = internal_date = Date header; labels SENT | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 88 | 185 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844318935449600041` | mailbox frederick.stone@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 89 | 187 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_lp6f26Gm0Vi7deiv8pmy@mail.gmail.com>` | mailbox frederick.stone@harmonygames.co; 'Harmony Games bridge'; from PERSON_9903_EMAIL; 2025-09-26T09:40:00Z = internal_date = Date header; labels INBOX,IMPORTANT,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 90 | 189 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844318935449600043` | mailbox leonard.hayes@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 91 | 191 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_lp6f26Gm0Vi7deiv8pmy@mail.gmail.com>` | mailbox leonard.hayes@harmonygames.co; 'Harmony Games bridge'; from PERSON_9903_EMAIL; 2025-09-26T09:40:00Z = internal_date = Date header; labels INBOX,IMPORTANT,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 92 | 193 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844347876147200047` | mailbox frederick.stone@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 93 | 195 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>` | mailbox frederick.stone@harmonygames.co; 'Zombie Match 3D access'; from leonard.hayes@harmonygames.co; 2025-09-26T17:20:00Z = internal_date = Date header; labels INBOX,IMPORTANT,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 94 | 197 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844347876147200049` | mailbox leonard.hayes@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 95 | 199 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>` | mailbox leonard.hayes@harmonygames.co; 'Zombie Match 3D access'; from leonard.hayes@harmonygames.co; 2025-09-26T17:20:00Z = internal_date = Date header; labels SENT | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 96 | 201 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844347876147200050` | mailbox robert@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 97 | 203 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>` | mailbox robert@harmonygames.co; 'Zombie Match 3D access'; from leonard.hayes@harmonygames.co; 2025-09-26T17:20:00Z = internal_date = Date header; labels INBOX,IMPORTANT,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 98 | 205 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844347876147200051` | mailbox arthur.blake@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 99 | 207 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>` | mailbox arthur.blake@harmonygames.co; 'Zombie Match 3D access'; from leonard.hayes@harmonygames.co; 2025-09-26T17:20:00Z = internal_date = Date header; labels INBOX,IMPORTANT,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 100 | 209 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844276782694400053` | mailbox frederick.stone@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 101 | 211 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>` | mailbox frederick.stone@harmonygames.co; 'Harmony Games - follow up'; from leonard.hayes@harmonygames.co; 2025-09-25T22:30:00Z = internal_date = Date header; labels INBOX,IMPORTANT,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 102 | 213 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844276782694400055` | mailbox leonard.hayes@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 103 | 215 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>` | mailbox leonard.hayes@harmonygames.co; 'Harmony Games - follow up'; from leonard.hayes@harmonygames.co; 2025-09-25T22:30:00Z = internal_date = Date header; labels SENT | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 104 | 217 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844276782694400056` | mailbox robert@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 105 | 219 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>` | mailbox robert@harmonygames.co; 'Harmony Games - follow up'; from leonard.hayes@harmonygames.co; 2025-09-25T22:30:00Z = internal_date = Date header; labels INBOX,IMPORTANT,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 106 | 221 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844276782694400057` | mailbox arthur.blake@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 107 | 223 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>` | mailbox arthur.blake@harmonygames.co; 'Harmony Games - follow up'; from leonard.hayes@harmonygames.co; 2025-09-25T22:30:00Z = internal_date = Date header; labels INBOX,IMPORTANT,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 108 | 225 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1844276782694400053` | snippet → Ilse reply (latest message) | target inserted earlier in SQL | PASS |
| 109 | 226 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>` | mailbox frederick.stone@harmonygames.co; 'Re: Harmony Games - follow up'; from PERSON_9904_EMAIL; 2025-09-26T15:05:00Z = internal_date = Date header; labels INBOX,IMPORTANT,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 110 | 228 | gmail.gmail_threads | UPDATE | `leonard.hayes@harmonygames.co/1844276782694400055` | snippet → Ilse reply | target inserted earlier in SQL | PASS |
| 111 | 229 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>` | mailbox leonard.hayes@harmonygames.co; 'Re: Harmony Games - follow up'; from PERSON_9904_EMAIL; 2025-09-26T15:05:00Z = internal_date = Date header; labels INBOX,IMPORTANT,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 112 | 231 | gmail.gmail_threads | UPDATE | `robert@harmonygames.co/1844276782694400056` | snippet → Ilse reply | target inserted earlier in SQL | PASS |
| 113 | 232 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>` | mailbox robert@harmonygames.co; 'Re: Harmony Games - follow up'; from PERSON_9904_EMAIL; 2025-09-26T15:05:00Z = internal_date = Date header; labels INBOX,IMPORTANT,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 114 | 234 | gmail.gmail_threads | UPDATE | `arthur.blake@harmonygames.co/1844276782694400057` | snippet → Ilse reply | target inserted earlier in SQL | PASS |
| 115 | 235 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>` | mailbox arthur.blake@harmonygames.co; 'Re: Harmony Games - follow up'; from PERSON_9904_EMAIL; 2025-09-26T15:05:00Z = internal_date = Date header; labels INBOX,IMPORTANT,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 116 | 237 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843992534712320061` | mailbox frederick.stone@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 117 | 239 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-2b67d1aa-cbdd-d816-22c3-d5ace6cf900b@google.com>` | mailbox frederick.stone@harmonygames.co; 'Invitation: Ilse Marrow and Leonard Hayes @ Thu Se'; from leonard.hayes@harmonygames.co; 2025-09-22T19:12:00Z = internal_date = Date header; labels INBOX,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 118 | 241 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1843992534712320063` | mailbox robert@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 119 | 243 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-c82c189b-c33c-a6e0-5e43-def7d943af26@google.com>` | mailbox robert@harmonygames.co; 'Invitation: Ilse Marrow and Leonard Hayes @ Thu Se'; from leonard.hayes@harmonygames.co; 2025-09-22T19:12:00Z = internal_date = Date header; labels INBOX,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 120 | 245 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1843992534712320064` | mailbox arthur.blake@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 121 | 247 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-44faeeb8-a4b0-dae2-c4eb-4d2fda67b29b@google.com>` | mailbox arthur.blake@harmonygames.co; 'Invitation: Ilse Marrow and Leonard Hayes @ Thu Se'; from leonard.hayes@harmonygames.co; 2025-09-22T19:12:00Z = internal_date = Date header; labels INBOX,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 122 | 249 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844724105216000067` | mailbox frederick.stone@harmonygames.co | thread numeric id absent from all 81,404 thread files | PASS |
| 123 | 251 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-297f69c9-ad63-fafd-14c3-70dbf78756f3@google.com>` | mailbox frederick.stone@harmonygames.co; 'Invitation: Board pre-read review - fundraising @ '; from leonard.hayes@harmonygames.co; 2025-09-30T21:00:00Z = internal_date = Date header; labels INBOX,CATEGORY_PERSONAL | gmail threads/*.json /messages id lookup (95,164, complete): no collision | PASS |
| 124 | 254 | gcal.gcal_events | INSERT | `evt_2f86b0d4c9e17a35b64e0d` | cal frederick.stone@harmonygames.co; 'Ilse Marrow and Leonard Hayes'; 2025-09-25T16:00:00Z–2025-09-25T16:45:00Z; created 2025-09-22T19:12:00Z | gcal /events event_id + ical_uid (10,395) complete: no collision; calendar exists | PASS |
| 125 | 256 | gcal.gcal_events | INSERT | `evt_b511d4619c6f46ee63959b` | cal leonard.hayes@harmonygames.co; 'Ilse Marrow and Leonard Hayes'; 2025-09-25T16:00:00Z–2025-09-25T16:45:00Z; created 2025-09-22T19:12:00Z | gcal /events event_id + ical_uid (10,395) complete: no collision; calendar exists | PASS |
| 126 | 258 | gcal.gcal_events | INSERT | `evt_8bd5e929463b854ec0ad13` | cal robert@harmonygames.co; 'Ilse Marrow and Leonard Hayes'; 2025-09-25T16:00:00Z–2025-09-25T16:45:00Z; created 2025-09-22T19:12:00Z | gcal /events event_id + ical_uid (10,395) complete: no collision; calendar exists | PASS |
| 127 | 260 | gcal.gcal_events | INSERT | `evt_ca908a712455521f1f8b43` | cal arthur.blake@harmonygames.co; 'Ilse Marrow and Leonard Hayes'; 2025-09-25T16:00:00Z–2025-09-25T16:45:00Z; created 2025-09-22T19:12:00Z | gcal /events event_id + ical_uid (10,395) complete: no collision; calendar exists | PASS |
| 128 | 262 | gcal.gcal_events | INSERT | `evt_9c41e7a2d05b38f6e1a7c4` | cal frederick.stone@harmonygames.co; 'Board pre-read review - fundraising'; 2025-10-06T16:00:00Z–2025-10-06T16:45:00Z; created 2025-09-30T21:00:00Z | gcal /events event_id + ical_uid (10,395) complete: no collision; calendar exists | PASS |
| 129 | 264 | gcal.gcal_events | INSERT | `evt_75d8a0687ea57b663a40b0` | cal leonard.hayes@harmonygames.co; 'Board pre-read review - fundraising'; 2025-10-06T16:00:00Z–2025-10-06T16:45:00Z; created 2025-09-30T21:00:00Z | gcal /events event_id + ical_uid (10,395) complete: no collision; calendar exists | PASS |
| 130 | 267 | linear.linear_issues | INSERT | `ZOM-567` | ZOM-567 team team_ZOM; creator/assignee usr_cc3e90160f490686 (Arthur Blake); state Todo; 2025-09-30T17:10:00Z/2025-09-30T18:40:00Z | linear /issues id/identifier/number complete: no collision (ZOM max 566) | PASS |
| 131 | 269 | linear.linear_comments | INSERT | `lc_94eb35d962cfbdd31e1bd496` | on ZOM-567 by usr_cc3e90160f490686; 2025-09-30T17:25:00Z | linear /comments is empty in base: no collision; parent issue in SQL | PASS |
| 132 | 271 | linear.linear_comments | INSERT | `lc_b549f3057640a5eb08f7581e` | on ZOM-567 by usr_cc3e90160f490686; 2025-09-30T18:40:00Z | linear /comments is empty in base: no collision; parent issue in SQL | PASS |
| 133 | 274 | contacts.contacts | INSERT | `e3a91c07d5b48f26a0c7e314` | Edith Vane; Partner, Hiro Capital; PERSON_9903_EMAIL | contacts contact_id + email complete: no collision; no existing contact for this email | PASS |
| 134 | 276 | contacts.contacts | INSERT | `b72f0d6e19c3a84e5d21f9a0` | Ilse Marrow; Principal, Brightwater Games Fund; PERSON_9904_EMAIL | contacts contact_id + email complete: no collision; no existing contact for this email | PASS |
| 135 | 278 | contacts.contacts | INSERT | `5d0e8b31f7a29c64e1b0d3a8` | Karthic R; T-Accelerate Capital (PXLite fund); PERSON_3242_EMAIL | contacts contact_id + email complete: no collision; no existing contact for this email | PASS |

BEGIN (line 5) and COMMIT (line 280) wrap all 135 statements in one transaction, so any statement that the live database rejects rolls back the whole script (see Advisory 1).

## 6. Check A — Records, references and IDs: PASS

- **Actors resolve to the people the records name.** Slack `EMPLOYEE_0038_SLACK_ID` = Leonard Hayes, `EMPLOYEE_0025_SLACK_ID` = Arthur Blake, `EMPLOYEE_0016_SLACK_ID` = Robert (slack `users.json` /23, /13, /9). All three are members of `C07C2866011` (#executives) and `C096HFA5Z8W` (#bridge-pitch) (`channels.json` /75, /135). Trello `PERSON_6094_TRELLO_USER_ID` = Leonard Hayes (`/members/2`). Linear `usr_cc3e90160f490686` = arthur.blake@harmonygames.co, a member of `team_ZOM` (`tmem_team_ZOM_usr_cc3e90160f490686`). The Drive, Gmail and Calendar accounts for frederick.stone, leonard.hayes, robert and arthur.blake all exist.
- **Parents and targets exist.** Drive parents `d_63fffeb4fab5233ed5bb73` (Leonard's root, `/drive_files/9030`) and `d_175c0d7bc72ed244b944cb` (Frederick's root, `/drive_files/2060`). The README goes in the new folder, which Leonard can write to. Trello board `640643a3fd8f3ca308d9318e` "Harmony Games", list `640643a3fd8f3ca308d93196` "Doing", card `68c5a49e8491a9d7faf869d0` "Existing Investor Update" (idShort 455, shortLink MfMCBpMm, matching the action data). Slack parent `73c2247f4a31f32d10b3068ecd1d13ac` is in `C096HFA5Z8W/2025-09.json` /159. Linear `team_ZOM`. Every child row (docs/sheets/slides rows, slides pages and elements, checklist and items, Gmail messages, Linear comments) points at a parent created earlier in the same SQL.
- **No collisions.** None of the new keys matches a base key in the complete scans above, and none repeats inside the SQL (the 12 pages and 23 elements are unique). New Linear `ZOM-567`/567 follows the base maximum ZOM-566 (created 2025-09-30T16:26:02Z). Trello idShort 466 skips 456–465 after the board's max of 455; that field has no listed ID contract, so the gap alone is not a finding.
- **ID contracts.** Every Gmail `history_id` is NULL (allowed). No Drive `content_path` is set, so the path contract doesn't apply.
- **Drive readability.** The three Docs have `docs_documents` rows with non-empty `body_text`; the spreadsheet has `sheets_spreadsheets`/`sheets_sheets` rows; the presentation has slides rows; the folder needs no content.
- **One person, one account.** Anton Bernstein and Paul Heydon appear only as names in base investor sheets (`gsheets /sheets_spreadsheets/17` and `/96` grid rows, Website "[REDACTED]") with no email anywhere, so `PERSON_9901_EMAIL`/`PERSON_9902_EMAIL` are their first addresses, not second ones. Edith Vane (`PERSON_9903_EMAIL`) and Ilse Marrow (`PERSON_9904_EMAIL`) appear nowhere in the base. Edith is a new person at an existing firm: the base Hiro Capital people are PERSON_2712 ("Ian"), PERSON_5487 ("Spike", Partner), PERSON_5282 and PERSON_3489, and her email cc's PERSON_5282 as a separate person. The `PERSON_99xx` tokens aren't used anywhere in the base. Karthic (`PERSON_3242_EMAIL`, "karthic R" in base Gmail) has no existing contact row, so the new contact isn't a duplicate. Dentsu recipients PERSON_2581 (小川 浩史), PERSON_5584 (田端 剛治, "Koji-san") and PERSON_5221 (石川 遼, "Ryo-san") match the base Dentsu thread ("[PERSON_NAME_19603], Koji-san, Ryo-san"). `SVC_1302_EMAIL` is the base DocuSign sender.

## 7. Check B — SQL structure and supported schema rules: PASS

- All 129 INSERTs parse with column and value counts equal. The 6 UPDATEs are single-row with key predicates. Quoting of reserved/camelCase identifiers (`"index"`, `"references"`, `"desc"`, `"idBoard"`, `"dateLastActivity"`, …) and E-string escapes are valid.
- All 294 `*_json` values parse as JSON with the base shapes (lint `json_shape` clean). Slack `metadata_json` is `'{}'`.
- No generated columns are set (`text_fts`, `body_text_fts` absent).
- Linear text dates are all `YYYY-MM-DDTHH:MM:SSZ`, and `state_history_json` = `'[]'` is supplied.
- Every NOT NULL column without a default is supplied for every affected table (lint `missing_required` clean, confirmed by hand against the snapshot).
- **Provisional snapshot comparison:** MATCH for every column used except four that are NOT COVERED by the snapshot. Base exports don't carry them either: `gslides.slides_pages.notes` (12 rows), `gslides.slides_page_elements.table_json` and `.ordinal` (23 rows), `linear.linear_comments.sequence` (2 rows). Under Eval 0 and schema/README this is an advisory, not a defect (see Advisory 1).

## 8. Check C — Dates, relationships and consistency: PASS

- **Clock.** The latest event timestamp is 2025-09-30T21:05:00Z (Leonard's email), before 2025-10-01T07:00Z. Only plan fields are later: the Calendar event on 2025-10-06 16:00–16:45Z (created 2025-09-30T21:00Z) and the Trello card due date 2025-10-14T16:00Z.
- **Timestamp agreement.** For all 30 Gmail rows, `date` = `internal_date` = `Date` header, weekdays are right, and `Message-ID`/`Subject` headers match. Each Slack `ts` equals its `created_at`. Trello ObjectId time prefixes match the action dates (e.g. `0x68d8193c` = 2025-09-27T17:05:00Z createCard). Style runs in the Docs are contiguous and end at the body length (432, 1684, 285).
- **Order of events.** The reply 2025-09-29T22:14Z comes after its parent (2025-09-12T22:43Z). Ilse's reply 2025-09-26T15:05Z follows the follow-up 2025-09-25T22:30Z, which follows the meeting 16:00–16:45Z, which follows the invite 2025-09-22T19:12Z (= event created). DocuSign completion (09-26) follows Anton's $25K email (09-24). The angels sheet (09-19 17:52Z) follows the Slack angel update (17:40Z). Leonard's email (21:05Z) follows the Oct 6 invite (21:00Z), which it mentions ("I put Monday's review on your calendar"). Robert's request (09-29) comes before Leonard's "Let's not". The deck (created 09-27 17:00Z) exists before the Trello comment that cites "slide 9" (17:30Z); index 8 is the 9th slide and carries the notes. Linear comments 17:25Z and 18:40Z fall inside the issue's created/updated window, and `updated_at` = last comment.
- **Counts after the UPDATEs.** The Slack parent goes from 0 to 1 reply. The Existing Investor Update card goes from 0 to 1 comment, matching the one new commentCard action. The new card's badges (4 check items, 1 comment) match its children. Gmail thread snippets point at each thread's latest message.
- **Agreement with base records.** Dentsu: the base call was 2025-09-23 and Leonard asked for tester emails that day. The Oct 1 1:30pm LA meeting and Leonard's earlier flight are in the base (`Re: Griffin AGM || Dentsu`), which fits "flying to LA tomorrow morning". T-Accelerate: base Leonard 2025-09-22 "We already sent a testflight invite" fits "TestFlight added Sep 22". Sciplay appears in the parent outreach message.
- **Deliberate conflicts that the records settle** (allowed): Anton $40K (Slack, sheet) is replaced by $25K (later email) plus a signed DocuSign. Leonard's "Invites … are out to all three of you" (09-26) is refined by Arthur's Linear comment (09-30): Play track not added. Robert's "email the board" and Arthur's "only who Leonard emailed" are both overridden by Leonard's later email and the template. These are later corrections or competing claims, not introduced contradictions.
- **No grader-facing text** in any injected record.
- **No Snowflake/Confluence** records touched, and no known base-data conflict is built on.

## 9. Findings

No demonstrated defects. Advisories (none blocks this stage):

1. **Columns not in the schema snapshot (Check B, provisional).** `slides_pages.notes`, `slides_page_elements.table_json`/`ordinal` and `linear_comments.sequence` are in neither the snapshot nor the base exports. If the platform tables lack any of them, that INSERT fails and BEGIN/COMMIT rolls back the whole injection. Smallest fix: confirm the script loads on the platform (Database tab → Run Query, then look for the slide notes and Linear comments), or drop `table_json`, `ordinal` and `sequence` (all NULL/default-like) and move the slide-9 note text somewhere served (slide body or the Trello comment). Whether the Slides tools return speaker notes at all is unverified (the tool catalog doesn't describe it); that visibility question belongs to `/prompt`.
2. **Hiro "session" with no matching record (Check C context).** Edith Vane writes "Thanks again for the session earlier this month". No calendar event, base email or Slack note records a Hiro call in Sep 2025 (base #bridge-pitch 09-08: "Hiro Capital (sent, no update)"). This doesn't contradict a record, but the Trello rule (Keep warm only for firms pitched on "a call or meeting") and the template rule ("A call counts when it's on our calendars") make Hiro's Keep-warm treatment depend on it. `/prompt` should decide whether it has one answer. To make it clear-cut, either add the call to the calendars or change the wording (e.g. "thanks for the deck and the follow-ups").
3. **Attachment claimed but absent (cosmetic).** Leonard's 2025-09-25 email to Ilse says "the deck and the puzzle engine doc are attached", but `attachments_meta_json` is `[]` in all four copies. In the base, emails like this carry attachment metadata. Smallest fix: reword ("I'll send the deck and the puzzle engine doc separately") unless the task needs the files.
4. **Dentsu account emails not on record (context).** Leonard's 09-26 "Thank you for sending your emails" and Arthur's "3 accounts from Ryo-san, came in Fri" refer to a Dentsu message that isn't in the base or the SQL. This isn't a contradiction; add it only if the task should let the agent verify it.

## 10. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | All actors, parents and targets resolve. New keys don't collide in complete scans (§4). No ID-contract breaks. Drive files are readable. No second accounts. |
| B — SQL structure and supported schema rules | PASS | Structure, JSON shapes, NOT NULL columns, generated columns and Linear formats are all valid. Snapshot NOT COVERED for 4 columns is advisory (Advisory 1). Not live-certified. |
| C — Dates, relationships and consistency | PASS | All event times before the clock. Chronology, counts and cross-record facts agree. Deliberate conflicts are settled by later records. Advisories 2–4 are context. |

Outside certification scope (disclosed, not gates): live execution and current database compatibility (including the 4 columns), actual search ranking, Agent visibility and persona access, task difficulty.

## 11. Stage dependencies for reuse

`/prompt` may reuse these static checks only while all of these hold: SQL SHA-256 `0b6812c56fe6876a2c916c8a15138d16c33635b848890d57d4ec058afafc640d`, universe manifest `da2f4cf0…aac1a`, schema snapshot `31dcb2b4…`, id_contracts `fc4711ef…`, Eval 0 `e034019b…`, clock 2025-10-01T07:00Z. `/prompt` still owns discoverability, persona access, slide-notes visibility (Advisory 1) and the Hiro call question (Advisory 2). Any new SQL version needs `/injection` again, then `/prompt`, `/hardness`, `/oe` and `/rubric`.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt. Before that, consider Advisory 1 (confirm the 4 non-snapshot columns load, or drop them) and Advisory 2 (Hiro "session" wording).

Evidence limits: Static review only. The schema snapshot is unverified and doesn't cover slides_pages.notes, slides_page_elements.table_json/ordinal or linear_comments.sequence. No live load, tool-visibility or ranking checks.