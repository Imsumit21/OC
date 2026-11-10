# Deep recheck P1 · Unique Ground Truth and Clarity

Pass P1, blind to the main review. Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Inputs read verbatim: `04_Prompt.txt`, the Platform assignment block of `00_Task_Assigned_Inputs.md`, `02_Universe_Date.txt`, `01_Universe_Inject.sql` (read in full, not executed; its rows are treated as part of the universe).

**Sentences checked: 42.** That is 6 prompt sentences (S1–S6) plus 36 sentences from the sources the prompt pulls in:
- Frederick's DM `slack D05SD5QLG94 8b090dec472117f4598b9ad84318272e`: 5 sentences.
- His thread reply `097c95c6e043ada8294b60f13e1656ba`: 5 sentences.
- The brief `gdocs f_7c3e91a4d2b85f60e1a9c4` "ZM3D beta live-ops calendar - working rules": 26 sentences.

Records opened to settle them: UA plan deck `f_2b9d4e7a1c63f08d5e7b21` (3 slides), the calendar sheet `f_e4a17c90b3d25f6a8c1d73` (both tab headers), the PNs Beta tab of "Push Notifications Zombie Match" (`gsheets data.json /sheets_spreadsheets/220/sheets/1`, 14 rows), and every record cited below.

Format: `DR# | pass | checklist section | quote | record | dimension / issue | proposed score or severity`, then the readings and what would settle the fork.

---

## Findings

**DR1 | P1 | §2 Kill the other reading: which beats are held (what counts as the event) | Prompt S5 "If a beat ends up held, leave a note on its ticket so the owner picks it up." with brief "An unresolved change-request review blocker on an in-scope live-ops PR from that cohort does hold it." | GitHub `harmonygames-Games/match3d#438#rev_4` (state `COMMENTED`, 2025-09-30T20:41:17Z) `#rc_74` "The Season Pass premium strip needs to move to the November range rather than the current one — Oliver is taking the date change."; `match3d#370#rev_1` (`COMMENTED`, 2025-09-30T19:48:33Z) `#rc_1` "The final vial sprites are still missing for the Collect & Win set — Claire has those on her list." | Unique Ground Truth; Clarity (Action Decision Ambiguity) | UGT 2 / Clarity 2**

Both PRs fall inside Aug–Sep by either date. #438 "Feature/season pass" was created and merged 2025-09-15. #370 "Collect&Win Items" was created 2025-08-08 and merged 2025-08-13.

In the base data, the only `CHANGES_REQUESTED` review on any match3d PR is `match3d#303#rev_6`: CodeRabbit, 2025-07-16, on "Samuel/zom 349". That is outside Aug–Sep, which fits the brief's "neither does a change request outside the Aug-Sep live-ops cohort". On the Aug–Sep live-ops PRs, CodeRabbit's reviews are all `COMMENTED`, but they carry open "Actionable comments":
- `#438#rev_1` "Actionable comments posted: 71" and `#rev_3` "…: 4".
- #468 "Collect And Win": 36, then 1.
- #470: 1, 1, 1, 2.
- Reading A: "change-request review" means a GitHub *Request changes* review. The cohort has none, so neither Season Pass nor Collect & Win is held. Arthur's two comments go under "Still to do (owner)" (Oliver: premium strip; Claire: vial sprites), following the brief's "player-facing art an owner has flagged". The only ticket note is the weekly-leaderboard one (ZOM-429).
- Reading B: Arthur's Sep 30 review comments are change requests made in a review. They are unresolved ("is taking", "still missing") and sit on in-cohort live-ops PRs. Under the brief that makes them blockers, so **Season Pass and Collect & Win are both Held**. Each gets a Status, a Hold-until value and a ticket note, and the recommendation changes. Where the note goes is itself unsettled: Linear ZOM-552 or ZOM-566, Trello ZM ROADMAP card #27 "Season Pass" or #10 "Win and Collect", or the PR. CodeRabbit's open actionable-comment reviews on #438, #468 and #470 support the same reading.
- What differs: the decision (2 beats held or not), the writes (+2 ticket notes), the sheet's Status and Hold-until cells, and the recommendation.
- Why nothing kills B: the brief never defines "change-request review blocker", "in-scope" or the "Aug-Sep live-ops cohort". The `COMMENTED` state is the only record that pushes against B, and nothing says a COMMENTED review cannot carry a change request. A reviewer-flagged art or date fix fits both the "Still to do" sentence and the "Held or not" sentence.
- Missing: a brief or message sentence saying a change-request blocker means a GitHub "Request changes" review, or that reviewer-flagged art and date fixes are still-to-dos, not holds.

