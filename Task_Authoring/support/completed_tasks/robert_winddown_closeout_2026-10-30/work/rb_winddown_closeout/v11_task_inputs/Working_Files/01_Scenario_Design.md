# Scenario Design — rb-winddown-closeout · design only · contains no prompt, OE or criterion text

Persona Robert (Co-Founder & Creative Director, Executive) · competency Corporate Ops · task skill Planning and Decision Support · horizon Long (platform "Task Type": long-horizon) · difficulty mode easy · universe date February 14, 2026 00:00 UTC (Saturday). Author targets (`00_Assigments.md`, chat 2026-10-28): **more than 150 tool calls in every run** and an average **under 80%**; the Evals line is under 75% (strictest governs), so the design aims at ~62–68%. Builder scripts: `support/task_work/rb_winddown_closeout/` (`mint_ids.py` mints every id, the seeded wording `planned_text.json` and the emitted ground truth `truth.json`; `build_manifest.py` writes the draft manifest; `build_design.py` writes this file). Reference designs: the three tasks in `support/completed_tasks/` (Frederick ×2 missed 75% at 78.3% / 80.8%; Douglas landed 56.3% after three hardening rounds — its lessons are applied in §6).

## 0 Assignment, persona census and horizon note

| Field | Assigned (verbatim, `00_Assigments.md`) | Resolution |
|---|---|---|
| persona | Robert | roster `robert`, robert@harmonygames.co, Executive (`Evals/references/persona/roster.json`) |
| role | Co-founder & Creative Director | co-founder; member of #winddown (C0ADGSZKR3R) with Leonard and Arthur; holds the creative-tool logins (Soundly cancelled by him, C0ADGSZKR3R/1770839322.836779; Figma admin, C0ADGSZKR3R/1770859313.592649) |
| business function | Executive | Evals category Founders / Exec / Strategy (`Evals/references/rules/task_categories.md`) |
| competency | Corporate Ops | wind-down account and subscription close-out (timeline 2026-02-09 "Vendor terminations" beat) |
| task skill | Planning and decision support | a close-out plan: per account an action, status, deadline, owner and monthly cost, decided by four rule sources, plus the clashes with earlier decisions |
| horizon | long-horizon | manifest `horizon: Long Horizon`, `effective_profile: long` with `profile_exception` (author's >150-call band) |
| universe date | February 14, 2026 00:00 | clock 2026-02-14T00:00:00Z (`tools/hg_clock.py`); latest seed 2026-02-13T20:49:58Z |
| difficulty mode | easy | recorded; author target under 80%, Evals gate under 75%, pass@1 ≤ 3 of 6, SD 0.1–0.3, ≥ 2 failure patterns |

**Remit argument.** On Feb 9 the founders decided to shut down (C0ADGSZKR3R/1770663250.160009). Leonard ran the vendor terminations (Helpshift C0ADGSZKR3R/1770673717.808759, Singular C0ADGSZKR3R/1770674268.840059), asked Robert to cancel Soundly or move it to his personal card (C0ADGSZKR3R/1770837766.132019), posted a keep list (C0ADGSZKR3R/1770933601.686309) and action items (C0ADGSZKR3R/1770933903.645709), and said the P&L covered everything (C0ADGSZKR3R/1770933999.157259). His own plate (C0ADGSZKR3R/1770934638.035469) is Carta, the angels and Sunset onboarding; Arthur took the data hand-off (C0ADGSZKR3R/1770935695.500189). The base Task List in the Wind Down folder has "Cancel or move all software subscriptions" open with no owner (f_31115ddb6ed866f2b10d60). Pulling the third co-founder in to own the close-out register before the Google accounts are archived is the Corporate Ops planning work Robert would plausibly get on Feb 13.

**Effective profile.** Long Horizon normally maps to `extreme` (≥ 500 calls). The author asked for more than 150 calls in every run, not a ~600-call design, so the manifest uses the gate's `long` profile (extreme breadth, authorities, chains and traps; 100-call floor) with `profile_exception` quoting the author. Necessary budget: **158 unconditional calls** (§9). Douglas's 139-call budget measured 163–238 counted calls, so this budget should put the leanest correct run above 150.

Persona reach census (`python3 Task_Authoring/tools/persona_view.py reach robert --top 10`, verbatim):

```
REACH  Robert <robert@harmonygames.co>  Co-Founder & Creative Director / Executive
clock 2026-02-14

SLACK  user=EMPLOYEE_0016_SLACK_ID  visible channels=224 {'mpim': 66, 'private': 82, 'public': 37, 'im': 39}  messages=383979  public-not-member (UNVERIFIED)=33
  persona posts=129939 last post=2026-02-13  last activity in visible channels=2026-02-13
  C05433XK267    builds                                 public  mem=31  msgs=41107  2023-04-20..2026-02-12
  C04UTBZL6AX    founders                               private mem=7   msgs=40552  2023-03-20..2025-10-06
  C07C2866011    executives                             private mem=9   msgs=28266  2024-07-11..2026-02-13
  D04UP2L3E3S    D04UP2L3E3S                            im      mem=5   msgs=27517  2023-03-15..2026-02-12
  C05H8KVNU67    game-design                            private mem=27  msgs=22751  2023-07-16..2025-10-06 archived
  C050WGU41HR    engineering-bots                       private mem=35  msgs=20306  2023-03-29..2026-02-11
  C05V5FNLB9V    god-bugs                               private mem=31  msgs=16889  2023-10-07..2026-02-11
  C0880U9751A    zombie-match3d                         private mem=25  msgs=16773  2025-01-09..2026-02-11
  C09UHHN6PFZ    prototype                              private mem=18  msgs=12172  2025-11-24..2026-02-12
  C04UEQVDVB7    admin_foundersonly                     private mem=7   msgs=11086  2023-03-17..2026-02-11

GMAIL  mailbox=robert@harmonygames.co threads=16233 messages=19169 range=2023-03-15..2026-02-13
  threads by last-message month (recent): {'2025-09': 327, '2025-10': 354, '2025-11': 251, '2025-12': 184, '2026-01': 397, '2026-02': 250}
  top correspondents: SVC_0107_EMAIL (6580), leonard.hayes@harmonygames.co (2277), SVC_4131_EMAIL (1685), arthur.blake@harmonygames.co (1361), SVC_2398_EMAIL (543), SVC_0325_EMAIL (517), SVC_4249_EMAIL (424), SVC_3942_EMAIL (359), frederick.stone@harmonygames.co (353), julia.lawson@harmonygames.co (312)

GCAL  own=['robert@harmonygames.co'] shared=[] events=1229 (distinct ical_uid 547, cancelled 118)
  last event before clock=2026-02-12T16:30:00Z  next after clock=None
  by month: 2023-03:9 2023-04:27 2023-05:40 2023-06:23 2023-07:27 2023-08:62 2023-09:32 2023-10:43 2023-11:34 2023-12:26 2024-01:57 2024-02:32 2024-03:20 2024-04:36 2024-05:36 2024-06:49 2024-07:49 2024-08:42 2024-09:79 2024-10:50 2024-11:40 2024-12:47 2025-01:49 2025-02:17 2025-03:11 2025-04:33 2025-05:42 2025-06:39 2025-07:36 2025-08:14 2025-09:27 2025-10:41 2025-11:19 2025-12:21 2026-01:16 2026-02:4

DRIVE  owned=223 {'application/json': 72, 'application/vnd.google-apps.document': 67, 'folder': 27, 'application/vnd.google-apps.spreadsheet': 26, 'text/plain': 23, 'application/pdf': 5, 'application/vnd.google-apps.presentation': 3}
  shared-with=464 {'application/vnd.google-apps.document': 133, 'application/pdf': 125, 'application/vnd.google-apps.presentation': 80, 'application/vnd.google-apps.spreadsheet': 64, 'text/plain': 37, 'application/json': 22, 'text/csv': 2, 'application/msword': 1}
  shared by owner: {'Resource: 7240535625619857401': 252, 'Resource: -6481757892984311338': 102, 'leonard.hayes@harmonygames.co': 81, 'arthur.blake@harmonygames.co': 13, 'frederick.stone@harmonygames.co': 6, 'julia.lawson@harmonygames.co': 3, 'marcus.bennett@harmonygames.co': 3, 'thomas@harmonygames.co': 2, 'calvin.price@harmonygames.co': 1, 'samuel.turner@harmonygames.co': 1}
  native visible: {'gdocs': 200, 'gsheets': 90, 'gslides': 83}  last modified visible=2026-02-12T19:02:18Z
  UNVERIFIED (domain/anyone, not owned/shared)=101 {'application/vnd.google-apps.document': 39, 'application/vnd.google-apps.spreadsheet': 34, 'application/json': 11, 'application/pdf': 9, 'application/vnd.google-apps.presentation': 8}

UNSCOPED (always visible): contacts, github, trello, linear, snowflake, confluence

LAST ACTIVITY (days before clock): slack_persona_post=2026-02-13 (1d), slack_visible_channels=2026-02-13 (1d), gmail=2026-02-13 (1d), gcal_last_event_before_clock=2026-02-12 (2d), drive_last_modified_visible=2026-02-12 (2d)
```

Linear / GitHub / Trello identities (`entity.py resolve`, §1c): Robert Linear `usr_Robert`, Trello `3d06b73654d0c8940792514c`, Slack `EMPLOYEE_0016_SLACK_ID`, Confluence `user_EMPLOYEE_0016`. Leonard: Linear `usr_63fffeb4fab5233e`, Trello `PERSON_6094_TRELLO_USER_ID`, Confluence `user_EMPLOYEE_0038`. Arthur: Linear `usr_cc3e90160f490686`, Trello `2162c1ba310341bf318f48b7`. Oliver: Linear `usr_bdf01b53c6a92c5e`, Confluence `user_EMPLOYEE_0003`, GitHub `EMPLOYEE_0003_GITHUB_USERNAME`.

## 1 Storyline

**Arc.** Shutdown was decided on Feb 9 (timeline 2026-02-09, `slack:C0ADGSZKR3R:1770663250.160009`). Over Feb 9–12 the founders cancel or keep vendors one message at a time in #winddown, sign the wind-down and data agreements with Sunset (Feb 12 21:29Z, C0ADGSZKR3R/1770931777.561519; signed SOW forwarded to Robert, robert@harmonygames.co/1856956532017091340) and plan to pay off and close the SVB card once the data money lands (C0ADGSZKR3R/1770927223.969899). At 23:24Z Arthur turns the costs tab and the #winddown lists into a Linear project, "Shutdown – accounts" (47 issues, ENG-2438…ENG-2484). Leonard books the delivery review with Sunset for Mar 12 (event created 22:40Z) and Sunset's onboarding lead mails the data delivery checklist (23:58Z). On Feb 13 Arthur amends the keep list in its thread (Gusto), Leonard puts SVB's card terms on the founders' Trello board, writes the register conventions into a doc in the Wind Down folder, comments on his issues, and at 17:21Z asks Robert in #winddown to own the register. Sunset corrects its list in the same mail thread at 18:20Z.

**Timeline placement** (`references/universe_kb/timeline.md`, clock 2026-02-14): the 2026-02-09 "wind-down" and "vendor" beats (Helpshift/Singular Feb 9, Unity Feb 12), 2026-02-11 (termination letters, Google accounts to be archived after Feb 15, Sunset call `gcal:evt_212e50fb5a53ea8016ce29`), 2026-02-12 (agreements signed, `snowflake:FINANCE_LEDGER/FIN-000702` Sunset fee), 2026-02-13 (work continues; Combo-Fighters#37 merged) and 2026-01-13 (Combo Fighter monetisation; Meta UA spend Dec–Feb — the ledger's meta rows). No seed is after 2026-02-13T20:49:58Z.

**Anchors per service.**

| Service | Record | Role |
|---|---|---|
| slack | C0ADGSZKR3R/1771003267.448213 (seed) | anchor A1, Leonard → Robert, 2026-02-13T17:21:07.448213Z |
| slack | C0ADGSZKR3R/1770933601.686309, /1770933903.645709, /1770933999.157259, /1770937232.664809, /1770936655.574079, /1770937188.477219, /1770839729.441789, /1770839825.928989, /1770840054.486779, /1770927223.969899 (base) | keep list, action items, 'covers everything', LLC moves, 'cancelled' claims, Gusto/Slack-plan history, card closure |
| slack | C0ADGSZKR3R/1770948876.205117 (seed, thread of 1770933601.686309) | Arthur's Gusto amendment |
| slack | C09UHHN6PFZ/1770976938.774231 (seed, #prototype) | Oliver asks to keep Cursor (distractor) |
| linear | project 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a 'Shutdown – accounts' (seed), ENG-2438…ENG-2484 + 39 comments | cohort; write targets |
| gmail | robert@harmonygames.co/1856965916492026238 (seed thread: robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> + robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com>) | H1 Sunset's checklist and its correction |
| gmail | robert@harmonygames.co/1856945900224536585 (seed) | Sherwood checklist decoy |
| gmail | robert@harmonygames.co/1853470745017478863, robert@harmonygames.co/1850283027022457279, robert@harmonygames.co/1854432461283937829, robert@harmonygames.co/1849420841999587093 (base) | Singular billing thread (termination asks for written confirmation), Singular Dec 1 invoice, iPostal1 mailbox closed Jan 16, Trello Standard ended Nov 21 |
| gmail | 4 vendor billing mails (seed; §11) | next charge dates, card, Soundly/Kapwing confirmations, Pond5/ElevenLabs |
| trello | 698f48be4ba0affafbf153db (seed, board 640643a3fd8f3ca308d9318e list To Do) | H2 'SVB card payoff + closure' |
| trello | 64de736c2b10abdbda220c1b (base #170, same board, Done 2024) | decoy: the 2023 move of subscriptions onto the SVB card |
| gdocs | f_1326e66bcabfda8fd29e4a (seed, parent d_e5caf6a8c630421942ee59 'Wind Down') | H3 'Close-out register conventions' |
| gdrive | f_768cd23a00c4b12fa0e975 (seed) | Arthur's superseded 'Subscriptions' sheet |
| gsheets | f_605121f4a36752645e0ac3 'HG Costs' (base) | cost lines (rule 3 membership); 'Sound (Pond5, Soundly,Elevenlabs)' and 'UA' shared lines; stale December figures (cost decoy) |
| snowflake | FINANCE.EXPENSES.FINANCE_LEDGER FIN-000687…FIN-000700 (base) | AWS 1,485; meta −2,843.84/−956.45; applovin −9.80/−9.83 |
| gcal | evt_f1d245d44ceff5a6e049c0 (seed, Robert's copy of 3; ical a8690ec17cab7912257b3b1b2b9fcbef@hg4) | review call 2026-03-12 17:00Z |
| linear | cmt_96ae7b3689c1d073a2ff (Oliver's ENG-2439 comment) + drive helpshift_export_2026-02-13.zip | Helpshift export done Feb 13 |
| confluence | page_ua_vendor_closeout (seed, 2025-03-18) | Growth/UA conventions decoy |
| github | harmonygames-Games/Combo-Fighters#38 + harmonygames-Games/Combo-Fighters#38#c_1 (seed) | CodeRabbit's own cancellation notice |

**Cohort.** `cohorts.json: no fit — the cohort is the seeded Linear project (45 issues, created Feb 12) plus four accounts the project lacks; the nearest base cohort, LIN-OPEN-ENG (115 open ENG issues), holds none of them and is not touched` — the seeded issues take ENG-2438… after the base maximum ENG-2437; LIN-CQ11 (ENG created 2025-Q4, 61) ends before them. SF-LEDGER (FINANCE_LEDGER rows by category, 704) is the ledger population rule 3 points into; its `hazards_inside` (Q05 burn vs ledger) are not read by the task (only Jan/Feb rows by counterparty).

**Natural traps used** (`references/universe_kb/trap_catalog.json`): X03 (the costs tab's blanked '[PERSON_NAME_0499]' is Singular — named in Arthur's description), D04/D08 (P&L workbook versions; only the January workbook's costs tab is named), D07 (the founders' Trello board is stale since Nov 2025 — H2 revives it with one card), C01 (a reply that corrects — Arthur's Gusto reply, Sunset's correction), B03 (CodeRabbit bot activity — its notice is the confirmation), B05 (Zapier pipes Helpshift into #issuefeed — Oliver's note), K02 (app-name lineage, not used), P02 (Brooks: Oliver vs Lauren).

**Originality.** Not the Combo Fighters launch record, the 133-PR residue register, the RC-flag gate or the art-canon handoff; not the Frederick card-spend or account-handover tasks (Frederick's reconciled card charges to receipts; this task decides an action per vendor account under four rule sources) and not Douglas's beta sign-off (tickets × deploys).

## 1a Coherence audit

Scope = every record a correct run opens: the #winddown history Feb 9–13, the keep-list thread, #prototype's Cursor message, the 47 issues and their comments, Sunset's and Sherwood's mails, the 18 seeded billing mails, the base Workspace and ElevenLabs receipts and the base Singular, iPostal and Trello mails, the two Trello cards, the conventions doc, Arthur's sheet, the January P&L costs tab, the Jan/Feb ledger rows, the review event, the UA page, page_aws_infra and Combo-Fighters#38. Known hazards walked from `references/universe_kb/coherence_hazards.json` (all six categories).

| Record | Category | Fields | Evidence pointer | Hazard id | Disposition |
|---|---|---|---|---|---|
| Seeded mail threads (Sunset checklist + correction) | temporal | message dates in thread order | robert@harmonygames.co/1856965916492026238 | hazard T02 | avoid: both messages in ISO date order, the correction 18h after the checklist |
| Base support playbook page contradicts itself | semantic | page body vs comments | page_support_playbook (base) | hazard S08 | avoid: the Helpshift export is logged on a seeded page (page_support_after_helpshift), so page_support_playbook is neither modified nor cited |
| Storyline YAML artifacts dated 2026-02-13 | temporal | artifacts absent from base | slack:C0ADGSZKR3R (Feb 13 base posts: none) | hazard T07 | avoid: no seed references a YAML artifact; seeds carry their own ids |
| Contacts job titles (Robert 'CPO', Leonard 'CEO') | semantic | job | contacts.json /contacts/108, contacts.json /contacts/170 | hazard S06 | avoid: no seed or graded value uses a Contacts title |
| Gemini notes misname the entity | semantic | entity name | f_0c37bb7235683d73569903 | hazard S07 | avoid: Leonard-private; not cited or read |
| Slack links to native Google ids | cross-service referential | folder link | C0ADGSZKR3R/1770673821.508389 | hazard R04 | avoid: seeds name the Wind Down folder and every file by title |
| Calendar invitations with no GCal instance | cross-service referential | invitation mails | evt_f1d245d44ceff5a6e049c0 | hazard R08 | fold in: the review event is seeded on all three calendars with no invitation mails (integration_exceptions no_notify), so no orphan mail and no orphan event |
| Helpshift balance quoted three ways | quantitative | $1,500 / $150×8 / $300 | C0ADGSZKR3R/1770673467.186629, C07C2866011/1770765511.243329, C04UEQVDVB7/1770765910.100299 | hazard Q07 | fold in: balances owed, not the monthly cost; the register uses the costs tab 150 and Leonard's comment quotes Helpshift's final $300 invoice — consistent with the last of the three |
| Keep-list parent counters after the Gusto reply | quantitative | reply_count / latest_reply | C0ADGSZKR3R/1770933601.686309 | hazard Q01 | fold in: UPDATE companion sets reply_count 1, reply_users_count 1, latest_reply = the reply ts |
| P&L vs Snowflake cash | quantitative | month-end cash | f_605121f4a36752645e0ac3, CASH_BALANCE | hazard Q06 | avoid: only the HG Costs tab is used; no cash figure is graded |
| Combo-Fighters#37 merged after the announcement; CodeRabbit comment | state/lifecycle | merge vs shutdown | harmonygames-Games/Combo-Fighters#37 | hazard L13 | avoid: the CodeRabbit notice is seeded on a new open PR #38; #37 is not modified or cited |
| Open issues assigned to quiet people | state/lifecycle | assignee | ART-384 | hazard L08 | avoid: every seeded issue is assigned to Leonard, Arthur or Robert (active_feb_2026) |
| Linear ids not usr_ + 16 hex | identifier/format | assignee_id | usr_Robert on ART-100 (base) | hazard I10 | fold in: Robert's base id usr_Robert is used verbatim on his issues |
| Drive owner is a Resource token | identifier/format | owner_email | f_31115ddb6ed866f2b10d60 | hazard I14 | fold in: the conventions doc copies the Wind Down siblings' owner 'Resource: 7240535625619857401' and share list |
| Mailbox file aliases | identifier/format | thread file names | blake@harmonygames.co_1856689465050769375.json | hazard I03 | fold in: copies of Sunset/Sherwood mails filed under the base aliases (leonard@, blake@) |
| Token-owned billing mailboxes / senders | identifier/format | sender tokens | SVC_5771_EMAIL (Unity), SVC_0019_EMAIL (Singular, robert@harmonygames.co/1850283027022457279) | hazard I05 | fold in: seeded billing mails reuse the vendor's base sender token where one exists; new vendors get new SVC_77nn tokens |
| 'Sunset' counterparty redacted in Slack | other | [USERNAME_26907] | C0ADGSZKR3R/1770931777.561519 | none (other) | fold in: the signed SOW mail (robert@harmonygames.co/1856956532017091340) names Sunset; the checklist thanks them 'for signing today' |

**Sibling-defect sweep.** For each designed defect, other records with the same kind in scope:

- *Stale costs-tab forecast:* iPostal (tab 34.79 in Dec-25; closed Jan 16, robert@harmonygames.co/1854432461283937829) is designed. Siblings: Trello (tab 0 since its Standard plan ended Nov 21 — consistent), AWS (tab 0 while the ledger shows 1,485/month, FIN-000687), UA (tab 0 while meta/applovin charge, FIN-000689/FIN-000688), Kling (tab 9 in Sep-25, 0 since — consistent with Robert's 'dropped after the september trial'). AWS, meta and applovin take their own January ledger line under rule 8 (the costs-tab AWS/UA values decide nothing); UA membership is rule 3; none is left as a silent second answer.
- *'Cancelled' said in Slack without the vendor's word:* Layer (C0ADGSZKR3R/1770837793.168589), CodeRabbit (C0ADGSZKR3R/1770936655.574079), Cursor and Kapwing (C0ADGSZKR3R/1770937188.477219), Zapier (Leonard's list C0ADGSZKR3R/1770933450.410449), Soundly (C0ADGSZKR3R/1770839322.836779), Helpshift (C0ADGSZKR3R/1770789534.434749). Every one is a cohort issue with a designed status; Soundly, Kapwing, Helpshift and CodeRabbit have a vendor confirmation, Layer, Cursor and Zapier do not, Singular's own thread asks for one that never came (robert@harmonygames.co/1853470745017478863, Feb 12 21:43Z).
- *Blanked vendor names:* '[PERSON_NAME_0499]' (Singular, X03), the hosting line '[PERSON_NAME_0250]' (GitHub: its Sep–Dec values 165/169/105/86 are Arthur's GitHub receipts), '[PERSON_NAME_20852]' (Kapwing per C0ADGSZKR3R/1770933450.410449) and '[USERNAME_30019]' (dbt in base Slack, C0ADGSZKR3R/1770937232.664809) are resolved by base records, not Arthur's project description; the two $30 game-ops lines are named as stipends. The redacted names in #winddown are not relabelled (injection review F2): Leonard's subscriptions table (C0ADGSZKR3R/1770933450.410449) names Kapwing outright, and Arthur's own comment on the dbt issue says dbt is on his KubLLC card.
- *Accounts on Leonard's own card ('I canceled other subscriptions under mine', C0ADGSZKR3R/1770933601.686309):* no seeded receipt names a card number; which card an account bills is stated by its holder in the issue (Intuit on the SVB card per its receipts, Deel by bank transfer; base: the SVB card is a MasterCard, leonard.hayes@harmonygames.co/1846148320251001978), so no hidden personal-card account exists.

## 1b Active speakers

Every person given a seeded voice, with `status_at_clock` from `references/universe_kb/activity.json` (clock 2026-02-14).

| Person | Email | status_at_clock (activity.json) | Seeding role |
|---|---|---|---|
| Leonard Hayes | leonard.hayes@harmonygames.co | active_feb_2026 | anchor; conventions doc; SVB card; comments on his issues; review event organizer |
| Arthur Blake | arthur.blake@harmonygames.co | active_feb_2026 | Linear project and 47 issues; Gusto reply; comments on his issues; 'Subscriptions' sheet |
| Robert | robert@harmonygames.co | active_feb_2026 | persona; comments on his own issues (Feb 13 20:41–20:49Z) |
| Oliver Brooks | oliver.brooks@harmonygames.co | active_feb_2026 | Cursor request in #prototype; Zapier note; Helpshift export comment; PR #38 author |
| Frederick Stone | frederick.stone@harmonygames.co | quiet_since_2025-10 | author of the 2025-03-18 UA conventions page only (he was active then) |

Vendors write only billing mail through the billing group (base precedent robert@harmonygames.co/1850283027022457279); CodeRabbit (`PERSON_6026_GITHUB_USERNAME`) writes only its PR notice; Sunset's onboarding lead and Sherwood write one mail thread each. Seeded text follows `references/universe_kb/conventions.json` (Arthur lowercase and short, Leonard plain sentences, Linear comments one line).

## 1c Identity traps

`python3 Task_Authoring/tools/entity.py collisions` (verbatim, first sections) and `resolve` for every person the design names:

```

SHARED_FIRST_NAMES (4)
  claire: ['Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]', 'Claire <github:PERSON_2360_GITHUB_USERNAME>']
  marcus: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Marcus Lee <marcus.lee@harmonygames.co>', 'Marcus <marcus@harmonygames.co>', 'Marcus <github:PERSON_0396_GITHUB_USERNAME>']
  martin: ['Martin Lewis <PERSON_0394_EMAIL>', 'Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]']
  thomas: ['Thomas Baker <thomas.baker@harmonygames.co>', 'Thomas <thomas@harmonygames.co> [persona thomas]']

SHARED_LAST_NAMES (5)
  baker: ['Owen Baker <owen.baker@harmonygames.co> [persona owen_baker]', 'Thomas Baker <thomas.baker@harmonygames.co>']
  bennett: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Oscar Bennett <oscar.bennett@harmonygames.co>']
  brooks: ['Lauren Brooks <lauren@harmonygames.co>', 'Oliver Brooks <oliver.brooks@harmonygames.co> [persona oliver_brooks]']
  lawson: ['Julia Lawson <julia.lawson@harmonygames.co> [persona julia_lawson]', 'Peter Lawson <peter.lawson@harmonygames.co>']
  price: ['Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]', 'Nathan Price <nathan@harmonygames.co>']

LOOKALIKE_HANDLES_AND_ALIASES (15)
  - Gmail thread files of arthur.blake@harmonygames.co are named 'blake@harmonygames.co_*'
  - Gmail thread files of brian.foster@harmonygames.co are named 'brian@harmonygames.co_*'
  - Gmail thread files of calvin.price@harmonygames.co are named 'calvin@harmonygames.co_*'
  - Gmail thread files of claire.morgan@harmonygames.co are named 'claire@harmonygames.co_*'
  - Gmail thread files of frederick.stone@harmonygames.co are named 'frederick@harmonygames.co_*'
ENTITY email:leonard.hayes@harmonygames.co  name=Leonard Hayes  kind=person  emails=['leonard.hayes@harmonygames.co']
  persona: leonard_hayes - Co-founder & Creative Director / Executive
  slack      id=EMPLOYEE_0038_SLACK_ID, name=Leonard Hayes, real_name=Leonard Hayes, email=leonard.hayes@harmonygames.co, is_bot=False, deleted=False, messages=143292, first_post=2023-03-15, last_post=2026-02-13   [join: exact_email]
  gmail      mailbox=leonard.hayes@harmonygames.co, threads=17635, messages=22648, first=2023-03-15, last=2026-02-13, thread_filename_alias=['leonard@harmonygames.co']   [join: exact_email]
ENTITY email:arthur.blake@harmonygames.co  name=Arthur Blake  kind=person  emails=['arthur.blake@harmonygames.co']
  persona: arthur_blake - Co-founder & CTO / Executive
  slack      id=EMPLOYEE_0025_SLACK_ID, name=Arthur Blake, real_name=Arthur Blake, email=arthur.blake@harmonygames.co, is_bot=False, deleted=False, messages=38591, first_post=2023-03-20, last_post=2026-02-12   [join: exact_email]
  gmail      mailbox=arthur.blake@harmonygames.co, threads=4721, messages=6876, first=2023-03-23, last=2026-02-13, thread_filename_alias=['blake@harmonygames.co']   [join: exact_email]
ENTITY email:oliver.brooks@harmonygames.co  name=Oliver Brooks  kind=person  emails=['oliver.brooks@harmonygames.co']
  persona: oliver_brooks - Senior Game Engineer / Engineering
  slack      id=EMPLOYEE_0003_SLACK_ID, name=Oliver Brooks, real_name=Oliver Brooks, email=oliver.brooks@harmonygames.co, is_bot=False, deleted=False, messages=23993, first_post=2024-08-12, last_post=2026-02-12   [join: exact_email]
  gmail      mailbox=oliver.brooks@harmonygames.co, threads=1687, messages=2445, first=2024-08-08, last=2026-02-12, thread_filename_alias=['oliver@harmonygames.co']   [join: exact_email]
ENTITY email:robert@harmonygames.co  name=Robert  kind=person  emails=['robert@harmonygames.co']
  persona: robert - Co-Founder & Creative Director / Executive
  slack      id=EMPLOYEE_0016_SLACK_ID, name=Robert, real_name=Robert, email=robert@harmonygames.co, is_bot=False, deleted=False, messages=129939, first_post=2023-03-15, last_post=2026-02-13   [join: exact_email]
  gmail      mailbox=robert@harmonygames.co, threads=16233, messages=19169, first=2023-03-15, last=2026-02-13   [join: exact_email]
```

Correct entity vs lookalikes: Oliver Brooks is oliver.brooks@harmonygames.co (not Lauren Brooks, lauren@harmonygames.co, active_jan_2026_quiet_in_feb); Arthur's mailbox files are `blake@…`, Leonard's `leonard@…`. 'Sunset' is the wind-down provider (signed SOW robert@harmonygames.co/1856956532017091340), not the 'Sunset of Creative Reporting' notices (robert@harmonygames.co mail 00014921) or Sunset's platform invite sender SVC_0210 (robert@harmonygames.co/1856871927204514890). 'Intuit' and 'QuickBooks' are one vendor (rule 1). 'Meta' appears as ad spend (ledger marketing_ua) and as Audience Network self-billing (robert@harmonygames.co mail 00016816, revenue) — only the spend account is a register row. 'AppLovin' is UA spend (marketing_ua) and MAX ad revenue (FIN-000697) — only the UA account is a row.

## 2 Cohort spine

**Rule (K2 + H3).** Every issue of the Linear project 'Shutdown – accounts' (47, ENG-2438…ENG-2484), plus accounts the project lacks that (a) still charge us in the January/February ledger lines, (b) share a costs-tab line with an account in the project, or (c) are on Sunset's corrected list. Then rule 1 (one row per vendor account; the newer of two issues for one vendor is the duplicate) and rule 2 (exclusions; Sunset's list overrides them). Candidates **52**; register rows **28**; excluded issues **20**.

**Per-account truth** (emitted by `mint_ids.py` → `truth.json`; deadlines are the conventions' rule 6, costs rule 8):

| Issue | Account | Action | Status | Deadline | Owner | Monthly cost | Cost source | Decisive evidence |
|---|---|---|---|---|---|---|---|---|
| ENG-2438 | Unity | Cancel | Requested | 2026-02-18 | Arthur | 2,348.50 | owner figure: Unity Pro 11 seats, $2,348.50 a month (invoiced on the 19th) | comments / tab |
| ENG-2439 | Helpshift | Cancel | Closed | — | Leonard | 150.00 | owner figure: $150 a month | ZIP |
| ENG-2440 | Soundly | Cancel | Closed | — | Robert | 10.00 | own charge (shares the Sound line) | robert@harmonygames.co/<CAxSGYrkpVAs45dr7lAugwSThN-X-ma7vq_V1xAV@mail.gmail.com> |
| ENG-2448 | Linear | Hold for Sunset | — | 2026-03-12 | Arthur | 152.72 | owner figure: annual Standard $1,832.65 paid Aug 21 2025 / 12 | evt_f1d245d44ceff5a6e049c0 |
| ENG-2449 | Figma | Hold for Sunset | — | 2026-03-12 | Robert | 101.00 | own charge, annual $1,212 / 12 | robert@harmonygames.co/<CAowZ1ukjS1ZxLCL4aRt1VM-c-GnNMTNWVQS47OM@mail.gmail.com>, evt_f1d245d44ceff5a6e049c0 |
| ENG-2451 | Trello | Hold for Sunset | — | 2026-03-12 | Leonard | 0.00 | free plan since Nov 21, 2025 | robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com>, evt_f1d245d44ceff5a6e049c0 |
| ENG-2454 | Singular | Cancel | Requested | 2026-02-28 | Leonard | 2,083.33 | own charge, quarterly $6,250 / 3 | comments / tab |
| ENG-2455 | AWS | Cancel | Open | 2026-02-28 | Arthur | 1,485.00 | own January line in the finance ledger (FIN-000687, -1,485) | comments / tab |
| ENG-2456 | Metabase | Move to Arthur's LLC | — | — | Arthur | 148.00 | owner figure: $148 a month | robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> |
| ENG-2457 | dbt | Hold for Sunset | — | 2026-03-12 | Arthur | 100.00 | owner figure: $100 a month | robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> |
| ENG-2458 | BigQuery | Hold for Sunset | — | 2026-03-12 | Arthur | 4.97 | owner figure: $4.97 charged Feb 1 | robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> |
| ENG-2460 | Intuit QuickBooks | Keep | — | 2026-02-19 | Leonard | 115.00 | owner figure: $115 on the 4th | 698f48be4ba0affafbf153db |
| ENG-2462 | Carta | Cancel | Open | 2026-08-14 | Leonard | 321.00 | owner figure: annual $3,852 / 12 | comments / tab |
| ENG-2464 | Google Workspace | Hold for Sunset | — | 2026-02-19 | Leonard | 298.13 | owner figure: this month's invoice $298.13 (= Feb 2 2026 invoice PDF) | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>, robert@harmonygames.co/1856033699491658253 |
| ENG-2465 | Slack | Hold for Sunset | — | 2026-02-19 | Leonard | 87.22 | owner figure: renewed Feb 3 for $87.22 | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> |
| ENG-2467 | Gusto | Cancel | Open | 2026-03-02 | Leonard | 116.00 | owner figure: January's invoice $116 | b9ef575bec54b095edb75a0fe83580f5 |
| ENG-2468 | Deel | Keep | — | — | Leonard | 300.00 | owner figure: $300 a month | comments / tab |
| ENG-2469 | Docusign | Cancel | Open | 2026-04-19 | Robert | 25.00 | own charge, annual $300 / 12 | comments / tab |
| ENG-2473 | Layer | Cancel | Requested | 2026-03-02 | Leonard | 49.00 | own charge (not on the tab) | robert@harmonygames.co/<CA4Ce6Oa74xUtCgFI1iGnZMieCxsUh90MhimgGu3@mail.gmail.com> |
| ENG-2474 | CodeRabbit | Cancel | Closed | — | Arthur | 45.00 | own charge (not on the tab) | harmonygames-Games/Combo-Fighters#38#c_1 |
| ENG-2475 | Cursor | Cancel | Requested | 2026-03-04 | Arthur | 40.00 | own charge (not on the tab) | comments / tab |
| ENG-2476 | Zapier | Cancel | Closed | — | Leonard | 73.50 | own charge (not on the tab) | comments / tab |
| ENG-2477 | GitHub | Hold for Sunset | — | 2026-03-12 | Arthur | 90.00 | owner figure: $90 this month all in | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>, evt_f1d245d44ceff5a6e049c0 |
| ENG-2478 | Kapwing | Cancel | Closed | — | Arthur | 24.00 | own charge (not on the tab) | comments / tab |
| ENG-2479 | 1Password | Cancel | Open | 2026-03-07 | Arthur | 19.95 | own charge (not on the tab) | comments / tab |
| (new issue) | ElevenLabs | Cancel | Open | 2026-07-08 | Robert | 4.17 | own charge, annual $50 / 12 (shares the Sound line) | robert@harmonygames.co/1837122624854744558 |
| (new issue) | Meta Ads | Cancel | Open | 2026-02-28 | Robert | 2,843.84 | ledger Jan marketing_ua meta (FIN-000689; shares the UA line) | FIN-000689, FIN-000700 |
| (new issue) | AppLovin (UA) | Cancel | Open | 2026-02-28 | Robert | 9.80 | ledger Jan marketing_ua applovin (FIN-000688) | FIN-000688, FIN-000699 |

Totals: every row today **11,045.13**; Keep + Hold after the plan **1,249.04**. Actions: {'Cancel': 17, 'Hold for Sunset': 8, "Move to Arthur's LLC": 1, 'Keep': 2}; Cancel statuses: {'Requested': 4, 'Closed': 5, 'Open': 8}.

**Excluded issues → Canceled** (rule 2 / rule 1):

| Issue | Vendor | Why out |
|---|---|---|
| ENG-2441 | OpenAI | one-off purchases (prepaid API credit top-ups) |
| ENG-2442 | Typecast.ai | cancelled before Feb 9 (last charge Aug 2025) |
| ENG-2443 | Unity Asset Store | one-off purchases |
| ENG-2444 | Veed | cancelled before Feb 9 (last charge Nov 2025) |
| ENG-2445 | Kling | cancelled before Feb 9 (after the Sep 2025 trial) |
| ENG-2446 | Hailuo.ai | cancelled before Feb 9 (last charge Oct 2025) |
| ENG-2447 | JetBrains | cancelled before Feb 9 (license cancelled end of Dec 2025) |
| ENG-2450 | Adobe | cancelled before Feb 9 (company plan ended Oct 2024) |
| ENG-2452 | Dailybot | cancelled before Feb 9 (last charge early 2024; workspace deleted Sep 2025) |
| ENG-2453 | Solsten | one-off purchase (one study, 2024) |
| ENG-2461 | Intuit | duplicate of the QuickBooks issue (newer) |
| ENG-2463 | Calendly | cancelled before Feb 9 (cancelled Oct 2025 after the annual charge) |
| ENG-2466 | iPostal | cancelled before Feb 9 (mailbox closed Jan 16, 2026) |
| ENG-2470 | Fondo | filing service (taxes and filings) |
| ENG-2471 | Insurance | insurance |
| ENG-2472 | Office 365 | cancelled before Feb 9 (dropped end of 2024) |
| ENG-2480 | Notarize | one-off purchases (per notarization) |
| ENG-2481 | UA Assets | one-off purchases (campaign creative buys, last Apr 2025) |
| ENG-2482 | Lucidchart | cancelled before Feb 9 (Oct 10, 2025) |
| ENG-2483 | Google Ads | cancelled before Feb 9 (account canceled Oct 17, 2025) |

**Surfaces and shortcut audit.**

| Surface | Tool | Records | What it decides | Bulk call that does not cover it |
|---|---|---|---|---|
| linear | linear_list_comments | 46 | R3 · status for Cancel rows | linear_list_issues returns description, state and assignee but no comments; there is no workspace-wide comment listing, so each issue's comments take their own call |
| gmail | gmail_search_messages + gmail_get_message | 8 | R4 · deadline per account | billing mail is spread over 16,000 threads in Robert's mailbox from a dozen tokenised senders; a search snippet does not carry the next-charge date or the card, so each vendor's latest receipt has to be found by name and opened |
| gsheets | gsheets_values_get (HG Costs) | 51 | R1 · register membership: one row per vendor account | one read returns the tab, but its labels have to be split line by line: the Sound line names three sound accounts and the UA line covers two ad networks, none of which has its own issue |

**Necessity rule.** Comments sit on 38 of 45 issues; 31 are decisive (ENG-2438, ENG-2439, ENG-2441, ENG-2442, ENG-2446, ENG-2447, ENG-2448, ENG-2450, ENG-2452, ENG-2453, ENG-2454, ENG-2455, ENG-2456, ENG-2457, ENG-2458, ENG-2460, ENG-2462, ENG-2463, ENG-2464, ENG-2465, ENG-2467, ENG-2468, ENG-2469, ENG-2473, ENG-2475, ENG-2476, ENG-2477, ENG-2478, ENG-2479, ENG-2480, ENG-2481), the rest neutral ('we went to basic at the renewal', 'robert cancelled this on the 11th per #winddown', 'same account as the quickbooks issue', 'cancelled. lite plan, 3 seats at $15' — CodeRabbit's status comes from GitHub, not this comment). 7 issues have no comment, so having a comment reveals nothing; the decisive subset (~40%) is not predictable from title, state, assignee or description. Billing mails exist for 21 accounts, including Keep/Hold ones, so finding a receipt does not flag a Cancel row.

**Short-circuit audit.** Linear comments: the status, owner and in/out columns are written per issue whatever Gmail says; a run that reads only descriptions gets Docusign's owner, Unity/Layer/Singular's status, OpenAI/Typecast/Adobe/Solsten/JetBrains's exclusion and Metabase/dbt/GitHub's card wrong. Gmail: the deadline column for 14 Cancel rows and the move/no-move decision for 6 Keep/Hold rows need the next charge date; no comment carries it. One filtered search cannot sweep it: the senders are 12 different tokens, and a 'receipt' search returns hundreds of Google Play, SVB and Bizxpress mails (robert@harmonygames.co mail 00016326, 00016329) — each vendor has to be found by name.

**House rule overriding the natural reading (A15).** Rule 5: an account is Closed only when the vendor itself has confirmed. Arthur's and Leonard's 'cancelled' messages (C0ADGSZKR3R/1770936655.574079, /1770937188.477219, /1770837793.168589) read as closed; under rule 5 Layer, Cursor and Zapier are Requested, CodeRabbit and Kapwing Closed (bot notice, cancellation mail).

**Dual regime.** Not used — one rule set applies to every account; the time element is the supersession chain (keep list → thread reply; checklist → correction).

**Boundary records (A17).** Inside: Pond5 and ElevenLabs (share the Sound line), Meta Ads and AppLovin (UA) (ledger only), Trello (excluded by its Nov downgrade but held by Sunset). Outside: iPostal (tab still forecasts it), Intuit (duplicate), Arthur's 18-row sheet (stale shorter list), Legal & accounting and Sunset in the ledger (professional firms, rule 2).

## 3 Hidden authorities

| Id | Name (as the hub names it) | Home | Governs | Decoy (scope) | Findability proof |
|---|---|---|---|---|---|
| H1 | Sunset's data checklist | gmail robert@harmonygames.co/1856965916492026238 (checklist robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> + correction robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com>) | R2, R7 | gmail robert@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com> Sherwood's checklist (issuer: Sherwood, not engaged) | `hg.py search search gmail "data delivery checklist"` returns the seeded thread (planned; base has no hit for the phrase) |
| H2 | SVB's card terms | trello 698f48be4ba0affafbf153db 'SVB card payoff + closure' (founders' board, To Do) | R4 | trello 64de736c2b10abdbda220c1b base card #170 'move subscriptions to SVB credit card' (Done, 2023–24) on the same board | `trello_search` 'SVB card' / board card list returns both cards |
| H3 | the conventions doc in the Wind Down folder | gdocs f_1326e66bcabfda8fd29e4a 'Close-out register conventions' | R1, R3, R6 | confluence page_ua_vendor_closeout 'Vendor close-out conventions (Growth/UA)' (team: Growth/UA tracker, 2025) | `gdocs` search 'close-out register conventions' returns the doc; a Confluence search for 'close-out conventions' returns the decoy |

`governs` lists do not overlap. H1's correction is A14 (a reply inside the thread). H2 is A12 (Trello, opened in 50/131 runs) with a same-board decoy; Gmail has 162 SVB notification threads (`references/Scenario_Atlas.md` §1) and none of them dates the closure. H3's decoy carries the same search terms ('close-out conventions') and differs on cost and closed rules for another team's tracker.

## 4 Delegation lattice

| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |
|---|---|---|
| A1 | Leonard's close-out register ask | C0ADGSZKR3R/1771003267.448213 |

**Hub.** A1 is Leonard's message in #winddown: it names the deliverable columns, the destination (a sheet shared with him and Arthur as editors), the Linear write and the reply, and delegates by name to the project, the keep list and its replies, Arthur's LLC moves, Sunset's checklist, SVB's card terms and the conventions doc.

| Fragment | Service | Container | Record | Kind | Delegated by | Delegation quote (verbatim) | Requirements |
|---|---|---|---|---|---|---|---|
| K2 | linear | project Shutdown – accounts | 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a | requirement | C0ADGSZKR3R/1771003267.448213 | "Arthur put every account into the Linear shutdown project last night" | R1, R9 |
| K3 | gmail | thread Harmony Games – data delivery checklist | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | requirement | C0ADGSZKR3R/1771003267.448213 | "Sunset's data checklist" | R2, R7 |
| K4 | gmail | thread Harmony Games – data delivery checklist | robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> | amendment | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | "If our engineers change anything on this list, we'll reply on this thread." | R2 |
| K5 | gcal | event Sunset – data delivery review | evt_f1d245d44ceff5a6e049c0 | requirement | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | "the delivery review call Leonard booked with us" | R4 |
| K6 | trello | card SVB card payoff + closure | 698f48be4ba0affafbf153db | requirement | C0ADGSZKR3R/1771003267.448213 | "SVB's card terms" | R4 |
| K7 | gdocs | doc Close-out register conventions | f_1326e66bcabfda8fd29e4a | format | C0ADGSZKR3R/1771003267.448213 | "the conventions doc I just put in the Wind Down folder" | R1, R3, R4, R5, R6 |
| K8 | slack | C0ADGSZKR3R | C0ADGSZKR3R/1770933601.686309 | requirement | C0ADGSZKR3R/1771003267.448213 | "my keep list from last night" | R2 |
| K9 | slack | C0ADGSZKR3R/1770933601.686309 thread | b9ef575bec54b095edb75a0fe83580f5 | amendment | C0ADGSZKR3R/1771003267.448213 | "the replies under it" | R2, R4 |
| K10 | slack | C0ADGSZKR3R | C0ADGSZKR3R/1770937232.664809 | requirement | C0ADGSZKR3R/1771003267.448213 | "Arthur's moves to his LLC card" | R2 |
| K11 | gsheets | f_605121f4a36752645e0ac3 HG Costs | f_605121f4a36752645e0ac3 | requirement | f_1326e66bcabfda8fd29e4a | "one issue per costs-tab line" | R1 |
| K12 | snowflake | FINANCE.EXPENSES.FINANCE_LEDGER | FINANCE.EXPENSES.FINANCE_LEDGER | requirement | f_1326e66bcabfda8fd29e4a | "anything else still charging us in the January and February lines of the finance ledger" | R1, R6 |
| K13 | linear | issue ENG-2439 Helpshift | cmt_96ae7b3689c1d073a2ff | requirement | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | "please export the full ticket history to Drive before your subscription ends" | R4 |

**Amendments.** K9 (Slack thread reply, Feb 13 02:14Z) changes Gusto from Keep to Cancel and leaves the rest of the keep list standing; K4 (Gmail reply, Feb 13 18:20Z) adds Trello, BigQuery and dbt and removes Metabase ('The rest of the list stands'). No later record re-asserts either amended clause (searched 'gusto' and 'metabase' over the seeded rows in `planned_text.json`).

**Distractors outside the chain.** Oliver's request to keep Cursor (C09UHHN6PFZ/1770976938.774231), Sherwood's checklist, Arthur's 'Subscriptions' sheet (f_768cd23a00c4b12fa0e975), the 2023 SVB-move card, the UA conventions page, page_aws_infra's ~$1,550, the Helpshift balance messages and the Singular Mar 15 extension.

## 5 Chains and trap register

| Chain | Mechanism | Hops (service · record · finding) | Ends in |
|---|---|---|---|
| C1 | A1 | slack C0ADGSZKR3R/1770933999.157259: Leonard: 'I looked at the P&L and I think this covers everything' → linear 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a: Arthur's project: one issue per vendor from the P&L and the lists (Soundly only) → gsheets f_605121f4a36752645e0ac3: costs tab line 'Sound (Pond5, Soundly,Elevenlabs)' = three accounts → gmail robert@harmonygames.co/<CAIoQDHYpNPHXVgnNS8DUmtr__81CmMffz7hcWJv@mail.gmail.com>: Pond5 ended Sep 8 2025 (not renewed → rule 2, left out); ElevenLabs is prepaid to Jul 9 2026 (base receipt robert@harmonygames.co/1837122624854744558) | R1 |
| C2 | A13 | gdocs f_1326e66bcabfda8fd29e4a: rule 3: check the Jan/Feb ledger lines for anything still charging → snowflake FIN-000689: meta marketing_ua -2,843.84 (Jan) and -956.45 (Feb 13); applovin -9.80/-9.83 → linear 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a: no Meta Ads or AppLovin issue in the project → gsheets f_605121f4a36752645e0ac3: the UA line is one costs-tab line for two ad accounts | R1 |
| C3 | A14 | gmail robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>: hold list: Slack, Google Workspace, Figma, Linear, GitHub, Metabase → gmail robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com>: in-thread correction: Trello in, Metabase out, BigQuery and dbt in → linear ENG-2456: Metabase billing already on the KubLLC card → Move, not Hold → slack C0ADGSZKR3R/1770937232.664809: Arthur moves Metabase to his KubLLC card | R2 |
| C4 | A12 | slack C0ADGSZKR3R/1770927223.969899: 'pay SVB fully and close the credit card' — no date → trello 698f48be4ba0affafbf153db: card closes Feb 20; anything kept that charges again must move by Feb 19 → linear cmt_ec684ef632bdd6b375c3: Slack renews on the 3rd and Google Cloud charges on the 1st, both on the SVB card — before the Mar 12 review → gcal evt_f1d245d44ceff5a6e049c0: review call Mar 12 — holds that need no move stay until then | R4 |
| C5 | A15 | gdocs f_1326e66bcabfda8fd29e4a: rule 5: Closed only when the vendor itself confirmed → slack C0ADGSZKR3R/1770936655.574079: Arthur: 'coderabbit is cancelled'; 'cursor and … cancelled' → github harmonygames-Games/Combo-Fighters#38#c_1: CodeRabbit's own notice: subscription canceled Feb 12 → Closed → linear cmt_ed6dab8ad539165c22f1: Cursor: cancelled in the dashboard, no vendor word → Requested, renews the 5th | R3 |
| C6 | A16 | slack C0ADGSZKR3R/1770840054.486779: Arthur: 'yeah free version' (Slack downgrade) → slack C0ADGSZKR3R/1770933903.645709: Leonard to archive the Google accounts after Feb 15 → slack C0ADGSZKR3R/1770842405.931359: Leonard: keep only the three founders as paid Slack accounts, the rest as guests → gmail robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>: keep Slack on the paid plan; don't archive or delete any Google account → gcal evt_f1d245d44ceff5a6e049c0: no closing, downgrading or archiving before Mar 12 | R7 |
| C7 | A19 | linear cmt_5da8c3467fc022248fb3: owner figures in the issues: Unity 2,348.50, Slack 87.22, GitHub 90, BigQuery 4.97 (not the costs tab's stale December figures) → snowflake FIN-000687: AWS 1,485 (Jan), Meta 2,843.84, AppLovin 9.80 → gmail robert@harmonygames.co/<CAowZ1ukjS1ZxLCL4aRt1VM-c-GnNMTNWVQS47OM@mail.gmail.com>: annual/quarterly charges brought to a month (Figma 1,212/12, Singular 6,250/3) → gdocs f_1326e66bcabfda8fd29e4a: two totals: all rows today, Keep + Hold after the plan | R6 |

| Trap | Family | Records | Requirement | Expected wrong reading | Resolver | Discovery order |
|---|---|---|---|---|---|---|
| T1 | superseding | b9ef575bec54b095edb75a0fe83580f5, C0ADGSZKR3R/1770839729.441789, C0ADGSZKR3R/1770933601.686309 | R2 | keeps Gusto through the shutdown (Leonard's keep list) with a Feb 19 card move | Arthur's reply in the keep-list thread: docs pulled, renews Mar 1, cancel before the 1st → Cancel, Open, Feb 28 | the keep list is a top-level #winddown message every run reads; the reply only shows as reply_count 1 |
| T2 | superseding | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>, C0ADGSZKR3R/1770839825.928989, C0ADGSZKR3R/1770840054.486779 | R7 | plans the Slack downgrade to free (agreed Feb 11) without flagging it | Sunset's checklist (Feb 12 23:58Z) requires the paid plan with full history and every user in place until the review; the reply must name the downgrade and the cut to guest seats (C0ADGSZKR3R/1770842405.931359) | the downgrade agreement sits in the #winddown history the anchor points at; the checklist is in Gmail |
| T3 | superseding | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>, C0ADGSZKR3R/1770933903.645709 | R2 | puts Google Workspace down for archiving after Feb 15 (Leonard's action item) | Sunset: don't archive or delete any Google account before the review → Hold for Sunset; the archive plan is a clash to report | — |
| T4 | superseding | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>, robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com>, C0ADGSZKR3R/1770937232.664809 | R2 | holds Metabase for Sunset (first checklist) or leaves its card move open | the in-thread correction takes Metabase off the list; Arthur's issue comment confirms the KubLLC card → Move, dash | the first checklist names Metabase; the correction is the second message of the same thread |
| T5 | conclusion_stop | robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> | R2 | stops at the first checklist: cancels Trello (paid plan ended Nov 2025), dbt and BigQuery | the correction adds Trello, BigQuery and dbt → Hold for Sunset (Trello despite its pre-Feb-9 downgrade) | — |
| T6 | stale_summary | 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a, C0ADGSZKR3R/1770933999.157259 | R1 | treats Arthur's 40 issues as the complete account list | conventions rule 3 (ledger lines, shared costs-tab lines) add ElevenLabs, Meta Ads and AppLovin (UA); Pond5 ended Sep 2025 (rule 2) | Leonard's 'covers everything' and the project are met before the ledger or the costs tab |
| T7 | scope_alias | robert@harmonygames.co/<CAIoQDHYpNPHXVgnNS8DUmtr__81CmMffz7hcWJv@mail.gmail.com>, f_605121f4a36752645e0ac3 | R1 | one Sound row (or Soundly at $15) because the tab has one line | rule 1 + rule 8: one row per vendor account, each at its own charge — Soundly 10, ElevenLabs 50/12 (prepaid to Jul 9); Pond5 ended Sep 8 2025, so rule 2 leaves it out | — |
| T8 | eliminating_evidence | FIN-000688, FIN-000689, FIN-000699, FIN-000700 | R1 | no UA account on the register (no issue for it, Frederick left in October) | ledger marketing_ua rows in Jan and Feb: meta and applovin are still charging → two Cancel rows, usage-billed → Feb 28 | — |
| T9 | authority | 698f48be4ba0affafbf153db, C0ADGSZKR3R/1770927223.969899 | R4 | no card deadline (Slack never dates the closure) or the 2023 move onto the SVB card read as current | SVB card on the founders' board: closes Feb 20, move kept charging accounts by Feb 19 | a board search for 'SVB card' returns the 2023 'move subscriptions to SVB credit card' card in Done next to the payoff card in To Do |
| T10 | authority | robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>, robert@harmonygames.co/<CAS-TQ8VVR3eSFKWcX8_qppbQEILXpnhEbstiMuR@mail.gmail.com> | R2 | applies Sherwood's 'cancel every subscription now except payroll and accounting' | Sunset is the provider signed on Feb 12 (#winddown 1770931777.561519); Sherwood was not engaged | a mailbox search for 'checklist' returns Sherwood's (Feb 11) before Sunset's (Feb 12) in date order |
| T11 | authority | f_1326e66bcabfda8fd29e4a, page_ua_vendor_closeout | R6 | costs Meta Ads at trailing 30-day spend or treats it closed once spend reads $0 | the conventions doc governs the founders' register: last full month (January) from the ledger | — |
| T12 | reuse_exclusion | cmt_7cf5d70170f54a8f925f | R1 | two rows (QuickBooks and Intuit) or Canceled on the older issue | rule 1: one row 'Intuit QuickBooks' (invoice name); ENG-2461 (newer) is the duplicate → Canceled | — |
| T13 | near_miss_mention | harmonygames-Games/Combo-Fighters#38#c_1, cmt_ed6dab8ad539165c22f1, C0ADGSZKR3R/1770936655.574079, C0ADGSZKR3R/1770937188.477219 | R3 | Closed for CodeRabbit and Cursor because Arthur said they're cancelled (and Done in Linear) | rule 5: CodeRabbit's own notice on Combo-Fighters#38 (canceled Feb 12) → Closed; Cursor has no vendor word → Requested, Mar 4 | Arthur's 'cancelled' messages are in the #winddown history; the bot notice is on a PR |
| T14 | cross_reference_gap | evt_f1d245d44ceff5a6e049c0, robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | R4 | Hold rows with no date, Feb 15, or 'until Sunset confirms' | the review call Leonard booked is on Robert's calendar for 2026-03-12 → deadline for Linear, Figma, Trello, GitHub | — |
| T15 | synthesis_omission | cmt_96ae7b3689c1d073a2ff, robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com> | R4 | Helpshift deadline Feb 27 (export still pending) or no export check at all | Sunset asks for the Helpshift export before the subscription ends; Oliver's ENG-2439 comment says it was exported Feb 13 (helpshift_export_2026-02-13.zip) → Closed row gets a dash | — |
| T16 | unit_or_timezone | robert@harmonygames.co/<CAowZ1ukjS1ZxLCL4aRt1VM-c-GnNMTNWVQS47OM@mail.gmail.com>, cmt_e8ae507893bfdb06c8c7, cmt_4179664f58817a32a076, robert@harmonygames.co/1850283027022457279, f_605121f4a36752645e0ac3 | R6 | Singular at 6,250 or 0, Figma at 0 or 1,212, Carta/Docusign/Linear at their annual price | rule 8: quarterly ÷ 3 (2,083.33), annual ÷ 12 (Figma 101, Carta 321, Linear 152.72, Docusign 25, ElevenLabs 4.17); GitHub at its costs-tab line 86 | — |
| T17 | exact_predicate | 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a, f_1326e66bcabfda8fd29e4a, robert@harmonygames.co/1849420841999587093, robert@harmonygames.co/1854432461283937829 | R1 | keeps never-paid, one-off or pre-Feb-9 accounts, or drops Trello for its Nov 2025 downgrade | rule 2 exclusions (21 issues → Canceled) with the Sunset exception (Trello stays as a Hold) | — |
| T18 | superseding | ENG-2469, cmt_4179664f58817a32a076 | R5 | Leonard as Docusign's owner (the assignee) | Leonard's comment hands Docusign to Robert (rule 7) | — |
| T19 | distractor (already_done) | f_605121f4a36752645e0ac3, robert@harmonygames.co/1854432461283937829 | R1 | iPostal as a Cancel row at $34.79 (Dec-25 on the tab) | iPostal1 closed the mailbox on Jan 16 (Robert's mail) → cancelled before Feb 9 → excluded | — |
| T20 | distractor (partial_listing) | f_768cd23a00c4b12fa0e975 | R1 | uses Arthur's 18-row 'Subscriptions' sheet (rounded figures) as the list | the project description says it replaces that sheet | — |
| T21 | distractor (non_authoritative_instruction) | fda86aac9fb55c96ffee4bba3e59cc14 | R2 | keeps Cursor for Oliver | Oliver asks; the founders cancelled it (Feb 11 list, Arthur Feb 12) → Cancel | — |
| T22 | distractor (scope_adjacent) | robert@harmonygames.co/1853470745017478863, robert@harmonygames.co/1850283027022457279 | R4 | Singular deadline Mar 14 (the past-due extension to Mar 15) | Mar 15 is the due date of the overdue balance; the next quarterly invoice is Mar 1 (Sep 1, Dec 1) → Feb 28 | — |
| T23 | distractor (keyword_collision) | C0ADGSZKR3R/1770673467.186629 | R6 | Helpshift at $1,500 / $300 (balances owed) instead of its monthly 150 | rule 8: Leonard's ENG-2439 comment gives $150 a month | — |
| T24 | distractor (stale_summary) | page_aws_infra, FIN-000687 | R6 | AWS at ~$1,550 (page) or ~$1k (Arthur's DD prod estimate) or 0 (tab) | rule 8: a cloud account with its own ledger line takes its January line (FIN-000687, 1,485); Arthur's issue comment gives the same 1,485 | — |
| T25 | distractor (stale_summary) | cmt_5da8c3467fc022248fb3, cmt_ec684ef632bdd6b375c3, f_605121f4a36752645e0ac3 | R6 | costs read off the costs tab's December figures (Unity 2,172, Workspace 316.56, Slack 129.50, BigQuery 14.33, GitHub 86) | rule 8: the owner's monthly figure in the issue (Unity 2,348.50, Slack 87.22, BigQuery 4.97, GitHub 90) or the account's own last invoice (Workspace 298.13, Feb 2) | — |

**Trap independence.** T1 (thread reply), T5/T4 (mail-thread correction), T8 (ledger), T9 (Trello), T13 (GitHub notice), T14 (calendar), T15 (Confluence comments) and T7 (shared costs line) each need a different read; a run that has beaten all the others still fails each one it skips. T4 and T5 fall to the same reply and are counted as one discovery in §6. No record states a conclusion: the SVB card never lists accounts, the checklist never names a deadline, the review event never mentions holds, and no comment says 'Closed' or 'Requested'.

## 6 Failure-diversity plan

Douglas's lessons (memory, 2026-10-27): every hidden fact must decide two or more rubric rows; levers must be independent ~50% habits, not one 'deep reader' trait; never hide a fact on the ask itself; project with `difficulty_stats.py` on an atomic, work-weighted rubric.

| Discovery (lever) | Habit it tests | Rows it decides | Expected find rate |
|---|---|---|---|
| D1 Sunset's correction (K4, in-thread reply) | opening the second message of a mail thread | Trello, dbt, BigQuery, Metabase action; dbt/BigQuery deadline; T2 | ~0.5 (Gmail get_thread 1/6–5/6 in Douglas) |
| D2 Gusto reply (K9, Slack thread) | opening a thread on a message the run already read | Gusto action, status, deadline; total after | ~0.5–0.7 (reply_count 1 on a key message) |
| D3 ledger UA lines (T8) | opening Snowflake on a doc's instruction | Meta Ads and AppLovin rows (membership, cost, deadline); total today | ~0.4 (Snowflake 46/131) |
| D4 SVB card on Trello (H2) | searching Trello for a named rule | six Keep/Hold Feb 19 deadlines | ~0.5 (Trello 50/131) |
| D5 review call date (K5, GCal) | opening Calendar for a referenced meeting | five Hold deadlines (Mar 12) | ~0.3–0.5 (Calendar 5/131, but the mail names the call) |
| D6 CodeRabbit notice (GitHub) | looking for a bot confirmation outside mail | CodeRabbit status/deadline; Done vs open | ~0.3 |
| D7 Confluence comments (T15) | listing page comments | Helpshift deadline | ~0.25 (Douglas: 2/6, 1/6) |
| D8 Sound line split (T7) + Pond5/ElevenLabs mail | reading a costs line as several accounts | two rows, Soundly cost, total today | ~0.5 |
| D9 rule 5 per record (A15) | applying a house rule against 'cancelled' claims | Layer, Cursor, Unity, Singular status | ~0.6 |

No single discovery decides more than ~15% of the register's cells; D1 and D3 each touch both totals, so the totals rows fail for different reasons in different runs. Expected shape: no run finds all nine; typical runs find 4–6, so the failing sets differ on several rows (≥ 2 failure patterns, largest ≤ 50%). Predicted average ~62–70% before the rubric exists; the rubric stage must replay `difficulty_stats.py` against this lever table, as Douglas round 3 showed.

## 7 Deliverables and dependent writes

| Write | Service · tool | Content depends on | Requirements |
|---|---|---|---|
| W1 | gsheets · gsheets_create_spreadsheet + gsheets_values_update ×2 | K2, K3, K4, K5, K6, K7, K8, K9, K10, K11, K12, C1 … | R1, R2, R3, R4, R5, R6 |
| W2 | gdrive · gdrive_share_file ×2 | A1 | R8 |
| W3 | linear · linear_update_issue + linear_create_comment ×70 | K2, K7, T12, T13, T17, C5 | R9 |
| W4 | linear · linear_create_issue ×3 | C1, C2, T6, T7, T8 | R9, R1 |
| W5 | slack · slack_post_message (thread reply) ×1 | C6, C7, T2, T3 | R7 |

- W1: one register sheet in Robert's Drive (28 rows: account, action, status, deadline, owner, monthly cost) with the two totals (11,045.13 / 1,249.04). The Wind Down folder is not writable or readable for Robert (owner 'Resource: …', empty share list), so A1 asks for sharing, not a folder.
- W2: shared with leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co as writers.
- W3: Done on ENG-2439, ENG-2440, ENG-2474, ENG-2476, ENG-2478; Canceled on the 20 excluded issues; the 20 other issues stay open; one comment on each of the 47 (what happens, by when).
- W4 (reuse vs create, A8): new issues in the project for ElevenLabs, Meta Ads, AppLovin (UA) — Soundly's issue is not reused for Pond5/ElevenLabs (one issue per vendor).
- W5: a reply in Leonard's thread with both totals and the three clashes (Slack downgrade to free; cutting Slack to three paid seats and guests; archiving Google accounts after Feb 15) against Sunset's hold until Mar 12.

## 8 Service role map

| Service | Role | Load-bearing fact / write | Carrier |
|---|---|---|---|
| slack | anchor A1 in #winddown (Leonard → Robert); base keep list, action items, Arthur's LLC-card move, the Slack free-plan decision and the 'P&L covers everything' claim; Arthur's Gusto reply in the keep-list thread; reply destination | the ask, the keep list and its amendment (Gusto → cancel), the LLC moves and both clashes exist only in #winddown; the reply write lands there | ● |
| gmail | authority H1 (Sunset's data checklist + its in-thread correction); Sherwood decoy; vendor billing mail through the billing group (next charge dates, Soundly's confirmation, Pond5's end notice, ElevenLabs receipt, iPostal closure, Singular invoices and termination thread) | which accounts are held for Sunset, the next-charge dates behind most deadlines and the only vendor confirmation for Soundly live only in Robert's mailbox | ● |
| linear | cohort: the 45 issues of the 'Shutdown – accounts' project; per-issue comments (status, owner handover, billing notes); write targets (state, comment, 3 new issues) | membership starts from the project; per-issue comments decide status/owner/deadline for an unpredictable subset; R9 writes | ● |
| trello | authority H2 'SVB card payoff + closure' on the founders' board; same-board 2023 'move subscriptions to SVB credit card' decoy (base #170) | the Feb 19 card-move deadline for every Keep row and every Hold row that charges before the review call exists only on that card | ● |
| gdocs | authority H3 'Close-out register conventions' in the Wind Down folder | exclusions, the ledger check, status vocabulary, deadline and cost rules and both totals | ● |
| gdrive | Wind Down folder holds the conventions doc; Arthur's superseded 'Subscriptions' sheet (decoy); sharing write for the register | R8: the register must be shared with Leonard and Arthur as editors | ● |
| gsheets | January P&L 'HG Costs' tab — the cost lines Arthur's project came from (rule 3); 'Sound (Pond5, Soundly,Elevenlabs)' and 'UA' lines hide several accounts; its December figures are stale (cost decoy); register write | membership: the shared Sound and UA lines hide accounts the project lacks | ● |
| snowflake | FINANCE_LEDGER Jan/Feb lines: meta and applovin UA charges (rule 3 membership, rule 8 cost for cloud/ad-spend accounts with their own ledger line: AWS, meta, applovin) | Meta Ads and AppLovin (UA) are still charging and are absent from the P&L and the project; their monthly cost is their January ledger line | ● |
| gcal | 'Sunset – data delivery review' (Mar 12, 2026) on Robert's calendar | the deadline for every Hold row that does not have to move cards | ● |
| confluence | Growth/UA close-out conventions decoy page; base page_aws_infra (stale AWS estimate) | whether Helpshift still has an export pending before Feb 28 (its deadline) is only in the page comments | ● |
| github | CodeRabbit's subscription notice on Combo-Fighters#38 | the only vendor confirmation that CodeRabbit is cancelled (Closed vs Requested) | ● |
| contacts | not used | no vendor contacts exist; no write needs an address beyond the two founders | — |
| gslides | not used | the BoD Jan 14 deck (f_65ada5e24989d256cabdfa) has no vendor list; nothing graded | — |

Carriers: Linear comments ● (Ask_Carriers §6b), Gmail bodies ●, Trello card desc ●, Docs body ●, Slack messages ●, Confluence comments ●, GitHub PR comments ●, Sheets cells ●, Snowflake rows ●. No load-bearing fact sits in a GCal description, Slides notes or Drive `content_text` (○): the review event's load-bearing field is its start time.

## 9 Call budget

| Phase | Service | Calls | Necessity |
|---|---|---|---|
| discovery | slack | 4 | read the ask and the #winddown history it points at (2 pages), the keep-list thread replies, one search for Arthur's LLC message |
| discovery | linear | 3 | find the 'Shutdown – accounts' project, read its description, list its 46 issues |
| rules | gmail | 3 | search for Sunset's checklist, read the thread (checklist + correction), search for SVB's terms (none in mail) |
| rules | trello | 3 | search the boards for the SVB terms, open the card, read its description |
| rules | gdocs | 2 | find and read the conventions doc |
| rules | gdrive | 1 | search Drive for the doc Leonard named by title (the Wind Down folder itself is not shared; its files are) |
| rules | gcal | 2 | find the review call Sunset's mail refers to and read its date |
| enumeration | gsheets | 2 | find the January P&L and read the HG Costs tab |
| enumeration | snowflake | 3 | find FINANCE_LEDGER, read its columns, query the Jan/Feb lines |
| per-record | linear | 45 | linear_list_comments on each of the 45 issues: a decisive comment sits on an unpredictable 29 of them |
| per-record | gmail | 8 | the billing mail in Robert's own mailbox: Figma, Layer, Pond5, Soundly, Workspace, ElevenLabs, Singular, iPostal (the other accounts' billing facts are in their Linear comments) |
| per-record | linear | 70 | settle each issue: 25 state changes (5 Done, 20 Canceled) and one comment on each of the 45 |
| reconciliation | github | 2 | look for CodeRabbit's own word (search PR comments by the bot, read #38's comments) |
| reads-before-writes | linear | 2 | workflow state ids and the project id needed by the writes |
| writes | gsheets | 2 | create the register and write its 28 rows and two totals |
| writes | gdrive | 2 | share the register with Leonard and with Arthur as editors |
| writes | linear | 3 | a new issue in the project for each added account |
| writes | slack | 1 | reply in Leonard's thread with the totals and the clashes |

**Total 158**, all unconditional; 11 services; largest share outside the per-record phase 25% (Linear). Golden-run rule: a correct run must open each issue's comments, settle each issue and find each billing account's receipt; decoy reads, read-backs and repeated searches are not counted. Measured runs add discovery searches on top (Douglas: +17% to +71% over budget).

## 10 QC rails

### Two-reading table

| Decision point | Best reading | Strongest alternative | Resolved by |
|---|---|---|---|
| Trello: excluded (paid plan ended Nov 21) or held | Hold for Sunset, cost 0, Mar 12 | out: cancelled before Feb 9 (robert@harmonygames.co/1849420841999587093) | rule 2 exception + correction robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> (newer, names Trello) |
| Metabase: Hold (first checklist) or Move | Move to Arthur's LLC, dash | Hold for Sunset (robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>) | correction robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> removes it; Arthur's comment on ENG-2456 confirms the KubLLC card |
| GitHub: Move (Arthur's LLC message) or Hold | Hold for Sunset, Mar 12 (already off the SVB card) | Move to Arthur's LLC (C0ADGSZKR3R/1770937232.664809) | rule 4: Sunset's list wins over everything above |
| Gusto: Keep or Cancel | Cancel, Open, Feb 28 | Keep (C0ADGSZKR3R/1770933601.686309) | newer reply in that thread (C0ADGSZKR3R/1770948876.205117) incorporated by A1 'the replies under it' |
| CodeRabbit: Closed or Requested | Closed (vendor's notice) | Requested (only Arthur's word in Slack) | harmonygames-Games/Combo-Fighters#38#c_1 is CodeRabbit's own notice; rule 5 lists 'an in-app or bot notice' |
| Singular deadline: Feb 28 or Mar 14 | Feb 28 (next quarterly invoice Mar 1) | Mar 14 (extension to Mar 15) | Mar 15 is the overdue balance's due date (robert@harmonygames.co/1853470745017478863); invoices Sep 1 and Dec 1 (robert@harmonygames.co/1850283027022457279) fix the quarterly cycle |
| Helpshift deadline: dash or Feb 27 | dash (export done) | Feb 27 (export pending before Feb 28) | cmt_96ae7b3689c1d073a2ff (Oliver, Feb 13) logs the export; rule 6 dash |
| Figma deadline: Feb 19 or Mar 12 | Mar 12 | Feb 19 (card on file is the SVB card) | robert@harmonygames.co/<CAowZ1ukjS1ZxLCL4aRt1VM-c-GnNMTNWVQS47OM@mail.gmail.com>: next charge Sep 11, 2026 ($1,212 annual, tab Sep-25) — after the review call; rule 6 'won't charge it again before Sunset's review call' |
| Meta Ads cost: Jan 2,843.84, Feb 956.45, the UA line 610 or 30-day spend | 2,843.84 | 610 (UA line on the costs tab) / 956.45 (last ledger line) / trailing 30-day (UA page) | rule 8: the UA line is shared by two accounts → own last full month (January) in the ledger; UA page scoped to the Growth/UA tracker |
| Docusign owner: Leonard or Robert | Robert | Leonard (assignee) | rule 7 + Leonard's comment cmt_4179664f58817a32a076 handing it over |
| Clashes to report: which | Slack free plan; Slack cut to three paid seats + guests; Google archiving after Feb 15 | also Metabase/GitHub moves, Gusto | the three decided steps Sunset's hold forbids (C0ADGSZKR3R/1770840054.486779, /1770842405.931359, /1770933903.645709); card moves close nothing; extras are accepted, the three are the minimum |
| Confluence: on the register | Hold for Sunset, cost 0, owner Robert | out (never billed; not in the project) | Sunset's list (robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>) + rule 2 exception; rule 8 'accounts that have never charged us are 0' (no Atlassian charge in Robert's mail); rule 7 'anything you add is yours' |

### Reach table (load-bearing records)

`python3 Task_Authoring/tools/persona_view.py can-see robert <service> <id>` for every scoped base record the design leans on (all YES); seeded records are planned in Robert's mailbox / calendar / shares and are checked by `check-sql` at the injection gate.

| Record | Service | can-see robert | Reason |
|---|---|---|---|
| C0ADGSZKR3R/1770933601.686309 | slack | YES | member of private #winddown |
| C0ADGSZKR3R/1770933903.645709 | slack | YES | member of private #winddown |
| C0ADGSZKR3R/1770933999.157259 | slack | YES | member of private #winddown |
| C0ADGSZKR3R/1770937232.664809 | slack | YES | member of private #winddown |
| C0ADGSZKR3R/1770936655.574079 | slack | YES | member of private #winddown |
| C0ADGSZKR3R/1770937188.477219 | slack | YES | member of private #winddown |
| C0ADGSZKR3R/1770839729.441789 | slack | YES | member of private #winddown |
| C0ADGSZKR3R/1770839825.928989 | slack | YES | member of private #winddown |
| C0ADGSZKR3R/1770840054.486779 | slack | YES | member of private #winddown |
| C0ADGSZKR3R/1770927223.969899 | slack | YES | member of private #winddown |
| C0ADGSZKR3R/1770673467.186629 | slack | YES | member of private #winddown |
| C0ADGSZKR3R/1770931777.561519 | slack | YES | member of private #winddown |
| robert@harmonygames.co/1853470745017478863 | gmail | YES | own mailbox |
| robert@harmonygames.co/1850283027022457279 | gmail | YES | own mailbox |
| robert@harmonygames.co/1854432461283937829 | gmail | YES | own mailbox |
| robert@harmonygames.co/1849420841999587093 | gmail | YES | own mailbox |
| robert@harmonygames.co/1856956532017091340 | gmail | YES | own mailbox |
| f_605121f4a36752645e0ac3 | gsheets | YES | shared with robert@harmonygames.co |
| evt_212e50fb5a53ea8016ce29 | gcal | YES | Robert's calendar (Sunset call context) |
| f_1326e66bcabfda8fd29e4a (planned) | gdocs | planned | shared with robert@harmonygames.co like its Wind Down siblings f_31115ddb6ed866f2b10d60 |
| evt_f1d245d44ceff5a6e049c0 (planned) | gcal | planned | Robert's own calendar copy |
| robert@harmonygames.co/1856965916492026238 (planned) | gmail | planned | Robert cc'd; copy in his mailbox |

Unscoped and always readable: Linear, Trello, Confluence, GitHub, Snowflake. The Wind Down folder itself is not readable by Robert and is not load-bearing (the doc is found by title).

**Feasibility.** Writes in `Evals/references/tools/catalog.json`: `gsheets_create_spreadsheet`, `gsheets_values_update`, `gdrive_share_file` (role writer), `linear_update_issue` (state), `linear_create_comment`, `linear_create_issue` (project), `slack_post_message` with `thread_ts`. Robert owns the sheet he creates; Linear is unscoped; he is a #winddown member. Values observable to the cent in the tab, the ledger and the receipts.

**Explicit rules.** Temporal comparison: newer replies amend (A1 'the replies under it'; Sunset 'we'll reply on this thread'). Duplicates: rule 1 (newer issue). 'Now': clock Feb 14; deadlines are future dates. Write end states: Done / Canceled / open per K2. Every cross-reference postdates its target: A1 (Feb 13 17:21Z) after the doc (16:38Z), the card (15:52Z) and the project (Feb 12 23:24Z); the checklist (Feb 12 23:58Z) after the review event it calls booked (created Feb 12 22:40Z) and after the signing (21:29Z); the correction (Feb 13 18:20Z) after the checklist.

**Precedence.** Every load-bearing fact is in a ● carrier (Ask_Carriers §5 as amended by §6b).

**Prompt naturalness.** The trigger names the anchor in plain words (Leonard's close-out register ask), the deadline (before Leonard archives the Google accounts) and the deliverables (register, Linear, reply). It must not name Sunset's list contents, the SVB date, the Trello board, the ledger, the Sound line, any account, the review date or the totals.

**Grading devices.** Exact set of 28 account rows; per-column spot checks (≤ 5 per group) + a volume row; the two totals; Linear exact sets (4 Done, 21 Canceled, 5 new); one row per share target; the reply's three clashes (extras such as the GitHub card move accepted). Hidden-fact rows at weight 5; avoid always-pass per-issue rows (Douglas round 3).

## 11 Record plan for /create-injection

| Table | Rows | Ids | Notes |
|---|---|---|---|
| slack.slack_messages | 3 (+1 UPDATE parent counters) | b9ef575bec54b095edb75a0fe83580f5, fda86aac9fb55c96ffee4bba3e59cc14, 9e245e76cbaf7f080e1995ec0c4ec30d | ts 1770948876.205117, 1770976938.774231, 1771003267.448213; reply thread_ts 1770933601.686309 |
| gmail.gmail_threads / gmail_messages | 13 messages | Robert copies e.g. robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>; Leonard/Arthur copies of Sunset ×2 and Sherwood | sender tokens PERSON_7731 (Sunset), PERSON_0728 (Sherwood), SVC_77nn new vendors |
| linear.linear_projects (+project_teams) | 1 | 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a | team_ENG, lead usr_cc3e90160f490686, created 2026-02-12T23:24:10Z |
| linear.linear_issues | 47 | ENG-2438…ENG-2484 | creator Arthur, created 2026-02-12T23:24:13Z… (17 s apart), states Todo |
| linear.linear_comments | 39 | cmt_ + 20 hex (`minted_ids.json` L_ISSUES) | authors Arthur, Leonard, Robert, Oliver at their Feb 12–13 times |
| trello.trello_cards + actions | 1 + 1 | 698f48be4ba0affafbf153db | createCard action 698f48be304fbb37e4e3aafa |
| gdrive.drive_files + gdocs.docs_documents | 1 | f_1326e66bcabfda8fd29e4a | parent d_e5caf6a8c630421942ee59, owner Resource token, shared with the three founders |
| gdrive.drive_files + gsheets.sheets_spreadsheets | 1 | f_768cd23a00c4b12fa0e975 | Arthur's 'Subscriptions' (Feb 10), shared with Leonard and Robert |
| gcal.gcal_events | 3 | evt_2ac66383ee72bbb05a0376, evt_f1d245d44ceff5a6e049c0, evt_d1fe12afe85ffbb49bd998 | ical a8690ec17cab7912257b3b1b2b9fcbef@hg4, 2026-03-12 17:00–17:45Z |
| confluence.confluence_pages (+versions) | 1 + 1 | page_ua_vendor_closeout | UA page by user_EMPLOYEE_0008 2025-03-18 (before the Oct 2025 deactivation notice; decoy only) |
| github.github_pull_requests / pr_comments | 1 + 1 | harmonygames-Games/Combo-Fighters#38, harmonygames-Games/Combo-Fighters#38#c_1 | open PR by Oliver Feb 13 09:38Z; CodeRabbit notice 09:41Z |

### Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| github | INT-01 | Slack mirror of PR comments | none: Combo-Fighters is not a mirrored repo (INT-01 covers GameOfDominoes, game-of-dominoes-backend, match3d) |
| github | INT-23 | CodeRabbit comment author PERSON_6026_GITHUB_USERNAME + timeline actor SVC_0321 | seeded with the base author token; no review row (review skipped) |
| github | INT-12 | GitHub notification mail per PR | none: Robert is not a Combo-Fighters participant; no mail seeded (integration_exceptions at injection if base_check asks) |
| linear | INT-03 | linear[bot] PR comment | none: no PR names an ENG-24xx key |
| linear | INT-04 | Linear Slack app posts | none: the ENG team posts to no Slack channel in 2026 |
| linear | INT-05 | Linear e-mail digests | none: digests are not seeded for one day of activity |
| gcal | INT-11 | invitation mails | none: no_notify (integration_exceptions) |
| slack | INT-22 | Slack e-mail notifications | none: Robert is active in Slack; no notification mail |
| gmail | none | — | gmail: no integration sources from Gmail; seeded threads get gmail_label_user_counters bumps |
| trello | INT-21 | Trello → Slack | none: no integration exists |
| gdrive | INT-13 | Drive Slack app DMs | none: the doc is shared without a Slack notification |
| confluence | none | — | confluence: no integration; page version row seeded with the page |
| gsheets / gdocs | none | — | gsheets: the decoy sheet and the doc get drive_files rows with the same sharing |

## 12 Self-test results

`python3 Task_Authoring/tools/hardness_gate.py Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.draft.json --design` (verbatim):

```
HARDNESS GATE (long (design)): PASS
  [ok] effective_profile: effective_profile 'long' for 'Long Horizon' → thresholds 'long'
  [ok] sql_lint_clean: skipped (--design: no SQL yet)
  [ok] base_consistency: skipped (--design: no SQL yet)
  [ok] services_injected: skipped (--design: no SQL yet)
  [ok] rows: skipped (--design: no SQL yet)
  [ok] services_carrying_weight: 11 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: skipped (--design: no SQL yet)
  [ok] seeded_ids_exist_in_sql: skipped (--design: no SQL yet)
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
  [ok] supersession_chronology: skipped (--design: no SQL yet)
  [ok] distractors: 7 distractors of 6 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 7 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 7 chains with 7 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] hidden_authorities: 3 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 2 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 19 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 9 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 5 writes over 4 services; each must depend on findings
```

**Lazy-solver pass** (one broad search per service, first hits only, no thread or reply opened, stops at the first
conclusion, every bulk shortcut used):
- Slack: reads the anchor and the #winddown history page → keep list, action items, 'covers everything', LLC moves,
  'cancelled' claims. Gets Deel/Intuit Keep, Metabase Move, most Cancel actions right. Misses the Gusto reply
  (thread, `C0ADGSZKR3R/1770948876.205117`) → Gusto wrong in action, status, deadline and the after-plan total.
- Linear: `linear_list_issues` on the project → 48 titles, assignees, description. Never lists comments → wrong owner for
  Docusign (ENG-2469), wrong in/out for OpenAI/Typecast/Adobe/JetBrains/Solsten (ENG-2441, ENG-2442, ENG-2450, ENG-2447,
  ENG-2453), wrong status for Unity/Layer/Singular, and Metabase/GitHub/dbt card state unknown.
- Gmail: one search 'checklist' → Sherwood's (Feb 11) and Sunset's (Feb 12) first messages. Reads the first hit only →
  either Sherwood (cancel everything) or Sunset v1 (Metabase held, Trello/dbt/BigQuery cancelled). Never opens the
  thread's second message. No per-vendor receipt search → no next-charge dates: every Cancel deadline guessed.
- Trello / Calendar / Confluence / GitHub / Snowflake: a lazy run opens none of them → no Feb 19 card deadline, no Mar 12
  hold date, Helpshift export unknown, CodeRabbit Requested, Meta Ads/AppLovin missing.
- Sheets: reads the costs tab → Dec-25 costs right for the tab rows only if it reads column AF (the header dates are a year off — the trap row in §10); one Sound row; iPostal kept at 34.79.
- **Leaks found and fixed in this design:** (1) the review event was first minted after the checklist that calls it
  booked — moved to Feb 12 22:40Z (§10 Explicit rules); (2) the project description first carried 'vendor has confirmed'
  in its Done rule, which would have put the A15 house rule in the most-read record — removed, Done now says 'once the
  account is closed' and rule 5 defines closed; (3) the SVB card text first asked to 'put the new card next to it in the
  register', a manufactured column — removed; (4) the blanked '[PERSON_NAME_20852]' and '[USERNAME_30019]' vendors in
  #winddown left a second reading of membership — Leonard's base subscriptions table (C0ADGSZKR3R/1770933450.410449) names Kapwing (ENG-2478) and Arthur's ENG-2457 comment states dbt's KubLLC move (an invented Notion/Sentry mapping was removed at the /injection review, F2). Review fixes (§13) removed the remaining cues ('nothing back yet', billing days in comments, exact costs in Arthur's sheet). What the lazy run still scores: Keep/Move actions, the tab costs if it picks column AF, the exclusions it can
  read from the tab (Veed, Kling, Hailuo zeros), the share and the reply's existence — about 30–40% of the weight.

**Literal-value sweep** (each decisive value searched across the seeded wording in `planned_text.json` and the base):
'Feb 19' / 'Feb 20' appear only in the SVB card (`698f48be4ba0affafbf153db`); no seeded record carries a card number; 'March 12' / '2026-03-12' only in the event start (no mail subject, no_notify);
'Trello is part of the bundle' / 'keep BigQuery and dbt' only in the correction (`robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com>`); 'on the 3rd' (Gusto)
only in the thread reply; meta/applovin amounts only in Snowflake (FIN-000688/FIN-000689/FIN-000699/FIN-000700); the
Sound line split only in the costs tab and the Pond5/ElevenLabs mails; 'canceled on Feb 12' only on Combo-Fighters#38 (matching CodeRabbit's base notice to Arthur). No
base record carries these values (`hg.py search` 'Feb 19', 'data delivery', 'KubLLC card', 'Shutdown – accounts': only
the base C0ADGSZKR3R/1770937232.664809 for KubLLC).

**Wording sweep.** Rule 5's decisive words ('confirmed', 'Closed', 'Requested') appear in no seeded comment or receipt;
cancellation mails say 'has been cancelled/canceled' (vendor voice), founders say 'cancelled' (our voice) — the rule, not a
keyword, separates them. Sunset's list never says 'Hold'; the SVB card never names an account; no comment says 'Keep'.

**"The rest stands" check.** After K9 (Gusto) no record re-asserts 'keep gusto'; after K4 (Metabase out) no record
re-asserts Metabase on the list (searched 'gusto', 'metabase' over `planned_text.json`; base mentions are older:
C0ADGSZKR3R/1770933601.686309, /1770937232.664809).

### Self-review

Walked against `Evals/1_Prompt_Eval.md` §2.1 (Unique Ground Truth), §2.2 (Feasibility), §3.2 (Cross-Service Coherence)
and `Evals/0_Injection_Quality_Eval.md` Check C, in that order. Every base value below was re-read through `tools/hg.py` /
the export (`persona_view` for reach); planned values come from `planned_text.json` and `truth.json` (emitted, not typed).

| # | Item | Counter-reading (strongest case it FAILS) | Resolution with evidence |
|---|---|---|---|
| 1 | temporal | A seeded record refers to something that did not exist yet (the checklist calls the review call 'booked') | fixed: event created 2026-02-12T22:40:15Z (`minted_ids.json` E_REVIEW) before the checklist 23:58:21Z, after the SOW signing C0ADGSZKR3R/1770931777.561519 |
| 2 | semantic | 'Closed' could mean 'we cancelled it' (Arthur's 'coderabbit is cancelled', C0ADGSZKR3R/1770936655.574079) | rule 5 in `planned_text.json` DOC_CONV defines Closed as vendor-confirmed and lists the carriers; the counter reading is the designed A15 trap T13 |
| 3 | cross-service referential | the redacted vendor names in #winddown (C0ADGSZKR3R/1770839715.391309, /1770937232.664809) point at accounts no issue covers | Leonard's table C0ADGSZKR3R/1770933450.410449 names Kapwing (ENG-2478); dbt's move is in Arthur's ENG-2457 comment; the costs tab's '[PERSON_NAME_0499]' is Singular (trap_catalog X03) |
| 4 | quantitative | Helpshift's monthly cost could be read as $1,500 / $300 (C0ADGSZKR3R/1770673467.186629, hazard Q07) | rule 8 reads column AF (150, f_605121f4a36752645e0ac3 row 10); balances are owed amounts, not a month |
| 5 | quantitative | AWS cost: the tab says 0, Confluence page_aws_infra ~$1,550, Arthur ~$1k | rule 8 fallback (revised at /prompt): tab 0 → the owner's figure in ENG-2455 (1,485; Arthur: the P&L line was never kept up), matching FIN-000687 |
| 6 | state/lifecycle | Trello's paid plan ended Nov 21 (robert@harmonygames.co/1849420841999587093), so rule 2 drops it | rule 2's exception ('anything on Sunset's list goes on the register whatever else applies') + the correction naming Trello |
| 7 | state/lifecycle | Singular could be Closed: Leonard terminated it on Feb 12 (robert@harmonygames.co/1853470745017478863) | the same message asks Singular to 'confirm in writing'; no reply exists before the clock → Requested |
| 8 | identifier/format | the conventions doc's owner 'Resource: 7240535625619857401' is not an email (hazard I14) | it is the owner of every Wind Down sibling (f_31115ddb6ed866f2b10d60); Robert reads it through its share list |
| 9 | other | 'Sunset' is redacted in Slack ([USERNAME_26907], C0ADGSZKR3R/1770931777.561519), so Sherwood could be the provider | the signed SOW mail robert@harmonygames.co/1856956532017091340 names Sunset; Sherwood's mail says 'If you decide to engage us' |
| 10 | two-reading: Trello | best argument it is out: cancelled before Feb 9 | resolved in §10 row 1 (correction `robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com>`, rule 2 exception) |
| 11 | two-reading: Metabase | best argument it is a Hold: the first checklist names it | §10 row 2: correction removes it; ENG-2456 comment confirms the KubLLC card |
| 12 | two-reading: GitHub | best argument it is a Move (Arthur's LLC message C0ADGSZKR3R/1770937232.664809) | rule 4 'Sunset's list wins over everything above' → Hold, Mar 12 |
| 13 | two-reading: Gusto | best argument it stays Keep (C0ADGSZKR3R/1770933601.686309) | the later reply `C0ADGSZKR3R/1770948876.205117` in that thread, incorporated by A1's 'the replies under it' |
| 14 | two-reading: CodeRabbit | best argument it is Requested: no mail from CodeRabbit | rule 5 accepts 'an in-app or bot notice'; harmonygames-Games/Combo-Fighters#38#c_1 is the vendor's own |
| 15 | two-reading: Singular deadline | best argument for Mar 14: the extension to Mar 15 | Mar 15 is the overdue balance's due date (robert@harmonygames.co/1853470745017478863); invoices Sep 1, Dec 1 (robert@harmonygames.co/1850283027022457279) → Mar 1 → Feb 28 |
| 16 | two-reading: Helpshift deadline | best argument for Feb 27: export pending | comment_support_after_helpshift_c1 on page_support_after_helpshift logs the export and the switch-over Feb 13 |
| 17 | two-reading: Figma deadline | best argument for Feb 19: the SVB card is on file | `robert@harmonygames.co/<CAowZ1ukjS1ZxLCL4aRt1VM-c-GnNMTNWVQS47OM@mail.gmail.com>` next charge 2026-09-11, after the Mar 12 review → rule 6 'won't charge it again before Sunset's review call' |
| 17a | two-reading: costs-tab column | best argument for column AR: its header reads 2025-12-26 | rule 8 names column AF by position; HG P&L's Dec-25 (header 2025-12-25) is column AF; subtotals tie (UA 610) |
| 18 | two-reading: Meta Ads cost | best argument for 956.45 (last ledger line, FIN-000700) or trailing 30 days (page_ua_vendor_closeout) | rule 8 'last full month in the ledger (January)' → FIN-000689 2,843.84; the UA page is scoped to the Growth/UA tracker |
| 19 | two-reading: Docusign owner | best argument for Leonard (assignee of ENG-2469) | rule 7 + Leonard's handover comment on ENG-2469 |
| 20 | two-reading: clashes | best argument the GitHub/Metabase card moves or Gusto also clash | card moves close nothing; the three that Sunset forbids are C0ADGSZKR3R/1770840054.486779 (free plan), /1770842405.931359 (guest seats), /1770933903.645709 (archive); extras accepted |
| 21 | two-reading: Confluence | best argument it is out: never billed, not in the project | Sunset's list names it (`robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>`), rule 2 exception, rule 8 'never charged us are 0', rule 7 owner Robert |
| 22 | feasibility | Robert cannot write into the Wind Down folder (d_e5caf6a8c630421942ee59, persona_view NO) | A1 asks for a shared sheet, not a folder; Robert owns what he creates and shares it (gdrive_share_file) |
| 23 | difficulty | the levers might all reward one 'deep reader' trait (Douglas round 2, SD collapse) | §6: nine levers in seven services with different habits (thread reply, mail thread, Trello, Calendar, Snowflake, PR bot comment, page comments); rubric must be replayed with `difficulty_stats.py` |

Expected baseline metrics (to be measured, never assumed): errored runs 0 of 6 expected (no forced errors; Friction: none);
pass@1 0 of 6 expected (no run expected to find all nine levers); average ~62–70% before the rubric is modelled; SD
0.1–0.3 if levers stay independent; ≥ 2 failure patterns with the largest ≤ 50%; horizon basis = rollout mean, budget
158 → expected counted calls ~185–260 (Douglas ratio), every run above the author's 150 floor if each issue is settled.

Gate output pasted above (HARDNESS GATE (long (design)): PASS). Re-verified base values: P&L Dec-25 column AF
(f_605121f4a36752645e0ac3 HG Costs rows 2–73, re-read after review A #1), ledger FIN-000686…FIN-000704, #winddown timestamps (C0ADGSZKR3R/2026-02.json),
Robert's mail 00016283/00016086/00016395/00016044/00016902 (thread ids in §1), persona_view can-see (§10 Reach table).

Unresolved: (1) Linear comment rendering of injected comments is verified (Ask_Carriers §6b) but `linear_list_comments` per
issue vs a hypothetical bulk path must be confirmed in the Opus pre-check; (2) whether runs open the review event (Calendar
5/131) — the mail names the call, so the fact is reachable, but the find rate is unmeasured; (3) the rubric's atomic
weighting decides the average — projection deferred to `/create-rubric-writing`.

```
STAGE GATE scenario: PASS — Task_Authoring-2/task_inputs · 01_Scenario_Design.md#8f37cbc35bf2 · 01_Hardness_Manifest.draft.json#9a523dac3d2c · blocking 0 · warnings 0 · checks 26
[PASS] structure.outputs: 2 output(s) present: 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json
[PASS] structure.inputs: 1 input(s) present: 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md)
[PASS] structure.sections: 19 required sections present and non-empty (01_Scenario_Design.md)
[PASS] structure.placeholders: no placeholders in 01_Scenario_Design.md
[PASS] evidence.storyline: 17/19 items carry a source pointer (min 80%); unsourced e.g. L80: 'gmail | 4 vendor billing mails (seed; §11) | next charge dates, card, Soundly/Kapwing conf'
[PASS] evidence.coherence_audit: 21/21 items carry a source pointer (min 100%)
[PASS] evidence.hidden_authorities: 3/3 items carry a source pointer (min 100%)
[PASS] evidence.delegation: 13/13 items carry a source pointer (min 90%)
[PASS] evidence.trap_register: 31/32 items carry a source pointer (min 90%); unsourced e.g. L328: 'T8 | eliminating_evidence | FIN-000688, FIN-000689, FIN-000699, FIN-000700 | R1 | no UA ac'
[PASS] evidence.record_plan: 20/24 items carry a source pointer (min 80%); unsourced e.g. L496: 'linear.linear_comments | 39 | cmt_ + 20 hex (`minted_ids.json` L_ISSUES) | authors Arthur,'
[PASS] evidence.active_speakers: 5/5 items carry a source pointer (min 100%)
[PASS] tool.hardness_gate_design: hardness_gate --design pasted PASS; re-run PASS
[PASS] tool.persona_reach: persona_view reach pasted for robert@harmonygames.co and matches the re-run (224 channels)
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] kb.coherence_hazards: coherence audit cites 16 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 5 speaker rows carry their activity.json status_at_clock
[PASS] kb.integrations: companions listed per integrations.json (10 INT ids, services ['confluence', 'gcal', 'gdocs', 'gdrive', 'github', 'gmail', 'gsheets', 'linear', 'slack', 'snowflake', 'trello'])
[PASS] kb.storyline: timeline cited; cohorts ['LIN-CQ11', 'LIN-OPEN-ENG', 'SF-LEDGER']; trap_catalog ['B03', 'B05', 'C01', 'D04', 'D07', 'D08']
[PASS] boundary.anchor_naming: 2 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] tool.redteam_dual: dual red team present (01b_Redteam_Review.md + .second.md)
[PASS] reach.scenario: 23 scoped load-bearing ids YES for robert (3 planned seeds not yet in base: verified at the injection gate)
[PASS] review.counter_readings: 23 evidenced counter-readings (of 24 found; need ≥ 19) in 01_Scenario_Design.md
[PASS] review.coverage: self-review addresses all 8 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## 13 Red team (dual)

RED TEAM UNAVAILABLE: redteam_review: set REDTEAM_MODEL or pass --model (no REDTEAM_* environment configured — error)

Substitute (dual), following the Douglas task's precedent: two independent reviewers (fresh subagents given only the
design, the manifest, `planned_text.json` and `truth.json`, read-only on the base). Reviewer A (coherence and unique
ground truth) → `01b_Redteam_Review.md` (Blocker 1 · Major 11 · Minor 7). Reviewer B (difficulty, shortcuts and volume,
a different model) → `01b_Redteam_Review.second.md` (Blocker 3 · Major 6 · Minor 5). Every finding was re-checked against
the exports before it was dispositioned.

| Finding | Source file | Disposition with evidence |
|---|---|---|
| A1 Blocker: costs came from the Dec-26 forecast column (header 2025-12-26, col AR); the true Dec-25 is col AF (header 2024-12-25) | 01b_Redteam_Review.md | **fixed.** Verified: HG P&L's Dec-25 header 2025-12-25 sits at col AF (index 31) and HG Costs' col AF ties to it (UA 610, f_605121f4a36752645e0ac3). Rule 8 now names column AF by position; every tab cost recomputed (Unity 2,172, Workspace 316.56, Slack 129.50, Gusto 116, Deel 300, Metabase 148, dbt 100, BigQuery 14.33, Vercel 86); a two-reading row added (§10); totals re-emitted by `mint_ids.py` |
| A2 SVB card is a MasterCard in base | 01b_Redteam_Review.md | **fixed.** leonard.hayes@harmonygames.co/1846148320251001978 confirmed; every receipt and the SVB card now say Mastercard ending 4417 (varied wording, see B1) |
| A3 ElevenLabs is an annual $50 plan to Jul 9 2026 in base | 01b_Redteam_Review.md | **fixed.** robert@harmonygames.co/1837122624854744558 confirmed; seeded receipt dropped; row = 50/12 = 4.17, deadline 2026-07-08 from the base receipt |
| A4 Figma's tab charge is 1,212 (Sep-25), not 1,440 | 01b_Redteam_Review.md | **fixed.** receipt now $1,212.00 → 101.00/month |
| A5 Linear is on a paid plan in base | 01b_Redteam_Review.md | **fixed.** robert@harmonygames.co/1850617582652876839 (Standard → Basic after Feb 1) confirmed; seeded Feb 1 receipt (Basic annual, 4 seats, $480, renews Feb 1 2027) → 40.00/month, Hold to Mar 12 (does not charge before the review) |
| A6 Helpshift dash vs Feb 27 (switch to email not shown) | 01b_Redteam_Review.md | **fixed.** comment_support_after_helpshift_c1 (moved off the base page_support_playbook, hazard S08, at injection) also says both games' support buttons open email; rule 6 names 'an export or a switch-over' |
| A7 'Done once the account is closed' vs access running to Feb 26–Mar 3 | 01b_Redteam_Review.md | **fixed.** project description: 'Done once the account counts as closed in the register (access can run out later)' — points at rule 5 without restating it |
| A8 Leonard's 'keeping this one' on the newer Intuit issue | 01b_Redteam_Review.md | **fixed.** comment on ENG-2461 now 'same account as the quickbooks issue'; row name variants (QuickBooks / Intuit QuickBooks / QuickBooks Online) to be accepted by the rubric |
| A9 'Carta terminations are done' (C0ADGSZKR3R/1770935621.095649) undercuts Open | 01b_Redteam_Review.md | **fixed.** Leonard's Carta comment says the terminations were the contractor grants and the subscription is untouched; tab col AA shows Carta 3,852 in Aug-25 → annual 321.00, renews Aug 14 → deadline 2026-08-13 |
| A10 a third clash: Slack seats cut to guests (C0ADGSZKR3R/1770842405.931359) vs 'every user in place' | 01b_Redteam_Review.md | **fixed.** R7 now names three clashes (downgrade, guest seats, Google archiving); C6 carries the seat-cut hop; the rubric treats the three as the minimum and accepts extras (GitHub card move, Gusto) |
| A11 GitHub/Figma in the after-plan total | 01b_Redteam_Review.md | **fixed.** rule 9 now defines the total as 'the same sum over the Keep and Hold rows only' (column arithmetic) |
| A12 Gusto 'annual' vs monthly charges on the tab | 01b_Redteam_Review.md | **fixed.** reply now 'gusto bills on the 1st … let's cancel before mar 1' |
| A13 §1a Layer sentence contradicts its receipt | 01b_Redteam_Review.md | **fixed.** §1a sibling sweep rewritten (every receipt on the company card) |
| A14 'blanked names' reads as an evaluator hint | 01b_Redteam_Review.md | **fixed.** project description now says the tab 'leaves a few lines unlabeled' (the Notion/Sentry naming was later removed at the /injection review, F2) |
| A15 rule 6 undefined for Keep rows that won't charge / Holds already off the card | 01b_Redteam_Review.md | **fixed.** rule 6 adds both cases (GitHub/Linear/Figma → review call; a Keep that won't charge before Feb 20 → dash) |
| A16 Docusign handover is only a question | 01b_Redteam_Review.md | **fixed.** 'docusign goes to robert, he used it for the art contracts' |
| A17 §1 prose order of booking vs checklist | 01b_Redteam_Review.md | **fixed.** §1 Arc now has the event at 22:40Z before the 23:58Z checklist |
| A18 Chase decoy implies autopays on Chase in 2025 | 01b_Redteam_Review.md | **fixed.** T_CHASE now only says nothing may pull from the account after Apr 25 (base Done card 64de736c2b10abdbda220c1b moved subscriptions to SVB in 2023) |
| A19 Unity invoice 1,200 vs tab 2,172 | 01b_Redteam_Review.md | **fixed** with A1 (invoice now $2,172.00) |
| B1 Gmail phase collapses: one 'Visa ending 4417' search + batch get | 01b_Redteam_Review.second.md | **fixed in part.** The card phrase now varies per vendor (Mastercard •••• 4417, MASTERCARD ending in 4417, MC •••4417, x4417, card on file …4417), so one literal search no longer sweeps them; `gmail_get_messages_batch` can still read several hits at once, so the budget counts one search per vendor (22), not search + read |
| B2 150 floor not secure (lean run ~135–150) | 01b_Redteam_Review.second.md | **fixed.** Six more project issues (1Password in scope; Notarize, UA Assets, Miro, Lucidchart, Google Ads excluded — Lucidchart and Google Ads closed in base mail, robert@harmonygames.co/1845611902985063512 and robert@harmonygames.co/1846207913731182209) add ~18 necessary calls; the anchor now asks for 'a line on each' issue directly (not only the project description). Budget 183; reviewer B's lean arithmetic plus 18 ≈ 160 |
| B3 every hidden source is named by a pointer → find rates near 1.0 | 01b_Redteam_Review.second.md | **accepted risk, partly mitigated.** Incorporation requires the pointers (`1_Prompt_Eval.md` §2.1). Mitigations: per-record cues removed (B4/B9), the decoy sheet made stale (B6), the costs-tab column trap added (A1), so score loss also comes from per-record execution over 32 rows × 6 columns. Recorded in Unresolved; `/create-hardening` MODE B after the Opus pre-check is the planned lever if the run finds every pointer |
| B4 Linear comments pre-answer dates/cards | 01b_Redteam_Review.second.md | **fixed.** Vercel's billing day moved to its receipt (G_VERCEL), Workspace's 'invoices on the 1st' removed (base invoice robert@harmonygames.co/1856033699491658253 carries the cycle); Carta and GitHub keep their comment as the only source (no mail exists) |
| B5 levers correlated through one 'follow every pointer' trait | 01b_Redteam_Review.second.md | **accepted risk** (same as B3); §6 keeps the lever table as the hypothesis to measure, not a projection |
| B6 Arthur's decoy sheet carries exact costs | 01b_Redteam_Review.second.md | **fixed.** SHEET_SUBS now shows stale rounded figures (Cursor 20, CodeRabbit 30, Layer 39, Zapier 20, Figma 0, Unity 1200) — a run that copies it is wrong |
| B7 truth cells without seeded evidence (Singular, Carta, Vercel, Workspace, GitHub) | 01b_Redteam_Review.second.md | **rebutted / fixed.** Singular: base invoices robert@harmonygames.co/1850283027022457279 (Dec 1) and Sep 1 INVSINC22671 fix the quarterly cycle (reviewer A confirmed). Carta and GitHub: Leonard's/Arthur's comments. Vercel: new G_VERCEL. Workspace: base Feb 2 invoice |
| B8 Sentry receipt still on 4417 vs moved to KubLLC | 01b_Redteam_Review.second.md | **superseded.** Sentry was removed at the /injection review (F2: the KubLLC message's redacted vendor is dbt in base Slack). Original rebuttal: the receipt was dated 2026-01-20; Arthur's KubLLC message is Feb 12 23:00Z (C0ADGSZKR3R/1770937232.664809) and his comment Feb 13 01:31Z; a later record supersedes an earlier receipt |
| B9 rule 5 won by comment text ('nothing back yet') | 01b_Redteam_Review.second.md | **fixed.** 'nothing back yet', 'asked them to confirm', 'nothing from them since' removed from the Unity, Singular and Layer comments; status now needs rule 5 plus a search for a vendor reply |
| B10 Gusto reply found by one search | 01b_Redteam_Review.second.md | **accepted.** A14 is a habit lever, not a hidden record; it stays incorporated by 'the replies under it' |
| B11 Helpshift only needs Confluence for the dash | 01b_Redteam_Review.second.md | **accepted.** Low-weight per-record fact (synthesis_omission T15); the rubric weights it 1–3 |
| B12 Trello decoy is trivial | 01b_Redteam_Review.second.md | **accepted.** The decoy exists for the same-service rule; the A12 difficulty is opening Trello at all (Gmail has 162 SVB threads, none dated) |
| B13 linear_list_issues / get_issue might return comments | 01b_Redteam_Review.second.md | **rebutted, to verify.** Ask_Carriers §6b / Hardness_Mastery §2.5: list items carry no comments (277 V1 trajectories); listed in Unresolved for the pre-check |
| B14 issue descriptions and comments not in planned_text.json | 01b_Redteam_Review.second.md | **noted.** Comments live in `accounts.json`; issue descriptions are written at injection and carry only the source ('costs tab' / '#winddown list'), never a per-record fact (dossier rule for /create-injection) |

