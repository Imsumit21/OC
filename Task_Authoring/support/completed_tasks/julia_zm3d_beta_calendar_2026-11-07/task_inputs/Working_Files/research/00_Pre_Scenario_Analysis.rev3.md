# Pre-scenario analysis — Julia Lawson · Product · Marketing and GTM · Planning and decision support · Long Horizon · Medium · Oct 1, 2025 (synth-cut)

Analysis only — **rev 3** (with the round-4 fixes), after five independent red-team rounds (§13; round 5 PASS). This file holds no prompt, Oracle Event or
rubric text; it prepares `/create-scenario`. No SQL was written or executed. Writes went only to
`Task_Authoring/task_inputsS/` (this file, `Working_Files/research/`, and the `00_Task_Context.json` refresh) plus the
helper caches under `Task_Authoring/support/local_search/`. `Evals/` (including its input store), `claude/`,
`Task_Authoring/tools/`, the universe and the other task folders were not written.

| Item | Value (source) |
|---|---|
| Clock | `Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)` (`hg.py universe show`) |
| Seed bound | `2025-10-01T00:00:00Z` = Tue Sep 30, 5:00 PM PT. Every seeded event timestamp at or before it (`sql_lint.py`); base records 00:00–07:00Z Oct 1 exist and are checked as possible superseding records (§5.6) |
| Persona today | Wednesday, October 1, 2025; "yesterday" = Tuesday, September 30 (GEN_EXECUTION §0a; learnings §20) |
| Universe | synthcut, `hg4-synth-sep30cut v16`; no shutdown rules; Victor Barnes departed April 2025 and cannot act |
| Context | `task_context.py --task-dir Task_Authoring/task_inputsS --write --require-source` → `source.status: ready`, `kb_status: bound`, `context_hash 7b0cc66ffd451f41aff7b1db7367e86f141b0d1fa444f1839482cf2e5839dc5e` |
| Assignment | `00_Assigments.md` sha256 `e8b8269803d55217…`; mode **medium** (cap < 85 %, design target ≤ 77 %); Long Horizon → `effective_profile: extreme` |
| Tools | `Task_Authoring/tools` last commit `58c37b1` (2026-11-03 03:40 +0530, re-checked for rev 3); one untracked `tools/stage_check.py` from another session (not touched). Re-check `git log -3 -- Task_Authoring/tools` before any gate run (learnings §57) |
| Evidence files | `Working_Files/research/`: `S1_liveops_census.md` + `S1b_liveops_followup.md` (live-ops census), `S2_cohort_options.md` (≥ 40 populations), `S3_alt_storylines.md` (B and C), `S4_reach_writes.md` (reach, write tools, DM languages, `can-see` output), `S5_coherence_hazards.md` + `S5b_kb_transcription.md` (hazards, KB), `S6_art_readiness.md` (per-beat art records), `S7_backend_config_and_gh_tools.md` (backend leads and GitHub tool semantics — see Method); spine lists `raw/spine_open_issues_nonba.json` (12), `raw/spine_merged_liveops_prs_nonba.json` (22), `raw/liveops_threads_sep.json`; rev 3 sketch `00_sketch_manifest_rev3.json` (+ `_rev3_control`), `00_sketch_surface_rev3.json`, `00_sketch_geometry_rev3.json` (+ `_rev3_sens`); outputs `hardness_v2_check_rev3.txt` (+ `_rev3_control`), `geometry_mc_rev3.txt` (+ `_rev3_sens`); `tool_reach.txt`, `tool_entity.txt`; `raw/` (reads through `tools/hg.py`), `scripts/`. Earlier sketches (rev a–e, the no-C5 variants) and `00_Pre_Scenario_Analysis.rev0–rev2.md` are kept for history only |
| Method | Seven research workers (S1–S7) plus two follow-ups (S1b, S5b) on disjoint briefs; the build session wrote up findings where workers ran out of steps (each file says so) and re-ran every load-bearing check itself (`can-see`, Part 7 checker, geometry, spine counts). **Process deviation (disclosed):** S7 read the `match3d-backend` and `match3d` working copies under `Services_Data/github/root/` with direct file reads, not through `tools/hg.py` (`hg.py search files` lists those paths; `hg.py search get` cannot read non-JSON blobs). Its code facts are **unverified leads**: used only to remove design dependencies (C5, Plague Race dates), never as a seeded or graded fact; `/create-scenario` S1 re-verifies them through the agent's GitHub tools |

---

## 1 · What a 5 needs at each gate

| Gate | A 5 / PASS needs | What this task must do to get it |
|---|---|---|
| `/injection` (static, Checks A–C) | A: every id, reference and person token exists or is new and collision-free, and every seeded fact agrees with the **whole** universe (learnings §10, §14, §15). B: SQL valid against `universe_schema_live.json`, only writable tables (never Snowflake, Confluence or `_changelog`, §26, §50). C: every seed after the base events it relies on (§13, §17), at or before the seed bound, no Linear comment after its ticket's `completed_at` (§50, §57), companions present (thread counters, `updated_at`, per-attendee GCal copies and invitation mail, `commented` timeline events). | Census every event, person and claim across all 13 services before seeding (S1/S1b/S5/S6). Douglas has **no** comment or review on any `match3d` PR in base (his 98 reviews are on backend, liveops and Dominoes repos), so C1's comment is Owen Baker's on his own PR, with its `#zombie-prs` INT-01 copy (integration window ends 2025-09-30). The issue spine uses **open** issues only, so no note follows a `completed_at`. Seeds must also read naturally next to base records after the seed bound (Robert's Oct 1 03:32Z DM message, §5.6). |
| `/prompt` | Every scored sub-dimension 5: UGT (one end state after the two-reading test), Feasibility, ACL reachability (every required scoped read YES), no tool names, not contrived, today = Wed Oct 1, Truthfulness, investigation + action, persona, **business function 5, competency 5, task skill 5**, a load-bearing complexity dimension, data seeding, Cross-Service Coherence 5 on all task-touched data incl. pre-existing defects — the dimension "fails on the **presence** of an inconsistency itself, whether or not it would cause an agent failure" (`1_Prompt_Eval.md` §1.5, §2.1, §3.2). | Fit argued in §3 (the competency gate is a local hard FAIL). Rules, definitions and exceptions live in records; the prompt is an ordinary request naming its destinations. **No artifact that carries a known contradiction is required or cited** (§5.5 `excluded`); the push sheet's translated tab is explained by a dated owner statement; residual risks are named (§10.4). |
| `/hardness` | Score 5 = "genuine model failures invalidate the central result/delivery or defeat much of the core task" on the single unhinted Opus 5.5 run (`1A_Hardness_Eval.md` §5); 3–4 still PROCEED. | The central result is the calendar Frederick runs the bought cohort on: a missed trap starts Collect & Win before its prod windows exist, runs a withdrawn one-off over the recurring race, sends old-name pushes to bought users, runs a beat players cannot enter, or misses the Season Pass config lock — consequential, not cosmetic (§6). |
| `/oe` | PASS: complete critical path (discovery, dependencies, every required write) with accurate tools, parameters, ids and expected data; no non-action or final-response event (`2_Oracle_Events_Eval.md`). | Every deciding record reachable from a prompt noun by a natural call; expected values quoted from records; catalog tool names only — e.g. `github_get_issue_comments` for PR conversation comments (observed to accept PR numbers, S7 §3.3), `gsheets_values_update`, `slack_send_message`, `linear_create_comment` (S4 §2). |
| `/rubric` | No Major, no Moderate, Minor < 5 %; weights 1/3/5 by kind of work; ≥ 1 Outcome; Process ≤ 50 %; no row passable by doing nothing; one fact per row and never in ≥ 3 rows; ≤ 5 samples per group + a volume row + direct exception rows; predicted all-fail 0 (`3_Rubrics_Eval.md`; GEN_EXECUTION §3). | The planned surface (§6.4) keeps each trap's miss on ≤ 2 rows, weight 5 only where the work is multi-source; exclusions are graded as positive results (the reply calls the Halloween one-off off and gives the reason; Plague Race appears in the Oct 27 – Nov 2 week), never "leaves X alone". |
| `/create-difficulty` (`12_Difficulty.md`) | Six Opus 5.5 slots with provenance, ≤ 2 errored; corrected average **strictly < 85 %** (medium); < 5 full passes; population SD 0.10–0.30; ≥ 2 failure patterns, largest ≤ 50 %; ≥ 100 counted calls (golden run if any, lowest governs). | Six independent loss channels on five services with graded findability (§6.1, §6.5). Honest shortest path ≈ **110** counted calls with the issue + PR spine (78 per-record), ≈ 44 without the PR spine — **at, not above,** the 110 design margin (§7, D2, D5). |
| Local stage gates | `stage_gate.py` scenario → … → release PASS; `hardness_gate.py` at `effective_profile: extreme` (≥ 10 services, ≥ 120 rows, cohort ≥ 40 × 3 surfaces, ≥ 12 traps, …); dual red team or a recorded `RED TEAM FALLBACK:`. | Decisions D2 (volume exception), D4 (review fallback) and D5 (cohort spine) in §11; gate 3 (cohort shape) is an **open blocker** (§8). |

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
  `Evals/references/rules/task_categories.md`). The calendar decides which live-ops features the beta cohort plays and
  when — product decisions on a prototype under evaluation (Leonard will "decide: either iterate or pivot the core game"
  on the beta data, `C090N54TG79/1758517286.431379`) — and sets each beat's design requirements: which one-off runs, which
  beat is held for a player-facing fault, what setup is still to do and by when (the Season Pass November config). Julia
  owns the live-ops icon system and Zombie Lane design docs (`f_744027532fb1b0cc8821c4`, `f_023c7331d7e34900bd226f`, S4 §1).
  S6 found no per-beat art-readiness surface, so art evaluation enters only through the one-off (no event art before the
  pivot call) — the fit rests on product decisions and design requirements.
