# Injection data-integrity review — `injection-static-v2`

## 1. Scope

| Field | Value |
|---|---|
| Review | Chat review for your attempt (6adfee3f27ce6ca81b457137), `/injection`, static audit mode |
| Review version | `injection-static-v2` (evidence contract `stage-evidence-v1`) |
| Actual review time | 2026-10-29 (session) |
| Clock | 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal` (hg4-2026-08-31 v37); manifest `Evals/references/universes/normal/universe_manifest.json` sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Input reviewed | Injection SQL, revision 21 (attachment `01_Universe_Inject (13).sql`, saved as `Evals/task_inputs/01_Universe_Inject.sql`), 92,829 bytes, sha256 `fc9bc388ee2a5ae81ee42cea8c7bf34b1040dc50e92a333e3a263257b42f7e6f` |
| Previous version | Revision 20 (`01_Universe_Inject (12).sql`), sha256 `22c1b5ddc7aa18578dfc03b6042768479bbcf0b1698e85a8cab0c86d5db25c2c`, reviewed in report sha256 `a5602a61b7342b13dc15367e375a1de96d0ad775090d2fd9b430d0eb52a9de4e` (PASS / COMPLETE) |
| References (re-hashed this run, unchanged) | Eval 0 `e034019b…6f663eff`; WORKFLOW `ee4cd8e1…504fcd5d`; schema snapshot `31dcb2b4…d74c5151`; `id_contracts.json` `fc4711ef…d9ed4682`; known_base_issues `79b20289…e7553a7b` |

## 2. Input / authority issues

- The only input for this stage is the SQL. It is substantive: 126 statements (BEGIN, 120 INSERT, 4 UPDATE, COMMIT) across gdrive, gdocs, gsheets, confluence, slack, trello, gmail, gcal, github and linear. The header comment's counts (120 INSERT, 4 UPDATE) match the parse. The 14 comment lines are authoring notes; none mention tool calls, pass rate or gates.
- `known_base_issues.md` (unchanged) has no entries for the normal universe (its three entries are synth-cut). Nothing injected builds on a listed conflict.

**Change set from revision 20 (line diff of the two files):** every other line is byte-identical. The changes:

| v12 line → v13 line | Record | Change |
|---|---|---|
| 3 → 3 | header comment | statement count 122 → 120 INSERT |
| 15 → 15 | `gdocs.docs_documents` `f_1326e66bcabfda8fd29e4a` (conventions doc body) | Rule 3 now keeps "AWS and the ad accounts in the UA line" off the register ("he and I are closing those out ourselves") and limits the add-ons to accounts inside "any other costs-tab line that covers several vendors"; the finance-ledger add-on is gone. Rule 8 loses the "January ledger line" basis for cloud/ad accounts. `style_runs_json` last run end 2904 → 2727. Timestamps unchanged. |
| 34 → 34 | `slack.slack_messages` `9e245e76…` (Leonard's ask) | "every account … last night" → "our accounts … yesterday"; "keep list from last night and the replies under it" → "keep list from yesterday and the reply under it". Timestamps unchanged. |
| 147 → 147 | `linear.linear_projects` `3f0c6a52…` description | Drops "we cancelled the unity ads in the UA line after october"; adds "AWS and the ad accounts in the UA line aren't in here either: I'm shutting AWS down myself once the store transfer is done, and Leonard is closing the ad networks directly." Timestamps unchanged. |
| 182–185 → removed | `linear.linear_issues` ENG-2445 "AWS" and `linear.linear_comments` `cmt_276e0b8a551891ddbdff` | Both rows deleted; statements after them move up 4 lines. |

## 3. Lint (`hg_injection_lint.py`, injection-lint-v1, run on SQL sha256 `fc9bc388…`)

Flags: FAIL 0, CHECK 0, INFO 1. Row counts parsed: 120 inserts and 4 updates, the same as the header.

| Flag | Location | Resolution |
|---|---|---|
| INFO `unparsed` (metadata-only media) | line 9, `gdrive.drive_files` `f_4ac7a77383e7317eedcd83` `helpshift_export_2026-02-13.zip` | Accepted, unchanged. A zip package is metadata-only, as in the base; Oliver's ENG-2439 comment cites it by name only. It becomes a FAIL only if an OE or rubric row needs the zip's contents. |

A clean lint doesn't replace checks A–C; they were done below.

## 4. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; hash, manifest, review version | NEW, done (revision 21 saved from the attachment) |
| Run lint, resolve flags | NEW, done (1 INFO, resolved) |
| Inventory every statement | NEW, done (126/126, §5; line diff against revision 20) |
| Check A: references, collisions, ID contracts | PASS (removed-row references NEW; collision sweep REUSED for the unchanged key set) |
| Check B: structure and supported schema rules | PASS (NEW for changed rows and statement structure; advisory A1 carried over) |
| Check C: dates, relationships, consistency | PASS (changed text NEW; unchanged claims REUSED) |
| Report and verdict | NEW, done |

**Reuse basis (stage-evidence-v1):** the collision sweep (§6 upper table), actor/channel/member/sender resolutions and the unchanged factual-claim rows reuse the revision-20 report (sha256 `a5602a61…de4e`, §6–§8). Dependencies verified unchanged this run: every inserted key in v13 is one of v12's keys with an identical value (only rows were removed, no key edited); all other lines are byte-identical; universe manifest `5e01ac44…`, clock and every reference hash in §1 re-hashed equal. Changed and removed rows were checked fresh.

## 5. Operation ledger (every statement, execution order)

Line = line of the statement's first keyword (verified against the saved file: all 126 statement lines and record ids match). All 120 INSERT keys are unique within their tables in the SQL. "REUSED" rows are byte-identical to revision 20 and keep that report's results; "NEW" rows were checked this run.

| # | Line | Table | Op | Record / target | Latest event time in row | Result | Basis |
|---|---|---|---|---|---|---|---|
| 1 | 5 | `—` | BEGIN | `—` | — | PASS | NEW (structure re-parsed) |
| 2 | 7 | `gdrive.drive_files` | INSERT | `f_1326e66bcabfda8fd29e4a` | 2026-02-13T16:58:40Z | PASS | REUSED (row byte-identical to v12) |
| 3 | 9 | `gdrive.drive_files` | INSERT | `f_4ac7a77383e7317eedcd83` | 2026-02-13T15:04:51Z | PASS | REUSED (row byte-identical to v12) |
| 4 | 11 | `gdrive.drive_files` | INSERT | `f_768cd23a00c4b12fa0e975` | 2026-02-10T18:31:55Z | PASS | REUSED (row byte-identical to v12) |
| 5 | 14 | `gdocs.docs_documents` | INSERT | `f_1326e66bcabfda8fd29e4a` | 2026-02-13T16:58:40Z | PASS | NEW (text changed in v13) |
| 6 | 17 | `gsheets.sheets_spreadsheets` | INSERT | `f_768cd23a00c4b12fa0e975` | 2026-02-10T18:31:55Z | PASS | REUSED (row byte-identical to v12) |
| 7 | 19 | `gsheets.sheets_sheets` | INSERT | `f_768cd23a00c4b12fa0e975` | — | PASS | REUSED (row byte-identical to v12) |
| 8 | 22 | `confluence.confluence_pages` | INSERT | `page_ua_vendor_closeout` | 2025-03-18T15:20:00Z | PASS | REUSED (row byte-identical to v12) |
| 9 | 24 | `confluence.confluence_page_versions` | INSERT | `ver_64b0ed607e093b18a698fb883a584aa6` | 2025-03-18T15:20:00Z | PASS | REUSED (row byte-identical to v12) |
| 10 | 27 | `slack.slack_messages` | INSERT | `b9ef575bec54b095edb75a0fe83580f5` | 2026-02-13T02:14:36.205117Z | PASS | REUSED (row byte-identical to v12) |
| 11 | 29 | `slack.slack_messages` | INSERT | `fda86aac9fb55c96ffee4bba3e59cc14` | 2026-02-13T10:02:18.774231Z | PASS | REUSED (row byte-identical to v12) |
| 12 | 31 | `slack.slack_messages` | INSERT | `6303f60fefe86f1c3ebaa864318f6907` | 2026-02-13T14:07:33.518204Z | PASS | REUSED (row byte-identical to v12) |
| 13 | 33 | `slack.slack_messages` | INSERT | `9e245e76cbaf7f080e1995ec0c4ec30d` | 2026-02-13T17:21:07.448213Z | PASS | NEW (text changed in v13) |
| 14 | 35 | `slack.slack_messages` | INSERT | `cd1423b23b5d39c3341a5838c31a3138` | 2026-02-13T21:18:40.226917Z | PASS | REUSED (row byte-identical to v12) |
| 15 | 37 | `slack.slack_messages` | INSERT | `fb53c42227d5b5868efdade6b69c3738` | 2026-02-12T19:44:05.613380Z | PASS | REUSED (row byte-identical to v12) |
| 16 | 39 | `slack.slack_messages` | INSERT | `87626c59a436ce9c3a87c0eda56d1354` | 2026-02-13T22:40:26.317702Z | PASS | REUSED (row byte-identical to v12) |
| 17 | 41 | `slack.slack_messages` | UPDATE | `id = 6d8c8d8affd1255b13d8d875f1547e70` | — | PASS | REUSED (row byte-identical to v12) |
| 18 | 43 | `trello.trello_cards` | INSERT | `698f48be4ba0affafbf153db` | 2026-02-13T23:12:05Z | PASS | REUSED (row byte-identical to v12) |
| 19 | 45 | `trello.trello_actions` | INSERT | `698f48be304fbb37e4e3aafa` | 2026-02-13T15:52:30Z | PASS | REUSED (row byte-identical to v12) |
| 20 | 47 | `trello.trello_actions` | INSERT | `698fa9f7f77cecfe5c7aa524` | 2026-02-13T22:47:19Z | PASS | REUSED (row byte-identical to v12) |
| 21 | 49 | `trello.trello_actions` | INSERT | `698fafc529f7ffa32ff7dd20` | 2026-02-13T23:12:05Z | PASS | REUSED (row byte-identical to v12) |
| 22 | 52 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1856945900224536585` | — | PASS | REUSED (row byte-identical to v12) |
| 23 | 54 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com>` | 2026-02-12T18:40:12Z | PASS | REUSED (row byte-identical to v12) |
| 24 | 56 | `gmail.gmail_threads` | INSERT | `leonard.hayes@harmonygames.co/1856945900224877235` | — | PASS | REUSED (row byte-identical to v12) |
| 25 | 58 | `gmail.gmail_messages` | INSERT | `leonard.hayes@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gma` | 2026-02-12T18:40:12Z | PASS | REUSED (row byte-identical to v12) |
| 26 | 60 | `gmail.gmail_threads` | INSERT | `arthur.blake@harmonygames.co/1856945900225226172` | — | PASS | REUSED (row byte-identical to v12) |
| 27 | 62 | `gmail.gmail_messages` | INSERT | `arthur.blake@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmai` | 2026-02-12T18:40:12Z | PASS | REUSED (row byte-identical to v12) |
| 28 | 64 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1856965916492026238` | — | PASS | REUSED (row byte-identical to v12) |
| 29 | 66 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>` | 2026-02-12T23:58:21Z | PASS | REUSED (row byte-identical to v12) |
| 30 | 68 | `gmail.gmail_threads` | INSERT | `leonard.hayes@harmonygames.co/1856965916492755786` | — | PASS | REUSED (row byte-identical to v12) |
| 31 | 70 | `gmail.gmail_messages` | INSERT | `leonard.hayes@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gma` | 2026-02-12T23:58:21Z | PASS | REUSED (row byte-identical to v12) |
| 32 | 72 | `gmail.gmail_threads` | INSERT | `arthur.blake@harmonygames.co/1856965916492023943` | — | PASS | REUSED (row byte-identical to v12) |
| 33 | 74 | `gmail.gmail_messages` | INSERT | `arthur.blake@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmai` | 2026-02-12T23:58:21Z | PASS | REUSED (row byte-identical to v12) |
| 34 | 76 | `gmail.gmail_threads` | UPDATE | `id = robert@harmonygames.co/1856965916492026238` | — | PASS | REUSED (row byte-identical to v12) |
| 35 | 77 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com>` | 2026-02-13T18:20:44Z | PASS | REUSED (row byte-identical to v12) |
| 36 | 79 | `gmail.gmail_threads` | UPDATE | `id = leonard.hayes@harmonygames.co/1856965916492755786` | — | PASS | REUSED (row byte-identical to v12) |
| 37 | 80 | `gmail.gmail_messages` | INSERT | `leonard.hayes@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gma` | 2026-02-13T18:20:44Z | PASS | REUSED (row byte-identical to v12) |
| 38 | 82 | `gmail.gmail_threads` | UPDATE | `id = arthur.blake@harmonygames.co/1856965916492023943` | — | PASS | REUSED (row byte-identical to v12) |
| 39 | 83 | `gmail.gmail_messages` | INSERT | `arthur.blake@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmai` | 2026-02-13T18:20:44Z | PASS | REUSED (row byte-identical to v12) |
| 40 | 85 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1842712894505970340` | — | PASS | REUSED (row byte-identical to v12) |
| 41 | 87 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAIoQDHYpNPHXVgnNS8DUmtr__81CmMffz7hcWJv@mail.gmail.com>` | 2025-09-08T16:12:40Z | PASS | REUSED (row byte-identical to v12) |
| 42 | 89 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1842984194671106077` | — | PASS | REUSED (row byte-identical to v12) |
| 43 | 91 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAowZ1ukjS1ZxLCL4aRt1VM-c-GnNMTNWVQS47OM@mail.gmail.com>` | 2025-09-11T16:04:52Z | PASS | REUSED (row byte-identical to v12) |
| 44 | 93 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1856114791547562583` | — | PASS | REUSED (row byte-identical to v12) |
| 45 | 95 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CA4Ce6Oa74xUtCgFI1iGnZMieCxsUh90MhimgGu3@mail.gmail.com>` | 2026-02-03T14:30:05Z | PASS | REUSED (row byte-identical to v12) |
| 46 | 97 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1856859516436705234` | — | PASS | REUSED (row byte-identical to v12) |
| 47 | 99 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAxSGYrkpVAs45dr7lAugwSThN-X-ma7vq_V1xAV@mail.gmail.com>` | 2026-02-11T19:47:10Z | PASS | REUSED (row byte-identical to v12) |
| 48 | 101 | `gmail.gmail_threads` | INSERT | `arthur.blake@harmonygames.co/1857018744799627050` | — | PASS | REUSED (row byte-identical to v12) |
| 49 | 103 | `gmail.gmail_messages` | INSERT | `arthur.blake@harmonygames.co/<CAiNg4QTh-tYTcaxqfYeePA5pS-5wWPkXvAPL9qS@mail.gmai` | 2026-02-13T13:58:02Z | PASS | REUSED (row byte-identical to v12) |
| 50 | 105 | `gmail.gmail_threads` | INSERT | `arthur.blake@harmonygames.co/1857044821836129041` | — | PASS | REUSED (row byte-identical to v12) |
| 51 | 107 | `gmail.gmail_messages` | INSERT | `arthur.blake@harmonygames.co/<CAUS1JuCoozyJO5SgXcz-1dVbo7duszBh21aQwZr@mail.gmai` | 2026-02-13T20:52:31Z | PASS | REUSED (row byte-identical to v12) |
| 52 | 109 | `gmail.gmail_threads` | INSERT | `leonard.hayes@harmonygames.co/1857044821836034704` | — | PASS | REUSED (row byte-identical to v12) |
| 53 | 111 | `gmail.gmail_messages` | INSERT | `leonard.hayes@harmonygames.co/<CAUS1JuCoozyJO5SgXcz-1dVbo7duszBh21aQwZr@mail.gma` | 2026-02-13T20:52:31Z | PASS | REUSED (row byte-identical to v12) |
| 54 | 113 | `gmail.gmail_threads` | INSERT | `leonard.hayes@harmonygames.co/1857051067155022210` | — | PASS | REUSED (row byte-identical to v12) |
| 55 | 115 | `gmail.gmail_messages` | INSERT | `leonard.hayes@harmonygames.co/<CAlutvfoiS_dRLmmsgE-rPqfCnV24mT0fiHMbdWe@mail.gma` | 2026-02-13T22:31:47Z | PASS | REUSED (row byte-identical to v12) |
| 56 | 117 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1856961002865672224` | — | PASS | REUSED (row byte-identical to v12) |
| 57 | 119 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<calendar-951230da-b530-be28-7f3e-7de01fef9ec5@google.com` | 2026-02-12T22:40:15Z | PASS | REUSED (row byte-identical to v12) |
| 58 | 121 | `gmail.gmail_threads` | INSERT | `arthur.blake@harmonygames.co/1856961002865002536` | — | PASS | REUSED (row byte-identical to v12) |
| 59 | 123 | `gmail.gmail_messages` | INSERT | `arthur.blake@harmonygames.co/<calendar-6e72e8ad-9998-760c-3f6b-0e9e31fa44ce@goog` | 2026-02-12T22:40:15Z | PASS | REUSED (row byte-identical to v12) |
| 60 | 126 | `gcal.gcal_events` | INSERT | `evt_2ac66383ee72bbb05a0376` | 2026-02-12T22:40:15Z (start/end 2026-03-12 = plan fields) | PASS | REUSED (row byte-identical to v12) |
| 61 | 128 | `gcal.gcal_events` | INSERT | `evt_f1d245d44ceff5a6e049c0` | 2026-02-12T22:40:15Z (start/end 2026-03-12 = plan fields) | PASS | REUSED (row byte-identical to v12) |
| 62 | 130 | `gcal.gcal_events` | INSERT | `evt_d1fe12afe85ffbb49bd998` | 2026-02-12T22:40:15Z (start/end 2026-03-12 = plan fields) | PASS | REUSED (row byte-identical to v12) |
| 63 | 133 | `github.github_pull_requests` | INSERT | `harmonygames-Games/Combo-Fighters#38` | 2026-02-13T09:41:12Z | PASS | REUSED (row byte-identical to v12) |
| 64 | 135 | `github.github_branches` | INSERT | `harmonygames-Games/Combo-Fighters:oliver/final-build-settings` | — | PASS | REUSED (row byte-identical to v12) |
| 65 | 137 | `github.github_commits` | INSERT | `c769b476f150a76280886f194b4d2186cfd96ca4` | 2026-02-13T09:23:51Z | PASS | REUSED (row byte-identical to v12) |
| 66 | 139 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/Combo-Fighters#38#c_0` | — | PASS | REUSED (row byte-identical to v12) |
| 67 | 141 | `github.github_pr_comments` | INSERT | `harmonygames-Games/Combo-Fighters#38#c_1` | 2026-02-13T09:41:12Z | PASS | REUSED (row byte-identical to v12) |
| 68 | 143 | `github.github_timeline_events` | INSERT | `harmonygames-Games/Combo-Fighters#38#ev_1` | 2026-02-13T09:41:12Z | PASS | REUSED (row byte-identical to v12) |
| 69 | 146 | `linear.linear_projects` | INSERT | `3f0c6a52-ee13-4b1e-68e3-a74bcc33818a` | 2026-02-12T23:24:10Z | PASS | NEW (text changed in v13) |
| 70 | 148 | `linear.linear_project_teams` | INSERT | `ptm_2183726e36ddf7f8` | 2026-02-12T23:24:10Z | PASS | REUSED (row byte-identical to v12) |
| 71 | 150 | `linear.linear_project_members` | INSERT | `pmem_dec4e6c3f1315d8a` | 2026-02-12T23:24:10Z | PASS | REUSED (row byte-identical to v12) |
| 72 | 152 | `linear.linear_project_members` | INSERT | `pmem_5648d2826ae7a30d` | 2026-02-12T23:24:10Z | PASS | REUSED (row byte-identical to v12) |
| 73 | 154 | `linear.linear_project_members` | INSERT | `pmem_ca4f8a31e35bad07` | 2026-02-12T23:24:10Z | PASS | REUSED (row byte-identical to v12) |
| 74 | 156 | `linear.linear_issues` | INSERT | `ENG-2438` | 2026-02-13T19:05:12Z | PASS | REUSED (row byte-identical to v12) |
| 75 | 158 | `linear.linear_comments` | INSERT | `cmt_5da8c3467fc022248fb3` | 2026-02-13T19:05:12Z | PASS | REUSED (row byte-identical to v12) |
| 76 | 160 | `linear.linear_issues` | INSERT | `ENG-2439` | 2026-02-13T16:12:40Z | PASS | REUSED (row byte-identical to v12) |
| 77 | 162 | `linear.linear_comments` | INSERT | `cmt_96ae7b3689c1d073a2ff` | 2026-02-13T15:12:18Z | PASS | REUSED (row byte-identical to v12) |
| 78 | 164 | `linear.linear_comments` | INSERT | `cmt_51ff7e6b4cdea7033c08` | 2026-02-13T16:12:40Z | PASS | REUSED (row byte-identical to v12) |
| 79 | 166 | `linear.linear_issues` | INSERT | `ENG-2440` | 2026-02-12T23:52:03Z | PASS | REUSED (row byte-identical to v12) |
| 80 | 168 | `linear.linear_comments` | INSERT | `cmt_e8aa0ee7c1bbe08a47c9` | 2026-02-12T23:52:03Z | PASS | REUSED (row byte-identical to v12) |
| 81 | 170 | `linear.linear_issues` | INSERT | `ENG-2441` | 2026-02-12T23:58:30Z | PASS | REUSED (row byte-identical to v12) |
| 82 | 172 | `linear.linear_comments` | INSERT | `cmt_37c23c5d30cc6597ebe9` | 2026-02-12T23:58:30Z | PASS | REUSED (row byte-identical to v12) |
| 83 | 174 | `linear.linear_issues` | INSERT | `ENG-2442` | 2026-02-12T23:25:21Z | PASS | REUSED (row byte-identical to v12) |
| 84 | 176 | `linear.linear_issues` | INSERT | `ENG-2443` | 2026-02-12T23:25:38Z | PASS | REUSED (row byte-identical to v12) |
| 85 | 178 | `linear.linear_issues` | INSERT | `ENG-2444` | 2026-02-13T16:24:02Z | PASS | REUSED (row byte-identical to v12) |
| 86 | 180 | `linear.linear_comments` | INSERT | `cmt_497a61c14b69830f198a` | 2026-02-13T16:24:02Z | PASS | REUSED (row byte-identical to v12) |
| 87 | 182 | `linear.linear_issues` | INSERT | `ENG-2446` | 2026-02-13T01:30:22Z | PASS | REUSED (row byte-identical to v12) |
| 88 | 184 | `linear.linear_comments` | INSERT | `cmt_a83cc20eced4c1064f0a` | 2026-02-13T01:30:22Z | PASS | REUSED (row byte-identical to v12) |
| 89 | 186 | `linear.linear_issues` | INSERT | `ENG-2447` | 2026-02-13T01:29:55Z | PASS | REUSED (row byte-identical to v12) |
| 90 | 188 | `linear.linear_comments` | INSERT | `cmt_8ab16d9d7ac715d1c9a7` | 2026-02-13T01:29:55Z | PASS | REUSED (row byte-identical to v12) |
| 91 | 190 | `linear.linear_issues` | INSERT | `ENG-2448` | 2026-02-13T01:33:10Z | PASS | REUSED (row byte-identical to v12) |
| 92 | 192 | `linear.linear_comments` | INSERT | `cmt_e8ae507893bfdb06c8c7` | 2026-02-13T01:33:10Z | PASS | REUSED (row byte-identical to v12) |
| 93 | 194 | `linear.linear_issues` | INSERT | `ENG-2449` | 2026-02-13T16:25:31Z | PASS | REUSED (row byte-identical to v12) |
| 94 | 196 | `linear.linear_comments` | INSERT | `cmt_5fb637b0247b82594b16` | 2026-02-13T16:25:31Z | PASS | REUSED (row byte-identical to v12) |
| 95 | 198 | `linear.linear_issues` | INSERT | `ENG-2450` | 2026-02-13T16:26:19Z | PASS | REUSED (row byte-identical to v12) |
| 96 | 200 | `linear.linear_comments` | INSERT | `cmt_e3da997ff7b6575fbea0` | 2026-02-13T16:26:19Z | PASS | REUSED (row byte-identical to v12) |
| 97 | 202 | `linear.linear_issues` | INSERT | `ENG-2451` | 2026-02-13T16:29:47Z | PASS | REUSED (row byte-identical to v12) |
| 98 | 204 | `linear.linear_comments` | INSERT | `cmt_f430b60b346c70afda13` | 2026-02-13T16:29:47Z | PASS | REUSED (row byte-identical to v12) |
| 99 | 206 | `linear.linear_issues` | INSERT | `ENG-2452` | 2026-02-13T16:31:05Z | PASS | REUSED (row byte-identical to v12) |
| 100 | 208 | `linear.linear_comments` | INSERT | `cmt_ae352002e2f80996f096` | 2026-02-13T16:31:05Z | PASS | REUSED (row byte-identical to v12) |
| 101 | 210 | `linear.linear_issues` | INSERT | `ENG-2453` | 2026-02-13T16:31:48Z | PASS | REUSED (row byte-identical to v12) |
| 102 | 212 | `linear.linear_comments` | INSERT | `cmt_276837877e2b3edc466a` | 2026-02-13T16:31:48Z | PASS | REUSED (row byte-identical to v12) |
| 103 | 214 | `linear.linear_issues` | INSERT | `ENG-2454` | 2026-02-12T23:28:45Z | PASS | REUSED (row byte-identical to v12) |
| 104 | 216 | `linear.linear_issues` | INSERT | `ENG-2455` | 2026-02-13T16:32:02Z | PASS | REUSED (row byte-identical to v12) |
| 105 | 218 | `linear.linear_comments` | INSERT | `cmt_62852832c28dc669e459` | 2026-02-13T16:32:02Z | PASS | REUSED (row byte-identical to v12) |
| 106 | 220 | `linear.linear_issues` | INSERT | `ENG-2456` | 2026-02-13T16:32:20Z | PASS | REUSED (row byte-identical to v12) |
| 107 | 222 | `linear.linear_comments` | INSERT | `cmt_2b4807a6cf797d1f4886` | 2026-02-13T16:32:20Z | PASS | REUSED (row byte-identical to v12) |
| 108 | 224 | `linear.linear_issues` | INSERT | `ENG-2457` | 2026-02-13T16:33:51Z | PASS | REUSED (row byte-identical to v12) |
| 109 | 226 | `linear.linear_comments` | INSERT | `cmt_bbdca23f075e9fca5cb8` | 2026-02-13T16:33:51Z | PASS | REUSED (row byte-identical to v12) |
| 110 | 228 | `linear.linear_issues` | INSERT | `ENG-2458` | 2026-02-13T16:36:10Z | PASS | REUSED (row byte-identical to v12) |
| 111 | 230 | `linear.linear_comments` | INSERT | `cmt_6e664bfa3fea62baabb5` | 2026-02-13T16:36:10Z | PASS | REUSED (row byte-identical to v12) |
| 112 | 232 | `linear.linear_issues` | INSERT | `ENG-2459` | 2026-02-13T00:05:31Z | PASS | REUSED (row byte-identical to v12) |
| 113 | 234 | `linear.linear_comments` | INSERT | `cmt_8f765d1313e9b01a8c22` | 2026-02-13T00:05:31Z | PASS | REUSED (row byte-identical to v12) |
| 114 | 236 | `linear.linear_issues` | INSERT | `ENG-2460` | 2026-02-13T00:06:58Z | PASS | REUSED (row byte-identical to v12) |
| 115 | 238 | `linear.linear_comments` | INSERT | `cmt_7cf5d70170f54a8f925f` | 2026-02-13T00:06:58Z | PASS | REUSED (row byte-identical to v12) |
| 116 | 240 | `linear.linear_issues` | INSERT | `ENG-2461` | 2026-02-13T16:37:02Z | PASS | REUSED (row byte-identical to v12) |
| 117 | 242 | `linear.linear_comments` | INSERT | `cmt_2238bd7d0a60d8e4f31c` | 2026-02-13T16:37:02Z | PASS | REUSED (row byte-identical to v12) |
| 118 | 244 | `linear.linear_issues` | INSERT | `ENG-2462` | 2026-02-13T01:28:49Z | PASS | REUSED (row byte-identical to v12) |
| 119 | 246 | `linear.linear_comments` | INSERT | `cmt_75b0e4e31a02f9a022bd` | 2026-02-13T01:28:49Z | PASS | REUSED (row byte-identical to v12) |
| 120 | 248 | `linear.linear_issues` | INSERT | `ENG-2463` | 2026-02-13T00:09:12Z | PASS | REUSED (row byte-identical to v12) |
| 121 | 250 | `linear.linear_comments` | INSERT | `cmt_2785f039cfee9d256150` | 2026-02-13T00:09:12Z | PASS | REUSED (row byte-identical to v12) |
| 122 | 252 | `linear.linear_issues` | INSERT | `ENG-2464` | 2026-02-13T01:34:02Z | PASS | REUSED (row byte-identical to v12) |
| 123 | 254 | `linear.linear_comments` | INSERT | `cmt_5d88052b6f8c1b2fc181` | 2026-02-13T01:34:02Z | PASS | REUSED (row byte-identical to v12) |
| 124 | 256 | `linear.linear_issues` | INSERT | `ENG-2465` | 2026-02-12T23:31:52Z | PASS | REUSED (row byte-identical to v12) |
| 125 | 258 | `linear.linear_issues` | INSERT | `ENG-2466` | 2026-02-12T23:32:09Z | PASS | REUSED (row byte-identical to v12) |
| 126 | 260 | `—` | COMMIT | `—` | — | PASS | NEW (structure re-parsed) |

