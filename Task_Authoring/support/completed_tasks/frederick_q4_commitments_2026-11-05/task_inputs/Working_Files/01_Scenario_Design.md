# Scenario Design — frederick_q4_commitments · design only · contains no prompt, OE or criterion text

Written 2026-11-03 by `/create-scenario` (Claude Opus 5.5); revised 2026-11-04 by `/create-scenario --revise` (design-2, after the rev3 Opus pre-check: §14). Builders: `Working_Files/plan/build_scenario.py` (manifest, surface, ids), `plan/assemble_design.py` (this file), `plan/policy_scores.py` (UNCALIBRATED scores). Learnings applied: `Working_Files/00_Completed_Task_Learnings.md` (the three completed Frederick tasks) and `00_Pre_Scenario_Analysis.md`.

## 0 Assignment, persona census and horizon note

| Field | Value |
|---|---|
| Universe | key `synthcut`, label Oct 1, 2025 (synth-cut), `Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)`; seed bound `freeze_utc` 2025-10-01T00:00:00Z (Tue Sep 30 17:00 PT); `shutdown_rules_apply` false |
| Assignment | Executive · Frederick Stone (Co-founder, `frederick.stone@harmonygames.co`) · Corporate Ops · Actions · long-horizon · easy · October 1, 2025 07:00 (context_hash `db8af19cc1c3`) |
| Evals category | Founders / Exec / Strategy (`Evals/references/rules/task_categories.md`: strategic decisions, priorities and executive coordination) inside Corporate Ops (vendor, legal/contracts) |
| Loss budget | Easy cap < 90 %; requester target < 80 % (author_targets in the draft manifest); design target E[avg] ≤ 72 % |
| Horizon | Long Horizon → `effective_profile: extreme`; requester target > 130 counted calls in every run; `volume_exception {call_budget_floor 200, per_record_floor 90}` (honest budget 237, lean correct run ≈ 150) |
| Theme screen | no bio-adjacent theme in the storyline or seeded text (vendors, partners, contracts) |
| Role remit | Frederick is a co-founder (roster) and the Commercial Lead who owns the external vendor and partner portfolio (persona brief; Contacts `175c0d7bc72ed244b944cb90` 'Commercial Lead, Marketing & Business Development'). Leonard is in LA on Oct 1 for the Dentsu meeting (`C07C2866011/1758739727.864319`) and hands him the vendor/partner side under the founders' Sep 15 and Sep 24 runway decisions (`C07C2866011/1757961037.465799`, `C07C2866011/1758739409.488879`) |

Persona reach census (`persona_view.py reach frederick_stone --top 10`, verbatim):

```
REACH  Frederick Stone <frederick.stone@harmonygames.co>  Co-founder / Executive
clock 2025-10-01

SLACK  user=EMPLOYEE_0008_SLACK_ID  visible channels=105 {'public': 12, 'private': 34, 'mpim': 17, 'im': 42}  messages=160793  public-not-member (UNVERIFIED)=55
  persona posts=4780 last post=2025-09-30  last activity in visible channels=2025-10-01
  C05H8KVNU67    game-design                            private mem=27  msgs=22750  2023-07-16..2025-08-28 archived
  C07C2866011    executives                             private mem=9   msgs=21836  2024-07-11..2025-10-01
  C050WGU41HR    engineering-bots                       private mem=35  msgs=19854  2023-03-29..2025-09-19
  C05V5FNLB9V    god-bugs                               private mem=31  msgs=16695  2023-10-07..2025-07-15
  C0880U9751A    zombie-match3d                         private mem=25  msgs=16250  2025-01-09..2025-09-30
  C04UM32UWKD    investors                              private mem=8   msgs=6581   2023-03-18..2024-10-17
  C0553V44CE4    god-ui-ux                              private mem=30  msgs=5008   2023-04-21..2025-05-29 archived
  C04S28HSD0U    product                                private mem=21  msgs=4365   2023-03-02..2024-05-11 archived
  C069FF9Q57S    analytics                              private mem=28  msgs=4276   2023-12-05..2025-09-19
  D05S58U4SAK    D05S58U4SAK                            im      mem=5   msgs=4233   2023-09-15..2025-09-29

GMAIL  mailbox=frederick.stone@harmonygames.co threads=4656 messages=5474 range=2024-06-25..2025-10-01
  threads by last-message month (recent): {'2025-05': 323, '2025-06': 333, '2025-07': 249, '2025-08': 108, '2025-09': 185, '2025-10': 3}
  top correspondents: SVC_0107_EMAIL (1870), SVC_4131_EMAIL (1476), leonard.hayes@harmonygames.co (528), robert@harmonygames.co (337), arthur.blake@harmonygames.co (266), SVC_0521_EMAIL (192), brian.foster@harmonygames.co (102), SVC_0009_EMAIL (91), PERSON_5681_EMAIL (76), PERSON_1294_EMAIL (75)

GCAL  own=['frederick.stone@harmonygames.co'] shared=[] events=316 (distinct ical_uid 148, cancelled 27)
  last event before clock=2025-09-30T17:30:00Z  next after clock=2025-10-01T20:30:00Z
  by month: 2023-10:1 2024-07:1 2024-08:1 2024-09:65 2024-10:28 2024-11:27 2024-12:25 2025-01:28 2025-02:15 2025-03:7 2025-04:17 2025-05:25 2025-06:23 2025-07:22 2025-08:5 2025-09:22 2025-10:3 2026-01:1

DRIVE  owned=46 {'application/pdf': 12, 'application/vnd.google-apps.presentation': 12, 'application/vnd.google-apps.document': 8, 'application/json': 4, 'application/vnd.google-apps.spreadsheet': 4, 'folder': 2, 'text/plain': 2, 'text/csv': 2}
  shared-with=189 {'application/vnd.google-apps.document': 63, 'application/vnd.google-apps.spreadsheet': 31, 'text/plain': 28, 'application/vnd.google-apps.presentation': 23, 'application/json': 21, 'application/pdf': 21, 'text/csv': 2}
  shared by owner: {'Resource: -6481757892984311338': 100, 'Resource: 7240535625619857401': 40, 'leonard.hayes@harmonygames.co': 39, 'robert@harmonygames.co': 5, 'arthur.blake@harmonygames.co': 3, 'julia.lawson@harmonygames.co': 2}
  native visible: {'gdocs': 71, 'gsheets': 35, 'gslides': 35}  last modified visible=2025-09-30T17:50:11Z
  UNVERIFIED (domain/anyone, not owned/shared)=91 {'application/vnd.google-apps.document': 35, 'application/vnd.google-apps.spreadsheet': 33, 'application/json': 11, 'application/pdf': 8, 'application/vnd.google-apps.presentation': 4}

UNSCOPED (always visible): contacts, github, trello, linear, snowflake, confluence

LAST ACTIVITY (days before clock): slack_persona_post=2025-09-30 (1d), slack_visible_channels=2025-10-01 (0d), gmail=2025-10-01 (0d), gcal_last_event_before_clock=2025-09-30 (1d), drive_last_modified_visible=2025-09-30 (1d)
```

Identities (`entity.py resolve "Frederick Stone"`): Linear `usr_175c0d7bc72ed244`, Trello `4b4a68fc0fec0b254e4f9d8e`, Confluence `user_EMPLOYEE_0008`, Drive root `d_175c0d7bc72ed244b944cb` (owned). GitHub login shows 'Ryan' (S04): GitHub carries no row.

## 1 Storyline

Before flying to LA, Leonard hands Frederick everything outside the investor work that is waiting on Harmony Games: offers, trials, quotes, terms and partner asks that one of the founders engaged with. Frederick applies the founders' runway guardrails to each (Answered / End / Keep / Sign / Park), answers each company, routes signatures to Leonard or Arthur and counsel, sets revisit reminders, files contacts, logs it in his Q4 commitments folder and reports what stays and what waits on a signature. 46 companies are looked at; 36 pass the scope rule.

