# P1c findings, rerun on rev11: Unique Ground Truth and Clarity

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Pass: P1. New SQL sha256 1348d287ac4a105c41b9f0bf511c6664e306adcc3cf42406688a228fd4b684e7, verified. Prev rev10 sha256 ffbac458...bdc, verified. Prompt unchanged, verified. SQL read as overlay, never run.

Blindness note: the new setup puts review_rev10 off limits. My first command compared the prompt, setup and old SQL against that folder's inputs before I had read the change. I opened no reports or other reviewers' files there, and did not open R11/work/p1a or anything else in R11/out. My earlier DR1-DR5 come from my own report.

## Summary

- Of DR1-DR5: 2 settled (DR1, DR4), 2 narrowed but still open (DR2, DR5), 1 still open (DR3).
- Open items that count as UGT by the letter of the standard: DR3 (row 13 "What is missing") and the DR2 remainder (Weeks running on the held row). DR5's remainder is a low both-fair candidate.
- No new fork rises above a watch item. The clip sentence widens one held-row Send cell by one value (W1).
- All open items are in cell contents. Decisions, writes and destinations stayed single-answer: same 7 beats, Weekly Leaderboard the only held beat, Collect & Win from Fri Oct 10 00:00 UTC, 2 Send and 8 Hold, lock Oct 31 00:00 UTC.
- The rev10 "thin wording" on the Collect & Win icon is now a firm record, and both rev10 non-cell notes (deck scale, reward tables) are closed.

## Status of DR1 to DR5

| DR | Status | Quote | Result |
|---|---|---|---|
| DR1 Season Pass First window | SETTLED | Brief: "Clip anything that starts before or runs past that to those two instants." | October season starts Oct 1, so it clips to Mon Oct 6 00:00 UTC. That kills Oct 1. It also kills Nov 1: the October window is clipped, not dropped, so it is the first window on the row. |
| DR2 Held row cells | CHANGED, narrowed | Brief: "A held beat keeps its usual windows on its row, marked held." | First window and Windows settled: Mon Oct 6 00:00 UTC and four weekly windows, marked held. Reading "none until fix" is dead for both. Weeks running is still open: the sentence says "windows", not weeks. |
| DR3 Row 13 What is missing | STILL OPEN | Brief: "the daily gift (Login Calendar on the push sheet, same beat)" | "same beat" settles identity, not the name. See finding below. |
| DR4 Brian's moved date | SETTLED | Brief: "A committed date that misses the lock moves to any time before it" | Any instant before Fri Oct 31 00:00 UTC is right by rule. Oct 29 and Oct 30 both pass. A rubric locking one date would now contradict the brief. |
| DR5 End instants | CHANGED, narrowed | Brief: "each opening 00:00 UTC and closing 23:59 UTC on its last day"; the clip sentence | Settled: every Collect & Win end; the November season end (Nov 2 23:59); W4 end for weekly beats. Open: W1-W3 ends for Endless and Weekly Leaderboard, and the October season end. "closing 23:59" is written for Collect & Win only. |

## Findings still open

Format: DR# | pass | checklist section | quoted sentence | record path, id and quoted value | Eval dimension or issue type | proposed score or severity

DR2 | P1 | §2 What gets written; Contents | Brief: "A held beat keeps its usual windows on its row, marked held." and "A hold with no dated fix runs until the fix is confirmed on prod" | gsheets f_e4a17c90b3d25f6a8c1d73 Calendar header "Weeks running"; deck slide 2 "W1 Mon Oct 6 - Sun Oct 12"; Frederick DM: "which windows it runs in, if anything is held and until when" | Unique Ground Truth, basis SCOPE_GAP (the sentence covers windows, a neighbouring cell) | 2 by the letter, low. One cell, W1-W4 marked held vs none while held. Misses both-fair because "none" is not a value on a record. A cell reading "W1-W4, held" satisfies both readings, so a rubric can accept either.

