# P1 findings: Unique Ground Truth and Clarity

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

**Checked:** 43 sentences: prompt 6, Frederick's message 6, thread reply 5, brief 26. Every sentence was read against the base data plus the SQL overlay.

**Result:** 7 entries.
- 3 open forks: DR1, DR2, DR3.
- 2 both-fair candidates: DR4, DR5.
- 1 fork that depends on Slack visibility: DR6.
- 1 minor Clarity item: DR7.

**The core decisions are settled by records:** hold set, send/hold split, first C&W window, lock instant, reply thread, tickets and destinations (section 3).

**Clarity:** no write-action divergence survived, so there is no fail-level Clarity finding.

Sentence labels: S = prompt, M = message, R = thread reply, B = brief. Record ids are from R/inputs/01_Universe_Inject.sql unless a path is given.

## 1. Findings

### DR1: how far "moves earlier" moves Brian's date

`DR1 | P1 | common_errors §2 (which date) | B26 "A committed date that misses the lock moves earlier and its owner is told in a reply on the mail where they committed to it." | see records below | Unique Ground Truth | fail-level unless the main session accepts "before its lock" as the acceptance boundary`

**Records**
- Confluence /pages/20 (page_season_pass_spec): "Season config (tiers, rewards, theme) is authored in the live-ops tool and locked 24h before each season opens". B11 gives the open as the 1st at 00:00 UTC, so the lock is Fri Oct 31 00:00 UTC.
- Julia's copy of the Sep 26 mail, thread julia.lawson@harmonygames.co/1844311412966040123: "moves from Wed Oct 29 to Fri Oct 31, 10:00 Istanbul time"; "I just need the two extra days on the premium track"; "Treat Fri Oct 31 as the date I am committing to and drop the Oct 29 one."
- Julia's copy of the Sep 22 mail, thread julia.lawson@harmonygames.co/1843954828968533812: "The config handoff we agreed with Product is for Wed Oct 29".
- Confluence /pages/6: "Event definitions ... Design (Julia Lawson)". The handoff reaches Julia, and the config still has to be authored before the lock.

**Reading A:** move to the last workable point before the lock. Sheet and reply say Thu Oct 30 or "before Oct 31 00:00 UTC".

**Reading B:** go back to the date agreed with Product, Wed Oct 29. Sheet and reply say Oct 29.

**Edge values**

| Value | UTC | Margin to lock |
|---|---|---|
| Brian's date as committed | Oct 31 07:00 | misses by 7h |
| A, latest instant | Oct 30 23:59 | 1 min |
| A, same clock one day earlier | Oct 30 07:00 | 17h |
| B, end of Oct 29 Istanbul | Oct 29 20:59 | 27h01 |
| B, end of Oct 29 UTC | Oct 29 23:59 | 24h01 |

All four replacement dates clear the lock. The mail and sheet contents differ.

**Looked for a settling record:** none names the new date. "Drop the Oct 29 one" is Brian's own wording, and the brief overrides his date, so it does not kill B. B2 "the calls are yours" and B25 "lands before its lock" support a range, not one date.

**Both-fair:** the same-writes conditions hold. Oct 29 is on a record, but Oct 30 is not stated anywhere, so condition 2 holds only if the leading value is "before Oct 31 00:00 UTC", derived from the spec.

**What would settle it:** a brief sentence saying where the date moves to, or a decision that any instant before Oct 31 00:00 UTC is correct. In the second case the rubric must accept both.

**Basis:** SILENCE.

### DR2: is Marcus's C&W icon animation a Still-to-do item

`DR2 | P1 | common_errors §2 (which items are in the set) | B20 "anything flagged since this brief as still needed for it (prod deploy, config or player-facing art)" | see records below | Unique Ground Truth | fail-level under the setup standard (SCOPE_GAP)`

**Records**
- cmt_zom465_2 (Marcus, ZOM-465, 2025-09-30T18:05:02Z): "The Collect & Win event icon animation is still to do on my side, the other event icons are finished."
- Polish items that are out carry an explicit line, and this one does not:
  - cmt_zom565_1: "it is not needed for the beta"
  - cmt_zom566_1: "do not have to land before the beta"
  - cmt_zom526_2: "does not have to land before the beta"
