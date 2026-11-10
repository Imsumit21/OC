# P1e findings: Unique Ground Truth and Clarity (deep recheck pass P1)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

## Result

No fail-level fork found. Of 30 candidates, 29 are killed by a quote or give the same result at every edge. One stays open (DR1). No quote kills its Reading B, but it differs only by an extra clause in one free-text cell.

Clarity: no write divergence survives. Both candidates that change the writes (F2, F10) are killed by rule-source quotes.

Checked: 45 rule-source sentences (prompt 6, Frederick's message 6, thread reply 5, brief 28), 14 PNs Beta rows, 16 sheet columns, 7 beats in and 9 out.

## Reading A, built from the rule sources

Calendar tab

| Beat | First window (UTC) | Windows (UTC) | Weeks | Status | Hold until | Push | Still to do (owner) |
|---|---|---|---|---|---|---|---|
| Collect & Win | Fri Oct 10 00:00 | 10 windows: Oct 10-12; then Mon-Tue, Wed-Thu, Fri-Sun for W2-W4, last Oct 31-Nov 2 23:59 | W1 (from Fri) to W4 | Starts late, not held | none | Hold | Oct 8 prod deploy (Douglas); final vial models (Claire); C&W icon animation (Marcus) |
| Season Pass | Mon Oct 6 00:00 (clipped) | Oct 6 00:00 to Oct 31 23:59; Nov 1 00:00 to Nov 2 23:59 | W1-W4 | Runs | none | Hold | November config before Oct 31 00:00 (Brian); November range on premium strip art (Oliver) |
| Weekly Leaderboard | Mon Oct 6 00:00 | 4 Mon 00:00 to Sun 23:59 windows | W1-W4 | Held | Until the fix is confirmed on prod, no date | Hold | ZOM-429 fix (Douglas) |
| Endless | Mon Oct 6 00:00 | Daily 00:00-23:59; 4 weekly Mon-Sun windows | W1-W4 | Runs | none | No row on the tab | none |
| Plague Race | no dates | no dates | W1-W4 | In | none | Hold | none |
| Quest rollover | no dates | no dates | W1-W4 | In | none | Hold | none |
| Daily gift | no dates | no dates | W1-W4 | In | none | Hold | none |

Off the calendar: Boss Arena, shop rotation, Zombie Lane, Halloween prop set, Axe Arena, Hourly Coins, Nathan's Treasure Hunt, Streak Fever.

Pushes tab: 10 lines (14 rows less 4).
- Send (2): row 4 lives recharged; row 6 Lapsed 7d.
- Hold (8), with what the row is missing:
  - Row 2 Quests: Not Ready
  - Row 5 Lapsed 1d: copy says Puzzles vs Zombies
  - Row 7 FTUE: copy says Puzzles vs Zombies
  - Row 8 Win & Collect: Not Ready, WIP, wrong event name
  - Row 10 Plague Race: WIP
  - Row 13 Login Calendar: Not Ready, WIP
  - Row 14 Season Pass: Not Ready, WIP
  - Row 15 Weekly Leaderboard: WIP

Writes (5):
1. Both tabs of ZM3D Beta Live-Ops Calendar (f_e4a17c90b3d25f6a8c1d73).
2. Note on ZOM-429.
3. Sheet link on ZOM-78.
4. Recommendation in the Frederick DM D05SD5QLG94.
5. Reply to Brian on his Sep 26 mail.

## Findings

DR1 | P1 | common_errors §2 contents; Eval 1 §2.1 check 5 | Brief, Push copy: "Anything else is held, with what its row is missing." | Sheet f_a325dd4af80afc5994d5dc, tab PNs Beta, row 2: Status "Not Ready", Details "Revisit once new quests roll out.", Status (NA, WIP, LIVE) "LIVE". Trello action 68dac8204f1e9a3b7c2d5e61 on card 61: "More quests and the reward balance go in with the Mon Oct 13 rollover if they are ready." | Unique Ground Truth | Open, basis SILENCE. Reading A: missing = Ready status. Reading B: missing = Ready status plus the new quests the row says to wait for. The decision (held), writes and destination are the same; only the "What is missing" cell differs. My view is same material result under check 5, so I would not fail on it alone. The main session must rule, because Setup says "additive" is no ground to reject. The rubric should accept either wording.

No other findings.

## Fork list

- F1: Local push rows as Calendar beats | A: Pushes tab only | B: Lives, Lapsed and FTUE get Calendar rows | Settled by: brief "an event window, a reset or a start push"; their When values are triggers, and thread reply puts them under "Pushes: plan the PNs Beta tab".
- F2: Held start push counts as a held beat, so ticket notes multiply | A: one note, on ZOM-429 | B: a note per held start push | Settled by: Frederick "the push that goes with it"; brief "Hold a beat only when players provably cannot enter, score or claim". No ZOM ticket exists for a push row.
- F3: Weekly Leaderboard | A: held | B: not held, restart works | Settled by: Vincent, #zombie-match3d, Sep 30 20:50 UTC: "I killed the app and reopened it twice ... my week is still last week one. Same on the second device." This is newer than Douglas on ZOM-429, Sep 16: "they land in the new week fine".
- F4: Endless held on the S23 freeze | A: not held | B: held | Settled by: Leonard, the reporter, Sep 29: "Could not get it to freeze, so I am leaving this one."; brief "an unverified one does not".
- F5: C&W held by PR #468 review notes (rc_38 vials; CodeRabbit rc_1 "blocking gameplay") | A: not held | B: held | Settled by: both reviews are state COMMENTED, while the same bot used CHANGES_REQUESTED on #303. Brief: "cosmetic ... gaps" do not hold, and "player-facing art" goes in Still to do. The rc_1 guard is at HEAD, GameLoader.cs line 184.
- F6: "Aug-Sep live-ops cohort" has no defining record | A: rule holds nothing | B: some wider cohort holds a beat | Same result at every edge: 0 of 74 CHANGES_REQUESTED reviews are dated Aug-Sep. The nearest are #303 (Jul 16) and backend #4 (Jun 6 and 10). The term is undefined but changes no cell.
- F7: C&W first window | A: Fri Oct 10 | B: Wed Oct 8 or Thu Oct 9 | Settled by: GCal evt_5c1e83a7d94b02f6c8e31a 15:00-16:00 UTC; brief "first window that opens after" and "Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC". This overrides the CDK cron "0 0 * * 3,4", which fires on Thursday too.
- F8: Season Pass lock | A: Oct 31 00:00 UTC, Brian misses by 7h | B: "the day before" means all of Oct 31, or no lock exists | Settled by: spec "locked 24h before each season opens"; calendar page "The 24h season-pass freeze".
- F9: Which commitment and which mail | A: Oct 31, Sep 26 mail | B: Oct 29, Sep 22 mail | Settled by: Brian Sep 26: "Treat Fri Oct 31 as the date I am committing to and drop the Oct 29 one"; "reply on this mail".
- F10: Reply to Brian (write vs no write) | A: reply | B: the prompt lists no such write, so record it on the sheet only | Settled by: brief "its owner is told in a reply on the mail where they committed to it"; prompt "his working rules ... are in the brief", "Can you take it on for me?". The clause is passive, so this is the thinnest kill in the list.
- F11: More quests in Still to do | A: nothing for the quest rollover | B: Leonard/Douglas, Oct 13 | Settled by: "The weekly rollover does not wait on them". If that owner claim is discounted, nothing is flagged since the brief (card created Sep 12), and "Nothing else goes in" excludes it. Out either way.
- F12: Quests push "What is missing" | A: Not Ready | B: Not Ready plus new quests | Missing: a brief sentence saying whether a row's Details note counts as missing. See DR1.
- F13: Halloween row | A: off | B: on, or shown as pulled | Settled by: Robert DM Sep 30 22:10 UTC: "pulling my ok. Take it off the beta calendar"; brief "his later word is the one that counts".
- F14: Endless polish and themes in Still to do | A: none | B: ZOM-565, refill timer, desert and port themes | Settled by: ZOM-565 Marcus "not needed for the beta"; Brian "do not have to land before the beta"; Robert "nothing waits on new themes".
- F15: lightSweep box | A: out | B: Still to do | Settled by: Vincent, who flagged it: "nothing has to land for the beta".
- F16: C&W title, info text, token travel, analytics | A: out | B: Still to do | Settled by: ZOM-566 Brian "do not have to land before the beta"; ZOM-526 Calvin "Only the Axe Arena travel is left here"; brief "not analytics".
- F17: Daily gift frame | A: done | B: Still to do until store approval | Settled by: ZOM-432 Samuel "in both submission builds"; #builds iOS #50 and Android #135; UA deck "once the stores approve the Sep 30 builds".
- F18: Daily gift held on ZOM-556 | A: no | B: yes | Settled by: Vincent "claiming works and nothing is lost"; brief "Wrong counters".
- F19: Quest rollover held on ZOM-534 (still In Progress) | A: no | B: yes | Settled by: Leonard, the reporter, Sep 30: "it is good on prod now".
- F20: Which PNs Beta tab | A: Zombie Match sheet | B: Domino Adventure sheet | Settled by: brief "Ready and LIVE" and "Weekly Rankings"; the Domino tab has no Ready column and no such copy.
- F21: Row 8 name | A: wrong name | B: fine, since Slack and PR titles say Win & Collect | Settled by: calendar page "Same feature as Win & Collect on Domino Delights, under a different name".
- F22: Leagues and Weekly Leaderboard as two beats | A: one | B: two | Settled by: Debug Wishlist "Weekly Leaderboards: ... weekly league sessions"; ZOM-544 "Weekly contest of leaderboard, the score, the league itself".
- F23: Endless Windows cell | A: daily and weekly | B: weekly only | Settled by: brief "Every window is stated"; calendar page "resets daily at 00:00 UTC and weekly on Monday 00:00 UTC". The rubric should accept a compact rendering of the 28 daily windows.
- F24: Which sheet | A: ZM3D Beta Live-Ops Calendar | B: LiveOps Event Calendar | Settled by: prompt "my live-ops calendar sheet"; Frederick "your ZM Live Ops folder".
- F25: Which ticket | A: ZOM-78 | B: a new ticket | Settled by: Frederick on ZOM-78: "Link the sheet here when it is ready."
- F26: Boss Arena | A: off | B: back after the pivot call | Settled by: brief "off this calendar until the pivot call"; Frederick "This goes into the pivot call". No dated pivot call found in GCal.
- F27: Season Pass first window | A: Oct 6 | B: Oct 1 or Nov 1 | Settled by: brief "Clip anything that starts before".
- F28: Owner of the Oct 8 deploy | A: Douglas | B: Arthur | Settled by: GCal organizer and creator douglas@; Live-Ops Event Engine "Scheduler ... Backend (Douglas)"; Douglas on ZOM-563 "wait for the Oct 8 release".
- F29: Thread reply outside "his message" | A: applies | B: does not | Settled by: same author, same thread, later: "Two things on top of the brief."
- F30: Store approval in Still to do | A: out | B: in | Settled by: brief "Nothing else goes in". The deck predates the brief, so it is not flagged since.

## Edge values

| Item | Edge | Result |
|---|---|---|
| Release instant | Start 15:00 or end 16:00 UTC; Istanbul 18:00; PT 08:00 | Fri Oct 10 at every edge |
| Lock | UTC (rule) Oct 31 00:00; Istanbul reading of the same instant, 03:00 | Brian (07:00 UTC) misses by 7h |
| Lock, wrong base | Season open read as PT: lock Oct 31 07:00 UTC | Brian lands exactly at the lock, not before; still misses |
| Lock, before correction | Oct 29 commitment | Passes, no mail. The Sep 26 correction governs. |
| C&W windows | W1 partial | 1 + 3 + 3 + 3 = 10 |
| Span ends | Oct 6 00:00 and Nov 2 23:59 included | Every weekly and C&W window fits; only Season Pass clips |
| ZOM-429 | Before and after Sep 30 | Not held on Sep 16; held on Sep 30 |
| ZOM-465 | Before and after Sep 30 | Sep 26 "every event icon" corrected; icon is in Still to do |
| Borderline status | ZOM-534 In Progress, ZOM-566 In Progress, ZOM-429 Backlog | Decisions rest on comments, not state |
| Change requests | Any Aug-Sep definition | 0 |
| Plague Race cycle | CDK daily vs Snowflake 5-day runs | No effect: brief says "not its window dates" |

## Decision sweep basis

RECORD:
- Holds: Weekly Leaderboard (Vincent); Endless (Leonard); quest rollover (Leonard); daily gift (Vincent).
- Late start: Arthur on #470 rc_10; GCal; ZOM-563.
- Lock: spec.
- Commitment: Sep 26 mail.
- Still to do: vials (Arthur); icon (Brian, who is not the owner); strip art (Arthur).
- Halloween: Robert.
- Every push decision: sheet cells plus the brief and thread reply.

RECORD through the brief's closed list ("flagged ... as still needed", "Nothing else goes in"), not through any owner claim:
- Exclusion of ZOM-542, ZOM-471, ZOM-543, ZOM-521.
- Trello card 61 and the Addressables work.

Owner claims I did not rely on alone:
- Douglas on ZOM-534: corroborated by Leonard.
- Owen on ZOM-546: not needed, because no record shows players cannot score, and the ticket predates the brief.
- Leonard on card 61: see F11.

SILENCE: F12 only.

SCOPE_GAP: none left.

## Clarity (Eval 1 §2.6)

Intent is clear and key details are present. Each destination resolves to one record. The write sets of the surviving readings are identical. The only write-changing readings (F2, F10) are killed. The brief authorizes one free value: the moved date is "any time before" the lock, so the rubric must accept any instant before Oct 31 00:00 UTC.

## Platform defects

PLATFORM:anonymized-token: PNs Beta rows 7 and 14 carry [PERSON_NAME_2549] in the copy. A copy cell using the token as shown is correct.

## What I scanned

- Inputs: prompt, assignment block, date, full SQL.
- References: deep_recheck.md, common_errors.md, SEARCH.md, persona folder, catalog.json write tools, Eval 1 §1.2, §2.1, §2.6, known issues SC-1 to SC-73.
- Sheets: both Push Notifications spreadsheets, PNs Beta and PNs tabs, translated tab header.
- Linear: all open ZOM issues, and key descriptions including ZOM-78, 429, 432, 465, 521, 526, 534, 543, 556, 563, 565, 566.
- Trello: ZM ROADMAP Beta and Oct 21 lists, cards 10, 22, 27, 58, 61, 63, 79, actions since Sep 20.
- GitHub: PRs since Aug 1 for match3d, backend and live-ops repos; all 74 CHANGES_REQUESTED reviews; timeline events; reviews on #468, 470-475, 477.
- Repos: ZM-Liveops-Docs; backend scheduler, cycle servers, config and CDK stack; GameLoader.cs at HEAD.
- Confluence: live-ops calendar, event engine, Season Pass spec, ops home, release checklist, ZM3D GDD, quest postmortem.
- Snowflake: LIVE_EVENT_PERFORMANCE, all ZM3D rows.
- Other: GCal, Docs and Drive keyword searches; all 304 messages in Julia's base mailbox (one since Sep 1, an unrelated calendar cancel).
- Slack, Aug-Sep 2025: #zombie-bugs read from Sep 21; #zombie-ops; #zm-collect-win to Sep 19; Frederick DM tail; Halloween, S23 and lightSweep threads; keyword sweeps across the rest.

Limits:
- Most Slack channels were keyword-swept, not read in full.
- Image attachments were not opened, so I cannot say which beat the lightSweep box belongs to. Vincent's retraction makes that moot.
- The cross-mailbox Gmail queries "Season Pass" and "push notification" hit their limits, so they prove no absence. Julia's own mailbox was read in full instead.
- P2, P3 and P4 topics were not assessed. SQL was read, never run.
- I opened no other reviewer's file.
