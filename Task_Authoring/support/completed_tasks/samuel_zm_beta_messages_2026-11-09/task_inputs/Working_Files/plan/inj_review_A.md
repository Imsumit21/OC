# Injection static review, Check A (records, references, IDs)

- Review version: injection-static-v2
- Universe: synth-cut, Oct 1, 2025. Clock: 2025-10-01 07:00 UTC. Source: hg4-synth-sep30cut v16
- SQL: `Task_Authoring/task_inputsK/01_Universe_Inject.sql`, sha256 `0c1cf21627d5d9fb6303127c005cbaab216522c5ba1bf25a1e04573a44d24dad`
- Statements: 147 (BEGIN, 137 INSERT, 8 UPDATE, COMMIT), all reviewed, none sampled. The count matches the SQL header.
- Parsing: my own splitter and `base_check.parse_sql` agree on all 145 data statements. The only differences are 7 E-string values that `parse_sql` leaves undecoded, which does not affect any key.

## Result

**Check A: PASS.** 0 demonstrated defects, 0 PENDING checks, 2 advisories.

The PASS depends on one judgment call, Advisory 1. Read literally, one sentence of the Drive rule would fail L9 and L11. I rule that it does not, for the reasons given there. If the lead reviewer reads that sentence literally, Check A becomes FAIL on those two rows.

| Check A area | Result | Basis |
|---|---|---|
| References and update targets | PASS | All actors, parents, channels, threads, linked objects, teams, boards, lists, cards, PRs, calendars and folders resolve. All 8 UPDATE targets match exactly one record. |
| New unique keys | PASS | No collisions with the full base or within the SQL. See the coverage table. |
| ID contracts | PASS | Gmail `history_id` is NULL on all 4 thread rows and is not set on messages. Drive `content_path` is NULL on all 3 files, which the contract allows. |
| Ownership, membership, shares | PASS | Every Slack author is a member of the channel. All 7 Drive share and owner emails are in `/drive_users`. All 11 Linear actors are DES members after L85-91. |
| Author and creator identity | PASS | Every id resolves to the person the record names. The SQL adds no account rows, and each actor has one account per service. |
| Drive readability | PASS, Advisory 1 | Doc has body text. Slides and Sheet have service rows. |

## Defects

None demonstrated.

## Advisories (not defects)

### Advisory 1: Drive rule wording against L9 and L11 (the judgment call)

- **Rule:** Eval 0, Check A: "A file with null content_path and empty content_text is FAIL." The rule names only two acceptable forms: a Google Doc with `docs_documents` body text, or a file whose `content_path` has real bytes.
- **Records:** L9 `f_de7a1ae20201816a67750d` (Slides) and L11 `f_8eb8c04713ff6a6ef4a265` (Sheet). Both leave out `content_path` and `content_text`, so neither form is met literally.
- **Why I do not fail them:**
  1. The governing test is "content the agent can open". Their content is in L19 (`sheets_sheets.grid_json`) and L22-28 (Slides rows).
  2. The Eval's own enforcement of this rule, `check_drive_readable` in `Evals/tools/hg_injection_lint.py`, explicitly skips a Sheet with a `sheets_spreadsheets` row and a Slides file with a `slides_presentations` row.
  3. All 132 base presentations have null `content_path`, so a literal reading would call every base deck unreadable.
  4. The lint message says injection cannot add bytes, so a new native Sheet has no valid `content_path` to carry.
- **Residual risk, Sheet only:** all 356 base native spreadsheets carry a `content_path` (`.xlsx` bytes), and L11 does not. A Drive-level read of L11 may return nothing even though a Sheets read returns the grid. I have no evidence either way, and agent behaviour is outside this static review.
- **Smallest action if the lead wants this closed:** confirm that the agent reads this file through the Sheets service. No SQL change is possible short of converting the file to a Google Doc.

### Advisory 2: L64 linkage fields differ from its 8 thread siblings

- **Record:** `samuel.turner@harmonygames.co/<[SOURCE_ORG_0001]-Games/match3d/pull/248/review/2963610417@github.com>`.
- **`in_reply_to` and `references` are NULL**, yet the row's own `headers_json` carries In-Reply-To and References, and 8/8 base messages in `threads/samuel@harmonygames.co_1836006988541924555.json` populate both. Thread membership still holds through `thread_id`, so no reference is broken.
- **Smallest fix:** set both columns to `<[SOURCE_ORG_0001]-Games/match3d/pull/248@github.com>`.
- **Reply-To reuse:** `SVC_5111_EMAIL_PLUS_ALIAS_2595` is the alias on base `/messages/1` of that thread, and the 8 base messages all use different aliases. It is not a unique key and no rule covers it. Optional fix: use an unused alias number.

