# P1c findings: Unique Ground Truth and Clarity (third independent sample, emphasis outside Slack)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Pass: P1. SQL sha256 as supplied (ffbac458...bdc), read as overlay, never run. Blind to all other reviewers.

## Summary

- 5 findings. 2 are UGT forks with no killing quote (DR2, DR3). 3 are one-figure forks that look like BOTH_FAIR_FIGURE candidates (DR1, DR4, DR5); each stays a UGT finding if the rubric locks one value.
- The core decisions held up under every edge I computed: the 7-beat set, Weekly Leaderboard as the only held beat, Collect & Win first window Fri Oct 10 00:00 UTC, 10 push lines with 2 Send and 8 Hold, lock Oct 31 00:00 UTC against Brian's Oct 31 07:00 UTC, and every write destination (ZOM-429, ZOM-78, the DM, the Sep 26 mail).
- The forks are all in cell contents, not in the decision, writes or destinations. Under the grading standard (contents differ, no quote) DR2 and DR3 still count as open.

## Findings

Format: DR# | pass | checklist section | quoted sentence | record path, id and quoted value | Eval dimension or issue type | proposed score or severity

DR1 | P1 | §2 Which number or date; deep_recheck Edge values | Brief, "When a beat starts": "A beat starts with the first window that opens after its server windows are live on prod ... Season Pass seasons open on the 1st at 00:00 UTC." and "Span and time base": "The calendar covers Mon Oct 6 00:00 UTC to Sun Nov 2 23:59 UTC" | github match3d#470#rc_10 (SQL): "The Plague Race, leagues, Endless and Season Pass schedules are already running on prod."; Confluence page_season_pass_spec: "production seasons reset monthly on the 1st at 00:00 UTC"; Snowflake LIVE_OPS.EVENTS.LIVE_EVENT_PERFORMANCE EVT-0527 Season Pass 2025-09-29 to 2025-09-30; sheet header "First window (UTC)" | Unique Ground Truth, basis SILENCE | BOTH_FAIR_FIGURE candidate: Wed Oct 1 00:00 UTC or Sat Nov 1 00:00 UTC (Mon Oct 6 00:00 UTC is the span-clipped spelling of the first). UGT 2 if the rubric locks one.

DR2 | P1 | §2 What gets written; Contents | Frederick DM: "which windows it runs in, if anything is held and until when"; Brief: "Every window is stated in server time (UTC) as a start-end instant." and "A hold with no dated fix runs until the fix is confirmed on prod; say that instead of guessing a date." | gsheets f_e4a17c90b3d25f6a8c1d73 Calendar header "First window (UTC)","Windows (UTC)","Weeks running","Status","Hold until (UTC)"; match3d-backend zombies-game-cdk-stack.ts "LEAGUES_SCHEDULE: props.production ? \"0 0 * * 1\""; Slack #zombie-match3d b5f2955c... (SQL): "it still does not start a new week" | Unique Ground Truth, basis SILENCE | 2. Three cells on the held Weekly Leaderboard row have two defensible fillings, so it misses the one-figure both-fair test.

DR3 | P1 | §2 Which items are in the set; Contents | Brief, "Push copy": "the English copy on that row names the game as Zombie Match 3D and events by their ZM3D names. Anything else is held, with what is missing." and "the daily gift (the Login Calendar row on the push sheet)"; Frederick reply: "the naming rule is only about wrong names" | gsheets f_a325dd4af80afc5994d5dc PNs Beta row 13 body: "Check the login calendar — fresh rewards are here!"; row 2 Details: "Revisit once new quests roll out."; match3d Assets/Scripts/UI/Daily Gift/DailyGiftProgressBar.cs:180 string "Daily Gift"; Trello 6851a7635cdbb7ca38654da8 "[Feature] Daily Login" | Unique Ground Truth, basis SCOPE_GAP | 2. Row 13 is Hold either way; the "What is missing" set differs. "Superset" is not a ground to reject.

