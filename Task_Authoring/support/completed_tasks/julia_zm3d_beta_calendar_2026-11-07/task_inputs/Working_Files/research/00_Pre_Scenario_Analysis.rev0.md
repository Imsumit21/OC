# Pre-scenario analysis — Julia Lawson · Product · Marketing and GTM · Planning and decision support · Long Horizon · Medium · Oct 1, 2025 (synth-cut)

Analysis only. This file holds no prompt, Oracle Event or rubric text; it prepares `/create-scenario`. No SQL was written
or executed. Writes went only to `Task_Authoring/task_inputsS/` (this file, `Working_Files/research/`, and the
`00_Task_Context.json` refresh) plus the helper caches under `Task_Authoring/support/local_search/`. `Evals/` (including
its input store), `claude/`, `Task_Authoring/tools/`, the universe and the other task folders were not written.

| Item | Value (source) |
|---|---|
| Clock | `Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)` (`hg.py universe show`) |
| Seed bound | `2025-10-01T00:00:00Z` = Tue Sep 30, 5:00 PM PT. Every seeded event timestamp at or before it (`sql_lint.py`); base records 00:00–07:00Z Oct 1 exist and are checked as possible superseding records (§5.6) |
| Persona today | Wednesday, October 1, 2025; "yesterday" = Tuesday, September 30 (GEN_EXECUTION §0a; learnings §20) |
| Universe | synthcut, `hg4-synth-sep30cut v16`; no shutdown rules; Victor Barnes departed April 2025 and cannot act |
| Context | `task_context.py --task-dir Task_Authoring/task_inputsS --write --require-source` → `source.status: ready`, `kb_status: bound`, `context_hash 7b0cc66ffd451f41aff7b1db7367e86f141b0d1fa444f1839482cf2e5839dc5e` |
| Assignment | `00_Assigments.md` sha256 `e8b8269803d55217…`; mode **medium** (cap < 85 %, design target ≤ 77 %); Long Horizon → `effective_profile: extreme` |
| Tools | `Task_Authoring/tools` last commit `58c37b1` (2026-11-03 03:40 +0530); one untracked `tools/stage_check.py` from another session (not touched). Re-check `git log -3 -- Task_Authoring/tools` before any gate run (learnings §57) |
| Evidence files | `Working_Files/research/`: `S1_liveops_census.md` + `S1b_liveops_followup.md` (live-ops readiness census), `S2_cohort_options.md` (≥ 40 populations), `S3_alt_storylines.md` (B and C), `S4_reach_writes.md` (reach, write targets, DM languages, `can-see` output), `S5_coherence_hazards.md` + `S5b_kb_transcription.md` (hazards, KB), `00_sketch_manifest.json` / `00_sketch_surface.json` / `00_sketch_geometry.json` (+ control and sensitivity), `hardness_v2_check_sketch.txt`, `hardness_v2_check_control.txt`, `geometry_mc_output.txt`, `geometry_mc_sens_judgment.txt`, `tool_reach.txt`, `tool_entity.txt`, `raw/` (reads through `tools/hg.py`), `scripts/` |
| Method | Five parallel research workers (S1–S5) plus two follow-ups (S1b, S5b) on disjoint briefs; the build session wrote up the workers' findings where they ran out of steps (each file says so) and re-ran every load-bearing check itself (`can-see`, Part 7 checker, geometry) |

---

## 1 · What a 5 needs at each gate

| Gate | A 5 / PASS needs | What this task must do to get it |
|---|---|---|
| `/injection` (static, Checks A–C) | A: every id, reference and person token exists or is new and collision-free, and every seeded fact agrees with the **whole** universe (learnings §10, §14, §15). B: SQL valid against `universe_schema_live.json`, only writable tables (never Snowflake, Confluence or `_changelog`, §26, §50). C: every seed after the base events it relies on (§13, §17), at or before the seed bound, no Linear comment after its ticket's `completed_at` (§50, §57), companions present (thread counters, `updated_at`, per-attendee GCal copies and invitation mail). | Census every event, person and claim across all 13 services before seeding (S1/S1b/S5 already list the base state per event). Seeded GitHub comments only on `match3d-backend`, which has **no** Slack mirror (S5b §4); any `match3d` comment needs its `#zombie-prs` INT-01 copy. No per-issue Linear note on a Done ticket after its completion (use open issues or a `#zombie-bugs` thread reply). |
| `/prompt` | Every scored sub-dimension 5: UGT (one end state after the two-reading test), Feasibility, ACL reachability (every required scoped read YES), no tool names, not contrived, today = Wed Oct 1, Truthfulness, investigation + action, persona, **business function 5, competency 5, task skill 5**, a load-bearing complexity dimension, data seeding, Cross-Service Coherence 5 on all task-touched data incl. pre-existing defects (`1_Prompt_Eval.md` §1.5, §2.1, §3.2). | Fit argued in §3 (the competency gate is a local hard FAIL). Rules, definitions and exceptions live in records; the prompt is an ordinary request naming its destinations. Every known-data-issue card in the area is dispositioned (§5.5) and every graded value avoids them. |
| `/hardness` | Score 5 = "genuine model failures invalidate the central result/delivery or defeat much of the core task" on the single unhinted Opus 5.5 run (`1A_Hardness_Eval.md` §5); 3–4 still PROCEED. | The central result is the beta calendar Frederick will run the bought cohort on: a missed trap starts an event before its server windows exist, runs a cancelled one-off over a recurring race, sends pushes with the old game name to bought users, or leaves a broken event on the calendar — consequential, not cosmetic (§6). |
| `/oe` | PASS: complete critical path (discovery, dependencies, every required write) with accurate tools, parameters, ids and expected data; no non-action or final-response event (`2_Oracle_Events_Eval.md`). | Every deciding record reachable from a prompt noun by a natural call; expected values quoted from records; catalog tool names only (`gsheets_create_spreadsheet`, `gsheets_values_update`, `slack_send_message`, `linear_create_comment`, S4 §2). |
| `/rubric` | No Major, no Moderate, Minor < 5 %; weights 1/3/5 by kind of work; ≥ 1 Outcome; Process ≤ 50 %; no row passable by doing nothing; one fact per row and never in ≥ 3 rows; ≤ 5 samples per group + a volume row + direct exception rows; predicted all-fail 0 (`3_Rubrics_Eval.md`; GEN_EXECUTION §3). | The planned surface (§6.4) keeps each trap's miss on ≤ 2 rows, weight 5 only where the work is multi-source; exclusions are graded as positive results inside the calendar ("Halloween one-off not on the calendar" is the calendar's content, with the Plague Race window present), never "leaves X alone". |
| `/create-difficulty` (`12_Difficulty.md`) | Six Opus 5.5 slots with provenance, ≤ 2 errored; corrected average **strictly < 85 %** (medium); < 5 full passes; population SD 0.10–0.30; ≥ 2 failure patterns, largest ≤ 50 %; ≥ 100 counted calls (golden run if any, lowest governs). | Six independent loss channels on different services and surfaces with graded findability (§6.1, §6.5); honest shortest path ≈ 125 counted calls, typical runs far above (§7). |
| Local stage gates | `stage_gate.py` scenario → … → release PASS; `hardness_gate.py` at `effective_profile: extreme` (≥ 10 services, ≥ 120 rows, cohort ≥ 40 × 3 surfaces, ≥ 12 traps, …); dual red team or a recorded `RED TEAM FALLBACK:`. | Decisions D2 (volume exception) and D4 (review fallback) in §11; the cohort is the weakest structural point (§8). |