**DR2 | P1 | §2 what gets written / Eval 1 §2.6 write vs no-write | Brief "A committed date that misses the lock moves earlier and its owner is told." Prompt S6 names the closing writes as "link it on the calendar ticket and send Frederick the recommendation he asked for" and names no message to the config owner | Confluence `page_season_pass_spec` "Season config (tiers, rewards, theme) is authored in the live-ops tool and locked 24h before each season opens"; Gmail `julia.lawson@harmonygames.co/<CAH4q9Zc8uV1nE5kJ2mRtP7aW3xQ9bLs@mail.gmail.com>` (Brian, 2025-09-26) "moves from Wed Oct 29 to Fri Oct 31, 10:00 Istanbul time … Treat Fri Oct 31 as the date I am committing to"; Brian's Sep 22 mail `…<CAH4q9Zb2fK7xQe1M8sPnL3vT6wR0yDc@mail.gmail.com>` "If anything moves on your side, tell me before that date, not after." | Clarity (Action Decision Ambiguity); UGT | Clarity 2 unless B is killed**

The rule does fire:
- Lock: Fri Oct 31 00:00 UTC, which is 24 h before "Season Pass seasons open on the 1st at 00:00 UTC" and Brian's "The November season opens on Sat Nov 1".
- Brian's commitment: Fri Oct 31 10:00 Istanbul (UTC+3), which is 07:00 UTC.
- It misses the lock by 7 h whether you read it in UTC or Istanbul time.

The readings:
- Reading A: the agent, acting as Julia, tells Brian (a reply on his mail thread or a Slack DM) that the handoff has to move earlier.
- Reading B: "its owner is told" is passive, and the prompt spells out the writes without any message to Brian. So the agent puts the earlier date and the owner in the sheet's Still to do and in the recommendation to Frederick (who is cc'd on Brian's thread), and sends Brian nothing.
- What differs: one extra write, or none.
- Counter-quote the main session may test: brief "The rules stay here; the calls are yours." This addresses the rules to Julia, but it still does not say who tells the owner.
- Missing: a prompt or brief sentence saying the agent tells the owner, and through which channel.

**DR3 | P1 | §2 which number or date (edge values) | Brief "A committed date that misses the lock moves earlier" | Brian's Sep 22 mail `julia.lawson@harmonygames.co/<CAH4q9Zb2fK7xQe1M8sPnL3vT6wR0yDc@mail.gmail.com>` "The config handoff we agreed with Product is for Wed Oct 29"; spec `page_season_pass_spec` "locked 24h before each season opens" (gives Fri Oct 31 00:00 UTC) | Unique Ground Truth (date figure) | BOTH_FAIR_FIGURE candidate (else UGT 2)**

- Reading A: move it to just before the lock, meaning Thu Oct 30 (by 23:59 UTC) or "before Fri Oct 31 00:00 UTC".
- Reading B: move it back to Wed Oct 29, the date "agreed with Product".
- Both readings make the same decision (move the date earlier and tell the owner) with the same writes, destinations and recipients. Only the date differs.
- Newer-source check: Brian's Sep 26 "drop the Oct 29 one" withdraws Oct 29 as his own commitment. The brief overrides his commitment anyway, so this does not pick the replacement date. No record names it.
- Settled by: a sentence giving the target, either "move to the lock" or "move back to the agreed date". Otherwise the rubric must accept any time before Fri Oct 31 00:00 UTC, which covers both Oct 29 and Oct 30.

