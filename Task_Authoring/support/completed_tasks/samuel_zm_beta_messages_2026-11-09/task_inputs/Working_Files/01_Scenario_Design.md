# Scenario Design — samuel_zm_beta_messages · design only · contains no prompt, OE or criterion text

Written 2026-11-04 by `/create-scenario` (Claude Opus 5.5). Builders: `plan/build_scenario.py` (manifest, surface, ids), `plan/assemble_design.py` (this file), `plan/policy_scores.py` (UNCALIBRATED scores). Prior analysis: `Working_Files/00_Pre_Scenario_Analysis.md`.

## 0 Assignment, persona census and horizon note

| Field | Value |
|---|---|
| Universe | key `synthcut`, label Oct 1, 2025 (synth-cut), `Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)`; seed bound `freeze_utc` 2025-10-01T00:00:00Z; `shutdown_rules_apply` False |
| Assignment | Design · Samuel Turner (Game Designer, `samuel.turner@harmonygames.co`) · Marketing and GTM · Retrieval · long-horizon · medium · October 1, 2025 07:00 |
| Evals category | Product & Design (`Evals/references/rules/task_categories.md`: gameplay and design requirements) inside Marketing and GTM (focus: demand and retention, GTM, communications) |
| Loss budget | Medium cap < 85 %. Requester bar on 2026-11-04: corrected average under 80 %, over 130 tool calls in every run, all other gates apply. Design target E[avg] ≤ 72 % (8 points under the bar) |
| Profile | `effective_profile: extreme` (Long Horizon); `volume_exception {call_budget_floor: 200, per_record_floor: 90}` |
| Theme screen | The game is Zombie Match 3D and the base copy says "zombie outbreak" and "Plague Race". 12 stored Opus 5.5 ZM baselines (Julia, Douglas) mention "zombie" 253–1,350 times and "plague" 23–129 times with 0 `model_refusal_fallback` events. Accepted under the requester's delegation; seeded text avoids those words, and the pre-check is read for fallback events. Base copy stays as it is (`f_a325dd4af80afc5994d5dc`) |
| Role remit | Samuel built these messages: Leonard sent him the sheet (`D06L58XCVKK/1750138057.452159`), the card is `6851a769c65dc0017a227bb7`, and he merged `harmonygames-Games/match3d#248` |
| Decisions taken | The requester delegated every open choice on 2026-11-04 (`you can choose from your self which option is best fit`): storyline B, the volume exception, the review fallback (§13), one read of `match3d/Assets/Scripts/Notifications/NotificationManager.cs` outside `hg.py` (no other repo file was read) and the theme acceptance |

Lessons taken from the completed tasks, and where they bind this design:

| Source | Measured | Applied here |
|---|---|---|
| `frederick_bridge_pipeline_2026-11-03` | Reads alone stalled at 60–83 calls; about 44 single-object writes lifted every run to 109–150 | Two writes per ticket with no batch form, sized so a lean run clears 150 (§9) |
| `douglas_beta_server_signoff_2026-10-28` | 166–239 calls on 17 tickets: per-ticket comments plus a comment and an update each; inline PR comments opened in 1 of 6 runs | Ticket-per-message spine; DONE sits on an inline comment |
| `julia_zm_difficulty_baseline_2026-11-01` | Judgement traps did not land across 28+ runs; DM thread replies and inline comments discriminated; SD 0.099 on one choke point | QA sits in a DM thread reply; eight independent channels; DEP rated lowest |
| `frederick_card_spend_q3_6ad83eebbd6456fd065bbd20` | SD 0.054: every run lost the same rows | Each channel has its own behaviour and at least two rows |
| `frederick_account_handover_2026-10-26` | Bimodal from one hidden class; 80.8 % | No single discovery decides most rows; the largest channel moves about 14 % of the weight |
| `robert_winddown_closeout_2026-10-30` | About 100 rows passed every run; SD flat | Always-pass weight kept near a quarter, 35 members graded by samples |
| `frederick_q4_commitments` rev3 pre-check | One Slack search per name found every named correction; 1 of 8 nodes landed | Corrections use aliases with 0 base hits (`plan/literal_sweep.txt`); feature names are common words |

```
REACH  Samuel Turner <samuel.turner@harmonygames.co>  Game Designer / Design
clock 2025-10-01

SLACK  user=EMPLOYEE_0004_SLACK_ID  visible channels=84 {'public': 17, 'private': 24, 'mpim': 17, 'im': 26}  messages=170930  public-not-member (UNVERIFIED)=50
  persona posts=4586 last post=2025-09-29  last activity in visible channels=2025-10-01
  C05433XK267    builds                                 public  mem=31  msgs=35617  2023-04-20..2025-10-01
  C05H8KVNU67    game-design                            private mem=27  msgs=22750  2023-07-16..2025-08-28 archived
  C050WGU41HR    engineering-bots                       private mem=35  msgs=19854  2023-03-29..2025-09-19
  C05V5FNLB9V    god-bugs                               private mem=31  msgs=16695  2023-10-07..2025-07-15
  C0880U9751A    zombie-match3d                         private mem=25  msgs=16250  2025-01-09..2025-09-30
  C0553V44CE4    god-ui-ux                              private mem=30  msgs=5008   2023-04-21..2025-05-29 archived
  C04S28HSD0U    product                                private mem=21  msgs=4365   2023-03-02..2024-05-11 archived
  C069FF9Q57S    analytics                              private mem=28  msgs=4276   2023-12-05..2025-09-19
  C05KNDCHAAG    company-internal                       private mem=38  msgs=4048   2023-07-31..2025-10-01
  C04RYU8TJ8K    random                                 public  mem=32  msgs=3950   2023-03-02..2025-09-29
  C08R27X0EAH    zombie-bugs                            private mem=23  msgs=3830   2025-05-06..2025-09-30
  C04V7N09LE7    god-gameart                            private mem=30  msgs=3744   2023-03-22..2025-07-15
  C05UQKDLGAU    god-vfx                                private mem=29  msgs=2763   2023-09-26..2025-04-18 archived
  C08R8CHB0QL    zombie-art                             public  mem=23  msgs=2650   2025-05-06..2025-09-30
  D06KV30TPL4    D06KV30TPL4                            im      mem=5   msgs=2189   2024-02-20..2025-09-23

GMAIL  mailbox=samuel.turner@harmonygames.co threads=3870 messages=4504 range=2024-02-20..2025-10-01
  threads by last-message month (recent): {'2025-05': 29, '2025-06': 26, '2025-07': 36, '2025-08': 35, '2025-09': 31, '2025-10': 1}
  top correspondents: SVC_0107_EMAIL (2959), SVC_0248_EMAIL (912), SVC_2463_EMAIL (807), SVC_0613_EMAIL (542), SVC_5123_EMAIL (282), SVC_0251_EMAIL (184), leonard.hayes@harmonygames.co (136), robert@harmonygames.co (120), owen.baker@harmonygames.co (118), julia.lawson@harmonygames.co (117), SVC_2809_EMAIL (111), marcus.bennett@harmonygames.co (110), SVC_3649_EMAIL (105), arthur.blake@harmonygames.co (99), calvin.price@harmonygames.co (98)

GCAL  own=['samuel.turner@harmonygames.co'] shared=[] events=344 (distinct ical_uid 83, cancelled 30)
  last event before clock=2025-09-29T16:30:00Z  next after clock=None
  by month: 2023-10:1 2024-02:5 2024-03:5 2024-04:17 2024-05:20 2024-06:30 2024-07:25 2024-08:14 2024-09:32 2024-10:19 2024-11:23 2024-12:26 2025-01:27 2025-02:13 2025-03:5 2025-04:14 2025-05:18 2025-06:20 2025-07:19 2025-08:2 2025-09:9

DRIVE  owned=24 {'application/vnd.google-apps.spreadsheet': 9, 'text/csv': 6, 'application/json': 6, 'application/vnd.google-apps.document': 2, 'folder': 1}
  shared-with=108 {'application/vnd.google-apps.document': 38, 'text/plain': 27, 'application/json': 21, 'application/vnd.google-apps.spreadsheet': 19, 'text/csv': 2, 'application/vnd.google-apps.presentation': 1}
  shared by owner: {'Resource: -6481757892984311338': 100, 'leonard.hayes@harmonygames.co': 4, 'robert@harmonygames.co': 2, 'Resource: 7240535625619857401': 1, 'calvin.price@harmonygames.co': 1}
  native visible: {'gdocs': 40, 'gsheets': 28, 'gslides': 1}  last modified visible=2025-09-30T16:30:39Z
  UNVERIFIED (domain/anyone, not owned/shared)=104 {'application/vnd.google-apps.document': 38, 'application/vnd.google-apps.spreadsheet': 37, 'application/pdf': 11, 'application/json': 11, 'application/vnd.google-apps.presentation': 7}

UNSCOPED (always visible): contacts, github, trello, linear, snowflake, confluence

LAST ACTIVITY (days before clock): slack_persona_post=2025-09-29 (2d), slack_visible_channels=2025-10-01 (0d), gmail=2025-10-01 (0d), gcal_last_event_before_clock=2025-09-29 (2d), drive_last_modified_visible=2025-09-30 (1d)
```

Linear, GitHub, Trello and Confluence identities (`entity.py resolve`):

```
ENTITY email:samuel.turner@harmonygames.co  name=Samuel Turner  kind=person  emails=['samuel.turner@harmonygames.co']
  persona: samuel_turner - Game Designer / Design
  slack      id=EMPLOYEE_0004_SLACK_ID, name=Samuel Turner, real_name=Samuel Turner, email=samuel.turner@harmonygames.co, is_bot=False, deleted=False, messages=4586, first_post=2024-02-20, last_post=2025-09-29   [join: exact_email]
  gmail      mailbox=samuel.turner@harmonygames.co, threads=3870, messages=4504, first=2024-02-20, last=2025-10-01, thread_filename_alias=['samuel@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=samuel.turner@harmonygames.co, owner_email=samuel.turner@harmonygames.co, summary=Samuel Turner — primary, events=344, last_event_before_clock=2025-09-29   [join: exact_email]
  gdrive     id=user_caafeec2804b, email=samuel.turner@harmonygames.co, display_name=samuel.turner@harmonygames.co, root_folders=['d_caafeec2804b3a67ce46aa'], owned_items=24, last_modified=2025-07-04, files_shared_with=108   [join: exact_email]
  linear     id=usr_caafeec2804b3a67, email=samuel.turner@harmonygames.co, name=samuel.turner@harmonygames.co, is_active=True, last_activity=2025-09-30   [join: exact_email]
  github     login=EMPLOYEE_0004_GITHUB_USERNAME, name=Samuel Turner, email=samuel.turner@harmonygames.co, type=User, last_activity=2025-09-29   [join: exact_email]
  trello     id=4ac40f0fbbad94d9e0e2df2a, username=samuel.turner, fullName=Samuel Turner   [join: exact_name]
  confluence id=user_STAFF_18, account_id=acct_STAFF_18, email=samuel.turner@harmonygames.co, display_name=Samuel Turner, is_active=True   [join: exact_email]
  contacts   contact_id=caafeec2804b3a67ce46aabb, name=Samuel Turner, email=samuel.turner@harmonygames.co, job=Game Designer, is_user=False   [join: exact_email]
  last activity: {'slack': '2025-09-29', 'gmail': '2025-10-01', 'gcal': '2025-09-29', 'gdrive': '2025-07-04', 'linear': '2025-09-30', 'github': '2025-09-29'}
```

## 1 Storyline

The beta decides iterate or pivot on D1 and D7, and UA money is about to go behind it. What the game says to a player who stops playing is one of the few retention levers left, and the push notification sheet has not moved since June. Leonard wants one straight answer on what players will actually hear. The sheet says six are Ready; only three really go. Samuel built these messages, so the plan lands with him, and the team gets a note on what a lapsed player hears and when.

- Sheet and owner: PNs Beta tab of `f_a325dd4af80afc5994d5dc`, last edited 2025-06-23, 14 rows; Leonard handed it to Samuel on Jun 17 (`D06L58XCVKK/1750138057.452159`, `D06L58XCVKK/1750138076.953689`).
- Client: `harmonygames-Games/match3d#248` added six messages; the current source schedules exactly those six. Everything is local (`C08R27X0EAH/1758239520.618939`, `D06KV30TPL4/1750979784.704799`).
- Beta scope: `C05KNDCHAAG/1757704290.799329` (Sep 12) and `C05KNDCHAAG/1758558164.541689` (Sep 22); ZM ROADMAP board `6851a6569f3bf818760632ab`.
- Permission ask: `D06KPMDV2JZ/1752162738.497679` (Jul 10), `C08R27X0EAH/1755084279.518809` (Aug 13), `C08R27X0EAH/1758238811.686629` (Sep 18), `C08R27X0EAH/1758291802.756889` (Sep 19).
- Retention stakes: Leonard's beta-then-decide framing and the weekly cohorts in the warehouse (`wh_USER_COHORT_RETENTION`); the permission debate in `C08R27X0EAH/1758238811.686629`.
- Names: rename on Jul 24 (`page_zm3d_gdd`, `page_release_checklist`); Collect & Win is the Zombie Match name for Win & Collect (`page_liveops_calendar`).

Universe KB use: this sits on the timeline spine after the Sep 12 beta pipeline post and the Sep 22 Axe Arena postponement (`references/universe_kb/by_universe/synthcut/timeline.md`). cohorts.json: no fit — the population is sheet rows plus filed asks, not a Linear state or label cohort. trap_catalog precedents: C01 (thread replies that correct), C02 (a stated resolution another person says still fails), D05 (version-marked title families), K02 (app-name lineage: Puzzles vs Zombies), N01 (ticket series collisions).

## 1a Coherence audit

Scope: everything a correct run opens. Hazard ids from `coherence_hazards.json`; cards from `references/known_data_issues/synthcut.md`.

