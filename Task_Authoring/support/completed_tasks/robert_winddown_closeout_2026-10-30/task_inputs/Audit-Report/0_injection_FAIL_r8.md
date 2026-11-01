# Injection data-integrity review — `injection-static-v2`

## 1. Scope

| Field | Value |
|---|---|
| Review | Chat review for your attempt (6adfee3f27ce6ca81b457137), `/injection`, static audit mode |
| Review version | `injection-static-v2` (evidence contract `stage-evidence-v1`) |
| Actual review time | 2026-10-28T13:29Z |
| Clock | 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal` (hg4-2026-08-31 v37); manifest `Evals/references/universes/normal/universe_manifest.json` sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Input reviewed | Injection SQL, revision 11 (attachment `01_Universe_Inject (8).sql`, saved as `Evals/task_inputs/01_Universe_Inject.sql`), 113,333 bytes, sha256 `567d031b5ecfbf10e20b3ef3f9d34389777ae58b96786ab8555c426bb7701069` |
| Previous version | Revision 10, SQL sha256 `8dc03aba83352cfc6e55461c74ce57e210247a29e0138c1f378cbddda34e87b5`, reviewed in report sha256 `444b0395e9ed023627c4a68bde4c07af8985c9e6ac5404787883efa87bb70e2b` (PASS / COMPLETE) |
| References (re-hashed this run, unchanged since that report) | Eval 0 `e034019b…6f663eff`; WORKFLOW `ee4cd8e1…504fcd5d`; schema snapshot `31dcb2b4…d74c5151`; schema README `9e320787…9a76eb42`; `id_contracts.json` `fc4711ef…d9ed4682`; ENVIRONMENT `4ffb2b5f…a5d5e165`; SEARCH `cab83c61…c9d3a45c`; roster `3f217451…b3c84575`; acl `e9bca2b3…04468c9f`; known_base_issues `79b20289…e7553a7b` |

## 2. Input / authority issues

- The only input for this stage is the SQL. It is substantive: 147 statements (BEGIN, 138 INSERT, 7 UPDATE, COMMIT) across gdrive, gdocs, gsheets, confluence, slack, trello, gmail, gcal, github and linear. The header comment's counts ("138 INSERT … 7 UPDATE") match the parse.
- Header comments are authoring notes; none mention tool calls, pass rate or gates.
- `known_base_issues.md` lists no normal-universe conflicts. Revision 11 now **edits a base file**: the January P&L spreadsheet `f_605121f4a36752645e0ac3`. That file exists in two base stores (the Sheets grid and the Drive file's xlsx bytes), which is the subject of finding F1.

**Change set from revision 10 (statement-level diff):** 134 statements are byte-identical. Revision 10's 150 statements become 147: 16 statements removed or changed, 13 added or changed.

| Rev-10 line → Rev-11 line | Record | Change |
|---|---|---|
| — → 13 | `gdrive.drive_files` UPDATE `f_605121f4a36752645e0ac3` (base P&L file) | **New.** `modified_time` 2026-01-12T20:25:34Z → 2026-02-13T16:31:07Z |
| — → 22 | `gsheets.sheets_sheets` UPDATE spreadsheet `f_605121f4a36752645e0ac3`, `sheet_id = 2` ("HG Costs") | **New.** Replaces the whole `grid_json`. Cell-by-cell against the base: only header row cells 21–43 (columns V–AR) change, each year +1 (e.g. AF `2024-12-25T00:00:00` → `2025-12-25T00:00:00`, AR `2025-12-26` → `2026-12-26`). All 75 rows × 44 columns of data are value- and type-identical to the base |
| — → 23 | `gsheets.sheets_spreadsheets` UPDATE `f_605121f4a36752645e0ac3` | **New.** `modified_time` → 2026-02-13T16:31:07Z |
| 14 → 15 | `gdocs.docs_documents` `f_1326e66bcabfda8fd29e4a` (conventions doc) | Rule 8: removed "whatever the costs tab shows" and the positional note ("The dates in that tab's header row are off by a year, so go by position: it's column AF…"); now "the Dec-25 column of the costs tab in the January P&L (the last month of actuals; the columns after it are forecast)". NORMAL_TEXT `end` 3162 → 3024 |
| 19 → 20 | `gsheets.sheets_sheets` `f_768cd23a00c4b12fa0e975` "Feb" | Removed the `["Vercel", 90]` row |
| 26, 28, 30 → removed | Confluence page `page_support_after_helpshift`, its version `ver_16458585…`, its comment `comment_support_after_helpshift_c1` | Removed |
| 41, 43 → removed | Trello card `643efb2ab65c5e952575dde5` "Chase account closure" + its createCard action | Removed |
| 64/68/72 → 57/61/65 | Sunset "data delivery checklist" email, three mailbox copies | Dropped "Confluence" from the list and the sentence "Oliver said he'll log the export on your support handover page"; `size_estimate` 1840 → 1764 (−76 chars, matching the deleted text) |
| 128 → 121 | `linear.linear_projects` "Shutdown – accounts" | "the hosting one is Vercel" → "GitHub"; "the two $30 game-ops lines are people's tool stipends" → "I'm handling myself" |
| 144 → 137 | `linear.linear_comments` `cmt_96ae7b3689c1d073a2ff` (ENG-2439) | Same id, new author and content: now Oliver Brooks (`usr_bdf01b53c6a92c5e`), 2026-02-13T15:12:18Z, "exported the full helpshift ticket history … helpshift_export_2026-02-13.zip" |
| — → 139 | `linear.linear_comments` `cmt_51ff7e6b4cdea7033c08` (ENG-2439) | New id carrying the old Leonard comment ("helpshift wrote back … end of february", 2026-02-13T16:12:40Z) |
| 218, 220 → removed | `ENG-2459` "Vercel" + comment `cmt_8f765d1313e9b01a8c22` | Removed |
| 284 → 275 | `ENG-2477` "GitHub" | description "From the #winddown lists." → "From costs tab (unlabeled hosting line)." |
| 286 → 277 | `cmt_977a0d481cd84d275f08` (ENG-2477) | Dropped "team plan is $52 a month plus copilot usage, $90 last month all in" |

## 3. Lint (`hg_injection_lint.py`, injection-lint-v1, run on this SQL hash)

Flags: FAIL 0, CHECK 0, INFO 1.

| Flag | Record | Resolution |
|---|---|---|
| INFO `unparsed` (metadata-only media) | line 9, `gdrive.drive_files` `f_4ac7a77383e7317eedcd83` `helpshift_export_2026-02-13.zip` | Accepted, unchanged. A zip package is metadata-only, as in the base. Now also cited by Oliver's Linear comment (line 137) by name only. It becomes a FAIL only if an OE or rubric row needs the zip's contents. |

A clean lint doesn't replace checks A–C. The lint does not compare a base-row UPDATE against the same file's Drive bytes; that check was done by hand (F1).

## 4. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; hash, manifest, review version | NEW, done (revision 11 saved from the attachment; byte-identical to the upload) |
| Run lint, resolve flags | NEW, done (1 INFO, resolved) |
| Inventory every statement | NEW, done (147/147, §5) |
| Check A: references, collisions, ID contracts | PASS (NEW for changed/added rows; REUSED for 134 identical) |
| Check B: structure and supported schema rules | PASS (NEW for changed rows; advisory A1 carried over) |
| Check C: dates, relationships, consistency | **FAIL** (F1, NEW) |
| Report and verdict | NEW, done |

**Reuse basis (stage-evidence-v1):** the 134 byte-identical statements reuse the revision-10 report's per-record results (report sha256 `444b0395…bb70e2b`, §5 ledger rows, §6 reference/collision table, §7 structure checks, §8 base facts), which carried earlier revisions' complete checks. Dependencies verified unchanged: identical statement text, universe manifest `5e01ac44…`, clock, and the Eval/WORKFLOW/schema/id_contracts/roster/acl/known-issues hashes (§1). Removed statements were checked for dangling references in the remaining SQL (§6). Every changed or added row was checked from source this run.

## 5. Operation ledger (every statement, execution order)

"Line" is the physical line (LF) where the statement starts in the saved SQL. "Latest event time" is the last ISO event timestamp in the row. "Verification" is NEW (checked this run) or REUSED (byte-identical to revision 10).

| # | Line | Table | Op | Record / target | Latest event time | Result | Verification |
|---|---|---|---|---|---|---|---|
| 1 | 5 | — | BEGIN | — | — | — | REUSED |
| 2 | 7 | `gdrive.drive_files` | INSERT | `f_1326e66bcabfda8fd29e4a` | 2026-02-13T16:58:40Z | PASS | REUSED |
| 3 | 9 | `gdrive.drive_files` | INSERT | `f_4ac7a77383e7317eedcd83` | 2026-02-13T15:04:51Z | PASS | REUSED |
| 4 | 11 | `gdrive.drive_files` | INSERT | `f_768cd23a00c4b12fa0e975` | 2026-02-10T18:31:55Z | PASS | REUSED |
| 5 | 13 | `gdrive.drive_files` | UPDATE | `WHERE id = 'f_605121f4a36752645e0ac3'` | 2026-02-13T16:31:07Z | FAIL (F1) | NEW |
| 6 | 15 | `gdocs.docs_documents` | INSERT | `f_1326e66bcabfda8fd29e4a` | 2026-02-13T16:58:40Z | PASS | NEW |
| 7 | 18 | `gsheets.sheets_spreadsheets` | INSERT | `f_768cd23a00c4b12fa0e975` | 2026-02-10T18:31:55Z | PASS | REUSED |
| 8 | 20 | `gsheets.sheets_sheets` | INSERT | `f_768cd23a00c4b12fa0e975` | — | PASS | NEW |
| 9 | 22 | `gsheets.sheets_sheets` | UPDATE | `WHERE spreadsheet_id = 'f_605121f4a36752645e0ac3' AND sheet_id = 2` | — | FAIL (F1) | NEW |
| 10 | 23 | `gsheets.sheets_spreadsheets` | UPDATE | `WHERE spreadsheet_id = 'f_605121f4a36752645e0ac3'` | 2026-02-13T16:31:07Z | FAIL (F1) | NEW |
| 11 | 25 | `confluence.confluence_pages` | INSERT | `page_ua_vendor_closeout` | 2025-03-18T15:20:00Z | PASS | REUSED |
| 12 | 27 | `confluence.confluence_page_versions` | INSERT | `ver_64b0ed607e093b18a698fb883a584aa6` | 2025-03-18T15:20:00Z | PASS | REUSED |
| 13 | 30 | `slack.slack_messages` | INSERT | `b9ef575bec54b095edb75a0fe83580f5` | 2026-02-13T02:14:36 | PASS | REUSED |
| 14 | 32 | `slack.slack_messages` | INSERT | `fda86aac9fb55c96ffee4bba3e59cc14` | 2026-02-13T10:02:18 | PASS | REUSED |
| 15 | 34 | `slack.slack_messages` | INSERT | `9e245e76cbaf7f080e1995ec0c4ec30d` | 2026-02-13T17:21:07 | PASS | REUSED |
| 16 | 36 | `slack.slack_messages` | UPDATE | `WHERE id = '6d8c8d8affd1255b13d8d875f1547e70'` | — | PASS | REUSED |
| 17 | 38 | `trello.trello_cards` | INSERT | `698f48be4ba0affafbf153db` | 2026-02-13T15:52:30Z | PASS | REUSED |
| 18 | 40 | `trello.trello_actions` | INSERT | `698f48be304fbb37e4e3aafa` | 2026-02-13T15:52:30Z | PASS | REUSED |
| 19 | 43 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1856945900224536585` | — | PASS | REUSED |
| 20 | 45 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com>` | 2026-02-12T18:40:12Z | PASS | REUSED |
| 21 | 47 | `gmail.gmail_threads` | INSERT | `leonard.hayes@harmonygames.co/1856945900224877235` | — | PASS | REUSED |
| 22 | 49 | `gmail.gmail_messages` | INSERT | `leonard.hayes@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.…` | 2026-02-12T18:40:12Z | PASS | REUSED |
| 23 | 51 | `gmail.gmail_threads` | INSERT | `arthur.blake@harmonygames.co/1856945900225226172` | — | PASS | REUSED |
| 24 | 53 | `gmail.gmail_messages` | INSERT | `arthur.blake@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.g…` | 2026-02-12T18:40:12Z | PASS | REUSED |
| 25 | 55 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1856965916492026238` | — | PASS | REUSED |
| 26 | 57 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>` | 2026-02-12T23:58:21Z | PASS | NEW |
| 27 | 59 | `gmail.gmail_threads` | INSERT | `leonard.hayes@harmonygames.co/1856965916492755786` | — | PASS | REUSED |
| 28 | 61 | `gmail.gmail_messages` | INSERT | `leonard.hayes@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.…` | 2026-02-12T23:58:21Z | PASS | NEW |
| 29 | 63 | `gmail.gmail_threads` | INSERT | `arthur.blake@harmonygames.co/1856965916492023943` | — | PASS | REUSED |
| 30 | 65 | `gmail.gmail_messages` | INSERT | `arthur.blake@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.g…` | 2026-02-12T23:58:21Z | PASS | NEW |
| 31 | 67 | `gmail.gmail_threads` | UPDATE | `WHERE id = 'robert@harmonygames.co/1856965916492026238'` | — | PASS | REUSED |
| 32 | 68 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com>` | 2026-02-13T18:20:44Z | PASS | REUSED |
| 33 | 70 | `gmail.gmail_threads` | UPDATE | `WHERE id = 'leonard.hayes@harmonygames.co/1856965916492755786'` | — | PASS | REUSED |
| 34 | 71 | `gmail.gmail_messages` | INSERT | `leonard.hayes@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.…` | 2026-02-13T18:20:44Z | PASS | REUSED |
| 35 | 73 | `gmail.gmail_threads` | UPDATE | `WHERE id = 'arthur.blake@harmonygames.co/1856965916492023943'` | — | PASS | REUSED |
| 36 | 74 | `gmail.gmail_messages` | INSERT | `arthur.blake@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.g…` | 2026-02-13T18:20:44Z | PASS | REUSED |
| 37 | 76 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1842984194671106077` | — | PASS | REUSED |
| 38 | 78 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAowZ1ukjS1ZxLCL4aRt1VM-c-GnNMTNWVQS47OM@mail.gmail.com>` | 2025-09-11T16:04:52Z | PASS | REUSED |
| 39 | 80 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1855299418849853856` | — | PASS | REUSED |
| 40 | 82 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CA4Ce6Oa74xUtCgFI1iGnZMieCxsUh90MhimgGu3@mail.gmail.com>` | 2026-01-25T14:30:05Z | PASS | REUSED |
| 41 | 84 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1855912858878482138` | — | PASS | REUSED |
| 42 | 86 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAL7W0WN5jkixON6h71KIRU6DcLoQyjXVIYONWEZ@mail.gmail.com>` | 2026-02-01T09:00:27Z | PASS | REUSED |
| 43 | 88 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1856653066502254886` | — | PASS | REUSED |
| 44 | 90 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAIoQDHYpNPHXVgnNS8DUmtr__81CmMffz7hcWJv@mail.gmail.com>` | 2026-02-09T13:05:44Z | PASS | REUSED |
| 45 | 92 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1856761009013149089` | — | PASS | REUSED |
| 46 | 94 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAAV70N_MnwWfJSNuqS_HKOnLheApwCzJGSFQi8q@mail.gmail.com>` | 2026-02-10T17:41:26Z | PASS | REUSED |
| 47 | 96 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1856859516436705234` | — | PASS | REUSED |
| 48 | 98 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAxSGYrkpVAs45dr7lAugwSThN-X-ma7vq_V1xAV@mail.gmail.com>` | 2026-02-11T19:47:10Z | PASS | REUSED |
| 49 | 101 | `gcal.gcal_events` | INSERT | `evt_2ac66383ee72bbb05a0376` | 2026-02-12T22:40:15Z (created/updated; start/end 2026-03-12 are plan fields) | PASS | REUSED |
| 50 | 103 | `gcal.gcal_events` | INSERT | `evt_f1d245d44ceff5a6e049c0` | 2026-02-12T22:40:15Z (created/updated; start/end 2026-03-12 are plan fields) | PASS | REUSED |
| 51 | 105 | `gcal.gcal_events` | INSERT | `evt_d1fe12afe85ffbb49bd998` | 2026-02-12T22:40:15Z (created/updated; start/end 2026-03-12 are plan fields) | PASS | REUSED |
| 52 | 108 | `github.github_pull_requests` | INSERT | `harmonygames-Games/Combo-Fighters#38` | 2026-02-13T09:41:12Z | PASS | REUSED |
| 53 | 110 | `github.github_branches` | INSERT | `harmonygames-Games/Combo-Fighters:oliver/final-build-settings` | — | PASS | REUSED |
| 54 | 112 | `github.github_commits` | INSERT | `c769b476f150a76280886f194b4d2186cfd96ca4` | 2026-02-13T09:23:51Z | PASS | REUSED |
| 55 | 114 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/Combo-Fighters#38#c_0` | — | PASS | REUSED |
| 56 | 116 | `github.github_pr_comments` | INSERT | `harmonygames-Games/Combo-Fighters#38#c_1` | 2026-02-13T09:41:12Z | PASS | REUSED |
| 57 | 118 | `github.github_timeline_events` | INSERT | `harmonygames-Games/Combo-Fighters#38#ev_1` | 2026-02-13T09:41:12Z | PASS | REUSED |
| 58 | 121 | `linear.linear_projects` | INSERT | `3f0c6a52-ee13-4b1e-68e3-a74bcc33818a` | 2026-02-12T23:24:10Z | PASS | NEW |
| 59 | 123 | `linear.linear_project_teams` | INSERT | `ptm_2183726e36ddf7f8` | 2026-02-12T23:24:10Z | PASS | REUSED |
| 60 | 125 | `linear.linear_project_members` | INSERT | `pmem_dec4e6c3f1315d8a` | 2026-02-12T23:24:10Z | PASS | REUSED |
| 61 | 127 | `linear.linear_project_members` | INSERT | `pmem_5648d2826ae7a30d` | 2026-02-12T23:24:10Z | PASS | REUSED |
| 62 | 129 | `linear.linear_project_members` | INSERT | `pmem_ca4f8a31e35bad07` | 2026-02-12T23:24:10Z | PASS | REUSED |
| 63 | 131 | `linear.linear_issues` | INSERT | `ENG-2438` | 2026-02-13T19:05:12Z | PASS | REUSED |
| 64 | 133 | `linear.linear_comments` | INSERT | `cmt_5da8c3467fc022248fb3` | 2026-02-13T19:05:12Z | PASS | REUSED |
| 65 | 135 | `linear.linear_issues` | INSERT | `ENG-2439` | 2026-02-13T16:12:40Z | PASS | REUSED |
| 66 | 137 | `linear.linear_comments` | INSERT | `cmt_96ae7b3689c1d073a2ff` | 2026-02-13T15:12:18Z | PASS | NEW |
| 67 | 139 | `linear.linear_comments` | INSERT | `cmt_51ff7e6b4cdea7033c08` | 2026-02-13T16:12:40Z | PASS | NEW |
| 68 | 141 | `linear.linear_issues` | INSERT | `ENG-2440` | 2026-02-12T23:52:03Z | PASS | REUSED |
| 69 | 143 | `linear.linear_comments` | INSERT | `cmt_e8aa0ee7c1bbe08a47c9` | 2026-02-12T23:52:03Z | PASS | REUSED |
| 70 | 145 | `linear.linear_issues` | INSERT | `ENG-2441` | 2026-02-13T20:41:09Z | PASS | REUSED |
| 71 | 147 | `linear.linear_comments` | INSERT | `cmt_37c23c5d30cc6597ebe9` | 2026-02-13T20:41:09Z | PASS | REUSED |
| 72 | 149 | `linear.linear_issues` | INSERT | `ENG-2442` | 2026-02-13T20:43:30Z | PASS | REUSED |
| 73 | 151 | `linear.linear_comments` | INSERT | `cmt_6f994dc8a93d75efb3f8` | 2026-02-13T20:43:30Z | PASS | REUSED |
| 74 | 153 | `linear.linear_issues` | INSERT | `ENG-2443` | 2026-02-12T23:55:41Z | PASS | REUSED |
| 75 | 155 | `linear.linear_comments` | INSERT | `cmt_ec32fbf9ca984b23f7a6` | 2026-02-12T23:55:41Z | PASS | REUSED |
| 76 | 157 | `linear.linear_issues` | INSERT | `ENG-2444` | 2026-02-13T20:45:02Z | PASS | REUSED |
| 77 | 159 | `linear.linear_comments` | INSERT | `cmt_497a61c14b69830f198a` | 2026-02-13T20:45:02Z | PASS | REUSED |
| 78 | 161 | `linear.linear_issues` | INSERT | `ENG-2445` | 2026-02-13T20:45:51Z | PASS | REUSED |
| 79 | 163 | `linear.linear_comments` | INSERT | `cmt_276e0b8a551891ddbdff` | 2026-02-13T20:45:51Z | PASS | REUSED |
| 80 | 165 | `linear.linear_issues` | INSERT | `ENG-2446` | 2026-02-13T20:46:20Z | PASS | REUSED |
| 81 | 167 | `linear.linear_comments` | INSERT | `cmt_a83cc20eced4c1064f0a` | 2026-02-13T20:46:20Z | PASS | REUSED |
| 82 | 169 | `linear.linear_issues` | INSERT | `ENG-2447` | 2026-02-12T23:57:10Z | PASS | REUSED |
| 83 | 171 | `linear.linear_comments` | INSERT | `cmt_8ab16d9d7ac715d1c9a7` | 2026-02-12T23:57:10Z | PASS | REUSED |
| 84 | 173 | `linear.linear_issues` | INSERT | `ENG-2448` | 2026-02-12T23:58:30Z | PASS | REUSED |
| 85 | 175 | `linear.linear_comments` | INSERT | `cmt_e8ae507893bfdb06c8c7` | 2026-02-12T23:58:30Z | PASS | REUSED |
| 86 | 177 | `linear.linear_issues` | INSERT | `ENG-2449` | 2026-02-12T23:27:20Z | PASS | REUSED |
| 87 | 179 | `linear.linear_issues` | INSERT | `ENG-2450` | 2026-02-13T20:47:15Z | PASS | REUSED |
| 88 | 181 | `linear.linear_comments` | INSERT | `cmt_e3da997ff7b6575fbea0` | 2026-02-13T20:47:15Z | PASS | REUSED |
| 89 | 183 | `linear.linear_issues` | INSERT | `ENG-2451` | 2026-02-12T23:27:54Z | PASS | REUSED |
| 90 | 185 | `linear.linear_issues` | INSERT | `ENG-2452` | 2026-02-12T23:58:05Z | PASS | REUSED |
| 91 | 187 | `linear.linear_comments` | INSERT | `cmt_ae352002e2f80996f096` | 2026-02-12T23:58:05Z | PASS | REUSED |
| 92 | 189 | `linear.linear_issues` | INSERT | `ENG-2453` | 2026-02-13T16:20:33Z | PASS | REUSED |
| 93 | 191 | `linear.linear_comments` | INSERT | `cmt_276837877e2b3edc466a` | 2026-02-13T16:20:33Z | PASS | REUSED |
| 94 | 193 | `linear.linear_issues` | INSERT | `ENG-2454` | 2026-02-13T16:24:02Z | PASS | REUSED |
| 95 | 195 | `linear.linear_comments` | INSERT | `cmt_5a650ef858f3cd5a0410` | 2026-02-13T16:24:02Z | PASS | REUSED |
| 96 | 197 | `linear.linear_issues` | INSERT | `ENG-2455` | 2026-02-13T19:12:45Z | PASS | REUSED |
| 97 | 199 | `linear.linear_comments` | INSERT | `cmt_62852832c28dc669e459` | 2026-02-13T19:12:45Z | PASS | REUSED |
| 98 | 201 | `linear.linear_issues` | INSERT | `ENG-2456` | 2026-02-13T01:30:22Z | PASS | REUSED |
| 99 | 203 | `linear.linear_comments` | INSERT | `cmt_2b4807a6cf797d1f4886` | 2026-02-13T01:30:22Z | PASS | REUSED |
| 100 | 205 | `linear.linear_issues` | INSERT | `ENG-2457` | 2026-02-13T01:29:55Z | PASS | REUSED |
| 101 | 207 | `linear.linear_comments` | INSERT | `cmt_bbdca23f075e9fca5cb8` | 2026-02-13T01:29:55Z | PASS | REUSED |
| 102 | 209 | `linear.linear_issues` | INSERT | `ENG-2458` | 2026-02-13T01:33:10Z | PASS | REUSED |
| 103 | 211 | `linear.linear_comments` | INSERT | `cmt_6e664bfa3fea62baabb5` | 2026-02-13T01:33:10Z | PASS | REUSED |
| 104 | 213 | `linear.linear_issues` | INSERT | `ENG-2460` | 2026-02-13T16:25:31Z | PASS | REUSED |
| 105 | 215 | `linear.linear_comments` | INSERT | `cmt_7cf5d70170f54a8f925f` | 2026-02-13T16:25:31Z | PASS | REUSED |
| 106 | 217 | `linear.linear_issues` | INSERT | `ENG-2461` | 2026-02-13T16:26:19Z | PASS | REUSED |
| 107 | 219 | `linear.linear_comments` | INSERT | `cmt_2238bd7d0a60d8e4f31c` | 2026-02-13T16:26:19Z | PASS | REUSED |
| 108 | 221 | `linear.linear_issues` | INSERT | `ENG-2462` | 2026-02-13T16:29:47Z | PASS | REUSED |
| 109 | 223 | `linear.linear_comments` | INSERT | `cmt_75b0e4e31a02f9a022bd` | 2026-02-13T16:29:47Z | PASS | REUSED |
| 110 | 225 | `linear.linear_issues` | INSERT | `ENG-2463` | 2026-02-13T20:49:58Z | PASS | REUSED |
| 111 | 227 | `linear.linear_comments` | INSERT | `cmt_2785f039cfee9d256150` | 2026-02-13T20:49:58Z | PASS | REUSED |
| 112 | 229 | `linear.linear_issues` | INSERT | `ENG-2464` | 2026-02-13T16:31:05Z | PASS | REUSED |
| 113 | 231 | `linear.linear_comments` | INSERT | `cmt_5d88052b6f8c1b2fc181` | 2026-02-13T16:31:05Z | PASS | REUSED |
| 114 | 233 | `linear.linear_issues` | INSERT | `ENG-2465` | 2026-02-13T16:31:48Z | PASS | REUSED |
| 115 | 235 | `linear.linear_comments` | INSERT | `cmt_ec684ef632bdd6b375c3` | 2026-02-13T16:31:48Z | PASS | REUSED |
| 116 | 237 | `linear.linear_issues` | INSERT | `ENG-2466` | 2026-02-12T23:32:09Z | PASS | REUSED |
| 117 | 239 | `linear.linear_issues` | INSERT | `ENG-2467` | 2026-02-12T23:32:26Z | PASS | REUSED |
| 118 | 241 | `linear.linear_issues` | INSERT | `ENG-2468` | 2026-02-13T16:32:20Z | PASS | REUSED |
| 119 | 243 | `linear.linear_comments` | INSERT | `cmt_c767f5417cafd21d0457` | 2026-02-13T16:32:20Z | PASS | REUSED |
| 120 | 245 | `linear.linear_issues` | INSERT | `ENG-2469` | 2026-02-13T16:33:51Z | PASS | REUSED |
| 121 | 247 | `linear.linear_comments` | INSERT | `cmt_4179664f58817a32a076` | 2026-02-13T16:33:51Z | PASS | REUSED |
| 122 | 249 | `linear.linear_issues` | INSERT | `ENG-2470` | 2026-02-12T23:33:17Z | PASS | REUSED |
| 123 | 251 | `linear.linear_issues` | INSERT | `ENG-2471` | 2026-02-12T23:33:34Z | PASS | REUSED |
| 124 | 253 | `linear.linear_issues` | INSERT | `ENG-2472` | 2026-02-13T00:02:44Z | PASS | REUSED |
| 125 | 255 | `linear.linear_comments` | INSERT | `cmt_4ca653c559b182ed6ee6` | 2026-02-13T00:02:44Z | PASS | REUSED |
| 126 | 257 | `linear.linear_issues` | INSERT | `ENG-2473` | 2026-02-13T16:36:10Z | PASS | REUSED |
| 127 | 259 | `linear.linear_comments` | INSERT | `cmt_46c0a9358e1df9a6ded4` | 2026-02-13T16:36:10Z | PASS | REUSED |
| 128 | 261 | `linear.linear_issues` | INSERT | `ENG-2474` | 2026-02-13T00:05:31Z | PASS | REUSED |
| 129 | 263 | `linear.linear_comments` | INSERT | `cmt_a932354ee5e226971ed1` | 2026-02-13T00:05:31Z | PASS | REUSED |
| 130 | 265 | `linear.linear_issues` | INSERT | `ENG-2475` | 2026-02-13T00:06:58Z | PASS | REUSED |
| 131 | 267 | `linear.linear_comments` | INSERT | `cmt_ed6dab8ad539165c22f1` | 2026-02-13T00:06:58Z | PASS | REUSED |
| 132 | 269 | `linear.linear_issues` | INSERT | `ENG-2476` | 2026-02-13T16:37:02Z | PASS | REUSED |
| 133 | 271 | `linear.linear_comments` | INSERT | `cmt_8a420b3635db4a36f750` | 2026-02-13T11:20:37Z | PASS | REUSED |
| 134 | 273 | `linear.linear_comments` | INSERT | `cmt_af582f63b3fef6e310a7` | 2026-02-13T16:37:02Z | PASS | REUSED |
| 135 | 275 | `linear.linear_issues` | INSERT | `ENG-2477` | 2026-02-13T01:28:49Z | PASS | NEW |
| 136 | 277 | `linear.linear_comments` | INSERT | `cmt_977a0d481cd84d275f08` | 2026-02-13T01:28:49Z | PASS | NEW |
| 137 | 279 | `linear.linear_issues` | INSERT | `ENG-2478` | 2026-02-13T00:09:12Z | PASS | REUSED |
| 138 | 281 | `linear.linear_comments` | INSERT | `cmt_d10e47fd216f16429b45` | 2026-02-13T00:09:12Z | PASS | REUSED |
| 139 | 283 | `linear.linear_issues` | INSERT | `ENG-2479` | 2026-02-13T01:34:02Z | PASS | REUSED |
| 140 | 285 | `linear.linear_comments` | INSERT | `cmt_4a019a675b55484b05ec` | 2026-02-13T01:34:02Z | PASS | REUSED |
| 141 | 287 | `linear.linear_issues` | INSERT | `ENG-2480` | 2026-02-13T16:38:44Z | PASS | REUSED |
| 142 | 289 | `linear.linear_comments` | INSERT | `cmt_e3b5ee0557dca1cb519c` | 2026-02-13T16:38:44Z | PASS | REUSED |
| 143 | 291 | `linear.linear_issues` | INSERT | `ENG-2481` | 2026-02-13T20:50:40Z | PASS | REUSED |
| 144 | 293 | `linear.linear_comments` | INSERT | `cmt_5f33dc45f96bbae1e85d` | 2026-02-13T20:50:40Z | PASS | REUSED |
| 145 | 295 | `linear.linear_issues` | INSERT | `ENG-2482` | 2026-02-12T23:36:41Z | PASS | REUSED |
| 146 | 297 | `linear.linear_issues` | INSERT | `ENG-2483` | 2026-02-12T23:36:58Z | PASS | REUSED |
| 147 | 299 | — | COMMIT | — | — | — | REUSED |
## 6. Check A — Records, references and IDs: **PASS**