- **Competency — Marketing and GTM** ("Demand and retention, GTM, communications"; typical personas include PM). The
  deliverable is the **beta-weeks retention calendar and player-push plan** for the bought-user beta: in-game live-ops
  campaigns, their start pushes and lapse reminders, timed to the beta buy and sent to the GTM owner (Frederick, Growth/UA)
  as a recommendation. Every graded value is a calendar, campaign or communication call — never a ticket state, a PR
  verdict or a build fact for its own sake.
- **Task skill — Planning and decision support** ("Recommend a course of action, plan, or schedule, with tradeoffs"):
  a schedule (which beat runs in which window, what is held and until when, what moves earlier) with the tradeoffs
  Frederick asked for — a late Collect & Win against a clean first week, the recurring race against a one-off, holding
  lapse pushes against D1 re-engagement, a week without leagues against a broken weekly session, an earlier Season Pass
  config deadline against the owner's date.
- **Role.** In the task, the seeded ask from Frederick makes this Julia's job. Background (not on the task's path): the
  Confluence calendar page names "Design, led by Julia Lawson" for exactly this weekly walk with Frederick Stone.
- **Risk (named, mitigated in design).** The issue + PR spine (§7, §8) is engineering-shaped and in rev 3 makes up 78 of
  ≈ 110 necessary calls; if the sweep becomes the output, the task reads as Engineering Ops. Mitigation: the spine is
  input only — no graded row is a ticket state or a PR verdict; the request reads as the beta GTM calendar. The opposite
  slide (Product Management) happens if communications drop out; the push plan and the reply to the GTM owner stay graded.

---

## 4 · Storylines

All of Julia's 2025 work is ZM3D: Domino Delights is in maintenance and its live-ops area carries SC-31/SC-47; the
Mattel, Combo Fighter and web-distribution arcs are normal-only. All three candidates are therefore ZM3D (theme: D3).

### 4.1 A — ZM3D beta-weeks live-ops and player-push calendar (recommended)

**Situation at the clock (verified, S1/S1b/S6; Julia-visible unless marked).** Leonard set "Beta target: Sep 30" with Win &
Collect, Reward Animations, Season Pass and Infinite HP Boss Mode in the beta pipeline (`C05KNDCHAAG/1757704290.799329`),
then descoped Axe Arena and asked for clean data from a tech-stable beta in 15–20 days before an iterate-or-pivot call
(`C090N54TG79/1758517286.431379`; Brian `C05KNDCHAAG/1758558164.541689`). UA scales once the stores approve the Sep 30
builds ("when it's approved we'll start buying users at small scale", `C0880U9751A/1757561483.446549`); small Unity
retention campaigns already run (Frederick on Sep 30: "We are only running the retention campaigns", a reply under
`C0880U9751A/1759211437.306779`). Live for players: Plague Race, Endless Monster Mode, weekly leagues, Zombie Lane, quests
(ZOM-534 "Quest points not resetting until app restart in production", In Progress), daily login (ZOM-556, Todo) and Season
Pass (iOS 0.3.49 released Sep 29, `C0880U9751A/1759182908.627389`). Built but not live: Collect & Win (match3d#468 merged
09-29 16:13Z, #470/#472 merged 09-30 15:51–15:53Z; Julia's own Sep 22 notes: "[PERSON_NAME_0067] and Douglas feature
completed Win and Collect", `C05KNDCHAAG/1758558302.777379`; the hidden `#zm-collect-win` shows it tested on the dev server
through Sep 26) and Boss Arena (endpoints "ready for testing on dev", `C08R6BF4ENN/1756747348.667629`; SC-68). Not built:
Axe Arena (descoped) and a Halloween one-off (Martin's one-line idea `C08R8CHB0QL/1758121809.236839`, no replies, card,
ticket or push row). On Sep 22 Vincent could not join the weekly leaderboard even after killing the app (standalone report
`C08R27X0EAH/1758546048.524829`); in Oliver's thread `C08R27X0EAH/1758546119.789009` he got in "after a moment", Oliver
reverted the change, and the thread ends "yep, it's working fine right now" (`…/1758550789.777509`); ZOM-429 "Leaderboard next session doesn't start without killing the app" is open
(Backlog, assignee Douglas). Push sheet `f_a325dd4af80afc5994d5dc` "PNs Beta" has 14 rows: Ready = lives recharged, 1-day
lapse, 7-day lapse, D0-1 FTUE, Plague Race, weekly leaderboard reset; the 1-day lapse and FTUE rows still say "Puzzles vs
Zombies" (renamed in August: "Rename product" in the commit list `C08R27X0EAH/1754330589.504269`); the quests and
login-calendar rollover rows are Not Ready. ZOM-78 "Event Calendar For Zombie Match 3D" sits in Backlog. Context only, never
on the task's path: the Confluence calendar and Season Pass pages, the Snowflake event table and the backend repository
(§5.5).

**The work for Julia on Oct 1.** Frederick (owner of the calendar and of the beta buy) asked her yesterday, in their DM, for
the live-ops calendar of the four beta buy weeks (Mon Oct 6 – Sun Nov 2): which beats run in which windows, what is held and
until when, the push for each beat, what is still to do before each runs and by whom, and her recommendation with the
tradeoffs; the calendar goes in the sheet in her Drive folder, linked from the calendar ticket, and the recommendation goes
back to him in the DM. (The ask is a seeded record; this is its meaning, not its text.)

**Services.** Native and load-bearing: Slack (`#zombie-design`, `#company-internal`, `#zombie-art`, `#zombie-ops`,
`#zombie-bugs`, `#zombie-match3d`, DMs with Frederick and Robert), Linear (ZOM live-ops issues, ZOM-78, ZOM-429), GitHub
(`match3d` live-ops PRs), Sheets (push sheet), Trello (Axe Arena card), Drive (her root). **Confluence, Snowflake and the
backend repository are context only — never required, never cited** (§5.5).

**Injection plan: ten injected services, each with its own fact** (companion-only rows such as invitation mail, timeline
events or `#zombie-prs` mirrors are counted separately and never toward the ten):

