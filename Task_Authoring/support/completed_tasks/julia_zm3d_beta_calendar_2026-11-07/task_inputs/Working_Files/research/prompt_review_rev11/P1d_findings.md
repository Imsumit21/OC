# P1 deep recheck: Unique Ground Truth and Clarity (rev11)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
SQL read, never run; sha256 1348d287...84e7 matches the setup. R/prev/ and all other forbidden folders were not opened.

## Result

**3 findings, plus 1 harmless both-fair figure.** Checked 45 sentences (prompt 6, Frederick's message 6, thread reply 5, brief 28), all 14 PNs Beta rows, all 16 sheet columns, and 10 beats or one-offs.

The heavy outcomes each come to one answer with a quote: the hold set, Collect & Win's first window, the Send/Hold split, the lock and mail, the Still to do list, and all destinations. The three open items are smaller, but under the setup's standard none has a kill quote:

- **F1 (set membership):** "beat" is never listed, and the daily rotating shop is a reset a player sees.
- **F2 (contents of a cell):** whether "login calendar" and "Weekly Rankings" count as wrong event names.
- **F3 (edge value):** window end instants other than Collect & Win's, 23:59 or the next 00:00.

If the main session cannot quote a kill for F1 or F2, Unique Ground Truth fails. F3 passes only as BOTH_FAIR_FIGURE, and only if condition 2 is accepted.

## Reading A (built from the prompt, Frederick's message and reply, and the brief)

**Calendar tab, 7 beats:**

| Beat | Windows and weeks | Status | Push | Still to do (owner) |
|---|---|---|---|---|
| Collect & Win | First window Fri Oct 10 00:00 to Sun Oct 12 23:59 UTC; 10 windows, W1 Fri-Sun only, W2-W4 full | Starts late, not held | Held | Oct 8 prod deploy (Douglas); final vial models (Claire); event icon animation (Marcus) |
| Season Pass | October season clipped to Oct 6 00:00; November opens Nov 1 00:00, clipped to Nov 2 23:59; W1-W4 | Running | Held | November config (Brian), moved before Oct 31 00:00 UTC; November strip art (Oliver) |
| Weekly Leaderboard | Mon-Sun windows, W1-W4 | Held until the fix is confirmed on prod | Held | ZOM-429 fix (Douglas) |
| Endless | Daily and Monday resets, W1-W4 | Running | None | None |
| Plague Race | In, W1-W4, no window dates | Running | Held | None |
| Quest rollover | In, W1-W4, no window dates | Running | Held | None |
| Daily gift | In, W1-W4, no window dates | Running | Held | None |

Off the calendar: Boss Arena, Zombie Lane, Halloween one-off.

**Pushes tab:** 10 lines, 2 Send (row 4 lives recharged, row 6 seven-day lapse), 8 Hold.

**Other writes:** ZOM-429 note; sheet link on ZOM-78; reply on Brian's Sep 26 mail; recommendation in the Frederick DM.

## Findings

`DR1 | P1 | common_errors §2 "Which items are in the set", §6.1 | Brief: "Every ZM3D beat a player can see in those weeks: an event window, a reset or a start push." Frederick: "Every beat players can see in those weeks" | slack messages/C0880U9751A/2025-06.json ts 1748953118.655379: "these packs are in daily rotation part of the shop. daily rotation means limited amount of content each day"; Linear ZOM-348 (Todo) "Rotating Shop Discount Issues"; Trello ZM ROADMAP, list "BETA: Oct 10": "Shop Inventory Review and Additions" | Unique Ground Truth | 2 if the main session cannot quote a kill; none found`

`DR2 | P1 | common_errors §2 "What gets written" | Brief: "the English copy on that row names the game as Zombie Match 3D and events by their ZM3D names. Anything else is held, with what is missing." | gsheets "Push Notifications Zombie Match" / PNs Beta row 13 body: "Check the login calendar", row 15 headline: "Weekly Rankings Reset!"; brief: "the daily gift (Login Calendar on the push sheet, same beat)" | Unique Ground Truth (Clarity not scored twice) | 2 under the strict standard: a fork in a cell, and not a figure, so BOTH_FAIR cannot apply. Send/Hold does not change`

`DR3 | P1 | deep_recheck Edge values | Brief: "Every window is stated in server time (UTC) as a start-end instant. A PT/PDT rendering of the same instant is fine, a different instant is not." | page_season_pass_spec: "production seasons reset monthly on the 1st at 00:00 UTC"; slack messages/C08R6BF4ENN/2025-06.json ts 1750284719.479869: "Weekly leagues: every monday at 00:00 AM UTC"; page_liveops_calendar: "weekly reset Monday 00:00 UTC"; brief: "closing 23:59 UTC on its last day" (Collect & Win only) | Unique Ground Truth | BOTH_FAIR_FIGURE candidate; condition 2 is arguable, see F3`

## Fork list

**Open**

- **F1: Beat set.** Reading A: seven beats, shop rotation out. Reading B: a Rotating Shop row, because the brief's test is "a reset" a player can see, and Julia-visible records show the shop rotates daily.
  - Attempted kills, none holds:
    - Frederick's Zombie Lane reason ("no window or reset to plan") does not reach it, since the shop does reset.
    - page_liveops_calendar's "single source of truth" table omits the shop, but for ZM3D it also omits Season Pass, quests and the daily gift (its only quest row is Domino's), so it is not a closed list. It is also a fact source, not a rule source.
    - No record gives a UTC reset instant, which makes a row hard to fill. That is an inference, not a kill.
  - Basis: SILENCE.
  - Missing: a rule-source line listing the beats or putting the shop out. My view is that few runs add this row; "B is less likely" does not settle it.
