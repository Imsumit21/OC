# 01 — Scenario Design — Julia Lawson · Product · Marketing and GTM · Planning and decision support · Long Horizon · Medium · Oct 1 2025 (synth-cut)

Command `/create-scenario`. Universe synth-cut; Clock 2025-10-01 00:00 PT (07:00Z); seed bound `2025-10-01T00:00:00Z`; `context_hash 4bbc727fd48ac35a16b4afeda5430937563f2ce969970841bb4f3f97b6a38a39` (re-bound to this machine for revision 2). Profile extreme (Long Horizon), with a requester-confirmed `volume_exception` (floors 130/75) recorded in the manifest; the cohort has 41 members since revision 6 (42 in revision 5, 39 in revision 4, 44 in revisions 2 and 3, 47 before), above the extreme ≥ 40 cohort rule with no cohort exception (§5, and Revisions 6 and 7 in §18). This file designs the scenario, records and difficulty only; the prompt, Oracle Events and rubric criteria come later.

Method note. All discovery ran read-only through `tools/hg.py` and `tools/persona_view.py`; cached pulls live in `Working_Files/research/raw/`. Four research workers (R-A gate contract, R-B spine facts, R-C carriers/ids, R-D coherence audit) produced `research/R_*.md`. One early worker (S7) read backend files outside `hg.py`; its leads are unverified and used only to REMOVE design dependencies (no Plague Race/Endless window dates are graded, the dropped C5 reward-cut channel), never to add a graded fact. No SQL is executed at this stage.

## 0 · Assignment, persona census and method

Assignment (V3, verbatim from `00_Assigments.md`): Business Function Product; Persona Julia Lawson, Role Product Manager; Competency Marketing and GTM; Task Skill Planning and decision support; Task Type long-horizon; Difficulty Mode medium; Universe Date October 1, 2025 07:00. `task_context.py --write --require-source` resolves `source.mode=universe`, universe `synthcut`, `context_hash 4bbc727f…`.

Persona reach (`persona_view reach julia_lawson`, re-run by the gate; verbatim):

```text
REACH  Julia Lawson <julia.lawson@harmonygames.co>  Product Manager / Product
clock 2025-10-01

SLACK  user=EMPLOYEE_0005_SLACK_ID  visible channels=147 {'mpim': 52, 'public': 23, 'private': 47, 'im': 25}  messages=238131  public-not-member (UNVERIFIED)=44
  persona posts=31848 last post=2025-09-30  last activity in visible channels=2025-10-01
GMAIL  mailbox=julia.lawson@harmonygames.co threads=253 messages=304 range=2023-07-16..2025-09-17
DRIVE  owned=28 {'application/vnd.google-apps.spreadsheet': 12, 'application/vnd.google-apps.document': 10, 'folder': 2, 'application/vnd.google-apps.presentation': 2, 'application/pdf': 2}
UNSCOPED (always visible): contacts, github, trello, linear, snowflake, confluence
LAST ACTIVITY (days before clock): slack_persona_post=2025-09-30 (1d), slack_visible_channels=2025-10-01 (0d), gmail=2025-09-17 (14d), gcal_last_event_before_clock=2025-09-29 (2d), drive_last_modified_visible=2025-09-30 (1d)
```

Julia is a member of every Slack channel, DM and Drive folder the design uses, her own Gmail mailbox and (unscoped) Linear / GitHub / Trello; the one channel she is NOT in, `#zombie-prs` (C093LEZGF6J), carries only companion mirrors, never evidence (§16). Writes: her own Drive/Sheets, a reply in a DM she is a member of, Linear (unscoped) and a Gmail reply — all confirmed in §10 and §14.

## 1 · Storyline

On Oct 1 2025 the Zombie Match 3D (ZM3D) beta is about to buy its first users. Frederick Stone — owner of the beta buy and of the calendar — asked Julia in their DM yesterday for the live-ops calendar of the four beta buy weeks (Mon Oct 6 – Sun Nov 2): which beats run in which windows, what is held and until when, the push for each beat, what is still to do before each runs and by whom, and her recommendation with the tradeoffs. Four minutes later, in a thread reply under his own ask, he added two things on top of his brief: the push plan covers the PNs Beta tab as it stands except four named rows (and copy that names no game may go out), and Zombie Lane stays off the calendar. The calendar goes in a sheet in her Drive folder, is linked from the calendar ticket, and the recommendation goes back to him in the DM. The whole task is one PM planning deliverable; every hard call survives complete retrieval. (KB anchors: `timeline` 2025-09 live-ops entries; cohort `LIN-OPEN-ZOM`; `trap_catalog` families `C01`/`C02` thread corrections, `N01` ticket-series collisions, `P01` lookalike people.)

The storyline's load-bearing records (each a seeded or base locator):
- **The ask.** Frederick's DM to Julia (the anchor, scope and reply destination) — `slack:D05SD5QLG94/1759263617.418209`
- **The ask's follow-up.** Frederick's thread reply under his own ask (the root shows `reply_count` 1): the push plan is the PNs Beta tab one line per row, local notifications included, minus Hourly Coins, Nathan's Treasure Hunt, Streak Fever and Axe Arena; copy that names no game may go out; Zombie Lane stays off the calendar (R1, R6) — `slack:D05SD5QLG94/1759263878.305129`
- **The rulebook.** Frederick's beta brief — the calendar owner's working rules (R1-R6, R8) — `f_7c3e91a4d2b85f60e1a9c4`
- **The span.** Frederick's beta UA plan deck — the four buy weeks (R9) — `f_2b9d4e7a1c63f08d5e7b21`
- **Done-not-deployed.** Collect & Win client PRs merged before the Sep 30 cut — `harmonygames-Games/match3d#470`
- **The deploy date.** Douglas's backend release plan event, Wed Oct 8: "The server windows that are still on the DEV stack go live with this release", so only Collect & Win waits on it (its first prod window, a late start and not a hold) — `evt_9a4c2e7f1b3d58e06c7a2f`
- **The one-off.** Robert's #zombie-art approval of Martin's Halloween one-off, later withdrawn in his DM — `slack:C08R8CHB0QL/1758121809.236839`
- **The prod re-test.** Vincent's Sep 30 re-test, a #zombie-match3d root (cross-channel), weekly leagues do not start on the current prod build even after a restart (an established prod failure -> held) — `slack:C0880U9751A/1759265412.481909`
- **The config slip.** Brian's Season Pass November handoff, slipped to Fri Oct 31 in a later mail of its own (R8) — `julia.lawson@harmonygames.co/1844311412966040123`
- **The push sheet.** the shared 'PNs Beta' tab — Ready flags, the second 'Status (NA, WIP, LIVE)' column and old-title copy; ten of its rows are planned (R6) — `f_a325dd4af80afc5994d5dc`
- **The calendar ticket.** ZOM-78 'Event Calendar For Zombie Match 3D' (Backlog) — reuse, do not file new (R7) — `ZOM-78`

Anchor names (noun phrases, ≤ 6 words; the prompt may name the work only through these):

| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |
|---|---|---|
| A1 | Frederick's beta calendar ask | `slack:D05SD5QLG94/1759263617.418209` |
| A2 | my beta live-ops calendar sheet | `f_e4a17c90b3d25f6a8c1d73` |

Distinctness. Vincent's `vincent-zm3d-release-gate` decides whether two Sep 30 submission builds may ship; Claire's `claire-zm3d-october-object-handoff` decides which art objects go to level design. This task decides the live-ops and push calendar for the bought-user beta — a calendar, a push plan and a recommendation. No ticket or PR gets a ship/defect verdict here (`harmonygames-Games/match3d#470`); the issue and PR spine is a readiness surface, not a release gate.

## 2 · Coherence audit

Source: `coherence_hazards.json` (6 categories, 59 emitted hazards), the synth-cut `known_data_issues` cards, and R-D's probe over every record a correct run opens (`research/R_D_coherence_audit.md`). The design requires and cites no artifact that carries an ungoverned contradiction; where a required artifact holds an odd state, a dated owner statement in the brief explains it (never a silent edit). Each row below is a real record pointer.

Per `coherence_hazards` category (all six covered):
- **temporal** hazard `T01`: `reviewed` timeline events have null `created_at` and empty actor on every in-scope PR (`harmonygames-Games/match3d#470`) — the design never dates a review from the timeline; review dates come from the review's own `submitted_at`.
- **semantic/category** hazard `S01`: cross-game copy reuse; the push sheet's `PN BETA Translated` tab holds Domino Adventures / River Rush rows (`f_a325dd4af80afc5994d5dc`) — the brief scopes beta pushes to the English `PNs Beta` tab only, so the translated tab is out of scope by a dated owner rule.
- **cross-service referential** hazard `R07`: Snowflake/Confluence live-ops pages disagree with warehouse rows (`page_liveops_calendar`) — excluded; no Snowflake record and no live-ops calendar page is on the required path (`f_a325dd4af80afc5994d5dc` is the only required sheet). The one Confluence page on the path is `page_season_pass_spec` (the 24 h config lock, §11), which this card does not cover.
- **quantitative** hazard `Q02`: `reply_users_count` vs distinct repliers mismatch — the only in-universe example sits in July, outside the Sep 15-30 read window (`slack:C0880U9751A/1750724624.203279`); none in scope.
- **state/lifecycle** hazards `L03`/`L09`/`L10`: open ZOM issues whose fix shipped, and merged PRs with no human APPROVED (`ZOM-429`, `harmonygames-Games/match3d#470`) — these ARE the designed decisions (R3, R5); each is governed by a dated record (Vincent's re-test, the per-PR review list), never left as a bare contradiction. Since revision 5 the SQL closes only the two tickets whose own seeded notes report the work finished (`ZOM-344`, `ZOM-432`) and leaves `ZOM-387` exactly as base has it, Todo with no seeded note; the three closures and the `ZOM-387` start that revision 4 added were at odds with base and are taken back. Revision 6 takes `ZOM-387` out of the cohort on its merits (the `L03` case: Todo while its PR merged in July, so "open" is not a reliable predicate for it), so `L03` is neither modified nor cited and needs no acknowledgement (dossier §10 and §11 Revision 6). Revision 9 closes `ZOM-563` with Vincent's check on prod, whose base confirmation sits in a DM Julia cannot read.
- **identifier/format** hazards `I01`/`I10`: raw-shaped Slack rows in DMs and non-`usr_<16hex>` Linear ids (`usr_Robert`) (`slack:D05GU6L0XFH/1759248350.473459`) — cosmetic; no graded value reads an id's shape.

Required-artifact contradictions and their governed treatment (each a dated owner statement, not a silent edit):
- Push sheet title 'Push Notifications Zombie Match' vs its two internal status columns and cross-game translated tab (`f_a325dd4af80afc5994d5dc`): the brief reads the first 'Status' column as the copy/readiness flag and the second 'Status (NA, WIP, LIVE)' as the live state (a push goes out only if its row is Ready and LIVE; a WIP row is held on that status, which says nothing about client wiring); the translated tab is the old Domino set awaiting ZM3D localization. The tab's four rows for things that are not in the beta (Hourly Coins, Nathan's Treasure Hunt, Streak Fever, Axe Arena) are left off by Frederick's dated follow-up (`slack:D05SD5QLG94/1759263878.305129`).
- The Sep 22 leaderboard report 'killing the app doesn't help' vs the same thread ending 'working fine right now' (`slack:C08R27X0EAH/1758546119.789009`): a fault on a test build fixed by a revert; the governing record is Vincent's LATER Sep 30 prod re-test, a root in #zombie-match3d (`slack:C0880U9751A/1759265412.481909`) — a different channel from the Sep 22 recovery, so the reconciliation is cross-channel, not a same-thread correction.
- Robert's DM holds an auto-battler topic on Oct 1 03:32Z after the seed bound (`slack:D05GU6L0XFH/1759289577.628399`): the seeded withdrawal sits before it on its own topic and reads naturally.
- Known-issue card SC-15 (`ZOM-521`), added in revision 3 — touched: SC-15 — repaired; not graded. In base the VFX master ticket ticks all six checklist items while two of its children are still In Progress (`ZOM-526` Tokens traveling to live-ops, `ZOM-528` Claimed Cards traveling to inventory section), and the seeded notes `cmt_zom526_1` and `cmt_zom521_1` sit on those tickets; the platform `/prompt` review of revision 2 failed Cross-Service Coherence on exactly this. Revision 3 governs it with a dated owner statement, neither left standing nor edited silently: the seeded `ZOM-521` description keeps four items ticked and unticks the two whose child tickets are open, and Brian Foster, who created the tickets, notes on `ZOM-526` on Sep 26 that he unticked it because it was marked done too early and that the Season Pass part is polish on an effect that already ships (`cmt_zom526_2`). Base behind the wording: Calvin's Sep 17 Linear unfurl of the master ticket still showed Claimed Cards unticked, and `ZOM-526` was only put In Progress at 2025-09-17T15:52:10Z, after the master ticket's last base update at 15:50:49Z (`slack:D0770ET6WBW/1758124315.038369`, a DM between Calvin and Brian that Julia is not in: grounding for the author, not a record any run needs). No rule, slot, trap, fragment or cohort decision reads the checklist or token travel; `ZOM-521` and `ZOM-526` stay cohort members read per record. Revisions 6 and 7 explain why the two items stay open: `cmt_zom526_3` says only the postponed Axe Arena travel is left on `ZOM-526`, and `cmt_zom521_2` says the card pack animation went in with #475 and the item and `ZOM-528` stay open until Brian has seen it in a build.