---

## 2 · Julia's reach at the clock

`python3 Task_Authoring/tools/persona_view.py reach julia_lawson --top 10` (verbatim, `research/tool_reach.txt`):

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
```

Identity (`entity.py resolve "Julia Lawson"`, `research/tool_entity.txt`): Slack `EMPLOYEE_0005_SLACK_ID` (31,848 posts,
last 2025-09-30); Gmail `julia.lawson@harmonygames.co` (thread-file alias `jlawson@`; last mail 2025-09-17); GCal own
calendar (time zone Europe/Istanbul, S4 §5); Drive `user_8140f09bf9f1` root `d_8140f09bf9f1b94cb8ee2d` (28 owned); Linear
`usr_8140f09bf9f1b94c`; GitHub `PERSON_0005_GITHUB_USERNAME`; Trello `793af7ca6940bf18eb516c75`; Confluence
`user_EMPLOYEE_0005`; Contacts `8140f09bf9f1b94cb8ee2dd7` (job "Product Manager"). Status at the clock: active through
2025-09-30 (KB `activity.json`).

**What she does in September 2025 (verified).** She is the ZM3D funnel and level designer: 141 posts in `#zombie-design`
`C090N54TG79` and 286 in her DM with Robert `D05GU6L0XFH` in September, on levels 1–300, the "Variant C" funnel, the Sep 29
card-intro change and the casual-vs-hardcore debate (`C090N54TG79/1759172119.133819`, `…/1759173386.589489`). Confluence
names her role in live-ops planning: `page_liveops_calendar` (owner Frederick Stone, Growth/UA, v3 2025-09-29) — "Daily
live-ops pod review. Design, led by Julia Lawson, walks the coming weeks with Frederick Stone: which recurring slots fire
and whether a one-off drops on top"; `page_live_ops_engine` — "Event definitions … Design (Julia Lawson)";
`page_season_pass_spec` — "Design partner: Julia Lawson". She supports Frederick's UA creatives (`D05SD5QLG94/1752672252.963899`
UK static CPI test; `…/1756234644.700299` screenshots round 3) and owns two live-ops docs: `[LiveOps] Event Icon Management
System` `f_744027532fb1b0cc8821c4` and `[Zombie Ops] Zombie Lane` `f_023c7331d7e34900bd226f` (S4 §1).

**Reach on the records the recommended storyline needs** (`persona_view.py can-see`, verbatim in S4 §7):