| Item | Evidence | Result |
|---|---|---|
| UPDATE targets (lines 13, 22, 23) | gdrive `data.json` `/drive_files/34920` `f_605121f4a36752645e0ac3` "Harmony Games P&L and forecast - Jan 2026.xlsx" (complete scan, 53,866 records). gsheets `data.json` `/sheets_spreadsheets/141` same id, with `sheets[2]` `sheet_id` 2 "HG Costs". Each predicate selects exactly one existing row. | PASS |
| New comment id `cmt_51ff7e6b4cdea7033c08` | Linear `data.json`: `/comments` is empty (0 records, complete), and a full text scan of the Linear export for the id has 0 matches (`scan_complete: true`). Unique within the SQL (no repeated first-column key across all 138 INSERTs). | PASS |
| Re-used id `cmt_96ae7b3689c1d073a2ff` (new author/content) | Still inserted once; same collision result as before (absent from base). | PASS |
| Comment authors | `usr_bdf01b53c6a92c5e` = oliver.brooks@harmonygames.co (`/users/29`); `usr_63fffeb4fab5233e` = leonard.hayes (`/users/13`); `usr_cc3e90160f490686` = arthur.blake (`/users/35`). All active. Oliver already authors `cmt_8a420b3635db4a36f750` (ENG-2476) in this SQL, and his GitHub identity (`EMPLOYEE_0003`) matches the removed Confluence comment's author, so it's the same person. | PASS |
| Parents | ENG-2439 (line 135) and ENG-2477 (line 275) are inserted before their comments; project `3f0c6a52-…` is inserted at line 121 before its issues. | PASS |
| Removed records leave no dangling references | Full scan of revision 11 for `ENG-2459`, `Vercel`, `Chase`, `643efb2a…`, `page_support_after_helpshift`, `comment_support_after_helpshift`, `handover`: no matches. The Sunset follow-up reply ("The rest of the list stands") doesn't name Confluence. The one remaining Confluence page (`page_ua_vendor_closeout`) is unrelated. Issue-number gap at 2459 is not an ID-contract issue (no listed contract). | PASS |
| Gmail copies | The three Sunset-email rows differ only in mailbox prefix and thread id; thread rows (lines 55/59/63 and UPDATEs 127/132/137) unchanged. | PASS |
| ID contracts / Drive readability / one account per person | Lint clean. No new accounts or Drive files. | PASS |