- B15: "cosmetic, VFX and performance gaps" (this governs holds only).
- B21: "not polish nobody flagged".

**Reading A:** in. It is player-facing art, flagged after Sep 24. C&W Still to do has 3 items: deploy (Douglas), vials (Claire), icon animation (Marcus).

**Reading B:** out. "Still to do on my side" is a work note. Nobody says it must land "before it runs for bought users" (B20). An idle icon animation is cosmetic polish. C&W Still to do has 2 items.

**Edge:** the comment is after the brief under every cutoff (date, created 17:15:22Z, modified 17:40:52Z), so the timing edge changes nothing.

**Looked for a settling record:** no other record covers this animation. PR #475 is the card pack, and cmt_zom465_1 is corrected by c2. A rule-based argument for A exists: B21's "polish nobody flagged" implies flagged polish stays in. That is an inference, and the only flag is the owner's own.

**Related:** #468 rc_38 says the final vial models "are missing", also without a before-beta statement. It is a third party's flag, so I treat it as in.

**What would settle it:** a dated line from Brian, Robert or Frederick that the icon animation must or need not land before the beta.

**Basis:** SCOPE_GAP.

### DR3: is "login calendar" a wrong event name on row 12

`DR3 | P1 | common_errors §2 (contents) | B22 "...names the game as Zombie Match 3D and events by their ZM3D names"; B23 "Anything else is held, with what is missing." | see records below | Unique Ground Truth / Clarity | low; send/hold unchanged, one required cell differs`

**Records**
- gsheets data.json /sheets_spreadsheets/220/sheets/1/grid/12 (Not Ready, WIP): "Check the login calendar — fresh rewards are here!"
- The Domino tab has the same copy: /sheets_spreadsheets/73/sheets/1/grid/15.
- Client string: match3d Assets/Scripts/UI/Daily Gift/DailyGiftProgressBar.cs:180 `"Daily Gift"`.
- B12: "the daily gift (the Login Calendar row on the push sheet)".

**Reading A:** what is missing = Not Ready, WIP. Wrong-name rows = 3 (rows 4, 6, 7).

**Reading B:** also the copy's old event name. Wrong-name rows = 4.

Held count is 8 under both. B12 labels the row but does not rule on the copy. Row 14 ("Weekly Rankings") is not a parallel case, because its body says "leaderboard".

**What would settle it:** a brief line on whether "login calendar" is a wrong name, or a rubric that does not count wrong-name rows.

**Basis:** SILENCE.

### DR4: window close instants (both-fair candidate)

`DR4 | P1 | deep_recheck edge values (cutoff included or excluded) | B4 "Every window is stated in server time (UTC) as a start-end instant."; B5 "...a different instant is not." | see records below | Unique Ground Truth | BOTH_FAIR_FIGURE candidate; rubric must accept either`

**Records**
- match3d-backend config/runtime.exs:215-219: "Wednesday midnight (end of Tuesday)", "Friday midnight (end of Thursday)", "Monday midnight (end of Sunday)".
- lib/zombies_game/win_and_collect.ex:77-81: `hours_since_monday < 48 / 96 / 168`.
- B3: "Sun Nov 2 23:59 UTC". B6 gives only the opening time.

| Window | Reading A: next-opener close | Reading B: 23:59 close |
|---|---|---|
| First C&W window, Oct 10 00:00 | Oct 13 00:00 | Oct 12 23:59 |
| Last C&W window, Oct 31 00:00 | Nov 3 00:00 (past the span) | Nov 2 23:59 |
| October season | Nov 1 00:00 | Oct 31 23:59 |
| November season | Dec 1 00:00 | Nov 30 23:59, or clipped to Nov 2 23:59 |

All 10 C&W windows have the same one-minute difference. Decision, writes and destinations are the same.

Note: B5 makes a rubric that locks one close instant fail the other, so the rubric must accept both.