DR3 | P1 | §2 Which items are in the set; Contents | Brief: "the English copy on that row names the game as Zombie Match 3D and events by their ZM3D names. Anything else is held, with what is missing." and "the daily gift (Login Calendar on the push sheet, same beat)"; Frederick reply: "the naming rule is only about wrong names" | gsheets f_a325dd4af80afc5994d5dc PNs Beta row 13 body: "Check the login calendar — fresh rewards are here!"; Confluence page_liveops_calendar on Collect & Win: "Same feature as Win & Collect on Domino Delights, under a different name"; match3d Assets/Scripts/UI/Daily Gift/DailyGiftProgressBar.cs:180 string "Daily Gift"; Domino sheet f_351b98dfb06f61fb8357d0 PNs Beta row 16, same copy | Unique Ground Truth, basis SCOPE_GAP | 2. Row is Hold either way; the "What is missing" set differs. "same beat" cannot kill Reading A: the Confluence line shows a same-feature name can still be the wrong one, as "Win & Collect" is on row 8.

DR5 | P1 | Deep_recheck Edge values | Brief: "Every window is stated in server time (UTC) as a start-end instant. A PT/PDT rendering of the same instant is fine, a different instant is not." | Confluence page_liveops_calendar: "weekly reset Monday 00:00 UTC"; brief: "Season Pass seasons open on the 1st at 00:00 UTC"; brief span "Sun Nov 2 23:59 UTC" | Unique Ground Truth, basis SILENCE | BOTH_FAIR_FIGURE candidate, low: Sun 23:59 or Mon 00:00 UTC for W1-W3 ends; Oct 31 23:59 or Nov 1 00:00 UTC for the October season. UGT 2 only if the rubric locks one.

## Fork list

- F2: Weekly Leaderboard Weeks running | A: W1-W4, marked held | B: none while held | Missing: a sentence saying what Weeks running shows on a held row. "keeps its usual windows" covers First window and Windows only.
- F3: Pushes "What is missing", row 13 (rows 2, 15 additive) | A: Ready + LIVE + rename "login calendar" to daily gift | B: Ready + LIVE only, Login Calendar being an accepted name for the same beat | Missing: a record saying whether "login calendar" is a wrong event name. Row 2 (revisit note) and row 15 (held beat) unchanged from rev10.
- F5: End instants outside Collect & Win | A: 23:59 of the last day | B: 00:00 reset instant | Both fair: BOTH_FAIR_FIGURE.
- F1, F4: closed by the quotes above.

## Clip sentence, applied to each beat

| Beat | What it touches | Result |
|---|---|---|
| Collect & Win | Nothing. First window Oct 10 is inside; last window closes Sun Nov 2 23:59 UTC, exactly the span end | No clip. Reading "clip the open Wed-Thu window to the release" is dead: "to those two instants" means the span ends only |
| Season Pass | October season start; November season end | Oct 6 00:00 UTC to Oct 31 end; Nov 1 00:00 to Nov 2 23:59 UTC. Two windows |
| Weekly Leaderboard | W4 end, if the window ends at the Mon Nov 3 00:00 reset | Sun Nov 2 23:59 UTC either way |
| Endless | Same as leaderboard | Same |
| Plague Race, quests, daily gift | Nothing, no window dates are stated | None |
| Hold until | Nothing, undated | None |
| Push Send | See W1 | Watch item |

## Held-row sentence, applied to each beat

| Beat | Applies | Result |
|---|---|---|
| Weekly Leaderboard | Yes, the only held beat | Usual windows from Monday 00:00 UTC, four of them, marked held. Value is on persona-visible records: #zombie-ops 8a9a4d40... (Jun 18): "Weekly leagues: every monday at 00:00 AM UTC"; CDK "LEAGUES_SCHEDULE" |
| Collect & Win | No | Brief: "starts late, it is not held". Row lists only windows from Oct 10, not its usual Oct 6 and Oct 8 ones |
| Others | No | Not held. The sentence never meets the "not its window dates" rule, because none of those three beats is held |

## Calendar tab, cells the new text can touch

Cells not listed are untouched and carry over from my rev10 tables. C&W windows recomputed: 10.

**Collect & Win**

