# Deep recheck P1: Unique Ground Truth and Clarity

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Blind pass. I did not open R/prev/, R/work/ outside p1h/, other reviewers' files or any task_inputs folder.

## Result

**Findings: none. 46 sentences checked**: 6 in the prompt, 6 in Frederick's message, 5 in his thread reply, 29 in the brief. I also swept 7 beat rows, 14 push rows (10 planned, 4 left off), all 5 writes and 34 fork candidates.

I tried to fail this and could not. Each candidate has a quote that kills Reading B, or an incorporated rule that does. No item came out as SCOPE_GAP or SILENCE. Forks open: 0. BOTH_FAIR_FIGURE: 0.

Five of the kills are thinner than the rest. They are under "Weakest kills" so the main session can re-judge them. W1 is the one that matters: if it is rejected, it is a fail-level fork.

## Reading A (built from the prompt, message, reply and brief)

**Calendar tab, 7 rows**

| Beat | Windows (UTC) | Weeks | Status | Push | Still to do (owner) |
|---|---|---|---|---|---|
| Collect & Win | First: Fri Oct 10 00:00 to Sun Oct 12 23:59. 10 windows: Oct 10-12; 13-14, 15-16, 17-19; 20-21, 22-23, 24-26; 27-28, 29-30; Oct 31-Nov 2 | W1 (partial) to W4 | Starts late, not held | Hold: Not Ready, WIP, wrong event name | Oct 8 15:00 UTC backend release (Douglas); vial final models (Claire); event icon animation (Marcus) |
| Endless | 4 weekly windows, Mon 00:00 to Sun 23:59; daily reset 00:00 UTC noted | W1-W4 | Runs | No row on the tab | Nothing |
| Weekly Leaderboard | Usual 4 weekly windows, same instants | W1-W4 | **Held**, until the fix is confirmed on prod | Hold: WIP | Its fix (Douglas) |
| Season Pass | Oct 6 00:00 to Oct 31 23:59; Nov 1 00:00 to Nov 2 23:59 | W1-W4 | Runs | Hold: Not Ready, WIP | November config before Oct 31 00:00 UTC (Brian); premium strip art, November range (Oliver) |
| Plague Race | No dates, per the brief | W1-W4 | In | Hold: WIP | Nothing |
| Quest rollover | No dates, per the brief | W1-W4 | In | Hold: Not Ready | Nothing |
| Daily gift | No dates, per the brief | W1-W4 | In | Hold: Not Ready, WIP | Nothing |

Off the calendar: Boss Arena, Zombie Lane, rotating shop, Halloween one-off.

**Pushes tab, 10 rows from "Push Notifications Zombie Match"**

- Send (2): lives recharged, 7 Days Lapsed.
- Hold (8):

| Row | What is missing |
|---|---|
| Quests | Ready |
| Plague Race | LIVE |
| Weekly Leaderboard reset | LIVE |
| Login Calendar | Ready, LIVE |
| Season Pass | Ready, LIVE |
| Win & Collect | Ready, LIVE, event name |
| 1 Days Lapsed | Game name ("Puzzles vs Zombies") |
| FTUE | Game name ("Puzzles vs Zombies") |

**Writes**

1. Both tabs of ZM3D Beta Live-Ops Calendar.
2. Note on ZOM-429.
3. Sheet link on ZOM-78.
4. Recommendation to Frederick in DM D05SD5QLG94.
5. Gmail reply on Brian's Sep 26 thread.

## Findings

`DR# | pass | checklist section | quote | record | dimension | score`

None.

## Fork list (all candidates, every basis RECORD)

**Set and hold**