DR4 | P1 | §2 Which number or date | Brief, "Config locks": "A committed date that misses the lock moves earlier and its owner is told in a reply on the mail where they committed to it." | Confluence page_season_pass_spec: "locked 24h before each season opens"; Gmail julia.lawson@harmonygames.co/1844311412966040123 (SQL): "moves from Wed Oct 29 to Fri Oct 31, 10:00 Istanbul time" and "drop the Oct 29 one"; Gmail julia.lawson@harmonygames.co/1843954828968533812 (SQL): "The config handoff we agreed with Product is for Wed Oct 29" | Unique Ground Truth, basis SILENCE | BOTH_FAIR_FIGURE candidate: any instant before Fri Oct 31 00:00 UTC (Thu Oct 30 end of day, or Wed Oct 29). UGT 2 if the rubric locks one date.

DR5 | P1 | Deep_recheck Edge values | Brief: "Every window is stated in server time (UTC) as a start-end instant. A PT/PDT rendering of the same instant is fine, a different instant is not." | Brief span style "Sun Nov 2 23:59 UTC"; match3d-backend config/runtime.exs:215 "Wednesday midnight (end of Tuesday)"; Confluence page_season_pass_spec "reset monthly on the 1st"; span end Nov 2 vs November season end Nov 30 | Unique Ground Truth, basis SILENCE | BOTH_FAIR_FIGURE candidate, low: window end Tue 23:59 or Wed 00:00 UTC; November season end Nov 2 23:59 (clipped) or Nov 30 23:59 UTC. The brief's "a different instant is not" makes a locked end instant unsafe.

## Fork list

- F1: Season Pass First window | A: Wed Oct 1 00:00 UTC (first "1st" after the schedules were on prod; the October season spans W1-W4) | B: Sat Nov 1 00:00 UTC (first season that opens inside the span) | Both fair: Oct 1 or Nov 1, BOTH_FAIR_FIGURE. The literal rule favours A, but the same literal rule gives a pre-span date for Endless and the leaderboard, so it cannot be applied literally to already-live beats and does not kill B.
- F2: Weekly Leaderboard First window, Windows, Weeks running | A: none until the fix is confirmed | B: Mon Oct 6 00:00 UTC, weekly Mon 00:00 to Sun 23:59 x4, W1-W4, all under the open hold | Missing: a sentence in the brief or thread saying what those three cells hold for a beat held with no dated fix. "say that instead of guessing a date" kills only a guessed resume date.
- F3: Pushes "What is missing", row 13 (and rows 2, 15) | A: row 13 Ready + LIVE + rename "login calendar" to daily gift | B: row 13 Ready + LIVE only, since the brief itself uses "Login Calendar" for that row | Missing: a record saying whether "login calendar" is a wrong event name. Rows 2 and 15 have the same additive shape: row 2 Ready vs Ready plus "Revisit once new quests roll out"; row 15 LIVE vs LIVE plus the held beat.
- F4: Brian's moved date | A: before Fri Oct 31 00:00 UTC | B: back to Wed Oct 29 | Both fair: any instant before the lock, BOTH_FAIR_FIGURE. The rubric must check "before Oct 31 00:00 UTC", not a date.
- F5: Window end instants | A: 23:59 of the last day | B: 00:00 of the next day; November season ends Nov 2 (clipped) vs Nov 30 | Both fair, BOTH_FAIR_FIGURE.

## Calendar tab, every beat by column

Span Mon Oct 6 00:00 UTC to Sun Nov 2 23:59 UTC. W1 Oct 6-12, W2 Oct 13-19, W3 Oct 20-26, W4 Oct 27-Nov 2 (deck slide 2). All weekdays checked. Istanbul is UTC+3 on both dates used.

**Collect & Win**

