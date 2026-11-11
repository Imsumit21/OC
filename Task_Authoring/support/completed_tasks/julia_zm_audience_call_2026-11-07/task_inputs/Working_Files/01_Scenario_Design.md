# Scenario Design — julia_zm_audience_read · design only · contains no prompt, OE or criterion text

Design of record: `00_Rev5_Design_Brief.md`, its Resolutions section first. Sections 0, 1, 1a, 1b, 1c, the Reach table and Integrations are copied from `01_Grounding_Sections.md`, changed only where the audience-labelling rule moved to deck `f_a087f049d271e9aa9f567f`, where a row was missing for a service added since, and where `01b_Design_Review_Final.md` required a repair. Older working files (`00_Rev5_Design_Brief.md`, `01_Manifest_Notes.md`) still show pre-repair values; this document, the draft manifest and the surface win. Times are UTC. "Seed" means a planned record. Planned record text in the delegation table is seed text the SQL must carry, not prompt text.

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
| Slides | ZM audience read criteria (seed, owned by Julia) | `f_a087f049d271e9aa9f567f` | Audience labels, metric, tie band, minimum |
| Confluence | QA runbook | `page_qa_runbook` | Read context, not injected |

**K5 build id (confirmed in section 2).** `Match3D Android - #1943 - main`, Success at `C05433XK267/1758575557.575349` (Sep 22 21:12Z). The post says neither "dev" nor "store". It only shows a non-Submission job, so the Route Hunt row 3 bypass stays open as a second fair path. K5's find rate in section 5 allows for it.

**Coupling seams.**
- A rule in Docs changes a value read in Linear: the stability clause decides whether 11 Samsung tickets count, and the ticket that seems to clear them is answered only on GitHub (`harmonygames-Games/match3d#476`).
- A rule in Slack changes a Sheet row and a Linear state: the game-industry exclusion (row R3 under `C090N54TG79/1758517286.431379`) and Brian's DM line (`D076RBM29JS`) flip 9 rows that tie out on form, ticket and log.
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
| Session labels | Semantic | "casual", "RPG" as session labels | `C090N54TG79/1758517286.431379` | S03 | Folded in: one label per session, set by the audience read criteria deck `f_a087f049d271e9aa9f567f` |
| "25–45" in the note | Semantic | Age band or headcount | `C090N54TG79/1758517286.431379` | none in KB | Designed reply settles it as age (base meaning at `D04UP2L3E3S/1758515667.845849`, not Julia-visible) |
| "Marcus" as a name on forms | Semantic | Marcus Bennett, Marcus Lee, Trello Marcus | `usr_c77c50cc15c5342d` | S04 | Avoid: full name on each form |
| Seeded pointer from a channel post to Doc | Cross-service referential | Slack doc links use native ids, never `f_` ids | `C090N54TG79/1758517286.431379` | R04 | Point by title, with no constructed URL |
| Arthur's note and its mirror | Cross-service referential | Comment and Slack copy | `C093LEZGF6J/1759258475.735779` | R06, R07 | Mirror text matches the comment; base mirrored #476 CodeRabbit rows, so the mirror is planned |
| GitHub notification mail for #476 | Cross-service referential | Redacted subject | `harmonygames-Games/match3d#476` | R03 | Not seeded (INT-12 optional) |
| Calendar event and invite mail | Cross-service referential | Mail with no GCal row | `evt_f08d0e87c8c7aafe580d42` | R08 | Event seeded with no invite mail |
| Slack keys that do not exist | Cross-service referential | ZOM keys in seeds | `ZOM-566` | R01 | Seeds cite only ZOM-559 and seeded ZOM-567 to ZOM-627 |
| Thread counters on seeded roots | Quantitative | `reply_count`, `reply_users_count`, `latest_reply` | `C090N54TG79/1758581651.167799` | Q01, Q02, Q03 | All four touched roots checked clean against their replies; bump all three per section 11 |
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
| Leonard Hayes | leonard.hayes@harmonygames.co | active_sep_2025_quiet_in_oct | Author of the ask, note-thread replies, K5 reply, panel definition, stability Doc, Trello card; not an observer | Yes | Yes |
| Robert | robert@harmonygames.co | active_sep_2025_quiet_in_oct | F reply; retention reply; observer of K5's 10 | Yes | Yes |
| Arthur Blake | arthur.blake@harmonygames.co | active_sep_2025_quiet_in_oct | K3 inline note on his own PR; observer, 1 clean session | Yes | No, left Sep 11 |
| Brian Foster | brian.foster@harmonygames.co | active_sep_2025_quiet_in_oct | K4 line and form Doc; observer of K4's 9; never in Gmail (SC-6) | Yes | Yes |
| Vincent Parker | vincent.parker@harmonygames.co | active_sep_2025_quiet_in_oct | Owner of `ZOM-567` and its dated line; observer, 3 clean | Yes | Yes |
| Julia Lawson | julia.lawson@harmonygames.co | active_sep_2025_quiet_in_oct | Persona: question on the note, relay, log note, ticket batch, audience read criteria deck; not an observer | Yes | Yes |
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

## 2 Cohort spine

**Rule.** One row per friend session in Julia's workbook log (`f_43bc35baf77fd59f4e57b8`), keyed by session ticket `ZOM-568` to `ZOM-627`: the sessions the note (`C090N54TG79/1758517286.431379`) asked for, logged on Sep 30. Size 60, 12 observers, one audience label each. `cohorts.json` has no fit (section 1). `ZOM-567` and the re-sent form (`julia.lawson@harmonygames.co/<CA8db5b364a9d7d3c1946e722aed490d591476@mail.gmail.com>`) sit outside the 60 and outside the tie-out.

**Truth (provisional design ratings, recomputed from `planned_records.sessions` after the seven-rating repair).** Casual n 9, mean 3.833. RPG n 8, mean 3.375. Casual leads by 0.458, past the 0.25 tie band, and both audiences clear the minimum of 6. All 60 kept: overall 3.592, casual 2.833 (n 30), RPG 4.350 (n 30). All 15 miss combinations give RPG past the band; single misses K5 0.270, K4 0.284, K1 0.333, K3 0.350; largest 1.517. Recomputed here from the session rows, and it matches `00_PreScenario_Audience_Table.txt`. The panel takes no part in this (Resolution C2). Ratings overlap now: `ZOM-588`, `ZOM-594`, `ZOM-579`, `ZOM-584` sit at 3 to 3.5 and `ZOM-608`, `ZOM-614`, `ZOM-570` at 4, so stars alone no longer sort counted from not counted (review M3). The wrong-gap slack is thin, so re-run the proof after any rating change.

| Group | Sessions | Audience and mean | Verdict | Requirement | Tickets | Observers |
|---|---|---|---|---|---|---|
| CLEAN | 17 | rpg 8 at 3.375, casual 9 at 3.833 | Counted | none | ZOM-598, ZOM-599, ZOM-600, ZOM-601, ZOM-602, ZOM-603, ZOM-604, ZOM-605, ZOM-606, ZOM-620, ZOM-621, ZOM-622, ZOM-623, ZOM-624, ZOM-625, ZOM-626, ZOM-627 | Marcus Bennett 3, Vincent Parker 3, Oliver Brooks 2, Owen Baker 2, Samuel Turner 2, Martin Walsh 2, Calvin Price 1, Arthur Blake 1, Douglas 1 |
| K1 | 13 | rpg 13 at 4.654 | Not counted: coached | R1 | ZOM-607 to ZOM-619 | Claire Morgan 13 |
| K3 | 11 | casual 11 at 2.364 | Not counted: device not cleared | R2 | ZOM-587 to ZOM-597 | Oliver Brooks 3, Owen Baker 3, Samuel Turner 3, Calvin Price 2 |
| K4 | 9 | rpg 9 at 4.778 | Not counted: game industry | R4 | ZOM-568 to ZOM-576 | Brian Foster 9 |
| K5 | 10 | casual 10 at 2.450 | Not counted: non-store build | R3 | ZOM-577 to ZOM-586 | Robert 10 |

**Surfaces and shortcut audit.** Each surface names a declared requirement and the column it decides (`surface_requirements`).

| Service | Tool | Calls | Requirement · decides | Why no bulk call covers it | Short-circuit and sweep answer | Records |
|---|---|---|---|---|---|---|
| gdocs | `gdocs_get_document` | 1 x 60 = 60 | R3 · session verdict | gdocs_search_documents and gdrive_search return titles and metadata; only gdocs_get_document returns the body with the build id, age and relation line | the build id sits only here and decides R3 for an unpredictable 10 of 60; a fullText search needs the id first, and which id matters is known only after the K5 reply, so a careful run reads the Docs before it can filter | `f_524278b67bfa30dde78699` and the rest of its set |
| linear | `linear_list_comments` | 1 x 60 = 60 | R2 · session verdict | linear_list_issues and linear_get_issue return no comments and the catalog has no bulk comment listing; device model is only in the comment | device model decides R2 for 11 of 60, written as marketing names and model numbers, so no text filter sweeps it; a run may skip this read on a session another rule already dropped, so the true need is 60 less those skips | `cmt_2fbcaf2d990d8b4e9c0d` and the rest of its set |
| gmail | `gmail_get_messages_batch` | 0.2 x 15 = 3 | R1 · session verdict | gmail_search_messages returns snippets; gmail_get_messages_batch returns bodies about 5 at a time, so 15 form mails cost about 3 calls, not 15 | host, day and the observer's coaching line sit only in the form mail, and R1 needs them for the join with the later mail | `julia.lawson@harmonygames.co/<CA01dc2d92371c7bfa63e451026f81fffed801@mail.gmail.com>` and the rest of its set |
| linear | `linear_update_issue` | 1 x 60 = 60 | R7 · ticket state | this surface is the state write, not a read: the catalog has no bulk issue update, so each ticket takes one linear_update_issue call | every session needs a final state, counted or not, so no verdict lets a run skip the write; declared here because the requester's confirmed per_record_floor of 160 counts the 60 state writes (Analysis section 10) | `ZOM-568` to `ZOM-627` (the write itself) |

Field map: log has date, observer, label, stars; ticket comment has device; notes Doc has build id, age and relation line; form mail has host, day and coaching line. Age is 25 to 45 on every session, so the "25–45" clause applies and excludes none (`planned_records.sessions`). Relation is a closed list: friend, family, neighbor, classmate, and one neutral group nickname, Kadıköy ekibi, on Brian's 9 Docs. No relation line implies work or a studio. Forms: 15 mails plus Brian's 9 Docs (`f_524278b67bfa30dde78699` and siblings), because Brian stays out of Gmail (SC-6). A form mail is a batch cover; the per-session form is the notes Doc.

**Disclosure on volume.** The per-record figure of 183 counts the 60 state writes as a surface (`linear_update_issue`, `ZOM-568` to `ZOM-627`). Evidence reads alone are 123 (60 ticket comments + 60 notes Docs + 3 mail batches). The requester accepted a per-record floor of 160 and a call-budget floor of 260 on 2026-11-07 (`volume_exception`, `00_Pre_Scenario_Analysis.md` section 12), on a table that counted those writes. A write is not evidence, so the 183 clears 160 only by that accepted counting; the reads alone would not. A correct run may also skip a comment read on a session another rule already dropped, so the true read need is below 60 on that surface.

**Classification predicate.** Closed vocabulary. Verdict: counted, not counted. Audience: casual, RPG, one per session (`f_a087f049d271e9aa9f567f`). Reason, for not counted: coached (R1), device not cleared (R2), non-store build (R3), game industry (R4). A session counts only if no exclusion applies. Groups are disjoint, so no session has two reasons and no two misses can cancel: K1 and K4 are RPG and high, K3 and K5 are casual and low.

**House rules that override the natural reading.** A Done ticket is not a clean pass covering that device, and a pass covers a device only if it ran on that device (`f_748d26e760e54651eaa0d8`). Samsung, listed by model family, is the one group on this gate; every other group needs no pass. A valid pass would clear the group's sessions whatever day they ran, and the Doc's rules apply to every session in the read whatever day it ran. The form's "no coaching" line loses to the host's later account. No clear lead means keep (Resolution C14), so a run must establish the casual lead to change the action.

**Dual regime.** No cohort-wide effective-date split is used. The one date rule is that the fact date governs, not the Sep 30 ticket date: each ticket transcribes a dated form (`f_c691d577b8f837eb4f9eaa`), which is what makes `julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>` later than the record it corrects (review B4).

**Boundary records.** `ZOM-567` (Done, not a session), the re-sent form, Leonard's S23 Ultra bug report (`C08R27X0EAH/1758420497.482989`, no ticket or log row), the 8 other sessions dated Sep 26 by other observers, of which `ZOM-605`, `ZOM-606` and `ZOM-620` are the K1 controls (same day, not the gathering).

**K5 build id, confirmed.** `Match3D Android - #1943 - main` at `C05433XK267/1758575557.575349` (re-read through `hg.py`: Success after 5 min 53 sec, Sep 22 21:12Z). All ids now share one shape, as base Crashlytics writes it: `0.3.38 (38)`, `0.3.40 (40)`, `0.3.127 (127)`, and K5's `0.3.127 (1943)`. Device and build agree: 0.3.38 and 0.3.40 are iOS, 0.3.127 is Android (`C0880U9751A/1758643365.607149`). The reply still names 1943. A search for 1943 still reaches the #builds post, which is a non-Submission job, so that second fair path stays open.

## 3 Hidden authorities

| Id | Name | Home | Decoy | Decoy scope | Governs | Findable query | Findability proof |
|---|---|---|---|---|---|---|---|
| H-GATE | ZM session stability gate | gdocs `f_748d26e760e54651eaa0d8` | gdocs `gdocs: data.json /docs_documents/346`, `page_qa_runbook` | team: QA team's release checks for store submissions against product team's friend-session device clearance | R2, R3 | "stability gate" | Base search for "stability gate" returns 0 in slack, gmail, gdocs, gdrive, gslides, gcal, linear, trello, confluence and github (section 12), so nothing competes. A search that returns the seed can only be proved once it exists: injection re-runs it. A top-level post after the note names the Doc by title (`C090N54TG79/1758728411.540327`). |
| H-AUD | ZM audience read criteria | gslides `f_a087f049d271e9aa9f567f` | gdocs `gdocs: data.json /docs_documents/328` | older version in trap version_records | R5 | "audience read criteria" | "audience read" has 0 base hits in gslides and gdrive, scans complete. The ask names it by what it governs, not by location. Proof that a search returns deck `f_a087f049d271e9aa9f567f` waits for the seed. |
| H-PANEL | the panel results forward | gmail `julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com>` | slack `C090N54TG79/1758517286.431379` | older version in trap version_records | R10 | "Playtest results for Puzzles vs. Zombies" | The subject has base hits only in Leonard's older mail (`leonard.hayes@harmonygames.co/1843922088670958384` and earlier threads); brief section 7 records 0 Playtestcloud mail visible to Julia, so her copy is the seed. Proof waits for the seed. |

`governs` lists do not overlap. H-GATE's decoys are the QA team's release checks, true for store submissions, not for friend sessions. H-AUD's decoy is the older GDD line (`f_89fadbc54660c9881d8cf9`, modified 2025-06-19), an older entry of T-AUD's `version_records`. Three authorities is the count: no slack on `hidden_authorities` beyond the minimum of 2 plus one. The KPI Sheet (`f_4e21b203a62910bdae0353`) is a superseded version in T-RET, not an authority decoy, because the retention rule is in Slack.

## 4 Delegation lattice

**Anchors.**

| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |
|---|---|---|
| A1 | Leonard's feedback note | `C090N54TG79/1758517286.431379` |
| A2 | Leonard's keep-or-hold message | `C090N54TG79/1759266627.418203` |
| A3 | audience sessions workbook | `f_43bc35baf77fd59f4e57b8` |

**Hub.** Leonard's ask, seeded root `C090N54TG79/1759266627.418203` (Sep 30 21:10:27Z), in the owner's voice. It delegates by role: "the rules I posted in the channel after my note", "the audience read criteria", "your log note", "Robert", "the panel results I forwarded you", "the roadmap card". It names no Doc link, channel or thread. The trap_liveness tool counts 10 direct delegations; those that reach T-F, T-PANEL, T-AUD and T-RET are breadcrumbs, accepted in section 5 and never removed.

**Fragments and incorporation.** 16 fragments, 8 services, 12 containers. Quotes are verbatim from the delegating record: the note's is base, read through `hg.py` at `C090N54TG79/1758517286.431379`; the others are planned seed text the SQL must carry exactly.