| Record | Category | Fields | Pointer | Hazard or card | Disposition |
|---|---|---|---|---|---|
| Sheet status columns | semantic | Status vs Status (NA, WIP, LIVE) disagree on 4 of 14 rows | `f_a325dd4af80afc5994d5dc` | hazard none listed; sibling of SC-14 | designed claim: the rule doc says neither column decides |
| Sheet vs client copy | quantitative | 1-day and first-mission bodies say Puzzles vs Zombies; the client says Zombie Match 3D; two emoji differ | `f_a325dd4af80afc5994d5dc` | hazard none listed; trap_catalog K02 | dated claim: the rule says emoji don't count; String change is No for the 1-day line; bodies are not graded |
| Permission ask point | temporal | level 20, level 13 on variant C, 'at the beginning', iOS 'at the start of the game', Robert's Sep 18 'punt this even further' | `C08R27X0EAH/1755084279.518809` | hazard T02 not touched | dated claim: Robert's Sep 29 post settles it for the beta build and answers his Sep 18 post (C0880U9751A/1758215775.137159) |
| Snowflake push stats | cross-service referential | 25 ZM rows with provider firebase, Apr 12 to Sep 27, against 'All our PNs are local' | `C08R27X0EAH/1758239520.618939` | hazard R06 family; no card | avoid: Snowflake stays out of the task and nothing asks for send stats |
| Sheet link in DM | cross-service referential | Slack links use Google-native ids | `D06L58XCVKK/1750138057.452159` | hazard R04 | avoid: no row depends on the link; the sheet is found by title |
| GitHub mail subjects | cross-service referential | repo name redacted in some mails | `samuel.turner@harmonygames.co/1836006988541924555` | hazard R03 | avoid: no row reads a subject |
| Arthur's inline comment | cross-service referential | no #zombie-prs copy | `harmonygames-Games/match3d#248` | hazard R07 | declared: the GitHub app subscribed on Jun 30, after the Jun 26 comment |
| Key series | semantic | PR 327 and the Rate Us card cite ENG keys for ZOM work | `harmonygames-Games/match3d#248` | hazard S01 | avoid: no row depends on those keys |
| Thread counters | quantitative | seeded replies change parent counters | `C08R8CHB0QL/1759159849.386619` | hazard Q01 | companion: SQL updates reply_count, reply_users_count, latest_reply |
| Card activity | temporal | a seeded comment moves dateLastActivity | `68d1eb90bef538c7c5c5599d` | hazard T06 | companion: SQL updates the card |
| Parent and child state | state/lifecycle | parent stays open while children change | `DES-314` | hazard L06 | excluded: the parent is never Done |
| Ticket as shipping proof | state/lifecycle | Linear state is not proof of shipping | `ZOM-564` | SC-16; hazard L03 | avoid: seeded DES tickets only; calls rest on the rule tests |
| Assignees | state/lifecycle | open issues on quiet people | `ZOM-542` | hazard L08 | excluded: no seeded ticket is assigned to a quiet person |
| Owner field | identifier/format | sheet owner is a Resource id | `f_a325dd4af80afc5994d5dc` | hazard I14 | avoid: never a write target; the plan is a new sheet Samuel owns |
| Drive name | identifier/format | title keeps .xlsx in Drive | `f_a325dd4af80afc5994d5dc` | hazard I15 | avoid: found by title words |
| Beta date | other | Trello list named BETA: Oct 10 | `68c451141c69fb8af1b4568e` | SC-13 | avoid: no date graded; 'on the BETA list' only |
| Beta flags | other | dueComplete disagrees on beta cards | `68c451141c69fb8af1b4568e` | SC-14 | avoid: no complete flag read |
| Season Pass | other | ship date and analytics status conflict | `page_season_pass_spec` | SC-38 | avoid: the call rests on nothing being scheduled, never on a ship date |
| Retention figures | other | OKR page D1 disagrees with the warehouse | `page_product_okrs` | SC-28 | avoid: the hub names the warehouse and the Sep 15 week; the OKR page is never read for a value |
| Pop-up offers | other | ZOM-225 Done against an Oct 21 card; unclear if live | `ZOM-225` | hazard none listed | avoid: no member depends on it (removed after the review, §13) |
| Telemetry versions | other | 0.1.x vs 0.3.x | `C05433XK267/1753831576.732069` | SC-19 | avoid: no version matching |
| Boss Arena dates | other | prod date before its code | `page_liveops_calendar` | SC-68 | avoid: only 'in the beta' is used, from the BETA list |
| Channel lists | other | leavers stay listed; Slack timezones; Victor on invites | `C08R27X0EAH/1758238811.686629` | SC-7, SC-36, SC-70 | avoid: no membership or timezone is graded |
| #zm-collect-win | other | archived but active | `page_liveops_calendar` | SC-57 | avoid: no post there |

Sibling-defect sweep: other rows with the same defect kind as the four designed Holds. `harmonygames-Games/match3d#248` schedules six messages; Lives and both lapsed rows pass the day test, Plague Race fires daily, which Leonard accepts on its ticket. No seventh built row exists. Hazard categories in scope: temporal T06, semantic S01, referential R03 R04 R07, quantitative Q01, state/lifecycle L06 L08, identifier/format I14 I15.

## 1b Active speakers

Status from `activity.json` (selected universe).

| Person | Email | status_at_clock | Seeding role |
|---|---|---|---|
| Leonard Hayes | leonard.hayes@harmonygames.co | active_sep_2025_quiet_in_oct | hub, rule doc, both line changes, freeze note, parent ticket |
| Robert | robert@harmonygames.co | active_sep_2025_quiet_in_oct | permission decision, asks |
| Arthur Blake | arthur.blake@harmonygames.co | active_sep_2025_quiet_in_oct | inline review comment, client-or-server notes |
| Vincent Parker | vincent.parker@harmonygames.co | active_sep_2025_quiet_in_oct | QA note, ticket passes, DM reply |
| Brian Foster | brian.foster@harmonygames.co | active_sep_2025_quiet_in_oct | asks, opinion post |
| Julia Lawson | julia.lawson@harmonygames.co | active_sep_2025_quiet_in_oct | asks |
| Calvin Price | calvin.price@harmonygames.co | active_sep_2025_quiet_in_oct | Collect & Win ticket, ask |
| Oliver Brooks | oliver.brooks@harmonygames.co | active_sep_2025_quiet_in_oct | ask |
| Owen Baker | owen.baker@harmonygames.co | active_sep_2025_quiet_in_oct | asks |
| Martin Walsh | martin.walsh@harmonygames.co | active_sep_2025_quiet_in_oct | ask |

## 1c Identity traps

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

```
ENTITY email:leonard.hayes@harmonygames.co  name=Leonard Hayes  kind=person  emails=['leonard.hayes@harmonygames.co']
  persona: leonard_hayes - Co-founder & Creative Director / Executive
ENTITY email:robert@harmonygames.co  name=Robert  kind=person  emails=['robert@harmonygames.co']
  persona: robert - Co-Founder & Creative Director / Executive
ENTITY email:arthur.blake@harmonygames.co  name=Arthur Blake  kind=person  emails=['arthur.blake@harmonygames.co']
  persona: arthur_blake - Co-founder & CTO / Executive
ENTITY email:vincent.parker@harmonygames.co  name=Vincent Parker  kind=person  emails=['vincent.parker@harmonygames.co']
  persona: vincent_parker - Game Systems Engineer / Engineering
ENTITY email:brian.foster@harmonygames.co  name=Brian Foster  kind=person  emails=['brian.foster@harmonygames.co']
  persona: brian_foster - Game Engineer / Engineering
ENTITY email:julia.lawson@harmonygames.co  name=Julia Lawson  kind=person  emails=['julia.lawson@harmonygames.co']
  persona: julia_lawson - Product Manager / Product
ENTITY email:calvin.price@harmonygames.co  name=Calvin Price  kind=person  emails=['calvin.price@harmonygames.co']
  persona: calvin_price - Game Engineer (Unity VFX) / Engineering
ENTITY email:oliver.brooks@harmonygames.co  name=Oliver Brooks  kind=person  emails=['oliver.brooks@harmonygames.co']
  persona: oliver_brooks - Senior Game Engineer / Engineering
ENTITY email:owen.baker@harmonygames.co  name=Owen Baker  kind=person  emails=['owen.baker@harmonygames.co']
  persona: owen_baker - Game Engineer (Unity) / Engineering
ENTITY email:martin.walsh@harmonygames.co  name=Martin Walsh  kind=person  emails=['martin.walsh@harmonygames.co']
  persona: martin_walsh - Game Designer / Design
ENTITY email:douglas@harmonygames.co  name=Douglas  kind=person  emails=['douglas@harmonygames.co']
  persona: douglas - Software Engineer / Engineering
```

| Name in records | Correct entity | Lookalike and how it is pinned |
|---|---|---|
| Marcus | marcus.bennett@harmonygames.co | Marcus Lee and a Trello token; no seed uses him |
| Martin | martin.walsh@harmonygames.co | Martin Lewis (`PERSON_0394_EMAIL`); seeds use the full name |
| Blake | arthur.blake@harmonygames.co | the same person; Slack uses Blake, seeds use Arthur |

## 2 Cohort spine

Rule: every row on the PNs Beta tab plus every ask for a new phone message filed on a ticket or a card by Sep 30. 43 looked at, 36 in scope: 14 sheet rows, 18 asks under the parent `DES-314`, 4 asks in comments on other tickets. Calls: Go 2, Hold 28, Drop 6.

| Message | Ticket | Source | Call | What's missing | Audience | Role |
|---|---|---|---|---|---|---|
| Win & Collect start | DES-313 | PNs Beta row 7 | Hold | not scheduled in the client | players on the event | ALIAS |
| Lives recharged | DES-315 | PNs Beta row 3 | Hold | not seen on both platforms | everyone | PULL |
| Lapsed 1 day | DES-316 | PNs Beta row 4 | Go | — | everyone who has stopped | control |
| Lapsed 7 days | DES-317 | PNs Beta row 5 | Go | — | everyone who has stopped | CORR |
| Finish first mission | DES-318 | PNs Beta row 6 | Hold | cannot reach its players | new players below level 20 | DEP |
| Plague Race | DES-319 | PNs Beta row 9 | Hold | not seen on both platforms | players past the race unlock | QA |
| Weekly Leaderboard reset | DES-320 | PNs Beta row 14 | Hold | fires on the wrong day | players past the leaderboard unlock | DONE |
| Quests rollover | DES-321 | PNs Beta row 1 | Hold | not scheduled in the client | everyone | control |
| Login Calendar update | DES-322 | PNs Beta row 12 | Hold | not scheduled in the client | everyone | control |
| Season Pass start | DES-323 | PNs Beta row 13 | Hold | not scheduled in the client | players past the pass unlock | control |
| Hourly Coins | DES-324 | PNs Beta row 2 | Drop | — | everyone | control |
| Nathan's Treasure Hunt | DES-325 | PNs Beta row 8 | Drop | — | everyone | control |
| Streak Fever | DES-326 | PNs Beta row 10 | Drop | — | everyone | control |
| Axe Arena | DES-327 | PNs Beta row 11 | Drop | — | everyone | control |
| Endless entries back | DES-328 | ask under the parent | Hold | not scheduled in the client | players who used all their entries | control |
| Endless weekly result | DES-329 | ask under the parent | Hold | needs a server send | players who ranked that week | control |
| Boss Arena open | DES-330 | ask under the parent | Hold | not scheduled in the client | players past the arena unlock | control |
| Boss Arena last hours | DES-331 | ask under the parent | Hold | not scheduled in the client | players who started the arena | control |
| Season Pass last 48 hours | DES-332 | ask under the parent | Hold | not scheduled in the client | players with unclaimed tiers | control |
| Season Pass premium nudge | DES-333 | ask under the parent | Hold | needs a server send | free-track players near a premium reward | control |
| Plague Race last hour | DES-334 | ask under the parent | Hold | not scheduled in the client | players in a race | control |
| Plague Race result | DES-335 | ask under the parent | Hold | needs a server send | players in a race | control |
| Zombie Lane reward ready | DES-336 | ask under the parent | Hold | not scheduled in the client | players with a reward to claim | control |
| Achievement reward waiting | DES-337 | ask under the parent | Hold | not scheduled in the client | players with a reward to claim | control |
| Daily chest ready | DES-338 | ask under the parent | Hold | not scheduled in the client | everyone | control |
| Free shop coins ready | DES-339 | ask under the parent | Hold | not scheduled in the client | everyone | control |
| Support reply waiting | DES-340 | ask under the parent | Hold | needs a server send | players with an open support thread | control |
| New levels added | DES-341 | ask under the parent | Hold | needs a server send | players past the hand-made levels | control |
| Lapsed 3 days | DES-342 | ask under the parent | Hold | not scheduled in the client | everyone who has stopped | control |
| Lapsed 30 days | DES-343 | ask under the parent | Hold | not scheduled in the client | everyone who has stopped | control |
| Lapsed 14 days | DES-344 | ask under the parent | Drop | — | everyone who has stopped | BUILT |
| Comeback gift | DES-345 | ask under the parent | Drop | — | everyone who has stopped | control |
| Boss Arena attempts refilled | (new ticket) | comment on ZOM-542 | Hold | not scheduled in the client | players who used their attempts | FILT |
| Daily gift about to reset | (new ticket) | comment on ZOM-556 | Hold | not scheduled in the client | players on a gift streak | FILT |
| Teammate sent lives | (new ticket) | comment on ZOM-563 | Hold | needs a server send | players on a team | FILT |
| Infinite lives ending | (new ticket) | comment on ZOM-483 | Hold | not scheduled in the client | players with infinite lives running | FILT |

Looked at and ruled out (boundary records):

