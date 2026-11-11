# Deep recheck P1: Unique Ground Truth and Clarity

Pass: P1 (blind, independent). Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Persona: Julia Lawson (julia.lawson@harmonygames.co).
Inputs read in full: 00_Task_Assigned_Inputs.md (platform block), 02_Universe_Date.txt, 04_Prompt.txt, 01_Universe_Inject.sql (243 lines, not executed; post-SQL values used).
Incorporated sources checked sentence by sentence: Frederick's DM ask and its thread follow-up (SQL l.11, l.13), the brief "ZM3D beta live-ops calendar - working rules" (SQL l.93), and the UA plan deck the brief cites (SQL l.113-128).

**Sentences checked: 43.** That is 6 in the prompt, 11 in Frederick's two DMs and 26 in the brief. I also checked the 9 text lines of the UA plan deck.

## Findings

`DR# | pass | checklist section | quote | record | dimension | proposed severity`

### DR1 | P1 | common_errors §2 "Which items are in the set" / Eval 1 §2.1 | quest rollover "still to do"

- **Quote:** Brief: "For each beat, what still has to land before it runs for bought users (prod deploy, config, player-facing art an owner has flagged) and who owns it." Also: "For the quest rollover, the daily gift (...) and Plague Race put down whether the beat is in and whether its push is ready, not its window dates."
- **Records:**
  - Trello action `68dac8204f1e9a3b7c2d5e61` (SQL l.237), commentCard by Leonard Hayes, 2025-09-29T17:55:44Z, on card #61 "Add more quests and balance quest rewards - (Leonard/Douglas)" (list "BETA: Sep 30"): "New quest set goes in with the Mon Oct 13 rollover, the current set carries the first week."
  - Base gsheets `f_a325dd4af80afc5994d5dc` "Push Notifications Zombie Match", tab "PNs Beta", Quests row: "Not Ready | Quests | Push Notification | Rollover | Revisit once new quests roll out. | ... | LIVE | New Quests Await! 🌟".
- **Dimension:** Unique Ground Truth (contents).
- **Reading A:** The quest row's still-to-do is "new quest set (config) lands for the Mon Oct 13 00:00 UTC rollover", owned by Leonard/Douglas.
- **Reading B:** The quest row has nothing still to do. The beat runs from Oct 6 on the current set ("the current set carries the first week"), and the new set is a scheduled refresh, not something that must land "before it runs".
- **What changes:** The Calendar-tab quest "Still to do (owner)" cell, and how the recommendation describes quests. A sub-fork on the owner is possible: the card title names "Leonard/Douglas" and Leonard wrote the comment.
- **Settler search:** No prompt sentence, brief sentence or record says whether content due partway through the span counts as "before it runs". The brief's quest sentence restricts only window dates.
- **Missing:** One brief or prompt sentence, or a Leonard/Douglas note, saying whether the Oct 13 set is required for the beta calendar.
- **Proposed severity:** Major. UGT fork, fail-level if any criterion grades the quest still-to-do one way. It clears only if the rubric accepts both readings, and both owners.

### DR2 | P1 | common_errors §2 "Which items are in the set" / Eval 1 §2.1 | ZOM-544 sign-in versus the brief's two still-to-do sentences

- **Quote:** Brief: "An established failure holds it; an unverified build or platform is a still-to-do, not a hold." Against that: "For each beat, what still has to land before it runs for bought users (prod deploy, config, player-facing art an owner has flagged) and who owns it."
- **Records:**
  - Linear comment `cmt_zom544_1` (SQL l.225), Vincent Parker, 2025-09-29T15:35:50Z: "Apple sign-in works from the settings menu on the auth branch, but progress does not restore yet: levels, currencies and cards are not synced. Google Play login is still waiting on the backend setup."
  - Base ZOM-544 "Implement Google Apple Login", In Progress, assignee EMPLOYEE_0032. Its description "What we need to store" lists "Season pass rewards and progression & and premium pass if any" and "Quest and achievement progression...".
- **Dimension:** Unique Ground Truth (contents).
- **Reading A:** ZOM-544 stays off the calendar. Sign-in is not a beat, and it is not a prod deploy, config or flagged art item.
- **Reading B:** The brief classes "an unverified build [auth branch] or platform [Google Play]" as a still-to-do. So ZOM-544 is a still-to-do, listed under Season Pass (premium and progress restore) and/or quests, owned by EMPLOYEE_0032.
- **What changes:** The Season Pass and quest still-to-do cells, and possibly the recommendation.
- **Settler search:** No record ties sign-in to a beat or says it is needed for the beta. This is the only persona-visible item I found that matches "unverified build or platform". The two brief sentences point opposite ways.
- **Missing:** A brief sentence or record that puts sign-in or progress restore in or out of the calendar.
- **Proposed severity:** Major. UGT fork, fail-level if a criterion grades ZOM-544 either way. Otherwise the rubric must stay neutral on it.