| Fragment | Service | Locator | Kind | Requirement | Chain to anchor | delegated_by_record | delegation_quote |
|---|---|---|---|---|---|---|---|
| F-COACH | slack | `C090N54TG79/1758517286.431379` | exclusion | R1 | A1 | `C090N54TG79/1758517286.431379` | "No coaching, just observe and collect honest reactions." |
| F-AGE | slack | `C090N54TG79/1758554405.774120` | amendment | R5 | A2 | `C090N54TG79/1759266627.418203` | "the rules I posted in the channel after my note still stand" |
| F-INDUSTRY | slack | `C090N54TG79/1758733233.117446` | exclusion | R4 | A2 | `C090N54TG79/1759266627.418203` | "the rules I posted in the channel after my note still stand" |
| F-LEAD | gslides | `gslides:f_a087f049d271e9aa9f567f` | requirement | R5 | A2 | `C090N54TG79/1759266627.418203` | "how a session gets its audience label and how the lead is read is in the audience read criteria" |
| F-GATE | slack | `C090N54TG79/1758728411.540327` | delegation | R2 | A2 | `C090N54TG79/1759266627.418203` | "the rules I posted in the channel after my note still stand" |
| F-DEVICE | gdocs | `gdocs:f_748d26e760e54651eaa0d8 device groups` | requirement | R2 | A2 > F-GATE | `2c84150a541063a6138e2f5a0cff9f33` | "ZM session stability gate" |
| F-BUILD | gdocs | `gdocs:f_748d26e760e54651eaa0d8 builds` | exclusion | R3 | A2 > F-GATE | `2c84150a541063a6138e2f5a0cff9f33` | "ZM session stability gate" |
| F-LIMIT | github | `harmonygames-Games/match3d#476#rc_27` | requirement | R2 | A2 > F-GATE > F-DEVICE | `f_748d26e760e54651eaa0d8` | "limits on a pass sit in review on the PR for the branch the job ran on" |
| F-STATE | gdocs | `gdocs:f_c691d577b8f837eb4f9eaa` | format | R7 | A2 | `C090N54TG79/1759266627.418203` | "close the tickets the way your log note says" |
| F-REG | gsheets | `gsheets:f_43bc35baf77fd59f4e57b8 Register tab` | format | R14 | A3 | `f_43bc35baf77fd59f4e57b8` | "one row per session" |
| F-RERUN | slack | `D05GU6L0XFH/1758913471.205816` | requirement | R8 | A2 | `C090N54TG79/1759266627.418203` | "Robert already told you how not-counted sessions get handled" |
| F-PANEL | gmail | `julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com>` | requirement | R10 | A2 | `C090N54TG79/1759266627.418203` | "the panel results I forwarded you" |
| F-PANELDEF | slack | `C090N54TG79/1758729919.603185` | requirement | R10 | A2 | `C090N54TG79/1759266627.418203` | "read the panel the way I set out when Robert asked who those players were" |
| F-RET | slack | `C090N54TG79/1759167008.881274` | requirement | R11 | A2 | `C090N54TG79/1759266627.418203` | "retention the way Robert set it in the channel after Vincent's post" |
| F-MEMO | trello | `trello:68dc0acf1815df76ed9b887d desc` | format | R12 | A2 | `C090N54TG79/1759266627.418203` | "what the memo holds is on the roadmap card" |
| F-FOLDER | gdrive | `gdrive:d_8140f09bf9f1b94cb8ee2d` | destination | R13 | A2 > F-MEMO | `68dc0acf1815df76ed9b887d` | "memo goes in Julia's folder with her log note" |

**Amendments.** F-AGE: Julia's question and Leonard's answer, posted in the channel after the note (`C090N54TG79/1758553214.330914`, `C090N54TG79/1758554405.774120`) settle "25–45" as an age band and change that clause only. F-INDUSTRY (`C090N54TG79/1758733233.117446`) narrows who counts, later and in the same channel. F-LEAD (`f_a087f049d271e9aa9f567f`) is in a different service and fixes one label per session against the note's "and/or": the observer's label stands, so nothing is re-derived.

**Distractors outside the chain.** Robert's lean and "we decided" (`C090N54TG79/1759176983.189479`, `C090N54TG79/1759171957.791499`), PR `harmonygames-Games/match3d#466`, `ZOM-559`, the re-sent form, the Card System FTUE Doc (`gdocs: data.json /docs_documents/334`), and Leonard's S23 Ultra report (`C08R27X0EAH/1758420497.482989`).

**Relay.** R0 (`C0880U9751A`, row `4500761ad805eeda66272ec37c91a8ef`) is not in the brief but is needed: eight of the twelve observers never received the note in base. It carries the ask, no rule text.

## 5 Chains and trap register

**Honest reading first.** T-K1, T-K3, T-K4 and T-K5 are the real difficulty: four independent routes to one wrong answer. T-F is a side channel. T-PANEL, T-AUD and T-RET are delegated breadth: the ask points at them, so they cost volume and little else. The six distractors are real records (`ZOM-559`, `C090N54TG79/1759176983.189479`, `harmonygames-Games/match3d#466`) that clear the gate's counts, with low expected loss. So the 14 traps are 4 real blocks plus 10 that serve breadth and the floors. T-AGE was removed: the ask pointed straight at it, so it was dead. Families pass at exactly 7, supersessions at exactly 4 and distractors at exactly 6, so losing any one record fails the floor.

Most of the real difficulty is about what gets surfaced, plus the join after it (`00_Hardness_Deep_Analysis.md` section 2: "Opus reads it and ignores it" barely exists). The playbook warns that retrieval traps leak, so the table in S5a states what stays hard after complete retrieval, and for K1, K4 and K5 that part is modest.

**Chains.**

