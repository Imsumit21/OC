# Prompt Brief — vincent-zm3d-release-gate · prep

> Built 2026-11-04 from 00_Assigments.md, Working_Files/00_Task_Context.json, Working_Files/01_Grounding_Dossier.md, 01_Universe_Inject.sql (sha256 @@SQLSHA@@), Working_Files/01_Hardness_Manifest.json, Working_Files/01_Scenario_Design.md, Working_Files/01_Gradable_Surface.json, Working_Files/solver/truth.json, 03_Error_Async_Config.txt · Persona view verified: all (check-sql PASS, 0 load-bearing rows not visible)
> Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) · seed bound 2025-10-01T00:00:00Z · persona today Wednesday 1 Oct 2025
> 04_Prompt.txt may be drafted by Claude or Codex (/create-prompt-writing draft) or written by the human.

## 1 · Assignment fit

| Axis | Assigned value | What it requires here (cited) |
| --- | --- | --- |
| Business function | Engineering → Engineering & Technical Operations | Build, release and quality work (`Evals/references/rules/task_categories.md`); the gate decides whether the ZM store candidates (`C05433XK267/1759263189.219529`, `C05433XK267/1759259749.259909`) ship. |
| Persona | Vincent Parker, `vincent.parker@harmonygames.co`, Game Systems Engineer, Engineering (roster persona_key vincent_parker; Slack `EMPLOYEE_0012_SLACK_ID`; Linear `usr_65c76e0b87aa7e9b`) | Voice and remit in one line: the QA owner of both games (page_qa_runbook "Owned by QA (Vincent Parker)"; page_release_checklist "Owner: Vincent Parker (QA)"), writes short build-tagged bug notes; read scope: #zombie-bugs `C08R27X0EAH`, #builds `C05433XK267`, DMs `D0770ET1HV2` and `D079SNE2TL4` (Douglas), GitHub `harmonygames-Games/match3d-backend#36` with its reviews and inline review comments, his mailbox and Drive. |
| Competency | Engineering Ops | Release readiness, QA gates and build tracking (`Task_Authoring/references/Taxonomy_V2_Step_Map.md`, Engineering Ops). Remit: the release checklist makes QA sign-off "a hard gate" before any store submission, and Arthur's release ticket `ZOM-570` assigns the gate to Vincent. |
| Task skill | Analysis and synthesis | Combine many records into one judgement per item and an overall call: 132 register rows, each decided by the ticket, its QA notes (Linear comments), the build cut (#builds, GitHub), re-tests in Slack / Trello and the two rule docs (`@@doc_h2@@`, `@@doc_h1@@`); the sign-off synthesises them. |
| Task type | Long Horizon; effective profile extreme (dossier §4 pastes HARDNESS GATE (extreme): PASS) | Services carrying weight: linear (132 register rows, ~60 seeded QA notes, the release ticket), slack (#builds job starts and change lists, #zombie-bugs thread, two DMs), gdocs / gdrive (four rule docs, the update-path log), gsheets (gate sheet, regression matrix), github (`harmonygames-Games/match3d-backend#36`, match3d PR merge times), trello (`68d1eb90bef538c7c5c5599d`), gmail (vendor notes), contacts, gcal, confluence (base runbook pages). Call budget 251 (manifest `call_budget`, requester-confirmed floor 250). |
| Difficulty mode | easy, cap 0.90 | Six Opus 5.5 baselines must average below 90% with fewer than five full passes (`Working_Files/00_Task_Context.json /difficulty_cap`); design target 62–77%. |
| Freeze and clock | seed bound `2025-10-01T00:00:00Z`; eval clock 2025-10-01 07:00 UTC = Wed 1 Oct 2025 00:00 PT | The candidates were started on Tue 30 Sep 2025 at 11:43 / 11:45 PT (`C05433XK267/1759257812.041449`, `C05433XK267/1759257934.076209`), "yesterday" for the persona; the go/no-go is Fri 3 Oct 2025 9:00 PT (`evt_81e6dc4dbfd331f1a6a317`). |

## 2 · Situation

| Symptom | Seen by | Where it shows (locator) | Relevant records the persona cannot see |
| --- | --- | --- | --- |
| Arthur cut the ZM store candidates and opened a store release ticket asking QA for the gate before Friday's go/no-go. | Vincent, the ticket's assignee | `ZOM-570` (2025-09-30T20:20Z, creator `usr_cc3e90160f490686`) | none (Linear is unscoped) |
| Arthur posted the candidates in #zombie-bugs, @-mentioning Vincent; Brian replied that the regression matrix is green. | Vincent, channel member | `C08R27X0EAH/1759263900.484190`, reply `C08R27X0EAH/1759266600.265963` | none |
| Vincent's release gate sheet holds the "How we gate" tab and the previous gate's tab for #127 / #40. | Vincent, the owner | `@@gate_sheet@@` | none |
| The go/no-go for the store push is on Vincent's calendar for Friday. | Vincent, an invited guest | `evt_81e6dc4dbfd331f1a6a317` | the other attendees' own calendar copies |

## 3 · Investigation → action

Questions (no answers):

- Which tickets does the gate cover, by the rules the release ticket points to (`ZOM-570`, `@@doc_h2@@`)?
- For each ticket moved to Done since the last gate, is its change in the candidate builds or live on prod (`@@doc_h1@@`, #builds `C05433XK267`, match3d and match3d-backend PRs)?
- What does the latest QA check on the candidates (or on prod) say for each ticket (Linear comments, #zombie-bugs, DMs, the ZM ROADMAP card `68d1eb90bef538c7c5c5599d`)?
- How bad is each remaining defect under the rules, and does an outside report change that (`vincent.parker@harmonygames.co/1844730396672762606`)?
- Does the regression matrix pass the runbook's gate, every row included (`page_qa_runbook`, `@@matrix_sheet@@`, `@@update_log@@`)?
- What does the gate sheet expect (`@@gate_sheet@@`, "How we gate"), and how do blockers go on the release ticket (`68dc3ef455344e471b1d2ea9`)?

Writes:

- The register in a new tab of `@@gate_sheet@@`.
- The blocker list on `ZOM-570` (existing ticket keys).
- A new Linear ticket for each failure nobody has filed yet (the update-path failure on iOS #50).
- A reply in Arthur's thread `C08R27X0EAH/1759263900.484190` with the QA call.

Every write depends on the investigation: the register needs each ticket's build status and call, the blocker list needs the BLOCKER set, the new ticket needs the matrix check and the "already filed?" check, and the reply needs the blocker list.

## 4 · Pinned final state (UGT anchor)

| Deliverable | Required contents | Destination | Recipients | Catalog write | Fed by |
| --- | --- | --- | --- | --- | --- |
| 1 · Register | One row per in-scope ticket (132), each with ticket, title, build status, QA result, call (BLOCKER / KNOWN ISSUE / FIXED / NO CALL) and evidence | a new tab in `@@gate_sheet@@` (ZM3D Release Gate, owner vincent.parker@harmonygames.co) | no recipient | `gsheets_batch_update` (add sheet) + `gsheets_values_update` | `@@doc_h2@@`, `@@doc_h1@@`, `ZOM-570`, per-ticket comments, #builds `C05433XK267` |
| 2 · Blocker list | Every BLOCKER by its existing key: @@BLOCKERS@@ | the description of `ZOM-570` | no recipient | `linear_update_issue` (description) | the register's BLOCKER rows; reuse rule `68dc3ef455344e471b1d2ea9` |
| 3 · New ticket | One Linear bug for the failed update from the N-1 store build (the App Store build) to iOS Submission #50 with device (iPhone 13), OS (iOS 18.6), source build (N-1, App Store) and repro | team `team_ZOM` | no recipient | `linear_create_issue` | `@@update_log@@`, `page_qa_runbook`, `page_release_checklist` |
| 4 · Sign-off | The QA call: the candidates are not ready (blockers listed / no-go) | reply in the thread of `C08R27X0EAH/1759263900.484190` | Arthur Blake `EMPLOYEE_0025_SLACK_ID` and the channel | `slack_send_message` (channel `C08R27X0EAH`, thread_ts 1759263900.484190) | the blocker list; Leonard's note `cmt_zom570_1` |

Alternatives a careful run could defend:

- The blocker list added below Arthur's text in the `ZOM-570` description or with the description rewritten around it; keys in any order, with or without titles. A comment on `ZOM-570` instead is a different write (the prompt asks for the description). The new update-path ticket goes on the list by its new key (`ZOM-570`: "by key, the existing ticket if there is one").
- The new update-path ticket labelled Bug or not; priority free; it gets a register row as a BLOCKER (`@@doc_h2@@`, Sep 23: "From the next gate on, tickets filed while the gate is running get a row too").
- Register columns in the "How we gate" order or a superset; calls in capitals or mixed case; the evidence column as ids or links (`@@gate_sheet@@`).
- The tab name in `@@gate_sheet@@`: anything naming the candidates or the date (e.g. "Sep 30 - Android #135 / iOS #50").
- The sign-off wording in the thread `C08R27X0EAH/1759263900.484190`: "no-go", "not ready", "hold" or "blocked", with or without the blocker keys; also sent to the channel is fine.

### 4b · Canonical outcome (all fair outcomes)

| Deliverable | Field | Fixed value (or closed accepted set, with sources) | Delegated by (quoted span, or —) | Allowed equivalence class | Material / representational |
| --- | --- | --- | --- | --- | --- |
| Register | Row set | Exactly the 132 keys of `scenario_gen/scope_keys.json` (`solver/truth.json`): every open ZOM ticket except ZOM-359 / ZOM-475 and the release ticket `ZOM-570`, ART-790, ART-792, ART-793, DES-313, and every ticket moved to Done after the Sep 22 builds were cut (18 base + ZOM-567, ZOM-569) | `@@doc_h2@@`: "every ZM ticket that's still open (any state but Done, Canceled or Duplicate), whatever team or label" | Rows in any order; plus one row for the new update-path ticket (`@@doc_h2@@`); extra columns allowed | Material |
| Register | Call per row | As `solver/truth.json`: samples ZOM-569 BLOCKER, ZOM-567 BLOCKER, ZOM-435 BLOCKER, ZOM-473 BLOCKER, ZOM-562 BLOCKER, ART-793 KNOWN ISSUE, DES-313 BLOCKER, ZOM-578 BLOCKER, ZOM-563 FIXED, ZOM-559 BLOCKER, ZOM-560 BLOCKER, ZOM-481 KNOWN ISSUE, ZOM-458 BLOCKER, ZOM-535 BLOCKER, ZOM-293 BLOCKER, ZOM-564 FIXED, ZOM-506 FIXED, ZOM-557 FIXED, ZOM-561 FIXED, ZOM-513 NO CALL, ZOM-387 NO CALL; totals 18 BLOCKER / 19 KNOWN ISSUE / 10 FIXED / 85 NO CALL, the blocker set being the 18 keys plus the new update-path ticket | — (rules in `@@doc_h2@@`) | The four call words in any case | Material |
| Register | Build status | By the "build status means" row of `@@gate_sheet@@` "How we gate": ZOM-569 not in candidate; ZOM-567 server – not live; ZOM-563 server – live; Done bugs closed before 18:43Z and bugs QA saw working on the candidates (ZOM-429, ZOM-517, ZOM-564) in candidate; open bugs not seen working and every no-call ticket n/a | `@@gate_sheet@@` "How we gate" vocabulary | Equivalent wording ("not in #135 / #50", "merged, not deployed") | Material for ZOM-569 / ZOM-567; representational otherwise |
| Register | Tab | A new tab of `@@gate_sheet@@` | prompt "a new tab of my release gate sheet" | Any tab name | Material tab; representational name |
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
| 3 · Leonard's rules H2 | scope, verification, severity | `@@doc_h2@@` | YES — shared with Vincent | ZOM-570 names "Leonard's submission rules" | medium — a Drive doc, not mail | No |
| 4 · Arthur's build rules H1 | main at job start; merged is not live | `@@doc_h1@@` | YES — shared | ZOM-570 names "my note on how we cut submissions" | medium | No |
| 5 · Sep 2 hotfix doc (decoy) | hotfix submissions from release/1.3.24_HotFix | `@@doc_h1_decoy@@` | YES — shared | met by the same Drive search; overturned by H1 | medium | No |
| 6 · July beta-drop doc (decoy) | only crashes and wipes block a beta drop | `@@doc_h2_decoy@@` | YES — shared | met by the same search; different lot | medium | No |
| 7 · Gate sheet | "How we gate" tab, Sep 22 tab | `@@gate_sheet@@` | YES — owner | the Sep 22 tab is met first (stale calls, Bug-only scope) | low | Yes (anchor A3) |
| 8 · Submission job starts | #50 18:43:32Z, #135 18:45:34Z, both main | `C05433XK267/1759257812.041449`, `C05433XK267/1759257934.076209` | YES — #builds member | evidence for every Done row | medium — 450 Jenkins posts | Yes (the build names only) |
| 9 · The post-cut fix | #2028 started 21:36Z with "Fix season pass main screen instance from join popup" | `C05433XK267/1759268201.182309`, `C05433XK267/1759268589.049939` | YES | overturns ZOM-569's Done | high — a dev build, not a submission | No |
| 10 · ZOM-569 Done | ticket closed 18:05Z right after "fixed on my branch, the join popup only opens one SP screen now" (18:02Z) | `ZOM-569`, `cmt_zom569_1` | YES — Linear | claim met first (T1) | high | No |
| 11 · Backend PR approval and rollout | merged with Arthur's APPROVED review `#36#rev_1` (empty body, like the repo's other 30), then Douglas's 22:01:52Z "#36 is rolled out to prod too, the container is up. that's the code side" | `harmonygames-Games/match3d-backend#36`, `harmonygames-Games/match3d-backend#36#rev_1`, `D079SNE2TL4/1759269712.483915` | YES — GitHub, DM party | claim met first (T2) | high | No |
| 12 · Arthur's inline review comment | the migration's chest rows are read on prod but are still only on dev (rolled out is not migrated) | `harmonygames-Games/match3d-backend#36#rc_1`, under the COMMENTED review `#36#rev_2` (22:40Z) | YES — GitHub unscoped | overturning (T2) | high — an inline comment with no Slack copy (INT-01 mirrors match3d only) | No |
| 13 · CI/CD page | "CI stops here", deploy "Run by hand" | `page_cicd_pipeline` | YES — Confluence | supports H1 | low | No |
| 14 · Vincent's #133 pass | ZOM-435 ok on #133 | `C08R27X0EAH/1759140300.935009` | YES | claim met first (T3) | high | No |
| 15 · Leonard's Trello re-test | stuck on the trophy path on #135 | `68dc63484a5b2d0a869e758f` on `68d1eb90bef538c7c5c5599d` | YES — Trello | overturns the pass (T3) | high — a card comment | No |
| 16 · Brian's DM re-test | ZOM-473 still skippable on iOS #50 (Turkish) | `D0770ET1HV2/1759267800.858041` | YES — DM party | overturns ZOM-473's Done (T3b) | high — Turkish DM | No |
| 17 · Brian's green reply | "regression matrix green on #135 and #50" | `C08R27X0EAH/1759266600.265963`, `@@matrix_sheet@@` | YES | claim met first (T4) | high — sounds conclusive | No |
| 18 · Update-path log | update from the N-1 store build to iOS #50 FAIL (level 1, 500 coins) | `@@update_log@@`; pointer `D0770ET1HV2/1759272300.342229` | YES — shared | overturns the green reply (T4) | high | No |
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

@@SAP_TABLE@@

@@SAP_PASTES@@

## 6 · Triggers, incorporation and implicit requirements

| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · persona-readable · unique · instructions-not-answer) | Inferable |
| --- | --- | --- | --- | --- |
| R1 scope of the register | `@@doc_h2@@` | deliverable ("the gate register") | `ZOM-570` → "Leonard's submission rules" · readable · one doc with that title · states the rule, not the row list | gotcha → triggered by the register ask and the release ticket |
| R2 build status | `@@doc_h1@@` | scope (the named candidates) | `ZOM-570` → "my note on how we cut submissions" · readable · unique · rule only | gotcha → triggered |
| R3 QA result | `@@doc_h2@@` | deliverable (register) | as R1 | inferable for a QA gate; the latest-on-candidate rule is in H2 |
| R4 backend liveness | `@@doc_h1@@` + `page_cicd_pipeline` | scope | as R2 | gotcha → triggered through H1 |
| R5 calls | `@@doc_h2@@` | deliverable (register, blockers) | as R1 | gotcha → triggered |
| R6 matrix verdict | `page_qa_runbook` | constraint ("the checks in the QA regression runbook") | the runbook page · readable · unique · rule | triggered |
| R7 blockers on the ticket | `ZOM-570`, `68dc3ef455344e471b1d2ea9` | deliverable ("add the blockers to the release ticket's description") | ZOM-570 → "I'm putting the reuse rule on the tech-issues card" | triggered |
| R8 sign-off reply | `C08R27X0EAH/1759263900.484190` | recipient / destination | named in the prompt | triggered |
| R9 new ticket | `page_release_checklist`, `@@update_log@@` | deliverable ("file a new ZM ticket in Linear for anything ... nobody has filed yet") | the runbook / checklist "file the bug" rule | triggered |
| R10 register format | `@@gate_sheet@@` "How we gate" | destination ("a new tab of my release gate sheet") | the sheet itself | triggered |

| Anchor | May be named (noun phrases only) | Record |
| --- | --- | --- |
| A1 | the store release ticket; the release ticket | ZOM-570 |
| A2 | the QA regression runbook; the regression runbook | page_qa_runbook |
| A3 | my release gate sheet; the gate sheet | @@gate_sheet@@ |

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
| Ambiguity | yes | yes | the rules live in two Drive docs the release ticket names by description (`@@doc_h2@@`, `@@doc_h1@@`); the scope crosses teams | the prompt names the destinations, not where the rules live |
| Dynamic change | yes | yes | corrections met second and elsewhere: `68dc63484a5b2d0a869e758f`, `D0770ET1HV2/1759267800.858041`, `harmonygames-Games/match3d-backend#36#rc_1`, `D0770ET1HV2/1759160460.731000`, `cmt_zom293_1`, `@@update_log@@`, `cmt_zom559_1` | the prompt names neither the first summary nor the correction |
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
@@COLLISIONS@@
@@RESOLVE@@
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
| Incorporation | The release ticket points to the rules without links | `ZOM-570` names "Leonard's submission rules" and "my note on how we cut submissions"; Drive search on those words finds `@@doc_h2@@` / `@@doc_h1@@` (both shared with Vincent) |
| Incorporation | The runbook could hand over the answer | `page_qa_runbook` states the update rule, not the failing row; the row lives only in `@@update_log@@` |
| Truthfulness | "Arthur cut yesterday" might be wrong for an Oct 1 persona | both jobs were started by Arthur on 2025-09-30 (`C05433XK267/1759257812.041449`, `C05433XK267/1759257934.076209`) |
| Truthfulness | "Arthur's candidates thread in #zombie-bugs" may not exist | `C08R27X0EAH/1759263900.484190` (seeded, check-sql YES) |
| Feasibility / ACL | Vincent might not be able to write the gate sheet | he owns `@@gate_sheet@@` (drive_files owner and sheets_spreadsheets owner) |
| Feasibility / ACL | The group DM or the GitHub / Linear comments could be scoped | Vincent is a party to `D0770ET1HV2` (five-member group DM) and to `D079SNE2TL4`; GitHub and Linear comments are unscoped (check-sql YES) |
| Contrived register | Naming the runbook could hint at the update-path trap | the runbook is Vincent's own gate document (owner line) and the prompt names its checks generally; the failing row stays in Brian's doc |
| Contrived register | The four asks could read as a deliverable catalogue | one purpose (the store gate), the screen-24 skeleton (do the work, put it here, tell them) |

Unresolved: none for the brief; the difficulty risk (forecast shard views near the 0.90 cap) is carried in the dossier.
