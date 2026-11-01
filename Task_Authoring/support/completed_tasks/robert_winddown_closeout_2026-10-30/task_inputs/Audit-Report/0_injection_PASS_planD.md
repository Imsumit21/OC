# Injection data-integrity review — `injection-static-v2`

## 1. Scope

| Field | Value |
|---|---|
| Review | Chat review for your attempt (6adfee3f27ce6ca81b457137), `/injection`, static audit mode |
| Review version | `injection-static-v2` (evidence contract `stage-evidence-v1`) |
| Actual review time | 2026-10-29T06:21Z |
| Clock | 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal` (hg4-2026-08-31 v37); manifest `Evals/references/universes/normal/universe_manifest.json` sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Input reviewed | Injection SQL, revision 19 (attachment `01_Universe_Inject (11).sql`, saved as `Evals/task_inputs/01_Universe_Inject.sql`), 93,857 bytes, sha256 `559744195c35a9164bfea353b61768d993020bbe42f2687889600bbfb3e4f2e4` |
| Previous version | Revision 13, SQL sha256 `50f6a195de7e1d2842b4966192eb31888ef587acc054191ff310ee39473f09d0` (byte-identical to upload `(10)`), reviewed in report sha256 `8f780bb245a9805c49440380df0b517c3933ff940e8e2b2e965578eb6ac5bb0a` (PASS / COMPLETE) |
| References (re-hashed this run, unchanged since that report) | Eval 0 `e034019b…6f663eff`; WORKFLOW `ee4cd8e1…504fcd5d`; schema snapshot `31dcb2b4…d74c5151`; `id_contracts.json` `fc4711ef…d9ed4682`; known_base_issues `79b20289…e7553a7b` |

## 2. Input / authority issues

- The only input for this stage is the SQL. It is substantive: 128 statements (BEGIN, 122 INSERT, 4 UPDATE, COMMIT) across gdrive, gdocs, gsheets, confluence, slack, trello, gmail, gcal, github and linear. The header comment ("122 INSERT (one row each), 4 UPDATE") matches the parse.
- Header and section comments are authoring notes; none mention tool calls, pass rate or gates.
- `known_base_issues.md` (unchanged) lists one normal-universe Snowflake note (MONTHLY_BURN vs FINANCE_LEDGER marketing); no injected row builds on it. The new AppLovin rows sit beside the FINANCE_LEDGER January line (`FIN-000688`, 2026-01-31, applovin −9.80) without contradicting it.

**Change set from revision 13 (row-level parse of both versions):** 57 data rows byte-identical (plus BEGIN/COMMIT); 47 changed; 22 added; 34 removed. Because the change is large, every changed and added row was checked afresh (NEW below), not carried forward.

| Change | Rows | What changed |
|---|---|---|
| Conventions doc (gdocs, line 14) | changed | Rule 3 now says Arthur "skipped one-off, filing and insurance lines and ones long gone"; rule 6 adds "or the SVB card on the founders' board if it sets an earlier date". `style_runs_json` end 2800 → 2904 (= new body length). |
| Slack | 4 added, 1 changed | Arthur's reply to Oliver in #prototype (Cursor already cancelled, seats until Mar 5); Arthur in #executives (Unity confirmed termination); Leonard to the AppLovin rep in the AppLovin channel (Feb 12) and Leonard in #admin_foundersonly (AppLovin closed). Oliver's #prototype message now carries the reply-thread fields. |
| Trello | 2 comments added, card changed | Leonard (22:47Z): card now closes Feb 18; keeps off it and all cancellations done by EOD Feb 17; Carta excepted. Arthur (23:12Z): AWS and 1Password by the 17th too. Card `dateLastActivity` → 23:12:05Z, `badges.comments` → 2. |
| Gmail | 12 rows added (6 threads + 6 messages) | Cursor cancellation (Arthur, Feb 13); Unity termination reply (Arthur + Leonard copies, Feb 13); AppLovin account closure (Leonard, Feb 13); Sunset review invitation (Robert + Arthur copies, Feb 12). |
| Linear | project description changed; 29 issues now ENG-2438–2466 (ENG-2459 is a new key); 3 comment ids new | Issues for OpenAI, Typecast.ai, Unity Asset Store, Veed, Kling, Hailuo.ai, JetBrains, Adobe, Dailybot, Solsten, Office 365, Notarize, UA Assets, Fondo, Insurance and Calendly removed with their comments. Remaining issues renumbered (e.g. Linear ENG-2448 → ENG-2441). Every surviving comment keeps its exact text, author and time and stays on an issue with the same title; three keep their text under new ids (QuickBooks `cmt_5fb637…`, Carta `cmt_f430b6…`, CodeRabbit `cmt_8f765d…`). |

## 3. Lint (`hg_injection_lint.py`, injection-lint-v1, run on this SQL hash)

Flags: FAIL 0, CHECK 0, INFO 1.

| Flag | Location | Resolution |
|---|---|---|
| INFO `unparsed` (metadata-only media) | line 9, `gdrive.drive_files` `f_4ac7a77383e7317eedcd83` `helpshift_export_2026-02-13.zip` | Accepted, unchanged. A zip package is metadata-only, as in the base; Oliver's comment (line 162) cites it by name only. It becomes a FAIL only if an OE or rubric row needs the zip's contents. |

A clean lint doesn't replace checks A–C; they were done below.

## 4. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; hash, manifest, review version | NEW, done (revision 19 saved from the attachment) |
| Run lint, resolve flags | NEW, done (1 INFO, resolved) |
| Inventory every statement | NEW, done (128/128, §5) |
| Check A: references, collisions, ID contracts | PASS (NEW for all changed/added keys; REUSED for 57 identical rows) |
| Check B: structure and supported schema rules | PASS (advisory A1 carried over) |
| Check C: dates, relationships, consistency | PASS (every new claim checked against base sources, §8) |
| Report and verdict | NEW, done |

**Reuse basis (stage-evidence-v1):** the 57 byte-identical rows reuse the revision-13 report's per-record results (report sha256 `8f780bb2…6ac5bb0a`, §5 ledger, §6 reference table, §7 structure checks, §8 claim table), which carried earlier revisions' complete checks. Moved Linear comment texts reuse that report's §8 factual results because text, author, time and issue title are unchanged. Dependencies verified unchanged: statement text, universe manifest `5e01ac44…`, clock and every reference hash in §1. Collision checks for all changed/added keys and all new claims were re-run this time.

## 5. Operation ledger (every statement, execution order)

Line = line of the statement's first keyword. All 122 INSERT keys are unique within their tables in the SQL. Basis: REUSED = byte-identical to revision 13; NEW = changed or added, checked this run.

| # | Line | Table | Op | Record / target | Latest event time in row | Result | Basis |
|---|---|---|---|---|---|---|---|
| 1 | 5 | `—` | BEGIN | `—` | — | PASS | REUSED |
| 2 | 7 | `gdrive.drive_files` | INSERT | `f_1326e66bcabfda8fd29e4a` | 2026-02-13T16:58:40Z | PASS | REUSED |
| 3 | 9 | `gdrive.drive_files` | INSERT | `f_4ac7a77383e7317eedcd83` | 2026-02-13T15:04:51Z | PASS | REUSED |
| 4 | 11 | `gdrive.drive_files` | INSERT | `f_768cd23a00c4b12fa0e975` | 2026-02-10T18:31:55Z | PASS | REUSED |
| 5 | 14 | `gdocs.docs_documents` | INSERT | `f_1326e66bcabfda8fd29e4a` | 2026-02-13T16:58:40Z | PASS | NEW (changed) |
| 6 | 17 | `gsheets.sheets_spreadsheets` | INSERT | `f_768cd23a00c4b12fa0e975` | 2026-02-10T18:31:55Z | PASS | REUSED |
| 7 | 19 | `gsheets.sheets_sheets` | INSERT | `f_768cd23a00c4b12fa0e975` | — | PASS | REUSED |
| 8 | 22 | `confluence.confluence_pages` | INSERT | `page_ua_vendor_closeout` | 2025-03-18T15:20:00Z | PASS | REUSED |
| 9 | 24 | `confluence.confluence_page_versions` | INSERT | `ver_64b0ed607e093b18a698fb883a584aa6` | 2025-03-18T15:20:00Z | PASS | REUSED |
| 10 | 27 | `slack.slack_messages` | INSERT | `b9ef575bec54b095edb75a0fe83580f5` | 2026-02-13T02:14:36.205117Z | PASS | REUSED |
| 11 | 29 | `slack.slack_messages` | INSERT | `fda86aac9fb55c96ffee4bba3e59cc14` | 2026-02-13T10:02:18.774231Z | PASS | NEW (changed) |
| 12 | 31 | `slack.slack_messages` | INSERT | `6303f60fefe86f1c3ebaa864318f6907` | 2026-02-13T14:07:33.518204Z | PASS | NEW (added) |
| 13 | 33 | `slack.slack_messages` | INSERT | `9e245e76cbaf7f080e1995ec0c4ec30d` | 2026-02-13T17:21:07.448213Z | PASS | REUSED |
| 14 | 35 | `slack.slack_messages` | INSERT | `cd1423b23b5d39c3341a5838c31a3138` | 2026-02-13T21:18:40.226917Z | PASS | NEW (added) |
| 15 | 37 | `slack.slack_messages` | INSERT | `fb53c42227d5b5868efdade6b69c3738` | 2026-02-12T19:44:05.613380Z | PASS | NEW (added) |
| 16 | 39 | `slack.slack_messages` | INSERT | `87626c59a436ce9c3a87c0eda56d1354` | 2026-02-13T22:40:26.317702Z | PASS | NEW (added) |
| 17 | 41 | `slack.slack_messages` | UPDATE | `id = 6d8c8d8affd1255b13d8d875f1547e70` | — | PASS | REUSED |
| 18 | 43 | `trello.trello_cards` | INSERT | `698f48be4ba0affafbf153db` | 2026-02-13T23:12:05Z | PASS | NEW (changed) |
| 19 | 45 | `trello.trello_actions` | INSERT | `698f48be304fbb37e4e3aafa` | 2026-02-13T15:52:30Z | PASS | REUSED |
| 20 | 47 | `trello.trello_actions` | INSERT | `698fa9f7f77cecfe5c7aa524` | 2026-02-13T22:47:19Z | PASS | NEW (added) |
| 21 | 49 | `trello.trello_actions` | INSERT | `698fafc529f7ffa32ff7dd20` | 2026-02-13T23:12:05Z | PASS | NEW (added) |
| 22 | 52 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1856945900224536585` | — | PASS | REUSED |
| 23 | 54 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com>` | 2026-02-12T18:40:12Z | PASS | REUSED |
| 24 | 56 | `gmail.gmail_threads` | INSERT | `leonard.hayes@harmonygames.co/1856945900224877235` | — | PASS | REUSED |
| 25 | 58 | `gmail.gmail_messages` | INSERT | `leonard.hayes@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gma` | 2026-02-12T18:40:12Z | PASS | REUSED |
| 26 | 60 | `gmail.gmail_threads` | INSERT | `arthur.blake@harmonygames.co/1856945900225226172` | — | PASS | REUSED |
| 27 | 62 | `gmail.gmail_messages` | INSERT | `arthur.blake@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmai` | 2026-02-12T18:40:12Z | PASS | REUSED |
| 28 | 64 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1856965916492026238` | — | PASS | REUSED |
| 29 | 66 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>` | 2026-02-12T23:58:21Z | PASS | REUSED |
| 30 | 68 | `gmail.gmail_threads` | INSERT | `leonard.hayes@harmonygames.co/1856965916492755786` | — | PASS | REUSED |
| 31 | 70 | `gmail.gmail_messages` | INSERT | `leonard.hayes@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gma` | 2026-02-12T23:58:21Z | PASS | REUSED |
| 32 | 72 | `gmail.gmail_threads` | INSERT | `arthur.blake@harmonygames.co/1856965916492023943` | — | PASS | REUSED |
| 33 | 74 | `gmail.gmail_messages` | INSERT | `arthur.blake@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmai` | 2026-02-12T23:58:21Z | PASS | REUSED |
| 34 | 76 | `gmail.gmail_threads` | UPDATE | `id = robert@harmonygames.co/1856965916492026238` | — | PASS | REUSED |
| 35 | 77 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com>` | 2026-02-13T18:20:44Z | PASS | REUSED |
| 36 | 79 | `gmail.gmail_threads` | UPDATE | `id = leonard.hayes@harmonygames.co/1856965916492755786` | — | PASS | REUSED |
| 37 | 80 | `gmail.gmail_messages` | INSERT | `leonard.hayes@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gma` | 2026-02-13T18:20:44Z | PASS | REUSED |
| 38 | 82 | `gmail.gmail_threads` | UPDATE | `id = arthur.blake@harmonygames.co/1856965916492023943` | — | PASS | REUSED |
| 39 | 83 | `gmail.gmail_messages` | INSERT | `arthur.blake@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmai` | 2026-02-13T18:20:44Z | PASS | REUSED |
| 40 | 85 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1842712894505970340` | — | PASS | REUSED |
| 41 | 87 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAIoQDHYpNPHXVgnNS8DUmtr__81CmMffz7hcWJv@mail.gmail.com>` | 2025-09-08T16:12:40Z | PASS | REUSED |
| 42 | 89 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1842984194671106077` | — | PASS | REUSED |
| 43 | 91 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAowZ1ukjS1ZxLCL4aRt1VM-c-GnNMTNWVQS47OM@mail.gmail.com>` | 2025-09-11T16:04:52Z | PASS | REUSED |
| 44 | 93 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1856114791547562583` | — | PASS | REUSED |
| 45 | 95 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CA4Ce6Oa74xUtCgFI1iGnZMieCxsUh90MhimgGu3@mail.gmail.com>` | 2026-02-03T14:30:05Z | PASS | REUSED |
| 46 | 97 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1856859516436705234` | — | PASS | REUSED |
| 47 | 99 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAxSGYrkpVAs45dr7lAugwSThN-X-ma7vq_V1xAV@mail.gmail.com>` | 2026-02-11T19:47:10Z | PASS | REUSED |
| 48 | 101 | `gmail.gmail_threads` | INSERT | `arthur.blake@harmonygames.co/1857018744799627050` | — | PASS | NEW (added) |
| 49 | 103 | `gmail.gmail_messages` | INSERT | `arthur.blake@harmonygames.co/<CAiNg4QTh-tYTcaxqfYeePA5pS-5wWPkXvAPL9qS@mail.gmai` | 2026-02-13T13:58:02Z | PASS | NEW (added) |
| 50 | 105 | `gmail.gmail_threads` | INSERT | `arthur.blake@harmonygames.co/1857044821836129041` | — | PASS | NEW (added) |
| 51 | 107 | `gmail.gmail_messages` | INSERT | `arthur.blake@harmonygames.co/<CAUS1JuCoozyJO5SgXcz-1dVbo7duszBh21aQwZr@mail.gmai` | 2026-02-13T20:52:31Z | PASS | NEW (added) |
| 52 | 109 | `gmail.gmail_threads` | INSERT | `leonard.hayes@harmonygames.co/1857044821836034704` | — | PASS | NEW (added) |
| 53 | 111 | `gmail.gmail_messages` | INSERT | `leonard.hayes@harmonygames.co/<CAUS1JuCoozyJO5SgXcz-1dVbo7duszBh21aQwZr@mail.gma` | 2026-02-13T20:52:31Z | PASS | NEW (added) |
| 54 | 113 | `gmail.gmail_threads` | INSERT | `leonard.hayes@harmonygames.co/1857051067155022210` | — | PASS | NEW (added) |
| 55 | 115 | `gmail.gmail_messages` | INSERT | `leonard.hayes@harmonygames.co/<CAlutvfoiS_dRLmmsgE-rPqfCnV24mT0fiHMbdWe@mail.gma` | 2026-02-13T22:31:47Z | PASS | NEW (added) |
| 56 | 117 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1856961002865672224` | — | PASS | NEW (added) |
| 57 | 119 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<calendar-951230da-b530-be28-7f3e-7de01fef9ec5@google.com` | 2026-02-12T22:40:15Z | PASS | NEW (added) |
| 58 | 121 | `gmail.gmail_threads` | INSERT | `arthur.blake@harmonygames.co/1856961002865002536` | — | PASS | NEW (added) |
| 59 | 123 | `gmail.gmail_messages` | INSERT | `arthur.blake@harmonygames.co/<calendar-6e72e8ad-9998-760c-3f6b-0e9e31fa44ce@goog` | 2026-02-12T22:40:15Z | PASS | NEW (added) |
| 60 | 126 | `gcal.gcal_events` | INSERT | `evt_2ac66383ee72bbb05a0376` | 2026-02-12T22:40:15Z (start/end 2026-03-12 = plan fields) | PASS | REUSED |
| 61 | 128 | `gcal.gcal_events` | INSERT | `evt_f1d245d44ceff5a6e049c0` | 2026-02-12T22:40:15Z (start/end 2026-03-12 = plan fields) | PASS | REUSED |
| 62 | 130 | `gcal.gcal_events` | INSERT | `evt_d1fe12afe85ffbb49bd998` | 2026-02-12T22:40:15Z (start/end 2026-03-12 = plan fields) | PASS | REUSED |
| 63 | 133 | `github.github_pull_requests` | INSERT | `harmonygames-Games/Combo-Fighters#38` | 2026-02-13T09:41:12Z | PASS | REUSED |
| 64 | 135 | `github.github_branches` | INSERT | `harmonygames-Games/Combo-Fighters:oliver/final-build-settings` | — | PASS | REUSED |
| 65 | 137 | `github.github_commits` | INSERT | `c769b476f150a76280886f194b4d2186cfd96ca4` | 2026-02-13T09:23:51Z | PASS | REUSED |
| 66 | 139 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/Combo-Fighters#38#c_0` | — | PASS | REUSED |
| 67 | 141 | `github.github_pr_comments` | INSERT | `harmonygames-Games/Combo-Fighters#38#c_1` | 2026-02-13T09:41:12Z | PASS | REUSED |
| 68 | 143 | `github.github_timeline_events` | INSERT | `harmonygames-Games/Combo-Fighters#38#ev_1` | 2026-02-13T09:41:12Z | PASS | REUSED |
| 69 | 146 | `linear.linear_projects` | INSERT | `3f0c6a52-ee13-4b1e-68e3-a74bcc33818a` | 2026-02-12T23:24:10Z | PASS | NEW (changed) |
| 70 | 148 | `linear.linear_project_teams` | INSERT | `ptm_2183726e36ddf7f8` | 2026-02-12T23:24:10Z | PASS | REUSED |
| 71 | 150 | `linear.linear_project_members` | INSERT | `pmem_dec4e6c3f1315d8a` | 2026-02-12T23:24:10Z | PASS | REUSED |
| 72 | 152 | `linear.linear_project_members` | INSERT | `pmem_5648d2826ae7a30d` | 2026-02-12T23:24:10Z | PASS | REUSED |
| 73 | 154 | `linear.linear_project_members` | INSERT | `pmem_ca4f8a31e35bad07` | 2026-02-12T23:24:10Z | PASS | REUSED |
| 74 | 156 | `linear.linear_issues` | INSERT | `ENG-2438` | 2026-02-13T19:05:12Z | PASS | REUSED |
| 75 | 158 | `linear.linear_comments` | INSERT | `cmt_5da8c3467fc022248fb3` | 2026-02-13T19:05:12Z | PASS | REUSED |
| 76 | 160 | `linear.linear_issues` | INSERT | `ENG-2439` | 2026-02-13T16:12:40Z | PASS | REUSED |
| 77 | 162 | `linear.linear_comments` | INSERT | `cmt_96ae7b3689c1d073a2ff` | 2026-02-13T15:12:18Z | PASS | REUSED |
| 78 | 164 | `linear.linear_comments` | INSERT | `cmt_51ff7e6b4cdea7033c08` | 2026-02-13T16:12:40Z | PASS | REUSED |
| 79 | 166 | `linear.linear_issues` | INSERT | `ENG-2440` | 2026-02-12T23:52:03Z | PASS | REUSED |
| 80 | 168 | `linear.linear_comments` | INSERT | `cmt_e8aa0ee7c1bbe08a47c9` | 2026-02-12T23:52:03Z | PASS | REUSED |
| 81 | 170 | `linear.linear_issues` | INSERT | `ENG-2441` | 2026-02-12T23:58:30Z | PASS | NEW (changed) |
| 82 | 172 | `linear.linear_comments` | INSERT | `cmt_37c23c5d30cc6597ebe9` | 2026-02-12T23:58:30Z | PASS | NEW (changed) |
| 83 | 174 | `linear.linear_issues` | INSERT | `ENG-2442` | 2026-02-12T23:25:21Z | PASS | NEW (changed) |
| 84 | 176 | `linear.linear_issues` | INSERT | `ENG-2443` | 2026-02-12T23:25:38Z | PASS | NEW (changed) |
| 85 | 178 | `linear.linear_issues` | INSERT | `ENG-2444` | 2026-02-13T16:24:02Z | PASS | NEW (changed) |
| 86 | 180 | `linear.linear_comments` | INSERT | `cmt_497a61c14b69830f198a` | 2026-02-13T16:24:02Z | PASS | NEW (changed) |
| 87 | 182 | `linear.linear_issues` | INSERT | `ENG-2445` | 2026-02-13T19:12:45Z | PASS | NEW (changed) |
| 88 | 184 | `linear.linear_comments` | INSERT | `cmt_276e0b8a551891ddbdff` | 2026-02-13T19:12:45Z | PASS | NEW (changed) |
| 89 | 186 | `linear.linear_issues` | INSERT | `ENG-2446` | 2026-02-13T01:30:22Z | PASS | NEW (changed) |
| 90 | 188 | `linear.linear_comments` | INSERT | `cmt_a83cc20eced4c1064f0a` | 2026-02-13T01:30:22Z | PASS | NEW (changed) |
| 91 | 190 | `linear.linear_issues` | INSERT | `ENG-2447` | 2026-02-13T01:29:55Z | PASS | NEW (changed) |
| 92 | 192 | `linear.linear_comments` | INSERT | `cmt_8ab16d9d7ac715d1c9a7` | 2026-02-13T01:29:55Z | PASS | NEW (changed) |
| 93 | 194 | `linear.linear_issues` | INSERT | `ENG-2448` | 2026-02-13T01:33:10Z | PASS | NEW (changed) |
| 94 | 196 | `linear.linear_comments` | INSERT | `cmt_e8ae507893bfdb06c8c7` | 2026-02-13T01:33:10Z | PASS | NEW (changed) |
| 95 | 198 | `linear.linear_issues` | INSERT | `ENG-2449` | 2026-02-13T16:25:31Z | PASS | NEW (changed) |
| 96 | 200 | `linear.linear_comments` | INSERT | `cmt_5fb637b0247b82594b16` | 2026-02-13T16:25:31Z | PASS | NEW (added) |
| 97 | 202 | `linear.linear_issues` | INSERT | `ENG-2450` | 2026-02-13T16:26:19Z | PASS | NEW (changed) |
| 98 | 204 | `linear.linear_comments` | INSERT | `cmt_e3da997ff7b6575fbea0` | 2026-02-13T16:26:19Z | PASS | NEW (changed) |
| 99 | 206 | `linear.linear_issues` | INSERT | `ENG-2451` | 2026-02-13T16:29:47Z | PASS | NEW (changed) |
| 100 | 208 | `linear.linear_comments` | INSERT | `cmt_f430b60b346c70afda13` | 2026-02-13T16:29:47Z | PASS | NEW (added) |
| 101 | 210 | `linear.linear_issues` | INSERT | `ENG-2452` | 2026-02-13T16:31:05Z | PASS | NEW (changed) |
| 102 | 212 | `linear.linear_comments` | INSERT | `cmt_ae352002e2f80996f096` | 2026-02-13T16:31:05Z | PASS | NEW (changed) |
| 103 | 214 | `linear.linear_issues` | INSERT | `ENG-2453` | 2026-02-13T16:31:48Z | PASS | NEW (changed) |
| 104 | 216 | `linear.linear_comments` | INSERT | `cmt_276837877e2b3edc466a` | 2026-02-13T16:31:48Z | PASS | NEW (changed) |
| 105 | 218 | `linear.linear_issues` | INSERT | `ENG-2454` | 2026-02-12T23:28:45Z | PASS | NEW (changed) |
| 106 | 220 | `linear.linear_issues` | INSERT | `ENG-2455` | 2026-02-13T16:32:02Z | PASS | NEW (changed) |
| 107 | 222 | `linear.linear_comments` | INSERT | `cmt_62852832c28dc669e459` | 2026-02-13T16:32:02Z | PASS | NEW (changed) |
| 108 | 224 | `linear.linear_issues` | INSERT | `ENG-2456` | 2026-02-13T16:32:20Z | PASS | NEW (changed) |
| 109 | 226 | `linear.linear_comments` | INSERT | `cmt_2b4807a6cf797d1f4886` | 2026-02-13T16:32:20Z | PASS | NEW (changed) |
| 110 | 228 | `linear.linear_issues` | INSERT | `ENG-2457` | 2026-02-13T16:33:51Z | PASS | NEW (changed) |
| 111 | 230 | `linear.linear_comments` | INSERT | `cmt_bbdca23f075e9fca5cb8` | 2026-02-13T16:33:51Z | PASS | NEW (changed) |
| 112 | 232 | `linear.linear_issues` | INSERT | `ENG-2458` | 2026-02-13T16:36:10Z | PASS | NEW (changed) |
| 113 | 234 | `linear.linear_comments` | INSERT | `cmt_6e664bfa3fea62baabb5` | 2026-02-13T16:36:10Z | PASS | NEW (changed) |
| 114 | 236 | `linear.linear_issues` | INSERT | `ENG-2459` | 2026-02-13T00:05:31Z | PASS | NEW (added) |
| 115 | 238 | `linear.linear_comments` | INSERT | `cmt_8f765d1313e9b01a8c22` | 2026-02-13T00:05:31Z | PASS | NEW (added) |
| 116 | 240 | `linear.linear_issues` | INSERT | `ENG-2460` | 2026-02-13T00:06:58Z | PASS | NEW (changed) |
| 117 | 242 | `linear.linear_comments` | INSERT | `cmt_7cf5d70170f54a8f925f` | 2026-02-13T00:06:58Z | PASS | NEW (changed) |
| 118 | 244 | `linear.linear_issues` | INSERT | `ENG-2461` | 2026-02-13T16:37:02Z | PASS | NEW (changed) |
| 119 | 246 | `linear.linear_comments` | INSERT | `cmt_2238bd7d0a60d8e4f31c` | 2026-02-13T16:37:02Z | PASS | NEW (changed) |
| 120 | 248 | `linear.linear_issues` | INSERT | `ENG-2462` | 2026-02-13T01:28:49Z | PASS | NEW (changed) |
| 121 | 250 | `linear.linear_comments` | INSERT | `cmt_75b0e4e31a02f9a022bd` | 2026-02-13T01:28:49Z | PASS | NEW (changed) |
| 122 | 252 | `linear.linear_issues` | INSERT | `ENG-2463` | 2026-02-13T00:09:12Z | PASS | NEW (changed) |
| 123 | 254 | `linear.linear_comments` | INSERT | `cmt_2785f039cfee9d256150` | 2026-02-13T00:09:12Z | PASS | NEW (changed) |
| 124 | 256 | `linear.linear_issues` | INSERT | `ENG-2464` | 2026-02-13T01:34:02Z | PASS | NEW (changed) |
| 125 | 258 | `linear.linear_comments` | INSERT | `cmt_5d88052b6f8c1b2fc181` | 2026-02-13T01:34:02Z | PASS | NEW (changed) |
| 126 | 260 | `linear.linear_issues` | INSERT | `ENG-2465` | 2026-02-12T23:31:52Z | PASS | NEW (changed) |
| 127 | 262 | `linear.linear_issues` | INSERT | `ENG-2466` | 2026-02-12T23:32:09Z | PASS | NEW (changed) |
| 128 | 264 | `—` | COMMIT | `—` | — | PASS | REUSED |