| Record | Result |
|---|---|
| `slack C05KNDCHAAG/1757704290.799329` (Leonard, "Beta target: Sep 30", beta pipeline) | YES |
| `slack C090N54TG79/1758517286.431379` (Leonard, "tech-stable beta in 15-20 days"; "Axe Arena is descoped") | YES |
| `slack C05KNDCHAAG/1758558164.541689` (Brian, "postpone Axe Arena for the beta release") | YES |
| `slack C090N54TG79/1757478958.104989` (Leonard, halve Plague Race rewards; thread "60, 120, 250?" / "sounds good") | YES |
| `slack C08R8CHB0QL/1758121809.236839` (Martin, "Halloween theme for an app icon or an event", no replies) | YES |
| `slack C08R6BF4ENN/1756747348.667629` (Douglas, "BossArena API Endpoints are ready for testing on dev") | YES |
| `slack C08H78VJG80/1759174925.309129` (Frederick pauses the playable over the pivot) | YES |
| `slack D05SD5QLG94/1758220925.518329` (Frederick–Julia DM, English) | YES |
| `gsheets f_a325dd4af80afc5994d5dc` "Push Notifications Zombie Match" (owner Resource, shared with Julia) | YES (read only; not a write target) |
| `gdocs f_744027532fb1b0cc8821c4`, `f_023c7331d7e34900bd226f` (Julia-owned), `f_9956263905ddb43d1500ff` (Endless spec) | YES |
| `confluence page_liveops_calendar`, `linear ZOM-566`, `trello 6851a6fde24742cce9ad7b1c` ("Plague Race (AKA Mine Dash)") | YES (unscoped) |
| `gdrive d_8140f09bf9f1b94cb8ee2d` (her Drive root) | YES |
| `gsheets f_c0518ab5dacb03dcc8a144`, `f_89aebb6083dc44501666c7` (Season Pass reward sheets) | **NO** |
| `gsheets f_d224d9f6fcd6045faeee22` (Vincent's ZM3 event and league bots) | **UNVERIFIED** |

Gaps that shape the design (S4): no Gmail after 2025-09-17 and no work mail in Aug–Sep; no Julia calendar event on or after
the clock and no recurring all-hands in 2025 H2; no live-ops sheet she owns (write targets are created at run time);
the push sheet belongs to `Resource: -6481757892984311338`; her DMs with Brian, Vincent and Claire are Turkish and with
Leonard mixed, while Robert, Frederick, Martin, Marcus, Calvin and Oliver are English (seeded DM text goes only into
English DMs); no `#executives`, `#bridge-pitch`, `#zm-collect-win` or `#zombie-prs` access.

---

## 3 · Fit (rule 2)

- **Business function — Product & Design** ("Product decisions, gameplay/design requirements, art and prototype evaluation",
  `Evals/references/rules/task_categories.md`). The calendar decides which live-ops features run for the beta cohort and
  when (product decisions on a prototype under evaluation: Leonard will "decide: either iterate or pivot the core game"
  on the beta data, `C090N54TG79/1758517286.431379`), with each event's design requirements set by the event specs Julia
  owns as "Event definitions … Design (Julia Lawson)" (`page_live_ops_engine`): windows, rewards, one-offs.
- **Competency — Marketing and GTM** ("Demand and retention, GTM, communications"; typical personas include PM; outputs
  decks, memos, spreadsheets, emails; `Taxonomy_V2_Step_Map.md` screen 7; `/prompt` reads "campaigns/GTM"). The
  deliverable is the **beta-weeks retention calendar and player-push plan** for the bought-user beta: in-game live-ops
  campaigns plus their start pushes and lapse reminders, owned by Growth/UA (`page_liveops_calendar` "Owner: Frederick
  Stone (Growth/UA)"), timed to the UA buy ("when it's approved we'll start buying users at small scale",
  `C0880U9751A/1757561483.446549`) and sent to the GTM owner as a recommendation. Every graded value is a calendar,
  campaign or communication call — never a ticket state or a build fact for its own sake.
- **Task skill — Planning and decision support** ("Recommend a course of action, plan, or schedule, with tradeoffs"):
  the output is a schedule (which beat fires in which window, what is held and until when) with the tradeoffs Frederick
  asked for (late Collect & Win against a clean first week, recurring race against a one-off, holding lapse pushes
  against D1 re-engagement).
- **Role.** The Confluence page names this exact work as Julia's ("Design, led by Julia Lawson, walks the coming weeks with
  Frederick Stone"); she designs the ZM3D events and funnel and is Season Pass design partner.
- **Risk (named, mitigated in design).** Two readings could pull the competency elsewhere: "check every live-ops issue"
  reads as Engineering Ops if the issue sweep becomes the output (§8 keeps it an input; no graded row is a ticket state);
  "plan the events" reads as Product Management if communications drop out (the push plan and the GTM owner's
  recommendation stay in the deliverable). The prompt must read as the beta GTM calendar request.

---

## 4 · Storylines

All of Julia's 2025 work is ZM3D: Domino Delights is in maintenance and its live-ops area carries SC-31/SC-47; the
Mattel, Combo Fighter and web-distribution arcs are normal-only. All three candidates are therefore ZM3D (theme: D3).

### 4.1 A — ZM3D beta-weeks live-ops and player-push calendar (recommended)

**Situation at the clock (verified, S1/S1b).** Leonard set "Beta target: Sep 30" with Win & Collect, Reward Animations,
Season Pass and Infinite HP Boss Mode as the beta pipeline (`C05KNDCHAAG/1757704290.799329`), then descoped Axe Arena and
asked for "clean data from a tech-stable beta in 15-20 days" before an iterate-or-pivot call (`C090N54TG79/1758517286.431379`;
Brian `C05KNDCHAAG/1758558164.541689`). The submission builds were cut on Sep 30 and UA starts when the stores approve
("when it's approved we'll start buying users at small scale", `C0880U9751A/1757561483.446549`; "It will take a few days to
go live", `C08R27X0EAH/1758767858.307829`). Live for players: Plague Race (5-day windows, 20 runs EVT-0306 … EVT-0514 in
`LIVE_OPS.EVENTS.LIVE_EVENT_PERFORMANCE`, last 09-22 → 09-26), Endless Monster Mode (daily 00:00 UTC / weekly Monday
resets), weekly leagues, Zombie Lane, quests (with ZOM-534 "Quest points not resetting until app restart in production",
In Progress), daily login (ZOM-556 Todo) and Season Pass (iOS 0.3.49 released Sep 29, `C0880U9751A/1759182908.627389`;
EVT-0527 partial season 09-29 → 09-30; monthly seasons reset on the 1st 00:00 UTC, config locked 24 h before,
`page_season_pass_spec`). Built but not live: Collect & Win (match3d#468 merged 09-29, #470/#472 merged 09-30 15:51–15:53Z,
before the cut; `page_liveops_calendar` "QA blockers cleared 26 Sep 2025); not yet live"; #477 analytics open — SC-18) and
Boss Arena (client merged #424; server endpoints "ready for testing on dev", `C08R6BF4ENN/1756747348.667629`; SC-68). Not
built: Axe Arena (descoped, Trello list "Oct 21"), a Halloween one-off (Martin's one-line idea, no replies, no card, page,
ticket or push row; S1b §4). The push sheet `f_a325dd4af80afc5994d5dc` "PNs Beta" has 14 rows: Ready = lives recharged,
1-day lapse, 7-day lapse, D0-1 FTUE, Plague Race, weekly leaderboard reset; the 1-day lapse and FTUE rows still say
"Puzzles vs Zombies", renamed 24 Jul 2025 (`page_zm3d_gdd`). PlayableX is paused until Nov 3 over the pivot
(`C08H78VJG80/1759174925.309129`, `…/1759226395.551469`). The calendar ticket ZOM-78 "Event Calendar For Zombie Match 3D"
sits in Backlog with no description.

**The work for Julia on Oct 1.** Frederick (calendar owner) asked her yesterday, in their DM, for the live-ops calendar of
the four beta weeks (Mon Oct 6 – Sun Nov 2) the bought cohort will play: which beats fire in which windows, what is held
and until when, the start push for each beat, what is still to do before each one runs and by whom, and her
recommendation with the tradeoffs; the calendar goes in a sheet in her Drive, linked from the calendar ticket, and her
recommendation goes back to him in the DM. (The ask is a seeded record; this is its meaning, not its text.)

**Services.** Native and load-bearing: Slack (`#zombie-design`, `#company-internal`, `#zombie-art`, `#zombie-ops`,
`#zombie-bugs`, `#zombie-match3d`, DMs with Frederick and Robert), Confluence (calendar page, live-ops engine, Season Pass
spec, GDD — base only, never injected), Linear (ZOM live-ops issues, ZOM-78), GitHub (match3d, match3d-backend), Snowflake
(Plague Race cadence, past runs), Sheets (push sheet), Trello (ZM ROADMAP: "Mine Dash" alias, beta list), Drive (her root).
Injection lifts Docs (Frederick's beta UA brief: buy dates and geos), Slides or Gmail (the UA plan carrier Frederick shares),
GCal (the live-ops pod review and the November season lock as plan events), Drive (a Julia-owned "ZM Live Ops" folder),
Linear (per-issue QA notes — base has 0 comments on 3,687 issues, S2), GitHub (`match3d-backend` deploy note), Slack (the
ask, Robert's call and his withdrawal), Trello (a beta-list card comment) to 10–11 services; whether Slides and Contacts
can carry a natural fact is an S1/S2 decision (risk §10.4).

**Hardness opportunities (each its own fact, detail §6).** v2 trap 1 done across services (Collect & Win merged and "QA
blockers cleared", server windows only on dev); trap 2 correction elsewhere (Robert's approval of a Halloween one-off in
Martin's thread, withdrawn in his DM); trap 7 outside the obvious filter (beats the calendar page does not list); trap 9
work someone already did (the Plague Race reward cut already live); trap 5 a rule in the data overriding a status (Ready
pushes with the pre-rename title); a tool-surface blind spot on the per-issue QA re-test (list views return no comments).

**Volume.** Shortest sufficient path ≈ 125 counted calls (§7): below the local 500 floor, above the platform's 100.

### 4.2 B — ZM3D beta audience test plan (casual vs midcore, UA cells, creatives, readout)

Anchors (verified, S3): PlayableX `C08H78VJG80` (Scenario 1 `1757695108.506159`, pause `1759174925.309129`, Nov 3 restart
`1759226395.551469`), `#zombie_marketing` `C06DJBJL798` (30-s UA cut `1755114007.441789`, marketing screens
`1756393931.415699`), Frederick–Julia DM (UK static CPI test `1752672252.963899`; ART-792), `#zombie-design` Sep 22
priorities and Sep 29 hardcore debate. **Against it:** UA buys belong to Frederick and Leonard (Julia has no posts in
`#zombie_marketing` or `#analytics`), the deciding CPI/retention numbers live in `#executives` and mpdm channels Julia
cannot read, and every UA number sits on a known-issue card (SC-11, SC-12, SC-23, SC-28, SC-29, SC-16, SC-65). Population
well under 40. Business-function risk: creative and channel choices read as Growth/UA/Marketing, not Product & Design.

### 4.3 C — ZM3D Season Pass Season 2 (November) plan

Anchors (verified, S3): `page_season_pass_spec` v2 (30 tiers, $6.99, unlock level 30 "an active A/B variable", monthly reset
1st 00:00 UTC, config locked 24 h before, "No Season Pass purchase has been recorded yet"; Owner Robert, design partner
Julia), `page_zm3d_gdd` comments (Julia's 6-slot tray A/B; Robert: "queue the 6-slot test for after the season ends"),
EVT-0527, ZOM-552, match3d#438, Trello `6851ab766fcaf894d0c0048b`. **Against it:** the reward-track sheets are NO for
Julia (S4 §7), so the 60-slot population cannot carry a graded value; SC-38 sits on the ship date and analytics; the
October season opened hours before the clock, so November planning has thin base support. Product & Design fit strong,
GTM fit medium.

### 4.4 Comparison, distinctness and recommendation

| | A — beta live-ops & push calendar | B — beta audience test plan | C — Season Pass Season 2 |
|---|---|---|---|
| Fit (function / competency / skill / role) | 5 / 5 as the GTM calendar (risk §3) / 5 / named on the Confluence page | 3–4 (Growth) / 5 / 5 / weak (UA is Frederick's) | 5 / 4 / 5 / design partner |
| Native services with base records | 9 (Slack, Confluence, Linear, GitHub, Snowflake, Sheets, Trello, Drive, Docs) | 5–6 | 6 |
| v2 trap types with base precedent | 1, 2, 5, 7, 9 (+ tool-surface) | 2, 5 | 4, 5 |
| Consequence of a miss (for `/hardness` 5) | the bought cohort plays a broken or wrong calendar; stale-name pushes go to new users | a mis-specified test cell | a wrong reward tier |
| Known-issue cards | SC-13/14/18/38/62/68 near the area, all avoidable (§5.5) | SC-11/12/23/28/29 on the core numbers | SC-38 on the core dates |
| Natural population ≥ 40 | 56 live-ops ZOM issues (with seeded notes, §8) | no | 60 tiers, invisible to Julia |
| Honest volume | ≈ 125 | < 100 | < 100 |

**Distinctness.** Vincent's `vincent-zm3d-release-gate` decides, defect by defect, whether two Sep 30 submission builds may
ship (fix in the candidate, verified, deployed), with release-ticket blockers. Claire's
`claire-zm3d-october-object-handoff` decides which new art objects go to level design for the October batch. A decides
the live-ops and push calendar for the bought-user beta: its population is the beta's live-ops beats and their issues,
its authorities are the calendar page, the Season Pass spec, the GTM owner's ask and the Product owner's one-off call, and
its outputs are a calendar, a push plan and a recommendation. Overlap to keep out: A's issue sweep (§8) must not become a
defect gate (no graded ticket verdicts); its done-across trap is a server-window deploy on an event, not a fix in a build.
A also differs from the completed Julia tasks (`julia_zm` difficulty register, `julia_dd` close-out) and from Douglas's
beta server sign-off (prod-vs-dev per ticket): A never grades a ticket's prod state.

**Recommendation: A.** It is Julia's named job on her actual today, its rules already live in base records (the calendar
page's overlap, displacement and deploy rules; the Season Pass cadence and lock; the rename), the hard decisions survive
complete retrieval (a merge vs a server deploy, a thread approval vs a later DM, a Ready flag vs the rename, a scope page vs
the ask's scope), and a miss changes the calendar the bought cohort plays.

---

## 5 · UGT plan (rule 1) — storyline A

### 5.1 Rules every decision needs, homed in incorporated records

| Decision | Rule (meaning, not wording) | Home (planned; base where possible) | Census / proof needed |
|---|---|---|---|
| Scope | every ZM3D beat players can see in Mon Oct 6 – Sun Nov 2: a window, a reset or a start push | the ask (seeded Frederick DM, the anchor) | census of every live-ops feature in the beta build (S1b §6 table) and every push row (14); a completeness claim only with it (learnings §23) |
| Window cadence | Collect & Win Mon-Tue / Wed-Thu / Fri-Sun; Plague Race rolling 5-day windows; Endless daily 00:00 UTC + weekly Monday; Season Pass monthly 1st 00:00 UTC, config locked 24 h before | base: `page_liveops_calendar`, `page_season_pass_spec`, Snowflake rows, Endless doc `f_9956263905ddb43d1500ff` | the Plague Race cadence is only implicit in Snowflake rows: settle with one dated record if a window is graded, or grade it as derived (sample row) with the derivation accepted |
| "Starts" | a beat starts with the first window that opens after (a) the beta build is live and (b) its server windows are live on prod | base page "Windows are cron expressions in the CDK stack and do need a deploy to change" + the ask's UA start date + a seeded backend deploy note | no base record dates a Collect & Win prod deploy (S1b §2 "Negative pins"): the seeded note may not conflict with any base claim |
| Held for tech | hold an event whose core loop (enter, score, claim, reset) is broken on prod by an open issue; cosmetic, VFX and analytics gaps do not hold it | Leonard `C090N54TG79/1758517286.431379` ("Beta must be tech stable, no excuses") + the ask's definition | apply to every live-ops issue in the cohort; ZOM-534 (reset only after restart) and ZOM-556 must each get one answer — settle with a dated QA note, else keep them out of graded rows |
| One-offs | may overlap recurring slots; displacing one needs documented Product approval; the approver's latest dated call stands | base page ("Overlapping events are normal…", "should never displace a recurring slot without documented Product approval") + seeded approval and withdrawal | Robert is the Product owner on record (`page_zm3d_gdd`, `page_season_pass_spec` "Owner: Robert (Product)") |
| Rewards / setup | reward settings in force are the latest dated change; no setup task for work already done | base thread `C090N54TG79/1757478958.104989` + a seeded completion note away from it (consistent with the hidden base "plague stage rewards are fixed") | every event's reward change in Sep (Plague Race halved; Endless coin cut asked Sep 13) checked for a later record |
| Pushes | a push goes out only with copy that names the current game and the right event | base rename (`page_zm3d_gdd` 24 Jul 2025) + the ask's copy line | every Ready row read (14 rows) |
| Destinations | calendar in a Julia-owned sheet, linked from ZOM-78; recommendation as a reply in the ask's DM | prompt (named) + the ask | ZOM-78 is the only calendar ticket (title search) |

### 5.2 Two-reading tests to run at S8

1. Merged vs live on prod (Collect & Win) → the page's deploy rule + the dated deploy note decide; the first window is a
   single date. Both PT and UTC renderings of the same instant accepted.
2. Robert's thread approval vs his later DM → the later call by the same Product owner on the same item stands; no other
   Product approval exists (census of Robert's records Sep 17 – Sep 30).
3. Ready vs stale copy → the rename decides; only rows that name the old title are held (the 7-day lapse row does not and
   stays sendable).
4. Calendar page rows vs the ask's scope → the ask governs scope; the page governs rules. Accept any row layout.
5. Reward cut pending vs done → the dated completion note decides.
6. Quest reset after restart (ZOM-534): held or not → must be settled by a record before it can be graded (else ungraded).
7. Boss Arena → no record settles its prod state without touching SC-68: keep it out of graded rows ("any status accepted").
8. Sheet layout, wording, date format, PT/UTC → any equivalent accepted (learnings §8).

### 5.3 Boundaries the rubric accepts in full

Row layout (one row per beat or per window), labels, PT or UTC (or both) for the same instant, owner names where a
record names one (owner tokens such as `[PERSON_NAME_0092]` are never graded), the order of the recommendation, Boss
Arena's status.

### 5.4 Writes the rubric will not loosen

The reply goes in Frederick's DM (not a channel post); the calendar link goes on ZOM-78 (not a new ticket) — learnings §5.

### 5.5 Known-data-issue dispositions (learnings §51; `known_data_issues/synthcut.md`; S5)

| Card / defect | Disposition |
|---|---|
| SC-13 Trello list "BETA: Oct 10" vs "Beta target: Sep 30" | never cite the list name; dates come from dated messages and the ask |
| SC-14 Trello `dueComplete` vs `badges` (cards 54/56/58/67) | Trello completion flags are never a deciding fact (the W&C and Season Pass cards are not among the four, still unused) |
| SC-18 match3d#477 open/closed | never graded; Collect & Win readiness rests on the deploy record |
| SC-38 Season Pass ship date / analytics | never graded; only the November season boundary (spec cadence) is used |
| SC-62 reward import hourly vs 5 min | never graded; no row depends on import cadence |
| SC-68 Boss Arena on prod before its code | Boss Arena prod state never graded (§5.2 #7) |
| SC-28 Product OKRs numbers | never graded; the page's "retro against its target" rule is not used |
| SC-31 / SC-47 Domino live-ops outage, Weekly Quests | Domino rows of the calendar page never used |
| SC-7 channel membership, SC-36 Victor on invites, SC-70 Slack time zones | never graded; seeded invites exclude Victor |
| S5 §1 #1–#2: page "Weekly Leaderboards — DD / ZM3D — Live" vs no ZM3D rows; "Leagues" with no other record | never graded beyond "the weekly leaderboard reset push is Ready" (a sheet fact) |
| S5 §1 #5: push row "Win & Collect event start" for ZM3D | never grade a display name; the page states the two names are the same feature |

Coherence hazards touched (KB `coherence_hazards.json`, S5b §1): T04 (completion vs merge), S01, R07, L03, I15 (Julia's
Zombie Lane doc), I01/I18 (raw-shaped Slack rows, strikethrough retractions), Q01/Q04 (thread counters for appended
replies), L08–L10 (lifecycle stamps). `/create-scenario` S1 cites each with its disposition; all six categories are covered.

### 5.6 Chronology and the data horizon

Every seed lands at or before 2025-10-01T00:00Z and after the base events it names: the backend deploy note after
match3d#470/#472 (2025-09-30 15:53Z) and before the seed bound; Robert's approval after Martin's post (2025-09-17 15:10Z);
his withdrawal after Frederick's pause (2025-09-29 19:42Z) and after the last base message in his DM with Julia
(2025-09-30 20:46Z); the reward completion note after Leonard's "sounds good" (`C090N54TG79/1757524860.067099`). Base records
00:00–07:00Z Oct 1 that the task could touch: `#builds` Android #2029 (05:51Z) and its `#zombie-prs` commit post — no beat
depends on them. Plan dates (beta weeks, windows, the Nov 1 season and its Oct 31 00:00 UTC lock) are future plan fields.

---

## 6 · Hardness plan (rule 4) — storyline A

### 6.1 Loss channels (independent, each its own fact and surface, each flipping ≤ 2 rows of weight 5 by kind of work)

| Ch | v2 trap type (guide Part 3) | Convincing wrong source (who · when · authority) | Record that beats it | Findability | Survives complete retrieval because | Rows it flips |
|---|---|---|---|---|---|---|
| C1 | 1 · proving "done" across services | match3d#468/#470/#472 merged into main before the Sep 30 cut (GitHub, Sep 29–30) and the calendar page's "QA blockers cleared 26 Sep" (Frederick's own page) | a dated Douglas note on the `match3d-backend` Collect & Win windows PR: deployed to the dev stack only, prod with a named later backend release; the page's rule that windows need a deploy decides the first prod window | tier 3: another repo, a PR conversation comment (no Slack mirror) | "merged" and "QA cleared" are true; only the deploy meaning decides | Collect & Win first window (5) · reply names it as late (3) |
| C2 | 2 · a correction somewhere else | Robert's reply in Martin's `#zombie-art` Halloween thread approving a one-off in Plague Race's last-October slot (Product owner, documented approval) | Robert's later message in his DM with Julia withdrawing the event (no event art before the pivot call) — same person, same item, other container | tier 2: a DM with 286 Sep messages, the withdrawal near its end | the approval is real and the page's displacement rule is satisfied by it until the later DM | no Halloween one-off on the calendar (5) · Plague Race Oct 27–31 window present (5) |
| C4 | 7 · items outside the obvious filter | the calendar page's ZM3D rows (Weekly Leaderboards, Plague Race, Zombie Lane, Endless, Collect & Win), the natural scope | the ask's scope (every window, reset or start push) brings in the Season Pass November season (spec page) and a second beat the page omits (the weekly quest reset with its push, if §5.2 #6 settles; otherwise the daily login rollover) | tier 1–2 | the page calls itself "the single source of truth"; only the ask widens it | one row per member (5 + 5) · beat count (3) |
| C5 | 9 · work someone already did | Leonard's Sep 10 ask to halve Plague Race rewards, Vincent's "60, 120, 250?" and "sounds good" (same thread) — reads as setup still to do | a dated completion note away from that thread (Douglas in `#zombie-ops`, or on an open ticket) recording the new stage rewards live on prod; matches the hidden base "plague stage rewards are fixed" | tier 2 | the ask is real and has no visible completion in its own thread | no reward-change task in "still to do" (5) · rewards in force 60/120/250 (3) |
| C6 | 5 · a rule hidden in the data | the push sheet's "Ready" status on the 1-day lapse and D0-1 FTUE rows | the store rename (`page_zm3d_gdd`: renamed 24 Jul 2025) and the ask's copy line: both rows still say "Puzzles vs Zombies" | tier 1 to find, tier 2 to apply | the Ready flag is the owner's own column; the agent must read the copy against the rename | 1-day lapse push held for copy (5) · FTUE push held (3) |
| C8 | tool-surface blind spot (A3) on the tech-stable rule | the Linear list view and states (no comments returned; Ask_Carriers §6b) | a QA re-test note on the prod build on one open live-ops issue (or a `#zombie-bugs` thread reply under its Linear-bot post) showing the event's reset broken for players; the event is held | tier 2–3: one of ≈ 56 per-issue reads | the list view shows nothing wrong; only the per-issue read decides | that event held with its reason (5) |

Load-bearing pair named for the guide's "1–2 traps that carry the difficulty": **C1 (done across services) and C2
(correction elsewhere)** — two separate cross-source decisions on distinct v2 trap types, each naming its wrong source and
its winning record. C4–C8 add independent spread. The largest unit of discovery decides C2's 10 of 67 weight points
(15 %); no channel is near half. The calendar-ticket reuse (ZOM-78) is a weight-3 lookup and is kept as an ordinary row,
not a mechanism (DECISION_FLIP disposition, §6.3).

### 6.2 What will not be relied on (guide Part 4; learnings §45–46, §52, §54; Claire R3 §2.9, §3)

Volume, routine writes and clean totals (no weight-5 aggregate); the per-issue sweep is horizon, not difficulty, except
C8's single member; visible caveats (the page's "not yet live" is support, never the deciding record) and same-thread
corrections (Plague Race's "sounds good" is in the ask's thread, so C5's completion lives elsewhere); rules in the prompt
or a hub that lists sources; keyword-findable wording (seeded notes say what happened in plain words, not "dev only" /
"withdrawn"); Trello flags (SC-14); anything an obvious subagent brief sweeps by default (the deploy note is a backend PR
comment, not a client PR review).

### 6.3 Part 7 self-checks, run by `tools/hardness_v2_check.py`

Run on the pre-scenario sketch (`research/00_sketch_manifest.json`, `research/00_sketch_surface.json`; planned ids, so
containers are declared). First run (rev 0) flagged `DECISION_FLIP R_REUSE_TICKET: rule R_REUSE_TICKET (A8) can flip slots
of weight [3], no weight-5 slot`; disposition: a reuse write is lookup-band work, so the rule left the mechanism portfolio
and the row stays ordinary (never raise a weight). Re-run (verbatim, `research/hardness_v2_check_sketch.txt`):

```text
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      4 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 6 requirements: {'R2': ['R_DONE_DEPLOY'], 'R4': ['R_WITHDRAWN'], 'R1': ['R_SCOPE_BEATS'], 'R5': ['R_DONE_ELSEWHERE'], 'R6': ['R_COPY_CURRENT'], 'R3': ['R_TECH_HOLD']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   6 of 6 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     0 weight-5 total(s); 0 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  SKIP       RULE_IN_PROMPT  no prompt (04_Prompt.txt) yet  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

Positive control (the check is live): moving C2's withdrawal into Martin's approval thread
(`research/00_sketch_manifest_control.json`) gives `FLAG SAME_PLACE … 1 flagged` — "the correction and a superseded
version share slack:C08R8CHB0QL/1758121809.236839" (`research/hardness_v2_check_control.txt`).

Guide Part 7 in words: **done check** — C1: the merged PRs and the page say done; the backend repo shows the server
windows only on dev. **Same-place** — C2's withdrawal is in Robert's DM, not the approval thread; C5's completion is
away from the ask's thread; C8's re-test is on the issue or its bug thread, not the list view. **Filter** — the calendar
page's rows miss C4's two members. **Input** — no total is graded at weight 5; trap 8 is not used. **Decision flip** —
every mechanism flips at least one weight-5 multi-source row.

### 6.4 Planned surface and policy scores (UNCALIBRATED; rule 5)

Planned surface: 19 slots, total weight 67, 8 weight-5 slots, 4 ordinary samples plus a volume slot and two delivery
slots; weights by kind of work, never raised (`research/00_sketch_geometry.json`). Scored with
`research/scripts/geometry_mc.py` (adapted from Claire's, read-only logic), which grades simulated six-run baselines with
the bundle's own gate math (`difficulty_stats._gates`, **medium**, long-horizon). Output (verbatim,
`research/geometry_mc_output.txt`, 20,000 draws per scale):

```text
PLANNED SURFACE (pre-scenario sketch, UNCALIBRATED; mode medium, cap < 85%)
  slots 19  total weight 67  weight-5 slots 8
  weight by flip: {'C1': '8/67=12%', 'C2': '10/67=15%', 'C4a': '5/67=7%', 'C4b': '5/67=7%', 'C5': '8/67=12%', 'C6': '8/67=12%', 'C8': '5/67=7%', 'any:C4a,C4b': '3/67=4%', 'ordinary': '15/67=22%'}

WHOLE POLICIES (deterministic, no slips)
   22.4%  P0 lazy: Frederick's ask + the Confluence calendar page + push sheet as written
   22.4%  P1 + client PRs, Trello and Linear list view (no backend PRs, no issue comments, no DMs)
   53.7%  P2 + every ZM3D channel and thread incl. #zombie-art (no DMs, no backend repo, no issue comments)
   88.1%  P3 + DMs and issue comments (no backend repo)
   88.1%  P4 everything retrieved, Ready column trusted
   80.6%  P5 everything retrieved, calendar page taken as the scope
  100.0%  P6 perfect

SINGLE MISSES (everything else right)
   88.1%  miss C1
   85.1%  miss C2
   80.6%  miss C4 (all 2 members)
   88.1%    miss member C4a only
   88.1%    miss member C4b only
   88.1%  miss C5
   88.1%  miss C6
   92.5%  miss C8

SIX-RUN BASELINES (20000 draws per scale; gate math = difficulty_stats._gates, medium, long-horizon)
  scale = multiplier on every design miss rate (1.0 = design rates; <1 = a stronger Opus)
  scale 1.00: E[avg] 63.3% (p10-p90 52.7%-73.9%)  E[SD] 0.175  P(avg<85%) 1.00  P(<5 full) 1.00  P(SD band) 0.84  P(patterns) 1.00  P(all four) 0.83  E[full passes] 0.26
           P(row fails all six) >= 1%: {'S_C1_cw_first_window': 0.025, 'S_C1_reply_cw_late': 0.025, 'S_C2_halloween_not_scheduled': 0.015, 'S_C2_plague_last_oct_window_kept': 0.015, 'S_volume_beat_rows': 0.018}
  scale 0.75: E[avg] 71.2% (p10-p90 60.9%-81.1%)  E[SD] 0.167  P(avg<85%) 0.97  P(<5 full) 1.00  P(SD band) 0.80  P(patterns) 0.99  P(all four) 0.78  E[full passes] 0.55
  scale 0.60: E[avg] 76.0% (p10-p90 66.2%-85.3%)  E[SD] 0.157  P(avg<85%) 0.89  P(<5 full) 1.00  P(SD band) 0.74  P(patterns) 0.99  P(all four) 0.70  E[full passes] 0.82
  scale 0.50: E[avg] 79.2% (p10-p90 69.9%-88.1%)  E[SD] 0.148  P(avg<85%) 0.79  P(<5 full) 1.00  P(SD band) 0.68  P(patterns) 0.99  P(all four) 0.61  E[full passes] 1.05
  scale 0.35: E[avg] 84.3% (p10-p90 76.1%-92.0%)  E[SD] 0.130  P(avg<85%) 0.51  P(<5 full) 1.00  P(SD band) 0.54  P(patterns) 0.97  P(all four) 0.38  E[full passes] 1.52
```

Design miss rates (scale 1.0): C1 0.55, C2 0.50, C4 0.35 per member (ρ 0.5), C5 0.45, C6 0.40, C8 0.45; slips 0.03–0.06;
a per-run thoroughness latent (loading 0.5) correlates the channels. These are assumptions: the Opus 5.5 ledger
(`hardness_ledger.py priors --model claude-opus-5-5`) holds Beta(1,2) one-trial priors for A7 and A14–A17, Beta(1.86,2)
for A1 and nothing for A3, A8, A11, A24 or A25; Claire's R3 (`task_inputsH/Working_Files/research/R3_opus_failure_modes.md`
§2) verifies the done-across (2.1), correction-elsewhere (2.2), outside-filter (2.4) and record-never-opened (2.5) modes on
completed tasks, and finds follow-through and slips contradicted (2.3, 2.9).

**Against the goal's bar (E[avg] ≤ 77 %, P(all gates) ≥ 0.5):** at the design rates 63.3 % / 0.83; the bar holds down to a
miss-rate scale of about 0.6 (76.0 % / 0.70); at 0.5 P holds (0.61) but E[avg] is 79.2 %. **Sensitivity — judgment solved**
(C4 and C6 missed only 10 % of the time, `research/geometry_mc_sens_judgment.txt`): 71.7 % / 0.71 at scale 1.0, 77.7 % /
0.60 at 0.75, 81.4 % / 0.47 at 0.6. **Binding risk: a strong Opus.** Every single miss leaves a run at 80.6–92.5 %, so the
85 % cap needs about two misses per run on average; retrieval policies P0–P2 score 22–54 %, but a run that retrieves
everything and slips once scores 81–88 %. C1 and C2 therefore carry the margin, and C4/C6 must keep their deciding record
off the first-read path. `/create-scenario` replaces this with `hardness_forecast.py forecast --design` on the real
`01_Gradable_Surface.json`, pre-registered (S9b).

### 6.5 Spread (rule 5)

Each channel's deciding record sits on a different surface — a backend PR comment (C1), a DM (C2), the ask vs the page
(C4), a channel post away from the ask's thread (C5), push-sheet copy vs a Confluence rename (C6), one per-issue note in a
56-issue sweep (C8) — with findability tiers 1–3, so runs fail different subsets: P(patterns) ≈ 1.0 and P(SD band)
0.68–0.84 at scales 0.5–1.0. The highest predicted all-six miss is C1's pair at 2.5 % (scale 1.0) — VALID workload if it
happens (every value reachable), not a predicted all-fail. C1 is the deepest channel and the first to soften if the
pre-check shows a universal miss.

---

## 7 · Volume plan (honest, never padded)

| Phase | Services | Calls, shortest sufficient path | Why each is necessary |
|---|---|---|---|
| Anchors and rules | Slack (the ask), Confluence (calendar page, live-ops engine, Season Pass spec, GDD), Sheets (push sheet metadata + "PNs Beta" + translated tab), Docs (UA brief), GCal (pod review / season lock), Slides or Gmail (UA plan) | 12 | each carries a different rule, date or scope |
| Enumeration | Linear (live-ops issue list, 3 pages + ZOM-78 search), GitHub (client and backend PR searches, 4), Slack (`#zombie-design`, `#zombie-art`, `#company-internal`, `#zombie-ops` windows and searches, 8), Snowflake (describe + Plague Race query, 2), Trello (board, 1) | 19 | the scope rule needs every beat and every live-ops issue |
| Per-record, no bulk call | ≈ 56 live-ops issues × `linear_list_comments` (56); ≈ 12 issues' fix PRs × (get + comments) (24) | **80** | comments and PR conversations have no bulk call (Ask_Carriers §3, §6b); the tech-stable rule needs each issue's prod state |
| Per-record, sweepable | `#zombie-bugs` report threads | 0 counted | thread replies come back from `slack_conversations_search_messages` (§6b) |
| Hidden authorities | Robert DM history (2), backend PR comments (2), the completion note (1) | 5 | one authority each |
| Writes + read-backs | Drive folder (1), sheet create + values + read-back (4), DM reply (1), ZOM-78 comment (1), 1–2 tickets (2) | 9 | each write is requested |
| **Total** | 11 services | **≈ 125** (observed counted calls on comparable completed tasks 163–1,209 per run, Claire R3 §1/§2.10) | ≥ 500 is **not** reachable without padding; the 100-call platform floor is met with a margin of ≈ 25 on the shortest path |

Every surface and its shortcut audit are re-derived at S2/S7; if S2's census finds fewer live-ops issues or fix PRs, the
floors in D2 drop with it and are never padded.

---

## 8 · Cohort spine (hard gate 3: ≥ 40 records × ≥ 3 per-record surfaces over ≥ 2 services)

The volume exception lowers only the call-budget and per-record floors; the cohort floor stays (`hardness_gate.py`
`cohort_size`, verified in its source). Populations checked (S2): Zombie Lane nodes (live sheet not visible), Season Pass
tiers (NO), quests (no list), event reward lines (~25), push rows (14, one read), Trello cards (sparse, SC-13/14), store
reviews (templated text), levels (level design, not GTM). The one natural ≥ 40 population on the plan's decision path is
**the ZOM live-ops issues**: a draft keyword rule (title names a live-ops feature; open at the clock or closed in Sep 2025)
gives **56** (Done 24, Todo 12, Backlog 8, In Progress 6, In Validation 3, Canceled 2, Duplicate 1; S2 row 10). Per-record
surfaces: (1) Linear comments — **0 in the whole base**, so every note is seeded under the necessity rule (decisive for
15–40 %, neutral QA re-test notes on the rest; never on a Done issue after its `completed_at`); (2) the fix PR (GitHub, for
the ≈ 12 that have one); (3) the `#zombie-bugs` report thread (Linear-bot post + replies; sweepable, support only). Shortcut
audit: the list call returns state and description but no comments; the decision (does it break the event on prod?) lives in
the comment or thread. **This is the design's weakest structural point:** the seeding is large (dozens of Linear comments),
the sweep resembles a defect gate (the overlap with Vincent's storyline must stay out of the graded rows, §4.4), and
Hardness v2 says the volume itself adds no difficulty. If S2 finds a natural population that is closer to the calendar
(for example per-window records the backend already exposes), it replaces this one.

---

## 9 · Writes and ownership (rule 6)

| Write | Trigger the persona owns | Write access |
|---|---|---|
| Beta calendar (Google Sheet) | Frederick's ask to Julia; the page names Design (Julia) in the weekly walk | Julia-owned: created at run time with `gsheets_create_spreadsheet(title, initialSheetTitle, driveFileId)` in a Julia-owned folder (seeded with `owner_email` Julia in both Drive and Sheets rows if seeded at all, learnings §31); extra tabs need `gsheets_batch_update addSheet` (S4 §2). Never the Resource-owned push sheet |
| Recommendation reply to Frederick | the ask itself | Julia is a member of `D05SD5QLG94` (YES) |
| Calendar link on ZOM-78 (comment) | the ask names the calendar ticket | Linear unscoped; ZOM team writes confirmed in the pre-check |
| Optional: one or two setup tickets (e.g. the push copy fix) | the ask's "what is still to do, by whom" | Linear unscoped; reuse an existing ticket where one covers it |

---

## 10 · Risks and open items

1. **A strong Opus** (scale ≤ 0.5) pushes E[avg] past 77 % and, with judgment solved, P(all gates) under 0.5 at 0.6 (§6.4).
   C1 and C2 must stay off the first-read path; verify with the pre-check before the baseline.
2. **Cohort (§8):** the ≥ 40 floor rests on seeded per-issue notes. The overlap with Vincent's defect gate must stay
   ungraded; if the user prefers, a different population is the S2 decision to revisit.
3. **Boss Arena and quests** (§5.2 #6–#7): SC-68 keeps Boss Arena ungraded; ZOM-534 needs a settling record before the
   quest beat can be graded.
4. **Ten injected services without Confluence or Snowflake** means Docs, GCal, Gmail or Slides, Trello and Drive must each
   carry a natural fact (Frederick's UA brief or deck, the pod review / season lock events, a beta-list card comment, the
   folder). Contacts has no natural role yet; S1/S2 decide, never padding (§3a).
5. **Language:** seeded DM text only in English DMs (Frederick, Robert); Julia–Leonard, Brian, Vincent and Claire DMs are
   Turkish or mixed (S4 §3).
6. **Plague Race cadence** is implicit in Snowflake rows (no doc states "every 5 days"); settle it with a dated record if a
   window is graded.
7. **Theme:** ZM3D content (zombies, "outbreak" in base push copy) is unavoidable for this persona at this clock (D3).
8. Ledger priors for A3, A8, A11, A24, A25 are empty: every forecast stays UNCALIBRATED until the pre-check.
9. **Seed realism:** Robert's approval and withdrawal must fit his Sep 29–30 stance (pivot, "lean hardcore",
   `C090N54TG79/1759176983.189479`) and Frederick's playable pause; the completion note must match the hidden base
   "plague stage rewards are fixed" and the 60/120/250 ladder.

---

## 11 · Decisions needed from you

| # | Decision | Recommendation |
|---|---|---|
| D1 | Storyline | **A — ZM3D beta-weeks live-ops and player-push calendar** (§4.4). Alternatives: C (Season Pass Season 2) if you weigh Product & Design fit over reach and volume; B is not recommended (role fit and hazards) |
| D2 | Volume exception (GEN_EXECUTION §3a; ≥ 500 necessary calls not reachable without padding) | **Yes**: `volume_exception {call_budget_floor: 115, per_record_floor: 70}` (the §7 shortest path ≈ 125 with 80 per-record; re-derived at S2/S7 from the census), with your confirmation recorded as `requester_confirmation`. Floors stay above the platform's 100-call Long Horizon floor; every other extreme target stays (≥ 10 services, ≥ 120 rows, cohort ≥ 40, ≥ 12 traps, …) |
| D3 | Theme screen (playbook 01 S0: no zombie/outbreak theme) | **Waive for this task, recorded:** every Julia storyline at this clock is ZM3D; Claire's R3 §5 found 0 refusals or fallbacks in 13 Opus 5.5 runs on ZM3D data. Mitigation: seeded text says "ZM3D" / event names, never "infection" or "outbreak"; every pre-check and baseline is checked for model fallback |
| D4 | Review waiver | No `REDTEAM_*` variables are set in this shell (`env | grep -c '^REDTEAM'` → 0), so `redteam_review.py --dual` cannot run. Either set `REDTEAM_*` (preferred), or approve a recorded `RED TEAM FALLBACK:` using this session's independent GPT `redteam` and `oracle` subagents on the design (kept in every Unresolved line until covered, learnings §44). This analysis itself was reviewed that way (§13) |

---

## 12 · The goal's seven rules, and where this analysis answers each

| Rule | Answered in | Status at this stage |
|---|---|---|
| 1 UGT (each material choice fixed by the prompt or a Julia-visible record, or bounded; every rule sentence applied to every item; census before completeness) | §5.1 (home + census per decision), §5.2 (two-reading tests), §5.3 (bounded choices), §2 reach table | planned; S1/S8 run the censuses and the fork sweep (ZOM-534, Boss Arena, Plague Race cadence named) |
| 2 Fit (Product & Design inside Marketing and GTM) | §3 | argued, with the Engineering Ops and Product Management slide risks and their mitigations |
| 3 `/injection` (whole-universe check, seeds after base events, tool-visible) | §1 row 1, §5.5, §5.6, §10 items 4, 5, 9 | planned; `base_check`, `base_claims` and `hg.py lint` run at injection |
| 4 `/hardness` (≥ 3 independent channels, none over half, ≥ 2 cross-source decisions on distinct named v2 traps with wrong source and winning record; nothing passes by doing nothing; weight 5 by kind of work) | §6.1 (six channels on six surfaces, largest 15 %), §6.2, §6.3 (Part 7 checks + positive control) | sketch CLEAN on all six applicable checks after the DECISION_FLIP disposition |
| 5 Spread (graded findability; E[avg] ≤ 77 %, P(all gates) ≥ 0.5, UNCALIBRATED) | §6.4, §6.5 | 63.3 % / 0.83 at design rates; holds to scale ≈ 0.6; judgment-solved sensitivity 71.7 % / 0.71 (both stated) |
| 6 Writes (authorized trigger, proven access, Julia owns Drive/Docs/Sheets targets) | §9 | planned; each write confirmed in the pre-check |
| 7 Alignment (every OE and rubric row traces to incorporated facts; no traps, rules or answers in the prompt) | §5.1 homes, §6.2 | the prompt is not written at this stage; `RULE_IN_PROMPT` runs once it exists |

---

## 13 · Independent review of this analysis

_(filled after the review below)_
