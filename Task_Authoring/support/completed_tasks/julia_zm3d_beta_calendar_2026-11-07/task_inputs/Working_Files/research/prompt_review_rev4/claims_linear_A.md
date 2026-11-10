# Injected Linear comments, slice A: contradiction audit against the SynthCut base

Clock 2025-10-01 07:00 UTC. Nothing was executed; the SQL was read as an overlay only.
Slice: ZOM-429, ZOM-556, ZOM-543, ZOM-526 (2), ZOM-552, ZOM-534, ZOM-432, ZOM-78, ZOM-465 (2), ZOM-344.

## Outcome

Of the 12 comments, 5 carry a claim or a timestamp that base data contradicts, 1 has a structural mismatch, and 6 are clean (2 of those with wording that has no base referent).

| Rank | Comment | Problem | Severity |
|---|---|---|---|
| 1 | cmt_zom556_1 (ZOM-556) | Second sentence contradicts the ticket and three base Slack statements | High |
| 2 | cmt_zom429_1 (ZOM-429) | Timestamp falls inside a window where Douglas says he was out | Medium-high |
| 3 | cmt_zom552_1 (ZOM-552) | "Tagging the remaining events now" on Sep 26, but base shows all three done Sep 19; "release notes" has no referent | Medium |
| 4 | cmt_zom526_1 (ZOM-526) | "the Collect and Win trigger is in" on Sep 24, 68 min after Brian's own base DM says it is not merged | Medium |
| 5 | cmt_zom465_1 (ZOM-465) | "every event icon animates at idle now" contradicts Marcus's own base statements | Medium |
| 6 | cmt_zom78_1 (ZOM-78) | Author is not a member of the ZOM Linear team in base | Low |

Clean: cmt_zom543_1, cmt_zom526_2, cmt_zom534_1, cmt_zom432_1, cmt_zom465_2, cmt_zom344_1.

Two out-of-slice findings are at the end; the ZOM-565 one is high severity.

## Path legend

- SLACK = `/Users/sumit/Source/OC/Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/slack/messages` (locator: `<channel>/<YYYY-MM>.json[index]`, times UTC)
- LINEAR = `/Users/sumit/Source/OC/Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json`
- GH = `/Users/sumit/Source/OC/Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json`
- REPO = `/Users/sumit/Source/OC/Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/root/harmonygames-Games/match3d`
- TRELLO = `.../Services_Data/trello/data.json`
- CONF = `.../Services_Data/confluence/confluence_working.json`
- GMAIL = `/Users/sumit/Source/OC/Universe_SynthCut/SynthCut_HarmonyGames_Gmail/Services_Data/gmail/threads`
- SNOW = `.../Services_Data/snowflake/snowflake.json`
- SHEETS = `.../Services_Data/gsheets/data.json`

Channel ids used: C08R27X0EAH #zombie-bugs, C09ATAJ220H #zm-animations, C093LEZGF6J #zombie-prs, C05433XK267 #builds, C05KNDCHAAG #company-internal, C09EVVCFHKR #zm-collect-win, C07C2866011 #executives, C08R6BF4ENN #zombie-ops, D0770ET6WBW Brian-Calvin, D079SNE2TL4 Vincent-Douglas, D05QUH5URK2 Calvin-Douglas, D06UPGF5PQV Calvin-Vincent, D07GCPNJPSA Oliver-Calvin, D07GK9QQG7M Oliver-Brian, D07GY332589 Oliver-Douglas, D076V3NB6P7 Marcus-Brian, D05U73FNDDL Marcus-Calvin, D06477JGUKT Vincent-Arthur, D06UFE81RF0 Samuel-Vincent, D05SG9H1CFM Owen-Douglas.

## Ranked contradictions and fixes

### 1. cmt_zom556_1, ZOM-556 (Vincent Parker, 2025-09-24T15:20Z): second sentence contradicted

Injected: "The counter display on the main menu is cosmetic, the streak itself is fine."

Base says the opposite on three counts:

