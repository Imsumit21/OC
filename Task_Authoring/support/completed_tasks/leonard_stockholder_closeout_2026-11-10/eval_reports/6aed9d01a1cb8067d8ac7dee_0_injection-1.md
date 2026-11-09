# Injection Data-Integrity Review (Eval 0)

- Review version: `injection-static-v2`
- Evidence contract: `stage-evidence-v1` (no reused evidence; all checks NEW)
- Mode: chat/attachment review, attempt 6aed9d01a1cb8067d8ac7dee
- Actual review time: 2026-11-07T20:56Z
- Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
- Universe: `Universe_Normal`; manifest `Evals/references/universes/normal/universe_manifest.json` (sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450`)
- Input: `Evals/task_inputs/01_Universe_Inject.sql`, 74,125 bytes, sha256 `bc72db9c31e9982751e47762f94939c7c5367ee7979830e28acb55627b957f2d` (input-store revision 3, from upload `01_Universe_Inject.sql`)
- Schema snapshot: `Evals/references/schema/injection.json` (guide view sha256 `31dcb2b43feca8e5c7cb67f37973f819c9b9774f12f8b15cb7da89ecd74c5151`), unverified/provisional
- Lint: `hg_injection_lint.py` `injection-lint-v1`

## Input / authority issues

None. SQL read in full before base searches. Source text treated as evidence only.

## Checklist

- [x] Save/reload SQL; hash, manifest, review version recorded (NEW)
- [x] Lint run; 0 FAIL / 0 CHECK / 0 INFO (NEW)
- [x] Inventory of all 130 statements (NEW)
- [x] Check A (NEW)
- [x] Check B (NEW)
- [x] Check C (NEW)
- [x] Coverage, findings, limits, single verdict

## Lint flags and resolutions

Lint ran checks `future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required, json_shape`; base loaded: contacts, slack users, trello, gmail users, linear, confluence. **Flags: none.** Statements: 130 (1 BEGIN, 121 INSERT, 7 UPDATE, 1 COMMIT). Checks A–C performed in full below regardless.

## Operation ledger (execution order)

Base paths are under `Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/` unless marked Gmail (`Universe_Normal/Normal_HarmonyGames_Gmail/Services_Data/gmail/`).

| # / lines | Table | Op | Record(s) | Key values | Base reference / result |
|---|---|---|---|---|---|
| L3-4 | gdrive.drive_files | INSERT | `d_601064334a0b493022fe83` folder "Stockholder close-out" | parent `d_63fffeb4fab5233ed5bb73`, owner leonard.hayes, created 2026-02-12T23:20:37Z | Parent = Leonard's root folder (`gdrive/data.json` /drive_files/9034). New ID unused (53,866 files scanned). PASS |
| L5-6 | gdrive.drive_files | INSERT | `f_a37b403d5200d4f0a31d31` Doc "Stockholder close-out notes" | parent new folder, 2026-02-13T01:05:41Z | Unused; content row L14-15. PASS |
| L7-8 | gdrive.drive_files | INSERT | `f_762c60832854d3e7a7f7df` Doc "Holder outreach notes" | parent root, 2026-02-10T17:41:09Z | Unused; content row L16-17. PASS |
| L9-10 | gdrive.drive_files | INSERT | `f_5ecaa967db3adcfa440b09` Sheet "Holder list (draft)" | parent new folder, 2026-02-10T18:12:26Z | Unused; content L19-22. PASS |
| L11-12 | gdrive.drive_files | INSERT | `f_75dddccabb26eeea4842c8` Slides "Harmony Games February 26 Update" | parent new folder, 2026-02-10T18:33:52Z | Unused; content L24-45. PASS |
| L14-15 | gdocs.docs_documents | INSERT | `f_a37b403d5200d4f0a31d31` | body 1,950 chars; style run end 1950 | Unused in 633 docs; run length = body length. PASS |
| L16-17 | gdocs.docs_documents | INSERT | `f_762c60832854d3e7a7f7df` | body 290 chars; run end 290 | Unused; consistent. PASS |
| L19-20 | gsheets.sheets_spreadsheets | INSERT | `f_5ecaa967db3adcfa440b09` | owner leonard | Unused in 398 sheets. PASS |
| L21-22 | gsheets.sheets_sheets | INSERT | sheet 0 of above | 8 rows (header + 7 holders) | Values match Nov 26 2024 owner list (see C). PASS |
| L24-25 | gslides.slides_presentations | INSERT | `f_75dddccabb26eeea4842c8` | rev `0b2616045d` | Unused in 164 presentations. PASS |
| L26-45 | gslides.slides_pages ×5 / slides_page_elements ×5 | INSERT | slides `slide_341616bedf43`, `slide_659353384faa`, `slide_fdc349f96a2c`, `slide_3ac232c61018`, `slide_e30ad4186e4c`; elements `el_f71854425943`, `el_3f1b82e16a82`, `el_b4a6a6d9a533`, `el_9dabe7a0ac53`, `el_453848aef60e` | index 0-4, TEXT_BOX, full-slide EMU | Scoped to new presentation; base element shape (TEXT_BOX, 9144000×5143500) matches. PASS (column advisory, see B) |
| L47-48 | slack.slack_messages | INSERT | `d281112d634372d5a8b35fc49a3e4b8c` ts 1770938120.410229 | C0ADGSZKR3R (#winddown), EMPLOYEE_0038 (Leonard), top-level | Channel exists (`slack/channels.json` /154), Leonard member; ID unused (687,230 msgs, 5,353 files). ts = created_at. PASS |
| L49-50 | slack.slack_messages | INSERT | `44975451e7eee53377ea87461fade5ab` ts 1770938131.882339 | same | PASS |
| L51-52 | slack.slack_messages | INSERT | `a8540bc368de959fd190648f5b48fdf1` ts 1770938158.104719 | same | PASS |
| L53-54 | slack.slack_messages | INSERT | `4f54dff9722aaeef2ba59316ff0cf2f9` ts 1770949310.220519 | reply to `e3e198cc…` (thread_ts 1770934638.035469), Leonard | Parent exists (`slack/messages/C0ADGSZKR3R/2026-02.json` /197), base reply_count 0. PASS |
| L55-56 | slack.slack_messages | INSERT | `0e3d2253c9a2f33c47110c2917d3a724` ts 1770949322.640149 | reply, Leonard | PASS |
| L57-58 | slack.slack_messages | INSERT | `846c625fed7922e6b261026e703636d9` ts 1770949351.317729 | reply, Leonard | PASS |
| L59-60 | slack.slack_messages | INSERT | `7440b1baf08601fe1a281017181fa98f` ts 1770949437.902269 | reply, EMPLOYEE_0025 (Arthur Blake) | Arthur is channel member. PASS |
| L61 | slack.slack_messages | UPDATE | `e3e198cc6e3f866a032d34c5f69e39f9` | thread_ts_legacy→own ts; reply_count 0→4; reply_users_count 0→2; latest_reply→1770949437.902269 | Matches 4 injected replies, 2 distinct users, latest ts; same representation as base parent `d4d97535…` (thread_ts = own ts). PASS |
| L63-64 | trello.trello_cards | INSERT | `698e5a10c3f24b7e9d16a0e4` "Stockholder close-out", idShort 456 | board `640643a3fd8f3ca308d9318e`, list `640643a3fd8f3ca308d93195` "To Do", badges comments 1 | Board/list exist (/boards/1, /lists/3); card ID, idShort 456 (base max 455) unused in 803 cards; shortLink/shortUrl NULL as in all 449 base cards on board. ID hex time = 2026-02-12T22:54:08Z. PASS |
| L65-66 | trello.trello_actions | INSERT | `698e5a108882c0b9e98cdb3e` createCard 2026-02-12T22:54:08Z | creator PERSON_6094 | Member = Leonard Hayes (/members/2); ID unused in 5,294 actions; hex time matches. PASS |
| L67 | trello.trello_boards | UPDATE | board `640643a3fd8f3ca308d9318e` | dateLastActivity 2025-11-12T17:25:43Z → 2026-02-13T18:14:27Z | Equals latest injected action. PASS |
| L68-69 | trello.trello_actions | INSERT | `698f6a03a222ee9dc57bc90f` commentCard 2026-02-13T18:14:27Z | Leonard | Unused; hex time matches; card badge comments = 1. PASS |
| L71-72 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1857029474983245439` | history_id NULL | Unused (grep of all 88,726 thread files); thread-ID time 2026-02-13T16:48:35Z ≈ first msg. PASS |
| L73-74 | gmail.gmail_messages | INSERT | `…/<LV3PR19MB8524F1C07D3A94E26B58D0AC7A1E2@…>` KPMG audit request | from PERSON_3088 (cc 4416, 2322, 2847), 2026-02-13T16:48:33Z, label Label_b19fb8d1b3 | All four externals exist in base KPMG audit threads (e.g. Gmail `threads/leonard@harmonygames.co_1817557789846606177.json`); label exists ("Opened", `labels.json`). internal_date = date. PASS |
| L75, L78 | gmail.gmail_threads | UPDATE | thread …1857029474983245439 snippet | set to latest message snippet each time | Final snippet = L80 message. PASS |
| L76-77 | gmail.gmail_messages | INSERT | `…/<CAPBs_a7Tq2LmV9xYcR4KdN8wUe3HsJ6oFbZ1gPiA5tGyQnE0Xw@mail.gmail.com>` Leonard reply | 2026-02-13T17:12:40Z; In-Reply-To L74 | Quote header "8:48 AM" = 16:48Z PST. PASS |
| L79-80 | gmail.gmail_messages | INSERT | `…/<LV3PR19MB85246D2E9B14C7A03F5E8D12BC4A7@…>` KPMG clarification | 2026-02-13T17:37:15Z; In-Reply-To L77 | Chronology coherent. PASS |
| L81-82 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1857034369525983506` | history_id NULL | Unused; thread-ID time 2026-02-13T18:06:22Z ≈ first msg. PASS |
| L83-84 | gmail.gmail_messages | INSERT | `…/<mlkq74xd.3f9e2c1a-6b48-4d07-a1e5-8c2f0d7b6a94@we.are.superhuman.com>` Sunset intake | from PERSON_2888, 2026-02-13T18:06:21Z | PERSON_2888 = Sunset Head of Partnerships in base (Gmail `threads/00016827.json`), same signature. PASS |
| L85 | gmail.gmail_threads | UPDATE | thread …1857034369525983506 snippet | latest message | PASS |
| L86-87 | gmail.gmail_messages | INSERT | `…/<CAPBs_a5Wn3RvK8yZtH2DqL7mJc9XeU4oGfB6sPiN1aTuYkEr0Q@mail.gmail.com>` Leonard reply | 2026-02-13T18:19:02Z | Quote "10:06 AM" = 18:06Z PST. PASS |
| L88 | gmail.gmail_threads | UPDATE | `leonard.hayes@harmonygames.co/1773963101399472184` snippet | → new Robert message | Thread exists (Gmail `threads/leonard@harmonygames.co_1773963101399472184.json`, user leonard.hayes). PASS |
| L89-90 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAGkro_PbX4mT7nQe2LwV9sKd1YhJ3uF6aRc8ZoGi5NtEyMq0Bw@mail.gmail.com>` | from robert, to PERSON_3941, cc Leonard, 2026-02-12T23:41:12Z; In-Reply-To `<CAGkro_Ox2wP8…>` | Parent message exists in this thread (2023-08-11 "Thanks!!!", 13:00:43 -0700 = quoted "1:00 PM"); sign-off [PERSON_NAME_0054] matches Robert's base sign-off. Unused ID. PASS |
| L91 | gmail.gmail_threads | UPDATE | `robert@harmonygames.co/1773963101279916523` snippet | → new message | Thread exists (Gmail `threads/00001367.json`, user robert). PASS |
| L92-93 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAGkro_PbX4mT7nQe2LwV9sKd1YhJ3uF6aRc8ZoGi5NtEyMq0Bw@mail.gmail.com>` | SENT copy, same content/time | Parent `<CAGkro_Ox2wP8…>` in this thread; mailbox robert@ exists (`users.json`). PASS |
| L95-96 | gcal.gcal_events | INSERT | `evt_6f1a2c9e4b7d3a58c0e1d2` "Holder notes due" | calendar leonard.hayes; start 2026-02-17T17:00Z (Tue 9:00 PT); created 2026-02-13T01:12:18Z | Calendar exists (/calendars/15); event_id and ical_uid unused (11,130 events). Future start = plan field. PASS |
| L98-99 | contacts.contacts | INSERT | `d3c6e5b57e0ee6656a1bdd2c` PERSON_0693 | email PERSON_0693_EMAIL, job Investor | ID/email/name unused in 170 contacts; person exists in base Gmail (`threads/00013855.json`). Naming matches base convention. PASS |
| L100-101 | contacts.contacts | INSERT | `13f3b76067d577bc30c45242` PERSON_2275 | email PERSON_2275_EMAIL | Unused; person exists in base Gmail (`threads/leonard@harmonygames.co_1770141224265557526.json`). PASS |
| L103-104 | linear.linear_projects | INSERT | `ec2ea957-fc8e-4958-b809-0fb735b1e916` "Holder records" | team_ENG, lead usr_63fffeb4fab5233e, state started, created 2026-02-12T23:24:12Z, updated 2026-02-13T18:21:46Z | Team (/teams/2) and Leonard's Linear user (/users/13) exist; project ID/name unused (2 projects). PASS (column advisory, see B) |
| L105-260 | linear.linear_issues ×26 | INSERT | `ENG-2438` … `ENG-2463` (ids = identifiers, numbers 2438-2463) | team_ENG, creator Leonard, state Backlog, project above, created 2026-02-12T23:25:03Z–23:32:26Z, updated = last comment time | ENG max in base 2437; none of the 26 ids/identifiers/numbers exist (3,852 issues). `Backlog` is a base state value. state_history_json `'[]'`. PASS |
| L107-259 | linear.linear_comments ×52 | INSERT | two per issue (`comment_ed8c0824…` … `comment_b8881cec…`), all 52 IDs distinct | author Leonard, 2026-02-12T23:34:21Z–2026-02-13T00:03:06Z | Base `/comments` is empty (0 records), so no collision; each comment after its issue's creation. PASS |

## Check A — Records, references and IDs: PASS

- All referenced parents/targets resolve: Drive root folder, #winddown channel and thread parent, Trello board/list/member, Gmail mailboxes (leonard.hayes, robert), both existing Gmail threads and the In-Reply-To parent message, Gmail label, Google Calendar, Linear team and user.
- Actors resolve to the named person in each service: Slack EMPLOYEE_0038 = Leonard Hayes, EMPLOYEE_0025 = Arthur Blake (both #winddown members); Trello PERSON_6094 = Leonard Hayes; Linear usr_63fffeb4fab5233e = leonard.hayes; Gmail senders match base addresses and display format. No second account for any existing person (lint `identities` clean; contacts' emails/names absent from base contacts).
- New-key collisions: none across complete scopes (Drive 53,866; Docs 633; Sheets 398; Slides 164; Slack 687,230 messages/5,353 files; Trello cards 803 + idShort + actions 5,294; Gmail all 88,726 thread files by grep for thread and Message-IDs; GCal 11,130 event_id/ical_uid; Contacts 170; Linear projects 2, issues 3,852 by id/identifier/number, comments 0). No duplicate keys inside the SQL.
- ID contracts: Gmail history_id NULL (allowed). No Drive content_path used. Readable-Drive rule: both Docs have docs_documents rows with non-empty body; Sheet and Slides have content rows.

## Check B — SQL structure and supported schema rules: PASS (with provisional advisory)

- Single BEGIN/COMMIT transaction; every INSERT column/value count consistent (lint parse clean); no generated columns (`text_fts`, `body_text_fts`) set; Linear `*_at`/`start_date` in `YYYY-MM-DDTHH:MM:SSZ` / `YYYY-MM-DD`; `state_history_json '[]'` given; `*_json` shapes match base (slack metadata_json `'{}'`, arrays `'[]'`); no NOT NULL column without default omitted.
- **Advisory (snapshot MISMATCH, not a defect under Eval 0 / schema README):** four columns used are not in the unverified snapshot: `gslides.slides_pages.notes`, `gslides.slides_page_elements.table_json`, `gslides.slides_page_elements.ordinal`, `linear.linear_projects.links_json` (the snapshot has `links_json` on `linear_issues`, not on `linear_projects`). If the live database lacks any of them, the whole transaction would roll back. Safest option: drop those columns (all carry NULL/`'[]'`/0 values that add no content), or keep them if confirmed elsewhere.
- Remaining tables: MATCH to snapshot.

## Check C — Dates, relationships and consistency: PASS

- Clock: all event timestamps ≤ 2026-02-13T18:21:46Z (< 2026-02-14 00:00 UTC). Only post-clock values: GCal start/end 2026-02-17 (plan fields, allowed).
- Encoded times agree: Slack ts = created_at (7/7); Gmail internal_date = date and Date headers (7/7); quoted "On … wrote" times correct in PT; Trello ID hex times = action dates; Gmail thread-ID times ≈ first message.
- Chronology: Slack "Putting the holders in linear" (23:15:20 Feb 12) → project 23:24:12 → issues 23:25–23:32 → comments 23:34–00:03; Drive folder 23:20:37 with contacts; close-out Doc 01:05:41 Feb 13 → calendar slot 01:12:18; thread replies 02:21–02:23 follow parent (Feb 12 22:17:18Z); KPMG 16:48 → reply 17:12 → clarification 17:37; Sunset 18:06 → reply 18:19 → Trello comment "Sunset wants the same sheet" 18:14 (after the 18:06 email) → project updated 18:21 (description mentions Sunset and KPMG, both received by then). Trello board activity raised to the latest action.
- Facts vs base: the "Nov 2024 owner list" cited by the sheet, slide and 25 Linear comments is Leonard's 2024-11-26 email (Gmail `threads/leonard@harmonygames.co_1816809274978043917.json`, msg 0). It lists 27 owners (slide says 27) and every copied figure matches (e.g. Griffin 2,746,693; [PERSON_NAME_0038] 127,162; TOR 50,865; Calvin Price 8,138; Claire Morgan 7,630; [PERSON_NAME_0100] absent = "Not on the Nov 2024 owner list"). Name masking variants (e.g. "Martin [PERSON_NAME_7250] Walsh" vs "Martin Georgiev Walsh") are anonymization differences, not introduced conflicts.
- Base context consistent: "archive google after the 15th" matches base #winddown task list (1770933903); "linear we keep during transition" matches base 1770933601; the "Feb 12 Board position thread" exists (Gmail `threads/00016903.json`, 2026-02-12T22:14:52Z); "notes ready by Tuesday" = Feb 17 = calendar slot.
- Superseded/stale content is supported: "Holder outreach notes" (Feb 10) is explicitly replaced by the Feb 13 close-out notes; Linear "Last written contact I have before Feb" comments are dated, scoped notes, not contradicted by the Feb 12 Robert email.
- Grader-facing text: none found (lint clean; manual read of all injected text). SQL contains only section-header comments; no tool-call/pass-rate comments.
- Snowflake/Confluence base conflicts: none listed for this universe touch these records (only SC-63, synth-cut, mentions Griffin). No advisory.

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | All targets resolve; no collisions across complete scopes; one account per person. |
| B — SQL structure and supported schema rules | PASS | Structure and documented rules clean. Provisional snapshot MISMATCH advisory on 4 columns (gslides notes/table_json/ordinal, linear_projects.links_json). |
| C — Dates, relationships and consistency | PASS | All events before the clock; chronology and copied figures consistent with base. |

## Findings

No demonstrated defects.

Advisory (optional, smallest change): remove `notes` from the 5 `gslides.slides_pages` INSERTs, `table_json` and `ordinal` from the 5 `gslides.slides_page_elements` INSERTs, and `links_json` from the `linear.linear_projects` INSERT, since the snapshot has no such columns and a missing live column would roll back the whole script.

## Dependencies for later stages

- SQL sha256 `bc72db9c31e9982751e47762f94939c7c5367ee7979830e28acb55627b957f2d`; universe manifest sha256 `5e01ac44…de450`; schema view sha256 `31dcb2b4…5c151`; clock 2026-02-14 00:00 UTC.
- Base files checked: gdrive/gdocs/gsheets/gslides/trello/gcal/linear `data.json`, slack `channels.json`, `users.json`, `messages/*.json`, contacts `contacts.json`, Gmail `users.json`, `labels.json`, `threads/*.json`.
- Any SQL change invalidates this review; rerun /injection, then /prompt, /hardness, /oe, /rubric.

### FINAL VERDICT: PASS

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Next action: Proceed to /prompt (optionally drop the 4 snapshot-mismatch columns first, then rerun /injection).

Evidence limits: Static review only; no SQL execution or live-database compatibility check. Schema snapshot is unverified, and 4 used columns are not covered by it (advisory). Agent visibility, discoverability and difficulty are out of scope (/prompt, /hardness).
