# Scenario Design — frederick_dd_publishing · design only · contains no prompt, OE or criterion text

Written 2026-11-06 by `/create-scenario` (Claude Opus 5.5). Builders: `Working_Files/plan/build_scenario.py` (manifest, surface, ids, planned wording), `plan/assemble_design.py` (this file), `plan/policy_scores.py` (UNCALIBRATED scores). Learnings applied: `00_Pre_Scenario_Analysis.md` §1a (the four completed Frederick tasks) and the root `learnings` file.

## 0 Assignment, persona census and horizon note

| Field | Value |
|---|---|
| Universe | key `synthcut`, label Oct 1, 2025 (synth-cut), `Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)`; seed bound `freeze_utc` 2025-10-01T00:00:00Z (Tue Sep 30 17:00 PT); `shutdown_rules_apply` false; build hg4-synth-sep30cut v16 |
| Assignment | Executive · Frederick Stone (Co-founder, `frederick.stone@harmonygames.co`) · Finance · Analysis and synthesis · long-horizon · medium · October 1, 2025 07:00 (context_hash `ec895c36b5f1`) |
| Evals category | Founders / Exec / Strategy (`Evals/references/rules/task_categories.md`: strategic decisions, pitches, priorities and executive coordination) inside Finance (models, budgets, forecasts) |
| Loss budget | Medium cap < 85 %; requester target < 80 % (`author_targets` in the draft manifest); design target E[avg] ≤ 72 % (requester cap minus 8 points) |
| Horizon | Long Horizon → `effective_profile: extreme`; requester target over 130 counted calls in every run; `volume_exception` call floor 180, per-record floor 60; `cohort_exception` floor 24 (honest budget 203, per-record 69, about 85 single-object writes) |
| Theme screen | Domino Delights is a tile game with no bio-adjacent theme; no seeded text uses one |
| Role remit | Frederick is a co-founder (roster) and Commercial Lead (Contacts `175c0d7bc72ed244b944cb90`). Leonard put the publishing-rights question to him by name on Aug 25 (`C07C2866011/1756140953.197759`), Frederick ran the Appodeal talks (`frederick.stone@harmonygames.co/1830012626042968381`) and opened outreach on Sep 24 (`D05S58U4SAK/1758736827.548589`, `f_10dfa1b4236a7c35dcb632`) |

Persona reach census (`persona_view.py reach frederick_stone --top 40`, verbatim):

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
  C05KNDCHAAG    company-internal                       private mem=38  msgs=4048   2023-07-31..2025-10-01
  C04RYU8TJ8K    random                                 public  mem=32  msgs=3950   2023-03-02..2025-09-29
  C08R27X0EAH    zombie-bugs                            private mem=23  msgs=3830   2025-05-06..2025-09-30
  C04V7N09LE7    god-gameart                            private mem=30  msgs=3744   2023-03-22..2025-07-15
  C06M373FT63    [SOURCE_ORG_0001]-gpt                  public  mem=18  msgs=2775   2024-03-01..2025-09-30
  C08R8CHB0QL    zombie-art                             public  mem=23  msgs=2650   2025-05-06..2025-09-30
  C06DJBJL798    zombie_marketing                       private mem=17  msgs=2045   2024-01-11..2025-09-04
  C05M9QYMZUN    industry-news                          public  mem=19  msgs=1528   2023-08-11..2025-07-15 archived
  C077MTAKNS3    lucky_drop                             private mem=16  msgs=1278   2024-06-13..2025-01-18 archived
  C08R6BF4ENN    zombie-ops                             private mem=22  msgs=1025   2025-05-06..2025-09-15
  C057NHCNF44    ai-art                                 public  mem=16  msgs=1005   2023-05-12..2025-04-09 archived
  C08MCEP1B9B    node-[SOURCE_ORG_0001]-external        private mem=15  msgs=846    2024-09-18..2025-04-09 archived
  C07JYF2CFFU    god-sfx                                private mem=20  msgs=785    2024-08-28..2025-04-18 archived
  C05UY5VN1KL    god-animation                          private mem=21  msgs=705    2023-10-03..2025-01-18 archived
  C1C2137664A3   applovin_[SOURCE_ORG_0001]             public  mem=8   msgs=653    2023-12-18..2025-07-07
  C096HFA5Z8W    bridge-pitch                           private mem=8   msgs=592    2025-07-20..2025-09-28
  C07F4G84XV4    leaderboards                           private mem=14  msgs=588    2024-08-02..2025-04-09 archived
  C07KZG57QKD    ad_monetization                        private mem=14  msgs=514    2024-09-04..2025-04-09 archived
  C7442B7CD94B   mpdm-leonard.hayes--person_r004--rober mpim    mem=4   msgs=506    2024-09-04..2025-09-24
  C061D04GU0K    marketing_partnerships                 private mem=7   msgs=505    2023-10-16..2024-08-07 archived
  C07K74CLNJD    god-monetizationoffers                 private mem=15  msgs=493    2024-08-28..2025-04-09 archived
  C04SNNQ9B5W    general-not-used-actively              public  mem=30  msgs=421    2023-03-02..2025-05-19
  C07ML6RN72M    company-playtest                       private mem=24  msgs=405    2024-09-12..2025-04-10 archived
  C07RBFB9WR3    prototype_striketeam                   private mem=16  msgs=358    2024-10-11..2025-04-09 archived
  C07UCC631A6    adjoe-[SOURCE_ORG_0001]                private mem=18  msgs=358    2024-10-31..2025-09-08
  C076Q0Z5R47    quests                                 public  mem=17  msgs=294    2024-06-07..2025-04-09 archived
  C07GEQTHY0L    playstupidgames                        public  mem=19  msgs=243    2024-08-09..2025-04-18 archived
  C8B75A13B6E5   mpdm-leonard.hayes--marcus.bennett--ro mpim    mem=4   msgs=241    2024-10-21..2025-04-29
  D05SD5QLG94    D05SD5QLG94                            im      mem=5   msgs=241    2023-09-15..2025-09-18
  C3C507EA71D6   mpdm-robert--frederick.stone--leonard. mpim    mem=4   msgs=235    2023-10-25..2025-06-10

GMAIL  mailbox=frederick.stone@harmonygames.co threads=4656 messages=5474 range=2024-06-25..2025-10-01
  threads by last-message month (recent): {'2025-05': 323, '2025-06': 333, '2025-07': 249, '2025-08': 108, '2025-09': 185, '2025-10': 3}
  top correspondents: SVC_0107_EMAIL (1870), SVC_4131_EMAIL (1476), leonard.hayes@harmonygames.co (528), robert@harmonygames.co (337), arthur.blake@harmonygames.co (266), SVC_0521_EMAIL (192), brian.foster@harmonygames.co (102), SVC_0009_EMAIL (91), PERSON_5681_EMAIL (76), PERSON_1294_EMAIL (75), PERSON_1298_EMAIL (72), marcus.bennett@harmonygames.co (63), martin.walsh@harmonygames.co (59), victor.barnes@harmonygames.co (52), julia.lawson@harmonygames.co (51)

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

Identities (`entity.py resolve "Frederick Stone"`): Linear `usr_175c0d7bc72ed244`, Trello `4b4a68fc0fec0b254e4f9d8e`, Confluence `user_EMPLOYEE_0008`, Drive root `d_175c0d7bc72ed244b944cb` (owned). GitHub shows 'Ryan' (hazard S04), and the sync doc lists him as Ryan too: GitHub carries no row.

## 1 Storyline

Leonard asked the founders on Aug 25 whether to give up Domino Delights' mobile publishing rights while keeping code, IP and non-mobile rights (`C07C2866011/1756140953.197759`, `f_26e1f9a86761e35049192a`). The bridge is going badly by Sep 30 (`C07C2866011/1759196260.965849`, `C07C2866011/1759182620.491829`), so he hands Frederick the model: where each publisher stands, what each Live offer brings in over 12 months and in Q4, what the game earns if kept, and which offer goes first. One publisher takes the rights, so offers are compared, never summed. 26 publishers, 7 Live.