## 7. Check B — SQL structure and supported schema rules: **PASS**

- All 147 statements parse (lint). Column/value counts match in every changed INSERT.
- Line 22: `grid_json` (text) parses as a JSON list of 75 rows × 44 columns, the base shape; no unescaped quote. Columns `grid_json`, `modified_time` exist in the snapshot for `gsheets.sheets_sheets`, `gsheets.sheets_spreadsheets` and `gdrive.drive_files`. `modified_time` is `timestamp with time zone` in those tables, so `'2026-02-13T16:31:07Z'` is valid (Linear's text-date rule doesn't apply).
- Line 15: the decoded `body_text` is 3,024 characters and the NORMAL_TEXT range ends at 3024 (title range 0–31 = "Close-out register conventions" + newline), so the style ranges cover the body exactly.
- Linear dates in the changed rows (lines 121, 137, 139, 275, 277) are all `YYYY-MM-DDTHH:MM:SSZ`; ENG-2477 keeps `state_history_json = '[]'`.
- **A1 (advisory, carried over):** `linear.linear_projects.links_json` (now line 121) isn't in the provisional snapshot. If the live table lacks it, the whole transaction rolls back. Safest: drop `links_json` and its `'[]'` value from that insert.

## 8. Check C — Dates, relationships and consistency: **FAIL**