| Column | Reading A | Reading B | Kill | Basis |
|---|---|---|---|---|
| First window | Fri Oct 10 00:00 UTC (Thu Oct 9 17:00 PDT) | Wed Oct 8 00:00 or Oct 8 15:00 UTC, because the Wed-Thu window is open at release (GCal evt_5c1e83a7d94b02f6c8e31a, 15:00-16:00 UTC) | Brief: "the first window that opens after its server windows are live on prod". Start or end of the release slot gives the same answer. | RECORD |
| Windows | 10: Oct 10-12; 13-14, 15-16, 17-19; 20-21, 22-23, 24-26; 27-28, 29-30, Oct 31-Nov 2 | End-instant variants | None, see F5 | SILENCE, both fair |
| Weeks running | W1 (Fri-Sun only) to W4 | W2-W4 | Deck slide 2 "W1 Mon Oct 6 - Sun Oct 12" holds Oct 10 | RECORD |
| Status | Starts late, not held | Held until release | Brief: "starts late, it is not held" | RECORD |
| Hold until | Blank | Oct 8 or Oct 10 | Same quote | RECORD |
| Push | Held | Send | PNs Beta row 8 Not Ready, WIP, "Win & Collect" | RECORD |
| Still to do | Prod release Oct 8 (Douglas); final vial models (Claire); event icon animation (Marcus) | Omit icon as polish | Brief: "anything flagged since this brief as still needed ... (prod deploy, config or player-facing art)" and "not polish nobody flagged"; cmt_zom465_2: "The Collect & Win event icon animation is still to do on my side"; ZOM-465 description: "For all event icons we some need slight animations at the idle." | RECORD, thin wording |

**Season Pass**

| Column | Reading A | Reading B | Kill | Basis |
|---|---|---|---|---|
| First window | Oct 1 00:00 UTC | Nov 1 00:00 UTC, or Oct 6 clipped | None, see F1 | SILENCE |
| Windows | October season to Oct 31 23:59; November season from Nov 1 00:00 UTC | November end Nov 2 vs Nov 30 | None, see F5 | SILENCE, both fair |
| Weeks running | W1-W4 | W4 only (November season alone) | match3d#470#rc_10 "already running on prod"; match3d#472#rc_1 "still set to the October range" | RECORD |
| Status | Running | Held for config | Brief test is "cannot enter, score or claim" | RECORD |
| Hold until | Blank | Lock date | Same | RECORD |
| Push | Held | Send | Row 14 Not Ready, WIP | RECORD |
| Still to do | November config (Brian), moved before Oct 31 00:00 UTC; premium strip November range (Oliver) | Keep Brian's Oct 31 07:00 UTC; or add ZOM-552 | Brief: "moves earlier"; "not analytics". Lock: 24h before Nov 1 00:00 UTC = Oct 31 00:00 UTC; miss is 7h. "Day before" in the spec's Rollout line is killed by "locked 24h before". | RECORD. New date: F4 |

No date is required for the strip. If one is stated, "before that season opens" (Nov 1) and the config lock (Oct 31) are both arguable, so a row must not lock it.

**Weekly Leaderboard (leagues)**

| Column | Reading A | Reading B | Kill | Basis |
|---|---|---|---|---|
| First window, Windows, Weeks running | None until fix | Oct 6, weekly x4, W1-W4 under hold | None, see F2 | SILENCE |
| Status | Held | Not held: Douglas found restart works, so "a reset that needs a restart" | Vincent, Sep 30 (SQL, b5f2955c...): "I killed the app and reopened it twice, played a few levels, and my week is still last week one. Same on the second device." Douglas is the assignee, so cmt_zom429_1 is an owner's claim and does not settle it. ZOM-429 description: "doesn't start the new one or let me claim my rewards" | RECORD |
| Hold until | Until the fix is confirmed on prod | Oct 8 release | Brief: "say that instead of guessing a date"; GCal description covers only "server windows that are still on the DEV stack" | RECORD |
| Push | Held | | Row 15 Ready but WIP | RECORD |
| Still to do | Fix (Douglas, ZOM-429 assignee) | | Brief: "its fix if it is held" | RECORD |

**Endless**

