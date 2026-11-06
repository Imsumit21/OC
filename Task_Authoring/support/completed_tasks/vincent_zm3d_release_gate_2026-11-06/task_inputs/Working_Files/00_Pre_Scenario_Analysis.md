# Pre-scenario analysis — Vincent Parker · Engineering · Engineering Ops · Analysis and synthesis · Long Horizon · Easy · Oct 1, 2025 (synth-cut)

Analysis only. This file holds no prompt, Oracle Event or rubric text; it prepares `/create-scenario`. No SQL was
written or executed, and nothing outside `Task_Authoring/task_inputs/` was written.

| Item | Value (source) |
|---|---|
| Clock | `Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)` (`hg.py universe show`) |
| Seed bound | `2025-10-01T00:00:00Z` = Tue Sep 30, 5:00 PM PT: every seeded event timestamp must be at or before it (`sql_lint.py`); base records 00:00–07:00Z Oct 1 exist (data horizon) and were checked (§5.5) |
| Persona today | Wednesday, October 1, 2025; "yesterday" = Tuesday, September 30 (GEN_EXECUTION §0a; learnings §20) |
| Universe | synthcut, `hg4-synth-sep30cut v16`, shutdown rules do not apply; Victor Barnes departed Apr 2025 |
| Context | `task_context.py --write --require-source` → `source.status: ready`, `kb_status: bound`, `context_hash fb209f3058d7e399087b2b69e0108dfc9429f64c9c1cb45eeb3e417275bd498a` |
| Assignment | `00_Assigments.md` sha256 `c2f3888d…6deac`, identical to the Evals store's saved `task-details` (store `universe_intake: SELECTED synthcut`; read-only check, store not written) |
| Tools | `Task_Authoring/tools` last changed in `58c37b1` (2026-11-03 03:40 +0530); learnings §57: re-check before any gate run |
| Evidence files | `Working_Files/research/` (raw reads through `tools/hg.py`, the sketch manifest/surface, `geometry_mc.py` and its output, the Part 7 check outputs) |

---

## 1 · What a 5 needs at each gate

| Gate | A 5 / PASS needs | What this task must do to get it |
|---|---|---|
| `/injection` (static, Checks A–C) | A: every id, reference and person token exists or is new and collision-free, and every seeded fact agrees with the **whole** universe, not the persona's view (learnings §10, §14, §15). B: SQL valid against `universe_schema_live.json`, only the 64 writable tables (never Snowflake or `_changelog`, §50). C: dates and chronology — every seed after the base events it relies on (§13, §17), before the seed bound, no Linear comment after its ticket's `completed_at` (§50), companions present (thread counters, `updated_at`, INT-01 Slack mirrors for match3d PR comments into `#zombie-prs` `C093LEZGF6J`, one GCal copy per attendee plus invitation mails, R08). | Census each seeded ticket, build, person and claim across all 13 services; every claim about a build or branch checked by `base_claims.py` (B1–B4) against `#builds` and git (§49); no injected Confluence page (§26, §32): use the base pages as authorities. |
| `/prompt` | Every scored sub-dimension 5 (lowest wins): UGT (two-reading comparison done, one end state), Feasibility, ACL reachability (every required scoped read YES), no tool names, Clarity, not contrived (short ordinary request, no spec), today's date (Wed Oct 1), Truthfulness (every descriptor true), cross-service, investigation + action, coherence (no bolt-on), persona, business function 5 (not 3), competency 5, task skill 5, complexity dimensions + data seeding, data exists, Cross-Service Coherence 5 on all task-touched data incl. pre-existing defects (`1_Prompt_Eval.md` §4.1, §3.2). | Fit argued in §3; every rule and exception lives in records (Ambiguity + Dynamic Change + Multi-Source all load-bearing); destinations named; the known-data-issue cards in the task's area settled or kept out (§5.4). |
| `/hardness` | Score 5 = "genuine model failures invalidate the central result/delivery or defeat much of the core task" on the single unhinted Opus 5.5 run (`1A_Hardness_Eval.md` §5); 3–4 still PROCEED. | The central result is the release decision and its blocker list: a missed blocker ships a crash or progression loss, so each designed miss is consequential, not cosmetic (§6). |
| `/oe` | PASS 5: complete critical path (discovery, dependencies, every required write) and accurate tools, parameters, ids and expected data; no non-action or final-response event (`2_Oracle_Events_Eval.md` §4.1). | Every deciding record reachable from a prompt noun by a natural call; expected values quoted from records; catalog tool names only (`linear_update_issue`, `gsheets_values_update`, `slack_send_message` …, learnings §6). |
| `/rubric` | No Major, no Moderate, Minor < 5 %; weights 1/3/5 by kind of work; ≥ 1 Outcome; Process ≤ 50 %; no row passable by doing nothing; no prohibition-only title; one fact per row, never in ≥ 3 rows; ≤ 5 samples per group + a volume row + direct exception rows; predicted all-fail 0 (harness tolerance) (`3_Rubrics_Eval.md` §4.2, §5.1–5.2). | Planned surface (§6.4) keeps each trap's miss on 1–2 multi-source rows of weight 5 by work kind, never raised; exclusions graded as positive results (a verdict in the register), never "leaves X alone". |
| `/create-difficulty` (`12_Difficulty.md`) | Six Opus 5.5 slots with provenance, ≤ 2 errored; corrected average strictly < 90 % (Easy); < 5 full passes; population SD 0.10–0.30; ≥ 2 failure patterns, largest ≤ 50 %; ≥ 100 counted calls (golden run if any, lowest count governs). | Graded findability across ≥ 3 independent channels so runs fail different subsets (§6.5); honest volume ≥ ~300 (§7). |
| Local stage gates | `stage_gate.py` scenario → … → release PASS; `hardness_gate.py` at the manifest's `effective_profile: extreme` (Long Horizon); dual red team or a recorded `RED TEAM FALLBACK:`. | Decisions D2 (volume exception) and D4 (review) in §10 settle the two gate inputs this stage cannot settle alone. |

