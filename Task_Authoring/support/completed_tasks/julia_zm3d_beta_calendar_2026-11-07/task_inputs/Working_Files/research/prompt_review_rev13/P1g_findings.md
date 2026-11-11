# Deep recheck P1: Unique Ground Truth and Clarity

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Result: 2 findings, both open forks. 38 other candidates are settled by a quoted rule or record.

Checked: 45 sentences (prompt 6, Frederick's message 6, thread reply 5, brief 28), 7 beats, 14 PNs Beta rows, 16 sheet columns (Calendar 9, Pushes 7), 6 writes. Blind: I did not open R/prev, R/work outside p1g, other reviewers' files, or any task folder.

## Reading A, built from the prompt, message, reply and brief

**Calendar tab, 7 rows**

| Beat | First window (UTC) | Windows | Weeks | Status | Push | Still to do (owner) |
|---|---|---|---|---|---|---|
| Collect & Win | Fri Oct 10 00:00 | 10 windows, Fri Oct 10-Sun Oct 12 through Fri Oct 31-Sun Nov 2 | W1 from Oct 10, W2-W4 | Starts late, not held | Held: Not Ready, WIP, wrong event name | Oct 8 prod deploy (Douglas); final vial models (Claire); event icon animation (Marcus) |
| Season Pass | Mon Oct 6 00:00, clipped | Oct 6 00:00-Oct 31 23:59; Nov 1 00:00-Nov 2 23:59 | W1-W4 | Running | Held: Not Ready, WIP | November config before Fri Oct 31 00:00 UTC (Brian); premium strip art (Oliver) |
| Weekly Leaderboard | Mon Oct 6 00:00 | 4 weekly windows, Mon 00:00-Sun 23:59 | W1-W4 | HELD, until the fix is confirmed on prod | Held: WIP | ZOM-429 fix (Douglas) |
| Endless | Mon Oct 6 00:00 | Open fork F2 | W1-W4 | Running | No row on the tab | None |
| Plague Race | No dates, per brief | No dates | W1-W4 | In | Held: WIP | None |
| Quest rollover | No dates | No dates | W1-W4 | In | Held: Not Ready | None |
| Daily gift | No dates | No dates | W1-W4 | In | Held: Not Ready, WIP | None |

**Pushes tab, 10 rows**

- Send (2): R4 lives recharged, R6 7-day lapsed.
- Hold (8): R2 quests (Ready); R5 and R7 (wrong game name, "Puzzles vs Zombies"); R8 (Ready, LIVE, event name); R10 and R15 (LIVE); R13 and R14 (Ready, LIVE).
- Left off: R3, R9, R11, R12.

**Writes**

1. Calendar tab of ZM3D Beta Live-Ops Calendar.
2. Pushes tab of the same sheet.
3. Comment on ZOM-429.
4. Sheet link on ZOM-78.
5. Reply to Frederick in DM D05SD5QLG94.
6. Reply on Brian's Sep 26 mail. This one is open: F1.

## Findings

`DR1 | P1 | common_errors §2 "What gets written"; Eval 1 §2.1, §2.6 write-action hard gate | "What he wants in it is in his message, and his working rules for building it are in the brief he shared with me." + "Once the sheet's done, link it on the calendar ticket and send Frederick the recommendation he asked for." | gdocs f_7c3e91a4d2b85f60e1a9c4: "A committed date that misses the lock moves to any time before it and its owner is told in a reply on the mail where they committed to it."; gmail julia.lawson@harmonygames.co/1844311412966040123: "Treat Fri Oct 31 as the date I am committing to"; confluence page_season_pass_spec: "locked 24h before each season opens" | Unique Ground Truth; Clarity (Action Decision Ambiguity) | 2 and 2, fail-level: write vs no-write`

- **Reading A:** the Agent replies on Brian's Sep 26 mail, moving the date to before Fri Oct 31 00:00 UTC.
- **Reading B:** the Agent writes the moved deadline in the Season Pass row, flags it to Frederick and sends no mail.
- **Why B is defensible:**
  - The prompt scopes the brief as rules "for building it", which means the sheet.
  - The prompt then lists the outbound writes (ticket note, ticket link, recommendation) and leaves this one out.
  - The brief's sentence is passive and names no sender. Frederick is on that mail in copy.
  - WORKFLOW `prompt-incorporation-v1` says to inspect the passage's "task scope", and Eval 1 §1.2 needs the source to "clearly state" the requirement.
- **Kill:** none. The best candidates are the sentence above plus "Can you take it on for me?". They rule out Brian going untold. They do not say the Agent is the one who tells him. That is an inference, even though A is the leading reading.
- **Basis:** SCOPE_GAP.
- **Missing:** a prompt sentence that puts the brief's follow-ups, or this reply, in the Agent's hands.

`DR2 | P1 | common_errors §2 "Which number"; deep_recheck Edge values; Eval 1 §2.1 | Frederick: "which windows it runs in"; brief: "Every window is stated in server time (UTC) as a start-end instant, closing 23:59 UTC on its last day." | confluence page_liveops_calendar: "Recurring - daily reset 00:00 UTC, weekly reset Monday 00:00 UTC"; match3d-backend zombies-game-cdk-stack.ts: ENDLESS_MONSTER_DAILY_SCHEDULE "0 0 * * *", ENDLESS_MONSTER_WEEKLY_SCHEDULE "0 0 * * 1" | Unique Ground Truth (contents of the Endless Windows cell) | 2 under the Portal standard as an unresolved SILENCE fork; Clarity at most NON-FAIL, since the writes are the same`

- **Reading A:** 4 weekly windows, Mon 00:00-Sun 23:59.
- **Reading B:** 28 daily windows, each 00:00-23:59.
- **Why it is open:** the brief excuses quests, daily gift and Plague Race from window dates. It does not excuse Endless and does not say which cadence is its window.
- **Kill:** none.
- **Caveat:** a cell stating both satisfies both readings, so the harm is one rubric cell. The setup says a superset is not grounds to reject, so it stays open.
- **Not a both-fair figure:** it is a set of windows, not one figure.
- **Missing:** a brief line naming the cadence for Endless, or adding Endless to the no-dates list.

## Fork list

Each line ends with its basis. Open forks come first.

**Open**

- F1: Reply to Brian | A: Gmail reply on the Sep 26 mail | B: no mail, flag only | Missing: a prompt sentence giving the Agent that reply. [SCOPE_GAP]
- F2: Endless Windows cell | A: 4 weekly | B: 28 daily | Missing: a brief line naming the cadence. [SILENCE]

**Set and destination**

- F3: Sheet | A: ZM3D Beta Live-Ops Calendar | B: LiveOps Event Calendar.xlsx or the Confluence calendar | Settled by: "Put it in the calendar sheet in your ZM Live Ops folder". [RECORD]
- F4: Calendar ticket | A: ZOM-78 | B: ENG-2240 | Settled by: cmt_zom78_1 "Let us use this ticket for the ZM3D beta live-ops calendar". [RECORD]
- F5: Push source | A: Push Notifications Zombie Match, PNs Beta | B: the Domino Adventure file, or the Translated tab | Settled by: brief "its row is Ready and LIVE" (the Domino tab has no Ready column), and "the translated tab is the old Domino set". [RECORD]
- F6: Push rows | A: 10 | B: 14, or fewer | Settled by: "Leave off the four rows ... just those four". [RECORD]
- F7: Calendar rows for lives, lapsed and FTUE pushes | A: Pushes tab only | B: their own beats | Settled by: "an event window, a reset or a start push". [RECORD]
- F8: Off-calendar items | A: Zombie Lane, Boss Arena, rotating shop and Axe Arena stay off | B: listed anyway | Settled by: "keep Zombie Lane off the calendar"; "Boss Arena is off this calendar until the pivot call, and the rotating shop is not a beat"; "not in the beta". The Trello "Oct 21" Axe Arena card loses to Frederick's reply. [RECORD]
- F9: Halloween | A: off | B: stays as an overlap, since overlaps need no approval | Settled by: Robert's Sep 30 DM "pulling my ok. Take it off the beta calendar". Spec: "Owner: Robert (Product)". [RECORD]
- F10: Desert and port themes | A: no beat, no to-do | B: Endless to-do | Settled by: Robert "Keep them as options, Endless runs with what it has now and nothing waits on new themes." [RECORD]

**Push decisions**

- F11: R4 and R6 | A: Send | B: Hold, because the game is not named | Settled by: "Copy that does not name the game at all is fine to go out". [RECORD]
- F12: R5 and R7 | A: Hold | B: Send, since it is the old store name | Settled by: Live-Ops Event Engine "listed as "Puzzles vs Zombies" until the July 2025 store rename" and brief "names the game as Zombie Match 3D". [RECORD]
- F13: R8 event name | A: wrong | B: fine | Settled by: calendar page "Collect & Win ... Same feature as Win & Collect on Domino Delights, under a different name". [RECORD]
- F14: R10 and R15 | A: Hold on the sheet | B: Send, because NotificationManager.cs already schedules them and Leonard says "All our PNs are local" | Settled by: "plan the PNs Beta tab as it stands". [RECORD]
- F15: R2 after Oct 13 | A: Hold | B: Send once the new quests land | Settled by: "as it stands"; the row is Not Ready. [RECORD]
- F16: R4 Send cell | A: lives recharged | B: Rollover | Settled by: row Details "When lives are recharged" and client ScheduleLivesRechargedNotification. The header allows "UTC or trigger", so accept either wording. [RECORD]

**Windows**

- F17: Collect & Win status | A: starts late | B: held | Settled by: "A beat whose server windows are waiting on that release starts late, it is not held." [RECORD]
- F18: Collect & Win first window | A: Fri Oct 10 00:00 | B: Wed Oct 8 at the release, or Mon Oct 6 | Settled by: "the first window that opens after"; gcal "2025-10-08 15:00:00+00"; rc_10 "still on the DEV stack only"; cmt_zom563_1 "wait for the Oct 8 release". [RECORD]
- F19: Season Pass first window | A: Oct 6 clipped | B: Oct 1, or Nov 1 | Settled by: "Clip anything that starts before ..."; rc_10 "already running on prod". [RECORD]
- F20: Plague Race dates | A: none | B: Snowflake 5-day blocks vs CDK daily | Settled by: "not its window dates". [RECORD]

**Holds**

- F21: Leaderboard | A: held | B: not held, as a reset that needs a restart, or as unverified | Settled by: Vincent, C0880U9751A 1759265412.481909: "I killed the app and reopened it twice ... my week is still last week one. Same on the second device." This is later than Douglas's Sep 16 owner claim. It is the closest call, but a QA retest on prod meets "even after a restart". [RECORD]
- F22: Hold until | A: until the fix is confirmed on prod | B: Oct 8 | Settled by: "say that instead of guessing a date"; no record ties ZOM-429 to that release. [RECORD]
- F23: Endless freeze | A: not held | B: held | Settled by: Leonard's reply "Could not get it to freeze, so I am leaving this one." [RECORD]
- F24: Quest rollover | A: in | B: held on ZOM-534 | Settled by: Leonard, the reporter: "it is good on prod now". The rule also clears it: "a reset that needs a restart". [RECORD]
- F25: Daily gift | A: in | B: held on ZOM-556 | Settled by: Vincent "claiming works and nothing is lost", and "Wrong counters". [RECORD]
- F26: Other holds | A: none | B: Season Pass, Plague Race or Endless bugs | Settled by: "Hold a beat only when ...". I found no prod enter, score or claim failure on these after a restart. ZOM-546 rests on Owen's own check, but it could not hold in any case. [RECORD]
- F27: Change-request rule | A: no hit | B: CodeRabbit criticals, or #477 | Settled by the data. Of 76 CHANGES_REQUESTED and DISMISSED reviews, the latest is match3d#303, 2025-07-16. There are none in Aug-Sep 2025 in any repo, so "cohort" needs no definition. The Aug-Sep 2024 ones are closed Domino PRs. #477: Brian "none of it is a blocker". #468: "Not a blocker for this PR". [RECORD]

**Config lock**

- F28: Lock instant | A: Fri Oct 31 00:00 UTC, so Brian misses by 7h | B: "the day before" or "no technical content lock", so his date stands and no reply follows | Settled by: spec "Season config (tiers, rewards, theme) ... locked 24h before each season opens"; calendar page "The 24h season-pass freeze". [RECORD]
- F29: Which mail | A: Sep 26 | B: Sep 22 | Settled by: "Treat Fri Oct 31 as the date I am committing to and drop the Oct 29 one". [RECORD]
- F30: New date | any time before the lock | Settled by: "moves to any time before it". This is an authorized alternative, so the rubric must not pin a date. [RECORD]

**Still to do**

- F31: Collect & Win set | A: deploy, vials, icon | B: fewer | Settled by: rc_38 "still need their final models before the event runs"; cmt_zom465_3 "does have to land before the event runs". [RECORD]
- F32: Collect & Win exclusions | A: analytics, title text, token travel and queue manager are out | B: in | Settled by: "not analytics"; cmt_zom566_1; cmt_zom526_3; nobody flagged ZOM-543 as needed. [RECORD]
- F33: Deploy owner | A: Douglas | B: Arthur | Settled by: gcal organizer douglas on "Prod backend deploy for the beta"; Arthur to Douglas in #zombie-bugs, Sep 9: "we need to deploy changes to prod server / Is that already done?"; Backend Services "Owner: Douglas". [RECORD]
- F34: Season Pass set | A: config (Brian), strip art (Oliver) | B: config owned by Julia | Settled by: rc_1 "Oliver is taking the date change"; Sep 26 mail "Same contents, same owner". [RECORD]
- F35: Endless, Plague Race | A: none | B: ZOM-465, ZOM-565, ZOM-471, ZOM-542 | Settled by: "not polish nobody flagged". Nobody flagged them as needed, so this does not rest on the owners' own "not needed" notes. [RECORD]
- F36: Quests | A: none | B: more quests and balance on Oct 13 | Settled by: Leonard on Trello: "The weekly rollover does not wait on them". [RECORD]
- F37: Daily gift frame | A: none | B: to-do | Settled by: ZOM-432 Done, and commit 41a0d814ed touches img - DailyGift.png. [RECORD]
- F38: lightSweep and store approval | A: out | B: in | Settled by: "nothing has to land for the beta"; brief "Nothing else goes in". [RECORD]

**Other writes**

- F39: Hold note | A: ZOM-429 only, owner Douglas | B: a note for Collect & Win or for held pushes | Settled by: "If a beat ends up held"; ticket assignee douglas. [RECORD]
- F40: Recommendation | A: DM to Frederick; run and hold follow the sheet | B: extra holds or email | Settled by: "back here" and "Hold a beat only when". A thread vs root difference is the same recipient, so at most a minor Clarity point. [RECORD]

## Edge values

| Item | Value | Effect at the edge |
|---|---|---|
| Release | 15:00-16:00 UTC Wed Oct 8 (18:00 Istanbul, 08:00 PDT) | Same day in every zone, start or end. First opening after it is Fri Oct 10 00:00 UTC. |
| Collect & Win count | 10 windows after the release, of 12 in the span | W1 has 1 window; W2-W4 have 3 each. |
| Lock | 00:00 UTC Oct 31 (03:00 Istanbul, 17:00 PDT Oct 30) | None. |
| Brian's date | 07:00 UTC Oct 31 (10:00 Istanbul) | Misses in every zone. The superseded Oct 29 date would have passed. |
| Season Pass | Oct 6 00:00-Oct 31 23:59; Nov 1 00:00-Nov 2 23:59 | Clipped at both ends. |
| Endless | 4 windows or 28 | This is F2. |

Weekdays verified: Oct 6 Mon, Oct 8 Wed, Oct 10 Fri, Oct 13 Mon, Oct 29 Wed, Oct 31 Fri, Nov 1 Sat, Nov 2 Sun.

## Clarity

- First-person scan: no "I'll" statements.
- Write-action gate: fails only on F1. All other readings converge on the same writes.
- Assumptions an expert needs: 1 (who tells Brian).

## Platform and known issues

- Anonymized token: PNs Beta R7 and R14 carry `[PERSON_NAME_2549]`. Copy shown with the token is correct.
- Known issues touched, none load-bearing in Reading A:
  - SC-13: Trello list name.
  - SC-15: ZOM-521 checklist.
  - SC-18: #477 state; F27 does not rely on it.
  - SC-38: Season Pass ship date; F19 rests on rc_10 and the clip rule.
  - SC-45: the Backend Services owner line is one of three sources in F33.
  - SC-57: #zm-collect-win is not visible to Julia.
- FD-2880 and FD-3785 apply to nothing here.

## Scanned

- **Inputs:** assignment, prompt, full SQL (sha matches).
- **Slack (610,468 messages flattened):**
  - Full reads, Sep 2025: #zombie-match3d, #zombie-bugs (from Sep 17), #zombie-ops, #zm-animations, #live-incidents.
  - Targeted reads: #zombie-art, #zombie-design, #company-internal, Julia's DMs with Frederick and Robert, her group DMs.
  - Term sweeps across all Julia-visible channels for each beat, deploy, lock, pivot and "still need".
- **Linear:** every open ZOM issue, all ZOM beat tickets, other teams for calendar tickets.
- **GitHub:**
  - All 76 change-request and dismissed reviews, all match3d and match3d-backend PRs since Jul 25, human review comments, open PRs.
  - Backend schedules and CDK, client NotificationManager, recent git log, ZM-Liveops-Docs.
- **Trello:** whole ZM ROADMAP board and its comments.
- **Confluence:** all 30 page titles; full reads of Live-Ops Calendar, Event Engine, Season Pass spec, GDD; deploy lines of Backend Services, CI/CD and Release Checklist.
- **Mail and calendar:** subject list of Julia's mailbox, Aug 15-Oct 1, plus the injected Brian mails in full; her calendar events in the period.
- **Drive, Docs, Sheets:** Julia-visible files changed since Sep 15, all live-ops-named files, both push sheets in full, old live-ops sheets, the Endless and icon docs, a lock and calendar term scan of all docs and sheets.
- **Snowflake:** LIVE_EVENT_PERFORMANCE and PUSH_NOTIFICATION_STATS rows for ZM3D.
- **Rules:** deep_recheck, common_errors, Eval 1 §1.2, §2.1, §2.6, WORKFLOW task authority, SEARCH, persona, catalog write tools, known issues.
