# Injection data-integrity review (Eval 0)

## 1. Scope

| Field | Value |
|---|---|
| Stage / review version | `/injection` · `injection-static-v2` · evidence contract `stage-evidence-v1` |
| Mode | Chat review, attempt 6ae9909f707bc2aa0a7ed6e9 (audit; SQL never executed) |
| Review time | 2026-11-03 (UTC) |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); manifest `Evals/references/universes/synthcut/universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Input | `Evals/task_inputs/01_Universe_Inject.sql` (saved rev 4 from upload `01_Universe_Inject (2).sql`), 236,249 bytes, sha256 `795bd191872d7f57be1d2e0d09bd74f23a05561ce2c6e58e87c6162c11b4713f` |
| Previous version | rev 3, sha256 `9066997d…ef74ef3` (PASS, `injection-static-v2`). Diff rev 3 → rev 4: exactly 3 lines changed (93, 135, 137, all `gdocs.docs_documents` VALUES rows); every other line is byte-identical. |
| References | Eval 0 sha256 `e034019b…6eff`; schema snapshot `injection.json` sha256 `31dcb2b4…5c7cb67f`; `id_contracts.json` sha256 `fc4711ef…ed4682`; WORKFLOW sha256 `ee4cd8e1…fcd5d` |
| Lint | `hg_injection_lint.py` injection-lint-v1 on rev 4 (sha256 `795bd191…b4713f`): 297 statements (BEGIN, 260 INSERT, 35 UPDATE, COMMIT), 0 FAIL, 0 CHECK, 0 INFO, 0 unparsed |

## 2. Input / authority issues

None. One SQL input (rev 4), saved and read in full, and diffed line by line against rev 3. SQL comments (lines 1–4 plus section headers) only describe intent and structure; none mention tool calls, pass rate or gates (line 4's "before every agent run" is an authoring note in a comment, not text in an injected record).

**Evidence reuse (stage-evidence-v1).** The rev 3 report's per-row checks are reused for the 292 row operations whose SQL lines are byte-identical in rev 4. All reuse dependencies were revalidated: universe manifest sha256 `da2f4cf0…a04aac1a` (unchanged), Eval 0 `e034019b…6eff`, schema snapshot `31dcb2b4…5c7cb67f`, `id_contracts.json` `fc4711ef…ed4682`, WORKFLOW `ee4cd8e1…fcd5d` (all unchanged), same synth-cut clock. Drive/Docs collision checks were re-run fresh against current source bytes (gdrive `data.json` hashed this call, 39,760,628 bytes, verified-id-index; gdocs full scan), and both match the rev 3 results. The 3 changed rows were re-checked NEW in full (A–C).

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, manifest, review version | NEW, done (rev 4) |
| Run lint; resolve every flag | NEW, done on rev 4 (no flags) |
| Inventory every statement and record | NEW diff of all 571 lines; ledger §6 (295 row operations + BEGIN/COMMIT); 3 rows NEW, 292 REUSED from rev 3 report (byte-identical lines) |
| Check A: references and ID collisions | PASS: Drive (42 ids) and Docs (36 ids) collisions NEW; other services REUSED (unchanged rows, unchanged manifest) |
| Check B: SQL structure and schema rules | PASS: 3 changed rows NEW (column/value counts, JSON style runs parse); rest REUSED (provisional snapshot advisories) |
| Check C: dates, relationships and consistency | PASS: changed text and style runs NEW; rest REUSED (advisories) |
| Coverage, findings, limits, one verdict | NEW, done |

## 4. Lint flags and resolutions

On rev 4 the lint returned no FAIL, CHECK or INFO flags (counts FAIL 0, CHECK 0, INFO 0; row counts identical to rev 3) for any check (future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape). Checks A–C below were still run in full. A manual scan for grader-facing words (agent, rubric, grader, decoy, trap, solver, hint, tool call, pass rate) found nothing.

## 5. Checks A–C

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | All new keys are absent from the complete local collections (details below). All referenced parents, actors, channels, boards, lists, members, calendars, teams and users exist and are who the records say. No second accounts. Every Drive file is readable (Docs/Sheets/Slides rows present). |
| B — SQL structure and supported schema rules | PASS | All 297 statements parse; column and value counts match for all 260 INSERTs. Reserved words are quoted (`"desc"`, `"references"`, `"index"`, camelCase Trello columns). No generated columns. Linear text dates use `YYYY-MM-DDTHH:MM:SSZ`; `state_history_json='[]'` is present. JSON shapes match. Provisional snapshot advisories are listed under B-adv. |
| C — Dates, relationships and consistency | PASS | All event timestamps are at or before 2025-10-01 07:00 UTC; only plan values (Jan 5, 2026 review event; vendor deadlines in text) are later. Reply chains, thread snippets, internal_date and headers agree. Facts that build on the base match it. Advisories are listed under C-adv. |

### Check A detail (all NEW, all `scan_complete: true`)

- **Drive (NEW, rev 4):** 42 new ids absent from 53,631 `drive_files` (`lookup gdrive --pointer /drive_files`, scan_complete true, errors []). Docs: 36 doc ids absent from 595 `docs_documents` (`lookup gdocs --key document_id`, scan_complete true, errors []). The items below are REUSED from the rev 3 report (rows byte-identical, manifest unchanged).
- **Drive (rev 3 detail):** 42 new ids absent from 53,631 `drive_files`. Parents `d_175c0d7bc72ed244b944cb` (Frederick's root, /drive_files/2060) and `d_63fffeb4fab5233ed5bb73` (Leonard's root, /drive_files/9030) exist and their owners match. 36 Docs have `docs_documents` rows with non-empty `body_text`. 2 spreadsheets have sheet rows. 2 presentations have pages and elements. 2 are folders. None has a `content_path`, so the content_path contract does not apply.
- **Docs / Sheets / Slides:** new ids absent from 595 docs, 356 spreadsheets and 132 presentations. Children (sheets, 7 pages, 14 elements) reference parents created earlier in the SQL.
- **Slack:** 6 new message ids absent from 610,468 messages (all `messages/*.json`). No `ts` clash in C07C2866011 or D05S58U4SAK. C07C2866011 is `#executives`, with Leonard (`EMPLOYEE_0038`) and Robert (`EMPLOYEE_0016`) as members. D05S58U4SAK contains Leonard and Frederick (`EMPLOYEE_0008`). The UPDATE target `c41d37178fca394c135408d2b38e0879` exists (C07C2866011/2025-09.json /866, Leonard, `reply_count 0`, no existing replies), so `reply_count=1` and `reply_users_count=1` are correct.
- **Trello:** card, 2 actions, checklist and 4 check items are absent from 803 / 5,252 / 54 / 161 records. Board `640643a3fd8f3ca308d9318e` "Harmony Games" (shortLink f4LGcmuh, as in data_json), list `…3196` "Doing", and a "To Do" list on the same board all exist. Member `2162c1ba310341bf318f48b7` is Arthur Blake. idShort 456 is unused (board max 455). Null `shortLink` with the link in `url` follows the base pattern.
- **Gmail:** 47 thread ids and 72 distinct Message-IDs are absent from all 81,404 thread files (full text scan, complete). Mailboxes for Frederick, Leonard, Robert and Arthur exist in `users.json`. Every message id and thread id carries its own mailbox prefix, and each message's thread is inserted in the same mailbox. All 34 thread UPDATEs target threads inserted earlier in the SQL. `history_id` is NULL everywhere (contract OK).
- **Calendar:** 7 event ids and 3 iCal UIDs absent from 10,395 events. All four calendars exist. One shared UID across copies on several calendars matches the base convention (802 of 964 base UIDs are shared).
- **Linear:** `ZOM-567` is absent as id and identifier among 3,687 issues. `team_ZOM` exists. `usr_cc3e90160f490686` is arthur.blake, which fits the comment's "Leonard or I". The base `comments` array is empty, so the comment id cannot collide. `state_id 'Todo'` is a literal state used in the base.
- **Contacts:** 4 contact ids, the emails (`PERSON_2599_EMAIL`, `PERSON_9716/9717/9720_EMAIL`) and the names are absent from 170 contacts, so no duplicates.
- **Identity tokens:** none of the new tokens `PERSON_9701…9735_EMAIL` or `SVC_9701_EMAIL` appears anywhere in base Gmail, Slack users, contacts, gcal, gdocs, gslides, trello or linear. Inside the SQL each token maps to exactly one name. Existing tokens keep their base identities: `PERSON_2694` is the ESG Law partner and `PERSON_2599_EMAIL` is ESG's group intake address (base thread 00015129.json, 2025-08-27). The new contact "ESG Law intake" therefore names the right address.

### Check B detail

- **Changed rows (NEW):** lines 93, 135 and 137 each keep 11 values for 11 columns; `style_runs_json` parses as a JSON list (base shape) in all three; quoting/escaping (`E''` with doubled quotes) is unchanged in form.

- Structure: BEGIN…COMMIT, literal values only, no ON CONFLICT, DELETE or conditional SQL. The UPDATEs use exact-id predicates.
- **B-adv (provisional snapshot, advisory only):** these columns are NOT COVERED by the unverified snapshot: `gslides.slides_pages.notes`, `gslides.slides_page_elements.table_json` and `ordinal`, `linear.linear_comments.sequence`. If the live tables lack them, those INSERTs would be rejected. This is not a demonstrated defect under Eval 0 or the schema README. Every other inserted column matches the snapshot.

### Check C detail

- **Changed rows (NEW):**
  - Line 93, `f_b98287f6f80fe431a71209` (Leonard's guardrails doc, created/modified 2025-09-26): body now says parked items come back "at the January commitments review **I'll put on our calendars**" (twice). This is forward-looking. The four "Q4 commitments review" events (Jan 5, 2026 17:00Z, a Monday in the first week of January) are organized and created by leonard.hayes on 2025-09-29T18:00Z, after the doc, so the doc author does what the doc promises. **This resolves rev 3's advisory C-adv 1.** Body is 1,393 chars; style runs 0–35 TITLE, 35–198, 198–212 H2 "How to decide", 212–1278, 1278–1286 H2 "Answers", 1286–1393: contiguous, start at 0, end at body length, and each heading run covers exactly its heading line.
  - Line 135, `f_71a95593c736b3baf45f91` (Markward terms): TITLE run is now 0–43 = "Markward - Free Tier Terms (click-through)\n", body run 43–215 = end of text. Line 137, `f_9a7fc4a3e45e4394227fa5` (Playfuse NDA): TITLE run 0–56 = "Playfuse - Mutual NDA (Harmony Games template, ESG Law)\n", body run 56–218 = end of text. **This resolves rev 3's advisory C-adv 4.** The text of both docs is unchanged from rev 3.
  - All 36 injected Docs were re-checked: every style-run set starts at 0, is contiguous, ends at the body length, and every TITLE run covers exactly the first line.
  - No dates, ids, owners or shares changed in any row, so the clock check and the rest of the cross-record checks below carry over unchanged.
- **Below: REUSED from the rev 3 report (byte-identical rows).**

- **Clock:** latest event timestamp is 2025-09-30T23:20:00Z (Leonard's hand-off email). Calendar `created/updated`, Slack `ts`/`created_at` (all six agree to the microsecond), Drive/Docs times, Trello action dates (and ObjectId timestamps), and Linear created/updated are all before the clock.
- **Gmail:** for all 81 rows, `internal_date` equals `date`; Date, Subject, Message-ID, From, To, Cc, In-Reply-To and References headers match the columns; snippets match the body start; sender copies are SENT and recipient copies INBOX. Every reply's parent is in the same thread and earlier, with a "Re:" subject. Each thread's final snippet equals its latest message. All copies of a message are identical. Calendar invitations go one per invitee (not the organizer), as Google does. Invite text times match the events (Jan 5 2026 09:00 PST = 17:00Z, 12:00 EST for Arthur; Sep 17 11:00 PDT = 18:00Z).
- **Attachment timing:** each vendor document's Drive `created_time` is 10–15 minutes after the email that sends it. Prices, dates and terms in each doc match its email (e.g. Pixel Harbor $4,800 / $2,400 deposit by Oct 10; Lingora $2,640, valid to Oct 3; Soundvault $1,188, valid to Oct 15; Clipforge 20-video cap → Paylane notice Oct 15/16 at $1,800). The Jul 31 tracker matches the pilot agreement and booth quote.
- **Fit with base:** Leonard "in LA from tomorrow for Dentsu" matches base Slack (C07C2866011 2025-09 /1009, "come to LA on Oct 1st for the Dentsu in person meeting") and the base Oct 1 20:30Z Dentsu events. Linear "Fred registered … on Sep 4 … $400-500 per kit" matches Frederick's base #executives post 1757011319.449149 (2025-09-04). The tracker line "Singular … quarterly billing on Jul 17" fits base Slack (Jul 8 plan to ask; Jul 24 "restructure Singular payments to quarterly"). "#executives on Monday" resolves to the injected Sep 29 post. Corrections (Leonard's Jul 22 "under $500" message replaced by the Sep 25 ESG reply; Sep 29 travel-cost change; Framewell hold to Feb 1) are later, dated and attributed, so they are valid superseding records, not contradictions.
- **Known base issues:** no injected record builds on a Snowflake or Confluence conflict. The UA-buckets doc names adjoe but no install, spend or payment figure (SC-1/SC-4 not used).
- **C-adv (advisories, not defects):**
  1. *(Resolved in rev 4, kept for history.)* In rev 3 the guardrails doc (created and modified 2025-09-26) said parked items return "at the January commitments review on our calendars", but the calendar events and invites were created 2025-09-29. A forward-looking reading is possible. To remove the gap, set the events' `created`/`updated` and the invite emails to ≤ 2025-09-26T16:00Z, or move the doc's `modified_time` to ≥ 2025-09-29T18:00Z.
  2. Sequence numbers out of creation order: `ZOM-567` is created 2025-09-23T17:00Z, but base ZOM-564/565/566 were created Sep 24–30. Trello idShort 456 is created 2025-08-12, but base cards 452–455 were created Aug 13–Sep 13. The base itself has 6 ZOM inversions, and neither field has a listed ID contract, so this is not a finding. It could be tidied by dating the issue after 2025-09-30T16:26:02Z (it can't be: its comment is Sep 25) or by accepting it as is.
  3. Emails say "attached", but `attachments_meta_json` is `[]`. The documents live in Drive ("Vendor & partner paperwork"). This is a realism note only.
  4. *(Resolved in rev 4.)* In rev 3 the Markward and Playfuse Docs' TITLE style runs covered fewer characters than the first line.

## 6. Operation ledger (every row; base/SQL check per row)

Rows #43, #64 and #65 are NEW for rev 4; Drive rows #1–42 and all Docs rows had their collision checks re-run NEW; every other row's result is REUSED from the rev 3 review (identical SQL line, unchanged universe manifest and references).

BEGIN (line 5) … COMMIT (end): one transaction.

| # | Line | Table | Op | Record / target | Key values | Base check | Result |
|---|---|---|---|---|---|---|---|
| 1 | 7 | gdrive.drive_files | INSERT | `f_b98287f6f80fe431a71209` | document; parent d_63fffeb4fab5233ed5bb73; owner leonard.hayes; created 2025-09-26T16:00:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 2 | 9 | gdrive.drive_files | INSERT | `f_7bacf15c4e8eea1a52dcd4` | document; parent d_175c0d7bc72ed244b944cb; owner frederick.stone; created 2025-09-16T17:00:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 3 | 11 | gdrive.drive_files | INSERT | `f_3b06917a41dd59308d890b` | document; parent d_63fffeb4fab5233ed5bb73; owner leonard.hayes; created 2025-09-25T16:20:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 4 | 13 | gdrive.drive_files | INSERT | `d_80a8c04753ba82ba4ba6a5` | folder; parent d_175c0d7bc72ed244b944cb; owner frederick.stone; created 2025-09-29T20:00:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 5 | 15 | gdrive.drive_files | INSERT | `f_846ddc38b2aab3d2ed3fcb` | document; parent d_80a8c04753ba82ba4ba6a5; owner leonard.hayes; created 2025-09-30T22:40:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 6 | 17 | gdrive.drive_files | INSERT | `f_05f0a451b29b19a1c0b90f` | spreadsheet; parent d_80a8c04753ba82ba4ba6a5; owner leonard.hayes; created 2025-09-30T22:45:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 7 | 19 | gdrive.drive_files | INSERT | `f_9d6edd4922d8130ccd272e` | spreadsheet; parent d_175c0d7bc72ed244b944cb; owner frederick.stone; created 2025-07-31T21:00:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 8 | 21 | gdrive.drive_files | INSERT | `d_ffa3e6e473da7e6523614f` | folder; parent d_175c0d7bc72ed244b944cb; owner frederick.stone; created 2025-06-18T17:40:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 9 | 23 | gdrive.drive_files | INSERT | `f_fba21c2d5d4bbb02983961` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-18T16:20:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 10 | 25 | gdrive.drive_files | INSERT | `f_6c212cbfb31c3ded44ef8a` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-24T15:30:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 11 | 27 | gdrive.drive_files | INSERT | `f_8d0e0e3ae076b2f745e7e2` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-07-08T18:30:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 12 | 29 | gdrive.drive_files | INSERT | `f_614f88a28a2f0cf1b88408` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-06-18T17:45:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 13 | 31 | gdrive.drive_files | INSERT | `f_5dbbaf5b251d5261427eb1` | presentation; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-09T15:45:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 14 | 33 | gdrive.drive_files | INSERT | `f_9d4639f91c93478d888f4b` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-08-29T17:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 15 | 35 | gdrive.drive_files | INSERT | `f_2686da1086bfcc2fba3f57` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-09T15:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 16 | 37 | gdrive.drive_files | INSERT | `f_4bdfb8e0c47288087c7bba` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-19T17:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 17 | 39 | gdrive.drive_files | INSERT | `f_5b961c9c6887d31dcd2ee2` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-11T20:15:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 18 | 41 | gdrive.drive_files | INSERT | `f_34ba4ac9a0f0fa4fd34e9e` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-03T09:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 19 | 43 | gdrive.drive_files | INSERT | `f_41a9ea5036a231989745b2` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-04T17:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 20 | 45 | gdrive.drive_files | INSERT | `f_a9593b0bf23b760e2972c7` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-08-21T16:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 21 | 47 | gdrive.drive_files | INSERT | `f_54c2b4e172bb73a4a19845` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-17T19:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 22 | 49 | gdrive.drive_files | INSERT | `f_2715771ae5f0358ad39aa9` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-22T16:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 23 | 51 | gdrive.drive_files | INSERT | `f_cfb172dea30b9f6ac8a340` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-23T15:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 24 | 53 | gdrive.drive_files | INSERT | `f_6252955f500f81e3aacbef` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-10T16:40:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 25 | 55 | gdrive.drive_files | INSERT | `f_a227b14f03e12005fe8324` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-11T18:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 26 | 57 | gdrive.drive_files | INSERT | `f_9d1e0270574584de0eb92c` | presentation; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-16T17:40:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 27 | 59 | gdrive.drive_files | INSERT | `f_2ae7e3ee3220b628391234` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-19T16:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 28 | 61 | gdrive.drive_files | INSERT | `f_71a95593c736b3baf45f91` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-09T16:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 29 | 63 | gdrive.drive_files | INSERT | `f_9a7fc4a3e45e4394227fa5` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-25T17:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 30 | 65 | gdrive.drive_files | INSERT | `f_f7902fdbb11a8bbd623959` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-08-05T16:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 31 | 67 | gdrive.drive_files | INSERT | `f_f6701704e5659b05d9530f` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-16T08:40:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 32 | 69 | gdrive.drive_files | INSERT | `f_eb94c65ce9f273c6b5a579` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-12T17:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 33 | 71 | gdrive.drive_files | INSERT | `f_68e288146ba0eee9fc17fa` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-18T17:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 34 | 73 | gdrive.drive_files | INSERT | `f_a9bb79c86b8b7b92083785` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-11T16:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 35 | 75 | gdrive.drive_files | INSERT | `f_be21bac5d50e291ebfbe2b` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-15T16:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 36 | 77 | gdrive.drive_files | INSERT | `f_af809bf6325b452edc8476` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-03T17:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 37 | 79 | gdrive.drive_files | INSERT | `f_6d13a63be892a29f796b78` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-19T16:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 38 | 81 | gdrive.drive_files | INSERT | `f_e916ab7563891481ab3b16` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-23T16:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 39 | 83 | gdrive.drive_files | INSERT | `f_6963d4d30aceef4f88966a` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-08T16:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 40 | 85 | gdrive.drive_files | INSERT | `f_17878d7b82fafcee79bfe7` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-25T16:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 41 | 87 | gdrive.drive_files | INSERT | `f_e81c6ef89513cac632700a` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-15T16:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 42 | 89 | gdrive.drive_files | INSERT | `f_9d9cf4e53b1c8607f9c869` | document; parent d_ffa3e6e473da7e6523614f; owner frederick.stone; created 2025-09-08T16:10:00Z | id absent of 53,631 drive_files; parent folder exists | OK |
| 43 | 92 | gdocs.docs_documents | INSERT | `f_b98287f6f80fe431a71209` | drive_file_id same; body 1393 chars (rev 4 wording "I'll put on our calendars"); style runs end 1393; created 2025-09-26T16:00:00Z | NEW: id absent of 595 docs; drive row in SQL; runs contiguous | OK |
| 44 | 94 | gdocs.docs_documents | INSERT | `f_7bacf15c4e8eea1a52dcd4` | drive_file_id same; body 391 chars; created 2025-09-16T17:00:00Z | id absent of 595 docs; drive row in SQL | OK |
| 45 | 96 | gdocs.docs_documents | INSERT | `f_3b06917a41dd59308d890b` | drive_file_id same; body 340 chars; created 2025-09-25T16:20:00Z | id absent of 595 docs; drive row in SQL | OK |
| 46 | 98 | gdocs.docs_documents | INSERT | `f_846ddc38b2aab3d2ed3fcb` | drive_file_id same; body 731 chars; created 2025-09-30T22:40:00Z | id absent of 595 docs; drive row in SQL | OK |
| 47 | 100 | gdocs.docs_documents | INSERT | `f_fba21c2d5d4bbb02983961` | drive_file_id same; body 301 chars; created 2025-09-18T16:20:00Z | id absent of 595 docs; drive row in SQL | OK |
| 48 | 102 | gdocs.docs_documents | INSERT | `f_6c212cbfb31c3ded44ef8a` | drive_file_id same; body 336 chars; created 2025-09-24T15:30:00Z | id absent of 595 docs; drive row in SQL | OK |
| 49 | 104 | gdocs.docs_documents | INSERT | `f_8d0e0e3ae076b2f745e7e2` | drive_file_id same; body 445 chars; created 2025-07-08T18:30:00Z | id absent of 595 docs; drive row in SQL | OK |
| 50 | 106 | gdocs.docs_documents | INSERT | `f_614f88a28a2f0cf1b88408` | drive_file_id same; body 271 chars; created 2025-06-18T17:45:00Z | id absent of 595 docs; drive row in SQL | OK |
| 51 | 108 | gdocs.docs_documents | INSERT | `f_9d4639f91c93478d888f4b` | drive_file_id same; body 222 chars; created 2025-08-29T17:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 52 | 110 | gdocs.docs_documents | INSERT | `f_2686da1086bfcc2fba3f57` | drive_file_id same; body 176 chars; created 2025-09-09T15:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 53 | 112 | gdocs.docs_documents | INSERT | `f_4bdfb8e0c47288087c7bba` | drive_file_id same; body 230 chars; created 2025-09-19T17:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 54 | 114 | gdocs.docs_documents | INSERT | `f_5b961c9c6887d31dcd2ee2` | drive_file_id same; body 198 chars; created 2025-09-11T20:15:00Z | id absent of 595 docs; drive row in SQL | OK |
| 55 | 116 | gdocs.docs_documents | INSERT | `f_34ba4ac9a0f0fa4fd34e9e` | drive_file_id same; body 212 chars; created 2025-09-03T09:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 56 | 118 | gdocs.docs_documents | INSERT | `f_41a9ea5036a231989745b2` | drive_file_id same; body 177 chars; created 2025-09-04T17:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 57 | 120 | gdocs.docs_documents | INSERT | `f_a9593b0bf23b760e2972c7` | drive_file_id same; body 207 chars; created 2025-08-21T16:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 58 | 122 | gdocs.docs_documents | INSERT | `f_54c2b4e172bb73a4a19845` | drive_file_id same; body 283 chars; created 2025-09-17T19:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 59 | 124 | gdocs.docs_documents | INSERT | `f_2715771ae5f0358ad39aa9` | drive_file_id same; body 170 chars; created 2025-09-22T16:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 60 | 126 | gdocs.docs_documents | INSERT | `f_cfb172dea30b9f6ac8a340` | drive_file_id same; body 143 chars; created 2025-09-23T15:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 61 | 128 | gdocs.docs_documents | INSERT | `f_6252955f500f81e3aacbef` | drive_file_id same; body 202 chars; created 2025-09-10T16:40:00Z | id absent of 595 docs; drive row in SQL | OK |
| 62 | 130 | gdocs.docs_documents | INSERT | `f_a227b14f03e12005fe8324` | drive_file_id same; body 161 chars; created 2025-09-11T18:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 63 | 132 | gdocs.docs_documents | INSERT | `f_2ae7e3ee3220b628391234` | drive_file_id same; body 202 chars; created 2025-09-19T16:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 64 | 134 | gdocs.docs_documents | INSERT | `f_71a95593c736b3baf45f91` | drive_file_id same; body 215 chars; TITLE run 0–43 (rev 4); created 2025-09-09T16:10:00Z | NEW: id absent of 595 docs; drive row in SQL; runs contiguous | OK |
| 65 | 136 | gdocs.docs_documents | INSERT | `f_9a7fc4a3e45e4394227fa5` | drive_file_id same; body 218 chars; TITLE run 0–56 (rev 4); created 2025-09-25T17:10:00Z | NEW: id absent of 595 docs; drive row in SQL; runs contiguous | OK |
| 66 | 138 | gdocs.docs_documents | INSERT | `f_f7902fdbb11a8bbd623959` | drive_file_id same; body 142 chars; created 2025-08-05T16:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 67 | 140 | gdocs.docs_documents | INSERT | `f_f6701704e5659b05d9530f` | drive_file_id same; body 150 chars; created 2025-09-16T08:40:00Z | id absent of 595 docs; drive row in SQL | OK |
| 68 | 142 | gdocs.docs_documents | INSERT | `f_eb94c65ce9f273c6b5a579` | drive_file_id same; body 142 chars; created 2025-09-12T17:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 69 | 144 | gdocs.docs_documents | INSERT | `f_68e288146ba0eee9fc17fa` | drive_file_id same; body 129 chars; created 2025-09-18T17:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 70 | 146 | gdocs.docs_documents | INSERT | `f_a9bb79c86b8b7b92083785` | drive_file_id same; body 151 chars; created 2025-09-11T16:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 71 | 148 | gdocs.docs_documents | INSERT | `f_be21bac5d50e291ebfbe2b` | drive_file_id same; body 144 chars; created 2025-09-15T16:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 72 | 150 | gdocs.docs_documents | INSERT | `f_af809bf6325b452edc8476` | drive_file_id same; body 89 chars; created 2025-09-03T17:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 73 | 152 | gdocs.docs_documents | INSERT | `f_6d13a63be892a29f796b78` | drive_file_id same; body 119 chars; created 2025-09-19T16:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 74 | 154 | gdocs.docs_documents | INSERT | `f_e916ab7563891481ab3b16` | drive_file_id same; body 124 chars; created 2025-09-23T16:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 75 | 156 | gdocs.docs_documents | INSERT | `f_6963d4d30aceef4f88966a` | drive_file_id same; body 112 chars; created 2025-09-08T16:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 76 | 158 | gdocs.docs_documents | INSERT | `f_17878d7b82fafcee79bfe7` | drive_file_id same; body 136 chars; created 2025-09-25T16:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 77 | 160 | gdocs.docs_documents | INSERT | `f_e81c6ef89513cac632700a` | drive_file_id same; body 116 chars; created 2025-09-15T16:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 78 | 162 | gdocs.docs_documents | INSERT | `f_9d9cf4e53b1c8607f9c869` | drive_file_id same; body 75 chars; created 2025-09-08T16:10:00Z | id absent of 595 docs; drive row in SQL | OK |
| 79 | 165 | gsheets.sheets_spreadsheets | INSERT | `f_05f0a451b29b19a1c0b90f` | drive_file_id same; created 2025-09-30T22:45:00Z | id absent of 356 spreadsheets; drive row in SQL | OK |
| 80 | 167 | gsheets.sheets_sheets | INSERT | `f_05f0a451b29b19a1c0b90f` | sheet_id 0 'Log'; 1 rows | parent spreadsheet in SQL | OK |
| 81 | 169 | gsheets.sheets_spreadsheets | INSERT | `f_9d6edd4922d8130ccd272e` | drive_file_id same; created 2025-07-31T21:00:00Z | id absent of 356 spreadsheets; drive row in SQL | OK |
| 82 | 171 | gsheets.sheets_sheets | INSERT | `f_9d6edd4922d8130ccd272e` | sheet_id 0 'Tracker'; 6 rows | parent spreadsheet in SQL | OK |
| 83 | 174 | gslides.slides_presentations | INSERT | `f_5dbbaf5b251d5261427eb1` | drive_file_id same; created 2025-09-09T15:45:00Z | id absent of 132 presentations; drive row in SQL | OK |
| 84 | 176 | gslides.slides_pages | INSERT | `f_5dbbaf5b251d5261427eb1` | pres 427eb1; index 0 | parent presentation in SQL | OK |
| 85 | 178 | gslides.slides_page_elements | INSERT | `f_5dbbaf5b251d5261427eb1` | page slide_bd9e4b92fdc9; TITLE | parent page in SQL | OK |
| 86 | 180 | gslides.slides_page_elements | INSERT | `f_5dbbaf5b251d5261427eb1` | page slide_bd9e4b92fdc9; BODY | parent page in SQL | OK |
| 87 | 182 | gslides.slides_pages | INSERT | `f_5dbbaf5b251d5261427eb1` | pres 427eb1; index 1 | parent presentation in SQL | OK |
| 88 | 184 | gslides.slides_page_elements | INSERT | `f_5dbbaf5b251d5261427eb1` | page slide_e799ff88ca1a; TITLE | parent page in SQL | OK |
| 89 | 186 | gslides.slides_page_elements | INSERT | `f_5dbbaf5b251d5261427eb1` | page slide_e799ff88ca1a; BODY | parent page in SQL | OK |
| 90 | 188 | gslides.slides_pages | INSERT | `f_5dbbaf5b251d5261427eb1` | pres 427eb1; index 2 | parent presentation in SQL | OK |
| 91 | 190 | gslides.slides_page_elements | INSERT | `f_5dbbaf5b251d5261427eb1` | page slide_07d1f58819b2; TITLE | parent page in SQL | OK |
| 92 | 192 | gslides.slides_page_elements | INSERT | `f_5dbbaf5b251d5261427eb1` | page slide_07d1f58819b2; BODY | parent page in SQL | OK |
| 93 | 194 | gslides.slides_presentations | INSERT | `f_9d1e0270574584de0eb92c` | drive_file_id same; created 2025-09-16T17:40:00Z | id absent of 132 presentations; drive row in SQL | OK |
| 94 | 196 | gslides.slides_pages | INSERT | `f_9d1e0270574584de0eb92c` | pres 0eb92c; index 0 | parent presentation in SQL | OK |
| 95 | 198 | gslides.slides_page_elements | INSERT | `f_9d1e0270574584de0eb92c` | page slide_3818928cc5b4; TITLE | parent page in SQL | OK |
| 96 | 200 | gslides.slides_page_elements | INSERT | `f_9d1e0270574584de0eb92c` | page slide_3818928cc5b4; BODY | parent page in SQL | OK |
| 97 | 202 | gslides.slides_pages | INSERT | `f_9d1e0270574584de0eb92c` | pres 0eb92c; index 1 | parent presentation in SQL | OK |
| 98 | 204 | gslides.slides_page_elements | INSERT | `f_9d1e0270574584de0eb92c` | page slide_111fef17ef5d; TITLE | parent page in SQL | OK |
| 99 | 206 | gslides.slides_page_elements | INSERT | `f_9d1e0270574584de0eb92c` | page slide_111fef17ef5d; BODY | parent page in SQL | OK |
| 100 | 208 | gslides.slides_pages | INSERT | `f_9d1e0270574584de0eb92c` | pres 0eb92c; index 2 | parent presentation in SQL | OK |
| 101 | 210 | gslides.slides_page_elements | INSERT | `f_9d1e0270574584de0eb92c` | page slide_52be557fc2cd; TITLE | parent page in SQL | OK |
| 102 | 212 | gslides.slides_page_elements | INSERT | `f_9d1e0270574584de0eb92c` | page slide_52be557fc2cd; BODY | parent page in SQL | OK |
| 103 | 214 | gslides.slides_pages | INSERT | `f_9d1e0270574584de0eb92c` | pres 0eb92c; index 3 | parent presentation in SQL | OK |
| 104 | 216 | gslides.slides_page_elements | INSERT | `f_9d1e0270574584de0eb92c` | page slide_2961165dab03; TITLE | parent page in SQL | OK |
| 105 | 218 | gslides.slides_page_elements | INSERT | `f_9d1e0270574584de0eb92c` | page slide_2961165dab03; BODY | parent page in SQL | OK |
| 106 | 221 | slack.slack_messages | INSERT | `0573efd133cabdb1acde61e68571aa82` | C07C2866011; user EMPLOYEE_0038_SLACK_ID; ts 1753207800.603298 | id absent of 610,468 msgs; no ts clash; author is channel member | OK |
| 107 | 223 | slack.slack_messages | INSERT | `80ced6c98e9bd0aa1ccb462488f1746d` | C07C2866011; user EMPLOYEE_0016_SLACK_ID; ts 1758819840.884370 | id absent of 610,468 msgs; no ts clash; author is channel member | OK |
| 108 | 225 | slack.slack_messages | INSERT | `fc2f69c06b333f6c54dfd63d455c3958` | C07C2866011; user EMPLOYEE_0016_SLACK_ID; ts 1758134460.899858 | id absent of 610,468 msgs; no ts clash; author is channel member | OK |
| 109 | 227 | slack.slack_messages | INSERT | `7e88911312fa9a969f0659a105af59a3` | C07C2866011; user EMPLOYEE_0038_SLACK_ID; ts 1759166100.370044 | id absent of 610,468 msgs; no ts clash; author is channel member | OK |
| 110 | 229 | slack.slack_messages | INSERT | `9fb2d23420c7e01ca163571f4129c912` | C07C2866011; user EMPLOYEE_0038_SLACK_ID; ts 1758920520.674991; reply to c41d37178fca394c135408d2b38e0879 | id absent of 610,468 msgs; no ts clash; author is channel member | OK |
| 111 | 231 | slack.slack_messages | UPDATE | `c41d37178fca394c135408d2b38e0879` | SET reply_count=1, reply_users_count=1, latest_reply=1758920520.674991, thread_ts_legacy=1758513190.847889 | Parent exists C07C2866011/2025-09.json /866 (Leonard; reply_count 0) | OK |
| 112 | 232 | slack.slack_messages | INSERT | `418a0a6d6c29b7b67ce0ffb270c78c1e` | D05S58U4SAK; user EMPLOYEE_0038_SLACK_ID; ts 1759174260.052645 | id absent of 610,468 msgs; no ts clash; author is channel member | OK |
| 113 | 235 | trello.trello_cards | INSERT | `689b662c60cbe40b9f4a97ae` | board ...318e list Doing (...3196); idShort 456; member Arthur | id/idShort 456 free (board max 455); board/list/member exist | OK |
| 114 | 237 | trello.trello_actions | INSERT | `689b662ce06ba74821d997f4` | createCard 2025-08-12T16:05:00Z; creator Arthur | id absent of 5,252 actions; card in SQL | OK |
| 115 | 239 | trello.trello_checklists | INSERT | `689b66a4b56c4354aa1efab8` | card ...97ae | id absent of 54 | OK |
| 116 | 241 | trello.trello_check_items | INSERT | `689b66a46f62e8218a32924c` | 'Vaultline nightly DB backups' | id absent of 161 | OK |
| 117 | 243 | trello.trello_check_items | INSERT | `689b66a49d4295a2b3145041` | 'Certwell SSL cert for the API domain' | id absent of 161 | OK |
| 118 | 245 | trello.trello_check_items | INSERT | `689b66a450734c26dcdf6291` | 'the night pager for backend outages (wha' | id absent of 161 | OK |
| 119 | 247 | trello.trello_check_items | INSERT | `689b66a4c5bb6c266c1cedba` | 'App Store and Google Play developer acco' | id absent of 161 | OK |
| 120 | 249 | trello.trello_actions | INSERT | `689b66a48cfc5e5bd6608131` | addChecklistToCard 2025-08-12T16:07:00Z; creator Arthur | id absent of 5,252 actions; card in SQL | OK |
| 121 | 252 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844732913254784171` | user frederick.stone; history_id NULL | GMAILT | OK |
| 122 | 254 | gmail.gmail_messages | INSERT | `frederick.stone/<CAlIXcq3nWlSRBAZONcbY…` | frederick.stone; 2025-09-30T23:20:00Z; from leonard.hayes@harmonygames.co; 'Vendor and partner stuff while I'm in LA' | GMAILM | OK |
| 123 | 256 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844732913254960629` | user leonard.hayes; history_id NULL | GMAILT | OK |
| 124 | 258 | gmail.gmail_messages | INSERT | `leonard.hayes/<CAlIXcq3nWlSRBAZONcbY…` | leonard.hayes; 2025-09-30T23:20:00Z; from leonard.hayes@harmonygames.co; 'Vendor and partner stuff while I'm in LA' | GMAILM | OK |
| 125 | 260 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844177063117059830` | user frederick.stone; history_id NULL | GMAILT | OK |
| 126 | 262 | gmail.gmail_messages | INSERT | `frederick.stone/<CAyKP29rjypyVF_dZsTX0…` | frederick.stone; 2025-09-24T20:05:00Z; from PERSON_2694_EMAIL; 'Signing and review for Harmony Games agr' | GMAILM | OK |
| 127 | 264 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844177063117003267` | user leonard.hayes; history_id NULL | GMAILT | OK |
| 128 | 266 | gmail.gmail_messages | INSERT | `leonard.hayes/<CAyKP29rjypyVF_dZsTX0…` | leonard.hayes; 2025-09-24T20:05:00Z; from PERSON_2694_EMAIL; 'Signing and review for Harmony Games agr' | GMAILM | OK |
| 129 | 268 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844177063117516849` | user robert; history_id NULL | GMAILT | OK |
| 130 | 270 | gmail.gmail_messages | INSERT | `robert/<CAyKP29rjypyVF_dZsTX0…` | robert; 2025-09-24T20:05:00Z; from PERSON_2694_EMAIL; 'Signing and review for Harmony Games agr' | GMAILM | OK |
| 131 | 272 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844177063117181908` | user arthur.blake; history_id NULL | GMAILT | OK |
| 132 | 274 | gmail.gmail_messages | INSERT | `arthur.blake/<CAyKP29rjypyVF_dZsTX0…` | arthur.blake; 2025-09-24T20:05:00Z; from PERSON_2694_EMAIL; 'Signing and review for Harmony Games agr' | GMAILM | OK |
| 133 | 276 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1844177063117059830` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 134 | 277 | gmail.gmail_messages | INSERT | `frederick.stone/<CAyZDYLgzExhQkAm-LGcR…` | frederick.stone; 2025-09-25T16:30:00Z; from leonard.hayes@harmonygames.co; 'Re: Signing and review for Harmony Games' | GMAILM | OK |
| 135 | 279 | gmail.gmail_threads | UPDATE | `leonard.hayes@harmonygames.co/1844177063117003267` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 136 | 280 | gmail.gmail_messages | INSERT | `leonard.hayes/<CAyZDYLgzExhQkAm-LGcR…` | leonard.hayes; 2025-09-25T16:30:00Z; from leonard.hayes@harmonygames.co; 'Re: Signing and review for Harmony Games' | GMAILM | OK |
| 137 | 282 | gmail.gmail_threads | UPDATE | `robert@harmonygames.co/1844177063117516849` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 138 | 283 | gmail.gmail_messages | INSERT | `robert/<CAyZDYLgzExhQkAm-LGcR…` | robert; 2025-09-25T16:30:00Z; from leonard.hayes@harmonygames.co; 'Re: Signing and review for Harmony Games' | GMAILM | OK |
| 139 | 285 | gmail.gmail_threads | UPDATE | `arthur.blake@harmonygames.co/1844177063117181908` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 140 | 286 | gmail.gmail_messages | INSERT | `arthur.blake/<CAyZDYLgzExhQkAm-LGcR…` | arthur.blake; 2025-09-25T16:30:00Z; from leonard.hayes@harmonygames.co; 'Re: Signing and review for Harmony Games' | GMAILM | OK |
| 141 | 288 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843067564852153540` | user frederick.stone; history_id NULL | GMAILT | OK |
| 142 | 290 | gmail.gmail_messages | INSERT | `frederick.stone/<CAYV6MxN9j-x1B7nyXxQQ…` | frederick.stone; 2025-09-12T14:10:00Z; from SVC_9701_EMAIL; 'Workspace HG-2291: your pilot is ending' | GMAILM | OK |
| 143 | 292 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843618067251203081` | user frederick.stone; history_id NULL | GMAILT | OK |
| 144 | 294 | gmail.gmail_messages | INSERT | `frederick.stone/<CAGJkuaxoKn_J2zxTzhLs…` | frederick.stone; 2025-09-18T16:00:00Z; from PERSON_9701_EMAIL; 'Framewell Pro for Harmony Games' | GMAILM | OK |
| 145 | 296 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844157874176168845` | user frederick.stone; history_id NULL | GMAILT | OK |
| 146 | 298 | gmail.gmail_messages | INSERT | `frederick.stone/<CAZgisbRwHgHd3Hk_E9LY…` | frederick.stone; 2025-09-24T15:00:00Z; from PERSON_9703_EMAIL; 'Your Pingwise Starter tier ends Oct 31' | GMAILM | OK |
| 147 | 300 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1837102635418059486` | user frederick.stone; history_id NULL | GMAILT | OK |
| 148 | 302 | gmail.gmail_messages | INSERT | `frederick.stone/<CAyIhcf4XSg_rUt0eT-St…` | frederick.stone; 2025-07-08T18:00:00Z; from PERSON_9704_EMAIL; 'Clipforge UGC Studio pilot - welcome' | GMAILM | OK |
| 149 | 304 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1837102635418059486` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 150 | 305 | gmail.gmail_messages | INSERT | `frederick.stone/<CAFEbdSLTqGx4K9ylCWMj…` | frederick.stone; 2025-09-22T17:30:00Z; from PERSON_9704_EMAIL; 'Re: Clipforge UGC Studio pilot - welcome' | GMAILM | OK |
| 151 | 307 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1835288808653226583` | user frederick.stone; history_id NULL | GMAILT | OK |
| 152 | 309 | gmail.gmail_messages | INSERT | `frederick.stone/<CAC1R0eFyTK7ezriX3kHg…` | frederick.stone; 2025-06-18T17:30:00Z; from PERSON_9705_EMAIL; 'Booth hold - Bay Area Indie Showcase, Oc' | GMAILM | OK |
| 153 | 311 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1835288808653226583` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 154 | 312 | gmail.gmail_messages | INSERT | `frederick.stone/<CALCA8gxcwd0yOaLVGO1K…` | frederick.stone; 2025-06-19T16:10:00Z; from frederick.stone@harmonygames.co; 'Re: Booth hold - Bay Area Indie Showcase' | GMAILM | OK |
| 155 | 314 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842800807116855774` | user frederick.stone; history_id NULL | GMAILT | OK |
| 156 | 316 | gmail.gmail_messages | INSERT | `frederick.stone/<CAUTttDNR2kwXReKZgzK8…` | frederick.stone; 2025-09-09T15:30:00Z; from PERSON_9702_EMAIL; 'Lanternfly x Harmony Games: Southeast As' | GMAILM | OK |
| 157 | 318 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842800807116855774` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 158 | 319 | gmail.gmail_messages | INSERT | `frederick.stone/<CAY11pXWEb2u5uCxBJhKp…` | frederick.stone; 2025-09-10T17:05:00Z; from frederick.stone@harmonygames.co; 'Re: Lanternfly x Harmony Games: Southeas' | GMAILM | OK |
| 159 | 321 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842800807116855774` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 160 | 322 | gmail.gmail_messages | INSERT | `frederick.stone/<CArrsRpTwnF5vDz3j8sB1…` | frederick.stone; 2025-09-22T08:40:00Z; from PERSON_9702_EMAIL; 'Re: Lanternfly x Harmony Games: Southeas' | GMAILM | OK |
| 161 | 324 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1841809902797646290` | user frederick.stone; history_id NULL | GMAILT | OK |
| 162 | 326 | gmail.gmail_messages | INSERT | `frederick.stone/<CA0uGW7WigxQ0mENWo-aI…` | frederick.stone; 2025-08-29T17:00:00Z; from PERSON_9706_EMAIL; 'Brightlane x Harmony Games - creative re' | GMAILM | OK |
| 163 | 328 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1841809902797646290` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 164 | 329 | gmail.gmail_messages | INSERT | `frederick.stone/<CA-xgF65XCwo6QXURZM_e…` | frederick.stone; 2025-09-26T16:20:00Z; from PERSON_9706_EMAIL; 'Re: Brightlane x Harmony Games - creativ' | GMAILM | OK |
| 165 | 331 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842719647334876669` | user frederick.stone; history_id NULL | GMAILT | OK |
| 166 | 333 | gmail.gmail_messages | INSERT | `frederick.stone/<CAdDglIne-JLPfhnQyZF8…` | frederick.stone; 2025-09-08T18:00:00Z; from frederick.stone@harmonygames.co; 'Music licence for Zombie Match 3D traile' | GMAILM | OK |
| 167 | 335 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842719647334876669` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 168 | 336 | gmail.gmail_messages | INSERT | `frederick.stone/<CAeW3ux2LavW4Rp-PXhOt…` | frederick.stone; 2025-09-09T15:00:00Z; from PERSON_9707_EMAIL; 'Re: Music licence for Zombie Match 3D tr' | GMAILM | OK |
| 169 | 338 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842719647334876669` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 170 | 339 | gmail.gmail_messages | INSERT | `frederick.stone/<CAa-jv7GWQa7i06XwUWtN…` | frederick.stone; 2025-09-25T16:00:00Z; from PERSON_9707_EMAIL; 'Re: Music licence for Zombie Match 3D tr' | GMAILM | OK |
| 171 | 341 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843712439092112354` | user frederick.stone; history_id NULL | GMAILT | OK |
| 172 | 343 | gmail.gmail_messages | INSERT | `frederick.stone/<CAN4G0SGg1BdZ4ApKmfoi…` | frederick.stone; 2025-09-19T17:00:00Z; from PERSON_9708_EMAIL; 'Your Reviewly trial has started' | GMAILM | OK |
| 173 | 345 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1843712439092112354` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 174 | 346 | gmail.gmail_messages | INSERT | `frederick.stone/<CAEcTJxNSlNWdzmdlv0uA…` | frederick.stone; 2025-09-29T15:30:00Z; from PERSON_9708_EMAIL; 'Re: Your Reviewly trial has started' | GMAILM | OK |
| 175 | 348 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842998987980893279` | user frederick.stone; history_id NULL | GMAILT | OK |
| 176 | 350 | gmail.gmail_messages | INSERT | `frederick.stone/<CAKGQuOVQjttk8qpLC2bh…` | frederick.stone; 2025-09-11T20:00:00Z; from PERSON_9709_EMAIL; 'Creator campaign for Zombie Match 3D - N' | GMAILM | OK |
| 177 | 352 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842998987980893279` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 178 | 353 | gmail.gmail_messages | INSERT | `frederick.stone/<CAIauDHOvbuHs1D8VFmRd…` | frederick.stone; 2025-09-24T18:00:00Z; from PERSON_9709_EMAIL; 'Re: Creator campaign for Zombie Match 3D' | GMAILM | OK |
| 179 | 355 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842168515789422611` | user frederick.stone; history_id NULL | GMAILT | OK |
| 180 | 357 | gmail.gmail_messages | INSERT | `frederick.stone/<CAIMbUgCSlodxbiO4p94u…` | frederick.stone; 2025-09-02T16:00:00Z; from frederick.stone@harmonygames.co; 'Store listing localization quote' | GMAILM | OK |
| 181 | 359 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842168515789422611` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 182 | 360 | gmail.gmail_messages | INSERT | `frederick.stone/<CAdgQm_LmTWyiKsAANkrE…` | frederick.stone; 2025-09-03T09:00:00Z; from PERSON_9710_EMAIL; 'Re: Store listing localization quote' | GMAILM | OK |
| 183 | 362 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842168515789422611` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 184 | 363 | gmail.gmail_messages | INSERT | `frederick.stone/<CAb3f_RRKlDbfktS3_Cu7…` | frederick.stone; 2025-09-23T08:30:00Z; from PERSON_9710_EMAIL; 'Re: Store listing localization quote' | GMAILM | OK |
| 185 | 365 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842353484595925809` | user frederick.stone; history_id NULL | GMAILT | OK |
| 186 | 367 | gmail.gmail_messages | INSERT | `frederick.stone/<CA1qNRLdbV7Qkr9KCNYq0…` | frederick.stone; 2025-09-04T17:00:00Z; from PERSON_9711_EMAIL; 'Player panel for Zombie Match 3D' | GMAILM | OK |
| 187 | 369 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842353484595925809` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 188 | 370 | gmail.gmail_messages | INSERT | `frederick.stone/<CAM5dEEI7CWxEdApgrQnK…` | frederick.stone; 2025-09-26T15:00:00Z; from PERSON_9711_EMAIL; 'Re: Player panel for Zombie Match 3D' | GMAILM | OK |
| 189 | 372 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1841081352192260725` | user frederick.stone; history_id NULL | GMAILT | OK |
| 190 | 374 | gmail.gmail_messages | INSERT | `frederick.stone/<CAyf6nlOFNNbNBnx3fo0w…` | frederick.stone; 2025-08-21T16:00:00Z; from PERSON_9712_EMAIL; 'ASO retainer proposal' | GMAILM | OK |
| 191 | 376 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1841081352192260725` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 192 | 377 | gmail.gmail_messages | INSERT | `frederick.stone/<CA0BbU6OEljE3nhaS2pWM…` | frederick.stone; 2025-09-25T17:00:00Z; from PERSON_9712_EMAIL; 'Re: ASO retainer proposal' | GMAILM | OK |
| 193 | 379 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843538794906427760` | user frederick.stone; history_id NULL | GMAILT | OK |
| 194 | 381 | gmail.gmail_messages | INSERT | `frederick.stone/<CAXYl4kZwjniI2DACcpaE…` | frederick.stone; 2025-09-17T19:00:00Z; from PERSON_9713_EMAIL; 'Seattle Indie Expo - pre-registration pu' | GMAILM | OK |
| 195 | 383 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1843538794906427760` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 196 | 384 | gmail.gmail_messages | INSERT | `frederick.stone/<CAHavdKpt7nR3fxojrxKL…` | frederick.stone; 2025-09-26T18:30:00Z; from PERSON_9713_EMAIL; 'Re: Seattle Indie Expo - pre-registratio' | GMAILM | OK |
| 197 | 386 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843980455117084538` | user frederick.stone; history_id NULL | GMAILT | OK |
| 198 | 388 | gmail.gmail_messages | INSERT | `frederick.stone/<CASRfZCkXuHwLJPLUeim9…` | frederick.stone; 2025-09-22T16:00:00Z; from PERSON_9714_EMAIL; 'Vaultline Standard renewal - Oct 12' | GMAILM | OK |
| 199 | 390 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844067277209770126` | user frederick.stone; history_id NULL | GMAILT | OK |
| 200 | 392 | gmail.gmail_messages | INSERT | `frederick.stone/<CApaJB4i_PhvJp_95Q3bE…` | frederick.stone; 2025-09-23T15:00:00Z; from PERSON_9715_EMAIL; 'Certificate renewal for your API domain' | GMAILM | OK |
| 201 | 394 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842895178957083445` | user frederick.stone; history_id NULL | GMAILT | OK |
| 202 | 396 | gmail.gmail_messages | INSERT | `frederick.stone/<CA3aUrexaU1ytNuMja5-4…` | frederick.stone; 2025-09-10T16:30:00Z; from PERSON_9716_EMAIL; 'Kinetic Arcade - publishing LOI for Zomb' | GMAILM | OK |
| 203 | 398 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842895178957083445` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 204 | 399 | gmail.gmail_messages | INSERT | `frederick.stone/<CAwVKKP1C-1rXHFCWIgbB…` | frederick.stone; 2025-09-29T17:00:00Z; from PERSON_9716_EMAIL; 'Re: Kinetic Arcade - publishing LOI for ' | GMAILM | OK |
| 205 | 401 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842991438234544282` | user frederick.stone; history_id NULL | GMAILT | OK |
| 206 | 403 | gmail.gmail_messages | INSERT | `frederick.stone/<CAMStwDpDMa-TpyL6LYTn…` | frederick.stone; 2025-09-11T18:00:00Z; from PERSON_9717_EMAIL; 'Lumencloud Startup Program - $25k credit' | GMAILM | OK |
| 207 | 405 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842991438234544282` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 208 | 406 | gmail.gmail_messages | INSERT | `frederick.stone/<CA2AOLHmh-RU9NexSr5s8…` | frederick.stone; 2025-09-30T16:00:00Z; from PERSON_9717_EMAIL; 'Re: Lumencloud Startup Program - $25k cr' | GMAILM | OK |
| 209 | 408 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843442535629243130` | user frederick.stone; history_id NULL | GMAILT | OK |
| 210 | 410 | gmail.gmail_messages | INSERT | `frederick.stone/<CAO2B00xDzwszNF3Ilw5P…` | frederick.stone; 2025-09-16T17:30:00Z; from PERSON_9718_EMAIL; 'Bundlehouse holiday bundle - Domino Deli' | GMAILM | OK |
| 211 | 412 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1843442535629243130` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 212 | 413 | gmail.gmail_messages | INSERT | `frederick.stone/<CAlSBl5tSj6BhvNqcMHhD…` | frederick.stone; 2025-09-26T16:00:00Z; from PERSON_9718_EMAIL; 'Re: Bundlehouse holiday bundle - Domino ' | GMAILM | OK |
| 213 | 415 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843708664218314020` | user frederick.stone; history_id NULL | GMAILT | OK |
| 214 | 417 | gmail.gmail_messages | INSERT | `frederick.stone/<CAdma6oOdAQE9dig43QVu…` | frederick.stone; 2025-09-19T16:00:00Z; from PERSON_9719_EMAIL; 'Orbit Store featuring - Zombie Match 3D' | GMAILM | OK |
| 215 | 419 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1843708664218314020` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 216 | 420 | gmail.gmail_messages | INSERT | `frederick.stone/<CAo7WkZSvPT7fVQd40F1H…` | frederick.stone; 2025-09-30T15:30:00Z; from PERSON_9719_EMAIL; 'Re: Orbit Store featuring - Zombie Match' | GMAILM | OK |
| 217 | 422 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842802694553769659` | user frederick.stone; history_id NULL | GMAILT | OK |
| 218 | 424 | gmail.gmail_messages | INSERT | `frederick.stone/<CAkJn3vHo1ZSVJM1fxECs…` | frederick.stone; 2025-09-09T16:00:00Z; from PERSON_9720_EMAIL; 'Markward free tier - brand monitoring' | GMAILM | OK |
| 219 | 426 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842802694553769659` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 220 | 427 | gmail.gmail_messages | INSERT | `frederick.stone/<CAjzt3v0v5AIRijm5FdJu…` | frederick.stone; 2025-09-23T16:30:00Z; from PERSON_9720_EMAIL; 'Re: Markward free tier - brand monitorin' | GMAILM | OK |
| 221 | 429 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844256020889910750` | user frederick.stone; history_id NULL | GMAILT | OK |
| 222 | 431 | gmail.gmail_messages | INSERT | `frederick.stone/<CAWCBU--R8_Q4xxjtvPvD…` | frederick.stone; 2025-09-25T17:00:00Z; from PERSON_9721_EMAIL; 'Playfuse bundle partnership - NDA' | GMAILM | OK |
| 223 | 433 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1839631800730308867` | user frederick.stone; history_id NULL | GMAILT | OK |
| 224 | 435 | gmail.gmail_messages | INSERT | `frederick.stone/<CAat3tn3W0qDDTcWKmBYw…` | frederick.stone; 2025-08-05T16:00:00Z; from PERSON_9722_EMAIL; 'Your Hootline promo' | GMAILM | OK |
| 225 | 437 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1839631800730308867` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 226 | 438 | gmail.gmail_messages | INSERT | `frederick.stone/<CAhKYUa4HtPNJGhGU5qif…` | frederick.stone; 2025-09-24T16:30:00Z; from PERSON_9722_EMAIL; 'Re: Your Hootline promo' | GMAILM | OK |
| 227 | 440 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843350051225919345` | user frederick.stone; history_id NULL | GMAILT | OK |
| 228 | 442 | gmail.gmail_messages | INSERT | `frederick.stone/<CAK5OtyGBKIjnQ7R24aq6…` | frederick.stone; 2025-09-15T17:00:00Z; from frederick.stone@harmonygames.co; 'Font licence quote - Zombie Match 3D' | GMAILM | OK |
| 229 | 444 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1843350051225919345` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 230 | 445 | gmail.gmail_messages | INSERT | `frederick.stone/<CAWFrjpQqU9OPoIfzxLgV…` | frederick.stone; 2025-09-16T08:30:00Z; from PERSON_9723_EMAIL; 'Re: Font licence quote - Zombie Match 3D' | GMAILM | OK |
| 231 | 447 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1843350051225919345` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 232 | 448 | gmail.gmail_messages | INSERT | `frederick.stone/<CApanLB9xL5jrjcNSzDTW…` | frederick.stone; 2025-09-30T08:00:00Z; from PERSON_9723_EMAIL; 'Re: Font licence quote - Zombie Match 3D' | GMAILM | OK |
| 233 | 450 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843078260327282996` | user frederick.stone; history_id NULL | GMAILT | OK |
| 234 | 452 | gmail.gmail_messages | INSERT | `frederick.stone/<CAXUVl-vI7c6T4f22vI41…` | frederick.stone; 2025-09-12T17:00:00Z; from PERSON_9724_EMAIL; 'Cloudlark credits reserved for Harmony G' | GMAILM | OK |
| 235 | 454 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1841538111898044975` | user frederick.stone; history_id NULL | GMAILT | OK |
| 236 | 456 | gmail.gmail_messages | INSERT | `frederick.stone/<CAF3j_dVe4Smvh19S7lyC…` | frederick.stone; 2025-08-26T17:00:00Z; from PERSON_9725_EMAIL; 'Echohall Pro for your community' | GMAILM | OK |
| 237 | 458 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1841538111898044975` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 238 | 459 | gmail.gmail_messages | INSERT | `frederick.stone/<CAHV7my-sLo9CEzISCj6j…` | frederick.stone; 2025-09-18T17:00:00Z; from PERSON_9725_EMAIL; 'Re: Echohall Pro for your community' | GMAILM | OK |
| 239 | 461 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842983888486665921` | user frederick.stone; history_id NULL | GMAILT | OK |
| 240 | 463 | gmail.gmail_messages | INSERT | `frederick.stone/<CAGdptfs7cIHOLvLgF6LB…` | frederick.stone; 2025-09-11T16:00:00Z; from PERSON_9726_EMAIL; 'Pressbeam launch package' | GMAILM | OK |
| 241 | 465 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843346276352069546` | user frederick.stone; history_id NULL | GMAILT | OK |
| 242 | 467 | gmail.gmail_messages | INSERT | `frederick.stone/<CAOHCdeuLRHpqtIPQZRUG…` | frederick.stone; 2025-09-15T16:00:00Z; from PERSON_9727_EMAIL; 'Welcome to Retainly' | GMAILM | OK |
| 243 | 469 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842262887629456494` | user frederick.stone; history_id NULL | GMAILT | OK |
| 244 | 471 | gmail.gmail_messages | INSERT | `frederick.stone/<CAi_XBSxfgfRVpvhsqJCt…` | frederick.stone; 2025-09-03T17:00:00Z; from PERSON_9728_EMAIL; 'Quillcraft beta' | GMAILM | OK |
| 245 | 473 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842262887629456494` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 246 | 474 | gmail.gmail_messages | INSERT | `frederick.stone/<CALcXsJB9Dsqckdbzui4z…` | frederick.stone; 2025-09-29T16:00:00Z; from PERSON_9728_EMAIL; 'Re: Quillcraft beta' | GMAILM | OK |
| 247 | 476 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843708664217753499` | user frederick.stone; history_id NULL | GMAILT | OK |
| 248 | 478 | gmail.gmail_messages | INSERT | `frederick.stone/<CAdfSBCTPq8pDFK70IArh…` | frederick.stone; 2025-09-19T16:00:00Z; from PERSON_9729_EMAIL; 'Tilecast pilot slot' | GMAILM | OK |
| 249 | 480 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843984229991264696` | user frederick.stone; history_id NULL | GMAILT | OK |
| 250 | 482 | gmail.gmail_messages | INSERT | `frederick.stone/<CAHSfM6DagNeY2EUvRjCO…` | frederick.stone; 2025-09-22T17:00:00Z; from frederick.stone@harmonygames.co; 'Benchmarkly sample report' | GMAILM | OK |
| 251 | 484 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1843984229991264696` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 252 | 485 | gmail.gmail_messages | INSERT | `frederick.stone/<CAFrM1JgqylGFM5MjwuqQ…` | frederick.stone; 2025-09-23T16:00:00Z; from PERSON_9730_EMAIL; 'Re: Benchmarkly sample report' | GMAILM | OK |
| 253 | 487 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842712097587609477` | user frederick.stone; history_id NULL | GMAILT | OK |
| 254 | 489 | gmail.gmail_messages | INSERT | `frederick.stone/<CAXtogZgoD89z43tdTH1z…` | frederick.stone; 2025-09-08T16:00:00Z; from PERSON_9731_EMAIL; 'Your Loopnote trial' | GMAILM | OK |
| 255 | 491 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842712097587609477` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 256 | 492 | gmail.gmail_messages | INSERT | `frederick.stone/<CAff-LH5Vcdc03I5o2aYm…` | frederick.stone; 2025-09-26T16:00:00Z; from PERSON_9731_EMAIL; 'Re: Your Loopnote trial' | GMAILM | OK |
| 257 | 494 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844165423924029064` | user frederick.stone; history_id NULL | GMAILT | OK |
| 258 | 496 | gmail.gmail_messages | INSERT | `frederick.stone/<CA6I5lYTxcuD1NKwoqPt6…` | frederick.stone; 2025-09-24T17:00:00Z; from frederick.stone@harmonygames.co; 'Voice-over quote' | GMAILM | OK |
| 259 | 498 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1844165423924029064` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 260 | 499 | gmail.gmail_messages | INSERT | `frederick.stone/<CA-DqRg1TZ4TPniI7P8AW…` | frederick.stone; 2025-09-25T16:00:00Z; from PERSON_9732_EMAIL; 'Re: Voice-over quote' | GMAILM | OK |
| 261 | 501 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843346276352084348` | user frederick.stone; history_id NULL | GMAILT | OK |
| 262 | 503 | gmail.gmail_messages | INSERT | `frederick.stone/<CAroxkgBywTvnZooHWA1Q…` | frederick.stone; 2025-09-15T16:00:00Z; from PERSON_9733_EMAIL; 'Motive Forge - 3D art quote' | GMAILM | OK |
| 263 | 505 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1843346276352842555` | user arthur.blake; history_id NULL | GMAILT | OK |
| 264 | 507 | gmail.gmail_messages | INSERT | `arthur.blake/<CAroxkgBywTvnZooHWA1Q…` | arthur.blake; 2025-09-15T16:00:00Z; from PERSON_9733_EMAIL; 'Motive Forge - 3D art quote' | GMAILM | OK |
| 265 | 509 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1843346276352084348` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 266 | 510 | gmail.gmail_messages | INSERT | `frederick.stone/<CALRuD4F9RvCLHQDHmtUq…` | frederick.stone; 2025-09-19T17:45:00Z; from arthur.blake@harmonygames.co; 'Re: Motive Forge - 3D art quote' | GMAILM | OK |
| 267 | 512 | gmail.gmail_threads | UPDATE | `arthur.blake@harmonygames.co/1843346276352842555` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 268 | 513 | gmail.gmail_messages | INSERT | `arthur.blake/<CALRuD4F9RvCLHQDHmtUq…` | arthur.blake; 2025-09-19T17:45:00Z; from arthur.blake@harmonygames.co; 'Re: Motive Forge - 3D art quote' | GMAILM | OK |
| 269 | 515 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842712097588195482` | user frederick.stone; history_id NULL | GMAILT | OK |
| 270 | 517 | gmail.gmail_messages | INSERT | `frederick.stone/<CAjj6h7BzqoAZSS2-4M7N…` | frederick.stone; 2025-09-08T16:00:00Z; from PERSON_9734_EMAIL; 'Spotlight Fest - showcase slot, Dec 5' | GMAILM | OK |
| 271 | 519 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1842255337882328812` | user frederick.stone; history_id NULL | GMAILT | OK |
| 272 | 521 | gmail.gmail_messages | INSERT | `frederick.stone/<CAFbpDWclpri3pr8w9gLz…` | frederick.stone; 2025-09-03T15:00:00Z; from PERSON_9735_EMAIL; 'Nova Rewards partnership' | GMAILM | OK |
| 273 | 523 | gmail.gmail_threads | UPDATE | `frederick.stone@harmonygames.co/1842255337882328812` | SET snippet = latest message snippet | Target thread inserted earlier in this SQL | OK |
| 274 | 524 | gmail.gmail_messages | INSERT | `frederick.stone/<CA32kc92PkZh7ZypeSz7a…` | frederick.stone; 2025-09-23T16:00:00Z; from PERSON_9735_EMAIL; 'Re: Nova Rewards partnership' | GMAILM | OK |
| 275 | 526 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844622183629433486` | user frederick.stone; history_id NULL | GMAILT | OK |
| 276 | 528 | gmail.gmail_messages | INSERT | `frederick.stone/<calendar-7ab9aa8e-d44…` | frederick.stone; 2025-09-29T18:00:00Z; from leonard.hayes@harmonygames.co; 'Invitation: Q4 commitments review @ Mon ' | GMAILM | OK |
| 277 | 530 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1844622183628992238` | user robert; history_id NULL | GMAILT | OK |
| 278 | 532 | gmail.gmail_messages | INSERT | `robert/<calendar-a902eeee-7fb…` | robert; 2025-09-29T18:00:00Z; from leonard.hayes@harmonygames.co; 'Invitation: Q4 commitments review @ Mon ' | GMAILM | OK |
| 279 | 534 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1844622183629272206` | user arthur.blake; history_id NULL | GMAILT | OK |
| 280 | 536 | gmail.gmail_messages | INSERT | `arthur.blake/<calendar-d127348e-905…` | arthur.blake; 2025-09-29T18:00:00Z; from leonard.hayes@harmonygames.co; 'Invitation: Q4 commitments review @ Mon ' | GMAILM | OK |
| 281 | 538 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843074485453681260` | user frederick.stone; history_id NULL | GMAILT | OK |
| 282 | 540 | gmail.gmail_messages | INSERT | `frederick.stone/<calendar-36ed726c-941…` | frederick.stone; 2025-09-12T16:00:00Z; from robert@harmonygames.co; 'Invitation: Spotlight Fest showcase call' | GMAILM | OK |
| 283 | 543 | gcal.gcal_events | INSERT | `evt_fd469c29811879519c2c96` | cal frederick.stone; 2026-01-05T17:00:00Z; created 2025-09-29T18:00:00Z | id absent of 10,395 events; uid absent; calendar exists | OK |
| 284 | 545 | gcal.gcal_events | INSERT | `evt_2ad963d94b80e64c3a3c12` | cal leonard.hayes; 2026-01-05T17:00:00Z; created 2025-09-29T18:00:00Z | id absent of 10,395 events; uid absent; calendar exists | OK |
| 285 | 547 | gcal.gcal_events | INSERT | `evt_c8f5a9295ed40f33d90fab` | cal robert; 2026-01-05T17:00:00Z; created 2025-09-29T18:00:00Z | id absent of 10,395 events; uid absent; calendar exists | OK |
| 286 | 549 | gcal.gcal_events | INSERT | `evt_bde03e4af2d3b5039711c0` | cal arthur.blake; 2026-01-05T17:00:00Z; created 2025-09-29T18:00:00Z | id absent of 10,395 events; uid absent; calendar exists | OK |
| 287 | 551 | gcal.gcal_events | INSERT | `evt_0a5e42c3aac62434ba2cfc` | cal frederick.stone; 2025-07-14T16:00:00Z; created 2025-07-08T18:10:00Z | id absent of 10,395 events; uid absent; calendar exists | OK |
| 288 | 553 | gcal.gcal_events | INSERT | `evt_564a16d0f5f6598d0360d5` | cal frederick.stone; 2025-09-17T18:00:00Z; created 2025-09-12T16:00:00Z | id absent of 10,395 events; uid absent; calendar exists | OK |
| 289 | 555 | gcal.gcal_events | INSERT | `evt_0c2bdb97953bcb213e1d36` | cal robert; 2025-09-17T18:00:00Z; created 2025-09-12T16:00:00Z | id absent of 10,395 events; uid absent; calendar exists | OK |
| 290 | 558 | linear.linear_issues | INSERT | `ZOM-567` | team_ZOM; creator Arthur (usr_cc3e…); Todo; created 2025-09-23T17:00:00Z | id/identifier absent of 3,687; team/user exist | OK |
| 291 | 560 | linear.linear_comments | INSERT | `cmt_c9a6660d81e067ad1de7` | issue ZOM-567; author Arthur; 2025-09-25T18:20:00Z | base comments array empty; issue in SQL | OK |
| 292 | 563 | contacts.contacts | INSERT | `9b0185e445572aeee9f27d35` | ESG Law intake; PERSON_2599_EMAIL; job Outside counsel - agreement intake | id/email/name absent of 170 contacts | OK |
| 293 | 565 | contacts.contacts | INSERT | `a6ebc7683d450b0017b8acf3` | Noor Haddad; PERSON_9716_EMAIL; job Kinetic Arcade | id/email/name absent of 170 contacts | OK |
| 294 | 567 | contacts.contacts | INSERT | `35a52a2e3c634972639806b5` | Aiden Clarke; PERSON_9717_EMAIL; job Lumencloud | id/email/name absent of 170 contacts | OK |
| 295 | 569 | contacts.contacts | INSERT | `8a7605bdc08105137d87f5a7` | Leah Brennan; PERSON_9720_EMAIL; job Markward | id/email/name absent of 170 contacts | OK |

Gmail ledger key: "GMAILT" = thread id absent from all 81,404 base thread files (complete scan) and its messages inserted in the same mailbox. "GMAILM" = Message-ID absent from the base (complete scan), thread inserted earlier in the SQL, and headers, dates and reply chain verified (§5 C).

## 7. Findings

No demonstrated defects. Rev 4 resolves rev 3's advisories C-adv 1 (guardrails doc vs calendar creation date) and C-adv 4 (Doc title style runs). Remaining advisories: B-adv (4 columns missing from the snapshot), C-adv 2 (ZOM-567 / Trello idShort 456 numbered out of creation order, matching base patterns) and C-adv 3 ("attached" emails with empty `attachments_meta_json`; docs live in Drive). None blocks this stage.

## 8. Dependencies for later stages (stage-evidence-v1)

This report's checks hold only while all of these stay the same: SQL sha256 `795bd191872d7f57be1d2e0d09bd74f23a05561ce2c6e58e87c6162c11b4713f`; universe manifest `da2f4cf0…a04aac1a`; synth-cut clock; schema snapshot `31dcb2b4…`; id_contracts `fc4711ef…`. `/prompt` may reuse the static A–C results for this exact SQL but must still check discoverability, persona access and feasibility itself.

Input-manifest entry (recorded here; the output writer saves only this report): `{"injection": {"review_version": "injection-static-v2", "evidence_contract": "stage-evidence-v1", "reused_evidence": ["0_injection.md rev3 (sql 9066997d…ef74ef3) per-row checks for 292 byte-identical rows; manifest da2f4cf0…a04aac1a unchanged"], "input": "Evals/task_inputs/01_Universe_Inject.sql", "sha256": "795bd191872d7f57be1d2e0d09bd74f23a05561ce2c6e58e87c6162c11b4713f"}}`

## 9. Next action

Proceed to `/prompt`. If the SQL changes, rerun `/injection` first, then every later stage that reads the SQL.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt (then /hardness, /oe and /rubric, since all read the injection SQL)

Evidence limits: Rows unchanged since rev 3 reuse that review's checks under stage-evidence-v1 (identical lines, unchanged manifest and references); Drive/Docs collisions and the 3 changed rows were re-checked fresh. Static review only. No live execution, deployment or live-schema check. The bundled schema snapshot is unverified, and 4 inserted columns are not covered by it (advisory). Agent visibility, task design and difficulty are outside this stage.
