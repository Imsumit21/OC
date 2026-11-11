# Re-audit of the injected Linear records (rev 5) against the SynthCut base

Scope: the 23 `linear.linear_comments` INSERTs and 21 `linear.linear_issues` UPDATEs in
`review_rev5/inputs/01_Universe_Inject.sql` (lines 179-249). SQL not executed. Clock 2025-10-01 07:00 UTC.

## 0. Result in one paragraph

Two comments are contradicted by base code, commits and Slack (both on ZOM-526). One comment (ZOM-429) is
arguably contradicted by base QA evidence from the same week. Two comments use the phrase "the beta buy"
days before any record defines it (ZOM-471, ZOM-542). One clause of ZOM-565 contradicts the ticket's own
description. Five further comments are uncontradicted but exposed (no base trace, weak author, or weak
authority). Twelve comments are fully clean, eight of them positively confirmed by base records. All 21
UPDATE statements are chronologically sound; no ticket's post-SQL status contradicts its own comment.

## 1. Two facts about the base that change how this slice must be checked

1. **The repo trees are real git repositories.** `github/root/harmonygames-Games/match3d/.git` holds 4,001
   commits on `main` plus branches; `match3d-backend` and `match3d-quests` also have `.git`. `git log -S`,
   `git show --stat` and per-path history work (prefab/PNG blobs are truncated or LFS pointers, text files are
   complete). Several commits that decide claims below exist only there, not in `github/data.json`.
2. **`match3d` main is at `0ff577550e` "Fix end popup", committed 2025-10-01T05:44:17Z**, not ~2025-09-30T15:41Z.
   It already contains PRs #470, #471, #472, #473, #474, #475.

Other base anchors used repeatedly:
- Leonard's beta pipeline post, `slack/messages/C05KNDCHAAG/2025-09.json` #21, 2025-09-12 19:11:30Z
  ("Beta target: Sep 30 ... Reward animations VFX polish (Brian, Marcus, Calvin) ... Queue manager service (Brian, Calvin)").
- Leonard's priorities post, `C090N54TG79/2025-09.json` #537, 2025-09-22 05:01:26Z ("Fix tech issues first ... Beta must be tech stable").
- Trello ZM ROADMAP list `6851a674975da1fe76e70d93` (named "BETA: Sep 30" in every action up to 2025-09-30T17:09Z):
  cards "Queue Manager", "Reward Animations (VFX)", "Win and Collect", "Minor Bugs to Fix" (the last links ZOM-546).
- Confluence `page_liveops_calendar`: weekly resets are Monday 00:00 UTC.
- Base Linear has 0 comments, so every comment is injected. Comment-surface attachments on ZOM-471, ZOM-542, ZOM-565
  are images from base comments whose text was not exported.

## 2. Verdict table

Verdicts: CONFIRMED / UNCONTRADICTED / CONTRADICTED / TIMING CONFLICT. "Exposed" marks an uncontradicted claim a strict reviewer can still attack.
Slack locators are `channel/2025-09.json #array-index (UTC time)`. Git shas are in `github/root/harmonygames-Games/<repo>/.git`.