### DR3 | P1 | common_errors §2 "Which number, if two amounts or dates exist" / Eval 1 §2.1 both-fair | new date for the November Season Pass config

- **Quote:** Brief: "Every config a beat needs lands before its lock, read in server time (UTC). A committed date that misses the lock moves earlier and its owner is told in a reply on the mail where they committed to it."
- **Records:**
  - Julia's copy of Brian Foster's Sep 26 mail, thread `julia.lawson@harmonygames.co/1844311412966040123` (SQL l.65-72): "the November Season Pass config handoff moves from Wed Oct 29 to Fri Oct 31, 10:00 Istanbul time ... Treat Fri Oct 31 as the date I am committing to and drop the Oct 29 one ... If the new date is a problem on your side, reply on this mail."
  - Brian's Sep 22 mail, thread `julia.lawson@harmonygames.co/1843954828968533812` (SQL l.34-43): "The config handoff we agreed with Product is for Wed Oct 29".
  - Confluence `page_season_pass_spec` (current, v2 2025-09-30): "Season config (tiers, rewards, theme) is authored in the live-ops tool and locked 24h before each season opens" and "production seasons reset monthly on the 1st at 00:00 UTC".
- **Settled part:** The lock is Fri Oct 31 00:00 UTC. Brian's date is 07:00 UTC (Istanbul is UTC+3), so it misses the lock. Even at UTC+2 (08:00 UTC), or reading both instants in PT, it still misses. So the decision is fixed: move the date earlier and reply on the Sep 26 thread to Brian.
- **Dimension:** Unique Ground Truth, one figure (a date).
- **Reading A:** Move it to land by the lock, that is by Thu Oct 30 23:59 UTC or Fri Oct 31 00:00 UTC.
- **Reading B:** Move it back to Wed Oct 29, the date Brian first gave as agreed with Product.
- **What is the same:** The decision, the write (a reply on the Sep 26 thread), the destination and the recipient.
- **Five checks:**
  - Newer source: Brian's "drop the Oct 29 one" retires Oct 29 as his own commitment, but it does not set Julia's new date.
  - Authority: the brief says only "moves earlier".
  - Source identity, scope and same result: none of these ranks the two dates.
  - Both readings complete every ask, and neither changes the next action.
- **Proposed severity:** BOTH_FAIR_FIGURE, not a UGT fail. The rubric must accept any handoff date that lands before Fri Oct 31 00:00 UTC. It must not lock Oct 29 or Oct 30.

### DR4 | P1 | Eval 1 §2.6 Clarity / §2 edge values | "until when" for the held weekly leaderboard / leagues

- **Quote:** Frederick DM (SQL l.11): "...if anything is held and until when..." The sheet header (SQL l.132) is "Hold until (UTC)".
- **Records:**
  - Slack `b5f2955c2e154efc6835946ecfe1758e`, #zombie-match3d, Vincent, 2025-09-30T20:50:12Z (SQL l.19): "Re-tested the weekly leaderboard on the current prod build: it still does not start a new week. I killed the app and reopened it twice ... Same on the second device."
  - Base ZOM-429 is Backlog, assignee Douglas, with no due date.
  - Searches of Slack Sep 2025 ("new week|next session|ZOM-429|restart"), the GCal releases and the injected rows found no fix date or ETA. The Oct 8 release (`evt_5c1e83a7d94b02f6c8e31a`) covers only "The server windows that are still on the DEV stack".
- **Dimension:** Clarity (one content field with no record behind it).
- **Reading A:** No instant. The hold lasts "until ZOM-429 is fixed and re-verified on prod".
- **Reading B:** A concrete end. Either the whole span (Sun Nov 2 23:59 UTC, held all four weeks) or the first Mon 00:00 UTC reset after a fix.
- **What changes:** The "Hold until" cell and the recommendation's run/hold call. The hold decision, the ticket note and its destination are the same.
- **Missing:** A dated fix or ETA for ZOM-429.
- **Proposed severity:** Minor, Clarity NON-FAIL (3-4). The rubric must accept any explicit open-ended or whole-span end and must not require a specific instant.

### DR5 | P1 | Eval 1 §2.6 Clarity | Plague Race "whether its push is ready"

