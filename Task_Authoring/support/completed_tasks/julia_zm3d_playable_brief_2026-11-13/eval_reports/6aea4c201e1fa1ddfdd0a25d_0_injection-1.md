# /injection report: Eval 0, injection-static-v2

## 1. Scope

| Field | Value |
|---|---|
| Stage / mode | `/injection` (Eval 0), audit, chat review; no task folder or preflight |
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`; reused evidence: unchanged-statement checks from the prior report (section 5, section 11) |
| Actual review time | 2026-11-11 (session date), after the SQL upload at 17:59 workspace time |
| Task date / universe | Oct 1, 2025 (synth-cut), `Universe_SynthCut/`, hg4-synth-sep30cut v16 |
| Clock | 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Reviewed SQL | `Evals/task_inputs/01_Universe_Inject.sql` (uploaded as `01_Universe_Inject (2).sql`), 135,986 bytes, sha256 `c037dd89736e83e0ca136aaa14985b8e2b7524f74a56b423a7480bb3cc421197` (input revision 6) |
| Previous SQL version | sha256 `3a76797fbde16ffa560e3bc54794965464db8f8ef38dc1019f8b11df3ceaeddb` (revision 3), reviewed in prior report sha256 `86ce3e957d58d81442cc1adcc6e4d04bd8f2b3ad0c0b3a0f9494ceb29ce52b7d` |
| Universe manifest | `Evals/references/universes/synthcut/universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` (unchanged from prior review) |
| Reference fingerprints (all unchanged from prior review) | Eval 0 `e034019b…`; WORKFLOW.md `d5702ee2…`; scoring.json `c14873e6…`; schema/injection.json `31dcb2b4…`; id_contracts.json `fc4711ef…`; hg_injection_lint.py `a8226e2a…`; acl.md `29723168…`; roster.json `3f217451…`; ENVIRONMENT.md `b0b45005…`; SEARCH.md `cab83c61…`; EXECUTION.md `4c1875e3…`; known_base_issues.md `79b20289…` |
| Base files read this review | slack `channels.json` (948 records), `users.json`, `messages/*.json` (4,840 files, 610,468 messages; complete id/ts scans), `messages/C08H78VJG80/2025-09.json`, `messages/D05GU6L0XFH/2025-09.json` and `2025-10.json`, `messages/D076Y0SDV18/2025-09.json`, `messages/D05HMBQUC8Z/2025-09.json`, all `messages/*/2025-09.json` (149 files) for colour/recolour/bathroom terms |

Tools: `hg_injection_lint.py` (once, on this SQL), `hg_records.py` (complete exact-field checks), `hg_search.py search-many`, targeted read-only Python reads of single Slack files. No SQL was executed and no base export was modified.

## 2. Inputs and authority issues

- The only input for this stage is the saved SQL. It is substantive: 240 statements (BEGIN, 235 INSERT, 3 UPDATE, COMMIT), 238 affected rows, no DELETE and no upsert/ON CONFLICT.
- The new upload differed from the saved version, so it was saved as revision 6 before review.
- **Diff against the previously reviewed SQL (revision 3):** exactly six lines differ, all edited in place (no line added or removed):
  1. Line 17, `gdocs.docs_documents` `f_faf4d7c167d14a1127dcc3` ("Outgoing folder - what's in it"). "The sound files." became "The .wav exports.", and a new sentence was added: "Tue 30 Sep: Claire sent the three recoloured models again. Opened them, they look right, and they replace Thursday's." The style run end changed 586 → 693.
  2. Line 55, Slack `a5ee6e90…` (Marcus, #zombie-match3d). The text now says the Thursday Unity exports are ASCII because "the setting was wrong that day so youll need to redo them".
  3. Line 59, Slack. Claire's Turkish DM `6642a2d5…` (D05HMBQUC8Z) is **removed**. It is replaced by a new message `8a1b1c6d448eecb7ccc81f796c95d5ce` from Robert in DM D05GU6L0XFH (Julia–Robert) relaying Claire's bathroom-UV redo.
  4. Line 84, `DES-334` Plushie Chick. completed_at and updated_at moved from 07:28:05Z to 14:07:40Z on 2025-09-25.
  5. Line 180, the DES-334 comment `f38cbc5b…`. Its text was extended ("Their message today about that zip is the zombie package, not the chick.") and its time moved 07:27:06Z → 14:06:41Z.
  6. Line 255, the DES-409 comment `31b53426…`. "Need" became "Waiting on".
- The SQL comments are section labels only (`-- gdrive`, `-- gdocs`, … `-- contacts`). None of them is a padding, pass-rate or tool-count comment.

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, base manifest, review version | NEW, done (sections 1–2) |
| Run `hg_injection_lint.py`; resolve every flag | NEW, done (section 4) |
| Inventory every statement and affected record | done (section 5): 6 rows NEW, 232 rows REUSED with provenance |
| Check A: references, collisions, ID contracts, readable Drive, one account per person | PASS (changed records NEW, unchanged REUSED) |
| Check B: SQL structure and supported schema rules; provisional snapshot comparison | PASS (lint NEW on the whole file; advisory ADV-1 unchanged) |
| Check C: dates, relationships, cross-service consistency | PASS (changed records NEW against base, unchanged REUSED) |
| Report coverage, findings, limits and one verdict | done |

## 4. Lint (`hg_injection_lint.py`, injection-lint-v1)

Result for sha256 `c037dd89…1197`, universe `synthcut`, clock `2025-10-01T07:00:00Z`:

- Counts: FAIL 0, CHECK 0, INFO 0.
- Checks run: future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required and json_shape.
- Base lists loaded: contacts, slack users, linear, trello, gmail users and confluence.
- Rows per table: drive_files 5, docs_documents 2, sheets_spreadsheets 2, sheets_sheets 2, slides_presentations 1, slides_pages 4, slides_page_elements 8, slack_messages 6 insert + 1 update, linear_issues 97, linear_comments 96, trello_actions 1, trello_cards 1 update, trello_boards 1 update, gcal_events 4, gmail_threads 3, gmail_messages 3, contacts 1. These match the inventory.

**Resolution:** there were no flags to resolve. A clean lint is not a PASS, so checks A–C were completed below.

## 5. Full operation ledger (execution order)

Rows marked **(NEW)** were checked fresh in this review. Every other row is **REUSED** from the prior report `Evals/task_inputs/reports/0_injection.md` (sha256 `86ce3e957d58d81442cc1adcc6e4d04bd8f2b3ad0c0b3a0f9494ceb29ce52b7d`, SQL `3a76797f…eddb`), ledger item with the same `#`. Reuse is valid because a line-by-line diff shows those statements are byte-identical in both SQL versions, the line numbers are unchanged (only lines 17, 55, 59, 84, 180 and 255 differ, all edited in place), and the universe manifest and every reference fingerprint match (section 1).

The INSERTs are plain (no ON CONFLICT) inside one BEGIN/COMMIT. The three UPDATEs target existing base rows by primary key. No statement depends on an earlier statement except child rows that point at parents inserted earlier in the same script: docs/sheets/slides rows reference drive files from lines 3–11, slides pages and elements reference the presentation, Linear sub-issues and comments reference DES-313..DES-409, and the Slack reply's parent already exists in the base.

