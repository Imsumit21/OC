# Injection data-integrity review — `injection-static-v2`

## 1. Scope

| Field | Value |
|---|---|
| Review | Chat review for your attempt (6adfee3f27ce6ca81b457137), `/injection`, static audit mode |
| Review version | `injection-static-v2` (evidence contract `stage-evidence-v1`) |
| Actual review time | 2026-10-28T15:49Z |
| Clock | 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal` (hg4-2026-08-31 v37); manifest `Evals/references/universes/normal/universe_manifest.json` sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Input reviewed | Injection SQL, revision 13 (attachment `01_Universe_Inject (10).sql`, saved as `Evals/task_inputs/01_Universe_Inject.sql`), 92,086 bytes, sha256 `50f6a195de7e1d2842b4966192eb31888ef587acc054191ff310ee39473f09d0` |
| Previous version | Revision 12, SQL sha256 `78c2cad0d18969502b616eb4c22b8343b8ff6fc6d7a7c6bbf995bccc2c85da34` (byte-identical to upload `(9)`), reviewed in report sha256 `c6c9096d18d96728d7a3c66d90db973b865e8216620f47f60ca1578723715cc2` (PASS / COMPLETE) |
| References (re-hashed this run, unchanged since that report) | Eval 0 `e034019b…6f663eff`; WORKFLOW `ee4cd8e1…504fcd5d`; schema snapshot `31dcb2b4…d74c5151`; `id_contracts.json` `fc4711ef…d9ed4682`; known_base_issues `79b20289…e7553a7b` |

## 2. Input / authority issues

- The only input for this stage is the SQL. It is substantive: 140 statements (BEGIN, 134 INSERT, 4 UPDATE, COMMIT) across gdrive, gdocs, gsheets, confluence, slack, trello, gmail, gcal, github and linear. The header comment ("134 INSERT (one row each), 4 UPDATE") matches the parse.
- Header and section comments are authoring notes; none mention tool calls, pass rate or gates.
- `known_base_issues.md` (unchanged) lists no normal-universe conflicts that these rows build on.
- The 66 raw carriage-return bytes inside the Gmail `E'…'` body literals are unchanged from revision 12 (string content, not statement structure).

**Change set from revision 12 (line diff, 10 hunks):** 130 statements are byte-identical; 9 changed; 1 removed.

| Change | Line (INSERT) | Record | What changed |
|---|---|---|---|
| Changed | 1–3 | header comment | INSERT count 135 → 134 |
| Changed | 81, 83 | Gmail thread + message, Layer receipt | Thread id `…/1855299418849853856` → `robert@harmonygames.co/1856114791547562583`; sent 2026-01-25T14:30:05Z → **2026-02-03T14:30:05Z**; "next payment … February 25" → **"March 3, 2026"**; `size_estimate` 1000 → 996. Message-ID unchanged |
| Changed | 110 | `linear.linear_projects` description | Adds "and we cancelled the unity ads in the UA line after october, so they're not in here" |
| Changed | 126 | `cmt_96ae7b3689c1d073a2ff` (ENG-2439, Oliver) | Adds "both games' support buttons now open email instead of helpshift" |
| Changed | 164 | `cmt_e8ae507893bfdb06c8c7` (ENG-2448 Linear, Arthur) | Adds "the p&l stops after the 2024 payment" |
| Changed | 216 | `cmt_2785f039cfee9d256150` (ENG-2463 Calendly, Leonard) | Now "we cancelled calendly in october right after the annual charge, it just runs out" |
| Changed | 220 | `cmt_5d88052b6f8c1b2fc181` (ENG-2464 Google Workspace, Leonard) | Adds "this month's invoice was $298.13" |
| Changed | 238 | `cmt_4179664f58817a32a076` (ENG-2469 DocuSign, Leonard) | Adds "(the p&l missed last april's charge)" |
| Changed + removed | 262 | ENG-2476 (Zapier) comments | Oliver's comment (`cmt_8a420b…`, "zapier is what pipes helpshift tickets into #issuefeed", 11:20:37Z) removed; Leonard's comment now uses id `cmt_8a420b3635db4a36f750` (was `cmt_af582f63b3fef6e310a7`); text and time (16:37:02Z) unchanged |

## 3. Lint (`hg_injection_lint.py`, injection-lint-v1, run on this SQL hash)

Flags: FAIL 0, CHECK 0, INFO 1.

| Flag | Location | Resolution |
|---|---|---|
| INFO `unparsed` (metadata-only media) | line 9, `gdrive.drive_files` `f_4ac7a77383e7317eedcd83` `helpshift_export_2026-02-13.zip` | Accepted, unchanged. A zip package is metadata-only, as in the base; Oliver's comment (line 126) cites it by name only. It becomes a FAIL only if an OE or rubric row needs the zip's contents. |

A clean lint doesn't replace checks A–C; they were done below.

## 4. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; hash, manifest, review version | NEW, done (revision 13 saved from the attachment) |
| Run lint, resolve flags | NEW, done (1 INFO, resolved) |
| Inventory every statement | NEW, done (140/140, §5) |
| Check A: references, collisions, ID contracts | PASS (NEW for the 9 changed rows; REUSED for 130 identical) |
| Check B: structure and supported schema rules | PASS (advisory A1 carried over) |
| Check C: dates, relationships, consistency | PASS (every new claim checked against base sources, §8) |
| Report and verdict | NEW, done |

**Reuse basis (stage-evidence-v1):** the 130 byte-identical statements reuse the revision-12 report's per-record results (report sha256 `c6c9096d…23715cc2`, §5 ledger, §6 reference/collision table, §7 structure checks, §8 amount table rows for unchanged comments), which carried earlier revisions' complete checks. Dependencies verified unchanged: identical statement text, universe manifest `5e01ac44…`, clock and every reference hash in §1. Check C was re-run for every changed claim and for the records they interact with (Layer cancellation, SVB card closure, ENG-2476 issue timestamps).

## 5. Operation ledger (every statement, execution order)

Line = line of the statement's first keyword, counting `\n` only. All 134 INSERT keys are unique within their tables in the SQL. Rows after line 262 sit 2 lines higher than in revision 12 because one comment insert was removed.

| # | Line | Table | Op | Record / target | Latest event time in row | Result | Basis |
|---|---|---|---|---|---|---|---|
| 1 | 5 | `—` | BEGIN | `—` | — | PASS | REUSED |
| 2 | 7 | `gdrive.drive_files` | INSERT | `f_1326e66bcabfda8fd29e4a` | 2026-02-13T16:58:40Z | PASS | REUSED |
| 3 | 9 | `gdrive.drive_files` | INSERT | `f_4ac7a77383e7317eedcd83` | 2026-02-13T15:04:51Z | PASS | REUSED |
| 4 | 11 | `gdrive.drive_files` | INSERT | `f_768cd23a00c4b12fa0e975` | 2026-02-10T18:31:55Z | PASS | REUSED |
| 5 | 14 | `gdocs.docs_documents` | INSERT | `f_1326e66bcabfda8fd29e4a` | 2026-02-13T16:58:40Z | PASS | REUSED |
| 6 | 17 | `gsheets.sheets_spreadsheets` | INSERT | `f_768cd23a00c4b12fa0e975` | 2026-02-10T18:31:55Z | PASS | REUSED |
| 7 | 19 | `gsheets.sheets_sheets` | INSERT | `f_768cd23a00c4b12fa0e975` | — | PASS | REUSED |
| 8 | 22 | `confluence.confluence_pages` | INSERT | `page_ua_vendor_closeout` | 2025-03-18T15:20:00Z | PASS | REUSED |
| 9 | 24 | `confluence.confluence_page_versions` | INSERT | `ver_64b0ed607e093b18a698fb883a584aa6` | 2025-03-18T15:20:00Z | PASS | REUSED |
| 10 | 27 | `slack.slack_messages` | INSERT | `b9ef575bec54b095edb75a0fe83580f5` | 2026-02-13T02:14:36.205117Z | PASS | REUSED |
| 11 | 29 | `slack.slack_messages` | INSERT | `fda86aac9fb55c96ffee4bba3e59cc14` | 2026-02-13T10:02:18.774231Z | PASS | REUSED |
| 12 | 31 | `slack.slack_messages` | INSERT | `9e245e76cbaf7f080e1995ec0c4ec30d` | 2026-02-13T17:21:07.448213Z | PASS | REUSED |
| 13 | 33 | `slack.slack_messages` | UPDATE | `id = '6d8c8d8affd1255b13d8d875f1547e70'` | — | PASS | REUSED |
| 14 | 35 | `trello.trello_cards` | INSERT | `698f48be4ba0affafbf153db` | 2026-02-13T15:52:30Z | PASS | REUSED |
| 15 | 37 | `trello.trello_actions` | INSERT | `698f48be304fbb37e4e3aafa` | 2026-02-13T15:52:30Z | PASS | REUSED |
| 16 | 40 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1856945900224536585` | — | PASS | REUSED |
| 17 | 42 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com>` | 2026-02-12T18:40:12Z | PASS | REUSED |
| 18 | 44 | `gmail.gmail_threads` | INSERT | `leonard.hayes@harmonygames.co/1856945900224877235` | — | PASS | REUSED |
| 19 | 46 | `gmail.gmail_messages` | INSERT | `leonard.hayes@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gma` | 2026-02-12T18:40:12Z | PASS | REUSED |
| 20 | 48 | `gmail.gmail_threads` | INSERT | `arthur.blake@harmonygames.co/1856945900225226172` | — | PASS | REUSED |
| 21 | 50 | `gmail.gmail_messages` | INSERT | `arthur.blake@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmai` | 2026-02-12T18:40:12Z | PASS | REUSED |
| 22 | 52 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1856965916492026238` | — | PASS | REUSED |
| 23 | 54 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>` | 2026-02-12T23:58:21Z | PASS | REUSED |
| 24 | 56 | `gmail.gmail_threads` | INSERT | `leonard.hayes@harmonygames.co/1856965916492755786` | — | PASS | REUSED |
| 25 | 58 | `gmail.gmail_messages` | INSERT | `leonard.hayes@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gma` | 2026-02-12T23:58:21Z | PASS | REUSED |
| 26 | 60 | `gmail.gmail_threads` | INSERT | `arthur.blake@harmonygames.co/1856965916492023943` | — | PASS | REUSED |
| 27 | 62 | `gmail.gmail_messages` | INSERT | `arthur.blake@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmai` | 2026-02-12T23:58:21Z | PASS | REUSED |
| 28 | 64 | `gmail.gmail_threads` | UPDATE | `id = 'robert@harmonygames.co/1856965916492026238'` | — | PASS | REUSED |
| 29 | 65 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com>` | 2026-02-13T18:20:44Z | PASS | REUSED |
| 30 | 67 | `gmail.gmail_threads` | UPDATE | `id = 'leonard.hayes@harmonygames.co/1856965916492755786'` | — | PASS | REUSED |
| 31 | 68 | `gmail.gmail_messages` | INSERT | `leonard.hayes@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gma` | 2026-02-13T18:20:44Z | PASS | REUSED |
| 32 | 70 | `gmail.gmail_threads` | UPDATE | `id = 'arthur.blake@harmonygames.co/1856965916492023943'` | — | PASS | REUSED |
| 33 | 71 | `gmail.gmail_messages` | INSERT | `arthur.blake@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmai` | 2026-02-13T18:20:44Z | PASS | REUSED |
| 34 | 73 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1842712894505970340` | — | PASS | REUSED |
| 35 | 75 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAIoQDHYpNPHXVgnNS8DUmtr__81CmMffz7hcWJv@mail.gmail.com>` | 2025-09-08T16:12:40Z | PASS | REUSED |
| 36 | 77 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1842984194671106077` | — | PASS | REUSED |
| 37 | 79 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAowZ1ukjS1ZxLCL4aRt1VM-c-GnNMTNWVQS47OM@mail.gmail.com>` | 2025-09-11T16:04:52Z | PASS | REUSED |
| 38 | 81 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1856114791547562583` | — | PASS | NEW |
| 39 | 83 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CA4Ce6Oa74xUtCgFI1iGnZMieCxsUh90MhimgGu3@mail.gmail.com>` | 2026-02-03T14:30:05Z | PASS | NEW |
| 40 | 85 | `gmail.gmail_threads` | INSERT | `robert@harmonygames.co/1856859516436705234` | — | PASS | REUSED |
| 41 | 87 | `gmail.gmail_messages` | INSERT | `robert@harmonygames.co/<CAxSGYrkpVAs45dr7lAugwSThN-X-ma7vq_V1xAV@mail.gmail.com>` | 2026-02-11T19:47:10Z | PASS | REUSED |
| 42 | 90 | `gcal.gcal_events` | INSERT | `evt_2ac66383ee72bbb05a0376` | 2026-02-12T22:40:15Z (start/end 2026-03-12 = plan fields) | PASS | REUSED |
| 43 | 92 | `gcal.gcal_events` | INSERT | `evt_f1d245d44ceff5a6e049c0` | 2026-02-12T22:40:15Z (start/end 2026-03-12 = plan fields) | PASS | REUSED |
| 44 | 94 | `gcal.gcal_events` | INSERT | `evt_d1fe12afe85ffbb49bd998` | 2026-02-12T22:40:15Z (start/end 2026-03-12 = plan fields) | PASS | REUSED |
| 45 | 97 | `github.github_pull_requests` | INSERT | `harmonygames-Games/Combo-Fighters#38` | 2026-02-13T09:41:12Z | PASS | REUSED |
| 46 | 99 | `github.github_branches` | INSERT | `harmonygames-Games/Combo-Fighters:oliver/final-build-settings` | — | PASS | REUSED |
| 47 | 101 | `github.github_commits` | INSERT | `c769b476f150a76280886f194b4d2186cfd96ca4` | 2026-02-13T09:23:51Z | PASS | REUSED |
| 48 | 103 | `github.github_pull_request_commits` | INSERT | `harmonygames-Games/Combo-Fighters#38#c_0` | — | PASS | REUSED |
| 49 | 105 | `github.github_pr_comments` | INSERT | `harmonygames-Games/Combo-Fighters#38#c_1` | 2026-02-13T09:41:12Z | PASS | REUSED |
| 50 | 107 | `github.github_timeline_events` | INSERT | `harmonygames-Games/Combo-Fighters#38#ev_1` | 2026-02-13T09:41:12Z | PASS | REUSED |
| 51 | 110 | `linear.linear_projects` | INSERT | `3f0c6a52-ee13-4b1e-68e3-a74bcc33818a` | 2026-02-12T23:24:10Z | PASS | NEW |
| 52 | 112 | `linear.linear_project_teams` | INSERT | `ptm_2183726e36ddf7f8` | 2026-02-12T23:24:10Z | PASS | REUSED |
| 53 | 114 | `linear.linear_project_members` | INSERT | `pmem_dec4e6c3f1315d8a` | 2026-02-12T23:24:10Z | PASS | REUSED |
| 54 | 116 | `linear.linear_project_members` | INSERT | `pmem_5648d2826ae7a30d` | 2026-02-12T23:24:10Z | PASS | REUSED |
| 55 | 118 | `linear.linear_project_members` | INSERT | `pmem_ca4f8a31e35bad07` | 2026-02-12T23:24:10Z | PASS | REUSED |
| 56 | 120 | `linear.linear_issues` | INSERT | `ENG-2438` | 2026-02-13T19:05:12Z | PASS | REUSED |
| 57 | 122 | `linear.linear_comments` | INSERT | `cmt_5da8c3467fc022248fb3` | 2026-02-13T19:05:12Z | PASS | REUSED |
| 58 | 124 | `linear.linear_issues` | INSERT | `ENG-2439` | 2026-02-13T16:12:40Z | PASS | REUSED |
| 59 | 126 | `linear.linear_comments` | INSERT | `cmt_96ae7b3689c1d073a2ff` | 2026-02-13T15:12:18Z | PASS | NEW |
| 60 | 128 | `linear.linear_comments` | INSERT | `cmt_51ff7e6b4cdea7033c08` | 2026-02-13T16:12:40Z | PASS | REUSED |
| 61 | 130 | `linear.linear_issues` | INSERT | `ENG-2440` | 2026-02-12T23:52:03Z | PASS | REUSED |
| 62 | 132 | `linear.linear_comments` | INSERT | `cmt_e8aa0ee7c1bbe08a47c9` | 2026-02-12T23:52:03Z | PASS | REUSED |
| 63 | 134 | `linear.linear_issues` | INSERT | `ENG-2441` | 2026-02-13T20:41:09Z | PASS | REUSED |
| 64 | 136 | `linear.linear_comments` | INSERT | `cmt_37c23c5d30cc6597ebe9` | 2026-02-13T20:41:09Z | PASS | REUSED |
| 65 | 138 | `linear.linear_issues` | INSERT | `ENG-2442` | 2026-02-13T20:43:30Z | PASS | REUSED |
| 66 | 140 | `linear.linear_comments` | INSERT | `cmt_6f994dc8a93d75efb3f8` | 2026-02-13T20:43:30Z | PASS | REUSED |
| 67 | 142 | `linear.linear_issues` | INSERT | `ENG-2443` | 2026-02-12T23:55:41Z | PASS | REUSED |
| 68 | 144 | `linear.linear_comments` | INSERT | `cmt_ec32fbf9ca984b23f7a6` | 2026-02-12T23:55:41Z | PASS | REUSED |
| 69 | 146 | `linear.linear_issues` | INSERT | `ENG-2444` | 2026-02-13T20:45:02Z | PASS | REUSED |
| 70 | 148 | `linear.linear_comments` | INSERT | `cmt_497a61c14b69830f198a` | 2026-02-13T20:45:02Z | PASS | REUSED |
| 71 | 150 | `linear.linear_issues` | INSERT | `ENG-2445` | 2026-02-13T20:45:51Z | PASS | REUSED |
| 72 | 152 | `linear.linear_comments` | INSERT | `cmt_276e0b8a551891ddbdff` | 2026-02-13T20:45:51Z | PASS | REUSED |
| 73 | 154 | `linear.linear_issues` | INSERT | `ENG-2446` | 2026-02-13T20:46:20Z | PASS | REUSED |
| 74 | 156 | `linear.linear_comments` | INSERT | `cmt_a83cc20eced4c1064f0a` | 2026-02-13T20:46:20Z | PASS | REUSED |
| 75 | 158 | `linear.linear_issues` | INSERT | `ENG-2447` | 2026-02-12T23:57:10Z | PASS | REUSED |
| 76 | 160 | `linear.linear_comments` | INSERT | `cmt_8ab16d9d7ac715d1c9a7` | 2026-02-12T23:57:10Z | PASS | REUSED |
| 77 | 162 | `linear.linear_issues` | INSERT | `ENG-2448` | 2026-02-12T23:58:30Z | PASS | REUSED |
| 78 | 164 | `linear.linear_comments` | INSERT | `cmt_e8ae507893bfdb06c8c7` | 2026-02-12T23:58:30Z | PASS | NEW |
| 79 | 166 | `linear.linear_issues` | INSERT | `ENG-2449` | 2026-02-12T23:27:20Z | PASS | REUSED |
| 80 | 168 | `linear.linear_issues` | INSERT | `ENG-2450` | 2026-02-13T20:47:15Z | PASS | REUSED |
| 81 | 170 | `linear.linear_comments` | INSERT | `cmt_e3da997ff7b6575fbea0` | 2026-02-13T20:47:15Z | PASS | REUSED |
| 82 | 172 | `linear.linear_issues` | INSERT | `ENG-2451` | 2026-02-12T23:27:54Z | PASS | REUSED |
| 83 | 174 | `linear.linear_issues` | INSERT | `ENG-2452` | 2026-02-12T23:58:05Z | PASS | REUSED |
| 84 | 176 | `linear.linear_comments` | INSERT | `cmt_ae352002e2f80996f096` | 2026-02-12T23:58:05Z | PASS | REUSED |
| 85 | 178 | `linear.linear_issues` | INSERT | `ENG-2453` | 2026-02-13T16:20:33Z | PASS | REUSED |
| 86 | 180 | `linear.linear_comments` | INSERT | `cmt_276837877e2b3edc466a` | 2026-02-13T16:20:33Z | PASS | REUSED |
| 87 | 182 | `linear.linear_issues` | INSERT | `ENG-2454` | 2026-02-13T16:24:02Z | PASS | REUSED |
| 88 | 184 | `linear.linear_comments` | INSERT | `cmt_5a650ef858f3cd5a0410` | 2026-02-13T16:24:02Z | PASS | REUSED |
| 89 | 186 | `linear.linear_issues` | INSERT | `ENG-2455` | 2026-02-13T19:12:45Z | PASS | REUSED |
| 90 | 188 | `linear.linear_comments` | INSERT | `cmt_62852832c28dc669e459` | 2026-02-13T19:12:45Z | PASS | REUSED |
| 91 | 190 | `linear.linear_issues` | INSERT | `ENG-2456` | 2026-02-13T01:30:22Z | PASS | REUSED |
| 92 | 192 | `linear.linear_comments` | INSERT | `cmt_2b4807a6cf797d1f4886` | 2026-02-13T01:30:22Z | PASS | REUSED |
| 93 | 194 | `linear.linear_issues` | INSERT | `ENG-2457` | 2026-02-13T01:29:55Z | PASS | REUSED |
| 94 | 196 | `linear.linear_comments` | INSERT | `cmt_bbdca23f075e9fca5cb8` | 2026-02-13T01:29:55Z | PASS | REUSED |
| 95 | 198 | `linear.linear_issues` | INSERT | `ENG-2458` | 2026-02-13T01:33:10Z | PASS | REUSED |
| 96 | 200 | `linear.linear_comments` | INSERT | `cmt_6e664bfa3fea62baabb5` | 2026-02-13T01:33:10Z | PASS | REUSED |
| 97 | 202 | `linear.linear_issues` | INSERT | `ENG-2460` | 2026-02-13T16:25:31Z | PASS | REUSED |
| 98 | 204 | `linear.linear_comments` | INSERT | `cmt_7cf5d70170f54a8f925f` | 2026-02-13T16:25:31Z | PASS | REUSED |
| 99 | 206 | `linear.linear_issues` | INSERT | `ENG-2461` | 2026-02-13T16:26:19Z | PASS | REUSED |
| 100 | 208 | `linear.linear_comments` | INSERT | `cmt_2238bd7d0a60d8e4f31c` | 2026-02-13T16:26:19Z | PASS | REUSED |
| 101 | 210 | `linear.linear_issues` | INSERT | `ENG-2462` | 2026-02-13T16:29:47Z | PASS | REUSED |
| 102 | 212 | `linear.linear_comments` | INSERT | `cmt_75b0e4e31a02f9a022bd` | 2026-02-13T16:29:47Z | PASS | REUSED |
| 103 | 214 | `linear.linear_issues` | INSERT | `ENG-2463` | 2026-02-13T16:38:44Z | PASS | REUSED |
| 104 | 216 | `linear.linear_comments` | INSERT | `cmt_2785f039cfee9d256150` | 2026-02-13T16:38:44Z | PASS | NEW |
| 105 | 218 | `linear.linear_issues` | INSERT | `ENG-2464` | 2026-02-13T16:31:05Z | PASS | REUSED |
| 106 | 220 | `linear.linear_comments` | INSERT | `cmt_5d88052b6f8c1b2fc181` | 2026-02-13T16:31:05Z | PASS | NEW |
| 107 | 222 | `linear.linear_issues` | INSERT | `ENG-2465` | 2026-02-13T16:31:48Z | PASS | REUSED |
| 108 | 224 | `linear.linear_comments` | INSERT | `cmt_ec684ef632bdd6b375c3` | 2026-02-13T16:31:48Z | PASS | REUSED |
| 109 | 226 | `linear.linear_issues` | INSERT | `ENG-2466` | 2026-02-12T23:32:09Z | PASS | REUSED |
| 110 | 228 | `linear.linear_issues` | INSERT | `ENG-2467` | 2026-02-13T16:32:02Z | PASS | REUSED |
| 111 | 230 | `linear.linear_comments` | INSERT | `cmt_0bd2c882285911d54ade` | 2026-02-13T16:32:02Z | PASS | REUSED |
| 112 | 232 | `linear.linear_issues` | INSERT | `ENG-2468` | 2026-02-13T16:32:20Z | PASS | REUSED |
| 113 | 234 | `linear.linear_comments` | INSERT | `cmt_c767f5417cafd21d0457` | 2026-02-13T16:32:20Z | PASS | REUSED |
| 114 | 236 | `linear.linear_issues` | INSERT | `ENG-2469` | 2026-02-13T16:33:51Z | PASS | REUSED |
| 115 | 238 | `linear.linear_comments` | INSERT | `cmt_4179664f58817a32a076` | 2026-02-13T16:33:51Z | PASS | NEW |
| 116 | 240 | `linear.linear_issues` | INSERT | `ENG-2470` | 2026-02-12T23:33:17Z | PASS | REUSED |
| 117 | 242 | `linear.linear_issues` | INSERT | `ENG-2471` | 2026-02-12T23:33:34Z | PASS | REUSED |
| 118 | 244 | `linear.linear_issues` | INSERT | `ENG-2472` | 2026-02-13T00:02:44Z | PASS | REUSED |
| 119 | 246 | `linear.linear_comments` | INSERT | `cmt_4ca653c559b182ed6ee6` | 2026-02-13T00:02:44Z | PASS | REUSED |
| 120 | 248 | `linear.linear_issues` | INSERT | `ENG-2473` | 2026-02-13T16:36:10Z | PASS | REUSED |
| 121 | 250 | `linear.linear_comments` | INSERT | `cmt_46c0a9358e1df9a6ded4` | 2026-02-13T16:36:10Z | PASS | REUSED |
| 122 | 252 | `linear.linear_issues` | INSERT | `ENG-2474` | 2026-02-13T00:05:31Z | PASS | REUSED |
| 123 | 254 | `linear.linear_comments` | INSERT | `cmt_a932354ee5e226971ed1` | 2026-02-13T00:05:31Z | PASS | REUSED |
| 124 | 256 | `linear.linear_issues` | INSERT | `ENG-2475` | 2026-02-13T00:06:58Z | PASS | REUSED |
| 125 | 258 | `linear.linear_comments` | INSERT | `cmt_ed6dab8ad539165c22f1` | 2026-02-13T00:06:58Z | PASS | REUSED |
| 126 | 260 | `linear.linear_issues` | INSERT | `ENG-2476` | 2026-02-13T16:37:02Z | PASS | REUSED |
| 127 | 262 | `linear.linear_comments` | INSERT | `cmt_8a420b3635db4a36f750` | 2026-02-13T16:37:02Z | PASS | NEW |
| 128 | 264 | `linear.linear_issues` | INSERT | `ENG-2477` | 2026-02-13T01:28:49Z | PASS | REUSED |
| 129 | 266 | `linear.linear_comments` | INSERT | `cmt_977a0d481cd84d275f08` | 2026-02-13T01:28:49Z | PASS | REUSED |
| 130 | 268 | `linear.linear_issues` | INSERT | `ENG-2478` | 2026-02-13T00:09:12Z | PASS | REUSED |
| 131 | 270 | `linear.linear_comments` | INSERT | `cmt_d10e47fd216f16429b45` | 2026-02-13T00:09:12Z | PASS | REUSED |
| 132 | 272 | `linear.linear_issues` | INSERT | `ENG-2479` | 2026-02-13T01:34:02Z | PASS | REUSED |
| 133 | 274 | `linear.linear_comments` | INSERT | `cmt_4a019a675b55484b05ec` | 2026-02-13T01:34:02Z | PASS | REUSED |
| 134 | 276 | `linear.linear_issues` | INSERT | `ENG-2480` | 2026-02-13T16:38:44Z | PASS | REUSED |
| 135 | 278 | `linear.linear_comments` | INSERT | `cmt_e3b5ee0557dca1cb519c` | 2026-02-13T16:38:44Z | PASS | REUSED |
| 136 | 280 | `linear.linear_issues` | INSERT | `ENG-2481` | 2026-02-13T20:50:40Z | PASS | REUSED |
| 137 | 282 | `linear.linear_comments` | INSERT | `cmt_5f33dc45f96bbae1e85d` | 2026-02-13T20:50:40Z | PASS | REUSED |
| 138 | 284 | `linear.linear_issues` | INSERT | `ENG-2482` | 2026-02-12T23:36:41Z | PASS | REUSED |
| 139 | 286 | `linear.linear_issues` | INSERT | `ENG-2483` | 2026-02-12T23:36:58Z | PASS | REUSED |
| 140 | 288 | `—` | COMMIT | `—` | — | PASS | REUSED |