**Clock and chronology:** latest event timestamp 2026-02-13T20:50:40Z (ENG-2481 comment); the only later values are gcal plan fields (2026-03-12). The new P&L `modified_time` 2026-02-13T16:31:07Z moves forward from the base 2026-01-12T20:25:34Z and precedes the conventions doc (created 16:38:02Z). Helpshift chronology: Sunset email 2026-02-12T23:58:21Z → zip file created 2026-02-13T15:04:51Z → Oliver's export comment 15:12:18Z → Leonard's comment 16:12:40Z = ENG-2439 `updated_at`. Clean.

### F1 — FAIL: the P&L header edit makes the Sheets copy and the Drive bytes of the same file disagree

- **Rule:** Eval 0 Check C: incompatible facts introduced by SQL are FAIL.
- **Records:** lines 13, 22, 23 (`f_605121f4a36752645e0ac3`, costs tab "HG Costs").
- **Evidence:**
  - The base Drive row (`gdrive data.json /drive_files/34920`) has `content_path` `Resource: 7240535625619857401/Financial Docs/harmonygames P&L and forecast - Jan 2026.xlsx`, which resolves to real bytes (sha256 `71e8e0b0…12763a2f`). Drive file reads serve `content_path` bytes (`id_contracts.json` `drive_content_path` failure evidence). Injection SQL cannot change those bytes.
  - In the xlsx, `xl/worksheets/sheet3.xml` ("HG Costs") row 1 still stores the base header: **AF1 = 45651 (2024-12-25)**, AR1 = 46017 (2025-12-26), V1 = 45347 (2024-02-25). The HG P&L tab (`sheet1.xml`) stores AF1 = 46016 (2025-12-25).
  - After line 22, the Sheets copy stores **AF = `2025-12-25T00:00:00`** and AR = `2026-12-26T00:00:00`. Before the SQL, both stores agreed exactly (`2024-12-25` at AF).
  - Line 13 bumps the Drive row's `modified_time` to 2026-02-13T16:31:07Z, which says the file changed, while its bytes (`size` 157,427) still have the pre-edit header.