## 6. Check A — Records, references and IDs: **PASS**

| Item | Evidence | Result |
|---|---|---|
| Linear issue keys ENG-2438–2466 (incl. new ENG-2459) | `hg_records` on linear `data.json` `/issues`, fields `identifier`, `id` and `number` (2438–2466): 3,852 records, `scan_complete: true`, 0 matches. Full-text scan of linear `data.json` for "ENG-2459": 0. | PASS |
| New comment ids `cmt_5fb637b0247b82594b16`, `cmt_f430b60b346c70afda13`, `cmt_8f765d1313e9b01a8c22` | Full-text scan of linear `data.json` for each full id and its hex part: 0 (complete). Each inserted once in the SQL. | PASS |
| Linear actors | `/users` (41, complete): `usr_cc3e90160f490686` = arthur.blake, `usr_63fffeb4fab5233e` = leonard.hayes, `usr_bdf01b53c6a92c5e` = oliver.brooks, `usr_Robert` = robert@. Project `3f0c6a52…` absent from base `/projects` (complete). | PASS |
| Parents | Every comment follows its issue in the SQL; ENG-* issues follow the project; Slack reply `6303f60f…` (line 31) follows parent `fda86aac…` (line 29); each Gmail message follows its thread; Trello comments follow the card. | PASS |
| New Slack message ids (4) and ts values | `lookup` slack `messages/*.json` (5,353 files, 687,230 records, complete): 0 matches for all 7 injected ids. Full-text search for the 4 new ts strings: 0 (complete). | PASS |
| Slack actors and channels | `users.json` (complete): EMPLOYEE_0003 = Oliver Brooks, EMPLOYEE_0025 = Arthur Blake, EMPLOYEE_0038 = Leonard Hayes, PERSON_2705 = Marcus Lee. `channels.json`: C09UHHN6PFZ #prototype (Oliver, Arthur members), C07C2866011 #executives (Arthur member), C1C2137664A3 `applovin_[SOURCE_ORG_0001]` (Leonard, PERSON_2705 members), C04UEQVDVB7 #admin_foundersonly (Leonard member). All five channel records were returned; the run flagged the file as changing mid-read (lazy-loading filesystem), which doesn't affect matches that were found. PERSON_2705 is the AppLovin account rep in base (199 messages in that channel: CPI benchmarks, campaign setup, Dec 2025 event-postback requests), so Leonard addressing him about the ad account fits. | PASS |
| Trello | `/actions` (5,294, complete): 0 matches for `698fa9f7…`, `698fafc5…`. Action ids' first 8 hex = 2026-02-13T22:47:19Z / 23:12:05Z = their `date`. `/members`: PERSON_6094 = Leonard Hayes, `2162c1ba310341bf318f48b7` = Arthur Blake. Comment `data_json` matches the base commentCard shape (board, card, idCard, list, text, textData). | PASS (A5 advisory) |
| New Gmail thread ids (6) and Message-IDs (5) | Full-text Gmail scan (`threads/*.json`, 88,726 files, complete): 0 matches for every new thread number and Message-ID. Each thread number decodes to its message's send time. | PASS |
| Gmail senders | Base Gmail confirms the placeholders: `SVC_2674` = Cursor (product mail to arthur.blake/oliver), `SVC_5543` = Unity (Unity Pro mail to arthur.blake), `SVC_0553` = AppLovin billing (monthly invoices/statements to leonard.hayes, 2025). `PERSON_7731` (Maya, Sunset) is an external contact introduced by the injection; absent from base Gmail, Slack, gcal and contacts (complete), used consistently. | PASS |
| Removed rows | No remaining text references a removed issue, comment or vendor (searched for every removed vendor name, `issuefeed` and any `ENG-` number in text fields: 0). | PASS |
| ID contracts / Drive readability / one account per person | Lint clean; every new Gmail thread `history_id` is NULL; mailboxes are the existing robert@, arthur.blake@, leonard.hayes@. No new Drive files or accounts. | PASS |