**DR4 | P1 | §2 which items are in the set / what gets written | Prompt S5 "If a beat ends up held, leave a note on its ticket so the owner picks it up." with brief Scope "Every ZM3D beat a player can see in those weeks: an event window, a reset or a start push." and brief Push copy "Anything else is held, with what is missing." | `gsheets data.json /sheets_spreadsheets/220/sheets/1` (Push Notifications Zombie Match › PNs Beta): row 9 Plague Race "Ready"/"WIP", row 7 Win & Collect "Not Ready"/"WIP", row 13 Season Pass "Not Ready"/"WIP", row 1 Quests "Not Ready", row 12 Login Calendar "Not Ready"/"WIP", row 14 Weekly Leaderboard reset "Ready"/"WIP" | Clarity (Action Decision Ambiguity); UGT | Clarity 2 / UGT 2**

- Reading A: only beats held under "Held or not" get a ticket note. That is the weekly leaderboard, on ZOM-429. Held pushes are recorded on the Pushes tab only.
- Reading B: the brief lists a start push as a kind of beat and calls a failing push "held". So each held start push gets a note on its beat's ticket: Plague Race, Collect & Win, Season Pass, quest rollover, and Login Calendar / daily gift. That is up to 5 extra notes, on Trello ZM ROADMAP #1, #10, #27, #4 and #6, or on Linear.
- What differs: the number of ticket-note writes, 1 or up to 6.
- Counter-quote: Frederick's DM "if anything is held and until when, the push that goes with it" treats the push as part of a beat, but it does not say a held start push is not a held beat. No ZOM ticket exists for these pushes. The only ZOM titles matching "push|notification" are ZOM-295, ZOM-320 and ZOM-366, none of them about these pushes.
- Missing: a sentence limiting ticket notes to beats held under "Held or not", or saying held pushes stay on the Pushes tab.

**DR5 | P1 | §2 which date (content) | Frederick's DM "if anything is held and until when"; sheet column "Hold until (UTC)" | Linear ZOM-429 "Leaderboard next session doesn't start without killing the app" (Backlog, assignee douglas@, `due_date` null), injected `cmt_zom429_1` (Douglas, 2025-09-23) "not blocking. Leaving as-is for now."; Slack `C0880U9751A fa3eee2c614b0741aeb240275f86abf7` (Vincent, 2025-09-30T20:50Z) "Re-tested the weekly leaderboard on the current prod build: it still does not start a new week … Same on the second device." No fix PR, ETA or date anywhere: searched Slack, Linear and GitHub for "ZOM-429", "weekly leaderboard" and "leaderboard reset" | Unique Ground Truth (content cell) | UGT finding unless the main session accepts "no date" as the single record-backed value**

- Reading A: Hold until is "open, until ZOM-429 is fixed and verified on prod". No date exists.
- Reading B: Hold until is "Sun Nov 2 23:59 UTC". With no fix scheduled, the beat is held for the whole buy, as a planning call ("the calls are yours").
- What differs: the content of a cell Frederick asked for.
- Missing: a dated fix or ETA record for ZOM-429. Otherwise the rubric must accept either.

**DR6 | P1 | §2 which date (edge: a window that straddles the span) | Brief "A beat starts with the first window that opens after its server windows are live on prod"; "Every window is stated in server time (UTC) as a start-end instant. A PT/PDT rendering of the same instant is fine, a different instant is not."; sheet column "First window (UTC)" | GitHub `match3d#470#rc_10` (injected, Arthur) "The Plague Race, leagues, Endless and Season Pass schedules are already running on prod."; `match3d-backend/zombies-game-cdk/lib/zombies-game-cdk-stack.ts` lines 186–189 `SEASON_PASS_SCHEDULE: props.production ? "0 0 1 * *"` ("PROD: every first day of the month at 00:00 AM UTC"); `page_season_pass_spec` "production seasons reset monthly on the 1st at 00:00 UTC"; Brian's mail "The November season opens on Sat Nov 1." | Unique Ground Truth (date figure) | BOTH_FAIR_FIGURE candidate (else UGT 2)**