- **Why it matters:** the edited cell is the one the conventions doc (line 15, rule 8) now names without a fallback: "the Dec-25 column of the costs tab … the columns after it are forecast". Revision 11 removed the positional note ("go by position: it's column AF") that made both copies lead to the same column. A reader of the Drive bytes who decodes the stored dates finds December 2025 at **AR** (a forecast column), not AF. For example, G-Suite is 316.56 at AF vs 297.6 at AR, Gusto 116 vs 128 and Deel 300 vs 250 (`sheet3.xml` rows 52/60/61). The Sheets copy points to AF.
- **Mitigating fact (stated for fairness):** the xlsx header cells use the number format `mmm - d`, so a formatted rendering of AF still displays "Dec - 25". The disagreement is in the stored dates. Which form the Agent's Drive read returns is a runtime question this static review can't settle, but the data disagreement itself is introduced by this SQL and shown above.
- **Smallest fix (recommended):** delete the three P&L statements (lines 13, 22, 23) and put a position-based pointer back into rule 8 of the conventions doc (line 15), for example revision 10's sentence "The dates in that tab's header row are off by a year, so go by position: it's column AF, the same column as Dec-25 on the HG P&L tab; everything to its right is forecast." Then set the NORMAL_TEXT `end` in `style_runs_json` to the new body length. Revision 10's approach passed this check.
- **Alternative:** keeping the header edit can't be made consistent, because SQL can't rewrite the xlsx bytes.