**What would settle it:** B6 stating the close.

### DR5: Season Pass "First window (UTC)" cell (both-fair candidate)

`DR5 | P1 | deep_recheck edge values | B9 "A beat starts with the first window that opens after its server windows are live on prod"; B3 "The calendar covers Mon Oct 6 00:00 UTC..."; B11 | see records below | Unique Ground Truth | BOTH_FAIR_FIGURE candidate; low`

**Records**
- #470 rc_10: "Season Pass schedules are already running on prod."
- #472 rc_1: "still set to the October range".
- Brian's mails: "opens on Sat Nov 1".

**Values:** Oct 1 00:00 UTC (season running at span open), Oct 6 00:00 UTC (clipped to span), or Nov 1 00:00 UTC (first opening inside the span). B9 leans to Oct 1, but it does not say whether the calendar reports a pre-span window. Only this cell differs, and Nov 1 appears in the Windows cell under every reading.

**What would settle it:** a brief line on pre-span windows.

### DR6: Brian's reward-table request (depends on Slack visibility, not counted yet)

`DR6 | P1 | common_errors §2 (which items are in the set) | B20 "...(prod deploy, config or player-facing art)" | Slack C09EVVCFHKR thread 1758899400.476649 | Unique Ground Truth | open only if the channel is persona-visible`

**Records**
- Brian, 2025-09-26 15:10Z: "@Douglas I Also changed 1 reward in each of the two reward tables. Could you update them?" No reply in the thread.
- Same channel, Marcus, 2025-09-24 16:58Z: "them particles are wrong but i can come in later and modify the prefab". This is 17 minutes before the brief's created_time, so it is out by instant and in by date.

**Visibility:** Julia is not in the channel's members list. The channel is is_private false and is_archived true, and the catalog has `slack_search_public`. Under ENVIRONMENT.md membership rules this is hidden, or at best "unverified". SC-57 also warns about this channel.

**If visible**
- Reading A: not in Still to do.
- Reading B: add "Douglas applies the two reward-table changes" as config.
- Nearest kill: Confluence /pages/27, "Reward tables are re-imported from Google Sheets hourly in production", plus the `import_win_and_collect_rewards` job at config/runtime.exs:292. That is a general statement, not about this request, so the label would be SCOPE_GAP. SC-62 only bars grading the cadence.

**What would settle it:** confirm how public non-member channels behave, or a Douglas reply.

### DR7: cells for a held beat (Clarity, minor)

`DR7 | P1 | common_errors §6.2 | M2 "which windows it runs in, if anything is held and until when" | B17 "A hold with no dated fix runs until the fix is confirmed on prod; say that instead of guessing a date." | Clarity | NON-FAIL 3, same writes`

For the Weekly Leaderboard, the First window, Windows and Weeks running cells could show either:
- the scheduled Mondays (Oct 6, 13, 20, 27; CDK stack line 139) with Status Held, or
- nothing until the fix is confirmed.

The status, hold text, note and recipient are the same under both.

**Basis:** SILENCE.

## 2. Open tickets, PR notes, bug reports and Trello/Slack notes

Items that stay IN Still to do, each from a record:

| Item | Owner | Record |
|---|---|---|
| C&W prod deploy | Douglas | #470 rc_10; GCal evt_5c1e83a7d94b02f6c8e31a |
| Final vial models | Claire | #468 rc_38 |
| Season Pass premium strip | Oliver | #472 rc_1 |
| November config | Brian | mails above |
| Leaderboard fix | Douglas | ZOM-429 |

Everything else, with its kill:

