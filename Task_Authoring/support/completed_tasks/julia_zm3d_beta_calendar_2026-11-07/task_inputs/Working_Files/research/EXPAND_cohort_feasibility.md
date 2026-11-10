# EXPAND: Cohort Feasibility (honest live-ops cohort, ≥40 members, 150+ calls)

Clock: 2025-10-01 00:00 PT (07:00Z) · Universe: synth-cut · Persona: Julia Lawson (PM)
Seed bound: `2025-10-01T00:00:00Z`
Sources read (read-only): `research/R_B_spine_facts.md`, `S1_liveops_census.md`, `S1b_liveops_followup.md`,
`S6_art_readiness.md`, `H2_faultthreads_retest.md`, `H3_reviewblocker_companion_audit.md`,
`references/known_data_issues/synthcut.md`, and fresh queries over `raw/linear.json` (553 ZOM issues, 99 non-Done),
`raw/github.json` (512 match3d PRs, 210 merged 2025-07-01..09-30), `raw/slack_*.json`, `raw/gh_prs.json`.
Filter used throughout: `created_at ≤ 2025-10-01T00:00:00Z` (verified: **0** open ZOM issues created after the bound).

## 1. Open live-ops ZOM issues at the clock

Universe: ZOM team = 553 issues; **99** are not in `Done/Canceled/Duplicate` (Todo 45, Backlog 34, In Progress 15,
In Validation 3, Regression 2). A title+description screen for `live.?ops|queue manager|leaderboard|league|season pass|plague|endless|collect & win|win & collect|daily gift|login|quest|trophy|zombie lane|event icon|panel` returns **29** candidates; hand-reading all 29 descriptions plus the 70 non-matching ones leaves **23** that bear on an in-scope beat's readiness or on live-ops infrastructure that gates a beat. Excluded and why: ZOM-62 "Zombie Ops #3 Spec (Dead Eye)" and ZOM-390 "Icon…Win Streak Event (axe arena)" (both explicitly the Axe-Arena/Win-Streak family), ZOM-520 + ZOM-560 (win-streak), ZOM-513/514/564/563 (item art / boosters / team lives — SC-16 tickets, no beat), ZOM-359/468 (generic device perf), ZOM-483/539/541/528 (lives, cards, shop), ZOM-548 (boss arena), ZOM-118/317/202/311 (shop/level-editor).