- Timeline (`references/universe_kb/by_universe/synthcut/timeline.md`): the window sits after the Sep 3 bridge launch (`C07C2866011:1756749288.785249`) and inside the founders' late-September runway discussion (`C07C2866011/1758739409.488879`). Synth-cut, no shutdown premise: the company operates normally and only freezes new cash commitments.
- cohorts.json: no fit — every KB cohort is a Linear issue set (LIN-*), and this cohort is outside companies with offers in mail, papers and calls (defined by the hub `frederick.stone@harmonygames.co/1844732913254784171`).
- trap_catalog precedents: C01 (thread replies that correct: Framewell `C07C2866011/1758920520.674991`), B02 (automated senders: Clipforge's processor notice `frederick.stone@harmonygames.co/1843067564852153540`), D04 (spreadsheets with lookalike titles: the template `f_05f0a451b29b19a1c0b90f` vs the July tracker `f_9d6edd4922d8130ccd272e`), P01 (shared first names: no seeded external person shares an HG first name, entity output §1c).
- Base anchors Frederick can see: Balancy `frederick.stone@harmonygames.co/1840501641217286806`, Nintendo `frederick.stone@harmonygames.co/1842359398719557772` and `frederick.stone@harmonygames.co/1842358947604469113`, his Switch post `C07C2866011/1757011358.730529`, the Playtestcloud root `C07C2866011/1758513190.847889`, the ESG engagement `frederick.stone@harmonygames.co/1841636073974841484`, founders' board `688c4fa78031638f0804a994` (card on board `640643a3fd8f3ca308d9318e`).
- Boundary anchors (excluded by the hub's rule): Rayking `frederick.stone@harmonygames.co/1842348778705877030` (Frederick's Sep 4 reply went to Leonard), Playable Factory `frederick.stone@harmonygames.co/1843000993076735547`, Gamesforum `frederick.stone@harmonygames.co/1842890197572292911`, InterCo `frederick.stone@harmonygames.co/1841620870486605150`, Google partner `frederick.stone@harmonygames.co/1817715521687421486`, Singular `frederick.stone@harmonygames.co/1837914783244638008` (SC-39), NCsoft `frederick.stone@harmonygames.co/1842898562278009736`, Dentsu `frederick.stone@harmonygames.co/1843473831194478743`, Mattel `C07C2866011/1756832039.396149`.
- Natively spans gmail, slack, gcal, gdrive, gdocs, gsheets, trello, contacts (8: e.g. `frederick.stone@harmonygames.co/1840501641217286806`, `C07C2866011`); injection adds linear (ZOM-567) and gslides (`f_5dbbaf5b251d5261427eb1`) with load-bearing roles (10 injected, all used; Confluence never carries a fact, learnings §26).

## 1a Coherence audit

Scope = every record a correct run opens. Walked against `references/universe_kb/by_universe/synthcut/coherence_hazards.json` and the known-data-issue cards `references/known_data_issues/synthcut.md`.

| Record | Category | Fields | Pointer | Hazard / card | Disposition |
|---|---|---|---|---|---|
| Balancy thread message order | temporal | message dates | frederick.stone@harmonygames.co/1840501641217286806 | hazard T02 | fold: no seed appended; the agent reads dates, not order |
| seeded threads' date format | identifier/format | date header | frederick.stone@harmonygames.co/1843618067251203081 | hazard I04 | fold: seeded Gmail rows use the RFC-2822 form of their mailbox's neighbours |
| Frederick's GitHub display name | semantic | name | frederick.stone@harmonygames.co/1842359398719557772 | hazard S04 | avoid: GitHub carries no row |
| seeded calendar events with invitation mails | cross-service referential | summary ±1 day | evt_fd469c29811879519c2c96 | hazard R08 | fold: each seeded event gets its INT-11 invitation mail in every attendee mailbox |
| Slack links to Docs | cross-service referential | doc ids in links | C07C2866011/1759166100.370044 | hazard R04 | avoid: seeded Slack names documents by title, never by link |
| Playtestcloud root reply counters | quantitative | reply_count / latest_reply | C07C2866011/1758513190.847889 | hazard Q01 | fold: SQL updates the root's counters for Leonard's reply (manifest hazard_acknowledgements Q01, dated_claim) |
| DM localization root reply counters (rev4) | quantitative | reply_count / latest_reply | D05S58U4SAK/1758151772.570449 | hazard Q01 | fold: SQL updates the Sep 17 DM root's counters for Leonard's Sep 29 thread reply (second Q01 acknowledgement) |
| Spotlight call description (rev4) | cross-service referential | description | evt_564a16d0f5f6598d0360d5 | none (○ carrier) | fold: the description no longer states the answer; Robert's ● note carries it alone, so the two cannot disagree |
| Hootline thread without a filed paper (rev4) | cross-service referential | attachments / paper | frederick.stone@harmonygames.co/1839631800730308867 | none | fold: the terms are in the mail body, and no message says 'attached', so no missing-attachment claim exists |
| ESG note copies in four mailboxes | quantitative | body | frederick.stone@harmonygames.co/1844177063117059830 | hazard Q10 | fold: one identical body per mailbox copy |
| ZOM-567 assignee at the clock | state/lifecycle | assignee | ZOM-567 | hazard L08 | avoid: ZOM-567 has no assignee (creator Arthur), so no open issue sits on a person quiet after the clock |
| keep-running card list | state/lifecycle | list / checklist | 689b662c60cbe40b9f4a97ae | hazard L12 | avoid: the card sits in Doing with open checklist items, never in Done |
| Frederick's mailbox file alias | identifier/format | file name | frederick@harmonygames.co_1842348778705877030.json | hazard I03 | fold: seeded threads follow the frederick@ file alias with frederick.stone@ ids |
| Singular payment plan | quantitative | plan terms | frederick.stone@harmonygames.co/1837914783244638008 | card SC-39 | excluded: the hub keeps Singular off the log; no row grades its plan |
| Frederick's founder status | semantic | role | Contacts 175c0d7bc72ed244b944cb90 | card SC-49 | excluded: no row grades founder status |
| channel membership | state/lifecycle | members | C07C2866011 | card SC-7 | excluded: no row grades who is in a channel |
| Frederick's pay | quantitative | ledger | snowflake.FINANCE_LEDGER | card SC-54 | excluded: no money row reads payroll |
| Rayking 'reply' addressed to Leonard | other | To header | frederick.stone@harmonygames.co/1842348778705877030 | none (base quirk) | designed boundary: the hub's 'only forwarded around internally' clause settles it (T18) |
| Mattel RFP open at the clock | other | deadline | C07C2866011/1756832039.396149 | none in scope | excluded by the hub (Leonard keeps it) |
| Dentsu meeting at 13:30 PT Oct 1 | temporal | start | frederick.stone@harmonygames.co/1843473831194478743 | none in scope | excluded: investor work |

Six hazard categories in scope: temporal T02; semantic S04; referential R08, R04; quantitative Q01, Q10; state/lifecycle L08, L12; identifier/format I04, I03.

**Sibling-defect sweep.** Designed defects are a superseded price (Framewell), an unanswered follow-up already answered elsewhere (Lanternfly), a moved pilot end (Clipforge), a done claim with a missing acceptance (Nintendo). Siblings checked: other vendor threads in Frederick's mailbox with an unanswered follow-up (Playable Factory `frederick.stone@harmonygames.co/1843000993076735547`, InterCo `frederick.stone@harmonygames.co/1841620870486605150`) are cold pitches and stay off by the scope rule; no other base portal mail claims registration (`frederick.stone@harmonygames.co/1842358947604469113`); no base vendor has a waiver or a moved end date (name census `plan/name_census.json`, positive control Balancy found in gmail/slack/gdrive).

## 1b Active speakers

Status from `references/universe_kb/by_universe/synthcut/activity.json` (status_at_clock).

| Person | Email | status_at_clock | Seeding role |
|---|---|---|---|
| Leonard Hayes | leonard.hayes@harmonygames.co | active_sep_2025_quiet_in_oct | hub mail, guardrails doc, Sep 29 amendment, Framewell thread reply (names Maren), Lanternfly DM thread reply (names Wen), Jan 5 review event, July signing note, ESG reply, folder README and template |
| Arthur Blake | arthur.blake@harmonygames.co | active_sep_2025_quiet_in_oct | keep-running card (Aug 12), ZOM-567 and its Sep 25 comment, Motive Forge decline |
| Robert | robert@harmonygames.co | active_sep_2025_quiet_in_oct | 'cancel everything' #executives post (distractor), Sep 17 showcase note (names the Dec 5 indie showcase and Rina) |
| Frederick Stone | frederick.stone@harmonygames.co | active_sep_2025_quiet_in_oct | persona: July tracker sheet, UA-buckets decoy doc, Lanternfly Sep 10 reply, the Q4 commitments folder |
| ESG Law partner | PERSON_2694_EMAIL | external (not in activity.json; base signature 'PARTNER, ESG Law' in mailbox file frederick@harmonygames.co_1841636073974841484.json) | signing note, intake checklist |
| 33 counterparty people | e.g. maren@framewell.io, dana@pingwise.io | external, seeded with no base footprint (plan/name_census.json) | offers, notices, follow-ups |

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

ENTITY email:frederick.stone@harmonygames.co  name=Frederick Stone  kind=person  emails=['frederick.stone@harmonygames.co']
  persona: frederick_stone - Co-founder / Executive
  slack      id=EMPLOYEE_0008_SLACK_ID, name=Frederick Stone, real_name=Frederick Stone, email=frederick.stone@harmonygames.co, is_bot=False, deleted=False, messages=4780, first_post=2023-09-15, last_post=2025-09-30   [join: exact_email]
  gmail      mailbox=frederick.stone@harmonygames.co, threads=4656, messages=5474, first=2024-06-25, last=2025-10-01, thread_filename_alias=['frederick@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=frederick.stone@harmonygames.co, owner_email=frederick.stone@harmonygames.co, summary=Frederick Stone — primary, events=316, last_event_before_clock=2025-09-30   [join: exact_email]
  gdrive     id=user_175c0d7bc72e, email=frederick.stone@harmonygames.co, display_name=frederick.stone@harmonygames.co, root_folders=['d_175c0d7bc72ed244b944cb'], owned_items=46, last_modified=2025-09-24, files_shared_with=213   [join: exact_email]
  linear     id=usr_175c0d7bc72ed244, email=frederick.stone@harmonygames.co, name=frederick.stone@harmonygames.co, is_active=True, last_activity=2025-08-26   [join: exact_email]
  github     login=PERSON_2314_GITHUB_USERNAME, name=Ryan, email=frederick.stone@harmonygames.co, type=User, last_activity=2025-03-25   [join: exact_email]
  trello     id=4b4a68fc0fec0b254e4f9d8e, username=frederick.stone, fullName=Frederick Stone   [join: exact_name]
  confluence id=user_EMPLOYEE_0008, account_id=acct_EMPLOYEE_0008, email=frederick.stone@harmonygames.co, display_name=Frederick Stone, is_active=True, last_activity=2025-09-01   [join: exact_email]
  contacts   contact_id=175c0d7bc72ed244b944cb90, name=Frederick Stone, email=frederick.stone@harmonygames.co, job=Commercial Lead, Marketing & Business Development, is_user=False   [join: exact_email]
  last activity: {'slack': '2025-09-30', 'gmail': '2025-10-01', 'gcal': '2025-09-30', 'gdrive': '2025-09-24', 'linear': '2025-08-26', 'github': '2025-03-25', 'confluence': '2025-09-01'}
  FLAG: GitHub PERSON_2314_GITHUB_USERNAME joined by email but shows name 'Ryan' (entity is Frederick Stone)

ENTITY email:leonard.hayes@harmonygames.co  name=Leonard Hayes  kind=person  emails=['leonard.hayes@harmonygames.co']
  persona: leonard_hayes - Co-founder & Creative Director / Executive
  slack      id=EMPLOYEE_0038_SLACK_ID, name=Leonard Hayes, real_name=Leonard Hayes, email=leonard.hayes@harmonygames.co, is_bot=False, deleted=False, messages=129898, first_post=2023-03-15, last_post=2025-10-01   [join: exact_email]
  gmail      mailbox=leonard.hayes@harmonygames.co, threads=15339, messages=19668, first=2023-03-15, last=2025-10-01, thread_filename_alias=['leonard@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=leonard.hayes@harmonygames.co, owner_email=leonard.hayes@harmonygames.co, summary=Leonard Hayes — primary, events=1382, last_event_before_clock=2025-09-30   [join: exact_email]
  gdrive     id=user_63fffeb4fab5, email=leonard.hayes@harmonygames.co, display_name=leonard.hayes@harmonygames.co, root_folders=['d_63fffeb4fab5233ed5bb73'], owned_items=752, last_modified=2025-09-30, files_shared_with=365   [join: exact_email]
  linear     id=usr_63fffeb4fab5233e, email=leonard.hayes@harmonygames.co, name=leonard.hayes@harmonygames.co, is_active=True, last_activity=2025-09-22   [join: exact_email]
  trello     id=PERSON_6094_TRELLO_USER_ID, username=leonard.hayes, fullName=Leonard Hayes, last_activity=2025-09-30   [join: exact_name]
  confluence id=user_EMPLOYEE_0038, account_id=acct_EMPLOYEE_0038, email=leonard.hayes@harmonygames.co, display_name=Leonard Hayes, is_active=True, last_activity=2025-09-29   [join: exact_email]
  contacts   contact_id=63fffeb4fab5233ed5bb73bf, name=Leonard Hayes, email=leonard.hayes@harmonygames.co, job=Co-founder & CEO, is_user=False   [join: exact_email]
  absent from: github
  last activity: {'slack': '2025-10-01', 'gmail': '2025-10-01', 'gcal': '2025-09-30', 'gdrive': '2025-09-30', 'linear': '2025-09-22', 'trello': '2025-09-30', 'confluence': '2025-09-29'}
ENTITY email:arthur.blake@harmonygames.co  name=Arthur Blake  kind=person  emails=['arthur.blake@harmonygames.co']
  persona: arthur_blake - Co-founder & CTO / Executive
  slack      id=EMPLOYEE_0025_SLACK_ID, name=Arthur Blake, real_name=Arthur Blake, email=arthur.blake@harmonygames.co, is_bot=False, deleted=False, messages=35266, first_post=2023-03-20, last_post=2025-10-01   [join: exact_email]
  gmail      mailbox=arthur.blake@harmonygames.co, threads=3320, messages=5134, first=2023-03-23, last=2025-10-01, thread_filename_alias=['blake@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=arthur.blake@harmonygames.co, owner_email=arthur.blake@harmonygames.co, summary=Arthur Blake — primary, events=756, last_event_before_clock=2025-09-30   [join: exact_email]
  gdrive     id=user_cc3e90160f49, email=arthur.blake@harmonygames.co, display_name=arthur.blake@harmonygames.co, root_folders=['d_cc3e90160f490686039986'], owned_items=246, last_modified=2025-09-19, files_shared_with=403   [join: exact_email]
  linear     id=usr_cc3e90160f490686, email=arthur.blake@harmonygames.co, name=arthur.blake@harmonygames.co, is_active=True, last_activity=2025-09-15   [join: exact_email]
  github     login=EMPLOYEE_0025_GITHUB_USERNAME, name=Arthur Blake, email=arthur.blake@harmonygames.co, type=User, last_activity=2025-09-30   [join: exact_email]
  trello     id=2162c1ba310341bf318f48b7, username=arthur.blake, fullName=Arthur Blake   [join: exact_name]
  confluence id=user_EMPLOYEE_0025, account_id=acct_EMPLOYEE_0025, email=arthur.blake@harmonygames.co, display_name=Arthur Blake, is_active=True, last_activity=2025-09-12   [join: exact_email]
  contacts   contact_id=cc3e90160f49068603998654, name=Arthur Blake, email=arthur.blake@harmonygames.co, job=Co-founder & CTO, is_user=False   [join: exact_email]
  last activity: {'slack': '2025-10-01', 'gmail': '2025-10-01', 'gcal': '2025-09-30', 'gdrive': '2025-09-19', 'linear': '2025-09-15', 'github': '2025-09-30', 'confluence': '2025-09-12'}
ENTITY email:robert@harmonygames.co  name=Robert  kind=person  emails=['robert@harmonygames.co']
  persona: robert - Co-Founder & Creative Director / Executive
  slack      id=EMPLOYEE_0016_SLACK_ID, name=Robert, real_name=Robert, email=robert@harmonygames.co, is_bot=False, deleted=False, messages=110334, first_post=2023-03-15, last_post=2025-10-01   [join: exact_email]
  gmail      mailbox=robert@harmonygames.co, threads=14813, messages=17363, first=2023-03-15, last=2025-10-01   [join: exact_email]
  gcal       calendar_id=robert@harmonygames.co, owner_email=robert@harmonygames.co, summary=Robert — primary, events=1133, last_event_before_clock=2025-09-30   [join: exact_email]
  gdrive     id=user_9f7ba94f7526, email=robert@harmonygames.co, display_name=Robert, root_folders=['d_9f7ba94f7526d54d8482ba'], owned_items=190, last_modified=2025-09-25, files_shared_with=412   [join: exact_email]
  linear     id=usr_Robert, email=robert@harmonygames.co, name=Robert, is_active=True, last_activity=2025-09-30   [join: exact_email]
  github     login=EMPLOYEE_0016_GITHUB_USERNAME, name=Robert, email=robert@harmonygames.co, type=User, last_activity=2025-09-29   [join: exact_email]
  trello     id=3d06b73654d0c8940792514c, username=robert, fullName=Robert   [join: exact_name]
  confluence id=user_EMPLOYEE_0016, account_id=acct_EMPLOYEE_0016, email=robert@harmonygames.co, display_name=Robert, is_active=True, last_activity=2025-09-30   [join: exact_email]
  contacts   contact_id=5f647df33ba6e92fbd56b05b, name=Robert, email=robert@harmonygames.co, job=Co-founder & Chief Product Officer, is_user=True   [join: exact_email]
  last activity: {'slack': '2025-10-01', 'gmail': '2025-10-01', 'gcal': '2025-09-30', 'gdrive': '2025-09-25', 'linear': '2025-09-30', 'github': '2025-09-29', 'confluence': '2025-09-30'}
```

- Leonard Hayes (leonard.hayes@harmonygames.co) vs the subject 'Leonard Hayes from SEMC' (`frederick.stone@harmonygames.co/1842279098258817066`): no seed names SEMC.
- Seeded external first names avoid every HG first name (Leonard, Arthur, Robert, Frederick, Julia, Brian, Douglas, Owen, Oliver, Martin, Claire, Calvin, Marcus, Simon, Samuel, Oscar, Felix, Vincent, Victor, Thomas, Tim, Elliot, Lucas, Matthew) — P01.
- ESG reuses the base tokens PERSON_2694 (partner) and PERSON_2599 (group intake), whose roles are stated in `frederick.stone@harmonygames.co/1841636073974841484` (learnings §14).

## 2 Cohort spine

- Rule (hub `frederick.stone@harmonygames.co/1844732913254784171`): every outside company with an offer, a trial, a quote, terms or an ask in front of HG that one of the founders engaged with (a call, a reply, a sign-up or paper); off: cold pitches nobody answered (including ones only forwarded internally), ad networks and Singular, investors, Mattel, withdrawn offers.
- Size: 46 looked at, 36 kept (Answered 4 · End 10 · Keep 3 · Sign 7 · Park 12); key = company; planned ids `plan/member_ids.json`.
- Surfaces and shortcut audit (manifest cohort.evidence_surfaces):
  - gmail · `gmail_search_messages+gmail_get_thread` · 0.5 × 46 · decides: every outside company with an offer, a trial, a quote, terms or an ask waiting on us · no bulk: gmail_search returns ids only; gmail_get_messages_batch reads bodies in bulk, so only half a call per company is counted · short-circuit: whether a company is in scope (engaged, not cold, not withdrawn) and what it is waiting on is only in its own thread; no list names the 36 (`frederick.stone@harmonygames.co/1844732913254784171`)
  - gdocs · `gdocs_get_document / gslides_get_presentation` · 1.0 × 32 · decides: decision per company · no bulk: each paper is its own document; no call returns the body of more than one document · short-circuit: cost, conversion dates and terms (auto-renewal, exclusivity, IP, term length) decide 13 of 32 papers and the mail never states them, so every paper must be read (`frederick.stone@harmonygames.co/1844732913254784171`)
  - contacts · `contacts_search_contacts` · 1.0 × 35 · decides: a contact for every company's person in Contacts, company in the job field, added only when missing · no bulk: three counterparties already have contacts; a per-company lookup is the dedupe check before each add (contacts_get_contacts pages 170+ internal entries) · short-circuit: adding without the lookup duplicates Kinetic Arcade, Lumencloud and Markward (`frederick.stone@harmonygames.co/1844732913254784171`)
  - gcal · `gcal_list_events (Jun-Jan window)` · 0.2 × 46 · decides: already answered: no second answer; the log records who answered (Answered by) · no bulk: one listing covers many companies (counted at 0.2 per company) · short-circuit: Clipforge's workspace id appears only on its kickoff call and paper; Spotlight's call is the only calendar trace of its answer, which is in Robert's note (`frederick.stone@harmonygames.co/1844732913254784171`)
- Predicate: the five decisions are a closed set in the guardrails doc `f_b98287f6f80fe431a71209`, applied top to bottom: already answered → cash test (unless on Arthur's keep-running list) → signing → park.
- House rule over the natural reading (A15): the keep-running exemption (`689b662c60cbe40b9f4a97ae`) and the Sep 29 travel amendment (`C07C2866011/1759166100.370044`).
- Boundary records (A17): Pixel Harbor's June quote `frederick.stone@harmonygames.co/1835288808653226583` (in, outside the September window), Hootline `frederick.stone@harmonygames.co/1839631800730308867` (in: Aug 5 sign-up and Aug 12 ask, no paper, nothing later — WIN), Rayking (out, forwarded internally), Nova Rewards `frederick.stone@harmonygames.co/1842255337882328812` (out, withdrawn), July tracker `f_9d6edd4922d8130ccd272e` (stale shorter list).
- Necessity: 13 of 32 papers decide their company's decision (cost, conversion date, auto-renewal, exclusivity, IP, term); the rest confirm the mail. Papers are per-document reads with no bulk body call, so a run that skips one is wrong on the ones that flip (Hardness_Mastery §2.5).

## 3 Hidden authorities

| Id | Name | Home | Decoy (scope) | Governs | Findable query |
|---|---|---|---|---|---|
| H1 | the runway guardrails doc | gdocs `f_b98287f6f80fe431a71209` | gdocs `f_7bacf15c4e8eea1a52dcd4, C07C2866011/1757961037.465799` (team: decoy 'UA ad-network spend (fundraising bucket vs real UA bucket, Sep 15-16)' vs task 'vendor and partner commitments outside UA') | R2, R4, R7 | "runway guardrails" (proved at injection with hg.py search on the overlay; `f_b98287f6f80fe431a71209`) |
| H2 | ESG's note about signing | gmail `frederick.stone@harmonygames.co/1844177063117059830` | slack `C07C2866011/1753207800.603298` (superseded: older entry of T7's version_records) | R6 | "ESG signing" (proved at injection with hg.py search on the overlay; `frederick.stone@harmonygames.co/1844177063117059830`) |
| H3 | Arthur's keep-running list | trello `689b662c60cbe40b9f4a97ae` | trello `trello:688c4fa78031638f0804a994` (team: decoy 'tools Leonard cancelled in his August cleanup' vs task 'what the live game needs to keep running') | R3 | "keep-running" (proved at injection with hg.py search on the overlay; `689b662c60cbe40b9f4a97ae`) |

Each authority is named by a fragment (K1 names H1 and H2 in `frederick.stone@harmonygames.co/1844732913254784171`; K4 names H3 in `f_b98287f6f80fe431a71209`) and none is linked by the hub. `governs` lists do not overlap (hardness_gate hidden_authorities).

## 4 Delegation lattice

| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |
|---|---|---|
| A1 | Leonard's vendor and partner email | `frederick.stone@harmonygames.co/1844732913254784171` |
| A2 | my Q4 commitments folder | `d_80a8c04753ba82ba4ba6a5` |

Hub: Leonard's Sep 30 23:20Z mail to Frederick (`frederick.stone@harmonygames.co/1844732913254784171`), in Leonard's voice, delegating by role: the guardrails doc, the Monday #executives change, ESG's note, the folder README. It never lists companies, links or locations of evidence.

| Fragment | Service · container | Kind | Chain | Delegated by | Delegation quote (verbatim, planned wording) | Requirements | Names authorities |
|---|---|---|---|---|---|---|---|
| K1 | gmail · `frederick.stone@harmonygames.co/1844732913254784171` | requirement | A1 | `frederick.stone@harmonygames.co/1844732913254784171` | "anyone outside the investor work who has an offer, a trial, a quote, terms or an ask in front of us and that one of us has actually engaged with" | R1, R5, R8, R10 | H1 ('the runway guardrails doc'), H2 ('ESG's note about signing') |
| K2 | gdocs · `f_b98287f6f80fe431a71209` | delegation | A1 → K1 | `frederick.stone@harmonygames.co/1844732913254784171` | "Go by the runway guardrails doc for what we do with each one" | R2 | — |
| K3 | gdocs · `f_b98287f6f80fe431a71209` | requirement | A1 → K1 | `frederick.stone@harmonygames.co/1844732913254784171` | "Go by the runway guardrails doc for what we do with each one" | R4 | — |
| K4 | gdocs · `f_b98287f6f80fe431a71209` | requirement | A1 → K1 | `frederick.stone@harmonygames.co/1844732913254784171` | "Go by the runway guardrails doc for what we do with each one" | R3 | H3 ('Arthur's keep-running list on our board') |
| K5 | gmail · `frederick.stone@harmonygames.co/1844177063117059830` | requirement | A1 → K1 | `frederick.stone@harmonygames.co/1844732913254784171` | "Anything that needs signing goes the way ESG's note about signing says" | R6 | — |
| K6 | trello · `689b662c60cbe40b9f4a97ae` | requirement | A1 → K1 → K4 | `f_b98287f6f80fe431a71209` | "anything on Arthur's keep-running list on our board stays" | R3 | — |
| K7 | gcal · `evt_fd469c29811879519c2c96` | amendment | A1 → K1 → K2 | `f_b98287f6f80fe431a71209` | "comes back at the January commitments review on our calendars" | R7 | — |
| K8 | gdocs · `f_846ddc38b2aab3d2ed3fcb` | format | A1 → K1 | `frederick.stone@harmonygames.co/1844732913254784171` | "the README in the folder has the columns" | R9, R8 | — |
| K9 | gsheets · `f_05f0a451b29b19a1c0b90f` | format | A1 → K1 → K8 | `f_846ddc38b2aab3d2ed3fcb` | "copy the header row from the template sheet" | R9 | — |
| K10 | slack · `C07C2866011/1759166100.370044` | amendment | A1 → K1 | `frederick.stone@harmonygames.co/1844732913254784171` | "plus the one change I posted in #executives on Monday" | R2 | — |
| K11 | contacts · `9b0185e445572aeee9f27d35` | recipient | A1 → K1 → K5 | `frederick.stone@harmonygames.co/1844177063117059830` | "our intake address (it's in your Contacts as ESG Law intake)" | R6 | — |
| K12 | gdocs · `f_3b06917a41dd59308d890b` | format | A1 → K1 → K5 | `frederick.stone@harmonygames.co/1844177063117059830` | "what to include is in the intake checklist I shared" | R6 | — |
| K13 | gmail · `frederick.stone@harmonygames.co/1844732913254784171` | destination | A1 | `frederick.stone@harmonygames.co/1844732913254784171` | "reply here with what we're keeping and what's waiting on Arthur or me to sign" | R10 | — |
| K14 | gmail · `frederick.stone@harmonygames.co/1844732913254784171` | requirement | A1 | `frederick.stone@harmonygames.co/1844732913254784171` | "Everyone who is waiting to hear from us should get a written answer this week" | R5 | — |

- Amendments in another service, later in time: K10 Slack `C07C2866011/1759166100.370044` (Sep 29, travel counts as cash) changes one clause of K2 (`f_b98287f6f80fe431a71209`, Sep 26); K7 gcal `evt_fd469c29811879519c2c96` (created Sep 29) pins the revisit date the doc gives as 'the first week of January'. The rest of the doc stands (no later record restates the amended clauses).
- Non-authoritative distractors: Robert's 'just cancel every marketing tool' (`C07C2866011/1758819840.884370`, T10); Frederick's UA-buckets doc (`f_7bacf15c4e8eea1a52dcd4`, H1 decoy, another scope); Leonard's July 'sign small stuff yourself' (`C07C2866011/1753207800.603298`, superseded by ESG, T7).

## 5 Chains and trap register

| Chain | Root cause | Hops (service: record → finding) | Ends in |
|---|---|---|---|
| C1 | A24 | gmail: `frederick.stone@harmonygames.co/1842359398719557772` (Nintendo Developer Portal: Registration Completed (Sep 4)) → slack: `C07C2866011/1757011358.730529` (Frederick: I registered an account for harmonygames) → linear: `ZOM-567` (Arthur, Sep 25 comment: org account limited until an officer accepts the Global ToS and NDA) → gmail: `frederick.stone@harmonygames.co/1844177063117059830` (ESG: only Leonard or Arthur accept terms; waiting on a signature -> founders' board card) | R6 |
| C2 | A11 | gmail: `frederick.stone@harmonygames.co/1843618067251203081` (Framewell: Pro plan from Nov 1 at $149/month) → gdocs: `framewell order form` (billing starts Nov 1 (cash in window)) → slack: `C07C2866011/1758920520.674991` (Leonard (thread reply under the Sep 22 Playtestcloud post): no charge until Feb 1) → gcal: `evt_fd469c29811879519c2c96` (parked -> revisit at the Jan 5 review) | R7 |
| C3 | A25 | gmail: `frederick.stone@harmonygames.co/1842800807116855774` (Lanternfly proposal (Sep 9); Frederick: 'we'll take a look' (Sep 10); Sep 22 'any news?' unanswered in the thread) → gslides: `f_5dbbaf5b251d5261427eb1` (Southeast Asia publishing proposal deck) → slack: `D05S58U4SAK/1758151772.570449` (Leonard (DM root, Sep 17): 'we have no localization though') → slack: `D05S58U4SAK/1759174260.052645` (Leonard (DM thread reply, Sep 29): rang Wen back Saturday, Southeast Asia waits until after the raise, talk in January) | R4 |
| C4 | A15 | gmail: `frederick.stone@harmonygames.co/1844157874176168845` (free tier ends Oct 31; Team $29/month from Nov 1 unless you downgrade) → gdocs: `pingwise terms` (uptime monitoring and on-call paging for the backend endpoints) → gdocs: `f_b98287f6f80fe431a71209` (exemption: anything on Arthur's keep-running list stays) → trello: `689b662c60cbe40b9f4a97ae` (checklist item 'the night pager for backend outages') | R3 |
| C5 | A4 | gdocs: `clipforge pilot agreement` (pilot free through Jan 15, 2026; workspace HG-2291) → gmail: `frederick.stone@harmonygames.co/1843067564852153540` (processor notice for workspace HG-2291: pilot ends Oct 15, $1,800/month from Oct 16) → gcal: `evt_0a5e42c3aac62434ba2cfc` (Jul 14 kickoff (UGC Studio) ties the workspace to Clipforge) | R2 |
| C6 | A17 | gmail: `frederick.stone@harmonygames.co/1835288808653226583` (June 18 quote: booth hold needs a $2,400 deposit by Oct 10) → gdocs: `pixel harbor quote` (deposit terms; showcase Oct 24) → gmail: `frederick.stone@harmonygames.co/1844732913254784171` (scope: anyone with an offer in front of us that one of us engaged with (no date limit)) | R1 |
| C7 | A17 | gmail: `frederick.stone@harmonygames.co/1839631800730308867` (Aug 5 sign-up (free until Jan 31) and Gemma's Aug 12 'keep it after Jan 31?', nothing later, no filed paper) → gmail: `frederick.stone@harmonygames.co/1844732913254784171` (scope: an offer in front of us that one of us engaged with (a sign-up), no date limit) → gcal: `evt_fd469c29811879519c2c96` (parked -> revisit at the Jan 5 review) | R1 |
| C8 | A25 | gmail: `frederick.stone@harmonygames.co/1842712097588195482` (Rina's Sep 8 invitation: Dec 5 indie showcase, $750 stand fee, 'could we set up a call?') → gcal: `evt_564a16d0f5f6598d0360d5` (Sep 17 showcase call, Robert organizer (no answer in the description)) → slack: `C07C2866011/1758134460.899858` (Robert (Sep 17, #executives): sitting the Dec 5 indie showcase out, let Rina know) | R4 |

| Trap | Family | Records | Requirement | Expected wrong reading | Resolver | Discovery order |
|---|---|---|---|---|---|---|
| T1 | done_gap | `ZOM-567`, `cmt_c9a6660d81e067ad1de7`, `frederick.stone@harmonygames.co/1842359398719557772`, `C07C2866011/1757011358.730529` | R6 | Nintendo is done: Frederick registered and the portal sent Registration Completed, so nothing is waiting | Arthur's Sep 25 comment on ZOM-567: the org account stays limited until an officer accepts the Global ToS and NDA; with ESG's rule it is Sign with a founders' board card | the two Sep 4 portal mails and Frederick's #executives post come back from any Nintendo search; the comment needs linear_list_comments on ZOM-567 |
| T2 | superseding | `frederick.stone@harmonygames.co/1843618067251203081`, `C07C2866011/1758920520.674991`, `C07C2866011/1758513190.847889` | R2 | Framewell is paid from Nov 1, so it fails the cash test: End with a cancellation | Leonard's Sep 26 reply under his Sep 22 Playtestcloud post: Maren (Framewell's account manager on the order-form mail) holds the Pro plan at no charge until Feb 1 -> free until January -> Park, revisit Jan 5 | the quote thread and order form are read first; the reply sits under a root about another vendor, #executives history shows roots only, and the reply names neither Framewell nor 'vendor', so a company-name search misses it (rev3 pre-check found it by 'Framewell', event 444) |
| T3 | completion_elsewhere | `frederick.stone@harmonygames.co/1842800807116855774`, `D05S58U4SAK/1759174260.052645`, `D05S58U4SAK/1758151772.570449` | R4 | Lanternfly's Sep 22 follow-up is unanswered, so it gets a Park reply | Leonard's Sep 29 reply in the DM thread under his Sep 17 localization message: he rang Wen back (Southeast Asia waits until after the raise, talk in January) -> Answered by Leonard, revisit Jan 5, no second answer | the thread with the unanswered follow-up is the natural read; the answer is a thread reply in the 1:1 DM (history shows roots only) naming Wen and the Southeast Asia deal, so neither a 'Lanternfly' nor a 'told' search returns it (rev3 found the DM root at events 387, 426, 428) |
| T4 | authority | `frederick.stone@harmonygames.co/1844157874176168845`, `689b662c60cbe40b9f4a97ae` | R3 | Pingwise bills $29/month from Nov 1, so it fails the cash test: End (ask to downgrade) | the guardrails exempt Arthur's keep-running list; its checklist item 'the night pager for backend outages' is Pingwise's on-call paging -> Keep, confirm staying | the cash test is read before the exemption is joined to a checklist item that does not name the vendor |
| T5 | superseding | `frederick.stone@harmonygames.co/1843067564852153540`, `evt_0a5e42c3aac62434ba2cfc` | R2 | Clipforge's pilot is free through Jan 15, 2026 (its agreement), so Park | the processor notice for workspace HG-2291 (UGC Studio, tied to Clipforge by the paper and the Jul 14 kickoff) moves the pilot end to Oct 15 and starts $1,800/month on Oct 16 -> End, cancel in writing by Oct 15 | the agreement and the rep's thread name Clipforge; the notice names only the workspace and product, so a name search misses it |
| T6 | exact_predicate | `frederick.stone@harmonygames.co/1835288808653226583` | R1 | the backlog is what came in during September, so Pixel Harbor's June quote is missed | the hub's scope has no date limit (an offer in front of us that we engaged with); the June quote still needs a deposit by Oct 10 -> on the log, End | date-windowed mail searches (after Sep 1) do not return a June 18 thread |
| T7 | superseding | `C07C2866011/1753207800.603298`, `frederick.stone@harmonygames.co/1844177063117059830` | R6 | Leonard's July note lets Frederick accept small terms himself, so Markward's click-through needs no card | ESG's Sep 24 note (only Leonard or Arthur accept terms, whatever the amount) and Leonard's Sep 25 reply ('this replaces what I said in July') | — |
| T8 | superseding | `f_b98287f6f80fe431a71209`, `evt_fd469c29811879519c2c96` | R7 | revisit 'in the first week of January' (the guardrails' wording), dated by guess | Leonard's commitments review on Mon Jan 5, 2026 (created Sep 29) is the revisit date | — |
| T9 | superseding | `f_b98287f6f80fe431a71209`, `C07C2866011/1759166100.370044` | R2 | travel and event costs count only when we book them, so Wishwave (partner-booked travel) parks | Leonard's Sep 29 #executives change: travel and event costs count as cash even when a partner books them -> Wishwave End | — |
| T10 | distractor (non_authoritative_instruction) | `C07C2866011/1758819840.884370` | R2 | Robert's 'just cancel every marketing tool' settles every decision as End | Robert is not the owner of the guardrails; Leonard's doc decides | — |
| T11 | distractor (scope_adjacent) | `frederick.stone@harmonygames.co/1843000993076735547` | R1 | Playable Factory's unanswered follow-up is a company waiting on us | a cold pitch nobody engaged with is off the log | — |
| T12 | distractor (scope_adjacent) | `frederick.stone@harmonygames.co/1817715521687421486` | R1 | the Google partner check-in is a partner waiting on timing | the hub keeps ad networks off the log (UA budget call) | — |
| T13 | distractor (already_done) | `frederick.stone@harmonygames.co/1840501641217286806` | R4 | Balancy's trial offer needs an answer | Leonard answered in-thread on Sep 11 ('we'll circle back') -> Answered by Leonard, revisit | — |
| T14 | stale_summary (stale_summary) | `f_9d6edd4922d8130ccd272e` | R1 | Frederick's July 31 vendor tracker is the population | the tracker predates most offers and lists ended ones; the hub's scope rule over the mail decides | — |
| T15 | distractor (keyword_collision) | `frederick.stone@harmonygames.co/1842898562278009736` | R1 | NCsoft's engine demo and 'pilot' talk is a partner offer | NCsoft is strategic / investor talks (bridge work), off the log | — |
| T16 | distractor (withdrawn_ask) | `frederick.stone@harmonygames.co/1842255337882328812` | R1 | Nova Rewards' offer is waiting on us | Nova withdrew it on Sep 23 | — |
| T18 | distractor (scope_adjacent) | `frederick.stone@harmonygames.co/1842348778705877030` | R1 | Rayking's pitch is engaged: Frederick wrote 'Hi …, Leonard forwarded me your email' | that reply went to Leonard (To: leonard.hayes), so nothing from us reached Rayking: a pitch only forwarded around internally stays off the log | — |
| T17 | distractor (near_duplicate_record) | `retainly-terms` | R2 | Retainly's trial converts to paid like Reviewly's, so End | Retainly converts Jan 12, 2026, outside the cash window -> Park | — |
| T19 | completion_elsewhere | `frederick.stone@harmonygames.co/1842712097588195482`, `C07C2866011/1758134460.899858` | R4 | Spotlight Fest's Dec 5 invitation ($750 stand fee) is still open, so the cash test ends it with a written no | Robert's Sep 17 #executives note: he had the call about the Dec 5 indie showcase and let Rina know we're sitting it out -> Answered by Robert, no second answer | the invitation thread and the Sep 17 call event are the natural reads; the note names neither the fest nor 'told', and sits before the late-September #executives window (rev3 found the old wording by 'Spotlight' and 'told', events 386, 426) |
| T20 | exact_predicate | `frederick.stone@harmonygames.co/1839631800730308867` | R1 | the backlog is what is live in recent mail and the filed papers, so Hootline (nothing after Aug 12, no paper) is missed | the hub's scope has no date limit: Frederick signed up (engaged) and Gemma's Aug 12 question is unanswered -> on the log, Park, revisit Jan 5 | a mailbox listing from mid-August, the paperwork folder and the July tracker all miss it (rev3's cohort came from exactly those, events 66, 282, 284); an undated mail search or a June-onward listing finds it |

Hardness v2 traps used as separate cross-source decisions (guide Part 3), each with the convincing wrong source and the record that beats it:

| Channel | v2 trap | Convincing wrong source (who, when) | Record that beats it (who, when, authority) | Weight-5 rows it moves |
|---|---|---|---|---|
| DONE | 1 · proving done across services | portal 'Registration Completed' (Nintendo, Sep 4, `frederick.stone@harmonygames.co/1842359398719557772`) + Frederick's post (`C07C2866011/1757011358.730529`) | Arthur's ZOM-567 comment (Sep 25, CTO) + ESG's signing rule (`frederick.stone@harmonygames.co/1844177063117059830`, counsel) | X1, X2, X17 |
| CORR | 2 · a correction somewhere else | Framewell's quote thread (Sep 18, `frederick.stone@harmonygames.co/1843618067251203081`) and order form | Leonard's thread reply under his Sep 22 Playtestcloud post (Sep 26, `C07C2866011/1758920520.674991`), naming Maren and the Pro plan, not Framewell | X3, X4, X14 |
| COMPL | 9 · work someone already did | Lanternfly's unanswered Sep 22 follow-up in its thread (`frederick.stone@harmonygames.co/1842800807116855774`) | Leonard's Sep 29 reply in the DM thread under his Sep 17 localization message (`D05S58U4SAK/1759174260.052645` under `D05S58U4SAK/1758151772.570449`): he rang Wen back | X5, X6, X15, X19 |
| NOTE | 9 · work someone already did | Spotlight Fest's Dec 5 invitation with a $750 stand fee (`frederick.stone@harmonygames.co/1842712097588195482`) | Robert's Sep 17 #executives note (`C07C2866011/1758134460.899858`): sitting the Dec 5 indie showcase out, let Rina know | X20, C3 |
| EXC | 5 · a rule or exception hidden in the data | the cash test (guardrails `f_b98287f6f80fe431a71209`) against Pingwise's Nov 1 bill (`frederick.stone@harmonygames.co/1844157874176168845`) | Arthur's Aug 12 keep-running checklist (`689b662c60cbe40b9f4a97ae`), item named by function | X7, X16, P1 |
| DATE | 4 · dates, windows and dependencies | Clipforge's pilot agreement: free through Jan 15, 2026 | processor notice for workspace HG-2291 (Sep 12, `frederick.stone@harmonygames.co/1843067564852153540`): pilot ends Oct 15, billing from Oct 16 | X9, X10, X11 |
| FILT | 7 · items outside the obvious filter | September-window mail searches (the recent backlog) | Pixel Harbor's June 18 quote (`frederick.stone@harmonygames.co/1835288808653226583`) with a deposit due Oct 10, in scope by the hub's undated rule | X12, X13, V1 |
| WIN | 7 · items outside the obvious filter | the recent inbox, the paperwork folder and the July tracker (rev3 pre-check events 66, 282, 284) | Hootline's Aug 5 sign-up and Aug 12 unanswered ask (`frederick.stone@harmonygames.co/1839631800730308867`), no filed paper, in scope by the hub's undated rule | X18, X21, V1 |

### Mechanism portfolio (S5a)

Priors from `tools/hardness_ledger.py priors --model claude-opus-5-5` (UNCALIBRATED; never pooled across models). Rates used by the forecast are disclosed overrides from measured placements on the completed Frederick tasks (00_Completed_Task_Learnings.md).

| # | Candidate (anchor records) | Coupling | Findability term | Prior (family · record ids) | Design rate | Survives complete retrieval | Selected |
|---|---|---|---|---|---|---|---|
| DONE | Nintendo done-gap (`frederick.stone@harmonygames.co/1842359398719557772`, ZOM-567) | registration → officer acceptance → card | 'Nintendo' finds mail; comment needs linear_list_comments | done_gap Beta(1,2) · hev_7f44d83eaad625e9, hev_522f1ca2bc9062de | 0.50 | yes: judgment needs the comment + ESG rule | yes |
| CORR | Framewell waiver (`C07C2866011/1758920520.674991`) | waiver → Park → revisit | rev4: 'Framewell' and 'vendor' searches return nothing; found by 'Maren', 'Pro plan' or opening the Playtestcloud thread | superseding Beta(1,3) · hev_1ceea0e7e912f48b, hev_ebc012c844829411 | 0.70 | yes: the reply is a later dated claim | yes (rebuilt) |
| COMPL | Lanternfly answered by phone (`D05S58U4SAK/1759174260.052645`) | answered → no second answer → log who | rev4: a DM thread reply naming Wen and the Southeast Asia deal; found by opening the thread or a 'Southeast Asia'/'Wen' search | completion_elsewhere Beta(1,2) · hev_13d86dcf23442708 | 0.65 | yes: 'answered elsewhere' is a judgment | yes (rebuilt) |
| NOTE | Spotlight answered by Robert (`C07C2866011/1758134460.899858`) | answered → no second answer → log who | a full September #executives read, a 'showcase'/'Rina' search or Robert's history | completion_elsewhere Beta(1,2) · hev_13d86dcf23442708 | 0.60 | yes | yes (new, rev4) |
| WIN | Hootline outside the filter (`frederick.stone@harmonygames.co/1839631800730308867`) | undated scope → in → Park → revisit | an undated mail search or a June-onward listing; not the folder, the tracker or an Aug 15+ listing | exact_predicate Beta(1,3) · hev_9c403cae42eb4df8, hev_c2297d21ba5cbc7b | 0.55 | partly: once found, the decision is plain | yes (new, rev4) |
| EXC | Pingwise on the keep-running list (`689b662c60cbe40b9f4a97ae`) | exemption → Keep → next bill date | 'keep-running' finds the card; item names a function | authority Beta(1,2) · hev_d17e4abe74f0e7e0 | 0.40 | yes: function-to-vendor join | yes |
| DATE | Clipforge moved pilot end (`frederick.stone@harmonygames.co/1843067564852153540`) | moved end → in window → End → cancellation address | notice names workspace HG-2291, not the company | superseding Beta(1,2) · hev_e61e07235eadbd24 | 0.50 | yes: id join + window | yes |
| FILT | Pixel Harbor June quote (`frederick.stone@harmonygames.co/1835288808653226583`) | undated scope → in → End | its filed paper and the July tracker name it (rev3 events 284, 296) | exact_predicate Beta(1,3) · hev_9c403cae42eb4df8, hev_c2297d21ba5cbc7b | 0.10 | partly: once found, the decision is plain | yes (kept; leaks via its paper) |
| SIGN | July note vs ESG (`C07C2866011/1753207800.603298` → `frederick.stone@harmonygames.co/1844177063117059830`) | supersession → Markward card | on the delegation path | superseding · hev_e61e07235eadbd24 | 0.15 | yes | yes (secondary) |
| AMEND | travel counts as cash (`C07C2866011/1759166100.370044`) | amendment → Wishwave End | named by the hub | superseding · hev_1ceea0e7e912f48b | 0.10 | yes | yes (secondary) |
| ALIAS-DD | Rayking 'explore for DD' (`frederick.stone@harmonygames.co/1842348778705877030`) | DD = Domino Delights or due diligence | — | scope_alias: no record | — | no: an unsettled fork | rejected (UGT fork; Rayking made a boundary, T18) |
| CAL-ONLY | a member visible only through a calendar call | calendar listing → inclusion | the listing every run reads | exact_predicate · hev_9c403cae42eb4df8 | ≈0.05 (bridge Homa/Brightwater caught 6/6) | no | rejected (measured leak) |
| SAME-THREAD | Balancy's in-thread answer (`frederick.stone@harmonygames.co/1840501641217286806`) | answered | the thread itself | completion_elsewhere: none | ≈0 | — | kept as a control (T13) |
| TRACKER | July tracker as the population (`f_9d6edd4922d8130ccd272e`) | stale list | Drive search 'vendor' | stale_summary: none | ≈0.1 | — | kept as a distractor (T14) |
| CMP-SDK | a paid consent SDK the live game needs | exemption | — | — | — | no: GitHub review comment on deferred crash reporting (`C093LEZGF6J`) invites a git-level contradiction | rejected (coherence) |
| COUNTS | report counts per decision | aggregate of every channel | — | — | — | P(fails all six) 0.45–0.58 in the first forecast (`hev_02816c7ce07c1dbb`) | rejected (predicted all-fail rows) |

Each selected rule's controls and over-application operator are in the draft manifest (`mechanism_portfolio[].controls`, `over_application`), and its channel in `channels` (CH-DONE … CH-FILT, CH-NOTE, CH-WIN, CH-SLIP). Design rates for EXC, DATE, SIGN and AMEND were cut to 0.05–0.10 after the rev3 pre-check caught them on the delegation path or in the swept inbox (§14).

### Liveness flags (S5b)

`trap_liveness.py --design` (verbatim):

```
TRAP LIVENESS · ADVISORY · UNCALIBRATED · lexical warnings, not proof · DESIGN (no SQL: record text unavailable, only manifest-structure flags can fire) · on the Season Pass backtests these are development fixtures, not validation
  hub frederick.stone@harmonygames.co/1844732913254784171 · direct delegations 9 · rule placement: A15 nodes only: ['C4', 'T4', 'T9'] (mechanism_portfolio); every other node SKIP
  T1   done_gap           breadcrumb  [rule placement SKIP: not an A15 node]
  T2   superseding        breadcrumb  [rule placement SKIP: not an A15 node]
  T3   completion_elsewhe -  [rule placement SKIP: not an A15 node]
  T4   authority          breadcrumb
  T5   superseding        breadcrumb  [rule placement SKIP: not an A15 node]
  T6   exact_predicate    breadcrumb, order  [rule placement SKIP: not an A15 node]
  T7   superseding        breadcrumb  [rule placement SKIP: not an A15 node]
  T8   superseding        -  [rule placement SKIP: not an A15 node]
  T9   superseding        breadcrumb
  T10  distractor         breadcrumb  [rule placement SKIP: not an A15 node]
  T11  distractor         breadcrumb, order  [rule placement SKIP: not an A15 node]
  T12  distractor         breadcrumb, order  [rule placement SKIP: not an A15 node]
  T13  distractor         -  [rule placement SKIP: not an A15 node]
  T14  stale_summary      -  [rule placement SKIP: not an A15 node]
  T15  distractor         breadcrumb, order  [rule placement SKIP: not an A15 node]
  T16  distractor         breadcrumb, order  [rule placement SKIP: not an A15 node]
  T18  distractor         breadcrumb, order  [rule placement SKIP: not an A15 node]
  T17  distractor         breadcrumb  [rule placement SKIP: not an A15 node]
  T19  completion_elsewhe -  [rule placement SKIP: not an A15 node]
  T20  exact_predicate    breadcrumb, order  [rule placement SKIP: not an A15 node]
  H1-decoy  f_7bacf15c4e8eea1a52dcd4     - (not in the SQL overlay: not read)
  dispositions: 0/22 recorded
```

| Flag | Nodes | Disposition |
|---|---|---|
| breadcrumb | T1, T2, T4, T5, T6, T7, T9, T10, T11, T12, T15, T16, T17, T18, T20 | structural at design time: the entry set reaches the governing authority or the hub's scope rule for the trap's requirement (`f_b98287f6f80fe431a71209`, `frederick.stone@harmonygames.co/1844177063117059830`, `frederick.stone@harmonygames.co/1844732913254784171`) — the incorporation link, never removed. No hub sentence names a trap's deciding record (the reply `C07C2866011/1758920520.674991`, the DM `D05S58U4SAK/1759174260.052645`, ZOM-567's comment, the notice `frederick.stone@harmonygames.co/1843067564852153540`, the checklist `689b662c60cbe40b9f4a97ae`, the June thread `frederick.stone@harmonygames.co/1835288808653226583`, Robert's note `C07C2866011/1758134460.899858`, the August Hootline thread `frederick.stone@harmonygames.co/1839631800730308867`); injection S5c re-runs the flag on the SQL text |
| order | T6, T11, T12, T15, T16, T18, T20 | the hub (`frederick.stone@harmonygames.co/1844732913254784171`) is decisive because it states the scope rule (R1); every company's own state sits in its own thread, never in the hub thread |
| SAME_PLACE (hardness_v2_check) | T7 | ESG's note and Leonard's confirming reply share `frederick.stone@harmonygames.co/1844177063117059830`; both are the governing side and the superseded July note sits in Slack (`C07C2866011/1753207800.603298`). SIGN is a secondary on-path rule, not a landing channel |
| DECISION_FLIP (hardness_v2_check) | SIGN, AMEND | secondary rules moving weight-3 rows (C10, P2, C11) by kind of work; the six landing rules each move three weight-5 rows. Weights are never raised (`09_Rubric_Writing.md` gate 8) |

## 6 Failure-diversity plan

| Channel | Behaviour that finds the deciding record | Measured analog (completed Frederick tasks) | Rows | Independent of |
|---|---|---|---|---|
| DONE | opening ZOM-567's comments (Linear rarely opened in commercial tasks) | bridge build access in a later #zombie-match3d post: 0/7 then 3/6 caught | X1, X2, X17 | Slack and mail behaviour (`cmt_c9a6660d81e067ad1de7`) |
| CORR | opening the thread under an unrelated #executives root, or a 'Maren'/'Pro plan' search (rev4: no company name) | bridge SciPlay reply under an a16z post: 2/8 then 3/6 caught; rev3's named reply caught by name (precheck event 444) | X3, X4, X14 | Linear, Trello (`C07C2866011/1758920520.674991`) |
| COMPL | opening a thread inside the 1:1 DM, or a 'Southeast Asia'/'Wen' search | rev3's newest-root DM read at precheck event 428; DM threads are not shown by history (roots only) | X5, X6, X15, X19 | thread-opening behaviour is shared with CORR, but in a different container (`D05S58U4SAK/1759174260.052645`) |
| NOTE | reading every September #executives root, or a 'showcase'/'Rina' search | rev3 read #executives from Sep 27 only (precheck event 30) | X20, C3 | name searches (`C07C2866011/1758134460.899858`) |
| WIN | an undated mail search or a June-onward listing | rev3 listed after:2025/08/15 (precheck event 66) and built the cohort from the folder and the tracker | X18, X21, V1 | Slack and Linear behaviour (`frederick.stone@harmonygames.co/1839631800730308867`) |
| EXC | joining a checklist item named by function to a vendor's paper | handover rules card + comment: caught by most runs; the function join is new (design 0.40) | X7, X16, P1 | mail and Slack (`689b662c60cbe40b9f4a97ae`) |
| DATE | reading a processor notice keyed by workspace id | handover deactivation mail keyed by publisher id: 5/6 missed (halved to 0.50 for a fairer id join) | X9, X10, X11 | name searches (`frederick.stone@harmonygames.co/1843067564852153540`) |
| FILT | mail searches with no September date filter | handover Arthur's email outside the money window: 2/6 missed | X12, X13, V1 | everything else (`frederick.stone@harmonygames.co/1835288808653226583`) |

Each landing channel moves two to four rows (a 1-row trap chains patterns: bridge rev12 batch 1). Five rebuilt or new channels (DONE, CORR, COMPL, NOTE, WIN) at ~0.55–0.70 give 0–5 landings per run; P(a run misses at most one of them) ≈ 0.1 (UNCALIBRATED). Replaying the rev3 pre-check's own behaviour on this surface scores 48.6 % (policy row below). Policy scores on the real surface (`plan/policy_scores.py`, UNCALIBRATED):

```
UNCALIBRATED · 34 slots · weight 138 · flippable 115
Whole policies:
  100.0%  perfect
   56.5%  reads mail, papers, hub-path rules; no Slack search, no Linear, no checklist join
   52.9%  trusts each company's own thread and paper
   90.6%  thorough but September-window searches only
   85.5%  thorough except DMs
   89.1%  thorough except Linear comments
   92.8%  literal cash test (no exemption join)
   48.6%  rev3 pre-check behaviour (name searches, Aug 15+ inbox, folder papers, no Linear)
   73.9%  rev3 behaviour plus DM threads and contact-name searches
Single misses: DONE 89.1%, CORR 89.1%, COMPL 85.5%, EXC 92.8%, DATE 89.1%, FILT 90.6%, SIGN 95.7%, AMEND 97.8%, NOTE 92.8%, WIN 92.0%
Pairs at or above 80 %: DONE+NOTE, DONE+WIN, CORR+NOTE, CORR+WIN, NOTE+WIN
scale rho  E[avg]  P(<80%) P(<90%) P(SD) E[SD]  P(<5 full) P(patterns) P(all, <80%)
 1.00 0.35   64.7%    0.98    1.00  0.89 0.157       1.00        0.99        0.87
 1.00 0.60   64.8%    0.96    1.00  0.94 0.185       1.00        0.98        0.89
 0.80 0.35   71.7%    0.87    1.00  0.91 0.160       1.00        1.00        0.80
 0.60 0.35   78.6%    0.56    0.95  0.86 0.151       1.00        0.99        0.52
 0.50 0.35   82.1%    0.36    0.88  0.80 0.142       1.00        0.98        0.34
 0.40 0.35   85.6%    0.18    0.75  0.70 0.129       0.99        0.97        0.17
 1.40 0.35   50.8%    1.00    1.00  0.51 0.105       1.00        0.91        0.49
```

Correlation risk named: CORR and COMPL both reward opening Slack threads (different containers: #executives vs the DM); NOTE rewards a full #executives read. The forecast's correlated scenario is the pessimistic view (P(all) 0.284). DONE (Linear) and WIN (undated mail) use distinct behaviours. SIGN and AMEND (rate 0.05) are left out of the forecast's exact combinations (8-mechanism limit).

## 7 Deliverables and dependent writes

| Write | Tool | Count | Depends on | Requirements | Target and access |
|---|---|---|---|---|---|
| gsheets | `gsheets_create_spreadsheet+gsheets_values_update` | 3 | K8, K9, C1, C2, C3, C4, C5, C6, C7, C8, T1, T2, T3, T4, T5, T6, T19, T20 | R1, R2, R3, R4, R9 | new sheet in Frederick's folder `d_80a8c04753ba82ba4ba6a5` (owner Frederick, Drive and Sheets rows agree) |
| gmail | `gmail_reply_to_message+gmail_send_message` | 34 | K1, K14, K5, K11, K12, C2, C3, C4, C5, C6 | R5, R6 | threads in Frederick's mailbox (`frederick.stone@harmonygames.co/1844732913254784171` and each company's); ESG intake from Contacts `9b0185e445572aeee9f27d35` |
| gcal | `gcal_create_event` | 14 | K7, C2, C3, C7, T8, T20 | R7 | Frederick's own calendar `frederick.stone@harmonygames.co` |
| contacts | `contacts_add_new_contact` | 32 | K1, K8, C6 | R8 | Contacts (unscoped) |
| trello | `trello_create_card` | 7 | K5, C1, T7 | R6 | founders' board To Do list `640643a3fd8f3ca308d93195` |
| gmail | `gmail_reply_to_message (report)` | 1 | K13, C1, C2, C3, C4, C5, C6 | R10 | threads in Frederick's mailbox (`frederick.stone@harmonygames.co/1844732913254784171` and each company's); ESG intake from Contacts `9b0185e445572aeee9f27d35` |

Reuse vs create (A8): three counterparties already have contacts (Kinetic Arcade, Lumencloud, Markward) — reuse, no duplicate.

## 8 Service role map

| Service | Role | Load-bearing fact or write | Carrier |
|---|---|---|---|
| gmail | hub ask and report destination; ESG's signing note and intake emails; every counterparty's offer thread (36 in scope, 10 boundary); Clipforge's processor notice; replies and cancellations | the ask, the signing rule, every offer's state and every written answer live in mail | ● (`frederick.stone@harmonygames.co/1844732913254784171`) |
| gdocs | runway guardrails doc (H1) and its UA-buckets decoy; the folder README; ESG's intake checklist; 28 counterparties' papers (order forms, terms, quotes) | the decision rules and each paper's cost, dates and terms (auto-renewal, exclusivity, IP, term) decide the decision | ● (`f_b98287f6f80fe431a71209`) |
| gdrive | Frederick's Q4 commitments folder (destination, owned by Frederick) holding the README and template; papers shared by counterparties | the log must be created in the owned folder | ● (`d_80a8c04753ba82ba4ba6a5`) |
| gsheets | log template header row; Frederick's stale July vendor tracker (decoy); the log itself | the log is the graded register | ● (`f_05f0a451b29b19a1c0b90f`) |
| gslides | partners' proposal decks as their papers (Lanternfly, Bundlehouse) | Bundlehouse's IP-licence term (counsel route) and Lanternfly's proposal live only in the deck | ● (`f_5dbbaf5b251d5261427eb1`) |
| slack | Leonard's Sep 29 #executives amendment; Leonard's Sep 26 thread reply (Framewell waiver, names Maren) under the Sep 22 Playtestcloud root; Leonard's Sep 29 DM thread reply under his Sep 17 localization message (Lanternfly answered, names Wen); Robert's Sep 17 note (Spotlight answered, names the Dec 5 indie showcase); Leonard's July 'sign small stuff' note (superseded); Robert's 'cancel everything' post (non-authoritative); Frederick's Sep 4 Nintendo post (base) | Framewell's decision, Lanternfly's answered state and the travel amendment exist only in Slack | ● (`C07C2866011/1759166100.370044`) |
| gcal | Leonard's Jan 5, 2026 commitments review (revisit date); Clipforge's Jul 14 kickoff; Spotlight's Sep 17 call (no answer in its description); revisit writes | the revisit date lives in the calendar; the revisit reminders are writes | ● (`evt_fd469c29811879519c2c96`) |
| trello | Arthur's keep-running list card (H3) on the founders' board; signature cards in To Do (writes); base BrowserStack card (decoy) | the Keep exemption is decided by the card's checklist; routed signatures are cards | ● (`689b662c60cbe40b9f4a97ae`) |
| contacts | ESG Law intake entry (recipient); three counterparties already present; contact writes | ESG's intake address and the dedupe check live in Contacts; contacts are writes | ● (`9b0185e445572aeee9f27d35`) |
| linear | ZOM-567 'Switch dev kit' and Arthur's Sep 25 comment (the Nintendo done-gap) | the missing piece of Nintendo's 'done' lives only in the Linear comment | ● (`ZOM-567`) |
| github | not used | none (S04 name mismatch; nothing in scope) | — (`frederick.stone@harmonygames.co/1842359398719557772`) |
| confluence | not used | never carries a fact (injected pages may not load, learnings §26) | — |
| snowflake | not used | not writable; no money row reads the warehouse | — |

## 9 Call budget

| Phase | Service | Calls | Necessity reason |
|---|---|---|---|
| discovery | gmail | 4 | read the hub; open ESG's signing thread with Leonard's reply; open the ESG engagement thread for the intake group |
| discovery | gdocs | 4 | read the guardrails doc, the folder README, ESG's intake checklist; reject the UA-buckets doc on scope |
| discovery | gsheets | 2 | read the template header row; reject the July tracker as stale |
| discovery | gdrive | 2 | list the Q4 commitments folder; locate papers shared by counterparties |
| discovery | slack | 4 | read Leonard's Sep 29 amendment; search #executives for the guardrails context and the July signing note |
| discovery | trello | 2 | read the founders' board lists and cards; read Arthur's keep-running checklist |
| discovery | gcal | 1 | read the Jan 5 commitments review |
| discovery | contacts | 1 | find ESG Law intake |
| enumeration | gmail | 8 | census of offer threads since June (dated and undated searches, vendor and partner terms); every company has its own thread |
| enumeration | gcal | 2 | list calls Jun 2025 to Jan 2026 (kickoffs, partner calls, the review) |
| enumeration | slack | 3 | search #executives and DMs for vendor and partner decisions Leonard or Arthur already made |
| per-record | gmail | 23 | each of 46 companies' thread read (bulk batch reads counted at half a call per company) |
| per-record | gdocs | 29 | each counterparty's paper (order form, terms, quote): cost, conversion dates, auto-renewal, exclusivity, IP, term |
| per-record | gslides | 3 | partners' proposal decks (Lanternfly, Bundlehouse) and one deck-only term |
| per-record | contacts | 35 | lookup before each add (three counterparties already exist; ESG intake) |
| per-record | slack | 8 | name, contact-name and topic searches for companies whose state may have moved off their thread (Framewell, Lanternfly, Spotlight and others), and opening the threads they land in |
| per-record | linear | 2 | ZOM-567 and its comments (Nintendo) |
| per-record | gcal | 9 | calls tied to a company (Clipforge kickoff, Spotlight, partner calls) read at 0.2 per company |
| writes | gmail | 31 | a written answer to each of 31 companies waiting to hear from us (replies on their threads; Clipforge's cancellation to the notice's address) |
| writes | gmail | 3 | one email per counsel agreement to ESG's intake address (Kinetic Arcade, Lumencloud, Bundlehouse) |
| writes | gcal | 14 | a revisit reminder on Jan 5 for each of 12 parked companies and 2 'later' answers |
| writes | contacts | 32 | a contact for each company's person not already in Contacts |
| writes | trello | 7 | a founders' board To Do card for each company waiting on a signature |
| writes | gsheets | 3 | create the log in the folder and write its rows |
| writes | gmail | 1 | reply on Leonard's thread with what stays and what waits on a signature |
| read-back | gsheets | 2 | read the log back against the README columns |
| read-back | trello | 1 | confirm the cards landed in To Do |
| **total** | 10 services | **236** | unconditional; largest share outside the per-record phase 37 % (gmail) |

Golden-run note: a lean correct run still needs every paper read (13 decide) and every per-company write (31 answers, 14 reminders, 32 contacts, 7 cards, 3 ESG emails, the log, the report) ≈ 150 counted calls; the requester's > 130 floor sits under it. Measured analogs: bridge (44 per-entry writes) 109–150; card spend (per-document reads) 554–573.

## 10 QC rails

### Two-reading table

| Decision point | Best reading | Strongest alternative | Resolution (record) |
|---|---|---|---|
| Rayking in scope | out: nothing from HG reached them | in: Frederick wrote 'Hi …, Leonard forwarded me your email' | the reply's To is leonard.hayes (`frederick.stone@harmonygames.co/1842348778705877030`); hub: pitches only forwarded around internally stay off (T18) |
| Pixel Harbor in scope | in: a June quote still waiting (deposit by Oct 10) | out: stale, before the September backlog | hub scope has no date limit; the quote's hold runs to Oct 10 (`frederick.stone@harmonygames.co/1835288808653226583`) |
| Balancy | Answered by Leonard, revisit Jan 5 | Park with a new reply | Leonard answered in-thread Sep 11 'we'll circle back' (`frederick.stone@harmonygames.co/1840501641217286806`); guardrails: already answered with 'later' → revisit |
| Lanternfly | Answered by Leonard, revisit Jan 5 | Sign (2-year exclusivity) or Park with a reply to the follow-up | Leonard's Sep 29 DM thread reply (`D05S58U4SAK/1759174260.052645`): 'rang Wen back … about their Southeast Asia deal' — Wen Halvorsen signs Lanternfly's thread (`frederick.stone@harmonygames.co/1842800807116855774`) |
| Framewell | Park to Jan 5 | End: Pro billed from Nov 1 | Leonard's Sep 26 reply: 'Maren called me back about the Pro plan … no charge until Feb 1' (`C07C2866011/1758920520.674991`) — Maren Holt sends Framewell's order form (`frederick.stone@harmonygames.co/1843618067251203081`), and the reply is later |
| Spotlight Fest | Answered by Robert, no second answer | End: say no to the $750 stand fee | Robert's Sep 17 note: the call about the Dec 5 indie showcase, sitting it out, let Rina know (`C07C2866011/1758134460.899858`) — Rina Takeda's invitation is for the Dec 5 indie showcase (`frederick.stone@harmonygames.co/1842712097588195482`) |
| Hootline | in: Park, revisit Jan 5 | out: nothing recent and no filed paper | hub scope has no date limit and counts a sign-up as engagement; Gemma's Aug 12 question is unanswered (`frederick.stone@harmonygames.co/1839631800730308867`) |
| Pingwise | Keep, confirm staying | End (cash test) or Sign (new terms) | keep-running checklist (`689b662c60cbe40b9f4a97ae`); the Team plan continues under the existing agreement, so no new acceptance (`frederick.stone@harmonygames.co/1844157874176168845`) |
| Clipforge | End, cancel in writing by Oct 15 to the notice's address | Park: free through Jan 15 | processor notice Sep 12 for workspace HG-2291 (`frederick.stone@harmonygames.co/1843067564852153540`) is later than the agreement; workspace id is on the agreement and the Jul 14 kickoff (`evt_0a5e42c3aac62434ba2cfc`) |
| Nintendo | Sign: card for Leonard/Arthur, next date Oct 15 | nothing waiting (registration completed) | Arthur's ZOM-567 comment (`cmt_c9a6660d81e067ad1de7`) + ESG (`frederick.stone@harmonygames.co/1844177063117059830`) |
| Markward click-through | Sign: an officer accepts | Frederick accepts it himself (small, free) | ESG Sep 24 'whatever the amount, including click-through terms' + Leonard's Sep 25 reply 'this replaces what I said in July' (`frederick.stone@harmonygames.co/1844177063117059830`) over `C07C2866011/1753207800.603298` |
| Playfuse NDA | Sign card only, no ESG email | also send to ESG | ESG: mutual NDAs on our template need no review (`frederick.stone@harmonygames.co/1844177063117059830`) |
| Kinetic Arcade | ESG email and a card | ESG email only | ESG: anything waiting on a signature gets a card, including the ones sent to us (`frederick.stone@harmonygames.co/1844177063117059830`) |
| Wishwave | End: partner-booked travel counts as cash | Park: we book nothing | Sep 29 amendment (`C07C2866011/1759166100.370044`) later than the doc (`f_b98287f6f80fe431a71209`) |
| Retainly | Park: converts Jan 12, 2026 | End: a trial that converts | the conversion date is outside Oct 1–Dec 31 (guardrails `f_b98287f6f80fe431a71209`) |
| Portal with no person (Nintendo) | no reply, no contact; the card is the action | write to the portal | guardrails: portals and no-reply notices need no answer (`f_b98287f6f80fe431a71209`) |
| Revisit date | Mon Jan 5, 2026 (the review) | any day in the first week of January | Leonard's review event created Sep 29 (`evt_fd469c29811879519c2c96`) |
| Contacts already present | reuse: no new contact | add again | README: add only when missing (`f_846ddc38b2aab3d2ed3fcb`) |

No decision forks on a reported figure; one reading per point (BOTH_FAIR_FIGURE not needed). Dates: every graded date is a plan date (Oct 10, Oct 15, Nov 1, Jan 5) with the same PT and UTC day.

### Reach table (load-bearing records)

Base records, `persona_view.py can-see frederick_stone …` (verbatim, `00_PreScenario/cansee_anchors.txt`):

- frederick_stone gmail frederick.stone@harmonygames.co/1840501641217286806: YES
- frederick_stone gmail frederick.stone@harmonygames.co/1842348778705877030: YES
- frederick_stone gmail frederick.stone@harmonygames.co/1817715521687421486: YES
- frederick_stone gmail frederick.stone@harmonygames.co/1843000993076735547: YES
- frederick_stone gmail frederick.stone@harmonygames.co/1842358947604469113: YES
- frederick_stone gmail frederick.stone@harmonygames.co/1842890197572292911: YES
- frederick_stone gmail frederick.stone@harmonygames.co/1837914783244638008: YES
- frederick_stone gmail frederick.stone@harmonygames.co/1844214653847908044: YES
- frederick_stone gmail frederick.stone@harmonygames.co/1841636073974841484: YES
- frederick_stone gmail frederick.stone@harmonygames.co/1843473831194478743: YES
- frederick_stone gmail frederick.stone@harmonygames.co/1844166352857573845: YES
- frederick_stone gmail frederick.stone@harmonygames.co/1843553829515378870: YES
- frederick_stone slack C07C2866011/1757961037.465799: YES
- frederick_stone slack C07C2866011/1758739409.488879: YES
- frederick_stone slack C07C2866011/1758739727.864319: YES
- frederick_stone slack C07C2866011/1758739208.041469: YES
- frederick_stone slack C0880U9751A: YES
- frederick_stone slack C08R8CHB0QL: YES
- frederick_stone slack D05S58U4SAK: YES
- frederick_stone gdrive f_af99b76ff4da59a710edba: YES
- frederick_stone gdrive d_175c0d7bc72ed244b944cb: YES
- frederick_stone gdrive f_26e1f9a86761e35049192a: YES

Planned seeds (verified at the injection gate; owner or invitee Frederick): 
- LB `frederick.stone@harmonygames.co/1844732913254784171` (hub_thread)
- LB `frederick.stone@harmonygames.co/1844177063117059830` (esg_thread)
- LB `frederick.stone@harmonygames.co/1843618067251203081` (framewell_thread)
- LB `frederick.stone@harmonygames.co/1844157874176168845` (pingwise_thread)
- LB `frederick.stone@harmonygames.co/1843067564852153540` (clipforge_notice_thread)
- LB `frederick.stone@harmonygames.co/1835288808653226583` (pixel_thread)
- LB `frederick.stone@harmonygames.co/1842800807116855774` (lanternfly_thread)
- LB `f_b98287f6f80fe431a71209` (guardrails_doc)
- LB `f_846ddc38b2aab3d2ed3fcb` (readme_doc)
- LB `f_05f0a451b29b19a1c0b90f` (template_sheet)
- LB `f_3b06917a41dd59308d890b` (esg_checklist_doc)
- LB `f_5dbbaf5b251d5261427eb1` (lanternfly_deck)
- LB `d_80a8c04753ba82ba4ba6a5` (q4_folder)
- LB `evt_fd469c29811879519c2c96` (review_event)
- LB `evt_0a5e42c3aac62434ba2cfc` (clipforge_kickoff)
- LB `evt_564a16d0f5f6598d0360d5` (spotlight_call)
- LB `C07C2866011/1759166100.370044` (amendment_root)
- LB `C07C2866011/1758920520.674991` (framewell_waiver_reply)
- LB `D05S58U4SAK/1759174260.052645` (lanternfly_dm)
- LB `C07C2866011/1758134460.899858` (spotlight_note)
- LB `frederick.stone@harmonygames.co/1842712097588195482` (spotlight_thread)
- LB `frederick.stone@harmonygames.co/1839631800730308867` (hootline_thread)

Unscoped load-bearing records: Trello `689b662c60cbe40b9f4a97ae` (board `640643a3fd8f3ca308d9318e`), Linear ZOM-567 and `cmt_c9a6660d81e067ad1de7`, Contacts `9b0185e445572aeee9f27d35`.

**Feasibility.** Every write exists in `Evals/references/tools/catalog.json` (`gmail_reply_to_message`, `gmail_send_message`, `gcal_create_event`, `contacts_add_new_contact`, `trello_create_card`, `gsheets_create_spreadsheet`, `gsheets_values_update`, `gdrive_move_file`); Frederick owns the folder `d_80a8c04753ba82ba4ba6a5` and his calendar; Trello and Contacts are unscoped. **Precedence.** Load-bearing facts sit in ● carriers (mail bodies, Docs/Slides bodies, Slack messages, Linear comments, Trello checklist, calendar descriptions of events Frederick attends), never only in an attachment. **Naturalness.** The prompt names Leonard's email and the folder; it never names companies, rules, decisions, authorities or locations of evidence. **Grading devices.** ≤ 5 samples per group (decision, next date, answered by, told) plus the membership volume row; exclusions graded as the exact log membership, never as leave-alone rows.

### Coherence rail

Every 1a row is dispositioned; every designed disagreement is a dated human claim overturned by a named later record (T2 `C07C2866011/1758920520.674991`, T5 `frederick.stone@harmonygames.co/1843067564852153540`, T7 `frederick.stone@harmonygames.co/1844177063117059830`, T8 `evt_fd469c29811879519c2c96`, T9 `C07C2866011/1759166100.370044`); no system field is modified. Companions are planned in §11.

## 11 Record plan for /create-injection

| Record | Service · table | Planned id | Time (UTC) | Author | Content (planned) |
|---|---|---|---|---|---|
| hub | gmail · gmail_messages/threads | frederick.stone@harmonygames.co/1844732913254784171 | 2025-09-30T23:20:00Z | Leonard → Frederick | the backlog handoff: 'anyone outside the investor work who has an offer, a trial, a quote, terms or an ask in front of us and that one of us has actually engaged with'; 'Cold pitches nobody answered, including ones we only forwarded around internally, stay off it'; 'Go by the runway guardrails doc for what we do with each one'; 'plus the one change I posted in #executives on Monday'; 'Anything that needs signing goes the way ESG's note about signing says'; 'Everyone who is waiting to hear from us should get a written answer this week'; 'Get each company's contact into Contacts so we're not digging through mail next time'; 'the README in the folder has the columns'; 'reply here with what we're keeping and what's waiting on Arthur or me to sign' |
| guardrails doc | gdocs · docs_documents + gdrive · drive_files | f_b98287f6f80fe431a71209 | 2025-09-26T16:00:00Z | Leonard (shared Robert, Arthur, Frederick) | decisions top to bottom; cash window Oct 1–Dec 31 PT incl. trial conversions; 'anything on Arthur's keep-running list on our board stays'; travel counts only when we book it; portals and no-reply notices need no answer; already answered → log who and when, revisit if 'later'; park 'comes back at the January commitments review on our calendars' (first week of January) |
| UA-buckets doc (H1 decoy) | gdocs + gdrive | f_7bacf15c4e8eea1a52dcd4 | 2025-09-16T17:00:00Z | Frederick | fundraising bucket vs real UA bucket for ad-network spend (scope: UA) |
| ESG signing note + Leonard's reply | gmail (Frederick, Leonard, Robert, Arthur copies) | frederick.stone@harmonygames.co/1844177063117059830 | 2025-09-24T20:05:00Z / 2025-09-25T16:30:00Z | PERSON_2694 → founders; Leonard | only Leonard or Arthur accept terms, whatever the amount, including click-through and portal NDAs; auto-renewal, exclusivity, IP licence or > 12 months → 'our intake address (it's in your Contacts as ESG Law intake)', one email per agreement; 'what to include is in the intake checklist I shared'; mutual NDAs on our template need no review; 'put it on your founders' board To Do list with the company's name in the card title', including the ones sent to us · reply: 'Agreed. This replaces what I said in July about Fred signing small stuff himself.' |
| ESG intake checklist | gdocs + gdrive (owner PERSON_2694, shared founders) | f_3b06917a41dd59308d890b | 2025-09-24T19:40:00Z | PERSON_2694 | per agreement: counterparty, what it is, term, renewal, cost, who signs |
| ESG Law intake contact | contacts · contacts | 9b0185e445572aeee9f27d35 | — | — | ESG Law intake, email PERSON_2599_EMAIL (base token) |
| July signing note (superseded) | slack · slack_messages | C07C2866011/1753207800.603298 | 2025-07-22T18:10:00Z | Leonard | for small stuff under $500 a year Fred can accept the terms himself |
| Robert's cancel-everything post | slack | C07C2866011/1758819840.884370 | 2025-09-25T17:04:00Z | Robert | honestly just cancel every marketing tool, all of it |
| travel amendment (root) | slack | C07C2866011/1759166100.370044 | 2025-09-29T17:15:00Z | Leonard | one change to the guardrails: travel and event costs count as cash even when a partner books them |
| Framewell waiver (reply under Playtestcloud root; rev4 wording) | slack (+ root counter UPDATE) | C07C2866011/1758920520.674991 | 2025-09-26T21:02:00Z | Leonard | 'side note, Maren called me back about the Pro plan. they'll hold it at no charge until Feb 1 with nothing to sign before then, so nothing from them lands before January. treat them like the other free ones' (no 'Framewell', no 'vendor') |
| Lanternfly answer (rev4: DM thread reply under D05S58U4SAK/1758151772.570449) | slack (+ DM root counter UPDATE) | D05S58U4SAK/1759174260.052645 | 2025-09-29T19:31:00Z | Leonard → Frederick | 'on localization: I rang Wen back on Saturday about their Southeast Asia deal and let them know Southeast Asia has to wait until after the raise. we'll pick it up again in January' (no 'Lanternfly', no 'told') |
| Robert's Spotlight note (rev4 wording) | slack | C07C2866011/1758134460.899858 | 2025-09-17T18:41:00Z | Robert | 'had the call about the Dec 5 indie showcase. we're sitting this one out this year, I let Rina know' (no 'Spotlight', no 'told', no 'booth') |
| keep-running card | trello · cards/checklists/check_items/actions | 689b662c60cbe40b9f4a97ae | 2025-08-12T16:05:00Z | Arthur | Doing list; checklist: Vaultline nightly DB backups · Certwell SSL for the API domain · the night pager for backend outages (whatever wakes me at 3am) · App Store and Play developer accounts |
| ZOM-567 + comment | linear · issues/comments | ZOM-567 / cmt_c9a6660d81e067ad1de7 | 2025-09-23T17:00:00Z / 2025-09-25T18:20:00Z | Arthur (no assignee) | 'Switch: order dev kits' · comment: can't order kits, the org account stays limited until a company officer accepts the Global ToS and NDA from their own login; Fred's sign-up doesn't count; the request lapses Oct 15 |
| Jan 5 commitments review | gcal · events (one copy per attendee) | evt_fd469c29811879519c2c96 | 2025-09-29T18:00:00Z | Leonard (attendees founders) | Mon Jan 5, 2026 09:00 PT: everything we parked comes back here |
| Clipforge kickoff | gcal | evt_0a5e42c3aac62434ba2cfc | 2025-07-14T16:00:00Z | Priya Raman (Frederick invited) | UGC Studio kickoff — workspace HG-2291 |
| Spotlight Fest call | gcal | evt_564a16d0f5f6598d0360d5 | 2025-09-17T18:00:00Z | Robert (Frederick invited) | rev4 description: 'Showcase slot call with Rina.' (no answer) |
| Hootline thread (rev4) | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1839631800730308867 | 2025-08-05T16:00:00Z / 2025-08-12T16:30:00Z | Gemma Doyle | Aug 5 welcome (promo free until Jan 31, then $39/month) · Aug 12: 'Hi Frederick, now that your profiles are set up, a quick planning question: when the startup promo ends on Jan 31, would you like to keep the scheduler after that? Gemma'; the filed paper is dropped (terms in the body) |
| Q4 commitments folder | gdrive · drive_files (owner Frederick, shared Leonard as writer) | d_80a8c04753ba82ba4ba6a5 | 2025-09-29T20:00:00Z | Frederick | destination |
| folder README | gdocs + gdrive (in the folder) | f_846ddc38b2aab3d2ed3fcb | 2025-09-30T22:40:00Z | Leonard | columns Company · Contact · What's waiting · Decision · Answered by · What we told them · Next date; Next date = End: the last day to cancel or say no · Park and 'later' answers: the January review · Keep: when it next bills · Sign: the date they need it by, if any; contacts: company in the job field, add only when missing; 'copy the header row from the template sheet' |
| log template | gsheets + gdrive (in the folder) | f_05f0a451b29b19a1c0b90f | 2025-09-30T22:45:00Z | Leonard | header row only |
| July vendor tracker (stale) | gsheets + gdrive (owner Frederick) | f_9d6edd4922d8130ccd272e | 2025-07-31T21:00:00Z | Frederick | 19 offers as of Jul 31 (D04 lookalike of the template) |
| Clipforge processor notice | gmail (sender billing@paylane.io) | frederick.stone@harmonygames.co/1843067564852153540 | 2025-09-12T14:10:00Z | Paylane on behalf of workspace HG-2291 (UGC Studio) | pilot cap reached: pilot ends Oct 15; $1,800/month from Oct 16 unless cancelled in writing to billing@paylane.io |
| Ascendo thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822660725 | 2025-08..09 (dated per member) | Lucia Ferrer <lucia@ascendo.agency> | ASO agency retainer: paper: $900/month from Oct 1 |
| Benchmarkly thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918823264696 | 2025-08..09 (dated per member) | Clara Weiss <clara@benchmarkly.com> | benchmark report subscription: paper: free sample now, paid from February |
| Brightlane Studio thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918823246290 | 2025-08..09 (dated per member) | Ines Varga <ines@brightlane.studio> | creative agency retainer: paper: $3,500/month from Oct 1 |
| Bundlehouse thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822843130 | 2025-08..09 (dated per member) | Freya Olsen <freya@bundlehouse.gg> | co-marketing bundle (licenses our game IP): free; licence of our IP -> ESG first |
| Certwell thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822570126 | 2025-08..09 (dated per member) | Jonas Weber <jonas@certwell.com> | SSL certificate for the API domain: renews Oct 20 at $89/year; on Arthur's keep-running list by name |
| Clipforge thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1837102635418059486 | 2025-07-08T18:00:00Z | Priya Raman <priya@clipforge.co> | UGC video ad pilot: pilot agreement (Jul 14): free through Jan 15, 2026; processor notice (Sep 12) for workspace HG-2291 'UGC Studio': pilot cap reached, pilot ends Oct 15, $1,800/month from Oct 16 unless cancelled in writing to the address in the notice -> End, cancel by Oct 15 |
| Cloudlark thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918823282996 | 2025-08..09 (dated per member) | Yara Nasser <yara@cloudlark.io> | startup credits offer: paper: credits, no term, start any time |
| Driftwood Audio thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918823229064 | 2025-08..09 (dated per member) | Sofia Marin <sofia@driftwood.audio> | voice-over studio quote: paper: quote valid until Feb 28 |
| Echohall thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822844975 | 2025-08..09 (dated per member) | Bruno Costa <bruno@echohall.chat> | community platform upgrade proposal: paper: free plan continues |
| Framewell thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1843618067251203081 | 2025-09-18T16:00:00Z | Maren Holt <maren@framewell.io> | creative asset subscription: order form: Pro plan billed from Nov 1 at $149/month; Leonard's Sep 26 thread reply under the Playtestcloud post (rev4: names Maren and the Pro plan, not Framewell): no charge until Feb 1 -> nothing before January |
| Glyphworks thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822719345 | 2025-08..09 (dated per member) | Tomas Novotny <tomas@glyphworks.type> | font licence quote: paper: quote valid to Jan 31, nothing owed until ordered |
| Hootline thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918823108867 | 2025-08-05T16:00:00Z | Gemma Doyle <gemma@hootline.co> | social scheduler: Frederick signed up Aug 5 (promo keeps the scheduler free until Jan 31, then $39/month); Gemma's Aug 12 question whether to keep it after Jan 31 is unanswered; no filed paper and nothing after Aug 12 -> in scope by the hub's undated rule, Park |
| Kinetic Arcade thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822683445 | 2025-08..09 (dated per member) | Noor Haddad <noor@kineticarcade.com> | publishing LOI (12-month exclusivity): free in window; exclusivity -> ESG first; officer signs |
| Lanternfly Publishing thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842800807116855774 | 2025-09-09T15:30:00Z | Wen Halvorsen <wen@lanternfly.games> | Southeast Asia publishing proposal: Frederick replied Sep 10 ('thanks, we'll take a look'); Lanternfly's Sep 22 'any news?' sits unanswered in the thread; Leonard's Sep 29 reply in the DM thread under his Sep 17 'we have no localization though' (rev4: names Wen and the Southeast Asia deal, not Lanternfly): he rang Wen back on Saturday, Southeast Asia waits until after the raise, talk again in January |
| Lingora thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918823022611 | 2025-08..09 (dated per member) | Elena Petrova <elena@lingora.com> | store-listing localization sprint: paper: $2,640 invoiced on delivery; quote valid until Oct 3 |
| Loopnote thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822809477 | 2025-08..09 (dated per member) | Pavel Sokol <pavel@loopnote.app> | meeting-notes tool trial: paper: trial free until Feb 1 |
| Lumencloud thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918823344282 | 2025-08..09 (dated per member) | Aiden Clarke <aiden@lumencloud.dev> | cloud credits programme (36-month term): free; 36-month term -> ESG first |
| Markward thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822569659 | 2025-08..09 (dated per member) | Leah Brennan <leah@markward.io> | brand-monitoring free tier (click-through terms): free; click-through terms = an officer accepts (ESG overrides Leonard's July note) |
| Motive Forge thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1843346276352084348 | 2025-08..09 (dated per member) | Hugo Lambert <hugo@motiveforge.art> | outsourced art quote: Arthur declined in-thread on Sep 19 (cc Frederick) |
| Orbit Store thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918823114020 | 2025-08..09 (dated per member) | Mateo Rossi <mateo@orbitstore.games> | store featuring agreement: free; needs an officer's acceptance |
| Panelpulse thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918823125809 | 2025-08..09 (dated per member) | Arjun Shah <arjun@panelpulse.io> | player research panel: paper: $1,200 prepaid for an Oct 14 panel; confirm by Oct 6 |
| Pingwise thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1844157874176168845 | 2025-09-24T15:00:00Z | Dana Whitfield <dana@pingwise.io> | uptime monitoring and on-call paging: free tier ends Oct 31, Team $29/month from Nov 1 (cash in window); Arthur's keep-running list names 'the night pager for backend outages' -> Pingwise's on-call paging -> Keep |
| Pixel Harbor Events thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1835288808653226583 | 2025-06-18T17:30:00Z | Teodor Lind <teodor@pixelharbor.events> | booth at the Oct 24 indie showcase: June 18 quote (outside the September window): booth hold needs a $2,400 deposit by Oct 10 -> cash in window -> End |
| Playfuse thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822710750 | 2025-08..09 (dated per member) | Iris Navarro <iris@playfuse.gg> | bundle partnership NDA (ESG mutual template): mutual NDA on ESG's template: an officer signs, no counsel review |
| Pressbeam thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822665921 | 2025-08..09 (dated per member) | Ava Lindqvist <ava@pressbeam.news> | PR distribution package for 2026: paper: booked later; no travel |
| Quillcraft thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918823056494 | 2025-08..09 (dated per member) | Nadia Petrov <nadia@quillcraft.ai> | AI copywriting tool beta: paper: free beta through January |
| Retainly thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822469546 | 2025-08..09 (dated per member) | Omar Farouk <omar@retainly.io> | analytics trial: paper: trial converts Jan 12, 2026 (outside the window) |
| Reviewly thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918823312354 | 2025-08..09 (dated per member) | Hana Kobayashi <hana@reviewly.app> | store-review management trial: paper: trial converts Oct 20 at $79/month |
| Soundvault thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822876669 | 2025-08..09 (dated per member) | Rafael Moreno <rafael@soundvault.fm> | music licence (annual): paper: $1,188 prepaid on signature; quote valid to Oct 15 |
| Spotlight Fest thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842712097588195482 | 2025-08..09 (dated per member) | Rina Takeda <rina@spotlightfest.events> | showcase slot invitation: Robert's Sep 17 #executives note (rev4: names the Dec 5 indie showcase and Rina, not Spotlight Fest; the call's calendar description no longer carries the answer): sitting this one out, he let Rina know |
| Streamcast Talent thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822493279 | 2025-08..09 (dated per member) | Kofi Mensah <kofi@streamcast.tv> | influencer campaign: paper: 50% deposit on booking for a November campaign |
| Tilecast thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822553499 | 2025-08..09 (dated per member) | Kenji Mori <kenji@tilecast.io> | website playable-preview widget: paper: free pilot slot in February |
| Vaultline thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822684538 | 2025-08..09 (dated per member) | Mila Novak <mila@vaultline.io> | nightly database backups: renews Oct 12 at $19/month; on Arthur's keep-running list by name |
| Wishwave thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918823227760 | 2025-08..09 (dated per member) | Sven Aalto <sven@wishwave.gg> | pre-registration push at a partner showcase: paper: partner-booked travel for two (counts under the Sep 29 amendment); confirm by Oct 17 |
| Ascendo paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_a9593b0bf23b760e2972c7 | same day as its thread | Lucia Ferrer | terms: $900/month from Oct 1 |
| Benchmarkly paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_e916ab7563891481ab3b16 | same day as its thread | Clara Weiss | terms: paper: free sample now, paid from February |
| Brightlane Studio paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_9d4639f91c93478d888f4b | same day as its thread | Ines Varga | terms: $3,500/month from Oct 1 |
| Bundlehouse paper | gslides + gdrive (owner the counterparty, shared with Frederick) | f_9d1e0270574584de0eb92c | same day as its thread | Freya Olsen | terms: free; licence of our IP -> ESG first |
| Certwell paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_cfb172dea30b9f6ac8a340 | same day as its thread | Jonas Weber | terms: $89/year |
| Clipforge paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_8d0e0e3ae076b2f745e7e2 | same day as its thread | Priya Raman | terms: $1,800/month from Oct 16 |
| Cloudlark paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_eb94c65ce9f273c6b5a579 | same day as its thread | Yara Nasser | terms: paper: credits, no term, start any time |
| Driftwood Audio paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_17878d7b82fafcee79bfe7 | same day as its thread | Sofia Marin | terms: paper: quote valid until Feb 28 |
| Echohall paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_68e288146ba0eee9fc17fa | same day as its thread | Bruno Costa | terms: paper: free plan continues |
| Framewell paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_fba21c2d5d4bbb02983961 | same day as its thread | Maren Holt | terms: order form: Pro plan billed from Nov 1 at $149/month; Leonard's Sep 26 thread reply under the Playtestcloud post (rev4:  |
| Glyphworks paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_f6701704e5659b05d9530f | same day as its thread | Tomas Novotny | terms: paper: quote valid to Jan 31, nothing owed until ordered |
| Kinetic Arcade paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_6252955f500f81e3aacbef | same day as its thread | Noor Haddad | terms: free in window; exclusivity -> ESG first; officer signs |
| Lanternfly Publishing paper | gslides + gdrive (owner the counterparty, shared with Frederick) | f_5dbbaf5b251d5261427eb1 | same day as its thread | Wen Halvorsen | terms: Frederick replied Sep 10 ('thanks, we'll take a look'); Lanternfly's Sep 22 'any news?' sits unanswered in the thread; L |
| Lingora paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_34ba4ac9a0f0fa4fd34e9e | same day as its thread | Elena Petrova | terms: $2,640 invoiced on delivery; quote valid until Oct 3 |
| Loopnote paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_6963d4d30aceef4f88966a | same day as its thread | Pavel Sokol | terms: paper: trial free until Feb 1 |
| Lumencloud paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_a227b14f03e12005fe8324 | same day as its thread | Aiden Clarke | terms: free; 36-month term -> ESG first |
| Markward paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_71a95593c736b3baf45f91 | same day as its thread | Leah Brennan | terms: free; click-through terms = an officer accepts (ESG overrides Leonard's July note) |
| Motive Forge paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_e81c6ef89513cac632700a | same day as its thread | Hugo Lambert | terms: Arthur declined in-thread on Sep 19 (cc Frederick) |
| Orbit Store paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_2ae7e3ee3220b628391234 | same day as its thread | Mateo Rossi | terms: free; needs an officer's acceptance |
| Panelpulse paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_41a9ea5036a231989745b2 | same day as its thread | Arjun Shah | terms: $1,200 prepaid for an Oct 14 panel; confirm by Oct 6 |
| Pingwise paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_6c212cbfb31c3ded44ef8a | same day as its thread | Dana Whitfield | terms: $29/month from Nov 1 |
| Pixel Harbor Events paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_614f88a28a2f0cf1b88408 | same day as its thread | Teodor Lind | terms: $2,400 deposit by Oct 10 |
| Playfuse paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_9a7fc4a3e45e4394227fa5 | same day as its thread | Iris Navarro | terms: mutual NDA on ESG's template: an officer signs, no counsel review |
| Pressbeam paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_a9bb79c86b8b7b92083785 | same day as its thread | Ava Lindqvist | terms: paper: booked later; no travel |
| Quillcraft paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_af809bf6325b452edc8476 | same day as its thread | Nadia Petrov | terms: paper: free beta through January |
| Retainly paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_be21bac5d50e291ebfbe2b | same day as its thread | Omar Farouk | terms: paper: trial converts Jan 12, 2026 (outside the window) |
| Reviewly paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_4bdfb8e0c47288087c7bba | same day as its thread | Hana Kobayashi | terms: trial converts Oct 20 at $79/month |
| Soundvault paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_2686da1086bfcc2fba3f57 | same day as its thread | Rafael Moreno | terms: $1,188 prepaid on signature; quote valid to Oct 15 |
| Spotlight Fest paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_9d9cf4e53b1c8607f9c869 | same day as its thread | Rina Takeda | terms: Robert's Sep 17 #executives note (rev4: names the Dec 5 indie showcase and Rina, not Spotlight Fest; the call's calendar |
| Streamcast Talent paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_5b961c9c6887d31dcd2ee2 | same day as its thread | Kofi Mensah | terms: 50% deposit on booking for a November campaign |
| Tilecast paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_6d13a63be892a29f796b78 | same day as its thread | Kenji Mori | terms: paper: free pilot slot in February |
| Vaultline paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_2715771ae5f0358ad39aa9 | same day as its thread | Mila Novak | terms: $19/month |
| Wishwave paper | gdocs + gdrive (owner the counterparty, shared with Frederick) | f_54c2b4e172bb73a4a19845 | same day as its thread | Sven Aalto | terms: partner-booked travel for two (counts under the Sep 29 amendment); confirm by Oct 17 |

Existing contacts seeded: Kinetic Arcade (Noor Haddad), Lumencloud (Aiden Clarke), Markward (Leah Brennan), company in the job field (`a6ebc7683d450b0017b8acf3`, `35a52a2e3c634972639806b5`, `8a7605bdc08105137d87f5a7`).

### Integrations and companions

Companions from `references/universe_kb/by_universe/synthcut/integrations.json`:

| Service | INT id | Companion | Decision |
|---|---|---|---|
| gcal | INT-11 | invitation / update mails for `evt_fd469c29811879519c2c96`, `evt_0a5e42c3aac62434ba2cfc`, `evt_564a16d0f5f6598d0360d5` in each attendee mailbox | seed them (one GCal copy per attendee calendar too) |
| gdrive | INT-13 | Google Drive Slack app DMs for shares | integration_exceptions: shares of `f_b98287f6f80fe431a71209`, `f_846ddc38b2aab3d2ed3fcb` and the papers are mirrored only in drive sharing rows (no Drive-app DM), declared at injection |
| linear | INT-03, INT-04, INT-05 | linear[bot] PR comment (no PR exists: none); Slack DM notifications (ZOM-567 has no assignee or subscriber: none); unread-notification digests | INT-03/04: none; INT-05: declared exception for ZOM-567's comment |
| slack | INT-22 | '[Slack] … sent you a message' mail for the DM thread reply `D05S58U4SAK/1759174260.052645` | seed the notification mail in Frederick's mailbox or declare it; decided at injection with base_check (the rev3 decision carries over) |
| trello | INT-21 | Trello → Slack: no integration exists | none |
| gmail | — | no INT source maps to gmail itself | none |
| gdocs / gsheets / gslides | INT-13 (google_drive) | as gdrive | as gdrive |
| contacts | — | no integration | none |

## 12 Self-test results

`hardness_gate.py 01_Hardness_Manifest.draft.json --design` (verbatim):

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
  [ok] ask_fragments: 14 fragments; need ≥ 12
  [ok] ask_fragment_services: 7 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 10 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 10 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 46; need ≥ 40 (source-defined: True)
  [ok] evidence_surfaces: 4 surfaces over 4 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 99; need ≥ 90
  [ok] call_budget: unconditional (verified) floor 236 of 236 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 200 (requester-confirmed volume_exception)
  [ok] call_budget_spread: 10 services in budget; largest share outside the per-record phase 37% (≤ 50%)
  [ok] traps: 20 traps across 7 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 6 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 5 supersessions (5 with versions in ≥ 2 services, 1 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: skipped (--design: no SQL yet)
  [ok] distractors: 8 distractors of 6 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 8 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 8 chains with 6 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] mechanism_portfolio: 10 portfolio entries, each a mechanism-enum id with trap/chain nodes, a requirement, a natural-reading fallback and a prior family with its reason
  [ok] artifact_fields: declared ['gradable_surface']: paths relative, digests sha256
  [ok] hidden_authorities: 3 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 2 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 18 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 10 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 6 writes over 5 services; each must depend on findings
  [note] volume_exception: call-budget floor 200 and per-record floor 90 replace 500 and 300; every other extreme target applies — reason: the cohort is 46 real companies (36 in scope); mail and calendar are bulk-readab; requester confirmation: task author in chat on 2026-11-03 set the horizon target at 'over 130 tool calls
```

`gradable_surface.py validate` and `gradeable-report` (verbatim):

```
GRADABLE SURFACE (01_Gradable_Surface.json): PASS · 34 slots · weight 138 · mechanism share 83.3% (reported, not gated) · weight by class {'direct': 66, 'write_content': 67, 'delivery': 5}
SURFACE.GRADEABLE PASS · 34 slot(s) · {'GRADABLE': 34}
```

`hardness_v2_check.py --design` (verbatim; dispositions in §5 Liveness flags):

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  FLAG       SAME_PLACE      5 trap(s) with two or more version records; 1 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 5 requirements: {'R6': ['DONE', 'SIGN'], 'R2': ['CORR', 'DATE', 'AMEND'], 'R4': ['COMPL', 'NOTE'], 'R3': ['EXC'], 'R1': ['FILT', 'WIN']}  [Part 5 rule 1]
  FLAG       DECISION_FLIP   8 of 10 rules can flip a weight-5 slot; not: ['SIGN', 'AMEND']  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     0 weight-5 total(s); 0 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  CLEAN      RULE_IN_PROMPT  no run of 8 resolver words in the prompt  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']

Flags (each needs a written disposition; redesign the difficulty, never weaken a fairness link or raise a weight):
  SAME_PLACE T7 (same_container): the correction and a superseded version share gmail:1844177063117059830
  DECISION_FLIP SIGN: rule SIGN (A12) can flip slots of weight [3], no weight-5 slot
  DECISION_FLIP AMEND: rule AMEND (A15) can flip slots of weight [3], no weight-5 slot
```

S9b prior forecast (UNCALIBRATED, advisory, pre-registered): ledger id `hev_da8a164703569b79`; mechanism rates are disclosed overrides sourced from the completed Frederick tasks.

```
  V3: P(all four difficulty gates) 0.284-0.559 across scenarios; value of information (first scenario): ['rule:DONE', 'rule:CORR', 'rule:COMPL']
  correlated  whole    V3 E[avg] 0.654 [0.524, 0.798] P(all) 0.284
  independent whole    V3 E[avg] 0.655 [0.591, 0.719] P(all) 0.559
  source      whole    V3 E[avg] 0.655 [0.591, 0.719] P(all) 0.559
```

**Lazy-solver pass.** One broad search per service, first hits, no thread opens, stop at the first conclusion: it reads the hub, the guardrails doc and each company's own thread and paper → loses DONE, CORR, COMPL, EXC (no checklist join), DATE (notice not returned by name), FILT (September window) → 52.0 % on the surface (`plan/policy_scores_output.txt`). Every point it scores comes from controls; no leak found.

**Literal-value sweep (planned text).** 'Feb 1' appears only in Framewell's waiver reply; 'Oct 15' for Clipforge only in the processor notice; 'night pager' only on the checklist; 'lapses Oct 15' only in the ZOM-567 comment; 'pick it up again in January' for Lanternfly only in the DM thread reply; 'sitting this one out' only in Robert's note. **Wording sweep (rev4).** None of the three moved corrections names its company or uses the rev3 pre-check's search words ('told', 'vendor', 'trial', 'quote', 'booth', 'retainer'; precheck events 386–480); each names the company's own contact (Maren, Wen, Rina) who signs that company's thread, so the alias resolves from a record the persona reads. 'SEA deal', 'indie showcase' and 'Halvorsen' have 0 base hits (hg.py search slack/gmail/contacts); 'Maren' matches only inside 'gsmarena'. **The rest stands.** No later record re-asserts the amended travel clause or the doc's 'first week of January'.

### Self-review

Walked `Evals/1_Prompt_Eval.md` §2.1 (UGT), §2.2 (feasibility), §3.2 (cross-service coherence) and `Evals/0_Injection_Quality_Eval.md` Check C against this design.

| # | Category or decision point | Counter-reading (strongest argument it fails) | Resolution and evidence |
|---|---|---|---|
| 1 | temporal | seeded Sep 30 hub is after the seed bound in PT or UTC | 23:20Z Sep 30 < freeze 2025-10-01T00:00Z; every T value in build_scenario.py T is earlier (`frederick.stone@harmonygames.co/1844732913254784171`) |
| 2 | semantic | 'answered' could mean any reply, so Frederick's Sep 10 'we'll take a look' answers Lanternfly | guardrails define already answered as an answer to what they asked; Leonard's DM gives that answer (`D05S58U4SAK/1759174260.052645`); the follow-up shows 'take a look' was not an answer |
| 3 | cross-service referential | Clipforge's workspace HG-2291 maps to no record the persona can see | the agreement and the Jul 14 kickoff (`evt_0a5e42c3aac62434ba2cfc`) carry HG-2291 and UGC Studio (C5) |
| 4 | quantitative | Leonard's reply under the Playtestcloud root leaves its reply_count stale | hazard Q01 acknowledged; SQL updates the counters (`C07C2866011/1758513190.847889`) |
| 5 | state/lifecycle | ZOM-567 open and assigned to someone quiet in October (L08) | no assignee; creator Arthur; open is its true state at the clock (ZOM-567) |
| 6 | identifier/format | ESG intake address as a token breaks the send | base already uses PERSON_2599_EMAIL as the group address (`frederick.stone@harmonygames.co/1841636073974841484`); the Contacts entry reuses it (`9b0185e445572aeee9f27d35`) |
| 7 | other | seeding 33 vendor relationships never mentioned in base Slack reads as contrived | they are trials, quotes and proposals with no spend history (name census plan/name_census.json); Frederick's base mailbox already holds many such inbound offers (`frederick.stone@harmonygames.co/1843000993076735547`) |
| 8 | Rayking in scope | Frederick's 'Hi …' message makes Rayking engaged | To: leonard.hayes in `frederick.stone@harmonygames.co/1842348778705877030`; the hub excludes pitches only forwarded internally (T18) |
| 9 | Pixel Harbor | June quote is stale and could be ignored | deposit due Oct 10 is still pending and the scope has no date limit (`frederick.stone@harmonygames.co/1835288808653226583`, C6) |
| 10 | Balancy | Leonard's 'we'll circle back' is not an answer, so it needs a reply | it answers the trial offer (`frederick.stone@harmonygames.co/1840501641217286806`); Balancy acknowledged on Sep 15; guardrails: 'later' answers get a revisit |
| 11 | Lanternfly | the DM reply could be about another publisher (it no longer names Lanternfly) | it names Wen and 'their Southeast Asia deal'; Wen Halvorsen signs Lanternfly's Southeast Asia proposal thread (`frederick.stone@harmonygames.co/1842800807116855774`); dated after the Sep 22 follow-up (T3) |
| 12 | Spotlight Fest | Robert's note could be about another showcase (Wishwave's partner showcase) | it names the Dec 5 indie showcase and Rina; Rina Takeda's invitation is for the Dec 5 indie showcase (`frederick.stone@harmonygames.co/1842712097588195482`), Wishwave's is a pre-registration push with Sven (T19) |
| 13 | Hootline | with no paper and nothing after Aug 12 it is a stale sign-up, not something waiting | Gemma's Aug 12 question is unanswered and the promo decision falls at Jan 31; the hub's scope counts a sign-up and has no date limit (`frederick.stone@harmonygames.co/1844732913254784171`, T20) |
| 14 | rev4 rebuild | de-naming the corrections makes them unfair (a reviewer cannot tie Maren or Wen to the company) | each contact signs its own company's thread; the rev3 /prompt review accepted the alias-by-function night pager (run_forensics/rev3/platform_prompt_review.md F7); the blind fork sweep at injection re-checks it |
| 15 | Framewell | 'treat it like the other free ones' could mean Keep | guardrails: free until January → Park (`f_b98287f6f80fe431a71209`); Keep is only for Arthur's list (`689b662c60cbe40b9f4a97ae`) |
| 16 | Pingwise | staying on Team means accepting new paid terms → Sign | the notice says the Team plan continues under the existing agreement unless downgraded (`frederick.stone@harmonygames.co/1844157874176168845`); nothing to accept (T4) |
| 17 | Clipforge | the agreement (free through Jan 15) still governs | the Sep 12 notice is later and reports the cap the agreement allows (`frederick.stone@harmonygames.co/1843067564852153540`, T5 version_records) |
| 18 | Nintendo | Frederick's registration is a sign-up, so it is done | Arthur's comment: org account limited until an officer accepts (`cmt_c9a6660d81e067ad1de7`); ESG: only Leonard or Arthur accept terms (`frederick.stone@harmonygames.co/1844177063117059830`) |
| 19 | Markward | Leonard's July note lets Frederick accept small free terms | ESG's Sep 24 note and Leonard's Sep 25 'this replaces what I said in July' (`frederick.stone@harmonygames.co/1844177063117059830`, T7) |
| 20 | Playfuse | an NDA is legal paper, so it goes to ESG | ESG: mutual NDAs on our template need no review; an officer signs (K5) |
| 21 | Kinetic Arcade | counsel items wait on counsel, not a signature: no card | ESG: anything waiting on a signature gets a card, including the ones sent to us (`frederick.stone@harmonygames.co/1844177063117059830`) |
| 22 | Wishwave | the partner books travel, so the doc's rule parks it | the Sep 29 amendment is later and changes that clause (`C07C2866011/1759166100.370044`, T9) |
| 23 | Retainly | a converting trial should end like Reviewly | Retainly converts Jan 12, 2026, outside Oct 1–Dec 31 (T17) |
| 24 | portal (Nintendo) | everyone waiting gets a written answer, so write to Nintendo | guardrails: portals and no-reply notices need no answer (`f_b98287f6f80fe431a71209`) |
| 25 | revisit date | the doc's 'first week of January' allows any day | Leonard's review event fixes Mon Jan 5 (`evt_fd469c29811879519c2c96`, T8) |
| 26 | contacts present | a duplicate contact is harmless, so the dedupe read is padding | three counterparties exist; README says add only when missing (K8); the lookup changes the result |
| 27 | volume | ~150 calls in a lean run is padding-driven | every read decides or confirms a company's own decision; every write is one per company the hub or an authority asks for (K1, K8, K5); no record exists only for count (§2 necessity) |
| 28 | difficulty | six channels at 0.35–0.50 is optimistic; measured pre-checks missed ~1 of 3 traps | at 0.6× the rates P(all, < 80 %) is 0.48 (`plan/policy_scores_output.txt`); the correlated forecast view is the floor (§12) |
| 29 | HARDNESS GATE output | a PASS at --design proves nothing about the SQL | true: injection re-runs hardness_gate on the SQL with every seeded id; this design PASS covers structure only (§12) |

HARDNESS GATE (design) result is pasted verbatim above. Forecast `hev_da8a164703569b79` is advisory and UNCALIBRATED.

Amendment, 2026-11-03 (found at `/create-injection` S4b, re-certified here): the five "What we told them" slots (X13, X15, C5, C6, C11) use the `reason_matches` selector, which `surface_grader.py` scores by regex against the written reason cell, never against a solver value; `oracle_kit.py` has no solver reading for it, so as class `direct` they failed `contract.slots`. They are now class `write_content` (graded from the written log, like the other written-content slots); weights, keys, groups and mechanisms are unchanged. X15's pattern now keys on the part only Leonard's DM holds (no new publishing deals / before the raise): the old pattern also matched the guardrails' own Park wording ("we'll pick it up in January"), so a run that missed the DM still passed it. The draft manifest is byte-identical (db7e2c16e5a8).

Amendment, 2026-11-04 (`--revise`, design-2): §14 takes in the rev3 pre-check. T2 and T3 are rebuilt (de-named corrections; Lanternfly's answer moves into a DM thread), T19/NOTE (Spotlight) and T20/WIN (Hootline outside the filter) are added, X7 leaves the decision group for X20, X18/X19/X21 are added, and the told/answered-by/next-date matchers are loosened (manifest design_delta). truth.json values do not change.

Unresolved: no independent red-team review of this design (REDTEAM_* unset; fallback in §13); the rev4 landing rates are UNCALIBRATED estimates from one pre-check plus bridge analogs, and the stop rule allows one more pre-check for this scenario; INT-13/INT-05/INT-22 companion choices are decided at injection with base_check.

```
STAGE GATE scenario: PASS — Task_Authoring/task_inputs · 01_Scenario_Design.md#2c09f947100b · 01_Hardness_Manifest.draft.json#84fea705bc87 · 01_Gradable_Surface.json#abd340b2b96e · 00_Assigments.md#5418f950517f · __context__#db8af19cc1c3 · __assignment__#b196657eace0 · __policy__#dc4ab5df3cdd · __gate_policy__#115714063000 · __review__#f8ef1e723697 · blocking 0 · warnings 0 · checks 36
[PASS] assignment.v3_context: Frederick Stone / Co-founder; easy cap <90%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 3 output(s) present: 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json
[PASS] structure.inputs: 1 input(s) present: 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md)
[PASS] structure.sections: 19 required sections present and non-empty (01_Scenario_Design.md)
[PASS] structure.placeholders: no placeholders in 01_Scenario_Design.md
[PASS] evidence.storyline: 6/6 items carry a source pointer (min 80%)
[PASS] evidence.coherence_audit: 20/20 items carry a source pointer (min 100%)
[PASS] evidence.hidden_authorities: 3/3 items carry a source pointer (min 100%)
[PASS] evidence.delegation: 18/18 items carry a source pointer (min 90%)
[PASS] evidence.trap_register: 52/56 items carry a source pointer (min 90%); unsourced e.g. L335: "T17 | distractor (near_duplicate_record) | `retainly-terms` | R2 | Retainly's trial conver"
[PASS] evidence.record_plan: 96/98 items carry a source pointer (min 80%); unsourced e.g. L716: 'gmail | — | no INT source maps to gmail itself | none'
[PASS] evidence.active_speakers: 6/6 items carry a source pointer (min 100%)
[PASS] tool.hardness_gate_design: hardness_gate --design pasted PASS; re-run PASS
[PASS] tool.persona_reach: persona_view reach pasted for frederick.stone@harmonygames.co and matches the re-run (105 channels)
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] kb.coherence_hazards: coherence audit cites 11 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 4 speaker rows carry their activity.json status_at_clock
[PASS] kb.integrations: companions listed per integrations.json (7 INT ids, services ['contacts', 'gcal', 'gdocs', 'gdrive', 'gmail', 'gsheets', 'gslides', 'linear', 'slack', 'trello'])
[PASS] kb.storyline: timeline cited; cohorts []; trap_catalog ['B02', 'C01', 'D04', 'P01']
[PASS] boundary.anchor_naming: 4 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] tool.redteam_dual: red team did not run (missing 01b_Redteam_Review.md, 01b_Redteam_Review.second.md); explicit fallback recorded: Claude (Opus 5.5) self-review only, plus (for design-2) the rev3 platform Opus 5.5 pre-che
[PASS] surface.valid: 34 slots, weight 138; geometry report-only, never gated: mechanism share 83%, always-pass share 17%
[PASS] forecast.preregistered: prior forecast pre-registered in the ledger: ['hev_02816c7ce07c1dbb', 'hev_da8a164703569b79'] (UNCALIBRATED, advisory)
[PASS] revise.intake: revision intake consumes run_forensics/rev3/precheck.node_verdicts.json
[PASS] revise.verdict_dispositions: 8 proposed node verdict(s) dispositioned; 2 CONFOUNDED candidate(s) addressed
[PASS] revise.revision_binding: every export is bound on evidence to the revision it ran on, or marked historical (historical evidence never certifies a revision)
[PASS] evidence.register_run_step: 8/8 items carry a source pointer (min 100%)
[PASS] reach.scenario: 46 scoped load-bearing ids YES for frederick_stone (36 planned seeds not yet in base: verified at the injection gate)
[PASS] review.counter_readings: 29 evidenced counter-readings (of 29 found; need ≥ 25) in 01_Scenario_Design.md
[PASS] review.coverage: self-review addresses all 8 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.draft.json is bound to the current assignment, policy, source context and freeze
[PASS] v3.role_review: current role-plausibility review recorded; semantic judgment belongs to the named reviewer
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## 13 Red team (dual)

RED TEAM UNAVAILABLE: REDTEAM_* is not set in this environment, so `tools/redteam_review.py --mode redteam --dual` cannot reach a reviewer endpoint.

RED TEAM FALLBACK: Claude (Opus 5.5) self-review only, plus (for design-2) the rev3 platform Opus 5.5 pre-check and its /hardness review as independent evidence of where the design leaked (run_forensics/rev3/platform_hardness_review.md) — the counter-reading table in §12, the whole-universe name census with a positive control (`plan/name_census.json`), the id-collision check (`plan/id_checks.json`, positive controls found), the policy scores and the pre-registered forecast. The requester delegated the review choice in chat on 2026-11-03 ('you can choose from your self'). No independent review of this design exists; it stays in every Unresolved line until a review or the Opus pre-check covers it (learnings §44).

## 14 Revision intake (S0r)

Verdicts file consumed: `run_forensics/rev3/precheck.node_verdicts.json` (node_verdicts.py on the rev3 pre-check; dispositioned records `run_forensics/rev3/precheck.dispositioned.jsonl`, ledger ids hev_b8f28a892a74b855 … hev_0791c57922eeb614; report `01a_Hardening_Report.md`).

Export binding: the one export, label `precheck` (`06_PreCheck_Trajectory/trajectory.json`, sha256 d5dc726b6150), is BOUND to rev3 on discriminating content (sql 2176eb708f74; binding basis and seen needles in the verdicts file). It certifies nothing about design-2; rev4 needs its own pre-check.

| Node | Runs | Proposed verdict | Disposition | Evidence |
|---|---|---|---|---|
| DONE | 1 | BYPASSED (dispositioned LANDED) | keep: Nintendo stays as designed; the run never opened the portal mails or Linear | precheck event 66 (Nintendo threads listed, not opened); register write precheck event 533 has no Nintendo row; no Linear call in 265 |
| CORR | 1 | LEAKED (mechanism? pending: Framewell Next date) | rebuild: de-name Leonard's reply (Maren, the Pro plan), keep it under the Playtestcloud root (T2). CONFOUNDED candidate rejected: the flagged value '2026-01-05 (January commitments review)' is the right date (representation), so no tool, fairness, verifier or run cause | precheck event 444 ('Framewell' search) and event 480 ('vendor after:'), thread opened at precheck event 455 |
| COMPL | 1 | LEAKED (mechanism? pending: Lanternfly Answered by) | rebuild: the answer becomes a DM thread reply under Leonard's Sep 17 localization root, naming Wen and the Southeast Asia deal (T3). CONFOUNDED candidate rejected: 'Leonard Hayes, Sep 27 (call)' is the right person (representation) | precheck event 387 ('Lanternfly'), event 426 ('told after:'), DM history newest root at precheck event 428/430 |
| EXC | 1 | LEAKED | keep: the keep-running card is an incorporated authority (guardrails step 3); rate cut to 0.05; X7 leaves the decision group | card opened directly at precheck event 50 |
| DATE | 1 | LEAKED | keep: an incorporated cash-test decision on a swept notice; rate cut to 0.10 | notice in the Aug 15+ listing at precheck event 66, opened at precheck event 187 |
| FILT | 1 | LEAKED | keep Pixel Harbor (its paper and the tracker lead to it); the filter move is rebuilt on Hootline as the new rule WIN (T20) | tracker at precheck event 284, paper at precheck event 296, name search at precheck event 309 |
| SIGN | 1 | LEAKED | keep: on the delegation path by design (the hub names ESG's note); SAME_PLACE T7 accepted | ESG thread opened at precheck event 43 |
| AMEND | 1 | LEAKED | keep: named by the hub (the Monday post) | #executives history read at precheck event 35 |

Controls (7) and channels (6) in the verdicts file are HELD in the dispositioned records; CH-SLIP's flagged slips are representational (the brief's §4b classes) and the loosened matchers (issue_key for Answered by and Next date; wider told patterns) stop the proxy from counting them.

Routing: universe changes → `/create-injection` rev4 (design_delta in the draft manifest); prompt-side defects: none (rev3 /prompt scored 5 on every dimension; `04_Prompt.txt` 32f7ab0cabd6 stays); OE/rubric notes (accept the §4b classes, grade negative writes, require the Priya note) → `/create-oe-writing`, `/create-rubric-writing`; no verifier or all-fail findings (no baseline yet).

