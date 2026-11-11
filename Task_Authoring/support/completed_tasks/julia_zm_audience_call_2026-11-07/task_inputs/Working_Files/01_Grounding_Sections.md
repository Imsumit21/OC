# Grounding sections for /create-scenario (rev 5.1)

Design only: no prompt, Oracle Event or criterion text. Design of record: `00_Rev5_Design_Brief.md`, its Resolutions section first. Times are UTC. "Seed" means a planned record; everything else was read from base through `hg.py`, `persona_view.py` or `entity.py`.

## 0 Assignment, persona census and horizon note

**Universe.** key `synthcut` · label `Oct 1, 2025 (synth-cut)` · `Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)` · seed bound `2025-10-01T00:00:00Z` · `shutdown_rules_apply: false` · build `hg4-synth-sep30cut v16`.

**Assignment (`Working_Files/00_Task_Context.json`).**

| Field | Value |
|---|---|
| business_function | Product (Evals category: Product & Design) |
| persona_name | Julia Lawson |
| persona_role | Product Manager |
| competency | Marketing and GTM |
| task_skill | Analysis and synthesis |
| task_type | long-horizon |
| difficulty_mode | medium |
| universe_date_raw | October 1, 2025 07:00 |

**Loss budget.** Cap .85, from `difficulty_mode: medium`; the mode is never changed. Design target E[avg] 62 %, tighter than the playbook's Medium ceiling of 77 %. The target is the requester's. The forecast stays uncalibrated until it is re-run on the real surface (C13).

**Theme screen.** The storyline sits inside Zombie Match 3D. The requester accepted ZM as a product name (Analysis §12, 2026-11-07). Seeded text carries no outbreak, infection or plague words. Plague Race is avoided: base calls the live-op "plague race" at `C090N54TG79/1759173389.051889`, so no seed names it.

**Persona reach census.**

```text
REACH  Julia Lawson <julia.lawson@harmonygames.co>  Product Manager / Product
clock 2025-10-01

SLACK  user=EMPLOYEE_0005_SLACK_ID  visible channels=147 {'mpim': 52, 'public': 23, 'private': 47, 'im': 25}  messages=238131  public-not-member (UNVERIFIED)=44
  persona posts=31848 last post=2025-09-30  last activity in visible channels=2025-10-01
  C05433XK267    builds                                 public  mem=31  msgs=35617  2023-04-20..2025-10-01
  C05H8KVNU67    game-design                            private mem=27  msgs=22750  2023-07-16..2025-08-28 archived
  C050WGU41HR    engineering-bots                       private mem=35  msgs=19854  2023-03-29..2025-09-19
  C05V5FNLB9V    god-bugs                               private mem=31  msgs=16695  2023-10-07..2025-07-15
  C0880U9751A    zombie-match3d                         private mem=25  msgs=16250  2025-01-09..2025-09-30
  D076RBM29JS    D076RBM29JS                            im      mem=5   msgs=11174  2024-06-06..2025-09-29
  CC43664F351E   mpdm-julia.lawson--brian.foster--vince mpim    mem=4   msgs=9711   2024-06-26..2025-09-25
  D05GU6L0XFH    D05GU6L0XFH                            im      mem=5   msgs=9251   2023-07-16..2025-10-01
  D05QA585LTY    D05QA585LTY                            im      mem=5   msgs=6709   2023-09-21..2025-09-15
  C0553V44CE4    god-ui-ux                              private mem=30  msgs=5008   2023-04-21..2025-05-29 archived

GMAIL  mailbox=julia.lawson@harmonygames.co threads=253 messages=304 range=2023-07-16..2025-09-17
  threads by last-message month (recent): {'2025-04': 4, '2025-05': 2, '2025-06': 3, '2025-07': 5, '2025-08': 3, '2025-09': 1}
  top correspondents: leonard.hayes@harmonygames.co (94), robert@harmonygames.co (85), arthur.blake@harmonygames.co (50), victor.barnes@harmonygames.co (43), claire.morgan@harmonygames.co (40), calvin.price@harmonygames.co (38), [EMAIL_0072] (36), martin.walsh@harmonygames.co (33), SVC_1295_EMAIL (31), SVC_0251_EMAIL (28)

GCAL  own=['julia.lawson@harmonygames.co'] shared=[] events=748 (distinct ical_uid 253, cancelled 46)
  last event before clock=2025-09-29T16:30:00Z  next after clock=None
  by month: 2023-07:14 2023-08:50 2023-09:24 2023-10:35 2023-11:26 2023-12:24 2024-01:45 2024-02:22 2024-03:9 2024-04:21 2024-05:24 2024-06:39 2024-07:34 2024-08:35 2024-09:40 2024-10:27 2024-11:32 2024-12:32 2025-01:46 2025-02:18 2025-03:11 2025-04:23 2025-05:42 2025-06:31 2025-07:27 2025-08:8 2025-09:9

DRIVE  owned=28 {'application/vnd.google-apps.spreadsheet': 12, 'application/vnd.google-apps.document': 10, 'folder': 2, 'application/vnd.google-apps.presentation': 2, 'application/pdf': 2}
  shared-with=158 {'application/vnd.google-apps.document': 50, 'text/plain': 38, 'application/vnd.google-apps.spreadsheet': 32, 'application/json': 21, 'application/vnd.google-apps.presentation': 8, 'application/pdf': 7, 'text/csv': 2}
  shared by owner: {'Resource: -6481757892984311338': 100, 'leonard.hayes@harmonygames.co': 33, 'robert@harmonygames.co': 12, 'arthur.blake@harmonygames.co': 10, 'Resource: 7240535625619857401': 3}
  native visible: {'gdocs': 60, 'gsheets': 44, 'gslides': 10}  last modified visible=2025-09-30T16:30:39Z
  UNVERIFIED (domain/anyone, not owned/shared)=89 {'application/vnd.google-apps.document': 35, 'application/vnd.google-apps.spreadsheet': 27, 'application/json': 11, 'application/pdf': 10, 'application/vnd.google-apps.presentation': 6}

UNSCOPED (always visible): contacts, github, trello, linear, snowflake, confluence

LAST ACTIVITY (days before clock): slack_persona_post=2025-09-30 (1d), slack_visible_channels=2025-10-01 (0d), gmail=2025-09-17 (14d), gcal_last_event_before_clock=2025-09-29 (2d), drive_last_modified_visible=2025-09-30 (1d)
```

**Identities.**

```text
ENTITY email:julia.lawson@harmonygames.co  name=Julia Lawson  kind=person  emails=['julia.lawson@harmonygames.co']
  persona: julia_lawson - Product Manager / Product
  slack      id=EMPLOYEE_0005_SLACK_ID, name=Julia Lawson, real_name=Julia Lawson, email=julia.lawson@harmonygames.co, is_bot=False, deleted=False, messages=31848, first_post=2023-07-16, last_post=2025-09-30   [join: exact_email]
  gmail      mailbox=julia.lawson@harmonygames.co, threads=253, messages=304, first=2023-07-16, last=2025-09-17, thread_filename_alias=['jlawson@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=julia.lawson@harmonygames.co, owner_email=julia.lawson@harmonygames.co, summary=Julia Lawson — primary, events=748, last_event_before_clock=2025-09-29   [join: exact_email]
  gdrive     id=user_8140f09bf9f1, email=julia.lawson@harmonygames.co, display_name=julia.lawson@harmonygames.co, root_folders=['d_8140f09bf9f1b94cb8ee2d'], owned_items=28, last_modified=2025-09-11, files_shared_with=158   [join: exact_email]
  linear     id=usr_8140f09bf9f1b94c, email=julia.lawson@harmonygames.co, name=julia.lawson@harmonygames.co, is_active=True, last_activity=2025-09-23   [join: exact_email]
  github     login=PERSON_0005_GITHUB_USERNAME, name=Julia Lawson, email=julia.lawson@harmonygames.co, type=User, last_activity=2025-09-29   [join: exact_email]
  trello     id=793af7ca6940bf18eb516c75, username=julia.lawson, fullName=Julia Lawson   [join: exact_name]
  confluence id=user_EMPLOYEE_0005, account_id=acct_EMPLOYEE_0005, email=julia.lawson@harmonygames.co, display_name=Julia Lawson, is_active=True, last_activity=2025-09-21   [join: exact_email]
  contacts   contact_id=8140f09bf9f1b94cb8ee2dd7, name=Julia Lawson, email=julia.lawson@harmonygames.co, job=Product Manager, is_user=False   [join: exact_email]
  last activity: {'slack': '2025-09-30', 'gmail': '2025-09-17', 'gcal': '2025-09-29', 'gdrive': '2025-09-11', 'linear': '2025-09-23', 'github': '2025-09-29', 'confluence': '2025-09-21'}
```