## 6. Check A — Records, references and IDs: **PASS**

| Item | Evidence | Result |
|---|---|---|
| New Gmail thread `robert@harmonygames.co/1856114791547562583` | Full-text Gmail scan (`threads/*.json`, 88,726 files, all mailboxes): 0 matches, `scan_complete: true`. Appears once in the SQL (thread row + its message's `thread_id`). The thread number decodes to 2026-02-03T14:30:05Z, the message's send time. The old thread id `…/1855299418849853856` no longer appears anywhere in the SQL. | PASS |
| Reused Message-ID `<CA4Ce6Oa74xUtCgFI1iGnZMieCxsUh90MhimgGu3@mail.gmail.com>` | Unchanged string, inserted once (line 83); revision-12 complete scan showed it absent from base Gmail. | PASS (REUSED) |
| Comment id `cmt_8a420b3635db4a36f750`, now Leonard's | `lookup` on linear `data.json` `/comments` (verified id index, `scan_complete: true`, 0 matches) and full-text scan of every linear `*.json` for the id and its hex part: 0 matches. In the SQL it is now inserted once (Oliver's row with the same id is gone), so no duplicate key. | PASS |
| Removed rows leave no dangling references | `cmt_af582f63b3fef6e310a7`, Oliver's Zapier comment and "#issuefeed" no longer appear in the SQL; nothing referenced them. | PASS |
| Authors on changed rows | Unchanged ids, resolved in revision 12 against linear `/users` (complete): `usr_63fffeb4fab5233e` = leonard.hayes, `usr_cc3e90160f490686` = arthur.blake, `usr_bdf01b53c6a92c5e` = oliver.brooks. | PASS (REUSED) |
| Parents | ENG-2476 (line 260) precedes its comment (262); every other changed comment's issue precedes it, unchanged. | PASS |
| ID contracts / Drive readability / one account per person | Lint clean; new Gmail thread `history_id` NULL. No new accounts or Drive files. | PASS |

