# P1 findings, rev11: Unique Ground Truth and Clarity

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

SQL reviewed: sha256 1348d287ac4a105c41b9f0bf511c6664e306adcc3cf42406688a228fd4b684e7 (hash verified). Prompt unchanged.

**Checked:** 45 sentences: prompt 6, message 6, thread reply 5, brief 28 (two new). The rev10-to-rev11 diff has 18 hunks, and I read every changed statement in full.

**Result**
- Settled: DR1, DR2, DR5.
- Narrowed, still open: DR3 (one cell, send/hold unchanged) and DR4 (both-fair candidate, now only non-C&W closes).
- Mostly settled: DR6 (reward tables closed; particle note stays conditional on Slack visibility) and DR7 (only the Weeks running cell is left).
- New text: I found no new fail-level fork. Two small residuals come from it, and both are folded into DR4 and DR7.
- Clarity: no write-action divergence, so no fail-level Clarity finding.
- Read by the letter of the setup standard, DR3 is still an unresolved fork, because a careful reader could put it in a cell. It changes no decision, write or recipient. The main session has to rule on whether that is the same material result.

Sentence labels: S = prompt, M = message, R = thread reply, B = brief. Record ids are from R/inputs/01_Universe_Inject.sql unless a path is given. New-file line numbers are given as L#.

## 1. Status of DR1 to DR7

| DR | Rev10 issue | Status | Deciding record |
|---|---|---|---|
| DR1 | how far "moves earlier" moves Brian's date | SETTLED | B26, L127: "A committed date that misses the lock moves to any time before it" |
| DR2 | C&W icon animation in Still to do | SETTLED: in | cmt_zom465_3, L210 |
| DR3 | "login calendar" as a wrong name on row 12 | CHANGED, still open, low | B12 "same beat" settles identity, not the name |
| DR4 | window close instants | CHANGED: C&W and span clips settled; other closes open | B6, B3 clip sentence |
| DR5 | Season Pass First window | SETTLED: Oct 6 00:00 UTC | B3 clip sentence |
| DR6 | reward tables, particles | Reward tables SETTLED; particles conditional | L35 "Both tables are updated." |
| DR7 | cells for a held beat | First window and Windows SETTLED; Weeks running residual | B17 follow-on sentence |

### DR1: SETTLED

`DR1 | P1 | common_errors §2 (which date) | B26 | gdocs f_7c3e91a4d2b85f60e1a9c4 | Unique Ground Truth | closed; rubric constraint only`

New text: "A committed date that misses the lock moves to any time before it and its owner is told in a reply on the mail where they committed to it."

- This is a rule source and it authorizes the whole range. Oct 29, Oct 30 and a deadline-only reply are all inside it.
- Lock: Fri Oct 31 00:00 UTC ("locked 24h before each season opens", Confluence /pages/20). Brian's Oct 31 10:00 Istanbul is 07:00 UTC, so it misses by 7h.
- Rubric constraint: it must accept any instant before Oct 31 00:00 UTC and must not lock one date.

### DR2: SETTLED, in

`DR2 | P1 | common_errors §2 (items in the set) | B20 | linear cmt_zom465_3 | Unique Ground Truth | closed`

Brian, 2025-09-30T18:13:41Z, on ZOM-465: "Marcus, the Collect & Win icon does have to land before the beta, it is the one event icon with no animation. Keep it on this ticket, the master VFX list was written before that event came in."

- Brian is a non-owner, the comment is dated after the brief, and it says "before the beta". That rules out Reading B.
- Owner stays Marcus: cmt_zom465_2 "still to do on my side"; ZOM-465 assignee is Marcus.
- It does not hold the beat: B15 "cosmetic, VFX and performance gaps ... do not hold a beat".

### DR3: CHANGED, still open, low

`DR3 | P1 | common_errors §2 (contents) | B22 "...and events by their ZM3D names"; B23 "Anything else is held, with what is missing."; R4 "the naming rule is only about wrong names." | see records | Unique Ground Truth / Clarity | low; send/hold, writes and recipients unchanged, one required cell differs`

**Change:** B12 was "(the Login Calendar row on the push sheet)". It is now "the daily gift (Login Calendar on the push sheet, same beat)".

**Records**
- gsheets data.json /sheets_spreadsheets/220/sheets/1/grid/12 (Not Ready, WIP): "Check the login calendar — fresh rewards are here!"
- The Domino tab has the same copy: /sheets_spreadsheets/73/sheets/1/grid/15.
- match3d Assets/Scripts/UI/Daily Gift/DailyGiftProgressBar.cs:180: `"Daily Gift"`.

