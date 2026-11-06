# Prompt Brief — vincent-zm3d-release-gate · prep

> Built 2026-11-04 from 00_Assigments.md, Working_Files/00_Task_Context.json, Working_Files/01_Grounding_Dossier.md, 01_Universe_Inject.sql (sha256 5a8d995238f3), Working_Files/01_Hardness_Manifest.json, Working_Files/01_Scenario_Design.md, Working_Files/01_Gradable_Surface.json, Working_Files/solver/truth.json, 03_Error_Async_Config.txt · Persona view verified: all (check-sql PASS, 0 load-bearing rows not visible)
> Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) · seed bound 2025-10-01T00:00:00Z · persona today Wednesday 1 Oct 2025
> 04_Prompt.txt may be drafted by Claude or Codex (/create-prompt-writing draft) or written by the human.

## 1 · Assignment fit

| Axis | Assigned value | What it requires here (cited) |
| --- | --- | --- |
| Business function | Engineering → Engineering & Technical Operations | Build, release and quality work (`Evals/references/rules/task_categories.md`); the gate decides whether the ZM store candidates (`C05433XK267/1759263189.219529`, `C05433XK267/1759259749.259909`) ship. |
| Persona | Vincent Parker, `vincent.parker@harmonygames.co`, Game Systems Engineer, Engineering (roster persona_key vincent_parker; Slack `EMPLOYEE_0012_SLACK_ID`; Linear `usr_65c76e0b87aa7e9b`) | Voice and remit in one line: the QA owner of both games (page_qa_runbook "Owned by QA (Vincent Parker)"; page_release_checklist "Owner: Vincent Parker (QA)"), writes short build-tagged bug notes; read scope: #zombie-bugs `C08R27X0EAH`, #builds `C05433XK267`, DMs `D0770ET1HV2` and `D079SNE2TL4` (Douglas), GitHub `harmonygames-Games/match3d-backend#36` with its reviews and inline review comments, his mailbox and Drive. |
| Competency | Engineering Ops | Release readiness, QA gates and build tracking (`Task_Authoring/references/Taxonomy_V2_Step_Map.md`, Engineering Ops). Remit: the release checklist makes QA sign-off "a hard gate" before any store submission, and Arthur's release ticket `ZOM-570` assigns the gate to Vincent. |
| Task skill | Analysis and synthesis | Combine many records into one judgement per item and an overall call: 132 register rows, each decided by the ticket, its QA notes (Linear comments), the build cut (#builds, GitHub), re-tests in Slack / Trello and the two rule docs (`f_632c44650df44fe252ee59`, `f_a038a576ca8db6955fae95`); the sign-off synthesises them. |
| Task type | Long Horizon; effective profile extreme (dossier §4 pastes HARDNESS GATE (extreme): PASS) | Services carrying weight: linear (132 register rows, ~60 seeded QA notes, the release ticket), slack (#builds job starts and change lists, #zombie-bugs thread, two DMs), gdocs / gdrive (four rule docs, the update-path log), gsheets (gate sheet, regression matrix), github (`harmonygames-Games/match3d-backend#36`, match3d PR merge times), trello (`68d1eb90bef538c7c5c5599d`), gmail (vendor notes), contacts, gcal, confluence (base runbook pages). Call budget 251 (manifest `call_budget`, requester-confirmed floor 250). |
| Difficulty mode | easy, cap 0.90 | Six Opus 5.5 baselines must average below 90% with fewer than five full passes (`Working_Files/00_Task_Context.json /difficulty_cap`); design target 62–77%. |
| Freeze and clock | seed bound `2025-10-01T00:00:00Z`; eval clock 2025-10-01 07:00 UTC = Wed 1 Oct 2025 00:00 PT | The candidates were started on Tue 30 Sep 2025 at 11:43 / 11:45 PT (`C05433XK267/1759257812.041449`, `C05433XK267/1759257934.076209`), "yesterday" for the persona; the go/no-go is Fri 3 Oct 2025 9:00 PT (`evt_81e6dc4dbfd331f1a6a317`). |

## 2 · Situation

| Symptom | Seen by | Where it shows (locator) | Relevant records the persona cannot see |
| --- | --- | --- | --- |
| Arthur cut the ZM store candidates and opened a store release ticket asking QA for the gate before Friday's go/no-go. | Vincent, the ticket's assignee | `ZOM-570` (2025-09-30T20:20Z, creator `usr_cc3e90160f490686`) | none (Linear is unscoped) |
| Arthur posted the candidates in #zombie-bugs, @-mentioning Vincent; Brian replied that the regression matrix is green. | Vincent, channel member | `C08R27X0EAH/1759263900.484190`, reply `C08R27X0EAH/1759266600.265963` | none |
| Vincent's release gate sheet holds the "How we gate" tab and the previous gate's tab for #127 / #40. | Vincent, the owner | `f_0ebfccf33076f9dbf086bc` | none |
| The go/no-go for the store push is on Vincent's calendar for Friday. | Vincent, an invited guest | `evt_81e6dc4dbfd331f1a6a317` | the other attendees' own calendar copies |

## 3 · Investigation → action

Questions (no answers):

- Which tickets does the gate cover, by the rules the release ticket points to (`ZOM-570`, `f_632c44650df44fe252ee59`)?
- For each ticket moved to Done since the last gate, is its change in the candidate builds or live on prod (`f_a038a576ca8db6955fae95`, #builds `C05433XK267`, match3d and match3d-backend PRs)?
- What does the latest QA check on the candidates (or on prod) say for each ticket (Linear comments, #zombie-bugs, DMs, the ZM ROADMAP card `68d1eb90bef538c7c5c5599d`)?
- How bad is each remaining defect under the rules, and does an outside report change that (`vincent.parker@harmonygames.co/1844730396672762606`)?
- Does the regression matrix pass the runbook's gate, every row included (`page_qa_runbook`, `f_b91db376f65604b8602657`, `f_5e40215b7d4d24b0455412`)?
- What does the gate sheet expect (`f_0ebfccf33076f9dbf086bc`, "How we gate"), and how do blockers go on the release ticket (`68dc3ef455344e471b1d2ea9`)?

Writes:

- The register in a new tab of `f_0ebfccf33076f9dbf086bc`.
- The blocker list on `ZOM-570` (existing ticket keys).
- A new Linear ticket for each failure nobody has filed yet (the update-path failure on iOS #50).
- A reply in Arthur's thread `C08R27X0EAH/1759263900.484190` with the QA call.

Every write depends on the investigation: the register needs each ticket's build status and call, the blocker list needs the BLOCKER set, the new ticket needs the matrix check and the "already filed?" check, and the reply needs the blocker list.

## 4 · Pinned final state (UGT anchor)

| Deliverable | Required contents | Destination | Recipients | Catalog write | Fed by |
| --- | --- | --- | --- | --- | --- |
| 1 · Register | One row per in-scope ticket (132), each with ticket, title, build status, QA result, call (BLOCKER / KNOWN ISSUE / FIXED / NO CALL) and evidence | a new tab in `f_0ebfccf33076f9dbf086bc` (ZM3D Release Gate, owner vincent.parker@harmonygames.co) | no recipient | `gsheets_batch_update` (add sheet) + `gsheets_values_update` | `f_632c44650df44fe252ee59`, `f_a038a576ca8db6955fae95`, `ZOM-570`, per-ticket comments, #builds `C05433XK267` |
| 2 · Blocker list | Every BLOCKER by its existing key: DES-313, ZOM-293, ZOM-435, ZOM-449, ZOM-458, ZOM-473, ZOM-483, ZOM-535, ZOM-546, ZOM-554, ZOM-559, ZOM-560, ZOM-562, ZOM-567, ZOM-569, ZOM-573, ZOM-576, ZOM-578 (18) | the description of `ZOM-570` | no recipient | `linear_update_issue` (description) | the register's BLOCKER rows; reuse rule `68dc3ef455344e471b1d2ea9` |
| 3 · New ticket | One Linear bug for the failed update from the N-1 store build (the App Store build) to iOS Submission #50 with device (iPhone 13), OS (iOS 18.6), source build (N-1, App Store) and repro | team `team_ZOM` | no recipient | `linear_create_issue` | `f_5e40215b7d4d24b0455412`, `page_qa_runbook`, `page_release_checklist` |
| 4 · Sign-off | The QA call: the candidates are not ready (blockers listed / no-go) | reply in the thread of `C08R27X0EAH/1759263900.484190` | Arthur Blake `EMPLOYEE_0025_SLACK_ID` and the channel | `slack_send_message` (channel `C08R27X0EAH`, thread_ts 1759263900.484190) | the blocker list; Leonard's note `cmt_zom570_1` |

Alternatives a careful run could defend:

- The blocker list added below Arthur's text in the `ZOM-570` description or with the description rewritten around it; keys in any order, with or without titles. A comment on `ZOM-570` instead is a different write (the prompt asks for the description). The new update-path ticket goes on the list by its new key (`ZOM-570`: "by key, the existing ticket if there is one").
- The new update-path ticket labelled Bug or not; priority free; it gets a register row as a BLOCKER (`f_632c44650df44fe252ee59`, Sep 23: "From the next gate on, tickets filed while the gate is running get a row too").
- Register columns in the "How we gate" order or a superset; calls in capitals or mixed case; the evidence column as ids or links (`f_0ebfccf33076f9dbf086bc`).
- The tab name in `f_0ebfccf33076f9dbf086bc`: anything naming the candidates or the date (e.g. "Sep 30 - Android #135 / iOS #50").
- The sign-off wording in the thread `C08R27X0EAH/1759263900.484190`: "no-go", "not ready", "hold" or "blocked", with or without the blocker keys; also sent to the channel is fine.

### 4b · Canonical outcome (all fair outcomes)

| Deliverable | Field | Fixed value (or closed accepted set, with sources) | Delegated by (quoted span, or —) | Allowed equivalence class | Material / representational |
| --- | --- | --- | --- | --- | --- |
| Register | Row set | Exactly the 132 keys of `scenario_gen/scope_keys.json` (`solver/truth.json`): every open ZOM ticket except ZOM-359 / ZOM-475 and the release ticket `ZOM-570`, ART-790, ART-792, ART-793, DES-313, and every ticket moved to Done after the Sep 22 builds were cut (18 base + ZOM-567, ZOM-569) | `f_632c44650df44fe252ee59`: "every ZM ticket that's still open (any state but Done, Canceled or Duplicate), whatever team or label" | Rows in any order; plus one row for the new update-path ticket (`f_632c44650df44fe252ee59`); extra columns allowed | Material |
| Register | Call per row | As `solver/truth.json`: samples ZOM-569 BLOCKER, ZOM-567 BLOCKER, ZOM-435 BLOCKER, ZOM-473 BLOCKER, ZOM-562 BLOCKER, ART-793 KNOWN ISSUE, DES-313 BLOCKER, ZOM-578 BLOCKER, ZOM-563 FIXED, ZOM-559 BLOCKER, ZOM-560 BLOCKER, ZOM-481 KNOWN ISSUE, ZOM-458 BLOCKER, ZOM-535 BLOCKER, ZOM-293 BLOCKER, ZOM-564 FIXED, ZOM-506 FIXED, ZOM-557 FIXED, ZOM-561 FIXED, ZOM-513 NO CALL, ZOM-387 NO CALL; totals 18 BLOCKER / 19 KNOWN ISSUE / 10 FIXED / 85 NO CALL, the blocker set being the 18 keys plus the new update-path ticket | — (rules in `f_632c44650df44fe252ee59`) | The four call words in any case | Material |
| Register | Build status | By the "build status means" row of `f_0ebfccf33076f9dbf086bc` "How we gate": ZOM-569 not in candidate; ZOM-567 server – not live; ZOM-563 server – live; Done bugs closed before 18:43Z and bugs QA saw working on the candidates (ZOM-429, ZOM-517, ZOM-564) in candidate; open bugs not seen working and every no-call ticket n/a | `f_0ebfccf33076f9dbf086bc` "How we gate" vocabulary | Equivalent wording ("not in #135 / #50", "merged, not deployed") | Material for ZOM-569 / ZOM-567; representational otherwise |
| Register | Tab | A new tab of `f_0ebfccf33076f9dbf086bc` | prompt "a new tab of my release gate sheet" | Any tab name | Material tab; representational name |
| Blocker list | Set | Contains ZOM-569, ZOM-567, ZOM-435, ZOM-473, ZOM-562 (graded samples) among the BLOCKER keys; existing keys, no duplicate tickets, plus the new update-path ticket's key | `68dc3ef455344e471b1d2ea9`: "goes on ZOM-570 under the ticket that already exists"; `ZOM-570`: "by key, the existing ticket if there is one" | The description of ZOM-570 (prompt: "add the blockers to the release ticket's description"); any order; titles optional | Material set and destination; representational layout |
| New ticket | Subject | The update from the N-1 store build (the App Store build) to iOS Submission #50 resets progress (level 1, 500 coins); device iPhone 13, iOS 18.6, source build N-1 (App Store) | `page_release_checklist`: "file the bug with device / OS / source build" | Title and wording free; team ZOM | Material subject and source build; representational wording |
| Sign-off | Destination | A reply in the thread of `C08R27X0EAH/1759263900.484190` | prompt "Reply in Arthur's candidates thread in #zombie-bugs"; `cmt_zom570_1` | Thread reply, also-sent-to-channel allowed; a top-level post is a different write | Material |
| Sign-off | Call | Not ready / no-go while blockers remain (the blocker set of `ZOM-570`) | — | Any wording | Material |
| All writes | Timing | Done in the run, before the go/no-go at 2025-10-03T16:00Z | prompt "before Friday's go/no-go" (`evt_81e6dc4dbfd331f1a6a317`) | No scheduling needed | Representational |

## 5 · Discovery map

| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |
| --- | --- | --- | --- | --- | --- | --- |
| 1 · Store release ticket | candidates #135 / #50, rules pointers, reuse card, go/no-go | `ZOM-570` | YES — Linear | first link (A1) | low | Yes (anchor A1, by noun phrase) |
| 2 · Arthur's candidate post | the sign-off thread | `C08R27X0EAH/1759263900.484190` | YES — #zombie-bugs member | destination | low | Yes ("Arthur's candidates thread in #zombie-bugs") |
| 3 · Leonard's rules H2 | scope, verification, severity | `f_632c44650df44fe252ee59` | YES — shared with Vincent | ZOM-570 names "Leonard's submission rules" | medium — a Drive doc, not mail | No |
| 4 · Arthur's build rules H1 | main at job start; merged is not live | `f_a038a576ca8db6955fae95` | YES — shared | ZOM-570 names "my note on how we cut submissions" | medium | No |
| 5 · Sep 2 hotfix doc (decoy) | hotfix submissions from release/1.3.24_HotFix | `f_fcb4f7c9b508088e0d5803` | YES — shared | met by the same Drive search; overturned by H1 | medium | No |
| 6 · July beta-drop doc (decoy) | only crashes and wipes block a beta drop | `f_5ae4332fb6927f84b3afdc` | YES — shared | met by the same search; different lot | medium | No |
| 7 · Gate sheet | "How we gate" tab, Sep 22 tab | `f_0ebfccf33076f9dbf086bc` | YES — owner | the Sep 22 tab is met first (stale calls, Bug-only scope) | low | Yes (anchor A3) |
| 8 · Submission job starts | #50 18:43:32Z, #135 18:45:34Z, both main | `C05433XK267/1759257812.041449`, `C05433XK267/1759257934.076209` | YES — #builds member | evidence for every Done row | medium — 450 Jenkins posts | Yes (the build names only) |
| 9 · The post-cut fix | #2028 started 21:36Z with "Fix season pass main screen instance from join popup" | `C05433XK267/1759268201.182309`, `C05433XK267/1759268589.049939` | YES | overturns ZOM-569's Done | high — a dev build, not a submission | No |
| 10 · ZOM-569 Done | ticket closed 18:05Z right after "fixed on my branch, the join popup only opens one SP screen now" (18:02Z) | `ZOM-569`, `cmt_zom569_1` | YES — Linear | claim met first (T1) | high | No |
| 11 · Backend PR approval and rollout | merged with Arthur's APPROVED review `#36#rev_1` (empty body, like the repo's other 30), then Douglas's 22:01:52Z "#36 is rolled out to prod too, the container is up. that's the code side" | `harmonygames-Games/match3d-backend#36`, `harmonygames-Games/match3d-backend#36#rev_1`, `D079SNE2TL4/1759269712.483915` | YES — GitHub, DM party | claim met first (T2) | high | No |
| 12 · Arthur's inline review comment | the migration's chest rows are read on prod but are still only on dev (rolled out is not migrated) | `harmonygames-Games/match3d-backend#36#rc_1`, under the COMMENTED review `#36#rev_2` (22:40Z) | YES — GitHub unscoped | overturning (T2) | high — an inline comment with no Slack copy (INT-01 mirrors match3d only) | No |
| 13 · CI/CD page | "CI stops here", deploy "Run by hand" | `page_cicd_pipeline` | YES — Confluence | supports H1 | low | No |
| 14 · Vincent's #133 pass | ZOM-435 ok on #133 | `C08R27X0EAH/1759140300.935009` | YES | claim met first (T3) | high | No |
| 15 · Leonard's Trello re-test | stuck on the trophy path on #135 | `68dc63484a5b2d0a869e758f` on `68d1eb90bef538c7c5c5599d` | YES — Trello | overturns the pass (T3) | high — a card comment | No |
| 16 · Brian's DM re-test | ZOM-473 still skippable on iOS #50 (Turkish) | `D0770ET1HV2/1759267800.858041` | YES — DM party | overturns ZOM-473's Done (T3b) | high — Turkish DM | No |
| 17 · Brian's green reply | "regression matrix green on #135 and #50" | `C08R27X0EAH/1759266600.265963`, `f_b91db376f65604b8602657` | YES | claim met first (T4) | high — sounds conclusive | No |
| 18 · Update-path log | update from the N-1 store build to iOS #50 FAIL (level 1, 500 coins) | `f_5e40215b7d4d24b0455412`; pointer `D0770ET1HV2/1759272300.342229` | YES — shared | overturns the green reply (T4) | high | No |
| 19 · Runbook update rule | "A failure in any UPDATE column blocks the release" | `page_qa_runbook` | YES — Confluence | the rule for T4 | low | Yes (anchor A2, "the QA regression runbook") |
| 20 · Vendor session notes | boss-fight singles, no clear, life lost (Puzzles vs Zombies, TestFlight 50) | `vincent.parker@harmonygames.co/1844730396672762606` | YES — Vincent's inbox | escalates ZOM-562 (T5) | high — old app name | No |
| 21 · Vendor contact | QA Lead, Cobalt Playtesting (ZM3D playtests) | `29016e2ba1a844a2509b847b` | YES — Contacts | identifies the sender (T5) | medium | No |
| 22 · ZOM-562 | Orphan items in boss arena | `ZOM-562` | YES | alias target | medium — reads cosmetic | No |
| 23 · Other-team ZM tickets | ART-793, DES-313 (and unlabeled ZOM-578) | `ART-793`, `DES-313`, `ZOM-578` | YES | outside the team ZOM + Bug view (T6) | high | No |
| 24 · ZOM-563 confirmed on prod | Douglas deployed 18:16Z, Vincent confirmed 21:58Z | `D079SNE2TL4/1759256193.859279`, `D079SNE2TL4/1759269524.769369` | YES — DM party | overturns the In Progress state (T7) | medium | No |
| 25 · Reuse rule | blockers by existing keys, no duplicates | `68dc3ef455344e471b1d2ea9` | YES — Trello | ZOM-570 names the "tech-issues card" | low | No |
| 26 · Per-ticket QA notes | e.g. ZOM-559 froze on a Samsung S22 on #133 | `cmt_zom559_1` and the other cmt_* rows | YES — Linear | decide calls the labels do not (T12, channel scale:comments) | high — one read per ticket | No |
| 27 · Leonard's push note | sign-off as a reply on Arthur's thread | `cmt_zom570_1` | YES | amends the destination | low | No (the prompt names the thread itself) |
| 28 · Go/no-go | Fri 3 Oct 2025 16:00Z (9:00 PT) | `evt_81e6dc4dbfd331f1a6a317` | YES — own calendar | deadline | low | Yes ("Friday's go/no-go") |
| 29 · Brian's Sep 29 group-DM findings | ZOM-458: chest claimed, nothing in the inventory after quitting a level without winning; ZOM-535: boss-arena nuke goes to a dead zombie at 120 cpm, arena can't be finished in 3 tries (Turkish) | `D0770ET1HV2/1759160460.731000` | YES — group-DM party | overturning (T16) | high — an older group DM above the read floor | No |
| 30 · ZOM-293's own symptom | lost 4 in a row on level 63, demoted to tier 0; the glue and trampoline taken for the retry were gone after the reload, 600 coins' worth | `ZOM-293`, `cmt_zom293_1` | YES — Linear | overturning (T17) | high — list view and issue read show no comment | No |
| 31 · Douglas's rollout note | "#36 is rolled out to prod too, the container is up. that's the code side" (22:01:52Z) | `D079SNE2TL4/1759269712.483915` | YES — DM party | claim met first (T2) | high — a one-line DM between two others | No |

Never in the prompt: any rule (scope, severity, build cut, liveness, update rule), any ticket key, the blocker list or its size, the cut times, Brian's Sep 29 group-DM findings, the dev-only chest rows, ZOM-293's lost boosters, Leonard's Trello re-test, Brian's DM or doc, the vendor or the old app name, the other-team tickets, the call vocabulary.

## 5a · Search-as-persona proof

Thirty-one §5 facts, one row each, in §5 order. Every row is `persona_view.py search vincent_parker <service> "<query>" --limit 10` on the base universe (the tool reads no SQL overlay; `--no-hidden` on Gmail), run 2026-11-04. Seeded facts are proven reachable by `persona_view.py check-sql vincent_parker 01_Universe_Inject.sql --load-bearing` (PASS, dossier Self-review) and are reached in a run through the record the prompt names (§6).

| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |
| --- | --- | --- | --- | --- | --- | --- |
| 1 · Store release ticket `ZOM-570` | linear — unscoped (not ACL-scoped) | `store push` | 0 (showing 0) | 0 in 0 containers | — (0 hits) | NO in base search — seeded by /create-injection (check-sql YES); routed |
| 2 · Arthur's candidate post `C08R27X0EAH/1759263900.484190` | slack | `store candidates` | 0 (showing 0) | 0 in 0 containers | — (0 hits) | NO in base search — seeded by /create-injection (check-sql YES); routed |
| 3 · Leonard's rules H2 `f_632c44650df44fe252ee59` | gdrive | `submission rules` | 0 (showing 0) | 0 in 0 containers | — (0 hits) | NO in base search — seeded by /create-injection (check-sql YES); routed |
| 4 · Arthur's build rules H1 `f_a038a576ca8db6955fae95` | gdrive | `submission builds` | 0 (showing 0) | 0 in 0 containers | — (0 hits) | NO in base search — seeded by /create-injection (check-sql YES); routed |
| 5 · Sep 2 hotfix doc `f_fcb4f7c9b508088e0d5803` | gdrive | `hotfix submissions` | 0 (showing 0) | 0 in 0 containers | — (0 hits) | NO in base search — seeded by /create-injection (check-sql YES); routed |
| 6 · July beta-drop doc `f_5ae4332fb6927f84b3afdc` | gdrive | `beta drops` | 0 (showing 0) | 0 in 0 containers | — (0 hits) | NO in base search — seeded by /create-injection (check-sql YES); routed |
| 7 · Gate sheet `f_0ebfccf33076f9dbf086bc` | gdrive | `Release Gate` | 0 (showing 0) | 0 in 0 containers | — (0 hits) | NO in base search — seeded by /create-injection (check-sql YES); routed |
| 8 · Submission job starts `C05433XK267/1759257934.076209` | slack | `Android Submission - #135` | 4 (showing 4) | 0 in 0 containers | `C05433XK267/1738328514.768779` | YES — base record `C05433XK267/1738328514.768779` |
| 9 · The post-cut fix `C05433XK267/1759268589.049939` | slack | `season pass main screen instance` | 3 (showing 3) | 0 in 0 containers | `C05433XK267/1759268526.402559` | YES — base record `C05433XK267/1759268526.402559` |
| 10 · ZOM-569 Done `ZOM-569` | linear — unscoped (not ACL-scoped) | `Season Pass opens twice` | 0 (showing 0) | 0 in 0 containers | — (0 hits) | NO in base search — seeded by /create-injection (check-sql YES); routed |
| 11 · Backend PR approval `harmonygames-Games/match3d-backend#36` | github — unscoped (not ACL-scoped) | `chest grant` | 0 (showing 0) | 0 in 0 containers | — (0 hits) | NO in base search — seeded by /create-injection (check-sql YES); routed |
| 12 · Arthur's inline review comment `harmonygames-Games/match3d-backend#36#rc_1` | github — unscoped (not ACL-scoped) | `chest rows` | 0 (showing 0) | 0 in 0 containers | — (0 hits) | NO in base search — seeded by /create-injection (check-sql YES); routed |
| 13 · CI/CD page `page_cicd_pipeline` | confluence — unscoped (not ACL-scoped) | `CI/CD Pipeline` | 3 (showing 3) | 0 in 0 containers | `confluence_working.json /pages/11` | YES — base record `confluence_working.json /pages/11` |
| 14 · Vincent's #133 pass `C08R27X0EAH/1759140300.935009` | slack | `trophy path claim spam` | 0 (showing 0) | 0 in 0 containers | — (0 hits) | NO in base search — seeded by /create-injection (check-sql YES); routed |
| 15 · Leonard's Trello re-test `68dc63484a5b2d0a869e758f` | trello — unscoped (not ACL-scoped) | `trophy path` | 10 (showing 10) | 0 in 0 containers | `data.json /cards/703` | YES — base neighbours (`data.json /cards/703`); the seeded record itself is in the SQL overlay (check-sql YES), routed |
| 16 · Brian's DM re-test `D0770ET1HV2/1759267800.858041` | slack | `ZOM-473` | 0 (showing 0) | 0 in 0 containers | — (0 hits) | NO in base search — seeded by /create-injection (check-sql YES); routed |
| 17 · Brian's green reply `C08R27X0EAH/1759266600.265963` | slack | `regression matrix green` | 0 (showing 0) | 0 in 0 containers | — (0 hits) | NO in base search — seeded by /create-injection (check-sql YES); routed |
| 18 · Update-path log `f_5e40215b7d4d24b0455412` | gdrive | `Update-path` | 0 (showing 0) | 0 in 0 containers | — (0 hits) | NO in base search — seeded by /create-injection (check-sql YES); routed |
| 19 · Runbook update rule `page_qa_runbook` | confluence — unscoped (not ACL-scoped) | `QA Regression Runbook` | 7 (showing 7) | 0 in 0 containers | `confluence_working.json /pages/7` | YES — base record `confluence_working.json /pages/7` |
| 20 · Vendor session notes `vincent.parker@harmonygames.co/1844730396672762606` | gmail | `Session notes` | 0 (showing 0) | not scanned (--no-hidden) | — (0 hits) | NO in base search — seeded by /create-injection (check-sql YES); routed |
| 21 · Vendor contact `29016e2ba1a844a2509b847b` | contacts — unscoped (not ACL-scoped) | `Cobalt` | 0 (showing 0) | 0 in 0 containers | — (0 hits) | NO in base search — seeded by /create-injection (check-sql YES); routed |
| 22 · ZOM-562 `ZOM-562` | linear — unscoped (not ACL-scoped) | `Orphan items` | 2 (showing 2) | 0 in 0 containers | `data.json /issues/3639` | YES — base record `data.json /issues/3639` |
| 23 · Other-team ZM tickets `ART-793`, `DES-313` | linear — unscoped (not ACL-scoped) | `ZM3D` | 2 (showing 2) | 0 in 0 containers | `data.json /issues/591` | YES — base neighbours (`data.json /issues/591`); the seeded record itself is in the SQL overlay (check-sql YES), routed |
| 24 · ZOM-563 on prod `D079SNE2TL4/1759269524.769369` | slack | `Yep it works as expected` | 1 (showing 1) | 0 in 0 containers | `D079SNE2TL4/1759269524.769369` | YES — base record `D079SNE2TL4/1759269524.769369` |
| 25 · Reuse rule `68dc3ef455344e471b1d2ea9` | trello — unscoped (not ACL-scoped) | `TECH ISSUES` | 3 (showing 3) | 0 in 0 containers | `data.json /cards/802` | YES — base neighbours (`data.json /cards/802`); the seeded record itself is in the SQL overlay (check-sql YES), routed |
| 26 · Per-ticket QA notes `cmt_zom559_1` | linear — unscoped (not ACL-scoped) | `Samsung S22` | 0 (showing 0) | 0 in 0 containers | — (0 hits) | NO in base search — seeded by /create-injection (check-sql YES); routed |
| 27 · Leonard's push note `cmt_zom570_1` | linear — unscoped (not ACL-scoped) | `sign-off as a reply` | 0 (showing 0) | 0 in 0 containers | — (0 hits) | NO in base search — seeded by /create-injection (check-sql YES); routed |
| 28 · Go/no-go `evt_81e6dc4dbfd331f1a6a317` | gcal | `go/no-go` | 0 (showing 0) | 0 in 0 containers | — (0 hits) | NO in base search — seeded by /create-injection (check-sql YES); routed |
| 29 · Brian's Sep 29 group-DM findings `D0770ET1HV2/1759160460.731000` | slack | `ZOM-458` | 0 (showing 0) | 1 in 1 containers | — (0 hits) | NO in base search — seeded by /create-injection (check-sql YES); routed |
| 30 · ZOM-293 and its reporter note `cmt_zom293_1` | linear — unscoped (not ACL-scoped) | `Dynamic Difficulty Tiering` | 2 (showing 2) | 0 in 0 containers | `data.json /issues/3347` | YES — base neighbours (`data.json /issues/3347`); the seeded record itself is in the SQL overlay (check-sql YES), routed |
| 31 · Douglas's #36 rollout note `D079SNE2TL4/1759269712.483915` | slack | `rolled out to prod` | 0 (showing 0) | 0 in 0 containers | — (0 hits) | NO in base search — seeded by /create-injection (check-sql YES); routed |

§5 row 1 — linear — `store push`

```
SEARCH linear 'store push' as vincent_parker  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

§5 row 2 — slack — `store candidates`

```
SEARCH slack 'store candidates' as vincent_parker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

§5 row 3 — gdrive — `submission rules`

```
SEARCH gdrive 'submission rules' as vincent_parker  scope: Drive file/folder names (on-disk file content is not searched)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

§5 row 4 — gdrive — `submission builds`

```
SEARCH gdrive 'submission builds' as vincent_parker  scope: Drive file/folder names (on-disk file content is not searched)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

§5 row 5 — gdrive — `hotfix submissions`

```
SEARCH gdrive 'hotfix submissions' as vincent_parker  scope: Drive file/folder names (on-disk file content is not searched)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

§5 row 6 — gdrive — `beta drops`

```
SEARCH gdrive 'beta drops' as vincent_parker  scope: Drive file/folder names (on-disk file content is not searched)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

§5 row 7 — gdrive — `Release Gate`

```
SEARCH gdrive 'Release Gate' as vincent_parker  scope: Drive file/folder names (on-disk file content is not searched)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

§5 row 8 — slack — `Android Submission - #135`

```
SEARCH slack 'Android Submission - #135' as vincent_parker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=4 (showing 4)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C05433XK267/1738328514.768779", "channel": "builds", "kind": "public", "date": "2025-01-31", "user": null, "reply": false, "snippet": "DD Android Submission - #135 Started by user Arthur Blake (<http://blake.tplinkdns.com:9009/job/DD%20Android"}
  {"id": "C05433XK267/1738329484.096599", "channel": "builds", "kind": "public", "date": "2025-01-31", "user": null, "reply": false, "snippet": "DD Android Submission - #135 - develop - (228MB) Success after 16 min (<http://blake.tplinkdns.com:9009/job/"}
  {"id": "C05433XK267/1759257934.076209", "channel": "builds", "kind": "public", "date": "2025-09-30", "user": null, "reply": false, "snippet": "Match3D Android Submission - #135 Started by user Arthur Blake (<http://blake.tplinkdns.com:9009/job/Match3D%20An"}
```

§5 row 9 — slack — `season pass main screen instance`

```
SEARCH slack 'season pass main screen instance' as vincent_parker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=3 (showing 3)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C05433XK267/1759268526.402559", "channel": "builds", "kind": "public", "date": "2025-09-30", "user": "SLACK_BOT_0005_SLACK_ID", "reply": false, "snippet": "|Open>) Match 3D iOS Internal - #1759 - main Changes: - Fix season pass main screen instance from join popup [[PERSON_NAME_0022]]"}
  {"id": "C05433XK267/1759268589.049939", "channel": "builds", "kind": "public", "date": "2025-09-30", "user": null, "reply": false, "snippet": "direct|Open>) Match3D Android - #2028 - main Changes: - Fix season pass main screen instance from join popup [[PERSON_NAME_0022]]"}
  {"id": "C093LEZGF6J/1759268180.590379", "channel": "zombie-prs", "kind": "public", "date": "2025-09-30", "user": "SLACK_BOT_0004_SLACK_ID", "reply": false, "snippet": "t/a61cb2b9c57d858aeda409758bc65ec5b3380602|a61cb2b9>` - Fix season pass main screen instance from join popup"}
```

§5 row 10 — linear — `Season Pass opens twice`

```
SEARCH linear 'Season Pass opens twice' as vincent_parker  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

§5 row 11 — github — `chest grant`

```
SEARCH github 'chest grant' as vincent_parker  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

§5 row 12 — github — `chest rows`

```
SEARCH github 'chest rows' as vincent_parker  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

§5 row 13 — confluence — `CI/CD Pipeline`

```
SEARCH confluence 'CI/CD Pipeline' as vincent_parker  scope: hg.py search (unscoped: no ACL filter)
visible hits=3 (showing 3)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json", "service_file": "confluence_working.json", "pointer": "/pages/11/title", "parent_pointer": "/pages/11", "encoding": "json", "text": "CI/CD Pipeline & Branching", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json", "service_file": "confluence_working.json", "pointer": "/page_versions/14/title", "parent_pointer": "/page_versions/14", "encoding": "json", "text": "CI/CD Pipeline & Branching", "tru
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json", "service_file": "confluence_working.json", "pointer": "/page_versions/15/title", "parent_pointer": "/page_versions/15", "encoding": "json", "text": "CI/CD Pipeline & Branching", "tru
```

§5 row 14 — slack — `trophy path claim spam`

```
SEARCH slack 'trophy path claim spam' as vincent_parker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

§5 row 15 — trello — `trophy path`

```
SEARCH trello 'trophy path' as vincent_parker  scope: hg.py search (unscoped: no ACL filter)
visible hits=10 (showing 10)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/cards/703/name", "parent_pointer": "/cards/703", "encoding": "json", "text": "[Feature] Trophy Path ([PERSON_NAME_0022])", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/4670/data/card/name", "parent_pointer": "/actions/4670/data/card", "encoding": "json", "text": "Trophy Path - [PERSON_NAME_0022] (link)", "truncated":
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/4733/data/card/name", "parent_pointer": "/actions/4733/data/card", "encoding": "json", "text": "Trophy Path - [PERSON_NAME_0022] (link)", "truncated":
```

§5 row 16 — slack — `ZOM-473`

```
SEARCH slack 'ZOM-473' as vincent_parker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

§5 row 17 — slack — `regression matrix green`

```
SEARCH slack 'regression matrix green' as vincent_parker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

§5 row 18 — gdrive — `Update-path`

```
SEARCH gdrive 'Update-path' as vincent_parker  scope: Drive file/folder names (on-disk file content is not searched)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

§5 row 19 — confluence — `QA Regression Runbook`

```
SEARCH confluence 'QA Regression Runbook' as vincent_parker  scope: hg.py search (unscoped: no ACL filter)
visible hits=7 (showing 7)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json", "service_file": "confluence_working.json", "pointer": "/pages/0/body", "parent_pointer": "/pages/0", "encoding": "json", "text": "ge ri:content-title=\"Live-Ops Event Engine\"/><ac:l
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json", "service_file": "confluence_working.json", "pointer": "/pages/7/title", "parent_pointer": "/pages/7", "encoding": "json", "text": "QA Regression Runbook", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json", "service_file": "confluence_working.json", "pointer": "/pages/26/body", "parent_pointer": "/pages/26", "encoding": "json", "text": "amp; QA</h3><ul><li>Full manual regression is gree
```

§5 row 20 — gmail — `Session notes`

```
SEARCH gmail 'Session notes' as vincent_parker  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned
```

§5 row 21 — contacts — `Cobalt`

```
SEARCH contacts 'Cobalt' as vincent_parker  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

§5 row 22 — linear — `Orphan items`

```
SEARCH linear 'Orphan items' as vincent_parker  scope: hg.py search (unscoped: no ACL filter)
visible hits=2 (showing 2)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/3639/title", "parent_pointer": "/issues/3639", "encoding": "json", "text": "Orphan items in boss arena", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/3639/description", "parent_pointer": "/issues/3639", "encoding": "json", "text": ". \n\n[ScreenRecording_[CREDIT_CARD_NUMBER_6362]_1.MP4]([URL_52871])\
```

§5 row 23 — linear — `ZM3D`

```
SEARCH linear 'ZM3D' as vincent_parker  scope: hg.py search (unscoped: no ACL filter)
visible hits=2 (showing 2)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/591/title", "parent_pointer": "/issues/591", "encoding": "json", "text": "ZM3D - Marketing Screenshots round 3", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/3134/title", "parent_pointer": "/issues/3134", "encoding": "json", "text": "Get everyone into linear for ZM3D", "truncated": false}
```

§5 row 24 — slack — `Yep it works as expected`

```
SEARCH slack 'Yep it works as expected' as vincent_parker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "D079SNE2TL4/1759269524.769369", "channel": "D079SNE2TL4", "kind": "im", "date": "2025-09-30", "user": "EMPLOYEE_0012_SLACK_ID", "reply": false, "snippet": "Yep it works as expected "}
```

§5 row 25 — trello — `TECH ISSUES`

```
SEARCH trello 'TECH ISSUES' as vincent_parker  scope: hg.py search (unscoped: no ACL filter)
visible hits=3 (showing 3)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/cards/802/name", "parent_pointer": "/cards/802", "encoding": "json", "text": "Fix TECH ISSUES", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/5244/data/card/name", "parent_pointer": "/actions/5244/data/card", "encoding": "json", "text": "Fix TECH ISSUES", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json", "service_file": "data.json", "pointer": "/actions/5245/data/card/name", "parent_pointer": "/actions/5245/data/card", "encoding": "json", "text": "Fix TECH ISSUES", "truncated": false}
```

§5 row 26 — linear — `Samsung S22`

```
SEARCH linear 'Samsung S22' as vincent_parker  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

§5 row 27 — linear — `sign-off as a reply`

```
SEARCH linear 'sign-off as a reply' as vincent_parker  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

§5 row 28 — gcal — `go/no-go`

```
SEARCH gcal 'go/no-go' as vincent_parker  scope: GCal event summary (base events carry no description/location)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
note: counted per meeting instance (ical_uid + start), visible if any copy is visible
```

§5 row 29 — slack — `ZOM-458`

```
SEARCH slack 'ZOM-458' as vincent_parker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=1 in 1 containers  UNVERIFIED=0 in 0 containers
```

§5 row 30 — linear — `Dynamic Difficulty Tiering`

```
SEARCH linear 'Dynamic Difficulty Tiering' as vincent_parker  scope: hg.py search (unscoped: no ACL filter)
visible hits=2 (showing 2)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/3347/title", "parent_pointer": "/issues/3347", "encoding": "json", "text": "Dynamic Difficulty Tiering Down Issue", "truncated": false}
  {"file": "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/3347/description", "parent_pointer": "/issues/3347", "encoding": "json", "text": "Dynamic Difficulty Tiering", "truncated": false}
```

§5 row 31 — slack — `rolled out to prod`

```
SEARCH slack 'rolled out to prod' as vincent_parker  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```


## 6 · Triggers, incorporation and implicit requirements

| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · persona-readable · unique · instructions-not-answer) | Inferable |
| --- | --- | --- | --- | --- |
| R1 scope of the register | `f_632c44650df44fe252ee59` | deliverable ("the gate register") | `ZOM-570` → "Leonard's submission rules" · readable · one doc with that title · states the rule, not the row list | gotcha → triggered by the register ask and the release ticket |
| R2 build status | `f_a038a576ca8db6955fae95` | scope (the named candidates) | `ZOM-570` → "my note on how we cut submissions" · readable · unique · rule only | gotcha → triggered |
| R3 QA result | `f_632c44650df44fe252ee59` | deliverable (register) | as R1 | inferable for a QA gate; the latest-on-candidate rule is in H2 |
| R4 backend liveness | `f_a038a576ca8db6955fae95` + `page_cicd_pipeline` | scope | as R2 | gotcha → triggered through H1 |
| R5 calls | `f_632c44650df44fe252ee59` | deliverable (register, blockers) | as R1 | gotcha → triggered |
| R6 matrix verdict | `page_qa_runbook` | constraint ("the checks in the QA regression runbook") | the runbook page · readable · unique · rule | triggered |
| R7 blockers on the ticket | `ZOM-570`, `68dc3ef455344e471b1d2ea9` | deliverable ("add the blockers to the release ticket's description") | ZOM-570 → "I'm putting the reuse rule on the tech-issues card" | triggered |
| R8 sign-off reply | `C08R27X0EAH/1759263900.484190` | recipient / destination | named in the prompt | triggered |
| R9 new ticket | `page_release_checklist`, `f_5e40215b7d4d24b0455412` | deliverable ("file a new ZM ticket in Linear for anything ... nobody has filed yet") | the runbook / checklist "file the bug" rule | triggered |
| R10 register format | `f_0ebfccf33076f9dbf086bc` "How we gate" | destination ("a new tab of my release gate sheet") | the sheet itself | triggered |

| Anchor | May be named (noun phrases only) | Record |
| --- | --- | --- |
| A1 | the store release ticket; the release ticket | ZOM-570 |
| A2 | the QA regression runbook; the regression runbook | page_qa_runbook |
| A3 | my release gate sheet; the gate sheet | f_0ebfccf33076f9dbf086bc |

## 7 · Dates and constraints

| Item | Absolute date or value | Source | Past fact or deadline |
| --- | --- | --- | --- |
| Persona today | Wed 1 Oct 2025 | `00_Task_Context.json /universe/persona_today` | — |
| Candidates cut ("yesterday") | Tue 30 Sep 2025, jobs started 18:43:32Z / 18:45:34Z (11:43 / 11:45 PT) | `C05433XK267/1759257812.041449`, `C05433XK267/1759257934.076209` | past fact |
| Previous gate builds | Mon 22 Sep 2025 ~12:30Z (Android #127 / iOS #40) | `C05433XK267/1758544783.817259`, `C05433XK267/1758544698.778509` | past fact |
| Go/no-go | Fri 3 Oct 2025 16:00–16:30Z (9:00–9:30 PT) | `evt_81e6dc4dbfd331f1a6a317` | deadline |
| Release ticket | created 2025-09-30T20:20Z | `ZOM-570` | past fact |

## 8 · Difficulty levers

| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |
| --- | --- | --- | --- | --- |
| Ambiguity | yes | yes | the rules live in two Drive docs the release ticket names by description (`f_632c44650df44fe252ee59`, `f_a038a576ca8db6955fae95`); the scope crosses teams | the prompt names the destinations, not where the rules live |
| Dynamic change | yes | yes | corrections met second and elsewhere: `68dc63484a5b2d0a869e758f`, `D0770ET1HV2/1759267800.858041`, `harmonygames-Games/match3d-backend#36#rc_1`, `D0770ET1HV2/1759160460.731000`, `cmt_zom293_1`, `f_5e40215b7d4d24b0455412`, `cmt_zom559_1` | the prompt names neither the first summary nor the correction |
| Multi-source | yes | yes | 11 services (manifest `services`) | no source named as an exact artifact beyond the three anchors and the thread |
| Async | no | — | `03_Error_Async_Config.txt` Friction: none | — |
| Error recovery | no | — | Friction: none | — |
| Access control | no | — | every needed record is visible (check-sql PASS) | — |

## 9 · Must not appear in the prompt

- Catalog tool names and parameters (`linear_list_comments`, `gsheets_values_update`, `slack_send_message`, …) and MCP server names (`Evals/references/tools/catalog.json`).
- Ids: any ZOM / ART / DES key, cmt_* ids, Slack ts, Drive f_ ids, evt_ ids, Trello ids, the PR `harmonygames-Games/match3d-backend#36`.
- Rules and findings: the scope rule, the severity words, "main at job start", "merged is not live", the update-row rule, the call vocabulary, any blocker, the cut times, Brian's Sep 29 findings, the dev-only chest rows, ZOM-293's lost boosters, the re-tests, the update-path failure, the vendor, "Puzzles vs Zombies".
- Format: markdown, numbered steps, column lists for the register.

## 10 · Entity traps

```

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
ENTITY email:vincent.parker@harmonygames.co  name=Vincent Parker  kind=person  emails=['vincent.parker@harmonygames.co']
  persona: vincent_parker - Game Systems Engineer / Engineering
  slack      id=EMPLOYEE_0012_SLACK_ID, name=Vincent Parker, real_name=Vincent Parker, email=vincent.parker@harmonygames.co, is_bot=False, deleted=False, messages=39854, first_post=2023-08-30, last_post=2025-09-30   [join: exact_email]
ENTITY email:arthur.blake@harmonygames.co  name=Arthur Blake  kind=person  emails=['arthur.blake@harmonygames.co']
  persona: arthur_blake - Co-founder & CTO / Executive
  slack      id=EMPLOYEE_0025_SLACK_ID, name=Arthur Blake, real_name=Arthur Blake, email=arthur.blake@harmonygames.co, is_bot=False, deleted=False, messages=35266, first_post=2023-03-20, last_post=2025-10-01   [join: exact_email]
ENTITY email:leonard.hayes@harmonygames.co  name=Leonard Hayes  kind=person  emails=['leonard.hayes@harmonygames.co']
  persona: leonard_hayes - Co-founder & Creative Director / Executive
  slack      id=EMPLOYEE_0038_SLACK_ID, name=Leonard Hayes, real_name=Leonard Hayes, email=leonard.hayes@harmonygames.co, is_bot=False, deleted=False, messages=129898, first_post=2023-03-15, last_post=2025-10-01   [join: exact_email]
ENTITY email:brian.foster@harmonygames.co  name=Brian Foster  kind=person  emails=['brian.foster@harmonygames.co']
  persona: brian_foster - Game Engineer / Engineering
  slack      id=EMPLOYEE_0026_SLACK_ID, name=Brian Foster, real_name=Brian Foster, email=brian.foster@harmonygames.co, is_bot=False, deleted=False, messages=28951, first_post=2024-06-06, last_post=2025-09-30   [join: exact_email]
ENTITY email:douglas@harmonygames.co  name=Douglas  kind=person  emails=['douglas@harmonygames.co']
  persona: douglas - Software Engineer / Engineering
  slack      id=EMPLOYEE_0031_SLACK_ID, name=Douglas, real_name=Douglas, email=douglas@harmonygames.co, is_bot=False, deleted=False, messages=13832, first_post=2023-09-01, last_post=2025-09-30   [join: exact_email]
ENTITY email:oliver.brooks@harmonygames.co  name=Oliver Brooks  kind=person  emails=['oliver.brooks@harmonygames.co']
  persona: oliver_brooks - Senior Game Engineer / Engineering
  slack      id=EMPLOYEE_0003_SLACK_ID, name=Oliver Brooks, real_name=Oliver Brooks, email=oliver.brooks@harmonygames.co, is_bot=False, deleted=False, messages=13475, first_post=2024-08-12, last_post=2025-09-30   [join: exact_email]
```

| Correct entity (exact) | Lookalike(s) | How they differ | Locator |
| --- | --- | --- | --- |
| Arthur Blake | "blake@" thread-file alias | the alias is a Gmail file name, not a person | arthur.blake@harmonygames.co |
| Oliver Brooks | Lauren Brooks | different person, not in this task | oliver.brooks@harmonygames.co |
| Zombie Match 3D | Puzzles vs Zombies | the pre-July name of the same game (page_qa_runbook) | `29016e2ba1a844a2509b847b` |
| harmonygames-Games/match3d-backend#36 | harmonygames-Games/match3d#36 | client PR with the same number | `harmonygames-Games/match3d-backend#36` |
| Android Submission #135 (Sep 30, Match3D) | DD Android Submission #135 (Jan 31, Domino Delights) | different game and job | `C05433XK267/1759257934.076209` vs `C05433XK267/1738328514.768779` |
| ZOM-562 | ZOM-516 (closed Duplicate, endless mode refill), ZOM-546 (draining refill) | different mechanism | `ZOM-562` |

## 11 · Pre-submit checklist

- [ ] The prompt names the three anchors only by noun phrase, the candidates by build name and the destination thread; no id.
- [ ] No rule, finding, count or vocabulary from §9.
- [ ] Every deliverable of §4 has a trigger in the prompt (§6).
- [ ] Relative dates resolve against Wed 1 Oct 2025 ("yesterday" = Tue 30 Sep; "Friday" = 3 Oct).
- [ ] Clean spelling; no markdown; one plain paragraph.
- [ ] `hardness_v2_check.py` RULE_IN_PROMPT clean.

## 12 · Blockers and routed defects

- Seeded facts are absent from the base search by construction (rows marked "routed" in §5a): each was seeded by `/create-injection` and check-sql proves it visible (dossier Self-review). No fact is unfindable from the record the prompt names.
- No unverified fact remains for the prompt itself; the ○ carriers (Contacts job, GCal description) are listed as dossier platform follow-ups.

## 13 · Self-review

| Area | Counter to a PASS | Resolution (evidence) |
| --- | --- | --- |
| Fair readings (UGT) | A run could list the blockers as a comment instead of editing the ticket and be marked wrong | the prompt pins the description; a comment is a different write, recorded as rejected in the outcome review (`ZOM-570`) |
| Fair readings (UGT) | ZOM-429 / ZOM-517 could be KNOWN ISSUE instead of FIXED | ungraded rows; "can't reproduce on #135 or #50" (`cmt_zom429_1`, `cmt_zom517_1`) matches H2's "A ticket counts as fixed when Vincent or Brian saw it working"; accepted outcomes record both |
| Clarity | "file a new ZM ticket in Linear for anything ... nobody has filed yet" could also cover the vendor's report | the vendor report maps to `ZOM-562` (already filed); the reuse rule `68dc3ef455344e471b1d2ea9` says no duplicates |
| Clarity | "the QA call" could be read as a per-ticket list | the thread asks for the gate before the go/no-go (`C08R27X0EAH/1759263900.484190`); a go / no-go call with the blockers is the natural reading, both forms accepted |
| Incorporation | The release ticket points to the rules without links | `ZOM-570` names "Leonard's submission rules" and "my note on how we cut submissions"; Drive search on those words finds `f_632c44650df44fe252ee59` / `f_a038a576ca8db6955fae95` (both shared with Vincent) |
| Incorporation | The runbook could hand over the answer | `page_qa_runbook` states the update rule, not the failing row; the row lives only in `f_5e40215b7d4d24b0455412` |
| Truthfulness | "Arthur cut yesterday" might be wrong for an Oct 1 persona | both jobs were started by Arthur on 2025-09-30 (`C05433XK267/1759257812.041449`, `C05433XK267/1759257934.076209`) |
| Truthfulness | "Arthur's candidates thread in #zombie-bugs" may not exist | `C08R27X0EAH/1759263900.484190` (seeded, check-sql YES) |
| Feasibility / ACL | Vincent might not be able to write the gate sheet | he owns `f_0ebfccf33076f9dbf086bc` (drive_files owner and sheets_spreadsheets owner) |
| Feasibility / ACL | The group DM or the GitHub / Linear comments could be scoped | Vincent is a party to `D0770ET1HV2` (five-member group DM) and to `D079SNE2TL4`; GitHub and Linear comments are unscoped (check-sql YES) |
| Contrived register | Naming the runbook could hint at the update-path trap | the runbook is Vincent's own gate document (owner line) and the prompt names its checks generally; the failing row stays in Brian's doc |
| Contrived register | The four asks could read as a deliverable catalogue | one purpose (the store gate), the screen-24 skeleton (do the work, put it here, tell them) |

Unresolved: none for the brief; the difficulty risk (forecast shard views near the 0.90 cap) is carried in the dossier.

```
STAGE GATE prompt-writing: PASS — Task_Authoring/task_inputs · 04_Prompt_Writing_Brief.md#25ac59db2409 · 00_Assigments.md#90d69427cab7 · 01_Grounding_Dossier.md#4f38db93303c · 01_Universe_Inject.sql#5a8d995238f3 · 03_Error_Async_Config.txt#af03ea097424 · 01a_Hardening_Report.md#795a1564ad1b · __context__#fb209f3058d7 · __assignment__#c2f3888d53bd · __policy__#dc4ab5df3cdd · __gate_policy__#9b78441396d8 · __review__#a0b18efc8b3c · blocking 0 · warnings 0 · checks 24
[PASS] assignment.v3_context: Vincent Parker / Game Systems Engineer; easy cap <90%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Writing_Brief.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql, 03_Error_Async_Config.txt, 01a_Hardening_Report.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#5a8d995238f3, 01_Hardness_Manifest.json#01a3caa4a5bf, 01_Grounding_Dossier.md#4f38db93303c, solver/solver.py#f7a6aeed38d8, 01c_Dispositions.json#0d69abd8f7ab, 01c_Preflight_Report.json#8fb3c8b8c94d, 00_Assigments.md#90d69427cab7, 01_Scenario_Design.md#087cccf519b5, 01_Hardness_Manifest.draft.json#35516411430b, 01_Gradable_Surface.json#e3001f0c8fa4, __context__#fb209f3058d7, __assignment__#c2f3888d53bd, __policy__#dc4ab5df3cdd, __gate_policy__#9b78441396d8, __review__#4c88e8308ed5)
[PASS] chain.error-async: upstream 'error-async' PASS pasted and current (03_Error_Async_Config.txt#af03ea097424, 00_Assigments.md#90d69427cab7, 01_Grounding_Dossier.md#4f38db93303c, 01_Universe_Inject.sql#5a8d995238f3, __context__#fb209f3058d7, __assignment__#c2f3888d53bd, __policy__#dc4ab5df3cdd, __gate_policy__#9b78441396d8, __review__#4c88e8308ed5)
[PASS] structure.sections: 14 required sections present and non-empty (04_Prompt_Writing_Brief.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Writing_Brief.md
[PASS] evidence.situation: 4/4 items carry a source pointer (min 100%)
[PASS] evidence.final_state: 18/18 items carry a source pointer (min 100%)
[PASS] evidence.discovery_map: 31/31 items carry a source pointer (min 100%)
[PASS] evidence.dates: 5/5 items carry a source pointer (min 100%)
[PASS] evidence.entity_traps: 6/6 items carry a source pointer (min 100%)
[PASS] tool.search_as_persona: 31 facts proven findable by persona_view search as vincent_parker
[PASS] reach.brief: 24 scoped load-bearing ids YES for vincent_parker
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] structure.accepted_outcomes: V3 accepts multiple fair outcomes; see v3.fair_outcomes_review
[PASS] boundary.anchor_naming: 3 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 10 evidenced counter-readings (of 12 found; need ≥ 6) in 04_Prompt_Writing_Brief.md
[PASS] review.coverage: self-review addresses all 6 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.fair_outcomes_review: current accepted outcomes and considered alternatives recorded; multiple fair outcomes are allowed
[PASS] handoff.pasted: pasted into the Self-review by --paste
```
