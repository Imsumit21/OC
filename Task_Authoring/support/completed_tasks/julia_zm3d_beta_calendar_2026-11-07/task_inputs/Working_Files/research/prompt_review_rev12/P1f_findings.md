# P1 deep recheck: Unique Ground Truth and Clarity (independent sample P1f)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
SQL read: sha256 b5ccbfa5...d60d3 (matches the setup). Blind: I did not open R/prev/, R/work/, task_inputs folders or other reviewers' files.

## Findings

`none`. Checked 45 sentences (prompt 6, Frederick's message 6, his reply 5, brief 28), 6 writes and the recommendation.

No fork is left without a killing quote. Every decision-sweep item is RECORD. I found no SCOPE_GAP or SILENCE item that a careful reader could put in a cell. Two forks are close calls (F1 and F2), and the main session should test those quotes itself. F1 is the one I would attack first.

## What each write must hold

| # | Write | Target | Must contain |
|---|---|---|---|
| W1 | Calendar tab | ZM3D Beta Live-Ops Calendar, in ZM Live Ops | 7 rows, listed below |
| W2 | Pushes tab | same sheet | 10 lines (14 rows less 4); 2 send, 8 held |
| W3 | Ticket note | ZOM-429, assignee Douglas | Weekly Leaderboard is held until the fix is confirmed on prod |
| W4 | Sheet link | ZOM-78 | The sheet link |
| W5 | Recommendation | Frederick, DM D05SD5QLG94 | The call, with trade-offs |
| W6 | Mail reply | Brian's Sep 26 mail | Oct 31 10:00 Istanbul = 07:00 UTC misses the lock of Fri Oct 31 00:00 UTC; the date moves to any time before it |

W6 is the only write a rule requires that the prompt does not name.

W1 rows:

| Beat | Windows and weeks | Status | Still to do (owner) |
|---|---|---|---|
| Collect & Win | First window Fri Oct 10 00:00 to Sun Oct 12 23:59 UTC; 10 windows, W1-W4 | Starts late, not held | Prod deploy Oct 8 (Douglas); final vial models (Claire); event icon animation (Marcus) |
| Season Pass | Oct 6 00:00 to Oct 31 23:59; Nov 1 00:00 to Nov 2 23:59 (clipped) | Runs | November config before the lock (Brian); November strip art (Oliver) |
| Weekly Leaderboard | 4 Mon-Sun windows | Held until the fix is confirmed on prod | Fix (Douglas) |
| Endless | 4 Mon-Sun weekly windows, plus the daily 00:00 reset | Runs | None |
| Plague Race | In, W1-W4, no window dates | Runs, push held | None |
| Daily gift | In, W1-W4, no window dates | Runs, push held | None |
| Quest rollover | In, W1-W4, no window dates | Runs, push held | None |

Not on the calendar: Boss Arena, Zombie Lane, the shop rotation, Halloween.

W2: rows 4 (lives recharged) and 6 (7-day lapsed) send. The other eight are held:

| Row | Push | What is missing |
|---|---|---|
| 2 | Quests | Not Ready |
| 5 | 1-day lapsed | Copy says "Puzzles vs Zombies" |
| 7 | FTUE | Copy says "Puzzles vs Zombies" |
| 8 | Collect & Win | Not Ready, WIP, copy says "Win & Collect" |
| 10 | Plague Race | WIP |
| 13 | Login Calendar | Not Ready, WIP |
| 14 | Season Pass | Not Ready, WIP |
| 15 | Weekly Rankings | WIP |

No beat's push goes out. Both sends are local notifications.

W5 must say:
- Run: Season Pass, Endless, Plague Race, daily gift, quest rollover, and Collect & Win from Fri Oct 10.
- Hold: Weekly Leaderboard until the fix is confirmed on prod, with no date, plus the 8 held pushes.
- It must take a position and give trade-offs.

No part of the run/hold call has a second answer, because "Hold a beat only when" fixes it. The trade-off wording is open, so the rubric can test only that trade-offs are present and that they fit the call.

## Fork list

Close calls first. All are RECORD unless marked otherwise.

- **F1: Is any beat held (write vs no-write on ZOM-429)?**
  - Reading A: Weekly Leaderboard is held and gets a note.
  - Reading B: nothing is held, because this is "a reset that needs a restart", Douglas said "so not blocking", and one QA report is unverified and names no enter, score or claim failure.
  - Settled by: Vincent, C0880U9751A, id b5f2955c..., 2025-09-30: "it still does not start a new week. I killed the app and reopened it twice, played a few levels, and my week is still last week one. Same on the second device." Also the ZOM-429 description: "it doesn't start the new one or let me claim my rewards."
  - Douglas's cmt_zom429_1 (Sep 16) is the assignee's older claim and cannot settle it.
  - Residual: the Sep 30 post does not use the rule's verbs. The kill rests on its plain meaning plus "still" tying it to ZOM-429.
- **F2: Must the agent send the mail to Brian (write vs no-write)?**
  - Reading A: it replies on the mail.
  - Reading B: the prompt lists its writes and omits this one, "building it" limits the brief to the sheet, and "is told" names no sender.
  - Settled by: brief: "its owner is told in a reply on the mail where they committed to it"; prompt: "Can you take it on for me?"; Brian's mail to Julia: "If the new date is a problem on your side, reply on this mail."
  - WORKFLOW also says not to flag incorporated instructions because the prompt does not repeat them.
  - Residual: the passive voice. The sender is settled by a fact record, not by a rule sentence.
- **F3: Which mail?** A: Sep 26. B: Sep 22. Settled by: "Treat Fri Oct 31 as the date I am committing to and drop the Oct 29 one."
- **F4: Lock instant.** A: Oct 31 00:00 UTC. B: no lock, or "the day before" read as all of Oct 31, so 07:00 UTC passes. Settled by: Season Pass spec: "locked 24h before each season opens"; Live-Ops page: "The 24h season-pass freeze"; brief: "read in server time (UTC)".
- **F5: Is #468 rc_38 (vials) a change-request blocker that holds Collect & Win?** A: Still to do only. B: held under "unresolved change-request review blocker".
  - Settled by: #468#rev_3 state 'COMMENTED' (SQL line 156); brief: "cosmetic, VFX and performance gaps ... do not hold a beat".
  - The change-request rule has no live instance. The newest CHANGES_REQUESTED review on any PR is #303 on 2025-07-16, and no timeline event shows one later. "Aug-Sep live-ops cohort" is undefined, but that changes nothing.
- **F6: Does Collect & Win need to wait for the art?** A: runs from Oct 10, art listed as must-land. B: hold until the vials and icon land, per "need to be in before the beta". Settled by: "Hold a beat only when players provably cannot enter, score or claim"; rc_38: "still the first-pass models".
- **F7: Is Collect & Win held because its windows are not on prod?** Settled by: "starts late, it is not held". cmt_zom563_1 kills the idea that the Sep 30 prod update carried them: "the Collect & Win server windows wait for the Oct 8 release."
- **F8: Collect & Win first window.** A: Fri Oct 10. B: the Wed-Thu window, joined mid-way on Oct 8. Settled by: "the first window that opens after".
- **F9: Endless freeze holds Endless?** Settled by: e343557b..., Leonard: "Could not get it to freeze, so I am leaving this one."; brief: "an unverified one does not".
- **F10: Quest points hold the quest rollover?** Settled by: cmt_zom534_2, Leonard, the reporter: "Quest points reset on their own, no restart." The "needs a restart" exclusion covers it anyway.
- **F11: ZOM-556 holds the daily gift?** Settled by: "Wrong counters ... do not hold a beat"; cmt_zom556_1: "claiming works and nothing is lost."
- **F12: Does the hold reach Endless's own weekly board?** Settled by: Vincent's "played a few levels"; ZOM-429 is the main board. A hold needs an established failure, and none is reported for Endless.
- **F13: Is Endless on the calendar?** A: in. B: out, like Zombie Lane, as a permanent mode. Settled by: brief: "an event window, a reset or a start push"; reply: "no window or reset to plan"; Live-Ops page: "daily reset 00:00 UTC, weekly reset Monday 00:00 UTC".
- **F14: Are Leagues and Weekly Leaderboard two beats?** Settled by: LeaderboardController.weekly calls Leagues.get_league_record; CDK LEAGUES_SCHEDULE "0 0 * * 1".
- **F15: Does Halloween stay as an overlap?** Settled by: Robert's DM, 669d15f6...: "pulling my ok. Take it off the beta calendar".
- **F16: Plague Race, quests and daily gift: window dates?** A: none. B: Frederick's newer message asks "which windows", so give them. Settled by: "The working rules for the calendar are in my brief"; "Two things on top of the brief"; brief: "not its window dates".
- **F17: Season Pass first window.** A: Oct 6, clipped. B: Nov 1. Settled by: "Clip anything that starts before".
- **F18: Is more quests / reward balance in Still to do?** Settled by the rule test "flagged ... as still needed", plus "Nothing else goes in". The Trello comment says only "if they are ready". I rest this on the rule, not on Leonard's "does not wait on them", because he owns that card.
- **F19: Store approval of the Sep 30 builds in Still to do?** Settled by: "flagged since this brief" (the deck is dated Sep 23); "Nothing else goes in".
- **F20: Other Still-to-do candidates.** All out:
  - ZOM-432: closed, and first flagged before the brief.
  - ZOM-565, ZOM-526, ZOM-566 title text: Brian: "do not have to land before the beta".
  - lightSweep: "nothing has to land for the beta".
  - ZOM-552, ZOM-566 analytics: "not analytics".
  - Endless themes: "nothing waits on new themes".
  - ZOM-543: not flagged as needed.
- **F21: Prod deploy owner.** A: Douglas. B: Arthur or Owen. Settled by: GCal organizer douglas@, "Prod backend deploy for the beta"; Live-Ops Event Engine: "Scheduler ... Backend (Douglas)".
- **F22: Which PNs Beta tab?** A: Zombie Match. B: Domino, which has the same tab name. Settled by: "its row is Ready and LIVE"; only the Zombie Match tab has a Ready column and a Plague Race row.
- **F23: Must a nameless row still be Ready and LIVE?** Settled by: "the naming rule is only about wrong names". Row 15 stays held.
- **F24: Is "Win & Collect" a wrong name on row 8?** Settled by: Live-Ops page: "Same feature as Win & Collect on Domino Delights, under a different name". The row is held either way; only "What is missing" changes.
- **F25: Does the recommendation cover pushes?** A: beats and pushes. B: beats only. Settled by: "what we hold"; brief, on pushes: "Anything else is held"; the ask is for the "live-ops and push calendar".
- **F26: Which ticket, which sheet?** Settled by: ZOM-78, cmt_zom78_1: "Link the sheet here when it is ready"; no other live-ops calendar sheet in Julia's Drive.

Not a fork: Endless has both weekly and daily resets. Both are true, not rivals, so a row states both.

Forks: none open.

## Edge values

| Item | Edges tried | Result |
|---|---|---|
| Release instant | Window start 15:00 or end 16:00 UTC; UTC, Istanbul or PT | Fri Oct 10 in all cases |
| Collect & Win windows | 12 in span, 2 open before the release | 10; the last ends exactly at Nov 2 23:59, so no clip |
| Lock vs Brian | 00:00 UTC vs 07:00 UTC | Misses by 7 hours |
| Corrections | Brian Sep 22 to Sep 26; Robert Sep 18 to Sep 30; Douglas Sep 16 to Vincent Sep 30; Marcus Sep 26 to Sep 30 on ZOM-465 | The later record wins in each |
| Borderline status | ZOM-534 In Progress but confirmed on prod; ZOM-432 Done but only in submission builds | Neither changes a cell |
| Push counts | 14 rows, 4 left off | 10 lines, 2 send, 8 held |

Dates checked: Oct 6 is a Monday, Oct 8 a Wednesday, Oct 10 a Friday, Oct 31 a Friday, Nov 1 a Saturday and Nov 2 a Sunday.

## Rubric cautions (later stage)

- The moved config date must accept any time before the lock.
- A Calendar row for Plague Race, quests or the daily gift cannot be required to carry window dates.
- The Endless row should accept weekly windows with the daily reset stated.

## Platform defects

None. Known issues near the task, none of which the answer relies on: SC-13 (Trello "BETA: Oct 10"), SC-38 (Season Pass ship date), SC-57 (#zm-collect-win), SC-62 (reward import cadence).

## Scanned

- **Slack (Julia-visible):**
  - Read in full, non-bot: #zombie-bugs from Sep 22, #zombie-match3d from Sep 24, the Frederick DM from July.
  - Read in full: #zombie-art, #zm-animations, #zombie-ops and other small channels from Sep 24, and #zm-collect-win for context (Julia is not a member).
  - Keyword-filtered only: the Robert DM and #zombie-design since Sep 24, plus all visible channels for Aug-Sep on beat names, beta, lock, push, one-offs and prod failures.
- **SQL:** read in full; injected rows came from it, not from the base scan.
- **Linear:** all ZOM issues from 400 up, all issues updated since Sep 20, open ZOM tickets by live-ops terms. The base has no comments, so all comments are injected.
- **GitHub:** all CHANGES_REQUESTED reviews, timeline events, open PRs; human review comments on Aug-Sep PRs; #468, #470, #472, #477, #438; git logs of match3d and match3d-backend; CDK schedules; ZM-Liveops-Docs.
- **Confluence:** all 30 page titles; Live-Ops Calendar, Live-Ops Event Engine, Season Pass Spec and GDD in full; all comments; lock and freeze grep across pages and versions.
- **Trello:** the full ZM ROADMAP board and its actions since Sep 10.
- **Sheets:** PNs Beta in both Push Notifications spreadsheets, the Zombie Match PNs and translated tabs, live-ops sheet titles.
- **Drive and Docs:** metadata scan; Endless Monster Mode, Event Icon Management and Collect & Win Endpoints docs.
- **Gmail:** Julia's mailbox by live-ops terms, and all her mail since Sep 10.
- **GCal:** events since Sep 15 by release and live-ops terms.
- **Snowflake:** LIVE_EVENT_PERFORMANCE only; no ZM3D failed or degraded row after Aug 27.

Limits:
- Slack outside the channels listed was keyword-filtered, not read.
- Google Docs were filtered by title.
- `search-many` on Snowflake returned no usable output, so I scanned the file directly.
- Contacts was not scanned.

Setup deviation: helper scripts went in scratchpad/p1f_tmp, not R/work, because this task forbade opening R/work. I deleted them afterwards.