- Reading A: Season Pass's first window is Wed Oct 1 00:00 UTC. That is the October season (Oct 1 00:00 – Oct 31 23:59 UTC), already open when the buy starts. The next opens Nov 1 00:00 UTC.
- Reading B: the first window is Sat Nov 1 00:00 UTC, the first one that opens inside Mon Oct 6 – Sun Nov 2. A variant clips the windows to the span (Oct 6 00:00 start, Nov 2 23:59 end). The brief's own rule calls a clipped instant "a different instant".
- Only Season Pass straddles the span. Every other figure holds under each edge:
  - Plague Race (`"0 0 * * *"`), leagues (`"0 0 * * 1"`) and both Endless resets open at Mon Oct 6 00:00 UTC.
  - Collect & Win opens Fri Oct 10 00:00 UTC either way.
- Missing: a sentence saying whether a window already open at the span start counts as the first window, and whether straddling windows get their full or clipped instants. SC-38 (Season Pass ship date) is not relied on here.

**DR7 | P1 | §2 contents (open-ended call with no acceptance boundary) | Frederick's DM "your recommendation with the trade-offs … This goes into the pivot call, so I need your call, not a list of what we have."; prompt S6 "send Frederick the recommendation he asked for" | UA plan `f_2b9d4e7a1c63f08d5e7b21` `el_c07b2e9d3148` "Once the stores approve we start buying users at small scale and hold the spend there until the pivot call."; `el_5e83a1f4c092` "Small scale at first, scaled up week by week if the cohorts hold."; Slack `C08H78VJG80 33e6b9aae589e8207d7838f49b135ca1` (Frederick, 2025-09-29) "we are considering a pretty substantial pivot in core game play for Zombie Match." | Unique Ground Truth (contents); Clarity | Clarity 3 (same write); UGT 2 if no objective boundary is found**

- Reading A: the call is about running the calendar: what carries W1 before Collect & Win opens on Oct 10, and what to fix or move first.
- Reading B: the call is about the buy or the pivot: whether and when to scale spend (stay small in W1, or scale from W2) given the held and late beats, as input to the pivot call.
- Nothing names the decision the call answers. Both readings deliver "a call with trade-offs", but the contents differ.
- Missing: a sentence naming the decision the call answers.

**DR8 | P1 | §2 what gets written | Prompt S3 "What he wants in it is in his message"; Frederick's DM "Every beat players can see in those weeks: which windows it runs in, if anything is held and until when, the push that goes with it, what still has to land before it runs and who owns that, and your recommendation with the trade-offs. Put it in the calendar sheet in your ZM Live Ops folder … and send me the recommendation back here." | Sheet `f_e4a17c90b3d25f6a8c1d73` tab "Calendar" headers ["Beat","What players see","First window (UTC)","Windows (UTC)","Weeks running","Status","Hold until (UTC)","Push","Still to do (owner)"] and tab "Pushes" headers ["Beat","Push name","Send (UTC)","Segment","English copy","Status","Notes"]. Neither tab has a recommendation column | Clarity; UGT (sheet contents) | Clarity 3; record the fork, and the rubric must accept either**

- Reading A: the recommendation goes only in the Slack DM thread. The sheet holds the calendar columns.
- Reading B: the recommendation is part of "what he wants in it", since the colon list ends with it. So it is also written into the sheet (a per-beat note or a recommendation tab) as well as sent in the DM.
- What differs: an extra sheet write.
- Missing: a sentence saying where the recommendation lives.

**DR9 | P1 | §6.2 Clarity (wording; no effect on writes) | Brief "One-offs may overlap a recurring beat slots. A one-off may take a recurring beat slot only with Product latest dated approval, and if he takes that back his later word is the one that counts." | `page_season_pass_spec` "Owner: Robert (Product)"; `C08R8CHB0QL 2e75e232f5e6206273411a8305ac5d01` (Robert, 2025-09-18) "approved from my side"; `D05GU6L0XFH 58d06bd55ea4129eaadb726291967d5a` (Robert, 2025-09-30) "pulling my ok. Take it off the beta calendar" | Clarity (minor) | Clarity 4 (NON-FAIL wording only)**