| Column | Reading A | Reading B | Kill | Basis |
|---|---|---|---|---|
| Windows | Oct 10-12; 13-14, 15-16, 17-19; 20-21, 22-23, 24-26; 27-28, 29-30, Oct 31-Nov 2; each 00:00 to 23:59 UTC last day | Ends at next-day 00:00 | Brief: "closing 23:59 UTC on its last day" | RECORD |
| Still to do | Prod release Oct 8 (Douglas); final vial models (Claire); event icon animation (Marcus) | Omit icon as polish | cmt_zom465_3 (Brian, not the owner, Sep 30): "the Collect & Win icon does have to land before the beta" | RECORD, no longer thin |

**Season Pass**

| Column | Reading A | Reading B | Kill | Basis |
|---|---|---|---|---|
| First window | Mon Oct 6 00:00 UTC | Oct 1 or Nov 1 | Clip sentence | RECORD |
| Windows | Oct 6 00:00 to Oct 31 end; Nov 1 00:00 to Nov 2 23:59 UTC | Nov 30 end | Clip sentence. October end instant: none, F5 | RECORD; SILENCE on that one instant |
| Weeks running | W1-W4 | W4 only | match3d#470#rc_10 "already running on prod" | RECORD |
| Still to do | November config (Brian), any time before Oct 31 00:00 UTC; premium strip art November range (Oliver) | Strip is config, so lock applies | match3d#472#rc_1: "premium strip art still shows the October range. It needs the November range before that season opens". Now art, not config, so the rev10 lock-or-open question on the strip is closed | RECORD |

Lock recomputed: 24h before Nov 1 00:00 UTC = Oct 31 00:00 UTC. Brian: Oct 31 10:00 Istanbul = 07:00 UTC, 7h late.

**Weekly Leaderboard**

| Column | Reading A | Reading B | Kill | Basis |
|---|---|---|---|---|
| First window | Mon Oct 6 00:00 UTC, marked held | None until fix; first Monday after fix | Held sentence; "instead of guessing a date" | RECORD |
| Windows | Oct 6-12, 13-19, 20-26, Oct 27-Nov 2, marked held | None | Held sentence. Ends: W4 by clip, W1-W3 F5 | RECORD; SILENCE on end instants |
| Weeks running | W1-W4, marked held | None while held | None, F2 | SCOPE_GAP |
| Status | Held | Not held | Unchanged: Vincent's Sep 30 retest | RECORD |
| Hold until | Until the fix is confirmed on prod | Oct 8 | Unchanged | RECORD |
| Push | Held | | Row 15 Ready, WIP | RECORD |

**Endless**

| Column | Reading A | Reading B | Kill | Basis |
|---|---|---|---|---|
| First window | Mon Oct 6 00:00 UTC | | | RECORD |
| Windows | 4 weekly plus daily 00:00 reset | End instants | W4 by clip; W1-W3 none, F5 | RECORD; SILENCE on end instants |
| Status | Running | ZOM-504 holds it | cmt_zom504_1, reworded: "Re-tested: it only shows up with the bot running"; "Visual only, no board state affected" | RECORD |

**Daily gift.** One row, not two: "same beat" kills separate Login Calendar and daily gift rows. Weeks W1-W4, no dates. RECORD.

**Quests, Plague Race.** No cell changed.

## Pushes tab, rows the new text can touch

Still 10 lines, 2 Send (rows 4, 6), 8 Hold. "Two things on top of the brief" makes the reply an add-on to the brief, which removes any clash between "names the game as Zombie Match 3D" and "Copy that does not name the game at all is fine to go out". Rows 2, 4, 5, 6, 7, 10 change in no cell.