## 7. Check B — SQL structure and supported schema rules: **PASS**

- All 140 statements parse (lint: no `missing_required`, `json_shape`, `generated_column` or `text_time_format` flags). Changed rows keep their column lists; each VALUES tuple has the same count.
- Gmail line 83: `internal_date` 1770129005000 = 2026-02-03T14:30:05Z = `date` = the `Date` header "Tue, 03 Feb 2026 14:30:05 +0000" (a Tuesday). JSON list columns keep the base shape. No `body_text_fts` set.
- Linear changed rows: every `*_at` value is `YYYY-MM-DDTHH:MM:SSZ`; no offsets, milliseconds or casts. Apostrophes are doubled (`games''`, `month''s`, `april''s`).
- **A1 (advisory, carried over):** `linear.linear_projects.links_json` (line 110) isn't in the provisional snapshot. If the live table lacks it, the whole transaction rolls back. Safest: drop `links_json` and its `'[]'` value from that insert.

## 8. Check C — Dates, relationships and consistency: **PASS**

**Clock and chronology:** latest event timestamp is still 2026-02-13T20:50:40Z (ENG-2481 comment); the only later values are the gcal plan fields (2026-03-12). ENG-2476's `updated_at` (16:37:02Z) equals its only remaining comment; created 2026-02-12T23:34:59Z precedes it. The other changed comments kept their times, which matched their issues in revision 12.

