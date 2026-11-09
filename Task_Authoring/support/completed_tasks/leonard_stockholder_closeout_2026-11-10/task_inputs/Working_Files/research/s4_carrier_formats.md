# S4: carrier formats and record plan buildability (Leonard stockholder close-out)

Facts and locators only. No prompt, Oracle Event or rubric text. FACT vs INFERENCE marked. Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal). Status: complete 2026-11-07.

## 0. Verdict

**The record plan is buildable as ten schemas, with three things to settle first.**

1. **Ids are minted and clean.** ENG-2438 to ENG-2463, one project id, one folder, two Docs, one Sheet, one deck: 0 collisions on complete scans. Gmail thread numbers are minted from the `(ms << 20)` rule. Nothing is blocked.
2. **Row floor.** A realistic count is about 105 rows against the 120 floor. About 15 more real rows are needed, most likely second comments on Linear issues. See §I.
3. **Drafts stay unproven.** No `gmail_*draft*` call appears in 120 stored trajectories, Leonard's mailbox has 0 DRAFT messages, and `gmail_get_draft` is not in the catalog. The live text gives four readback routes. Pre-check it (§H) before a row depends on it.
4. **KPMG seed departs from base in one forced way.** Base bodies say "see the attached confirmation", and attachments return no bytes, so the FY25 items and as-of date must be in the body. It sits beside the FY23 and FY24 threads as a new root from `PERSON_3088`.
5. **Sunset has no legal or customer-success person in base.** Use `PERSON_2888` relaying legal, in the `Sunset: ...` form, beside the main thread. The SOW PDF is still unread.
6. **Three corrections to earlier work.** Trello `/cards/801` is not closed: it is open in the Done list, and useful as a free control. Ask_Carriers' Gmail `limit`/`offset` and Slack `channel` parameters are stale. The catalog's `slack_send_message` params (`channel`, `text`) differ from every stored call (`channel_id`, `message`).
7. **Cheap real difficulty found.** `reply_all` defaults to false and 207 of 213 stored replies went to the sender only, while KPMG's body asks for reply-all. Sheet cells and slide text have no word search. `gcal_list_events` spilled in 18 of 20 calls and Leonard's calendar holds 190 dead recurring masters, so a seeded event is found only by `gcal_search_events`.
8. **Weakest jobs.** Slides (LLC's deck had 0 reads in 6 runs) and Contacts. With exactly ten schemas neither can drop, so keep them honest and supporting, with no graded fact only there. Linear comments are always read, so they buy calls, not misses.

## A. Linear

Sources: base `linear/data.json` through hg.py (3,852 issues, 41 users, 5 teams, 2 projects, 0 comments, 76 memberships); `robert_llc_takeover_2026-11-06/task_inputs/01_Universe_Inject.sql` lines 141-290; LLC baseline runs 1-6 for real tool output; live tool text in `Audit_2026-10-30_Live_Sandbox/state_full.json`.

**How the LLC task seeded it (FACT, /injection PASS on all four revisions).**
- 1 `linear_projects` row, 37 `linear_issues` rows, 37 `linear_comments` rows. No `linear_teams`, `linear_project_teams`, `linear_project_members` or `linear_team_memberships` row, and no `issue_counter` bump.
- Project row columns: `id, team_id, name, summary, description, lead_id, priority, state, start_date, target_date, labels_json, links_json, is_archived, created_at, updated_at`. Values: `team_ENG`, `lead_id` = Leonard, `priority` 0, `state` 'started', `start_date` '2026-02-12', `labels_json` '[]', `links_json` '[]', `is_archived` false. The rule text lives in `description`. `uuid`, `icon`, `color` omitted (color has the only default).
- Issue row columns (all 27, in order): `id, project_id, team_id, parent_id, assignee_id, creator_id, state_id, cycle_id, identifier, number, title, description, priority, estimate, due_date, started_at, completed_at, canceled_at, archived_at, time_in_status_minutes, labels_json, links_json, relations_json, state_history_json, is_archived, created_at, updated_at`. All 37 were `state_id` 'Backlog', no assignee, no stamps, `labels_json` / `links_json` / `relations_json` / `state_history_json` all '[]', `priority` 0.
- Comment row columns: `id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at`. `id` = `comment_<32 hex>`, which is also the form the runtime mints (`comment_ee81a6bba9194449a6603e9d725960ed` in a run). `sequence` omitted. Authors: 27 Leonard, 10 Arthur, so a co-founder's comment is a tested non-owner voice.
- Stamps: project Feb 12 23:24Z, issues from 23:25Z at 20 s spacing, comments from Feb 13 00:24Z; each issue's `updated_at` = its newest comment.

**Team and id series.**

| Team | Id series | Max number in base | Next free | Open states seen in base | Last created | Note |
|---|---|---|---|---|---|---|
| `team_ENG` Engineering | `ENG-n` | 2437 | **2438** | Backlog 34, Todo 32, Bugs 22, PR 14, In Progress 7, Validation 4, Regression 2 | 2025-11-07 | 284 of Leonard's 315 created issues; LLC precedent |
| `team_ZOM` | `ZOM-n` | 672 | 673 | Backlog 51, Todo 54, In Validation 14, In Progress 6, Regression 4 | 2025-11-01 | |
| `team_ART` | `ART-n` | 792 | 793 | | 2025-08-26 | Claire's task seeded ART-808 upward |
| `team_DES` | `DES-n` | 312 | 313 | | 2025-05-07 | |
| `team_EPI` | `EPI-n` | 28 | 29 | | 2024-03-14 | |

Recommend `team_ENG`: Leonard is a member of all five, it is his home team, and it is the shape that has already passed `/injection`, `/prompt` and six baseline runs.

**Workflow states for ENG (FACT, `linear_list_issue_statuses(team="ENG")` in an LLC run; `linear_workflow_states` is not writable, so this list is fixed):**
Backlog `state_5629b9d6559f5f8c` (backlog) · Todo `state_f5f67279df1a52c2` (unstarted) · Bugs `state_1501c3f74ff95c8b` (unstarted) · In Progress `state_02676a4c61d154e7` (started) · PR `state_4c86d6bbbffa5021` (started) · Regression `state_89357fc048765157` (started) · Validation `state_de03c253d62e59bc` (started) · Done `state_f71945f4d2e95895` (completed) · Canceled `state_7e56143481a65571` (canceled) · Duplicate `state_e8f9e20c43f55ad8` (duplicate, 0 issues). `state_id` in the SQL holds the state **name**; the read resolves it (the seeded 'Backlog' rows raised the count from 34 to 71).

**Lifecycle rules (FACT: `sql_lint.py::linear_lifecycle`, measured on base).**

| `state_id` | `started_at` | `completed_at` | `canceled_at` |
|---|---|---|---|
| Backlog, Todo, Bugs | must be NULL | must be NULL | must be NULL |
| In Progress, PR, Validation, Regression | set (all 41 base rows) | NULL | NULL |
| Done | optional (923 of 3,153 have none) | required | NULL |
| Canceled, Duplicate | optional | NULL | required |

Also created <= each stamp <= updated, started <= completed. Text dates exactly `YYYY-MM-DDTHH:MM:SSZ`, dates `YYYY-MM-DD`. A comment dated after the issue was closed is a FAIL (2026-10-23 guideline): seed comments on Done or Canceled issues before the stamp. `state_history_json` '[]' on a new issue.

**What the reads return (FACT, real output).**
- `linear_list_projects(query, ...)`: row with `id, uuid, icon, color, name, summary, description` (description came back whole in LLC, where it is under 448 characters; no cap is stated for projects), `url, createdAt, updatedAt, startedAt, completedAt, canceledAt, startDate, targetDate, priority{value,name}, labels, lead{id,name}, leadTeam, status{id,name,type}, teams[], isArchived`. A seeded `state` 'started' reads as `status {name:"started", type:"started"}`.
- `linear_list_issues(project, team, state, assignee, label, query, limit<=250 default 50, cursor, orderBy default updatedAt, maxDescriptionChars, fields, ...)`: returns `{issues:[...], hasNextPage}`. Row keys: `id, uuid, identifier, number, title, description, priority{value,name}, estimate, url, gitBranchName, createdAt, updatedAt, archivedAt, completedAt, startedAt, canceledAt, dueDate, status, statusType, labels, links, createdBy, createdById, assignee?, assigneeId?, project, projectId, team, teamId, timeInStatusMinutes, isArchived`. Description cut at 448 characters by default, with `descriptionTruncated`/`descriptionLength`; `maxDescriptionChars` lifts it. **No comments.** `query` matches title and description only, any word. So one call returns every issue's title, state and description for the project.
- `linear_get_issue(id, maxDescriptionChars, includeRelations)`: same row plus `attachments` and `stateHistory`; no comments.
- `linear_list_comments(issueId, orderBy, limit<=250 default 50, cursor)`: `{comments:[{id, body, attachments, createdAt, updatedAt, parentId, resolvedAt, quotedText, author{id,name}, onBehalfOf, issueId, isEdited}], hasNextPage}`. Per issue, no bulk call exists (`linear_show_data` is gone from the live catalog).

**Consequences for the design.**
- FACT: the 60 stored baseline runs made 5,475 `linear_list_comments` calls in 48 runs; all 6 LLC runs read every issue's comments (222 calls for 37 issues). Comments are a reliable per-record read, so they buy call count (26 forced calls), not misses. A fact in a comment will be read and applied.
- FACT: anything in a title or description arrives in one `linear_list_issues` call, so per-holder facts belong in comments, per `--no-leak`.
- FACT: `linear_create_issue` in a run took ENG-2475 with 37 seeded rows, which is max + 1, so no `issue_counter` update is needed and a run cannot collide with the seeds.
- FACT: `linear_update_issue` writes `state`, `assignee`, and appends `stateHistory`; `linear_create_comment(issueId, body, parentId)`; `linear_update_comment` also exists.
- Honesty note: of 3,852 base issues, a word search of titles and descriptions for investor, stockholder, shareholder, Carta, cap table, legal, attorney, audit, tax, finance, payroll, invoice, contract, KPMG, Griffin and Sunset finds 4 hits, and only one is real admin work: ENG-392 "Contact Gusto About tax reporting" (2023, Done). So Linear is a product tracker, and the holder project would be its first investor-side project. The LLC project was equally new, in the same week and by the same author, and scored `/prompt` 5, so it is defensible, but the reason for putting holders in Linear should be in the seeded text. Last base activity is 2026-01-28 and Leonard's last created issue is 2025-11-01, so a Feb 12-13 project is a visible recency jump, as LLC's was.

**Can issue ids be minted now? Yes.** ENG is the only series touched and a run's own `linear_create_issue` takes max + 1, so nothing depends on later steps. Numbers in the base run to 2437 with gaps below that, so use 2438 upward rather than a gap.

**Minted ids (collision-checked).** `hg.py search lookup linear --file data.json --pointer /issues` over 27 ids: `records_checked` 3852, `scan_complete` true, 0 matches. `hg.py records` on `id`, `identifier`, `number` (/issues, 3852 records each) and `id` (/projects, 2 records): 0 matches, complete. Text scan for `ENG-244`, `ENG-245`, `ENG-246`, `ENG-2438`, `ENG-2439` in Slack 2025-26 and GitHub `data.json`: 0 hits, complete (positive control: `ENG-243` finds ENG-2432, 2433, 2434, 2436 in Slack).

- Project id: `ec2ea957-fc8e-4958-b809-0fb735b1e916` (uuid v4 form, like the base's two).
- Issues: ENG-2438, ENG-2439, ENG-2440, ENG-2441, ENG-2442, ENG-2443, ENG-2444, ENG-2445, ENG-2446, ENG-2447, ENG-2448, ENG-2449, ENG-2450, ENG-2451, ENG-2452, ENG-2453, ENG-2454, ENG-2455, ENG-2456, ENG-2457, ENG-2458, ENG-2459, ENG-2460, ENG-2461, ENG-2462, ENG-2463.
- Comment ids: `comment_` + 32 hex, mint at SQL time; a sha256 of a fixed string, cut to 32, is enough.
- Author ids: Leonard `usr_63fffeb4fab5233e`, Robert `usr_Robert`, Arthur `usr_cc3e90160f490686`. All three belong to `team_ENG`.

## B. Gmail

Sources: Leonard's thread files through hg.py; a complete search of all 88,726 thread files (`from` and `subject` fields); real tool output in stored runs; live tool text in `state_full.json`.

**Mailbox naming (FACT).** Leonard's files are `threads/leonard@harmonygames.co_<thrid>.json`, but every id inside uses `leonard.hayes@harmonygames.co`. Arthur's are `blake@harmonygames.co_<thrid>.json` with ids `arthur.blake@harmonygames.co/...`. Robert's sit partly in numbered files (`threads/00016827.json`).

**Id scheme (FACT).**
- Thread id: `leonard.hayes@harmonygames.co/<19 digits>`. The number is `(arrival_ms << 20) | 20 random bits`: `1856958794180374704 >> 20` = 1770933908634, against `internal_date` 1770933907000 (+1.6 s); `1817557789846606177 >> 20` = 1733358182760, against 1733358175000 (+7.8 s). Mint from the root message's time plus 1-8 s. LLC's seeds follow it.
- Message id: `leonard.hayes@harmonygames.co/<RFC Message-ID with the angle brackets>`. Each mailbox copy has its own thread number and the same RFC id.
- `gmail_threads`: `id, user_email, snippet, history_id` (NULL).
- `gmail_messages` columns LLC used: `id, thread_id, user_email, label_ids_json, snippet, internal_date, date, size_estimate, subject, from_email, from_name, to_json, cc_json, bcc_json, reply_to_json, body_text, body_html, headers_json, in_reply_to, "references", mbox_from, attachments_meta_json`. Never list `body_text_fts`.
- `to_json` / `cc_json`: JSON list of `"name <addr>"` strings. `headers_json`: list of `{name, value}` with at least Message-ID, Date, Subject, From, To, plus Cc, In-Reply-To, References when they apply. These are what the read returns.
- `internal_date` (ms) = `date`.

**Message-ID shapes by sender (FACT).**

| Sender | Shape | Example |
|---|---|---|
| Leonard (Gmail) | `<CAPBs_a` + about 36 base64-like characters + `@mail.gmail.com>` | `<CAPBs_a5shT3SSGoNBAoNH4Mn2gmxBYGuP__1fKKEyhP7G2A8rg@mail.gmail.com>` |
| KPMG (Outlook) | `<HOST + 25 upper hex @HOST.namprd19.prod.outlook.com>`, HOST like `LV3PR19MB8524` | `<LV3PR19MB8524A7F34357829DDCA90153CA302@LV3PR19MB8524.namprd19.prod.outlook.com>` |
| Griffin (Outlook) | same, `namprd02` | `<BYAPR02MB47273D67561AFA83C4D66355A0042@BYAPR02MB4727.namprd02.prod.outlook.com>` |
| Sunset people (Superhuman) | `<ml` + 6 lowercase alphanumerics + `.` + uuid + `@we.are.superhuman.com>` | `<mlin90ff.024721f6-609d-44eb-84e0-9d0f0e596c35@we.are.superhuman.com>` |
| Sunset platform `SVC_0210` | Amazon SES `<0100019c...-000000@email.amazonses.com>` | invite, thread 1856871594497249045 |

**Labels (FACT).** Human mail in Leonard's INBOX: `["INBOX","IMPORTANT","Label_b19fb8d1b3","CATEGORY_PERSONAL"]`. `Label_b19fb8d1b3` is his user label "Opened" (present on the Feb 13 mail too). His sent mail: `["SENT","Label_b19fb8d1b3"]` or `["SENT"]`. Export also uses `ARCHIVED` (Gmail has none at the tool level; `gmail_archive_thread` says find archived mail with `in:archive`). Load-bearing mail stays INBOX or SENT: base mail in Leonard's February listing is often SPAM or TRASH, and search skips those.

**Snippet rule.**
- FACT: base thread exports have no snippet key. LLC stored the first 140 characters of the body, whitespace collapsed, in both `gmail_threads.snippet` and `gmail_messages.snippet`.
- FACT: on read, `gmail_get_thread` returns the stored thread snippet (140 characters), while each message's `snippet` comes back as the first 100 characters of the body, whatever was stored. `sizeEstimate` is also recomputed (seeded 1490, returned 823).
- So: write the 140-character rule, and keep any pointer-free opening. The first 100 characters of a seeded body are visible in `format=minimal` and in batch reads.

**How a seeded outside mail should look (FACT from base and passed tasks).**
- Plain text, `\r\n` line ends, `body_html` NULL, `attachments_meta_json` '[]', `in_reply_to` and `"references"` NULL or '' on a root, `reply_to_json` '[]', `bcc_json` '[]', `mbox_from` NULL. `from_email` = the token (`PERSON_3088_EMAIL`), `from_name` = the token (`PERSON_3088_NAME`).
- Reuse base tokens where the person exists. New outside people have been minted before with /injection PASS (`PERSON_9901`-`9904` bridge, `PERSON_9701`-`9708` Q4, `PERSON_7731` close-out).
- Company name: 6 of 11 completed tasks' SQL says `Harmony Games`; base subjects carry `[SOURCE_ORG_0001]`, and the bridge task used that form 9 times. For a subject that must sit beside base subjects, use the token form.
- Never carry a fact only in an attachment: `gmail_get_attachment` returns no bytes here (`acl.md`, 2026-10-17 note).

### Seed 1: KPMG FY25 request: **beside**, as a new root thread

**Base pattern (FACT, all re-read).** Each year is its own new thread in Leonard's mailbox, never a reply to the last:

| Year | Thread | Root date | Sender | To | Cc | Due in body | Label |
|---|---|---|---|---|---|---|---|
| FY23 | `leonard.hayes@harmonygames.co/1788910618703813283` | 2024-01-23 19:28Z | `PERSON_4416_NAME <PERSON_4416_EMAIL>` | `leonard.hayes@harmonygames.co` (bare) | PERSON_0467, PERSON_3710, PERSON_2847, PERSON_3077 | 2/2/2024 | INBOX, IMPORTANT, Opened, CATEGORY_PERSONAL |
| FY24 | `leonard.hayes@harmonygames.co/1817557789846606177` | 2024-12-05 00:22Z | `PERSON_3088_NAME <PERSON_3088_EMAIL>` | `leonard.hayes@harmonygames.co` (bare) | PERSON_4416, PERSON_2322, PERSON_2847, PERSON_3077 | 12/20/2024 | same |

- **Sender token:** `PERSON_3088_NAME <PERSON_3088_EMAIL>`, the most recent associate, signing `[PERSON_NAME_46103] (she/her/ella)`, `Audit Associate`, `KPMG LLP | 55 Second Street | Suite 1400 | San Francisco, CA 94105`, plus the KPMG confidentiality block.
- **Cc:** `PERSON_4416_NAME <PERSON_4416_EMAIL>`, `PERSON_2322_NAME <PERSON_2322_EMAIL>`, `PERSON_2847_EMAIL` (Griffin VP Finance, still active: copied on the Feb 12 "Board position" mail). Leave out PERSON_3077: Griffin's own reply shows them as `[Deactivated]` in Dec 2024.
- **Subject:** `GRIFFIN GAMING PARTNERS 2025 Audit Request [SOURCE_ORG_0001], Inc.` (FY24's exact form; FY23 had ` - ` before the token).
- **Message-ID:** Outlook `namprd19` shape above. Label set as above.
- **Absence check:** "Audit Request" in `subject` across all 88,726 thread files: 11 hits, FY23 and FY24 only (9 Leonard, 1 Arthur, 1 numbered), `scan_complete` true. PERSON_3088 sent 3 mails, all in Leonard's mailbox; PERSON_4416 sent 1; PERSON_2322 sent 0 (Cc only). Nothing after Dec 2024.
- **Copies:** Leonard's only. Robert and Arthur are not on the mail. Leonard's Feb 2024 reply BCC'd both founders, so that habit is available.

**One departure from base is forced.** The base body is generic: "Please see the attached confirmation". The four numbered items are in the attached PDF, and Leonard's Dec 17, 2024 reply mirrors them: (1) confirmation of the fund's investment as of September 30, 2024; (2) latest audited and most recent unaudited statements; (3) cap table from Carta; (4) articles. Since attachments return no bytes, an FY25 seed must inline its items and as-of date in the body. A reader comparing years will see that change; a one-line reason in the body ("listed below so you don't need the PDF" or similar) keeps it natural.

**Timing.** FY23 came Jan 23 with 10 days to reply; FY24 came Dec 4 with 16 days, then a follow-up on Dec 17 after Leonard missed it ("I missed the previous one"). No FY25 mail is in any mailbox up to the clock, so a root dated in Feb 2026 fits. Candidate roots, each checked against file names (0 matches):

| Root time | Thread number | `internal_date` |
|---|---|---|
| 2026-02-10T18:41:07Z | `1856764766480503439` | 1770748867000 |
| 2026-02-13T16:48:33Z | `1857029474983245439` | 1771001313000 |

### Seed 2: Sunset notice list: **beside** by default; in-thread is the less-pointed option

**Sunset people in base (FACT).** PERSON_0767 CEO (15 messages across mailboxes), PERSON_2888 Head of Partnerships (8), PERSON_3131 CTO (0 sent; added on Cc Feb 12), `SVC_0210` platform invites, `SVC_1248` PandaDoc. **No Sunset legal or customer-success person exists in base.** The CEO's Feb 12 22:22:58Z mail says those people arrive after intake ("the legal team will review all the docs ... kickoff call with legal + your dedicated customer success manager").

| | Beside (recommended) | In-thread (less pointed) |
|---|---|---|
| Thread | new root, like `leonard.hayes@harmonygames.co/1856872398290956689` | inside `leonard.hayes@harmonygames.co/1856675475513544349` (14 messages) |
| Sender | `PERSON_2888_NAME <PERSON_2888_EMAIL>` | same, or `PERSON_0767_NAME <PERSON_0767_EMAIL>` |
| To / Cc | `leonard hayes <leonard.hayes@harmonygames.co>`, no Cc (as the Release of Claims mail) | To Leonard; Cc PERSON_2888 or 0767, robert, arthur blake, PERSON_3131 |
| Subject | `Sunset: <what it is>`; base form is Leonard's forward of `Sunset: Release of Claims Templates` (PERSON_2888's own subject is redacted to `[PERSON_NAME_3207]: Release of Claims Templates`) | `Re: Combo Fighter Data and [SOURCE_ORG_0001] Shut-Down` |
| `in_reply_to` | NULL | `<CAPBs_a5shT3SSGoNBAoNH4Mn2gmxBYGuP__1fKKEyhP7G2A8rg@mail.gmail.com>` (Leonard's Feb 12 22:56:54Z reply) |
| `references` | NULL | the full chain from message [0]'s `references` plus that id |
| Copies | Leonard only | Leonard; optional `robert@harmonygames.co/1856676159551928108`, `arthur.blake@harmonygames.co/1856676160903595465` |
| Message-ID | Superhuman shape | Superhuman shape |
| Date | after 2026-02-12T22:56:54Z, before the clock | same |
| Candidate thread | `1857034369525983506` (2026-02-13T18:06:21Z, `internal_date` 1771005981000; 0 file matches) | reuse base thread number |

- Why beside: this is how Sunset already sends how-to material (PERSON_2888, "Hi Leonard,", templates in the body, sent to Leonard alone), it needs no reference chain and no extra copies.
- Why in-thread may suit the 70 % aim: the subject carries no stockholder word. But free-text search matches the body either way, so a `stockholder` search finds it in both forms. Only the subject-based and first-hits routes differ.
- Sender: keep PERSON_2888 relaying legal's rules. That gives a non-owner voice with no new entity. A named legal or customer-success person would be a new token (`PERSON_98xx`), allowed by precedent, but the CEO's mail says they appear after intake, so the seed would also have to imply intake went in. Sunset-platform activity leaves no record either way.
- Subject words: 0 subjects across all mailboxes contain "stockholder" (complete scan), so the seed's own subject would be the first and only hit if it uses that word.
- Not checked: the signed Sunset SOW is an unread PDF (three attachments on 1856956483320787350). Anything the seed says about scope has to be checked against it (decision 6 in the analysis).

### Does search reach BCC?

- FACT, live tool text: `gmail_search_messages` grammar lists `from: to: cc: bcc:` and says free text "matches subject, body and sender/recipient names".
- FACT, base: Leonard's SENT copy keeps the list in the `Bcc` header and `bcc` field (`1781310711617833275` message [6], 13 addresses in header order `X-GM-THRID, X-Gmail-Labels, MIME-Version, Date, Bcc, ...`).
- FACT, runs: a `Bcc` header did come back in a `gmail_get_messages_batch` result (Frederick card-spend run). `metadata` format's default envelope also includes Bcc.
- NOT PROVEN: 0 `bcc:` queries in 120 stored trajectory files, and I cannot run the live tool. Whether plain free text reaches `bcc_json` is also untested. Treat `bcc:` search as catalogued but unproven, and test it in the pre-check, as the analysis says. A reading path through the two mailing threads does not depend on it.

### What the reads return (FACT, real output)

- `gmail_search_messages(query!, user_email, max_results<=500 default 100, page_token)`: `{messages:[{id, threadId}...]}` newest first, with `nextPageToken` when more. **Ids only**: no subject, no snippet. Every hit needs a second call. SPAM and TRASH excluded unless named. `query` uses `after:` / `before:` / `newer_than:`, `has:attachment`, `filename:`, `in:`, `is:`, `label:`.
- `gmail_get_thread(thread_id!, user_email, format default full, metadata_headers)`: `{id, snippet, messages:[...]}`. Whole thread, no paging, oldest first by `internalDate` (the export file is newest first). Each message: `id, threadId, labelIds, snippet, internalDate, sizeEstimate, payload{partId, mimeType, filename, headers[{name,value}], body{size, data}}`. `body.data` is base64url, so the agent decodes it. The Ask_Carriers `limit`/`offset` parameters no longer exist.
- `gmail_get_messages_batch(message_ids!<=100, user_email, format default metadata, metadata_headers)`: `{messages, not_found}`. Default has no body. `format=full` is capped at 10 ids: 13 calls in stored runs failed with a 400 for that, and at least 14 overflowed to a file.
- `gmail_get_message(message_id!, user_email, format default full, metadata_headers)`: one message, same shape.
- FACT: `gmail_list_messages` and `gmail_list_threads` also take `query`.

## C. Slack

Sources: `slack/channels.json`, `messages/<channel>/2026-02.json`, a complete `ts` scan of all 53 February shards through hg.py, LLC SQL lines 41-56, live tool text.

**Row shape (FACT, LLC columns).** `id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, reply_count, reply_users_count, latest_reply, is_activity_message, subtype, reactions_json, files_json, attachments_json, created_at, metadata_json`. Values: `type` 'message', `is_activity_message` false, `subtype` NULL, the three JSON lists '[]', `metadata_json` '{}'. Never list `text_fts`.

**ts rule.** String with exactly 6 decimals, unique per channel. `created_at` is the same instant as a timestamptz. Check `(channel, ts)`, because 101,657 base records have no `id`.

**id rule (re-verified).** `sha256("<channel_id>|<ts>").hexdigest()[:32]`: holds on the last message of both DMs (`cc260c66cb9d2d8a9c8062e9b3a67335`, `9a7fbfd90c172f806d72339af984e97b`).

**Thread encoding (resolves Ask_Carriers §7 SELECT 1, FACT from LLC, /injection PASS).** A reply sets `thread_parent_id` = the parent's **hash id** and `thread_ts_legacy` = the parent's ts, with its own counters 0. The parent gets `UPDATE ... SET thread_ts_legacy = '<parent ts>', reply_count = n, reply_users_count = n, latest_reply = '<reply ts>' WHERE id = '<parent id>'`.

**Latest allowed ts.** The last base record is `1770977006.104929` = 2026-02-13T10:03:26Z (`C09SWTHEMEW`, PERSON_0633). NB-6 says not to grade anything after 10:03 UTC and some records point at later messages that are missing. Keep every seed at or below `1770977006.000000`. The real floor for outreach seeds is later than Leonard's list, `1770934638.035469` (Feb 12 22:17:18Z, `#winddown`). The usable window is therefore about 11 h 45 m: ts `1770934700` to `1770977000`.

**Channel posting.** `channel_id` must exist and the poster must be a member. Membership is unchanged by seeds. NB-1: after Feb 11 20:40 UTC do not seed staff in channels they left (Julia, Marcus, Owen, Oliver, Martin, Claire, Brian). All three founders are safe.

**The two DMs (FACT).**

| | `D04UP2L3E3S` | `D04UGG61DUM` |
|---|---|---|
| Pair | Leonard + Robert (`EMPLOYEE_0016_SLACK_ID`) | Leonard + Arthur (`EMPLOYEE_0025_SLACK_ID`) |
| Flags | `is_im` true, `is_private` false, `num_members` 5 | same |
| `members` | Robert, Leonard, `PERSON_6089_SLACK_ID`, `U04TWDMDT0V`, `U04UP2L1RUY` | Arthur, Leonard, `PERSON_6089_SLACK_ID`, `U04UP2L1RUY`, `U04V95A7C80` |
| Leonard's reach | YES (`persona_view can-see`) | YES |
| Feb messages | 220 (Leonard 117, Robert 103) | 146 (Leonard 100, Arthur 45, PERSON_6089 1) |
| Busy days | Feb 6 (102), Feb 11 (100) | Feb 11 (51) |
| Feb 12 | 2 messages: Leonard 06:05:40Z, Robert 16:36:33Z "Yeah not very helpful" | 00:46-01:13Z only (data access work, ends "I like to count my chickens...") |
| Feb 13 | **none** | **none** |
| Last ts | `1770914193.165359` | `1770858816.197309` |
| Threads | 0 in Feb | 1 in Feb (`1770769607.801499`, 1 reply) |

Who is really active on Feb 12-13 (complete scan):
- **Feb 13 has only 13 Slack records in the whole export.** 10 in `#executives` `C07C2866011`: Leonard 02:49-03:23Z (Unity ad review) and Robert 04:19-04:19:59Z. 2 from a bot in `C06M373FT63`. 1 from PERSON_0633 in `C09SWTHEMEW`.
- Feb 12 evening: `#winddown` `C0ADGSZKR3R` carries it. Since Feb 12 00:00Z: Leonard 89, Robert 16, Arthur 4, PERSON_6089 1. Last post `1770937460.360699` (23:04:20Z, Leonard `:+1:`).
- `#admin_foundersonly` `C04UEQVDVB7`: 7 messages in Feb, last Feb 11 00:41Z. Effectively quiet.
- Adviser DM `D04UC0UEN2V`: 29 in Feb, last `1770928024.779979` (Feb 12 20:27Z).
- Last post per founder, checked across every channel active since Feb 12 12:40Z: Robert Feb 13 04:19:59Z (`1770956399.303509`), Leonard Feb 13 03:23:12Z (`1770952992.131649`), both in `#executives`; Arthur Feb 12 23:00:32Z (`1770937232.664809`, `#winddown`). A DM seed after those times has no base company around it, though nothing forbids it.

**How a seeded founder DM should look.** Bursts of 1-liners, not a paragraph. Median 39 characters base-wide; lowercase from Arthur, mixed from Leonard, Robert terse ("ok", "wtf?"). Spacing 3-60 s inside a burst. Top-level, no threads: the Leonard-Robert DM has none in February. `reply_count` 0. Example shape only (no content): three rows, `EMPLOYEE_0038_SLACK_ID`, ts `1770938xxx.xxxxxx` ascending, `D04UP2L3E3S`, each with its own sha id. A DM burst between Feb 12 22:17Z and Feb 13 04:30Z sits inside real founder activity.

**Reads (FACT, live text; Ask_Carriers' parameter names are stale).**
- `slack_read_channel(channel_id!, limit<=100 default 100, cursor, oldest, latest, response_format)`: top-level only, newest first, accepts a DM id or a user id.
- `slack_read_thread(channel_id!, message_ts!, ...)`: parent plus replies. 10 of 89 stored calls errored.
- `slack_search_public_and_private(query!, ...)`: all channel types including IMs, 301 calls in 51 of 60 runs. Used by most runs, so a keyword in a seeded DM is one search away.
- `slack_conversations_search_messages(...)`: filter-only works, returns replies.
- `slack_search_channels` never returns DMs: a run reaches a DM by `user_id` or search hit, so a founder DM is less pointed than a channel.

## D. Drive, Docs, Sheets, Slides

Sources: `gdrive/data.json` (53,866 files), `gdocs`, `gsheets`, `gslides` through hg.py; LLC SQL lines 7-40; Claire's SQL line 167; LLC run output.

**Id format (FACT).** `f_` + 22 lowercase hex for files, `d_` + 22 hex for folders; all 53,866 base ids are 24 characters. Docs, Sheets and Slides use the same `f_` id as their Drive row. `revision_id` 10 hex. Slides pages `slide_` + 12 hex, elements `el_` + 12 hex.

**Leonard's Drive (FACT).** Root `d_63fffeb4fab5233ed5bb73` (name = his address, `parents` [], `modified_time` null). 446 direct children: 140 Docs, 102 Sheets, 28 Slides, 13 folders, 13 others. He owns 817 items, 46 folders, none shared at root level. Newest visible items are dated 2026-02-11T23:22:39Z.

**What Leonard owning a folder needs (FACT: base `d_05c8d93dcee6197e61797f`; seeded precedent Claire's `d_272d849cde40c35980a433`, /injection PASS).** One row, no companion table:

| Column | Value |
|---|---|
| `id` | `d_` + 22 hex |
| `name` | folder name |
| `mime_type` | `application/vnd.google-apps.folder` |
| `parents_json` | `["d_63fffeb4fab5233ed5bb73"]` |
| `owner_email` | `leonard.hayes@harmonygames.co` |
| `owners_json` | `["leonard.hayes@harmonygames.co"]` |
| `shared_with_emails_json` | `[]`, or founders |
| `shared_roles_json` | `[{"email":..., "role":"writer"}]` matching the line above |
| `visibility` | `private` |
| `modified_time`, `created_time` | ISO Z |
| `trashed`, `starred` | false |
| `size`, `content_path`, `web_view_link`, `icon_link`, `description`, `drive_id`, `content_text` | NULL |

- Sharing is not inherited in the data: each child needs its own `shared_with_emails_json`.
- `gdrive_list_folder(folderId, pageSize default 25)` lists children, with `permissions`, `owners`, `parents`.
- The write target must be visible to the persona: 6 of 26 `gdrive_move_file` calls in stored runs returned 404 "Parent folder ... not found", all on `d_e5caf6a8c630421942ee59`, a base folder named "Wind Down" (modified 2026-02-09) owned by `Resource: 7240535625619857401` with empty sharing. `persona_view` says no persona can see it. Do not name that folder as a home; a Leonard-owned seed avoids the problem.

**Native Doc (FACT, LLC; read by all 6 runs).** Two rows.
1. `gdrive.drive_files`: `id, name, mime_type='application/vnd.google-apps.document', parents_json, owner_email, shared_with_emails_json, shared_roles_json, visibility, owners_json, modified_time, created_time, trashed, starred`.
2. `gdocs.docs_documents`: `document_id` (= Drive id), `title`, `owner_email`, `shared_with_emails_json` (identical list), `visibility`, `body_text` (non-empty), `style_runs_json` `[{"start":0,"end":n,"named_style":"TITLE","list_id":null,"list_nesting":0},...]`, `revision_id`, `drive_file_id` (= id), `created_time`, `modified_time`.

No `content_path` is needed: `gdrive_read_file(fileId)` served LLC's seeded Doc as `{"mimeType":"text/markdown","text":"# ..."}`, and `gdocs_get_document_text(documentId)` as `{documentId, title, name, revisionId, createdTime, modifiedTime, text}`. Base natives mostly do have a `content_path` (342 of 370 of Leonard's), so that is a harmless difference. `content_text` alone is not served.

**Native Sheet (FACT, LLC; read by all 6 runs).** Three rows: `drive_files` with `...spreadsheet` mime; `gsheets.sheets_spreadsheets (spreadsheet_id, title, owner_email, shared_with_emails_json, visibility, drive_file_id, created_time, modified_time)`; `gsheets.sheets_sheets (spreadsheet_id, sheet_id, title, "index", row_count, column_count, grid_json)`, one per tab, `sheet_id` from 0, `row_count` 1000, `column_count` 26, `grid_json` a 2-D array of cells (strings in LLC). Reads: `gdrive_list_sheets(spreadsheetId)`, `gsheets_values_get(spreadsheetId, range)` (trailing empty cells dropped), `gsheets_get_spreadsheet(spreadsheetId, includeGridData)`, `gdrive_read_sheet_range(spreadsheetId, sheetIndex)` as CSV, `gdrive_read_file` as CSV.

**Native Slides (FACT, LLC and Claire).** Four tables: `drive_files` with `...presentation` mime; `gslides.slides_presentations (presentation_id, title, owner_email, shared_with_emails_json, visibility, drive_file_id, revision_id, created_time, modified_time)`; `gslides.slides_pages (presentation_id, object_id, "index", layout, notes)` with `layout` 'BLANK' and `notes` NULL; `gslides.slides_page_elements (presentation_id, page_object_id, object_id, kind, text, placeholder_type, x_emu, y_emu, width_emu, height_emu, table_json, ordinal)` with 'TEXT_BOX', `0, 0, 9144000, 5143500`, one element per page. Reads: `gslides_get_presentation_text(presentationId)` gives `{presentationId, title, revisionId, slideCount, text}`, one slide per blank line. Base decks all carry a `description` "Reconstructed Google Slides sibling ..."; seeded ones with NULL passed.

**Ownership and sharing fields (FACT).** `owner_email` plus `owners_json`; `shared_with_emails_json` identical in the Drive row and the native row (`base_check`); `shared_roles_json` Drive row only; `visibility` 'private' for 801 of Leonard's 817. A Drive read expands these into `owners[]` and `permissions[]` with role.

**Who finds what (FACT, live text).** This is the main lever for this family.

| Tool | Matches on |
|---|---|
| `gdrive_search(query)` | word prefixes of the **name** |
| `gdrive_search(fullText)` | name, description, "document body text" |
| `gdocs_search_documents(query / fullText)` | title / body or title (substring) |
| `gsheets_search_spreadsheets(query)` | **title only** |
| `gslides_search_presentations(query)` | **title only** |

So Doc text can be reached by a word search; Sheet cells and slide text are reachable only through a title, a folder listing or a pointer (whether `gdrive_search fullText` reaches cells or slides is unproven).

**Read rate in LLC (FACT, 6 baseline runs).** Seeded Doc: named in all 6 runs (3 by `gdrive_read_file`, 3 by `gdocs_get_document_text`). Seeded Sheet: named in all 6 runs. **Seeded deck `f_7d2c9e7822e87b92a11759`: no call named its id in any of the 6 runs.** Stored runs overall: 24 `gslides_get_presentation_text` calls in 21 runs, 0 Slides writes.

**Minted ids (collision-checked).** `hg.py search lookup gdrive --pointer /drive_files` and `hg.py records` on `/drive_files` (53,866), `/docs_documents` (633), `/sheets_spreadsheets` (398), `/slides_presentations` (164): 0 matches, `scan_complete` true.

| Use | Id |
|---|---|
| Folder | `d_601064334a0b493022fe83` |
| Doc 1 | `f_a37b403d5200d4f0a31d31` (revision `3c986c6ce3`) |
| Doc 2 | `f_762c60832854d3e7a7f7df` (revision `84bdd1a5ac`) |
| Sheet | `f_5ecaa967db3adcfa440b09` |
| Deck | `f_75dddccabb26eeea4842c8` (revision `0b2616045d`; pages `slide_341616bedf43`, `slide_659353384faa`; elements `el_f71854425943`, `el_3f1b82e16a82`) |

**Base files a seed should line up with.** Leonard's only investor update was drafted in Doc `f_5a4fb6c74aab30e85771e5` (shared with Robert and Arthur), then BCC'd, so a letter in a shared Doc has precedent. Investor and board decks exist: `f_418f5adef3a62a0e55c427` "Harmony Games March 25 Investor Update", `f_84a3fffd6ba30c9bcfee07` "Harmony Games August 25 Update", `f_65ada5e24989d256cabdfa` "Harmony Games BoD Jan 14 2026" (all owned by a `Resource:` account and shared with Leonard). The title idiom is `Harmony Games <Audience or Month YY> <Update|BoD>`.

## E. GCal

Sources: `gcal/data.json` (11,130 events in this export; Ask_Carriers says 11,233), LLC SQL lines 119-124, stored runs, live text.

**Event shape (FACT, LLC columns).** `event_id, calendar_id, summary, description, location, start_ts, end_ts, start_json, end_json, organizer_email, creator_email, attendees_json, status, visibility, transparency, rrule_json, recurring_event_id, original_start_json, sequence, created, updated, hangout_link, ical_uid`. Example values: `evt_` + 22 hex; `start_json` `{"dateTime":"2026-02-16T18:00:00Z"}`; `attendees_json` entries `{"email","organizer","responseStatus"}` with `"self":true` on the calendar owner; `status` 'confirmed'; `visibility` NULL; `transparency` 'opaque'; `rrule_json` '[]'; `sequence` 0; `ical_uid` 32 hex + `@hg4`; `hangout_link` `https://meet.google.com/xxx-xxxx-xxx` (base adds `?hs=224`).

**Copies per attendee (FACT).** One row per attendee who has a calendar, each with its own `event_id`, one shared `ical_uid`, the same `attendees_json` except `self`. LLC: 3 rows for a 3-founder event. Outside people have no calendar row.

**Outside attendees.** Leonard's calendar has **0** events with a `PERSON_` token among attendees, even the Sunset calls: `evt_212e50fb5a53ea8016ce29` "[SOURCE_ORG_0001] Wind Down" Feb 11 lists only the three founders, while PERSON_2888's "Accepted:" mail shows Sunset attended. Base form for an outside 1:1 is a summary naming the person with Leonard as the sole attendee (`evt_1028de201ad2015bc64c9e`, Jan 13, 2026). Follow that form; do not put a token in `attendees_json`.

**Invitation mail (INT-11).** Not required: most base meetings have none in the persona's mailbox. LLC seeded `Invitation:` mails for Robert and Arthur. Either decide per event and record it, or list `no_notify` under `integration_exceptions`.

**What Leonard's calendar shows for the coming week (Feb 16-20).**
- FACT: **no stored event in any calendar starts on or after the clock.** Leonard's last dated event is `evt_81c5253b4381de75a4853c` "[SOURCE_ORG_0001] wind down", 2026-02-12T16:30Z. The last ones before it are Feb 11 "Wind Down" and a Feb 11 webinar. No Sunset kickoff and no investor call is scheduled.
- FACT: but 190 recurring masters on his calendar are not cancelled and have no `UNTIL` before Feb 16: 45 distinct titles (Company Standup, All Hands, Weekly Art Sync, Design Meeting Weekly, Executives Biweekly Sync and more), about 184 weekly instance-days in Feb 16-22 by my expansion. A company that shut on Feb 11 still shows its whole meeting grid.
- FACT: `gcal_list_events` spilled to a file in **18 of 20** stored calls, at 97,323 to 1,296,001 characters: 196,590 for a 3-day window on Claire's calendar (`singleEvents` true). Windowed lists without `q` are close to unusable.
- INFERENCE: on Leonard's calendar the same call will spill, and I could not run it. `gcal_search_events(q, timeMin, timeMax)` (25 calls in 22 runs, returns events across visible calendars; `q` terms all must match summary, description, location, organizer or attendee) is the working read, so a seeded event is found by a word in its summary or not at all. `gcal_get_event` returns `description` (seen in Claire's run).

**A real job here.** Two honest candidates, both dated after the clock (plan fields may be):

| Candidate | Why it is real | Effect | Risk |
|---|---|---|---|
| 1:1 call rows, e.g. `Leonard <> <holder or family name>` next week, Leonard alone as attendee | His promise is "personally reach out"; `#winddown` idx 8 says "one by one". A booked call means the first contact for that holder is a call, not a note | Changes that holder's call (one row can cover the three Disli holders if the design's FAM rule says so) | Implies he has already contacted them to book: the event must be a hold on his own calendar, and seeded text must not say anyone was told |
| Sunset kickoff with legal and the customer-success manager | The CEO's mail promises it | Sets a date the holder list must be ready by | The CEO says it follows intake, so a seeded date implies intake is in. Sunset people are not attendees in the base form |

Keep the load-bearing part in `summary` and time, not `description` (○; analysis §8 already says no fact only in a GCal description).

## F. Trello

Sources: `trello/data.json` (5 boards, 48 lists, 803 cards, 5,294 actions), LLC SQL lines 57-60, live text, runs.

**Boards (FACT).**

| Board | Id | Closed | Cards (open) | Last card activity | Last action | Max `idShort` |
|---|---|---|---|---|---|---|
| Harmony Games (founders' board) | `640643a3fd8f3ca308d9318e` | no | 449 (177) | 2025-11-12T17:25:43Z | 2025-11-13T20:43:07Z | 455 |
| DD Product Roadmap | `65eb4ec525346c8070ca638f` | no | 216 (175) | 2025-10-10 | 2025-11-13 | 210 |
| ZM ROADMAP | `6851a6569f3bf818760632ab` | no | 79 (69) | 2025-10-13 | 2025-11-13 | 79 |
| UA/BD | `66da196af476ab78deaa0cef` | no | 40 (39) | 2025-03-18 | 2025-03-18 | 40 |
| Welcome Board | `535af5816ca07f261e8cd420` | **yes** | 19 | 2014 | 2023 | 19 |

The Nov 13, 2025 actions are `deactivatedMemberInBoard` by Leonard on all three live boards. His Nov 12 actions moved the last cards. Nothing since: every seed is a visible 3-month recency jump, as LLC's was.

**Lists on Harmony Games (FACT).**

| List | Id | Cards | Open | Last |
|---|---|---|---|---|
| To Do | `640643a3fd8f3ca308d93195` | 10 | **0** | 2024-09-23 |
| Doing | `640643a3fd8f3ca308d93196` | 5 | **0** | 2025-01-04 |
| Done | `640643a3fd8f3ca308d93197` | 402 | 170 | 2025-11-12 |
| Backlog | `641359135e6148b9de0e076c` | 30 | 6 | 2025-11-12 |
| Recruiting (closed list) | `6406526934e8f4d907fa96a7` | 2 | 1 | 2024-04-26 |

To Do and Doing hold no open card, so a seed there is the only open card in its list: `trello_get_lists` shows `cardCount` 1 at once.

**Closed-card rule (FACT).**
- `closed` means archived. 324 of 803 cards are closed. Reads hide them by default: `trello_get_cards_on_board`, `trello_get_cards_in_list`, `trello_get_lists` `cardCount` and `trello_search` (`cards_filter` 'open') all return open cards unless `filter` / `cards_filter` is 'all' or 'closed'.
- `sql_lint` and `base_check` have **no** Trello closed-card check; the lifecycle FAIL (comment after close) is Linear only. "No activity on closed records" is the analysis's own rule, and a sound one (`/injection` State/Lifecycle is judged by a reader).
- **Correction to the analysis §8:** `/cards/801` is "Existing Investor Update" (`68c5a49e8491a9d7faf869d0`, `idShort` 455) and it is **not** closed: `closed` false. It sits in the **Done** list, moved from Doing on 2025-11-12 by Leonard, with 0 comments. So it is a done card, not an archived one. The practical advice stands: leave it alone, because a comment on a Done card dated Feb 2026 reads as reopened work.
- That card is useful as is: Leonard marked it Done on Nov 12, 2025, but the only update ever sent is May 18, 2024. It is a free base `done_gap` control with no seed.
- Closed base cards relevant to the theme, which must not be touched: `646bf1d5a038bfcd4c6cde85` "newsletter for angels", `64e3967c4bea2b815c99f59a` "notify stakeholders on Carta", `6416439c5b25384ba9035374` "Make a list of VC/Investors".

**Seed shape (FACT, LLC).**
- Card: `id` = hex(unix seconds) + 16 hex; `name`, `"idBoard"`, `"idList"`, `"desc"`, `pos`, `closed` false, `due` NULL, `"dueComplete"` false, `"idMembers_json"`, `"idLabels_json"` '[]', `"idShort"` **456**, `"shortLink"` NULL, `"shortUrl"` NULL, `url` `https://PERSON_6092_TRELLO_USERNAME.com/c/<8char>/<idShort>-<slug>`, `"dateLastActivity"`, `cover_json` NULL, `badges_json` full base shape.
- Action: `createCard`, `"idMemberCreator"` `PERSON_6094_TRELLO_USER_ID` (Leonard), `data_json` `{board{id,name,shortLink:"f4LGcmuh"}, card{id,idShort,name,shortLink}, list{id,name}}`. Reads derive `shortLink` from `url`.
- Comment: `commentCard` action with `data_json.text`; bump `badges.comments` and `"dateLastActivity"`.
- Checklists: `trello_checklists` + `trello_check_items`; bump `checkItems` and `checkItemsChecked`.

**Reads (FACT).** `trello_search(query, cards_filter, ...)` is the usual door: 63 calls in 50 of 60 runs, free words match name or desc, and the `actions` arm matches comment text. `trello_get_comments(cardId, ...)` accepts a short link. `trello_get_card` errored in 16 of 43 stored calls, all from one bad argument (`attachments` must be true, false or "cover"), not from data.

**What a real job could be.** The board is the founders' own to-do list and Leonard's cards there include the investor items above, so one new To Do card is honest.
- Best job: **who owns each conversation.** A Leonard card in To Do, created after his Feb 12 22:17Z list, with one short comment from Robert or Arthur (a non-owner voice) taking a named angel or two. That changes who signs or sends a note, and it mirrors LLC's "moving rule" card, which was read through `trello_search`.
- Avoid a checklist of all holders: it would be a second owner list, and `trello_get_checklists_on_board` returns it in bulk.
- Base context: "Trello is done" (Leonard, `D04UGG61DUM`, Feb 12 00:52Z) is in the run of messages on giving Sunset data access. INFERENCE: it means access granted, not that Trello is closed, since LLC seeded a card later than that and passed `/prompt` 5.

## G. Contacts

Sources: `contacts/contacts.json` (170 records here; Ask_Carriers says 171), four tasks' seeded rows, runs, live text.

**Shape (FACT).** Base keys: `contact_id, first_name, last_name, is_user, gender, age, nationality, city_living, country, status, job, description, phone, email, address`. Table adds `created_at, updated_at, source`. Required: `contact_id, first_name, last_name` ('' allowed). `contact_id`: 164 are 24 hex, 6 are `cnt_` + 12 hex. Sparse: `job` on 36, `description` on 0, `is_user` on 1, 103 tokenized emails. Typical token row: `first_name` 'PERSON_3336', `last_name` '', `email` 'PERSON_3336_EMAIL', `gender` and `status` 'Unknown'.

**Seed precedent (FACT).** Claire 1 row, Vincent 1, Frederick bridge 4, Q4 4. Example: `INSERT INTO contacts.contacts (contact_id, first_name, last_name, is_user, gender, status, job, description, email, created_at, updated_at)`. Q4's seeded rows appear in `contacts_get_contacts` (`total` 174 = 170 + 4), even though `contact_group_members` is not writable. Seeded rows read with `source: "CONTACT"`.

**Holders and counsel in Contacts (FACT, whole file).**

| Person | Token | In Contacts? |
|---|---|---|
| Deepak | PERSON_1287 | yes, token row `46aabf1857b0733da86c4649` |
| Enes Disli | PERSON_2260 | yes, `9498fdeb61155487c7a2eb59` |
| Schaeppi (work) | PERSON_3083 | yes, `aaf48372feabcf6490f30d7c` |
| Segerstrale | PERSON_3336 / PERSON_3335 | yes, `ca57f88d55376b4341c5b6d4`, `1673c82fc650e0c42ab440d8` |
| Nebojsa | PERSON_3941 | yes, `a65131d8d9f49c59825ffdaa` |
| TOR principal | PERSON_5275 | yes, `82103c829a5708060fb0b37b` |
| Griffin director, Griffin investor | PERSON_4337, PERSON_2717 | yes, `3cb768c4ca8515702d29b703`, `5fc298433d57bde4489f07fd` |
| Matthew Collins | named | yes, `db57e559500151d6b3991b62`, job "Independent Director (investor/advisor, not an employee)" (he resigned May 1, 2025, per analysis) |
| Patrick | `patrick@harmonygames.co` | yes, `e704baa2167b3624a98b3352`, job "Business Development / Partnerships Manager" |
| Bergmann | PERSON_0693 | **no** |
| Eren Disli | PERSON_2275 | **no** |
| Schaeppi (personal) | PERSON_3063 | **no** |
| Nebojsa (other) | PERSON_3935 | **no** |
| TOR signers, TLAS counsel | PERSON_5137, PERSON_5593 | **no** |
| Griffin VP Finance | PERSON_2847 | **no** |
| KPMG | PERSON_3088, 4416, 2322 | **no** |
| Sunset | PERSON_0767, 2888, 3131 | **no** |

Counsel rows that do exist: Benjamin Clark "Outside Counsel, Company Formation (not an employee)" `160683a33e80876b5e3ca6b3`; Michelle Carter "General Counsel" `84ae5ae20147349f7ef89b77`; Thomas Baker "General Counsel" `cnt_05f0a0d12f2a`. Note the base's own `Patrick` row says staff, which supports the census D4 trap (`patrick@` was a holder's address).

**Is a seeded contact honest and useful?** Yes, in a small way, and only for someone with no row today.
- Honest: the people above are real base people who were on Leonard's BCC lists, and the rule "one person, one account per service" is met only if the token has no row. Bergmann and Eren qualify.
- Useful: it ties a name to a token address. Bergmann's token resolves the D4 "patrick" collision, Eren's gives a route for the holder who has no mail of his own in the record. 5 holders are token-only by name (census), so a name-to-address row is real help.
- Keep it sparse: `first_name`, `last_name`, `job`, `email`. Put nothing in `description`: 0 base rows use it and `contacts_search_contacts` does not search it (name, email, phone, job only, by word prefix).
- Weak as a difficulty lever: 37 search calls in 17 of 60 runs, cheap, and `contacts_get_contacts(limit 250)` dumps all (spills at 82,021 characters). Grade ● for `email` and `job`, and treat it as a supporting fact only, never the only home of a graded fact.
- Do not edit `Patrick` or `Matthew Collins` rows: those stale job titles are base facts and useful as they are.
- Side effect (FACT, live text): `gmail_send_message`, `gmail_reply_to_message` and `gmail_send_draft` turn each address reached into a contact. 7 stored `contacts_list_other_contacts` calls returned `total` 0 or 1. A verifier reading Contacts after a run may see those rows.

## H. Write proof

Run counts are over the 60 stored baseline runs (`07_Baseline_Trajectories/*.json`, 10 tasks); no run used Leonard as the persona. "Catalog" is `Evals/references/tools/catalog.json`, the source `/oe` treats as authoritative. "Live" is `state_full.json` (Oct 30 synth-cut sandbox); the run tool list (387 names) contains every tool named below.

| Deliverable | Tools and catalog params | Runs | Limits |
|---|---|---|---|
| Holder schedule (Sheet) | `gsheets_create_spreadsheet(title, initialSheetTitle, driveFileId)`; `gsheets_values_update(spreadsheetId, range, values)`; `gsheets_batch_update(spreadsheetId, requests)` for `addSheet`; `gdrive_move_file(fileId, newParentId, oldParentId)` | 40, 55, 26, 26 | Lands in root; a move is a second call. Alternative: `gdrive_create_file(name, content, mimeType, parentId, driveMimeType)` with CSV bytes in one call (10 runs). `gdrive_create_folder` was never called |
| Letter (Doc) | `gdocs_create_document(title, bodyText, driveFileId)`, then move; `gdocs_batch_update(documentId, requests)` for headings | 6; 2 | No parent parameter. `bodyText` is plain text; headings need `updateParagraphStyle`. **No Drive or Docs comment tool exists**, so "leave a comment on the Doc" cannot be asked |
| Share | `gdrive_share_file(fileId, emailAddress, role, type, domain)` | 50 | Roles reader, writer, commenter; owner only. Sharing a seeded file works only if Leonard owns it |
| One-to-one notes | **drafts:** `gmail_create_draft(to, subject, body, cc, bcc, thread_id, user_email)`. **sends:** `gmail_send_message` same params | **0**; 12 | See below |
| Consent ask to Griffin | same as notes, or a reply in an existing thread | | Griffin director resigned Feb 12 in thread `1856958794180374704`, VP Finance copied; a reply there would keep context |
| KPMG reply | `gmail_reply_to_message(message_id, body, reply_all, user_email)` | 17 | **`reply_all` defaults to false**: 207 of 213 stored replies went to the sender only, 6 used `reply_all`. KPMG's body says to reply to all recipients. No `cc`, `to` or `subject` parameter, so a run cannot add anyone |
| KPMG attachments | live-only `attachments[{filename, mime_type, data_b64}]` on reply and send; not in catalog; 0 uses | 0 | **Cannot produce the base shape.** Leonard attached 7 files in FY23, and 3 then 32 in FY24; a run cannot read Gmail attachments and would have to rebuild content. Do not grade an attached statement or Carta PDF; a text answer per numbered item is the buildable shape |
| Holder issue state and comments | `linear_update_issue(id, state, assignee, ...)`; `linear_create_comment(issueId, body, parentId)` | 30; 36 | Per issue, no bulk write. Live-only `linear_update_comment` (`id, body`) is not in catalog |
| Founders' reply | `slack_send_message`: **catalog says `channel, text, thread_ts, user`; every stored call used `channel_id, message`, plus `thread_ts` in 35 of 43** | 42 | Catalog is stale here. Refused with `not_in_channel` if not a member; Leonard is in `#winddown`, the DMs and `#executives`. Posts as the persona only |
| Calls to book | `gcal_create_event(calendarId, event)`; live-only `sendUpdates` default 'none' | 6 | Live text: no copy is placed on an attendee's calendar; guests are mailed only with `sendUpdates` all or externalOnly |
| New contact | `contacts_add_new_contact(first_name!, last_name!, email, job, ...)` | 6 | Sends already mint Other contacts |
| Trello | `trello_add_comment(cardId, text)`; `trello_create_card(idList, name, desc, ...)` | 12; 12 | Fine |
| Deck | `gslides_create_presentation(title, driveFileId)`, `gslides_batch_update(presentationId, requests)` | **0; 0** | Never run. `gdrive_copy_file` says a copied deck is empty. Do not make a deck a graded deliverable without a pre-check |

### `gmail_create_draft`: what the live text says, and how a draft reads back

- **Live description (FACT):** "Save an unsent draft (mirrors users.drafts.create); answers the Draft resource {id, message}, where the draft id equals its message id here."
- **Params (FACT).** `to` ("may be omitted on a draft"), `subject`, `body`, `cc`, `bcc`, `thread_id` ("Existing thread this draft replies within, matched exactly in this mailbox; omit for a new conversation. An empty string is refused with 400"), `user_email`. Live-only: `html_body`, `attachments`, `headers` (From, To, Cc, Bcc, Subject, Date, Message-ID, In-Reply-To, References and Delivered-To are refused).
- **Readback, four routes (FACT from live text):**
  1. `gmail_get_draft(draft_id, user_email, format default full, metadata_headers)`: `{id, message}`; a sent or received id is a 404. **Not in catalog.**
  2. `gmail_list_drafts(user_email, max_results, page_token, query, include_spam_trash)`: newest first, `{id, message:{id, threadId}}`, `nextPageToken`, `resultSizeEstimate`. **In catalog as `limit, user_email`** (live has no `limit`), so only `user_email` is safe in an Oracle Event.
  3. `gmail_search_messages(query="in:drafts ...")`: the grammar lists `in:drafts`.
  4. `gmail_update_draft` and `gmail_send_draft(draft_id, user_email)` exist; `gmail_update_draft` is not in catalog.
- **Run evidence.** 0 calls to any `gmail_*draft*` tool in 120 stored trajectory files (baselines, pre-checks, forensics). Nothing has been observed.
- **Base.** Leonard's mailbox has 0 messages labelled DRAFT (complete, 17,635 files). `gmail_messages` has no drafts table, so a seeded draft has no precedent and the plan should not seed one.
- **Verifier.** FACT: the platform verifier is a tool-using reader of final state ("I listed the LLC take-over project with linear_list_issues..."). INFERENCE: it can call the same draft tools, but whether it is given them, and acts as Leonard's mailbox, is unproven. `trajectory_ledger.py` line 571 already treats `gmail_create_draft` and `gmail_send_draft` as mail writes, so local forensics will see them.
- **Tokens.** 22 stored `gmail_send_message` calls used `PERSON_####_EMAIL` recipients without error. Untested on drafts, and 0 stored sends used `bcc`.
- **Draft limits.** A draft in a thread needs an explicit `to`: there is no `reply_all`, and threading headers cannot be set by hand. Whether `thread_id` alone sets In-Reply-To is unknown.

**Pre-check tests for decision 4:** one `gmail_create_draft` with a token `to`, then `gmail_list_drafts`, then `gmail_get_draft`; confirm the verifier reports the draft. Fallback if not: sends, or the notes as sections of one Doc.

### Writes that cannot produce the needed shape

| Wanted | Why not | Buildable shape |
|---|---|---|
| Reply with attached statements or the Carta PDF | Attachments return no bytes | Numbered text answers, or a note saying the file comes separately |
| Comment on a Doc | No comment tool for Drive, Docs, Sheets or Slides | Slack or mail note, or a Linear comment |
| Add a Cc to a reply | Reply has no `cc` | `reply_all` to the original set, or `gmail_send_message` with `thread_id` (which then needs full recipients) |
| Reply-all draft | Drafts have no `reply_all` | Spell out `to` and `cc` with `thread_id`, or send |
| Doc or Sheet straight into a folder | No parent parameter on the create | Create, then `gdrive_move_file`, or `gdrive_create_file` with `parentId` |
| Scheduled mail after the clock | Gmail has no schedule tool; only `slack_schedule_message` | Draft |
| A bulk state change in Linear | One issue per call | 26 calls; good for call count |

## I. Service table

Grades per Ask_Carriers §5 and §6b. ● = base precedent. ○ = no precedent or unproven rendering. "Job strength" is my judgement.

| Service | Seeded record | Real job in a stockholder close-out | Grade | Companion needed | Job strength |
|---|---|---|---|---|---|
| linear | 1 project (`ec2ea957-...`, `team_ENG`, lead Leonard, rule in `description`), 26 issues ENG-2438..2463, comments | Leonard's working tracker: one issue per non-founder holder, state = where that holder stands | description, state, assignee ●; comments ○ in §5, but ● under playbook S4 and §6b (rendered in real runs) | Issue `updated_at` >= newest comment; lifecycle stamps per state; comment before any close stamp | Strong for calls; comments are always read, so low for misses |
| gmail | KPMG FY25 root, new thread beside FY23 and FY24; optional follow-up | Griffin's yearly confirmation, as-of date and items in the body | body, headers, labels ● | `gmail_threads` row; inline items (no attachment) | Strong |
| gmail | Sunset list: `Sunset: <...>` from PERSON_2888 to Leonard | Notice rules from a non-owner | ● | `gmail_threads` row; must match the unread SOW | Strong, carries the closed rule |
| slack | Burst of 1-liners in `D04UP2L3E3S` or `D04UGG61DUM`, ts `1770934700`-`1770977000` | Founders settling who talks to whom | message text ● | sha id; no thread needed; keep to founders | Medium |
| gcal | 1-2 holds, `Leonard <> <name>` next week, Leonard sole attendee | A holder gets a call first, not a note | summary, time ●; description ○ | No attendee copies unless founders join; INT-11 decision recorded | Medium; found only by `gcal_search_events` because lists spill |
| gdocs | Doc 1 `f_a37b...`: Leonard's letter working copy in a shared Doc (base precedent `f_5a4fb6c74aab30e85771e5`) | Newest letter text, later than the `#winddown` draft: a real supersession | body_text ● | Drive row; identical sharing; `style_runs_json` inside body | Strong |
| gdocs | Doc 2 `f_762c...`: earlier outreach notes, superseded (LLC's "notes (Monday)" pattern) | Same-service decoy | ● | Same | Medium |
| gdrive | Folder `d_6010...` owned by Leonard, in his root, shared with founders | Home for the close-out files and the write target; a listing surfaces the sheet and deck | folder path, owner, sharing ● | None; each child repeats sharing. Rows for Doc, Sheet, deck | Strong as container; also required for the three below |
| gsheets | Sheet `f_5eca...`: `Investor ... (draft)`, one tab, header row plus a handful of partial rows, dated before the Feb 12 Carta terminations | Layout source and stale decoy (LLC's "LLC 90 days (draft)"). Must not be a full list | grid_json ●, prose cells ● | Drive row; `row_count` 1000, `column_count` 26 | Medium |
| gslides | Deck `f_75dd...`: Leonard's draft last update, 3-4 BLANK pages, title idiom `Harmony Games <Mon YY> Update` | A founder's outline of what investors hear; base has March 25 and August 25 updates | element text ●; notes ○ | Drive row; pages; elements | **Weakest.** LLC's deck had 0 reads in 6 runs. Sits in the folder to help; no graded fact only here |
| contacts | 2 rows: Bergmann `PERSON_0693_EMAIL`, Eren `PERSON_2275_EMAIL` (neither has a row) | Name to address for two token-only people; resolves the `patrick` collision | email, job ●; description ○ | None; `last_name` not null | Low but honest |
| trello | 1 card in To Do `640643a3fd8f3ca308d93195`, `idShort` 456, + createCard action, + 1 comment from a co-founder | Founders' own to-do: who owns each conversation | desc, comment ● | badges, `dateLastActivity`, action rows | Medium. Base card 801 stays untouched |

**Row tally (estimate).** Linear 1 + 26 + about 40 comments = 67; Gmail 5; Slack 8; GCal 3; Drive 5; Docs 2; Sheets 3; Slides 7; Contacts 2; Trello 3. Total about **105, under the 120-row floor**. Closing it honestly needs about 15 more rows, most naturally a second real comment on more issues (a 26-issue plan with 26 comments would land near 90) or more Slack lines. LLC reached 136 with 37 issues.

**Writable tables.** Every table named in this file is among the 64 in `sql_lint.py::WRITABLE_TABLES`. `linear_workflow_states`, `linear_project_teams`, `linear_project_members`, `contact_groups`, `contact_group_members` and `gcal_calendar_list` are not, and none is needed.

**Exactly-10 risk.** Snowflake and Confluence are barred from seeding, and GitHub has no honest job here, so losing any one of the ten fails the ≥ 10 floor. Slides and Contacts are the two to protect.

## J. What was not read or could not be done

- **No live tool was run.** All tool behaviour comes from stored run output or from `state_full.json`, which is an Oct 30 synth-cut sandbox. Where they disagree I used run output.
- **Not proven:** `bcc:` search; drafts of any kind; token recipients on drafts; `gdrive_search fullText` on Sheets or Slides; `gcal_list_events` on Leonard's calendar (inferred from other personas); `gslides` writes; the verifier's access to drafts.
- **Unread by rule:** every PDF and Gmail attachment, including the KPMG confirmation PDFs (the FY24 items come from Leonard's reply mirroring them), the signed Sunset SOW and the data licence. Any Sunset seed still needs decision 6.
- **Not checked:** Trello checklists; `gmail_label_user_counters` handling for seeded mail (no earlier task bumped them, as far as the SQL I read shows); Drive sidecars (not needed for natives). I read LLC, Claire and bridge SQL rows only, not every seeded row.
- **Not read in full:** the GitHub, Confluence and Snowflake sections of Ask_Carriers; `Hardness_Manifest_Spec.md` was searched for gate lines, not read end to end.
- **Counts differ from Ask_Carriers:** 170 contacts (it says 171), 11,130 events (11,233), 41 Linear users (42). I used what hg.py returns.
- Base collisions are checked against the universe only. Text mentions were scanned for Linear ids in Slack and GitHub, not in Drive or Gmail bodies.