Write identities: Linear `usr_8140f09bf9f1b94c`, GitHub `PERSON_0005_GITHUB_USERNAME`, Trello `793af7ca6940bf18eb516c75`, Slack `EMPLOYEE_0005_SLACK_ID`, Drive root `d_8140f09bf9f1b94cb8ee2d`. Calendar zone is Europe/Istanbul, and Julia says she is in Turkey (`D05GU6L0XFH/1758907319.711599`).

**Remit argument.** An interim audience read is plausible work for a Product Manager under a Marketing and GTM competency. Every source below predates the freeze.
- Julia already argues audience fit: "Techically, we'll get better d1-d3 from casuals and better long term from hardcores" (`C090N54TG79/1758569491.223089`). Going generic in the playable is her GTM position (`C090N54TG79/1758569629.722849`).
- She carries the content cost of the target: "I have 300 casual levels and nothing geared to midcore play" (`C090N54TG79/1759173561.454829`).
- The team names the gap as an audience question: Brian, "the most important factor here is which type of user we’re going to target" (`C090N54TG79/1759173183.428879`); Julia, "We never had a preference between casual or midcore" (`C090N54TG79/1759173509.076179`).
- She reads player reactions herself: "They are playing to please us" (`C090N54TG79/1758582083.678989`). The note gave the collection job to "Everyone" (`C090N54TG79/1758517286.431379`).
- She stays inside her remit by giving a read that feeds Leonard's later iterate-or-pivot call, never the call itself (brief §1).

**Effective profile.** `horizon: Long Horizon` → `effective_profile: extreme`, with `volume_exception`: requester confirmation 2026-11-07 ("accept all", Analysis §12), `call_budget_floor: 260`, `per_record_floor: 160`, about 300 necessary calls. The exception covers those two floors only. Other extreme targets still apply, and the C12 resolution says to stop and report rather than pad.

## 1 Storyline

Julia reads the friend sessions the Sep 22 note asked for. She gives Leonard one audience call, the Sep 29 "cards earlier" change is kept or held on that call, she closes out the session tickets and she tells Brian. The log and the leaders point to RPG and keep. The sessions that truly count point to casual and hold.

**Universe KB placement.** timeline: 2025-09-25 "Vision bot tooling matures" (`C05433XK267/1758803475.436309`). The timeline row dated 2025-09-30 says PR #476 was "opened and merged". That is wrong for this universe, because `harmonygames-Games/match3d#476` reads `state open, merged false`, so the row is not used.

cohorts.json: no fit — the 60 session tickets are seeded and no base cohort holds friend sessions. LIN-S02 and LIN-OPEN-ZOM give only the ZOM state vocabulary, so no members and no `hazards_inside` ids are taken from them.

**trap_catalog precedents.**

| Id | Precedent | Use here | Record |
|---|---|---|---|
| C01 | A reply corrects an earlier reading | K5 reply under a quiet thread | `C090N54TG79/1758581651.167799` |
| C02 | A resolution is stated, another person undercuts it | K3: Done ticket and owner's line, then Arthur's inline note | `harmonygames-Games/match3d#476` |
| D05 | Stale against current | Older "Male, RPG gamers" GDD against the session read | `f_89fadbc54660c9881d8cf9` |
| B03 | CodeRabbit volume | K3's note sits among the PR's 26 existing review comments | `harmonygames-Games/match3d#476` |
| B04 | Jenkins volume | Run #15 and the K5 build sit in `#builds` | `C05433XK267/1758803475.436309` |
| P01 | Shared first names | Marcus, Martin and Claire on forms and tickets (section 1c) | `usr_c77c50cc15c5342d` |
| N01 | ZOM-n and ENG-n twins | Every seeded ZOM number has an unrelated ENG twin | `ZOM-559` |
| K02 | App-name lineage | "Puzzles vs. Zombies" on the panel mail is ZM | `leonard.hayes@harmonygames.co/1843922088670958384` |

**Anchors per service.**

| Service | Anchor | Id | Role |
|---|---|---|---|
| Slack | The note | `C090N54TG79/1758517286.431379` (reply_count 0, thread_ts null) | Rule hub |
| Slack | Sep 29 change | `C090N54TG79/1759171957.791499`, `C090N54TG79/1759172166.547199` | The live decision |
| Slack | Sep 29 lean | `C090N54TG79/1759176983.189479`, `C090N54TG79/1759178344.878219` | Where the wrong answer agrees with the leaders |
| Slack | K5 root | `C090N54TG79/1758581651.167799` (rc 15, users 2, latest `1758582083.678989`) | Seeded reply on Sep 25 |
| Slack | K4 DM | `D076RBM29JS` (Sep 23: 23 messages, `1758625378.489139` to `1758640673.917619`) | Seeded line after 15:17Z |
| Slack | F root | `D05GU6L0XFH/1758901945.292269` (rc 1, users 1, latest `1758902134.905169`) | Seeded reply on Sep 26 |
| Slack | Run #15 | `C05433XK267/1758803475.436309` (Sep 25 12:31Z, Success, `Blake/visionBot`) | The cited pass |
| Slack | Panel audience | `C090N54TG79/1758691397.679889` (rc 2, users 2), reply `C090N54TG79/1758729342.721289` | Panel definition home |
| GitHub | Open PR | `harmonygames-Games/match3d#476` (26 review comments, rev_1, rev_2, updated 09-30T19:03:57Z) | Next ids `#rc_27`, `#rev_3` |
| Linear | Samsung bug | `ZOM-559` (Todo, created 09-22T14:54:46Z by `usr_65c76e0b87aa7e9b`, assignee `usr_bdf01b53c6a92c5e`) | Stays Todo |
| Linear | Id floor | `ZOM-566` (created 09-30T16:26:02Z), next `ZOM-567`, `team_ZOM`, project dbab77c7-f871-4888-abf8-d98b52a41624 | Batch date floor |
| Gmail | Panel results | `leonard.hayes@harmonygames.co/1843922088670958384` | Leonard only; forward seeded to Julia |
| Docs | Older GDD | `f_89fadbc54660c9881d8cf9` ("Zombie Match 3D Testing and GDD", owner Robert, modified 2025-06-19, shared with Julia) | Distractor |
| Drive | Julia's root | `d_8140f09bf9f1b94cb8ee2d` | Home of her seeded Doc and Sheet |
| Trello | ZM ROADMAP | `6851a6569f3bf818760632ab`, Backlog `68c451221ebabaf255a7d16b`, next idShort 80 | Status echo only |
| GCal | Julia's calendar | Last base event `evt_f08d0e87c8c7aafe580d42` (Sep 29) | One seeded event |
| Confluence | QA runbook | `page_qa_runbook` | Read context, not injected |

**K5 build id (proposal, for section 2 to confirm).** `Match3D Android - #1943 - main`, Success at `C05433XK267/1758575557.575349` (Sep 22 21:12Z). The post says neither "dev" nor "store". It only shows a non-Submission job, so the Route Hunt row 3 bypass stays open as a second fair path. K5's .40 find odds should be read with that in mind.

**Coupling seams.**
- A rule in Docs changes a value read in Linear: the stability clause decides whether 11 Samsung tickets count, and the ticket that seems to clear them is answered only on GitHub (`harmonygames-Games/match3d#476`).
- A rule in Slack changes a Sheet row and a Linear state: the audience rule and Brian's DM line (`D076RBM29JS`) flip 9 rows that tie out on form, ticket and log.
- A record's meaning depends on the cohort: Claire's mail joins only through the 13 tickets that share her name and date.
- An exception the main instructions do not carry: a reply under `C090N54TG79/1758581651.167799` turns ordinary-looking ids into not-counted through the store-builds clause.
- A default that favours the wrong path: no clear lead means keep (C14), so a run must establish the casual lead to change the action.

**Originality.** This is not the Combo Fighters launch record, the 133-PR residue register, the RC-flag gate or the art-canon handoff control, and it takes no cohort, number, flag vocabulary or surface combination from `hardness_calibration.md`. The Sep 22 note and the Sep 29 lean are base (`C090N54TG79/1758517286.431379`); the sessions are new.

## 1a Coherence audit

