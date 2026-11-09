# Injection data-integrity review: PASS

**Review version:** `injection-static-v2` · **Evidence contract:** `stage-evidence-v1`

## 1. Scope

| Item | Value |
|---|---|
| Review | Chat review of attempt 6aed99b31c89eba1436ef322, `/injection`, audit mode |
| Review time | 2026-11-06T17:27Z |
| Universe / clock | Oct 1, 2025 (synth-cut), `Universe_SynthCut`, hg4-synth-sep30cut v16; clock 2025-10-01 00:00 PT (07:00 UTC) |
| Universe manifest | `Evals/references/universes/synthcut/universe_manifest.json`, SHA-256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Reviewed input | `Evals/task_inputs/01_Universe_Inject.sql` (injection input revision 3, from the attachment `01_Universe_Inject.sql`), 157,581 bytes, SHA-256 `e6aa859bea5fec91dff09ad2d02fe072d46cc6cef964eb12c389c1f5d2212d73` |
| References | Eval 0 `e034019b…3eff`; WORKFLOW `ee4cd8e1…fcd5d`; schema snapshot `injection.json` `31dcb2b4…5151` (unverified); `id_contracts.json` `fc4711ef…4682`; lint `hg_injection_lint.py` `a8226e2a…448b` (injection-lint-v1) |
| Assignment (context only) | Frederick Stone, Co-founder · Executive · Finance · Analysis and synthesis · long-horizon · medium |

## 2. Input and authority issues

- None blocking. The SQL was saved before review. No SQL was run and no base export was changed.
- **Manifest note:** the stage writer only saves the report. Under this portal's integrity rules nothing else may be written into `reports/`, so the `input_manifest.json` entry is recorded here instead: `{"injection": {"review_version": "injection-static-v2", "evidence_contract": "stage-evidence-v1", "input": "Evals/task_inputs/01_Universe_Inject.sql", "sha256": "e6aa859bea5fec91dff09ad2d02fe072d46cc6cef964eb12c389c1f5d2212d73", "universe_manifest_sha256": "da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a", "reused_evidence": []}}`.
- Every check below is NEW. No evidence was reused from an earlier report.

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, manifest, review version | DONE (NEW) |
| Run lint; resolve every flag | DONE: 0 FAIL / 0 CHECK / 0 INFO (NEW) |
| Inventory every statement and affected record | DONE: 178 statements = BEGIN + 144 INSERT + 32 UPDATE + COMMIT; 176 row effects, all in the ledger (NEW) |
| Check A: references and collisions | PASS (NEW) |
| Check B: structure and schema | PASS, with 4 provisional snapshot MISMATCHes (advisory) (NEW) |
| Check C: dates, relationships, consistency | PASS, with advisories (NEW) |

## 4. Lint flags and resolution

`hg_injection_lint.py` (injection-lint-v1, synthcut clock 2025-10-01T07:00:00Z) ran checks future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required and json_shape. **Result: 0 FAIL, 0 CHECK, 0 INFO, nothing unparsed.** There were no flags to resolve. Checks A–C below were still done in full.

## 5. Check results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | **PASS** | See 5A. All referenced actors, parents, channels, threads, boards, lists, issues and calendars resolve. All new keys were checked against complete collections and none collide. Every author id resolves to the person named. No second accounts. Every Drive file is readable (Docs have body_text; the Sheet has a grid; the Slides deck has pages and elements). |
| B — SQL structure and supported schema rules | **PASS** | See 5B. The parse is clean. Column/value counts match. Camel-case Trello columns are correctly double-quoted. No generated columns are set. Linear text times use `YYYY-MM-DDTHH:MM:SSZ`. NOT NULL columns are filled. JSON shapes are valid. Four columns are not in the unverified snapshot: a provisional MISMATCH, which is advisory under the schema README. |
| C — Dates, relationships and consistency | **PASS** | See 5C. Every event timestamp is at or before the clock. Only the Oct 6 meeting start/end (plan fields) are later. Reply chains, labels, thread counters and snippets agree. Drive, Docs, Sheets and Slides metadata agree. Base references made in the injected text resolve. No grader-facing text. No injected record depends on a listed SC-* conflict. |

### 5A. Records, references and IDs (NEW)

Existing references, all resolved with `hg_records.py` (scan_complete true):
- **Slack users** (`users.json`, 218 checked): EMPLOYEE_0008 = Frederick Stone, 0016 = Robert, 0025 = Arthur Blake, 0038 = Leonard Hayes.
- **Slack channels** (`channels.json`, 948 checked): each author is a member of the channel they post in.
  - D05S58U4SAK (DM; members include 0008 and 0038)
  - C096HFA5Z8W #bridge-pitch (includes 0038)
  - C07C2866011 #executives (includes 0016 and 0025)
  - C069FF9Q57S #analytics (includes 0025)
- **Slack thread parents:** each one exists in the channel named.
  - 0f6848b3… (ts 1758147530.732569)
  - aaec7171… (ts 1758736960.824899)
  - 330b95fd… (ts 1757345405.134829)
- **Trello:**
  - Board 66da196a… "UA/BD"
  - List 670015c2… "BD Follow Up" (idBoard = that board)
  - Members 4b4a68fc… = Frederick Stone and PERSON_6094_TRELLO_USER_ID = Leonard Hayes
- **Linear:** issue `ENG-2362` exists (id = identifier, assignee usr_cc3e90160f490686). Author usr_cc3e90160f490686 = arthur.blake@harmonygames.co.
- **Drive parents:**
  - d_175c0d7bc72ed244b944cb = Frederick's root folder
  - d_63fffeb4fab5233ed5bb73 = Leonard's root folder
  - The injected folder d_6fc54be6… is inserted before its children.
- **Gmail mailboxes:** frederick.stone@, leonard.hayes@, robert@ and arthur.blake@harmonygames.co are all base Gmail users.
- **Calendars:** all four `calendar_id`s exist (`/calendars`, 38 checked).
- **External lawyer:** PERSON_2694_EMAIL / PERSON_2694_NAME is the base ESG Law partner (base threads 00015129, blake@…_1841636074234083863). This is the existing identity, not a new account.

New-key collision coverage. Every scan was complete, with zero matches:

| Collection | New keys | Records scanned |
|---|---|---|
| gdrive `/drive_files` id | 13 | 53,631 |
| gdocs `/docs_documents` document_id | 10 | 595 |
| gsheets `/sheets_spreadsheets` spreadsheet_id | 1 | 356 |
| gslides `/slides_presentations` presentation_id | 1 | 132 |
| slack `messages/*.json` id | 6 | 610,468 (4,840 files) |
| trello `/cards` id | 3 | 803 |
| trello `/actions` id | 5 | 5,252 |
| linear `/comments` id | 1 | 0 (empty collection) |
| gmail `threads/*.json /messages` id | 57 | 95,164 (81,404 files) |
| gmail thread numbers (substring search, all JSON scalars) | 30 | 81,404 files |
| gcal `/events` event_id, ical_uid, hangout_link | 8 / 4 / 4 | 10,395 |
| contacts contact_id, email (+ name check) | 2 / 17 | 170 |

