# Scenario Design — dd-q4-claims-register · design only · contains no prompt, OE or criterion text

## 0 Assignment, persona census and horizon note

**Assignment (V3, copied from `00_Task_Context.json`; not changed).**

| Field | Value |
|---|---|
| Business function | Product |
| Persona | Julia Lawson, Product Manager |
| Persona key / e-mail / department | `julia_lawson` · julia.lawson@harmonygames.co · Product |
| Competency | Product Management |
| Task skill | Retrieval |
| Task type / horizon | normal · Normal Horizon |
| Difficulty mode / cap | hard · corrected weighted average strictly below 0.70 |
| Universe date / freeze | October 1, 2025 07:00 · 2025-10-01T00:00:00Z |
| Effective profile | `normal` (no `profile_exception`; the design budget is 67 unconditional calls, inside the Normal 60–100 band) |
| Design target | E[average] ≤ 0.62 (Hard target; cap minus 8 points) |

**Persona reach census (verbatim from `python3 Task_Authoring/tools/persona_view.py reach julia_lawson --top 10`).**

```
REACH  Julia Lawson <julia.lawson@harmonygames.co>  Product Manager / Product
clock 2025-10-01

SLACK  user=EMPLOYEE_0005_SLACK_ID  visible channels=158 {'mpim': 52, 'public': 26, 'private': 53, 'im': 27}  messages=267537  public-not-member (UNVERIFIED)=44
  persona posts=34047 last post=2026-02-12  last activity in visible channels=2026-02-13
  C05433XK267    builds                                 public  mem=31  msgs=41107  2023-04-20..2026-02-12
  C1CB3D58E38B    game-design                            private mem=27  msgs=22751  2023-07-16..2025-10-06 archived
  C050WGU41HR    engineering-bots                       private mem=35  msgs=20306  2023-03-29..2026-02-11
  C05V5FNLB9V    god-bugs                               private mem=31  msgs=16889  2023-10-07..2026-02-11
  C0880U9751A    zombie-match3d                         private mem=25  msgs=16773  2025-01-09..2026-02-11
  D076RBM29JS    D076RBM29JS                            im      mem=5   msgs=12287  2024-06-06..2026-01-28
  C09UHHN6PFZ    prototype                              private mem=18  msgs=12172  2025-11-24..2026-02-12
  D05GU6L0XFH    D05GU6L0XFH                            im      mem=5   msgs=10717  2023-07-16..2026-01-27
  CC43664F351E   mpdm-julia.lawson--brian.foster--vince mpim    mem=4   msgs=10170  2024-06-26..2025-11-21
  D05QA585LTY    D05QA585LTY                            im      mem=5   msgs=6756   2023-09-21..2025-11-10

GMAIL  mailbox=julia.lawson@harmonygames.co threads=304 messages=359 range=2023-07-16..2026-02-13
  threads by last-message month (recent): {'2025-09': 1, '2025-10': 1, '2025-11': 1, '2025-12': 6, '2026-01': 25, '2026-02': 18}
  top correspondents: leonard.hayes@harmonygames.co (105), robert@harmonygames.co (100), arthur.blake@harmonygames.co (61), claire.morgan@harmonygames.co (44), victor.barnes@harmonygames.co (43), calvin.price@harmonygames.co (38), martin.walsh@harmonygames.co (37), [EMAIL_0072] (36), SVC_1295_EMAIL (32), marcus@harmonygames.co (30)

GCAL  own=['julia.lawson@harmonygames.co'] shared=[] events=792 (distinct ical_uid 261, cancelled 50)
  last event before clock=2025-09-29T16:30:00Z  next after clock=2025-10-06T16:00:00Z
  by month: 2023-07:14 2023-08:50 2023-09:24 2023-10:35 2023-11:26 2023-12:24 2024-01:45 2024-02:22 2024-03:9 2024-04:21 2024-05:24 2024-06:39 2024-07:34 2024-08:35 2024-09:40 2024-10:27 2024-11:32 2024-12:32 2025-01:46 2025-02:18 2025-03:11 2025-04:23 2025-05:42 2025-06:31 2025-07:27 2025-08:9 2025-09:9 2025-10:25 2025-11:9 2025-12:6 2026-01:3

DRIVE  owned=45 {'application/vnd.google-apps.spreadsheet': 12, 'application/vnd.google-apps.document': 11, 'application/vnd.google-apps.presentation': 9, 'application/pdf': 9, 'folder': 3, 'application/json': 1}
  shared-with=169 {'application/vnd.google-apps.document': 52, 'text/plain': 38, 'application/vnd.google-apps.spreadsheet': 36, 'application/json': 21, 'application/pdf': 10, 'application/vnd.google-apps.presentation': 10, 'text/csv': 2}
  shared by owner: {'Resource: -6481757892984311338': 102, 'leonard.hayes@harmonygames.co': 37, 'robert@harmonygames.co': 17, 'arthur.blake@harmonygames.co': 10, 'Resource: 7240535625619857401': 3}
  native visible: {'gdocs': 63, 'gsheets': 48, 'gslides': 19}  last modified visible=2026-01-12T17:47:18Z
  UNVERIFIED (domain/anyone, not owned/shared)=117 {'application/vnd.google-apps.document': 45, 'application/vnd.google-apps.spreadsheet': 31, 'application/pdf': 17, 'application/vnd.google-apps.presentation': 13, 'application/json': 11}

UNSCOPED (always visible): contacts, github, trello, linear, snowflake, confluence

LAST ACTIVITY (days before clock): slack_persona_post=2026-02-12 (-134d), slack_visible_channels=2026-02-13 (-135d), gmail=2026-02-13 (-135d), gcal_last_event_before_clock=2025-09-29 (2d), drive_last_modified_visible=2026-01-12 (-103d)
```