---

## 2 · Vincent's reach at the clock

`python3 Task_Authoring/tools/persona_view.py reach vincent_parker --top 10` (verbatim):

```text
REACH  Vincent Parker <vincent.parker@harmonygames.co>  Game Systems Engineer / Engineering
clock 2025-10-01

SLACK  user=EMPLOYEE_0012_SLACK_ID  visible channels=140 {'mpim': 32, 'public': 40, 'private': 45, 'im': 23}  messages=262653  public-not-member (UNVERIFIED)=27
  persona posts=39854 last post=2025-09-30  last activity in visible channels=2025-10-01
  C05433XK267    builds                                 public  mem=31  msgs=35617  2023-04-20..2025-10-01
  C05H8KVNU67    game-design                            private mem=27  msgs=22750  2023-07-16..2025-08-28 archived
  D0770ET1HV2    D0770ET1HV2                            im      mem=5   msgs=22707  2024-06-06..2025-09-30
  C050WGU41HR    engineering-bots                       private mem=35  msgs=19854  2023-03-29..2025-09-19
  C05V5FNLB9V    god-bugs                               private mem=31  msgs=16695  2023-10-07..2025-07-15
  C0880U9751A    zombie-match3d                         private mem=25  msgs=16250  2025-01-09..2025-09-30
  C06FF10MMAM    [SOURCE_ORG_0001]-monkey               public  mem=6   msgs=14709  2024-01-22..2025-08-30
  CC43664F351E   mpdm-julia.lawson--brian.foster--vince mpim    mem=4   msgs=9711   2024-06-26..2025-09-25
  D05QA585LTY    D05QA585LTY                            im      mem=5   msgs=6709   2023-09-21..2025-09-15
  D07GJJBFHA5    D07GJJBFHA5                            im      mem=5   msgs=5410   2024-08-08..2025-09-30

GMAIL  mailbox=vincent.parker@harmonygames.co threads=1258 messages=1367 range=2023-08-30..2025-09-30
  threads by last-message month (recent): {'2025-04': 62, '2025-05': 138, '2025-06': 115, '2025-07': 79, '2025-08': 84, '2025-09': 55}
  top correspondents: SVC_2398_EMAIL (300), leonard.hayes@harmonygames.co (235), robert@harmonygames.co (214), julia.lawson@harmonygames.co (211), SVC_0203_EMAIL (144), brian.foster@harmonygames.co (143), arthur.blake@harmonygames.co (140), owen.baker@harmonygames.co (132), marcus.bennett@harmonygames.co (126), douglas@harmonygames.co (110)

GCAL  own=['vincent.parker@harmonygames.co'] shared=[] events=446 (distinct ical_uid 157, cancelled 52)
  last event before clock=2025-09-29T16:30:00Z  next after clock=2025-10-01T16:00:00Z
  by month: 2023-09:5 2023-10:8 2023-11:12 2023-12:7 2024-01:4 2024-02:1 2024-03:2 2024-04:13 2024-05:12 2024-06:22 2024-07:26 2024-08:27 2024-09:48 2024-10:33 2024-11:31 2024-12:40 2025-01:40 2025-02:22 2025-03:4 2025-04:17 2025-05:30 2025-06:17 2025-07:12 2025-08:7 2025-09:5 2025-10:1

DRIVE  owned=190 {'application/json': 90, 'application/vnd.google-apps.spreadsheet': 48, 'application/vnd.google-apps.document': 23, 'folder': 15, 'text/plain': 7, 'application/pdf': 4, 'application/vnd.google-apps.presentation': 2, 'text/csv': 1}
  shared-with=141 {'application/vnd.google-apps.document': 50, 'application/vnd.google-apps.spreadsheet': 32, 'text/plain': 27, 'application/json': 21, 'application/vnd.google-apps.presentation': 5, 'application/pdf': 4, 'text/csv': 2}
  shared by owner: {'Resource: -6481757892984311338': 100, 'leonard.hayes@harmonygames.co': 27, 'robert@harmonygames.co': 7, 'Resource: 7240535625619857401': 5, 'julia.lawson@harmonygames.co': 1, 'calvin.price@harmonygames.co': 1}
  native visible: {'gdocs': 73, 'gsheets': 80, 'gslides': 7}  last modified visible=2025-09-30T16:30:39Z
  UNVERIFIED (domain/anyone, not owned/shared)=85 {'application/vnd.google-apps.document': 32, 'application/vnd.google-apps.spreadsheet': 25, 'application/json': 11, 'application/pdf': 10, 'application/vnd.google-apps.presentation': 7}

UNSCOPED (always visible): contacts, github, trello, linear, snowflake, confluence

LAST ACTIVITY (days before clock): slack_persona_post=2025-09-30 (1d), slack_visible_channels=2025-10-01 (0d), gmail=2025-09-30 (1d), gcal_last_event_before_clock=2025-09-29 (2d), drive_last_modified_visible=2025-09-30 (1d)
```

