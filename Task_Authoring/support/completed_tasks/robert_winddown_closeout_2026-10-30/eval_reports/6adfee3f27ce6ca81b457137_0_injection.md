# /injection — Injection data-integrity review

## 1. Scope

| Field | Value |
|---|---|
| Review version | `injection-static-v2` (evidence contract `stage-evidence-v1`) |
| Mode | Chat review (attachment), audit only; attempt 6adfee3f27ce6ca81b457137 |
| Actual review time | 2026-10-28T02:44Z |
| Clock | Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal` (source hg4-2026-08-31 v37); manifest `Evals/references/universes/normal/universe_manifest.json` sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Reviewed input | `Evals/task_inputs/01_Universe_Inject.sql` (115,815 bytes) sha256 `e57cf4f4bfa67cf483a98becee179c301a7a413f8c0d0a861c0f75046428b393` |
| References | Eval 0 sha256 `e034019b…6eff`; schema snapshot `injection.json` sha256 `31dcb2b4…5c151` (unverified); `id_contracts.json` sha256 `fc4711ef…4682`; `known_base_issues.md` sha256 `79b20289…3a7b`; WORKFLOW sha256 `ee4cd8e1…fcd5d` |
| Assignment context (not graded here) | Robert, Co-Founder & Creative Director; long-horizon; Feb 14, 2026 |
| Execution | Static only. SQL was parsed, never executed. No base export modified. |

## 2. Input / authority issues

- None blocking. SQL comments (lines 1–4) are evidence of intent only: they describe services and statement counts and contain no grader-facing, padding or tool-call language.
- The SQL contains 66 literal carriage returns inside Gmail `E'…'` body strings (CR before each `\n` escape), which gives CRLF bodies like the base Gmail export. Valid inside PostgreSQL string literals; no finding.

## 3. Lint (`hg_injection_lint.py`, injection-lint-v1)

168 statements (1 BEGIN, 162 INSERT, 4 UPDATE, 1 COMMIT); base lists loaded for confluence, slack, trello, gmail, github, linear.
**Flags: FAIL 0, CHECK 0, INFO 0.** There was nothing to resolve. A clean lint does not replace checks A–C, which follow.

## 4. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; hash, manifest, review version | NEW, done |
| Lint run; every flag resolved | NEW, done (no flags) |
| Full statement inventory | NEW, done (§5, 168 rows) |
| Check A: references and collisions | NEW, PASS |
| Check B: structure and schema | NEW, PASS (advisories A1, A2) |
| Check C: dates, relationships, consistency | NEW, **FAIL** (F1–F3) |
| Report, limits, single verdict | done |

Reused evidence: none. Every check is NEW.

## 5. Operation ledger (every statement, execution order)

Line = physical line of the `VALUES`/`UPDATE` text in the saved SQL. Key = the record's own unique key. "PASS" means that record passed checks A–C.

| # | Line | Table | Op | Key / target | Relevant values | Result |
|---|---|---|---|---|---|---|
| 1 | 5 | — | BEGIN | — | — | PASS |
| 2 | 8 | gdrive.drive_files | INSERT | `f_1326e66bcabfda8fd29e4a` | created_time=2026-02-13T16:38:02Z; owner_email=Resource: 7240535625619857401 | PASS |
| 3 | 10 | gdrive.drive_files | INSERT | `f_768cd23a00c4b12fa0e975` | created_time=2026-02-10T18:05:12Z; owner_email=arthur.blake@harmonygames.co | PASS |
| 4 | 13 | gdocs.docs_documents | INSERT | `f_1326e66bcabfda8fd29e4a` | created_time=2026-02-13T16:38:02Z; owner_email=Resource: 7240535625619857401 | PASS |
| 5 | 16 | gsheets.sheets_spreadsheets | INSERT | `f_768cd23a00c4b12fa0e975` | created_time=2026-02-10T18:05:12Z; owner_email=arthur.blake@harmonygames.co | PASS |
| 6 | 18 | gsheets.sheets_sheets | INSERT | `f_768cd23a00c4b12fa0e975` |  | PASS |
| 7 | 21 | confluence.confluence_pages | INSERT | `page_ua_vendor_closeout` | created_at=2025-03-18T15:20:00Z; author_id=user_EMPLOYEE_0008 | PASS |
| 8 | 23 | confluence.confluence_page_versions | INSERT | `ver_64b0ed607e093b18a698fb883a584aa6` | created_at=2025-03-18T15:20:00Z; author_id=user_EMPLOYEE_0008 | PASS |
| 9 | 25 | confluence.confluence_pages | INSERT | `page_support_after_helpshift` | created_at=2026-02-12T20:05:14Z; author_id=user_EMPLOYEE_0038 | PASS |
| 10 | 27 | confluence.confluence_page_versions | INSERT | `ver_16458585128da06d66a64fa5055bea00` | created_at=2026-02-12T20:05:14Z; author_id=user_EMPLOYEE_0038 | PASS |
| 11 | 29 | confluence.confluence_comments | INSERT | `comment_support_after_helpshift_c1` | created_at=2026-02-13T15:10:27Z; author_id=user_EMPLOYEE_0003 | FAIL F3: cites Drive zip that does not exist |
| 12 | 32 | slack.slack_messages | INSERT | `b9ef575bec54b095edb75a0fe83580f5` | created_at=2026-02-13T02:14:36.205117Z; user_id=EMPLOYEE_0025_SLACK_ID | PASS |
| 13 | 34 | slack.slack_messages | INSERT | `fda86aac9fb55c96ffee4bba3e59cc14` | created_at=2026-02-13T10:02:18.774231Z; user_id=EMPLOYEE_0003_SLACK_ID | PASS |
| 14 | 36 | slack.slack_messages | INSERT | `9e245e76cbaf7f080e1995ec0c4ec30d` | created_at=2026-02-13T17:21:07.448213Z; user_id=EMPLOYEE_0038_SLACK_ID | PASS |
| 15 | 37 | slack.slack_messages | UPDATE | `6d8c8d8affd1255b13d8d875f1547e70` (exists in base/earlier SQL) | thread_ts_legacy = '1770933601.686309', reply_count = 1, rep… | PASS |
| 16 | 40 | trello.trello_cards | INSERT | `67f3f904b65c5e952575dde5` |  | idShort NULL / url "None-…" (A2) |
| 17 | 42 | trello.trello_actions | INSERT | `67f3f9042768759bdebceec4` | date=2025-04-07T16:10:44Z; idMemberCreator=PERSON_6094_TRELLO_USER_ID | PASS |
| 18 | 44 | trello.trello_cards | INSERT | `698f48be4ba0affafbf153db` |  | PASS |
| 19 | 46 | trello.trello_actions | INSERT | `698f48be304fbb37e4e3aafa` | date=2026-02-13T15:52:30Z; idMemberCreator=PERSON_6094_TRELLO_USER_ID | PASS |
| 20 | 49 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1856855303258169133` |  | FAIL F1 (thread of the misdated email) |
| 21 | 51 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com>` | date=2026-02-11T18:40:12Z; from_email=PERSON_0728_EMAIL; subj=Wind-down checklist – Harmony Games | FAIL F1: "As promised on our call" before the Feb 12 call |
| 22 | 53 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1856855303258365823` |  | FAIL F1 (thread of the misdated email) |
| 23 | 55 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com>` | date=2026-02-11T18:40:12Z; from_email=PERSON_0728_EMAIL; subj=Wind-down checklist – Harmony Games | FAIL F1: "As promised on our call" before the Feb 12 call |
| 24 | 57 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1856855303258754588` |  | FAIL F1 (thread of the misdated email) |
| 25 | 59 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com>` | date=2026-02-11T18:40:12Z; from_email=PERSON_0728_EMAIL; subj=Wind-down checklist – Harmony Games | FAIL F1: "As promised on our call" before the Feb 12 call |
| 26 | 61 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1856965916492026238` |  | PASS |
| 27 | 63 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>` | date=2026-02-12T23:58:21Z; from_email=PERSON_7731_EMAIL; subj=Harmony Games – data delivery checklist | PASS |
| 28 | 65 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1856965916492755786` |  | PASS |
| 29 | 67 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>` | date=2026-02-12T23:58:21Z; from_email=PERSON_7731_EMAIL; subj=Harmony Games – data delivery checklist | PASS |
| 30 | 69 | gmail.gmail_threads | INSERT | `arthur.blake@harmonygames.co/1856965916492023943` |  | PASS |
| 31 | 71 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>` | date=2026-02-12T23:58:21Z; from_email=PERSON_7731_EMAIL; subj=Harmony Games – data delivery checklist | PASS |
| 32 | 72 | gmail.gmail_threads | UPDATE | `robert@harmonygames.co/1856965916492026238` (exists in base/earlier SQL) | snippet = 'Hi all — one change after our engineers walked th… | PASS |
| 33 | 74 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com>` | date=2026-02-13T18:20:44Z; from_email=PERSON_7731_EMAIL; subj=Re: Harmony Games – data delivery checkl | PASS |
| 34 | 75 | gmail.gmail_threads | UPDATE | `leonard.hayes@harmonygames.co/1856965916492755786` (exists in base/earlier SQL) | snippet = 'Hi all — one change after our engineers walked th… | PASS |
| 35 | 77 | gmail.gmail_messages | INSERT | `leonard.hayes@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com>` | date=2026-02-13T18:20:44Z; from_email=PERSON_7731_EMAIL; subj=Re: Harmony Games – data delivery checkl | PASS |
| 36 | 78 | gmail.gmail_threads | UPDATE | `arthur.blake@harmonygames.co/1856965916492023943` (exists in base/earlier SQL) | snippet = 'Hi all — one change after our engineers walked th… | PASS |
| 37 | 80 | gmail.gmail_messages | INSERT | `arthur.blake@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com>` | date=2026-02-13T18:20:44Z; from_email=PERSON_7731_EMAIL; subj=Re: Harmony Games – data delivery checkl | PASS |
| 38 | 82 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1842984194671106077` |  | PASS |
| 39 | 84 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAowZ1ukjS1ZxLCL4aRt1VM-c-GnNMTNWVQS47OM@mail.gmail.com>` | date=2025-09-11T16:04:52Z; from_email=SVC_7702_EMAIL; subj=Your Figma receipt – Harmony Games | PASS |
| 40 | 86 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1854830420165651612` |  | PASS |
| 41 | 88 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CA_YQeqxyaSHy54PGUwOBw-Vxw5wppMILLqe1GKR@mail.gmail.com>` | date=2026-01-20T10:15:33Z; from_email=SVC_7710_EMAIL; subj=Sentry receipt – Harmony Games | PASS |
| 42 | 90 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1854998065447619750` |  | PASS |
| 43 | 92 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAghBopAa9b3Is7AhqgT18GKCw29EnA80oVE-7fX@mail.gmail.com>` | date=2026-01-22T06:40:12Z; from_email=SVC_7703_EMAIL; subj=Vercel invoice for Harmony Games | PASS |
| 44 | 94 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1855299418849853856` |  | PASS |
| 45 | 96 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CA4Ce6Oa74xUtCgFI1iGnZMieCxsUh90MhimgGu3@mail.gmail.com>` | date=2026-01-25T14:30:05Z; from_email=SVC_7704_EMAIL; subj=Receipt from Layer | PASS |
| 46 | 98 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1855909193056957908` |  | PASS |
| 47 | 100 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAv8nvlKROAs2VoeOR_bQeeWQz7g3s8ZMLG3H-EN@mail.gmail.com>` | date=2026-02-01T08:02:11Z; from_email=SVC_1177_EMAIL; subj=Deel invoice for February 2026 – Harmony | PASS |
| 48 | 102 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1855912858878482138` |  | PASS |
| 49 | 104 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAL7W0WN5jkixON6h71KIRU6DcLoQyjXVIYONWEZ@mail.gmail.com>` | date=2026-02-01T09:00:27Z; from_email=SVC_0251_EMAIL; subj=Your Linear receipt | PASS |
| 50 | 106 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1856013526368700009` |  | PASS |
| 51 | 108 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAKjJND_8egfzy8HvU7J5D_J_upaj1ZTvWelJ_yY@mail.gmail.com>` | date=2026-02-02T11:40:31Z; from_email=SVC_0982_EMAIL; subj=Google Cloud: your January invoice is av | PASS |
| 52 | 110 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1856087468802978676` |  | PASS |
| 53 | 112 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CA6O4h7y3ONTF1SGizuSMRJrSzY6qdpPJSeEtajS@mail.gmail.com>` | date=2026-02-03T07:15:48Z; from_email=SVC_7705_EMAIL; subj=dbt Cloud payment receipt | PASS |
| 54 | 114 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1856105872360240122` |  | PASS |
| 55 | 116 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAg-xAFLqOwRDSkTyD_arU8SfH5x7vpVAsbcfl-6@mail.gmail.com>` | date=2026-02-03T12:08:19Z; from_email=SVC_7706_EMAIL; subj=Your Zapier receipt | PASS |
| 56 | 118 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1856280437195390644` |  | PASS |
| 57 | 120 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAvxW79HsTWPxt9LnCKDUGQBjUfyvrRJcQ6W1_0N@mail.gmail.com>` | date=2026-02-05T10:22:57Z; from_email=SVC_7707_EMAIL; subj=Your QuickBooks Online payment receipt | PASS |
| 58 | 122 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1856308191952904709` |  | PASS |
| 59 | 124 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAXSOrUQwguHw7FUjZYmYWAZdozK65cwTBOoyUVJ@mail.gmail.com>` | date=2026-02-05T17:44:06Z; from_email=SVC_7708_EMAIL; subj=Your receipt from Cursor | PASS |
| 60 | 126 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1856390427574402743` |  | PASS |
| 61 | 128 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAkZ3dbdoYi7-CRSLIGCQHggFtws4bRsYwq0ch0C@mail.gmail.com>` | date=2026-02-06T15:31:12Z; from_email=SVC_2600_EMAIL; subj=Your Docusign plan renews soon | PASS |
| 62 | 130 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1856563498189712911` |  | PASS |
| 63 | 132 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAHLIUh_nxuC2bAwLx_8d6hgTCAH_dlfrvPqR6v_@mail.gmail.com>` | date=2026-02-08T13:22:05Z; from_email=SVC_7712_EMAIL; subj=Your 1Password Teams receipt | PASS |
| 64 | 134 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1856653066502254886` |  | PASS |
| 65 | 136 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAIoQDHYpNPHXVgnNS8DUmtr__81CmMffz7hcWJv@mail.gmail.com>` | date=2026-02-09T13:05:44Z; from_email=SVC_7709_EMAIL; subj=Your Pond5 annual plan renews on March 2 | PASS |
| 66 | 138 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1856665291850355683` |  | PASS |
| 67 | 140 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAKOOhrKQ5xdFBKDVSuoITfSIhosrVd_8apUKV4c@mail.gmail.com>` | date=2026-02-09T16:20:03Z; from_email=SVC_0124_EMAIL; subj=Your Slack invoice for Harmony Games | PASS |
| 68 | 142 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1856761009013149089` |  | PASS |
| 69 | 144 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAAV70N_MnwWfJSNuqS_HKOnLheApwCzJGSFQi8q@mail.gmail.com>` | date=2026-02-10T17:41:26Z; from_email=SVC_5771_EMAIL; subj=Unity Technologies SF Invoice#: CINV_000 | PASS |
| 70 | 146 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1856859516436705234` |  | PASS |
| 71 | 148 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAxSGYrkpVAs45dr7lAugwSThN-X-ma7vq_V1xAV@mail.gmail.com>` | date=2026-02-11T19:47:10Z; from_email=SVC_3550_EMAIL; subj=Your Soundly subscription has been cance | PASS |
| 72 | 150 | gmail.gmail_threads | INSERT | `robert@harmonygames.co/1856962350284960318` |  | PASS |
| 73 | 152 | gmail.gmail_messages | INSERT | `robert@harmonygames.co/<CAEBA3xPbeRpHpK0fNxaGRudf66PqnAwFljlxpLB@mail.gmail.com>` | date=2026-02-12T23:01:40Z; from_email=SVC_7711_EMAIL; subj=Your Notion plan has been canceled | PASS |
| 74 | 155 | gcal.gcal_events | INSERT | `evt_2ac66383ee72bbb05a0376` | created=2026-02-12T22:40:15Z; organizer_email=leonard.hayes@harmonygames.co | PASS |
| 75 | 157 | gcal.gcal_events | INSERT | `evt_f1d245d44ceff5a6e049c0` | created=2026-02-12T22:40:15Z; organizer_email=leonard.hayes@harmonygames.co | PASS |
| 76 | 159 | gcal.gcal_events | INSERT | `evt_d1fe12afe85ffbb49bd998` | created=2026-02-12T22:40:15Z; organizer_email=leonard.hayes@harmonygames.co | PASS |
| 77 | 162 | github.github_pull_requests | INSERT | `harmonygames-Games/Combo-Fighters#38` | created_at=2026-02-13T09:38:51Z; author_login=EMPLOYEE_0003_GITHUB_USERNAME | PASS |
| 78 | 164 | github.github_branches | INSERT | `harmonygames-Games/Combo-Fighters:oliver/final-build-settings` |  | PASS |
| 79 | 166 | github.github_commits | INSERT | `c769b476f150a76280886f194b4d2186cfd96ca4` | authored_date=2026-02-13T09:23:51Z; author_login=EMPLOYEE_0003_GITHUB_USERNAME | PASS |
| 80 | 168 | github.github_pull_request_commits | INSERT | `harmonygames-Games/Combo-Fighters#38#c_0` |  | PASS |
| 81 | 170 | github.github_pr_comments | INSERT | `harmonygames-Games/Combo-Fighters#38#c_1` | created_at=2026-02-13T09:41:12Z; author_login=PERSON_6026_GITHUB_USERNAME | PASS |
| 82 | 172 | github.github_timeline_events | INSERT | `harmonygames-Games/Combo-Fighters#38#ev_1` | created_at=2026-02-13T09:41:12Z | PASS |
| 83 | 175 | linear.linear_projects | INSERT | `3f0c6a52-ee13-4b1e-68e3-a74bcc33818a` | created_at=2026-02-12T23:24:10Z | FAIL F2: re-labels base redaction tokens; links_json NOT IN SNAPSHOT (A1) |
| 84 | 177 | linear.linear_project_teams | INSERT | `ptm_2183726e36ddf7f8` | created_at=2026-02-12T23:24:10Z | PASS |
| 85 | 179 | linear.linear_project_members | INSERT | `pmem_dec4e6c3f1315d8a` | created_at=2026-02-12T23:24:10Z; user_id=usr_cc3e90160f490686 | PASS |
| 86 | 181 | linear.linear_project_members | INSERT | `pmem_5648d2826ae7a30d` | created_at=2026-02-12T23:24:10Z; user_id=usr_63fffeb4fab5233e | PASS |
| 87 | 183 | linear.linear_project_members | INSERT | `pmem_ca4f8a31e35bad07` | created_at=2026-02-12T23:24:10Z; user_id=usr_Robert | PASS |
| 88 | 185 | linear.linear_issues | INSERT | `ENG-2438` | created_at=2026-02-12T23:24:13Z; creator_id=usr_cc3e90160f490686; title=Unity | PASS |
| 89 | 187 | linear.linear_comments | INSERT | `cmt_5da8c3467fc022248fb3` | created_at=2026-02-13T19:05:12Z; author_id=usr_cc3e90160f490686; issue=ENG-2438 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 90 | 189 | linear.linear_issues | INSERT | `ENG-2439` | created_at=2026-02-12T23:24:30Z; creator_id=usr_cc3e90160f490686; title=Helpshift | PASS |
| 91 | 191 | linear.linear_comments | INSERT | `cmt_96ae7b3689c1d073a2ff` | created_at=2026-02-13T16:12:40Z; author_id=usr_63fffeb4fab5233e; issue=ENG-2439 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 92 | 193 | linear.linear_issues | INSERT | `ENG-2440` | created_at=2026-02-12T23:24:47Z; creator_id=usr_cc3e90160f490686; title=Soundly | PASS |
| 93 | 195 | linear.linear_comments | INSERT | `cmt_e8aa0ee7c1bbe08a47c9` | created_at=2026-02-12T23:52:03Z; author_id=usr_cc3e90160f490686; issue=ENG-2440 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 94 | 197 | linear.linear_issues | INSERT | `ENG-2441` | created_at=2026-02-12T23:25:04Z; creator_id=usr_cc3e90160f490686; title=OpenAI | PASS |
| 95 | 199 | linear.linear_comments | INSERT | `cmt_37c23c5d30cc6597ebe9` | created_at=2026-02-13T20:41:09Z; author_id=usr_Robert; issue=ENG-2441 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 96 | 201 | linear.linear_issues | INSERT | `ENG-2442` | created_at=2026-02-12T23:25:21Z; creator_id=usr_cc3e90160f490686; title=Typecast.ai | PASS |
| 97 | 203 | linear.linear_comments | INSERT | `cmt_6f994dc8a93d75efb3f8` | created_at=2026-02-13T20:43:30Z; author_id=usr_Robert; issue=ENG-2442 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 98 | 205 | linear.linear_issues | INSERT | `ENG-2443` | created_at=2026-02-12T23:25:38Z; creator_id=usr_cc3e90160f490686; title=Unity Asset Store | PASS |
| 99 | 207 | linear.linear_comments | INSERT | `cmt_ec32fbf9ca984b23f7a6` | created_at=2026-02-12T23:55:41Z; author_id=usr_cc3e90160f490686; issue=ENG-2443 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 100 | 209 | linear.linear_issues | INSERT | `ENG-2444` | created_at=2026-02-12T23:25:55Z; creator_id=usr_cc3e90160f490686; title=Veed | PASS |
| 101 | 211 | linear.linear_comments | INSERT | `cmt_497a61c14b69830f198a` | created_at=2026-02-13T20:45:02Z; author_id=usr_Robert; issue=ENG-2444 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 102 | 213 | linear.linear_issues | INSERT | `ENG-2445` | created_at=2026-02-12T23:26:12Z; creator_id=usr_cc3e90160f490686; title=Kling | PASS |
| 103 | 215 | linear.linear_comments | INSERT | `cmt_276e0b8a551891ddbdff` | created_at=2026-02-13T20:45:51Z; author_id=usr_Robert; issue=ENG-2445 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 104 | 217 | linear.linear_issues | INSERT | `ENG-2446` | created_at=2026-02-12T23:26:29Z; creator_id=usr_cc3e90160f490686; title=Hailuo.ai | PASS |
| 105 | 219 | linear.linear_issues | INSERT | `ENG-2447` | created_at=2026-02-12T23:26:46Z; creator_id=usr_cc3e90160f490686; title=JetBrains | PASS |
| 106 | 221 | linear.linear_comments | INSERT | `cmt_8ab16d9d7ac715d1c9a7` | created_at=2026-02-12T23:57:10Z; author_id=usr_cc3e90160f490686; issue=ENG-2447 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 107 | 223 | linear.linear_issues | INSERT | `ENG-2448` | created_at=2026-02-12T23:27:03Z; creator_id=usr_cc3e90160f490686; title=Linear | PASS |
| 108 | 225 | linear.linear_comments | INSERT | `cmt_e8ae507893bfdb06c8c7` | created_at=2026-02-12T23:58:30Z; author_id=usr_cc3e90160f490686; issue=ENG-2448 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 109 | 227 | linear.linear_issues | INSERT | `ENG-2449` | created_at=2026-02-12T23:27:20Z; creator_id=usr_cc3e90160f490686; title=Figma | PASS |
| 110 | 229 | linear.linear_issues | INSERT | `ENG-2450` | created_at=2026-02-12T23:27:37Z; creator_id=usr_cc3e90160f490686; title=Adobe | PASS |
| 111 | 231 | linear.linear_comments | INSERT | `cmt_e3da997ff7b6575fbea0` | created_at=2026-02-13T20:47:15Z; author_id=usr_Robert; issue=ENG-2450 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 112 | 233 | linear.linear_issues | INSERT | `ENG-2451` | created_at=2026-02-12T23:27:54Z; creator_id=usr_cc3e90160f490686; title=Trello | PASS |
| 113 | 235 | linear.linear_issues | INSERT | `ENG-2452` | created_at=2026-02-12T23:28:11Z; creator_id=usr_cc3e90160f490686; title=Dailybot | PASS |
| 114 | 237 | linear.linear_issues | INSERT | `ENG-2453` | created_at=2026-02-12T23:28:28Z; creator_id=usr_cc3e90160f490686; title=Solsten | PASS |
| 115 | 239 | linear.linear_comments | INSERT | `cmt_276837877e2b3edc466a` | created_at=2026-02-13T16:20:33Z; author_id=usr_63fffeb4fab5233e; issue=ENG-2453 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 116 | 241 | linear.linear_issues | INSERT | `ENG-2454` | created_at=2026-02-12T23:28:45Z; creator_id=usr_cc3e90160f490686; title=Singular | PASS |
| 117 | 243 | linear.linear_comments | INSERT | `cmt_5a650ef858f3cd5a0410` | created_at=2026-02-13T16:24:02Z; author_id=usr_63fffeb4fab5233e; issue=ENG-2454 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 118 | 245 | linear.linear_issues | INSERT | `ENG-2455` | created_at=2026-02-12T23:29:02Z; creator_id=usr_cc3e90160f490686; title=AWS | PASS |
| 119 | 247 | linear.linear_comments | INSERT | `cmt_62852832c28dc669e459` | created_at=2026-02-13T19:12:45Z; author_id=usr_cc3e90160f490686; issue=ENG-2455 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 120 | 249 | linear.linear_issues | INSERT | `ENG-2456` | created_at=2026-02-12T23:29:19Z; creator_id=usr_cc3e90160f490686; title=Metabase | PASS |
| 121 | 251 | linear.linear_comments | INSERT | `cmt_2b4807a6cf797d1f4886` | created_at=2026-02-13T01:30:22Z; author_id=usr_cc3e90160f490686; issue=ENG-2456 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 122 | 253 | linear.linear_issues | INSERT | `ENG-2457` | created_at=2026-02-12T23:29:36Z; creator_id=usr_cc3e90160f490686; title=dbt | PASS |
| 123 | 255 | linear.linear_issues | INSERT | `ENG-2458` | created_at=2026-02-12T23:29:53Z; creator_id=usr_cc3e90160f490686; title=BigQuery | PASS |
| 124 | 257 | linear.linear_issues | INSERT | `ENG-2459` | created_at=2026-02-12T23:30:10Z; creator_id=usr_cc3e90160f490686; title=Vercel | PASS |
| 125 | 259 | linear.linear_comments | INSERT | `cmt_8f765d1313e9b01a8c22` | created_at=2026-02-13T19:15:08Z; author_id=usr_cc3e90160f490686; issue=ENG-2459 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 126 | 261 | linear.linear_issues | INSERT | `ENG-2460` | created_at=2026-02-12T23:30:27Z; creator_id=usr_cc3e90160f490686; title=QuickBooks | PASS |
| 127 | 263 | linear.linear_issues | INSERT | `ENG-2461` | created_at=2026-02-12T23:30:44Z; creator_id=usr_cc3e90160f490686; title=Intuit | PASS |
| 128 | 265 | linear.linear_comments | INSERT | `cmt_2238bd7d0a60d8e4f31c` | created_at=2026-02-13T16:26:19Z; author_id=usr_63fffeb4fab5233e; issue=ENG-2461 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 129 | 267 | linear.linear_issues | INSERT | `ENG-2462` | created_at=2026-02-12T23:31:01Z; creator_id=usr_cc3e90160f490686; title=Carta | PASS |
| 130 | 269 | linear.linear_comments | INSERT | `cmt_75b0e4e31a02f9a022bd` | created_at=2026-02-13T16:29:47Z; author_id=usr_63fffeb4fab5233e; issue=ENG-2462 | Carta "aug 14" vs base 8/15 (A3) |
| 131 | 271 | linear.linear_issues | INSERT | `ENG-2463` | created_at=2026-02-12T23:31:18Z; creator_id=usr_cc3e90160f490686; title=Calendly | PASS |
| 132 | 273 | linear.linear_comments | INSERT | `cmt_2785f039cfee9d256150` | created_at=2026-02-13T20:49:58Z; author_id=usr_Robert; issue=ENG-2463 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 133 | 275 | linear.linear_issues | INSERT | `ENG-2464` | created_at=2026-02-12T23:31:35Z; creator_id=usr_cc3e90160f490686; title=Google Workspace | PASS |
| 134 | 277 | linear.linear_comments | INSERT | `cmt_5d88052b6f8c1b2fc181` | created_at=2026-02-13T16:31:05Z; author_id=usr_63fffeb4fab5233e; issue=ENG-2464 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 135 | 279 | linear.linear_issues | INSERT | `ENG-2465` | created_at=2026-02-12T23:31:52Z; creator_id=usr_cc3e90160f490686; title=Slack | PASS |
| 136 | 281 | linear.linear_issues | INSERT | `ENG-2466` | created_at=2026-02-12T23:32:09Z; creator_id=usr_cc3e90160f490686; title=iPostal | PASS |
| 137 | 283 | linear.linear_issues | INSERT | `ENG-2467` | created_at=2026-02-12T23:32:26Z; creator_id=usr_cc3e90160f490686; title=Gusto | PASS |
| 138 | 285 | linear.linear_issues | INSERT | `ENG-2468` | created_at=2026-02-12T23:32:43Z; creator_id=usr_cc3e90160f490686; title=Deel | PASS |
| 139 | 287 | linear.linear_issues | INSERT | `ENG-2469` | created_at=2026-02-12T23:33:00Z; creator_id=usr_cc3e90160f490686; title=Docusign | PASS |
| 140 | 289 | linear.linear_comments | INSERT | `cmt_4179664f58817a32a076` | created_at=2026-02-13T16:33:51Z; author_id=usr_63fffeb4fab5233e; issue=ENG-2469 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 141 | 291 | linear.linear_issues | INSERT | `ENG-2470` | created_at=2026-02-12T23:33:17Z; creator_id=usr_cc3e90160f490686; title=Fondo | PASS |
| 142 | 293 | linear.linear_issues | INSERT | `ENG-2471` | created_at=2026-02-12T23:33:34Z; creator_id=usr_cc3e90160f490686; title=Insurance | PASS |
| 143 | 295 | linear.linear_issues | INSERT | `ENG-2472` | created_at=2026-02-12T23:33:51Z; creator_id=usr_cc3e90160f490686; title=Office 365 | PASS |
| 144 | 297 | linear.linear_comments | INSERT | `cmt_4ca653c559b182ed6ee6` | created_at=2026-02-13T00:02:44Z; author_id=usr_cc3e90160f490686; issue=ENG-2472 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 145 | 299 | linear.linear_issues | INSERT | `ENG-2473` | created_at=2026-02-12T23:34:08Z; creator_id=usr_cc3e90160f490686; title=Layer | PASS |
| 146 | 301 | linear.linear_comments | INSERT | `cmt_46c0a9358e1df9a6ded4` | created_at=2026-02-13T16:36:10Z; author_id=usr_63fffeb4fab5233e; issue=ENG-2473 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 147 | 303 | linear.linear_issues | INSERT | `ENG-2474` | created_at=2026-02-12T23:34:25Z; creator_id=usr_cc3e90160f490686; title=CodeRabbit | PASS |
| 148 | 305 | linear.linear_comments | INSERT | `cmt_a932354ee5e226971ed1` | created_at=2026-02-13T00:05:31Z; author_id=usr_cc3e90160f490686; issue=ENG-2474 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 149 | 307 | linear.linear_issues | INSERT | `ENG-2475` | created_at=2026-02-12T23:34:42Z; creator_id=usr_cc3e90160f490686; title=Cursor | PASS |
| 150 | 309 | linear.linear_comments | INSERT | `cmt_ed6dab8ad539165c22f1` | created_at=2026-02-13T00:06:58Z; author_id=usr_cc3e90160f490686; issue=ENG-2475 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 151 | 311 | linear.linear_issues | INSERT | `ENG-2476` | created_at=2026-02-12T23:34:59Z; creator_id=usr_cc3e90160f490686; title=Zapier | PASS |
| 152 | 313 | linear.linear_comments | INSERT | `cmt_8a420b3635db4a36f750` | created_at=2026-02-13T11:20:37Z; author_id=usr_bdf01b53c6a92c5e; issue=ENG-2476 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 153 | 315 | linear.linear_issues | INSERT | `ENG-2477` | created_at=2026-02-12T23:35:16Z; creator_id=usr_cc3e90160f490686; title=GitHub | PASS |
| 154 | 317 | linear.linear_comments | INSERT | `cmt_977a0d481cd84d275f08` | created_at=2026-02-13T01:28:49Z; author_id=usr_cc3e90160f490686; issue=ENG-2477 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 155 | 319 | linear.linear_issues | INSERT | `ENG-2478` | created_at=2026-02-12T23:35:33Z; creator_id=usr_cc3e90160f490686; title=Notion | desc relies on "Notion" mapping (F2) |
| 156 | 321 | linear.linear_comments | INSERT | `cmt_d10e47fd216f16429b45` | created_at=2026-02-13T00:09:12Z; author_id=usr_cc3e90160f490686; issue=ENG-2478 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 157 | 323 | linear.linear_issues | INSERT | `ENG-2479` | created_at=2026-02-12T23:35:50Z; creator_id=usr_cc3e90160f490686; title=Sentry | desc relies on KubLLC "Sentry" mapping (F2) |
| 158 | 325 | linear.linear_comments | INSERT | `cmt_4a019a675b55484b05ec` | created_at=2026-02-13T01:31:40Z; author_id=usr_cc3e90160f490686; issue=ENG-2479 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 159 | 327 | linear.linear_issues | INSERT | `ENG-2480` | created_at=2026-02-12T23:36:07Z; creator_id=usr_cc3e90160f490686; title=1Password | PASS |
| 160 | 329 | linear.linear_comments | INSERT | `cmt_e3b5ee0557dca1cb519c` | created_at=2026-02-13T01:34:02Z; author_id=usr_cc3e90160f490686; issue=ENG-2480 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 161 | 331 | linear.linear_issues | INSERT | `ENG-2481` | created_at=2026-02-12T23:36:24Z; creator_id=usr_cc3e90160f490686; title=Notarize | PASS |
| 162 | 333 | linear.linear_comments | INSERT | `cmt_5f33dc45f96bbae1e85d` | created_at=2026-02-13T16:38:44Z; author_id=usr_63fffeb4fab5233e; issue=ENG-2481 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 163 | 335 | linear.linear_issues | INSERT | `ENG-2482` | created_at=2026-02-12T23:36:41Z; creator_id=usr_cc3e90160f490686; title=UA Assets | PASS |
| 164 | 337 | linear.linear_issues | INSERT | `ENG-2483` | created_at=2026-02-12T23:36:58Z; creator_id=usr_cc3e90160f490686; title=Miro | PASS |
| 165 | 339 | linear.linear_comments | INSERT | `cmt_84b504bb6386075755fa` | created_at=2026-02-13T20:51:20Z; author_id=usr_Robert; issue=ENG-2483 | PASS (sequence NOT IN SNAPSHOT, A1) |
| 166 | 341 | linear.linear_issues | INSERT | `ENG-2484` | created_at=2026-02-12T23:37:15Z; creator_id=usr_cc3e90160f490686; title=Lucidchart | PASS |
| 167 | 343 | linear.linear_issues | INSERT | `ENG-2485` | created_at=2026-02-12T23:37:32Z; creator_id=usr_cc3e90160f490686; title=Google Ads | PASS |
| 168 | 344 | — | COMMIT | — | — | PASS |
## 6. Check A — Records, references and IDs: **PASS**