**New claims checked against base sources:**

| Claim (line) | Base evidence | Result |
|---|---|---|
| Layer receipt: "Layer Pro (monthly) — $49.00 … next payment is on March 3, 2026", sent Feb 3 (81, 83) | #winddown `messages/C0ADGSZKR3R/2026-02.json` `/64`, Robert, 2026-02-11T19:23Z: "I just canceled layer"; `/187` checklist "[x] layer". Leonard's unchanged ENG-2473 comment: "cancelled it in the app on the 11th". A monthly charge on Feb 3 with the next one on Mar 3 is consistent with a Feb 11 cancel running to Mar 3, and with the SVB card terms (Trello line 35: "Whatever we're cancelling can stay on the card until it ends"). The only base Layer receipt (leonard@ mailbox, "layer Data LTD", $59, June 19, 2023) is 2½ years older. Arthur's injected Subscriptions sheet (Layer 39) is marked as replaced by the project description. No Layer row in the costs tab. | No contradiction |
| "we cancelled the unity ads in the UA line after october" (110) | Gmail "Receipt from Unity Ads" (subject search, complete, 28 threads): last one 2025-10-15. Unity Technologies SF monthly invoices (subject search, complete): last is CINV_00022209, 2025-11-10, "Attached is your 10 2025 monthly invoice"; PDF (`robert@…/1848419141089023383/…/att_0001.pdf`) customer message "uAds 1 - 31/10/2025", Zombie Match. No later Unity Ads invoice or receipt. Costs-tab UA line continues (Nov 2025 4,806.02; Dec 610; Jan 2026 5,000), which fits other networks; the sentence doesn't say the line was only Unity. Jan–Feb 2026 Slack mentions of "Unity Ads" are about in-game ad mediation (revenue) in Combo Fighter, plus one DM (`D07H86MV4DN/2026-02.json` `/6`) about paying for Unity Ads "out of my own pocket", not a company account. | Supported |
| "both games' support buttons now open email instead of helpshift" (126, Feb 13) | #winddown `/57`, Robert, 2026-02-11T05:58Z, tagging Arthur: "We gotta move domino delights and zombie match off Helpshift before Feb 28th. We can just open up the email app and let players send email to …". No base record after Feb 11 says the switch is still pending (Slack "email app" search in Feb 2026, complete: only `/57`). | Supported (plan in base; completion stated only in the comment) |
| "the p&l stops after the 2024 payment" (164) | Costs tab (gsheets `data.json` `/sheets_spreadsheets/141/sheets/2`) Linear row: 2,403 in Aug 2024, −288 Sep 2024, then 0 every month through Jan 2026. Base receipt for the Aug 2025 payment ($1,832.65) exists (revision-12 evidence). | Supported |
| Calendly "cancelled … in october right after the annual charge, it just runs out" (216) | Gmail leonard.hayes 2025-10-13 receipt PDF: "Essentials Yearly", $96.00, billing period Oct 13, 2025 – Oct 13, 2026 (same plan Oct 2023). Costs tab: 96 in Oct 2023, Oct 2024, Oct 2025 only. No Calendly cancellation or renewal email contradicts (subject search, complete, 11 threads). | Supported |
| Google Workspace "this month's invoice was $298.13" (220) | Gmail 2026-02-02 "Google Workspace: Your invoice is available" (robert `00016704.json`, leonard.hayes `…_1856033699288555295`, same invoice): PDF invoice 5473295269, invoice date Jan 31, 2026, Jan 1–31 usage, **$298.13**. | Supported |
| DocuSign "(the p&l missed last april's charge)" (238) | Costs tab DocuSign row: only 300 in Apr 2024, nothing in Apr 2025. Gmail 2025-03-19 renewal notice: Standard – Annual, renewal 04/20/2025, $300 (revision-12 evidence). | Supported |