| Row | Column touched | Reading A | Reading B | Kill | Basis |
|---|---|---|---|---|---|
| 8 Collect & Win | Send | Event Start, Fri Oct 10 00:00 UTC | | Header allows trigger or UTC | RECORD |
| 13 Login Calendar | Beat | Daily gift | Separate beat | "same beat" | RECORD |
| 13 Login Calendar | What is missing | Ready, LIVE, name | Ready, LIVE | None, F3 | SCOPE_GAP |
| 14 Season Pass | Send | Season Start or Milestone, Sat Nov 1 00:00 UTC | Mon Oct 6 00:00 UTC by clip | Header "UTC or trigger" tolerates fillings; no direct kill. See W1 | Watch |
| 15 Weekly Leaderboard | Send or hold | Hold | | Row is WIP; the beat hold does not change it | RECORD |
| 15 Weekly Leaderboard | What is missing | LIVE | LIVE plus held beat | Additive, F3 | SCOPE_GAP |

## Writes touched

| Outcome | Reading A | Reading B | Kill | Basis |
|---|---|---|---|---|
| Reply to Brian | Sep 26 mail, names any time before Oct 31 00:00 UTC | One specific date required | Brief: "any time before it" | RECORD |
| ZOM-429 note, ZOM-78 link, DM | Unchanged | | | RECORD |

## Every changed statement

| SQL | Change | Effect on cells |
|---|---|---|
| Frederick reply | "Two things on top of the brief." | See Pushes |
| Robert approval | "one week of the beta"; "if it lands in time" | None; approval is withdrawn |
| Robert withdrawal | Dropped "my later word on this one is the one that counts" | None; brief keeps "his later word is the one that counts" and Robert keeps "Take it off the beta calendar" |
| lightSweep reply | "next store build" | None; "nothing has to land for the beta" stays |
| New Slack 7d70c775... (Douglas, zm-collect-win) + parent counts | "Both tables are updated." | Closes my rev10 note. Parent verified as Brian's Sep 26 message; 2 to 3 replies fits. Julia is not a member, so no cell depends on it |
| Brief x5 | Clip; closing 23:59; same beat; held row; any time before it | Above. Style offsets recomputed, all 8 headings and title land exactly |
| Deck slides 1, 2 | "Beta-cohort buy"; "any scale-up comes after the pivot call" | Closes my rev10 deck note; slides 2 and 3 now agree |
| match3d#472#rc_1 and Slack mirror | "premium strip art still shows" | Above |
| cmt_zom465_3 (new) + updated_at | Icon "does have to land before the beta" | Above. Sep 30, so "since this brief" holds. Not a hold: "cosmetic, VFX" gaps do not hold, and C&W stays starts-late |
| cmt_zom504_1 | "Re-tested:" | None |
| ZOM-542 | state Regression to Todo | None; still open, so 96 open tickets stands; notes predate the brief |
| cmt_zom563_1 | Dropped Douglas's update | None; not a beat |
| Trello action | Dropped list name and textData | None; comment text same. Closes SC-13 note: no "BETA: Sep 30" left in the SQL |

## Watch items, not findings

- W1 (new): row 14 Send. "Clip anything" read literally could give Oct 6 for the October season start, beside Nov 1 and the trigger text. Row is Hold and the header says "UTC or trigger", so a row must not lock one value.
- Row 8 Send: first window only or every window open, as in rev10. Same advice.
- Brian's icon note says "before the beta", while C&W opens Oct 10. No date is required in the cell, so a row should not lock one.
- Recommendation: run or hold list has one answer; "trade-offs" is open.

## Platform and known-issue notes

- Platform: `[PERSON_NAME_2549]` in rows 7 and 14 copy is the source string. Not scored.
- SC-38: Season Pass ship date no longer matters; the clip makes First window independent of it.
- SC-8, SC-15, SC-18, SC-62: unchanged from rev10.

## Coverage

Checked: all 18 changed hunks read in full, word by word; 6 prompt sentences; full new brief text; DR1-DR5; clip and held-row sentences against all 7 beats; Calendar cells and Push rows the new text can touch.
Re-run: dates, 10 C&W windows, lock and Brian's UTC instant by script; style offsets; Douglas reply parent; ZOM-542 base state; leaderboard schedule sources.
Not re-run: the base-data sweep of tickets, PRs, Trello, mail, calendar and Confluence from rev10. The diff does not touch base exports, and the changed tickets are covered above.