**Reading A:** "same beat" means Frederick treats Login Calendar as the sheet's label for this beat, so it is not a wrong name. What is missing = Not Ready, WIP. Wrong-name rows = 3 (rows 4, 6, 7).

**Reading B:** "same beat" only maps the row to the beat. The copy still uses the Domino name, so B22 fails on it too. What is missing adds the name. Wrong-name rows = 4.

**Why it stays open:** "same beat" answers which beat the row belongs to. It does not answer whether the copy's name passes B22, and reading it as approval of the name is an inference. Held count is 8 under both.

**What would settle it:** a brief line on whether "login calendar" counts as a wrong name, or a rubric that neither requires nor penalises the extra note and does not count wrong-name rows.

**Basis:** SCOPE_GAP (was SILENCE).

### DR4: CHANGED, narrowed, both-fair candidate

`DR4 | P1 | deep_recheck edge values | B4 "Every window is stated in server time (UTC) as a start-end instant."; B5 "...a different instant is not." | see records | Unique Ground Truth | BOTH_FAIR_FIGURE candidate; rubric must accept either`

**Now settled by rule**
- B6: "each opening 00:00 UTC and closing 23:59 UTC on its last day". The 10 C&W windows are Oct 10-12, 13-14, 15-16, 17-19, 20-21, 22-23, 24-26, 27-28, 29-30 and Oct 31-Nov 2, each 00:00 to 23:59. This outranks runtime.exs "Wednesday midnight (end of Tuesday)".
- B3: "Clip anything that starts before or runs past that to those two instants." November season = Nov 1 00:00 to Nov 2 23:59 UTC. The last weekly window also ends Nov 2 23:59 UTC.

**Still open:** B6 covers only C&W. No rule states the close of other windows.

| Window | Reading A: next reset | Reading B: 23:59 by analogy |
|---|---|---|
| October season (clipped start Oct 6 00:00) | Nov 1 00:00 UTC | Oct 31 23:59 UTC |
| Weekly Leaderboard, Endless weekly: interior weeks | Oct 13, 20, 27 00:00 | Oct 12, 19, 26 23:59 |
| Endless daily | next day 00:00 | same day 23:59 |

**Records for A**
- B11.
- /pages/20: "production seasons reset monthly on the 1st at 00:00 UTC".
- CDK stack line 139: LEAGUES_SCHEDULE "0 0 * * 1".
- /pages/27: Endless "resets daily at 00:00 UTC and weekly on Monday 00:00 UTC".

**Record for B:** the brief's own 23:59 convention in B3 and B6. That is an analogy, not a rule, and an inference is not a kill.

**Related format difference:** B7 lists "a reset" apart from "an event window", so Endless may be stated as reset instants with no close at all. The new "usual windows" sentence calls the Leaderboard's slots windows, so the Leaderboard row does need closes.

**Both-fair check:** same decision, writes and recipients. Reading A's value is on records; Reading B's value is derived from the brief's operands. None of the five checks ranks them, and the figure changes nothing the agent does next. B5 means a rubric that locks one close would fail the other.

**What would settle it:** a brief line giving the close for every window, not just C&W.

### DR5: SETTLED