- F1: Beat set | 7 beats | Add Boss Arena, Zombie Lane, shop, Axe Arena, or Pop-up Offers (Trello list "Oct 21" falls inside the span) | Settled by: brief "Boss Arena is off this calendar until the pivot call, and the rotating shop is not a beat."; reply "keep Zombie Lane off the calendar"; reply "things that are not in the beta: Hourly Coins, Nathan's Treasure Hunt, Streak Fever and Axe Arena". Pop-up Offers fails the brief's test ("an event window, a reset or a start push") and has no PN row.
- F2: Leagues and Weekly Leaderboard as two beats | One beat | Two rows | Settled by: match3d#470 rc_10 "The Plague Race, leagues, Endless and Season Pass schedules"; CDK `LEAGUES_SCHEDULE` "PROD: every monday at 00:00 AM UTC"; PN row "Weekly Leaderboard reset".
- F3: Weekly Leaderboard held | Held | Not held: owner said restart works, one tester, a stale reset is a "reset" gap | Settled by: Vincent, #zombie-match3d, Sep 30: "it still does not start a new week. I killed the app and reopened it twice, played a few levels, and my week is still last week one. Same on the second device."; ZOM-429 "doesn't start the new one or let me claim my rewards"; brief "even after a restart". This is newer than Douglas's Sep 16 "they land in the new week fine". See W1.
- F4: Hold until | Until the fix is confirmed on prod | Oct 8 release date | Settled by: brief "A hold with no dated fix runs until the fix is confirmed on prod; say that instead of guessing a date." The GCal description covers only "server windows that are still on the DEV stack".
- F5: Other holds | None | Endless freeze; Aug 29 and Sep 7 refresh failures; quest reset; daily gift; Season Pass premium | Settled by: Leonard's thread "Could not get it to freeze, so I am leaving this one."; Douglas Sep 7 "Solved, try again please"; #470 rc_10 (schedules running on prod, Sep 30); ZOM-534 "That was my report, it is good on prod now."; ZOM-556 "claiming works and nothing is lost"; brief "Wrong counters, a reset that needs a restart ... do not hold a beat". Season Pass has no prod failure on record after the Sep 16 fixes.
- F6: Change-request hold | None | A cohort PR blocker holds a beat | Settled by: full scan. The last CHANGES_REQUESTED reviews are match3d#303 (Jul 16, tooltips) and match3d-backend#4 (June). Nothing in Aug-Sep on any repo, and the only Slack mirror of "changes requested" is #303. See W3.
- F7: Collect & Win status | Starts late | Held until Oct 10 | Settled by: brief "starts late, it is not held."

**Windows**

- F8: Collect & Win first window | Fri Oct 10 00:00 | Wed Oct 8 00:00, or Oct 6 from the client merge | Settled by: brief "the first window that opens after its server windows are live on prod ... not when its client PRs merged"; GCal 2025-10-08T15:00:00Z; ZOM-563 "the Collect & Win server windows wait for the Oct 8 release."
- F9: Season Pass first window | Oct 6 00:00 clipped | Nov 1, as the first season that opens inside the span | Settled by: brief "Clip anything that starts before or runs past that to those two instants."; #470 rc_10 (Season Pass schedule already on prod).
- F10: Weekly Leaderboard windows | Mon 00:00 to Sun 23:59 x4 | Any other cut | Settled by: brief "keeps its usual windows and weeks"; CDK comment quoted in F2. See W5.
- F11: Dates for quests, gift, Plague Race | None | List dates (the Snowflake 5-day Plague runs, the CDK daily cron) | Settled by: brief "not its window dates".

**Still to do**

- F12: Collect & Win items in | Release, vials, icon | Vials and icon out as "not a blocker" or polish | Settled by: #468 rc_38 "still need their final models before the event runs. Not a blocker for this PR"; ZOM-465 Brian "the Collect & Win icon does have to land before the event runs".
- F13: Collect & Win items out | Analytics, title text, token travel, store approval out | Any added | Settled by: brief "not analytics"; ZOM-566 "the header title and the info screen text do not have to land before the beta."; ZOM-526 "does not have to land before the beta"; UA plan "starting once the stores approve the Sep 30 builds" (Sep 23, before the brief, and bought users arrive only after approval); brief "Nothing else goes in".
- F14: Season Pass items | Config and strip art | Strip art out as cosmetic | Settled by: #472 rc_1 "It needs the November range before that season opens, Oliver is taking the date change."; brief "player-facing art".
- F15: Endless items | Nothing | VFX, ZOM-542, new themes | Settled by: ZOM-565 Brian "do not have to land before the beta"; Robert "nothing waits on new themes"; ZOM-542 dates from Sep 22, before the brief.
- F16: Quest items | Nothing | More quests and reward balance for Oct 13 (Trello card 61, still open) | Settled by: brief "anything flagged since this brief as still needed ... Nothing else goes in"; Leonard "The weekly rollover does not wait on them". See W2.
- F17: Daily gift frame | Out | Still to land, because a Done ticket is not the event and the builds are unapproved | Settled by: PR #471 merged; commit 41a0d814ed touches "Sprites/Daily Gift/img - DailyGift.png"; #builds Android #135 lists "Fixing UI Elements on Daily Gift"; UA plan as in F13. Not resting on Samuel's comment alone.
- F18: Plague Race items | Nothing | ZOM-471 red dot | Settled by: closed-list rule. Its only comment is Sep 17, before the brief, and nothing flags it since.
- F19: Owners | Douglas, Claire, Marcus, Brian, Oliver, Douglas | Arthur for the deploy | Settled by: GCal organizer douglas@harmonygames.co; ZOM-563 Douglas; ZOM-429 assignee; the quotes in F12 and F14.

