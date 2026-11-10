# P1 deep recheck, rerun on rev12: Unique Ground Truth and Clarity

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
SQL read, never run; sha256 b5ccbfa5...60d3 matches the setup. Prompt and assignment are byte-identical to rev11. The diff against rev11 has 10 hunks, and I read each changed statement in full. I did not open R12/work/p1c or any other reviewer's file.

## Result

**No open Unique Ground Truth fork. F1, F2 and F3 are settled by the new brief text. F4 is unchanged and stays a harmless both-fair figure.**

I could not break the new text. One edit raised pressure on a rule that was idle in rev11: Arthur's vial note on PR #468 now reads like a blocker. Reading B there is still ruled out, but the kill now rests on the recorded review state, so the main session should open that record itself (break attempt B1).

## F1 to F4

| Fork | rev11 | rev12 | Record that decides it |
|---|---|---|---|
| F1 Rotating shop as a beat | Open | **Settled** | Brief: "and the shop rotation is not a beat." |
| F2 "Login calendar", "Weekly Rankings" as wrong names | Open | **Settled** | Brief: "(Login Calendar and Weekly Rankings are fine)" |
| F3 End instants, 23:59 or next 00:00 | Open | **Settled** | Brief: "Every window is stated in server time (UTC) as a start-end instant, closing 23:59 UTC on its last day." and "a different instant is not." |
| F4 Release instant, 15:00 or 16:00 UTC | Both fair | **Unchanged** | gcal evt_5c1e83a7d94b02f6c8e31a: start 2025-10-08 15:00 UTC, end 16:00 UTC. ZOM-563's new comment gives only "the Oct 8 release" |

What each settlement means in the cells:

- **F1:** The carve-out names only the shop, so "beat" is still not a closed list. I looked for any other reset to take its place and found none (B3).
- **F2:** Row 13's "What is missing" is Ready and LIVE. Row 15's is LIVE.
- **F3:** The October Season Pass closes Oct 31 23:59. Weekly Leaderboard and Endless weekly windows close Sun 23:59. Endless daily windows close 23:59. The Mon 00:00 and Nov 1 00:00 end instants are now wrong, because "a different instant is not" fine.

## Changed statements

| Hunk | Statement | Change | Effect |
|---|---|---|---|
| 1 | Brief, Span | The 23:59 close moved from Collect & Win to every window | Settles F3. Collect & Win is unchanged |
| 2 | Brief, Scope | Adds "the shop rotation is not a beat" | Settles F1 |
| 3 | Brief, Held | "usual windows and weeks" | Strengthens the rule that a held beat keeps W1-W4 |
| 4 | Brief, Push copy | Names the two fine terms; "what its row is missing" | Settles F2, and excludes beat-level reasons from the cell |
| 5 | Brief style runs | Offsets recomputed | All 9 runs land exactly on their title and headings |
| 6, 7 | #468 rc_38 and its #zombie-prs mirror | Adds "and need to be in before the beta" | Kills "polish, omit" for the vials. Creates the B1 pressure |
| 8 | ZOM-465 comment 3 | "was ticked before that event merged" | No cell changes. Dates agree: ZOM-525 Done Sep 17, #468 merged Sep 29 |
| 9 | ZOM-563 | New Douglas comment at 18:17:05Z; Vincent's becomes comment 2 | Gives Julia a visible kill for the "next backend release" reading, and supports Douglas as deploy owner |
| 10 | Trello action JSON | Adds idCard and textData | Format only. JSON is valid and matches base comment actions apart from `list` |

## Break attempts on the new and changed text

**B1. Does the vial note now hold Collect & Win?** This is the strongest attempt.
- Reading B: rc_38 is on PR #468 (live-ops, opened Sep 26, so in the Aug-Sep cohort). It says the models "need to be in before the beta", and they have not landed. That is "An unresolved change-request review blocker on an in-scope live-ops PR from that cohort", which "does hold it". The "cosmetic" exemption does not help, because that sentence is the exception to the list before it. #468 also has no approval: its reviews are three COMMENTED and no APPROVED.
- Killed by:
  - Record `github_reviews` harmonygames-Games/match3d#468#rev_3: state `COMMENTED`. It is not a change-request review. The universe has 74 real `CHANGES_REQUESTED` reviews, including #303, the out-of-cohort case the brief describes. None falls after 2025-07-16 in any repo.
  - PR #468 merged at 2025-09-29T16:13:50Z, after the note.
  - The brief has a named place for this item: "anything flagged since this brief as still needed for it (prod deploy, config or player-facing art)".
- Basis: RECORD. Collect & Win stays not held.
- Caution: in rev11 "cosmetic" could also carry this. Now the kill leans on the state field and the plain meaning of "change-request review". The brief does not define that phrase.