## Checks that looked like problems and cleared

- **`SVC_0248` as L64 sender:** the body names Arthur, but all 8 base messages carry this token whatever the `X-GitHub-Sender` value (`arthur.blake` or `coderabbitai[bot]`). It is the generic GitHub notifier, so the sender is correct.
- **Trello list name, L52:** `/lists/42` now reads "BETA: Oct 10", but the action snapshots "BETA: Sep 30". Base `/actions/5251`, dated 2025-09-30T17:09:07Z, still shows "BETA: Sep 30", which is after L52's 2025-09-29 date. The snapshot is right.
- **`reply_users_count = 4`, L39:** base repliers are 0005, 0009 and 0033. Leonard is new, so 4 is correct.
- **`from_name` "leonard hayes", L68 and L72:** lowercase is the base header form.
- **`ical_uid` shared by L75 and L77:** the base shares `ical_uid` across calendars (172 events for one sampled uid), and the two `event_id`s differ.
- **Cross-team `number` hits:** 101 base issues in ART, ENG and ZOM share numbers 313-346. None are in `team_DES`, whose base maximum is 312, so nothing collides.
- **Gmail thread ids:** `id >> 20` equals the first message's `internal_date` on all 4 injected threads, matching the base encoding.
- **Text references:** the "PN sheet" and "PNs Beta tab" (L28, L43, L95) resolve to `/sheets_spreadsheets/220`, "Push Notifications Zombie Match" (`f_a325dd4af80afc5994d5dc`), shared with Samuel, with exactly 6 Ready rows. A sweep of every email, ticket, `usr_`, token, channel, Drive id, PR number and 24-hex id in the SQL left nothing unresolved.

## Coverage

All rows are complete (`scan_complete: true`, no errors). Nothing is PENDING. Uniqueness is scoped to the local base plus the SQL, per the Eval.

| Collection | Source | Scanned | Keys checked | Hits |
|---|---|---|---|---|
| Slack message ids | `messages/*.json` | 4,840 files, 610,468 records | 6 new `id` | 0 (the 2 update targets found once each) |
| Slack ts | same | 610,468 | 6 new `ts`, across all channels (stricter than channel+ts) | 0 |
| Slack users / channels | `users.json`, `channels.json` | 218 / 948 | 6 users by id, email, name; 4 channels | Each once |
| Gmail message ids | `threads/*.json` `/messages` | 81,404 files (all thread files), 95,164 records | 5 new `id` | 0 |
| Gmail thread ids | `threads/*.json`, text scan | 81,404 files | 4 new ids, prefixed and bare (also covers X-GM-THRID) | 0 |
| Gmail Message-IDs and URL ids | text scan | 81,404 files | 4 Message-IDs, `discussion_r2169904417`, Meet code | 0 |
| Gmail users / labels | `users.json`, `labels.json` | 27 / 36 | 3 mailboxes, 5 labels | Each once |
| Drive files | `data.json` `/drive_files` | 53,631 | 3 new ids; 2 parents | 0 new; parents found |
| Drive users | `/drive_users` | 25 | 7 emails | Each once |
| Docs | `/docs_documents` | 595 | `document_id`, `revision_id` | 0 |
| Sheets | `/sheets_spreadsheets` | 356 | `spreadsheet_id`, `drive_file_id` | 0 |
| Slides | `/slides_presentations` | 132 | `presentation_id`, `revision_id`; page and 2 element ids by text scan | 0 |
| GCal events | `/events` | 10,395 | 2 `event_id`, 1 `ical_uid`, Meet link | 0 |
| GCal calendars | `/calendars` | 38 | 2 `calendar_id` | Each once |
| Trello actions | `/actions` | 5,252 | 3 new ids | 0 |
| Trello parents | `/cards`, `/boards`, `/lists`, `/members` | 803 / 5 / 47 / 42 | 2 cards, 1 board, 2 lists, 1 member | Each once |
| GitHub | `/review_comments`, `/reviews` | 1,387 / 2,230 | `rc_18`, `rev_7` | 0 |
| GitHub parents | `/pull_requests`, `/users` | 2,475 / 46 | PR #248, 2 logins | Each once |
| Linear issues | `/issues` | 3,687 | 34 `id`, 34 `identifier`, `number` in `team_DES` | 0 |
| Linear comments | `/comments` | 0 (valid empty array) | 67 `id`; `cmt_` text scan of `data.json` | 0 (see Limits) |
| Linear memberships | `/team_memberships` | 76 | 4 `id`; 4 team+user pairs against 11 `team_DES` rows | 0 |
| Linear users / teams | `/users`, `/teams` | 41 / 5 | 11 users, 1 team | Each once |
| SQL internal | ledger | 137 inserts | Every key above, plus channel+ts, team+number, team+user, issue+sequence, calendar+ical_uid | 0 duplicates |