**Config lock and mail**

- F20: Lock instant | Oct 31 00:00 UTC, Brian misses | Whole day of Oct 31, or no real lock, so Brian is fine and no reply | Settled by: Season Pass spec "locked 24h before each season opens"; Live-Ops Calendar "The 24h season-pass freeze in the Season Pass spec is a process control"; brief "before its lock, read in server time (UTC)".
- F21: Brian's date and thread | Oct 31 10:00 Istanbul, Sep 26 thread | Oct 29, Sep 22 thread | Settled by: Brian "Treat Fri Oct 31 as the date I am committing to and drop the Oct 29 one."; "reply on this mail."
- F22: Reply is a required write | Send | Not in the prompt's list, so skip it | Settled by: prompt "Can you take it on for me?" and "his working rules for building it are in the brief"; brief "you tell its owner in a reply on the mail where they committed to it." See W4.

**Pushes**

- F23: Which sheet | Zombie Match | Domino Adventure, which also has a "PNs Beta" tab | Settled by: brief "Ready and LIVE" (only the Zombie Match tab has a Ready column); reply's four row names; brief "the translated tab is the old Domino set".
- F24: Rows | 10 | 14, or also dropping non-event rows | Settled by: reply "one line per row, local notifications included", "just those four".
- F25: Copy with no game name | Sends if Ready and LIVE | Held, or Quests sends | Settled by: reply "Copy that does not name the game at all is fine to go out, the naming rule is only about wrong names." The reply scopes the naming rule only, so the Ready and LIVE gate stands.
- F26: "Win & Collect" | Wrong event name, 3 items missing | Team also says Win & Collect (PR #472, Leonard, Julia), so 2 items | Settled by: Live-Ops Calendar "Same feature as Win & Collect on Domino Delights, under a different name"; brief "Collect & Win runs". Send or hold is unchanged either way.
- F27: "Puzzles vs Zombies" | Wrong game name | Legacy name allowed | Settled by: brief "names the game as Zombie Match 3D"; Engine page "until the July 2025 store rename".
- F28: Missing cell for the held beat's push | LIVE only | Add the beat hold | Settled by: brief "with which of those its row is missing".

**One-off, destinations, recommendation**

- F29: Halloween | Off | Stays as an overlap needing no approval, or Product is someone else | Settled by: Robert DM Sep 30 "pulling my ok. Take it off the beta calendar"; brief "his later word is the one that counts"; Confluence "Owner: Robert (Product)".
- F30: Ticket note | ZOM-429 only | Also on held pushes or late beats | Settled by: prompt "If a beat ends up held"; the brief separates push holds from beat holds, and only one beat is held.
- F31: Calendar ticket | ZOM-78 | ENG-2240 or a new ticket | Settled by: Frederick on ZOM-78 "Let us use this ticket for the ZM3D beta live-ops calendar instead of opening a new one."
- F32: Sheet | ZM3D Beta Live-Ops Calendar | LiveOps Event Calendar or a new sheet | Settled by: Frederick "the calendar sheet in your ZM Live Ops folder".
- F33: Recommendation channel | Frederick's DM | Mail | Settled by: "send me your recommendation back here". Top level or in thread is the same recipient, so a 3 at most under §2.6, not a fork.
- F34: Recommendation call | Run all but Weekly Leaderboard, Collect & Win from Oct 10 | Hold Collect & Win until art lands | Settled by: brief "Hold a beat only when players provably cannot enter, score or claim". Trade-offs stay open, inside that boundary.

## Edge values

| Item | Edges tried | Result |
|---|---|---|
| Release vs Wed window | 15:00 or 16:00 UTC; Oct 8 08:00 PDT; Wed window opens Tue 17:00 PDT | Wed window opens before the release in every zone, so Fri Oct 10 |
| Collect & Win window count | Include Wed Oct 8 / exclude | 11 / **10** (W1 1, W2-W4 3 each); the rule excludes it |
| Lock | Nov 1 00:00 UTC minus 24h | Oct 31 00:00 UTC = Oct 30 17:00 PDT = Oct 31 03:00 Istanbul |
| Brian's date | 10:00 Istanbul | 07:00 UTC = Oct 31 00:00 PDT; misses by 7h in every zone. The withdrawn Oct 29 would have met it |
| Span end | DST ends Nov 2 | Nov 2 23:59 UTC = 15:59 PST; same instant, accepted |
| Pushes, before and after the reply | Brief alone / with the reply | Send 0 / **2**; the later word applies |
| Pushes, row count | Before and after leaving off rows | 14 / **10** |
| "Since this brief" | Sep 24 16:10Z (ZOM-432), 15:20Z (ZOM-556), 17:30Z (ZOM-526), brief 17:15Z to 17:40Z | Each later closed or settled, so no cell changes |
| Later corrections | Oct 29 to Oct 31; Robert ok to pulled; ZOM-465 c1 to c2; Douglas to Vincent | Newest wins in all four |
| Borderline statuses | ZOM-534 In Progress, ZOM-566 In Progress, ZOM-429 Backlog, ZOM-432 Done | No cell rests on status alone |

## Weakest kills, for the main session to re-judge

- **W1 (F3), the only one that would fail the task.** Vincent never uses the brief's verbs. I read "does not start a new week" plus ZOM-429's "or let me claim my rewards" as direct, not as an inference: a week that never starts cannot be entered, and restart is tested twice on two devices. "Established" is undefined; the newest-source check and the two-device retest carry it. If this is rejected, the fork flips Status, the ZOM-429 write and the recommendation. The defect would be that the retest does not state that the player could not join, score or claim in the new week.
- **W2 (F16).** The fact leg, "does not wait on them", is the card co-owner's own comment. The kill does not rest on it: the brief needs a post-brief flag "as still needed", and none exists. Card 61 is still open on the BETA list, so a stricter reader may press this.
- **W3 (F6).** "Aug-Sep live-ops cohort" is defined nowhere in the records I searched. It changes nothing, because every reading finds zero change requests. CodeRabbit "Critical" comments are review state COMMENTED, not change requests.
- **W4 (F22).** The Brian reply is the one write the prompt does not list. Only the brief carries it.
- **W5 (F10).** The leaderboard's weekly cut is stated only in the CDK file, not in the brief or Confluence. It is reachable through `github_get_file_contents`.

## Limits on the rubric and Oracle Events

- The new config date is "any time before" the lock, so a row cannot fix one date.
- Strip art needs-by is "before that season opens", not the lock.
- PT renderings of the same instant are valid.
- Quest, gift and Plague Race rows must not require window dates.

## Platform defects

PLATFORM: anonymized tokens in the push copy ([PERSON_NAME_2549], [PERSON_NAME_16313]) are the source strings. Not scored.

Known-issue cards near the task, with no cell depending on any of them:

- SC-13: the injected Trello action says list "BETA: Sep 30", the list table says "BETA: Oct 10".
- SC-15, SC-16, SC-18, SC-38, SC-47.
- SC-57: Douglas's injected reply sits in #zm-collect-win, which Julia cannot see.

## What I scanned

- **Slack:** 204,413 messages from 2025, filtered to Julia's 147 channels. Read in full: zombie-bugs Sep 21-30, zombie-match3d Sep 23-30, zombie-ops Aug 1 to Sep 15, zombie-art and zm-animations Sep 24-30, the Frederick DM tail, the SQL-touched threads. Skimmed zombie-design Sep 24-30 at line level. Keyword scans for the rest, including all her DMs and MPDMs. #zm-collect-win read as context only.
- **Linear:** all ZOM issues from 420 up, all 43 open issues on live-ops keywords, ticket searches for "calendar", all 32 injected comment lines.
- **GitHub:** match3d PRs #339-477, all non-match3d PRs since mid June, all reviews, timeline events, and human review and PR comments since Jul 25. Commit logs, backend `runtime.exs` and the CDK stack, ZM-Liveops-Docs.
- **Trello:** ZM ROADMAP, all lists and cards, 122 actions since Sep 10.
- **Confluence:** 30 pages (5 read in full, the rest by keyword), 12 comments.
- **Gmail:** all 253 threads in Julia's mailbox; only 2 base messages since Aug 15, plus Brian's two injected threads.
- **Drive and Docs:** 53,631 file records filtered to Julia's view, 595 docs by title, specs for schedule lines.
- **Sheets:** titles of all 356; full PNs Beta tabs in both push sheets.
- **GCal:** Julia's events.
- **Snowflake:** LIVE_EVENT_PERFORMANCE (529 rows), ZM3D push stats, event names. No ZM3D leaderboard rows, so nothing contradicts the hold.

**Not read:** the Slack canvases (Bug_Checklist, Season_Pass_Issues), images and videos; the diff for PR #477's "title change". The in-game Collect & Win header text could not be confirmed from the prefabs. No cell rests on any of these, and ZOM-566 says the title need not land.