| identifier | state | assignee | title (verbatim) | the live-ops decision it bears on | multi-source? | SC-card risk |
|---|---|---|---|---|---|---|
| ZOM-78 | Backlog | Douglas | Event Calendar For Zombie Match 3D | **infra dependency for all beats**: description is empty; there is no calendar/scheduling backend, so every event window in Oct 6–Nov 2 is hand-set and every reset depends on Douglas's manual post-deploy job check (`C08R27X0EAH/1754669246.962529`) | **yes** — Slack reset-cron thread + Confluence `page_liveops_calendar` claims the calendar is the single source of truth | none, but record is evidence-thin (empty body) |
| ZOM-344 | Todo | Marcus Bennett | Quest UI box animation | **still-to-do for quests** (open/close box animation); the *control case*: no commit, PR, build line or Slack post anywhere | **no** (single-source; deliberately so) | none |
| ZOM-387 | Todo | Arthur Blake | Giant Analytics Ticket | **infra dependency for beats [Plague Race, quests]**: names `plague_race_start`, `quest_completion`, `quest_reward_redeem`, `liveops_reward_redeem` as un-instrumented; yet PR #319 is titled "ZOM-387" and merged 2025-07-19 | **yes** — PR #319 + Robert's `liveops_completion` complaint (`C0880U9751A/1758062399.419489`) | SC-16 shape (open ticket, merged PR) |
| ZOM-429 | Backlog | Douglas | Leaderboard next session doesn't start without killing the app | **known-issue, weekly leaderboard**: fix shipped (`#builds` #123) and then **reverted** (#129 "Revert …"); Slack QA re-tested "working fine" after the revert → only defensible status is "reverted, still open" | **yes** — Slack `1758546119.789009`/last reply + two `#builds` submissions | none |
| ZOM-432 | Todo | Calvin Price | Daily gift artwork needs to have the frame | **done-elsewhere (daily login)**: commit `f0bb8b48` "Fixing UI Elements on Daily Gift" → PR #471 body "updated Daily Gift sprite configuration" → Submission #135 "Fixing UI Elements on Daily Gift" | **yes** — commit + PR + `#builds` | none (the §5-A trap in R_B) |
| ZOM-442 | In Validation | Oliver Brooks | Analytics Instrumentation for Tropy Reward Redeem | **still-to-do for Trophy Path**: `trophy_reward_redeem` + super-properties stuck in validation, so trophy/lane reward telemetry is not in prod | **yes** — validation state vs ZOM-555 `Done` (09-30) on the same track | mild (In-Validation = "shipped but unvalidated") |
| ZOM-465 | In Progress | Marcus Bennett | Endless Mode Master VFX Ticket | **still-to-do for endless + all event icons**: every line is struck except "**Refill Timer ticking animation as well as colour change from 5 to 1**", with an unanswered inline question ("i've seen that the refil counter it's already animated do we still need to do that?"); its struck "Idle Icon Animation for all event icons" is contradicted by §2 #454/#456 (no Collect & Win icon) | **yes** — PRs #454/#456/#475 + no closing source | none |
| ZOM-471 | Todo | Samuel Turner | Add red dot icon for players not in Plague Race | **cancelled-in-Slack (Plague Race)**: the Aug 13 thread kills it ("i think it's annoying, it already has start button" · "yeah, we don't need it! cancel the ticket lol" · "I don't think we should do it") while Linear stays Todo | **yes** — 12-reply `#zombie-match3d` thread 1755108052 + Linear-bot post 1755108077 | **SC-71** (priority high vs Medium — do not grade priority) |
| ZOM-484 | Todo | Marcus Bennett | Info Screen Animations | **still-to-do for live-ops surface**: checklist `- [ ] Live-ops` unchecked while Season Pass, Collect & Win, Plague Race, Endless, Zombie Lane, Quest, Leaderboard are all `[X]`; PR #415 "Objects Effects Tutorial Screens" (merged 08-27) does not name live-ops | **weak** — Linear checklist only; PR #415 read is needed to see whether it covers it | none, but the "Live-ops" item is not a named beat (borderline) |
| ZOM-504 | Backlog | EMPLOYEE_0032 (Blake) | In endless mode, objects might stay persistent in the deck after match | **known-issue, endless**: reproducible per report ("happens in every attempt"), no fix source | **yes** — Sep 15–30 fault threads on endless | none |
| ZOM-517 | Backlog | EMPLOYEE_0032 (Blake) | Monster loses enrage during item refill in endless mode | **known-issue, endless**: high-priority ticket minted by the Linear bot in-thread (`1756938142`), never touched since | **yes** — `#zombie-bugs` 1756938116 thread | none |
| ZOM-521 | In Progress | Calvin Price | Master Ticket - VFX implementation | **state conflict for live-ops icons + tokens**: all six checklist items `[X]` (incl. "Live-ops icons appearing on the screen and animations" and "Tokens traveling to live-ops") while children ZOM-526/528 stay In Progress → parent cannot settle any beat | **yes** — #408 + child tickets | **SC-15** (do **not** grade "what is left on ZOM-521"; grade the children) |
| ZOM-526 | In Progress | *(unassigned)* | Tokens traveling to live-ops | **infra dependency for beats [Season Pass, Collect & Win]**: "Part of the queue manager. We will show that tokens earned from levels go to live-ops icons. We will implement this together with season passes and collect&win events" — no PR names it | **yes** — ZOM-521 tick + ZOM-543 + #408 | SC-15 (child of 521) |
| ZOM-534 | In Progress | Douglas | Quest points not resetting until app restart in production | **known-issue, quests rollover**: prod-only symptom; rollover code touched twice after filing (#builds #36 "sync quests end with client", #130) but no record says the symptom is fixed → honest verdict "unclear" | **yes** — Slack prod report + Linear bot + `#builds` | none |
| ZOM-542 | Regression | Samuel Turner | Update home screen and victory score screen for game modes | **partly-done, endless**: endless half delivered by PR #379 (08-14, "Update and fix UI for Endless Mode"); boss-arena half is out of scope; ticket still Regression | **yes** — PR #379 + ZOM-470 `Done` | none |
| ZOM-543 | In Progress | Calvin Price | Queue Manager | **infra dependency for every beat's panel**: "orchestrate panels and animations on the Main Menu… handle tutorials, level-end animations, claimed-reward animations, Live-Ops token animations, the order of opening Live-Ops panels". PRs #459/#465/#472 wire only level-end, daily gift, Season Pass, tutorial, **Collect & Win** → Plague Race, Zombie Lane, Endless, Quests panels are *not* in the queue | **yes** — 3 PRs + Julia's 09-02 note ("because we don't have a queue manager yet… that was one of the issues in last week's meetings") | none |
| ZOM-544 | In Progress | EMPLOYEE_0032 (Blake) | Implement Google Apple Login | **infra dependency for beats [Season Pass, quests, leaderboard/league, Zombie Lane]**: sign-in must persist SP rewards/progression, quest chest progression, weekly leaderboard contest, ZL progression; not live (ZOM-563 prod-env failures) | **yes** — Julia's 09-22 status ("he's working on Apple/Google login") + ZOM-563 | none |
| ZOM-546 | Todo | Owen Baker | Bug: refill algorithm spawns fewer items over time | **known-issue, shared board/endless**: refill decays (39, 38, 37…) — the same mechanic that breaks endless enrage (ZOM-517) and was re-opened by the `#zombie-bugs` Sep 3 thread | **yes** — Slack 1756937350 thread | none |
| ZOM-549 | In Validation | EMPLOYEE_0032 (Blake) | Add new fields to left_level and endless_left analytics events | **in-flight, endless analytics**: fields (endless_level, player_cpm, total_equipped_power, nuke_damage_total) merged in PR #451 ("Infinite/endless analytics") yet still In Validation → endless scoring telemetry unconfirmed | **yes** — PR #451 + Sep 16 thread ("Did you implement the endless instrumentation?") | none |
| ZOM-552 | In Progress | Oliver Brooks | Season Pass Analytics | **still-to-do, Season Pass**: `Season_pass_left`/`Season_pass_redeem` events; `#builds` #123 already carries "Sending SeasonPass_Redeem info to analytics" → partially shipped, ticket open | **yes** — `#builds` + `page_season_pass_spec` "events are tagged" | **SC-38** (never grade SP ship date or analytics status) |
| ZOM-556 | Todo | Calvin Price | When the daily gift is skipped, it doesn't reset to 0. | **known-issue, daily login**: missing a day leaves the progress bar on the old day; the streak logic is wrong at the clock, on a beat the PN sheet marks "Not Ready" | **yes** — ZOM-412 unlock `Done` + PRs #317/#328 | none |
| ZOM-565 | Todo | Calvin Price | Endless Horde Start Screen Vfx | **done-elsewhere (endless)**: commit `f7e971b0` "Endless Mode start screen VFX" authored **13:25Z**, 21 min *before* the 13:46Z ticket, has **no PR mapping**; in build #2023 | **yes** — commit + `#builds` 1759248192 | none |
| ZOM-566 | Todo | Owen Baker | Collect&Win Analytics | **in-flight, Collect & Win**: implementation sits in **open** PR #477 → the beat ships with no start/reward telemetry | **yes** — #477 + Confluence "not yet live" + PN row "Not Ready" | **SC-18** (never grade #477's open/closed state) |

### §1 count and verdict

- **23 in-scope, decision-bearing issues** (target ≥20 → **met**).
- Of those, **21 are solid** (each carries a readiness / hold / still-to-do / done-elsewhere / known-issue verdict that changes at least one beat's calendar row). **2 are borderline** and should be carried only with a caveat: **ZOM-484** (the unchecked item is literally "Live-ops", not a named beat) and **ZOM-78** (empty description; the decision "no scheduling backend" rests on Slack, not on the ticket).
- **20 of 23** are genuinely multi-source — the Linear state alone gives the wrong or an insufficient answer: 78, 387, 429, 432, 442, 465, 471, 504, 521, 526, 534, 542, 543, 544, 546, 549, 552, 556, 565, 566. Only **ZOM-344** (nothing anywhere), **ZOM-484** (Linear checklist only) and **ZOM-78** (empty body) rest on Linear alone; ZOM-78's *decision* still needs Slack if it is kept.
- **Zero** members resolve to "nothing outstanding": every row terminates in done-elsewhere, cancelled, reverted, still-to-do, in-flight or known-issue.
- **Answer to "≥40 from issues alone": no.** 23 is the honest ceiling on the issue side; the remaining ~47 open ZOM issues are core-game, shop, art or boss-arena work with no beat consequence.

## 2. Merged match3d live-ops PRs (2025-07-01 .. 2025-09-30)

Population: **210** match3d PRs merged in the window; a beat/infra screen (title + head_ref + body) returns **104**, of which **40** are genuinely in-scope after reading body, commit titles and review rows. The spine's 22 (`353 356 357 360 364 370 384 394 396 397 400 403 420 438 454 456 459 465 468 470 472 475`) is **not** the in-scope population: the July founding PRs (quests, daily login, Zombie Lane, endless core, plague-race UI) and the Sep 30 addressables PR are outside it and are exactly the ones that fix each beat's state.

Classes: **G** = the PR record itself carries a post-merge still-to-do / deploy / config / scope-gap fact that changes a beat's Oct 6–Nov 2 row; **ID** = read is needed to know which beat and what shipped, but leaves no outstanding decision; **CLEAN** = title+diff repeat each other, read adds nothing. `human text` = substantive human review/inline/conversation sentence (CodeRabbit and the `PERSON_6028` Linear bot excluded).

| pr | title (verbatim, truncated) | merged_at | beat | class · the decision the record carries | human text |
|---|---|---|---|---|---|
| #259 | …/quests | 2025-07-01 | quests | ID — quests client incl. chest/reward types; no gap named | 1 COMMENTED, no inline |
| #270 | …/quests | 2025-07-03 | quests | **G** — adds **daily and weekly quest reset countdown timers** + claimable warnings; fixes "broom quest not being tracked" → reset cadence is client-side, not only server | 1 COMMENTED |
| #296 | ZOM-370, ZOM-371, ZOM-372 | 2025-07-11 | Plague Race | ID — body empty; only the commit ("ZOM-370, ZOM-371, ZOM-372") and `Blake/plague_race_iPad` reveal the beat is Plague Race iPad UI | Linear bot only |
| #297 | Finishing Zombie Lane | 2025-07-11 | Zombie Lane / Trophy Path | **G** — ZL client complete incl. "server communication for fetching event data and claiming rewards"; **zero reviews**; backend `match3d-backend#10` still unmerged → client-done/server-open split | none |
| #303 | Samuel/zom 349 | 2025-07-16 | leaderboard + quests tooltips | **G (guard)** — the only unresolved `CHANGES_REQUESTED` in match3d sits here (bot, never dismissed); a beat-scoped blocker clause would wrongly hold leaderboard+quests. Reading it is how you *avoid* the false hold | **yes** — Arthur Blake inline ("I strongly think we should change this implementation…") |
| #306 | Endless levels | 2025-07-16 | Endless | ID — endless mode core lands | 1 COMMENTED |
| #308 | Adding "ExtraData" to RewardData… | 2025-07-16 | Zombie Lane | **G** — adds a **manual "Zombie Lane" debug option to refresh spreadsheet data from the server** → ZL rewards are sheet-driven; ships a warning dot on the ZL icon for unclaimed levels | 1 human conv (unrelated shadow note) |
| #315 | Endless spawn algo change | 2025-07-17 | Endless | ID — item-pool replacement; Arthur's inline reserves future "4-sided mega ice tile" work | **yes** — 4 inline (Arthur Blake ↔ dev) |
| #317 | …/daily login merge | 2025-07-18 | daily login / daily gift | **G** — daily gift + chest built on **`LiveOpsRewards`** (human review forces reuse, not new classes) + "DailyLogin Endpoint"; reward-type ownership decision | **yes** — Arthur Blake inline "Don't make new reward classes. We should reuse `LiveOpsRewards`" (×3) |
| #328 | …/daily login merge | 2025-07-22 | daily login | **G** — "**Change chapter unlock for daily gift**" → the daily-gift gate moves again; only this PR records the change | 1 APPROVED (empty) |
| #336 | Endless mode | 2025-08-01 | Endless (+ leaderboard) | **G** — "Endless Mode **live event** featuring **daily and weekly leaderboards**, milestone claiming" → the only record of the endless reset structure and its leaderboard coupling | **yes** — 2 inline (Arthur) |
| #338 | Fix zombie lane icon and Quests | 2025-07-25 | ZL icon + quests | ID — icon aspect fix | approval only |
| #353 #356 #357 #360 #364 #384 #405 #420 | endless UI / items / bar / level 3 / rotation / perf / polishes / bar .cs | 08-02…09-08 | Endless | **CLEAN** (8 PRs) — each repeats the title; none names a pending dependency | approvals only |
| #370 | Collect&Win Items | 2025-08-13 | Collect & Win | **G** — **art only** (baseball/ping-pong/bowling/potion props); C&W had items 6 weeks before it had a client → the beat's item set is a different deliverable from its UI | approval only |
| #382 | Samuel/eng 472 | 2025-08-15 | leaderboard (+shop/items/teams) | **G** — lock popups now "show **required level**" for **Leaderboard**; the unlock-level surface every beat's icon uses | CodeRabbit only |
| #394 | …/icon management system | 2025-08-21 | icons (all beats) | **G** — "**Locked Live Ops events** show an unlock message with required level; related buttons are disabled and visually grayed out" + event-icon grouping/replacement | approval + 7 CR inline |
| #396 | …/icon management system | 2025-08-22 | icons | ID — build-pipeline define ordering (Arthur inline) | **yes** (Arthur, build correctness) |
| #397 | …/icon management system | 2025-08-22 | icons | CLEAN — coin/heart icons, gray-icon-after-tutorial fix | approval |
| #400 | …/icon management system | 2025-08-26 | icons (Endless, Plague, Quests, ZL) | **G** — "Added gray scale and unlock text to all event icons from Main Menu" enumerates **Endless, Plague Race, Quests, Zombie Lane** only → Collect & Win and Season Pass absent from the unlock surface | approval only |
| #403 | …/icon management system | 2025-08-26 | icons (Endless) | CLEAN — gray-scale material, EndlessHorde_4 texture | approval + 2 CR |
| #405 | Samuel/zom 501 | 2025-08-26 | Endless | CLEAN — rocket active state, header gap (matches ZOM-501 `Done`) | 1 APPROVED |
| #408 | …/vfx implementation | 2025-09-11 | endgame + Endless VFX, tokens | **G** — commits: "EndlessReardScreen with Vfx and Sfx. **Needs more coding work!**"; this is the only PR that could carry ZOM-526's token-to-live-ops animation, and it never names it | 1 APPROVED (empty), 47 CR inline |
| #419 | …/hot fixes | 2025-09-09 | quests | **G** — commit "**change quest unlcok to level 15**" → the current unlock gate; contradicts ZOM-410 `Done` ("level 4 instead of 19") | **yes** — 5 inline (streak-reward validation removal) |
| #438 | Feature/season pass | 2025-09-15 | Season Pass | **G** — "full Season Pass (tokens, premium purchase, bonus bank, main screen, popups, VFX) and **LiveOps integration**", 259 files, **zero human review** (3 CodeRabbit COMMENTED, 73 CR inline) → shipped code with no human sign-off and analytics still open | **no** — CodeRabbit only |
| #447 | …/vfx fixes | 2025-09-17 | ZL + reward screens | **G** — fixes "Individual card rewards in **zombie lane** are not visible" and "reward screen … doesn't go away after opening the pack, needs another click" → post-merge state of the ZL reward flow | 1 human review + 4 CR |
| #454 | Marcus/animated icons | 2025-09-19 | icons (5 beats) | **G** — animations for **Quests, Season Pass, Endless, Zombie Lane, Plague Race** — **Collect & Win missing** | 1 APPROVED (Calvin Price) |
| #456 | …/animated icons | 2025-09-24 | icons (6 beats) | **G** — adds **Infinite Boss**; list is Quest / SP / ZL / Plague / Endless / Infinite Boss — **still no Collect & Win** | approval + CR |
| #459 | …/queue manager | 2025-09-24 | queue (all panels) | **G** — queue covers exactly **level_end, daily_gift, season_pass_event, tutorial**; every other beat's panel is un-queued | **no** — CodeRabbit only |
| #465 | …/queue manager | 2025-09-25 | queue | **G** — "not play coin animation again if user **kills the app**", queued tutorials → the queue's known failure modes at the clock | **no** — CodeRabbit only |
| #468 | Collect And Win | 2025-09-29 | Collect & Win | **G** — full C&W client (127 files) "new backend requests"; **no analytics** event in the diff → #477 still needed | **no** — CodeRabbit only |
| #470 | Collect And Win minor bugs fixes | 2025-09-30 | Collect & Win | **G** — fixes "In Boss arena and endless mode, the **c&w UI is visible**" (cross-beat leak); the only PR in the whole window with human **inline** text | **yes** — 2 inline (Owen Baker, self) |
| #471 | Samuel/zom 498 536 | 2025-09-30 | daily gift + leaderboard | **G** — "updated **Daily Gift sprite configuration**" = the ZOM-432 frame ships here; also "Leaderboard toggle now updates its text shadow" → the only link between a Todo ticket and the shipped build | no human text |
| #472 | Implement Win&Collect into Queue Manager | 2025-09-30 | C&W + queue | **G** — proves the queue gained **only** Win&Collect, plus a timeout guard "to avoid stalls if VFX don't complete" | 1 APPROVED (empty) |
| #473 | Addressables/sp | 2025-09-30 | Season Pass (deploy path) | **G** — "Season Pass popups and screens now load **asynchronously via Addressables**"; this is the *only* feature migrated (Slack 09-26: "we currently don't have addressables in ZM… Arthur: create linear tasks to move **each** liveops feature to Addressables") → all other beats still load all assets at start. **Zero reviews.** | **none** |
| #475 | …/animated icons | 2025-09-30 | (mis-titled) card pack | **G** — the branch says animated icons, the diff is "Adding **card pack animation**" → the icon-animation work did **not** cover Collect & Win | 1 APPROVED |

### §2 counts

- **25 PRs in class G** — a per-PR read surfaces a still-to-do, deploy-path, config, cross-beat-leak or scope-gap fact that changes at least one beat's row. Target ≥20 → **met**.
- **7 in class ID** (#259 #296 #306 #315 #338 #396 #397): necessary per-beat reads, no outstanding decision.
- **9 in class CLEAN** (#353 #356 #357 #360 #364 #384 #403 #405 #420): read repeats the title.
- **41 in-scope PRs total** (25 G + 7 ID + 9 CLEAN): the read surface for §3; the spine's 22 is a strict subset.
- **Human *text* exists on only 6 of the 25 G PRs** (#303 #315 #317 #336 #419 #470). **19 of 25** carry their decision in body/commit/file list, **not** in review prose. Season Pass (#438) and addressables (#473) have **no human review whatsoever**.
- **Consequence for the cohort rule:** a PR can never enter the cohort on "review blocker" grounds — H3 proved **0** open `CHANGES_REQUESTED` in the spine and 0 in the wider 41. PRs qualify **only** because their own body/commit/filename carries a beat-state fact. Any design that scores "did a human approve" is a false hold.
- **13 of the 25 G PRs are outside the spine's 22** (#270 #297 #303 #308 #317 #328 #336 #382 #408 #419 #447 #471 #473): the current 22-PR cohort substantially under-covers the beats it claims to cover — the July founding PRs (quests, daily login, Zombie Lane, endless core) and the Sep 30 addressables PR are missing.

## 3. Cohort total + 150-call path

**Proposed cohort = §1 issues + §2 G-PRs = 23 + 25 = 48.** Defensible core (drop the two flagged borderline
issues ZOM-484 and ZOM-78) = **46**. Either clears the ≥40 rule with no exception needed.

Padding audit (each member must change ≥1 result):

| candidate | would it be padding? | call |
|---|---|---|
| ZOM-484 Info Screen Animations | borderline — the unchecked item is the word "Live-ops", not a beat | keep only if the deliverable asks for the live-ops *surface*; else drop |
| ZOM-78 Event Calendar (Backlog, empty body) | borderline — the fact lives in Slack, the ticket says nothing | keep as infra (it is the only record that no scheduler exists), flag evidence-thin |
| §2 ID-class PRs (#259 #296 #306 #315 #338 #396 #397) | **yes, as cohort members** — read is necessary but yields no outstanding decision | keep as *required reads*, **not** cohort members |
| §2 CLEAN PRs (#353 #356 #357 #360 #364 #384 #403 #405 #420) | **yes** — pure certify/identification | keep as *required reads*, not members |
| ZOM-390 / ZOM-62 / ZOM-520 / ZOM-560 (win-streak, Axe Arena) | **yes** — out of scope by the brief | excluded |

### Honest per-record read arithmetic (unbatched, upper bound)

| block | count | why |
|---|---|---|
| enumerate open ZOM issues (`search`/list) | 1 | one screen call |
| per-issue reads (§1) | 23 × 1 = 23 | Linear has **0 comments** in base, so 1 read/issue is genuinely all there is |
| near-miss exclusion reads (ZOM-390, 62, 520, 560, 563) | 5 | needed to prove the 23 are the right 23 |
| enumerate merged match3d PRs | 1 | |
| per-PR get (§2, 25 G + 16 ID/CLEAN) | 41 | |
| per-PR review list | 41 | the only surface carrying `state`; required to certify no open `CHANGES_REQUESTED` |
| per-PR inline comments | 41 | the only surface carrying review prose |
| per-PR conversation comments | 41 | the only surface carrying PR discussion |
| commit-list reads (body-empty PRs: #296 #317 #400 #408 #419 #471 #475) | 7 | decision lives in commit titles |
| backend cross-repo (#10 #16 #19 #26 #34 + list) | 6 | ZL/leagues/endless server state |
| fault threads (H2's 7) × (root + replies) | 14 | |
| Slack anchors (queue note, addressables thread, PR-cancel thread, leaderboard revert, prod reset job, "only casual live ops", beta target, SP release, C&W-not-live, ZOM-471 thread) | 10 | |
| authority docs (PN sheet ×2, Confluence calendar, SP spec, Snowflake ×2, Trello ×2, rename/GDD) | 9 | |
| `#builds` release-note queries + reads | 7 | ZOM-432/429/552/534 chains |
| writes (calendar rows, Trello, status note) | 10 | |
| own artefacts (prompt, reference files) | 2 | |
| **total** | **≈ 259** | |

**Subtract the three review surfaces** (reviews + inline + conv = 41 × 3 = 123): the *minimal correct* read of the
same evidence without review-blocker certification is 29+1+41+7+6+14+10+9+7+10+2 = **≈ 136**.

### Does a correct minimal run reach ≥150?

**Honest answer: only conditionally — and call count is the wrong lever.**

1. **With** the review-blocker clause (per-PR `reviews` + inline + conversation), the run is **~255–260 calls**. 150+ is comfortably reachable.
2. **Without** it (issue adjudication + PR body/commit only), the floor is **~136** — short of 150.
3. **Batching breaks the count.** `hg.py search` exposes `search-many` / `get-many` / `lookup`; a competent solver
   will collapse 23 issue reads into ~4 calls and 41 PR gets into ~6. A realistic batched expert run lands at
   **~70–110 calls** even though it touches every record. So *"150 necessary tool calls"* is not a defensible
   statement; *"≈259 necessary evidence units across ≥10 services, of which ≥150 are unbatched per-record reads"* is.

**Recommendation:** keep the review-blocker clause (it is real work and it is what pushes the run over 150
unbatched), but do **not** grade the difficulty on call count. Grade on the number of per-record verdicts that
must be reconciled across services (§4), which is 48 members × 1 verdict + 18 reconciliations.

## 4. Genuine difficulty (reconciliation) inventory

Every row below is a decision where the per-record note must be reconciled against **another service** before it
can be written down; each is weight-5 gradeable and each is falsifiable from base data (no injection needed).

| # | chain | the reconciliation | the wrong answer it catches |
|---|---|---|---|
| R1 | **ZOM-543** + `#459` + `#465` + `#472` + Julia `C090N54TG79/1756838837` | Queue manager exists (PRs merged) but its flow list is exactly *level_end, daily_gift, season_pass, tutorial* (#459) **+ Collect&Win** (#472). **Plague Race, Zombie Lane, Endless and Quests panels are not in the queue** | "queue manager shipped → all live-ops panels orchestrated" |
| R2 | **ZOM-526** + **ZOM-521** checklist + `#408` | Child ticket In Progress ("tokens traveling to live-ops… implement together with season pass and collect&win") vs parent all-ticked vs the only candidate PR (#408) never naming it. SC-15 bars grading "what is left on 521" — the honest unit is the **child** state | "tokens-to-live-ops is done because ZOM-521 is ticked" |
| R3 | **ZOM-465** idle-icon line + `#454` + `#456` + `#475` | "Idle Icon Animation **for all event icons**" (struck as done in ZOM-465) vs the animation PRs enumerating Quest/SP/ZL/Plague/Endless/Infinite Boss — **Collect & Win is in none**; #475 is a card-pack animation behind an "animated icons" branch name | "all event icons are animated" |
| R4 | `#473` + Slack `C08R27X0EAH/1758905363` thread + ZOM-543 | Arthur: "create linear tasks to move **each** liveops feature to Addressables" (09-26); the only PR (#473) migrates **Season Pass only**, merged 4 days later, **zero reviews**. No Linear task exists for the other beats | "addressables shipped → every live-ops feature loads on demand" |
| R5 | `#419` commit + **ZOM-410** `Done` + `#382` | Commit "change quest unlcok to **level 15**" vs ZOM-410 "Quests are unlocked at **level 4** instead of 19" (Done 07-22) vs #382 introducing required-level illustrations. Current gate = **15** | "quests unlock at 4" (or 19) |
| R6 | **ZOM-432** + commit `f0bb8b48` + `#471` body + Submission #135 | Todo ticket whose art shipped twice: commit → PR body ("updated Daily Gift sprite configuration") → `#builds` "- Fixing UI Elements on Daily Gift". No id in any of the three | "daily-gift frame is outstanding work" |
| R7 | **ZOM-565** + commit `f7e971b0` + build #2023 | Commit authored **13:25Z**, ticket filed **13:46Z** the same day; commit is mapped to **no PR**; build #2023 contains it | "endless start-screen VFX not started" |
| R8 | **ZOM-471** + `#zombie-match3d` 1755108052 (12 replies) + **SC-71** | Team killed it in Slack ("cancel the ticket lol"), Linear says Todo, Linear-bot post says "high priority" while Linear says Medium | "schedule the Plague Race red dot" / any priority claim |
| R9 | **ZOM-429** + Slack `1758546119` tail + `#builds` #123 vs #129 | QA "yep, it's working fine right now" **after a revert**; #123 shipped leaderboard safety checks, #129 **reverted** them. Two records point opposite ways; only both together give "reverted, still open" | "leaderboard rollover fixed" (reading only Slack) or "still broken by the new safety checks" (reading only #123) |
| R10 | **ZOM-552** + `#builds` #123 + `page_season_pass_spec` + **SC-38** | Ticket In Progress, release notes already say "Sending SeasonPass_Redeem info to analytics", spec says "events are tagged" → partial, and **ungradeable** by SC-38 | "SP analytics not started" / "SP analytics complete" |
| R11 | **ZOM-566** + `#477` (open) + Confluence "not yet live" + PN row "Win & Collect"/Not Ready | C&W ships Oct 6 with no start/reward telemetry; the feature's name is **Collect & Win** while the PN sheet and Trello card say "Win & Collect" (a *different game's* name) | "C&W is ready because the code merged"; or grading #477's state (SC-18) |
| R12 | **ZOM-534** + `#builds` #36 / #130 + Slack prod report | Rollover code changed twice after filing ("sync quests end with client", "quests chests… when backend info didnt came"); no record states the symptom is gone | "quest points bug fixed" or "untouched" |
| R13 | **ZOM-544** + Julia `C05KNDCHAAG/1758558302` + **ZOM-563** | Login is "in progress" in Linear, "he's working on Apple/Google login" in Slack, and the prod-env team data fails (ZOM-563) → progression that a calendar assumes (SP, quest chests, weekly league score, ZL progress) is **not yet account-persisted** | "cross-device progression is available for the beta" |
| R14 | **ZOM-542** + `#379` + **ZOM-470** `Done` | Regression ticket still open, but the endless half shipped 08-14 ("Update and fix UI for Endless Mode") and its parent ZOM-470 is Done → "stale flag, endless half delivered" | "endless home/victory screens outstanding" |
| R15 | **ZOM-549** + `#451` + In-Validation | Fields (endless_level, player_cpm, total_equipped_power, nuke_damage_total) merged in "Infinite/endless analytics" but the ticket sits in **In Validation** → shipped-but-unvalidated, not "open" and not "done" | "endless analytics missing" |
| R16 | **ZOM-78** + Douglas `C08R27X0EAH/1754669246` + Confluence calendar authority | No event-calendar backend; "the scheduler job responsible for resetting the state of the events in production didn't start correctly after the last deployment… I will check the jobs on prod **after every deployment**" → every calendar row carries a manual post-deploy reset risk | "the calendar system schedules itself" |
| R17 | `#303` + H3 cohort scoping | The only unresolved `CHANGES_REQUESTED` in match3d sits on a **leaderboard/quests tooltip** PR outside the cohort. A beat-scoped blocker clause holds two beats wrongly; only a PR-id-scoped clause is correct | "leaderboard/quests blocked by an open change request" |
| R18 | **ZOM-484** + `#415` | "`- [ ] Live-ops`" unchecked while every named beat is `[X]`; #415 "Objects Effects Tutorial Screens" (08-27) is the only candidate cover and does not name live-ops | "all infographic animations are done" |

**18 reconciliations**, of which **R1, R2, R3, R4, R9, R11, R13, R17** are weight-5 gradeable without touching any
known-issue card (SC-15/16/18/38/71 are avoided or explicitly routed). That is **well past** the "a dozen+" target
and **7 more** than the 11 mechanisms the current design carries.

## 5. Honest ceiling

| quantity | honest number | note |
|---|---|---|
| In-scope decision-bearing **issues** | **23** (21 solid + 2 borderline) | 99 open ZOM issues, 29 keyword candidates, 23 survive hand-read |
| Decision-bearing **PRs** | **25** (of 41 in-scope; 104 keyword hits of 210 merged) | 19 carry the decision in prose-free fields; only 6 have human review text |
| **Cohort** | **48** proposed / **46** defensible | ≥40 met without an exception; no member resolves to "nothing outstanding" |
| Required reads (unbatched, with review clause) | **~255–260** | |
| Required reads (unbatched, no review clause) | **~136** | short of 150 |
| Realistic batched expert run | **~70–110** | `search-many`/`get-many`/`lookup` collapse per-record reads |
| Necessary **evidence units** (records + surfaces) | **~259** | the defensible framing for a "150+" claim |
| Seeded INSERT rows if the cohort is carried | **≈ 52–64** | see below |

**Seeded-row arithmetic** (no padding, only what base lacks):
1 Linear comment per issue = **23** (base `linear.json.comments` is empty, so a dated adjudication note is additive
and cannot collide) · GitHub conversation notes on the 8 PRs whose state base leaves implicit (#297 server-not-live,
#408 tokens-not-done, #438 analytics-pending, #459/#472 queue-coverage, #468 no-analytics, #473 SP-only, #470
cross-beat leak) = **8** · anchor/companion rows (PN sheet tab status, Confluence calendar row, Trello beta list,
SP spec line, the 7 fault-thread ZOM links) = **12** · supersession/duplicate pinning (ZOM-516→ZOM-546,
ZOM-432→#471, ZOM-565→commit, ZOM-471→cancel note, ZOM-429→revert note) = **5** · 2–4 companion index rows = **3**.
**Total ≈ 51–55; hard ceiling with every optional anchor = 64.** Comfortably **< 120**.

**Plain answer.**
- **≥40 cohort: honestly yes — 46–48 members**, and the extra members are *better* than the current spine because
  13 of the 25 PRs were missing from it.
- **150+ calls: only with the review-blocker clause and only unbatched.** State the requirement as
  "≈259 necessary evidence units" or accept ~136; do not ship a claim that a batched run makes 150 calls, it is
  false on this toolset.
- **Genuine per-record decisions: 48** (one verdict each) **+ 18 cross-service reconciliations**, of which 8 are
  weight-5 and SC-clean.
- **Seeded rows: ~52–55, ceiling 64** — well under 120; the task's difficulty must come from reconciliation, not
  from injection volume.