The SQL has no duplicate keys: 57 distinct message ids and 30 distinct thread ids. Every message's thread_id and every thread UPDATE targets a thread inserted earlier in the SQL. Trello idShort 41/42/43 are the next numbers on UA/BD, whose 40 base cards use idShort 1–40. Positions 81920/98304/114688 follow the four base BD Follow Up cards (16384–65536). Base cards also have `shortLink` null, so the NULL here matches. There are no Drive `content_path` values (all files are Google-native) and Gmail `history_id` is NULL, so both listed ID contracts hold.

### 5B. SQL structure and schema (NEW; snapshot comparisons provisional)

- The lint's parser read all 178 statements with nothing unparsed. The script is one BEGIN…COMMIT. Every INSERT is a single literal row in parent-before-child order. Every UPDATE has a primary-key predicate.
- Column names were compared case-exactly against the snapshot. All Trello camel-case identifiers are double-quoted and match: `"idBoard"`, `"idList"`, `"dueComplete"`, `"idMembers_json"`, `"idLabels_json"`, `"idShort"`, `"shortLink"`, `"shortUrl"`, `"dateLastActivity"`, `"idMemberCreator"`, `"idCard"`, `"desc"`.
- No `slack_messages.text_fts` or `gmail_messages.body_text_fts` is set. `metadata_json` = `'{}'`. Linear `created_at`/`updated_at` use `YYYY-MM-DDTHH:MM:SSZ`. NOT NULL columns with no default are all filled.
- **Provisional MISMATCH (advisory, not a defect):** these four columns are not in the unverified snapshot, and the base exports have no matching field:
  - `gslides.slides_pages.notes` (lines 62, 68; value NULL)
  - `gslides.slides_page_elements.table_json` (lines 64–72; NULL)
  - `gslides.slides_page_elements.ordinal` (lines 64–72; 0/1)
  - `linear.linear_comments.sequence` (line 328; 1)

  Under the schema README a mismatch alone does not prove a defect. It is listed because, if the live table lacks a column, that single INSERT would roll back the whole transaction.

### 5C. Dates, relationships and consistency (NEW)