### Other changes (checked, no defect)

| Change | Evidence | Result |
|---|---|---|
| "the hosting one is GitHub" (line 121) and ENG-2477 "From costs tab (unlabeled hosting line)" (line 275) | Costs tab Hosting group: "Servers (AWS)" and the redacted line `[PERSON_NAME_0250]` (grid row 41) = 105 / 86 / 89.36 at AE/AF/AG. Base GitHub "Payment Receipt" emails (23 threads, complete subject search, blake@ mailbox): 2025-11-03 **$105.00**, 2025-12-03 **$86.00**, 2026-01-03 **$86.00**, 2026-02-03 $90.00. Ledger (`snowflake.json /tables/38`, 704 rows): only `cloud_infra` counterparty is AWS, no other hosting vendor. | Supported by the base; the earlier "Vercel" label was not (no Vercel billing records; Gmail/Slack "Vercel" hits are newsletters/a Unity URL) |
| ENG-2477 comment trimmed to "github is on the kubllc card now" | Removes the $52/$90 claim; Feb 3 receipt ($90) still in base, no contradiction | PASS |
| "the two $30 game-ops lines I'm handling myself" | Costs tab rows 10 and 17 (`[PERSON_NAME_1000]`, `[PERSON_NAME_5480]`) = 30 at AF | PASS |
| Feb sheet minus Vercel | No remaining record mentions Vercel | PASS |
| Sunset email minus Confluence and the handover-page sentence | Size estimate reduced by exactly the deleted 76 characters; follow-up reply ("Trello … too, Metabase isn't … keep BigQuery and dbt … The rest of the list stands") still consistent | PASS |
| Helpshift export now logged by Oliver on ENG-2439 | Zip (line 9) shared with Oliver as writer, created 7 minutes before his comment; Sunset asked for the export "to Drive before your subscription ends" | PASS |
| Rule 8 cloud/ad-spend clause | Unchanged in effect from revision 10 (AWS FIN-000687 −1,485.00; AppLovin/Meta January lines). Re-read this run | PASS |

