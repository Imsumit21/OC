# Scenario Atlas — verified HarmonyGames storylines for extreme tasks
`<U>/<P>_HarmonyGames_*` = the selected universe folder and prefix (`Universe_Normal/Normal_…` for Feb 14, 2026; `Universe_SynthCut/SynthCut_…` for Oct 1, 2025).

> **V3 use:** The assigned universe date selects the universe (GEN_EXECUTION § 0a): Feb 14, 2026 → normal, Oct 1, 2025 → synth-cut. Read only that universe, apply its state rules and clock, and stop if the date is missing — there is no default.
> Compiled from the older Feb 14 export; reference-only for both universes until re-verified against the selected universe. Lines tagged [normal-only] do not exist on Oct 1 (synth-cut).
> Storylines below
> span dates before and after the cut; verify every selected fact at the assigned
> freeze. Later-edited bodies need dated history or independent earlier evidence.
> Atlas summaries are leads, not a dataset gate.
> Accept every fair outcome and use V3 prompt/rubric rules from GEN_EXECUTION.
> Existing extreme/normal design targets are preserved local policy.

> 17 storylines (8 engineering/product/live-ops + 2 reserves, 7 business/finance/wind-down) that **natively span 9–13 services**, with per-service anchor IDs verified by exact lookup on 2026-10-03, persona read-reach, natural contradictions usable as traps, data volume, and the injection needed to reach 10–13 services. Input to `playbooks/01_Scenario_Design.md` §S1.

## Read before using any storyline

1. **Persona gate.** Only the 17 personas in `Evals/references/persona/roster.json` pass `/prompt`. Tim Steudler (0 Slack channels, no mailbox, no Drive) and Thomas (mail ends Apr 2025, no 2025 calendar) cannot carry these. Simon Walker has no Drive root and reaches little beyond `#analytics`. Victor Barnes departed April 2025 (last Slack 2025-04-15) — cannot review, approve or reply in either universe.
2. **Coherence risk.** The Evals fail Cross-Service Coherence on *any* inconsistency in task-touched data, even pre-existing. The contradictions listed below are powerful traps **only** when they are framed as dated human claims overturned by records (a Slack summary vs Snowflake rows). Where two system fields silently disagree (e.g. Snowflake `CASH_BALANCE` vs the P&L sheets, ~$37K/month apart; warehouse rows `completed` where Slack reports outages), either keep the task off that field, or make the reconciliation the explicit, incorporated job and record it as an intended disagreement — expect reviewer scrutiny.
3. **Unreadable files.** Drive-family files owned by `Resource: -6481757892984311338` with empty sharing are readable by **no** persona (several GDDs, the Wind Down folder, some P&L versions, the Season Pass economy workbooks). They are access boundaries, not evidence. `domain`/`anyone` visibility is unverified — do not count it as reach.
4. **Private channels.** `#season-pass`, `#leaderboards`, `#difficulty-optimization`, `#dd_economy_v2`, `#4day-quests`, `#winandcollect`, `#winddown`, `#admin_foundersonly`, `#executives` — check membership for the persona.
5. **Originality.** Do not reuse the ML-selected Combo Fighters launch record or the calibration tasks (133-PR residue register, RC-flag gate, art-canon handoff control). Combo Fighter data can be used from a different angle (Reserve A).
6. **Sensitive content.** `#winddown` ts `1770858495.115779` and its next reply `1770858501.263569` contain a pasted OAuth client secret. Never make a requirement, fact or seeded record depend on or repeat them.
7. **Storyline YAMLs are not ground truth** (`<U>/<P>_HarmonyGames_Other_Services/metadata/*.yaml`): their figures disagree with the data (e.g. the fundraising cash figures). Ground every fact in the exports.
8. **Calendar is the most common gap** for engineering storylines; most need GCal injection to carry weight (one row per attendee calendar).
9. **Overlap.** Storylines 1 and 2 share ENG-1892 and the quest outage — use one angle per task.
10. **Who is active at the clock.** Vincent Parker left in Nov 2025; Douglas is silent after Aug 2025. Give a seeded Feb 2026 message only to someone still active (founders, Julia, Brian, Oliver, Owen …) — check their last activity first. [normal-only] On Oct 1, 2025 every roster persona except Victor Barnes (departed April 2025) is active through 2025-09-30.
11. **Mailbox file names ≠ roster emails.** Gmail exports are filed by mailbox (`blake@harmonygames.co_…` for Arthur, `leonard@harmonygames.co_…`) while thread ids and headers use the roster address (`arthur.blake@…`). Search by both when proving reach.
12. **Contradiction types.** Below, "contradiction" covers two kinds. **Human claim vs record** (a Slack/mail statement that a record later overturns) is usable as an A1 trap. **System field vs system field** (warehouse rows vs Slack outage reports, Snowflake cash vs P&L sheets, two Confluence pages giving different root causes as fact) fails Cross-Service Coherence on presence — keep those records out of the task, or make reconciling them the explicit, incorporated job.

## Cohort notes (from the first engine test, Oct 4)

| Candidate cohort | Size | Status |
|---|---|---|
| Open ENG/ZOM defects (state Bugs or Regression, or label Bug) | 73 | **Coherent**; used by `support/examples/sample_task_01` (pick another selection rule or angle for a real task). List calls return most fields → add seeded per-record surfaces (`Hardness_Mastery.md` §2.5) |
| Linear issues in state "PR" (ENG-2414…2435) | ~22 | **Avoid** — several have merged PRs while still in state PR (State/Lifecycle inconsistency fails coherence on presence) |
| GitHub PRs selected through a Linear/Slack-defined set | varies | Allowed if selection, surfaces and vocabulary differ from the calibration register (§2.5 pattern 3) |
| Crashlytics "Trending stability issues" digests | ~900 mails | Weak — heavy redaction noise, hard to make decidable |
| `#live-incidents` thread roots | ~120 threads | Weak as a cohort — conversational, outcomes rarely decidable; good as per-record reply surfaces |

---

# Part A — Engineering, live-ops, product, design and analytics

## How this was checked
- The raw exports were streamed and indexed directly: Slack (687,230 messages, 985 conversations), Gmail (88,726 thread files), the Drive family, GCal, Linear, GitHub, Trello, Confluence, Contacts, and Snowflake table metadata, row counts and row scans.
- Every ID below was checked by an exact lookup in the source:
  - Linear identifiers, GitHub PR ids, Trello card ids, Docs/Sheets/Slides ids, GCal event ids and Gmail thread files were bulk-checked; **0 were missing**.
  - Slack timestamps were read directly from `messages/<channel>/<month>.json`.
- Read access was worked out from the actual fields:
  - Slack: channel `members`.
  - Gmail: the thread's mailbox `user_email`.
  - Drive family: `owner_email` plus `shared_with_emails`. The `domain` and `anyone` visibility values are **not verified**, so they are not counted as access.
  - GCal: the event's `calendar_id`.
  - Confluence and Snowflake are unscoped.
- Two Drive-family traps apply to every storyline:
  - Files owned by `Resource: -6481757892984311338` with an empty share list cannot be read by any persona. These are deliberate access-control boundaries.
  - Slack channels `#season-pass`, `#leaderboards`, `#difficulty-optimization`, `#dd_economy_v2`, `#4day-quests` and `#winandcollect` are private.

## Ranking (service coverage × how tightly the records connect × volume)

