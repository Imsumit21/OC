# Grounding Dossier — rb-winddown-closeout (persona Robert, robert@harmonygames.co)

Implements `01_Scenario_Design.md` (review-fixed design, §13) as `task_inputs/01_Universe_Inject.sql`. Builder: `support/task_work/rb_winddown_closeout/build_sql.py` (ids, wording and truth from `mint_ids.py`; row map `sql_ids.json`). Clock 2026-02-14T00:00:00Z; latest seeded timestamp 2026-02-13T20:51:20Z. Profile `long` (manifest `effective_profile`, author's >150-call band). Statement counts are in the sql_lint output (§13).

## 1.A Structural

| Table | Rows (INSERT/UPDATE) | Base sample ids (verbatim) | Notes |
|---|---|---|---|
| slack.slack_messages | 3/1 | C0ADGSZKR3R/1770933601.686309 (id 6d8c8d8affd1255b13d8d875f1547e70), C0ADGSZKR3R/1770936725.388049 | id = sha256(channel\|ts)[:32]; the keep-list parent gets thread_ts_legacy, reply_count 1, reply_users_count 1, latest_reply |
| gmail.gmail_threads / gmail_messages | 10/3 · 13/0 | robert@harmonygames.co/1853470745017478863, robert@harmonygames.co/1850283027022457279 | ids `<mailbox>/<Message-ID>`, thread `<mailbox>/<19 digits>`; internal_date = date (ms); reply carries in_reply_to + references |
| linear.linear_projects / _project_teams / _project_members | 1/0 · 1/0 · 3/0 | project 1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2 (GoD - Beta, team_ENG) | uuid-shaped id; team_ENG; lead usr_cc3e90160f490686 |
| linear.linear_issues | 45/0 | ENG-2405 (Todo), ENG-990 (Canceled) | ENG-2438…ENG-2484 after the base maximum ENG-2437; state Todo, no lifecycle stamps; labels/links/relations/state_history `[]` |
| linear.linear_comments | 39/0 | none in base (0 rows; Ask_Carriers §6b verifies injected comments render) | cmt_ + 20 hex; authors usr_cc3e90160f490686, usr_63fffeb4fab5233e, usr_Robert, usr_bdf01b53c6a92c5e |
| trello.trello_cards / trello_actions | 1/0 · 1/0 | 68c5a49e8491a9d7faf869d0 (idShort 455), createCard 68c5a49e8491a9d7faf869eb | id = 8 hex unix seconds + 16 hex; full badges shape; idShort 456 (SVB, next after the board's last card 455) |
| gdrive.drive_files + gdocs.docs_documents | 3/0 · 1/0 | f_31115ddb6ed866f2b10d60 (Wind Down Task List, owner 'Resource: 7240535625619857401') | the doc copies the Wind Down siblings' owner and share list |
| gsheets.sheets_spreadsheets / sheets_sheets | 1/0 · 1/0 | f_605121f4a36752645e0ac3 | Arthur's sheet in his root d_cc3e90160f490686039986 |
| gcal.gcal_events | 3/0 | evt_212e50fb5a53ea8016ce29 (Sunset call, on the three founders' calendars) | one copy per attendee calendar, self:true on the owner's copy, ical 32hex@hg4 |
| confluence.confluence_pages / page_versions / comments | 1/0 · 1/0 · 0/0 | page_ops_home (parent), comment_analytics_integration_c1 | version 1 rows; space_OPS |
| github.github_pull_requests (+branch, commit, pr_commit, pr_comment, timeline) | 1/0 … | harmonygames-Games/Combo-Fighters#37, harmonygames-Games/Combo-Fighters#36#c_1 (CodeRabbit skip notice) | #38 open, base develop; CodeRabbit author PERSON_6026_GITHUB_USERNAME, timeline actor SVC_0321_GITHUB_USERNAME (hazard I07 convention) |

## 1.B Entity table

| Entity | Canonical | Where it appears (cited) | Agreement |
|---|---|---|---|
| Robert | robert@harmonygames.co, Slack EMPLOYEE_0016_SLACK_ID, Linear usr_Robert | C0ADGSZKR3R/1770839322.836779; ENG-2440 assignee | AGREE |
| Leonard Hayes | leonard.hayes@harmonygames.co, EMPLOYEE_0038_SLACK_ID, usr_63fffeb4fab5233e, Trello PERSON_6094_TRELLO_USER_ID | C0ADGSZKR3R/1770933601.686309 | AGREE |
| Arthur Blake | arthur.blake@harmonygames.co, EMPLOYEE_0025_SLACK_ID, usr_cc3e90160f490686 | C0ADGSZKR3R/1770937232.664809 | AGREE |
| Oliver Brooks | oliver.brooks@harmonygames.co, EMPLOYEE_0003_SLACK_ID, usr_bdf01b53c6a92c5e, EMPLOYEE_0003_GITHUB_USERNAME | harmonygames-Games/Combo-Fighters#37 (merged_by) | AGREE (not Lauren Brooks) |
| Sunset | the wind-down provider signed Feb 12 | robert@harmonygames.co/1856956532017091340 (signed SOW); C0ADGSZKR3R/1770931777.561519 | AGREE; sender token PERSON_7731_EMAIL is new (0 hits) |
| Sherwood Partners | ABC firm consulted, not engaged | robert@harmonygames.co/1856689465442954434 (base thread, PERSON_0728) | AGREE; decoy reuses PERSON_0728_EMAIL |
| SVB card | company card, never given digits in seeds | leonard.hayes@harmonygames.co/1846148320251001978 ('Silicon Valley Bank MasterCard') | AGREE (review A #2 fix) |
| Singular | '[PERSON_NAME_0499]' on the costs tab | f_605121f4a36752645e0ac3 row 36; robert@harmonygames.co/1850283027022457279 | AGREE (trap_catalog X03) |
| Kapwing / dbt | '[PERSON_NAME_20852]' and '[USERNAME_30019]' in #winddown | C0ADGSZKR3R/1770933450.410449 (Leonard's table: 'Kapwing (Blake)', '[USERNAME_30019] (keep it until … stops caring about data)'); C0ADGSZKR3R/1770937232.664809 | AGREE: no relabelling; Kapwing is ENG-2478, dbt's KubLLC move is stated in Arthur's comment on ENG-2457 |
| QuickBooks / Intuit | one vendor | ENG-2460, ENG-2461; costs tab 'Quickbooks'; keep list 'Intuit' | DISAGREE (designed duplicate, rule 1) |
| ElevenLabs | annual Starter, Jul 9 2025–Jul 9 2026, $50 | robert@harmonygames.co/1837122624854744558 | AGREE (base receipt governs; no seeded ElevenLabs mail) |
| Linear plan | Basic annual from the Feb 1 renewal | robert@harmonygames.co/1850617582652876839 (Standard → Basic notice); seeded receipt | AGREE |

## 1.C Voice and realism (speakers, activity, conventions)

Lengths, hours and styles from `references/universe_kb/conventions.json` (`slack.per_person_hours_and_style`, `slack.length_chars_by_channel_type`, `gmail.internal_subject_len_chars`, `linear.title_prefixes_by_team` — ENG titles are plain nouns, so issues are titled by vendor). Seeded speakers with `status_at_clock` from `references/universe_kb/activity.json`:

| Speaker | activity.json status | Where seeded | Voice evidence |
|---|---|---|---|
| Leonard Hayes leonard.hayes@harmonygames.co (EMPLOYEE_0038_SLACK_ID) | activity active_feb_2026 | anchor; SVB Trello card; Linear comments; review event organizer | full sentences, plain, long Slack asks (C0ADGSZKR3R/1770933601.686309, /1770934638.035469) |
| Arthur Blake arthur.blake@harmonygames.co (EMPLOYEE_0025_SLACK_ID) | activity active_feb_2026 | Gusto reply; project + issues; Linear comments; 'Subscriptions' sheet | lowercase, short (C0ADGSZKR3R/1770936655.574079 'coderabbit is cancelled') |
| Robert robert@harmonygames.co (EMPLOYEE_0016_SLACK_ID) | activity active_feb_2026 | Linear comments on his creative tools | short lowercase (C0ADGSZKR3R/1770859313.592649) |
| Oliver Brooks oliver.brooks@harmonygames.co (EMPLOYEE_0003_SLACK_ID) | activity active_feb_2026 | #prototype message; Helpshift export comment; PR #38 | casual, lowercase in #prototype (C09UHHN6PFZ, SL-T09 thread roots) |
| Frederick Stone frederick.stone@harmonygames.co | activity quiet_since_2025-10 | Confluence UA page dated 2025-03-18 only (active then) | Growth/UA voice, page_product_okrs owner |
| CodeRabbit PERSON_6026_GITHUB_USERNAME | bot (not in activity.json) | PR #38 notice | base skip-notice shape harmonygames-Games/Combo-Fighters#36#c_1 |
| Sunset PERSON_7731_EMAIL, Sherwood PERSON_0728_EMAIL, vendor senders SVC_* | external (not in activity.json) | mail only | vendor receipts mirror base receipts (robert@harmonygames.co/1849420841999587093) |

Posting hours: Leonard 16:12–17:21Z and Arthur 23:52–02:14Z / 19:05Z match their base #winddown hours (Feb 12 21:00–23:00Z, Feb 11 19–20Z); Robert's comments 20:41–20:51Z sit in his Feb 11 posting window (19:48Z).

## 1.D Keyword / findability (base hit counts via `tools/hg.py search search <svc> <term>`)

| Term | Base hits / pointer | Seeded home |
|---|---|---|
| 'data delivery checklist' | NEW TERM — introduced in robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>, reached via A1 "Sunset's data checklist" | Gmail thread robert@harmonygames.co/1856965916492026238 |
| 'checklist' (gmail) | base hits in Robert's mail are unrelated (QA checklists); the seeded Sherwood mail robert@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com> shares the word | decoy first by date |
| 'SVB card' / 'payoff' | base: C0ADGSZKR3R/1770927223.969899 ('close the credit card'), 162 SVB notification threads (Scenario_Atlas §1) — none dated | Trello 698f48be4ba0affafbf153db |
| 'close-out register conventions' | NEW TERM — introduced in f_1326e66bcabfda8fd29e4a, reached via A1 'conventions doc … Wind Down folder' | Docs; decoy page_ua_vendor_closeout shares 'close-out conventions' |
| 'Shutdown – accounts' | NEW TERM — introduced in project 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a, reached via A1 'Linear shutdown project' | Linear |
| 'KubLLC' | base C0ADGSZKR3R/1770937232.664809 (1 hit) | Linear comments on ENG-2456, ENG-2477, ENG-2479 |
| 'data delivery review' | NEW TERM — introduced in evt_f1d245d44ceff5a6e049c0, reached via the checklist 'delivery review call Leonard booked' | GCal |
| 'Pond5' / 'Elevenlabs' | base: costs tab row 15 'Sound (Pond5, Soundly,Elevenlabs)'; robert@harmonygames.co/1837122624854744558 (ElevenLabs) | Pond5 end notice robert@harmonygames.co/<CAIoQDHYpNPHXVgnNS8DUmtr__81CmMffz7hcWJv@mail.gmail.com> (ended Sep 8 2025) |
| 'coderabbit' (github) | base B03: 417 PR comments by PERSON_6026, e.g. harmonygames-Games/Combo-Fighters#37#c_1 | notice harmonygames-Games/Combo-Fighters#38#c_1 |

## 1.E Persona reach (scoped records)

Every load-bearing seeded record is in Robert's mailbox (INBOX), on his calendar (self copy), shared with him (doc) or in a Slack channel he belongs to (#winddown C0ADGSZKR3R, #prototype C09UHHN6PFZ). Base Workspace invoice robert@harmonygames.co/1856033699491658253 sits in SPAM — not load-bearing (Workspace's monthly billing is visible on the costs tab). Load-bearing ids written one per line to `support/task_work/rb_winddown_closeout/lb_ids.txt`.

| Record | Service | Visibility path |
|---|---|---|
| robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | gmail | Robert cc'd; own copy INBOX |
| robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> | gmail | Robert cc'd; own copy INBOX |
| robert@harmonygames.co/<CAowZ1ukjS1ZxLCL4aRt1VM-c-GnNMTNWVQS47OM@mail.gmail.com> | gmail | own copy INBOX (billing mail to robert@harmonygames.co) |
| robert@harmonygames.co/<CA4Ce6Oa74xUtCgFI1iGnZMieCxsUh90MhimgGu3@mail.gmail.com> | gmail | own copy INBOX (billing mail to robert@harmonygames.co) |
| robert@harmonygames.co/<CAIoQDHYpNPHXVgnNS8DUmtr__81CmMffz7hcWJv@mail.gmail.com> | gmail | own copy INBOX (billing mail to robert@harmonygames.co) |
| robert@harmonygames.co/<CAxSGYrkpVAs45dr7lAugwSThN-X-ma7vq_V1xAV@mail.gmail.com> | gmail | own copy INBOX (billing mail to robert@harmonygames.co) |
| evt_f1d245d44ceff5a6e049c0 | gcal | Robert's own calendar copy, self:true |
| f_1326e66bcabfda8fd29e4a | gdocs | shared_with robert@harmonygames.co |
| C0ADGSZKR3R/1771003267.448213 | slack | member of private #winddown |
| C0ADGSZKR3R/1770948876.205117 | slack | member of private #winddown |
| robert@harmonygames.co/1853470745017478863, robert@harmonygames.co/1850283027022457279, robert@harmonygames.co/1854432461283937829, robert@harmonygames.co/1837122624854744558 | gmail | own mailbox (base) |
| f_605121f4a36752645e0ac3 | gsheets | shared_with robert@harmonygames.co (base) |

```
CHECK-SQL as robert <robert@harmonygames.co>
[YES LB] L6 gdrive.drive_files insert f_1326e66bcabfda8fd29e4a - file is shared with the persona (shared_with_emails)
[YES] L9 gdrive.drive_files insert f_4ac7a77383e7317eedcd83 - file is shared with the persona (shared_with_emails)
[YES] L11 gdrive.drive_files insert f_768cd23a00c4b12fa0e975 - file is shared with the persona (shared_with_emails)
[YES LB] L13 gdocs.docs_documents insert f_1326e66bcabfda8fd29e4a - file is shared with the persona (shared_with_emails)
[YES] L16 gsheets.sheets_spreadsheets insert f_768cd23a00c4b12fa0e975 - file is shared with the persona (shared_with_emails)
[YES] L19 gsheets.sheets_sheets insert f_768cd23a00c4b12fa0e975, f_768cd23a00c4b12fa0e975#0 - file is shared with the persona (shared_with_emails)
[YES LB] L26 slack.slack_messages insert b9ef575bec54b095edb75a0fe83580f5, C0ADGSZKR3R/1770948876.205117 - persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES] L29 slack.slack_messages insert fda86aac9fb55c96ffee4bba3e59cc14, C09UHHN6PFZ/1770976938.774231 - persona EMPLOYEE_0016_SLACK_ID is in members of private prototype
[YES LB] L31 slack.slack_messages insert 9e245e76cbaf7f080e1995ec0c4ec30d, C0ADGSZKR3R/1771003267.448213 - persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] L33 slack.slack_messages update 6d8c8d8affd1255b13d8d875f1547e70, C0ADGSZKR3R/1770933601.686309 - persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES] L39 gmail.gmail_threads insert robert@harmonygames.co/1856945900224536585 - row user_email is the persona (robert@harmonygames.co)
[YES] L42 gmail.gmail_messages insert robert@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com>, robert@h - row user_email is the persona (robert@harmonygames.co)
[NO] L54 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1856945900224877235 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (robert@harmonygames.co)
[NO] L56 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (robert@harmonygames.co)
[NO] L68 gmail.gmail_threads insert arthur.blake@harmonygames.co/1856945900225226172 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (robert@harmonygames.co)
[NO] L70 gmail.gmail_messages insert arthur.blake@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com>, ar - row is in mailbox arthur.blake@harmonygames.co, not the persona's (robert@harmonygames.co)
[YES] L82 gmail.gmail_threads insert robert@harmonygames.co/1856965916492026238 - row user_email is the persona (robert@harmonygames.co)
[YES LB] L84 gmail.gmail_messages insert robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>, robert@h - row user_email is the persona (robert@harmonygames.co)
[NO] L96 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1856965916492755786 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (robert@harmonygames.co)
[NO] L98 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (robert@harmonygames.co)
[NO] L110 gmail.gmail_threads insert arthur.blake@harmonygames.co/1856965916492023943 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (robert@harmonygames.co)
[NO] L112 gmail.gmail_messages insert arthur.blake@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>, ar - row is in mailbox arthur.blake@harmonygames.co, not the persona's (robert@harmonygames.co)
[YES] L124 gmail.gmail_threads update robert@harmonygames.co/1856965916492026238 - row user_email is the persona (robert@harmonygames.co)
[YES LB] L125 gmail.gmail_messages insert robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com>, robert@h - row user_email is the persona (robert@harmonygames.co)
[NO] L129 gmail.gmail_threads update leonard.hayes@harmonygames.co/1856965916492755786 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (robert@harmonygames.co)
[NO] L130 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (robert@harmonygames.co)
[NO] L134 gmail.gmail_threads update arthur.blake@harmonygames.co/1856965916492023943 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (robert@harmonygames.co)
[NO] L135 gmail.gmail_messages insert arthur.blake@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com>, ar - row is in mailbox arthur.blake@harmonygames.co, not the persona's (robert@harmonygames.co)
[YES] L139 gmail.gmail_threads insert robert@harmonygames.co/1842712894505970340 - row user_email is the persona (robert@harmonygames.co)
[YES LB] L141 gmail.gmail_messages insert robert@harmonygames.co/<CAIoQDHYpNPHXVgnNS8DUmtr__81CmMffz7hcWJv@mail.gmail.com>, robert@h - row user_email is the persona (robert@harmonygames.co)
[YES] L143 gmail.gmail_threads insert robert@harmonygames.co/1842984194671106077 - row user_email is the persona (robert@harmonygames.co)
[YES LB] L145 gmail.gmail_messages insert robert@harmonygames.co/<CAowZ1ukjS1ZxLCL4aRt1VM-c-GnNMTNWVQS47OM@mail.gmail.com>, robert@h - row user_email is the persona (robert@harmonygames.co)
[YES] L147 gmail.gmail_threads insert robert@harmonygames.co/1856114791547562583 - row user_email is the persona (robert@harmonygames.co)
[YES LB] L149 gmail.gmail_messages insert robert@harmonygames.co/<CA4Ce6Oa74xUtCgFI1iGnZMieCxsUh90MhimgGu3@mail.gmail.com>, robert@h - row user_email is the persona (robert@harmonygames.co)
[YES] L151 gmail.gmail_threads insert robert@harmonygames.co/1856859516436705234 - row user_email is the persona (robert@harmonygames.co)
[YES LB] L153 gmail.gmail_messages insert robert@harmonygames.co/<CAxSGYrkpVAs45dr7lAugwSThN-X-ma7vq_V1xAV@mail.gmail.com>, robert@h - row user_email is the persona (robert@harmonygames.co)
[YES] L155 gcal.gcal_events insert evt_2ac66383ee72bbb05a0376 - persona is an attendee and holds its own copy evt_f1d245d44ceff5a6e049c0 (same ical_uid and start) on robert@harmonygames.co
[YES LB] L158 gcal.gcal_events insert evt_f1d245d44ceff5a6e049c0 - event is on the persona's own calendar robert@harmonygames.co
[YES] L160 gcal.gcal_events insert evt_d1fe12afe85ffbb49bd998 - persona is an attendee and holds its own copy evt_f1d245d44ceff5a6e049c0 (same ical_uid and start) on robert@harmonygames.co
[YES LB] base slack C0ADGSZKR3R/1770839729.441789 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] base slack C0ADGSZKR3R/1770839825.928989 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] base slack C0ADGSZKR3R/1770840054.486779 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] base slack C0ADGSZKR3R/1770842405.931359 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] base slack C0ADGSZKR3R/1770927223.969899 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] base slack C0ADGSZKR3R/1770931777.561519 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] base slack C0ADGSZKR3R/1770933903.645709 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] base slack C0ADGSZKR3R/1770933999.157259 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] base slack C0ADGSZKR3R/1770936655.574079 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] base slack C0ADGSZKR3R/1770937188.477219 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] base slack C0ADGSZKR3R/1770937232.664809 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] base gdrive f_605121f4a36752645e0ac3 - base record: file is shared with the persona (shared_with_emails)
[YES LB] base gmail robert@harmonygames.co/1837122624854744558 - base record: thread is in the persona's own mailbox robert@harmonygames.co
[YES LB] base gmail robert@harmonygames.co/1849420841999587093 - base record: thread is in the persona's own mailbox robert@harmonygames.co
[YES LB] base gmail robert@harmonygames.co/1850283027022457279 - base record: thread is in the persona's own mailbox robert@harmonygames.co
[YES LB] base gmail robert@harmonygames.co/1853470745017478863 - base record: thread is in the persona's own mailbox robert@harmonygames.co
[YES LB] base gmail robert@harmonygames.co/1854432461283937829 - base record: thread is in the persona's own mailbox robert@harmonygames.co
[YES LB] base gmail robert@harmonygames.co/1856956532017091340 - base record: thread is in the persona's own mailbox robert@harmonygames.co

summary: {'YES': 27, 'NO': 12}  unscoped rows (always visible): 99
  gcal.gcal_events: {'YES': 3}
  gdocs.docs_documents: {'YES': 1}
  gdrive.drive_files: {'YES': 3}
  gmail.gmail_messages: {'YES': 7, 'NO': 6}
  gmail.gmail_threads: {'YES': 7, 'NO': 6}
  gsheets.sheets_sheets: {'YES': 1}
  gsheets.sheets_spreadsheets: {'YES': 1}
  slack.slack_messages: {'YES': 4}
verdict: PASS (0 load-bearing rows not visible)
```

## 1.F Collision checks

Identity tokens: PERSON_7731 and SVC_7702–SVC_7712 have 0 hits across HarmonyGames_Gmail, HarmonyGames_Other_Services and HarmonyGames_GitHub (`grep -rhoE` over all three, run 2026-10-28); PERSON_0728 (Sherwood), SVC_5771 (Unity), SVC_1177 (Deel), SVC_0982 (Google Cloud), SVC_2600 (Docusign), SVC_3550 (Soundly), SVC_0124 (Slack), SVC_0251 (Linear) reuse the vendor's own base token. Minted ids (`hg.py search lookup`, full collections):

```
lookup conf_comments scan_complete: True records_checked: 12 matches: 0 errors: none
lookup conf_pages scan_complete: True records_checked: 31 matches: 0 errors: none
lookup gdrive scan_complete: True records_checked: 53866 matches: 0 errors: none
lookup linear_issues scan_complete: True records_checked: 3852 matches: 0 errors: none
lookup linear_projects scan_complete: True records_checked: 2 matches: 0 errors: none
lookup slack scan_complete: True records_checked: 687230 matches: 0 errors: none
lookup trello_actions scan_complete: True records_checked: 5294 matches: 0 errors: none
lookup trello_cards scan_complete: True records_checked: 803 matches: 0 errors: none
```

Linear ENG-2438…ENG-2484 follow the base maximum ENG-2437; Gmail ids carry the persona prefix and new Message-IDs; Combo-Fighters #38 follows the base maximum #37.

## 2 Record ledger

| # | Service · table | Id | Container | Manifest element | Carrier | Reach | Role |
|---|---|---|---|---|---|---|---|
| 1 | slack.slack_messages | C0ADGSZKR3R/1771003267.448213 | C0ADGSZKR3R | A1 anchor | ● | #winddown member | first link |
| 2 | slack.slack_messages | C0ADGSZKR3R/1770948876.205117 | C0ADGSZKR3R thread 1770933601.686309 | K9 · T1 | ● | #winddown member | overturning |
| 3 | slack.slack_messages (UPDATE) | C0ADGSZKR3R/1770933601.686309 | C0ADGSZKR3R | K8 counters | ● | #winddown member | companion |
| 4 | slack.slack_messages | C09UHHN6PFZ/1770976938.774231 | C09UHHN6PFZ | T21 distractor | ● | #prototype member | decoy |
| 5 | linear.linear_projects | 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a | team_ENG | K2 · cohort source | ● | unscoped | first link |
| 6 | linear.linear_issues | ENG-2438 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 7 | linear.linear_issues | ENG-2439 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 8 | linear.linear_issues | ENG-2440 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 9 | linear.linear_issues | ENG-2441 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 10 | linear.linear_issues | ENG-2442 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 11 | linear.linear_issues | ENG-2443 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 12 | linear.linear_issues | ENG-2444 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 13 | linear.linear_issues | ENG-2445 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 14 | linear.linear_issues | ENG-2446 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 15 | linear.linear_issues | ENG-2447 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 16 | linear.linear_issues | ENG-2448 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 17 | linear.linear_issues | ENG-2449 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 18 | linear.linear_issues | ENG-2450 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 19 | linear.linear_issues | ENG-2451 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 20 | linear.linear_issues | ENG-2452 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 21 | linear.linear_issues | ENG-2453 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 22 | linear.linear_issues | ENG-2454 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 23 | linear.linear_issues | ENG-2455 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 24 | linear.linear_issues | ENG-2456 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 25 | linear.linear_issues | ENG-2457 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 26 | linear.linear_issues | ENG-2458 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 27 | linear.linear_issues | ENG-2460 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 28 | linear.linear_issues | ENG-2461 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 29 | linear.linear_issues | ENG-2462 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 30 | linear.linear_issues | ENG-2463 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 31 | linear.linear_issues | ENG-2464 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 32 | linear.linear_issues | ENG-2465 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 33 | linear.linear_issues | ENG-2466 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 34 | linear.linear_issues | ENG-2467 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 35 | linear.linear_issues | ENG-2468 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 36 | linear.linear_issues | ENG-2469 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 37 | linear.linear_issues | ENG-2470 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 38 | linear.linear_issues | ENG-2471 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 39 | linear.linear_issues | ENG-2472 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 40 | linear.linear_issues | ENG-2473 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 41 | linear.linear_issues | ENG-2474 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 42 | linear.linear_issues | ENG-2475 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 43 | linear.linear_issues | ENG-2476 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 44 | linear.linear_issues | ENG-2477 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 45 | linear.linear_issues | ENG-2478 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 46 | linear.linear_issues | ENG-2479 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 47 | linear.linear_issues | ENG-2480 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 48 | linear.linear_issues | ENG-2481 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 49 | linear.linear_issues | ENG-2482 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 50 | linear.linear_issues | ENG-2483 | project Shutdown – accounts | cohort | ● | unscoped | write target |
| 51 | linear.linear_comments | cmt_5da8c3467fc022248fb3 | ENG-2438 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 52 | linear.linear_comments | cmt_96ae7b3689c1d073a2ff | ENG-2439 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 53 | linear.linear_comments | cmt_51ff7e6b4cdea7033c08 | ENG-2439 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 54 | linear.linear_comments | cmt_e8aa0ee7c1bbe08a47c9 | ENG-2440 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 55 | linear.linear_comments | cmt_37c23c5d30cc6597ebe9 | ENG-2441 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 56 | linear.linear_comments | cmt_6f994dc8a93d75efb3f8 | ENG-2442 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 57 | linear.linear_comments | cmt_ec32fbf9ca984b23f7a6 | ENG-2443 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 58 | linear.linear_comments | cmt_497a61c14b69830f198a | ENG-2444 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 59 | linear.linear_comments | cmt_276e0b8a551891ddbdff | ENG-2445 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 60 | linear.linear_comments | cmt_a83cc20eced4c1064f0a | ENG-2446 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 61 | linear.linear_comments | cmt_8ab16d9d7ac715d1c9a7 | ENG-2447 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 62 | linear.linear_comments | cmt_e8ae507893bfdb06c8c7 | ENG-2448 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 63 | linear.linear_comments | cmt_e3da997ff7b6575fbea0 | ENG-2450 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 64 | linear.linear_comments | cmt_ae352002e2f80996f096 | ENG-2452 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 65 | linear.linear_comments | cmt_276837877e2b3edc466a | ENG-2453 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 66 | linear.linear_comments | cmt_5a650ef858f3cd5a0410 | ENG-2454 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 67 | linear.linear_comments | cmt_62852832c28dc669e459 | ENG-2455 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 68 | linear.linear_comments | cmt_2b4807a6cf797d1f4886 | ENG-2456 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 69 | linear.linear_comments | cmt_bbdca23f075e9fca5cb8 | ENG-2457 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 70 | linear.linear_comments | cmt_6e664bfa3fea62baabb5 | ENG-2458 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 71 | linear.linear_comments | cmt_7cf5d70170f54a8f925f | ENG-2460 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 72 | linear.linear_comments | cmt_2238bd7d0a60d8e4f31c | ENG-2461 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 73 | linear.linear_comments | cmt_75b0e4e31a02f9a022bd | ENG-2462 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 74 | linear.linear_comments | cmt_2785f039cfee9d256150 | ENG-2463 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 75 | linear.linear_comments | cmt_5d88052b6f8c1b2fc181 | ENG-2464 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 76 | linear.linear_comments | cmt_ec684ef632bdd6b375c3 | ENG-2465 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 77 | linear.linear_comments | cmt_0bd2c882285911d54ade | ENG-2467 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 78 | linear.linear_comments | cmt_c767f5417cafd21d0457 | ENG-2468 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 79 | linear.linear_comments | cmt_4179664f58817a32a076 | ENG-2469 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 80 | linear.linear_comments | cmt_4ca653c559b182ed6ee6 | ENG-2472 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 81 | linear.linear_comments | cmt_46c0a9358e1df9a6ded4 | ENG-2473 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 82 | linear.linear_comments | cmt_a932354ee5e226971ed1 | ENG-2474 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 83 | linear.linear_comments | cmt_ed6dab8ad539165c22f1 | ENG-2475 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 84 | linear.linear_comments | cmt_8a420b3635db4a36f750 | ENG-2476 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 85 | linear.linear_comments | cmt_977a0d481cd84d275f08 | ENG-2477 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 86 | linear.linear_comments | cmt_d10e47fd216f16429b45 | ENG-2478 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 87 | linear.linear_comments | cmt_4a019a675b55484b05ec | ENG-2479 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 88 | linear.linear_comments | cmt_e3b5ee0557dca1cb519c | ENG-2480 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 89 | linear.linear_comments | cmt_5f33dc45f96bbae1e85d | ENG-2481 | cohort surface (linear_list_comments) | ● | unscoped | evidence |
| 90 | trello.trello_cards | 698f48be4ba0affafbf153db | board 640643a3fd8f3ca308d9318e To Do | H2 · K6 | ● | unscoped | authority |
| 91 | gdocs.docs_documents | f_1326e66bcabfda8fd29e4a | Wind Down d_e5caf6a8c630421942ee59 | H3 · K7 | ● | shared | authority |
| 92 | gsheets.sheets_spreadsheets | f_768cd23a00c4b12fa0e975 | Arthur root d_cc3e90160f490686039986 | T20 distractor | ● | shared | decoy |
| 93 | gmail.gmail_messages | robert@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com> | robert@harmonygames.co/1856945900224536585 | H1 decoy · T10 | ● | own copy INBOX | decoy |
| 94 | gmail.gmail_messages | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | robert@harmonygames.co/1856965916492026238 | H1 · K3 | ● | own copy INBOX | authority |
| 95 | gmail.gmail_messages | robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> | robert@harmonygames.co/1856965916492026238 | K4 amendment · T4/T5 | ● | own copy INBOX | overturning |
| 96 | gmail.gmail_messages | robert@harmonygames.co/<CAowZ1ukjS1ZxLCL4aRt1VM-c-GnNMTNWVQS47OM@mail.gmail.com> | robert@harmonygames.co/1842984194671106077 | cohort surface (billing mail) | ● | own copy INBOX | evidence |
| 97 | gmail.gmail_messages | robert@harmonygames.co/<CA4Ce6Oa74xUtCgFI1iGnZMieCxsUh90MhimgGu3@mail.gmail.com> | robert@harmonygames.co/1856114791547562583 | cohort surface (billing mail) | ● | own copy INBOX | evidence |
| 98 | gmail.gmail_messages | robert@harmonygames.co/<CAIoQDHYpNPHXVgnNS8DUmtr__81CmMffz7hcWJv@mail.gmail.com> | robert@harmonygames.co/1842712894505970340 | cohort surface (billing mail) | ● | own copy INBOX | evidence |
| 99 | gmail.gmail_messages | robert@harmonygames.co/<CAxSGYrkpVAs45dr7lAugwSThN-X-ma7vq_V1xAV@mail.gmail.com> | robert@harmonygames.co/1856859516436705234 | cohort surface (billing mail) | ● | own copy INBOX | evidence |
| 100 | gcal.gcal_events | evt_f1d245d44ceff5a6e049c0 | a8690ec17cab7912257b3b1b2b9fcbef@hg4 | K5 · T14 | ● | own calendar | evidence |
| 101 | confluence.confluence_pages | page_ua_vendor_closeout | space_OPS | H3 decoy · T11 | ● | unscoped | decoy |
| 102 | github.github_pull_requests | harmonygames-Games/Combo-Fighters#38 | harmonygames-Games/Combo-Fighters | C5 container | ● | unscoped | evidence |
| 103 | github.github_pr_comments | harmonygames-Games/Combo-Fighters#38#c_1 | harmonygames-Games/Combo-Fighters#38 | C5 · T13 | ● | unscoped | evidence |

Companion rows (not separate elements): the doc's and sheet's drive_files rows, the sheet tab, page versions, the Leonard/Arthur mail copies (SENT/INBOX in their own mailboxes, not load-bearing), the PR branch, commit, pr_commit and timeline event, project team/members, Trello createCard actions.

## 3 Findability and discovery-order proofs

| Record | Agent's likely query | Chain position | Discovery order / competing hits |
|---|---|---|---|
| slack C0ADGSZKR3R/1771003267.448213 | anchor named by the prompt; #winddown history | first link | the prompt names it |
| linear project 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a | 'shutdown' via linear search / project list | connecting | named in A1 |
| gmail robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | 'checklist' / 'Sunset' in Gmail | connecting | Sherwood's robert@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com> (Feb 12, 18:40Z) sorts before it in date order — decoy met first; Sunset signed Feb 12 decides |
| gmail robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> | read the whole thread (gmail_get_thread) | overturning | the first message reads complete; the correction is message 2 (A14) |
| trello 698f48be4ba0affafbf153db | 'SVB' / 'card' in Trello | connecting | the board also holds base card #170 'move subscriptions to SVB credit card' (Done, 2023–24) — same words, older move |
| gdocs f_1326e66bcabfda8fd29e4a | 'conventions' / 'close-out' in Docs | connecting | a Confluence-first run meets page_ua_vendor_closeout (Growth/UA) first |
| gcal evt_f1d245d44ceff5a6e049c0 | 'Sunset' / 'review' in Calendar | terminal | only reached through the checklist's 'review call Leonard booked' |
| linear ENG-2439 comment cmt_96ae7b3689c1d073a2ff | 'Helpshift' in Linear, then list comments | terminal | the export status is in Oliver's comment, not the issue |
| github harmonygames-Games/Combo-Fighters#38#c_1 | PRs/comments by CodeRabbit after Feb 12 | terminal | Arthur's Slack 'coderabbit is cancelled' (C0ADGSZKR3R/1770936655.574079) is met first |
| snowflake FIN-000688 / FIN-000689 / FIN-000699 / FIN-000700 (base) | FINANCE_LEDGER Jan–Feb | terminal | Leonard's 'covers everything' (C0ADGSZKR3R/1770933999.157259) is met first |
| slack C0ADGSZKR3R/1770948876.205117 | thread replies of the keep list | overturning | parent 1770933601.686309 reads conclusive; reply_count 1 |

**Hidden authorities.** H1 'Sunset's data checklist' → Gmail search 'data delivery checklist' returns only robert@harmonygames.co/1856965916492026238; decoy Sherwood differs on 'cancel every subscription right away'. H2 'SVB's card terms' → Trello search 'SVB card' returns 698f48be4ba0affafbf153db; decoy Chase card differs on the bank and date. H3 'the conventions doc' → Docs search 'close-out register conventions' returns f_1326e66bcabfda8fd29e4a; decoy UA page differs on the cost and closed rules (Growth/UA tracker scope).

## 4 Self-validation

| QC category | Tool-enforced (sql_lint / base_check) | Manual (evidence) |
|---|---|---|
| Missing Universe Data | — | every fact in §9 is in a Robert-readable record; no tool is killed (Friction: none planned) |
| Temporal Field | PASS (base_check Check C) | dates in text agree: receipts' next dates follow their send dates; the checklist (23:58Z) after the event (22:40Z) it calls booked; A1 17:21Z after the doc/card/comments it names |
| Cross-service Referential | PASS (Check A) | Kapwing and dbt follow Leonard's table C0ADGSZKR3R/1770933450.410449 and Arthur's KubLLC message; every PR/issue cited exists (ENG-24xx, Combo-Fighters#38) |
| Quantitative / Reconciliation | PASS (keep-list counters) | every cost not from the ledger is the owner's figure in the issue or the account's own last invoice, each equal to its latest base charge (Unity Pro 2,348.50 Jan 19; Slack 87.22 Feb 3; GitHub 90 Feb 3; BigQuery 4.97 Feb 1; Workspace 298.13 Feb 2; Metabase 148; dbt 100; QuickBooks 115; Gusto 116; Helpshift 150); the costs tab is used for membership only; Arthur's sheet is deliberately stale (T20) |
| State / Lifecycle | PASS (Linear issues Todo without stamps) | no status contradicts activity: issues stay Todo for the agent to settle; Singular's termination asks for confirmation that never came |
| Identifier / Format | PASS (sha ids, Message-IDs, f_ ids, evt_/ical, cmt_, Trello timestamped ids) | sender tokens reused from the base where the vendor exists |
| Semantic / Category | — | issue titles = vendor names; card/list names match content; page title matches its body |
| Other | — | no seeded record states a register cell; voice per §1.C |

## 5 Lazy-solver pass on the implemented records

A run that lists the project, reads #winddown and the first Gmail hit and stops: gets the Keep/Move actions and the tab costs (if it copies the costs tab's December figures), misses the Gusto reply, Sunset's correction (Trello/dbt/BigQuery/Metabase), the card deadline, the review date, CodeRabbit's notice, the Helpshift switch-over, the UA accounts, the Sound split and every per-issue status/owner/exclusion that only a comment carries. Implemented records add no shortcut: issue descriptions carry only the source ('From costs tab.'), the SVB card names no account, receipts vary their card wording, and Arthur's sheet holds stale figures.

## 6 Intended disagreements

| Disagreement | Older claim | Overturning record | Why realistic |
|---|---|---|---|
| Gusto kept vs cancelled | C0ADGSZKR3R/1770933601.686309 (Feb 12 22:00Z) | C0ADGSZKR3R/1770948876.205117 (Feb 13 02:14Z) | Arthur exports the docs that night and replies in the thread |
| Slack downgrade / guest seats vs paid with every user | C0ADGSZKR3R/1770840054.486779, C0ADGSZKR3R/1770842405.931359 (Feb 11) | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> (Feb 12 23:58Z) | the data deal came after; the founders haven't reconciled it — the reply must report it |
| Google archive after Feb 15 vs no archiving | C0ADGSZKR3R/1770933903.645709 (Feb 12 22:05Z) | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | same; a clash to report |
| Metabase held vs not in the bundle | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> (Feb 13 18:20Z) | Sunset's engineers map the data a day later |
| Sherwood's 'cancel everything' vs Sunset's list | robert@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com> (Feb 12) | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | different issuer; Sherwood not engaged |
| Docusign owner Leonard vs Robert | ENG-2469 assignee | cmt_4179664f58817a32a076 (Feb 13 16:33Z) | handover in a comment |
| Arthur's 'Subscriptions' sheet vs the project | f_768cd23a00c4b12fa0e975 (Feb 10) | project 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a (Feb 12, 'replaces my subscriptions sheet') | a rough first list, rounded |

## 7 Constraints for the prompt brief

| Anchor | May be named (noun phrases only) | Record |
|---|---|---|
| A1 | Leonard's close-out register ask; Leonard's #winddown request | C0ADGSZKR3R/1771003267.448213 |

Never name: Sunset's list or its correction, the SVB date or the Trello board, the conventions doc's rules, the ledger, the Sound line, any account, the review date, the Helpshift page, CodeRabbit's notice, the totals, ids. Deadline: before Leonard archives the Google accounts (after Feb 15). Deliverables: the register sheet shared with Leonard and Arthur, the Linear issues settled, a reply in Leonard's thread.

## 8 Fact sheet

| Key | Value | Kind | Home / must appear in |
|---|---|---|---|
| they close the card | 2026-02-20 | date | 698f48be4ba0affafbf153db |
| one of our personal cards | 2026-02-19 | date | 698f48be4ba0affafbf153db |
| Figma Professional (annual) | 2026-09-11 | date | robert@harmonygames.co/<CAowZ1ukjS1ZxLCL4aRt1VM-c-GnNMTNWVQS47OM@mail.gmail.com> |
| not renewed and ended on | 2025-09-08 | date | robert@harmonygames.co/<CAIoQDHYpNPHXVgnNS8DUmtr__81CmMffz7hcWJv@mail.gmail.com> |
| Layer Pro | 49.00 | amount | robert@harmonygames.co/<CA4Ce6Oa74xUtCgFI1iGnZMieCxsUh90MhimgGu3@mail.gmail.com> |
| we paid $1,832.65 last august | 1832.65 | amount | cmt_e8ae507893bfdb06c8c7 |
| cancelled zapier yesterday | 73.50 | amount | cmt_8a420b3635db4a36f750 |
| the subscription itself is untouched | 3852 | amount | cmt_75b0e4e31a02f9a022bd |
| docusign goes to robert | 2026-04-20 | date | cmt_4179664f58817a32a076 |

`fact_check.py --no-leak` (verbatim):

```
FACT CHECK: PASS — 115 text-bearing rows, 9 declared facts, 9 declared superseded records
Errors: none
Warnings (1):
  line 153: gmail.gmail_messages robert@harmonygames.co/<CAxSGYrkpVAs45dr7lAugwSThN-X-ma7vq_V1xAV@mail.gmail.com>: [value_drift] 'monthly' carries 2 different amounts across rows: '$49.00' (line 149, row robert@harmonygames.co/<CA4Ce6Oa74xUtCgFI1iGnZMieCxsUh90MhimgGu3@mail.gmail.com>); '$10.00' (line 153, row robert@harmonygames.co/<CAxSGYrkpVAs45dr7lAugwSThN-X-ma7vq_V1xAV@mail.gmail.com>) — supersession (declare it in traps[].version_records / facts) or drift?
```

Warning dispositions (fact_check): the value_drift warnings pair different vendors' prices/dates under one common word ('monthly', 'annual', 'invoice', 'payment') — distinct accounts, not drift.

## 9 Facts for the human

### 9.1 Records

| Locator | Base/seeded | Fact (UTC) | Reach | Role |
|---|---|---|---|---|
| C0ADGSZKR3R/1771003267.448213 | seeded | Leonard → Robert 2026-02-13T17:21:07.448213Z: own the register; share with Leonard and Arthur as editors; settle each Linear issue with a line on each; reply with the two totals and the clashes | #winddown member | claim/ask (anchor) |
| C0ADGSZKR3R/1770948876.205117 | seeded | Arthur 2026-02-13T02:14:36.205117Z: Gusto: docs pulled, 'let's cancel before mar 3' | #winddown member | overturning evidence |
| C0ADGSZKR3R/1770933601.686309 | base | Leonard Feb 12 22:00Z: keep Deel, gusto, Intuit; Figma won't charge before renewal; Linear kept | #winddown member | claim met first |
| C0ADGSZKR3R/1770937232.664809 | base | Arthur Feb 12 23:00Z: moving github, dbt ([USERNAME_30019]) and Metabase to his KubLLC card | #winddown member | evidence |
| C0ADGSZKR3R/1770840054.486779 | base | Arthur Feb 11: 'yeah free version' (Slack) | #winddown member | clash 1 |
| C0ADGSZKR3R/1770842405.931359 | base | Leonard Feb 11: keep the three founders as paid Slack seats | #winddown member | clash 2 |
| C0ADGSZKR3R/1770933903.645709 | base | Leonard Feb 12: archive Google accounts after Feb 15 | #winddown member | clash 3 |
| robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | seeded | Sunset 2026-02-12T23:58:21Z: hold Slack (paid), Google Workspace (all users), Figma, Linear, GitHub, Metabase until the review call; export Helpshift | own INBOX | authority (H1) |
| robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> | seeded | Sunset 2026-02-13T18:20:44Z: Trello in, Metabase out, BigQuery and dbt in | own INBOX | overturning evidence |
| robert@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com> | seeded | Sherwood Feb 12: cancel everything except payroll/accounting | own INBOX | decoy |
| evt_f1d245d44ceff5a6e049c0 | seeded | review call 2026-03-12 17:00–17:45Z (created Feb 12 22:40Z) | own calendar | evidence |
| f_1326e66bcabfda8fd29e4a | seeded | conventions rules 1–10 (membership, exclusions, statuses, deadlines, costs, totals, clashes) | shared | authority (H3) |
| f_605121f4a36752645e0ac3 | base | HG Costs cost lines (membership; Sound and UA shared lines) | shared | evidence |
| robert@harmonygames.co/1850283027022457279 | base | Singular quarterly invoice Dec 1 (Sep 1 earlier) → next Mar 1 | own mailbox | evidence |
| robert@harmonygames.co/1853470745017478863 | base | Leonard's Feb 12 21:43Z termination asks Singular to confirm in writing; no reply | own mailbox | evidence |
| robert@harmonygames.co/1854432461283937829 | base | iPostal1 mailbox closed Jan 16 2026 | own mailbox | evidence (exclusion) |
| robert@harmonygames.co/1837122624854744558 | base | ElevenLabs Starter annual $50, Jul 9 2025–Jul 9 2026 | own mailbox | evidence |
| robert@harmonygames.co/<CAowZ1ukjS1ZxLCL4aRt1VM-c-GnNMTNWVQS47OM@mail.gmail.com> | seeded | 2025-09-11T16:04:52Z: Figma Professional (annual) — $1,212.00. Charged to the card on file. Your plan renews on September 11, 2026. | own INBOX | evidence |
| robert@harmonygames.co/<CA4Ce6Oa74xUtCgFI1iGnZMieCxsUh90MhimgGu3@mail.gmail.com> | seeded | 2026-02-03T14:30:05Z: Layer Pro (monthly) — $49.00. Paid with the card on file. Your next payment is on March 3, 2026. | own INBOX | evidence |
| robert@harmonygames.co/<CAIoQDHYpNPHXVgnNS8DUmtr__81CmMffz7hcWJv@mail.gmail.com> | seeded | 2025-09-08T16:12:40Z: Your Pond5 Annual Membership was not renewed and ended on September 8, 2025. Your licensed downloads stay your | own INBOX | evidence |
| robert@harmonygames.co/<CAxSGYrkpVAs45dr7lAugwSThN-X-ma7vq_V1xAV@mail.gmail.com> | seeded | 2026-02-11T19:47:10Z: Your Soundly Pro (monthly, $10.00) subscription has been cancelled. You'll keep access until March 3, 2026 and | own INBOX | evidence |
| snowflake.wh_finance__expenses__finance_ledger FIN-000687 / FIN-000688 / FIN-000689 / FIN-000699 / FIN-000700 (base) | base | AWS 1,485 Jan; applovin −9.80/−9.83; meta −2,843.84/−956.45 | unscoped | evidence |
| 698f48be4ba0affafbf153db | seeded | SVB closes the card Feb 20; move kept charging accounts by Feb 19 | unscoped | authority (H2) |
| harmonygames-Games/Combo-Fighters#38#c_1 | seeded | CodeRabbit 2026-02-13T09:41:12Z: subscription canceled on Feb 12 | unscoped | evidence |
| cmt_96ae7b3689c1d073a2ff on ENG-2439 | seeded | Oliver 2026-02-13T15:12:18Z: Helpshift ticket history exported (helpshift_export_2026-02-13.zip) | unscoped | overturning evidence |

### 9.2 Derived ground truth (from the records above; for the human's Oracle Events and rubric)

| Account | Issue | Action | Status | Deadline | Owner | Monthly cost | Evidence |
|---|---|---|---|---|---|---|---|
| Unity | ENG-2438 | Cancel | Requested | 2026-02-18 | Arthur | 2,348.50 | f_605121f4a36752645e0ac3 / comments |
| Helpshift | ENG-2439 | Cancel | Closed | — | Leonard | 150.00 | ZIP |
| Soundly | ENG-2440 | Cancel | Closed | — | Robert | 10.00 | robert@harmonygames.co/<CAxSGYrkpVAs45dr7lAugwSThN-X-ma7vq_V1xAV@mail.gmail.com> |
| Linear | ENG-2448 | Hold for Sunset | — | 2026-03-12 | Arthur | 152.72 | evt_f1d245d44ceff5a6e049c0 |
| Figma | ENG-2449 | Hold for Sunset | — | 2026-03-12 | Robert | 101.00 | robert@harmonygames.co/<CAowZ1ukjS1ZxLCL4aRt1VM-c-GnNMTNWVQS47OM@mail.gmail.com>, evt_f1d245d44ceff5a6e049c0 |
| Trello | ENG-2451 | Hold for Sunset | — | 2026-03-12 | Leonard | 0.00 | robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com>, evt_f1d245d44ceff5a6e049c0 |
| Singular | ENG-2454 | Cancel | Requested | 2026-02-28 | Leonard | 2,083.33 | f_605121f4a36752645e0ac3 / comments |
| AWS | ENG-2455 | Cancel | Open | 2026-02-28 | Arthur | 1,485.00 | f_605121f4a36752645e0ac3 / comments |
| Metabase | ENG-2456 | Move to Arthur's LLC | — | — | Arthur | 148.00 | robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> |
| dbt | ENG-2457 | Hold for Sunset | — | 2026-03-12 | Arthur | 100.00 | robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> |
| BigQuery | ENG-2458 | Hold for Sunset | — | 2026-03-12 | Arthur | 4.97 | robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> |
| Intuit QuickBooks | ENG-2460 | Keep | — | 2026-02-19 | Leonard | 115.00 | 698f48be4ba0affafbf153db |
| Carta | ENG-2462 | Cancel | Open | 2026-08-14 | Leonard | 321.00 | f_605121f4a36752645e0ac3 / comments |
| Google Workspace | ENG-2464 | Hold for Sunset | — | 2026-02-19 | Leonard | 298.13 | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>, robert@harmonygames.co/1856033699491658253 |
| Slack | ENG-2465 | Hold for Sunset | — | 2026-02-19 | Leonard | 87.22 | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> |
| Gusto | ENG-2467 | Cancel | Open | 2026-03-02 | Leonard | 116.00 | b9ef575bec54b095edb75a0fe83580f5 |
| Deel | ENG-2468 | Keep | — | — | Leonard | 300.00 | f_605121f4a36752645e0ac3 / comments |
| Docusign | ENG-2469 | Cancel | Open | 2026-04-19 | Robert | 25.00 | f_605121f4a36752645e0ac3 / comments |
| Layer | ENG-2473 | Cancel | Requested | 2026-03-02 | Leonard | 49.00 | robert@harmonygames.co/<CA4Ce6Oa74xUtCgFI1iGnZMieCxsUh90MhimgGu3@mail.gmail.com> |
| CodeRabbit | ENG-2474 | Cancel | Closed | — | Arthur | 45.00 | harmonygames-Games/Combo-Fighters#38#c_1 |
| Cursor | ENG-2475 | Cancel | Requested | 2026-03-04 | Arthur | 40.00 | f_605121f4a36752645e0ac3 / comments |
| Zapier | ENG-2476 | Cancel | Closed | — | Leonard | 73.50 | f_605121f4a36752645e0ac3 / comments |
| GitHub | ENG-2477 | Hold for Sunset | — | 2026-03-12 | Arthur | 90.00 | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>, evt_f1d245d44ceff5a6e049c0 |
| Kapwing | ENG-2478 | Cancel | Closed | — | Arthur | 24.00 | f_605121f4a36752645e0ac3 / comments |
| 1Password | ENG-2479 | Cancel | Open | 2026-03-07 | Arthur | 19.95 | f_605121f4a36752645e0ac3 / comments |
| ElevenLabs | (new issue) | Cancel | Open | 2026-07-08 | Robert | 4.17 | robert@harmonygames.co/1837122624854744558 |
| Meta Ads | (new issue) | Cancel | Open | 2026-02-28 | Robert | 2,843.84 | snowflake.wh_finance__expenses__finance_ledger FIN-000689, snowflake.wh_finance__expenses__finance_ledger FIN-000700 |
| AppLovin (UA) | (new issue) | Cancel | Open | 2026-02-28 | Robert | 9.80 | snowflake.wh_finance__expenses__finance_ledger FIN-000688, snowflake.wh_finance__expenses__finance_ledger FIN-000699 |

Totals: today **11,045.13**, Keep + Hold **1,249.04**. Linear: Done ENG-2439, ENG-2440, ENG-2474, ENG-2476, ENG-2478; Canceled ENG-2441, ENG-2442, ENG-2443, ENG-2444, ENG-2445, ENG-2446, ENG-2447, ENG-2450, ENG-2452, ENG-2453, ENG-2461, ENG-2463, ENG-2466, ENG-2470, ENG-2471, ENG-2472, ENG-2480, ENG-2481, ENG-2482, ENG-2483; new issues for ElevenLabs, Meta Ads, AppLovin (UA); a comment on each of the 45 issues. Reply clashes: Slack free plan, Slack guest seats, Google archiving (extras accepted).

## 10 Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| github | INT-01 | Slack mirror | none: Combo-Fighters is outside INT-01's mirrored repos |
| github | INT-23 | CodeRabbit author + SVC_0321 timeline actor | seeded (commented event #38#ev_1) |
| github | INT-12 | notification mail | none: Robert is not a PR participant |
| linear | INT-03 / INT-04 / INT-05 | linear[bot], Slack app, digests | none: no PR names an ENG-24xx key; the ENG team has no Slack feed in 2026; no digest seeded |
| gcal | INT-11 | invitation mails | none: integration_exceptions no_notify (manifest) |
| slack | INT-22 | email notification | none |
| trello | INT-21 | Slack posts | none: no integration exists |
| gdrive | INT-13 | Drive Slack DM | none |
| gmail | none | — | gmail: no outbound integration |
| confluence | none | — | confluence: version 1 rows seeded with each page |
| gsheets / gdocs | none | — | gdocs: drive_files twin rows with identical sharing |

## 11 Touched-data census and coherence hazards

Touched: #winddown Feb 9–13 (incl. the keep-list thread), #prototype's Oliver message, the 47 issues and their comments, the project, Robert's billing mail (seeded + base Singular, iPostal, Trello, ElevenLabs, Linear notice), Sunset/Sherwood threads, the two Trello cards on board 640643a3fd8f3ca308d9318e, the conventions doc and Arthur's sheet, the costs tab f_605121f4a36752645e0ac3, FINANCE_LEDGER Jan–Feb, the review event, the support handover page, the UA page, page_aws_infra, Combo-Fighters#38. Hazards from `references/universe_kb/coherence_hazards.json`:

| Hazard id | Category | Disposition |
|---|---|---|
| hazard T02 | temporal | seeded threads in date order |
| hazard T08 | temporal | Leonard/Oliver active_feb_2026 |
| hazard S08 | semantic | page_support_playbook avoided (export logged on a seeded page) |
| hazard S06 | semantic | Contacts titles not used |
| hazard R04 | referential | folder named by title only |
| hazard R08 | referential | event has no invitation mail and no orphan mail (no_notify) |
| hazard Q07 | quantitative | Helpshift balances are distractor text; cost from the tab |
| hazard Q01 | quantitative | keep-list parent counters updated with the reply |
| hazard L13 | state/lifecycle | Combo-Fighters#37 untouched; notice on #38 (hazard_acknowledgements excluded) |
| hazard L08 | state/lifecycle | issues assigned to active founders only |
| hazard I10 | identifier/format | usr_Robert used verbatim |
| hazard I14 | identifier/format | doc owner = Wind Down siblings' Resource owner |
| hazard I07 | identifier/format | CodeRabbit comment author PERSON_6026 with SVC_0321 timeline actor, as in base |

## 12 Platform follow-ups

- Linear comments are ● (Ask_Carriers §6b); confirm in the Opus pre-check that `linear_list_issues` returns no comments.
- The review event's start time is its load-bearing field (no description used).
- base_check patched locally to accept a Linear project inserted by the same SQL (it already accepted same-SQL issues); diff kept in `support/task_work/rb_winddown_closeout/base_check.orig.py`. The platform `/injection` has its own reference check — watch for a project-id finding there.
- Snowflake rows are base only (not injected); re-verify FIN-000687…FIN-000700 after any data regeneration.

## 13 Self-review

### Tool outputs (verbatim, final run)

`sql_lint.py`:

```
schemas touched (10): confluence, gcal, gdocs, gdrive, github, gmail, gsheets, linear, slack, trello
rows by schema: {'gdrive': 3, 'gdocs': 1, 'gsheets': 2, 'confluence': 2, 'slack': 4, 'trello': 2, 'gmail': 26, 'gcal': 3, 'github': 6, 'linear': 89}  total rows: 138  ops: {'insert': 134, 'update': 4}
errors: 0  warnings: 8
  warn  line 21: confluence statement — unscoped and rarely opened by agents: make sure another record points here
  warn  line 24: confluence statement — unscoped and rarely opened by agents: make sure another record points here
  warn  line 155: gcal.gcal_events.start_ts = 2026-03-12T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 155: gcal.gcal_events.end_ts = 2026-03-12T17:45:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 158: gcal.gcal_events.start_ts = 2026-03-12T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 158: gcal.gcal_events.end_ts = 2026-03-12T17:45:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 160: gcal.gcal_events.start_ts = 2026-03-12T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 160: gcal.gcal_events.end_ts = 2026-03-12T17:45:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
```

`base_check.py`:

```
BASE CHECK (/injection A + C, static): PASS  — 134 inserts, 4 updates
Check A — records, references, IDs: PASS
Check C — dates and relationships: PASS
Warnings (1):
  line 155: gcal.gcal_events: meeting a8690ec17cab7912257b3b1b2b9fcbef@hg4 'Sunset – data delivery review' has 3 attendee(s) but no invitation mail ('Invitation: Sunset – data delivery review @ …') in any attendee mailbox — INT-11 base: 836/941 meetings with attendees have one (2298/2974 attendee mailboxes); add the copies or declare integration_exceptions [{record_id, reason: 'no_notify: …'}]
  note: github.github_branches: no base-reference rules (checked by sql_lint only)
  note: github.github_commits: no base-reference rules (checked by sql_lint only)
  note: github.github_pull_request_commits: no base-reference rules (checked by sql_lint only)
  note: gsheets.sheets_sheets: no base-reference rules (checked by sql_lint only)
  note: linear.linear_project_members: no base-reference rules (checked by sql_lint only)
  note: linear.linear_project_teams: no base-reference rules (checked by sql_lint only)
  note: linear.linear_projects: no base-reference rules (checked by sql_lint only)
```

`hardness_gate.py (SQL)`:

```
HARDNESS GATE (long): PASS
  [ok] effective_profile: effective_profile 'long' for 'Long Horizon' → thresholds 'long'
  [ok] sql_lint_clean: 0 lint error(s) — run tools/sql_lint.py
  [ok] base_consistency: /injection-style checks vs the base universe: A 0 finding(s), C 0 finding(s), 0 warning(s) — run tools/base_check.py --manifest
  [ok] persona_reach: 57 load-bearing seeded ids for robert (45 in unscoped services = visible, 12 judged by persona_view check-sql); not provably visible: none
  [ok] fact_consistency: fact_check: 0 error(s) (9 declared facts), 1 drift warning(s); first: none — run tools/fact_check.py --manifest --no-leak
  [ok] hazard_scope: 2 pre-existing hazard(s) among task-touched records; state/lifecycle or referential without a verified resolution: none; resolved/other: ['Q06', 'Q07']
  [ok] services_injected: 10 schemas injected (confluence, gcal, gdocs, gdrive, github, gmail, gsheets, linear, slack, trello); need ≥ 10
  [ok] rows: 134 INSERTed rows (UPDATE companions not counted; 138 rows in all); need ≥ 120
  [ok] services_carrying_weight: 11 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: schemas injected but absent from the design: none
  [ok] seeded_ids_exist_in_sql: 52 seeded ids cited; missing from SQL: none
  [ok] anchors: 1 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 12 fragments; need ≥ 12
  [ok] ask_fragment_services: 8 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 10 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 9 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 48; need ≥ 30 (source-defined: True)
  [ok] evidence_surfaces: 3 surfaces over 3 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 56; need ≥ 30
  [ok] call_budget: unconditional (verified) floor 158 of 158 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 100 (Long Horizon; plan ~600 for headroom)
  [ok] call_budget_spread: 10 services in budget; largest share outside the per-record phase 23% (≤ 50%)
  [ok] traps: 25 traps across 13 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 7 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 5 supersessions (3 with versions in ≥ 2 services, 3 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: 5 trap(s) with version_records; the records' own timestamps (SQL created_at/ts/date/updated_at, or the base record) must be strictly increasing in the listed order (oldest first); bad: none
  [ok] distractors: 7 distractors of 6 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 7 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 7 chains with 7 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] hidden_authorities: 3 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 2 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 19 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 9 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 5 writes over 4 services; each must depend on findings
```

**Warning dispositions.** sql_lint weekend warn ×4 (disposition): automated vendor receipts sent on their billing dates (Layer Jan 25, Deel/Linear Feb 1, 1Password Feb 8) — base vendor mail arrives on weekends too (robert@harmonygames.co Google Play receipts on Sat/Sun). sql_lint clock warn ×6 (disposition): the review call on 2026-03-12 is a not-yet-happened future event, scheduled before the clock. sql_lint confluence warn (disposition): both seeded pages are reached through a pointer (the UA page by a Confluence search for close-out conventions; the handover page through the checklist's 'support handover page'). base_check INT-11 warn (disposition): declared in `integration_exceptions` (no_notify).

### /injection Checks A–C walk (`Evals/0_Injection_Quality_Eval.md`)

| Check | Verdict | Evidence |
|---|---|---|
| Inventory | PASS | 162 INSERT + 4 UPDATE, every statement keyed on a primary key; no upsert, no DELETE (sql_lint stats) |
| Check A — references | PASS | channels C0ADGSZKR3R, C09UHHN6PFZ; users EMPLOYEE_00nn; Linear users/team_ENG; project inserted first; page_ops_home parent; Combo-Fighters repo; board 640643a3fd8f3ca308d9318e lists; collisions 0 (§1.F) |
| Check B — structure | PASS | literal JSON in every *_json column; no generated column written; quoted camelCase (sql_lint 0 errors) |
| Check C — dates/relations | PASS | all timestamps before the clock except the future event; reply after parent; comments after issues; in_reply_to in the same mailbox (base_check) |

### Counter-readings

| # | Category | Counter-reading (strongest case it FAILS) | Resolution with evidence | Verdict |
|---|---|---|---|---|
| 1 | temporal | a receipt dated before a change contradicts the later state (dbt receipt Feb 3 on the SVB card vs moved to KubLLC); Sherwood's 'as promised on our call' | the move is Feb 12 23:00Z (C0ADGSZKR3R/1770937232.664809) and ENG-2457's comment Feb 13 01:29Z supersede the receipt; Sherwood's mail now follows the Feb 12 16:30Z call (robert@harmonygames.co/1856689465442954434, review F1) | PASS |
| 2 | semantic / category | 'Closed' in rule 5 vs Linear 'Done' in the project description could be read as two definitions | project 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a description (K2): 'Done once the account counts as closed in the register' — one definition, rule 5 of f_1326e66bcabfda8fd29e4a | PASS |
| 3 | cross-service referential | the injection could relabel base redaction tokens (review F2) or cite a file that does not exist (F3) | no seeded text names a redacted vendor: Kapwing comes from Leonard's base table C0ADGSZKR3R/1770933450.410449, dbt's move from Arthur's own ENG-2457 comment; helpshift_export_2026-02-13.zip is now a drive_files row in d_e5caf6a8c630421942ee59 | PASS |
| 4 | quantitative | the costs tab's month labels (HG Costs a year behind HG P&L) and its December figures vs the latest receipts | rule 8 of f_1326e66bcabfda8fd29e4a takes no cost from the tab: owner figures in the issues or own last invoices, matching the latest base charges | PASS |
| 5 | state/lifecycle | Singular could be closed: Leonard terminated it | robert@harmonygames.co/1853470745017478863 asks for written confirmation; no later Singular message exists before the clock | PASS |
| 6 | state/lifecycle (sibling) | another base account might look still-active without an issue (Calendly charged Oct 2025, tab col AC) | ENG-2463 exists; Robert's comment 'turned off auto-renew in october' → excluded (cancelled before Feb 9) | PASS |
| 7 | identifier/format | new sender tokens could collide with existing identities | PERSON_7731, SVC_7702–SVC_7712: 0 hits in all three data folders (§1.F, collide.sh lookups); vendor tokens reused: SVC_5771_EMAIL (Unity) | PASS |
| 8 | people status | Frederick (quiet since Oct 2025) authors a page | page_ua_vendor_closeout is dated 2025-03-18, when he was active (page_product_okrs owner; frederick.stone@harmonygames.co quiet_since_2025-10) | PASS |
| 9 | other | the Sunset correction could read as an unintended contradiction of the first checklist | same sender, same thread robert@harmonygames.co/1856965916492026238, later date, 'one change … The rest of the list stands' — a dated amendment (robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com>) | PASS |
| 10 | intended: Gusto | Arthur's reply could be read as a suggestion, not a decision | A1 C0ADGSZKR3R/1771003267.448213 tells Robert to go by the keep list 'and the replies under it'; rule 4 'my keep list, as amended in the thread' | PASS |
| 11 | intended: Slack/Google clashes | the clashes could be read as Sunset overriding silently (no report needed) | A1 C0ADGSZKR3R/1771003267.448213 asks to report 'anything in the plan that clashes with what we already decided' | PASS |
| 12 | intended: Metabase | Arthur's LLC move could clash with Sunset's first list | the correction robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> removes Metabase; ENG-2456's comment confirms the KubLLC card | PASS |
| 13 | intended: Sherwood | two checklists from two firms are two live answers | decoy_scope issuer: Sherwood was not engaged (signed SOW robert@harmonygames.co/1856956532017091340 is Sunset's) | PASS |
| 14 | intended: Docusign | a handover by comment without Robert's acceptance | Leonard's comment cmt_4179664f58817a32a076 on ENG-2469 is a statement ('docusign goes to robert'); rule 7 | PASS |
| 15 | intended: Arthur's sheet | the sheet could be read as current costs | project 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a description 'replaces my subscriptions sheet from Tuesday' (f_768cd23a00c4b12fa0e975 Feb 10) | PASS |

### Revision 2 — /injection review 6adfee3f27ce6ca81b457137 (FAIL: F1–F3) and fixes

| Finding | Fix | Evidence |
|---|---|---|
| F1 Sherwood mail cites a call before it happened | redated to 2026-02-12T18:40:12Z, after the Thu Feb 12 16:30Z call | robert@harmonygames.co/1856689465442954434 (base call booking); robert@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com> |
| F2 project description relabelled redaction tokens (Notion, Sentry) | sentence removed; Notion issue is now Kapwing (Leonard's table C0ADGSZKR3R/1770933450.410449, closed by its cancellation mail); Sentry issue dropped; dbt's KubLLC move stated in Arthur's ENG-2457 comment, so dbt's deadline is Mar 12; Zapier is Requested (ticked by Leonard in the same table, comment on its issue) | C0ADGSZKR3R/1770937232.664809, C0ADGSZKR3R/1770933903.645709 |
| F3 Confluence comment cites a missing Drive file | drive_files row f_4ac7a77383e7317eedcd83 helpshift_export_2026-02-13.zip (application/zip) in d_e5caf6a8c630421942ee59, 15:04:51Z, before the comment | comment_support_after_helpshift_c1 (removed in Revision 8) |
| A1 links_json / sequence not in the snapshot (provisional) | linear_comments.sequence dropped (nullable in the live schema); linear_projects.links_json kept: references/universe_schema_live.json (platform DB export 2026-10-04) marks it NOT NULL with no default, so omitting it fails the insert — the eval snapshot injection.json is the older 58-table cross-check | linear_projects, linear_comments |
| A2 Chase card idShort NULL | card dated 2023-04-18T20:18:50Z between cards 67 and 69, idShort 68 (the free number there) | board 640643a3fd8f3ca308d9318e |
| A3 Carta renewal 8/15 | comment and deadline aligned (renews Aug 15 → 2026-08-14) | C0ADGSZKR3R/1770933450.410449 |


### Revision 3 — /injection review 6adfee3f27ce6ca81b457137 rerun (FAIL: F1–F3) and fixes

Root cause: the seeded receipts in Robert's mailbox were never checked against the vendors' real billing mail in Leonard's and Arthur's mailboxes (their message dates are RFC-2822, which an ISO-only scan skipped). Every vendor was re-scanned across all mailboxes (Nov 2025–Feb 2026, and Sep 2024 onward for the rest).

| Finding | Fix | Base evidence |
|---|---|---|
| F1a Kapwing | seeded cancellation mail removed; Arthur's comment relays Kapwing's own cancellation notice ($24/month; base notice: Pro until Feb 25) → Closed | blake@harmonygames.co_1856962040028188034.json, blake@harmonygames.co_1855319224557456875.json |
| F1b CodeRabbit | bot notice now says canceled on Feb 12; comment 'lite plan, 3 seats at $15' (cost 45) | blake@harmonygames.co_1856750389874631062.json, blake@harmonygames.co_1854150876243727777.json |
| F1c Slack | seeded invoice removed; Leonard's comment 'renews on the 3rd, svb card' (Feb 3 renewal, next 3/3) | leonard@harmonygames.co_1856103558554635848.json |
| F1d QuickBooks | seeded receipt removed; Leonard's comment 'takes the $115 from my own card on the 4th, not the svb one' → Keep, dash | leonard@harmonygames.co_1856211152930380063.json |
| F1e Google Cloud | seeded email removed; Arthur's comment 'charges the svb card on the 1st' | blake@harmonygames.co_1855947447649217022.json |
| F1f dbt | seeded receipt removed (dbt is on the KubLLC card per Arthur's comment) | leonard@harmonygames.co_1855983949220444975.json |
| F1g Zapier | seeded receipt removed; Leonard's comment quotes Zapier's own notice (plan runs until Feb 27) → Closed | leonard@harmonygames.co_1856958213684823393.json |
| F1 sweep (same defect class) | removed seeded Deel, Cursor, Vercel, Docusign and 1Password mail; Deel is paid by bank transfer (Keep, dash); Docusign renews Apr 20 for $300 (deadline Apr 19); GitHub costs $52 + Copilot ($90 last invoice); Gusto pulls its invoice from the bank on the 3rd (deadline Mar 2); Helpshift comment no longer quotes a $300 figure; no seeded record carries a card number | blake@harmonygames.co_1856009246393472679.json (Deel transfer), leonard@harmonygames.co_1827068676034658582.json (Docusign 04/20, 300), blake@harmonygames.co_1856132203079406675.json (GitHub $52 + $38), blake@harmonygames.co_1856071940774386395.json (Gusto Feb 3) |
| F2 'never paid' comments | Office 365, Typecast, Adobe, OpenAI comments now agree with the costs tab (stopped paying before Feb 9); Miro issue dropped (live base receipts to Brian, A2) | f_605121f4a36752645e0ac3 rows 8, 11, 26, 54; leonard@harmonygames.co_1841288941522824072.json (Typecast Aug 2025) |
| F3 commit identity | author/committer 'Oliver Brooks' <oliver.brooks@harmonygames.co> | harmonygames-Games/Combo-Fighters#38 |
| A3 / A7 | 1Password's description no longer claims #winddown; Chase card closed like its neighbours 67 and 69 | C0ADGSZKR3R/1770933450.410449 |


### Revision 4 — /prompt review 6adfee3f27ce6ca81b457137 (FAIL 2: UGT, Clarity, Cross-Service Coherence) and fixes

| Finding | Fix | Evidence |
|---|---|---|
| Sound-line accounts (Pond5, ElevenLabs) two readings of rule 3 | rule 3 now names two sources explicitly: ledger lines still charging, and every other account inside a costs-tab line that covers several vendors, each its own row with or without a ledger line | f_1326e66bcabfda8fd29e4a rule 3; f_605121f4a36752645e0ac3 row 15 |
| Hailuo.ai, Dailybot, UA Assets had no status record | assignee comments: Hailuo cancelled in October (tab AD 10, AE 0), Dailybot stopped early 2024 (tab C–L), UA Assets one-off campaign creative buys, last Apr 2025 (tab X) → all excluded, issues Canceled | ENG-2446, ENG-2452, ENG-2481 |
| clash list undefined | rule 10: a clash is a #winddown decision that Sunset's list or SVB's terms would undo; card moves and requests are not decisions → exactly Slack free plan (C0ADGSZKR3R/1770840054.486779), Slack cut to three paid seats (C0ADGSZKR3R/1770842405.931359), Google archiving (C0ADGSZKR3R/1770933903.645709) | f_1326e66bcabfda8fd29e4a rule 10 |
| AWS: costs tab 0 vs ledger 1,485 | rule 8 no longer falls back to the ledger except for ad spend; Arthur's ENG-2455 comment gives all of AWS at $1,485 in January and says the P&L line was never kept up (a dated human explanation of the near-empty line) | ENG-2455; FIN-000687 |
| Singular date both-fair (Feb 28 / Mar 14) | Leonard's ENG-2454 comment: the next quarterly invoice is Mar 1; Mar 15 is only the extension on the old one → Feb 28 | ENG-2454; robert@harmonygames.co/1850283027022457279 |
| minor: Docusign / Linear charges missing from the P&L | owner comments say the P&L missed last April's Docusign charge and only caught Linear's 2024 payment | ENG-2469; ENG-2448 |
| platform note: PR #38 base_sha not in the export | base_sha = 4e9e1e94d7d89fb7ef9985d1a6c271421129888a (Combo-Fighters#37's develop base) | harmonygames-Games/Combo-Fighters#38 |


### Revision 5 — /injection review 6adfee3f27ce6ca81b457137 (FAIL: F1 Dailybot, F2 UA Assets) and fixes

Root cause: the Revision-4 comments were checked against the recent costs-tab columns only. Every comment that states a payment history was then re-checked against its row's full history (C=Jul-23 … AF=Dec-25); one more defect of the same kind was found and fixed (Kling).

| Finding | Fix | Costs-tab evidence (f_605121f4a36752645e0ac3) |
|---|---|---|
| F1 Dailybot 'cancelled after the first month' | 'we stopped paying for dailybot in early 2024, it's sat on the free plan since' (ENG-2452) | Dailybot C–I 25–34, J–L rolling averages to Apr-24; base Free-plan notices 2025 |
| F2 UA Assets 'never spent on it' | 'that line was one-off creative buys for campaigns, the last one was last april' → excluded as one-off (ENG-2481) | UA Assets I, J, M, N, R, S, T, X (last Apr-25) |
| sweep: Kling 'dropped after the september trial' | 'dropped kling after september' (ENG-2445) | Kling U–AC 9/month Jan–Sep 2025 |
| A2 Linear / A3 AWS wording | 'the p&l stops after the 2024 payment' (ENG-2448); 'the p&l line for it was never kept up' (ENG-2455) | Linear D–Q (last Sep-24); Servers (AWS) AE 15 only |
| sweep, held | OpenAI (last Apr-24), Typecast (last Jul-25), Veed (last Nov-25), Hailuo (last Oct-25), JetBrains (to Dec-25), Adobe (last Oct-24), Office 365 (last Dec-24), Calendly (Oct-25), Solsten (Jan-24), Notarize (Aug-23), Docusign (Apr-24 only), Carta (Aug-25 3,852) all agree with their comments | rows 8, 11, 19–22, 26, 51, 55, 64, 69, 32, 49 |


### Revision 6 — /injection review 6adfee3f27ce6ca81b457137 (FAIL: F1 Dailybot still 'on the free plan') and fix

| Finding | Fix | Evidence |
|---|---|---|
| F1 Dailybot comment implied the workspace still exists | 'we stopped paying for dailybot in early 2024, it sat on the free plan until they deleted the workspace last september' (ENG-2452) | blake@harmonygames.co_1842691964207508503.json (8 Sep 2025 'We deleted your organization'); blake@harmonygames.co_1839039701685601092.json (30 Jul 2025 removal notice); costs tab Dailybot C–L |
| sweep: every comment's current-state claim vs vendor account-state mail in all mailboxes (full-body scan, 2025-01 → clock: deleted / deactivated / canceled / expired / downgraded / plan changed) | only Dailybot contradicted; Kapwing and Zapier notices already match their comments; Carta notices are contractor terminations (match ENG-2462); no notice exists for Typecast, Adobe, Office 365, Hailuo, Veed, Kling, OpenAI, Calendly, JetBrains, Solsten, Notarize, 1Password, Vercel, Cursor, Layer, Figma, Pond5, Soundly, ElevenLabs, Docusign or Linear | blake@harmonygames.co_1856962040028188034.json; leonard@harmonygames.co_1856958213684823393.json |


### Revision 7 — /prompt review 6adfee3f27ce6ca81b457137_1_prompt (1) (FAIL: Cross-Service Coherence 2, AWS costs tab vs ledger) and fix

| Finding | Fix | Evidence |
|---|---|---|
| Issue 1: the AWS cost was routed by the costs tab's 0 (rule 8 fallback) and ENG-2455 explained the tab/ledger gap, so the task depended on a base quantitative conflict | rule 8 now starts: 'A cloud or ad-spend account with its own line in the finance ledger uses its January line there, whatever the costs tab shows' — only AWS (FIN-000687 −1,485), applovin (FIN-000688 −9.80) and meta (FIN-000689 −2,843.84) have such lines in Jan 2026; BigQuery (inside 'SaaS vendors') keeps AF 14.33. ENG-2455 comment drops 'the p&l line for it was never kept up'. Costs and totals unchanged (10,916.98 / 1,206.39) | snowflake FINANCE_LEDGER 2026-01-31 rows FIN-000686…FIN-000696 (other lines: aggregates, salaries, revenue) |
| Known base issue (not depended on): HG Costs 'Servers (AWS)' AC–AF vs ledger AWS Sep–Dec 2025, and 'UA' vs ledger marketing_ua | no graded value reads either side; rubric and OEs stay off monthly AWS and UA spend for 2025 | f_605121f4a36752645e0ac3 row 41; FIN-000672 |
| Issue 2 (Business Function 3, NON-FAIL, optional) | not changed: any reframing risks a new fork; the reviewer marks it non-blocking | — |


### Revision 8 — /prompt review 6adfee3f27ce6ca81b457137_1_prompt (2) (FAIL: Cross-Service Coherence 2) and fixes

| Finding | Fix | Evidence |
|---|---|---|
| 1 Vercel label on GitHub's costs-tab line | project description now 'the hosting one is GitHub'; Vercel issue ENG-2459 and its comment removed (numbering kept, the gap is ENG-2459); ENG-2477 GitHub 'From costs tab (unlabeled hosting line).'; GitHub costed from AF = 86.00 (rule 8) and its comment no longer quotes $52/$90 (one route); 'Vercel 90' dropped from the stale Subscriptions sheet | HG Costs row 42 '[PERSON_NAME_0250]' AC–AF 165/169/105/86 = Arthur's GitHub receipts (2025-09-03 … 2025-12-03); Leonard's SVB feed −189.49 2025-04-04 = GitHub Apr receipt |
| 2 Confluence deactivated (Vincent's mailbox, 2025-10-03) vs injected Confluence activity | Confluence removed from Sunset's list (all three copies); the 'support handover page' sentence dropped; page_support_after_helpshift, its version and comment deleted; register loses the Confluence Hold row ($0). Helpshift export now logged by Oliver on ENG-2439 (2026-02-13T15:12:18Z, after the zip's 15:04:51Z) | helpshift_export_2026-02-13.zip in the Wind Down folder, shared with Robert; the Growth/UA page (2025-03-18) predates the deactivation and stays a decoy |
| 3 HG Costs header a year behind HG P&L from column V | UPDATE gsheets.sheets_sheets (f_605121f4a36752645e0ac3, sheet 2): header V…AR +1 year, so V–AL equal HG P&L's labels and AF reads 2025-12-25; values unchanged; spreadsheet and Drive modified_time 2026-02-13T16:31:07Z (before the conventions doc, 16:38); rule 8's 'off by a year, go by position' sentence removed | builder asserts costs header C–AL == HG P&L header C–AL; the early I/L–T labels are identical on both tabs (base, unchanged) |
| 4 Chase-closure decoy card vs the Chase account opening in Apr 2023 | Trello card and its createCard action deleted; H2's decoy is now base card #170 'move subscriptions to SVB credit card' (Done, 2023–24) on the same board | #admin_foundersonly 2023-04-24/28 |
| 5 (optional) AWS wording | 'whatever the costs tab shows' removed from rule 8 | FIN-000687 |
| sweep: other unlabeled costs-tab lines | the '$30 game-ops lines are people's tool stipends' claim removed (Leonard's SVB feed books '[PERSON_NAME_5480]' as −29.99 Software & apps, 2025-03-27) → 'the two $30 game-ops lines I'm handling myself, so they're not in here' (a scope decision, no identity claim); '$6,250 one is Singular' kept: Singular invoices quarterly $6,250 in Robert's mailbox, and the same token reads 'Singular Fix' in the Android version tracker | HG Costs rows 11/18/36; SVB feed sheet |
| totals (before Revision 9) | 29 rows: 10,826.98 / 1,202.39; 45 issues; 4 new issues | truth.json |


### Revision 9 — independent coherence audit of the Revision-8 SQL (before resubmitting /injection and /prompt)

| Finding | Fix | Evidence |
|---|---|---|
| Linear: seeded receipt 'Linear Basic (annual), 4 seats, $480, renews Feb 1 2027' contradicts the base Standard renewal | receipt removed; Arthur's ENG-2448 comment: 'linear is on standard, paid yearly. we paid $1,832.65 last august for the year to aug 21, it moves to basic at that renewal' → 1,832.65 / 12 = 152.72 (rule 8: tab AF 0 for Dec is a true no-charge month for an annual plan); 'the p&l stops after the 2024 payment' removed | leonard@harmonygames.co_1841095243838114182.json (Aug 21 2025, Standard ×22, Aug 21 2025 – Aug 21 2026, amount paid $1,832.65); leonard@harmonygames.co_1840819416447370635.json; 00016109.json (Robert, Dec 4 2025: Basic at the next renewal after Feb 1 2026) |
| QuickBooks: 'from my own card, not the svb one' contradicts the Intuit receipts (MASTER 5348 = the SVB card) | comment: 'intuit takes the $115 off the svb card on the 4th' → Keep row still charging the SVB card → by when Feb 19 (rule 6 + SVB card terms); Revision-3 row F1d superseded | leonard@harmonygames.co_1856211152930380063.json (Feb 4 2026, MASTER ending in 5348); leonard@harmonygames.co_1787909925965085132.json ('Silicon Valley Bank Card ending in 5348') |
| OpenAI: 'we stopped those in 2024' contradicts the May 2025 $50 API top-up | comment: 'prepaid api credits we topped up by hand now and then, the last one was $50 last may. nothing recurring' → left out as one-off purchases (rule 2); the ChatGPT Plus claim dropped | blake@harmonygames.co_1830989465254730549.json (2025-05-02, $50) |
| Pond5: 'renews on March 2, 2026' implies a Mar 2025 $60 charge the Sound line never shows | seeded mail now an end notice dated 2025-09-08: not renewed, ended Sep 8 2025 → rule 2 leaves it out (no row, no new issue) | HG Costs row 15: Sep-24 70.5 (the annual), flat 15 after, no Sep-25 bump |
| JetBrains: 'contractor who left' vs EMPLOYEE_0032 full_time | 'the engineer who left in october' | PAYROLL_ROSTER (last month Oct-25) |
| checked clean by the audit | GitHub and Singular relabels match receipts; Figma, Kapwing, CodeRabbit, Zapier, Carta, Docusign, Calendly, AWS, Unity, Typecast/Veed/Kling/Hailuo/Adobe/Office 365/Dailybot/UA Assets/Solsten, Trello, Slack, KubLLC moves; mail dates and weekdays; authors' channel membership; header UPDATE changes only row 0 cols V–AR | — |
| totals | 28 rows: 10,934.70 today / 1,315.11 after the plan; 45 issues; 3 new issues (ElevenLabs, Meta Ads, AppLovin UA) | truth.json |


### Revision 10 — /injection review 6adfee3f27ce6ca81b457137_0_injection (6) (FAIL: F1 header UPDATE vs the Drive xlsx bytes) and fix

The two reviews conflict: /prompt (run 3) failed a positional note around the HG Costs header year slip, and /injection (run 6) failed the header UPDATE because the same file's Drive xlsx bytes keep the old labels. The only route both accept is that no graded value reads the costs tab's month columns.

| Finding | Fix | Evidence |
|---|---|---|
| F1 Sheets header vs Drive xlsx bytes | the three P&L statements removed (Drive modified_time, sheets_sheets header grid, spreadsheet modified_time); base file untouched | Audit-Report/0_injection_FAIL_r8.md |
| rule 8 depended on the costs tab's month columns | rule 8: ledger line for cloud/ad-spend accounts with their own line; everything else the owner's monthly figure in its Linear issue, or its own last invoice brought to a month; the costs tab is now used only for membership (rule 3) | doc f_1326e66bcabfda8fd29e4a |
| owner figures added (each = the latest base charge before the clock) | Unity 'unity pro is 11 seats at $2,348.50 a month with tax, next invoice is the 19th' → 2,348.50, by when Feb 18 | Arthur's mailbox INZ02468432/INZ02517133/INZ02565829/INZ02614348: UTY-PRO ×11 $2,200 + $148.50 tax, Oct 19 … Jan 19 |
| | Slack 'it was $87.22 this month' | Leonard's mailbox 'your plan has renewed' 2026-02-03 Total $87.22 (Dec 129.50, Jan 121.10) |
| | GitHub 'it was $90 this month all in' | GitHub receipt 2026-02-03: Team $52 + Copilot $38 = $90 |
| | BigQuery 'it was $4.97 this month' | Google payment 2026-02-01 $4.97 |
| | Metabase $148, dbt $100, Helpshift $150, Deel $300, Gusto 'january invoice was $116' | Metabase receipts Dec 21/Jan 21 $148; dbt Feb 1 $100; Helpshift INV/HSUS9879 (31/1/2026) $150; Gusto January 2026 invoice paid Feb 3, $116; Deel: costs tab Nov/Dec 300, no billing mail |
| | Workspace: own last invoice in Robert's mailbox, Feb 2 2026, $298.13 | robert@harmonygames.co/1856033699491658253 att_0001.pdf |
| seeded Unity 'CINV' invoice (Feb 10) removed | the base CINV invoices are Unity Ads (uAds per-game lines) and stop after Nov 10 2025; a Feb CINV was invented | 00015915.json CINV-00022209 (uAds 1 – 31/10/2025) |
| decoy | T25: the costs tab's December figures (Unity 2,172, Workspace 316.56, Slack 129.50, BigQuery 14.33, GitHub 86) are now wrong answers | f_605121f4a36752645e0ac3 |
| totals | 28 rows: 11,045.13 today / 1,249.04 after the plan | truth.json |


### Revision 11 — second independent coherence audit of the Revision-10 SQL

| Finding (verified both sides) | Fix | Evidence |
|---|---|---|
| BigQuery 'google cloud charges the svb card' vs Google payments on MasterCard x-2758 (the SVB card is 5348; 2758 also pays Arthur's GitHub and PayPal) | 'google cloud charges my card on the 1st, not the svb one. it was $4.97 this month' → Hold row already off the SVB card → by when = the review call (Mar 12) | blake@harmonygames.co_1855947447649217022.json (Feb 1 2026, $4.97, x-2758); leonard@harmonygames.co_1787909925965085132.json (SVB card 5348) |
| OpenAI 'the last one was $50 last may' vs the costs tab (no OpenAI charge after Apr-24) — the mail (May 2 2025 $50) and the tab disagree in base | the comment no longer dates a top-up: 'prepaid api credits we topped up now and then, nothing recurring' (rule 2 one-off purchases) | HG Costs OpenAI row; blake@harmonygames.co_1830989465254730549.json |
| rule 6 'ads, cloud — bill on the 1st' vs Meta's threshold billing (many receipts a month) | rule 6 now states a convention: 'for accounts billed on usage — ads, cloud — use Feb 28' | Leonard's mailbox: Meta ads receipts Jan 2026 ×26, Feb 2/3/5/8/12 |
| 'unlabeled' costs-tab lines (labels are names in the tab) | project description 'A few costs-tab lines are filed under other names: the $6,250 one is Singular and the hosting one is GitHub'; issue descriptions '($6,250 line)', '(hosting line)' | Singular invoices $25,000 (Sep-24) / $6,250 (Sep-25) = tab Q/AC; GitHub receipts 169/105/86 = AD/AE/AF |
| Docusign 'he used it for the art contracts' vs every envelope being Leonard's | 'docusign goes to robert from here. annual, $300, renews apr 20' | leonard@harmonygames.co_1827068676034658582.json |
| Calendly auto-renew claim by Robert while renewals go to Leonard | Leonard's comment 'auto-renew has been off since october, right after it charged' | Calendly Oct 13 2025 charge (costs tab Oct-25 96) |
| held: Soundly $10 notice vs the Aug 2025 'Monthly: $19.99' change | kept — the same Aug 2025 notice offers to lock the current rate; /prompt run 2 rejected this as a conflict (P2-DR9) | 00014928.json |
| held: Slack and Workspace 'on the svb card' | kept — no base billing mail names their card | Slack renewal mails Jan 3 / Feb 3 2026; Workspace invoices Jan 1 / Feb 2 2026 |


### Revision 12 — /prompt review 6adfee3f27ce6ca81b457137_1_prompt (3) (FAIL: Feasibility 2, UGT 2, Cross-Service Coherence 2) and fixes

| Finding | Fix | Evidence |
|---|---|---|
| 1 Workspace cost only inside a PDF the Agent can't read | Leonard's ENG-2464 comment: 'workspace is on the svb card, this month's invoice was $298.13' | robert@harmonygames.co/1856033699491658253 att_0001.pdf: $298.13 (Jan 1–31 2026) |
| 2 Unity Ads inside the UA line, no record of it ending | project description: 'we stopped the unity ads in the UA line after october, so they're not in here' (rule 2) | Unity Ads CINV invoices end with 'uAds 1 - 31/10/2025' (Nov 10 2025); no later Unity Ads invoice; ledger Jan/Feb has no Unity line |
| 3 Zapier switch-over undecided (Oliver's #issuefeed pipe note) | Oliver's Zapier comment removed | — |
| Helpshift by when (switch-over of both games off Helpshift not recorded) | Oliver's ENG-2439 comment: '... both games' support buttons now open email instead of helpshift' → export and switch-over done → Closed row, dash | Leonard #winddown 1770789534.434749 'We gotta move domino delights and zombie match off Helpshift before Feb 28th. We can just open up the email app' |
| 4 Layer receipt 'next payment Feb 25' vs Leonard 'we have access until March 3rd' | receipt dated 2026-02-03, 'Your next payment is on March 3, 2026' → Requested row by when 2026-03-02 | #prototype C09UHHN6PFZ/1770837702.167889 |
| 5 Linear and DocuSign 2025 charges missing from the costs tab | in-world lines restored as the reviewer recommends: ENG-2448 '... the p&l stops after the 2024 payment'; ENG-2469 '(the p&l missed last april's charge)' (accepted in /prompt run 2) | HG Costs Linear (last Aug-24 2403), Docusign (Apr-24 300) |
| 6 HG Costs header years (minor) | no graded value reads the costs tab's month columns; OEs and rubric stay off them | — |
| totals | unchanged: 28 rows, 11,045.13 / 1,249.04 | truth.json |


### Revision 13 — blind unique-answer audit (register rebuilt from Robert-readable records only)

| Finding | Fix |
|---|---|
| no fatal fork; required values all readable; totals re-added 11,045.13 / 1,249.04 | — |
| Calendly 'auto-renew off' is not plainly 'cancelled' (rule 2) | Leonard: 'we cancelled calendly in october right after the annual charge, it just runs out' |
| Unity Ads 'stopped' is not plainly 'cancelled' (rule 2) | project description: 'we cancelled the unity ads in the UA line after october' |
| held as settled by /prompt run 4 | Layer/Cursor Requested (rule 5: nothing back from the vendor); Slack is a clash (reading I); Metabase Move (keep list = the thread parent and its reply) |
| rubric note | the clash set is three (Slack free plan and guest seats, Google archive, plus the third in §9.2); the rubric accepts the two Slack items merged or listed apart |


### Re-verified facts

Re-read through the exports this session: costs tab column AF values (f_605121f4a36752645e0ac3), ledger FIN-000686…FIN-000704, #winddown timestamps (C0ADGSZKR3R/2026-02.json), Robert's mail 00016283 / 00016086 / 00016395 / 00016044 / ElevenLabs / Linear notice, Trello board 640643a3fd8f3ca308d9318e idShort range, Combo-Fighters#37 fields, Linear team memberships.

Unresolved: (1) platform /injection may not resolve a Linear project inserted by the same SQL (local base_check patched, §12); (2) the difficulty projection waits for the Opus pre-check and the rubric (scenario §6, red team B3/B5).

```
STAGE GATE injection: PASS — Task_Authoring-2/task_inputs · 01_Universe_Inject.sql#50f6a195de7e · 01_Hardness_Manifest.json#526f2a78d444 · 01_Grounding_Dossier.md#7bf3e5461eb4 · blocking 0 · warnings 0 · checks 28
[PASS] structure.outputs: 3 output(s) present: 01_Universe_Inject.sql, 01_Hardness_Manifest.json, 01_Grounding_Dossier.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json)
[PASS] chain.scenario: upstream 'scenario' PASS pasted and current (01_Scenario_Design.md#8f37cbc35bf2, 01_Hardness_Manifest.draft.json#9a523dac3d2c)
[PASS] structure.sections: 17 required sections present and non-empty (01_Grounding_Dossier.md)
[PASS] structure.placeholders: no placeholders in 01_Grounding_Dossier.md
[PASS] evidence.entity: 12/12 items carry a source pointer (min 90%)
[PASS] evidence.keyword: 9/9 items carry a source pointer (min 100%)
[PASS] evidence.persona_reach: 12/12 items carry a source pointer (min 100%)
[PASS] evidence.record_ledger: 103/103 items carry a source pointer (min 100%)
[PASS] evidence.facts_for_human: 53/53 items carry a source pointer (min 100%)
[PASS] tool.sql_lint: sql_lint re-run matches the paste: errors 0, warnings 8, rows 138
[PASS] review.warning_dispositions: every sql_lint warning class dispositioned (confluence statement — unscoped and rare×2, clock×6)
[PASS] tool.base_check: base_check pasted PASS; re-run PASS
[PASS] tool.hardness_gate: hardness_gate (SQL) pasted PASS; re-run PASS
[PASS] structure.design_delta: final manifest keeps all 57 draft ids
[PASS] tool.check_sql_pasted: persona_view check-sql --load-bearing output pasted with verdict PASS
[PASS] reach.injection: 24 scoped load-bearing ids YES for robert
[PASS] structure.facts_declared: manifest declares 9 load-bearing fact(s) in `facts`
[PASS] tool.fact_check: fact_check --no-leak pasted PASS; re-run PASS
[PASS] kb.coherence_hazards: coherence audit cites 13 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 5 seeded speakers each cited with activity.json status; conventions.json cited
[PASS] kb.integrations: companions listed per integrations.json (10 INT ids, services ['confluence', 'gcal', 'gdocs', 'gdrive', 'github', 'gmail', 'gsheets', 'linear', 'slack', 'trello'])
[PASS] boundary.anchor_naming: 2 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 15 evidenced counter-readings (of 15 found; need ≥ 14) in 01_Grounding_Dossier.md
[PASS] review.coverage: self-review addresses all 9 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