**References resolved (complete scans unless noted):**

| Reference | Base record | Coverage |
|---|---|---|
| Drive parents `d_e5caf6a8c630421942ee59` ("Wind Down", owner `Resource: 7240535625619857401`) and `d_cc3e90160f490686039986` (Arthur's root) | gdrive `data.json` `/drive_files` | 53,866 records, complete |
| Drive owner `Resource: 7240535625619857401`, plus Arthur, Leonard and Robert | `/drive_users` (user_bd09066a8bf0, user_cc3e90160f49, user_63fffeb4fab5, user_9f7ba94f7526) | 25, complete |
| Injected doc follows the Wind Down folder convention | The 3 base files in the folder (Termination Notices, Employee Termination Letters, Task List) are all owned by the Resource account and shared with the three founders. The injected doc matches. | folder children scan complete |
| Confluence `space_OPS`, parent `page_ops_home`, authors `user_EMPLOYEE_0038` (Leonard Hayes), `user_EMPLOYEE_0008` (Frederick Stone, active when the 2025-03-18 page was written; inactive since 2025-10-25), `user_EMPLOYEE_0003` (Oliver Brooks) | `confluence_working.json` | complete |
| Slack users 0025 (Arthur), 0003 (Oliver), 0038 (Leonard), 0016 (Robert); channels `C0ADGSZKR3R` #winddown (members 0016/0025/0038) and `C09UHHN6PFZ` #prototype (member 0003) | `users.json`, `channels.json` | complete |
| Slack UPDATE target `6d8c8d8affd1255b13d8d875f1547e70` (Leonard's keep list, 2026-02-12T22:00:01Z) | `messages/C0ADGSZKR3R/2026-02.json` `/188`; base reply_count 0, no replies | all 5,353 message files |
| Trello board `640643a3fd8f3ca308d9318e`, lists To Do / Done, creator `PERSON_6094_TRELLO_USER_ID` (Leonard Hayes) | trello `data.json` | complete |
| Gcal calendars for leonard, robert, arthur | gcal `/calendars` | complete |
| GitHub repo Combo-Fighters, base branch `develop`; users EMPLOYEE_0003 (Oliver), PERSON_6026 (the org that authors all 417 base CodeRabbit comments), SVC_0321 (the bot that is the actor on base `commented` events) | github `data.json` | complete |
| Linear `team_ENG`; users usr_cc3e90160f490686 (Arthur), usr_63fffeb4fab5233e (Leonard), usr_Robert, usr_bdf01b53c6a92c5e (Oliver); all four are team_ENG members | linear `data.json` | complete |
| Gmail senders reused from the base: SVC_0124 (Slack), SVC_0251 (Linear), SVC_0982 (Google Cloud/BigQuery), SVC_1177 (Deel), SVC_2600 (Docusign), SVC_3550 (Soundly), SVC_5771 (Unity invoices), PERSON_0728 (Sherwood Partners, base thread `threads/00016832.json`) | Gmail threads | first matches read; each identity matches the vendor named in the injected record |
| New tokens SVC_7702–7712 (Figma, Vercel, Layer, dbt, Zapier, QuickBooks, Cursor, Pond5, Sentry, Notion, 1Password) and PERSON_7731 (Maya, Sunset) | Not present in base Gmail (88,726 files, complete) | New external senders. Sunset's base contacts are different people (PERSON_0767, PERSON_3131), and no base "Maya" works at Sunset, so this is not a second account. |

**New-key collisions: none.** Drive/Docs/Sheets ids; Confluence pages, versions and comment; 3 Slack message ids (687,230 messages); 2 Trello cards, 2 actions, idShort 456 (base max 455); 3 gcal events and ical_uid; GitHub PR #38 (base max #37; no repo issues), branch, commit, PR-commit, comment, timeline ids; Linear project, ENG-2438…ENG-2485 by id and identifier (base ENG max 2437; contiguous), 32 comment ids (base has 0 comments); 24 Gmail thread ids (grep over all thread files) and 27 message ids (104,480 messages, complete). No duplicate keys within the SQL.

**ID contracts:** Gmail `history_id` is NULL on all 24 threads ✓. No `content_path` was injected. The Google Doc has a `docs_documents` row with a non-empty body, and the sheet has a `sheets_sheets` grid, so both are readable ✓. One account per person ✓. Every author/creator id resolves to the person named.

## 7. Check B — SQL structure and supported schema rules: **PASS** (advisories)

- All 162 INSERTs parse, with column count equal to value count, no duplicate columns, and every statement terminated. BEGIN…COMMIT wraps everything. The 4 UPDATEs have single-row id predicates.
- Every NOT NULL column without a default is supplied, including `linear_issues.state_history_json = '[]'`. No generated columns (`text_fts`, `body_text_fts`) are set.
- Every `*_json` literal parses with the snapshot's shape (`metadata_json '{}'`, arrays where required). `grid_json` parses.
- Linear dates are all `YYYY-MM-DDTHH:MM:SSZ` and `start_date '2026-02-12'` ✓. State literals (`Todo`, project `started`) match base representations.
- Snapshot comparison (provisional): MATCH for every column except **A1**. NOT COVERED: `confluence.*`, `linear.linear_project_teams`, `linear.linear_project_members`.

## 8. Check C — Dates, relationships and consistency: **FAIL**

No event timestamp is after the clock. Calendar start/end (2026-03-12) are plan fields. Slack `ts` equals `created_at` on all 3 messages. Gmail `internal_date`, `date`, Date header, Subject and Message-ID agree on all 27 messages. Replies follow their parents, and every Linear comment follows its issue with the issue's `updated_at` equal to the comment time. The P&L claims check out against the base: costs tab AF header reads 2024-12-25 and the HG P&L tab AF reads 2025-12-25; the hosting subtotal (348.33) equals P&L COGS; the unlabeled hosting line is 86; the unlabeled quarterly 6,250 line sits under Sales/Mkgt; there are two unlabeled $30 Game Ops lines. The Sunset signing (base Feb 12 21:29–22:22Z), the calendar invite (22:40Z) and Maya's email (23:58Z) are in order. Soundly, Layer, Helpshift, Carta-terminations and CodeRabbit comments agree with the base #winddown messages.

### F1 — Sherwood email refers to a call that hadn't happened yet (FAIL, impossible chronology)

- **Records:** lines 48–59: the three thread rows and three message copies of "Wind-down checklist – Harmony Games", dated `2026-02-11T18:40:12Z`, body "As promised on our call, here is the checklist…".
- **Base evidence:** `gmail/threads/00016832.json` (Leonard ↔ PERSON_0728, Sherwood Partners): first contact 2026-02-09; on 2026-02-11T04:25Z Sherwood proposes "830am PST" on Thursday; Leonard confirms "see you at 8:30am on Thursday"; the invite is accepted at 04:28:45Z. So the first call was Thu 2026-02-12 16:30Z. #winddown also has 2026-02-11T15:39:38Z Leonard: "We are talking to him tomorrow." and 2026-02-12T15:43:55Z: "Let's talk to sherwood today and then decide".
- **Effect:** the email presents the call as already done about 22 hours before it took place.
- **Smallest fix:** in all three copies, move the email after the call, e.g. `date '2026-02-12T18:40:12Z'`, `internal_date 1770921612000`, Date header `Thu, 12 Feb 2026 18:40:12 +0000`. Alternatively, drop "As promised on our call".

### F2 — Linear project description re-labels base redaction tokens as different vendors (FAIL, introduced contradiction)

- **Record:** line 175, `linear.linear_projects` `3f0c6a52-…818a`, description by Arthur. ENG-2478 and ENG-2479 (lines 319, 323) depend on it.
- **(a) "the third account in my KubLLC message is Sentry".** Base #winddown 2026-02-12T23:00:32Z (`messages/C0ADGSZKR3R/2026-02.json` `/204`), Arthur: "I'll be moving github, [USERNAME_30019], and Metabase to my KubLLC card." The third account is Metabase. Across base Slack, `[USERNAME_30019]` is **dbt**: `D0695BE0AKT/2025-08.json` `/42` links to `…dbt.com/develop/…`; `C069FF9Q57S/2023-12.json` `/37` says it "manages your database by maintaining 'create view' queries in bigquery"; `/66` says "one for Metabase and one for [USERNAME_30019]"; `D0695BE0AKT/2025-10.json` `/53` says "force deploy… then metabase re-sync". The #winddown table (`/187`) lists "[USERNAME_30019] (keep it until [Robert] stops caring about data)", which mirrors Leonard's "keep Metabase and dbt until <@Robert> stops caring" (`/190`). No other KubLLC message exists (complete Slack search: 2 hits, the other from 2023). So the base says dbt moved to Arthur's card. The injection says Sentry did, and says nothing about dbt.
- **(b) "In Leonard's Feb 11 cancel list the one between Zapier and Cursor is Notion".** Base `/74` (2026-02-11T19:55:15Z): "Zapier, [PERSON_NAME_20852], cursor, coderabbit we should just cancel". Leonard's table (`/187`) gives Blake's (Arthur's) items as "Kapwing (Blake)", "cursor (Blake)", "coderabbit (Blake)", matching his assignment "<@Arthur> to cancel [PERSON_NAME_20852], coderabbit, cursor" (`/190`). Arthur then reports "cursor and [PERSON_NAME_20852] cancelled" (`/203`). The token is Kapwing, not Notion.
- **Effect:** the SQL writes a mapping into the data that conflicts with what base Slack shows for which accounts were moved (dbt) and cancelled (Kapwing). That changes the Action and Status values for dbt, Sentry, Notion and Kapwing.
- **Smallest fix:** remove or correct both sentences, for example "the second account in my KubLLC message is dbt" and "the one between Zapier and Cursor is Kapwing". Then give Sentry and Notion sources that exist: keep the ENG-2479 comment "sentry is on the kubllc card now", but change its description away from "From Arthur's KubLLC message", or add a separate Arthur message moving Sentry. Change ENG-2478's description to a source such as the Notion cancellation email or old receipts. Decide how dbt (moved per base) and Kapwing (cancelled per base; it has no issue) should appear. The OEs and rubric must follow whatever you choose.

### F3 — Confluence comment cites a Drive export that doesn't exist (FAIL, broken cross-service fact)

- **Record:** line 29, `confluence.confluence_comments` `comment_support_after_helpshift_c1` (Oliver, 2026-02-13T15:10:27Z): "exported to the Wind Down folder today (helpshift_export_2026-02-13.zip)".
- **Evidence:** a full search of 53,866 `drive_files` for "helpshift_export" returns 0 hits. The Wind Down folder holds only 3 base files plus the injected conventions doc, and no SQL statement adds the zip.
- **Effect:** the conventions doc makes the Helpshift deadline depend on whether "an export … still has to happen". The comment says it did, but Drive shows no export.
- **Smallest fix:** add a `gdrive.drive_files` row for `helpshift_export_2026-02-13.zip` (mime `application/zip`, parent `d_e5caf6a8c630421942ee59`, owner matching the folder convention, shared with the founders, created/modified about 2026-02-13T15:05Z, before the comment). Metadata-only is acceptable for a package file per Eval 0. Alternatively, reword the comment so it doesn't name a Drive file.

### Advisories (not failing)

- **A1 (Check B, provisional):** `linear.linear_projects.links_json` (line 174) and `linear.linear_comments.sequence` (32 inserts) are not in the schema snapshot. The base Linear project export also has no `links` field, and the base has no comments to compare against. If either column doesn't exist on the live database, the whole BEGIN…COMMIT rolls back. Safest course: drop both columns from the column lists unless you've confirmed they exist.
- **A2:** Trello "Chase account closure" card (line 40) has `idShort NULL` and url `…/None-chase-account-closure`, while all 449 base cards on this board have an idShort. Not an ID-contract field. Consider giving it a real idShort and url slug.
- **A3:** ENG-2462 comment (Leonard) says Carta "renews aug 14". Leonard's base table (`/187`) says "Carta (renewal 8/15 …)". This could be charge date versus renewal date, so it isn't proven incompatible, but aligning to 8/15 removes ambiguity on a by-when date.
- **A4:** Leonard's request says "last night" for the Linear project (Feb 12, 15:24 PT) and the keep list (14:00 PT). This is colloquial and not a defect.
- Base-data conflicts: `known_base_issues.md` lists none for the normal universe. The injected Confluence pages don't build on a known conflict.

## 9. Results

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | All references resolve; complete collision scans clean; ID contracts met. |
| B — SQL structure and supported schema rules | PASS | No structural errors. Provisional snapshot MISMATCH on `links_json` / `sequence` (A1, advisory). Confluence and Linear join tables NOT COVERED. |
| C — Dates, relationships and consistency | FAIL | F1 chronology (Sherwood email before the call); F2 re-labelled redaction tokens (dbt → Sentry, Kapwing → Notion); F3 missing Drive export. |

## 10. Next action and downstream

Fix F1–F3 (and preferably A1), save the new SQL, then rerun in order: `/injection`, `/prompt`, `/hardness`, `/oe`, `/rubric`. F2 changes the expected handling of dbt, Sentry, Notion and Kapwing, so the OEs and rubric must be rechecked against the corrected data.

## 11. Evidence limits and provenance

- Static scope only: no live execution, database compatibility, search ranking, Agent visibility or difficulty assessment.
- Schema snapshot is unverified. Snapshot mismatches are advisory.
- Vendor sender tokens: base identity was confirmed from the first matching messages of each token, not from every occurrence.
- Sources: Gmail `threads/*.json` (88,726 files: message-id lookup complete, thread-id grep complete, token search complete for new tokens); Slack `messages/*.json` (5,353 files) and `users.json`/`channels.json`; gdrive/gdocs/gsheets/gcal/trello/linear `data.json`; github `data.json`; confluence `confluence_working.json`; gsheets Jan-2026 P&L (`/sheets_spreadsheets/141`, HG P&L and HG Costs tabs). Snowflake was searched for "Carta" (0 hits, complete).
- Dependencies for reuse by `/prompt`: this SQL hash, universe manifest above, clock 2026-02-14T00:00Z, Eval 0 / schema / id_contracts hashes above.

### FINAL VERDICT: FAIL

Execution status: COMPLETE

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Fix F1 (redate the Sherwood email to after the Feb 12 16:30Z call), F2 (correct the dbt/Kapwing mappings in the Linear project description and re-source ENG-2478/2479) and F3 (add the Helpshift export file to Drive or reword the comment); drop links_json/sequence unless confirmed; then rerun /injection, /prompt, /hardness, /oe, /rubric.

Evidence limits: Static review only; schema snapshot unverified (A1 advisory); vendor sender identities confirmed from first matches per token.