**Grader-facing text:** none in any changed or injected record.

### Advisories (not failing)

- **A1 — `links_json`** (Check B above).
- **A2 — Base P&L gaps (now stated by your comments):** the costs tab omits the Aug 2025 Linear payment and the Apr 2025 DocuSign renewal that base emails confirm. Your ENG-2448 and ENG-2469 comments now say so, which matches the base. Keep rubric rows and OEs off any claim that needs those P&L cells to be right.
- **A3 — Facts carried only by injected comments:** Slack $87.22, Google Cloud $4.97, Zapier $73.50, 1Password $19.95, Cursor $40, Deel $300 (unchanged), plus the new "support buttons now open email" (base has only the Feb 11 plan). None conflicts with the base.
- **A4 — Layer amount:** the receipt ($49/month) and Arthur's superseded sheet (39) differ on purpose; only the receipt is current. /prompt and /rubric should treat the receipt as the source.

## 9. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | New Gmail thread id absent from base Gmail (complete scan) and used once; `cmt_8a420b…` absent from base Linear (complete) and now inserted once; removed rows leave no dangling references; authors and parents resolve. |
| B — SQL structure and supported schema rules | PASS | All statements parse; changed Gmail row's dates agree; Linear text dates in base format. Provisional MISMATCH on `linear_projects.links_json` (A1, advisory). |
| C — Dates, relationships and consistency | PASS | All event times ≤ clock (plan fields excepted). Every new claim is supported by base receipts, invoices, the costs tab or #winddown, or is uncontradicted (A3). |