The brief has two grammar slips ("a recurring beat slots", "Product latest dated approval"), and "Product" is a person the brief never names. It resolves to Robert through the spec. Even if "Product" meant Julia, no approval would be standing, so Halloween comes off the calendar under both readings. No write changes.

---

## Fork list

- F1 (DR1): Season Pass / Collect & Win held or not | Reading A: a "change-request review" is a GitHub Request-changes review; none in the cohort, so both beats run and Arthur's comments are still-to-dos for Oliver and Claire | Reading B: Arthur's open COMMENTED review change-requests on #438 and #370 are blockers, so both beats are held, with 2 ticket notes | Missing: a definition of "change-request review blocker" and "Aug-Sep live-ops cohort".
- F2 (DR2): tell the config owner or not | Reading A: message Brian | Reading B: only record it in the sheet and the recommendation | Missing: a sentence saying who tells the owner, and where.
- F3 (DR3): the moved-to config date | Reading A: before Fri Oct 31 00:00 UTC (Thu Oct 30) | Reading B: Wed Oct 29 | Both fair: Oct 30 or Oct 29 (any time before Oct 31 00:00 UTC), as a BOTH_FAIR_FIGURE candidate; the rubric must accept either.
- F4 (DR4): ticket notes for held start pushes | Reading A: the weekly-leaderboard note only | Reading B: plus up to 5 notes for held pushes | Missing: a sentence limiting notes to beats held under "Held or not".
- F5 (DR5): weekly leaderboard Hold until | Reading A: open, until fixed (no date) | Reading B: Sun Nov 2 23:59 UTC | Missing: a dated fix or ETA record for ZOM-429.
- F6 (DR6): Season Pass first window | Reading A: Oct 1 00:00 UTC | Reading B: Nov 1 00:00 UTC (or instants clipped to the span) | Both fair: Oct 1 00:00 UTC or Nov 1 00:00 UTC, as a BOTH_FAIR_FIGURE candidate; the rubric must accept either.
- F7 (DR7): the decision the recommendation makes | Reading A: a call on running the calendar | Reading B: a call on scaling the buy / the pivot | Missing: the decision question.
- F8 (DR8): where the recommendation lives | Reading A: DM only | Reading B: DM and sheet | Missing: a sentence naming where it goes.

## Checked and settled (no finding)