## 3 · Active speakers

Every person the design puts words in the mouth of is active in Sep 2025 and quiet in Oct (`activity.json` `status_at_clock`), so a seeded Sep-dated record is in character and a reader will not expect Oct chatter from them. Each row carries the speaker's email (RX_EMAIL) and `activity` status.

| Speaker | Email | activity.json status_at_clock | Seeds they carry |
|---|---|---|---|
| Frederick Stone | frederick.stone@harmonygames.co | active_sep_2025_quiet_in_oct | the ask and his thread follow-up under it, the beta brief, the UA deck |
| Robert | robert@harmonygames.co | active_sep_2025_quiet_in_oct | the #zombie-art one-off approval and its DM withdrawal; since revision 10 the reply in Martin's desert thread |
| Vincent Parker | vincent.parker@harmonygames.co | active_sep_2025_quiet_in_oct | the Sep 30 prod re-test on weekly leagues; since revision 9 the closing note on ZOM-563 (`cmt_zom563_2` since revision 12); since revision 10 the close of the Sep 30 shader thread |
| Douglas | douglas@harmonygames.co | active_sep_2025_quiet_in_oct | the ZOM-429 owner note and the Oct 8 backend release event; since revision 11 the reply in the #zm-collect-win reward-table thread; since revision 12 the first note on ZOM-563 (`cmt_zom563_1`) |
| Brian Foster | brian.foster@harmonygames.co | active_sep_2025_quiet_in_oct | the Season Pass November handoff and its slip; the Axe Arena card comment; since revision 9 the note on ZOM-566 (`cmt_zom566_1`); since revision 10 the note on ZOM-565 (`cmt_zom565_2`); since revision 11 the note on ZOM-465 (`cmt_zom465_3`) |
| Owen Baker | owen.baker@harmonygames.co | active_sep_2025_quiet_in_oct | the analytics note on ZOM-566 (`cmt_zom566_2` since revision 9); Oct 8 release attendee |
| Arthur Blake | arthur.blake@harmonygames.co | active_sep_2025_quiet_in_oct | the inline review notes on #470, #468 and, since revision 8, #472 (revisions 4 to 7: a conversation note on #473; through revision 3: #370/#438) |
| Samuel Turner | samuel.turner@harmonygames.co | active_sep_2025_quiet_in_oct | the closing note on ZOM-432 that the daily-gift frame went out with PR #471 and is in both submission builds (iOS 50, Android 135) |
| Marcus Bennett | marcus.bennett@harmonygames.co | active_sep_2025_quiet_in_oct | the two notes on ZOM-465; the second says the Collect & Win icon animation is still to do (a #454 conversation note through revision 3) |
| Oliver Brooks | oliver.brooks@harmonygames.co | active_sep_2025_quiet_in_oct | the Sep 22 leaderboard thread (base, unchanged) |
| Leonard Hayes | leonard.hayes@harmonygames.co | active_sep_2025_quiet_in_oct | the base beta pipeline and tech-stable call (base, unchanged); since revision 5 the note on the open quests roadmap card; since revision 9 the S23 Ultra reply in #zombie-bugs and the confirmation on ZOM-534 (`cmt_zom534_2`) |
| Martin Walsh | martin.walsh@harmonygames.co | active_sep_2025_quiet_in_oct | the base #zombie-art Halloween icon post (base, unchanged) |

## 4 · Identity traps

`entity.py collisions` (verbatim head). The design never relies on a bare first name or a token; every seeded speaker is pinned by a full service id (§3, R-C §2). `trap_catalog` family `P01` (lookalike people) and `N01` (ENG-n / ZOM-n share 521 numbers) are live in this universe.

```text
SHARED_FIRST_NAMES (4)
  claire: ['Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]', 'Claire <github:PERSON_2360_GITHUB_USERNAME>']
  marcus: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Marcus Lee <marcus.lee@harmonygames.co>', 'Marcus <trello:c48a210d5c5a4b59231c6873>']
  martin: ['Martin Lewis <PERSON_0394_EMAIL>', 'Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]']
  thomas: ['Thomas Baker <thomas.baker@harmonygames.co>', 'Thomas <thomas@harmonygames.co> [persona thomas]']
SHARED_LAST_NAMES (5)
  baker: ['Owen Baker <owen.baker@harmonygames.co> [persona owen_baker]', 'Thomas Baker <thomas.baker@harmonygames.co>']
  brooks: ['Lauren Brooks <lauren@harmonygames.co>', 'Oliver Brooks <oliver.brooks@harmonygames.co> [persona oliver_brooks]']
  lawson: ['Julia Lawson <julia.lawson@harmonygames.co> [persona julia_lawson]', 'Peter Lawson <peter.lawson@harmonygames.co>']
  price: ['Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]', 'Nathan Price <nathan@harmonygames.co>']
```

Design consequences: Martin Walsh (the Halloween post) is distinct from Martin Lewis (`martin.walsh@harmonygames.co`); Owen Baker (the ZOM-566 note) from Thomas Baker (`owen.baker@harmonygames.co`); Marcus Bennett (the ZOM-465 icon notes) from Marcus Lee and the Trello Marcus (`marcus.bennett@harmonygames.co`). The persona Julia Lawson is distinct from Peter Lawson (`julia.lawson@harmonygames.co`). Frederick Stone's GitHub login renders as 'Ryan' (`PERSON_2314_GITHUB_USERNAME`) — never cross-attributed.

## 5 · Cohort spine

The honest live-ops work-item population is **41 records of two types** since revision 6 (42 in revision 5, 39 in revision 4, 44 in revisions 2 and 3) under one readiness rule (cohort `LIN-OPEN-ZOM`): 18 open ZOM issues whose title bear on an in-scope beat's readiness or live-ops infrastructure (Boss Arena / Axe Arena / Win Streak / Zombie Lane out) and 23 merged match3d PRs (Jul 1 – Sep 30) each carrying a post-merge still-to-do, deploy or scope fact, outside Boss Arena and not misfiled. The revision-5 SQL closes two of the 21 issues as Done, each at the time of its own note (`ZOM-344`, `ZOM-432`). A closed ticket is not an open work item under the brief's still-to-do rule (what still has to land, not what already shipped), so the two leave the cohort. `ZOM-471`, `ZOM-542` and `ZOM-565`, which revision 4 had closed, are open and are members again, the first and last in their base states and `ZOM-542` Todo since revision 11; `ZOM-566`, In Progress, stays; `ZOM-387` left the cohort in revision 6 on its merits (the requester's decision): it is a KB `L03` record, Todo while its referencing PR #319 merged in July, so "open" is not a reliable predicate for it, and the KB's guidance is to keep such issues out of a cohort whose predicate is "open". The five PRs whose seeded notes moved away (#370, #438, #454, #471, #473) stay too: each is a member for a fact in its own body, commits or files (`research/EXPAND_cohort_feasibility.md` §2), never for the note. 41 is above the extreme minimum of 40 with no exception (42 in revision 5; revision 4 stood at 39, one short). The enriched cohort reached 44 members in revisions 2 and 3 (≥ 40 with no exception; the earlier borderline 36-member spine is superseded). It had 47 before revision 2: `ZOM-442` and PRs #297 and #308 existed only for Zombie Lane and left with it, and the GitHub read surface went from 41 to 39 in-scope PRs (figures as in the revision-2 draft manifest). Every member carries a genuine per-record readiness, deploy or scope decision — no 'nothing-outstanding' padding (`research/EXPAND_cohort_feasibility.md`). The ≥ 3 surfaces over ≥ 2 services, each surface's `why_no_bulk` and the extreme `short_circuit` analysis apply and are satisfied below. Definition source: fragment `K6` (the brief's scope rule).

| Surface | Service · tool | Records × per-record | why_no_bulk (abridged) | short_circuit (abridged) |
|---|---|---|---|---|
| Status column (R3) | linear · `linear_list_comments` | 18 × 1.0 | linear_list_issues returns state and description, never comments (Ask_Carriers §3, §6b); b… | no other surface carries an issue's latest prod note: the state is stale for ZOM-429 (Back… |
| Status column (R3) | github · `github_get_pull_request_reviews` | 39 × 1.0 | a PR's review STATE lives only in the per-PR review list; inline and conversation comments… | the hold rule certifies no in-scope cohort PR carries an unresolved change-request review … |
| Still to do column (R5) | github · `github_get_pull_request_comments` | 39 × 1.0 | inline review comments come back only from this per-PR call; search 'comments' counts conv… | reviews show an empty-bodied APPROVED on #470 and #472; the server-window note on #470 and the vial-model note on #468 a… |

Σ per-record calls × records = **96** (18 + 2 × 39; floor 75; it was 135 in revisions 6 and 7, 136 in revision 5, 133 in revision 4, 138 in revisions 2 and 3 and 145 before). Three surfaces over two services (Linear, GitHub); none can be bulk-read — Linear issue notes come only from `linear_list_comments` (base holds 0 comments), and a PR's review state and inline review comments are separate per-PR calls that search never returns. A fourth surface, `github_get_issue_comments`, stopped counting in revision 8: no seeded note is left in a PR conversation, and the 42 base comments there on the 39 PRs are all bots (38 CodeRabbit, 4 Linear), so it fails the necessity rule (`Hardness_Mastery.md` §2.5) (R-C §1, R-B §4). A run that skips them cannot tell a hold from a known issue (`ZOM-429` vs `ZOM-534`) or find the still-to-do notes (`harmonygames-Games/match3d#468`).

## 6 · Hidden authorities

Three hidden authorities, each homed in a rarely-opened service, each governing a disjoint set of requirements, each with a same- or cross-service decoy that a targeted search also meets. Every row carries a seeded pointer.

| Authority | Home | Governs | findable_query | Authority record | Decoy record (scope) |
|---|---|---|---|---|---|
| H1 Frederick's beta brief | gdocs | R1, R3, R4, R6 | "beta brief" | `f_7c3e91a4d2b85f60e1a9c4` | `slack:C05KNDCHAAG/1757704290.799329` (Leonard's beta pipeline — a feature list, not the rulebook) |
| H2 Brian's Season Pass November handoff | gmail | R8 | "Season Pass November" | `julia.lawson@harmonygames.co/<CAPT--p4a5fY9wd6vr+8JtjFXfffkxQOCEUYsuqSPy9HbQJu3Fs@mail.gmail.com>` | `julia.lawson@harmonygames.co/1843954828968533812` (Brian's earlier Oct 29 mail — superseded) |
| H3 Douglas's backend release | gcal | R2 | "backend release" | `evt_9a4c2e7f1b3d58e06c7a2f` | `slack:C05KNDCHAAG/1758558302.777379` (Julia's own Sep 22 'feature completed' note — dev-side) |

The brief (`H1`, `f_7c3e91a4d2b85f60e1a9c4`) states rules and never names a held or late beat — it is the rulebook, not an answer key. Brian's handoff (`H2`, `julia.lawson@harmonygames.co/1844311412966040123`) and Douglas's release event (`H3`, `evt_9a4c2e7f1b3d58e06c7a2f`) each decide exactly one requirement (R8, R2). Decoy scopes are disjoint (a feature list vs the rulebook; an earlier vs later mail; a dev-side note vs the prod deploy), so no identical-scope contradiction can arise.

## 7 · Delegation lattice

Every ask fragment chains back to an anchor through explicit delegations whose words appear in the delegating record. The hub is the ask (`A1`, `slack:D05SD5QLG94/1759263617.418209`); the brief is one hop from it and most rules delegate from the brief. Each row carries the delegating record pointer.

