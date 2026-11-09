# Scenario Design — owen_dd_bug_carryover · design only · contains no prompt, OE or criterion text

Storyline: Domino Delights' bug record moves out of Slack into Linear before Slack loses its history. Planned seed texts live in `plan/seed_text.json`; planned outcomes for all 89 graded items in `plan/truth_sketch.json`. Every number marked UNCALIBRATED is a design aid. All open choices were delegated by the requester on 2026-11-07 (`00_Pre_Scenario_Analysis.md` §11).

## 0 Assignment, persona census and horizon note

| Field | Value |
|---|---|
| Universe key | normal |
| Universe label | Feb 14, 2026 (normal) |
| Clock line | Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Seed bound | freeze_utc 2026-02-14T00:00:00Z |
| shutdown_rules_apply | true |
| Persona | Owen Baker, Game Engineer (Unity), owen.baker@harmonygames.co, roster owen_baker |
| Function · competency · skill | Engineering · Engineering Ops · Actions |
| Evals category | Engineering & Live-Ops (`Evals/references/rules/task_categories.md`) |
| Task type · mode | long-horizon · medium, platform cap under 85 % |
| Requester targets | over 130 counted calls in every run; average strictly under 80 %; all other difficulty guidelines |
| Loss budget | E[average] ≤ 72 % (requester line less 8 points) |
| Effective profile | extreme (Long Horizon) |
| Volume exception | call_budget_floor 250, per_record_floor 100, requester-delegated; ≥ 500 needs padding. The per-record floor is 100, not the 200 in the analysis, because the gate counts read surfaces only |
| Theme screen | Domino Delights: no bio-adjacent theme. The ZM canvas is a scoped-out decoy and no seed uses zombie, infection or outbreak words |

Persona census, `persona_view.py reach owen_baker --top 10`, verbatim:

```
REACH  Owen Baker <owen.baker@harmonygames.co>  Game Engineer (Unity) / Engineering
clock 2026-02-14

SLACK  user=EMPLOYEE_0021_SLACK_ID  visible channels=116 {'public': 25, 'private': 34, 'mpim': 30, 'im': 27}  messages=222246  public-not-member (UNVERIFIED)=45
  persona posts=16295 last post=2026-02-12  last activity in visible channels=2026-02-13
  C05433XK267    builds                                 public  mem=31  msgs=41107  2023-04-20..2026-02-12
  C05H8KVNU67    game-design                            private mem=27  msgs=22751  2023-07-16..2025-10-06 archived
  C050WGU41HR    engineering-bots                       private mem=35  msgs=20306  2023-03-29..2026-02-11
  C05V5FNLB9V    god-bugs                               private mem=31  msgs=16889  2023-10-07..2026-02-11
  C0880U9751A    zombie-match3d                         private mem=25  msgs=16773  2025-01-09..2026-02-11
  C09UHHN6PFZ    prototype                              private mem=18  msgs=12172  2025-11-24..2026-02-12
  D05S1S2H55M    D05S1S2H55M                            im      mem=5   msgs=5934   2023-09-15..2025-10-18
  C0553V44CE4    god-ui-ux                              private mem=30  msgs=5009   2023-04-21..2025-10-06 archived
  D05S1S2AB5M    D05S1S2AB5M                            im      mem=5   msgs=4975   2023-09-15..2026-02-12
  C08R27X0EAH    zombie-bugs                            private mem=23  msgs=4688   2025-05-06..2026-02-11

GMAIL  mailbox=owen.baker@harmonygames.co threads=1595 messages=1633 range=2023-09-14..2026-02-10
  threads by last-message month (recent): {'2025-09': 22, '2025-10': 73, '2025-11': 42, '2025-12': 42, '2026-01': 23, '2026-02': 7}
  top correspondents: SVC_2398_EMAIL (545), SVC_0251_EMAIL (459), leonard.hayes@harmonygames.co (292), robert@harmonygames.co (244), julia.lawson@harmonygames.co (222), arthur.blake@harmonygames.co (205), marcus.bennett@harmonygames.co (204), calvin.price@harmonygames.co (175), douglas@harmonygames.co (171), martin.walsh@harmonygames.co (170)

GCAL  own=['owen.baker@harmonygames.co'] shared=[] events=511 (distinct ical_uid 143, cancelled 63)
  last event before clock=2026-01-01T17:00:00Z  next after clock=None
  by month: 2023-10:24 2023-11:17 2023-12:18 2024-01:34 2024-02:16 2024-03:5 2024-04:17 2024-05:21 2024-06:26 2024-07:29 2024-08:17 2024-09:37 2024-10:23 2024-11:23 2024-12:29 2025-01:29 2025-02:13 2025-03:6 2025-04:14 2025-05:19 2025-06:19 2025-07:21 2025-08:4 2025-09:9 2025-10:18 2025-11:8 2025-12:13 2026-01:2

DRIVE  owned=10 {'application/vnd.google-apps.document': 6, 'folder': 2, 'application/json': 2}
  shared-with=134 {'application/vnd.google-apps.document': 44, 'text/plain': 31, 'application/vnd.google-apps.spreadsheet': 26, 'application/json': 21, 'application/pdf': 5, 'application/vnd.google-apps.presentation': 5, 'text/csv': 2}
  shared by owner: {'Resource: -6481757892984311338': 102, 'leonard.hayes@harmonygames.co': 21, 'arthur.blake@harmonygames.co': 4, 'Resource: 7240535625619857401': 2, 'robert@harmonygames.co': 2, 'julia.lawson@harmonygames.co': 2, 'calvin.price@harmonygames.co': 1}
  native visible: {'gdocs': 50, 'gsheets': 26, 'gslides': 5}  last modified visible=2026-01-31T21:43:57Z
  UNVERIFIED (domain/anyone, not owned/shared)=143 {'application/vnd.google-apps.document': 47, 'application/vnd.google-apps.spreadsheet': 41, 'application/pdf': 24, 'application/vnd.google-apps.presentation': 20, 'application/json': 11}

UNSCOPED (always visible): contacts, github, trello, linear, snowflake, confluence

LAST ACTIVITY (days before clock): slack_persona_post=2026-02-12 (2d), slack_visible_channels=2026-02-13 (1d), gmail=2026-02-10 (4d), gcal_last_event_before_clock=2026-01-01 (44d), drive_last_modified_visible=2026-01-31 (14d)
```

Remit, from before-freeze sources: Owen holds 16 of the 28 UI children (for example ENG-2417, ENG-2432); his fixes sit in the canvas threads (CE156FDFB428/1763549617.765149); he owns open items such as the mega tile (C05V5FNLB9V/1764262971.568809). He is still active: harmonygames-Games/Combo-Fighters#37 merged Feb 13 and his last DM to Arthur is D05S1S2AB5M/1770934881.073719. Linear ticket work on a live game is squarely his, and `role_reviews.scenario` is recorded in `00_V3_Authoring_Evidence.json`.

## 1 Storyline

Leonard can't drop Slack yet but will (C09UHHN6PFZ/1770842590.881439), Linear stays through the transition, and DD's bug record exists only in Slack: Vincent's canvas and #god-bugs. Linear went quiet on Nov 7. BoomBit wants a sync next week (C09SWTHEMEW/1770977006.104929), so Arthur asks Owen to move the whole list into Linear and close out the UI tree.

Anchors and spine (every id YES for Owen, or planned):

| Service | Record | Role |
|---|---|---|
| slack | D05S1S2AB5M/1770937805.214409 (planned) | hub: Arthur's DM (AN1) |
| linear | ENG-2401 | UI Changes master ticket (AN2), 3 masters and 28 children |
| slack | CE156FDFB428/1763041126.468099 to /1763737449.845379 | 63 canvas lines, 55 ticked, 8 unticked |
| slack | C05V5FNLB9V/1763042988.277099 | Vincent posts the list |
| slack | C05V5FNLB9V/1764256187.655299 to /1766415326.501939 | 7 later bugs |
| slack | C05433XK267/1765310004.760809 | build log: fix line in a submission build |
| slack | C09SWTHEMEW/1764659626.614679 | Leonard: lives removed for tickets |
| slack | C05KNDCHAAG/1770839984.194409 | Feb 11 shutdown post, Google archive by Feb 15 |
| gdocs | f_948768f5a462e7037d17c9 | economy doc |
| github | harmonygames-Games/GameOfDominoes#1913 | open PR |
| github | harmonygames-Games/GameOfDominoes#1914 | open economy PR; its commit list defines the economy line |