Identity (`entity.py resolve "Vincent Parker"`): Slack `EMPLOYEE_0012_SLACK_ID`; Gmail mailbox `vincent.parker@harmonygames.co`
(thread-file alias `vincent@`, hazard I03: search both); GCal own calendar; Drive root `d_65c76e0b87aa7e9b84d1df`
(190 owned items); Linear `usr_65c76e0b87aa7e9b` (creator of 926 issues: ENG 792, ZOM 121; 112 ZOM since Jul 2025);
GitHub `EMPLOYEE_0012_GITHUB_USERNAME` (Jenkins shows his commits as `43593629+vincent.parker`, e.g. `#builds`
Match3D Android #1947/#1948/#1987); Trello `864e381ee6c844b2a3a7eaf8`; Confluence `user_EMPLOYEE_0012`; Contacts
`65c76e0b87aa7e9b84d1df22` (job "Game Systems Engineer"). Status at clock: active through 2025-09-30 (KB `activity.json`).

Reach on the records the recommended storyline needs (`persona_view.py can-see`, all YES):

| Record | Result |
|---|---|
| `slack C05433XK267/1759263189.219529` (Android Submission #135) | YES — public `#builds`, Vincent a member |
| `slack C08R27X0EAH/1758546048.524829` (Vincent's re-test report) | YES — private `#zombie-bugs`, member |
| `slack C0880U9751A/1758643365.607149` (Arthur's required-versions post) | YES — private `#zombie-match3d`, member |
| `gsheets f_74d23fd3ed7290dccc5fc1` "QA Test Template" | YES — Vincent owns it |
| `gsheets f_d224d9f6fcd6045faeee22` "ZM3 - Event and League Bots" | YES — Vincent owns it |
| `confluence page_qa_runbook`, `linear ZOM-559` | YES — unscoped services |

What he owns that matters: the Confluence **Release Checklist & Store Submission** (`page_release_checklist`, "Owner:
Vincent Parker (QA)", v1 2025-07-26) and **Customer Support Playbook** (`page_support_playbook`, v1 2025-05-24); the
**QA Regression Runbook** (`page_qa_runbook`, author Arthur, v2 2025-08-04) says "Owned by QA (Vincent Parker)". His
Drive holds a precedent release-issue register, "Baklava Issues" (`f_676a9d5f8a1597e5ec07db`, a Linear export with a
Chronology column, Sep 2024). Gaps: no TestFlight mail in his mailbox (0 visible hits), a thin Sept calendar (5
events), and no access to `#executives` (`C07C2866011` is not in his channels).

---

## 3 · Fit (rule 2)

- **Business function — Engineering & Live-Ops** ("engineering delivery, releases, incidents and live game operations",
  `Evals/references/rules/task_categories.md`): a store-release gate for the live Zombie Match 3D build is release work
  on a live game.
- **Competency — Engineering Ops** ("Epic & task management, tooling support"; expected outputs "Linear tickets, GitHub
  issues/PRs, database entries", `Taxonomy_V2_Step_Map.md` screen 6; `/prompt` names "tickets/PRs/release ops"):
  the deliverable is ticket management on a release ticket (blocker sub-issues, a filed bug, reuse of existing
  tickets) plus a register built from the CI build tooling.
- **Task skill — Analysis and synthesis** ("combine information from multiple sources and … reconcile, or diagnose to
  reach findings"): each register verdict reconciles Linear, GitHub, Jenkins `#builds` change lists, QA re-tests and
  deploy state; the release call is a synthesis, not a lookup.
- **Role** — Game Systems Engineer who files most ZOM live bugs, runs the QA regression and owns the release
  checklist: the persona would plausibly own this work, and the base shows it (Vincent's Crashlytics canvas post
  `C08R27X0EAH/1758312927.981069`; his re-test reports `C08R27X0EAH/1758546048.524829`, `…/1758547742.461489`).

---

## 4 · Storylines

### 4.1 A — Zombie Match 3D store release gate for the Sep 30 submission builds (recommended)

**Situation at the clock (verified).** The ZM3D team cuts store submissions from `main` through Jenkins jobs posted to
`#builds` (`C05433XK267`): Android Submission #127 and iOS Submission #40 on Sep 22 (`1758544783.817259`,
`1758544698.778509`), whose versions Arthur asked Douglas to set as the required versions ("Android: 0.3.127 | iOS: 0.3.40",
`C0880U9751A/1758643365.607149`, "Done!" in reply); Leonard released iOS 0.3.49 on Sep 29 (`C0880U9751A/1759182908.627389`); Leonard
blocked an earlier candidate over a level-30 soft-lock ("Submission blocker", "please don't release it on Android
either", `C08R27X0EAH/1758485492.586459`, `…/1758486809.397569`). The newest candidates are **iOS Submission #50**
(job start `1759257812.041449` 18:43:32Z, success post `1759259749.259909` 19:15Z) and **Android Submission #135**
(job start `1759257934.076209` 18:45:34Z, success post `1759263189.219529` 20:13Z, with a 36-line change list). No
change-triggered build ran between 18:37:53Z and 21:21:06Z, so both candidates hold one `main` snapshot. Changes
landed after the cut: direct commits in Android #2027 (start `1759267266.044859` 21:21Z, success `1759267655.279269`)
and #2028 "Fix season pass main screen instance from join popup" (start `1759268201.182309` 21:36Z, success
`1759268589.049939` 21:43Z); every match3d PR merged on Sep 30 (#469–#475) merged before 18:43Z (merged_at
01:50Z–16:09Z, `github data.json /pull_requests`). The release is Friday (runbook: "In practice Friday is the usual
release day"), so Friday Oct 3 is the natural deadline.

**Rules already in the base, owned by Vincent's QA role** (incorporated authorities; base Confluence loads):
`page_release_checklist` ("Do not submit a build until every box below is ticked and QA has signed off"; "When any
check fails, block the release, file the bug with device / OS / source build"); `page_qa_runbook` ("A failure in any
UPDATE column blocks the release - fresh-install-only regressions do not pass the gate"; "QA posts the completed matrix
in … #zombie-bugs (ZM3D) and links it from the release ticket"); `page_cicd_pipeline` (backend deploy is "Run by hand
… CI stops here": merged is not deployed).

**The work for Vincent on Oct 1.** Run the gate on the two candidates: decide, for every defect in scope, whether its
fix is in the candidate, verified and live; decide what blocks; manage the release ticket's blockers in Linear (reuse
existing tickets, file the bug the matrix failure requires); keep the register in a Vincent-owned sheet; post the
sign-off where the runbook says.

**Services.** Natural, load-bearing: Slack (`#builds`, `#zombie-bugs` `C08R27X0EAH`, `#zombie-match3d`, `#zombie-prs`
`C093LEZGF6J`, the "Bug Checklist" canvas channel `CF4EDAF93359` Sep 4–30, the "Crasyltyics Bugs" canvas
`CA661879E3ED`, DMs), Linear (team ZOM: 25 open Bug/Regression issues, 7 Bug issues completed since Android #127;
project "Zombie Match 3D" `dbab77c7-…`), GitHub (`match3d` 477 PRs, trunk on `main`, branch names carry keys such as
`Samuel/ZOM-498-536`), Confluence (four base pages above), Sheets (Vincent's "QA Test Template" with Bug List / Daily
Commit-Feature Tests tabs), Gmail (Crashlytics "Trending stability issues" digests reach his mailbox monthly, 12 in Sep
2025). Injection lifts GCal (release go/no-go event), Trello (ZM release card), Docs/Drive (tester notes and evidence
folder), Contacts (external tester alias) and Gmail (tester/partner mail) to carry weight: 11 services, 10 injected
(Confluence is never injected, learnings §26).

**Hardness opportunities (distinct v2 trap types, each its own fact; detail in §6).** T1 done across services, twice
(a Done ticket whose fix is a post-cut commit; a client fix in the build whose server half is merged but deployed only
to dev); T2 a re-test correction in another channel; T5 the runbook's update-path rule against a "regression green"
summary; T6 a symptom-named report that is an existing, differently titled ticket; T7 in-scope defects outside the
Bug-label view; T9 a defect verified fixed on the candidate in a record away from its open ticket.

**Hazards in scope (known-data-issue cards, synthcut).** SC-8 (ZOM-475 glass crash fixed or not), SC-15 (ZOM-521 VFX
checklist), SC-16 (Linear status vs shipped: ZOM-563/564, ZOM-513/514), SC-18 (PR #477 open/closed), SC-19 (telemetry
`app_version` 0.1.534/0.1.601 vs Slack 0.3.x builds — measured: CLIENT_ERROR_EVENTS ZM rows carry only 0.1.30/0.1.37/
0.1.534/0.1.601), SC-30 (ZOM-457 Done with open child ZOM-458), SC-37 (crash-by-level comment), SC-38 (Season Pass ship
date; avoid ZOM-529), SC-56 (commit-title case), SC-67 (build heading vs change list), SC-68 (Boss Arena prod date),
SC-70 (Slack timezones), SC-71 (ZOM-471 priority). Dispositions in §5.4. Coherence hazards touched: S03 (label
vocabulary), L03/L06 (state lifecycle), T04 (completion vs merge), R04 (Slack Google links), R06/R07 (GitHub-app
mirrors), R08 (invites vs GCal), I03 (mailbox alias), I08 (GitHub token logins vs mirrored real logins).

**Volume.** Honest ≈ 300 necessary calls with a ~50-defect scope (§7) — below the local 500 floor, far above the
platform's 100.

### 4.2 B — Domino Delights live-ops scheduler reliability follow-up (Jun–Sep 2025)

Anchors (verified): `#live-incidents` `C080X4GTZ0E` (2025 monthly files Jul 114 KB, Aug 123 KB, Sep 8 KB; Vincent's
"events are not active in prod builds" `messages/C080X4GTZ0E/2025-06.json /38`); LIVE_EVENT_PERFORMANCE 529 runs with
48 DD `degraded` rows (17 in the May 10–16 crash window, 31 scheduler-outage rows EVT-0342…EVT-0382, Jul 7–25) and one
`failed` (EVT-0024); ENG-1972 Canceled 2025-05-05, ENG-2275 Todo (compensation dashboard), ENG-2277 Bugs (negative
lives), ENG-2366 Todo (DD maintenance build); `page_live_ops_engine` v1 with Arthur/Douglas remediation comments
2025-07-28; `page_liveops_calendar` v3 (2025-09-29); `page_support_playbook` (Vincent); `liveops-dashboard-buddy#1–#3`
(merged Aug 25–26); `game-of-dominoes-backend#79` (open, opened 2025-09-10). Engineering Ops angle: remediation epic
status and follow-up tickets; Analysis angle: which runs were affected and what is still unremediated.
**Against it:** SC-31 forbids grading outage end dates or affected events except from the degraded rows (the core of
the analysis), SC-47 (Weekly Quests status), SC-52 (backend #79 open but merged), SC-53 (one player token for two
players), SC-62 (reward import hourly vs 5 min); DD is in maintenance mode, so the work is retrospective and Douglas or
Arthur, not Vincent, own remediation. Higher coherence risk, weaker role fit.

### 4.3 C — Zombie Match 3D event-bot parameters ready for backend ingestion (tooling support)

Anchors (verified): ZOM-545 "Ingest bot params from a spreadsheet" (Todo, created by Vincent 2025-09-15, assignee
Douglas, labels Improvement + "Hot Fix - Global Launch"; description "at start we can use that sheet, but I need
@douglas's help on the format"); Vincent's "ZM3 - Event and League Bots" (`f_d224d9f6fcd6045faeee22`, 15 tabs: Boss
Arena, Plague Race, Axe Arena, Streak Fever, River Rush, nine league tiers, Bot Score Simulator; modified 2025-09-18)
and its DD twin (`f_23dc18d9d6ca57fe86fadd`); ZM Plague Race runs EVT-0403…EVT-0514 (five `degraded` for ZOM-459, Aug
3–27); `match3d-backend#24–#35` (leaderboard/endless weekly, last activity Aug 2025). Strong "tooling support" fit.
**Against it:** the facts are numeric bot-tier parameters (UGT risk on every number, few cross-service per-record
surfaces: one sheet read returns a whole tab), hazards SC-58 (monster roster/boss rules) and SC-68 (Boss Arena on prod
before its code), and honest volume well under 200.

### 4.4 Comparison and recommendation

| | A — ZM3D release gate | B — DD scheduler follow-up | C — ZM3D bot-param ingestion |
|---|---|---|---|
| Fit (function / competency / skill / role) | 5 / 5 (release ops, tickets) / 5 / owns checklist + runbook | 5 / 4 (retrospective) / 5 / secondary owner | 5 / 5 (tooling) / 4 (mostly numeric checks) / owns the sheet |
| Natural services | 6–7, injection to 11 | 9–10 | 6 |
| v2 trap types available | 1 (×2), 2, 5, 6, 7, 9 | 1, 2, 4 | 5, 8 |
| Consequence of a miss (for `/hardness` 5) | a blocker ships | a gap in a retrospective | a wrong parameter row |
| Known-issue cards to settle | many, but avoidable by scope rule | SC-31 sits on the core fact | SC-58, SC-68 |
| Honest volume | ≈ 300 | ≈ 250 | < 200 |

**Recommendation: A.** It is the persona's own job on his actual today, its rules already live in base records he
owns, the hard decisions are judgments that survive complete retrieval (build cut-off, deploy state, the update-path
rule, aliasing, scope), and a miss changes the central release result. Its hazards are dense but discrete: each is a
named ticket or field that a scope rule or a dated settling record can keep out (§5.4).

---

## 5 · UGT plan (rule 1) — storyline A

### 5.1 Rules every decision needs, homed in incorporated records

| Decision | Rule it needs | Home (planned) | Census / proof needed |
|---|---|---|---|
| Scope of the gate | which defects count: every player-facing defect reported against a submission build since the last shipped versions, whatever its label, state or team; earlier defects only if re-reported | a seeded scope note in the release ticket's history or a Vincent-owned sheet tab (hidden authority, not the prompt) | full ZOM + ENG census for defects reported Sep 22–30 (Linear, `#zombie-bugs`, `#zombie-match3d`, both canvases, DMs) so the truth set is complete; no completeness claim without it (learnings §23) |
| "In the candidate" | a submission contains `main` as of its job start; its change list is the record; later commits go to the next submission | Arthur's dated build note (Gmail or DM, hidden authority) + the base `#builds` posts; decoy: early-September submissions built from `release/1.3.24_HotFix` (`#builds` Submission #107/#108/#112/#114), a time-superseded version, not a contradiction | base check: no change-triggered build between Arthur's 18:37:50Z commit (`#builds` Android #2026 `1759257470.890689`, iOS Internal #1757) and #2027 at 21:21:06Z, so iOS #50 (18:43:32Z) and Android #135 (18:45:34Z) hold one snapshot (verified) |
| "Live" for a server-dependent fix | merged ≠ deployed; prod needs the manual deploy | base `page_cicd_pipeline` + a seeded deploy record | the seeded server change must not contradict any base deploy message (census `#engineering-bots`, `#zombie-ops`, Douglas's DMs) |
| "Fixed" | QA (Vincent or the contract tester) re-test pass on the candidate or later | base runbook ("Reproduce the trigger, confirm the fix holds") + Vincent's QA sheet convention | every dev "fixed" claim in scope has a dated QA outcome or is explicitly "not re-tested" |
| Blocker vs known issue | crash, progression/save loss, purchase failure, soft-lock block; others ship as known issues | base runbook recurring classes + a seeded severity note from Leonard (precedent: his "Submission blocker" call, Sep 21) | apply the rule to every in-scope defect; no defect satisfies two classes (learnings §21) |
| Duplicate vs new defect | one ticket per defect; reuse and link the existing one | base checklist "file the bug … and link it" + ZOM's `Duplicate` state (7 issues) | the alias pair shares device, repro and build history in persona-visible records |
| Update-path failure | any failed UPDATE column blocks; file the bug with device / OS / source build | base runbook + checklist (verbatim, above) | N-1 and N-2 for each platform settled by a dated record (open fork: is Android N-1 0.3.127 or a later submission? → seed a release-log entry, learnings §58) |

### 5.2 Two-reading tests to run at S8 (each resolved by a record, else both accepted)

1. Merge time vs change list vs Linear completion time for "in the candidate" (T04 hazard) → the build rule decides;
   base timestamps agree for Sep 30.
2. Android vs iOS candidate → one snapshot (above); the register may record them together or apart (both accepted).
3. Dev "fixed" vs a later QA re-test → newer QA result on the candidate wins (dated, other channel).
4. Merged server PR vs deploy note → the deploy note wins (CI/CD page defines it).
5. Fresh-install green vs update-from-N-2 failure → the runbook rule decides.
6. New report vs existing ticket → identity evidence decides; accept either "link existing" representation (sub-issue
   or relation) if the platform's Linear tools can express both (verify in the pre-check).
7. Label-defined vs rule-defined scope → the scope rule decides; the register's volume follows it.
8. Verdict vocabulary, column layout, date formats → any equivalent wording accepted (learnings §8).

### 5.3 Boundaries the rubric accepts in full
Register shape and labels; whether the sign-off is a channel post or a reply in the runbook's channel only if the
prompt does not fix it (learnings §5: a named destination is not loosened); PT/UTC dates written either way when the
day agrees; one register or one tab per platform.

### 5.4 Known-data-issue dispositions (learnings §51)

| Card | Disposition |
|---|---|
| SC-8 ZOM-475 | outside scope by rule (reported Aug 14, not re-reported against a submission since 0.3.127); never graded |
| SC-15 ZOM-521, SC-38 Season Pass/ZOM-529, SC-68 Boss Arena, SC-71 ZOM-471 | not defects in scope; never graded |
| SC-16 ZOM-563 / ZOM-564 | both reported after Android #127 (Sep 23/24), so inside the date window: read the confirming DMs and builds at S1 and either seed nothing that contradicts them and grade their verdicts from the shipped evidence, or carve them out by a dated scope note; never grade Linear state as proof |
| SC-30 ZOM-457 → ZOM-458 | each child on its own state |
| SC-19, SC-37 | Snowflake app versions and crash-by-level never used; Snowflake carries no deciding fact in A |
| SC-56, SC-67 | change lists read by content and order, never by exact-case title or the post heading |
| SC-70 | dates stated in PT with UTC where the day differs |

### 5.5 Chronology and the data horizon
Every seed lands before 2025-10-01T00:00Z (Sep 30, 5:00 PM PT) and after the base events it names (the Submission
#135 post is 20:13Z, so a seeded reaction to it fits in 20:13–23:59Z). Base records after the seed bound and visible to
the agent: `#builds` Android #2029 "Fix end popup" (`C05433XK267/1759297904.607829`, Oct 1 05:51Z) and its `#zombie-prs`
commit post (`C093LEZGF6J/1759297469.978559`): a post-cut change, so no seeded ticket may depend on "end popup" as
fixed or unfixed in the candidate. `#executives` traffic after 00:00Z is not visible to Vincent.

---

## 6 · Hardness plan (rule 4) — storyline A

### 6.1 Load-bearing channels (independent, each its own fact, each flipping weight-5 multi-source rows)

| Ch | v2 trap type (guide Part 3) | Convincing wrong source (who · when · authority) | Record that beats it | Findability | Survives complete retrieval because | Rows it flips (planned) |
|---|---|---|---|---|---|---|
| C1 | 1 · proving "done" across services | the ticket's Done state and the developer's "fixed" (Linear, Sep 30 after 21:43Z) | the base `#builds` Android #2028 post after the Submission #135 cut (job 21:36Z vs 18:45Z) + the build rule | tier 2: one channel of ~1,100 bot posts in Sep | the agent must line up a commit time against a job start: Linear and GitHub both say done | register verdict + release-ticket blocker (10/84) |
| C2 | 1 · proving "done" across services | client PR merged and in the build; server PR merged (GitHub, before the cut) | a deploy note showing the server change only on dev + `page_cicd_pipeline` "Run by hand" | tier 3: a DM / ops channel, not on the ticket | "merged" is literally true; only the deploy meaning decides | register verdict + blocker (10/84) |
| C3 | 2 · a correction somewhere else | the developer's "fixed" in a `#zombie-bugs` thread and the Done state (Sep 26) | a later re-test on the candidate reproducing it, in a `#zombie-match3d` thread reply (Sep 30) — other channel, other thread, same item and tester | tier 2: thread reply in another channel | needs the newer-on-the-candidate comparison across channels | register verdict + blocker (10/84) |
| C4 | 5 · a rule hidden in the data | the matrix's fresh-install column green and a teammate's "regression green, good to ship" summary | the tester's update-from-N-2 save/progression FAIL + the runbook's UPDATE-column rule; follow-through: file the bug with device / OS / source build | tier 1 to find, tier 3 to apply | the rule must be applied against a summary every run reads | matrix verdict (5) + filed bug content (3) |
| C5 | 6 · different names for the same thing | a symptom-named report from support/leadership that reads as a new defect | the existing, differently titled ZOM ticket with the same device, repro and build history | tier 2 | mapping, not retrieval: both records are found | blocker is the existing ticket (5) + register reference (3) |
| C6 | 7 · items outside the obvious filter | the ZOM view filtered to the Bug label / open states | two in-scope defects with another label or state (or filed in ENG), brought in by the scope rule | tier 2 | the filter is the agent's own choice; the rule widens it | two inclusion verdicts (5 + 5) + volume (3) |
| C7 | 9 · work someone already did | the ticket still Todo in Linear | a QA verification on the candidate recorded on the fixing PR's review (GitHub, mirrored to `#zombie-prs`) | tier 3 | the open state is real; the completion lives elsewhere | register verdict (5) |

Load-bearing pair named for the guide's "1–2 traps that carry the difficulty": **C1/C2 (done across services) and C3
(correction elsewhere)**; C4–C7 add independent spread. Every channel keeps its own fact (no stacking), the largest
unit of discovery decides 15 % of the weight (C6) — well under half — and no correction sits in the superseded record's
container, an anchor's container or the delegation path (checked in §6.3).

### 6.2 What will not be relied on (guide Part 4; learnings §45–46, §52, §54)
Volume, routine writes, clean totals (no weight-5 aggregate at all), visible caveats, same-thread corrections, rules
in the prompt, keyword-findable wording (hidden texts say what happened in plain language, not "still repro" /
"reopen"), anything a subagent brief would sweep by default (corrections sit off the ticket comments that a
brute-force `linear_list_comments` pass reads), base-status-vs-base-status disagreements (only dated human claims
overturn a stale state).

### 6.3 Part 7 self-checks, run by `tools/hardness_v2_check.py`

Run on a pre-scenario sketch of the trap geometry (`research/00_sketch_manifest.json`, `research/00_sketch_surface.json`;
planned ids, so containers are declared explicitly):

```text
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      2 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 6 requirements: {'R1': ['R_DONE_BUILD'], 'R2': ['R_DONE_SERVER'], 'R3': ['R_CORRECTION'], 'R4': ['R_UPDATE_RULE'], 'R5': ['R_ALIAS'], 'R7': ['R_COMPLETION']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   7 of 7 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     0 weight-5 total(s); 0 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  SKIP       RULE_IN_PROMPT  no prompt (04_Prompt.txt) yet  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

Positive control (the check is live): moving C3's correction into the superseded `#zombie-bugs` thread
(`research/00_sketch_manifest_control.json`) gives `FLAG SAME_PLACE … 1 flagged`. Guide Part 7 answered in words:
**done check** — C1/C2: Linear Done + merged PR say done; `#builds` and the deploy note show the missing piece.
**Same-place** — C3's correction is in another channel's thread, C7's on a PR review: neither in the original's
container. **Filter** — the Bug-label view misses C6's two members. **Input** — no total is graded; trap 8 is not used.
**Decision flip** — every channel flips at least one weight-5 multi-source row. `/create-scenario` S5b re-runs the
tool on the real draft manifest and surface; injection re-runs it on the SQL.

### 6.4 Planned surface and policy scores (UNCALIBRATED; rule 5)

The planned surface (22 slots, total weight 84; 11 weight-5 slots; weights by kind of work, never raised; ≤ 5 ordinary
samples + one volume slot; exceptions are the trap members their authorities single out) was scored with
`research/geometry_mc.py`, which grades simulated six-run baselines with the bundle's own gate math
(`difficulty_stats._gates`, easy, long-horizon). Output (verbatim, 20,000 draws per scale):

```text
WHOLE POLICIES (deterministic, no slips)
   20.2%  P0 lazy: Linear states + labels only
   29.8%  P1 Linear + GitHub merges (no #builds, no deploy check, no re-tests)
   35.7%  P2 + #builds change lists
   51.2%  P3 + every ticket comment and PR review (no DMs, no runbook rule)
   90.5%  P4 everything retrieved, house rule not applied
   84.5%  P5 everything retrieved, obvious filter kept
  100.0%  P6 perfect

SINGLE MISSES (everything else right)
   88.1%  miss C1
   88.1%  miss C2
   88.1%  miss C3
   90.5%  miss C4
   90.5%  miss C5
   84.5%  miss C6  (both outside-filter members)
   94.0%  miss C7
   90.5%  miss one outside-filter member only

SIX-RUN BASELINES (20000 draws per scale; gate math = difficulty_stats._gates, easy, long-horizon)
  scale = multiplier on every design miss rate (1.0 = the design rates; <1 = a stronger Opus)
  scale 1.00: E[avg] 60.9% (p10-p90 50.4%-71.2%)  E[SD] 0.174  P(avg<90%) 1.00  P(<5 full) 1.00  P(SD band) 0.84  P(patterns) 1.00  P(all four) 0.84  E[full passes] 0.17
  scale 0.75: E[avg] 69.4% (p10-p90 59.3%-79.4%)  E[SD] 0.166  P(avg<90%) 1.00  P(<5 full) 1.00  P(SD band) 0.81  P(patterns) 1.00  P(all four) 0.81  E[full passes] 0.38
  scale 0.50: E[avg] 78.2% (p10-p90 69.0%-86.9%)  E[SD] 0.147  P(avg<90%) 0.96  P(<5 full) 1.00  P(SD band) 0.70  P(patterns) 0.99  P(all four) 0.69  E[full passes] 0.81
  scale 0.35: E[avg] 83.6% (p10-p90 75.4%-91.3%)  E[SD] 0.129  P(avg<90%) 0.85  P(<5 full) 1.00  P(SD band) 0.55  P(patterns) 0.98  P(all four) 0.54  E[full passes] 1.25
  scale 0.25: E[avg] 87.4% (p10-p90 80.2%-93.8%)  E[SD] 0.112  P(avg<90%) 0.66  P(<5 full) 0.99  P(SD band) 0.41  P(patterns) 0.97  P(all four) 0.38  E[full passes] 1.68
```

Design miss rates (scale 1.0): C1 0.45, C2 0.60, C3 0.50, C4 0.40, C5 0.45, C6 0.50 (members ρ 0.8), C7 0.50; slips
0.03–0.06; a per-run thoroughness latent correlates the channels. These are assumptions: the Opus 5.5 ledger holds Beta(1,2) for A7 and
A14–A17 from one robert-vendor-schedule trial each, Beta(1.86,2) for the A1 family (7 trials), and nothing for A8, A11,
A24 or A25 (`hardness_ledger.py priors --model claude-opus-5-5`); and three earlier pre-checks in this workspace met
every requirement (learnings §27, §45, §52).

Reading: the goal's bars (E[avg] ≤ 82 %, P(all gates) ≥ 0.5) hold down to a miss-rate scale of about 0.35 (mean miss
≈ 0.17); at the design rates the model gives 60.9 % with P(all four) 0.84. The binding risk is a strong Opus (scale
≤ 0.25): every single miss leaves a run at 84–94 %, so the cap needs at least two misses per run on average.
The whole-policy table also shows where difficulty lives: retrieval policies P0–P3 score 20–51 %, but a run that
retrieves everything and applies one rule wrong still reaches 84–91 %, so the judgment channels (C2, C4, C5, C6) must
stay hard after complete retrieval. `/create-scenario` replaces this with `hardness_forecast.py forecast --design` on
the real `01_Gradable_Surface.json`, pre-registered (S9b).

### 6.5 Spread (rule 5)
Graded findability (tiers in §6.1) and different deciding services per channel make runs fail different subsets:
P(patterns) ≈ 1.0 and P(SD band) 0.70–0.84 at scales 0.5–1.0. No row is predicted to fail all six runs at ≥ 5 % (the
highest is C2's pair at 4.2 % at scale 1.0); C2 is the design's deepest channel and the first to soften if the
pre-check shows a universal miss.

### 6.6 Difficulty target (the user's instruction)
The assignment stays **Easy** (cap < 90 %, design target ≤ 82 %); the mode is never switched. Per the instruction to
aim for Medium or Hard, the design aims at **E[avg] 62–77 %** (between the Hard and Medium design targets): the margin
to the 90 % cap absorbs a much stronger Opus than modelled, while the floor keeps spread and all-fail workload in hand.

---

## 7 · Volume plan (honest, never padded)

Scope estimate: 25 open ZOM Bug/Regression issues + 7 Bug issues completed since Android #127 = 32 base candidates
(minus the carved-out hazard tickets) + ~20 seeded defects from Vincent's and the contract tester's passes on
submissions #129–#135 / iOS #46–#50 ≈ 50.

| Phase | Services | Calls (est.) | Why each is necessary |
|---|---|---|---|
| Anchors and rules | Linear (release ticket + comments), Slack (the ask), Confluence (checklist, runbook, CI/CD, support playbook; comments) | ~12 | each page or ticket carries a different rule |
| Hidden authorities | Gmail (build rule, tester mail), Sheets (tester matrix, QA template tabs), GCal (go/no-go), Trello (release card), Docs/Drive (tester notes, evidence), Contacts (tester alias) | ~22 | one authority each, no bulk path |
| Enumeration | Linear list pages; `#builds` Sep 22–30; `#zombie-bugs`, `#zombie-match3d`, both canvases, DMs | ~33 | the scope rule needs every report source |
| Per-record | ~50 × (`linear_get_issue` + `linear_list_comments`) + ~30 fixed defects × (PR search + PR read + reviews) | ~190 | comments and reviews have no bulk call (`Ask_Carriers.md` §3, §6b) |
| Reconciliation | GitHub commits/compare for cut boundaries | ~4 | |
| Writes + read-backs | Sheets (create + values), Linear (bug + ~8 parent links + comment), Slack (sign-off) | ~25 | each write is requested |
| **Total** | 11 services | **≈ 290–310** | ≥ 500 is not reachable without padding |

Every surface and its shortcut audit are re-derived at S2/S7; Slack thread replies are search-sweepable and are not
counted as per-record volume.

---

## 8 · Writes and ownership (rule 6)

| Write | Trigger the persona owns | Write access |
|---|---|---|
| Register (Google Sheet) | the runbook's sign-off is Vincent's gate | Vincent-owned: either a seeded sheet with `owner_email` Vincent in every Drive/Sheets row (learnings §31) or created at run time by `gsheets_create_spreadsheet` in his Drive; never shared-to-him |
| Release ticket blockers (parent links), a filed bug, a sign-off comment | runbook "links it from the release ticket"; checklist "file the bug with device / OS / source build" | Linear is unscoped; ZOM team writes verified in the pre-check |
| Sign-off post in `#zombie-bugs` | runbook "QA posts the completed matrix in … #zombie-bugs (ZM3D)" | Vincent is a member (YES above) |

---

## 9 · Risks and open items

1. A strong Opus that checks `#builds`, deploy state and every re-test (scale ≤ 0.25) could average ≥ 87 % (§6.4):
   judgment channels must stay hard after full retrieval; verify with the pre-check before the baseline.
2. Base density: SC-16 tickets sit inside the date window; S1 must read their DMs before seeding anything near them.
3. Android N-1/N-2 identity is not established by any base record found so far: settle it with one dated record.
4. Seeded GitHub review comments need INT-01 mirrors in `#zombie-prs` with real-login style (I08).
5. Linear's tools may not express both "sub-issue" and "relation" links; the acceptance rule follows what
   `linear_update_issue` (`parentId`, `links`) can write.
6. Ledger priors for A24/A25 are empty (Beta(1,1)): every forecast stays UNCALIBRATED until the pre-check.

---

## 10 · Decisions needed from you

| # | Decision | Recommendation |
|---|---|---|
| D1 | Storyline | **A — Zombie Match 3D store release gate for the Sep 30 submission builds** (§4.4) |
| D2 | Volume exception (GEN_EXECUTION §3a; ≥ 500 necessary calls not reachable without padding) | **Yes**: `volume_exception {call_budget_floor: 280, per_record_floor: 170}` with your confirmation recorded as `requester_confirmation`; every other extreme target stays (≥ 10 services, ≥ 120 rows, ≥ 12 traps, …) |
| D3 | Difficulty target (mode stays Easy) | design E[avg] **62–77 %** per your instruction (§6.6) |
| D4 | Review waiver | No `REDTEAM_*` variables are set in this shell, so `redteam_review.py --dual` cannot run. Either set `REDTEAM_*` (preferred), or approve a recorded `RED TEAM FALLBACK:` using the session's independent GPT `redteam` and `oracle` subagents on the design (named in §13 of the design and kept in every Unresolved line until covered, learnings §44) |

Next step: take D1–D4, then run **`/create-scenario`** in this session.