| Ticket | Comment id | Claim | Verdict | Evidence locator |
|---|---|---|---|---|
| ZOM-429 | cmt_zom429_1 (Douglas, 09-23 18:12Z) | Force-close and reopen lands the player in the new week | **CONTRADICTED (arguable)** | C08R27X0EAH #902 (09-22 13:00:48Z) Vincent: "I cannot participate in leaderboard. Killing the app doesn't help." Prod builds were cut before the revert: C05433XK267 #694 iOS Submission #40 (12:38:18Z), #696 Android Submission #127 (12:39:43Z); revert pushed 13:44:55Z (C093LEZGF6J #430). D06477JGUKT #184 (09-23 16:04:38Z) Vincent to Arthur: "then it's live" |
| ZOM-429 | same | "not blocking. Leaving as-is" | UNCONTRADICTED | Ticket Backlog since 09-22T14:51:23Z; description: "wouldn't be the biggest issue ... once a week" |
| ZOM-556 | cmt_zom556_1 (Vincent, 09-24 15:20Z) | Lower day row carries on instead of resetting to day 1 | CONFIRMED | C08R27X0EAH #740-744 (09-17); D06UPGF5PQV #87 (09-22 16:13:18Z); no daily-reward commit in `match3d-backend` after 2025-07-25 |
| ZOM-556 | same | Claimed on the submission build after skipping a day; paid out | UNCONTRADICTED | D05QUH5URK2 #51 (09-22 16:38Z) says Vincent had not yet tested it himself; two days later is feasible |
| ZOM-565 | cmt_zom565_1 (Marcus, 09-29 14:34Z) | Pushed a small prefab change on Marcus/EndlessMode_Vfx; new bar still hidden | CONFIRMED | git `44988da015` (data.json `/commits/4056`), 14:33:08Z: "a little change to the prefab in the engldess screen prefab in main menu, it's still hidden in there for you to use"; D05U73FNDDL #130-131 (14:34:06Z, 14:34:25Z "i wrote a comment on the linear task"); Gmail `calvin@harmonygames.co_1844610214477156424.json` #0 (14:49:44Z) |
| ZOM-565 | same | "the claim glow [is] still hidden" | **CONTRADICTED (minor)** | Ticket description: "the glow behind its on all and the bar its the old bar ... mine it's in there but not active" |
| ZOM-565 | same | "nothing here has to land before the beta buy" | UNCONTRADICTED, exposed | No base statement either way. Marcus defers such calls: D05U73FNDDL #57-58 (09-19 17:15Z) "[Brian] it's the best person to respond ... he is Product Manager on this" |
| ZOM-543 | cmt_zom543_1 (Calvin, 09-30 16:20Z) | Flow is level_end, daily_gift, season_pass, tutorial plus Collect and Win | CONFIRMED | `Assets/Scripts/UI/MainMenu/QueueManager.cs` L52-58; PR #459 body; PR #472 merged 15:53:04Z (`/pull_requests/2377`) |
| ZOM-543 | same | "Queue manager is in progress" | UNCONTRADICTED | Base state In Progress. Tension only: Trello "Queue Manager" card set dueComplete 2025-09-30T16:40:22Z |
| ZOM-526 | cmt_zom526_1 (Brian, 09-24 17:30Z) | Collect and Win trigger is on its branch, waiting for the merge | CONFIRMED | D0770ET6WBW #252 (09-24 16:22:28Z); commits `5130ccb932`, `106587168f` on the winAndCollect branch; PR #468 merged 09-29T16:13:50Z |
| ZOM-526 | same | "vfx path is shipped for Quests, Endless and Daily Gift" | **CONTRADICTED** | `Assets/Scripts/UI/LiveOps/ERewardType.cs` L41-45: `enum ERewardLiveopsCategory { SeasonPass, WinAndCollect }`. No other live-ops token path exists |
| ZOM-526 | same | "finishing it alongside Season Pass" (Season Pass part not finished) | **CONTRADICTED** | git `c3976ae222` (data.json `/commits/863`), 2025-09-12T01:24:57Z "Adding season Pass token animation"; on main since PR #438 merge `8b8d069b57`, 2025-09-15T23:09:34Z; D0770ET6WBW #244 (09-23 20:20:41Z) Brian himself: "Does the season pass token animation start at about the same time as the level-end animation?" |
| ZOM-526 | cmt_zom526_2 (Brian, 09-26 15:40Z) | Unticked on the master ticket; it was marked done too early | CONFIRMED | Base master all `[X]` while ZOM-526 In Progress since 09-17T15:52:10Z; consistent with the ZOM-521 UPDATE |
| ZOM-526 | same | "What is left, the Collect and Win trigger and the Season Pass part" | **CONTRADICTED** (Season Pass half) | Same as above; also D05S1S2H55M #39 (09-18 20:52:27Z) Calvin: the season pass token instruction is already in RewardVFXManager |
| ZOM-526 | same | "does not have to land before the beta buy or the November season" | UNCONTRADICTED, exposed | Brian is product owner (C05KNDCHAAG #21). Tension: D0770ET6WBW #252 "we need to integrate it to queue manager too"; Queue Manager is on the Trello BETA list |
| ZOM-552 | cmt_zom552_1 (Oliver, 09-26 15:45Z) | Redeem events sent; left and premium in from the sheet; kept open | CONFIRMED | git `daeea991ce` (09-18T20:00:32Z), `ba194fd16b` (09-18T20:40:27Z), `663f4ccb84` (09-19T15:44:09Z); `SeasonPassController.cs` L390, `SeasonPassUI.cs` L204, `SeasonPassPopup.cs` L108/119; D07GK9QQG7M #126-149, #157, #167 |
| ZOM-534 | cmt_zom534_1 (Douglas, 09-25 16:35Z) | Rollover now syncs quests-end with the client instead of waiting on a restart | CONFIRMED | git `47c65623e7` (Oliver, 2025-09-10T23:53:56Z) "Using remaining-time endpoint to sync quests end with client"; on main since 09-15 |
| ZOM-534 | same | Watching one backend timing edge case | UNCONTRADICTED | Nothing bears on it |
| ZOM-432 | cmt_zom432_1 (Calvin, 09-24 16:10Z) | Artwork still needs the frame | CONFIRMED | `Assets/Sprites/Daily Gift/img - DailyGift.png` untouched from 2025-07-18 (`111562e3a2`) until `41a0d814ed` (2025-09-27T03:43:14Z, Samuel, "update header image") |
| ZOM-432 | same | Card back and gift box are done | UNCONTRADICTED | Daily Gift prefabs last changed by Calvin in July |
| ZOM-78 | cmt_zom78_1 (Frederick, 09-30 18:15Z) | Use this ticket for the beta calendar; link the sheet here | UNCONTRADICTED, lightly exposed | Frederick is not in team_ZOM (`/team_memberships`: ART, ENG) and has created 0 ZOM issues; comment precedes his own DM ask (20:20Z) |
| ZOM-465 | cmt_zom465_1 (Marcus, 09-26 18:10Z) | Idle icon animations done, in the animated-icons PRs; every event icon animated | CONFIRMED | PRs #454, #458, #456 (merged 09-24T14:30:39Z; body lists six icons); `_iconAnim` in QuestIcon, SeasonPassUI, ZombieLaneIcon, PlagueRaceMenuIcon, EndlessMenuIcon, InfiniteBossMenuIcon |
| ZOM-465 | cmt_zom465_2 (Marcus, 09-30 18:05Z) | Collect & Win came in after the note; its icon is not animated | CONFIRMED | PR #468 created 09-26T20:16:25Z, merged 09-29T16:13:50Z; no Collect & Win animated icon at HEAD |
| ZOM-465 | same | Collect & Win icon animation still to do on my side | UNCONTRADICTED | C09ATAJ220H #96: "P0 - Collect & Win -> may need your help later" |
| ZOM-344 | cmt_zom344_1 (Marcus, 09-16 16:20Z) | Quest box animation reuses the endless chest curve; art signed off | UNCONTRADICTED, exposed | No base trace of this work near 09-16. Quest prefabs last touched by Calvin (`e8cc6b3544`, 09-15). "the hub" is not a base term |
| ZOM-442 | cmt_zom442_1 (Oliver, 09-19 15:10Z) | trophy_reward_redeem fires with trophy_level and chest_content | CONFIRMED | `Assets/Scripts/LiveOps/Zombie Lane/Cells/ZombieLaneCellBase.cs` L174, L226-227; git `6027d248ec` (2025-07-30) |
| ZOM-471 | cmt_zom471_1 (Samuel, 09-17 16:45Z) | Leonard said we do not need it | CONFIRMED | C0880U9751A/2025-08.json #288 (08-13 18:32:48Z) "yeah, we don't need it! cancel the ticket"; #296 |
| ZOM-471 | same | Icon already shows the Start button outside a race | CONFIRMED | Same thread #287; `PlagueRaceMenuIcon.cs` `case NotJoined: _orangeStartButton.SetActive(true)` |
| ZOM-471 | same | "before the beta buy" | **TIMING CONFLICT** | See finding 3 |
| ZOM-504 | cmt_zom504_1 (Vincent, 09-22 15:30Z) | Only with the bot; not in manual play | CONFIRMED | D07GJJBFHA5 #13-16 (09-03 12:53-14:33Z) "yeah, I couldn't repro without bots" |
| ZOM-504 | same | Clears on next throw; visual only | UNCONTRADICTED | Description: "stay visually after thrown" |
| ZOM-517 | cmt_zom517_1 (Robert, 09-18 17:40Z) | Retested; enrage kept through refills | UNCONTRADICTED, lightly exposed | No fix commit, no retest record. "endless test board" is not a base term |
| ZOM-521 | cmt_zom521_1 (Calvin, 09-26 17:25Z) | Checklist down to two items | CONFIRMED (against the post-SQL description) | ZOM-526 and ZOM-528 both In Progress in base |
| ZOM-521 | same | Cards VFX is what I am on now | CONFIRMED | ZOM-541 started_at 2025-09-25T17:44:34Z; D05U73FNDDL #112 (09-24 17:00Z); C09ATAJ220H #160 (09-29 15:54:49Z) "almost done" |
| ZOM-542 | cmt_zom542_1 (Samuel, 09-22 18:40Z) | Still at the mockup stage; not in the build | CONFIRMED | C08R8CHB0QL #94 (09-15 16:24:21Z) "few comments with mockups in the ticket", #102, #110; 12 comment-surface images; no implementing commit |
| ZOM-542 | same | "before the beta buy" | **TIMING CONFLICT** | See finding 3 |
| ZOM-544 | cmt_zom544_1 (Vincent, 09-29 15:35Z) | Apple sign-in works; levels, currencies, cards not restored | CONFIRMED | CD843DBC4C3E #19-20 (09-24 17:46Z), #36 (09-25 14:52:11Z) |
| ZOM-544 | same | Google Play still waiting on the backend setup | CONFIRMED at that minute | D079SNE2TL4 #252 (15:11:16Z) asks; #253 (15:40:28Z) "almost done ... about 1 hour"; #256 (16:47:43Z) done |
| ZOM-546 | cmt_zom546_1 (Owen, 09-24 19:00Z) | Refill counts hold level across a long endless run | UNCONTRADICTED, exposed | Bug acknowledged in base: C0880U9751A #166 (repro), #183 (09-16) engineer "i know, trying to fix it"; Trello BETA bug list links ZOM-546. No fix or retest recorded. Owen's commits 09-22 to 09-25 are all Collect and Win |
| ZOM-549 | cmt_zom549_1 (Vincent, 09-26 16:50Z) | endless_left carries the three fields; left_level lacks total_equipped_power | CONFIRMED | `Assets/Scripts/Utils/AnalyticsManager.cs` L473-510 vs L418-447; git `f44fe52b7f` (#451, 09-17) |
| ZOM-566 | cmt_zom566_1 (Owen, 09-30 19:40Z) | Two events (start, redeem) mapped; wiring into the analytics manager | CONFIRMED | D07E9PSQB6W #3-9 (16:26-16:30Z); D05S1S2AB5M #35 (17:13:12Z); PR #477 opened 22:26:30Z; commit `31ee4178bd` 22:23:02Z |

### linear_issues UPDATE statements

| Ticket | Post-SQL change | Verdict |
|---|---|---|
| ZOM-432 | Todo to Done, completed/updated 09-30T21:20Z | Consistent. PR #471 merged 15:52:24Z; iOS Submission #50 (19:15:49Z) and Android #135 (20:13:09Z) built after it; PR note 21:07:26Z; close 21:20Z |
| ZOM-344 | Todo to Done, completed/updated 09-16T16:20Z | Not contradicted; nothing in base anchors that date |
| ZOM-566 | Todo to In Progress, started 17:20Z, updated 19:40Z | Consistent. Follows D05S1S2AB5M #37 (17:17:29Z); precedes the analytics commit |
| ZOM-521 | Description unticks two boxes; updated 09-26T17:25Z | Consistent with children ZOM-526 and ZOM-528. Text differs from base only in the two ticks. Note: PR #475 merged the card animation on 09-30T16:09:15Z, so the cards box is stale by the clock, as base ZOM-528 itself is |
| 17 others | updated_at only | All move forward from base and equal the latest comment |

## 3. Ranked findings and smallest fixes

### 1. HIGH: ZOM-526, both comments, are contradicted by code, commits and the author's own Slack
- Injected: "The vfx path is shipped for Quests, Endless and Daily Gift ... finishing it alongside Season Pass", then
  "What is left, the Collect and Win trigger and the Season Pass part".
- Base: token-to-live-ops travel exists for exactly two categories, Season Pass and Collect and Win. The Season Pass
  one has been on main since 2025-09-15T23:09:34Z and shipped in the following submission builds. Brian watched it
  on 09-23. Quests, Endless and Daily Gift have no such path; what they have is ZOM-527's claim-scene reward travel.
- Fix, comment 1: "Token-to-live-ops travel is in progress. Season Pass tokens already fly to the icon; the Collect
  and Win trigger is on its branch, waiting for the merge."
- Fix, comment 2: "Unticked this one on the master ticket, it was marked done too early. What is left is the
  Collect and Win trigger I mentioned above. It is polish on an effect that already ships for Season Pass, and the
  event runs without it, so it does not have to land before the beta." Drop "or the November season".

### 2. MEDIUM: ZOM-429, Douglas's "force-close and reopen works" sits against base QA from the same rollover
- The Monday 09-22 rollover is the one Douglas would have checked. That day Vincent reported "Killing the app
  doesn't help" on the build carrying Oliver's leaderboard commit. The store builds (Android 0.3.127, iOS 0.3.40)
  were cut about an hour before the revert, and Vincent told Arthur "then it's live" two hours before the comment.
- Mitigating: Vincent got in "after a moment" (#904) and the post-revert internal build worked (#910). The cause
  is a different bug from ZOM-429. Hence "arguable".
- Fix: re-date the comment to Tue 2025-09-16T18:12:00Z (after the Mon 09-15 rollover, before regression commit
  `70571e610c` of 09-19T21:02Z) and delete the ZOM-429 `updated_at` UPDATE, so base 2025-09-22T14:51:23Z stands.
  Douglas is on Slack 16:35-16:38Z that day and nothing in base bears on that rollover.

### 3. MEDIUM: "the beta buy" is used before anything defines it (ZOM-471 on 09-17, ZOM-542 on 09-22)
- "beta buy" has 0 hits in all Slack (610,468 messages) and in Gmail from June to October. The only sources are
  injected: the UA deck (created 2025-09-23T16:05Z, shared with Julia only), the brief (09-24) and the 09-30 DM.
- Fix: in both comments replace "before the beta buy" with "before the beta". The base term is established
  (C05KNDCHAAG #21, "Beta target: Sep 30").
- Lower-severity instance of the same thing: ZOM-565 (09-29) and ZOM-526 comment 2 (09-26) postdate the deck, but
  neither author is on its share list. The same substitution removes it.

### 4. LOW-MEDIUM: ZOM-565, one clause contradicts the description, and the scope call is not Marcus's
- Fix: "The new bar is still hidden in there for you to hook up, and the glow still shows on every box until it is
  tied to the Claim state."
- For the last sentence either drop it or ground it in Brian's list: "Brian has this as P1/P2 polish, so nothing
  here has to land before the beta" (C09ATAJ220H #96: "P1/P2 - VFX for endless and boss arena").
- Also: the real commit message and DM from the same minute are in Marcus's lowercase, typo-heavy style; the
  injected text is clean prose. The same applies to his ZOM-465 and ZOM-344 comments.

### 5. LOW-MEDIUM: who can make the "need not land before the beta" call
| Ticket | Author | Plausible? | Base statement that it is required, scheduled or decided otherwise |
|---|---|---|---|
| ZOM-471 | Samuel (assignee) | Yes, he relays Leonard | Decided otherwise and more strongly: Leonard said "cancel the ticket" and "I don't think we should do it". "Parking it" is compatible |
| ZOM-542 | Samuel (assignee) | Weak. Robert raised it as high priority with a Hot Fix label | None found. Leonard's 09-22 05:01Z post ("Fix tech issues first") supports it; citing that would ground the comment |
| ZOM-565 | Marcus (creator, VFX artist) | Weak, see finding 4 | None found. Not on the Trello BETA list |
| ZOM-526 | Brian (creator, product owner) | Yes | The parent scope is scheduled: "Queue manager service" in Leonard's beta pipeline and on the Trello BETA list; Brian on 09-24: "we need to integrate it to queue manager too". Nothing names ZOM-526 itself |

### 6. LOW: ZOM-344, the Done state and comment have no base anchor
- Marcus's 09-16 activity is the liquid VFX; Brian's task list for him re-shared that day (D077ALC9VK3 #152,
  16:40:22Z) has no quest box item.
- Later base chatter about quest chest timing (D070FDB7GM8 #94 on 09-23, CF4EDAF93359 #124 on 09-30) concerns the
  claim sequence, not this ticket, so it does not contradict.
- Optional hardening: replace "reads well on the hub" with "reads well on the quest screen".

### 7. LOW: ZOM-546, Owen reports no repro of a bug base treats as live
- Not contradicted, because PRs #453 and #457 changed the refill code on 09-22 and 09-23.
- Hardening: add "on main after the manual-refill merge" to the comment.

### 8. LOW: remaining notes
- ZOM-517: replace "endless test board" with a base term such as "endless_02 with the bot".
- ZOM-78: Frederick is outside team_ZOM and comments two hours before his own ask. No contradiction.
- ZOM-543: Leonard ticks the Trello Queue Manager card complete 20 minutes after "in progress". The base Linear
  state supports the comment.
- ZOM-544: the Google Play clause goes stale 73 minutes later (CD843DBC4C3E #39, 16:48:51Z). Correct when written.

## 4. Comments found fully clean

Confirmed by base records: cmt_zom552_1, cmt_zom534_1, cmt_zom442_1, cmt_zom504_1, cmt_zom544_1, cmt_zom549_1,
cmt_zom566_1, cmt_zom521_1, cmt_zom465_1, cmt_zom465_2, cmt_zom543_1.

Uncontradicted with nothing a reviewer can use: cmt_zom556_1, cmt_zom432_1.

Clean except the single phrase "the beta buy": cmt_zom471_1, cmt_zom542_1.

Not clean: cmt_zom526_1, cmt_zom526_2, cmt_zom429_1, cmt_zom565_1.
Exposed only: cmt_zom344_1, cmt_zom546_1, cmt_zom517_1, cmt_zom78_1.

## 5. Mutual consistency of the injected records

- ZOM-521 / 526 / 543 / 465: consistent with each other on the sequence (untick 09-26 15:40Z, "two items left"
  17:25Z, Collect and Win in the queue 09-30). The only defect is the Season Pass premise in finding 1.
- ZOM-432 and the PR #471 note: consistent, and the base commit "update header image" supports the note.
- ZOM-429 and Vincent's 09-30 Slack re-test: consistent as a dated supersession. Vincent's "still" matches his own
  base 09-22 report, which is what makes Douglas's 09-23 comment the odd one out.
- Arthur's #470 review note ("prod update from today carried the teams/social changes only") matches D079SNE2TL4
  #263 (09-30 18:16:33Z).

## 6. Author timing

No absence conflicts. Douglas was out the morning of 09-23 (C05KNDCHAAG #36) and back by 17:24Z, before his
18:12Z comment. Every author has Slack or commit activity within about an hour of each timestamp, except:
- Samuel on 09-22 (no Slack that day; a commit at 00:12Z on 09-23 shows him working),
- Marcus on 09-26 18:10Z (last Slack 17:05Z; he posts as late as 20:12Z on other days).

## 7. Searches run

All tickets:
- Full read of the base ticket (description, state, dates, parent/children, attachments).
- All-channel, all-DM Slack regex for the ticket id (which also matches the URL slug).
- Gmail (8,208 messages dated from 2025-06-01) for the id.
- Trello cards, descriptions and action history for the id.
- Confluence, Docs, Sheets, Slides, Drive and GCal exports for the id (0 hits for all 21).
- The author's Slack activity within 50 minutes of each timestamp, and an absence-message sweep for 09-12 to 10-01.

| Ticket | Additional searches |
|---|---|
| ZOM-429 | Slack "leaderboard / weekly / league / new week" 09-08 to 10-01; C08R27X0EAH 09-22; DMs Vincent-Douglas, Vincent-Arthur, Oliver-Vincent; submission builds 09-19 to 09-24; git log grep leaderboard in client and backend; Confluence calendar page |
| ZOM-556 | Slack "daily gift / login / reward / claim / reset" 09-15 to 10-01; DMs Calvin-Vincent, Calvin-Douglas, Vincent-Douglas; backend and client git log grep daily/login/gift; description image |
| ZOM-565 | DM Marcus-Calvin 09-19 to 10-01; #zm-animations 09-11 to 10-01; branch log; comment image; Gmail notification |
| ZOM-543 | DM Calvin-Brian 09-15 to 10-01; QueueManager.cs; PRs #459, #465, #472; Trello card actions |
| ZOM-526 | Slack "token" 09-01 to 10-01; RewardVFXManager.cs, ERewardType.cs; `git log -S` for both category names; file content at three merge commits; DMs Oliver-Calvin, Calvin-Owen; beta pipeline post; Trello BETA list |
| ZOM-552 | Code grep for the three event names; `git log -S` each; DM Oliver-Brian 09-17 to 09-30 |
| ZOM-534 | Origin thread; Slack "quest" with reset/restart/rollover; git log on the Quests path and the commit diff; backend and quests repo logs |
| ZOM-432 | Slack "frame / card back / gift box"; #zombie-ops 07-23 thread; DM Samuel-Vincent; PR #471 commits, comments, timeline; per-path git history of the Daily Gift assets; builds #50 and #135 |
| ZOM-78 | Slack "event calendar / live-ops calendar / calendar ticket"; Linear team memberships and issue counts per author |
| ZOM-465 | PRs #454, #456, #458, #468; animated-icon prefabs and `_iconAnim` users at HEAD; Slack regex for Collect and Win icon animation |
| ZOM-344 | Slack regex quest + box/chest + animation from 06-25; Marcus's September messages on quest/chest/box; git history of the Quests prefabs and Marcus's commits; description image |
| ZOM-442 | Code grep "trophy"; `git log -S`; Slack "trophy_reward" |
| ZOM-471 | Origin thread in full; Slack "red dot"; PlagueRaceMenuIcon.cs; comment image |
| ZOM-504 | DM Vincent-engineer 08-25, 09-03, 09-22; Slack "orphan / persistent"; git log grep |
| ZOM-517 | Slack "enrage" from 08-20; git log grep enrage; Robert's activity 09-18 |
| ZOM-521 | Children ZOM-523 to 528 and ZOM-541; DM Calvin-Brian; PR #475; #zm-animations 09-29 |
| ZOM-542 | #zombie-art thread and channel from 09-14; Slack "win screen / victory / best score / home screen"; git log on the Endless and InfiniteBoss paths; state analysis of "Regression" (a base triage-like state, 4 issues) |
| ZOM-544 | Sign-in mpdm CD843DBC4C3E 09-24 to 09-30; DMs Vincent-Douglas, Vincent-engineer; auth builds |
| ZOM-546 | Slack "refill" 09-10 to 10-01; origin thread; Trello card history; git history of EndlessObjectsSpawnManager.cs; Owen's commits and Slack 09-23 to 09-25 |
| ZOM-549 | AnalyticsManager.cs; `git log -S` for the three field names; PR #451; Slack field-name regex |
| ZOM-566 | DMs Brian-Owen, Owen-Arthur, Owen-Douglas on 09-30; #zm-collect-win; PR #477 body, commits, reviews |
| "beta buy" | Slack all channels from 08-01 for "beta buy" and beta with ua/buy/spend/campaign/scale; Gmail same: 0 hits |

## 8. Limits

- Unity prefab blobs are truncated at 10,240 bytes and PNGs are LFS pointers, so "the frame is in the header image"
  (ZOM-432) and "the bar is hidden" (ZOM-565) rest on commit messages, not asset content. The ZOM-565 comment
  screenshot appears to show the new bar active in the hierarchy; I did not rely on that reading.
- Analytics sheet URLs are redacted, so "matches the sheet" claims (ZOM-442, ZOM-552, ZOM-566) were checked against
  code and Slack only.
- The ZOM-429 verdict is a judgment call; the evidence on both sides is quoted so it can be re-weighed.