**B2. Does the Sep 30 prod update change Collect & Win's start?**
- Reading B: Arthur said "the next backend release", and a backend update reached prod after his comment.
- Killed by: ZOM-563: "That update carried only these, the Collect & Win server windows wait for the Oct 8 release." The gcal title and description name that release independently. Douglas's comment alone would be an owner's claim about his own deploy; the gcal event is what makes this RECORD.

**B3. Is there another reset, now that the shop is carved out?**
- Reading B: listing one exclusion implies other visible resets are in.
- Result: no candidate exists.
  - The CDK stack's schedules are leagues, Plague Race, Endless daily and weekly, Boss Arena daily and weekly, the three Win and Collect groups and Season Pass, plus the daily reward timers and the reward import job. Every player-facing one maps to a named beat or to Boss Arena.
  - A Julia-visible Slack sweep of reset terms found only daily and weekly quest chests (quest rollover), daily login (daily gift) and Endless.
  - Lives recharge is a per-player timer, not a calendar reset.
- A fork needs a concrete Reading B item, and none remains.

**B4. Does "closing 23:59 UTC on its last day" misfire?**
- Clipped windows: Nov 2 23:59 agrees with the clip rule.
- Collect & Win: Fri-Sun closes Sun 23:59, as before.
- A reset read as ending on Monday: a window that resets at Mon 00:00 has Sunday as its last day.
- The gcal "release window": it is not a calendar window, and the brief calls it "instant".
- No misfire found.

**B5. May a reset beat be stated as reset instants, not start-end windows?**
- Reading B: Scope lists "an event window, a reset or a start push" separately, so Endless and Weekly Leaderboard could be stated as Mon 00:00 resets only.
- Killed by: Frederick: "Every beat players can see in those weeks: which windows it runs in"; the brief's exemption lists only the quest rollover, daily gift and Plague Race; and "keeps its usual windows and weeks", which applies to Weekly Leaderboard.
- Basis: RECORD. A cell that gives the Monday starts carries the same schedule, so a rubric should test instants, not layout.

**B6. Does the "fine" parenthetical make "Win & Collect" fine too?**
- Reading B: two loose names pass, so row 8's name passes and only Ready and LIVE are missing.
- Killed by: the parenthetical names two terms and not this one; the brief calls the beat "Collect & Win"; page_liveops_calendar: "Same feature as Win & Collect on Domino Delights, under a different name".
- Basis: RECORD. Row 8 stays Hold either way.

**B7. Does "what its row is missing" change any cell?**
- Reading B: row 15 should add "beat held", and row 8 should add "server windows not live".
- Killed by: "its row". Those are beat facts, not gaps on the row. Row 15 is LIVE only; row 8 is Ready, LIVE and name.
- Row 2 may also quote its own Details text ("Revisit once new quests roll out"). That adds to "Ready" and does not conflict.

**B8. Does "before the beta" set a date for the art?**
- Reading B: the vials and icon are due by Oct 6, or by Oct 10, or by the Trello "BETA: Oct 10" list.
- No sheet column asks for a date on those items. The brief's test is "before it runs". This is not a fork, but a rubric must not lock a date.

**B9. Does "off this calendar until the pivot call" bring Boss Arena back mid-span?**
- No record dates the pivot call, and the calendar is built now: "off this calendar". Basis: RECORD.

## Findings

`DR1 | P1 | deep_recheck both-fair figure | Brief: "the backend release instant read in UTC" | gcal evt_5c1e83a7d94b02f6c8e31a start 2025-10-08 15:00:00+00, end 2025-10-08 16:00:00+00 | Unique Ground Truth | BOTH_FAIR_FIGURE, not a failure; arises only if the sheet states the instant`

No other findings. Checked 45 sentences (prompt 6, message 6, reply 5, brief 28), 14 PNs Beta rows, 16 sheet columns, 10 beats or one-offs, and 10 changed hunks.

## Fork list

- F1: Beat set | Seven beats | Add a Rotating Shop row | Settled by: brief "the shop rotation is not a beat."
- F2: "What is missing", rows 13 and 15 | Status fields only | Also a wrong name | Settled by: brief "(Login Calendar and Weekly Rankings are fine)"
- F3: End instants | 23:59 on the last day | Next reset at 00:00 | Settled by: brief "closing 23:59 UTC on its last day"
- F4: Release instant, if stated | Oct 8 15:00 UTC | Oct 8 16:00 UTC | Both fair: 15:00 or 16:00 UTC, BOTH_FAIR_FIGURE; the rubric must accept either
- F5 (new, closed): Collect & Win held by the vial note | Not held | Held | Settled by: github_reviews #468#rev_3 state `COMMENTED`, and brief "anything flagged since this brief as still needed for it (prod deploy, config or player-facing art)"

## Reading A, updated

**Calendar tab, 7 beats:**

