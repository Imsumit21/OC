# Injection data-integrity review — `injection-static-v2`

## 1. Scope

| Field | Value |
|---|---|
| Review | Chat review for your attempt (6adfee3f27ce6ca81b457137), `/injection`, static audit mode |
| Review version | `injection-static-v2` (evidence contract `stage-evidence-v1`) |
| Actual review time | 2026-10-28T03:45Z |
| Clock | 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal` (hg4-2026-08-31 v37); manifest `Evals/references/universes/normal/universe_manifest.json` sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Input reviewed | Injection SQL, revision 5 (attachment `01_Universe_Inject (3).sql`, saved as `Evals/task_inputs/01_Universe_Inject.sql`), 97,579 bytes, sha256 `9cfacf863bf1320bad32aabc6a88271429e35467338e7f6de2b0b33e26b49d4c` |
| Previous version | Revision 4, sha256 `cbc2dfed…4966`, reviewed in report sha256 `ad14e77a89a8185d36ea432ff3fa12410ea0ac3214e16ce092db7e122e2c327d` (FAIL: F1–F3). |
| References (all unchanged since that report) | Eval 0 `e034019b…6f663eff`; WORKFLOW `ee4cd8e1…504fcd5d`; schema snapshot `injection.json` `31dcb2b4…d74c5151`; schema README `9e320787…9a76eb42`; `id_contracts.json` `fc4711ef…d9ed4682`; ENVIRONMENT `4ffb2b5f…a5d5e165`; SEARCH `cab83c61…c9d3a45c`; roster `3f217451…b3c84575`; acl `e9bca2b3…04468c9f`; known_base_issues `79b20289…e7553a7b` |

## 2. Input / authority issues

- Only input for this stage is the SQL. It is substantive: 147 statements (BEGIN, 141 INSERT, 4 UPDATE, COMMIT) across gdrive, gdocs, gsheets, confluence, slack, trello, gmail, gcal, github and linear.
- Header comments ("Are you planning to inject? Yes", persona line, statement counts, "re-apply this exact SQL") are authoring notes. None mention tool calls, pass rate or gates.
- `known_base_issues.md` lists no normal-universe conflicts. No injected record builds on a Snowflake or Confluence base conflict (Snowflake streaming grep for every vendor named in the changed records: 0 hits, see §8a).

**Change set from revision 4 (statement-level diff, keyed by table + primary id):** 106 statements byte-identical; 40 changed; 4 Linear comments added; 22 removed (11 Gmail thread + 11 message rows: Vercel, Deel, Google Cloud, dbt, Zapier, QuickBooks, Cursor, DocuSign, 1Password, Slack, Kapwing; plus ENG-2484 and the Miro comment `cmt_c69744b3a98fc7bfd14a`). Changed rows: conventions doc §6 wording; Gusto Slack reply; both Trello cards; Figma/Layer/Linear/Pond5 receipts (card number removed); Unity invoice email (now copies the base Unity invoice format); commit identity; CodeRabbit PR comment; 18 Linear comments/issues.

## 3. Lint (`hg_injection_lint.py`, injection-lint-v1, run on this SQL hash)

Flags: FAIL 0, CHECK 0, INFO 1.

| Flag | Record | Resolution |
|---|---|---|
| INFO `unparsed` (metadata-only media) | line 10, `gdrive.drive_files` `f_4ac7a77383e7317eedcd83` `helpshift_export_2026-02-13.zip` | Accepted. A zip package is metadata-only, as in the base. The injected records need only the file to exist (name, folder, time); Oliver's Confluence comment names it. It becomes a FAIL only if an OE or rubric row needs the zip's contents. |

A clean lint doesn't replace checks A–C; they were run in full below.

## 4. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; hash, manifest, review version | NEW, done (revision 5 saved from the attachment) |
| Run lint, resolve flags | NEW, done (1 INFO, resolved) |
| Inventory every statement | NEW, done (147/147, §5) |
| Check A: references, collisions, ID contracts | PASS (NEW for changed/added rows; REUSED for byte-identical keys) |
| Check B: structure and supported schema rules | PASS (NEW; advisory A1) |
| Check C: dates, relationships, consistency | PASS (NEW for every changed/added row; REUSED base facts for byte-identical rows) |
| Report and verdict | NEW, done |

**Reuse basis (stage-evidence-v1):** byte-identical statements reuse the revision-4 report's per-record results (report sha256 `ad14e77a…327d`, §5 ledger rows, §6 reference/collision table, §8 "What passes"). Every dependency is unchanged: same statement text, same universe manifest `5e01ac44…`, same clock, same Eval/schema/id_contracts/roster/acl hashes (§1). Removing rows can't create a collision or broken reference, since no remaining row references a removed one (checked: no remaining record cites a removed Gmail id or ENG-2484). Every changed or added row and every claim it makes was checked again from source this run.

## 5. Operation ledger (every statement, execution order)

Lines are physical lines in the saved SQL. "Latest event time" is the last ISO event timestamp in the row (the gcal start/end plan fields, 2026-03-12, are excluded). "Verification" is NEW (changed/added and re-checked) or REUSED (byte-identical to revision 4, previously checked).

| # | Line | Table | Op | Record / target | Latest event time or change | Result | Verification |
|---|---|---|---|---|---|---|---|
| 1 | 5 | — | BEGIN | — | — | PASS | — |
| 2 | 8 | gdrive.drive_files | INSERT | f_1326e66bcabfda8fd29e4a | 2026-02-13T16:58:40Z | PASS | REUSED |
| 3 | 10 | gdrive.drive_files | INSERT | f_4ac7a77383e7317eedcd83 | 2026-02-13T15:04:51Z | PASS (lint INFO: metadata-only zip) | REUSED |
| 4 | 12 | gdrive.drive_files | INSERT | f_768cd23a00c4b12fa0e975 | 2026-02-10T18:31:55Z | PASS | REUSED |
| 5 | 15 | gdocs.docs_documents | INSERT | f_1326e66bcabfda8fd29e4a | 2026-02-13T16:58:40Z | PASS | NEW (changed) |
| 6 | 18 | gsheets.sheets_spreadsheets | INSERT | f_768cd23a00c4b12fa0e975 | 2026-02-10T18:31:55Z | PASS | REUSED |
| 7 | 20 | gsheets.sheets_sheets | INSERT | f_768cd23a00c4b12fa0e975 |  | PASS | REUSED |
| 8 | 23 | confluence.confluence_pages | INSERT | page_ua_vendor_closeout | 2025-03-18T15:20:00Z | PASS | REUSED |
| 9 | 25 | confluence.confluence_page_versions | INSERT | ver_64b0ed607e093b18a698fb883a584aa6 | 2025-03-18T15:20:00Z | PASS | REUSED |
| 10 | 27 | confluence.confluence_pages | INSERT | page_support_after_helpshift | 2026-02-12T20:05:14Z | PASS | REUSED |
| 11 | 29 | confluence.confluence_page_versions | INSERT | ver_16458585128da06d66a64fa5055bea00 | 2026-02-12T20:05:14Z | PASS | REUSED |
| 12 | 31 | confluence.confluence_comments | INSERT | comment_support_after_helpshift_c1 | 2026-02-13T15:10:27Z | PASS | REUSED |
| 13 | 34 | slack.slack_messages | INSERT | b9ef575bec54b095edb75a0fe83580f5 | 2026-02-13T02:14:36.205117Z | PASS (advisory A3 Gusto timing) | NEW (changed) |
| 14 | 36 | slack.slack_messages | INSERT | fda86aac9fb55c96ffee4bba3e59cc14 | 2026-02-13T10:02:18.774231Z | PASS | REUSED |
| 15 | 38 | slack.slack_messages | INSERT | 9e245e76cbaf7f080e1995ec0c4ec30d | 2026-02-13T17:21:07.448213Z | PASS | REUSED |
| 16 | 39 | slack.slack_messages | UPDATE | 6d8c8d8affd1255b13d8d875f1547e70 | thread_ts_legacy = '1770933601.686309', reply_count = 1, rep | PASS | REUSED |
| 17 | 42 | trello.trello_cards | INSERT | 643efb2ab65c5e952575dde5 | 2023-04-18T20:18:50Z | PASS | NEW (changed) |
| 18 | 44 | trello.trello_actions | INSERT | 643efb2a2768759bdebceec4 | 2023-04-18T20:18:50Z | PASS | REUSED |
| 19 | 46 | trello.trello_cards | INSERT | 698f48be4ba0affafbf153db | 2026-02-13T15:52:30Z | PASS | NEW (changed) |
| 20 | 48 | trello.trello_actions | INSERT | 698f48be304fbb37e4e3aafa | 2026-02-13T15:52:30Z | PASS | REUSED |
| 21 | 51 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856945900224536585 |  | PASS | REUSED |
| 22 | 53 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com> | 2026-02-12T18:40:12Z | PASS | NEW (changed) |
| 23 | 65 | gmail.gmail_threads | INSERT | leonard.hayes@harmonygames.co/1856945900224877235 |  | PASS | REUSED |
| 24 | 67 | gmail.gmail_messages | INSERT | leonard.hayes@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com> | 2026-02-12T18:40:12Z | PASS | NEW (changed) |
| 25 | 79 | gmail.gmail_threads | INSERT | arthur.blake@harmonygames.co/1856945900225226172 |  | PASS | REUSED |
| 26 | 81 | gmail.gmail_messages | INSERT | arthur.blake@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com> | 2026-02-12T18:40:12Z | PASS | NEW (changed) |
| 27 | 93 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856965916492026238 |  | PASS | REUSED |
| 28 | 95 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | 2026-02-12T23:58:21Z | PASS | NEW (changed) |
| 29 | 107 | gmail.gmail_threads | INSERT | leonard.hayes@harmonygames.co/1856965916492755786 |  | PASS | REUSED |
| 30 | 109 | gmail.gmail_messages | INSERT | leonard.hayes@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | 2026-02-12T23:58:21Z | PASS | NEW (changed) |
| 31 | 121 | gmail.gmail_threads | INSERT | arthur.blake@harmonygames.co/1856965916492023943 |  | PASS | REUSED |
| 32 | 123 | gmail.gmail_messages | INSERT | arthur.blake@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | 2026-02-12T23:58:21Z | PASS | NEW (changed) |
| 33 | 134 | gmail.gmail_threads | UPDATE | robert@harmonygames.co/1856965916492026238 | snippet = 'Hi all — one change after our engineers walked th | PASS | REUSED |
| 34 | 136 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> | 2026-02-13T18:20:44Z | PASS | NEW (changed) |
| 35 | 139 | gmail.gmail_threads | UPDATE | leonard.hayes@harmonygames.co/1856965916492755786 | snippet = 'Hi all — one change after our engineers walked th | PASS | REUSED |
| 36 | 141 | gmail.gmail_messages | INSERT | leonard.hayes@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> | 2026-02-13T18:20:44Z | PASS | NEW (changed) |
| 37 | 144 | gmail.gmail_threads | UPDATE | arthur.blake@harmonygames.co/1856965916492023943 | snippet = 'Hi all — one change after our engineers walked th | PASS | REUSED |
| 38 | 146 | gmail.gmail_messages | INSERT | arthur.blake@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> | 2026-02-13T18:20:44Z | PASS | NEW (changed) |
| 39 | 150 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1842984194671106077 |  | PASS | NEW (changed) |
| 40 | 152 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAowZ1ukjS1ZxLCL4aRt1VM-c-GnNMTNWVQS47OM@mail.gmail.com> | 2025-09-11T16:04:52Z | PASS | NEW (changed) |
| 41 | 154 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1855299418849853856 |  | PASS | NEW (changed) |
| 42 | 156 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CA4Ce6Oa74xUtCgFI1iGnZMieCxsUh90MhimgGu3@mail.gmail.com> | 2026-01-25T14:30:05Z | PASS | NEW (changed) |
| 43 | 158 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1855912858878482138 |  | PASS | NEW (changed) |
| 44 | 160 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAL7W0WN5jkixON6h71KIRU6DcLoQyjXVIYONWEZ@mail.gmail.com> | 2026-02-01T09:00:27Z | PASS | NEW (changed) |
| 45 | 162 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856653066502254886 |  | PASS | NEW (changed) |
| 46 | 164 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAIoQDHYpNPHXVgnNS8DUmtr__81CmMffz7hcWJv@mail.gmail.com> | 2026-02-09T13:05:44Z | PASS | NEW (changed) |
| 47 | 166 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856761009013149089 |  | PASS | NEW (changed) |
| 48 | 168 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAAV70N_MnwWfJSNuqS_HKOnLheApwCzJGSFQi8q@mail.gmail.com> | 2026-02-10T17:41:26Z | PASS | NEW (changed) |
| 49 | 170 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856859516436705234 |  | PASS | REUSED |
| 50 | 172 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAxSGYrkpVAs45dr7lAugwSThN-X-ma7vq_V1xAV@mail.gmail.com> | 2026-02-11T19:47:10Z | PASS | REUSED |
| 51 | 175 | gcal.gcal_events | INSERT | evt_2ac66383ee72bbb05a0376 | 2026-02-12T22:40:15Z | PASS | REUSED |
| 52 | 177 | gcal.gcal_events | INSERT | evt_f1d245d44ceff5a6e049c0 | 2026-02-12T22:40:15Z | PASS | REUSED |
| 53 | 179 | gcal.gcal_events | INSERT | evt_d1fe12afe85ffbb49bd998 | 2026-02-12T22:40:15Z | PASS | REUSED |
| 54 | 182 | github.github_pull_requests | INSERT | harmonygames-Games/Combo-Fighters#38 | 2026-02-13T09:41:12Z | PASS | REUSED |
| 55 | 184 | github.github_branches | INSERT | harmonygames-Games/Combo-Fighters:oliver/final-build-settings |  | PASS | REUSED |
| 56 | 186 | github.github_commits | INSERT | c769b476f150a76280886f194b4d2186cfd96ca4 | 2026-02-13T09:23:51Z | PASS (F3 fixed) | NEW (changed) |
| 57 | 188 | github.github_pull_request_commits | INSERT | harmonygames-Games/Combo-Fighters#38#c_0 |  | PASS | REUSED |
| 58 | 190 | github.github_pr_comments | INSERT | harmonygames-Games/Combo-Fighters#38#c_1 | 2026-02-13T09:41:12Z | PASS (F1b fixed) | NEW (changed) |
| 59 | 192 | github.github_timeline_events | INSERT | harmonygames-Games/Combo-Fighters#38#ev_1 | 2026-02-13T09:41:12Z | PASS | REUSED |
| 60 | 195 | linear.linear_projects | INSERT | 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a | 2026-02-12T23:24:10Z | PASS (advisory A1 links_json) | REUSED |
| 61 | 197 | linear.linear_project_teams | INSERT | ptm_2183726e36ddf7f8 | 2026-02-12T23:24:10Z | PASS | REUSED |
| 62 | 199 | linear.linear_project_members | INSERT | pmem_dec4e6c3f1315d8a | 2026-02-12T23:24:10Z | PASS | REUSED |
| 63 | 201 | linear.linear_project_members | INSERT | pmem_5648d2826ae7a30d | 2026-02-12T23:24:10Z | PASS | REUSED |
| 64 | 203 | linear.linear_project_members | INSERT | pmem_ca4f8a31e35bad07 | 2026-02-12T23:24:10Z | PASS | REUSED |
| 65 | 205 | linear.linear_issues | INSERT | ENG-2438 | 2026-02-13T19:05:12Z | PASS | REUSED |
| 66 | 207 | linear.linear_comments | INSERT | cmt_5da8c3467fc022248fb3 | 2026-02-13T19:05:12Z | PASS | NEW (changed) |
| 67 | 209 | linear.linear_issues | INSERT | ENG-2439 | 2026-02-13T16:12:40Z | PASS | REUSED |
| 68 | 211 | linear.linear_comments | INSERT | cmt_96ae7b3689c1d073a2ff | 2026-02-13T16:12:40Z | PASS | NEW (changed) |
| 69 | 213 | linear.linear_issues | INSERT | ENG-2440 | 2026-02-12T23:52:03Z | PASS | REUSED |
| 70 | 215 | linear.linear_comments | INSERT | cmt_e8aa0ee7c1bbe08a47c9 | 2026-02-12T23:52:03Z | PASS | REUSED |
| 71 | 217 | linear.linear_issues | INSERT | ENG-2441 | 2026-02-13T20:41:09Z | PASS | REUSED |
| 72 | 219 | linear.linear_comments | INSERT | cmt_37c23c5d30cc6597ebe9 | 2026-02-13T20:41:09Z | PASS (F2 fixed: matches costs tab) | NEW (changed) |
| 73 | 221 | linear.linear_issues | INSERT | ENG-2442 | 2026-02-13T20:43:30Z | PASS | REUSED |
| 74 | 223 | linear.linear_comments | INSERT | cmt_6f994dc8a93d75efb3f8 | 2026-02-13T20:43:30Z | PASS (F2 fixed; advisory A3 wording) | NEW (changed) |
| 75 | 225 | linear.linear_issues | INSERT | ENG-2443 | 2026-02-12T23:55:41Z | PASS | REUSED |
| 76 | 227 | linear.linear_comments | INSERT | cmt_ec32fbf9ca984b23f7a6 | 2026-02-12T23:55:41Z | PASS | REUSED |
| 77 | 229 | linear.linear_issues | INSERT | ENG-2444 | 2026-02-13T20:45:02Z | PASS | REUSED |
| 78 | 231 | linear.linear_comments | INSERT | cmt_497a61c14b69830f198a | 2026-02-13T20:45:02Z | PASS | REUSED |
| 79 | 233 | linear.linear_issues | INSERT | ENG-2445 | 2026-02-13T20:45:51Z | PASS | REUSED |
| 80 | 235 | linear.linear_comments | INSERT | cmt_276e0b8a551891ddbdff | 2026-02-13T20:45:51Z | PASS | REUSED |
| 81 | 237 | linear.linear_issues | INSERT | ENG-2446 | 2026-02-12T23:26:29Z | PASS | REUSED |
| 82 | 239 | linear.linear_issues | INSERT | ENG-2447 | 2026-02-12T23:57:10Z | PASS | REUSED |
| 83 | 241 | linear.linear_comments | INSERT | cmt_8ab16d9d7ac715d1c9a7 | 2026-02-12T23:57:10Z | PASS | REUSED |
| 84 | 243 | linear.linear_issues | INSERT | ENG-2448 | 2026-02-12T23:58:30Z | PASS | REUSED |
| 85 | 245 | linear.linear_comments | INSERT | cmt_e8ae507893bfdb06c8c7 | 2026-02-12T23:58:30Z | PASS | REUSED |
| 86 | 247 | linear.linear_issues | INSERT | ENG-2449 | 2026-02-12T23:27:20Z | PASS | REUSED |
| 87 | 249 | linear.linear_issues | INSERT | ENG-2450 | 2026-02-13T20:47:15Z | PASS | REUSED |
| 88 | 251 | linear.linear_comments | INSERT | cmt_e3da997ff7b6575fbea0 | 2026-02-13T20:47:15Z | PASS (F2 fixed) | NEW (changed) |
| 89 | 253 | linear.linear_issues | INSERT | ENG-2451 | 2026-02-12T23:27:54Z | PASS | REUSED |
| 90 | 255 | linear.linear_issues | INSERT | ENG-2452 | 2026-02-12T23:28:11Z | PASS | REUSED |
| 91 | 257 | linear.linear_issues | INSERT | ENG-2453 | 2026-02-13T16:20:33Z | PASS | REUSED |
| 92 | 259 | linear.linear_comments | INSERT | cmt_276837877e2b3edc466a | 2026-02-13T16:20:33Z | PASS | REUSED |
| 93 | 261 | linear.linear_issues | INSERT | ENG-2454 | 2026-02-13T16:24:02Z | PASS | REUSED |
| 94 | 263 | linear.linear_comments | INSERT | cmt_5a650ef858f3cd5a0410 | 2026-02-13T16:24:02Z | PASS | REUSED |
| 95 | 265 | linear.linear_issues | INSERT | ENG-2455 | 2026-02-13T19:12:45Z | PASS | REUSED |
| 96 | 267 | linear.linear_comments | INSERT | cmt_62852832c28dc669e459 | 2026-02-13T19:12:45Z | PASS | REUSED |
| 97 | 269 | linear.linear_issues | INSERT | ENG-2456 | 2026-02-13T01:30:22Z | PASS | REUSED |
| 98 | 271 | linear.linear_comments | INSERT | cmt_2b4807a6cf797d1f4886 | 2026-02-13T01:30:22Z | PASS | REUSED |
| 99 | 273 | linear.linear_issues | INSERT | ENG-2457 | 2026-02-13T01:29:55Z | PASS | REUSED |
| 100 | 275 | linear.linear_comments | INSERT | cmt_bbdca23f075e9fca5cb8 | 2026-02-13T01:29:55Z | PASS | REUSED |
| 101 | 277 | linear.linear_issues | INSERT | ENG-2458 | 2026-02-13T01:33:10Z | PASS | NEW (changed) |
| 102 | 279 | linear.linear_comments | INSERT | cmt_6e664bfa3fea62baabb5 | 2026-02-13T01:33:10Z | PASS (advisory A2 card identity) | NEW (added) |
| 103 | 281 | linear.linear_issues | INSERT | ENG-2459 | 2026-02-13T19:15:08Z | PASS | REUSED |
| 104 | 283 | linear.linear_comments | INSERT | cmt_8f765d1313e9b01a8c22 | 2026-02-13T19:15:08Z | PASS (advisory A2 no base receipt) | NEW (changed) |
| 105 | 285 | linear.linear_issues | INSERT | ENG-2460 | 2026-02-13T16:25:31Z | PASS | NEW (changed) |
| 106 | 287 | linear.linear_comments | INSERT | cmt_7cf5d70170f54a8f925f | 2026-02-13T16:25:31Z | PASS (advisory A2 card identity) | NEW (added) |
| 107 | 289 | linear.linear_issues | INSERT | ENG-2461 | 2026-02-13T16:26:19Z | PASS | REUSED |
| 108 | 291 | linear.linear_comments | INSERT | cmt_2238bd7d0a60d8e4f31c | 2026-02-13T16:26:19Z | PASS | REUSED |
| 109 | 293 | linear.linear_issues | INSERT | ENG-2462 | 2026-02-13T16:29:47Z | PASS | REUSED |
| 110 | 295 | linear.linear_comments | INSERT | cmt_75b0e4e31a02f9a022bd | 2026-02-13T16:29:47Z | PASS | REUSED |
| 111 | 297 | linear.linear_issues | INSERT | ENG-2463 | 2026-02-13T20:49:58Z | PASS | REUSED |
| 112 | 299 | linear.linear_comments | INSERT | cmt_2785f039cfee9d256150 | 2026-02-13T20:49:58Z | PASS | REUSED |
| 113 | 301 | linear.linear_issues | INSERT | ENG-2464 | 2026-02-13T16:31:05Z | PASS | REUSED |
| 114 | 303 | linear.linear_comments | INSERT | cmt_5d88052b6f8c1b2fc181 | 2026-02-13T16:31:05Z | PASS (advisory A2 card identity) | REUSED |
| 115 | 305 | linear.linear_issues | INSERT | ENG-2465 | 2026-02-13T16:31:48Z | PASS | NEW (changed) |
| 116 | 307 | linear.linear_comments | INSERT | cmt_ec684ef632bdd6b375c3 | 2026-02-13T16:31:48Z | PASS (advisory A2 card identity) | NEW (added) |
| 117 | 309 | linear.linear_issues | INSERT | ENG-2466 | 2026-02-12T23:32:09Z | PASS | REUSED |
| 118 | 311 | linear.linear_issues | INSERT | ENG-2467 | 2026-02-12T23:32:26Z | PASS | REUSED |
| 119 | 313 | linear.linear_issues | INSERT | ENG-2468 | 2026-02-13T16:32:20Z | PASS | NEW (changed) |
| 120 | 315 | linear.linear_comments | INSERT | cmt_c767f5417cafd21d0457 | 2026-02-13T16:32:20Z | PASS | NEW (added) |
| 121 | 317 | linear.linear_issues | INSERT | ENG-2469 | 2026-02-13T16:33:51Z | PASS | REUSED |
| 122 | 319 | linear.linear_comments | INSERT | cmt_4179664f58817a32a076 | 2026-02-13T16:33:51Z | PASS | NEW (changed) |
| 123 | 321 | linear.linear_issues | INSERT | ENG-2470 | 2026-02-12T23:33:17Z | PASS | REUSED |
| 124 | 323 | linear.linear_issues | INSERT | ENG-2471 | 2026-02-12T23:33:34Z | PASS | REUSED |
| 125 | 325 | linear.linear_issues | INSERT | ENG-2472 | 2026-02-13T00:02:44Z | PASS | REUSED |
| 126 | 327 | linear.linear_comments | INSERT | cmt_4ca653c559b182ed6ee6 | 2026-02-13T00:02:44Z | PASS (F2 fixed) | NEW (changed) |
| 127 | 329 | linear.linear_issues | INSERT | ENG-2473 | 2026-02-13T16:36:10Z | PASS | REUSED |
| 128 | 331 | linear.linear_comments | INSERT | cmt_46c0a9358e1df9a6ded4 | 2026-02-13T16:36:10Z | PASS | REUSED |
| 129 | 333 | linear.linear_issues | INSERT | ENG-2474 | 2026-02-13T00:05:31Z | PASS | REUSED |
| 130 | 335 | linear.linear_comments | INSERT | cmt_a932354ee5e226971ed1 | 2026-02-13T00:05:31Z | PASS (F1b fixed) | NEW (changed) |
| 131 | 337 | linear.linear_issues | INSERT | ENG-2475 | 2026-02-13T00:06:58Z | PASS | REUSED |
| 132 | 339 | linear.linear_comments | INSERT | cmt_ed6dab8ad539165c22f1 | 2026-02-13T00:06:58Z | PASS (advisory A2 no base receipt) | NEW (changed) |
| 133 | 341 | linear.linear_issues | INSERT | ENG-2476 | 2026-02-13T16:37:02Z | PASS | REUSED |
| 134 | 343 | linear.linear_comments | INSERT | cmt_8a420b3635db4a36f750 | 2026-02-13T11:20:37Z | PASS | REUSED |
| 135 | 345 | linear.linear_comments | INSERT | cmt_af582f63b3fef6e310a7 | 2026-02-13T16:37:02Z | PASS (advisory A2 amount has no base receipt) | NEW (changed) |
| 136 | 347 | linear.linear_issues | INSERT | ENG-2477 | 2026-02-13T01:28:49Z | PASS | REUSED |
| 137 | 349 | linear.linear_comments | INSERT | cmt_977a0d481cd84d275f08 | 2026-02-13T01:28:49Z | PASS | NEW (changed) |
| 138 | 351 | linear.linear_issues | INSERT | ENG-2478 | 2026-02-13T00:09:12Z | PASS | REUSED |
| 139 | 353 | linear.linear_comments | INSERT | cmt_d10e47fd216f16429b45 | 2026-02-13T00:09:12Z | PASS | NEW (changed) |
| 140 | 355 | linear.linear_issues | INSERT | ENG-2479 | 2026-02-13T01:34:02Z | PASS | NEW (changed) |
| 141 | 357 | linear.linear_comments | INSERT | cmt_4a019a675b55484b05ec | 2026-02-13T01:34:02Z | PASS (advisory A2 no base receipt) | NEW (changed) |
| 142 | 359 | linear.linear_issues | INSERT | ENG-2480 | 2026-02-13T16:38:44Z | PASS | REUSED |
| 143 | 361 | linear.linear_comments | INSERT | cmt_e3b5ee0557dca1cb519c | 2026-02-13T16:38:44Z | PASS | REUSED |
| 144 | 363 | linear.linear_issues | INSERT | ENG-2481 | 2026-02-12T23:36:24Z | PASS | REUSED |
| 145 | 365 | linear.linear_issues | INSERT | ENG-2482 | 2026-02-12T23:36:41Z | PASS | NEW (changed) |
| 146 | 367 | linear.linear_issues | INSERT | ENG-2483 | 2026-02-12T23:36:58Z | PASS | NEW (changed) |
| 147 | 368 | — | COMMIT | — | — | PASS | — |

## 6. Check A — Records, references and IDs: **PASS**

**References resolved:**

| Reference | Source / coverage | Result |
|---|---|---|
| Linear users Arthur `usr_cc3e90160f490686` (`/users/35`), Leonard `usr_63fffeb4fab5233e` (`/users/13`), `usr_Robert` (`/users/26`), Oliver `usr_bdf01b53c6a92c5e` (`/users/29`) | `linear/data.json` `/users`, 41 records, scan complete (NEW) | all exist. ENG-2482 is now assigned to Arthur and ENG-2483 to Leonard, both existing users. |
| GitHub `EMPLOYEE_0003_GITHUB_USERNAME` (`/users/1`: Oliver Brooks, oliver.brooks@harmonygames.co); `PERSON_6026_GITHUB_USERNAME` (`/users/37`, CodeRabbit); `SVC_0321_GITHUB_USERNAME` (`/users/42`, bot) | `github/data.json` `/users`, 47 records, complete (NEW) | all exist. **F3 fixed:** commit `c769b476…` now uses author/committer name `Oliver Brooks` and email `oliver.brooks@harmonygames.co`, matching `/users/1`. |
| Unity sender token `SVC_5771` | base Gmail: Unity invoices from SVC_5771 monthly, e.g. `CINV_00003891` (2025-05-09), `CINV_00022209` (2025-11-10, `threads/00015915`) (NEW) | the right vendor. The new body copies the base invoice wording ("Attached is your 10 2025 monthly invoice…" pattern). `CINV_00031877` has 0 base hits (complete Gmail scan) and fits the base sequence (~3,000 per month; Feb 2026 ≈ 31,000). |
| All other actors, parents, channels, boards, repos, Drive folders, Confluence space/pages, Slack UPDATE target `6d8c8d8a…` | REUSED from revision-4 report §6 (unchanged values) | resolve |

**New-key collisions: none.**
- NEW: the 4 added Linear comment ids (`cmt_6e664bfa3fea62baabb5`, `cmt_7cf5d70170f54a8f925f`, `cmt_ec684ef632bdd6b375c3`, `cmt_c767f5417cafd21d0457`) against `linear/data.json` `/comments` (empty base collection, scan complete) and against the other 35 SQL comment ids (no duplicates). Commit sha `c769b476…` against `/commits` (12,687 records, complete, 0 hits). ENG issue identifiers re-checked against `/issues` (3,852 records, complete, 0 hits); ENG-2438…2483 are contiguous and unique in the SQL.
- REUSED (unchanged keys, revision-4 §6, all complete scans): Drive 3, gdocs, gsheets, Confluence 5, Slack 3 (687,230 messages), Trello 2 cards + 2 actions + idShort 68/456, gcal 3 + ical_uid, GitHub PR #38/branch/PR-commit/comment/timeline, Linear project/team/members, Gmail 15 message ids and 12 thread ids.

**ID contracts:** Gmail `history_id` is NULL on all 12 threads ✓. No Drive `content_path` is set (Google-native doc and sheet, metadata-only zip) ✓. One account per person: no new account for an existing person. Maya (PERSON_7731, Sunset) and Sherwood (PERSON_0728) are unchanged from revision 4 ✓.

## 7. Check B — SQL structure and supported schema rules: **PASS** (advisory A1)

- All 141 INSERTs are single-row, column count equals value count, no duplicate columns, every statement terminated; BEGIN…COMMIT wraps the script. The 4 UPDATEs each use a single-row `id =` predicate on a base row (Slack `6d8c8d8a…`) or a row inserted earlier in the script (3 Gmail threads).
- Every NOT NULL column without a default is supplied (lint `missing_required` clean), including `linear_issues.state_history_json = '[]'`. No generated column (`text_fts`, `body_text_fts`) is set.
- `*_json` literals parse and match the snapshot shapes (lint `json_shape` clean). Slack `metadata_json = '{}'`.
- Linear text dates are all `YYYY-MM-DDTHH:MM:SSZ`, and `start_date = '2026-02-12'` (lint `text_time_format` clean).
- gdocs `style_runs_json` NORMAL_TEXT run now ends at 2656, which equals the new body length (2,656 characters) ✓.
- Provisional snapshot comparison: MATCH for every listed column except A1. NOT COVERED: `confluence.confluence_pages`, `confluence_page_versions`, `confluence_comments`, `linear.linear_project_teams`, `linear.linear_project_members`.
- **A1 (advisory, carried over):** `linear.linear_projects.links_json` (line 128) isn't in the snapshot, and base Linear projects have no `links` field. If the live table lacks it, the whole transaction rolls back. Safest: drop `links_json` and its `'[]'` value from that insert.

## 8. Check C — Dates, relationships and consistency: **PASS**

**Clock and internal chronology (NEW, all 147 statements):** the latest event timestamp is 2026-02-13T20:49:58Z (ENG-2463 comment). The only later values are gcal start/end plan fields (2026-03-12 17:00–17:45Z). All 46 Linear issues have `updated_at` equal to their last comment (or creation) time, including the four whose `updated_at` changed (ENG-2458 01:33:10Z, ENG-2460 16:25:31Z, ENG-2465 16:31:48Z, ENG-2468 16:32:20Z). No comment predates its issue. Gmail `internal_date`, `date` and Date headers agree on every changed row (dates unchanged).

**Revision-4 failures, now fixed:**

| Finding | Revision 5 | Evidence |
|---|---|---|
| F1a Kapwing notice (Mar 1, Feb 1 charge) | Removed. ENG-2478: "kapwing emailed to confirm, pro runs out later this month. it was $24 a month" | Base Kapwing notice to Arthur, 2026-02-12T22:56Z: Pro until Feb 25; monthly receipts $24 on card 2758 ✓. Comment (Feb 13 00:09Z) follows the notice ✓ |
| F1b CodeRabbit (Pro, 2×$24, ends Feb 26) | PR #38 bot: "was canceled on Feb 12, 2026, so this pull request was not reviewed". ENG-2474: "lite plan, 3 seats at $15" | Base CodeRabbit email: Lite (Monthly) $15 × 3 units, cancellation date 12-Feb-2026 ✓. PR created Feb 13, after the cancellation ✓ |
| F1c Slack second invoice | Removed. ENG-2465: "slack renews on the 3rd, it's on the svb card" | Base Slack renewal 2026-02-03, next renewal 3/3/26 ✓ |
| F1d QuickBooks second receipt | Removed. ENG-2460: "intuit takes the $115 from my own card on the 4th, not the svb one" | Base Intuit receipt to Leonard: invoice date 02/04/2026, $115.00, card ending 5348; monthly "Intuit subscription payment" mails on the 4th (Oct–Feb) ✓; costs tab AF Quickbooks 115 ✓ |
| F1e Google Cloud ($14.33 Jan, card 4417) | Removed. ENG-2458: "google cloud charges the svb card on the 1st" | Base Google Cloud payment receipts on the 1st every month (Oct 1, Nov 1, Dec 1, Jan 1, Feb 1), card x-2758 ✓ |
| F1f dbt second charge | Removed. ENG-2457 unchanged ("dbt is on the kubllc card now") | Base dbt receipts on the 1st/2nd; Arthur's base #winddown move message ✓ |
| F1g Zapier Starter $29.99 | Removed. ENG-2476: "cancelled zapier yesterday, their email says the plan runs until feb 27. it was $73.50 a month" | Base Zapier email to Leonard 2026-02-12T21:55Z: "Professional with 750 tasks has been canceled … billing cycle on February 27, 2026" ✓; "yesterday" from Feb 13 ✓ |
| F2 Office 365 / Typecast / Adobe / OpenAI "never paid" | Reworded | Costs tab (`/sheets_spreadsheets/141/sheets/2`, months by position, AF = Dec-25): Office 365 $12.50 Sep 2023–Dec 2024 → "dropped at the end of 2024, the line's been 0 since" ✓. OpenAI Jul 2023–Apr 2024 → "api credits, we stopped those in 2024" ✓. Adobe through Oct 2024 → "plan ended in october 2024" ✓. Typecast $33 May 2024–Jul 2025 → "stopped paying after the summer" (see A3) |
| F3 commit identity | Fixed | §6 |
| Prior advisories | Miro row removed (A2); 1Password now "From Arthur's own list", Lucidchart/Google Ads "From old receipts" (A3); Helpshift comment now "discontinuing us at the end of february", matching base Helpshift reply of Feb 11 (A4); Gusto reworded (A5, now A3 below); Chase card `closed = true` like its neighbours (A7) | ✓ |

**New claims in changed rows, checked against base:**
- Unity: the Feb 10 invoice email (above) and ENG-2438 "their invoice lands on the 10th": base Unity invoices land 8th–13th; base #winddown `/190` assigns Arthur to email Unity ✓.
- GitHub (ENG-2477): "team plan is $52 a month plus copilot usage, $90 last month all in". Base GitHub receipt to Arthur 2026-02-03: Team Plan $52.00 + Copilot Usage $38.00 = Total $90.00, card ending 2758 ✓.
- DocuSign (ENG-2469): "annual, $300, renews apr 20". Base DocuSign renewal notice to Leonard, 2025-03-19 (`leonard@…1827068676034658582`): Plan Standard - Annual, Renewal Date 04/20/2025, Renewal Price 300 ✓.
- Deel (ENG-2468): "paid by transfer from the bank account, nothing on a card". Base SVB payment notifications: Analysis Checking → Deel, Inc. (Dec 1, 2025 $20,879.68; Jan 2, 2026 $19,656.03) ✓. The removed injected Deel card receipt was the only contrary record.
- Gusto (Slack reply): "pulls its invoice from the bank on the 3rd". Base Gusto "invoice has been paid" mails say "You will see the funds debit from your bank account in 1 business day": January invoice notice Feb 2 PT → debit Feb 3 ✓ (earlier months: Dec 2, Jan 5). See A3.
- Lucidchart (ENG-2482, "From old receipts"): base Lucidchart receipts and subscription mails 2024-07 to 2025-10 ✓. Google Ads (ENG-2483): base Google Ads account mails (2024) exist ✓.
- Receipts with the card number removed (Figma, Layer, Linear, Pond5): amounts and dates unchanged and previously verified (Figma $1,212 in costs-tab AC = Sep 2025 ✓). There are no base Layer, Pond5, Soundly, Cursor, 1Password or Vercel billing mails to conflict with (complete Gmail scan since 2024-06 for those names).
- Conventions doc §6 now says "Keep rows that aren't on the SVB card get a dash". This is persona guidance; it contradicts no record.
- Grader-facing text: none. Every injected text reads as workplace content (doc, emails, Slack, comments); none addresses a solver or grader or describes the test.

### Advisories (not failing)

- **A1 — `links_json`** (Check B above).
- **A2 — Facts that only the injected comments carry.** These comments are the only source for some vendor facts. Base Gmail and Snowflake have nothing that contradicts them, and nothing that confirms them either:
  - Cursor "$40/mo, renews on the 5th", Zapier "$73.50 a month", 1Password "$19.95 a month, renews on the 8th", Vercel "bills on the 22nd".
  - Which card is "the svb card" (Workspace, Slack, BigQuery, QuickBooks "not the svb one"). Base SVB mails redact the card number.
  - One soft tension: card 5348, which Leonard calls "my own card", also paid company items in base (Meta ads receipts Dec 2024, Cogency Global Dec 2024, a Metabase receipt Jun 2024). That's not proof that it's a company card.
  - These are valid injected facts. If the expected register or rubric depends on them, /prompt should confirm the Agent can find them in these comments.
- **A3 — Persona approximations.** Typecast "stopped paying after the summer": the last charge is Jul 2025 (costs-tab AA), and Aug 2025 is blank. Gusto "on the 3rd" matches the latest debit, but earlier months fell on Dec 2 and Jan 5. Neither is a demonstrated contradiction. Avoid grading an exact day or month that depends on them.
- **A4 — Stale sheet, consistent.** Arthur's Feb 10 "Subscriptions" sheet values differ from the costs tab and the comments: Unity 1200 vs 2172, Cursor 20 vs 40, Layer 39 vs 49, Zapier 20 vs 73.50, CodeRabbit 30 vs 45. The Linear project description says it "replaces my subscriptions sheet from Tuesday", so the records explain the sheet as superseded.
- **A5 — Context, consistent (carried over).**
  - Leonard told Helpshift on Feb 10 "We don't need to export any data". The Sunset deal signed Feb 12 later requires an export.
  - Base SVB (Feb 12 20:29Z) offered to cancel the card "asap". The injected Feb 13 Trello card sets closure for Feb 20 after the payoff.
  - "Last night" for Feb 12 afternoon items is colloquial.
  - The costs-tab Sound line at AF is 20, which covers Pond5, Soundly and Elevenlabs together, so it doesn't conflict with Soundly $10 + Pond5 $5.

### 8a. Snowflake cross-check

Streaming grep of `snowflake.json` (2,595,500,625 bytes, complete) for cursor, anysphere, 1password, lucidchart, google ads, vercel, docusign, layer.ai, pond5, zapier, github, kapwing, coderabbit and "unity technologies": 0 hits. Revision 4 also found 0 hits for Kapwing, Zapier, CodeRabbit, QuickBooks, Intuit, dbt Labs, Slack Technologies, Google Cloud, Miro and Typecast. Snowflake neither supports nor contradicts these records.

## 9. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | All references resolve (Linear and GitHub users re-checked; Unity sender verified). F3 fixed. New Linear comment ids, commit sha and ENG identifiers are collision-free (complete scans). Unchanged keys reuse revision-4 complete scans. ID contracts met. |
| B — SQL structure and supported schema rules | PASS | No structural errors. Required columns present. JSON shapes, Linear date formats and gdocs style-run length valid. Provisional MISMATCH on `linear_projects.links_json` (A1, advisory). Confluence and Linear join tables NOT COVERED by the snapshot. |
| C — Dates, relationships and consistency | PASS | No event after the clock. Linear `updated_at`/comment chronology consistent. F1 (a–g) and F2 resolved by deleting or aligning to base. Every new numeric/date/card claim either matches base (GitHub, DocuSign, Deel, Unity, Kapwing, CodeRabbit, Zapier end date, Slack, Intuit, Google Cloud) or has no conflicting base record (A2). |

## 10. Next action and downstream

1. Optional: drop `links_json` from the Linear project insert (A1), so a column mismatch can't roll back the whole script.
2. Proceed to `/prompt`. Because the SQL changed, every later stage that read the earlier SQL needs to run again, in order: `/prompt`, `/hardness`, `/oe`, `/rubric`. Re-derive any expected register values that came from the removed receipts (Vercel, Deel, Google Cloud, dbt, Zapier, QuickBooks, Cursor, DocuSign, Slack, Kapwing). The facts now come from base mail and the Linear comments.

## 11. Evidence limits and provenance

- Static scope only. No live execution, database compatibility, search ranking, Agent visibility or difficulty assessment.
- The schema snapshot is unverified, so mismatches are advisory.
- Sources read this run (all in `Universe_Normal`):
  - Gmail `threads/*.json`: 88,726 files, two complete streaming scans. One covered vendor terms since 2025-11-01 (3,015 hits). The other covered vendor, card-number and invoice terms since 2024-06-01 (7,248 hits). Cited messages were read in full.
  - Plus a `search-many` batch over all thread files: `CINV_00031877` 0 hits, complete.
  - gsheets `data.json`: `/sheets_spreadsheets/141/sheets/2` (HG Costs, full grid), `/sheets/0/grid/0` (HG P&L header), plus a complete `search-many` for vendor names.
  - linear and github `data.json` via `hg_records.py` (complete). Slack `messages/C0ADGSZKR3R/*.json` (Cursor search). Snowflake `snowflake.json`, a streaming grep.
- Reused evidence: revision-4 report sha256 `ad14e77a89a8185d36ea432ff3fa12410ea0ac3214e16ce092db7e122e2c327d`, §5 ledger rows, §6 reference/collision table and §8 base facts, for the 106 byte-identical statements only. Dependencies verified unchanged: statement text, universe manifest, clock, and the Eval/schema/id_contracts/roster/acl hashes.
- Dependencies for reuse by `/prompt`: this SQL hash, the universe manifest above, clock 2026-02-14T00:00Z, and the reference hashes in §1.

### FINAL VERDICT: PASS

Execution status: COMPLETE

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt, then rerun /hardness, /oe and /rubric against this SQL. Optionally drop links_json from the Linear project insert (A1).

Evidence limits: Static review only. Schema snapshot unverified (A1 advisory). Some vendor prices, billing days and SVB-card claims rest only on injected Linear comments, with no base record to confirm or contradict them (A2). No live database or deployment check.
