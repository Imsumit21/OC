# Injection data-integrity review — `injection-static-v2`

## 1. Scope

| Field | Value |
|---|---|
| Review | Chat review for your attempt (6adfee3f27ce6ca81b457137), `/injection`, static audit mode |
| Review version | `injection-static-v2` (evidence contract `stage-evidence-v1`) |
| Actual review time | 2026-10-28T03:14Z |
| Clock | 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal` (hg4-2026-08-31 v37); manifest `Evals/references/universes/normal/universe_manifest.json` sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Input reviewed | Injection SQL, revision 4 (attachment `01_Universe_Inject (2).sql`, saved as `Evals/task_inputs/01_Universe_Inject.sql`), 114,217 bytes, sha256 `cbc2dfed2ec7994c2b76cadbbf914ad250bc690bb25aa859eba047bde01e4966` |
| Previous version | Revision 3, sha256 `e57cf4f4…b393` (FAIL F1–F3). This review re-checks every statement in revision 4 from source; it does not reuse the earlier verdict. |
| References | Eval 0 `e034019b…6eff`; WORKFLOW `ee4cd8e1…504fcd5d`; schema snapshot `injection.json` `31dcb2b4…5151`; schema README `9e320787…eb42`; `id_contracts.json` `fc4711ef…d4682`; ENVIRONMENT `4ffb2b5f…5165`; SEARCH `cab83c61…a5cbc`; roster `3f217451…4575`; acl `e9bca2b3…c9f`; known_base_issues `79b20289…a7b` |

## 2. Input / authority issues

- Only input for this stage is the SQL. It is substantive: 167 statements (BEGIN, 161 INSERT, 4 UPDATE, COMMIT) across gdrive, gdocs, gsheets, confluence, slack, trello, gmail, gcal, github and linear.
- SQL header comments ("Are you planning to inject? Yes", persona line, statement counts, "re-apply this exact SQL") are authoring notes. None mention tool calls, pass rate or gates.
- `known_base_issues.md` lists no normal-universe conflicts. No injected record builds on a listed Snowflake or Confluence conflict.

## 3. Lint (`hg_injection_lint.py`, injection-lint-v1, run on this SQL hash)

Flags: FAIL 0, CHECK 0, INFO 1.

| Flag | Record | Resolution |
|---|---|---|
| INFO `unparsed` (metadata-only media) | line 10, `gdrive.drive_files` `f_4ac7a77383e7317eedcd83` `helpshift_export_2026-02-13.zip` | Accepted. A zip package is metadata-only, as in the base. The injected records only need the file to exist (name, folder, time). It becomes a FAIL only if an OE or rubric row needs the zip's contents. |

A clean lint doesn't replace checks A–C. Those checks found the defects below, which the lint can't see because they come from comparing records with base data.

## 4. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; hash, manifest, review version | NEW, done (revision 4 saved from the attachment, which differed from revision 3) |
| Run lint, resolve flags | NEW, done (1 INFO, resolved) |
| Inventory every statement | NEW, done (167/167, §5) |
| Check A: references, collisions, ID contracts | NEW, **FAIL** (F3) |
| Check B: structure and supported schema rules | NEW, PASS (advisory A1) |
| Check C: dates, relationships, consistency | NEW, **FAIL** (F1, F2) |
| Report and verdict | NEW, done |

Nothing was reused from the earlier report. The earlier P&L, Sherwood-thread and #winddown facts were re-read from source for this run.

## 5. Operation ledger (every statement, execution order)

Lines are physical lines in the saved SQL. "Latest event time" is the last ISO timestamp in the row. Gmail rows are keyed by message id. All rows dated at or before the clock unless noted (the only later values are the gcal start/end plan fields, 2026-03-12).

| # | Line | Table | Op | Record / target | Latest event time or change | Result |
|---|---|---|---|---|---|---|
| 1 | 5 | — | BEGIN | — | — | PASS |
| 2 | 8 | gdrive.drive_files | INSERT | f_1326e66bcabfda8fd29e4a | 2026-02-13T16:38:02Z | PASS |
| 3 | 10 | gdrive.drive_files | INSERT | f_4ac7a77383e7317eedcd83 | 2026-02-13T15:04:51Z | PASS (INFO: metadata-only zip) |
| 4 | 12 | gdrive.drive_files | INSERT | f_768cd23a00c4b12fa0e975 | 2026-02-10T18:05:12Z | PASS |
| 5 | 15 | gdocs.docs_documents | INSERT | f_1326e66bcabfda8fd29e4a | 2026-02-13T16:58:40Z | PASS |
| 6 | 18 | gsheets.sheets_spreadsheets | INSERT | f_768cd23a00c4b12fa0e975 | 2026-02-10T18:31:55Z | PASS |
| 7 | 20 | gsheets.sheets_sheets | INSERT | f_768cd23a00c4b12fa0e975 |  | PASS |
| 8 | 23 | confluence.confluence_pages | INSERT | page_ua_vendor_closeout | 2025-03-18T15:20:00Z | PASS |
| 9 | 25 | confluence.confluence_page_versions | INSERT | ver_64b0ed607e093b18a698fb883a584aa6 | 2025-03-18T15:20:00Z | PASS |
| 10 | 27 | confluence.confluence_pages | INSERT | page_support_after_helpshift | 2026-02-12T20:05:14Z | PASS |
| 11 | 29 | confluence.confluence_page_versions | INSERT | ver_16458585128da06d66a64fa5055bea00 | 2026-02-12T20:05:14Z | PASS |
| 12 | 31 | confluence.confluence_comments | INSERT | comment_support_after_helpshift_c1 | 2026-02-13T15:10:27Z | PASS |
| 13 | 34 | slack.slack_messages | INSERT | b9ef575bec54b095edb75a0fe83580f5 | 2026-02-13T02:14:36.205117Z | PASS |
| 14 | 36 | slack.slack_messages | INSERT | fda86aac9fb55c96ffee4bba3e59cc14 | 2026-02-13T10:02:18.774231Z | PASS |
| 15 | 38 | slack.slack_messages | INSERT | 9e245e76cbaf7f080e1995ec0c4ec30d | 2026-02-13T17:21:07.448213Z | PASS |
| 16 | 39 | slack.slack_messages | UPDATE | 6d8c8d8affd1255b13d8d875f1547e70 | thread_ts_legacy = '1770933601.686309', reply_count = 1, reply_users_c | PASS |
| 17 | 42 | trello.trello_cards | INSERT | 643efb2ab65c5e952575dde5 | 2023-04-18T20:18:50Z | PASS |
| 18 | 44 | trello.trello_actions | INSERT | 643efb2a2768759bdebceec4 | 2023-04-18T20:18:50Z | PASS |
| 19 | 46 | trello.trello_cards | INSERT | 698f48be4ba0affafbf153db | 2026-02-13T15:52:30Z | PASS |
| 20 | 48 | trello.trello_actions | INSERT | 698f48be304fbb37e4e3aafa | 2026-02-13T15:52:30Z | PASS |
| 21 | 51 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856945900224536585 |  | PASS |
| 22 | 53 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com> | 2026-02-12T18:40:12Z | PASS |
| 23 | 65 | gmail.gmail_threads | INSERT | leonard.hayes@harmonygames.co/1856945900224877235 |  | PASS |
| 24 | 67 | gmail.gmail_messages | INSERT | leonard.hayes@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com> | 2026-02-12T18:40:12Z | PASS |
| 25 | 79 | gmail.gmail_threads | INSERT | arthur.blake@harmonygames.co/1856945900225226172 |  | PASS |
| 26 | 81 | gmail.gmail_messages | INSERT | arthur.blake@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com> | 2026-02-12T18:40:12Z | PASS |
| 27 | 93 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856965916492026238 |  | PASS |
| 28 | 95 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | 2026-02-12T23:58:21Z | PASS |
| 29 | 107 | gmail.gmail_threads | INSERT | leonard.hayes@harmonygames.co/1856965916492755786 |  | PASS |
| 30 | 109 | gmail.gmail_messages | INSERT | leonard.hayes@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | 2026-02-12T23:58:21Z | PASS |
| 31 | 121 | gmail.gmail_threads | INSERT | arthur.blake@harmonygames.co/1856965916492023943 |  | PASS |
| 32 | 123 | gmail.gmail_messages | INSERT | arthur.blake@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | 2026-02-12T23:58:21Z | PASS |
| 33 | 134 | gmail.gmail_threads | UPDATE | robert@harmonygames.co/1856965916492026238 | snippet = 'Hi all — one change after our engineers walked through your | PASS |
| 34 | 136 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> | 2026-02-13T18:20:44Z | PASS |
| 35 | 139 | gmail.gmail_threads | UPDATE | leonard.hayes@harmonygames.co/1856965916492755786 | snippet = 'Hi all — one change after our engineers walked through your | PASS |
| 36 | 141 | gmail.gmail_messages | INSERT | leonard.hayes@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> | 2026-02-13T18:20:44Z | PASS |
| 37 | 144 | gmail.gmail_threads | UPDATE | arthur.blake@harmonygames.co/1856965916492023943 | snippet = 'Hi all — one change after our engineers walked through your | PASS |
| 38 | 146 | gmail.gmail_messages | INSERT | arthur.blake@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> | 2026-02-13T18:20:44Z | PASS |
| 39 | 150 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1842984194671106077 |  | PASS |
| 40 | 152 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAowZ1ukjS1ZxLCL4aRt1VM-c-GnNMTNWVQS47OM@mail.gmail.com> | 2025-09-11T16:04:52Z | PASS |
| 41 | 154 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1854998065447619750 |  | PASS |
| 42 | 156 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAghBopAa9b3Is7AhqgT18GKCw29EnA80oVE-7fX@mail.gmail.com> | 2026-01-22T06:40:12Z | PASS |
| 43 | 158 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1855299418849853856 |  | PASS |
| 44 | 160 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CA4Ce6Oa74xUtCgFI1iGnZMieCxsUh90MhimgGu3@mail.gmail.com> | 2026-01-25T14:30:05Z | PASS |
| 45 | 162 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1855909193056957908 |  | PASS |
| 46 | 164 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAv8nvlKROAs2VoeOR_bQeeWQz7g3s8ZMLG3H-EN@mail.gmail.com> | 2026-02-01T08:02:11Z | PASS |
| 47 | 166 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1855912858878482138 |  | PASS |
| 48 | 168 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAL7W0WN5jkixON6h71KIRU6DcLoQyjXVIYONWEZ@mail.gmail.com> | 2026-02-01T09:00:27Z | PASS |
| 49 | 170 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856013526368700009 |  | FAIL F1e (Google Cloud) |
| 50 | 172 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAKjJND_8egfzy8HvU7J5D_J_upaj1ZTvWelJ_yY@mail.gmail.com> | 2026-02-02T11:40:31Z | FAIL F1e (Google Cloud) |
| 51 | 174 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856087468802978676 |  | FAIL F1f (dbt) |
| 52 | 176 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CA6O4h7y3ONTF1SGizuSMRJrSzY6qdpPJSeEtajS@mail.gmail.com> | 2026-02-03T07:15:48Z | FAIL F1f (dbt) |
| 53 | 178 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856105872360240122 |  | FAIL F1g (Zapier) |
| 54 | 180 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAg-xAFLqOwRDSkTyD_arU8SfH5x7vpVAsbcfl-6@mail.gmail.com> | 2026-02-03T12:08:19Z | FAIL F1g (Zapier) |
| 55 | 182 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856280437195390644 |  | FAIL F1d (QuickBooks) |
| 56 | 184 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAvxW79HsTWPxt9LnCKDUGQBjUfyvrRJcQ6W1_0N@mail.gmail.com> | 2026-02-05T10:22:57Z | FAIL F1d (QuickBooks) |
| 57 | 186 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856308191952904709 |  | PASS |
| 58 | 188 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAXSOrUQwguHw7FUjZYmYWAZdozK65cwTBOoyUVJ@mail.gmail.com> | 2026-02-05T17:44:06Z | PASS |
| 59 | 190 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856390427574402743 |  | PASS |
| 60 | 192 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAkZ3dbdoYi7-CRSLIGCQHggFtws4bRsYwq0ch0C@mail.gmail.com> | 2026-02-06T15:31:12Z | PASS |
| 61 | 194 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856563498189712911 |  | PASS |
| 62 | 196 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAHLIUh_nxuC2bAwLx_8d6hgTCAH_dlfrvPqR6v_@mail.gmail.com> | 2026-02-08T13:22:05Z | PASS |
| 63 | 198 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856653066502254886 |  | PASS |
| 64 | 200 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAIoQDHYpNPHXVgnNS8DUmtr__81CmMffz7hcWJv@mail.gmail.com> | 2026-02-09T13:05:44Z | PASS |
| 65 | 202 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856665291850355683 |  | FAIL F1c (Slack) |
| 66 | 204 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAKOOhrKQ5xdFBKDVSuoITfSIhosrVd_8apUKV4c@mail.gmail.com> | 2026-02-09T16:20:03Z | FAIL F1c (Slack) |
| 67 | 206 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856761009013149089 |  | PASS |
| 68 | 208 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAAV70N_MnwWfJSNuqS_HKOnLheApwCzJGSFQi8q@mail.gmail.com> | 2026-02-10T17:41:26Z | PASS |
| 69 | 210 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856859516436705234 |  | PASS |
| 70 | 212 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAxSGYrkpVAs45dr7lAugwSThN-X-ma7vq_V1xAV@mail.gmail.com> | 2026-02-11T19:47:10Z | PASS |
| 71 | 214 | gmail.gmail_threads | INSERT | robert@harmonygames.co/1856962350284960318 |  | FAIL F1a (Kapwing) |
| 72 | 216 | gmail.gmail_messages | INSERT | robert@harmonygames.co/<CAQqiRFJYv8INQuR5F7J2EKiG_htghrsu2H37xDM@mail.gmail.com> | 2026-02-12T23:01:40Z | FAIL F1a (Kapwing) |
| 73 | 219 | gcal.gcal_events | INSERT | evt_2ac66383ee72bbb05a0376 | 2026-02-12T22:40:15Z | PASS |
| 74 | 221 | gcal.gcal_events | INSERT | evt_f1d245d44ceff5a6e049c0 | 2026-02-12T22:40:15Z | PASS |
| 75 | 223 | gcal.gcal_events | INSERT | evt_d1fe12afe85ffbb49bd998 | 2026-02-12T22:40:15Z | PASS |
| 76 | 226 | github.github_pull_requests | INSERT | harmonygames-Games/Combo-Fighters#38 | 2026-02-13T09:41:12Z | PASS |
| 77 | 228 | github.github_branches | INSERT | harmonygames-Games/Combo-Fighters:oliver/final-build-settings |  | PASS |
| 78 | 230 | github.github_commits | INSERT | c769b476f150a76280886f194b4d2186cfd96ca4 | 2026-02-13T09:23:51Z | FAIL F3 (commit identity) |
| 79 | 232 | github.github_pull_request_commits | INSERT | harmonygames-Games/Combo-Fighters#38#c_0 |  | PASS |
| 80 | 234 | github.github_pr_comments | INSERT | harmonygames-Games/Combo-Fighters#38#c_1 | 2026-02-13T09:41:12Z | FAIL F1b (CodeRabbit) |
| 81 | 236 | github.github_timeline_events | INSERT | harmonygames-Games/Combo-Fighters#38#ev_1 | 2026-02-13T09:41:12Z | PASS |
| 82 | 239 | linear.linear_projects | INSERT | 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a | 2026-02-12T23:24:10Z | PASS (advisory A1 links_json) |
| 83 | 241 | linear.linear_project_teams | INSERT | ptm_2183726e36ddf7f8 | 2026-02-12T23:24:10Z | PASS |
| 84 | 243 | linear.linear_project_members | INSERT | pmem_dec4e6c3f1315d8a | 2026-02-12T23:24:10Z | PASS |
| 85 | 245 | linear.linear_project_members | INSERT | pmem_5648d2826ae7a30d | 2026-02-12T23:24:10Z | PASS |
| 86 | 247 | linear.linear_project_members | INSERT | pmem_ca4f8a31e35bad07 | 2026-02-12T23:24:10Z | PASS |
| 87 | 249 | linear.linear_issues | INSERT | ENG-2438 | 2026-02-13T19:05:12Z | PASS |
| 88 | 251 | linear.linear_comments | INSERT | cmt_5da8c3467fc022248fb3 | 2026-02-13T19:05:12Z | PASS |
| 89 | 253 | linear.linear_issues | INSERT | ENG-2439 | 2026-02-13T16:12:40Z | PASS |
| 90 | 255 | linear.linear_comments | INSERT | cmt_96ae7b3689c1d073a2ff | 2026-02-13T16:12:40Z | PASS |
| 91 | 257 | linear.linear_issues | INSERT | ENG-2440 | 2026-02-12T23:52:03Z | PASS |
| 92 | 259 | linear.linear_comments | INSERT | cmt_e8aa0ee7c1bbe08a47c9 | 2026-02-12T23:52:03Z | PASS |
| 93 | 261 | linear.linear_issues | INSERT | ENG-2441 | 2026-02-13T20:41:09Z | PASS |
| 94 | 263 | linear.linear_comments | INSERT | cmt_37c23c5d30cc6597ebe9 | 2026-02-13T20:41:09Z | FAIL F2 (OpenAI) |
| 95 | 265 | linear.linear_issues | INSERT | ENG-2442 | 2026-02-13T20:43:30Z | PASS |
| 96 | 267 | linear.linear_comments | INSERT | cmt_6f994dc8a93d75efb3f8 | 2026-02-13T20:43:30Z | FAIL F2 (Typecast) |
| 97 | 269 | linear.linear_issues | INSERT | ENG-2443 | 2026-02-12T23:55:41Z | PASS |
| 98 | 271 | linear.linear_comments | INSERT | cmt_ec32fbf9ca984b23f7a6 | 2026-02-12T23:55:41Z | PASS |
| 99 | 273 | linear.linear_issues | INSERT | ENG-2444 | 2026-02-13T20:45:02Z | PASS |
| 100 | 275 | linear.linear_comments | INSERT | cmt_497a61c14b69830f198a | 2026-02-13T20:45:02Z | PASS |
| 101 | 277 | linear.linear_issues | INSERT | ENG-2445 | 2026-02-13T20:45:51Z | PASS |
| 102 | 279 | linear.linear_comments | INSERT | cmt_276e0b8a551891ddbdff | 2026-02-13T20:45:51Z | PASS |
| 103 | 281 | linear.linear_issues | INSERT | ENG-2446 | 2026-02-12T23:26:29Z | PASS |
| 104 | 283 | linear.linear_issues | INSERT | ENG-2447 | 2026-02-12T23:57:10Z | PASS |
| 105 | 285 | linear.linear_comments | INSERT | cmt_8ab16d9d7ac715d1c9a7 | 2026-02-12T23:57:10Z | PASS |
| 106 | 287 | linear.linear_issues | INSERT | ENG-2448 | 2026-02-12T23:58:30Z | PASS |
| 107 | 289 | linear.linear_comments | INSERT | cmt_e8ae507893bfdb06c8c7 | 2026-02-12T23:58:30Z | PASS |
| 108 | 291 | linear.linear_issues | INSERT | ENG-2449 | 2026-02-12T23:27:20Z | PASS |
| 109 | 293 | linear.linear_issues | INSERT | ENG-2450 | 2026-02-13T20:47:15Z | PASS |
| 110 | 295 | linear.linear_comments | INSERT | cmt_e3da997ff7b6575fbea0 | 2026-02-13T20:47:15Z | FAIL F2 (Adobe) |
| 111 | 297 | linear.linear_issues | INSERT | ENG-2451 | 2026-02-12T23:27:54Z | PASS |
| 112 | 299 | linear.linear_issues | INSERT | ENG-2452 | 2026-02-12T23:28:11Z | PASS |
| 113 | 301 | linear.linear_issues | INSERT | ENG-2453 | 2026-02-13T16:20:33Z | PASS |
| 114 | 303 | linear.linear_comments | INSERT | cmt_276837877e2b3edc466a | 2026-02-13T16:20:33Z | PASS |
| 115 | 305 | linear.linear_issues | INSERT | ENG-2454 | 2026-02-13T16:24:02Z | PASS |
| 116 | 307 | linear.linear_comments | INSERT | cmt_5a650ef858f3cd5a0410 | 2026-02-13T16:24:02Z | PASS |
| 117 | 309 | linear.linear_issues | INSERT | ENG-2455 | 2026-02-13T19:12:45Z | PASS |
| 118 | 311 | linear.linear_comments | INSERT | cmt_62852832c28dc669e459 | 2026-02-13T19:12:45Z | PASS |
| 119 | 313 | linear.linear_issues | INSERT | ENG-2456 | 2026-02-13T01:30:22Z | PASS |
| 120 | 315 | linear.linear_comments | INSERT | cmt_2b4807a6cf797d1f4886 | 2026-02-13T01:30:22Z | PASS |
| 121 | 317 | linear.linear_issues | INSERT | ENG-2457 | 2026-02-13T01:29:55Z | PASS |
| 122 | 319 | linear.linear_comments | INSERT | cmt_bbdca23f075e9fca5cb8 | 2026-02-13T01:29:55Z | PASS |
| 123 | 321 | linear.linear_issues | INSERT | ENG-2458 | 2026-02-12T23:29:53Z | PASS |
| 124 | 323 | linear.linear_issues | INSERT | ENG-2459 | 2026-02-13T19:15:08Z | PASS |
| 125 | 325 | linear.linear_comments | INSERT | cmt_8f765d1313e9b01a8c22 | 2026-02-13T19:15:08Z | PASS |
| 126 | 327 | linear.linear_issues | INSERT | ENG-2460 | 2026-02-12T23:30:27Z | PASS |
| 127 | 329 | linear.linear_issues | INSERT | ENG-2461 | 2026-02-13T16:26:19Z | PASS |
| 128 | 331 | linear.linear_comments | INSERT | cmt_2238bd7d0a60d8e4f31c | 2026-02-13T16:26:19Z | PASS |
| 129 | 333 | linear.linear_issues | INSERT | ENG-2462 | 2026-02-13T16:29:47Z | PASS |
| 130 | 335 | linear.linear_comments | INSERT | cmt_75b0e4e31a02f9a022bd | 2026-02-13T16:29:47Z | PASS |
| 131 | 337 | linear.linear_issues | INSERT | ENG-2463 | 2026-02-13T20:49:58Z | PASS |
| 132 | 339 | linear.linear_comments | INSERT | cmt_2785f039cfee9d256150 | 2026-02-13T20:49:58Z | PASS |
| 133 | 341 | linear.linear_issues | INSERT | ENG-2464 | 2026-02-13T16:31:05Z | PASS |
| 134 | 343 | linear.linear_comments | INSERT | cmt_5d88052b6f8c1b2fc181 | 2026-02-13T16:31:05Z | PASS |
| 135 | 345 | linear.linear_issues | INSERT | ENG-2465 | 2026-02-12T23:31:52Z | PASS |
| 136 | 347 | linear.linear_issues | INSERT | ENG-2466 | 2026-02-12T23:32:09Z | PASS |
| 137 | 349 | linear.linear_issues | INSERT | ENG-2467 | 2026-02-12T23:32:26Z | PASS |
| 138 | 351 | linear.linear_issues | INSERT | ENG-2468 | 2026-02-12T23:32:43Z | PASS |
| 139 | 353 | linear.linear_issues | INSERT | ENG-2469 | 2026-02-13T16:33:51Z | PASS |
| 140 | 355 | linear.linear_comments | INSERT | cmt_4179664f58817a32a076 | 2026-02-13T16:33:51Z | PASS |
| 141 | 357 | linear.linear_issues | INSERT | ENG-2470 | 2026-02-12T23:33:17Z | PASS |
| 142 | 359 | linear.linear_issues | INSERT | ENG-2471 | 2026-02-12T23:33:34Z | PASS |
| 143 | 361 | linear.linear_issues | INSERT | ENG-2472 | 2026-02-13T00:02:44Z | PASS |
| 144 | 363 | linear.linear_comments | INSERT | cmt_4ca653c559b182ed6ee6 | 2026-02-13T00:02:44Z | FAIL F2 (Office 365) |
| 145 | 365 | linear.linear_issues | INSERT | ENG-2473 | 2026-02-13T16:36:10Z | PASS |
| 146 | 367 | linear.linear_comments | INSERT | cmt_46c0a9358e1df9a6ded4 | 2026-02-13T16:36:10Z | PASS |
| 147 | 369 | linear.linear_issues | INSERT | ENG-2474 | 2026-02-13T00:05:31Z | PASS |
| 148 | 371 | linear.linear_comments | INSERT | cmt_a932354ee5e226971ed1 | 2026-02-13T00:05:31Z | FAIL F1b (CodeRabbit) |
| 149 | 373 | linear.linear_issues | INSERT | ENG-2475 | 2026-02-13T00:06:58Z | PASS |
| 150 | 375 | linear.linear_comments | INSERT | cmt_ed6dab8ad539165c22f1 | 2026-02-13T00:06:58Z | PASS |
| 151 | 377 | linear.linear_issues | INSERT | ENG-2476 | 2026-02-13T16:37:02Z | PASS |
| 152 | 379 | linear.linear_comments | INSERT | cmt_8a420b3635db4a36f750 | 2026-02-13T11:20:37Z | PASS |
| 153 | 381 | linear.linear_comments | INSERT | cmt_af582f63b3fef6e310a7 | 2026-02-13T16:37:02Z | PASS |
| 154 | 383 | linear.linear_issues | INSERT | ENG-2477 | 2026-02-13T01:28:49Z | PASS |
| 155 | 385 | linear.linear_comments | INSERT | cmt_977a0d481cd84d275f08 | 2026-02-13T01:28:49Z | PASS |
| 156 | 387 | linear.linear_issues | INSERT | ENG-2478 | 2026-02-13T00:09:12Z | PASS |
| 157 | 389 | linear.linear_comments | INSERT | cmt_d10e47fd216f16429b45 | 2026-02-13T00:09:12Z | PASS |
| 158 | 391 | linear.linear_issues | INSERT | ENG-2479 | 2026-02-13T01:34:02Z | PASS |
| 159 | 393 | linear.linear_comments | INSERT | cmt_4a019a675b55484b05ec | 2026-02-13T01:34:02Z | PASS |
| 160 | 395 | linear.linear_issues | INSERT | ENG-2480 | 2026-02-13T16:38:44Z | PASS |
| 161 | 397 | linear.linear_comments | INSERT | cmt_e3b5ee0557dca1cb519c | 2026-02-13T16:38:44Z | PASS |
| 162 | 399 | linear.linear_issues | INSERT | ENG-2481 | 2026-02-12T23:36:24Z | PASS |
| 163 | 401 | linear.linear_issues | INSERT | ENG-2482 | 2026-02-13T20:51:20Z | PASS |
| 164 | 403 | linear.linear_comments | INSERT | cmt_c69744b3a98fc7bfd14a | 2026-02-13T20:51:20Z | PASS (advisory A3 Miro) |
| 165 | 405 | linear.linear_issues | INSERT | ENG-2483 | 2026-02-12T23:36:58Z | PASS |
| 166 | 407 | linear.linear_issues | INSERT | ENG-2484 | 2026-02-12T23:37:15Z | PASS |
| 167 | 408 | — | COMMIT | — | — | PASS |

## 6. Check A — Records, references and IDs: **FAIL** (F3)

**References resolved (complete scans, `hg_records.py` and `lookup`):**

| Reference | Source / coverage | Result |
|---|---|---|
| Drive parents `d_e5caf6a8c630421942ee59` (Wind Down, owner `Resource: 7240535625619857401`) and `d_cc3e90160f490686039986` (Arthur's root) | gdrive `data.json` `/drive_files/20868`, `/18538`; 53,866 files | resolve. The new doc and zip copy the Wind Down owner and sharing pattern of its 3 base files (`/25229`, `/26277`, `/29148`). |
| Drive users (Resource, Leonard, Arthur, Robert, Oliver) | `/drive_users`, 25 | all exist |
| Confluence `space_OPS`, parent `page_ops_home`, authors `user_EMPLOYEE_0008` (Frederick Stone, active in Mar 2025, inactive since 2025-10-25), `user_EMPLOYEE_0038` (Leonard), `user_EMPLOYEE_0003` (Oliver) | `confluence_working.json` | all exist |
| Slack users 0025/0003/0038/0016; channels `C0ADGSZKR3R` (#winddown, members include 0016, 0025, 0038) and `C09UHHN6PFZ` (#prototype, members include 0003) | `users.json` 218, `channels.json` 985 | authors are channel members |
| Slack UPDATE target `6d8c8d8affd1255b13d8d875f1547e70` (Leonard's keep list, ts 1770933601.686309, base `reply_count` 0) | `messages/C0ADGSZKR3R/2026-02.json` `/188`; full lookup over 5,353 files / 687,230 messages | exists. The reply count goes 0→1, matching the one injected reply. |
| Trello board `640643a3…318e`, lists To Do/Done, member `PERSON_6094_TRELLO_USER_ID` (Leonard) | trello `data.json` | all exist |
| GitHub repo Combo-Fighters, base branch `develop`, users EMPLOYEE_0003 (Oliver), PERSON_6026 (CodeRabbit org, author of all 417 base CodeRabbit comments), SVC_0321 (bot, actor on those 417 `commented` events) | github `data.json` | all exist and match base conventions |
| Linear `team_ENG`; users Arthur `usr_cc3e…`, Leonard `usr_63ff…`, `usr_Robert`, Oliver `usr_bdf0…`, all ENG team members | linear `data.json` | all exist |
| Gmail sender tokens reused from base: SVC_1177 (Deel), SVC_0251 (Linear), SVC_0982 (Google BigQuery), SVC_2600 (DocuSign), SVC_0124 (Slack), SVC_5771 (Unity invoices), SVC_3550 (Soundly), PERSON_0728 (Sherwood Partners) | first base messages per token: `threads/00013730`, `00000745`, `00003296`, `00013843`, `00000682`, `00006387`, `00013537`, `00016832` | each token belongs to the vendor it's used for |
| New tokens SVC_7702–7712 and PERSON_7731 (Maya, Sunset) | full Gmail text scan, 88,726 files: 0 hits each | new external senders. Sunset's base people are PERSON_0767 (founder) and PERSON_3131 (CTO), so Maya isn't a second account. |

**New-key collisions: none** (all complete): Drive ids 3; gdocs `document_id`; gsheets `spreadsheet_id`; Confluence pages 2, versions 2, comment 1; Slack message ids 3 (687,230 messages); Trello cards 2 and actions 2; Trello `idShort` 68 (free on this board; 67 and 69 are `643efb25…`/`643efb2e…`, which bracket the new `643efb2a…` id) and 456 (base max 455); gcal events 3 and `ical_uid`; GitHub PR #38 (base max #37), branch, commit, PR-commit, comment and timeline ids; Linear project, ENG-2438…2484 by id and identifier (base ENG max 2437, 2,331 ENG issues), 33 comment ids (base has 0 comments); Gmail message ids 26 (104,480 messages) and thread ids 23 (88,726 thread files, root id).

**ID contracts:** Gmail `history_id` NULL on all 23 threads ✓. No Drive `content_path` is set (Google-native doc/sheet, metadata-only zip) ✓. Trello ids encode their own timestamps (`698f48be` = 2026-02-13T15:52:30Z, `643efb2a` = 2023-04-18T20:18:50Z). Gmail thread ids encode their message times.

### F3 — Injected commit names Oliver with placeholder identity strings (FAIL, Check A identity)

- **Record:** line 163–164, `github.github_commits` `c769b476f150a76280886f194b4d2186cfd96ca4`: `author_login`/`committer_login` = `EMPLOYEE_0003_GITHUB_USERNAME` (Oliver), but `author_name`/`committer_name` = `'EMPLOYEE_0003_NAME'` and `author_email`/`committer_email` = `'EMPLOYEE_0003_EMAIL'`.
- **Evidence:** neither string appears anywhere in the base exports (full grep of every service folder, including github `data.json`, Gmail threads and Snowflake: 0 hits). Oliver's base GitHub user (`/users/1`) is `name: "Oliver Brooks"`, `email: "oliver.brooks@harmonygames.co"`, and 1,040 of his 1,065 base commits use exactly that author name and email.
- **Rule:** each author/creator id must resolve to the person the record names (Eval 0 Check A). These two identity fields resolve to nobody.
- **Smallest fix:** set `author_name` and `committer_name` to `'Oliver Brooks'`, and `author_email` and `committer_email` to `'oliver.brooks@harmonygames.co'`.

## 7. Check B — SQL structure and supported schema rules: **PASS** (advisory A1)

- All 161 INSERTs are single-row, with column count equal to value count, no duplicate columns, and every statement terminated. BEGIN…COMMIT wraps the script. The 4 UPDATEs each use a single-row `id =` predicate on an existing or earlier-inserted row.
- Every NOT NULL column without a default is supplied (lint `missing_required` clean), including `linear_issues.state_history_json = '[]'`. No generated column (`text_fts`, `body_text_fts`) is set.
- `*_json` literals parse and match the snapshot's shapes (lint `json_shape` clean). Slack `metadata_json = '{}'`. `grid_json` parses.
- Linear text dates are all `YYYY-MM-DDTHH:MM:SSZ`, and `start_date = '2026-02-12'` (lint `text_time_format` clean). State literals `Todo` (32 base ENG issues use it) and project `started` are valid representations.
- Provisional snapshot comparison: MATCH for every listed column except **A1** below. NOT COVERED by the snapshot: `confluence.confluence_pages`, `confluence_page_versions`, `confluence_comments`, `linear.linear_project_teams`, `linear.linear_project_members`.
- **A1 (advisory, unchanged from revision 3):** `linear.linear_projects.links_json` (line 172) isn't in the snapshot, and base Linear projects have no `links` field. If the live table lacks it, the whole transaction rolls back. Safest: drop `links_json` from that column list. (Revision 4 already dropped the other one, `linear_comments.sequence`.)

## 8. Check C — Dates, relationships and consistency: **FAIL** (F1, F2)

**What passes:**

- **Clock:** no event timestamp is after 2026-02-14T00:00Z. The gcal start/end values (2026-03-12 17:00–17:45Z) are plan fields.
- **Internal consistency:** for all 26 Gmail rows, `internal_date`, `date` and the Date header agree. For all 3 Slack rows, `ts` equals `created_at`. The Slack reply follows its parent. Each Linear comment follows its issue, and every issue's `updated_at` equals its last comment (or creation) time (47 issues, 33 comments checked). The Sunset reply (Feb 13 18:20Z) follows the checklist (Feb 12 23:58Z), with matching In-Reply-To and References.
- **Revision-3 failures, now fixed:**
  - Sherwood email: moved to 2026-02-12T18:40:12Z. Base robert thread `00016832` shows the first call was booked for Thu Feb 12, 8:30 PST (16:30Z), so "As promised on our call" now comes after the call ✓.
  - Linear project description: the dbt→Sentry and Kapwing→Notion mapping is removed. ENG-2457's "dbt is on the kubllc card now, same as github and metabase" matches Arthur's base message (#winddown `/204`: github, `[USERNAME_30019]` = dbt, Metabase). ENG-2478 is Kapwing, which matches Leonard's table (`/187` "Kapwing (Blake)") ✓.
  - Helpshift export zip: now in Drive (created 15:04:51Z), before Oliver's comment (15:10:27Z) ✓.
- **Other facts that check out:** costs tab AF (Dec-25) values: Unity 2172, Helpshift 150, hosting line 86 (= Vercel $86), dbt 100, BigQuery 14.33, Slack 129.5, QuickBooks 115, Gusto 116, Deel 300. The unlabeled 6,250 line sits under Sales/Mkgt (quarterly). Both unlabeled $30 Game Ops lines are person-name tokens. Carta $3,852 in Aug 2025 with renewal 8/15 ✓. Calendly $96 in October ✓. Figma $1,212 in Sep 2025, "good until September 11th" ✓. Sound line 15 = Soundly $10 + Pond5 $5 ✓. No JetBrains invoice after Dec 19, 2025 ✓. Veed is 0 from Dec 2025 ✓. Arthur's KubLLC moves happen after his base message ✓. Soundly, Layer, Zapier, Cursor and Kapwing cancellation comments follow the base #winddown messages ✓. Calendar invite (22:40Z) and Maya's email (23:58Z) come after the Sunset signing (base 21:25–21:28Z) ✓. The Chase card (2023) matches base "our Chase account which is closed" (`/183`).

### F1 — Injected vendor billing records contradict the vendors' own base billing records (FAIL, introduced incompatible facts)

Base Gmail already holds real receipts and notices for these accounts. The injected receipts and notices describe the same Harmony Games accounts with different plans, amounts, cards, charge dates or end dates. One account can't bill on two cycles, so no reading reconciles both. These are the values the task's "by when", "where it stands" and "monthly cost" columns depend on.

| # | Injected record (SQL line) | Base record (file) | Conflict |
|---|---|---|---|
| a | Kapwing cancellation to Robert, 2026-02-12T23:01:40Z, new sender SVC_7711 (l.147–150): "keep access until **March 1, 2026** … Last charge: **$24.00 on February 1, 2026**" | Kapwing's own notice to Arthur, 2026-02-12T22:56:42Z, SVC_0103 (`blake@harmonygames.co_1856962040028188034`): Pro features "until **Wed Feb 25 2026**". Receipts $24.00 paid on the **25th** (Dec 25, 2025 `…1852510867596285211`; Jan 25, 2026 `…1855319224557456875`), card ending 2758. | Two vendor confirmations 5 minutes apart give different end dates (Feb 25 vs Mar 1), and a Feb 1 charge that the base never shows. |
| b | PR #38 CodeRabbit bot comment, 2026-02-13 (l.168): "CodeRabbit **Pro** subscription … canceled and **ends on Feb 26, 2026**. Reviews continue until then". ENG-2474 Arthur comment (l.305): "cancelled. **2 seats at $24**" | CodeRabbit email to Arthur, 2026-02-10 (`…1856750389874631062`): "**Lite (Monthly) $15.00 x 3 Units**, Cancellation date **12-Feb-2026**". Jan 12 payment $45.00 (`…1854150876243727777`). | Plan, seat count, price and end date all differ. By base, the subscription had already ended when the bot says reviews continue. |
| c | Slack invoice to Robert, 2026-02-09 (l.135–138): "$129.50 for February … next bill is on **March 9, 2026**" | Slack renewal to Leonard, 2026-02-03 (`leonard@…1856103558554635848`): "renewed for your team of 12 active users. Your next renewal will be on **3/3/26** … Total **$87.22**" | Second February charge, different amount and different billing cycle. |
| d | QuickBooks receipt to Robert, 2026-02-05 (l.115–118): "$115.00. Payment: **Mastercard x4417**. Next payment … **March 5, 2026**" | Intuit receipt to Leonard (`leonard@…1856211152930380063`): "Invoice date: **02/04/2026** Total: $115.00 Payment method: **MASTER ending in 5348**" | Second February payment, different card and day. The injected card is the SVB card, so which card QuickBooks bills changes. |
| e | Google Cloud email to Robert, 2026-02-02 (l.103–106): "January 2026 invoice **$14.33** (BigQuery). Charged automatically to **Mastercard-4417**" | Google payment receipt to Arthur and Leonard, 2026-02-01 (`blake@…1855947447649217022`): "Your payment amount of **$4.97** … received on Feb 1, 2026. Payment for: Google Cloud … **Mastercard x-2758**". Costs tab, January 2026 column: BigQuery 4.96. | January's amount and card differ. $14.33 is the December figure. |
| f | dbt Cloud receipt to Robert, 2026-02-03 (l.107–110): "$100.00 … Next charge: **March 3, 2026**" | dbt Labs receipt to Leonard (`leonard@…1855983949220444975`): "$100.00 **Paid February 1, 2026** … Feb 1 – Feb 28, 2026 Seats" (monthly receipts on the 1st/2nd since Aug 2025) | Second February charge for the same seat, with a different billing day (next charge Mar 1 vs Mar 3). |
| g | Zapier receipt to Robert, 2026-02-03 (l.111–114): "Zapier **Starter** (monthly) — **$29.99** … renews on **March 3, 2026**" | Zapier email to Leonard, 2026-02-12 (`leonard@…1856958213684823393`): "your **Professional with 750 tasks** has been canceled … until the end of your billing cycle on **February 27, 2026**" | Plan and billing cycle differ. |

- **Rule:** proven incompatible facts introduced by SQL are FAIL under Check C. The base records are vendor system mail. Neither side is a stale human statement or a correction of the other.
- **Smallest fix (per row):** the base already confirms each of these accounts, so the simplest repair is to **delete** the conflicting injected rows and let the task use the base mail. Where you need the record in Robert's inbox, copy the base facts exactly instead:
  - (a) Kapwing: delete l.147–150, or say access until Feb 25, 2026 and last charge $24.00 on Jan 25, 2026.
  - (b) CodeRabbit: reword the bot comment to say the Lite subscription ended Feb 12, 2026 (or drop the PR #38 rows). Change ENG-2474's comment to "3 seats at $15".
  - (c) Slack: delete, or use Feb 3, $87.22, next renewal Mar 3.
  - (d) QuickBooks: delete, or use Feb 4 and card ending 5348, next payment Mar 4.
  - (e) Google Cloud: delete, or use $4.97 on card ending 2758, paid Feb 1.
  - (f) dbt: delete, or use paid Feb 1, next charge Mar 1.
  - (g) Zapier: delete, or use the Professional plan with its cycle ending Feb 27.

  Then re-derive every row of the expected register that used these values.

### F2 — Linear comments state "never paid" / "always 0" facts that the costs tab contradicts (FAIL, introduced incompatible facts)

The January P&L costs tab (`gsheets/data.json` `/sheets_spreadsheets/141`, tab "HG Costs"; months by column position, AF = Dec-25) shows company payments for accounts that injected comments say the company never paid:

| Comment (SQL line) | Costs-tab row | Conflict |
|---|---|---|
| ENG-2472 Arthur (l.297): "we never used it, **the line has always been 0**" | row 54 "Office 365": $12.50 every month Sep 2023 – Dec 2024 | The line wasn't always 0 |
| ENG-2442 Robert (l.201): "free tier for the zm trailer voice, **we never paid**" | row 11 "Typecast.ai (Voice)": $33 every month May 2024 – Jul 2025 | 15 months of company spend |
| ENG-2450 Robert (l.229): "**we never had a company adobe plan**, marcus bennett used his own" | row 26 "Adobe": $35 every month Jan – Oct 2024 | Company Adobe spend |
| ENG-2441 Robert (l.197): "chatgpt plus is on my own card, **the company never paid for it**" | row 8 "OpenAI": $7.02–$50 in Jul 2023 – Apr 2024 | The company line shows OpenAI spend. This one is weaker, since the line could be API use rather than ChatGPT Plus. |

- These accounts likely end up off the register anyway (cancelled before Feb 9). But the comments make checkable claims about the same ledger the task tells the solver to use, and the ledger says otherwise. Nothing in the records explains the gap. A comment calling the line 0 isn't a stale or superseded note; it's simply false against the cited record.
- **Smallest fix:** reword each comment so it agrees with the ledger. For example: "we stopped paying for it after december 2024, the line's been 0 since", "we stopped paying after july, it's free tier now", "the company adobe plan ended in october 2024, marcus uses his own now", "the company stopped paying openai in 2024; chatgpt plus is on my own card". Or pick vendors whose ledger lines really are 0.

### Advisories (not failing)

- **A2 — Miro (ENG-2482):** Robert says "free board, we never paid". Base Gmail has monthly Miro Starter receipts to `brian.foster@harmonygames.co` through Jan 29, 2026 ($12.00 incl. Turkish VAT, period Jan 29 – Feb 28, card ending 0025; `brian@…1855657024896088958`). Miro isn't on the costs tab, and nothing shows card 0025 is a company card, so this isn't proven incompatible. It is a live paid account on a company login, though, and it conflicts with the comment as written. Align the comment, or make sure the task's answer doesn't hinge on it.
- **A3 — Misleading source pointers:** ENG-2479 (1Password) and ENG-2482 (Miro) say "From the #winddown lists", but neither vendor appears anywhere in #winddown (complete channel read; Leonard's table `/187` lists Helpshift, Google, Slack, Intuit, layer, github, dbt, Soundly, Zapier, Carta, Kapwing, cursor, Metabase, coderabbit, gusto, Unity, SVB).
- **A4 — Helpshift quote:** ENG-2439 has Leonard quoting Helpshift ("your subscription ends on February 28, 2026. your final invoice for $300 is attached."). No such Helpshift message exists in the base or the SQL. Helpshift's real Feb 11 reply (`leonard@…1856273045304945702`) acknowledges discontinuation "effective February 29,2025" (sic), invoices run $150/month, and Leonard had written "We paid the outstanding bills". The quote's end date is a fair reading. The $300 figure has no support.
- **A5 — Gusto timing:** Arthur's reply says "gusto bills on the 1st". Base Gusto invoices are paid on the 2nd–4th by bank transfer (Jan invoice: Feb 3 03:08Z, $116). That's an approximate persona claim, not proven wrong. Avoid grading a by-when that needs exactly the 1st.
- **A6 — Context, consistent:** Leonard told Helpshift on Feb 10 "We don't need to export any data". The Feb 12 Confluence page and Sunset's email then require an export, which is explained by the Sunset deal signed Feb 12. Base SVB (Feb 12 20:29Z) offered to cancel the card "asap". The injected Feb 13 Trello card sets closure on Feb 20 after the payoff, which can be read as a later arrangement. Leonard's "last night" for Feb 12 afternoon items is colloquial.
- **A7 — Cosmetic:** the Trello "Chase account closure" card (idShort 68, Done list) has `closed = false`, while neighbours 67 and 69 are `closed = true`. Docusign's ledger shows a single $300 charge in Apr 2024 against an "annual, renews April 8" receipt. Linear's ledger shows no 2025 charge against "went to basic at the renewal". Ledger gaps, not proven conflicts.

### 8a. Snowflake cross-check

Complete scan of `snowflake.json` (2.6 GB, one shared streaming pass) for Kapwing, Zapier, CodeRabbit, QuickBooks, Intuit, "dbt Labs", "Slack Technologies", "Google Cloud", Miro and Typecast: 0 hits each, scan complete. Snowflake has no ledger rows for these vendors, so it neither supports nor contradicts F1/F2. The injected records don't build on a Snowflake or Confluence base conflict.


## 9. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | FAIL | F3: commit `c769b476…` author/committer name and email are `EMPLOYEE_0003_NAME` / `EMPLOYEE_0003_EMAIL`, found nowhere in the base. All other references resolve. Complete collision scans are clean. ID contracts are met. |
| B — SQL structure and supported schema rules | PASS | No structural errors, required columns present, JSON shapes and Linear date formats valid. Provisional snapshot MISMATCH on `linear_projects.links_json` (A1, advisory). Confluence and Linear join tables NOT COVERED by the snapshot. |
| C — Dates, relationships and consistency | FAIL | F1: seven injected vendor receipts/notices contradict the vendors' own base mail (Kapwing, CodeRabbit, Slack, QuickBooks, Google Cloud, dbt, Zapier). F2: four Linear comments say "never paid"/"always 0" where the costs tab shows company spend. Revision-3 F1–F3 are fixed. |

## 10. Next action and downstream

1. Fix F1 by deleting the conflicting injected receipts/notices (the base already confirms these accounts) or copying the base facts exactly. Also fix the CodeRabbit PR comment and ENG-2474's seat count.
2. Fix F2 by rewording the four Linear comments to agree with the costs tab.
3. Fix F3 with Oliver's real name and email on commit `c769b476…`.
4. Preferably drop `links_json` from the Linear project insert (A1), and look at A2–A4.
5. Save the new SQL, then rerun in order: `/injection`, `/prompt`, `/hardness`, `/oe`, `/rubric`. F1 changes the end dates, charge dates, cards and costs for Kapwing, CodeRabbit, Slack, QuickBooks, Google Cloud/BigQuery, dbt and Zapier, so the expected register, OEs and rubric must be re-derived from the corrected data.

## 11. Evidence limits and provenance

- Static scope only. No live execution, database compatibility, search ranking, Agent visibility or difficulty assessment.
- The schema snapshot is unverified; mismatches are advisory.
- Sources read for this review (all in `Universe_Normal`):
  - Gmail `threads/*.json`: 88,726 files. Complete message-id lookup (104,480 messages). Complete root thread-id check. Complete token scan for new senders. Full vendor scan of every message since 2025-08-01 (2,825 hits), with the cited receipts read in full.
  - Slack: `messages/*.json` (5,353 files, complete id lookup), the full #winddown 2026-02 file, `users.json` and `channels.json`.
  - gdrive, gdocs, gsheets, gcal, trello, github and linear `data.json`; confluence `confluence_working.json`. The January P&L is gsheets `/sheets_spreadsheets/141` (HG P&L and HG Costs tabs; months mapped by column position, AF = Dec-25).
  - Snowflake `snowflake.json`: see §8a.
- Dependencies for reuse by `/prompt`: this SQL hash, the universe manifest above, clock 2026-02-14T00:00Z, and the Eval 0, schema and id_contracts hashes in §1. This report is FAIL, so its PASS rows (references, collisions, structure) are reusable only for unchanged statements and must be rechecked after edits.
- `reused_evidence`: none.

### FINAL VERDICT: FAIL

Execution status: COMPLETE

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Fix F1 (delete or align the injected Kapwing, CodeRabbit, Slack, QuickBooks, Google Cloud, dbt and Zapier billing records to the base vendor mail), F2 (reword the Office 365, Typecast, Adobe and OpenAI Linear comments to match the costs tab) and F3 (Oliver's real name and email on commit c769b476); preferably drop links_json (A1). Then rerun /injection, /prompt, /hardness, /oe, /rubric.

Evidence limits: Static review only; schema snapshot unverified (A1 advisory); Miro card ownership (A2) unproven; no live database or deployment check.