| Fragment | Service | Reqs | incorporated_via | delegated_by_record | quote |
|---|---|---|---|---|---|
| K1 | gdocs | R1 | A1 | `slack:D05SD5QLG94/1759263617.418209` | "working rules for the calendar are in my brief" |
| K2 | gdocs | R2 | A1 | `slack:D05SD5QLG94/1759263617.418209` | "working rules for the calendar are in my brief" |
| K3 | gdocs | R3 | A1 | `slack:D05SD5QLG94/1759263617.418209` | "working rules for the calendar are in my brief" |
| K4 | gdocs | R4 | A1 | `slack:D05SD5QLG94/1759263617.418209` | "working rules for the calendar are in my brief" |
| K5 | gdocs | R6 | A1 | `slack:D05SD5QLG94/1759263617.418209` | "working rules for the calendar are in my brief" |
| K6 | gdocs | R5 | A1 | `slack:D05SD5QLG94/1759263617.418209` | "working rules for the calendar are in my brief" |
| K7 | gdocs | R8 | A1 | `slack:D05SD5QLG94/1759263617.418209` | "working rules for the calendar are in my brief" |
| K8 | gslides | R9 | A1→K1 | `f_7c3e91a4d2b85f60e1a9c4` | "the four buy weeks in my UA plan" |
| K9 | gmail | R8 | A1→K7 | `f_7c3e91a4d2b85f60e1a9c4` | "Every config a beat needs lands before its lock" |
| K10 | gcal | R2 | A1→K2 | `f_7c3e91a4d2b85f60e1a9c4` | "the backend release instant read in UTC" |
| K12 | linear | R7 | A1 | `slack:D05SD5QLG94/1759263617.418209` | "the calendar ticket" |
| K13 | slack | R3 | A1→K3 | `f_7c3e91a4d2b85f60e1a9c4` | "An established failure holds it" |
| K14 | slack | R1 | A1→K1 | `f_7c3e91a4d2b85f60e1a9c4` | "Boss Arena is off this calendar until the pivot call" |
| K15 | gsheets | R7 | A2 | `f_e4a17c90b3d25f6a8c1d73` | "Still to do (owner)" |
| K16 | gsheets | R6 | A1→K5 | `f_7c3e91a4d2b85f60e1a9c4` | "A push goes out only if its row is Ready and LIVE" |
| K17 | slack | R1, R6 | A1 | `slack:D05SD5QLG94/1759263617.418209` | "the live-ops and push calendar for the beta buy" |

K17 (added in revision 2) is the amendment in the ask's own thread, `slack:D05SD5QLG94/1759263878.305129`: the ask asks for the calendar, and Frederick's reply under it says which push rows it covers and that Zombie Lane stays off. K11 (the quest note on Trello, R5) was dropped in revision 5: the note carries no requirement any more. 16 fragments over 7 services and 10 containers remain, each at or above its floor (12 / 7 / 10).

## 8 · Chains and trap register

5 independent chains (distinct root-cause mechanisms; CH5 was retired in revision 5), each ≥ 3 hops over ≥ 2 services ending in a graded fact. Then the trap register: 14 traps (T1–T15 without T12; T15 added in revision 2) in multiple families plus 12 distractors (D1–D11 and, since revision 5, T12, which keeps its id). Each row carries a record pointer.

### Chains

| Chain | Root cause | Ends in | Hops (service: finding) |
|---|---|---|---|
| CH1 | A24 | R2 | slack `D05SD5QLG94/1759263617.418209`: Frederick asks for the beta-weeks ; gdocs `f_7c3e91a4d2b85f60e1a9c4`: deploy rule: windows go live only ; github `harmonygames-Games/match3d#468`: client merged Sep 29; github `harmonygames-Games/match3d#470#rc_10`: server windows only on dev; prod w; gcal `evt_9a4c2e7f1b3d58e06c7a2f`: the next backend release is Wed Oc |
| CH2 | A11 | R4 | gdocs `f_7c3e91a4d2b85f60e1a9c4`: a one-off takes a recurring slot o; slack `C08R8CHB0QL/1758213623.552919`: Robert: Halloween one-off in Plagu; slack `D05GU6L0XFH/1759270241.638119`: Robert drops the October one-off;  |
| CH3 | A13 | R8 | gdocs `f_7c3e91a4d2b85f60e1a9c4`: config locks 24 h before the seaso; gmail `julia.lawson@harmonygames.co/<CAPT--p4sBC8XnaA7qBDMtZkWqJPiXP0MT3deOQGPusOZhHF+vo@mail.gmail.com>`: Brian: November config Wed Oct 29; gmail `julia.lawson@harmonygames.co/<CAPT--p4a5fY9wd6vr+8JtjFXfffkxQOCEUYsuqSPy9HbQJu3Fs@mail.gmail.com>`: Brian: Fri Oct 31 10:00 Istanbul t |
| CH4 | A1 | R3 | linear `cmt_zom429_1`: owner: a restart gets players in; ; slack `C08R27X0EAH/1758550789.777509`: Sep 22: working fine after the rev; slack `C0880U9751A/1759265412.481909`: Sep 30 submission builds: no new w |
| CH5 | A25 | R5 | retired in revision 5: its last hop, Samuel's note on PR #471, no longer exists, and the fact is settled by one read of `ZOM-432` (Done, with his closing note `cmt_zom432_2`). The id is not reused |
| CH6 | A3 | R5 | gdocs `f_7c3e91a4d2b85f60e1a9c4`: still to do = flagged player-facin; github `harmonygames-Games/match3d#468#rc_38`: review note before the merge: the final vial models (Claire); github `harmonygames-Games/match3d#472#rc_1`: inline note under his approval, before the merge: premium strip to November (Oliver) |

### Trap register

