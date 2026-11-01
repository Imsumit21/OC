# Injection data-integrity review — `injection-static-v2`

## 1. Scope

| Field | Value |
|---|---|
| Review | Chat review for your attempt (6adfee3f27ce6ca81b457137), `/injection`, static audit mode |
| Review version | `injection-static-v2` (evidence contract `stage-evidence-v1`) |
| Actual review time | 2026-10-28T10:34Z |
| Clock | 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal` (hg4-2026-08-31 v37); manifest `Evals/references/universes/normal/universe_manifest.json` sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Input reviewed | Injection SQL, revision 8 (attachment `01_Universe_Inject (5).sql`, saved as `Evals/task_inputs/01_Universe_Inject.sql`), 99,262 bytes, sha256 `57c535c2e70aac7a2af8280625938b1418b68b86fbbee0371145efa3c193faef` |
| Previous version | Revision 7, sha256 `b03b3b07…69984b`, reviewed in report sha256 `960228048110de283bd9257cc9a992b9ac57d23807cb14c050947b9992fee397` (FAIL: F1 Dailybot, F2 UA Assets) |
| References (all re-hashed, unchanged since that report) | Eval 0 `e034019b…6f663eff`; WORKFLOW `ee4cd8e1…504fcd5d`; schema snapshot `31dcb2b4…d74c5151`; schema README `9e320787…9a76eb42`; `id_contracts.json` `fc4711ef…d9ed4682`; ENVIRONMENT `4ffb2b5f…a5d5e165`; SEARCH `cab83c61…c9d3a45c`; roster `3f217451…b3c84575`; acl `e9bca2b3…04468c9f`; known_base_issues `79b20289…e7553a7b` |

## 2. Input / authority issues

- The only input for this stage is the SQL. It is substantive: 150 statements (BEGIN, 144 INSERT, 4 UPDATE, COMMIT) across gdrive, gdocs, gsheets, confluence, slack, trello, gmail, gcal, github and linear.
- Header comments are authoring notes; none mention tool calls, pass rate or gates.
- `known_base_issues.md` lists no normal-universe conflicts. No Snowflake/Confluence base conflict was found for the changed rows (the Snowflake ledger has no vendor-level Kling, Dailybot, Linear or UA-asset entries; see §8).

**Change set from revision 7 (line diff):** 145 statements are byte-identical. 5 statements changed, none added or removed. All five are `linear.linear_comments` inserts, and only the `body` text changed (ids, authors, issue ids and timestamps are identical):

| SQL line | Comment / issue | Revision 7 body | Revision 8 body |
|---|---|---|---|
| 168 | `cmt_276e0b8a551891ddbdff` / ENG-2445 Kling | "dropped after the september trial" | "dropped kling after september" |
| 180 | `cmt_e8ae507893bfdb06c8c7` / ENG-2448 Linear | "…the p&l only ever caught the 2024 payment" | "…the p&l stops after the 2024 payment" |
| 192 | `cmt_ae352002e2f80996f096` / ENG-2452 Dailybot | "dailybot was a 2023 thing, cancelled after the first month" | "we stopped paying for dailybot in early 2024, it's sat on the free plan since" |
| 204 | `cmt_62852832c28dc669e459` / ENG-2455 AWS | "…the p&l line for it never got filled in" | "…the p&l line for it was never kept up" |
| 302 | `cmt_5f33dc45f96bbae1e85d` / ENG-2481 UA Assets | "…that line was a placeholder and we never spent on it" | "…that line was one-off creative buys for campaigns, the last one was last april" |

## 3. Lint (`hg_injection_lint.py`, injection-lint-v1, run on this SQL hash)

Flags: FAIL 0, CHECK 0, INFO 1.

| Flag | Record | Resolution |
|---|---|---|
| INFO `unparsed` (metadata-only media) | line 9, `gdrive.drive_files` `f_4ac7a77383e7317eedcd83` `helpshift_export_2026-02-13.zip` | Accepted, unchanged. A zip package is metadata-only, as in the base. It becomes a FAIL only if an OE or rubric row needs the zip's contents. |

A clean lint doesn't replace checks A–C. They were run below and found one defect the lint can't detect.

## 4. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; hash, manifest, review version | NEW, done (revision 8 saved from the attachment) |
| Run lint, resolve flags | NEW, done (1 INFO, resolved) |
| Inventory every statement | NEW, done (150/150, §5) |
| Check A: references, collisions, ID contracts | PASS (REUSED; the 5 changed rows changed only body text) |
| Check B: structure and supported schema rules | PASS (NEW for the 5 changed rows; advisory A1 carried over) |
| Check C: dates, relationships, consistency | **FAIL** (F1) |
| Report and verdict | NEW, done |

**Reuse basis (stage-evidence-v1):** the 145 byte-identical statements reuse the revision-7 report's per-record results (report sha256 `96022804…92fee397`, §5 ledger rows, §6 reference/collision table, §7 structure checks and §8 base facts for unchanged rows), which in turn carried revision-5 and revision-4 checks for rows unchanged since then. Every dependency is unchanged: identical statement text, the same universe manifest `5e01ac44…`, the same clock, and the same Eval/schema/id_contracts/roster/acl/known-issues hashes (§1, re-hashed this run). For the five changed rows, the ids, authors, parents and timestamps are byte-identical, so their Check A results are reused; every claim in their new body text was checked again from source in this run.

## 5. Operation ledger (every statement, execution order)

"Line" is the physical line where the statement starts in the saved SQL. "Latest event time" is the last ISO event timestamp in the row. The gcal start/end plan fields (2026-03-12) are excluded. "Verification" is NEW (re-checked this run) or REUSED (byte-identical to revision 7, checked previously).

| # | Line | Table | Op | Record / target | Latest event time | Result | Verification |
|---|---|---|---|---|---|---|---|
| 1 | 5 | — | BEGIN | — |  | PASS | — |
| 2 | 7 | gdrive.drive_files | INSERT | f_1326e66bcabfda8fd29e4a | 2026-02-13T16:58:40Z | PASS | REUSED |
| 3 | 9 | gdrive.drive_files | INSERT | f_4ac7a77383e7317eedcd83 | 2026-02-13T15:04:51Z | PASS (lint INFO: metadata-only zip) | REUSED |
| 4 | 11 | gdrive.drive_files | INSERT | f_768cd23a00c4b12fa0e975 | 2026-02-10T18:31:55Z | PASS | REUSED |
| 5 | 14 | gdocs.docs_documents | INSERT | f_1326e66bcabfda8fd29e4a | 2026-02-13T16:58:40Z | PASS | REUSED |
| 6 | 17 | gsheets.sheets_spreadsheets | INSERT | f_768cd23a00c4b12fa0e975 | 2026-02-10T18:31:55Z | PASS | REUSED |
| 7 | 19 | gsheets.sheets_sheets | INSERT | f_768cd23a00c4b12fa0e975 |  | PASS | REUSED |
| 8 | 22 | confluence.confluence_pages | INSERT | page_ua_vendor_closeout | 2025-03-18T15:20:00Z | PASS | REUSED |
| 9 | 24 | confluence.confluence_page_versions | INSERT | ver_64b0ed607e093b18a698fb883a584aa6 | 2025-03-18T15:20:00Z | PASS | REUSED |
| 10 | 26 | confluence.confluence_pages | INSERT | page_support_after_helpshift | 2026-02-12T20:05:14Z | PASS | REUSED |
| 11 | 28 | confluence.confluence_page_versions | INSERT | ver_16458585128da06d66a64fa5055bea00 | 2026-02-12T20:05:14Z | PASS | REUSED |
| 12 | 30 | confluence.confluence_comments | INSERT | comment_support_after_helpshift_c1 | 2026-02-13T15:10:27Z | PASS | REUSED |
| 13 | 33 | slack.slack_messages | INSERT | b9ef575bec54b095edb75a0fe83580f5 | 2026-02-13T02:14:36.205117Z | PASS | REUSED |
| 14 | 35 | slack.slack_messages | INSERT | fda86aac9fb55c96ffee4bba3e59cc14 | 2026-02-13T10:02:18.774231Z | PASS | REUSED |
| 15 | 37 | slack.slack_messages | INSERT | 9e245e76cbaf7f080e1995ec0c4ec30d | 2026-02-13T17:21:07.448213Z | PASS | REUSED |
| 16 | 39 | slack.slack_messages | UPDATE | id = '6d8c8d8affd1255b13d8d875f1547e70' |  | PASS | REUSED |
| 17 | 41 | trello.trello_cards | INSERT | 643efb2ab65c5e952575dde5 | 2023-04-18T20:18:50Z | PASS | REUSED |
| 18 | 43 | trello.trello_actions | INSERT | 643efb2a2768759bdebceec4 | 2023-04-18T20:18:50Z | PASS | REUSED |
| 19 | 45 | trello.trello_cards | INSERT | 698f48be4ba0affafbf153db | 2026-02-13T15:52:30Z | PASS | REUSED |
| 20 | 47 | trello.trello_actions | INSERT | 698f48be304fbb37e4e3aafa | 2026-02-13T15:52:30Z | PASS | REUSED |
| 21 | 50 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856945900224536585 |  | PASS | REUSED |
| 22 | 52 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com> | 2026-02-12T18:40:12Z | PASS | REUSED |
| 23 | 54 | gmail.gmail_threads | INSERT | leonard.hayes@harmonygames.co/1856945900224877235 |  | PASS | REUSED |
| 24 | 56 | gmail.gmail_messages | INSERT | leonard.hayes@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com> | 2026-02-12T18:40:12Z | PASS | REUSED |
| 25 | 58 | gmail.gmail_threads | INSERT | arthur.blake@harmonygames.co/1856945900225226172 |  | PASS | REUSED |
| 26 | 60 | gmail.gmail_messages | INSERT | arthur.blake@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com> | 2026-02-12T18:40:12Z | PASS | REUSED |
| 27 | 62 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856965916492026238 |  | PASS | REUSED |
| 28 | 64 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | 2026-02-12T23:58:21Z | PASS | REUSED |
| 29 | 66 | gmail.gmail_threads | INSERT | leonard.hayes@harmonygames.co/1856965916492755786 |  | PASS | REUSED |
| 30 | 68 | gmail.gmail_messages | INSERT | leonard.hayes@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | 2026-02-12T23:58:21Z | PASS | REUSED |
| 31 | 70 | gmail.gmail_threads | INSERT | arthur.blake@harmonygames.co/1856965916492023943 |  | PASS | REUSED |
| 32 | 72 | gmail.gmail_messages | INSERT | arthur.blake@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | 2026-02-12T23:58:21Z | PASS | REUSED |
| 33 | 74 | gmail.gmail_threads | UPDATE | id = 'robert@harmonygames.co/1856965916492026238' |  | PASS | REUSED |
| 34 | 75 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> | 2026-02-13T18:20:44Z | PASS | REUSED |
| 35 | 77 | gmail.gmail_threads | UPDATE | id = 'leonard.hayes@harmonygames.co/1856965916492755786' |  | PASS | REUSED |
| 36 | 78 | gmail.gmail_messages | INSERT | leonard.hayes@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> | 2026-02-13T18:20:44Z | PASS | REUSED |
| 37 | 80 | gmail.gmail_threads | UPDATE | id = 'arthur.blake@harmonygames.co/1856965916492023943' |  | PASS | REUSED |
| 38 | 81 | gmail.gmail_messages | INSERT | arthur.blake@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> | 2026-02-13T18:20:44Z | PASS | REUSED |
| 39 | 83 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1842984194671106077 |  | PASS | REUSED |
| 40 | 85 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAowZ1ukjS1ZxLCL4aRt1VM-c-GnNMTNWVQS47OM@mail.gmail.com> | 2025-09-11T16:04:52Z | PASS | REUSED |
| 41 | 87 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1855299418849853856 |  | PASS | REUSED |
| 42 | 89 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CA4Ce6Oa74xUtCgFI1iGnZMieCxsUh90MhimgGu3@mail.gmail.com> | 2026-01-25T14:30:05Z | PASS | REUSED |
| 43 | 91 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1855912858878482138 |  | PASS | REUSED |
| 44 | 93 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAL7W0WN5jkixON6h71KIRU6DcLoQyjXVIYONWEZ@mail.gmail.com> | 2026-02-01T09:00:27Z | PASS | REUSED |
| 45 | 95 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856653066502254886 |  | PASS | REUSED |
| 46 | 97 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAIoQDHYpNPHXVgnNS8DUmtr__81CmMffz7hcWJv@mail.gmail.com> | 2026-02-09T13:05:44Z | PASS | REUSED |
| 47 | 99 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856761009013149089 |  | PASS | REUSED |
| 48 | 101 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAAV70N_MnwWfJSNuqS_HKOnLheApwCzJGSFQi8q@mail.gmail.com> | 2026-02-10T17:41:26Z | PASS | REUSED |
| 49 | 103 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856859516436705234 |  | PASS | REUSED |
| 50 | 105 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAxSGYrkpVAs45dr7lAugwSThN-X-ma7vq_V1xAV@mail.gmail.com> | 2026-02-11T19:47:10Z | PASS | REUSED |
| 51 | 108 | gcal.gcal_events | INSERT | evt_2ac66383ee72bbb05a0376 | 2026-02-12T22:40:15Z | PASS | REUSED |
| 52 | 110 | gcal.gcal_events | INSERT | evt_f1d245d44ceff5a6e049c0 | 2026-02-12T22:40:15Z | PASS | REUSED |
| 53 | 112 | gcal.gcal_events | INSERT | evt_d1fe12afe85ffbb49bd998 | 2026-02-12T22:40:15Z | PASS | REUSED |
| 54 | 115 | github.github_pull_requests | INSERT | harmonygames-Games/Combo-Fighters#38 | 2026-02-13T09:41:12Z | PASS | REUSED |
| 55 | 117 | github.github_branches | INSERT | harmonygames-Games/Combo-Fighters:oliver/final-build-settings |  | PASS | REUSED |
| 56 | 119 | github.github_commits | INSERT | c769b476f150a76280886f194b4d2186cfd96ca4 | 2026-02-13T09:23:51Z | PASS | REUSED |
| 57 | 121 | github.github_pull_request_commits | INSERT | harmonygames-Games/Combo-Fighters#38#c_0 |  | PASS | REUSED |
| 58 | 123 | github.github_pr_comments | INSERT | harmonygames-Games/Combo-Fighters#38#c_1 | 2026-02-13T09:41:12Z | PASS | REUSED |
| 59 | 125 | github.github_timeline_events | INSERT | harmonygames-Games/Combo-Fighters#38#ev_1 | 2026-02-13T09:41:12Z | PASS | REUSED |
| 60 | 128 | linear.linear_projects | INSERT | 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a | 2026-02-12T23:24:10Z | PASS | REUSED |
| 61 | 130 | linear.linear_project_teams | INSERT | ptm_2183726e36ddf7f8 | 2026-02-12T23:24:10Z | PASS | REUSED |
| 62 | 132 | linear.linear_project_members | INSERT | pmem_dec4e6c3f1315d8a | 2026-02-12T23:24:10Z | PASS | REUSED |
| 63 | 134 | linear.linear_project_members | INSERT | pmem_5648d2826ae7a30d | 2026-02-12T23:24:10Z | PASS | REUSED |
| 64 | 136 | linear.linear_project_members | INSERT | pmem_ca4f8a31e35bad07 | 2026-02-12T23:24:10Z | PASS | REUSED |
| 65 | 138 | linear.linear_issues | INSERT | ENG-2438 | 2026-02-13T19:05:12Z | PASS | REUSED |
| 66 | 140 | linear.linear_comments | INSERT | cmt_5da8c3467fc022248fb3 | 2026-02-13T19:05:12Z | PASS | REUSED |
| 67 | 142 | linear.linear_issues | INSERT | ENG-2439 | 2026-02-13T16:12:40Z | PASS | REUSED |
| 68 | 144 | linear.linear_comments | INSERT | cmt_96ae7b3689c1d073a2ff | 2026-02-13T16:12:40Z | PASS | REUSED |
| 69 | 146 | linear.linear_issues | INSERT | ENG-2440 | 2026-02-12T23:52:03Z | PASS | REUSED |
| 70 | 148 | linear.linear_comments | INSERT | cmt_e8aa0ee7c1bbe08a47c9 | 2026-02-12T23:52:03Z | PASS | REUSED |
| 71 | 150 | linear.linear_issues | INSERT | ENG-2441 | 2026-02-13T20:41:09Z | PASS | REUSED |
| 72 | 152 | linear.linear_comments | INSERT | cmt_37c23c5d30cc6597ebe9 | 2026-02-13T20:41:09Z | PASS | REUSED |
| 73 | 154 | linear.linear_issues | INSERT | ENG-2442 | 2026-02-13T20:43:30Z | PASS | REUSED |
| 74 | 156 | linear.linear_comments | INSERT | cmt_6f994dc8a93d75efb3f8 | 2026-02-13T20:43:30Z | PASS | REUSED |
| 75 | 158 | linear.linear_issues | INSERT | ENG-2443 | 2026-02-12T23:55:41Z | PASS | REUSED |
| 76 | 160 | linear.linear_comments | INSERT | cmt_ec32fbf9ca984b23f7a6 | 2026-02-12T23:55:41Z | PASS | REUSED |
| 77 | 162 | linear.linear_issues | INSERT | ENG-2444 | 2026-02-13T20:45:02Z | PASS | REUSED |
| 78 | 164 | linear.linear_comments | INSERT | cmt_497a61c14b69830f198a | 2026-02-13T20:45:02Z | PASS | REUSED |
| 79 | 166 | linear.linear_issues | INSERT | ENG-2445 | 2026-02-13T20:45:51Z | PASS | REUSED |
| 80 | 168 | linear.linear_comments | INSERT | cmt_276e0b8a551891ddbdff | 2026-02-13T20:45:51Z | PASS | NEW (changed text) |
| 81 | 170 | linear.linear_issues | INSERT | ENG-2446 | 2026-02-13T20:46:20Z | PASS | REUSED |
| 82 | 172 | linear.linear_comments | INSERT | cmt_a83cc20eced4c1064f0a | 2026-02-13T20:46:20Z | PASS | REUSED |
| 83 | 174 | linear.linear_issues | INSERT | ENG-2447 | 2026-02-12T23:57:10Z | PASS | REUSED |
| 84 | 176 | linear.linear_comments | INSERT | cmt_8ab16d9d7ac715d1c9a7 | 2026-02-12T23:57:10Z | PASS | REUSED |
| 85 | 178 | linear.linear_issues | INSERT | ENG-2448 | 2026-02-12T23:58:30Z | PASS | REUSED |
| 86 | 180 | linear.linear_comments | INSERT | cmt_e8ae507893bfdb06c8c7 | 2026-02-12T23:58:30Z | PASS | NEW (changed text) |
| 87 | 182 | linear.linear_issues | INSERT | ENG-2449 | 2026-02-12T23:27:20Z | PASS | REUSED |
| 88 | 184 | linear.linear_issues | INSERT | ENG-2450 | 2026-02-13T20:47:15Z | PASS | REUSED |
| 89 | 186 | linear.linear_comments | INSERT | cmt_e3da997ff7b6575fbea0 | 2026-02-13T20:47:15Z | PASS | REUSED |
| 90 | 188 | linear.linear_issues | INSERT | ENG-2451 | 2026-02-12T23:27:54Z | PASS | REUSED |
| 91 | 190 | linear.linear_issues | INSERT | ENG-2452 | 2026-02-12T23:58:05Z | PASS | REUSED |
| 92 | 192 | linear.linear_comments | INSERT | cmt_ae352002e2f80996f096 | 2026-02-12T23:58:05Z | **FAIL (F1)** | NEW (changed text) |
| 93 | 194 | linear.linear_issues | INSERT | ENG-2453 | 2026-02-13T16:20:33Z | PASS | REUSED |
| 94 | 196 | linear.linear_comments | INSERT | cmt_276837877e2b3edc466a | 2026-02-13T16:20:33Z | PASS | REUSED |
| 95 | 198 | linear.linear_issues | INSERT | ENG-2454 | 2026-02-13T16:24:02Z | PASS | REUSED |
| 96 | 200 | linear.linear_comments | INSERT | cmt_5a650ef858f3cd5a0410 | 2026-02-13T16:24:02Z | PASS | REUSED |
| 97 | 202 | linear.linear_issues | INSERT | ENG-2455 | 2026-02-13T19:12:45Z | PASS | REUSED |
| 98 | 204 | linear.linear_comments | INSERT | cmt_62852832c28dc669e459 | 2026-02-13T19:12:45Z | PASS | NEW (changed text) |
| 99 | 206 | linear.linear_issues | INSERT | ENG-2456 | 2026-02-13T01:30:22Z | PASS | REUSED |
| 100 | 208 | linear.linear_comments | INSERT | cmt_2b4807a6cf797d1f4886 | 2026-02-13T01:30:22Z | PASS | REUSED |
| 101 | 210 | linear.linear_issues | INSERT | ENG-2457 | 2026-02-13T01:29:55Z | PASS | REUSED |
| 102 | 212 | linear.linear_comments | INSERT | cmt_bbdca23f075e9fca5cb8 | 2026-02-13T01:29:55Z | PASS | REUSED |
| 103 | 214 | linear.linear_issues | INSERT | ENG-2458 | 2026-02-13T01:33:10Z | PASS | REUSED |
| 104 | 216 | linear.linear_comments | INSERT | cmt_6e664bfa3fea62baabb5 | 2026-02-13T01:33:10Z | PASS | REUSED |
| 105 | 218 | linear.linear_issues | INSERT | ENG-2459 | 2026-02-13T19:15:08Z | PASS | REUSED |
| 106 | 220 | linear.linear_comments | INSERT | cmt_8f765d1313e9b01a8c22 | 2026-02-13T19:15:08Z | PASS | REUSED |
| 107 | 222 | linear.linear_issues | INSERT | ENG-2460 | 2026-02-13T16:25:31Z | PASS | REUSED |
| 108 | 224 | linear.linear_comments | INSERT | cmt_7cf5d70170f54a8f925f | 2026-02-13T16:25:31Z | PASS | REUSED |
| 109 | 226 | linear.linear_issues | INSERT | ENG-2461 | 2026-02-13T16:26:19Z | PASS | REUSED |
| 110 | 228 | linear.linear_comments | INSERT | cmt_2238bd7d0a60d8e4f31c | 2026-02-13T16:26:19Z | PASS | REUSED |
| 111 | 230 | linear.linear_issues | INSERT | ENG-2462 | 2026-02-13T16:29:47Z | PASS | REUSED |
| 112 | 232 | linear.linear_comments | INSERT | cmt_75b0e4e31a02f9a022bd | 2026-02-13T16:29:47Z | PASS | REUSED |
| 113 | 234 | linear.linear_issues | INSERT | ENG-2463 | 2026-02-13T20:49:58Z | PASS | REUSED |
| 114 | 236 | linear.linear_comments | INSERT | cmt_2785f039cfee9d256150 | 2026-02-13T20:49:58Z | PASS | REUSED |
| 115 | 238 | linear.linear_issues | INSERT | ENG-2464 | 2026-02-13T16:31:05Z | PASS | REUSED |
| 116 | 240 | linear.linear_comments | INSERT | cmt_5d88052b6f8c1b2fc181 | 2026-02-13T16:31:05Z | PASS | REUSED |
| 117 | 242 | linear.linear_issues | INSERT | ENG-2465 | 2026-02-13T16:31:48Z | PASS | REUSED |
| 118 | 244 | linear.linear_comments | INSERT | cmt_ec684ef632bdd6b375c3 | 2026-02-13T16:31:48Z | PASS | REUSED |
| 119 | 246 | linear.linear_issues | INSERT | ENG-2466 | 2026-02-12T23:32:09Z | PASS | REUSED |
| 120 | 248 | linear.linear_issues | INSERT | ENG-2467 | 2026-02-12T23:32:26Z | PASS | REUSED |
| 121 | 250 | linear.linear_issues | INSERT | ENG-2468 | 2026-02-13T16:32:20Z | PASS | REUSED |
| 122 | 252 | linear.linear_comments | INSERT | cmt_c767f5417cafd21d0457 | 2026-02-13T16:32:20Z | PASS | REUSED |
| 123 | 254 | linear.linear_issues | INSERT | ENG-2469 | 2026-02-13T16:33:51Z | PASS | REUSED |
| 124 | 256 | linear.linear_comments | INSERT | cmt_4179664f58817a32a076 | 2026-02-13T16:33:51Z | PASS | REUSED |
| 125 | 258 | linear.linear_issues | INSERT | ENG-2470 | 2026-02-12T23:33:17Z | PASS | REUSED |
| 126 | 260 | linear.linear_issues | INSERT | ENG-2471 | 2026-02-12T23:33:34Z | PASS | REUSED |
| 127 | 262 | linear.linear_issues | INSERT | ENG-2472 | 2026-02-13T00:02:44Z | PASS | REUSED |
| 128 | 264 | linear.linear_comments | INSERT | cmt_4ca653c559b182ed6ee6 | 2026-02-13T00:02:44Z | PASS | REUSED |
| 129 | 266 | linear.linear_issues | INSERT | ENG-2473 | 2026-02-13T16:36:10Z | PASS | REUSED |
| 130 | 268 | linear.linear_comments | INSERT | cmt_46c0a9358e1df9a6ded4 | 2026-02-13T16:36:10Z | PASS | REUSED |
| 131 | 270 | linear.linear_issues | INSERT | ENG-2474 | 2026-02-13T00:05:31Z | PASS | REUSED |
| 132 | 272 | linear.linear_comments | INSERT | cmt_a932354ee5e226971ed1 | 2026-02-13T00:05:31Z | PASS | REUSED |
| 133 | 274 | linear.linear_issues | INSERT | ENG-2475 | 2026-02-13T00:06:58Z | PASS | REUSED |
| 134 | 276 | linear.linear_comments | INSERT | cmt_ed6dab8ad539165c22f1 | 2026-02-13T00:06:58Z | PASS | REUSED |
| 135 | 278 | linear.linear_issues | INSERT | ENG-2476 | 2026-02-13T16:37:02Z | PASS | REUSED |
| 136 | 280 | linear.linear_comments | INSERT | cmt_8a420b3635db4a36f750 | 2026-02-13T11:20:37Z | PASS | REUSED |
| 137 | 282 | linear.linear_comments | INSERT | cmt_af582f63b3fef6e310a7 | 2026-02-13T16:37:02Z | PASS | REUSED |
| 138 | 284 | linear.linear_issues | INSERT | ENG-2477 | 2026-02-13T01:28:49Z | PASS | REUSED |
| 139 | 286 | linear.linear_comments | INSERT | cmt_977a0d481cd84d275f08 | 2026-02-13T01:28:49Z | PASS | REUSED |
| 140 | 288 | linear.linear_issues | INSERT | ENG-2478 | 2026-02-13T00:09:12Z | PASS | REUSED |
| 141 | 290 | linear.linear_comments | INSERT | cmt_d10e47fd216f16429b45 | 2026-02-13T00:09:12Z | PASS | REUSED |
| 142 | 292 | linear.linear_issues | INSERT | ENG-2479 | 2026-02-13T01:34:02Z | PASS | REUSED |
| 143 | 294 | linear.linear_comments | INSERT | cmt_4a019a675b55484b05ec | 2026-02-13T01:34:02Z | PASS | REUSED |
| 144 | 296 | linear.linear_issues | INSERT | ENG-2480 | 2026-02-13T16:38:44Z | PASS | REUSED |
| 145 | 298 | linear.linear_comments | INSERT | cmt_e3b5ee0557dca1cb519c | 2026-02-13T16:38:44Z | PASS | REUSED |
| 146 | 300 | linear.linear_issues | INSERT | ENG-2481 | 2026-02-13T20:50:40Z | PASS | REUSED |
| 147 | 302 | linear.linear_comments | INSERT | cmt_5f33dc45f96bbae1e85d | 2026-02-13T20:50:40Z | PASS | NEW (changed text) |
| 148 | 304 | linear.linear_issues | INSERT | ENG-2482 | 2026-02-12T23:36:41Z | PASS | REUSED |
| 149 | 306 | linear.linear_issues | INSERT | ENG-2483 | 2026-02-12T23:36:58Z | PASS | REUSED |
| 150 | 308 | — | COMMIT | — |  | PASS | — |

## 6. Check A — Records, references and IDs: **PASS**

| Item | Evidence | Result |
|---|---|---|
| Five changed comment rows (lines 168, 180, 192, 204, 302) | Only `body` changed. `id`, `issue_id`, `author_id`, `is_edited`, `created_at`, `updated_at` are byte-identical to revision 7, where the ids were collision-checked (`linear/data.json` `/comments`, complete, 0 hits) and the authors resolved (`usr_Robert` → robert@harmonygames.co; `usr_cc3e90160f490686` → arthur.blake@harmonygames.co, `linear/data.json` `/users`, re-confirmed this run). | PASS (REUSED, author re-confirmed) |
| Unchanged keys (145 statements) | Revision-7 §6 complete scans reused: Drive, gdocs, gsheets, Confluence, Slack, Trello, gcal, GitHub (PR #38 `base_sha`), Linear project/members/issues, Gmail. | PASS (REUSED) |
| ID contracts / Drive readability / one account per person | Lint clean. No new accounts. | PASS |

## 7. Check B — SQL structure and supported schema rules: **PASS**

- All 150 statements parse (lint). The five changed rows keep 8 columns / 8 values.
- The new bodies escape apostrophes correctly (`it''s`, `there''s`); no unescaped quote breaks a literal.
- Timestamps and NOT NULL columns are unchanged from revision 7 (`YYYY-MM-DDTHH:MM:SSZ`).
- Provisional snapshot comparison unchanged. **A1 (advisory, carried over):** `linear.linear_projects.links_json` (line 128) isn't in the snapshot. If the live table lacks it, the whole transaction rolls back. Safest: drop `links_json` and its `'[]'` value from that insert.

## 8. Check C — Dates, relationships and consistency: **FAIL**

**Clock and chronology:** no timestamp changed. The latest event timestamp is still 2026-02-13T20:50:40Z (ENG-2481 comment); the only later values are the gcal plan fields (2026-03-12). Every relative date in the new text resolves before the clock ("september" = Sep 2025, "last april" = Apr 2025, "early 2024").

**Base sources read this run:**
- Costs tab: gsheets `data.json` `/sheets_spreadsheets/141/sheets/2` ("HG Costs", 75 rows, not truncated). Months counted by position as the conventions doc says: C = Jul-23 … AF = Dec-25; AG–AR are forecast.
- Ledger: Snowflake `FINANCE.EXPENSES.FINANCE_LEDGER` (704 rows, read in full from its line in `snowflake.json`).
- Gmail `threads/*.json`: complete `search-many` scans for `dailybot` (176 matches, scan complete), case-sensitive `Kling` (23), `klingai` (3), `UA assets` (0). Cited DailyBot threads read in full.
- Slack `messages/*.json`: complete scans for case-sensitive `Kling` (7), `ua assets` (3), and `dailybot` over 2024–2026 files (1,154 matches, complete; last activity Apr 2024 standups plus one Jul 2024 DM).

### Findings

**F1 — Dailybot comment says the account is still on the free plan; the vendor deleted it in September 2025 (Check C, introduced contradiction).**
- SQL: line 192, `linear.linear_comments` `cmt_ae352002e2f80996f096` on ENG-2452, by Arthur (`usr_cc3e90160f490686`), dated 2026-02-12T23:58:05Z: "we stopped paying for dailybot in early 2024, it's sat on the free plan since".
- The first half checks out: costs tab "Dailybot" row has C–I 25/25/25/30/34/32/32 (Jul-23 → Jan-24), J–L ≈ 32.67/32.22/32.30 (Feb–Apr 2024), then 0 from M (May-24) through AF. Slack DM `messages/D04UGG61DUM/2024-07.json` /9–/14 (2 Jul 2024): "are we still paying for DailyBot?" → "it says we are on the free plan" → cancelled "end of april i think". Gmail `blake@harmonygames.co_1829825914633740644` (19 Apr 2025) confirms the Free plan in 2025.
- The second half doesn't. "It's sat on the free plan since", written on 12 Feb 2026, says the workspace still exists on the free plan today. Base Gmail says it doesn't:
  - `blake@harmonygames.co_1839039701685601092`, 30 Jul 2025, "Notice: Full Data Removal in 30 Days": no billing plan or activity in 6 months, workspace to be deleted after 30 days.
  - `blake@harmonygames.co_1842691964207508503`, **8 Sep 2025, "We deleted your organization"**: "The deletion process has been completed and we have removed your organization … and all the data related to it, including user accounts."
  - Both went to Arthur, the comment's own author. Nothing later in the base or the SQL restores or recreates the workspace.
- Effect: this is an account close-out register task. The comment makes Dailybot an existing $0 free account (a possible Cancel row with status Open). The vendor's own email makes it an account closed in September 2025, which under conventions rules 2 and 5 is cancelled before Feb 9 and vendor-confirmed. Those two readings give different register rows for the same vendor, and nothing in the records says which one wins. Calling the comment a stale or mistaken note doesn't settle it: it is the newest record and nothing corrects it.
- Note: revision 7's report suggested this wording. That suggestion missed the 8 Sep 2025 deletion email. This review corrects it.
- Smallest fix: keep the paying history and end it at the deletion, e.g. "we stopped paying for dailybot in early 2024, it sat on the free plan until they deleted the workspace last september". That matches the costs tab, the Jul 2024 Slack DM, and the Jul and Sep 2025 vendor emails.

### New claims that check out

- **Kling** (line 168, ENG-2445, Robert): "dropped kling after september". Costs-tab "Kling" row: 9 in U–AC (Jan-25 → Sep-25), 0 in AD–AF (Oct–Dec 2025) ✓. Slack: Dec 2024 "I have a paid subscription for Kling" (`C05KNDCHAAG/2024-12.json` /69) and last use Sep 2025 (`D05S58U4SAK/2025-09.json` /54) ✓. Gmail Kling hits are third-party newsletters only; no Kling receipts after September. The forecast columns (AK May-26 = 9, AO Sep-26 = 9) are base forecasts, not charges, so they don't contradict "dropped".
- **Linear** (line 180, ENG-2448, Arthur): "the p&l stops after the 2024 payment". Costs-tab "Linear" row: P (Aug-24) 2,403, Q (Sep-24) −288, then 0 through AF ✓. The Sep-24 −288 is a credit against that payment, not a later charge. The rest of the comment ("basic at the renewal, it's annual now") is unchanged and reused from revision 7. This resolves revision 7's advisory A2.
- **AWS** (line 204, ENG-2455, Arthur): "the p&l line for it was never kept up". Costs-tab "Servers (AWS)" row has one non-zero entry, AE (Nov-25) = 15; AF (Dec-25) is 0. The ledger has 35 `cloud_infra` AWS rows including FIN-000687 (2026-01-31, −1,485), which still matches "$1,485 in january" ✓. This resolves revision 7's advisory A3.
- **UA Assets** (line 302, ENG-2481, Robert): "there's no ua assets account, that line was one-off creative buys for campaigns, the last one was last april". Costs-tab "UA Assets" row: I 183.45, J 21, M 125, N 250, R 5,125, S 5,000, T 6,429, X 3,500 (Apr-25), then 0 through AF ✓. Irregular amounts fit "one-off buys". Slack Apr 2024 "We have a category called UA Assets" (`C04UEQVDVB7/2024-04.json` /167) fits a P&L category, not an account. The ledger's `marketing_ua` rows are ad networks (meta, applovin, adjoe, google_uac), not asset buys, so nothing contradicts. Gmail `UA assets`: 0 hits (complete). This fixes revision 7's F2.
- **Grader-facing text:** none. All five bodies read as workplace comments.

### Advisories (not failing)

- **A1 — `links_json`** (Check B above).
- **A4 — Carried over** (unchanged rows): facts only the injected comments carry, persona approximations (Typecast, Gusto), the stale Feb 10 sheet, and context items. See the revision-5/7 reports §8. None is affected by this change set.

## 9. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | Only comment bodies changed. Ids, authors, parents and timestamps are identical to revision 7's complete checks. |
| B — SQL structure and supported schema rules | PASS | All statements parse, quotes are escaped, column counts match. Provisional MISMATCH on `linear_projects.links_json` (A1, advisory). |
| C — Dates, relationships and consistency | **FAIL** | F1: Dailybot "it's sat on the free plan since" (12 Feb 2026) vs vendor email "We deleted your organization" (8 Sep 2025). Kling, Linear, AWS and UA Assets check out. Revision 7's F2 is fixed; A2 and A3 are resolved. Chronology clean. |

## 10. Next action and downstream

1. Reword the Dailybot comment (line 192) so it ends the free-plan period at the September 2025 deletion. Suggested wording is in §8.
2. Optional: A1 (drop `links_json`).
3. Save the corrected SQL and run `/injection` again. Because the SQL changed, every later stage that read the SQL needs to run again, in order: `/prompt`, `/hardness`, `/oe`, `/rubric`.

## 11. Evidence limits and provenance

- Static scope only. No live execution, database compatibility, search ranking, Agent visibility or difficulty assessment.
- The schema snapshot is unverified, so mismatches are advisory.
- Sources read this run (all in `Universe_Normal`): gsheets `data.json` `/sheets_spreadsheets/141/sheets/2` (full grid); Snowflake `FINANCE.EXPENSES.FINANCE_LEDGER` (704 rows); linear `data.json` `/users` (author check); Gmail `threads/*.json` complete scans listed in §8, plus the full DailyBot threads `blake@…1775440967771704865`, `…1821282500838064117`, `…1829825914633740644`, `…1839039701685601092`, `…1842691964207508503` and `vincent@…1797398353448427769`; Slack `messages/*.json` complete scans listed in §8, plus `D04UGG61DUM/2024-07.json` /5–/15 and `C04UEQVDVB7/2024-04.json` /167.
- Reused evidence: revision-7 report sha256 `960228048110de283bd9257cc9a992b9ac57d23807cb14c050947b9992fee397` (§5 ledger rows, §6 reference/collision table, §7 structure checks, §8 base facts for unchanged rows), for the 145 byte-identical statements and the unchanged non-body columns of the 5 changed rows. Dependencies verified unchanged: statement text, universe manifest, clock and the reference hashes in §1.
- Dependencies for reuse by `/prompt`: this SQL hash, the universe manifest above, clock 2026-02-14T00:00Z and the reference hashes in §1. This report is a FAIL, so `/prompt` can't reuse it as a whole-injection PASS.

### FINAL VERDICT: FAIL

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Reword the Dailybot comment (line 192) so it no longer says the workspace is still on the free plan (the vendor deleted it on 8 Sep 2025), then run /injection again, followed by /prompt, /hardness, /oe and /rubric.

Evidence limits: Static scope only; schema snapshot unverified (A1 advisory); no live deployment or Agent-visibility check.