| Beat | Windows and weeks | Status | Push | Still to do (owner) |
|---|---|---|---|---|
| Collect & Win | First window Fri Oct 10 00:00 to Sun Oct 12 23:59 UTC; 10 windows, W1 Fri-Sun only, W2-W4 full | Starts late, not held | Held | Oct 8 prod deploy (Douglas); final vial models (Claire); event icon animation (Marcus) |
| Season Pass | Oct 6 00:00 to Oct 31 23:59; Nov 1 00:00 to Nov 2 23:59; W1-W4 | Running | Held | November config (Brian), moved before Oct 31 00:00 UTC; November strip art (Oliver) |
| Weekly Leaderboard | Mon 00:00 to Sun 23:59, W1-W4 | Held until the fix is confirmed on prod | Held | ZOM-429 fix (Douglas) |
| Endless | Daily 00:00 to 23:59; weekly Mon 00:00 to Sun 23:59; W1-W4 | Running | None | None |
| Plague Race | In, W1-W4, no window dates | Running | Held | None |
| Quest rollover | In, W1-W4, no window dates | Running | Held | None |
| Daily gift | In, W1-W4, no window dates | Running | Held | None |

Off the calendar: Boss Arena, Zombie Lane, Halloween one-off, and the shop rotation is not a beat.

**Pushes tab:** 10 lines. Rows 3, 9, 11 and 12 are left off.

| Row | Item | Answer | What is missing |
|---|---|---|---|
| 2 | Quests | Hold | Ready |
| 4 | Lives recharged | **Send** | None |
| 5 | 1-day lapsed | Hold | Game name |
| 6 | 7-day lapsed | **Send** | None |
| 7 | FTUE | Hold | Game name |
| 8 | Win & Collect | Hold | Ready, LIVE, event name |
| 10 | Plague Race | Hold | LIVE |
| 13 | Login Calendar | Hold | Ready, LIVE |
| 14 | Season Pass | Hold | Ready, LIVE |
| 15 | Weekly Leaderboard | Hold | LIVE |

**Other writes:** ZOM-429 note; sheet link on ZOM-78; reply on Brian's Sep 26 mail; recommendation in the Frederick DM.

## Decisions carried over from rev11

These rest on text and records rev12 did not touch, or only strengthened. All 46 quotes used as kills from the SQL are present in the new file, checked by script.

| Decision | Basis | Kill |
|---|---|---|
| Destinations: sheet, ZOM-78, DM, Zombie Match workbook | RECORD | Frederick: "the calendar sheet in your ZM Live Ops folder"; cmt_zom78_1: "Let us use this ticket"; "send me your recommendation back here"; brief: "names the game as Zombie Match 3D" |
| Thread reply binds | RECORD | "Two things on top of the brief." |
| Weekly Leaderboard held | RECORD | Vincent Sep 30: "my week is still last week one. Same on the second device."; newer than Douglas's Sep 16 "not blocking" |
| Hold stops at the leaderboard | RECORD | Brief: "an unverified one does not"; Leonard: "Could not get it to freeze"; Leonard on quests: "it is good on prod now"; Vincent on daily gift: "claiming works and nothing is lost" |
| Collect & Win first window Oct 10 | RECORD | Brief: "the first window that opens after its server windows are live"; gcal Oct 8 15:00Z |
| Halloween off | RECORD | Robert Sep 30: "pulling my ok. Take it off the beta calendar"; brief: "his later word is the one that counts" |
| Lock Oct 31 00:00 UTC; Brian misses by 7 hours | RECORD | Spec: "locked 24h before each season opens"; calendar page: "The 24h season-pass freeze ... is a process control" |
| Reply goes on the Sep 26 mail | RECORD | Brian: "If the new date is a problem on your side, reply on this mail." |
| Still to do exclusions | RECORD | Brief: "Nothing else goes in"; Brian on ZOM-566 and ZOM-565; Calvin on ZOM-526; Robert: "nothing waits on new themes"; Vincent on lightSweep |
| Vials and icon stay in | RECORD, stronger | rc_38: "need to be in before the beta"; Brian: "does have to land before the beta" |
| Deploy owner Douglas | RECORD, stronger | gcal organizer, Confluence owner table, and now ZOM-563: "Prod has the teams and social changes now" |

## Platform defects

None scored. Rows 7 and 14 carry `[PERSON_NAME_2549]`, an anonymized token that is the source string, not a defect.

Outside P1, for whoever runs P4: the two new brief clauses answer named traps directly, so check them for hint wording. I did not score this.

## What I scanned for this rerun, and limits

- **SQL:** full line diff, every changed statement read, brief text extracted, style runs and Trello JSON verified.
- **GitHub:** all PR #468 reviews and timeline, review states across repos, the CDK schedule list, backend scheduler config.
- **Slack:** a Julia-visible sweep of reset terms since mid-June, and a search for a dated pivot call (none found).
- **Carried from the rev11 pass, not repeated:** the wide scans of Slack, Linear, Trello, Confluence, Gmail, GCal and Drive. The base exports did not change, and rev12's only universe changes are the 10 hunks above.

Limits:

- Images and videos were not viewed.
- "Change-request review" is not defined in the brief. B1 relies on its plain GitHub meaning.