| Record | Where | Why it is off the plan |
|---|---|---|
| Rate Us popup | ZOM-397 | shows inside the game |
| Permission popup | ZOM-366 | shows inside the game |
| Plague Race red dot | ZOM-471 | shows inside the game |
| Cards and shop red dots | ZOM-539 | shows inside the game |
| Mini-game lives ready | PNs tab | Domino only, not on PNs Beta |
| Mini-games discover | PNs tab | Domino only, not on PNs Beta |
| Tiledozer and Luckydrop coins | PN BETA Translated tab | Domino only, not on PNs Beta |

Surfaces and shortcut audit:

| Surface | Calls × records | Serves | Why no bulk call | Short-circuit |
|---|---|---|---|---|
| linear `linear_list_comments` | 1.0 × 32 | R2: the Audience each message is written for | linear_list_issues returns descriptions but no comments; comments come one issue at a time | each message's Audience and whether it needs a server send live only in its ticket's comments, and both are plan values, so the read cannot be skipped once the client source shows a message is unbuilt |
| slack `slack_search_public_and_private` | 0.5 × 36 | R2: a Call per message | no channel read covers DMs, threads and every project channel at once; a search is keyed to one feature name | a feature can be cut, moved or re-judged in chat after its ticket was written, so each feature needs its own look before its call stands |
| trello `trello_get_cards_in_list` | 0.25 × 36 | R2: a Call per message | cards_in_list returns one list; the feature-to-card match is a name join per message | whether a feature is in the beta depends on which list its card sits in, and the ticket does not say |
| github `github_get_pull_request_comments + github_get_file_contents` | 3.0 × 6 | R5: the lapsed reminders the client schedules day by day | review comments come one PR at a time and the schedule is only in the client source; github_search_pull_requests carries neither | the six built messages are the only Go candidates, and when each really fires is not on the sheet or the ticket |

Predicate: a message is what reaches a closed phone. No filler: every member is a real sheet row or a teammate's plausible ask with its own decision, and every write is asked for by a record (Reaching the Tool-Call Minimum). The first draft's Drop asks that mapped one-to-one onto Backlog cards were removed after review (§13).

## 3 Hidden authorities

| Authority | Home | Governs | Decoy and scope | Findability |
|---|---|---|---|---|
| H1 the message rule doc (`f_dc45e0e5a8b8635c1b82b2`) | gdocs | R2, R4 | `f_ffbe775ff72a994c5d6b7c`: Domino Delights beta launch plan, 2024, against Zombie Match 3D beta player messages | a search for "message rule" returns it |
| H2 Vincent's QA note (`samuel.turner@harmonygames.co/1843335316636662321`) | gmail | R3 | `page_release_checklist`: whole-build store submission checklist, against phone message checks | a search for "phone messages" returns it |
| H3 the roadmap freeze (`68dae8c7d95e24b55b69bf80`) | trello | R7 | `68c451141c69fb8af1b4568e`: the Minor Bugs to Fix card, for bug tickets, against held message tickets | a search for "Held tickets" returns it |

## 4 Delegation lattice

| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |
|---|---|---|
| A1 | Leonard's DM from yesterday | `D06L58XCVKK/1759264851.763895` |
| A2 | the Zombie Match PN sheet | `f_a325dd4af80afc5994d5dc` |
| A3 | my Drive folder | `d_caafeec2804b3a67ce46aa` |

The hub delegates by role and lists no members. Incorporation table (each quote is verbatim from the planned record):

| Fragment | Service | Record | Kind | Chain | Delegated by | Delegation quote | Requirements |
|---|---|---|---|---|---|---|---|
| K1 | slack | `D06L58XCVKK/1759264851.763895` | requirement | A1 | `D06L58XCVKK/1759264851.763895` | every row on the PNs Beta tab plus every ask for a new phone message that's been filed on a ticket or a card up to today | R1, R6, R9 |
| K2 | gdocs | `f_dc45e0e5a8b8635c1b82b2` | delegation | A1 → K1 | `D06L58XCVKK/1759264851.763895` | using the message rule doc | R2, R3, R4, R8 |
| K3 | gsheets | `f_a325dd4af80afc5994d5dc` | requirement | A2 | `f_a325dd4af80afc5994d5dc` | the Zombie Match PN sheet | R1 |
| K4 | linear | `DES-314` | delegation | A1 → K1 | `D06L58XCVKK/1759264851.763895` | I made tickets for the sheet rows under DES-314 | R6, R7 |
| K5 | gdrive | `d_caafeec2804b3a67ce46aa` | destination | A1 → K1 | `D06L58XCVKK/1759264851.763895` | Put it in one sheet in your Drive folder | R9 |
| K6 | trello | `6851a769c65dc0017a227bb7` | destination | A1 → K1 | `D06L58XCVKK/1759264851.763895` | Every Go goes on a checklist on our push notifications card | R9 |
| K7 | trello | `6851a6569f3bf818760632ab` | requirement | A1 → K1 → K2 | `f_dc45e0e5a8b8635c1b82b2` | on the BETA list of the ZM ROADMAP board | R2 |
| K8 | gmail | `samuel.turner@harmonygames.co/1843335316636662321` | requirement | A1 → K1 → K2 | `f_dc45e0e5a8b8635c1b82b2` | What Vincent counts as seen is in his QA note | R2, R3 |
| K9 | slack | `C0880U9751A/1759167608.326578` | requirement | A1 → K1 → K2 | `f_dc45e0e5a8b8635c1b82b2` | The permission ask is Robert's call | R2, R3 |
| K10 | trello | `68d1eb90bef538c7c5c5599d` | amendment | A1 → K1 → K2 | `f_dc45e0e5a8b8635c1b82b2` | unless the roadmap says otherwise | R7 |
| K11 | slack | `C08R8CHB0QL/1759169129.445834` | amendment | A1 → K1 → K2 | `f_dc45e0e5a8b8635c1b82b2` | the latest line I've called | R4 |
| K12 | github | `harmonygames-Games/match3d#248` | requirement | A1 → K1 → K2 | `f_dc45e0e5a8b8635c1b82b2` | The client already schedules it | R2, R3, R5 |
| K13 | linear | `ZOM-542` | requirement | A1 → K1 | `D06L58XCVKK/1759264851.763895` | filed on a ticket or a card up to today | R1 |
| K14 | linear | `ZOM-556` | requirement | A1 → K1 | `D06L58XCVKK/1759264851.763895` | filed on a ticket or a card up to today | R1 |
| K15 | confluence | `page_liveops_calendar` | requirement | A1 → K1 | `D06L58XCVKK/1759264851.763895` | under whatever name | R6 |
| K16 | gcal | `evt_b56d5b19baa0a573da4553` | requirement | A1 → K1 → K2 | `f_dc45e0e5a8b8635c1b82b2` | the client already covers it under another message | R2 |
| K17 | snowflake | `wh_USER_COHORT_RETENTION` | requirement | A1 → K1 | `D06L58XCVKK/1759264851.763895` | D1 and D7 for the Sep 15 cohort week from the warehouse, iOS and Android separately | R5 |
| K18 | linear | `ZOM-563` | requirement | A1 → K1 | `D06L58XCVKK/1759264851.763895` | filed on a ticket or a card up to today | R1 |
| K19 | linear | `ZOM-483` | requirement | A1 → K1 | `D06L58XCVKK/1759264851.763895` | filed on a ticket or a card up to today | R1 |
| K20 | gcal | `evt_f2c03e69f50acf62c9d1c3` | amendment | A1 → K1 → K2 | `f_dc45e0e5a8b8635c1b82b2` | the latest line I've called | R4 |
| K21 | slack | `C0880U9751A/1759245146.720608` | amendment | A1 → K1 → K2 | `f_dc45e0e5a8b8635c1b82b2` | Vincent has seen it arrive on both iOS and Android | R2, R3 |

Amendments in another service, later in time: K10 (`68dae8c7d95e24b55b69bf80`) amends the Todo sentence of `f_dc45e0e5a8b8635c1b82b2`; K11 (`C08R8CHB0QL/1759169129.445834`) replaces a line, K20 (`evt_f2c03e69f50acf62c9d1c3`) replaces it again, K21 (`C0880U9751A/1759245146.720608`) takes a pass back. Non-authoritative distractors: T12 `C0880U9751A/1758909739.853209`, T10 `f_de7a1ae20201816a67750d`.

## 5 Chains and trap register

