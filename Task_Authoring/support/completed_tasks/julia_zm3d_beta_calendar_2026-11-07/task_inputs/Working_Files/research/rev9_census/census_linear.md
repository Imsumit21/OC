# Fork census, Linear slice (task_inputsS, SQL revision 8, sha 0e8c8ad8...)

Clock: 2025-10-01 07:00 UTC. All times UTC. "Julia sees" means a channel she is a member of, or an unscoped service.

## 1. Result

- 97 open ZOM tickets read one by one (section 8): 7 are real forks, 11 are weak candidates, 1 is the held beat (ZOM-429), and 78 are a No (no beat, off-calendar, analytics, or settled by a record).
- Section 3 has 17 rows, because some rows join tickets and two cover Done tickets. Only 2 of the 7 real forks were on the platform's list (ZOM-534, the #477 text).
- **Biggest new item: ZOM-563.** It is a prod-deploy gap on Season Pass premium frames, the exact kind of still-to-do the brief names, and Julia can see the to-do. The confirmation exists only in a DM she cannot read.
- **ZOM-534 is not a backend fix.** The fix is a client commit, and the endpoint lives in a separate service repo with no commits since July. Nothing in it rides on the Oct 8 release. The platform's suggested outcome "ships with the Oct 8 backend release" would be false to the base. Do not use it.
- **#477 is not polish nobody flagged.** Vincent flagged the strings and Brian agreed, in a DM Julia cannot see. #477 also has a second player-facing commit the platform has not raised (info-screen text).
- Open non-ZOM tickets (149): 3 name ZM3D (ART-790, ART-792, ENG-2258). None is a beat item. The Win & Collect tickets are Domino Delights.

## 2. What I scanned

**Linear (complete).** Base `linear/data.json`: 3,687 issues, 553 ZOM, 0 comments in the base. The only comments in the universe are the SQL's 26, on 21 issues. Post-SQL state built by parsing all 26 comment INSERTs and 20 issue UPDATEs. Every field of all 97 open ZOM tickets read, descriptions in full. All 149 open tickets in ENG, ART, DES and EPI listed by title and keyword-scanned on title, description and labels. All 553 ZOM tickets scanned for closed beat tickets since Aug 10 (19 found).

**Cross-references per ticket (complete regex, not message-by-message reading).**
- Slack: all 4,840 files, 610,468 messages, for any `ZOM-nnn`, with Julia membership flagged per channel.
- GitHub `data.json`: 2,475 PRs (title, body, head ref), 11,226 commits, PR comments, review comments, reviews, 1,824 branches.
- Trello `data.json`: all arrays. Confluence: pages, comments, versions.
- Gmail: all 81,404 thread files for `ZOM-`. 156 Linear or GitHub notifications, none in Julia's mailbox, bodies empty.
- GDocs, GDrive, GCal: grep for 11 key IDs, 0 hits.

**Targeted reads.** #zombie-bugs Sep 7-12 and Sep 29-30, and threads 1757289825.998289, 1758031982.956109, 1759249488.495439, 1758001153.294589, 1757998501.671659, 1756202193.675789, 1757558514.626259. #zombie-match3d threads 1755108052.016359, 1758215891.943009. #zombie-design Sep 22 and Sep 29-30. #zombie-art thread 1757890558.725009. #zm-animations Sep 12. #builds Sep 5-30 submission lines. DMs D079SNE2TL4 (Sep 22-23, 30), D07GY332589 (Sep 10), D07GMT8NVM2 (thread Sep 12), D05QUH5URK2 (Sep 22), D0770ET6WBW (Sep 23, 29-30), D0770ET1HV2 (Sep 30), D07E9PSQB6W (Sep 30), D076V3NB6P7 and D05TZ6N23F1 (Sep 23), #executives (Sep 11). Keyword scans: samsung/s23/galaxy, golden frame, deploy/prod, leaderboard/league, daily gift, season pass, refill timer, red dot, release. Git history of match3d, match3d-backend, match3d-quests, match3d-backend-auth.

**Not scanned or not possible.**
- No Slack channel was read message by message for the whole month. That is the Slack slice.
- Linear image and video attachments were not opened, and neither were Slack images.
- The #477 diff could not be read. Its branch and commits are not in the exported repo or `commit_map`, so what the header says before and after is unknown.
- Exported prefabs are truncated, so sprite and material references cannot be traced. This blocks two checks: the CodeRabbit "Critical" GUID note on #471, and which box the Sep 30 shader thread is about.
- Trello: only the "Minor Bugs to Fix" card, the "Fix TECH ISSUES" card and the BETA list states were read.

## 3. Unsettled and weakly settled candidates, ranked

Brief's still-to-do test: "what still has to land before it runs for bought users (prod deploy, config, player-facing art an owner has flagged) and who owns it. Not what already shipped, not analytics, not polish nobody flagged."

Latest possible date for any new record is 2025-10-01T06:59Z.

