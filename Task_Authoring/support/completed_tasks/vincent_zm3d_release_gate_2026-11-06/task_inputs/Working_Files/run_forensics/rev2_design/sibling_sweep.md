# Sibling Sweep — Cross-Service Coherence (rev2)

**Role:** platform `/prompt` deep-recheck P2 — "injected facts that contradict dated base records the persona can open".
**Universe:** synth-cut · **Clock:** 2025-10-01T07:00Z · persona = Vincent Parker (QA / Game Systems Eng.)
**Subject:** `Task_Authoring/task_inputs/01_Universe_Inject.sql` (159 statements / 300 lines)
**Rule:** CONFLICT only when a dated base record the persona can open says otherwise. Absence ≠ conflict.
**Skipped:** `Task_Authoring/references/known_data_issues/synthcut.md` (SC-1…SC-73), incl. SC-13 Trello list name, SC-19 telemetry versions, SC-38 Season Pass ship date.
**Already reported by the platform (only confirming line ranges):**
- Brian update-path doc, `1.3.24` = "N-1, current store build" → **lines 269, 271, 274** (all three; 270/272 are unnamed "N-2" and are not themselves wrong).
- Leonard "every ZM store submission from now on" (line 225) vs ungated iOS #49 Sep 29 → confirmed by base Season Pass spec "iOS 0.3.49 released Sep 29".
- Arthur #36 review comment (line 291) — fixed.

## Findings