## 6. Check A — Records, references and IDs: **PASS**

**Collision sweep (REUSED from the revision-20 report §6; key set unchanged except two removed keys):**

| Collection (Universe_Normal) | Field(s) | Keys checked (v13) | Records / files | Coverage | Matches |
|---|---|---|---|---|---|
| gdrive `data.json` `/drive_files` | `id` | 3 | 53,866 | complete | 0 |
| gdocs `data.json` `/docs_documents` | `document_id` | 1 | 633 | complete | 0 |
| gsheets `data.json` `/sheets_spreadsheets` | `spreadsheet_id`, `drive_file_id` | 1 | 398 | complete | 0 |
| confluence `confluence_working.json` `/pages`, `/page_versions` | `id` | 1 + 1 | 31 / 78 | complete | 0 |
| trello `data.json` `/cards`, `/actions` | `id` | 1 + 3 | 803 / 5,294 | complete | 0 |
| gcal `data.json` `/events` | `id`, `event_id` | 3 | 11,130 | complete | 0 |
| github `data.json` PRs, branches, commits (`sha`), PR commits, PR comments, timeline events | `id`/`sha` | 1 each | 2,629 / 2,011 / 12,687 / 15,938 / 884 / 12,435 | complete | 0 |
| linear `data.json` `/projects`; `/issues` | `id`; `identifier`, `id`, `number` (2438–2466) | 1; 28 | 2; 3,852 | complete | 0 |
| linear `data.json` full-text | 24 comment ids, project-team id, 3 project-member ids | 28 | 1 file | complete | 0 |
| slack `messages/*.json` | `id` (lookup) and `ts` (full-text) | 7 + 7 | 687,230 records / 5,353 files | complete | 0 |
| gmail `threads/*.json` full-text | 16 thread numbers + Message-IDs | 28 | 88,726 files | complete | 0 |
| slack UPDATE target | `id = 6d8c8d8a…` | 1 | — | re-read this run | 1: `slack/messages/C0ADGSZKR3R/2026-02.json` `/188` (#winddown, Leonard's keep list, `reply_count` 0, no thread fields), as the UPDATE requires |

**Fresh this run:**

| Item | Evidence | Result |
|---|---|---|
| Removed ENG-2445 / `cmt_276e0b8a551891ddbdff` | The comment was removed with its issue. `grep` of the v13 SQL for `ENG-2445`, `2445`, `cmt_276e0b8a551891ddbdff`, `1,485`, `1485` and `dd prod`: 0 hits. No relation, link or comment points at the removed issue. | PASS |
| Linear numbering | ENG-2438–2444 and 2446–2466 remain (28 issues); `created_at` still rises with the number. Number 2445 is now unused. Not a listed ID contract; a numbering gap alone isn't a defect (A8). | PASS |
| Keep-list thread | Base `/188` (ts `1770933601.686309` = 2026-02-12 22:00:01Z) has 0 replies; full-text search of that ts over all 5,357 Slack files (complete) finds only its own `ts`. With the injected Gusto reply `b9ef575b…` and the UPDATE (`reply_count = 1`), the thread has exactly one reply, so Leonard's new "the reply under it" matches the data. | PASS |
| Actors, channels, senders, parents | Unchanged rows; results REUSED from revision-20 §6 (Linear users `usr_cc3e…` Arthur, `usr_63ff…` Leonard, `usr_bdf0…` Oliver, `usr_Robert`; Slack EMPLOYEE_0003/0025/0038, PERSON_2705 and channel memberships; Trello members; Gmail placeholders SVC_2674/5543/0553 and external PERSON_7731). | PASS |
| ID contracts / Drive readability / one account per person | Lint clean; Gmail thread `history_id` NULL; no new accounts; the conventions doc has a `docs_documents` row with non-empty body. | PASS |

## 7. Check B — SQL structure and supported schema rules: **PASS**

- All 126 statements parse (lint: no `missing_required`, `json_shape`, `generated_column` or `text_time_format` flags); each VALUES tuple binds to its column list; BEGIN at line 5, COMMIT at line 260. No `text_fts`/`body_text_fts` set.
- Changed gdocs row: decoding the `E'…'` body gives 2,727 characters (2,727 UTF-16 units), 11 line breaks; `style_runs_json` runs 0–31 (title "Close-out register conventions" + newline = 31) and 31–2727 cover it exactly.
- Changed Slack and Linear rows: plain `'…'` strings with `''` escapes only, no backslashes; timestamps unchanged and in base format (`linear_projects` `*_at` `YYYY-MM-DDTHH:MM:SSZ`).
- Unchanged rows: results REUSED from revision-20 §7 (escapes only inside `E'…'` strings, CR LF Gmail bodies, Slack `ts` = `created_at`, `metadata_json` `'{}'`, Gmail `internal_date` = `date`, every issue `state_history_json = '[]'`).
- Provisional snapshot comparison (unchanged): MATCH for every column except `linear.linear_projects.links_json` (MISMATCH); confluence pages/versions and linear project teams/members NOT COVERED.
- **A1 (advisory, carried over):** `linear.linear_projects.links_json` (line 146) isn't in the provisional snapshot. If the live table lacks it, the whole transaction rolls back. Safest: drop `links_json` and its `'[]'` value from that insert.

## 8. Check C — Dates, relationships and consistency: **PASS**

**Chronology:** the changed rows keep their timestamps (doc 2026-02-13T16:38:02Z / 16:58:40Z; Leonard's ask 2026-02-13T17:21:07Z; project 2026-02-12T23:24:10Z). Latest event timestamp in the file is still 2026-02-13T23:12:05Z (Arthur's Trello comment); the only later values are the gcal/invite plan times (2026-03-12). Thread, reply and comment order is unchanged from revision 20 (REUSED, §8 there); removing ENG-2445 and its comment removes no parent of any remaining row.

**Changed text checked against base and other injected records (NEW):**

| Claim (line) | Evidence | Result |
|---|---|---|
| Leonard's ask: "Arthur put our accounts into the Linear shutdown project yesterday" (34, sent Feb 13 17:21Z = 09:21 PST) | Project created 2026-02-12T23:24:10Z (Feb 12 15:24 PST); all 28 issues created Feb 12 23:24–23:32Z. | Consistent |
| "my keep list from yesterday and the reply under it" (34) | Keep list `/188` posted 2026-02-12T22:00:01Z (Feb 12 PST); exactly one reply after the injection (§6). | Consistent |
| Project description: costs-tab lines "AWS and the ad accounts in the UA line aren't in here", Arthur shuts AWS down "once the store transfer is done", Leonard "closing the ad networks directly" (147) | HG Costs tab of "Harmony Games P&L and forecast - Jan 2026" (gsheets `data.json` `/sheets_spreadsheets/141/sheets/2`) has a "UA" line (Jan 2026 = 5,000) and a "Hosting / Servers (AWS)" line. No remaining issue is AWS, meta or applovin (issue inserts, lines 156–258). Google Ads (ENG-2466) is "From old receipts", not from the UA line. Leonard's AppLovin request (37, Feb 12 19:44Z) and AppLovin closure (115/39, Feb 13) fit "Leonard is closing the ad networks". Arthur's Trello comment (49, Feb 13 23:12Z) "aws and 1password go by the 17th too then, the store transfer is done by then" fits "once the store transfer is done". | Consistent |
| Conventions doc rule 3: AWS and UA-line ad accounts "stay off the register: he and I are closing those out ourselves" (15, Leonard, Feb 13 16:58Z) | Same facts as the project description row; "he and I" = Arthur (AWS) and Leonard (ad networks). The doc predates the ask that names it (17:21Z). | Consistent |
| Removed "we cancelled the unity ads in the UA line after october" | No remaining injected text mentions Unity Ads (grep: 0); the Unity issue ENG-2438 is Unity Pro seats. Nothing relied on the removed sentence. | Consistent |
| Rule 8 without the ledger basis | Rule 8 now uses the issue owner's figure or the last invoice/receipt only. No remaining row cites a FINANCE_LEDGER amount (the removed ENG-2445 comment held the only one, `$1,485`). This lowers the task's reliance on Snowflake. | Consistent |

**Unchanged claims (REUSED from revision-20 §8, text byte-identical):** Unity termination/$2,348.50 invoice; Cursor cancellation and Mar 5 end; AppLovin request and closure; Leonard's Trello payoff/Carta comment; Sunset invitation emails vs gcal rows; rule 6 "the SVB card on the founders' board"; skipped one-off/filing/insurance/long-gone lines; moved Linear comment facts (Linear $1,832.65, Google Workspace $298.13, DocuSign renewal, Helpshift, Singular, Kapwing). The revision-20 row about Arthur's Trello comment cited the now-removed ENG-2445 comment as its earlier line; it is re-based above on the project description, with the same result.

**Grader-facing text:** none in any changed or injected record.

### Advisories (not failing)

- **A1 — `links_json`** (Check B above).
- **A2 — Base P&L gaps:** the costs tab omits the Aug 2025 Linear payment and the Apr 2025 DocuSign renewal that base emails confirm; your ENG-2441 and ENG-2457 comments say so. Keep rubric rows and OEs off any claim that needs those P&L cells to be right.
- **A3 — Facts carried only by injected records:** Slack $87.22, Google Cloud $4.97, Zapier $73.50, 1Password $19.95, Cursor $40 and the Mar 5 end, Deel $300, Kapwing $24, the AppLovin closure, Unity's Feb 28 seat end, the Feb 18 card date and "support buttons now open email". None conflicts with the base.
- **A4 — Layer amount:** the receipt ($49/month) and Arthur's superseded sheet differ on purpose; only the receipt is current.
- **A5 — Arthur on the Trello card:** base data can't confirm Arthur's board access (no board-membership list; other non-org members act on this board). Not a defect.
- **A6 — Unity reply without its original:** the Unity email is a "Re:" with no `In-Reply-To`, and Arthur's outgoing termination isn't injected. No reference breaks.
- **A7 — `invite.ics` metadata only:** both invitation emails list an `invite.ics` attachment with no bytes; the gcal events carry the data.
- **A8 — Linear number 2445 unused:** the issues jump from ENG-2444 to ENG-2446. It reads like a deleted issue and breaks nothing; renumber ENG-2446–2466 only if you want a continuous run (that would also require changing every OE/rubric reference).
- **A9 — Base context (not caused by the SQL):** the costs-tab "Servers (AWS)" line shows $15 in Nov 2025 and 0 in Jan 2026. With AWS off the register and no injected AWS amount, nothing in v13 depends on that line's value.

## 9. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | Every inserted key is absent from its full base collection and unique in the SQL (complete sweep REUSED; key set only shrank). Removed issue/comment leave no dangling reference. Slack UPDATE target exists with 0 prior replies. |
| B — SQL structure and supported schema rules | PASS | All statements parse; changed doc's style runs end at its 2,727-character length; changed rows keep base formats. Provisional MISMATCH on `linear_projects.links_json` (A1, advisory). |
| C — Dates, relationships and consistency | PASS | All event times ≤ clock (latest 2026-02-13T23:12:05Z; only 2026-03-12 calendar plan fields are later). The new AWS/ad-account carve-out matches the issue list, the costs tab, Leonard's AppLovin closure and Arthur's Trello comment; "yesterday" and "the reply under it" match the records. |

## 10. Next action and downstream

1. Optional: A1 (drop `links_json` from the `linear_projects` insert at line 146).
2. The SQL changed, so every earlier pass that read it is outdated: run `/prompt`, `/hardness`, `/oe`, `/rubric` again, in that order. The saved OEs still describe an older issue set and register (for example ENG-2445 Kling, ENG-2455 AWS, and AWS/meta/applovin register rows built from the ledger); they need updating to this SQL before `/oe`.

## 11. Evidence limits and provenance

- Static scope only. No live execution, database compatibility, search ranking, Agent visibility or difficulty assessment. The schema snapshot is unverified, so mismatches are advisory.
- Sources read this run (`Universe_Normal`): line diff of v12 vs v13 SQL; lint on v13; Slack `messages/C0ADGSZKR3R/2026-02.json` `/188` and a complete full-text search for its ts (5,357 files); gsheets `data.json` `/sheets_spreadsheets/141` title and `/sheets/2` (HG Costs, 75 rows); decoded gdocs body length; grep of the v13 SQL for removed ids/amounts and Unity Ads/ad-account text.
- Reused evidence: revision-20 report sha256 `a5602a61b7342b13dc15367e375a1de96d0ad775090d2fd9b430d0eb52a9de4e` (§6 collision sweep and actor/sender rows, §7 unchanged-row structure, §8 unchanged claim rows, advisories A2–A7), which itself carried revision-19 (`a8e6be5e…b43cd`) results. Verified unchanged: all unchanged SQL lines byte-identical, inserted key values identical, universe manifest, clock and the reference hashes in §1.
- Dependencies for reuse by `/prompt`: Checks A–C above for SQL sha256 `fc9bc388…7e6f`, universe manifest `5e01ac44…f22de450`, clock 2026-02-14T00:00Z, Eval 0 `e034019b…`, WORKFLOW `ee4cd8e1…`, schema `31dcb2b4…`, id_contracts `fc4711ef…`. Any SQL change invalidates them.

### FINAL VERDICT: PASS

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt (then /hardness, /oe, /rubric, since the SQL changed). Optional: drop `links_json` from the `linear_projects` insert (A1).

Evidence limits: Static scope only (no live execution, database compatibility, Agent visibility or difficulty). Schema snapshot unverified (A1 advisory). Some facts exist only in injected records (A3); the base doesn't contradict them. Arthur's Trello board access can't be confirmed from the export (A5).