- **Where the defect is.** The ticket (LINEAR, ZOM-556, written by Vincent himself): "If I didn't log in for a day, the bottom part should reset to day 1. However, it doesn't reset right now." Its screenshot (`linear/root/attachments/images/ZOM-556/ZOM-556__3d58bb8b-bda6-4a.png`) is the Day 1..Day 7 grid inside the Daily Gift popup, not a counter on the main menu.
- **Whether the streak is fine.** SLACK C08R27X0EAH/2025-09.json[740-744], 2025-09-17 17:28-18:03: Leonard "daily login doesn' rest if you miss a day"; Vincent "which part lower or top progression?"; Leonard "lower"; Vincent "yes it's a bug then"; Brian "Yes it's a bug. The progress bar doesn't reset, but the daily rewards should reset". The non-resetting streak is the bug.
- **Whether it is display-only.** SLACK D06UPGF5PQV/2025-09.json[87], 2025-09-22 16:13:18, Calvin: "I think this is backend change. When the daily gift is skipped, it doesn't reset to 0. I just consume what backend sends me". Repeated at D07GCPNJPSA/2025-09.json[333], 18:19:51. Leonard calls it "beneficial to players", so it is not cosmetic.

The first sentence is fine: "paid out and moved to the next day" is exactly the unfixed behaviour, and Vincent's "I couldn't test it, it's Leonard's feedback" (D06UPGF5PQV[95], Sep 22 16:38:04) leaves room for a skip-a-day test by Sep 24. Submission builds existed (C05433XK267[694],[696], Sep 22).

Smallest fix: keep sentence 1, replace sentence 2 with
`So the lower day row still carries on instead of going back to day 1, but claiming works and nothing is lost.`

### 2. cmt_zom429_1, ZOM-429 (Douglas, 2025-09-23T16:12:00Z): timing conflict

- SLACK C05KNDCHAAG/2025-09.json[36], 2025-09-23 02:37:26, Douglas: "I will be out for a few hours tomorrow morning, There's a conference at my Alma Mater that I need to attend. I won't be able to attend the sync meeting".
- SLACK D079SNE2TL4/2025-09.json[213], 2025-09-23 17:25:30, Douglas, answering Vincent's 14:19:43 message: "Sorry, I was out for a few hours."
- Douglas has no Slack message between 02:xx and 17:24:09 UTC that day (first one back: D05SG9H1CFM/2025-09.json[167]). His hourly counts for Sep 23 are {00:5, 01:2, 02:1, 17:17, 18:3, 20:2}.

The comment at 16:12 sits inside the absence, and at the hour of the daily sync he said he would miss.

Smallest fix: move the comment's `created_at`/`updated_at` and the issue `updated_at` to `2025-09-23T18:12:00Z` (any time from 17:30Z works).

Content is otherwise consistent with the ticket ("It can only proceed to next leaderboard if the app is killed"; base state Backlog since 2025-09-22T14:51:23Z).

Adjacent risk, not a direct contradiction: the latest base QA statement before the comment says the opposite about killing the app.
- C08R27X0EAH/2025-09.json[902], Sep 22 13:00:48, Vincent: "I cannot participate in leaderboard. Killing the app doesn't help."
- That was a regression from commit 11497b93, reverted in main at 13:44:55 (C093LEZGF6J[430]). Android Submission #127 was built at 12:39:43, before the revert (C05433XK267[696]).
- CONF page_season_pass_spec: "Android 0.3.127 published Sep 22".
- D06477JGUKT/2025-09.json[180-184], Sep 23 16:01-16:04: "did we releasE?" / "yeah yesterday on android" / Vincent "then it's live". That is 8 minutes before the injected comment.

Optional hardening: "Checked the weekly rollover on dev - ...".

### 3. cmt_zom552_1, ZOM-552 (Oliver Brooks, 2025-09-26T15:45Z): timing conflict plus dangling reference

Injected: "Season pass redeem events are being sent, the release notes confirm them. Tagging the remaining events from the sheet now."

"Redeem events are being sent" is confirmed: C093LEZGF6J/2025-09.json[409], 2025-09-18 20:00:41, commit bf0c3183 "Sending SeasonPass_Redeem info to analytics" pushed to main by Oliver; also in the #builds change lists (C05433XK267[610],[611],[682]).