| Trap | Family · mech | Req | Expected wrong reading | Resolver (deciding record) | Pointer |
|---|---|---|---|---|---|
| T1 | done_gap · A24 | R2 | Collect & Win's client PRs #468/#470/#472 merged before the Sep 30 cut… | Arthur's inline review note on #470 (left with his approval, just before the merge) says the group wi… | `harmonygames-Games/match3d#470#rc_10` |
| T2 | superseding · A11 | R4 | Robert, the Product owner, approved Martin's Halloween one-off in Plag… | Robert's later message in his DM with Julia takes the approval back (a top-level message since revision 4; since revision 9 it says "the themed prop set I okayed in Martin's thread", so a 'Halloween' search returns only the approval)… | `933cee9f6464a80e4b1f05259b595b20` |
| T3 | exact_predicate · A17 | R1 | the beats are the events everyone lists (Leonard's beta pipeline, the … | the brief's scope (an event window, a reset or a start push) brings in the quest rollover and the daily gift, which the brief ties to Login Calendar on the push sheet as the same beat; with Frederick's follow-up keeping Zombie Lane off (T15), the calendar has seven beats | `f_7c3e91a4d2b85f60e1a9c4` |
| T4 | authority · A15 | R6 | pushes marked Ready in the push sheet go out as written… | the 1-day lapse and D0-1 FTUE rows still call the game 'Puzzles vs Zombies'; und… | `f_7c3e91a4d2b85f60e1a9c4` |
| T5 | authority · A15 | R6 | the Plague Race start push is Ready, so it goes out with each race… | the brief sends a push only if its row is Ready and LIVE; the sheet's second column 'Status (NA, WIP, LIVE)' reads WIP for the Plague Race start and Weekly Leaderboard reset rows, so both are held on that status (not a claim about client wiring: the base client already schedules them locally) | `f_7c3e91a4d2b85f60e1a9c4` |
| T6 | reuse_exclusion ·  | R7 | file a new ticket for the beta calendar… | ZOM-78 'Event Calendar For Zombie Match 3D' already exists (Backlog) and Frederi… | `cmt_zom78_1` |
| T7 | superseding · A1 | R3 | ZOM-429's owner note says a restart gets players into the new week and… | Vincent's Sep 30 prod re-test on the 0.3.49 submission build, a root post in #zo… | `cmt_zom429_1` |
| T8 | superseding · A14 | R8 | Brian's Season Pass handoff commits the November config for Wed Oct 29… | Brian's later mail (another thread) moves it to Fri Oct 31 10:00 Istanbul time… | `julia.lawson@harmonygames.co/<CAPT--p4sBC8XnaA7qBDMtZkWqJPiXP0MT3deOQGPusOZhHF+vo@mail.gmail.com>` |
| T9 | unit_or_timezone · A19 | R8 | Fri Oct 31 10:00 is before the Nov 1 season opening, so the config is … | the brief locks config 24 h before the season opens at Nov 1 00:00 UTC, i.e. Fri… | `f_7c3e91a4d2b85f60e1a9c4` |
| T10 | completion_elsewhere · A25 | R5 | Calvin's Sep 24 note on ZOM-432 says the frame is the last piece still needed, so the daily login beat still needs it… | a trap in name only since revision 5: ZOM-432 is Done and Samuel's closing note on the ticket itself (Sep 30 21:07:26Z) says the frame went out with PR #471 and is in both of the day's submission builds, so one read of the ticket settles it and a run that lists open issues never meets it; the family and mechanism id are kept for id stability only… | `cmt_zom432_2` |
| T11 | tool_surface · A3 | R5 | merged live-ops PRs with an APPROVED review or only CodeRabbit notes l… | Arthur's inline review note on #468, before its merge (the final vial models, Claire), and his inline note under his approval of #472, six seconds before that merge (premium strip to the November range, Oliver); weaker since revision 8, one per-PR call type returns both; through revision 3 these sat on #370 and #438… | `harmonygames-Games/match3d#468#rc_38` |
| T12 | distractor · scope_adjacent (a graded cross_reference_gap · A13 trap through revision 4) | R5 | the open quests card and the push row's 'Revisit once new quests roll out' mean Quests waits for a new quest set, so it gets a still-to-do… | Leonard's note on that card: more quests and the reward balance go in with the Mon Oct 13 rollover if they are ready and the weekly rollover does not wait on them, so nothing has to land before the beat runs. Ungraded since revision 5: no slot reads the Quests still-to-do cell… | `68dac8204f1e9a3b7c2d5e61` |
| T13 | superseding · A1 | R1 | Leonard's beta pipeline lists Infinite HP Boss Mode, so Boss Arena is … | Frederick's brief keeps Boss Arena off this calendar until the pivot call… | `f_7c3e91a4d2b85f60e1a9c4` |
| D1 | distractor · stale_summary | R2 | 'feature completed Win and Collect' means Collect & Win is ready for p… | a dev-side status; the server windows are not on prod (T1)… | `C05KNDCHAAG/1758558302.777379` |
| D2 | distractor · partial_listing | R1 | the beta pipeline's named features are the whole calendar… | the brief's scope adds the rollovers (T3)… | `C05KNDCHAAG/1757704290.799329` |
| D3 | distractor · keyword_collision | R1 | Martin's 'Halloween theme for an app icon' is a live-ops beat… | an app icon is not a window, reset or push; only the one-off event matters, and … | `C08R8CHB0QL/1758121809.236839` |
| D4 | distractor · other_title | R6 | the PN BETA Translated tab's rows (Domino Adventures, River Rush, Tile… | the brief says beta pushes are English-only from PNs Beta; the translated tab is… | `f_a325dd4af80afc5994d5dc` |
| D5 | distractor · lookalike_entity | R6 | 'Win & Collect' (the Domino Delights name on the push row and the road… | the ZM3D event is Collect & Win; under the copy rule the row would be held even … | `f_a325dd4af80afc5994d5dc` |
| D6 | distractor · scope_adjacent | R1 | Boss Arena's endpoints are ready and Axe Arena is on the roadmap, so b… | Boss Arena is off until the pivot call (brief) and Axe Arena is postponed for th… | `C08R6BF4ENN/1756747348.667629` |
| D7 | distractor · scope_adjacent | R3 | the Sep 30 Season Pass shader fault thread holds Season Pass or adds a shader fix to its still-to-do… | a shader defect is cosmetic, so Season Pass runs, and since revision 10 Vincent, who raised it, says Oliver pushed the fix and nothing has to land for the beta… | `C08R27X0EAH/1759249488.495439` |
| D8 | distractor · scope_adjacent | R3 | the unexplained Endless heating fault thread holds Endless… | a performance/heating issue does not stop players entering, scoring or claiming;… | `C08R27X0EAH/1758145553.265559` |
| D9 | distractor · scope_adjacent | R1 | the Zombie Lane fix verified only on Android makes Zombie Lane a held beat or a calendar row… | the thread no longer decides any calendar status: Zombie Lane is not on this calendar at all (Frederick's follow-up, T15), so there is neither a hold nor a still-to-do row to write for it | `C08R27X0EAH/1758903616.346579` |
| T14 | exact_predicate · A17 | R5 | ZOM-465's master ticket struck 'Idle Icon Animation for all event icon… | Marcus's later note on the same ticket says the Collect & Win icon animation is still to do, Brian says there that it has to land (since revision 11), and the three animation PRs (#454/#456/#475) agree; weaker since revision 4, both notes come back from one per-issue call… | `cmt_zom465_2`, `cmt_zom465_3` |
| T15 | superseding · A14 | R6 | the brief is read as the whole rulebook: its push rule is applied to whatever a run takes a beta push to be (all 14 PNs Beta rows, only the Push Notification rows, or only the Ready ones), copy that names no game fails the naming rule, and Zombie Lane is listed with the other live-ops… | Frederick's thread reply under his own ask (one thread-open from the root, which shows `reply_count` 1): plan the tab one line per row, local notifications included, leave off exactly four rows (Hourly Coins, Nathan's Treasure Hunt, Streak Fever, Axe Arena); copy that names no game may go out; keep Zombie Lane off the calendar — ten push rows, seven beats | `890dc27f56e8501bd7590ffdfc231057` |
| D10 | distractor · scope_adjacent | R3 | the queue manager (ZOM-543 In Progress; #459 orders only level_end/dai… | the queue manager orders panel animations additively ('we'll add its order'); an… | `ZOM-543` |
| D11 | distractor · scope_adjacent | R3 | #473 migrated Season Pass to Addressables (Arthur asked for every live… | Addressables is a load-time optimization, not an enter/score/claim blocker and n… | `harmonygames-Games/match3d#473` |

Supersession families (`superseding`/`effective_date`) carry ordered `version_records`; the `hardness_v2_check` SAME_PLACE check is CLEAN for the five revision-1 supersessions (every correction sits in a different container from the claim it beats — `slack:C08R8CHB0QL/1758121809.236839` vs `slack:D05GU6L0XFH/1759270241.638119`). T15, added in revision 2, is the exception: its version records run from the brief (`f_7c3e91a4d2b85f60e1a9c4`, Sep 24) to Frederick's reply (`slack:D05SD5QLG94/1759263878.305129`, Sep 30), and the reply sits in the anchor's own thread. Re-run on the revision-2 manifest on 2026-11-06, the check flags it: SAME_PLACE T15 (`first_read`), the correction sits in the container of anchor A1. The flag is accepted, not designed away; §9 states what it means for the landing rate and §18 records the disposition.

## 9 · Failure-diversity plan

The 14 portfolio mechanisms (14 from revision 1 plus `R_ASK_FOLLOWUP`, added in revision 2, less `R_QUEST_SET`, retired in revision 5) flip slots on different surfaces, so runs fail different subsets through reconciliation errors that survive complete retrieval, not concealment (forecast reports the failure-pattern spread; the operative gate is largest-pattern ≤ 50%; `hev_10c8bb5be00ab2cf`, pre-registered on the 14 revision-1 mechanisms). Mapping mechanism → requirement → carrier:

| Mechanism | Req | Carrier surface (the reconciliation once retrieved) | Prior family |
|---|---|---|---|
| R_DONE_DEPLOY | R2 | merged-not-deployed / inline-470 | A24 |
| R_WITHDRAWN | R4 | approval-taken-back / robert-dm-thread | A11 |
| R_SCOPE_BEATS | R1 | resets-are-beats / brief-scope | A17 |
| R_COPY_CURRENT | R6 | old-title-held / brief-copy | A15 |
| R_WIRED | R6 | ready-but-wip / brief-wiring | A15 |
| R_TECH_HOLD | R3 | fails-after-restart / retest-reply | wrong summary + thread past its conclusion (A1) |
| R_HANDOFF_SLIP | R8 | date-moved-in-other-thread / brian-slip-mail | A14 |
| R_LOCK_BOUNDARY | R8 | lock-day-late / lock-instant | A19 |
| R_DONE_ELSEWHERE | R5 | older-note-on-closed-ticket / frame-ticket-closing-note (one ticket since revision 5; no difficulty carrier) | A25 (kept for id stability) |
| R_REVIEW_FLAGS | R5 | flag-in-inline-note / inline-review-notes (both notes pre-merge since revision 8; one call type) | A3 |
| R_HOLD_SCOPE | R3 | cosmetic-fault-not-a-hold / fault-threads | A17 |
| R_ICON_SCOPE | R5 | cw-icon-absent / icon-master-vs-prs | A17 |
| R_INFRA_SCOPE | R3 | unqueued-panel-not-a-hold / queue-manager | A17 |
| R_ASK_FOLLOWUP | R6 | amendment-in-the-ask-thread / ask-thread-reply (`slack:D05SD5QLG94/1759263878.305129`) | A14 (replies never opened) |

The heaviest single discovery is the scope rule (`R_SCOPE_BEATS`: the calendar has seven beats, and omitting the two rollovers, Quests and the daily gift, fails S04/S05/S07 and V01, 14 of the 102 weight points, ~14% since revision 5 (23 of 111, ~21%, while S06 existed and S07 weighed 5) — corrected from an earlier ~15% claim after the review; listing Zombie Lane as one more beat is now wrong as well, since V01 checks the beat keys exactly and the follow-up keeps Zombie Lane off); next are the three still-to-do review-flag slots (`R_REVIEW_FLAGS`, per-PR inline notes, `harmonygames-Games/match3d#468`), the carrier the completed-task hardening report proved lands misses. The hold rule is attacked from two independent directions — under-hold (`R_TECH_HOLD`, the cross-channel leagues re-test) and over-hold (`R_HOLD_SCOPE`, a cosmetic/perf fault read as a hold on Endless/Season Pass; Zombie Lane is no longer one of its beats) — which spread the failures. Carriers span a Slack DM thread, a cross-channel #zombie-match3d root, Gmail, GCal, a Confluence page, Linear comments and per-PR GitHub calls; every deciding record is retrievable, so the difficulty is reconciliation, not hiding.

`R_ASK_FOLLOWUP`, stated honestly. The push-plan rows (ten, with four named rows left off), the no-game-copy allowance and Zombie Lane's exclusion live in a thread reply under the ask itself. A run that reads only the DM root misses all three, and the root's `reply_count` 1 is the only pointer. Evidence for it landing: the completed `julia_zm_difficulty_baseline` task saw 3 of 6 Opus 5.5 runs miss DM thread replies. Evidence against: the reply is in the anchor's own thread, one call from the first record every run opens, and the local `hardness_v2_check` classes an anchor-thread reply as `first_read` (SAME_PLACE flag on T15). Its landing rate is therefore uncertain. On the revision-2 surface it decides only weight-3 slots (P04 and P05, the two Send rows, and V02, the exact push keys), so it also carries a DECISION_FLIP flag. It was added to settle the platform review's push-plan forks with a dated record, not to raise difficulty, and no difficulty claim in §18 leans on it.

## 10 · Deliverables

Two table deliverables in Julia's Drive, plus three message writes. Key regexes are disjoint so each table decodes its own sheet (forensics note: §13 QC rails).
- **Calendar** (table, keyed by beat): columns Beat / First window (UTC) / Weeks running / Status / Still to do (owner); class column Status ∈ {Run, Hold}. Seven beats: Plague Race, Collect & Win, Season Pass, Endless Monster Mode, Weekly Leagues (Weekly Leaderboard), Quests and the daily gift (key "Daily Login"). Zombie Lane, the Halloween one-off, Boss Arena and Axe Arena are not rows. Since revision 10 Quests and the daily gift read All four weeks under Weeks running. Since revision 12 Weekly Leagues reads Mon Oct 6 00:00 UTC and All four weeks on its held row, and Season Pass's First window reads Mon Oct 6 00:00 UTC under the clip sentence. Julia-owned sheet in her 'ZM Live Ops' folder, Calendar tab (`f_e4a17c90b3d25f6a8c1d73` in `d_5f2c8e1b7a94d03c6e2b58`).
- **Pushes** (table, keyed by push): key column Push name, then Send (UTC or trigger), Send or hold and What is missing, as the seeded tab has them since revision 9; class column Send-or-hold ∈ {Send, Hold}. Ten rows: every PNs Beta row except Hourly Coins, Nathan's Treasure Hunt, Streak Fever and Axe Arena, which must not be listed (`slack:D05SD5QLG94/1759263878.305129`). Two Send (Lives recharged, 7-day lapse) and eight Held. The Pushes tab of the same Julia-owned sheet (`f_e4a17c90b3d25f6a8c1d73`).
- **Recommendation** reply in Frederick's DM (`slack_send_message` to `D05SD5QLG94`).
- **Calendar link** on `ZOM-78` and a **hold note** on `ZOM-429` (`linear_create_comment`, unscoped). Weekly Leagues is the only held beat, so `ZOM-429` carries the only ticket note; Collect & Win starts late and is not held, so it gets none.
- **Reply to Brian** on the Season Pass November config (`gmail_reply_to_message`, `julia.lawson@harmonygames.co/1844311412966040123`); the trigger is the brief's "you tell its owner in a reply on the mail where they committed to it".

## 11 · Service role map

10 services carry weight, each with its own fact (companion-only rows are counted separately, §16); an eleventh, Trello, is injected and carries none since revision 5. Each row names the service's weight reason.

| Service | Role | Weight reason |
|---|---|---|
| slack | the ask and its thread follow-up, the one-off approval and its withdrawal, the prod re-test, fault threads, the reply | Frederick's ask is the anchor and the reply destination (R7); Robert's #zombie-art approval and his later message in his |
| gdocs | Frederick's beta brief: the calendar owner's rules | the scope, deploy, hold, one-off, still-to-do, push and lock rules (R1-R6, R8) live only here |
| gslides | Frederick's beta UA plan | the four buy weeks that set the calendar's span (R9) |
| gmail | Brian's Season Pass November handoff | Brian's Sep 22 date and his Sep 26 slip to Fri Oct 31 10:00 Istanbul time decide the November config deadline  |
| gcal | Douglas's backend release plan event | the Wed Oct 8 release date fixes Collect & Win's first prod window (R2) |
| gdrive | Julia's ZM Live Ops folder | holds Julia's calendar sheet, the write target (R7) |
| gsheets | the push sheet and Julia's calendar sheet | the PNs Beta rows (status, live state, copy) decide every push (R6); Julia's sheet carries the column contract and |
| linear | open live-ops issues, owner notes, the calendar ticket | per-issue notes decide holds and still-to-do (R3, R5; Marcus's second note on ZOM-465 carries the Collect & Win icon |
| github | live-ops PRs, their reviews and comments | Arthur's inline note on #470 holds Collect & Win's server windows to the backend release (R2); his inline notes on #468 and #472 add the vial and premium-strip still-to-dos (R5) |
| trello | the open quests roadmap card and Leonard's note on it | no weight since revision 5: the note decides no graded value (T12, ungraded); the schema is still injected |
| confluence | the base Season Pass spec page (nothing is injected) | `page_season_pass_spec` is the only source of the config-lock offset ('locked 24h before each season opens') that the Fri Oct 31 00:00 UTC lock needs (R8); on the required path since the brief stopped stating the offset, declared in revision 5 |

## 12 · Call budget

Unconditional floor **154** counted calls over 10 services (103 in the per-record phase) since revision 8 (193 / 142 in revisions 6 and 7, 194 / 143 in revision 5, 192 / 140 in revision 4); the requester-confirmed `volume_exception` floor is 130/75, so both floors hold. Revision 4 moves the revision-2 total of 200 as follows: −5 per-record calls for the five tickets the SQL closes, −1 for the thread-open call the retraction no longer needs, −2 for the separate read of PR #471, which nothing requires once ZOM-432 is Done (Samuel's note still came back with the per-PR conversation call). Revision 8 moves the revision-7 total of 193 by −39: the conversation surface carries nothing a rule uses any more (§5). Revision 6 moves the revision-5 total of 194 by −1: `ZOM-387` left the cohort, so its per-issue comment read goes. Revision 5 moves the revision-4 total of 192 as follows: +3 per-record calls for the three tickets that are open again, −2 for the two Trello calls no graded value needs any more, +1 for the Confluence read of the Season Pass spec, which was on the required path and had not been counted. Revision 2 moves the revision-1 total of 208 as follows: +1 discovery call to open the ask's thread, and −9 for reads that existed only for Zombie Lane, now off the calendar (one issue and two PRs out of the cohort, so −1 and −6 per-record calls; the backend PR #10; the Zombie Lane fault thread). The rows below follow the revision-8 draft manifest. Conditional rows (unverified tool behaviour) count 0. Largest share outside the per-record phase ≤ 50% (gate `call_budget_spread`, last run on the revision-1 budget).

| Phase | Service | Calls | Why necessary |
|---|---|---|---|
| discovery | slack | 1 | read Frederick's ask in his DM with Julia (anchor A1: scope of the work, destination |
| discovery | slack | 1 | open the ask's thread (the root shows reply_count 1): Frederick's follow-up sets the push-plan rows and keeps Zombie Lane off the calendar (R6, R1) |
| discovery | gdrive | 1 | find the brief the ask names and Julia's calendar sheet (no links are posted) |
| discovery | gdocs | 1 | read Frederick's beta brief: every rule the calendar applies (R1-R6, R8) |
| discovery | gslides | 2 | find and read the UA plan the brief names for the buy weeks (R9) |
| discovery | gmail | 2 | search Brian's Season Pass handoff and read the thread (R8) |
| discovery | gcal | 2 | list Julia's events in the span and read the backend release event (R2) |
| discovery | gsheets | 3 | push sheet metadata and the PNs Beta tab (R6); Julia's calendar sheet header (R7) |
| discovery | linear | 1 | find the calendar ticket the ask names (ZOM-78, R7) |
| discovery | confluence | 1 | find the Season Pass spec page and read its config-lock rule ('locked 24h before each season opens'), the offset the brief's 'before its lock' points to (R8); first counted in revision 5 |
| enumeration | linear | 3 | list open ZOM issues (96 open since revision 9, 99 in base: 2 pages) and search the beat terms the titles use |
| enumeration | github | 4 | list the live-ops PRs merged Jul 1 - Sep 30 (search + pages); 210 merged, 39 in-scope |
| enumeration | github | 5 | list the match3d-backend cross-repo PRs and read #16/#19/#26/#34: leagues / endless server state (#10 is Zombie Lane only, off the calendar: not read) |
| enumeration | slack | 9 | #zombie-bugs Sep 15-30 (3 pages), #zombie-design (2), #zombie-match3d (2), #company-internal (1), #builds Sep 30 submission posts (1) |
| per-record | linear | 18 | linear_list_comments on each of the 18 open live-ops issues (cohort surface 1; base Linear holds 0 comments; the two closed tickets and ZOM-387, out of the cohort since revision 6, are not read) |
| per-record | github | 39 | github_get_pull_request_reviews on each of the 39 in-scope PRs (surface 2; certify no open change-request blocker per PR) |
| per-record | github | 39 | github_get_pull_request_comments on each of the 39 PRs (surface 3, inline review notes) |
| per-record | github | 7 | commit-list reads on the body-empty PRs (#296/#317/#400/#408/#419/#471/#475): the de |
| authorities | slack | 2 | #zombie-art Halloween thread replies (1); Robert's DM history, where the retraction is a top-level message (1) |
| reconciliation | slack | 6 | open the 6 open live-ops fault threads whose deciding last reply carries no beat keyword; the Zombie Lane thread is not needed (off the calendar) |
| writes | gsheets | 3 | write the Calendar and Pushes tabs, then read the sheet back |
| writes | slack | 1 | reply to Frederick in his DM with the recommendation (R7) |
| writes | linear | 2 | link the calendar on ZOM-78; note the leagues hold on ZOM-429 (R7) |
| writes | gmail | 1 | reply to Brian that the November config must land before the lock (R8) |
| enumeration | github | 10 | files of the 10 shared-title PRs (icons, queue manager) to tie a flag to a beat *(conditional, counts 0)* |

## 13 · QC rails

- **The still-to-do rule is closed** (revision 9, re-worded in revision 10): its fix if a beat is held, and anything flagged since the brief as still needed for it (prod deploy, config or player-facing art). Nothing else goes in: not what already shipped, not analytics, not polish nobody flagged. Every still-to-do value in `solver/truth.json` already fits it (dossier §11 Revision 9 and Revision 10).
- **No graded fact rests on Snowflake or backend code** — context only, never cited (Pre-Scenario §5.5). Confluence carries one graded dependency: the 24 h config lock on the base `page_season_pass_spec`, which the Season Pass config deadline needs (§11); `page_liveops_calendar` stays context. No Plague Race or Endless window dates are graded (the warehouse's 5-day series and an unverified backend lead disagree; `page_liveops_calendar`).
- **Boundaries accepted in full**: row layout (one row per beat or window), labels, PT or UTC renderings of the same instant, order of the recommendation; owner names only where a record names one (`cmt_zom429_1`).
- **Writes the rubric will not loosen**: the reply goes in the DM not a channel; the link goes on `ZOM-78` not a new ticket; a failing push is held, not rewritten in place. Since revision 2 also: the push plan has the ten rows Frederick's follow-up sets and none of the four he left off; Zombie Lane is not a calendar row; Collect & Win is a late start, not a hold; the only ticket note is the held beat's, on `ZOM-429` (`slack:D05SD5QLG94/1759263878.305129`, `f_7c3e91a4d2b85f60e1a9c4`).
- **Local-grader forensics note (not a platform rule)**: the two table deliverables use disjoint, case-insensitive key regexes (beats vs push names) and disjoint title patterns ('calendar' vs 'push'), so each decodes its own sheet even when both are seeded; a run that writes both tabs into one spreadsheet at overlapping A1 ranges is hand-normalized in `/create-hardening` (`f_e4a17c90b3d25f6a8c1d73`). Likewise the local `surface_grader` regex is an advisory forensic proxy only: the platform rubric (09) is authoritative for decision polarity, timezone, destination-issue binding and deliverable completeness (the regex matches the decision keyword, not its negation/instant/owner), so the measured difficulty at `/create-difficulty` rests on the rubric verdicts, not on these regexes.
- **Known-issue cards kept off the path**: SC-13/14/18/38/62/68 are near but never required or cited (`f_a325dd4af80afc5994d5dc` is the only required sheet, used for English `PNs Beta` copy only). SC-15 (the `ZOM-521` checklist against its open children) is the one card the task touches: repaired in revision 3 and not graded (§2).

## 14 · Reach table (load-bearing records)

Every scoped load-bearing id re-verified with `persona_view can-see julia_lawson` (base = YES; planned seeds = UNVERIFIED (U4), verified at the injection gate). Linear / GitHub / Trello are unscoped (always readable).

| Record | Service | Visibility path | LB |
|---|---|---|---|
| `slack:C08R8CHB0QL/1758121809.236839` | slack | YES — member of #zombie-art | LB |
| `slack:C08R27X0EAH/1758546048.524829` | slack | YES — member of #zombie-bugs | LB |
| `slack:C08R27X0EAH/1758546119.789009` | slack | YES — member of #zombie-bugs | LB |
| `slack:C05KNDCHAAG/1757704290.799329` | slack | YES — member of #company-internal | LB |
| `slack:C05KNDCHAAG/1758558302.777379` | slack | YES — member of #company-internal | LB |
| `slack:C090N54TG79/1758517286.431379` | slack | YES — member of #zombie-design | LB |
| `slack:C05433XK267/1759263189.219529` | slack | YES — member of #builds (since revision 5 it only agrees with the closing note on ZOM-432, which decides the frame) | LB |
| `slack:C0880U9751A/1759265412.481909` | slack | UNVERIFIED (U4; if injected, use check-sql) — planned seed: Vincent's cross-channel leagues re-test root (channel C0880U9751A is a Julia-visible base channel) | LB |
| `slack:D05SD5QLG94/1759263878.305129` | slack | UNVERIFIED (U4; if injected, use check-sql) — seed added in revision 2: Frederick's thread reply under his ask (D05SD5QLG94 is Julia's own DM with him; check-sql on the revision-2 SQL returns YES) | LB |
| `f_a325dd4af80afc5994d5dc` | gsheets | YES — shared with Julia (base push sheet) | LB |
| `d_8140f09bf9f1b94cb8ee2d` | gdrive | YES — Julia's own Drive root | LB |
| `ZOM-78` | linear | YES — unscoped service | LB |
| `ZOM-429` | linear | YES — unscoped service | LB |
| `harmonygames-Games/match3d#470` | github | YES — unscoped service | LB |
| `page_season_pass_spec` | confluence | YES — unscoped service (the base Season Pass spec page: the 24 h config lock; replaces the Trello quests card, which decides nothing since revision 5) | LB |
| `f_7c3e91a4d2b85f60e1a9c4` | gdocs | UNVERIFIED (U4; if injected, use check-sql) — planned seed: Frederick's brief | LB |
| `f_2b9d4e7a1c63f08d5e7b21` | gslides | UNVERIFIED (U4; if injected, use check-sql) — planned seed: UA deck | LB |
| `f_e4a17c90b3d25f6a8c1d73` | gsheets | UNVERIFIED (U4; if injected, use check-sql) — planned seed: Julia's calendar sheet | LB |
| `d_5f2c8e1b7a94d03c6e2b58` | gdrive | UNVERIFIED (U4; if injected, use check-sql) — planned seed: ZM Live Ops folder | LB |
| `evt_9a4c2e7f1b3d58e06c7a2f` | gcal | UNVERIFIED (U4; if injected, use check-sql) — planned seed: Oct 8 release | LB |
| `julia.lawson@harmonygames.co/1844311412966040123` | gmail | UNVERIFIED (U4; if injected, use check-sql) — planned seed: Brian's slip thread | LB |

## 15 · Record plan for /create-injection

What `/create-injection` must seed (≥ 10 services; companions counted separately). Each row carries its planned or base pointer.

| Service | Seeds | Pointer |
|---|---|---|
| Slack | Frederick's ask DM and his thread reply under it (D05SD5QLG94/1759263878.305129; the root carries reply_count 1); Robert's #zombie-art approval reply + his DM withdrawal (a top-level DM message since revision 4); Vincent's Sep 30 re-test root in #zombie-match3d (C0880U9751A/1759265412.481909); since revision 9 two replies in #zombie-bugs (Leonard's S23 Ultra re-run and, since revision 10, Vincent's close of the shader thread) since revision 10 Robert's reply in Martin's desert thread, and since revision 11 Douglas's reply in the #zm-collect-win reward-table thread, which decide no value | `slack:D05SD5QLG94/1759263617.418209` |
| gdocs | Frederick's beta brief (rules R1-R6, R8), shared with Julia | `f_7c3e91a4d2b85f60e1a9c4` |
| gslides | Frederick's beta UA plan deck (the four buy weeks) | `f_2b9d4e7a1c63f08d5e7b21` |
| gcal | Douglas's backend release plan event Wed Oct 8 + per-attendee copies + INT-11 invitation mails | `evt_9a4c2e7f1b3d58e06c7a2f` |
| gmail | Brian's Oct 29 handoff thread and his Oct 31-Istanbul slip thread (Frederick cc) | `julia.lawson@harmonygames.co/1844311412966040123` |
| gdrive+gsheets | Julia's 'ZM Live Ops' folder; her calendar sheet and push sheet (owner Julia in both rows) | `d_5f2c8e1b7a94d03c6e2b58` |
| linear | owner notes on the open live-ops issues (e.g. Douglas on ZOM-429); the ZOM-78 reuse comment; since revision 3 a second, later note from Brian on ZOM-526 (`cmt_zom526_2`) and the ZOM-521 description with its two open items unticked (the SC-15 repair, §2); since revision 4 Marcus's second note on ZOM-465 (`cmt_zom465_2`), five tickets closed Done and two moved to In Progress so that each state followed the ticket's own note; since revision 5 only two are closed (ZOM-344, ZOM-432, the second by Samuel's closing note `cmt_zom432_2`), ZOM-566 is In Progress, ZOM-565 / ZOM-471 / ZOM-542 are open again (ZOM-542 Todo since revision 11, the other two in their base states) and ZOM-387 carries no seeded note; since revision 6 a third note on ZOM-526 (`cmt_zom526_3`) since revision 7 a second note on ZOM-521 (`cmt_zom521_2`), and since revision 9 a second note on ZOM-534 (`cmt_zom534_2`), Brian's note on ZOM-566 (`cmt_zom566_1`, with Owen's now `cmt_zom566_2`) Vincent's closing note on ZOM-563 (`cmt_zom563_2` since revision 12, after Douglas's `cmt_zom563_1`), and since revision 10 Brian's note on ZOM-565 (`cmt_zom565_2`), none of which decides a value; since revision 11 Brian's note on ZOM-465 (`cmt_zom465_3`), a deciding record of the Collect & Win icon item | `cmt_zom429_1` |
| github | Arthur's inline note on #470, inside his base approval review since revision 5; his review note on #468, left before its merge, and since revision 8 his inline note inside his base approval of #472, also before its merge (revisions 4 to 7: a conversation note on #473; through revision 3 these were post-merge notes on #370/#438); no note on #454 since revision 4 and none on #471 since revision 5 | `harmonygames-Games/match3d#470#rc_10` |
| trello | Leonard's note on the open quests card #61 (more quests and the reward balance from Oct 13 if they are ready, the weekly rollover does not wait on them); decides no graded value since revision 5 | `68c452a03006277f55d9dc96` |

Every seed lands at or before `2025-10-01T00:00:00Z` and after the base events it names (chronology in Pre-Scenario §5.6). Planned ids are collision-checked free (R-C §7): next free Linear key `ZOM-567`; the `#470` inline-comment suffix `#rc_10` is the next free one on that PR (the `#471#c_18` note is gone since revision 5).

## 16 · Integrations and companions

Companion rows (counted separately from the 10 services) and the `integrations.json` sources that mirror each seeded record. `#zombie-prs` (C093LEZGF6J) is NOT visible to Julia, so any GitHub→Slack mirror is a companion, never evidence.
- github → Slack mirror of a PR comment: `INT-01` (GitHub Slack app) — companion in `#zombie-prs`, not load-bearing. Injection constraint (H3, `research/H3_reviewblocker_companion_audit.md`): the base INT-01 mirror carries the FULL comment body verbatim; because Julia is NOT a member of #zombie-prs (ACL), `/create-injection` seeds the faithful INT-01 mirror for integration parity (suppressing it would make the seeded comment the only PR comment without a mirror); it stays non-load-bearing by the ACL, not by suppression, and the deciding text goes in `review_comments` (human `reviews.body` are empty in this cohort).
- github → Gmail notification of a PR comment: `INT-12` — companion in Julia's mailbox.
- linear → Slack DM notification of an issue comment: `INT-04` — a generic 'commented on' notice, no comment text.
- gcal → invitation / update / RSVP mails for the Oct 8 release event: `INT-11` — per-attendee companion mails.
- gdrive → Slack app DMs (shares, comments): `INT-13` — companion when the brief/sheet is shared.
- slack → Slack email notifications: `INT-22` — companion, never required.
- github CodeRabbit reviews: `INT-23` — base bot content on every PR, never the deciding human note.
- trello → Slack: `INT-21` — NO integration exists; no companion for the quests-card comment.
- gdocs / gslides / gsheets: no dedicated integration source beyond the gdrive share (INT-13); no companion of their own — none.
- gmail: a destination of INT-11/INT-12, not a source; no companion of its own — none.

## 17 · Red team

RED TEAM FALLBACK: the dual red team ran as two independent GPT-6.1 Sol subagents (an adversarial `redteam` pass and a `methodologist` pass) on this design and the draft manifest, because no `REDTEAM_*` environment is configured; their findings and dispositions are recorded in `01b_Redteam_Review.md` and `01b_Redteam_Review.second.md`, and the requester approved this fallback (decision D4). See §18 for the disposition of every finding.

## 18 · Self-review

Hardness gate (re-run verbatim head; the stage gate re-runs and must agree):

```text
HARDNESS GATE (extreme (design)): PASS
```

Hardness v2 (Opus 5.5) self-checks (advisory; `research/hardness_v2_check_design.txt`): SAME_PLACE, DONE_CHECK, TWO_DECISIONS, INPUT_CHECK, FILTER_CHECK all CLEAN; DECISION_FLIP FLAG on `R_COPY_CURRENT`, `R_WIRED` and `R_HOLD_SCOPE` (each flips only weight-3 slots). Disposition: all three are intentionally secondary interpretation-band (weight-3) mechanisms whose honest work kind is applying one stated rule to one row — `R_COPY_CURRENT` (old-title copy rule, P01/P02/P06), `R_WIRED` (the second 'Status (NA, WIP, LIVE)' column, P03 Plague Race start and P07 Weekly Leaderboard reset, both Ready-but-WIP and held on that status) and `R_HOLD_SCOPE` (the over-application twin of the hold rule, flipping the Endless and Season Pass 'runs' samples C02 and C04 when a run over-holds a cosmetic/perf fault; C03, the Zombie Lane sample, left the surface with the beat in revision 2). Raising any of their weights would violate the QC weight-by-work-kind rule. Re-run on the revision-2 manifest and surface on 2026-11-06 (console output, not yet saved under `research/`): SAME_PLACE is now a FLAG, on T15 only (`first_read`: the correction sits in the container of anchor A1); DECISION_FLIP flags `R_COPY_CURRENT`, `R_WIRED`, `R_ASK_FOLLOWUP`, `R_HOLD_SCOPE` and `R_INFRA_SCOPE` (weight-3 slots only; 10 of the 15 rules flip a weight-5 slot); DONE_CHECK, TWO_DECISIONS, INPUT_CHECK, FILTER_CHECK and RULE_IN_PROMPT (on the 100-word prompt) are CLEAN. Disposition of the two new flags: T15 / `R_ASK_FOLLOWUP` is the requester's own scope note in his own thread, added to settle the platform review's push-plan forks with a dated record; it is accepted as `first_read` and weight 3, and is not counted as a difficulty carrier (§9). The weight-5 difficulty is carried by the nine reconciliation mechanisms that DO flip weight-5 slots (R_DONE_DEPLOY, R_WITHDRAWN, R_SCOPE_BEATS, R_TECH_HOLD, R_HANDOFF_SLIP, R_LOCK_BOUNDARY, R_DONE_ELSEWHERE, R_REVIEW_FLAGS, R_QUEST_SET - retired in revision 5); these three add distinct failure patterns — an over-hold direction independent of the under-hold R_TECH_HOLD — at weight 3.

Trap liveness (advisory; `research/trap_liveness_design.txt`): breadcrumb flags on T3, T4, T5, T6, T9, T11, T13 and an order flag on T6.

| Flag | Disposition |
|---|---|
| T4/T5 breadcrumb (brief) | Intended — the brief (`f_7c3e91a4d2b85f60e1a9c4`) is the rulebook the ask names; an authority must be findable. The difficulty is applying its rule against a convincing wrong reading elsewhere (Ready flags, merged PRs), not hiding the brief. |
| T3/T9/T11/T13 breadcrumb | The flagged record is the brief or a base pipeline post one hop from the hub; the deciding records that beat each trap sit deep (per-PR inline notes `harmonygames-Games/match3d#470`, a DM thread reply, a UTC computation). |
| T6 breadcrumb + order | Intended — the ask names the calendar ticket (`ZOM-78`); reuse-vs-new is a weight-1 destination check, not a difficulty carrier. |
| T15 (added in revision 2; trap liveness not re-run) | Flagged `first_read` by the SAME_PLACE check above: the reply sits in the anchor's own thread (`slack:D05SD5QLG94/1759263878.305129`). Intended — it is the requester's own scope note, placed where he would put it; it settles the platform review's push-plan forks and is not counted as a difficulty carrier (§9). |

Forecast (pre-registered `hev_10c8bb5be00ab2cf`, UNCALIBRATED, frozen to the revision-1 manifest+surface and not re-run for revision 2; `research/hardness_forecast_design.txt`): E[avg] 0.660-0.672, P(all four difficulty gates) 0.479-0.533 - E[avg] is comfortably under the 0.77 goal bar, but P(all) STRADDLES the 0.5 bar (independent 0.479, correlated 0.533). After the round-3 repairs this matches the round-2 borderline (0.658/0.520): the enrichment added length (the 47-member cohort, ~255 evidence units, >=150 unbatched reads) and one clean weight-5 reconciliation (the S11 Collect & Win icon scope gap on `R_ICON_SCOPE`), but did NOT raise the forecast difficulty - the apparent gain in an earlier draft came from an over-reaching `R_INFRA_SCOPE` attribution that both reviewers correctly flagged, now narrowed to one honest over-hold (Plague Race via the un-queued queue-manager panel). The LIMITER is the SD-band gate (expected six-run SD ~0.106, just above the 0.10 floor), not the difficulty: E[avg] 0.66 clears avg < 85% with ~0.99 probability. Binding risk (both independent reviewers, `01b_Redteam_Review.md` / `01b_Redteam_Review.second.md`): four mechanisms (R_WITHDRAWN A11, R_LOCK_BOUNDARY A19, R_REVIEW_FLAGS A3, R_QUEST_SET A13, retired in revision 5) have no Opus 5.5 ledger record and sit on a flat Beta(1,1)=0.50 prior (~33/108 of the weight); the methodologist's independent sensitivity (those four at ~10%) gives E[avg] ~0.756 and P(all) ~0.480, so a thorough Opus that reconciles the retrieval-bound carriers could clear the 85% cap. The enrichment does not by itself turn retrieval VOLUME into harder performance (both reviewers): more records can aid enumeration as much as burden it, so the ~50% miss on the flat-prior carriers is an unhedged assumption, not a proven bigger-haystack fact. This is UNCALIBRATED and resolved only by the six real Opus 5.5 baselines at `/create-difficulty`; first-time pass is a coin-flip on the SD gate. The difficulty rests on reconciliation that survives complete retrieval - the deploy/lock computations (S01/S10), the cross-channel leagues re-test (S03), the certify-absence review clause, the icon scope gap (S11: ZOM-465 struck 'all icons' done vs #454/#456/#475 omitting C&W, reachable via EITHER Marcus's second note on ZOM-465 (his #454 note through revision 3) OR the #456 enumeration, so it fails only when both are missed), and two over-application patterns over DISJOINT beats (fault-thread `R_HOLD_SCOPE` on Endless/SP, Zombie Lane having left the calendar in revision 2; infra-gap `R_INFRA_SCOPE` on Plague Race; the addressables/#473 and token/ZOM-526 tickets are retrieval-context distractors, not graded) - not concealment. Highest predicted all-six-fail: S10 0.25 (Season Pass config), S06 0.21 (quests Oct 13 rollover), S08/S09 0.15 - all reachable (`julia.lawson@harmonygames.co/1844311412966040123`, `6851a724601a61857a1b202f`); VALID all-fail workload if they occur, not a block - for `/create-allfail`.

### Two-reading tests (decision points)

| # | The two readings | What decides |
|---|---|---|
| 1 | Merged client PRs 'done' vs live on prod | the deploy rule + Arthur's #470 inline note + the Oct 8 release event → Fri Oct 10 00:00 UTC (`evt_9a4c2e7f1b3d58e06c7a2f`) |
| 2 | Robert's thread approval vs his later DM | the later call by the same Product owner stands (`slack:D05GU6L0XFH/1759270241.638119`) |
| 3 | Ready flag vs the copy rule | held for the copy owner; 'send with corrected copy' is not accepted (`f_a325dd4af80afc5994d5dc`) |
| 4 | The obvious event list vs the brief's scope | the brief governs; the two rollovers are in (`f_7c3e91a4d2b85f60e1a9c4`) |
| 5 | Restart-clearing faults vs the hold rule | ZOM-534/556 are known issues, not holds (`ZOM-534`) |
| 6 | Douglas's restart note vs Vincent's cross-channel prod re-test | the later #zombie-match3d prod re-test decides; leagues held (`slack:C0880U9751A/1759265412.481909`) |
| 7 | Lock day vs lock instant | Oct 31 07:00 UTC is 7h late vs the Oct 31 00:00 UTC lock (`julia.lawson@harmonygames.co/1844311412966040123`) |
| 8 | Calvin's Sep 24 note on ZOM-432 (frame still needed) vs the frame shipped | the ticket was closed Done after Samuel's #471 note: the frame is in both submission builds, iOS 50 and Android 135 → nothing left (`harmonygames-Games/match3d#471`) |
| 9 | Collect & Win held until its first prod window vs a late start | the brief's late-start sentence "A beat whose server windows are waiting on that release starts late, it is not held." → Runs, first window Fri Oct 10 00:00 UTC, no ticket note (`f_7c3e91a4d2b85f60e1a9c4`) |
| 10 | The push plan as a run's own pick of which rows are beta pushes (all 14 PNs Beta rows, the Push Notification rows only, or the Ready rows only) vs the rows Frederick names | his thread reply under the ask: the tab as it stands, one line per row, local notifications included, four named rows left off → ten rows, two of them Send (`slack:D05SD5QLG94/1759263878.305129`) |

### Strongest counter-readings

A counter-reading per trap/mechanism: the most convincing wrong reading and the record that overturns it. Coverage of the seven QC categories and the hardness gate is stated after the table.

| # | Strongest counter-reading (why a careful run could still fail it) | Overturning record |
|---|---|---|
| 1 | C&W 'feature completed' + merged PRs read as live on Mon Oct 6 | Arthur's inline #470 note: server windows on dev only (`harmonygames-Games/match3d#470#rc_10`) |
| 2 | Robert's documented #zombie-art approval read as final | his later DM message withdrawing it, top-level since revision 4 (`slack:D05GU6L0XFH/1759270241.638119`) |
| 3 | The brief read as the event list everyone names | the brief's scope sentence brings in the two rollovers (`f_7c3e91a4d2b85f60e1a9c4`) |
| 4 | Push Ready flag read as sendable | the copy rule + the August rename: 1-day lapse still says the old title (`f_a325dd4af80afc5994d5dc`) |
| 5 | Plague Race push Ready read as sendable | the second 'Status (NA, WIP, LIVE)' column reads WIP, not LIVE, so the row is held on its status (`f_a325dd4af80afc5994d5dc`) |
| 6 | The Sep 22 thread 'working fine' read as resolved | Vincent's Sep 30 prod re-test, a #zombie-match3d root in another channel (`slack:C0880U9751A/1759265412.481909`) |
| 7 | Brian's first handoff date (Oct 29) read as the commitment | his later slip mail (Oct 31 Istanbul) in another thread (`julia.lawson@harmonygames.co/1844311412966040123`) |
| 8 | Oct 31 10:00 Istanbul read as before the Nov 1 season | the 24h-before-00:00-UTC lock from base `page_season_pass_spec` (the brief only points to 'before its lock'): 07:00 UTC is 7h late (`…/1844311412966040123`) |
| 9 | Calvin's Sep 24 note on ZOM-432 read as a still-to-do for daily login | the ticket is Done since Sep 30, after Samuel's #471 note: the frame is in both submission builds, iOS 50 and Android 135, nothing left (`harmonygames-Games/match3d#471`) |
| 10 | A merged PR with an APPROVED read as nothing-left | Arthur's inline review note on #468 adds still-to-do art (`harmonygames-Games/match3d#468#rc_38`) |
| 11 | An empty-bodied APPROVED review read as no human flag | Arthur's inline note on the Season Pass premium strip inside that approval (`harmonygames-Games/match3d#472#rc_1`) |
| 12 | The open quests card read as work the Quests beat waits for | Leonard's note on that card: the weekly rollover does not wait on the new quests, so nothing is put down; ungraded since revision 5 (`68c452a03006277f55d9dc96`) |
| 13 | Boss Arena on Leonard's pipeline read as a beta beat | the brief keeps Boss Arena off this calendar (`slack:C05KNDCHAAG/1757704290.799329`) |
| 14 | Martin's Halloween app-icon read as a live-ops beat | an app icon is not a window/reset/push (`slack:C08R8CHB0QL/1758121809.236839`) |
| 15 | The translated push tab read as ZM3D beta pushes | the brief scopes beta pushes to English PNs Beta (`f_a325dd4af80afc5994d5dc`) |
| 16 | 'Win & Collect' (Domino name) copy read as fine for ZM3D | the ZM3D event is Collect & Win; held under the copy rule (`f_a325dd4af80afc5994d5dc`) |
| 17 | An open or diagnosed fault thread read as a beat hold | the hold rule needs an enter/score/claim failure after a restart; a shader or heating fault is not a hold, and the Zombie Lane iOS-verify thread decides nothing now that Zombie Lane is off the calendar (`slack:C08R27X0EAH/1759249488.495439`) |
| 18 | The un-queued Plague Race panel (queue manager in progress) read as a Plague Race hold | the queue orders panel animations additively; an un-ordered panel is engineering wiring, not an enter/score/claim blocker - Plague Race runs (`ZOM-543`, `harmonygames-Games/match3d#459`/`#472`) |
| 19 | ZOM-465's 'all event icons' struck done read as every icon animated | the three animation PRs enumerate a subset that omits Collect & Win, so its icon animation is still to do, Marcus's later note on the ticket says so and Brian's says it has to land (`harmonygames-Games/match3d#456`, `cmt_zom465_2`, `cmt_zom465_3`) |
| 20 | (revision 2) Collect & Win read as held until Oct 10, with a note on a Collect & Win ticket | the brief: "A beat whose server windows are waiting on that release starts late, it is not held." — a late start, Runs, no ticket note (`f_7c3e91a4d2b85f60e1a9c4`) |
| 21 | (revision 2) "Beta pushes" read as the Push Notification rows only, or as all 14 rows of the tab | Frederick's thread reply: "plan the PNs Beta tab as it stands, one line per row, local notifications included" and four named rows left off — ten rows (`slack:D05SD5QLG94/1759263878.305129`) |
| 22 | (revision 2) Copy that names no game read as failing the naming rule, so no push goes out | the same reply: "Copy that does not name the game at all is fine to go out, the naming rule is only about wrong names." — Lives recharged and 7-day lapse are Send (`slack:D05SD5QLG94/1759263878.305129`) |
| 23 | (revision 2) Zombie Lane read as a beat players see | the same reply: "keep Zombie Lane off the calendar, it is a permanent track with no window or reset to plan"; base `page_liveops_calendar` lists it as a permanent level-gated track (`slack:D05SD5QLG94/1759263878.305129`) |
| 24 | (revision 2) The daily-gift frame read as a still-to-do because the stores have not approved the builds or only Android is named | Samuel's note names both builds and says nothing is left; the brief's closed still-to-do is a beat's fix if it is held and anything flagged since the brief as still needed for it (`cmt_zom432_2`, on ZOM-432 since revision 5) |
| 25 | (revision 2) The Season Pass October season read as not counting, with a first window on Nov 1 | Arthur's note: "The Plague Race, leagues, Endless and Season Pass schedules are already running on prod."; the release event covers only the windows still on the DEV stack (`harmonygames-Games/match3d#470#rc_10`, `evt_9a4c2e7f1b3d58e06c7a2f`); since revision 11 the brief's clip sentence holds the October season to the span's start, Mon Oct 6 00:00 UTC |
| 26 | (revision 2) Arthur's premium-strip note read as a change-request blocker that holds Season Pass | since revision 8 the note is an inline comment inside his APPROVED review of #472, so the review state itself says no blocker; the platform review had rejected the fork while it was a COMMENTED review (P1-DR13); it is a still-to-do owned by Oliver (`harmonygames-Games/match3d#472#rc_1`) |

QC-category coverage of this review. temporal: seed chronology and the review-timestamp hazard T01 (`harmonygames-Games/match3d#470`). semantic/category: cross-game push copy (`f_a325dd4af80afc5994d5dc`). referential (cross-service): the deploy chain spans GitHub, GCal and the brief (`evt_9a4c2e7f1b3d58e06c7a2f`). quantitative: the UTC lock conversion, the only computed instant (`julia.lawson@harmonygames.co/1844311412966040123`). state/lifecycle: open issues vs shipped fixes (`ZOM-429`; `ZOM-432` is Done since revision 4). identifier/format: lookalike people and ZOM/ENG id collisions (§4). other: the local-grader two-table forensics caveat (§13). HARDNESS GATE: extreme (design) PASS, re-run above.

Correct-reading count: 26 counter-readings above (19 from revision 1, 7 added for revision 2), each with an overturning record, exceeding the floor of 7 + 10 decision points = 17. Unresolved for revision 2: the pasted hardness-gate head and the gate block below are revision-1 records and are re-pasted once the tools are synced; the forecast and trap liveness have not been re-run with T15 / `R_ASK_FOLLOWUP`, whose landing rate is unknown (§9); the forecast figures quoted in this section (and its cohort and evidence-unit counts) are those of the revision-1 manifest and surface, while §5, §8, §9 and §12 follow the revision-2 draft manifest as it stood on 2026-11-06. Unresolved from before: the difficulty is UNCALIBRATED and BORDERLINE (the enrichment added length but matches the round-2 difficulty) - P(all four gates) 0.479 (independent) to 0.533 (correlated), pessimistic ~0.480, resting partly on four flat-prior mechanisms (~33/108); the SD-band gate is the fragile one (expected six-run SD ~0.106, just above 0.10) and the forecast's `source` scenario does not test shared physical sources; a thorough Opus is the binding risk (forecast paragraph above), resolved only by the `/create-difficulty` baseline. The ~255 evidence units / >=150 unbatched reads is a workload estimate, not a necessary-call claim; the ~130 counted floor is confirmed only by an efficient correct trajectory at the baseline. The S10 (0.25) and S08/S09 (0.15) all-six-fail risks (and S06 at 0.21 until revision 5 dropped it) are recorded as VALID all-fail workload for `/create-allfail` (all values reachable); the two-table local-decode caveat is a forensics hand-normalization item for `/create-hardening`. None is a blocking defect at this stage.

Revision 3 (2026-11-06, after the second platform `/prompt` FAIL). The review of revision 2 (`plateform_reports/6aea4c1e9b621f28dc3a5332_1_prompt-2.md`, SQL sha256 `3afbf7cbbdb7`) passed every dimension except Cross-Service Coherence (2, Major): known-issue card SC-15, the `ZOM-521` checklist against its open children `ZOM-526` and `ZOM-528`, with two seeded notes sitting on those tickets. The design is unchanged by the repair: no requirement, rule, slot, trap, fragment, authority, cohort member or budget row moves, and every expected value is the same. Two things changed in the SQL (sha256 `837d4f5dedbd`, 78 INSERT and 34 UPDATE): one new Linear comment on `ZOM-526` (`cmt_zom526_2`, which the draft manifest now lists with the seeded rows of the per-issue comment surface) and the `ZOM-521` description with the two open items unticked. §2 carries the coherence line and the base grounding, §13 the card and §15 the record plan. The pasted gate block below is still the revision-1 record.

Revision 4 (2026-11-06, after an independent `/prompt` run on revision 3). That run (`research/prompt_review_rev3/1_prompt.md`) failed Cross-Service Coherence (2) on more than SC-15 and gave Clarity 3: seeded notes that reported work finished on tickets still Todo, open-work notes dated 11 to 48 days after their PRs merged, a Plague Race cadence the synthetic warehouse rows contradict, the retraction threaded under an unrelated DM message, the correction mail's threading, and three wording gaps. Revision 4 (SQL sha256 `c955d6ca2bca`, 75 INSERT and 31 UPDATE; transform `research/scripts/apply_review_fix_rev4.py`) repairs each in the data and leaves the expected values alone: seven beats, ten push rows, the same cells. What moves in this design: the vial-sprite note is an inline review note on #468 left before its merge, the premium-strip note a conversation note on #473, and the icon note Marcus's second comment on `ZOM-465` (T11, T14, CH6, §15); five tickets are Done and two In Progress, so each state follows its own note; the retraction is a top-level DM message (T2) and the correction a mail of its own (T8); the brief plans Plague Race without window dates, rewords the one-off rule and says where the config owner is told; the ask separates the calendar from the recommendation. Said plainly, four traps are weaker for it: T2 (nothing hides the retraction now), T10 (`ZOM-432` is itself Done, so the frame question hardly arises), T14 (both notes come back from one call) and, less so, T8. The cohort drops to 39 and the budget to 192 (§5, §12); the cohort is one short of the extreme minimum and needs the requester's word or a further revision. The forecast was not re-run and still describes revision 1.

Revision 5 (2026-11-06, after an independent `/prompt` run on revision 4 and a claim-by-claim audit of every injected record). That round (`research/prompt_review_rev4/`, re-audited in `research/prompt_review_rev5_audits/`) found injected statements, dates and field shapes that base contradicts: a Trello comment on a card completed in June, tickets closed or started against base code and messages (`ZOM-565`, `ZOM-471`, `ZOM-542`, `ZOM-387`), a PR note five hours after its merge, Slack and Gmail id and header shapes, and re-worded notes that named sprites, flags or release notes base does not have. Revision 5 (SQL sha256 `3c035f2af029`, 70 INSERT and 26 UPDATE; transform `research/scripts/apply_review_fix_rev5.py`) repairs each in the data. The answer key changes in two cells, both by design: the Quests still-to-do is empty (the quest note, now Leonard's on the open quests card, says the current set carries the first week), and the Collect & Win vial item reads "the final vial models (Claire)". Seven beats, ten push rows, every status, the Fri Oct 10 00:00 UTC window and the writes are unchanged. What moves in the design: slot S06, rule `R_QUEST_SET` and fragment K11 are retired (30 slots, weight 102; 14 rules; 16 fragments); T12 keeps its id as an ungraded distractor and T3 loses its Trello record; Samuel's frame note sits on the ticket it closes, so S07 is a weight-1 lookup, T10 is a trap in name only and chain CH5 is retired (5 chains); Trello carries no weight and Confluence, which has decided the lock offset all along, is declared in its place (§11); the cohort is 42 (19 issues + 23 PRs: `ZOM-565`, `ZOM-471` and `ZOM-542` are back, `ZOM-344` and `ZOM-432` are out, `ZOM-387` is in as base has it), and the budget is 194 unconditional calls with 136 on the per-record surfaces. Geometry U is 0.8824 (90/102; it was 0.8919, 99/111). The unregistered forecast re-run reads E[avg] 0.614 with P(all four gates) 0.475 to 0.542 in design mode (0.596 and 0.510 to 0.536 on revision 4) and E[avg] 0.808 in solver mode (0.813); neither is calibrated. Two things stay open and are the designer's to settle: the cohort cites `ZOM-387`, whose base state disagrees with its merged PR, and no acknowledgement fits it, so the gate's hazard line fails; and with S06 gone and S07 at weight 1 the daily-gift and quests rows carry almost no graded difficulty (dossier §11 Revision 5).

Revisions 6 and 7 (2026-11-06, after independent `/prompt` and Eval 0 rounds on revisions 5 and 6: `research/prompt_review_rev5/`, `research/prompt_review_rev6/`). The round on revision 5 scored every dimension 5 except Unique Ground Truth, which failed on one fork: nothing said whether the Oct 13 quest set has to land for the beta. Revision 6 (SQL sha256 `f8d905bdd0c2`, transform `research/scripts/apply_review_fix_rev6.py`) settles it in the quest note, adds a third note on `ZOM-526`, shortens the notes on `ZOM-544` and in Brian's Sep 22 mail, and restores Drive and Gmail field shapes. Revision 7 (SQL sha256 `091722f6a281`, 72 INSERT and 26 UPDATE; transform `research/scripts/apply_review_fix_rev7.py`) makes the quest note say the new quests are additive and adds a second note on `ZOM-521` after #475 merged. The answer key does not change: `solver/truth.json` is byte for byte the revision-5 file. The requester settled the three points revision 5 left open: `ZOM-387` is out of the cohort on its merits, so the cohort is 41 (18 issues + 23 PRs), the budget 193 unconditional calls and the per-record surfaces 135, and the gate's hazard line passes with no acknowledgement; Confluence stays the tenth weight-carrying service and Trello a touched schema with no weight; S07 stays a weight-1 lookup. The surface is unchanged (30 slots, weight 102, U 0.8824) and so is the unregistered forecast (E[avg] 0.614 with P(all four gates) 0.475 to 0.542 in design mode, E[avg] 0.808 in solver mode; neither is calibrated). `ZOM-521` has been a cohort member since revision 1 and stays one, `ZOM-528` is not, and no graded slot reads either (dossier §11 Revision 7).

Revision 8 (2026-11-06, after a fresh blind `/prompt` round on revision 7: `research/prompt_review_rev7/`). Revision 8 (SQL sha256 `0e8c8ad83f3b`, 71 INSERT and 25 UPDATE; transform `research/scripts/apply_review_fix_rev8.py`) answers its findings: one sentence in the brief on undated holds, re-worded notes on `ZOM-534`, `ZOM-521` and `ZOM-542`, the quest note saying the rollover does not wait on the new quests, a `web_view_link` on the calendar sheet, and the premium-strip note moved off merged #473 to an inline note under Arthur's base approval of #472, six seconds before that merge. No graded value changes; the one evidence id that moves is `#473#c_2` to `#472#rc_1`. The move has a measured cost. That note was the only seeded row on the conversation surface, so `github_get_issue_comments` stops counting: three surfaces, 96 per-record calls (135) and 154 unconditional calls (193), each still above its floor (75 / 130). T11 is weaker because one per-PR call type now reaches both of its notes, and #472 is the likelier PR to be opened: `cmt_zom526_3` names it and T1, D10 and `R_INFRA_SCOPE` already use it. The mechanism stays A3 and the surface keeps 30 slots, weight 102 and U 0.8824. The unregistered forecast does not move, but it cannot see this change, so that is no evidence that difficulty held (dossier §11 Revision 8).

Revision 9 (2026-11-06, after the platform's third `/prompt` failure: Unique Ground Truth and Clarity on `ZOM-534`, the S23 freeze and #477; census in `research/rev9_census/`). Revision 9 (SQL sha256 `892f7edda809`, 76 INSERT and 28 UPDATE; transform `research/scripts/apply_review_fix_rev9.py`) closes the brief's open rules and adds records only where the platform asked for one or the rule cannot reach. The still-to-do rule is closed: a held beat's fix, plus what has been flagged for that beat as not done since the brief (prod deploy, config or player-facing art), and nothing else. The change-request sentence is untouched. No graded value changes: `solver/truth.json` is byte for byte the revision-8 file. New records, none deciding: `cmt_zom534_2`, `cmt_zom566_1` (Brian's; Owen's note is `cmt_zom566_2` now), `cmt_zom563_1` (`ZOM-563` goes Done and stays out of the cohort) and two #zombie-bugs replies. Three wording changes come from the difficulty review (`research/rev9_census/difficulty.md`): Robert's withdrawal drops the search words, the Collect & Win cadence moves to "Span and time base", and Push copy drops "only" twice. No `R_` rule or `T` trap depended on the removed "unverified build or platform" clause, so none is retired; K13's quote moves to "An established failure holds it", and D7 and D9 are re-worded. The surface keeps 30 slots, weight 102 and U 0.8824; S04, S05 and C01 accept "In" and the Pushes table follows the seeded headers. Cohort 41, per-record 96, budget 154 of 164: unchanged. The unregistered forecast is unchanged too, and it cannot see any of this: with the revision-8 SQL swapped in it reads the same (dossier §11 Revision 9).

Revision 10 (2026-11-06, after a pre-review attack on revision 9: `research/rev9_attack/`). Revision 10 (SQL sha256 `ffbac4586fb9`, 78 INSERT and 29 UPDATE; transform `research/scripts/apply_review_fix_rev10.py`) re-words the still-to-do rule to "its fix if it is held, and anything flagged since this brief as still needed for it (prod deploy, config or player-facing art)", removes the "pre-empts" sentence, and makes Push copy judge "the English copy on that row". It adds `cmt_zom565_2` and Robert's reply in Martin's desert thread, replaces Oliver's shader reply with Vincent's, moves Leonard's S23 reply and `cmt_zom534_2`, and re-words Brian's ZOM-566 note, Vincent's ZOM-563 note and the Trello note. None of these records decides a value. Two value changes are deliberate, and no evidence id moves: the owners (Weekly Leagues' fix and Collect & Win's server windows name Douglas) and Weeks running (Quests and Daily Login read All four weeks). No slot reads those cells, so none needed a new accepted outcome; C05 also accepts "Starts late". Slots, weight, U, cohort, per-record count, call budget and the unregistered forecast are all unchanged (dossier §11 Revision 10).

Revision 11 (2026-11-06, after the formal blind round on revision 10: `research/prompt_review_rev10/`). Revision 11 (SQL sha256 `1348d287ac4a`, 80 INSERT and 30 UPDATE; transform `research/scripts/apply_review_fix_rev11.py`) adds five things to the brief: the clip sentence ("Clip anything that starts before or runs past that to those two instants."), "closing 23:59 UTC on its last day", the held-row sentence ("A held beat keeps its usual windows on its row, marked held."), "Login Calendar on the push sheet, same beat" and "moves to any time before it". It adds `cmt_zom465_3` (Brian: the Collect & Win icon has to land) and Douglas's reply in the #zm-collect-win reward-table thread, moves ZOM-542 to Todo, and re-words the strip note and its mirror, Robert's approval and withdrawal, the UA deck, Frederick's opener, ZOM-504, ZOM-563 and the shader note. The quest note's payload has no `list` or `idCard` key any more, the base shape of one commentCard. No value changes. One evidence id is added: `cmt_zom465_3` on the Collect & Win row. Season Pass's First window stays empty in `solver/truth.json`. Slots, weight, U, cohort, per-record count, call budget and the unregistered forecast are in dossier §11 Revision 11.

Revision 12 (2026-11-06, after the verification round on revision 11: `research/prompt_review_rev11/`). Revision 12 (SQL sha256 `b5ccbfa577fc`, 81 INSERT and 30 UPDATE; transform `research/scripts/apply_review_fix_rev12.py`) states the 23:59 UTC close once for every window, widens the held-row sentence to "windows and weeks", adds "and the shop rotation is not a beat", "(Login Calendar and Weekly Rankings are fine)" and "what its row is missing". Arthur's vial note and its mirror say the models are needed before the beta, Brian's ZOM-465 note reads "ticked before that event merged", the quest note's payload has `idCard` and `textData` back and still no `list`, `cmt_zom563_1` is Douglas's note at 18:17:05Z and Vincent's check is `cmt_zom563_2`. Three empty, ungraded cells are filled by design: Weekly Leagues' First window and Weeks running, and Season Pass's First window. No other value and no evidence id moves. Slots, weight, U, cohort, per-record count, call budget and the unregistered forecast are in dossier §11 Revision 12.

Revision 13 (2026-11-06, after the cold reviewers' last items on revision 12: `research/prompt_review_rev12/`). Revision 13 (SQL sha256 `1f2175a297fd`, 81 INSERT and 30 UPDATE; transform `research/scripts/apply_review_fix_rev13.py`) re-words Arthur's vial note and its mirror ("still need their final models before the event runs. Not a blocker for this PR"), Brian's ZOM-465 note ("before the event runs") and two brief phrases ("the rotating shop", "with which of those its row is missing"), and puts the `list` key back on the quest note's payload. No value and no evidence id moves. Slots, weight, U, cohort, per-record count, call budget and the unregistered forecast are in dossier §11 Revision 13.

Revision 14 (2026-11-06, after the last cold P1 on revision 13: `research/prompt_review_rev13/`). Revision 14 (SQL sha256 `edae63f3e838`, 81 INSERT and 30 UPDATE; transform `research/scripts/apply_review_fix_rev14.py`) changes two brief sentences: the config-lock rule now reads "and you tell its owner in a reply on the mail where they committed to it", and the span section adds "Endless goes down as its weekly windows, with the daily reset noted." No value and no evidence id moves. Slots, weight, U, cohort, per-record count, call budget and the unregistered forecast are in dossier §11 Revision 14.

```
STAGE GATE scenario: PASS — Task_Authoring/task_inputsS · 01_Scenario_Design.md#d3905efac6f9 · 01_Hardness_Manifest.draft.json#a69a0e4fe2ed · 01_Gradable_Surface.json#f17918c8dfc4 · 00_Assigments.md#4844ae9f5ae7 · __context__#7b0cc66ffd45 · __assignment__#e8b8269803d5 · __policy__#dc4ab5df3cdd · __gate_policy__#9b78441396d8 · __review__#31f6b63ef388 · blocking 0 · warnings 0 · checks 33
[PASS] assignment.v3_context: Julia Lawson / Product Manager; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 3 output(s) present: 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json
[PASS] structure.inputs: 1 input(s) present: 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md)
[PASS] structure.sections: 19 required sections present and non-empty (01_Scenario_Design.md)
[PASS] structure.placeholders: no placeholders in 01_Scenario_Design.md
[PASS] evidence.storyline: 12/12 items carry a source pointer (min 80%)
[PASS] evidence.coherence_audit: 9/9 items carry a source pointer (min 100%)
[PASS] evidence.hidden_authorities: 3/3 items carry a source pointer (min 100%)
[PASS] evidence.delegation: 16/16 items carry a source pointer (min 90%)
[PASS] evidence.trap_register: 62/62 items carry a source pointer (min 90%)
[PASS] evidence.record_plan: 9/9 items carry a source pointer (min 80%)
[PASS] evidence.active_speakers: 12/12 items carry a source pointer (min 100%)
[PASS] tool.hardness_gate_design: hardness_gate --design pasted PASS; re-run PASS
[PASS] tool.persona_reach: persona_view reach pasted for julia.lawson@harmonygames.co and matches the re-run (147 channels)
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] kb.coherence_hazards: coherence audit cites 9 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 12 speaker rows carry their activity.json status_at_clock
[PASS] kb.integrations: companions listed per integrations.json (8 INT ids, services ['gcal', 'gdocs', 'gdrive', 'github', 'gmail', 'gsheets', 'gslides', 'linear', 'slack', 'trello'])
[PASS] kb.storyline: timeline cited; cohorts ['LIN-OPEN-ZOM']; trap_catalog ['C01', 'C02', 'C03', 'N01', 'P01', 'P02']
[PASS] boundary.anchor_naming: 4 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] tool.redteam_dual: dual red team present (01b_Redteam_Review.md + .second.md)
[PASS] surface.valid: 31 slots, weight 111; geometry report-only, never gated: mechanism share 89%, always-pass share 11%
[PASS] forecast.preregistered: prior forecast pre-registered in the ledger: ['hev_10c8bb5be00ab2cf'] (UNCALIBRATED, advisory)
[SKIP] revise.intake: no MODE B report and no revision-intake section: nothing to take in
[PASS] reach.scenario: 17 scoped load-bearing ids YES for julia_lawson (7 planned seeds not yet in base: verified at the injection gate)
[PASS] review.counter_readings: 19 evidenced counter-readings (of 19 found; need ≥ 15) in 01_Scenario_Design.md
[PASS] review.coverage: self-review addresses all 8 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.draft.json is bound to the current assignment, policy, source context and freeze
[PASS] v3.role_review: current role-plausibility review recorded; semantic judgment belongs to the named reviewer
[PASS] handoff.pasted: pasted into the Self-review by --paste
```