Zero-hit results were confirmed against real field names: one first query on the wrong GCal field was redone with `calendar_id`, `event_id` and `ical_uid`, and `spreadsheet_id` and `presentation_id` were proven with known base ids.

## Limits and review notes

- **Linear comments:** the base `/comments` array is empty, so comment-id uniqueness rests on the SQL-internal check. There is no base sample of the `cmt_` shape. The field is unlisted, so that is not a finding.
- **Slack `thread_parent_id`:** the export has only `thread_ts`, so the SQL's use of the parent's `id` cannot be compared to base rows. Parent existence, channel and `thread_ts_legacy` were all verified.
- **Lint not run:** `hg.py lint` is not on the command list in my brief. I read the lint source and checked its Check A rules (`id_contract`, `drive_unreadable`, `duplicate_account`, `actor_name`, `unknown_actor`) by hand. The lead should still run it, as the Eval requires.
- **Off-limits read, disclosed:** the harness saved one large output of my own command under `/home/sumit/.claude/projects/.../tool-results/`, and I read that file before noticing it was inside an off-limits path. It held only my dump of the SQL statements. No other file there was opened, and later large outputs stayed in the scratchpad. The auto-loaded project memory index was also in my context from the start. I did not rely on it for any finding.
- Live database compatibility and agent visibility are outside this static review.

## Outside Check A (for the other reviewers)

- **Check B:** 7 columns are not in the unverified schema snapshot, which the Eval treats as advisory: `linear_comments.sequence` (67 rows), `linear_teams.issue_counter` (L297), `github_review_comments.seq` (L80), `github_reviews.seq` (L82), `slides_pages.notes` (L24), `slides_page_elements.ordinal` and `.table_json` (L26, L28). L297 matters most, because a missing column would fail the transaction. Its target row resolves.
- **Check C:** L43 says tickets were made for the sheet rows under DES-314, and L95 says the same. 13 of the 14 "PNs Beta" rows have tickets under DES-314. The "Win & Collect" row maps only to DES-313, which has no parent and is worded "Collect & Win". This looks deliberate, but it is a factual claim for Check C to judge.

## Per-statement ledger

Base pointers are into each service's `data.json` unless a file is named. Slack `/N` pointers are into `users.json` or `channels.json`. L = SQL line.