| SQL line | record | claim (quote) | base evidence (pointer + quote) | verdict | decides graded value? | smallest fix |
|---|---|---|---|---|---|---|
| 269 | Update-path doc `f_5e40215b7d4d24b0455412`, iOS row | "1.3.24 (N-1, current store build)" | Confluence `page_season_pass_spec` v2, updated 2025-09-30T17:30Z: "Reached production in the week of September 22-29, 2025 - Android 0.3.127 published Sep 22, **iOS 0.3.49 released Sep 29** at $6.99" | **CONFLICT** | yes — decides the N-1/N-2 update rows and whether 1.3.24 can be installed "from the App Store" | relabel N-1 as **0.3.49 (current App Store build)**; label 1.3.24 as N-2 (Sep 2-3 hotfix) |
| 271 | same doc, Pixel 6 row | "1.3.24 (N-1, current store build)" | same spec: "**Android 0.3.127 published Sep 22**" (= Submission #127) | **CONFLICT** | yes | "0.3.127 (N-1, current store build)" |
| 274 | same doc, repro line | "install 1.3.24 from the App Store, play past level 200" | same spec: App Store serves 0.3.49 since Sep 29; 1.3.24 is the Sep 2-3 hotfix branch (`release/1.3.24_HotFix`, #builds 09-02/09-03) | **CONFLICT** | yes | "install 0.3.49 (the current App Store build)" |
| 270, 272 | same doc, N-2 rows | "N-2 (store build before the hotfix)" | #builds: `release/1.3.24_HotFix` submissions #28/#29/#31/#33 (iOS) and #107/#108/#112/#114 (Android) Sep 2-3; unnamed version, so nothing to contradict | HOLDS | yes | none (but see 269 — N-2 becomes 1.3.24 once N-1 is fixed) |
| 240 | Arthur doc `f_a038a576ca8db6955fae95` | "Since the hotfix train ended on Sep 3, every store submission ... is cut straight from main" | #builds: last `release/1.3.24_HotFix` build 09-03 (#33 iOS, #114 Android); every Submission build 09-06→09-30 shows branch `main` (#34,35,36,37,38,39,40,43,46-50 / #116,118-120,122,126,127,129-131,133,135) | HOLDS | yes (it is the rule that makes "in candidate" computable) | none |
| 240 | Arthur doc | "The auth branch submission jobs are sign-in test builds, not store candidates" | #builds: iOS Submission #41/#42/#44/#45 and Android Submission #128 are on branch `[PERSON_NAME_0120]/auth`, distinct from the `main` candidates | HOLDS | yes | none |
| 241 | Arthur doc | "the iOS posts only ever print the newest change, Android prints the whole list" | #builds 09-30: iOS Submission #50 Success lists one change ("Bump max level for debug menu"); Android Submission #135 Success lists the full list ("Fixing UI Elements on Home screen…") | HOLDS | yes (it is the reason a grep of the Changes block is wrong) | none |
| 241 | Arthur doc | "A submission has exactly what was on main when its job started (the Started line in #builds)" | #builds 09-26 23:07:43 iOS #49 / 23:09:25 Android #133 Started; 09-30 18:43:32 iOS #50 / 18:45:34 Android #135 Started (all `main`) | HOLDS | yes | none |
| 227 | Leonard doc `f_632c44650df44fe252ee59` | "last gate's builds were cut (Android #127 / iOS #40 on Sep 22)" | #builds 09-22 12:30:43 Android Submission #127 Started; 12:32:20 iOS Submission #40 Started | HOLDS | yes | none |
| 225 | Leonard doc | "After the orange juice one on Sunday" | #builds 09-22 12:38/12:39 iOS #40 / Android #127 Success change: "Fix pear and orange juice [Arthur Blake]" (fix cut Mon 09-22; incident before it — no base record dates it) | HOLDS (no contradiction; date itself unverifiable) | no | none |
| 227 | Leonard doc | "ZOM-359 and ZOM-475 stay out" | Linear: ZOM-359 "Phone heating up too much…" (Regression), ZOM-475 "Consecutive glass impact sfx/vfx causes crash on android" (Todo) — both exist | HOLDS | yes | none |
| 258 | `How we gate` tab, 8 quoted titles | e.g. "ZOM-546 Bug: refill algorithm spawns fewer items over time", "ZOM-559 Homing out on android(samsung), sound disappears." | Linear titles match verbatim (ZOM-546, 559, 534, 520, 535, 517, 429, 503) | HOLDS | yes | none |
| 258 | `How we gate` tab, ZOM-503 evidence | "match3d#422" | GitHub match3d #422 "Giving lives in teams fix and Popup animations", merged 2025-09-09T14:39Z (before #127/#40 cut 09-22) | HOLDS | yes | none |
| 83, 84 | cmt_zom536_1 / cmt_zom498_1 | "it's in #471 with the home screen fixes" | GitHub match3d #471 "Samuel/zom 498 536", created 2025-09-29T22:00Z, merged 2025-09-30T15:52Z; head branch `Samuel/ZOM-498-536` | HOLDS (PR existed when posted; merged before #135/#50 Started) | no (art tickets = no call) | none |
| 30 | cmt_zom567_1 | "fix is in match3d-backend #36, merged" | GitHub match3d-backend max base PR = **#35**, so #36 is the next free number; PR #36 created 18:30, merged 18:50 (after the 18:55 comment? no — 18:50 < 18:55) | HOLDS | yes | none |
| 286-299 | backend#36 PR/commit/reviews | commit authored 18:24, PR 18:30, approve 18:42, merge 18:50, Arthur's prod comment 22:35 | ordering is internally consistent and consistent with the Douglas DM at 22:01 | HOLDS | yes | none |
| 87 | cmt_zom293_1 | "the glue + trampoline I'd picked … both gone, 600 coins worth" | Confluence economy page: "Glue (pre-level, one use) 400 Coins", "Trampoline (pre-level, one use) 200 Coins" → 600 | HOLDS | yes (ZOM-293 is in gate scope; 600 is the loss that makes it a Blocker) | none |
| 118 | #zombie-bugs candidate post | "Android Submission #135 and iOS Submission #50, both from main" | #builds 09-30 18:45:34 / 18:43:32 Started, branch `main` | HOLDS | yes | none |
| 119 | Brian reply | "regression matrix green on #135 and #50" (21:10) | #builds: #50 Success 19:15, #135 Success 20:13 — both finished before the sheet (created 20:35) and the reply | HOLDS | yes | none |
| 116, 121 | Vincent re-test posts | "#133 / #49" (Sep 29) and "#135 / #50" (Sep 30) | #builds: #133/#49 Success 09-26 23:20/23:13; #135/#50 Success 09-30 20:13/19:15 | HOLDS | yes | none |
| 121 | Vincent re-test list | "ZOM-506 zombie lane text ok … ZOM-561 low-end black surfaces ok … ZOM-558 weekly board says Level: now" | Linear: ZOM-506 completed 09-22T15:14, ZOM-561 completed 09-30T12:43, ZOM-558 completed 09-23T14:49 — all before #135/#50 Started 18:43 | HOLDS | yes | none |
| 116 | Vincent re-test | "trophy path claim spam is ok now (ZOM-435)" | Linear ZOM-435 completed 2025-09-22T13:53 (before #133/#49 cut 09-26) | HOLDS | yes | none |
| 278 | Trello comment 2 (Leonard) | "trophy path on android #135: tapped claim twice fast and got stuck on the path again … same as ZOM-435" | A #135 regression *after* the 09-29 #133 pass — different build, not a contradiction | HOLDS (watch: it re-opens a "FIXED" symptom on the candidate — intentional) | yes | none |
| 214-218 | gcal go/no-go ×5 | "Friday Oct 3, 2025 9am - 9:30am (PDT)"; start_ts 2025-10-03T16:00Z | Oct 3 2025 is a Friday; 16:00Z = 09:00 PDT | HOLDS | yes | none |
| 141-211 | Gmail invite ×4 | organizer arthur.blake, guests leonard/vincent/brian/robert | Linear+Slack identities: all five are HG staff with those addresses; gcal events' `ical_uid` identical across copies | HOLDS | no | none |
| 120, 122, 123, 125 | D0770ET1HV2 DMs | Vincent↔Brian DM (Turkish bug reports, update-path doc) | slack/channels.json: `D0770ET1HV2` is an `is_im` channel whose members include EMPLOYEE_0012 (Vincent Parker) and EMPLOYEE_0026 (Brian Foster) | HOLDS | yes | none |
| 126 | D079SNE2TL4 DM | "#36 is rolled out to prod too, the container is up. that's the code side" | `D079SNE2TL4` members include EMPLOYEE_0012 (Vincent) + EMPLOYEE_0031 (**Douglas**); text is consistent with Arthur's 22:35 "code deployed, data load not run" | HOLDS | yes (it is the misleading-but-true decoy) | none |
| 116-121 | channel `C08R27X0EAH` | "post the candidates in #zombie-bugs" | slack/channels.json: `C08R27X0EAH` = `zombie-bugs` (private), Vincent/Brian/Arthur are members | HOLDS | yes | none |
| 277-279 | Trello actions on card 79 | board "ZM ROADMAP", card idShort 79 "Fix TECH ISSUES", list "BETA: Sep 30", 2 comments | trello: board `6851a6569f3bf818760632ab` = ZM ROADMAP; card `68d1eb90bef538c7c5c5599d` idShort **79**, name "Fix TECH ISSUES", url `/c/pTbZYXdb/79-fix-tech-issues`; base badges.comments 0 → 2 after insert | HOLDS | yes (the card is the "reuse rule" anchor) | none |
| 277-278 | Trello `data_json.list.name` | "BETA: Sep 30" | base list record name is **"BETA: Oct 10"** (rename history per SC-13 says Sep 30) | WATCH — covered by SC-13, not a new defect | no | optionally omit `list.name` from `data_json` |
| 8, 10, 18, 23, 25-27 | new Linear tickets | "#133/#49", "#135/#50", "Android #135 … Pixel 6", "iOS #50 (iPhone SE)", "iPad (iOS #50)" | all four build numbers exist as Submission jobs; #135 tested on Pixel 6 and #50 on iPhone 13/SE/14 across the seeded rows — mutually consistent | HOLDS | yes | none |
| 8-29 | new Linear ids | ZOM-567…580, ART-793, DES-313, cmt_* ids | base max: ZOM-566, ART-792, DES-312; no id collisions; all referenced base ids (ZOM-237/348/427/429/438/443/449/458/468/473/477/481/483/498/503-506/517/520/534-536/546/554-562/564, ZOM-293, ZOM-434/435, ZOM-359/475) exist with matching titles | HOLDS | yes | none |
| 29 | DES-313 | "Level 214 asks for 3 jars but only 2 jars ever spawn" | No base level-config record exposes per-level goals (GDD is loop-level only; commits show levels authored up to 300) | UNVERIFIABLE | yes (it is the DESIGN row) | none — but keep it out of any "state the exact jar count from the universe" rubric |
| 24 | ZOM-577 | "level_fail event is missing the booster_used param" | Confluence Data Model v2 lists progression family as `begin_level, left_level, oom_in_level`; no `level_fail` documented either way | UNVERIFIABLE (absence only) | no | none |
| 283 | contacts | "QA Lead, Cobalt Playtesting (ZM3D playtests)" | base has only PlaytestCloud evidence (2024 receipts, `#company-playtest` archived Apr 2025); no competing ZM3D vendor | UNVERIFIABLE | no | none |
| 129-139 | vendor email | "sessions on **Puzzles vs Zombies**, TestFlight build 50" | Confluence GDD + Season Pass spec + Release Checklist: ZM3D was "listed as *Puzzles vs Zombies* … until the … **rename on 24 July 2025**" | **CONFLICT (low)** | no (the boss-fight note is duplicative of ZOM-562; not a deciding record) | "Zombie Match 3D" (store name since 24 Jul 2025) |
| 23 | ZOM-576 | "Tier 12 premium reward on iOS #50 is two chests … only one chest lands" | Confluence Season Pass spec, tier table: band **11-20 premium = "Booster bundles + gems"** (no chests anywhere in the premium track); same page also states "**No Season Pass purchase has been recorded yet**" | **CONFLICT (band-level + premise)** | yes — ZOM-576 is the Season Pass reward row on the release ticket | make the missing reward a "booster bundle and gems" (spec wording), or state the tier as "the tier-12 premium bundle" |
| 262-274 | Update-path doc | "iPhone 13 / iOS 18.6", "Pixel 6 / Android 14" | No base device/OS register exists; base QA runbook only requires "one iOS and one Android device" | UNVERIFIABLE (no contradiction) | yes (device/OS columns of the update rows) | none |
| 20, 26 | ZOM-573 / ZOM-579 | "Pixel 6", "iPad" for #135/#50 | none in base | UNVERIFIABLE | no | none |

## Scope coverage log

| surface | rows inspected | depth |
|---|---|---|
| Slack `text` (14 seeded) | all 14 | full read; identities, channels, DMs, ts→created_at, thread shape, build Started/Success cross-check |
| Linear title/description/comment (14 issues + 56 comments) | all | every claim extracted; ids/titles/states/assignees/completed_at vs base |
| Gmail body/subject (1 vendor + 4 invites) | all 5 | full body read |
| Docs body (4 docs) | all 4 | every bullet checked against #builds / Confluence / GitHub |
| Sheet cells (2 sheets, 6 grids) | all | titles, evidence refs, devices, versions |
| Trello comments/desc (2 actions + card/board/badges) | all | ids, idShort, board, list, member creators, badge counts |
| GitHub PR/review text (#36, plus #422/#471 cited) | all | numbering, dates, merge order, branch names |
| Calendar description (5 events) | all 5 | weekday/UTC↔PDT, attendees, ical_uid |

Base readers used: `hgget.py`/`hg.py search`, raw `Services_Data/*/data.json` for linear, github, trello, gsheets, gdrive, gdocs, slack, contacts; Confluence `confluence_working.json`.

## CONFLICT items ranked by severity

1. **L269 + L271 + L274 — Brian's update-path doc calls 1.3.24 "current store build (N-1)"** and tells the reader to install it from the App Store. Base (Confluence Season Pass spec, updated 2025-09-30T17:30Z, i.e. four hours before the doc was written) says the shipped builds are **Android 0.3.127 published Sep 22** and **iOS 0.3.49 released Sep 29**; 1.3.24 is the Sep 2-3 hotfix (`release/1.3.24_HotFix`, #builds 09-02/09-03). This is the one that also breaks the whole N-1/N-2 framing: the doc's N-1 is really N-2, so both "current store build" cells and the repro line are wrong, and the N-2 rows are unnamed so they survive only by accident. Fix: N-1 = 0.3.49 (iOS) / 0.3.127 (Android), N-2 = 1.3.24, repro = "install 0.3.49 from the App Store".
2. **L23 — ZOM-576 "Tier 12 premium reward … is two chests"** vs the Season Pass spec's tier table (band 11-20 premium = "Booster bundles + gems") and its "No Season Pass purchase has been recorded yet" (17:30Z, four hours before the ticket). Decides the Season Pass row on the release ticket. Fix: use the spec's "booster bundle and gems".
3. **L132 — vendor email says "Puzzles vs Zombies" on Sep 30** vs three Confluence pages ("listed as *Puzzles vs Zombies* … until the … rename on 24 July 2025"). Low severity (the email's finding duplicates ZOM-562), but it is a dated-name conflict a strict reviewer will read as stale copy. Fix: "Zombie Match 3D".

Non-conflicts worth knowing (all checked, all hold): hotfix train end Sep 3; "everything from main since Sep 3"; auth-branch submissions are test builds; iOS posts print only the newest change; #127/#40 cut Sep 22; the 8 sheet titles and `match3d#422`; `#471` for ZOM-498/536; backend #36 free and correctly ordered; glue 400 + trampoline 200 = 600 coins; every DM/channel/identity; Oct 3 = Friday and 16:00Z = 9am PDT; Trello card 79 / board / 2-comment badge.
