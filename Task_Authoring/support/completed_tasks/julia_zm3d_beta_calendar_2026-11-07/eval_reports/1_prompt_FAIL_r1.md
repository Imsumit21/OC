## PROMPT EVALUATION REPORT

### Task: ZM3D beta live-ops and push calendar for the four buy weeks (Oct 6 – Nov 2, 2025), built to Frederick's brief, with ticket notes, a ZOM-78 link and a recommendation to Frederick
### Assigned Persona: Julia Lawson - Product Manager
### Assigned Business Function: Product
### Assigned Competency: Marketing and GTM
### Assigned Task Skill: Planning and decision support
### Assigned Horizon: long-horizon (difficulty mode: medium)

## 1. Scope

| Field | Value |
|---|---|
| Stage / version | /prompt, Eval 1 (`Evals/1_Prompt_Eval.md`), policy `prompt-source-checks-v2` |
| Mode | Chat review, audit (attempt 6aea4c1e9b621f28dc3a5332) |
| Review date | 2026-11-05 |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16); `Evals/references/universes/synthcut/universe_manifest.json` |
| Eval version | task-quality-v1 |
| Eval release SHA-256 | 81446b85bb68b971bfce06d9d3cf07ad43d923b5702670f206122d1f6d34d53c |
| Reviewed prompt SHA-256 | b5d6559cdf2613b7635345784a4914c7025f440ba4ea12268246e1cfab559770 (`Evals/task_inputs/04_Prompt.txt`, 801 bytes, attachment to the /prompt message) |
| Review context SHA-256 | e83f0270c23e9967fb826a48f9566ae993a5989898b4f49773c588a968d9cc4a |
| Prompt record SHA-256 | 95edff732441a8d9b3d12a703c9c333c057ed7e2e2480a83b82a4c5370a92a85 |
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql`, SHA-256 4c6328ab2e86835892054641d61871f9c304db667e4e27446eabfd71489b5e47 (59,953 bytes) |
| Assignment | `Evals/task_inputs/00_Task_Assigned_Inputs.md` (platform record), SHA-256 2fda797a28eed36e9cd07c0e8cacbdf0ed6400fc5717c15b2c7f6110fbde5a5d |
| Error/async config, dynamic context, reference files | None supplied (not applicable) |

## 2. Input / authority issues

- All five assignment fields are on the saved platform record; the injection answer is saved SQL. Intake cleared without a round trip.
- The prompt incorporates Frederick's brief ("The working rules for how he wants it built are in the brief he shared with me"). The brief (Google Doc `f_7c3e91a4d2b85f60e1a9c4`, SQL statement 25) is shared with Julia, so its rules are requirements (prompt-incorporation-v1). Frederick's DM (`8b090dec…`) is the ask the prompt refers to.
- Push sheet evidence is cited from a verbatim extract of `gsheets/data.json` `/sheets_spreadsheets/220` (source SHA-256 a9cc229c…0a28f), because the 330 MB export can't be loaded whole on the review machine.

### Injection Gate
- State: CURRENT (no rerun needed)
- Reviewed SQL sha256: 4c6328ab2e86835892054641d61871f9c304db667e4e27446eabfd71489b5e47  Eval 0 verdict: PASS (injection-static-v2, 2026-11-05)
- Eval 0 findings on records this prompt depends on: none at fail level. Advisory A6 (who "Product" is) is settled by base Confluence `page_season_pass_spec`: "Owner: Robert (Product)." Advisory A9 ("the current prod build") is enough for the hold: Vincent re-tested after a restart on two devices. Advisories A1–A5 and A7 don't change any graded value.

### Dataset Similarity
- Library: refreshed 2026-11-05T08:40Z, 7.6 h old, 410 tasks  Gate: PASS  Nearest tier: same scenario
- (hidden) (completed, Julia Lawson, Product Management / Planning and decision support), meaning 0.726, wording 0.021: also a Julia → Frederick ZM3D live-ops slot plan ("live-ops slot plan covering October 13 to December 31, 2025"). This prompt differs in window (four buy weeks from Oct 6), push plan, brief-driven hold/lock rules and writes. No score change; see Recommended Improvements.

## 3. Checklist (all NEW this run unless marked)

| Item | Status |
|---|---|
| Intake (five fields, injection answer) | NEW, cleared from saved inputs |
| STEP 0.5 injection gate | NEW: CURRENT, Eval 0 PASS REUSED |
| STEP 0.6 dataset similarity | NEW: PASS (same scenario 0.726) |
| Phase 0 Docs, catalog, universe exploration | NEW: SQL read in full (110 statements); base checked: push sheet (gsheets #220), Confluence calendar / Season Pass spec / engine pages, match3d-backend CDK schedules, GitHub reviews Aug–Sep 2025 (no CHANGES_REQUESTED in the cohort; only #303 in July, by a bot), Linear cohort issues, Slack memberships |
| Phase 1 persona, naturalness, anti-patterns, diversity, assignment gates | NEW |
| Phase 2 UGT, feasibility, truthfulness, cross-service, investigation, clarity, contrived, date, originality | NEW |
| Phase 3 data exists, coherence | NEW (static integrity REUSED from Eval 0) |
| Phase 4 scoring; Phase 5 deep recheck | NEW |

## 4. Requirement ledger

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Build the calendar for the four buy weeks (Oct 6 00:00 – Nov 2 23:59 UTC) in Julia's sheet | Frederick DM `8b090dec…`; brief "Span and time base"; UA plan slides W1–W4; sheet `f_e4a17c90…` (Calendar tab, 9 columns) | Slack DM → brief → Drive folder "ZM Live Ops" | Slack read; GDocs read; GSlides read; GSheets read/write | DM member; brief shared (reader); sheet owner | Calendar tab rows per beat |
| Each beat a player can see: windows, held/until, push, still to do + owner | Brief rules; CDK schedules (Plague Race daily, Leagues Mon, Endless daily + Mon, Collect & Win 1,2 / 3,4 / 5,6,0, Season Pass 1st); Confluence calendar; gcal release Oct 8 15:00Z; Arthur #470 (C&W server on DEV); Vincent re-test (leaderboard); Robert retraction (Halloween); Brian's handoff emails; Season Pass spec lock "24h before"; PR comments #370 / #438 / #454 / #471; Linear cohort comments; Trello Oct 13 quests | GitHub repo + PRs, Confluence, Slack, Gmail, GCal, Linear, Trello | GitHub/Confluence/Linear/Trello reads (unscoped); Gmail/GCal/Slack reads | Julia's mailbox and calendar; #zombie-match3d and #zombie-art member; Robert DM member | One row per beat |
| Push plan: each beta push goes out or waits, and what's missing | Brief "Push copy"; "Push Notifications Zombie Match" tab "PNs Beta" (14 rows) | Drive share | GSheets read | Shared with Julia | Pushes tab rows (**fork, see UGT**) |
| Note on the ticket of each beat that can't run yet | ZOM-429 (weekly leaderboard bug) | Linear search | Linear comment create | Unscoped | Comment(s) |
| Link the sheet on the calendar ticket | ZOM-78 + Frederick's comment `cmt_zom78_1` | Linear | Linear comment / attachment | Unscoped | Link on ZOM-78 |
| Recommendation with trade-offs to Frederick | DM "send me the recommendation back here" | Slack DM | Slack send message | DM member | DM reply |

## Phase 1: Prompt Structure & Persona

**Persona:** PASS (5)
- Julia is the PM; Confluence `page_liveops_calendar` says "Design, led by Julia Lawson, walks the coming weeks with Frederick Stone", and the engine page names her owner of event definitions. Frederick's DM asks her directly. Voice and scope fit.

**Assigned Competency:** PASS (5). A live-ops and push calendar for a paid UA beta buy (UK/US, English creative), with a go/hold recommendation for the pivot call, is Marketing and GTM work.

**Assigned Task Skill:** PASS (5). Planning and decision support is the core: plan windows, hold calls, lock moves and a recommendation with trade-offs.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y. PASS
- Dynamic change: Brian Oct 29 → Fri Oct 31 handoff; Robert's Sep 18 approval → Sep 30 retraction; ZOM-429 "force-closes and reopens … fine" (Sep 23) → Vincent's Sep 30 prod re-test; ZOM-465 "every event icon animates" (Sep 26) → Marcus's #454 "Collect & Win event icon animation is still to do" (Sep 30); ZOM-432 frame missing → Samuel's #471 "went out … submission 135".
- Multi-source: Slack, Gmail, GCal, Drive/Docs/Sheets/Slides, GitHub (repo + PRs), Linear, Trello, Confluence.
- Data seeding: PASS. The rules live in the brief and records; the prompt is a short trigger.

**Naturalness:** FAIL (scored under Contrived, see 2.7)
- First person, plain, no formatting, no typos. But the second paragraph spells out each sheet row's contents ("work out the windows it runs in, whether it's held and until when, the push that goes with it, and what still has to land before it runs and who owns that" and "whether it goes out or waits, and if it waits, what's missing"), restating Frederick's DM field list instead of pointing to it. That is the "enumerated deliverable specs" red flag.

**Anti-Patterns:**
| Pattern | Status |
|---------|--------|
| Command List | PASS (no first/then/finally; "Once the sheet's done, link it…" is natural sequencing of two writes) |
| Bolt-On | PASS (every sentence feeds the calendar, ticket notes, link or recommendation) |
| Pre-Solving | PASS (no beat, hold, lock or cause is named) |
| Tool Mention | PASS (no tool, MCP or parameter names) |

**Diversity:** goes well beyond "investigate + post one Slack message": sheet build across two tabs, Linear comments, a Linear link and a DM.

## Phase 2: Depth Assessment

**Unique Ground Truth:** FAIL (2)

### Unique Ground Truth comparison

Unique Ground Truth: FAIL 2

Basis: Unresolved material differences, led by the push plan. The brief's rule ('A push goes out only if its row is Ready and LIVE and its English copy names the game only as Zombie Match 3D') meets two edges no record settles: rows 3 and 5 are Ready and LIVE but their copy names no game (go out vs wait), and every Ready and LIVE row is a Local Notification, not a Push Notification (in the push set or not). Whether any beta push goes out, the Pushes tab rows and the recommendation differ. The deep recheck added four more open forks: Domino-only push rows in or out (D), which beats get ticket notes (E), whether the Season Pass October season counts (F) and whether the daily-gift frame is still to do (G).

Alternative selection: Applied the brief's push rule to all 14 'PNs Beta' rows. Rows 3 and 5 are the only rows that meet Ready + LIVE without a wrong game or event name, so any alternative that changes their outcome changes whether any push goes out. B (no game name fails the rule) and C (local notifications are not pushes) are the two readings a careful PM could defend from the rule's own words and the sheet's own type column.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Every row of the 'PNs Beta' tab is a beta push; a Ready and LIVE row whose copy names no wrong game or event goes out. | Calendar per the brief (Collect &amp; Win from Fri Oct 10 00:00 UTC, Weekly Leaderboard held, Season 2 from Nov 1 with the config lock moved before Oct 31 00:00 UTC, Halloween and Boss Arena off). Push plan lists all 14 'PNs Beta' rows; Lives recharged (row 3) and 7 Days Lapsed (row 5) go out because they are Ready and LIVE and their English copy names no other game or event; the other 12 wait with what is missing. | Fill the Calendar and Pushes tabs of Julia's ZM3D Beta Live-Ops Calendar sheet (14 push rows, 2 marked go-out); note on ZOM-429; link the sheet on ZOM-78; Slack DM to Frederick. | ZM3D Beta Live-Ops Calendar (Calendar and Pushes tabs); Linear ZOM-429; Linear ZOM-78; Slack DM D05SD5QLG94 with Frederick. | Pushes tab: rows 3 (Full Ammo Reloaded!) and 5 (They’ve Taken Over…) go out; rows 1, 2, 4, 6-14 wait with the missing piece (Not Ready, WIP, or Puzzles vs Zombies / Win &amp; Collect copy). Recommendation to Frederick says two retention notifications are cleared to send. | SP (Evals/task\_inputs/04\_Prompt.txt): "for each beta push, whether it goes out or waits, and if it waits, what's missing."; S\_BRIEF\_PUSH (Evals/task\_inputs/01\_Universe\_Inject.sql): "A push goes out only if its row is Ready and LIVE and its English copy names the game only as Zombie Match 3D and events only by their ZM3D names. Anything else is held, with what is missing. Beta pushes are English-only (UK and US buys); the translated tab is the old Domino set still waiting on ZM3D localization."; S\_PUSH3 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/3): ""Ready", "Core Game", "Local Notification ", "Rollover", "When lives are recharged", "Everyone", "Main Menu", "LIVE", "Full Ammo Reloaded! 🔫", "Your energy is fully charged! The zombies are closing in—jump back into the battle now and show them who's boss. 🧟⚔️""; S\_PUSH5 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/5): ""Ready", "LAPSED", "Local Notification ", "7 Days Lapsed", "Has not played in seven days.", "7d lapse since last session", "Main Menu", "LIVE", "They’ve Taken Over… Can You Stop Them? 😱", "It’s been a while, survivor. The undead are stronger than ever. Rally your gear and get back into the fray before it’s too late! 🧟‍♀️💥"" |
| B | 'names the game only as Zombie Match 3D' requires the copy to name the game as Zombie Match 3D; copy that names no game does not meet it. | Same calendar. Push plan lists all 14 'PNs Beta' rows, but Lives recharged (row 3) and 7 Days Lapsed (row 5) wait because their English copy never names the game as Zombie Match 3D, which the rule requires of any push that goes out; no beta push goes out. | Fill the Calendar and Pushes tabs of the same sheet (14 push rows, 0 marked go-out); note on ZOM-429; link the sheet on ZOM-78; Slack DM to Frederick. | ZM3D Beta Live-Ops Calendar (Calendar and Pushes tabs); Linear ZOM-429; Linear ZOM-78; Slack DM D05SD5QLG94 with Frederick. | Pushes tab: all 14 rows wait; rows 3 and 5 wait because their copy does not name Zombie Match 3D. Recommendation to Frederick says no beta push is cleared to send. | S\_BRIEF\_PUSH (Evals/task\_inputs/01\_Universe\_Inject.sql): "A push goes out only if its row is Ready and LIVE and its English copy names the game only as Zombie Match 3D and events only by their ZM3D names. Anything else is held, with what is missing. Beta pushes are English-only (UK and US buys); the translated tab is the old Domino set still waiting on ZM3D localization."; S\_PUSH3 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/3): ""Ready", "Core Game", "Local Notification ", "Rollover", "When lives are recharged", "Everyone", "Main Menu", "LIVE", "Full Ammo Reloaded! 🔫", "Your energy is fully charged! The zombies are closing in—jump back into the battle now and show them who's boss. 🧟⚔️""; S\_PUSH5 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/5): ""Ready", "LAPSED", "Local Notification ", "7 Days Lapsed", "Has not played in seven days.", "7d lapse since last session", "Main Menu", "LIVE", "They’ve Taken Over… Can You Stop Them? 😱", "It’s been a while, survivor. The undead are stronger than ever. Rally your gear and get back into the fray before it’s too late! 🧟‍♀️💥"" |
| C | A 'beta push' is a row whose What column is Push Notification; Local Notification rows are timer messages, not pushes. | Same calendar. Only rows whose What column is 'Push Notification' (rows 1 and 7-14) are beta pushes; the five Local Notification rows (rows 2-6) are not pushes and are left out; all nine pushes wait; no beta push goes out. | Fill the Calendar and Pushes tabs of the same sheet (9 push rows, 0 marked go-out); note on ZOM-429; link the sheet on ZOM-78; Slack DM to Frederick. | ZM3D Beta Live-Ops Calendar (Calendar and Pushes tabs); Linear ZOM-429; Linear ZOM-78; Slack DM D05SD5QLG94 with Frederick. | Pushes tab: 9 rows (Quests rollover plus the eight event/rollover pushes), all waiting; no Local Notification row. Recommendation to Frederick says no beta push is cleared to send. | SP (Evals/task\_inputs/04\_Prompt.txt): "for each beta push, whether it goes out or waits, and if it waits, what's missing."; S\_PUSH\_HDR (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/0): ""Status", "Type", "What", "When", "Details", "Segmentation", "Destination", "Status (NA, WIP, LIVE)", "Headline", "Body", "Action Button""; S\_PUSH1 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/1): ""Not Ready", "Quests", "Push Notification ", "Rollover""; S\_PUSH3 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/3): ""Ready", "Core Game", "Local Notification ", "Rollover", "When lives are recharged", "Everyone", "Main Menu", "LIVE", "Full Ammo Reloaded! 🔫", "Your energy is fully charged! The zombies are closing in—jump back into the battle now and show them who's boss. 🧟⚔️""; S\_PUSH14 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/14): ""Ready", "Event", "Push Notification", "Weekly Rollover", "Weekly Leaderboard reset", "Everyone", "Main Menu", "WIP"" |
| D | Only beta rows that map to a ZM3D beat belong in the push plan; the Domino carry-overs (Nathan's Treasure Hunt, Streak Fever, Axe Arena, Hourly Coins) are left out. | Same calendar; push plan lists only rows tied to a ZM3D beat; rows 2, 8, 10, 11 are not written. | Pushes tab with 10 rows (rows 2, 8, 10, 11 omitted); same ticket, link and DM writes. | ZM3D Beta Live-Ops Calendar (Calendar and Pushes tabs); Linear ZOM-429; Linear ZOM-78; Slack DM D05SD5QLG94 with Frederick. | Pushes tab without the Domino-only event rows; recommendation counts pushes over the ZM3D beats only. | S\_SHEET\_PUSHTAB (Evals/task\_inputs/01\_Universe\_Inject.sql): "\[\["Beat","Push name","Send (UTC)","Segment","English copy","Status","Notes"\]\]"; S\_CONF\_DOMINO (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/confluence/confluence\_working.json pointer /pages/27/body): "&lt;td&gt;Streak Fever&lt;/td&gt;&lt;td&gt;Domino Delights&lt;/td&gt;"; S\_CONF\_AXE (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/confluence/confluence\_working.json pointer /pages/27/body): "&lt;td&gt;Axe Arena&lt;/td&gt;&lt;td&gt;Domino Delights&lt;/td&gt;"; S\_PUSH8 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/8): ""Not Ready", "Event", "Push Notification", "Event Start (server time)", "Nathan’s Treasure Hunt event start"" |
| E | 'If a beat can't run yet' covers beats that cannot run as of today, not only held ones: Collect &amp; Win (server windows still on DEV) and Season Pass Season 2 (config still to land) also get ticket notes. | Same calendar and push plan; notes on Collect &amp; Win's and Season Pass's tickets as well as ZOM-429. | Linear comments on ZOM-429 plus ZOM-566 and ZOM-552 (the only tickets for those beats); same sheet, link and DM. | Same sheet and DM; Linear ZOM-429, ZOM-566, ZOM-552, ZOM-78. | Extra notes telling the Collect &amp; Win and Season Pass owners what must land. | SP (Evals/task\_inputs/04\_Prompt.txt): "for each beta push, whether it goes out or waits, and if it waits, what's missing."; S\_ARTHUR470 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Server-side windows for Collect &amp; Win are still on the DEV stack only, they reach prod with the next backend release."; S\_ZOM566 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3643/title): "Collect&amp;Win Analytics"; S\_ZOM552 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3628/title): "Season Pass Analytics" |
| F | Season Pass server windows go live only with the Oct 8 15:00 UTC backend release, so the October season (opened Oct 1, before the release) does not count; the first Season Pass window is Nov 1 00:00 UTC. | Season Pass row: first window Sat Nov 1 00:00 UTC, no window in W1-W4. | Calendar tab Season Pass row with first window Nov 1 only; other writes the same. | ZM3D Beta Live-Ops Calendar (Calendar and Pushes tabs); Linear ZOM-429; Linear ZOM-78; Slack DM D05SD5QLG94 with Frederick. | Season Pass windows: Nov 1 00:00 - Nov 2 23:59 UTC only, versus A's October season Oct 6 - Oct 31 plus Nov 1 onward. | S\_GCAL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Prod backend deploy for the beta. The live-ops server windows go live with this release; release window 18:00-19:00 Istanbul time."; S\_BRIEF\_START (Evals/task\_inputs/01\_Universe\_Inject.sql): "A beat starts with the first window that opens after its server windows are live on prod, the backend release instant read in UTC, not when its client PRs merged. Collect &amp; Win runs Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC, so a window the release instant pre-empts does not count."; S\_SPSPEC\_PROD (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/confluence/confluence\_working.json pointer /pages/20/body): "Android 0.3.127 published Sep 22, iOS 0.3.49 released Sep 29" |
| G | The daily-gift frame is still to do: Samuel's 'submission 135' is an Android submission build, iOS is not stated and the stores have not approved it, so under the brief an unverified build or platform is a still-to-do. | Login calendar / daily gift row: still to do lists the frame on iOS / pending store approval (owner Samuel or Calvin) instead of nothing. | Calendar tab daily-gift row still-to-do cell filled; ZOM-432 may get a note; other writes the same. | ZM3D Beta Live-Ops Calendar (Calendar and Pushes tabs); Linear ZOM-429; Linear ZOM-78; Slack DM D05SD5QLG94 with Frederick. | Still-to-do cell names the daily-gift frame versus A's 'shipped, nothing to land'. | S\_SAMUEL471 (Evals/task\_inputs/01\_Universe\_Inject.sql): "The daily-gift frame went out with this PR — it is in submission 135, so that one can be closed."; S\_BUILD135 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C05433XK267/2025-09.json pointer /1124/attachments/0/fallback): "Match3D Android Submission - \#135 - main  Success after 1 hr 28 min"; S\_BRIEF\_UNVER (Evals/task\_inputs/01\_Universe\_Inject.sql): "An established failure holds it; an unverified build or platform is a still-to-do, not a hold."; S\_SLIDES\_STORES (Evals/task\_inputs/01\_Universe\_Inject.sql): "Scaled beta-cohort buy, starting once the stores approve the Sep 30 builds." |

Explicit option inventory: The prompt gives one explicit option list for pushes: goes out or waits.
Inventory evidence: SP (Evals/task\_inputs/04\_Prompt.txt): "for each beta push, whether it goes out or waits, and if it waits, what's missing."

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| goes out | RETAINED | A | A sends rows 3 and 5; nothing excludes it. Evidence: SP (Evals/task\_inputs/04\_Prompt.txt): "whether it goes out or waits" |
| waits | RETAINED | B, C | B and C hold rows 3 and 5; nothing excludes it. Evidence: SP (Evals/task\_inputs/04\_Prompt.txt): "whether it goes out or waits" |

Compared alternative: B
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. The brief's only push rule says a push goes out if it is Ready and LIVE and its English copy 'names the game only as Zombie Match 3D'. Rows 3 and 5 are Ready and LIVE but their copy names no game at all. Read as 'uses no name other than Zombie Match 3D' they go out; read as 'names the game, and only as Zombie Match 3D' they wait. No record speaks to copy that omits the game name, so the general rule cannot settle its own edge (ugt-boundary-v1).
Resolution evidence: S\_BRIEF\_PUSH (Evals/task\_inputs/01\_Universe\_Inject.sql): "A push goes out only if its row is Ready and LIVE and its English copy names the game only as Zombie Match 3D and events only by their ZM3D names. Anything else is held, with what is missing. Beta pushes are English-only (UK and US buys); the translated tab is the old Domino set still waiting on ZM3D localization."; S\_PUSH3 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/3): ""Ready", "Core Game", "Local Notification ", "Rollover", "When lives are recharged", "Everyone", "Main Menu", "LIVE", "Full Ammo Reloaded! 🔫", "Your energy is fully charged! The zombies are closing in—jump back into the battle now and show them who's boss. 🧟⚔️""; S\_PUSH5 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/5): ""Ready", "LAPSED", "Local Notification ", "7 Days Lapsed", "Has not played in seven days.", "7d lapse since last session", "Main Menu", "LIVE", "They’ve Taken Over… Can You Stop Them? 😱", "It’s been a while, survivor. The undead are stronger than ever. Rally your gear and get back into the fray before it’s too late! 🧟‍♀️💥""

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | A marks rows 3 and 5 as going out; B holds every push. |
| writes | DIFFERENT | The Pushes tab Status cells for rows 3 and 5 differ (go out vs wait). |
| destinations | SAME | Both write to the same sheet, tickets and DM. |
| contents | DIFFERENT | A tells Frederick two notifications are cleared; B tells him none is, and gives the missing game name as the reason. |

Resolution relevance challenge: The cited rule is the only instruction about push copy; it is silent on copy without a game name, and rows 3 and 5 are the only Ready and LIVE rows without a wrong name, so the edge decides whether any push goes out.
Delegation challenge: NOT_CLAIMED. No source delegates the call or accepts both outcomes.
Challenge evidence: S\_BRIEF\_PUSH (Evals/task\_inputs/01\_Universe\_Inject.sql): "A push goes out only if its row is Ready and LIVE and its English copy names the game only as Zombie Match 3D and events only by their ZM3D names. Anything else is held, with what is missing. Beta pushes are English-only (UK and US buys); the translated tab is the old Domino set still waiting on ZM3D localization."; S\_PUSH4 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/4): "Return to Puzzles vs Zombies now"

Compared alternative: C
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. The 'PNs Beta' tab mixes 'Push Notification' rows (1, 7-14) and 'Local Notification' rows (2-6). The prompt asks for 'each beta push' and the brief speaks of 'A push' and 'Beta pushes'; nothing Julia can open says whether timer-based local notifications count. Every Ready and LIVE row is a Local Notification, so the scope decides whether any push goes out and how many rows the Pushes tab carries.
Resolution evidence: SP (Evals/task\_inputs/04\_Prompt.txt): "for each beta push, whether it goes out or waits, and if it waits, what's missing."; S\_PUSH\_HDR (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/0): ""Status", "Type", "What", "When", "Details", "Segmentation", "Destination", "Status (NA, WIP, LIVE)", "Headline", "Body", "Action Button""; S\_PUSH3 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/3): ""Ready", "Core Game", "Local Notification ", "Rollover", "When lives are recharged", "Everyone", "Main Menu", "LIVE", "Full Ammo Reloaded! 🔫", "Your energy is fully charged! The zombies are closing in—jump back into the battle now and show them who's boss. 🧟⚔️""; S\_PUSH1 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/1): ""Not Ready", "Quests", "Push Notification ", "Rollover""

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | A sends rows 3 and 5; C holds everything and drops the local rows. |
| writes | DIFFERENT | A writes 14 push rows, C writes 9. |
| destinations | SAME | Same sheet, tickets and DM. |
| contents | DIFFERENT | Different row set and a different go-out count in the recommendation. |

Resolution relevance challenge: The What column is the sheet's own type field, so C reads the data as written; the tab name 'PNs Beta' and the brief's 'its row' support A. Neither is a record that rules on whether local notifications are pushes.
Delegation challenge: NOT_CLAIMED. No source delegates the call or accepts both outcomes.
Challenge evidence: S\_PUSH\_HDR (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/0): ""Status", "Type", "What", "When", "Details", "Segmentation", "Destination", "Status (NA, WIP, LIVE)", "Headline", "Body", "Action Button""; S\_BRIEF\_PUSH (Evals/task\_inputs/01\_Universe\_Inject.sql): "A push goes out only if its row is Ready and LIVE and its English copy names the game only as Zombie Match 3D and events only by their ZM3D names. Anything else is held, with what is missing. Beta pushes are English-only (UK and US buys); the translated tab is the old Domino set still waiting on ZM3D localization."

Compared alternative: D
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. Rows 8 (Nathan's Treasure Hunt), 10 (Streak Fever), 11 (Axe Arena) and 2 (Hourly Coins) are Domino carry-overs with no ZM3D beat, yet sit in the 'PNs Beta' tab; Julia's Pushes tab has a Beat column. Nothing says whether they are listed as waiting or left out.
Resolution evidence: S\_SHEET\_PUSHTAB (Evals/task\_inputs/01\_Universe\_Inject.sql): "\[\["Beat","Push name","Send (UTC)","Segment","English copy","Status","Notes"\]\]"; S\_CONF\_DOMINO (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/confluence/confluence\_working.json pointer /pages/27/body): "&lt;td&gt;Streak Fever&lt;/td&gt;&lt;td&gt;Domino Delights&lt;/td&gt;"; S\_PUSH8 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/8): ""Not Ready", "Event", "Push Notification", "Event Start (server time)", "Nathan’s Treasure Hunt event start""

| Material field | Relation | Explanation |
|---|---|---|
| decision | SAME | Every listed push waits in both. |
| writes | DIFFERENT | A writes rows 2, 8, 10, 11; D does not. |
| destinations | SAME | Same sheet. |
| contents | DIFFERENT | Different row set. |

Resolution relevance challenge: The Beat column and the Confluence event list tie these rows to Domino Delights; the tab name ties them to the beta. Neither rules on inclusion.
Delegation challenge: NOT_CLAIMED. No source delegates the call or accepts both outcomes.
Challenge evidence: S\_SHEET\_PUSHTAB (Evals/task\_inputs/01\_Universe\_Inject.sql): "\[\["Beat","Push name","Send (UTC)","Segment","English copy","Status","Notes"\]\]"; S\_CONF\_DOMINO (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/confluence/confluence\_working.json pointer /pages/27/body): "&lt;td&gt;Streak Fever&lt;/td&gt;&lt;td&gt;Domino Delights&lt;/td&gt;"; S\_PUSH8 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/8): ""Not Ready", "Event", "Push Notification", "Event Start (server time)", "Nathan’s Treasure Hunt event start""

Compared alternative: E
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. Collect &amp; Win cannot run as of the Oct 1 clock (server windows on DEV until the Oct 8 release) and Season Pass Season 2 still needs its config, but neither is held under the brief. 'Can't run yet' can mean held or not runnable now; and the only tickets for those beats are analytics tickets.
Resolution evidence: SP (Evals/task\_inputs/04\_Prompt.txt): "for each beta push, whether it goes out or waits, and if it waits, what's missing."; S\_ARTHUR470 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Server-side windows for Collect &amp; Win are still on the DEV stack only, they reach prod with the next backend release."; S\_ZOM566 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3643/title): "Collect&amp;Win Analytics"; S\_ZOM552 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3628/title): "Season Pass Analytics"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Which beats get notes. |
| writes | DIFFERENT | One Linear note versus three. |
| destinations | DIFFERENT | ZOM-566 and ZOM-552 added. |
| contents | DIFFERENT | Extra note contents. |

Resolution relevance challenge: The prompt's 'can't run yet' is not the brief's 'Hold'; no record defines it or names a Collect &amp; Win or Season Pass ticket for notes.
Delegation challenge: NOT_CLAIMED. No source delegates the call or accepts both outcomes.
Challenge evidence: SP (Evals/task\_inputs/04\_Prompt.txt): "for each beta push, whether it goes out or waits, and if it waits, what's missing."; S\_ARTHUR470 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Server-side windows for Collect &amp; Win are still on the DEV stack only, they reach prod with the next backend release."; S\_ZOM566 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3643/title): "Collect&amp;Win Analytics"; S\_ZOM552 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/linear/data.json pointer /issues/3628/title): "Season Pass Analytics"

Compared alternative: F
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. The brief starts a beat at the first window after its server windows are live on prod, 'not when its client PRs merged'. The Season Pass spec cites only client builds for 'reached production'; Julia's calendar event says 'The live-ops server windows go live with this release' (Oct 8). Whether Season Pass server windows were already live, so the October season counts, has no settling record.
Resolution evidence: S\_BRIEF\_START (Evals/task\_inputs/01\_Universe\_Inject.sql): "A beat starts with the first window that opens after its server windows are live on prod, the backend release instant read in UTC, not when its client PRs merged. Collect &amp; Win runs Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC, so a window the release instant pre-empts does not count."; S\_GCAL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Prod backend deploy for the beta. The live-ops server windows go live with this release; release window 18:00-19:00 Istanbul time."; S\_SPSPEC\_PROD (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/confluence/confluence\_working.json pointer /pages/20/body): "Android 0.3.127 published Sep 22, iOS 0.3.49 released Sep 29"; S\_ARTHUR438 (Evals/task\_inputs/01\_Universe\_Inject.sql): "The Season Pass premium strip needs to move to the November range rather than the current one"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | October season in or out of the calendar. |
| writes | DIFFERENT | Season Pass row windows differ. |
| destinations | SAME | Same sheet. |
| contents | DIFFERENT | First window Oct 6 vs Nov 1. |

Resolution relevance challenge: Arthur's 'rather than the current one' implies a current range in the client, not server windows on prod; the spec's build numbers are client builds the brief says not to use.
Delegation challenge: NOT_CLAIMED. No source delegates the call or accepts both outcomes.
Challenge evidence: S\_BRIEF\_START (Evals/task\_inputs/01\_Universe\_Inject.sql): "A beat starts with the first window that opens after its server windows are live on prod, the backend release instant read in UTC, not when its client PRs merged. Collect &amp; Win runs Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC, so a window the release instant pre-empts does not count."; S\_GCAL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Prod backend deploy for the beta. The live-ops server windows go live with this release; release window 18:00-19:00 Istanbul time."; S\_SPSPEC\_PROD (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/confluence/confluence\_working.json pointer /pages/20/body): "Android 0.3.127 published Sep 22, iOS 0.3.49 released Sep 29"; S\_ARTHUR438 (Evals/task\_inputs/01\_Universe\_Inject.sql): "The Season Pass premium strip needs to move to the November range rather than the current one"

Compared alternative: G
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. Samuel says the frame 'went out ... in submission 135', but \#135 is an Android submission build on Sep 30, iOS is not mentioned and the UA plan waits for store approval. The brief says 'Not what already shipped' and 'an unverified build or platform is a still-to-do'; nothing says whether a submitted Android build counts as shipped.
Resolution evidence: S\_SAMUEL471 (Evals/task\_inputs/01\_Universe\_Inject.sql): "The daily-gift frame went out with this PR — it is in submission 135, so that one can be closed."; S\_BUILD135 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C05433XK267/2025-09.json pointer /1124/attachments/0/fallback): "Match3D Android Submission - \#135 - main  Success after 1 hr 28 min"; S\_BRIEF\_UNVER (Evals/task\_inputs/01\_Universe\_Inject.sql): "An established failure holds it; an unverified build or platform is a still-to-do, not a hold."; S\_SLIDES\_STORES (Evals/task\_inputs/01\_Universe\_Inject.sql): "Scaled beta-cohort buy, starting once the stores approve the Sep 30 builds."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | Frame shipped vs still to do. |
| writes | DIFFERENT | Still-to-do cell filled or empty. |
| destinations | SAME | Same sheet. |
| contents | DIFFERENT | Different still-to-do contents. |

Resolution relevance challenge: Samuel's newer comment speaks to the frame but only for one Android submission; the brief's unverified-platform rule speaks to that case without saying which side a submitted build is on.
Delegation challenge: NOT_CLAIMED. No source delegates the call or accepts both outcomes.
Challenge evidence: S\_SAMUEL471 (Evals/task\_inputs/01\_Universe\_Inject.sql): "The daily-gift frame went out with this PR — it is in submission 135, so that one can be closed."; S\_BUILD135 (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C05433XK267/2025-09.json pointer /1124/attachments/0/fallback): "Match3D Android Submission - \#135 - main  Success after 1 hr 28 min"; S\_BRIEF\_UNVER (Evals/task\_inputs/01\_Universe\_Inject.sql): "An established failure holds it; an unverified build or platform is a still-to-do, not a hold."; S\_SLIDES\_STORES (Evals/task\_inputs/01\_Universe\_Inject.sql): "Scaled beta-cohort buy, starting once the stores approve the Sep 30 builds."

Decision sweep: The prompt applies the brief's push rule to each beta push ('for each beta push, whether it goes out or waits') and the hold and start rules to each beat.
Decision rule: S\_BRIEF\_PUSH (Evals/task\_inputs/01\_Universe\_Inject.sql): "A push goes out only if its row is Ready and LIVE and its English copy names the game only as Zombie Match 3D and events only by their ZM3D names. Anything else is held, with what is missing. Beta pushes are English-only (UK and US buys); the translated tab is the old Domino set still waiting on ZM3D localization."; S\_BRIEF\_HOLD (Evals/task\_inputs/01\_Universe\_Inject.sql): "Hold a beat only when players provably cannot enter, score or claim on prod even after a restart."; S\_BRIEF\_START (Evals/task\_inputs/01\_Universe\_Inject.sql): "A beat starts with the first window that opens after its server windows are live on prod, the backend release instant read in UTC, not when its client PRs merged. Collect &amp; Win runs Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC, so a window the release instant pre-empts does not count."

| Item | Outcome | Basis | Settled by / gap |
|---|---|---|---|
| Push row 1 Quests rollover (Push Notification, Not Ready, LIVE) | waits: row not marked Ready | RECORD | S\_PUSH1 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/1): ""Not Ready", "Quests", "Push Notification ", "Rollover""; S\_BRIEF\_PUSH (Evals/task\_inputs/01\_Universe\_Inject.sql): "A push goes out only if its row is Ready and LIVE and its English copy names the game only as Zombie Match 3D and events only by their ZM3D names. Anything else is held, with what is missing. Beta pushes are English-only (UK and US buys); the translated tab is the old Domino set still waiting on ZM3D localization." |
| Push row 2 Hourly Coins (Local Notification, Not Ready, LIVE) | listed and waiting (A/B) vs left out as not a push (C) | BOUNDARY | Edge: Local Notification row: outside the term 'push' if a push is only a Push Notification. Not settled; tested as A vs C |
| Push row 3 Lives recharged (Local Notification, Ready, LIVE, copy names no game) | goes out (A) vs waits (B) vs left out (C) | BOUNDARY | Edge: copy lacks the game name the rule assumes every row has; also a Local Notification. Not settled; tested as A vs B |
| Push row 4 1 Days Lapsed (Local Notification, Ready, LIVE, copy says Puzzles vs Zombies) | listed and waiting (A/B) vs left out (C) | BOUNDARY | Edge: Local Notification row: outside the term 'push' if a push is only a Push Notification. Not settled; tested as A vs C |
| Push row 5 7 Days Lapsed (Local Notification, Ready, LIVE, copy names no game) | goes out (A) vs waits (B) vs left out (C) | BOUNDARY | Edge: copy lacks the game name the rule assumes every row has; also a Local Notification. Not settled; tested as A vs B |
| Push row 6 FTUE first mission (Local Notification, Ready, LIVE, copy says Puzzles vs Zombies) | listed and waiting (A/B) vs left out (C) | BOUNDARY | Edge: Local Notification row: outside the term 'push' if a push is only a Push Notification. Not settled; tested as A vs C |
| Push row 7 Win &amp; Collect event start (Push Notification, Not Ready, WIP) | waits: Not Ready, WIP, copy uses the Domino name | RECORD | S\_PUSH7 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/7): ""Not Ready", "Event", "Push Notification", "Event Start (server time)", "Win &amp; Collect event start", "Everyone", "Main Menu", "WIP""; S\_BRIEF\_PUSH (Evals/task\_inputs/01\_Universe\_Inject.sql): "A push goes out only if its row is Ready and LIVE and its English copy names the game only as Zombie Match 3D and events only by their ZM3D names. Anything else is held, with what is missing. Beta pushes are English-only (UK and US buys); the translated tab is the old Domino set still waiting on ZM3D localization." |
| Push row 8 Nathan's Treasure Hunt event start (Push Notification, Not Ready, WIP; Domino-only event) | listed and waiting (A) vs left out (D) | BOUNDARY | Edge: row with no ZM3D beat in a tab whose plan has a Beat column. Not settled; tested as A vs D |
| Push row 9 Plague Race event start (Push Notification, Ready, WIP) | waits: status WIP, not LIVE | RECORD | S\_PUSH9 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/9): ""Ready", "Event", "Push Notification", "Event Start (server time)", "Plague Race", "Everyone", "Main Menu", "WIP""; S\_BRIEF\_PUSH (Evals/task\_inputs/01\_Universe\_Inject.sql): "A push goes out only if its row is Ready and LIVE and its English copy names the game only as Zombie Match 3D and events only by their ZM3D names. Anything else is held, with what is missing. Beta pushes are English-only (UK and US buys); the translated tab is the old Domino set still waiting on ZM3D localization." |
| Push row 10 Streak Fever event start (Push Notification, Not Ready, WIP; Domino-only event) | listed and waiting (A) vs left out (D) | BOUNDARY | Edge: row with no ZM3D beat. Not settled; tested as A vs D |
| Push row 11 Axe Arena event start (Push Notification, Not Ready, WIP; Domino-only event) | listed and waiting (A) vs left out (D) | BOUNDARY | Edge: row with no ZM3D beat. Not settled; tested as A vs D |
| Push row 12 Login Calendar update (Push Notification, Not Ready, WIP) | waits | RECORD | S\_PUSH12 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/12): ""Not Ready", "Event", "Push Notification", "Daily/Monthly Rollover", "Login Calendar update""; S\_BRIEF\_PUSH (Evals/task\_inputs/01\_Universe\_Inject.sql): "A push goes out only if its row is Ready and LIVE and its English copy names the game only as Zombie Match 3D and events only by their ZM3D names. Anything else is held, with what is missing. Beta pushes are English-only (UK and US buys); the translated tab is the old Domino set still waiting on ZM3D localization." |
| Push row 13 Season Pass activation (Push Notification, Not Ready, WIP) | waits | RECORD | S\_PUSH13 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/13): ""Not Ready", "Event", "Push Notification", "Season Start or Milestone", "Season Pass activation or reward unlock""; S\_BRIEF\_PUSH (Evals/task\_inputs/01\_Universe\_Inject.sql): "A push goes out only if its row is Ready and LIVE and its English copy names the game only as Zombie Match 3D and events only by their ZM3D names. Anything else is held, with what is missing. Beta pushes are English-only (UK and US buys); the translated tab is the old Domino set still waiting on ZM3D localization." |
| Push row 14 Weekly Leaderboard reset (Push Notification, Ready, WIP) | waits: status WIP, not LIVE | RECORD | S\_PUSH14 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/14): ""Ready", "Event", "Push Notification", "Weekly Rollover", "Weekly Leaderboard reset", "Everyone", "Main Menu", "WIP""; S\_BRIEF\_PUSH (Evals/task\_inputs/01\_Universe\_Inject.sql): "A push goes out only if its row is Ready and LIVE and its English copy names the game only as Zombie Match 3D and events only by their ZM3D names. Anything else is held, with what is missing. Beta pushes are English-only (UK and US buys); the translated tab is the old Domino set still waiting on ZM3D localization." |
| Beat Collect &amp; Win | not held; first window Fri Oct 10 00:00 UTC (Wed Oct 8 window pre-empted by the 15:00 UTC release) | RECORD | S\_ARTHUR470 (Evals/task\_inputs/01\_Universe\_Inject.sql): "Server-side windows for Collect &amp; Win are still on the DEV stack only, they reach prod with the next backend release."; S\_GCAL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Prod backend deploy for the beta. The live-ops server windows go live with this release; release window 18:00-19:00 Istanbul time."; S\_BRIEF\_START (Evals/task\_inputs/01\_Universe\_Inject.sql): "A beat starts with the first window that opens after its server windows are live on prod, the backend release instant read in UTC, not when its client PRs merged. Collect &amp; Win runs Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC, so a window the release instant pre-empts does not count."; S\_CDK\_WAC (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d-backend/zombies-game-cdk/lib/zombies-game-cdk-stack.ts): "WIN\_AND\_COLLECT\_GROUP\_3\_SCHEDULE: props.production<br>          ? "0 0 \* \* 5,6,0"" |
| Beat Weekly Leaderboard | held: reset fails on prod after restart | RECORD | S\_VINCENT (Evals/task\_inputs/01\_Universe\_Inject.sql): "Re-tested the weekly leaderboard on the current prod build: it still does not start a new week. I killed the app and reopened it twice, played a few levels, and my week is still last week one. Same on the second device."; S\_BRIEF\_HOLD (Evals/task\_inputs/01\_Universe\_Inject.sql): "Hold a beat only when players provably cannot enter, score or claim on prod even after a restart." |
| Beat Season Pass October season | runs Oct 6-31 (A) vs not counted, first window Nov 1 (F) | SILENCE | No record; tested as A vs F |
| Collect &amp; Win ticket note | no note, not held (A) vs note on its ticket as a beat that can't run yet (E) | SILENCE | No record; tested as A vs E |
| Daily-gift frame still-to-do | shipped, nothing to land (A) vs still to do for iOS / store approval (G) | SILENCE | No record; tested as A vs G |
| Beat Season Pass Season 2 | opens Sat Nov 1 00:00 UTC; Brian's Fri Oct 31 07:00 UTC config handoff misses the Oct 31 00:00 UTC lock, moves earlier and Brian is told | RECORD | S\_SPSPEC\_LOCK (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/confluence/confluence\_working.json pointer /pages/20/body): "Season config (tiers, rewards, theme) is authored in the live-ops tool and locked 24h before each season opens"; S\_BRIAN\_FIX (Evals/task\_inputs/01\_Universe\_Inject.sql): "the November Season Pass config handoff moves from Wed Oct 29 to Fri Oct 31, 10:00 Istanbul time."; S\_BRIEF\_LOCK (Evals/task\_inputs/01\_Universe\_Inject.sql): "Every config a beat needs lands before its lock, read in server time (UTC). A committed date that misses the lock moves earlier and its owner is told."; S\_CDK\_SP (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d-backend/zombies-game-cdk/lib/zombies-game-cdk-stack.ts): "SEASON\_PASS\_SCHEDULE: props.production ? "0 0 1 \* \*" : "\*/30 \* \* \* \*"" |
| Halloween one-off | off the calendar: Product (Robert) pulled his approval | RECORD | S\_ROBERT\_PULL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Coming back on the Halloween one-off: pulling my ok. Take it off the beta calendar, we are not spending art time on a theme we may not ship at all. Sorry for the flip, my later word on this one is the one that counts."; S\_SPSPEC\_OWNER (Universe\_SynthCut/SynthCut\_HarmonyGames\_Other\_Services/Services\_Data/confluence/confluence\_working.json pointer /pages/20/body): "Owner: Robert (Product)."; S\_BRIEF\_ONEOFF (Evals/task\_inputs/01\_Universe\_Inject.sql): "A one-off may take a recurring beat slot only with Product latest dated approval, and if he takes that back his later word is the one that counts." |
| Boss Arena | off the calendar | RECORD | S\_BRIEF\_SCOPE (Evals/task\_inputs/01\_Universe\_Inject.sql): "Boss Arena is off this calendar until the pivot call." |
| Plague Race | not held; daily 00:00 UTC windows | RECORD | S\_CDK\_PR (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d-backend/zombies-game-cdk/lib/zombies-game-cdk-stack.ts): "PLAGUE\_RACE\_SCHEDULE: props.production ? "0 0 \* \* \*" : "0 \*/2 \* \* \*"" |
| Endless Monster Mode resets | not held; weekly reset Monday 00:00 UTC (plus daily) | RECORD | S\_CDK\_EM (Universe\_SynthCut/SynthCut\_HarmonyGames\_GitHub/Services\_Data/github/root/harmonygames-Games/match3d-backend/zombies-game-cdk/lib/zombies-game-cdk-stack.ts): "ENDLESS\_MONSTER\_WEEKLY\_SCHEDULE: props.production<br>          ? "0 0 \* \* 1"" |
| Quests rollover | in from the Mon Oct 13 rollover; push not Ready | RECORD | S\_TRELLO (Evals/task\_inputs/01\_Universe\_Inject.sql): "Putting the new quest set in with the Mon Oct 13 rollover."; S\_BRIEF\_ROLL (Evals/task\_inputs/01\_Universe\_Inject.sql): "For quest and login-calendar rollovers put down whether the beat is in and whether its push is ready, not its window dates."; S\_PUSH1 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/1): ""Not Ready", "Quests", "Push Notification ", "Rollover"" |
| Login calendar / daily gift rollover | in; counter display is cosmetic, not a hold; push not Ready | RECORD | S\_ZOM556 (Evals/task\_inputs/01\_Universe\_Inject.sql): "The counter display on the main menu is cosmetic, the streak itself is fine."; S\_BRIEF\_ROLL (Evals/task\_inputs/01\_Universe\_Inject.sql): "For quest and login-calendar rollovers put down whether the beat is in and whether its push is ready, not its window dates."; S\_PUSH12 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/12): ""Not Ready", "Event", "Push Notification", "Daily/Monthly Rollover", "Login Calendar update"" |

Strongest-alternative challenge (B): B rests only on the rule's own wording ('names the game only as Zombie Match 3D') and keeps the same 14-row set, so it is the narrowest defensible change; C is also retained because the sheet's own What column separates Push from Local Notification.
Challenge evidence: S\_BRIEF\_PUSH (Evals/task\_inputs/01\_Universe\_Inject.sql): "A push goes out only if its row is Ready and LIVE and its English copy names the game only as Zombie Match 3D and events only by their ZM3D names. Anything else is held, with what is missing. Beta pushes are English-only (UK and US buys); the translated tab is the old Domino set still waiting on ZM3D localization."; S\_PUSH3 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/3): ""Ready", "Core Game", "Local Notification ", "Rollover", "When lives are recharged", "Everyone", "Main Menu", "LIVE", "Full Ammo Reloaded! 🔫", "Your energy is fully charged! The zombies are closing in—jump back into the battle now and show them who's boss. 🧟⚔️""; S\_PUSH5 (/tmp/hgs/push\_sheet\_220.json pointer /sheets/1/grid/5): ""Ready", "LAPSED", "Local Notification ", "7 Days Lapsed", "Has not played in seven days.", "7d lapse since last session", "Main Menu", "LIVE", "They’ve Taken Over… Can You Stop Them? 😱", "It’s been a while, survivor. The undead are stronger than ever. Rally your gear and get back into the fray before it’s too late! 🧟‍♀️💥""

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

**Feasibility:** PASS (5). Every ask maps to cataloged reads/writes (GSheets update, Linear comment, Slack send). Windows are derivable from the CDK cron schedules plus the brief's start rule; the release instant is on Julia's calendar. No breakdown lacks a field. Nothing needs precision the tools lose.

**Persona ACL Reachability:** PASS (5). Every scoped read the answer needs is reachable: Frederick DM D05SD5QLG94 (member), Robert DM D05GU6L0XFH (member), #zombie-match3d C0880U9751A and #zombie-art C08R8CHB0QL (member), brief / slides / push sheet shared with Julia, her own sheet, mailbox (Brian's emails delivered to Julia) and calendar (event on julia.lawson@harmonygames.co). The #zombie-prs mirrors (Julia not a member) duplicate GitHub comments that are unscoped.

**Truthfulness:** PASS (5). Premises verified: Frederick's ask (DM `8b090dec…`), "four buy weeks that start Monday the 6th" (slides W1–W4; Oct 6, 2025 is a Monday), brief shared with Julia, "my live-ops calendar sheet" (Julia-owned), beta pushes ("PNs Beta" tab), "the calendar ticket" (ZOM-78 + `cmt_zom78_1`). Nothing treated as done sits after the clock.

**Tool Use & Cross-service:** PASS (5). Graded facts come from GitHub (C&W server windows on DEV; cron windows; PR still-to-do comments), Slack (leaderboard re-test; Halloween retraction), Gmail (Oct 31 handoff), Confluence (24h lock; Robert is Product), GCal (release instant) and Sheets (push rows). Dropping any one changes the answer.

**Investigation + Action:** PASS (5). Discovery feeds the sheet, the ticket notes, the link and the DM.

**Clarity & Specificity:** FAIL (2): Action Decision Ambiguity on the same push-plan fork. Rows 3 and 5 are sent or held, and rows 2–6 are listed or left out. The Pushes tab writes differ (Eval 1 §2.6 decision-sweep forks; no Non-Fail band applies when writes differ).

**Contrived / Unnatural:** FAIL (2). AI-text red flag "enumerated deliverable specs" (§1.2, local override 2026-10-05: any red flag fails; scoring.json names "enumerated deliverable specs" under this row). The spec-sheet escalation (two triggers) is not needed. Other rows are clean: no opaque IDs or timestamps, no trap hint, no hidden destination ("send Frederick" and the DM's "back here" agree), no if-chain, no staged errors.

**Alignment with Today's Date:** PASS (5). "Monday the 6th" resolves to Mon Oct 6, 2025 (DM and slides). All work is future-dated against the Oct 1 clock; nothing future is treated as past.

**Originality / Sample Similarity:** N/A (no comparison samples supplied; library similarity handled in STEP 0.6).

**Coherence (Bolt-on):** PASS (5). **Business Function:** PASS (5): Product persona doing GTM planning for her title, a clear Product scenario.

## Phase 3: Universe Feasibility

**Data Existence:**
- Entities verified: 6 of 6 premises; all beats' windows and states have source records (decision sweep).
- All retrievable via MCP: Yes.

**Cross-Service Coherence:** NON-FAIL (3)
- One minor inconsistency (deep recheck P2 DR1, confirmed): Brian's injected handoff emails say "Season 2 opens on Sat Nov 1", while base Confluence `page_season_pass_spec` has the pass reaching production in the week of Sep 22–29 with "production seasons reset monthly on the 1st at 00:00 UTC". So an October season opened Oct 1 and Nov 1 would be at least the third season (or the second, if the September launch isn't counted). It is a season label only: the cron windows (`SEASON_PASS_SCHEDULE "0 0 1 * *"`) are the same either way. Fix: drop "Season 2" from both emails or make it "the November season".
- No other inconsistencies. The overlaps are designed and correctly dated: ZOM-429's Sep 23 comment against Vincent's Sep 30 re-test; ZOM-465 against Marcus's #454; ZOM-432 against Samuel's #471. The Confluence calendar's "There is no technical content lock" sits next to the Season Pass spec's "locked 24h before each season opens", and the calendar page reconciles them itself ("The 24h season-pass freeze in the Season Pass spec is a process control on top of that"). Confluence "Weekly Leaderboards … Live" is a slot status, not a claim that the reset works.
- Known base-data issues (not scored): Confluence engine page "the July 2025 outage … nothing in the record yet marks it restored" (Domino Delights only; keep the rubric and OEs off it). Eval 0 A8 Linear areas (SC-15 ZOM-521/526, SC-38 ZOM-552, SC-16 ZOM-565) aren't graded by this prompt; keep the rubric and OEs off them.
- Injection SQL considered: Yes.
- Static integrity evidence: REUSED from `0_injection.md` (injection-static-v2 PASS / COMPLETE, same SQL SHA): checks A–C, all IDs unique, Slack authors are channel members, apostrophes doubled.
- Prompt-specific sources, access and configuration: supported (no error/async config).

## Phase 4: Final Evaluation

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|-----------|--------------|-------------|---------------|
| Prompt | Unique Ground Truth | 2 | Push-plan fork on rows 2–6 of "PNs Beta" (game-name edge and push vs local notification), unsettled by any record |
| Prompt | Feasibility | 5 | All asks doable with cataloged tools and existing data |
| Prompt | Persona ACL Reachability | 5 | Every scoped read reachable by Julia |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 2 | Action Decision Ambiguity on the same fork (Pushes tab writes differ) |
| Prompt | Contrived / Unnatural | 2 | Enumerated deliverable specs restating the DM |
| Prompt | Alignment with Today's Date | 5 | Resolves to Oct 6, 2025; no contradiction |
| Prompt | Originality / Sample Similarity | N/A | No samples supplied |
| Prompt | Truthfulness | 5 | All six premises verified |
| Prompt | Tool Use & Cross-service | 5 | Six services each change a graded fact |
| Prompt | Investigation + Action | 5 | Findings drive four write kinds |
| Prompt | Coherence (Bolt-on) | 5 | One workflow |
| Prompt | Persona | 5 | PM leading live-ops design |
| Prompt | Business Function | 5 | Product |
| Prompt | Assigned Competency | 5 | Marketing and GTM |
| Prompt | Assigned Task Skill | 5 | Planning and decision support |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three dimensions load-bearing; short trigger |
| Universe | Data Exists | 5 | All needed records exist and are reachable |
| Universe | Cross-Service Coherence | 3 | One minor season-label mismatch (Brian's "Season 2" vs the spec's monthly seasons since late September) |

## Issues Found

| # | Issue | Severity | Dimension |
|---|-------|----------|-----------|
| 1 | Push rule edge: "PNs Beta" rows 3 (Lives recharged, "Full Ammo Reloaded!") and 5 (7 Days Lapsed, "They’ve Taken Over…") are Ready + LIVE but their copy names no game. The brief's "names the game only as Zombie Match 3D" doesn't say whether that passes, so whether they go out or wait has no settling record | Major | Unique Ground Truth; Clarity |
| 2 | Push set scope: "PNs Beta" mixes "Push Notification" (rows 1, 7–14) and "Local Notification" (rows 2–6) rows. Every Ready + LIVE row is a Local Notification, and nothing says whether local notifications are "beta pushes" | Major | Unique Ground Truth; Clarity |
| 3 | The prompt restates the per-row deliverable fields of Frederick's DM | Major | Contrived / Unnatural |
| 4 | Domino-only rows on "PNs Beta" (Nathan's Treasure Hunt, Streak Fever, Axe Arena, Hourly Coins) have no ZM3D beat; listed as waiting or left out is unsettled (your Pushes tab has a Beat column) | Major | Unique Ground Truth |
| 5 | "If a beat can't run yet" could mean held only (ZOM-429) or also Collect & Win (server windows on DEV until Oct 8) and Season Pass (config still to land), whose only tickets are the analytics tickets ZOM-566 / ZOM-552 | Major | Unique Ground Truth; Clarity |
| 6 | Season Pass October season: the brief starts a beat only once its server windows are live, the spec cites only client builds for "reached production", and Julia's Oct 8 event says "The live-ops server windows go live with this release". So the October season either counts (Oct 6–31) or doesn't (first window Nov 1) | Major | Unique Ground Truth |
| 7 | Daily-gift frame: Samuel says it "went out … in submission 135", but #135 is an Android submission build (Sep 30), iOS isn't mentioned and the stores haven't approved the builds. Shipped vs still to do is unsettled under the brief's "unverified build or platform is a still-to-do" | Major | Unique Ground Truth |
| 8 | Brian's emails call the Nov 1 season "Season 2"; the spec's monthly seasons since late September make it at least the third | Minor | Cross-Service Coherence |

## Recommended Improvements

1. **Settle each fork in the data, not the prompt** (one dated, persona-visible record each; then rerun /injection and /prompt):
   - Push plan: say whether Local Notification rows count as beta pushes, whether copy that names no game passes, and whether the Domino-only rows (Treasure Hunt, Streak Fever, Axe Arena, Hourly Coins) are listed or dropped.
   - Ticket notes: say whether "can't run yet" means held only, and if not, name the Collect & Win and Season Pass tickets.
   - Season Pass: say whether its server windows are already on prod, i.e. whether the October season counts.
   - Daily-gift frame: add a record that settles it (an iOS submission or approval line, or a line saying an Android-only submission isn't shipped).

   On the push fork specifically: (then rerun /injection and /prompt). Add one dated, persona-visible record from Frederick (a short brief edit or a DM reply) that states two things: whether the Local Notification rows on "PNs Beta" count as beta pushes, and whether copy that names no game passes the naming rule. Alternatively, change the sheet so the edge disappears: give rows 3 and 5 copy that either names Zombie Match 3D or names another game. If you edit the sheet, note it's base gsheets data, so the change has to come through injection on a Sheets row your SQL owns.
2. **Cut the field list from the prompt.** The DM already lists the per-beat fields, so the prompt can point to Frederick's ask instead of repeating it. Prompts are screened for AI-written text, so write the replacement sentence in your own voice.
3. **Same scenario note:** the nearest library task (0.726) is also a Julia → Frederick ZM3D live-ops slot plan. Your four-week buy window, push plan and hold/lock rules already differ. Keep it that way, and avoid reusing that task's Oct 13 – Dec 31 framing.
4. **Advisories (not scored):** the injected sheet row `f_e4a17c90…` has no `web_view_link` (base Drive rows carry one), so the agent has to build the link from the ID for ZOM-78. Robert's Halloween retraction is threaded under an unrelated DM question, so it's findable only by search or thread expansion. The brief's "Aug-Sep live-ops cohort" is undefined, but no change-request review exists in Aug–Sep, so no item turns on it. "Moves earlier" for Brian's handoff is bounded by the lock (any time before Oct 31 00:00 UTC). How Brian is "told" is open (same recipient, minor).
5. **Fix the season label:** change "Season 2" in Brian's two emails to "the November season" (or align it with the spec).

## Deep Recheck

Passes: P1, P2, P3, P4, Opus 5.5 (claude-opus-5-5), session effort, each blind to the main review (fresh subagents given only the saved inputs, SEARCH.md, persona references, common_errors.md and deep_recheck.md).

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 7 prompt sentences + 25 brief rule sentences; 30 fork lines | 13 | 7 |
| P2 | 7 sentences | 4 | 1 |
| P3 | 7 sentences | 1 | 0 |
| P4 | 7 sentences | 3 | 1 (DR1 + DR2 merged) |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| P1-DR4 | P1 | "Do the push plan the same way — for each beta push…" | gsheets #220 PNs Beta rows 3, 5 (Ready, LIVE, copy names no game) | §2 what gets written | Unique Ground Truth | CONFIRMED | Same as main fork B; no record on copy without a game name |
| P1-DR3 | P1 | same | PNs Beta rows 2–6 "Local Notification"; rows 2, 8, 10, 11 Domino-only (Confluence calendar lists Streak Fever, Axe Arena, Nathan's Treasure Hunt as "Domino Delights") | §2 which items | Unique Ground Truth | CONFIRMED | Forks C and D; nothing rules on local or Domino-only rows |
| P1-DR8 | P1 | "If a beat can't run yet, leave a note on its ticket…" | #470 rc_10 "still on the DEV stack only"; ZOM-566 / ZOM-552 analytics only | §2 which items / destination | Unique Ground Truth | CONFIRMED | Fork E; "can't run yet" undefined, no clean ticket for C&W or Season Pass |
| P1-DR5 | P1 | "work out the windows it runs in" | spec "Android 0.3.127 published Sep 22, iOS 0.3.49 released Sep 29" (client builds); gcal "The live-ops server windows go live with this release" | §2 which date | Unique Ground Truth | CONFIRMED | Fork F; brief excludes client merges, no record puts Season Pass server windows on prod |
| P1-DR10 | P1 | "what still has to land before it runs" | #471 c_18 "in submission 135"; #builds C05433XK267 /1124 "Match3D Android Submission - #135"; UA plan "once the stores approve" | §2 which source wins | Unique Ground Truth | CONFIRMED | Fork G; Android submission only, brief's unverified-platform rule covers the case without ruling which side |
| P1-DR1 | P1 | "For each beat a player can see…" | Confluence calendar: Endless "resets daily … and weekly"; Zombie Lane "Permanent (level-gated reward track)"; PNs Beta row 12 "Login Calendar update"; ZM3D has Daily Gift (ZOM-432, ZOM-556), no login-calendar ticket | §2 which items | Unique Ground Truth | CONFIRMED (in part) | Login calendar identity (F3/F5) open, recorded with fork G's beat. Endless REJECTED: brief "an event window, a reset or a start push" covers its resets. Zombie Lane REJECTED: no window, reset or start push. Local notifications as Calendar "start push" REJECTED: start pushes are the "Event Start (server time)" rows |
| P1-DR2 | P1 | brief "quest and login-calendar rollovers" | PNs Beta row 12 Domino copy; Linear ZOM-432/556 | §2 which items | Unique Ground Truth | CONFIRMED | Merged with P1-DR1 login-calendar fork (F5) |
| P1-DR6 | P1 | brief "A committed date that misses the lock moves earlier" | spec "locked 24h before each season opens"; Brian "moves from Wed Oct 29 to Fri Oct 31, 10:00 Istanbul time" | §2 which date | Unique Ground Truth | REJECTED | The brief sets the boundary itself ("lands before its lock"); any date before Oct 31 00:00 UTC satisfies it, so it's an acceptance boundary, not two answers. Channel for telling Brian = same recipient, minor clarity only |
| P1-DR7 | P1 | "whether it's held and until when" | ZOM-429 state Backlog, no due date; Vincent re-test Sep 30 | §2 which date | Unique Ground Truth | REJECTED | Reading B (until the Oct 8 release) has no supporting record: the release event names no leaderboard fix, and ZOM-429 sits in Backlog with no date. The only supported content is "held, no fix date on record" |
| P1-DR9 | P1 | "who owns that" | #370 rc_1 "Claire has those on her list" | §2 per item | Unique Ground Truth | REJECTED | The record itself says the art owner has the sprites on her list, which meets "player-facing art an owner has flagged" |
| P1-DR11 | P1 | "what still has to land" | Trello "Putting the new quest set in with the Mon Oct 13 rollover" | §2 per item | Unique Ground Truth | REJECTED | Brief: for quest rollovers "put down whether the beat is in and whether its push is ready, not its window dates"; the Oct 13 set is when the beat is in, settled by the Trello record |
| P1-DR12 | P1 | "send Frederick your recommendation with the trade-offs" | DM "I need your call, not a list of what we have" | §2 contents | Clarity | REJECTED | Open-ended recommendation; the DM sets the acceptance boundary (a call with trade-offs); no write differs |
| P1-DR13 | P1 | brief "Aug-Sep live-ops cohort" | GitHub reviews: no CHANGES_REQUESTED Aug–Sep 2025; #438 rev_4 "COMMENTED" | §2 rule term | Clarity | REJECTED | No item turns on the undefined term (same material result) |
| P2-DR1 | P2 | "work out the windows it runs in" | Gmail Brian "Season 2 opens on Sat Nov 1" vs spec "production seasons reset monthly on the 1st" after a Sep 22–29 launch | P2 date-slip | Cross-Service Coherence | CONFIRMED | Label-only mismatch; windows unchanged → one minor inconsistency |
| P2-DR2 | P2 | "leave a note on its ticket" | ZOM-566 / ZOM-552 | §6.5 | Feasibility | REJECTED | Folded into fork E (UGT), not a separate feasibility defect: the held beat's ticket exists |
| P2-DR3 | P2 | "link it on the calendar ticket" | drive_files f_e4a17c90… web_view_link NULL | §6.5 | Feasibility | REJECTED | Link can be built from the file ID; advisory only |
| P2-DR4 | P2 | "for each beat…" | Slack D05GU6L0XFH reply 58d06bd5… under an unrelated parent | §3 hidden record | Cross-Service Coherence | REJECTED | Julia is a member and the reply is searchable; placement oddity (Eval 0 A5), no value conflict |
| P3-DR1 | P3 | n/a (SQL) | schema snapshot lacks extras_json, drive_id, seq and others | §6.8 | Injection | REJECTED | Already Eval 0 advisory A1; the snapshot is unverified, so this is not a demonstrated defect |
| P4-DR1/DR2 | P4 | "work out the windows it runs in, whether it's held and until when, the push that goes with it, and what still has to land before it runs and who owns that." / "whether it goes out or waits, and if it waits, what's missing." | prompt text vs DM 8b090dec… field list | §1.2 / §2.7 | Contrived or Unnatural Prompt | CONFIRMED | "Enumerated deliverable specs" red flag; any red flag fails (local override 2026-10-05) |
| P4-DR3 | P4 | em-dash asides | prompt text | §1.2 | Contrived or Unnatural Prompt | REJECTED | Clean punctuation is not a red flag on its own |

Effect on verdict: Unique Ground Truth stays FAIL (2), with forks D–G added to the record. Clarity stays FAIL (2). Contrived FAIL (2) confirmed. Cross-Service Coherence 5 → 3. Overall FAIL 2.

- F1: Push rows 3 (Lives recharged) and 5 (7 Days Lapsed) go out / wait | A: go out (Ready, LIVE, no wrong name) | B: wait (copy never names Zombie Match 3D) | Missing: a dated record from Frederick saying whether copy that names no game passes the naming rule
- F2: Local Notification rows 2–6 in / out of the push plan | A: all 14 PNs Beta rows | B: only Push Notification rows 1, 7–14 | Missing: a record saying whether local notifications are beta pushes
- F3: Domino-only rows 2, 8, 10, 11 listed / dropped | A: listed as waiting | B: dropped (no ZM3D beat; Pushes tab has a Beat column) | Missing: a record saying how non-ZM3D rows in the beta tab are handled
- F4: Ticket notes for beats that "can't run yet" | A: held beats only (ZOM-429) | B: also Collect & Win and Season Pass (on ZOM-566 / ZOM-552) | Missing: a record defining "can't run yet" and naming those beats' tickets
- F5: Season Pass October season | A: runs Oct 6–31, then Nov 1 | B: not counted; first window Nov 1 00:00 UTC | Missing: a record saying whether Season Pass server windows were live on prod before Oct 8
- F6: Daily-gift frame | A: shipped (#471 "in submission 135") | B: still to do (Android submission only, iOS / store approval unverified) | Missing: an iOS submission or approval record, or a line on whether an Android submission counts as shipped
- F7: Login-calendar beat | A: = ZM3D Daily Gift (in; push row 12 waits) | B: ZM3D has no login calendar (no beat) | Missing: a ZM3D record naming its login calendar
- F8: Weekly Leaderboard held | A: held | B: not held | Settled by: Vincent, #zombie-match3d Sep 30 "it still does not start a new week. I killed the app and reopened it twice"
- F9: Collect & Win first window | A: Fri Oct 10 00:00 UTC | B: Wed Oct 8 / Thu Oct 9 | Settled by: Julia's calendar "release window 18:00-19:00 Istanbul time" (Oct 8 15:00Z) + brief "a window the release instant pre-empts does not count"
- F10: Season 2 config | A: Brian's Oct 31 07:00 UTC misses the lock, moves earlier, Brian told | B: on time | Settled by: spec "locked 24h before each season opens"
- F11: Halloween one-off | A: off | B: on / held | Settled by: Robert "pulling my ok. Take it off the beta calendar" + spec "Owner: Robert (Product)."
- F12: Plague Race / Weekly LB pushes (Ready, WIP) | A: wait | B: go out | Settled by: brief "only if its row is Ready and LIVE"
- F13: Push sheet identity | A: Push Notifications Zombie Match | B: Domino Adventure sheet | Settled by: only the ZM sheet has the Ready/Not Ready Status column the brief's "row is Ready" needs

Platform defects: none

### FINAL VERDICT: FAIL

Score: 2

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Eval version: task-quality-v1

Eval release SHA-256: 81446b85bb68b971bfce06d9d3cf07ad43d923b5702670f206122d1f6d34d53c

Reviewed prompt SHA-256: b5d6559cdf2613b7635345784a4914c7025f440ba4ea12268246e1cfab559770

Review context SHA-256: e83f0270c23e9967fb826a48f9566ae993a5989898b4f49773c588a968d9cc4a

Prompt record SHA-256: 95edff732441a8d9b3d12a703c9c333c057ed7e2e2480a83b82a4c5370a92a85


Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Settle forks F1–F7 with dated, persona-visible records in the injection SQL (or change the push sheet rows so the edges disappear), cut the per-row field list from the prompt in your own words, fix Brian's "Season 2" label. Then rerun /injection, /prompt and /hardness in that order (any /oe or /rubric after that).

Evidence limits: Push-sheet evidence is cited from a verbatim extract of gsheets/data.json /sheets_spreadsheets/220 (source SHA-256 a9cc229c…0a28f); the injection schema snapshot is unverified (Eval 0 A1). None changes a finding.

**Lowest Dimension:** Unique Ground Truth - 2 - seven open forks, led by the push plan (whether any beta push goes out has two defensible answers); Clarity 2 and Contrived 2 also fail.

**Summary:** The scenario is strong: well seeded across Slack, Gmail, GCal, Drive, GitHub, Linear, Trello and Confluence, with real dynamic-change traps, a clean config-lock trap and correct premises. But the brief's push rule and several beat-level calls (ticket-note scope, the Season Pass October window, the daily-gift frame, the login calendar) meet edges no record settles, so the end state isn't unique. The prompt also restates the DM's per-row field list.
