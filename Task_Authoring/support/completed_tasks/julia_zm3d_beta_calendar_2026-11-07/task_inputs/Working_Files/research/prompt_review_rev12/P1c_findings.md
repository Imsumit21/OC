# P1c findings, delta on rev12: Unique Ground Truth and Clarity

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Pass: P1. New SQL sha256 b5ccbfa577fc9f2c8f6eb3098f8d62a16623d799f41d11285de8227f1bed60d3, verified. Prev rev11 sha256 1348d287...e7, verified. Prompt read and unchanged. SQL read as overlay, never run. This run opened only R12 and the universe, no sibling review folder and no other reviewer's file. Earlier item numbers come from my own reports.

## Summary

- DR2, DR3 and DR5 are all settled, each by a rule in the brief.
- W1 is unchanged: no new text touches it. It is the only open item, a low both-fair candidate on a held row.
- No fail-level UGT finding remains from this pass.
- I tried to break all five new brief phrases and the other changed records. No fork came out of the new wording. Two residual readings are killed by records, listed in the fork hunt.

## Status of open items

| Item | Status | Rule | Result |
|---|---|---|---|
| DR2 Held row Weeks running | SETTLED | Brief: "A held beat keeps its usual windows and weeks on its row, marked held." | Weekly Leaderboard Weeks running is W1-W4, marked held. "None while held" is dead. |
| DR3 Row 13 What is missing | SETTLED | Brief: "events by their ZM3D names (Login Calendar and Weekly Rankings are fine). Anything else is held, with what its row is missing." | "login calendar" is not a wrong name, so row 13 is missing Ready and LIVE only. Reading A's rename is dead. The rows 2 and 15 additive readings are also dead, see below. |
| DR5 End instants | SETTLED | Brief: "Every window is stated in server time (UTC) as a start-end instant, closing 23:59 UTC on its last day." | The closing rule now covers every window, not only Collect & Win. Mon 00:00 and Nov 1 00:00 ends are dead. |
| W1 Row 14 Send | STILL OPEN, unchanged | Brief: "Clip anything that starts before or runs past that to those two instants." and "Season Pass seasons open on the 1st at 00:00 UTC." | No changed text touches it. See below. |

## Open item

Format: item | pass | checklist section | quoted sentence | record path, id and quoted value | Eval dimension or issue type | proposed score or severity

W1 | P1 | Deep_recheck Edge values | Brief: "Clip anything that starts before or runs past that to those two instants." and "Season Pass seasons open on the 1st at 00:00 UTC." | gsheets f_a325dd4af80afc5994d5dc PNs Beta row 14 When: "Season Start or Milestone"; gsheets f_e4a17c90b3d25f6a8c1d73 Pushes header "Send (UTC or trigger)" | Unique Ground Truth, basis SILENCE | BOTH_FAIR_FIGURE candidate, low. Trigger text is the safe fill. If a UTC value is written, Sat Nov 1 00:00 UTC is the only season start in the span, while a literal "Clip anything" gives Mon Oct 6 00:00 UTC. The Oct 6 reading is weak, but no quote kills it. Row is Hold either way, with the same writes. A rubric must not lock a value in this cell.

Fork list:

- W1: row 14 Send | A: trigger text, or Sat Nov 1 00:00 UTC | B: Mon Oct 6 00:00 UTC by clip | Both fair: BOTH_FAIR_FIGURE.
- F2, F3, F5: closed by the rules above.

## Window close for every beat

Rule: "closing 23:59 UTC on its last day". All dates and weekdays recomputed by script.