| Chain | root_cause | Ends in | Hops |
|---|---|---|---|
| CH-K3 | A24 | R2 | linear `ZOM-567` (Done ticket on level-20 Samsung scope cites Vision Bot run #15; Vincent's line says it covers the device gate) > gdocs `f_748d26e760e54651eaa0d8` (Samsung is the one device group on this gate; a pass covers a device only if it ran on that device and clears the group's sessions whatever day they ran; limits on a pass sit in review on the PR for the branch the job ran on) > slack `C05433XK267/1758803475.436309` (run #15 Success, Sep 25 12:31Z, branch Blake/visionBot) > github `harmonygames-Games/match3d#476#rc_27` (the job's pass comes from Unity editor play mode on the Jenkins machine with no phone in the loop) |
| CH-K1 | A13 | R1 | gsheets `f_43bc35baf77fd59f4e57b8` (13 sessions, one observer, one date) > gmail `julia.lawson@harmonygames.co/<CAefcc9dd45170efad4834318d398795bc1db8@mail.gmail.com>` (observer's form reports no coaching) > gcal `evt_da65644831bc088267263d` (Friday at Claire's, a second record of host and day) > gmail `julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>` (Claire states what she did before the group played, naming host and day) |
| CH-K5 | A14 | R3 | gdocs `f_4ceb107c67c8348b1df02b` (session Docs carry 0.3.127 (1943), in the same shape as the ordinary ids) > slack `d7122186e361aa99778c65cb1502759d` (Leonard's reply says build 1943 never went through a store) > gdocs `f_748d26e760e54651eaa0d8` (sessions on dev builds do not count) |
| CH-K4 | A18 | R4 | gdocs `f_524278b67bfa30dde78699` (Brian's notes Doc gives the group's neutral nickname, Kadıköy ekibi, with a clean RPG label) > slack `246d6f4a90620e5dafbb06068f450e46` (a Turkish line in the DM says Kadıköy ekibi works in games) > slack `e72083b249987542a134098010edd305` (game-industry people do not count) |

**Trap register.**

| Trap | Family | Records | Requirement | Expected wrong reading | Resolver | Discovery order | Honest class |
|---|---|---|---|---|---|---|---|
| T-K3 | done_gap | `ZOM-567`, `cmt_38b3cc50dceda37f40f5`, `harmonygames-Games/match3d#476#rc_27`, `harmonygames-Games/match3d#476#rev_3`, `C05433XK267/1758803475.436309` | R2 | the 11 Samsung sessions count: ZOM-567 is Done and its owner says run #15 covers the device gate | Arthur Blake's inline note on the file the job runs says the pass comes from editor play mode with no phone involved | the Done ticket and owner's line are met in Linear with the session tickets; the PR note needs an inline-comment read on a PR no ticket names | REAL DIFFICULTY. Strongest block, not a wall; one direct call reaches it; no reserve move |
| T-K1 | effective_date | `julia.lawson@harmonygames.co/<CAefcc9dd45170efad4834318d398795bc1db8@mail.gmail.com>`, `julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>`, `evt_da65644831bc088267263d` | R1 | the 13 sessions count: the form and ticket report no coaching, and the Sep 30 ticket is the newest record | Claire's Sep 29 mail states what she did before the group played; tickets are a Sep 30 batch transcription of the Sep 26 form, so the mail is the later source | the log, ticket and form tie out first; the mail shares no vocabulary with the form mails | REAL DIFFICULTY. Splitter; only vocabulary hides it, because Julia's mailbox is short |
| T-K4 | superseding | `f_524278b67bfa30dde78699`, `246d6f4a90620e5dafbb06068f450e46` | R4 | Brian's 9 sessions count: the Doc's RPG label is clean and no mail or Doc comment questions it | Brian's later Turkish line in his DM with Julia says Kadıköy ekibi, the nickname on his Docs, works in games | the Doc is found through the log and Drive; the DM line sits in a Turkish working chat with no shared keyword | REAL DIFFICULTY. Splitter; the Turkish line must survive the collision test |
| T-K5 | exact_predicate | `julia.lawson@harmonygames.co/<CA01dc2d92371c7bfa63e451026f81fffed801@mail.gmail.com>`, `d7122186e361aa99778c65cb1502759d` | R3 | the 10 sessions count: form and log look complete and the build id reads as one more ordinary id | Leonard's thread reply says build 1943 never went through a store, so the store-builds clause applies | channel reads return parents only; the reply sits under a root the ask does not name | REAL DIFFICULTY. Splitter; odds untested, and #builds is a second fair path |
| T-F | cross_reference_gap | `167dc58affb9902420038f71d0f5af28` | R8 | not-counted tickets get a state and nothing else, or every one of the 43 gets a re-run note | Robert's reply limits the re-run note to sessions dropped for a technical reason, device or build | the ask names Robert as owner, not the DM; the reply sits under an off-topic root in that DM | SIDE CHANNEL. Easiest by design, weight 3 |
| T-PANEL | eliminating_evidence | `julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com>`, `7b38bd6429ce0f189456ac72af02f210`, `C090N54TG79/1758517286.431379` | R10 | panel average 3.1 over 10 players, or the note's 3-3.5 restated | the forward states one rating void with its reason, and Leonard's panel reply takes a void out of both sum and count | none declared | DELEGATED BREADTH. On the path the ask names; low expected loss |
| T-AUD | superseding | `f_a087f049d271e9aa9f567f`, `gdocs: data.json /docs_documents/328`, `C090N54TG79/1758517286.431379` | R5 | reads the target audience from the older GDD line (male RPG gamers, all ages), which reinforces an RPG call | the note widens the audience to casual and/or RPG adults, and the audience read criteria deck fixes one label per session and the lead test | a Docs search for audience returns the GDD; the criteria sit in a deck | DELEGATED BREADTH. On the path the ask names; low expected loss |
| T-RET | superseding | `f_4e21b203a62910bdae0353`, `2ca968ace3e14d1a34c535f8a5c0cd6e` | R11 | copies the KPI tab's simple cohort mean as D7 | Robert's channel post after Vincent's retention post sets install weighting over mature cohorts, computed from USER_COHORT_RETENTION | the KPI tab is a one-call answer in a Sheet shared with Julia | DELEGATED BREADTH. On the path the ask names; low expected loss |
| T-559 | distractor | `ZOM-559` | R2 | drops the Samsung sessions because ZOM-559 is open, reaching the right verdict on a reason the rule rules out | the stability gate says ZOM-559 is not a session blocker; only a device pass decides | a Samsung search returns ZOM-559 first | DISTRACTOR. Real record, counted for the floor; low expected loss |
| T-LEAN | distractor | `C090N54TG79/1759176983.189479`, `C090N54TG79/1759178344.878219`, `C090N54TG79/1759171957.791499` | R6 | treats the Sep 29 lean to hardcore and 'we decided' as settling keep | the ask reopens the change and rests it on the one audience call | the Sep 29 thread is the newest ZM debate in the named channel | DISTRACTOR. Real record, counted for the floor; low expected loss |
| T-466 | distractor | `harmonygames-Games/match3d#466` | R6 | merges the Sep 29 cards-earlier change with the PR #466 tutorial change and says it shipped | b429c2a8 is in no PR and on no build list; #466 is a different change | tutorial searches return #466 and its build lines | DISTRACTOR. Real record, counted for the floor; low expected loss |
| T-DUP | distractor | `julia.lawson@harmonygames.co/<CA8db5b364a9d7d3c1946e722aed490d591476@mail.gmail.com>` | R14 | counts the re-sent form as more sessions | the re-sent mail repeats the same sessions; the log and tickets hold them once | both mails sit on the first page of Julia's mailbox | DISTRACTOR. Real record, counted for the floor; low expected loss |
| T-FTUE | distractor | `gdocs: data.json /docs_documents/334` | R5 | cites the Card System FTUE line on RPG players as evidence for an RPG lead | the audience read criteria say sessions decide; the Doc is a June design opinion | a Docs search for RPG and casual returns it | DISTRACTOR. Real record, counted for the floor; low expected loss |
| T-S23 | distractor | `C08R27X0EAH/1758420497.482989` | R14 | adds Leonard's S23 Ultra bug report as a 61st session or a Samsung data point | that report has no ticket or log row and Leonard is not an observer | a Samsung search of #zombie-bugs returns it | DISTRACTOR. Real record, counted for the floor; low expected loss |

**Supersession chronology (oldest first; seeded `at` values must match the SQL).**

| Trap | Versions |
|---|---|
| T-K3 | 2025-09-30T16:50:22Z linear `cmt_38b3cc50dceda37f40f5` > 2025-09-30T20:10:26Z github `harmonygames-Games/match3d#476#rc_27` |
| T-K1 | 2025-09-26T21:00:12Z gmail `julia.lawson@harmonygames.co/<CAefcc9dd45170efad4834318d398795bc1db8@mail.gmail.com>` > 2025-09-29T10:02:47Z gmail `julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>` |
| T-K4 | 2025-09-23T09:05:00Z gdocs `f_524278b67bfa30dde78699` > 2025-09-23T20:23:32Z slack `246d6f4a90620e5dafbb06068f450e46` |
| T-K5 | 2025-09-23T22:14:09Z gmail `julia.lawson@harmonygames.co/<CA01dc2d92371c7bfa63e451026f81fffed801@mail.gmail.com>` > 2025-09-25T17:05:34Z slack `d7122186e361aa99778c65cb1502759d` |
| T-PANEL | 2025-09-22T05:01:26Z slack `C090N54TG79/1758517286.431379` > 2025-09-22T09:14:06Z gmail `julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com>` |
| T-AUD | 2025-06-19T20:29:04Z gdocs `gdocs: data.json /docs_documents/328` > 2025-09-22T05:01:26Z slack `C090N54TG79/1758517286.431379` > 2025-09-24T17:20:00Z gslides `f_a087f049d271e9aa9f567f` |
| T-RET | 2025-09-24T11:15:08Z gsheets `f_4e21b203a62910bdae0353` > 2025-09-29T17:30:08Z slack `2ca968ace3e14d1a34c535f8a5c0cd6e` |

**Hardness v2 trap selection.**

| v2 trap | Node | Convincing wrong source (who, when, authority) | Record that beats it | Weight-5 row it flips |
|---|---|---|---|---|
| Trap 1, done source with the gap elsewhere | T-K3 | `ZOM-567`, Done Sep 30 17:10Z, with Vincent's dated line (`cmt_38b3cc50dceda37f40f5`) that run #15 covers the device gate; QA owner's claim | `harmonygames-Games/match3d#476#rc_27`, Arthur Blake, owner of the job and the PR, Sep 30 20:10:26Z | S-K3a, S-H1, S-G1, S-G2 |
| Trap 2, correction elsewhere | T-K1 | Claire's own form (`julia.lawson@harmonygames.co/<CAefcc9dd45170efad4834318d398795bc1db8@mail.gmail.com>`, Sep 26), transcribed to 13 tickets | Claire's later mail, separate thread, Sep 29 10:02:47Z; same person, closer to the event than the Sep 30 batch transcription | S-K1a, S-H1, S-G1, S-G2 |
| Trap 2, correction elsewhere | T-K5 | Robert's form mail, Sep 23, and a complete log row | Leonard's reply `d7122186e361aa99778c65cb1502759d`, Sep 25, under `C090N54TG79/1758581651.167799`; he wrote the store-builds rule | S-K5a, S-H1, S-G1, S-G2 |
| Trap 5, exception in older records | T-K4 | Brian's Doc `f_524278b67bfa30dde78699`, Sep 23 09:05Z, clean label | Brian's line `246d6f4a90620e5dafbb06068f450e46`, Sep 23 20:23:32Z, in `D076RBM29JS`; same author, later | S-K4a, S-H1, S-G1, S-G2 |

**Corrections off the first-read path.** None sits in the superseded record's container or an anchor's. K5's reply is under a root in the ask's channel but on a different thread (`C090N54TG79/1758581651.167799`). K1 is a separate mail thread. K3 is on a PR no ticket names. K4 is in a DM, not in Docs.

### Mechanism portfolio (S5a)

**Budget.** Assigned Medium: cap 85 %, playbook target ≤ 77 %, requester target 62 % with about 64 % acceptable. Channels: four blocks (`harmonygames-Games/match3d#476#rc_27` and the K1, K4, K5 records), plus the declared channels in `CHANNELS` (scale:verdict, tool_surface:state_writes, delegation:handling, chain:decision, synthesis:context). Geometry on the surface (`01_Gradable_Surface.json`): 23 slots, weight 77, seven of weight 5. The block mechanisms can flip 59 of 77. One block miss alone fails its own 8 plus 15 aggregate plus 6 decision plus 6 state weight: 35 of 77 (45.5 %), a score of 54.5 %. This holds for all four blocks only while S-F1 stays a presence check, which is how the surface has it (mechanisms R_F only). If the rubric graded the exact 21, a K3 or K5 miss would reach 38 of 77 (49.4 %), 1 point under the half-weight limit of `09_Rubric_Writing.md` gate 12, and losing one neutral weight would hit it. So S-F1 must stay presence. No weight was raised or moved. K3 remains the likeliest shared cause, so it could still exceed half of failing runs; that is disclosed, not solved. The rubric budget of 20–25 rows protects this: the deep analysis measured +40 easy weight as worth about 14 points of average.

**Priors.** Each from `hardness_ledger.py priors --model claude-opus-5-5 --family <family>`. Only `done_gap` has a record. The other six families return no entry, so the forecast uses a flat Beta(1,1): that is an absence of evidence, not a 50 % estimate. No Opus 4.8 transfer record is used. The brief's find odds are replaced by these find rates, one run finding the record, all judgement: F .70, K4 .45, K1 about .50, K3 about .50–.60 (`01b_Design_Review_Final.md`), K5 about .60–.75 (the carrier's measured 78 % found, lowered a little by the one id shape and the author move). `00_Carrier_Calibration.md` figures are miss rates, record-runs missed: github inline 21/30 missed overall, 3/12 on Julia tasks; gmail separate thread unpointed 41/72 missed; slack channel thread reply 4/18 missed, so about 78 % found; slack DM thread reply 4/24 missed.

```text
PRIORS for claude-opus-5-5 · UNCALIBRATED (hardness_ledger.py priors, one call per family)
--family A13: no entry for this family
--family done_gap: done_gap: Beta(1.0, 2.0) mean 0.33 n_eff 1.0 from 1 trial(s) · per task julia_card_art_signoff 1.0 (1 trial(s), deff 1.0) · records 1 excluded 0
--family A18: no entry for this family
--family A17: no entry for this family
--family A14: no entry for this family
--family A19: no entry for this family
--family A15: no entry for this family
```

| Rule | Mechanism | Prior family | Prior (Opus 5.5) | Ledger record ids | Nodes | Req | Natural-reading fallback | Natural call that returns the deciding record | Hard step left after complete retrieval | Slots it can flip |
|---|---|---|---|---|---|---|---|---|---|---|
| R_K1 | A13 | A13 | no ledger entry for this family; flat Beta(1.0, 1.0) mean 0.50 n_eff 0.0 | none | T-K1, CH-K1 | R1 | the form's no-coaching line stands, so the 13 sessions count | `julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>` by `gmail_search_messages` or a listing, then a body read | Join by host and day across 13 tickets, and read an unlabelled account of what happened as coaching | S-K1a, S-K1b, S-H1, S-G1, S-G2, S-DEC, S-BRIAN, S-ST1, S-ST2 |
| R_K3 | A24 | done_gap | Beta(1.0, 2.0) mean 0.33 n_eff 1.0, 1 trial | `hev_2e118ac21ad437f9` | T-K3, CH-K3 | R2 | the Done ticket and owner's line clear the device group, so the 11 sessions count | `harmonygames-Games/match3d#476#rc_27` by the inline review-comment read on the PR | Decide that editor play mode does not meet "a clean pass covering that device", against a dated human claim, then find the 11 sessions by marketing names and model numbers | S-K3a, S-K3b, S-H1, S-G1, S-G2, S-DEC, S-BRIAN, S-ST1, S-ST2 |
| R_K4 | A18 | A18 | no ledger entry for this family; flat Beta(1.0, 1.0) mean 0.50 n_eff 0.0 | none | T-K4, CH-K4 | R4 | Brian's clean label stands, so the 9 sessions count | `246d6f4a90620e5dafbb06068f450e46` in `D076RBM29JS` by a history read of the DM | Read a Turkish line about a group, and join it by its nickname to Brian's Docs | S-K4a, S-K4b, S-H1, S-G1, S-G2, S-DEC, S-BRIAN, S-ST1, S-ST2 |
| R_K5 | A17 | A17 | no ledger entry for this family; flat Beta(1.0, 1.0) mean 0.50 n_eff 0.0 | none | T-K5, CH-K5 | R3 | build id 1943 is treated as ordinary, so the 10 sessions count | `d7122186e361aa99778c65cb1502759d` by `slack_conversations_replies` on `C090N54TG79/1758581651.167799` | Join one id across 60 Docs and apply the store-builds clause to it | S-K5a, S-K5b, S-H1, S-G1, S-G2, S-DEC, S-BRIAN, S-ST1, S-ST2 |
| R_F | A14 | A14 | no ledger entry for this family; flat Beta(1.0, 1.0) mean 0.50 n_eff 0.0 | none | T-F | R8 | no re-run note, or a note on all 43 not-counted tickets | `167dc58affb9902420038f71d0f5af28` by replies under `D05GU6L0XFH/1758901945.292269` | Limit the re-run note to technical drops, 21 of the 43 | S-F1 |
| R_D | A19 | A19 | no ledger entry for this family; flat Beta(1.0, 1.0) mean 0.50 n_eff 0.0 | none | T-PANEL | R10 | mean of all 10 ratings, 3.1 | `julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com>` by a body read | Remove the void from sum and count | S-D1 |
| R_E | A15 | A15 | no ledger entry for this family; flat Beta(1.0, 1.0) mean 0.50 n_eff 0.0 | none | T-RET | R11 | simple cohort mean from the KPI tab | `2ca968ace3e14d1a34c535f8a5c0cd6e` by a read of the channel after `C090N54TG79/1759165414.829399` | Compute install-weighted D7 over the mature cohorts in `snowflake.USER_COHORT_RETENTION` | S-E1 |

**Four A5b checks per node.**
- R_K1: incorporated through the note's "No coaching" (`C090N54TG79/1758517286.431379`); survives retrieval weakly, the join and the reading remain; tool surface clean, reachable on page 1 of Julia's mail (`julia.lawson@harmonygames.co/1844592159752803121`); graded on S-K1a, S-K1b and the aggregates.
- R_K3: incorporated through F-GATE, F-DEVICE and F-LIMIT (`f_748d26e760e54651eaa0d8`); survives retrieval best of the four, because a confident human claim must be overturned; tool surface is the one risk: the comments result for `harmonygames-Games/match3d#476` is about 266–285K characters and spills (one observation), so a miss caused by the spill alone would be CONFOUNDED; graded on S-K3a, S-K3b and the aggregates. Base text helps a careful reader already on the PR: the CodeRabbit summary `harmonygames-Games/match3d#476#c_1` says "Editor window", "Play mode" and "run plans headlessly", the path holds `/Editor/`, and the runbook `page_qa_runbook` names real devices. So the true gate is opening the PR, and the gate Doc sentence points there. The seeded "a pass covers a device only if it ran on that device" lets "no phone in the loop" answer the rule directly, because Arthur never names Samsung.
- R_K4: incorporated through F-INDUSTRY (`C090N54TG79/1758733233.117446`); survives weakly, a read of the DM settles it and the nickname makes the join; tool surface clean, page 1 of `D076RBM29JS`; graded on S-K4a, S-K4b and the aggregates.
- R_K5: incorporated through F-BUILD (`f_748d26e760e54651eaa0d8`); survives weakly; tool surface clean, one replies call on `C090N54TG79/1758581651.167799`; the #builds post is a second fair path, and an author search on Robert no longer returns K5 with F; graded on S-K5a, S-K5b and the aggregates.
- R_F, R_D, R_E: incorporated by name in the ask (`C090N54TG79/1759266627.418203`); each is correct work rather than a hidden fact; weight 3 only.

**Candidates considered and rejected.**

| Candidate | Anchor | Why rejected |
|---|---|---|
| K2 tutorial split | `harmonygames-Games/match3d#466` | Regrouping moves no count or mean, so one cause and two outputs (review B2); dropped by requester |
| S memo access | `C090N54TG79/1759207989.371869` | Moves nothing central; thread freed |
| C duplicates as a trap | `julia.lawson@harmonygames.co/1844318948033312842` | Mandatory read, always caught; kept as hygiene only (T-DUP) |
| T-AGE as a trap | `C090N54TG79/1758554405.774120` | The ask points at it; dead |
| K3 on PR #463 | `harmonygames-Games/match3d#463` | Post-merge comment has no base precedent, 0 of 23 |
| K3 no-mirror slot | `C093LEZGF6J/1759258475.735779` | Could read as an integration gap; coherence was the risk to remove |
| K5 under the New Item thread | `C090N54TG79/1758757016.553559` | Robert's art list, so a session reply would not fit |
| Panel audience labels | `leonard.hayes@harmonygames.co/1843922088670958384` | Would be invented, and could pull the lead inside the band (Resolution C2) |

### rev7 delta (S0r, 2026-11-08): mechanism portfolio after the rev6 pre-check

Source of the changes: `01a_Hardening_Report.md` §8–§11 and the S0r dispositions in section 14. Truth from `Working_Files/solver/solver.py` on the rev7 SQL (`Working_Files/run_forensics/rev7/01_Universe_Inject.sql`): 82 sessions (80 ticketed `ZOM-568`..`ZOM-647` plus Owen's two late sessions T1/T2), 45 counted; casual 27 at 103.5 (3.8333), RPG 18 at 63.0 (3.5000), gap 0.3333, so casual leads and the call is HOLD. Each single-rule miss gives KEEP (no clear lead): K4 −0.093, K1 −0.151, K5 −0.125, K3 +0.060, G +0.189, T +0.171, all off the 0.25 edge by ≥ 0.06 (`f_a087f049d271e9aa9f567f`). Re-run notes go on the 13 build-1943 drops only (`167dc58affb9902420038f71d0f5af28`). Panel 3.33 over 9 (`7b38bd6429ce0f189456ac72af02f210`). Retention 10.47 % over 16 rows, 2,607 installs (`f_4e21b203a62910bdae0353`).

De-signposting (all proposals of §9 taken): Leonard's ask `C090N54TG79/1759266627.418203` now carries the asks only; the gate Doc `f_748d26e760e54651eaa0d8` loses "A closed ticket isn't a pass." and the Sep 30 update line, and its Passes line reads "A pass is a clean test run of the build players get. Arthur Blake owns the Vision Bot job and says what its passes do and don't cover."; Vincent's ZOM-567 comment `cmt_38b3cc50dceda37f40f5` no longer says "no Samsung phone" or claims the device gate. The rule fragments now chain through the note (`C090N54TG79/1758517286.431379`, F-AGE, F-INDUSTRY, F-GATE, F-RERUN) and the roadmap card (`68dc0acf1815df76ed9b887d`, F-STATE, F-PANEL, F-PANELDEF, F-RET), not through an index in the ask.

| Rule | Mechanism | Prior family | Prior (Opus 5.5) | Ledger record ids | Nodes | Req | Natural-reading fallback | Natural call that returns the deciding record | Hard step left after complete retrieval | Slots it can flip |
|---|---|---|---|---|---|---|---|---|---|---|
| R_K3 (rebuilt, two-sided) | A24 | done_gap | Beta(1.0, 3.0) mean 0.25 n_eff 2.0, 2 trials | `hev_2592b8dada401b01`, `hev_2e118ac21ad437f9` | T-K3, CH-K3 | R2 | no on-device pass is found (ZOM-567 / Vision Bot is editor-only per `harmonygames-Games/match3d#476#rc_27`), so the 13 Samsung sessions are dropped with re-run notes | `3dd0b6d6c52c21cd5bbfcd6d6f5345cd` by a history read of `C08R27X0EAH`, then `f_cadae9f611d82d56ac02c3` | Accept a QA matrix row that names the phone only as SM-A546E as "a clean pass covering that device", against the Done ticket and Arthur's note, then carry it to all 13 Samsung sessions | S-K3a, S-K3b, S-H1, S-G1, S-G2, S-DEC, S-BRIAN, S-ST1, S-ST2 |
| R_G (new) | A13 | A13 | Beta(1.0, 2.0) mean 0.33 n_eff 1.0, 1 trial | `hev_95929012ed8c2503` | T-G, CH-G | R4 | no doc or ticket names the player's work, so every non-Brian session counts | `038b5eb5a30326895cb54756`, `0810fb8287e489c125fe2cd9` by `contacts_search_contacts` on the notes Docs' "Player:" name | Join each player by name to Julia's contacts and read a job title as "works in games" under `e72083b249987542a134098010edd305` | S-Ga, S-Gb, S-H1, S-G1, S-G2, S-DEC, S-BRIAN, S-ST1, S-ST2 |
| R_T (new) | A17 | A17 | Beta(1.0, 2.0) mean 0.33 n_eff 1.0, 1 trial | `hev_d32ebec661ad71ba` | T-T | R14 | the read is the ticketed sessions only; the late inline sessions are missed | `julia.lawson@harmonygames.co/<CAab474c9390349b2f96626bafff9ff2c5f9cd@mail.gmail.com>` by a thread read of Owen's form thread | Treat two inline lines in a late reply as sessions the log note says get a ticket and a log row | S-Ta, S-Tb, S-H1, S-G1, S-G2, S-DEC, S-BRIAN |
| R_E (rebuilt) | A15 | A15 | Beta(1.0, 2.0) mean 0.33 n_eff 1.0, 1 trial | `hev_d4c64a63c62b7037` | T-RET | R11 | install-weighted over all 47 mature cohorts (9.09 %), missing the 2025-07-24 cut-off | `f_4e21b203a62910bdae0353` (KPI tab, note row) by `gsheets` read of the snapshot | Apply a later, separate scope correction to the warehouse number | S-E1 |
| R_K1, R_K4, R_K5, R_F, R_D (kept) | A13, A18, A17, A14, A19 | as above | Beta(1.0, 2.0) mean 0.33 each | `hev_95929012ed8c2503`, `hev_7931898c8f612018`, `hev_d32ebec661ad71ba`, `hev_0bbc5289e9cdfa03`, `hev_a27d065c2054f0b4` | as above | R1, R4, R3, R8, R10 | as above | as above, no longer named by the ask | as above; counted as controls, not for difficulty (§9) | as above |

```text
PRIORS for claude-opus-5-5 · UNCALIBRATED (hardness_ledger.py priors, one call per family, 2026-11-08)
  A13: Beta(1.0, 2.0) mean 0.33 n_eff 1.0 from 1 trial(s) · per task julia-gtm 1.0 (1 trial(s), deff 1.0) · records 1 excluded 0
  A17: Beta(1.0, 2.0) mean 0.33 n_eff 1.0 from 1 trial(s) · per task julia-gtm 1.0 (1 trial(s), deff 1.0) · records 1 excluded 0
  done_gap: Beta(1.0, 3.0) mean 0.25 n_eff 2.0 from 2 trial(s) · per task julia-gtm 1.0 (1 trial(s), deff 1.0), julia_card_art_signoff 1.0 (1 trial(s), deff 1.0) · records 2 excluded 0
  A15: Beta(1.0, 2.0) mean 0.33 n_eff 1.0 from 1 trial(s) · per task julia-gtm 1.0 (1 trial(s), deff 1.0) · records 1 excluded 0
  A18: Beta(1.0, 2.0) mean 0.33 n_eff 1.0 from 1 trial(s) · per task julia-gtm 1.0 (1 trial(s), deff 1.0) · records 1 excluded 0
  A14: Beta(1.0, 2.0) mean 0.33 n_eff 1.0 from 1 trial(s) · per task julia-gtm 1.0 (1 trial(s), deff 1.0) · records 1 excluded 0
  A19: Beta(1.0, 2.0) mean 0.33 n_eff 1.0 from 1 trial(s) · per task julia-gtm 1.0 (1 trial(s), deff 1.0) · records 1 excluded 0
```

The priors are the rev6 pre-check records (every one a miss for the design, n = 1), so they say these families did not land once on this task; they are not landing rates for the rebuilt nodes.

**Four A5b checks, rev7 nodes.**
- R_K3: incorporated through F-GATE → F-DEVICE → F-QA ("A pass is a clean test run of the build players get", `f_748d26e760e54651eaa0d8`); survives complete retrieval, because the decoys (`cmt_38b3cc50dceda37f40f5`, `harmonygames-Games/match3d#476#rc_27`) now argue for the wrong side and the matrix names no brand; tool surface clean, `C08R27X0EAH` is a private channel Julia is in (`persona_view` YES at injection); base support: Confluence `page_qa_runbook` ("on real devices, not just the emulator"; "QA posts the completed matrix in #zombie-bugs"), read-only. Graded on S-K3a, S-K3b and the aggregates.
- R_G: incorporated through F-STATE → F-PLAYERS (log note `f_c691d577b8f837eb4f9eaa`: "Players are in my contacts"); survives retrieval, because no keyword in any doc, ticket or form carries the job; tool surface clean, Contacts is unscoped; graded on S-Ga, S-Gb and the aggregates. Brian's nine contacts carry no job, so Brian's DM `246d6f4a90620e5dafbb06068f450e46` stays the sole decider for his group.
- R_T: incorporated through F-STATE → F-LATE (log note: "Any form that comes in after this batch gets a ticket and a log row when I see it"); survives retrieval only if the reader reads past the batch; tool surface clean, page 1 of Julia's mail; graded on S-Ta, S-Tb and the aggregates.
- R_E: incorporated through F-MEMO → F-RET → F-RETCUT; the correction sits on Vincent's own sheet, not in the request's channel; graded on S-E1 only (weight 3, context).

Volume, planned apart from the traps (requester asked 400+ calls over all 13 services, 2026-11-08): one more cohort of 20 sessions, `ZOM-628`..`ZOM-647`, observed by Douglas (12, Sat Sep 27) and Frederick Stone (8, Mon Sep 29), all governed by the existing rules. It earns no hardness credit (v2 Part 4). Victor Barnes, first named as the second observer, left in April 2025 (`Evals/ENVIRONMENT.md`; SC-36; `activity.json` quiet_since_2025-04), so the 12 sessions are Douglas's (active at the clock, `d_cd7849ec043ab3da107f8c`, already an observer on `ZOM-625`); numbers unchanged.

### Liveness flags (S5b)

Advisory, UNCALIBRATED. Tool output, then a disposition for every flag. The tool's "0/6 recorded" line counts a dispositions JSON, which `--design` was not given; the dispositions are the table below.

```text
TRAP LIVENESS · ADVISORY · UNCALIBRATED · lexical warnings, not proof · DESIGN (no SQL: record text unavailable, only manifest-structure flags can fire) · on the Season Pass backtests these are development fixtures, not validation
  hub C090N54TG79/1759266627.418203 · direct delegations 10 · rule placement: A15 nodes only: ['T-RET'] (mechanism_portfolio); every other node SKIP
  T-K3 done_gap           breadcrumb  [rule placement SKIP: not an A15 node]
  T-K1 effective_date     -  [rule placement SKIP: not an A15 node]
  T-K4 superseding        breadcrumb  [rule placement SKIP: not an A15 node]
  T-K5 exact_predicate    -  [rule placement SKIP: not an A15 node]
  T-F  cross_reference_ga breadcrumb  [rule placement SKIP: not an A15 node]
  T-PANEL eliminating_eviden breadcrumb  [rule placement SKIP: not an A15 node]
  T-AUD superseding        breadcrumb  [rule placement SKIP: not an A15 node]
  T-RET superseding        breadcrumb
  T-559 distractor         -  [rule placement SKIP: not an A15 node]
  T-LEAN distractor         -  [rule placement SKIP: not an A15 node]
  T-466 distractor         -  [rule placement SKIP: not an A15 node]
  T-DUP distractor         -  [rule placement SKIP: not an A15 node]
  T-FTUE distractor         -  [rule placement SKIP: not an A15 node]
  T-S23 distractor         -  [rule placement SKIP: not an A15 node]
  dispositions: 0/6 recorded
```

```text
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      7 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 7 requirements: {'R1': ['R_K1'], 'R2': ['R_K3'], 'R4': ['R_K4'], 'R3': ['R_K5'], 'R8': ['R_F'], 'R10': ['R_D'], 'R11': ['R_E']}  [Part 5 rule 1]
  FLAG       DECISION_FLIP   4 of 7 rules can flip a weight-5 slot; not: ['R_F', 'R_D', 'R_E']  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     3 weight-5 total(s); 3 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  SKIP       RULE_IN_PROMPT  no prompt (04_Prompt.txt) yet  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']

Flags (each needs a written disposition; redesign the difficulty, never weaken a fairness link or raise a weight):
  DECISION_FLIP R_F: rule R_F (A14) can flip slots of weight [3], no weight-5 slot
  DECISION_FLIP R_D: rule R_D (A19) can flip slots of weight [3], no weight-5 slot
  DECISION_FLIP R_E: rule R_E (A15) can flip slots of weight [3], no weight-5 slot
```

| Flag | Node | Disposition | Record |
|---|---|---|---|
| breadcrumb | T-K3 | Keep. The flagged link is the rule reply to the gate Doc, not to the deciding record; the deciding note stays unnamed | `C090N54TG79/1758728411.540327`, `harmonygames-Games/match3d#476#rc_27` |
| breadcrumb | T-K4 | Keep. The flagged link is the industry rule, not the DM line | `C090N54TG79/1758733233.117446`, `246d6f4a90620e5dafbb06068f450e46` |
| breadcrumb | T-F | True and accepted: delegated by owner, the fair chain review M1 required. Side channel | `167dc58affb9902420038f71d0f5af28` |
| breadcrumb | T-PANEL | True and accepted: delegated breadth. Removing the link would break incorporation | `7b38bd6429ce0f189456ac72af02f210` |
| breadcrumb | T-AUD | True and accepted: delegated breadth; the deck is named by what it governs | `f_a087f049d271e9aa9f567f` |
| breadcrumb | T-RET | True and accepted: delegated breadth. Rule placement is the one A15 node checked; it stays in the channel post after Vincent's post | `2ca968ace3e14d1a34c535f8a5c0cd6e` |
| DECISION_FLIP | R_F | Accepted. Weight 3 by the kind of work; F is a side channel by brief. Weight not raised | `167dc58affb9902420038f71d0f5af28` |
| DECISION_FLIP | R_D | Accepted. Panel is context (Resolution C2). Weight not raised | `julia.lawson@harmonygames.co/1843954918097449014` |
| DECISION_FLIP | R_E | Accepted. Retention is one context row. Weight not raised | `snowflake.USER_COHORT_RETENTION` |
| RULE_IN_PROMPT SKIP | no node | No prompt exists yet; re-run at the prompt stage, against `C090N54TG79/1759266627.418203` | `C090N54TG79/1759266627.418203` |

SAME_PLACE on T-AUD was a real flag before the deck move; it now reports 0 flagged.

## 6 Failure-diversity plan

| Chain | Who plausibly misses it | Find rate (judgement) | Requirements touched | Rows only this miss flips | Record |
|---|---|---|---|---|---|
| CH-K3 | Any run that reads reviews and stops short of the inline read; skips GitHub unless a build is disputed (3/3 blind plans) | .50–.60 | R2 | S-K3a, S-K3b | `harmonygames-Games/match3d#476#rc_27` |
| CH-K1 | Any run whose coaching keywords find nothing, and that lists no recent mail; Julia's mail stops Sep 17, so the seeded mails sit together and a search on Claire returns both | about .50 | R1 | S-K1a, S-K1b | `julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>` |
| CH-K4 | Any run that does not read the DM or does not read Turkish as evidence | .45 | R4 | S-K4a, S-K4b | `246d6f4a90620e5dafbb06068f450e46` |
| CH-K5 | Any run that pages the channel and reads only the named thread | .60–.75 | R3 | S-K5a, S-K5b | `d7122186e361aa99778c65cb1502759d` |
| T-F | Any run that does not follow the owner to the DM | .70 | R8 | S-F1 | `167dc58affb9902420038f71d0f5af28` |

No single discovery gates most requirements: the four routes are independent and no block unlocks another. Which block a run misses sets which `S-K?` rows fail, so runs differ there. What is shared: S-H1, S-G1, S-G2, S-DEC, S-BRIAN, S-ST1, S-ST2 fail under any block miss (forecast P(fail) 0.92 and P(fails all six) 0.69 per slot, at flat priors). That is a real concentration, not a diversity. Any run with a miss scores at most about 54.5 %, and a clean run scores near 100 %, so spread and the pattern gate rest on the mix of clean and missed runs. Pre-register `/create-allfail` reasons for S-H1, S-G1, S-G2 (brief section 9). Keep K1, K4 and K5 splitting runs; at least one clean run helps the SD gate.

## 7 Deliverables and dependent writes

| Output | Tool | Target truth | Requirements |
|---|---|---|---|
| Register in `f_43bc35baf77fd59f4e57b8` | `gsheets_values_update` or `_append` | 60 verdicts, 17 counted, with audience, rating and reason | R14 |
| Memo in `d_8140f09bf9f1b94cb8ee2d` | `gdocs_create_document`, `gdocs_batch_update` | One audience decision; casual leads 3.833 to 3.375; panel and retention context | R5, R10, R11, R12, R13 |
| Reply to Leonard under `C090N54TG79/1759266627.418203` | `slack_send_message` | Hold (casual lead means hold, Resolution C14) | R6 |
| 60 ticket states on `ZOM-568` to `ZOM-627` | `linear_update_issue` `state` | Counted to Done (17), not counted to Canceled (43) | R7 |
| Re-run notes on 21 tickets, `ZOM-577` to `ZOM-597` | `linear_create_comment` | Technical drops only: K3 11 plus K5 10; before or after the state write, both accepted | R8 |
| Message to Brian in `C090N54TG79` | `slack_send_message` | Hold: tutorial and level-order work stops; thread or top level both accepted | R9 |

| Service | Tool | Count | Requirements | depends_on |
|---|---|---|---|---|
| gsheets | `gsheets_values_update` | 1 | R14 | T-K1, T-K3, T-K4, T-K5 |
| gdocs | `gdocs_create_document` | 1 | R5, R10, R11, R12, R13 | CH-K1, CH-K3, CH-K4, CH-K5, T-PANEL, T-RET |
| slack | `slack_send_message` | 1 | R6 | CH-K1, CH-K3, CH-K4, CH-K5 |
| slack | `slack_send_message` | 1 | R9 | CH-K1, CH-K3, CH-K4, CH-K5 |
| linear | `linear_update_issue` | 60 | R7 | T-K1, T-K3, T-K4, T-K5 |
| linear | `linear_create_comment` | 21 | R8 | T-F, T-K3, T-K5 |

A reuse-vs-create write: the register tab already exists in the workbook, so a run reuses it; the memo is new. Every write depends on findings. Rejected carriers: Trello card write, brief to PlayableX, merging b429c2a8, UA or store change. Stakes stay moderate: one build cycle, no money, retractable (`C090N54TG79/1759172166.547199`).

**Gradable surface.** `01_Gradable_Surface.json`: 23 slots, weight 77, mechanism share 88.3 % (reported, not gated), classes as amended 2026-11-08 (section 12). Each slot has a read or write in the section 9 budget, so a later OE step can reach it.

| Slot | Weight | Class | Role | Fact | Mechanisms |
|---|---|---|---|---|---|
| S-K1a | 5 | direct | exception | the 13 sessions of the one gathering at Claire's are not counted | R_K1 |
| S-K1b | 3 | write_content | core | the not-counted reason for the 13 sessions of the one gathering at Claire's names the deciding fact | R_K1 |
| S-K3a | 5 | direct | exception | the 11 Samsung sessions are not counted | R_K3 |
| S-K3b | 3 | write_content | core | the not-counted reason for the 11 Samsung sessions names the deciding fact | R_K3 |
| S-K4a | 5 | direct | exception | the 9 sessions of Brian's batch are not counted | R_K4 |
| S-K4b | 3 | write_content | core | the not-counted reason for the 9 sessions of Brian's batch names the deciding fact | R_K4 |
| S-K5a | 5 | direct | exception | the 10 sessions on build 1943 are not counted | R_K5 |
| S-K5b | 3 | write_content | core | the not-counted reason for the 10 sessions on build 1943 names the deciding fact | R_K5 |
| S-H1 | 5 | write_content | core | casual leads over counted sessions | R_K1, R_K3, R_K4, R_K5 |
| S-G1 | 5 | aggregate | volume | 17 sessions are counted | R_K1, R_K3, R_K4, R_K5 |
| S-G2 | 5 | write_content | core | casual mean 3.83 and RPG mean 3.38 over counted sessions | R_K1, R_K3, R_K4, R_K5 |
| S-DEC | 3 | write_content | core | the reply to Leonard says hold | R_K1, R_K3, R_K4, R_K5 |
| S-BRIAN | 3 | write_content | core | the message to Brian in #zombie-design says hold | R_K1, R_K3, R_K4, R_K5 |
| S-ST1 | 3 | write_content | core | 43 tickets move to Canceled | R_K1, R_K3, R_K4, R_K5 |
| S-ST2 | 3 | write_content | core | 17 tickets move to Done | R_K1, R_K3, R_K4, R_K5 |
| S-F1 | 3 | write_content | core | technical drops carry a re-run note | R_F |
| S-D1 | 3 | write_content | core | panel context: 3.33 over 9 players after the void | R_D |
| S-E1 | 3 | write_content | core | retention context: install-weighted D7 over mature cohorts | R_E |
| S-O1 | 3 | direct | sample | an ordinary Pixel session stays counted | none |
| S-O2 | 3 | direct | sample | another session of the same day stays counted | none |
| S-R1 | 1 | delivery | core | the register holds exactly the 60 session tickets | none |
| S-M1 | 1 | delivery | core | the memo exists | none |
| S-L1 | 1 | delivery | core | the reply sits in Leonard's thread | none |

Limits of the surface (`01_Manifest_Notes.md`): per-ticket state cannot be bound by the selector vocabulary, so state is two count slots. S-F1 checks presence, not the exact 21, and must stay so (section 5). R13 has no slot, because no selector reads a Doc's parent. Memo slots read `gdocs_create_document` only, so a run writing by `gdocs_batch_update` reads False on the surface. S-DEC cannot separate the reply from the Brian message, and S-BRIAN is a regex. S-G2 expects 3.38 and would miss a memo that writes 3.375. S-E1 now accepts 9.09 and 9.1 and rejects 9.15. The rubric stays the grading of record.

## 8 Service role map

| Service | Role | Fact or write it carries | Carrier |
|---|---|---|---|
| Slack | The note, its rule replies, the relay, the ask, K4, K5, F, both message writes | `C090N54TG79/1758517286.431379`, `C090N54TG79/1759266627.418203` | ● message text, thread replies |
| Gmail | 15 form mails, Claire's later mail, the panel forward | K1 and the only per-player panel ratings, `julia.lawson@harmonygames.co/1843954918097449014` | ● body, separate thread |
| Google Docs | Gate Doc, log note, 60 notes Docs, memo write | Store and device rules, state mapping, each build id, `f_748d26e760e54651eaa0d8` | ● body_text |
| Google Slides | Audience read criteria deck | Label, metric, tie band and minimum, `f_a087f049d271e9aa9f567f` | ● element text (not notes, ○) |
| Google Sheets | Workbook log and register, KPI snapshot | Cohort list and the register write, `f_43bc35baf77fd59f4e57b8` | ● grid_json, tab titles |
| Google Drive | Julia's root and Drive rows of seeds | Memo destination; sharing, `d_8140f09bf9f1b94cb8ee2d` | ● metadata, sharing |
| Google Calendar | "Friday at Claire's", Julia declined | Second record of host and day; no deciding fact, `evt_da65644831bc088267263d` | ○ for detail; ● summary and attendees |
| Trello | ZM ROADMAP card #80 | What the memo holds and where it goes, `68dc0acf1815df76ed9b887d` | ● card desc |
| Linear | 60 tickets, `ZOM-567`, `ZOM-559`, state writes | Device model per session in comments; the K3 wrong source | ● comments per §6b, ● state |
| GitHub | Open PR `harmonygames-Games/match3d#476` | The only record limiting run #15 | ● review comments |
| Snowflake | `snowflake.USER_COHORT_RETENTION`, read only, not injected | The retention value | ● rows |
| Confluence | `page_qa_runbook`, read context, not injected | Second fair route to doubt a bot-only pass; carries no graded fact | ● body, no seed |
| Contacts | No role | Tester contacts carry no job; none seeded, `harmonygames-Games/match3d#476` needs nothing here | no carrier used |

Eleven services carry weight and ten are injected (all but Snowflake; Confluence and Contacts are not among the eleven). `services_injected` is exactly 10, which the `--design` gate skips and the SQL must prove. Dropping Trello gives 9.

## 9 Call budget

Unconditional floor 291 of 351 planned, 11 services, largest share outside the per-record phase 34 %. Golden-run rule: a correct run needs this volume, because each row is a read or write a careful person must make.

| Phase | gcal | gdocs | gdrive | github | gmail | gsheets | gslides | linear | slack | snowflake | trello | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| discovery | · | · | 2 | · | · | 6 | · | 4 | 6 | · | · | 18 |
| rules | · | 6 | 2 | · | · | · | 1 | · | 8 | · | 2 | 19 |
| per-record | · | 60 | · | · | 3 | · | · | 141 | · | · | · | 204 |
| reconciliation | 2 | · | · | · | 4 | · | · | · | 10 | · | · | 16 |
| build-check | · | · | · | 8 | · | · | · | 2 | 4 | · | · | 14 |
| warehouse | · | · | · | · | · | · | · | · | · | 10 | · | 10 |
| writes | · | 3 | · | · | · | 3 | · | 2 | 2 | · | · | 10 |
| **unconditional floor** | 2 | 69 | 4 | 8 | 7 | 9 | 1 | 149 | 30 | 10 | 2 | **291** |

| Phase | Service | Calls | Reason | Status |
|---|---|---|---|---|
| discovery | slack | 6 | the ask, its channel pages back to the note, the rule posts after it | unconditional |
| discovery | gsheets | 6 | workbook metadata, log tab, register tab header, KPI Sheet metadata and tab | unconditional |
| discovery | linear | 4 | ZOM statuses and two pages of session tickets with a raised description cap, plus team lookup | unconditional |
| discovery | gdrive | 2 | find the session notes Docs and Brian's shared Docs | unconditional |
| rules | gdocs | 6 | stability gate and log note Docs, then the GDD, FTUE and QA checklist hits a careful reader must rule out | unconditional |
| rules | slack | 8 | search and read the panel thread, the retention thread and Robert's handling reply | unconditional |
| rules | gslides | 1 | read the audience read criteria deck: label, metric, tie band and minimum are only there | unconditional |
| rules | trello | 2 | find card #80 on ZM ROADMAP and read it | unconditional |
| rules | gdrive | 2 | resolve Julia's folder and list it | unconditional |
| per-record | linear | 60 | one linear_list_comments per session: device model is only there | unconditional |
| per-record | gdocs | 60 | one gdocs_get_document per session: build id and relation line are only there | unconditional |
| per-record | gmail | 3 | 15 form mails through gmail_get_messages_batch, about 5 per call | unconditional |
| per-record | linear | 60 | one state write per session, no bulk update tool | unconditional |
| per-record | linear | 21 | one re-run note per session dropped for a technical reason, K3 11 plus K5 10 | unconditional |
| per-record | linear | 60 | one linear_get_issue per session for the transcribed form header | counts 0: replaceable: linear_list_issues takes a caller-set maxDescriptionChars and linear_show_data is untested, so this row counts 0 unless the bulk view is shown to drop the header |
| reconciliation | gmail | 4 | list Julia's mail, open Claire's later mail, the panel forward and the re-sent form | unconditional |
| reconciliation | slack | 10 | Brian's DM and the open threads in #zombie-design and Robert's DM a careful person checks for session facts | unconditional |
| reconciliation | gcal | 2 | Julia's calendar around the session dates, which shows Friday at Claire's | unconditional |
| build-check | github | 8 | find the Vision Bot PR, read #476, its reviews, its inline comments and the job file | unconditional |
| build-check | slack | 4 | #builds run #15 and the #13 failure, plus the build id lookup | unconditional |
| build-check | linear | 2 | ZOM-567 comments and ZOM-559 | unconditional |
| warehouse | snowflake | 10 | table discovery, schema, ZM cohort pull and the weighted D7 per the rule | unconditional |
| writes | gsheets | 3 | register rows and read-back | unconditional |
| writes | gdocs | 3 | create the memo, edit, read back | unconditional |
| writes | slack | 2 | reply to Leonard and message to Brian | unconditional |
| writes | linear | 2 | spot read-back of the close-out | unconditional |

**Disclosure.** Requester accepted floors 260 and 160 in place of 500 and 300 (`volume_exception`, 2026-11-07), because 500 would need about 150 sessions, which is padding. The floor of 291 includes 81 writes in the per-record phase (60 state writes on `ZOM-568` to `ZOM-627`, 21 re-run notes). Per-record is 183 with the 60 state writes as a declared surface; evidence reads are 123. The 60-call `linear_get_issue` row counts 0 until `linear_show_data` and `maxDescriptionChars` are tested. The brief's 300 became 291 once F's scope was set at 21 (`01_Manifest_Notes.md`). A horizon of about 300 calls sits below the extreme profile by exception, not by default.

## 10 QC rails

### Two-reading table

| Decision point | Best reading | Strongest alternative | Resolved by | Result |
|---|---|---|---|---|
| "25–45" in the note | Age band | Headcount | Leonard's answer `C090N54TG79/1758554405.774120`, newer, same author | One reading |
| Coached gathering | 13 sessions not counted | Form says no coaching, so they count | Newer source and first-hand: Claire's mail of Sep 29 after her Sep 26 form; the Sep 30 ticket transcribes the form, so its date does not make it newer (`f_c691d577b8f837eb4f9eaa`) | One reading |
| Samsung clearance | 11 sessions not counted | `ZOM-567` Done and Vincent's line clear the group | Authority and newer source: the job owner's note `harmonygames-Games/match3d#476#rc_27` after the line; rule wording "a clean pass covering that device", and a pass covers a device only if it ran on that device | One reading |
| Scope of the device rule | Samsung is the one group on the gate; every other group needs no pass | Other open reports (`ZOM-475`, `ZOM-468`, `ZOM-449`, `ZOM-359`) also need a pass, which drops Android sessions and takes RPG under the minimum | `f_748d26e760e54651eaa0d8` names Samsung by model family and says every other group needs no pass, so no open report is read at all. The older-iPhone thread (`C08R27X0EAH/1758642623.835409`) touches no session device | One reading |
| Rule timing for K3 sessions | The pass decides, whatever day the session ran | Sessions before run #15 were uncleared when played, so 9 drop with no PR read and 2 are unsettled | Clause in `f_748d26e760e54651eaa0d8`: a valid pass clears the group's sessions whatever day they ran | One reading |
| Open bug as the reason | Reason is the missing pass | `ZOM-559` itself blocks the sessions | Gate Doc says `ZOM-559` is no session blocker; verdict is the same either way, reason differs | One reading |
| Non-store build | 10 sessions not counted | 1943 is one more ordinary id | Leonard's reply `d7122186e361aa99778c65cb1502759d`; `C05433XK267/1758575557.575349` is a second fair path to the same verdict | One reading |
| Game-industry group | 9 sessions not counted | Brian's clean label stands; a nickname says nothing about jobs | Later same-author line `246d6f4a90620e5dafbb06068f450e46` uses the same nickname, plus `C090N54TG79/1758733233.117446` | One reading |
| Which sessions set the lead | Sessions alone | Panel players also count | `f_a087f049d271e9aa9f567f` says sessions decide (Resolution C2) | One reading |
| Keep or hold | Casual lead means hold | Leaders' lean means keep | Ask states the mapping, `C090N54TG79/1759266627.418203` (Resolution C14); gap 0.458 is past the band | One reading |
| Close enough to call no clear lead | Clear casual lead | 17 sessions are too few | Stated band 0.25 and minimum 6 in `f_a087f049d271e9aa9f567f`; casual 9, RPG 8 | One reading |
| Re-run scope | 21 technical drops | All 43 not counted | Robert's reply `167dc58affb9902420038f71d0f5af28` | One reading |
| Panel average | 3.33 over 9 | 3.1 over 10 | Void stated in the forward; rule in `7b38bd6429ce0f189456ac72af02f210` takes it out of sum and count | One reading |
| Retention D7 | 9.09 install-weighted over the 47 rows with a D14 figure | 8.63 simple mean on the KPI tab `f_4e21b203a62910bdae0353` (45 rows through cohort 09-08, which fits its Sep 24 date) | Robert's reply `2ca968ace3e14d1a34c535f8a5c0cd6e`, newer than the tab, defines mature as cohorts that have a D14 figure | One reading |
| Brian's message destination | `C090N54TG79` | Thread or top level | Both reach him, same decision; the ask authorizes the channel | Both accepted; Rubric must accept: thread or top level |
| Re-run note order | Before or after the state write | One order required | No record orders them (C4) | Both accepted; Rubric must accept: either order |
| Re-sent form | One set of sessions | Extra sessions | Log and tickets hold them once, `julia.lawson@harmonygames.co/1844318948033312842` | One reading |

No BOTH_FAIR_FIGURE fork is designed. No gradable slot in `01_Gradable_Surface.json` is a date, so a PT/UTC day split decides nothing.

### Reach table (load-bearing records)

Base records, plus the one seeded record added since grounding (the deck row); seeds are checked at the injection gate. Each row below was run through `persona_view.py can-see julia_lawson`.

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
| `C08R27X0EAH/1758420497.482989` | slack | YES | Distractor | T-S23, Leonard's S23 Ultra report |
| `D05GU6L0XFH/1758907345.403359` | slack | YES | Reserve | F second choice |
| `f_89fadbc54660c9881d8cf9` | gdocs | YES | Distractor | Older GDD |
| `d_8140f09bf9f1b94cb8ee2d` | gdrive | YES | LB | Julia's root folder |
| `f_a087f049d271e9aa9f567f` | gslides | Planned seed | LB | Audience read criteria; Julia owns it, proof at the injection gate |
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
julia_lawson slack C08R27X0EAH/1758420497.482989: YES
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

**Incorporation.** Every requirement is named by an incorporated fragment or anchor (`requirement_coverage`, `C090N54TG79/1759266627.418203`), and the note and ask are the prompt's nouns.

**Feasibility.** `Evals/references/tools/catalog.json` holds `gsheets_values_update`, `gsheets_values_append`, `gdocs_create_document` (title, bodyText, driveFileId), `gdocs_batch_update`, `slack_send_message` (thread_ts), `linear_update_issue` (state), `linear_create_comment`, `linear_list_comments`, `gmail_get_messages_batch`, `gslides_get_presentation_text`, `linear_show_data`, `gdrive_move_file`. Done and Canceled both exist on ZOM. Julia owns the workbook and her folder, and she created the tickets. `gdocs_create_document` has no parent parameter, so whether a new Doc lands in `d_8140f09bf9f1b94cb8ee2d` is untested, and `gdrive_move_file` returned 404 in 6 of 6 runs on another task's folder (`00_Opus_Behaviour.md`, Q7). R13 therefore must not be graded until a run shows the path works. Numeric values are observable at the precision used.

**Precedence.** Deciding facts sit only in ● carriers of `Ask_Carriers.md` §5 as amended by §6b; Linear comments are ● there. GCal detail stays supporting (`evt_da65644831bc088267263d`). The deck's facts sit in element text, never notes (`f_a087f049d271e9aa9f567f`).

**Explicit rules.** Comparison across versions is by fact date (`f_c691d577b8f837eb4f9eaa`). "Now" against a future deadline does not arise. Each write's end state is set by a record: states by the log note, hold or keep by the ask. Every cross-reference postdates its target: R2b after the Doc, card after the log note, ask after all tickets. The gate Doc is dated Sep 24 15:30Z, after Bot #8 and the first Vision Bot success (`C05433XK267/1758669042.879369` is job #1, Sep 23 23:10:42Z), not Sep 23 18:30Z, which predated the job. #476 opened Sep 30, so run #15 tested a branch and no PR: the Doc says "the PR for the branch the job ran on", and calls Arthur the job's owner, not the tool's author (Samuel Turner wrote the CLI commits).

**Prompt naturalness.** The trigger needs only the anchors of section 4, the outputs and that Leonard needs the call. It must not hold rules, locations, ids, root causes, exclusions, the word "valid" or anything that invites an audit (brief section 2). Destinations are ones Julia knows or are named by a seeded record. No riddle, no rule list: all per-case rules are seeded.

**Grading devices.** Exact multiset of 17; aggregates 17, 43, means and gap; at most 5 samples per group with a volume slot (`S-G1`); direct rows only for groups an incorporated authority singles out; one row per required write. Exclusions are graded as counts on a required write, never as "left as found". No count the ask will not state. All for `ZOM-568` to `ZOM-627`.

**Coherence rail.** Every section 1a row is dispositioned. The one designed disagreement between records of different authors on a system-looking fact is a dated human claim: `cmt_38b3cc50dceda37f40f5`, overturned by `harmonygames-Games/match3d#476#rc_27`. Companion fields per section 11. Plan claims agree with base git: run #15 on `Blake/visionBot` (`C05433XK267/1758803475.436309`). The build-platform defect found while assembling this document is repaired: `ZOM-570`, `ZOM-573`, `ZOM-576` are iPhones on 0.3.38.

## 11 Record plan for /create-injection

Ids are minted in `01_Hardness_Manifest.draft.json`, collision-checked (`01_Manifest_Notes.md`). Keep them. Volume: 60 tickets `ZOM-568` to `ZOM-627`, 60 comments (`cmt_2fbcaf2d990d8b4e9c0d` onward), 60 notes Docs (`f_524278b67bfa30dde78699` onward), 15 form mails, Brian's Docs among the 60.

| Record | Id | Service | Date | Author | Companions and limits |
|---|---|---|---|---|---|
| Ask | `b07f1e10112b7661e1d8eaf3b127227f`, ts `1759266627.418203` | slack | Sep 30 21:10:27Z | Leonard Hayes | New root in `C090N54TG79`. Omit Leonard's travel, any ship claim, version, release date, Trello "BETA: Oct 10", spend, bots, fundraising, "beta data" |
| Rule posts after the note (top-level) | ts `1758553214.330914`, `1758554405.774120`, `1758728411.540327`, `1758733233.117446` | slack | Sep 22–24 | Julia, Leonard | Top-level in `C090N54TG79`; the note `C090N54TG79/1758517286.431379` keeps reply_count 0, because it has no base thread |
| K4 line | `246d6f4a90620e5dafbb06068f450e46`, ts `1758659012.418207` | slack | Sep 23 20:23:32Z | Brian Foster | `D076RBM29JS`, Turkish; uses the nickname Kadıköy ekibi from his Docs; avoid test, beta, playtest, build, RPG, casual, session, tester and any other form label. Base Sep 29 "sektör" talk there is Brian's own job case, so the seed must not read as that |
| K5 reply | `d7122186e361aa99778c65cb1502759d`, ts `1758819934.612483` | slack | Sep 25 17:05:34Z | Leonard Hayes | Root `C090N54TG79/1758581651.167799` rc 15 to 16, users 2 to 3, latest_reply bumped. On-topic reason needed (C16); names 1943; avoid "dev build" phrasing |
| F reply | `167dc58affb9902420038f71d0f5af28`, ts `1758913471.205816` | slack | Sep 26 19:04:31Z | Robert | Root `D05GU6L0XFH/1758901945.292269` rc 1 to 2, users 1 to 2; speaks of sessions, not tickets |
| Arthur's note | `harmonygames-Games/match3d#476#rc_27`, `#rev_3` | github | Sep 30 20:10:26Z | Arthur Blake | Path `Assets/Scripts/Utils/Bot/Editor/VisionBatchCLI.cs` and diff hunk; `line`, `position` and `commit_id` null as on all 26 base rows; no `side` or `subject_type` column; update `updated_at`. Avoid "Samsung", any fix, branch, build, schedule, "nightly", "cannot run on a device" |
| CodeRabbit reply | `harmonygames-Games/match3d#476#rc_28` (no review row; `#rev_4` removed) | github | Sep 30 20:11:04Z | CodeRabbit | 38 s later, inside the base 26–66 s; mirrors `37d66469c43368f08befb2d6bf0c8d28`, `2386636f2f828606f470fa38df201f16`; root reply_count 29 to 31 |
| Done ticket | `ZOM-567`, line `cmt_38b3cc50dceda37f40f5` | linear | Sep 30 16:30:41Z, line 16:50:22Z, closed 17:10:05Z | Vincent Parker | Names no PR, build number, "on main", "full regression" or "QA sign-off"; comment dated before close |
| Claire's mail | `julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>` | gmail | Sep 29 10:02:47Z | Claire Morgan | Subject "a small thing from Friday"; no fact in subject or first lines. Avoid playtest, beta, session, form, walked through, helped, coached, explained, hint, doesn't count, exclude, duplicate |
| Panel forward | `julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com>` | gmail | Sep 22 09:14:06Z | Leonard Hayes | Ratings 3.5, 3, 3.5, 4, 3, 3, 3.5, 1, 3, 3.5 with the eighth void; Leonard's copy byte-identical (Q10) |
| Gate Doc, log note, deck | `f_748d26e760e54651eaa0d8`, `f_c691d577b8f837eb4f9eaa`, `f_a087f049d271e9aa9f567f` | gdocs, gslides | Sep 24 15:30:02Z, Sep 30 16:35:20Z, Sep 24 17:20:00Z | Leonard, Julia, Julia | Drive row, sharing and native type for each. Gate Doc content in row R2 below. Log note says why the tickets exist. Deck: the observer's label stands |
| Workbook, KPI Sheet | `f_43bc35baf77fd59f4e57b8`, `f_4e21b203a62910bdae0353` | gsheets | Sep 30, Sep 24 11:15:08Z | Julia owns the workbook; Vincent Parker owns the KPI Sheet, shared with Julia | Drive rows; log and register tabs; KPI simple mean 8.63 (45 rows through cohort 09-08) |
| Card #80 | `68dc0acf1815df76ed9b887d` | trello | Sep 30 16:52:31Z | Leonard Hayes | Backlog `68c451221ebabaf255a7d16b`, createCard action and `dateLastActivity` agree |
| Friday event | `evt_da65644831bc088267263d` | gcal | Sep 26 17:00Z, created Sep 24 09:20Z | Claire Morgan | One row per attendee calendar; Julia declined; no description fact |

One deciding record per day: K4 Sep 23, K5 Sep 25, F Sep 26, never Sep 27–28. Pre-run tests from brief section 9 stay required: blind plan, collision test including mail bodies, tie-out 60 for 60, flip proof, careful-person walk, then one Opus pre-check. `rev_3` lint, spill handling, `linear_show_data`, `linear_list_comments` on injected rows (base has none, so 60 devices and Vincent's line ride on it), attachment search and non-member reads are still untested. Tickets carry jittered `created_at` values, no longer exactly 150 s apart.

### (a) K1 host and dates

**Host: Claire Morgan** (claire.morgan@harmonygames.co, Art Lead, UTC+3, active). Why she fits:
- Her seeded mails (`julia.lawson@harmonygames.co/<CAefcc9dd45170efad4834318d398795bc1db8@mail.gmail.com>`, `julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>`) fit: she is the only non-founder with a human-looking recent send (`sent_last` 2025-09-30, from `activity.json`). Oliver, Owen and Samuel have no sent mail at all. Marcus last sent in 2024-10, and Leonard removed him from `#zombie-design`.
- She is Julia's close friend, with Turkish DMs through Sep 24 (`D05HMBQUC8Z`, can-see YES). A friend writing about what happened at her place is natural.
- She is not Brian (SC-6), not Martin (her form is `julia.lawson@harmonygames.co/<CAefcc9dd45170efad4834318d398795bc1db8@mail.gmail.com>`), and holds no other job in the design. Robert, Vincent and Arthur stay on their own blocks.
- A calendar scan of Sep 20 to Oct 2 shows no event on Sep 26 for anyone, and her last Slack post that day is 16:28Z (`C08R8CHB0QL/1758904103.894649`).

| Item | Date | Note |
|---|---|---|
| Gathering (all 13 sessions, one session date) | Fri Sep 26, evening TRT | One date, no other session by Claire that day; `ZOM-607` to `ZOM-619` |
| Claire's form | Sep 26, about 21:00Z | Weekday; states no coaching; transcribed to 13 tickets and the log; `julia.lawson@harmonygames.co/<CAefcc9dd45170efad4834318d398795bc1db8@mail.gmail.com>` |
| K1 mail | **Mon Sep 29**, about 10:00Z | Separate thread, after the form, before the Sep 30 batch, and before the Sep 29 debate starts at 18:52Z; `julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>` |

Sep 29 beats Sep 24: a Sep 24 mail would need a gathering within two days of the note, on a work night, while this date gives a Friday evening. No record falls on Sep 27–28, and all dates are weekdays, so `sql_lint` raises no weekend warning.

Subject proposal: `a small thing from Friday`. The host and day stay in the body, and no fact sits in the subject or first lines. English: Claire and Julia chat in Turkish, but mail is a work register and K4 already holds the Turkish carrier. The collision test must still cover this subject and body against the K1 avoid list.

### (b) Calendar and Trello roles

**Calendar: real but supporting.** One event on Fri Sep 26 at 17:00Z, organizer Claire, attendees Claire and Julia, Julia declined, plain summary such as `Friday at Claire's`, no description fact. It is a second Julia-visible record of host and day, so the join does not rest on one mail. It also explains why Julia cannot know first-hand what happened. Base has social precedent, though it is rare ("hangout in PDX", Aug 2024). It carries no deciding fact, GCal being a ○ carrier. Sep 2025 has 9 events on Julia's calendar, so this one is visible: treat its effect on K1 find rate as a small rise in the forecast.

**Trello: thin, and I would not claim more.** One card, idShort 80, in Backlog `68c451221ebabaf255a7d16b` on `6851a6569f3bf818760632ab`, created by Leonard (`PERSON_6094_TRELLO_USER_ID`) inside his real board session of Sep 30 16:40:13–17:09:07Z. It names the card-order change as waiting on the read. It is a status echo: no deciding fact, no write target (rejected carrier in brief §6), no date, and it stays off the BETA list (SC-13, SC-14). It adds a truthful tracker and one distractor, nothing more. Base offers no better role: no card on the board mentions playtest, feedback, audience, friends or testers. If `hardness_gate.py` does not need Trello, dropping the card loses nothing, and the brief's "10 injected" then becomes 9.

**Update after grounding (01_Manifest_Notes.md).** Trello card `68dc0acf1815df76ed9b887d` now does more than echo status: it also states what the memo holds and where it goes (F-MEMO, F-FOLDER; R12, R13). Without that text the card has no real role, and it is what keeps services_injected at 10. Calendar event `evt_da65644831bc088267263d` stays supporting only.

### (c) Leonard's ask and Julia's reply

**Container: a new root by Leonard in `C090N54TG79`, Sep 30 about 21:10Z. Julia replies in that thread.**
- Julia and Leonard are live members, and every party to the Sep 29 debate is there. Newest base message: Robert 19:35:33Z (`C090N54TG79/1759260933.283799`), so the root becomes the newest parent.
- Window check for `C090N54TG79/1759266627.418203`: after 20:13Z, after all 61 tickets, after Arthur's note if that lands near 20:10Z, before Oct 1 00:00Z.
- Leonard's base Slack on Sep 30 stops at 18:24Z in the channels read (`C090N54TG79`), so nothing contradicts a later post.
- Rejected: the Julia–Leonard DM `D05HB64NMQU` has no export file after 2025-08, so a Sep 30 post there would restart a quiet DM. Under `C090N54TG79/1759172119.133819`: that thread is about bots. After the rule posts as a reply: it would bury the ask among them.
- Brian's message also goes in `C090N54TG79` (C10). Thread or top level both reach him, so the rubric should accept either.

### (d) Rule record homes and dates

Top-level posts after the note carry the rules, and each says what it refers to, so the rules enter through the note by name. None is in Confluence. Authors in `C090N54TG79` are live members only.

| Row | Record | Home | Date (about) | Author | Notes |
|---|---|---|---|---|---|
| R0 | Relay of the note's ask, no rule text | Slack top level in `C0880U9751A` | Sep 22 15:30Z | Julia | **Not in the brief; needed.** Reaches all twelve observers |
| R1 | "25–45" is an age band | Slack top-level posts after `C090N54TG79/1758517286.431379`: Julia's question, Leonard's answer | Sep 22 15:00 and 15:20Z | Julia, Leonard | The note keeps reply_count 0; the posts quote it |
| R2 | Stability rule and store-builds clause: a clean pass covering that device; a pass covers a device only if it ran on that device; Samsung, by model family, is the one group on this gate and every other group needs no pass; a valid pass clears the group's sessions whatever day they ran, and the Doc's rules apply to every session whatever day it ran; ZOM-559 is no session blocker; limits sit in review on the PR for the branch the job ran on; Arthur owns the job; dev builds do not count | New Google Doc `f_748d26e760e54651eaa0d8` owned by Leonard, shared with Julia, Robert, Brian, Vincent | Sep 24 15:30Z | Leonard | After Bot #8 (`C05433XK267`), before R3. Pointer by title in R2b |
| R2b | Pointer to the Doc (`2c84150a541063a6138e2f5a0cff9f33`) | Slack top-level post after the note | Sep 24 15:40Z | Leonard | Dated after the Doc |
| R3 | Game-industry exclusion only: game-industry people don't count | Slack top-level post after the note | Sep 24 17:00Z | Leonard | After Robert's "Audience can vary results" at `C090N54TG79/1758691528.127789`. The audience-labelling rule no longer lives here: see R3b |
| R3b | Audience read criteria: the observer's label stands, one label per session, lead is the higher mean star rating over counted sessions, at least 6 per audience, gap under 0.25 is no clear lead, sessions decide | Slides deck `f_a087f049d271e9aa9f567f` 'ZM audience read criteria', owned by Julia | Sep 24 17:20Z | Julia | Moved out of R3 after the v2 SAME_PLACE check. The ask names it by what it governs; no Slack reply points at it |
| R4 | Panel definition: stars per player, void treatment | Slack reply under `C090N54TG79/1758691397.679889` | Sep 24 16:05Z | Leonard | rc 2 → 3, users stays 2, after 15:55Z |
| R5 | Retention rule: install-weighted, mature cohorts, meaning cohorts that have a D14 figure | Slack top-level post after `C090N54TG79/1759165414.829399` | Sep 29 17:30Z | Robert | Refers to Vincent's retention post; that post keeps rc 0 |
| R6 | Julia's log note: counted → Done, not counted → Canceled, each ticket transcribes a dated form with session date; states why the tickets exist | New Doc owned by Julia in `d_8140f09bf9f1b94cb8ee2d` | Sep 30 16:35Z | Julia | After 16:26:02Z |
| R7 | Leonard's ask | Slack root in `C090N54TG79` | Sep 30 21:10Z | Leonard | Section (c); states the C14 mapping |

Sequence on Sep 30: `ZOM-567` created about 16:30Z, Vincent's line about 16:50Z, Done about 17:10Z, session tickets to about 19:45Z, Arthur's note about 20:10Z, ask about 21:10Z.

Counter updates beyond the brief: F's root goes rc 1 → 2 **and reply_users_count 1 → 2**, because Julia is the only base replier on `D05GU6L0XFH/1758901945.292269` and Robert would be new. K5's root goes to users 3, because Leonard is a new replier (review M4).

### Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| slack | INT-22 | Mail notices | None seeded; optional and never needed. Four roots get counter updates: `C090N54TG79/1758581651.167799`, `C090N54TG79/1758691397.679889`, `D05GU6L0XFH/1758901945.292269`, `C093LEZGF6J/1759258475.735779` |
| gmail | none | gmail: none, no integration has Gmail as its source | Forms and K1 (`julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>`) are human mail. Sender's copy sits in the sender's mailbox and Julia's copy in hers, both identical (Q10). The forward keeps Leonard's vendor copy |
| gcal | INT-11 | Invitation mail | Not seeded: a seeded meeting needs no mail. One row per attendee calendar, Claire and Julia |
| gdrive | INT-13 | Drive app DMs | None seeded; DM-only and optional. Drive rows mirror each seeded Doc and Sheet with sharing |
| gdocs | none | gdocs: none in the KB; the Drive row with the same id is the companion | Each seeded Doc (`f_748d26e760e54651eaa0d8` and the rest) has its Drive row and `shared_with_emails` |
| gsheets | none | gsheets: none in the KB; the Drive row with the same id is the companion | Julia owns the workbook `f_43bc35baf77fd59f4e57b8`; Drive row seeded with it |
| contacts | none | contacts: none, no integration feeds this service | No job on tester contacts; if the volume plan keeps contacts they carry a name and email only |
| github | INT-01, INT-23 | `#zombie-prs` copy under `C093LEZGF6J/1759258475.735779` (row 637fc98bc66d41b104fe243006fdcf98); CodeRabbit rc_28 26–66 s later | Seeded with fallback "[harmonygames-Games/match3d] Comment on #476". rc 29 → 31 with rc_28 mirrored (C8); `latest_reply` bumped. `rev_3` goes in `integration_exceptions` citing #470 rev_3; CodeRabbit's `rev_4` is not seeded; no timeline `reviewed` row (T01). Comment time must fall before 22:33:40Z |
| github | INT-02, INT-12 | Push posts, notification mail | None: no push is seeded; mail is optional |
| linear | INT-03 | linear[bot] on PRs that name a key | None: no seeded PR and `ZOM-567` is named by no PR |
| linear | INT-04, INT-05 | Slack notices, digest mail | None: a seeded state change needs no notice. Done on `ZOM-567` gets no `#zombie-match3d` post, though ZOM-553's got one at `C0880U9751A/1759236043.004679`, because not every transition is posted |
| trello | INT-21 | No Trello bot exists | No Slack post. Card, `createCard` action and `dateLastActivity` agree (T06) |
| gslides | none | gslides: none in the KB; the Drive row with the same id is the companion | Deck `f_a087f049d271e9aa9f567f` gets its Drive row and sharing fields; Julia is the owner |
| snowflake | none | snowflake: none, read only and never injected | `USER_COHORT_RETENTION` stays base; `snowflake.USER_COHORT_RETENTION` feeds R11 |
| confluence | none | confluence: none, read context only and never injected | `page_qa_runbook` stays as it is |

## 12 Self-test results

**hardness_gate --design, verbatim.**

```text
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
  [ok] ask_fragments: 20 fragments; need ≥ 12
  [ok] ask_fragment_services: 9 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 19 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 14 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 82; need ≥ 40 (source-defined: True)
  [ok] evidence_surfaces: 5 surfaces over 4 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 246; need ≥ 240
  [ok] call_budget: unconditional (verified) floor 358 of 438 planned calls (80 conditional on unverified tool behaviour count 0); need floor ≥ 340 (requester-confirmed volume_exception)
  [ok] call_budget_spread: 13 services in budget; largest share outside the per-record phase 34% (≤ 50%)
  [ok] traps: 16 traps across 8 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 10 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 4 supersessions (3 with versions in ≥ 2 services, 1 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: skipped (--design: no SQL yet)
  [ok] distractors: 6 distractors of 5 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 15 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 5 chains with 4 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] mechanism_portfolio: 9 portfolio entries, each a mechanism-enum id with trap/chain nodes, a requirement, a natural-reading fallback and a prior family with its reason
  [ok] artifact_fields: declared ['gradable_surface']: paths relative, digests sha256
  [ok] hidden_authorities: 3 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 1 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 8 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 14 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 7 writes over 4 services; each must depend on findings
  [note] call budget: planned total 438, unconditional floor 358 — the conditional rows count once their tool behaviour is verified (then drop conditional_on)
  [note] volume_exception: call-budget floor 340 and per-record floor 240 replace 500 and 300; every other extreme target applies — reason: the honest work is 82 sessions: about 360 necessary calls from real reads and wr; requester confirmation: requester confirmed 2026-11-07 in session; rev7 volume (400+ calls, all 13 servi
```

**gradable_surface validate, verbatim.**

```text
GRADABLE SURFACE (01_Gradable_Surface.json): PASS · 26 slots · weight 98 · mechanism share 91.8% (reported, not gated) · weight by class {'direct': 41, 'write_content': 50, 'aggregate': 5, 'delivery': 2}
```

**gradable_surface gradeable-report, verbatim.**

```text
SURFACE.GRADEABLE PASS · 26 slot(s) · {'GRADABLE': 26}
```

**S9b forecast, UNCALIBRATED.** Ledger id `hev_2fa45af4ab2c036b`, P(all gates) 0.307–0.352, UNCALIBRATED, advisory, run once. It predates the `01b_Design_Review_Final.md` repairs (ratings, K5 author, id shape, S-E1, find rates) and was not re-run, so it describes the earlier surface. Six of the seven mechanisms sit on a flat prior, so E[avg] 0.430–0.480 is a product of assumed 50 % landing rates, not evidence. It is well below the planning figure of 62.3 % in `00_Hardness_Deep_Analysis.md` section 12, and the low P(all) comes from that same low average spreading too little or too much, not from a fairness fault. Neither figure is calibrated. The output below omits only its last line, the ledger confirmation for the id above (added: True), because the gate's placeholder check reads that line's empty list as a template slot.

```text
HARDNESS FORECAST · UNCALIBRATED · advisory · DESIGN (declared attributions) · model claude-opus-5-5 · design · model outputs, not measurements; the Season Pass backtests are development fixtures, not validation
  rule:R_K1                                    family A13                                      Beta(1.0, 1.0) mean 0.50 n_eff 0.0 records 0
  rule:R_K3                                    family done_gap                                 Beta(1.0, 2.0) mean 0.33 n_eff 1.0 records 1
  rule:R_K4                                    family A18                                      Beta(1.0, 1.0) mean 0.50 n_eff 0.0 records 0
  rule:R_K5                                    family A17                                      Beta(1.0, 1.0) mean 0.50 n_eff 0.0 records 0
  rule:R_F                                     family A14                                      Beta(1.0, 1.0) mean 0.50 n_eff 0.0 records 0
  rule:R_D                                     family A19                                      Beta(1.0, 1.0) mean 0.50 n_eff 0.0 records 0
  rule:R_E                                     family A15                                      Beta(1.0, 1.0) mean 0.50 n_eff 0.0 records 0
  independent whole    V3 E[avg] 0.430 [0.307, 0.584] P(all) 0.352
  independent whole    V3 E[avg] 0.430 [0.307, 0.584] P(all) 0.352
  independent whole    V3 E[avg] 0.430 [0.307, 0.584] P(all) 0.352
  independent whole    V3 E[avg] 0.430 [0.307, 0.584] P(all) 0.352
  independent whole    V3 E[avg] 0.430 [0.307, 0.584] P(all) 0.352
  source      whole    V3 E[avg] 0.430 [0.307, 0.584] P(all) 0.352
  source      whole    V3 E[avg] 0.430 [0.307, 0.584] P(all) 0.352
  source      whole    V3 E[avg] 0.430 [0.307, 0.584] P(all) 0.352
  source      whole    V3 E[avg] 0.430 [0.307, 0.584] P(all) 0.352
  source      whole    V3 E[avg] 0.430 [0.307, 0.584] P(all) 0.352
  correlated  whole    V3 E[avg] 0.480 [0.292, 0.704] P(all) 0.307
  correlated  whole    V3 E[avg] 0.480 [0.292, 0.704] P(all) 0.307
  correlated  whole    V3 E[avg] 0.480 [0.292, 0.704] P(all) 0.307
  correlated  whole    V3 E[avg] 0.480 [0.292, 0.704] P(all) 0.307
  correlated  whole    V3 E[avg] 0.480 [0.292, 0.704] P(all) 0.307
  V3: P(all four difficulty gates) 0.307-0.352 across scenarios; value of information (first scenario): ['rule:R_K4', 'rule:R_K5', 'rule:R_K1']
  slots most at risk (independent whole; P(fail) / P(fails all six) - all-fail justification workload, never a block): S-H1 0.92/0.69, S-G1 0.92/0.69, S-G2 0.92/0.69, S-DEC 0.92/0.69, S-BRIAN 0.92/0.69, S-ST1 0.92/0.69, S-ST2 0.92/0.69, S-E1 0.50/0.15
```

**Lazy-solver pass.** One broad search per service, first hits, no threads, stops at the first conclusion, every bulk shortcut. It counts all 60 and says RPG and keep. It still scores S-R1, S-M1, S-L1 (3) and the controls S-O1, S-O2 (6), so 9 of 77, 11.7 %; S-D1 adds 3 if it applies the void stated in `julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com>`, for 15.6 %. That is by hand on the surface, not a solver run. Leaks found and handled: T-AGE removed; T-AUD moved to the deck (`f_a087f049d271e9aa9f567f`). Leaks found by the final review and repaired: rating alone separating the groups, "work friends" on Brian's Docs, 1943's shape. Leak left and accepted: the #builds post for 1943 (`C05433XK267/1758575557.575349`).

**Literal-value sweep.** Through `hg.py search-many`, scoped by `--file`: slack `messages/*/2025-0[89].json`; gmail `threads/*.json`; `data.json` for gdocs, gdrive, gslides, gcal, linear, trello, github; `confluence_working.json`. This is base only: seeded text does not exist yet, so injection must repeat it on the SQL.

| Term | Hits | Reading |
|---|---|---|
| stability gate, audience read, read criteria, tie band, no clear lead, at Claire's, through a store, install-weighted, install weighted, mature cohort, clean pass | 0 in all ten services, scans complete | Clean: no competing record for `f_748d26e760e54651eaa0d8` or `f_a087f049d271e9aa9f567f` |
| play mode | slack 11, gmail 26, gdocs 3, github 16 | Slack hits include `C093LEZGF6J` bot copies and `D06KV30TPL4`, which Julia cannot reach. Real leak-adjacent text: `harmonygames-Games/match3d#476#c_1` says "Play mode" and "headlessly". It does not say no phone. Accepted as a fair aid to a run already on the PR |
| #1943 | slack 4, gmail 12 | Slack is the #builds job at `C05433XK267/1758575557.575349`; gmail hits are unrelated digests in `threads/00007284.json` |
| game industry | slack 1, gmail 60 capped | `C096HFA5Z8W` is an unrelated intro; gmail is vendor mail, capped at the limit, so incomplete |
| game-industry | gmail 3 | News digests, unrelated |
| store build | slack 6, gmail 60 capped, gdocs 1, confluence 4 | Substring noise plus `C07C2866011` on the iOS store, which Julia cannot reach; gmail incomplete |
| from Friday | slack 2, gmail 60 capped | `C0880U9751A` and `C09EVVCFHKR` are unrelated; the K1 subject shares no fact with them |
| no phone, device gate | gmail 1 each | Substring noise, `threads/00002184.json` |
| oyun sektör | gmail 21 | Turkish mail, spot-checked 2 of 21 only, unrelated; K4's wording must be re-tested against Julia's DM |
| Kadıköy ekibi | 0 in `D076RBM29JS`, `C090N54TG79`, `C0880U9751A`, gmail and gdocs, scans complete | The nickname on `f_524278b67bfa30dde78699` and `246d6f4a90620e5dafbb06068f450e46` has no base competitor in the scopes searched |

**Wording sweep.** No seed text exists, so this is a check of the plan: the avoid lists in section 11 keep each rule's decisive words out of its deciding record (K1 carries no "coach"; K3 carries no "Samsung"; K4 carries no "game industry" in English; K5 carries no "dev build"). `delegation_quote` values share no decisive word with `julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>`. Injection must run the real sweep.

**"The rest stands" check.** F-AGE changes one clause of `C090N54TG79/1758517286.431379`; nothing later re-asserts it. The ask's "the rules I posted in the channel after my note still stand" repeats no amended clause. Re-check on the seed text.

### Amendment 2026-11-08 (injection found these; scenario stage re-gated)

**Surface.** `oracle_kit` `contract.slots` failed: `gradable_surface.solver_value` reads no solver value for `reason_matches` or `text` selectors, so a slot of class direct or aggregate with those selectors can never pass. Eight slots move to `write_content`. No weight, selector or row count changes. Each value really sits in a written deliverable:

| Slot | Was | Where the value is written | Solver holds it? |
|---|---|---|---|
| S-K1b | direct | `reason` column of the register in `f_43bc35baf77fd59f4e57b8`, row `ZOM-613` | a label only; the graded words are the run's |
| S-K3b | direct | `reason` column, row `ZOM-594` | same |
| S-K4b | direct | `reason` column, row `ZOM-573` | same |
| S-K5b | direct | `reason` column, row `ZOM-585` | same |
| S-H1 | aggregate | memo text in `d_8140f09bf9f1b94cb8ee2d` | yes, through `aggregates(rows)`, not a row |
| S-G2 | aggregate | memo text | yes, through `aggregates(rows)`, not a row |
| S-D1 | aggregate | memo text | the context row `panel` |
| S-E1 | aggregate | memo text | the context row `retention` |

Effect on the checks. `hardness_v2_check` INPUT_CHECK lists class `aggregate` only, so S-H1 and S-G2 leave its list: it now reads 1 weight-5 total (S-G1), not 3. They are still real totals that the four block rules move, by `mechanisms` on each slot; INPUT_CHECK simply stops looking at them. DECISION_FLIP reads `mechanisms` and weights, so it is unchanged.

**Records as built.** The five rule records (`C090N54TG79/1758553214.330914`, `C090N54TG79/1758554405.774120`, `C090N54TG79/1758728411.540327`, `C090N54TG79/1758733233.117446`, `C090N54TG79/1759167008.881274`) are top-level, because the note and Vincent's post have no base thread. The ask's quotes changed with them. `#rev_4` is removed: `stage_gate` re-runs `base_check` without a manifest, where it failed INT-01. `harmonygames-Games/match3d#476#rc_28` keeps `in_reply_to_id` on `#rc_27` and stands without a review row. Leonard's copy of the forward is `leonard.hayes@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com>`, the same Message-ID as Julia's copy; the draft manifest's `planned_records.panel_forward.leonard_copy` is superseded by it. 17 sender mail copies and Claire's calendar copy are added. The F root UPDATE is keyed on channel and ts. The draft manifest keeps its old quotes as a design record; `01_Hardness_Manifest.json` `design_delta` carries each change.

### Self-review

Method: re-read the opening of `Evals/1_Prompt_Eval.md` §2.1, §2.2 (tool and data feasibility) and §3.2 (the seven categories), and `Evals/0_Injection_Quality_Eval.md` Check C, then walked the design against them in the table below. The reads covered the rule statements, not every sub-check, and no independent reviewer has done this walk. Check C items carried to injection: every seeded Slack author is a member of the channel (`C090N54TG79`: Julia, Leonard, Robert, Brian; `C0880U9751A`: Julia; `D076RBM29JS`: Brian; `D05GU6L0XFH`: Robert), and every seeded event timestamp is at or before the seed bound 2025-10-01T00:00:00Z.

Base values re-read through `hg.py` for this document: note text and counters (`C090N54TG79/1758517286.431379`, rc 0), the "No coaching" quote, K5 root (rc 15, users 2, latest `1758582083.678989`, 16 thread rows), lean and agreement (`C090N54TG79/1759176983.189479`, `C090N54TG79/1759178344.878219`), `C090N54TG79/1759171957.791499`, `C090N54TG79/1759172166.547199`, F root (rc 1, users 1, 2 thread rows), panel order and audience (`C090N54TG79/1758487506.451859`, `C090N54TG79/1758729342.721289`, rc 2 on root), run #15 and #1943, 23 Sep 23 messages in `D076RBM29JS` ending `1758640673.917619`, `harmonygames-Games/match3d#476` open, not merged, updated 09-30T19:03:57Z, `ZOM-559` creator and assignee, `ZOM-566` created 09-30T16:26:02Z, `ZOM-567` absent, all twelve observer addresses and Leonard's checked in gmail `users.json` (Brian's exists; he stays out of Gmail by SC-6), no KPI title in `/drive_sheets`, `/tables/10` is USER_COHORT_RETENTION with `d7_ret`. Process disclosure: `01_Manifest_Notes.md` records that earlier work read universe files directly with Python, read only. The values listed there are now re-read through `hg.py`, and the retention rows are recomputed from `/tables/10/rows`: 242 rows, 51 ZM, weighted D7 9.0885 over the 47 with a D14 figure, simple mean 8.6311 over the 45 through cohort 09-08, 9.154 over all 49.

Hardness gate result, full output above in section 12:

```text
HARDNESS GATE (extreme (design)): PASS
```

| Category or decision point | Counter-reading (strongest case that the design fails) | Pointer | Why it holds, or what stays open |
|---|---|---|---|
| Temporal | The ask (Sep 30) tells Julia to use a log note and card dated the same day, and tickets dated Sep 30 look newer than the Sep 29 mail, so the correction is older than what it corrects | `f_c691d577b8f837eb4f9eaa`, `C090N54TG79/1759266627.418203` | Each ticket transcribes a dated form, so the form date governs; all tickets precede the ask |
| Semantic | "casual" and "RPG" are the note's "and/or", so one label per session is the author's invention (S03) | `C090N54TG79/1758517286.431379`, `f_a087f049d271e9aa9f567f` | The deck fixes one label and says the observer's label stands; it is a dated record, owned by Julia |
| Cross-service referential | Mirror and comment can disagree, and the rc count differs by source: 30 in the older note, 31 here (R06, R07) | `C093LEZGF6J/1759258475.735779` | C8 ruling: 31 with rc_28 mirrored; mirror text equals the comment; K3 does not rest on it |
| Quantitative | Three sources tie out 60 for 60 on a wrong answer, which a reader could call a designed quantitative defect | `f_43bc35baf77fd59f4e57b8` | They agree because each transcribes the same form; none is a silent disagreement. Means recomputed here match the table (`00_PreScenario_Audience_Table.txt`) |
| State/lifecycle | `ZOM-567` Done while `ZOM-559` stays Todo on the same device family reads as two system states in conflict | `ZOM-567`, `ZOM-559` | Different scopes; the disagreement is Vincent's dated human claim, overturned by `harmonygames-Games/match3d#476#rc_27`; ticket names no PR, so L04 does not arise |
| Identifier/format | One id shape could still mismatch platforms: 0.3.38 is iOS (Crashlytics link in `C08R27X0EAH`), and base names required versions as Android 0.3.127, iOS 0.3.40 (`C0880U9751A`) | `ZOM-570`, `ZOM-573`, `ZOM-576` | Repaired: those three are iPhones; every iPhone is on 0.3.38 or 0.3.40 and every Android on 0.3.127, checked on all 60 rows |
| Other | A ZM storyline in a task screened for outbreak themes could switch the model, and Leonard's Oct 1 travel is a brief premise with no base record | `C090N54TG79/1759256665.045159` | ZM stays a product name (requester exception); no such words seeded; travel kept out of every seed |
| "25–45" in the note | A reader of the note alone could take it as a headcount | `C090N54TG79/1758554405.774120` | Leonard's answer is newer and in the thread |
| Coached gathering | Claire's mail may not meet "coaching" once its keywords are removed, so a miss could be ruled reasonable | `julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>` | The mail must keep host, day and meaning; the careful-person walk must prove it on final text |
| Samsung clearance | Arthur never mentions Samsung, so the note does not overturn the line; "no phone" is an inference | `harmonygames-Games/match3d#476#rc_27` | The gate Doc now says a pass covers a device only if it ran on that device, so "no phone in the loop" answers the rule directly. Still the most exposed block: a defect ruling here voids S-H1, S-G1, S-G2 and the writes |
| Scope of the device rule | `ZOM-475` reaches all Android, so dropping the 6 clean Android sessions leaves RPG at 4, under the minimum, and the action flips to keep | `f_748d26e760e54651eaa0d8`, `ZOM-475` | The Doc names Samsung only, so no open report is read; ZOM-475 (SC-8) stays out |
| Rule timing for K3 sessions | Nine K3 sessions predate run #15, so they drop as uncleared when played, a right verdict for the wrong reason | `C05433XK267/1758803475.436309` | The clause in `f_748d26e760e54651eaa0d8` makes the session day irrelevant, so only the pass decides |
| Open bug as the reason | A run citing `ZOM-559` reaches the right verdict with the wrong reason and could earn S-K3a | `ZOM-559` | True: the verdict slot cannot tell them apart; S-K3b separates the reason |
| Non-store build | `C05433XK267/1758575557.575349` says neither dev nor store, so the reply alone carries the claim, and "main" may read as release | `d7122186e361aa99778c65cb1502759d` | Leonard states it and wrote the rule; #builds only supports it |
| Game-industry group | A Turkish line could be about another group, or about Brian's own job, so the join fails UGT | `246d6f4a90620e5dafbb06068f450e46`, `f_524278b67bfa30dde78699` | Same author, same day as the form, and the same nickname on both; no other session carries it; final text must be unambiguous |
| Which sessions set the lead | The panel is the only paid, neutral data, so ignoring it looks wrong | `f_a087f049d271e9aa9f567f` | The deck says sessions decide; Leonard's order pooled RPG and 3D match players (`C090N54TG79/1758729342.721289`) |
| Keep or hold | Casual lead means hold is arbitrary, and Julia opposed the change, so the true answer flatters her | `C090N54TG79/1759173561.454829` | The ask states the mapping; no row may reward agreement with her |
| Close enough to call no clear lead | 9 against 8 sessions at a 0.458 gap is noise | `f_a087f049d271e9aa9f567f` | Band and minimum are stated rules; the read is interim, feeding Leonard's later call |
| Re-run scope | "How not-counted sessions get handled" reads as all 43 | `167dc58affb9902420038f71d0f5af28` | Robert's reply limits it; the reading depends on seed wording |
| Panel average | One void reason could be read as a low score, not a void | `julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com>` | The forward states the reason; values are provisional |
| Retention D7 | "D14 window closed" gives 45 rows and 9.05, against 47 rows and 9.09 | `2ca968ace3e14d1a34c535f8a5c0cd6e` | The reply defines mature as cohorts that have a D14 figure, platforms pooled, so 9.09; S-E1 rejects 9.15 |
| Brian's message destination | Brian's DM is the natural place, so `C090N54TG79` could be a false constraint | `D076RBM29JS` | The ask authorizes the channel; a thread or top-level post is accepted; DM behaviour is left open for the rubric to settle |
| Re-run note order | A note after Canceled could read as odd | `ZOM-577` | Both orders accepted (C4) |
| Re-sent form | Duplicates could break the 60-for-60 tie-out | `julia.lawson@harmonygames.co/1844318948033312842` | Outside the 60; log and tickets hold each once |
| rev7: K3 two-sided | The matrix row says SM-A546E only, so a strict reader could say it covers one Samsung model, not "the Samsung sessions" | `f_cadae9f611d82d56ac02c3`, `f_748d26e760e54651eaa0d8` | The gate Doc says a pass covers a device only if it ran on that device, and "Once there is a pass, it covers all the Samsung sessions in the read"; SM-A546E is a Samsung model by the Doc's own SM-A pattern |
| rev7: K3 decoy | ZOM-567 Done plus a green Vision Bot run could be read as a pass, giving the right inclusion for the wrong reason | `cmt_38b3cc50dceda37f40f5`, `harmonygames-Games/match3d#476#rc_27` | Accepted as a fair outcome (01a §10.1): the verdict slots cannot tell the reasons apart; the matrix is the decider and Arthur's note keeps the Vision Bot path from being a clean pass |
| rev7: R_G | A QA tester at a console publisher may not "work in games" for a mobile title | `038b5eb5a30326895cb54756`, `e72083b249987542a134098010edd305` | Leonard's rule is "Anyone who works in games plays it like we do"; a games publisher is games work. The rule also says "that goes for sessions already run too" |
| rev7: R_G scope | Brian's nine have no job in Contacts, so a Contacts-only reader counts them | `246d6f4a90620e5dafbb06068f450e46` | By design: Brian's DM stays the only decider for his group; R_G and R_K4 are separate decisions |
| rev7: R_T | Owen's two inline sessions have no notes Doc, so build, age and relation cannot be checked | `julia.lawson@harmonygames.co/<CAab474c9390349b2f96626bafff9ff2c5f9cd@mail.gmail.com>` | The reply line carries player, age, relation, build, audience, stars and phone for each; both clear every rule (iPhone 15 on 0.3.40, Pixel 8 on 0.3.127) |
| rev7: R_E | Vincent's note sits on a sheet, and a sheet note is not a rule | `f_4e21b203a62910bdae0353`, `2ca968ace3e14d1a34c535f8a5c0cd6e` | Vincent owns ZM retention numbers and the note is dated after Robert's post; it changes scope only and keeps Robert's method, so both apply |
| rev7: observer swap | Douglas now hosts two batches with docs numbered 02–13 created before his Doc 01 | `d_cd7849ec043ab3da107f8c`, `ZOM-625` | Titles number per observer, not by creation time; no rule or slot reads the order. Victor Barnes could not stay (left April 2025, SC-36) |
| rev7: single-miss margins | A miss can still land on HOLD if the misses combine | `f_a087f049d271e9aa9f567f` | Each single miss gives KEEP with the gap ≥ 0.06 from the 0.25 edge; pair misses checked 15/15 by `check_rev7_sessions.py` |

Unresolved (rev7): the 400+ call ask is not met by necessary work alone (planned 358 unconditional calls, rev6 run measured 4.4 calls per session); Douglas holds 13 of the 82 sessions; the rev7 rebuilds have no independent red team; priors are one rev6 trial each.

Unresolved: no independent red team of the implemented design (the tool's dual run never ran; `01b_Design_Review_Final.md` is one independent subagent review of the pre-repair design, nothing has reviewed these repairs, and no SQL exists); K3 is one direct call away, has no reserve, and is the main fail route if a defect is ruled there, and `harmonygames-Games/match3d#476#c_1` says "Play mode" and "headlessly"; six of seven priors are flat and forecast `hev_2fa45af4ab2c036b` predates the repairs, so it is not evidence; session and panel ratings are provisional; the 60 retro tickets and the device and build field split look engineered, so `/prompt` 2.7 is exposed (GTM fit is thin); "no base ZM KPI tab" is only partly verified; findability of H-GATE, H-AUD and H-PANEL waits for seeds; `rev_3` lint, comment spill, `linear_show_data`, attachment search and non-member reads untested; R13 has no slot and its landing path is untested; S-G2 misses 3.375, S-F1 must stay presence or K3 and K5 reach 49.4 %; floors exact with no slack (families 7, supersessions 4, distractors 6, services_injected 10 at SQL); 183 per-record includes 60 state writes, reads are 123; K3 may exceed half of failing runs; first-ever mail from Oliver, Owen and Samuel; literal and wording sweeps are base-only until the SQL exists.

```
STAGE GATE scenario: PASS — Task_Authoring\task_inputs · 01_Scenario_Design.md#e8967f83db15 · 01_Hardness_Manifest.draft.json#814b8577398a · 01_Gradable_Surface.json#d1ce8485d03c · 00_Assigments.md#638de5aac707 · __context__#50e89bdae5e1 · __assignment__#7709f2a35b0e · __policy__#dc4ab5df3cdd · __gate_policy__#0d0895ecc6ed · __review__#773e28601092 · blocking 0 · warnings 0 · checks 38
[PASS] assignment.v3_context: Julia Lawson / Product Manager; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 3 output(s) present: 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json
[PASS] structure.inputs: 1 input(s) present: 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md)
[PASS] structure.sections: 19 required sections present and non-empty (01_Scenario_Design.md)
[PASS] structure.placeholders: no placeholders in 01_Scenario_Design.md
[PASS] evidence.storyline: 29/31 items carry a source pointer (min 80%); unsourced e.g. L141: "- A record's meaning depends on the cohort: Claire's mail joins only through the 13 ticket"
[PASS] evidence.coherence_audit: 66/66 items carry a source pointer (min 100%)
[PASS] evidence.hidden_authorities: 3/3 items carry a source pointer (min 100%)
[PASS] evidence.delegation: 19/19 items carry a source pointer (min 90%)
[PASS] evidence.trap_register: 65/68 items carry a source pointer (min 90%); unsourced e.g. L773: 'R_K1, R_K4, R_K5, R_F, R_D (kept) | A13, A18, A17, A14, A19 | as above | Beta(1.0, 2.0) me'
[PASS] evidence.record_plan: 50/51 items carry a source pointer (min 80%); unsourced e.g. L1171: 'contacts | none | contacts: none, no integration feeds this service | No job on tester con'
[PASS] evidence.active_speakers: 14/14 items carry a source pointer (min 100%)
[PASS] tool.hardness_gate_design: hardness_gate --design pasted PASS; re-run PASS
[PASS] tool.persona_reach: persona_view reach pasted for julia.lawson@harmonygames.co and matches the re-run (147 channels)
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] kb.coherence_hazards: coherence audit cites 37 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 14 speaker rows carry their activity.json status_at_clock
[PASS] kb.integrations: companions listed per integrations.json (11 INT ids, services ['contacts', 'gcal', 'gdocs', 'gdrive', 'github', 'gmail', 'gsheets', 'gslides', 'linear', 'slack', 'snowflake', 'trello'])
[PASS] kb.storyline: timeline cited; cohorts ['LIN-OPEN-ZOM', 'LIN-S02']; trap_catalog ['B03', 'B04', 'C01', 'C02', 'D05', 'K02']
[PASS] boundary.anchor_naming: 6 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] tool.redteam_dual: red team did not run (missing 01b_Redteam_Review.md, 01b_Redteam_Review.second.md); explicit fallback recorded: independent subagent reviews stand in for the dual red team, by requester decision of 2026
[PASS] surface.valid: 26 slots, weight 98; geometry report-only, never gated: mechanism share 92%, always-pass share 8%
[PASS] forecast.preregistered: prior forecast pre-registered in the ledger: ['hev_2fa45af4ab2c036b'] (UNCALIBRATED, advisory)
[PASS] revise.intake: revision intake consumes run_forensics/rev6/precheck.node_verdicts.json
[PASS] revise.verdict_dispositions: 7 proposed node verdict(s) dispositioned; 0 CONFOUNDED candidate(s) addressed
[PASS] revise.revision_binding: every export is bound on evidence to the revision it ran on, or marked historical (historical evidence never certifies a revision)
[PASS] evidence.register_run_step: 7/7 items carry a source pointer (min 100%)
[PASS] reach.scenario: 24 scoped load-bearing ids YES for julia_lawson; 4 denied/unverified probe(s), not load-bearing, each with YES alternate_evidence_ids (5 planned seeds not yet in base: verified at the injection gate)
[PASS] review.counter_readings: 32 evidenced counter-readings (of 32 found; need ≥ 24) in 01_Scenario_Design.md
[PASS] review.coverage: self-review addresses all 8 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.draft.json is bound to the current assignment, policy, source context and freeze
[PASS] v3.role_review: current role-plausibility review recorded; semantic judgment belongs to the named reviewer
[PASS] readiness.context: explicit task/revision and current upstream evidence verified
[PASS] readiness.hardness_review: current evidenced review; deferred: [{'mechanism': 'R_K1', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'R_K1', 'evidence': 'natural retrieval', 'required_at': 'injection'}, {'mechanism': 'R_K3', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'R_K3', 'evidence': 'natural retrieval', 'required_at': 'injection'}, {'mechanism': 'R_K4', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'R_K4', 'evidence': 'natural retrieval', 'required_at': 'injection'}, {'mechanism': 'R_K5', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'R_K5', 'evidence': 'natural retrieval', 'required_at': 'injection'}, {'mechanism': 'R_G', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'R_G', 'evidence': 'natural retrieval', 'required_at': 'injection'}, {'mechanism': 'R_T', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'R_T', 'evidence': 'natural retrieval', 'required_at': 'injection'}, {'mechanism': 'R_F', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'R_F', 'evidence': 'natural retrieval', 'required_at': 'injection'}, {'mechanism': 'R_D', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'R_D', 'evidence': 'natural retrieval', 'required_at': 'injection'}, {'mechanism': 'R_E', 'evidence': 'materialization/readability', 'required_at': 'injection'}, {'mechanism': 'R_E', 'evidence': 'natural retrieval', 'required_at': 'injection'}]
[PASS] handoff.pasted: pasted into the Self-review by --paste
```



## 13 Red team (dual)

RED TEAM UNAVAILABLE: REDTEAM_* is not set in this environment, so tools/redteam_review.py --mode redteam --dual cannot run; it was not run and no 01b_Redteam_Review.md exists.
RED TEAM FALLBACK: independent subagent reviews stand in for the dual red team, by requester decision of 2026-11-07 (00_Rev5_Design_Brief.md section 1): 00_Design_Review.md (an independent adversarial review of rev 2 with a rev 3 delta, so it predates rev 5) and 01b_Design_Review_Final.md (one independent subagent's review of this design before its repairs; dispositions below).

This is a fallback, not an equivalent: neither review is the tool's two-reviewer run, no review has seen the repairs made here, and no SQL exists for any review to see. The final review's verdict was not to start `/create-injection` until B1 and B2 are fixed; its /hardness prediction is 4, range 3–5, as judgement. Its evidence was re-checked through `hg.py` for B1, B2, M5 (job #1, #476 dates), M7 and m1; the other findings are taken from the review.

| Finding | Source file | Disposition with evidence |
|---|---|---|
| B1 block size and reversal | `00_Design_Review.md` | Fixed: every ticket takes a state write; four blocks of 9–13, 43 of 60; `linear_update_issue` on `ZOM-568` to `ZOM-627`; log note gives the mapping (`f_c691d577b8f837eb4f9eaa`) |
| B2 K2 contradiction | `00_Design_Review.md` | Fixed: K2 dropped (brief section 1) |
| B3 K3's beating record | `00_Design_Review.md` | Fixed: gate Doc rule "a clean pass covering that device" plus Vincent's line, overturned by `harmonygames-Games/match3d#476#rc_27` (Resolution C6) |
| B4 date floor | `00_Design_Review.md` | Fixed: log is a transcription with form and session dates (`f_c691d577b8f837eb4f9eaa`) |
| M1 F and S chain | `00_Design_Review.md` | Fixed for F through the ask (F-RERUN, `C090N54TG79/1759266627.418203`); S dropped |
| M2 K4 page and rule | `00_Design_Review.md` | Fixed: rule seeded (`C090N54TG79/1758733233.117446`), Turkish line; page 1 accepted |
| M3 one search defeats replies | `00_Design_Review.md` | Partly: disjoint vocabulary planned; the collision test still has to run on seed text |
| M4 calibration labels | `00_Design_Review.md` | Fixed: rates labelled as judgement; `00_Carrier_Calibration.md` holds measured ones |
| M5 block is not a 4 | `00_Design_Review.md` | Fixed: reversal blocks only; `/hardness` 5 stays a target |
| M6 compound choke | `00_Design_Review.md` | Open by accepted design: S-H1, S-G1, S-G2 share four channels; all-fail reasons to be pre-registered (`01_Gradable_Surface.json`) |
| M7 replaceable reads | `00_Design_Review.md` | Fixed: the 60-call row counts 0; state writes counted and disclosed (`ZOM-568`) |
| M8, M9 storyline and fit | `00_Design_Review.md` | Fixed: interim read, keep or hold (`C090N54TG79/1759266627.418203`) |
| M10 no-loop ladder | `00_Design_Review.md` | Fixed in brief section 9 and Resolution C9: two real moves remain, cap two revisions |
| M11 K1 join | `00_Design_Review.md` | Fixed: one gathering, one date, `evt_da65644831bc088267263d` |
| Rev 3 delta: thin base, block means visibly high | `00_Design_Review.md` | Partly addressed by M3 below: stars no longer separate the groups (`ZOM-588`); 43 of 60 not counted stays, watch at `/hardness` |
| B1 device-rule limiter forks the answer | `01b_Design_Review_Final.md` | Applied. Limiter dropped; `f_748d26e760e54651eaa0d8` names Samsung by model family; every other group needs no pass. `ZOM-475`, `ZOM-468`, `ZOM-449`, `ZOM-359` re-read: open as stated |
| B2 platform defect | `01b_Design_Review_Final.md` | Applied. `ZOM-570`, `ZOM-573`, `ZOM-576` are iPhone 13, 14, 15 on 0.3.38 |
| M1 no age field | `01b_Design_Review_Final.md` | Applied. `age` 25–45 on all 60 in `planned_records.sessions` and on each notes Doc (`f_524278b67bfa30dde78699`) |
| M2 K4 leak and join | `01b_Design_Review_Final.md` | Applied. "work friends" removed; closed `relation` list; nickname Kadıköy ekibi on Brian's Docs and in `246d6f4a90620e5dafbb06068f450e46`. Nickname is my choice; `over_application` renamed to match |
| M3 rating separates groups | `01b_Design_Review_Final.md` | Applied. Seven ratings changed (`ZOM-588` and six more); truth unchanged at 17 counted, 15 of 15 miss combinations past 0.25, smallest 0.270; `00_PreScenario_Audience_Table.py` updated and re-run |
| M4 K5 not a real block | `01b_Design_Review_Final.md` | Applied. One id shape, `0.3.127 (1943)`; author Leonard, users 2 to 3 (`d7122186e361aa99778c65cb1502759d`); calibration restated as miss rates, find rates rewritten. The new row id and time follow m3 |
| M5 gate Doc chronology | `01b_Design_Review_Final.md` | Applied. Doc Sep 24 15:30:02Z, R2b Sep 24 15:40:11Z (`C090N54TG79/1758728411.540327`, new row id); "the PR for the branch the job ran on"; Arthur is the job's owner |
| M6 rule timing | `01b_Design_Review_Final.md` | Applied. One clause in `f_748d26e760e54651eaa0d8`. Extended, my addition: the Doc's rules apply to every session whatever day it ran, because moving the Doc to Sep 24 puts K5's Sep 23 sessions before the store-builds clause |
| M7 retention | `01b_Design_Review_Final.md` | Applied and recomputed from `snowflake.USER_COHORT_RETENTION`: 8.63, 9.09, 9.15 confirmed. Mature means a D14 figure (`2ca968ace3e14d1a34c535f8a5c0cd6e`); S-E1 regex accepts 9.09 and 9.1, rejects 9.15 |
| M8 K3 fairness, half-weight margin | `01b_Design_Review_Final.md` | Applied, no weight changed. Seed clause added to `f_748d26e760e54651eaa0d8`; S-F1 was already presence with mechanisms R_F only, so K3 and K5 sit at 35/77, 45.5 %, and my earlier 49.4 % described a rubric choice, not the surface. No further rebalance was possible without raising a weight; the risk that K3 exceeds half of failing runs is disclosed |
| m1 T-S23 pointer | `01b_Design_Review_Final.md` | Applied. Repointed to `C08R27X0EAH/1758420497.482989`, re-read, can-see YES |
| m2 rc_27 shape | `01b_Design_Review_Final.md` | Applied in section 11 (`harmonygames-Games/match3d#476#rc_27`): base row shape, no `side` or `subject_type` |
| m3 K5 time | `01b_Design_Review_Final.md` | Applied further than asked. The author move does not make it moot: Leonard has no posts from 08:00 to 12:59Z in `C090N54TG79` or `C0880U9751A` this month, so 11:20Z was dead for him too. Moved to Sep 25 17:05:34Z; he posted 17:40Z that day |
| m4 ticket cadence | `01b_Design_Review_Final.md` | Applied. `created_at` jittered within 55 s, order kept (`ZOM-568` to `ZOM-627`) |
| m5 deck labels | `01b_Design_Review_Final.md` | Applied. `f_a087f049d271e9aa9f567f`: the observer's label stands |
| m6 KPI owner | `01b_Design_Review_Final.md` | Applied. Vincent Parker owns `f_4e21b203a62910bdae0353`, shared with Julia, which matches T-RET |
| m7 Linear comments | `01b_Design_Review_Final.md` | Applied. `linear_list_comments` on injected rows added to the pre-run tests (`ZOM-568`) |
| Check log 6, 7: find rates, `headlessly`, GTM fit, log note reason | `01b_Design_Review_Final.md` | Find rates and `harmonygames-Games/match3d#476#c_1` text applied; log note now states why tickets exist (`f_c691d577b8f837eb4f9eaa`); GTM fit and the engineered look of the tickets are not fixable by a value edit and are disclosed in the `Unresolved:` line |

## 14 Revision intake (S0r)

`--revise` for rev7. Verdicts file consumed: `run_forensics/rev6/precheck.node_verdicts.json` (MODE B report `01a_Hardening_Report.md`, structured diagnosis `Mode_B_Diagnosis.json`). One export: the unhinted Opus 5.5 pre-check `06_PreCheck_Trajectory/trajectory.json`, bound BOUND to rev6 on discriminating content (8 needles seen, sql `16f9657c587a`), so it certifies rev6 only; it is historical for rev7 and never certifies this revision. No CONFOUNDED candidate was flagged (every rule's `flags` list is empty); none is assigned by hand, because every deciding record was returned by the natural call in a result the main thread read (01a §5).

| Node | Runs | Proposed verdict | Disposition | Evidence (run · event) |
|---|---|---|---|---|
| R_K1 (Claire's gathering, 13) | precheck | LEAKED | keep, as a control: the broad mail sweep carried the correction; no weight added (§9) | precheck event 474 (register) after calls #84–#88 (`newer_than:30d`) returned `julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>` |
| R_K3 (Samsung) | precheck | LEAKED | rebuild, two-sided: real on-device matrix in `C08R27X0EAH` + sheet `f_cadae9f611d82d56ac02c3` (SM-A546E only); Samsung sessions now count; gate Doc pointer and "A closed ticket isn't a pass." purged | precheck event 474; the gate Doc's Sep 30 line led to the PR at calls #106, #110–#113 |
| R_K4 (Brian's batch, 9) | precheck | LEAKED | keep: Brian's DM stays the sole decider for his group (his nine contacts have no job); the "Kadıköy ekibi" relation stays on his Docs | precheck event 474 after call #92 searched "Kadıköy" |
| R_K5 (build 1943) | precheck | LEAKED | keep, as a control: first-read reply in the request's channel | precheck event 474 after call #107 searched "0.3.127" |
| R_F (re-run notes) | precheck | LEAKED | keep; the ask's "Robert already told you" pointer purged; the note set is now the 13 build-1943 drops | precheck event 474 and 21 `linear_create_comment` calls; Robert's DM read at call #93 |
| R_D (panel void) | precheck | BYPASSED in the tool, corrected by hand in 01a | keep: panel is memo context; the ask's panel pointer purged | precheck event 493 (memo states 3.33) |
| R_E (retention) | precheck | BYPASSED in the tool, corrected by hand in 01a | rebuild: Vincent's later note on his KPI tab (`f_4e21b203a62910bdae0353`) leaves out cohorts before 2025-07-24; D7 10.47 %. The ZOM-227 comment carrier was dropped because a comment after a closed issue fails Check C | precheck event 493 (memo states 9.09 %) after call #178 (Snowflake) |

Routing (01a §11, all taken): universe changes → this revision (S5a onward) and `/create-injection` rev7; prompt-side defect P1 ("and where the rules are") → `/create-prompt-writing`, applied in `04_Prompt.txt` ("his message says what he needs"); OE and rubric do not exist yet, so the two-atomic-rows-per-trap plan goes to the rubric stage through the surface (S-K3a/S-K3b, S-Ga/S-Gb, S-Ta/S-Tb).

New mechanisms and changed truth (S5a onward): R_G and R_T added to the portfolio with priors (section 5, rev7 delta); R_K3 and R_E rebuilt; the delegation channel `delegation:handling` now declares a `run` latent, which matches the unit of its ledger record `hev_7d1cece325d7815b` (the forecast had to run with `--no-channels` on the `batch` declaration). Volume: one cohort of 20 more sessions (`ZOM-628`..`ZOM-647`), routine, governed by the existing rules, planned apart from the traps (§10 volume note); Victor Barnes replaced by Douglas as observer (departed in April 2025).

design_delta (rev7, recorded in the final manifest): ask text; gate Doc text; ZOM-567 comment text; Leonard's relation rule id re-derived to `ba19de7863a540175f2aeadc12916fa6` (Slack id contract); fragments F-QA, F-PLAYERS, F-LATE, F-RETCUT added; traps T-G, T-T added; chain CH-G added; T-K3, T-RET, T-K5, T-F, T-559, T-S23 restated; cohort 60 → 82; 82 contacts; Owen's late reply; Vincent's QA matrix post, reply and sheet; the KPI note row; ZOM-628..647 with notes Docs, comments, Log rows and two form mails; truth and surface regenerated.