"Tagging the remaining events now" on Sep 26 is contradicted. The remaining events were finished on Sep 19:
- D07GK9QQG7M/2025-09.json[126-153], Sep 18-19: Oliver proposes a separate premium event and a bonus-bank bool on the left event; Brian "Sure, Let's do it!"; [154] 2025-09-19 12:01:05 Oliver "done!"; [171-173] 15:48 "Did we add bonus bank info There?" / "on sp_left?" / "yes"; Oliver "the sheets looks fine".
- C05433XK267[642],[643], Sep 19 15:49: "Changing name of SPs event to analytics".
- REPO has all three: `Assets/Scripts/LiveOps/SeasonPass/SeasonPassController.cs:390` "SeasonPass_redeem"; `SeasonPassPopup.cs:108,119` "SeasonPass_premium"; `SeasonPassUI.cs:204` "SeasonPass_left". These match the three sheet tabs (SHEETS, "Zombie Match Data Dictionary Firebase", f_12b4105f4b64c3ad374a9f).
- On Sep 26 itself Oliver was on tutorial, crash and performance fixes (D07GK9QQG7M[255] Sep 23 "I working on performance improvements atm"; D07H86MU8JC[39-40] Sep 26 15:28).

"the release notes confirm them" has no base referent. No release notes for this period exist in Slack (Aug-Sep), Confluence (only "release notes drafted for both stores" in the checklist), Docs/Drive (only 2023-24 docs) or the ZM-Liveops-Docs repo. The nearest real thing is the #builds change list.

Side note: SNOW shows the first ZM3D Season Pass rows on 2025-09-29 (LIVE_EVENT_PERFORMANCE EVT-0527; RESOURCE_FLOW_EVENTS "Season Pass|1000"), after the comment date.

Fix, either:
- **A, keep Sep 26:** `Season pass redeem events are being sent, the submission build change list shows them. Left and premium are in from the sheet as well; keeping this open until the data is checked against the sheet.`
- **B, keep the text, re-date:** set the comment and the issue `updated_at` to `2025-09-18T20:40:00Z` (after the 20:00:41 push, before "done!" on Sep 19; Oliver is active at 20:35) and change "the release notes confirm them" to "the build change log lists the commit".

### 4. cmt_zom526_1, ZOM-526 (Brian Foster, 2025-09-24T17:30Z): "the Collect and Win trigger is in"

- D0770ET6WBW/2025-09.json[252], 2025-09-24 16:22:28, Brian himself, 68 minutes earlier: "Because collect&win event is almost ready to merge, we need to integrate it to queue manager too".
- [253] 16:45:11 Calvin: "Yeah I'll need to add it to the queue manager once is merged". [259] Sep 25 14:02:20: "still waiting to implement on [Owen]'s branch".
- GH: PR match3d#468 "Collect And Win" created 2025-09-26T20:16:25Z, merged 2025-09-29T16:13:50Z. PR #472 "Implement Win&Collect into Queue Manager" merged 2025-09-30T15:53:04Z.
- The only "trigger" that existed on Sep 24 is on Owen's unmerged branch: commit 10658716, 2025-09-23T17:18:35Z, "Updated GetCollectAndWinStatus to trigger token animation before sending request".

It also clashes inside the injection with cmt_zom465_2 ("Collect & Win came in after my note above", note dated Sep 26).

Smallest fix: replace "the Collect and Win trigger is in" with `the Collect and Win trigger is on its branch, waiting for the merge`.

Secondary, low: "The vfx path is shipped for Quests, Endless and Daily Gift" is mis-scoped for this ticket. Brian's own definition of token travel is Collect&Win, Season Pass and Axe Arena tokens (D0770ET6WBW[212], Sep 18 17:10:03). Quests, Endless and Daily Gift are the claim-reward flows of ZOM-527. The wording does trace to PR #408's summary ("token path animations ... across Quests, Endless, Daily Gift"), so it is uncontradicted rather than wrong. Safer: "The token path animation is shipped (PR 408) and Season Pass tokens already travel".

### 5. cmt_zom465_1, ZOM-465 (Marcus Bennett, 2025-09-26T18:10Z): "so every event icon animates at idle now"