## 7. Check B — SQL structure and supported schema rules: **PASS**

- All 128 statements parse (lint: no `missing_required`, `json_shape`, `generated_column` or `text_time_format` flags). Each VALUES tuple matches its column list. No `text_fts`/`body_text_fts` set.
- Slack rows: `ts` = `created_at` for all 7 inserts; parent `fda86aac…` now has `thread_ts_legacy` = its own ts, `reply_count` 1, `latest_reply` = the reply's ts; `metadata_json` `'{}'`, list columns `'[]'`.
- Gmail rows: `internal_date` = `date` = `Date` header (weekdays correct) for all 12 new rows. Invitation subjects say PDT, correct for Mar 12, 2026 (DST starts Mar 8).
- gdocs: `style_runs_json` last run ends at 2904 = `body_text` length.
- Linear: every `*_at` is `YYYY-MM-DDTHH:MM:SSZ`; every issue has `state_history_json = '[]'`; apostrophes doubled.
- Provisional snapshot comparison: MATCH for every column except `linear.linear_projects.links_json` (MISMATCH); confluence pages/versions and linear project teams/members NOT COVERED (unchanged from earlier revisions).
- **A1 (advisory, carried over):** `linear.linear_projects.links_json` (line 146) isn't in the provisional snapshot. If the live table lacks it, the whole transaction rolls back. Safest: drop `links_json` and its `'[]'` value from that insert.