- **Quote:** Brief: "For the quest rollover, the daily gift (...) and Plague Race put down whether the beat is in and whether its push is ready, not its window dates." Then: "A push goes out only if its row is Ready and LIVE ... Anything else is held, with what is missing."
- **Record:** "PNs Beta" Plague Race row: "Ready | Event | Push Notification | Event Start (server time) | Plague Race | Everyone | Main Menu | WIP | Plague Race Is On! 🌊🚣".
- **Dimension:** Clarity.
- **Reading A:** The push is not ready. It is WIP, not LIVE, so it is held.
- **Reading B:** The push is "Ready", because the row's own Status column says Ready.
- **What changes:** The Calendar-tab Plague Race "Push" cell. The Pushes tab is held under both readings. The quest and Login Calendar rows read Not Ready either way, so only Plague Race differs.
- **Settler found:** The brief's push rule leans to Reading A. Lowercase "ready" in the quest/Plague Race sentence is not explicitly tied to it.
- **Proposed severity:** Minor, Clarity NON-FAIL. The main session may reject it with the quote "A push goes out only if its row is Ready and LIVE ... Anything else is held".

### DR6 | P1 | common_errors §2 "Which items are in the set" | leagues versus weekly leaderboard: one beat or two

- **Quote:** Brief: "Every ZM3D beat a player can see in those weeks: an event window, a reset or a start push. Not only the events everyone lists."
- **Records:**
  - GitHub review comment `harmonygames-Games/match3d#470#rc_10` (SQL l.138): "The Plague Race, leagues, Endless and Season Pass schedules are already running on prod."
  - Vincent, as quoted in DR4: "the weekly leaderboard ... does not start a new week".
  - "PNs Beta" row "Weekly Leaderboard reset".
  - Confluence `page_liveops_calendar` (v3 2025-09-29): table row "Weekly Leaderboards | Domino Delights / Zombie Match 3D | Recurring | Live", and the note "Zombie Match 3D overlaps Plague Race, Leagues and both Endless Monster resets".
  - #zombie-ops, Julia-visible, base `C08R6BF4ENN/2025-06.json#298`, 2025-06-18: "currently PROD schedules are: Weekly leagues: every monday at 00:00 AM UTC".
  - match3d-backend `lib/zombies_game/leagues.ex`: Leagues are Leaderboards records.
- **Dimension:** Unique Ground Truth / Clarity (set and contents).
- **Reading A:** One beat, the weekly leagues leaderboard (Mon 00:00 UTC). It is held, with a note on ZOM-429.
- **Reading B:** Two beats. "Leagues" runs W1-W4 (per Arthur), and a separate "Weekly Leaderboard" is held.
- **What changes:** Calendar rows and statuses. The ZOM-429 note is written under both readings.
- **Settler found:** The #zombie-ops naming, the Confluence overlap note and the code lean strongly to Reading A. No record says outright "the weekly leaderboard is the leagues".
- **Proposed severity:** Minor, Clarity NON-FAIL. It can likely be rejected with the #zombie-ops quote. The rubric must grade leagues and the weekly leaderboard as one held beat.

**Topic status:**
- UGT: two open forks (DR1, DR2) and one both-fair date (DR3).
- Clarity: three minor items (DR4-DR6) and no write-action divergence. The sheet, the ZOM-78 link, the conditional ZOM-429 note, the reply to Brian and the DM to Frederick each resolve to one action, so there is **no fail-level Clarity finding**.

## Open tickets, PR notes and Trello/Slack notes read as "still to do"

Each line gives the post-SQL state and whether a record settles it.

### Linear tickets