Marcus's own base words:
- C09ATAJ220H/2025-09.json[137], 2025-09-22 15:42:46: "its going to be animated only when the red dot appears and when it's calling for action. I still have the axe icon but i will wait for the engeneers to make the button on the main menu scene".
- D05U73FNDDL/2025-09.json[101-102], Sep 22 16:31: "has the animated bool paramenter in the animator that u can call when red dot its on" / "otherwise it will just stay static".
- D05U73FNDDL[44], Sep 19 17:08:16: "There is another icon. the axe one but that button doesnt exist yet".
- Calvin, D06UPGF5PQV[96], Sep 24 00:04: "they should be triggered once you are ready to claim or There's any red dot on the icon".

So the icons do not animate at idle (they are static unless there is a red dot or a claim), and not every event icon is done (axe is waiting on its button).

The first half is confirmed: PRs #454 "Marcus/animated icons" (merged Sep 19 17:50:52), #458 "Infinite Boss Icon Animated" (Sep 22 17:10:19), #456 "[Calvin]/animated icons" (Sep 24 14:30:39). The ticket had "~~Idle Icon Animation~~" struck by Sep 23 (unfurl at D076V3NB6P7[67]).

Smallest fix: `...are done and in the animated-icons PRs, so every event icon on the main menu has its animation now.`

### 6. cmt_zom78_1, ZOM-78 (Frederick Stone, 2025-09-30T18:15Z): author not on the ZOM team

LINEAR team_memberships has Frederick (usr_175c0d7bc72ed244) in team_ART and team_ENG only. In base, every ZOM issue's creator and assignee is a team_ZOM member (0 exceptions across the team's issues).

Linear does allow workspace members to comment on a public team's issues, so this is a plausibility flag, not a hard contradiction.

Fix: add a team_ZOM membership row for him if the schema carries that table, or accept.

Content and timing are fine. CONF page_liveops_calendar: "Owner: Frederick Stone (Growth/UA)... Design, led by Julia Lawson, walks the coming weeks with Frederick Stone". Frederick is active at 18:09:54 (C07C2866011/2025-09.json[1180]). ZOM-78 was created by Julia and assigned to Douglas (GMAIL `douglas@harmonygames.co_1830655156097598499.json`, Apr 28). No base Slack mention of ZOM-78.

### Lower-grade notes on clean comments

- **cmt_zom543_1:** TRELLO action 68dc07f69bc8f26035805883, 2025-09-30T16:40:22Z, Leonard marks the roadmap card "Queue Manager" complete, 20 minutes after the comment says "in progress". Base Linear itself still has ZOM-543 In Progress, so the comment matches Linear. No change needed.
- **cmt_zom344_1:** "on the hub" is not base vocabulary (base says main menu, home screen, quest page). No contradiction. SLACK CF4EDAF93359/2025-09.json[124] (Sep 30 13:29:35, Vincent: "the timing is off. Especially in the quest chests") is about reward-VFX sequencing assigned to Calvin, a different scope.
- **cmt_zom432_1:** "Card back" has no base referent in the Daily Gift context. "Gift box" maps to `Assets/Prefabs/UI/Daily Gift/Daily Gift Box.prefab`.
- **Voice:** Marcus's, Calvin's and Douglas's injected comments are in clean formal English, while their base writing is very informal (see the ZOM-565 description). Realism only.

## Claim-by-claim table