| id | beat | where it lives | how a reader would use it | basis | what the base truly shows | best minimal settling record |
|---|---|---|---|---|---|---|
| L-01 ZOM-563 (NEW) | Season Pass (premium frames and names); also Teams, not a beat | Linear ZOM-563, In Progress since Sep 30, P2, assignee Douglas, creator Vincent, no comment. Title "Teams' lives, golden frames and names not working on prod env". Description "It works great in dev env, but in prod it doesn't." Plus #zombie-bugs (Julia member) thread 1758031982.956109, Vincent, 2025-09-16 14:13, under To Dos: "Deploy teams and profile changes to prod (about premium pass avatar & frames etc)" tagging Douglas | Season Pass Still to do: "teams/profile premium frames to prod (Douglas)". Reading A has nothing. "prod deploy" is the first kind the brief lists | SILENCE. Nothing Julia can reach says the deploy happened; the open ticket says it has not | Done before the clock, in a DM Julia cannot see. D079SNE2TL4 (Vincent, Douglas): Sep 23 17:44 Vincent "one ticket about the social stuff is not deployed to prod"; Sep 30 18:16:33 Douglas "Ok, I updated the prod environment with the latest teams/social changes, let me know if you are still getting those issues"; Sep 30 21:58:44 Vincent "Yep it works as expected". Golden frame is the Season Pass premium perk: Owen, Sep 8, D07J501DBNE "all players with season pass should have golden frame"; PR #438 commit 3ed959b3c "setting golden frame on premium buy". Listed in known issue SC-16 | Linear comment on ZOM-563, author Vincent (usr_65c76e0b87aa7e9b), tester not owner. Earliest 2025-09-30T21:58:44Z. Says Douglas updated prod with the latest teams and social changes and that lives, golden frames and names now work on prod. Optional UPDATE to Done. Outcome: nothing left |
| L-02 ZOM-534 (platform P1-DR4) | Quest rollover | Linear ZOM-534, In Progress, P1, assignee Douglas, title "Quest points not resetting until app restart in production". cmt_zom534_1, Douglas, 2025-09-25T16:35:04Z: "That is on main, so nothing else has to land for the beta. I am keeping this open to watch one backend timing edge case on the day boundary." #zombie-bugs Sep 10 23:55 Leonard: "it's hard to test on prod without waiting a day - if you feel confident let's just take it in lol". Sep 11 00:03 Oliver: "yeah its on main", "I tested with Douglas", "settings resets to 1 minute on dev" | Quest rollover Still to do: "ZOM-534 fix to prod (Douglas)", or "watch backend timing edge case (Douglas)", or nothing | SCOPE_GAP. Owner's own claim, "main" against a production ticket, and Julia-visible chat shows dev-only testing | Client fix, not backend: match3d commit 47c65623e7, Oliver, Sep 10 23:53, "Using remaining-time endpoint to sync quests end with client" (QuestAPI, QuestManager, QuestTimerAPI, QuestsMainScreen). Endpoint `/quest-remaining-time` is in repo match3d-quests, present in its prod swagger since Jun 17; that repo has no commit after Jul 10. Reached players through client builds, a chain Julia can see but which names no ticket: #builds iOS Submission #36 (Sep 11 00:28) lists the commit; #zombie-match3d Sep 23 16:02 Arthur "update the match3d required versions: Android: 0.3.127 iOS: 0.3.40"; Sep 29 21:55 Leonard "I just released 0.3.49 on IOS" (version equals submission number). Confirmation Julia cannot see: #executives Sep 11 01:04 Leonard "my quest points are reset", 01:08 "everything else looks good on submission build 36 on ios". The "edge case" maps to D07GMT8NVM2 Sep 12: Vincent's parse error on `{"daily":"0:10:60"}`, Oliver "Douglas sent a fix for this" | Two edits. (a) Linear comment on ZOM-534, author Leonard (usr_63fffeb4fab5233e), the reporter, not the owner. Earliest 2025-09-30T00:05Z (first UTC day boundary after 0.3.49 went live), or after 2025-10-01T00:00Z. Says the fix is client-side, live in iOS 0.3.49, and he stayed online through the reset and points cleared with no restart. (b) Delete the last sentence of cmt_zom534_1; it is a fork by itself. Outcome: nothing left. Do not use "ships with the Oct 8 release" |
| L-03 ZOM-566 / PR #477 (platform P1-DR3, plus NEW commit) | Collect & Win | ZOM-566 "Collect&Win Analytics", In Progress via SQL, assignee Owen. cmt_zom566_1 2025-09-30T19:40:47Z: "Wiring both into the analytics manager now, ahead of the beta." PR match3d#477 open, 2025-09-30T22:26:30Z, "Collect And Win Analytics and title change". Commits c7d3bc6f2 "Change text on Collect And Win info screen" (not raised by the platform), 9dc995cb3 "Changed titled to collect and win main screen header" | Collect & Win Still to do: "#477 header and info-screen text (Owen)", or nothing | SILENCE. No record names either text change | Text changes trace to D0770ET1HV2 Sep 30 08:45 (Vincent, Brian; Julia not a member; Turkish): Vincent "Bence burada bazı stringlerin düzelmesi lazım" (some strings here need fixing), "Token çok sırıtıyo" ("Token" sticks out). Brian "evet isim gerek" (yes it needs a name). D07E9PSQB6W Sep 30 16:27 Brian to Owen: "If we add this today release, it'll be great!" #477 opened after iOS 50 (19:15) and Android 135 (20:13), so it missed both submission builds. So it was flagged by QA and agreed by design, which cuts against "polish nobody flagged" | Comment on ZOM-566 or #477, author Brian (usr_fc22d5941b2aeb5c), 2025-09-30T22:26Z or later, naming both text commits. Two possible outcomes. (a) Most faithful to the base: the text is wanted before Collect & Win runs, owner Owen, and the answer key gains a still-to-do. (b) Keeps the key: Brian says the text rides with the analytics PR and the event can run without it. The base does not contradict (b), but it does not support it either |
| L-04 ZOM-465 refill timer (NEW) | Endless Monster Mode | ZOM-465 "Endless Mode Master VFX Ticket", In Progress, P2, Marcus. Only item not struck through: "### Refill Timer ticking animation as well as color change from 5 to 1." then "(i've seen that the refil counter it's already animated do we still need to do that?)". #zm-animations Sep 12 11:41 Brian's list, unstruck: "*P1/P2 – Endless mode remaining VFX* ( ...ZOM-465...ticket )" | Endless Still to do: "refill timer animation (Marcus)". Marcus's open question has no answer | SCOPE_GAP. The only cover is cmt_zom565_1, on another ticket about the start screen. cmt_zom465_1 and _2 speak only to icons | Nobody answered the question in any export. Marcus was still on it: Sep 23 D05TZ6N23F1 "There are some Core-Game animations that i need to do also"; Sep 30 commit 7683df0351 "infiniteBoss and endless mode core gameplay ui vfx wip" on Marcus/EndlessMode_Vfx_NewUnity, not on main. Sep 23 D076V3NB6P7 Brian: Robert owns endless and boss arena; "the ticket was made by" Vincent | Comment on ZOM-465, author Vincent (ticket creator) or Robert (mode owner). Earliest 2025-09-23T14:16Z (ticket's base update). Says the refill counter is already animated, the line is dropped, the remaining endless VFX is polish and not needed for the beta. Outcome: out |
| L-05 ZOM-542 (platform F24 accepted it; own claim under this standard) | Endless Monster Mode (Boss Arena is off) | ZOM-542, state Regression, P2, label Hot Fix - Global Launch, Samuel. #zombie-art Sep 14 22:55 Robert: "We need to update our home screen for endless mode and boss arena, as well as the end game victory score screen for both these modes". cmt_zom542_1 Samuel 2025-09-22T18:40:21Z: "Picking this up after the bug list... a layout refresh on screens that already work, so they are not needed for the beta." | Endless Still to do: "home and victory score screen update (Samuel)" | SCOPE_GAP. Only the assignee's own claim answers Product's "We need" | No PR or commit for it found (match3d, Sep 10-30). Sep 15 #zombie-art: Robert "The current score that you just received needs to be emphasized more"; Martin "If we change the layout of the screen we need to change the animations". No later word on the beta. Label suggests it is a launch item, but no record says so | Comment on ZOM-542, author Robert (usr_Robert), the requester and mode owner. Earliest 2025-09-22T18:41Z. Agrees this waits until after the beta. Outcome: out |
| L-06 ZOM-556 (NEW as a still-to-do; platform F26 covered only the hold) | Daily gift (Login Calendar) | ZOM-556, Todo, P2, Calvin, "When the daily gift is skipped, it doesn't reset to 0." cmt_zom556_1 Vincent 2025-09-24T15:20:38Z: "Claimed the daily gift on the submission build after skipping a day... the lower day row still carries on instead of going back to day 1, but claiming works and nothing is lost." | Daily gift Still to do: "day-row reset fix (Calvin)" or "re-check on prod", or nothing. Status is unaffected | Hold: RECORD (brief "Wrong counters ... do not hold a beat"). Still-to-do: SILENCE. The counter clause sits under Held, nothing says the fix need not land, and the test was on the submission build while the report came from prod | Fix not done. D079SNE2TL4 Sep 22 16:18, forwarded from Calvin: "I think this is backend change... I just consume what backend sends me". D05QUH5URK2 Calvin: Leonard reported it on prod. Douglas said he would sync. No commit in match3d-backend. So the real owner is likely Douglas, not assignee Calvin | Add one sentence to cmt_zom556_1 (same date, Vincent): the row fix does not have to land before the beta. Outcome: out. Removes the owner question too |
| L-07 ZOM-559 (NEW; same family as platform P1-DR5) | No single beat; every level-based beat, closest to Endless | ZOM-559, Todo, P2, Oliver: "if I were to finish a level, I hard freeze at end game victory screen", "Doesn't happen to me, might be again a Samsung issue but I need to see video". Trello "Minor Bugs to Fix" on list BETA: Oct 10. #zombie-design Sep 22 18:00 Vincent: "I think we have problems specific to Samsung devices. Just like glass vfx issues, I haven't experienced the airstrike freeze, notification muting the game." | "verify the Samsung freeze and sound (Oliver)" under the brief's "an unverified build or platform is a still-to-do" | SILENCE | Looks real and unresolved. Sep 11 02:41 Robert's report. Sep 22 23:02 #zombie-design Robert "The app froze hard for a user at end of level 21. Requiring a hard restart." Sep 23 #zombie-bugs Samsung S24 crash at end of level 20. Sep 25 Robert's permission-prompt theory. #executives Sep 21 05:13 (Julia cannot see) Leonard "Endless mode was unplayable on my friends samsung s23 ultra phone". No fix found | Settle with the Sep 21 S23 item in one record (coordinate with the Slack slice), Vincent or Robert, on ZOM-559 or #zombie-bugs, Sep 25 or later. (a) Most faithful: Samsung verification becomes a still-to-do with an owner and the key changes. (b) A Product decision that the Samsung issues are device-wide, tracked here, and gate no beat. A "cannot reproduce on Samsung" outcome would not be true to the base |
| L-08 ZOM-546 (NEW, weak) | Endless Monster Mode | ZOM-546, Todo, P2, Owen. Trello: "Refill algorithm spawns fewer items over time for both events." cmt_zom546_1 Owen 2025-09-24T19:00:57Z: "Refill counts hold level across a long endless run here, the board refills the same amount at the 40th refill as at the second." | Endless Still to do: "verify refill on prod (Owen)" | SCOPE_GAP. Assignee's own claim, and "here" names no build | Consistent with a fix: PR #453 "Manual refill logic" merged 2025-09-22T16:13Z ("Improves Endless Mode object refill timing"). Ticket simply not closed | Replace "here" with a named build in cmt_zom546_1, or add a one-line Robert re-test like ZOM-517. Earliest 2025-09-22T16:14Z. Outcome: out |
| L-09 ZOM-565 (weak; platform F24) | Endless Monster Mode | ZOM-565, Todo, P3, assignee Calvin, creator Marcus. cmt_zom565_1 2025-09-29T14:34:12Z: "This is the P1/P2 endless polish from the list Brian gave me, the screen already works without it, so it is not needed for the beta." | Endless Still to do: "start screen bar and glow (Calvin)" | SCOPE_GAP, weak. The art owner's own call; assignee and Brian silent. But it is an explicit not-needed on the exact item | Comment matches base: commit 44988da015 Sep 29 "...it's still hidden in there for you to use"; DM Sep 29 14:34 "i wrote a comment on the linear task" | Covered if the L-04 record says the remaining endless VFX is polish |
| L-10 ZOM-543 (weak) | Collect & Win; by omission Plague Race, Endless, Leaderboard | cmt_zom543_1 Calvin 2025-09-30T16:20:37Z: "Queue manager is in progress. Adding panel-order entries as each live-ops feature lands; current flow is level_end, daily_gift, season_pass, tutorial plus Collect and Win." | "queue entries for the other beats (Calvin)" | RECORD for Collect & Win (comment, PR #472 merged Sep 30, Trello "Queue Manager" dueComplete true, last activity 2025-09-30T16:40:22Z). SILENCE for other beats, weak | QueueManager.cs on main enqueues Level_end_animations, daily_gift, season_pass_event, unblock_tutorials, matching the comment | Optional reword: end with "that is everything the beta needs" |
| L-11 ZOM-528, ZOM-541, ZOM-521 (platform F33, Reading D resolved) | No beat (card packs) | cmt_zom521_2 Calvin 2025-09-30T16:27:38Z: "Card pack animation went in with #475. I am leaving this item, ZOM-528 and ZOM-541 open until Brian has seen it in a build." ZOM-528 and ZOM-541 have no comments | "Brian checks card VFX in a build", under "unverified build" | RECORD per platform ("went in with #475" plus "master ticket for VFX polish"). The clause still invites the reading | #475 merged Sep 30 16:09, before iOS 50 and Android 135 started. D0770ET6WBW Sep 29 Brian: "I'll test it tomorrow", "it looks great on the video". No record that he did | Optional: drop "until Brian has seen it in a build" |
| L-12 ZOM-544 (weak) | No beat; description lists Season Pass, quest and leaderboard progress | cmt_zom544_1 Vincent 2025-09-29T15:35:50Z: "Apple sign-in works from the settings menu, but progress does not restore yet: levels, currencies and cards are not synced." Trello "Google/Apple Login" on BETA: Oct 10, not complete | "sign-in progress sync (EMPLOYEE_0032)" as a general still-to-do | SILENCE, weak. Not an event window, reset or start push | Work continues: Sep 30 D079SNE2TL4 Vincent "after the data sycning for sign in" | None needed unless the key wants it stated |
| L-13 ZOM-475 (weak; SC-8) | No single beat | ZOM-475, Todo, P1, Oliver. Trello Minor Bugs. #zombie-design Sep 10 21:24 Vincent: "it's still happens for samsung devices" | "verify the glass crash on Samsung" | RECORD, contested. Confluence page_zm3d_gdd (Sep 30): "fixed by removing the glass SFX and VFX"; #zombie-match3d Sep 10 18:54 Robert pushed the removal. Ticket still Todo and PR #435 re-added glass FX (SC-8) | Status truly conflicting in the base | Name it in the L-07 Samsung record |
| L-14 ZOM-359, ZOM-449, ZOM-468 (weak) | No single beat | ZOM-359 Regression P2 "Phone heating up too much"; ZOM-449 and ZOM-468 low-end Android artifacts | "performance on low-end or Samsung" | SILENCE, weak. Brief covers performance and cosmetic gaps only under Held | Heating also reported on S23 (#executives Sep 22, Julia cannot see) | None |
| L-15 ZOM-432 (Done via SQL; weak; platform F25) | Daily gift | cmt_zom432_2 Samuel 2025-09-30T21:07:26Z: "The frame went out with PR #471. It is in both submission builds from today, iOS 50 and Android 135, so nothing is left here. Closing." | "frame reaches players once stores approve the Sep 30 builds" | RECORD. Author is the PR author, not assignee Calvin, and PR #471 is independent evidence. Residual: "submission" is not live | #471 merged Sep 30 15:52, commit "Fixing UI Elements on Daily Gift ... update header image" changes `img - DailyGift.png`; iOS 50 started 18:43, so it is included. No commit says "frame". CodeRabbit "Critical" GUID note on that sprite has no human reply; could not trace it | None. The deck ties the buy to those builds |
| L-16 ZOM-344 (Done via SQL; weak) | Quest rollover | cmt_zom344_1 Marcus 2025-09-16T16:20:28Z: "Art side is signed off on my end." Base state was Todo; the SQL closes it | "quest box animation integration" | SCOPE_GAP, weak. Assignee, creator and closer are one person; "Art side" leaves code unsaid. But nobody flagged it and the comment says it "reads well on the quest screen" | No commit found for a quest box open and close animation (match3d, Jul-Sep). Label Hot Fix - Global Launch | Optional: drop "Art side ... on my end" or leave the ticket as base. It does not need closing for the task |
| L-17 ZOM-484, ENG-2258 (weak) | Off-calendar only | ZOM-484 Todo P4: every beat ticked, "- [ ] Axe Arena" and parent "- [ ] Live-ops" open. ENG-2258 Todo: same list, all unticked, but "tutorials we use in Domino Delights" | "infographic animations" | RECORD (ZOM-484's ticks; Axe Arena not in the beta per the DM reply) | Brian's Sep 12 list still shows P2 infographic animations | None |

## 4. Candidates settled by a record (kept so they are not re-opened)

| id | beat | locator | reader's alternative | settled by (quote) | base check |
|---|---|---|---|---|---|
| ZOM-429 | Weekly Leaderboard | Backlog P3 Douglas; cmt_zom429_1 Sep 16 "if a player force-closes and reopens, they land in the new week fine, so not blocking" | Not held | RECORD, non-owner, later: Vincent #zombie-match3d Sep 30 20:50 "I killed the app and reopened it twice... my week is still last week one. Same on the second device." | No Slack, PR or commit cites the ticket. Only a Jul 22 assignment mail |
| ZOM-526 | Collect & Win, Season Pass | In Progress, unassigned | Token travel still to do | RECORD: Brian Sep 26 "it does not have to land before the beta"; Calvin Sep 30 "Only the Axe Arena travel is left here" | PR #472 merged Sep 30 15:53 |
| ZOM-471 | Plague Race | Todo P3 Samuel, "Add red dot icon" | Red dot still to do | RECORD beyond the owner: #zombie-match3d Aug 13 18:32 Leonard "yeah, we don't need it! cancel the ticket", 20:28 "I don't think we should do it" | The comment's claim is accurate |
| ZOM-504 | Endless | Backlog, EMPLOYEE_0032 | Persistent objects bug | RECORD, reporter: "Visual only, no board state affected." | Base Aug 25 and Sep 3 DMs only |
| ZOM-517 | Endless | Backlog P2 | Enrage bug | RECORD, reporter: Robert "could not get one to lose it while walking." Build unnamed, minor | None against it |
| ZOM-552, ZOM-442, ZOM-549, ZOM-548, ZOM-387, ZOM-386, ZOM-400, ZOM-439, ZOM-441 | Analytics | Season Pass, trophy, endless_left, Boss Arena, general | Analytics still to do | RECORD: brief "not analytics" | ZOM-552 P0 means no priority set |
| ZOM-505 | No beat | Backlog, Vincent: "you can't proceed" | FTUE blocker | RECORD: #zombie-match3d Sep 18 17:46 Brian "It doesn't seem to be blocking it". Old version V 1736 | Aug 26 Vincent "the tutorial was always like that" |
| ZOM-562, ZOM-390, ZOM-62 | Off-calendar | Boss Arena orphans; Axe Arena visual (assigned to Julia); Dead Eye spec | None | RECORD: brief "Boss Arena is off this calendar"; DM reply on Axe Arena | None |
| ENG-2331, ENG-2349, ENG-2353 | None | Open "Win & Collect" tickets | Mistaken for Collect & Win | RECORD: versions and crash links are Domino Delights | Not ZM3D |

## 5. Every injected Linear comment: does its wording fork?

| comment | author (role) | fork from wording? | note |
|---|---|---|---|
| cmt_zom534_1 | Douglas (assignee) | **Yes, three** | "on main" against prod; "nothing else has to land" is own claim; "watch one backend timing edge case" is a named open item and "backend" pulls the reader to the Oct 8 release. Delete the last sentence (L-02) |
| cmt_zom521_2 | Calvin (assignee) | **Yes** | "until Brian has seen it in a build" matches "unverified build" (L-11) |
| cmt_zom542_1 | Samuel (assignee) | **Yes** | "Picking this up after the bug list" says work continues; "not needed" is own claim against Robert's "We need" (L-05) |
| cmt_zom556_1 | Vincent (creator) | **Yes** | "on the submission build" is not prod; silent on whether the fix must land (L-06) |
| cmt_zom546_1 | Owen (assignee) | **Yes, mild** | "here" names no build (L-08) |
| cmt_zom566_1 | Owen (assignee) | Mild | "ahead of the beta" reads as must-land, the brief answers it; silent on the #477 text (L-03) |
| cmt_zom543_1 | Calvin (assignee) | Mild | "in progress", "as each live-ops feature lands" (L-10) |
| cmt_zom565_1 | Marcus (creator) | Mild | "P1/P2" and "for you to hook up" read as live work (L-09) |
| cmt_zom544_1 | Vincent (creator) | Mild | "does not restore yet" (L-12) |
| cmt_zom344_1 | Marcus (owner) | Mild | "Art side ... on my end" (L-16) |
| cmt_zom432_2 | Samuel (PR author) | Mild | "submission builds" (L-15) |
| cmt_zom465_2 | Marcus (assignee) | By omission | Clear on the icon, silent on the refill timer (L-04) |
| cmt_zom517_1 | Robert (reporter) | Very mild | Build unnamed |
| cmt_zom465_1 | Marcus | No | Corrected by _2 by design |
| cmt_zom429_1 | Douglas (assignee) | No new fork | Designed decoy, closed by Vincent's Sep 30 re-test |
| cmt_zom432_1 | Calvin | No | Superseded by _2 |
| cmt_zom521_1 | Calvin | No | Superseded by _2 |
| cmt_zom526_1 | Brian | No | Superseded by _3 |
| cmt_zom526_2 | Brian | No | Says "does not have to land before the beta" |
| cmt_zom526_3 | Calvin | No | Clean |
| cmt_zom552_1 | Oliver | No | Analytics |
| cmt_zom442_1 | Oliver | No | Analytics, no beat |
| cmt_zom549_1 | Vincent | No | Analytics |
| cmt_zom471_1 | Samuel | No | Own claim, but Leonard's thread backs it |
| cmt_zom504_1 | Vincent | No | "Visual only" |
| cmt_zom78_1 | Frederick | No | Destination only |

## 6. Done tickets touched by the SQL

Only two: ZOM-432 (L-15) and ZOM-344 (L-16). Both were Todo in the base. ZOM-432's closing is backed by merged PR #471, so it is not owner-only. ZOM-344's closing is owner-only, but nothing rests on it: the quest rollover does not depend on a box animation. The other state change is ZOM-566, Todo to In Progress.

## 7. Notes for other slices (outside Linear, found on the way)

- **Season Pass fixes landed after the Sep 30 submission builds.** iOS 50 and Android 135 started 18:43 and 18:45. After them on main: 25c6c66b6b (21:20) "Ensuring that in level popups are only called in normal levels; removing popup tutorial from level model endless_02"; 93f45ebbfc (21:36) "Fix season pass main screen instance from join popup"; 0ff577550e (Oct 1 05:44) "Fix end popup". The bug behind the second: D07GMT8NVM2 Sep 30 17:17 Vincent "After the addressable, sp is not opened after it's introduced. Clicking continue button doesn't redirect me" (Julia cannot see). #builds does show the fix on iOS Internal #1759. If the submitted builds carry that bug, this is a Season Pass still-to-do no record speaks to.
- **Sep 16 #zombie-bugs list** (thread 1758031982.956109), no open ticket for these: "After purchasing premium pass, lives are reset to 8 after every win", "After purchasing premium pass, the refill doesn't refill 8 lives", trampoline timer rewards in Season Pass, "Rearrange rewards until win streak freezer duration is implemented" (Brian).
- **Sep 30 #zombie-bugs thread 1759249488.495439**, no ticket: Vincent "i think we should squeeze in the fix for that issue if it's an easy fix... players can see that for 10 times in a day"; Marcus on the "lightSweep Box Variant" shader; Oliver "will work on this asap". Julia sees it. I could not tell which box, since the image is unread and prefabs are truncated.
- **S23 follow-up exists.** Vincent's Sep 22 #zombie-design line ("airstrike freeze") reads as a Julia-visible follow-up to Leonard's Sep 21 report, and it supports the fork rather than closing it.
- Sep 7 #zombie-bugs: Leonard "Endless horde finished and didn't restart", "Killing the app doesn't solve the issue"; Douglas "Solved, try again please".

## 8. All 97 open ZOM tickets, one by one

Priority: 1 Urgent, 2 High, 3 Medium, 4 Low, 0 none set. "Could it go in Still to do?" is the reader test, not the expected answer.

| ticket | state | P | assignee | title | beat touched | could it go in Still to do? |
|---|---|---|---|---|---|---|
| ZOM-359 | Regression | 2 | arthur.blake | Phone heating up too much after playing 15 to 20 levels. | all modes | Weak, L-14 |
| ZOM-542 | Regression | 2 | samuel.turner | Update home screen and victory score screen for game modes | Endless | Yes, L-05 |
| ZOM-442 | In Validation | 2 | oliver.brooks | Analytics Instrumentation for Tropy Reward Redeem | none (trophy road) | No, analytics |
| ZOM-548 | In Validation | 2 | EMPLOYEE_0032 | Track events for boss arena as listed in the spreadsheet | Boss Arena (off) | No, analytics, off |
| ZOM-549 | In Validation | 2 | EMPLOYEE_0032 | Add new fields to left_level and endless_left analytics events | Endless | No, analytics |
| ZOM-202 | In Progress | 3 | arthur.blake | Minimize or migrate selection panel for easier difficulty tab  | none | No, level editor |
| ZOM-311 | In Progress | 2 | arthur.blake | Consider migrating the list of items and list of monsters to b | none | No, level editor |
| ZOM-465 | In Progress | 2 | marcus.bennett | Endless Mode Master VFX Ticket | Endless, Collect & Win | Yes, L-04; C&W icon is in Reading A |
| ZOM-467 | In Progress | 2 | marcus.bennett | Zombie Match 3d - Marketing Videos | none | No, marketing video; "production" means video production |
| ZOM-513 | In Progress | 1 | claire.morgan | Convert Maracas into multi-color variant-enabled | none | No, item art, SC-16 |
| ZOM-514 | In Progress | 1 | claire.morgan | Request to add motorcycle helmet as a survival item | none | No, item art, SC-16 |
| ZOM-521 | In Progress | 2 | calvin.price | Master Ticket - VFX implementation | Collect & Win, Season Pass tokens | Weak, L-11 |
| ZOM-526 | In Progress | 2 | - | Tokens traveling to live-ops | Collect & Win, Season Pass | No, section 4 |
| ZOM-528 | In Progress | 2 | calvin.price | Claimed Cards traveling to inventory section | none (cards) | Weak, L-11 |
| ZOM-534 | In Progress | 1 | douglas | Quest points not resetting until app restart in production | Quest rollover | Yes, L-02 |
| ZOM-541 | In Progress | 2 | calvin.price | Cards Collect Vfx animation | none (cards) | Weak, L-11 |
| ZOM-543 | In Progress | 2 | calvin.price | Queue Manager | Collect & Win | Weak, L-10 |
| ZOM-544 | In Progress | 2 | EMPLOYEE_0032 | Implement Google Apple Login | none directly | Weak, L-12 |
| ZOM-552 | In Progress | 0 | oliver.brooks | Season Pass Analytics | Season Pass | No, analytics |
| ZOM-563 | In Progress | 2 | douglas | Teams' lives, golden frames and names not working on prod env | Season Pass premium | Yes, L-01 |
| ZOM-566 | In Progress | 2 | owen.baker | Collect&Win Analytics | Collect & Win | Analytics no; #477 text yes, L-03 |
| ZOM-62 | Todo | 4 | vincent.parker | Zombie Ops #3 Spec (Dead Eye) | Axe Arena type (off) | No, off |
| ZOM-97 | Todo | 4 | robert | REVISION FOR ITEMS | none | No, item art |
| ZOM-118 | Todo | 2 | marcus.bennett | Shop Animations Master Ticket | none | No, shop VFX |
| ZOM-130 | Todo | 2 | leonard.hayes | Create an out of moves screen flow with offers | none | No, out-of-moves flow, not a beat |
| ZOM-171 | Todo | 3 | martin.walsh | Icon for double damage in-game boost | none | No, future boost |
| ZOM-181 | Todo | 4 | claire.morgan | 8. Vaious Solid color Plates/cups/mugs/egg on plates | none | No, item art |
| ZOM-182 | Todo | 4 | claire.morgan | 9. Bagel | none | No, item art |
| ZOM-184 | Todo | 4 | claire.morgan | 11.Curling Iron (Maybe Drop the item) | none | No, item art |
| ZOM-292 | Todo | 2 | arthur.blake | Level Editor Improvements 2.0 | none | No, level editor |
| ZOM-293 | Todo | 4 | robert | Dynamic Difficulty Tiering Down Issue | none | No, difficulty tooling |
| ZOM-342 | Todo | 4 | claire.morgan | Indoor Plant | none | No, item art |
| ZOM-348 | Todo | 2 | - | Rotating Shop Discount Issues | none | No; Rotating Shop has no schedule in backend config and no PNs Beta row |
| ZOM-386 | Todo | 2 | douglas | Track Player Card Inventory and Sync to BigQuery | none | No, data |
| ZOM-387 | Todo | 2 | arthur.blake | Giant Analytics Ticket | mentions plague_race_start, quest events | No, analytics |
| ZOM-400 | Todo | 0 | arthur.blake | We want to add a new field to left_level event to track what u | none | No, analytics |
| ZOM-427 | Todo | 2 | arthur.blake | App icon is too zoomed in for android | none | No, app icon |
| ZOM-438 | Todo | 1 | arthur.blake | Investigate why some zombie tracks do not spawn | none | No; "zombie tracks" are spawn lanes, not Zombie Lane |
| ZOM-439 | Todo | 0 | arthur.blake | Investigate card_upgrade event not recording correctly | none | No, analytics |
| ZOM-441 | Todo | 2 | arthur.blake | Fix reward_str and chest_content_str sending issue | none | No, analytics |
| ZOM-443 | Todo | 1 | arthur.blake | Investigate non-random item removal from board due to win stre | none | No, core gameplay |
| ZOM-453 | Todo | 3 | samuel.turner | Fix text inconsistency | none | No, text; parent ZOM-450 Done |
| ZOM-458 | Todo | 4 | arthur.blake | Quitting algo levels still makes the level change animation | none | No, algo level animation |
| ZOM-468 | Todo | 2 | arthur.blake | Low-end devices rendering issues | none directly | Weak, L-14 |
| ZOM-471 | Todo | 3 | samuel.turner | Add red dot icon for players not in Plague Race | Plague Race | No, section 4 |
| ZOM-475 | Todo | 1 | oliver.brooks | Consecutive glass impact sfx/vfx causes crash on android | none directly | Weak, L-13 |
| ZOM-477 | Todo | 3 | EMPLOYEE_0032 | DOT kills can take too long and cause perceived unresponsivene | none | No, kill cam UX |
| ZOM-481 | Todo | 1 | owen.baker | Zombie Health bar persists too long after death. | none | No, core gameplay |
| ZOM-483 | Todo | 3 | calvin.price | Infinite lives from new-install are not granted, rewards 30 mi | none | No, new-install lives; on Trello Minor Bugs |
| ZOM-484 | Todo | 4 | marcus.bennett | Info Screen Animations | all beats ticked; Axe Arena open | No, L-17 |
| ZOM-508 | Todo | 3 | oliver.brooks | Assisted Start | none | No, FTUE; Oliver asked Julia Sep 23 in a DM |
| ZOM-520 | Todo | 4 | oliver.brooks | First loss as level doesn't reset win streak | none | No, win streak |
| ZOM-535 | Todo | 1 | EMPLOYEE_0032 | Fast matching might target an already-dead zombie | none | No, core gameplay |
| ZOM-539 | Todo | 2 | samuel.turner | Implement Red Dot for Cards and Shop | none | No, cards and shop red dots |
| ZOM-545 | Todo | 0 | douglas | Ingest bot params from a spreadsheet | none | No, bot params |
| ZOM-546 | Todo | 2 | owen.baker | Bug: refill algorithm spawns fewer items over time | Endless | Weak, L-08 |
| ZOM-554 | Todo | 1 | owen.baker | Quiting level mid tornado boost breaks the object physics | none | No, core; a restart clears it |
| ZOM-556 | Todo | 2 | calvin.price | When the daily gift is skipped, it doesn't reset to 0. | Daily gift | Yes, L-06 |
| ZOM-559 | Todo | 2 | oliver.brooks | Homing out on android(samsung), sound disappears. | none directly; level end | Yes, L-07 |
| ZOM-560 | Todo | 1 | samuel.turner | The abandoned pack win streak freezer reward is not granted. | none | No, shop pack reward |
| ZOM-562 | Todo | 1 | owen.baker | Orphan items in boss arena | Boss Arena (off) | No, off |
| ZOM-564 | Todo | 3 | oliver.brooks | "Free" label stays on boosters after Tutorial | none | No, tutorial label, SC-16 |
| ZOM-565 | Todo | 3 | calvin.price | Endless Horde Start Screen Vfx | Endless | Weak, L-09 |
| ZOM-16 | Backlog | 3 | marcus.bennett | Liquid Impact | none | No, VFX backlog |
| ZOM-48 | Backlog | 0 | robert | Reward Animations | none | No, old backlog |
| ZOM-56 | Backlog | 3 | marcus.bennett | Glued VFX | none | No, VFX backlog |
| ZOM-64 | Backlog | 3 | marcus.bennett | Experiment with VFX when matching boss busters off the board | none | No, VFX backlog |
| ZOM-65 | Backlog | 0 | - | Profile page endpoints | none | No, old server backlog |
| ZOM-66 | Backlog | 0 | - | Stats endpoints | none | No, old server backlog |
| ZOM-69 | Backlog | 0 | - | Bot system | none | No, old server backlog |
| ZOM-70 | Backlog | 0 | - | Rewards system | none | No, old server backlog |
| ZOM-73 | Backlog | 3 | arthur.blake | A/B Test Item Sizes | none | No, A/B idea |
| ZOM-76 | Backlog | 3 | EMPLOYEE_0032 | [PERSON_NAME_0120] to implement this VFX | none | No, VFX backlog |
| ZOM-78 | Backlog | 3 | douglas | Event Calendar For Zombie Match 3D | calendar ticket | No, destination for the sheet link |
| ZOM-104 | Backlog | 4 | claire.morgan | Gas Can improvement | none | No, item art |
| ZOM-119 | Backlog | 2 | marcus.bennett | Shine for gold and gem piles. | none | No, shop VFX |
| ZOM-121 | Backlog | 2 | marcus.bennett | Card pack animation in the shop | none | No, shop VFX |
| ZOM-122 | Backlog | 4 | marcus.bennett | Simple animations for offers bands and labels. | none | No, shop VFX |
| ZOM-137 | Backlog | 0 | claire.morgan | FOOD ITEMS | none | No, item art |
| ZOM-147 | Backlog | 0 | claire.morgan | Peach | none | No, item art |
| ZOM-148 | Backlog | 0 | claire.morgan | Plum | none | No, item art |
| ZOM-150 | Backlog | 0 | claire.morgan | Cherries | none | No, item art |
| ZOM-151 | Backlog | 0 | claire.morgan | Cucumbers | none | No, item art |
| ZOM-155 | Backlog | 0 | claire.morgan | Squash | none | No, item art |
| ZOM-168 | Backlog | 3 | EMPLOYEE_0032 | 5th In-game Boost Double Damage | none | No, future boost |
| ZOM-236 | Backlog | 3 | EMPLOYEE_0032 | Shop Pack Idle animation | none | No, shop VFX |
| ZOM-237 | Backlog | 3 | - | packs animations bugs | none | No, pack VFX bugs |
| ZOM-243 | Backlog | 2 | marcus.bennett | Poison/Fire/Shock Death Vfx Animations | none | No, VFX backlog |
| ZOM-255 | Backlog | 3 | owen.baker | Tap to skip kill cam + Dimming the board area and only keeping | none | No, feature idea |
| ZOM-317 | Backlog | 2 | martin.walsh | Martin to polish UI assets in FIGMA | none | No, shop UI |
| ZOM-390 | Backlog | 3 | julia.lawson | Icon and Event Visual for Win Streak Event (axe arena) | Axe Arena (off) | No, off; assigned to Julia |
| ZOM-429 | Backlog | 3 | douglas | Leaderboard next session doesn't start without killing the app | Weekly Leaderboard | Held; fix is in Reading A, section 4 |
| ZOM-449 | Backlog | 2 | arthur.blake | Some items are acting weird in low-end android device | none directly | Weak, L-14 |
| ZOM-482 | Backlog | 2 | EMPLOYEE_0032 | Make "Fast-forwarding" another boolean properties in zombies | none | No, design tooling |
| ZOM-504 | Backlog | 0 | EMPLOYEE_0032 | In endless mode, objects might stay persistent in the deck aft | Endless | No, section 4 |
| ZOM-505 | Backlog | 0 | vincent.parker | Tutorial repeats at level 19 in V 1736 Android version | none | No, section 4 |
| ZOM-517 | Backlog | 2 | EMPLOYEE_0032 | Monster loses enrage during item refill in endless mode | Endless | No, section 4 |

## 9. Open non-ZOM tickets touching ZM3D

149 open tickets in ENG (96), ART (30), DES (14), EPI (9) were listed. The three that name ZM3D:

| ticket | state | what | verdict |
|---|---|---|---|
| ART-790 | Todo | "Updated ZM Marketing Screenshots" (Martin) | No beat. Store art, SC-16 |
| ART-792 | Team Epic | "ZM3D - Marketing Screenshots round 3" (Martin) | No beat. A/B mock-ups, SC-16 |
| ENG-2258 | Todo | "Infographic Tutorial Animations", Domino Delights twin of ZOM-484 | Weak, L-17 |

The other 25 beat-word hits (leaderboard, quest, season pass, daily gift, Win & Collect) are older Domino Delights tickets, none touched after Jun 3, 2025. ENG-2360 only says "similar to the ones we implemented in Zombie Match".