| Item | Note | Kill (quoted) | Basis |
|---|---|---|---|
| ZOM-432 | "still needs the frame" | "The frame went out with PR #471 ... nothing is left here"; B21 "not what already shipped" | RECORD |
| ZOM-344 | Quest box animation | Done Sep 16; no flag since brief; B21 "Nothing else goes in" | RECORD (rule) |
| ZOM-465 description | unstruck Refill Timer animation | cmt_zom565_2 "the refill timer are the same P1/P2 polish ... do not have to land before the beta" | RECORD |
| ZOM-465 c2 | C&W icon animation | none, see DR2 | SCOPE_GAP |
| ZOM-471 | red dot | Sep 17, before the brief; B20 "flagged since this brief" (Samuel's own "nothing here has to land" is not the kill) | RECORD (rule) |
| ZOM-504 | objects stay in deck | "Visual only, no board state affected."; B15 "cosmetic" | RECORD |
| ZOM-517 | enrage lost | "could not get one to lose it while walking"; B14 | RECORD |
| ZOM-546 | refill shrinks | Owen's own retest does not settle it; B13 "cannot enter, score or claim" and B20 "its fix if it is held" do | RECORD (rule) |
| ZOM-556 | daily gift no reset | "claiming works and nothing is lost"; B15 "Wrong counters" | RECORD |
| ZOM-534 | quest reset | "it is good on prod now" (reporter Leonard); B15 "a reset that needs a restart" | RECORD |
| ZOM-563 | teams on prod | "all work as expected. Closing." Not a beat | RECORD |
| ZOM-565 | Endless screen VFX | Brian: "can follow and do not have to land before the beta" | RECORD |
| ZOM-566, PR #477 | header and info text; analytics | "do not have to land before the beta"; B21 "not analytics". SC-18: #477 state not relied on | RECORD |
| ZOM-526 | token travel | "Only the Axe Arena travel is left here"; R3 Axe Arena "not in the beta" | RECORD |
| ZOM-521, 528, 541 | card VFX | "Card pack animation went in with #475"; not a beat (B7) | RECORD |
| ZOM-543 | queue manager | "plus Collect and Win", #472 merged; no flag; B21 | RECORD (rule) |
| ZOM-542 | home screen | Sep 22, before the brief; B20 (owner's own "not needed" is not the kill) | RECORD (rule) |
| ZOM-544 | Apple login | not a window, reset or start push (B7) | RECORD (rule) |
| ZOM-552, 549, 442 | analytics | B21 "not analytics" | RECORD |
| ZOM-475, 359, 560, 483 | crash, heat, pack, lives | not a beat (B7); B15 "performance" | RECORD (rule) |
| match3d-backend #34 | open draft since Aug 1 | no flag, no review; B21 | RECORD (rule) |
| Trello card 61 | more quests, Mon Oct 13 | "The weekly rollover does not wait on them, the current quests keep running either way." Leonard is on the card, so the kill is B20: nobody flags it as needed | RECORD (rule); watch |
| Trello 58, 79, 54 | bug and tech lists | no flag for a beat since brief | RECORD (rule) |
| #zombie-bugs airstrike freeze | Sep 21 report | Leonard: "Could not get it to freeze, so I am leaving this one."; B14 | RECORD |
| #zombie-bugs lightSweep | "squeeze in the fix" | "nothing has to land for the beta"; B15 "cosmetic" | RECORD |
| #zombie-art desert and port themes | Sep 29-30 | Robert: "nothing waits on new themes." | RECORD |
| #zombie-art Halloween | Robert Sep 18 ok | Robert DM D05GU6L0XFH: "pulling my ok. Take it off the beta calendar"; B19; Product = Robert per /pages/20 "Owner: Robert (Product)" | RECORD |
| #zombie-bugs Sep 22 leaderboard | "Killing the app doesn't help" | "yep, it's working fine right now"; superseded by the Sep 30 retest | RECORD |
| #zombie-bugs Sep 7 Endless | "didn't restart" | Douglas: "Solved, try again please" | RECORD |
| #zm-animations Marcus Sep 25 | Endless text animations | cmt_zom565_2 "endless VFX inside the core game" | RECORD |
| #zm-animations Robert Sep 30 | enrage aura | not for a beat; B20 "for it" | RECORD (rule) |
| PNs Beta row 1 | "Revisit once new quests roll out." | push cell only; Not Ready already holds it | RECORD |
| #zm-collect-win items | reward tables, particles | see DR6 | visibility unverified |

The FC: canvas channels have no Julia membership, and the C&W canvas lists depend on them. Vincent, in #zm-collect-win: "none of them blockers". The Brian-to-Marcus DM (D076V3NB6P7) is hidden from Julia, so it resolves nothing.

## 3. Decisions checked and settled

| Decision | Result | Kill of Reading B | Basis |
|---|---|---|---|
| Leaderboard held or not | Held; note on ZOM-429 (Douglas) | Newer source: Vincent Sep 30 "killed the app and reopened it twice ... Same on the second device" beats cmt_zom429_1, which is the owner's own claim | RECORD |
| Other beats held | None | Rows above | RECORD |
| B16 change-request hold | Does not fire | Only 4 CHANGES_REQUESTED since May (GoD #1837, match3d #303, backend #4 twice); none Aug-Sep; #468 rev_3 is COMMENTED, #470 rev_9 is APPROVED; SQL adds none. The undefined "cohort" changes nothing | RECORD |
| C&W first window | Fri Oct 10 00:00 UTC; 10 windows; W1 is Fri-Sun only | B9 "first window that opens after"; GCal 15:00Z or 16:00Z gives the same result | RECORD |
| C&W status | Starts late, no ticket note | B10 | RECORD |
| Lock instant | Oct 31 00:00 UTC | "locked 24h before"; /pages/27 "The 24h season-pass freeze"; "the day before" cannot rescue 07:00 UTC | RECORD |
| Mail to reply on | Sep 26 thread | "reply on this mail"; "the date I am committing to" | RECORD |
| Who tells Brian | The agent | B26 names the form of the write; B2 and S2 give the job to Julia's side. Passive voice is the only weakness | RECORD (rule) |
| Push sheet | "Push Notifications Zombie Match" | Domino sheet has no Ready column; S1 ZM3D | RECORD |
| Push split | 10 lines: rows 3, 5 send; rows 1, 4, 6, 7, 9, 12, 13, 14 held | B22, R3, R4 | RECORD |
| Beats | C&W, Season Pass, Weekly Leaderboard/Leagues, Endless, Plague Race, quest rollover, daily gift | B7, B8, B12, R5, #470 rc_10. Leagues = weekly leaderboard per ZOM-544 "Weekly contest of leaderboard, the score, the league itself" | RECORD |
| M2 windows vs B12 no dates | B12 applies | M5 and R1 point to the brief | RECORD |
| Destinations | Sheet f_e4a17c90b3d25f6a8c1d73; ZOM-78; DM D05SD5QLG94 | M3; cmt_zom78_1; M4 "back here" | RECORD |

**Edge values that changed nothing**
- "Since this brief" at day, created and modified cutoffs.
- Span start inclusive: 4 weekly resets, and the Nov 3 reset is out.
- Release at 15:00Z or 16:00Z.
- Istanbul vs UTC vs PT for the release.

## 4. Fork list for the report

- F1 (DR1): Brian's new date | before the lock, about Oct 30 | back to Oct 29 | Missing: a brief line on where the date moves to.
- F2 (DR2): C&W icon animation | in Still to do | out | Missing: a dated non-owner line that it is or is not needed for the beta.
- F3 (DR3): row 12 what is missing | status only | plus "login calendar" name | Missing: a ruling on that name.
- F4 (DR4): window close instants | next-opener 00:00 | 23:59 | Both fair if the main session agrees; rubric must accept either.
- F5 (DR5): Season Pass first window | Oct 1 | Oct 6 or Nov 1 | Both fair if the main session agrees; rubric must accept either.
- F6 (DR6): C&W reward tables | out | in | Open only if #zm-collect-win is persona-visible.

## 5. Topic lines and platform notes

- Unique Ground Truth: findings above.
- Clarity: no fail-level finding; DR7 only.
- Platform: `[PERSON_NAME_2549]` in PNs Beta rows 6 and 13 is the source string, not a copy defect.

Run note: R/work is shared with other reviewers, and one of my helper scripts there was overwritten mid-run. I moved to R/work/p1a and re-read the affected ticket. No finding depends on the overwritten file.
