# Closure audit: Linear, GitHub/Confluence and Trello/mail/Drive census candidates against revision 9

Clock 2025-10-01 07:00 UTC, synth-cut. SQL revision 9 read as an overlay, not executed. All times UTC. "J" means Julia can reach it.

## 1. Result

- **1 row is OPEN:** Endless core-game VFX, which includes the ZOM-465 refill timer. It passes every part of the new rule (since the brief, names Endless, player-facing art, says not done), and the only cover is the art owner's claim about a different screen.
- **8 rows are closed but soft.** The kill rests on an inference or an owner's claim. Two matter: push rows 4 and 6, and the three commits after the submission builds.
- **Every other row is closed by a record or by a rule sentence applied literally.** That includes store approval, the Confluence items, ZOM-559, ZOM-546, ZOM-556, ZOM-543 and push rows 9 and 14.
- Rev 9 closed the three platform forks. L-01, L-02, L-03, TMD-07 and TMD-10 now have the records or wording they needed.
- No value in truth.json needs to change for any fix below.

## 2. Findings, most serious first

### F1. OPEN: Endless core-game VFX (L-04, the branch half of R9, Slack census SO-45)

Reading A: Endless Still to do is blank. Reading B: "core-game VFX, including the refill timer, then implementation (Marcus)".

Rule test, strictly applied, against the brief's last edit 2025-09-24T17:40:52Z:

| test | result | quote |
|---|---|---|
| since this brief | Pass | ZOM-565 description, Marcus, created 2025-09-25T13:46:04Z: "I'm going to start working on the endless mode vfx inside of the core game part." |
| since this brief, Julia-visible | Pass | #zm-animations (J) ts 1758815614.940719, Marcus, 2025-09-25T15:53:34Z: "The vfx added to the endless mode gameplay ... I also need to add few text animations like for the combo when it changes etc.... and when i'm done with that if this it's cool i will make ticket for implementation" |
| as not done | Pass | Commit 7683df0351, marcus, 2025-09-30T12:44:08Z: "infiniteBoss and endless mode core gameplay ui vfx wip". It sits on marcus.bennett/EndlessMode_Vfx and _NewUnity only; I checked it, e14a0a5b52 and ebd5baed12, and none is on main |
| names the beat | Pass | All three say endless |
| kind | Pass | Player-facing art |

ZOM-465 still shows, unstruck, under "## Core-Game Animations": "### Refill Timer ticking animation as well as color change from 5 to 1." It is In Progress, and Marcus's own question ("do we still need to do that?") has no answer.

Best kill available, cmt_zom565_1, Marcus, 2025-09-29T14:34:12Z: "This is the P1/P2 endless polish from the list Brian gave me, the screen already works without it, so it is not needed for the beta."

Why it does not rule Reading B out:
- "This" is the bar and glow on the endless screen prefab. Reading B is about gameplay, which he separated from the screen in the ZOM-565 description.
- The core-game commit is dated the day after the comment, and work is still marked wip.
- cmt_zom465_2 (Sep 30) speaks only to icons: "the other event icons are finished".
- The brief's "VFX ... gaps ... do not hold a beat" settles the hold only. "polish nobody flagged" does not apply, because Marcus flagged it.