- **Push sheet identity.** Two "PNs Beta" tabs exist: Push Notifications Zombie Match (`/sheets_spreadsheets/220`, domain, shared with Julia) and Push Notifications Domino Adventure (`/sheets_spreadsheets/73`). Two quotes settle it: Frederick's reply "Leave off the four rows … Hourly Coins, Nathan's Treasure Hunt, Streak Fever and Axe Arena, just those four", since only the ZM tab has exactly those four non-beta rows (the Domino tab also has River Rush, Tiledozer/Luckydrop and mini-game rows); and the brief's "Ready and LIVE", since only the ZM tab has a Ready column.
- **Pushes that go out.** Only rows 3 ("Full Ammo Reloaded!", Ready/LIVE, no game name) and 5 (7-day lapsed, Ready/LIVE, no game name) go out. Rows 4 and 6 name "Puzzles vs Zombies" and are held. Row 1 is Not Ready, and rows 7, 9, 12, 13 and 14 are not LIVE. The reply's "Copy that does not name the game at all is fine to go out" settles rows 3 and 5. The Pushes tab has 10 lines (14 rows minus the 4).
- **"his message".** This means the DM plus the thread reply 4 minutes later. The newer source, from the same author on the same scope ("Two things the brief does not spell out"), settles it.
- **Brief identity.** It is the only Frederick-owned doc shared with Julia; no base Frederick doc is shared with her.
- **Sheet destination.** The DM's "the calendar sheet in your ZM Live Ops folder" points to `f_e4a17c90b3d25f6a8c1d73`, which Julia owns, in folder `d_5f2c8e1b7a94d03c6e2b58`. The domain-visible "LiveOps Event Calendar.xlsx" is not "my".
- **Calendar ticket.** Linear ZOM-78, settled by `cmt_zom78_1` (Frederick) "Let us use this ticket for the ZM3D beta live-ops calendar instead of opening a new one. Link the sheet here when it is ready." ENG-2240 is not it.
- **Collect & Win first window.** The Oct 8 backend release is at 15:00–16:00 UTC (GCal `evt_5c1e83a7d94b02f6c8e31a`, "18:00-19:00 Istanbul time"). The Wed–Thu window opened Oct 8 00:00 and is pre-empted ("a window the release instant pre-empts does not count"). So the first window is Fri Oct 10 00:00 UTC, with 10 windows through Sun Nov 2 23:59 UTC. This is the same whether you use the release's start or end instant, and in UTC or a PT rendering. The brief's "each opening 00:00 UTC" means the CDK cron firing on Thursday (`"0 0 * * 3,4"`) does not open a new window.
- **Weekly leaderboard held.** Vincent's Sep 30 retest is newer than Douglas's Sep 23 "force-closes and reopens … fine". It matches the brief's "on prod even after a restart" ("on the current prod build … killed the app and reopened it twice … Same on the second device") and its "An established failure holds it". I also tried a reading that treats it as an unverified-build still-to-do (the Sep 30 submission builds); the retest is on prod, so that reading does not stand. The ticket is ZOM-429 (assignee Douglas); ZOM-71 is Done and unassigned.
- **Leagues = weekly leaderboard.** The CDK's `LEAGUES_SCHEDULE` ("every monday at 00:00 AM UTC") is the only weekly leaderboard schedule. Confluence `page_liveops_calendar` lists "Weekly Leaderboards — Domino Delights / Zombie Match 3D".
- **Halloween off.** "Owner: Robert (Product)" identifies Product, and Robert's later DM pulls his ok. Boss Arena (brief) and Zombie Lane (reply) are off too.
- **Config lock exists.** The spec says "locked 24h before each season opens". `page_liveops_calendar`'s "There is no technical content lock" is about the mechanism, and the same page calls "The 24h season-pass freeze in the Season Pass spec … a process control". That puts the lock at Fri Oct 31 00:00 UTC.
- **Plague Race windows are daily.** CDK `PLAGUE_RACE_SCHEDULE: … "0 0 * * *"`, and `plague_race.ex` sets `expires_at: Leaderboards.get_next_reset_date(event.schedule)`. Endless has a daily reset plus a Monday reset (CDK lines 144–155 and `page_liveops_calendar`).
- **Still-to-dos where the newer record wins:**
  - Daily-gift frame: nothing left. `#471#c_18` (Sep 30) "nothing is left on it" is newer than ZOM-432 (Sep 24).
  - Collect & Win icon animation: still to do. `#454#c_4` (Sep 30, author of "Marcus/animated icons") is newer than ZOM-465 (Sep 26).
  - Token travel and the two unticked ZOM-521 items: not still-to-dos. Brian's `cmt_zom526_2` says "does not have to land", and Calvin's `cmt_zom521_1` calls them "both polish". This follows SC-15.
  - Collect & Win prod deploy: the owner is Douglas, the GCal organizer.
- **Quest rollover and daily gift.** Both are in: the reset-needs-restart and cosmetic-counter cases do not hold under the brief. Their pushes are not ready (rows 1 and 12).

## Platform defects

- PLATFORM: anonymized tokens. `[PERSON_NAME_2549]` appears in PNs Beta rows 6 and 13, and `PERSON_0396_GITHUB_USERNAME` is the author of `#454#c_4`. Both rows are held for other reasons, and "Marcus" comes from the PR head ref "Marcus/Animated_Icons". No effect on any figure.