| Chain | Root cause | Hops | Ends in |
|---|---|---|---|
| C1 | A24 | gsheets: `f_a325dd4af80afc5994d5dc` (Weekly Leaderboard reset: Status Ready, When Weekly Rollover) → linear: `DES-320` (ticket Done; Vincent saw it arrive on both store builds) → github: `harmonygames-Games/match3d#248#rc_18` (Arthur, Jun 26: counts seven days from the last leave, not tied to the rollover) → github: `harmonygames-Games/match3d#248` (the schedule adds i * 7 days to today, so the day depends on when the player left) | R3 |
| C2 | A11 | gsheets: `f_a325dd4af80afc5994d5dc` (Lapsed 7 days headline from June) → linear: `DES-317` (ticket repeats the June line) → slack: `C08R8CHB0QL/1759169129.445834` (Leonard's thread reply replaces the line with Your Squad Needs You Back) → gcal: `evt_f2c03e69f50acf62c9d1c3` (Leonard's later note on the copy check makes the final line Your Squad Is Waiting) | R4 |
| C3 | A4 | gsheets: `f_a325dd4af80afc5994d5dc` (first-session message: level 20 not completed, 12 hours) → slack: `D06KPMDV2JZ/1752162738.497679` (Robert, Jul 10: shove the ask to level 20) → slack: `C0880U9751A/1759167608.326578` (Robert, Sep 29: stays after level 20, nothing before it in the beta build) → gdocs: `f_dc45e0e5a8b8635c1b82b2` (a player only counts once the ask has happened) | R3 |
| C4 | A14 | linear: `cmt_fd950c410ed25c447c02` (Vincent, Sep 24: arrived on both, the same words as every other pass) → gmail: `samuel.turner@harmonygames.co/1843335316636662321` (a build with shortened timers does not count) → slack: `D06UFE81RF0/1759174846.723833` (Vincent, Sep 29: that iPhone was on the 5-minute timers build, and on 0.3.40 it never showed up) | R3 |
| C5 | A7 | gsheets: `f_a325dd4af80afc5994d5dc` (row says Win & Collect event start) → confluence: `page_liveops_calendar` (Collect & Win is the same feature under a different name) → linear: `DES-313` (an existing ticket outside the parent carries the work) | R6 |
| C6 | A17 | slack: `D06L58XCVKK/1759264851.763895` (asks filed on any ticket or card count) → linear: `DES-330` (a child ticket with a relates-to link to ZOM-542) → linear: `cmt_f1b8a109dfa70cdc4565` (Brian's ask sits in a comment on ZOM-542) | R1 |
| C7 | A25 | linear: `DES-344` (Robert's ask for a day-14 message, no note from Arthur) → gcal: `evt_b56d5b19baa0a573da4553` (cancelled review: the weekly one repeats, day 14 is covered) → github: `harmonygames-Games/match3d#248` (the weekly batch fires on days 7, 14, 21 and 28) | R2 |
| C8 | A15 | gdocs: `f_dc45e0e5a8b8635c1b82b2` (Hold tickets go back to Todo unless the roadmap says otherwise) → trello: `68d1eb90bef538c7c5c5599d` (the tech issues card on the BETA list) → trello: `68dae8c7d95e24b55b69bf80` (Leonard, Sep 29, in the card's description: held tickets sit in Backlog, unassigned) | R7 |
| C9 | A14 | linear: `cmt_51e018b23e18c2f680cd` (Vincent, Sep 24: arrived on both on store builds) → gsheets: `f_8eb8c04713ff6a6ef4a265` (the pass log shows Lives recharged on 0.3.127 and 0.3.40) → slack: `C0880U9751A/1759182908.627389` (Leonard, Sep 29: released 0.3.49 on iOS) → slack: `C0880U9751A/1759245146.720608` (Vincent, Sep 30: Full Ammo did not show on 0.3.49, he takes his tick off it) | R3 |

| Trap | Family | Records | Requirement | Expected wrong reading | Resolver | Discovery order |
|---|---|---|---|---|---|---|
| T1 | done_gap | `harmonygames-Games/match3d#248#rc_18`, `cmt_f76672cf21387ec1eeab`, `f_a325dd4af80afc5994d5dc`, `harmonygames-Games/match3d#248` | R3 | the weekly leaderboard message is finished: the sheet says Ready, its ticket is Done, Vincent saw it arrive and PR #248 merged approved | Arthur's inline comment on PR #248 and the schedule in the client: it counts seven days from the last leave, so it misses the rollover day: Hold, fires on the wrong day | the sheet, the ticket and the approval come back first; the comment needs github_get_pull_request_comments, or the source read closely |
| T2 | superseding | `C08R8CHB0QL/1759169129.445834`, `evt_f2c03e69f50acf62c9d1c3`, `DES-317`, `f_a325dd4af80afc5994d5dc`, `C08R8CHB0QL/1759159849.386619` | R4 | Leonard's Sep 29 reply is the latest line: Your Squad Needs You Back | Leonard's Sep 30 note on the copy check replaces that line with Your Squad Is Waiting; the client still ships the June line, so a string ticket follows | a search for Leonard's posts finds the Sep 29 reply and the hunt stops there; the later note sits on a calendar event |
| T3 | cross_reference_gap | `C0880U9751A/1759167608.326578`, `C0880U9751A/1759170096.924778`, `cmt_f4960d3c073493b6bfc6`, `f_dc45e0e5a8b8635c1b82b2`, `f_a325dd4af80afc5994d5dc`, `D06KPMDV2JZ/1752162738.497679` | R3 | the first-session message is Ready and LIVE with a level 20 trigger, Vincent saw it arrive, so it goes | its trigger selects players below level 20, our own ask is after level 20 and nothing is scheduled before it runs, and the rule counts a player only once asked: Hold, cannot reach its players | each record is plain on its own; only the join shows it |
| T4 | superseding | `cmt_fd950c410ed25c447c02`, `f_8eb8c04713ff6a6ef4a265`, `samuel.turner@harmonygames.co/1843335316636662321`, `D06UFE81RF0/1759174846.723833`, `D06UFE81RF0/1759163970.141449` | R3 | Vincent passed the race message on both platforms on its ticket | Vincent's later thread reply in his DM with Samuel: that iPhone was on the 5-minute timers build, which his QA note says does not count, and on 0.3.40 it never showed up: Hold, not seen on both platforms | the sheet and ticket read like every other pass, so nothing prompts a hunt; the reply sits in a DM thread under a build request and says 'the race one' |
| T5 | scope_alias | `DES-313`, `f_a325dd4af80afc5994d5dc`, `page_liveops_calendar` | R6 | the Win & Collect row has no ticket under the parent, so it needs a new one | the live-ops page says Collect & Win is the same feature under another name, and DES-313 already carries it: reuse it | the parent's children and a Win & Collect search both miss it; the ticket predates the parent |
| T6 | exact_predicate | `cmt_f1b8a109dfa70cdc4565`, `cmt_2b519285937e7fa79453`, `cmt_eabac5435f2b3a575aad`, `cmt_e2e2926a2080ca53c4ea`, `ZOM-542`, `ZOM-556`, `ZOM-563`, `ZOM-483`, `f_a325dd4af80afc5994d5dc` | R1 | the sheet rows and the parent's children are the whole list | Leonard's scope takes in asks on any ticket or card: DES-330 relates to ZOM-542, DES-338 relates to ZOM-556 and DES-315 relates to ZOM-563 and ZOM-483, and each holds an ask in a comment | the relation shows on linear_get_issue with relations; the ask needs linear_list_comments on a ticket about something else |
| T7 | completion_elsewhere | `DES-344`, `evt_b56d5b19baa0a573da4553`, `harmonygames-Games/match3d#248` | R2 | Robert's day-14 ask is not scheduled, so it is a Hold | the weekly message already repeats on days 7, 14, 21 and 28 (the source, and Leonard's cancelled review): Drop, covered by Lapsed 7 days | the ask reads as new work; the source or the cancelled invite settles it |
| T8 | superseding | `f_dc45e0e5a8b8635c1b82b2`, `68dae8c7d95e24b55b69bf80`, `68d1eb90bef538c7c5c5599d` | R7 | the rule doc says Hold tickets go back to Todo | Leonard's later note in the description of the tech issues card: held tickets sit in Backlog, unassigned | the doc is read first; the note is in the description of a card read only for its list position, so a comment listing never shows it |
| T9 | superseding | `C0880U9751A/1759167608.326578`, `D06KPMDV2JZ/1752162738.497679`, `C08R27X0EAH/1755084279.518809` | R3 | the permission ask moves further out, as Robert said on Sep 18, or sits at level 13 on variant C | Robert's Sep 29 post settles it for the beta build: after level 20, not pushed further | older DM and channel records come back first |
| T10 | distractor (stale_summary) | `f_de7a1ae20201816a67750d` | R2 | the beta readiness deck says six messages are Ready, so six go | the deck repeats the June sheet flags; the rule says neither flag decides | — |
| T11 | distractor (near_duplicate_record) | `f_a325dd4af80afc5994d5dc` | R1 | the PN BETA Translated tab and the older PNs tab are part of the list | both hold Domino copy; Leonard's scope is the PNs Beta tab | — |
| T12 | distractor (non_authoritative_instruction) | `C0880U9751A/1758909739.853209` | R2 | Brian's 'send all the Ready ones' settles the calls | Brian does not own the rule; the rule doc decides | — |
| T13 | distractor (other_title) | `ENG-2311` | R2 | ENG-2311 is Done, so event start messages are built | that ticket is Domino Delights; the Zombie Match client schedules six messages | — |
| T14 | distractor (keyword_collision) | `ZOM-471`, `ZOM-539` | R1 | red-dot tickets are asks for notifications | a red dot is in the game; the rule covers what reaches a closed phone | — |
| T16 | superseding | `cmt_51e018b23e18c2f680cd`, `f_8eb8c04713ff6a6ef4a265`, `C0880U9751A/1759245146.720608`, `C0880U9751A/1759182908.627389` | R3 | Vincent passed Lives recharged on both store builds, so it goes | Vincent's Sep 30 post in #zombie-match3d: on 0.3.49 the Full Ammo one did not show up and he takes his tick off it: Hold, not seen on both platforms | the ticket and pass log are clean and read first; the post names the headline, not the row, and sits outside the DM and the search terms the rule gives |
| T15 | distractor (scope_adjacent) | `6874409dfe0decf6f8fca64f`, `ZOM-397` | R1 | Rate Us and the permission popup are messages on the plan | both show inside the game; the rule covers a closed game | — |

Hardness v2 traps, each a separate cross-source decision:

| Channel | v2 trap | Convincing wrong source | Record that beats it | Weight-5 rows |
|---|---|---|---|---|
| DONE | 1 · proving done across services | sheet Ready, ticket Done, approved merge of `harmonygames-Games/match3d#248` | Arthur's inline comment `harmonygames-Games/match3d#248#rc_18` (reviewer, Jun 26) and the source | X1, X2, X2b, X1c, T1 |
| CORR | 2 · a correction somewhere else | Leonard's Sep 29 reply `C08R8CHB0QL/1759169129.445834`, which replaces the June line on `f_a325dd4af80afc5994d5dc` | Leonard's Sep 30 note on the calendar event `evt_f2c03e69f50acf62c9d1c3` | X3, X4 |
| PULL | 2 · a correction somewhere else | Vincent's clean pass `cmt_51e018b23e18c2f680cd` on DES-315 and `f_8eb8c04713ff6a6ef4a265` | Vincent's channel post `C0880U9751A/1759245146.720608` after the 0.3.49 release `C0880U9751A/1759182908.627389` | K1, X21, X21b, X21c, X22, T1 |
| QA | 2 · a correction somewhere else | Vincent's pass `cmt_fd950c410ed25c447c02` on DES-319 | Vincent's DM thread reply `D06UFE81RF0/1759174846.723833` plus his QA note `samuel.turner@harmonygames.co/1843335316636662321` | X7, X8, X8b, X8c, T1 |
| DEP | 4 · dates, windows and dependencies | first-session row, Ready and LIVE | Robert's `D06KPMDV2JZ/1752162738.497679` and `C0880U9751A/1759167608.326578` joined to the trigger | X5, X6, X6b, X6c, X20, T1 |
| ALIAS | 6 · different names for the same thing | no Win & Collect ticket under the parent | `page_liveops_calendar` plus DES-313 | X9, X10 |
| FILT | 7 · items outside the obvious filter | the sheet and the parent's children | comments `cmt_f1b8a109dfa70cdc4565` on ZOM-542, `cmt_2b519285937e7fa79453` on ZOM-556, `cmt_eabac5435f2b3a575aad` on ZOM-563 and `cmt_e2e2926a2080ca53c4ea` on ZOM-483, one relation from a child ticket | X11, X12, X11b, X12b |
| BUILT | 9 · work someone already did | Robert's day-14 ask on DES-344 | the weekly batch in the source and Leonard's cancelled review `evt_b56d5b19baa0a573da4553` | X15, X15b |
| FOLLOW | 3 · follow-through a rule requires | 'back to Todo' in `f_dc45e0e5a8b8635c1b82b2` | Leonard's note `68dae8c7d95e24b55b69bf80` in the description of `68d1eb90bef538c7c5c5599d` | X18, X19, X19b |

### Mechanism portfolio (S5a)

Priors from `tools/hardness_ledger.py priors --model claude-opus-5-5` (UNCALIBRATED, per model): `done_gap` Beta(2,2) mean 0.50, `superseding` Beta(1,3) mean 0.25, `authority` Beta(1,3) mean 0.25, `exact_predicate` Beta(1,3) mean 0.25, `scope_alias` Beta(1,2) mean 0.33, `completion_elsewhere` Beta(1,2) mean 0.33. Each n_eff ≤ 2, from `frederick_bridge_pipeline` and `frederick_q4_commitments`. Design rates are disclosed overrides from measured placements.

| # | Candidate (records) | Coupling | Findability | Prior family | Design rate | Survives complete retrieval | Selected |
|---|---|---|---|---|---|---|---|
| DONE | Weekly reset (`harmonygames-Games/match3d#248#rc_18`) | day test → Hold → note and state | needs inline comments or a close read of the source | done_gap | 0.10 | needs the rollover join | yes |
| CORR | the later line (`evt_f2c03e69f50acf62c9d1c3`, over `C08R8CHB0QL/1759169129.445834`) | line → string ticket text | a calendar note; the Sep 29 reply satisfies the hunt first | superseding | 0.60 | no: placement | yes |
| QA | race one (`D06UFE81RF0/1759174846.723833`) | QA note → Hold → note and state | DM thread under a build request; sheet and ticket read like every other pass | superseding | 0.65 | no: placement | yes |
| PULL | Lives recharged pass withdrawn (`C0880U9751A/1759245146.720608`) | post → Hold → checklist, note and state | root post in #zombie-match3d naming the headline; no search the rule gives reaches it | superseding | 0.60 | no: placement | yes |
| DEP | first-session reach (`C0880U9751A/1759167608.326578`) | ask point → reach test → Hold | all records on the normal path | authority | 0.05 | yes: a join | yes |
| ALIAS | Collect & Win ticket (DES-313) | alias → reuse | outside the parent, other name | scope_alias | 0.10 | yes: a name map | yes |
| FILT | four off-parent asks (`cmt_f1b8a109dfa70cdc4565`, `cmt_2b519285937e7fa79453`, `cmt_eabac5435f2b3a575aad`, `cmt_e2e2926a2080ca53c4ea`) | relation → comment → member → new ticket | one relation from a child ticket | exact_predicate | 0.65 | no: placement | yes |
| BUILT | day 14 already covered (DES-344, `evt_b56d5b19baa0a573da4553`) | source → Drop, name the cover | source read plus a connection, or the cancelled invite | completion_elsewhere | 0.05 | yes: a join | yes |
| FOLLOW | freeze note (`68dae8c7d95e24b55b69bf80`) | amendment → Backlog on every Hold | a card description, read only when cards are listed with desc; a comment listing misses it | superseding | 0.40 | no: placement | yes |
| RATE-US | Rate Us level chain (`6874409dfe0decf6f8fca64f`, ZOM-397) | levels | ticket is plain | superseding | — | — | rejected: in-game prompt, outside the message rule |
| STORE-NOTE | store-review note on promotions (`ZOM-314`) | promo opt-in | older mail | authority | — | — | rejected: conflict risk with Snowflake sale rows, 337 mail hits uncensused, and the general toggle is a fork |
| OLD-NAME | old game name already fixed (`harmonygames-Games/match3d#248`) | source → no string ticket | one source read | completion_elsewhere | — | — | rejected as a trap after review: a run that never opens GitHub answers No for free; kept as a control |
| QUIET | quiet-hours rule on midnight sends | every midnight message | older mail | authority | — | — | rejected: one rule would flip most Go rows (choke point) |
| COUNTS | Hold total in the report (`hev_` not filed) | aggregate of four channels | — | — | — | — | rejected: forecast P(fails all six) 0.66 and no added spread |
| PUSH-ROWS | server sends not set up (`D06KV30TPL4/1750979784.704799`) | needs a server send | per-ticket Arthur notes | — | control | — | kept as a control (K9) |
| V2-GIFT | reward on tap is version 2 (`cmt_13477aa8d1468ae11c9d`) | Drop | on its own ticket | — | ≈0.05 | — | kept as a control |

Each selected rule's controls and over-application are in the draft manifest (`mechanism_portfolio[].controls`, `over_application`), its channel in `channels`.

### Liveness flags (S5b)

`trap_liveness.py --design` (verbatim):

```
TRAP LIVENESS · ADVISORY · UNCALIBRATED · lexical warnings, not proof · DESIGN (no SQL: record text unavailable, only manifest-structure flags can fire) · on the Season Pass backtests these are development fixtures, not validation
  hub D06L58XCVKK/1759264851.763895 · direct delegations 11 · rule placement: A15 nodes only: ['C8', 'T8'] (mechanism_portfolio); every other node SKIP
  T1   done_gap           -  [rule placement SKIP: not an A15 node]
  T2   superseding        -  [rule placement SKIP: not an A15 node]
  T3   cross_reference_ga breadcrumb  [rule placement SKIP: not an A15 node]
  T4   superseding        -  [rule placement SKIP: not an A15 node]
  T5   scope_alias        breadcrumb  [rule placement SKIP: not an A15 node]
  T6   exact_predicate    breadcrumb  [rule placement SKIP: not an A15 node]
  T7   completion_elsewhe -  [rule placement SKIP: not an A15 node]
  T8   superseding        -
  T9   superseding        -  [rule placement SKIP: not an A15 node]
  T10  distractor         -  [rule placement SKIP: not an A15 node]
  T11  distractor         -  [rule placement SKIP: not an A15 node]
  T12  distractor         -  [rule placement SKIP: not an A15 node]
  T13  distractor         -  [rule placement SKIP: not an A15 node]
  T14  distractor         breadcrumb  [rule placement SKIP: not an A15 node]
  T16  superseding        -  [rule placement SKIP: not an A15 node]
  T15  distractor         breadcrumb  [rule placement SKIP: not an A15 node]
  dispositions: 0/5 recorded
```

| Flag | Nodes | Disposition |
|---|---|---|
| breadcrumb | T5, T6, T14, T15 | structural: the hub (`D06L58XCVKK/1759264851.763895`) states the scope and reuse rule these traps depend on, which is the incorporation link. The members themselves sit outside the parent and the sheet |

`hardness_v2_check.py --design` (verbatim):

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      5 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 6 requirements: {'R3': ['DONE', 'DEP', 'QA', 'PULL'], 'R4': ['CORR'], 'R6': ['ALIAS'], 'R1': ['FILT'], 'R2': ['BUILT'], 'R7': ['FOLLOW']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   9 of 9 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     0 weight-5 total(s); 0 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  CLEAN      RULE_IN_PROMPT  no run of 8 resolver words in the prompt  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

No FLAG or UNRESOLVED fired. SAME_PLACE is clean over declared containers and re-runs on the SQL at injection.

## 6 Failure-diversity plan

| Channel | Behaviour that finds the deciding record | Measured analog | Rows | Independent of |
|---|---|---|---|---|
| DONE | opening inline comments, or reading the weekly schedule closely | Douglas: inline comments opened in 1 of 6 runs | X1, X2, X2b, X1c | Slack and mail (`harmonygames-Games/match3d#248#rc_18`) |
| CORR | opening a thread under another topic, or searching the old line's words | bridge SciPlay reply caught 2/8 then 3/6 | X3, X4, X16 | GitHub and Linear (`C08R8CHB0QL/1759169129.445834`) |
| QA | opening a DM thread | Julia: DM thread replies discriminated | X7, X8, X8b, X8c | channel reads (`D06UFE81RF0/1759174846.723833`) |
| DEP | joining a trigger to the ask point | Julia: judgement traps rarely landed, so rated 0.25 | X5, X6, X6b, X6c, X20 | search behaviour (`C0880U9751A/1759167608.326578`) |
| ALIAS | searching a second name | ledger scope_alias mean 0.33 | X9, X10 | everything else (DES-313) |
| FILT | following a relation to a ticket about something else | frederick_q4 rev3: the one trap that landed was outside the filter | X11, X12, X13, V1 | ZOM-542, ZOM-556 |
| BUILT | connecting the batch in the source to the day-14 ask | Julia: github_get_file_contents in 4 of 6 runs; a join on top | X15, X15b, T3 | Slack (`harmonygames-Games/match3d#248`) |
| FOLLOW | reading comments on a card seen only in a list | Douglas: trello_get_comments in 3 of 6 runs | X18, X19, X19b | Linear (`68d1eb90bef538c7c5c5599d`) |

Named correlation: DONE and BUILT both reward reading GitHub; CORR and QA both reward opening threads. `plan/policy_scores.py` models those two shared latents on top of a run-level latent.

```
UNCALIBRATED · surface 57 slots, weight 227, mechanism-flippable 181 (79.7%), always-pass 46 (20.3%)

Whole policies
  100.0%  Perfect  [lands: -]
   20.3%  Sheet flags and the parent's children only  [lands: ALIAS, BUILT, CORR, DEP, DONE, FILT, FOLLOW, PULL, QA]
   83.3%  Thorough on tickets, never opens GitHub  [lands: BUILT, DONE]
   72.2%  Thorough on tickets and GitHub, never opens Slack threads or the calendar  [lands: CORR, PULL, QA]
   86.8%  Reads everything, takes each flag literally (no join)  [lands: DEP]
   56.8%  Trusts Done tickets, otherwise thorough  [lands: DEP, DONE, PULL, QA]
   78.9%  Stays inside the sheet's names and the parent  [lands: ALIAS, FILT]
   93.4%  Right calls, misses the freeze note  [lands: FOLLOW]
   50.2%  The rev5 pre-check run, replayed on rev6 (its reads, new records unseen)  [lands: CORR, FILT, FOLLOW, PULL, QA]

Single misses
  DONE     89.0%
  CORR     95.6%
  DEP      86.8%
  QA       89.0%
  PULL     85.5%
  ALIAS    95.6%
  FILT     83.3%
  BUILT    94.3%
  FOLLOW   93.4%

Pairs at or above the 80 % bar: ['DONE+CORR', 'DONE+QA', 'DONE+ALIAS', 'DONE+BUILT', 'DONE+FOLLOW', 'CORR+DEP', 'CORR+QA', 'CORR+PULL', 'CORR+ALIAS', 'CORR+BUILT', 'CORR+FOLLOW', 'DEP+ALIAS', 'DEP+BUILT', 'DEP+FOLLOW', 'QA+ALIAS', 'QA+BUILT', 'QA+FOLLOW', 'PULL+ALIAS', 'ALIAS+BUILT', 'ALIAS+FOLLOW', 'BUILT+FOLLOW']

Design landing rates {'DONE': 0.1, 'CORR': 0.6, 'DEP': 0.05, 'QA': 0.65, 'PULL': 0.6, 'ALIAS': 0.1, 'FILT': 0.65, 'BUILT': 0.05, 'FOLLOW': 0.4}; sum 3.20, mean 0.36
P(one run catches every trap) ~ 0.009 under independence -> E[full passes of 6] ~ 0.05

Six-run Monte Carlo (run latent rho, plus shared latents for code-read and thread-open behaviour)
  scale mean-rate rho   E[avg]  P(<80)  P(<85)  P(SD)  P(<5 full)  P(patterns)  P(all, 80 bar)  P(all, 85 cap)
  1.00    0.36   0.30  66.6%    0.97    1.00   0.86       1.00        1.00           0.83           0.85
  1.00    0.36   0.50  66.7%    0.95    0.99   0.93       1.00        0.99           0.88           0.91
  0.80    0.28   0.35  73.0%    0.83    0.95   0.91       1.00        1.00           0.76           0.87
  0.70    0.25   0.35  76.2%    0.69    0.89   0.89       1.00        1.00           0.64           0.81
  0.60    0.21   0.35  79.4%    0.52    0.78   0.87       1.00        0.99           0.48           0.72
  0.60    0.21   0.50  79.5%    0.51    0.75   0.90       1.00        0.99           0.49           0.72
  0.50    0.18   0.35  82.7%    0.33    0.61   0.81       1.00        0.99           0.31           0.56
  0.40    0.14   0.35  86.0%    0.17    0.41   0.71       1.00        0.98           0.16           0.38
  0.30    0.11   0.35  89.3%    0.06    0.21   0.58       0.99        0.97           0.05           0.19
```

**Read of these numbers.** The result turns on the real per-trap landing rate. The rates were lowered after the independent review, which estimated about 0.25 for the first draft. Measured per-trap landing: 0.50 on bridge rev12 batch 2, about 0.33 on bridge pre-checks, 0.125 on the frederick_q4 rev3 pre-check before de-naming. At 0.125 this design would miss the bar; at 0.25 the bar is close to a coin flip.

## 7 Deliverables and dependent writes

| Write | Tool | Count | Depends on | Requirements | Target and access |
|---|---|---|---|---|---|
| gsheets | `gsheets_create_spreadsheet+gsheets_values_update` | 3 | K1, K2, C1, C2, C3, C4, C5, C6, C7, C9 | R1, R2, R3, R4, R9 | new sheet, Samuel as owner, moved into `d_caafeec2804b3a67ce46aa` |
| gdocs | `gdocs_create_document` | 1 | K1, K17, C7 | R5 | new doc, Samuel as owner, moved into `d_caafeec2804b3a67ce46aa` |
| gdrive | `gdrive_move_file` | 2 | K5 | R9 | `d_caafeec2804b3a67ce46aa` (YES, owner) |
| linear | `linear_create_comment` | 32 | K4, C1, C3, C4, C5, C9 | R6 | seeded DES tickets under `DES-314`; `DES-313`; team DES |
| linear | `linear_update_issue` | 30 | K4, K10, C8 | R7 | seeded DES tickets under `DES-314`; `DES-313`; team DES |
| linear | `linear_create_issue` | 5 | K13, K14, K18, K19, C2, C6 | R6, R8 | seeded DES tickets under `DES-314`; `DES-313`; team DES |
| trello | `trello_create_checklist+trello_create_check_item` | 3 | K6, C1, C3, C4, C9 | R9 | card `6851a769c65dc0017a227bb7` |
| gmail | `gmail_send_message` | 8 | K1, C6, C7 | R9 | one email per asker from Samuel's mailbox |
| slack | `slack_send_message` | 1 | K1 | R9 | `D06L58XCVKK` |

Reuse vs create (A8): the Win & Collect row reuses DES-313. The PN sheet is never a write target: its owner is a Resource id and write access is unproven (learnings §31).

## 8 Service role map

| Service | Role | Load-bearing fact or write | Carrier |
|---|---|---|---|
| slack | hub DM; Robert's ask decision; Leonard's Sep 29 line; Vincent's DM reply and his channel post; feature talk | the ask, the ask point, the first line change and both withdrawn QA passes live here | ● (`D06L58XCVKK/1759264851.763895`) |
| gsheets | the PN sheet (population, June flags and copy); Vincent's pass log; the plan sheet | the population, the build behind each pass, and the deliverable | ● (`f_a325dd4af80afc5994d5dc`) |
| gdocs | the message rule doc; the team note | the ordered tests, and the note that tells the team what players hear | ● (`f_dc45e0e5a8b8635c1b82b2`) |
| gdrive | Samuel's folder, owner of the plan | the destination the plan must land in | ● (`d_caafeec2804b3a67ce46aa`) |
| linear | one ticket per message, its notes and comments, off-parent asks, new tickets | per-message build, QA and client-or-server facts, and the ticket writes | ● (`DES-314`) |
| trello | ZM ROADMAP lists for beta scope, the push notifications card, the freeze note in a card description, the list rename | In the beta, the Go checklist and the Hold parking rule | ● (`6851a769c65dc0017a227bb7`) |
| github | match3d#248, Arthur's inline comment, the client source | what the client schedules and when | ● (`harmonygames-Games/match3d#248`) |
| gmail | Vincent's QA note; the GitHub mail for Arthur's comment; the emails to each asker | what counts as seen, and telling each asker the outcome | ● (`samuel.turner@harmonygames.co/1843335316636662321`) |
| gcal | the cancelled ladder review; the copy check note | the completion note that settles the day-14 ask, and the final headline | ● (`evt_b56d5b19baa0a573da4553`) |
| gslides | beta readiness deck, a stale summary | the convincing wrong count of six | ● (`f_de7a1ae20201816a67750d`) |
| confluence | live-ops page and release checklist, base only | the Collect & Win name map and feature state | ● (`page_liveops_calendar`) |
| snowflake | USER_COHORT_RETENTION, read only | the D1 and D7 baseline the note opens with | ● (`wh_USER_COHORT_RETENTION`) |
| contacts | not used | no value needs it | — |

## 9 Call budget

| Phase | Service | Calls | Why each call answers a distinct question |
|---|---|---|---|
| discovery | slack | 4 | read the hub; read the DM history around it; find the PN thread in #zombie-bugs |
| discovery | gdocs | 2 | read the rule doc; reject the 2024 GTM - Beta doc on scope |
| discovery | gsheets | 4 | list the tabs; read PNs Beta; read the older PNs tab; read PN BETA Translated to rule it out |
| discovery | trello | 5 | board lists; BETA, Oct 21 and Backlog lists for beta scope; the push notifications card |
| discovery | confluence | 3 | live-ops page for feature state and names; GDD; release checklist |
| discovery | gslides | 1 | read the beta readiness deck the search returns and reject it |
| discovery | gdrive | 2 | confirm the folder; find the rule doc |
| discovery | gcal | 2 | list the window for message reviews and QA sessions |
| discovery | gmail | 3 | find Vincent's QA note; open it; search for message mail |
| discovery | linear | 4 | read the parent; its comments; page its children; search for message asks |
| discovery | snowflake | 2 | describe the cohort table; read the Sep 15 week |
| per-record | linear | 32 | one linear_list_comments per message ticket: Audience and the client-or-server note exist nowhere else |
| per-record | slack | 22 | a search per feature family (the stored Frederick run made 39 for 36 members): a feature can be cut or re-judged in chat after its ticket was written |
| per-record | trello | 9 | a card check per feature: which list it sits on decides In the beta |
| per-record | github | 18 | PR reviews, inline comments and source for the six built messages |
| per-record | linear | 32 | one linear_create_comment per ticket: the call lands on each ticket, no batch form exists |
| per-record | linear | 30 | one linear_update_issue per Hold and Drop ticket: the state follows the call, no batch form exists |
| per-record | linear | 5 | new tickets for the four off-parent asks and the one string change |
| per-record | trello | 3 | the checklist and one trello_create_check_item per Go message |
| per-record | gmail | 8 | one email per person who asked: each lists that person's asks and their calls |
| writes | gsheets | 3 | create the plan sheet; write the rows; check it |
| writes | gdocs | 1 | create the team note |
| writes | gdrive | 2 | move the sheet and the note into the folder |
| writes | slack | 1 | report the counts to Leonard |
| readback | gsheets | 1 | read the plan back |
| readback | linear | 2 | spot-check ticket states |
| readback | trello | 1 | read the checklist back |
| **Total** | 11 services | **202** | per-record 77 on the surfaces |

**The over-130 bar.** A lean correct run: 32 ticket comment reads, 32 ticket comments, 30 state updates, 5 new tickets, 3 checklist calls, 8 emails, 7 sheet, note, folder and report calls, and about 26 discovery reads: about 143. The comment reads cannot be skipped once the source shows a message is unbuilt, because Audience and the client-or-server note sit only in comments. Measured: Douglas's 17-ticket task ran 166–239. Every write has no batch form in the catalog. A run that skipped every state update would land near 115, so the pre-check's counted calls are read at intake.

**≥ 500 is not reachable without padding**, so the requester-confirmed `volume_exception` applies. Every other extreme target stands.

## 10 QC rails

### Two-reading table

| Decision point | Best reading | Strongest alternative | Resolved by | Evidence |
|---|---|---|---|---|
| Weekly Leaderboard reset | Hold: wrong day | Go: it arrives weekly | rule test 5: the day matters; the row says rollover | `harmonygames-Games/match3d#248#rc_18` |
| Lapsed 1 day | Go | Hold: not exactly 24 hours | rule: the hour doesn't matter | `f_dc45e0e5a8b8635c1b82b2` |
| Lapsed 7 days | Go with a string ticket | Hold until the line changes | rule: a line change needs a string ticket, not a Hold | `f_dc45e0e5a8b8635c1b82b2` |
| Finish first mission | Hold: cannot reach its players | Go: Vincent saw it arrive via the settings toggle | rule test 4: a player counts only once asked and the toggle doesn't count; Robert: nothing asks before level 20 in the beta build. Reach runs before the day test, so the noon-today schedule never becomes a second stopping point | `C0880U9751A/1759167608.326578` |
| Lives and lapsed reach | Go: players past the ask count | Hold: some of their players are below the ask | test 4 fails only when nobody it is written for has been asked | `f_dc45e0e5a8b8635c1b82b2` |
| The team note's reminders | the lapsed ladder the client schedules by day, and the built messages still on Hold | a total count of messages a player gets, or who hears from us overall | no count is graded, and the note never asks who hears from us: the warehouse push table answers that differently from Slack and the code, and /prompt failed rev4 on it | `harmonygames-Games/match3d#248` |
| Plague Race timing | fires daily is acceptable | Hold: not at event start | Leonard's comment on the ticket says daily is fine while a race is always on | DES-319 |
| Plague Race QA | Hold: iOS unproven | Go: passed on the ticket | Vincent's own later reply and his QA note | `D06UFE81RF0/1759174846.723833` |
| Lapsed 14 days | Drop: covered by Lapsed 7 days | Hold: nothing named day 14 is scheduled | rule: an ask the client already covers is a Drop; the batch fires on day 14 | `evt_b56d5b19baa0a573da4553` |
| Lapsed 30 days | Hold: not scheduled | Drop: covered by the batch | the batch ends on day 28 | `harmonygames-Games/match3d#248` |
| Season Pass start | Hold: nothing scheduled | Drop: not shipped | BETA list card; no ship date used (SC-38) | 6851ab766fcaf894d0c0048b |
| Comeback gift | Drop: reward on tap is not in the beta | Hold: lapsed messages exist | Leonard's comment on its ticket | `cmt_13477aa8d1468ae11c9d` |
| Unbuilt Holds | name the first test failed | either of two gaps | the rule orders the tests and stops at the first failure | `f_dc45e0e5a8b8635c1b82b2` |
| Scope of asks | tickets and cards only | Slack asks count too | hub wording; the census found no base ask on a ticket or card | `D06L58XCVKK/1759264851.763895` |
| Rate Us and permission popup | off the plan | they are messages | rule: a message reaches a closed phone | ZOM-397 |
| Win & Collect ticket | reuse | new ticket | hub: under whatever name; page maps the names | `page_liveops_calendar` |
| Hold state | Backlog | Todo | the rule doc's own exception and Leonard's later card note | `68dae8c7d95e24b55b69bf80` |
| Final headline | headline text, emoji ignored | two more string tickets for emoji | rule: emoji don't count as a different line | `f_dc45e0e5a8b8635c1b82b2` |

One reading per decision; no BOTH_FAIR_FIGURE is claimed. Each fork is settled by a dated record, never by rubric acceptance (memory: prompt-ugt-forks-need-records).

### Reach table (load-bearing records)

Proofs: `00_PreScenario/cansee_anchors.txt`. Unscoped services are always readable. Planned seeds are verified at the injection gate.

| Record | Service | Why it is load-bearing | Mark |
|---|---|---|---|
| `f_a325dd4af80afc5994d5dc` | gsheets | population | LB |
| `d_caafeec2804b3a67ce46aa` | gdrive | destination | LB |
| `D06L58XCVKK/1750138057.452159` | slack | Samuel's remit | LB |
| `D06KPMDV2JZ/1752162738.497679` | slack | ask point | LB |
| `C08R27X0EAH/1755084279.518809` | slack | ask point | LB |
| `C08R27X0EAH/1758238811.686629` | slack | context | LB |
| `C08R27X0EAH/1758239520.618939` | slack | local only | LB |
| `D06KV30TPL4/1750979856.324639` | slack | local vs server | LB |
| `C05KNDCHAAG/1757704290.799329` | slack | beta scope | LB |
| `C05KNDCHAAG/1758558164.541689` | slack | Axe Arena out | LB |
| `samuel.turner@harmonygames.co/1836006988541924555` | gmail | the PR mail thread | LB |
| `D06L58XCVKK/1759264851.763895` | slack | planned hub | LB |
| `f_dc45e0e5a8b8635c1b82b2` | gdocs | planned rule | LB |
| `D06UFE81RF0/1759174846.723833` | slack | planned QA reply | LB |
| `C08R8CHB0QL/1759169129.445834` | slack | planned line change | LB |

Feasibility: every write exists in the catalog; `gsheets_create_spreadsheet` has no folder argument, so the plan moves with `gdrive_move_file`. Samuel holds no DES team membership in the base, so the SQL adds one. Precedence: load-bearing facts sit in ● carriers (Linear comments per Ask_Carriers §6b; PR review comments; Slack; Gmail; Docs). The cancelled review's description is ○ and only supports; the source carries the fact. Naturalness: the prompt may name Leonard's DM, the PN sheet, my Drive folder and the card, and must not name the rule's tests, tickets, traps, counts or any member. Grading devices: ≤ 5 samples per group, a volume row, exception rows singled out by fragments K13, K14 and K15; exclusions graded as an exact population on the plan.

### Coherence rail

Every audit row has a disposition; each designed disagreement is a dated human claim with a later overturning record. Seeded notes report observations and decisions, never code facts beyond `harmonygames-Games/match3d#248` and the source read for this design. `tools/base_claims.py` runs before any solver work.

## 11 Record plan for /create-injection

| Service | Record | Planned content | Time |
|---|---|---|---|
| slack | `D06L58XCVKK/1759264851.763895` | Leonard's hub: Samuel, we're about to put more money behind beta and D1 and D7 are what we get judged on, so I want one straight answer on what we actually say to players. The PN sheet says six are Ready and I don't trust that. Take every row on the PNs Beta tab plus every ask for a new phone message that's been filed on a ticket or a card up to today, and make a call on each one using the message rule doc. Put it in one sheet in your Drive folder, one row per message: Message, Ticket, Call, What's missing, Audience, Final headline, String change. Next to it a one-page note for the team: start with D1 and D7 for the Sep 15 cohort week from the warehouse, iOS and Android separately, then the lapsed reminders the client schedules day by day, and anything the client already schedules that's still a Hold and why. I made tickets for the sheet rows under DES-314 and people added their asks there. Leave the call as a comment on each ticket and move the ticket to match. Anything with no ticket gets one, but don't make a second one for something that already has a ticket under whatever name. Every Go goes on a checklist on our push notifications card so Vincent can tick it off. Email each person who asked for something, apart from me, to say what happened to their asks. When it's done tell me here how many Go, Hold and Drop. | 2025-09-30T20:40:51Z |
| gdocs | `f_dc45e0e5a8b8635c1b82b2` | Beta message rule. A message is anything the game puts on a player's phone while the game is closed. Run these tests in order and stop at the first one that fails. 1. The feature behind it is in the beta. 2. The client can send it without a server. 3. The client already schedules it. 4. It can reach the players it is written for. A player only counts once our own permission ask has happened, the settings toggle doesn't count. It fails only if none of them count. 5. It fires on the right day. The hour doesn't matter for beta, the day does. 6. Vincent has seen it arrive on both iOS and Android. Go: it passes all six. Drop: it fails test 1, or the client already covers it under another message, then name that message. Hold: anything else, and name the test it failed. In the beta means live in Zombie Match today or on the BETA list of the ZM ROADMAP board. Neither status column on the sheet decides anything. What Vincent counts as seen is in his QA note. The permission ask is Robert's call. The final headline is the latest line I've called. A line that differs from what the client ships needs a string ticket under DES-314, because the strings are hard-coded, so open one when you make the call. Emoji don't count as a different line. Final headline and String change are only for Go rows. Audience is who the ask says it's for. Drop tickets go to Canceled, Go tickets stay as they are, Hold tickets go back to Todo unless the roadmap says otherwise. | 2025-09-26T17:10:54Z |
| gmail | `samuel.turner@harmonygames.co/1843335316636662321` | Vincent to Samuel, Oliver, Owen: How I'm checking the phone messages for beta. Seen only counts on a store build, on a real iOS device and a real Android device. A build with shortened timers doesn't count, it only proves the code path. Moving the phone date forward on a store build is fine. | 2025-09-15T13:05:48Z |
| github | `harmonygames-Games/match3d#248#rc_18` | inline comment on the weekly leaderboard schedule lines: This counts seven days from the day they last left the game, so it isn't tied to the rollover. Fine to merge, but it isn't a reset message until it's anchored to the real reset. | 2025-06-26T20:58:14Z |
| github | `harmonygames-Games/match3d#248#rev_7` | Arthur's COMMENTED review that carries the inline comment | 2025-06-26T20:58:14Z |
| gmail | `samuel.turner@harmonygames.co/<[SOURCE_ORG_0001]-Games/match3d/pull/248/review/2963610417@github.com>` | INT-12 mail copy of that comment to Samuel, in the base PR thread samuel.turner@harmonygames.co/1836006988541924555 | 2025-06-26T20:58:14Z |
| slack | `C0880U9751A/1759170096.924778` | Arthur, reply under Robert's post: that popup doesn't switch anything on btw. NotificationManager only schedules once our own ask has run or they switch it on from settings, on both platforms | 2025-09-29T18:21:36Z |
| gsheets | `f_8eb8c04713ff6a6ef4a265` | Vincent's Phone message checks log: one row per built message with the Android and iOS build of his pass, the same words as his ticket comments; named in his QA note | 2025-09-24T15:00:00Z |
| slack | `C0880U9751A/1759167608.326578` | Robert, root post in #zombie-match3d: Permission ask for beta: leaving our own ask after level 20, not pushing it further, Leonard's right that we need PNs for retention. The Unity popup at launch on iOS stays as it is. | 2025-09-29T17:40:08Z |
| slack | `C08R8CHB0QL/1759169129.445834` | Leonard, reply under `C08R8CHB0QL/1759159849.386619`: random one while I'm here: the 'taken over' push reads like we've given up. make it "Your Squad Needs You Back", body stays. | 2025-09-29T18:05:29Z |
| slack | `D06UFE81RF0/1759174846.723833` | Vincent, reply under `D06UFE81RF0/1759163970.141449`: also on the race one I passed: that iPhone was still on the 5-minute timers build when I ticked it, so scratch iOS. put the real 0.3.40 on it after and it never showed up. Android is fine. | 2025-09-29T19:40:46Z |
| slack | `C0880U9751A/1758909739.853209` | Brian in #zombie-match3d: honestly just send all the Ready ones at beta and fix copy after, the readiness deck says 6 anyway | 2025-09-26T18:02:19Z |
| slack | `C0880U9751A/1759245146.720608` | Vincent, root post in #zombie-match3d: on 0.3.49 the Full Ammo one didn't show up after a full refill, tried it twice on the iPhone this morning. the lapsed ones are still coming through. taking my tick off Full Ammo until I've seen it land | 2025-09-30T15:12:26Z |
| trello | `68dae8c7d95e24b55b69bf80` | Leonard's edit to the description of `68d1eb90bef538c7c5c5599d`: Until the beta build is out nothing that isn't beta work lands in anyone's Todo. Held tickets sit in Backlog, unassigned. | 2025-09-29T20:15:03Z |
| trello | `68dc20c6d5fbf6ab70025295` | Leonard renames the BETA list from BETA: Sep 30 to BETA: Oct 10 | 2025-09-30T18:26:14Z |
| trello | `6851a769c65dc0017a227bb7` | Leonard reopens the card, marked complete on Jun 30, then comments: The beta list goes on this card as a checklist. Vincent ticks these as he checks them on the store builds. | 2025-09-24T16:00:39Z |
| gcal | `evt_b56d5b19baa0a573da4553` | cancelled 'Lapsed ladder review', Leonard and Samuel: Cancelled, no need. The weekly one repeats for four weeks, so day 14 is already covered. | 2025-09-25T15:00:33Z |
| gcal | `evt_f2c03e69f50acf62c9d1c3` | 'Lapsed copy check', Leonard and Samuel, Sep 30; his note on the event: Went through the lapsed lines with Martin Walsh after this. Final for the 7 day one is "Your Squad Is Waiting", body stays. That replaces what I said in the art thread. | 2025-09-30T17:02:41Z |
| gslides | `f_de7a1ae20201816a67750d` | Beta readiness. Retention is the goal for the first cohorts. Player messages: 6 Ready on the PN sheet. | 2025-09-19T18:30:26Z |
| linear | `DES-314` | parent ticket by Leonard: One ticket per player message for beta. Rows from the PNs Beta tab, plus anything the team wants added. Add your ask as a child with who it's for in a comment. These sit in Design so the ZOM board stays on build work. | 2025-09-23T16:40:12Z |
| linear | `DES-313` | Calvin's ticket outside the parent, 'Ping when a Collect & Win window opens' | 2025-09-17T15:20:37Z |
| linear | `DES-315 to DES-345` | sheet-row tickets by Leonard on Sep 23; asks filed by each asker across Sep 24-29, no two at the same minute; six built tickets Done, the rest In Review; descriptions state the feature's state in plain words | 2025-09-23T16:40:12Z |
| linear | `DES-330 and DES-338` | relates-to links to ZOM-542 and ZOM-556 | 2025-09-26T13:27:41Z |
| linear | `DES-315` | relates-to links to ZOM-483 and ZOM-563 | 2025-09-26T16:41:28Z |
| linear | `cmt_eabac5435f2b3a575aad` | Douglas on ZOM-563: prod has the latest teams changes now. while I'm in here, could we get a phone message when a teammate sends you lives? for players on a team. it would have to go out from the server, the phone has no way of knowing. | 2025-09-30T18:22:14Z |
| linear | `cmt_e2e2926a2080ca53c4ea` | Calvin on ZOM-483: we do hand out infinite lives, just not on the first session. could we also remind players on their phone when their infinite lives are about to run out? not the lives recharged one, this is for players with infinite lives running. local timer per Arthur. | 2025-09-26T16:41:28Z |
| linear | `cmt_fd950c410ed25c447c02` | Vincent on DES-319: arrived on both on store builds, Android 0.3.127 and iOS 0.3.40 | 2025-09-24T14:02:00Z |
| linear | `cmt_9338bb2c286a6c207792` | Leonard on DES-319: Daily is fine for this one, there's always a race on. | 2025-09-24T15:10:00Z |
| linear | `cmt_f76672cf21387ec1eeab` | Vincent on DES-320: arrived on both on store builds, Android 0.3.127 and iOS 0.3.40 | 2025-09-24T14:40:00Z |
| linear | `cmt_f4960d3c073493b6bfc6` | Vincent on DES-318: arrives on both when notifications are switched on from settings | 2025-09-24T14:50:00Z |
| linear | `cmt_13477aa8d1468ae11c9d` | Leonard on DES-345: A reward on tap is a version 2 idea, it isn't in the beta. | 2025-09-26T16:00:00Z |
| linear | `cmt_f1b8a109dfa70cdc4565` | Brian on ZOM-542: while someone's in here, can we get a phone reminder once the daily Boss Arena attempts refill? separate from the weekly board ping Robert filed, this is for players who used their attempts. Arthur says a local timer is enough. | 2025-09-26T13:27:41Z |
| linear | `cmt_2b519285937e7fa79453` | Julia on ZOM-556: the gift streak itself is live, this only breaks the skip case. could we also send a phone reminder the evening before the daily gift streak resets? separate from the chest ping Calvin filed, this is for players on a gift streak. local timer per Arthur. | 2025-09-26T14:08:12Z |
| linear | `DES-314 children` | each asker's comment says who the message is for; Arthur on each unbuilt ticket: not in NotificationManager yet, and a local timer can do it or it needs a server send, on every ticket filed before his Sep 25 pass, so not on the two filed after it (Lapsed 14 days, Comeback gift); except on Lapsed 14 days, filed after his pass; Vincent on each built ticket | 2025-09-25T12:00:00Z |
| linear | `team_DES` | Samuel's membership row so he can file DES tickets | 2025-09-23T16:00:00Z |

Estimated rows: Linear 33 issues and about 65 comments, Slack 6, Gmail 4, Trello 2, GCal 2, Drive 3, Docs 1, Sheets 2, Slides 4, GitHub 1, plus companions: about 120–140 INSERTs. Every row is cohort evidence; if an honest count falls under 120, that is a finding to bring back, never a gap to pad.

### Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| github | INT-01 | Slack copy of the inline comment | exception: `harmonygames-Games/match3d#248#rc_18` predates the Jun 30 subscription of #zombie-prs |
| github | INT-12 | GitHub mail to Samuel | seeded: `samuel.turner@harmonygames.co/<[SOURCE_ORG_0001]-Games/match3d/pull/248/review/2963610417@github.com>` |
| github | INT-23 | CodeRabbit | no companion: human comment |
| linear | INT-04, INT-05 | Slack and mail notifications | no companion: base Linear comments are empty and carry none (Ask_Carriers §6b) |
| gcal | INT-11 | invitation and cancellation mails | seeded for `evt_b56d5b19baa0a573da4553` |
| gdrive | INT-13 | Drive share DMs | no companion for owner-shared files, declared at injection (`f_dc45e0e5a8b8635c1b82b2`) |
| slack | INT-22 | Slack mail digests | no companion (`D06L58XCVKK/1759264851.763895`) |
| gdocs, gsheets, gslides | none | no integration writes from these | none |
| trello | INT-21 | none exists | none |
| gmail | none | sources only | none |
| confluence, snowflake | none | not seeded | none |

## 12 Self-test results

`hardness_gate.py --design` (verbatim):

```
HARDNESS GATE (extreme (design)): PASS
  [ok] assignment_context: manifest bound to current V3 assignment, freeze and policy
  [ok] effective_profile: effective_profile 'extreme' for 'Long Horizon' → thresholds 'extreme'
  [ok] sql_lint_clean: skipped (--design: no SQL yet)
  [ok] base_consistency: skipped (--design: no SQL yet)
  [ok] services_injected: skipped (--design: no SQL yet)
  [ok] rows: skipped (--design: no SQL yet)
  [ok] services_carrying_weight: 12 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: skipped (--design: no SQL yet)
  [ok] seeded_ids_exist_in_sql: skipped (--design: no SQL yet)
  [ok] anchors: 3 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 21 fragments; need ≥ 12
  [ok] ask_fragment_services: 11 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 21 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 9 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 43; need ≥ 40 (source-defined: True)
  [ok] evidence_surfaces: 4 surfaces over 4 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 77; need ≥ 75
  [ok] call_budget: unconditional (verified) floor 202 of 202 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 200 (requester-confirmed volume_exception)
  [ok] call_budget_spread: 12 services in budget; largest share outside the per-record phase 19% (≤ 50%)
  [ok] traps: 16 traps across 7 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 6 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 5 supersessions (4 with versions in ≥ 2 services, 4 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: skipped (--design: no SQL yet)
  [ok] distractors: 6 distractors of 6 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 10 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 9 chains with 8 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] mechanism_portfolio: 9 portfolio entries, each a mechanism-enum id with trap/chain nodes, a requirement, a natural-reading fallback and a prior family with its reason
  [ok] artifact_fields: declared ['gradable_surface']: paths relative, digests sha256
  [ok] hidden_authorities: 3 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 2 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 12 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 9 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 9 writes over 7 services; each must depend on findings
  [note] volume_exception: call-budget floor 200 and per-record floor 75 replace 500 and 300; every other extreme target applies — reason: 36 real messages; mail, channels and sheets are bulk-readable, so honest necessa; requester confirmation: task author in chat on 2026-11-04 set the horizon target at 'over 130 tool calls
```

`gradable_surface.py validate` and `gradeable-report` (verbatim):

```
GRADABLE SURFACE (01_Gradable_Surface.json): PASS · 57 slots · weight 227 · mechanism share 79.7% (reported, not gated) · weight by class {'direct': 75, 'write_content': 147, 'delivery': 5}
SURFACE.GRADEABLE PASS · 57 slot(s) · {'GRADABLE': 57}
```

Lazy-solver pass: one broad search per service, first hits, no threads, no comments. It reads the sheet, the parent's children and the hub, so it scores some always-pass rows and none of the eight channels (`plan/policy_scores_output.txt`). Leaks fixed in design: the rule doc holds only tests, no member; the hub names no ticket but the parent; ticket titles carry no alias.

Literal-value and wording sweep (`plan/literal_sweep.txt`, verbatim):

```
Slack, Apr-Sep 2025 (substring match, through hg.py search-many):
pos_control_rate_us: 3 hits, complete False | C05433XK267: 'en>)\nMatch3D Android - #1289 - Samuel/ZOM-397 Changes:\n- Lev'; C05433XK267: 'en>)\nMatch3D Android - #1289 - Samuel/ZOM-397 Changes:\n- Lev'
taken_over: 2 hits, complete True | C07C2866011: '\u200eSurvive the Outbreak in the Ultimate Zombie Match 3D Challe'; C096HFA5Z8W: '\u200eSurvive the Outbreak in the Ultimate Zombie Match 3D Challe'
race_one: 1 hits, complete True | CD5C9E6CC238: 'do you want me to write a doc for quests just like the leade'
five_minute: 3 hits, complete True | C0880U9751A: 'Those 5-minute timers are just for testing purposes; the one'; C0880U9751A: 'Those 5-minute timers are just for testing purposes; the one'
needs_you_back: 0 hits, complete True | no hits
held_work: 0 hits, complete True | no hits
phone_reminder: 0 hits, complete True | no hits
shortened_timers: 0 hits, complete True | no hits
test_build: 6 hits, complete False | C05433XK267: 'tplinkdns.com:9009/job/Match%203D%20iOS%20Submission/311/dis'; C05433XK267: 'tplinkdns.com:9009/job/Match%203D%20iOS%20Submission/311/dis'
DES-313..346 free: True; positive control DES-312 present: True
ZOM ask census: 1 regex hit (ZOM-295, a monster 'push back' effect, not a message ask); Trello ZM ROADMAP cards mentioning notifications: 6851a713aa4e4da6cb2c2227 (a bug list), 6851a769c65dc0017a227bb7 (the PN card)
```

"The rest stands" check: the freeze note amends one clause; no later record restates Todo. Leonard's reply changes one line and his calendar note changes that line again, and says so; the body stays.

S9b prior forecast (UNCALIBRATED, CONDITIONAL on disclosed rates): ledger id `hev_19ece0d92e1274f2`.

```
  V3: P(all four difficulty gates) 0.384-0.539 across scenarios; value of information (first scenario): ['rule:DONE', 'rule:CORR', 'rule:DEP']
  correlated  whole    V3 E[avg] 0.678 [0.546, 0.834] P(all) 0.384
  independent whole    V3 E[avg] 0.669 [0.607, 0.734] P(all) 0.539
  source      whole    V3 E[avg] 0.669 [0.607, 0.734] P(all) 0.539
```

These use the assigned Medium cap, not the requester's 80 % bar (`plan/policy_scores_output.txt` carries that view). Rates now start from the rev5 pre-check, which beat the earlier forecast by more than its band, so treat them as weak.

### Self-review

Walked against `Evals/1_Prompt_Eval.md` §2.1, §2.2, §3.2 and `Evals/0_Injection_Quality_Eval.md` Check C.

| Category or decision | Counter-reading (it should fail) | Resolution with evidence |
|---|---|---|
| temporal | seeded tickets numbered after a May series look back-dated | DES stopped at DES-312 on 2025-05-07, so DES-313 onward from Sep 17 are in order; ZOM-566 from Sep 30 would not be |
| semantic | the job reads as a release sign-off, so Engineering Ops or Product Management | the job is what players hear and when, to move D1 and D7: a comms plan, a team note opening on retention, an email to each asker; tickets are follow-through (`6851a769c65dc0017a227bb7`, `wh_USER_COHORT_RETENTION`) |
| cross-service referential | the rule says Vincent's QA note but the ticket and note could disagree | they differ by design and the later record wins: `D06UFE81RF0/1759174846.723833` |
| quantitative | Go 2 could be argued as 3 or 4 if a run counts Lives recharged or Plague Race | Vincent withdraws iOS on one (`D06UFE81RF0/1759174846.723833`) and his tick on the other (`C0880U9751A/1759245146.720608`); the count is the rule applied to 36 rows |
| state/lifecycle | a Done ticket moved to Backlog looks odd | the rule doc makes state follow the call (`f_dc45e0e5a8b8635c1b82b2`); agent writes come after the clock |
| identifier/format | seeded review comment rc_18 could collide | PR 248 holds rc_1 to rc_17 (`harmonygames-Games/match3d#248`), checked through hg.py |
| other | the theme screen names zombies | 12 stored runs show no fallback; seeds avoid the words (`f_a325dd4af80afc5994d5dc`) |
| Weekly Leaderboard reset | Go: it arrives weekly | rule test 5: the day matters; the row says rollover (`harmonygames-Games/match3d#248#rc_18`) |
| Lapsed 1 day | Hold: not exactly 24 hours | rule: the hour doesn't matter (`f_dc45e0e5a8b8635c1b82b2`) |
| Lapsed 7 days | Hold until the line changes | rule: a line change needs a string ticket, not a Hold (`f_dc45e0e5a8b8635c1b82b2`) |
| Finish first mission | Go: Vincent saw it arrive via the settings toggle | rule test 4: a player counts only once asked and the toggle doesn't count; Robert: nothing asks before level 20 in the beta build. Reach runs before the day test, so the noon-today schedule never becomes a second stopping point (`C0880U9751A/1759167608.326578`) |
| Lives and lapsed reach | Hold: some of their players are below the ask | test 4 fails only when nobody it is written for has been asked (`f_dc45e0e5a8b8635c1b82b2`) |
| The team note's reminders | a total count of messages a player gets, or who hears from us overall | no count is graded, and the note never asks who hears from us: the warehouse push table answers that differently from Slack and the code, and /prompt failed rev4 on it (`harmonygames-Games/match3d#248`) |
| Plague Race timing | Hold: not at event start | Leonard's comment on the ticket says daily is fine while a race is always on (DES-319) |
| Plague Race QA | Go: passed on the ticket | Vincent's own later reply and his QA note (`D06UFE81RF0/1759174846.723833`) |
| Lapsed 14 days | Hold: nothing named day 14 is scheduled | rule: an ask the client already covers is a Drop; the batch fires on day 14 (`evt_b56d5b19baa0a573da4553`) |
| Lapsed 30 days | Drop: covered by the batch | the batch ends on day 28 (`harmonygames-Games/match3d#248`) |
| Season Pass start | Drop: not shipped | BETA list card; no ship date used (SC-38) (6851ab766fcaf894d0c0048b) |
| Comeback gift | Hold: lapsed messages exist | Leonard's comment on its ticket (`cmt_13477aa8d1468ae11c9d`) |
| Unbuilt Holds | either of two gaps | the rule orders the tests and stops at the first failure (`f_dc45e0e5a8b8635c1b82b2`) |
| Scope of asks | Slack asks count too | hub wording; the census found no base ask on a ticket or card (`D06L58XCVKK/1759264851.763895`) |
| Rate Us and permission popup | they are messages | rule: a message reaches a closed phone (ZOM-397) |
| Win & Collect ticket | new ticket | hub: under whatever name; page maps the names (`page_liveops_calendar`) |
| Hold state | Todo | the rule doc's own exception and Leonard's later card note (`68dae8c7d95e24b55b69bf80`) |
| Final headline | two more string tickets for emoji | rule: emoji don't count as a different line (`f_dc45e0e5a8b8635c1b82b2`) |

Base values re-read through `tools/hg.py` this session: the sheet tabs, PR 248 reviews and hunks, the Trello lists and card, the DMs and posts cited above.

HARDNESS GATE (extreme (design)): PASS

Unresolved: the dual red team did not run (`REDTEAM_*` unset, §13); the fresh-context reviewer has not re-read the final B5 fix; both blind sweeps run before `/injection`; the INSERT count is an estimate; STEP 0.6 cannot be measured locally; landing rates are UNCALIBRATED; competency is defensible, not certain (§13); `linear_show_data` and the `query` scope of `linear_list_issues` are unverified, and if either exposes comments FILT leaks; seeded relations must be seen rendering in the pre-check.

```
STAGE GATE scenario: PASS — Task_Authoring/task_inputsK · 01_Scenario_Design.md#a477a8d3015e · 01_Hardness_Manifest.draft.json#ed860637b593 · 01_Gradable_Surface.json#095a6e4fc9df · 00_Assigments.md#55f6d8057880 · __context__#72168f70a409 · __assignment__#3adec6ac02d7 · __policy__#dc4ab5df3cdd · __gate_policy__#115714063000 · __review__#8ac0cdb4d008 · blocking 0 · warnings 0 · checks 36
[PASS] assignment.v3_context: Samuel Turner / Game Designer; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 3 output(s) present: 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json
[PASS] structure.inputs: 1 input(s) present: 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md)
[PASS] structure.sections: 19 required sections present and non-empty (01_Scenario_Design.md)
[PASS] structure.placeholders: no placeholders in 01_Scenario_Design.md
[PASS] evidence.storyline: 6/6 items carry a source pointer (min 80%)
[PASS] evidence.coherence_audit: 24/24 items carry a source pointer (min 100%)
[PASS] evidence.hidden_authorities: 3/3 items carry a source pointer (min 100%)
[PASS] evidence.delegation: 24/24 items carry a source pointer (min 90%)
[PASS] evidence.trap_register: 49/51 items carry a source pointer (min 90%); unsourced e.g. L440: 'QUIET | quiet-hours rule on midnight sends | every midnight message | older mail | authori'
[PASS] evidence.record_plan: 43/46 items carry a source pointer (min 80%); unsourced e.g. L732: 'gdocs, gsheets, gslides | none | no integration writes from these | none'
[PASS] evidence.active_speakers: 10/10 items carry a source pointer (min 100%)
[PASS] tool.hardness_gate_design: hardness_gate --design pasted PASS; re-run PASS
[PASS] tool.persona_reach: persona_view reach pasted for samuel.turner@harmonygames.co and matches the re-run (84 channels)
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] kb.coherence_hazards: coherence audit cites 13 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 10 speaker rows carry their activity.json status_at_clock
[PASS] kb.integrations: companions listed per integrations.json (9 INT ids, services ['confluence', 'gcal', 'gdocs', 'gdrive', 'github', 'gmail', 'gsheets', 'gslides', 'linear', 'slack', 'snowflake', 'trello'])
[PASS] kb.storyline: timeline cited; cohorts []; trap_catalog ['C01', 'C02', 'D05', 'K02', 'N01']
[PASS] boundary.anchor_naming: 6 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] tool.redteam_dual: red team did not run (missing 01b_Redteam_Review.md, 01b_Redteam_Review.second.md); explicit fallback recorded: a fresh-context Claude agent with none of this session's reasoning reviewed the design on 
[PASS] surface.valid: 57 slots, weight 227; geometry report-only, never gated: mechanism share 80%, always-pass share 20%
[PASS] forecast.preregistered: prior forecast pre-registered in the ledger: ['hev_19ece0d92e1274f2'] (UNCALIBRATED, advisory)
[PASS] revise.intake: revision intake consumes run_forensics/rev5/precheck.node_verdicts.json
[PASS] revise.verdict_dispositions: 8 proposed node verdict(s) dispositioned; 1 CONFOUNDED candidate(s) addressed
[PASS] revise.revision_binding: every export is bound on evidence to the revision it ran on, or marked historical (historical evidence never certifies a revision)
[PASS] evidence.register_run_step: 8/8 items carry a source pointer (min 100%)
[PASS] reach.scenario: 15 scoped load-bearing ids YES for samuel_turner (4 planned seeds not yet in base: verified at the injection gate)
[PASS] review.counter_readings: 25 evidenced counter-readings (of 25 found; need ≥ 25) in 01_Scenario_Design.md
[PASS] review.coverage: self-review addresses all 8 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.draft.json is bound to the current assignment, policy, source context and freeze
[PASS] v3.role_review: current role-plausibility review recorded; semantic judgment belongs to the named reviewer
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## 13 Red team (dual)

RED TEAM UNAVAILABLE: redteam_review: set REDTEAM_MODEL or pass --model (REDTEAM_* is unset in this environment).

RED TEAM FALLBACK: a fresh-context Claude agent with none of this session's reasoning reviewed the design on 2026-11-04 as the platform's strict reviewer: it read the design, the builder, Evals/1_Prompt_Eval.md and the known-issue cards, and checked the planned seeds against the universe through tools/hg.py and tools/persona_view.py plus NotificationManager.cs. Report: plan/redteam_independent.md. It is one reviewer from the same model family, not the two-family review the gate intends, so this stays in Unresolved until the blind sweeps or the pre-check cover it. The requester delegated this choice on 2026-11-04.

Verdict on the first draft: FAIL, four blocking findings. The same agent then re-checked the revision and found B1 to B4 closed and one new blocker, B5. Every finding and what was done:

| Finding | Source | Disposition | Evidence |
|---|---|---|---|
| B1 the two off-parent asks cannot be found by any fair route | plan/redteam_independent.md | fixed: each child ticket carries a relates-to link to the ticket that holds the ask, and linear_list_issues returns relations (Ask_Carriers §6b) | T6, C6, ZOM-542, ZOM-556 |
| B2 "can reach" unsettled for the first-session message, and Lives and lapsed passed on a different standard | plan/redteam_independent.md | fixed: the reach test now says a player counts only once the ask has happened and the settings toggle doesn't count; Robert's post is scoped to the beta build | T3, C0880U9751A/1758216118.113509 |
| B3 Lapsed 14 days contradicts the code, because the weekly batch fires on days 7, 14, 21 and 28 | plan/redteam_independent.md | fixed and turned into the design's work-already-done trap: Drop, covered by Lapsed 7 days; Lapsed 30 days added as the control past the batch | T7, harmonygames-Games/match3d#248 |
| B4 two Drop values rest on no record | plan/redteam_independent.md | fixed: Comeback gift has a planned Leonard comment; Pop-up offer live removed because ZOM-225 leaves its state unclear | T7, ZOM-225 |
| N1 the job reads as a release sign-off, which is Engineering Ops | plan/redteam_independent.md | changed the job: framed on D1 and D7, a team note on what a lapsed player hears with a warehouse baseline, an Audience column, and an email to each asker | wh_USER_COHORT_RETENTION |
| N2 most traps leak one hop past the four sources | plan/redteam_independent.md | title aliases removed, the correction now quotes the old line's words, the QA reply avoids the note's keywords; design rates lowered to a 0.42 mean | T2, T4 |
| N3 the old-name trap defeats itself | plan/redteam_independent.md | dropped as a trap and kept as a control; BUILT now rests on the day-14 join | T7 |
| N4 the planned QA builds clash with #builds | plan/redteam_independent.md | fixed: comments cite store versions Android 0.3.127 and iOS 0.3.40 and give no iPhone build on the race ticket | C0880U9751A/1758643365.607149 |
| N5 comment reads could be skipped, dropping the lean run under 130 | plan/redteam_independent.md | fixed: Audience and the client-or-server note exist only in comments, and both are plan values | T4, surface linear_list_comments |
| N6 asks looked generated, and gcal and gslides existed for service count | plan/redteam_independent.md | six one-to-one Backlog asks removed; gcal now carries the completion note; the deck stays a stale summary | T7, T10 |
| N7 "name the one thing missing" had no order | plan/redteam_independent.md | fixed: the rule's tests are numbered and stop at the first failure, and test 2 makes server sends a rule test | K2 |
| N8 emoji fork settled only by the grader | plan/redteam_independent.md | fixed: the rule says emoji don't count as a different line | K2 |
| N9 live today has no single authority | plan/redteam_independent.md | accepted: ticket descriptions state the feature's state in plain words; those members converge on Hold either way | K7 |
| N10 housekeeping | plan/redteam_independent.md | Robert's Sep 18 post is now answered by his seeded post; hub wording and ticket times fixed; stale counts regenerate from the builder | C0880U9751A/1758215775.137159 |
| B5 "five messages over 28 days" is not one value: it depends on level, lives and the ask | plan/redteam_independent.md, Delta review | fixed: no total is graded. The note now gives the lapsed ladder by day and says who hears nothing, which is also the retention finding. Self-verified against the source: days 1, 7, 14, 21, 28; NotificationsEnabled stays false before the ask. The reviewer has not re-read this fix | harmonygames-Games/match3d#248, X17, X20 |
| N11 Leonard's daily-is-fine comment had no planned wording | plan/redteam_independent.md, Delta review | fixed: wording added to the builder and the record plan | T4 |
| N12 the first-session message could stop at the day test | plan/redteam_independent.md, Delta review | fixed: the reach test now runs before the day test, so it has one stopping point | K2, T3 |
| N13 a delegation quote no longer matched the hub | plan/redteam_independent.md, Delta review | fixed: fragment K4 quotes the current wording | K4 |
| N14 three state rows required Backlog, making FOLLOW the largest choke | plan/redteam_independent.md, Delta review | fixed: those rows accept Backlog or Todo and now test only that the ticket left Done | X1c, X6c, X8c |
| N15 the cohort floor of 40 is met only by counting ruled-out records | plan/redteam_independent.md, Delta review | accepted and disclosed: 42 looked at, 35 in scope, the same reading frederick_q4 used | T14, T15 |
| N16 baseline rows checked D1 only | plan/redteam_independent.md, Delta review | fixed: both regexes now need D1 and D7 | K16, K17 |
| Competency after the revision: defensible, not yet clearly Marketing and GTM | plan/redteam_independent.md, Delta review | improved by making the reach gap the note's graded core at weight 5; most writes stay on Linear because they carry the horizon, so this stays an open risk for /prompt | X20 |
| B1 depended on relations being visible | plan/redteam_independent.md, Delta review | checked: stored Douglas runs show a relations object in Linear tool output; seeded rows must still be seen rendering in the pre-check | ZOM-542 |

## 14 Revision intake (S0r)

Verdicts file consumed: `run_forensics/rev5/precheck.node_verdicts.json` (node_verdicts.py on the rev5 pre-check; dispositioned records `run_forensics/rev5/precheck.dispositioned.jsonl`). The export is bound on discriminating content to rev5 and stays bound to it; it certifies nothing about rev6. Report: `01a_Hardening_Report.md` (MODE B, gate PASS). Platform: /hardness FAIL 2 (188 calls, about 90%, one cause), /prompt NON-FAIL 3 (Coherence, SC-13), /injection PASS.

| Node | Runs | Proposed verdict | Disposition | Evidence |
|---|---|---|---|---|
| FILT | 1 | BYPASSED | keep, confirmed LANDED: the rows are absent because the run never read a comment on a ZOM ticket; two more asks move outside the filter so this miss alone passes the 15% line | opus · event 137 and opus · event 335 |
| DONE | 1 | LEAKED | keep: an honest decision that no longer counts as difficulty, because the source settles it | opus · event 165 |
| CORR | 1 | LEAKED | rebuild: the Sep 29 reply stays as the answer a search finds, and a later calendar note replaces it. CONFOUNDED rejected: the pending Lapsed 7 days error is decoder strictness on a String change cell | opus · event 226 and opus · event 231 |
| DEP | 1 | BYPASSED | keep: confirmed LEAKED, the row was only named differently; the source shows the join, so rewording Robert's post would change nothing | opus · event 161 and opus · event 166 |
| QA | 1 | LEAKED | rebuild: the visible iPhone caveat goes and the reply drops the store build wording | opus · event 202 and opus · event 207 |
| ALIAS | 1 | BYPASSED | keep: confirmed LEAKED, the row was only named differently | opus · event 142 |
| BUILT | 1 | LEAKED | keep: an honest decision, settled by the source | opus · event 165 |
| FOLLOW | 1 | LEAKED | rebuild: the rule moves from a comment to the card's description, and the doc's clause stays because /prompt's authority chain needs it | opus · event 113 |

New node: PULL, Vincent's channel post takes his pass off Lives recharged. Truth moves to Go 2, Hold 28, Drop 6 over 36 messages, 8 askers and 5 new tickets. One Trello updateList action settles SC-13 (`run_forensics/rev5/prompt_report_NONFAIL_3.md`, Recommended Improvement 1). Prompt and Leonard's DM are unchanged. Every choice here was made under the requester's delegation: "you can choose from your self which option is best fit for my requirements in this task".

Blind sweep of rev6 (`plan/sweep_fork_rev6.md`): the reviewer reached the same calls with no sight of this design. F1 FATAL taken: Snowflake AD_IMPRESSION_EVENTS can answer test 1 for the rewarded ask, and Snowflake cannot be injected, so that ask is removed. F2 taken: Douglas's comment moved after his Sep 30 prod update. F3, F4 and F14 taken: Vincent's race tick is now his first of the day, the infinite lives ask follows Arthur's pass, and the board's last activity follows the rename. F5 taken for the new asks only, because the older lines scored 5 on Contrived at /prompt. F6 and F7 left: the platform reviewed both on rev5 and scored them clean, and fixing F6 would change the prompt.

Routing: the surface key matcher fix stays open (`01a_Hardening_Report.md` §6): a run's row name that differs from the truth key still fails locally, so read local grades with that in mind. No verifier or OE finding exists yet.