B3: "Clip anything that starts before or runs past that to those two instants." The October season opened Oct 1 (B11; #470 rc_10 "already running on prod"), so its first window clips to Oct 6 00:00 UTC. That rules out Oct 1, and Nov 1 cannot be first because the clipped October window precedes it.

### DR6: reward tables SETTLED; particle note conditional

`DR6 | P1 | common_errors §2 (items in the set) | B20 | Slack C09EVVCFHKR | Unique Ground Truth | not counted; open only if the channel is persona-visible`

- Reward tables: Douglas, 2025-09-26T16:22:44Z, new reply in the same thread (L35): "Both tables are updated." If the channel is hidden from Julia, the ask does not exist for her. If it is visible, the reply is visible too. Either way the item is out. The reply is the owner's own report, but nothing disputes it, and /pages/27 "Reward tables are re-imported from Google Sheets hourly in production" points the same way.
- Particle note, unchanged: Marcus, 2025-09-24T16:58Z: "them particles are wrong but i can come in later and modify the prefab". It is 17 minutes before the brief's created_time (17:15:22Z), and the byline is day-level "Frederick, Sep 24". So it is out by instant, in by day, and "can come in later" is not a need. No record closes it.
- Visibility is unchanged: Julia is not in the members list; is_private false, is_archived true; catalog has `slack_search_public`. Treat as unverified. I recommend not counting it unless public non-member channels are confirmed readable.

### DR7: mostly SETTLED; one cell left

`DR7 | P1 | common_errors §6.2 | M2; B17 follow-on "A held beat keeps its usual windows on its row, marked held." | brief | Clarity | NON-FAIL 3 at most, same writes`

- First window and Windows cells: settled. Weekly Leaderboard keeps Mondays Oct 6, 13, 20, 27, marked held.
- Weeks running cell: the rule says "windows", not weeks. A reader can write "W1-W4, held" or "none until the fix is confirmed". The first fits "keeps its usual windows"; ruling out the second takes an inference.
- Status, hold text, ticket note and recipient are the same under both.

**Basis:** SILENCE on that one cell. The rubric should accept either.

## 2. Forks tried in the new and changed text

| New or changed text | Reading B tried | Outcome and quote |
|---|---|---|
| B3 "Clip anything that starts before or runs past that to those two instants." | Clip touches push sends or the Oct 31 lock | No: sentence sits under windows, and neither is outside the span |
| B3 clip | Season Pass keeps Oct 1 | Killed by the sentence itself (DR5) |
| B6 "closing 23:59 UTC on its last day" | Applies to every window | Not stated; stays DR4 |
| B6 | Code close (Wed 00:00) wins | Killed: brief is the rule source, code is a fact source |
| B17 follow-on "A held beat keeps its usual windows" | C&W keeps its Oct 6 and Oct 8 windows | Killed: B10 "starts late, it is not held" |
| B17 follow-on | Leaderboard row shows no windows | Killed by the sentence itself |
| B17 follow-on | Weeks running cell | Residual, DR7 |
| B26 "moves to any time before it" | One date is required | Killed: "any time" |
| B26 | No reply needed | Killed: "its owner is told in a reply" |
| B12 "same beat" | Login Calendar is a separate beat | Killed: "same beat" |
| B12 "same beat" | Copy name still wrong | Not killed, DR3 |
| R1 "Two things on top of the brief." | B22 still needs the game name, so rows 3 and 5 hold | Killed: R4 "Copy that does not name the game at all is fine to go out" |
| R1 | M2 "which windows" adds dates to the B12 beats | Killed: B12 "not its window dates"; M5; R1 adds only pushes and Zombie Lane |
| Robert Sep 18 "one week of the beta ... if it lands in time" | Halloween stays as an overlap under B18 | Killed: DM "Take it off the beta calendar"; no art means nothing players see (B7) |
| Robert DM, "my later word" removed | His retraction loses force | Killed: B19 "his later word is the one that counts" |
| cmt_zom465_3 "does have to land before the beta" | C&W is held until it lands | Killed: B15 "cosmetic, VFX ... do not hold a beat" |
| cmt_zom465_3 | Contrast pushes vials out | Not killed by contrast alone, but see vials in section 3 |
| #472 rc_1 "premium strip art" | It is config, so the Oct 31 lock applies | No cell carries that deadline. Record says "before that season opens"; owner "Oliver is taking the date change" |
| lightSweep "rides the next store build" | Client art needs a store build, so add it to Still to do | Killed: no flag since the brief; B21 "Nothing else goes in" |
| Deck "starting once the stores approve the Sep 30 builds" | Store approval is a Still-to-do item or moves C&W's start | Killed: B9 "not when its client PRs merged"; deck is Sep 23, before the brief; B21 |
| Deck "any scale-up comes after the pivot call" | Changes what runs | No: spend only, and it removes the old slide 2 vs slide 3 conflict |
| ZOM-504, ZOM-542, ZOM-563, Trello JSON edits | Any change to a decision | None: quotes below still hold; Trello text unchanged |

## 3. Open tickets, PR notes, bug reports and Trello/Slack notes

Items that stay IN Still to do:

| Item | Owner | Record |
|---|---|---|
| C&W prod deploy | Douglas | #470 rc_10; GCal evt_5c1e83a7d94b02f6c8e31a |
| Final vial models | Claire | #468 rc_38 |
| C&W event icon animation (changed) | Marcus | cmt_zom465_2, cmt_zom465_3 |
| Season Pass premium strip art | Oliver | #472 rc_1 "It needs the November range before that season opens" |
| November config, before Oct 31 00:00 UTC | Brian | mails; /pages/20 |
| Leaderboard fix | Douglas | ZOM-429 |

**Vials, watch item:** after the DR2 fix, the vial note is the only IN art item with no explicit before-beta wording: "The final vial models are missing, Claire has those on her list." Reading B (out) is ruled out by B20 plus that flag. It is a third party's dated statement that final player-facing art is missing, and B21 excludes only "polish nobody flagged". I label it RECORD, but the main session should look at it, because the icon comment sharpens the contrast.

Everything else, with its kill:

| Item | Note | Kill (quoted) | Basis |
|---|---|---|---|
| ZOM-432 | "still needs the frame" | "The frame went out with PR #471 ... nothing is left here"; B21 "not what already shipped" | RECORD |
| ZOM-344 | Quest box animation | Done Sep 16; no flag since brief; B21 | RECORD (rule) |
| ZOM-465 description | unstruck Refill Timer | cmt_zom565_2 "the refill timer are the same P1/P2 polish ... do not have to land before the beta" | RECORD |
| ZOM-471 | red dot | Sep 17, before the brief; B20 "flagged since this brief" (Samuel's own line is not the kill) | RECORD (rule) |
| ZOM-504 | objects stay in deck | "Re-tested: it only shows up with the bot running"; "Visual only, no board state affected."; B15 | RECORD |
| ZOM-517 | enrage lost | "could not get one to lose it while walking"; B14 | RECORD |
| ZOM-546 | refill shrinks | Owen's own retest does not settle it; B13 "cannot enter, score or claim" and B20 "its fix if it is held" do | RECORD (rule) |
| ZOM-556 | daily gift no reset | "claiming works and nothing is lost"; B15 "Wrong counters" | RECORD |
| ZOM-534 | quest reset | "it is good on prod now" (reporter Leonard); B15 | RECORD |
| ZOM-563 | teams on prod | "Checked on prod: ... all work as expected. Closing." Not a beat | RECORD |
| ZOM-565 | Endless screen VFX | Brian: "can follow and do not have to land before the beta" | RECORD |
| ZOM-566, PR #477 | header and info text; analytics | "do not have to land before the beta"; B21 "not analytics". SC-18: #477 state not relied on | RECORD |
| ZOM-526 | token travel | "Only the Axe Arena travel is left here"; R3 "not in the beta" | RECORD |
| ZOM-521, 528, 541 | card VFX | "Card pack animation went in with #475"; not a beat (B7) | RECORD |
| ZOM-543 | queue manager | "plus Collect and Win", #472 merged; no flag; B21 | RECORD (rule) |
| ZOM-542 (state now Todo) | home screen | Sep 22, before the brief; B20 (owner's own "not needed" is not the kill) | RECORD (rule) |
| ZOM-544 | Apple login | not a window, reset or start push (B7) | RECORD (rule) |
| ZOM-552, 549, 442 | analytics | B21 "not analytics" | RECORD |
| ZOM-475, 359, 560, 483 | crash, heat, pack, lives | not a beat (B7); B15 "performance" | RECORD (rule) |
| match3d-backend #34 | open draft since Aug 1 | no flag, no review; B21 | RECORD (rule) |
| Trello card 61 | more quests, Mon Oct 13 | "The weekly rollover does not wait on them, the current quests keep running either way." Leonard is on the card, so the kill is B20: nobody flags it as needed | RECORD (rule); watch |
| Trello 58, 79, 54 | bug and tech lists | no flag for a beat since brief | RECORD (rule) |
| Deck store approval (new row) | Sep 30 builds | B9 "not when its client PRs merged"; B21 | RECORD (rule) |
| #zombie-bugs airstrike freeze | Sep 21 report | Leonard: "Could not get it to freeze, so I am leaving this one."; B14 | RECORD |
| #zombie-bugs lightSweep | "squeeze in the fix" | "rides the next store build and nothing has to land for the beta"; B15 | RECORD |
| #zombie-art desert and port themes | Sep 29-30 | Robert: "nothing waits on new themes." | RECORD |
| #zombie-art Halloween | Robert Sep 18 ok | DM D05GU6L0XFH "pulling my ok. Take it off the beta calendar"; B19; /pages/20 "Owner: Robert (Product)" | RECORD |
| #zombie-bugs Sep 22 leaderboard | "Killing the app doesn't help" | "yep, it's working fine right now"; superseded by the Sep 30 retest | RECORD |
| #zombie-bugs Sep 7 Endless | "didn't restart" | Douglas: "Solved, try again please" | RECORD |
| #zm-animations Marcus Sep 25 | Endless text animations | cmt_zom565_2 "endless VFX inside the core game" | RECORD |
| #zm-animations Robert Sep 30 | enrage aura | not for a beat; B20 "for it" | RECORD (rule) |
| PNs Beta row 1 | "Revisit once new quests roll out." | push cell only; Not Ready already holds it | RECORD |
| #zm-collect-win reward tables | Brian Sep 26 | "Both tables are updated." | RECORD if visible; else no item |
| #zm-collect-win particles | Marcus Sep 24 | none; see DR6 | visibility unverified |

The FC: canvas channels have no Julia membership. The Brian-to-Marcus DM (D076V3NB6P7) is hidden from Julia, so it resolves nothing.

## 4. Decisions rechecked and settled

| Decision | Result | Kill of Reading B | Basis |
|---|---|---|---|
| Leaderboard held or not | Held; note on ZOM-429 (Douglas) | Newer source: Vincent Sep 30 "killed the app and reopened it twice ... Same on the second device" beats cmt_zom429_1, the owner's own claim | RECORD |
| Other beats held | None | Rows above | RECORD |
| B16 change-request hold | Does not fire | Only 4 CHANGES_REQUESTED since May (GoD #1837, match3d #303, backend #4 twice); none Aug-Sep; SQL adds none | RECORD |
| C&W first window | Fri Oct 10 00:00 UTC; 10 windows; W1 Fri-Sun only | B9 "first window that opens after"; 15:00Z or 16:00Z gives the same result | RECORD |
| C&W status | Starts late, no ticket note | B10 | RECORD |
| Season Pass windows | Oct 6 00:00 start; Nov 1 00:00 to Nov 2 23:59 | B3 clip; October close is DR4 | RECORD |
| Lock instant | Oct 31 00:00 UTC | "locked 24h before"; /pages/27 "The 24h season-pass freeze" | RECORD |
| Mail to reply on | Sep 26 thread | "reply on this mail"; "the date I am committing to" | RECORD |
| Who tells Brian | The agent | B26 names the write; B2 and S2 give the job to Julia's side. Reply-all to Frederick is optional; Brian is the required recipient | RECORD (rule) |
| Push sheet | "Push Notifications Zombie Match" | Domino sheet has no Ready column; S1 ZM3D | RECORD |
| Push split | 10 lines: rows 3, 5 send; rows 1, 4, 6, 7, 9, 12, 13, 14 held | B22, R3, R4 | RECORD |
| Beats | C&W, Season Pass, Weekly Leaderboard/Leagues, Endless, Plague Race, quest rollover, daily gift | B7, B8, B12, R5, #470 rc_10; ZOM-544 "Weekly contest of leaderboard, the score, the league itself" | RECORD |
| Destinations | Sheet f_e4a17c90b3d25f6a8c1d73; ZOM-78; DM D05SD5QLG94 | M3; cmt_zom78_1; M4 "back here" | RECORD |

**Edge values that changed nothing:** "since this brief" at day, created and modified cutoffs for persona-visible items; span start inclusive (4 weekly resets, Nov 3 out); release at 15:00Z or 16:00Z; Istanbul vs UTC vs PT for the release.

## 5. Fork list for the report

- F3 (DR3): row 12 what is missing | status only | plus "login calendar" name | Missing: a ruling on that name.
- F4 (DR4): close of non-C&W windows | next reset 00:00 | 23:59 | Both fair if the main session agrees; rubric must accept either.
- F6 (DR6): C&W particle note | out | in | Open only if #zm-collect-win is persona-visible.
- F7 (DR7): held beat's Weeks running cell | W1-W4, held | none until fix | Missing: a brief word on weeks; rubric should accept either.

Closed since rev10: F1 by B26, F2 by cmt_zom465_3, F5 by the B3 clip sentence.

Rubric constraints from this round: accept any instant before Oct 31 00:00 UTC for Brian's new date, and do not count wrong-name rows.

## 6. Topic lines and platform notes

- Unique Ground Truth: findings above.
- Clarity: no fail-level finding; DR7 only.
- Platform: `[PERSON_NAME_2549]` in PNs Beta rows 6 and 13 is the source string, not a copy defect.