In the kill's favour: Brian's Sep 12 list (#zm-animations, J) has "*P1/P2 – Endless mode remaining VFX* ( ...ZOM-465... )" and "*P1/P2 – VFX for endless and boss arena*", so "the P1/P2 endless polish" can be stretched over both. The platform's Reading A also listed "ZOM-465 leftovers" as not listed. But its F24 quote is the ZOM-565 comment only, the Sep 25 post was never cited, and that was under the old rule. By the standard this is a SCOPE_GAP: an owner's claim on a neighbouring scope.

Smallest fix: one Linear comment on ZOM-465, by Brian Foster (usr_fc22d5941b2aeb5c), who owns the list and is not the art owner. This is the same pattern as his ZOM-526 and ZOM-566 notes.
- id cmt_zom465_3, sequence 3, about 2025-09-30T18:12Z, after Marcus's 18:05:02Z note, so no id or evidence reference changes. Bump updated_at.
- Text: "Marcus, the refill timer line and the endless gameplay VFX on your branch are polish from my list. Endless runs fine without them, so they can follow and do not have to land before the beta."
- Do not write "the rest of this ticket": that would sweep in the Collect & Win icon, which is S11. Do not mention the icon at all, so the S11 trap stays as it is.
- Do not say the work is dropped. In Normal (not reachable, used only to keep the wording true), ZOM-567 "Endless Mode Core game Vfx" opens Oct 1 12:26Z and closes Oct 13, so it was real work that gated nothing.

Adjacent, outside my three files: #zombie-art ts 1759159849.386619, Martin, Sep 29: "I'm preparing a *desert theme* for the *Endless Mode*!" (census SO-22). Same date, beat and kind, but no one calls it unfinished or needed. The Slack auditor should rule on it.

### F2. Push rows 4 and 6 against the client: closed, but not by "its row"

Reading B: Send. Both rows are Ready and LIVE. "its English copy" belongs to the push, and the push's copy on main says the right name.

- Client, match3d `Assets/Scripts/Notifications/NotificationManager.cs` lines 146 and 158: "Return to Zombie Match 3D now and continue your mission"; "Complete your first mission in Zombie Match 3D". Verified. Commit ec377e9fcf, arthur blake, 2025-07-22, "Update more title references". No .cs file on main still has "Puzzles vs Zombies".
- Julia-visible support that the client is where these live: Leonard, #zombie-bugs, 2025-09-18 23:52: "All our PNs are local".

What each quote does:
- **"its row" settles nothing here.** It governs only Ready and LIVE, and both rows pass that. In "A push goes out only if its row is Ready and LIVE and its English copy names the game...", both "its" point at the push.
- **"plan the PNs Beta tab as it stands, one line per row, local notifications included" does the work.** The next sentence drops four rows, so "as it stands" cannot mean only "keep every row"; it means take the tab's content as it is. The reply also covers local rows expressly, and tells Julia to plan the tab for them.
- **The brief's same paragraph supports it:** "the translated tab is the old Domino set" sets English copy against a translated tab, so copy is discussed by tab. Nothing in the rules mentions the client.
- Under Eval 1 §2.1 this resolves by check 2 (Authority) and check 3 (Source identity: "A statement from a different source is not automatically interchangeable with the named source").

My call: Send is ruled out, but only through a reading of "as it stands". No record says the sheet text outranks the client string, and I searched Julia's Slack from June to September for one. The hold's reason ("still names Puzzles vs Zombies") is true of the sheet and false of the shipped client. A Held note that adds the client fact still passes: P06's regex takes "puzzles|old (game|title|name)|rename|copy". So the only live risk is Send against Held.

Smallest fix, optional but nearly free: in the brief change "its English copy names the game" to "the English copy on that row names the game". It names no item and hints at nothing. Recompute the Config locks heading offset. With that edit this becomes a literal rule kill.

### F3. Push rows 9 and 14 against the client: truly settled

Reading B: already going out. The client schedules both: `BatchSchedulePlagueRace` (daily at 00:15 server date for 5 days, from the unlock level) and `BatchScheduleWeeklyLeaderboardNotifications` (every 7 days for 4 weeks), lines 177 and 180.

Kill: brief "A push goes out only if its row is Ready and LIVE ... Anything else is held, with what is missing." Sheet R10 and R15 read "WIP". Here "its row" is literal and decisive. The client's behaviour cannot make a row LIVE. A run may add that a hold needs a client change, but the cell stays Held and the WIP reason stays.

### F4. The three commits after the submission builds: closed, and only the word "flagged" closes them

Submission builds: iOS #50 started 18:43, finished 19:15; Android #135 started 18:45, finished 20:13.

| commit | date test | beat named | kill |
|---|---|---|---|
| 25c6c66b6b, 21:20 | Since the brief | "endless_02" | Rev 9 reply covers only the material: "It is only that sweep on the art, it goes out with the next build and nothing waits on it." The commit also changes TutorialEventManager.cs, which no record covers |
| 93f45ebbfc, 21:36 | Since the brief | "season pass" | No record. Only the rule |
| 0ff577550e, Oct 1 05:44 | Since the brief | Subject names none; files are SeasonPass | No record. Only the rule |

So date and beat do not help. The kill is that a "Fix ..." commit says a thing is done, and nobody flagged it as not done: "Nothing else goes in". I searched Julia's Slack since the brief and found only the #builds lines. The Vincent report behind 93f45ebbfc is in a DM she cannot read.

I accept the kill, but it is the softest rule kill here, because the shape (on main, not in a store build) is the one the platform failed on before. The client's `EndDate + 1 day` is killed separately by "Every window is stated in server time (UTC)".

Optional fix, only if you want a record: Oliver or Vincent in #zombie-bugs, Oct 1 05:55-06:59Z, saying the two Season Pass popup fixes also go with the next build and nothing waits on them. I would not add it unless a reviewer asks, since it adds a search hit and a new since-brief statement.

### F5. Store approval in the deck: truly settled

Reading B: "store approval of the Sep 30 builds (Leonard or Arthur)" as a Still to do, or a later Collect & Win start, or a hold.

- **Still to do:** the deck is dated 2025-09-23T16:05:43Z, before the brief (created 2025-09-24T17:15:22Z), and names no beat. It fails "for that beat" and "since this brief".
- **Newer source:** Frederick's DM, 2025-09-30T20:20:17Z, after both submission builds finished: "the beta buy we start Mon Oct 6". The prompt repeats it.
- **Window start:** "the backend release instant read in UTC, not when its client PRs merged."
- **Hold:** "A beat whose server windows are waiting on that release starts late, it is not held."
- **Two since-brief records that look like flags, both answered:**
  - Season Pass spec v2 (Sep 30): "We gate on store approval and a live-ops config freeze the day before." The same page: "Reached production in the week of September 22-29, 2025". The gate has passed. The freeze is the lock already in the key.
  - Calendar v3 (Sep 29), Collect & Win: "Built for the end-of-September beta submission ...; not yet live." Arthur's later rc_10 gives the reason: "still on the DEV stack only". That item is in the key. This one small step is an inference, and no record says "store approval" since the brief.

No fix needed.

### F6. Confluence items: settled

CF-1 to CF-5 all die on the rule; rows below. Only CF-1 and CF-2 are since the brief, and neither is a flag of a listed kind on a beat.

### F7. ZOM-559, ZOM-546, ZOM-556, ZOM-543: settled by rule, not by owner comments

- **ZOM-559:** created Sep 22, no comment, names no beat, a bug. Fails all tests. Trello [58]'s Sep 30 action is a `pos` move only, not a description edit.
- **ZOM-546:** created Sep 15. Owen's note is after the brief (Sep 24 19:00:57Z) but says the opposite of not done. The kill does not need his claim.
- **ZOM-556:** the date test is a same-day call. Vincent's note is 2025-09-24T15:20:38Z, which is 1h55m before the doc existed but the same calendar day as the header "Frederick, Sep 24". The kind test decides it: a day-row bug is not prod deploy, config or art.
- **ZOM-543:** since the brief, but it names no missing beat, and Trello [63] was completed 20 minutes later.

## 3. Key to the table

Rule quotes used below:
- **STILL:** "what still has to land before it runs for bought users and who owns it: a held beat's fix, and what has been flagged for that beat as not done since this brief (prod deploy, config or player-facing art). Nothing else goes in: not what already shipped, not analytics, not polish nobody flagged."
- **HOLD:** "Hold a beat only when players provably cannot enter, score or claim on prod even after a restart. An established failure holds it; an unverified one does not. Wrong counters, a reset that needs a restart, cosmetic, VFX and performance gaps and analytics gaps do not hold a beat"
- **START:** "A beat starts with the first window that opens after its server windows are live on prod, the backend release instant read in UTC, not when its client PRs merged. A window the release instant pre-empts does not count."
- **PUSH:** "A push goes out only if its row is Ready and LIVE and its English copy names the game as Zombie Match 3D and events by their ZM3D names. Anything else is held, with what is missing."
- **TAB:** "plan the PNs Beta tab as it stands, one line per row, local notifications included."

Rule-test tag in the kill cell: [latest flag date; beat named or not; kind]. "Pre-brief" means before 2025-09-24T17:40:52Z.

Last column:
- RECORD: a dated reachable record, not just the owner on their own gap.
- RULE: a brief or reply sentence applied literally, with dates from records. It counts as a kill under the standard.
- OWNER: only an owner's claim.
- INFERENCE: the kill needs a step no quote states.
- Then Yes, Partly or No: does the quote truly rule Reading B out.

## 4. All candidates

### 4.1 OPEN

| id | Reading B tried | kill quote and source, or OPEN | kill type |
|---|---|---|---|
| L-04 (ZOM-465 refill timer), with SO-45 and the branch half of R9 | Endless Still to do: "core-game VFX including refill timer (Marcus)" | **OPEN.** [Sep 25 and Sep 30; Endless; art.] Best available, cmt_zom565_1: "This is the P1/P2 endless polish from the list Brian gave me, the screen already works without it, so it is not needed for the beta." Its "this" is the screen, not gameplay. See F1 | OWNER, neighbouring scope. No. The refill line alone has no since-brief mention, but it sits under "Core-Game Animations", which the Sep 25 posts pick up, and the line itself cannot be dated |

### 4.2 Closed, but the kill is an inference or an owner's claim

| id | Reading B tried | kill quote and source | kill type |
|---|---|---|---|
| TMD-01 row 4 (1 day lapsed) and row 6 (FTUE) | Send, because the client copy names Zombie Match 3D. Or Held with only a sheet update missing | TAB, plus brief "the translated tab is the old Domino set". Sheet R5 K "Return to Puzzles vs Zombies now", R7 K "in Puzzles vs Zombies". "its row" does nothing here. See F2 | RULE + INFERENCE. Partly: yes on Authority and Source identity, but "as it stands" must be read to reach the copy. The Held variant has the same cell |
| GH-3a, 25c6c66b6b | Endless Still to do: popup fix not in the submission build (Oliver) | [Sep 30; "endless_02"; fix, not a flag.] Oliver, rev 9, #zombie-bugs: "it goes out with the next build and nothing waits on it." STILL "Nothing else goes in" | OWNER for the sweep. RULE + INFERENCE for the popup half. Partly |
| GH-3b, 93f45ebbfc | Season Pass Still to do: join-popup fix must reach a build (Oliver) | [Sep 30; Season Pass; fix, not a flag.] STILL "flagged ... as not done ... Nothing else goes in". No item record | RULE + INFERENCE that a "Fix" commit is not a flag. Partly |
| GH-3c, 0ff577550e | Season Pass Still to do: end popup fix before the Nov 1 rollover. Or a window read from the client's `EndDate + 1 day` | [Oct 1 05:44; subject names no beat.] STILL as above. Window: "Every window is stated in server time (UTC)"; "Season Pass seasons open on the 1st at 00:00 UTC" | RULE + INFERENCE for the to-do. RULE, Yes, for the window |
| L-09 ZOM-565 | Endless Still to do: start-screen bar and glow (Calvin) | [Sep 25 and Sep 29; Endless; art, so it passes every test.] cmt_zom565_1: "the screen already works without it, so it is not needed for the beta." On the exact item, no contrary record, platform F24 accepted | OWNER. Yes on its face, owner only. The F1 fix does not change this row; add "start screen" to the Brian note if you want it non-owner |
| TMD-07 Trello [61] | Quest rollover Still to do: more quests and reward balance (Leonard/Douglas). Or quests run only from Oct 13 | [Sep 29; quests; config.] Injected comment: "More quests and the reward balance go in with the Mon Oct 13 rollover if they are ready. The rollover does not wait on them, the current quests keep running either way." Rev 9 closed the reward-balance half | OWNER (card owner), no contrary record, platform F30. Yes |
| L-15 ZOM-432 | Daily gift Still to do: frame reaches players once stores approve | [Sep 30; Daily gift; art.] cmt_zom432_2, Samuel: "The frame went out with PR #471. It is in both submission builds from today, iOS 50 and Android 135, so nothing is left here. Closing." Done; #471 merged 15:52, before iOS 50 | OWNER (fix author) + RECORD (PR and Done state). Yes. Residual: "submission" is not live, answered by F5 |
| R2 #471 sprite GUID | Daily gift Still to do: CodeRabbit Critical, 2025-09-29T22:04:53Z: "this change will surface as missing sprites across the UI" | [Sep 29; Daily gift; art, and "has been flagged" is passive, so a bot can count.] Later: Arthur APPROVED 15:52:15Z; Samuel "nothing is left here". Base check: the warning is false, but that proof is in Normal's untruncated prefab | RECORD (approval) + OWNER. Yes |

### 4.3 Closed by a record or a rule

**Store approval, Confluence and the named tickets**

| id | Reading B tried | kill quote and source | kill type |
|---|---|---|---|
| TMD-03 / GH-4 store approval | Still to do "store approval (Leonard or Arthur)"; or Collect & Win starts later; or held | [Deck Sep 23; no beat.] STILL "for that beat ... since this brief". DM Sep 30: "the beta buy we start Mon Oct 6". START "not when its client PRs merged". "starts late, it is not held". See F5 | RULE + RECORD. Yes. One small step: calendar "not yet live" is read as the server windows, per Arthur rc_10 |
| CF-1 no purchase recorded | Still to do: verify the $6.99 purchase on prod. Or hold Season Pass | [Sep 30; Season Pass; a sales fact, not a listed kind.] Spec: "No Season Pass purchase has been recorded yet" is no flag of a kind in STILL. HOLD: "an unverified one does not" | RULE. Yes |
| CF-2 GDD glass crash | Still to do: confirm Samsung crash on the re-added glass VFX | [Sep 30; no beat; page says done.] GDD: "Known launch issues (tracked, historical)", "fixed by removing the glass SFX and VFX". STILL "for that beat". SC-8 stays ungraded | RULE. Yes |
| CF-3 QA matrix | Still to do: QA sign-off on iOS 50 / Android 135 (Vincent) | [Jul 26 and Aug 4; no beat.] STILL. Runbook also says "builds have shipped without a completed pass" | RULE. Yes |
| CF-4 scheduler | Still to do: confirm scheduler after the Oct 8 deploy (Douglas) | [Aug 1; no beat.] STILL | RULE. Yes |
| CF-5 Nakama | Leaderboard held or to-do: team leaderboard off in prod | [Aug 1; team leaderboard, a neighbouring feature.] STILL. Leagues on CDK: `LEAGUES_SCHEDULE ... "0 0 * * 1"` | RULE. Yes |
| L-07 / TMD-06 ZOM-559, ZOM-535 | Still to do "verify Samsung freeze (Oliver)". Or hold level-based beats | [Sep 22; no beat; a bug.] STILL. HOLD "an unverified one does not". Ticket: "Doesn't happen to me, might be again a Samsung issue". Trello's Sep 30 action is a `pos` move. Since-brief Robert posts (Sep 24 18:32 "had to restart his app ... Once Leonard's friend restarted, his log just continued"; Sep 25 audio theory) fail "even after a restart" and name no listed kind | RULE. Yes |
| L-08 / TMD-04 ZOM-546 | Endless Still to do: "verify refill (Owen)". Or the refill bug | [Sep 15; Trello "for both events"; a bug.] STILL kind and "as not done": cmt_zom546_1, Sep 24 19:00:57Z: "the board refills the same amount at the 40th refill as at the second." #453 "Manual refill logic" on main | RULE. Yes. Owen's unnamed "here" no longer matters |
| L-06 ZOM-556 | Daily gift Still to do: day-row fix (Calvin). Or held | [Sep 22; note Sep 24 15:20:38Z, same calendar day as the brief, but before the doc existed; Daily gift; logic bug.] STILL "(prod deploy, config or player-facing art)". HOLD "Wrong counters". cmt_zom556_1 (Vincent, reporter): "claiming works and nothing is lost." | RULE + RECORD. Yes. The kind test decides; date alone would be a same-day call |
| L-10 ZOM-543 | Queue entries for other beats (Calvin). Or hold Plague Race on an unqueued panel | [Sep 30; names no missing beat.] cmt_zom543_1: "current flow is level_end, daily_gift, season_pass, tutorial plus Collect and Win." Trello [63] completed 2025-09-30T16:40:22Z, #472 merged. HOLD. Arthur rc_10: "The Plague Race, leagues, Endless and Season Pass schedules are already running on prod." | RULE + RECORD. Yes. Note: on main Collect & Win runs through RewardVFXManager, not an EnqueueEvent line. No effect |
| L-01 / GH-6 ZOM-563 | Season Pass Still to do: golden frame to prod (Douglas) | cmt_zom563_1, Vincent (tester), Sep 30 22:04:33Z: "Checked on prod after the update: teams' lives, golden frames and names all work as expected. Closing." State Done | RECORD. Yes |
| L-02 / GH-2 ZOM-534 | Quest Still to do: fix to prod (Douglas) | cmt_zom534_2, Leonard (reporter), Sep 30 01:22:46Z: "Stayed online through the 00:00 UTC reset on the store build tonight. Quest points reset on their own, no restart. That was my report, it is good on prod now." | RECORD. Yes |
| GH-5 ZOM-534 edge case | Quest Still to do: watch the day-boundary edge case (Douglas) | [Sep 25; quests; a watch, no listed kind.] STILL. cmt_zom534_1: "so nothing else has to land for the beta." cmt_zom534_2 is later | RULE + RECORD. Yes |
| L-03 / GH-1 #477 | Collect & Win Still to do: header title and info text (Owen) | cmt_zom566_1, Brian (ticket creator, not implementer), Sep 30 17:53:19Z: "The header title and the info screen text can follow with it. The event runs fine with the current text, so they do not have to land before the beta." | RECORD. Yes |
| GH-7 #477 `currentColor` | Collect & Win Still to do: fix the "regression" | [Sep 30; Collect & Win; code, not a listed kind.] STILL. PR unmerged, so it is on no build. The other flags in that review are analytics | RULE. Yes |
| L-05 ZOM-542 | Endless Still to do: home and victory screen update (Samuel) | [Sep 14 and Sep 22; no since-brief record found.] STILL "since this brief". Backup cmt_zom542_1: "so they are not needed for the beta." | RULE. Yes; no longer leans on the owner |
| L-11 ZOM-521, 528, 541 | "Brian checks card VFX in a build" | [Sep 30; cards, not a beat.] STILL "for that beat". Scope: "an event window, a reset or a start push". cmt_zom521_2: "Card pack animation went in with #475." | RULE. Yes |
| L-12 / TMD-17 ZOM-544, Trello [54] | Global to-do: sign-in progress sync | [Sep 29; no beat.] STILL "for that beat" | RULE. Yes |
| L-13 ZOM-475 | "verify the glass crash on Samsung" | [Aug 14; no beat.] STILL. SC-8 | RULE. Yes |
| L-14 ZOM-359, 449, 468 | Performance to-do or hold | [Pre-brief; no beat.] STILL. HOLD "performance gaps". Oliver's Sep 25 heating post is performance too | RULE. Yes |
| L-16 ZOM-344 | Quest box animation integration | [Sep 16.] STILL "since this brief". Ticket Done | RULE. Yes |
| L-17 ZOM-484, ENG-2258 | Infographic animations | [Aug 14; Domino twin.] STILL. Reply "things that are not in the beta" for Axe Arena | RULE. Yes |

**Census sections 4, 7, 8 and 9 of the Linear file**

| id | Reading B tried | kill quote and source | kill type |
|---|---|---|---|
| ZOM-429 hold | Not held | Vincent, #zombie-match3d, Sep 30 20:50: "I killed the app and reopened it twice, played a few levels, and my week is still last week one. Same on the second device." Newer than cmt_zom429_1 | RECORD. Yes |
| ZOM-429 Hold until | Oct 8, or a guessed Monday | "A hold with no dated fix runs until the fix is confirmed on prod; say that instead of guessing a date." The release covers "server windows that are still on the DEV stack", and Arthur has leagues on prod | RULE. Yes |
| ZOM-526 | Token travel still to do | cmt_zom526_3, Calvin: "Only the Axe Arena travel is left here, and that waits on the event coming back." cmt_zom526_2, Brian: "it does not have to land before the beta." | RECORD. Yes |
| ZOM-471 | Red dot still to do | [Sep 17.] STILL. cmt_zom471_1: "nothing here has to land for the beta." | RULE. Yes |
| ZOM-504 | Persistent objects to-do | [Sep 22.] STILL. Vincent: "Visual only, no board state affected." | RULE. Yes |
| ZOM-517 | Enrage bug to-do | [Sep 18.] STILL. Robert: "could not get one to lose it while walking." | RULE. Yes |
| ZOM-552, 442, 549, 548, 387, 386, 400, 439, 441 | Analytics still to do | STILL "not analytics" | RULE. Yes |
| ZOM-505 | FTUE blocker | [Pre-brief; no beat.] STILL | RULE. Yes |
| ZOM-562, 390, 62 | Boss Arena, Axe Arena, Dead Eye items | Brief "Boss Arena is off this calendar until the pivot call."; reply "things that are not in the beta" | RULE. Yes |
| ENG-2331, 2349, 2353 | Mistaken for Collect & Win | [May 2025.] Domino Delights tickets; calendar "Same feature as Win & Collect on Domino Delights, under a different name" | RECORD. Yes |
| Note: Sep 16 #zombie-bugs list (premium lives reset, refill of 8, trampoline rewards, freezer rewards) | Season Pass Still to do | [Sep 16.] STILL "since this brief" | RULE. Yes |
| Note: Sep 30 shader thread | "lightSweep box fix (Oliver)" as art to-do | [Sep 30; names no beat.] STILL "for that beat". Rev 9 Oliver: "It is only that sweep on the art, it goes out with the next build and nothing waits on it." | RULE. Yes; the rule holds without the owner's note |
| Note: S23 follow-up | Endless "verify S23" | Leonard, rev 9 thread reply: "Could not get it to freeze, so I am leaving this one." Also [Sep 21; not a listed kind] | RECORD + RULE. Yes |
| Note: Sep 7 "Endless horde finished and didn't restart" | Endless reset failure | [Sep 7.] Douglas: "Solved, try again please". Arthur rc_10 has Endless on prod | RECORD. Yes |
| Section 8, the other tickets: ZOM-16, 48, 56, 64, 65, 66, 69, 70, 73, 76, 97, 104, 118, 119, 121, 122, 130, 137, 147, 148, 150, 151, 155, 168, 171, 181, 182, 184, 202, 236, 237, 243, 255, 292, 293, 311, 317, 342, 348, 427, 438, 443, 453, 458, 467, 477, 481, 482, 483, 508, 513, 514, 520, 535, 539, 545, 554, 560, 564 | Any as a Still to do | [All activity pre-brief; no beat.] STILL "since this brief". Post-SQL, 83 of 96 open tickets have no activity after the brief. No Julia-visible Slack message since the brief cites any of them by ZOM id | RULE. Yes |
| ZOM-78 | None | Calendar ticket, destination only | n/a |
| ART-790, ART-792 | Store art to-do | [Jul 9 and Aug 26; no beat.] STILL. SC-16 | RULE. Yes |

**GitHub and Confluence, remaining rows**

| id | Reading B tried | kill quote and source | kill type |
|---|---|---|---|
| GH-8 Thursday cron | First window Thu Oct 9, because CDK fires "0 0 * * 3,4". Or to-do: mid-window reset | Brief: "Collect & Win runs Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC." START "A window the release instant pre-empts does not count." Release 2025-10-08 15:00Z. Three windows, three openings, so Thursday is not an opening | RULE. Yes |
| GH-9 revert 49211bd82f | "re-land the reverted fix (Oliver)" | [Sep 22.] STILL. The beat's hold already carries "a held beat's fix" | RULE. Yes |
| GH-10 backend #34 | "EMM real players PR" | [Aug 1, draft.] STILL | RULE. Yes |
| R1 change-request hold | Hold on a review blocker | In ZM3D repos only match3d#303 (2025-07-16) and backend#4 (June) are CHANGES_REQUESTED, re-checked. Brief "a change request outside the Aug-Sep live-ops cohort" | RECORD + RULE. Yes |
| R2 other CodeRabbit Criticals, #468, #470, #465, #477 | Hold, or to-do from bot notes | All state COMMENTED, so no "change-request review blocker". Code null-guards and memory flags are not a kind in STILL | RULE. Yes |
| R3 calendar "Weekly Leaderboards ... Live" | Not held | Vincent Sep 30, later and specific | RECORD. Yes |
| R4 "no technical content lock" | No lock, so Brian's Oct 31 stands | Calendar, same passage: "The 24h season-pass freeze in the Season Pass spec is a process control on top of that"; spec "locked 24h before each season opens" | RECORD. Yes |
| R5 calendar "not yet live" | Collect & Win held | Brief "starts late, it is not held" | RULE. Yes |
| R6 push row 7 name | Ready under a new name | Sheet Not Ready and WIP; PUSH | RULE. Yes |
| R7 release checklist quest config | Quest to-do | [Jul 26.] STILL. Trello "The rollover does not wait on them" | RULE. Yes |
| R8 Plague Race "algo bug Aug 2025" | Held | Calendar "fixed 25 Aug 2025"; ZOM-459 Done | RECORD. Yes |
| R9 schedule half | Different Endless resets | Calendar: "resets daily at 00:00 UTC and weekly on Monday 00:00 UTC"; CDK agrees | RECORD. Yes |
| R10 #471 before builds | Frame missed the builds | #471 merged 15:52; iOS #50 started 18:43 | RECORD. Yes |
| R11 Axe branches, liveops#5, #10, #476 | Off-calendar work | Reply "things that are not in the beta"; 2024 Domino PRs; #476 is a test bot | RULE. Yes |
| R12 owners | Config owner is Robert or Julia | Brian mail: "Same contents, same owner"; brief "its owner is told in a reply on the mail where they committed to it" | RECORD. Yes |
| Spec "the initial launch may be a partial first season" | October window form differs | Both fair (F16) | Both-fair figure |
| Spec "Do not touch tray count or Endless refill cadence during an active season" against #453 | To-do or Endless change | [#453 Sep 22.] A guardrail, flags nothing as not done. STILL | RULE. Yes |
| "Ship to 100%", "hourly Quantum crons", hourly import against CDK `*/5` (SC-62) | No cell | None of these reaches a Still to do, status, Hold until, window start or push call | n/a |
| Code TODOs on main (QuestChestManager, QuestManager) | Quest to-do | No date, no flag. STILL | RULE. Yes |

**Trello, mail and Drive, remaining rows**

| id | Reading B tried | kill quote and source | kill type |
|---|---|---|---|
| TMD-02 rows 9 and 14 | Already going out from the client, so Send, or held needs a client change | PUSH "only if its row is Ready and LIVE"; sheet R10 and R15 "WIP". "Anything else is held". See F3 | RULE. Yes |
| TMD-05 Endless ad entry | Still to do: third entry needs Rewarded Ads | [Doc Aug 14; Trello move 2025-09-23T00:34:30Z.] STILL "since this brief" | RULE. Yes |
| TMD-08 rows 1, 7, 12, 13 | No server push pipeline | Same held call either way: rows are Not Ready or WIP. PUSH | RULE. Yes; no call differs |
| TMD-09 permission prompt | Rows 3, 5 held | [Sep 18.] PUSH tests row and copy only. Robert's Sep 25 audio theory names no row | RULE. Yes |
| TMD-10 Nov quest tables | Quest Still to do | Text gone in rev 9: "reward tiers, the premium track and the season theme." All 3 copies checked | RECORD. Yes |
| TMD-11 Bug Checklist Endless lines | Endless art to-do | [Doc 2025-08-25.] STILL "since this brief". Only 1 Julia-reachable Drive file changed since Sep 20, the analytics dictionary | RULE. Yes |
| TMD-12 VFX Polish doc | Collect & Win reward animation (Marcus) | [Doc 2025-07-30.] STILL. Marcus names only the icon | RULE. Yes |
| TMD-13 "Profile for Leaderboard" | To-do | [Doc 2025-08-25.] STILL | RULE. Yes |
| TMD-14 Trello [64] | Bot scoring to-do | [Last activity Sep 12; no beat.] STILL | RULE. Yes |
| TMD-15 Trello [62] | Mid-span change | [Sep 12; no beat.] STILL | RULE. Yes |
| TMD-16 Trello [79] | Any beat | [Sep 23; empty; no beat.] STILL | RULE. Yes |
| TMD-18 row 12 name | Wrong event name | Brief: "the daily gift (the Login Calendar row on the push sheet)". Held anyway | RULE. Yes |
| TMD-19 "Weekly Update Oct 24" | "De-prioritize Zombie Match" in the recommendation | Reaches no listed cell. Drive date 2025-08-29, label after the clock; keep off the rubric and add to known issues | n/a |
| Row 1 quests | Held until Oct 13 | Not Ready. PUSH | RULE. Yes |
| Row 3 lives, row 5 seven days | Held: rev 9 dropped "only", so copy naming no game fails | Reply: "Copy that does not name the game at all is fine to go out, the naming rule is only about wrong names." | RULE. Yes |
| Rows 7, 12, 13 | Send | Not Ready and WIP. PUSH | RULE. Yes |
| Rows 2, 8, 10, 11 | Planned | Reply: "Leave off the four rows ... just those four." | RULE. Yes |
| R-01 | = rows 3, 5 | As above | RULE. Yes |
| R-02 | "Ready" in column B is enough | PUSH "Ready and LIVE" | RULE. Yes |
| R-03 | Row 1 note | Row Not Ready. Brief (rev 9): "whether the beat is in, which weeks it runs and whether its push goes out, not its window dates." | RULE. Yes |
| R-04 | Off rows | Reply; Trello [73] in Backlog | RULE. Yes |
| R-05 | Translated tab copy | Brief "the translated tab is the old Domino set" | RULE. Yes |
| R-06 | Other tabs | TAB | RULE. Yes |
| R-07 | Endless push row | TAB; no row exists | RULE. Yes |
| R-08 | Axe Arena in Oct 21 | Reply "things that are not in the beta"; Brian "once that event is back" | RULE. Yes |
| R-09 | Queue Manager open | Trello complete 16:40:22Z, after Calvin's 16:20:37Z | RECORD. Yes |
| R-10 | Trello [10], [27] open | dueComplete true | RECORD. Yes |
| R-11 | Consecutive login quest | ZOM-557 Done 2025-09-30 | RECORD. Yes |
| R-12 | Weekly star image, as art | ZOM-558 Done 2025-09-23 | RECORD. Yes |
| R-13 | Plague Race above level 100 | ZOM-459 Done 2025-08-25 | RECORD. Yes |
| R-14 | Plague Race unlock level | ZOM-413 Done | RECORD. Yes |
| R-15 | Reward Animations | Trello [22] complete; ZOM-463 Done 2025-09-15 | RECORD. Yes |
| R-16 | Endless skip, rocket button | ZOM-473, ZOM-474 Done | RECORD. Yes |
| R-17 | "12:00:01 AM Monday GMT" reset | Calendar "Monday 00:00 UTC". One second, no cell | RECORD. Yes |
| R-18 | Plague Race on Mon, Wed, Fri | Brief: "not its window dates" | RULE. Yes |
| R-19 | Collect & Win cadence | Matches the brief | RULE. Yes |
| R-20 | Oct 29 is a holiday | F15: any date before Oct 31 00:00 UTC | Boundary set by the brief |
| R-21 | Reply on Sep 22 mail | Brian Sep 26: "Treat Fri Oct 31 as the date I am committing to"; "reply on this mail" | RECORD. Yes |
| R-22 | Other release date | Only release event; organizer Douglas | RECORD. Yes |
| R-23 | Stale unchecked items, 13 on complete cards | [June.] STILL | RULE. Yes |
| R-24 | Data Dictionary and other analytics | STILL "not analytics". This is the one Drive file changed since Sep 20 | RULE. Yes |
| R-25 | Domino Drive files | Not ZM3D | RULE. Yes |
| Other open ZM ROADMAP cards: [55], [56], [60], [65], [66], [67], [72], [46], [48], [57], [59], [75], Backlog list | Still to do | [No action since the brief but a `dueComplete` on [55]; no beat.] STILL. Only 5 Trello actions on the board are since the brief, plus the injected comment | RULE. Yes |
| Other boards: UA/BD list "ZM 3d Technical Launch / Alpha", DD Product Roadmap, Harmony Games | Still to do | [Last activity March 2025 or Domino-era; no beat.] STILL | RULE. Yes |
| Gmail, GCal | New fork | No base mail or event in the window names a beat; only the injected items do | RECORD. Yes |

## 5. Checks on the census itself

- The census counts 97 open ZOM tickets. Post-SQL there are 96, because ZOM-563 closes.
- Census L-10 says QueueManager "matches the comment". The four EnqueueEvent lines do, but Collect & Win is not one of them; it runs through `RewardVFXManager.PlayCollectAndWin`. No effect on any cell.
- Rev 9's Oliver reply says "It is only that sweep on the art", but commit 25c6c66b6b also changes `TutorialEventManager.cs`. Harmless, since he is speaking of the sweep fix.
- All key Still-to-do items pass the new rule: vials Sep 29, icon Sep 30, server windows Sep 30, strip Sep 30, config Sep 26, and the held beat's fix. Rev 9's cutoff excludes none of them.

## 6. What I scanned and did not

Scanned:
- All rows in sections 3 to 9 of census_linear.md, sections 1 to 2 of census_github_confluence.md, and sections 1 to 5 of census_trello_mail_drive.md.
- Rev 9 SQL in full, the rev 9 change list, the platform report (Reading A, lines 338-476), truth.json, the solver rationale and the gradable surface for the push and Endless rows.
- Linear post-SQL state for all open ZOM tickets, rebuilt from the SQL.
- Julia's Slack (147 channels) Sep 17 to the clock, 2,299 messages, by keyword and ZOM id. All of #zm-animations from Sep 2 was read by message. June to September was keyword-searched for push and rename terms.
- All 5 ZM ROADMAP Trello actions since the brief. All Julia-reachable Drive files by modified date.
- GitHub: human reviews and comments since the brief, all CHANGES_REQUESTED, open PRs, #471 and #477 comments, CodeRabbit Critical and Major on beat PRs by keyword.
- match3d: NotificationManager.cs and its history, the three commits, Marcus's branch commits, QueueManager. match3d-backend: CDK schedules and log since Sep 15.
- Confluence: Season Pass spec, calendar and GDD in full; QA runbook, release checklist, engine, Nakama and AWS by the quoted sentences; all comments and version rows for the key pages.

Not scanned:
- Slack was not read message by message outside #zm-animations; that is the Slack slices' job. census_slack_bugs.md and census_slack_other.md were used only for cross-reference.
- Images and video attachments, including the Sep 30 shader image, so I cannot say which box it shows.
- SynthCut prefabs past 10,240 bytes, so I could not confirm in code whether the refill timer is animated.
- Linear keeps no line-level description history, so the age of ZOM-465's refill line is inferred from the ticket's base `updated_at` of Sep 23.
- Universe_Normal was used only to keep the F1 fix wording true; nothing from it is reachable at the clock.

Helper scripts are under R/work/closure_other/. Nothing was executed from the SQL, and nothing was written outside R/.