**Remit argument (Product Management + Retrieval).** Julia authors `page_economy_design` (Confluence, v3 dated 2025-09-21) and owns the Domino Delights progression/economy design, the puzzle-layout pipeline and the FTUE requirements (`Task_Authoring/references/Persona_Briefs.md:61`). A product manager owning the external product story is a normal part of that remit: before a board product page or a publisher conversation, the PM certifies every claim against what is actually live. The work is retrieval first (locate each claim's production evidence) and product judgment second (classify status, apply the wording rule, apply the title scope). It is not a finance, incident or engineering-ops task.

**Theme screen.** Domino Delights is a domino puzzle game. This design contains no bio-adjacent theme (no infection, outbreak, contamination or zombie framing in the storyline or seeded text). The out-of-scope claim is an internal-tooling claim, chosen specifically so the scope trap is an audience boundary rather than a title boundary.

## 1 Storyline

**Situation at the clock.** On 30 September 2025 the Q4 pack is being assembled: the October board product page is due before the 14 October board, and publisher conversations open at the end of October. Leonard asks Julia to certify the product claims before anything external is written. Julia has a draft claims list of thirteen numbered lines about Domino Delights. Several of those lines read as live because the ticket is Done or the PR is merged; two are not live, one is only in testing, one is internal tooling rather than a player-facing product claim, and three carry wrong numbers or dates. The certification must be built from production evidence, not from the draft's own summary.

**Storyline beats and anchors by service.**

| Service | Anchor record | What it carries | Date |
|---|---|---|---|
| slack | `C1CB3D58E38B` (#dd-product-leads) | leadership mpim (Leonard, Julia, Brian) where the claims note and the correction thread live; Julia is a member | channel live; seed messages 2025-09-30 |
| gdrive | `f_5a1b2c3d4e5f60718293a4` (planned) | Julia's Q4 claims draft: 13 numbered claims plus an unnumbered note | 2025-09-30 |
| gdocs | `f_c57724584820a26f3bbe54` | DD Global Launch Readiness: P0 "Instead of Season Pass show the $0.99 Starter Pack"; "Global Release Date: April 23th" | 2025-05-05 |
| linear | `ENG-2136`, `ENG-2323`, `ENG-1874`, `ENG-2065`, `ENG-1385`, `ENG-1871`, `ENG-645` | feature work-of-record and the per-claim production config facts | 2024-03-06..2025-05-13 |
| github | `harmonygames-Games/GameOfDominoes#1755`, `#1557`, `#1794`, `#1838`, `#1563`, `#1781`, `#503` | merged code, branches and per-claim review facts | 2024-04-10..2025-05-08 |
| snowflake | `snowflake.LIVE_EVENT_PERFORMANCE` | completed Domino Delights runs through 2025-09-30 (`EVT-0513`, `EVT-0515`, `EVT-0529`, `EVT-0531`, `EVT-0532`, `EVT-0533`) | run starts 2025-09-22..2025-09-30 |
| snowflake | `snowflake.IAP_TRANSACTIONS` | Domino Delights SKUs actually sold: `dd_coins_small`, `dd_coins_medium`, `dd_coins_large`, `dd_coins_mega`, `dd_starter_pack`, `dd_remove_ads` | through 2025-09-30 |
| snowflake | `snowflake.INSTALL_EVENTS` | comment: "the US soft launch 2025-04-11 … the earliest install date for this title is not its launch date" | static comment, table through 2026 |
| confluence | `page_domino_gdd` | v4 2025-09-15: internal codename GoD, US soft launch 11 April 2025, worldwide 6 May 2025, about 4,755 levels across 160 chapters | 2025-09-15 |
| confluence | `page_live_ops_engine` | v1 2025-08-01: the live-ops event engine is internal scheduling tooling, not a player-facing surface | 2025-08-01 |
| trello | `67ec1f6021f4291d45f9c21e` | Collectibles card in the October list, last activity 2025-05-27, no build | 2025-05-27 |
| confluence | `page_economy_design` | Julia's economy page, v3 2025-09-21, evidence of her product ownership | 2025-09-21 |

**Timeline placement (`Task_Authoring/references/universe_kb/timeline.md`).** The design sits on the 2025-09-29 Collect & Win event beat and the 2025-09-30 vision-bot beat; the next relevant beats are the 2025-10-18 fundraising-status row and the 2025-10-19 Telegram port. The October board pack (a 14 October 2025 deck exists in the base as `f_d03044b385b94f24b21ff4`, created 2025-10-10) and the late-October publisher outreach are future deadlines, allowed by the freeze rule. Nothing relied on is dated after 2025-10-01T00:00:00Z.

**Cohort source.** `cohorts.json` has no fit for a claims set: the nearest service cohort is `SL-T26` (#dd-product-leads, 113 thread roots), but it does not define the claims and is not used as the spine. The cohort is source-defined by the numbered lines of the claims draft (section 2).

**trap_catalog precedents (`Task_Authoring/references/universe_kb/trap_catalog.json`).** `D05` (version markers in Drive titles) supports the draft v1/v2 lookalike; `C01`/`C02` (thread replies that correct or retract) support the correction reply; `C04` (documented human claim vs record contradiction) supports the Season Pass overturn; `D07` (Trello stale against Linear) supports the Collectibles card; `N01`/`N02` (ticket and PR number collisions) support the identifier discipline; `D04` (spreadsheet near-duplicates) supports the old register tab.

## 1a Coherence audit

Scope walked against `Task_Authoring/references/universe_kb/coherence_hazards.json`: the claims draft `gdrive:f_5a1b2c3d4e5f60718293a4` and its v1 `gdrive:f_5a1b2c3d4e5f60718293a5`, the register workbook `gsheets:f_6b2c3d4e5f60718293a4b5` and its old tab, all 13 claims, their tickets (`linear:ENG-2136`), PRs (`github:harmonygames-Games/GameOfDominoes#1755`) and comments, the three authorities and their decoys, the readiness doc `gdocs:f_c57724584820a26f3bbe54`, the event/SKU/install tables, the correction thread `slack:C1CB3D58E38B/1759255200.000200`, the claims-review event `gcal:evt_5c1a7e93b2d04f61a8e7`, and the pages the run opens. Seven QC categories, each row dispositioned.

| Record | Category | Fields | Evidence pointer | Hazard id | Disposition |
|---|---|---|---|---|---|
| DD Global Launch Readiness | temporal | "Global Release Date: April 23th" vs the US soft launch 2025-04-11 in `INSTALL_EVENTS` | `gdocs:f_c57724584820a26f3bbe54`; `snowflake.INSTALL_EVENTS` | T04 check: no ticket/PR pair in scope is out of order | Fold into design: claim C13 asks for the launch date; the scope note fixes the governing date; the register reports the three dated values instead of silently choosing |
| `ENG-2136` vs `harmonygames-Games/GameOfDominoes#1755` vs readiness doc | state/lifecycle | ticket Done 2025-05-05; PR merged 2025-03-29; readiness P0 removes the pass from the out-of-moves screen while saying the fix is in develop | `linear:ENG-2136`; `github:harmonygames-Games/GameOfDominoes#1755`; `gdocs:f_c57724584820a26f3bbe54` | L04 check: the PR is merged, so not the L04 predicate | Designed claim + overturning record: the readiness P0 is a scoped instruction (2025-05-05), and the seeded production-config comment (2025-09-28) is the later, decisive record that the pass stayed default-off with no SKU and no run |
| Confluence pages in scope | semantic | overlapping "release status" and "external messaging" pages; the decoy pages deliberately near-match the authorities | `confluence:page_release_status_definitions`; `confluence:page_external_messaging_guide`; `confluence:page_q4_product_narrative` | S08 (overlapping pages: page-level, not a field contradiction) | Fold into design: the decoys are same-purpose pages of another scope (team=Engineering); the authority wins on issuer and scope, not on a label |
| Slack links in the seeded thread | cross-service referential | seeded Slack text carries no Google-native links, so R04 cannot occur | `slack:C1CB3D58E38B/1759248600.000100` | R04 avoided | Avoid: no Drive links in seeded Slack text; records are named by role |
| Seed threads | quantitative | reply counters must equal the exported replies; `latest_reply` must equal the newest reply ts | `slack:C1CB3D58E38B/1759248600.000100` | Q01–Q04 avoided | Fold into design: seed `reply_count=1`, `reply_users_count=1`, `latest_reply=1759255200.000200` on the parent |
| Julia's mailbox threads | identifier/format | Gmail thread file uses the `jlawson@` alias while `user_email` is `julia.lawson@` | `gmail:julia.lawson@harmonygames.co/1860000000000000001` | I03 | Known base convention: the alias is the mailbox filename, not a second identity; the scope thread uses the Julia mailbox |
| Claims draft vs v1 | other | two Drive docs with the same title family | `gdrive:f_5a1b2c3d4e5f60718293a4`; `gdrive:f_5a1b2c3d4e5f60718293a5` | D05 | Fold into design: v1 is the stale 9-claim draft; v2 (2025-09-30) is current; the register cites v2 only |

**Sibling-defect sweep.** For each designed defect the base was searched for other records of the same kind in the same scope. (a) "Done but not live": `ENG-2136` is the only Domino Delights feature in this scope whose flag is off at the freeze; `ENG-1874`, `ENG-2065`, `ENG-2323`, `ENG-645` all have completed production surfaces. (b) "Merged without human review": the in-scope PRs `#1557` and `#1755` carry human approvals, so no in-scope sign-off defect displaces the designed Season Pass case. (c) "Stale card in a live list": `67ec1f6021f4291d45f9c21e` is the only October-list card with no ticket and no activity since May; the other October cards (`68c44cf45171b65e64221c01`, `68c453cd0ff184d95550bc58`) have September activity. (d) "Wrong count": the four coin SKUs and the starter pack are the complete sold set in `IAP_TRANSACTIONS`; there is no fifth coin SKU. Each base defect is either in the design as a designed claim with a resolver, or outside the scope.

## 1b Active speakers

Every person the design gives a voice to is referenced by a dated record before 2025-10-01, so the activity view is a reference record rather than a departure inference; the status column is the literal `status_at_clock` the stage context supplies for this freeze (`activity_record_verification_required`) and the dated activity evidence is in the service reads (for example Julia's 2025-09-24 post at `C090N54TG79/1758689839.300009` and Leonard's 2025-09-30 note at `C1CB3D58E38B/1759248600.000100`).

| Person | E-mail | status_at_clock | Seeding role |
|---|---|---|---|
| Julia Lawson | julia.lawson@harmonygames.co | activity_record_verification_required | persona; author of the claims draft and the register |
| Leonard Hayes | leonard.hayes@harmonygames.co | activity_record_verification_required | request owner; the 30 September note; invitation mail |
| Brian Foster | brian.foster@harmonygames.co | activity_record_verification_required | commerce owner; Season Pass and shop config facts |
| Arthur Blake | arthur.blake@harmonygames.co | activity_record_verification_required | merged the Season Pass PR; claims-review attendee |
| Owen Baker | owen.baker@harmonygames.co | activity_record_verification_required | event and shop engineering facts |
| Calvin Price | calvin.price@harmonygames.co | activity_record_verification_required | Collectibles parked decision |
| Samuel Turner | samuel.turner@harmonygames.co | activity_record_verification_required | level manifest owner |
| Martin Walsh | martin.walsh@harmonygames.co | activity_record_verification_required | decoy wording card author |
| Claire Morgan | claire.morgan@harmonygames.co | activity_record_verification_required | publication claims reviewer |

No seeded voice is given to Victor Barnes (`quiet_since_2025-04`), Douglas (`quiet_since_2025-12` is active at the clock but is not needed), or any person with no October activity.

## 1c Identity traps

`python3 Task_Authoring/tools/entity.py resolve "Julia Lawson"` (verbatim first lines) plus the collision classes that matter for this design:

```
ENTITY email:julia.lawson@harmonygames.co  name=Julia Lawson  kind=person  emails=['julia.lawson@harmonygames.co']
  persona: julia_lawson - Product Manager / Product
  slack      id=EMPLOYEE_0005_SLACK_ID, name=Julia Lawson, real_name=Julia Lawson, email=julia.lawson@harmonygames.co, is_bot=False, deleted=False
  gmail      mailbox=julia.lawson@harmonygames.co, threads=304 messages=359, thread_filename_alias=['jlawson@harmonygames.co']
  gcal       calendar_id=julia.lawson@harmonygames.co, owner_email=julia.lawson@harmonygames.co, events=792
  linear     id=usr_8140f09bf9f1b94c, email=julia.lawson@harmonygames.co
  github     login=PERSON_0005_GITHUB_USERNAME, name=Julia Lawson, email=julia.lawson@harmonygames.co
  trello     id=793af7ca6940bf18eb516c75, username=julia.lawson, fullName=Julia Lawson
  confluence id=user_EMPLOYEE_0005, email=julia.lawson@harmonygames.co, last_activity=2025-09-21
```

```
SHARED_FIRST_NAMES (4)
  claire: ['Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]', 'Claire <github:PERSON_2360_GITHUB_USERNAME>']
  marcus: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Marcus Lee <marcus.lee@harmonygames.co>', 'Marcus <marcus@harmonygames.co>', 'Marcus <github:PERSON_0396_GITHUB_USERNAME>']
  martin: ['Martin Lewis <PERSON_0394_EMAIL>', 'Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]']
  thomas: ['Thomas Baker <thomas.baker@harmonygames.co>', 'Thomas <thomas@harmonygames.co> [persona thomas]']
SHARED_LAST_NAMES (5)
  lawson: ['Julia Lawson <julia.lawson@harmonygames.co> [persona julia_lawson]', 'Peter Lawson <peter.lawson@harmonygames.co>']
  bennett: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Oscar Bennett <oscar.bennett@harmonygames.co>']
LOOKALIKE_HANDLES_AND_ALIASES (15)
  Gmail thread files of julia.lawson@harmonygames.co are named 'jlawson@harmonygames.co_*'
```

Pins: the persona is the `julia.lawson@` person, not Peter Lawson (`peter.lawson@`); the mailbox alias `jlawson@` is her export filename (`gmail:julia.lawson@harmonygames.co/1860000000000000001`), not a second person; "Martin" in the decoy wording card is Martin Walsh (`martin.walsh@harmonygames.co`), not Martin Lewis; "Claire" is Claire Morgan (`claire.morgan@harmonygames.co`). No claim names a person by first name only.

## 2 Cohort spine

**Definition rule (reconstructable, not a list).** The cohort is every **numbered claim line** in the current Q4 claims draft (`gdrive:f_5a1b2c3d4e5f60718293a4`, v2, modified 2025-09-30T15:40:00Z): a line that starts with a claim number in the `Cnn` form and states a product claim about Domino Delights. Unnumbered notes, bullets under a numbered line, the "Next steps" list, and the v1 draft are excluded. Applying the rule yields **13 claims** (`C01`–`C13`), the cohort key. The draft's unnumbered final note ("remember to mention the internal-tooling appendix") is not a claim and is a boundary record.

**Cohort composition.** 13 claims: 9 live claims covering ten features (six event features across five claims, ads, shop bundles, levels and the launch), 1 feature in a staged rollout, 2 features with no production surface, 1 internal-tooling claim, and 1 launch-date claim. Status is decided per claim by H1; the decision is decided by H2. The claim set is: C01 Weekly Quests; C02 Weekly Leaderboards; C03 Win & Collect; C04 River Rush; C05 Axe Arena and Streak Fever; C06 Domino Delights Season Pass; C07 Collectibles; C08 ad monetization and remove-ads IAP; C09 shop coin bundles; C10 Hero Offers rotation; C11 the live-ops event engine; C12 the level count; C13 the launch date. The unnumbered note about the internal-tooling appendix is a boundary record, not a claim, and is excluded by the numbered-line rule.

**Claim set, expected status and decision.**

| Claim | Statement | Status | Decision | Qualifier | Deciding evidence |
|---|---|---|---|---|---|
| C01 | Weekly Quests run every week | LIVE | KEEP | none | `snowflake.EVT-0513` completed 2025-09-28; `linear:ENG-645` comment |
| C02 | Weekly Leaderboards are automated | LIVE | KEEP | none | `snowflake.EVT-0515` completed 2025-09-28; `linear:ENG-1874` comment |
| C03 | Win & Collect runs every day | LIVE | QUALIFY | runs Mon/Wed/Fri, not daily | `snowflake.EVT-0529`; `linear:ENG-1385` comment |
| C04 | River Rush is live | LIVE | KEEP | none | `snowflake.EVT-0531`; `linear:ENG-2065` comment |
| C05 | Axe Arena and Streak Fever are live | LIVE | KEEP | none | `snowflake.EVT-0532`, `snowflake.EVT-0533`; `linear:ENG-2368` comment |
| C06 | Domino Delights Season Pass is live | NOT_LIVE | DROP | flag off; replaced by the starter pack on the out-of-moves screen | `linear:ENG-2136` comment; `github:harmonygames-Games/GameOfDominoes#1755`; `gdocs:f_c57724584820a26f3bbe54`; no DD run or SKU |
| C07 | Collectibles ship in October | NOT_LIVE | DROP | no build slot this quarter | `trello:67ec1f6021f4291d45f9c21e`; `slack:C1CB3D58E38B/1759251600.000400` |
| C08 | Ad monetization and remove-ads IAP are live | LIVE | KEEP | none | `snowflake.IAP_TRANSACTIONS` dd_remove_ads; `snowflake.AD_REVENUE`; `linear:ENG-2367` comment |
| C09 | Five coin bundles and a starter pack are live | LIVE | QUALIFY | four coin bundles plus the starter pack | `snowflake.IAP_TRANSACTIONS`; `linear:ENG-2369` comment |
| C10 | Hero Offers rotate every 48 hours | TESTING | QUALIFY | in testing at a 10% cohort; the 48-hour rotation is the enabled behaviour | `linear:ENG-2323` comment; `github:harmonygames-Games/GameOfDominoes#1838` |
| C11 | The live-ops event engine is live | OUT_OF_SCOPE | DROP | internal tooling, not a player-facing claim | `confluence:page_live_ops_engine`; `linear:ENG-2372` comment |
| C12 | 5,000 handcrafted levels are live | LIVE | QUALIFY | 4,755 live; 245 planned | `confluence:page_domino_gdd`; `gsheets:f_7c3d4e5f60718293a4b5c6`; `linear:DES-313` comment |
| C13 | Domino Delights launched on 14 April 2025 | LIVE | QUALIFY | US soft launch 11 April; worldwide 6 May; 14 April unsupported | `confluence:page_domino_gdd`; `snowflake.INSTALL_EVENTS`; `gdocs:f_c57724584820a26f3bbe54` conflict |

Status counts: LIVE 9, TESTING 1, NOT_LIVE 2, OUT_OF_SCOPE 1. Decision counts: KEEP 5, QUALIFY 5, DROP 3.

**Evidence surfaces (2 surfaces, 11 and 8 records, 2 services).**

| Surface | Tool | Records | Per-record calls | Why the bulk call does not return it | Short-circuit analysis | Requirement | Decides |
|---|---|---|---|---|---|---|---|
| Linear comments | `linear_list_comments` | 11 | 2.0 | `linear_list_issues` returns identifier, title, state, labels and assignee but never comments; a comment is reachable only per issue | The comment carries the raw production-config fact (flag default, cohort, slot list, manifest count) that no event row or PR states; a run that skips it cannot distinguish "shipped" from "enabled" for C06/C10/C12 | R4 | evidence |
| GitHub PR conversation comments | `github_list_pr_comments` | 2 | 1.5 | `github_list_pull_requests` returns PR metadata and review state but not conversation comments; each PR's thread is a separate read | The thread carries the branch/flag fact (develop, not release; 10% cohort) that the issue state hides; only the two contested claims need it, and neither surface alone decides | R4 | evidence |

Σ per-record calls × records = 11×2.0 + 2×1.5 = 25; floor 25.

**Classification predicate (closed vocabulary).** Status is one of `LIVE`, `TESTING`, `NOT_LIVE`, `OUT_OF_SCOPE`. The predicate is exhaustive and applied per claim in this order: (1) a claim that is not player-facing (internal tooling) → `OUT_OF_SCOPE` under H3; (2) enabled for a positive subset of production players (a flag or cohort below 100%) → `TESTING`; (3) enabled for 100% of production players and either an active production config row or at least one completed production run/transaction → `LIVE`; (4) otherwise (zero enablement, or no production surface) → `NOT_LIVE`. Zero enablement is not a subset. The decision is one of `KEEP`, `QUALIFY`, `DROP` under H2.

**House rule that overrides the natural reading (A15).** H1: "a merged PR, a Linear Done, a store listing, or a design doc is not evidence of live." The natural reading of `ENG-2136` (Done) plus `#1755` (merged) is "Season Pass shipped"; H1 turns it into `NOT_LIVE` because the production flag is off and no Domino Delights run or SKU exists.

**Boundary records (A17).**  (a) The unnumbered note about the internal-tooling appendix at the end of the draft; (b) the two bullets under C10 that mention "48 hours" and "hero pool" but are not separate claims; (c) claim C13, the launch-date line, which is numbered but is not a feature; (d) the v1 draft with 9 claims, which is stale; (e) the "Old register" tab with 9 rows, which is stale and includes a live-ops engine row.

**Dual regime.** None: the task has one clock (2025-10-01T00:00:00Z) and one version of each rule. The only date rule is the launch-date rule in H3 (global release date, not soft launch), stated explicitly.

## 3 Hidden authorities

Three authorities, each named in plain words by the 30 September note, each homed in a rarely-opened service, each with a decoy in the service Opus opens first. No `governs` overlap.

| Authority | Home record | Decoy record | Governs | Findable query | Decoy scope |
|---|---|---|---|---|---|
| H1 the live-claim standard | `gcal:evt_5c1a7e93b2d04f61a8e7` | `confluence:page_release_status_definitions` | R1 | "Q4 product claims review" | team: decoy Engineering release tracking, task Product claims pack |
| H2 the external wording rules | `trello:68d672304f5e6d7a8b9c0d11` | `trello:68d6735c4f5e6d7a8b9c0d12` | R2 | "external wording" | team: decoy Engineering release wording, task Product claims |
| H3 the Q4 scope note | `gmail:julia.lawson@harmonygames.co/1860000000000000001` | `confluence:page_q4_product_narrative` | R3, R5 | "player-facing claims only" | team: decoy Engineering appendix, task Product pack |

**H1 — the live-claim standard.** Home: the calendar event "Q4 product claims review" on 2025-09-29 (`gcal:evt_5c1a7e93b2d04f61a8e7`), description: "Live-claim standard … a claim is live only if the feature is enabled for 100% of production players and either an active production config row or at least one completed production run/transaction exists for Domino Delights … A merged PR, a Linear Done, a store listing or a design doc is not evidence of live. Enabled for a positive subset is testing. Zero enablement with no production run is not live." Decoy: `confluence:page_release_status_definitions` ("Release Status Definitions", Engineering), which says a release is shipped when the PR is merged to main and deployed, and says nothing about flags or cohorts. Both pages are returned by a search for "release status"; the decoy differs on the decisive clause because it governs Engineering release tracking, not product claims (dimension team: decoy Engineering, task Product). Governs R1.

**H2 — the external wording rules.** Home: the Trello card `68d672304f5e6d7a8b9c0d11` "External wording — product claims" on the DD Product Roadmap board (`65eb4ec525346c8070ca638f`), description: "LIVE items may say live or available. TESTING items must say in testing and must not use live, available or launched. NOT_LIVE items are removed, not caveated. Numeric claims state the exact count in the register. Every retained claim names an owner." Decoy: `68d6735c4f5e6d7a8b9c0d12`, a card on the Harmony Games board titled "Engineering release wording", which says merged-and-deployed is shipped and allows "launched" for anything in testing. Same service, adjacent scope (dimension team: decoy Engineering release wording, task Product claims). Governs R2.

**H3 — the Q4 scope note.** Home: the Gmail thread `gmail:julia.lawson@harmonygames.co/1860000000000000001`, subject "Q4 pack — Domino Delights only", from Leonard to Julia, 2025-09-30T07:05:00Z: "This pack covers player-facing Domino Delights claims only; internal tooling claims go in the engineering appendix, even when they are live. For any launch-date line use the soft-launch and worldwide dates in the current GDD, not the April 14 date." Decoy: `confluence:page_q4_product_narrative`, which mixes the live-ops engine, the internal admin tools and the player-facing product into one Q4 story and says the launch date is "the April 14 date the team uses". Dimension team (decoy Engineering appendix, task Product pack). Governs R3 and R5.

**Findability proof.** Each home is named by role in the note (A1, `slack:C1CB3D58E38B/1759248600.000100`) and is reachable by a natural search for that role: "Q4 product claims review" (calendar), "external wording" (Trello), "Domino Delights only" (Gmail). The decoy pages use the same search terms and sound complete; they lose on issuer/scope, not on a self-advertising label.

## 4 Delegation lattice

**Anchors (1–2; noun phrases only).**

| Anchor | Name (noun phrase, ≤ 6 words) | Record | Requirement ids |
|---|---|---|---|
| A1 | Leonard's Q4 claims note | `slack:C1CB3D58E38B/1759248600.000100` (planned) | R7 |
| A2 | my Q4 claims draft | `gdrive:f_5a1b2c3d4e5f60718293a4` (planned) | R1, R4 |

**Hub (A1, Leonard's voice, 2025-09-30T16:10:00Z; `slack:C1CB3D58E38B/1759248600.000100`).** "Julia — before the Q4 pack goes out I need the product claims checked against what is actually live. Use the live-claim standard we agreed at the Q4 review and the external wording rules product signed off; the scope note I sent this morning fixes which title is in. The claims draft you started is the set. Post the corrected counts in this thread, drop the register in the tab we already use, and put anything we can't support on the claims review ticket. If a claim's sources disagree, write both and say which one governs — don't pick one silently."

The hub names what governs and delegates by role; it never gives a location, an id, a document title or a source list.

**Spokes (7 fragments over 7 services and 7 containers).**

| Fragment | Service | Container | Kind | Carries |
|---|---|---|---|---|
| K2 | slack | C1CB3D58E38B thread reply 1759255200.000200 | amendment | R1, R7 |
| K3 | gcal | evt_5c1a7e93b2d04f61a8e7 | requirement | R1 |
| K4 | gmail | julia.lawson@harmonygames.co/1860000000000000001 | requirement | R3, R5 |
| K5 | trello | 68d672304f5e6d7a8b9c0d11 | format | R2 |
| K6 | gsheets | f_6b2c3d4e5f60718293a4b5 (Register tab) | destination | R4, R6 |
| K7 | linear | ENG-2371 | delegation | R8 |
| K8 | confluence | page_q4_claims_conflict_format | format | R5 |

**Incorporation table (fragment → anchor → delegating record → verbatim quote).**

| Fragment | incorporated_via | delegated_by_record | Delegation quote | Requirement ids |
|---|---|---|---|---|
| K2 | A1 | slack:C1CB3D58E38B/1759248600.000100 | "Post the corrected counts in this thread" | R1, R7 |
| K3 | A1 | slack:C1CB3D58E38B/1759248600.000100 | "the live-claim standard we agreed at the Q4 review" | R1 |
| K4 | A1 | slack:C1CB3D58E38B/1759248600.000100 | "the scope note I sent this morning" | R3, R5 |
| K5 | A1 | slack:C1CB3D58E38B/1759248600.000100 | "the external wording rules product signed off" | R2 |
| K6 | A1 | slack:C1CB3D58E38B/1759248600.000100 | "drop the register in the tab we already use" | R4, R6 |
| K7 | A1 | slack:C1CB3D58E38B/1759248600.000100 | "put anything we can't support on the claims review ticket" | R8 |
| K8 | A1 | slack:C1CB3D58E38B/1759248600.000100 | "If a claim's sources disagree, write both and say which one governs" | R5 |

**Amendment.** K2 (Slack, 2025-09-30T18:00:00Z, Calvin): "Two corrections before you lock it: `dd_season_pass` is still default-off in the production config, and Collectibles has no build slot this quarter. The rest stands." It changes two claims' evidence and retains every other clause. The phrase "The rest stands" is the partial-amendment marker; no later record re-asserts C06 or C07 as live.

**Non-authoritative instruction distractors.** T9: Brian's message in `C1CB3D58E38B/1759249980.000300` — "while you're in there add the offer calendar to the pack" — is an instruction-shaped message with no authority over the claims register; ignoring it is correct. T12: the v1 claims draft is a document, not an instruction. The "Old register" tab (T10) is stale data, not a delegation.

**Wording check (`slack:C1CB3D58E38B/1759248600.000100`).** No record in the chain uses the register's expected values as a checklist. The claims draft states claims, not statuses; the authorities state rules, not per-claim answers; the per-claim comments state raw events (flag defaults, cohorts, slot lists, counts), never the classification.

## 5 Chains and trap register

### Independent chains

| Chain | root_cause | Hops (service · record · finding) | ends_in |
|---|---|---|---|
| C1 | A1 | slack · C1CB3D58E38B/1759248600.000100 · the draft's "all live" summary is met first; gdocs · f_c57724584820a26f3bbe54 · P0 says the Season Pass was replaced by the starter pack; linear · ENG-2136 comment · the production flag is off and no SKU exists; snowflake · LIVE_EVENT_PERFORMANCE · no Domino Delights Season Pass row | R1 |
| C2 | A15 | gcal · evt_5c1a7e93b2d04f61a8e7 · the standard requires 100% enablement plus a production surface; linear · ENG-2323 comment · `offer_rotation_v2` is at a 10% cohort; github · GameOfDominoes#1838 · the offers code is merged; snowflake · LIVE_EVENT_PERFORMANCE · no 48-hour rotation run | R1 |
| C3 | A12 | trello · 68d672304f5e6d7a8b9c0d11 · testing items must say "in testing"; confluence · page_external_messaging_guide · the decoy allows "live" for anything shipped this quarter; linear · ENG-2323 comment · the rotation is a 10% cohort; gsheets · Register tab · the qualifier is "in testing" | R2 |
| C4 | A7 | gmail · julia.lawson@harmonygames.co/1860000000000000001 · the pack covers player-facing claims only; confluence · page_live_ops_engine · the engine is internal scheduling tooling; linear · ENG-2372 · the engine has no player-facing surface; gsheets · Register tab · C11 is out of scope | R3 |
| C5 | A16 | gdrive · f_5a1b2c3d4e5f60718293a4 · C06 is written as live; gdocs · f_c57724584820a26f3bbe54 · the readiness doc says it was replaced; linear · ENG-2136 comment · the flag is off; gsheets · Register tab · the conflict column states both sources and the governing one | R5 |

Distinct root causes: A1, A15, A12, A7, A16. Each chain has ≥3 hops over ≥2 services and ends in a graded requirement.

### Trap register

| Trap | Family | Services | Records | Requirement | Expected wrong reading | Resolver | Discovery order |
|---|---|---|---|---|---|---|---|
| T1 | stale_summary | gdrive, gsheets | f_5a1b2c3d4e5f60718293a4 | R1 | The draft's opening line ("all 13 items are live in the current build") is repeated as the status set | H1 applied to each claim's production evidence | The draft is the first record the task opens |
| T2 | authority | gcal, confluence | evt_5c1a7e93b2d04f61a8e7; page_release_status_definitions | R1 | The Engineering "Release Status Definitions" page is used: merged and deployed means shipped, so C06 is live | H1's flag and production-surface clause | The Confluence page is the first search hit for "release status" |
| T3 | authority | trello, confluence | 68d672304f5e6d7a8b9c0d11; page_external_messaging_guide | R2 | The marketing guide is used: anything shipped this quarter can be called live, so C10 keeps "live" | H2's "in testing" rule | The marketing guide is in Confluence and is read before Trello |
| T4 | scope_alias | gmail, confluence, linear | julia.lawson@harmonygames.co/1860000000000000001; page_live_ops_engine; ENG-2372 | R3 | C11 is marked live because the engine runs | H3: the pack covers player-facing claims only | C11 is true but internal and looks live |
| T5 | superseding | github, gdocs, slack | GameOfDominoes#1755; f_c57724584820a26f3bbe54; C1CB3D58E38B/1759255200.000200 | R1 | C06 is live because the PR merged and the ticket is Done | The 2025-05-05 readiness P0 and the 2025-09-28 config comment overturn the merge | The PR and ticket are met before the readiness doc |
| T6 | superseding | trello, linear | 680222a04f5e6d7a8b9c0d13; ENG-2369 comment | R7 | The April "five coin bundles" card is copied into the register | The September SKU comment lists four coin bundles and the starter pack | The Trello card is found by "coin bundles" before the ticket |
| T7 | exact_predicate | snowflake | snowflake.LIVE_EVENT_PERFORMANCE | R7 | The number of event rows (60+ runs) is reported as the number of event features | The register counts six event features across five event claims, not runs | The table's row count is the first number seen |
| T8 | conclusion_stop | slack | C1CB3D58E38B/1759255200.000200 | R1 | The parent message is read and the thread is not opened; C06 and C07 stay live | The 18:00 reply corrects both | The parent is returned by the search; the reply is not |
| T9 | distractor | slack | C1CB3D58E38B/1759249980.000300 | R6 | Brian's offer-calendar request is added to the register or the pack | Ignore: no authority over claims | The message is in the same channel and arrives before the correction |
| T10 | distractor | gsheets | f_6b2c3d4e5f60718293a4b5 (Old register tab) | R6 | The old 9-row register is copied as the answer | Use the Register tab and the 13-claim set | The old tab has data and looks complete |
| T11 | distractor | gsheets, confluence | f_6b2c3d4e5f60718293a4b5; page_live_ops_engine | R3 | The old register's live-ops engine row is carried forward as in scope | H3 excludes internal tooling | The old tab looks like a shortcut |
| T12 | distractor | gdrive | f_5a1b2c3d4e5f60718293a5 | R4 | The 9-claim v1 draft is used as the cohort | The current v2 draft (2025-09-30) is the source | v1 is a near-duplicate title and is found by the same search |
| T13 | eliminating_evidence | trello, linear, slack | 67ec1f6021f4291d45f9c21e; C1CB3D58E38B/1759251600.000400 | R1 | C07 is live because the card exists | The card has no ticket, no PR and no config; the 2025-09-30 decision records no build slot | The card is in the October list |
| T14 | reuse_exclusion | gsheets | f_6b2c3d4e5f60718293a4b5 | R6 | A new workbook is created, or the Old register tab is overwritten | Update the existing Register tab | The workbook has two tabs and one looks empty |

**Supersession records.**

| Trap | version_records (oldest first) |
|---|---|
| T5 | `github` · `harmonygames-Games/GameOfDominoes#1755`, seeded false, at 2025-03-29T01:57:59Z · `gdocs` · `f_c57724584820a26f3bbe54`, seeded false, at 2025-05-05T15:42:14Z · `slack` · `C1CB3D58E38B/1759255200.000200`, seeded true, at 2025-09-30T18:00:00Z |
| T6 | `trello` · `680222a04f5e6d7a8b9c0d13`, seeded true, at 2025-04-18T10:00:00Z · `linear` · `ENG-2369` comment, seeded true, at 2025-09-26T13:20:00Z |

**Trap counts (`gsheets:f_6b2c3d4e5f60718293a4b5`; `linear:ENG-2136`).** 14 traps over 9 families, 7 distinct requirements, 2 supersessions (T5 cross-service and 3 versions), 4 distractor-family traps over 4 types (non_authoritative_instruction, stale_summary, scope_adjacent, near_duplicate_record), 3 discovery-order proofs (T1, T5, T8), and 3 rare-service traps (T2 gcal, T3 trello, T4 gmail).

### Mechanism portfolio (S5a)

| Rule id | Mechanism | Prior family | Prior records (per model) | Nodes | Requirement | Natural reading | Decides | Source | Signature |
|---|---|---|---|---|---|---|---|---|---|
| M1_status | A1 | wrong summary + thread past its conclusion (A1) | `hev_0e23d0e0b6b029a5` (Opus 5.5, 6 trials, mean 0.65); `gdrive:f_5a1b2c3d4e5f60718293a4` | T1, T5, C1 | R1 | trust the draft's "all live" summary | status | claims-draft | status-from-production-evidence |
| M2_flag | A15 | A15 | Opus 5.5: none; Opus 4.8 family A15 has 12 records, not pooled without a transfer record (Beta(1,1) fallback); `linear:ENG-2136` | T2, C2 | R1 | Done plus merged means live | status | live-standard | flag-and-cohort-overrides-done |
| M3_live_standard | A12 | A12 | Opus 5.5: none; Opus 4.8 family A12 record `hev_b5ebfc3b82bc4894` (not pooled); `gcal:evt_5c1a7e93b2d04f61a8e7` | T2 | R1 | use the first release-status page found | status | live-standard | find-the-q4-standard-not-the-engineering-page |
| M4_wording | A12 | A12 | Opus 5.5: none; Opus 4.8 family A12 record `hev_b5ebfc3b82bc4894` (not pooled); `trello:68d672304f5e6d7a8b9c0d11` | T3 | R2 | anything shipped may be called live | decision, qualifier | wording-rules | testing-must-say-in-testing |
| M5_scope | A7 | A7 | Opus 5.5: none; Opus 4.8 family A7 records `hev_a1293478aa959d92`, `hev_0b6f3eee30afcffc` (not pooled); `confluence:page_live_ops_engine` | T4, T11, C4 | R3 | a live feature is in scope | scope | scope-note | internal-tooling-is-out-of-scope |
| M6_conflict | A16 | A16 | Opus 5.5: none; Opus 4.8 family A16 record `hev_15d2cbdad732909e` (not pooled); `gdocs:f_c57724584820a26f3bbe54` | T5, C5 | R5 | pick the more recent of two sources silently | conflict | claims-draft | report-both-sources-and-the-governing-one |
| M7_counts | A19 | A19 | Opus 5.5: none; Opus 4.8 family A19 records `hev_bdca78a1902331c3`, `hev_23c914c6d59c0828` (not pooled); `snowflake.LIVE_EVENT_PERFORMANCE` | T6, T7, C1 | R7 | count rows or repeat card numbers | counts | claims-draft | count-features-and-exact-values |

Prior policy: priors are per model. Only M1 has an Opus 5.5 ledger record (`hev_0e23d0e0b6b029a5`); that record carries an uncertain model-provenance flag and an effective sample size of about 0.86 after weighting, so its 0.65 is a weak posterior mean, not a measured six-run mean. The other six families have Opus 4.8 evidence only, which is **not pooled**; the forecast therefore falls back to Beta(1,1) for those rules and labels them UNPARAMETERIZED with the exclusion reason, never zero. No transfer record is claimed and no forecast output is presented as calibration.

**Record anchors for the portfolio.**

- M1_status: `gdrive:f_5a1b2c3d4e5f60718293a4`
- M2_flag: `linear:ENG-2136`
- M3_live_standard: `gcal:evt_5c1a7e93b2d04f61a8e7`
- M4_wording: `trello:68d672304f5e6d7a8b9c0d11`
- M5_scope: `gmail:julia.lawson@harmonygames.co/1860000000000000001`
- M6_conflict: `gdocs:f_c57724584820a26f3bbe54`
- M7_counts: `snowflake.LIVE_EVENT_PERFORMANCE`

**A5b check per rule.** Incorporated: each rule's chain reaches A1 (section 4). Survives complete retrieval: M1/M2/M3 survive because the production flag and the warehouse absence remain after every record is read; M4 survives because the wording rule is a judgment on a live feature; M5 survives because the claim is true but internal; M6 survives because the two sources remain in conflict; M7 survives because the exact counts must still be derived. The register destination is a delivery requirement (R6), not a designed mechanism: it is graded by the workbook/tab check in the rubric, not counted in the mechanism share. Tool-surface proof: each decisive record is returned by a natural call (gcal list, Trello card read, Gmail thread read, Linear comment list, GitHub PR comment list, Snowflake query, Sheet read). Graded weight: each rule flips the slots named in section 12 and the surface file.

### Liveness flags (S5b)

`python3 Task_Authoring/tools/trap_liveness.py --design --task-dir Task_Authoring/task_inputs` reports eight `breadcrumb` flags and no `self-advertising` or `order` flags; `rule placement` is SKIP for every node except the A15 node T2 and is not raised there. The flags are lexical, advisory and uncalibrated. Every flag has a disposition; none is resolved by removing an incorporation link.

| Node | Flag | Disposition |
|---|---|---|
| T2 `gcal:evt_5c1a7e93b2d04f61a8e7` | breadcrumb | A1 names "the live-claim standard" by role, which is the incorporation the prompt requires; it does not name the calendar event, the page or the decisive flag clause. The agent still has to find the event and choose against the Confluence decoy; keep |
| T3 `trello:68d672304f5e6d7a8b9c0d11` | breadcrumb | A1 names "the external wording rules" by role; the clauses are only on the Trello card and the decoy is not linked; keep |
| T4 `confluence:page_live_ops_engine` | breadcrumb | A1 names "the scope note" by role; the player-facing-only clause is only in the Gmail thread and C11 is not linked to it; keep |
| T5 `github:harmonygames-Games/GameOfDominoes#1755` | breadcrumb | A1 names the claims draft and asks for the corrections in the thread; the readiness doc and the PR are not linked from the entry set. The correction reply is the amendment the hub asks for; it states two raw production/plan facts, not a classification; keep |
| T8 `slack:C1CB3D58E38B/1759255200.000200` | breadcrumb | same record as T5: the thread is a direct delegation, so the agent must open it; the reply states the correction but not the governing rule; keep |
| T10 `gsheets:f_6b2c3d4e5f60718293a4b5` | breadcrumb | A1 names "the tab we already use"; the Old register tab is not named and the Register tab is the intended reuse target; keep |
| T13 `trello:67ec1f6021f4291d45f9c21e` | breadcrumb | A1 names the claims draft, which contains C07; the Collectibles card and the parking decision are not linked; keep |
| T14 `gsheets:f_6b2c3d4e5f60718293a4b5` | breadcrumb | same destination as T10: the reuse target is named by role, not by tab; the Old register remains a live distractor; keep |

Rule placement: the A15 rule is T2's resolver (the flag and cohort clause). It is not stated in A1, K2 or any direct delegation; A1 names the standard, not its clause. No rule-placement flag fires, so no fix is required. Injection re-runs the tool on the SQL and dispositions every new flag in the same table.

## 6 Failure-diversity plan

The five chains form three independent discovery clusters. C1 and C5 are one cluster (the Season Pass finding, reached through the status chain and the conflict chain); C2 and C3 are one cluster (the Hero Offers finding, reached through the status and wording chains); C4 is the third (the player-facing scope and the internal-tooling claim). A run that finds H1 but not H2 gets the statuses right and the qualifiers wrong; a run that finds H2 but not H1 keeps C06 live but words C10 correctly; a run that finds both but misses H3 keeps C11 in the pack; a run that finds all three but trusts the count card gets the counts wrong; a run that reads the parent but not the reply may still recover C06 from the config comment, so T8 is a speed trap, not a gate on every requirement.

| Run type | Plausible misses | Requirements touched | Expected score shape |
|---|---|---|---|
| Strong retrieval, weak authority search | H1 and/or H2 | R1, R2, R5, R7 | Statuses partly wrong, qualifiers wrong, counts wrong; C01–C05 and C08 still right |
| Strong authority search, weak per-record reads | Linear/GitHub comments | R1, R4 | C06/C10/C12 wrong or unqualified; the rest right |
| Strong on features, weak on scope | H3 | R3, R7 | C11 wrong, counts off by one |
| Strong everywhere, weak on destination | Register tab / old tab | R6 | Content right, delivery wrong; only delivery weight lost |
| Strong everywhere, weak on conflict | R5 | R5 | One weight-5 row lost; the rest right |

No single discovery gates more than half the weight: the three authorities each govern a different subset, and the per-record facts split across Linear and GitHub. The design target is at least two failure patterns among six runs and a largest pattern at most 50% of failing runs.

## 7 Deliverables and dependent writes

| Deliverable | Shape | Destination | Depends on |
|---|---|---|---|
| D1 register | one row per claim with claim_id, claim, feature, scope, status, decision, qualifier, evidence, evidence_date, conflict, owner, action | the existing `Register` tab in `f_6b2c3d4e5f60718293a4b5` | M1, M2, M3, M4, M5, M6, M7 |
| D2 summary | tracker text with the status and decision counts | a message in `C1CB3D58E38B` | M1, M7 |
| D3 claims page | corrected status paragraph and the dropped-claim list | `page_q4_product_claims` | M1, M5, M6 |
| D4 follow-up ticket | one new Linear issue listing C06, C07 and C11 with their evidence, linked to the claims review ticket | a new ENG issue under `ENG-2371` | M1, M3 |

**Writes.** 4 writes over 4 services: `gsheets` update (the Register tab), `slack` post (the summary), `confluence` update (the claims page), `linear` create (the follow-up issue). Every write's content depends on findings; none is a bolt-on. The register is the only exact-total surface; the summary repeats the totals, so the two must agree.

## 8 Service role map

| Service | Role in this task | Load-bearing fact or write | Carrier |
|---|---|---|---|
| slack | hub, correction thread, summary destination | A1 note; K2 amendment; T9 distractor | ● per-record? no — the correction is a reply, not per-record volume; ● for the hub and amendment |
| gmail | scope authority (H3) | the "Domino Delights only" thread | ● authority |
| gcal | live-claim standard (H1) | the 2025-09-29 review event description | ● authority |
| gdrive | cohort source (A2) and stale v1 | the 13-claim draft; the 9-claim v1 | ● cohort source |
| gdocs | resolving record for C06 and C13 | the DD Global Launch Readiness P0 and global release date | ● base resolver |
| gsheets | register destination, level manifest, old tab | Register tab headers; 4,755/245 level rows; Old register | ● write target and per-claim count |
| linear | per-record production facts and the follow-up write | comments on ENG-645, ENG-1874, ENG-1385, ENG-2065, ENG-2136, ENG-2323, ENG-1871, ENG-2367, ENG-2368, ENG-2369, DES-313 | ● per-record |
| github | per-record merge/branch facts | comments on #1755, #1557, #1794, #1838, #842, #1563, #503, #1781 | ● per-record |
| trello | wording authority and Collectibles boundary | H2 card; decoy card; Collectibles card | ● authority and boundary |
| confluence | decoys, conflict format, claims page write | three decoy pages; K8; D3 | ● decoy and write |
| snowflake | event, SKU and install evidence | EVT-0513/0515/0529/0531/0532/0533; the six SKUs; the install comment | ● aggregate |
| contacts | not used | none | ○ |
| gslides | not used | none | ○ |

## 9 Call budget

| Phase | Service | Calls | Necessity reason |
|---|---|---|---|
| discovery | slack | 5 | find the note, the leadership mpim and the correction reply; read the parent and its thread |
| discovery | gdrive | 3 | open the current draft, check its modified date, reject the v1 near-duplicate |
| discovery | gmail | 2 | find and read the scope thread |
| discovery | gcal | 2 | find the 2025-09-29 review event and read its description |
| rules | confluence | 5 | read the three decoys, the conflict-format page and the claims page to be corrected |
| rules | trello | 3 | read the DD wording card, the same-service decoy and the Collectibles card |
| rules | gmail | 1 | re-read the scope note once for the player-facing and launch-date clauses |
| per-record | linear | 22 | 11 issues plus their comments (2 calls per claim), each carrying a distinct production fact |
| per-record | github | 3 | the two contested PR threads whose branch and flag state contradicts the ticket |
| structured | snowflake | 6 | one query per evidence family: event runs, event types, SKU set, ad revenue, install dates, and the empty Season Pass check |
| structured | gsheets | 4 | Register headers, Old register, level manifest active/disabled counts, summary totals |
| reconciliation | slack | 1 | reconcile the parent, the amendment and the draft's opening line in one read |
| reconciliation | gdocs | 2 | reconcile the readiness P0 with the Season Pass ticket and the launch date |
| writes | gsheets | 2 | write the 13 rows and read back the totals |
| writes | slack | 2 | post the summary and read it back |
| writes | confluence | 2 | update the claims page and read it back |
| writes | linear | 2 | create the follow-up issue and read it back |
| **Total** | **11 services** | **67** | **unconditional floor 67** |

No row is conditional on unverified tool behaviour, so the floor is 67. The largest non-per-record service share is slack at 8 of 42 non-spine calls (19.0%), under the 40% cap. The one Gmail re-read is the clause check for the player-facing and launch-date rules; the write read-backs verify delivery, not difficulty. The Linear comments are the decisive per-record read for eleven claims; the GitHub threads are necessary only for the two contested claims whose PR state could contradict the ticket.

## 10 QC rails

### Two-reading table

| Decision point | Best reading | Strongest alternative | Resolution |
|---|---|---|---|
| C06 status | NOT_LIVE: flag off, no DD SKU, no DD run, readiness P0 removes it from the out-of-moves screen (`gdocs:f_c57724584820a26f3bbe54`) | LIVE: `ENG-2136` Done and `GameOfDominoes#1755` merged (2025-03-29) | H1 excludes merge and ticket state; the readiness P0 is a scoped instruction (2025-05-05) and the config comment is the later, decisive record (2025-09-28); NOT_LIVE |
| C10 status | TESTING: `offer_rotation_v2` is enabled for a 10% cohort and the 48-hour rotation is the enabled behaviour (`linear:ENG-2323` comment) | LIVE: the Hero Offers code is merged and the shop shows offers (`GameOfDominoes#1838`) | H1: a positive subset is testing; TESTING |
| C11 scope | OUT_OF_SCOPE: the live-ops engine is internal scheduling tooling (`confluence:page_live_ops_engine`, `linear:ENG-2372`) | LIVE: the engine runs, so it qualifies | H3: the pack covers player-facing claims only; OUT_OF_SCOPE and drop |
| C13 date | QUALIFY: US soft launch 11 April 2025, worldwide 6 May 2025; "April 14" is unsupported (`confluence:page_domino_gdd`; `snowflake.INSTALL_EVENTS`) | LIVE: the game launched and the exact day does not matter | H3 fixes the GDD soft-launch and worldwide dates as the external values; the readiness 23 April value is reported as a conflict; qualify |
| C09 count | QUALIFY: four coin bundles plus the starter pack (`snowflake.IAP_TRANSACTIONS`) | LIVE as written: "five coin bundles" from the April card (`trello:680222a04f5e6d7a8b9c0d13`) | H2 requires the exact count; the September comment and the SKU set govern; four |
| C12 count | QUALIFY: 4,755 live levels and 245 planned (`confluence:page_domino_gdd`; `gsheets:f_7c3d4e5f60718293a4b5c6`) | LIVE as written: 5,000 from the pipeline target | H2 requires the exact count; the GDD and the manifest agree on 4,755; qualify |
| C03 cadence | QUALIFY: 2–3 runs per week (`snowflake.EVT-0529`) | LIVE as written: "every day" | The event table shows 3 slots per week, not daily; qualify with the cadence |
| Register destination | Update the existing Register tab (`gsheets:f_6b2c3d4e5f60718293a4b5`) | Create a new workbook or overwrite Old register | A1 says the tab "we already use"; the Register tab has headers, the Old register is stale; update Register |
| Conflict reporting | Write both sources and name the governing one (`confluence:page_q4_claims_conflict_format`) | Silently use the readiness doc | A1 and K8 require the conflict column; both sources are written |

### Reach table (load-bearing records)

| Record | Service | Persona verdict | Why it is load-bearing |
|---|---|---|---|
| f_5a1b2c3d4e5f60718293a4 | gdrive | planned seed (U4) | the 13-claim cohort source |
| f_6b2c3d4e5f60718293a4b5 | gsheets | planned seed (U4) | the register destination and the Old register distractor |
| C1CB3D58E38B/1759248600.000100 | slack | planned seed (U4) | the hub and the three authority names |
| C1CB3D58E38B/1759255200.000200 | slack | planned seed (U4) | the correction amendment |
| evt_5c1a7e93b2d04f61a8e7 | gcal | planned seed (U4) | the live-claim standard |
| julia.lawson@harmonygames.co/1860000000000000001 | gmail | planned seed (U4) | the scope and launch-date authority |
| f_c57724584820a26f3bbe54 | gdocs | YES | the Season Pass P0 and the global release date |
| 68d672304f5e6d7a8b9c0d11 | trello | unscoped (always visible) | the external wording rules |
| 67ec1f6021f4291d45f9c21e | trello | unscoped (always visible) | the Collectibles boundary |
| ENG-2136 | linear | unscoped (always visible) | Season Pass ticket state |
| harmonygames-Games/GameOfDominoes#1755 | github | unscoped (always visible) | Season Pass merge evidence |
| snowflake.LIVE_EVENT_PERFORMANCE | snowflake | unscoped (always visible) | the completed-run evidence |
| snowflake.IAP_TRANSACTIONS | snowflake | unscoped (always visible) | the SKU set and count |
| page_economy_design | confluence | unscoped (always visible) | Julia's product ownership and the economy context |

No load-bearing record is a designed denial. The persona can read every scoped record either as a planned seed or as a base YES; the unscoped services are always visible.

**Feasibility.** All four writes exist in `Evals/references/tools/catalog.json`: `gsheets_update_cells` or the sheet write tool, `slack_post_message`, `confluence_update_page`, `linear_create_issue`. Julia owns the register workbook and the claims doc; the Confluence page is editable by her role; the leadership mpim is one she is a member of; the Linear workspace is unscoped. The counts are observable at the needed precision (integers from the table rows and the sheet manifest). Output formats are native.

**Precedence.** Load-bearing facts live only in ● carriers: Linear comments and PR conversation comments (per-record), Gmail thread body (authority), Trello card description (authority), GCal description (authority), Sheet cells and headers (register/manifest), Snowflake rows (aggregate). No load-bearing fact is placed in a ○ carrier (Slides notes, Contacts description, Drive content_text, Slack file content).

**Naturalness constraints.** The prompt will name the anchors ("Leonard's note", "my claims draft"), the deliverable kinds and the deadline. It will not name the authorities' locations, the ids of the tickets or PRs, the number of live claims, the root cause, or the contents of the register.

**Grading devices.** Exact cohort multiset (13 claims), exact status/decision counts, five sampled statuses and three sampled decisions, one conflict row, one volume row, two delivery rows, and the owner/feature lookups that carry the rest of the weight. The register is the single source for the counts; the summary repeats them.

### Coherence rail

Every row in section 1a is dispositioned. The two designed disagreements are (a) the Season Pass ticket/PR vs the readiness P0, resolved by H1 and the dated 2025-09-28 config comment, and (b) the launch-date claim vs the readiness doc and the install table, resolved by H3 and reported in the conflict column. No disagreement is two silent system fields. Seeded records are planned with their companions: Slack thread counters, Trello card activity, Linear issue timestamps and comments, Confluence page versions, GCal attendee copies and invitation mails, Gmail thread counters, and Sheet rows. Ids follow the base scheme (ENG/DES numbers in the pre-freeze gap, 24-hex Trello ids, `evt_`/`f_` ids, `page_` ids, Gmail thread ids in the `jlawson@` mailbox).

## 11 Record plan for /create-injection

**Draft ids are minted here and must survive into the final manifest.** Seeded ids below are exact tokens for the SQL; base ids are citations.

| # | Service | Table / object | Id | Purpose | Date |
|---|---|---|---|---|---|
| 1 | slack | slack_messages | C1CB3D58E38B/1759248600.000100 | A1 hub, Leonard's note | 2025-09-30T16:10:00Z |
| 2 | slack | slack_messages | C1CB3D58E38B/1759255200.000200 | K2 amendment and T8 reply | 2025-09-30T18:00:00Z |
| 3 | slack | slack_messages | C1CB3D58E38B/1759251600.000400 | T13 Collectibles parked decision | 2025-09-30T17:00:00Z |
| 4 | slack | slack_messages | C1CB3D58E38B/1759249980.000300 | T9 Brian distractor | 2025-09-30T16:33:00Z |
| 5 | slack | slack_messages | C1CB3D58E38B/1759246200.000050 | "Season Pass is our headline live feature" wrong summary | 2025-09-30T15:30:00Z |
| 6 | gcal | gcal_events | evt_5c1a7e93b2d04f61a8e7 | H1 review event, three attendee copies | 2025-09-29T15:00:00Z |
| 7 | gmail | gmail_threads / gmail_messages | julia.lawson@harmonygames.co/1860000000000000001 | H3 scope note, one message | 2025-09-30T07:05:00Z |
| 8 | gmail | gmail_messages | julia.lawson@harmonygames.co_1860000000000000002 | INT-11 invitation mail for the review | 2025-09-26T10:00:00Z |
| 9 | gdrive | drive_files + docs_documents | f_5a1b2c3d4e5f60718293a4 | A2 current claims draft, 13 claims | 2025-09-30T15:40:00Z |
| 10 | gdrive | drive_files + docs_documents | f_5a1b2c3d4e5f60718293a5 | T12 v1 draft, 9 claims | 2025-09-12T10:00:00Z |
| 11 | gsheets | drive_files + sheets_spreadsheets + sheets_sheets | f_6b2c3d4e5f60718293a4b5 | Register workbook, Register and Old register tabs | 2025-09-28T14:00:00Z |
| 12 | gsheets | same | f_7c3d4e5f60718293a4b5c6 | level manifest, 4,755 active and 245 planned | 2025-09-29T18:00:00Z |
| 13 | linear | linear_issues | ENG-2367 | ad placement config ticket | 2025-09-27T11:00:00Z |
| 14 | linear | linear_issues | ENG-2368 | event cadence ticket | 2025-09-27T11:10:00Z |
| 15 | linear | linear_issues | ENG-2369 | shop SKU list ticket | 2025-09-26T13:00:00Z |
| 16 | linear | linear_issues | ENG-2370 | level manifest ticket | 2025-09-29T09:00:00Z |
| 17 | linear | linear_issues | ENG-2371 | claims review ticket (K7) | 2025-09-29T12:00:00Z |
| 18 | linear | linear_comments | comment on ENG-645 | weekly quests schedule fact | 2025-09-29T10:00:00Z |
| 19 | linear | linear_comments | comment on ENG-1874 | leaderboard cron fact | 2025-09-29T10:10:00Z |
| 20 | linear | linear_comments | comment on ENG-1385 | Win & Collect slot fact | 2025-09-29T10:20:00Z |
| 21 | linear | linear_comments | comment on ENG-2065 | River Rush schedule fact | 2025-09-29T10:30:00Z |
| 22 | linear | linear_comments | comment on ENG-2136 | Season Pass flag/SKU fact | 2025-09-28T16:00:00Z |
| 23 | linear | linear_comments | comment on ENG-2323 | Hero Offers cohort fact | 2025-09-28T16:20:00Z |
| 24 | linear | linear_comments | comment on ENG-2372 | live-ops engine is internal scheduling only | 2025-09-28T16:40:00Z |
| 25 | linear | linear_comments | comment on ENG-2367 | ads production config fact | 2025-09-28T17:00:00Z |
| 26 | linear | linear_comments | comment on ENG-2368 | Axe/Streak cadence fact | 2025-09-28T17:10:00Z |
| 27 | linear | linear_comments | comment on ENG-2369 | four coin bundles and starter pack | 2025-09-26T13:20:00Z |
| 28 | linear | linear_comments | comment on DES-313 | 4,755 live and 245 planned | 2025-09-29T09:20:00Z |
| 29 | github | github_pr_comments | GameOfDominoes#1755 | Season Pass branch and flag fact | 2025-09-28T18:00:00Z |
| 30 | github | github_pr_comments | GameOfDominoes#1557 | leaderboard cron and cache fact | 2025-09-28T18:10:00Z |
| 31 | github | github_pr_comments | GameOfDominoes#1794 | interstitial control fact | 2025-09-28T18:20:00Z |
| 32 | github | github_pr_comments | GameOfDominoes#1838 | Hero Offers rotation branch fact | 2025-09-28T18:30:00Z |
| 33 | github | github_pr_comments | GameOfDominoes#842 | Win & Collect event fact | 2025-09-28T18:40:00Z |
| 34 | github | github_pr_comments | GameOfDominoes#616 | quest update evidence | 2025-09-28T18:50:00Z |
| 35 | github | github_pr_comments | GameOfDominoes#503 | quest UI evidence | 2025-09-28T19:00:00Z |
| 36 | github | github_pr_comments | GameOfDominoes#1781 | level balance evidence | 2025-09-28T19:10:00Z |
| 37 | trello | trello_cards | 68d672304f5e6d7a8b9c0d11 | H2 external wording card | 2025-09-26T11:00:00Z |
| 38 | trello | trello_cards | 68d6735c4f5e6d7a8b9c0d12 | H2 same-service decoy card | 2025-09-26T11:05:00Z |
| 39 | trello | trello_cards | 680222a04f5e6d7a8b9c0d13 | April five-bundle card (T6) | 2025-04-18T10:00:00Z |
| 40 | confluence | confluence_pages + versions | page_release_status_definitions | H1 decoy | 2025-09-05T09:00:00Z |
| 41 | confluence | confluence_pages + versions | page_external_messaging_guide | H2 decoy | 2025-09-08T09:00:00Z |
| 42 | confluence | confluence_pages + versions | page_q4_product_narrative | H3 decoy | 2025-09-22T09:00:00Z |
| 43 | confluence | confluence_pages + versions | page_q4_claims_conflict_format | K8 conflict format | 2025-09-29T16:00:00Z |
| 44 | confluence | confluence_pages + versions | page_q4_product_claims | D3 page to correct | 2025-09-25T09:00:00Z |

**Base citations that must not be re-seeded:** `gdocs:f_c57724584820a26f3bbe54`; `linear:ENG-645`, `ENG-1385`, `ENG-1874`, `ENG-2065`, `ENG-2136`, `ENG-2323`, `ENG-1871`; `github:harmonygames-Games/GameOfDominoes#1755`, `#1557`, `#1794`, `#1838`, `#842`, `#1563`, `#503`, `#1781`; `trello:67ec1f6021f4291d45f9c21e`; `snowflake.LIVE_EVENT_PERFORMANCE`, `snowflake.IAP_TRANSACTIONS`, `snowflake.INSTALL_EVENTS`; `confluence:page_economy_design`.

### Integrations and companions

| Service | INT id | Companion decision |
|---|---|---|
| slack | INT-06, INT-22 | No Jenkins build post and no Slack e-mail notification are seeded for the claims thread; the messages are ordinary human posts, so no companion is required |
| gmail | INT-11 | The GCal review event seeds invitation mails to its attendees (one per mailbox) |
| gcal | INT-11 | Three attendee copies (Julia, Leonard, Brian) and matching invitation mails |
| github | INT-01, INT-02, INT-03 | Seeded PR conversation comments are recorded in `integration_exceptions` where the GitHub Slack mirror is not seeded; base PRs keep their base companions |
| linear | INT-05 | No Linear e-mail digest is seeded; issue and comment rows are complete |
| trello | INT-21 | Trello has no Slack integration in this universe; no companion |
| confluence | none | Confluence has no integration source in `integrations.json`; no companion |
| gdrive | INT-13 | No Drive share or comment DM is seeded; the files are seeded with their sharing lists |
| gdocs | INT-13 | Same as Drive; no share DM |
| gsheets | INT-13 | Same as Drive; no share DM |
| snowflake | INT-18 | No Metabase chart is seeded; the task reads the tables directly |

## 12 Self-test results

**Hardness gate (design).**

```
HARDNESS GATE (normal (design)): PASS
  [ok] assignment_context: manifest bound to current V3 assignment, freeze and policy
  [ok] effective_profile: effective_profile 'normal' for 'Normal Horizon' → thresholds 'normal'
  [ok] sql_lint_clean: skipped (--design: no SQL yet)
  [ok] base_consistency: skipped (--design: no SQL yet)
  [ok] services_injected: skipped (--design: no SQL yet)
  [ok] rows: skipped (--design: no SQL yet)
  [ok] services_carrying_weight: 11 services with a weight_reason; need ≥ 7
  [ok] no_orphan_injection: skipped (--design: no SQL yet)
  [ok] seeded_ids_exist_in_sql: skipped (--design: no SQL yet)
  [ok] anchors: 2 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 7 fragments; need ≥ 7
  [ok] ask_fragment_services: 7 services carry asks; need ≥ 5
  [ok] ask_fragment_containers: 7 distinct containers; need ≥ 6
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 8 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 13; need ≥ 10 (source-defined: True)
  [ok] evidence_surfaces: 2 surfaces over 2 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 25; need ≥ 25
  [ok] call_budget: unconditional (verified) floor 67 of 67 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 60 and total ≤ 100 (Normal Horizon 50–100)
  [ok] call_budget_spread: 11 services in budget; largest share outside the per-record phase 19% (≤ 40%)
  [ok] traps: 14 traps across 9 families; need ≥ 8 / ≥ 5; unknown family: none
  [ok] trap_independence: traps hit 6 distinct requirements; need ≥ 4 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 2 supersessions (2 with versions in ≥ 2 services, 1 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: skipped (--design: no SQL yet)
  [ok] distractors: 4 distractors of 4 types; need ≥ 4 / ≥ 3
  [ok] discovery_order_proofs: 14 traps carry a discovery-order proof; need ≥ 2
  [ok] independent_chains: 5 chains with 5 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 2, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] mechanism_portfolio: 7 portfolio entries, each a mechanism-enum id with trap/chain nodes, a requirement, a natural-reading fallback and a prior family with its reason
  [ok] artifact_fields: declared ['gradable_surface']: paths relative, digests sha256
  [ok] hidden_authorities: 3 authorities (need ≥ 1), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 1 (need ≥ 0: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 10 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 2
  [ok] requirements: 8 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 4 writes over 4 services; each must depend on findings
```

The stage-gate re-run compares this block with the live tool output; a stale block is not a PASS.

**Gradable surface validate.** `python3 Task_Authoring/tools/gradable_surface.py validate --task-dir Task_Authoring/task_inputs` returns PASS on 55 slots, weight 101, mechanism share 60.4% (reported, never gated); `gradeable-report` returns `SURFACE.GRADEABLE PASS` with 0 ungradable slots. Each sampled group has at most five samples plus one volume row that covers every group: status 5, decision 4, qualifier 2, owner 5, feature 5, evidence 5, evidence_date 5, claim 5, scope 5, action 5.

**Prior forecast (advisory, UNCALIBRATED, pre-registered).** `python3 Task_Authoring/tools/hardness_forecast.py forecast --design --task-dir Task_Authoring/task_inputs --model claude-opus-5-5 --mechanisms M1_status,M2_flag,M3_live_standard,M4_wording,M5_scope,M6_conflict,M7_counts --preregister` returns ledger id `hev_8203a6ce967f5047`. The model reports E[average] 0.584 (independent), 0.589 (source) and 0.617 (correlated), with P(all four difficulty gates) 0.309–0.406. It is a model output, not a measurement, and is UNCALIBRATED; the target sits inside the correlated interval and the independent scenario is 3.6 points under it. The value-of-information order is M4_wording, M7_counts, M2_flag. No channel or batch rate is declared at design time; the forecast models the declared rules only.

**Lazy-solver pass.** A lazy run opens the claims draft, trusts the "all live" line, reads the first Confluence release-status page (the Engineering decoy), copies the Old register tab, and posts the draft's own counts. It fails R1 on C06/C07/C10/C11, R2 on all four qualifiers, R3 on C11, R5 on C06, R7 on both counts, and R6 on the destination. No leak remains: the authorities are not linked from the hub, the draft states no statuses, and no record states a claim's classification.

**Literal-value sweep.** The values "Season Pass", "Collectibles", "live-ops engine", "five coin", "four coin", "5,000", "4,755", "April 14", "April 23", "11 April", "6 May" were searched across the seeded and base records. Each appears only in its own claim/evidence pair; the decoys do not repeat the governing value. The "Old register" repeats the wrong "five" and the wrong "live" statuses by design; it is the stale distractor, not a second live answer.

**"The rest stands" check.** K2 amends C06 and C07 only and says "The rest stands"; no later record re-asserts C06 or C07 as live. The readiness P0 (2025-05-05) is earlier than K2, so it is evidence, not a later amendment.

### Self-review

| Category / decision point | Counter-reading (the strongest argument that the design fails here) | Evidence and resolution |
|---|---|---|
| temporal | The readiness doc's "April 23th" is a typo and could be read as April 23, while the install table says April 11; a run could treat the two as a contradiction that invalidates the date claim | `gdocs:f_c57724584820a26f3bbe54` and `snowflake.INSTALL_EVENTS` are both dated before the freeze; the install comment explicitly separates soft launch from launch date; H3 fixes the external value to the global release date and the register reports both values |
| semantic / category | The Season Pass code is merged and the ticket is Done, so a run may think the claim is true even though the production flag is off | `gdocs:f_c57724584820a26f3bbe54` P0 removes it from the DD out-of-moves screen; `linear:ENG-2136` comment records the DD flag off; no DD row exists in `snowflake.LIVE_EVENT_PERFORMANCE`; the claim is about DD |
| cross-service referential | A reader could think `ENG-2136` and `GameOfDominoes#1755` are the same fact counted twice, so the "no DD SKU" check is redundant | `linear:ENG-2136` is the ticket (2025-05-05) and `github:harmonygames-Games/GameOfDominoes#1755` is the code merge (2025-03-29); the warehouse `IAP_TRANSACTIONS` has no DD Season Pass SKU; three independent sources agree |
| quantitative / reconciliation | The "five coin bundles" card is older but could still be the correct count if one coin SKU was delisted before the freeze | `snowflake.IAP_TRANSACTIONS` lists four coin SKUs and the starter pack across the sold set; `linear:ENG-2369` comment (2025-09-26) lists the same four; no fifth coin SKU appears |
| state / lifecycle | `ENG-2323` is Done and `GameOfDominoes#1838` merged, so the Hero Offers rotation could be live even if the flag is at 10% | `linear:ENG-2323` comment says `offer_rotation_v2` is at a 10% cohort and the 48-hour cadence is not enabled; H1 classifies a subset as TESTING; no 48-hour run exists in `snowflake.LIVE_EVENT_PERFORMANCE` |
| identifier / format | A run could treat the `jlawson@` thread filename as a different mailbox and miss the scope note | `gmail:julia.lawson@harmonygames.co/1860000000000000001` is Julia's mailbox alias (`entity.py`); the scope note is in her mailbox and is reachable by the Gmail tool |
| other | The v1 draft and the Old register tab give a plausible shorter answer; a run could mistake them for the current set | `gdrive:f_5a1b2c3d4e5f60718293a5` is v1 (2025-09-12); `gdrive:f_5a1b2c3d4e5f60718293a4` is v2 (2025-09-30); `gsheets:f_6b2c3d4e5f60718293a4b5` Old register is stale and includes the live-ops engine row; the current Register tab is the destination |
| C06 status | A run may argue the readiness doc is a launch checklist, not a live-claim rule, so the merge should win | H1 is the governing rule (`gcal:evt_5c1a7e93b2d04f61a8e7`); the readiness P0 is a dated human claim that the pass was not shown; the 2025-09-28 comment is later; NOT_LIVE |
| C10 status | A run may argue the offers are live even if the rotation is testing | H1 classifies the feature named in the claim ("rotation every 48 hours") as TESTING because the flag is at 10%; the qualifier must say "in testing" |
| C11 scope | A run may argue that a live feature belongs in a product claims pack even if it is another title | H3 (`gmail:julia.lawson@harmonygames.co/1860000000000000001`) says DD only; the old register row is a distractor; OUT_OF_SCOPE |
| C13 date | A run may argue the exact date is immaterial and mark C13 KEEP | H3 fixes the global release date; the three dated values disagree; the conflict column must state both and the register must qualify; the rubric's conflict row is weight 5 |
| C09 count | A run may copy the April card's five bundles | The sold set is four coin SKUs plus the starter pack; H2 requires the exact count; QUALIFY |
| C03 cadence | A run may accept "every day" because the event is live | The event table shows three slots per week (`snowflake.EVT-0529` and the September series); QUALIFY with the cadence |
| Register destination | A run may create a new workbook because the Register tab is empty | A1 says "the tab we already use"; the Register tab has headers and the workbook is Julia's; update it |
| conflict report | A run may silently use the readiness doc and not record the disagreement | K8 (`confluence:page_q4_claims_conflict_format`) and A1 require both sources; the conflict column is graded |
| Delivery | A run may write the register but skip the summary or the ticket | A1 and K2/K7 require the summary counts and the follow-up ticket; delivery slots are separate |
| Sibling defect | Another October-list card could be a second unbuilt feature, which would make C07 less exceptional | `trello:68c44cf45171b65e64221c01` and `trello:68c453cd0ff184d95550bc58` have September activity and linked tickets; `trello:67ec1f6021f4291d45f9c21e` is the only card with no ticket, no PR and no activity since May |
| Companion | The seeded GCal event could fail base_check if its attendee copies or invitation mails are missing | `gcal:evt_5c1a7e93b2d04f61a8e7` is planned with three attendee copies and INT-11 invitation mails (record plan rows 6 to 8); the injection preflight verifies the companions |
| Tool surface | The table decoder could miss a native Sheet write if the workbook title does not match the register name pattern | the workbook is named Q4 Product Claims Register and `gsheets:f_6b2c3d4e5f60718293a4b5` carries the Register tab; the table name_regex matches the workbook title |

**Hardness gate.** The self-review re-states the gate result in the required form: HARDNESS GATE (normal (design)): PASS. The full output is pasted verbatim above.

**Unresolved: none.**

```
STAGE GATE scenario: PASS — Task_Authoring/task_inputs · 01_Scenario_Design.md#5aefb2d5ce41 · 01_Hardness_Manifest.draft.json#81b53550b53a · 01_Gradable_Surface.json#ed7f0476e12c · 00_Assigments.md#f8550b78dd9d · __context__#fee9c0ab9e8c · __assignment__#3f9540413be0 · __policy__#dc4ab5df3cdd · __gate_policy__#bf8e231eb5d9 · __review__#73fa568faaa0 · blocking 0 · warnings 0 · checks 32
[PASS] assignment.v3_context: Julia Lawson / Product Manager; hard cap <70%; freeze 2025-10-01T00:00:00Z; shared source available; record dates and freeze-state evidence checked separately
[PASS] structure.outputs: 3 output(s) present: 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json
[PASS] structure.inputs: 1 input(s) present: 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md)
[PASS] structure.sections: 19 required sections present and non-empty (01_Scenario_Design.md)
[PASS] structure.placeholders: no placeholders in 01_Scenario_Design.md
[PASS] evidence.storyline: 12/12 items carry a source pointer (min 80%)
[PASS] evidence.coherence_audit: 7/7 items carry a source pointer (min 100%)
[PASS] evidence.hidden_authorities: 3/3 items carry a source pointer (min 100%)
[PASS] evidence.delegation: 16/16 items carry a source pointer (min 90%)
[PASS] evidence.trap_register: 64/64 items carry a source pointer (min 90%)
[PASS] evidence.record_plan: 54/55 items carry a source pointer (min 80%); unsourced e.g. L523: 'confluence | none | Confluence has no integration source in `integrations.json`; no compan'
[PASS] evidence.active_speakers: 9/9 items carry a source pointer (min 100%)
[PASS] tool.hardness_gate_design: hardness_gate --design pasted PASS; re-run PASS
[PASS] tool.persona_reach: persona_view reach pasted for julia.lawson@harmonygames.co and matches the re-run (158 channels)
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] kb.coherence_hazards: coherence audit cites 7 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 9 speaker rows carry their activity.json status_at_clock
[PASS] kb.integrations: companions listed per integrations.json (10 INT ids, services ['confluence', 'gcal', 'gdocs', 'gdrive', 'github', 'gmail', 'gsheets', 'linear', 'slack', 'snowflake', 'trello'])
[PASS] kb.storyline: timeline cited; cohorts ['SL-T26']; trap_catalog ['C01', 'C02', 'C03', 'C04', 'D04', 'D05']
[PASS] boundary.anchor_naming: 4 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] tool.redteam_dual: dual red team present (01b_Redteam_Review.md + .second.md)
[PASS] surface.valid: 55 slots, weight 101; geometry report-only, never gated: mechanism share 60%, always-pass share 40%
[PASS] forecast.preregistered: prior forecast pre-registered in the ledger: ['hev_8203a6ce967f5047'] (UNCALIBRATED, advisory)
[SKIP] revise.intake: no MODE B report and no revision-intake section: nothing to take in
[PASS] reach.scenario: 7 scoped load-bearing ids YES for julia_lawson (6 planned seeds not yet in base: verified at the injection gate)
[PASS] review.counter_readings: 18 evidenced counter-readings (of 19 found; need ≥ 16) in 01_Scenario_Design.md
[PASS] review.coverage: self-review addresses all 8 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.draft.json is bound to the current assignment, policy, source context and freeze
[PASS] v3.role_review: current role-plausibility review recorded; semantic judgment belongs to the named reviewer
[PASS] handoff.pasted: pasted into the Self-review by --paste
```









## 13 Red team (dual)

The dual red-team tool is attempted in section 12's run log. Because the local proxy has no reviewer key, this design uses the recorded fallback required by the playbook; the two independent reviews are in `01b_Redteam_Review.md` and `01b_Redteam_Review.second.md`.

RED TEAM FALLBACK: two independent read-only reviewers (the redteam agent, GPT-6.1 Sol, and the methodologist-gpt agent, GPT-6.1 Sol) reviewed the dossier, manifest and surface against the hardness, fairness, coherence and methodology rails; the proxy was unavailable because REDTEAM_BASE_URL and REDTEAM_API_KEY are not set in this session, and Claude reviewers were rate-limited, so both reviews are recorded in the two 01b files with their findings and dispositions.

Findings and dispositions are listed in the two review files; every finding is either fixed in this revision or rebutted with a record pointer in the same file.