**Grader-facing text:** none in the changed rows.

### Advisories (not failing)

- **A1 — `links_json`** (Check B above).
- **A4 — Carried over** (unchanged rows): facts only the injected comments carry, persona approximations, the stale Feb 10 sheet, context items. See earlier reports.
- **A5 — Note for later stages:** Meta's January ledger figure (2,843.84) still applies under rule 8; GitHub's monthly cost by rule 8 is the costs-tab AF value 86 (its Feb 3 receipt is $90).

## 9. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | UPDATE targets resolve to one row each; new comment id absent from base (complete scan) and unique in SQL; authors resolve; no dangling references to removed records. |
| B — SQL structure and supported schema rules | PASS | All statements parse; grid JSON shape matches base; doc style range matches body length. Provisional MISMATCH on `linear_projects.links_json` (A1, advisory). |
| C — Dates, relationships and consistency | **FAIL** | F1: line 22 makes the costs-tab header in Sheets (AF = 2025-12-25) disagree with the same file's Drive xlsx bytes (AF = 2024-12-25, Dec 2025 at AR), on the column rule 8 relies on, with the positional note removed. Chronology otherwise clean; GitHub relabel supported by base receipts. |

## 10. Next action and downstream

1. Fix F1: delete lines 13, 22, 23 and restore a position-based pointer (column AF) in rule 8 of the conventions doc, updating the NORMAL_TEXT `end`.
2. Optional: A1 (drop `links_json` from the `linear_projects` insert at line 121).
3. Then send `/injection` again. Because the SQL changed, every earlier pass that read it is outdated: after `/injection` passes, run `/prompt`, `/hardness`, `/oe`, `/rubric` again, in that order.

