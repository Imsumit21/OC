# Census slice: bug and failure reports touching a beat (#zombie-bugs, #zombie-match3d), Jul 15 2025 to the clock

Base read-only. All times UTC. "J" = Julia can read it (she is EMPLOYEE_0005_SLACK_ID, a member of both channels, #zombie-design, #live-incidents, #builds, #god-bugs, #company-internal). "not J" = she cannot.

Headline findings:
- The platform's "no follow-up" on the S23 report is true of the thread only. Follow-ups exist elsewhere, Julia can read them, and they make the fork worse: Vincent Sep 22 calls it a Samsung-specific "airstrike freeze" he has not seen.
- Five new items were in no earlier review: Robert's Sep 10 Endless end-screen freeze with ZOM-559, Robert and Julia's quest-table request, the Sep 30 reward box shader, ZOM-563 (premium golden frames on prod), and the client-crash owner question on the leaderboard.
- ZOM-534 has a non-owner record no reviewer cited: the build bot in #builds shows the fix in the Sep 11 store submission builds.

## 1. Coverage

| Container | Period | Messages | Threads with replies | Reading |
|---|---|---|---|---|
| #zombie-bugs C08R27X0EAH | Jul 15 to last message Sep 30 17:42 | 2351 (Jul 442, Aug 812, Sep 1097); 1563 thread replies read, a few of them before Jul 15 in the same threads | 163 (1 started before Jul 15, read whole) | Every line, in order |
| #zombie-match3d C0880U9751A | Jul 15 to last message Sep 30 16:04 | 1500 (Jul 592, Aug 435, Sep 473); 1006 thread replies read, some before Jul 15 in the same threads; plus 1 injected row (Vincent Sep 30) | 130 (6 started before Jul 15, read whole) | Every line, in order |

No message in either channel is dated after Sep 30. Rev 8 SQL inserts only b5f2955c into these two channels.

Read for context, not in the slice:
- #zombie-design Sep 19-30, in full.
- #live-incidents Jul 15-Sep 30.
- #executives Sep 20-23 and Sep 28 (not J).
- DM D079SNE2TL4 Vincent/Douglas, Aug 13 and Sep 20-30 (not J).
- DM D04UGG61DUM Jul 30 and Sep 27-29 (not J).
- Canvas comment channels Bug Checklist, Endless Horde Issues, Season Pass Issues - ZM, Collect&Win issues and Crasyltyics Bugs (all not J; most checklist bodies export empty).
- All-Slack regex searches: samsung/galaxy/s2x, airstrike, plague, quest, golden/season pass/deploy, friend, ZOM-429/534/563.
- All ZOM Linear titles touching a beat, and every ZOM ticket created since Sep 10.
- match3d and match3d-backend git logs.
- Economy sheet Daily Quests tab.
- Trello quest card.

Not scanned or not readable:
- 372 + 196 Slack attachments (video/images; file records carry no content), so reports that live only in a video or image are known only from their text. The Sep 30 box image is one.
- Slack bot attachments were read truncated to 400 characters.
- Gmail, GCal, Drive and Confluence were not scanned for this slice.
- Universe_Normal was not read, so nothing after Oct 1 is known.

Out of scope by your list, so not itemised: core-level, FTUE, Zombie Lane, Boss Arena, Teams-only, tooling and editor reports.

## 2. Unsettled candidates, ranked

Same fields as the brief, as labelled blocks because the cells are long.

### U1. Endless: Leonard's Sep 21 S23 air-strike freeze
- **Where:** #zombie-bugs, msg id ede90bc6ec6cb16fd97663f2888f39a2, ts 1758420497.482989, Leonard, Sep 21 02:08. "Bug endless mode. Tried to use [USERNAME_25225] the screen froze.  Samsung galaxy s23 ultra - production build". reply_count 0, no reactions, no files.
- **Reader's use:** Endless Still to do gets "verify the Samsung S23 freeze" under "an unverified build or platform is a still-to-do".
- **Basis:** Still-to-do call is SCOPE_GAP. Hold call is RECORD: not held, because Robert Sep 24 (J) says "had to restart his app... Once Leonard's friend restarted, his log just continued to the next level".
- **Julia-readable follow-ups the platform did not cite:**
  - Vincent, #zombie-design, Sep 22 18:00, ts 1758564051.199019: "I think we have problems specific to Samsung devices. Just like glass vfx issues, I haven't experienced the airstrike freeze, notification muting the game." This also resolves the anonymised token to air strike (my inference).
  - Robert, #zombie-bugs, Sep 24 18:32, ts 1758738754.255909: "Leonard also had a friend, that had his game froze for good, and had to restart his app. This was during his first attempt at endless mode level. The log registered NOTHING."
  - Robert, #zombie-design, Sep 23 16:48: "@Vincent Parker Leonard's friend *[IDENTIFIER_2104]*" (a user id handed to QA; no result posted).
- **Base truth:** see section 3. Never re-tested, never ticketed, no fix commit.
- **Best settling record:** thread reply on that message, and update the parent's reply_count, latest_reply and thread_ts_legacy.
  - Author: Leonard.
  - Window: Sep 28 to Sep 30 is the most natural (Android 0.3.133 was the latest by Sep 28); hard limits are after Sep 21 02:08 and before the clock.
  - Outcome that fits the base and Reading A: re-ran Endless with air strike on an S23 Ultra on the live Android build, no freeze; the original was his friend's first run and a restart cleared it; nothing to land.
  - It must not claim a root cause or a fix, because none exists.
  - It should name Samsung broadly enough to answer Vincent's "specific to Samsung devices".

### U2. Endless: Robert's Sep 10 hard freeze at the end screen, and ZOM-559
- **Where:**
  - #zombie-bugs, id 51696f3621eb437b78c6fa36088720cd, ts 1757467270.178829, Robert, Sep 10 01:21: "I finished endless horde for the 3rd time, and on the third time my game hard froze at this screen". Replies are Robert's only: "I had to manual force quit", "I'm sure the game is frozen for good", then a tag to EMPLOYEE_0032, no answer.
  - Sep 11 02:41, ts 1757558514.626259: "On android, if I home out during a level, and home back in, my sound completely disappears. And if I were to finish a level, I hard freeze at end game victory screen", then "So Android version is unstable and should not be released".
  - Linear ZOM-559 (Todo, Oliver, created Sep 22 by Vincent, never updated): "Doesn't happen to me, might be again a Samsung issue but I need to see video".
- **Reader's use:** the same clause, with stronger wording than the S23 report because an open ticket says "might be again a Samsung issue". Endless Still to do gets "verify the end-screen freeze on Samsung (Oliver, ZOM-559)". A reviewer who sees U1 settled will look here next.
- **Basis:** SILENCE on the freeze. Robert Sep 25 (ts 1758823142.221059) addresses only the audio half: "I think on Samsung devices, when you trigger that prompt... it disables the audio", "It could very well be an OS bug that we can't fix."
- **Base truth:** test build at the time (Leonard calls 0.3.35 the build under test on Sep 10). Android; Robert's phone is a Samsung S25 Ultra (DM Aug 14, not J; his "Device care" recordings show Samsung in J). Force quit recovered it, so not a hold. Nothing after Sep 11 mentions the freeze; no fix commit found.
- **Best settling record:** Linear comment on ZOM-559, Sep 25-Sep 30, by Robert (reporter, the device) or Oliver (assignee). Outcome: re-test on the live Android build shows no end-screen freeze, audio is the OS permission prompt, nothing to land for the beta. Mention Endless explicitly, since the Sep 10 report has no ticket.

### U3. Quest rollover: "Match boss buster" quests and "bosses killed"
- **Where:**
  - #zombie-bugs, id 1c201f83d18f495f5dc91093c7ba5452, ts 1758580854.440599, Robert, Sep 22 22:40: "Match boss buster items needs to be removed from quest".
  - id b6fdd1cc59f15c0ff1ac484dbdc9b6c9, ts 1758637301.299449, Julia, Sep 23 14:21: "And adjust bosses killed because we're using the trick to make all zombies bosses".
  - Both top-level, no replies, no ticket.
- **Reader's use:** Quest rollover Still to do gets "remove the boss buster quests, adjust the bosses-killed counts (config)". This is Julia's own message, and config is in the brief's still-to-do list.
- **Basis:** SILENCE. The injected Trello comment ("The rollover does not wait on them, the current quests keep running either way") covers more quests, not removing a quest players cannot finish.
- **Base truth:** "Zombie Match Economy 1.0 / Daily Quests" still has "Match 50/100/150 Boss Buster Items" and "Kill 5/10/20 Bosses" in the export (Brian's sheet, shared_with empty, so not J). Levels have no boss busters: Robert Sep 4, #zombie-match3d, "I didn't see any levels where [token] is not 0", and Sep 10 "var c is the base now". No commit or ticket follows.
- **Best settling record:** smallest change is to extend the injected Trello comment 68dac8204f1e9a3b7c2d5e61 on card 68c452a0 ("Add more quests and balance quest rewards - (Leonard/Douglas)", dated Sep 29, after both messages): the boss buster and bosses-killed quest changes go in with the same batch and the rollover does not wait on them. Do not say the rows were removed; the sheet still has them.

### U4. Quest chests and other reward chests: Sep 30 reward box shader
- **Where:** #zombie-bugs, id d0dd5d3ad4658add1f79802e2aa60e48, ts 1759249488.495439, Vincent, Sep 30 16:24: "i think we should squeeze in the fix for that issue if it's an easy fix. annoying and players can see that for 10 times in a day if they make it that far." Thread:
  - Marcus: "them old shaders dont deform no more the sprites with bones, so i had There a lightSweep Box Variant material".
  - Oliver 17:41: "will work on this asap".
  - Vincent 17:42: "I think [Oliver] will handle the problem".
- **Reader's use:** Quest rollover, Daily gift or Endless Still to do gets "reward box animation fix (Oliver)", under "player-facing art an owner has flagged". The fork is on the record of the day before the clock.
- **Basis:** SILENCE. No reply after 17:42. #builds shows later builds but no line names this fix.
- **Base truth:** commit 25c6c66b6b (Oliver, Sep 30 21:20) adds keyword SKINNED_SPRITE to lightSweep Box Variant.mat, but its message is about level popups. It landed after iOS Submission #50 (started 18:43) and Android Submission #135 (started 18:45), so it is on main and in neither submission build ("iOS 50 and Android 135" in Samuel's injected ZOM-432 note). Unity 6000.2.6f1 merged Sep 29. Same on-main-not-submitted shape as ZOM-534.
- **Best settling record:** thread reply by Vincent (asked for it) or Oliver, Sep 30 21:21 to Oct 1 06:59. Outcome: fixed on main, missed today's submission builds, cosmetic, rides the next client build, nothing waits on it. Without "nothing waits on it" it remains a flagged-art still-to-do.

### U5. Season Pass: ZOM-563 and Vincent's Sep 16 prod deploy to-do
- **Where:**
  - #zombie-bugs, ts 1758031982.956109, Vincent, Sep 16 14:13, To Dos: "Deploy teams and profile changes to prod (about premium pass avatar & frames etc) @Douglas".
  - Linear ZOM-563, In Progress, Douglas, created Sep 23, updated Sep 30 18:14: "Teams' lives, golden frames and names not working on prod env". "It works great in dev env, but in prod it doesn't."
- **Reader's use:** Season Pass Still to do gets "premium golden frames/names to prod (Douglas)". It is literally a prod deploy for a paid perk.
- **Basis:** SILENCE for Julia. No J record closes it.
- **Base truth:** closed in a DM she cannot read. D079SNE2TL4 Sep 30 18:16 Douglas: "I updated the prod environment with the latest teams/social changes, let me know if you are still getting those issues"; 21:58 Vincent: "Yep it works as expected". Known issue SC-16 names ZOM-563 as open after the fix was confirmed in DMs. SC-16 tells graders not to grade status; it does not stop a reviewer raising the fork.
- **Best settling record:** Linear comment on ZOM-563 by Vincent, Sep 30 21:58 to Oct 1 06:59, near the DM words, optionally state Done with completed_at. True to the base as written.

### U6. Quest rollover: ZOM-534 on main vs prod (platform item, new evidence)
- **Where:**
  - #zombie-bugs ts 1752624425.286219 (Leonard Jul 16, first report; "killing the app forces a refresh and fixes it").
  - ts 1757289825.998289 (Leonard Sep 8: "They only got reset after I kill the app and restarted it... this is on production").
  - ts 1757548457.699419 (Oliver Sep 10: "pushed a fix for the quests reset bug").
  - ts 1757548540.713749 (Leonard: "it's hard to test on prod without waiting a day - if you feel confident let's just take it in lol").
  - ts 1757548990.218989 / 1757549002.157479 (Oliver: "yeah its on main", "settings resets to 1 minute on dev").
- **Reader's use:** "ZOM-534 fix to prod (Douglas)". Separately, Douglas's "keeping this open to watch one backend timing edge case" could read as an open item.
- **Basis:** SCOPE_GAP as the platform ruled, but a Julia-readable non-owner chain exists:
  - #builds, Match 3D iOS Submission #36, ts 1757550527.308879, Sep 11 00:28: "Using remaining-time endpoint to sync quests end with client".
  - Android Submission #119, ts 1757550766.189709, Sep 11 00:32.
  - Leonard Sep 11 03:31: "submitted to app store".
  - Leonard Sep 17: "1.3.38 is out!".
  - Inferential, and nobody re-tested on prod in a J record.
- **Base truth:** it is a client fix (commit 47c65623e7, Oliver, Sep 10), not backend, so Arthur's "next backend release" line does not apply. Leonard, #executives Sep 11 01:04 (not J): "my quest points are reset". Oliver and Douglas tested it on dev.
- **Best settling record:** comment on ZOM-534 by Oliver or Vincent, after Sep 25 16:35: the sync is client side, went out with the Sep 11 submission builds, is on prod now; the backend edge case does not gate the rollover.

### U7. Weekly Leaderboard: who owns the fix (client crash vs ZOM-429 assignee)
- **Where:**
  - #live-incidents thread 1756469671.477659, Aug 29, Vincent: "my problem with leaderboard persists... I'm getting that error in every new session now", then a stack in `LeaderboardEvent`, `HandleWeeklyEnd`; Calvin: "Okay let me check on that".
  - #zombie-bugs ts 1758546048.524829, Vincent Sep 22: "After fixes for the crashlytics issues, I cannot participate in leaderboard. Killing the app doesn't help", citing Crashlytics "Issue 1 @Oliver Brooks", "It happens when players are not in the weekly leaderboard".
  - Oliver ts 1758548804.266909: "I reverted the changes".
  - Vincent ts 1758550789.777509: "yep, it's working fine right now".
- **Reader's use:** Still to do owner is Oliver or Calvin (client code) rather than Douglas (ZOM-429 assignee). Hold-until wording could name the reverted crash fix.
- **Basis:** SCOPE_GAP. The ticket assignee is a record, but nothing links ZOM-429 to the client crash or says who owns it after the revert.
- **Base truth:** commit 70571e610c (Sep 19) added safety checks; 49211bd82f (Sep 22) reverted them, so the crash fix is not in. ZOM-429 last updated Sep 22, Backlog, Douglas. The Sep 22 failure was on a test build and cleared on revert. It does not contradict the injected Sep 30 prod re-test.
- **Best settling record:** if you want one, a line on ZOM-429 from Vincent dated with his Sep 30 re-test saying Douglas keeps it. Otherwise have the rubric accept the ticket assignee and treat the crash as separate.

### U8. Plague Race: bots stuck
- **Where:** #zombie-bugs ts 1754645673.290909, Vincent Aug 8: "Stage 2 bots are at the same step, I can restart the race even though it's already completed... bots' scores are also persistent". Douglas ts 1754698719.078019, Aug 9: "The Plague race also restarted. I'm just debugging the bots' behavior". Nothing further.
- **Reader's use:** Plague Race Still to do gets "bot behaviour (Douglas)".
- **Basis:** SCOPE_GAP. Vincent Aug 29 "endless and plague race is working now" covers the daily refresh, not bots.
- **Base truth:** no later bot report in either channel; backend "Plague race economy changes" Sep 12. Leonard, #live-incidents Aug 23 (J), relays a player: "Plague race is also bad again now, it immediately says that I was first and can claim, but when I click it, the game hasn't counted any levels at all". No reply. Weak.
- **Best settling record:** probably none needed. If one is, a sentence from Vincent in a later note.

### U9. Endless: daily reset stuck on prod, recurring
- **Where:** four rounds, Endless and Plague Race together (section 4 rows 11, 18, 20, 24). Key lines:
  - Douglas Aug 8: "the scheduler job... didn't start correctly after the last deployment to production... To prevent that, I will check the jobs on prod after every deployment".
  - Leonard Sep 7 ts 1757203643.996789: "Killing the app doesn't solve the issue... This is prod server I believe".
  - Douglas: "Solved, try again please", "Ok, I will investigate".
- **Reader's use:** Endless or Plague Race Still to do gets "check the reset jobs after the Oct 8 deploy (Douglas)". Less likely, Sep 7 as an established restart-surviving failure.
- **Basis:** hold side RECORD: Leonard is back in Endless Sep 16 05:02 and Sep 17 21:45. Cause side SCOPE_GAP: no outcome from "I will investigate".
- **Base truth:** Sep 7 was a submission candidate on the prod server; Douglas: "Yes, just 2 (I guess you are one of them)". No recurrence after Sep 7.
- **Best settling record:** none needed unless a reviewer raises it.

### U10. Endless: weekly bots too strong on prod
- **Where:** #zombie-match3d ts 1754493271.370749, Vincent Aug 6: "The weekly bots for endless mode is too op for prod configuration". Douglas: "checking the bots' configuration right now".
- **Reader's use:** Endless config still-to-do (Douglas).
- **Basis:** SILENCE. Balance, weak.
- **Base truth:** DM Aug 13: Vincent "oh okay it's not changed then". ZOM-545 "Ingest bot params from a spreadsheet" is Todo, labelled Hot Fix - Global Launch.
- **Best settling record:** none recommended.

### U11. Endless: heat and performance
- **Where:**
  - #zombie-bugs ts 1757998921.355209, Leonard Sep 16: "Endless mode stuttered really badly".
  - ts 1758145553.265559, Sep 17: "I let endless level to run for 5 mins+ and my phone is burning right now".
  - #zombie-match3d ts 1758821469.554029, Oliver Sep 25: "reducing number of objects in endless mode", "I'll merge it soon".
- **Reader's use:** Endless Still to do gets "reduce objects / heat fix (Oliver)".
- **Basis:** SCOPE_GAP. The brief says performance does not hold; its still-to-do sentence lists prod deploy, config and flagged art, and does not exclude performance.
- **Base truth:** my log search found only a debug collider option (4243a48088), not the object reduction. Playtestcloud S23 heat note is #executives only.
- **Best settling record:** none needed if the rubric ignores it.

### U12. Endless: rotation config
- **Where:** #zombie-match3d thread 1756937239.183879, Sep 3-5, EMPLOYEE_0032: "daily_max_entries: 3, daily_max_level: 3 / this is incorrect bc if we add 4 levels or more", "they need to pass month day then instead of 1-3".
- **Reader's use:** Endless config still-to-do.
- **Basis:** SILENCE, but no effect now.
- **Base truth:** repo HEAD has only Endless_01-03. Very weak.
- **Best settling record:** none.

### U13. Adjacent, outside this slice: fixes on main after the submission builds
Julia can read these in #builds:
- 25c6c66b6b (Android #2027, Sep 30 21:27): "Ensuring that in level popups are only called in normal levels; removing popup tutorial from level model endless_02". Code adds Endless and Boss Arena guards in TutorialEventManager.
- 93f45ebbfc: "Fix season pass main screen instance from join popup".
- 0ff577550e (Oct 1 05:51, Android #2029 / iOS #1760): "Fix end popup" (SeasonPassEndedPopup).

All are after iOS #50 and Android #135. Same "on main, not in the store build" shape. Basis SILENCE. Flagging for whoever owns #builds in the census.

## 3. Leonard's Sep 21 report: full record

| When (UTC) | Where | Visible | Who | Text |
|---|---|---|---|---|
| Sep 17 20:34 | #zombie-match3d | J | Leonard | "1.3.38 is out!" |
| Sep 21 02:08 | #zombie-bugs | J | Leonard | The report |
| Sep 21 05:13 | #executives | not J | Leonard | "Endless mode was unplayable on my friends samsung s23 ultra phone guys. And he downloaded it from the App Store" |
| Sep 21 05:18-05:21 | #executives | not J | Leonard | "Also on the endless mode he never clicked to special buttons"; friend is a "game 3d graphics engineer"; Leonard was with him |
| Sep 22 03:54 | #executives | not J | Leonard | Playtestcloud: "On androide Samsung S23 device... a significant performance issue where the device heats up enough for the player to stop the session" |
| Sep 22 04:28 | DM D04UP2L3E3S | not J | Leonard | "I showed the game to friends, families over the weekend at a party" |
| Sep 22 12:39 / 21:04 | #builds; #executives (not J) | J / not J | bot; Leonard | Android Submission #127; "0.3.127 on AnDroid (we just published it)" |
| Sep 22 14:44-15:17 | Linear ZOM-556 to 560 | J | Vincent | Batch of tickets including ZOM-559; none for the air-strike freeze |
| Sep 22 18:00 | #zombie-design | J | Vincent | "problems specific to Samsung devices... I haven't experienced the airstrike freeze, notification muting the game" |
| Sep 22 23:02 | #zombie-design | J | Robert | Playtester: "The app froze hard for a user at end of level 21... Requiring a hard restart. It might be related to the sound getting disabled bug on Samsung devices." |
| Sep 23 16:02-17:30 | #zombie-match3d | J | Arthur, Douglas | Required versions Android 0.3.127, iOS 0.3.40: "Done!" |
| Sep 23 16:48 | #zombie-design | J | Robert | "Leonard's friend *[IDENTIFIER_2104]*" |
| Sep 23 19:50-20:24 | #executives | not J | Robert, Arthur | "hard freeze mid level, showed 0 log"; Arthur "A freeze won't show up as a crash."; Robert "His game froze and he had to force quit and restart" |
| Sep 24 18:32 | #zombie-bugs | J | Robert | "Leonard also had a friend... froze for good, and had to restart his app... first attempt at endless mode level. The log registered NOTHING..." |
| Sep 25 16:01-17:31 | DM D04UP2L3E3S / #zombie-match3d | not J / J | Robert; Oliver | DM "your friend hard froze"; optimisation note |
| Sep 28 16:11 | #executives | not J | Leonard | "this is the latest Android - 0.3.133" (Android Submission #133, Sep 26 23:20 in #builds) |

Reading: one event on a friend's phone, on the live Android build at the time, likely 0.3.122 (Submission #122, Sep 17; inference). Freeze on the friend's first Endless run; force quit and restart cleared it; he continued. Nobody reproduced it. Vincent has no Samsung. No ticket. No path change touching air strike since Sep 20 (git log path filter empty) and no commit message naming it. No later report.

Who owns such devices:

| Person | Devices on record | Visible | Note |
|---|---|---|---|
| Leonard's friend | Galaxy S23 Ultra | not J | The affected phone |
| Leonard | Own Android is not Samsung: Apr 16 #god-bugs "my Android device... it's not Samsung". iPhone, iPad Pro, iPhone 15 Pro, iPhone 7, OnePlus | J / not J | Reached a "galaxy s23 ultra" on a remote device list: Jul 30 DM to Arthur (not J), "I downloaded from Netherlands play store", "most samsung ones are There", "no issue with s21". Best honest route to an S23 Ultra re-test. |
| Owen Baker | S22 Ultra, S24 Ultra (Jul 28 #zombie-bugs), iPhone 11 | J | Apr 15 #god-bugs says "my S23", but later lists omit it. Nearest real device; he reproduced earlier Samsung issues |
| Robert | Galaxy S25 Ultra | DM not J; Samsung recordings J | Sep 22: audio bug on Samsung |
| Brian Foster | Samsung S22 (Sep 10 #zombie-bugs) | J | Reproduced the glass crash |
| Oliver | Galaxy Note 20 5G (Aug 12 #zombie-match3d) | J | |
| Julia | Samsung A73 (May 15 #zombie-bugs, Jun 18 #zombie-ops) | J | |
| Marcus | Samsung A20 | J | |
| Arthur | Galaxy A10 (Jan) | J | |
| Vincent | Oppo Reno 5 Lite, iPhones; no Samsung | J | "I haven't experienced the airstrike freeze" |

Earlier Samsung history a reviewer may connect: April Samsung startup freeze on DD (#god-bugs, ENG-2324, Done May 27); glass VFX crash (ZOM-475, Todo; Robert Sep 10 #zombie-match3d "It is fixed").

## 4. Full census of reports touching a beat

Prod = prod build or prod server as stated. Closes = what Julia can read.

### #zombie-bugs

| # | Date, ts | Report | Beat | Follow-up | Prod/test | Device | Survives restart | Closes for Julia |
|---|---|---|---|---|---|---|---|---|
| 1 | Jul 10-17, 1752125133 | All-time rank off, then "+3 more than the completed levels" | Leaderboard | Vincent's revert ask unanswered | Prod data | iOS | n/a | RECORD by rule: wrong counters |
| 2 | Jul 16, 1752624425 | Quest points did not reset at UTC | Quests | See U6 | Prod | iOS | No | U6 |
| 3 | Jul 29, 1753778302 | Daily chest tooltips all coins | Daily/quest | Calvin fixed | Test iOS 1226 | iOS | n/a | RECORD |
| 4 | Jul 31, 1753977355 | 4th daily chest gives common pack | Quests | Douglas, Vincent "yep fixed", Leonard "4th daily chest is fixed" | Test, prod config | Both | n/a | RECORD |
| 5 | Jul 31, 1753998029 | Strange shadows in Endless | Endless | Julia: normal levels too | Test | Android | n/a | Rule: cosmetic |
| 6 | Aug 4, 1754318636 | Daily Gift Claim panel did not close, "Build - #1528 / Server - production" | Daily gift | Vincent: "only killing the app solved it" | Test build, prod server | Android | No | RECORD: ZOM-556 comment "claiming works and nothing is lost" (submission build) |
| 7 | Aug 6, 1754471574 | Endless tutorial visible above other UI | Endless | Input-block note | Test | iOS | n/a | Rule: cosmetic |
| 8 | Aug 6, 1754513461 | Endless unlock message under 0.5s | Endless | None | Test | Android | n/a | Rule: cosmetic |
| 9 | Aug 6, 1754513871 | Endless stutter on each spawn | Endless | Robert Aug 19 "monster stuttering is gone" | Test | Android | n/a | Rule: performance |
| 10 | Aug 7, 1754587417 | Date parse error after claiming daily reward | Daily gift | Calvin fix #1564 / #1356 | Prod env | Android 1559 | n/a | RECORD via row 6 |
| 11 | Aug 7, 1754525158 | "Endless mode got stuck after the first day", "plague race also got stuc" | Endless, Plague | Root cause Aug 8; Douglas Aug 9 checked after 0:00 UTC | Prod, "live builds" | iOS, Android | Yes (Aug 7 Leonard: can't pass the claim button) | RECORD; Vincent Aug 8 saw daily refreshed |
| 12 | Aug 8, 1754669412 | "I didn't see daily login today" | Daily gift | "may be related" | Prod | iOS | ? | RECORD via row 6 |
| 13 | Aug 8, 1754645673 | Plague bots persistent | Plague | Douglas debugging | Prod | iOS | ? | U8 |
| 14 | Aug 13, 1755061184 | Red dot when not in race | Plague | Leonard: "we don't need it" | n/a | n/a | n/a | RECORD: ZOM-471 comment |
| 15 | Aug 13-14, 1755127046 | 0.3.21 notes: Endless info screen twice; end screen skipped; "needs A LOT of polish" | Endless | Oliver fixed info; ZOM-473 Done | Submission candidate | iPad | No | RECORD |
| 16 | Aug 14, 1755192938 | Endless timer beeps after end | Endless | ZOM-479 Done | Test | n/a | n/a | RECORD |
| 17 | Aug 28 and Sep 22, 1756396651 | Timeout/reconnect errors | All live-ops fetch | Arthur "maybe... bump up the 'Connect Timeout'" | Android test | Android | ? | No closure in thread; base b2542cfd1c doubles Get timeouts |
| 18 | Aug 25, 1756111564 | Plague, Endless do not refresh on prod | Endless, Plague | Douglas "running correctly"; Vincent cannot validate | Dev build, prod server | Android 1713 | ? | Then row 20 |
| 19 | Aug 29, 1756460310 | Leaderboard ended, placeholder frame | Leaderboard | Persisted; Calvin checks; Sep 19 fix, Sep 22 revert | Test iOS 1504, prod env; Vincent: not seen on live builds | iOS | Yes | U7; hold is Sep 30 re-test |
| 20 | Aug 29, 1756460310 | Endless, Plague not refreshed | Endless, Plague | #live-incidents: "endless and plague race is working now" | Prod env | iOS | ? | RECORD (QA) |
| 21 | Sep 3, 1756937250 | Sound bugs in Endless | Endless | ZOM-515 Done | Test | Android | n/a | RECORD |
| 22 | Sep 3, 1756937350 | Refill 1 fewer each time | Endless | ZOM-516 Duplicate; ZOM-546 | Test | Android | n/a | RECORD: ZOM-546 comment |
| 23 | Sep 3, 1756938116 | Monster loses enrage on refill | Endless | ZOM-517 | Test | Android | n/a | RECORD: ZOM-517 comment |
| 24 | Sep 7, 1757203305 | "Endless horde finished and didn't restart" | Endless | Douglas "Solved", "I will investigate" | Submission candidate, prod server | iOS | Yes | U9 |
| 25 | Sep 8, 1757289825 | Quest points need restart | Quests | ZOM-534, Oliver fix | Prod | iOS | No | U6 |
| 26 | Sep 10, 1757478773 | Live-ops buttons gone at level 112 | All | Back at 113; Douglas "network error/lag" | Candidate 0.3.35 | iOS | n/a | RECORD |
| 27 | Sep 10, 1757467270 | Endless hard froze at end screen | Endless | None | Test | Android Samsung | No, force quit | U2 |
| 28 | Sep 11, 1757558514 | Sound gone, hard freeze at victory screen | All levels | ZOM-559 Todo | Test, 0.3.119 per Arthur | Android Samsung | Sound yes until reset | U2 |
| 29 | Sep 11, 1757565808 | Endless quit keeps ticket | Endless | Vincent video; "Let's keep it as is" | Test | n/a | n/a | RECORD |
| 30 | Sep 11, 1757554129 | Weekly star count wrong image | Leaderboard | ZOM-558 Done | Test | n/a | n/a | RECORD |
| 31 | Sep 15, 1757939514 | Quest claim spam; "If I left, the quest cannot be claimed" | Quests | Calvin PR; Robert "Things fixed?" +1 | Test | Both | ? | Owner +1, plus Leonard Sep 17 "no other blockers" |
| 32 | Sep 15, 1757939514 | Season pass branch: left events invisible, packs, price 9.99 vs 6.99, bank overlap, frame mismatch | Season Pass | Oliver Sep 16 "bugs fixed"; base 91b58ce55a "Fixing: Prices" | Test branch | Both | n/a | Owner claim, plus Leonard Sep 17 "no major bugs" |
| 33 | Sep 15, 1757939514 | "For win&collect, I haven't seen any update or build" | Collect & Win | Superseded by #468 merge | n/a | n/a | n/a | Other slice |
| 34 | Sep 16, 1757998292 | Quest animation sluggish, "blocker" | Quests | Calvin PR | Submission candidate (Leonard: "0.1.37") | iPad | n/a | As row 31 |
| 35 | Sep 16, 1757998921 | Endless stutter on open | Endless | Robert, Marcus ideas | Submission candidate (Leonard: "0.1.37") | iPad | n/a | U11 |
| 36 | Sep 16, 1757999990 | No claim SFX on Season Pass | Season Pass | Oliver; struck through in Vincent's list | Candidate | n/a | n/a | RECORD |
| 37 | Sep 16, 1758000132 | Carnage streak freeze no timer | Season Pass | Vincent to-do Brian; base b8fb70f9a5 adds timer | Candidate | iOS | n/a | No J record names the fix; weak |
| 38 | Sep 16, 1758031982 | Premium lives reset to 8, refill gives 5, trampoline set not added, pack chests need extra click; To Dos | Season Pass, quests, Endless | Oliver "bugs fixed" | Test | Android | n/a | Owner claim; To Do is U5 |
| 39 | Sep 17, 1758130096 | Daily login does not reset after a missed day | Daily gift | Brian "it's a bug"; ZOM-556 | Unstated | n/a | n/a | RECORD: comment plus rule |
| 40 | Sep 17, 1758145553 | Phone burning in Endless, 10 fps on air strike | Endless | Vincent same on iOS | Test (animation-test) | iOS | n/a | U11 |
| 41 | Sep 21, 1758420497 | S23 freeze | Endless | Not in thread | Prod | S23 Ultra, Android | No | U1 |
| 42 | Sep 22, 1758546048 | "I cannot participate in leaderboard. Killing the app doesn't help" | Leaderboard | Reverted; "working fine right now" | Test | iOS | Yes, until revert | RECORD for this build; U7 |
| 43 | Sep 22-23, 1758580854 | Quest table changes | Quests | None | Prod config | n/a | n/a | U3 |
| 44 | Sep 24, 1758738754 | Friend's freeze, restated | Endless | n/a | Prod | S23 Ultra | No | U1 |
| 45 | Sep 30, 1759249488 | Reward box | Quests and chests | Oliver "asap" | Latest build | n/a | n/a | U4 |

### #zombie-match3d

| # | Date, ts | Report | Beat | Follow-up | Prod/test | Device | Survives restart | Closes for Julia |
|---|---|---|---|---|---|---|---|---|
| 46 | Jul 23-24, 1753302592 | Endless thread: wrong colour variants; claim button persists, no next event | Endless | Refill "Flawless"; "stop testing the event flow before the backend integration" | Dev | n/a | Yes | RECORD: superseded by prod launch |
| 47 | Jul 23, 1753305766 | Bosses double spawning in Endless | Endless | Vincent asks for video; none | Dev | n/a | n/a | Silence, cosmetic-level, stale |
| 48 | Jul 24, 1753393838 | TestFlight 0.3.3: no trophy road, 1 quest, no Plague Race | Quests, Plague | Arthur root cause; TestFlight 5/6 | Test, prod server | iOS | Partly | RECORD |
| 49 | Jul 29-31, 1753822757 | Pack from daily chest before level 35 | Quests | Vincent "yep fixed" | Test | Android | n/a | RECORD |
| 50 | Aug 5, 1754423041 | Daily Gift cannot close; "DailyLoginReward data loading error" | Daily gift | No answer | Editor | n/a | Yes | Editor only; RECORD via row 6 |
| 51 | Aug 6, 1754439427 | Algo levels not counting for Plague Race | Plague | Arthur "not able to repro" | Prod player | Both | n/a | RECORD: ZOM-459 Done Aug 25 |
| 52 | Aug 6, 1754493271 | Endless weekly bots too strong | Endless | Douglas checking | Prod | n/a | n/a | U10 |
| 53 | Aug 7, 1754584405 | Summary of 3 backend bugs | Plague, Endless | Rows 11, 13 | Prod | n/a | Yes | Rows 11, 13 |
| 54 | Aug 18, 1755556150 | De-enrage; end screen still runs timer and spawns | Endless | ZOM-517; "will continue checking" | Test | Android | n/a | RECORD for enrage; end-screen note feeds U2 |
| 55 | Sep 3-5, 1756937239 | Rotation config | Endless | No closure | Prod server | n/a | n/a | U12 |
| 56 | Sep 15, 1757961539 | Refill spawns fewer over time | Endless | ZOM-546; "trying to fix it" | Test | n/a | n/a | RECORD: ZOM-546 comment |
| 57 | Sep 17, 1758138979 | Heat after Endless | Endless | Sep 25 note | Test | iOS | n/a | U11 |
| 58 | Sep 18, 1758215775 | Push prompt "killing the funnel" | Push | Leonard Sep 19 #zombie-bugs "It's not PNs" | Prod data | iOS, Android | n/a | RECORD by brief rule: rows go by sheet status and copy |
| 59 | Sep 30 (SQL), b5f2955c | Leaderboard re-test | Leaderboard | Held | Prod | Two devices | Yes | RECORD |

Collect & Win: no failure report in either channel beyond row 33. Its reports sit in the canvas and #zm-collect-win (not J). Canvas items still unticked include "In every level, I got two errors both backend and client" (Sep 23); no J record carries it.

## 5. Suggested minimum for this slice

- Five records cover the top of the list:
  - U1 thread reply.
  - U2 ZOM-559 comment.
  - U4 thread reply.
  - U5 ZOM-563 comment.
  - U6 ZOM-534 comment.
- Plus an extended sentence in the existing Trello comment for U3.
- U1 and U2 should be written together. Settling S23 alone leaves the same clause pointing at ZOM-559 and at Vincent's "specific to Samsung devices".
