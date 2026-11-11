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
| `/prompt` | Every scored sub-dimension 5: UGT (one end state after the two-reading test), Feasibility, ACL reachability (every required scoped read YES), no tool names, not contrived, today = Wed Oct 1, Truthfulness, investigation + action, persona, **business function 5, competency 5, task skill 5**, a load-bearing complexity dimension, data seeding, Cross-Service Coherence 5 on all task-touched data incl. pre-existing defects — the dimension "fails on the **presence** of an inconsistency itself, whether or not it would cause an agent failure" (`1_Prompt_Eval.md` §1.5, §2.1, §3.2). | Fit argued in §3 (the competency gate is a local hard FAIL). Rules, definitions and exceptions live in records; the prompt is an ordinary request naming its destinations. "Never graded" is **not** enough for an artifact on the required path: §5.5 gives each required artifact's known contradictions and a resolution (kept off the path, or a dated claim overturned by a later seeded record), plus the residual risk. |
| `/hardness` | Score 5 = "genuine model failures invalidate the central result/delivery or defeat much of the core task" on the single unhinted Opus 5.5 run (`1A_Hardness_Eval.md` §5); 3–4 still PROCEED. | The central result is the beta calendar Frederick will run the bought cohort on: a missed trap starts an event before its server windows exist, runs a cancelled one-off over a recurring race, sends pushes with the old game name to bought users, or leaves a broken event on the calendar — consequential, not cosmetic (§6). |
| `/oe` | PASS: complete critical path (discovery, dependencies, every required write) with accurate tools, parameters, ids and expected data; no non-action or final-response event (`2_Oracle_Events_Eval.md`). | Every deciding record reachable from a prompt noun by a natural call; expected values quoted from records; catalog tool names only (`gsheets_create_spreadsheet`, `gsheets_values_update`, `slack_send_message`, `linear_create_comment`, S4 §2). |
| `/rubric` | No Major, no Moderate, Minor < 5 %; weights 1/3/5 by kind of work; ≥ 1 Outcome; Process ≤ 50 %; no row passable by doing nothing; one fact per row and never in ≥ 3 rows; ≤ 5 samples per group + a volume row + direct exception rows; predicted all-fail 0 (`3_Rubrics_Eval.md`; GEN_EXECUTION §3). | The planned surface (§6.4) keeps each trap's miss on ≤ 2 rows, weight 5 only where the work is multi-source; exclusions are graded as positive results inside the calendar ("Halloween one-off not on the calendar" is the calendar's content, with the Plague Race window present), never "leaves X alone". |
| `/create-difficulty` (`12_Difficulty.md`) | Six Opus 5.5 slots with provenance, ≤ 2 errored; corrected average **strictly < 85 %** (medium); < 5 full passes; population SD 0.10–0.30; ≥ 2 failure patterns, largest ≤ 50 %; ≥ 100 counted calls (golden run if any, lowest governs). | Six independent loss channels on different services and surfaces with graded findability (§6.1, §6.5); honest shortest path ≈ 178 counted calls under D5-b, but only ≈ 74 under D5-a — below the 100-call floor (§7, D5). |
| Local stage gates | `stage_gate.py` scenario → … → release PASS; `hardness_gate.py` at `effective_profile: extreme` (≥ 10 services, ≥ 120 rows, cohort ≥ 40 × 3 surfaces, ≥ 12 traps, …); dual red team or a recorded `RED TEAM FALLBACK:`. | Decisions D2 (volume exception), D4 (review fallback) and D5 (cohort spine) in §11; the cohort and the honest volume are the weakest structural points (§7, §8). |

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
`#zombie-bugs`, `#zombie-match3d`, DMs with Frederick and Robert), Linear (ZOM live-ops issues, ZOM-78), GitHub (match3d,
match3d-backend), Sheets (push sheet), Drive (her root). **Confluence and Snowflake are context only — never required,
never cited** (rev 2, §5.5): both synthetic sources carry known contradictions in exactly the pages a live-ops calendar
would lean on (SC-31, SC-38, SC-47, SC-62). The Trello BETA list stays off the path (SC-13/14).

**Injection plan: ten injected services, each with its own load-bearing fact** (companion-only rows, such as invitation
mail for a seeded event, are counted separately and never toward the ten):