| Column | Reading A | Reading B | Kill | Basis |
|---|---|---|---|---|
| In scope | In | Out as a permanent mode, like Zombie Lane | Frederick: Zombie Lane is off for having "no window or reset to plan"; Confluence page_liveops_calendar: "daily reset 00:00 UTC, weekly reset Monday 00:00 UTC" | RECORD |
| First window | Mon Oct 6 00:00 UTC | | Same page | RECORD |
| Windows | 4 weekly, Mon 00:00-Sun 23:59, plus daily 00:00 reset | Daily only | Both true together, cell holds both | RECORD |
| Weeks running | W1-W4 | | | RECORD |
| Status, Hold until | Running, blank | Held on the airstrike freeze | Slack e343557b... (SQL): "Could not get it to freeze, so I am leaving this one."; brief: "an unverified one does not" | RECORD |
| Push | None, no PNs Beta row | Row 15 | Row 15 Details: "Weekly Leaderboard reset" | RECORD |
| Still to do | None | ZOM-565 VFX, refill timer, desert or port theme | cmt_zom565_2 (Brian, list owner): "do not have to land before the beta"; Slack 532747cb... (Robert): "nothing waits on new themes" | RECORD |

**Plague Race, quest rollover, daily gift**

| Column | Reading A | Reading B | Kill | Basis |
|---|---|---|---|---|
| First window, Windows | Not stated, all three | State dates (Plague Race has daily cron in CDK, 5-day runs in Snowflake) | Brief: "not its window dates". This also removes that source conflict. | RECORD |
| Weeks running | W1-W4, all three | Quests from W2 (Oct 13) | Trello 68dac8204f1e9a3b7c2d5e61: "The weekly rollover does not wait on them, the current quests keep running either way." Brief rule, not only Leonard's word: "flagged ... as still needed" | RECORD |
| Status, Hold until | In, blank | Daily gift held on ZOM-556; quests on ZOM-534 | cmt_zom556_1 (Vincent): "claiming works and nothing is lost"; brief "Wrong counters"; cmt_zom534_2 (Leonard, the reporter): "it is good on prod now" | RECORD |
| Push | All held | | Rows 10, 2, 13 | RECORD |
| Still to do | None | ZOM-471 red dot; more quests; ZOM-432 frame | ZOM-471 and its note predate the brief; Trello as above; cmt_zom432_2 with PR #471 ("updated Daily Gift sprite configuration") | RECORD |