Scope: every record a correct run opens. Walked with `hg.py` over the anchors, chains, channels and rule homes, plus `coherence_hazards.json` (59 hazards indexed in this universe's file, 6 categories). Row format: record · category · fields · pointer · hazard id · disposition.

### QC categories (seven)

| Record | Category | Fields | Pointer | Hazard id | Disposition |
|---|---|---|---|---|---|
| Timeline row on #476 | Temporal | KB says merged; PR says open | `harmonygames-Games/match3d#476` | none in KB | Avoid: use the PR record, never the KB line |
| #476 undated `reviewed` rows | Temporal | `created_at` null, actor empty | `harmonygames-Games/match3d#476` | T01 | Avoid: date only from `github_reviews.submitted_at`; ungraded |
| Panel mail thread | Temporal | Messages at Sep 22 00:32 and 03:44Z | `leonard.hayes@harmonygames.co/1843922088670958384` | T02 | Avoid order claims; forward is dated after 03:44Z |
| ZM ROADMAP board | Temporal | Action date against `dateLastActivity` | `68d1eb90bef538c7c5c5599d` | T06 | Seeded card sets both to the same moment |
| Slack "Beta target: Sep 30", list "BETA: Oct 10" | Temporal | Date in prose and list name | `C05KNDCHAAG/1757704290.799329` | SC-13, not a hazard id | Avoid: no beta date in any seed |
| Session labels | Semantic | "casual", "RPG" as session labels | `C090N54TG79/1758517286.431379` | S03 | Folded in: one label per session, set by the audience rule |
| "25–45" in the note | Semantic | Age band or headcount | `C090N54TG79/1758517286.431379` | none in KB | Designed reply settles it as age (base meaning at `D04UP2L3E3S/1758515667.845849`, not Julia-visible) |
| "Marcus" as a name on forms | Semantic | Marcus Bennett, Marcus Lee, Trello Marcus | `usr_c77c50cc15c5342d` | S04 | Avoid: full name on each form |
| Seeded pointer from note thread to Doc | Cross-service referential | Slack doc links use native ids, never `f_` ids | `C090N54TG79/1758517286.431379` | R04 | Point by title, with no constructed URL |
| Arthur's note and its mirror | Cross-service referential | Comment and Slack copy | `C093LEZGF6J/1759258475.735779` | R06, R07 | Mirror text matches the comment; base mirrored #476 CodeRabbit rows, so the mirror is planned |
| GitHub notification mail for #476 | Cross-service referential | Redacted subject | `harmonygames-Games/match3d#476` | R03 | Not seeded (INT-12 optional) |
| Calendar event and invite mail | Cross-service referential | Mail with no GCal row | `evt_f08d0e87c8c7aafe580d42` | R08 | Event seeded with no invite mail |
| Slack keys that do not exist | Cross-service referential | ZOM keys in seeds | `ZOM-566` | R01 | Seeds cite only ZOM-559 and seeded ZOM-567 to ZOM-627 |
| Thread counters on seeded roots | Quantitative | `reply_count`, `reply_users_count`, `latest_reply` | `C090N54TG79/1758581651.167799` | Q01, Q02, Q03 | All five roots checked clean against their replies; bump all three per section 11 |
| Panel "3-3.5" against "2.5-3" | Quantitative | Star range | `C090N54TG79/1758517286.431379` | none in KB | Julia sees only 3-3.5; the other is at `D04UP2L3E3S/1758515667.845849`, not used |
| Forward held in two mailboxes | Quantitative | Same RFC message, different content | `leonard.hayes@harmonygames.co/1843922088670958384` | Q10 | Keep both copies byte-identical |
| Calendar copies of the seeded event | Quantitative | Copies disagree | `evt_b371a24b8dad3a2cd9f432` | Q11 | One copy per attendee, same fields |
| Run #15 and the bot's state | State/lifecycle | Branch-only pass, never on main | `C05433XK267/1758803475.436309` | L04 | Designed: dated human claim on `ZOM-567`, overturned by `harmonygames-Games/match3d#476#rc_27`; ticket names no PR, so L04 does not arise |
| ZOM-559 | State/lifecycle | Todo with no fix in base | `ZOM-559` | L03 | Stays Todo; no seeded fix, PR or build claim |
| Open issues on quiet people | State/lifecycle | Assignee activity | `usr_bdf01b53c6a92c5e` | L08 | Oliver is active at the clock; no quiet assignee in scope |
| #476 review state | State/lifecycle | Open, no human approval | `harmonygames-Games/match3d#476` | L09, L10 | Not a merged PR, so neither applies; do not call it merged |
| Done parent, open child | State/lifecycle | Parent implies child | `ZOM-567` | L06 | No parent links on seeded tickets |
| Julia's mailbox file names | Identifier/format | `jlawson@` file alias, `julia.lawson@` mailbox | `julia.lawson@harmonygames.co/1843554280387239889` | I03 | Keep the alias in file names, the real address in `user_email` |
| Date formats on seeded mail | Identifier/format | RFC-2822 and ISO-Z | `leonard.hayes@harmonygames.co/1843922088670958384` | I04 | Follow the mailbox's RFC-2822 shape |
| CodeRabbit author on rc_28 | Identifier/format | Comment author against timeline actor | `harmonygames-Games/match3d#476` | I07 | Use `PERSON_6026_GITHUB_USERNAME`; never grade the account (SC-50) |
| GitHub logins | Identifier/format | Tokens against real logins in the mirror | `harmonygames-Games/match3d#476` | I08 | Mirror shows `arthur.blake`, comment row `EMPLOYEE_0025_GITHUB_USERNAME` |
| Robert's Linear id | Identifier/format | `usr_Robert` is not `usr_` plus hex | `ZOM-559` | I10 | Keep as is; no ticket assigned to him depends on the shape |
| Seeded event rows | Identifier/format | Master plus instance, copy without attendee | `evt_b371a24b8dad3a2cd9f432` | I11, I13 | Single non-recurring event, copies only for attendees |
| Seeded Doc and Sheet | Identifier/format | Owner token; Drive name extension | `d_8140f09bf9f1b94cb8ee2d` | I14, I15 | Real owner emails, native Google types with no extension |
| Trello member | Identifier/format | Leonard is a token | `68d1eb90bef538c7c5c5599d` | I17 | Use `PERSON_6094_TRELLO_USER_ID` as the creator |
| Seeded Slack rows | Identifier/format | Raw shape; id against `sha256(channel\|ts)` | `C090N54TG79/1758517286.431379` | I01, I02 | Use the canonical shape of the note row and a computed id |
| #zombie-design membership | Other | `channels.json` lists leavers | `C090N54TG79/1757612613.847149` | SC-7, not a hazard id | Live humans are Leonard, Robert, Julia, Brian and Vincent; Marcus and Arthur left on Sep 11 at `C090N54TG79/1757612639.935649`. No seed from a leaver |
| Leonard's Oct 1 travel | Other | Brief premise; no base record found | `C090N54TG79/1759256665.045159` | none in KB | Keep the claim out of every seed; his base calendar has a meeting at Oct 1 20:30Z |

### Hazard citations by category (coherence_hazards)

- temporal: T01, T02, T06 (`harmonygames-Games/match3d#476`).
- semantic: S03, S04 (`C090N54TG79/1758517286.431379`).
- referential: R01, R03, R04, R06, R07, R08 (`C093LEZGF6J/1759258475.735779`).
- quantitative: Q01, Q02, Q03, Q10, Q11 (`C090N54TG79/1758581651.167799`).
- lifecycle: L03, L04, L06, L08, L09, L10 (`ZOM-559`).
- identifier: I01, I02, I03, I04, I07, I08, I10, I11, I13, I14, I15, I17 (`D076RBM29JS`).

### Known-issue cards touched (`known_data_issues/synthcut.md`)

| Cards | Touch | Pointer | Disposition |
|---|---|---|---|
| SC-8, 16, 30, 32 | ZOM ticket state read as proof | `ZOM-559` | Avoid; ZOM-475 stays out; no parent links; no In Review state |
| SC-1, 11, 12, 23 | Spend and CPI | `snowflake.AD_SPEND_DAILY` | No spend or CPI row anywhere |
| SC-13, 14 | BETA list name and flags | `6851a674975da1fe76e70d93` | Seeded card goes in Backlog, never that list |
| SC-19 | App versions | `C05433XK267/1758803475.436309` | Build names as Slack writes them, never `RAW_EVENTS` versions |
| SC-26 | ENG-2367 and later | `ZOM-566` | Never cited or seeded |
| SC-28, 38, 44, 65 | OKR numbers, Season Pass, tutorial funnel, playtime | `ZOM-566` | Avoid; gap 529 stays unused |
| SC-5, 36 | Victor Barnes | `C090N54TG79/1758517286.431379` | No role, not an observer |
| SC-6 | Brian's Gmail address | `D076RBM29JS` | Brian stays out of Gmail; his form is a Doc |
| SC-7 | Channel membership | `C090N54TG79/1757612639.935649` | Do not grade membership; Claire's and Marcus's reach is design only |
| SC-24, 60 | Tim, Josh Dempsey | `C090N54TG79` | Not used; no seed names either |
| SC-70 | Slack zones | `evt_b371a24b8dad3a2cd9f432` | Use calendar zones, never decisively |
| SC-18 | PR #477 residue family | `harmonygames-Games/match3d#476` | #477 not cited; #476 state read from data |
| SC-37 | Crash by level | `C08R27X0EAH/1758642623.835409` | No crash-by-level split; level 20 stays a ticket scope only |
| SC-50 | Bot author types | `harmonygames-Games/match3d#476` | Name CodeRabbit by content |

### Sibling-defect sweep

- Designed defect: a Done ticket on a Samsung scope. Linear search "samsung" (scan complete, 5 distinct issues; control "Homing out" hit `ZOM-559`): `ENG-1431` Canceled, `ENG-2285` Done, `ENG-2324` Done, `ENG-383` Done (all ENG team, created 2023-11 to 2025-05) and `ZOM-559` Todo. `ENG-2324` "Fix Samsung Startup Issues" names S23, S24 and S25. It is a fair result on the other team's board, not a defect: no seed cites it, and the collision test should include it.
- Designed defect: a human claim on a pass. Linear "vision bot" returns 0 with the same control, and "not reproduc" returns 0, so `ZOM-567` stands alone.
- Designed defect: a form contradicted elsewhere. `C090N54TG79` month search: "session" 0 hits and "Dev_" 0 hits, with control "friend" at 7 hits. All 7 friend hits were read. Brian's artist-friend hits (`C090N54TG79/1758570425.654109`) are grounding only and Leonard's friend (`C08R27X0EAH/1758738754.255909`) is excluded from the cohort.
- Julia's mailbox (`julia.lawson@harmonygames.co/1771782257114362264`): "playtest" hits are 2023 GoD Weekly Playtest invites (search capped at 12, read as a family). "vision" has 3 substring hits, all "Division of tasks" on one invite, so they are false positives. Control "Join your team on Slack" hit 1.

### hazard_acknowledgements candidates

| Hazard id | Resolution | Basis | Pointer |
|---|---|---|---|
| T01 | excluded | Undated rows neither modified nor cited as dates | `harmonygames-Games/match3d#476` |
| L04 | excluded | `ZOM-567` is referenced by no PR | `ZOM-567` |
| Q11 | excluded | Base event copies are not touched | `evt_b371a24b8dad3a2cd9f432` |

The K3 claim is a `dated_claim` by design, not a hazard: Vincent's line on `ZOM-567` is attributed and dated, and `harmonygames-Games/match3d#476#rc_27` overturns it later. No system field carries the disagreement.

## 1b Active speakers

Status comes from `activity.json` (build per-universe-v1, clock 2025-10-01T07:00:00Z). Voice follows `conventions.json`: Slack DM median 39 characters and private-channel median 51, lower-case starts common, about 15–20 % end in punctuation. Julia and Brian write Turkish together in `D076RBM29JS`.

| Person | Email | status_at_clock | Seeding role | In `C0880U9751A` | Live in `C090N54TG79` |
|---|---|---|---|---|---|
| Leonard Hayes | leonard.hayes@harmonygames.co | active_sep_2025_quiet_in_oct | Author of the ask, note-thread replies, panel definition, stability Doc, Trello card; not an observer | Yes | Yes |
| Robert | robert@harmonygames.co | active_sep_2025_quiet_in_oct | K5 reply and F reply; retention reply; observer of K5's 10 | Yes | Yes |
| Arthur Blake | arthur.blake@harmonygames.co | active_sep_2025_quiet_in_oct | K3 inline note on his own PR; observer, 1 clean session | Yes | No, left Sep 11 |
| Brian Foster | brian.foster@harmonygames.co | active_sep_2025_quiet_in_oct | K4 line and form Doc; observer of K4's 9; never in Gmail (SC-6) | Yes | Yes |
| Vincent Parker | vincent.parker@harmonygames.co | active_sep_2025_quiet_in_oct | Owner of `ZOM-567` and its dated line; observer, 3 clean | Yes | Yes |
| Julia Lawson | julia.lawson@harmonygames.co | active_sep_2025_quiet_in_oct | Persona: question on the note, relay, log note, ticket batch; not an observer | Yes | Yes |
| Claire Morgan | claire.morgan@harmonygames.co | active_sep_2025_quiet_in_oct | K1 host and author; observer of K1's 13; no other session that day | Yes | No, never a member |
| Marcus Bennett | marcus.bennett@harmonygames.co | active_sep_2025_quiet_in_oct | Observer, 3 clean | Yes | No, left Sep 11 |
| Oliver Brooks | oliver.brooks@harmonygames.co | active_sep_2025_quiet_in_oct | Observer, 3 Samsung and 2 clean | Yes | No, never a member |
| Owen Baker | owen.baker@harmonygames.co | active_sep_2025_quiet_in_oct | Observer, 3 Samsung and 2 clean | Yes | No, never a member |
| Samuel Turner | samuel.turner@harmonygames.co | active_sep_2025_quiet_in_oct | Observer, 3 Samsung and 2 clean | Yes | No, never a member |
| Calvin Price | calvin.price@harmonygames.co | active_sep_2025_quiet_in_oct | Observer, 2 Samsung and 1 clean | Yes | No, never a member |
| Martin Walsh | martin.walsh@harmonygames.co | active_sep_2025_quiet_in_oct | Observer, 2 clean, session date Sep 29 only | Yes | No, never a member |
| Douglas | douglas@harmonygames.co | active_sep_2025_quiet_in_oct | Observer, 1 clean; thin in the window (4 messages) | Yes | No, never a member |

Twelve observers: Claire 13, Robert 10, Brian 9, then Oliver 5, Owen 5, Samuel 5, Calvin 3, Vincent 3, Marcus 3, Martin 2, Arthur 1, Douglas 1, which is 60 (K1 13 + K5 10 + K4 9 + K3 11 + clean 17). Frederick Stone stays out because he is thin and adds nothing. Leonard stays out so his S23 Ultra friend cannot enter the cohort.

Finding: `C090N54TG79` has five live humans (membership list minus the Sep 11 leavers), and Leonard said "please don’t add people to this channel" at `C090N54TG79/1757612648.292579`. The note also sits in `#executives`, which adds Arthur. Eight of the twelve observers therefore never received it in base. All twelve are in `C0880U9751A`, so one seeded relay from Julia there is required (section "Scenario open items resolved", row R0).

## 1c Identity traps

```text

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

```text
ENTITY email:julia.lawson@harmonygames.co  name=Julia Lawson  kind=person  emails=['julia.lawson@harmonygames.co']
  persona: julia_lawson - Product Manager / Product
  slack      id=EMPLOYEE_0005_SLACK_ID, name=Julia Lawson, real_name=Julia Lawson, email=julia.lawson@harmonygames.co, is_bot=False, deleted=False, messages=31848, first_post=2023-07-16, last_post=2025-09-30   [join: exact_email]
  gmail      mailbox=julia.lawson@harmonygames.co, threads=253, messages=304, first=2023-07-16, last=2025-09-17, thread_filename_alias=['jlawson@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=julia.lawson@harmonygames.co, owner_email=julia.lawson@harmonygames.co, summary=Julia Lawson — primary, events=748, last_event_before_clock=2025-09-29   [join: exact_email]
  gdrive     id=user_8140f09bf9f1, email=julia.lawson@harmonygames.co, display_name=julia.lawson@harmonygames.co, root_folders=['d_8140f09bf9f1b94cb8ee2d'], owned_items=28, last_modified=2025-09-11, files_shared_with=158   [join: exact_email]
  linear     id=usr_8140f09bf9f1b94c, email=julia.lawson@harmonygames.co, name=julia.lawson@harmonygames.co, is_active=True, last_activity=2025-09-23   [join: exact_email]
  github     login=PERSON_0005_GITHUB_USERNAME, name=Julia Lawson, email=julia.lawson@harmonygames.co, type=User, last_activity=2025-09-29   [join: exact_email]
  trello     id=793af7ca6940bf18eb516c75, username=julia.lawson, fullName=Julia Lawson   [join: exact_name]
  confluence id=user_EMPLOYEE_0005, account_id=acct_EMPLOYEE_0005, email=julia.lawson@harmonygames.co, display_name=Julia Lawson, is_active=True, last_activity=2025-09-21   [join: exact_email]
  contacts   contact_id=8140f09bf9f1b94cb8ee2dd7, name=Julia Lawson, email=julia.lawson@harmonygames.co, job=Product Manager, is_user=False   [join: exact_email]
  last activity: {'slack': '2025-09-30', 'gmail': '2025-09-17', 'gcal': '2025-09-29', 'gdrive': '2025-09-11', 'linear': '2025-09-23', 'github': '2025-09-29', 'confluence': '2025-09-21'}

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

ENTITY email:brian.foster@harmonygames.co  name=Brian Foster  kind=person  emails=['brian.foster@harmonygames.co']
  persona: brian_foster - Game Engineer / Engineering
  slack      id=EMPLOYEE_0026_SLACK_ID, name=Brian Foster, real_name=Brian Foster, email=brian.foster@harmonygames.co, is_bot=False, deleted=False, messages=28951, first_post=2024-06-06, last_post=2025-09-30   [join: exact_email]
  gmail      mailbox=brian.foster@harmonygames.co, threads=297, messages=307, first=2024-06-05, last=2025-09-30, thread_filename_alias=['brian@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=brian.foster@harmonygames.co, owner_email=brian.foster@harmonygames.co, summary=Brian Foster — primary, events=417, last_event_before_clock=2025-09-29   [join: exact_email]
  gdrive     id=user_fc22d5941b2a, email=brian.foster@harmonygames.co, display_name=brian.foster@harmonygames.co, root_folders=['d_fc22d5941b2aeb5c03ad32'], owned_items=101, last_modified=2025-09-17, files_shared_with=127   [join: exact_email]
  linear     id=usr_fc22d5941b2aeb5c, email=brian.foster@harmonygames.co, name=brian.foster@harmonygames.co, is_active=True, last_activity=2025-09-30   [join: exact_email]
  github     login=PERSON_0180_GITHUB_USERNAME, name=Brian Foster, email=brian.foster@harmonygames.co, type=User, last_activity=2025-09-29   [join: exact_email]
  trello     id=d1cd0fef645a6c978ae1f068, username=brian.foster, fullName=Brian Foster   [join: exact_name]
  confluence id=user_EMPLOYEE_0026, account_id=acct_EMPLOYEE_0026, email=brian.foster@harmonygames.co, display_name=Brian Foster, is_active=True   [join: exact_email]
  contacts   contact_id=fc22d5941b2aeb5c03ad32fa, name=Brian Foster, email=brian.foster@harmonygames.co, job=Game Engineer, is_user=False   [join: exact_email]
  last activity: {'slack': '2025-09-30', 'gmail': '2025-09-30', 'gcal': '2025-09-29', 'gdrive': '2025-09-17', 'linear': '2025-09-30', 'github': '2025-09-29'}

ENTITY email:vincent.parker@harmonygames.co  name=Vincent Parker  kind=person  emails=['vincent.parker@harmonygames.co']
  persona: vincent_parker - Game Systems Engineer / Engineering
  slack      id=EMPLOYEE_0012_SLACK_ID, name=Vincent Parker, real_name=Vincent Parker, email=vincent.parker@harmonygames.co, is_bot=False, deleted=False, messages=39854, first_post=2023-08-30, last_post=2025-09-30   [join: exact_email]
  gmail      mailbox=vincent.parker@harmonygames.co, threads=1258, messages=1367, first=2023-08-30, last=2025-09-30, thread_filename_alias=['vincent@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=vincent.parker@harmonygames.co, owner_email=vincent.parker@harmonygames.co, summary=Vincent Parker — primary, events=446, last_event_before_clock=2025-09-29   [join: exact_email]
  gdrive     id=user_65c76e0b87aa, email=vincent.parker@harmonygames.co, display_name=vincent.parker@harmonygames.co, root_folders=['d_65c76e0b87aa7e9b84d1df'], owned_items=190, last_modified=2025-09-29, files_shared_with=141   [join: exact_email]
  linear     id=usr_65c76e0b87aa7e9b, email=vincent.parker@harmonygames.co, name=vincent.parker@harmonygames.co, is_active=True, last_activity=2025-09-30   [join: exact_email]
  github     login=EMPLOYEE_0012_GITHUB_USERNAME, name=Vincent Parker, email=vincent.parker@harmonygames.co, type=User, last_activity=2025-09-16   [join: exact_email]
  trello     id=864e381ee6c844b2a3a7eaf8, username=vincent.parker, fullName=Vincent Parker   [join: exact_name]
  confluence id=user_EMPLOYEE_0012, account_id=acct_EMPLOYEE_0012, email=vincent.parker@harmonygames.co, display_name=Vincent Parker, is_active=True, last_activity=2025-07-26   [join: exact_email]
  contacts   contact_id=65c76e0b87aa7e9b84d1df22, name=Vincent Parker, email=vincent.parker@harmonygames.co, job=Game Systems Engineer, is_user=False   [join: exact_email]
  last activity: {'slack': '2025-09-30', 'gmail': '2025-09-30', 'gcal': '2025-09-29', 'gdrive': '2025-09-29', 'linear': '2025-09-30', 'github': '2025-09-16', 'confluence': '2025-07-26'}

ENTITY email:oliver.brooks@harmonygames.co  name=Oliver Brooks  kind=person  emails=['oliver.brooks@harmonygames.co']
  persona: oliver_brooks - Senior Game Engineer / Engineering
  slack      id=EMPLOYEE_0003_SLACK_ID, name=Oliver Brooks, real_name=Oliver Brooks, email=oliver.brooks@harmonygames.co, is_bot=False, deleted=False, messages=13475, first_post=2024-08-12, last_post=2025-09-30   [join: exact_email]
  gmail      mailbox=oliver.brooks@harmonygames.co, threads=1466, messages=1971, first=2024-08-08, last=2025-09-30, thread_filename_alias=['oliver@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=oliver.brooks@harmonygames.co, owner_email=oliver.brooks@harmonygames.co, summary=Oliver Brooks — primary, events=265, last_event_before_clock=2025-09-29   [join: exact_email]
  gdrive     id=user_bdf01b53c6a9, email=oliver.brooks@harmonygames.co, display_name=oliver.brooks@harmonygames.co, root_folders=['d_bdf01b53c6a92c5e167c65'], owned_items=8, last_modified=2025-09-01, files_shared_with=108   [join: exact_email]
  linear     id=usr_bdf01b53c6a92c5e, email=oliver.brooks@harmonygames.co, name=oliver.brooks@harmonygames.co, is_active=True, last_activity=2025-09-30   [join: exact_email]
  github     login=EMPLOYEE_0003_GITHUB_USERNAME, name=Oliver Brooks, email=oliver.brooks@harmonygames.co, type=User, last_activity=2025-09-30   [join: exact_email]
  trello     id=12c4a9dcd2d37a25a8d3b557, username=oliver.brooks, fullName=Oliver Brooks   [join: exact_name]
  confluence id=user_EMPLOYEE_0003, account_id=acct_EMPLOYEE_0003, email=oliver.brooks@harmonygames.co, display_name=Oliver Brooks, is_active=True, last_activity=2025-09-29   [join: exact_email]
  contacts   contact_id=bdf01b53c6a92c5e167c658c, name=Oliver Brooks, email=oliver.brooks@harmonygames.co, job=Senior Game Engineer, is_user=False   [join: exact_email]
  last activity: {'slack': '2025-09-30', 'gmail': '2025-09-30', 'gcal': '2025-09-29', 'gdrive': '2025-09-01', 'linear': '2025-09-30', 'github': '2025-09-30', 'confluence': '2025-09-29'}

ENTITY email:claire.morgan@harmonygames.co  name=Claire Morgan  kind=person  emails=['claire.morgan@harmonygames.co']
  persona: claire_morgan - Art Lead / Design
  slack      id=EMPLOYEE_0009_SLACK_ID, name=Claire Morgan, real_name=Claire Morgan, email=claire.morgan@harmonygames.co, is_bot=False, deleted=False, messages=9824, first_post=2023-03-22, last_post=2025-09-30   [join: exact_email]
  gmail      mailbox=claire.morgan@harmonygames.co, threads=846, messages=923, first=2023-03-30, last=2025-09-30, thread_filename_alias=['claire@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=claire.morgan@harmonygames.co, owner_email=claire.morgan@harmonygames.co, summary=Claire Morgan — primary, events=553, last_event_before_clock=2025-09-29   [join: exact_email]
  gdrive     id=user_7fe31e7ec819, email=claire.morgan@harmonygames.co, display_name=claire.morgan@harmonygames.co, root_folders=['d_7fe31e7ec81996189e1f14'], owned_items=69, last_modified=2024-07-08, files_shared_with=115   [join: exact_email]
  linear     id=usr_7fe31e7ec8199618, email=claire.morgan@harmonygames.co, name=claire.morgan@harmonygames.co, is_active=True, last_activity=2025-09-03   [join: exact_email]
  github     login=EMPLOYEE_0009_GITHUB_USERNAME, name=Claire Morgan, email=claire.morgan@harmonygames.co, type=User, last_activity=2025-09-25   [join: exact_email]
  trello     id=4bc5d398e54226f344ad3abc, username=claire.morgan, fullName=Claire Morgan   [join: exact_name]
  confluence id=user_EMPLOYEE_0009, account_id=acct_EMPLOYEE_0009, email=claire.morgan@harmonygames.co, display_name=Claire Morgan, is_active=True   [join: exact_email]
  contacts   contact_id=7fe31e7ec81996189e1f14d6, name=Claire Morgan, email=claire.morgan@harmonygames.co, job=Art Lead, is_user=False   [join: exact_email]
  last activity: {'slack': '2025-09-30', 'gmail': '2025-09-30', 'gcal': '2025-09-29', 'gdrive': '2024-07-08', 'linear': '2025-09-03', 'github': '2025-09-25'}
  UNRESOLVED (ambiguous_name): mononym 'Claire' is an exact name of [] and the first name of ['email:claire.morgan@harmonygames.co']

ENTITY email:marcus.bennett@harmonygames.co  name=Marcus Bennett  kind=person  emails=['marcus.bennett@harmonygames.co']
  persona: marcus_bennett - Artist / Design
  slack      id=EMPLOYEE_0002_SLACK_ID, name=Marcus Bennett, real_name=Marcus Bennett, email=marcus.bennett@harmonygames.co, is_bot=False, deleted=False, messages=25786, first_post=2023-09-28, last_post=2025-09-30   [join: exact_email]
  gmail      mailbox=marcus.bennett@harmonygames.co, threads=4219, messages=4245, first=2023-09-28, last=2025-09-29, thread_filename_alias=['marcus.bennett@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=marcus.bennett@harmonygames.co, owner_email=marcus.bennett@harmonygames.co, summary=Marcus Bennett — primary, events=604, last_event_before_clock=2025-09-29   [join: exact_email]
  gdrive     id=user_c77c50cc15c5, email=marcus.bennett@harmonygames.co, display_name=marcus.bennett@harmonygames.co, root_folders=['d_c77c50cc15c5342d638ebb'], owned_items=47335, last_modified=2025-09-10, files_shared_with=132   [join: exact_email]
  linear     id=usr_c77c50cc15c5342d, email=marcus.bennett@harmonygames.co, name=marcus.bennett@harmonygames.co, is_active=True, last_activity=2025-09-25   [join: exact_email]
  github     login=PERSON_0396_GITHUB_USERNAME, name=Marcus Bennett, email=marcus.bennett@harmonygames.co, type=User, last_activity=2025-09-30   [join: exact_email]
  trello     id=7a20445f698bc5871ffd17f5, username=marcus.bennett, fullName=Marcus Bennett   [join: exact_name]
  confluence id=user_EMPLOYEE_0002, account_id=acct_EMPLOYEE_0002, email=marcus.bennett@harmonygames.co, display_name=Marcus Bennett, is_active=True   [join: exact_email]
  contacts   contact_id=c77c50cc15c5342d638ebb21, name=Marcus Bennett, email=marcus.bennett@harmonygames.co, job=Artist (VFX & Animation), is_user=False   [join: exact_email]
  last activity: {'slack': '2025-09-30', 'gmail': '2025-09-29', 'gcal': '2025-09-29', 'gdrive': '2025-09-10', 'linear': '2025-09-25', 'github': '2025-09-30'}
  UNRESOLVED (ambiguous_name): mononym 'Marcus' is an exact name of [] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']

ENTITY email:martin.walsh@harmonygames.co  name=Martin Walsh  kind=person  emails=['martin.walsh@harmonygames.co']
  persona: martin_walsh - Game Designer / Design
  slack      id=EMPLOYEE_0033_SLACK_ID, name=Martin Walsh, real_name=Martin Walsh, email=martin.walsh@harmonygames.co, is_bot=False, deleted=False, messages=7527, first_post=2023-08-28, last_post=2025-09-30   [join: exact_email]
  gmail      mailbox=martin.walsh@harmonygames.co, threads=4356, messages=4618, first=2023-08-27, last=2025-10-01, thread_filename_alias=['martin.walsh@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=martin.walsh@harmonygames.co, owner_email=martin.walsh@harmonygames.co, summary=Martin Walsh — primary, events=581, last_event_before_clock=2025-09-29   [join: exact_email]
  gdrive     id=user_51f5f16d46e8, email=martin.walsh@harmonygames.co, display_name=martin.walsh@harmonygames.co, root_folders=['d_51f5f16d46e8cf55f5ee33'], owned_items=30, last_modified=2024-02-16, files_shared_with=136   [join: exact_email]
  linear     id=usr_51f5f16d46e8cf55, email=martin.walsh@harmonygames.co, name=martin.walsh@harmonygames.co, is_active=True, last_activity=2025-09-30   [join: exact_email]
  trello     id=ba9cc333cefad99228d6757d, username=martin.walsh, fullName=Martin Walsh   [join: exact_name]
  confluence id=user_EMPLOYEE_0033, account_id=acct_EMPLOYEE_0033, email=martin.walsh@harmonygames.co, display_name=Martin Walsh, is_active=True   [join: exact_email]
  contacts   contact_id=51f5f16d46e8cf55f5ee337b, name=Martin Walsh, email=martin.walsh@harmonygames.co, job=Game Designer, is_user=False   [join: exact_email]
  absent from: github
  last activity: {'slack': '2025-09-30', 'gmail': '2025-10-01', 'gcal': '2025-09-29', 'gdrive': '2024-02-16', 'linear': '2025-09-30'}

ENTITY email:owen.baker@harmonygames.co  name=Owen Baker  kind=person  emails=['owen.baker@harmonygames.co']
  persona: owen_baker - Game Engineer (Unity) / Engineering
  slack      id=EMPLOYEE_0021_SLACK_ID, name=Owen Baker, real_name=Owen Baker, email=owen.baker@harmonygames.co, is_bot=False, deleted=False, messages=14941, first_post=2023-09-15, last_post=2025-10-01   [join: exact_email]
  gmail      mailbox=owen.baker@harmonygames.co, threads=1408, messages=1444, first=2023-09-14, last=2025-09-29, thread_filename_alias=['owen@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=owen.baker@harmonygames.co, owner_email=owen.baker@harmonygames.co, summary=Owen Baker — primary, events=469, last_event_before_clock=2025-09-29   [join: exact_email]
  gdrive     id=user_4e13bd40cc73, email=owen.baker@harmonygames.co, display_name=owen.baker@harmonygames.co, root_folders=['d_4e13bd40cc73d0fc76f87c'], owned_items=10, last_modified=2025-08-25, files_shared_with=127   [join: exact_email]
  linear     id=usr_4e13bd40cc73d0fc, email=owen.baker@harmonygames.co, name=owen.baker@harmonygames.co, is_active=True, last_activity=2025-09-30   [join: exact_email]
  github     login=PERSON_5877_GITHUB_USERNAME, name=Owen Baker, email=owen.baker@harmonygames.co, type=User, last_activity=2025-09-30   [join: exact_email]
  trello     id=919ee44a0d5157b7839f66a8, username=owen.baker, fullName=Owen Baker   [join: exact_name]
  confluence id=user_EMPLOYEE_0021, account_id=acct_EMPLOYEE_0021, email=owen.baker@harmonygames.co, display_name=Owen Baker, is_active=True   [join: exact_email]
  contacts   contact_id=4e13bd40cc73d0fc76f87c7d, name=Owen Baker, email=owen.baker@harmonygames.co, job=Game Engineer (Unity), is_user=False   [join: exact_email]
  last activity: {'slack': '2025-10-01', 'gmail': '2025-09-29', 'gcal': '2025-09-29', 'gdrive': '2025-08-25', 'linear': '2025-09-30', 'github': '2025-09-30'}

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

ENTITY email:douglas@harmonygames.co  name=Douglas  kind=person  emails=['douglas@harmonygames.co']
  persona: douglas - Software Engineer / Engineering
  slack      id=EMPLOYEE_0031_SLACK_ID, name=Douglas, real_name=Douglas, email=douglas@harmonygames.co, is_bot=False, deleted=False, messages=13832, first_post=2023-09-01, last_post=2025-09-30   [join: exact_email]
  gmail      mailbox=douglas@harmonygames.co, threads=4342, messages=4505, first=2023-08-29, last=2025-10-01, thread_filename_alias=['douglas@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=douglas@harmonygames.co, owner_email=douglas@harmonygames.co, summary=Douglas — primary, events=437, last_event_before_clock=2025-09-29   [join: exact_email]
  gdrive     id=user_cd7849ec043a, email=douglas@harmonygames.co, display_name=douglas@harmonygames.co, root_folders=['d_cd7849ec043ab3da107f8c'], owned_items=9, last_modified=2025-06-27, files_shared_with=129   [join: exact_email]
  linear     id=usr_cd7849ec043ab3da, email=douglas@harmonygames.co, name=douglas@harmonygames.co, is_active=True, last_activity=2025-09-30   [join: exact_email]
  github     login=PERSON_5760_GITHUB_USERNAME, name=Douglas, email=douglas@harmonygames.co, type=User, last_activity=2025-08-13   [join: exact_email]
  trello     id=1c0688ee1d9093f5b978c1db, username=douglas, fullName=Douglas   [join: exact_name]
  confluence id=user_EMPLOYEE_0031, account_id=acct_EMPLOYEE_0031, email=douglas@harmonygames.co, display_name=Douglas, is_active=True, last_activity=2025-09-29   [join: exact_email]
  contacts   contact_id=cd7849ec043ab3da107f8c03, name=Douglas, email=douglas@harmonygames.co, job=Software Engineer, is_user=False   [join: exact_email]
  last activity: {'slack': '2025-09-30', 'gmail': '2025-10-01', 'gcal': '2025-09-29', 'gdrive': '2025-06-27', 'linear': '2025-09-30', 'github': '2025-08-13', 'confluence': '2025-09-29'}

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

ENTITY email:simon.walker@harmonygames.co  name=Simon Walker  kind=person  emails=['simon.walker@harmonygames.co']
  persona: simon_walker - Data Analyst (Contractor) / Engineering
  slack      id=EMPLOYEE_0037_SLACK_ID, name=Simon Walker, real_name=Simon Walker, email=simon.walker@harmonygames.co, is_bot=False, deleted=False, messages=829, first_post=2023-12-05, last_post=2025-09-30   [join: exact_email]
  gmail      mailbox=simon.walker@harmonygames.co, threads=690, messages=701, first=2023-12-05, last=2025-09-30, thread_filename_alias=['simon@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=simon.walker@harmonygames.co, owner_email=simon.walker@harmonygames.co, summary=Simon Walker — primary, events=3, last_event_before_clock=2025-09-19   [join: exact_email]
  gdrive     share_recipient=simon.walker@harmonygames.co, files_shared_with=10   [join: exact_email]
  linear     id=usr_eac7fcafa75e4935, email=simon.walker@harmonygames.co, name=simon.walker@harmonygames.co, is_active=True   [join: exact_email]
  trello     id=60eb52a015fd4a1bf8837300, username=simon.walker, fullName=Simon Walker   [join: exact_name]
  confluence id=user_STAFF_2, account_id=acct_STAFF_2, email=simon.walker@harmonygames.co, display_name=Simon Walker, is_active=True   [join: exact_email]
  contacts   contact_id=a126ad1d54296023b4480445, name=Simon Walker, email=simon.walker@harmonygames.co, job=Data Analyst (Contractor), is_user=False   [join: exact_email]
  absent from: github
  last activity: {'slack': '2025-09-30', 'gmail': '2025-09-30', 'gcal': '2025-09-19'}
```

| Name on a record | Correct entity | Lookalike | Pin |
|---|---|---|---|
| Marcus | Marcus Bennett, marcus.bennett@harmonygames.co, `usr_c77c50cc15c5342d` | Marcus Lee, quiet since 2025-06; Trello Marcus `c48a210d5c5a4b59231c6873` | Full name on every form and ticket |
| Martin | Martin Walsh, martin.walsh@harmonygames.co | Martin Lewis, a token person | Full name; no session Sep 23–25 |
| Claire | Claire Morgan, claire.morgan@harmonygames.co, mail files `claire@` | GitHub display "Claire" on `PERSON_2360_GITHUB_USERNAME` | Full name on the form; From line carries her address |
| Lawson | Julia Lawson | Peter Lawson, peter.lawson@harmonygames.co | Persona only |
| Oliver | Oliver Brooks, `usr_bdf01b53c6a92c5e` | Lauren Brooks shares the surname | Full name |
| Owen | Owen Baker, `usr_4e13bd40cc73d0fc` | Thomas Baker shares the surname | Full name |
| Calvin | Calvin Price, `PERSON_0003_GITHUB_USERNAME` | Second GitHub login `PERSON_2137_GITHUB_USERNAME`; Nathan Price shares the surname | No GitHub role here |
| Brian | Brian Foster at HG | Node's CEO mails from the same address (SC-6) | No Brian mail; form is a Doc he owns |
| Leonard, Robert | Contacts job differs from the roster role | Roster says Creative Director for both | Refer to neither by title in a seed |
| ZOM-n | `ZOM-567` onward | Unrelated ENG-n twins (N01) | Always write the ZOM prefix |

No second account, duplicate mailbox or malformed id is planned.

### Reach table (load-bearing records)

Base records only; seeds are checked at the injection gate. Each row below was run through `persona_view.py can-see julia_lawson`.

| Record | Service | Verdict | Mark | Why it is needed |
|---|---|---|---|---|
| `C090N54TG79/1758517286.431379` | slack | YES | LB | The note; rule hub and "No coaching" |
| `C090N54TG79/1758581651.167799` | slack | YES | LB | K5 root |
| `C090N54TG79/1758582083.678989` | slack | YES | LB | Support for the coached rule |
| `C090N54TG79/1758691397.679889` | slack | YES | LB | Panel definition root |
| `C090N54TG79/1758729342.721289` | slack | YES | LB | Panel audience |
| `C090N54TG79/1759171957.791499` | slack | YES | LB | The Sep 29 change |
| `C090N54TG79/1759172166.547199` | slack | YES | LB | "17 -> level 5" |
| `C090N54TG79/1759176983.189479` | slack | YES | LB | The lean |
| `C090N54TG79/1759178344.878219` | slack | YES | LB | Leonard agrees |
| `D076RBM29JS` | slack | YES | LB | K4 container |
| `D05GU6L0XFH/1758901945.292269` | slack | YES | LB | F root |
| `C05433XK267/1758803475.436309` | slack | YES | LB | Run #15 |
| `C0880U9751A` | slack | YES | LB | Relay home |
| `C08R27X0EAH/1758642623.835409` | slack | YES | Reserve | K5 reserve root |
| `D05GU6L0XFH/1758907345.403359` | slack | YES | Reserve | F second choice |
| `f_89fadbc54660c9881d8cf9` | gdocs | YES | Distractor | Older GDD |
| `d_8140f09bf9f1b94cb8ee2d` | gdrive | YES | LB | Julia's root folder |
| `evt_b371a24b8dad3a2cd9f432` | gcal | YES | Context | Own-calendar control |
| `C093LEZGF6J/1759258475.735779` | slack | UNVERIFIED | Probe | UNVERIFIED-OK: Julia is not a member of the public channel, the mirror only copies the comment. alternate_evidence_ids: harmonygames-Games/match3d#476, C05433XK267/1758803475.436309 |
| `D04UP2L3E3S/1758515667.845849` | slack | NO | Probe | DENIAL-INTENDED: Leonard and Robert DM, grounding for the age band only. alternate_evidence_ids: C090N54TG79/1758517286.431379 |
| `C07C2866011` | slack | NO | Probe | DENIAL-INTENDED: `#executives` copy of the note, unused. alternate_evidence_ids: C090N54TG79/1758517286.431379 |
| `leonard.hayes@harmonygames.co/1843922088670958384` | gmail | NO | Probe | DENIAL-INTENDED: vendor mail in Leonard's mailbox; the seeded forward carries it. alternate_evidence_ids: C090N54TG79/1758517286.431379 |

GitHub, Linear, Trello, Contacts, Snowflake and Confluence are unscoped, so `harmonygames-Games/match3d#476`, `ZOM-559` and `6851a6569f3bf818760632ab` need no can-see line. Arthur's note is the one deciding GitHub record, and it does not depend on the `#zombie-prs` copy.

```text
julia_lawson slack C090N54TG79/1758517286.431379: YES
julia_lawson slack C090N54TG79/1758581651.167799: YES
julia_lawson slack C090N54TG79/1758582083.678989: YES
julia_lawson slack C090N54TG79/1758691397.679889: YES
julia_lawson slack C090N54TG79/1758729342.721289: YES
julia_lawson slack C090N54TG79/1759171957.791499: YES
julia_lawson slack C090N54TG79/1759172166.547199: YES
julia_lawson slack C090N54TG79/1759176983.189479: YES
julia_lawson slack C090N54TG79/1759178344.878219: YES
julia_lawson slack D076RBM29JS: YES
julia_lawson slack D05GU6L0XFH/1758901945.292269: YES
julia_lawson slack C05433XK267/1758803475.436309: YES
julia_lawson slack C0880U9751A: YES
julia_lawson slack C08R27X0EAH/1758642623.835409: YES
julia_lawson slack D05GU6L0XFH/1758907345.403359: YES
julia_lawson gdocs f_89fadbc54660c9881d8cf9: YES
julia_lawson gdrive d_8140f09bf9f1b94cb8ee2d: YES
julia_lawson gcal evt_b371a24b8dad3a2cd9f432: YES
julia_lawson slack C093LEZGF6J/1759258475.735779: UNVERIFIED
julia_lawson slack D04UP2L3E3S/1758515667.845849: NO
julia_lawson slack C07C2866011: NO
julia_lawson gmail leonard.hayes@harmonygames.co/1843922088670958384: NO
julia_lawson slack D05HMBQUC8Z: YES
```

### Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| slack | INT-22 | Mail notices | None seeded; optional and never needed. Five roots get counter updates: `C090N54TG79/1758517286.431379`, `C090N54TG79/1758581651.167799`, `C090N54TG79/1758691397.679889`, `C090N54TG79/1759165414.829399`, `D05GU6L0XFH/1758901945.292269` |
| gmail | none | gmail: none, no integration has Gmail as its source | Forms and K1 are human mail. Sender's copy sits in the sender's mailbox and Julia's copy in hers, both identical (Q10). The forward keeps Leonard's vendor copy |
| gcal | INT-11 | Invitation mail | Not seeded: a seeded meeting needs no mail. One row per attendee calendar, Claire and Julia |
| gdrive | INT-13 | Drive app DMs | None seeded; DM-only and optional. Drive rows mirror each seeded Doc and Sheet with sharing |
| gdocs | none | gdocs: none in the KB; the Drive row with the same id is the companion | Each seeded Doc has its Drive row and `shared_with_emails` |
| gsheets | none | gsheets: none in the KB; the Drive row with the same id is the companion | Julia owns the workbook; Drive row seeded with it |
| contacts | none | contacts: none, no integration feeds this service | No job on tester contacts; if the volume plan keeps contacts they carry a name and email only |
| github | INT-01, INT-23 | `#zombie-prs` copy under `C093LEZGF6J/1759258475.735779` (row 637fc98bc66d41b104fe243006fdcf98); CodeRabbit rc_28 26–66 s later | Seeded with fallback "[harmonygames-Games/match3d] Comment on #476". rc 29 → 31 with rc_28 mirrored (C8); `latest_reply` bumped. `rev_3`, and `rev_4` for CodeRabbit, go in `integration_exceptions` citing #470 rev_3; no timeline `reviewed` row (T01). Comment time must fall before 22:33:40Z |
| github | INT-02, INT-12 | Push posts, notification mail | None: no push is seeded; mail is optional |
| linear | INT-03 | linear[bot] on PRs that name a key | None: no seeded PR and `ZOM-567` is named by no PR |
| linear | INT-04, INT-05 | Slack notices, digest mail | None: a seeded state change needs no notice. Done on `ZOM-567` gets no `#zombie-match3d` post, though ZOM-553's got one at `C0880U9751A/1759236043.004679`, because not every transition is posted |
| trello | INT-21 | No Trello bot exists | No Slack post. Card, `createCard` action and `dateLastActivity` agree (T06) |

## Scenario open items resolved

### (a) K1 host and dates

**Host: Claire Morgan** (claire.morgan@harmonygames.co, Art Lead, UTC+3, active). Why she fits:
- She is the only non-founder with a human-looking recent send (`sent_last` 2025-09-30, from `activity.json`). Oliver, Owen and Samuel have no sent mail at all. Marcus last sent in 2024-10, and Leonard removed him from `#zombie-design`.
- She is Julia's close friend, with Turkish DMs through Sep 24 (`D05HMBQUC8Z`, can-see YES). A friend writing about what happened at her place is natural.
- She is not Brian (SC-6), not Martin, and holds no other job in the design. Robert, Vincent and Arthur stay on their own blocks.
- A calendar scan of Sep 20 to Oct 2 shows no event on Sep 26 for anyone, and her last Slack post that day is 16:28Z (`C08R8CHB0QL/1758904103.894649`).

| Item | Date | Note |
|---|---|---|
| Gathering (all 13 sessions, one session date) | Fri Sep 26, evening TRT | One date, no other session by Claire that day |
| Claire's form | Sep 26, about 21:00Z | Weekday; states no coaching; transcribed to 13 tickets and the log |
| K1 mail | **Mon Sep 29**, about 10:00Z | Separate thread, after the form, before the Sep 30 batch, and before the Sep 29 debate starts at 18:52Z |

Sep 29 beats Sep 24: a Sep 24 mail would need a gathering within two days of the note, on a work night, while this date gives a Friday evening. No record falls on Sep 27–28, and all dates are weekdays, so `sql_lint` raises no weekend warning.

Subject proposal: `a small thing from Friday`. The host and day stay in the body, and no fact sits in the subject or first lines. English: Claire and Julia chat in Turkish, but mail is a work register and K4 already holds the Turkish carrier. The collision test must still cover this subject and body against the K1 avoid list.

### (b) Calendar and Trello roles

**Calendar: real but supporting.** One event on Fri Sep 26 at 17:00Z, organizer Claire, attendees Claire and Julia, Julia declined, plain summary such as `Friday at Claire's`, no description fact. It is a second Julia-visible record of host and day, so the join does not rest on one mail. It also explains why Julia cannot know first-hand what happened. Base has social precedent, though it is rare ("hangout in PDX", Aug 2024). It carries no deciding fact, GCal being a ○ carrier. Sep 2025 has 9 events on Julia's calendar, so this one is visible: treat its effect on K1 find odds as a small rise in the forecast.

**Trello: thin, and I would not claim more.** One card, idShort 80, in Backlog `68c451221ebabaf255a7d16b` on `6851a6569f3bf818760632ab`, created by Leonard (`PERSON_6094_TRELLO_USER_ID`) inside his real board session of Sep 30 16:40:13–17:09:07Z. It names the card-order change as waiting on the read. It is a status echo: no deciding fact, no write target (rejected carrier in brief §6), no date, and it stays off the BETA list (SC-13, SC-14). It adds a truthful tracker and one distractor, nothing more. Base offers no better role: no card on the board mentions playtest, feedback, audience, friends or testers. If `hardness_gate.py` does not need Trello, dropping the card loses nothing, and the brief's "10 injected" then becomes 9.

### (c) Leonard's ask and Julia's reply

**Container: a new root by Leonard in `C090N54TG79`, Sep 30 about 21:10Z. Julia replies in that thread.**
- Julia and Leonard are live members, and every party to the Sep 29 debate is there. Newest base message: Robert 19:35:33Z (`C090N54TG79/1759260933.283799`), so the root becomes the newest parent.
- Window check: after 20:13Z, after all 61 tickets, after Arthur's note if that lands near 20:10Z, before Oct 1 00:00Z.
- Leonard's base Slack on Sep 30 stops at 18:24Z in the channels read, so nothing contradicts a later post.
- Rejected: the Julia–Leonard DM `D05HB64NMQU` has no export file after 2025-08, so a Sep 30 post there would restart a quiet DM. Under `C090N54TG79/1759172119.133819`: that thread is about bots. Under the note: it would bury the ask in the rule thread.
- Brian's message also goes in `C090N54TG79` (C10). Thread or top level both reach him, so the rubric should accept either.

### (d) Rule record homes and dates

Slack replies under the note make it the hub, so rules enter through the note by name. None is in Confluence. Authors in `C090N54TG79` are live members only.

| Row | Record | Home | Date (about) | Author | Notes |
|---|---|---|---|---|---|
| R0 | Relay of the note's ask, no rule text | Slack top level in `C0880U9751A` | Sep 22 15:30Z | Julia | **Not in the brief; needed.** Reaches all twelve observers |
| R1 | "25–45" is an age band | Slack replies under `C090N54TG79/1758517286.431379`: Julia's question, Leonard's answer | Sep 22 15:00 and 15:20Z | Julia, Leonard | Root gets `thread_ts`, reply_count 4 after R3, users 2 |
| R2 | Stability rule and store-builds clause: "a clean pass covering that device", ZOM-559 is no session blocker, limits sit in review on the PR it tested, tool owner Arthur | New Google Doc owned by Leonard, shared with Julia, Robert, Brian, Vincent | Sep 23 18:30Z | Leonard | Pointer by title in R2b |
| R2b | Pointer to the Doc | Slack reply under the note | Sep 23 18:40Z | Leonard | Dated after the Doc |
| R3 | Audience rule: no game-industry people, lead is the higher mean star rating over counted sessions, one label each, at least 6 per audience, gap under 0.25 is no clear lead, sessions decide | Slack reply under the note | Sep 24 17:00Z | Leonard | After Robert's "Audience can vary results" at `C090N54TG79/1758691528.127789` |
| R4 | Panel definition: stars per player, void treatment | Slack reply under `C090N54TG79/1758691397.679889` | Sep 24 16:05Z | Leonard | rc 2 → 3, users stays 2, after 15:55Z |
| R5 | Retention rule: install-weighted, mature cohorts | Slack reply under `C090N54TG79/1759165414.829399` | Sep 29 17:30Z | Robert | Vincent's retention post; root rc 0 → 1 |
| R6 | Julia's log note: counted → Done, not counted → Canceled, each ticket transcribes a dated form with session date | New Doc owned by Julia in `d_8140f09bf9f1b94cb8ee2d` | Sep 30 16:35Z | Julia | After 16:26:02Z |
| R7 | Leonard's ask | Slack root in `C090N54TG79` | Sep 30 21:10Z | Leonard | Section (c); states the C14 mapping |

Sequence on Sep 30: `ZOM-567` created about 16:30Z, Vincent's line about 16:50Z, Done about 17:10Z, session tickets to about 19:45Z, Arthur's note about 20:10Z, ask about 21:10Z.

Counter updates beyond the brief: F's root goes rc 1 → 2 **and reply_users_count 1 → 2**, because Julia is the only base replier on `D05GU6L0XFH/1758901945.292269` and Robert would be new. K5's root stays at users 2.