| # | Service | Seeded record (planned) | Load-bearing fact it carries |
|---|---|---|---|
| 1 | Slack | Frederick's ask in `D05SD5QLG94` (Sep 30); Robert's approval reply in Martin's `#zombie-art` thread; Robert's withdrawal in `D05GU6L0XFH`; Douglas's reward and import notes in `#zombie-ops`; Vincent's prod re-test reply in a `#zombie-bugs` thread | anchor scope and destinations; C2; C5; SC-62 overturning record; C8 |
| 2 | Linear | dated note on the open ZOM-552 (Season Pass events not yet tagged); prod re-test notes only on **open** live-ops issues | SC-38 overturning record; per-issue spine (§8) |
| 3 | GitHub | `match3d-backend` Collect & Win windows PR with Douglas's dev-only deploy comment (repo has no Slack mirror, S5b §4) | C1 |
| 4 | Docs | Frederick's beta brief (shared with Julia), in his voice as the calendar's owner: the span and server time (UTC); the scope (every window, reset or start push, not only the events list); the working rules restated from his own page — windows go live only with a prod backend deploy, overlaps are fine, a one-off may displace a recurring slot only with Product's (Robert's) approval; the readiness rule (a beat runs only if its live-ops changes carry no open human review blocker and its open issues don't stop players entering, scoring or claiming); pushes go out only as Ready rows naming "Zombie Match 3D", else held for the copy owner; the November Season Pass season opens Nov 1 00:00 UTC with config locked 24 h before; Boss Arena off this calendar until the pivot call | the rules and scope every decision needs, so no Confluence page is required |
| 5 | Slides | Frederick's beta UA plan deck: the four buy weeks Mon Oct 6 – Sun Nov 2 and the geos | the calendar's span (plan dates) |
| 6 | Gmail | Leonard's mail to the product team (Sep 30) with the planned release of the Sep 30 builds (a plan date such as Fri Oct 3 "if both stores approve" — never an approval, which would postdate the seed bound) | "the beta build is live" input to every first window |
| 7 | GCal | the live-ops pod review with Frederick (Thu Oct 2) and the November Season Pass config lock (Fri Oct 31 00:00 UTC = Thu Oct 30 5:00 PM PT) as plan events, one copy per attendee calendar | due time for the deliverable; the season boundary |
| 8 | Drive | a Julia-owned "ZM Live Ops" folder (owner Julia in Drive) | the calendar's destination |
| 9 | Sheets | a Julia-owned calendar sheet in that folder with Frederick's headers (owner Julia in both Drive and Sheets rows, learnings §31) | the write target and its column contract |
| 10 | Trello | Brian's comment on the Axe Arena card in the "Oct 21" list (not the BETA list) moving it to the first post-beta release | Axe Arena's slot (a dated, Julia-visible record beyond the Sep 22 posts) |

Contacts carries no natural fact and is not used. Whether Slides and Gmail can each hold a fact that no other record
repeats (or the agent can skip them) is checked at S2/S9 (literal-value sweep); if either fails, the design drops to
nine injected services, which `hardness_gate.py` fails — then the volume exception does not help and a natural tenth
carrier has to be found, never padded.

**Hardness opportunities (each its own fact, detail §6).** v2 trap 1 done across services (Collect & Win merged and "QA
blockers cleared", server windows only on dev); trap 2 correction elsewhere (Robert's approval of a Halloween one-off in
Martin's thread, withdrawn in his DM); trap 7 outside the obvious filter (beats the calendar page does not list); trap 9
work someone already did (the Plague Race reward cut already live); trap 5 a rule in the data overriding a status (Ready
pushes with the pre-rename title); a tool-surface blind spot on the per-issue QA re-test (list views return no comments).

**Volume.** Shortest sufficient path ≈ 178 counted calls with the live-ops PR spine (D5-b), ≈ 74 without it (§7): below the local 500 floor in both cases, and below the platform's 100 without the PR spine.

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
| Natural population ≥ 40 | **weak**: 47 live-ops ZOM issues since Aug 1 (34 under the clock-window rule), thin per-record surfaces; or 41 live-ops PRs with genuine surfaces but an engineering slant (§8, D5) | no | 60 tiers, invisible to Julia |
| Honest volume | ≈ 110 (§7) | < 100 | < 100 |

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

### 5.1 Rules every decision needs, homed in incorporated records (rev 2: no Confluence page is a home)

| Decision | Rule (meaning, not wording) | Home (planned; base where possible) | Census / proof needed |
|---|---|---|---|
| Span and time base | Mon Oct 6 00:00 UTC – Sun Nov 2 23:59 UTC (the four buy weeks); windows stated in server time (UTC) as start–end instants; PT renderings of the same instant accepted, a different instant is not | UA plan deck (span) + Frederick's brief (server time) | every graded date is one instant with both renderings precomputed (PDT until Nov 2) |
| Scope | every ZM3D beat players can see in the span: a window, a reset or a start push; **Boss Arena off this calendar until the pivot call** (a dated decision, not a prod-date claim, so SC-68 is untouched) | Frederick's brief (one hop from the anchor) | census of every live-ops feature in the beta build (S1b §6) and all 14 "PNs Beta" rows; no completeness claim without it (learnings §23) |
| Window cadence | Collect & Win Mon-Tue / Wed-Thu / Fri-Sun; Plague Race rolling 5-day windows from 00:00 UTC; Endless daily 00:00 UTC + weekly Monday; quests weekly rollover; daily-login monthly rollover; Season Pass seasons on the 1st 00:00 UTC, config locked 24 h before | the brief (Collect & Win, Season Pass), Endless spec `f_9956263905ddb43d1500ff` (base Docs), a seeded dated Douglas statement for Plague Race (its only base evidence is Snowflake, which stays off the path) | each graded window computed from its rule; Plague Race windows Oct 2–6, 7–11, 12–16, 17–21, 22–26, 27–31, Nov 1–5 continue the base 5-day series |
| "Starts" | a beat starts with the first window that opens after (a) the beta build is live and (b) its server windows are live on prod | the brief's deploy rule (restating Frederick's own page) + Leonard's planned-release mail + the backend deploy note | no base record dates a Collect & Win prod deploy (S1b §2 "Negative pins"), so the seeded note conflicts with nothing |
| Held for tech | hold an event whose players **cannot enter, score or claim** on prod **even after a restart**; wrong counters, resets that need a restart, cosmetic, VFX and analytics gaps do not hold it | Leonard `C090N54TG79/1758517286.431379` ("Beta must be tech stable, no excuses") + the brief's readiness rule | applied to every open cohort issue (14): ZOM-534 (quest points reset only after a restart) → known issue; ZOM-556 (skipped daily gift does not reset the streak; claiming works) → known issue; ZOM-429 (weekly leaderboard session does not start without killing the app) → known issue **unless** Vincent's prod re-test says it fails even after a restart (C8) → held; every other open member gets exactly one answer under this sentence (learnings §21) |
| One-offs | may overlap recurring slots; displacing one needs Product's (Robert's) approval; the approver's latest dated call stands | the brief (Frederick restating his page) + seeded approval and withdrawal | census of Robert's records Sep 17 – Sep 30 for any other approval |
| Rewards / setup | reward settings in force are the latest dated change; no setup task for work already done | base thread `C090N54TG79/1757478958.104989` + a seeded completion note in `#zombie-ops` (matches the hidden base "plague stage rewards are fixed" and the 60/120/250 ladder) | every live-ops reward change asked in Sep (Plague Race halved; Leonard's Sep 13 "first step is to cut coins back to half" for a 4–5-minute mode, `C090N54TG79/1757726465.239759`) checked for a later record; the second is settled by a record too, or kept ungraded |
| Pushes | a push goes out only if its "PNs Beta" row is Ready **and** its copy names "Zombie Match 3D" and the right event; a failing row is **held** for the copy owner the brief names; the calendar names the change and the owner (Julia may propose wording, the row stays held) | the brief; the rename is also base Slack (58 "Puzzles vs Zombies" uses in `#zombie-match3d` June 2025; the Aug "Rename product" commit listed in `#zombie-bugs` `C08R27X0EAH` 2025-08) | all 14 rows read; only the 1-day lapse and D0-1 FTUE rows name the old title; the 7-day lapse row does not and is sendable |
| Destinations | calendar in the Julia-owned sheet; linked from ZOM-78; recommendation as a reply in the ask's DM | prompt (named) + the ask | ZOM-78 is the only calendar ticket (title search) |

### 5.2 Two-reading tests to run at S8

1. Merged vs live on prod (Collect & Win) → the brief's deploy rule + the dated deploy note decide; the first window is one
   instant (Fri Oct 10 00:00 UTC if the deploy lands Wed Oct 8, to be fixed by the seeded note).
2. Robert's thread approval vs his later DM → the later call by the same Product owner on the same item stands; no other
   Product approval exists in the census.
3. Ready vs stale copy → the copy rule decides; held, with the change named. "Send with corrected copy" is a different
   action and is not accepted, because the brief says rows go out as the sheet holds them.
4. The obvious event list vs the brief's scope → the brief governs; resets with pushes (quests, daily login) are in. Any row layout accepted.
5. Reward cut pending vs done → the dated completion note decides.
6. Restart-clears faults and wrong counters (ZOM-534, ZOM-556, ZOM-429 without the re-test) → known issues under the enter/score/claim sentence; no second reading survives.
7. Boss Arena → off this calendar by the brief's dated decision; a run that lists it as "off" or omits it passes; a run
   that schedules it fails the scope rule (one end state).
8. Halloween app icon (Martin's post also mentions an icon) → not a live-ops beat; out of scope, never graded.
9. Sheet layout, wording, date format, PT/UTC rendering of the same instant → any equivalent accepted (learnings §8).

### 5.3 Boundaries the rubric accepts in full

Row layout (one row per beat or per window), labels, PT or UTC (or both) for the same instant, the order of the
recommendation, owner names only where a record names one by name (tokens such as `[PERSON_NAME_0092]` are never graded).

### 5.4 Writes the rubric will not loosen

The reply goes in Frederick's DM (not a channel post); the calendar link goes on ZOM-78 (not a new ticket); pushes that
fail the copy rule are held, not rewritten in place — learnings §5.

### 5.5 Coherence plan for every artifact on the required path (rule 3; `1_Prompt_Eval.md` §3.2 "fails on the presence")

Rev 2 follows the strict reading (red-team findings 1 and R2-4): keeping a contradiction's other side off the path does not
repair a false statement inside a **required** artifact. So the design requires and cites **no** artifact that carries a
known contradiction — the playbook's `excluded` resolution ("the hazard's records are neither modified by the SQL nor cited
by the design", 01 S1) — and puts every rule it needs into records whose owners would write them.

| Status | Artifact | Known contradictions | Treatment |
|---|---|---|---|
| excluded (context only) | `page_liveops_calendar` | SC-62 import cadence; Domino rows (SC-31, SC-47); "Weekly Leaderboards — DD / ZM3D — Live" vs DD-only warehouse rows; "Friday all-hands" vs no 2025 H2 event | never required or cited; the brief restates only the page's sentences that no card touches (overlaps fine, Product approval to displace, windows need a deploy) and none that a card touches |
| excluded | `page_season_pass_spec` | SC-38 (production week; "events are tagged" vs ZOM-552) | the Nov 1 00:00 UTC season start and 24 h lock come from the brief and a GCal plan event |
| excluded | `page_zm3d_gdd`, `page_live_ops_engine`, `page_product_okrs` | SC-8, SC-58, SC-31, SC-28 | not needed (the rename comes from the brief and base Slack) |
| excluded | Snowflake `LIVE_EVENT_PERFORMANCE`; Trello BETA list and cards 54/56/58/67 | page/warehouse pairs; SC-13, SC-14 | Plague Race cadence from a seeded dated statement; Trello weight from the Axe Arena card in "Oct 21" |
| required | push sheet `f_a325dd4af80afc5994d5dc` | "PNs" (Domino-era) vs "PNs Beta" tabs; "Win & Collect event start" for ZM3D | two tabs with different purposes (not a contradiction); only "PNs Beta" used; the display name is never graded; the stale title on two Ready rows is the designed work item, overturned by the brief and the base rename record |
| required | Frederick DM, Robert DM, `#zombie-design`, `#company-internal`, `#zombie-art`, `#zombie-ops`, `#zombie-bugs` | SC-7 (membership), SC-70 (Slack time zones) | membership and time zones never used; seeded DM text only in English DMs |
| required | ZOM live-ops issues, ZOM-78 | SC-16 tickets not in the cohort (checked); SC-22 `time_in_status` | never used; no note after `completed_at` |
| required | `match3d` live-ops PRs, `match3d-backend` | SC-18 (#477); SC-56 (commit-title case) | #477 never decides; no `#builds` title matching; seeded `match3d` review comments carry their `#zombie-prs` INT-01 copy |

**Residual risk (open, not hidden):** the excluded pages are still in the universe and on the same topic; a `/prompt`
reviewer may read them as "task-touched" because an agent will likely open them. The design cannot change them (Confluence
is not injectable). If you judge that risk unacceptable, storyline A should be dropped, because every live-ops storyline at
this clock sits next to these pages.

Coherence hazards touched (KB `coherence_hazards.json`, S5b §1): T04, S01, R07, L03, I15, I01/I18, Q01/Q04, L08–L10;
`/create-scenario` S1 cites each with its disposition; all six categories are covered.

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
| C1 | 1 · proving "done" across services | match3d#468/#470/#472 merged into main before the Sep 30 cut (GitHub, Sep 29–30), Julia's own Sep 22 meeting notes "[PERSON_NAME_0067] and Douglas feature completed Win and Collect" (`C05KNDCHAAG/1758558302.777379`) and Leonard's Sep 12 beta pipeline listing it | a dated Douglas comment on the `match3d-backend` Collect & Win windows PR: deployed to the dev stack only, prod with a named later backend release; the brief's deploy rule decides the first prod window | tier 3: another repo, a PR conversation comment (no Slack mirror) | "merged" and "feature completed" are true; only the deploy meaning decides | Collect & Win first window (5) · reply names it as late (3) |
| C2 | 2 · a correction somewhere else | Robert's reply in Martin's `#zombie-art` Halloween thread approving a one-off in Plague Race's last-October slot (Product owner, documented approval) | Robert's later message in his DM with Julia withdrawing the event (no event art before the pivot call) — same person, same item, other container | tier 2: a DM with 286 Sep messages, the withdrawal near its end | the approval is real and the page's displacement rule is satisfied by it until the later DM | no Halloween one-off on the calendar (5) · Plague Race Oct 27–31 window present (5) |
| C4 | 7 · items outside the obvious filter | the event list everyone uses — Leonard's beta pipeline and the animated live-ops icons (Plague Race, Collect & Win, Season Pass, Endless, leagues) | Frederick's brief (one hop from the anchor) brings in every reset with a start push: the quests weekly rollover (push row "New Quests Await!") and the daily-login monthly rollover (push row "Login Calendar update"), both live (S1b §6) | tier 2: the scope sentence is one read away from the anchor | the agent must apply the brief's scope to features nobody calls events | one row per member (5 + 5) · beat count (3) |
| C5 | 9 · work someone already did | Leonard's Sep 10 ask to halve Plague Race rewards, Vincent's "60, 120, 250?" and "sounds good" (same thread) — reads as setup still to do | a dated completion note away from that thread (Douglas in `#zombie-ops`, or on an open ticket) recording the new stage rewards live on prod; matches the hidden base "plague stage rewards are fixed" | tier 2 | the ask is real and has no visible completion in its own thread | no reward-change task in "still to do" (5) · rewards in force 60/120/250 (3) |
| C6 | 5 · a rule hidden in the data | the push sheet's own "Ready" status on the 1-day lapse and D0-1 FTUE rows | the brief's copy rule ("Zombie Match 3D") backed by the base rename record (Aug "Rename product" commit in `#zombie-bugs`; the old name in `#zombie-match3d` June 2025): both rows still say "Puzzles vs Zombies" | tier 1 to find, tier 2 to apply | the stale title is visible in the sheet, so this channel is **weaker** than C1/C2 (design miss rate 0.30); it costs a run only if it trusts the owner's Ready column | 1-day lapse push held for copy (5) · FTUE push held (3) |
| C8 | tool-surface blind spot (A3) on the tech-stable rule | ZOM-429 "Leaderboard next session doesn't start without killing the app" (Backlog, 2025-07-22) reads as a known annoyance with a restart workaround, and the list view shows nothing newer | Vincent's Sep 30 re-test on the prod build, a reply in an older `#zombie-bugs` report thread about the weekly leaderboard (not the issue, not the anchor), shows the weekly session not starting even after a restart → the leagues beat is held | tier 2: Slack search returns replies (Ask_Carriers §6b), so the re-test is reachable by a leaderboard search; the issue itself has no comment (base Linear holds 0 comments) | only a run that applies the restart clause to fresh prod evidence holds the beat (design miss rate 0.35) | leagues beat held with its reason (5) |

Load-bearing pair named for the guide's "1–2 traps that carry the difficulty": **C1 (done across services) and C2
(correction elsewhere)** — two separate cross-source decisions on distinct v2 trap types, each naming its wrong source and
its winning record. C4–C8 add independent spread, and three of them are deliberately rated lower because a complete sweep
or the first reads can settle them (red-team finding 5): C4 0.30 per member, C6 0.30, C8 0.35. The largest unit of discovery decides C2's 10 of 67 weight points
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
and the row stays ordinary (never raise a weight). Re-run on sketch rev b (rev c: C8 re-homed after red-team finding 4; C4's scope rule in the brief; no Confluence or Snowflake record on any trap) — verbatim,
`research/hardness_v2_check_sketch.txt`:

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

Planned surface: 19 slots, total weight 67, 8 weight-5 slots, 4 ordinary samples (Plague Race cadence, Endless reset, Axe
Arena off, the 7-day lapse push sent) plus a volume slot and two delivery slots; weights by kind of work, never raised
(`research/00_sketch_geometry.json`, rev b). Scored with `research/scripts/geometry_mc.py` (adapted from Claire's, same
logic), which grades simulated six-run baselines with the bundle's own gate math (`difficulty_stats._gates`, **medium**,
long-horizon). **What it measures:** the four scoring gates (average < 85 %, < 5 full passes, SD band, failure patterns),
**conditional on six completed runs inside the horizon tier** — every simulated run is marked completed with 300 calls, so
error rate and horizon are not modelled (red-team finding 7); they are treated separately in §7 and §10. Output (verbatim,
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
  scale 1.00: E[avg] 66.6% (p10-p90 56.2%-76.9%)  E[SD] 0.172  P(avg<85%) 0.99  P(<5 full) 1.00  P(SD band) 0.82  P(patterns) 1.00  P(all four) 0.82  E[full passes] 0.36
           P(row fails all six) >= 1%: {'S_C1_cw_first_window': 0.014, 'S_C1_reply_cw_late': 0.014, 'S_C2_halloween_not_scheduled': 0.015, 'S_C2_plague_last_oct_window_kept': 0.015}
  scale 0.75: E[avg] 73.6% (p10-p90 63.7%-83.3%)  E[SD] 0.162  P(avg<85%) 0.94  P(<5 full) 1.00  P(SD band) 0.77  P(patterns) 0.99  P(all four) 0.75  E[full passes] 0.68
  scale 0.60: E[avg] 78.0% (p10-p90 68.4%-87.1%)  E[SD] 0.151  P(avg<85%) 0.83  P(<5 full) 1.00  P(SD band) 0.70  P(patterns) 0.99  P(all four) 0.64  E[full passes] 0.96
  scale 0.50: E[avg] 81.0% (p10-p90 71.9%-89.3%)  E[SD] 0.142  P(avg<85%) 0.71  P(<5 full) 1.00  P(SD band) 0.64  P(patterns) 0.98  P(all four) 0.54  E[full passes] 1.20
  scale 0.35: E[avg] 85.6% (p10-p90 77.6%-92.8%)  E[SD] 0.124  P(avg<85%) 0.43  P(<5 full) 0.99  P(SD band) 0.49  P(patterns) 0.96  P(all four) 0.32  E[full passes] 1.68
```

Design miss rates (rev b, scale 1.0): C1 0.50, C2 0.50, C4 0.30 per member (ρ 0.5), C5 0.45, C6 0.30, C8 0.35; slips
0.03–0.06; a per-run thoroughness latent (loading 0.5) correlates the channels. These are assumptions: the Opus 5.5 ledger
(`hardness_ledger.py priors --model claude-opus-5-5`) holds Beta(1,2) one-trial priors for A7 and A14–A17, Beta(1.86,2) for
A1 and nothing for A3, A8, A11, A24 or A25. Claire's R3 (`task_inputsH/Working_Files/research/R3_opus_failure_modes.md` §2)
verifies the done-across (2.1), correction-elsewhere (2.2), outside-filter (2.4) and record-never-opened (2.5) modes on
completed tasks, and finds follow-through and slips contradicted (2.3, 2.9).

**Sensitivity — sweep- and judgment-settled channels solved** (C4 and C6 missed 10 % of the time, C8 15 %; C1, C2, C5 as
designed; `research/geometry_mc_sens_judgment.txt`):

```text
SIX-RUN BASELINES (20000 draws per scale; gate math = difficulty_stats._gates, medium, long-horizon)
  scale = multiplier on every design miss rate (1.0 = design rates; <1 = a stronger Opus)
  scale 1.00: E[avg] 74.3% (p10-p90 65.2%-83.1%)  E[SD] 0.148  P(avg<85%) 0.94  P(<5 full) 1.00  P(SD band) 0.70  P(patterns) 0.98  P(all four) 0.67  E[full passes] 0.62
           P(row fails all six) >= 1%: {'S_C1_cw_first_window': 0.014, 'S_C1_reply_cw_late': 0.014, 'S_C2_halloween_not_scheduled': 0.015, 'S_C2_plague_last_oct_window_kept': 0.015}
  scale 0.75: E[avg] 79.7% (p10-p90 71.1%-87.8%)  E[SD] 0.138  P(avg<85%) 0.78  P(<5 full) 1.00  P(SD band) 0.62  P(patterns) 0.97  P(all four) 0.54  E[full passes] 1.01
  scale 0.60: E[avg] 83.0% (p10-p90 74.9%-90.8%)  E[SD] 0.129  P(avg<85%) 0.60  P(<5 full) 1.00  P(SD band) 0.53  P(patterns) 0.96  P(all four) 0.41  E[full passes] 1.34
```

**Against the goal's bar (E[avg] ≤ 77 %, P(all gates) ≥ 0.5), conditional on valid runs inside the tier:** design rates
66.6 % / 0.82; the bar holds down to a miss-rate scale of about 0.7 (73.6 % / 0.75 at 0.75; 78.0 % / 0.64 at 0.6). With the
weak channels solved: 74.3 % / 0.67 at design rates for C1/C2/C5, 79.7 % / 0.54 at 0.75. **Binding risk: a strong Opus.**
Every single miss leaves a run at 80.6–92.5 %, so the 85 % cap needs about two misses per run; the margin rests on C1, C2
and C5 staying off the first-read path. **What would buy margin** if `/create-scenario`'s forecast on the real surface comes
back above 77 %: a seventh channel on a different service and surface (candidates: a v2 trap 4 boundary — the November
Season Pass config lock falls on Thu Oct 30, 5:00 PM PT, the day before the UTC date, and changes a "still to do" deadline;
or a v2 trap 6 alias — the push row "Win & Collect event start" vs the ZM3D "Collect & Win", which the page itself
explains, so only as support), or fewer ordinary samples — never raised weights, never padding.

### 6.5 Spread (rule 5)

Each channel's deciding record sits on a different surface — a backend PR comment (C1), a DM (C2), a brief one hop from
the anchor (C4), a channel post away from the ask's thread (C5), push-sheet copy against the rename (C6), a thread reply
under a non-anchor root (C8) — with findability tiers 1–3, so runs fail different subsets: P(patterns) ≈ 0.98–1.0 and
P(SD band) 0.64–0.82 at scales 0.5–1.0. The highest predicted all-six miss is C2's pair at 1.5 % (scale 1.0) — VALID
workload if it happens (every value reachable), not a predicted all-fail.

---

## 7 · Volume plan (honest, never padded; recounted in rev 2 after red-team findings 2 and R2-2)

| Phase | Services | Calls, shortest sufficient path | Why each is necessary |
|---|---|---|---|
| Anchors and rules | Slack (the ask, 1), Docs (the brief, 1), Slides (UA plan deck, 1), Gmail (planned-release mail: search + read, 2), Sheets ("PNs Beta" metadata + tab, 2), GCal (pod review / season lock, 1) | 8 | each carries a different rule, date or scope |
| Enumeration | Linear (live-ops issue list, 3 pages; ZOM-78 search, 1), GitHub (backend + client live-ops PR searches, 3), Slack (`#zombie-design`, `#company-internal`, `#zombie-art`, `#zombie-ops`, `#zombie-bugs`: 6 searches/windows), Trello (1) | 14 | the scope rule needs every beat, live-ops issue and live-ops PR |
| Per-beat readiness | Collect & Win backend PR + comments (2), Plague Race cadence note (1), Endless spec (1), Zombie Lane doc (1), leagues re-test thread (1), Axe Arena card (1), Halloween thread (1) | 8 | each beat's start depends on its own record |
| Hidden authorities | Robert DM history (2), completion note (1) | 3 | one authority each |
| Writes + read-backs | sheet values (2) + read-back (1), DM reply (1), ZOM-78 comment (1) | 5 | each write is requested |
| **Non-spine subtotal** | | **38** | |
| Spine, issues (§8 D5-i) | `linear_list_comments` on all 47 live-ops issues (each carries the prod re-test or owner note the readiness rule reads; base has 0 comments, so these are seeded, dated before `completed_at` on Done issues) | 47 | the held-for-tech rule needs each issue's prod state |
| Spine, PRs (§8 D5-i) | reviews + inline review comments on the 31 live-ops PRs outside Boss Arena (41 minus 10 Boss Arena PRs) | 62 | the readiness rule needs "no open human review blocker" per PR; neither surface comes back from a list or search call (learnings §53) |
| **Total** | 10 services | **38 + 47 + 62 ≈ 147** | ≥ 500 is not reachable without padding; 147 clears the 100-call floor with ≈ 47 margin |

Without the spine the honest total is **38** (the rev-1 figure of "58 without the spine" double-counted 16 spine calls; the
cohort has **14** open issues, not 16 — ZOM-516 is a Duplicate and ZOM-551 Canceled). With only the 14 open issues' comments
it is 52; with 41 × 3 PR reads instead of the issue spine it is ≈ 161. Observed counted calls on comparable completed tasks
run far above the shortest path (163–1,209, Claire R3 §1), but the margin must come from necessary calls, which only the
spine provides.

---

## 8 · Cohort spine (hard gate 3: ≥ 40 records × ≥ 3 per-record surfaces over ≥ 2 services)

The volume exception lowers only the call-budget and per-record floors; the cohort floor stays (`hardness_gate.py`
`cohort_size` and `evidence_surfaces`, read in its source: ≥ 40 records, ≥ 3 surfaces over ≥ 2 services, each with a true
`why_no_bulk` and a `short_circuit` analysis). Populations checked (S2): Zombie Lane nodes (live sheet not visible), Season
Pass tiers (NO), quests (no list), event reward lines (~25), push rows (14, one read), Trello cards (sparse, SC-13/14), store
reviews (templated text), levels (level design, not GTM). The two candidates on the plan's decision path:

**Live-ops ZOM issues.** Predicate: ZOM issue whose title names a live-ops feature (whole-word: Plague Race, Collect & Win,
Season Pass, Boss Arena / Infinite HP Boss, Endless, leaderboard/league, quest(s), daily gift/login, Zombie Lane / Trophy
Path, event icon, push notification), open at the clock or closed on/after 2025-08-01. Count **47** (Done 31, Todo 7, Backlog
3, In Progress 3, In Validation 1, Duplicate 1, Canceled 1; **14 open**); 39 without Boss Arena issues. Members
(`research/raw/cohort_liveops_issues_since_aug.json`): ZOM-297, 304, 344, 358, 395, 401, 429, 432, 433, 435, 459, 463, 465,
466, 470, 471, 473, 474, 478, 479, 485, 487, 488, 489, 490, 501, 504, 506, 509, 510, 515, 516, 517, 534, 540, 547, 548, 550,
551, 552, 553, 555, 556, 557, 562, 565, 566. None is an SC-16 ticket.

**Live-ops PRs.** Predicate: `match3d` / `match3d-backend` PR whose title or branch names a live-ops feature, created Aug 1 –
Sep 30: **41** (40 match3d + backend#34; 37 merged); 31 outside Boss Arena (Boss Arena is off the calendar, so its PRs leave
the population — red-team R2-1). Of the 41, 25 have reviews and 14 inline review comments (`research/raw/github.json`; not
independently re-certified by the reviewer).

| Surface | Service | Members | Honest `why_no_bulk`? |
|---|---|---|---|
| issue state + description | Linear | 47 issues | **no** — the list call returns both |
| issue comments | Linear | 47 issues (all seeded; base has 0) | yes |
| report / re-test thread | Slack | 17 issues reported Aug–Sep | **no** — search returns replies (Ask_Carriers §6b) |
| `#builds` change lists | Slack | per build, not per PR | **no** — one channel read covers many PRs |
| PR changed files | GitHub | 31 PRs | yes, but no requirement needs every file list (red-team R2-1) |
| PR reviews | GitHub | 31 PRs | yes |
| PR inline review comments | GitHub | 31 PRs | yes |

**Verdict: no single population of ≥ 40 records has three honest no-bulk surfaces over two services.** The issues have one
(comments); the 31 non-Boss-Arena PRs have two (reviews, inline comments) and are below 40 on their own; combining them
gives two record types, each short of three surfaces. Gate 3 therefore **cannot be certified honestly for storyline A**, and
— on the evidence in S2 — not for B or C either. This is a conflict between the local extreme profile and this
persona/competency, and only you can resolve it (D5). Padding a third surface (filler threads, synthetic per-record docs)
is a failing error and is not an option.

---

## 9 · Writes and ownership (rule 6)

| Write | Trigger the persona owns | Write access |
|---|---|---|
| Beta calendar (Google Sheet) | Frederick's ask to Julia; the page names Design (Julia) in the weekly walk | Julia-owned: the seeded calendar sheet in her seeded "ZM Live Ops" folder, with `owner_email` Julia in both the Drive and Sheets rows (learnings §31), written with `gsheets_values_update`; if instead created at run time, `gsheets_create_spreadsheet(title, initialSheetTitle, driveFileId)` makes one tab and extra tabs need `gsheets_batch_update addSheet` (S4 §2). Never the Resource-owned push sheet |
| Recommendation reply to Frederick | the ask itself | Julia is a member of `D05SD5QLG94` (YES) |
| Calendar link on ZOM-78 (comment) | the ask names the calendar ticket | Linear unscoped; ZOM team writes confirmed in the pre-check |
| Optional: one or two setup tickets (e.g. the push copy fix) | the ask's "what is still to do, by whom" | Linear unscoped; reuse an existing ticket where one covers it |

---

## 10 · Risks and open items

1. **Gate 3 (cohort shape) cannot be certified honestly** for storyline A (§8) — and, on S2's evidence, for B or C. It needs
   your decision (D5) and, under D5-i, a requester-confirmed exception that `hardness_gate.py` does not implement today.
2. **Horizon:** the honest shortest path is ≈ 147 calls with the issue + PR spine and 38 without it (§7). The spine is
   necessary only because the brief's readiness rule reads each issue's prod note and each PR's human reviews; if
   `/create-scenario` cannot make that rule natural, the task falls below the 100-call floor.
3. **Competency drift:** the spine is engineering-shaped (issues, PR reviews); every graded row must stay a calendar,
   campaign or communication outcome and the request must read as the GTM calendar (`/prompt` §1.5 is a local hard FAIL).
4. **Coherence residual (§5.5):** the excluded Confluence pages are still in the universe on the same topic; a `/prompt`
   reviewer may treat them as touched. Not fixable by injection.
5. **The brief is a hub:** it carries the scope, readiness, copy and one-off rules (rules, not answers). C4 and C6 sit one hop
   from the anchor and are rated weak (0.30); the margin rests on C1, C2 and C5, whose deciding records sit elsewhere.
6. **A strong Opus** (scale ≤ 0.6) pushes E[avg] past 77 %; with the weak channels solved, P(all gates) is 0.54 at scale 0.75
   (§6.4). A seventh channel is the first lever.
7. **Ten injected services** depend on Slides and Gmail each holding a fact no other record repeats (§4.1).
8. **Seeding load:** 47 per-issue notes (dated before `completed_at` on Done issues) and human review blockers on a few of
   31 PRs, each `match3d` comment with its `#zombie-prs` INT-01 copy; seeds must stay consistent with the hidden base
   ("plague stage rewards are fixed"), Robert's Sep 29–30 stance and Frederick's playable pause; the release mail is a plan.
9. **Language:** seeded DM text only in English DMs (Frederick, Robert). **Theme:** ZM3D content is unavoidable (D3).
10. Ledger priors for A3, A8, A11, A24, A25 are empty; the geometry is conditional on six completed runs inside the tier.

---

## 11 · Decisions needed from you

| # | Decision | Recommendation |
|---|---|---|
| D1 | Storyline | **A — ZM3D beta-weeks live-ops and player-push calendar** (§4.4), **conditional on D5-i**. It is the best fit (Julia is named for this work on the calendar page) with the strongest traps; its structural gaps (§8, §10.1–10.4) are stated, not solved |
| D5 | Cohort spine (hard gate 3) — **blocking for `/create-scenario`** | **D5-i:** approve a recorded, requester-confirmed deviation from the extreme cohort *shape* for this task: a two-type spine on the plan's decision path — the 47 live-ops issues (one honest no-bulk surface, comments) and the 31 non-Boss-Arena live-ops PRs (two: reviews, inline review comments) — ≈ 109 necessary per-record calls over Linear and GitHub. `hardness_gate.py` supports only `volume_exception`, so the tool owner must add the exception first; I may not edit `Task_Authoring/tools/`. **D5-ii:** pick another storyline — none with a natural ≥ 40 × 3 population was found for Julia × Marketing and GTM at this clock (S2; the 100-level ladder fails the competency). **D5-iii (rejected):** add filler surfaces or members to reach the shape — padding, a failing error |
| D2 | Volume exception (GEN_EXECUTION §3a; ≥ 500 necessary calls not reachable without padding) | **Yes, under D5-i:** `volume_exception {call_budget_floor: 130, per_record_floor: 100}` (§7: 38 non-spine + 109 spine ≈ 147; re-derived at S2/S7 from the census), with your confirmation recorded as `requester_confirmation`; every other extreme target stays (≥ 10 services, ≥ 120 rows, ≥ 12 traps, …) |
| D3 | Theme screen (playbook 01 S0: no zombie/outbreak theme) | **Waive for this task, recorded:** every Julia storyline at this clock is ZM3D; Claire's R3 §5 found 0 refusals or fallbacks in 13 Opus 5.5 runs on ZM3D data. Mitigation: seeded text says "ZM3D" / event names, never "infection" or "outbreak"; every pre-check and baseline is checked for model fallback |
| D4 | Review waiver | No `REDTEAM_*` variables are set in this shell (`env | grep -c '^REDTEAM'` → 0), so `redteam_review.py --dual` cannot run. Either set `REDTEAM_*` (preferred), or approve a recorded `RED TEAM FALLBACK:` using this session's independent GPT `redteam` and `oracle` subagents on the design (kept in every Unresolved line until covered, learnings §44). This analysis itself was reviewed that way (§13) |

---

## 12 · The goal's seven rules, and where this analysis answers each

| Rule | Answered in | Status at this stage |
|---|---|---|
| 1 UGT (each material choice fixed by the prompt or a Julia-visible record, or bounded; every rule sentence applied to every item; census before completeness) | §5.1 (home + census per decision: span, time base, scope incl. Boss Arena, enter/score/claim hold rule applied to all 14 open issues, push holds), §5.2 (nine two-reading tests), §5.3 | planned; S1/S8 run the censuses and the fork sweep |
| 2 Fit (Product & Design inside Marketing and GTM) | §3, §10.3 | argued; the engineering-shaped spine is the named risk |
| 3 `/injection` (whole-universe check, seeds after base events, tool-visible) | §4.1 injection table, §5.5 (no contradicted artifact required or cited), §5.6, §10.8 | planned; `base_check`, `base_claims` and `hg.py lint` run at injection |
| 4 `/hardness` (≥ 3 independent channels, none over half, ≥ 2 cross-source decisions on distinct named v2 traps with wrong source and winning record; nothing passes by doing nothing; weight 5 by kind of work) | §6.1 (six channels on six surfaces, largest 15 %), §6.2, §6.3 (Part 7 checks + positive control) | sketch CLEAN on all six applicable checks (rev c) |
| 5 Spread (graded findability; E[avg] ≤ 77 %, P(all gates) ≥ 0.5, UNCALIBRATED) | §6.4, §6.5 | 66.6 % / 0.82 at design rates, holds to scale ≈ 0.7; weak-channels-solved 74.3 % / 0.67; conditional on valid runs inside the tier |
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

Round 3 (confirmation of rev 2): _(below)_