- **F2: "What is missing" on rows 13 and 15.** Reading A: row 13 also lacks the ZM3D name, because the copy says "login calendar" while the team says Daily Gift (ZOM-432, Brian's Jul 18 zombie-design post). Row 15's "Weekly Rankings" may fail the same way. Reading B: the brief's parenthetical accepts Login Calendar as the same beat, and row 15's body says "leaderboard", so only the status fields are missing (Ready and LIVE on row 13, LIVE on row 15).
  - Both rows stay Hold, so only the cell differs.
  - Basis: SILENCE. "Same beat" settles the mapping, not whether the name is wrong.
  - Missing: a line saying whether the login-calendar wording counts as a wrong name.
  - Row 8 is not part of this fork. page_liveops_calendar settles it: "Same feature as Win & Collect on Domino Delights, under a different name".
- **F3: End instants other than Collect & Win.** Reading A: 23:59 close, by analogy with the brief's span and Collect & Win. Reading B: the next reset instant.

  | Window | A | B |
  |---|---|---|
  | October Season Pass end | Oct 31 23:59 | Nov 1 00:00 |
  | Weekly Leaderboard W1-W3 end | Sun 23:59 | Mon 00:00 |
  | Endless weekly W1-W3 end | Sun 23:59 | Mon 00:00 |
  | W4 end, all weekly beats | Nov 2 23:59 | Same; the clip fixes it |

  - Decision, writes and destinations are the same.
  - Basis: SILENCE, made sharper by "a different instant is not".
  - Both fair: X or Y, BOTH_FAIR_FIGURE only if condition 2 holds. The 00:00 values are quoted on records. The 23:59 values for these beats are derived; only the span end and Collect & Win state them. If that fails, F3 stays a UGT finding.
  - The rubric must accept either.

**Harmless both-fair**

- **F4: Release instant, if the sheet states it.** Oct 8 15:00 UTC (start) or 16:00 UTC (end of the release window). Both are on gcal evt_5c1e83a7d94b02f6c8e31a. The first window is Oct 10 under either.
  - Both fair: 15:00 or 16:00 UTC, BOTH_FAIR_FIGURE; the rubric must accept either.

## Decision sweep: every candidate, Reading B and the quote that kills it

All quoted records are persona-reachable unless marked. Rule sources are the prompt, the message, the reply and the brief.

**Destinations**

| # | Decision | Reading B | Basis | Kill quote |
|---|---|---|---|---|
| 1 | Sheet | Domain "LiveOps Event Calendar" | RECORD | Frederick: "the calendar sheet in your ZM Live Ops folder" |
| 2 | Calendar ticket is ZOM-78 | ENG-2240 "Web interface for the liveops calendar" | RECORD | cmt_zom78_1: "Let us use this ticket for the ZM3D beta live-ops calendar" |
| 3 | Recommendation in the DM | Elsewhere | RECORD | Frederick: "send me your recommendation back here" |
| 4 | Workbook is Push Notifications Zombie Match | Domino workbook, which also has PNs Beta | RECORD | Brief: "names the game as Zombie Match 3D"; title. Julia can open both |
| 5 | Thread reply binds | Only the top message counts, giving 14 lines and 0 Send | RECORD | Reply: "Two things on top of the brief." |

**Beat set and scope**

| # | Decision | Reading B | Basis | Kill quote |
|---|---|---|---|---|
| 6 | Leagues and Weekly Leaderboard are one beat | Two rows, because Arthur and Confluence say "leagues" | RECORD | zombie-ops: "Weekly leagues: every monday"; zombie-bugs Jun 27: "leaderboard league changes" |
| 7 | Endless in | Permanent mode, so off like Zombie Lane | RECORD | Brief test "a reset"; Confluence: "resets daily at 00:00 UTC and weekly on Monday 00:00 UTC" |
| 8 | Axe Arena out | In W3, Trello list "Oct 21" | RECORD | Reply: "things that are not in the beta" |
| 9 | Boss Arena, Zombie Lane off, no rows | "Off" rows | RECORD | Brief: "off this calendar"; reply: "keep Zombie Lane off the calendar" |
| 10 | Halloween off | Overlap needs no approval, so it stays | RECORD | Robert Sep 30: "pulling my ok. Take it off the beta calendar"; brief: "his later word is the one that counts" |
| 11 | Lives, lapsed and FTUE rows stay off the Calendar tab | They are beats | RECORD | Reply puts them in Pushes; none is an event window, reset or start push |

**Windows and start**

| # | Decision | Reading B | Basis | Kill quote |
|---|---|---|---|---|
| 12 | Collect & Win starts Oct 10 | Joins Wed-Thu at release (11 windows); runs from Oct 6 (12) | RECORD | Brief: "the first window that opens after its server windows are live"; gcal Oct 8 15:00Z |
| 13 | Collect & Win not held | Not on prod now, so held | RECORD | Brief: "starts late, it is not held" |
| 14 | Collect & Win waits on Oct 8, not a nearer deploy | Douglas's Sep 30 prod deploy was the "next backend release" | RECORD | gcal: "The server windows that are still on the DEV stack go live with this release". The Sep 30 deploy is in a DM Julia cannot see |
| 15 | Season Pass first window Oct 6 | Oct 1 | RECORD | Brief: "Clip anything that starts before" |
| 16 | No window dates for the three beats | Dates, per Frederick's "which windows" | RECORD | Brief: "not its window dates" |
| 17 | Held beat keeps W1-W4 | No weeks while held | RECORD | Brief: "keeps its usual windows on its row, marked held" |

**Hold**

| # | Decision | Reading B | Basis | Kill quote |
|---|---|---|---|---|
| 18 | Weekly Leaderboard held | A reset that needs a restart (ZOM-429 title; Douglas Sep 16 "not blocking") | RECORD | Vincent Sep 30: "I killed the app and reopened it twice... my week is still last week one. Same on the second device." Douglas is the owner, so his claim does not settle it. The retest is newer |
| 19 | Hold does not reach Endless weekly | Endless also has a weekly leaderboard | RECORD | Brief: "an unverified one does not" |
| 20 | Endless not held | Freeze reports (Leonard Sep 21, Leonard's friend, Robert Sep 10) | RECORD | Leonard Sep 29: "Could not get it to freeze"; brief: "even after a restart" |
| 21 | Other Endless bugs do not hold | ZOM-504, 517, 546 | RECORD | Brief: "cosmetic, VFX and performance gaps". ZOM-546 rests on this line, because Owen's retest is an owner claim |
| 22 | Quests not held | ZOM-534 still In Progress | RECORD | Leonard Sep 30: "it is good on prod now" |
| 23 | Daily gift not held | ZOM-556 open | RECORD | Vincent: "claiming works and nothing is lost"; brief: "Wrong counters" |
| 24 | Change-request rule holds nothing | CodeRabbit "Critical" on #468; Arthur rc_38 | RECORD | No CHANGES_REQUESTED review after 2025-07-16 in any repo. #303 is July and merged. #468 reviews are COMMENTED; brief: "cosmetic" |
| 25 | "Cohort" is undefined | Any definition | RECORD | Same result under every definition, so there is no Clarity fork |
| 26 | Hold until is open-ended | Oct 8 | RECORD | Brief: "say that instead of guessing a date". No dated fix exists |
| 27 | Hold note goes on ZOM-429 only | Notes for held pushes or Collect & Win | RECORD | Prompt: "If a beat ends up held"; brief: "Hold a beat only when" |

**Still to do**

| # | Decision | Reading B | Basis | Kill quote |
|---|---|---|---|---|
| 28 | Deploy owner Douglas | Arthur or Owen | RECORD | gcal organizer douglas@; page_live_ops_engine: "Scheduler ... Backend (Douglas)". No record says "owner" in words, and no rival exists |
| 29 | Vial models, Claire | Polish, omit | RECORD | Arthur #468 rc_38: "The final vial models are missing, Claire has those on her list" |
| 30 | Icon animation, Marcus | Polish, omit | RECORD | Brian ZOM-465: "does have to land before the beta" |
| 31 | Config owner Brian | Julia owns event definitions | RECORD | Brian Sep 26: "Same contents, same owner"; brief: "its owner is told" |
| 32 | Strip art, Oliver | Omit | RECORD | Arthur #472 rc_1: "It needs the November range before that season opens, Oliver is taking the date change" |
| 33 | Header and info text out | Include | RECORD | Brian ZOM-566: "do not have to land before the beta" |
| 34 | Token travel out | Include | RECORD | Brian ZOM-526, then Calvin: "Only the Axe Arena travel is left here" |
| 35 | Endless polish and themes out | Include | RECORD | Brian ZOM-565; Robert: "nothing waits on new themes" |
| 36 | lightSweep out | Include, per Vincent's first post | RECORD | Vincent: "nothing has to land for the beta". He is the flagger, not the owner |
| 37 | Daily gift frame out | Include | RECORD | ZOM-432: "nothing is left here"; independently PR #471 commit "Fixing UI Elements on Daily Gift" |
| 38 | More quests out | Include for Oct 13 | RECORD | Leonard's comment is an owner claim, but nobody flagged it as needed, so the brief's inclusion test fails: "anything flagged ... as still needed" |
| 39 | Store approval out | Add for Collect & Win | RECORD | Brief: "Nothing else goes in". Only the Sep 23 UA deck says it, before the brief; Frederick: "the beta buy we start Mon Oct 6" |

**Lock and mail**

| # | Decision | Reading B | Basis | Kill quote |
|---|---|---|---|---|
| 40 | Lock Oct 31 00:00 UTC | No lock exists | RECORD | page_liveops_calendar: "The 24h season-pass freeze ... is a process control on top of that" |
| 41 | Same | "The day before" means all of Oct 31 | RECORD | page_season_pass_spec: "locked 24h before each season opens" |
| 42 | Reply on the Sep 26 mail | Reply on the Sep 22 mail | RECORD | Brian: "If the new date is a problem on your side, reply on this mail." |
| 43 | New date is any instant before the lock | One fixed date | RECORD | Brief: "any time before it". The rubric must accept any such instant |

**Recommendation**

| # | Decision | Reading B | Basis | Kill quote |
|---|---|---|---|---|
| 44 | Covers beats and pushes | Beats only | RECORD | Frederick: "what we hold"; brief uses held for pushes: "Anything else is held" |
| 45 | No new beat holds | A personal call to hold Collect & Win | RECORD | Brief: "Hold a beat only when". The trade-offs are open text, so a rubric must not lock them |

## Push rows

| Row | Item | Status / LIVE | Copy | Answer | What is missing | Basis |
|---|---|---|---|---|---|---|
| 2 | Quests | Not Ready / LIVE | No wrong name | Hold | Ready | RECORD ("as it stands" kills an Oct 13 revisit) |
| 3 | Hourly Coins | n/a | n/a | Left off | n/a | RECORD |
| 4 | Lives recharged | Ready / LIVE | No game name; "ammo" and "energy" are not events | **Send** | None | RECORD (reply) |
| 5 | 1-day lapsed | Ready / LIVE | "Puzzles vs Zombies" | Hold | Game name | RECORD |
| 6 | 7-day lapsed | Ready / LIVE | No game name | **Send** | None | RECORD (reply) |
| 7 | FTUE | Ready / LIVE | "Puzzles vs Zombies" | Hold | Game name | RECORD |
| 8 | Win & Collect | Not Ready / WIP | Wrong event name | Hold | Ready, LIVE, name | RECORD |
| 9 | Nathan's Treasure Hunt | n/a | n/a | Left off | n/a | RECORD |
| 10 | Plague Race | Ready / WIP | Name correct | Hold | LIVE | RECORD |
| 11 | Streak Fever | n/a | n/a | Left off | n/a | RECORD |
| 12 | Axe Arena | n/a | n/a | Left off | n/a | RECORD |
| 13 | Login Calendar | Not Ready / WIP | Open (F2) | Hold | Ready, LIVE, name open | SILENCE on name |
| 14 | Season Pass | Not Ready / WIP | Name correct | Hold | Ready, LIVE | RECORD |
| 15 | Weekly Leaderboard | Ready / WIP | Open (F2) | Hold | LIVE, name open | SILENCE on name |

## Edge values computed

| Value | Edges tried | Result |
|---|---|---|
| Collect & Win first window | Release in UTC, Istanbul, PDT; window start or end | Oct 10 00:00 UTC under all |
| Collect & Win window count | A; joins Wed-Thu; from Oct 6 | 10; 11; 12. Brief picks 10 |
| Lock against Brian | UTC, Istanbul, PDT | Lock Oct 31 00:00 UTC (03:00 Istanbul, Oct 30 17:00 PDT); Brian 07:00 UTC; misses by 7 hours under all |
| Brian's date | Before or after his correction | Oct 29 is clear of the lock; Oct 31 misses. Newer mail applies: "drop the Oct 29 one" |
| Leaderboard | Before or after Sep 30 | Not held; held. Newer record applies |
| Halloween | Before or after Sep 30 | On; off |
| Collect & Win icon | Marcus Sep 26 or Sep 30 | Done; to do |
| Send count | With or without the reply | 2; 0. The reply applies |
| Push lines | Tab as it stands | 14 less 4 = 10 |
| "Since this brief" | Doc created 17:15:22Z, modified 17:40:52Z on Sep 24; ZOM-432 at 16:10Z, ZOM-526 at 17:30Z | Both items closed later, so no cell changes at either edge |
| Borderline statuses | ZOM-534 In Progress, ZOM-563 Done, ZOM-432 Done, ZOM-344 Done | No cell changes |
| End instants | 23:59 or next 00:00 | Changes; open (F3) |

## Platform defects

None scored. Rows 7 and 14 carry `[PERSON_NAME_2549]`, an anonymized token that is the source string, not a defect.

## What I scanned, and limits

- **Slack:** 89,932 messages from Jun 1 to Oct 1 across all exported channels, with SQL rows read separately. I read zombie-match3d (Sep 10-30), zombie-bugs (Sep 19-30), zombie-ops (Jun-Sep), the Julia-Robert and Julia-Frederick DMs, and every SQL-touched thread. Keyword sweeps covered leaderboard, leagues, Season Pass, Collect & Win, Plague Race, daily gift, lock, prod and deploy, Halloween, airstrike, rotating shop, push notifications and beta. A live-ops term sweep covered all other Julia-visible channels since Sep 24. zm-collect-win and Douglas's DMs were read for facts only and used as no kill, because Julia cannot see them.
- **Linear:** 3,687 issues, all open ZOM issues, every issue touched since Sep 23, blocker labels (none open on ZOM), and all 31 injected comments. The base has no comments.
- **GitHub:** 175 match3d PRs since Jul 15, all reviews and change-request states across repos, human comments since Sep 20, open PRs, match3d-backend config and CDK schedules, ZM-Liveops-Docs.
- **Trello:** every ZM ROADMAP card, actions since Sep 10, the injected comment.
- **Confluence:** all 30 pages grepped for lock and freeze terms. Live-Ops Calendar, Live-Ops Engine, Season Pass spec and ZM3D GDD read in full.
- **Gmail:** Julia's 12 messages since Jul 1, plus the injected threads.
- **GCal:** all events by summary keyword, Julia's calendar since Sep 24. No other release event exists.
- **Drive, Docs, Sheets:** Julia-visible files by name since Jun 2025, docs by topic since Apr 2025, both PNs workbooks, the injected brief, deck and calendar sheet.
- **References:** Known issues list (SC-1 to SC-73) checked for this task's facts; none changes a cell.

Limits:

- Images and videos in Slack and Linear were not viewed, so the lightSweep box's beat is not identified. It does not matter under row 36.
- Slack before June was searched only where a thread led back.
- Originality and other dimensions are out of scope for P1.