## 11. Evidence limits and provenance

- Static scope only. No live execution, database compatibility, search ranking, Agent visibility or difficulty assessment. Whether the Agent's Drive read renders the xlsx header as formatted text or stored dates is a runtime limit; F1 rests on the stored-data disagreement, which is shown above.
- The schema snapshot is unverified, so mismatches are advisory.
- Sources read this run (all `Universe_Normal`): gsheets `data.json` `/sheets_spreadsheets/141` (complete record, paged; file sha256 `4f399b53…16ce3`; the batch record helper reported a spurious "source changed during read" on this 397 MB file while the file's hash and mtime were stable, so the record was read directly by pointer); gdrive `data.json` `/drive_files` (complete id check, sha256 `4cfc33e0…25108`) and `/drive_sheets` (empty, complete); the P&L xlsx bytes under `gdrive/root/Resource: 7240535625619857401/Financial Docs/` (sha256 `71e8e0b0…12763a2f`; `sheet1.xml`, `sheet3.xml`, `styles.xml`); linear `data.json` (`/users`, `/issues`, `/comments`, full-text id scan; sha256 `981e6e6a…31cc7`); snowflake `snowflake.json` `/tables/38` FINANCE_LEDGER (704 rows); Gmail GitHub receipt threads (23, complete subject search) and Gmail/Slack "Vercel", "GitHub billing", "hosting line" searches (complete except the receipt query, which hit its 20 limit and was re-run unbounded).
- Reused evidence: revision-10 report sha256 `444b0395e9ed023627c4a68bde4c07af8985c9e6ac5404787883efa87bb70e2b` (§5 ledger rows, §6 reference/collision table, §7 structure checks, §8 base facts) for the 134 byte-identical statements. Dependencies verified unchanged: statement text, universe manifest, clock and the reference hashes in §1.
- Dependencies for reuse by `/prompt`: none. This report is a FAIL, so its PASS rows for A and B can be reused only for statements unchanged in the next revision.

### FINAL VERDICT: FAIL

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Delete the three P&L header statements (lines 13, 22, 23), put a column-AF pointer back into rule 8 of the conventions doc (line 15) and fix its style range end, then send `/injection` again.

Evidence limits: Static scope only (no live execution, database compatibility, Agent visibility or difficulty). How the Agent's Drive read renders the xlsx header is a runtime limit; the stored-data disagreement behind F1 is shown. Schema snapshot unverified (A1 advisory).