| # | Storyline | Window | Services with natural records | Best persona |
|---|---|---|---|---|
| 1 | Domino Delights live-ops reliability and player-compensation record | Nov 2024 – Dec 2025 | 12–13 | Arthur Blake (Douglas, Vincent Parker) |
| 2 | Quest system lifecycle (Domino Delights → Zombie Match 3D → Zombie Lite) [after 2025-09-30: normal-only] | Feb 2024 – Nov 2025 | 12–13 | Douglas or Oliver Brooks |
| 3 | Season Pass (Domino Delights dry run → match3d PR #438 → $0 seasons) | Jan 2025 – Feb 2026 | 12 (calendar thin) | Oliver Brooks or Brian Foster |
| 4 | Leaderboards and leagues | Aug 2024 – Nov 2025 | 12 | Douglas or Vincent Parker |
| 5 | Domino Delights economy v2: April 2025 coin cut → Dec 2025 lives-to-tickets change | Mar – Dec 2025 | 11–12 (Linear thin) | Brian Foster, Owen Baker, Arthur Blake |
| 6 | Difficulty optimisation: Bayesian pity → bot auto-tuning → Zombie Match 3D dynamic difficulty [after 2025-09-30: normal-only] | Mar – Oct 2025 | 12 | Julia Lawson or Brian Foster |
| 7 | Collect & Win: Domino Delights 2024 → Zombie Match 3D rebuild → Magical Wings | Jul 2024 – Nov 2025 | 11 | Brian Foster |
| 8 | Domino Delights web port: Telegram → CrazyGames/BoomBit WebGL under 250 MB | Oct 2025 – Feb 2026 | 9–10 (no Trello, Confluence or Snowflake) | Arthur Blake or Owen Baker |
| Reserve A | Combo Fighter monetisation readiness (shop, IAP, push) [normal-only], not the calibration launch record | Nov 2025 – Feb 2026 | 10 (no Linear or Trello) | Brian Foster or Martin Walsh |
| Reserve B | Ad monetisation (Nov 2024 build → Apr 2025 interstitial silencing) | Sep 2024 – Apr 2025 | about 11 | Vincent Parker |

**Reading-reach counts per persona.** These count, inside each storyline's window and topic search, readable Slack messages, Gmail threads, GCal events and Drive-family files (title or body match). They are rough indicators:
- Live-ops record: Arthur 1,536 Slack / 252 Gmail / 1 GCal / 183 files; Douglas 930 / 52 / 1 / 13; Vincent 1,265 / 24 / 1 / 37.
- Quests: Douglas 1,784 / 24 / 3 / 13; Oliver 1,725 / 65 / 0 / 10.
- Season Pass: Oliver 295 / 16 / 0 / 4; Brian 326 / 3 / 0 / 8.
- Leaderboards: Douglas 789 / 14 / 2 / 12.
- Economy: Arthur 217 / 10 / 1 / 84; Brian 174 / 4 / 0 / 13; Owen 121 / 3 / 1 / 8.
- Difficulty: Julia 605 / 2 / 3 / 17; Brian 607 / 4 / 1 / 12.
- Collect & Win: Brian 362 / 8 / 3 / 9.
- Web port: Arthur 503 / 16 / 1 / 52.
- Simon Walker reaches almost none of this (only `#analytics`).

---

## 1. Domino Delights live-ops reliability and player-compensation record (Nov 2024 – Dec 2025)

**Summary.** `#live-incidents` was created during the quest outage of 15 Nov 2024 (first message 2024-11-15 18:51). It then tracked:
- the Domino Delights client-crash window of 10–16 May 2025;
- a weekend event-scheduler stall on 29 Jun 2025, which recurred on 11–12 Jul and was never marked restored;
- lives and coin balances going negative (ENG-2277 opened Apr 2025, ENG-2400 opened Nov 2025, both still open);
- events still being scheduled by hand on 27 Oct and 30 Nov 2025.

A player-compensation tool was ticketed but cancelled (ENG-1972), its follow-up stayed in Todo (ENG-2275), and every case was cleared by a manual lives grant. This is a strong "what actually happened versus what the documents and the warehouse say" task.

**Anchors by service**
- **Slack**
  - `C080X4GTZ0E` `#live-incidents`: 1,223 messages; by month 2024-11: 370, 2024-12: 179, 2025-01: 129, 2025-05: 108, 2025-07: 128, 2025-08: 98, 2025-10: 120, 2025-12: 29.
  - 2024-11-15: 1731696783.951159 (Leonard, "quests were not populating"); 1731697106.406839 (Arthur, "remove the auto-deploy of quests changes"); 1731699013.950769 ("removed the ad quest"); 1731707654.056579 (Oliver); 1731732000.476809 (Oliver, "merged big quest fix").
  - 2024-11-19 1732005140.008099 (Vincent, "testflight 0.68 quests are not working").
  - 2025-06-29 1751200739.524289 (Vincent, events not active in prod).
  - Jul 2025: 1752340681.703169, 1752357557.890929 ("River Rush, streak rush and Axe Arena are not working"), 1752436413.254079 (lives falling from 13 Jul 03:41).
  - Douglas's manual lives grants: 1752463834.941969 (14 Jul), 1752887733.007009 (19 Jul), 1753393461.138239 (24 Jul); also 1753742541.842929.
  - 1761559828.410849 and 1761577411.505979 (27 Oct, scheduler triggered by hand); 1762088965.657729 (ENG-2400 filed); 1764532627.291559 (30 Nov, "tournaments haven't restarted for weeks").
  - Top threads: 1732588984.980229 (55 replies), 1737753024.888769 (39).
- **Gmail**
  - Helpshift "New Domino Delights iOS/Android issue #N" emails: 182 distinct issues (#2–#226), 218 threads in Leonard's mailbox and 149 in Arthur's. Examples: issue #118 opened 2025-07-12 (`00000543.json`); Leonard's reply thread `leonard@harmonygames.co_1837475870152168022.json`.
  - Crashlytics "Trending stability issues" emails: about 384 in Arthur's mailbox, about 502 in Douglas's.
  - Linear notifications: `douglas@harmonygames.co_1829035630999538536.json` (ENG-2275 assigned); `oliver@harmonygames.co_1815819291614578291.json` and `..._1816087891092948345.json` (ENG-1892 assigned / Done).
- **Linear:** ENG-1892 (Done; created 2024-11-15T17:42:53Z, completed 2024-11-18T17:44:37Z); ENG-1972 (Canceled 2025-05-05); ENG-2275 (Todo); ENG-2277 (Bugs); ENG-2400 (Bugs); ZOM-459 (Done); ENG-1843.
- **GitHub**
  - `liveops#2` "Reset Quest Progress Function & Cron Events".
  - `GameOfDominoes#1458`, `#1464`, `#1468` (quest fixes, 16–19 Nov 2024); `#1306` "Quest Safety Checks".
  - `game-of-dominoes-backend#50` "Liveops calendar fixes" (2025-04-16).
  - `game-of-dominoes-backend#79` "Admin Endpoints and Store Catalog": opened 2025-09-10, merged 2025-12-03, 25 CodeRabbit comments.
  - `liveops-dashboard-buddy#1–#3`: an admin dashboard built in Aug 2025, all merged.
- **Confluence** (all unscoped):
  - `page_live_ops_engine` (Douglas, v3; comments by Arthur and Douglas, 2025-07-28).
  - `page_liveops_calendar` (Leonard, v3, 2026-01-31).
  - `page_quest_postmortem` (Arthur, v1–v3; comments `comment_quest_postmortem_c1` and `_c2`).
  - `page_support_playbook` (Vincent).
- **Snowflake**
  - `LIVE_OPS.EVENTS.LIVE_EVENT_PERFORMANCE`: 827 rows. 31 Domino Delights rows flagged "scheduler outage" (event starts 7–24 Jul 2025, ending by 27 Jul); 17 in the crash window; 5 Plague Race rows for ZOM-459; `EVT-0024` Weekly Quests 2024-11-11..17 status `failed`.
  - `ANALYTICS.MARKETING.APP_STORE_REVIEWS`: 490 incident-related reviews (DD 2024-11: 81, 2025-05: 243, 2025-07: 82; ZM 2025-08: 84).
  - `ANALYTICS.RAW_TELEMETRY.CLIENT_ERROR_EVENTS` (40,292 rows) and `ANALYTICS.GAME_EVENTS.PLAYER_DAILY_PROGRESS` (183,033 rows).
- **Sheets:** "DD - Event and League Bots" `f_23dc18d9d6ca57fe86fadd` (Vincent; tabs Plague Race, Axe Arena, Streak Fever, River Rush, Wood→King Leagues); "Live Ops Planning" `f_56a427d6933e193d7a6dbf` (Leonard, shared with 15).
- **Docs:** "DD QA Checklist" `f_5ad74e75c94ee1fe949b4f` (Vincent); "[LiveOps] Streak Fever" `f_97bbbdbf4a6078fa98e7a0` (17 personas can read); "DD Global Launch Readiness" `f_c57724584820a26f3bbe54` (16 can read).
- **Drive:** `f_f885b281bd11fbd5ae3df9` "Harmony Games_Engine_LiveOps_Short_Deck.pdf" and `f_63a3c63d1e6f7dfeb0993e` LiveOps_Engine.mp4 captions (both Leonard only).
- **Slides:** board decks claiming "Automated live events…": `f_868157b0665dcb6c16153a` (BoD Apr 16 2025), `f_7793bb93e59e9c0dee5129` (BoD Jul 16 2025). Readable by Leonard, Arthur, Robert, Frederick.
- **Trello:** `673796371c1ccb06376d5a4e` "incident channel"; `678027521a2c7a193d6b6565` "Live Ops Debugger – Pending on Douglas"; `66e7354337c16d06e67706a7` Helpshift implementation.
- **GCal (thin):** "Live Ops Leads" 2025-01-09 (`evt_7c3c76fef8c4a75f0f9864` Brian, `evt_cceb3498dd8817c2790f48` Vincent); "live ops chat" `evt_5b1dba4288330bbead21f6` (Arthur).
- **Contacts:** Douglas `/contacts/137` (the escalation owner).

**Who can read it**
- `#live-incidents` members: Arthur, Brian, Calvin, Douglas, Julia, Leonard, Oliver, Owen, Robert, Samuel, Vincent.
- Helpshift and Crashlytics mail: Arthur and Leonard.
- The LiveOps engine deck: Leonard only. Board decks: the four founders.

**Contradictions, stale facts and lookalikes**
- Auto-deploy: Arthur's Confluence comment and his Slack message say quest auto-deploy "stays off", but the postmortem body says the 8-hour ingestor auto-deploy "was left running".
- Postmortem says resolved 18 Nov 17:44; Vincent reports quests broken again on 19 Nov.
- Root cause: `page_live_ops_engine` blames "a deploy that leaves the job unscheduled on every node". `page_liveops_calendar` blames a generator date bug (block ends six days before it starts) and dates a "weekend scheduler outage from 15 May".
- Arthur's comment "nobody knew until revenue told us" conflicts with the page itself ("do not measure from revenue") and with Slack, where Leonard found the problem by playing.
- The warehouse looks healthy where Slack says otherwise:
  - 29 Jun rows `EVT-0324`/`EVT-0325` are `completed`;
  - `EVT-0592` (Win & Collect, 27 Oct) is `completed`;
  - every November Weekly Leaderboards row (`EVT-0608`, `-0625`, `-0640`, `-0656`) is `completed`, yet on 30 Nov players reported tournaments not restarting for weeks.
- The yaml claim "compensation tool never built" is undercut by `liveops-dashboard-buddy` (Aug 2025) and backend `#79` (admin endpoints merged 2025-12-03).
- `page_support_playbook` insists the lives bug is not the scheduler stall.

**Volume.** 1,223 channel messages plus DMs; about 370 Helpshift threads; about 900 Crashlytics emails across Arthur and Douglas; 827 event rows; 1,600 review rows; 40K error rows.

**Gaps to fill by injection.** A GCal incident review or postmortem meeting; a Drive filing folder readable by the persona; optionally a Slides incident summary. Linear deliberately has no ticket for the July outage ("No standalone ticket was cut").

**Persona and competency fits.** Arthur Blake: Engineering Ops (incident record before the wind-down) or Corporate Ops (support liabilities). Vincent Parker or Douglas: Engineering Ops.

---

## 2. Quest system lifecycle (Feb 2024 – Nov 2025)

**Summary.**
- Kickoff 29 Feb 2024; backend by Douglas and Felix Young (ENG-636, Done 2024-05-06) in the `liveops` repo, with client UI by Samuel.
- The design Google Sheet was pushed to production by an ingestor every 8 hours. That is what broke on 15 Nov 2024 (ENG-1892).
- Dec 2024: 4-day/FTUE quests (`#4day-quests`, `GameOfDominoes#1575`, `#1608`).
- 2025: Zombie Match 3D Quests & Achievements (ZOM-63, `match3d#259`, `#270`).
- Oct 2025: Zombie Lite quests left In Progress (ZOM-640, ZOM-641, ZOM-663).

This overlaps storyline 1 on ENG-1892. Use one angle or the other in a task, not both.

**Anchors by service**
- **Slack:**
  - `C076Q0Z5R47` `#quests`: 294 messages, archived, 2024-06..2025-04, top thread 1733847735.562949.
  - `C079WK8SNLR` `#quests-dev`: 227 messages.
  - `C0861UQTUN9` `#4day-quests`: 339 messages, private (Arthur, Douglas, Leonard, Oliver).
  - 3,374 quest-matching messages across 213 conversations, including `#god-bugs` (292), `#game-design` (170) and DMs `D07GMT8NVM2` (Oliver–Vincent, 164) and `D07GY332589` (Oliver–Douglas, 129).
- **Gmail:** 253 quest threads. `oliver@harmonygames.co_1815819291614578291.json` (ENG-1892); `oliver@harmonygames.co_1838351498527073854.json` (ZOM-410); `00005207.json` (Robert, "Document shared with you: QUEST"); kickoff invites in Douglas's mailbox (`douglas@harmonygames.co_1792261476674359497.json`).
- **GCal:** "Feature Kick-off with backend team: Quests" 2024-02-29 (`evt_152075d8f6c2d4b04384aa` Arthur, `evt_de473692b7c0e2057fce25` Douglas, plus 4 more); "Quest UI/UX Kickoff" 2024-03-01 (`evt_71acad3ba3e723ef8cc243` Martin); "Quest discussion" `evt_13bd0ea123a8b42afd82b9` and `evt_abe1cd340e3b6845d6673b` (Douglas).
- **Linear:** 149 quest-titled issues (123 Done, 15 Canceled, 4 Bugs, 2 In Progress). Includes ENG-636, ENG-821, ENG-868 (Canceled, "New quests for google spreadsheets"), ENG-1892, ENG-2112, ZOM-63, ZOM-410, ZOM-534, ZOM-640/641/663, ENG-2415 (state PR).
- **GitHub:** 77 PRs (GameOfDominoes 63, liveops 11, match3d 3), 94 reviews. Key ones: `liveops#1`, `#2`, `#8`, `#10` (open), `#13`, `#19`; `GameOfDominoes#1306`, `#1530`, `#1575`, `#1608`, `#1633` ("pushing updated quests to server"), `#1907`.
- **Trello** (17 cards): `65eb5026cd4ce4d6c42d7bfd` "(Douglas) Quests Backend"; `65e0f20d8eb1dd290b1d4593` "Add remaining quests to the spreadsheet"; `6733fe99e4e4801523cbd9d8` "Claim Ads ticket under quests"; `6851a724601a61857a1b202f`; `68c452a03006277f55d9dc96`.
- **Confluence:** `page_quest_postmortem` plus 9 other pages that mention quests.
- **Snowflake:** LIVE_EVENT_PERFORMANCE Weekly Quests, 71 Domino Delights runs (`EVT-0003` 2024-10-07 to 2026-02-09); `DESIGN_EVENTS` quest_reward_granted (DD 200, ZM 58).
- **Sheets:** "Quest System - Backend tasks" `f_988792dd670ec016bd9d71` (Douglas; tabs Tasks, Data Structures); "Zombie Match Data Dictionary Firebase" `f_12b4105f4b64c3ad374a9f` (quest_completion and quest_reward_redeem tabs, 18 personas can read); "ZM FTUE QUESTS" `f_c47290833d85ea15f1b71b` (Leonard, Robert); "OLD DO NOT USE Zombie Quests" `f_b890200635ff26cac065c3` (Julia; shared with Robert and Frederick); "Loc files" `f_b82d4d41386fe0a90da5bd` (shared with 12).
- **Docs:** "QUEST" `f_e9f89125d725ef7f402526` (Samuel; Martin, Robert, Leonard can read); "quests are unlocked at level 4 instead of 19" `f_2c0872cba2ddb3147507f1` (Leonard); "[Zombie Ops] Quests And Achievements" `f_8638fd463260c152a748ff` (17 can read, but only 59 characters long).
- **Slides:** "Quest UI" `f_63d0846aefee8d435d6f5d` and "FTUE Quest UI" `f_f6fae38b0fd5885e2fb6d8`. Neither is readable by any persona.
- **Contacts:** Felix Young `/contacts/138` (not a persona); Douglas `/contacts/137`.

**Access boundary.** The live design sheet "Quests" `f_cd68edb7d1efb48a6c7698` (in `Resource:/Design/Domino Delights/GDDs/Live-ops`), "Domino Delights Quests v1.0" `f_b3a1d0ee5cdd870fb35cac` and "FTUE Quests v1.0" `f_8aa20846be3fb849aba609` cannot be read by any persona. The alternative routes are Slack and Confluence.

**Contradictions and lookalikes**
- Same auto-deploy and recurrence conflicts as storyline 1.
- ENG-1892 is labelled a client bug in Linear but is the root-cause ticket in Confluence.
- The warehouse flags only one week as `failed` against a 73h53m outage.
- Sheet lookalikes: "Quests", "Copy of Quests - June 12" (`f_4db4bf23837bbd813e0b8c`), "Zombie lite Quests" (`f_6c84144d87180a28a0172b`), "[Zombie Ops] Quests", "OLD DO NOT USE Zombie Quests", "ZM FTUE QUESTS".
- "Loc files" against "Copy of Loc files" (`f_bd9be34bfd655b3f935972`): Quest Translations has 13,021 against 12,351 non-empty cells.

**Volume.** 149 tickets, 77 PRs, about 3.4K Slack messages, 253 Gmail threads, 15 calendar events.

**Gaps.** Readable Slides (share or inject); calendar events for the 2025 Zombie Match 3D quest work; Zombie Match 3D quest runs in Snowflake (only DD Weekly Quests exist).

**Persona and competency fits.** Douglas or Oliver: Engineering Ops or Product Management. Samuel Turner (Design): Product Management.

---

## 3. Season Pass (Jan 2025 – Feb 2026)

**Summary.**
- Domino Delights version first: spec in Feb 2025; Oliver estimated "5-7 weeks"; backend PRs in March; `GameOfDominoes#1755` merged 2025-03-29 with 313 files.
- Rebuilt for Zombie Match 3D in `match3d#438`: 259 files, +235,311 lines, merged 2025-09-15 with 73 CodeRabbit comments and **no human review**.
- Launch bugs followed (ZOM-571, ZOM-575, ZOM-577).
- The Zombie Match 3D spec prices the pass at $6.99, yet the warehouse records $0 across six seasons.

**Anchors by service**
- **Slack:** `C08BVMXHGD6` `#season-pass` (336 messages, private, Feb 95 / Mar 229; estimate at 1739396216.689109; top thread 1739984339.845999); `CD657C29B728` "FC:…Season Pass Issues" (52, Mar 2025); `CA2DFEA73CBC` "FC:…Season Pass Issues - ZM" (188, Sep 2025; 1757687309.296399 "activation… IAP comes afterwards"); `#zombie-bugs` 1758031982.956109 ("After purchasing premium pass, lives are reset to 8").
- **Gmail:** `oliver@harmonygames.co_1823672790177377393.json` (ENG-2136), `..._1844899489385039707.json` (ZOM-575), `..._1845339997728453934.json` (ZOM-577); `brian@harmonygames.co_1845388579571608679.json` (ZOM-552); `marcus@harmonygames.co_1824465152019670119.json` (ENG-2163, sent to the `marcus@` lookalike mailbox).
- **Linear** (21): DES-299 (Canceled), ART-767, ENG-2136, ENG-2163, ENG-2219–2221, ENG-2230, ENG-2246 (Canceled), ENG-2319, ZOM-552, ZOM-571, ZOM-575, ZOM-577, ENG-2428 (Validation).
- **GitHub** (22): `game-of-dominoes-backend#10`, `#11`, `#17` ("every 2h in DEV"), `#33` ("last second of month for PROD"); `GameOfDominoes#1755`, `#1760`, `#1823`, `#1824`; `match3d#438`.
- **Trello:** `65eb55497eac80d87326c811`, `6851ab766fcaf894d0c0048b`.
- **Confluence:** `page_season_pass_spec` (Robert, v2 2026-02-12: "$6.99… No Season Pass purchase has been recorded"); `page_live_ops_engine` (monthly cron `0 0 1 * *`); `page_zm3d_gdd` comments.
- **Snowflake:** LIVE_EVENT_PERFORMANCE has 6 Zombie Match 3D Season Pass rows (`EVT-0527`, `EVT-0536`, `EVT-0604`, `EVT-0673`, `EVT-0742`, `EVT-0807`; 754 participants; $0) and no Domino Delights Season Pass rows. `IAP_TRANSACTIONS` has no Season Pass SKU; Zombie Match 3D has a single $1.99 bundle.
- **Sheets:** "ZM Season Pass Backend" `f_c0518ab5dacb03dcc8a144` (Oliver); "Zombie Match Economy 1.0" `f_89aebb6083dc44501666c7` (Brian; Season Pass Free and Premium tabs); "Zombie Match Data Dictionary Firebase" (SeasonPass_left, _premium, _redeem tabs); "Missing Translation Texts" `f_9545ad78b698abe99fbdd0` (Samuel).
- **Docs:** "DD Global Launch Readiness" `f_c57724584820a26f3bbe54` (P0: "Instead of Season Pass show the $0.99 Starter Pack"); "Domino Delights Revamp" `f_f0b89407ecae337699a434` (7 can read: "Season Pass premium is super weak"); "Economy Changes for Domino Delights" `f_948768f5a462e7037d17c9` (remove the "8 lives instead of 5" test).
- **Slides:** BoD Apr 16 2025 `f_868157b0665dcb6c16153a` ("Three Major Features Shipped… Season Pass"); BoD Jul 16 2025 `f_7793bb93e59e9c0dee5129`; March 25 Investor Update `f_418f5adef3a62a0e55c427`.
- **GCal:** only `evt_f384a2c35fd43e65b0f0d9` "Season Pass - WIP check" (Martin's calendar).
- **Contacts:** `/contacts/2` Marcus (Backend Engineer, `marcus@`) against Marcus Bennett `/contacts/157`.

**Who can read it.** `#season-pass`: Arthur, Brian, Calvin, Douglas, Julia, Leonard, Marcus Bennett, Martin, Oliver, Robert, Victor, Vincent. The Zombie Match 3D issues channel: Brian, Douglas, Marcus Bennett, Oliver, Vincent.

**Contradictions and lookalikes**
- The board deck says "shipped" while launch-readiness pulled it from the out-of-moves screen and the revamp doc calls it weak.
- The spec says $6.99 and that premium raises lives from 5 to 8, but there are no purchases; Vincent's test purchase comment conflicts with that.
- There is no Domino Delights Season Pass row in the event table.
- Sheet lookalikes: "Domino Delights Game Economy v2.0" `f_42484f82f5ee0afe3a6704`, five "Copy of … v2.0 - Octobe(N)" copies, "(April 9, 9_39 P" `f_df7cce499833f4ef11f907`, and "Domino Delights Game Economy + Leaderboard Liveops" `f_1ec982eb12afa160af0ae6`. None can be read by a persona.

**Volume.** 693 matching Slack messages in 90 conversations; 22 PRs (match3d#438 alone has 259 files and 73 comments); 21 tickets.

**Gaps.** GCal (kickoff or launch review); Contacts is minimal.

**Persona and competency fits.** Oliver Brooks: Engineering Ops or Finance (revenue reconciliation). Brian Foster: Product Management.

---

## 4. Leaderboards and leagues (Aug 2024 – Nov 2025)

**Summary.**
- Designed Aug 2024; the client was built by EMPLOYEE_0032 (`GameOfDominoes#1557`, 1,045 files, merged 2024-12-19).
- ENG-1874 was marked Done 2024-12-23, but on 30 Dec the backend broke under load; Douglas added a cache layer ("a single lambda is not able to do the job").
- League bots were added in 2025; Zombie Match 3D leaderboards followed (ZOM-36).
- By Nov 2025 players reported "tournaments haven't restarted for weeks".

**Anchors by service**
- **Slack:** `C07F4G84XV4` `#leaderboards` (588 messages, 553 in Dec 2024, private). Key messages: 1735601005.546249 and 1735607748.101459 (cache "once a day during weekend"), 1735601524.031689 "Still nothing"; top thread 1733240935.786989 (43 replies). Also `C084DFBD99S` `#google-apple-sign-in` (394) and DM `D08F3K705EY` (Douglas, 133).
- **Gmail:** `douglas@harmonygames.co_1819240246856540322.json` (ENG-1874 Done), `douglas@harmonygames.co_1822424695199276209.json` (ENG-2067), `douglas@harmonygames.co_1818901930396104648.json` ("Leaderboard Tiers" shared), invites `00006073.json` and `00006116.json` (Robert).
- **GCal:** Leaderboard Sync 2024-08-01 (`evt_7129c66224a3e14c6556a3` Brian); Leaderboard UI Sync (`evt_96f28223129cd0007ac071`); Kickoff with Douglas 2024-11-12 (`evt_7838bee1f588e07dfcdc71`); Zombie Match 3D Leaderboards Kickoff 2025-04-21 (`evt_2840725deb001fa23c2463` Douglas, `evt_bc52cf7439a15ca76dc26c` Oliver).
- **Linear** (43): ENG-1149, ENG-1211, ENG-1213, ENG-1874, ENG-2027, ENG-2067, ENG-2072, ENG-2111 (Todo), ENG-2325 (Todo), ZOM-36, ZOM-353, ZOM-429 (Backlog), ENG-2384 (Todo), ENG-2414 (PR).
- **GitHub** (23): `GameOfDominoes#1557`, `#1587`, `#1604`, `#1655`; `game-of-dominoes-backend#44`, `#45`; `match3d-backend#4`, `#16`; `liveops-dashboard-buddy#2`.
- **Trello:** `65eb52197c068ed1c9673e58`, `66c380ee170e56e69d55410d`, `67c5f034f804836b839e5478`.
- **Confluence:** `page_live_ops_engine`, `page_api_reference`, `page_backend_services`, `page_nakama_setup`, `page_arch_overview`, `page_liveops_calendar`.
- **Snowflake:** Weekly Leaderboards, 59 Domino Delights runs from `EVT-0052` (2024-12-30), all November 2025 rows `completed`. There are no Zombie Match 3D leaderboard rows; Plague Race reuses the leaderboard tables per `match3d-backend#4`.
- **Sheets:** "Leaderboard Tiers" `f_b35114ffa7db7ee42118b2` (Leonard; shared with Vincent and Douglas); `f_23dc18d9d6ca57fe86fadd` and "ZM3 - Event and League Bots" `f_d224d9f6fcd6045faeee22` (Vincent).
- **Docs:** "Leaderboard API" `f_14699d293c02f63b3ba31d` and "Leaderboards API" `f_3c540b22bb8a42e672c7a4` (Oliver). "Domino Delights Leaderboards" `f_978a2ca70aa2d770311899` cannot be read by any persona.
- **Slides:** board-deck body claims only.

**Who can read it.** `#leaderboards`: Arthur, Brian, Douglas, Frederick, Julia, Leonard, Martin, Robert, Victor, Vincent. Oliver is not a member.

**Contradictions and lookalikes.** ENG-1874 is Done before the 30 Dec breakage. The warehouse says healthy where Slack on 30 Nov says otherwise. Lookalike docs: "Leaderboard API" against "Leaderboards API"; DD against ZM3 bot sheets.

**Volume.** 1,623 matching Slack messages in 153 conversations; 43 tickets; 23 PRs; 19 calendar events.

**Gaps.** Slides.

**Persona and competency fits.** Douglas or Vincent Parker: Engineering Ops.

---

## 5. Domino Delights economy v2 (Mar – Dec 2025)

**Summary.**
- Apr 2025: first-time level coin rewards cut by 34.4% (480 → 315; p99 daily earn about 25k → about 8.5k), with IAP payouts retuned (commit `ceb6021fb`, 2025-04-09).
- Dec 2025: a "net negative" change replacing lives with tickets (doc dated 2 Dec, bug canvas dated 9 Dec). PR `GameOfDominoes#1914` "Economy changes" is still **open and never merged**.

**Anchors by service**
- **Slack:** `C08HHAA4ZUK` `#dd_economy_v2` (72 messages, private; members Arthur, Brian, Calvin, Douglas, Leonard, Oliver, Owen, Samuel, Vincent; threads 1741811424.287809 and others); `C4208B207A1A` FC EconomyChanges Bugs (14 messages, 2025-12-09; Brian); `#difficulty-optimization` 1743298845.097839 ("New Econ is pretty tight").
- **Gmail:** `blake@harmonygames.co_1850377838409276491.json` ("Economy Changes" doc shared); `blake@harmonygames.co_1850420779223185132.json` ("DD Economy Change" invite).
- **GCal:** "DD Economy Change" 2025-12-02 (`evt_38b4bb8e9fb17676cf3d4e` Arthur, `evt_4e40170fc69d397244961c` Owen, `evt_d53d9d35da5236e6f244e8` Leonard).
- **GitHub:** commits `ceb6021fb3` "Adjusting IAP payouts", `46fa30aff1` "Add season pass back in to IAP payouts", `2e3bae667e` (chapter reward cut); `GameOfDominoes#1914` (open).
- **Confluence:** `page_economy_design` (Julia, v1 2025-03-05 pre-cut → v3; comments c1 and c2, 2025-04-22/23).
- **Snowflake:**
  - `VIRTUAL_CURRENCY_LEDGER` (1,483,075 rows): economy_version `base` until 2025-03, `v2` from 2025-04. Domino Delights: base 144,402 rows, v2 1,078,723 rows.
  - `RAW_EVENTS` experiment `exp_econ_v2` on Domino Delights: control 887 against cut34 963.
  - Also `RESOURCE_FLOW_EVENTS` and `IAP_TRANSACTIONS`.
- **Docs:** `f_948768f5a462e7037d17c9` (Leonard; shared with Arthur, Brian, Owen); `f_f0b89407ecae337699a434` Revamp.
- **Sheets:** `f_89aebb6083dc44501666c7` (Brian); "Domino Delights KPIs" `f_e3014bb00f64fcf2f0162d` (Leonard; shared with Robert, Arthur, Brian, Julia). The v2.0 workbook and its copies cannot be read by any persona.
- **Trello:** 7 cards (Harmony Games and DD Product Roadmap boards).

**Contradictions**
- Confluence says the cut "shipped", but RAW_EVENTS shows an A/B split between control and cut34.
- Confluence says the pre-cut curve is "recoverable from commit `1ee438b6a6`", **but that commit does not exist in GitHub**.
- The Dec 2025 changes have a design doc and a QA bug canvas, but the PR is open and unmerged.
- Domino Delights launch date: KPIs sheet "April 14, 2025", INSTALL_EVENTS "2025-04-11", Launch Readiness doc "April 23".

**Volume.** 1.48M ledger rows (needs aggregation by day and version); about 314 economy-matching Slack messages.

**Gaps.** Linear (only 6 economy-titled issues in 2025 and none for the Dec change); Slides.

**Persona and competency fits.** Brian Foster or Owen Baker: Finance or Product Management. Arthur Blake: Finance.

---

## 6. Difficulty optimisation (Mar – Oct 2025)

**Summary.**
- Bayesian and random-forest pity tuning (ENG-2215, 2216, 2217) gave way to bot-simulation auto-tuning (`GameOfDominoes#1757` "Bot balancing", 2,843 files, merged 2025-04-01; `#1781`).
- Levels were swapped manually afterwards.
- Zombie Match 3D then added dynamic-difficulty tiers (ZOM-42 through ZOM-622; `match3d#137`, `#265`, `#395`, `#485`).

**Anchors by service**
- **Slack:** `C08GLSV8Z7W` `#difficulty-optimization` (501 messages, 481 in Mar 2025, private; members Arthur, Brian, Julia, Leonard, Vincent). Key messages: 1743106070.563009 ("1/3 swap, 2/3rd keep"), 1743100682.116089 ("7-10 swaps per chapter"), 1743176680.216499 ("around 27% on 900 levels"), 1743447673.825789 (Brian, swap count "decreased considerably"). Also `#zombie-match3d` (125 difficulty messages) and DM `D04UGG61DUM`.
- **Gmail:** "Dynamic Difficulty" invites (`blake@harmonygames.co_1814920906070237464.json`); `brian@harmonygames.co_1802226966613240594.json` ("Bot… for Difficulty Adjustment").
- **GCal:** `evt_30fe6164a175da028df3cb` (Walkthrough Kickoff 2024-03-19); `evt_5738b99d9ea6ea4939e178` and `evt_58abff2348ff6f8b3653cc` (2024-06-24); `evt_0cad74da2d483179a469cf` (2024-11-05).
- **Linear:** ENG-2185, ENG-2215–2217, ENG-2270, ZOM-42, ZOM-199, ZOM-293 (Todo), ZOM-576, ZOM-622 (In Validation).
- **Trello:** `65eb5071ba556eea86878543`, `67085f5e76ddf9d44e4e8c77`, `680fc0206579cbfbad65fab1`, `68c457c45f9e302837332bf4`.
- **Confluence:** `page_economy_design`, `page_domino_gdd`, `page_zm3d_gdd` (comment on tray 7 → 6).
- **Snowflake:** `LEVEL_PERFORMANCE` (4,755 Domino Delights levels, all created 2023-11, so a stale snapshot); `PROGRESSION_EVENTS` (87,101 rows with a result for each attempt; Domino Delights win share Jan 2025 977/1,573 against May 9,778/15,049); `DESIGN_EVENTS`.
- **Sheets:** "Parameter Optimization" `f_34f0950581934de1278969` (Leonard; shared with Vincent, Arthur, Brian, Julia); "Chapter Win Rates" `f_0adb6b404bdde7b5288a3a` (Arthur); `f_dc20acf354e9f0fde2b319` (Leonard).
- **Docs:** "Dynamic Difficulty" `f_0df8ef4443c9fd001c2ad7` (Leonard); `f_489cea072df5428d9decb7` (Robert).

**Contradictions.** The swap ratio is stated as 1/3, 27% and "7–10 per chapter" within two days. The level count is "900 levels" here against 1,200 in the puzzle pipeline. The LEVEL_PERFORMANCE snapshot is stale.

**Gaps.** Slides; no Gmail in the 2025 window (the invites are from 2023–24).

**Persona and competency fits.** Julia Lawson: Product Management. Brian Foster or Vincent Parker: Analysis.

---

## 7. Collect & Win (Jul 2024 – Nov 2025)

**Summary.**
- Domino Delights event designed in DES-237 (Brian); ENG-1385 Done 2024-10-03, while the first warehouse run (`EVT-0001`) is dated 2024-10-02.
- Zombie Match 3D rebuild: `match3d#468` (127 files, 37 CodeRabbit comments) plus `#470`, `#472`, `#477`, `#482`, Sep 2025.
- Magical Wings UI optimisation: ENG-2424, still in state PR.

**Anchors by service**
- **Slack:** `C07DBSKKKJQ` `#winandcollect` (206 messages; Owen is not a member); `C09EVVCFHKR` `#zm-collect-win` (107; 1758038131.083579, 1758721617.772589); `C3DD99314033` FC C&W issues (81).
- **Gmail:** `brian@harmonygames.co_1805038815688748898.json` (kickoff invite); `owen@harmonygames.co_1848593940754018682.json` and `brian@harmonygames.co_1848741122600714857.json` (ENG-2424); `samuel@harmonygames.co_1816905837376025073.json` (ENG-1834).
- **GCal:** Win & Collect Kick Off 2024-07-22 on 10 calendars (`evt_5e2a031a3f8f0b53f3706a` Brian, `evt_5041fef8bfbe1598193e14` Douglas); Onboarding `evt_0c783751a2633cf5de665e`; Rewards `evt_6ece3442cea182b6c6ce96`.
- **Linear** (24): ENG-1834, ENG-2021, ENG-2298, ENG-2331 (Regression), ENG-2349 (Bugs), ZOM-566 (In Validation), ZOM-579, ENG-2402 (Bugs), ENG-2424.
- **Trello:** `6644fb2675ff166176503a1a`, `6851a7abf7876721472dba99`, `686fcb6369c0fdc0b925a0ea`.
- **Snowflake:** Win & Collect has 213 Domino Delights runs and **no Zombie Match 3D rows**.
- **Docs:** "[live-ops] ZM collect&Win" `f_7989a718d6be1e4428b143` (Brian); "Collect & Win Endpoints" `f_5cd94d57a7e6669f89e238` (Owen). The Magical Wings docs (`f_63bf1bd3ac55cbec23967a` and the -comm copy) cannot be read by any persona.
- **Sheets:** `f_89aebb6083dc44501666c7` (Collect&Win Day 2 and Day 3 tabs); Data Dictionary Collect&Win tabs.
- **Confluence:** `page_live_ops_engine`, `page_liveops_calendar`.

**Gaps.** Slides; Zombie Match 3D rows in Snowflake; 2025 calendar events.

**Persona and competency fit.** Brian Foster: Product Management.

---

## 8. Domino Delights web port (Oct 2025 – Feb 2026)

**Summary.**
- Telegram master ticket ENG-2377: 3 of 13 sub-tickets shipped on day one.
- WebGL sub-250 MB sprint (Nov 2025): `GameOfDominoes#1891` "WebGL Fixes" (321 files, 26 review comments) plus UI optimisation PRs `#1885`–`#1908`.
- The size metric keeps changing:
  - "initial 163MB / full 506MB" (1762045268.676029);
  - "301MB -> 255MB" (`#executives` 1763092243.257119);
  - "Total download size is 276mb" (1763341093.990849);
  - a "330mb update on top of 384mb install" on 10 Dec (`C9CA62B5180A` 1765332395.238069).

**Anchors by service**
- **Slack:** `C09KU8U4DPF` `#telegram-dd` (145); `C09Q4S613CN` `#dd-road-to-sub-250mb` (272; NPOT thread 1762446921.426029, 92 replies); `#builds` "Android Build Size" bot posts (hundreds, 217–295 MB); `C09SWTHEMEW` publishing partner channel (273 messages, 39 members).
- **Gmail:** 24–26-message partner thread (`00015818.json` Robert; `blake@harmonygames.co_1847444686529657894.json`); Telegram Kickoff invite `blake@harmonygames.co_1845628236025019758.json`; BoomBit kickoff `jlawson@harmonygames.co_1849661638563918741.json`.
- **GCal:** Telegram Kickoff 2025-10-13 (`evt_67bf7e4b598b8354659fa4` Arthur, `evt_a0e39000ba60ebbbc94ee4` Brian); BoomBit Kick Off `evt_f07c2d5d56f5110a888cef` (Julia).
- **Linear:** ENG-2377–2388; ENG-2401, 2403, 2404, 2405 families. Several are still in state PR or Validation even though their PRs merged: ENG-2417 → `#1901`, ENG-2418 → `#1902`, ENG-2419 → `#1903`, ENG-2425 → `#1895`, ENG-2426 → `#1908`.
- **Slides:** `f_61aa2afa731c82d726b330` (BoomBit pitch) and `f_7a6231aff4544d77ef5053` (CrazyGames pitch); readable by Leonard, Arthur, Robert.
- **Sheets:** "boombit_qa" `f_d766eaedb0c4d32dbb9666` (Leonard).
- **Docs:** `f_84dcc7c2b8e97e5c186a11` (Telegram terms, Leonard).

**Gaps.** Trello, Confluence and Snowflake have nothing (no web platform appears in INSTALL_EVENTS or DAU).

**Persona and competency fits.** Arthur Blake or Owen Baker: Engineering Ops. Arthur Blake: Marketing and GTM.

---

## Reserves

**A. Combo Fighter monetisation readiness** (a different angle from the calibration task) [normal-only — every record in Reserve A post-dates 2025-09-30 and does not exist on Oct 1]
- **Slack:** `C09UHHN6PFZ` (12,172 messages); `C0AA36TV9QA`.
- **GitHub:** Combo-Fighters, 37 PRs, including `#34` "IAP" merged 2026-01-27.
- **Gmail:** 14 "Review of your Combo Fighter (iOS) submission is complete" emails.
- **GCal:** Combo Fighter Kick off 2025-11-12, on 9 calendars (e.g. `evt_0c030e6eb00183a70d9267`).
- **Confluence:** `page_combo_gdd`.
- **Snowflake:** no Combo Fighter IAP sales; `PUSH_NOTIFICATION_STATS` has 7 Combo Fighter rows; `REVENUE_DAILY_V2` has 90.
- **Drive family:** Sheets `f_bf5cf7e68ca4f4e7854452` (push notifications, shared with 20) and `f_e782531004d48b81f91e97`; Docs `f_32cefb80cd45093c6e88dc` (Brian) and `f_8fb667cfb8d1e8dcc7a182`; Slides `f_dc2bcf2055ba55b750e60b` "SHOP COMBO FIGHTER".
- **Gaps:** Linear and Trello have zero records and need injection.

**B. Ad monetisation**
- **Slack:** `C07KZG57QKD` (514 messages, 428 in Nov 2024); `C07K74CLNJD` (493).
- **Linear:** ENG-1876, ENG-1951, ENG-1961, ENG-2292.
- **GitHub:** `GameOfDominoes#1483`, `#1494` ("3 lives instead of 5" in the ad-removal bundle; the Dec 2025 economy doc later removes "+3 lives"), `#1503`, `#1605`, `#1794`.
- **Trello:** `680287617cf86bf6f358fb54`.
- **Snowflake:** `AD_REVENUE` (77,373 rows); `AD_IMPRESSION_EVENTS` (53,370).
- **Sheets:** `f_a60df48a9fbe5e96e7ec64`, `f_3d27b871b46848df89e65e` (Vincent).

---

## Notes that apply across storylines
- **Shared trap.** The board decks are readable only by the four founders. Domino Delights designs live in a Resource-owned "Design/Domino Delights/GDDs/Live-ops" folder that no persona can open.
- **Name lookalikes:** `marcus@` (`/contacts/2`) against Marcus Bennett. Contacts also lists roles that differ from the roster: Leonard "Co-founder & CEO" (`/contacts/170`), Robert "Co-founder & Chief Product Officer" (`/contacts/108`).
- **Calendar is the most common gap.** Engineering personas have few topic events (Oliver 0 across most storylines). Plan a GCal injection for most of these tasks.


---

# Part B — Business, finance, legal and wind-down

### 10-line summary
1. **Rank 1, Orderly wind-down, Feb 9–13 2026.** [normal-only] Fully natural in 12 services; adding vendor records to Contacts makes 13. Core sources are #winddown `C0ADGSZKR3R` (206 msgs), the Sherwood Partners "wind-down support request" email thread (9 msgs), the Drive "Wind Down" folder, the Task List sheet, a Sunset fee row in Snowflake, 275 open Linear issues and 16 GitHub repos that were never archived.
2. **Rank 2, October 2025 layoffs and final contractor terminations.** Natural in all 13 services. The core is a three-way payroll reconciliation: `PAYROLL_ROSTER`/`FINANCE_LEDGER`, Carta "Termination details" emails, and termination letters.
3. **Rank 3, UA (user acquisition) spend and attribution reconciliation for 2025.** 12 natural; GCal events in 2025 need to be added. Volume comes from 2,590 daily spend rows, 93 Meta receipt threads from two ad accounts, and the Adjoe billing dispute.
4. **Rank 4, Publisher and web-distribution canvass, Oct 2025–Feb 2026** (CrazyGames, BoomBit, about 10 other publishers, Telegram). 12 natural. It is the only arc a non-founder (Julia Lawson or Brian Foster) can carry.
5. **Rank 5, Vendor liability and SaaS termination register** (Helpshift, Singular, Unity and the "HG Costs" tab). 10–11 natural.
6. **Rank 6, Bridge round to recapitalisation to board cadence, Jul 2025–Jan 2026.** 11 natural; Linear and GitHub would need injected records.
7. **Rank 7, Mattel Barbie "Dream Life Glow".** [after 2025-09-30: normal-only] Only 7–8 natural, so it needs about 5 injections.
8. **Data disagrees with itself in useful ways.** Snowflake cash and the P&L sheets differ by about $37K a month in late 2025, and the storyline yamls' cash figures are wrong. Helpshift's balance is quoted three ways ($1,500 / $1,200 / $300) and Sunset's fee as $11.7K, $13–15K and ~$15K. A Feb 11 letter says "effective January 31, 2025", which is a typo [normal-only].
9. **Tim Steudler cannot carry any of these** without heavy injection: no Slack membership, no Gmail mailbox, no Drive files owned or shared, 0 Linear issues, 0 Trello activity, and 1 calendar event. **Thomas is also weak**: his mailbox ends 2025-04-25 and he has no calendar events after Sep 2025.
10. **Check access first.** Drive files owned by a "Resource:…" account with empty sharing lists (the Wind Down folder, P&L Jun/Jul/Sep-2025, the Bridge Round sheet) may be readable by no persona; confirm from the persona's view before relying on them.

---

### Method and access notes
- **Access rules** (from `Evals/references/persona/acl.md`): Gmail, Slack, GCal, Drive, Docs, Sheets and Slides are filtered to the persona. Contacts, GitHub, Trello, Linear, Snowflake and Confluence are visible to everyone.
- **Slack user IDs.** Leonard `EMPLOYEE_0038_SLACK_ID`, Robert `…0016…`, Arthur `…0025…`, Frederick `…0008…`, Julia `…0005…`, Brian `…0026…`, Thomas `…0018…`, Tim `UBF5AB53C96`.
- **The storyline yamls are not ground truth.** The fundraising yaml's beat e01 says cash was $450K in Mar-25, $230K in Jun-25 and $195K in Sep-25. Snowflake `CASH_BALANCE` says $669,997, $365,165 and $157,538.
- **Snowflake row counts verified.** `FINANCE.EXPENSES`: `CASH_BALANCE` 34, `MONTHLY_BURN` 239, `HEADCOUNT` 371, `PAYROLL_ROSTER` 371, `FINANCE_LEDGER` 704 (89 rows since 2025-09). `ANALYTICS`: `AD_SPEND_DAILY` / `AD_SPEND` / `UA_SPEND_UNIFIED_V2` 2,590 each, `DAILY_ACTIVE_USERS` 1,682, `REVENUE_DAILY` 2,284.
- **Sensitive content.** #winddown contains a pasted Figma OAuth client ID and secret (ts `1770858495.115779`). No rubric should depend on that text.

| Rank | Storyline | Natural services | Coupling | Volume | Best personas |
|---|---|---|---|---|---|
| 1 | Feb-2026 orderly wind-down [normal-only] | 12 (+Contacts) | very high | high | Leonard, Arthur, Robert |
| 2 | Oct-2025 layoffs → Feb-2026 terminations [normal-only] | 13 | very high | high (payroll ledger) | Arthur, Leonard, Robert |
| 3 | 2025 UA spend & attribution reconciliation | 12 (+GCal 2025) | high | very high | Leonard, Robert (Frederick, with a caveat) |
| 4 | Publisher / web distribution canvass [normal-only] | 12 (+Contacts) | high | high | Julia, Brian, Leonard |
| 5 | Vendor liability & SaaS termination register [after 2025-09-30: normal-only] | 10–11 | high | medium-high | Leonard, Arthur |
| 6 | Bridge → recap → board cadence [after 2025-09-30: normal-only] | 11 | medium-high | high | Leonard, Robert, Arthur |
| 7 | Mattel Barbie pitch [after 2025-09-30: normal-only] | 7–8 | medium | medium | Julia, Leonard |

---

## 1. Orderly wind-down of Harmony Games Inc. (Dec 2025 prelude, decided Feb 9, executed Feb 9–13 2026) [normal-only]

> Everything in this section is normal-only: the wind-down does not exist in the Oct 1, 2025 (synth-cut) universe.

**(1) Summary.**
- **Lead-up.** On Dec 3 2025 Leonard quoted a ChatGPT estimate that shutdown would cost $30–50K. On Dec 18 he said December would be the last salaries. On Jan 12 he reported "$25K in the bank". The Jan 23 recapitalisation email to Griffin offered two paths: a cap-table reset or shutdown.
- **Decision.** Shutdown was decided Feb 9 after Combo Fighter's data came in.
- **Execution.**
  - **Vendors.** Helpshift, Singular and Unity were sent termination or release-of-claims emails. Soundly, Layer, CodeRabbit, Cursor and Zapier were cancelled. Deel, Gusto and Intuit were kept. GitHub and Metabase were moved to Arthur's LLC card.
  - **Wind-down provider.** Sherwood Partners (assignment-for-benefit-of-creditors firm) and Sunset (wind-down service) were both consulted. **Decided Feb 12:** Leonard reports the wind-down and data agreements "reviewed and signed" (`#winddown` `1770931777.561519`; the counterparty is a redacted username token, context points to Sunset) and hands Arthur the "data stuff" (`1770935695.500189`). A design that has Sherwood as the provider contradicts the base.
  - **Data sale.** Company data was sold to AI labs: a $22,500 cash offer against Sunset's $11,700 fee.
  - **People and accounts.** Contractor termination letters went out Feb 11. Google accounts are to be archived after Feb 15. GitHub repo ownership is to move to Arthur's LLC.
  - **Board and paperwork.** A board resignation was accepted and Carta records terminated.

**(2) Anchors by service.**
- **Slack.**
  - #winddown `C0ADGSZKR3R`: 206 msgs, all Feb 9–12 2026, members Leonard, Robert, Arthur. Key timestamps:
    - `1770663250.160009` posts the "Shut_Down_List" canvas `F0ADY9EET50`. The canvas has **no content** in the export.
    - `1770664094.831769` is the board-call email draft.
    - `1770664700.848759` is the investor announcement draft.
    - `1770673276.567499` attaches the Helpshift Order Form PDF `F0ADZED6L58`.
    - `1770673717.808759` is the Helpshift termination email.
    - `1770674268.840059` is the Singular termination email.
    - `1770911000.728559` gives the data offer ($22.5K) and Sunset fee ($11.7K).
    - `1770932147.282819` is the Unity termination note.
    - `1770933601.686309` and `1770933903.645709` are the keep/cancel list and action items ("archive account on google after Feb 15").
  - #executives `C07C2866011`: 7,647 msgs from Sep 2025 to Feb 2026. Key timestamps: `1768248003.017699` (cash $25K, card debt $6K, payroll $17K), `1770765511.243329` (Singular $18,750; Unity "~2.348*9 months"; Helpshift "$150*8 months"), `1770850852.708789` (Sunset "~$15K").
  - #admin_foundersonly `C04UEQVDVB7`: `1770765910.100299` ("Helpshift… $300 total"), `1770766119.978069`, `1768333863.145119` (Singular draft).
  - #company-internal `C05KNDCHAAG`: `1770839984.194409` (accounts archived by Feb 15), `1770841441.489819` (Oliver Brooks asks about git), `1770842137.835489` (Arthur: transfer repos to his LLC).
- **Gmail.**
  - "wind-down support request" with Sherwood (`PERSON_0728`): `leonard@harmonygames.co_1856688113228112603.json` (9 msgs, Feb 9–11). Copies: Robert `00016832.json`, Arthur `blake@harmonygames.co_1856689465050769375.json`.
  - Sherwood's acceptance: `leonard@harmonygames.co_1856801727690974853.json`.
  - "Singular – Past Due Invoices": `blake@harmonygames.co_1853470745439394465.json` (5 msgs, Jan 5–Feb 12; $6,250 overdue; extension to Mar 15).
  - "recap option, cap table reset" with Griffin's `PERSON_4337`: `leonard@harmonygames.co_1855133803855213163.json`.
  - Feb 11 termination letters: Robert copies `00016873`–`00016878.json`, Leonard copy `leonard@harmonygames.co_1856860994291529096.json`.
  - SVB (the bank) notifications: 162 unique threads since Apr 2025.
- **GCal.** `evt_9a8faed31d5ef3d9b2dcab` "Options with Investors" (2026-01-08). `evt_8cdcb12b7b4e1346db999d` board meeting (2026-01-14). `evt_212e50fb5a53ea8016ce29` Wind Down call with Sunset (2026-02-11 22:30Z). `evt_4ebbd76539b6304ad37a74` wind down call with Sherwood (2026-02-12 16:30Z). All on the Leonard, Robert and Arthur calendars.
- **Drive.** Folder `d_e5caf6a8c630421942ee59` "Wind Down", containing `f_105b20100113e6d6cccbf6` Termination Notices, `f_191742fdb229bf19737dd3` Employee Termination Letters and `f_31115ddb6ed866f2b10d60` Task List. Linked from Slack: folder `1XQAild72BAz_A-Wo-bvTBX7oZjygP53H`.
- **Docs.**
  - `f_0c37bb7235683d73569903` "Harmony Games Wind Down – 2026_02_11 Notes by Gemini" (7,675 chars). Sunset quotes $13–15K, the process takes 4–6 weeks, the board is "themselves and Griffin", and the notes misname the entity as "Robert Incorporated".
  - `f_105b…` and `f_191742…` are **stubs** (15 chars, `<REDACTED_FILE>`).
  - `f_11040fe5d66821bd6951aa` Reset Financing Term Sheet: $2.25M pre-money, 40:1 washout of existing preferred.
  - `f_f09041fe1e83ead96b3d09` Reset Financing Framework.
- **Sheets.** `f_31115ddb6ed866f2b10d60` Task List (11 tasks, all `False`, no owners or deadlines). `f_605121f4a36752645e0ac3` "P&L and forecast – Jan 2026", tabs HG P&L, HG Salary & Benefits, HG Costs, Reduced…, Detailed Reclassification.
- **Slides.** `f_65ada5e24989d256cabdfa` "Harmony Games BoD Jan 14 2026" (15 pp).
- **Snowflake.**
  - `FINANCE.EXPENSES.FINANCE_LEDGER`: `FIN-000702` (2026-02-12, "Sunset (wind-down)", −11,700), `FIN-000686`–`FIN-000704`.
  - `CASH_BALANCE` 2026-01-31: $8,096, runway 0.5 months, headcount 4.
  - `MONTHLY_BURN` 2026-02: legal $12,480, accrued but never closed.
  - `HEADCOUNT` tail: 7 in Dec-25, 4 in Jan-26.
- **GitHub.** 16 repos, `archived:false` on all. `Combo-Fighters#37` was merged 2026-02-13 by `EMPLOYEE_0003` (Oliver Brooks), after the announcement. A CodeRabbit comment `Combo-Fighters#37#c_1` (Feb 12 06:31Z) predates the CodeRabbit cancellation at 22:50Z.
- **Linear.** 275 open issues (ZOM 129, ENG 115, ART 18, EPI 9, DES 4). The last issue was created 2025-11-07. January cancellations include ZOM-400/427/439/441 and ART-790. Slack says "linear we keep during transition".
- **Confluence.** `page_support_playbook` triages via the player ID Helpshift attaches, so it needs rewriting for email support. `page_aws_infra` gives a cost note of about $1,550/mo. `page_company_story` mentions "October 2025 cost reductions".
- **Trello.** Board `640643a3fd8f3ca308d9318e` "Harmony Games" is the founders' to-do board: open cards are 6 Backlog, 1 Recruiting, 170 Done (recounted Oct 4); last activity 2025-11-12, so stale. Example card: `680ee5d709c2d601148c25ff` "Paperwork for the Board".
- **Contacts.** No vendor, Sherwood or Sunset contacts. `/contacts/160` is Matthew Collins, "Independent Director".

**(3) Who can read it.**
- **Leonard** can read everything.
- **Robert and Arthur** can read everything except Leonard-private items: the Gemini notes `f_0c37…`, the reset term sheet `f_1104…` and the Helpshift invoices, which are in Leonard's mailbox only. Their workaround is #winddown `1770911000.728559` plus the Gmail copies in their own mailboxes.
- **No non-founder** is a member of #winddown, #admin_foundersonly or #executives (except Frederick, who was terminated Oct 24 [normal-only]).

**(4) Contradictions and distractors.**
- **Cash.** January figures: $25K cash / $6K card debt (Jan 12) versus $25K / $8K card debt (Jan 23). Snowflake: Dec-25 $25,031 and Jan-26 $8,096. The Jan-2026 P&L sheet shows Dec ending $52,686 but Jan beginning $29,636, so it breaks internally.
- **Helpshift balance.** $150 × 10 = $1,500 (#winddown `1770673467.186629`), $150 × 8 (#executives) and "$300 total" (#admin_foundersonly).
- **Sunset fee.** $13–15K (Gemini notes), ~$15K (#executives), $11,700 (Slack and `FIN-000702`).
- **Data value.** "$25K" (Feb 10) versus a $22,500 cash offer (Feb 12).
- **Slack message volume.** "300,000" (Gemini notes) versus "220K in 365 days / 660K total" (#winddown) versus about 586K in the universe brief.
- **AWS cost.** "DD production ~$1k/mo" (Slack) versus Confluence ~$1,550 versus ledger AWS $1,485 versus the P&L "Servers (AWS)" line at 0.
- **"Shut down" vs still working.** Combo Fighter PRs were still merged after the shutdown announcement [normal-only].
- **Lookalike entity.** "Robert Incorporated" in the Gemini notes.

**(5) Volume.** #executives Dec–Feb: 2,959 msgs. Leonard's mailbox has 2,315 threads active since Oct 2025. 275 open Linear issues. 16 repos. 89 ledger rows since Sep 2025. Roughly 25 SaaS lines in HG Costs.

**(6) Injection gaps.**
- **Contacts:** Sherwood `PERSON_0728`, Sunset, Helpshift, Singular billing `SVC_0019`/`SVC_0028`, Unity.
- **Placeholders to fill or keep as traps:** the empty Termination Notices doc and the empty Shut_Down_List canvas could be given content.
- **Optional:** a Confluence "wind-down runbook" page.

**(7) Fit.** Leonard or Arthur for **Corporate Ops**: a creditor and vendor close-out plan, account archiving, a GitHub ownership-transfer runbook, and a Linear backlog disposition. Robert for **Finance**: a liabilities register reconciled to Snowflake.

---

## 2. Downsizing and offboarding: salary freeze → Oct 24 2025 layoffs → Dec "last salaries" → Feb 11 2026 terminations [after 2025-09-30: normal-only]

> The May 2025 salary freeze exists on Oct 1; the Oct 24 2025 layoffs and everything after them do not.

**(1) Summary.** Executive salaries were frozen (board consent, May 2025). In October one contractor was terminated for moonlighting. The marketing department was eliminated: Frederick Stone received an "involuntary termination" notice effective Oct 24. Terminations were processed in Carta (equity), Deel (international contractors) and Gusto (US payroll). The remaining contractors were terminated by letter on Feb 11 2026.

**(2) Anchors by service.**
- **Snowflake.**
  - `PAYROLL_ROSTER` (371 rows, 22 people). End months 2025-10-31 for Felix, Victor Barnes, Josh Dempsey (`EMPLOYEE_0032`), Frederick Stone and Artist 5 [normal-only].
  - `HEADCOUNT` comment: one engineer was terminated 2025-10-20 for dual employment and is not identified.
  - `FINANCE_LEDGER` salaries (~470 rows): Oct-25 still pays Frederick in full (`FIN-000651`, −3,089.81).
  - `CASH_BALANCE` headcount column.
- **Gmail.**
  - Carta emails (sender `SVC_0077` = Carta) titled "Termination details for…" [normal-only]:
    - `leonard@harmonygames.co_1847333347700620793.json`: Calvin Price, terminated as of Oct 24 2025, grant ES-3 of 8,138 shares with 4,408 vested, last day to exercise Jan 24 2026.
    - Siblings `…1847333272519888206`, `…1847333318158821452`, `…1847333395311994879`.
  - "Notice of Involuntary Termination" to Frederick: Robert copy `00015796.json` (Oct 29). The Feb 11 version is `leonard@harmonygames.co_1856858053929740799.json` [normal-only].
  - "Notice of Termination of Consulting Agreement" (breach of the competitors clause): `00015795.json`.
  - Lauren Brooks termination: `leonard@harmonygames.co_1853596374263642118.json` (Jan 6) [normal-only].
  - Six "Termination of Independent Contractor Agreement" letters, Feb 11 [normal-only].
  - Gusto: 66 threads since Apr 2025, mostly Arthur's.
- **Slack.**
  - #admin_foundersonly Oct-2025 (564 msgs): `1760994356.272729` ("let him go"), `1761168059.583569` ("dual gig… since June"), `1761702344.371469` (terminations in Carta), `1761844344.664939` (Deel terminations as of 10/24), `1761924828.820549` (Deel account misassociated).
  - #company-internal: "has left the channel" events Feb 11.
- **Drive.** Folder `d_2af93116d8dc22dba2323e` "Employees-Contractors": `f_b5cac6b6428ae5268e9d46` Board Consent Salary Freeze (2025-05-01), `f_ce0c4b43b26e5a3505249f` Board Consent Option Grants Q4 2024, an equity-calculator subfolder.
- **Docs.** Consulting agreements `f_20a0df3860bb5731d22f07` (Lauren Brooks), `f_093699b840b863c38ef12d`, `f_5f1c9697dd9eff50e12ebc`.
- **Sheets.** `f_28ecc492b19f3696a19a97` P&L Oct 2025 has salary-scenario tabs "Reduced", "Revo of", "Rollic of" and "Barebone of" HG Salary & Benefits. Also `f_605121f4…`.
- **Slides.** `f_d03044b385b94f24b21ff4` BoD Oct 14 2025 (20 pp); `f_7793bb93e59e9c0dee5129` BoD Jul 16 2025 (downsizing options).
- **GCal.** Two separate "All Hands" events on Oct 24: `evt_0a0658fbb9bbebae7f962a` (16:00Z) and `evt_11530fad245bf030e8563b` (16:30Z). Board `evt_4ee450f276f468e9ce95cf` (Oct 14) and its Jan 14 counterpart, both including frederick.stone.
- **Linear.** On 2025-12-02, Marcus Bennett's ENG-2062, 2063, 2358, 2359 and 2360 were cancelled. ENG-2301 (Douglas) was cancelled 2025-12-16. Open issues remain assigned to departed people.
- **GitHub.** The last PR per departed engineer can be traced through `author_login`.
- **Confluence.** `page_product_okrs` (owner "Frederick Stone (Growth/UA, departed Oct 2025)"); `page_company_story`.
- **Trello.** Contract and Carta cards: `66a90e012143802a0c808a8d`, `663ea0dd8ab21d22e29a7adb`, `680bae9dcfce67522fa080c0`.
- **Contacts.** Frederick `/contacts/139` is "Commercial Lead, Marketing & BD", not "Co-founder".

**(3) Who can read it.** Leonard fully. Arthur and Robert can read Slack, the Gmail termination letters (cc'd), Drive and Sheets, but the Carta "Termination details" emails sit in Leonard's mailbox only; their workaround is #admin_foundersonly `1761702344.371469`.

**(4) Contradictions and distractors.**
- **Calvin Price.** Carta says terminated Oct 24 with 4,408 vested shares, but `PAYROLL_ROSTER` shows him as a contractor for a single month (2025-04) [normal-only].
- **Moonlighting date.** `HEADCOUNT` says 2025-10-20; the consulting-agreement notice says effective Oct 24 [normal-only].
- **Frederick Stone's role.** The persona roster calls him "Co-founder"; the roster table has `is_founder=False` with a start of 2024-09; he was terminated Oct 24 yet is invited to the Jan 14 2026 board meeting [normal-only].
- **Josh Dempsey.** `EMPLOYEE_0032` is "Josh Dempsey, product" in the ledger, while the persona brief says `EMPLOYEE_0032` is a Senior Unity Engineer.
- **Julia Lawson.** `full_time` in the roster, but she receives Deel payouts and a "Validate your US tax forms" email.
- **Date typo.** One Feb 11 letter says "effective January 31, 2025" [normal-only].
- **Lookalike events.** Two "All Hands" events on the same day.

**(5) Volume.** 371 + 371 + 704 Snowflake rows. 25+ termination emails. 564 founder-channel messages in October. Five P&L scenario tabs.

**(6) Injection gaps.** None required. Optionally add Linear offboarding issues.

**(7) Fit.** Arthur Blake for **Corporate Ops** or **Finance**: reconcile final pay, equity and access per person, and produce an offboarding certification. Leonard also fits.

---

## 3. 2025 UA spend and attribution reconciliation (Domino Delights incent test Apr–Jun → ZM3D → Combo Fighter Meta, Dec–Feb) [after 2025-09-30: normal-only]

> The Apr–Jun 2025 incent test and the 2025 spend rows exist on Oct 1; the Combo Fighter Meta campaigns (Dec 2025 – Feb 2026) and their figures do not.

**(1) Summary.** In April–June 2025 Domino Delights ran an incentivised UA test, mainly on Adjoe. AppLovin underperformed. In Sep 2025 Adjoe switched a campaign back on without approval, and an invoice was sent anyway. A Unity→Singular cost connector reported $0. Singular went past due. Combo Fighter ran Meta campaigns from Dec 2025 to Feb 2026, and in Jan 2026 the CPI was claimed to be "~$5" [normal-only].

**(2) Anchors by service.**
- **Snowflake.**
  - `ANALYTICS.MARKETING.AD_SPEND_DAILY` (2,590 rows). Domino Delights Apr–Jul 2025: Adjoe $46,202 / 8,730 installs; AppLovin $6,086; Meta $1,005; total $53,305. Combo Fighter CPI: Dec $5.26, Jan $7.02 ($2,843.84 / 405 installs), Feb $12.75 [normal-only].
  - `AD_SPEND` and `UA_SPEND_UNIFIED_V2` (2,590 each); `INSTALL_ATTRIBUTION`; `DIM_PLAYER` channel mix; `FINANCE_LEDGER` `marketing_ua` (34 rows, no Unity Ads rows).
- **Gmail.**
  - Meta ad receipts: 93 threads in Leonard's mailbox (62 unique since Apr 2025) from two ad accounts, `[IDENTIFIER_5351]` and `[IDENTIFIER_3125]`. Examples: `leonard@harmonygames.co_1856612239565121370.json`, `…1856974663738001623.json`.
  - Google payments: 38 threads. AppLovin payment reminders: 17. Tipalti: 10.
  - Singular "Legacy Creative Reporting sunset": `frederick@harmonygames.co_1846237478582699658.json`, `simon@harmonygames.co_1847424846461394559.json`.
- **Slack.**
  - adjoe-[ORG] `C07UCC631A6` (360): `1757345931.336429`, `1757348929.625759`, `1759326759.229719` (invoice sent; credit promised).
  - applovin_[ORG] `C1C2137664A3` (698).
  - [ORG]-playablex `C08H78VJG80` (207).
  - node-[ORG]-external `C08MCEP1B9B` (846, Sep 2024–Apr 2025).
  - zombie_marketing `C06DJBJL798`.
  - publishing-ext `1764022591.269199` ("$50K on Adjoe… ~10K installs").
- **Drive.** `f_b871c0351b5bba5c2e3cba` "Mixing and Matching Adjoe with Applovin.xlsx"; folder `d_229337c774f2c7741cc042` AppLovin end-card assets.
- **Sheets.** `f_e3014bb00f64fcf2f0162d` Domino Delights KPIs (Marketing and Monetization tab, 36 rows; anyone-visible); `f_759fa5719181112c9b8d1a` "INSTALL COMP BY DIFFERENT DATA SOURCES".
- **Docs.** `f_af99b76ff4da59a710edba` Board Meeting Jul 25 ("$50K in UA spend"); `f_27a041fdb116695b01c566` Video Production Plan.
- **Slides.** `f_7793bb93e59e9c0dee5129` BoD Jul 16 2025.
- **Linear.** ENG-2361 (Adjoe ad frequency, completed 2025-10-27), ENG-2362 (Singular deep links, open), ZOM-467, ZOM-618, ART-790.
- **GitHub.** `GameOfDominoes#1860` (Singular links), `match3d#269`, `Combo-Fighters#24` (AppLovin MAX integration, merged 2026-01-13) [normal-only].
- **Confluence.** `page_product_okrs` (Unity→Singular connector reported $0, so blended CPI is "not measurable"); `page_analytics_dashboards`.
- **Trello.** UA/BD board `66da196af476ab78deaa0cef` (40 cards; "ZM 3d Technical Launch / Alpha" list has 16); `688c4d14c312a27fa2747e40` "Playable Kickoff" (backlog).
- **GCal.** Only 2024 UA syncs exist: `evt_8818fda620c38d2b81ef07`, `evt_1625cc9aeded5e62f4a97c`.
- **Contacts.** Internal UA managers only: Marcus Lee, George Miller, Megan Wilson, Victoria Lane.

**(3) Who can read it.** Leonard fully. Robert can read the applovin and adjoe channels and his own receipt copies. Frederick has strong access (vendor channels and 22 receipt copies), but was terminated Oct 24, which makes him an awkward choice of persona [normal-only].

**(4) Contradictions and distractors.**
- **CPI.** "CPI ~$5" (Jan 23 email) versus Snowflake January $7.02.
- **Adjoe totals.** "$50K Adjoe / 10K installs" (Slack) versus Snowflake $46,202 / 8,730.
- **Adjoe September dispute.** Unresolved: the invoice was sent and a credit was promised but never shown.
- **Meta, three sources.** February receipts total about $1,257 versus Snowflake/ledger $956.45 [normal-only].
- **AppLovin soft launch.** The marketing yaml has an AU/NZ/CA soft launch in 2024, but Snowflake has no AppLovin spend before 2025-04.

**(5) Volume.** 2,590 × 3 spend rows, 93 receipt threads, and channel histories of 360–846 messages.

**(6) Injection gaps.** GCal UA meetings in 2025, and vendor representative contacts.

**(7) Fit.** Leonard or Robert for **Marketing and GTM** or **Finance**: a channel-by-month spend reconciliation with an install-quality verdict.

---

## 4. Publisher and web-distribution canvass (Oct 2025–Feb 2026) [normal-only]

> Everything in this section is normal-only: the publisher canvass and web-distribution partnership do not exist in the Oct 1, 2025 (synth-cut) universe.

**(1) Summary.**
- **The canvass.** Eleven 29-page publisher pitch decks went out.
- **CrazyGames.** A web (HTML5) licence was signed around Dec 3–5. It required the build to come down toward 250MB.
- **BoomBit.** Mobile publishing via a shared Slack Connect channel. The Brazil creative test in January performed poorly.
- **UDO.** Rejected the games over CPI and retention.
- **Telegram mini-app.** Abandoned.
- **Status at the clock date.** The web launch never happened.

**(2) Anchors by service.**
- **Slack.**
  - publishing-ext-[ORG]-nbp7547 `C09SWTHEMEW` (273 msgs, Nov 2025–Feb 2026; BoomBit is external): `1769509283.414179` (Brazil test, conversion rates 1–2%), `1766005025.730949`.
  - dd-road-to-sub-250mb `C09Q4S613CN` (272): `1762361357.317589` (CrazyGames "exclusive launch period"), `1763310035.244339`.
  - telegram-dd `C09KU8U4DPF` (145).
  - [ORG]-udo `C09QKR2AR3J` (35): `1762253698.354819`.
  - mpdm `C1CB3D58E38B` (Leonard, Julia, Brian): `1760952652.853559` (publisher list).
  - #admin_foundersonly `1764907519.899639` (CrazyGames contract).
- **Gmail.**
  - CrazyGames, as `PERSON_5536`: `leonard@harmonygames.co_1847443396264475348.json` (26 msgs, Oct 30–Feb 11); Robert copy `00015818.json` (24).
  - Kwalee: `00015824.json` (7). Supercent: `leonard@harmonygames.co_1847274510773446727.json`. Publishing partnership on Domino Delights: `leonard@harmonygames.co_1844790807629452298.json` (7).
- **Slides.** Eleven near-identical decks: Crazygames `f_7a6231aff4544d77ef5053`, Boombit `f_61aa2afa731c82d726b330`, Kwalee `f_c63a862b231542649aaa90`, TapNation `f_8526e1d449593e82573670`, UDO `f_e524bfa36de1e7328d73e8`, Saygames `f_10b4ef1f122bcb73c8da9b`, Supercent `f_4713509878a6bdfcdf4df0`, HOMA `f_303de1c512a43dbd892efa`, Habby `f_2630810d5acf5cfb40b8c1`, Voodoo `f_6323065c3722c684158ac9` / `f_fccfc83b9a9b4139584272`, Template `f_0c94ef7a98241ef75ee589`.
- **Drive.** `d_1b3fe29da397e6f9df3d46` BoomBit_Harmony Games (Julia's), `f_d766eaedb0c4d32dbb9666` boombit_qa.xlsx.
- **Sheets.** boombit_qa (140 rows; Leonard-private); Domino Delights KPIs `f_e3014bb00f64fcf2f0162d`.
- **Docs.** `f_c2f5642b483949523656cc` Domino Delights × SayGames plan, `f_6d70fe46d8114d3d283b5b` Supercent, `f_951773cefaed013a6e51a3` NDA, `f_f0b89407ecae337699a434` Domino Delights Revamp, `f_84dcc7c2b8e97e5c186a11` Telegram terms.
- **GCal.** `evt_3d23fd10f04d1e251dfc9a` (UDO), `evt_2707803fb7bbde5d1a7703` (SayGames), `evt_b7de08f20b26983c580070` (Voodoo), `evt_f07c2d5d56f5110a888cef` (BoomBit kickoff, Julia), `evt_0c059c06fd743fa2cdc912` (Telegram kickoff).
- **Linear.** ENG-2403 "Core Game UI Optimization" (15 children), ENG-2377 to ENG-2388 (Telegram), ENG-2408.
- **GitHub.** `GameOfDominoes#1891` (WebGL fixes), `#1911`, `#1912`.
- **Snowflake.** Domino Delights `DAILY_ACTIVE_USERS`, `USER_COHORT_RETENTION`, `REVENUE_DAILY` (Domino Delights about $183 in Jan-26).
- **Partial sources.** Trello `65eb4ec525346c8070ca638f` (Domino Delights roadmap, stale since 2025-10-10). Confluence `page_domino_gdd`.

**(3) Who can read it.**
- **Julia** can read publishing-ext, udo, dd-road, telegram-dd and mattel; the BoomBit folder; the anyone-visible decks; and the GCal kickoffs. She **cannot** read the CrazyGames Gmail thread or boombit_qa; her workaround is dd-road `1762361357.317589` and Slack.
- **Brian** has similar Slack access.
- **Leonard** can read everything.

**(4) Contradictions and distractors.**
- **Exclusivity.** "Exclusive launch period" (dd-road, Nov 5) versus the signed non-exclusive licence.
- **Lookalike decks.** Eleven decks of 29 pages each.
- **Adjoe totals.** "$50K Adjoe" versus Snowflake, again.
- **Integration status.** Unresolved: the CrazyGames contact followed up twice with no reply.

**(5) Volume.** About 1,000 Slack messages across the channels, 26 + 24 + 7 + 7 email messages, 11 decks of 29 pages, and 15 + 12 Linear issues.

**(6) Injection gaps.** Contacts for the CrazyGames and BoomBit representatives, and a current Trello pipeline card.

**(7) Fit.** Julia Lawson or Brian Foster for **Marketing and GTM** or **Product Management**, for example a publisher-pipeline status and go/no-go memo.

---

## 5. Vendor liability and SaaS termination register (Helpshift, Singular, Unity, SaaS tools; Nov 2024–Feb 2026)

This overlaps rank 1; it is the vendor slice extended back to 2024.

**(1) Summary.** Helpshift was adopted in Nov 2024 (Order Form, $150/mo). Singular was billed quarterly at $6,250 and went past due. Unity Pro cost $1,200/mo. At the wind-down the team decided, vendor by vendor, whether to cancel, keep or move to a personal card.

**(2) Anchors by service.**
- **Sheets.** "HG Costs" tab of `f_605121f4a36752645e0ac3`. Monthly values (Sep–Dec 2025):
  - Unity License: 2,172 then 1,200, 1,200, 1,200.
  - Helpshift: 150.
  - A redacted line `[PERSON_NAME_0499]`: 6,250 in Oct only, which matches Singular's quarterly amount.
  - Metabase 138, dbt 122, BigQuery 26, Quickbooks 115, G-Suite 298, Slack 125, Gusto 128, Deel 250.
  - Linear, Figma and Trello at 0.
- **Gmail.** Helpshift invoices: 13 threads, all in Leonard's mailbox; for example INV/HSUS8673 `leonard@harmonygames.co_1844993512903865424.json` (2025-10-03). Also the Singular past-due thread `blake@harmonygames.co_1853470745439394465.json` and 18 Unity threads.
- **Slack.** The #winddown items listed under rank 1.
- **GitHub.** `GameOfDominoes#1452` and `#1505` (Helpshift), `match3d#275` (unmerged) and `#277`.
- **Linear.** ZOM-301 and ZOM-302.
- **Trello.** `67f435f0724b219caec281d7` "Pay up Helpshift for INV/HSUS6215"; `66e0b305808021874932a923` "pay Singular".
- **GCal.** `evt_12f117ae13fc18ca6592a4` "Harmony Games x Helpshift" (2024-11-20).
- **Confluence.** `page_support_playbook`, `page_aws_infra`.
- **Snowflake.** `FINANCE_LEDGER` `software_tools` (35 rows; Jun-25 −1,566 down to Jan/Feb-26 −786) and `cloud_infra` AWS.

**(3) Who can read it.** Leonard fully (the invoices are his alone). Arthur can read the Singular, Unity and SVB copies.

**(4) Contradictions and distractors.**
- **Vendor-list total vs ledger.** HG Costs totals about $2,918/mo on the line items, versus the ledger's `software_tools` at $786–1,566. The sheet's own "Total Spend" for Nov/Dec is $2,042.
- **Unity.** "~2.348 × 9 months" versus 1,200/mo in the sheet.
- **Helpshift.** The three-way balance mismatch from rank 1.
- **Redacted Singular line.** The sheet shows Singular only as `[PERSON_NAME_0499]`.
- **Leap-year error.** The Helpshift yaml says "migrate by Feb 29, 2026", a date that does not exist; Slack says Feb 28.

**(5) Volume.** About 70 HG Costs rows, 13 + 18 + 9 invoice threads, 35 ledger rows.

**(6) Injection gaps.** Slides (a vendor slide), Contacts, and content for the Termination Notices doc stub.

**(7) Fit.** Leonard or Arthur for **Finance** or **Corporate Ops**.

---

## 6. Bridge round → recapitalisation → board cadence (Jul 2025–Jan 2026)

**(1) Summary.** The July board meeting reported about $365K in the bank and 5 months of runway. The $2.5M bridge outreach started Sep 3. Rejections followed from A16Z Speedrun, 1AM, a Turkish fund and Initial Capital. In January 2026 a cap-table reset / pay-to-play recapitalisation was proposed to Griffin, and on Jan 22 the founders discussed a board seat for $125K.

**(2) Anchors by service.**
- **Slack.**
  - #bridge-pitch `C096HFA5Z8W` (596 msgs; 420 in Sep 2025): `1757345124.546449` (VC tracker).
  - #executives: `1756749288.785249` (outreach template), `1759288987.503349` (A16Z rejection), `1761579083.902079` ("3 engineers only"), `1768265943.581399` to `1768266587.810349` (three drafts of the Jan 14 board email).
  - mpdm `C7442B7CD94B`.
- **Gmail.** Bridge outreach Sep 3: `leonard@harmonygames.co_1842219327413774622.json`, `…1842284545492364031.json`. General Catalyst: `…1845324849163852511.json`. DocSend pitch-deck view notifications: 25 threads. Griffin quarterly-metrics requests: 14, including Jan 27 and Feb 3 reminders. Board materials: `…1837676721477425972.json`.
- **Sheets.** `f_48247af79428823c3cac92` Game Investor List 25 (82 rows). `f_efaec72066ee44e5888bd7` Bridge Round (Angel Investors 27 rows, VCs 17 rows). Lookalike: `f_0b29566cd7932a205d54d2` Internal Game Investor List (2024).
- **Docs.** `f_17e6175e84e745f92b3415` Bridge Narrative, `f_af99b76ff4da59a710edba`, `f_2e3969eb7c39ae04b99e3f` Reachout Template, `f_26e1f9a86761e35049192a` Executives Biweekly Sync, `f_11040fe5d66821bd6951aa`.
- **Slides.** `f_7793bb93e59e9c0dee5129`, `f_0421912301531f11c54686` (Internal BoD Jul 16), `f_d03044b385b94f24b21ff4`, `f_65ada5e24989d256cabdfa`, `f_7e68dfdc57ea569d7688a1` (Pitch MASTER), `f_18b4a27fcb4316a33040ed`, `f_36adfec7ed33bea26dbf8b` (FAQ, 48 pp). Lookalike: `f_683f74d5c8c60954e95efe` "Abridged BoD – Internal".
- **GCal.** `evt_771fc850b4096bad7ea8b2` (Jul 16, includes Matthew Collins), `evt_4ee450f276f468e9ce95cf`, `evt_8cdcb12b7b4e1346db999d`, `evt_444867d86a25159b0a7dff` (pitch dry run).
- **Snowflake.** `CASH_BALANCE` and `MONTHLY_BURN`.
- **Trello.** `6682b910110b8b60a37cb6b9`, `67018c4c962c1f06fcaf8ace`, `67f446b4b0817af30d2d63f6` (Board Deck), `68c5a49e8491a9d7faf869d0` (Existing Investor Update).
- **Confluence.** `page_product_okrs`.
- **Contacts.** `/contacts/160`.

**(3) Who can read it.** Leonard, Robert and Arthur. Frederick can read the Bridge Narrative, the Investor List, the Jul and Oct decks and the Oct and Jan board invites.

**(4) Contradictions and distractors.**
- **Cash, Snowflake vs P&L sheets** (month-end):

  | Month-end | Snowflake | P&L sheet |
  |---|---|---|
  | Sep 2025 | $157,538 | $194,133 |
  | Oct 2025 | $99,701 | $137,855 |
  | Nov 2025 | $52,965 | $85,868 |

- **P&L versions disagree.** The Jun, Jul, Sep-30, Oct and Jan versions (`f_846ac…`, `f_a5e9…`, `f_dd0b…`, `f_28ec…`, `f_6051…`) project different months to $0.
- **Yaml cash figures** are wrong (see Method notes).
- **Board membership.** Matthew Collins attended in July; Frederick in Oct and Jan; the Feb 12 Slack mentions an accepted board resignation.
- **Board dates.** A board-meeting acceptance email exists for Sep 17, but the calendar meeting is Oct 14.
- **Recap terms.** A "$2M pre" plan in Slack versus the term sheet's $2.25M pre-money.

**(5) Volume.** High: 596 + 7,647 Slack messages, 82 + 44 sheet rows, 7+ decks.

**(6) Injection gaps.** Linear and GitHub (for example a data-room or demo-build ticket or a release tag) and investor contacts.

**(7) Fit.** Leonard or Robert for **Finance**: a runway reconciliation and board pre-read.

---

## 7. Mattel Barbie "Dream Life Glow" (Aug–Dec 2025) [after 2025-09-30: normal-only]

> The Aug–Sep 2025 speaker notes and the M3 request-for-proposal thread exist on Oct 1; the pitch itself and everything after 2025-09-30 are normal-only.

**Anchors.**
- **Gmail.** M3 request-for-proposal thread from Tim: `leonard@harmonygames.co_1842359642190933488.json` (14 msgs, Sep 4–Dec 2); Robert copy `00015226.json`. Pitch email: `jlawson@harmonygames.co_1850507818902089538.json`.
- **Slack.** #mattel_proposal `C09QDMC3UL9` (145 msgs; Julia, Claire, Robert, Martin, Leonard): `1762962922.325239`, `1765212709.815689`. #executives `1764711857.752419`.
- **Drive / Slides.** `f_10de61ca7886bb1e5f3fe1` and `f_e37f1de047a1b1e5156607`, plus their PDFs `f_d455f64310d1ed5adae1af` and `f_56368b32bfbef721459801` (all domain-visible).
- **Docs.** `f_1260d68b087f86840f709e` Speaker Notes Mattel (Leonard-private).
- **GCal.** `evt_048b618ca76c5c85c7b98f` (Tim, 2025-08-20), `evt_03c7e307f396f762ad4727` (dry run), `evt_2bb239ad901c0545ddc3b5` (huddle).
- **Contacts.** `/contacts/98` Tim.

**Gaps.** Linear, Trello, GitHub, Confluence and Snowflake have nothing natural, so this needs about 5 injections.

**Contradictions.** Tim appears as Mattel's licensing contact but has a harmonygames.co address. Speaker notes dated Aug 20 predate the pitch. The pitch was never resolved.

**Fit.** Julia or Leonard, **Marketing and GTM**.

---

### Can Tim Steudler or Thomas carry a task?
- **Tim: no, not without heavy injection.**
  - Slack: 0 channels, 0 messages authored.
  - Gmail: no mailbox in `users.json`. He appears only as a sender in other people's mailboxes.
  - Drive: 0 files owned or shared, though the 179 domain/anyone-visible files may be readable.
  - GCal: one event, `evt_048b618ca76c5c85c7b98f`. The persona brief says 5; 1 was measured.
  - Linear user `usr_bf5ab53c966f8ba7`: 0 issues. Trello: 0 cards, 0 actions. Contacts: `/contacts/98`.
  - A Mattel task from his view would need Slack membership in #mattel_proposal and a seeded mailbox.
- **Thomas: weak for this scope.**
  - Gmail runs 2024-05 to 2025-04-25 (2,318 threads). GCal has 197 events, none after Sep 2025.
  - He is in 42 Slack channels, but not #executives or #winddown, and he left #company-internal at `1770839906.134099`, one minute before the account-archive announcement [normal-only].
  - Linear: 17 issues (Plinko / Lucky Drop, 2024). Drive: 111 files shared with him.
  - The only plausible business task is a personal "save your data before Feb 15" offboarding inventory, and it is unclear whether he can still read the announcement after leaving the channel [normal-only].

### Lower-value arcs in scope (each 7 services or fewer)
Superplay/TYZ patent threat (Slack, Gmail, Drive); Solsten (Slack, Gmail, Trello, HG Costs); Node Media (Slack, Gmail, GCal 2024); advisor equity / Carta (fold into ranks 2 and 6).