| Beat | Windows and closes (UTC) | Rule | Basis |
|---|---|---|---|
| Collect & Win | 10 windows. Fri Oct 10 00:00 to Sun Oct 12 23:59; then closes Tue Oct 14, Thu 16, Sun 19, Tue 21, Thu 23, Sun 26, Tue 28, Thu 30, Sun Nov 2, all 23:59 | General closing rule; last close equals the span end | RECORD |
| Season Pass | Mon Oct 6 00:00 (clipped) to Fri Oct 31 23:59; Sat Nov 1 00:00 to Sun Nov 2 23:59 (clipped from the season's own end) | Clip plus closing rule | RECORD |
| Weekly Leaderboard | Mon Oct 6 to Sun Oct 12, Oct 13-19, Oct 20-26, Oct 27-Nov 2, each Mon 00:00 to Sun 23:59, marked held | Held sentence plus closing rule; Monday schedule from #zombie-ops 8a9a4d40... and CDK | RECORD |
| Endless | Same four weekly windows; daily windows 00:00 to 23:59 | Closing rule. Monday 00:00 stays the reset and the next window's open, so no clash with Confluence | RECORD |
| Plague Race, quests, daily gift | No window dates | "not its window dates", the specific rule for these three, beats "Every window" | RECORD |

## Held row

Only Weekly Leaderboard is held. Collect & Win "starts late, it is not held", so the sentence does not apply and its row starts at Oct 10.

| Column | Value | Reading B | Kill | Basis |
|---|---|---|---|---|
| First window | Mon Oct 6 00:00 UTC, marked held | None until fix | "keeps its usual windows" | RECORD |
| Windows | Four weekly, closes above, marked held | None | Same | RECORD |
| Weeks running | W1-W4, marked held | None while held | "usual windows and weeks" | RECORD |
| Status | Held | Not held | Vincent's Sep 30 retest, unchanged. New cmt_zom563_1 shows the Sep 30 prod update "carried only these", so that retest came after it and no fix was in it | RECORD |
| Hold until | Until the fix is confirmed on prod | A date | "say that instead of guessing a date" | RECORD |
| Push | Held | | Row 15 | RECORD |
| Still to do | Fix (Douglas) | | "its fix if it is held" | RECORD |

## Push rows under "what its row is missing"

The set is the conditions of the sentence before it: Ready, LIVE, correct names. Rows that name no game are not missing it: Frederick, "Copy that does not name the game at all is fine to go out". Still 10 lines, 2 Send, 8 Hold.

| Row | Status / LIVE | Name check | Send or hold | What is missing | Reading B | Kill | Basis |
|---|---|---|---|---|---|---|---|
| 2 Quests | Not Ready / LIVE | No name issue | Hold | Ready | Also "Revisit once new quests roll out" | That Details note is not one of the conditions. Writing it as well is harmless, since Ready is still there | RECORD |
| 4 Lives | Ready / LIVE | No game name, allowed | Send | | | | RECORD |
| 5 1-day lapsed | Ready / LIVE | "Puzzles vs Zombies" wrong | Hold | Game name | | | RECORD |
| 6 7-day lapsed | Ready / LIVE | No game name, allowed | Send | | | | RECORD |
| 7 FTUE | Ready / LIVE | "Puzzles vs Zombies" wrong | Hold | Game name | | | RECORD |
| 8 Collect & Win | Not Ready / WIP | "Win & Collect" wrong, not on the allowed list | Hold | Ready, LIVE, event name | | | RECORD |
| 10 Plague Race | Ready / WIP | OK | Hold | LIVE | | | RECORD |
| 13 Login Calendar | Not Ready / WIP | "are fine" | Hold | Ready, LIVE | Also a rename | "(Login Calendar and Weekly Rankings are fine)" | RECORD |
| 14 Season Pass | Not Ready / WIP | OK | Hold | Ready, LIVE | | | RECORD |
| 15 Weekly Leaderboard | Ready / WIP | "are fine" | Hold | LIVE | Also the held beat | "its row": the beat hold is not on the row | RECORD |

Rows 13 and 15 stay Hold: "are fine" clears only the name, and "only if its row is Ready and LIVE" still fails.

## Shop sentence

| Item | Reading A | Reading B | Kill | Basis |
|---|---|---|---|---|
| Rotating shop | Not a beat | A daily reset players see | Brief: "the shop rotation is not a beat"; ZM3D records call it that: Confluence Economy Design, ZM3D table, "rotating shop"; ZOM-348 "Rotating Shop Discount Issues" | RECORD |
| Daily free coin (ZOM-539) | Not a beat | Not "rotation", so still "a reset" | Sentence does not name it. page_liveops_calendar: "the single source of truth for what live-ops events are scheduled" has no shop row | RECORD |
| Pop-up Offers, Rewarded Ads (Trello Oct 21) | Not beats | | Not "an event window, a reset or a start push" | RECORD |
| Other excluded items imply the rest are beats | Beat set stays 7 | More resets are beats | Every prod schedule in the CDK maps to a beat or a stated exclusion; quests and daily gift are named in the brief | RECORD |

"until the pivot call" stays with Boss Arena: the comma and "and" start a separate clause, and either way no shop row appears in the span.

## Other cells the new text touches

| Beat, cell | Value | Change | Basis |
|---|---|---|---|
| C&W Still to do | Prod release Oct 8 (Douglas); final vial models (Claire); icon animation (Marcus) | match3d#468#rc_38: "missing and need to be in before the beta". Vials now say "needed" outright | RECORD |
| C&W First window, Status | Fri Oct 10 00:00 UTC; starts late | cmt_zom563_1 (Douglas): "That update carried only these, the Collect & Win server windows wait for the Oct 8 release." This kills a reading that the Sep 30 prod update was the "next backend release" of #470#rc_10 | RECORD |

## Every changed statement

| SQL | Change | Effect |
|---|---|---|
| Brief, Span | Closing rule moved to "Every window"; C&W sentence back to "each opening 00:00 UTC" | Settles DR5 |
| Brief, Scope | "and the shop rotation is not a beat" | Shop table |
| Brief, Held | "windows and weeks" | Settles DR2 |
| Brief, Push copy | "(Login Calendar and Weekly Rankings are fine)"; "what its row is missing" | Settles DR3 |
| Brief style runs | Recomputed | Title and all 8 headings land exactly |
| match3d#468#rc_38 and Slack mirror | Vials "need to be in before the beta" | C&W Still to do |
| cmt_zom465_3 | "was ticked before that event merged" | No cell change; icon quote stays |
| cmt_zom563_1 (new, Douglas), cmt_zom563_2 (Vincent, renumbered) | Prod update scope | C&W and Leaderboard, above. Times 18:17 then 22:04 are in order; the Done UPDATE is unchanged |
| Trello action | idCard and textData restored | No text change |

## Fork hunt on the new wording

| Phrase | Reading tested | Result |
|---|---|---|
| "closing 23:59 UTC on its last day" | Clashes with Monday 00:00 reset | No: Monday 00:00 is the next window's open |
| Same | Applies to the GCal "release window" or the no-date beats | No: the release is "the backend release instant"; the three beats have "not its window dates" |
| Same | "last day" unclear for a clipped window | No: the clip sentence gives Nov 2 23:59, same value |
| "usual windows and weeks" | Conflicts with "A hold ... runs until the fix is confirmed" | No: the row shows the schedule, "marked held" shows the state, Hold until shows the end |
| Same | Reaches Collect & Win's Oct 6 and Oct 8 windows | No: "it is not held" |
| "(Login Calendar and Weekly Rankings are fine)" | Rows 13 and 15 may go out | No: "only if its row is Ready and LIVE" |
| Same | Allow-list makes other labels wrong | Checked all 10 copies. Only "Win & Collect" and "Puzzles vs Zombies" are wrong names; Plague Race, Season Pass, quests and leaderboard are ZM3D names |
| "what its row is missing" | Rows with no game name are missing it | No: Frederick's reply |
| "the shop rotation is not a beat" | Daily free coin survives | Killed by the Confluence page, a record rather than the sentence |
| "need to be in before the beta" with "does have to land before the beta" | C&W held or delayed until art lands | No: "cosmetic" gaps do not hold, and the start is set by server windows |
| Same | Which date is "the beta": Oct 6, or Oct 10 from Trello's list name (SC-13) | No date is required in the cell, so a row must not lock one. Watch only |

## Watch items, not findings

- Row 8 Send: first window only or every window open, unchanged. Header allows either; a row must not lock one.
- "Before the beta" date, as above.
- Recommendation: run or hold list has one answer; "trade-offs" is open.

## Platform and known-issue notes

- Platform: `[PERSON_NAME_2549]` in rows 7 and 14 copy is the source string. Not scored.
- SC-13: only the watch item above. SC-8, SC-15, SC-18, SC-38, SC-62: unchanged from rev11.

## Coverage

Checked: all 10 changed hunks read word by word; full new brief; 6 prompt sentences; closes for all 7 beats; the held row; all 10 push rows; the shop sentence.
Re-run: dates and closes by script; style offsets; ZOM-563 comment order; shop records in Linear, Confluence and the client repo.
Not re-run: the rev10 base-data sweep and any cell the diff cannot reach. The diff does not touch base exports.