**Beat set.** Seven beats. Out by quote: Boss Arena ("off this calendar until the pivot call"), Zombie Lane (Frederick), Halloween one-off (Robert Sep 30: "Take it off the beta calendar"), Axe Arena, Treasure Hunt, Streak Fever, Hourly Coins ("not in the beta"; this also kills Trello's "Oct 21" Axe Arena card). Pop-up Offers and Rewarded Ads (Trello Oct 21) fail the scope line "an event window, a reset or a start push". Rotating shop or Daily Offers reset: page_liveops_calendar calls itself "the single source of truth for what live-ops events are scheduled" and has no shop row. RECORD.

## Pushes tab, row by row

14 data rows in PNs Beta, 4 left off (rows 3, 9, 11, 12), 10 lines. Every Segment is copied from Segmentation; Reading B "UK and US" is killed by "plan the PNs Beta tab as it stands". English copy stays as written, same quote.

| Row | Status / LIVE | Send (UTC or trigger) | Segment | Copy check | Send or hold | What is missing |
|---|---|---|---|---|---|---|
| 2 Quests | Not Ready / LIVE | Rollover | Everyone | No name issue | Hold | Ready (F3: plus revisit note) |
| 4 Lives | Ready / LIVE | When lives are recharged | Everyone | No game name, allowed | Send | |
| 5 1-day lapsed | Ready / LIVE | 24h lapse | 24 hours lapse since last session | "Puzzles vs Zombies" wrong | Hold | Game name |
| 6 7-day lapsed | Ready / LIVE | 7d lapse | 7d lapse since last session | No game name, allowed | Send | |
| 7 FTUE | Ready / LIVE | D0-1 | Level 20 not completed and it's been 12 hours since first session | "Puzzles vs Zombies" wrong | Hold | Game name |
| 8 Collect & Win | Not Ready / WIP | Event Start, Fri Oct 10 00:00 UTC | Everyone | "Win & Collect" wrong | Hold | Ready, LIVE, name |
| 10 Plague Race | Ready / WIP | Event Start | Everyone | OK | Hold | LIVE |
| 13 Login Calendar | Not Ready / WIP | Daily/Monthly Rollover | Everyone | "login calendar" | Hold | Ready, LIVE (F3: name) |
| 14 Season Pass | Not Ready / WIP | Season Start or Milestone, Nov 1 00:00 UTC | Everyone | OK | Hold | Ready, LIVE |
| 15 Weekly Leaderboard | Ready / WIP | Weekly Rollover, Mon 00:00 UTC | Everyone | OK | Hold | LIVE (F3: beat held) |

Send or hold has one answer on all 10 rows; rows 4 and 6 are kept by "Copy that does not name the game at all is fine to go out". No row is Ready, LIVE and correctly named while its beat is held, so the two rules never collide.

Send on held rows 8, 14, 15: trigger text and a computed UTC instant are both allowed by the header "UTC or trigger", and row 8 can read as first window only or every window open. Not a fork, but a row must not lock one.

## Writes

| Outcome | Reading A | Reading B | Kill | Basis |
|---|---|---|---|---|
| Sheet | f_e4a17c90b3d25f6a8c1d73 in ZM Live Ops | Base "LiveOps Event Calendar" or "Live Ops Planning" | Frederick: "the calendar sheet in your ZM Live Ops folder" | RECORD |
| Calendar ticket | ZOM-78 | ENG-2240 | cmt_zom78_1: "Link the sheet here when it is ready." | RECORD |
| Held note | ZOM-429 only | Also a note for Collect & Win or for pushes | Prompt: "If a beat ends up held"; brief "starts late, it is not held" | RECORD |
| Recommendation | DM D05SD5QLG94 | | Frederick: "back here" | RECORD |
| Reply to Brian | Sent, on the Sep 26 mail | Not sent, because the prompt lists only three writes; or sent on the Sep 22 mail | Prompt: "Can you take it on for me?" and "his working rules for building it are in the brief"; brief: "its owner is told in a reply on the mail where they committed to it"; Sep 26 mail: "reply on this mail" | RECORD |

## Decision sweep outside Slack

**Open ZOM tickets post-SQL: 96 of 553, one by one.** SQL closes ZOM-432, ZOM-344 and ZOM-563 and moves ZOM-566 to In Progress.

| Tickets | Result | Basis |
|---|---|---|
| 78 | Calendar ticket | RECORD |
| 429 | Held beat | RECORD |
| 534, 556 | Not held, see above | RECORD |
| 465 | Icon in Still to do; refill timer out (cmt_zom565_2) | RECORD |
| 526, 521 | Out: cmt_zom526_3 "Only the Axe Arena travel is left here"; #472 merged | RECORD |
| 543 | Out: #472 merged, Trello card complete | RECORD |
| 565 | Out, Brian | RECORD |
| 566, 552, 442, 549, 387, 441, 439, 400, 386 | Out: "not analytics". Title text in #477: cmt_zom566_1 "do not have to land before the beta" | RECORD |
| 548, 562 | Boss Arena, off | RECORD |
| 390, 62 | Axe Arena or its zombie version, not in the beta | RECORD |
| 471, 542 | Out: both notes predate the brief, so "since this brief" excludes them. The notes themselves are owner claims and not relied on. | RECORD (rule) |
| 484 | Only Axe Arena unticked | RECORD |
| 504, 517, 546 | Endless bugs: visual or not reproduced, and none is cannot enter, score or claim. Owen's note on 546 is an owner claim; the rule excludes it without it. | RECORD (rule) |
| 475, 554, 559, 505, 535, 438, 443, 481, 477, 482, 483, 520, 560, 564, 458, 449, 468, 359, 427, 348 | Core or shop bugs, not tied to a beat. 475: SC-8 says do not grade its fix status; nothing here depends on it, since a crash is not "even after a restart". 559: "Doesn't happen to me", unverified. | RECORD (rule) |
| 16, 48, 56, 64, 65, 66, 69, 70, 73, 76, 97, 104, 118, 119, 121, 122, 130, 137, 147, 148, 150, 151, 155, 168, 171, 181, 182, 184, 202, 236, 237, 243, 255, 292, 293, 311, 317, 342, 453, 467, 508, 513, 514, 528, 539, 541, 544, 545 | Art, VFX, tooling, marketing or backlog with no beat | RECORD (rule) |

**PRs.** Open: match3d#476 (Vision bot, no beat), match3d#477 (analytics and title, bot COMMENTED only), match3d-backend#34 (Endless mix real players, no review), liveops#5 and #10 (2024, Domino). Human notes: #468 rc_38, #470 rc_10, #472 rc_1 (all used above), Owen's two replies on #470, and #336, #390, #395 (no live-ops effect). Change requests: none in Aug-Sep in any ZM3D repo. Last ones are match3d#303 (Jul 16, bot, tooltips, later approved) and match3d-backend#4 (June). So the brief's change-request hold rule matches nothing under any reading of "Aug-Sep live-ops cohort". #477's bot "Critical" note is state COMMENTED and analytics.

**Trello ZM ROADMAP.** All cards on the three live lists read: BETA 18, Oct 21 8, Backlog 9. Older lists are all complete; 10 closed cards checked. Only "Add more quests" and "Axe Arena" touch a cell, both killed above. "Minor Bugs to Fix" items map to the tickets above. Trello's other boards: nothing on ZM3D live-ops.

**Julia's mail.** 253 threads, 304 base messages: nothing on the beats after Aug 2025. The two Brian mails (SQL) are the only commitments. No other config commitment in her mailbox.

**Julia's calendar.** 748 events; last base event Sep 29. Only the SQL release event sits in the span. No conflicting release date anywhere reachable.

**Confluence.** 30 pages and 12 comments. Read in full: Live-Ops Calendar, Season Pass Spec, ZM3D GDD, Event Engine, QA Runbook, Quest Postmortem, Release Checklist, API Reference, Ops Home; the rest searched for beat terms. "There is no technical content lock" does not undo the lock: the same page keeps "The 24h season-pass freeze ... is a process control". Brief's rule reads "its lock".

**Sheets and Drive.** PNs Beta all rows and columns, PNs, PN BETA Translated, Deep Links; Domino sheet compared (row 13 copy is inherited from it unchanged). Calendar sheet headers tested above. Other Julia-visible calendar sheets are stale and killed by Frederick's folder quote.

**Other.** Backend CDK schedules confirm leagues Monday 00:00 UTC, Plague Race daily, Season Pass on the 1st, Collect & Win groups. ZM-Liveops-Docs read. Snowflake LIVE_EVENT_PERFORMANCE 529 rows, 21 ZM3D.

## Non-cell notes

- Deck slides 2 and 3 disagree on scale: "scaled up week by week if the cohorts hold" vs "hold the spend there until the pivot call". No cell reads it. A recommendation may cite either, so no row should grade it. Basis SILENCE.
- The run or hold list in the recommendation has one answer; "trade-offs" is open, so rows should check the list, not the wording.
- zm-collect-win (public, archived, Julia not a member): Brian Sep 26 asks Douglas to update two reward tables, no reply. Nothing in a member channel repeats it. No effect unless that channel counts as visible; I did not rely on it.

## Platform and known-issue notes

- Platform: anonymized token `[PERSON_NAME_2549]` in rows 7 and 14 English copy is the source string. Not scored.
- SC-13: SQL Trello action says list "BETA: Sep 30" while the list is "BETA: Oct 10"; no cell reads it.
- SC-15: SQL repairs the ZOM-521 checklist; the answer uses child ZOM-526. SC-18: #477 state not relied on. SC-38: F1 does not rely on the Season Pass ship date. SC-62: cadence not used.

## Coverage

Checked: 6 prompt sentences, Frederick's message and reply, and all 8 brief sections checked. 6 required outcomes (Calendar tab, Pushes tab, ZOM-429 note, ZOM-78 link, DM, Brian reply). 49 calendar cells, 50 push cells, 96 tickets, 35 Trello cards, 5 open PRs.
Slack was read only as needed to test a non-Slack item (DMs, the four SQL-touched threads, beat-name and failure searches from Sep 12).