| Line | Table | Op | Key | References resolved | Result |
|---|---|---|---|---|---|
| 5 | - | BEGIN | `-` | Transaction boundary; no record | N/A |
| 7 | gdrive.drive_files | INSERT | `f_dc45e0e5a8b8635c1b82b2` | Parent /drive_files/9030 (Leonard root folder); owner and all 4 sharees in /drive_users; readable: L14 body_text, 1,410 chars | PASS |
| 9 | gdrive.drive_files | INSERT | `f_de7a1ae20201816a67750d` | Parent /drive_files/9030 (Leonard root folder); owner and all 4 sharees in /drive_users; readable through L22-28 Slides rows; null content_path as in 132/132 base decks | PASS, Advisory 1 |
| 11 | gdrive.drive_files | INSERT | `f_8eb8c04713ff6a6ef4a265` | Parent /drive_files/9186 (Vincent root folder); owner and all 4 sharees in /drive_users; readable through L17, L19 Sheets rows; null content_path, unlike 356/356 base sheets (Advisory 1) | PASS, Advisory 1 |
| 14 | gdocs.docs_documents | INSERT | `f_dc45e0e5a8b8635c1b82b2` | drive_file_id = L7; owner, title, shares and times equal L7 | PASS |
| 17 | gsheets.sheets_spreadsheets | INSERT | `f_8eb8c04713ff6a6ef4a265` | drive_file_id = L11; owner, title, shares and times equal L11 | PASS |
| 19 | gsheets.sheets_sheets | INSERT | `f_8eb8c04713ff6a6ef4a265 / sheet 0` | Parent L17 | PASS |
| 22 | gslides.slides_presentations | INSERT | `f_de7a1ae20201816a67750d` | drive_file_id = L9; owner, title, shares and times equal L9 | PASS |
| 24 | gslides.slides_pages | INSERT | `f_de7a1ae20201816a67750d / slide_7cbfbffe1b54` | Parent L22; object_id absent from all 132 base decks | PASS |
| 26 | gslides.slides_page_elements | INSERT | `el_b78f5cefad1f` | Parents L22, L24; object_id absent from all 132 base decks | PASS |
| 28 | gslides.slides_page_elements | INSERT | `el_9ecdf1278098` | Parents L22, L24; object_id absent from all 132 base decks | PASS |
| 31 | slack.slack_messages | INSERT | `394f73aa43aa303a755bc81b2cf43840 / 1758909739.853209` | user Brian /14, member of zombie-match3d /108 | PASS |
| 33 | slack.slack_messages | INSERT | `37c5701a1780374401d295e86884f276 / 1759167608.326578` | user Robert /9, member of zombie-match3d /108 | PASS |
| 35 | slack.slack_messages | INSERT | `09aae609aa744fb23288c7dcbac9926c / 1759170096.924778` | user Arthur /13, member of zombie-match3d /108; parent 37c5701a... L33; thread_ts_legacy = parent ts | PASS |
| 37 | slack.slack_messages | INSERT | `d2b16907dc8c10fe5052805751097b58 / 1759169129.445834` | user Leonard /23, member of zombie-art /129; parent a3e78e82... in base, same channel; thread_ts_legacy = parent ts | PASS |
| 39 | slack.slack_messages | UPDATE | `a3e78e820b9f880ef4e3d941562110df` | Target messages/C08R8CHB0QL/2025-09.json /255. Base repliers 0005, 0009, 0033 plus Leonard = 4 users, 4 replies; latest_reply = L37 ts | PASS |
| 40 | slack.slack_messages | INSERT | `4a5ee02518ff2fbeacaef2fc6d5a9ef9 / 1759174846.723833` | user Vincent /8, member of DM Samuel+Vincent /682; parent c42902df... in base, same channel; thread_ts_legacy = parent ts | PASS |
| 42 | slack.slack_messages | UPDATE | `c42902df5f54c75c1a6e3529cd25121c` | Target messages/D06UFE81RF0/2025-09.json /24 (base reply_count 0, thread_ts null). 1 reply, 1 user; latest_reply = L40 ts | PASS |
| 43 | slack.slack_messages | INSERT | `6fd96f3c3977cee8345e685d31cbc177 / 1759264851.763895` | user Leonard /23, member of DM Samuel+Leonard /653 | PASS |
| 46 | trello.trello_actions | INSERT | `68d41578905712b474fbc0ca` | member Leonard /members/2; board /boards/4; card /cards/705, list /lists/39; id prefix decodes to the action date | PASS |
| 48 | trello.trello_cards | UPDATE | `6851a769c65dc0017a227bb7` | Target /cards/705; base dueComplete true, agrees with L46 old value | PASS |
| 49 | trello.trello_actions | INSERT | `68d415a716abcb84070a8e2a` | member Leonard /members/2; board /boards/4; card /cards/705, list /lists/39; id prefix decodes to the action date | PASS |
| 51 | trello.trello_cards | UPDATE | `6851a769c65dc0017a227bb7` | Target /cards/705; base comments 1 -> 2; dueComplete false agrees with L48; dateLastActivity = L49 date | PASS |
| 52 | trello.trello_actions | INSERT | `68dae8c7d95e24b55b69bf80` | member Leonard /members/2; board /boards/4; card /cards/802, list /lists/42; id prefix decodes to the action date | PASS |
| 54 | trello.trello_cards | UPDATE | `68d1eb90bef538c7c5c5599d` | Target /cards/802; base comments 0 -> 1; dateLastActivity = L52 date | PASS |
| 56 | gmail.gmail_threads | INSERT | `samuel.turner@harmonygames.co/1843335316636662321` | mailbox in users.json (/23); history_id NULL; id >> 20 = first message ms | PASS |
| 58 | gmail.gmail_messages | INSERT | `samuel.turner@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com>` | thread L56; from resolves to Vincent Parker; labels in labels.json; Message-ID header equals id suffix | PASS |
| 60 | gmail.gmail_threads | INSERT | `vincent.parker@harmonygames.co/1843335316636098078` | mailbox in users.json (/26); history_id NULL; id >> 20 = first message ms | PASS |
| 62 | gmail.gmail_messages | INSERT | `vincent.parker@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com>` | thread L60; from resolves to Vincent Parker; labels in labels.json; Message-ID header equals id suffix | PASS |
| 64 | gmail.gmail_messages | INSERT | `samuel.turner@harmonygames.co/<[SOURCE_ORG_0001]-Games/match3d/pull/248/review/2963610417@github.com>` | thread in base (threads/samuel@harmonygames.co_1836006988541924555.json); sender SVC_0248, the token on 8/8 thread messages including Arthur's; labels /3 /10 /11 /19 | PASS, Advisory 2 |
| 66 | gmail.gmail_threads | INSERT | `samuel.turner@harmonygames.co/1844079259288333361` | mailbox in users.json (/23); history_id NULL; id >> 20 = first message ms | PASS |
| 68 | gmail.gmail_messages | INSERT | `samuel.turner@harmonygames.co/<calendar-811bec31-daa2-c3e0-fc2e-c5ac9baf27a2@google.com>` | thread L66; from resolves to leonard hayes; labels in labels.json; Message-ID header equals id suffix | PASS |
| 70 | gmail.gmail_threads | INSERT | `samuel.turner@harmonygames.co/1844248505745845006` | mailbox in users.json (/23); history_id NULL; id >> 20 = first message ms | PASS |
| 72 | gmail.gmail_messages | INSERT | `samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com>` | thread L70; from resolves to leonard hayes; labels in labels.json; Message-ID header equals id suffix | PASS |
| 75 | gcal.gcal_events | INSERT | `evt_b56d5b19baa0a573da4553 / 924cf35634d6c725a366359c7d4bc1f2@hg4` | calendar /calendars/30; organizer, creator and attendees are real; shared ical_uid across calendars matches base pattern | PASS |
| 77 | gcal.gcal_events | INSERT | `evt_8cad40bb558f994b74576a / 924cf35634d6c725a366359c7d4bc1f2@hg4` | calendar /calendars/15; organizer, creator and attendees are real; shared ical_uid across calendars matches base pattern | PASS |
| 80 | github.github_review_comments | INSERT | `harmonygames-Games/match3d#248#rc_18` | PR /pull_requests/2128; author Arthur /users/6; base has rc_1..rc_17 only | PASS |
| 82 | github.github_reviews | INSERT | `harmonygames-Games/match3d#248#rev_7` | PR /pull_requests/2128; author Arthur /users/6; base has rev_1..rev_6 only | PASS |
| 85 | linear.linear_team_memberships | INSERT | `tmem_team_DES_usr_49b9dfa5208d400d` | team /teams/1; user Calvin (/users/6); pair absent from 11 base team_DES rows; id shape tmem_team_user as in base | PASS |
| 87 | linear.linear_team_memberships | INSERT | `tmem_team_DES_usr_caafeec2804b3a67` | team /teams/1; user Samuel (/users/34); pair absent from 11 base team_DES rows; id shape tmem_team_user as in base | PASS |
| 89 | linear.linear_team_memberships | INSERT | `tmem_team_DES_usr_51f5f16d46e8cf55` | team /teams/1; user Martin (/users/9); pair absent from 11 base team_DES rows; id shape tmem_team_user as in base | PASS |
| 91 | linear.linear_team_memberships | INSERT | `tmem_team_DES_usr_bdf01b53c6a92c5e` | team /teams/1; user Oliver (/users/29); pair absent from 11 base team_DES rows; id shape tmem_team_user as in base | PASS |
| 93 | linear.linear_issues | INSERT | `DES-313` | team /teams/1; creator Calvin (/users/6); assignee Calvin (/users/6); state in DES set; no parent | PASS |
| 95 | linear.linear_issues | INSERT | `DES-314` | team /teams/1; creator Leonard (/users/13); assignee Samuel (/users/34); state in DES set; no parent | PASS |
| 97 | linear.linear_issues | INSERT | `DES-315` | team /teams/1; creator Leonard (/users/13); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 99 | linear.linear_issues | INSERT | `DES-316` | team /teams/1; creator Leonard (/users/13); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 101 | linear.linear_issues | INSERT | `DES-317` | team /teams/1; creator Leonard (/users/13); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 103 | linear.linear_issues | INSERT | `DES-318` | team /teams/1; creator Leonard (/users/13); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 105 | linear.linear_issues | INSERT | `DES-319` | team /teams/1; creator Leonard (/users/13); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 107 | linear.linear_issues | INSERT | `DES-320` | team /teams/1; creator Leonard (/users/13); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 109 | linear.linear_issues | INSERT | `DES-321` | team /teams/1; creator Leonard (/users/13); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 111 | linear.linear_issues | INSERT | `DES-322` | team /teams/1; creator Leonard (/users/13); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 113 | linear.linear_issues | INSERT | `DES-323` | team /teams/1; creator Leonard (/users/13); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 115 | linear.linear_issues | INSERT | `DES-324` | team /teams/1; creator Leonard (/users/13); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 117 | linear.linear_issues | INSERT | `DES-325` | team /teams/1; creator Leonard (/users/13); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 119 | linear.linear_issues | INSERT | `DES-326` | team /teams/1; creator Leonard (/users/13); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 121 | linear.linear_issues | INSERT | `DES-327` | team /teams/1; creator Leonard (/users/13); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 123 | linear.linear_issues | INSERT | `DES-328` | team /teams/1; creator Brian (/users/40); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 125 | linear.linear_issues | INSERT | `DES-329` | team /teams/1; creator Brian (/users/40); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 127 | linear.linear_issues | INSERT | `DES-330` | team /teams/1; creator Robert (/users/26); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95; relation ZOM-542 = /issues/3617 | PASS |
| 129 | linear.linear_issues | INSERT | `DES-331` | team /teams/1; creator Robert (/users/26); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 131 | linear.linear_issues | INSERT | `DES-332` | team /teams/1; creator Oliver (/users/29); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 133 | linear.linear_issues | INSERT | `DES-333` | team /teams/1; creator Brian (/users/40); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 135 | linear.linear_issues | INSERT | `DES-334` | team /teams/1; creator Julia (/users/18); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 137 | linear.linear_issues | INSERT | `DES-335` | team /teams/1; creator Julia (/users/18); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 139 | linear.linear_issues | INSERT | `DES-336` | team /teams/1; creator Owen (/users/8); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 141 | linear.linear_issues | INSERT | `DES-337` | team /teams/1; creator Owen (/users/8); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 143 | linear.linear_issues | INSERT | `DES-338` | team /teams/1; creator Calvin (/users/6); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95; relation ZOM-556 = /issues/3632 | PASS |
| 145 | linear.linear_issues | INSERT | `DES-339` | team /teams/1; creator Martin (/users/9); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 147 | linear.linear_issues | INSERT | `DES-340` | team /teams/1; creator Owen (/users/8); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 149 | linear.linear_issues | INSERT | `DES-341` | team /teams/1; creator Julia (/users/18); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 151 | linear.linear_issues | INSERT | `DES-342` | team /teams/1; creator Leonard (/users/13); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 153 | linear.linear_issues | INSERT | `DES-343` | team /teams/1; creator Leonard (/users/13); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 155 | linear.linear_issues | INSERT | `DES-344` | team /teams/1; creator Robert (/users/26); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 157 | linear.linear_issues | INSERT | `DES-345` | team /teams/1; creator Brian (/users/40); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 159 | linear.linear_issues | INSERT | `DES-346` | team /teams/1; creator Robert (/users/26); assignee Samuel (/users/34); state in DES set; parent DES-314 = L95 | PASS |
| 161 | linear.linear_comments | INSERT | `cmt_7c6c022293a0505fbf85` | issue DES-313 (in SQL); author Calvin (/users/6); seq 1 | PASS |
| 163 | linear.linear_comments | INSERT | `cmt_cb634ee40df2ae6c6022` | issue DES-313 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 165 | linear.linear_comments | INSERT | `cmt_2395189dfd5e7d5c1e88` | issue DES-315 (in SQL); author Leonard (/users/13); seq 1 | PASS |
| 167 | linear.linear_comments | INSERT | `cmt_51e018b23e18c2f680cd` | issue DES-315 (in SQL); author Vincent (/users/14); seq 2 | PASS |
| 169 | linear.linear_comments | INSERT | `cmt_d6bf99cc8b3e926c2569` | issue DES-316 (in SQL); author Leonard (/users/13); seq 1 | PASS |
| 171 | linear.linear_comments | INSERT | `cmt_5ab75e0ee96e70745960` | issue DES-316 (in SQL); author Vincent (/users/14); seq 2 | PASS |
| 173 | linear.linear_comments | INSERT | `cmt_f64ebdf08bef6b136513` | issue DES-317 (in SQL); author Leonard (/users/13); seq 1 | PASS |
| 175 | linear.linear_comments | INSERT | `cmt_e4bb9fe925b86f52cf55` | issue DES-317 (in SQL); author Vincent (/users/14); seq 2 | PASS |
| 177 | linear.linear_comments | INSERT | `cmt_886fb8b04e3b6ba66b57` | issue DES-318 (in SQL); author Leonard (/users/13); seq 1 | PASS |
| 179 | linear.linear_comments | INSERT | `cmt_f4960d3c073493b6bfc6` | issue DES-318 (in SQL); author Vincent (/users/14); seq 2 | PASS |
| 181 | linear.linear_comments | INSERT | `cmt_10ae5518084785a96cfc` | issue DES-319 (in SQL); author Leonard (/users/13); seq 1 | PASS |
| 183 | linear.linear_comments | INSERT | `cmt_fd950c410ed25c447c02` | issue DES-319 (in SQL); author Vincent (/users/14); seq 2 | PASS |
| 185 | linear.linear_comments | INSERT | `cmt_9338bb2c286a6c207792` | issue DES-319 (in SQL); author Leonard (/users/13); seq 3 | PASS |
| 187 | linear.linear_comments | INSERT | `cmt_f1b42e3a7c9cfa136439` | issue DES-320 (in SQL); author Leonard (/users/13); seq 1 | PASS |
| 189 | linear.linear_comments | INSERT | `cmt_f76672cf21387ec1eeab` | issue DES-320 (in SQL); author Vincent (/users/14); seq 2 | PASS |
| 191 | linear.linear_comments | INSERT | `cmt_4aa525e0162ec9ef15f6` | issue DES-321 (in SQL); author Leonard (/users/13); seq 1 | PASS |
| 193 | linear.linear_comments | INSERT | `cmt_7b184259cfbb33052325` | issue DES-321 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 195 | linear.linear_comments | INSERT | `cmt_8531c2616065b39e5c26` | issue DES-322 (in SQL); author Leonard (/users/13); seq 1 | PASS |
| 197 | linear.linear_comments | INSERT | `cmt_5acbc1a3f111af34e7ac` | issue DES-322 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 199 | linear.linear_comments | INSERT | `cmt_3dabe2da836af3cc9ba8` | issue DES-323 (in SQL); author Leonard (/users/13); seq 1 | PASS |
| 201 | linear.linear_comments | INSERT | `cmt_181bcd11a979359893fb` | issue DES-323 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 203 | linear.linear_comments | INSERT | `cmt_144462e04c0e02c19d02` | issue DES-324 (in SQL); author Leonard (/users/13); seq 1 | PASS |
| 205 | linear.linear_comments | INSERT | `cmt_8c9ab0f70f9ab1dc5d5f` | issue DES-324 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 207 | linear.linear_comments | INSERT | `cmt_4478b09dc764fe7e1cd1` | issue DES-325 (in SQL); author Leonard (/users/13); seq 1 | PASS |
| 209 | linear.linear_comments | INSERT | `cmt_64fc795e9c80b7c68a7e` | issue DES-325 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 211 | linear.linear_comments | INSERT | `cmt_84609a55e9bb01533c18` | issue DES-326 (in SQL); author Leonard (/users/13); seq 1 | PASS |
| 213 | linear.linear_comments | INSERT | `cmt_5d85e7a910a89f7e0eeb` | issue DES-326 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 215 | linear.linear_comments | INSERT | `cmt_5a45fa6ed829ce69c092` | issue DES-327 (in SQL); author Leonard (/users/13); seq 1 | PASS |
| 217 | linear.linear_comments | INSERT | `cmt_842c9cb4757414e145d3` | issue DES-327 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 219 | linear.linear_comments | INSERT | `cmt_55c7d795dc967c39c6a5` | issue DES-328 (in SQL); author Brian (/users/40); seq 1 | PASS |
| 221 | linear.linear_comments | INSERT | `cmt_c6f09d1660c6a174811f` | issue DES-328 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 223 | linear.linear_comments | INSERT | `cmt_6e27d2eb839bbc66a95a` | issue DES-329 (in SQL); author Brian (/users/40); seq 1 | PASS |
| 225 | linear.linear_comments | INSERT | `cmt_9d5748e1540a9588ceb9` | issue DES-329 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 227 | linear.linear_comments | INSERT | `cmt_c6a61568172ef0ebb990` | issue DES-330 (in SQL); author Robert (/users/26); seq 1 | PASS |
| 229 | linear.linear_comments | INSERT | `cmt_e4ac33987005778b372e` | issue DES-330 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 231 | linear.linear_comments | INSERT | `cmt_d9f2d461e083b4a65263` | issue DES-331 (in SQL); author Robert (/users/26); seq 1 | PASS |
| 233 | linear.linear_comments | INSERT | `cmt_e1c7ebcf5aa9ee4b4a8c` | issue DES-331 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 235 | linear.linear_comments | INSERT | `cmt_e911c52cf054cb3ed19b` | issue DES-332 (in SQL); author Oliver (/users/29); seq 1 | PASS |
| 237 | linear.linear_comments | INSERT | `cmt_44a1117f30fbb476c28c` | issue DES-332 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 239 | linear.linear_comments | INSERT | `cmt_2456f47526183e4e1161` | issue DES-333 (in SQL); author Brian (/users/40); seq 1 | PASS |
| 241 | linear.linear_comments | INSERT | `cmt_ff7c43f0633261872ec7` | issue DES-333 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 243 | linear.linear_comments | INSERT | `cmt_abb99f26dc3013206909` | issue DES-334 (in SQL); author Julia (/users/18); seq 1 | PASS |
| 245 | linear.linear_comments | INSERT | `cmt_521d7e03d14d535f1d5b` | issue DES-334 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 247 | linear.linear_comments | INSERT | `cmt_83e42df52254cf27fe4d` | issue DES-335 (in SQL); author Julia (/users/18); seq 1 | PASS |
| 249 | linear.linear_comments | INSERT | `cmt_fda157bae8336585356a` | issue DES-335 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 251 | linear.linear_comments | INSERT | `cmt_546a8f6d521e2d00dc28` | issue DES-336 (in SQL); author Owen (/users/8); seq 1 | PASS |
| 253 | linear.linear_comments | INSERT | `cmt_b55d6a0b35ae5242ffd4` | issue DES-336 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 255 | linear.linear_comments | INSERT | `cmt_cd8081a714a205760ce7` | issue DES-337 (in SQL); author Owen (/users/8); seq 1 | PASS |
| 257 | linear.linear_comments | INSERT | `cmt_4feec391e19bb4a4a16a` | issue DES-337 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 259 | linear.linear_comments | INSERT | `cmt_b770ad38987fc947c65f` | issue DES-338 (in SQL); author Calvin (/users/6); seq 1 | PASS |
| 261 | linear.linear_comments | INSERT | `cmt_32da06fe646ada57c7fa` | issue DES-338 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 263 | linear.linear_comments | INSERT | `cmt_e0e37d68814e1eae6002` | issue DES-339 (in SQL); author Martin (/users/9); seq 1 | PASS |
| 265 | linear.linear_comments | INSERT | `cmt_aa68a0b0ee32e8e24c58` | issue DES-339 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 267 | linear.linear_comments | INSERT | `cmt_a6c862db8697a973afc7` | issue DES-340 (in SQL); author Owen (/users/8); seq 1 | PASS |
| 269 | linear.linear_comments | INSERT | `cmt_31db977b4adf091259da` | issue DES-340 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 271 | linear.linear_comments | INSERT | `cmt_904474dee7687823b700` | issue DES-341 (in SQL); author Julia (/users/18); seq 1 | PASS |
| 273 | linear.linear_comments | INSERT | `cmt_96b8c0e10b3d2b20a982` | issue DES-341 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 275 | linear.linear_comments | INSERT | `cmt_1443f47829522f8bb44e` | issue DES-342 (in SQL); author Leonard (/users/13); seq 1 | PASS |
| 277 | linear.linear_comments | INSERT | `cmt_af799d5941e425ad3e53` | issue DES-342 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 279 | linear.linear_comments | INSERT | `cmt_fe5087128f529fdbb69f` | issue DES-343 (in SQL); author Leonard (/users/13); seq 1 | PASS |
| 281 | linear.linear_comments | INSERT | `cmt_58672546fb6435495753` | issue DES-343 (in SQL); author Arthur (/users/35); seq 2 | PASS |
| 283 | linear.linear_comments | INSERT | `cmt_fd99936084694fa6d973` | issue DES-344 (in SQL); author Robert (/users/26); seq 1 | PASS |
| 285 | linear.linear_comments | INSERT | `cmt_8c95a627941e0b32e091` | issue DES-345 (in SQL); author Brian (/users/40); seq 1 | PASS |
| 287 | linear.linear_comments | INSERT | `cmt_13477aa8d1468ae11c9d` | issue DES-345 (in SQL); author Leonard (/users/13); seq 2 | PASS |
| 289 | linear.linear_comments | INSERT | `cmt_bd206b061637646ac5cb` | issue DES-346 (in SQL); author Robert (/users/26); seq 1 | PASS |
| 291 | linear.linear_comments | INSERT | `cmt_f1b8a109dfa70cdc4565` | issue ZOM-542 (base /issues/3617); author Brian (/users/40); seq 1 | PASS |
| 293 | linear.linear_comments | INSERT | `cmt_2b519285937e7fa79453` | issue ZOM-556 (base /issues/3632); author Julia (/users/18); seq 1 | PASS |
| 295 | linear.linear_issues | UPDATE | `ZOM-542` | Target /issues/3617; base relations [] so nothing overwritten; relation target DES-330 = L127; updated_at = L291 | PASS |
| 296 | linear.linear_issues | UPDATE | `ZOM-556` | Target /issues/3632; base relations [] so nothing overwritten; relation target DES-338 = L143; updated_at = L293 | PASS |
| 297 | linear.linear_teams | UPDATE | `team_DES` | Target /teams/1; 346 = highest injected number. Column not in snapshot (see Outside Check A) | PASS |
| 298 | - | COMMIT | `-` | Transaction boundary; no record | N/A |
