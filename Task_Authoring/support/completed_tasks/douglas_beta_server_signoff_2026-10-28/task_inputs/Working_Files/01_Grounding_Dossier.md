# Grounding Dossier — dg-beta-server-signoff (persona Douglas, Long Horizon, effective profile long)

Implements `01_Scenario_Design.md` v2 (scenario gate PASS) as `task_inputs/01_Universe_Inject.sql`: INSERT-only rows over 10 schemas (gdrive, gdocs, gsheets, confluence, slack, trello, gmail, gcal, github, linear). Builders: `support/task_work/dg_beta_server/` (`mint_ids.py`, `build_sql.py`, `build_final_manifest.py`, `build_dossier.py`; ids in `minted_ids.json`, SQL keys in `sql_ids.json`). Clock 2025-10-01T00:00Z; latest seeded timestamp 2025-09-30T21:12:44Z (Arthur's ask, D05QQF7V404/1759266764.508127). Revisions 5, 6 and 7 (§13) are hardening rounds 1, 2 and 3 (`01a_Hardening_Report.md`).

## 1.A Structural

Columns from `references/universe_schema_live.json` (NOT NULL marked *); base counts and sample ids read from the exports.

| Table | Columns used (NOT NULL *) | Base count · samples | Timestamp format / notes |
|---|---|---|---|
| slack.slack_messages | id*, ts*, channel_id*, type*, user_id, text*, thread_parent_id, thread_ts_legacy, reply_count*, reply_users_count*, latest_reply, is_activity_message*, reactions_json*, files_json*, attachments_json*, created_at*, metadata_json* | 687,230 · D079SNE2TL4/1759256193.859279, D05QQF7V404/1757975508.211599, C0880U9751A/1757618419.809199 | ts 6 decimals; id = sha256(channel|ts)[:32]; replies carry parent id + thread_ts_legacy (sample_task_01 shape) |
| gmail.gmail_threads / gmail_messages | id*, thread_id*, user_email*, label_ids_json, internal_date, date, subject, from_email, to_json, cc_json, body_text, headers_json, … | 88,726 thread files · douglas@harmonygames.co_1829035630999538536.json | date ISO-Z, internal_date ms; ids are the mailbox plus the RFC Message-ID, and the mailbox plus the numeric thread id |
| gcal.gcal_events | event_id*, calendar_id*, summary, start_ts, end_ts, start_json, end_json, organizer_email, attendees_json, status, ical_uid, created, updated, sequence | 11,233 · evt_00009bfb80dabb15aa5bb5, evt_0006932921e100bf00418e | one row per attendee calendar, self:true on the owner copy; ical_uid 32 hex@hg4 |
| gdrive.drive_files / gdocs.docs_documents / gsheets.* | id*, name, mime_type, parents_json, owner_email, shared_with_emails_json, shared_roles_json, modified_time, created_time; docs body_text, style_runs_json; sheets grid_json | 53,866 drive · 633 docs · 398 sheets · f_00117462881159eceee63e, f_00c30de5acd0cf7656c140 | folders d_ + 22 hex, files f_ + 22 hex; same id in drive and docs/sheets rows |
| trello.trello_cards / trello_actions | id*, name, "idBoard", "idList", "desc", pos, "idShort", url, "dateLastActivity", badges_json; actions type, date, "idMemberCreator", data_json | 803 cards, 5,294 actions · 6851a7abf7876721472dba99 (BETA: Oct 10), 68d1eb90bef538c7c5c5599d | ids = 8 hex unix seconds + 16 hex; idShort next free on ZM ROADMAP = 80 (max 79) |
| confluence.confluence_pages / page_versions | id*, space_id*, parent_id, title*, body*, body_format*, status*, version*, author_id, created_at*, updated_at* | 31 pages, 78 versions · page_cicd_pipeline, page_ops_home | version 1 + one version row each |
| github.github_pull_requests | id*, repo_id*, number*, title, state, merged, author_login, merged_by_login, body, base_ref, head_ref, base_sha, head_sha, merge_commit_sha, created_at, updated_at, merged_at, closed_at, … | 2,629 · harmonygames-Games/match3d-backend#31, harmonygames-Games/match3d-backend#14 | match3d-backend base #1–#36; new #37–#54 |
| github.github_pr_comments / github_reviews / github_timeline_events | comments id*, pr_id*, author_login, body, created_at; reviews id*, pr_id*, state, body, submitted_at, commit_id, seq*; timeline id*, pr_id*, event*, actor_login, created_at, data_json | 884 / 2,421 / 12,435 · match3d-backend#31#c_1, #31#rev_1, #31#ev_4 | ids are the PR id plus #c_n / #rev_n / #ev_n; CodeRabbit comment actor SVC_0321 on the timeline (I07) |
| github.github_branches / github_commits / github_pull_request_commits | branch id*, repo_id*, name*; commit sha*, repo_id*, message, authored_date, author_*; prc id*, pr_id*, commit_sha*, position | 2,011 / 12,687 / 15,938 · harmonygames-Games/match3d-backend:bot-names | one branch, one commit, one PR-commit row per seeded PR |
| linear.linear_comments / linear_issues | id*, issue_id*, author_id*, parent_id, body*, is_edited*, created_at*, updated_at*, sequence; issues updated_at* | 0 comments / 3,852 issues · ZOM-503, ZOM-459 | cmt_ + 20 hex; varchar ISO-Z; comments before completed_at |

## 1.B Entity table

| Entity | Canonical / ids | Services (cited) | Verdict |
|---|---|---|---|
| Douglas (persona) | douglas@harmonygames.co; Slack EMPLOYEE_0031_SLACK_ID; Linear usr_cd7849ec043ab3da; GitHub PERSON_5760_GITHUB_USERNAME | D05QQF7V404/1757975508.211599; harmonygames-Games/match3d-backend#2 | AGREE |
| Arthur Blake | arthur.blake@harmonygames.co; EMPLOYEE_0025_SLACK_ID; usr_cc3e90160f490686; EMPLOYEE_0025_GITHUB_USERNAME; Trello 2162c1ba310341bf318f48b7; user_EMPLOYEE_0025 | D05QQF7V404/1757975508.211599; page_eng_home | AGREE ("Blake" in Slack, D079SNE2TL4/1759164463.327349) |
| Oliver Brooks | oliver.brooks@harmonygames.co; EMPLOYEE_0003_SLACK_ID; usr_bdf01b53c6a92c5e | C0880U9751A/1757618419.809199; ZOM-509 | AGREE (not Lauren Brooks) |
| Vincent Parker | vincent.parker@harmonygames.co; usr_65c76e0b87aa7e9b; EMPLOYEE_0012_GITHUB_USERNAME | D079SNE2TL4/1759269524.769369; ZOM-503 creator | AGREE |
| match3d-backend contractor | PERSON_2967_GITHUB_USERNAME / PERSON_2967_NAME / PERSON_2967_EMAIL | harmonygames-Games/match3d-backend#14, #31 | AGREE (token only, P04) |
| CodeRabbit | PERSON_6026_GITHUB_USERNAME (timeline actor SVC_0321_GITHUB_USERNAME) | harmonygames-Games/match3d-backend#31#c_1, #10#rev_1 | AGREE (I07 mirrored) |
| match3d-backend vs match3d | harmonygames-Games/match3d-backend (server) vs harmonygames-Games/match3d (client, mirrored to C093LEZGF6J) | harmonygames-Games/match3d#438 | DISAGREE (designed lookalike, N02); every seed says match3d-backend |
| ZOM-n vs ENG-n | ZOM-503, ZOM-557 vs ENG-503, ENG-557 | linear ZOM-503 | AGREE (N01 noted) |
| Beta | ZM ROADMAP list 'BETA: Oct 10' (6851a674975da1fe76e70d93); page_zm_beta_oct10 | trello:6851a7abf7876721472dba99 | AGREE |
| Prod deploys | base deploy messages D079SNE2TL4/1757351863.576949, /1757449699.464389, /1758040504.640159, /1759256193.859279 | seeded prod: notes on #42/#44, #46, #48, #52 | AGREE (timeline built on them) |

## 1.C Voice and realism (speakers, activity, conventions)

Lengths and hours from `references/universe_kb/conventions.json` (`slack.length_chars_by_channel_type`: DMs short, lowercase for Arthur; `slack.per_person_hours_and_style`: Douglas posts 15:00–03:59Z; `github.pr_title_patterns`: 'Area: change' as in match3d-backend#31 'Endless Monster Mode: Best score and fixes to weekly rankings'; `linear` comments one or two lines). Every seeded speaker with `status_at_clock` from `references/universe_kb/activity.json`:

| Speaker | Email / id | activity.json status_at_clock | Seeded where | Real sample |
|---|---|---|---|---|
| Arthur Blake | arthur.blake@harmonygames.co | activity: active_sep_2025 | DM ask, inline review comment on #46, freeze message, #50 thread reply, cards + comment, reply-all in Leonard's thread, gcal, Confluence page + comment reply, reviews | D05QQF7V404/1758146982.108989 'Can we update required versions for ZM' |
| Douglas | douglas@harmonygames.co | activity: active_sep_2025 | claim, #50 question, 'ok', doc, log, prod:/rollback: notes, reviews, inline review comment on #39, ZOM-537 comment | D079SNE2TL4/1759164463.327349 'Ok, the deployment is done' |
| Oliver Brooks | oliver.brooks@harmonygames.co | activity: active_sep_2025 | May claim, summary, post-here ask, Linear comments, client QA folder, ZM beta page QA comment | C0880U9751A/1757618419.809199 |
| Leonard Hayes | leonard.hayes@harmonygames.co | activity: active_sep_2025 | go/no-go email (A2), ZOM-256 comment | gmail:leonard@harmonygames.co_1842219327413774622.json |
| Vincent Parker | vincent.parker@harmonygames.co | activity: active_sep_2025 | Linear QA comments, 'works on dev' on #51 | D079SNE2TL4/1759269524.769369 'Yep it works as expected' |
| Owen Baker | owen.baker@harmonygames.co | activity: active_sep_2025 | ZOM-503 comment | D05SG9H1CFM/1758919727.787169 (thread partner) |
| Calvin Price | calvin.price@harmonygames.co | activity: active_sep_2025 | ZOM-499 and client comments | ZOM-499 assignee |
| Claire Morgan | claire.morgan@harmonygames.co | activity: active_sep_2025 | ZOM-336 and prop comments | ZOM-336 assignee |
| Samuel Turner | samuel.turner@harmonygames.co | activity: active_sep_2025 | client comments | ZOM-470 assignee |
| Marcus Bennett | marcus.bennett@harmonygames.co | activity: active_sep_2025 | VFX comments | ZOM-464 assignee |
| Brian Foster | brian.foster@harmonygames.co | activity: active_sep_2025 | ZOM-419 comment | ZOM-419 assignee |
| contractor / CodeRabbit | PERSON_2967_EMAIL / SVC_0271_EMAIL (PERSON_6026_GITHUB_USERNAME) | activity: not a person in activity.json (GitHub tokens) | PR comments/reviews only (contractor: inline review comment on #38) | harmonygames-Games/match3d-backend#31#c_1 |

Douglas's seeded times all fall in 15:00–03:59Z (his base posting window); the cut-day deploys (2025-08-25 11:52Z) and #43 (12:50Z) are the contractor's. Weekend items are the designed freeze weekend (Sep 27–28) and Sep 20 02:00Z (Friday evening in Douglas's time zone).

## 1.D Keyword / findability (base hit counts via `tools/hg.py search search <svc> <term>`)

| Term | Service | Base hits | Disposition |
|---|---|---|---|
| beta sign-off | trello | 0 (scan_complete true) | NEW TERM — introduced in 68dabfe9bc2e8b969782e22d, 68dac311754b38be05be7ea9, reached via anchor A1 D05QQF7V404/1759266764.508127 |
| sign-off | trello | 0 (scan_complete true) | NEW TERM — introduced in 68dabfe9bc2e8b969782e22d, 68dac311754b38be05be7ea9, reached via anchor A1 D05QQF7V404/1759266764.508127 |
| server freeze | slack | 0 (scan_complete true) | NEW TERM — introduced in C0880U9751A/1758295268.611352; gcal evt_0f489eb7fb46ada9660881, reached via anchor A1 D05QQF7V404/1759266764.508127 |
| go ahead on dev | slack | 0 (scan_complete true) | NEW TERM — introduced in C0880U9751A/1758938751.402267, reached via anchor A1 D05QQF7V404/1759266764.508127 |
| prod deploys | gdocs | 0 (scan_complete true) | NEW TERM — introduced in f_470ae81236d5bd39045dc1, reached via anchor A1 D05QQF7V404/1759266764.508127 |
| deploy log | gdrive | 0 (scan_complete true) | NEW TERM — introduced in f_78bedc46245090a160d2dd, reached via anchor A1 D05QQF7V404/1759266764.508127 |
| ZM Beta sign-off | gdrive | 0 (scan_complete true) | NEW TERM — introduced in d_69fcebc484d472907b0b5c, d_d71300168ca5dffa4db8b3, reached via anchor A1 D05QQF7V404/1759266764.508127 |
| server sign-off | confluence | 0 (scan_complete true) | NEW TERM — introduced in page_dd_launch_server_signoff, reached via anchor A1 D05QQF7V404/1759266764.508127 |
| ZM beta | confluence | 0 (scan_complete true) | NEW TERM — introduced in page_zm_beta_oct10, reached via anchor A1 D05QQF7V404/1759266764.508127 |
| boss arena HP table | confluence/gsheets | 0 (scan_complete true) | NEW TERM — introduced in comment_zm_beta_oct10_c2 and the deploy log f_78bedc46245090a160d2dd, reached via anchor A1 D05QQF7V404/1759266764.508127 |
| economy table | github/gsheets | 0 (scan_complete true) | NEW TERM — introduced in harmonygames-Games/match3d-backend#46#rc_1 (inline review comment) and the deploy log f_78bedc46245090a160d2dd, reached via anchor A1 D05QQF7V404/1759266764.508127 |
| plague race table | github/gsheets | 0 (scan_complete true) | NEW TERM — introduced in harmonygames-Games/match3d-backend#38#rc_1 (inline review comment) and the deploy log f_78bedc46245090a160d2dd, reached via anchor A1 D05QQF7V404/1759266764.508127 |
| trophy path copy table | github/gsheets | 0 (scan_complete true) | NEW TERM — introduced in harmonygames-Games/match3d-backend#39#rc_1 (inline review comment) and the deploy log f_78bedc46245090a160d2dd, reached via anchor A1 D05QQF7V404/1759266764.508127 |
| analytics events table | gmail/gsheets | 0 (scan_complete true) | NEW TERM — introduced in douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> (Arthur's reply-all) and the deploy log f_78bedc46245090a160d2dd, reached via anchor A1 D05QQF7V404/1759266764.508127 |
| loadout table | gmail/gsheets | 0 (scan_complete true) | NEW TERM — introduced in douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> (Arthur's reply-all) and the deploy log f_78bedc46245090a160d2dd, reached via anchor A1 D05QQF7V404/1759266764.508127 |
| match3d-backend | linear | 0 (scan_complete true) | NEW TERM — introduced in the 19 decisive + ~30 neutral Linear comments (e.g. cmt_c95585f37ce6708a9ec4), reached via anchor A1 D05QQF7V404/1759266764.508127 |
| prod: | github | 0 returned (scan_complete false: bounded) | NEW TERM — introduced in the seeded PR comments (e.g. harmonygames-Games/match3d-backend#44#c_2); a bounded miss proves nothing, but no base PR comment uses the keyword (base match3d-backend comments are CodeRabbit walkthroughs, match3d-backend#31#c_1) |

## 1.E Persona reach (scoped records)

| Record | Service | Visibility path | LB |
|---|---|---|---|
| D05QQF7V404/1759266764.508127 | slack | im D05QQF7V404 (Arthur, Douglas) | LB |
| D05QQF7V404/1758571837.284511 | slack | im D05QQF7V404 | LB |
| C0880U9751A/1758295268.611352 | slack | #zombie-match3d member | LB |
| C0880U9751A/1758937233.118904 | slack | #zombie-match3d member | LB |
| C0880U9751A/1758938751.402267 | slack | thread reply in #zombie-match3d | LB |
| C0880U9751A/1758938832.553908 | slack | thread reply | LB |
| C0880U9751A/1758991212.775031 | slack | #zombie-match3d member | LB |
| C0880U9751A/1759253506.093318 | slack | #zombie-match3d member | LB |
| C0880U9751A/1748450537.204611 | slack | #zombie-match3d member | LB |
| douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> | gmail | Douglas's own mailbox (INBOX), reply inside thread douglas@harmonygames.co/1844721277206562572 | LB |
| douglas@harmonygames.co/1844721277206562572 | gmail | Douglas's own mailbox (INBOX) | LB |
| evt_0f489eb7fb46ada9660881 | gcal | Douglas's own calendar copy | LB |
| f_470ae81236d5bd39045dc1 | gdocs | owner | LB |
| f_78bedc46245090a160d2dd | gsheets | owner | LB |
| d_69fcebc484d472907b0b5c | gdrive | shared writer | LB |
| d_d71300168ca5dffa4db8b3 | gdrive | shared reader | LB |
| D079SNE2TL4/1759256193.859279 | slack | im member (base) | LB |
| D079SNE2TL4/1759269524.769369 | slack | im member (base) | LB |
| D079SNE2TL4/1757351863.576949 | slack | im member (base) | LB |
| D079SNE2TL4/1757355159.852859 | slack | im member (base) | LB |
| D079SNE2TL4/1757449699.464389 | slack | im member (base) | LB |
| D079SNE2TL4/1758040504.640159 | slack | im member (base) | LB |

Trello, Confluence, Linear and GitHub are unscoped (`Evals/references/persona/acl.md`). `persona_view.py check-sql douglas task_inputs/01_Universe_Inject.sql --load-bearing <ids>` (verbatim):

```
CHECK-SQL as douglas <douglas@harmonygames.co>
[YES LB] L6 gdrive.drive_files insert d_69fcebc484d472907b0b5c - file is shared with the persona (shared_with_emails)
[YES LB] L9 gdrive.drive_files insert d_d71300168ca5dffa4db8b3 - file is shared with the persona (shared_with_emails)
[YES LB] L11 gdrive.drive_files insert f_470ae81236d5bd39045dc1 - persona owns the file
[YES LB] L13 gdrive.drive_files insert f_78bedc46245090a160d2dd - persona owns the file
[YES LB] L15 gdocs.docs_documents insert f_470ae81236d5bd39045dc1 - persona owns the file
[YES LB] L18 gsheets.sheets_spreadsheets insert f_78bedc46245090a160d2dd - persona owns the file
[YES LB] L21 gsheets.sheets_sheets insert f_78bedc46245090a160d2dd, f_78bedc46245090a160d2dd#0 - persona owns the file
[YES LB] L23 gsheets.sheets_sheets insert f_78bedc46245090a160d2dd, f_78bedc46245090a160d2dd#1 - persona owns the file
[YES LB] L38 slack.slack_messages insert 3a2e99ef807fc28ef39b8d6973a44427, C0880U9751A/1748450537.204611 - persona EMPLOYEE_0031_SLACK_ID is in members of private zombie-match3d
[YES LB] L41 slack.slack_messages insert 9ba4f3770f458826c7503e1aa0992acc, C0880U9751A/1758295268.611352 - persona EMPLOYEE_0031_SLACK_ID is in members of private zombie-match3d
[YES LB] L43 slack.slack_messages insert f5dde99eaea0ac1773ca37e48871cb60, D05QQF7V404/1758571837.284511 - persona EMPLOYEE_0031_SLACK_ID is in members of im D05QQF7V404
[YES LB] L45 slack.slack_messages insert 10613025eb309bac6e0fb32438625484, C0880U9751A/1758991212.775031 - persona EMPLOYEE_0031_SLACK_ID is in members of private zombie-match3d
[YES LB] L47 slack.slack_messages insert 42f263bfce69ae5a4ef068383ae66c4a, C0880U9751A/1759253506.093318 - persona EMPLOYEE_0031_SLACK_ID is in members of private zombie-match3d
[YES LB] L49 slack.slack_messages insert 1e5d5d2bf50901f0d7376627d6f539e8, D05QQF7V404/1759266764.508127 - persona EMPLOYEE_0031_SLACK_ID is in members of im D05QQF7V404
[YES LB] L51 slack.slack_messages insert 81531d5f36d48a5d2028a22405aed65e, C0880U9751A/1758937233.118904 - persona EMPLOYEE_0031_SLACK_ID is in members of private zombie-match3d
[YES LB] L53 slack.slack_messages insert 33339417b07ab83542fc971a41320a36, C0880U9751A/1758938751.402267 - persona EMPLOYEE_0031_SLACK_ID is in members of private zombie-match3d
[YES LB] L55 slack.slack_messages insert bde0c0ff791441e66d57cdb2de8f0f51, C0880U9751A/1758938832.553908 - persona EMPLOYEE_0031_SLACK_ID is in members of private zombie-match3d
[YES LB] L68 gmail.gmail_threads insert douglas@harmonygames.co/1844721277206562572 - row user_email is the persona (douglas@harmonygames.co)
[YES LB] L71 gmail.gmail_messages insert douglas@harmonygames.co/<CAreN_3nXHn9vq-8FWgVQEC3_2hxsSjSNZRkPtWB@mail.gmail.com>, douglas - row user_email is the persona (douglas@harmonygames.co)
[NO] L78 gmail.gmail_threads insert arthur.blake@harmonygames.co/1844721277207387678 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (douglas@harmonygames.co)
[NO] L80 gmail.gmail_messages insert arthur.blake@harmonygames.co/<CAreN_3nXHn9vq-8FWgVQEC3_2hxsSjSNZRkPtWB@mail.gmail.com>, ar - row is in mailbox arthur.blake@harmonygames.co, not the persona's (douglas@harmonygames.co)
[NO] L87 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1844721277206833296 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (douglas@harmonygames.co)
[NO] L89 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAreN_3nXHn9vq-8FWgVQEC3_2hxsSjSNZRkPtWB@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (douglas@harmonygames.co)
[YES LB] L96 gmail.gmail_messages insert douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com>, douglas - row user_email is the persona (douglas@harmonygames.co)
[NO] L115 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (douglas@harmonygames.co)
[NO] L134 gmail.gmail_messages insert arthur.blake@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com>, ar - row is in mailbox arthur.blake@harmonygames.co, not the persona's (douglas@harmonygames.co)
[YES] L153 gcal.gcal_events insert evt_b6eda0097a341f225ad5d2 - persona is an attendee and holds its own copy evt_0f489eb7fb46ada9660881 (same ical_uid and start) on douglas@harmonygames.co
[YES LB] L156 gcal.gcal_events insert evt_0f489eb7fb46ada9660881 - event is on the persona's own calendar douglas@harmonygames.co
[YES] L158 gcal.gcal_events insert evt_e3c3cd6a8dec19d0e7b123 - persona is an attendee and holds its own copy evt_0f489eb7fb46ada9660881 (same ical_uid and start) on douglas@harmonygames.co
[YES] L160 gcal.gcal_events insert evt_5e9adacd9af476a6402dfa - persona is an attendee and holds its own copy evt_0f489eb7fb46ada9660881 (same ical_uid and start) on douglas@harmonygames.co
[YES] L162 gcal.gcal_events insert evt_bbe10af026c7f633387e2d - persona is an attendee and holds its own copy evt_0f489eb7fb46ada9660881 (same ical_uid and start) on douglas@harmonygames.co
[YES LB] base slack D079SNE2TL4/1757351863.576949 - base record: message inherits channel: persona EMPLOYEE_0031_SLACK_ID is in members of im D079SNE2TL4
[YES LB] base slack D079SNE2TL4/1757355159.852859 - base record: message inherits channel: persona EMPLOYEE_0031_SLACK_ID is in members of im D079SNE2TL4
[YES LB] base slack D079SNE2TL4/1757449699.464389 - base record: message inherits channel: persona EMPLOYEE_0031_SLACK_ID is in members of im D079SNE2TL4
[YES LB] base slack D079SNE2TL4/1758040504.640159 - base record: message inherits channel: persona EMPLOYEE_0031_SLACK_ID is in members of im D079SNE2TL4
[YES LB] base slack D079SNE2TL4/1759256193.859279 - base record: message inherits channel: persona EMPLOYEE_0031_SLACK_ID is in members of im D079SNE2TL4
[YES LB] base slack D079SNE2TL4/1759269524.769369 - base record: message inherits channel: persona EMPLOYEE_0031_SLACK_ID is in members of im D079SNE2TL4

summary: {'YES': 25, 'NO': 6}  unscoped rows (always visible): 373
  gcal.gcal_events: {'YES': 5}
  gdocs.docs_documents: {'YES': 1}
  gdrive.drive_files: {'YES': 4}
  gmail.gmail_messages: {'YES': 2, 'NO': 4}
  gmail.gmail_threads: {'YES': 1, 'NO': 2}
  gsheets.sheets_sheets: {'YES': 2}
  gsheets.sheets_spreadsheets: {'YES': 1}
  slack.slack_messages: {'YES': 9}
verdict: PASS (0 load-bearing rows not visible)
```

The NO rows are the sender's and cc's own mailbox copies (Arthur, Leonard); none is load-bearing. The two page comments (comment_zm_beta_oct10_c1, comment_zm_beta_oct10_c2) are Confluence rows, unscoped.

## 1.F Collision checks

Identity tokens: no new person or token is introduced; PR authors use the base logins (PERSON_5760, PERSON_2967, EMPLOYEE_0025, EMPLOYEE_0012, PERSON_6026). Every minted id (172: Slack ids and ts, Trello, Drive, GCal, Linear comment, Gmail thread/Message-ID, Confluence page, 40-hex sha) was scanned as a fixed string over the full collections (`grep -rFl -f minted.txt HarmonyGames_Other_Services/Services_Data HarmonyGames_GitHub/Services_Data HarmonyGames_Gmail`): 0 files hit. PR numbers harmonygames-Games/match3d-backend#37–#54 do not exist in the base (highest #36, post-clock). ZOM-n keys are base ids reused as references only.

| Id class | Count | Sample | Base hits |
|---|---|---|---|
| Slack id / ts | 10 | 1e5d5d2bf50901f0d7376627d6f539e8 / 1759266764.508127 | 0 |
| Trello | 5 | 68dabfe9bc2e8b969782e22d | 0 |
| Drive family | 4 | d_69fcebc484d472907b0b5c, f_470ae81236d5bd39045dc1 | 0 |
| GCal | 5 | evt_0f489eb7fb46ada9660881 | 0 |
| Linear comment | 79 | cmt_c95585f37ce6708a9ec4 | 0 |
| Gmail | 9 (3 threads, 6 Message-ID rows) | douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> | 0 |
| Confluence | 4 (2 pages, 2 comments) | page_zm_beta_oct10, comment_zm_beta_oct10_c2 | 0 |
| GitHub PR | 18 | harmonygames-Games/match3d-backend#37 | 0 |

## 2 Record ledger

| # | Service · table | Id(s) | Container | Manifest element | Carrier | Reach | Discovery role |
|---|---|---|---|---|---|---|---|
| 1 | gdrive · drive_files | d_69fcebc484d472907b0b5c | Arthur's root d_cc3e90160f490686039986 | K13 destination | ● | writer | write target |
| 2 | gdrive · drive_files | d_d71300168ca5dffa4db8b3 | Oliver's root d_bdf01b53c6a92c5e167c65 | T19 decoy | ● | reader | decoy |
| 3 | gdrive+gdocs | f_470ae81236d5bd39045dc1 | Douglas's root | H2 / K5, K6, K8, K11 | ● | owner | authority |
| 4 | gdrive+gsheets (2 tabs) | f_78bedc46245090a160d2dd | Douglas's root | K7, K8; T6, T11; C9-C13 (plague race, trophy path copy, loadout, analytics events, economy and boss arena HP table imports, dev) | ● | owner | connecting |
| 5 | confluence · pages+versions | page_zm_beta_oct10 | space_OPS / page_ops_home | K9 | ● | unscoped | connecting |
| 6 | confluence · pages+versions | page_dd_launch_server_signoff | space_OPS / page_ops_home | T1 decoy (H1) | ● | unscoped | decoy |
| 7 | confluence · comments ×2 | comment_zm_beta_oct10_c1 (Oliver, QA question), comment_zm_beta_oct10_c2 (Arthur's reply) | page_zm_beta_oct10 | K14; C9; T23 | ● | unscoped | overturning reply |
| 8 | slack · messages | D05QQF7V404/1759266764.508127 | D05QQF7V404 | A1 / K1 (plain message, reply_count 0) | ● | im | first link |
| 9 | github · review_comments | harmonygames-Games/match3d-backend#46#rc_1 | match3d-backend#46, on Arthur's Approve | K15; C10; T24 | ● | unscoped | amendment (inline review comment) |
| 10 | github · review_comments | harmonygames-Games/match3d-backend#38#rc_1 | match3d-backend#38, on the contractor's Approve | K17; C12; T27 | ● | unscoped | amendment (inline review comment) |
| 11 | github · review_comments | harmonygames-Games/match3d-backend#39#rc_1 | match3d-backend#39, on Douglas's Approve | K18; C13; T28 | ● | unscoped | amendment (inline review comment) |
| 12 | slack · messages | D05QQF7V404/1758571837.284511 | D05QQF7V404 | T22 | ● | im | claim met first |
| 13 | slack · messages | C0880U9751A/1758295268.611352 | C0880U9751A | T2 (oldest) | ● | member | claim met first |
| 14 | slack · messages | C0880U9751A/1758937233.118904, C0880U9751A/1758938751.402267, C0880U9751A/1758938832.553908 | C0880U9751A thread | T8, C2 | ● | member | claim + overturning reply |
| 15 | slack · messages | C0880U9751A/1758991212.775031 | C0880U9751A | T4, T20, C1 | ● | member | claim met first |
| 16 | slack · messages | C0880U9751A/1759253506.093318 | C0880U9751A | T16 | ● | member | decoy |
| 17 | slack · messages | C0880U9751A/1748450537.204611 | C0880U9751A | T3 (oldest), H2 decoy | ● | member | decoy |
| 18 | trello · cards+actions | 68dabfe9bc2e8b969782e22d (+ createCard 68dabfe93a26ef2186dcec1c) | 6851a6569f3bf818760632ab / BETA: Oct 10 | H1 / K2 | ● | unscoped | authority |
| 19 | trello · actions | 68dbf1b73eba0ba580f67a6e | card 68dabfe9bc2e8b969782e22d | K3 amendment | ● | unscoped | amendment |
| 20 | trello · cards+actions | 68dac311754b38be05be7ea9 (+ 68dac311a286768d02a6385d) | same list | T7 decoy | ● | unscoped | decoy |
| 21 | gmail · threads ×3 + messages ×3 | douglas@harmonygames.co/1844721277206562572 | Douglas INBOX (+ Arthur INBOX, Leonard SENT) | A2 / K12 | ● | own mailbox | first link |
| 22 | gmail · messages ×3 (reply in the same threads) | douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> | Douglas INBOX (+ Leonard INBOX, Arthur SENT); In-Reply-To Leonard's message | K4, K16 amendments; C6, C11; T25, T26 | ● | own mailbox | amendment (thread reply) |
| 23 | gcal · events ×5 | evt_b6eda0097a341f225ad5d2, evt_0f489eb7fb46ada9660881, evt_e3c3cd6a8dec19d0e7b123, evt_5e9adacd9af476a6402dfa, evt_bbe10af026c7f633387e2d | 5 attendee calendars | K6; T2 (newest) | ● (start) | own copy | overturning |
| 24 | github · pull_requests/branches/commits/prc ×18 | harmonygames-Games/match3d-backend#37 … #54 | match3d-backend | K11; cohort surface 2/3 | ● | unscoped | per-record |
| 25 | github · pr_comments ×40 | harmonygames-Games/match3d-backend#37#c_1 … #54#c_3 | PRs | prod:/rollback:/dev notes; CodeRabbit walkthroughs | ● | unscoped | per-record |
| 26 | github · reviews ×37 | harmonygames-Games/match3d-backend#37#rev_1 … #54#rev_2 | PRs | approval rule rows (C3, C8, T9, T21) | ● | unscoped | per-record |
| 27 | github · timeline_events ×131 | harmonygames-Games/match3d-backend#37#ev_1 … | PRs | companions (commented/reviewed/merged/closed) | — | unscoped | companion |
| 28 | linear · comments ×79 | cmt_c95585f37ce6708a9ec4 … (sql_ids.json linear_comments) | 73 cohort tickets + ZOM-461, ZOM-480, ZOM-479, ZOM-489 | cohort surface 1; K10 | ● (§6b) | unscoped | per-record |

## 3 Findability and discovery-order proofs

```
Record:              trello.trello_cards · 68dabfe9bc2e8b969782e22d
Agent's likely query: "beta sign-off" via trello_search
Term present:        NEW TERM (0 base hits); card title 'Beta sign-off - server side'
Competing base hits: 1 competing seed (68dac311754b38be05be7ea9, same list)
Chain position:      first link from A1
```
```
Record:              gdocs.docs_documents · f_470ae81236d5bd39045dc1
Agent's likely query: "prod deploys" / "match3d-backend" via gdocs_search_documents
Term present:        NEW TERM (0 base hits)
Competing base hits: 0
Chain position:      connecting (card rule 3)
```
```
Record:              gsheets · f_78bedc46245090a160d2dd
Agent's likely query: "deploy log" via gdrive_search
Term present:        NEW TERM (0 base hits)
Competing base hits: 0
Chain position:      connecting (card rule 1, doc)
```
```
Record:              gcal · evt_0f489eb7fb46ada9660881
Agent's likely query: gcal_list_events Sep 22–30 on Douglas's calendar
Term present:        summary 'ZM beta - server freeze'
Competing base hits: Douglas has 12 events in Sep 2025 (reach census)
Chain position:      terminal (freeze instant)
```
```
Record:              confluence · page_zm_beta_oct10
Agent's likely query: "ZM beta" via confluence_search
Term present:        NEW TERM (0 base hits)
Competing base hits: page_dd_launch_server_signoff on 'sign-off'
Chain position:      connecting (card rule 6)
```
```
Record:              gmail · douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com>
Agent's likely query: gmail_get_thread on Leonard's thread douglas@harmonygames.co/1844721277206562572 (or a 'go/no-go' search, which returns both messages)
Term present:        subject 'Re: beta go/no-go thursday'; both points (547/553 off; the analytics events and loadout table imports)
Competing base hits: 0 base mails on 'beta go/no-go'
Chain position:      amendment (reply under the A2 message)
```
```
Record:              confluence.confluence_comments · comment_zm_beta_oct10_c2
Agent's likely query: confluence_list_comments(page_zm_beta_oct10)
Term present:        reply to QA naming ZOM-487 and the boss arena HP table
Competing base hits: 0 other comments on the page
Chain position:      overturning reply (C9)
```
```
Record:              github.github_review_comments · harmonygames-Games/match3d-backend#46#rc_1
Agent's likely query: inline review comments of #46 (github_get_pull_request_comments)
Term present:        '537 also needs the economy table import'
Competing base hits: inline comments also on #38 and #39 (other tickets)
Chain position:      amendment (C10)
```
```
Record:              github.github_review_comments · harmonygames-Games/match3d-backend#38#rc_1
Agent's likely query: inline review comments of #38 (github_get_pull_request_comments)
Term present:        '459 also needs the plague race table import'
Competing base hits: inline comments also on #39 and #46 (other tickets)
Chain position:      amendment (C12)
```
```
Record:              github.github_review_comments · harmonygames-Games/match3d-backend#39#rc_1
Agent's likely query: inline review comments of #39 (github_get_pull_request_comments)
Term present:        '509 needs that table imported on the backend too'
Competing base hits: inline comments also on #38 and #46 (other tickets)
Chain position:      amendment (C13)
```
```
Record:              gmail · douglas@harmonygames.co/1844721277206562572
Agent's likely query: "go/no-go" via gmail_search_messages
Term present:        subject 'beta go/no-go thursday'
Competing base hits: 0 base mails on 'beta go/no-go'
Chain position:      first link (A2)
```
```
Record:              linear.linear_comments · cmt_877095d931428f1536df
Agent's likely query: linear_list_comments(ZOM-336)
Term present:        per-record; no list/search returns comments (Ask_Carriers §6b)
Competing base hits: —
Chain position:      per-record
```

**Discovery-order proofs (dynamic-change seeds).**

| Claim met first | Overturned by | Why met first | Why decisive |
|---|---|---|---|
| C0880U9751A/1758295268.611352 (Mon 29th) | evt_0f489eb7fb46ada9660881 (Fri 22:00Z, updated 2025-09-23T16:05Z) | a Slack search 'freeze' returns it; Calendar is rarely opened (A13) | decides whether #50's Sep 27 deploy needed Arthur's approval |
| C0880U9751A/1758991212.775031 | harmonygames-Games/match3d-backend#54#c_3 (rollback Sep 28) and the PR records | newest server-status message before the ask | flips ZOM-557 and five more rows |
| D05QQF7V404/1758571837.284511 | harmonygames-Games/match3d-backend#41#rev_2 (approval after the deploy); #51 dev note | same DM as the ask | flips ZOM-392, ZOM-435 |
| C0880U9751A/1758937233.118904 (parent) | C0880U9751A/1758938751.402267 (reply) | the parent names #50 and prod; the limit is in the reply (A14) | ZOM-550 |
| C0880U9751A/1748450537.204611 | f_470ae81236d5bd39045dc1 | Slack search 'merged' | merged is not on prod |
| page_dd_launch_server_signoff | 68dabfe9bc2e8b969782e22d → 68dbf1b73eba0ba580f67a6e → douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> | Confluence search 'server sign-off' returns it first | imports in, ZOM-547/553 out |
| douglas@harmonygames.co/1844721277206562572 (Leonard's message, what a 'from:leonard' search returns) | douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> (Arthur's reply-all under it) | a sender search returns Leonard's message only; the reply needs the thread (A14) | ZOM-547/553 out |
| cmt_41e71e303718899c0d3c (ZOM-487: #48 only) | comment_zm_beta_oct10_c2 (Arthur: the boss arena HP table import is part of it) + f_78bedc46245090a160d2dd (dev) | the ticket comment is read per ticket; the page reply needs a comment read (A9) | ZOM-487 N |
| cmt_92b95a95aa3414a22c89 (ZOM-537: #46 only) | harmonygames-Games/match3d-backend#46#rc_1 (Arthur: also the economy table import) + f_78bedc46245090a160d2dd (dev) | the PR's conversation comments and review list don't carry it; inline review comments are a separate call (A14) | ZOM-537 N |
| cmt_32c3a18150bf06ad3a12 (ZOM-444: #47 only), cmt_81278f65a6828964fd37 (ZOM-531: #45 only), cmt_7c7780e6f01e8b2c5103 (ZOM-436: QA device note) | douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> second point (analytics events table import for ZOM-444 and ZOM-436, loadout table import for ZOM-531) + f_78bedc46245090a160d2dd (dev) | a sender search returns Leonard's message only; the reply needs the thread (A14) | ZOM-444, ZOM-531 N; ZOM-436 in, N |
| cmt_0b9e52e7a05129c16301 (ZOM-459: #38 only) | harmonygames-Games/match3d-backend#38#rc_1 (reviewer: also the plague race table import) + f_78bedc46245090a160d2dd (dev) | inline review comments are a separate call (A14) | ZOM-459 N |
| cmt_112afca3ef67b713a9e7 (ZOM-509: #39 only) | harmonygames-Games/match3d-backend#39#rc_1 (Douglas: also the trophy path copy table import) + f_78bedc46245090a160d2dd (dev) | inline review comments are a separate call (A14) | ZOM-509 N |
| D079SNE2TL4/1759269524.769369 (Vincent: works as expected) | harmonygames-Games/match3d-backend#52#rev_2 (contractor approval only) + the freeze | Douglas's own DM, newest | ZOM-503 |

**Hidden authorities.** H1 → `trello_search "beta sign-off"` returns 68dabfe9bc2e8b969782e22d (and the client card 68dac311754b38be05be7ea9); decoy page_dd_launch_server_signoff is reached by `confluence_search "server sign-off"` and differs on scope (Domino Delights) and on approval (Slack thumbs-up). H2 → `gdocs_search_documents "prod deploys"` returns f_470ae81236d5bd39045dc1; decoy C0880U9751A/1748450537.204611 is reached by a Slack search on 'merged' and differs on the decisive clause (merged = live).

## 4 Self-validation

| QC category | Tool-enforced (sql_lint / base_check) | Manual evidence |
|---|---|---|
| Missing Universe Data | — | every needed fact seeded or base and persona-readable (1.E); reads via cataloged tools (`linear_list_comments`, `github_get_issue_comments`, `github_get_pull_request_reviews`, `gcal_list_events`) |
| Temporal Field | PASS (base_check Check C) | text dates agree with fields: log rows = prod: comment times (harmonygames-Games/match3d-backend#46#c_2 20:29Z = log row '2025-09-09 20:29'); every Linear comment before its ticket's completed_at |
| Cross-service Referential | PASS (Check A) | PR numbers in Linear comments and the email exist (#37–#54); Douglas's calendar copy carries the same ical_uid |
| Quantitative / Reconciliation | PASS | deploy log rows agree with PR comments for every row the tab has (through Sep 10) |
| State / Lifecycle | PASS | no ticket state changed; tickets closed before prod deploys by design (Done = verified on dev) |
| Identifier / Format | PASS | ids follow base schemes (1.F); Gmail Message-ID form; GitHub #c_/#rev_/#ev_ |
| Semantic / Category | — | titles match content; 'match3d-backend' vs 'match3d' kept distinct (1.B) |
| Other | — | no record states a conclusion; claims are dated human messages |

## 5 Lazy-solver pass on the implemented records

- One Slack search ('server', 'prod') returns C0880U9751A/1758991212.775031 → everything on prod: 8 rows wrong (ZOM-557, ZOM-336, ZOM-435, ZOM-392, ZOM-518, ZOM-550, ZOM-503, ZOM-256).
- Card description only (68dabfe9bc2e8b969782e22d) → no imports (ZOM-510, ZOM-256 missing) and ZOM-547/553 kept.
- Deploy log Prod deploys tab (f_78bedc46245090a160d2dd) as the record → ZOM-444, ZOM-499 read as not on prod; ZOM-392, ZOM-518 as on prod.
- Leonard's message only (get_message on douglas@harmonygames.co/1844721277206562572) → ZOM-547/553 kept, ZOM-436 missing, ZOM-444 and ZOM-531 Y (18 rows, wrong counts); Arthur's reply douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> is under it.
- #38 and #39 without their inline review comments → ZOM-459 and ZOM-509 Y; harmonygames-Games/match3d-backend#38#rc_1 and harmonygames-Games/match3d-backend#39#rc_1 add the plague race and trophy path copy table imports (dev).
- ZM beta page body only (no comment read) → ZOM-487 Y; comment_zm_beta_oct10_c2 adds the boss arena HP table import (dev).
- #46 without its inline review comments → ZOM-537 Y; harmonygames-Games/match3d-backend#46#rc_1 adds the economy table import (dev).
- Unlinked Console & imports rows (plague race, trophy path copy, loadout, analytics events, economy and boss arena HP tables) name no ticket; a Linear search on 'boss arena' returns five Done tickets in the window (ZOM-487, ZOM-540, ZOM-547, ZOM-550, ZOM-553), and the two analytics tickets (ZOM-444, ZOM-436) say nothing about a table, so each link comes from the note that names it.
- Comments without reviews → ZOM-392, ZOM-518, ZOM-550, ZOM-503 wrong (harmonygames-Games/match3d-backend#41#rev_2, #43, #50#rev_3, #52#rev_2).
- Parent of the #50 thread only (C0880U9751A/1758937233.118904) → reads approval; the reply (C0880U9751A/1758938751.402267) limits it to dev.
- Bulk shortcuts: `linear_list_issues` returns no comments; no Slack mirror for match3d-backend; the Console & imports tab names no tickets; nothing lists the 17 tickets.

## 6 Intended disagreements

| # | Disagreement | Why realistic | Resolved by |
|---|---|---|---|
| 1 | C0880U9751A/1758295268.611352 says Monday 29th; evt_0f489eb7fb46ada9660881 says Fri 26 22:00Z | freeze pulled in after QA asked for a frozen weekend (event description) | the calendar event, updated Sep 23, newer and named in the doc |
| 2 | C0880U9751A/1758991212.775031 says all server fixes are on prod | QA tested on prod Saturday morning, before #54's rollback, and did not check approvals | PR comments/reviews (harmonygames-Games/match3d-backend#54#c_3 etc.) |
| 3 | D05QQF7V404/1758571837.284511 (Douglas: fix is out; seeds on prod since the 3rd) | a developer's shorthand; #51 was on dev, #41's approval came later | harmonygames-Games/match3d-backend#51#c_2 (dev), #41#rev_2 after #41#c_2 |
| 4 | C0880U9751A/1748450537.204611 (May: merged = live) | true before match3d-backend#2 created prod | doc f_470ae81236d5bd39045dc1 |
| 5 | page_dd_launch_server_signoff (DD launch rules) | older rules for another game | card 68dabfe9bc2e8b969782e22d (ZM beta) |
| 6 | f_78bedc46245090a160d2dd Prod deploys tab stops on Sep 10 | a quick list Douglas stopped filling | doc: the PR's prod: comment is the record |
| 7 | D079SNE2TL4/1759256193.859279 + /1759269524.769369 (teams changes on prod, works) | deployed during the freeze on the contractor's approval | doc freeze clause; harmonygames-Games/match3d-backend#52#rev_2 |
| 8 | cmt_41e71e303718899c0d3c names #48 only; comment_zm_beta_oct10_c2 adds the boss arena HP table import | Vincent noted the PR when he closed the ticket; QA found the old HP values on prod on Sep 30 | Arthur's inline review comment (the rules' author, on his own Approve) + the deploy log (dev) |
| 9 | cmt_92b95a95aa3414a22c89 names #46 only; harmonygames-Games/match3d-backend#46#rc_1 adds the economy table import | Douglas's own one-line note; the values also live in an imported table | Arthur's inline review comment (the rules' author, on his own Approve) + the deploy log (dev) |
| 10 | cmt_32c3a18150bf06ad3a12 and cmt_81278f65a6828964fd37 name one PR each; cmt_7c7780e6f01e8b2c5103 is a QA device note; douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> adds the analytics events and loadout table imports | the closers noted the code change; the table imports were Douglas's later dev steps, which Arthur ties to the tickets before go/no-go | Arthur's reply-all (the rules' author, Sep 30, newest) + the deploy log (dev) |
| 11 | cmt_0b9e52e7a05129c16301 names #38 only; harmonygames-Games/match3d-backend#38#rc_1 adds the plague race table import | Arthur's one-line closing note; the reviewer flagged the table on the PR | the reviewer's inline comment on #38 (on the Approve) + the deploy log (dev) |
| 12 | cmt_112afca3ef67b713a9e7 names #39 only; harmonygames-Games/match3d-backend#39#rc_1 adds the trophy path copy table import | Oliver's closing note names the PR; Douglas left the import note on his own review | Douglas's inline comment on #39 (on his Approve) + the deploy log (dev) |

## 7 Constraints for the prompt brief

| Anchor | May be named (noun phrases only) | Record |
|---|---|---|
| A1 | Arthur's beta sign-off ask; Arthur's DM | slack D05QQF7V404/1759266764.508127 |
| A2 | Leonard's go/no-go email | gmail douglas@harmonygames.co/1844721277206562572 |

Never name: the Trello card or board, the deploy doc, the deploy log, the calendar freeze, the Confluence pages, the folder, the cut time, the PR numbers, the ticket keys, the approval/rollback rules, the counts. Deadline: Thursday's go/no-go (Oct 2). Deliverable kinds: a register (sheet), a reply in the DM, ticket updates, the share for Leonard.

## 8 Fact sheet

| Key | Value | Kind | Home / must appear in |
|---|---|---|---|
| ZOM-336 | match3d-backend#40 | id | cmt_877095d931428f1536df |
| ZOM-392 | match3d-backend#41 | id | cmt_d02aec11deff05b555cc |
| ZOM-518 | match3d-backend#43 | id | cmt_99069485a5f5d5eb9ce3 |
| ZOM-435 | match3d-backend#51 | id | cmt_8dbc7c9e3101efc08508 |
| ZOM-557 | match3d-backend#54 | id | cmt_e850768746208eefe527 |
| ZOM-499 | match3d-backend#44 | id | cmt_b197d27aaaba58c9b89f |
| ZOM-444 | match3d-backend#47 | id | cmt_32c3a18150bf06ad3a12 |
| ZOM-487 | match3d-backend#48 | id | cmt_41e71e303718899c0d3c |

`python3 Task_Authoring/tools/fact_check.py task_inputs/01_Universe_Inject.sql --manifest Working_Files/01_Hardness_Manifest.json --no-leak` (verbatim):

```
FACT CHECK: PASS — 215 text-bearing rows, 8 declared facts, 9 declared superseded records
Errors: none
```

## 9 Facts for the human

### 9.1 Records

| Locator | Base/seeded | Fact | Reach | Role | Re-verify? |
|---|---|---|---|---|---|
| D05QQF7V404/1759266764.508127 | seeded | Arthur 2025-09-30T21:12:44Z: for thursday's go/no-go i need the server side of the beta sign-off from you. the rules are on the beta card on the roadmap board. reply here when it's done with how many tickets are on prod and which ones aren't (plain message, no replies) | im | anchor A1 | no |
| harmonygames-Games/match3d-backend#46#rc_1 | seeded | Arthur 2025-09-09T19:40:00Z, inline review comment on #46 (lib/zombies_game/economy.ex, with his Approve): code's fine. heads up though, these now read from the economy table, so 537 also needs the economy table import on the backend. that import is part of 537's server change, the values aren't live without it | unscoped | amendment (ZOM-537) | no |
| harmonygames-Games/match3d-backend#38#rc_1 | seeded | contractor 2025-08-25T09:20:00Z, inline review comment on #38 (lib/zombies_game/plague_race.ex, with the Approve): looks right. one thing: standings come from the plague race table now, so 459 also needs the plague race table import on the backend. that import is part of 459's server change, the count won't change on prod without it | unscoped | amendment (ZOM-459) | no |
| harmonygames-Games/match3d-backend#39#rc_1 | seeded | Douglas 2025-09-02T15:20:00Z, inline review comment on #39 (lib/zombies_game/trophy_path.ex, with his Approve): approving. note for whoever ships it: the headlines and subtext come from the trophy path copy table now, so 509 needs that table imported on the backend too. the import is part of 509's server change | unscoped | amendment (ZOM-509) | no |
| comment_zm_beta_oct10_c1 | seeded | Oliver 2025-09-30T10:12Z on page_zm_beta_oct10: QA on prod this morning: the infinite HP boss still runs on the old HP values. Is the server side of ZOM-487 out? | unscoped | QA question | no |
| comment_zm_beta_oct10_c2 | seeded | Arthur 2025-09-30T11:03Z, reply to comment_zm_beta_oct10_c1: #48 is on prod, but the boss HP values come from the boss arena HP table, and that import is part of ZOM-487's server change too. Douglas has it in the deploy log. | unscoped | amendment (ZOM-487) | no |
| douglas@harmonygames.co/1844721277206562572 | seeded | Leonard 2025-09-30T20:15:03Z, cc Arthur, 'beta go/no-go thursday': share the register with him, comment access | own mailbox | anchor A2 | no |
| 68dabfe9bc2e8b969782e22d | seeded | Arthur 2025-09-29T17:20:41Z 'Beta sign-off - server side', rules 1–6 | unscoped | authority H1 | no |
| 68dbf1b73eba0ba580f67a6e | seeded | Arthur 2025-09-30T15:05:27Z: adding to rule 1: spreadsheet imports on the backend count as server changes too, same as console changes. they're in the deploy log. rest of the card stands. | unscoped | amendment | no |
| douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> | seeded | Arthur 2025-09-30T20:41:27Z, reply-all in Leonard's thread douglas@harmonygames.co/1844721277206562572 ('Re: beta go/no-go thursday'): ZOM-547 and ZOM-553 off the register, not counted; the analytics events table import is part of ZOM-444's and ZOM-436's server change, the loadout table import of ZOM-531's; both only on dev | own mailbox | amendment | no |
| f_470ae81236d5bd39045dc1 | seeded | Douglas, created 2025-06-01T18:30Z, edited 2025-09-25T16:40Z: prod branch, prod:/rollback: comments, Approve by someone else before the deploy, Arthur's Approve inside the freeze | owner | authority H2 | no |
| evt_0f489eb7fb46ada9660881 | seeded | 'ZM beta - server freeze' 2025-09-26T22:00Z–22:30Z, created 2025-09-22T14:02Z, updated 2025-09-23T16:05Z | own copy | freeze instant | no |
| f_78bedc46245090a160d2dd | seeded | Prod deploys row 1 '2025-08-25 11:52 · beta prod cut'; tab stops 2025-09-10; Console & imports: plague race table dev 2025-08-26 10:30, plague race bot names console prod 2025-08-28 17:05, trophy path copy table dev 2025-09-02 18:05, Zombie Lane rewards import prod 2025-09-08 16:45, loadout table dev 2025-09-10 17:40, algo level pack dev 2025-09-11 16:30, analytics events table dev 2025-09-12 19:20, economy table dev 2025-09-16 14:20, boss arena HP table dev 2025-09-17 15:50 | owner | cut + imports | no |
| page_zm_beta_oct10 | seeded | Arthur 2025-09-29T17:15Z: sign-off folder 'ZM Beta sign-off' | unscoped | destination pointer | no |
| d_69fcebc484d472907b0b5c | seeded | 'ZM Beta sign-off' (Arthur; Douglas, Oliver, Vincent writers) | writer | write target | no |
| d_d71300168ca5dffa4db8b3 | seeded | 'ZM Beta sign-off - client QA' (Oliver) | reader | decoy | no |
| 68dac311754b38be05be7ea9 | seeded | client sign-off card (In Validation, Aug 15) | unscoped | decoy | no |
| page_dd_launch_server_signoff | seeded | DD launch sign-off (May 2025) | unscoped | decoy | no |
| C0880U9751A/1758295268.611352 | seeded | Arthur 2025-09-19: freeze Monday the 29th | member | claim met first | no |
| C0880U9751A/1758937233.118904 / C0880U9751A/1758938751.402267 / C0880U9751A/1758938832.553908 | seeded | Douglas asks to push #50 to prod; Arthur: go ahead on dev, PR review before prod; Douglas: ok | member | claim + reply | no |
| C0880U9751A/1758991212.775031 | seeded | Oliver 2025-09-27T16:40Z: all server fixes since the cut on prod | member | claim met first | no |
| D05QQF7V404/1758571837.284511 | seeded | Douglas 2025-09-22T20:10Z: trophy path fix out; algo seeds on prod since the 3rd | im | claim met first | no |
| C0880U9751A/1759253506.093318 | seeded | Oliver: post the list here too | member | decoy | no |
| C0880U9751A/1748450537.204611 | seeded | Oliver 2025-05-28: merged into main = live | member | decoy | no |
| D079SNE2TL4/1759256193.859279 | base | Douglas 2025-09-30T18:16Z: updated prod with the latest teams/social changes | im | claim (= #52 prod:) | no |
| D079SNE2TL4/1759269524.769369 | base | Vincent 2025-09-30T21:58Z: works as expected | im | claim | no |
| harmonygames-Games/match3d-backend#37 | seeded | Algo levels: spawn points from the server seed · author douglas · created 2025-08-21T15:20:00Z · merged 2025-08-25T09:10:00Z · prod 2025-08-25T11:52:00Z (harmonygames-Games/match3d-backend#37#c_2) · reviews: APPROVED contractor 2025-08-25T09:00:00Z (harmonygames-Games/match3d-backend#37#rev_2) | unscoped | per-record evidence (ZOM-461) | no |
| harmonygames-Games/match3d-backend#38 | seeded | Plague race: count algo levels · author douglas · created 2025-08-22T15:10:00Z · merged 2025-08-25T09:30:00Z · prod 2025-08-25T11:52:00Z (harmonygames-Games/match3d-backend#38#c_2) · reviews: APPROVED contractor 2025-08-25T09:20:00Z (harmonygames-Games/match3d-backend#38#rev_2) | unscoped | per-record evidence (ZOM-459) | no |
| harmonygames-Games/match3d-backend#39 | seeded | Trophy path: container headlines config · author contractor · created 2025-08-29T13:00:00Z · merged 2025-09-02T15:40:00Z · prod 2025-09-02T17:30:00Z (harmonygames-Games/match3d-backend#39#c_2) · reviews: APPROVED douglas 2025-09-02T15:20:00Z (harmonygames-Games/match3d-backend#39#rev_2) | unscoped | per-record evidence (ZOM-509) | no |
| harmonygames-Games/match3d-backend#40 | seeded | Catalog: add usable item entries · author contractor · created 2025-09-01T10:15:00Z · merged 2025-09-02T18:20:00Z · dev 2025-09-02T18:40:00Z (harmonygames-Games/match3d-backend#40#c_2) · reviews: no human review | unscoped | per-record evidence (ZOM-336) | no |
| harmonygames-Games/match3d-backend#41 | seeded | Algo levels 100+: seed endpoint · author douglas · created 2025-09-01T19:40:00Z · merged 2025-09-03T16:00:00Z · prod 2025-09-03T16:30:00Z (harmonygames-Games/match3d-backend#41#c_2) · reviews: APPROVED contractor 2025-09-03T18:05:00Z (harmonygames-Games/match3d-backend#41#rev_2) | unscoped | per-record evidence (ZOM-392) | no |
| harmonygames-Games/match3d-backend#42 | seeded | Teams: ack lives gift · author douglas · created 2025-09-03T15:00:00Z · merged 2025-09-05T16:00:00Z · prod 2025-09-08T17:18:00Z (harmonygames-Games/match3d-backend#42#c_2) · reviews: APPROVED contractor 2025-09-05T15:30:00Z (harmonygames-Games/match3d-backend#42#rev_2) | unscoped | per-record evidence (ZOM-503) | no |
| harmonygames-Games/match3d-backend#43 | seeded | Inventory: drop non-card items from equipped · author contractor · created 2025-09-04T11:10:00Z · merged 2025-09-04T12:30:00Z · prod 2025-09-04T12:50:00Z (harmonygames-Games/match3d-backend#43#c_2) · reviews: no human review | unscoped | per-record evidence (ZOM-518) | no |
| harmonygames-Games/match3d-backend#44 | seeded | Profile: other players profile v2 · author contractor · created 2025-09-04T22:00:00Z · merged 2025-09-08T15:30:00Z · prod 2025-09-08T17:18:00Z (harmonygames-Games/match3d-backend#44#c_2); rollback 2025-09-20T02:00:00Z (harmonygames-Games/match3d-backend#44#c_3); prod 2025-09-22T17:30:00Z (harmonygames-Games/match3d-backend#44#c_4) · reviews: CHANGES_REQUESTED douglas 2025-09-05T16:00:00Z (harmonygames-Games/match3d-backend#44#rev_2); APPROVED douglas 2025-09-08T15:10:00Z (harmonygames-Games/match3d-backend#44#rev_3) | unscoped | per-record evidence (ZOM-499) | no |
| harmonygames-Games/match3d-backend#45 | seeded | Inventory: keep equipped slots across sessions · author douglas · created 2025-09-08T15:10:00Z · merged 2025-09-10T16:00:00Z · prod 2025-09-10T18:20:00Z (harmonygames-Games/match3d-backend#45#c_2) · reviews: CHANGES_REQUESTED contractor 2025-09-09T17:00:00Z (harmonygames-Games/match3d-backend#45#rev_2); APPROVED contractor 2025-09-10T15:10:00Z (harmonygames-Games/match3d-backend#45#rev_3) | unscoped | per-record evidence (ZOM-531) | no |
| harmonygames-Games/match3d-backend#46 | seeded | Economy: September adjustments · author douglas · created 2025-09-09T15:30:00Z · merged 2025-09-09T19:50:00Z · prod 2025-09-09T20:29:00Z (harmonygames-Games/match3d-backend#46#c_2) · reviews: APPROVED arthur 2025-09-09T19:40:00Z (harmonygames-Games/match3d-backend#46#rev_2) | unscoped | per-record evidence (ZOM-537) | no |
| harmonygames-Games/match3d-backend#47 | seeded | Analytics: log endless_start on the server · author contractor · created 2025-09-11T17:00:00Z · merged 2025-09-12T19:00:00Z · prod 2025-09-27T16:20:00Z (harmonygames-Games/match3d-backend#47#c_2) · reviews: APPROVED arthur 2025-09-27T16:05:00Z (harmonygames-Games/match3d-backend#47#rev_2) | unscoped | per-record evidence (ZOM-444) | no |
| harmonygames-Games/match3d-backend#48 | seeded | Boss arena: infinite HP event config · author contractor · created 2025-09-15T13:00:00Z · merged 2025-09-16T15:40:00Z · prod 2025-09-16T16:35:00Z (harmonygames-Games/match3d-backend#48#c_2) · reviews: APPROVED douglas 2025-09-16T15:20:00Z (harmonygames-Games/match3d-backend#48#rev_2) | unscoped | per-record evidence (ZOM-487) | no |
| harmonygames-Games/match3d-backend#49 | seeded | Boss arena: mirror balance values · author douglas · created 2025-09-16T19:00:00Z · merged 2025-09-17T15:30:00Z · prod 2025-09-18T16:00:00Z (harmonygames-Games/match3d-backend#49#c_2) · reviews: APPROVED contractor 2025-09-17T15:10:00Z (harmonygames-Games/match3d-backend#49#rev_2) | unscoped | per-record evidence (ZOM-547) | no |
| harmonygames-Games/match3d-backend#50 | seeded | Boss arena: don't take a life on a win · author contractor · created 2025-09-18T15:00:00Z · merged 2025-09-19T15:30:00Z · prod 2025-09-27T14:30:00Z (harmonygames-Games/match3d-backend#50#c_2) · reviews: APPROVED douglas 2025-09-19T15:10:00Z (harmonygames-Games/match3d-backend#50#rev_2); COMMENTED arthur 2025-09-29T14:50:00Z (harmonygames-Games/match3d-backend#50#rev_3) | unscoped | per-record evidence (ZOM-550) | no |
| harmonygames-Games/match3d-backend#51 | seeded | Trophy path: ignore duplicate claim requests · author douglas · created 2025-09-18T20:00:00Z · merged 2025-09-19T22:00:00Z · dev 2025-09-19T22:20:00Z (harmonygames-Games/match3d-backend#51#c_2) · reviews: APPROVED contractor 2025-09-19T21:30:00Z (harmonygames-Games/match3d-backend#51#rev_2) | unscoped | per-record evidence (ZOM-435) | no |
| harmonygames-Games/match3d-backend#52 | seeded | Teams: push lives refresh to client · author douglas · created 2025-09-22T12:10:00Z · merged 2025-09-22T15:05:00Z · prod 2025-09-30T18:16:00Z (harmonygames-Games/match3d-backend#52#c_2) · reviews: APPROVED contractor 2025-09-22T14:50:00Z (harmonygames-Games/match3d-backend#52#rev_2) | unscoped | per-record evidence (ZOM-503) | no |
| harmonygames-Games/match3d-backend#53 | seeded | Boss arena: mirror refill and nuke values · author douglas · created 2025-09-22T16:00:00Z · merged 2025-09-23T15:30:00Z · prod 2025-09-24T16:00:00Z (harmonygames-Games/match3d-backend#53#c_2) · reviews: APPROVED contractor 2025-09-23T15:15:00Z (harmonygames-Games/match3d-backend#53#rev_2) | unscoped | per-record evidence (ZOM-553) | no |
| harmonygames-Games/match3d-backend#54 | seeded | Login streak: count days in player timezone · author douglas · created 2025-09-22T18:00:00Z · merged 2025-09-23T16:00:00Z · prod 2025-09-24T19:00:00Z (harmonygames-Games/match3d-backend#54#c_2); rollback 2025-09-28T03:10:00Z (harmonygames-Games/match3d-backend#54#c_3) · reviews: APPROVED contractor 2025-09-23T15:20:00Z (harmonygames-Games/match3d-backend#54#rev_2) | unscoped | per-record evidence (ZOM-557) | no |
| cmt_0b9e52e7a05129c16301 on ZOM-459 | seeded | 2025-08-25T11:40:00Z: client sends the algo level flag now. backend part is match3d-backend#38, plague race counts it | unscoped | per-record membership | no |
| cmt_112afca3ef67b713a9e7 on ZOM-509 | seeded | 2025-09-04T10:15:00Z: container + headlines come from the trophy path config, backend part is match3d-backend#39 | unscoped | per-record membership | no |
| cmt_877095d931428f1536df on ZOM-336 | seeded | 2025-09-03T15:50:00Z: cooler model done. it's usable (cools zombies down), Douglas says that needs a catalog entry on the backend too: match3d-backend#40 | unscoped | per-record membership | no |
| cmt_d02aec11deff05b555cc on ZOM-392 | seeded | 2025-09-04T10:20:00Z: 100+ levels pull their seeds from the server now, backend part match3d-backend#41 | unscoped | per-record membership | no |
| cmt_c95585f37ce6708a9ec4 on ZOM-503 | seeded | 2025-09-22T15:08:00Z: client side was ok, the gift call was the problem. backend parts are match3d-backend#42 (ack) and match3d-backend#52 (refresh push) | unscoped | per-record membership | no |
| cmt_99069485a5f5d5eb9ce3 on ZOM-518 | seeded | 2025-09-04T12:55:00Z: backend part is match3d-backend#43, drops items that aren't cards anymore from the equipped list on login | unscoped | per-record membership | no |
| cmt_b197d27aaaba58c9b89f on ZOM-499 | seeded | 2025-09-17T15:44:00Z: other players' profile fields come from the backend, that part is match3d-backend#44 | unscoped | per-record membership | no |
| cmt_81278f65a6828964fd37 on ZOM-531 | seeded | 2025-09-15T15:01:00Z: it was the backend wiping the slots on a new session. backend part match3d-backend#45 | unscoped | per-record membership | no |
| cmt_92b95a95aa3414a22c89 on ZOM-537 | seeded | 2025-09-15T15:05:00Z: new values are in match3d-backend#46 | unscoped | per-record membership | no |
| cmt_32c3a18150bf06ad3a12 on ZOM-444 | seeded | 2025-09-15T15:06:00Z: client fires it, and the backend logs endless_start too now: match3d-backend#47 | unscoped | per-record membership | no |
| cmt_41e71e303718899c0d3c on ZOM-487 | seeded | 2025-09-17T16:09:00Z: infinite HP boss config is served by the backend: match3d-backend#48 | unscoped | per-record membership | no |
| cmt_2e0b9655e5d932f6b7e1 on ZOM-550 | seeded | 2025-09-19T16:10:00Z: life was taken on the backend when you won boss arena. backend part match3d-backend#50 | unscoped | per-record membership | no |
| cmt_8dbc7c9e3101efc08508 on ZOM-435 | seeded | 2025-09-22T13:49:00Z: double tap sends two claims. backend part is match3d-backend#51, it ignores the second one | unscoped | per-record membership | no |
| cmt_e850768746208eefe527 on ZOM-557 | seeded | 2025-09-30T12:39:00Z: client side fixed in 0.3.124, the streak count itself is on the backend: match3d-backend#54 | unscoped | per-record membership | no |
| cmt_0f256875faad3cad9843 on ZOM-510 | seeded | 2025-09-11T16:45:00Z: rewards were off because the backend still had the old sheet. fix is the Zombie Lane rewards import on the backend | unscoped | per-record membership | no |
| cmt_bc49540005814cc8f0e1 on ZOM-256 | seeded | 2025-09-11T16:48:00Z: algo levels 2.0 pack is ready, needs the level pack imported on the backend | unscoped | per-record membership | no |
| cmt_7c7780e6f01e8b2c5103 on ZOM-436 | seeded | 2025-09-17T15:08:39Z: tested on device with 0.3.122, looks good | unscoped | per-record membership | no |
| cmt_9a6e40246a899fc380bc on ZOM-547 | seeded | 2025-09-17T16:01:00Z: balance values updated in the client sheet, backend copy in match3d-backend#49 | unscoped | per-record membership | no |
| cmt_c2bad7e49457b4f6c558 on ZOM-553 | seeded | 2025-09-30T12:38:00Z: refill/nuke values updated in the client sheet, backend copy in match3d-backend#53 | unscoped | per-record membership | no |
| cmt_7777dfa66681d9a8aa7a on ZOM-461 | seeded | 2025-08-25T11:45:00Z: spawn points come from the server seed now, backend part is match3d-backend#37 | unscoped | per-record membership | no |

### 9.2 Derived ground truth (from the records above; for the human's Oracle Events and rubric)

| Ticket | Server change(s) | On prod |
|---|---|---|
| ZOM-459 | #38 + plague race table import (dev) | N |
| ZOM-509 | #39 + trophy path copy table import (dev) | N |
| ZOM-336 | #40 | N |
| ZOM-392 | #41 | N |
| ZOM-503 | #42 + #52 | N |
| ZOM-518 | #43 | N |
| ZOM-499 | #44 | Y |
| ZOM-531 | #45 + loadout table import (dev) | N |
| ZOM-537 | #46 + economy table import (dev) | N |
| ZOM-444 | #47 + analytics events table import (dev) | N |
| ZOM-487 | #48 + boss arena HP table import (dev) | N |
| ZOM-550 | #50 | N |
| ZOM-435 | #51 | N |
| ZOM-557 | #54 | N |
| ZOM-510 | Zombie Lane rewards import (prod) | Y |
| ZOM-256 | algo levels 2.0 level pack import (dev) | N |
| ZOM-436 | analytics events table import (dev) | N |

Register: 17 rows. On prod 2 (ZOM-499, ZOM-510); not on prod 15 (ZOM-336, ZOM-392, ZOM-503, ZOM-518, ZOM-550, ZOM-435, ZOM-557, ZOM-256, ZOM-487, ZOM-537, ZOM-444, ZOM-531, ZOM-459, ZOM-509, ZOM-436). Out: ZOM-547, ZOM-553 (Arthur's reply in Leonard's thread), ZOM-461 (12 s before the cut), ZOM-457 (parent), the other 53 candidates (client/art/VFX comments). Writes: sheet in d_69fcebc484d472907b0b5c; Leonard (leonard.hayes@harmonygames.co) commenter share; DM reply in D05QQF7V404 with 2 on prod and the 15 keys not on prod; each of the 15 moved to Todo with a comment naming what still has to go out (ZOM-336 #40; ZOM-392 #41 needs a redeploy after its approval; ZOM-503 #52; ZOM-518 #43 needs an approval; ZOM-550 #50; ZOM-435 #51; ZOM-557 #54; ZOM-256 the algo level pack import; ZOM-487 the boss arena HP table import; ZOM-537 the economy table import; ZOM-444 and ZOM-436 the analytics events table import; ZOM-531 the loadout table import; ZOM-459 the plague race table import; ZOM-509 the trophy path copy table import); no new tickets.

## 10 Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| github | INT-01 | GitHub Slack app mirror | none: match3d-backend is not mirrored (36 base PRs, no copies in C050WGU41HR or C093LEZGF6J) |
| github | INT-23 | CodeRabbit walkthrough + COMMENTED review | seeded on every PR (#c_1, #rev_1) as on harmonygames-Games/match3d-backend#31 |
| github | INT-03 | linear[bot] PR comment | none: no Linear key in PR title/branch/body (base match3d-backend convention) |
| github | INT-12 | notification mails | none (optional) |
| linear | INT-04 | Linear Slack app posts | none: comments are not posted |
| linear | INT-05 | Linear e-mail digests | none (optional) |
| gcal | INT-11 | invitation mails | none: declared integration_exceptions no_notify for 463338c3d4e070df180b0269037ee17f@hg4 (calendar-only freeze time) |
| gdrive | INT-13 | Drive Slack DM on share | none |
| trello | INT-21 | Trello → Slack | none: no integration exists |
| slack | INT-22 | Slack e-mail notification | none (optional) |
| gmail | — | gmail: none (no integration originates in Gmail) | sender SENT copy + recipient copies |
| confluence | — | confluence: none in integrations.json | — |
| gdocs / gsheets | INT-13 | covered with gdrive | — |

## 11 Touched-data census and coherence hazards

Hazards walked from `references/universe_kb/coherence_hazards.json` (all six categories) over the census below.

Census: the 73 cohort tickets (`cohort.json`) and ZOM-461/480/479/489; match3d-backend PRs (base #1–#36 neighbours); the Douglas–Vincent DM D079SNE2TL4 (Sep 8–30 deploy messages), D05QQF7V404, #zombie-match3d C0880U9751A, #zombie-bugs C08R27X0EAH/1757307297.870139; ZM ROADMAP board 6851a6569f3bf818760632ab; page_cicd_pipeline, page_ops_home; the ZM beta page's comment thread (no base comments on seeded pages).

| Hazard | Category | Intersects | Disposition |
|---|---|---|---|
| T04 | temporal | ticket closed before its PR merged | excluded: every seeded PR merges before its ticket's completed_at (ZOM-503 15:11:03 vs #52 merge 15:05) |
| T01 | temporal | base 'reviewed' events with null created_at (harmonygames-Games/match3d-backend#31#ev_6) | seeded reviewed events carry created_at = submitted_at; base rows untouched |
| S03 | semantic | labels as categories | none used (ZOM-503 labels not read by any rule) |
| S02 | semantic | cross-team parents | ZOM-97 and ZOM-457 are same-team parents; card rule 1 settles parents |
| R04 | cross-service referential | Google URLs in text | none seeded; records named by title |
| R07 | cross-service referential | PR comments without Slack mirror | match3d-backend not mirrored (INT-01); consistent with harmonygames-Games/match3d-backend#14 |
| R01 | cross-service referential | Slack/mail cite keys | all cited keys exist (ZOM-547, ZOM-553; match3d-backend#49, #53) |
| Q01 | quantitative | thread counters | seeded parent C0880U9751A/1758937233.118904 reply_count 2 / reply_users 2 / latest 1758938832.553908; ask D05QQF7V404/1759266764.508127 reply_count 0 (no thread); Gmail thread douglas@harmonygames.co/1844721277206562572 holds 2 messages, snippet = newest |
| Q09b | quantitative | imports named in notes vs the log | every import a note names (economy, boss arena HP, plague race, trophy path copy, analytics events, loadout tables) has exactly one Console & imports row, target dev, dated after the note's PR approval or merge |
| Q09 | quantitative | deploy log vs PR record | every log row agrees with its prod: comment |
| L09 | state/lifecycle | merged PRs with no review | excluded: base PRs not cited; seeded #40/#43 designed (manifest hazard_acknowledgements) |
| L13 | state/lifecycle | post-clock work (match3d-backend#36, Oct 12) | excluded: not cited or modified (manifest hazard_acknowledgements) |
| L08 | state/lifecycle | open issues assigned to quiet people after the writes | ZOM-550 (EMPLOYEE_0032) moved to Todo by the agent; no seeded text names the assignee |
| I10 | identifier/format | Linear user ids | exact base ids (usr_65c76e0b87aa7e9b …) |
| I08 | identifier/format | GitHub logins are tokens | base tokens reused |
| I07 | identifier/format | CodeRabbit author vs timeline actor | seeded the same split (PERSON_6026 author, SVC_0321 actor) |

The State/Lifecycle and Referential hazards the task touches (L09, L13, R04, T04) carry `hazard_acknowledgements` with resolution `excluded` in the final manifest; none is a repaired hazard. quantitative: no hazard beyond Q01/Q09 in scope.

## 12 Platform follow-ups

- `linear_show_data` / `linear_list_issues(query)` may return comment bodies in bulk (Ask_Carriers [U]) — probe at the Opus pre-check; if so the 73-call surface collapses (manifest Unresolved).
- `github_get_issue_comments` vs `github_get_pull_request_comments` for conversation comments — confirm at the pre-check which one returns harmonygames-Games/match3d-backend#44#c_2.
- The freeze event's description (○) is supporting only; the start time (●) carries the fact.
- Post-clock rendering: base match3d-backend#36 (2025-10-12) and ZOM-563 (Done 2025-10-01T13:40Z) must stay invisible at the Oct 1 freeze.

## 13 Self-review

### Tool outputs (verbatim, final run)

`python3 Task_Authoring/tools/sql_lint.py task_inputs/01_Universe_Inject.sql`:

```
schemas touched (10): confluence, gcal, gdocs, gdrive, github, gmail, gsheets, linear, slack, trello
rows by schema: {'gdrive': 4, 'gdocs': 1, 'gsheets': 3, 'confluence': 6, 'slack': 9, 'trello': 5, 'gmail': 9, 'gcal': 5, 'github': 285, 'linear': 77}  total rows: 404  ops: {'insert': 404}
errors: 0  warnings: 18
  warn  line 25: confluence statement — unscoped and rarely opened by agents: make sure another record points here
  warn  line 28: confluence statement — unscoped and rarely opened by agents: make sure another record points here
  warn  line 30: confluence statement — unscoped and rarely opened by agents: make sure another record points here
  warn  line 32: confluence statement — unscoped and rarely opened by agents: make sure another record points here
  warn  line 34: confluence statement — unscoped and rarely opened by agents: make sure another record points here
  warn  line 36: confluence statement — unscoped and rarely opened by agents: make sure another record points here
  warn  line 45: slack.slack_messages.ts = 1758991212.775031 falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 45: slack.slack_messages.created_at = 2025-09-27T16:40:12.775031Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 51: slack.slack_messages.ts = 1758937233.118904 falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 51: slack.slack_messages.created_at = 2025-09-27T01:40:33.118904Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 53: slack.slack_messages.ts = 1758938751.402267 falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 53: slack.slack_messages.created_at = 2025-09-27T02:05:51.402267Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 55: slack.slack_messages.ts = 1758938832.553908 falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 55: slack.slack_messages.created_at = 2025-09-27T02:07:12.553908Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 383: github.github_pr_comments.created_at = 2025-09-20T02:00:00Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 489: github.github_pr_comments.created_at = 2025-09-27T16:20:00Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 579: github.github_pr_comments.created_at = 2025-09-27T14:30:00Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 709: github.github_pr_comments.created_at = 2025-09-28T03:10:00Z falls on a weekend (UTC) — business messages should be on weekdays
```

Warning dispositions: weekend (warn ×12): the designed freeze weekend Sep 27–28 (#50, #47 deploys, the #50 thread, Oliver's QA summary, #54 rollback) and Sep 20 02:00Z (#44 rollback, Friday evening in the deployer's time zone) — kept on purpose. Confluence (warn ×6): both pages are pointed to — page_zm_beta_oct10 by card rule 6, page_dd_launch_server_signoff is a decoy a 'server sign-off' search reaches; the two comments sit on page_zm_beta_oct10, which the card points to; disposition: intended.

`python3 Task_Authoring/tools/base_check.py task_inputs/01_Universe_Inject.sql`:

```
BASE CHECK (/injection A + C, static): PASS  — 404 inserts, 0 updates
Check A — records, references, IDs: PASS
Check C — dates and relationships: PASS
Warnings (1):
  line 153: gcal.gcal_events: meeting 463338c3d4e070df180b0269037ee17f@hg4 'ZM beta - server freeze' has 4 attendee(s) but no invitation mail ('Invitation: ZM beta - server freeze @ …') in any attendee mailbox — INT-11 base: 836/941 meetings with attendees have one (2298/2974 attendee mailboxes); add the copies or declare integration_exceptions [{record_id, reason: 'no_notify: …'}]
  note: github.github_branches: no base-reference rules (checked by sql_lint only)
  note: github.github_commits: no base-reference rules (checked by sql_lint only)
  note: github.github_pull_request_commits: no base-reference rules (checked by sql_lint only)
  note: gsheets.sheets_sheets: no base-reference rules (checked by sql_lint only)
```

Warning disposition: the INT-11 invitation warning is declared in the manifest's `integration_exceptions` (no_notify) — the freeze time must stay calendar-only (design T2).

`python3 Task_Authoring/tools/hardness_gate.py Working_Files/01_Hardness_Manifest.json task_inputs/01_Universe_Inject.sql`:

```
HARDNESS GATE (long): PASS
  [ok] effective_profile: effective_profile 'long' for 'Long Horizon' → thresholds 'long'
  [ok] sql_lint_clean: 0 lint error(s) — run tools/sql_lint.py
  [ok] base_consistency: /injection-style checks vs the base universe: A 0 finding(s), C 0 finding(s), 0 warning(s) — run tools/base_check.py --manifest
  [ok] persona_reach: 78 load-bearing seeded ids for douglas (58 in unscoped services = visible, 20 judged by persona_view check-sql); not provably visible: none
  [ok] fact_consistency: fact_check: 0 error(s) (8 declared facts), 0 drift warning(s); first: none — run tools/fact_check.py --manifest --no-leak
  [ok] hazard_scope: 0 pre-existing hazard(s) among task-touched records; state/lifecycle or referential without a verified resolution: none
  [ok] services_injected: 10 schemas injected (confluence, gcal, gdocs, gdrive, github, gmail, gsheets, linear, slack, trello); need ≥ 10
  [ok] rows: 404 INSERTed rows (UPDATE companions not counted; 404 rows in all); need ≥ 120
  [ok] services_carrying_weight: 10 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: schemas injected but absent from the design: none
  [ok] seeded_ids_exist_in_sql: 182 seeded ids cited; missing from SQL: none
  [ok] anchors: 2 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 18 fragments; need ≥ 12
  [ok] ask_fragment_services: 10 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 13 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 7 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 73; need ≥ 30 (source-defined: True)
  [ok] evidence_surfaces: 3 surfaces over 2 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 100; need ≥ 30
  [ok] call_budget: unconditional (verified) floor 175 of 175 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 100 (Long Horizon; plan ~600 for headroom)
  [ok] call_budget_spread: 10 services in budget; largest share outside the per-record phase 21% (≤ 50%)
  [ok] traps: 28 traps across 9 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 7 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 4 supersessions (3 with versions in ≥ 2 services, 2 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: 6 trap(s) with version_records; the records' own timestamps (SQL created_at/ts/date/updated_at, or the base record) must be strictly increasing in the listed order (oldest first); bad: none
  [ok] distractors: 7 distractors of 6 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 15 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 13 chains with 10 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] hidden_authorities: 2 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 1 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 13 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 7 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 5 writes over 4 services; each must depend on findings
```

### /injection Checks A–C walk (`Evals/0_Injection_Quality_Eval.md`)

| Check | Verdict | Evidence |
|---|---|---|
| Inventory | PASS | INSERT only (one row each), 0 UPDATE, 0 DELETE, no upserts (sql_lint ops; e.g. ZOM-503 comment row) |
| Check A — references | PASS | channels C0880U9751A/D05QQF7V404 exist with Douglas a member; board 6851a6569f3bf818760632ab and list 6851a674975da1fe76e70d93 exist; repo harmonygames-Games/match3d-backend exists; ZOM tickets exist; Linear authors exist (usr_65c76e0b87aa7e9b …); parents page_ops_home, Drive roots d_cd7849ec043ab3da107f8c / d_cc3e90160f490686039986 / d_bdf01b53c6a92c5e167c65 exist |
| Check A — uniqueness | PASS | 172 minted ids, 0 hits over the full collections (1.F) |
| Check B — structure | PASS | columns from the live schema; NOT NULL supplied (reviews seq, comments is_edited); literal JSON in *_json; no generated columns written |
| Check C — dates | PASS | all timestamps < 2025-10-01T00:00Z; replies after parents; comments before completed_at; PR created < merged; reviews/comments after created |
| Check C — statuses and counts | PASS | no state changes; thread counters set; Trello badges.comments 1 on the server card |
| Check C — superseding records | PASS | version_records strictly increasing (hardness_gate supersession_chronology ok) |

### Counter-readings

| Category | Counter-reading (strongest argument it FAILS) | Evidence that resolves it | Verdict |
|---|---|---|---|
| temporal | seeded PRs #37–#54 (Aug–Sep) sit above base #36 (Oct 12) | #36 is post-clock (L13), invisible at the freeze; harmonygames-Games/match3d-backend#36 not cited | PASS |
| temporal (base deploys) | base DMs date prod deploys that the seeds might contradict | seeded prod: notes sit on them: #46 20:29Z (D079SNE2TL4/1757449699.464389), #42/#44 17:18Z (D079SNE2TL4/1757355159.852859), #48 16:35Z (D079SNE2TL4/1758040504.640159), #52 18:16Z (D079SNE2TL4/1759256193.859279) | PASS |
| semantic | 'Beta sign-off' cards could be read as one rule set | titles say server side / client side; rule 1 of 68dabfe9bc2e8b969782e22d vs 68dac311754b38be05be7ea9 | PASS |
| cross-service referential | the email cites #49 and #53; the ZM beta page names a folder | harmonygames-Games/match3d-backend#49, #53 seeded; d_69fcebc484d472907b0b5c titled 'ZM Beta sign-off' | PASS |
| quantitative | the log's Prod deploys tab omits deploys after Sep 10 | intended partial list (doc: 'quick list'); every row present agrees (f_78bedc46245090a160d2dd) | PASS |
| state/lifecycle | tickets Done while their server change is not on prod | the task exists to catch this; Done = verified on dev (C08R27X0EAH/1758014179.489689) | PASS |
| state/lifecycle (sibling) | Douglas's base Sep 30 teams deploy makes ZOM-503 on prod | it is #52's prod: comment inside the freeze with only the contractor's approval (harmonygames-Games/match3d-backend#52#rev_2) | PASS |
| identifier/format | PR comments ids could collide with base numbering | #37–#54 absent from the base; ids are the PR id plus #c_n as in harmonygames-Games/match3d-backend#31#c_1 | PASS |
| people status | a seeded speaker could be inactive at the clock | all 11 speakers active_sep_2025 (activity.json, 1.C) | PASS |
| other | designed disagreements read as two silent system fields | each is a dated human claim or older doc version (6 Intended disagreements) | PASS |
| intended disagreement 1 | C0880U9751A/1758295268.611352 says Monday 29th; evt_0f489eb7fb46ada9660881 says Fri 26 22:00Z is an unintended inconsistency | the calendar event, updated Sep 23, newer and named in the doc | PASS |
| intended disagreement 2 | C0880U9751A/1758991212.775031 says all server fixes are on prod is an unintended inconsistency | PR comments/reviews (harmonygames-Games/match3d-backend#54#c_3 etc.) | PASS |
| intended disagreement 3 | D05QQF7V404/1758571837.284511 (Douglas: fix is out; seeds on prod since the 3rd) is an unintended inconsistency | harmonygames-Games/match3d-backend#51#c_2 (dev), #41#rev_2 after #41#c_2 | PASS |
| intended disagreement 4 | C0880U9751A/1748450537.204611 (May: merged = live) is an unintended inconsistency | doc f_470ae81236d5bd39045dc1 | PASS |
| intended disagreement 5 | page_dd_launch_server_signoff (DD launch rules) is an unintended inconsistency | card 68dabfe9bc2e8b969782e22d (ZM beta) | PASS |
| intended disagreement 6 | f_78bedc46245090a160d2dd Prod deploys tab stops on Sep 10 is an unintended inconsistency | doc: the PR's prod: comment is the record | PASS |
| intended disagreement 7 | D079SNE2TL4/1759256193.859279 + /1759269524.769369 (teams changes on prod, works) is an unintended inconsistency | doc freeze clause; harmonygames-Games/match3d-backend#52#rev_2 | PASS |
| intended disagreement 8 | cmt_41e71e303718899c0d3c names #48 only; comment_zm_beta_oct10_c2 adds the boss arena HP table import is an unintended inconsistency | Arthur's inline review comment (the rules' author, on his own Approve) + the deploy log (dev) | PASS |
| intended disagreement 9 | cmt_92b95a95aa3414a22c89 names #46 only; harmonygames-Games/match3d-backend#46#rc_1 adds the economy table import is an unintended inconsistency | Arthur's inline review comment (the rules' author, on his own Approve) + the deploy log (dev) | PASS |
| intended disagreement 10 | cmt_32c3a18150bf06ad3a12 and cmt_81278f65a6828964fd37 name one PR each; cmt_7c7780e6f01e8b2c5103 is a QA device note; douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> adds the analytics events and loadout table imports is an unintended inconsistency | Arthur's reply-all (the rules' author, Sep 30, newest) + the deploy log (dev) | PASS |
| intended disagreement 11 | cmt_0b9e52e7a05129c16301 names #38 only; harmonygames-Games/match3d-backend#38#rc_1 adds the plague race table import is an unintended inconsistency | the reviewer's inline comment on #38 (on the Approve) + the deploy log (dev) | PASS |
| intended disagreement 12 | cmt_112afca3ef67b713a9e7 names #39 only; harmonygames-Games/match3d-backend#39#rc_1 adds the trophy path copy table import is an unintended inconsistency | Douglas's inline comment on #39 (on his Approve) + the deploy log (dev) | PASS |

### Revision 2 — /injection review 6ad90ea979eb9e5d89f8879f (PASS, 5 advisories) and fixes

The platform `/injection` review of SQL f48302c6acec returned FINAL VERDICT: PASS (A, B, C PASS; lint 0 FAIL / 0 CHECK / 0 INFO; report saved as `extra:injection-report-douglas-2026-10-26`). All five optional advisories were applied:

| Advisory | Fix |
|---|---|
| 1 snapshot columns not covered | dropped `maintainer_can_modify`, `requested_team_slugs_json` (github_pull_requests) and `extras_json` (gcal_events), all NULL; kept `seq` (NOT NULL in `references/universe_schema_live.json`) and `sequence` |
| 2 thread parent thread_ts_legacy NULL | parent C0880U9751A/1758937233.118904 now carries its own ts, as the 1,209 base parents in C0880U9751A do |
| 3 Douglas commit identity | Douglas-authored commits use PERSON_5760_NAME / PERSON_5760_EMAIL like his 68 base commits (harmonygames-Games/match3d-backend#31 neighbours) |
| 4 fields the base never populates | `merge_commit_sha` NULL and an empty `parent_shas_json` list on every seeded PR/commit |
| 5 wording/timing | ZOM-510 comment now says the fix is the Zombie Lane rewards import (the log shows it on prod since 2025-09-08); folder d_d71300168ca5dffa4db8b3 created 2025-09-29T17:05Z, before the ZM beta page (17:15Z) and the client card (17:34Z) name it |

### Revision 3 — /prompt review 6ad90ea979eb9e5d89f8879f (NON-FAIL 3, Cross-Service Coherence) and fixes

The /prompt review of prompt a0414d89216a with SQL 99128292df92 found one referential inconsistency: the deploy doc (f_470ae81236d5bd39045dc1) and the deploy log row 1 (f_78bedc46245090a160d2dd) name a match3d-backend prod branch that no branch row held. Fixed, and the whole class (a seeded text naming an artifact that no record holds) was swept:

| Reference | Fix |
|---|---|
| prod branch | branch harmonygames-Games/match3d-backend:prod added; head = a cherry-pick commit of #52 (2025-09-30T18:05Z, Douglas), matching the doc and the #52 prod: comment (harmonygames-Games/match3d-backend#52#c_2) |
| 'Zombie Lane rewards sheet v7' (no such sheet in Drive) | renamed to 'Zombie Lane rewards' in the log row and the ZOM-510 comment; base names only a reward sheet in Slack (C08R27X0EAH/1757307297.870139) |
| 'Register: the DD launch sheet' on page_dd_launch_server_signoff (no such sheet) | line replaced by 'Douglas keeps the deploy list.' |
| client card 'since the Aug 15 build' (no build of that date in the base) | 'closed since Aug 15' (trello:68dac311754b38be05be7ea9) |
| ZOM-457 parent comment 'nothing needed in match3d-backend' beside a child with a backend PR (review note, not scored) | parent note now says the fixes are on the child tickets |

Kept: 'zm-api:NN' task definitions (ECS revisions, page_cicd_pipeline describes them; no universe record type); 'balance sheet' in Arthur's email (Vincent's 'balance sheet.xlsx' f_341d9b8f6396daadb6806f exists); Android 0.3.122 / iOS 0.3.38 (D05QQF7V404/1758146982.108989).

### Revision 4 — /prompt review 6ad90ea979eb9e5d89f8879f rerun (FAIL 2, Cross-Service Coherence: State/Lifecycle) and fixes

The rerun on SQL 5918bcb0e3eb found that the neutral comments seeded on two OPEN non-cohort tickets read as fixed-and-verified (ZOM-535 Todo: 'client side fix … ok on 0.3.132'; ZOM-504 Backlog: 'client only, checked on 0.3.132'), contradicting their state and Trello card 68c451141c69fb8af1b4568e ('it's still happens for samsung devices'). Fixed by deleting both comments and both updated_at UPDATEs. Class sweep: every remaining seeded comment sits on a ticket whose base state is Done (73 cohort + ZOM-461, ZOM-480, ZOM-479, ZOM-489), so a fixed/checked note agrees with its state; base Slack Aug–Sep holds no 'still / not working / again' message about any commented ticket; card 68c451141c69fb8af1b4568e lists ZOM-498, ZOM-536, ZOM-557, ZOM-558, ZOM-561 without a per-ticket note (a to-do list whose Done tickets are pre-existing base state), and ZOM-557's comment already places the remaining part on the backend (#54, rolled back).

### Re-verified facts

Re-read from the exports this session: the cohort's completed_at/updated_at (all before the clock, `cohort.json`), ZOM-461 11:51:48Z and ZOM-459 11:53:11Z, the D079SNE2TL4 deploy messages (Sep 8 17:17:43Z, Sep 9 20:28:19Z, Sep 16 16:35:04Z, Sep 30 18:16:33Z), match3d-backend base PRs #1–#36 and their reviews (Douglas 15 APPROVED, contractor 15 APPROVED, CodeRabbit 11 COMMENTED), ZM ROADMAP idShort max 79, Drive roots.

### Revision 5 — hardening round 1 (`01a_Hardening_Report.md`, MODE B on the six baseline runs)

The baseline (six Opus 5.5 runs, 134–193 calls) beat every rule-application trap and failed only one fact, identically in all six (Arthur's separate amendment mail never searched: 18 rows, '10 on prod, 8 not'). Three independent decisive facts now sit behind the three reading habits the runs split on (report §4, §10):

| Change | Records | Fact that changed |
|---|---|---|
| Arthur's amendment moved into Leonard's go/no-go thread as his reply-all (In-Reply-To Leonard's message); the separate 'Beta sign-off - server side' mail and its 3 thread rows are gone; Oliver no longer gets a copy | douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> in douglas@harmonygames.co/1844721277206562572 (2025-09-30T20:41:27Z) | ZOM-547/553 leave the register only by reading Leonard's thread in full |
| QA question + Arthur's reply on the ZM beta page; deploy-log import row 'boss arena HP table' (dev, 2025-09-17 15:50) | comment_zm_beta_oct10_c1, comment_zm_beta_oct10_c2; f_78bedc46245090a160d2dd | ZOM-487 Y → N (two server changes, the import is dev only) |
| Arthur's thread reply on his own ask (removed in revision 6); deploy-log import row 'economy table' (dev, 2025-09-16 14:20) | D05QQF7V404/1759267192.331870; f_78bedc46245090a160d2dd | ZOM-537 Y → N (two server changes, the import is dev only) |
| match3d-backend#40 renamed 'Catalog: add usable item entries' (was 'Items: make the cooler a usable item'); branch, commit message and CodeRabbit text follow | harmonygames-Games/match3d-backend#40 | ZOM-336's server change is linked only by its Linear comment (design T12/T13); run-3's PR-title-to-ticket-title shortcut found it through the old title |

Ground truth now: 16 rows, 6 on prod, 10 not (9.2). Sheet modified_time moves to 2025-09-17T15:55Z (newest log row). Coherence sweep: the Linear comments on ZOM-487 (#48) and ZOM-537 (#46) name the PR only, which stays true (the PR is on prod); Oliver's Sep 27 summary predates his Sep 30 page question; no record names the new imports' targets except the log; every seeded reference in the new text (#46, #48, ZOM-487, ZOM-537, 'your deploy log', 'Leonard') resolves to a record.

### Revision 6 — hardening round 2 (`01a_Hardening_Report.md` §15, MODE B on the six round-1 baseline runs)

The round-1 baseline (six Opus 5.5 runs, 163–220 calls) opened Arthur's Slack thread reply in 6/6 runs (reply_count 1 on the first message every run reads), read Leonard's thread in 5/6 and the beta page's comments in 1/6: one dominant pattern (ZOM-487 wrong) in 4/6 runs. The ZOM-537 fact moves to where the runs did not look:

| Change | Records | Fact that changed |
|---|---|---|
| Arthur's Slack thread reply on the ask removed (the ask is a plain message again, reply_count 0) | D05QQF7V404/1759266764.508127 | no Slack record names the economy table import |
| Arthur's inline review comment on match3d-backend#46 (lib/zombies_game/economy.ex, line 21, attached to his Approve rev_2, 2025-09-09T19:40:00Z) | harmonygames-Games/match3d-backend#46#rc_1 | ZOM-537 still N; the link from the 'economy table' log row to ZOM-537 is now only this comment (read in 1/6 runs for #46) |

Ground truth unchanged: 16 rows, 6 on prod, 10 not (9.2). Coherence: the comment (Sep 9) precedes Douglas's dev import (Sep 16 14:20) and his Linear note naming #46 (Sep 15), which stays true but incomplete; #46's prod: comment (20:29) and Arthur's Approve (19:40) are unchanged; 'economy table' appears in no other seeded or base record about match3d-backend (base hits are GameOfDominoes#1764 'Plinko economy table updates', a different repo and game).

### Revision 7 — hardening round 3 (`01a_Hardening_Report.md`, MODE B on the six round-2 baseline runs)

The round-2 baseline (six Opus 5.5 runs, 194–228 calls) applied every rule correctly and split only on the hidden facts, but five runs missed all three in the same way. Under an atomic per-ticket rubric that gives a per-run SD of about 0.02-0.05 and one dominant pattern. Round 3 puts more rows behind the two habits that split runs across all three baselines:

| Change | Records | Fact that changed |
|---|---|---|
| Second point in Arthur's reply-all (same message, same time) | douglas@harmonygames.co/<CAuC1dALZU8ymJT3qa3a7Oqa5TvKZhNe0pW0P7QP@mail.gmail.com> | ZOM-444 and ZOM-531 Y → N (each also needs a dev-only table import); ZOM-436 joins the register (its only server change is the analytics events table import), N |
| Inline review comment on match3d-backend#38 by its approver (lib/zombies_game/plague_race.ex, line 34, on rev_2, 2025-08-25T09:20:00Z) | harmonygames-Games/match3d-backend#38#rc_1 | ZOM-459 Y → N |
| Inline review comment on match3d-backend#39 by its approver, Douglas (lib/zombies_game/trophy_path.ex, line 47, on rev_2, 2025-09-02T15:20:00Z) | harmonygames-Games/match3d-backend#39#rc_1 | ZOM-509 Y → N |
| Four Console & imports rows, all target dev, all by Douglas: plague race table (2025-08-26 10:30), trophy path copy table (2025-09-02 18:05), loadout table (2025-09-10 17:40), analytics events table (2025-09-12 19:20) | f_78bedc46245090a160d2dd | the dev-only second server change each note names |

Ground truth now: 17 rows, 2 on prod (ZOM-499, ZOM-510), 15 not (9.2). Coherence sweep: each new note precedes its log row (#38 approval Aug 25 09:20 < import Aug 26; #39 approval Sep 2 15:20 < import 18:05; #45 approval Sep 10 15:10 < loadout import 17:40 < #45 prod 18:20; #47 merge Sep 12 19:00 < analytics import 19:20); the log's modified time (Sep 17 15:55) stays the newest row; the Linear notes on ZOM-459, ZOM-509, ZOM-531 and ZOM-444 name the PR only, which stays true; ZOM-436's QA note ('tested on device with 0.3.122, looks good') does not claim the fix was client only; the four table names have 0 base hits in github, gsheets, gmail, linear and slack (scan_complete true); the email's references (ZOM-444, ZOM-436, ZOM-531, 'your deploy log') all resolve to records.

Unresolved: (1) `linear_show_data` / `linear_list_issues(query)` bulk comment behaviour unverified (§12). (2) The call budget is a plan (now 169); the baselines measured 134–193, 163–220 and 194–228 calls. (3) Find rates are measured habits from 20 runs (report §2); one fresh batch can still land off them.

```
STAGE GATE injection: PASS — Task_Authoring-2/task_inputs · 01_Universe_Inject.sql#2131bbeff16b · 01_Hardness_Manifest.json#dac54299d2c5 · 01_Grounding_Dossier.md#3cc21f8ed2b7 · blocking 0 · warnings 0 · checks 28
[PASS] structure.outputs: 3 output(s) present: 01_Universe_Inject.sql, 01_Hardness_Manifest.json, 01_Grounding_Dossier.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json)
[PASS] chain.scenario: upstream 'scenario' PASS pasted and current (01_Scenario_Design.md#66967771208f, 01_Hardness_Manifest.draft.json#781b05e72482)
[PASS] structure.sections: 17 required sections present and non-empty (01_Grounding_Dossier.md)
[PASS] structure.placeholders: no placeholders in 01_Grounding_Dossier.md
[PASS] evidence.entity: 10/10 items carry a source pointer (min 90%)
[PASS] evidence.keyword: 17/17 items carry a source pointer (min 100%)
[PASS] evidence.persona_reach: 22/22 items carry a source pointer (min 100%)
[PASS] evidence.record_ledger: 28/28 items carry a source pointer (min 100%)
[PASS] evidence.facts_for_human: 81/81 items carry a source pointer (min 100%)
[PASS] tool.sql_lint: sql_lint re-run matches the paste: errors 0, warnings 18, rows 404
[PASS] review.warning_dispositions: every sql_lint warning class dispositioned (confluence statement — unscoped and rare×6, weekend×12)
[PASS] tool.base_check: base_check pasted PASS; re-run PASS
[PASS] tool.hardness_gate: hardness_gate (SQL) pasted PASS; re-run PASS
[PASS] structure.design_delta: final manifest keeps all 70 draft ids
[PASS] tool.check_sql_pasted: persona_view check-sql --load-bearing output pasted with verdict PASS
[PASS] reach.injection: 23 scoped load-bearing ids YES for douglas
[PASS] structure.facts_declared: manifest declares 8 load-bearing fact(s) in `facts`
[PASS] tool.fact_check: fact_check --no-leak pasted PASS; re-run PASS
[PASS] kb.coherence_hazards: coherence audit cites 15 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 11 seeded speakers each cited with activity.json status; conventions.json cited
[PASS] kb.integrations: companions listed per integrations.json (10 INT ids, services ['confluence', 'gcal', 'gdocs', 'gdrive', 'github', 'gmail', 'gsheets', 'linear', 'slack', 'trello'])
[PASS] boundary.anchor_naming: 4 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 21 evidenced counter-readings (of 23 found; need ≥ 19) in 01_Grounding_Dossier.md
[PASS] review.coverage: self-review addresses all 9 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

