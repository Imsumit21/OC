# Scenario Design — calvin_qm_epic · design only · contains no prompt, OE or criterion text

Storyline: the ZM main-menu Queue Manager (ZOM-543) went to main on 24 Sep 2025. Brian Foster asks Calvin to turn the one ticket into an epic before Thursday's flow review and to say where every report from Vincent's flow pass stands. Planned seed texts are in `plan/seed_text.json`, the 39 reports and their planned outcomes in `plan/reports.py` and `plan/truth_sketch.json`. This is design-3: the blind fork sweep and the blind coherence sweep both ran on earlier versions and every finding is dispositioned in section 13. Every number marked UNCALIBRATED is a design aid. The open choices were delegated by the requester on 2026-11-10 (`00_Pre_Scenario_Analysis.md` §11).

## 0 Assignment, persona census and horizon note

| Field | Value |
|---|---|
| Universe key | synthcut |
| Universe label | Oct 1, 2025 (synth-cut) |
| Clock line | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Seed bound | freeze_utc 2025-10-01T00:00:00Z |
| shutdown_rules_apply | false |
| Persona | Calvin Price, Game Engineer (Unity VFX), calvin.price@harmonygames.co, roster calvin_price |
| Function · competency · skill | Engineering · Engineering Ops · Analysis and synthesis |
| Evals category | Engineering & Live-Ops (`Evals/references/rules/task_categories.md`) |
| Task type · mode | long-horizon · hard, platform cap under 70 % |
| Requester targets | average strictly under 60 %; over 130 counted calls in every run; largest failure pattern under 50 %; all other difficulty guidelines |
| Loss budget | E[average] ≤ 52 % (requester line less 8 points; the playbook's Hard target is ≤ 62 %) |
| Effective profile | extreme (Long Horizon) |
| Volume exception | call_budget_floor 180, per_record_floor 40, requester-delegated; ≥ 500 needs padding. The per-record floor counts read surfaces only, so it is 40 and not the 120 quoted in the analysis, which counted writes |
| Theme screen | The game's own name and one feature name (Zombie Lane) carry a theme word that cannot be avoided in base records. Seeded text says ZM for the game and uses no infection or outbreak wording. Earlier ZM tasks ran on Opus 5.5 without a model fallback; the pre-check confirms it for this one |

Persona census, `persona_view.py reach calvin_price --top 10`, verbatim:

```
REACH  Calvin Price <calvin.price@harmonygames.co>  Game Engineer (Unity VFX) / Engineering
clock 2025-10-01

SLACK  user=EMPLOYEE_0006_SLACK_ID  visible channels=107 {'mpim': 28, 'public': 22, 'private': 31, 'im': 26}  messages=193104  public-not-member (UNVERIFIED)=45
  persona posts=12017 last post=2025-09-29  last activity in visible channels=2025-10-01
  C05433XK267    builds                                 public  mem=31  msgs=35617  2023-04-20..2025-10-01
  C05H8KVNU67    game-design                            private mem=27  msgs=22750  2023-07-16..2025-08-28 archived
  C050WGU41HR    engineering-bots                       private mem=35  msgs=19854  2023-03-29..2025-09-19
  C05V5FNLB9V    god-bugs                               private mem=31  msgs=16695  2023-10-07..2025-07-15
  C0880U9751A    zombie-match3d                         private mem=25  msgs=16250  2025-01-09..2025-09-30
  D05S1S2H55M    D05S1S2H55M                            im      mem=5   msgs=5755   2023-09-15..2025-09-29
  C0553V44CE4    god-ui-ux                              private mem=30  msgs=5008   2023-04-21..2025-05-29 archived
  C04S28HSD0U    product                                private mem=21  msgs=4365   2023-03-02..2024-05-11 archived
  C069FF9Q57S    analytics                              private mem=28  msgs=4276   2023-12-05..2025-09-19
  C05KNDCHAAG    company-internal                       private mem=38  msgs=4048   2023-07-31..2025-10-01

GMAIL  mailbox=calvin.price@harmonygames.co threads=8142 messages=9856 range=2023-03-29..2025-09-30
  threads by last-message month (recent): {'2025-04': 344, '2025-05': 37, '2025-06': 28, '2025-07': 36, '2025-08': 47, '2025-09': 49}
  top correspondents: SVC_0107_EMAIL (6510), SVC_0248_EMAIL (2132), SVC_2463_EMAIL (1989), SVC_5123_EMAIL (1393), SVC_0613_EMAIL (524), SVC_0251_EMAIL (321), leonard.hayes@harmonygames.co (257), arthur.blake@harmonygames.co (209), robert@harmonygames.co (204), SVC_4410_EMAIL (200)

GCAL  own=['calvin.price@harmonygames.co'] shared=[] events=442 (distinct ical_uid 125, cancelled 43)
  last event before clock=2025-09-29T16:30:00Z  next after clock=None
  by month: 2023-04:3 2023-05:3 2023-06:2 2023-07:5 2023-08:19 2023-09:11 2023-10:19 2023-11:19 2023-12:17 2024-01:27 2024-02:11 2024-03:5 2024-04:14 2024-05:16 2024-06:19 2024-07:22 2024-08:12 2024-09:29 2024-10:16 2024-11:16 2024-12:24 2025-01:28 2025-02:14 2025-03:7 2025-04:13 2025-05:19 2025-06:20 2025-07:19 2025-08:3 2025-09:10

DRIVE  owned=1918 {'application/json': 1881, 'application/vnd.google-apps.document': 13, 'folder': 10, 'application/pdf': 5, 'application/vnd.google-apps.spreadsheet': 3, 'application/vnd.google-apps.presentation': 3, 'text/plain': 3}
  shared-with=128 {'application/vnd.google-apps.document': 41, 'text/plain': 37, 'application/vnd.google-apps.spreadsheet': 24, 'application/json': 21, 'text/csv': 2, 'application/vnd.google-apps.presentation': 2, 'application/pdf': 1}
  shared by owner: {'Resource: -6481757892984311338': 100, 'leonard.hayes@harmonygames.co': 10, 'arthur.blake@harmonygames.co': 10, 'robert@harmonygames.co': 4, 'Resource: 7240535625619857401': 2, 'thomas@harmonygames.co': 1, 'julia.lawson@harmonygames.co': 1}
  native visible: {'gdocs': 54, 'gsheets': 27, 'gslides': 5}  last modified visible=2025-09-30T16:30:39Z
  UNVERIFIED (domain/anyone, not owned/shared)=102 {'application/vnd.google-apps.document': 37, 'application/vnd.google-apps.spreadsheet': 36, 'application/pdf': 11, 'application/json': 11, 'application/vnd.google-apps.presentation': 7}

UNSCOPED (always visible): contacts, github, trello, linear, snowflake, confluence

LAST ACTIVITY (days before clock): slack_persona_post=2025-09-29 (2d), slack_visible_channels=2025-10-01 (0d), gmail=2025-09-30 (1d), gcal_last_event_before_clock=2025-09-29 (2d), drive_last_modified_visible=2025-09-30 (1d)
```

Remit, from before-freeze sources: Calvin is the assignee of ZOM-543 (Queue Manager, In Progress). He wrote and merged harmonygames-Games/match3d#459, opened #465 and #472, and Brian asked him to take the queue manager on (D0770ET6WBW/1758125053.929449 on 17 Sep; D0770ET6WBW/1758730948.999939 on 24 Sep). QA reports to him directly (D06UPGF5PQV/1758806199.381319). Julia's note about his scattered tickets is D05HYDTG5TJ/1756838837.147599. Turning his own ticket into an epic and reconciling the reports against it is epic and task management on live engineering work. `role_reviews.scenario` is recorded in `00_V3_Authoring_Evidence.json`.

## 1 Storyline

Base facts, all read through `tools/hg.py` this stage: #459 merged 2025-09-24T23:06:25Z (queue for level-end animations, daily gift, season pass, tutorial); #465 merged 09-25T22:15:51Z (coin replay, queued tutorials); #473 merged 09-30T15:41:20Z by Oliver himself (Addressables/sp; its summary is about Season Pass popups loading and queuing and names no bug); #472 merged 09-30T15:53:04Z (Collect & Win into the queue); #475 merged 09-30T16:09Z (card pack animation). Vincent told Calvin 'Looks ok to me' and 'Boss arena as well' on 25 Sep (D06UPGF5PQV/1758820544.160399) after Calvin named Match 3D iOS Internal #1718 (D06UPGF5PQV/1758817744.353289); the #builds post C05433XK267/1758817549.151639 shows #1718 was built from Calvin's QueueManager branch. Leonard ticked the Queue Manager roadmap card on 30 Sep (Trello action 68dc07f69bc8f26035805883), which is the base's own 'done' that the report records qualify. Vincent keeps his general bugs on a Slack canvas (CF4EDAF93359/1759236624.010909) and Collect & Win has its own (C3DD99314033/1758897445.985019); Brian's note leaves both out.

Anchors and spine (every base id is YES for Calvin; planned ids are marked):

| Service | Record | Role |
|---|---|---|
| slack | D0770ET6WBW/1759264805.214409 (planned) | hub: Brian's DM (AN1) |
| linear | ZOM-543 | the Queue Manager ticket (AN2); Brian's note comment_faaa792418a942cd40be046d8d217a7d (planned) |
| gsheets | f_cb40955893624e1acb8500 (planned) | Vincent's flow pass sheet, 38 rows |
| slack | D06UPGF5PQV/1758820544.160399 | Vincent's ok on a branch build |
| slack | C05433XK267/1758817549.151639 | build log: #1718 from the QueueManager branch |
| slack | C05433XK267/1759263189.219529 | build log: Android Submission #135 from main |
| github | harmonygames-Games/match3d#465 | merged fix PR three rows rest on |
| github | harmonygames-Games/match3d#473 | Oliver's merged PR that two rows turn out to rest on |
| github | harmonygames-Games/match3d#472 | merged; Arthur's APPROVED review harmonygames-Games/match3d#472#rev_1 |
| github | harmonygames-Games/match3d#475 | merged; Arthur's APPROVED review harmonygames-Games/match3d#475#rev_1 |
| slack | D0770ET6WBW/1758808795.588519 | Brian parks the input blocker |
| slack | D05HYDTG5TJ/1756838837.147599 | Julia's note on Calvin's tickets |

KB placement: `universe_kb/by_universe/synthcut/timeline.json` rows 2025-09-02 (Daily Login/Gift live tuning), 2025-09-15 (Collect and Win match3d rebuild), 2025-09-17 (Season Pass live-tuning) and 2025-09-30 (vision bot PR #476). Cohorts from `cohorts.json`: LIN-OPEN-ZOM (open ZOM issues at the clock, 99, the pool reuse candidates come from), LIN-CQ12 (ZOM issues created in 2025-Q3, 236) and LIN-UPD (ENG/ZOM issues updated since 2025-08-13); none of them is the cohort itself, which is Vincent's sheet, so `cohorts.json: no fit — the population is a planned QA sheet plus two reports`. `trap_catalog.json` entries: C01 and C02 (thread replies that correct, a parent that states a resolution), N01 (ENG-n and ZOM-n twins), B04 (Jenkins in #builds), P04 (tokenised GitHub logins), K02 (app-name lineage).

Natural services (9): slack, linear, github, gmail, gcal, gdrive, gdocs, gsheets, trello. Injected (10): slack, linear, github, gmail, gcal, gdrive, gdocs, gsheets, gslides, trello. Confluence and Snowflake stay off the graded path (learnings §26; Snowflake cannot be injected).

Coupling seams: a build's branch in Slack changes a status read from a sheet (C1); an inline review changes whether a merged PR has a fix (T_INLINE); a reply under another thread and a post in another channel each reverse a pass (C2, T_BACK); the dev's comment on a PR the sheet never names closes two rows (C3); a note on a ticket changes which Linear record a row lands on (C4); a changed Trello card changes which rows go on the review list (C5).

## 1a Coherence audit

Scope: every record a correct run opens. Hazards from `coherence_hazards.json`; cards from `references/known_data_issues/synthcut.md`.

| Record | Category | Fields | Pointer | Hazard / card | Disposition |
|---|---|---|---|---|---|
| Linear issue done before its PR merged | temporal | completed_at | ZOM-543 and harmonygames-Games/match3d#459 | T04 | avoid: no seeded ticket is Done; the 18 seeded tickets are open and dated 30 Sep, after base ZOM-566 |
| Trello card with an action later than dateLastActivity | temporal | dateLastActivity | card 68daad83bacf52c6ea7e1593 | T06 | fold into design: the seeded card's dateLastActivity equals its update action's date, and both ids carry their own second, as base ids do |
| Seeded comments on closed tickets | temporal | created_at | ZOM-556 | SC-16 pattern, learnings §50 | avoid: every seeded comment sits on an open ticket (ZOM-543, ZOM-556, ZOM-560) |
| match3d PRs citing ENG keys | semantic | title | harmonygames-Games/match3d#472 | S01 | avoid: seeds cite ZOM keys only |
| Label vocabulary | semantic | labels | ZOM-543 | S03 | avoid: seeded tickets use only the Bug label, as ZOM-556 does |
| App name lineage | semantic | text | D05HYDTG5TJ/1756838837.147599 | K02 | fold into design: seeds say ZM; Daily Login and Daily Gift are one feature and the tie is Vincent's dated note on base ticket ZOM-556 |
| Slack cites keys not in Linear | cross-service referential | text | D0770ET6WBW/1758808795.588519 | R01 | avoid: every key a seed cites is a planned ticket or a base ticket proved by lookup (`plan/out/id_collisions.txt`) |
| GitHub comments without a Slack mirror | cross-service referential | mirror | harmonygames-Games/match3d#472 | R06, R07 | fold into design: each seeded inline comment gets its copy under the PR's opened message in C093LEZGF6J |
| Google-native links in Slack | cross-service referential | url | D0770ET6WBW/1758653851.429209 | R04 | avoid: Brian's base link to a tutorial sheet is not used; the pass sheet is named, not linked |
| Calendar invitation mails without an event | cross-service referential | ical_uid | calvin.price@harmonygames.co/<calendar-f2b39cd5-884e-2def-a4d7-d41d80d4c55b@google.com> | R08 | fold into design: both invitation mails share the seeded event's ical_uid, one event row per attendee calendar, each with its own id |
| Thread reply counters | quantitative | reply_count | C08R27X0EAH/1759249488.495439 | Q01, Q02, Q03 | fold into design: the seeded reply updates the parent's reply_count, reply_users_count and latest_reply |
| Calendar copies that disagree | quantitative | updated | evt_342a813cb7765d4a6fce8d | Q11 | fold into design: all attendee copies carry the same fields |
| Tickets still open after work shipped | state/lifecycle | state | ZOM-564 | L03, SC-16 | excluded: ZOM-564, ZOM-513, ZOM-514 and ZOM-563 are neither cited nor modified; Brian's note leaves Oliver's tutorial work out |
| Parent with open children | state/lifecycle | state | ZOM-521 | L06, SC-15, SC-30 | excluded: ZOM-521, ZOM-526 and ZOM-528 are neither cited nor modified; the new epic's children are created by the run |
| In Review tickets with a completion date | state/lifecycle | completed_at | ART-760 | L05, SC-32 | excluded: no In Review ticket is in scope |
| Merged PRs with no human approval | state/lifecycle | reviews | harmonygames-Games/match3d#465 | L09, L10 | fold into design: #465 has only CodeRabbit reviews, which is base truth; the seeded inline comments sit on #472 and #475, which Arthur approved |
| Message ids and mailbox aliases | identifier/format | id | calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com>; base thread files use calvin@harmonygames.co | I02, I03 | fold into design: seeded Gmail ids carry their send time (id >> 20 = milliseconds), as base ids do; subjects end '(CST) (calvin.price@harmonygames.co)' |
| GitHub logins are tokens | identifier/format | author_login | harmonygames-Games/match3d#472#rev_1 | I08, P04, SC-50 | fold into design: Arthur's seeded comments use EMPLOYEE_0025_GITHUB_USERNAME, the login on his real review |
| Calvin has two GitHub logins | identifier/format | author_login | harmonygames-Games/match3d#459 | S04 | avoid: nothing is graded on a login; PERSON_0003_GITHUB_USERNAME authored all three PRs |
| Mail from Brian Foster's address | other | from_email | card SC-6; Brian's base chat D0770ET6WBW/1758808795.588519 is where he writes | SC-6 | excluded: Brian acts only in Slack and Linear; Leonard sends the invitations |
| Trello list named BETA: Oct 10 | other | list name | 68c453cd0ff184d95550bc58 | SC-13, SC-14 | excluded: Leonard's review card sits in the board's Backlog list (68c451221ebabaf255a7d16b), not the BETA list; nothing rests on a beta date or on a card's complete flag, and the Queue Manager card is cited only as a distractor |
| Build post naming a different build | other | attachment text | C05433XK267/1758817549.151639 | SC-56, SC-67 | avoid: build #1621 and commit titles are never used; only a build's branch, which its own post states, is read |
| Telemetry versions against builds | other | app version | card SC-19; builds are read from C05433XK267/1758838873.487119 instead | SC-19, SC-44 | excluded: no Snowflake record is on the path |
| Season Pass, Collect & Win and Boss Arena ship facts | other | dates | cards SC-38, SC-57, SC-58, SC-68; harmonygames-Games/match3d#472 is the only Collect & Win record used, and base canvas C3DD99314033/1758897445.985019 is left out by Brian's note | SC-38, SC-57, SC-58, SC-68 | excluded: areas are graded only on report statuses; no ship date, prod state or #zm-collect-win post is used |

Sibling-defect sweep: the designed defect is 'a done source that another record contradicts'. Its siblings in scope were listed: every sheet row with an ok or nr re-test (13 builds checked against #builds, `plan/reports.py` MAIN_BUILDS and BRANCH_BUILDS) and every row that names a fix PR (#465, #472, #475, plus #473). Rows 2, 3 and 17 are the controls where the ok is on a main build after the merge; the blind coherence sweep (section 13) re-read them against the base.

## 1b Active speakers

Status from `universe_kb/by_universe/synthcut/activity.json`:

| Person | Email | status_at_clock | Seeding role |
|---|---|---|---|
| Brian Foster | brian.foster@harmonygames.co | active_sep_2025_quiet_in_oct | hub DM and earlier chat line (both inside his usual 10:00 to 21:11 UTC hours), note on ZOM-543; no mail (SC-6) |
| Vincent Parker | vincent.parker@harmonygames.co | active_sep_2025_quiet_in_oct | flow pass sheet, legend, 18 tickets filed on 30 Sep, two ticket notes, reply in #zombie-bugs |
| Arthur Blake | arthur.blake@harmonygames.co | active_sep_2025_quiet_in_oct | the rule doc and its DD decoy (he owns Docs such as 'Tech Stack'), two one-line inline review comments; nothing on Trello, where he has never acted |
| Leonard Hayes | leonard.hayes@harmonygames.co | active_sep_2025_quiet_in_oct | review card on the board he runs, the two invitations, the calendar event |
| Oliver Brooks | oliver.brooks@harmonygames.co | active_sep_2025_quiet_in_oct | one comment on his own PR #473 |
| Marcus Bennett | marcus.bennett@harmonygames.co | active_sep_2025_quiet_in_oct | one line in his chat with Calvin |
| Robert | robert@harmonygames.co | active_sep_2025_quiet_in_oct | one post in #zombie-match3d, where he reports builds he plays; no mail |
| Julia Lawson | julia.lawson@harmonygames.co | active_sep_2025_quiet_in_oct | not seeded; base note only; invited to the review |
| Owen Baker | owen.baker@harmonygames.co | active_sep_2025_quiet_in_oct | not seeded |
| Calvin Price | calvin.price@harmonygames.co | active_sep_2025_quiet_in_oct | the persona; owner of the seeded folder and deck |

## 1c Identity traps

`entity.py collisions`, verbatim:

```

SHARED_FIRST_NAMES (4)
  claire: ['Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]', 'Claire <github:PERSON_2360_GITHUB_USERNAME>']
  marcus: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Marcus Lee <marcus.lee@harmonygames.co>', 'Marcus <trello:c48a210d5c5a4b59231c6873>']
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

LOOKALIKE_EMAIL_LOCAL_PARTS (1)
  - 'thomas@' vs 'thomas.baker@': ['Thomas <thomas@harmonygames.co> [persona thomas]'] / ['Thomas Baker <thomas.baker@harmonygames.co>']

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

UNRESOLVED (11)
  [ambiguous_name] github: mononym 'Claire' is an exact name of [] and the first name of ['email:claire.morgan@harmonygames.co'] -> candidates ['email:claire.morgan@harmonygames.co']
  [ambiguous_name] trello: mononym 'Marcus' is an exact name of [] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co'] -> candidates ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']
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

`entity.py resolve "Calvin Price"`, verbatim:

```
ENTITY email:calvin.price@harmonygames.co  name=Calvin Price  kind=person  emails=['calvin.price@harmonygames.co']
  persona: calvin_price - Game Engineer (Unity VFX) / Engineering
  slack      id=EMPLOYEE_0006_SLACK_ID, name=Calvin Price, real_name=Calvin Price, email=calvin.price@harmonygames.co, is_bot=False, deleted=False, messages=12017, first_post=2023-03-29, last_post=2025-09-29   [join: exact_email]
  gmail      mailbox=calvin.price@harmonygames.co, threads=8142, messages=9856, first=2023-03-29, last=2025-09-30, thread_filename_alias=['calvin@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=calvin.price@harmonygames.co, owner_email=calvin.price@harmonygames.co, summary=Calvin Price — primary, events=442, last_event_before_clock=2025-09-29   [join: exact_email]
  gdrive     id=user_49b9dfa5208d, email=calvin.price@harmonygames.co, display_name=calvin.price@harmonygames.co, root_folders=['d_49b9dfa5208d400d9b3937'], owned_items=1918, last_modified=2025-02-14, files_shared_with=128   [join: exact_email]
  linear     id=usr_49b9dfa5208d400d, email=calvin.price@harmonygames.co, name=calvin.price@harmonygames.co, is_active=True, last_activity=2025-09-25   [join: exact_email]
  github     login=PERSON_0003_GITHUB_USERNAME, name=Calvin Price, email=calvin.price@harmonygames.co, type=User, last_activity=2025-09-30   [join: exact_email]
  github     login=PERSON_2137_GITHUB_USERNAME, name=Calvin Price, type=User, last_activity=2025-09-30   [join: exact_name]
  trello     id=ca5bb4c09fbf2a437f04531e, username=calvin.price, fullName=Calvin Price   [join: exact_name]
  confluence id=user_STAFF_19, account_id=acct_STAFF_19, email=calvin.price@harmonygames.co, display_name=Calvin Price, is_active=True   [join: exact_email]
  contacts   contact_id=49b9dfa5208d400d9b3937ca, name=Calvin Price, email=calvin.price@harmonygames.co, job=Game Engineer (Unity/VFX), is_user=False   [join: exact_email]
  last activity: {'slack': '2025-09-29', 'gmail': '2025-09-30', 'gcal': '2025-09-29', 'gdrive': '2025-02-14', 'linear': '2025-09-25', 'github': '2025-09-30'}
```

Pinned: Calvin Price is calvin.price@harmonygames.co, not Nathan Price. His PRs use PERSON_0003_GITHUB_USERNAME; PERSON_2137_GITHUB_USERNAME joins by name only and is not used. Marcus is Marcus Bennett, not Marcus Lee. Brian is Brian Foster (Slack EMPLOYEE_0026_SLACK_ID, Linear usr_fc22d5941b2aeb5c). Arthur Blake's GitHub login is EMPLOYEE_0025_GITHUB_USERNAME. Oliver Brooks is EMPLOYEE_0003_SLACK_ID (GitHub EMPLOYEE_0003_GITHUB_USERNAME, author of #473). Owen Baker is EMPLOYEE_0021_SLACK_ID. No second account is created for anyone.

## 2 Cohort spine

Rule: 38 rows of Vincent's flow pass sheet, 1 report raised outside it and the 10 areas of Brian's note: 49 records. Source: the hub and Brian's note. Size 49; the design stays inside 40–150.

| Surface | Tool | Records | Calls each | Requirement | Decides | Why no bulk | Short circuit |
|---|---|---|---|---|---|---|---|
| linear | linear_list_comments | 22 | 1.0 | R4 | Ticket for each report | linear_list_issues returns no comments; the note that ties a row to a ticket needs that ticket's own linear_list_comments | a row with a blank Ticket cell is only settled by reading candidate tickets; titles use other words, so one search cannot sweep the ties |
| github | github_get_pull_request, github_get_pull_request_reviews, github_get_pull_request_comments and github_get_issue_comments | 4 | 4.0 | R3 | Status of each report | github_search_pull_requests returns neither reviews, inline comments nor conversation comments, and in:comments misses inline ones | merged state alone does not say whether a fix is in a PR; only its own review and comment surfaces do, and each of the four PRs (#465, #472, #473, #475) needs them |
| slack | slack_conversations_history or slack_search_public_and_private on #builds | 12 | 1.0 | R3 | Status of each report | the sheet names builds by number only; the branch is in each build's own post, and 146 match3d posts in the last week of September cannot be read in one call | a re-test only counts on a build of the main branch, so each of the 12 distinct builds in the Re-test column and the chat needs its branch |
| gsheets | gsheets_values_get | 38 | 0.1 | R1 | population | one range read returns the rows; counted at a tenth because it is a bulk read | the list itself; nothing else holds the rows |

Predicate: three statuses, closed vocabulary, in Brian's note comment_faaa792418a942cd40be046d8d217a7d: Passed, Waiting on QA, Waiting on a fix. House rule that overrides the natural reading: an ok only counts on a build of the main branch (Arthur's rule f_6d0326fa006b136f1bbf82). Effective-date regime: Leonard's review card was changed on 30 Sep and changes which areas the review covers. Boundary records: one report outside the sheet (D05U73FNDDL/1759252212.611349), the parked input blocker (D0770ET6WBW/1758808795.588519) and Oliver's tutorial skip thread (C08R27X0EAH/1758903616.346579), both left out by the note.

Shortcut audit: `linear_list_issues` returns states but no comments, so a ticket's state never settles a row and the ties need per-ticket reads. `github_search_pull_requests` returns no reviews or inline comments. A Slack search for a build number does return its post, so that surface is one call per distinct build, 12 in all. The pass sheet is one range read and counts at a tenth. The writes have no batch form.

## 3 Hidden authorities

| Id | Name | Home | Record | Decoy | Governs | Findable by |
|---|---|---|---|---|---|---|
| H1 | Arthur's rule for QA passes | gdocs | f_6d0326fa006b136f1bbf82 | f_ea7517885d11570b54bf13 (game: Domino Delights) | R3 | QA passes |
| H2 | Leonard's review card | trello | 68daad83bacf52c6ea7e1593, 68dc11dceb76ad640995fd98 | D0770ET6WBW/1759164072.337219, calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com> (older versions in T_GATE) | R5 | flow review |

Both are named by role in Brian's note and by nothing else; neither location is given. H1's decoy is Arthur's note on Domino Delights hotfixes, true for another game. H2's decoys are the older versions: Brian's chat line and the first invitation. Findability proof runs at injection, because both are planned seeds.

## 4 Delegation lattice

| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |
|---|---|---|
| AN1 | Brian's message from yesterday | D0770ET6WBW/1759264805.214409 |
| AN2 | the Queue Manager ticket | ZOM-543 |

Hub: AN1 in Brian's voice delegates by role. It names no report, no build, no authority location and no channel. Brian's note on the ticket holds the definitions a run needs to give one answer; it names sources by role only (Vincent's flow pass sheet, Arthur's rule for QA passes, Leonard's review card, Julia's point).

Fragments and incorporation (quotes are exact substrings of the delegating record, planned in `plan/seed_text.json` or read from the base):

| Id | Service | Container | Kind | Via | Delegated by | Quote | Requirements |
|---|---|---|---|---|---|---|---|
| K1 | linear | ZOM-543 | delegation | AN1 | D0770ET6WBW/1759264805.214409 | I left a note on the ticket | R2, R3, R4, R6, R9 |
| K2 | gsheets | f_cb40955893624e1acb8500 | requirement | AN1 | D0770ET6WBW/1759264805.214409 | Vincent's flow pass | R1 |
| K3 | gdocs | f_6d0326fa006b136f1bbf82 | requirement | AN1>K1 | comment_faaa792418a942cd40be046d8d217a7d | Arthur's rule for QA passes | R3 |
| K4 | trello | 68daad83bacf52c6ea7e1593 | requirement | AN1>K1 | comment_faaa792418a942cd40be046d8d217a7d | the agenda of Thursday's review | R5 |
| K5 | gdrive | d_36cdb0374c4aad3b8bf741 | destination | AN1 | D0770ET6WBW/1759264805.214409 | your ZM queue manager folder | R7 |
| K6 | gdocs | f_d3a1aa5976285aac98ffda | format | AN1>K2 | f_cb40955893624e1acb8500 | my pass sheet legend | R3 |
| K7 | gcal | evt_342a813cb7765d4a6fce8d | recipient | AN1 | D0770ET6WBW/1759264805.214409 | everyone on the review invite | R7 |
| K8 | slack | D05U73FNDDL | requirement | AN1>K1 | comment_faaa792418a942cd40be046d8d217a7d | told you about in a DM | R1 |
| K9 | slack | D06UPGF5PQV | requirement | AN1>K2>K6 | f_d3a1aa5976285aac98ffda | I told the dev ok in our chat | R3 |
| K10 | github | harmonygames-Games/match3d#472 | requirement | AN1>K1 | comment_faaa792418a942cd40be046d8d217a7d | a fix for it is in main | R3 |
| K16 | github | harmonygames-Games/match3d#475 | requirement | AN1>K1 | comment_faaa792418a942cd40be046d8d217a7d | a fix for it is in main | R3 |
| K11 | github | harmonygames-Games/match3d#473 | requirement | AN1>K1 | comment_faaa792418a942cd40be046d8d217a7d | a fix for it is in main | R3 |
| K12 | linear | ZOM-556 | requirement | AN1>K1 | comment_faaa792418a942cd40be046d8d217a7d | if a ticket already has the report | R4 |
| K13 | slack | C08R27X0EAH | amendment | AN1>K1>K3 | f_6d0326fa006b136f1bbf82 | until somebody sees the bug again on a main build made after the one it passed on | R3 |
| K18 | slack | C08R27X0EAH | amendment | AN1>K1>K3 | f_6d0326fa006b136f1bbf82 | until somebody sees the bug again on a main build made after the one it passed on | R3 |
| K21 | linear | ZOM-585 | amendment | AN1>K1>K3 | f_6d0326fa006b136f1bbf82 | until somebody sees the bug again on a main build made after the one it passed on | R3 |
| K22 | linear | ZOM-586 | amendment | AN1>K1>K3 | f_6d0326fa006b136f1bbf82 | until somebody sees the bug again on a main build made after the one it passed on | R3 |
| K14 | slack | D05HYDTG5TJ | format | AN1>K1 | comment_faaa792418a942cd40be046d8d217a7d | Julia's point about your tickets | R6 |
| K15 | linear | ZOM-560 | requirement | AN1>K1 | comment_faaa792418a942cd40be046d8d217a7d | if a ticket already has the report | R4 |
| K19 | gslides | f_637e63ae6c1b4a7eb016aa | destination | AN1 | D0770ET6WBW/1759264805.214409 | your queue manager deck | R9 |
| K20 | gmail | calvin.price@harmonygames.co/<calendar-f2b39cd5-884e-2def-a4d7-d41d80d4c55b@google.com> | recipient | AN1 | D0770ET6WBW/1759264805.214409 | the review invite | R7 |

Amendments: K13, Vincent's later reply, and K18, Robert's later post, each reverse one pass and leave the rest of the sheet standing. Distractors outside the chain are in section 5.

## 5 Chains and trap register

| Chain | Root cause | Hops | Ends in |
|---|---|---|---|
| C1 | A24 | gsheets f_cb40955893624e1acb8500 → slack D06UPGF5PQV/1758817744.353289 → slack D06UPGF5PQV/1758820544.160399 → slack C05433XK267/1758817549.151639 → gdocs f_6d0326fa006b136f1bbf82 | R3 |
| C2 | A11 | gsheets f_cb40955893624e1acb8500 → slack C05433XK267/1759263189.219529 → slack C08R27X0EAH/1759267212.418339 | R3 |
| C3 | A25 | gsheets f_cb40955893624e1acb8500 → github harmonygames-Games/match3d#473 → github harmonygames-Games/match3d#473#c_2 | R3 |
| C4 | A7 | gsheets f_cb40955893624e1acb8500 → linear ZOM-556 → linear comment_b3c560833d151268202546002e7613cf | R4 |
| C5 | A12 | slack D0770ET6WBW/1759164072.337219 → gmail calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com> → trello 68dc11dceb76ad640995fd98 | R5 |
| C6 | A17 | linear comment_faaa792418a942cd40be046d8d217a7d → slack D05U73FNDDL/1759252212.611349 → gsheets f_cb40955893624e1acb8500 | R1 |


| Trap | Family | Records | Requirement | Expected wrong reading | Resolver | Discovery order |
|---|---|---|---|---|---|---|
| T_BRANCH | done_gap | f_cb40955893624e1acb8500, f_6d0326fa006b136f1bbf82, D06UPGF5PQV/1758820544.160399, D06UPGF5PQV/1758817744.353289, C05433XK267/1758817549.151639 | R3 | rows 1, 2 and 25 are Passed: the sheet says ok and Vincent wrote looks ok, boss arena as well, in the chat | the build he looked at, Match 3D iOS Internal #1718, was cut from Calvin's QueueManager branch (the #builds post says so) and Arthur's rule counts only builds of the main branch; #465 is merged, so they wait on QA | the sheet row and the chat ok are both met before anyone looks the build number up in #builds |
| T_INLINE | done_gap | harmonygames-Games/match3d#472#rc_1, ZOM-571, ZOM-574, harmonygames-Games/match3d#472 | R3 | rows 12 and 15 wait on QA: the sheet gives #472 as their fix, #472 is merged and both tickets are In Validation | Arthur's inline review comment on #472 says the season pass icon restart and the event bar start are not in that diff; the review body is empty and the PR's own summary lists only the Collect & Win wait | the merged PR and the In Validation ticket come back first; the inline comment needs github_get_pull_request_comments |
| T_INLINE_PACK | done_gap | harmonygames-Games/match3d#475#rc_1, ZOM-581, harmonygames-Games/match3d#475 | R3 | row 32 waits on QA: the sheet gives #475 as its fix, #475 is merged and the ticket is In Validation | Arthur's inline review comment on #475 says the pack sound stop is nowhere in that PR; the review body is empty and the PR's summary does not mention sound | the merged PR and the In Validation ticket come back first; the inline comment needs its own call |
| T_REOPEN | superseding | f_cb40955893624e1acb8500, C08R27X0EAH/1759267212.418339, C05433XK267/1759263189.219529 | R3 | row 9 is Passed: nr on a main build | Vincent's later reply under his Sep 15 submission-issues thread in #zombie-bugs says it came back on Android Submission 135, a main build made after #1745, so under Arthur's note the pass no longer stands | the sheet is read first; the reply sits under a root two weeks older than the pass |
| T_BACK | superseding | f_cb40955893624e1acb8500, C08R27X0EAH/1759268652.552719, C05433XK267/1759263189.219529 | R3 | row 29 is Passed: ok on a main build | Robert's later reply under his Sep 10 endless thread in #zombie-bugs says the home intro played again every time on Android Submission 135, a main build made after #1750 | the sheet is read first; the reply sits under a root three weeks old and names no row |
| T_ELSE | completion_elsewhere | harmonygames-Games/match3d#473#c_2, ZOM-572, ZOM-573, ZOM-584, harmonygames-Games/match3d#473 | R3 | rows 13, 14, 37 and 38 wait on a fix: the sheet names no fix and their tickets are Todo | Oliver wrote on his own PR #473, merged on 30 Sep, that it also has those four fixes | the sheet's blank Fix cell and the Todo ticket are read first; #473 is named nowhere in the sheet |
| T_BODY | completion_elsewhere | ZOM-568, harmonygames-Games/match3d#472 | R3 | row 6 waits on a fix: the sheet names no fix and its ticket is Todo | the description of Calvin's own merged PR #472 says it also holds the pre-level panel until the level-end coins have landed; it merged on 30 Sep and QA has not tried a build with it | the sheet's blank Fix cell and the Todo ticket are read first; the description needs the PR itself, not the list |
| T_REOPEN_TICKET | superseding | f_cb40955893624e1acb8500, comment_5f530dc138f29bec3080eb175df98921, ZOM-585, C05433XK267/1759263189.219529 | R3 | row 17 is Passed: ok on a main build, and Vincent's own note on the ticket says ok | Samuel's later note on ZOM-585 says it came back on Android Submission 135, a main build made after #1757, so under Arthur's note the pass no longer stands | the sheet is read first; the note needs that ticket's own comments |
| T_BACK_TICKET | superseding | f_cb40955893624e1acb8500, comment_16aff20eceb0906dc0509214c2973635, ZOM-586, C05433XK267/1759263189.219529 | R3 | row 24 is Passed: nr on a main build, and Zombie Lane is Clear | Owen's later note on ZOM-586 says the lane bar starts from zero again on Android Submission 135, so the row is open and no area is Clear | the sheet is read first; the note needs that ticket's own comments |
| T_FILT | exact_predicate | D05U73FNDDL/1759252212.611349 | R1 | the reports are the 38 sheet rows | Brian's note brings in any bug somebody else saw in a build and told Calvin about in a DM since the 26th; Marcus told him about the pass icon glow on 30 Sep and no ticket holds it | - |
| T_ALIAS_GIFT | scope_alias | comment_b3c560833d151268202546002e7613cf, ZOM-556 | R4 | row 11 has no ticket, so it needs a new sub-issue | base ticket ZOM-556, the daily gift skip reset ticket, already has it; Vincent's note on that ticket ties his row to it | - |
| T_ALIAS_STREAK | scope_alias | comment_9f28b3d8d66bd04e3f7fc46bc6ed1ea9, ZOM-560 | R4 | row 20 has no ticket, so it needs a new sub-issue | base ticket ZOM-560, the abandoned pack freezer ticket, already has it; Vincent's note ties his row to it | - |
| T_GATE | effective_date | D0770ET6WBW/1759164072.337219, calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com>, 68dc11dceb76ad640995fd98, 68daad83bacf52c6ea7e1593, calvin.price@harmonygames.co/<calendar-f2b39cd5-884e-2def-a4d7-d41d80d4c55b@google.com> | R5 | Collect & Win and Daily Gift are the areas for the review, on Friday | Leonard's review card was changed on 30 Sep: Thursday, with Collect & Win and Level-end rewards; Daily Gift moves to next week | Brian's own line in the anchor chat is read first; the card is on Trello |
| T_PARK | superseding | D06UPGF5PQV/1758806199.381319, D0770ET6WBW/1758808795.588519 | R1 | the input blocker after every level is a report to carry | Brian parked it the same day in his own chat with Calvin, and his note leaves it out | - |
| T_SHARE | authority | evt_342a813cb7765d4a6fce8d, calvin.price@harmonygames.co/<calendar-f2b39cd5-884e-2def-a4d7-d41d80d4c55b@google.com> | R7 | the sheet is shared with Brian and Vincent, the two people in the conversation | the hub says everyone on the review invite: Leonard, Brian, Arthur, Julia and Vincent | - |
| T_FIELDS | authority | comment_faaa792418a942cd40be046d8d217a7d, D05HYDTG5TJ/1756838837.147599 | R6 | a new sub-issue takes the priority and assignee the report suggests | Brian's note, citing Julia's point about Calvin's tickets, wants no priority and no assignee on the new ones | - |
| T_STATE | stale_summary | ZOM-571, ZOM-572, ZOM-581, ZOM-574, ZOM-573, ZOM-584, ZOM-568, ZOM-585 | R4 | a ticket's own state is where the report stands | the state follows the status worked out from the records: ZOM-571, ZOM-574 and ZOM-581 go back to Todo, ZOM-585 goes back to Todo, and ZOM-568, ZOM-572, ZOM-573 and ZOM-584 go to In Validation | - |
| D_DDRULE | distractor (other_title) | f_ea7517885d11570b54bf13 | R3 | a pass on the dev's branch build is enough | that doc is about DD hotfixes | - |
| D_QMCARD | distractor (stale_summary) | 68c453cd0ff184d95550bc58 | R2 | Leonard ticked the Queue Manager roadmap card on 30 Sep, so the work is done | the card marks the feature as merged; report statuses come from the sheet and the records | - |
| D_SKIP | distractor (scope_adjacent) | C08R27X0EAH/1758903616.346579 | R1 | the tutorial skip exceptions are reports to carry | Brian's note leaves Oliver's skip work out, and a channel post is not something told to Calvin in a DM | - |
| D_ICONVFX | distractor (scope_adjacent) | D06UPGF5PQV/1758721951.996909 | R1 | Vincent's chat remark about the pass icon VFX is another report | for Vincent the sheet is the list | - |
| D_CANVAS | distractor (scope_adjacent) | CF4EDAF93359/1759236624.010909 | R1 | items on Vincent's Bug Checklist canvas are more reports | Brian's note leaves both canvases as they are | - |
| D_COINDM | distractor (already_done) | D0770ET6WBW/1758808900.412489 | R1 | Brian's own line about the coin animation is a second report | it is dated the 25th, before Vincent's pass, and it is row 5 already | - |
| D_432 | distractor (near_duplicate_record) | ZOM-432 | R4 | ZOM-432 is the daily gift ticket for row 11 | ZOM-432 is about the gift artwork frame; ZOM-556 carries Vincent's tie | - |
| D_OLDINVITE | distractor (withdrawn_ask) | calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com> | R5 | the first invitation's areas still stand | the card was changed on 30 Sep and the updated invitation says so | - |
| D_OLDBUILD | distractor (boundary_case) | C0880U9751A/1759185627.317849, C05433XK267/1759160363.685759, C05433XK267/1759162758.968639 | R3 | Robert saw the arena button bug after Vincent's nr, so row 27 is open again | he saw it on Android #2006, built 40 minutes before iOS Internal #1745, and Arthur's note reopens a pass only on a build made after the one it passed on | - |
| D_DDQUEUE | distractor (keyword_collision) | ENG-2069 | R1 | the DD queue manager tickets belong under the epic | they are Domino Delights tickets on another team | - |

Hardness v2 selection (`Hardness_Mastery.md` §13): trap 1, proving done across services (BRANCH, INLINE); trap 2, a correction somewhere else (REOPEN, BACK); trap 9, work someone already did (ELSE); trap 7, an item outside the obvious filter (FILT); trap 6, different names for one thing (ALIAS); trap 4, a moved date and scope (GATE). Each names its convincing wrong source and the record that beats it in the table above, and each flips a weight-5 slot. No correction sits in the anchor's thread, on the epic, or in the record that delegates to it.

### Mechanism portfolio (S5a)

Candidates, grounded in records. Priors are from `hardness_ledger.py priors --model claude-opus-5-5`.

| # | Anchor storyline (cited) | Coupling | Characteristic | Discovery-order proof | Reach | Findability term | Gradable fact | Services | Walk Δ vs tier | Risks |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Vincent's ok D06UPGF5PQV/1758820544.160399 | a build's branch changes a status | done gap | sheet row and chat ok come first | YES | 1718 | row waits on QA | gsheets, slack, gdocs | +12 build lookups | a stated rule is often applied; lottery; selected |
| 2 | harmonygames-Games/match3d#472 | inline review limits a merged PR | done gap | merged PR and In Validation ticket first | YES | not in this diff | row waits on a fix | github, gsheets | +16 reads | all-fail rows; selected |
| 3 | harmonygames-Games/match3d#475 | inline review limits a merged PR | done gap | merged PR and In Validation ticket first | YES | pack sound | row waits on a fix | github, linear | none | same habit as 2; one rule |
| 4 | thread C08R27X0EAH/1759249488.495439 | a reply reverses a pass | correction off path | sheet read first | YES | on top of the gift again | row waits on a fix | slack, gsheets | +1 | selected |
| 5 | channel C0880U9751A after build C05433XK267/1759263189.219529 | a post in another channel reverses a pass | correction off path | sheet read first | YES | home intro animation | row waits on a fix | slack, gsheets | +2 | a keyword search can return it; lottery; selected |
| 6 | harmonygames-Games/match3d#473 | the dev's comment on a PR the sheet never names closes two rows | completion elsewhere | blank Fix cell and Todo ticket read first | YES | For the flow list | rows wait on QA | github, linear | +4 | its Slack copy is searchable; lottery; selected |
| 7 | chat D05U73FNDDL/1759161394.516899 | scope sentence widens the list | outside the filter | sheet read first | YES | icon glow | report present | slack | +2 | the note names DMs, so a sweep can find it; selected |
| 8 | base tickets ZOM-556 and ZOM-560 | a note changes the ticket a row lands on | alias | blank Ticket cell read first | YES | daily gift, freezer | reuse the ticket | linear, gsheets | +6 | an area word finds the ticket; usually caught; selected |
| 9 | review card 68daad83bacf52c6ea7e1593 | a changed card changes which rows go on the review list | moved scope and date | Brian's chat line read first | planned | flow review | on the list or not | trello, gmail, slack | +5 | the note points at the card; usually caught; selected |
| 10 | Queue Manager roadmap card 68c453cd0ff184d95550bc58 | a ticked card against report records | stale summary | the tick is one read | YES | Queue Manager | areas still open | trello | +1 | base record on an SC-13 list; kept as a distractor, no rule |
| 11 | input blocker D06UPGF5PQV/1758806199.381319 | a later line parks a report | withdrawn ask | report read first | YES | input blocker | left out | slack | none | the note says it outright; kept as a control, no rule |
| 12 | Julia's note D05HYDTG5TJ/1756838837.147599 | a standing note sets new-ticket fields | follow-through | note on the epic read first | YES | priority | no priority set | linear, slack | none | cannot be graded without a 'leaves blank' row; kept as a trap, no rule |
| 13 | a mailed report to Calvin, as in design-1 | scope sentence widens the list | outside the filter | sheet read first | planned | mail | report present | gmail | +4 | rejected: nobody mails Calvin a bug in the base (coherence sweep), mail calvin.price@harmonygames.co/<calendar-f2b39cd5-884e-2def-a4d7-d41d80d4c55b@google.com> is the only human mail kept |
| 14 | code order in QueueManager.cs against Brian's list (harmonygames-Games/match3d#459) | code against tickets | source of truth | tickets first | YES | EnqueueEvent | in the queue or not | github | +2 | rejected: one file read settles it; base-git claims are unsafe (learnings §49) |

Selected rules:

| Rule | Record | Mechanism | Prior family | Why it applies | Nodes | Natural reading | Prior (record ids) | Controls | Over-application | After complete retrieval | Slots |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BRANCH | C05433XK267/1758817549.151639 | A24 | done_gap | same mechanism: a done source (sheet ok, chat ok) with the missing piece in another place (the build's branch in #builds) | T_BRANCH | the sheet's ok is a pass | Beta(3.0,3.0) hev_7f44d83eaad625e9, hev_522f1ca2bc9062de, hev_b8f28a892a74b855 | row 5, row 31, row 33 | branch_over: un-passes a row whose ok was on a main build | the build's branch must be looked up for a row the sheet calls ok | B1, B2, B3, B4, B5, V1, V2 |
| INLINE | harmonygames-Games/match3d#472 | A24 | done_gap | same mechanism: a merged PR is the done source and the missing piece sits in an inline review comment | T_INLINE, T_INLINE_PACK | a merged PR named in the sheet has the fix | Beta(3.0,3.0) hev_7f44d83eaad625e9, hev_522f1ca2bc9062de, hev_b8f28a892a74b855 | row 18 | inline_over: drops the PR from a row no reviewer excepted | retrieval-shaped: the inline comment needs its own call | I1, I2, I3, I4, I5, I6, I7, V2, V3 |
| REOPEN | C08R27X0EAH/1759249488.495439 | A11 | superseding | same mechanism: a dated correction in a thread reply under an older root, outside the window a reader pages | T_REOPEN, T_REOPEN_TICKET | nr on a main build is a pass | Beta(1.0,5.0) hev_e61e07235eadbd24, hev_1ceea0e7e912f48b, hev_ebc012c844829411 | row 7, row 27 | reopen_over: reopens another nr row | placement decides: a reply under another post | R1, R2, R3, R4, R5, R6, V1, V3, V4 |
| BACK | C05433XK267/1759263189.219529 | A11 | superseding | same mechanism, other author: a reply under a three-week-old root that names no row | T_BACK, T_BACK_TICKET | ok on a main build is a pass | Beta(1.0,5.0) hev_e61e07235eadbd24, hev_1ceea0e7e912f48b, hev_ebc012c844829411 | row 23, row 22 | back_over: reopens another ok row | placement decides: a post in a channel no record names | K1B, K2B, K3B, K4B, K5B, K9, V1, V3, V5 |
| ELSE | harmonygames-Games/match3d#473 | A25 | completion_elsewhere | same mechanism: an item that looks open while a record elsewhere shows the work done | T_ELSE, T_BODY | a blank Fix cell means no fix | Beta(1.0,4.0) hev_13d86dcf23442708, hev_638d1ef495e65d17, hev_58dcdb13d83f424d | row 19, row 30 | else_over: marks a row merged that no dev named | the blank cell must be doubted and unnamed PRs read | E1, E2, E3, E4, E5, E6, E7, E9, V2, V3 |
| FILT | D05U73FNDDL/1759161394.516899 | A17 | exact_predicate | same mechanism: an in-scope item outside the obvious list, brought in by the scope sentence | T_FILT | the sheet is the whole list | Beta(2.0,4.0) hev_9c403cae42eb4df8, hev_c2297d21ba5cbc7b, hev_0e15eed886c6fd32 | the 38 sheet rows | filt_over: adds a chat line that is not a bug seen in a build | placement decides: a 1:1 chat | F1, F2, F3, V3, V7 |
| ALIAS | ZOM-556 | A7 | scope_alias | same mechanism: a row and an existing ticket named differently, tied by a dated note | T_ALIAS_GIFT, T_ALIAS_STREAK | a blank Ticket cell means a new sub-issue | Beta(1.0,4.0) hev_ab2508cad060b0ac, hev_ace612d2f2268cdf, hev_9cefe52f59fd5be5 | row 1, row 38 | alias_over: reuses a ticket for a row with none | join needed | A1, A2, A3 |
| GATE | 68daad83bacf52c6ea7e1593 | A12 | authority | same mechanism: the governing source sits in a rarely opened service and an older version is met first | T_GATE | Brian's line in the chat names the review's areas | Beta(1.0,4.0) hev_d17e4abe74f0e7e0, hev_1de494f0682754d6, hev_4638d80f1d9f6311 | row 15, row 21 | gate_over: none | newer source must be preferred | G1, G2, V4 |

Four A5b checks per rule: **incorporated** (each chain runs from AN1 through Brian's note or a fragment, section 4); **tool-surface proof** (each deciding record is returned by the natural call for its service: `github_get_pull_request_comments`, `gmail_search_messages`, `slack_conversations_history`, `linear_list_comments`; confirmed in the pre-check); **graded weight** (slots above); **survives retrieval** (column above).

### Liveness flags (S5b)

`trap_liveness.py --design`, verbatim:

```
TRAP LIVENESS · ADVISORY · UNCALIBRATED · lexical warnings, not proof · DESIGN (no SQL: record text unavailable, only manifest-structure flags can fire) · on the Season Pass backtests these are development fixtures, not validation
  hub D0770ET6WBW/1759264805.214409 · direct delegations 6 · rule placement: SKIP for every node: the mechanism_portfolio declares no A15 node
  T_BRANCH done_gap           -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_INLINE done_gap           breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_INLINE_PACK done_gap           breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_REOPEN superseding        -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_BACK superseding        -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_ELSE completion_elsewhe breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_BODY completion_elsewhe breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_REOPEN_TICKET superseding        breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_BACK_TICKET superseding        breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_FILT exact_predicate    -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_ALIAS_GIFT scope_alias        breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_ALIAS_STREAK scope_alias        breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_GATE effective_date     -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_PARK superseding        -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_SHARE authority          breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_FIELDS authority          breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  T_STATE stale_summary      breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  D_DDRULE distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  D_QMCARD distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  D_SKIP distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  D_ICONVFX distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  D_CANVAS distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  D_COINDM distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  D_432 distractor         breadcrumb  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  D_OLDINVITE distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  D_OLDBUILD distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  D_DDQUEUE distractor         -  [rule placement SKIP: the mechanism_portfolio declares no A15 node]
  dispositions: 0/12 recorded
```

Dispositions: `T_INLINE`, `T_INLINE_PACK`, `T_ELSE` and `T_STATE` breadcrumb: keep. Each shares a planned ticket key (ZOM-571, ZOM-581, ZOM-572) with the sheet row it sits on, because the ticket is the done source; the record that beats it is a review comment or a PR comment that no fragment names. `T_ALIAS_GIFT`, `T_ALIAS_STREAK` and `D_432` breadcrumb: keep. Brian's note says a row may already have a ticket under another name, which is the fair findability link; a liveness flag is never fixed by removing a UGT link. `T_SHARE` and `T_FIELDS` breadcrumb: keep, they are controls on stated rules and carry no landing weight. Rule placement is skipped because no A15 node is declared. The tool reads no record text before the SQL exists; it re-runs at injection.

`hardness_v2_check.py --design`, verbatim:

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      6 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 3 requirements: {'R3': ['BRANCH', 'INLINE', 'REOPEN', 'BACK', 'ELSE'], 'R4': ['ALIAS'], 'R5': ['GATE']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   8 of 8 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     0 weight-5 total(s); 0 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  CLEAN      RULE_IN_PROMPT  no run of 8 resolver words in the prompt  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

Dispositions: no FLAG and no UNRESOLVED on design-3. An earlier build of it flagged T_GATE as SAME_PLACE, because the card as created and the card as changed share one Trello container; the middle version is now the first invitation mail (calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com>), so the three versions sit in Slack, Gmail and Trello. REOPEN and BACK are Slack-to-sheet, in other containers than anything the sheet or the anchor names.

## 6 Failure-diversity plan

Each channel is found by a different habit and written by a different person, so runs fail different subsets: BRANCH (looking a build number up in C05433XK267), INLINE (reading inline comments on harmonygames-Games/match3d#472 and #475, Arthur), REOPEN (opening Vincent's thread C08R27X0EAH/1759249488.495439), BACK (finding Robert's post in C0880U9751A), ELSE (reading the conversation on harmonygames-Games/match3d#473, Oliver), FILT (reading Marcus's chat), ALIAS (reading notes on ZOM-556 and ZOM-560), GATE (reading Leonard's card). Brian writes no correction, because runs sweep the rule owner's messages. No discovery gates most requirements: the largest channel, BRANCH, moves 21.1 % of the weight (`plan/policy_model_output.txt`). INLINE is the near-certain miss and sets the floor; BRANCH, REOPEN, BACK and ELSE are lotteries and give the spread; FILT, ALIAS and GATE are caught more often than not and mainly keep the answer unique.

## 7 Deliverables and dependent writes

| Write | Tool | Count | Depends on | Requirements |
|---|---|---|---|---|
| linear | linear_create_issue | 27 | T_FILT, T_ALIAS_GIFT, T_ALIAS_STREAK, T_ELSE, T_BRANCH, T_BACK | R2, R4, R6 |
| linear | linear_update_issue | 22 | T_INLINE, T_INLINE_PACK, T_ELSE, T_ALIAS_GIFT | R4 |
| linear | linear_create_comment | 22 | T_INLINE, T_ELSE, T_ALIAS_GIFT, T_ALIAS_STREAK | R4 |
| gsheets | gsheets_values_update | 3 | T_BRANCH, T_GATE, T_FILT | R7 |
| gdrive | gdrive_share_file | 5 | T_SHARE, K7 | R7 |
| gslides | gslides_batch_update | 2 | T_BRANCH, T_GATE, T_ELSE | R9 |
| slack | slack_send_message | 1 | T_BRANCH, T_GATE, T_ELSE | R8 |

One register (the stock-take sheet, tabs Reports and Areas) and its dependent writes: 10 area children, 17 new sub-issues, 22 tickets moved under a child with a matching state, 22 notes, five shares, one slide and the reply. Reuse-versus-create: rows 11 and 20 reuse base tickets ZOM-556 and ZOM-560. Three seeded tickets change state (ZOM-571 and ZOM-581 back to Todo, ZOM-572 to In Validation). The notes and the plain sub-issues are template-identical in shape, so a rubric can sample them. Full plan in `plan/truth_sketch.json`.

## 8 Service role map

| Service | Role | Load-bearing fact or write | Carrier |
|---|---|---|---|
| slack | hub, QA chat, build log, corrections | the ask, the branch each build came from, two later corrections and one report live here | ● |
| linear | epic, tickets, destination | Brian's note, the ticket ties and every structural write are here | ● |
| github | PR truth | merged PRs, Arthur's inline reviews and Oliver's comment decide whether a fix is merged | ● |
| gsheets | Vincent's flow pass sheet and the stock-take sheet | the report list is read here and the deliverable is written here | ● |
| gdocs | Arthur's rule and the sheet legend | which builds count for a pass, and what ok, nr and ok, chat mean | ● |
| gdrive | destination folder and sharing | the sheet goes in Calvin's folder and is shared | ● |
| gmail | review invitations | the invitation names the review, points at Leonard's card and carries the older list of areas the card replaced | ● |
| gcal | review event | the attendee list the sheet is shared with | ● |
| trello | Leonard's review card | the areas the review covers, which decide the review list | ● |
| gslides | Calvin's queue manager deck | the slide with the five numbers is written here | ● |
| contacts | not used | no load-bearing fact | ○ |
| confluence | base only, off the graded path | no load-bearing fact | ○ |
| snowflake | off the graded path | SC-19 and SC-44 joins are unsafe | ○ |

## 9 Call budget

| Phase | Service | Calls | Reason |
|---|---|---|---|
| discovery | slack | 5 | Brian's DM, the QA chat, channel lookups |
| discovery | linear | 6 | the epic, its comments, states, labels, team, users |
| discovery | gdrive | 3 | the folder, the pass sheet's and the deck's location |
| discovery | gsheets | 3 | the pass sheet: metadata and two range reads |
| discovery | gdocs | 4 | the legend and Arthur's rule: search and read |
| rules | trello | 3 | Leonard's review card: search, card, its actions |
| rules | gmail | 3 | the review invitation: search and the two messages |
| rules | gcal | 2 | the review event and its attendees |
| rules | slack | 2 | Julia's note |
| discovery | gslides | 2 | Calvin's deck: find and read |
| enumeration | slack | 15 | what was told to Calvin in a DM since the 26th: each recent 1:1 chat; later words on passed rows in #zombie-bugs threads and #zombie-match3d |
| enumeration | gmail | 3 | mail to Calvin since the 26th |
| enumeration | linear | 6 | ZOM tickets since the 20th and candidate tickets for rows with no key |
| enumeration | github | 4 | match3d PRs merged since the 24th |
| per-record | linear | 22 | comments on the 22 tickets that hold a report |
| per-record | github | 16 | body, reviews, inline and conversation comments of the four PRs the rows rest on |
| per-record | slack | 12 | the #builds post of each distinct build in the Re-test column and the chat |
| per-record | linear | 71 | 10 area children, 17 new sub-issues, 22 tickets moved under a child and 22 notes: each a distinct target with no batch form |
| writes | gsheets | 4 | stock-take sheet: create and fill two tabs |
| writes | gdrive | 6 | move into the folder and share with five people |
| writes | gslides | 2 | add the slide and its text |
| writes | linear | 1 | the epic's own state or text |
| writes | slack | 1 | reply to Brian |
| read-back | linear | 3 | confirm the tree |
| read-back | gsheets | 2 | confirm the sheet |

Total 201 unconditional calls over 10 services. The requester's floor is over 130 in every run: about 83 per-item writes happen whichever traps land, and reads on stored ticket tasks ran from 69 to 211, so the model's weakest of six runs clears 130 in every simulated batch (`plan/policy_model_output.txt`, UNCALIBRATED). The golden-run rule still applies: a correct run needs these calls. Nothing is added for count; each write is a distinct report, ticket, area or person that Brian's ask names.

## 10 QC rails

### Two-reading table

| Decision point | Best reading | Strongest alternative | Resolved by |
|---|---|---|---|
| Rows 1, 2 and 25 (ok, chat) | Waiting on QA | Passed | Arthur's rule f_6d0326fa006b136f1bbf82 and the build post C05433XK267/1758817549.151639: #1718 is a feature-branch build; #465 is merged |
| An nr re-test | counts as a pass on a main build | is not a pass | Brian's note comment_faaa792418a942cd40be046d8d217a7d: 'Vincent's ok or nr' |
| Row 9 after Vincent's later reply | Waiting on a fix | Passed, or Waiting on QA | the note: stays passed unless somebody says later, on a build made after that one, that it is back; 'also when it came back after a pass'; reply C08R27X0EAH/1759267212.418339 |
| Row 29 after Robert's later post | Waiting on a fix | Passed | the same sentence says 'somebody', not only whoever raised it; post C08R27X0EAH/1759268652.552719 names Android Submission 135, cut after build C05433XK267/1759197354.452939 |
| Row 12 with #472 merged | Waiting on a fix | Waiting on QA | the note: check the PR; Arthur's inline comment harmonygames-Games/match3d#472#rc_1 says it is not in that diff, and harmonygames-Games/match3d#472#c_1 lists two files, neither about icons |
| Row 32 with #475 merged | Waiting on a fix | Waiting on QA | Arthur's inline comment harmonygames-Games/match3d#475#rc_1; harmonygames-Games/match3d#475#c_1 says nothing about sound |
| Rows 13 and 38 with a blank Fix cell | Waiting on QA | Waiting on a fix | the note: a row with no PR in the sheet counts as merged if the dev wrote on a merged PR of theirs that it has the fix; Oliver's comment harmonygames-Games/match3d#473#c_2 on his own PR, merged 30 Sep 15:41 UTC |
| Rows 4 and 19, where a PR summary could be stretched to fit | Waiting on a fix | Waiting on QA | the note asks for the Fix column's PR or the dev's own word; neither exists for these rows, and harmonygames-Games/match3d#465 names neither |
| Row 17 re-tested the day #472 merged | Passed | Waiting on QA | iOS Internal #1754 is a main build cut after the merge: C05433XK267/1759248081.891639 |
| Rows 11 and 20 with no key in the sheet | note on ZOM-556 and ZOM-560 | new sub-issues | Vincent's notes comment_b3c560833d151268202546002e7613cf and comment_9f28b3d8d66bd04e3f7fc46bc6ed1ea9; the note's 'another name' sentence |
| Which areas the review covers | Collect & Win and Level-end rewards | Collect & Win and Daily Gift | the changed card 68dc11dceb76ad640995fd98 is later than calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com> and D0770ET6WBW/1759164072.337219 |
| Whether Waiting on QA goes on the review list | yes, anything not Passed | only Waiting on a fix | the note: 'a report that is not Passed' |
| Marcus's chat line | one more report | outside the list | the note: any bug somebody else saw in a build and told Calvin about in a DM since the 26th; D05U73FNDDL/1759252212.611349 |
| Items on Vincent's Bug Checklist canvas and the Collect & Win canvas | left out | more reports | the note leaves both canvases as they are; CF4EDAF93359/1759236624.010909 |
| Vincent's chat remarks not in his sheet | left out | extra reports | the note: for Vincent the sheet is the list; D06UPGF5PQV/1758721951.996909 |
| Brian's own coin line and the input blocker | left out | reports | the coin line D0770ET6WBW/1758808900.412489 is from the 25th and is row 5; the note parks the blocker, D0770ET6WBW/1758808795.588519 |
| Oliver's tutorial skip exceptions | left out | reports | the note; C08R27X0EAH/1758903616.346579 is a channel post about his own work |
| State of a ticket whose status differs | set to the mapped state | left as found | the note: 'If its state does not match the status'; ZOM-571, ZOM-572, ZOM-581 |
| Who the sheet is shared with | the five other people on the invite | Brian and Vincent only | the hub: everyone on the review invite; event evt_342a813cb7765d4a6fce8d |
| An area with every report Passed | Clear, child Done | Open | the note; Zombie Lane rows 22 to 24 in `plan/reports.py`, builds C05433XK267/1759160363.685759 |

### Reach table (load-bearing records)

Every scoped base record below is YES for Calvin (`persona_view.py can-see calvin_price …`); planned seeds are checked by `check-sql` at injection:

```
calvin_price slack D0770ET6WBW: YES   reason:   persona EMPLOYEE_0006_SLACK_ID is in members of im D0770ET6WBW 

calvin_price slack D06UPGF5PQV: YES   reason:   persona EMPLOYEE_0006_SLACK_ID is in members of im D06UPGF5PQV 

calvin_price slack D05S1S2H55M: YES   reason:   persona EMPLOYEE_0006_SLACK_ID is in members of im D05S1S2H55M 

calvin_price slack D05U73FNDDL: YES   reason:   persona EMPLOYEE_0006_SLACK_ID is in members of im D05U73FNDDL 

calvin_price slack D05HYDTG5TJ: YES   reason:   persona EMPLOYEE_0006_SLACK_ID is in members of im D05HYDTG5TJ 

calvin_price slack C05433XK267: YES   reason:   persona EMPLOYEE_0006_SLACK_ID is in members of public builds 

calvin_price slack C08R27X0EAH: YES   reason:   persona EMPLOYEE_0006_SLACK_ID is in members of private zombie-bugs 

calvin_price slack C093LEZGF6J: YES   reason:   persona EMPLOYEE_0006_SLACK_ID is in members of public zombie-prs 

calvin_price slack D06UPGF5PQV/1758820544.160399: YES   reason:   message inherits channel: persona EMPLOYEE_0006_SLACK_ID is in members of im D06UPGF5PQV 

calvin_price slack D06UPGF5PQV/1758817744.353289: YES   reason:   message inherits channel: persona EMPLOYEE_0006_SLACK_ID is in members of im D06UPGF5PQV 

calvin_price slack D06UPGF5PQV/1758806199.381319: YES   reason:   message inherits channel: persona EMPLOYEE_0006_SLACK_ID is in members of im D06UPGF5PQV 

calvin_price slack D0770ET6WBW/1758808795.588519: YES   reason:   message inherits channel: persona EMPLOYEE_0006_SLACK_ID is in members of im D0770ET6WBW 

calvin_price slack C05433XK267/1758817549.151639: YES   reason:   message inherits channel: persona EMPLOYEE_0006_SLACK_ID is in members of public builds 

calvin_price slack C05433XK267/1759263189.219529: YES   reason:   message inherits channel: persona EMPLOYEE_0006_SLACK_ID is in members of public builds 

calvin_price slack C05433XK267/1758838873.487119: YES   reason:   message inherits channel: persona EMPLOYEE_0006_SLACK_ID is in members of public builds 

calvin_price slack C05433XK267/1759162758.968639: YES   reason:   message inherits channel: persona EMPLOYEE_0006_SLACK_ID is in members of public builds 

calvin_price slack C08R27X0EAH/1759249488.495439: YES   reason:   message inherits channel: persona EMPLOYEE_0006_SLACK_ID is in members of private zombie-bugs 

calvin_price slack D05HYDTG5TJ/1756838837.147599: YES   reason:   message inherits channel: persona EMPLOYEE_0006_SLACK_ID is in members of im D05HYDTG5TJ 

calvin_price slack C08R27X0EAH/1758903616.346579: YES   reason:   message inherits channel: persona EMPLOYEE_0006_SLACK_ID is in members of private zombie-bugs 

calvin_price slack D06UPGF5PQV/1758721951.996909: YES   reason:   message inherits channel: persona EMPLOYEE_0006_SLACK_ID is in members of im D06UPGF5PQV 

calvin_price slack C0880U9751A: YES   reason:   persona EMPLOYEE_0006_SLACK_ID is in members of private zombie-match3d 

calvin_price slack D0770ET6WBW/1758658894.879649: YES   reason:   message inherits channel: persona EMPLOYEE_0006_SLACK_ID is in members of im D0770ET6WBW 

calvin_price slack D0770ET6WBW/1758730793.037609: YES   reason:   message inherits channel: persona EMPLOYEE_0006_SLACK_ID is in members of im D0770ET6WBW 

calvin_price slack D0770ET6WBW/1758808900.412489: YES   reason:   message inherits channel: persona EMPLOYEE_0006_SLACK_ID is in members of im D0770ET6WBW 

calvin_price slack D05U73FNDDL/1759161394.516899: YES   reason:   message inherits channel: persona EMPLOYEE_0006_SLACK_ID is in members of im D05U73FNDDL 

calvin_price slack C05433XK267/1759197354.452939: YES   reason:   message inherits channel: persona EMPLOYEE_0006_SLACK_ID is in members of public builds 

calvin_price slack C05433XK267/1759248081.891639: YES   reason:   message inherits channel: persona EMPLOYEE_0006_SLACK_ID is in members of public builds 

calvin_price slack C05433XK267/1759257787.502039: YES   reason:   message inherits channel: persona EMPLOYEE_0006_SLACK_ID is in members of public builds 

calvin_price slack C05433XK267/1759160363.685759: YES   reason:   message inherits channel: persona EMPLOYEE_0006_SLACK_ID is in members of public builds 

calvin_price slack C05433XK267/1758737279.948339: YES   reason:   message inherits channel: persona EMPLOYEE_0006_SLACK_ID is in members of public builds 

calvin_price slack C05433XK267/1758799630.301849: YES   reason:   message inherits channel: persona EMPLOYEE_0006_SLACK_ID is in members of public builds
```

Feasibility: `linear_create_issue` (team, parentId, state, title), `linear_update_issue`, `linear_create_comment`, `gsheets_create_spreadsheet`, `gsheets_values_update`, `gdrive_move_file`, `gdrive_share_file`, `gslides_batch_update` and `slack_conversations_add_message` are in `Evals/references/tools/catalog.json`. Calvin owns the folder d_36cdb0374c4aad3b8bf741, the deck f_637e63ae6c1b4a7eb016aa and the sheet he creates (learnings §31); Vincent's pass sheet is shared with him to read. Linear and GitHub are unscoped. Brian's note authorises moving and re-stating tickets that other people filed.

Precedence: load-bearing facts sit only in ● carriers, with Linear comments ● per `Ask_Carriers.md` §6b. The review's areas are on Leonard's Trello card (name and description) and, for the older version, in the first invitation mail; the calendar event carries the attendees. No fact lives on Confluence. Naturalness: the prompt names Brian's message, the ticket and the reply; it names no report, build, rule, person to check or count. Grading devices: exact counts in the reply, ≤ 5 samples per group plus a volume slot, one row per trap member, exclusions as a state or count on a required write, never 'leaves X alone'.

### Coherence rail

Every section 1a row is dispositioned. Every designed disagreement is a dated human claim with a later record that overturns it: the sheet's ok against the build post and Arthur's rule; the sheet's Fix cell against Arthur's inline comments; the nr and the ok against Vincent's and Robert's later words; the blank Fix cell against Oliver's comment; Brian's chat line against Leonard's changed card. Seeded ticket states are the ones Vincent set when he filed them on 30 Sep, from the same Fix cells the sheet shows, so no two system fields disagree silently. Claims about base artifacts stay observational and were read from the records: which branch a build came from (`plan/reports.py` MAIN_BUILDS and BRANCH_BUILDS, each a C05433XK267 post), which PRs are merged and when, and that no base PR text says the two planted inline comments are wrong. No seed names a commit title or build #1621 (SC-56, SC-67). Seeded ids follow the base encodings: Gmail ids carry their milliseconds, Trello ids their second, ZOM keys 567 to 584 are dated after base ZOM-566. `tools/base_claims.py` runs on the SQL at injection. Companions are planned in section 11.

## 11 Record plan for /create-injection

| Seed | Service | Id | Home record | Author | At | Purpose |
|---|---|---|---|---|---|---|
| hub | slack | D0770ET6WBW/1759264805.214409 | D0770ET6WBW/1759264805.214409 | Brian Foster | 2025-09-30T20:40:05Z | Before Thursday's flow review I want the queue manager to be a real epic. Right now it is  |
| epic_note | linear | comment_faaa792418a942cd40be046d8d217a7d | ZOM-543 | Brian Foster | 2025-09-30T20:25:37Z | How I want this epic.  Children: Tutorials, Level-end rewards, Daily Gift, Season Pass, Co |
| gate_old | slack | D0770ET6WBW/1759164072.337219 | D0770ET6WBW/1759164072.337219 | Brian Foster | 2025-09-29T16:41:12Z | For the flow review on Friday I want to go through collect&win and daily gift first, the r |
| sheet | gsheets | f_cb40955893624e1acb8500 | f_cb40955893624e1acb8500 | Vincent Parker | 2025-09-30T19:30:52Z | ZM home screen flow pass  Columns: #, Area, What happens, Found on, Ticket, Fix, Re-test.  |
| legend | gdocs | f_d3a1aa5976285aac98ffda | f_d3a1aa5976285aac98ffda | Vincent Parker | 2025-09-26T10:31:08Z | How to read my pass sheets  Found on: the build I first saw it on. Ticket: the Linear key  |
| rule_doc | gdocs | f_6d0326fa006b136f1bbf82 | f_6d0326fa006b136f1bbf82 | Arthur Blake | 2025-09-12T22:29:41Z | ZM builds and QA passes  Internal, Android and Submission are only the jobs. What matters  |
| dd_doc | gdocs | f_ea7517885d11570b54bf13 | f_ea7517885d11570b54bf13 | Arthur Blake | 2025-07-10T15:49:27Z | DD hotfix builds and QA passes  For DD hotfixes a pass on the dev's branch build is enough |
| rev_card_v1 | trello | 68daad83bacf52c6ea7ee56b | 68daad83bacf52c6ea7e1593 | Leonard Hayes | 2025-09-29T16:02:11Z | ZM home screen flow review - Fri Oct 3  Walk through what is still not passed in: Collect  |
| rev_card | trello | 68daad83bacf52c6ea7e1593 | 68daad83bacf52c6ea7e1593 | Leonard Hayes | 2025-09-30T17:22:36Z | ZM home screen flow review - Thu Oct 2  Walk through what is still not passed in: Collect  |
| rev_card_update | trello | 68dc11dceb76ad640995fd98 | 68daad83bacf52c6ea7e1593 | Leonard Hayes | 2025-09-30T17:22:36Z | updateCard: name and description changed to the Thu Oct 2 version |
| invite_v1 | gmail | calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com> | evt_342a813cb7765d4a6fce8d | Leonard Hayes | 2025-09-29T16:05:14Z | Subject: Invitation: ZM home screen flow review @ Fri Oct 3, 2025 12pm - 12:30pm (CST) (ca |
| invite_v2 | gmail | calvin.price@harmonygames.co/<calendar-f2b39cd5-884e-2def-a4d7-d41d80d4c55b@google.com> | evt_342a813cb7765d4a6fce8d | Leonard Hayes | 2025-09-30T17:24:09Z | Subject: Updated invitation with note: ZM home screen flow review @ Thu Oct 2, 2025 12pm - |
| event | gcal | evt_342a813cb7765d4a6fce8d | evt_342a813cb7765d4a6fce8d | Leonard Hayes | 2025-09-30T17:24:09Z | ZM home screen flow review, Thu Oct 2 2025 18:00 UTC. Attendees: Leonard Hayes, Brian Fost |
| inline | github | harmonygames-Games/match3d#472#rc_1 | harmonygames-Games/match3d#472 | Arthur Blake | 2025-09-30T15:53:40Z | Flow sheet has the season pass icon restart and the event bar starting under the gift popu |
| inline2 | github | harmonygames-Games/match3d#475#rc_1 | harmonygames-Games/match3d#475 | Arthur Blake | 2025-09-30T16:09:50Z | Don't see the pack sound stop anywhere in here. Still needs doing. |
| reopen | slack | C08R27X0EAH/1759267212.418339 | C08R27X0EAH/1759249488.495439 | Vincent Parker | 2025-09-30T21:20:12Z | from Android Submission 135 today: with a gift and a new pass stage both due after a level |
| back | slack | C08R27X0EAH/1759268652.552719 | C08R27X0EAH/1759268652.552719 | Robert | 2025-09-30T21:44:12Z | Played Android Submission 135 for an hour. No freeze this time, but coming back from endle |
| older | slack | C0880U9751A/1759185627.317849 | C0880U9751A/1759185627.317849 | Robert | 2025-09-29T22:40:27Z | Android 2006: I could tap the arena entry button while the reward animation was playing, a |
| else_pr | github | harmonygames-Games/match3d#473#c_2 | harmonygames-Games/match3d#473 | Oliver Brooks | 2025-09-30T15:42:10Z | For the flow list, this also has four fixes: the pass start popup coming back after every  |
| reopen2 | linear | comment_5f530dc138f29bec3080eb175df98921 | comment_5f530dc138f29bec3080eb175df98921 | Samuel | 2025-09-30T21:52:18Z | Got this again on Android Submission 135, so #472 did not sort it. The reward animation si |
| back2 | linear | comment_16aff20eceb0906dc0509214c2973635 | comment_16aff20eceb0906dc0509214c2973635 | Owen Baker | 2025-09-30T22:07:44Z | Android Submission 135: the lane bar starts from zero again every time I open home. Same a |
| body472 | github | harmonygames-Games/match3d#472 | harmonygames-Games/match3d#472 | Calvin Price | 2025-09-30T15:53:04Z | Implement Win&Collect into Queue Manager (this also holds the pre-level panel until the le |
| filt_dm | slack | D05U73FNDDL/1759252212.611349 | D05U73FNDDL/1759252212.611349 | Marcus Bennett | 2025-09-30T17:10:12Z | yo on today's main build the pass icon glow stays on after i claimed everything, saw it 3  |
| alias_gift | linear | comment_b3c560833d151268202546002e7613cf | ZOM-556 | Vincent Parker | 2025-09-30T18:05:21Z | Saw this one myself in my home screen pass on 1727, the day counter keeps going after a sk |
| alias_streak | linear | comment_9f28b3d8d66bd04e3f7fc46bc6ed1ea9 | ZOM-560 | Vincent Parker | 2025-09-30T18:08:48Z | Still there on Android 1984 in my home screen pass, the freezer from the abandoned pack ne |
| deck | gslides | f_637e63ae6c1b4a7eb016aa | f_637e63ae6c1b4a7eb016aa | Calvin Price | 2025-09-23T16:20:33Z | ZM queue manager  Slide 1: what the queue manager orders on the home screen. Slide 2: orde |
| folder | gdrive | d_36cdb0374c4aad3b8bf741 | d_36cdb0374c4aad3b8bf741 | Calvin Price | 2025-09-23T16:00:18Z | ZM queue manager |

Also planned, each with a stated purpose: the 38 sheet rows as Sheets cells; tickets ZOM-567 to ZOM-584, all filed by Vincent on 30 Sep between 16:40 and 19:20 UTC, after base ZOM-566 (16:26 UTC), for the 18 rows he sees as open (In Validation for the three whose Fix cell names a merged PR, Todo for the rest); one seeded note each on base tickets ZOM-556 and ZOM-560; Drive rows for f_cb40955893624e1acb8500, f_d3a1aa5976285aac98ffda, f_6d0326fa006b136f1bbf82, f_ea7517885d11570b54bf13, f_637e63ae6c1b4a7eb016aa, d_36cdb0374c4aad3b8bf741 with Calvin as owner of the folder and the deck; the Trello card 68daad83bacf52c6ea7e1593 in the Backlog list of ZM ROADMAP (board 6851a6569f3bf818760632ab) with its create and update actions by Leonard; one calendar event row per attendee for evt_342a813cb7765d4a6fce8d, each with its own id; the GitHub-app copies of both inline comments and of Oliver's comment in C093LEZGF6J under each PR's opened message (threads 1759185399.395419 and 1759247948.371729 for #472 and #475); the parent update for thread C08R27X0EAH/1759249488.495439. Estimated 125–150 INSERTs, most of them sheet cells and tickets. If honest evidence falls short of 120, that comes back to the requester rather than being padded.

### Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| github | INT-01, INT-02, INT-12, INT-23 | Slack app mirror; push notices; notification mails; CodeRabbit | INT-01 copies for both seeded inline comments and for Oliver's comment under each PR's opened message in C093LEZGF6J; review containers declared per learnings §53; no notification mail (no mention) and no bot comment seeded |
| linear | INT-03, INT-04, INT-05 | linear[bot] on PRs; Slack posts; digests | none needed for tickets no PR title names; declared at injection |
| gcal | INT-11 | invitation and update mails | seeded: the two invitation mails are the companions, in each attendee's mailbox that the base holds |
| gdrive | INT-13 | Drive app DMs on shares | none: Vincent's share of the pass sheet is declared no_notify |
| slack | INT-22 | Slack mail notices | none seeded; declared |
| trello | INT-21 | no Trello to Slack integration | none |
| gmail | INT-07, INT-08 | TestFlight and Firebase tester mails | none seeded: the only seeded mails are the two invitations |
| jenkins (slack) | INT-06 | #builds job posts | none seeded: base posts only |
| gsheets, gdocs, gslides | none | Drive rows mirror each file | seeded with matching owners and shares |

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
  [ok] ask_fragments: 21 fragments; need ≥ 12
  [ok] ask_fragment_services: 10 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 20 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 9 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 49; need ≥ 40 (source-defined: True)
  [ok] evidence_surfaces: 4 surfaces over 4 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 53; need ≥ 40
  [ok] call_budget: unconditional (verified) floor 201 of 201 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 180 (requester-confirmed volume_exception)
  [ok] call_budget_spread: 10 services in budget; largest share outside the per-record phase 29% (≤ 50%)
  [ok] traps: 27 traps across 9 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 7 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 6 supersessions (5 with versions in ≥ 2 services, 1 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: skipped (--design: no SQL yet)
  [ok] distractors: 10 distractors of 7 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 10 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 6 chains with 6 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] mechanism_portfolio: 8 portfolio entries, each a mechanism-enum id with trap/chain nodes, a requirement, a natural-reading fallback and a prior family with its reason
  [ok] artifact_fields: declared ['gradable_surface']: paths relative, digests sha256
  [ok] hidden_authorities: 2 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 1 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 16 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 9 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 7 writes over 5 services; each must depend on findings
  [note] volume_exception: call-budget floor 180 and per-record floor 40 replace 500 and 300; every other extreme target applies — reason: 49 cohort records and about 200 honest calls; reaching 500 would need padding, w; requester confirmation: requester, Claude Code chat 2026-11-10: 'i want over 130 tool calls in each runs
```

`gradable_surface.py validate`, verbatim:

```
GRADABLE SURFACE (01_Gradable_Surface.json): PASS · 63 slots · weight 223 · mechanism share 87.0% (reported, not gated) · weight by class {'write_content': 90, 'direct': 128, 'delivery': 5}
```

`gradable_surface.py gradeable-report`, verbatim:

```
SURFACE.GRADEABLE PASS · 63 slot(s) · {'GRADABLE': 63}
```

Id collisions (`plan/out/id_collisions.txt`), verbatim:

```
gdrive: 6 planned ids, base hits 0, positive control d_49b9dfa5208d400d9b3937 found, records checked 53631, scan_complete True
gcal: 1 planned ids, base hits 0, positive control none, records checked 10395, scan_complete True
trello_card: 1 planned ids, base hits 0, positive control 68c453cd0ff184d95550bc58 found, records checked 803, scan_complete True
trello_action: 2 planned ids, base hits 0, positive control 68dc07f69bc8f26035805883 found, records checked 5252, scan_complete True
github_rc: 2 planned ids, base hits 0, positive control harmonygames-Games/match3d#465#rc_1 found, records checked 1387, scan_complete True
github_pc: 1 planned ids, base hits 0, positive control harmonygames-Games/match3d#473#c_1 found, records checked 687, scan_complete True
linear_issue: 18 planned ids, base hits 0, positive control ZOM-566 found, records checked 3687, scan_complete True
slack ts: 1759264805.214409 0, 1759144812.337219 0, 1759267212.418339 0, 1759265412.552719 0, 1759252212.611349 0, 1758820544.160399 1 (the last one is the positive control, a real base ts); scan_complete True
gmail ids decode to: 2025-09-29T16:05:00Z, 2025-09-30T17:24:00Z
gmail thread files starting 184461494: 0 with the planned ids
```

Lazy-solver pass: a run that takes the sheet, the ticket states and Brian's chat line at face value scores about 16 % of the surface (`plan/policy_model_output.txt`); what it keeps is sampled lookups and delivery slots, and no trap slot leaks to it. Literal-value sweep: the counts 10, 9, 20, 0 and 7 appear in no seed; 'main branch' as the rule appears only in H1; 'Level-end rewards' as a review area appears only on the changed card. Wording sweep: no correction uses the words of the rule that decides it (Vincent says 'came up on top of the gift again'; Robert says 'played again every single time'; Oliver names no row number; Marcus says 'icon glow', not 'report'). 'The rest stands': the changed card moves the day and swaps one area and restates the other; no later record restates Daily Gift.

Requester targets, whole policies and six-run model, UNCALIBRATED:

```
UNCALIBRATED · surface: 51 slots, total weight 171, mechanism-flippable 144 (84.2%)
Share of weight each channel can flip: BRANCH 21.1%, REOPEN 12.3%, BACK 13.5%, INLINE 17.0%, FILT 12.3%, ALIAS 7.6%, ELSE 15.2%, GATE 8.8% · largest 21.1%

Whole policies
  100.0%  Perfect  [lands: -]
   15.8%  Takes every 'done' and 'ok' at face value, stays in the sheet, the QA chat and the epic  [lands: ALIAS, BACK, BRANCH, ELSE, FILT, GATE, INLINE, REOPEN]
   78.9%  Reads everything it is pointed at, never checks which build QA looked at  [lands: BRANCH]
   83.0%  Checks builds and PR bodies, never reads inline review comments  [lands: INLINE]
   80.1%  Thorough on the sheet's own records, never looks for later words on passed rows  [lands: BACK, REOPEN]
   56.7%  Never reads inline comments, PR conversation or later posts; otherwise perfect  [lands: BACK, ELSE, INLINE, REOPEN]
   71.3%  Takes Brian's chat line for the review, no reuse, no DM sweep  [lands: ALIAS, FILT, GATE]
   92.4%  Finds every record, files a new sub-issue per item (no reuse)  [lands: ALIAS]

Single misses
  BRANCH  78.9%
  REOPEN  87.7%
  BACK    86.5%
  INLINE  83.0%
  FILT    87.7%
  ALIAS   92.4%
  ELSE    84.8%
  GATE    91.2%

Pairs at or above the 60 % line: 28 of 28; triples at or above it: 42 of 56
Inline comments alone: 83.0% · inline + both later posts: 66.1%
P(one run catches every trap) ~ 0.0016 (independence); expected landings per run 4.10

One pre-check run: P(two or more causes, or one cause losing 30 % or more), independence
  scale 1.00: 0.98
  scale 0.70: 0.85
  scale 0.50: 0.65

Six-run Monte Carlo
  view                 scale  rho   E[avg]  P(<60)  P(SD)  med-SD  P(<5 full)  P(pat)  P(>130)   P(all)
  placement rates      1.00  0.20   52.0%    0.86   0.89   0.157       1.00    1.00      1.00    0.76
  placement rates      1.00  0.35   52.1%    0.82   0.93   0.185       1.00    0.99      1.00    0.76
  placement rates      1.00  0.60   52.6%    0.76   0.88   0.229       1.00    0.97      1.00    0.65
  placement rates      0.80  0.35   60.9%    0.46   0.94   0.196       1.00    0.99      1.00    0.43
  placement rates      0.70  0.35   65.3%    0.28   0.93   0.196       1.00    0.99      1.00    0.26
  placement rates      0.60  0.35   69.8%    0.14   0.93   0.192       1.00    0.98      1.00    0.13
  placement rates      0.50  0.35   74.4%    0.06   0.92   0.183       1.00    0.97      1.00    0.05
  bimodal carriers     1.00  0.35   51.4%    0.77   0.48   0.097       1.00    0.53      1.00    0.25
  bimodal carriers     0.70  0.35   62.4%    0.43   0.47   0.097       1.00    0.48      1.00    0.13
  ledger family means  1.00  0.35   69.8%    0.13   0.94   0.189       1.00    0.97      1.00    0.13
  ledger family means  0.70  0.35   78.3%    0.02   0.91   0.172       1.00    0.94      1.00    0.02

Rubric inflation: always-pass weight /rubric may add (placement rates, rho .35)
  + 20 weight                        1.00  0.35   57.1%    0.64   0.91   0.166       1.00    0.99      1.00    0.58
  + 20 weight                        0.70  0.35   68.9%    0.14   0.93   0.176       1.00    0.99      1.00    0.13
  + 40 weight                        1.00  0.35   61.2%    0.43   0.87   0.150       1.00    0.99      1.00    0.36
  + 40 weight                        0.70  0.35   71.9%    0.05   0.90   0.159       1.00    0.99      1.00    0.05
  + 70 weight                        1.00  0.35   66.0%    0.17   0.79   0.131       1.00    0.99      1.00    0.11
  + 70 weight                        0.70  0.35   75.4%    0.01   0.83   0.139       1.00    0.99      1.00    0.01
```

S9b prior forecast (advisory, UNCALIBRATED): ledger record hev_629545c85e58f03d, pre-registered on design-3 (hev_8f560b513a7e2c9d was design-1). E[avg] 0.696 (independent and source) to 0.715 (correlated), P(all four gates at the platform cap of 70 %) 0.238 to 0.332. These use ledger family means, which ignore placement and are lower than the placement rates in `plan/policy_model_output.txt`; both views are reported. Against the requester's 60 % line the ledger view says the target is unlikely, and the placement view gives 0.76.

### Self-review

Re-read `Evals/1_Prompt_Eval.md` §2.1, §2.2 and §3.2 and `Evals/0_Injection_Quality_Eval.md` Check C in order.

| Area | Counter-reading (strongest argument it fails) | Resolution (evidence) |
|---|---|---|
| temporal | the later words could be dated before the build they name | reply C08R27X0EAH/1759267212.418339 is 21:20 UTC and post C08R27X0EAH/1759268652.552719 21:44 UTC; Android Submission #135 posted 20:13 UTC, C05433XK267/1759263189.219529 |
| temporal | a re-test could predate the merge it relies on, or the sheet a build it cites | row 17's build C05433XK267/1759248081.891639 (16:01 UTC) is after #472 merged at 15:53; rows 31 and 33 use C05433XK267/1759257787.502039 (18:43) after #475 at 16:09; the sheet's last change is 19:30 UTC |
| temporal | the hub could fall outside Brian's hours or after the seed bound | hub D0770ET6WBW/1759264805.214409 is 2025-09-30T20:40:05Z; his September posts run 10:00 to 21:11 UTC; his last base line in that chat is D0770ET6WBW/1759173978.039839 |
| semantic | 'Passed' could be read as 'ticket Done' or 'card ticked' | note comment_faaa792418a942cd40be046d8d217a7d defines it by Vincent's ok or nr on a build that counts; ZOM-571 is In Validation while its row waits on a fix |
| semantic | a second QA list beside Vincent's canvas looks invented | Brian asked for this pass himself: D0770ET6WBW/1758658894.879649 ('check the panel openings and test the tutorials one by one') and D0770ET6WBW/1758730793.037609 (Vincent tests for him); the sheet's own note says general bugs stay on the canvas |
| cross-service referential | the sheet cites #472 for row 12 while the PR is about Collect & Win | that is the designed claim: the Fix column is what the dev told Vincent, and Arthur's review harmonygames-Games/match3d#472#rc_1 says it is not in the diff; harmonygames-Games/match3d#472#c_1 lists two files, neither about icons |
| cross-service referential | a seeded inline comment needs a PR that took a human review | harmonygames-Games/match3d#472#rev_1 and harmonygames-Games/match3d#475#rev_1 are Arthur's APPROVED reviews; the comments carry their timestamps and are one line each, as he writes |
| quantitative | the five counts could cancel between traps | each count sits beside named member slots (B1 to B3, R1, K1B, I1, I4, E1, E2, F1) in `01_Gradable_Surface.json`; ZOM-571 |
| quantitative | 10 + 9 + 20 must equal 39 and 7 must follow from the areas | `plan/reports.py` prints 10, 9, 20, 39 and review list 7 (Collect & Win 4, Level-end rewards 3); row keys in `plan/truth_sketch.json`; ZOM-576 |
| state/lifecycle | seeded tickets whose state the truth changes look like SC-16 defects | they are states Vincent set from what the devs told him, dated 30 Sep, and the run is asked to set them right; no base ticket in SC-16 is touched; ZOM-571, ZOM-572, ZOM-581 |
| state/lifecycle | a comment on a closed ticket fails base_check | every seeded comment sits on an open ticket: ZOM-543 In Progress, ZOM-556 and ZOM-560 Todo |
| identifier/format | a planned id could collide with a base id or break its encoding | `plan/out/id_collisions.txt`: 0 base hits, each scan with a positive control; ZOM-566 is the last base key; Gmail and Trello ids are computed from their timestamps in `plan/build_scenario.py` |
| other | the theme word could trigger a model fallback | base records carry it already; seeds add none beyond the feature name; D06UPGF5PQV/1758806296.703049 shows the base wording; the pre-check verifies the model |
| other | 70 Linear writes could be padding | each is a distinct report, ticket or area the note comment_faaa792418a942cd40be046d8d217a7d asks for; long_horizon.md; nothing repeats a call |
| decision: Rows 1, 2 and 25 (ok, chat) | the alternative 'Passed' could be a fair answer | Arthur's rule f_6d0326fa006b136f1bbf82 and the build post C05433XK267/1758817549.151639: #1718 is a feature-branch build; #465 is merged |
| decision: An nr re-test | the alternative 'is not a pass' could be a fair answer | Brian's note comment_faaa792418a942cd40be046d8d217a7d: 'Vincent's ok or nr' |
| decision: Row 9 after Vincent's later reply | the alternative 'Passed, or Waiting on QA' could be a fair answer | the note: stays passed unless somebody says later, on a build made after that one, that it is back; 'also when it came back after a pass'; reply C08R27X0EAH/1759267212.418339 |
| decision: Row 29 after Robert's later post | the alternative 'Passed' could be a fair answer | the same sentence says 'somebody', not only whoever raised it; post C08R27X0EAH/1759268652.552719 names Android Submission 135, cut after build C05433XK267/1759197354.452939 |
| decision: Row 12 with #472 merged | the alternative 'Waiting on QA' could be a fair answer | the note: check the PR; Arthur's inline comment harmonygames-Games/match3d#472#rc_1 says it is not in that diff, and harmonygames-Games/match3d#472#c_1 lists two files, neither about icons |
| decision: Row 32 with #475 merged | the alternative 'Waiting on QA' could be a fair answer | Arthur's inline comment harmonygames-Games/match3d#475#rc_1; harmonygames-Games/match3d#475#c_1 says nothing about sound |
| decision: Rows 13 and 38 with a blank Fix cell | the alternative 'Waiting on a fix' could be a fair answer | the note: a row with no PR in the sheet counts as merged if the dev wrote on a merged PR of theirs that it has the fix; Oliver's comment harmonygames-Games/match3d#473#c_2 on his own PR, merged 30 Sep 15:41 UTC |
| decision: Rows 4 and 19, where a PR summary could be stretched to fit | the alternative 'Waiting on QA' could be a fair answer | the note asks for the Fix column's PR or the dev's own word; neither exists for these rows, and harmonygames-Games/match3d#465 names neither |
| decision: Row 17 re-tested the day #472 merged | the alternative 'Waiting on QA' could be a fair answer | iOS Internal #1754 is a main build cut after the merge: C05433XK267/1759248081.891639 |
| decision: Rows 11 and 20 with no key in the sheet | the alternative 'new sub-issues' could be a fair answer | Vincent's notes comment_b3c560833d151268202546002e7613cf and comment_9f28b3d8d66bd04e3f7fc46bc6ed1ea9; the note's 'another name' sentence |
| decision: Which areas the review covers | the alternative 'Collect & Win and Daily Gift' could be a fair answer | the changed card 68dc11dceb76ad640995fd98 is later than calvin.price@harmonygames.co/<calendar-019530c0-b92a-84ed-a231-b228911277e8@google.com> and D0770ET6WBW/1759164072.337219 |
| decision: Whether Waiting on QA goes on the review list | the alternative 'only Waiting on a fix' could be a fair answer | the note: 'a report that is not Passed' |
| decision: Marcus's chat line | the alternative 'outside the list' could be a fair answer | the note: any bug somebody else saw in a build and told Calvin about in a DM since the 26th; D05U73FNDDL/1759252212.611349 |
| decision: Items on Vincent's Bug Checklist canvas and the Collect & Win canvas | the alternative 'more reports' could be a fair answer | the note leaves both canvases as they are; CF4EDAF93359/1759236624.010909 |
| decision: Vincent's chat remarks not in his sheet | the alternative 'extra reports' could be a fair answer | the note: for Vincent the sheet is the list; D06UPGF5PQV/1758721951.996909 |
| decision: Brian's own coin line and the input blocker | the alternative 'reports' could be a fair answer | the coin line D0770ET6WBW/1758808900.412489 is from the 25th and is row 5; the note parks the blocker, D0770ET6WBW/1758808795.588519 |
| decision: Oliver's tutorial skip exceptions | the alternative 'reports' could be a fair answer | the note; C08R27X0EAH/1758903616.346579 is a channel post about his own work |
| decision: State of a ticket whose status differs | the alternative 'left as found' could be a fair answer | the note: 'If its state does not match the status'; ZOM-571, ZOM-572, ZOM-581 |
| decision: Who the sheet is shared with | the alternative 'Brian and Vincent only' could be a fair answer | the hub: everyone on the review invite; event evt_342a813cb7765d4a6fce8d |
| decision: An area with every report Passed | the alternative 'Open' could be a fair answer | the note; Zombie Lane rows 22 to 24 in `plan/reports.py`, builds C05433XK267/1759160363.685759 |

Sources re-read through `tools/hg.py` this stage: every base pointer in sections 1, 5 and 10, the five PR records and all 15 build posts in `plan/reports.py`. `QueueManager.cs` in the match3d checkout was located with `hg.py search files` and read as a file, because the helper's `get` reads JSON only (`Evals/SEARCH.md`, blobs). `hardness_gate.py --design` output is pasted above: HARDNESS GATE (extreme (design)): PASS.

Unresolved: no independent model review of the design (RED TEAM FALLBACK in section 13); design-3 itself has not had a blind sweep, so a fork sweep and a coherence sweep run on it before the injection is sealed; the under-60 % average now rests on one near-certain carrier and four lotteries, and rubric growth is the main threat to it; whether the agent's Slack calls return the branch text in a #builds post's attachment is to be confirmed in the pre-check; about 20 items on Vincent's canvas have no text in the export and could not be compared with the rows; the platform duplicate score against earlier ZM tasks cannot be computed locally.

```
STAGE GATE scenario: PASS — Task_Authoring/task_inputs · 01_Scenario_Design.md#cd79a4e0e490 · 01_Hardness_Manifest.draft.json#b79d491b46aa · 01_Gradable_Surface.json#e2392bcc269e · 00_Assigments.md#a8cc00ce24ff · __context__#7be566a0936c · __assignment__#d644f7ef43f6 · __policy__#dc4ab5df3cdd · __gate_policy__#071e93f4073b · __review__#773c40d918b0 · blocking 0 · warnings 0 · checks 38
[PASS] assignment.v3_context: Calvin Price / Game Engineer (Unity VFX); hard cap <70%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 3 output(s) present: 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json
[PASS] structure.inputs: 1 input(s) present: 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md)
[PASS] structure.sections: 19 required sections present and non-empty (01_Scenario_Design.md)
[PASS] structure.placeholders: no placeholders in 01_Scenario_Design.md
[PASS] evidence.storyline: 12/12 items carry a source pointer (min 80%)
[PASS] evidence.coherence_audit: 43/43 items carry a source pointer (min 100%)
[PASS] evidence.hidden_authorities: 2/2 items carry a source pointer (min 100%)
[PASS] evidence.delegation: 23/23 items carry a source pointer (min 90%)
[PASS] evidence.trap_register: 55/55 items carry a source pointer (min 90%)
[PASS] evidence.record_plan: 33/36 items carry a source pointer (min 80%); unsourced e.g. L636: 'reopen2 | linear | comment_5f530dc138f29bec3080eb175df98921 | comment_5f530dc138f29bec3080'
[PASS] evidence.active_speakers: 10/10 items carry a source pointer (min 100%)
[PASS] tool.hardness_gate_design: hardness_gate --design pasted PASS; re-run PASS
[PASS] tool.persona_reach: persona_view reach pasted for calvin.price@harmonygames.co and matches the re-run (107 channels)
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] kb.coherence_hazards: coherence audit cites 22 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 10 speaker rows carry their activity.json status_at_clock
[PASS] kb.integrations: companions listed per integrations.json (14 INT ids, services ['gcal', 'gdocs', 'gdrive', 'github', 'gmail', 'gsheets', 'gslides', 'linear', 'slack', 'trello'])
[PASS] kb.storyline: timeline cited; cohorts ['LIN-CQ12', 'LIN-OPEN-ZOM', 'LIN-UPD']; trap_catalog ['B04', 'C01', 'C02', 'K02', 'N01', 'P04']
[PASS] boundary.anchor_naming: 4 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] tool.redteam_dual: red team did not run (missing 01b_Redteam_Review.md, 01b_Redteam_Review.second.md); explicit fallback recorded: two independent fresh Claude agents (general-purpose subagents, hg.py only, given the seed
[PASS] surface.valid: 63 slots, weight 261; geometry report-only, never gated: mechanism share 80%, always-pass share 20%
[PASS] forecast.preregistered: prior forecast pre-registered in the ledger: ['hev_629545c85e58f03d', 'hev_8f560b513a7e2c9d'] (UNCALIBRATED, advisory)
[PASS] revise.intake: revision intake consumes Working_Files/run_forensics/rev1/precheck.node_verdicts.json
[PASS] revise.verdict_dispositions: 8 proposed node verdict(s) dispositioned; 1 CONFOUNDED candidate(s) addressed
[PASS] revise.revision_binding: every export is bound on evidence to the revision it ran on, or marked historical (historical evidence never certifies a revision)
[PASS] evidence.register_run_step: 16/16 items carry a source pointer (min 100%)
[PASS] reach.scenario: 2 scoped load-bearing ids YES for calvin_price (2 planned seeds not yet in base: verified at the injection gate)
[PASS] review.counter_readings: 31 evidenced counter-readings (of 34 found; need ≥ 27) in 01_Scenario_Design.md
[PASS] review.coverage: self-review addresses all 8 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.draft.json is bound to the current assignment, policy, source context and freeze
[PASS] v3.role_review: current role-plausibility review recorded; semantic judgment belongs to the named reviewer
[PASS] readiness.context: explicit task/revision and current upstream evidence verified
[PASS] readiness.hardness_review: current evidenced review; deferred: [{'mechanism': 'BRANCH', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'BRANCH', 'evidence': 'natural retrieval', 'required_at': 'injection'}, {'mechanism': 'INLINE', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'INLINE', 'evidence': 'natural retrieval', 'required_at': 'injection'}, {'mechanism': 'REOPEN', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'REOPEN', 'evidence': 'natural retrieval', 'required_at': 'injection'}, {'mechanism': 'BACK', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'BACK', 'evidence': 'natural retrieval', 'required_at': 'injection'}, {'mechanism': 'ELSE', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'ELSE', 'evidence': 'natural retrieval', 'required_at': 'injection'}, {'mechanism': 'FILT', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'FILT', 'evidence': 'natural retrieval', 'required_at': 'injection'}, {'mechanism': 'ALIAS', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'ALIAS', 'evidence': 'natural retrieval', 'required_at': 'injection'}, {'mechanism': 'GATE', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'GATE', 'evidence': 'natural retrieval', 'required_at': 'injection'}]
[PASS] handoff.pasted: pasted into the Self-review by --paste
```


## 13 Red team (dual)

RED TEAM UNAVAILABLE: REDTEAM_* is unset (0 variables), so tools/redteam_review.py --dual cannot reach a reviewer.

RED TEAM FALLBACK: two independent fresh Claude agents (general-purpose subagents, hg.py only, given the seed texts and the report table but not this design's reasoning) ran blind sweeps on design-1: one applied every rule sentence to every report as the /prompt Unique Ground Truth reviewer, one tried to fail every seed against the whole base as the /injection and coherence reviewer. Chosen under the requester's delegation of 2026-11-10 because no second model family is reachable. Their reports are `plan/sweeps/fork_sweep.md` and `plan/sweeps/coherence_sweep.md`.

### Fork sweep dispositions (`plan/sweeps/fork_sweep.md`, run on design-1)

Row numbers below are design-3's.

The sweep recomputed the totals and agreed with them, then found five blocking forks and several moderate ones. All were fixed in the design (design-2); none was argued away.

| Finding | Source file | Disposition with evidence |
|---|---|---|
| Row 32: #475's body, its bot walkthrough and a commit title say the close button is locked, against the planned inline comment | plan/sweeps/fork_sweep.md | Fixed. Row 32 is now a different report (pack sound keeps playing), which harmonygames-Games/match3d#475 does not mention anywhere, and Arthur's planned comment says only that the sound stop is not in the PR |
| 'A merged PR covers it' has no test; rows 4 and 19 could fairly be Waiting on QA from PR text | plan/sweeps/fork_sweep.md | Fixed. Brian's note now says 'the fix is merged', that the Fix column is only what the dev said so the PR itself is checked, and that the dev naming the merged PR counts. Coverage is no longer inferred from PR prose: rows 13 and 38 rest on Oliver's own comment on harmonygames-Games/match3d#473, whose summary is about Season Pass popups and names no bug |
| Arthur's rule 'a build cut from main, Internal or Submission' reads three ways | plan/sweeps/fork_sweep.md | Fixed. The rule now reads 'a build of the main branch, whichever job built it, Internal, Android or Submission', and 'a build of a feature branch' for the other case; build C05433XK267/1758817549.151639 is a feature-branch build under any reading |
| Hub: 'how many hold the review' could count areas | plan/sweeps/fork_sweep.md | Fixed. The hub now says 'how many reports are passed … how many areas are clear and how many reports hold the review' |
| Base Collect & Win canvas holds more reports, including rows 15 and 16 | plan/sweeps/fork_sweep.md | Fixed. Rows 15 and 16 were replaced by rows that are not on the canvas, the two fixes no longer rest on harmonygames-Games/match3d#470, and Brian's note leaves the canvas out by name. The canvas item is C3DD99314033/1758897445.985019 |
| Row 12: the #472 walkthrough touches pass token timing | plan/sweeps/fork_sweep.md | Fixed. Row 12 is now the pass icon animation restarting; harmonygames-Games/match3d#472#c_1 lists two files, neither about icons, so the PR's own summary agrees with Arthur's comment |
| Row 18: 'only' in the inline comment could limit #472 to row 17 | plan/sweeps/fork_sweep.md | Fixed. The comment now says the PR 'only adds the Collect & Win wait', which is what rows 17 and 18 are about |
| Report 40 could belong to Level-end rewards, or to base tickets ZOM-541 or ZOM-528 | plan/sweeps/fork_sweep.md | Fixed. Marcus's report is now the pass icon glow (Season Pass, report 39), which no base ticket holds; ZOM-541 and ZOM-528 are untouched |
| Scope: ZOM-565, Marcus's #zm-animations thread and Brian's own DM line are borderline in-scope reports | plan/sweeps/fork_sweep.md | Fixed. Scope is now 'any bug somebody else on the team saw in a build and told you about in a DM since Vincent started his pass on the 26th', with 'if it is already a row, don't count it twice'. A census of every message to Calvin from 26 to 30 Sep found no other such report (D05U73FNDDL/1759161394.516899 is the last base line from Marcus; Brian's coin line D0770ET6WBW/1758808900.412489 is from the 25th) |
| 'If its state does not match' was untestable without the planned ticket states | plan/sweeps/fork_sweep.md | Fixed. The states are now in `plan/reports.py` (SEEDED_STATE, BASE_TICKETS) and `plan/truth_sketch.json`; three tickets change state: ZOM-571, ZOM-572, ZOM-581 |
| Sheet saved before a build it cites (#1757 at 18:43 UTC) | plan/sweeps/fork_sweep.md | Fixed. The sheet's last change is now 19:30 UTC; build C05433XK267/1759257787.502039 |
| Found-on builds later than Vincent's base chat reports | plan/sweeps/fork_sweep.md | Fixed. Rows 1 and 2 are found on iOS Internal #1698 (C05433XK267/1758737279.948339, 24 Sep 18:07 UTC, before his 21:36 UTC report); rows 5 and 25 on #1713 (C05433XK267/1758799630.301849, before his 25 Sep 13:17 UTC lines) |
| Keys ZOM-567 and up cannot carry dates before base ZOM-566 (30 Sep 16:26 UTC) | plan/sweeps/fork_sweep.md | Fixed. All 18 seeded tickets are filed on 30 Sep after 16:40 UTC, none is Done, and the two reuse tickets are now base tickets ZOM-556 and ZOM-560 |
| Not swept: the Brian–Vincent Turkish DM and Slack outside September | plan/sweeps/fork_sweep.md | Accepted as a limit. Calvin is not in D0770ET1HV2; I read its 30 Sep lines (D0770ET1HV2/1759251236.948149 onward): Vincent finds the merged card animation odd in two places, which no planned row contradicts, since his sheet is his whole list |

### Coherence sweep dispositions (`plan/sweeps/coherence_sweep.md`, run on design-1)

Nine blocking contradictions and a list of should-fix items. Five overlapped the fork sweep; the rest led to design-3.

| Finding | Source file | Disposition with evidence |
|---|---|---|
| Ticket keys out of order against base ZOM-566 | plan/sweeps/coherence_sweep.md | Fixed, as in the fork sweep: 18 tickets filed on 30 Sep after 16:40 UTC; reuse tickets are base ZOM-556 and ZOM-560 |
| Sheet cites build #1757 before it existed | plan/sweeps/coherence_sweep.md | Fixed: the sheet's last change is 19:30 UTC; C05433XK267/1759257787.502039 is 18:43 UTC |
| A Collect & Win go/no-go is contradicted the same afternoon (card ticked, 'none of them blockers', Submission #135 already holds #468) | plan/sweeps/coherence_sweep.md | Fixed by changing the premise. The meeting is now a plain home screen flow review that Leonard sets up; nothing is said to block a publish, and the column is 'Review list', not 'Holds review'. Build C05433XK267/1759263189.219529 and Vincent's 'none of them blockers' stand uncontradicted |
| Real QA lists exist as canvases; 'everything else is in chats' and 'his sheet is his whole list' are false | plan/sweeps/coherence_sweep.md | Fixed. The hub no longer says where everything else is. Brian's note says 'for Vincent that sheet is the list' for this job and names both canvases as left out (CF4EDAF93359/1759236624.010909, C3DD99314033/1758897445.985019); the sheet's own note says general bugs stay on his canvas. The pass itself has a base reason: Brian asked for it (D0770ET6WBW/1758658894.879649, D0770ET6WBW/1758730793.037609) |
| Rows 15 and 16 copy canvas items of 26 Sep | plan/sweeps/coherence_sweep.md | Fixed: both rows replaced; no row repeats a canvas item I could read (the old pair was C3DD99314033/1758897445.985019 and its neighbour) |
| Planned comment on #475 contradicts its walkthrough | plan/sweeps/coherence_sweep.md | Fixed: the comment is now about the pack sound, which harmonygames-Games/match3d#475#c_1 never mentions |
| Gmail ids carry their time; one decoded after the clock | plan/sweeps/coherence_sweep.md | Fixed: ids are computed from the send time in `plan/build_scenario.py` (id >> 20 = milliseconds), as base mail calvin.price@harmonygames.co/1842050583560498707 does |
| Arthur has never acted on Trello | plan/sweeps/coherence_sweep.md | Fixed: his rule is now a Google Doc. He owns Docs in the base, for example 'Tech Stack', changed 2025-09-19. Trello now carries only Leonard's review card, on the board Leonard runs (card create action 68c453cd0ff184d95550bc77 is his) |
| Linear has no comments in the base | plan/sweeps/coherence_sweep.md | Accepted with reason. Three seeded comments remain (Brian's note on ZOM-543, Vincent's two ties on ZOM-556 and ZOM-560). Earlier synth-cut tasks seeded Linear comments and passed the platform's injection review; the pre-check confirms `linear_list_comments` returns them |
| Brian's hours | plan/sweeps/coherence_sweep.md | Fixed: hub 20:40 UTC and note 20:25 UTC on 30 Sep, earlier line 11:20 UTC on 29 Sep, all inside his 10:00 to 21:11 UTC range; the earlier line no longer falls in his #zm-collect-win burst and says 'on Friday' on a Monday |
| Row 5: Vincent's chat ok never covered the coin replay | plan/sweeps/coherence_sweep.md | Fixed: the 'ok, chat' rows are now 1, 2 and 25, the tutorials and Boss Arena his words cover (D06UPGF5PQV/1758820544.160399); row 5 is re-tested on a main build |
| Row 3 reads as 'back' on the canvas on 30 Sep | plan/sweeps/coherence_sweep.md | Fixed: row 3 is now a different report (quest tutorial arrow); the canvas item is CF4EDAF93359/1759236624.010909 |
| 'Nathan's chest' is a Domino Delights name | plan/sweeps/coherence_sweep.md | Fixed: row 20 is the win streak freezer from the abandoned pack, the wording of base ZOM-560 |
| Trello id times, invitation subject format, one event row per attendee | plan/sweeps/coherence_sweep.md | Fixed in the plan: Trello ids are built from their second, subjects end '(CST) (calvin.price@harmonygames.co)', and each attendee calendar gets its own event row; section 11. The base pattern for Trello ids is action 68dc07f69bc8f26035805883, whose first eight hex digits are its second |
| Arthur's inline comments: no Slack copy, too long | plan/sweeps/coherence_sweep.md | Fixed: one line each, with a GitHub-app copy planned under each PR's opened message in C093LEZGF6J (thread 1759185399.395419 for #472) |
| Robert never mails Calvin | plan/sweeps/coherence_sweep.md | Fixed: the mailed report is gone. Robert now posts once in #zombie-match3d (C0880U9751A), where he writes about builds he plays, and that post reverses a pass on row 29 |
| No 'ZM weekly' deck series; Calvin has no recent folders | plan/sweeps/coherence_sweep.md | Fixed and accepted: the weekly deck is gone. Calvin's folder and his queue manager deck, both dated 23 Sep, stay; the sweep found they contradict nothing, and Calvin owns three decks in the base census (his Drive root is d_49b9dfa5208d400d9b3937) |
| Known-data cards: SC-57, SC-13, SC-14, SC-15 at risk | plan/sweeps/coherence_sweep.md | Dispositioned in section 1a. No seed posts in #zm-collect-win, the review card is off the BETA list, no complete flag is read, and ZOM-528 is no longer a plausible home for any report |
| Not checked by the sweep: sheet titles one by one, about 20 canvas items with empty text | plan/sweeps/coherence_sweep.md | Carried to Unresolved; the injection stage re-sweeps design-3 (the canvas item with text is CF4EDAF93359/1759236624.010909) |


## 14 Revision intake

Consumes `Working_Files/run_forensics/rev1/precheck.node_verdicts.json` (one Opus 5.5 platform pre-check, bound to rev1 as the sole revision, BOUND on seeded content) and `Working_Files/01a_Hardening_Report.md`. The platform /hardness on rev1 was FAIL, score 2: every rule leaked. No CONFOUNDED candidate was flagged and none is assigned: no tool, fairness, verifier or run cause was found.

| Node | Runs | Proposed verdict | Disposition | Evidence | What rev2 changes |
|---|---|---|---|---|---|
| BRANCH | precheck (1 run) | LEAKED | keep | precheck event 219 | nothing: it took the run until call 74 to find the rule; persistence beat it, not placement |
| INLINE | precheck (1 run) | LEAKED | rebuild | precheck event 129 | Brian's note no longer says to check the PR or its review; the status definition is 'a fix for it is in main that QA has not tried yet' and Arthur's comment settles the row as a fact |
| REOPEN | precheck (1 run) | LEAKED | rebuild | precheck event 85 | Vincent's line moves from a Sep 30 thread, inside the window the run paged, to a reply under his Sep 15 submission-issues thread; the rule that a later sighting ends a pass moves from the note into Arthur's doc |
| BACK | precheck (1 run) | LEAKED | rebuild | precheck event 75 | Robert's line moves from a top-level post in #zombie-match3d to a reply under his Sep 10 endless thread in #zombie-bugs |
| ELSE | precheck (1 run) | LEAKED | rebuild | precheck event 154 | the note's sentence about a dev's own merged PR is cut; Oliver's comment still states the fact |
| FILT | precheck (1 run) | BYPASSED by the tool, LEAKED on review | keep | precheck event 102 | nothing: the scope sentence has to stay or the population forks |
| ALIAS | precheck (1 run) | LEAKED | keep | precheck event 295 | the note's 'under another name' sentence is cut; the tie is still Vincent's notes on ZOM-556 and ZOM-560. CONFOUNDED candidate rejected: the pending key is a representation difference (a new sub-issue's key in the Ticket cell), not a tool, fairness, verifier or run cause |
| GATE | precheck (1 run) | LEAKED | rebuild | precheck event 278 | the note names the agenda of Thursday's review, not Leonard's card; the updated invitation points at the roadmap card |

Added in rev2, each a v2 move and none a new row or step:

- A sighting on an older build (D_OLDBUILD): Robert reports the arena button bug on Android #2006, built 40 minutes before iOS Internal #1745 where row 27 passed. Under Arthur's sentence the pass stands. It sits on the swept path on purpose: the check is the build order, not the search (the run paged that channel at precheck event 75).
- Two timing rows on existing rows: row 18 was re-tested on Android #2013, built before #472 merged, so QA has not tried the fix (Waiting on QA); row 34 was re-tested on iOS Internal #1757, built after #475 merged, so the fix did not hold (Waiting on a fix); the run compared a build's time with another's once, for build 135, in the sheet it wrote at precheck event 469.
- The five totals did not change in rev2 (12, 6, 21, 1, 6); the prompt does not change (the run's reply at precheck event 502 gave the same five).


Rev3 intake (after the platform /hardness on rev2, NON-FAIL score 3, and six Opus 5.5 baseline runs on rev2 in `07_Baseline_Trajectories/`, graded by hand against the rev2 truth; counts in `Working_Files/platform_reports/hardness_rev2_NONFAIL.md` and `Working_Files/run_forensics/rev2/baseline/calls.json`):

- INLINE and ELSE landed in all seven runs: nobody read Arthur's review comments on harmonygames-Games/match3d#472 and harmonygames-Games/match3d#475 or Oliver's comment harmonygames-Games/match3d#473#c_2. Disposition keep, and widen: row 15 (ZOM-574) joins Arthur's comment on #472, rows 14 and 37 (ZOM-573, ZOM-584) join Oliver's comment. The two swaps cancelled in the totals on rev2 (2 each way); on rev3 they are 3 against 4, so the Waiting on QA and Waiting on a fix numbers move with them (on rev1 the same comments were read only once the note pointed at them, precheck event 129).

- REOPEN and BACK landed in one run of seven (the Slack replies are found by a dated search). Disposition keep, and add a second carrier each: a dev's later note on the row's own ticket (ZOM-585 for row 17, ZOM-586 for row 24). Two of six baseline runs read the comments of every ticket in the sheet before writing, four did not. Row 17 is in a review area and row 24 is the last open row of Zombie Lane, so the Passed, review-list and clear-area numbers depend on them (the Slack carrier's read on rev1 is precheck event 85).

- New carrier under ELSE: the description of Calvin's own merged PR #472 gains the pre-level panel fix (row 6, ZOM-568). One of six runs opened #472 itself and two more asked for descriptions in the list (on rev1 the PR conversation was opened at precheck event 154).

- BRANCH, FILT, ALIAS, GATE, the timing rows and D_OLDBUILD leaked in all seven runs. Disposition keep as they are: they carry the task and fork if removed (rule found at precheck event 219).

- Totals on rev3: 10 Passed, 9 Waiting on QA, 20 Waiting on a fix, no area Clear, 7 on the review list; 22 existing tickets, 17 new sub-issues. No new rule: the solver still has eight. The prompt does not change (the rev1 reply with its five numbers is precheck event 502).

Routing: all changes are universe-side and go to /create-injection as rev2, then /injection and /prompt again. No prompt-side, OE or rubric defect was found; the rubric should accept the reply as a new DM message or a thread reply. The rev1 export stays bound to rev1 and certifies nothing about rev2.

Counter-readings for the eight verdicts are in the hardening report's Self-review; the strongest one against this revision: Opus 5.5 found a rule nobody pointed to in 60 calls, so cutting pointers may only cost it calls. Resolution: the cut sentences were the reason it read review comments and every PR's conversation (precheck events 129 and 154); without them those reads have no trigger, and the ledger shows done_gap landing 2 of 7 times against 0 of 12 for superseding.