| # | SQL line | Table | Op | Record / target | Key values | Base ref (path#pointer) | Result |
|---|---|---|---|---|---|---|---|
| 1 | 3 | gdrive.drive_files | INSERT | `f_8c1d0bca1d1d5fde4c5008` | document; owner frederick.stone@harmonygames.co; parent d_175c0d7bc72ed244b944cb; shared julia.lawson@harmonygames.co, brian.foster@harmonygames.co, robert@harmonygames.co; created 2025-09-30T16:25:41Z; modified 2025-09-30T16:58:19Z; content_path NULL; web_view_link not set | gdrive/data.json /drive_files: id absent (53,631 checked); parent = owner root folder | PASS |
| 2 | 5 | gdrive.drive_files | INSERT | `f_956e60ec7f2f7977d98934` | spreadsheet; owner brian.foster@harmonygames.co; parent d_fc22d5941b2aeb5c03ad32; shared frederick.stone@harmonygames.co, julia.lawson@harmonygames.co, robert@harmonygames.co; created 2025-09-25T06:48:27Z; modified 2025-09-26T17:25:08Z; content_path NULL; web_view_link not set | gdrive/data.json /drive_files: id absent (53,631 checked); parent = owner root folder | PASS |
| 3 | 7 | gdrive.drive_files | INSERT | `f_b2387e31d46d3a7b3fa2a9` | spreadsheet; owner calvin.price@harmonygames.co; parent d_49b9dfa5208d400d9b3937; shared robert@harmonygames.co, julia.lawson@harmonygames.co, brian.foster@harmonygames.co; created 2025-09-12T15:42:11Z; modified 2025-09-26T20:10:36Z; content_path NULL; web_view_link not set | gdrive/data.json /drive_files: id absent (53,631 checked); parent = owner root folder | PASS |
| 4 | 9 | gdrive.drive_files | INSERT | `f_6a2fa8e61b31139ca8e3d4` | presentation; owner julia.lawson@harmonygames.co; parent d_8140f09bf9f1b94cb8ee2d; shared brian.foster@harmonygames.co; created 2025-09-23T19:31:22Z; modified 2025-09-23T19:55:47Z; content_path NULL; web_view_link not set | gdrive/data.json /drive_files: id absent (53,631 checked); parent = owner root folder | PASS |
| 5 | 11 | gdrive.drive_files | INSERT | `f_faf4d7c167d14a1127dcc3` | document; owner brian.foster@harmonygames.co; parent d_fc22d5941b2aeb5c03ad32; shared frederick.stone@harmonygames.co, julia.lawson@harmonygames.co; created 2025-09-25T15:58:14Z; modified 2025-09-30T09:12:26Z; content_path NULL; web_view_link not set | gdrive/data.json /drive_files: id absent (53,631 checked); parent = owner root folder | PASS |
| 6 | 14 | gdocs.docs_documents | INSERT | `f_8c1d0bca1d1d5fde4c5008` | drive_file_id f_8c1d0bca1d1d5fde4c5008; body_text 2179 chars; ACL = drive row | gdocs/data.json /docs_documents: absent (595) | PASS |
| 7 | 16 | gdocs.docs_documents | INSERT | `f_faf4d7c167d14a1127dcc3` | drive_file_id f_faf4d7c167d14a1127dcc3; body_text 693 chars (style run 31–693 matches); adds "Tue 30 Sep: Claire sent the three recoloured models again … they replace Thursday's" and "The .wav exports."; ACL = drive row | gdocs/data.json /docs_documents: absent (595, REUSED); content checked against base C090N54TG79 (29 Sep 23:44Z) and DES-323/336/389, DES-401..405 | PASS (NEW) |
| 8 | 19 | gsheets.sheets_spreadsheets | INSERT | `f_956e60ec7f2f7977d98934` | title ZM3D playable - pack list; ACL = drive row | gsheets/data.json /sheets_spreadsheets: absent (356) | PASS |
| 9 | 21 | gsheets.sheets_sheets | INSERT | `f_956e60ec7f2f7977d98934 sheet 0` | 'Pack', grid 97x5 | new spreadsheet | PASS |
| 10 | 23 | gsheets.sheets_spreadsheets | INSERT | `f_b2387e31d46d3a7b3fa2a9` | title ZM3D sound sources; ACL = drive row | gsheets/data.json /sheets_spreadsheets: absent (356) | PASS |
| 11 | 25 | gsheets.sheets_sheets | INSERT | `f_b2387e31d46d3a7b3fa2a9 sheet 0` | 'Sources', grid 9x4 | new spreadsheet | PASS |
| 12 | 28 | gslides.slides_presentations | INSERT | `f_6a2fa8e61b31139ca8e3d4` | owner julia.lawson; shared brian.foster | gslides/data.json /slides_presentations: absent (132) | PASS |
| 13 | 30 | gslides.slides_pages | INSERT | `f_6a2fa8e61b31139ca8e3d4/slide_f9b479c24b7b` | index 0; notes column (ADV-1) | new presentation | PASS (ADV-1) |
| 14 | 32 | gslides.slides_page_elements | INSERT | `slide_f9b479c24b7b/el_c5c63f51d806` | TITLE: ZM3D playable - reference level; table_json/ordinal (ADV-1) | new presentation | PASS (ADV-1) |
| 15 | 34 | gslides.slides_page_elements | INSERT | `slide_f9b479c24b7b/el_829ffaef8aab` | BODY: Built 23 Sep on the playable levels branch. Brian recorded i; table_json/ordinal (ADV-1) | new presentation | PASS (ADV-1) |
| 16 | 36 | gslides.slides_pages | INSERT | `f_6a2fa8e61b31139ca8e3d4/slide_0e3a07bbbcdd` | index 1; notes column (ADV-1) | new presentation | PASS (ADV-1) |
| 17 | 38 | gslides.slides_page_elements | INSERT | `slide_0e3a07bbbcdd/el_40c443410200` | TITLE: Board; table_json/ordinal (ADV-1) | new presentation | PASS (ADV-1) |
| 18 | 40 | gslides.slides_page_elements | INSERT | `slide_0e3a07bbbcdd/el_bccaace88002` | BODY: Grenade (red, green), Couch, Couch and Pillow, Plushie Bunny; table_json/ordinal (ADV-1) | new presentation | PASS (ADV-1) |
| 19 | 42 | gslides.slides_pages | INSERT | `f_6a2fa8e61b31139ca8e3d4/slide_70fbd773b799` | index 2; notes column (ADV-1) | new presentation | PASS (ADV-1) |
| 20 | 44 | gslides.slides_page_elements | INSERT | `slide_70fbd773b799/el_d80b1de7a1b7` | TITLE: Zombies; table_json/ordinal (ADV-1) | new presentation | PASS (ADV-1) |
| 21 | 46 | gslides.slides_page_elements | INSERT | `slide_70fbd773b799/el_23bcd0034408` | BODY: A mix, nothing fixed yet.; table_json/ordinal (ADV-1) | new presentation | PASS (ADV-1) |
| 22 | 48 | gslides.slides_pages | INSERT | `f_6a2fa8e61b31139ca8e3d4/slide_97402415f9e1` | index 3; notes column (ADV-1) | new presentation | PASS (ADV-1) |
| 23 | 50 | gslides.slides_page_elements | INSERT | `slide_97402415f9e1/el_3ab2af2a0848` | TITLE: Win and lose; table_json/ordinal (ADV-1) | new presentation | PASS (ADV-1) |
| 24 | 52 | gslides.slides_page_elements | INSERT | `slide_97402415f9e1/el_9ea4f88ee342` | BODY: Win: every zombie on screen is eliminated. Lose: the zombies; table_json/ordinal (ADV-1) | new presentation | PASS (ADV-1) |
| 25 | 55 | slack.slack_messages | INSERT | `a5ee6e90923eeab380e6730f674240d2` | ch C0880U9751A; user EMPLOYEE_0002_SLACK_ID; ts 1758906517.912099 = 2025-09-26T17:08:37.912099Z; parent None; text now "…the setting was wrong that day so youll need to redo them…" | id/ts/membership unchanged (REUSED: id and ts absent over 610,468 msgs; author a member); text checked against DES-316..318, 361..369 and base C08H78VJG80 binary-FBX requirement | PASS (NEW) |
| 26 | 56 | slack.slack_messages | INSERT | `1d55b38831d7517fe403e4f2a906a897` | ch C08R8CHB0QL; user EMPLOYEE_0016_SLACK_ID; ts 1758922879.243189 = 2025-09-26T21:41:19.243189Z; parent 088b096edb82a130771a5da3344bcef1 | slack/messages/*.json: id and ts absent (610,468 msgs); author in channels.json members | PASS |
| 27 | 57 | slack.slack_messages | INSERT | `da6776f77288224ec67847a799bbde5a` | ch C090N54TG79; user EMPLOYEE_0016_SLACK_ID; ts 1758823946.262829 = 2025-09-25T18:12:26.262829Z; parent None | slack/messages/*.json: id and ts absent (610,468 msgs); author in channels.json members | PASS |
| 28 | 58 | slack.slack_messages | INSERT | `0b7f656a96c5cc50d1f6924e089bf8ba` | ch C090N54TG79; user EMPLOYEE_0016_SLACK_ID; ts 1759167068.371289 = 2025-09-29T17:31:08.371289Z; parent None | slack/messages/*.json: id and ts absent (610,468 msgs); author in channels.json members | PASS |
| 29 | 59 | slack.slack_messages | INSERT | `8a1b1c6d448eecb7ccc81f796c95d5ce` (replaces the earlier `6642a2d5…` in D05HMBQUC8Z) | ch D05GU6L0XFH; user EMPLOYEE_0016_SLACK_ID (Robert); mentions 0009 (Claire), 0026 (Brian); ts 1759178332.042459 = 2025-09-29T20:38:52.042459Z = created_at; parent None | slack/channels.json#/450 (IM; members EMPLOYEE_0005 Julia, EMPLOYEE_0016 Robert + anonymized); messages/*.json: id and ts absent (610,468 msgs, 4,840 files, scan_complete) | PASS (NEW) |
| 30 | 60 | slack.slack_messages | INSERT | `7e84f1cf59f8e95fef961268fbf37cc1` | ch D05SD5QLG94; user EMPLOYEE_0008_SLACK_ID; ts 1759256494.852159 = 2025-09-30T18:21:34.852159Z; parent None | slack/messages/*.json: id and ts absent (610,468 msgs); author in channels.json members | PASS |
| 31 | 61 | slack.slack_messages | UPDATE | `088b096edb82a130771a5da3344bcef1` | reply_count 1->2; reply_users_count 1->2; latest_reply 1758904103.894649->1758922879.243189; thread_ts_legacy = own ts | slack/messages/C08R8CHB0QL/2025-09.json#/252 (parent), #/254 (existing reply by EMPLOYEE_0009) | PASS |
| 32 | 63 | linear.linear_issues | INSERT | `DES-313` | Playable pack for PlayableX; In Progress; parent None; created 2025-09-25T07:05:12Z; started 2025-09-25T07:21:48Z; completed None; updated 2025-09-25T07:21:48Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 33 | 64 | linear.linear_issues | INSERT | `DES-314` | Couch; Done; parent DES-313; created 2025-09-25T07:06:05Z; started 2025-09-25T07:21:52Z; completed 2025-09-25T07:24:16Z; updated 2025-09-25T07:24:16Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 34 | 65 | linear.linear_issues | INSERT | `DES-315` | Couch and Pillow; Done; parent DES-313; created 2025-09-25T07:06:15Z; started 2025-09-25T07:21:52Z; completed 2025-09-25T07:25:19Z; updated 2025-09-25T07:25:19Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 35 | 66 | linear.linear_issues | INSERT | `DES-316` | Alarm Clock; In Progress; parent DES-313; created 2025-09-25T07:06:23Z; started 2025-09-25T07:21:52Z; completed None; updated 2025-09-25T15:21:19Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 36 | 67 | linear.linear_issues | INSERT | `DES-317` | Record Player; In Progress; parent DES-313; created 2025-09-25T07:06:31Z; started 2025-09-25T07:21:52Z; completed None; updated 2025-09-25T15:22:57Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 37 | 68 | linear.linear_issues | INSERT | `DES-318` | Retro TV; In Progress; parent DES-313; created 2025-09-25T07:06:37Z; started 2025-09-25T07:21:52Z; completed None; updated 2025-09-25T15:24:29Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 38 | 69 | linear.linear_issues | INSERT | `DES-319` | Desk Lamp; In Progress; parent DES-313; created 2025-09-25T07:06:43Z; started 2025-09-25T07:21:52Z; completed None; updated 2025-09-26T09:37:26Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 39 | 70 | linear.linear_issues | INSERT | `DES-320` | Small Lamp; In Progress; parent DES-313; created 2025-09-25T07:06:52Z; started 2025-09-25T07:21:52Z; completed None; updated 2025-09-26T09:39:29Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 40 | 71 | linear.linear_issues | INSERT | `DES-321` | Fly Zapper; In Progress; parent DES-313; created 2025-09-25T07:07:01Z; started 2025-09-25T07:21:52Z; completed None; updated 2025-09-29T12:31:37Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 41 | 72 | linear.linear_issues | INSERT | `DES-322` | Grenade; Done; parent DES-313; created 2025-09-25T07:07:10Z; started 2025-09-25T07:21:52Z; completed 2025-09-25T07:26:02Z; updated 2025-09-25T07:26:02Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 42 | 73 | linear.linear_issues | INSERT | `DES-323` | Chainsaw; In Progress; parent DES-313; created 2025-09-25T07:07:19Z; started 2025-09-25T07:21:52Z; completed None; updated 2025-09-25T08:05:17Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 43 | 74 | linear.linear_issues | INSERT | `DES-324` | Cute Axe; In Progress; parent DES-313; created 2025-09-25T07:07:26Z; started 2025-09-25T07:21:52Z; completed None; updated 2025-09-25T08:09:04Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 44 | 75 | linear.linear_issues | INSERT | `DES-325` | Cute Hammer; In Progress; parent DES-313; created 2025-09-25T07:07:34Z; started 2025-09-25T07:21:52Z; completed None; updated 2025-09-25T08:11:13Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 45 | 76 | linear.linear_issues | INSERT | `DES-326` | Dynamite; In Progress; parent DES-313; created 2025-09-25T07:07:39Z; started 2025-09-25T07:21:55Z; completed None; updated 2025-09-25T08:13:02Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 46 | 77 | linear.linear_issues | INSERT | `DES-327` | Shuriken; In Progress; parent DES-313; created 2025-09-25T07:07:51Z; started 2025-09-25T07:21:55Z; completed None; updated 2025-09-25T08:14:52Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 47 | 78 | linear.linear_issues | INSERT | `DES-328` | Saber; In Progress; parent DES-313; created 2025-09-25T07:07:56Z; started 2025-09-25T07:21:55Z; completed None; updated 2025-09-26T09:40:54Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 48 | 79 | linear.linear_issues | INSERT | `DES-329` | Safe; In Progress; parent DES-313; created 2025-09-25T07:08:07Z; started 2025-09-25T07:21:55Z; completed None; updated 2025-09-26T09:42:45Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 49 | 80 | linear.linear_issues | INSERT | `DES-330` | Flashlight; In Progress; parent DES-313; created 2025-09-25T07:08:14Z; started 2025-09-25T07:21:55Z; completed None; updated 2025-09-29T11:06:27Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 50 | 81 | linear.linear_issues | INSERT | `DES-331` | Fire Extinguisher; In Progress; parent DES-313; created 2025-09-25T07:08:23Z; started 2025-09-25T07:21:55Z; completed None; updated 2025-09-29T12:33:18Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 51 | 82 | linear.linear_issues | INSERT | `DES-332` | Propane Tank; In Progress; parent DES-313; created 2025-09-25T07:08:31Z; started 2025-09-25T07:21:55Z; completed None; updated 2025-09-29T12:35:00Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 52 | 83 | linear.linear_issues | INSERT | `DES-333` | Plushie Bunny; Done; parent DES-313; created 2025-09-25T07:08:36Z; started 2025-09-25T07:21:55Z; completed 2025-09-25T07:27:19Z; updated 2025-09-25T07:27:19Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 53 | 84 | linear.linear_issues | INSERT | `DES-334` | Plushie Chick; Done; parent DES-313; created 2025-09-25T07:08:46Z; started 2025-09-25T07:21:55Z; completed 2025-09-25T14:07:40Z; updated 2025-09-25T14:07:40Z | linear/data.json /issues: id/identifier absent (3,687, REUSED); DES max = 312 | PASS (NEW) |
| 54 | 85 | linear.linear_issues | INSERT | `DES-335` | Bow; In Progress; parent DES-313; created 2025-09-25T07:08:54Z; started 2025-09-25T07:21:55Z; completed None; updated 2025-09-29T11:08:27Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 55 | 86 | linear.linear_issues | INSERT | `DES-336` | Cone; In Progress; parent DES-313; created 2025-09-25T07:09:01Z; started 2025-09-25T07:21:55Z; completed None; updated 2025-09-25T08:05:54Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 56 | 87 | linear.linear_issues | INSERT | `DES-337` | Dice; In Progress; parent DES-313; created 2025-09-25T07:09:07Z; started 2025-09-25T07:21:55Z; completed None; updated 2025-09-25T08:16:44Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 57 | 88 | linear.linear_issues | INSERT | `DES-338` | Gift Box; In Progress; parent DES-313; created 2025-09-25T07:09:17Z; started 2025-09-25T07:21:58Z; completed None; updated 2025-09-25T08:18:12Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 58 | 89 | linear.linear_issues | INSERT | `DES-339` | Plushie Dog; In Progress; parent DES-313; created 2025-09-25T07:09:27Z; started 2025-09-25T07:21:58Z; completed None; updated 2025-09-26T09:44:33Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 59 | 90 | linear.linear_issues | INSERT | `DES-340` | Plushie Whale; In Progress; parent DES-313; created 2025-09-25T07:09:33Z; started 2025-09-25T07:21:58Z; completed None; updated 2025-09-26T09:46:24Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 60 | 91 | linear.linear_issues | INSERT | `DES-341` | Whistle; In Progress; parent DES-313; created 2025-09-25T07:09:41Z; started 2025-09-25T07:21:58Z; completed None; updated 2025-09-26T09:48:20Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 61 | 92 | linear.linear_issues | INSERT | `DES-342` | Wooden Tower; In Progress; parent DES-313; created 2025-09-25T07:09:51Z; started 2025-09-25T07:21:58Z; completed None; updated 2025-09-29T11:09:49Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 62 | 93 | linear.linear_issues | INSERT | `DES-343` | Toy Car; In Progress; parent DES-313; created 2025-09-25T07:09:58Z; started 2025-09-25T07:21:58Z; completed None; updated 2025-09-29T11:12:00Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 63 | 94 | linear.linear_issues | INSERT | `DES-344` | Toy Boat; In Progress; parent DES-313; created 2025-09-25T07:10:07Z; started 2025-09-25T07:21:58Z; completed None; updated 2025-09-29T11:13:47Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 64 | 95 | linear.linear_issues | INSERT | `DES-345` | Toy Airplane; In Progress; parent DES-313; created 2025-09-25T07:10:13Z; started 2025-09-25T07:21:58Z; completed None; updated 2025-09-29T11:15:13Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 65 | 96 | linear.linear_issues | INSERT | `DES-346` | Toy Train; In Progress; parent DES-313; created 2025-09-25T07:10:23Z; started 2025-09-25T07:21:58Z; completed None; updated 2025-09-29T12:36:28Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 66 | 97 | linear.linear_issues | INSERT | `DES-347` | Beach Ball; In Progress; parent DES-313; created 2025-09-25T07:10:28Z; started 2025-09-25T07:21:58Z; completed None; updated 2025-09-29T12:38:37Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 67 | 98 | linear.linear_issues | INSERT | `DES-348` | Bathroom Scale; In Progress; parent DES-313; created 2025-09-25T07:10:38Z; started 2025-09-25T07:21:58Z; completed None; updated 2025-09-26T11:08:21Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 68 | 99 | linear.linear_issues | INSERT | `DES-349` | Bathtub; In Progress; parent DES-313; created 2025-09-25T07:10:47Z; started 2025-09-25T07:21:58Z; completed None; updated 2025-09-26T11:09:37Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 69 | 100 | linear.linear_issues | INSERT | `DES-350` | Cabinet Sink; In Progress; parent DES-313; created 2025-09-25T07:10:55Z; started 2025-09-25T07:22:01Z; completed None; updated 2025-09-26T11:10:38Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 70 | 101 | linear.linear_issues | INSERT | `DES-351` | Flip Flops; In Progress; parent DES-313; created 2025-09-25T07:11:02Z; started 2025-09-25T07:22:01Z; completed None; updated 2025-09-26T11:11:59Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 71 | 102 | linear.linear_issues | INSERT | `DES-352` | Iron; In Progress; parent DES-313; created 2025-09-25T07:11:11Z; started 2025-09-25T07:22:01Z; completed None; updated 2025-09-26T11:13:18Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 72 | 103 | linear.linear_issues | INSERT | `DES-353` | Ironing Board; In Progress; parent DES-313; created 2025-09-25T07:11:16Z; started 2025-09-25T07:22:01Z; completed None; updated 2025-09-26T11:14:21Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 73 | 104 | linear.linear_issues | INSERT | `DES-354` | Plunger; In Progress; parent DES-313; created 2025-09-25T07:11:23Z; started 2025-09-25T07:22:01Z; completed None; updated 2025-09-26T11:16:07Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 74 | 105 | linear.linear_issues | INSERT | `DES-355` | Slippers; In Progress; parent DES-313; created 2025-09-25T07:11:31Z; started 2025-09-25T07:22:01Z; completed None; updated 2025-09-26T11:16:55Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 75 | 106 | linear.linear_issues | INSERT | `DES-356` | Toilet; In Progress; parent DES-313; created 2025-09-25T07:11:41Z; started 2025-09-25T07:22:01Z; completed None; updated 2025-09-26T11:18:24Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 76 | 107 | linear.linear_issues | INSERT | `DES-357` | Toilet Paper; In Progress; parent DES-313; created 2025-09-25T07:11:51Z; started 2025-09-25T07:22:01Z; completed None; updated 2025-09-26T11:19:28Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 77 | 108 | linear.linear_issues | INSERT | `DES-358` | Wash Basin; In Progress; parent DES-313; created 2025-09-25T07:11:58Z; started 2025-09-25T07:22:01Z; completed None; updated 2025-09-26T11:20:42Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 78 | 109 | linear.linear_issues | INSERT | `DES-359` | Washing Machine; In Progress; parent DES-313; created 2025-09-25T07:12:05Z; started 2025-09-25T07:22:01Z; completed None; updated 2025-09-26T11:22:18Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 79 | 110 | linear.linear_issues | INSERT | `DES-360` | Rubber Ducky; In Progress; parent DES-313; created 2025-09-25T07:12:11Z; started 2025-09-25T07:22:01Z; completed None; updated 2025-09-29T12:39:47Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 80 | 111 | linear.linear_issues | INSERT | `DES-361` | Coffee Machine; In Progress; parent DES-313; created 2025-09-25T07:12:22Z; started 2025-09-25T07:22:01Z; completed None; updated 2025-09-25T15:26:21Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 81 | 112 | linear.linear_issues | INSERT | `DES-362` | Cooler; In Progress; parent DES-313; created 2025-09-25T07:12:30Z; started 2025-09-25T07:22:04Z; completed None; updated 2025-09-25T15:27:40Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 82 | 113 | linear.linear_issues | INSERT | `DES-363` | Ice Cream Machine; In Progress; parent DES-313; created 2025-09-25T07:12:37Z; started 2025-09-25T07:22:04Z; completed None; updated 2025-09-25T15:29:42Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 83 | 114 | linear.linear_issues | INSERT | `DES-364` | Kitchen Mixer; In Progress; parent DES-313; created 2025-09-25T07:12:46Z; started 2025-09-25T07:22:04Z; completed None; updated 2025-09-25T15:31:34Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 84 | 115 | linear.linear_issues | INSERT | `DES-365` | Microwave; In Progress; parent DES-313; created 2025-09-25T07:12:55Z; started 2025-09-25T07:22:04Z; completed None; updated 2025-09-25T15:33:12Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 85 | 116 | linear.linear_issues | INSERT | `DES-366` | Oven; In Progress; parent DES-313; created 2025-09-25T07:13:03Z; started 2025-09-25T07:22:04Z; completed None; updated 2025-09-25T15:34:55Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 86 | 117 | linear.linear_issues | INSERT | `DES-367` | Refrigerator; In Progress; parent DES-313; created 2025-09-25T07:13:11Z; started 2025-09-25T07:22:04Z; completed None; updated 2025-09-25T15:36:24Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 87 | 118 | linear.linear_issues | INSERT | `DES-368` | Stove; In Progress; parent DES-313; created 2025-09-25T07:13:17Z; started 2025-09-25T07:22:04Z; completed None; updated 2025-09-25T15:38:15Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 88 | 119 | linear.linear_issues | INSERT | `DES-369` | Toaster; In Progress; parent DES-313; created 2025-09-25T07:13:24Z; started 2025-09-25T07:22:04Z; completed None; updated 2025-09-25T15:39:49Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 89 | 120 | linear.linear_issues | INSERT | `DES-370` | Dutch Oven; In Progress; parent DES-313; created 2025-09-25T07:13:32Z; started 2025-09-25T07:22:04Z; completed None; updated 2025-09-26T09:50:02Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 90 | 121 | linear.linear_issues | INSERT | `DES-371` | Rolling Pin; In Progress; parent DES-313; created 2025-09-25T07:13:43Z; started 2025-09-25T07:22:04Z; completed None; updated 2025-09-26T09:52:06Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 91 | 122 | linear.linear_issues | INSERT | `DES-372` | Round Kettle; In Progress; parent DES-313; created 2025-09-25T07:13:47Z; started 2025-09-25T07:22:04Z; completed None; updated 2025-09-26T09:53:39Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 92 | 123 | linear.linear_issues | INSERT | `DES-373` | Round Pan; In Progress; parent DES-313; created 2025-09-25T07:13:57Z; started 2025-09-25T07:22:04Z; completed None; updated 2025-09-29T11:17:18Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 93 | 124 | linear.linear_issues | INSERT | `DES-374` | Spatula; In Progress; parent DES-313; created 2025-09-25T07:14:04Z; started 2025-09-25T07:22:07Z; completed None; updated 2025-09-29T11:19:24Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 94 | 125 | linear.linear_issues | INSERT | `DES-375` | Whisk; In Progress; parent DES-313; created 2025-09-25T07:14:14Z; started 2025-09-25T07:22:07Z; completed None; updated 2025-09-29T11:21:14Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 95 | 126 | linear.linear_issues | INSERT | `DES-376` | Ladle; In Progress; parent DES-313; created 2025-09-25T07:14:21Z; started 2025-09-25T07:22:07Z; completed None; updated 2025-09-29T11:22:37Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 96 | 127 | linear.linear_issues | INSERT | `DES-377` | Small Kettle; In Progress; parent DES-313; created 2025-09-25T07:14:29Z; started 2025-09-25T07:22:07Z; completed None; updated 2025-09-29T12:42:07Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 97 | 128 | linear.linear_issues | INSERT | `DES-378` | Tall Kettle; In Progress; parent DES-313; created 2025-09-25T07:14:39Z; started 2025-09-25T07:22:07Z; completed None; updated 2025-09-29T12:43:17Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 98 | 129 | linear.linear_issues | INSERT | `DES-379` | Acoustic Guitar; In Progress; parent DES-313; created 2025-09-25T07:14:47Z; started 2025-09-25T07:22:07Z; completed None; updated 2025-09-26T13:04:08Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 99 | 130 | linear.linear_issues | INSERT | `DES-380` | Cello; In Progress; parent DES-313; created 2025-09-25T07:14:53Z; started 2025-09-25T07:22:07Z; completed None; updated 2025-09-26T13:06:04Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 100 | 131 | linear.linear_issues | INSERT | `DES-381` | Cymbals; In Progress; parent DES-313; created 2025-09-25T07:15:00Z; started 2025-09-25T07:22:07Z; completed None; updated 2025-09-26T13:07:26Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 101 | 132 | linear.linear_issues | INSERT | `DES-382` | Electric Guitar; In Progress; parent DES-313; created 2025-09-25T07:15:11Z; started 2025-09-25T07:22:07Z; completed None; updated 2025-09-26T13:08:20Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 102 | 133 | linear.linear_issues | INSERT | `DES-383` | Harp; In Progress; parent DES-313; created 2025-09-25T07:15:17Z; started 2025-09-25T07:22:07Z; completed None; updated 2025-09-26T13:09:43Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 103 | 134 | linear.linear_issues | INSERT | `DES-384` | Tambourine; In Progress; parent DES-313; created 2025-09-25T07:15:24Z; started 2025-09-25T07:22:07Z; completed None; updated 2025-09-26T13:11:33Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 104 | 135 | linear.linear_issues | INSERT | `DES-385` | Trumpet; In Progress; parent DES-313; created 2025-09-25T07:15:33Z; started 2025-09-25T07:22:07Z; completed None; updated 2025-09-26T13:13:02Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 105 | 136 | linear.linear_issues | INSERT | `DES-386` | Xylophone; In Progress; parent DES-313; created 2025-09-25T07:15:41Z; started 2025-09-25T07:22:10Z; completed None; updated 2025-09-26T13:14:23Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 106 | 137 | linear.linear_issues | INSERT | `DES-387` | Music Keyboard; In Progress; parent DES-313; created 2025-09-25T07:15:48Z; started 2025-09-25T07:22:10Z; completed None; updated 2025-09-29T11:24:21Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 107 | 138 | linear.linear_issues | INSERT | `DES-388` | Grand Piano; In Progress; parent DES-313; created 2025-09-25T07:15:56Z; started 2025-09-25T07:22:10Z; completed None; updated 2025-09-29T12:45:34Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 108 | 139 | linear.linear_issues | INSERT | `DES-389` | Cactus Plant; In Progress; parent DES-313; created 2025-09-25T07:16:05Z; started 2025-09-25T07:22:10Z; completed None; updated 2025-09-25T08:06:42Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 109 | 140 | linear.linear_issues | INSERT | `DES-390` | Barrel; In Progress; parent DES-313; created 2025-09-25T07:16:13Z; started 2025-09-25T07:22:10Z; completed None; updated 2025-09-26T09:55:27Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 110 | 141 | linear.linear_issues | INSERT | `DES-391` | Bench; In Progress; parent DES-313; created 2025-09-25T07:16:21Z; started 2025-09-25T07:22:10Z; completed None; updated 2025-09-26T09:57:10Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 111 | 142 | linear.linear_issues | INSERT | `DES-392` | Flower Pot; In Progress; parent DES-313; created 2025-09-25T07:16:29Z; started 2025-09-25T07:22:10Z; completed None; updated 2025-09-26T09:59:26Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 112 | 143 | linear.linear_issues | INSERT | `DES-393` | Garden Shears; In Progress; parent DES-313; created 2025-09-25T07:16:38Z; started 2025-09-25T07:22:10Z; completed None; updated 2025-09-29T11:26:46Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 113 | 144 | linear.linear_issues | INSERT | `DES-394` | Watering Can; In Progress; parent DES-313; created 2025-09-25T07:16:44Z; started 2025-09-25T07:22:10Z; completed None; updated 2025-09-29T11:28:25Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 114 | 145 | linear.linear_issues | INSERT | `DES-395` | Wooden Bucket; In Progress; parent DES-313; created 2025-09-25T07:16:54Z; started 2025-09-25T07:22:10Z; completed None; updated 2025-09-29T11:30:19Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 115 | 146 | linear.linear_issues | INSERT | `DES-396` | Wheelbarrow; In Progress; parent DES-313; created 2025-09-25T07:17:02Z; started 2025-09-25T07:22:10Z; completed None; updated 2025-09-29T12:46:59Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 116 | 147 | linear.linear_issues | INSERT | `DES-397` | Wooden Crate; In Progress; parent DES-313; created 2025-09-25T07:17:11Z; started 2025-09-25T07:22:10Z; completed None; updated 2025-09-29T12:48:46Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 117 | 148 | linear.linear_issues | INSERT | `DES-398` | Cannon; Done; parent DES-313; created 2025-09-25T07:17:17Z; started 2025-09-25T07:22:13Z; completed 2025-09-25T07:29:07Z; updated 2025-09-25T07:29:07Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 118 | 149 | linear.linear_issues | INSERT | `DES-399` | Background; Done; parent DES-313; created 2025-09-25T07:17:23Z; started 2025-09-25T07:22:13Z; completed 2025-09-25T07:29:59Z; updated 2025-09-25T07:29:59Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 119 | 150 | linear.linear_issues | INSERT | `DES-400` | Zombie characters; Done; parent DES-313; created 2025-09-25T07:17:34Z; started 2025-09-25T07:22:13Z; completed 2025-09-29T10:22:00Z; updated 2025-09-29T10:22:00Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 120 | 151 | linear.linear_issues | INSERT | `DES-401` | Matching sound; In Progress; parent DES-313; created 2025-09-25T07:17:41Z; started 2025-09-25T07:22:13Z; completed None; updated 2025-09-26T14:11:37Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 121 | 152 | linear.linear_issues | INSERT | `DES-402` | Rocket sound; In Progress; parent DES-313; created 2025-09-25T07:17:50Z; started 2025-09-25T07:22:13Z; completed None; updated 2025-09-26T14:12:21Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 122 | 153 | linear.linear_issues | INSERT | `DES-403` | Explosion sound; In Progress; parent DES-313; created 2025-09-25T07:17:59Z; started 2025-09-25T07:22:13Z; completed None; updated 2025-09-26T14:13:59Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 123 | 154 | linear.linear_issues | INSERT | `DES-404` | Success sound; In Progress; parent DES-313; created 2025-09-25T07:18:05Z; started 2025-09-25T07:22:13Z; completed None; updated 2025-09-26T14:15:03Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 124 | 155 | linear.linear_issues | INSERT | `DES-405` | Failure sound; In Progress; parent DES-313; created 2025-09-25T07:18:15Z; started 2025-09-25T07:22:13Z; completed None; updated 2025-09-26T14:16:15Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 125 | 156 | linear.linear_issues | INSERT | `DES-406` | Background music; In Progress; parent DES-313; created 2025-09-25T07:18:23Z; started 2025-09-25T07:22:13Z; completed None; updated 2025-09-29T12:50:36Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 126 | 157 | linear.linear_issues | INSERT | `DES-407` | Item visuals; In Progress; parent DES-313; created 2025-09-25T07:18:29Z; started 2025-09-25T07:22:13Z; completed None; updated 2025-09-29T12:52:29Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 127 | 158 | linear.linear_issues | INSERT | `DES-408` | UI elements; In Progress; parent DES-313; created 2025-09-25T07:18:36Z; started 2025-09-25T07:22:13Z; completed None; updated 2025-09-29T12:54:13Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 128 | 159 | linear.linear_issues | INSERT | `DES-409` | Fonts; In Progress; parent DES-313; created 2025-09-25T07:18:47Z; started 2025-09-25T07:22:13Z; completed None; updated 2025-09-29T12:55:40Z | linear/data.json /issues: id/identifier absent (3,687); DES max = 312 | PASS |
| 129 | 160 | linear.linear_comments | INSERT | `a022e31f-afd4-5ab4-81a2-fd1d62c1c2cf` | on DES-314; author usr_fc22d5941b2aeb5c; 2025-09-25T07:23:35Z; "In the first zip, 24 Sep." | linear/data.json /comments: empty base collection | PASS |
| 130 | 161 | linear.linear_comments | INSERT | `c9e602eb-3bf5-533a-9571-506ee278e07b` | on DES-315; author usr_fc22d5941b2aeb5c; 2025-09-25T07:24:29Z; "In the first zip, 24 Sep." | linear/data.json /comments: empty base collection | PASS |
| 131 | 162 | linear.linear_comments | INSERT | `513dd4bc-6bd5-5aaf-b4da-feb984524384` | on DES-316; author usr_fc22d5941b2aeb5c; 2025-09-25T15:21:19Z; "FBX saved out of the project, Thu 25 Sep, so the colours come along. O" | linear/data.json /comments: empty base collection | PASS |
| 132 | 163 | linear.linear_comments | INSERT | `7daa1ebe-84c9-5aba-ba45-22f69fdfd01f` | on DES-317; author usr_fc22d5941b2aeb5c; 2025-09-25T15:22:57Z; "FBX saved out of the project, Thu 25 Sep, so the colours come along. O" | linear/data.json /comments: empty base collection | PASS |
| 133 | 164 | linear.linear_comments | INSERT | `395bc5d2-8e32-537e-9286-a216ddf6b5af` | on DES-318; author usr_fc22d5941b2aeb5c; 2025-09-25T15:24:29Z; "FBX saved out of the project, Thu 25 Sep, so the colours come along. O" | linear/data.json /comments: empty base collection | PASS |
| 134 | 165 | linear.linear_comments | INSERT | `4cf25a71-ccf1-58cf-a70d-da1286b1320e` | on DES-319; author usr_fc22d5941b2aeb5c; 2025-09-26T09:37:26Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 135 | 166 | linear.linear_comments | INSERT | `558aa24b-3da7-5537-aaba-e8f68ffdabcf` | on DES-320; author usr_fc22d5941b2aeb5c; 2025-09-26T09:39:29Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 136 | 167 | linear.linear_comments | INSERT | `33933dbf-208d-5fab-be50-5bc02a0cf709` | on DES-321; author usr_fc22d5941b2aeb5c; 2025-09-29T12:31:37Z; "Not exported yet. Waiting on the FBX from Claire." | linear/data.json /comments: empty base collection | PASS |
| 137 | 168 | linear.linear_comments | INSERT | `c2522fd7-9203-57c6-8bfc-85eee899b758` | on DES-322; author usr_fc22d5941b2aeb5c; 2025-09-25T07:25:08Z; "In the first zip, 24 Sep." | linear/data.json /comments: empty base collection | PASS |
| 138 | 169 | linear.linear_comments | INSERT | `deb96bcb-7d02-5c29-8c41-79fcbd7c1c61` | on DES-323; author usr_fc22d5941b2aeb5c; 2025-09-25T08:05:17Z; "FBX from Claire, Thu 25 Sep, first thing. Opens, looks right. In the o" | linear/data.json /comments: empty base collection | PASS |
| 139 | 170 | linear.linear_comments | INSERT | `9b58d4b0-45c2-572d-8ce5-d64f5e2834ea` | on DES-324; author usr_fc22d5941b2aeb5c; 2025-09-25T08:09:04Z; "FBX from Claire, Thu 25 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 140 | 171 | linear.linear_comments | INSERT | `c015eaec-be3a-5c98-9ea0-aa07f9825bf9` | on DES-325; author usr_fc22d5941b2aeb5c; 2025-09-25T08:11:13Z; "FBX from Claire, Thu 25 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 141 | 172 | linear.linear_comments | INSERT | `158e9cc2-7625-5075-a6f9-ae787f05959f` | on DES-326; author usr_fc22d5941b2aeb5c; 2025-09-25T08:13:02Z; "FBX from Claire, Thu 25 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 142 | 173 | linear.linear_comments | INSERT | `637efd91-10a6-5346-92d0-0816d54f4dec` | on DES-327; author usr_fc22d5941b2aeb5c; 2025-09-25T08:14:52Z; "FBX from Claire, Thu 25 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 143 | 174 | linear.linear_comments | INSERT | `2f4ca97c-f3d4-5bb6-ab48-3bddf1130fea` | on DES-328; author usr_fc22d5941b2aeb5c; 2025-09-26T09:40:54Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 144 | 175 | linear.linear_comments | INSERT | `0a858079-e758-5bf9-a159-c65c627eb62e` | on DES-329; author usr_fc22d5941b2aeb5c; 2025-09-26T09:42:45Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 145 | 176 | linear.linear_comments | INSERT | `b2447303-d424-5811-b7d4-72aed39b7a8b` | on DES-330; author usr_fc22d5941b2aeb5c; 2025-09-29T11:06:27Z; "FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 146 | 177 | linear.linear_comments | INSERT | `80866ff3-da39-5209-aa58-5281e7bb5d2d` | on DES-331; author usr_fc22d5941b2aeb5c; 2025-09-29T12:33:18Z; "Not exported yet. Waiting on the FBX from Claire." | linear/data.json /comments: empty base collection | PASS |
| 147 | 178 | linear.linear_comments | INSERT | `abd87666-157e-592c-95af-cef00f4d9474` | on DES-332; author usr_fc22d5941b2aeb5c; 2025-09-29T12:35:00Z; "Not exported yet. Mine to do, didn't get to it on Friday." | linear/data.json /comments: empty base collection | PASS |
| 148 | 179 | linear.linear_comments | INSERT | `10b6ac18-a627-5255-af32-8410e8ccfcf1` | on DES-333; author usr_fc22d5941b2aeb5c; 2025-09-25T07:26:19Z; "In the first zip, 24 Sep." | linear/data.json /comments: empty base collection | PASS |
| 149 | 180 | linear.linear_comments | INSERT | `f38cbc5b-4f7a-5ffd-b5c6-6f59ad44a44c` | on DES-334; author usr_fc22d5941b2aeb5c; 2025-09-25T14:06:41Z; "Went in the second zip on 24 Sep (the one they called the duck). Their message today about that zip is the zombie package, not the chick." | /comments empty base collection (REUSED); claim checked against base slack/messages/C08H78VJG80/2025-09.json (PlayableX 2025-09-25 13:50:34Z) | PASS (NEW) |
| 150 | 181 | linear.linear_comments | INSERT | `e6b919e4-2499-5439-9234-0578fc2f80c6` | on DES-335; author usr_fc22d5941b2aeb5c; 2025-09-29T11:08:27Z; "FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 151 | 182 | linear.linear_comments | INSERT | `202ce85a-7926-5920-aa57-6cb399779639` | on DES-336; author usr_fc22d5941b2aeb5c; 2025-09-25T08:05:54Z; "FBX from Claire, Thu 25 Sep, first thing. Opens, looks right. In the o" | linear/data.json /comments: empty base collection | PASS |
| 152 | 183 | linear.linear_comments | INSERT | `414102ff-3e97-5412-821b-3a8497cb9f84` | on DES-337; author usr_fc22d5941b2aeb5c; 2025-09-25T08:16:44Z; "FBX from Claire, Thu 25 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 153 | 184 | linear.linear_comments | INSERT | `2df6bd67-01d4-56eb-afab-5513c5062d02` | on DES-338; author usr_fc22d5941b2aeb5c; 2025-09-25T08:18:12Z; "FBX from Claire, Thu 25 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 154 | 185 | linear.linear_comments | INSERT | `f8aed615-9f9d-5735-9fcf-75df00ef0ca6` | on DES-339; author usr_fc22d5941b2aeb5c; 2025-09-26T09:44:33Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 155 | 186 | linear.linear_comments | INSERT | `410f3628-b379-5ba1-8cf6-10f6ae7881e4` | on DES-340; author usr_fc22d5941b2aeb5c; 2025-09-26T09:46:24Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 156 | 187 | linear.linear_comments | INSERT | `a1ba138e-5b26-56c8-a400-c536e1c14e65` | on DES-341; author usr_fc22d5941b2aeb5c; 2025-09-26T09:48:20Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 157 | 188 | linear.linear_comments | INSERT | `501ec8ca-11d1-58e1-ace2-389a18e8e21a` | on DES-342; author usr_fc22d5941b2aeb5c; 2025-09-29T11:09:49Z; "FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 158 | 189 | linear.linear_comments | INSERT | `8c7e0da3-45ca-52ce-a259-48b8deb6adcb` | on DES-343; author usr_fc22d5941b2aeb5c; 2025-09-29T11:12:00Z; "FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 159 | 190 | linear.linear_comments | INSERT | `927ea351-543a-58fb-8a7b-d99499d67a77` | on DES-344; author usr_fc22d5941b2aeb5c; 2025-09-29T11:13:47Z; "FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 160 | 191 | linear.linear_comments | INSERT | `b4f681db-9252-5da0-a93c-39a2d3bf58e8` | on DES-345; author usr_fc22d5941b2aeb5c; 2025-09-29T11:15:13Z; "FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 161 | 192 | linear.linear_comments | INSERT | `6c4e3790-82ba-5ed4-99d8-5fc7dbdadba6` | on DES-346; author usr_fc22d5941b2aeb5c; 2025-09-29T12:36:28Z; "Not exported yet. Mine to do, didn't get to it on Friday." | linear/data.json /comments: empty base collection | PASS |
| 162 | 193 | linear.linear_comments | INSERT | `6bbf45d2-2be3-5f72-b56a-7fdec5b13eec` | on DES-347; author usr_fc22d5941b2aeb5c; 2025-09-29T12:38:37Z; "Not exported yet. Waiting on the FBX from Claire." | linear/data.json /comments: empty base collection | PASS |
| 163 | 194 | linear.linear_comments | INSERT | `f042b03a-1af6-50d5-8ff3-545287bde448` | on DES-348; author usr_fc22d5941b2aeb5c; 2025-09-26T11:08:21Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 164 | 195 | linear.linear_comments | INSERT | `8e881f9f-5d4d-554f-981c-5ac6f0f13e6c` | on DES-349; author usr_fc22d5941b2aeb5c; 2025-09-26T11:09:37Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 165 | 196 | linear.linear_comments | INSERT | `90e4ddbf-4fc8-5734-9240-bef69c616b89` | on DES-350; author usr_fc22d5941b2aeb5c; 2025-09-26T11:10:38Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 166 | 197 | linear.linear_comments | INSERT | `06c58af5-a743-5601-b211-f2daad64e863` | on DES-351; author usr_fc22d5941b2aeb5c; 2025-09-26T11:11:59Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 167 | 198 | linear.linear_comments | INSERT | `a02d9030-aebe-54e2-947f-280e45439268` | on DES-352; author usr_fc22d5941b2aeb5c; 2025-09-26T11:13:18Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 168 | 199 | linear.linear_comments | INSERT | `0cf2f7f2-53c5-5f19-a5a3-31e90081acfc` | on DES-353; author usr_fc22d5941b2aeb5c; 2025-09-26T11:14:21Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 169 | 200 | linear.linear_comments | INSERT | `9d0c26f1-427c-5bec-92fb-f213a3263686` | on DES-354; author usr_fc22d5941b2aeb5c; 2025-09-26T11:16:07Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 170 | 201 | linear.linear_comments | INSERT | `ef72a5ac-66a9-50f2-ac7f-cee26aab5b04` | on DES-355; author usr_fc22d5941b2aeb5c; 2025-09-26T11:16:55Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 171 | 202 | linear.linear_comments | INSERT | `7af82875-da67-5990-afed-d6750b208c1e` | on DES-356; author usr_fc22d5941b2aeb5c; 2025-09-26T11:18:24Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 172 | 203 | linear.linear_comments | INSERT | `568299c3-fb14-5752-a166-f4b5c8189205` | on DES-357; author usr_fc22d5941b2aeb5c; 2025-09-26T11:19:28Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 173 | 204 | linear.linear_comments | INSERT | `14a4804f-c2e9-50c1-8950-b9f79dd65258` | on DES-358; author usr_fc22d5941b2aeb5c; 2025-09-26T11:20:42Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 174 | 205 | linear.linear_comments | INSERT | `c61b88c5-8649-5dd0-aabb-d94dee62c8ab` | on DES-359; author usr_fc22d5941b2aeb5c; 2025-09-26T11:22:18Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 175 | 206 | linear.linear_comments | INSERT | `8b874340-d0a3-5476-9736-90e21eb71421` | on DES-360; author usr_fc22d5941b2aeb5c; 2025-09-29T12:39:47Z; "Not exported yet. Waiting on the FBX from Claire." | linear/data.json /comments: empty base collection | PASS |
| 176 | 207 | linear.linear_comments | INSERT | `16b99933-0d85-5efa-bb8b-db8393d6292e` | on DES-361; author usr_fc22d5941b2aeb5c; 2025-09-25T15:26:21Z; "FBX saved out of the project, Thu 25 Sep, so the colours come along. O" | linear/data.json /comments: empty base collection | PASS |
| 177 | 208 | linear.linear_comments | INSERT | `26028dad-f409-52fb-b4d2-bf3b697a8f43` | on DES-362; author usr_fc22d5941b2aeb5c; 2025-09-25T15:27:40Z; "FBX saved out of the project, Thu 25 Sep, so the colours come along. O" | linear/data.json /comments: empty base collection | PASS |
| 178 | 209 | linear.linear_comments | INSERT | `e080bee1-a56c-53f8-a675-ffb2ddfe6b0f` | on DES-363; author usr_fc22d5941b2aeb5c; 2025-09-25T15:29:42Z; "FBX saved out of the project, Thu 25 Sep, so the colours come along. O" | linear/data.json /comments: empty base collection | PASS |
| 179 | 210 | linear.linear_comments | INSERT | `abce170c-0c57-500e-9755-dc6b5658f0ae` | on DES-364; author usr_fc22d5941b2aeb5c; 2025-09-25T15:31:34Z; "FBX saved out of the project, Thu 25 Sep, so the colours come along. O" | linear/data.json /comments: empty base collection | PASS |
| 180 | 211 | linear.linear_comments | INSERT | `8f260004-7f8e-5a4f-ae73-250994f1fbd5` | on DES-365; author usr_fc22d5941b2aeb5c; 2025-09-25T15:33:12Z; "FBX saved out of the project, Thu 25 Sep, so the colours come along. O" | linear/data.json /comments: empty base collection | PASS |
| 181 | 212 | linear.linear_comments | INSERT | `f04cefe7-88a6-5571-a251-904748384834` | on DES-366; author usr_fc22d5941b2aeb5c; 2025-09-25T15:34:55Z; "FBX saved out of the project, Thu 25 Sep, so the colours come along. O" | linear/data.json /comments: empty base collection | PASS |
| 182 | 213 | linear.linear_comments | INSERT | `5980046f-e4a3-56f0-8f18-f6554227011d` | on DES-367; author usr_fc22d5941b2aeb5c; 2025-09-25T15:36:24Z; "FBX saved out of the project, Thu 25 Sep, so the colours come along. O" | linear/data.json /comments: empty base collection | PASS |
| 183 | 214 | linear.linear_comments | INSERT | `b8d22538-8e43-5240-8a74-40399ea9372d` | on DES-368; author usr_fc22d5941b2aeb5c; 2025-09-25T15:38:15Z; "FBX saved out of the project, Thu 25 Sep, so the colours come along. O" | linear/data.json /comments: empty base collection | PASS |
| 184 | 215 | linear.linear_comments | INSERT | `c549a962-07e3-5707-948b-fafab28ea49d` | on DES-369; author usr_fc22d5941b2aeb5c; 2025-09-25T15:39:49Z; "FBX saved out of the project, Thu 25 Sep, so the colours come along. O" | linear/data.json /comments: empty base collection | PASS |
| 185 | 216 | linear.linear_comments | INSERT | `2d66b43b-70df-599c-89e0-09043ecb3bb3` | on DES-370; author usr_fc22d5941b2aeb5c; 2025-09-26T09:50:02Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 186 | 217 | linear.linear_comments | INSERT | `6bae80f0-7156-5308-91d1-bc649360aeaf` | on DES-371; author usr_fc22d5941b2aeb5c; 2025-09-26T09:52:06Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 187 | 218 | linear.linear_comments | INSERT | `dd6b09c1-124e-5cdc-aa50-9e3bcab984d7` | on DES-372; author usr_fc22d5941b2aeb5c; 2025-09-26T09:53:39Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 188 | 219 | linear.linear_comments | INSERT | `d58e2ef2-eedf-51fa-8610-a5d00922dfe1` | on DES-373; author usr_fc22d5941b2aeb5c; 2025-09-29T11:17:18Z; "FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 189 | 220 | linear.linear_comments | INSERT | `5e211a7f-ccb8-5bbe-81aa-dfb6a3251fc2` | on DES-374; author usr_fc22d5941b2aeb5c; 2025-09-29T11:19:24Z; "FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 190 | 221 | linear.linear_comments | INSERT | `f8b3d54a-3b29-5273-9ecf-38e1feebe9e5` | on DES-375; author usr_fc22d5941b2aeb5c; 2025-09-29T11:21:14Z; "FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 191 | 222 | linear.linear_comments | INSERT | `600e8939-4e8b-5660-9638-c4328b605ff4` | on DES-376; author usr_fc22d5941b2aeb5c; 2025-09-29T11:22:37Z; "FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 192 | 223 | linear.linear_comments | INSERT | `f638e4f9-db25-5147-a967-772c4263d4b6` | on DES-377; author usr_fc22d5941b2aeb5c; 2025-09-29T12:42:07Z; "Not exported yet. Mine to do, didn't get to it on Friday." | linear/data.json /comments: empty base collection | PASS |
| 193 | 224 | linear.linear_comments | INSERT | `1fdef95d-609d-5eba-afb3-1bdc07494156` | on DES-378; author usr_fc22d5941b2aeb5c; 2025-09-29T12:43:17Z; "Not exported yet. Mine to do, didn't get to it on Friday." | linear/data.json /comments: empty base collection | PASS |
| 194 | 225 | linear.linear_comments | INSERT | `0d2b852c-979f-5ed8-a046-899a3e81e476` | on DES-379; author usr_fc22d5941b2aeb5c; 2025-09-26T13:04:08Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other" | linear/data.json /comments: empty base collection | PASS |
| 195 | 226 | linear.linear_comments | INSERT | `fc981716-2526-53b9-ad72-1e753cf07fa6` | on DES-380; author usr_fc22d5941b2aeb5c; 2025-09-26T13:06:04Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other" | linear/data.json /comments: empty base collection | PASS |
| 196 | 227 | linear.linear_comments | INSERT | `2e1503f8-fe6d-5d46-9be3-4f2e70d58bf8` | on DES-381; author usr_fc22d5941b2aeb5c; 2025-09-26T13:07:26Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other" | linear/data.json /comments: empty base collection | PASS |
| 197 | 228 | linear.linear_comments | INSERT | `cbb94883-96c9-5d48-a262-4b3f61968c86` | on DES-382; author usr_fc22d5941b2aeb5c; 2025-09-26T13:08:20Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other" | linear/data.json /comments: empty base collection | PASS |
| 198 | 229 | linear.linear_comments | INSERT | `17174e8a-464a-5509-a94d-1aae20ffe4b5` | on DES-383; author usr_fc22d5941b2aeb5c; 2025-09-26T13:09:43Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other" | linear/data.json /comments: empty base collection | PASS |
| 199 | 230 | linear.linear_comments | INSERT | `74e79473-1e5a-55af-9962-cd4ed0303cdd` | on DES-384; author usr_fc22d5941b2aeb5c; 2025-09-26T13:11:33Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other" | linear/data.json /comments: empty base collection | PASS |
| 200 | 231 | linear.linear_comments | INSERT | `4554db44-2454-5e50-a63e-2e825f187546` | on DES-385; author usr_fc22d5941b2aeb5c; 2025-09-26T13:13:02Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other" | linear/data.json /comments: empty base collection | PASS |
| 201 | 232 | linear.linear_comments | INSERT | `11a633e9-dfe3-5d3e-93ca-b7831510b562` | on DES-386; author usr_fc22d5941b2aeb5c; 2025-09-26T13:14:23Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other" | linear/data.json /comments: empty base collection | PASS |
| 202 | 233 | linear.linear_comments | INSERT | `fc775035-8381-5e0d-9591-626ed573c5b4` | on DES-387; author usr_fc22d5941b2aeb5c; 2025-09-29T11:24:21Z; "FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 203 | 234 | linear.linear_comments | INSERT | `6f786f20-f3fd-59e1-8d4c-4c7dda754a35` | on DES-388; author usr_fc22d5941b2aeb5c; 2025-09-29T12:45:34Z; "Not exported yet. Waiting on the FBX from Claire." | linear/data.json /comments: empty base collection | PASS |
| 204 | 235 | linear.linear_comments | INSERT | `6fcca602-b45d-5d9e-a519-d6a67875a6e9` | on DES-389; author usr_fc22d5941b2aeb5c; 2025-09-25T08:06:42Z; "FBX from Claire, Thu 25 Sep, first thing. Opens, looks right. In the o" | linear/data.json /comments: empty base collection | PASS |
| 205 | 236 | linear.linear_comments | INSERT | `c5008259-08bf-590d-bfaf-5afc88e9c965` | on DES-390; author usr_fc22d5941b2aeb5c; 2025-09-26T09:55:27Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 206 | 237 | linear.linear_comments | INSERT | `a1ee4ac0-3701-524c-aaa1-656761e111d3` | on DES-391; author usr_fc22d5941b2aeb5c; 2025-09-26T09:57:10Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 207 | 238 | linear.linear_comments | INSERT | `420807e5-7eae-5adb-b8f0-99897c93e8fb` | on DES-392; author usr_fc22d5941b2aeb5c; 2025-09-26T09:59:26Z; "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 208 | 239 | linear.linear_comments | INSERT | `ec5c139f-0fa3-5508-997b-325c926ed298` | on DES-393; author usr_fc22d5941b2aeb5c; 2025-09-29T11:26:46Z; "FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 209 | 240 | linear.linear_comments | INSERT | `801740a2-691c-5f53-9bba-90c5a6c3405a` | on DES-394; author usr_fc22d5941b2aeb5c; 2025-09-29T11:28:25Z; "FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 210 | 241 | linear.linear_comments | INSERT | `48c53d03-5e9c-50eb-ad08-85698a838e8c` | on DES-395; author usr_fc22d5941b2aeb5c; 2025-09-29T11:30:19Z; "FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folde" | linear/data.json /comments: empty base collection | PASS |
| 211 | 242 | linear.linear_comments | INSERT | `08f6b5e9-0d0c-585f-965c-cbe0856d60d1` | on DES-396; author usr_fc22d5941b2aeb5c; 2025-09-29T12:46:59Z; "Not exported yet. Waiting on the FBX from Claire." | linear/data.json /comments: empty base collection | PASS |
| 212 | 243 | linear.linear_comments | INSERT | `9e9cd387-beb3-5370-a54f-564699b560d4` | on DES-397; author usr_fc22d5941b2aeb5c; 2025-09-29T12:48:46Z; "Not exported yet. Mine to do, didn't get to it on Friday." | linear/data.json /comments: empty base collection | PASS |
| 213 | 244 | linear.linear_comments | INSERT | `b9331366-208f-54f7-b66f-29595e56b81f` | on DES-398; author usr_fc22d5941b2aeb5c; 2025-09-25T07:28:15Z; "In the first zip, 24 Sep, with its projectile. It is what they call th" | linear/data.json /comments: empty base collection | PASS |
| 214 | 245 | linear.linear_comments | INSERT | `e0bf84cd-6269-541d-9a1d-95cde07ef6d2` | on DES-399; author usr_fc22d5941b2aeb5c; 2025-09-25T07:28:51Z; "In the first zip, 24 Sep. The background of the reference level." | linear/data.json /comments: empty base collection | PASS |
| 215 | 246 | linear.linear_comments | INSERT | `8e46f0c1-1d5f-5a81-94d9-bf044167be06` | on DES-400; author usr_fc22d5941b2aeb5c; 2025-09-29T10:21:17Z; "Unity pack from Marcus, sent Fri 26 Sep. They have been through it and" | linear/data.json /comments: empty base collection | PASS |
| 216 | 247 | linear.linear_comments | INSERT | `507e797c-becd-5c82-af5e-a0d2afc68b47` | on DES-401; author usr_fc22d5941b2aeb5c; 2025-09-26T14:11:37Z; "Exported .wav from the project, Fri 26 Sep. Plays. In the outgoing fol" | linear/data.json /comments: empty base collection | PASS |
| 217 | 248 | linear.linear_comments | INSERT | `df8f83f4-dc50-5c79-8fff-cdb205166aa9` | on DES-402; author usr_fc22d5941b2aeb5c; 2025-09-26T14:12:21Z; "Exported .wav from the project, Fri 26 Sep. Plays. In the outgoing fol" | linear/data.json /comments: empty base collection | PASS |
| 218 | 249 | linear.linear_comments | INSERT | `4f248b0b-3991-59aa-b439-0e4d8742c70d` | on DES-403; author usr_fc22d5941b2aeb5c; 2025-09-26T14:13:59Z; "Exported .wav from the project, Fri 26 Sep. Plays. In the outgoing fol" | linear/data.json /comments: empty base collection | PASS |
| 219 | 250 | linear.linear_comments | INSERT | `4386339b-9cda-5d85-9470-7895c1c10a1c` | on DES-404; author usr_fc22d5941b2aeb5c; 2025-09-26T14:15:03Z; "Exported .wav from the project, Fri 26 Sep. Plays. In the outgoing fol" | linear/data.json /comments: empty base collection | PASS |
| 220 | 251 | linear.linear_comments | INSERT | `1af79ca9-52b2-50cc-9c85-f699e4ee3e54` | on DES-405; author usr_fc22d5941b2aeb5c; 2025-09-26T14:16:15Z; "Exported .wav from the project, Fri 26 Sep. Plays. In the outgoing fol" | linear/data.json /comments: empty base collection | PASS |
| 221 | 252 | linear.linear_comments | INSERT | `9ff62cdd-c2fe-500b-8832-539a7e4e04a7` | on DES-406; author usr_fc22d5941b2aeb5c; 2025-09-29T12:50:36Z; "Not exported. Calvin is still cutting the ad track down to a loop." | linear/data.json /comments: empty base collection | PASS |
| 222 | 253 | linear.linear_comments | INSERT | `c02ca57d-f926-54d1-ba56-b4154f35728a` | on DES-407; author usr_fc22d5941b2aeb5c; 2025-09-29T12:52:29Z; "Not exported yet. The item icons are in Figma, mine to pull as PNG." | linear/data.json /comments: empty base collection | PASS |
| 223 | 254 | linear.linear_comments | INSERT | `e3e92efb-563b-5f29-8bbf-b14b95ce291c` | on DES-408; author usr_fc22d5941b2aeb5c; 2025-09-29T12:54:13Z; "Not exported yet. In Figma, mine to pull as PNG." | linear/data.json /comments: empty base collection | PASS |
| 224 | 255 | linear.linear_comments | INSERT | `31b53426-4274-593c-b1cf-ef944ed22968` | on DES-409; author usr_fc22d5941b2aeb5c; 2025-09-29T12:55:40Z; "Not sent. Waiting on the .ttf files from Martin." | /comments empty base collection (REUSED); Martin = Martin Walsh, EMPLOYEE_0033_SLACK_ID in slack/users.json | PASS (NEW) |
| 225 | 257 | trello.trello_actions | INSERT | `68dc381b75aff34acf5a5424` | commentCard by PERSON_6094_TRELLO_USER_ID (Leonard Hayes) on card 688c4d14c312a27fa2747e40 at 2025-09-30T20:05:47Z | trello/data.json /actions absent (5,252); /members/2; /cards/765; /boards/1; /lists/3 | PASS |
| 226 | 259 | trello.trello_cards | UPDATE | `688c4d14c312a27fa2747e40` | badges.comments 0->1 (other badges unchanged); dateLastActivity 2025-09-13T17:05:46Z->2025-09-30T20:05:47Z | trello/data.json#/cards/765 | PASS |
| 227 | 260 | trello.trello_boards | UPDATE | `640643a3fd8f3ca308d9318e` | dateLastActivity 2025-09-13T17:06:40Z->2025-09-30T20:05:47Z | trello/data.json#/boards/1 | PASS |
| 228 | 262 | gcal.gcal_events | INSERT | `evt_d622b6ab55401d23626674` | calendar frederick.stone@harmonygames.co; 2025-11-03T17:00Z-17:30Z (plan); created/updated 2025-09-30T16:41:17Z; ical_uid shared | gcal/data.json /events absent (10,395); /calendars owner match | PASS |
| 229 | 264 | gcal.gcal_events | INSERT | `evt_421695d009e589ee85296c` | calendar julia.lawson@harmonygames.co; 2025-11-03T17:00Z-17:30Z (plan); created/updated 2025-09-30T16:41:17Z; ical_uid shared | gcal/data.json /events absent (10,395); /calendars owner match | PASS |
| 230 | 266 | gcal.gcal_events | INSERT | `evt_a78612f3eaf04ce8461eb4` | calendar brian.foster@harmonygames.co; 2025-11-03T17:00Z-17:30Z (plan); created/updated 2025-09-30T16:41:17Z; ical_uid shared | gcal/data.json /events absent (10,395); /calendars owner match | PASS |
| 231 | 268 | gcal.gcal_events | INSERT | `evt_1c99b11a66cfd562b13d9c` | calendar robert@harmonygames.co; 2025-11-03T17:00Z-17:30Z (plan); created/updated 2025-09-30T16:41:17Z; ical_uid shared | gcal/data.json /events absent (10,395); /calendars owner match | PASS |
| 232 | 271 | gmail.gmail_threads | INSERT | `julia.lawson@harmonygames.co/1844707828171527310` | history_id NULL | gmail threads/*.json: text search 0 hits (81,404 files) | PASS |
| 233 | 273 | gmail.gmail_messages | INSERT | `julia.lawson@harmonygames.co/<calendar-483bd48e-cfb4-fd3f-b55c-4b417cd0d88a@google.com>` | date 2025-09-30T16:41:17Z; internal_date 1759250477000; to julia/brian/robert | gmail threads/*.json: text search 0 hits (81,404 files) | PASS |
| 234 | 275 | gmail.gmail_threads | INSERT | `brian.foster@harmonygames.co/1844707828171705300` | history_id NULL | gmail threads/*.json: text search 0 hits (81,404 files) | PASS |
| 235 | 277 | gmail.gmail_messages | INSERT | `brian.foster@harmonygames.co/<calendar-c94e8bd4-a0ec-0177-cb05-b68828195e96@google.com>` | date 2025-09-30T16:41:17Z; internal_date 1759250477000; to julia/brian/robert | gmail threads/*.json: text search 0 hits (81,404 files) | PASS |
| 236 | 279 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844707828171004856` | history_id NULL | gmail threads/*.json: text search 0 hits (81,404 files) | PASS |
| 237 | 281 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-4263dbb8-cab6-41a8-95c1-dca6f6f7e53b@google.com>` | date 2025-09-30T16:41:17Z; internal_date 1759250477000; to julia/brian/robert | gmail threads/*.json: text search 0 hits (81,404 files) | PASS |
| 238 | 284 | contacts.contacts | INSERT | `d7d31caf63ee33db2b7ed271` | PlayableX Intake <intake@playablex.ai> | contacts.json: contact_id and email absent (170) | PASS |

## 6. Check A: records, references and IDs

**Changed records (NEW).**
- **New Slack message `8a1b1c6d448eecb7ccc81f796c95d5ce`** (line 59):
  - Channel `D05GU6L0XFH` exists at `slack/channels.json#/450`. It is an IM whose members are EMPLOYEE_0005 (Julia), EMPLOYEE_0016 (Robert), PERSON_6089, U04TWDMDT0V and U05GU6KV231.
  - The author, Robert (EMPLOYEE_0016), is a member.
  - The mentioned users, Claire (EMPLOYEE_0009) and Brian (EMPLOYEE_0026), are mentions only. A DM does not require them to be members.
  - The id and the ts `1759178332.042459` each have 0 matches in a complete scan of all 4,840 message files (610,468 records, `scan_complete: true`).
  - The id appears once in the SQL, so there is no within-SQL duplicate.
- **Removed message `6642a2d5…`.** Nothing in the SQL references it (0 occurrences), so no reference is left dangling.
- **Lines 17, 55, 84, 180 and 255** keep their primary keys, actors and parents. Only text and times changed, so their reference and collision results carry over (REUSED, prior ledger #7, #25, #53, #149, #224).
- **"Martin" in the DES-409 comment** resolves to Martin Walsh (`EMPLOYEE_0033_SLACK_ID`, `slack/users.json`).

**Actors and accounts (REUSED, prior §6; unchanged except for the Slack rows above).** Every actor resolves to one existing account for the person the record names. No account rows are inserted.

| Service | Reference in SQL | Base record | Person |
|---|---|---|---|
| Slack | EMPLOYEE_0002 / 0008 / 0016 / 0026 (authors); 0026, 0009 (mentions) | `slack/users.json` | Marcus Bennett, Frederick Stone, Robert, Brian Foster; Claire Morgan (mention) |
| Linear | creator/assignee/author `usr_fc22d5941b2aeb5c` | `linear/data.json#/users/40` (brian.foster@harmonygames.co), DES membership | Brian Foster |
| Linear | team `team_DES` | `#/teams/1` | n/a |
| Drive | owners frederick.stone, brian.foster (x2), calvin.price, julia.lawson; sharees robert, julia.lawson, brian.foster, frederick.stone | `gdrive/data.json /drive_users` | roster people |
| Trello | `PERSON_6094_TRELLO_USER_ID` | `trello/data.json#/members/2` | Leonard Hayes |
| GCal / Gmail | calendars and mailboxes of frederick.stone, julia.lawson, brian.foster, robert | `gcal /calendars`, `gmail/users.json` | n/a |
| Contacts | new `PlayableX Intake <intake@playablex.ai>` | id and email absent (170) | New external role mailbox, not a second account for an existing person |

**Slack channel membership of injected authors.**

| Message | Channel | Author | Member? | Verification |
|---|---|---|---|---|
| a5ee6e90… | C0880U9751A #zombie-match3d | Marcus (0002) | yes; mentions Brian and Claire, both members | REUSED |
| 1d55b388… (thread reply) | C08R8CHB0QL #zombie-art | Robert (0016) | yes | REUSED |
| da6776f7…, 0b7f656a… | C090N54TG79 #zombie-design | Robert (0016) | yes; mention Brian, a member | REUSED |
| 8a1b1c6d… | D05GU6L0XFH (IM, Julia + Robert) | Robert (0016) | yes | NEW |
| 7e84f1cf… | D05SD5QLG94 (IM, Julia + Frederick) | Frederick (0008) | yes | REUSED |

**Parents, targets, collisions, ID contracts, readable Drive files and ACL fields (REUSED, prior §6).** These are unchanged statements with unchanged base and fingerprints:
- **Parents and targets.** The Slack thread parent `088b096e…` and its UPDATE target exist. The Drive parents are the owners' root folders. The Trello board, card and list exist. Every docs/sheets/slides and Linear child points at a row inserted earlier in the script.
- **Collisions.** Complete scans found 0 collisions for:
  - the 5 other Slack ids and ts values
  - DES-313..409 (base DES max 312) and the 96 comment UUIDs (empty base collection)
  - the 5 Drive ids and the docs/sheets/slides ids
  - the Trello action and the 4 GCal events
  - the 3 Gmail threads and 3 Message-IDs (text scan over 81,404 files)
  - the contact
- **ID contracts.** Gmail `history_id` is NULL. Drive `content_path` is NULL, so the path contract does not apply.
- **Readable Drive files.** Both Docs have non-empty docs_documents bodies; for this file it is now 693 chars. The Sheets and Slides have their service rows.
- **ACLs and missing web_view_link.** The ACL fields are consistent across rows, and the missing web_view_link matches the base.

**Check A result: PASS.**

## 7. Check B: SQL structure and supported schema rules

- **Structure (NEW, whole file via lint).** All 240 statements parse with no unparsed text, and column/value counts match. There is one BEGIN/COMMIT with no ON CONFLICT, casts or `now()`.
- **Changed lines (NEW).**
  - Escaping: apostrophes are doubled (`what''s`, `Thursday''s`, `Friday''s`, `won''t`, `I''ll`). Line 17 stays an `E'…'` string using only `\n`.
  - The decoded doc body is 693 characters, which equals the NORMAL_TEXT style-run end (31–693). The style_runs_json parses.
  - The new Slack row keeps `metadata_json = '{}'` and `reactions_json`/`files_json`/`attachments_json = '[]'`. It does not set `text_fts`.
  - DES-334's dates use `YYYY-MM-DDTHH:MM:SSZ`, and `state_history_json = '[]'` is present (lint text_time_format and missing_required clean).
- **Unchanged structure (REUSED, prior §7).** This covers quoting of the Trello camelCase columns, JSON shapes and the provisional snapshot MATCH for every table except the ADV-1 columns.
- **ADV-1 (advisory, unchanged).** `linear_issues.uuid`, `linear_comments.sequence`, `slides_pages.notes`, and `slides_page_elements.table_json`/`ordinal` are not in the unverified schema snapshot or the base export shape. A snapshot mismatch alone is not a defect. However, if the live database lacked any of them, the single transaction would abort. Dropping those column/value pairs (all NULL or trivial) removes that risk.

**Check B result: PASS** (ADV-1 recorded as a compatibility limit).

## 8. Check C: dates, relationships and consistency

**Clock (NEW for changed rows; lint future_date clean on the whole file).**
- New Slack ts 1759178332.042459 equals 2025-09-29T20:38:52.042459Z, which equals `created_at`.
- DES-334: created 07:08:46Z < started 07:21:55Z < comment 14:06:41Z < completed = updated 14:07:40Z (all 2025-09-25). updated_at equals completed_at, as on the other Done tickets.
- Every event is before 2025-10-01T07:00Z. The latest event is still the Trello activity at 2025-09-30T20:05:47Z. Only the GCal plan times (2025-11-03) are later.

**Changed facts against the base (NEW).**

| Changed record | Claim | Base / SQL evidence | Result |
|---|---|---|---|
| DES-334 comment (line 180) | "Went in the second zip on 24 Sep (the one they called the duck). Their message today about that zip is the zombie package, not the chick." | `slack/messages/C08H78VJG80/2025-09.json`, PlayableX channel: <br>• 2025-09-24 14:18Z: PlayableX ask for "the duck asset" and the zombies as a Unity package. <br>• 15:58Z: Brian sends `Plushie-and-zombies.zip` (the second zip). <br>• **2025-09-25 13:50:34Z:** PlayableX say the zombie package "wasn't exported correctly". <br>The comment at 14:06:41Z is 16 minutes later, the same day, and correctly ties that message to the zombies (DES-400, later resent 26 Sep), not the chick. Brian (EMPLOYEE_0026) is a channel member. | Consistent |
| DES-334 issue (line 84) | Done, completed 14:07:40Z | It matches the pack-list line "zip 24 Sep (second)" and DES-313's rule that a ticket closes when PlayableX have the file. The close moving to just after the comment keeps comment < completed. | Consistent |
| Outgoing doc (line 17) | "Tue 30 Sep: Claire sent the three recoloured models again … they replace Thursday's." | Base `slack/messages/C090N54TG79/2025-09.json` (#zombie-design), **2025-09-29 23:44Z, Robert:** "Got new colored version of cactus, chainsaw and cones". These are exactly the three items whose comments say "FBX from Claire, Thu 25 Sep, first thing": DES-389 Cactus Plant, DES-323 Chainsaw and DES-336 Cone. The doc is modified 2025-09-30T09:12:26Z, after Robert's post. The hand-off doc (line 15) says changed art (new colour versions) "goes again". The pointer therefore resolves, and nothing contradicts it. | Consistent |
| Outgoing doc (line 17) | "Fri 26 Sep: … The .wav exports." | DES-401..405: "Exported .wav from the project, Fri 26 Sep". | Consistent |
| Marcus message (line 55) | The Thursday Unity exports are ASCII; "the setting was wrong that day so youll need to redo them" | They match DES-316..318 and 361..369 ("FBX saved out of the project, Thu 25 Sep"). PlayableX's format list in base C08H78VJG80 asks for Binary, not ASCII. Posted 2025-09-26 17:08Z, after those notes, as a later correction. | Consistent |
| Robert DM (line 59) | "<@Claire> is redoing the UVs on the bathroom objects from scratch… the bathroom files she gave <@Brian> on Friday are the old version too" | DES-348..359 (the bathroom items) say "FBX from Claire, Fri 26 Sep". Posted 2025-09-29 20:38Z, after those notes (2025-09-26 11:08–11:22Z), as a later update. It sits in the active English Julia–Robert DM just before Robert's base messages at 20:55Z and 21:21Z. It contradicts no base record. Claire's base #zombie-art activity on 29–30 Sep is about other objects. | Consistent |
| DES-409 comment (line 255) | "Waiting on the .ttf files from Martin." | Text-only change; Martin Walsh exists. | Consistent |

Removing Claire's Turkish DM leaves no orphaned reference or count. That DM was not a thread parent, and no UPDATE depended on it.

**Unchanged relationships (REUSED, prior §8).** These statements are unchanged, so their results carry over:
- **Slack thread.** The thread UPDATE counts are reply_count 1→2, reply_users_count 1→2 and latest_reply set to the new ts (complete thread_ts scan).
- **Linear.** DES-313 has 96 sub-issues, each with one comment. For the 88 In Progress tickets, updated_at equals the comment time.
- **Pack list.** The 8 Done tickets equal the pack-list "Went out" lines.
- **Note dates and instruments.** Note weekdays match the UTC+3 times, and the instruments zip (DES-379..386) matches "those eight".
- **Base storyline.** The PlayableX storyline matches base Slack: the start moved Sep 29 → Oct 6 → Nov 3, and the kickoff hold went in on 30 Sep.
- **Trello, GCal and Gmail.** The Trello badges are consistent, and so are the GCal copies with Gmail invite recipients.

**Grader-facing text.** None. The changed texts are persona-voiced notes to colleagues, and lint grader_language is clean.

**Known base issues.** SC-1..SC-3 concern Snowflake and Confluence. The SQL touches neither service, and no changed record builds on them.

**Check C result: PASS.**

## 9. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | The new Slack message's channel and author resolve, and its id and ts have 0 collisions (complete scan). The removed message leaves no dangling reference. Unchanged rows' checks are REUSED with matching fingerprints. |
| B — SQL structure and supported schema rules | PASS | The lint is clean on all 240 statements, and the changed lines are escaped correctly. The doc style run equals body length 693. ADV-1 (snapshot-unlisted columns) is advisory only. |
| C — Dates, relationships and consistency | PASS | DES-334's chronology is valid. Each changed claim is supported by base records: PlayableX 25 Sep 13:50Z, Robert 29 Sep 23:44Z (cactus, chainsaw, cones) and DES-348..359 / 401..405 / 316..369. No event is after the clock. |

## 10. Findings and fixes

- **Blocking defects:** none.
- **ADV-1 (advisory, Check B, unchanged from the prior review).** Optionally remove `uuid` from the 97 `linear_issues` INSERTs, `sequence` from the 96 `linear_comments` INSERTs, `notes` from the 4 `slides_pages` INSERTs, and `table_json`/`ordinal` from the 8 `slides_page_elements` INSERTs.
- **Note for /prompt (not an injection defect).** The doc's "three recoloured models" is resolved only by Robert's base #zombie-design post of 29 Sep (C090N54TG79), and the bathroom-UV update now reaches Julia through Robert's DM (D05GU6L0XFH). Both channels include Julia (EMPLOYEE_0005). /prompt owns discoverability and the persona's visibility of these records.

## 11. Source / check dependencies (stage-evidence-v1)

These checks depend on:
- SQL sha256 `c037dd89…1197`
- the synthcut universe manifest `da2f4cf0…`
- the reference hashes in section 1
- the clock 2025-10-01T07:00Z

**Reused evidence.** This covers ledger items #1–#238 except #7, #25, #29, #53, #149 and #224, plus the prior §6–§8 checks on unchanged statements. Source: `Evals/task_inputs/reports/0_injection.md`, sha256 `86ce3e957d58d81442cc1adcc6e4d04bd8f2b3ad0c0b3a0f9494ceb29ce52b7d`. Verified unchanged:
- statement bytes (diff of revision 3 vs revision 6)
- universe manifest
- all reference fingerprints
- clock

**New evidence.**
- the lint on the whole file
- Slack channel `#/450`
- the complete id/ts scans (610,468 records)
- PlayableX channel 2025-09
- the Julia–Robert DM 2025-09/10
- #zombie-design 2025-09
- the colour/recolour/bathroom scan of all 149 Sep 2025 Slack files

/prompt may reuse checks A–C only while all of these still match.

Manifest entry: `input_manifest.json` → `stages.injection`, with:
- `review_version: injection-static-v2`
- `evidence_contract: stage-evidence-v1`
- `reused_evidence` listing the prior report hash and ledger items

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort (not separately reported by runtime)

Next action: Proceed to /prompt (the SQL changed, so /prompt, /hardness, /oe and /rubric results based on the earlier SQL need rerunning). Optionally drop the ADV-1 columns.

Evidence limits: Static review only. There was no live execution, deployment or live database compatibility check. The schema snapshot is unverified, so the ADV-1 columns are unconfirmed. Uniqueness is scoped to the local synth-cut base plus this SQL. Unchanged-statement checks are reused from the prior report with verified matching dependencies. Agent visibility and task difficulty belong to /prompt and /hardness.