| Item | Disposition | Settled by |
|---|---|---|
| ZOM-429, Backlog, Douglas | Hold reason for the leaderboard/leagues; the note goes here. Douglas's Sep 16 note ("force-closes and reopens, they land in the new week fine") is superseded. | Settled by Vincent's later Sep 30 retest ("killed the app and reopened it twice") and the brief's "even after a restart". It is the only open leaderboard ticket (ZOM leaderboard/league/weekly list checked). |
| ZOM-556, Todo, Calvin | Not a hold, not a still-to-do. | `cmt_zom556_1`: "claiming works and nothing is lost", plus brief "Wrong counters ... do not hold". Settled. |
| ZOM-432 (SQL sets Done) | Excluded. | `cmt_zom432_2`: "in both submission builds from today, iOS 50 and Android 135, so nothing is left here", plus "Not what already shipped". Settled. |
| ZOM-534, In Progress, Douglas | Not a hold; the "edge case" is not a deploy, config or art item. | Brief "a reset that needs a restart ... do not hold". Settled. |
| ZOM-465, In Progress, Marcus | **Include:** C&W event icon animation, owner Marcus. | `cmt_zom465_2`: "The Collect & Win event icon animation is still to do on my side", plus "player-facing art an owner has flagged" and "not polish nobody flagged". Settled to include. The rubric must not treat it as excluded polish. |
| ZOM-526, In Progress (parent ZOM-521) | Excluded. | Brian `cmt_zom526_2`: "the event runs without it, so it does not have to land before the beta". Calvin's later `cmt_zom521_1` lists it as remaining but does not address beta need, so the scope check keeps Brian's answer. Settled. |
| ZOM-521, In Progress, Calvin | Excluded. | Tokens: as ZOM-526. "Claimed Cards traveling to inventory" is not a live-ops beat. Settled. |
| ZOM-543, In Progress, Calvin | Excluded. | `cmt_zom543_1`: "current flow is ... plus Collect and Win". Settled. |
| ZOM-552, ZOM-442, ZOM-549, ZOM-566 | Excluded. | Analytics, "not analytics". Settled. |
| ZOM-565 | Excluded. | "not needed for the beta". Settled. |
| ZOM-542 | Excluded. | "not needed for the beta". Settled. |
| ZOM-471 | Excluded. | "nothing here has to land for the beta". Settled. |
| ZOM-344 (SQL sets Done) | Excluded. | "Art side is signed off". Settled. |
| ZOM-504, ZOM-517, ZOM-546 | Not established failures; not still-to-dos. | Comments: not reproducible, visual only. Settled. |
| ZOM-544 | **Open fork (DR2).** | No settler found. |
| ZOM-78 | The calendar ticket (link destination). | `cmt_zom78_1`: "Let us use this ticket for the ZM3D beta live-ops calendar ... Link the sheet here". This beats ENG-2240 "Web interface for the liveops calendar". Settled. |
| ZOM-475 (base, Android glass crash) | Not a beat item. | Known data issue SC-8 (do not grade); outside the 21. |

### GitHub PR notes

| Item | Disposition | Settled by |
|---|---|---|
| PR #470 `rc_10` (Arthur) | C&W server windows reach prod at the Oct 8 release. Owner Douglas, who organizes `evt_5c1e83a7d94b02f6c8e31a`, Oct 8 15:00-16:00 UTC. | Settled. |
| PR #468 `rc_38` (Arthur) | Include: final vial models, owner Claire ("Claire has those on her list"). | Settled. |
| PR #473 `c_2` (Arthur) | Include: November premium strip range, owner Oliver. No committed date, so no lock reply is due. | Settled. |
| PR #477, open (Owen) | Excluded. It holds analytics plus info-screen and header text commits (`c7d3bc6f2e`, `9dc995cb39`). Its CodeRabbit review state is COMMENTED, not CHANGES_REQUESTED, and it is not deploy, config or flagged art. | Settled by "not analytics" and "analytics gaps do not hold". |
| Change-request reviews | Not applicable. GitHub has 0 CHANGES_REQUESTED reviews and 0 changes-requested timeline events on PRs created Aug-Sep 2025. The only nearby ones are outside that window: match3d#303 (Jul, later APPROVED) and match3d-backend#4 (Jun, Plague Race, merged). | Settled by "neither does a change request outside the Aug-Sep live-ops cohort". |

### Trello and Slack notes

| Item | Disposition | Settled by |
|---|---|---|
| Trello card #61, Leonard's comment | **Open fork (DR1).** | No settler found. |
| Robert's Sep 18 approval and Sep 30 pull | Halloween is off the calendar. | Robert is "Product" per Confluence `page_zm3d_gdd` and `page_season_pass_spec` ("Owner: Robert (Product)"). DM `669d15f685f158633e56302160957f1e`: "Take it off the beta calendar ... my later word on this one is the one that counts". Settled. |
| Martin's Endless desert and port themes (#zombie-art, Sep 29-30) | Not beats or still-to-dos. | Proposals only, with no approval or window. |

## Forks checked and settled (no finding)

### Destinations and sources