## 8. Check C — Dates, relationships and consistency: **PASS**

**Clock and chronology:** latest event timestamp is 2026-02-13T23:12:05Z (Arthur's Trello comment); the only later values are the gcal/invite plan times (2026-03-12). For all 29 issues, `created_at` rises with the number (23:24:13Z → 23:32:09Z on Feb 12, after the project at 23:24:10Z), every comment is later than its issue, and `updated_at` equals the latest comment (or `created_at` when there is none). Cross-service order holds: Cursor email 13:58:02Z → Arthur's "this morning" Slack reply 14:07:33Z; Arthur's Unity termination (ENG-2438 comment 19:05:12Z) → Unity reply 20:52:31Z → Arthur in #executives 21:18:40Z; Leonard's request to the AppLovin rep Feb 12 19:44:05Z → AppLovin email Feb 13 22:31:47Z → Leonard's post 22:40:26Z; Leonard's Trello comment 22:47:19Z → Arthur's 23:12:05Z.

**New claims checked against base sources:**

| Claim (line) | Base evidence | Result |
|---|---|---|
| Unity: "termination of your Unity Pro subscription (11 seats)… no further invoices, including the one scheduled for February 19" (107, 111); Arthur's #executives echo (35) | Arthur's mailbox, Unity invoice INZ02614348 PDF (`arthur.blake@…/1854822027634725037/…/att_0001.pdf`): date Jan 19, 2026, UTY-PRO qty 11, $2,200 + $148.50 tax = $2,348.50 (Dec 2025 invoice same total). #winddown `/174` (Leonard, Feb 12 21:35Z) drafts the termination note "for Unity team" for Arthur; `/190` assigns "Blake to email Unity". | Supported |
| Cursor: "Cursor Teams subscription… canceled… access until March 5, 2026" to Arthur (103); Arthur to Oliver "seats keep working until mar 5" (31) | #winddown `/203` (Arthur, Feb 12 22:59Z) "cursor and … cancelled"; Leonard's Feb 12 list `/187` "cursor (Blake)". Arthur's unchanged ENG-2460 comment: "$40/mo, renews on the 5th". Base has only Cursor product mail (no billing mail) to contradict. | Supported |
| AppLovin: Leonard asks the rep to close the ad account after this week's spend (37); AppLovin: "closed as of today's spend (February 13, 2026)… statement for February spend will follow" (115); Leonard's post (39) | FINANCE_LEDGER `FIN-000688` 2026-01-31 applovin −9.80 shows spend was still running in January. AppLovin invoices/statements go to leonard.hayes in base. Dec 2025 channel: Leonard tells the rep "We will be running UA". | No contradiction |
| Trello (Leonard): payoff posted early, card closes the 18th, keeps off by EOD 17th, cancellations by EOD 17th; "Only exception is carta, that renewal is in august and stays as I said" (47) | Card description (unchanged) set Feb 20 / Feb 19; this later comment by the card's creator supersedes it. Carta: #winddown `/182` (Leonard, Feb 12) "we have time for Carta renewal so I'm not gonna really touch that"; `/187` "Carta (renewal 8/15 and tied to Chase account…)"; ENG-2451 "renews aug 15". No base message after Feb 12 23:04Z in #winddown, and none mentions the payoff timing ("payoff" 0, Feb 2026 Slack). | Supported |
| Trello (Arthur): "aws and 1password go by the 17th too then, the store transfer is done by then" (49) | Updates Arthur's own earlier lines (ENG-2445 19:12Z "keeping dd prod up through the month for the store transfer"; ENG-2464 "cancel it last"), 4 hours later, in reply to Leonard's new date. Base sets no store-transfer date (Feb 2026 Slack "transfer": repos and AWS credits only; "1password": 0). | Valid later update |
| Sunset invitation emails (119, 123) | Match the unchanged gcal rows exactly: 2026-03-12T17:00–17:45Z (10:00–10:45 PDT), organizer leonard.hayes, guests robert/arthur/PERSON_7731, Meet `dea-8d47-3a8`, created 2026-02-12T22:40:15Z = email time. | Consistent |
| Conventions doc rule 3 / project description: skipped one-off, filing, insurance and long-gone lines (14, 146) | Matches the removed issues (OpenAI, Asset Store, Solsten, Notarize, UA Assets = one-off/pay-per-use; Fondo, Insurance; Veed, Kling, Hailuo, JetBrains, Adobe, Dailybot, Office 365, Typecast, Calendly = ended). Remaining "From old receipts" issues (Lucidchart, Google Ads) are Arthur's own picks for the register to judge. | Consistent |
| Rule 6 "the SVB card on the founders' board" (14) | Card 456 sits on Trello board "Harmony Games" (the founders' to-do board: lawyer, investor update, metrics cards); the only other open boards are DD Product Roadmap, UA/BD and ZM ROADMAP. | Resolves |
| Moved Linear comments (text, author, time unchanged) | Facts verified in the revision-13 report §8 and earlier (Linear $1,832.65 and P&L stop; Google Workspace $298.13; DocuSign renewal; Unity $2,348.50; Helpshift; Singular; AWS $1,485 = `FIN-000687`). Kapwing "cancelled with cursor" matches `/187` "Kapwing (Blake)" and `/203`. | Supported (REUSED) |

**Grader-facing text:** none in any changed or injected record.

### Advisories (not failing)

- **A1 — `links_json`** (Check B above).
- **A2 — Base P&L gaps:** the costs tab omits the Aug 2025 Linear payment and the Apr 2025 DocuSign renewal that base emails confirm; your ENG-2441 and ENG-2457 comments say so. Keep rubric rows and OEs off any claim that needs those P&L cells to be right.
- **A3 — Facts carried only by injected records:** Slack $87.22, Google Cloud $4.97, Zapier $73.50, 1Password $19.95, Cursor $40 and the Mar 5 end, Deel $300, Kapwing $24, the AppLovin closure, Unity's Feb 28 seat end, the Feb 18 card date and "support buttons now open email". None conflicts with the base.
- **A4 — Layer amount:** the receipt ($49/month) and Arthur's superseded sheet (39) differ on purpose; only the receipt is current.
- **A5 — Arthur on the Trello card:** Arthur has no other Trello activity and isn't in the Harmony Games organization's `memberIds` (only Leonard and PERSON_6095). The export has no board-membership list and other non-org members act on this board, so this isn't a defect; it just means base data can't confirm Arthur's board access.
- **A6 — Unity reply without its original:** the Unity email is a "Re:" with no `In-Reply-To`, and Arthur's outgoing termination isn't injected. No reference breaks; add Arthur's sent message to the thread only if you want the exchange to read complete.
- **A7 — `invite.ics` metadata only:** both invitation emails list an `invite.ics` attachment with no bytes. Gmail attachment reads return no bytes anyway (acl.md); the gcal events carry the data.

## 9. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | All new keys absent from complete base collections (Linear issues/numbers/comments, Slack ids/ts, Trello actions, Gmail thread ids/Message-IDs) and unique in the SQL; actors, channels, members and sender identities resolve; removed rows leave no dangling references. |
| B — SQL structure and supported schema rules | PASS | All statements parse; timestamps, thread fields and JSON shapes agree; Linear text dates in base format. Provisional MISMATCH on `linear_projects.links_json` (A1, advisory). |
| C — Dates, relationships and consistency | PASS | All event times ≤ clock (plan fields excepted); cross-service order holds; every new claim is supported by base invoices, #winddown, the FINANCE_LEDGER or the gcal rows, or is a valid later update by the same person. |

## 10. Next action and downstream

1. Optional: A1 (drop `links_json` from the `linear_projects` insert at line 146).
2. Because the SQL changed, every earlier pass that read it is outdated: run `/prompt`, `/hardness`, `/oe`, `/rubric` again, in that order.

## 11. Evidence limits and provenance

- Static scope only. No live execution, database compatibility, search ranking, Agent visibility or difficulty assessment. The schema snapshot is unverified, so mismatches are advisory.
- Sources read this run (all `Universe_Normal`): `hg_records` checks on linear `data.json` (`/issues` identifier/id/number, `/comments`, `/users`, `/projects`), slack `users.json` and `channels.json`, trello `data.json` (`/members`, `/actions`, `/cards`). Linear `data.json` full-text id scans (complete). Slack `lookup` over `messages/*.json` (complete) and full-text ts searches (complete); Feb 2026 Slack searches "carta", "transfer", "applovin", "cursor", "1password", "aws", "unity pro", "svb", "payoff", "wire", "sunset" (all complete); #winddown `2026-02.json` reads (`/16`–`/203` as cited, `/187` table); AppLovin channel history (all months). Gmail `threads/*.json` full scans (88,726 files, complete) for new thread ids, Message-IDs, PERSON_7731, Meet link, "Anysphere", "receipt from Cursor", "AppLovin Corporation -", "2,348.50"; sender-identification reads; Unity invoice INZ02614348 PDF. Snowflake FINANCE_LEDGER rows `/tables/38/rows/686–688`. Trello boards/organization. gcal/contacts PERSON_7731 searches (complete).
- Some searches reached their limits ("Unity Pro", "Carta" in Gmail; SVC sender queries); each was used only for identification, and the decisive checks above used complete narrower queries.
- The workspace filesystem loads files lazily; several helper runs reported "source changed during read" and were rerun until they completed. Results above come from completed runs.
- Reused evidence: revision-13 report sha256 `8f780bb245a9805c49440380df0b517c3933ff940e8e2b2e965578eb6ac5bb0a` (§5 ledger rows, §6 reference table, §7 structure checks, §8 claim rows) for the 57 byte-identical rows and the moved Linear comment texts. Dependencies verified unchanged: statement/comment text, universe manifest, clock and the reference hashes in §1.
- Dependencies for reuse by `/prompt`: Checks A–C above for SQL sha256 `55974419…f2e4`, universe manifest `5e01ac44…f22de450`, clock 2026-02-14T00:00Z, Eval 0 `e034019b…`, WORKFLOW `ee4cd8e1…`, schema `31dcb2b4…`, id_contracts `fc4711ef…`. Any SQL change invalidates them.

### FINAL VERDICT: PASS

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt (then /hardness, /oe, /rubric, since the SQL changed). Optional: drop `links_json` from the `linear_projects` insert (A1).

Evidence limits: Static scope only (no live execution, database compatibility, Agent visibility or difficulty). Schema snapshot unverified (A1 advisory). Some facts exist only in injected records (A3); the base doesn't contradict them. Arthur's Trello board access can't be confirmed from the export (A5).