- **Clock:** the latest event timestamps are 2025-09-30T23:10:00Z (Leonard's email, its copies, the Oct 6 invite emails and the event `created`/`updated`). All are at or before 2025-10-01T07:00Z. Only the Oct 6 17:00–18:00Z meeting start/end are later, and those are plan fields.
- **Slack:**
  - Every `ts` equals `created_at` to the microsecond, and each reply is later than its parent.
  - The thread counters equal the base replies plus the one new reply, checked by reading each full base thread:
    - 0f6848b3…: 4 replies by {0016, 0038}, plus Leonard → 5 / 2
    - aaec7171…: 8 replies all by 0016, plus Robert → 9 / 1
    - 330b95fd…: 2 replies by {0008, 0038}, plus Arthur → 3 / 3
  - Each `latest_reply` is later than the base value.
- **Gmail** (57 messages / 30 threads, checked by script with 0 problems):
  - `internal_date` = `date` = header `Date`.
  - Header Message-ID, Subject and From match the columns.
  - `in_reply_to` points to an earlier message in the same thread, and the last `references` entry equals `in_reply_to`.
  - Sender copies carry SENT and recipient copies carry INBOX.
  - Each message snippet is the start of its body. After the UPDATEs, each thread's snippet equals its latest message's snippet.
  - Leonard's and the lawyer's messages appear in both mailboxes with consistent labels.
- **Drive suite:**
  - Each Docs, Sheets and Slides row has the same owner, sharing, created_time and modified_time as its Drive row.
  - Each `shared_roles_json` email list equals `shared_with_emails_json`, and `owners_json` = [owner_email].
  - Each Doc's style runs are contiguous and end exactly at `len(body_text)`.
  - Each external term sheet's created_time equals the time of the email that announces it.
- **Trello:** each new id's leading timestamp equals its action date (cards and actions 2025-09-25T19:00/19:30Z, 2025-09-29T16:40/17:10Z, 2025-09-30T16:00Z). `datelastactivity` equals the card's latest action. The board UPDATE moves activity forward from 2025-03-18T18:24:07Z to 2025-09-30T16:00:00Z.
- **Linear:** the comment is at 2025-09-26T18:32Z. The issue UPDATE moves `updated_at` forward from 2025-06-03T05:08:25Z to that time. Arthur's Slack pointer to ENG-2362 is at 18:40Z, after the comment.
- **Calendar:**
  - Each event has start < end and created ≤ updated, and the `self` attendee equals the `calendar_id`.
  - Invite emails match the events: Tallwater, Mon Sep 29 11:30–12:00 PDT = 18:30–19:00Z; execs, Mon Oct 6 10–11 PDT = 17:00–18:00Z. Each invite's sent time equals the event's `created`.
- **Outreach sheet:** each of its 25 rows' "First contact" month and tranche matches the date of Frederick's injected first email to that publisher (May 5–6, Sep 9–11 and Sep 24 tranches).
- **Base facts the injected text points to all resolve:**
  - Leonard's Sep 24 DM "$0.50 D30 ARPI" (D05S58U4SAK 2025-09 #143)
  - The August-sync rights position: Leonard on Aug 25/26 in #executives, "retain code, IP and non-mobile distribution rights"
  - Rayking's Sep 4 2025 email, forwarded by Leonard to Frederick on Sep 4 (thread frederick@…_1842348778705877030)
  - Appodeal's Apr 17 2025 outreach (thread 00000488) and Frederick's Apr 21 Slack about its intake form
  - The Tilting Point UA-fund reply in Frederick's mailbox (…_1842443183462721250)
  - Homa and NCsoft talks in #executives / #bridge-pitch, Sep 2025
  - The a16z speedrun thread (#executives, Sep 2025)
  - The Calm Play LLC entity (#finance, #executives)
  - Leonard's Sep 24 "dude … looking for games" (D05S58U4SAK #149)
  - The ESG Law partner
  - `ANALYTICS.MONETIZATION.REVENUE_DAILY.total_revenue_usd` (in the Snowflake snapshot)
  - The "Publishing Partners" doc (f_10dfa1b4236a7c35dcb632, Frederick, modified 2025-09-24)
- **The May one-pager's numbers match the base:** "first 3K installs, incentivized, D1 50%+, D7 20%+, ARPDAU ≈ $0.13" equals Leonard's base 2025-05-01 investor update.
- **Grader-facing text:** none. Every injected text is written in a persona's voice, and the SQL comments contain no tool-call, pass-rate or gate language (lint is clean).
- **Known base issues:** no injected record depends on an SC-* conflict. SC-1 concerns DD September *installs*, while the SQL cites REVENUE_DAILY *revenue* and publisher-committed installs. The phrase "the four of us" is not a founder-count claim (SC-49). This is advisory context for `/prompt`.

## 6. Findings

**Demonstrated defects: none.**

Advisories (they don't affect the verdict; fix them if you want to lower risk):

1. **Columns not in the snapshot (Check B, provisional).** `slides_pages.notes`, `slides_page_elements.table_json`, `slides_page_elements.ordinal` and `linear_comments.sequence` (lines 62–72, 328) are not in the schema snapshot or the base export shapes. If the live tables lack any of them, the one statement fails and the whole BEGIN…COMMIT rolls back. *Smallest fix:* remove those four columns and their values. Element order already follows from the y-coordinates and insert order.
2. **Externally owned term sheets sit inside Frederick's private folder (Check C, realism).** The 8 term sheets (lines 17–31) are owned by external addresses but have parent d_6fc54be6… (Frederick's folder, shared only with Leonard). Frederick holds only reader on them. In real Drive, neither side could have put them there, and the base has 0 cross-owner parent links in 53,631 files. No rule covering this is in scope, so it is not a defect. *Optional fix:* set those files' `parents_json` to `'[]'` so they surface as shared-with-me, or keep them and accept the simplification. Whether the agent can find them is a `/prompt` question.
3. **Gmail thread-number timestamps (info only).** The 23 publisher threads use numbers whose high bits decode to 2025-09-01T16:00Z, although some of those threads start in May 2025. Gmail thread ids have no listed ID contract, so this is not a finding.
4. **Content referenced but not present (info).** Robert's Copperleaf message, Arthur's Redwood comment and Robert's Kestrel call cite an email or call that has no record of its own. These sources are deliberately Slack/Linear-only. This is not an integrity break. Whether they are visible and authoritative to Frederick belongs to `/prompt`.
5. **Invite subject time zone (cosmetic).** The Robert and Arthur invite copies say "(PDT)" although their calendars are UTC and America/New_York. Harmless.

## 7. Stage dependencies for reuse

The static checks A–C above can be reused by `/prompt` only while all of these still match: SQL SHA-256 `e6aa859b…2d73`, universe manifest `da2f4cf0…ac1a`, schema snapshot `31dcb2b4…5151`, id_contracts `fc4711ef…4682`, and the synth-cut clock. Any SQL edit invalidates this report, and `/injection` must be rerun.

## 8. Evidence limits (outside the certification scope)

No live execution or deployment was done. The current database's compatibility is unknown, and the schema snapshot is unverified (see advisory 1). Search ranking, Agent visibility and task difficulty belong to `/prompt` and `/hardness`.

## 9. Operation ledger (all 176 row effects, in execution order)

| # | Line | Table | Op | Record / target | Key values | Result |
|---|---|---|---|---|---|---|
| 1 | 7 | gdrive.drive_files | INSERT | `d_6fc54be60d1377e340a5b5` | DD publishing; owner frederick.stone@harmonygames.co; parent d_175c0d7bc72ed244b944cb; 2025-09-24T19:00:00Z | A: id unique (53,631 drive_files, complete); parent exists; owner/share emails resolve or are external. C: created<=modified<=clock — PASS |
| 2 | 9 | gdrive.drive_files | INSERT | `f_5e355d03f6eb6a4e866ead` | DD publishing model: ground rules; owner leonard.hayes@harmonygames.co; parent d_63fffeb4fab5233ed5bb73; 2025-09-29T16:00:00Z | A: id unique (53,631 drive_files, complete); parent exists; owner/share emails resolve or are external. C: created<=modified<=clock — PASS |
| 3 | 11 | gdrive.drive_files | INSERT | `f_21203dbcdf780cc07c76cb` | Co-dev: what we'd take; owner frederick.stone@harmonygames.co; parent d_175c0d7bc72ed244b944cb; 2025-09-19T17:30:00Z | A: id unique (53,631 drive_files, complete); parent exists; owner/share emails resolve or are external. C: created<=modified<=clock — PASS |
| 4 | 13 | gdrive.drive_files | INSERT | `f_fd467bd2ae0c6d4f3bd2bc` | DD publisher outreach; owner frederick.stone@harmonygames.co; parent d_6fc54be60d1377e340a5b5; 2025-09-24T19:30:00Z | A: id unique (53,631 drive_files, complete); parent exists; owner/share emails resolve or are external. C: created<=modified<=clock — PASS |
| 5 | 15 | gdrive.drive_files | INSERT | `f_4b3ef3dcf76258a6fda5cd` | Domino Delights one-pager (May 2025); owner frederick.stone@harmonygames.co; parent d_175c0d7bc72ed244b944cb; 2025-05-05T17:00:00Z | A: id unique (53,631 drive_files, complete); parent exists; owner/share emails resolve or are external. C: created<=modified<=clock — PASS |
| 6 | 17 | gdrive.drive_files | INSERT | `f_27cac0eed300cc33eeb4fd` | Oakline Games - term sheet - Domino Delights; owner marek@oaklinegames.com; parent d_6fc54be60d1377e340a5b5; 2025-09-25T15:30:00Z | A: id unique (53,631 drive_files, complete); parent exists; owner/share emails resolve or are external. C: created<=modified<=clock — PASS |
| 7 | 19 | gdrive.drive_files | INSERT | `f_e8cb875d5b7c8d9972d259` | Tallwater Games - term sheet - Domino Delight…; owner paola@tallwatergames.com; parent d_6fc54be60d1377e340a5b5; 2025-09-26T15:00:00Z | A: id unique (53,631 drive_files, complete); parent exists; owner/share emails resolve or are external. C: created<=modified<=clock — PASS |
| 8 | 21 | gdrive.drive_files | INSERT | `f_8ddfb9901891eb8e9dcab8` | Sunfold Mobile - term sheet - Domino Delights; owner lena@sunfoldmobile.com; parent d_6fc54be60d1377e340a5b5; 2025-09-25T15:00:00Z | A: id unique (53,631 drive_files, complete); parent exists; owner/share emails resolve or are external. C: created<=modified<=clock — PASS |
| 9 | 23 | gdrive.drive_files | INSERT | `f_d72e8b34e7496f0de668bc` | Harbor Lane Games - term sheet - Domino Delig…; owner diego@harborlanegames.com; parent d_6fc54be60d1377e340a5b5; 2025-09-25T16:00:00Z | A: id unique (53,631 drive_files, complete); parent exists; owner/share emails resolve or are external. C: created<=modified<=clock — PASS |
| 10 | 25 | gdrive.drive_files | INSERT | `f_a6a5647f977d4638b2b8b1` | Wavecrest Play - term sheet - Domino Delights; owner sofia@wavecrestplay.com; parent d_6fc54be60d1377e340a5b5; 2025-09-25T16:30:00Z | A: id unique (53,631 drive_files, complete); parent exists; owner/share emails resolve or are external. C: created<=modified<=clock — PASS |
| 11 | 27 | gdrive.drive_files | INSERT | `f_464839da025a0a01f53979` | Moonrail Studios - term sheet - Domino Deligh…; owner anika@moonrailstudios.com; parent d_6fc54be60d1377e340a5b5; 2025-09-25T17:00:00Z | A: id unique (53,631 drive_files, complete); parent exists; owner/share emails resolve or are external. C: created<=modified<=clock — PASS |
| 12 | 29 | gdrive.drive_files | INSERT | `f_3eccf6e0bb63955dc51e27` | Northglow Publishing - term sheet - Domino De…; owner callum@northglowpublishing.com; parent d_6fc54be60d1377e340a5b5; 2025-09-26T16:00:00Z | A: id unique (53,631 drive_files, complete); parent exists; owner/share emails resolve or are external. C: created<=modified<=clock — PASS |
| 13 | 31 | gdrive.drive_files | INSERT | `f_5f3ef4a4760d18e696a41a` | Pinegrove Games - term sheet - Domino Delight…; owner elena@pinegrovegames.com; parent d_6fc54be60d1377e340a5b5; 2025-09-26T17:00:00Z | A: id unique (53,631 drive_files, complete); parent exists; owner/share emails resolve or are external. C: created<=modified<=clock — PASS |
| 14 | 34 | gdocs.docs_documents | INSERT | `f_5e355d03f6eb6a4e866ead` | DD publishing model: ground rules; 2255 chars; 2025-09-29T16:00:00Z | A: id unique (595 docs); drive row in SQL; body_text non-empty. C: style_runs cover body exactly; times/owner/share = drive row — PASS |
| 15 | 36 | gdocs.docs_documents | INSERT | `f_21203dbcdf780cc07c76cb` | Co-dev: what we'd take; 273 chars; 2025-09-19T17:30:00Z | A: id unique (595 docs); drive row in SQL; body_text non-empty. C: style_runs cover body exactly; times/owner/share = drive row — PASS |
| 16 | 38 | gdocs.docs_documents | INSERT | `f_27cac0eed300cc33eeb4fd` | Oakline Games - term sheet - Domino Delights; 336 chars; 2025-09-25T15:30:00Z | A: id unique (595 docs); drive row in SQL; body_text non-empty. C: style_runs cover body exactly; times/owner/share = drive row — PASS |
| 17 | 40 | gdocs.docs_documents | INSERT | `f_e8cb875d5b7c8d9972d259` | Tallwater Games - term sheet - Domino Delight…; 236 chars; 2025-09-26T15:00:00Z | A: id unique (595 docs); drive row in SQL; body_text non-empty. C: style_runs cover body exactly; times/owner/share = drive row — PASS |
| 18 | 42 | gdocs.docs_documents | INSERT | `f_8ddfb9901891eb8e9dcab8` | Sunfold Mobile - term sheet - Domino Delights; 234 chars; 2025-09-25T15:00:00Z | A: id unique (595 docs); drive row in SQL; body_text non-empty. C: style_runs cover body exactly; times/owner/share = drive row — PASS |
| 19 | 44 | gdocs.docs_documents | INSERT | `f_d72e8b34e7496f0de668bc` | Harbor Lane Games - term sheet - Domino Delig…; 239 chars; 2025-09-25T16:00:00Z | A: id unique (595 docs); drive row in SQL; body_text non-empty. C: style_runs cover body exactly; times/owner/share = drive row — PASS |
| 20 | 46 | gdocs.docs_documents | INSERT | `f_a6a5647f977d4638b2b8b1` | Wavecrest Play - term sheet - Domino Delights; 237 chars; 2025-09-25T16:30:00Z | A: id unique (595 docs); drive row in SQL; body_text non-empty. C: style_runs cover body exactly; times/owner/share = drive row — PASS |
| 21 | 48 | gdocs.docs_documents | INSERT | `f_464839da025a0a01f53979` | Moonrail Studios - term sheet - Domino Deligh…; 235 chars; 2025-09-25T17:00:00Z | A: id unique (595 docs); drive row in SQL; body_text non-empty. C: style_runs cover body exactly; times/owner/share = drive row — PASS |
| 22 | 50 | gdocs.docs_documents | INSERT | `f_3eccf6e0bb63955dc51e27` | Northglow Publishing - term sheet - Domino De…; 308 chars; 2025-09-26T16:00:00Z | A: id unique (595 docs); drive row in SQL; body_text non-empty. C: style_runs cover body exactly; times/owner/share = drive row — PASS |
| 23 | 52 | gdocs.docs_documents | INSERT | `f_5f3ef4a4760d18e696a41a` | Pinegrove Games - term sheet - Domino Delight…; 323 chars; 2025-09-26T17:00:00Z | A: id unique (595 docs); drive row in SQL; body_text non-empty. C: style_runs cover body exactly; times/owner/share = drive row — PASS |
| 24 | 55 | gsheets.sheets_spreadsheets | INSERT | `f_fd467bd2ae0c6d4f3bd2bc` | DD publisher outreach | A: id unique (356); drive row in SQL. C: times/owner = drive row — PASS |
| 25 | 57 | gsheets.sheets_sheets | INSERT | `f_fd467bd2ae0c6d4f3bd2bc` | Outreach | A: parent spreadsheet inserted earlier. B: grid_json valid list — PASS |
| 26 | 60 | gslides.slides_presentations | INSERT | `f_4b3ef3dcf76258a6fda5cd` | Domino Delights one-pager (May 2025) | A: id unique (132); drive row in SQL. C: times/owner = drive row — PASS |
| 27 | 62 | gslides.slides_pages | INSERT | `f_4b3ef3dcf76258a6fda5cd` | slide_13e87746ab47 | A: parent presentation inserted earlier. B: `notes` not in snapshot (advisory) — PASS |
| 28 | 64 | gslides.slides_page_elements | INSERT | `f_4b3ef3dcf76258a6fda5cd` | Domino Delights | A: parent page inserted earlier. B: `table_json`,`ordinal` not in snapshot (advisory) — PASS |
| 29 | 66 | gslides.slides_page_elements | INSERT | `f_4b3ef3dcf76258a6fda5cd` | A tile puzzle game with a hybrid IAP and rewarded-… | A: parent page inserted earlier. B: `table_json`,`ordinal` not in snapshot (advisory) — PASS |
| 30 | 68 | gslides.slides_pages | INSERT | `f_4b3ef3dcf76258a6fda5cd` | slide_57bcd1eccbff | A: parent presentation inserted earlier. B: `notes` not in snapshot (advisory) — PASS |
| 31 | 70 | gslides.slides_page_elements | INSERT | `f_4b3ef3dcf76258a6fda5cd` | Early numbers | A: parent page inserted earlier. B: `table_json`,`ordinal` not in snapshot (advisory) — PASS |
| 32 | 72 | gslides.slides_page_elements | INSERT | `f_4b3ef3dcf76258a6fda5cd` | First 3K installs, incentivized traffic. D1 retent… | A: parent page inserted earlier. B: `table_json`,`ordinal` not in snapshot (advisory) — PASS |
| 33 | 75 | slack.slack_messages | INSERT | `bda432db3ac81bf7f0c8903f0465ec9d` | D05S58U4SAK; EMPLOYEE_0008_SLACK_ID; ts 1757090400.829462 (2025-09-05T16:40:00.829462Z); parent None | A: channel/user exist, author is member; id unique (610,468 msgs). C: ts=created_at — PASS |
| 34 | 77 | slack.slack_messages | INSERT | `f55bd27436eb285a15d833648b922e9b` | C096HFA5Z8W; EMPLOYEE_0038_SLACK_ID; ts 1758915000.867092 (2025-09-26T19:30:00.867092Z); parent 0f6848b39af117c741af520ce5204eac | A: channel/user exist, author is member; id unique (610,468 msgs). C: ts=created_at; thread parent exists, reply after parent — PASS |
| 35 | 79 | slack.slack_messages | UPDATE | `0f6848b39af117c741af520ce5204eac` | reply_count 5, reply_users_count 2, latest_reply 1758915000.867092 | C: counts = base replies + 1 new reply (verified from full thread) — PASS |
| 36 | 80 | slack.slack_messages | INSERT | `495d71a7e14dfaa68cac26fc4a6c4e03` | C07C2866011; EMPLOYEE_0016_SLACK_ID; ts 1758909900.662794 (2025-09-26T18:05:00.662794Z); parent aaec7171d897e134a22b41511467f646 | A: channel/user exist, author is member; id unique (610,468 msgs). C: ts=created_at; thread parent exists, reply after parent — PASS |
| 37 | 82 | slack.slack_messages | UPDATE | `aaec7171d897e134a22b41511467f646` | reply_count 9, reply_users_count 1, latest_reply 1758909900.662794 | C: counts = base replies + 1 new reply (verified from full thread) — PASS |
| 38 | 83 | slack.slack_messages | INSERT | `e64606893af9f4316891a357ec26a691` | C069FF9Q57S; EMPLOYEE_0025_SLACK_ID; ts 1758912000.686342 (2025-09-26T18:40:00.686342Z); parent None | A: channel/user exist, author is member; id unique (610,468 msgs). C: ts=created_at — PASS |
| 39 | 85 | slack.slack_messages | INSERT | `e44da6a468e7795a1b5853cfb0763aaf` | C07C2866011; EMPLOYEE_0016_SLACK_ID; ts 1759176900.065118 (2025-09-29T20:15:00.065118Z); parent None | A: channel/user exist, author is member; id unique (610,468 msgs). C: ts=created_at — PASS |
| 40 | 87 | slack.slack_messages | INSERT | `0230b2df24ec829928fe1c55ad6185bf` | C07C2866011; EMPLOYEE_0025_SLACK_ID; ts 1759251900.005166 (2025-09-30T17:05:00.005166Z); parent 330b95fd38236b4e7192e24f272685b4 | A: channel/user exist, author is member; id unique (610,468 msgs). C: ts=created_at; thread parent exists, reply after parent — PASS |
| 41 | 89 | slack.slack_messages | UPDATE | `330b95fd38236b4e7192e24f272685b4` | reply_count 3, reply_users_count 3, latest_reply 1759251900.005166 | C: counts = base replies + 1 new reply (verified from full thread) — PASS |
| 42 | 91 | trello.trello_cards | INSERT | `68d5913004a98be3b4c45408` | F/up with Marek; idShort 41; list BD Follow Up; members ["4b4a68fc0fec0b254e4f9d8e"] | A: board/list/member exist; new id unique (803 cards / 5,252 actions); idShort next on board. C: id timestamp = action date — PASS |
| 43 | 93 | trello.trello_actions | INSERT | `68d591301a22988efe387ad0` | createCard; 2025-09-25T19:00:00Z; by 4b4a68fc0fec0b254e4f9d8e; card 68d5913004a98be3b4c45408 | A: board/list/member exist; new id unique (803 cards / 5,252 actions); idShort next on board. C: id timestamp = action date — PASS |
| 44 | 95 | trello.trello_actions | INSERT | `68dabd6800e271eb0608d2d6` | commentCard; 2025-09-29T17:10:00Z; by 4b4a68fc0fec0b254e4f9d8e; card 68d5913004a98be3b4c45408 | A: board/list/member exist; new id unique (803 cards / 5,252 actions); idShort next on board. C: id timestamp = action date — PASS |
| 45 | 97 | trello.trello_cards | INSERT | `68d598387dea3e7fe85e3a0a` | F/up with Lena; idShort 42; list BD Follow Up; members ["4b4a68fc0fec0b254e4f9d8e"] | A: board/list/member exist; new id unique (803 cards / 5,252 actions); idShort next on board. C: id timestamp = action date — PASS |
| 46 | 99 | trello.trello_actions | INSERT | `68d59838d15e4b33136f7d16` | createCard; 2025-09-25T19:30:00Z; by 4b4a68fc0fec0b254e4f9d8e; card 68d598387dea3e7fe85e3a0a | A: board/list/member exist; new id unique (803 cards / 5,252 actions); idShort next on board. C: id timestamp = action date — PASS |
| 47 | 101 | trello.trello_actions | INSERT | `68dbfe80ef9c41b4f4fa8fe9` | commentCard; 2025-09-30T16:00:00Z; by 4b4a68fc0fec0b254e4f9d8e; card 68d598387dea3e7fe85e3a0a | A: board/list/member exist; new id unique (803 cards / 5,252 actions); idShort next on board. C: id timestamp = action date — PASS |
| 48 | 103 | trello.trello_cards | INSERT | `68dab660c900179df4f5f92d` | DD publishing; idShort 43; list BD Follow Up; members ["PERSON_6094_TRELLO_USER_ID", "4b4a68fc0fec0b254e4f9d8e"] | A: board/list/member exist; new id unique (803 cards / 5,252 actions); idShort next on board. C: id timestamp = action date — PASS |
| 49 | 105 | trello.trello_actions | INSERT | `68dab6601ab74f77950572c9` | createCard; 2025-09-29T16:40:00Z; by PERSON_6094_TRELLO_USER_ID; card 68dab660c900179df4f5f92d | A: board/list/member exist; new id unique (803 cards / 5,252 actions); idShort next on board. C: id timestamp = action date — PASS |
| 50 | 107 | trello.trello_boards | UPDATE | `66da196af476ab78deaa0cef` | dateLastActivity 2025-09-30T16:00:00Z (base 2025-03-18T18:24:07Z) | C: moves board activity forward to latest injected action — PASS |
| 51 | 109 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844732284109533…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 52 | 111 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAY2swo8Vt78l2V…` | leonard.hayes@harmonygames.co → ["Frederick Stone <frederick.stone@harmo…; 2025-09-30T23:10:00Z; DD publishing: what I need for Monday | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 53 | 113 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/184473228410941644…` | leonard.hayes@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 54 | 115 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAY2swo8Vt78l2VvR…` | leonard.hayes@harmonygames.co → ["Frederick Stone <frederick.stone@harmo…; 2025-09-30T23:10:00Z; DD publishing: what I need for Monday | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 55 | 117 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844620296192667…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 56 | 119 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CA9raR_pqldShsv…` | PERSON_2694_EMAIL → ["Leonard Hayes <leonard.hayes@harmonyga…; 2025-09-29T17:30:00Z; License paper timing | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 57 | 121 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/184462029619238589…` | leonard.hayes@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 58 | 123 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CA9raR_pqldShsvOh…` | PERSON_2694_EMAIL → ["Leonard Hayes <leonard.hayes@harmonyga…; 2025-09-29T17:30:00Z; License paper timing | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 59 | 125 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1844620296192667…` | snippet → OK. Fred, that makes Nov 14 our signing date,… | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 60 | 126 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAP16wHs998luhy…` | leonard.hayes@harmonygames.co → ["PERSON_2694_NAME <PERSON_2694_EMAIL>"]; 2025-09-30T16:10:00Z; Re: License paper timing | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 61 | 128 | gmail.gmail_threads | UPDATE | `leonard.hayes@harmonygames.co/184462029619238589…` | snippet → OK. Fred, that makes Nov 14 our signing date,… | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 62 | 129 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAP16wHs998luhyUQ…` | leonard.hayes@harmonygames.co → ["PERSON_2694_NAME <PERSON_2694_EMAIL>"]; 2025-09-30T16:10:00Z; Re: License paper timing | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 63 | 131 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842077918822838…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 64 | 133 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAP2WDhxJLWVtG1…` | frederick.stone@harmonygames.co → ["Marek Sobol <marek@oaklinegames.com>"]; 2025-09-09T16:10:00Z; Domino Delights on mobile | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 65 | 135 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918822838…` | snippet → Good to hear from you. Our term sheet for Dom… | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 66 | 136 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAM3LRAoD9ONdfZ…` | marek@oaklinegames.com → ["Frederick Stone <frederick.stone@harmo…; 2025-09-25T15:30:00Z; Re: Domino Delights on mobile | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 67 | 138 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918822838…` | snippet → Confirming our finance team sent the $10,000 … | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 68 | 139 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAybuYiHDdC_1wq…` | marek@oaklinegames.com → ["Frederick Stone <frederick.stone@harmo…; 2025-09-29T16:00:00Z; Re: Domino Delights on mobile | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 69 | 141 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842077918823428…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 70 | 143 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CA_SUmrrUxKRZgw…` | frederick.stone@harmonygames.co → ["Paola Duarte <paola@tallwatergames.com…; 2025-05-05T17:10:00Z; Domino Delights: publishing partners | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 71 | 145 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918823428…` | snippet → Thanks. Nothing for us right now, but we plan… | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 72 | 146 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAUAdeLf4img2MU…` | paola@tallwatergames.com → ["Frederick Stone <frederick.stone@harmo…; 2025-05-12T17:10:00Z; Re: Domino Delights: publishing partners | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 73 | 148 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918823428…` | snippet → Hi Paola, picking this back up. We're ready t… | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 74 | 149 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAdmUC104qnASUK…` | frederick.stone@harmonygames.co → ["Paola Duarte <paola@tallwatergames.com…; 2025-09-24T21:15:00Z; Re: Domino Delights: publishing partners | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 75 | 151 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918823428…` | snippet → Thanks for picking this back up. I've shared … | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 76 | 152 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CATuOaB7ct5kwVW…` | paola@tallwatergames.com → ["Frederick Stone <frederick.stone@harmo…; 2025-09-26T15:00:00Z; Re: Domino Delights: publishing partners | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 77 | 154 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842077918823258…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 78 | 156 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAtGdlTBzxQgaYA…` | frederick.stone@harmonygames.co → ["Lena Fischer <lena@sunfoldmobile.com>"…; 2025-09-09T16:40:00Z; Domino Delights on mobile | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 79 | 158 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918823258…` | snippet → Thanks for the note. Term sheet's shared with… | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 80 | 159 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CA0P8idnP7zRdjt…` | lena@sunfoldmobile.com → ["Frederick Stone <frederick.stone@harmo…; 2025-09-25T15:00:00Z; Re: Domino Delights on mobile | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 81 | 161 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842077918823445…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 82 | 163 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAqKllUzAFyNNaZ…` | frederick.stone@harmonygames.co → ["Diego Reyes <diego@harborlanegames.com…; 2025-05-05T17:30:00Z; Domino Delights: publishing partners | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 83 | 165 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918823445…` | snippet → Interesting, but we're full this year. Try me… | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 84 | 166 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAxaKI6sCYMsA4x…` | diego@harborlanegames.com → ["Frederick Stone <frederick.stone@harmo…; 2025-05-12T17:30:00Z; Re: Domino Delights: publishing partners | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 85 | 168 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918823445…` | snippet → Hi Diego, picking this back up. We're ready t… | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 86 | 169 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CA7reXRO7A3L9v6…` | frederick.stone@harmonygames.co → ["Diego Reyes <diego@harborlanegames.com…; 2025-09-24T21:25:00Z; Re: Domino Delights: publishing partners | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 87 | 171 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918823445…` | snippet → Timing works for us. I've put our term sheet … | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 88 | 172 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAC883mb0pCloui…` | diego@harborlanegames.com → ["Frederick Stone <frederick.stone@harmo…; 2025-09-25T16:00:00Z; Re: Domino Delights: publishing partners | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 89 | 174 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842077918823344…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 90 | 176 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CACrJqyP5OVwohR…` | frederick.stone@harmonygames.co → ["Sofia Lindqvist <sofia@wavecrestplay.c…; 2025-05-05T17:50:00Z; Domino Delights: publishing partners | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 91 | 178 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918823344…` | snippet → Thanks for the one-pager. Not the right momen… | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 92 | 179 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CACs-ibscXxR5Qz…` | sofia@wavecrestplay.com → ["Frederick Stone <frederick.stone@harmo…; 2025-05-12T17:50:00Z; Re: Domino Delights: publishing partners | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 93 | 181 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918823344…` | snippet → Hi Sofia, picking this back up. We're ready t… | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 94 | 182 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAJ_9MoUdsZwMeF…` | frederick.stone@harmonygames.co → ["Sofia Lindqvist <sofia@wavecrestplay.c…; 2025-09-24T21:35:00Z; Re: Domino Delights: publishing partners | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 95 | 184 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918823344…` | snippet → Happy to talk. Sharing our term sheet for Dom… | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 96 | 185 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAYPBDL8-vDU_A1…` | sofia@wavecrestplay.com → ["Frederick Stone <frederick.stone@harmo…; 2025-09-25T16:30:00Z; Re: Domino Delights: publishing partners | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 97 | 187 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842077918822811…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 98 | 189 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAYSOqxN-_aUSJm…` | frederick.stone@harmonygames.co → ["Anika Rao <anika@moonrailstudios.com>"…; 2025-05-05T18:10:00Z; Domino Delights: publishing partners | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 99 | 191 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918822811…` | snippet → Not right now, our slate's set. Ping me in th… | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 100 | 192 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAF7NPNtft83IuP…` | anika@moonrailstudios.com → ["Frederick Stone <frederick.stone@harmo…; 2025-05-12T18:10:00Z; Re: Domino Delights: publishing partners | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 101 | 194 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918822811…` | snippet → Hi Anika, picking this back up. We're ready t… | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 102 | 195 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CA78kSmFAWgUotE…` | frederick.stone@harmonygames.co → ["Anika Rao <anika@moonrailstudios.com>"…; 2025-09-24T21:45:00Z; Re: Domino Delights: publishing partners | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 103 | 197 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918822811…` | snippet → Great, we're interested. You should have our … | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 104 | 198 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAkAeFrhFWVvHmJ…` | anika@moonrailstudios.com → ["Frederick Stone <frederick.stone@harmo…; 2025-09-25T17:00:00Z; Re: Domino Delights: publishing partners | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 105 | 200 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842077918822429…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 106 | 202 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAdwjksxsuJJOcL…` | frederick.stone@harmonygames.co → ["Callum Ross <callum@northglowpublishin…; 2025-09-09T17:10:00Z; Domino Delights on mobile | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 107 | 204 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918822429…` | snippet → Thanks, this fits what we're looking for. Our… | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 108 | 205 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAlXwp5pu0sE1OU…` | callum@northglowpublishing.com → ["Frederick Stone <frederick.stone@harmo…; 2025-09-26T16:00:00Z; Re: Domino Delights on mobile | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 109 | 207 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842077918823323…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 110 | 209 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CACoVq8Ky0haUCZ…` | frederick.stone@harmonygames.co → ["Elena Petrova <elena@pinegrovegames.co…; 2025-09-10T16:20:00Z; Domino Delights on mobile | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 111 | 211 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918823323…` | snippet → Thanks for reaching out. We've shared a term … | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 112 | 212 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAoasKjUeOpKv0b…` | elena@pinegrovegames.com → ["Frederick Stone <frederick.stone@harmo…; 2025-09-26T17:00:00Z; Re: Domino Delights on mobile | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 113 | 214 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842077918822912…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 114 | 216 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAMpr5OcX5NXYR_…` | frederick.stone@harmonygames.co → ["Rhys Morgan <rhys@fernhollowmedia.com>…; 2025-05-06T16:20:00Z; Domino Delights: publishing partners | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 115 | 218 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918822912…` | snippet → Thanks for thinking of us, but we'll pass on … | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 116 | 219 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CA4HMxbTQ3f0dBk…` | rhys@fernhollowmedia.com → ["Frederick Stone <frederick.stone@harmo…; 2025-05-13T15:10:00Z; Re: Domino Delights: publishing partners | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 117 | 221 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842077918822894…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 118 | 223 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAn2ND39zPOi_-9…` | frederick.stone@harmonygames.co → ["Nadia Haddad <nadia@quietbaygames.com>…; 2025-05-06T16:50:00Z; Domino Delights: publishing partners | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 119 | 225 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918822894…` | snippet → Appreciate the note. We're going to pass, til… | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 120 | 226 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CA8vx_4jNxXdrEo…` | nadia@quietbaygames.com → ["Frederick Stone <frederick.stone@harmo…; 2025-05-15T15:20:00Z; Re: Domino Delights: publishing partners | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 121 | 228 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842077918823167…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 122 | 230 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAY2P49nMwKwieq…` | frederick.stone@harmonygames.co → ["Yuki Sato <yuki@slatewoodmobile.com>"]; 2025-09-10T16:50:00Z; Domino Delights on mobile | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 123 | 232 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918823167…` | snippet → We had a look and we'll pass for now. Our sla… | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 124 | 233 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CATyMO43tqibSWc…` | yuki@slatewoodmobile.com → ["Frederick Stone <frederick.stone@harmo…; 2025-09-17T15:30:00Z; Re: Domino Delights on mobile | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 125 | 235 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842077918822812…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 126 | 237 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CA2Z26MATHdprW0…` | frederick.stone@harmonygames.co → ["Tessa Hale <tessa@ironbridgeinteractiv…; 2025-09-10T17:20:00Z; Domino Delights on mobile | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 127 | 239 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918822812…` | snippet → Thanks, but we'll pass. We only take titles w… | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 128 | 240 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAd_cLOeha5s8T9…` | tessa@ironbridgeinteractive.com → ["Frederick Stone <frederick.stone@harmo…; 2025-09-19T15:40:00Z; Re: Domino Delights on mobile | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 129 | 242 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842077918822727…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 130 | 244 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CA4rE7_gd0Maxha…` | frederick.stone@harmonygames.co → ["Omar Khalil <omar@tidewellstudios.com>…; 2025-09-24T20:05:00Z; Domino Delights publishing | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 131 | 246 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918822727…` | snippet → Not for us, so we'll pass on this one. Good l… | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 132 | 247 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CABfR1GT5_5Tlu8…` | omar@tidewellstudios.com → ["Frederick Stone <frederick.stone@harmo…; 2025-09-29T15:50:00Z; Re: Domino Delights publishing | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 133 | 249 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842077918823060…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 134 | 251 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAgc-22Ffk7EEQt…` | frederick.stone@harmonygames.co → ["Greta Holm <greta@marlinplay.com>"]; 2025-09-24T20:15:00Z; Domino Delights publishing | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 135 | 253 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918823060…` | snippet → We've decided to pass on Domino Delights. Tha… | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 136 | 254 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CA9DvG_MtLDt4FJ…` | greta@marlinplay.com → ["Frederick Stone <frederick.stone@harmo…; 2025-09-30T15:10:00Z; Re: Domino Delights publishing | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 137 | 256 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842077918823167…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 138 | 258 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAI3ko-q07278dY…` | frederick.stone@harmonygames.co → ["Ivo Novak <ivo@kitebridgegames.com>"]; 2025-09-24T20:25:00Z; Domino Delights publishing | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 139 | 260 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918823167…` | snippet → Thanks, this looks interesting. Could you sen… | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 140 | 261 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAozTwdLEuSV1xB…` | ivo@kitebridgegames.com → ["Frederick Stone <frederick.stone@harmo…; 2025-09-26T16:00:00Z; Re: Domino Delights publishing | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 141 | 263 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842077918822627…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 142 | 265 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAthsveRLmc8kD8…` | frederick.stone@harmonygames.co → ["Orchard Lane Games <partnerships@orcha…; 2025-05-06T17:20:00Z; Domino Delights: publishing partners | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 143 | 267 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842077918822746…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 144 | 269 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CA2JlxL00XVM6Jn…` | frederick.stone@harmonygames.co → ["Summit Mobile <partnerships@summitmobi…; 2025-05-06T17:50:00Z; Domino Delights: publishing partners | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 145 | 271 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842077918822746…` | snippet → Thanks for contacting Summit Mobile. This is … | Target inserted earlier in SQL; C: snippet = new latest message — PASS |
| 146 | 272 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAVCa1kwMOk0Nk1…` | noreply@summitmobile.io → ["Frederick Stone <frederick.stone@harmo…; 2025-05-06T17:51:00Z; Automatic reply: Domino Delights: publis… | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 147 | 274 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842077918822773…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 148 | 276 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAZTUQuC3dVbDRj…` | frederick.stone@harmonygames.co → ["Silverlake Mobile <partnerships@silver…; 2025-09-11T16:30:00Z; Domino Delights on mobile | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 149 | 278 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842077918822506…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 150 | 280 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CA_SDWWIN5thiyw…` | frederick.stone@harmonygames.co → ["Cedarbrook Play <partnerships@cedarbro…; 2025-09-11T17:00:00Z; Domino Delights on mobile | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 151 | 282 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842077918822804…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 152 | 284 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAkwm_uqp3-570V…` | frederick.stone@harmonygames.co → ["Foxglove Games <partnerships@foxgloveg…; 2025-09-24T20:35:00Z; Domino Delights publishing | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 153 | 286 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842077918823170…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 154 | 288 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CAiok9sGZgcpDbX…` | frederick.stone@harmonygames.co → ["Riverstone Interactive <partnerships@r…; 2025-09-24T20:45:00Z; Domino Delights publishing | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 155 | 290 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842077918822759…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 156 | 292 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<CALyaIXhq7TwAhD…` | frederick.stone@harmonygames.co → ["Bellwether Arcade <partnerships@bellwe…; 2025-09-24T20:55:00Z; Domino Delights publishing | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 157 | 294 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844346617856625…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 158 | 296 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-e8098c…` | leonard.hayes@harmonygames.co → ["frederick.stone@harmonygames.co", "pao…; 2025-09-26T17:00:00Z; Invitation: Tallwater follow-up @ Mon Se… | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 159 | 298 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844732284109731…` | frederick.stone@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 160 | 300 | gmail.gmail_messages | INSERT | `frederick.stone@harmonygames.co/<calendar-faae36…` | leonard.hayes@harmonygames.co → ["frederick.stone@harmonygames.co", "rob…; 2025-09-30T23:10:00Z; Invitation: DD publishing: execs @ Mon O… | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 161 | 302 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844732284109187692` | robert@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 162 | 304 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<calendar-1a05ea6c-8c31-a…` | leonard.hayes@harmonygames.co → ["frederick.stone@harmonygames.co", "rob…; 2025-09-30T23:10:00Z; Invitation: DD publishing: execs @ Mon O… | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 163 | 306 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844732284108819059` | arthur.blake@harmonygames.co | A: thread no. absent from all 81,404 base thread files (complete). C: final snippet = latest message snippet — PASS |
| 164 | 308 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<calendar-71404a73-…` | leonard.hayes@harmonygames.co → ["frederick.stone@harmonygames.co", "rob…; 2025-09-30T23:10:00Z; Invitation: DD publishing: execs @ Mon O… | A: id absent from 95,164 base messages (complete); user mailbox exists. C: date=internal_date=header; reply chain/labels ok — PASS |
| 165 | 311 | gcal.gcal_events | INSERT | `evt_43fda04cd11b9d58a05161` | frederick.stone@harmonygames.co; Tallwater follow-up; 2025-09-29T18:30:00Z–19:00:00Z | A: event_id/ical_uid/meet link unique (10,395 events); calendar exists. C: start<end; created<=updated<=clock; self flag = calendar — PASS |
| 166 | 313 | gcal.gcal_events | INSERT | `evt_c6d68c2a6f110765c48b9b` | leonard.hayes@harmonygames.co; Tallwater follow-up; 2025-09-29T18:30:00Z–19:00:00Z | A: event_id/ical_uid/meet link unique (10,395 events); calendar exists. C: start<end; created<=updated<=clock; self flag = calendar — PASS |
| 167 | 315 | gcal.gcal_events | INSERT | `evt_d6905d9d5497d6a83a9a56` | frederick.stone@harmonygames.co; Harbor Lane call; 2025-09-26T19:00:00Z–19:30:00Z | A: event_id/ical_uid/meet link unique (10,395 events); calendar exists. C: start<end; created<=updated<=clock; self flag = calendar — PASS |
| 168 | 317 | gcal.gcal_events | INSERT | `evt_48e63a8c7304cf9432fb46` | frederick.stone@harmonygames.co; Wavecrest call; 2025-09-25T18:00:00Z–18:30:00Z | A: event_id/ical_uid/meet link unique (10,395 events); calendar exists. C: start<end; created<=updated<=clock; self flag = calendar — PASS |
| 169 | 319 | gcal.gcal_events | INSERT | `evt_881d3e07c598b2205a7ff3` | frederick.stone@harmonygames.co; DD publishing: execs; 2025-10-06T17:00:00Z–18:00:00Z | A: event_id/ical_uid/meet link unique (10,395 events); calendar exists. C: start<end; created<=updated<=clock; self flag = calendar — PASS |
| 170 | 321 | gcal.gcal_events | INSERT | `evt_8512c7a6aa483d8aeb6a7d` | leonard.hayes@harmonygames.co; DD publishing: execs; 2025-10-06T17:00:00Z–18:00:00Z | A: event_id/ical_uid/meet link unique (10,395 events); calendar exists. C: start<end; created<=updated<=clock; self flag = calendar — PASS |
| 171 | 323 | gcal.gcal_events | INSERT | `evt_b0d8daa048f918be523cb0` | robert@harmonygames.co; DD publishing: execs; 2025-10-06T17:00:00Z–18:00:00Z | A: event_id/ical_uid/meet link unique (10,395 events); calendar exists. C: start<end; created<=updated<=clock; self flag = calendar — PASS |
| 172 | 325 | gcal.gcal_events | INSERT | `evt_cb02d2cef6eb1d6bd4cd0b` | arthur.blake@harmonygames.co; DD publishing: execs; 2025-10-06T17:00:00Z–18:00:00Z | A: event_id/ical_uid/meet link unique (10,395 events); calendar exists. C: start<end; created<=updated<=clock; self flag = calendar — PASS |
| 173 | 328 | linear.linear_comments | INSERT | `lc_674982ffdca63f854ec6f591` | issue ENG-2362; author usr_cc3e90160f490686 (Arthur Blake); 2025-09-26T18:32:00Z | A: issue and author exist; comments collection empty in base. B: `sequence` not in snapshot (advisory) — PASS |
| 174 | 330 | linear.linear_issues | UPDATE | `ENG-2362` | updated_at 2025-09-26T18:32:00Z (base 2025-06-03T05:08:25Z) | A: target exists. B: iso_utc format. C: moves updated_at forward to comment time — PASS |
| 175 | 332 | contacts.contacts | INSERT | `5373edb55ca853d6052ecce5` | Anika Rao; anika@moonrailstudios.com; job Partnerships, Kestrel Group | A: contact_id and email unique (170 contacts); no name duplicate — PASS |
| 176 | 334 | contacts.contacts | INSERT | `1d6fd505d2fea08fa0f26c6e` | Lena Fischer; lena@sunfoldmobile.com; job Sunfold Mobile | A: contact_id and email unique (170 contacts); no name duplicate — PASS |

## 10. Final verdict

### FINAL VERDICT: PASS

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), effort unconfirmed

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Next action: Proceed to /prompt. Optional: drop the four columns that aren't in the snapshot (advisory 1) before deployment.

Evidence limits: No required static check is unresolved. Static scope only: no live run, and the schema snapshot is unverified (four columns not covered). Agent visibility and difficulty are not assessed here.