- Timeline (`references/universe_kb/by_universe/synthcut/timeline.md`): the window sits after the Sep 3 bridge launch (`C07C2866011/1756749288.785249`) and the Aug 28 sync (`f_26e1f9a86761e35049192a`). No shutdown premise: Leonard's line about closing costs (`C07C2866011/1758739428.647609`) and his Oct 1 banker line (`C07C2866011/1759290197.446099`) are never used.
- cohorts.json: no fit — every KB cohort is a Linear or service record set, and this cohort is outside publishers defined by the rule doc and the outreach sheet (`f_5e355d03f6eb6a4e866ead`, `f_fd467bd2ae0c6d4f3bd2bc`).
- trap_catalog precedents: C01 (thread replies that correct: Arthur's cash note `C07C2866011/1759251900.005166`), B02 (automated senders: Summit's acknowledgement `frederick.stone@harmonygames.co/1842077918822746195`, base Tilting Point `frederick.stone@harmonygames.co/1842443183462721250`), K02 (app-name lineage: Calm Play to Harmony Games, behind the wrong beneficiary on the returned wire; the account is in Harmony Games' name `D05S58U4SAK/1738003879.776129`, and Calm Play never held one `C07C2866011/1727980540.831209`), D03 (deck families: the May one-pager `f_4b3ef3dcf76258a6fda5cd`), P01 (shared first names: no seeded person shares an HG first name, §1c).
- Base anchors Frederick can see: rights position `C07C2866011/1756140953.197759`, the sync `f_26e1f9a86761e35049192a`, his numbers question `D05S58U4SAK/1758735778.095599`, Leonard's organic figure `D05S58U4SAK/1758736747.409459`, the tranche line `D05S58U4SAK/1758736827.548589`, Appodeal `frederick.stone@harmonygames.co/1830012626042968381`, Rayking `frederick.stone@harmonygames.co/1842348778705877030`, the UA/BD board `66da196af476ab78deaa0cef` and its BD Follow Up list `670015c2ecd45b634d5eec81`.
- Natively spans gmail, slack, gdocs, gdrive, trello, snowflake, gcal, gsheets, gslides (9, e.g. `frederick.stone@harmonygames.co/1830012626042968381`, `f_26e1f9a86761e35049192a`, `670015c2ecd45b634d5eec81`, `ANALYTICS.MONETIZATION.REVENUE_DAILY`); injection adds contacts and linear with load-bearing roles (`5373edb55ca853d6052ecce5`, `lc_674982ffdca63f854ec6f591`).

## 1a Coherence audit

Scope = every record a correct run opens. Walked against `references/universe_kb/by_universe/synthcut/coherence_hazards.json` and the known-data-issue cards `references/known_data_issues/synthcut.md`.

| Record | Category | Fields | Pointer | Hazard / card | Disposition |
|---|---|---|---|---|---|
| Rayking thread message order | temporal | message dates | frederick.stone@harmonygames.co/1842348778705877030 | hazard T02 | fold: no seed appended; the run reads dates |
| Seeded threads' date format | identifier/format | date header | frederick.stone@harmonygames.co/1842077918823428620 | hazard I04 | fold: seeded Gmail rows use the RFC-2822 form of their mailbox's neighbours |
| Frederick's mailbox file alias | identifier/format | file name | frederick@harmonygames.co_1842348778705877030.json | hazard I03 | fold: seeded threads follow the frederick@ file alias with frederick.stone@ ids |
| Drive name vs Docs title extension | identifier/format | name | f_10dfa1b4236a7c35dcb632 | hazard I15 | fold: seeded docs keep the same title in Drive and Docs |
| Frederick's GitHub display name | semantic | name | frederick.stone@harmonygames.co/1842359398719557772 | hazard S04 | avoid: GitHub carries no row |
| Seeded calendar events and invitation mails | cross-service referential | summary ±1 day | evt_43fda04cd11b9d58a05161 | hazard R08 | fold: each seeded event gets its INT-11 invitation mail in every attendee mailbox |
| Slack links to Docs | cross-service referential | doc ids in links | C096HFA5Z8W/1758915000.867092 | hazard R04 | avoid: seeded Slack names documents by title, never by link |
| Reply counters on three base roots | quantitative | reply_count / latest_reply | C07C2866011/1757345405.134829 | hazard Q01, Q03 | fold: SQL updates counters on the banker, 70 % D1 and Matthew roots (manifest hazard_acknowledgements Q01, dated_claim) |
| REVENUE_DAILY mirror | quantitative | total_revenue_usd | snowflake.wh_analytics__monetization__revenue_daily | hazard Q09 | fold: the rule doc names one table; V2 mirrors it; the sum is by month, never per network |
| Copies of the ESG note | quantitative | body | frederick.stone@harmonygames.co/1844620296192667598 | hazard Q10 | fold: one identical body per mailbox copy |
| ENG-2362 assignee | state/lifecycle | assignee, state | ENG-2362 | hazard L08 | avoid: assigned to Arthur (active), state Todo; the comment is his own, on an open ticket, so no closed-ticket activity |
| BD Follow Up list on the UA/BD board | state/lifecycle | list / activity | 670015c2ecd45b634d5eec81 | hazard L12 | fold: seeded cards sit in an open list; board dateLastActivity is updated with them |
| DD September installs | quantitative | installs | snowflake.wh_analytics__monetization__revenue_daily | card SC-1 | excluded: no row reads installs from the warehouse; monthly installs are publisher commitments |
| Warehouse revenue against P&L workbooks | quantitative | monthly revenue | f_a5e9fc9c8a3188faf66784 | cards SC-35, SC-3 | excluded: Frederick can open none of the P&L workbooks (persona_view: 12 hidden, the one visible hit is the 4X budget), so a correct run never meets a second figure; the rule doc names the table. No cell-level comparison was made |
| Ad-revenue payouts per network | quantitative | payouts | snowflake.wh_analytics__monetization__revenue_daily | card SC-17 | excluded: keep value uses total_revenue_usd, never a network figure |
| Runway, burn, cash balance | quantitative | cash | C07C2866011/1758739428.647609 | cards SC-3, SC-5, SC-73 | excluded: cash means deal inflows only; no deliverable asks for runway, burn or balance |
| Singular and Griffin lines in the sync doc | quantitative | plan terms | f_26e1f9a86761e35049192a | cards SC-39, SC-63 | excluded: only the rights line is cited |
| Vendor mail from brian.foster@ | semantic | sender | C08MCEP1B9B | card SC-6 | excluded: no vendor mail is on the path |
| Frederick's founder status and pay | semantic | role | Contacts 175c0d7bc72ed244b944cb90 | cards SC-49, SC-54 | excluded: no row grades either |
| Investor sheet rows | other | status | f_48247af79428823c3cac92 | cards SC-9, SC-10, SC-33, SC-34 | excluded: investor work is out of scope |
| Homa path | semantic | co-dev or publishing | C096HFA5Z8W/1758210489.170809 | bridge /prompt r1 fork | settled: the rule doc names Homa with the co-dev talks, out of scope |
| Rayking 'reply' | other | X-Gmail-Labels | frederick.stone@harmonygames.co/1842348778705877030 | Q4 /oe r1 finding | settled: an unsent draft addressed to Leonard; his Sep 4 LinkedIn line (`D05S58U4SAK/1757009185.631739`) is closed by a seeded Sep 5 DM (`D05S58U4SAK/1757090400.829462`), so Waiting on us |
| Tamatem | semantic | publisher name | C48D58CD7FBD/1748974617.722599 | design review F9 | settled: Julia passed a name along and nobody came to us; the rule doc excludes that (`f_5e355d03f6eb6a4e866ead`) |
| Term sheets against Frederick's Sep 24 words | temporal | dates | D05S58U4SAK/1758735778.095599 | design review B1 | settled: every term sheet is dated Sep 25 or later, after his DM and the new tranche |
| Tilting Point form | semantic | which title | frederick.stone@harmonygames.co/1842443183462721250 | none | settled: the rule doc names the form as out of scope (`f_5e355d03f6eb6a4e866ead`) |

Six hazard categories in scope: temporal T02; semantic S04; referential R08, R04; quantitative Q01, Q03, Q09, Q10; state/lifecycle L08, L12; identifier/format I03, I04, I15.

**Sibling-defect sweep.** Designed defects are a changed advance (Tallwater), a changed commitment (Sunfold), a claimed wire (Oakline), a moved date (ESG). Siblings checked: Harbor Lane and Wavecrest have calls with no change, so a found call doesn't by itself mark a trap (`evt_43fda04cd11b9d58a05161` is the only note that moves a term). No base publisher thread holds terms: Appodeal's proposal states no rev share or advance (`frederick.stone@harmonygames.co/1830012626042968381`). Whole-universe Slack scan for Aug and Sep shows no publisher reply or term (`00_PreScenario/whole_universe_publisher_sept.txt`); name census in `plan/name_census.json` with a positive control.

## 1b Active speakers

Status from `references/universe_kb/by_universe/synthcut/activity.json` (status_at_clock).

| Person | Email | status_at_clock | Seeding role |
|---|---|---|---|
| Leonard Hayes | leonard.hayes@harmonygames.co | active_sep_2025_quiet_in_oct | the hub mail, ground rules doc, DD publishing card, standing line, Tallwater call note, ESG reply |
| Arthur Blake | arthur.blake@harmonygames.co | active_sep_2025_quiet_in_oct | cash note, #analytics pointer, ENG-2362 comment |
| Robert | robert@harmonygames.co | active_sep_2025_quiet_in_oct | Copperleaf relay, Kestrel post |
| Frederick Stone | frederick.stone@harmonygames.co | active_sep_2025_quiet_in_oct | persona: outreach sheet, one-pager, folder, co-dev doc, sent mail, two card comments, the Rayking DM |
| ESG Law partner | PERSON_2694_EMAIL | external (not in activity.json; base signature in mailbox file frederick@harmonygames.co_1841636073974841484.json) | the signing-date note |
| Publisher people | marek@oaklinegames.com, paola@tallwatergames.com, lena@sunfoldmobile.com and the others | external, seeded with no base footprint (plan/name_census.json) | terms, passes and acknowledgements |

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
ENTITY email:arthur.blake@harmonygames.co  name=Arthur Blake  kind=person  emails=['arthur.blake@harmonygames.co']
  persona: arthur_blake - Co-founder & CTO / Executive
ENTITY email:robert@harmonygames.co  name=Robert  kind=person  emails=['robert@harmonygames.co']
  persona: robert - Co-Founder & Creative Director / Executive
```

- Seeded external first names avoid every HG first name and every shared name above: Marek, Paola, Lena, Diego, Sofia, Jonas, Mei, Anika, Callum, Elena, Rhys, Nadia, Yuki, Tessa, Omar, Greta, Ivo.
- `brian.foster@` is reused by Node's and Craftsman+'s people in base (SC-6): no seed uses it.
- ESG reuses the base token PERSON_2694, whose role is stated in `frederick.stone@harmonygames.co/1841636073974841484` (learnings §14).

## 2 Cohort spine

- Rule (rule doc `f_5e355d03f6eb6a4e866ead`): every publisher on Fred's outreach sheet plus any publisher that came to the founders about Domino Delights since Apr 1, 2025 (26: 24 on the sheet, 2 outside it).
- Size 26: Live 7 · Withdrawn 1 · Out on rights 2 · Passed 6 · Waiting on us 3 · No reply 7. Key = publisher. `cohort_exception` floor 24: no natural 40-record cohort exists, and padding it would add always-pass rows that cut the SD (`00_Pre_Scenario_Analysis.md` §1a).
- Surfaces and shortcut audit (manifest cohort.evidence_surfaces):
  - gmail · `gmail_search_messages+gmail_get_thread` · 0.75 × 24 · decides: status per publisher · no bulk: gmail_search_messages returns ids only; gmail_get_messages_batch reads bodies in bulk, so three quarters of a call per publisher is counted · short-circuit: only a publisher's own thread shows whether it answered, passed or wrote first; no list records outcomes, and the outreach sheet carries none (`f_5e355d03f6eb6a4e866ead`)
  - gdocs · `gdocs_get_document_text` · 1.0 × 8 · decides: latest terms per Live offer · no bulk: each term sheet is its own document; no call returns several bodies · short-circuit: rights, net terms, installs and advance are only in that sheet; the covering mail says terms are attached, not what they are (`f_5e355d03f6eb6a4e866ead`)
  - slack · `slack_search_public_and_private` · 1.0 × 26 · decides: status per publisher · no bulk: channel history returns roots only and a generic search misses a record that names a person or a group · short-circuit: a later founder note can change a publisher's standing, so a thread that looks settled still needs its own search (`f_5e355d03f6eb6a4e866ead`)
  - gcal · `gcal_search_events` · 1.0 × 9 · decides: latest terms per Live offer · no bulk: gcal_list_events shows the start of a description only; the rest needs the event itself · short-circuit: a call note can move a term after the sheet was sent; the sheet can't show that (`f_5e355d03f6eb6a4e866ead`)
  - contacts · `contacts_search_contacts` · 0.5 × 16 · decides: a contact per publisher person who gave terms or said no · no bulk: contacts_get_contacts lists everyone in bulk, so half a call per publisher is counted · short-circuit: Leonard asks to skip anyone already there, so each person has to be checked before each add (`f_5e355d03f6eb6a4e866ead`)
- Predicate: six statuses, a closed set in the rule doc, first that fits, top to bottom (`f_5e355d03f6eb6a4e866ead`).
- House rule over the natural reading (A15): the rights position (`f_26e1f9a86761e35049192a`) overrides the highest value.
- Boundary records (A17): Copperleaf `C07C2866011/1758909900.662794` and Redwood `lc_674982ffdca63f854ec6f591` are in although off the sheet; Summit `frederick.stone@harmonygames.co/1842077918822746195` is No reply although a message exists; Rayking `frederick.stone@harmonygames.co/1842348778705877030` is Waiting on us although a draft exists.
- Necessity: every term sheet decides rights, net terms or an input; every thread decides status. Volume is honest because the board, contacts and reminders are one write per publisher the founders asked for (`68dab660c900179df4f5f92d`, `frederick.stone@harmonygames.co/1844732284109533347`).

## 3 Hidden authorities

| Id | Name | Home | Decoy (scope) | Governs | Findable query |
|---|---|---|---|---|---|
| H1 | the ground rules doc | gdocs `f_5e355d03f6eb6a4e866ead` | gdocs `f_21203dbcdf780cc07c76cb` (game: decoy 'co-dev terms for a new title, not DD (Sep 19)' vs task 'publishing rights for Domino Delights') | R2, R4, R5, R7, R8, R11 | "ground rules" (`f_5e355d03f6eb6a4e866ead`) |
| H2 | the rights position from the August sync | gdocs `f_26e1f9a86761e35049192a` | gmail `frederick.stone@harmonygames.co/1829687508014442264` (issuer: decoy 'Appodeal's own programme line that it takes no game transfer or IP rights' vs task 'what the founders keep') | R6 | "publishing rights" (`f_26e1f9a86761e35049192a`) |
| H3 | the DD publishing card | trello `68dab660c900179df4f5f92d` | trello `trello:/cards/557` (lot: decoy 'the four Oct 2024 BD Follow Up cards from the first partner round' vs task 'the Sep 2025 publisher round') | R9 | "DD publishing" (`68dab660c900179df4f5f92d`) |

Each authority is named by a fragment (K1 names H1 in `frederick.stone@harmonygames.co/1844732284109533347`; K3 names H2 in `f_5e355d03f6eb6a4e866ead`; K4 names H3 on `68dab660c900179df4f5f92d`). The hub delegates by role and links none. `governs` lists don't overlap (hardness_gate hidden_authorities).

## 4 Delegation lattice

| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |
|---|---|---|
| A1 | Leonard's email from yesterday | `frederick.stone@harmonygames.co/1844732284109533347` |
| A2 | the DD publishing card | `68dab660c900179df4f5f92d` |
| A3 | my DD publishing folder | `d_6fc54be60d1377e340a5b5` |

Hub: Leonard's Sep 30 23:10Z mail to Frederick (`frederick.stone@harmonygames.co/1844732284109533347`), delegating by role to the ground rules doc, the folder and the card. It lists no publisher, link or location.

| Fragment | Service · container | Kind | Chain | Delegated by | Delegation quote (verbatim, planned wording) | Requirements | Names authorities |
|---|---|---|---|---|---|---|---|
| K1 | gdocs · `f_5e355d03f6eb6a4e866ead` | delegation | A1 | `frederick.stone@harmonygames.co/1844732284109533347` | "The ground rules doc has how we're doing this" | R2, R4, R5, R7, R11 | H1 ('The ground rules doc') |
| K2 | gsheets · `f_fd467bd2ae0c6d4f3bd2bc` | requirement | A1 → K1 | `f_5e355d03f6eb6a4e866ead` | "Every publisher on Fred's outreach sheet" | R1 | — |
| K3 | gdocs · `f_26e1f9a86761e35049192a` | requirement | A1 → K1 | `f_5e355d03f6eb6a4e866ead` | "The position from the August sync" | R6 | H2 ('The position from the August sync') |
| K4 | trello · `68dab660c900179df4f5f92d` | requirement | A2 | `68dab660c900179df4f5f92d` | "One checklist per status on this card" | R9 | H3 ('One checklist per status on this card') |
| K5 | gdrive · `d_6fc54be60d1377e340a5b5` | destination | A1 | `frederick.stone@harmonygames.co/1844732284109533347` | "Put the model in your DD publishing folder" | R13 | — |
| K6 | gmail · `frederick.stone@harmonygames.co/1844620296192667598` | amendment | A1 → K1 | `f_5e355d03f6eb6a4e866ead` | "If our lawyers give us a later date, use theirs" | R5 | — |
| K7 | gcal · `evt_43fda04cd11b9d58a05161` | amendment | A1 → K1 | `f_5e355d03f6eb6a4e866ead` | "Use the latest terms we have from them, wherever they are" | R3 | — |
| K8 | trello · `68d598387dea3e7fe85e3a0a` | amendment | A1 → K1 | `f_5e355d03f6eb6a4e866ead` | "Use the latest terms we have from them, wherever they are" | R3 | — |
| K9 | slack · `C096HFA5Z8W/1758147530.732569` | requirement | A1 → K1 | `f_5e355d03f6eb6a4e866ead` | "the notes I asked you for on what goes out to publishers still aren't done" | R12 | — |
| K10 | gslides · `f_4b3ef3dcf76258a6fda5cd` | format | A1 → K1 → K9 | `C096HFA5Z8W/1758915000.867092` | "the May one-pager" | R12 | — |
| K11 | slack · `C07C2866011/1758736960.824899` | requirement | A1 → K1 | `f_5e355d03f6eb6a4e866ead` | "however it reached us" | R1, R3 | — |
| K12 | linear · `ENG-2362` | requirement | A1 → K1 | `f_5e355d03f6eb6a4e866ead` | "however it reached us" | R1, R3 | — |
| K13 | slack · `C069FF9Q57S` | requirement | A1 → K1 | `f_5e355d03f6eb6a4e866ead` | "however it reached us" | R1 | — |
| K14 | snowflake · `snowflake:ANALYTICS.MONETIZATION.REVENUE_DAILY` | requirement | A1 → K1 | `f_5e355d03f6eb6a4e866ead` | "ANALYTICS.MONETIZATION.REVENUE_DAILY" | R8 | — |
| K15 | contacts · `5373edb55ca853d6052ecce5` | recipient | A1 | `frederick.stone@harmonygames.co/1844732284109533347` | "Everyone at a publisher who has given us terms or told us no should be in Contacts" | R10 | — |

- Amendments in another service, later in time: K6 gmail `frederick.stone@harmonygames.co/1844620296192667598` (Sep 30) changes the signing date in `f_5e355d03f6eb6a4e866ead` (Sep 29); K7 gcal `evt_43fda04cd11b9d58a05161` (Sep 29) changes Tallwater's advance in `f_e8cb875d5b7c8d9972d259` (Sep 26); K8 trello `68dbfe80ef9c41b4f4fa8fe9` (Sep 30) changes Sunfold's commitment in `f_8ddfb9901891eb8e9dcab8` (Sep 25). Each keeps the rest.
- Non-authoritative distractors: the co-dev doc (`f_21203dbcdf780cc07c76cb`, H1 decoy, another game); Frederick's candidate lists (`f_10dfa1b4236a7c35dcb632`, `f_0d17fc08eddaf231cf7f28`); Appodeal's programme line (`frederick.stone@harmonygames.co/1829687508014442264`).

## 5 Chains and trap register

| Chain | Root cause | Hops (service: record → finding) | Ends in |
|---|---|---|---|
| C1 | A24 | gmail: `frederick.stone@harmonygames.co/1842077918822838564` (Marek confirms the wire) → trello: `68dabd6800e271eb0608d2d6` (the card repeats it) → slack: `C07C2866011/1759251900.005166` (it never hit SVB) | R5 |
| C2 | A11 | gdocs: `f_e8cb875d5b7c8d9972d259` ($60,000) → gcal: `evt_43fda04cd11b9d58a05161` ($40,000 on the call) → gsheets: `model` (advance, value and Q4 cash follow) | R3 |
| C3 | A7 | gmail: `frederick.stone@harmonygames.co/1842077918822811962` (Anika's signature names Kestrel) → contacts: `5373edb55ca853d6052ecce5` (her row says Kestrel Group) → slack: `C07C2866011/1759176900.065118` (Kestrel's offer is off) | R2 |
| C4 | A17 | gdocs: `f_5e355d03f6eb6a4e866ead` (anyone who came to the four of us) → slack: `C069FF9Q57S/1758912000.686342` (a publisher's tech lead, notes on ENG-2362) → linear: `lc_674982ffdca63f854ec6f591` (Redwood's terms) | R1 |
| C5 | A15 | gdocs: `f_3eccf6e0bb63955dc51e27` (all digital storefronts) → slack: `C07C2866011/1756140953.197759` (keep code, IP and non-mobile rights) → gdocs: `f_5e355d03f6eb6a4e866ead` (Out on rights) | R6 |
| C6 | A13 | gdocs: `f_8ddfb9901891eb8e9dcab8` (50,000 a month) → trello: `68d598387dea3e7fe85e3a0a` (card titled by Lena's first name) → trello: `68dbfe80ef9c41b4f4fa8fe9` (30,000 a month) | R3 |
| C7 | A4 | gdocs: `f_5e355d03f6eb6a4e866ead` (Oct 31, unless ESG says later) → gmail: `frederick.stone@harmonygames.co/1844620296192667598` (Nov 14) → gdocs: `f_d72e8b34e7496f0de668bc` (net 60 lands Jan 13) | R5 |
| C8 | A14 | gdocs: `f_5e355d03f6eb6a4e866ead` (the notes are owed as part of this) → slack: `C096HFA5Z8W/1758915000.867092` (a note to anyone Live who got the one-pager) → gsheets: `f_fd467bd2ae0c6d4f3bd2bc` (who got it) | R12 |

| Trap | Family | Records | Requirement | Expected wrong reading | Resolver | Discovery order |
|---|---|---|---|---|---|---|
| T1 | done_gap | `frederick.stone@harmonygames.co/1842077918822838564`, `68dabd6800e271eb0608d2d6`, `C07C2866011/1759251900.005166`, `C07C2866011/1757345405.134829` | R5 | Oakline's $10,000 is banked: Marek confirms the wire and the card says it went out, so Q4 cash is only the remaining $20,000 | Arthur's Sep 30 reply: the $10K first-look never hit SVB, the bank sent it back and it will be resent next week; the rule doc says banked means in the SVB account | Marek's mail and the card are met first, in Oakline's own thread and on the board; Arthur's note sits in a reply under an older root about a banker |
| T2 | superseding | `f_e8cb875d5b7c8d9972d259`, `evt_43fda04cd11b9d58a05161` | R3 | Tallwater's advance is the $60,000 in its term sheet | Leonard's note on the follow-up call: $40,000 now, everything else stands | the term sheet is opened with every other offer; the note sits past the agenda in a calendar description |
| T3 | scope_alias | `frederick.stone@harmonygames.co/1842077918822811962`, `5373edb55ca853d6052ecce5`, `C07C2866011/1759176900.065118` | R2 | Moonrail's offer is Live: its term sheet is open and nothing carries the Moonrail name | the post says Kestrel; Anika's signature and her Contacts row tie Kestrel to Moonrail | a name search for Moonrail returns nothing in Slack, so the thread reads as open |
| T4 | exact_predicate | `C07C2866011/1758909900.662794`, `C07C2866011/1758736960.824899` | R1 | the population is the outreach sheet and Frederick's inbox | the rule doc brings in anyone who came to one of the four of us; Robert pasted Copperleaf's note into a thread | the sheet is read first and looks complete |
| T5 | exact_predicate | `C069FF9Q57S/1758912000.686342`, `lc_674982ffdca63f854ec6f591`, `ENG-2362` | R1 | deal terms don't live on engineering tickets | Arthur's post points at ENG-2362, whose comment holds Redwood's terms | the sheet is read first; Linear isn't on the mail path |
| T6 | authority | `f_3eccf6e0bb63955dc51e27`, `f_26e1f9a86761e35049192a`, `C07C2866011/1756140953.197759` | R6 | Northglow is the best deal: the largest 12-month value and a clean rev share | the founders keep non-mobile distribution rights; Northglow's grant covers all digital storefronts, including PC and web | the term sheet's numbers are met first; the rights position is an old record the rule doc points at by role |
| T7 | superseding | `f_8ddfb9901891eb8e9dcab8`, `68d598387dea3e7fe85e3a0a`, `68dbfe80ef9c41b4f4fa8fe9` | R3 | Sunfold commits 50,000 installs a month | Frederick's Sep 30 card comment: 30,000 a month, rest stands | the term sheet is opened first; the card is titled by Lena's first name |
| T8 | synthesis_omission | `C096HFA5Z8W/1758915000.867092`, `f_4b3ef3dcf76258a6fda5cd`, `C096HFA5Z8W/1758147530.732569` | R12 | the model, the board and the reply finish the job | Leonard's line under his Sep 17 root: anyone who got the May one-pager and is still Live hears the organic figure, as a draft | the rule doc points at it by role only; the reply sits under a root about raising |
| T9 | effective_date | `f_5e355d03f6eb6a4e866ead`, `frederick.stone@harmonygames.co/1844620296192667598` | R5 | the signing date is Oct 31, so net-60 advances land by Dec 30 | ESG's Sep 29 note and Leonard's Sep 30 reply make it Nov 14, so net-60 money lands Jan 13 | the rule doc is read first; ESG's thread doesn't name a publisher |
| T10 | reuse_exclusion | `68d5913004a98be3b4c45408`, `68d598387dea3e7fe85e3a0a` | R9 | every Live publisher needs a new card | two cards already exist under contacts' first names: leave a comment there | — |
| T11 | near_miss_mention | `frederick.stone@harmonygames.co/1842077918822746195` | R2 | Summit answered: there's a message from it | an automatic acknowledgement doesn't count, so No reply | — |
| T12 | tool_surface | `D05S58U4SAK/1757090400.829462`, `frederick.stone@harmonygames.co/1842348778705877030`, `D05S58U4SAK/1757009185.631739` | R2 | Frederick replied to Rayking, so it isn't waiting on us | his Sep 4 message is an unsent draft addressed to Leonard, and his Sep 5 DM says he found no one on LinkedIn and they still owe an answer, so Rayking is Waiting on us | — |
| T13 | superseding | `f_5e355d03f6eb6a4e866ead`, `frederick.stone@harmonygames.co/1830890312657338682`, `D05S58U4SAK/1758735778.095599` | R4 | value an install at the paid-traffic numbers ($0.87 ARPDAU, an LTV of $7) | the rule doc fixes $0.50, the organic D30 ARPI | the Sep 24 DM and the April board note are met by a metrics search |
| T14 | authority | `f_5f3ef4a4760d18e696a41a`, `f_26e1f9a86761e35049192a` | R6 | Pinegrove is Live: its grant is mobile only | it takes source code and the build pipeline; the founders keep the code | — |
| T15 | distractor (other_title) | `C096HFA5Z8W/1758210489.170809`, `C07C2866011/1757516293.887729` | R1 | Homa and NCsoft are publishers in talks | the rule doc leaves co-dev and investment talks out | — |
| T16 | distractor (scope_adjacent) | `frederick.stone@harmonygames.co/1842443183462721250` | R1 | Tilting Point is a publisher we approached | the rule doc leaves its UA funding form out | — |
| T17 | distractor (keyword_collision) | `C07C2866011/1756261199.570279` | R1 | Apple Arcade is a dominoes lead | it isn't on the sheet, and it had already signed someone | — |
| T18 | distractor (partial_listing) | `f_10dfa1b4236a7c35dcb632` | R1 | Frederick's Publishing Partners doc is the population | it's a candidate list; the outreach sheet records who was approached | — |
| T19 | distractor (stale_summary) | `f_0d17fc08eddaf231cf7f28` | R1 | the Biz Dev Notes regional list is the population | it's an April candidate list with a template | — |
| T20 | distractor (withdrawn_ask) | `D05S58U4SAK/1758736842.534589` | R1 | the Sep 24 lead is a publisher to add | Leonard's mail leaves him out: he only wants hypercasual | — |
| T21 | distractor (near_duplicate_record) | `f_21203dbcdf780cc07c76cb` | R4 | the co-dev doc's rules value an offer | it's about co-dev, not DD; the ground rules govern | — |

Hardness v2 traps used as separate cross-source decisions (guide Part 3), each with the convincing wrong source and the record that beats it:

| Channel | v2 trap | Convincing wrong source (who, when) | Record that beats it (who, when, authority) | Weight-5 rows it moves |
|---|---|---|---|---|
| DONE | 1 · proving done across services | Marek's Sep 29 wire confirmation (`frederick.stone@harmonygames.co/1842077918822838564`) and the card comment (`68dabd6800e271eb0608d2d6`) | Arthur, checking SVB with Leonard, Sep 30 (`C07C2866011/1759251900.005166`) | B_PA, VQ_Oakline, K_r_banked |
| CORR | 2 · a correction somewhere else | Tallwater's term sheet, Sep 26 (`f_e8cb875d5b7c8d9972d259`) | Leonard's note on the Sep 29 call (`evt_43fda04cd11b9d58a05161`) | A_adv_PB, V12_Tallwater |
| ALIAS | 6 · different names for the same thing | Moonrail's open term sheet under its trading name (`f_464839da025a0a01f53979`) | Robert's Sep 29 post on Kestrel (`C07C2866011/1759176900.065118`), joined by Anika's signature and Contacts `5373edb55ca853d6052ecce5` | S_out_PC, T_item_PC |
| FILT | 7 · items outside the obvious filter | the outreach sheet and Frederick's inbox (`f_fd467bd2ae0c6d4f3bd2bc`) | Robert's relay (`C07C2866011/1758909900.662794`) and Arthur's ENG-2362 comment (`lc_674982ffdca63f854ec6f591`), brought in by the rule doc | S_in_PH, S_in_PI, V12_Copperleaf, V12_Redwood, T_item_PH, T_item_PI, S_total |
| EXC | 5 · a rule hidden in the data | Northglow's numbers, the largest on the table (`f_3eccf6e0bb63955dc51e27`) | Leonard's Aug 25 rights position, adopted at the Aug 28 sync (`C07C2866011/1756140953.197759`, `f_26e1f9a86761e35049192a`) | S_out_PD, S_out_PJ, R_top |
| INPUT | 8 · wrong inputs to a total | Sunfold's term sheet, Sep 25 (`f_8ddfb9901891eb8e9dcab8`) | Frederick's Sep 30 comment after Lena's call (`68dbfe80ef9c41b4f4fa8fe9`) | A_com_PE, V12_Sunfold, R_top |
| DATE | 4 · dates, windows and dependencies | Oct 31 in the rule doc (`f_5e355d03f6eb6a4e866ead`) | ESG's Sep 29 note and Leonard's Sep 30 reply (`frederick.stone@harmonygames.co/1844620296192667598`) | VQ_Harbor, VQ_Wavecrest |
| FOLLOW | 3 · follow-through a rule requires | the model, the board and the reply look like the whole job | Leonard's standing line (`C096HFA5Z8W/1758915000.867092`), joined to the sheet's What we sent column (`f_fd467bd2ae0c6d4f3bd2bc`) | W_count, W_1, W_2, W_3 |

### Mechanism portfolio (S5a)

Priors from `tools/hardness_ledger.py priors --model claude-opus-5-5` (UNCALIBRATED; never pooled across models). Rates used by the forecast are disclosed overrides sourced from measured placements on the completed Frederick tasks (`plan/run_forecast.sh`).

| # | Candidate (anchor records) | Coupling | Findability term | Prior (family) | Design rate | Survives complete retrieval | Selected |
|---|---|---|---|---|---|---|---|
| DONE | the returned first-look wire (`C07C2866011/1759251900.005166`) | paid claim → banked → Q4 cash | 'SVB', 'first-look' or 'wire', under an older root; the note doesn't name Oakline | done_gap Beta(3,3) mean 0.50 · hev_7f44d83eaad625e9, hev_522f1ca2bc9062de, hev_b8f28a892a74b855 | 0.50 | yes: needs the banked definition | yes |
| CORR | Tallwater call note (`evt_43fda04cd11b9d58a05161`) | advance → value → Q4 cash | calendar search by name | superseding Beta(1,5) mean 0.17 · hev_e61e07235eadbd24, hev_1ceea0e7e912f48b, hev_ebc012c844829411 | 0.55 | no: placement, measured 3 of 7 caught | yes |
| ALIAS | Kestrel's freeze (`C07C2866011/1759176900.065118`) | group → studio → withdrawn | 'Kestrel', not 'Moonrail' or 'Anika' | scope_alias Beta(1,4) mean 0.20 · hev_ab2508cad060b0ac, hev_ace612d2f2268cdf, hev_9cefe52f59fd5be5 | 0.55 | yes: needs the join | yes |
| FILT | Copperleaf and Redwood (`C07C2866011/1758909900.662794`, `lc_674982ffdca63f854ec6f591`) | rule → off-sheet offer → value → pick | generic search, then the ticket | exact_predicate Beta(2,4) mean 0.33 · hev_9c403cae42eb4df8, hev_c2297d21ba5cbc7b, hev_0148aad4d8a4eb2d | 0.35 and 0.55 | no: placement | yes |
| EXC | rights position (`f_26e1f9a86761e35049192a`) | grant clause → status → pick | 'publishing rights' | authority Beta(1,4) mean 0.20 · hev_d17e4abe74f0e7e0, hev_1de494f0682754d6, hev_633340c96ebfc696 | 0.30 | yes: storefront wording against non-mobile | yes |
| INPUT | Sunfold comment (`68dbfe80ef9c41b4f4fa8fe9`) | installs → value → pick | card by first name | superseding Beta(1,5) mean 0.17 · hev_e61e07235eadbd24, hev_1ceea0e7e912f48b, hev_ebc012c844829411 | 0.45 | no: placement | yes |
| DATE | signing date (`frederick.stone@harmonygames.co/1844620296192667598`) | date → net terms → Q4 cash | thread names no publisher | boundary_date Beta(2,1) mean 0.67 · hev_3d96146a0a8b19a5 | 0.40 | yes: the arithmetic stays | yes |
| FOLLOW | standing line (`C096HFA5Z8W/1758915000.867092`) | rule → sheet column → status → draft | 'one-pager', 'organic' | authority Beta(1,4) mean 0.20 · hev_d17e4abe74f0e7e0, hev_1de494f0682754d6, hev_633340c96ebfc696 | 0.50 | no: placement | yes |
| REUSE | first-name cards (`68d5913004a98be3b4c45408`, `68d598387dea3e7fe85e3a0a`) | contact → publisher → comment, not a card | card title by first name | reuse: no record | 0.25 | yes | secondary (T10, no rule: eight-rule limit) |
| ACK | Summit's acknowledgement (`frederick.stone@harmonygames.co/1842077918822746195`) | message → No reply | the thread | near_miss_mention: no record | 0.10 | yes | control (T11) |
| COMPL | a publisher already turned down in a cancelled invite | completion elsewhere | calendar | completion_elsewhere Beta(1,4) mean 0.20 | 0.20 | no | rejected: low prior, and the eight-rule limit |
| TOTALS | Q4 cash across all offers | aggregate of every channel | — | — | — | — | rejected: rights go to one publisher, so a total is meaningless, and it would fail every run |
| COUNT | number of Live offers in the reply | aggregate of four channels | — | — | — | — | rejected for the reply (Q4's COUNTS lesson); kept on the board only |
| WAREHOUSE-KPI | a test gate checked in USER_COHORT_RETENTION | warehouse join | — | — | — | — | rejected: a stated rule is caught every run, and SC-1 sits beside it |
| SDK-BUILD | a tranche tied to an SDK in the store build | git claim | — | — | — | — | rejected: invites a base git contradiction (learnings §49), and ENG-2367+ can't be seeded (SC-26) |

Each selected rule's controls and over-application operator are in the draft manifest (`mechanism_portfolio[].controls`, `over_application`), and its channel in `channels`.

### Liveness flags (S5b)

`trap_liveness.py --design` (verbatim):

```
TRAP LIVENESS · ADVISORY · UNCALIBRATED · lexical warnings, not proof · DESIGN (no SQL: record text unavailable, only manifest-structure flags can fire) · on the Season Pass backtests these are development fixtures, not validation
  hub frederick.stone@harmonygames.co/1844732284109533347 · direct delegations 3 · rule placement: A15 nodes only: ['C5', 'C8', 'T14', 'T6', 'T8'] (mechanism_portfolio); every other node SKIP
  T1   done_gap           -  [rule placement SKIP: not an A15 node]
  T2   superseding        -  [rule placement SKIP: not an A15 node]
  T3   scope_alias        -  [rule placement SKIP: not an A15 node]
  T4   exact_predicate    -  [rule placement SKIP: not an A15 node]
  T5   exact_predicate    -  [rule placement SKIP: not an A15 node]
  T6   authority          -
  T7   superseding        -  [rule placement SKIP: not an A15 node]
  T8   synthesis_omission -
  T9   effective_date     -  [rule placement SKIP: not an A15 node]
  T10  reuse_exclusion    -  [rule placement SKIP: not an A15 node]
  T11  near_miss_mention  -  [rule placement SKIP: not an A15 node]
  T12  tool_surface       -  [rule placement SKIP: not an A15 node]
  T13  superseding        -  [rule placement SKIP: not an A15 node]
  T14  authority          -
  T15  distractor         -  [rule placement SKIP: not an A15 node]
  T16  distractor         -  [rule placement SKIP: not an A15 node]
  T17  distractor         -  [rule placement SKIP: not an A15 node]
  T18  distractor         -  [rule placement SKIP: not an A15 node]
  T19  distractor         -  [rule placement SKIP: not an A15 node]
  T20  distractor         -  [rule placement SKIP: not an A15 node]
  T21  distractor         breadcrumb  [rule placement SKIP: not an A15 node]
  dispositions: 0/1 recorded
```

| Flag | Nodes | Disposition |
|---|---|---|
| breadcrumb | T21 | structural at design time: T21 is the co-dev decoy, which the entry set reaches by search; it decides nothing (`f_21203dbcdf780cc07c76cb`) |
| SAME_PLACE (hardness_v2_check) | T7 | clean, but the tool can't see that Sunfold's card sits on an anchor's list: the comment stays on one card (`68d598387dea3e7fe85e3a0a`) and never in the list or the DD publishing card |

## 6 Failure-diversity plan

| Channel | Behaviour that finds the deciding record | Measured analog (completed tasks) | Rows | Independent of |
|---|---|---|---|---|
| DONE | a Slack search for SVB, wire or first-look | bridge SciPlay reply under an unrelated post: 3 of 6 | B_PA, VQ_Oakline, K_r_banked | calendar and Trello (`C07C2866011/1759251900.005166`) |
| CORR | a calendar search per publisher, or opening the event | Q4 calendar note found 3 of 7 | A_adv_PB, V12_Tallwater, VQ_Tallwater | Slack behaviour (`evt_43fda04cd11b9d58a05161`) |
| ALIAS | joining a signature or Contacts row to a post | handover id join: 5 of 6 missed, halved for fairness | S_out_PC, T_item_PC, W_count | name searches (`C07C2866011/1759176900.065118`) |
| FILT, Copperleaf | a 'publisher' Slack search that reaches a reply | bridge reply under an unrelated post: 2 of 8 then 3 of 6, higher here because the reply says publisher | seven rows and the pick | mail behaviour (`C07C2866011/1758909900.662794`) |
| FILT, Redwood | a 'publisher' Slack search, then opening Linear | Q4 Linear-only fact: 0 of 6; pointer added | six rows | thread reading (`C069FF9Q57S/1758912000.686342`) |
| EXC | applying the sync position to grant wording | judgment rows rarely land | S_out_PD, S_out_PJ, R_top | retrieval habits (`f_26e1f9a86761e35049192a`) |
| INPUT | reading comments on a first-name card | trello_get_comments ran where the card was named | A_com_PE, V12_Sunfold | Slack and calendar (`68dbfe80ef9c41b4f4fa8fe9`) |
| DATE | opening a thread that names no publisher | handover mail outside the money window: 2 of 6 missed | VQ_Harbor, VQ_Wavecrest | Slack and Trello (`frederick.stone@harmonygames.co/1844620296192667598`) |
| FOLLOW | a search for the one-pager or the organic figure | reply under an unrelated root: 20–30 % caught | W_count, W_1, W_2, W_3 | mail (`C096HFA5Z8W/1758915000.867092`) |

Each channel moves at least two rows, so one trap can't chain patterns (bridge rev12 batch 1). Most trap rows hang on one channel, because a row on several channels fails nearly every run and adds no spread (`00_Pre_Scenario_Analysis.md` §1a: mixed weight tracks SD).

```
UNCALIBRATED · surface: 72 slots, total weight 242, mechanism-flippable 157 (64.9%) · cap 80%

Whole policies
  100.0%  Perfect  [-]
   35.1%  Inbox, outreach sheet and term sheets only  [ALIAS, CORR, DATE, DONE, EXC, FILT1, FILT2, FOLLOW, INPUT]
   78.5%  Term sheets at face value, otherwise thorough  [CORR, DONE, INPUT]
   71.5%  Thorough except the population  [FILT1, FILT2]
   65.3%  Thorough except anything not under the trading name  [ALIAS, FILT1, FILT2]
   84.7%  Thorough except calendar and card comments  [CORR, INPUT]
   64.5%  Thorough except Slack beyond name searches  [DONE, FILT1, FOLLOW]
   85.5%  Value alone, misses the rights position  [EXC]
   91.7%  Finishes at the model, the board and the reply  [FOLLOW]
   95.9%  Rule doc's Oct 31 date kept  [DATE]

Single misses
  DONE     93.8%  slots 3  weight share 6.2%
  CORR     94.6%  slots 3  weight share 5.4%
  ALIAS    89.3%  slots 6  weight share 10.7%
  FILT1    78.9%  slots 13  weight share 21.1%
  FILT2    84.7%  slots 9  weight share 15.3%
  EXC      85.5%  slots 9  weight share 14.5%
  INPUT    90.1%  slots 6  weight share 9.9%
  DATE     95.9%  slots 2  weight share 4.1%
  FOLLOW   91.7%  slots 4  weight share 8.3%

Pairs at or above the cap: ['DONE+CORR', 'DONE+ALIAS', 'DONE+INPUT', 'DONE+DATE', 'DONE+FOLLOW', 'CORR+ALIAS', 'CORR+EXC', 'CORR+INPUT', 'CORR+DATE', 'CORR+FOLLOW', 'ALIAS+DATE', 'ALIAS+FOLLOW', 'FILT2+DATE', 'EXC+INPUT', 'EXC+DATE', 'INPUT+DATE', 'INPUT+FOLLOW', 'DATE+FOLLOW']
P(one run catches every trap) ~ 0.0034; expected landings 4.15

Six-run Monte Carlo
  view                                    E[avg]  E[SD]  mixed  allfail P(<80) P(SD) P(pat) P(all)
  design rates, rho .35                   64.9%  0.161  66.0%   3.0%  0.98  0.92  1.00  0.90
  design rates, rho .2                    64.4%  0.137  65.2%   3.8%  0.99  0.82  1.00  0.81
  design rates, rho .6                    65.9%  0.197  66.9%   2.1%  0.94  0.97  1.00  0.91
  0.8x                                    71.0%  0.163  65.9%   1.2%  0.89  0.92  1.00  0.83
  0.7x                                    74.2%  0.160  64.7%   0.7%  0.78  0.92  1.00  0.73
  0.6x                                    77.4%  0.155  62.7%   0.3%  0.63  0.90  1.00  0.59
  0.5x                                    80.7%  0.147  59.4%   0.2%  0.44  0.85  1.00  0.42
  +40 always-pass weight                  69.9%  0.139  56.6%   2.6%  0.94  0.84  1.00  0.79
  +80 always-pass weight                  73.6%  0.121  49.6%   2.3%  0.87  0.73  1.00  0.64
  0.7x, +40                               77.8%  0.137  55.5%   0.6%  0.62  0.84  1.00  0.55
  0.7x, +80                               80.6%  0.120  48.6%   0.5%  0.45  0.74  1.00  0.36
  ledger priors                           75.7%  0.154  61.2%   0.8%  0.72  0.91  1.00  0.67
  ledger priors, +40                      79.2%  0.132  52.5%   0.7%  0.54  0.83  1.00  0.48

Pre-check (one run, rho .35)
  scale 1.0: P(none) 0.067  P(two or more) 0.83  P(first pick or banked figure wrong) 0.77
  scale 0.7: P(none) 0.159  P(two or more) 0.66  P(first pick or banked figure wrong) 0.62
  scale 0.5: P(none) 0.272  P(two or more) 0.51  P(first pick or banked figure wrong) 0.49
```

Correlation risk named: DONE, FILT and FOLLOW all reward thorough Slack searching, on different containers. The rho sweep above is the check on it.

## 7 Deliverables and dependent writes

| Write | Tool | Count | Depends on | Requirements | Target and access |
|---|---|---|---|---|---|
| gsheets | `gsheets_create_spreadsheet+gsheets_values_update+gdrive_move_file` | 5 | K1, K2, K5, C1, C2, C3, C4, C5, C6, C7, T1, T2, T3, T4, T5, T6, T7, T9 | R1, R2, R3, R4, R5, R7, R8 | new sheet moved into `d_6fc54be60d1377e340a5b5` (owner Frederick, Drive and Sheets rows agree) |
| trello | `trello_create_checklist+trello_create_check_item` | 32 | K4, C3, C4, C5 | R9 | UA/BD board list `670015c2ecd45b634d5eec81`, card `68dab660c900179df4f5f92d`; checklists and items proven there by all six handover baselines (card `67cf1b506d78ad3c72e02a35`) |
| trello | `trello_create_card+trello_add_comment` | 17 | K4, T10, C3, C4, C5 | R9 | UA/BD board list `670015c2ecd45b634d5eec81`, card `68dab660c900179df4f5f92d`; checklists and items proven there by all six handover baselines (card `67cf1b506d78ad3c72e02a35`) |
| contacts | `contacts_add_new_contact` | 14 | K15, C4 | R10 | Contacts (unscoped) |
| gcal | `gcal_create_event` | 7 | K1, C3, C4, C5 | R11 | Frederick's own calendar |
| gmail | `gmail_create_draft` | 3 | K9, C8 | R12 | drafts in his mailbox; the reply on `frederick.stone@harmonygames.co/1844732284109533347` |
| gmail | `gmail_create_draft` | 7 | K4, T11 | R9 | drafts in his mailbox; the reply on `frederick.stone@harmonygames.co/1844732284109533347` |
| gmail | `gmail_reply_to_message` | 1 | K1, C1, C2, C4, C5, C6 | R13 | drafts in his mailbox; the reply on `frederick.stone@harmonygames.co/1844732284109533347` |

Reuse vs create (A8): Oakline and Sunfold already have follow-up cards under their contacts' first names (`68d5913004a98be3b4c45408`, `68d598387dea3e7fe85e3a0a`), and Anika and Lena already have contacts (`5373edb55ca853d6052ecce5`, `1d6fd505d2fea08fa0f26c6e`).

## 8 Service role map

| Service | Role | Load-bearing fact or write | Carrier |
|---|---|---|---|
| gmail | Leonard's ask and the report destination; each publisher's thread; ESG's signing date; Oakline's payment confirmation; follow-through drafts | the ask, who answered and the signing date live in mail | ● (`frederick.stone@harmonygames.co/1844732284109533347`) |
| gdocs | the ground rules doc (H1), its co-dev decoy, ten-odd publisher term sheets, the base exec sync (H2) | rules, terms and the rights position | ● (`f_5e355d03f6eb6a4e866ead`) |
| gsheets | Fred's outreach sheet (population, what each got); the model itself | the population and the deliverable | ● (`f_fd467bd2ae0c6d4f3bd2bc`) |
| gdrive | the DD publishing folder and term-sheet filing | the destination Frederick owns | ● (`d_6fc54be60d1377e340a5b5`) |
| gslides | the May one-pager that carried the paid-traffic numbers | who was told what, behind the follow-through | ● (`f_4b3ef3dcf76258a6fda5cd`) |
| slack | Arthur's cash note, Robert's relay, the Kestrel post, Leonard's standing line, the analytics pointer | four deciding records sit in Slack | ● (`C07C2866011/1759251900.005166`) |
| gcal | Tallwater's follow-up note; Monday's sit-down; reminders | a corrected advance and the reminders | ● (`evt_43fda04cd11b9d58a05161`) |
| trello | the DD publishing card (H3); existing follow-up cards with a comment on Sunfold's commitment; new cards | the board ask, a corrected input and the board writes | ● (`68dab660c900179df4f5f92d`) |
| contacts | who Anika works for; existing and new contacts | the alias join and the contact writes | ● (`5373edb55ca853d6052ecce5`) |
| linear | Arthur's comment on ENG-2362 holding Redwood's terms | an in-scope offer outside the inbox | ● (`ENG-2362`) |
| snowflake | REVENUE_DAILY for the keep value | the only home of the keep value | ● (`ANALYTICS.MONETIZATION.REVENUE_DAILY`) |
| github | not used | none (S04 name mismatch; code claims invite a git contradiction) | — (`frederick.stone@harmonygames.co/1842359398719557772`) |
| confluence | not used | never carries a fact (learnings §26) | — |

## 9 Call budget

| Phase | Service | Calls | Necessity reason |
|---|---|---|---|
| discovery | gmail | 3 | read Leonard's ask; open the ESG thread; open Oakline's payment mail |
| discovery | gdocs | 3 | read the ground rules doc and the August sync; reject the co-dev doc |
| discovery | gsheets | 2 | read the outreach sheet's tabs |
| discovery | gdrive | 3 | list the DD publishing folder; find term sheets |
| discovery | slack | 4 | search founder talk on publishing, numbers and rights |
| discovery | trello | 3 | read the board, the BD Follow Up list and the DD publishing card |
| discovery | snowflake | 4 | list and describe the table; query three months of revenue |
| enumeration | gmail | 6 | census threads since Apr 1 by publisher, offer and rights terms |
| enumeration | slack | 5 | census publisher talk; Slack search has no bulk read of replies |
| enumeration | gcal | 3 | list calls in the window; read Monday's sit-down |
| enumeration | linear | 3 | follow the pointer to ENG-2362 and its comments |
| enumeration | contacts | 2 | list contacts; resolve people named in posts |
| per-record | gmail | 18 | each publisher's thread (three quarters of a call each, bulk reads discounted) |
| per-record | gdocs | 8 | each term sheet: terms and rights |
| per-record | slack | 26 | a search per publisher, since a later founder note can change its standing |
| per-record | gcal | 9 | a search per Live or Out offer for a call note |
| per-record | contacts | 8 | a lookup before each add (two already exist) |
| per-record | trello | 4 | read comments on the existing follow-up cards |
| writes | gsheets | 5 | create the model, write two tabs, move it into the folder |
| writes | contacts | 14 | a contact for each publisher person who gave terms or said no, minus two that exist |
| writes | trello | 32 | six checklists and one item per publisher |
| writes | trello | 17 | 15 new follow-up cards and comments on two existing ones |
| writes | gcal | 7 | a reminder on each Live offer's response date |
| writes | gmail | 4 | three follow-through drafts and the reply |
| writes | gmail | 7 | a one-line nudge draft to each No reply publisher |
| read-back | gsheets | 2 | check the model |
| read-back | trello | 1 | check the card |
| **total** | 10 services | **203** | unconditional |

Golden-run note: a lean correct run still needs every term sheet, about 82 single-object writes and the discovery reads, which is about 145 counted calls. Reads never fell below 54 on a Frederick task; bridge's 53–55 writes left its weakest run at 109, and Q4's 88–93 held its weakest at 151 (`00_PreScenario/stored_runs_counted_output.txt`). High-count writes are template-identical, so they are sampled in the rubric.

## 10 QC rails

### Two-reading table

| Decision point | Best reading | Strongest alternative | Resolution (record) |
|---|---|---|---|
| Oakline banked | $0: it never hit SVB | $10,000: Marek confirms the wire | Arthur's later note (`C07C2866011/1759251900.005166`); rule doc: banked means in the SVB account (`f_5e355d03f6eb6a4e866ead`) |
| Oakline Q4 cash | $30,000: the resend and the net-30 balance land in Q4 | $20,000: the first $10,000 already came | same note: resending next week; Dec 14 for the balance (`C07C2866011/1759251900.005166`, `f_27cac0eed300cc33eeb4fd`) |
| Tallwater advance | $40,000 | $60,000 in the term sheet | Leonard's later call note (`evt_43fda04cd11b9d58a05161`); rule doc: latest terms, wherever they are |
| Moonrail status | Withdrawn | Live: its sheet is open | Robert's post on Kestrel (`C07C2866011/1759176900.065118`), Anika's signature (`frederick.stone@harmonygames.co/1842077918822811962`), Contacts `5373edb55ca853d6052ecce5` |
| Copperleaf in | in, Live | out: not on the sheet, no term sheet | rule doc: came to one of the four of us, however it reached us; their note pasted in by one of us counts (`C07C2866011/1758909900.662794`) |
| Redwood in | in, Live | out: an engineering note | same rule; Arthur pastes her note (`lc_674982ffdca63f854ec6f591`) |
| Northglow | Out on rights | Live: the best numbers | grant covers PC and web (`f_3eccf6e0bb63955dc51e27`); founders keep non-mobile rights (`C07C2866011/1756140953.197759`) |
| Pinegrove | Out on rights | Live: mobile stores only | ownership of the code passes to Pinegrove (`f_5f3ef4a4760d18e696a41a`); founders keep code (`C07C2866011/1756140953.197759`) |
| Sunfold installs | 30,000 a month | 50,000 in the term sheet | Frederick's later comment (`68dbfe80ef9c41b4f4fa8fe9`); rule doc: latest terms |
| Signing date | Nov 14 | Oct 31 | rule doc: if ESG gives a later date, use theirs; Leonard's reply (`frederick.stone@harmonygames.co/1844620296192667598`) |
| Harbor Lane and Wavecrest Q4 cash | $0: net 60 from Nov 14 lands Jan 13 | their full advances | term sheets (`f_d72e8b34e7496f0de668bc`, `f_a6a5647f977d4638b2b8b1`) with the date above |
| Who gets a draft | Tallwater, Harbor Lane, Wavecrest | Moonrail too, or everyone | standing line: got it and still Live (`C096HFA5Z8W/1758915000.867092`); sheet column (`f_fd467bd2ae0c6d4f3bd2bc`) |
| Rayking | Waiting on us | No reply, or answered | they wrote and the last message is theirs: Frederick's is an unsent draft to Leonard (`frederick.stone@harmonygames.co/1842348778705877030`), and his LinkedIn line (`D05S58U4SAK/1757009185.631739`) is closed by his Sep 5 DM (`D05S58U4SAK/1757090400.829462`) |
| Appodeal | Waiting on us | Live: it made a proposal | no rev share or advance in writing, and the last message is theirs (`frederick.stone@harmonygames.co/1830012626042968381`) |
| Summit | No reply | answered | automatic acknowledgement (`frederick.stone@harmonygames.co/1842077918822746195`); rule doc says it doesn't count |
| Tilting Point | out | No reply | the rule doc names its form as out of scope (`frederick.stone@harmonygames.co/1842443183462721250`, `f_5e355d03f6eb6a4e866ead`) |
| Tamatem | out | a publisher to add | rule doc: a name someone passed along doesn't count (`C48D58CD7FBD/1748974617.722599`) |
| Homa and NCsoft | out | publishers in talks | rule doc: co-dev, engine or investment talks aren't part of this (`C096HFA5Z8W/1758210489.170809`, `C07C2866011/1757516293.887729`) |
| Sep 24 lead | out | add him | Leonard's mail (`frederick.stone@harmonygames.co/1844732284109533347`) over the DM (`D05S58U4SAK/1758736842.534589`) |
| Apple Arcade | out | a dominoes lead | not on the sheet, and no one came to us (`C07C2866011/1756261199.570279`) |
| Existing cards | comment on Lena's and Marek's | new cards | the card says so (`68dab660c900179df4f5f92d`); first names map through the threads (`68d598387dea3e7fe85e3a0a`, `68d5913004a98be3b4c45408`) |
| Contacts present | 16 people gave terms or said no; skip Anika and Lena, so 14 adds | add again, or add Appodeal and Rayking people | Leonard's mail (`frederick.stone@harmonygames.co/1844732284109533347`); Contacts `5373edb55ca853d6052ecce5`, `1d6fd505d2fea08fa0f26c6e` |
| Nudges | all seven No reply publishers, Summit included | skip Summit because it acknowledged | the card (`68dab660c900179df4f5f92d`) and the rule that an acknowledgement isn't a reply (`f_5e355d03f6eb6a4e866ead`) |
| First pick | Copperleaf, $67,200 | Northglow or Sunfold | rule doc ranks Live offers by 12-month value (`f_5e355d03f6eb6a4e866ead`) |

No decision forks on a reported figure; one reading per point. Dates: every graded date is a plan date with the same PT and UTC day.

### Reach table (load-bearing records)

Base records, `persona_view.py can-see frederick_stone …` (verbatim, `00_PreScenario/cansee_anchors.txt`):

- frederick_stone gdocs f_26e1f9a86761e35049192a: YES   reason:   file is shared with the persona (shared_with_emails) 
- frederick_stone gdocs f_10dfa1b4236a7c35dcb632: YES   reason:   persona owns the file 
- frederick_stone gdocs f_0d17fc08eddaf231cf7f28: YES   reason:   persona owns the file 
- frederick_stone gdocs f_37fba7a0a1500b6731dc83: YES   reason:   persona owns the file 
- frederick_stone gdrive d_175c0d7bc72ed244b944cb: YES   reason:   persona owns the file 
- frederick_stone slack C07C2866011: YES   reason:   persona EMPLOYEE_0008_SLACK_ID is in members of private executives 
- frederick_stone slack D05S58U4SAK: YES   reason:   persona EMPLOYEE_0008_SLACK_ID is in members of im D05S58U4SAK 
- frederick_stone slack C096HFA5Z8W: YES   reason:   persona EMPLOYEE_0008_SLACK_ID is in members of private bridge-pitch 
- frederick_stone slack C069FF9Q57S: YES   reason:   persona EMPLOYEE_0008_SLACK_ID is in members of private analytics 
- frederick_stone slack C0880U9751A: YES   reason:   persona EMPLOYEE_0008_SLACK_ID is in members of private zombie-match3d 
- frederick_stone gmail frederick.stone@harmonygames.co/1830012626042968381: YES   reason:   thread is in the persona's own mailbox frederick.stone@harmonygames.co 
- frederick_stone gmail frederick.stone@harmonygames.co/1829687508014442264: YES   reason:   thread is in the persona's own mailbox frederick.stone@harmonygames.co 
- frederick_stone gmail frederick.stone@harmonygames.co/1842348778705877030: YES   reason:   thread is in the persona's own mailbox frederick.stone@harmonygames.co 
- frederick_stone gmail frederick.stone@harmonygames.co/1842443183462721250: YES   reason:   thread is in the persona's own mailbox frederick.stone@harmonygames.co 
- frederick_stone gmail frederick.stone@harmonygames.co/1843552279434086285: YES   reason:   thread is in the persona's own mailbox frederick.stone@harmonygames.co 
- frederick_stone gcal evt_bd61f3209523d19fdd6ba2: YES   reason:   event is on the persona's own calendar frederick.stone@harmonygames.co 
- frederick_stone slack C08H78VJG80: YES   reason:   persona EMPLOYEE_0008_SLACK_ID is in members of private [SOURCE_ORG_0001]-playablex 
- frederick_stone slack C05KNDCHAAG: YES   reason:   persona EMPLOYEE_0008_SLACK_ID is in members of private company-internal 
- frederick_stone gsheets f_7fca456525bc65392b5a34: YES   reason:   persona owns the file

Probes (never load-bearing, and not cited by any fragment): Leonard's DMs `D04UC0UEN2V`, `D04UGG61DUM` are NO for Frederick and are used only as coherence support. DENIAL-INTENDED: outside his reach; alternate_evidence_ids: C07C2866011/1756140953.197759, D05S58U4SAK/1758736827.548589

Planned seeds (verified at the injection gate; owner, invitee or member Frederick):
- LB `frederick.stone@harmonygames.co/1844732284109533347` (hub_thread)
- LB `frederick.stone@harmonygames.co/1844620296192667598` (esg_thread)
- LB `f_5e355d03f6eb6a4e866ead` (rule_doc)
- LB `f_fd467bd2ae0c6d4f3bd2bc` (outreach_sheet)
- LB `f_4b3ef3dcf76258a6fda5cd` (onepager_deck)
- LB `d_6fc54be60d1377e340a5b5` (dd_folder)
- LB `evt_43fda04cd11b9d58a05161` (pb_event)
- LB `C07C2866011/1759251900.005166` (arthur_cash)
- LB `C07C2866011/1758909900.662794` (copperleaf_relay)
- LB `C07C2866011/1759176900.065118` (kestrel_post)
- LB `C096HFA5Z8W/1758915000.867092` (standing_line)
- LB `C069FF9Q57S/1758912000.686342` (arthur_analytics)
- LB `D05S58U4SAK/1757090400.829462` (rayking_dm)
- LB `f_27cac0eed300cc33eeb4fd` (Oakline Games term sheet)
- LB `f_e8cb875d5b7c8d9972d259` (Tallwater Games term sheet)
- LB `f_8ddfb9901891eb8e9dcab8` (Sunfold Mobile term sheet)
- LB `f_d72e8b34e7496f0de668bc` (Harbor Lane Games term sheet)
- LB `f_a6a5647f977d4638b2b8b1` (Wavecrest Play term sheet)
- LB `f_464839da025a0a01f53979` (Moonrail Studios term sheet)
- LB `f_3eccf6e0bb63955dc51e27` (Northglow Publishing term sheet)
- LB `f_5f3ef4a4760d18e696a41a` (Pinegrove Games term sheet)

Unscoped load-bearing records: Trello `68dab660c900179df4f5f92d`, `68d5913004a98be3b4c45408`, `68d598387dea3e7fe85e3a0a`; Linear ENG-2362 and `lc_674982ffdca63f854ec6f591`; Contacts `5373edb55ca853d6052ecce5`, `1d6fd505d2fea08fa0f26c6e`; Snowflake `ANALYTICS.MONETIZATION.REVENUE_DAILY`.

**Feasibility.** Every write exists in `Evals/references/tools/catalog.json` (`gsheets_create_spreadsheet`, `gsheets_values_update`, `gdrive_move_file`, `trello_create_checklist`, `trello_create_check_item`, `trello_create_card`, `trello_add_comment`, `contacts_add_new_contact`, `gcal_create_event`, `gmail_create_draft`, `gmail_reply_to_message`). Frederick owns the folder `d_6fc54be60d1377e340a5b5` and his calendar; Trello and Contacts are unscoped. `trello_create_card` on this board is unproven: confirm it in the pre-check. **Precedence.** Load-bearing facts sit in ● carriers (mail bodies, Docs bodies, Slack messages, Linear comments, Trello descriptions and comments), never only in an attachment. Tallwater's note is a calendar description, a ○ carrier in `Ask_Carriers.md`; stored runs show `gcal_search_events` returns descriptions, so the pre-check must prove the route. **Naturalness.** The prompt names Leonard's email, the folder and the card; it never names publishers, rules, statuses or where evidence sits. **Grading devices.** ≤ 5 samples per group plus volume rows; exclusions graded as exact counts on required writes, never as leave-alone rows. The reply carries a pick and three figures, never a list. Cap: 75 rows, at least 45 % mixed weight.

### Coherence rail

Every 1a row is dispositioned; every designed disagreement is a dated human claim overturned by a named later record (T1 `C07C2866011/1759251900.005166`, T2 `evt_43fda04cd11b9d58a05161`, T7 `68dbfe80ef9c41b4f4fa8fe9`, T9 `frederick.stone@harmonygames.co/1844620296192667598`); no system field is modified. Companions are planned in §11.

## 11 Record plan for /create-injection

| Record | Service · table | Planned id | Time (UTC) | Author | Content (planned) |
|---|---|---|---|---|---|
| hub | gmail · gmail_messages/threads | frederick.stone@harmonygames.co/1844732284109533347 | 2025-09-30T23:10:00Z | Leonard → Frederick | Fred, ¶ a16z didn't happen and the Turkish fund is a no, so DD publishing, the idea from the sync, is where my head is now. On Monday Oct 6 I want the four of us to sit down knowing what each publisher would actually bring in. Can you build the model for that? ¶ The ground rules doc has how we're doing this, including who counts and how an offer gets valued. Put the model in your DD publishing folder, laid out the way the doc says. ¶ Do what's on the DD publishing card on the UA/BD board too. ¶ Everyone at a publisher who has given us terms or told us no should be in Contacts, with the company in the job title. Skip anyone who's already there. ¶ That guy from Sep 24 I said I'd chase only wants hypercasual and never made it onto your sheet, so leave him out. ¶ When it's all in, reply here with which offer goes first, what it brings in over 12 months, what it brings in during Q4, and how much publisher money we've actually banked so far. ¶ Leonard |
| ground rules doc | gdocs + gdrive (owner Leonard, shared Frederick, Robert, Arthur) | f_5e355d03f6eb6a4e866ead | 2025-09-29T16:00:00Z | Leonard | DD publishing model: ground rules · Written for next Monday's talk. Leonard, Sep 29. ¶ Who's in · Every publisher on Fred's outreach sheet, plus any publisher that came to one of the four of us about Domino Delights since Apr 1, 2025, however it reached us. A name someone passed along doesn't count unless they came to us. Co-dev, engine or investment talks aren't part of this, even where DD came up. That covers Homa and NCsoft, and Fred's UA funding form to Tilting Point. ¶ Status (first that fits, top to bottom) · Withdrawn: they gave terms, then took them back. · Out on rights: their terms take something we keep. The position from the August sync still stands. · Live: a rev share and an advance in writing from them, whether that's a term sheet, an email, or their note pasted in by one of us. · Passed: they said no. · Waiting on us: they wrote to us, there are no terms, and the last message is theirs. · No reply: nothing back from them. An automatic acknowledgement doesn't count. ¶ Use the latest terms we have from them, wherever they are, calls included. ¶ Valuing a Live offer · Monthly installs x 12 x $0.50 is the gross. $0.50 is the organic D30 ARPI from my Sep 24 note. It's a planning figure, not a promise. · Our share is the rev share they offer us times the gross. · 12-month value is the larger of our share and the total advance, because the advance is recouped out of our share. ¶ Q4 cash · Advance money that lands between Oct 1 and Dec 31, 2025. Assume we sign on Oct 31. If our lawyers give us a later date, use theirs. A payment on net terms lands that many days after signature. Rev share statements don't land in Q4. Banked means it's actually in the SVB account. ¶ Keep value · What DD earned in Jul, Aug and Sep (ANALYTICS.MONETIZATION.REVENUE_DAILY, total_revenue_usd), averaged, times 12. ¶ First pick · The Live offer with the highest 12-month value. ¶ Reminders · One for each Live offer on Fred's calendar, on its response date, named for the publisher. ¶ Layout · A Google Sheet called DD publishing model. Tab Publishers: Publisher, Status, Advance, Monthly installs, 12-month value, Q4 cash. Figures only for Live offers. Tab Summary: Keep value, First pick, Banked so far. ¶ Fred, the notes I asked you for on what goes out to publishers still aren't done, so do those as part of this too. |
| co-dev doc (H1 decoy) | gdocs + gdrive (owner Frederick) | f_21203dbcdf780cc07c76cb | 2025-09-19T17:30:00Z | Frederick | co-dev terms we'd accept, not DD; scope: another game; no publisher terms |
| outreach sheet | gsheets + gdrive (owner Frederick, in the folder) | f_fd467bd2ae0c6d4f3bd2bc | 2025-09-24T19:30:00Z | Frederick | columns Publisher, Contact, First contact, Tranche, What we sent; 24 rows, Appodeal and Rayking among them as came to us; no outcomes; note: Names on my Publishing Partners doc that aren't listed here haven't been approached about DD publishing yet. |
| May one-pager | gslides + gdrive (owner Frederick) | f_4b3ef3dcf76258a6fda5cd | 2025-05-05T17:00:00Z | Frederick | the numbers from the Apr 30 board note (`frederick.stone@harmonygames.co/1830890312657338682`): D1 50%+, D7 20%+, ARPDAU about $0.13, marked as incentivized traffic |
| DD publishing folder | gdrive · drive_files (owner Frederick) | d_6fc54be60d1377e340a5b5 | 2025-09-24T19:00:00Z | Frederick | destination |
| DD publishing card | trello · cards (BD Follow Up list) | 68dab660c900179df4f5f92d | 2025-09-29T16:40:00Z | Leonard | For Monday. One checklist per status on this card, one item per publisher. Every Live, Waiting on us and No reply publisher gets a follow-up card on this list, named F/up with plus the publisher's name. If they already have a card here, leave a comment with the status on that one instead. Leave a one-line nudge to every No reply publisher in your Gmail drafts so it's ready to send. |
| F/up with Marek | trello · cards, comment action | 68d5913004a98be3b4c45408 / 68dabd6800e271eb0608d2d6 | 2025-09-25T19:00:00Z / 2025-09-29T17:10:00Z | Frederick | Marek says the $10K first-look payment went out today. |
| F/up with Lena | trello · cards, comment action | 68d598387dea3e7fe85e3a0a / 68dbfe80ef9c41b4f4fa8fe9 | 2025-09-25T19:30:00Z / 2025-09-30T16:00:00Z | Frederick | Lena called. Their UA budget got cut, so they can only commit 30,000 installs a month, not the 50,000 in the term sheet. Rest stands. |
| Tallwater follow-up | gcal · events (one copy per attendee) | evt_43fda04cd11b9d58a05161 | 2025-09-29T18:30:00Z, updated 2025-09-29T20:00:00Z | Leonard (Frederick, Paola invited) | Agenda: walk through their term sheet, the UA plan for the first two quarters, who runs live ops after launch, and what they need from us on store listings and analytics access. Notes: Paola came back on the call. The advance is $40,000 now, not the number in the term sheet. Everything else stands. |
| Monday sit-down | gcal · events (one copy per attendee) | evt_881d3e07c598b2205a7ff3 | 2025-09-30T23:10:00Z | Leonard (founders) | DD publishing, Mon Oct 6 |
| Harbor Lane call (control) | gcal · events (one copy per attendee) | evt_d6905d9d5497d6a83a9a56 | 2025-09-26T19:00:00Z | Frederick (Diego invited) | Agenda: their term sheet and the UA plan. Notes: went through it line by line, no changes from them. |
| Wavecrest call (control) | gcal · events (one copy per attendee) | evt_48e63a8c7304cf9432fb46 | 2025-09-25T18:00:00Z | Frederick (Sofia invited) | Agenda: their term sheet and who handles store assets. Notes: Sofia's team does the assets. Terms as sent. |
| Rayking DM | slack (DM root) | D05S58U4SAK/1757090400.829462 | 2025-09-05T16:40:00Z | Frederick | Couldn't find anyone from Rayking on LinkedIn. Parking it for now, we still owe them an answer. |
| Arthur's cash note | slack (reply under the banker root + counter UPDATE) | C07C2866011/1759251900.005166 | 2025-09-30T17:05:00Z | Arthur | Checked SVB with Leonard this morning: that $10K first-look never hit the account. Their bank sent it back because they put Calm Play as the beneficiary and the account is in Harmony Games' name. They're resending it next week, so it'll land in October. |
| Robert's relay | slack (reply under the 70 % D1 root + counter UPDATE) | C07C2866011/1758909900.662794 | 2025-09-26T18:05:00Z | Robert | Off topic but I'm in here anyway: someone I know at Copperleaf Games, a small publisher, saw DD and emailed me out of the blue: "We'd do 28% of net to you, a $32,000 advance net 30 from signature, 40,000 installs a month for 12 months, mobile stores only, respond by Oct 17. Jonas Weber, Copperleaf, jonas@copperleafgames.com" |
| Kestrel post | slack (root) | C07C2866011/1759176900.065118 | 2025-09-29T20:15:00Z | Robert | Got a call from Kestrel. They've frozen every outside signing for the year, so whatever they had on the table with us is off. |
| standing line | slack (reply under the Matthew root + counter UPDATE) | C096HFA5Z8W/1758915000.867092 | 2025-09-26T19:30:00Z | Leonard | On the numbers going out: the May one-pager only had the paid-traffic numbers on it. Anyone who got it and still has an offer in with us hears the organic figure from us, $0.50 D30 ARPI, before we go any further with them. Fred, one short note each, left in your Gmail drafts, and I'll read them with you first. |
| analytics pointer | slack (root) | C069FF9Q57S/1758912000.686342 | 2025-09-26T18:40:00Z | Arthur | A tech lead at a publisher asked me about Singular deep links for DD. Notes are on ENG-2362. |
| ENG-2362 comment | linear · comments | lc_674982ffdca63f854ec6f591 | 2025-09-26T18:32:00Z | Arthur | Redwood Arcade's tech lead, Mei Tanaka (mei@redwoodarcade.com), emailed me about deep links while they look at DD, and put their offer at the bottom for whoever handles this. Pasting it here for the record: "We'd do 24% of net to HG, a $25,000 advance net 45 from signature, 40,000 installs a month for 12 months, mobile stores only, respond by Oct 31. Mei Tanaka, Redwood Arcade" |
| ESG thread | gmail (Leonard, Frederick copies) | frederick.stone@harmonygames.co/1844620296192667598 | 2025-09-29T17:30:00Z / 2025-09-30T16:10:00Z | PERSON_2694 → Leonard, cc Frederick; Leonard | Leonard, we're tied up on an arbitration until Nov 7. The earliest I can turn a license for Domino Delights for signature is Nov 14. ¶ OK. Fred, that makes Nov 14 our signing date, not Oct 31. |
| Anika, Lena contacts | contacts · contacts | 5373edb55ca853d6052ecce5 / 1d6fd505d2fea08fa0f26c6e | — | — | Anika Rao, Partnerships, Kestrel Group; Lena Fischer, Sunfold Mobile |
| Oakline Games term sheet | gdocs + gdrive (shared with Frederick) | f_27cac0eed300cc33eeb4fd | same day as its mail | Oakline Games | 30% of net to Harmony Games, $30,000 advance ($10,000 first-look payment within 5 days of this sheet, credited to the advance, the remaining $20,000 net 30 from signature), 20,000 installs a month for 12 months, mobile stores, respond by Oct 24 |
| Tallwater Games term sheet | gdocs + gdrive (shared with Frederick) | f_e8cb875d5b7c8d9972d259 | same day as its mail | Tallwater Games | 25% of net to Harmony Games, $60,000 advance net 30 from signature, 30,000 installs a month for 12 months, mobile stores, respond by Oct 17 |
| Sunfold Mobile term sheet | gdocs + gdrive (shared with Frederick) | f_8ddfb9901891eb8e9dcab8 | same day as its mail | Sunfold Mobile | 30% of net to Harmony Games, $20,000 advance net 45 from signature, 50,000 installs a month for 12 months, mobile stores, respond by Oct 31 |
| Harbor Lane Games term sheet | gdocs + gdrive (shared with Frederick) | f_d72e8b34e7496f0de668bc | same day as its mail | Harbor Lane Games | 20% of net to Harmony Games, $25,000 advance net 60 from signature, 25,000 installs a month for 12 months, mobile stores, respond by Oct 24 |
| Wavecrest Play term sheet | gdocs + gdrive (shared with Frederick) | f_a6a5647f977d4638b2b8b1 | same day as its mail | Wavecrest Play | 22% of net to Harmony Games, $15,000 advance net 60 from signature, 15,000 installs a month for 12 months, mobile stores, respond by Oct 31 |
| Moonrail Studios term sheet | gdocs + gdrive (shared with Frederick) | f_464839da025a0a01f53979 | same day as its mail | Moonrail Studios | 26% of net to Harmony Games, $30,000 advance net 30 from signature, 35,000 installs a month for 12 months, mobile stores, respond by Oct 24 |
| Northglow Publishing term sheet | gdocs + gdrive (shared with Frederick) | f_3eccf6e0bb63955dc51e27 | same day as its mail | Northglow Publishing | 35% of net to Harmony Games, $50,000 advance net 30 from signature, 60,000 installs a month for 12 months, exclusive across all digital storefronts and platforms, including PC and web, respond by Oct 31 |
| Pinegrove Games term sheet | gdocs + gdrive (shared with Frederick) | f_5f3ef4a4760d18e696a41a | same day as its mail | Pinegrove Games | 30% of net to Harmony Games, $40,000 advance net 30 from signature, 45,000 installs a month for 12 months, mobile stores, ownership of the full source code and build pipeline passes to Pinegrove at signature, respond by Oct 24 |
| Oakline Games thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822838564 | 2025-05..09 by tranche | Marek Sobol | Live; sent: Intro only |
| Tallwater Games thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918823428620 | 2025-05..09 by tranche | Paola Duarte | Live; sent: May one-pager |
| Sunfold Mobile thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918823258769 | 2025-05..09 by tranche | Lena Fischer | Live; sent: Intro only |
| Harbor Lane Games thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918823445589 | 2025-05..09 by tranche | Diego Reyes | Live; sent: May one-pager |
| Wavecrest Play thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918823344908 | 2025-05..09 by tranche | Sofia Lindqvist | Live; sent: May one-pager |
| Moonrail Studios thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822811962 | 2025-05..09 by tranche | Anika Rao | Withdrawn; sent: May one-pager |
| Northglow Publishing thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822429064 | 2025-05..09 by tranche | Callum Ross | Out on rights; sent: Intro only |
| Pinegrove Games thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918823323729 | 2025-05..09 by tranche | Elena Petrova | Out on rights; sent: Intro only |
| Fernhollow Media thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822912178 | 2025-05..09 by tranche | Rhys Morgan | Passed; sent: May one-pager |
| Quietbay Games thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822894896 | 2025-05..09 by tranche | Nadia Haddad | Passed; sent: May one-pager |
| Slatewood Mobile thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918823167383 | 2025-05..09 by tranche | Yuki Sato | Passed; sent: Intro only |
| Ironbridge Interactive thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822812534 | 2025-05..09 by tranche | Tessa Hale | Passed; sent: Intro only |
| Tidewell Studios thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822727407 | 2025-05..09 by tranche | Omar Khalil | Passed; sent: Organic note |
| Marlin Play thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918823060205 | 2025-05..09 by tranche | Greta Holm | Passed; sent: Organic note |
| Kitebridge Games thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918823167536 | 2025-05..09 by tranche | Ivo Novak | Waiting on us; sent: Organic note |
| Orchard Lane Games thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822627795 | 2025-05..09 by tranche | — | No reply; sent: May one-pager |
| Summit Mobile thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822746195 | 2025-05..09 by tranche | — | No reply; sent: May one-pager; automatic acknowledgement only |
| Silverlake Mobile thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822773098 | 2025-05..09 by tranche | — | No reply; sent: Intro only |
| Cedarbrook Play thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822506013 | 2025-05..09 by tranche | — | No reply; sent: Intro only |
| Foxglove Games thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822804025 | 2025-05..09 by tranche | — | No reply; sent: Organic note |
| Riverstone Interactive thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918823170401 | 2025-05..09 by tranche | — | No reply; sent: Organic note |
| Bellwether Arcade thread | gmail (Frederick's mailbox) | frederick.stone@harmonygames.co/1842077918822759281 | 2025-05..09 by tranche | — | No reply; sent: Organic note |

Oakline's Sep 29 message says: 'Confirming our finance team sent the $10,000 first-look payment by wire today, ref OAK-2291. The remaining $20,000 of the advance stays payable net 30 from signature.' Moonrail's signature reads 'Anika Rao · Partnerships · Moonrail Studios, a Kestrel Group studio'.

| Thread class | Planned wording |
|---|---|
| Tranche 1 outbound (May, one-pager) `f_4b3ef3dcf76258a6fda5cd` | Hi {first}, I lead marketing at Harmony Games. Our first title, Domino Delights, is live on iOS and Android in the US, and we're exploring publishing partners for new markets. One-pager attached with early numbers. Open to a chat? |
| Tranche 2 outbound (Sep 8–12) `f_fd467bd2ae0c6d4f3bd2bc` | Hi {first}, I'm at Harmony Games. We're looking at a publishing partner for Domino Delights on mobile, and I'd love to compare notes. Happy to share numbers if there's interest. |
| Tranche 3 outbound (Sep 24–25) `f_fd467bd2ae0c6d4f3bd2bc` | Hi {first}, Harmony Games here. We're talking to publishers about Domino Delights on mobile. On organic traffic we see $0.50 D30 ARPI. Worth a call? |
| Pass `frederick.stone@harmonygames.co/1842077918822912178` | {'Fernhollow Media': "Thanks for thinking of us, but we'll pass on Domino Delights. It isn't a fit for our slate this year.", 'Quietbay Games': "Appreciate the note. We're going to pass, tile games aren't something we publish.", 'Slatewood Mobile': "We had a look and we'll pass for now. Our slate's full through next year.", 'Ironbridge Interactive': "Thanks, but we'll pass. We only take titles with a bigger live audience.", 'Tidewell Studios': "Not for us, so we'll pass on this one. Good luck with it.", 'Marlin Play': "We've decided to pass on Domino Delights. Thanks for sending it over."} |
| Term cover note `frederick.stone@harmonygames.co/1842077918823428620` | {'Oakline Games': 'Good to hear from you. Our term sheet for Domino Delights is in your Drive now.', 'Tallwater Games': "Thanks for picking this back up. I've shared our term sheet with you in Drive.", 'Sunfold Mobile': "Thanks for the note. Term sheet's shared with you in Drive, let me know what you think.", 'Harbor Lane Games': "Timing works for us. I've put our term sheet in Drive and shared it with you.", 'Wavecrest Play': 'Happy to talk. Sharing our term sheet for Domino Delights with you in Drive now.', 'Moonrail Studios': "Great, we're interested. You should have our term sheet in Drive.", 'Northglow Publishing': "Thanks, this fits what we're looking for. Our term sheet is shared with you in Drive.", 'Pinegrove Games': "Thanks for reaching out. We've shared a term sheet with you in Drive."} |
| Kitebridge `frederick.stone@harmonygames.co/1842077918823167536` | Thanks, this looks interesting. Could you send D7 by country before we go further? |
| Summit acknowledgement `frederick.stone@harmonygames.co/1842077918822746195` | Thanks for contacting Summit Mobile. This is an automatic reply. Our partnerships team reviews submissions every month. |

### Integrations and companions

Companions from `references/universe_kb/by_universe/synthcut/integrations.json`:

| Service | INT id | Companion | Decision |
|---|---|---|---|
| gcal | INT-11 | invitation mails for `evt_43fda04cd11b9d58a05161`, `evt_881d3e07c598b2205a7ff3` in each attendee mailbox | seed them, plus one GCal copy per attendee calendar |
| gdrive | INT-13 | Google Drive Slack app DMs for shares | integration_exceptions at injection: shares of `f_5e355d03f6eb6a4e866ead` and the term sheets sit in drive sharing rows only |
| linear | INT-03, INT-04, INT-05 | linear[bot] PR comment; Slack DM notifications; digests | no PR for the comment; declared exception for `lc_674982ffdca63f854ec6f591` |
| slack | INT-22 | '[Slack] … sent you a message' mails | optional, none seeded: replies are in channels |
| trello | INT-21 | Trello → Slack: no integration exists | none |
| gmail | — | no INT source maps to gmail itself | none |
| gdocs / gsheets / gslides | INT-13 (google_drive) | as gdrive | as gdrive |
| contacts | — | no integration | none |
| snowflake | — | not writable, not seeded | none |

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
  [ok] services_carrying_weight: 11 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: skipped (--design: no SQL yet)
  [ok] seeded_ids_exist_in_sql: skipped (--design: no SQL yet)
  [ok] anchors: 3 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 15 fragments; need ≥ 12
  [ok] ask_fragment_services: 11 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 15 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 13 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 26; need ≥ 24 (source-defined: True) (requester-confirmed cohort_exception)
  [ok] evidence_surfaces: 5 surfaces over 5 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 69; need ≥ 60
  [ok] call_budget: unconditional (verified) floor 203 of 203 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 180 (requester-confirmed volume_exception)
  [ok] call_budget_spread: 10 services in budget; largest share outside the per-record phase 41% (≤ 50%)
  [ok] traps: 21 traps across 11 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 8 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 4 supersessions (4 with versions in ≥ 2 services, 1 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: skipped (--design: no SQL yet)
  [ok] distractors: 7 distractors of 7 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 10 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 8 chains with 8 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] mechanism_portfolio: 8 portfolio entries, each a mechanism-enum id with trap/chain nodes, a requirement, a natural-reading fallback and a prior family with its reason
  [ok] artifact_fields: declared ['gradable_surface']: paths relative, digests sha256
  [ok] hidden_authorities: 3 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 2 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 14 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 13 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 8 writes over 5 services; each must depend on findings
  [note] volume_exception: call-budget floor 180 and per-record floor 60 replace 500 and 300; every other extreme target applies except the cohort floor below — reason: 26 publishers and 10 sets of terms; mail and calendars are bulk-readable, so hon; requester confirmation: task author in chat on 2026-11-06: 'my task is a long horizon task soo i want ov
  [note] cohort_exception: cohort floor 24 replaces 40; surfaces, surface services, why_no_bulk and short_circuit still apply — reason: no natural 40-record publisher cohort exists; padding it would add always-pass r; requester confirmation: task author in chat on 2026-11-06: 'my task is a long horizon task soo i want ov
```

`gradable_surface.py validate` and `gradeable-report` (verbatim):

```
GRADABLE SURFACE (01_Gradable_Surface.json): PASS · 72 slots · weight 242 · mechanism share 64.9% (reported, not gated) · weight by class {'delivery': 11, 'direct': 74, 'aggregate': 50, 'write_content': 107}
SURFACE.GRADEABLE PASS · 72 slot(s) · {'GRADABLE': 72}
```

`hardness_v2_check.py --design` (verbatim; dispositions in §5 Liveness flags):

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      4 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 6 requirements: {'R5': ['DONE', 'DATE'], 'R3': ['CORR', 'INPUT'], 'R2': ['ALIAS'], 'R1': ['FILT'], 'R6': ['EXC'], 'R12': ['FOLLOW']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   8 of 8 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     7 weight-5 total(s); 7 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  CLEAN      RULE_IN_PROMPT  no run of 8 resolver words in the prompt  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

S9b prior forecast (UNCALIBRATED, advisory, pre-registered): ledger id `hev_49facf6ed134c068`; mechanism rates are disclosed overrides sourced from the completed tasks (`plan/run_forecast.sh`).

```
  V3: P(all four difficulty gates) 0.476-0.680 across scenarios; value of information (first scenario): ['rule:DONE', 'rule:CORR', 'rule:ALIAS']
  correlated  whole    V3 E[avg] 0.654 [0.494, 0.804] P(all) 0.476
  independent whole    V3 E[avg] 0.624 [0.555, 0.696] P(all) 0.680
  source      whole    V3 E[avg] 0.624 [0.555, 0.696] P(all) 0.680
```

**Lazy-solver pass.** One broad search per service, first hits, no thread opens, stop at the first conclusion: it reads the hub, the rule doc, the sheet, each thread and term sheet, and loses every channel, scoring 35.1 % on the surface (`plan/policy_scores_output.txt`). Every point it scores comes from controls; no leak found.

**Literal-value sweep (planned text).** '$40,000' for Tallwater only in the call note; '30,000' for Sunfold only in the card comment; 'Nov 14' only in the ESG thread; 'beneficiary' only in Arthur's note; 'Kestrel' only in the post, Anika's signature and her contact. **Wording sweep.** Arthur's note and the standing line don't use the word 'publisher'; Robert's relay and the #analytics pointer do, on purpose, so the two off-sheet offers stay findable (`C07C2866011/1758909900.662794`, `C069FF9Q57S/1758912000.686342`). **The rest stands.** No later record re-asserts an amended clause.

### Self-review

Walked `Evals/1_Prompt_Eval.md` §2.1 (UGT), §2.2 (feasibility), §3.2 (cross-service coherence) and `Evals/0_Injection_Quality_Eval.md` Check C against this design.

| # | Category or decision point | Counter-reading (strongest argument it fails) | Resolution and evidence |
|---|---|---|---|
| 1 | temporal | the Sep 30 hub falls after the seed bound in PT or UTC | 23:10Z Sep 30 is before freeze 2025-10-01T00:00Z, and every T value in build_scenario.py is earlier (`frederick.stone@harmonygames.co/1844732284109533347`) |
| 2 | semantic | 'given us terms or told us no' could leave out a person who only reached a founder | Jonas and Mei gave terms to Robert and Arthur, so they count; their addresses are in the relay and the comment (`C07C2866011/1758909900.662794`, `lc_674982ffdca63f854ec6f591`) |
| 3 | cross-service referential | Kestrel maps to no record Frederick can see | her signature and Contacts row carry it (`5373edb55ca853d6052ecce5`, `frederick.stone@harmonygames.co/1842077918822811962`) |
| 4 | quantitative | seeded replies leave base reply counters stale | hazard Q01 acknowledged; SQL updates them (`C07C2866011/1757345405.134829`) |
| 5 | state/lifecycle | a comment on a closed or stale ticket fails the task | ENG-2362 is Todo, assigned to Arthur, and the comment is his (ENG-2362) |
| 6 | identifier/format | a seeded Linear comment id breaks the contract | minted to the base form and checked at injection (`lc_674982ffdca63f854ec6f591`) |
| 7 | other | advances this size look implausible for a game earning $381 in September | publishers buy on the one-pager and fund UA themselves; figures are modest, and Leonard's own line prices 1 million installs at $500K (`D05S58U4SAK/1758736747.409459`) |
| 8 | Oakline banked | the strongest alternative holds: $10,000: Marek confirms the wire | Arthur's later note (`C07C2866011/1759251900.005166`); rule doc: banked means in the SVB account (`f_5e355d03f6eb6a4e866ead`) |
| 9 | Oakline Q4 cash | the strongest alternative holds: $20,000: the first $10,000 already came | same note: resending next week; Dec 14 for the balance (`C07C2866011/1759251900.005166`, `f_27cac0eed300cc33eeb4fd`) |
| 10 | Tallwater advance | the strongest alternative holds: $60,000 in the term sheet | Leonard's later call note (`evt_43fda04cd11b9d58a05161`); rule doc: latest terms, wherever they are |
| 11 | Moonrail status | the strongest alternative holds: Live: its sheet is open | Robert's post on Kestrel (`C07C2866011/1759176900.065118`), Anika's signature (`frederick.stone@harmonygames.co/1842077918822811962`), Contacts `5373edb55ca853d6052ecce5` |
| 12 | Copperleaf in | the strongest alternative holds: out: not on the sheet, no term sheet | rule doc: came to one of the four of us, however it reached us; their note pasted in by one of us counts (`C07C2866011/1758909900.662794`) |
| 13 | Redwood in | the strongest alternative holds: out: an engineering note | same rule; Arthur pastes her note (`lc_674982ffdca63f854ec6f591`) |
| 14 | Northglow | the strongest alternative holds: Live: the best numbers | grant covers PC and web (`f_3eccf6e0bb63955dc51e27`); founders keep non-mobile rights (`C07C2866011/1756140953.197759`) |
| 15 | Pinegrove | the strongest alternative holds: Live: mobile stores only | ownership of the code passes to Pinegrove (`f_5f3ef4a4760d18e696a41a`); founders keep code (`C07C2866011/1756140953.197759`) |
| 16 | Sunfold installs | the strongest alternative holds: 50,000 in the term sheet | Frederick's later comment (`68dbfe80ef9c41b4f4fa8fe9`); rule doc: latest terms |
| 17 | Signing date | the strongest alternative holds: Oct 31 | rule doc: if ESG gives a later date, use theirs; Leonard's reply (`frederick.stone@harmonygames.co/1844620296192667598`) |
| 18 | Harbor Lane and Wavecrest Q4 cash | the strongest alternative holds: their full advances | term sheets (`f_d72e8b34e7496f0de668bc`, `f_a6a5647f977d4638b2b8b1`) with the date above |
| 19 | Who gets a draft | the strongest alternative holds: Moonrail too, or everyone | standing line: got it and still Live (`C096HFA5Z8W/1758915000.867092`); sheet column (`f_fd467bd2ae0c6d4f3bd2bc`) |
| 20 | Rayking | the strongest alternative holds: No reply, or answered | they wrote and the last message is theirs: Frederick's is an unsent draft to Leonard (`frederick.stone@harmonygames.co/1842348778705877030`), and his LinkedIn line (`D05S58U4SAK/1757009185.631739`) is closed by his Sep 5 DM (`D05S58U4SAK/1757090400.829462`) |
| 21 | Appodeal | the strongest alternative holds: Live: it made a proposal | no rev share or advance in writing, and the last message is theirs (`frederick.stone@harmonygames.co/1830012626042968381`) |
| 22 | Summit | the strongest alternative holds: answered | automatic acknowledgement (`frederick.stone@harmonygames.co/1842077918822746195`); rule doc says it doesn't count |
| 23 | Tilting Point | the strongest alternative holds: No reply | the rule doc names its form as out of scope (`frederick.stone@harmonygames.co/1842443183462721250`, `f_5e355d03f6eb6a4e866ead`) |
| 24 | Tamatem | the strongest alternative holds: a publisher to add | rule doc: a name someone passed along doesn't count (`C48D58CD7FBD/1748974617.722599`) |
| 25 | Homa and NCsoft | the strongest alternative holds: publishers in talks | rule doc: co-dev, engine or investment talks aren't part of this (`C096HFA5Z8W/1758210489.170809`, `C07C2866011/1757516293.887729`) |
| 26 | Sep 24 lead | the strongest alternative holds: add him | Leonard's mail (`frederick.stone@harmonygames.co/1844732284109533347`) over the DM (`D05S58U4SAK/1758736842.534589`) |
| 27 | Apple Arcade | the strongest alternative holds: a dominoes lead | not on the sheet, and no one came to us (`C07C2866011/1756261199.570279`) |
| 28 | Existing cards | the strongest alternative holds: new cards | the card says so (`68dab660c900179df4f5f92d`); first names map through the threads (`68d598387dea3e7fe85e3a0a`, `68d5913004a98be3b4c45408`) |
| 29 | Contacts present | the strongest alternative holds: add again, or add Appodeal and Rayking people | Leonard's mail (`frederick.stone@harmonygames.co/1844732284109533347`); Contacts `5373edb55ca853d6052ecce5`, `1d6fd505d2fea08fa0f26c6e` |
| 30 | Nudges | the strongest alternative holds: skip Summit because it acknowledged | the card (`68dab660c900179df4f5f92d`) and the rule that an acknowledgement isn't a reply (`f_5e355d03f6eb6a4e866ead`) |
| 31 | First pick | the strongest alternative holds: Northglow or Sunfold | rule doc ranks Live offers by 12-month value (`f_5e355d03f6eb6a4e866ead`) |
| 32 | volume | about 145 calls in a lean run is padding-driven | each write is one per publisher the founders asked for, and most are template-identical; reads decide status or terms (`68dab660c900179df4f5f92d`) |
| 33 | difficulty | eight channels near 0.5 is optimistic; measured pre-checks missed about 1 of 3 | at 0.7× the rates E[avg] is 74.2% and P(all gates) 0.73; the ledger view is 75.7% (`plan/policy_scores_output.txt`) |
| 34 | HARDNESS GATE output | a PASS at --design proves nothing about the SQL | true: injection re-runs hardness_gate on the SQL with every seeded id; this PASS covers structure only (§12) |

HARDNESS GATE (design) result is pasted verbatim above. Forecast `hev_49facf6ed134c068` is advisory and UNCALIBRATED.

Unresolved: no independent red-team review of this design (REDTEAM_* unset; fallback in §13); landing rates are UNCALIBRATED placement priors; `trello_create_card` on the UA/BD board and the calendar-description route are unproven until the pre-check; INT-13 and INT-05 companion choices are decided at injection with base_check.

```
STAGE GATE scenario: PASS — Task_Authoring/task_inputs · 01_Scenario_Design.md#e6f4b48f11e9 · 01_Hardness_Manifest.draft.json#70c5ac3229a5 · 01_Gradable_Surface.json#7e68f34657e8 · 00_Assigments.md#b715c1dcdbe1 · __context__#ec895c36b5f1 · __assignment__#a95625679300 · __policy__#dc4ab5df3cdd · __gate_policy__#f8638415ca2c · __review__#d0a6485ae7d0 · blocking 0 · warnings 0 · checks 33
[PASS] assignment.v3_context: Frederick Stone / Co-founder; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 3 output(s) present: 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json
[PASS] structure.inputs: 1 input(s) present: 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md)
[PASS] structure.sections: 19 required sections present and non-empty (01_Scenario_Design.md)
[PASS] structure.placeholders: no placeholders in 01_Scenario_Design.md
[PASS] evidence.storyline: 5/5 items carry a source pointer (min 80%)
[PASS] evidence.coherence_audit: 25/25 items carry a source pointer (min 100%)
[PASS] evidence.hidden_authorities: 3/3 items carry a source pointer (min 100%)
[PASS] evidence.delegation: 20/20 items carry a source pointer (min 90%)
[PASS] evidence.trap_register: 50/54 items carry a source pointer (min 90%); unsourced e.g. L376: 'COMPL | a publisher already turned down in a cancelled invite | completion elsewhere | cal'
[PASS] evidence.record_plan: 65/68 items carry a source pointer (min 80%); unsourced e.g. L727: 'gmail | — | no INT source maps to gmail itself | none'
[PASS] evidence.active_speakers: 6/6 items carry a source pointer (min 100%)
[PASS] tool.hardness_gate_design: hardness_gate --design pasted PASS; re-run PASS
[PASS] tool.persona_reach: persona_view reach pasted for frederick.stone@harmonygames.co and matches the re-run (105 channels)
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] kb.coherence_hazards: coherence audit cites 13 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 4 speaker rows carry their activity.json status_at_clock
[PASS] kb.integrations: companions listed per integrations.json (7 INT ids, services ['contacts', 'gcal', 'gdocs', 'gdrive', 'gmail', 'gsheets', 'gslides', 'linear', 'slack', 'snowflake', 'trello'])
[PASS] kb.storyline: timeline cited; cohorts []; trap_catalog ['B02', 'C01', 'D03', 'K02', 'P01']
[PASS] boundary.anchor_naming: 6 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] tool.redteam_dual: red team did not run (missing 01b_Redteam_Review.md, 01b_Redteam_Review.second.md); explicit fallback recorded: a fresh-context agent reviewed this design blind to the author's reasoning, with `hg.py`-o
[PASS] surface.valid: 72 slots, weight 242; geometry report-only, never gated: mechanism share 65%, always-pass share 35%
[PASS] forecast.preregistered: prior forecast pre-registered in the ledger: ['hev_49facf6ed134c068'] (UNCALIBRATED, advisory)
[SKIP] revise.intake: no MODE B report and no revision-intake section: nothing to take in
[PASS] reach.scenario: 43 scoped load-bearing ids YES for frederick_stone; 2 denied/unverified probe(s), not load-bearing, each with YES alternate_evidence_ids (27 planned seeds not yet in base: verified at the injection gate)
[PASS] review.counter_readings: 32 evidenced counter-readings (of 34 found; need ≥ 31) in 01_Scenario_Design.md
[PASS] review.coverage: self-review addresses all 8 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.draft.json is bound to the current assignment, policy, source context and freeze
[PASS] v3.role_review: current role-plausibility review recorded; semantic judgment belongs to the named reviewer
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## 13 Red team (dual)

RED TEAM UNAVAILABLE: REDTEAM_* is not set in this environment, so `tools/redteam_review.py --mode redteam --dual` cannot reach a reviewer endpoint.

RED TEAM FALLBACK: a fresh-context agent reviewed this design blind to the author's reasoning, with `hg.py`-only access to the base, hunting forks, base contradictions and leaks (findings and dispositions below). The counter-reading table in §12, the whole-universe name census with a positive control (`plan/name_census.json`) and the policy scores back it up. Two blind sweeps run at `/create-injection` before preflight. The requester delegated this choice on 2026-11-06. The waiver stays in Unresolved until a review or the pre-check covers it (learnings §44).

Fresh-context design review, 2026-11-06 (`plan/design_review.md`): 2 BLOCKER, 5 MAJOR, 17 MINOR. Every base quote it relied on for a truth change was re-read by the author through `hg.py`.

| Finding | Severity | Disposition | Evidence |
|---|---|---|---|
| F1 Pinegrove's code clause | BLOCKER | fixed: ownership of the source code passes to Pinegrove, so Out on rights can't fork and the pick can't flip | build_scenario.py TERM_DOCS, C07C2866011/1756140953.197759 |
| F2 Redwood's terms fit no Live form | BLOCKER | fixed: the ENG-2362 comment now quotes Mei's note, like Robert's relay | ENG-2362 |
| F3 Rayking and the LinkedIn line | MAJOR | fixed: seeded Sep 5 DM closes it; the rule now says the last message is theirs | D05S58U4SAK/1757009185.631739 |
| F4 Contacts count | MAJOR | fixed: the hub now says given us terms or told us no, 16 people, 14 adds, no masked names. The three lost writes are replaced by seven template nudge drafts on the card | build_scenario.py HUB, CARD |
| F5 Appodeal | MAJOR | fixed: Live now needs a rev share and an advance in writing | frederick.stone@harmonygames.co/1830012626042968381 |
| B1 term sheets against Frederick's Sep 24 words | MAJOR | fixed: every term sheet moved to Sep 25 or later, and the wire to Sep 29, so no line needs seeding into the DM | D05S58U4SAK/1758735819.982259 |
| L1 Copperleaf relay unfindable | MAJOR | fixed: the relay says a small publisher, and stays a reply; rate cut from 0.45 to 0.35 | C07C2866011/1758736960.824899 |
| F6, F7, F8 first-look wording, open to, rev share direction | MINOR | fixed: within 3 days of this sheet; respond by; to Harmony Games | build_scenario.py TERM_DOCS |
| F9 Tamatem | MINOR | fixed: rule sentence and a two-reading row | C48D58CD7FBD/1748974617.722599 |
| F10 handover wording | MINOR | fixed: after launch | build_scenario.py PB_NOTE |
| F11 unplanned thread bodies, control calls, sheet rows | MINOR | fixed: planned wording by class, both control calls and the two came-to-us rows are in §11 | build_scenario.py BODIES |
| B2 Calm Play as a former account name | MINOR | fixed: they put Calm Play as the beneficiary; the wrong July anchor is removed, and the analysis corrected | D05S58U4SAK/1738003879.776129, C07C2866011/1727980540.831209 |
| B3 Homa and NCsoft aren't Zombie Match only | MINOR | fixed: co-dev, engine or investment talks, even where DD came up | C096HFA5Z8W/1758210943.211579 |
| B4, B5 relay and cash note voice | MINOR | fixed: off-topic opener; Arthur checked SVB with Leonard | C07C2866011/1757345405.134829 |
| B6 Matthew root | MINOR | kept: passes, and the suggested opener would add the word publisher, which lowers the trap's landing rate | C096HFA5Z8W/1758147530.732569 |
| B7 SC-6 thread cited | MINOR | fixed: citation dropped | C08MCEP1B9B |
| B8 Partners doc against the sheet | MINOR | fixed: a note on the sheet | f_10dfa1b4236a7c35dcb632 |
| L2 T1 named | MINOR | fixed: the note says that $10K first-look, not Oakline | build_scenario.py ARTHUR_CASH |
| L3 T3 first name | MINOR | fixed: the post says Kestrel only | build_scenario.py KESTREL |
| L4 T9 names ESG | MINOR | fixed: the rule says our lawyers | build_scenario.py RULES |
| L5 read-and-done items counted as traps | MINOR | accepted: T10, T11, T13, T15, T16 and T20 are controls and decoys, not load-bearing; the eight channels carry the difficulty | §5 |
| L6 calendar description route | open | stays open: the pre-check must prove it (`evt_` note on the Tallwater call) | §10 |
| The sync doc is an agenda with no recorded decision | note | fixed: the rule now says the position from the August sync, not the position we agreed | f_26e1f9a86761e35049192a |