- **"my live-ops calendar sheet":** this is `f_e4a17c90b3d25f6a8c1d73` "ZM3D Beta Live-Ops Calendar", owned by Julia, in folder `d_5f2c8e1b7a94d03c6e2b58` "ZM Live Ops". Frederick: "Put it in the calendar sheet in your ZM Live Ops folder". The other live-ops calendars ("LiveOps Event Calendar", Leonard's "Live Ops Planning") are not Julia's.
- **"the brief he shared with me":** this is `f_7c3e91a4d2b85f60e1a9c4`, shared to Julia as reader.
- **"the PNs Beta tab":** this is the Zombie Match sheet `f_a325dd4af80afc5994d5dc`, not "Push Notifications Domino Adventure".
  - Only the Zombie Match sheet has the Ready/Not Ready column the brief's push rule needs.
  - Its non-beta rows are exactly "Hourly Coins, Nathan's Treasure Hunt, Streak Fever and Axe Arena, just those four".
  - Its "PN BETA Translated" tab is the Domino set, as the brief says.

### Pushes

- 10 rows remain after the four exclusions.
- Two go out: lives-recharged ("Full Ammo Reloaded!") and 7-days-lapsed. Both are Ready, LIVE and name no game.
- Eight are held:
  - quests: Not Ready
  - 1-day lapsed and FTUE: "Puzzles vs Zombies"
  - Win & Collect: Not Ready, WIP, and the Domino name; the ZM3D name is "Collect & Win" per `page_liveops_calendar`
  - Plague Race: WIP
  - Login Calendar: Not Ready, WIP
  - Season Pass: Not Ready, WIP
  - Weekly Leaderboard: WIP
- The decisions are robust. Only the "what is missing" wording can vary, for example whether "Weekly Rankings" or "login calendar" counts as a wrong event name.

### Beat set and windows

- **Beat set:** Collect & Win, Season Pass (October and November seasons), Plague Race, leagues/weekly leaderboard, Endless (daily 00:00 UTC and Mon 00:00 UTC resets, per `page_liveops_calendar` and `zombies-game-cdk-stack.ts` l.136-189), quest rollover, and daily gift.
  - Out: Boss Arena (brief), Zombie Lane (Frederick) and Halloween (Robert).
  - Lives, lapsed and FTUE notifications are pushes, not beats. The brief says "a start push".
- **C&W first window:** Fri Oct 10 00:00 UTC to Sun Oct 12 23:59 UTC.
  - The release is Wed Oct 8 15:00 UTC (18:00 Istanbul), and the brief says "a window the release instant pre-empts does not count". That also rules out the CDK cron's Thursday 00:00 firing for group 2.
  - Using the release end (16:00 UTC) changes nothing.
  - The beat is "starts late, it is not held". The window end can be written as 23:59 or as 00:00 the next day.
- **Season Pass:** the October season runs Oct 1 00:00 to Oct 31 23:59 UTC and is visible in all four weeks ("Season Pass seasons open on the 1st at 00:00 UTC"). It is not clipped to Oct 6, because "a different instant is not" fine. The November season opens Sat Nov 1 00:00 UTC.

### Holds, lock and reply

- **Leaderboard hold versus "unverified build":** Vincent tested "on the current prod build" on two devices, which matches the brief's "on prod even after a restart". I read it as an established failure, not an unverified build, so the beat is held and the note goes on ZOM-429.
- **Lock exists:** `page_liveops_calendar` says "There is no technical content lock", but it also says "The 24h season-pass freeze in the Season Pass spec is a process control on top of that". The lock is that freeze, Oct 31 00:00 UTC.
- **Reply thread:** the reply goes on the Sep 26 thread, per Brian's "reply on this mail".

### Equivalent paths (rubric must accept either)

- "link it on the calendar ticket" can be done with `linear_create_comment` or with `linear_update_issue` adding the link. Same destination and content.
- "back here" can be a reply in Frederick's DM thread or a new message in the same DM. Same recipient, so Clarity 3 at most.

### Edge values worked through, none of which changes an answer

- UTC versus PT for the lock and for Brian's handoff.
- Istanbul read as UTC+3 or UTC+2.
- C&W window end written as 23:59 or as 00:00 the next day.
- Release instant read as the start or the end of the window.
- Calendar span cut-off (Sun Nov 2 23:59 UTC) for the last C&W window, Fri Oct 31 to Sun Nov 2.
- Before or after a later correction in the thread: ZOM-432 (Done), ZOM-465 (later "still to do"), ZOM-526 (unticked) and Brian's Sep 26 change, each read at its latest value.

## Platform notes

- Anonymized tokens in the push copy ("[PERSON_NAME_2549] your first mission", "Nathan's [PERSON_NAME_16313]") are the source strings. Do not score them.
- No FD-2880 or FD-3785 dependency. No Slack paste artifact affects the saved files.