KB placement: `universe_kb/by_universe/normal/timeline.json` rows 2025-11-02 (web port and UI work), 2025-11-07 (planning tools go quiet), 2026-02-09 and 2026-02-11 (wind-down), 2026-02-13 (work continues). Cohorts from `cohorts.json`: LIN-EPIC (children of epics), LIN-OPEN-ENG (open ENG issues, source of reuse candidates), SL-T05 (#god-bugs 2025 roots), GH-Q08 (GameOfDominoes 2025-Q4 PRs). `trap_catalog.json` entries: K01 (canvas pseudo-channels), N03 (branch keys), C01 and C02 (thread corrections and parent resolutions), D07 (Trello stale against Linear), B04 (Jenkins in #builds).

Natural services (11): slack, gmail, gcal, gdrive, gdocs, gsheets, linear, github, trello, confluence, snowflake. Injected (10): slack, gmail, gcal, gdrive, gdocs, gsheets, gslides, linear, github, trello. Confluence and Snowflake stay out of the graded path (NB-21 and learnings §26).

Coupling seams: a mail changes which ticket a canvas line lands on (C5); a spec in Docs voids three lines read in Slack (C2); an inline review changes a Linear state (C1); a DM reverses a tick (C3); a commit closes an open thread (C4).

## 1a Coherence audit

Scope: every record a correct run opens. Hazards from `coherence_hazards.json`; cards from `references/known_data_issues/normal.md`.

| Record | Category | Fields | Pointer | Hazard / card | Disposition |
|---|---|---|---|---|---|
| Seeded Slack near the export end | temporal | ts | D05S1S2AB5M/1770937805.214409 | T07, NB-6 | avoid: all seeded Slack ts before Feb 13 10:03 UTC |
| Trello board quiet since Nov | temporal | dateLastActivity | card 690b27282f4c1b7a6e93d512 | T06, D07 | fold into design: the card and comment date from Nov 5, before the board went quiet |
| Linear activity after Nov 7 | temporal | created_at | ENG-2401 comment comment_49b5ac4788465f72ddf245e34f2b7034 | T04 | fold into design: Arthur's Feb note is on an open master |
| Seeded notes on closed children | temporal | created_at | ENG-2417 | T05 | avoid: no seeded comment on a child after completed_at; closed children take none |
| Labels mix sprints and codenames | semantic | labels | ENG-2410 | S03 | avoid: only the Bug label is used |
| Contacts job titles | semantic | job | ENG-2401 authors are not titled; contact 4e13bd40cc73d0fc76f87c7d | S06 | avoid: no title is graded |
| Canvas title date against comment dates | semantic | title | CE156FDFB428/1763041126.468099 | K01 | avoid: no build number or canvas date is graded (NB-21) |
| Slack cites keys or PRs not in export | cross-service referential | text | C05V5FNLB9V/1763042988.277099 | R01, R02 | avoid: seeds cite only keys and PRs proved by records |
| Google-native doc links in Slack | cross-service referential | url | C05V5FNLB9V/1764662837.138929 | R04 | avoid: Robert's QA doc link is not used; the rule doc scopes population by post |
| Thread reply counters | quantitative | reply_count | C05V5FNLB9V/1766415326.501939 | Q01, Q03 | fold into design: a seeded reply updates the parent's counters |
| Tree children in state PR with merged PRs | state/lifecycle | state | ENG-2417 and harmonygames-Games/GameOfDominoes#1901 | L01, L07 | fold into design: the SQL leaves these states alone; closing them out is the job Arthur gives, so PR on a merged ticket is the stale status it reconciles |
| ENG-2405 Todo with merged PR | state/lifecycle | state | ENG-2405 and harmonygames-Games/GameOfDominoes#1905 | L03 | fold into design: the SQL leaves it alone and the rule doc keeps the masters as they are |
| Master checklists against child states | state/lifecycle | description | ENG-2404 | NB-14 | repaired: the SQL clears the ENG-2403 and ENG-2404 checklists, so they can't disagree with the child tickets |
| Message ids and mailbox aliases | identifier/format | id | owen.baker@harmonygames.co/1849333980856689601 style ids; base files use owen@harmonygames.co | I02, I03 | fold into design: seeded ids follow `id_contracts.json` |
| Branch names differ between lists and Slack | identifier/format | name | C05433XK267/1765310004.760809 against the branch list | NB-13 | avoid: no exact branch name is graded |
| Owen left #god-bugs on Feb 11 | other | membership | C09UHHN6PFZ/1770842566.250369 | NB-1 | repaired: Arthur puts Owen on a spare paid seat, and he rejoins the DD channels on Feb 12 before Arthur's DM; the platform /prompt failed rev2 on this |
| Slack DM member lists | other | members | D05S1S2AB5M/1770934881.073719 | NB-31 | avoid: no access argument rests on member lists |
| Linear base comments | other | comments | ENG-2401 | NB-24 | fold into design: every Linear comment here is seeded |

Sibling-defect sweep: the designed 'merged but not done' defect has siblings across the tree. All 19 open children were reviewed; their planned states are in `plan/truth_sketch.json`, and the blind fork sweep (section 13) re-read them.

## 1b Active speakers

Status from `universe_kb/by_universe/normal/activity.json`:

| Person | Email | status_at_clock | Seeding role |
|---|---|---|---|
| Arthur Blake | arthur.blake@harmonygames.co | active_feb_2026 | hub DM, rule doc, master note, inline reviews, invite |
| Brian Foster | brian.foster@harmonygames.co | active_feb_2026 | check notes on three Validation children, thread replies, DM, Trello comment and checklist, deck; dated Sep–Dec 2025 |
| Vincent Parker | vincent.parker@harmonygames.co | quiet_since_2025-12 | mail, ticket note and canvas replies, all dated by Nov 23, 2025 |
| Oliver Brooks | oliver.brooks@harmonygames.co | active_feb_2026 | Season Pass note; invited |
| Robert | robert@harmonygames.co | active_feb_2026 | invited; base bug posts only |
| Leonard Hayes | leonard.hayes@harmonygames.co | active_feb_2026 | not seeded; base posts only |
| Marcus Bennett | marcus.bennett@harmonygames.co | active_feb_2026 | 1:1 note to Owen on Dec 11; base #1913 and thread |
| Owen Baker | owen.baker@harmonygames.co | active_feb_2026 | the persona; recipient of seeds |

## 1c Identity traps

`entity.py collisions`, verbatim:

```

SHARED_FIRST_NAMES (4)
  claire: ['Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]', 'Claire <github:PERSON_2360_GITHUB_USERNAME>']
  marcus: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Marcus Lee <marcus.lee@harmonygames.co>', 'Marcus <github:PERSON_0396_GITHUB_USERNAME>', 'Marcus <trello:c48a210d5c5a4b59231c6873>']
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
  - Gmail thread files of julia.lawson@harmonygames.co are named 'jlawson@harmonygames.co_*'
  - Gmail thread files of leonard.hayes@harmonygames.co are named 'leonard@harmonygames.co_*'
  - Gmail thread files of oliver.brooks@harmonygames.co are named 'oliver@harmonygames.co_*'
  - Gmail thread files of owen.baker@harmonygames.co are named 'owen@harmonygames.co_*'
  - Gmail thread files of samuel.turner@harmonygames.co are named 'samuel@harmonygames.co_*'
  - Gmail thread files of simon.walker@harmonygames.co are named 'simon@harmonygames.co_*'
  - Gmail thread files of vincent.parker@harmonygames.co are named 'vincent@harmonygames.co_*'
  - Gmail thread files of felix.young@harmonygames.co are named 'felixyoung@harmonygames.co_*'
  - Gmail thread files of oscar.bennett@harmonygames.co are named 'oscar@harmonygames.co_*'
  - Slack handle 'thomas' (U05F0A0D12F) belongs to Thomas Baker <thomas.baker@harmonygames.co> but equals the mailbox local part of Thomas <thomas@harmonygames.co> [persona thomas]

LOOKALIKE_EMAIL_LOCAL_PARTS (2)
  - 'thomas@' vs 'thomas.baker@': ['Thomas <thomas@harmonygames.co> [persona thomas]'] / ['Thomas Baker <thomas.baker@harmonygames.co>']
  - 'thomas@' vs 'thomaslee@': ['Thomas <thomas@harmonygames.co> [persona thomas]'] / ['? <thomaslee@harmonygames.co>']

TOKENS_MAPPING_TO_SEVERAL_ENTITIES (9)
  EMPLOYEE_0024: {'entities': ['scott <employee_0024@harmonygames.co>', '? <slack:EMPLOYEE_0024_SLACK_ID>', '? <trello:3d36d70154e6a715614e0d75>'], 'records': ['gcal.calendar_id=employee_0024@harmonygames.co', 'gcal.owner_email=employee_0024@harmonygames.co', 'linear.id=usr_EMPLOYEE_0024', 'linear.email=employee_0024@harmonygames.co', 'contacts.email=employee_0024@harmonygames.co', 'email.email=employee_0024@harmonygames.co', 'slack.id=EMPLOYEE_0024_SLACK_ID', 'trello.username=employee_0024']}
  EMPLOYEE_0032: {'entities': ['? <EMPLOYEE_0032_EMAIL>', 'Josh Dempsey <josh.dempsey@harmonygames.co>', '? <github:EMPLOYEE_0032_GITHUB_USERNAME>', '? <slack:EMPLOYEE_0032_SLACK_ID>'], 'records': ['confluence.id=user_EMPLOYEE_0032', 'gmail.mailbox=EMPLOYEE_0032_EMAIL', 'gdrive.email=EMPLOYEE_0032_EMAIL', 'linear.id=usr_EMPLOYEE_0032', 'linear.email=EMPLOYEE_0032_EMAIL', 'contacts.email=EMPLOYEE_0032_EMAIL', 'email.email=EMPLOYEE_0032_EMAIL', 'github.login=EMPLOYEE_0032_GITHUB_USERNAME', 'slack.id=EMPLOYEE_0032_SLACK_ID']}
  PERSON_2218: {'entities': ['? <PERSON_2218_EMAIL>', '? <github:PERSON_2218_GITHUB_USERNAME>'], 'records': ['linear.id=usr_PERSON_2218', 'linear.email=PERSON_2218_EMAIL', 'contacts.email=PERSON_2218_EMAIL', 'email.email=PERSON_2218_EMAIL', 'github.login=PERSON_2218_GITHUB_USERNAME']}
  PERSON_2360: {'entities': ['? <PERSON_2360_EMAIL>', 'Claire <github:PERSON_2360_GITHUB_USERNAME>'], 'records': ['github.login=PERSON_2360_GITHUB_USERNAME', 'email.email=PERSON_2360_EMAIL']}
  PERSON_3233: {'entities': ['? <PERSON_3233_EMAIL>', '? <github:PERSON_3233_GITHUB_USERNAME>', '? <slack:PERSON_3233_SLACK_ID>'], 'records': ['linear.id=usr_PERSON_3233', 'linear.email=PERSON_3233_EMAIL', 'contacts.email=PERSON_3233_EMAIL', 'email.email=PERSON_3233_EMAIL', 'github.login=PERSON_3233_GITHUB_USERNAME', 'slack.id=PERSON_3233_SLACK_ID']}
  PERSON_3335: {'entities': ['? <PERSON_3335_EMAIL>', '? <slack:PERSON_3335_SLACK_ID>'], 'records': ['contacts.email=PERSON_3335_EMAIL', 'email.email=PERSON_3335_EMAIL', 'slack.id=PERSON_3335_SLACK_ID']}
  PERSON_3935: {'entities': ['? <PERSON_3935_EMAIL>', '? <slack:PERSON_3935_SLACK_ID>'], 'records': ['email.email=PERSON_3935_EMAIL', 'slack.id=PERSON_3935_SLACK_ID']}
  PERSON_5275: {'entities': ['? <PERSON_5275_EMAIL>', '? <slack:PERSON_5275_SLACK_ID>'], 'records': ['contacts.email=PERSON_5275_EMAIL', 'email.email=PERSON_5275_EMAIL', 'slack.id=PERSON_5275_SLACK_ID']}
  PERSON_5360: {'entities': ['? <PERSON_5360_EMAIL>', '? <slack:PERSON_5360_SLACK_ID>'], 'records': ['email.email=PERSON_5360_EMAIL', 'slack.id=PERSON_5360_SLACK_ID']}

SEVERAL_IDS_IN_ONE_SERVICE (1)
  - Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]: 2 github identities ['PERSON_0003_GITHUB_USERNAME', 'PERSON_2137_GITHUB_USERNAME'] (joins: ['exact_email', 'exact_name'])

PERSONA_ROLE_VS_CONTACTS_JOB (5)
  - Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]: roster role 'Game Engineer (Unity VFX)' vs Contacts job 'Game Engineer (Unity/VFX)'
  - Frederick Stone <frederick.stone@harmonygames.co> [persona frederick_stone]: roster role 'Co-founder' vs Contacts job 'Commercial Lead, Marketing & Business Development'
  - Leonard Hayes <leonard.hayes@harmonygames.co> [persona leonard_hayes]: roster role 'Co-founder & Creative Director' vs Contacts job 'Co-founder & CEO'
  - Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]: roster role 'Artist' vs Contacts job 'Artist (VFX & Animation)'
  - Robert <robert@harmonygames.co> [persona robert]: roster role 'Co-Founder & Creative Director' vs Contacts job 'Co-founder & Chief Product Officer'

SHARED_CONTACT_JOB_TITLES (5)
  Game Designer: ['Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]', 'Samuel Turner <samuel.turner@harmonygames.co> [persona samuel_turner]']
  Game Developer: ['Thomas <thomas@harmonygames.co> [persona thomas]', 'Lucas <lucas@harmonygames.co>']
  Game Engineer: ['Brian Foster <brian.foster@harmonygames.co> [persona brian_foster]', 'Victor Barnes <victor.barnes@harmonygames.co> [persona victor_barnes]']
  General Counsel: ['Michelle Carter <michelle.carter@harmonygames.co>', 'Thomas Baker <thomas.baker@harmonygames.co>']
  User Acquisition Manager: ['George Miller <george.miller@harmonygames.co>', 'Megan Wilson <megan.wilson@harmonygames.co>', 'Victoria Lane <victoria.lane@harmonygames.co>']

UNRESOLVED (12)
  [ambiguous_name] github: mononym 'Marcus' is an exact name of [] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co'] -> candidates ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']
  [ambiguous_name] github: mononym 'Claire' is an exact name of [] and the first name of ['email:claire.morgan@harmonygames.co'] -> candidates ['email:claire.morgan@harmonygames.co']
  [ambiguous_name] trello: mononym 'Marcus' is an exact name of ['github:PERSON_0396_GITHUB_USERNAME'] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co'] -> candidates ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co', 'github:PERSON_0396_GITHUB_USERNAME']
  [token_link] EMPLOYEE_0024: same token number across services but no shared exact email/name: not joined -> candidates ['email:employee_0024@harmonygames.co', 'slack:EMPLOYEE_0024_SLACK_ID', 'trello:3d36d70154e6a715614e0d75']
  [token_link] EMPLOYEE_0032: same token number across services but no shared exact email/name: not joined -> candidates ['email:EMPLOYEE_0032_EMAIL', 'email:josh.dempsey@harmonygames.co', 'github:EMPLOYEE_0032_GITHUB_USERNAME', 'slack:EMPLOYEE_0032_SLACK_ID']
  [token_link] PERSON_2218: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_2218_EMAIL', 'github:PERSON_2218_GITHUB_USERNAME']
  [token_link] PERSON_2360: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_2360_EMAIL', 'github:PERSON_2360_GITHUB_USERNAME']
  [token_link] PERSON_3233: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3233_EMAIL', 'github:PERSON_3233_GITHUB_USERNAME', 'slack:PERSON_3233_SLACK_ID']
  [token_link] PERSON_3335: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3335_EMAIL', 'slack:PERSON_3335_SLACK_ID']
  [token_link] PERSON_3935: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3935_EMAIL', 'slack:PERSON_3935_SLACK_ID']
  [token_link] PERSON_5275: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_5275_EMAIL', 'slack:PERSON_5275_SLACK_ID']
  [token_link] PERSON_5360: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_5360_EMAIL', 'slack:PERSON_5360_SLACK_ID']

INTEGRITY FLAGS (2)
  {'type': 'id_with_space', 'service': 'linear', 'id': 'usr_Victor Barnes'}
  {'type': 'name_mismatch_on_email_join', 'service': 'github', 'id': 'PERSON_2314_GITHUB_USERNAME', 'detail': "GitHub PERSON_2314_GITHUB_USERNAME joined by email but shows name 'Ryan' (entity is Frederick Stone)"}
```

`entity.py resolve "Owen Baker"`, verbatim:

```
ENTITY email:owen.baker@harmonygames.co  name=Owen Baker  kind=person  emails=['owen.baker@harmonygames.co']
  persona: owen_baker - Game Engineer (Unity) / Engineering
  slack      id=EMPLOYEE_0021_SLACK_ID, name=Owen Baker, real_name=Owen Baker, email=owen.baker@harmonygames.co, is_bot=False, deleted=False, messages=16295, first_post=2023-09-15, last_post=2026-02-12   [join: exact_email]
  gmail      mailbox=owen.baker@harmonygames.co, threads=1595, messages=1633, first=2023-09-14, last=2026-02-10, thread_filename_alias=['owen@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=owen.baker@harmonygames.co, owner_email=owen.baker@harmonygames.co, summary=Owen Baker — primary, events=511, last_event_before_clock=2026-01-01   [join: exact_email]
  gdrive     id=user_4e13bd40cc73, email=owen.baker@harmonygames.co, display_name=owen.baker@harmonygames.co, root_folders=['d_4e13bd40cc73d0fc76f87c'], owned_items=10, last_modified=2025-08-25, files_shared_with=134   [join: exact_email]
  linear     id=usr_4e13bd40cc73d0fc, email=owen.baker@harmonygames.co, name=owen.baker@harmonygames.co, is_active=True, last_activity=2025-11-19   [join: exact_email]
  github     login=PERSON_5877_GITHUB_USERNAME, name=Owen Baker, email=owen.baker@harmonygames.co, type=User, last_activity=2026-02-13   [join: exact_email]
  trello     id=919ee44a0d5157b7839f66a8, username=owen.baker, fullName=Owen Baker   [join: exact_name]
  confluence id=user_EMPLOYEE_0021, account_id=acct_EMPLOYEE_0021, email=owen.baker@harmonygames.co, display_name=Owen Baker, is_active=True   [join: exact_email]
  contacts   contact_id=4e13bd40cc73d0fc76f87c7d, name=Owen Baker, email=owen.baker@harmonygames.co, job=Game Engineer (Unity), is_user=False   [join: exact_email]
  last activity: {'slack': '2026-02-12', 'gmail': '2026-02-10', 'gcal': '2026-01-01', 'gdrive': '2025-08-25', 'linear': '2025-11-19', 'github': '2026-02-13'}
```

Pinned: Marcus is Marcus Bennett (marcus.bennett@harmonygames.co), not Marcus Lee or the `marcus@` mailbox. Owen Baker is not Thomas Baker. Brian is Brian Foster. No second account is created for anyone.

## 2 Cohort spine

Rule: 63 canvas lines with a comment thread, 7 bugs posted in the bug channel after the canvas's last line, and 32 UI tree records: 102 records. Source: the hub and H1. Size 102; the design stays inside 40–150.

| Surface | Tool | Records | Calls each | Requirement | Why no bulk | Short circuit |
|---|---|---|---|---|---|---|
| linear | linear_list_comments | 32 | 1.0 | R5 | linear_list_issues returns no comments; each child's sign-off note needs its own linear_list_comments | a child's state turns on its own note; the master checklist is unreliable (NB-14), so no other record decides it, and one search cannot page every child's comments |
| github | github_get_pull_request_reviews and github_get_pull_request_comments | 13 | 2.0 | R5 | github_search_pull_requests does not return reviews or inline comments, and in:comments misses inline ones | merged state does not decide a child; only the PR's own review surfaces show a held piece, and no search sweeps inline comments |
| linear | linear_list_issues by subject and linear_list_comments | 15 | 1.0 | R3 | titles use other words, so each unticked line or later bug needs its own ticket search and comment read | reuse cannot be decided from the canvas; the tie sits on or about the ticket |
| slack | slack_read_thread | 70 | 0.5 | R2 | slack_read_channel returns roots without replies, and fixes and doubts sit in replies; a search can sweep some, so this surface counts at half | the outcome needs the thread's last word on each line; a search for fixed misses replies in other words |

Predicate: four outcomes, closed vocabulary, in H1 f_3ca9e15d7b20f4e681ad52: Fixed, Broken, Gone, Covered. House rule that overrides the natural reading: a tick stands only until a later record about that bug. Effective-date regime: the economy change removes lives from the build players have (C09SWTHEMEW/1764659626.614679). Boundary records: 7 later bugs (C05V5FNLB9V/1764256187.655299), and the shortlist of Robert's sub-250 reports the rule folds into the canvas (C09Q4S613CN/1764013026.858409).

Shortcut audit: `slack_search_public_and_private` can sweep canvas replies, so that surface counts at half. No call returns Linear comments or inline PR comments in bulk. The writes have no batch form.

## 3 Hidden authorities

| Id | Name | Home | Record | Decoy | Governs | Findable by |
|---|---|---|---|---|---|---|
| H1 | the carry-over notes doc | gdocs | f_3ca9e15d7b20f4e681ad52 | f_72e0b4c3d91a5f68c2b7e4 (game: Zombie Match 3D) | R2, R3, R4, R9 | carry-over notes |
| H2 | Brian's closing rule from the UI work | trello | 690b29bc3c7d2e51b0f86a47 | 68d284b84b7e9a3c5d16e208 (game: Zombie Match 3D) | R6 | close these out |

Both are named by role. H1 is named in the hub; H2 is named in H1 without saying where it sits. Findability proof runs at injection, because both are planned seeds.

## 4 Delegation lattice

| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |
|---|---|---|
| AN1 | Arthur's DM from Thursday | D05S1S2AB5M/1770937805.214409 |
| AN2 | the UI Changes master ticket | ENG-2401 |

Hub: AN1 in Arthur's voice delegates by role. It names no bug, no authority location and no channel.

Fragments and incorporation (quotes are exact substrings of the planned record in `plan/seed_text.json`):

| Id | Service | Container | Kind | Via | Delegated by | Quote | Requirements |
|---|---|---|---|---|---|---|---|
| K1 | gdocs | f_3ca9e15d7b20f4e681ad52 | delegation | AN1 | D05S1S2AB5M/1770937805.214409 | the carry-over notes doc | R2, R3, R4, R5, R9 |
| K2 | slack | CE156FDFB428 | requirement | AN1 | D05S1S2AB5M/1770937805.214409 | Vincent's Android canvas | R1 |
| K3 | slack | C05V5FNLB9V | requirement | AN1>K1 | f_3ca9e15d7b20f4e681ad52 | every bug posted in the bug channel after the last line in that comment channel | R1 |
| K4 | linear | ENG-2401 | amendment | AN1>K1 | f_3ca9e15d7b20f4e681ad52 | If anything changes after this I'll put it on the master ticket | R4 |
| K5 | trello | 690b27282f4c1b7a6e93d512 | format | AN1>K1 | f_3ca9e15d7b20f4e681ad52 | Brian's closing rule from the UI work | R6 |
| K6 | gcal | evt_6e2c91d4b07f3a58c1d2e4 | recipient | AN1 | D05S1S2AB5M/1770937805.214409 | everyone on Sunday's bug review | R7 |
| K7 | gdrive | d_9b41e7c2a05d36f8e1c7a4 | destination | AN1 | D05S1S2AB5M/1770937805.214409 | your DD bug carry-over folder | R7 |
| K8 | gmail | owen.baker@harmonygames.co/1849333980856689601 | requirement | AN1>K1 | f_3ca9e15d7b20f4e681ad52 | Vincent tied a few lines to tickets before he left | R3 |
| K9 | linear | ENG-2363 | requirement | AN1>K1 | f_3ca9e15d7b20f4e681ad52 | Vincent tied a few lines to tickets before he left | R3 |
| K10 | slack | C09SWTHEMEW | requirement | AN1>K1 | f_3ca9e15d7b20f4e681ad52 | which came off the economy line | R2 |
| K11 | linear | ENG-2428 | requirement | AN1>K1 | f_3ca9e15d7b20f4e681ad52 | Brian and Oliver left notes on some of the open children | R5 |
| K12 | linear | ENG-2437 | requirement | AN1>K1 | f_3ca9e15d7b20f4e681ad52 | Brian and Oliver left notes on some of the open children | R5 |

Amendment: K4, Arthur's later note on ENG-2401, adds the title prefix and leaves the rest of H1 standing. Distractors outside the chain are in section 5.

## 5 Chains and trap register

| Chain | Root cause | Hops | Ends in |
|---|---|---|---|
| C1 | A24 | linear ENG-2434 → github harmonygames-Games/GameOfDominoes#1905 → github harmonygames-Games/GameOfDominoes#1905#rc_1 | R5 |
| C2 | A15 | slack CE156FDFB428/1763548856.943389 → slack C09SWTHEMEW/1764659626.614679 → gdocs f_948768f5a462e7037d17c9 | R9 |
| C3 | A11 | slack CE156FDFB428/1763642831.967359 → slack CE156FDFB428/1763642831.967359 → slack D05USBTQY1F/1765452012.418229 → linear ENG-2401 | R2 |
| C4 | A25 | slack C05V5FNLB9V/1764659550.713509 → github harmonygames-Games/GameOfDominoes#1914 → slack C05433XK267/1765310004.760809 | R2 |
| C5 | A7 | slack CE156FDFB428/1763041538.186339 → gmail owen.baker@harmonygames.co/1849333980856689601 → linear ENG-2073 | R3 |


| Trap | Family | Records | Requirement | Expected wrong reading | Resolver | Discovery order |
|---|---|---|---|---|---|---|
| T_INLINE_TD | done_gap | harmonygames-Games/GameOfDominoes#1905#rc_1, harmonygames-Games/GameOfDominoes#1905#c_3, f_d15a8c70e3f2b94a61c8d3, harmonygames-Games/GameOfDominoes#1905 | R5 | ENG-2434 is finished: #1905 merged with Arthur's approval, Brian ticked the screen off and the wrap deck says shipped | Arthur's inline comment on #1905 says the how-to-play popup must be swapped before the ticket closes; the review body is silent | the merged PR and Brian's tick come back from the tree read; the inline comment needs github_get_pull_request_comments |
| T_WINGS | eliminating_evidence | C9CA62B5180A/1765927876.696389 | R5 | ENG-2424 goes Done like the other merged children | Owen disabled Win & Collect on Dec 16, so that screen is not in the build; no re-enable is on record | the child reads as finished until the disable post or its commit is found |
| T_INLINE_AXE | done_gap | harmonygames-Games/GameOfDominoes#1908#rc_1, harmonygames-Games/GameOfDominoes#1908#c_3, harmonygames-Games/GameOfDominoes#1908 | R5 | ENG-2426 is finished: #1908 merged and Brian ticked the panel off | Arthur's inline comment on #1908 says the info popup keeps the old frame and must be done first | Brian's tick is read first; the inline comment sits behind a separate call |
| T_SEASON | superseding | f_d15a8c70e3f2b94a61c8d3, comment_d6aee2099bd71050facc422ccef8f809 | R5 | the wrap deck says the UI pass wrapped up, so ENG-2428 is Done | Oliver's later note on ENG-2428 says the reward track still uses the old frames | - |
| T_REPLY | superseding | C09Q4S613CN/1764606918.318209, CE156FDFB428/1763549455.195819 | R2 | the River Tile and Memory Tile shop icons line is ticked, so it is fixed | Brian's later reply under an unrelated sub-250 post says the round icons came back | the tick is read from the canvas; the reply sits under a gems question |
| T_BACK | superseding | D05USBTQY1F/1765452012.418229, CE156FDFB428/1763642831.967359 | R2 | the Tavern buttons line is ticked and Brian sent the fix, so it is fixed | Marcus's later 1:1 note to Owen says the frame was lost again and Brian's fix did not hold | the tick and Brian's fix are in the canvas thread; the note sits in a DM no anchor names |
| T_GONE | effective_date | CE156FDFB428/1763548856.943389, C09SWTHEMEW/1764659626.614679, f_948768f5a462e7037d17c9 | R9 | the unticked lives lines are still broken | the lives feature was removed: Leonard's BoomBit post, the economy doc and his Jan no-lives note; the live build has tickets | the unticked lines come first; the removal sits in another channel and a doc |
| T_LINE | done_gap | C05V5FNLB9V/1764329192.159229, harmonygames-Games/GameOfDominoes#1913 | R2 | the tile dozer window is fixed: Marcus fixed it and did a PR | GameOfDominoes#1913 is still open and its commit is not in #1914's list, so the fix never reached that build | Marcus's reply reads as closed before any PR lookup |
| T_ELSE_FLICKER | completion_elsewhere | C09Q4S613CN/1766164222.418229, C05V5FNLB9V/1764659550.713509, C05433XK267/1765310004.760809 | R2 | the flicker thread ends at testing a fix now, so it is still broken | Robert's later reply under his sub-250 report says both flickers are gone, and the fix commit is on the economy line | - |
| T_ELSE_MUSIC | completion_elsewhere | D07E9PSQB6W/1765206644.602119, C05V5FNLB9V/1764660142.352319 | R2 | Owen said he would check the music next and nothing closed it | Brian's DM to Owen says music plays normally since the audio player change | - |
| T_ELSE_ACID | completion_elsewhere | D07E9PSQB6W/1765206644.602119, C05V5FNLB9V/1764661312.152719 | R2 | Brian's I'm checking is the last word on the acid delay | the same DM says the acid throw lines up after his animation fix | - |
| T_ALIAS_APPLE | scope_alias | owen.baker@harmonygames.co/1849333980856689601, CE156FDFB428/1763041538.186339 | R3 | no ticket has the canvas wording, so a new one is filed | Vincent's mail ties the Apple sync line to ENG-2073 | - |
| T_ALIAS_SPLASH | scope_alias | comment_7ab5299cbb609d95ba12249d315daedc, CE156FDFB428/1763132009.017599 | R3 | no ticket has the canvas wording, so a new one is filed | Vincent's note on ENG-2363 ties the manual sign-in line to it | - |
| T_FILT | exact_predicate | C05V5FNLB9V/1764256187.655299, C05V5FNLB9V/1766415326.501939 | R1 | the canvas is the whole list | the rule doc brings in bugs posted in the bug channel after the canvas's last line | - |
| T_FOLLOW | authority | 690b29bc3c7d2e51b0f86a47 | R6 | any line on a child is enough | Brian's comment on the UI work card says every close-out note names the current public build | - |
| D_ZMCANVAS | distractor (scope_adjacent) | C3DD99314033/1758276844.870419 | R1 | the ZM Collect & Win canvas is part of the job | the rule doc leaves the ZM canvas where it is | - |
| D_SIGNIN | distractor (near_duplicate_record) | ENG-2280 | R3 | ENG-2280 covers the Apple sign-in line | Vincent's mail names ENG-2073 | - |
| D_LIVESTICKETS | distractor (keyword_collision) | ENG-2277, ENG-2400 | R9 | the open lives tickets mean those lines have a ticket | the feature is gone from the live build | - |
| D_ZMDOC | distractor (other_title) | f_72e0b4c3d91a5f68c2b7e4 | R2 | the ZM notes set how ticks and close-outs work | they cover the other game | - |
| D_SUB250 | distractor (scope_adjacent) | C09Q4S613CN/1764013026.858409 | R1 | Robert's sub-250 reports are extra bugs | the rule doc leaves them out | - |
| D_DECK | distractor (stale_summary) | f_d15a8c70e3f2b94a61c8d3 | R5 | the wrap deck proves the UI work finished | child records decide | - |
| D_ECONCANVAS | distractor (scope_adjacent) | C4208B207A1A/1765298859.629579 | R1 | the economy canvas is part of the list | the rule doc leaves it where it is | - |

Hardness v2 selection (`Hardness_Mastery.md` §13): trap 1 (INLINE, LINE), trap 2 (REPLY, BACK), trap 3 (FOLLOW), trap 5 (GONE), trap 6 (ALIAS), trap 9 (ELSE). Each names its convincing wrong source and beating record in the table above and flips a weight-5 slot.

### Mechanism portfolio (S5a)

Candidates, grounded in records. Priors are from `hardness_ledger.py priors --model claude-opus-5-5`.

| # | Anchor storyline (cited) | Coupling | Characteristic | Discovery-order proof | Reach | Findability term | Gradable fact | Services | Walk Δ vs tier | Risks |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | tree child, harmonygames-Games/GameOfDominoes#1905 | inline review changes a Linear state | done gap | PR merged is read first | YES | how-to-play | child stays open | github, linear | +13 reads | all-fail rows; selected |
| 2 | ticked line CE156FDFB428/1763549455.195819 | reply reverses a tick | correction off path | tick read first | YES | round icons | line Broken | slack | none | selected |
| 3 | ticked line CE156FDFB428/1763642831.967359 | DM reverses a tick | correction off path | tick read first | YES | Tavern | line Broken | slack | none | DM sweeps; selected |
| 4 | rule comment on card 690b27282f4c1b7a6e93d512 | rule changes every note | follow-through | rule doc read first | planned | close these out | note names the build | trello, linear | none | board actions call; selected |
| 5 | line CE156FDFB428/1763548856.943389 | spec voids a bug | rule in older records | line read first | YES | lives | line Gone | slack, gdocs | none | judgement; selected |
| 6 | window post C05V5FNLB9V/1764329192.159229 | open PR denies a fix | done gap | reply reads as closed | YES | tile dozer | line Broken | slack, github | +1 | stated rule; selected |
| 7 | flicker post C05V5FNLB9V/1764659550.713509 | commit closes a thread | completion elsewhere | thread read first | YES | flicker | bug Fixed | slack, github | +2 | selected |
| 8 | line CE156FDFB428/1763041538.186339 | mail ties line to ticket | alias | title search first | YES | sign in | reuse ENG-2073 | slack, gmail, linear | +2 | selected |
| 9 | later posts C05V5FNLB9V/1764256187.655299 | rule widens the list | outside the filter | canvas read first | YES | bug channel | bug present | slack | +9 | rule doc must name the channel, so it leaks: kept as a trap with control rows, no rule |
| 10 | deck f_d15a8c70e3f2b94a61c8d3 | summary against records | stale summary | deck is short | planned | wrap | children stay | gslides, linear | +1 | kept as a distractor |
| 11 | Robert's sub-250 reports C09Q4S613CN/1764013026.858409 | scope edge | scope adjacent | search hits them | YES | sub-250 | not filed | slack | none | kept as a distractor |
| 12 | iOS-only line CE156FDFB428/1763642769.995649 | platform scope | exception | thread shows ios | YES | ios | filed anyway | slack | none | rejected: adds a fork, no landing |
| 13 | build numbers in C05433XK267/1765310004.760809 | boundary date | date window | log is long | YES | build | qualifies or not | slack | +6 | rejected: NB-21 and SC-67-style joins are unsafe |

Selected rules:

| Rule | Record | Mechanism | Prior family | Why it applies | Nodes | Natural reading | Prior (record ids) | Controls | Over-application | After complete retrieval | Slots |
|---|---|---|---|---|---|---|---|---|---|---|---|
| INLINE | harmonygames-Games/GameOfDominoes#1905 | A24 | done_gap | same mechanism: a merged PR is the done source and the missing piece sits in an inline review comment | T_INLINE_TD, T_INLINE_AXE | a merged PR with Brian's tick means the child is Done | Beta(3.0,3.0) hev_7f44d83eaad625e9, hev_522f1ca2bc9062de, hev_b8f28a892a74b855 | ENG-2417, ENG-2432 | inline_over: holds a child whose PR has no inline comment | retrieval-shaped, placement decides | I1, I2, I3, I4, V4 |
| REPLY | CE156FDFB428/1763549455.195819 | A11 | superseding | same mechanism: a dated correction in a thread reply under an unrelated root | T_REPLY | a ticked line is fixed | Beta(1.0,5.0) hev_e61e07235eadbd24, hev_1ceea0e7e912f48b, hev_ebc012c844829411 | the Purple bg line | reply_over: reopens another ticked line | retrieval-shaped, placement decides | B3, B4, V1, V3 |
| BACK | CE156FDFB428/1763642831.967359 | A11 | superseding | same mechanism: a dated correction in a 1:1 DM off the delegation path | T_BACK | a ticked line is fixed | Beta(1.0,5.0) hev_e61e07235eadbd24, hev_1ceea0e7e912f48b, hev_ebc012c844829411 | the character frames line | back_over: reopens another ticked line | retrieval-shaped, placement decides | B1, B2, V1, V3 |
| FOLLOW | ENG-2417 | A15 | authority | closest ledger family: a rule homed in a card comment off the named path; house_rule has no record | T_FOLLOW | any note on a child is enough | Beta(1.0,1.0) hev_d17e4abe74f0e7e0, hev_1de494f0682754d6, hev_4638d80f1d9f6311 | the moved children | follow_over: none | retrieval-shaped, placement decides | O1, O2, O3 |
| GONE | C09SWTHEMEW/1764659626.614679 | A15 | exact_predicate | closest ledger family: a condition in older records changes which items qualify; house_rule has no record | T_GONE, T_WINGS | an unticked line is still broken | Beta(2.0,4.0) hev_9c403cae42eb4df8, hev_c2297d21ba5cbc7b, hev_0e15eed886c6fd32 | the team navigation line | gone_over: cancels a line that is not about lives | join needed | G1, G2, G3, G4, V1, V3, V4 |
| LINE | harmonygames-Games/GameOfDominoes#1913 | A24 | done_gap | same mechanism: a done claim in one service with the missing piece in another | T_LINE | fixed and did a PR means it shipped | Beta(3.0,3.0) hev_7f44d83eaad625e9, hev_522f1ca2bc9062de, hev_b8f28a892a74b855 | the treasure button post | line_over: holds a post whose fix did land | claim must be doubted | L1, L2, V1, V3 |
| ELSE | C05V5FNLB9V/1764659550.713509 | A25 | completion_elsewhere | same mechanism: a thread left open while another record shows the work done | T_ELSE_FLICKER, T_ELSE_MUSIC, T_ELSE_ACID | a thread nobody closed is still broken | Beta(1.0,4.0) hev_13d86dcf23442708, hev_638d1ef495e65d17, hev_58dcdb13d83f424d | the mega tile post | else_over: closes a post nobody fixed | retrieval-shaped, placement decides | E1, E2, E3, V1, V3 |
| ALIAS | ENG-2073 | A7 | scope_alias | same mechanism: a line and an existing ticket named differently, tied by a dated note | T_ALIAS_APPLE, T_ALIAS_SPLASH | no matching title means a new ticket | Beta(1.0,4.0) hev_ab2508cad060b0ac, hev_ace612d2f2268cdf, hev_9cefe52f59fd5be5 | the team navigation line | alias_over: reuses a ticket for a line with none | join needed | A1, A2, A3, V2 |

Four A5b checks per rule: **incorporated** (each chain runs from AN1 through H1 or a fragment); **tool-surface proof** (each deciding record is returned by the natural call for its service, checked in the pre-check); **graded weight** (slots above); **survives retrieval** (column above).

### Liveness flags (S5b)

`trap_liveness.py --design`, verbatim:

```
TRAP LIVENESS · ADVISORY · UNCALIBRATED · lexical warnings, not proof · DESIGN (no SQL: record text unavailable, only manifest-structure flags can fire) · on the Season Pass backtests these are development fixtures, not validation
  hub D05S1S2AB5M/1770937805.214409 · direct delegations 4 · rule placement: A15 nodes only: ['T_FOLLOW', 'T_GONE', 'T_WINGS'] (mechanism_portfolio); every other node SKIP
  T_INLINE_TD done_gap           -  [rule placement SKIP: not an A15 node]
  T_WINGS eliminating_eviden -
  T_INLINE_AXE done_gap           -  [rule placement SKIP: not an A15 node]
  T_SEASON superseding        -  [rule placement SKIP: not an A15 node]
  T_REPLY superseding        -  [rule placement SKIP: not an A15 node]
  T_BACK superseding        -  [rule placement SKIP: not an A15 node]
  T_GONE effective_date     breadcrumb
  T_LINE done_gap           -  [rule placement SKIP: not an A15 node]
  T_ELSE_FLICKER completion_elsewhe -  [rule placement SKIP: not an A15 node]
  T_ELSE_MUSIC completion_elsewhe -  [rule placement SKIP: not an A15 node]
  T_ELSE_ACID completion_elsewhe -  [rule placement SKIP: not an A15 node]
  T_ALIAS_APPLE scope_alias        -  [rule placement SKIP: not an A15 node]
  T_ALIAS_SPLASH scope_alias        -  [rule placement SKIP: not an A15 node]
  T_FILT exact_predicate    breadcrumb  [rule placement SKIP: not an A15 node]
  T_FOLLOW authority          -
  D_ZMCANVAS distractor         breadcrumb  [rule placement SKIP: not an A15 node]
  D_SIGNIN distractor         -  [rule placement SKIP: not an A15 node]
  D_LIVESTICKETS distractor         -  [rule placement SKIP: not an A15 node]
  D_ZMDOC distractor         breadcrumb  [rule placement SKIP: not an A15 node]
  D_SUB250 distractor         breadcrumb  [rule placement SKIP: not an A15 node]
  D_DECK distractor         -  [rule placement SKIP: not an A15 node]
  D_ECONCANVAS distractor         breadcrumb  [rule placement SKIP: not an A15 node]
  H2-decoy  68d284b84b7e9a3c5d16e208     - (not in the SQL overlay: not read)
  dispositions: 0/6 recorded
```

Dispositions: `T_GONE` breadcrumb: keep. The word 'lives' is shared with the hub-free canvas lines; it is the fair findability term and the rule itself never says it (H1). `T_FILT`, `D_ZMCANVAS`, `D_ZMDOC`, `D_SUB250` breadcrumbs: keep. These are scoped by H1 on purpose, so their terms must stay findable; a liveness flag is never fixed by removing a UGT link. `H2-decoy` not read: no SQL yet, re-run at injection. Nothing flagged on INLINE, REPLY, BACK or FOLLOW, which carry the landing weight.

`hardness_v2_check.py --design`, verbatim:

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      4 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 5 requirements: {'R5': ['INLINE'], 'R6': ['FOLLOW'], 'R9': ['GONE'], 'R2': ['LINE', 'ELSE'], 'R3': ['ALIAS']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   8 of 8 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     1 weight-5 total(s); 1 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  CLEAN      RULE_IN_PROMPT  no run of 8 resolver words in the prompt  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

Dispositions: no FLAG or UNRESOLVED. The tool reads declared containers, so it re-runs on the SQL. BACK and REPLY are Slack-to-Slack: cross-container, not cross-service.

## 6 Failure-diversity plan

Each channel is found by a different habit, so runs fail different subsets: INLINE (reading inline comments on PRs), REPLY (opening a thread under an unrelated post), BACK (reading a 1:1 with Marcus), ELSE (reading #builds or a DM with Brian), FOLLOW (reading a card comment), GONE (asking what the live build contains), LINE (looking a PR up), ALIAS (searching mail and ticket notes). No discovery gates most requirements: the largest channel, GONE, moves about 20.5 % of the weight (`plan/policy_model_output.txt`). Trap independence: each rule has its own member, so a run that beats the others can still fail it. Records: C05V5FNLB9V/1764329192.159229, CE156FDFB428/1763642831.967359, harmonygames-Games/GameOfDominoes#1905.

## 7 Deliverables and dependent writes

| Write | Tool | Count | Depends on | Requirements |
|---|---|---|---|---|
| linear | linear_create_issue | 68 | T_GONE, T_LINE, T_REPLY, T_BACK, T_ELSE_FLICKER, T_ALIAS_APPLE | R1, R2, R4, R9 |
| linear | linear_create_comment | 30 | T_ALIAS_APPLE, T_ALIAS_SPLASH, T_FOLLOW | R3, R6 |
| linear | linear_update_issue | 14 | T_INLINE_TD, T_INLINE_AXE, T_SEASON, T_WINGS | R5 |
| gsheets | gsheets_values_update | 3 | T_GONE, T_ALIAS_APPLE | R7 |
| gdrive | gdrive_share_file | 3 | K6 | R7 |
| slack | slack_send_message | 1 | T_GONE, T_INLINE_TD, T_ALIAS_APPLE | R8 |

Reuse-versus-create: two lines reuse ENG-2073 and ENG-2363. High-count writes are template-identical, so the rubric can sample them: the tick-line tickets, the child moves and the child notes. Full plan in `plan/truth_sketch.json`.

## 8 Service role map

| Service | Role | Load-bearing fact or write | Carrier |
|---|---|---|---|
| slack | canvas lines, later bugs, hub, corrections | the bug record and every correction live here | ● |
| linear | destination and tree | every record is written here and the tree states are decided here | ● |
| github | PR truth | open and merged PRs and inline review comments decide fixes and child states | ● |
| gdocs | rule doc and economy doc | the outcomes and the lives removal are read here | ● |
| gdrive | destination folder | the sheet goes in Owen's folder | ● |
| gsheets | index sheet | the deliverable index | ● |
| gslides | sprint wrap deck | the convincing done summary the child records overturn | ● |
| trello | closing rule | Brian's rule sets what every child note must name | ● |
| gmail | alias note | Vincent's mail ties the Apple sync line to its ticket | ● |
| gcal | share list | the review invite fixes who the sheet is shared with | ● |
| contacts | not used | no load-bearing fact | ○ |
| confluence | base only, off the graded path | no load-bearing fact | ○ |
| snowflake | off the graded path | NB-21 joins are unsafe | ○ |

## 9 Call budget

| Phase | Service | Calls | Reason |
|---|---|---|---|
| discovery | slack | 4 | Arthur's DM, #prototype context, canvas channel lookup |
| discovery | gdocs | 2 | rule doc read |
| discovery | gdrive | 3 | folder and doc location |
| discovery | gcal | 2 | review invite attendees |
| discovery | linear | 6 | tree parents, statuses, labels, users |
| rules | trello | 3 | finding Brian's closing rule |
| enumeration | slack | 14 | canvas pages, #god-bugs pages, #builds searches, BoomBit posts |
| enumeration | linear | 4 | open ENG tickets |
| enumeration | github | 6 | PR search for tree and bug fixes |
| enumeration | gdocs | 2 | economy doc |
| enumeration | gmail | 2 | sign-in mail search |
| enumeration | gslides | 1 | wrap deck |
| per-record | linear | 47 | comments on 32 tree records and about 15 candidate tickets: each answers a distinct question |
| per-record | github | 26 | reviews and inline comments on 13 merged PRs |
| per-record | slack | 35 | thread reads on lines that need one |
| per-record | linear | 117 | one record per bug line, child moves and child notes: each is a distinct target with no batch form |
| writes | gsheets | 3 | index sheet create and fill |
| writes | gdrive | 2 | move and share |
| writes | slack | 1 | reply to Arthur |
| read-back | linear | 3 | confirm filed records |
| read-back | gsheets | 2 | confirm the index |

Total 285 unconditional calls over 10 services. The requester's floor is over 130 in every run: about 120 per-entry writes happen whichever traps land, and reads have not fallen below 54 on comparable stored runs, so the model's mean six-run minimum is about 182 (`plan/policy_model_output.txt`, UNCALIBRATED). The golden-run rule still applies: a correct run needs these calls. Filing only unfixed lines would cut about 55 writes and put the weakest run near 116, which is why the whole list goes over.

## 10 QC rails

### Two-reading table

| Decision point | Best reading | Strongest alternative | Resolved by |
|---|---|---|---|
| What 'still broken' tests | the build players have (H1) | develop | H1 f_3ca9e15d7b20f4e681ad52 states it |
| A tick with no later record | Fixed | re-verify every line | H1: a tick stands unless a later record says otherwise |
| Lives lines | Gone | Broken, or covered by ENG-2277 | C09SWTHEMEW/1764659626.614679, f_948768f5a462e7037d17c9 and C05KNDCHAAG January no-lives post |
| Tile dozer window | Broken | Fixed on Marcus's word | harmonygames-Games/GameOfDominoes#1913 open; H1: an open PR doesn't count |
| Flicker thread | Fixed | Broken, nobody closed it | commit a6fb440f0c in #1914 and C05433XK267/1765310004.760809 |
| Apple sync line | Covered by ENG-2073 | new ticket, or ENG-2280 | Vincent's mail owen.baker@harmonygames.co/1849333980856689601 |
| Population edge | canvas plus bug channel | Robert's sub-250 reports too | H1 folds them in; base C09Q4S613CN/1764092109.741509 |
| Child with a merged PR and an inline hold | stays | Done | Arthur's inline comment harmonygames-Games/GameOfDominoes#1905#rc_1 says it must be done first |
| Which note wording | names the build | any line | H2 690b29bc3c7d2e51b0f86a47 |
| Share list | Arthur, Robert, Oliver | everyone on the DM | invite evt_6e2c91d4b07f3a58c1d2e4 |
| Ticked line about lives or Win & Collect | Fixed | Gone | H1: take the first outcome that fits, and Fixed comes first; CE156FDFB428/1763042343.632569 |
| Unticked lives line against open ENG-2277 | Gone | Covered | H1 order puts Gone before Covered; ENG-2277 |
| Train and team lines with a fix commit | Broken | Fixed by the commit | Vincent's later replies CE156FDFB428/1763845212.507119 and CE156FDFB428/1763742012.611229 say they still happen; H1: nothing later says otherwise is the test |
| ENG-2424 with no hold note | stays | Done | Owen's Dec 16 post C9CA62B5180A/1765927876.696389 says the event is disabled; no re-enable is on record |
| A broken bug on an open child's screen | child still moves | child held | H1: a bug on a screen doesn't hold its child; ENG-2432 |

### Reach table (load-bearing records)

Every scoped base record below is YES for Owen (`persona_view.py can-see owen_baker …`); planned seeds are checked by `check-sql` at injection:

```
owen_baker slack D05S1S2AB5M: YES   reason:   persona EMPLOYEE_0021_SLACK_ID is in members of im D05S1S2AB5M 
owen_baker slack D05USBTQY1F: YES   reason:   persona EMPLOYEE_0021_SLACK_ID is in members of im D05USBTQY1F 
owen_baker slack D07E9PSQB6W: YES   reason:   persona EMPLOYEE_0021_SLACK_ID is in members of im D07E9PSQB6W 
owen_baker slack CE156FDFB428/1763642831.967359: YES   reason:   message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F
owen_baker slack CE156FDFB428/1763549455.195819: YES   reason:   message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F
owen_baker slack CE156FDFB428/1763548856.943389: YES   reason:   message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F
owen_baker slack CE156FDFB428/1763642552.651279: YES   reason:   message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F
owen_baker slack CE156FDFB428/1763642659.467529: YES   reason:   message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F
owen_baker slack CE156FDFB428/1763041538.186339: YES   reason:   message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F
owen_baker slack CE156FDFB428/1763132009.017599: YES   reason:   message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F
owen_baker slack CE156FDFB428/1763394823.486369: YES   reason:   message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F
owen_baker slack CE156FDFB428/1763549817.580759: YES   reason:   message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of public FC:F
owen_baker slack C05V5FNLB9V/1764256187.655299: YES   reason:   message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of private god-
owen_baker slack C05V5FNLB9V/1764329192.159229: YES   reason:   thread reply inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of private
owen_baker slack C05V5FNLB9V/1764659550.713509: YES   reason:   message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of private god-
owen_baker slack C05V5FNLB9V/1764660142.352319: YES   reason:   message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of private god-
owen_baker slack C05V5FNLB9V/1764661312.152719: YES   reason:   message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of private god-
owen_baker slack C05V5FNLB9V/1764661921.018749: YES   reason:   message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of private god-
owen_baker slack C05V5FNLB9V/1766415326.501939: YES   reason:   message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of private god-
owen_baker slack C09SWTHEMEW/1764659626.614679: YES   reason:   message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of private publ
owen_baker slack C09SWTHEMEW/1770926214.816149: YES   reason:   thread reply inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of private
owen_baker slack C05433XK267/1765310004.760809: YES   reason:   message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of public build
owen_baker slack C05433XK267/1764977839.069349: YES   reason:   message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of public build
owen_baker slack C09Q4S613CN/1764042435.541279: YES   reason:   message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of public dd-ro
owen_baker slack C9CA62B5180A/1765927876.696389: YES   reason:   message inherits channel: persona EMPLOYEE_0021_SLACK_ID is in members of mpim mpdm-l
owen_baker gdocs f_948768f5a462e7037d17c9: YES   reason:   file is shared with the persona (shared_with_emails) 
owen_baker gdrive d_4e13bd40cc73d0fc76f87c: YES   reason:   persona owns the file
```

Feasibility: `linear_create_issue` (team, parentId, labels, state), `linear_update_issue`, `linear_create_comment`, `gsheets_create_spreadsheet`, `gdrive_move_file`, `gdrive_share_file` and `slack_send_message` are all in `Evals/references/tools/catalog.json`. Owen owns the folder d_9b41e7c2a05d36f8e1c7a4 and the sheet he creates (learnings §31). Linear is unscoped.

Precedence: load-bearing facts sit only in ● carriers, with Linear comments ● per `Ask_Carriers.md` §6b. No fact lives only in a GCal description or on Confluence. Naturalness: the prompt names the DM, the tree, the folder and the reply; it names no bug, channel, rule or count. Grading devices: exact counts, ≤ 5 samples per group plus a volume slot, one row per trap member, exclusions as a state or count on a required write, never 'leaves X alone'.

### Coherence rail

Every section 1a row is dispositioned. Every designed disagreement is a dated human claim with a later record. Companions are planned in section 11. Claims about base artifacts stay observational: `00_PreScenario/git_containment_check.txt` shows #1913's commit 4e344c5291 is not in #1914's list, and fix commits a6fb440f0c, 9afe3918b5 and d0b222c9cf are. The git export holds only 50 commits on main, so branch containment comes from the PR commit lists. No exact branch name is graded (NB-13).

## 11 Record plan for /create-injection

| Seed | Service | Id | Home record | Author | At | Purpose |
|---|---|---|---|---|---|---|
| hub | slack | D05S1S2AB5M/1770937805.214409 | D05S1S2AB5M/1770937805.214409 | Arthur Blake | 2026-02-12T23:10:05Z | hey, one thing before the next BoomBit sync. Once the data export is done Slack drops to t |
| rule_doc | gdocs | f_3ca9e15d7b20f4e681ad52 | f_3ca9e15d7b20f4e681ad52 | Arthur Blake | 2026-02-12T22:48:00Z | DD bug carry-over notes  What goes over: every ticked or unticked line in the comment chan |
| decoy_doc | gdocs | f_72e0b4c3d91a5f68c2b7e4 | f_72e0b4c3d91a5f68c2b7e4 | Brian Foster | 2025-09-24T14:10:00Z | Zombie Match bug list notes  ZM bugs go on the ZOM team. A tick on a ZM canvas means QA pa |
| amend | linear | comment_49b5ac4788465f72ddf245e34f2b7034 | ENG-2401 | Arthur Blake | 2026-02-13T00:40:00Z | For the carry-over: put [2231] at the front of every title you file so I can filter them. |
| vincent_note | slack | D05USBTQY1F/1765452012.418229 | D05USBTQY1F/1765452012.418229 | Marcus Bennett | 2025-12-11T11:20:12Z | the Tavern buttons lost their frame again on last night's Android build, I looked at the p |
| brian_reply | slack | C09Q4S613CN/1764606918.318209 | C09Q4S613CN/1764042435.541279 | Brian Foster | 2025-12-01T16:35:18Z | I was back in the shop prefabs today, the round icons on the River Tile and Memory Tile sh |
| brian_dm | slack | D07E9PSQB6W/1765206644.602119 | D07E9PSQB6W/1765206644.602119 | Brian Foster | 2025-12-08T15:10:44Z | music plays normally on my side since your audio player change, and Nate's acid throw line |
| bar_reply | slack | C05V5FNLB9V/1767021345.207719 | C05V5FNLB9V/1766415326.501939 | Brian Foster | 2025-12-29T15:15:45Z | the new camera setup fixed it, the bottom bar and the top panel both show on the devices I |
| mail | gmail | owen.baker@harmonygames.co/1849333980856689601 | owen.baker@harmonygames.co/1849333980856689601 | Vincent Parker | 2025-11-20T18:12:00Z | Subject: sign in lines on my list  The Apple sync line on my Android list comes down to th |
| alias_note | linear | comment_7ab5299cbb609d95ba12249d315daedc | ENG-2363 | Vincent Parker | 2025-11-20T18:20:00Z | Android still hits this: the manual sign-in line on my list gets stuck on loading after si |
| rule_comment | trello | 690b29bc3c7d2e51b0f86a47 | 690b27282f4c1b7a6e93d512 | Brian Foster | 2025-11-05T10:41:00Z | When we close these UI tickets out every one gets a note naming the current public build,  |
| zm_comment | trello | 68d284b84b7e9a3c5d16e208 | 6851a6569f3bf818760632ab | Brian Foster | 2025-09-23T11:30:00Z | ZM close-outs just need the ticket state, no note. |
| deck | gslides | f_d15a8c70e3f2b94a61c8d3 | f_d15a8c70e3f2b94a61c8d3 | Brian Foster | 2025-11-21T20:30:00Z | UI optimization wrap  UI pass wrapped up. Core, Live-Ops and Mini-Games main screens are o |
| season_note | linear | comment_d6aee2099bd71050facc422ccef8f809 | ENG-2428 | Oliver Brooks | 2025-12-05T12:30:00Z | The illustrations went in but the reward track still uses the old frames, this isn't finis |
| gift_note | linear | comment_3e81bf306c58746580a9cfa0ca12bd60 | ENG-2437 | Brian Foster | 2025-11-24T16:00:00Z | Ran out of time on this one, the panel never got its last pass before the build went out. |
| inline_td | github | harmonygames-Games/GameOfDominoes#1905#rc_1 | harmonygames-Games/GameOfDominoes#1905 | Arthur Blake | 2025-11-19T13:05:35Z | Approving so we can keep moving, but the Tile Dozer how-to-play popup still points at the  |
| inline_axe | github | harmonygames-Games/GameOfDominoes#1908#rc_1 | harmonygames-Games/GameOfDominoes#1908 | Arthur Blake | 2025-11-20T01:51:55Z | Fine to merge, but the Axe Arena info popup keeps the old frame here. Needs doing before t |
| flick_reply | slack | C09Q4S613CN/1766164222.418229 | C09Q4S613CN/1766164222.418229 | Robert | 2025-12-19T17:10:22Z | the flickering is gone on this week's build, both on the play button and coming out of a l |
| train_reply | slack | CE156FDFB428/1763845212.507119 | CE156FDFB428/1763394823.486369 | Vincent Parker | 2025-11-22T21:00:12Z | better but the snow train is still off and the green shows, leaving this one open |
| team_reply | slack | CE156FDFB428/1763742012.611229 | CE156FDFB428/1763549817.580759 | Vincent Parker | 2025-11-21T16:20:12Z | the leave team popup is fine now but the navigation bar still goes after quitting |
| lives_reply1 | slack | CE156FDFB428/1763845812.703339 | CE156FDFB428/1763548856.943389 | Vincent Parker | 2025-11-22T21:10:12Z | same after Oliver's change, a loss still doesn't take a life |
| lives_reply2 | slack | CE156FDFB428/1763845872.804449 | CE156FDFB428/1763642552.651279 | Vincent Parker | 2025-11-22T21:11:12Z | same here, it still only drops on the second loss |
| invite | gcal | evt_6e2c91d4b07f3a58c1d2e4 | evt_6e2c91d4b07f3a58c1d2e4 | Arthur Blake | 2026-02-12T23:05:00Z | DD bug review, Sunday Feb 15 17:00 UTC. Attendees: Arthur Blake, Robert, Oliver Brooks, Ow |

Also planned, each with a stated purpose: Brian's check notes on the Validation children ENG-2410, ENG-2429 and ENG-2430; Brian's 28-item screen checklist on the Trello card, the per-screen record for the children in PR state; triage notes on open ENG bug tickets (reuse controls, for example ENG-2280); PR conversation comments on the 13 merged tree PRs with INT-01 copies in #engineering-bots C050WGU41HR; control replies on ticked lines in CE156FDFB428; Drive and Docs rows for f_3ca9e15d7b20f4e681ad52, f_72e0b4c3d91a5f68c2b7e4, f_d15a8c70e3f2b94a61c8d3 and d_9b41e7c2a05d36f8e1c7a4; the Trello card and its comment on list 66c38013d3990617429e50e3 with the ZM decoy card on board 6851a6569f3bf818760632ab; GCal copies of evt_6e2c91d4b07f3a58c1d2e4 per attendee; SQL UPDATEs moving the 14 PR-state tree tickets and ENG-2405 to Validation. Estimated 110–135 INSERTs. If honest evidence falls short, that comes back to the requester rather than being padded.

### Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| github | INT-01, INT-02, INT-12 | Slack app mirror; push notices; notification mails | INT-01 copies for each seeded PR comment in C050WGU41HR under the PR's opened message; review containers declared per learnings §53 |
| linear | INT-03, INT-04, INT-05 | linear[bot] on PRs; Slack posts; digests | none needed for comments on open tickets; declared at injection |
| gcal | INT-11 | invitation mails | seed invitations for attendees, or no_notify |
| gdrive | INT-13 | Drive app DMs | none: shares by notice only; declared |
| slack | INT-22 | Slack email notices | none for DMs after the plan change; declared |
| trello | INT-21 | no Trello to Slack integration | none |
| gmail | none | Vincent's mail is ordinary mail | none |
| jenkins (slack) | INT-06 | #builds job posts | none seeded: base posts only |

## 12 Self-test results

`hardness_gate.py --design`, verbatim:

```
HARDNESS GATE (extreme (design)): PASS
  [ok] assignment_context: manifest bound to current V3 assignment, freeze and policy
  [ok] effective_profile: effective_profile 'extreme' for 'Long Horizon' → thresholds 'extreme'
  [ok] sql_lint_clean: skipped (--design: no SQL yet)
  [ok] base_consistency: skipped (--design: no SQL yet)
  [ok] services_injected: skipped (--design: no SQL yet)
  [ok] rows: skipped (--design: no SQL yet)
  [ok] services_carrying_weight: 10 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: skipped (--design: no SQL yet)
  [ok] seeded_ids_exist_in_sql: skipped (--design: no SQL yet)
  [ok] anchors: 2 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 12 fragments; need ≥ 12
  [ok] ask_fragment_services: 7 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 12 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 9 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 102; need ≥ 40 (source-defined: True)
  [ok] evidence_surfaces: 4 surfaces over 3 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 108; need ≥ 100
  [ok] call_budget: unconditional (verified) floor 285 of 285 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 250 (requester-confirmed volume_exception)
  [ok] call_budget_spread: 10 services in budget; largest share outside the per-record phase 32% (≤ 50%)
  [ok] traps: 22 traps across 9 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 6 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 4 supersessions (2 with versions in ≥ 2 services, 1 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: skipped (--design: no SQL yet)
  [ok] distractors: 7 distractors of 5 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 7 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 5 chains with 5 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] mechanism_portfolio: 8 portfolio entries, each a mechanism-enum id with trap/chain nodes, a requirement, a natural-reading fallback and a prior family with its reason
  [ok] artifact_fields: declared ['gradable_surface']: paths relative, digests sha256
  [ok] hidden_authorities: 2 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 2 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 5 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 9 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 6 writes over 4 services; each must depend on findings
  [note] volume_exception: call-budget floor 250 and per-record floor 100 replace 500 and 300; every other extreme target applies — reason: 102 cohort records and about 285 honest calls; reaching 500 would need padding, ; requester confirmation: requester, Claude Code chat 2026-11-07: 'i want over 130 tool calls in each runs
```

`gradable_surface.py validate`, verbatim:

```
GRADABLE SURFACE (01_Gradable_Surface.json): PASS · 49 slots · weight 151 · mechanism share 76.8% (reported, not gated) · weight by class {'aggregate': 8, 'write_content': 67, 'direct': 74, 'delivery': 2}
```

`gradable_surface.py gradeable-report`, verbatim:

```
SURFACE.GRADEABLE PASS · 49 slot(s) · {'GRADABLE': 49}
```

Lazy-solver pass: a run that reads the canvas once and files ticks as written scores about a quarter of the surface (`plan/policy_model_output.txt`); the points it keeps are sampled lookups and delivery rows, with no leak on a trap row. Literal-value sweep: `0.3.310` appears only in H1 and in notes the run writes. Wording sweep: the corrections avoid 'canvas' and ticket words (C09Q4S613CN thread, D05USBTQY1F). 'The rest stands': K4 changes one clause and no later record restates it.

Requester targets, whole policies and six-run model, UNCALIBRATED:

```
UNCALIBRATED · surface: 49 slots, total weight 151, mechanism-flippable 116 (76.8%)

Whole policies
  100.0%  Perfect  [lands: -]
   23.2%  Canvas ticks at face value, nothing else  [lands: ALIAS, BACK, ELSE, FOLLOW, GONE, INLINE, LINE, REPLY]
   86.1%  Reads PR reviews but never inline comments, otherwise perfect  [lands: INLINE]
   58.3%  Thorough, never opens threads under unrelated posts or other DMs  [lands: BACK, ELSE, INLINE, REPLY]
   72.2%  Stays with the named records, otherwise thorough  [lands: BACK, ELSE, REPLY]
   63.6%  Reads everything, never asks what the live build contains  [lands: ELSE, GONE, LINE]
   92.7%  Right calls, misses the note rule  [lands: FOLLOW]

Single misses
  INLINE  86.1%
  REPLY   86.1%
  BACK    86.1%
  FOLLOW  92.7%
  ELSE    82.8%
  GONE    79.5%
  LINE    88.1%
  ALIAS   88.1%

Pairs at or above the 80 % line: ['REPLY+BACK', 'REPLY+LINE', 'BACK+LINE', 'FOLLOW+LINE', 'FOLLOW+ALIAS']

P(one run catches every trap) ~ 0.003 (independence); expected landings per run at design rates 3.75
Triples at or above the 80 % line: none

One pre-check run under the narrow-miss rule (one cause under 15 % caps /hardness at 2), independence
  scale 1.00: P(two or more causes, or one cause losing 15 % or more) = 0.97
  scale 0.70: P(two or more causes, or one cause losing 15 % or more) = 0.83
  scale 0.50: P(two or more causes, or one cause losing 15 % or more) = 0.65

Six-run Monte Carlo, carrier rates (scale x rho)
  scale  rho   mean-land  E[avg]  P(<80)  P(SD)  P(<5 full)  P(pat)  P(>130 all six)  mean-min-calls  P(all)
  1.00  0.30      0.47   58.9%    1.00   0.88       1.00    1.00            1.00            181    0.88
  1.00  0.60      0.47   59.7%    0.98   0.95       1.00    0.99            1.00            181    0.93
  0.80  0.35      0.38   66.3%    0.95   0.93       1.00    1.00            1.00            181    0.89
  0.70  0.35      0.33   70.1%    0.89   0.93       1.00    1.00            1.00            181    0.84
  0.60  0.35      0.28   73.9%    0.77   0.93       1.00    1.00            1.00            181    0.73
  0.60  0.60      0.28   74.7%    0.70   0.92       1.00    0.99            1.00            181    0.65
  0.50  0.35      0.23   77.8%    0.60   0.90       1.00    0.99            1.00            181    0.57
  0.40  0.35      0.19   81.8%    0.39   0.85       1.00    0.99            1.00            181    0.37

Ledger view (scale x rho)
  1.00  0.35      0.32   70.9%    0.86   0.93       1.00    1.00            1.00            181    0.82
  0.70  0.35      0.22   78.9%    0.54   0.89       1.00    0.99            1.00            181    0.51

Rubric inflation view: /rubric adds always-pass per-target rows (carrier rates, rho .35)
  + 30 weight  1.00  0.35      0.47   65.8%    0.98   0.82       1.00    1.00            1.00            181    0.80
  + 30 weight  0.70  0.35      0.33   75.0%    0.77   0.86       1.00    1.00            1.00            181    0.68
  + 60 weight  1.00  0.35      0.47   70.7%    0.95   0.70       1.00    1.00            1.00            181    0.66
  + 60 weight  0.70  0.35      0.33   78.6%    0.59   0.76       1.00    1.00            1.00            181    0.47
  +100 weight  1.00  0.35      0.47   75.3%    0.84   0.50       1.00    1.00            1.00            181    0.42
  +100 weight  0.70  0.35      0.33   82.0%    0.34   0.56       1.00    1.00            1.00            181    0.21
```

S9b prior forecast (advisory, UNCALIBRATED): ledger record hev_9d17a8ebbe17cc08, pre-registered. E[avg] 0.728 (independent and source) to 0.750 (correlated), P(all four gates at the platform cap) 0.488 to 0.534. These use ledger family means, lower than the carrier rates in `plan/policy_model_output.txt`, and both views are reported. Against the requester's stricter 80 % line the ledger view is the cautious one.

### Self-review

Re-read `Evals/1_Prompt_Eval.md` §2.1, §2.2 and §3.2 and `Evals/0_Injection_Quality_Eval.md` Check C in order.

| Area | Counter-reading (strongest argument it fails) | Resolution (evidence) |
|---|---|---|
| temporal | the hub could postdate the export and read as invented | hub D05S1S2AB5M/1770937805.214409 is before Feb 13 10:03 UTC; NB-6; T07 hazard avoided |
| temporal | Vincent's replies could postdate his exit | CE156FDFB428/1763845212.507119 is Nov 22; his last Slack is C09Q4S613CN/1763890610.357549 |
| semantic | 'Gone' could read as deleted from the backlog | H1 f_3ca9e15d7b20f4e681ad52 defines it as a bug in something the live build lacks |
| semantic | a tick might mean only 'looked at' | H1 says a tick stands; Vincent's own words at C05V5FNLB9V/1763042988.277099 call the list remaining issues |
| cross-service referential | the mail names ENG-2073, which must fit the line | ENG-2073 'Sign-In Account Synchronization Issues' is open; line CE156FDFB428/1763041538.186339 |
| cross-service referential | a seeded inline comment needs a PR that took reviews | harmonygames-Games/GameOfDominoes#1905 has Arthur's APPROVED review; the comment predates merge |
| quantitative | the counts could cancel out | V1 and the reply rows sit beside named member rows; CE156FDFB428/1763642831.967359 |
| quantitative | 68 new tickets assumes 63 plus 7 less 2 | plan/truth_sketch.json: 70 items, 2 Covered; ENG-2073 and ENG-2363 take notes |
| state/lifecycle | tree tickets in PR state fail coherence on presence | L01, L03, L07 left as they are: the job reconciles them, so the SQL updates no such ticket; ENG-2417 |
| state/lifecycle | a Done child could need reopening | no closed child is touched; ENG-2411 stays Done |
| identifier/format | a seeded id could collide | every minted id was checked with `hg.py records` and scoped Slack searches, with a positive control: `plan/out/id_collisions.txt`, 0 hits; f_3ca9e15d7b20f4e681ad52 |
| other | Owen can't read #god-bugs as a guest | the SQL seeds his rejoin in each DD channel on Feb 12, and C05V5FNLB9V/1764256187.655299 predates Feb 11 |
| other | filing 58 fixed lines is padding | hub gives the reason: the list exists only in Slack; each is a distinct bug; long_horizon.md; CE156FDFB428/1763041126.468099 |
| decision: What 'still broken' tests | the alternative 'develop' could be a fair answer | H1 f_3ca9e15d7b20f4e681ad52 states it |
| decision: A tick with no later record | the alternative 're-verify every line' could be a fair answer | H1: a tick stands unless a later record says otherwise |
| decision: Lives lines | the alternative 'Broken, or covered by ENG-2277' could be a fair answer | C09SWTHEMEW/1764659626.614679, f_948768f5a462e7037d17c9 and C05KNDCHAAG January no-lives post |
| decision: Tile dozer window | the alternative 'Fixed on Marcus's word' could be a fair answer | harmonygames-Games/GameOfDominoes#1913 open; H1: an open PR doesn't count |
| decision: Flicker thread | the alternative 'Broken, nobody closed it' could be a fair answer | commit a6fb440f0c in #1914 and C05433XK267/1765310004.760809 |
| decision: Apple sync line | the alternative 'new ticket, or ENG-2280' could be a fair answer | Vincent's mail owen.baker@harmonygames.co/1849333980856689601 |
| decision: Population edge | the alternative 'Robert's sub-250 reports too' could be a fair answer | H1 folds them in; base C09Q4S613CN/1764092109.741509 |
| decision: Child with a merged PR and an inline hold | the alternative 'Done' could be a fair answer | Arthur's inline comment harmonygames-Games/GameOfDominoes#1905#rc_1 says it must be done first |
| decision: Which note wording | the alternative 'any line' could be a fair answer | H2 690b29bc3c7d2e51b0f86a47 |
| decision: Share list | the alternative 'everyone on the DM' could be a fair answer | invite evt_6e2c91d4b07f3a58c1d2e4 |
| decision: Ticked line about lives or Win & Collect | the alternative 'Gone' could be a fair answer | H1: take the first outcome that fits, and Fixed comes first; CE156FDFB428/1763042343.632569 |
| decision: Unticked lives line against open ENG-2277 | the alternative 'Covered' could be a fair answer | H1 order puts Gone before Covered; ENG-2277 |
| decision: Train and team lines with a fix commit | the alternative 'Fixed by the commit' could be a fair answer | Vincent's later replies CE156FDFB428/1763845212.507119 and CE156FDFB428/1763742012.611229 say they still happen; H1: nothing later says otherwise is the test |
| decision: ENG-2424 with no hold note | the alternative 'Done' could be a fair answer | Owen's Dec 16 post C9CA62B5180A/1765927876.696389 says the event is disabled; no re-enable is on record |
| decision: A broken bug on an open child's screen | the alternative 'child held' could be a fair answer | H1: a bug on a screen doesn't hold its child; ENG-2432 |

Sources re-read through `tools/hg.py` this stage: every base pointer in sections 1 and 5. `hardness_gate.py --design` output is pasted in section 12: HARDNESS GATE (extreme (design)): PASS.

Unresolved: no independent model review of the design (RED TEAM FALLBACK in section 13); rubric growth is the main risk to the 80 % target; `linear_create_issue` at volume and a direct read of the canvas channel are to be confirmed in the pre-check; ≥ 120 INSERTs is tight.

```
STAGE GATE scenario: PASS — Task_Authoring/task_inputs · 01_Scenario_Design.md#de755e35633e · 01_Hardness_Manifest.draft.json#459add197b56 · 01_Gradable_Surface.json#6d9cd388cdbb · 00_Assigments.md#c039da1b9b09 · __context__#ba6bb23d4a12 · __assignment__#560a0d2ca2a9 · __policy__#dc4ab5df3cdd · __gate_policy__#f8638415ca2c · __review__#cd30ba058f1a · blocking 0 · warnings 0 · checks 33
[PASS] assignment.v3_context: Owen Baker / Game Engineer (Unity); medium cap <85%; freeze 2026-02-14T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe normal; KB bound; clock Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
[PASS] structure.outputs: 3 output(s) present: 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json
[PASS] structure.inputs: 1 input(s) present: 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md)
[PASS] structure.sections: 19 required sections present and non-empty (01_Scenario_Design.md)
[PASS] structure.placeholders: no placeholders in 01_Scenario_Design.md
[PASS] evidence.storyline: 11/11 items carry a source pointer (min 80%)
[PASS] evidence.coherence_audit: 18/18 items carry a source pointer (min 100%)
[PASS] evidence.hidden_authorities: 2/2 items carry a source pointer (min 100%)
[PASS] evidence.delegation: 14/14 items carry a source pointer (min 90%)
[PASS] evidence.trap_register: 48/48 items carry a source pointer (min 90%)
[PASS] evidence.record_plan: 30/31 items carry a source pointer (min 80%); unsourced e.g. L581: "gmail | none | Vincent's mail is ordinary mail | none"
[PASS] evidence.active_speakers: 8/8 items carry a source pointer (min 100%)
[PASS] tool.hardness_gate_design: hardness_gate --design pasted PASS; re-run PASS
[PASS] tool.persona_reach: persona_view reach pasted for owen.baker@harmonygames.co and matches the re-run (116 channels)
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] kb.coherence_hazards: coherence audit cites 16 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 8 speaker rows carry their activity.json status_at_clock
[PASS] kb.integrations: companions listed per integrations.json (11 INT ids, services ['gcal', 'gdocs', 'gdrive', 'github', 'gmail', 'gsheets', 'gslides', 'linear', 'slack', 'trello'])
[PASS] kb.storyline: timeline cited; cohorts ['GH-Q08', 'LIN-EPIC', 'LIN-OPEN-ENG', 'SL-T05']; trap_catalog ['B04', 'C01', 'C02', 'D07', 'K01', 'N03']
[PASS] boundary.anchor_naming: 4 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] tool.redteam_dual: red team did not run (missing 01b_Redteam_Review.md, 01b_Redteam_Review.second.md); explicit fallback recorded: two independent fresh Claude agents (general-purpose subagents, hg.py only, no prompt and 
[PASS] surface.valid: 49 slots, weight 151; geometry report-only, never gated: mechanism share 77%, always-pass share 23%
[PASS] forecast.preregistered: prior forecast pre-registered in the ledger: ['hev_9d17a8ebbe17cc08'] (UNCALIBRATED, advisory)
[SKIP] revise.intake: no MODE B report and no revision-intake section: nothing to take in
[PASS] reach.scenario: 1 scoped load-bearing ids YES for owen_baker (1 planned seeds not yet in base: verified at the injection gate)
[PASS] review.counter_readings: 28 evidenced counter-readings (of 28 found; need ≥ 22) in 01_Scenario_Design.md
[PASS] review.coverage: self-review addresses all 8 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.draft.json is bound to the current assignment, policy, source context and freeze
[PASS] v3.role_review: current role-plausibility review recorded; semantic judgment belongs to the named reviewer
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## 13 Red team (dual)

RED TEAM UNAVAILABLE: REDTEAM_* is unset (0 variables), so tools/redteam_review.py --dual cannot reach a reviewer.

RED TEAM FALLBACK: two independent fresh Claude agents (general-purpose subagents, hg.py only, no prompt and no solver) ran blind sweeps: one tried to break every planned outcome as the /prompt UGT reviewer, one tried to fail every seed against the whole base as the /injection and coherence reviewer. Chosen under the requester's delegation of 2026-11-07 because no second model family is reachable. Their reports are `plan/sweeps/fork_sweep.md` and `plan/sweeps/coherence_sweep.md`.

Sweep dispositions (each re-checked against the base through hg.py before changing the design). Full tables are in the two sweep files.

| Severity | Finding | Disposition | Evidence and change |
|---|---|---|---|
| BLOCK | inline_td, inline_axe dated after merge | Fixed | re-dated before Arthur's reviews: 2025-11-19T13:04:10Z (approved 13:05:32Z) and 2025-11-20T01:50:40Z (approved 01:51:51Z); harmonygames-Games/GameOfDominoes#1905, #1908 |
| BLOCK | td_note, axe_note predate the tickets starting | Fixed | re-dated after the merges and scoped to the main screen only; ENG-2434, ENG-2426 |
| BLOCK | shop icons line re-closed by Brian's later posts | Fixed | correction moved to Dec 1, after C09Q4S613CN/1764192110.492299 and /1764364896.416939 |
| BLOCK | ENG-2432 and ENG-2433 Done while their shop icons are Broken | Fixed | H1 now says a bug on a screen doesn't hold its child |
| BLOCK | later DD economy canvas unscoped | Fixed | H1 leaves it out; distractor D_ECONCANVAS C4208B207A1A/1765298859.629579 |
| BLOCK | 'An open PR doesn't count' is false for #1914 | Fixed | reworded: a PR that never made it into that build doesn't count; #builds shows the build line C05433XK267/1765310004.760809 |
| FORK | train and team lines have later commits, two standards | Fixed | H1 states the test once; seeded Vincent replies after each commit keep them Broken (commits 4189eca5, 100612a7) |
| FORK | Win & Collect disabled Dec 16: ticked lines and ENG-2424 | Fixed | H1 first-fit order keeps ticked lines Fixed; ENG-2424 stays (C9CA62B5180A/1765927876.696389), so 23 children end Done |
| FORK | 'has a comment thread' gives 61 or 63 lines | Fixed | H1 says every ticked or unticked line; two empty-text roots have no line (CE156FDFB428/1763042124.247899) |
| FORK | no record for ENG-2427, 2429, 2431 | Fixed | default-Done rule plus a Brian check note on each moving child |
| FORK | Tavern correction predates Brian's blanket posts | Fixed | moved to Marcus's DM on Dec 3, D05USBTQY1F, after those posts |
| FORK | lives lines could be Fixed by Oliver's commit 3646982c | Fixed | Vincent replies say the same after that change (CE156FDFB428/1763845812.703339) |
| FORK | ENG-2331 and ENG-2277 against Fixed and Gone | Fixed | H1 first-fit order: Fixed, Gone, Covered, Broken |
| FORK | still-broken count 7 or 9 | Fixed | H1: Covered ones count as still broken in the reply, so 9 |
| FIX | rule doc cited a later amendment; 'on Thursday' on a Thursday | Fixed | H1 now says 'If anything changes after this' and 'today'; ENG-2401 |
| FIX | hub overclaims and ignored Owen's guest status | Fixed | hub softened ('most of', 'once the data export is done') and gives read access back; D05S1S2AB5M |
| FIX | deck false, not stale, after the gift note | Fixed | deck dated Nov 21 and the gift note Nov 24, so the note overturns it; f_d15a8c70e3f2b94a61c8d3 |
| FIX | season note rivalled by Dec 4 commits | Fixed | note moved to Dec 5 and names the reward track; ENG-2428 |
| FIX | alias notes overclaimed the tickets | Fixed | reworded to fit ENG-2073 and ENG-2363 |
| FIX | Gmail and Trello ids did not match their dates | Fixed | regenerated from the seeded dates; mailbox id for owen.baker@harmonygames.co |
| FIX | 'sprint' is not the team's word | Fixed | seeds say 'UI work'; C09Q4S613CN has no use of it |
| LIMIT | 0.3.310 has no base record tying it to Feb 12's build | Accepted | H1 is the authority; sequence holds (C09SWTHEMEW/1770753609.436139); no row joins it to a review version (NB-21) |
| LIMIT | 'no later fix' rests on commit titles | Accepted | the rule's test is a commit named for the bug; prefab diffs are not in the export |

Injection sweep (/create-injection rev1): a third fresh reviewer read the new seeds against the base. Each finding was re-checked through hg.py before the change. It printed some SQL rows outside its list, so its view of those rows is not blind.

| Severity | Finding | Disposition | Evidence and change |
|---|---|---|---|
| BLOCK | ENG-2419 note dated before the retry screen fix | Fixed | note moved to Nov 20, after #builds DD Android #2179 and Owen's reply CE156FDFB428/1763549617.765149 |
| BLOCK | ENG-2430 note dated before the offers fix | Fixed | note moved to Nov 21, after Brian's fix on CE156FDFB428/1763549271.970799 and #2205 |
| BLOCK | ENG-2427 note dated before the River Rush sail fix | Fixed | note moved to Nov 21 15:00, after #2214 on Nov 21 04:08 (CE156FDFB428/1763394845.067219) |
| BLOCK | ENG-2425 note dated minutes after a banner bug | Fixed | note moved to Nov 21, after #2187, #2189 and #2208 (CE156FDFB428/1763131864.808869) |
| BLOCK | ENG-2398 'no bug behind it' contradicts the ticket | Fixed | reworded as the stopgap for the relogin problems |
| BLOCK | Marcus says he is on the window after finishing it | Fixed | reply now only says he hasn't got to the mega tile; C05V5FNLB9V/1764256187.655299 |
| FIX | ENG-2410 shipped offer work through #1898 | Fixed | note moved to Nov 21 with ENG-2430 |
| FIX | ENG-2429 note after the checklist tick | Fixed | note moved to 14:27, before the ENG-2404 tick at 14:29:13 |
| FIX | #1902 and #1903 claims beyond their files | Fixed | comments now name the pop up, banner and stars, and the out of moves screen; harmonygames-Games/GameOfDominoes#1902, #1903 |
| FIX | Vincent's 'too' and a same-day 1 pixel gap | Fixed | reply now reads 'looks ok now'; his gap post is about navigation tooltips, CE156FDFB428/1763394941.178509 |
| FIX | tracker and deck timing | Fixed | tracker stays Nov 20 with Season Pass 'next'; deck moves to Nov 21 after #2214; gift note moves to Nov 24 |
| FIX | tracker and deck list 6 of 15 Core children | Fixed | all 15 are listed |
| FIX | 'new atlases' has no source | Fixed | 'optimized sprites', from the #1905 body, in the deck and the Trello card |
| FIX | deck and tracker differ on Daily Gift | Accepted | tracker Nov 20 'last pass', deck Nov 21 claims it shipped, Brian's Nov 24 note corrects it: a dated human sequence |
| FIX | inline comments cite prefabs not in the export, and one hunk has identical lines | Fixed | both now anchor on files the PRs changed (CodeRabbit summaries #1905#c_2 and #1908#c_2) with new-file hunks |
| FIX | ENG-2426 note before the Axe Arena overflow report | Fixed | note moved to Nov 21 15:30, after Arthur's Done on CE156FDFB428/1763643032.027129 |
| LIMIT | could not verify the Purple fix, the 24 hours checkbox's screen, ENG-2406's video, or every channel | Accepted | the Purple line is ticked; no record about it says otherwise, and the tick rule decides it |

Later change: the Linear notes on PR-state children left the design with the hazard change (design_delta 'tree states and notes'), so the re-dated ENG-2419, ENG-2425, ENG-2427, ENG-2426 and ENG-2434 notes no longer exist; Brian's ticks on card 690b27282f4c1b7a6e93d512 carry no date. The ENG-2410, ENG-2429 and ENG-2430 fixes stand.

Fork sweep before /prompt (rev2): a fresh agent with no answer key reproduced 58 Fixed, 3 Gone, 2 Covered, 7 Broken, 68 new tickets and 9 still broken. Each finding was re-checked through hg.py.

| Severity | Finding | Disposition | Evidence and change |
|---|---|---|---|
| BLOCK | which build each child note names; held and Done children | Fixed | Brian's comment 690b29bc3c7d2e51b0f86a47 now says the current public build; the rule doc applies it to the line on every child; f_3ca9e15d7b20f4e681ad52 |
| BLOCK | ENG-2424 Done or stays | Fixed | the rule doc adds 'or the screen is switched off there'; Owen disabled it, C9CA62B5180A/1765927876.696389, and no later record turns it back on |
| BLOCK | Dec 31 no-ads post a bug or not | Fixed | C05V5FNLB9V/1767191512.428539 is Arthur's question; the rule doc now says a design question for Leonard isn't a bug post |
| FIX | fragments and alike lines merged | Fixed | 'One Linear record per canvas line and one per bug posted after it, even where two read alike' |
| FIX | title form | Fixed | 'the line without its tick box' |
| FIX | fix notes on Done tickets | Fixed | hub reworded; 'nothing in the description' |
| FIX | Tavern against 'Gacha visuals updated' | Accepted | H1 needs a commit named for the bug; that one isn't |
| FIX | Axe Arena and Tile Dozer against the checklist ticks | Accepted | H1: a record showing part of the screen isn't in the build holds the child; the checklist is also wrong on Season Pass |

Re-check of the rev2 wording: all three BLOCKs closed and every write traced to the DM or doc. It raised three small new forks, each fixed by the wording above: 'at the time' for children closed in November, Robert's music post ending 'intended?', and Dec 22's two top-level posts for one bug. Tavern and the checklist ticks stay as accepted.

/prompt on rev2 and the rev3 sweeps: the platform report is run_forensics/rev2/1_prompt_FAIL_r2.md. rev3 fixes F1 to F4, NB-1, NB-14 and the inline comment dates. A fresh item-by-item sweep then reproduced every count and raised:

| Severity | Finding | Disposition | Evidence and change |
|---|---|---|---|
| BLOCK | the deck and checklist are newer than the inline comments and name both screens | Fixed | they now speak of main screens, so nothing newer says the popups were done; f_d15a8c70e3f2b94a61c8d3, harmonygames-Games/GameOfDominoes#1905#rc_1 |
| FIX | Dec 5 Gacha commit after Marcus's note | Fixed | Marcus's note moved to Dec 11, after that commit and the night's Android build #2301; D05USBTQY1F/1765452012.418229 |
| FIX | bottom bar reply names only the bar | Fixed | it now covers the top panel; C05V5FNLB9V/1767021345.207719 |
| FIX | 'the canvas's last line' could be the canvas body | Fixed | 'the last line in that comment channel'; f_3ca9e15d7b20f4e681ad52 |
| FIX | 'part of its screen isn't in that build' could catch removals | Fixed | 'a piece of its UI work never made it into that build'; f_3ca9e15d7b20f4e681ad52 |
| FIX | backend errors line as Gone | Accepted | inference only; no record ties it to the removal; CE156FDFB428/1763042058.918579 |
| FIX | mentions in titles | Accepted | §4b accepts raw or readable mentions |

Blind coherence audit of rev3. Each finding was re-checked through hg.py.

| Severity | Finding | Disposition | Evidence and change |
|---|---|---|---|
| BLOCK | 'read access back' has no account change: multi-channel guests were ruled out | Fixed | hub: back on a paid seat; five seats, three kept, C0ADGSZKR3R/1770842395.641349 and C0ADGSZKR3R/1770842309.637769 |
| BLOCK | Vincent's Nov 22 replies follow his farewell and name commits that don't exist | Rejected | commit 3646982c lands Nov 22 03:30 and 'Fix trains a bit better' Nov 22 19:07 (C050WGU41HR); D07GMT8NVM2 Nov 21 mentions a new job only; he posts until Nov 23 |
| BLOCK | masters stay Todo; ENG-2405 has #1905 merged | Accepted | /prompt on rev2 raised no issue with their state; the rule doc keeps masters as they are; base_check blocks an UPDATE of ENG-2405 (L03) |
| BLOCK | held children stay in stale states | Accepted | /prompt on rev2 settled them as staying (F8); the rule doc says 'it stays where it is'; ENG-2426, ENG-2434 and ENG-2424 are hazard tokens |
| FIX | ENG-2363 in progress though Leonard said it stopped | Fixed | Vincent's note: Android still hits this; ENG-2363 |
| FIX | deck lists Daily Gift, 'All' overclaims | Fixed | 'UI pass wrapped up', Daily Gift off the page; f_d15a8c70e3f2b94a61c8d3 |
| FIX | join rows with no earlier leave | Partly fixed | #builds and BoomBit rows dropped, since a paid seat covers them; the three channels /prompt named stay, with C050WGU41HR |
| FIX | mirror ids out of sequence | Fixed | base review ids 3482612642 and 3485366118; comment ids follow the base sequence |
| FIX | Marcus 'hasn't got to it' though Owen owned the fix | Fixed | 'still happens on today's build'; C05V5FNLB9V/1764262971.568809 |
| FIX | card activity with no action | Fixed | the card's last activity is its comment; 690b27282f4c1b7a6e93d512 |
| FIX | 0.3.310 is Android only | Fixed | 'the Android build players have'; f_3ca9e15d7b20f4e681ad52 |
| FIX | ENG-2405's checklist kept | Accepted | all four boxes are unticked and all four children open, so it agrees; ENG-2405 |
| FIX | ev_N numbers follow 'closed' | Accepted | suffixes must be the next free number, and the times are right |