## 10. Next action and downstream

1. Optional: A1 (drop `links_json` from the `linear_projects` insert at line 110).
2. Because the SQL changed, every earlier pass that read it is outdated: run `/prompt`, `/hardness`, `/oe`, `/rubric` again, in that order.

## 11. Evidence limits and provenance

- Static scope only. No live execution, database compatibility, search ranking, Agent visibility or difficulty assessment. The schema snapshot is unverified, so mismatches are advisory.
- Sources read this run (all `Universe_Normal`): Gmail `threads/*.json` full scans (88,726 files): new thread id (complete, 0); subject searches complete for "Google Workspace" (80), "Calendly" (11), "Unity Technologies SF" (29), "Receipt from Unity" (28), "Receipt from Layer" (1 body hit, 2023); selected reads: Google Workspace Feb 2026 invoice email + PDF (two mailboxes), Calendly 2025 and 2023 receipt PDFs, Unity CINV_00022209 and CINV_00019296 emails and Robert's CINV_00022209 PDF. gsheets `data.json` `/sheets_spreadsheets/141/sheets/2` (HG Costs, 75×44, complete; columns mapped by the year suffix in each header date, confirmed by Calendly's October charges). Slack `messages/*/*.json` searches (complete where noted: "unity ads" 57, "uads" 34, "support button" 8, case-sensitive "Layer" 85; Oct 2025–Feb 2026 "calendly"/"helpshift" complete); #winddown `/57`, `/64` reads; `users.json` (EMPLOYEE_0025 = Arthur Blake). Linear `data.json` `/comments` id lookup and full-text id scans (complete).
- Some broad text queries ("layer", "calendly", "helpshift" across all Slack history; "Layer Pro", "Google Workspace" body text in Gmail) hit their limits; each was replaced by the complete narrower query listed above.
- Reused evidence: revision-12 report sha256 `c6c9096d18d96728d7a3c66d90db973b865e8216620f47f60ca1578723715cc2` (§5 ledger rows, §6 reference/collision table, §7 structure checks, §8 amount rows for unchanged comments) for the 130 byte-identical statements. Dependencies verified unchanged: statement text, universe manifest, clock and the reference hashes in §1.
- Dependencies for reuse by `/prompt`: Checks A–C above for SQL sha256 `50f6a195…73f09d0`, universe manifest `5e01ac44…f22de450`, clock 2026-02-14T00:00Z, Eval 0 `e034019b…`, WORKFLOW `ee4cd8e1…`, schema `31dcb2b4…`, id_contracts `fc4711ef…`. Any SQL change invalidates them.

### FINAL VERDICT: PASS

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt (then /hardness, /oe, /rubric, since the SQL changed). Optional: drop `links_json` from the `linear_projects` insert (A1).

Evidence limits: Static scope only (no live execution, database compatibility, Agent visibility or difficulty). Schema snapshot unverified (A1 advisory). Some facts exist only in the injected comments (A3); the base doesn't contradict them.
