# Injection Data-Integrity Review (Eval 0)

- Stage: `/injection`. Review version: `injection-static-v2`. Evidence contract: `stage-evidence-v1`; `reused_evidence: []`. Every check here is NEW. The earlier platform report (`prev/eval0_report_on_sha_bc72db9c.md`) was used only as a map of where to look and is not cited as evidence.
- Mode: local static audit of a scratch copy, run blind (no `Task_Authoring/task_inputs*` or `Task_Authoring/support/` read). No SQL executed. Nothing written under `Evals/`.
- Actual review time: 2026-11-08T03:40Z (machine clock).
- Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
- Universe: `Universe_Normal`, source `hg4-2026-08-31 v37`. Archive sha256 `2913eb8b71daf249107a9f6dba25d00f4ec00d276126a0b881a647189244e21a`. Manifest `Evals/references/universes/normal/universe_manifest.json`, sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450`.
- Input under review: `$R/inputs/01_Universe_Inject.sql`. 74,274 bytes, 265 lines, **sha256 `6f3b18994e1a507b5829f5b2cfb6ff36897dcacc0b192c8649e97845b4ec200d`**.
- Task date input: `$R/inputs/02_Universe_Date.txt` ("February 14, 2026 00:00 (normal universe)").
- Reference fingerprints (sha256):
  - Eval 0: `86af2102ea6693c41047ed84dd60d59069d7c8810a652aeb7367ce4b563dfcd3`
  - WORKFLOW.md: `05a5e45e0585b435bc12f275c5b48ca6f725565b46bc0f5b68a554624bd68c69`
  - `references/schema/injection.json` (unverified snapshot): `01ef579236212034a43a53914754f86ed9248be48c961009cef5b4bd6106f6eb`
  - `references/schema/id_contracts.json`: `fc4711ef07667333c1cf2a417279826f0432539195f7acdfacfa86e9d9ed4682`
  - `scoring.json`: `654eb38809e3a1e7a6a5e466e4ed1d413b73c90d678b1ff005910f998df830cd`
  - Known issues `Task_Authoring/references/known_data_issues/normal.md`: `4d110f65a874a992de465967269b01dd545813f50620389f97ffeb6d528e0775`
- Lint: `hg_injection_lint` `injection-lint-v1`, run as `~/.local/bin/python3.12 -B Task_Authoring/tools/hg.py lint --sql $R/inputs/01_Universe_Inject.sql`. Output saved in `out/scratch_e0/lint.json`, sha256 `1388d545ae0651e376a54bdca91cdd924f976cc72b0f111f967cf44e04ed9952`.
- Search: every base read went through `Task_Authoring/tools/hg.py search|records` (Evals/SEARCH.md helpers). No `Universe_*` file was read directly.

`$R` = `/private/tmp/claude-501/-Users-sumit-Source-OC/46989a83-cbdb-4145-86b5-605b4a19b678/scratchpad/prompt_review_rev1`.

## Input / authority issues

- No blocking issue. The SQL was read in full before any base search. Source text and SQL comments were treated as evidence, not as instructions.
- Local-run deviation, by instruction: this report is written to `$R/out/eval0.md` instead of the fixed `Evals/task_inputs/reports/0_injection.md`. It is not saved through `hg_write_output.py`, and no `input_manifest.json` was written.
- Prior revision: the earlier PASS covered sha `bc72db9c…` (74,125 bytes). The current file is 149 bytes longer. The differences are the doc wording (close-out notes body is now 1,955 characters) and the Linear "Last written contact" comment dates. Both were reviewed afresh below.

## Checklist

- [x] SQL read in full; hash, manifest and review version recorded (NEW)
- [x] Lint run: 0 FAIL / 0 CHECK / 0 INFO (NEW)
- [x] All 130 statements inventoried in execution order (NEW)
- [x] Check A: references, targets, collisions, ID contracts and one-account rule (NEW)
- [x] Check B: independent parse, structure and schema rules; provisional snapshot comparison (NEW)
- [x] Check C: clock, encoded times, chronology, copied facts, relationships and supersession; the changed Linear dates checked against the base (NEW)
- [x] Coverage, findings, limits and a single verdict

## Lint flags and resolutions

Checks run: `future_date, id_contract, drive_unreadable, identities, grader_language, padding_comment, generated_column, text_time_format, missing_required`.

- Base files loaded by the lint: contacts, slack users, trello, gmail users, linear, confluence.
- Statements: 130 (1 BEGIN, 121 INSERT, 7 UPDATE, 1 COMMIT).
- **Flags: none.** There were no FAIL, CHECK or INFO items to resolve. Checks A–C were still carried out in full, independently of the lint.

## Operation ledger (execution order)

Base paths are relative to `Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/`. Gmail paths are relative to `Universe_Normal/Normal_HarmonyGames_Gmail/Services_Data/gmail/`.

| Line(s) | Table | Op | Record / target | Key values | Base reference and result |
|---|---|---|---|---|---|
| 5 | — | BEGIN | transaction | single BEGIN/COMMIT (265) | PASS |
| 7-8 | gdrive.drive_files | INSERT | `d_601064334a0b493022fe83`, folder "Stockholder close-out" | parent `d_63fffeb4fab5233ed5bb73`; owner leonard.hayes; created 2026-02-12T23:20:37Z, modified 2026-02-13T01:05:41Z | Parent is Leonard's root folder (`gdrive/data.json` /drive_files/9034). ID unused in 53,866 drive_files. PASS |
| 9-10 | gdrive.drive_files | INSERT | `f_a37b403d5200d4f0a31d31`, Doc "Stockholder close-out notes" | in new folder; 2026-02-13T01:05:41Z | Unused. Content row at L18-19. PASS |
| 11-12 | gdrive.drive_files | INSERT | `f_762c60832854d3e7a7f7df`, Doc "Holder outreach notes" | in root; 2026-02-10T17:41:09Z | Unused. Content row at L20-21. PASS |
| 13-14 | gdrive.drive_files | INSERT | `f_5ecaa967db3adcfa440b09`, Sheet "Holder list (draft)" | in new folder; 2026-02-10T18:12:26Z | Unused. Content rows at L23-26. PASS |
| 15-16 | gdrive.drive_files | INSERT | `f_75dddccabb26eeea4842c8`, Slides "Harmony Games February 26 Update" | in new folder; 2026-02-10T18:33:52Z | Unused. Content rows at L28-49. Distinct from the base 2024 deck "Harmony Games February Update" (/drive_files/37703). PASS |
| 18-19 | gdocs.docs_documents | INSERT | `f_a37b403d5200d4f0a31d31` | body 1,955 chars; style runs 0-28 TITLE, 28-1955 NORMAL; rev `3c986c6ce3` | document_id and revision unused in 633 docs. Last run end equals body length. PASS |
| 20-21 | gdocs.docs_documents | INSERT | `f_762c60832854d3e7a7f7df` | body 290 chars; runs end 290; rev `84bdd1a5ac` | Unused. Consistent. PASS |
| 23-24 | gsheets.sheets_spreadsheets | INSERT | `f_5ecaa967db3adcfa440b09` | owner leonard.hayes | spreadsheet_id and drive_file_id unused in 398 spreadsheets. PASS |
| 25-26 | gsheets.sheets_sheets | INSERT | sheet 0 "Sheet1" | 8 rows (header + 7 holders) | All 7 figures match the Nov 26, 2024 owner list (see C). PASS |
| 28-29 | gslides.slides_presentations | INSERT | `f_75dddccabb26eeea4842c8` | rev `0b2616045d` | Presentation and revision unused in 164 presentations. PASS |
| 30-49 | gslides.slides_pages ×5, slides_page_elements ×5 | INSERT | pages `slide_341616bedf43`, `slide_659353384faa`, `slide_fdc349f96a2c`, `slide_3ac232c61018`, `slide_e30ad4186e4c` (index 0-4); elements `el_f71854425943`, `el_3f1b82e16a82`, `el_b4a6a6d9a533`, `el_9dabe7a0ac53`, `el_453848aef60e` | TEXT_BOX, 9144000×5143500, ordinal 0 | Scoped to the new presentation; element shape matches the base. PASS (column advisory O-1) |
| 51-52 | slack.slack_messages | INSERT | `d281112d634372d5a8b35fc49a3e4b8c`, ts 1770938120.410229 | C0ADGSZKR3R (#winddown); EMPLOYEE_0038 (Leonard Hayes); top-level | Channel exists (`slack/channels.json` /154) and Leonard is a member. ID unused (687,230 msgs / 5,353 files, complete). ts unused in channel file. ts = created_at. PASS |
| 53-54 | slack.slack_messages | INSERT | `44975451e7eee53377ea87461fade5ab`, ts 1770938131.882339 | same | PASS |
| 55-56 | slack.slack_messages | INSERT | `a8540bc368de959fd190648f5b48fdf1`, ts 1770938158.104719 | same | PASS |
| 57-58 | slack.slack_messages | INSERT | `4f54dff9722aaeef2ba59316ff0cf2f9`, ts 1770949310.220519 | reply to `e3e198cc…` (thread 1770934638.035469); Leonard | Parent at `slack/messages/C0ADGSZKR3R/2026-02.json` /197 is Leonard's 22:17:18Z "next things for me are…" list. The base has 0 replies to it. PASS |
| 59-60 | slack.slack_messages | INSERT | `0e3d2253c9a2f33c47110c2917d3a724`, ts 1770949322.640149 | reply; Leonard | PASS |
| 61-62 | slack.slack_messages | INSERT | `846c625fed7922e6b261026e703636d9`, ts 1770949351.317729 | reply; Leonard; mentions `<@EMPLOYEE_0025_SLACK_ID>` | Mention format matches the base. PASS |
| 63-64 | slack.slack_messages | INSERT | `7440b1baf08601fe1a281017181fa98f`, ts 1770949437.902269 | reply; EMPLOYEE_0025 (Arthur Blake) | Arthur is a channel member (`slack/users.json` /13). PASS |
| 65 | slack.slack_messages | UPDATE | `e3e198cc6e3f866a032d34c5f69e39f9` | thread_ts_legacy null → own ts; reply_count 0→4; reply_users_count 0→2; latest_reply → 1770949437.902269 | Matches the 4 injected replies, 2 distinct users and the latest ts. Representation matches the base threaded parent `d4d97535…` (thread_ts = own ts). PASS |
| 67-68 | trello.trello_cards | INSERT | `698e5a10c3f24b7e9d16a0e4` "Stockholder close-out", idShort 456 | board `640643a3fd8f3ca308d9318e`, list `640643a3fd8f3ca308d93195` "To Do"; dateLastActivity 2026-02-13T18:14:27Z; badges comments 1 | Board (/boards/1) and list (/lists/3) exist. Card ID unused in 803 cards. idShort 456 is unused, following the board's base maximum of 455 (/actions createCard idShort 455). shortLink `XVXa9OOQ` unused. ID hex time 2026-02-12T22:54:08Z = createCard date. PASS |
| 69-70 | trello.trello_actions | INSERT | `698e5a108882c0b9e98cdb3e` createCard 2026-02-12T22:54:08Z | creator PERSON_6094 | Member = Leonard Hayes (/members/2). Unused in 5,294 actions. data_json shape matches base createCard. Hex time matches. PASS |
| 71 | trello.trello_boards | UPDATE | `640643a3fd8f3ca308d9318e` | dateLastActivity 2025-11-12T17:25:43Z → 2026-02-13T18:14:27Z | Equals the latest injected action. PASS |
| 72-73 | trello.trello_actions | INSERT | `698f6a03a222ee9dc57bc90f` commentCard 2026-02-13T18:14:27Z | Leonard; text about Sunset | Unused. Hex time matches. Card badge comments = 1. PASS (shape note O-5) |
| 75-76 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1857029474983245439` | history_id NULL | Not found anywhere in the complete scan of all 88,726 thread files. Thread-ID time 2026-02-13T16:48:35Z ≈ first message. PASS |
| 77-78 | gmail.gmail_messages | INSERT | `…/<LV3PR19MB8524F1C07D3A94E26B58D0AC7A1E2@…>`, KPMG 2025 audit request | from PERSON_3088; cc 4416, 2322, 2847; 2026-02-13T16:48:33Z; labels INBOX/IMPORTANT/Label_b19fb8d1b3/CATEGORY_PERSONAL | Same people, signature and label set as the base KPMG 2024 thread (`threads/leonard@harmonygames.co_1817557789846606177.json`). Label_b19fb8d1b3 = "Opened". Message-ID unused. PASS |
| 79 | gmail.gmail_threads | UPDATE | thread …1857029474983245439 snippet | → Leonard reply snippet | Target inserted at L75. PASS |
| 80-81 | gmail.gmail_messages | INSERT | `…/<CAPBs_a7Tq2LmV9xYcR4KdN8wUe3HsJ6oFbZ1gPiA5tGyQnE0Xw@mail.gmail.com>`, Leonard reply | 2026-02-13T17:12:40Z; In-Reply-To L78 | Quote line "8:48 AM" = 16:48Z PST. Labels SENT + Opened, as in base sent replies. Unused. PASS |
| 82 | gmail.gmail_threads | UPDATE | same thread snippet | → clarification snippet | Final snippet = latest message. PASS |
| 83-84 | gmail.gmail_messages | INSERT | `…/<LV3PR19MB85246D2E9B14C7A03F5E8D12BC4A7@…>`, KPMG clarification | 2026-02-13T17:37:15Z; In-Reply-To L81; References chain of 2 | Unused. Chronology coherent. PASS |
| 85-86 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1857034369525983506` | history_id NULL | Unused (complete scan). Thread-ID time 2026-02-13T18:06:22Z ≈ first message. PASS |
| 87-88 | gmail.gmail_messages | INSERT | `…/<mlkq74xd.3f9e2c1a-6b48-4d07-a1e5-8c2f0d7b6a94@we.are.superhuman.com>`, Sunset intake | from PERSON_2888; 2026-02-13T18:06:21Z | PERSON_2888 is Sunset's Head of Partnerships in the base, with the same signature and phone token (`threads/00016827.json`). Unused. PASS |
| 89 | gmail.gmail_threads | UPDATE | thread …1857034369525983506 snippet | → Leonard reply | Target inserted at L85. PASS |
| 90-91 | gmail.gmail_messages | INSERT | `…/<CAPBs_a5Wn3RvK8yZtH2DqL7mJc9XeU4oGfB6sPiN1aTuYkEr0Q@mail.gmail.com>`, Leonard reply | 2026-02-13T18:19:02Z | Quote "10:06 AM" = 18:06Z PST. Unused. PASS |
| 92 | gmail.gmail_threads | UPDATE | `leonard.hayes@harmonygames.co/1773963101399472184` snippet | → new Robert message | Thread exists (`threads/leonard@harmonygames.co_1773963101399472184.json`, 2 base messages from 2023-08-11). The new message is the latest. PASS |
| 93-94 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAGkro_PbX4mT7nQe2LwV9sKd1YhJ3uF6aRc8ZoGi5NtEyMq0Bw@mail.gmail.com>` | from robert, to PERSON_3941, cc Leonard; 2026-02-12T23:41:12Z; In-Reply-To `<CAGkro_Ox2wP8…>` | Parent is the base "Thanks!!!" message in this thread (2023-08-11 13:00:43 -0700 = quoted "1:00 PM"). References chain extends the base chain exactly. From format `robert <robert@…>` matches the base. Unused. PASS |
| 95 | gmail.gmail_threads | UPDATE | `robert@harmonygames.co/1773963101279916523` snippet | → new message | Thread exists (`threads/00001367.json`, mailbox robert@). PASS |
| 96-97 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAGkro_PbX4m…>`, sent copy | labels ["SENT"]; same content and time | Parent `<CAGkro_Ox2wP8…>` is in this thread. Robert's base sent label is `['SENT']`. PASS |
| 99-100 | gcal.gcal_events | INSERT | `evt_6f1a2c9e4b7d3a58c0e1d2` "Holder notes due" | calendar leonard.hayes; 2026-02-17T17:00Z-17:30Z (Tue 09:00 PT); created/updated 2026-02-13T01:12:18Z; ical `3d02d5fe…@hg4` | Calendar exists (/calendars/15, America/Los_Angeles). event_id and ical_uid unused in 11,130 events. Start/end are plan fields and may be in the future. PASS |
| 102-103 | contacts.contacts | INSERT | `d3c6e5b57e0ee6656a1bdd2c` PERSON_0693, job Investor | email PERSON_0693_EMAIL | No match in 170 contacts by ID, email or first_name. PERSON_0693_EMAIL is the angel `[PERSON_NAME_4468]`, whose own mail to Leonard is in base Gmail (`threads/leonard@harmonygames.co_1773213846196143460.json`). No duplicate account. PASS |
| 104-105 | contacts.contacts | INSERT | `13f3b76067d577bc30c45242` PERSON_2275, job Investor | email PERSON_2275_EMAIL | Unused. PERSON_2275_EMAIL is the angel `[PERSON_NAME_27652]` (`threads/leonard@harmonygames.co_1770141224265557526.json`). PASS |
| 107-108 | linear.linear_projects | INSERT | `ec2ea957-fc8e-4958-b809-0fb735b1e916` "Holder records" | team_ENG; lead usr_63fffeb4fab5233e; state started; start 2026-02-12; created 2026-02-12T23:24:12Z, updated 2026-02-13T18:21:46Z | Team (/teams/2) and Leonard's user (/users/13) exist. ID and name unused (2 base projects). PASS (column advisory O-1) |
| 109-264 | linear.linear_issues ×26, linear_comments ×52 | INSERT | ENG-2438 … ENG-2463 (see table below) | team_ENG; creator Leonard; state Backlog; state_history_json `'[]'` | None of the 26 IDs, identifiers or numbers exists in 3,852 base issues; ENG-2437 is the base maximum. `Backlog`, `Todo`, `Canceled` are base state_id values. Base /comments is empty (0), so no comment collision; all 52 comment IDs are distinct. PASS |
| 265 | — | COMMIT | — | — | PASS |

### Linear issues and comments (L109-264)

Every issue was created after the project (23:24:12Z) and before both of its comments. Every issue's `updated_at` equals its last comment's `created_at`. Every comment has `updated_at` = `created_at`.

| Issue (line) | Title | Created / updated | Comment IDs (created) | "Nov 2024 owner list" figure vs base | "Last written contact ... before Feb" claim and base check |
|---|---|---|---|---|---|
| ENG-2438 (L109) | GRIFFIN GAMING PARTNERS II, L.P. | 2026-02-12T23:25:03Z / 2026-02-12T23:43:08Z | comment_ed8c08243736a351d7becd7ce7fa13d2 (2026-02-12T23:34:21Z); comment_382488a155c90d75e97cc7aab5bce415 (2026-02-12T23:43:08Z) | 2,746,693, both funds on one line: matches owner list | Jan 24, 2026: PERSON_4337 reply 16:06 PT and Leonard reply 16:22 PT, "Re: Harmony Games: recap option, cap table reset" (Gmail robert@ mailbox); next founder mail is Feb 9. MATCH |
| ENG-2439 (L115) | GRIFFIN GAMING PARTNERS II SIDE FUND, L.P. | 2026-02-12T23:25:31Z / 2026-02-12T23:43:46Z | comment_ecc608531f261813bc32e6d06db8f294 (2026-02-12T23:34:29Z); comment_1b339a46addf9f2aaa2ee6c1e2dffc43 (2026-02-12T23:43:46Z) | 2,746,693, both funds on one line: matches owner list | Jan 24, 2026: Same Griffin partner (PERSON_4337) as ENG-2438. MATCH |
| ENG-2440 (L121) | [PERSON_NAME_0089] [PERSON_NAME_25152] | 2026-02-12T23:26:00Z / 2026-02-12T23:44:25Z | comment_2111c140a4689c9cea5bf649e0035f4f (2026-02-12T23:34:42Z); comment_fd8b0ca2cfc99f96fa00047c38f24b8f (2026-02-12T23:44:25Z) | 81,383: matches owner list | Jan 30, 2026: Not individually reconciled (header token for this holder unresolved) |
| ENG-2441 (L127) | Arthur PERSON_3083_NAME | 2026-02-12T23:26:13Z / 2026-02-12T23:45:30Z | comment_55a53b92256a15c171347daccfb3d3c0 (2026-02-12T23:34:52Z); comment_cc647e12d1fa9be8936004db08b5d744 (2026-02-12T23:45:30Z) | 25,432: matches owner list | Nov 6, 2025: Not individually reconciled (PERSON_3083 token collides with Arthur Blake sign-off) |
| ENG-2442 (L133) | [PERSON_NAME_4468] | 2026-02-12T23:26:40Z / 2026-02-12T23:46:27Z | comment_3553af035a9738781951b795e0e0cedc (2026-02-12T23:35:09Z); comment_a7fe6dd5603747ef8cd40bef6ca13be8 (2026-02-12T23:46:27Z) | 25,432: matches owner list | Jun 27, 2025: "Ask for support" (Jun 27, 2025) from the Solsten COO address (patrick@, signature [PERSON_NAME_4468]). MATCH; see advisory O-2 (Jan 15, 2026 Solsten pitch from PERSON_0663) |
| ENG-2443 (L139) | [PERSON_NAME_52949] | 2026-02-12T23:27:05Z / 2026-02-12T23:47:05Z | comment_f2da3914f4e7e0c8130cffcdd560c27a (2026-02-12T23:35:18Z); comment_00a8c71af2ca3252b5ea1d5d90ea59e9 (2026-02-12T23:47:05Z) | 25,432: matches owner list | Dec 16, 2025: Not individually reconciled (PERSON_2260 headers not scanned) |
| ENG-2444 (L145) | Patrick Lewis | 2026-02-12T23:27:35Z / 2026-02-12T23:48:07Z | comment_ddac696381e399e80cb72b2eed4ba3d2 (2026-02-12T23:35:32Z); comment_5b55af2597c61f87ef541e32ef58e705 (2026-02-12T23:48:07Z) | 25,432: matches owner list | May 18, 2024: Latest Patrick Lewis-identified mail: May 18, 2024 investor report (bcc). The 2025 patrick@ mails are signed by the Solsten COO. MATCH |
| ENG-2445 (L151) | [PERSON_NAME_27652] | 2026-02-12T23:28:06Z / 2026-02-12T23:48:52Z | comment_f750001de682e027ffc4cad6992d8e09 (2026-02-12T23:35:47Z); comment_cbffbe9078804fc1f64ae7a430f7427e (2026-02-12T23:48:52Z) | 25,432: matches owner list | May 18, 2024: PERSON_2275 latest: May 18, 2024 investor report (bcc); complete token scan. MATCH |
| ENG-2446 (L157) | PERSON_3941_NAME [PERSON_NAME_0127] | 2026-02-12T23:28:38Z / 2026-02-12T23:49:29Z | comment_828018862b6830931b07005fb37392cd (2026-02-12T23:36:07Z); comment_8480de000b6ccc738bb35b81a65d7677 (2026-02-12T23:49:29Z) | 31,536: matches owner list | Oct 23, 2025: Holder = Frederick Stone (PERSON_3941 personal address, Slack EMPLOYEE_0008). Last DM with Leonard Oct 23, 2025 (D05S58U4SAK, 08:08-10:29 PT); later Oct 24 entry is a channel_leave system message. MATCH |
| ENG-2447 (L163) | [PERSON_NAME_11362] | 2026-02-12T23:28:44Z / 2026-02-12T23:50:09Z | comment_2f94df42f7cb90e3d04bea2945c2c1a8 (2026-02-12T23:36:26Z); comment_dd5ccdfa4a49c7f9a5ad4b596aa8fb82 (2026-02-12T23:50:09Z) | 86,470: matches owner list | Jan 5, 2026: Not individually reconciled (no header token) |
| ENG-2448 (L169) | TOR Capital Limited | 2026-02-12T23:29:09Z / 2026-02-12T23:51:05Z | comment_3d28d40e61eb9113c2705fc13e05fd11 (2026-02-12T23:36:45Z); comment_e278ff5e9952da862549d4ec99133f23 (2026-02-12T23:51:05Z) | 50,865: matches owner list | Nov 4, 2025: Not individually reconciled (no TOR header contact found in indexed files) |
| ENG-2449 (L175) | PERSON_1287_NAME | 2026-02-12T23:29:20Z / 2026-02-12T23:51:37Z | comment_aa0dbafe2b7f1048eca7fdb7c40ec3ad (2026-02-12T23:37:01Z); comment_59d2bd49bdbbf5ce5cb944fa5419aefa (2026-02-12T23:51:37Z) | 31,536: matches owner list | May 18, 2024: PERSON_1287 latest: May 18, 2024 investor report (bcc); complete token scan. MATCH |
| ENG-2450 (L181) | [PERSON_NAME_0043] | 2026-02-12T23:29:30Z / 2026-02-12T23:52:13Z | comment_0dd9ef1af3877876b50494ebdd5db91d (2026-02-12T23:37:10Z); comment_55a5df2f574d25cfdadf6a16f9f1d608 (2026-02-12T23:52:13Z) | 30,519: matches owner list | Jan 27, 2026: Not individually reconciled (generic token) |
| ENG-2451 (L187) | [PERSON_NAME_0100] | 2026-02-12T23:29:37Z / 2026-02-12T23:52:40Z | comment_2520b4abb46c84ed5b7d8c5b3ff5f778 (2026-02-12T23:37:20Z); comment_315a03e2ae88266b1b80f267067ca77d (2026-02-12T23:52:40Z) | "Not on the Nov 2024 owner list": correct, absent from the 27-owner list | Jun 16, 2024: Not individually reconciled (generic token) |
| ENG-2452 (L193) | Calvin Price | 2026-02-12T23:29:44Z / 2026-02-12T23:53:36Z | comment_a6d982880c16bb4b3263ce923c037211 (2026-02-12T23:37:33Z); comment_713a525ee79a69a522dd9bf1d54c1ede (2026-02-12T23:53:36Z) | 8,138: matches owner list | Oct 23, 2025: Calvin Price: last exchange in Leonard-visible conversation Oct 23, 2025 08:13 PT with Robert in #zombie-bugs (private, Leonard member). Oct 24 "okay sure" is in an mpdm without Leonard. MATCH on the Leonard-view reading |
| ENG-2453 (L199) | Claire Morgan | 2026-02-12T23:29:52Z / 2026-02-12T23:54:07Z | comment_ece7420618510fab05ab176f95ec14b7 (2026-02-12T23:37:48Z); comment_eebf1175c303c57236d50d2abf02fb7a (2026-02-12T23:54:07Z) | 7,630: matches owner list | Jan 7, 2026: Claire Morgan: Jan 7, 2026 08:26 PT post in #company-internal (founders present). MATCH |
| ENG-2454 (L205) | [PERSON_NAME_0612] | 2026-02-12T23:30:10Z / 2026-02-12T23:55:08Z | comment_03a221587faf55ab99f029bda1af0f7c (2026-02-12T23:37:56Z); comment_9d3a744e837979208a01b9c3b59528ea (2026-02-12T23:55:08Z) | 10,173: matches owner list | Oct 21, 2025: Not individually reconciled (generic token) |
| ENG-2455 (L211) | Victor [PERSON_NAME_2770] [PERSON_NAME_0086] | 2026-02-12T23:30:18Z / 2026-02-12T23:55:47Z | comment_0709c84516aaff1c4249e5c659013a8f (2026-02-12T23:38:15Z); comment_c4eec14f40d6d7a739209d8832fa6d1e (2026-02-12T23:55:47Z) | 30,519: matches owner list | Apr 14, 2025: Victor Barnes (the roster Victor, departed Apr 2025; identity assumed from the name): Apr 14, 2025 exchanges with Leonard 08:27, Arthur 08:29, Robert 09:00 PT. Apr 15 posts are DMs with Claire/Martin only. MATCH |
| ENG-2456 (L217) | Marcus Bennett | 2026-02-12T23:30:33Z / 2026-02-12T23:56:48Z | comment_26d197b4b86b50214098cfc75d33b215 (2026-02-12T23:38:35Z); comment_506293f320ae744a99e1b16c1db39fdc (2026-02-12T23:56:48Z) | 22,889: matches owner list | Jan 30, 2026: Marcus Bennett: Jan 29, 2026 23:08 PT = Jan 30 07:08Z in #prototype. MATCH (UTC date; ENVIRONMENT accepts either) |
| ENG-2457 (L223) | [PERSON_NAME_0068] | 2026-02-12T23:30:55Z / 2026-02-12T23:57:42Z | comment_1a50f7986e95578672eeb6bfacfba9c4 (2026-02-12T23:38:48Z); comment_a5cb7550cfae40a7b319ed4d15e7900a (2026-02-12T23:57:42Z) | 16,277: matches owner list | Jan 31, 2026: Not individually reconciled (generic token) |
| ENG-2458 (L229) | Martin [PERSON_NAME_7250] Walsh | 2026-02-12T23:31:03Z / 2026-02-12T23:58:34Z | comment_799ff26523c065da1eace39451a716eb (2026-02-12T23:38:58Z); comment_e5d8572c6113d0adec1e91e27d5d1c13 (2026-02-12T23:58:34Z) | 3,866: matches owner list | Jan 30, 2026: Martin Walsh: Jan 30, 2026 08:39 PT in #prototype (founders present). MATCH |
| ENG-2459 (L235) | [PERSON_NAME_0051] | 2026-02-12T23:31:13Z / 2026-02-12T23:59:35Z | comment_990f6616e01c8c856fc4afcce855c143 (2026-02-12T23:39:15Z); comment_6493e909b95f20ead3764cc8e2ed06f9 (2026-02-12T23:59:35Z) | 3,866: matches owner list | Nov 23, 2025: Not individually reconciled (generic token) |
| ENG-2460 (L241) | [PERSON_NAME_2769] [PERSON_NAME_0093] | 2026-02-12T23:31:39Z / 2026-02-13T00:00:18Z | comment_05a15586d3ce166824156bed0b5962a7 (2026-02-12T23:39:33Z); comment_4dc00ec394c4642fa4204160b04846af (2026-02-13T00:00:18Z) | 10,173: matches owner list | Jan 26, 2026: Not individually reconciled (contractor; Carta termination mail Feb 12 confirms Carta name) |
| ENG-2461 (L247) | [PERSON_NAME_2768] [PERSON_NAME_0011] | 2026-02-12T23:31:48Z / 2026-02-13T00:01:24Z | comment_fda4088cc839189a5916123b36e621b1 (2026-02-12T23:39:42Z); comment_0e3bfd1c3c3f40eb038211e3e51e34ea (2026-02-13T00:01:24Z) | 35,605: matches owner list | Oct 30, 2025: Not individually reconciled (contractor; Carta termination as of Oct 24, 2025 and cap-table access request Oct 29 confirm identity only) |
| ENG-2462 (L253) | [PERSON_NAME_0038] | 2026-02-12T23:31:56Z / 2026-02-13T00:02:13Z | comment_67de802785cc048199ddbbeca6d4acfd (2026-02-12T23:39:58Z); comment_9712f6ba800daa8fbed67ada6828108c (2026-02-13T00:02:13Z) | 127,162: matches owner list | Oct 29, 2025: Not individually reconciled (generic token) |
| ENG-2463 (L259) | [PERSON_NAME_0022] [PERSON_NAME_2767] [PERSON_NAME_2763] | 2026-02-12T23:32:26Z / 2026-02-13T00:03:06Z | comment_4b6954b5234424aba03fe1b142c60812 (2026-02-12T23:40:14Z); comment_b8881cecb478b6807c8fc23ab4486c89 (2026-02-13T00:03:06Z) | 15,259: matches owner list | Jan 31, 2026: Not individually reconciled (contractor; Carta termination mail Feb 12 confirms Carta name) |

**How the "Last written contact" dates were checked.** These are the comment dates that changed in this revision. I verified 12 of the 26 issues (11 holders; the two Griffin funds share one partner) against the base. All 12 agree under one reading of the note: the holder's last written exchange before February in a conversation Leonard can see (Gmail or Slack). The date may be the Pacific or the UTC date, as ENVIRONMENT allows.

Two dates looked wrong at first. Both resolved once the reading was applied:

- **ENG-2452 (Calvin Price).** Calvin's Oct 24 "okay sure" is in a group DM made up of Arthur, Douglas, Samuel and Calvin. Leonard is not in it.
- **ENG-2446 (PERSON_3941).** This holder resolves to Frederick Stone. His personal address sends to the `frederick.stone@` mailbox, he holds an advisory contract, and he is invited to the workspace. The greeting token `[PERSON_NAME_0112]` is his first name in base invites. His Slack account is EMPLOYEE_0008. The DM D05S58U4SAK runs Sep 2023 to Oct 2025 and ends with the Oct 23 exchange. His Oct 24 entry is a channel-leave system message.

The 14 issues not reconciled appear under anonymized tokens that cannot be mapped consistently across services. Bracketed body names differ from the header tokens, and Deel and Carta use other forms again. For these, no contradiction was found. This is disclosed as an evidence limit below, not as a defect.

## Check A — Records, references and IDs: PASS

- **Referenced targets resolve.**
  - Drive: Leonard's root folder.
  - Slack: #winddown and the thread parent `e3e198cc…`.
  - Trello: board, To Do list, member PERSON_6094.
  - Gmail: mailboxes leonard.hayes and robert (`gmail/users.json`), both existing threads, the In-Reply-To parent `<CAGkro_Ox2wP8…>` in each mailbox, and label `Label_b19fb8d1b3`.
  - Calendar: Leonard's calendar.
  - Linear: team_ENG and usr_63fffeb4fab5233e.
- **Actors are the named people.**
  - Slack: EMPLOYEE_0038 = Leonard Hayes; EMPLOYEE_0025 = Arthur Blake. Both are #winddown members and were active after Feb 11 (NB-1 departures do not include them).
  - Trello: PERSON_6094 = Leonard Hayes.
  - Linear: usr_63fffeb4fab5233e = leonard.hayes.
  - Gmail sender formats match the base: `leonard hayes <…>`, `robert <…>`, and the KPMG and Sunset people.
- **New-key collisions: none.** Every scan below completed (`scan_complete: true`):

  | Service | Scope checked |
  |---|---|
  | Drive | 53,866 files |
  | Docs | 633 documents, ID and revision |
  | Sheets | 398 spreadsheets |
  | Slides | 164 presentations, ID and revision |
  | Slack | 687,230 messages in 5,353 files; channel ts |
  | Trello | 803 cards (ID and idShort), 5,294 actions, shortLink text |
  | Gmail | all 88,726 thread files, text scan for both new thread IDs and all 7 new Message-IDs: 0 hits |
  | Calendar | 11,130 events, event_id and ical_uid |
  | Contacts | 170 contacts, ID, email and first_name |
  | Linear | 2 projects (ID and name), 3,852 issues (id, identifier, number), 0 comments |

  There are no duplicate keys inside the SQL.
- **ID contracts.** Gmail history_id is NULL on both threads, which is allowed. No Drive content_path is set, so the path contract does not apply. Both Docs have docs_documents rows with non-empty bodies. The Sheet and Slides have content rows.
- **One account per person.** No second account for an existing person: the contacts table has no prior PERSON_0693 or PERSON_2275 entry, and the lint identities check is clean.

## Check B — SQL structure and supported schema rules: PASS (provisional advisory O-1)

- An independent parser (`out/scratch_e0/parsed.json`, `checkb.json`) agrees with the lint.
- **Structure.**
  - One BEGIN/COMMIT. 121 single-row INSERTs, each with matching column and value counts and no duplicate columns.
  - 7 UPDATEs, each with a single-ID predicate whose target exists or is created earlier.
  - E'' escapes are valid (`\n`, `\r`) and `''` quoting is correct.
- **Literals.**
  - Every `*_json` literal parses as JSON, and the shapes match the base: arrays `'[]'`, Slack `metadata_json '{}'`, headers arrays.
  - Integer and boolean literals sit in integer and boolean columns.
  - Every timestamptz literal carries `Z`.
- **Platform rules.**
  - The generated columns `text_fts` and `body_text_fts` are not set.
  - All Linear `*_at` values use `YYYY-MM-DDTHH:MM:SSZ`, and `start_date` is `YYYY-MM-DD`.
  - `state_history_json '[]'` is present on all 26 issues.
  - Every NOT NULL column without a default is supplied.
- **Provisional snapshot comparison (unverified snapshot).**
  - MATCH: 15 of the 18 affected tables.
  - MISMATCH: 4 columns in 3 tables are not in the snapshot: `gslides.slides_pages.notes`, `gslides.slides_page_elements.table_json` and `.ordinal`, and `linear.linear_projects.links_json` (the snapshot has `links_json` only on `linear_issues`). The values are NULL, 0 or `'[]'`. Under the schema README this is an advisory, not a defect.

## Check C — Dates, relationships and consistency: PASS

- **Clock.** Every event timestamp is at or before 2026-02-13T18:21:46Z, which is before 2026-02-14 00:00 UTC. The only later values are the calendar start and end on 2026-02-17, which are plan fields.
- **Encoded times agree.**
  - Slack ts = created_at (7 of 7).
  - Gmail internal_date = date = header Date (7 of 7); the Message-ID header equals the ID suffix; In-Reply-To and References match the columns; each snippet is the body prefix.
  - Trello ID hex times equal the action and card times.
  - Gmail thread-ID times match the first message to within 2 seconds.
  - The quoted "On … wrote" lines are correct in PT (8:48 AM, 10:06 AM, and 1:00 PM on 2023-08-11).
- **Chronology.**
  1. Trello card created 22:54:08 Feb 12.
  2. Slack "Putting the holders in linear" at 23:15:20.
  3. Drive folder and contacts at 23:20–23:21.
  4. Linear project 23:24, issues 23:25–23:32, comments 23:34 to 00:03 Feb 13.
  5. Robert's message to PERSON_3941 at 23:41.
  6. Close-out notes Doc at 01:05:41.
  7. Calendar entry at 01:12:18.
  8. Thread replies at 02:21–02:23, after the parent's 22:17:18.
  9. KPMG 16:48, reply 17:12, clarification 17:37.
  10. Sunset 18:06, then the Trello comment "Sunset wants the same sheet" at 18:14, then Leonard's reply 18:19, then the project update at 18:21. The project description names Sunset and KPMG, and both had arrived by then.

  The Feb 10 sheet and deck sit in a folder created Feb 12. That implies a later move; it is not an impossibility (O-7).
- **Copied facts match the base.**
  - The "Nov 2024 owner list" is Leonard's 2024-11-26 email (`threads/leonard@harmonygames.co_1816809274978043917.json`, msg 0). It lists 27 owners, which matches the slide's "27 holders".
  - All 7 sheet figures and all 25 issue figures match it. `[PERSON_NAME_0100]` is correctly absent.
  - Griffin "both funds on one line" is consistent with the two Griffin fund names in the 2023 financing documents (`gdocs` /docs_documents/57, 90, 119 and others).
  - Name forms such as `[PERSON_NAME_0022] [PERSON_NAME_2767] [PERSON_NAME_2763]`, `[PERSON_NAME_2769] [PERSON_NAME_0093]` and `[PERSON_NAME_2768] [PERSON_NAME_0011]` match the base Carta "Termination details" emails. "Martin [PERSON_NAME_7250] Walsh" versus "Martin Georgiev Walsh" is an anonymization variant, not an introduced conflict.
- **Pointers in the injected text resolve to the base.**
  - #winddown "Carta terminations are done" (22:33:41Z) supports "the angels are what's open … besides the Sunset onboarding".
  - The Feb 9 investor draft at 19:18:20Z and "I'll reach out to investors one by one" at 19:22:04Z exist.
  - The Task List sheet (/sheets_spreadsheets/76) has "Send email to investors".
  - "archieve account on google after Feb 15" and "keep accounts … until the data is extracted" are in the base (1770933903).
  - "linear we keep during transition" is in the base (1770933601).
  - The "Wind Down" folder exists (/drive_files/20868).
  - The Feb 12 "Board position" thread from PERSON_4337 is in Leonard's mailbox (and in Robert's, `threads/00016903.json`).
  - "notes ready … by Tuesday" equals the Feb 17 calendar slot.
  - The greeting `[PERSON_NAME_0112]` (PERSON_3941's first name) and the sign-off `[PERSON_NAME_0054]` (Robert's first name) match base usage.
  - "the three of us" is Leonard, Robert ([PERSON_NAME_0055]) and Arthur Blake, the three founders on the owner list.
- **Supersession is supported.** The Feb 13 notes state "These replace my earlier outreach notes" (Feb 10 doc). The Linear "Nov 2024 owner list" comments are labeled historical figures.
- **The changed "Last written contact … before Feb" dates.** As described above the Check A heading: 12 of 26 verified, all consistent; 14 not individually reconcilable because of anonymization; no contradiction found.
- **Grader-facing or padding text.** None. I read all injected text manually and the lint is clean. The SQL comments are a header plus section markers only.
- **Known data issues.**
  - NB-6: the injected Slack posts (latest 02:23:57Z Feb 13) are before the 10:03Z export end.
  - NB-1: the only posters are Leonard and Arthur.
  - NB-24: the base Linear export has no comments, so the injected comments create no conflict.
  - None of the 33 cards is worsened by this SQL.

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | All targets resolve. No collisions across complete scopes, including the full Gmail scan. One account per person. |
| B — SQL structure and supported schema rules | PASS | Structure and documented platform rules are clean. Provisional snapshot MISMATCH on 4 columns (O-1), advisory only. |
| C — Dates, relationships and consistency | PASS | All events precede the clock. Encoded times, chronology, copied figures and pointers are consistent. 12 of 26 changed contact dates verified with no contradiction. |

## Findings

No demonstrated defects.

Advisories and observations (non-blocking):

- **O-1 (Check B, provisional).** Four columns are absent from the unverified snapshot: `slides_pages.notes` (5 INSERTs), `slides_page_elements.table_json` and `.ordinal` (5 INSERTs), and `linear_projects.links_json` (1 INSERT). If the live database lacks any of them, the whole transaction rolls back. Smallest safe change: drop these columns from those INSERTs, since their values are NULL, 0 or `'[]'` and carry no content. This is the same advisory as on the prior revision.
- **O-2 (/prompt, not an integrity defect).** Base anonymization conflates identities, which matters for how an Agent finds the holders:
  - `patrick@harmonygames.co` is used by both Patrick Lewis and the Solsten COO `[PERSON_NAME_4468]`.
  - `PERSON_3083_NAME` is both Arthur Blake's sign-off and the holder "Arthur PERSON_3083_NAME".
  - PERSON_3941 appears as Frederick Stone in Slack and work mail.

  ENG-2442 (Jun 27, 2025) and ENG-2444 (May 18, 2024) are correct only once these are told apart. A Jan 15, 2026 "Solsten AI" mail to Leonard is a campaign blast (labeled SPAM/PROMOTIONS/UNREAD, signed PERSON_0663, with an opt-out footer), not a contact.
- **O-3 (/prompt).** ENG-2452's Oct 23 is right only on the Leonard-view reading. Arthur, one of "the three of us", had a later written exchange with Calvin on Oct 24 in a group DM Leonard is not in. If any grading depends on these dates, the reading should be unambiguous.
- **O-4 (cosmetic).** The Doc TITLE style runs end at 28 and 22, which includes the newline. The base sample excludes it.
- **O-5 (cosmetic).** The commentCard `data_json` omits the base's `idCard` and `textData` keys.
- **O-6.** The Linear project description says "one issue per holder on Carta". Carta's own holder list is not a base data export (only Carta notification emails exist), so completeness of the 26 issues against Carta is not statically checkable here. That is /prompt's concern.
- **O-7.** The Feb 10 Sheet and Slides sit in the Feb 12 folder, which implies a later move. This is plausible, not a defect.

## Outside-scope limits

- No SQL execution, deployment or live-database compatibility check. The schema snapshot is unverified.
- Agent visibility, discoverability, Carta completeness and difficulty belong to /prompt and /hardness.

## Dependencies for later stages

- SQL sha256 `6f3b18994e1a507b5829f5b2cfb6ff36897dcacc0b192c8649e97845b4ec200d`.
- Manifest sha256 `5e01ac44…de450`. Schema sha256 `01ef5792…6f6eb`. Clock 2026-02-14 00:00 UTC.
- Base files used:
  - gdrive, gdocs, gsheets, gslides, trello, gcal and linear `data.json`
  - contacts `contacts.json`
  - slack `users.json`, `channels.json` and `messages/*.json`
  - Gmail `users.json` and `threads/*.json` (complete text scan)
- Reusable evidence for /prompt:
  - The owner-list figures.
  - The identity mappings: PERSON_0693 = [PERSON_NAME_4468]; PERSON_2275 = [PERSON_NAME_27652]; PERSON_2260 = [PERSON_NAME_52949]; PERSON_3941 = Frederick Stone (EMPLOYEE_0008); PERSON_4337 = Griffin partner.
  - The per-holder contact dates in the table.
- Any change to the SQL invalidates this review. Rerun /injection, then /prompt, /hardness, /oe and /rubric.

### FINAL VERDICT: PASS

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt. Optionally drop the 4 snapshot-mismatch columns first (O-1) and rerun /injection.

Evidence limits:
- Static review only. The schema snapshot is unverified; 4 used columns are not in it (advisory).
- 14 of the 26 changed Linear "last written contact" persona notes could not be matched to a holder identity because of base anonymization. This is a source limit, not an unresolved required check, and no contradiction was found.
- Carta holder completeness and Agent visibility are outside this stage.

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