| Ticket | Comment | Claim | Verdict | Evidence locator |
|---|---|---|---|---|
| ZOM-429 | cmt_zom429_1 | Force-close and reopen lands in the new week | Uncontradicted (matches ticket); adjacent risk | LINEAR ZOM-429 desc; C08R27X0EAH[902],[910]; D06477JGUKT[184] |
| ZOM-429 | cmt_zom429_1 | "not blocking. Leaving as-is" | Confirmed | LINEAR ZOM-429: Backlog since 2025-09-22T14:51:23Z; desc "wouldn't be the biggest issue" |
| ZOM-429 | cmt_zom429_1 | Written by Douglas at Sep 23 16:12Z | **Timing conflict** | C05KNDCHAAG[36]; D079SNE2TL4[213]; no activity 02:xx-17:24 |
| ZOM-556 | cmt_zom556_1 | Claimed after skipping a day; paid out, moved to next day | Uncontradicted, consistent with the unfixed bug | D06UPGF5PQV[95]; D07GCPNJPSA[333]; C05433XK267[694],[696] |
| ZOM-556 | cmt_zom556_1 | Counter on main menu is cosmetic; streak is fine | **Contradicted** | LINEAR ZOM-556 desc and image; C08R27X0EAH[740-744]; D06UPGF5PQV[87]; D05QUH5URK2[45] |
| ZOM-543 | cmt_zom543_1 | Queue manager in progress | Confirmed against Linear; Trello card completed 16:40:22 | LINEAR ZOM-543 In Progress; TRELLO 68dc07f69bc8f26035805883 |
| ZOM-543 | cmt_zom543_1 | Flow is level_end, daily_gift, season_pass, tutorial | Confirmed | GH PR #459 body; REPO `Assets/Scripts/UI/MainMenu/QueueManager.cs` Start() |
| ZOM-543 | cmt_zom543_1 | "plus Collect and Win" by Sep 30 16:20 | Confirmed, 27 min after merge | GH PR #472 merged 2025-09-30T15:53:04Z; C09ATAJ220H[174] |
| ZOM-526 | cmt_zom526_1 | Token travel in progress | Confirmed | LINEAR ZOM-526 In Progress since 2025-09-17T15:52:10Z |
| ZOM-526 | cmt_zom526_1 | Path shipped for Quests, Endless, Daily Gift | Uncontradicted, mis-scoped | GH PR #408 summary; D0770ET6WBW[212] |
| ZOM-526 | cmt_zom526_1 | "the Collect and Win trigger is in" | **Timing conflict** | D0770ET6WBW[252],[253],[259]; GH PR #468, #472; commit 10658716 |
| ZOM-526 | cmt_zom526_1 | "finishing it alongside Season Pass" | Uncontradicted | LINEAR ZOM-526 desc; GH commit 12c23043 (Sep 12) in PR #438; D0770ET6WBW[244] |
| ZOM-526 | cmt_zom526_2 | Unticked on the master ticket; marked done too early | Consistent with post-SQL ZOM-521 | D0770ET6WBW[198] unfurl Sep 17 15:51:55 (ticked); ZOM-526 moved In Progress 15:52:10 |
| ZOM-526 | cmt_zom526_2 | Season Pass part is polish; pass runs without it | Confirmed | PR #438 merged 2025-09-15T23:09:34Z; D0770ET6WBW[244]; CONF page_season_pass_spec |
| ZOM-526 | cmt_zom526_2 | Not needed before the November season | Uncontradicted | CONF "seasons reset monthly on the 1st at 00:00 UTC"; D07GY332589[311] |
| ZOM-552 | cmt_zom552_1 | Redeem events are being sent | Confirmed | C093LEZGF6J[409]; REPO SeasonPassController.cs:390 |
| ZOM-552 | cmt_zom552_1 | "the release notes confirm them" | No base referent | Searches listed below |
| ZOM-552 | cmt_zom552_1 | "Tagging the remaining events now" (Sep 26) | **Timing conflict** | D07GK9QQG7M[154],[171-173]; C05433XK267[642]; REPO SeasonPassPopup.cs:108,119, SeasonPassUI.cs:204 |
| ZOM-534 | cmt_zom534_1 | Rollover syncs quests-end with the client, no restart | Confirmed (fix is Oliver's client commit of Sep 10) | C093LEZGF6J[208] commit 738b3928; C08R27X0EAH[587]; C07C2866011[389]; D07GY332589[163-170] |
| ZOM-534 | cmt_zom534_1 | Watching a backend timing edge case | Uncontradicted | D07GY332589[223-235] (Sep 12 TimeSpan "0:10:60" fix); ticket In Progress since Sep 15 |
| ZOM-432 | cmt_zom432_1 | Artwork still needs the frame on Sep 24 | Confirmed | C08R6BF4ENN/2025-07.json[290]; LINEAR ZOM-432 Todo; GH commit f0bb8b48 (Sep 27) |
| ZOM-432 | cmt_zom432_1 | Card back and gift box are done | Uncontradicted; "card back" has no referent | REPO `Assets/Prefabs/UI/Daily Gift/` |
| ZOM-432 | issue update | Done at 2025-09-30T21:20Z, started_at null | Consistent | PR #471 merged 15:52:24Z; C05433XK267[1123] iOS #50 19:15:49, [1124] Android #135 20:13:09; 37 of 68 ZOM issues completed in Sept have no started_at |
| ZOM-78 | cmt_zom78_1 | Use this ticket for the beta live-ops calendar; link the sheet | Uncontradicted | CONF page_liveops_calendar; no Slack mention of ZOM-78 |
| ZOM-78 | cmt_zom78_1 | Author Frederick on a ZOM issue | **Structural flag** | LINEAR team_memberships |
| ZOM-465 | cmt_zom465_1 | Idle icon animations done, in the animated-icons PRs | Confirmed | GH PRs #454, #456, #458; D076V3NB6P7[67] |
| ZOM-465 | cmt_zom465_1 | "every event icon animates at idle now" | **Contradicted** | C09ATAJ220H[137]; D05U73FNDDL[44],[101-102]; D06UPGF5PQV[96] |
| ZOM-465 | cmt_zom465_2 | Collect & Win came in after the Sep 26 18:10 note | Confirmed | GH PR #468 created 2025-09-26T20:16:25Z, merged 2025-09-29T16:13:50Z |
| ZOM-465 | cmt_zom465_2 | C&W icon not animated yet | Confirmed | REPO `Assets/Animations/mainMenu/icons/` has six folders, none for C&W; no C&W .anim or .controller anywhere |
| ZOM-465 | cmt_zom465_2 | C&W icon animation still to do on Marcus's side | Uncontradicted (base ask is "polish the bottle vfx") | D076V3NB6P7[53],[70] |
| ZOM-465 | cmt_zom465_2 | "the other event icons are finished" | Uncontradicted for main-menu icons (axe has no button yet) | D05U73FNDDL[44] |
| ZOM-344 | cmt_zom344_1 | Quest box animation reuses the endless chest curve | Uncontradicted | LINEAR ZOM-344 desc; CD5C9E6CC238/2025-07.json[38]; GH PR #273 (Jul 4) |
| ZOM-344 | cmt_zom344_1 | Art side signed off Sep 16 | Uncontradicted | No Sept base record on it; Marcus active 16:03:55 and 17:12:10 that day |
| ZOM-344 | issue update | Done, completed 2025-09-16T16:20Z | Consistent | Same Done-without-started pattern |

Lifecycle check for all ten issues: every post-SQL `updated_at` is at or after the base value and before the clock; states left unchanged match the comment content; comment `sequence` values are consistent because none of these ten tickets has a comment-surface attachment or a base "commented on" record.

## Searches run, for coverage

Common to all tickets:
- LINEAR: full record, children, attachments, team memberships.
- SLACK: every channel and DM, 2025-07 to 2025-10, for the ticket id and URL slug (bot unfurls included).
- GMAIL: grep of all threads for the ticket ids (hits are Linear assignment notifications only).
- TRELLO: every ZM ROADMAP card and all actions since Sep 12.
- CONF: all 30 pages keyword-scanned; page_liveops_calendar and page_season_pass_spec read in full.
- Per-author Slack activity around each comment time, plus an out-of-office phrase search for all seven authors.
- A search for "commented on / updated the ticket / unticked" statements.

Per ticket:
- **ZOM-429:** Slack "leaderboard" with week, kill, restart, next, new, rollover (Jul 15 to Sep 30, all channels); #zombie-bugs Sep 21-23 read in sequence; Vincent-Douglas DM read for all of September; Vincent-Arthur DM Sep 16-30; #builds submission list; SNOW LIVE_EVENT_PERFORMANCE (no ZM3D leaderboard rows).
- **ZOM-556:** Slack "daily gift / daily login / daily claim / login calendar" (Jul to Sep); the #zombie-bugs thread of Sep 17; Calvin-Douglas, Calvin-Vincent and Oliver-Calvin DMs; ticket image viewed; GH commits for daily login and ConsecutiveLogins; #builds for submission builds.
- **ZOM-543:** Brian-Calvin DM Sep 12-30 read in full; GH PRs #459, #465, #472 (bodies, commits, reviews); REPO QueueManager.cs; Trello card actions; #zm-animations.
- **ZOM-526:** the above plus Slack "token" with travel, anim, icon, vfx, path; #zm-collect-win and the C&W issues canvas; GH PRs #408, #438, #440, #447, #468, #470; ZOM-521 and children ZOM-523 to 528.
- **ZOM-552:** Oliver-Brian DM Sep 17-30 read in full; Brian-Leonard DM Sep 17; Slack "season pass redeem / left / SPs event"; "release notes / patch notes / changelog" across Slack (Aug-Sep), Confluence, Docs, Drive and ZM-Liveops-Docs; GH PR, comment and commit text for "redeem" and "analytic"; REPO grep for event names; SHEETS data dictionary tabs; SNOW grep for SeasonPass tokens.
- **ZOM-534:** Slack "quest" with reset, restart, kill, rollover, sync (September, humans) and all "quest" messages Sep 11-30; Oliver-Douglas DM read for all of September; bot channels for quest commits; REPO QuestAPI / QuestTimerAPI and `liveops/quests`; non-match3d repo commits in September (no ZM backend commits exported).
- **ZOM-432:** Slack "frame" with daily, gift, artwork; "card back / gift box" (Jul to Sep); "daily gift" Jul-Aug; Samuel-Vincent DM Sep 20-30; GH PR #471 and all commits mentioning daily gift or frame since June; ticket image viewed; REPO Daily Gift sprites and prefabs (images are LFS pointers, not viewable).
- **ZOM-78:** Slack "event calendar / ZOM-78 / live-ops calendar" (Apr to Sep) and "calendar" (September); Linear "calendar" issues; Frederick's Linear footprint and memberships.
- **ZOM-465:** #zm-animations Sep 12-30 read in full; Marcus-Brian and Marcus-Calvin DMs read; GH PRs #454, #456, #458, #475; all Marcus commits and branches since June; REPO animated-icon folders and C&W assets.
- **ZOM-344:** Slack "quest" with box or chest and anim, vfx, open (Jul to Sep); "ZOM-344 / quest ui box / box animation" (Jun to Sep); Marcus's PRs and commits since June; ticket image viewed; "hub" usage (Jun to Sep).

Not covered: gcal, contacts and gslides were not searched; SNOW was grep-scanned only (2.2 GB), not loaded.

## Out-of-slice findings

**ZOM-565, cmt_zom565_1 (high).** Injected: Marcus, 2025-09-29T16:05Z, sequence 1, "The endless start screen vfx is in (commit f7e971b0). Claim button glow and the new bar are both live now, can close.", then Done at 17:10. Base contradicts it:
- Marcus already commented on that ticket about 90 minutes earlier. SLACK D05U73FNDDL/2025-09.json[131], Sep 29 14:34:25: "i wrote a comment on the linear task". GMAIL `calvin@harmonygames.co_1844610214477156424.json`, Sep 29 14:49:44: "Marcus Bennett mentioned you in a comment on [ZOM-565]". LINEAR has a comment-surface attachment for ZOM-565. So sequence 1 is wrong and the base comment said something else (he pushed prefab changes to his branch).
- The work was not implemented. D05U73FNDDL[120], Sep 26, Calvin: "no I haven't started yet on that"; [133], Sep 29 15:53:47: "Should I make another branch for those changes? and merge it".
- Commit f7e971b0 is on the unmerged branch `marcus.bennett/EndlessMode_Vfx`: no PR, and it appears in no #builds change list.

**ZOM-521 description UPDATE.** It also unticks "Claimed Cards traveling to inventory Section", which is `[X]` in the base export. That matches the Sep 17 Slack unfurl (unticked) and child ZOM-528 (In Progress), but no injected comment explains it, and PR #475 (the card animation) merged 2025-09-30T16:09:15Z.