| # | Service | Seeded record (planned) | Fact it carries |
|---|---|---|---|
| 1 | Slack | Frederick's ask in `D05SD5QLG94` (Sep 30); Robert's approval reply in Martin's `#zombie-art` thread (Sep 18); Robert's withdrawal in `D05GU6L0XFH` (Sep 30, between 20:46Z and the seed bound); Vincent's prod check of 0.3.49 as a root post in `#zombie-match3d` (Sep 30) | anchor, scope and destinations; C2; C8 |
| 2 | Linear | Douglas's owner note on ZOM-429 (Sep 23; he is the assignee); dated re-test or owner notes on the other 11 open live-ops issues — a few decisive (e.g. fixed on the Sep 30 build, so not still to do), the rest neutral | C8's wrong source; issue spine (§8) |
| 3 | GitHub | Owen Baker's conversation comment on his merged `match3d#470` (Sep 30, after the merge) + INT-01 mirror; a few human review notes on live-ops PRs (the PR spine's deciding members) | C1; PR spine |
| 4 | Docs | Frederick's beta brief (shared with Julia), in his voice as calendar owner: span and server time (UTC); scope (every window, reset or start push, not only the events everyone lists); Collect & Win windows Mon–Tue / Wed–Thu / Fri–Sun from 00:00 UTC; windows go live only with a prod backend deploy; overlaps are fine and a one-off may displace a recurring slot only with Product's (Robert's) approval; a beat runs only if its live-ops changes carry no open review blocker and players can enter, score and claim on prod even after a restart; pushes go out only if Ready and their English copy names the game only as "Zombie Match 3D" and events only by their ZM3D names, else held for the copy owner; beta pushes are English-only (UK/US buys) and the translated tab is the old Domino set awaiting ZM3D localization; Season Pass seasons open on the 1st at 00:00 UTC with config locked 24 h before; Boss Arena off this calendar until the pivot call | the rules every decision needs — rules, never answers (it names no held or late beat) |
| 5 | Slides | Frederick's beta UA plan deck: the scaled beta-cohort buy, Mon Oct 6 – Sun Nov 2, and its geos — worded so it does not deny the retention campaigns already running | the calendar's span |
| 6 | Gmail | Brian Foster's handoff mail to Julia (Frederick in copy, English), committing the November Season Pass config for "Fri Oct 31, 10:00 Istanbul time" | C9's input |
| 7 | GCal | Douglas's backend release as a plan event, Wed Oct 8 (attendees incl. Julia and Owen; per-attendee copies and invitation mail) | C1's prod date |
| 8 | Drive | a Julia-owned "ZM Live Ops" folder (owner Julia in Drive) | the calendar's destination |
| 9 | Sheets | a Julia-owned calendar sheet in that folder with Frederick's headers (owner Julia in both Drive and Sheets rows, learnings §31) | the write target and its column contract |
| 10 | Trello | Brian's comment on the Axe Arena card in the "Oct 21" list (not the BETA list) moving it to the first post-beta release | Axe Arena's slot (an ordinary sample) |

Contacts carries no natural fact and is not used. Drive and Sheets carry only the destination, Trello and Slides a sample and
the span; whether each holds a fact no other record repeats is checked by the S9 literal-value sweep, and a failure means
finding a natural tenth carrier, never padding (§10.7). No GCal event for the Season Pass lock is seeded: it would show the
instant C9 asks the agent to compute.

**Hardness opportunities (each its own fact; detail §6).** v2 trap 1 (C1), trap 2 twice on different people, items and
containers (C2, C8), trap 4 (C9), trap 5 (C6), trap 7 (C4). Trap 9 is available inside the issue spine (an open issue shown fixed
on the Sep 30 build by a dated note) and is a `/create-scenario` option, not counted here.

**Volume.** ≈ 110 counted calls on the shortest path with the issue + PR spine, ≈ 44 without the PR spine (§7).

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
| Fit (function / competency / skill / role) | 5 / 5 as the GTM calendar (risk §3) / 5 / asked by the calendar owner | 3–4 (Growth) / 5 / 5 / weak (UA is Frederick's) | 5 / 4 / 5 / design partner |
| Native services on the required path | 6 (Slack, Linear, GitHub, Sheets, Trello, Drive); Confluence, Snowflake and backend code context only | 5–6 | 6 |
| v2 trap types with base precedent | 1, 2, 4, 5, 7 (+ 9 inside the spine) | 2, 5 | 4, 5 |
| Consequence of a miss (for `/hardness` 5) | the bought cohort plays a broken or wrong calendar; old-name pushes go to new users | a mis-specified test cell | a wrong reward tier |
| Known-issue cards | SC-13/14/18/38/62/68 nearby, all kept off the path (§5.5) | SC-11/12/23/28/29 on the core numbers | SC-38 on the core dates |
| Natural population ≥ 40 | **no**: 12 open live-ops issues + 22 merged live-ops PRs = 34 records of two types (§8, D5) | no | 60 tiers, invisible to Julia |
| Honest volume | ≈ 110 with the issue + PR spine (§7) | < 100 | < 100 |

**Distinctness.** Vincent's `vincent-zm3d-release-gate` decides, defect by defect, whether two Sep 30 submission builds may
ship, with release-ticket blockers. Claire's `claire-zm3d-october-object-handoff` decides which new art objects go to level
design for the October batch. A decides the live-ops and push calendar for the bought-user beta: its population is the
beta's beats and the open issues and merged PRs behind them; its authorities are the GTM owner's brief, the Product owner's
one-off call, the deploy record, the prod check and the config owner's date; its outputs are a calendar, a push plan and a
recommendation. Overlap to keep out: the issue and PR spine must never become a defect or release gate — no graded ticket
or PR verdict; the done-across trap is a server-window deploy for an event, not a fix in a build. A also differs from the
completed Julia tasks (`julia_zm` difficulty register, `julia_dd` close-out) and from Douglas's beta server sign-off.

**Recommendation: A, conditional on D5.** It is Julia's natural job on her actual today; its hard decisions survive complete
retrieval (a merge against a deploy plan, a thread approval against a later DM, an owner's restart note against a later prod
check, a Ready flag against the copy rule, an obvious event list against the brief's scope, a lock-day date against a UTC
lock); and a miss changes the calendar the bought cohort plays. Its structural gaps — the cohort shape (§8) and a horizon
margin of zero (§7) — are stated, not solved.

---

## 5 · UGT plan (rule 1) — storyline A

### 5.1 Rules every decision needs, homed in incorporated records (no Confluence page, Snowflake table or backend file is a home)

| Decision | Rule (meaning, not wording) | Home (planned; base where possible) | Census / proof needed |
|---|---|---|---|
| Span and time base | Mon Oct 6 00:00 UTC – Sun Nov 2 23:59 UTC; windows stated in server time (UTC) as start–end instants; PT renderings of the same instant accepted (PDT until Nov 2 09:00 UTC), a different instant is not | UA plan deck (span) + the brief (server time) | every graded date is one instant with both renderings precomputed |
| Scope | every ZM3D beat players can see in the span — a window, a reset or a start push; Boss Arena off this calendar until the pivot call (a dated decision, not a prod claim, so SC-68 is untouched) | the brief (one hop from the anchor) | census of every live-ops feature in the beta build (S1b §6) and all 14 "PNs Beta" rows; no completeness claim without it (learnings §23) |
| Window cadence | Collect & Win groups Mon–Tue / Wed–Thu / Fri–Sun from 00:00 UTC; Season Pass seasons on the 1st 00:00 UTC; quests and login-calendar rollovers graded as **membership and push status only**; **no Plague Race or Endless window dates are graded** (the warehouse's 5-day series and an S7 backend-schedule lead disagree; the Endless spec is not needed) | the brief | each graded window computed from its rule |
| "Starts" | a beat starts with the first window that opens after its server windows are live on prod (the beta build being live is common to all beats) | the brief's deploy rule + Owen's `#470` comment + Douglas's release plan event (Wed Oct 8) | Collect & Win → Fri Oct 10 00:00 UTC (Thu Oct 9 5:00 PM PDT); the Wed–Thu window opened before the deploy. No base record dates a Collect & Win prod deploy (S1b §2), and the hidden `#zm-collect-win` shows dev-server testing only — the seed conflicts with nothing |
| Held for tech | hold a beat only if players **cannot enter, score or claim** on prod **even after a restart**; wrong counters, restart-needing resets, cosmetic, VFX and analytics gaps do not hold it | Leonard `C090N54TG79/1758517286.431379` ("Beta must be tech stable, no excuses") + the brief | all 12 open non-Boss-Arena live-ops issues get exactly one answer (learnings §21): ZOM-344, 432, 465, 471, 565 cosmetic/VFX → run; ZOM-504 (objects stay visible) and ZOM-517 (monster loses enrage) → run; ZOM-534 (quest points reset after a restart) and ZOM-556 (skipped daily gift keeps the streak; claim works) → known issues; ZOM-552, 566 analytics → run; ZOM-429 → **held**, by Vincent's Sep 30 prod check (C8) |
| One-offs | may overlap recurring slots; displacing one needs Product's (Robert's) approval; the approver's latest dated call stands | the brief + seeded approval and withdrawal | census of Robert's 756 Julia-visible messages Sep 17–30 (DM 192, `#zombie-design` 184, `#zombie-bugs` 181, `#zombie-match3d` 104, `#zombie-art` 91) for any other approval |
| Still to do and locks | every setup a beat needs lands before its config lock, read in UTC; an open issue is still to do unless a dated note shows it fixed on the Sep 30 build | the brief + Brian's mail; issue notes | November Season Pass config: lock Fri Oct 31 00:00 UTC (Thu Oct 30 5:00 PM PDT); Brian's "Fri Oct 31, 10:00 Istanbul time" = 07:00 UTC (Turkey is UTC+3 all year) → moved before the lock, owner Brian |
| Pushes | a push goes out only if its "PNs Beta" row is Ready **and** its English copy names the game only as "Zombie Match 3D" and events only by their ZM3D names; a failing row is **held** for the copy owner (Julia may propose wording; the row stays held); a beat's push follows its beat | the brief; the August rename in base Slack | all 14 rows read: 1-day lapse and D0-1 FTUE held; 7-day lapse and lives recharged sendable; weekly leaderboard reset follows the held leagues beat (not graded separately); rollover, Collect & Win and Season Pass rows Not Ready |
| Destinations | calendar in the Julia-owned sheet; linked from ZOM-78; recommendation as a reply in the ask's DM | prompt (named) + the ask | ZOM-78 is the only calendar ticket (title search) |

### 5.2 Two-reading tests to run at S8

1. Merged vs live on prod (Collect & Win) → the deploy rule, Owen's comment and the release plan event fix one instant
   (Fri Oct 10 00:00 UTC).
2. Robert's thread approval vs his later DM → the later call by the same Product owner on the same item stands.
3. Ready vs copy → held, with the change and the owner named; "send with corrected copy" is a different action and is not
   accepted.
4. The obvious event list vs the brief's scope → the brief governs; the two rollovers are in. Any row layout accepted.
5. Restart-clearing faults and wrong counters (ZOM-534, ZOM-556) → known issues under the enter/score/claim sentence.
6. Douglas's restart note and the Sep 22 revert-and-recovery vs Vincent's later prod check (ZOM-429) → the later prod check decides;
   leagues held.
7. Lock day vs lock instant (Season Pass November config) → "locked 24 h before 00:00 UTC Nov 1" is one instant; a delivery
   at 07:00 UTC Oct 31 is late; PT or UTC renderings of the moved deadline accepted if they are at or before the lock.
8. Boss Arena → off this calendar by the brief's dated decision; omitting it or listing it as off both pass.
9. Halloween app icon (Martin's post also mentions an icon) → not a live-ops beat; never graded.
10. Sheet layout, wording, date format, PT/UTC rendering of the same instant → any equivalent accepted (learnings §8).

### 5.3 Boundaries the rubric accepts in full

Row layout (one row per beat or per window), labels, PT or UTC (or both) for the same instant, the order of the
recommendation, owner names only where a record names one by name (tokens such as `[PERSON_NAME_0092]` are never graded).

### 5.4 Writes the rubric will not loosen

The reply goes in Frederick's DM (not a channel post); the calendar link goes on ZOM-78 (not a new ticket); pushes that
fail the copy rule are held, not rewritten in place — learnings §5.

### 5.5 Coherence plan for every artifact on the required path (rule 3; `1_Prompt_Eval.md` §3.2 "fails on the presence")

The design requires and cites **no** artifact that carries a known contradiction — the playbook's `excluded` resolution
("the hazard's records are neither modified by the SQL nor cited by the design", 01 S1) — and puts every rule it needs
into records whose owners would write them. Where a required artifact holds an odd state, a dated owner statement
explains it (never a silent edit).

| Status | Artifact | Known contradictions | Treatment |
|---|---|---|---|
| excluded | `page_liveops_calendar` | SC-62 import cadence; Domino rows (SC-31, SC-47); "Weekly Leaderboards — DD / ZM3D — Live" vs DD-only warehouse rows; "Friday all-hands" vs no 2025 H2 event | never required or cited; the brief restates only card-free working rules |
| excluded | `page_season_pass_spec` | SC-38 (production week; "events are tagged" vs ZOM-552) | season start and lock come from the brief |
| excluded | `page_zm3d_gdd`, `page_live_ops_engine`, `page_product_okrs` | SC-8, SC-58, SC-31, SC-28 | not needed |
| excluded | Snowflake `LIVE_EVENT_PERFORMANCE`; Trello BETA list and cards 54/56/58/67 | page/warehouse pairs; SC-13, SC-14 | no Plague Race dates graded; Trello weight only on the Axe Arena card in "Oct 21" |
| excluded | `match3d-backend` and client code (S7 leads, unverified) | a per-event prod cron table incl. Collect & Win groups; Plague Race "every day" vs the warehouse's 5-day series; a 60/120/250 Plague Race stage table vs Leonard's Sep 10 "250 instead of 500"; backend commits stop 2025-08-13 while the working copy holds Collect & Win modules | no graded or seeded fact rests on code; C5 (reward cut already done) dropped; S1 checks what `github_get_file_contents` returns before the final design |
| required | push sheet `f_a325dd4af80afc5994d5dc` | "PNs" (Domino-era) vs "PNs Beta"; "Win & Collect event start" for ZM3D; **"PN BETA Translated" holds Domino Adventures and River Rush copy (rows 3–8, 11) that does not match "PNs Beta"**; the "PNs Beta" Plague Race row carries River Rush's 🌊🚣 | only "PNs Beta" English copy is used; the brief says beta pushes are English-only and the translated tab is the old Domino set awaiting ZM3D localization (a dated owner statement explaining the state); display names and emoji never graded; residual risk §10.4 |
| required | `#zombie-bugs` Sep 22 report `C08R27X0EAH/1758546048.524829` (standalone, no replies) and Oliver's thread `C08R27X0EAH/1758546119.789009` | report: "Killing the app doesn't help"; thread: "after a moment, I am now in the weekly leaderboard", Oliver's revert, then "yep, it's working fine right now" (`…/1758550789.777509`) | not a contradiction: a fault on a test build, fixed by a revert. C8's Sep 30 prod check must give the fault a cause that fits this history (e.g. the reverted change re-landed in the 0.3.49 submission build) — a seed-realism item for S1 (§10.8) |
| required | Robert DM `D05GU6L0XFH` | base messages Sep 30 17:17Z and 20:46Z, then Oct 1 03:32Z (auto-battler topic) | the withdrawal sits between 20:46Z and 00:00Z on its own topic; the Oct 1 message must still read naturally after it |
| required | `#zombie-match3d` | Frederick, Sep 30: "We are only running the retention campaigns" | the deck's buy weeks are the scaled beta-cohort buy after store approval, worded so they do not deny the running campaigns |
| required | `match3d` #468/#470/#472 and the other live-ops PRs | SC-18 (#477, off path); CodeRabbit summaries; SC-56 commit-title case | Owen's comment after #470's merge with its INT-01 mirror; no `#builds` title matching |
| required | ZOM live-ops issues, ZOM-78, ZOM-429 | SC-16 tickets not in the spine (checked); SC-22 `time_in_status` | never used; notes only on open issues; companions bump `updated_at` |
| required | Frederick DM, `#zombie-design`, `#company-internal`, `#zombie-art`, `#zombie-ops` | SC-7 (membership), SC-70 (Slack time zones) | membership and profile time zones never used; every seeded time carries its own zone; seeded DM text only in English DMs |
| hidden base agrees | `#zm-collect-win` `C09EVVCFHKR` (not Julia-visible) | Brian and Owen test Collect & Win "on the dev server" through Sep 26 | consistent with "server windows on dev" |

**Residual risk (open, not hidden):** the excluded pages and code are still in the universe on the same topic, and the
translated tab stays mixed; a `/prompt` reviewer may treat them as task-touched because an agent will likely open them.
Confluence, Snowflake and git are not injectable. If you judge that risk unacceptable, storyline A should be dropped —
every live-ops storyline at this clock sits next to these records.

Coherence hazards touched (KB `coherence_hazards.json`, S5b §1): T04, S01, R07, L03, I15, I01/I18, Q01/Q04, L08–L10;
`/create-scenario` S1 cites each with its disposition; all six categories are covered.

### 5.6 Chronology and the data horizon

Every seed lands at or before 2025-10-01T00:00Z and after the base events it names: Robert's approval (Sep 18 16:40Z) after
Martin's post (Sep 17 15:10Z); Douglas's ZOM-429 note (Sep 23) after the Sep 22 thread and ZOM-429's `updated_at` (Sep 22
14:51Z); the brief (Sep 30 15:00Z) and the ask after it; Brian's mail (Sep 30 17:30Z); Vincent's prod check (Sep 30
18:30Z) after the iOS 0.3.49 release (Sep 29 21:55Z); the release plan event created Sep 30 21:00Z; Owen's comment (Sep 30
21:30Z) after #470's merge (15:51Z) and inside the INT-01 window; Robert's withdrawal (Sep 30 22:10Z) after Frederick's
playable pause (Sep 29) and the last base DM message (20:46Z). Base records after the seed bound that the task could touch:
Robert's DM Oct 1 03:32Z (continuity above), `#builds` Android #2029 (05:51Z) and `match3d` `pushed_at` 05:44Z — no beat
depends on them. Plan dates (buy weeks, windows, the Oct 8 release, the Nov 1 season and its lock) are future plan fields.

---

## 6 · Hardness plan (rule 4) — storyline A

### 6.1 Loss channels (independent, each its own fact and surface, each flipping ≤ 2 rows; weight 5 by kind of work)

| Ch | v2 trap type (guide Part 3) | Convincing wrong source (who · when · authority) | Record that beats it | Findability | Survives complete retrieval because | Rows it flips |
|---|---|---|---|---|---|---|
| C1 | 1 · proving "done" across services | #468/#470/#472 merged before the Sep 30 cut; Julia's own Sep 22 notes "feature completed Win and Collect" (`C05KNDCHAAG/1758558302.777379`); Leonard's Sep 12 beta pipeline | Owen Baker's conversation comment on his merged `#470` (Sep 30): the server windows are on the dev stack and go to prod with Douglas's next backend release; that release is a plan event in Julia's calendar (Wed Oct 8); under the brief's deploy rule the first prod window is Fri Oct 10 00:00 UTC | tier 3: returned only by the issue-comments call on a PR (search counts conversation comments but returns none, S7 §3.3), on one of three Collect & Win PRs, with the date in another service | "merged" and "feature completed" are true; only the deploy meaning decides | Collect & Win first window (5) · reply names it as late (3) |
| C2 | 2 · a correction somewhere else | Robert's reply in Martin's `#zombie-art` Halloween thread approving a one-off that displaces Plague Race in the Halloween week (the Product owner, a documented approval) | Robert's later message in his DM with Julia withdrawing it (no event art before the pivot call) — same person, same item, another container | tier 2: a DM with 192 Robert messages Sep 17–30 | the approval satisfies the brief's displacement rule until the DM | reply calls the one-off off with its reason (5) · Plague Race in the Oct 27 – Nov 2 week (5) |
| C4 | 7 · items outside the obvious filter | the event list everyone uses — Leonard's beta pipeline and the live-ops icons | the brief's scope (every window, reset or start push) brings in the quests rollover and the login-calendar rollover, each with its push row (both Not Ready) | tier 2: one hop from the anchor | the agent must apply the scope to features nobody calls events | one row per member (5 + 5) · beat count (3) |
| C6 | 5 · a rule hidden in the data | the push sheet's own Ready status on the 1-day lapse and D0-1 FTUE rows | the brief's copy rule (the game only as "Zombie Match 3D"), backed by the August rename: both rows say "Puzzles vs Zombies" | tier 1 to find, tier 2 to apply; weaker (design rate 0.30) | it costs a run only if the run trusts the owner's column | 1-day lapse held (5) · FTUE held (3) |
| C8 | 2 · a correction somewhere else (second instance: other people, item and containers) | Douglas's owner note on ZOM-429 (Sep 23; he is the assignee): client-side, a restart works; the base Sep 22 thread `C08R27X0EAH/1758546119.789009` ends with the change reverted and "yep, it's working fine right now" | Vincent's Sep 30 prod check of 0.3.49, a root post in `#zombie-match3d`: the weekly session does not start even after killing the app → leagues held under the hold rule | tier 2: a different Slack channel from the Sep 22 report and thread, and a different service from the Linear note; a leaderboard search finds it (design rate 0.35) | the note and the revert-and-recovery are real; only the later prod check under the restart clause decides | leagues beat held with its reason (5) |
| C9 | 4 · dates, windows and dependencies | Brian's handoff mail: the November Season Pass config "Fri Oct 31, 10:00 Istanbul time" — on the lock day | the brief: config locks 24 h before the season opens at Nov 1 00:00 UTC, i.e. Fri Oct 31 00:00 UTC (Thu Oct 30 5:00 PM PDT); 10:00 TRT = 07:00 UTC, seven hours late → the deadline moves before the lock, owner Brian | tier 2–3: Gmail is a rarely opened service (`hardness_gate.py` `RARELY_OPENED`) and the instant must be computed | a careful run reads both records in full; only the conversion decides | Season Pass config due before the lock (5) · reply names the conflict (3) |

Dropped in rev 3: **C5** (Plague Race reward cut already live) — its seed would sit next to Leonard's Sep 10 thread and an
unverified backend stage table that may already read 60/120/250 since June. **C7** (ZOM-78 reuse) stays an ordinary
weight-3 row (DECISION_FLIP disposition, §6.3).

Load-bearing pair for the guide's "1–2 traps that carry the difficulty": **C1 (trap 1) and C2 (trap 2)**, each naming its
wrong source and its winning record; C8 and C9 are further cross-source decisions (trap 2 on another item, trap 4). The
largest unit of discovery decides C2's 10 of 67 weight points (15 %); no channel is near half.

### 6.2 What will not be relied on (guide Part 4; learnings §45–46, §52, §54; Claire R3 §2.9, §3)

Volume, routine writes and clean totals (no weight-5 aggregate; the spine is horizon, not difficulty); visible caveats
(the Confluence "not yet live" left with the page); same-thread or same-channel corrections (C2's withdrawal left the
approval thread, C8's prod check left the Sep 22 report, Oliver's thread and `#zombie-bugs`); rules in the prompt; a hub that lists answers
(the brief states rules and never names a held or late beat); keyword-findable seeds (notes say what happened in plain words,
not "dev only" / "withdrawn"); Trello flags (SC-14); a GCal lock event (it would show C9's instant); anything an obvious
subagent brief sweeps by default (C1's comment is a conversation comment, not a review).

### 6.3 Part 7 self-checks, run by `tools/hardness_v2_check.py`

Run on the rev 3 sketch (`research/00_sketch_manifest_rev3.json`, `research/00_sketch_surface_rev3.json`; planned ids,
containers declared). History: rev 0 flagged `DECISION_FLIP R_REUSE_TICKET` (weight-3 only) and the reuse rule left the
mechanism portfolio (never raise a weight); revs d–e moved C1 to `#470`, C8 out of `#zombie-bugs`, and removed every
Confluence, Snowflake and backend record from the traps; rev 3 drops C5 and adds C9. Verbatim
(`research/hardness_v2_check_rev3.txt`):

```text
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      4 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 6 requirements: {'R2': ['R_DONE_DEPLOY'], 'R4': ['R_WITHDRAWN'], 'R1': ['R_SCOPE_BEATS'], 'R6': ['R_COPY_CURRENT'], 'R3': ['R_TECH_HOLD'], 'R8': ['R_LOCK_BOUNDARY']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   6 of 6 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     0 weight-5 total(s); 0 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  SKIP       RULE_IN_PROMPT  no prompt (04_Prompt.txt) yet  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

Positive control (the check is live): moving C2's withdrawal into Martin's approval thread
(`research/00_sketch_manifest_rev3_control.json`) gives, verbatim (`research/hardness_v2_check_rev3_control.txt`):

```text
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  FLAG       SAME_PLACE      4 trap(s) with two or more version records; 1 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 6 requirements: {'R2': ['R_DONE_DEPLOY'], 'R4': ['R_WITHDRAWN'], 'R1': ['R_SCOPE_BEATS'], 'R6': ['R_COPY_CURRENT'], 'R3': ['R_TECH_HOLD'], 'R8': ['R_LOCK_BOUNDARY']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   6 of 6 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     0 weight-5 total(s); 0 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  SKIP       RULE_IN_PROMPT  no prompt (04_Prompt.txt) yet  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']

Flags (each needs a written disposition; redesign the difficulty, never weaken a fairness link or raise a weight):
  SAME_PLACE T_C2 (same_container): the correction and a superseded version share slack:C08R8CHB0QL/1758121809.236839
```

Guide Part 7 in words: **done check** — C1: #468's merge and Julia's Sep 22 notes say done; `#470`'s conversation comment
and the release plan event show the server windows reach prod only on Oct 8. **Same-place** — C2: DM vs the `#zombie-art`
thread; C8: a `#zombie-match3d` root vs the Linear note and the `#zombie-bugs` report and thread; C9: Gmail vs the brief. **Filter** —
the obvious event list misses the two rollovers. **Input** — no total is graded; trap 8 is not used. **Decision flip** —
each mechanism flips at least one weight-5 multi-source row.

### 6.4 Planned surface and policy scores (UNCALIBRATED; rule 5)

Planned surface: 19 slots, total weight 67, 8 weight-5 slots, 4 ordinary samples (Season Pass November season opens Nov 1
00:00 UTC, lives-recharged push sent, Axe Arena off with its post-beta slot, 7-day lapse push sent) plus a volume slot and two
delivery slots (`research/00_sketch_geometry_rev3.json`). Scored with `research/scripts/geometry_mc.py`, which grades
simulated six-run baselines with the bundle's own gate math (`difficulty_stats._gates`, **medium**, long-horizon). It
measures the four scoring gates **conditional on six completed runs inside the horizon tier** (error rate and horizon are
not modelled; §7, §10). Verbatim (`research/geometry_mc_rev3.txt`, 20,000 draws per scale):

```text
PLANNED SURFACE (pre-scenario sketch, UNCALIBRATED; mode medium, cap < 85%)
  slots 19  total weight 67  weight-5 slots 8
  weight by flip: {'C1': '8/67=12%', 'C2': '10/67=15%', 'C4a': '5/67=7%', 'C4b': '5/67=7%', 'C6': '8/67=12%', 'C8': '5/67=7%', 'C9': '8/67=12%', 'any:C4a,C4b': '3/67=4%', 'ordinary': '15/67=22%'}

WHOLE POLICIES (deterministic, no slips)
   22.4%  P0 lazy: Frederick's ask + the events everyone lists + push sheet Ready column as written
   22.4%  P1 + client PRs (list/search only), Trello and Linear list view (no PR comments, no issue comments, no DMs)
   61.2%  P2 + every ZM3D channel and thread incl. #zombie-art, #zombie-match3d and #zombie-ops (no DMs, no mail, no PR comments, no issue comments)
   88.1%  P3 + DMs, mail and issue comments (no PR conversation comments)
   88.1%  P4 everything retrieved, Ready column trusted
   80.6%  P5 everything retrieved, the obvious event list taken as the scope
   88.1%  P7 everything retrieved, the lock read as the end of Oct 31
  100.0%  P6 perfect

SINGLE MISSES (everything else right)
   88.1%  miss C1
   85.1%  miss C2
   80.6%  miss C4 (all 2 members)
   88.1%    miss member C4a only
   88.1%    miss member C4b only
   88.1%  miss C6
   92.5%  miss C8
   88.1%  miss C9

SIX-RUN BASELINES (20000 draws per scale; gate math = difficulty_stats._gates, medium, long-horizon)
  scale = multiplier on every design miss rate (1.0 = design rates; <1 = a stronger Opus)
  scale 1.00: E[avg] 67.1% (p10-p90 56.5%-77.4%)  E[SD] 0.171  P(avg<85%) 0.99  P(<5 full) 1.00  P(SD band) 0.82  P(patterns) 1.00  P(all four) 0.81  E[full passes] 0.38
           P(row fails all six) >= 1%: {'S_C2_reply_halloween_off_with_reason': 0.015, 'S_C2_plague_runs_halloween_week': 0.015}
  scale 0.75: E[avg] 74.1% (p10-p90 64.2%-83.8%)  E[SD] 0.161  P(avg<85%) 0.93  P(<5 full) 1.00  P(SD band) 0.77  P(patterns) 0.99  P(all four) 0.74  E[full passes] 0.70
  scale 0.60: E[avg] 78.3% (p10-p90 68.9%-87.3%)  E[SD] 0.151  P(avg<85%) 0.82  P(<5 full) 1.00  P(SD band) 0.70  P(patterns) 0.99  P(all four) 0.63  E[full passes] 0.98
  scale 0.50: E[avg] 81.2% (p10-p90 72.4%-89.6%)  E[SD] 0.141  P(avg<85%) 0.69  P(<5 full) 1.00  P(SD band) 0.63  P(patterns) 0.98  P(all four) 0.53  E[full passes] 1.23
  scale 0.35: E[avg] 85.8% (p10-p90 77.9%-93.0%)  E[SD] 0.123  P(avg<85%) 0.41  P(<5 full) 0.99  P(SD band) 0.48  P(patterns) 0.96  P(all four) 0.31  E[full passes] 1.71
```

Design miss rates (scale 1.0): C1 0.45, C2 0.50, C4 0.30 per member (ρ 0.5), C6 0.30, C8 0.35, C9 0.45; slips 0.03–0.06;
a per-run thoroughness latent (loading 0.5) correlates the channels. These are assumptions: the Opus 5.5 ledger
(`hardness_ledger.py priors --model claude-opus-5-5`) holds Beta(1,2) one-trial priors for A7 and A14–A17, Beta(1.86,2) for
A1 and nothing for A3, A8, A11, A19, A24 or A25; Claire's R3 (`task_inputsH/Working_Files/research/R3_opus_failure_modes.md`
§2) verifies the done-across, correction-elsewhere, outside-filter and record-never-opened modes on completed tasks.

**Sensitivity — sweep- and judgment-settled channels solved** (C4 and C6 missed 10 % of the time, C8 15 %; C1, C2, C9 as
designed; `research/geometry_mc_rev3_sens.txt`):

```text
SIX-RUN BASELINES (20000 draws per scale; gate math = difficulty_stats._gates, medium, long-horizon)
  scale = multiplier on every design miss rate (1.0 = design rates; <1 = a stronger Opus)
  scale 1.00: E[avg] 74.8% (p10-p90 65.7%-83.6%)  E[SD] 0.147  P(avg<85%) 0.93  P(<5 full) 1.00  P(SD band) 0.69  P(patterns) 0.98  P(all four) 0.66  E[full passes] 0.65
           P(row fails all six) >= 1%: {'S_C2_reply_halloween_off_with_reason': 0.015, 'S_C2_plague_runs_halloween_week': 0.015}
  scale 0.75: E[avg] 80.1% (p10-p90 71.6%-88.3%)  E[SD] 0.138  P(avg<85%) 0.76  P(<5 full) 1.00  P(SD band) 0.61  P(patterns) 0.97  P(all four) 0.53  E[full passes] 1.06
  scale 0.60: E[avg] 83.4% (p10-p90 75.4%-91.0%)  E[SD] 0.128  P(avg<85%) 0.58  P(<5 full) 1.00  P(SD band) 0.52  P(patterns) 0.95  P(all four) 0.40  E[full passes] 1.38
```

**Against the goal's bar (E[avg] ≤ 77 %, P(all gates) ≥ 0.5), conditional on valid runs inside the tier:** design rates
67.1 % / 0.81; the bar holds to a miss-rate scale of about 0.7 (74.1 % / 0.74 at 0.75; 78.3 % / 0.63 at 0.6). With the
weak channels solved: 74.8 % / 0.66 at design rates, 80.1 % / 0.53 at 0.75. C9's contribution: the same surface without C9
(`geometry_mc_no_c5_sens.txt`) gives 77.5 % / 0.57 with the weak channels solved. **Binding risk: a strong Opus.** Every
single miss leaves a run at 80.6–92.5 %, so the 85 % cap needs about two misses per run; the margin rests on C1, C2 and C9
staying off the first-read path. Further levers if `/create-scenario`'s forecast on the real surface comes back above 77 %: a
trap 9 member inside the issue spine, or fewer ordinary samples — never raised weights, never padding.

### 6.5 Spread (rule 5)

Each channel's deciding record sits on a different surface — a PR conversation comment plus a calendar event (C1), a DM
(C2), a brief one hop from the anchor (C4), push-sheet copy against a rule (C6), a channel root in another channel (C8), a
mail and a UTC conversion (C9) — with findability tiers 1–3, so runs fail different subsets: P(patterns) ≈ 0.98–1.0 and
P(SD band) 0.63–0.82 at scales 0.5–1.0. The highest predicted all-six miss is C2's pair at 1.5 % (scale 1.0) — VALID
workload if it happens (every value reachable), not a predicted all-fail.

---

## 7 · Volume plan (honest, never padded; recounted in rev 3 after red-team finding R3-1)

Only reads with a distinct decision dependency count.

| Phase | Calls, shortest sufficient path | Why each is necessary |
|---|---|---|
| Anchors and rules: the ask (1), the brief (1), the UA deck (1), Brian's mail (search + read, 2), push sheet (metadata + "PNs Beta", 2), GCal release event (1) | 8 | each carries a different rule, date or scope |
| Enumeration: Linear live-ops issues (3 pages) + ZOM-78 search (1); GitHub live-ops PR search (3); Slack windows or searches in `#zombie-design`, `#company-internal`, `#zombie-art`, `#zombie-ops`, `#zombie-bugs`, `#zombie-match3d` (6); Trello board (1) | 14 | the scope rule needs every beat, open issue and merged live-ops PR |
| Per-beat records: Halloween thread (1), Robert DM history (2), Axe Arena card comments (1), Sep 22 leaderboard thread (1) | 5 | each beat's call depends on its own record |
| Writes + read-backs: sheet values (2) + read-back (1), DM reply (1), ZOM-78 comment (1) | 5 | each write is requested |
| **Non-spine subtotal** | **32** | |
| Spine, issues: `linear_list_comments` on the 12 open non-Boss-Arena live-ops issues (`raw/spine_open_issues_nonba.json`) | 12 | the hold rule and the still-to-do rule read each open issue's prod state; base has 0 Linear comments, so these notes are seeded |
| Spine, PRs: reviews + inline review comments + conversation comments on the 22 merged non-Boss-Arena live-ops PRs (`raw/spine_merged_liveops_prs_nonba.json`) | 66 | the readiness rule ("no open review blocker") can only be checked per PR, and the three surfaces come from three separate calls (S7 §3.3–3.4); C1's deciding comment sits on one of them |
| **Total** | **110** (78 per-record) | ≥ 500 is not reachable without padding |

Corrections in rev 3: Boss Arena is off the calendar, so its issues and PRs leave the spine; 5 more of the 41 keyword PRs are
not live-ops (#354, #363, #365, #377, #445), which leaves 24 non-Boss-Arena live-ops PRs, 22 of them merged (#477 and
backend#34 are open); only **2 of the 22** carry any human review content in base (#456 "LGTM"; #470 two author replies). So
the PR spine is necessary only if the brief's readiness rule is natural **and** 15–40 % of the PRs carry a deciding human
note (playbook 01 S2) — about 3–9 seeded notes, each with its INT-01 mirror. Without the PR spine the path is 44; without
both spines, 32. Possible honest upside, not counted: per-thread reads of the September live-ops report threads (28 roots
with replies Julia can see, `raw/liveops_threads_sep.json`; channel reads do not return replies, Ask_Carriers §3 [V]) if the
brief's hold rule names Slack bug reports. Observed counted calls on comparable completed tasks run far above the shortest
path (163–1,209, Claire R3 §1), but the design margin (GEN_EXECUTION §3: Long Horizon ≥ 110 necessary calls) is met with
**zero** slack.

---

## 8 · Cohort spine (hard gate 3: ≥ 40 records × ≥ 3 per-record surfaces over ≥ 2 services)

The volume exception lowers only the call-budget and per-record floors; the cohort floor stays (`hardness_gate.py`
`cohort_size` and `evidence_surfaces`: ≥ 40 records, ≥ 3 surfaces over ≥ 2 services, each with a true `why_no_bulk` and a
`short_circuit` analysis). Populations checked (S2, S6): Zombie Lane nodes (live sheet not visible), Season Pass tiers (NO),
quests (no list), event reward lines (~25), push rows (14, one read), Trello cards (sparse, SC-13/14), store reviews
(templated text), levels (level design, not GTM), per-beat art records (20 art-titled tickets; 43 only by folding in shared
VFX work, S6 §6). The two populations on the plan's decision path:

| Population (predicate) | Records | Surfaces with an honest `why_no_bulk` | Service |
|---|---|---|---|
| ZOM issues whose title names a live-ops feature, open at the clock, outside Boss Arena | **12** (ZOM-344, 429, 432, 465, 471, 504, 517, 534, 552, 556, 565, 566) | issue comments (all seeded; base has 0) — state and description come from the list call | Linear |
| `match3d` PRs whose title or branch names a live-ops feature, created Aug 1 – Sep 30, merged, outside Boss Arena and not misfiled | **22** | reviews, inline review comments, conversation comments — three separate calls | GitHub |

**Verdict: gate 3 cannot be certified honestly** for storyline A — 34 records of two types, neither ≥ 40, and no single
population with three surfaces over two services — and, on S2's evidence, not for B or C either. It is a conflict between
the local extreme profile and this persona and competency; only you can resolve it (D5). Padding a population or a surface
(filler threads, synthetic per-record docs) is a failing error and is not an option.

---

## 9 · Writes and ownership (rule 6)

| Write | Trigger the persona owns | Write access |
|---|---|---|
| Beta calendar (Google Sheet) | Frederick's ask to Julia | Julia-owned: the seeded calendar sheet in her seeded "ZM Live Ops" folder, `owner_email` Julia in both Drive and Sheets rows (learnings §31), written with `gsheets_values_update`; if created at run time instead, `gsheets_create_spreadsheet(title, initialSheetTitle, driveFileId)` makes one tab and more tabs need `gsheets_batch_update addSheet` (S4 §2). Never the Resource-owned push sheet |
| Recommendation reply to Frederick | the ask itself | Julia is a member of `D05SD5QLG94` (YES) |
| Calendar link on ZOM-78 (comment) | the ask names the calendar ticket | Linear unscoped; ZOM team writes confirmed in the pre-check |
| Optional: one setup ticket (e.g. the push copy fix) | the ask's "what is still to do, by whom" | Linear unscoped; reuse an existing ticket where one covers it |

---

## 10 · Risks and open items

1. **Gate 3 (cohort shape) cannot be certified honestly** (§8). It needs your decision (D5) and, under D5-i, a
   requester-confirmed cohort exception that `hardness_gate.py` does not implement today.
2. **Horizon margin is zero:** ≈ 110 necessary calls, 78 per-record (§7). 66 of them are PR reads that are necessary only if
   the readiness rule is natural and 3–9 PRs carry a seeded deciding human note; any census shrinkage puts the design under
   the 110 margin, and dropping the PR spine puts it under the 100 floor (44).
3. **Competency drift:** the PR spine is 60 % of necessary calls; every graded row must stay a calendar, campaign or
   communication outcome (`/prompt` §1.5 is a local hard FAIL).
4. **Coherence residuals (§5.5):** excluded pages, warehouse rows and code on the same topic; the mixed translated tab;
   Robert's DM continuity; the deck against the running retention campaigns. Not fixable by injection.
5. **The brief is a hub of rules:** scope, readiness, copy, one-off and lock rules (never answers). C4 and C6 sit one hop
   from the anchor and are rated weak; the margin rests on C1, C2 and C9.
6. **A strong Opus** (scale ≤ 0.7) pushes E[avg] past 77 %; with the weak channels solved, P(all gates) is 0.53 at scale 0.75.
7. **Ten injected services:** Drive and Sheets carry only the destination, Slides the span, Trello a sample; each must pass
   the S9 literal-value sweep or be replaced by a natural carrier, never padding.
8. **Seeding load:** ~12 Linear notes, 3–9 human notes on `match3d` PRs plus Owen's (each with its INT-01 mirror and timeline
   event), thread counters, GCal copies and invitation mail. Brian's mail is English with Frederick in copy, although
   Julia's DM with Brian is Turkish.
9. **Language and theme:** seeded DM text only in English DMs (Frederick, Robert); ZM3D content is unavoidable (D3).
10. **Calibration:** ledger priors for A3, A8, A11, A19, A24, A25 are empty; the geometry is conditional on valid runs.
11. **Process (disclosed):** S7 read backend code outside `tools/hg.py`; its leads changed the design only by removal and
    are re-verified at S1 through the agent's tools.

---

## 11 · Decisions needed from you

| # | Decision | Recommendation |
|---|---|---|
| D1 | Storyline | **A — ZM3D beta-weeks live-ops and player-push calendar** (§4.4), **conditional on D5-i**. Best fit and strongest traps; its structural gaps (§8, §7, §10.1–10.4) are stated, not solved |
| D5 | Cohort spine (hard gate 3) — **blocking for `/create-scenario`** | **D5-i:** approve a recorded, requester-confirmed deviation from the extreme cohort *shape*: a two-type spine on the plan's decision path — the 12 open live-ops issues (one honest surface: comments) and the 22 merged live-ops PRs (three: reviews, inline review comments, conversation comments) — 34 records, ≈ 78 necessary per-record calls over Linear and GitHub. `hardness_gate.py` supports only `volume_exception`, so the tool owner must add a cohort exception first; I may not edit `Task_Authoring/tools/`. **D5-ii:** pick another storyline — none with a natural ≥ 40 × 3 population was found for Julia × Marketing and GTM at this clock (S2, S6). **D5-iii (rejected):** add filler records or surfaces — padding, a failing error |
| D2 | Volume exception (GEN_EXECUTION §3a; ≥ 500 necessary calls not reachable without padding) | **Yes, under D5-i:** `volume_exception {call_budget_floor: 105, per_record_floor: 75}` (§7: 32 non-spine + 78 spine ≈ 110; re-derived at S2/S7 from the census), with your confirmation recorded as `requester_confirmation`; every other extreme target stays (≥ 10 services, ≥ 120 rows, ≥ 12 traps, …). The floors leave 5 and 3 calls of slack; if the census falls below them, D5-ii applies |
| D3 | Theme screen (playbook 01 S0: no zombie/outbreak theme) | **Waive for this task, recorded:** every Julia storyline at this clock is ZM3D; Claire's R3 §5 found 0 refusals or fallbacks in 13 Opus 5.5 runs on ZM3D data. Mitigation: seeded text says "ZM3D" and event names, never "infection" or "outbreak"; every pre-check and baseline is checked for model fallback |
| D4 | Review waiver | No `REDTEAM_*` variables are set in this shell (`env | grep -c '^REDTEAM'` → 0), so `redteam_review.py --dual` cannot run. Either set `REDTEAM_*` (preferred), or approve a recorded `RED TEAM FALLBACK:` using this session's independent GPT `redteam` and `oracle` subagents on the design (kept in every Unresolved line until covered, learnings §44). This analysis itself was reviewed that way (§13) |

---

## 12 · The goal's seven rules, and where this analysis answers each

| Rule | Answered in | Status at this stage |
|---|---|---|
| 1 UGT (each material choice fixed by the prompt or a Julia-visible record, or bounded; every rule sentence applied to every item; census before completeness) | §5.1 (home + census per decision: span, time base, scope, Collect & Win start, the hold rule applied to all 12 open issues, push holds, the lock), §5.2 (ten two-reading tests), §5.3 | planned; S1/S8 run the censuses and the fork sweep |
| 2 Fit (Product & Design inside Marketing and GTM) | §3, §10.3 | argued; the PR spine's engineering slant is the named risk |
| 3 `/injection` (whole-universe check, seeds after base events, tool-visible) | §4.1 injection table, §5.5 (no contradicted artifact required or cited), §5.6, §10.8 | planned; `base_check`, `base_claims` and `hg.py lint` run at injection |
| 4 `/hardness` (≥ 3 independent channels, none over half, ≥ 2 cross-source decisions on distinct named v2 traps with wrong source and winning record; nothing passes by doing nothing; weight 5 by kind of work) | §6.1 (six channels on five services, largest 15 %; traps 1, 2, 4, 5, 7), §6.2, §6.3 (Part 7 checks + positive control) | rev 3 sketch CLEAN on all six applicable checks; control FLAGs |
| 5 Spread (graded findability; E[avg] ≤ 77 %, P(all gates) ≥ 0.5, UNCALIBRATED) | §6.4, §6.5 | 67.1 % / 0.81 at design rates, holds to scale ≈ 0.7; weak-channels-solved 74.8 % / 0.66; conditional on valid runs inside the tier |
| 6 Writes (authorized trigger, proven access, Julia owns Drive/Docs/Sheets targets) | §9, §4.1 rows 8–9 | planned; each write confirmed in the pre-check |
| 7 Alignment (every OE and rubric row traces to incorporated facts; no traps, rules or answers in the prompt) | §5.1 homes (the brief, base Slack, seeded notes), §6.2 | the prompt is not written at this stage; `RULE_IN_PROMPT` runs once it exists |

---

## 13 · Independent review of this analysis

Reviewer: GPT-6.1 Sol `redteam` subagent (independent of the Claude build lane), read-only, static. Round 1 verdict **FAIL**
(2 Blocker, 5 Major). Its factual spot-checks all held (calendar-page quotes, Season Pass cadence and lock, #468/#470/#472
merge times, ZOM-78/534/556 states, the Ready rows with the old title, Martin's post with zero replies, the Robert DM ending
20:46Z, the 20 Plague Race rows ending Sep 22–26). Findings and dispositions (rev 1):

| # | Severity | Finding (short) | Disposition (rev 1) |
|---|---|---|---|
| 1 | Blocker | "Never graded" does not exclude coherence defects on required reads (§3.2 fails on presence) | **Fixed:** §5.5 now lists each required artifact's contradictions with a resolution — off the path (Snowflake, Trello BETA list, live-ops engine page, OKRs, GDD) or a dated claim overturned by a later seeded record (SC-62 via Douglas's note; ZOM-552 note for the spec's "tagged" claim); residual risks named (§10.4) |
| 2 | Blocker | The cohort does not supply three qualifying surfaces; predicate and list missing; volume really ≈ 99 | **Confirmed and escalated:** strict predicate gives 47 (34 in September); the surface matrix (§8) shows only one honest no-bulk surface; honest volume ≈ 74 (§7), below the 100-call floor. D5 now asks you to choose: D5-b (41 live-ops PRs, genuine surfaces, ≈ 178 calls) or revisit the storyline |
| 3 | Major | Boss Arena "any status" is an action fork; push hold vs corrected copy unsettled; time base and endpoints unpinned | **Fixed:** Boss Arena off this calendar by the brief's dated decision; failing pushes are held with the change and owner named (rewrites not accepted); span and server-time instants pinned (§5.1, §5.2 #3/#7) |
| 4 | Major | C8's sketch used a Done issue with a later comment and invented container labels | **Fixed:** C8 re-homed to Vincent's re-test reply under an older `#zombie-bugs` leaderboard root, base issue ZOM-429 open (Backlog); truthful containers; checker re-run CLEAN (§6.3) |
| 5 | Major | C4/C6/C8 collapse on first reads; C1 advertised by "not yet live" | **Partly fixed:** C4's scope rule moved off the anchor to the brief; C6 and C8 kept but rated lower (0.30, 0.35), C1 0.50; geometry re-run (66.6 % / 0.82) plus a weak-channels-solved sensitivity (74.3 % / 0.67); a seventh channel named as the first margin lever (§6.4). Residual: a strong Opus still threatens the 77 % target |
| 6 | Major | Injected services count was nine | **Fixed:** §4.1 lists ten injected services, each with its own load-bearing fact, companions counted separately; Slides/Gmail uniqueness to be proven by the S9 literal-value sweep |
| 7 | Major | The forecast is not "all gates": runs forced complete at 300 calls | **Fixed (labelled):** §6.4 states the result is conditional on six completed runs inside the tier; horizon is handled in §7/§10.1 and error rate is outside the model |

Round 2 (delta review of rev 1) verdict **FAIL**: findings 4, 6, 7 RESOLVED; 1, 3, 5 PARTLY; 2 NOT RESOLVED; four new
findings. Rev 2 dispositions:

| # | Severity | Finding (short) | Disposition (rev 2) |
|---|---|---|---|
| R2-1 | Blocker | D5-b's surfaces are all GitHub plus a sweepable `#builds`; changed-file reads are not shown necessary; Boss Arena PRs sit in the population although Boss Arena is off the calendar | **Accepted:** §8 now states that no single ≥ 40 population has three honest no-bulk surfaces over two services; Boss Arena PRs removed (31 remain); file lists marked unnecessary; D5 reframed as a blocking decision with a tool-owner dependency |
| R2-2 | Major | §7 double-counted the spine (58 included 16 spine calls); only 14 open issues; D2 floors unsupported | **Fixed:** non-spine 38; open issues 14; totals restated (38 / 52 / ≈ 147 / ≈ 161); D2 floors re-derived (130 / 100) from the ≈ 147 path |
| R2-3 | Major | ZOM-556 classified as a known issue without restart evidence | **Fixed:** the hold rule is now "players cannot enter, score or claim on prod even after a restart"; wrong counters and restart-needing resets are known issues; applied to ZOM-534, ZOM-556 and ZOM-429 (§5.1) |
| R2-4 / 1 | Major | False statements remain inside a required artifact; off-path corroboration repairs nothing | **Fixed by exclusion:** no Confluence page or Snowflake table is required or cited; the brief restates only card-free sentences of Frederick's page; rename from base Slack and the brief; residual risk (pages still on topic) kept open in §5.5 and §10.4 |

Status handed to you: the analysis now claims feasibility only where it is shown; gate 3 (D5) is an open blocker that
needs your decision before `/create-scenario` can pass `hardness_gate.py`.

Round 3 (confirmation of rev 2) verdict **FAIL**: R2-1 RESOLVED as disclosure; R2-3 and original 3 RESOLVED; R2-2, R2-4
and originals 1 and 5 PARTLY; two new Major findings. Rev 3 dispositions, plus what the build session found while fixing them:

| # | Severity | Finding (short) | Disposition (rev 3) |
|---|---|---|---|
| R3-1 | Major | the ≈ 147 path counts skippable work (closed and Boss Arena issues); a counter-path gives 112 / 74, below D2's floors | **Fixed:** only reads with a decision dependency count — 12 open non-Boss-Arena issues and 22 merged non-Boss-Arena live-ops PRs × 3 surfaces; total ≈ 110 / 78 per-record; D2 floors re-derived (105 / 75); the zero margin and the seeded-note dependency are stated (§7, §10.2) |
| R3-2 | Major | rev-2 exclusions not propagated (sketch T_C1 and R_SCOPE_BEATS on Confluence; P0/P5 policies; §1, §4.1, §4.4 figures) | **Fixed:** rev 3 sketch files rewritten (requirements, traps, policies; no Confluence, Snowflake or backend record on any trap); Part 7 re-run CLEAN, control FLAG; §1, §3, §4.1, §4.4 and §5–§12 rewritten |
| self | — | 24, not 31, non-Boss-Arena live-ops PRs (5 misfiled), 22 merged; human review content on only 2 | spine and floors recounted; the 3–9 seeded deciding notes named as a precondition (§7) |
| self | — | Douglas has no base comment or review on any `match3d` PR | C1's comment is Owen Baker's on his own `#470`; the prod date moves to a GCal release plan event |
| self | — | base Sep 22 `#zombie-bugs` thread already shows a restart-proof leaderboard fault that recovers | C8 re-homed: wrong source = Douglas's ZOM-429 note + that thread; deciding = a `#zombie-match3d` root (Part 7 "same channel") |
| self | — | S7's code leads (read outside `hg.py`) may contradict the warehouse windows and Leonard's Sep 10 thread | C5 dropped; no Plague Race dates graded; C9 (trap 4, Gmail) added; the process deviation disclosed (Method, §10.11) |
| self | — | push sheet's translated tab holds Domino and River Rush copy | explained by the brief (English-only beta pushes; the old Domino set awaiting localization); residual risk (§5.5, §10.4) |

Round 4 (confirmation of rev 3) verdict **FAIL**, on C8 locators only: R3-1 and R3-2 RESOLVED; R2-2, R2-4 and originals 1
and 5 stay PARTLY (each is a disclosed residual — the PR spine's conditional necessity, the task-touched coherence risk, the
mixed translated tab, the stronger-Opus sensitivity); the reviewer confirmed the 12 open issues, the 22 merged PRs with human
content on only #456 and #470, Robert's Oct 1 03:32Z DM message, Frederick's retention-only reply, and that the §1 / §4.1 /
§4.4 / §7 / §10 / §11 figures agree (32 + 12 + 66 = 110, 78 per-record, D2 105 / 75). The open cohort gate and the zero
horizon margin were stated as not reasons for the verdict. Dispositions:

| # | Severity | Finding (short) | Disposition (rev 3, round-4 fixes) |
|---|---|---|---|
| R4-1 | Moderate | C8 cited `C08R27X0EAH/1758546048.524829` as the recovery thread; it is a standalone report (no replies). The recovery is in Oliver's thread `…/1758546119.789009`, which runs on to his revert and ends "yep, it's working fine right now" (`…/1758550789.777509`) | **Fixed:** §4.1, §5.2 #6, §5.5, §6.1, §6.2 and §6.3 cite the report and the thread separately and give the thread's full ending; the rev 3 manifests carry both as separate version records; §5.5 adds a seed-realism item — Vincent's Sep 30 prod check must give the fault a cause that fits the revert (e.g. the reverted change re-landed in the 0.3.49 build). Part 7 re-run CLEAN, control FLAG (§6.3 blocks match the files) |
| R4-2 | Minor | C8's resolver said "another channel and service from both"; the Sep 22 records and the deciding root are all Slack | **Fixed:** "a different Slack channel from the Sep 22 report and thread, and a different service from the Linear note" (§6.1 and both manifests); §4.1 now reads "different people, items and containers" |

Round 5 (narrow confirmation of the round-4 fixes) verdict **PASS**: R4-1 RESOLVED (§4.1 and §5.5 separate the standalone
report from Oliver's thread; §5.2 #6 and §6.1–§6.3 consistent; both manifests carry separate version records, the recovery
record pointing to `…/1758550789.777509`); R4-2 RESOLVED (the old phrase survives only as a quotation in this section). The
reviewer re-read `raw/slack_C08R27X0EAH_2025-09.json` (report with no replies; recovery, revert at `1758548804.266909`, final
confirmation; the root's `latest_reply` matches) and judged the §5.5 seed-realism item sound as a prospective check (the
re-landed change is an example, not a base fact). No new findings. Stored checker outputs match §6.3.

Review chain: GPT-6.1 Sol `redteam` (session `ses_e59972067ffebrksYE4iSwFzwF`), five rounds, static evidence review (checker
and simulation outputs not independently re-run by the reviewer); no same-family fallback was used. Residuals that stay
open by design: gate 3 (D5), the zero horizon margin (§7), the task-touched coherence risk (§5.5), the stronger-Opus
sensitivity (§6.4). `RED TEAM FALLBACK:` applies to the scenario stage (D4), not to this analysis.
