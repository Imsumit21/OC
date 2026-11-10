# Slack flags in the brief window: revision 9, task_inputsS

Window: 2025-09-24 17:40:52Z (brief `modified_time`) to the clock, 2025-10-01 07:00Z. SQL sha 892f7edd checked.
Rule tested: "For each beat, what still has to land before it runs for bought users and who owns it: a held beat's fix, and what has been flagged for that beat as not done since this brief (prod deploy, config or player-facing art). Nothing else goes in: not what already shipped, not analytics, not polish nobody flagged."

## Verdict

The Slack side of the set is not proved closed. One flag in the window matches truth.json. One flag qualifies on its text and is not in truth.json. Two more are not cleanly closed.

1. **EXTRA, SCOPE_GAP: Marcus, Sep 25, Endless core-game VFX.** It meets every test of the rule. The only closing record is about the start screen, a neighbouring scope.
2. **OPEN, SILENCE: Martin's desert and Port themes for Endless.** Nothing says whether they have to land. Julia replied in the desert thread herself.
3. **BORDERLINE, SCOPE_GAP: the Sep 30 box thread.** It is kept out only by "for that beat" and by Oliver's own "nothing waits on it". His reply concedes the fix is not on prod.

No other Julia-visible window message adds to the set, and none contradicts or closes a truth.json item. The hold test is met by one report only, Vincent's Sep 30 re-test, which matches Reading A.

## What was read

Julia = EMPLOYEE_0005_SLACK_ID in `channels.json` `members` (147 conversations). 13 have window messages, 2 more have only Sep 24 margin rows, and 132 have none. All 4,840 monthly files were checked: no row's ts falls outside its month file, so no window reply sits in an older file. Replies to pre-window parents are counted. 8 mpims have julia.lawson in the name but not in `members`; none has a window row. Julia's join and leave events differ from `members` in three channels: #issuefeed (joined, not listed), #industry and the solsten channel (left, still listed). None has a Julia-visible window row in the table, so the differences change nothing.

| Conversation | Kind | Window msgs | of which replies | Injected | Sep 24 margin (before 17:40:52Z) |
|---|---|---:|---:|---:|---:|
| C05433XK267 #builds | public, bot only | 285 | 0 | 0 | 24 |
| D05GU6L0XFH Robert | DM | 269 | 8 | 1 | 10 |
| C08R27X0EAH #zombie-bugs | private | 156 | 81 | 2 | 2 |
| C090N54TG79 #zombie-design | private | 150 | 60 | 0 | 7 |
| C09ATAJ220H #zm-animations | private | 63 | 52 | 0 | 0 |
| C0880U9751A #zombie-match3d | private | 62 | 29 | 1 | 3 |
| C08R8CHB0QL #zombie-art | public | 31 | 17 | 0 | 0 |
| D076RBM29JS Brian | DM | 14 | 0 | 0 | 0 |
| C04RYU8TJ8K #random | public | 12 | 0 | 0 | 0 |
| CC43664F351E mpdm Julia, Brian, Vincent | mpim | 9 | 0 | 0 | 0 |
| C08H78VJG80 #playablex | private | 7 | 6 | 0 | 6 |
| C05KNDCHAAG #company-internal | private | 3 | 0 | 0 | 0 |
| D05SD5QLG94 Frederick | DM | 2 | 1 | 2 | 0 |
| D05HMBQUC8Z Claire | DM | 0 | 0 | 0 | 16 |
| D07GMT8T0AY Oliver | DM | 0 | 0 | 0 | 5 |
| **Total** | | **1,063** | **254** | **6** | **73** |

All 10 injected Slack rows are accounted for: 6 in the table, 1 before the window (Robert's Halloween ok, Sep 18, #zombie-art), 3 mirrors in #zombie-prs (not a member).

**How #builds was read.** Of 285 rows, 111 are "Started", 32 "Unknown" and 52 "Success, No Changes"; 4 failures and 86 success rows carry content. I read every row up to Sep 26 12:12Z raw, then a view with the Started, Unknown and No Changes rows dropped. All 165 unique commit lines were read in full, since the render cut long attachments. The failures are Vision Bot #13, Android #1990 on a branch, Android Submission #132 (rerun #133 passed) and iOS #1744 (next build passed). None concerns a beat.

**Other checks.** Block text matches `text` except three anonymised food words. File `transcription` fields carry status only. The two `tabbed_canvas_updated` rows carry no text. A beat-word sweep over everything except #builds, run after the full read, found nothing new.

## List 1: flags that qualify under the rule

| # | Flag | Beat | Kind | Closed? | Against truth.json and Reading A |
|---|---|---|---|---|---|
| 1 | Vincent, #zombie-match3d, ts 1759265412.481909 [INJ]: "Re-tested the weekly leaderboard on the current prod build: it still does not start a new week." | Weekly Leaderboard | Held beat's fix | Open at the clock | **MATCH.** Slack names no owner; the owner comes from elsewhere (truth "league owner", Reading A Douglas) |
| 2 | Marcus, #zm-animations, ts 1758815614.940719: "The vfx added to the endless mode gameplay... I also need to add few text animations like for the combo when it changes etc.... and when i'm done with that if this it's cool i will make ticket for implementation" | Endless | Player-facing art | Not cleanly (see below) | **EXTRA.** truth Endless Still to do is ""; Reading A says "Not listed: ... endless polish (ZOM-565, ZOM-465 leftovers)" |

**Truth items with no Julia-visible Slack carrier.** Vial models, C&W icon animation, C&W server windows, premium strip and November config have none. That is not a defect, because all five sit in GitHub, Linear, GCal or Gmail. Three have mirrors in #zombie-prs, where Julia is not a member. Nothing in the window closes or contradicts any of them.

### Why item 2 is not closed

- **It fits the rule.** It is dated after the brief, names Endless, is player-facing art and says not done. Somebody flagged it, so "polish nobody flagged" does not reach it.
- **"Nobody said it must land" cannot exclude it.** Truth's own Marcus item has no such words either: "The Collect & Win event icon animation is still to do on my side". The vial note has none: "The final vial models are missing, Claire has those on her list." Excluding item 2 on that ground removes both.
- **Keep-out record:** cmt_zom565_1, Sep 29: "I pushed a small change to the endless screen prefab... This is the P1/P2 endless polish from the list Brian gave me, the screen already works without it, so it is not needed for the beta." Brian's list (#zm-animations ts 1757677307.424489) has "*P1/P2 – Endless mode remaining VFX*" and "*P1/P2 – VFX for endless and boss arena*". That chain is real and Julia can read it.
- **The gap:** the comment's subject is the start screen, and ZOM-565's own description separates the two: "I'm going to start working on the endless mode vfx inside of the core game part." The core-game work is still unfinished on an unmerged branch: 7683df0351, Sep 30, "infiniteBoss and endless mode core gameplay ui vfx wip", on marcus.bennett/EndlessMode_Vfx. The comment is also the owner's own claim.
- **Records that cannot close it:** the Sep 29 POD notes say Marcus "has completed work on... VFX for the endless mode and boss arena", but f_b7aae618602a7ccc0cc9a7 is Leonard's, private, `shared_with_emails` empty, so Julia cannot open it. F24 and census SO-45 settled this under the old rule and on the start-screen comment, before "flagged... as not done" was the test.

**Smallest fix.** Add one comment on ZOM-565 from Brian, who owns the list, in the shape of his ZOM-526 and ZOM-566 comments the platform already accepted. It would go after 2025-09-29T14:34:12Z, with an `updated_at` bump. For example: "The core-game endless VFX Marcus is on is the same P1/P2 polish. Endless runs without it, so it does not have to land before the beta." No graded value changes. It fits the base, where Marcus's branch stays WIP.

## List 2: borderline flags

| # | Flag | Beat link | Status | Quote that keeps it out, or why it does not |
|---|---|---|---|---|
| B1 | Martin, #zombie-art, ts 1759159849.386619: "I'm preparing a *desert theme* for the *Endless Mode*! What do you think?"; ts 1759249627.370789: "*Port theme* to have more variants to choose for Endless or Main gameplay mode" | Endless, named | **OPEN, SILENCE** | No record speaks to it. Only the rule's wording helps: a preview asking for feedback is arguably not "flagged... as not done". Arthur #470: "Endless... schedules are already running on prod." Julia replied "It looks super cute and polished". Gmail search for "desert theme" returned nothing (complete scan). **Fix:** one reply in that thread from Martin: "Nothing waits on this, Endless runs with what it has." Update the parent's `reply_count` and `latest_reply`. Do not write "not in the beta": Leonard's private notes record Robert suggesting an A/B test of it. Martin's Sep 26 DM, not Julia-visible, says "we are not changing it for now" |
| B2 | #zombie-bugs thread ts 1759249488.495439. Vincent: "we should squeeze in the fix for that issue... players can see that for 10 times in a day". Marcus: "lightSweep Box Variant material". Oliver [INJ] ts 1759267492.604719: "it goes out with the next build and nothing waits on it." | No beat named. Reachable "box" wording: ZOM-344 "Quest box", ZOM-565 "The icon item (the box)". The image has no content | **BORDERLINE, SCOPE_GAP** | Keep-out: rule "for that beat" and "nothing waits on it". Weak point: the shape matches the failed ZOM-534 fork, the fix owner's own claim with the fix not yet on prod. Commit 25c6c66b6b is 21:20:26Z, after iOS #50 (19:15:49Z) and Android #135 (20:13:09Z). **Fix:** change the end of Oliver's reply to "...the boxes work the same without it, so it does not have to land before the beta", or add that line from Vincent, who raised it and is not the owner |
| B3 | #builds: ts 1759268526.402559 "Fix season pass main screen instance from join popup"; ts 1759297851.501209 "Fix end popup"; ts 1759267655.279269 "...removing popup tutorial from level model endless_02" | Season Pass and Endless, named. All after the submission builds Samuel's ZOM-432 note pins | **Kept out by the rule** | "what has been flagged": a Jenkins change line flags nothing as not done, and no person does. Watch it: same main-vs-prod shape as F27, and Oliver's new "next build" gives a reader the bridge |
| B4 | Robert, #zm-animations, Sep 30 18:16Z thread: "We also could use a better "enraged" effects on zombies, it's not obvious enough"; ts 1759271111.547909: "I want to replace the electricity, that was a placeholder" | No beat named; all modes | **Kept out by the rule** | "for that beat". A reviewer would have to map enrage to Endless through ZOM-517 |
| B5 | Robert, #zombie-bugs, ts 1758738754.255909: Leonard's friend's game "froze for good... during his first attempt at endless mode level" | Endless | **Kept out by the rule** | A bug, not a deploy, config or art: "Nothing else goes in". Brief: "an unverified one does not" hold. Same message: "Once Leonard's friend restarted, his log just continued to the next level". Leonard's reply [INJ]: "Could not get it to freeze" |
| B6 | Thread ts 1758905363.341129, Oliver: "create linear tasks to move each liveops feature to Addressables"; "I'll start moving season pass soon" | All live-ops; Season Pass | **Kept out by the rule** | Performance work, outside the parenthesis. Season Pass part shipped: #builds "setting addressables for season pass objects" (#473) |
| B7 | Oliver, #zombie-match3d, ts 1758821469.554029: "reducing number of objects in endless mode" | Endless | **Kept out by the rule** | Performance; same reason as B6 |
| B8 | Calvin, ts 1759183318.447139: "Showing Win&Collect Queue manager implementation... let me know if that seems okay" | Collect & Win, daily gift | **Closed** | #builds, Sep 30: "Merge pull request #472" |
| B9 | Calvin, ts 1759161289.051769: card VFX "almost done"; Marcus "um no" | None; cards are not a beat | **Closed** | Brian: "it looks better"; #builds "Adding card pack animation" |
| B10 | Marcus and Robert, ts 1759247492.619029 onwards: infinite boss tap-shot art; Robert's rapid-fire bar | Boss Arena | **Off calendar** | Brief: "Boss Arena is off this calendar until the pivot call." |
| B11 | Vincent, ts 1758903616.346579: "After I skipped the zombie lane tutorial, ı got the exception and skipping couldn't claim the ice cream." | Zombie Lane | **Off calendar** | Reply: "keep Zombie Lane off the calendar". Also Oliver: "sent a fix" |
| B12 | Robert, ts 1758823142.221059: push-permission prompt may cut audio on Samsung; seen in Fortress Merge, another game | Pushes, not a beat | **Kept out by the rule** | "It could very well be an OS bug that we can't fix." Not a deploy, config or art |

Read and found to be neither beats nor flags: new level objects (#zombie-art), level and funnel talk (#zombie-design), monster HP and shaders, playable ads, and Unity upgrade notes. Julia's DMs with Robert are mostly food talk.

Robert's reworded withdrawal does not collide with Martin's new themes. "the themed prop set I okayed" matches only his Sep 18 reply, "one themed prop set only"; he never replied in the Sep 29 or Sep 30 threads.

## Reports that could meet the hold test

Test: "players provably cannot enter, score or claim on prod even after a restart".

| Report | Prod | Survives restart | Beat | Result |
|---|---|---|---|---|
| Vincent, Sep 30 20:50Z [INJ]: "I killed the app and reopened it twice... my week is still last week one. Same on the second device." | Yes | Yes | Weekly Leaderboard | **Holds.** Matches truth and Reading A |
| Robert, ts 1758735677.043699 and ts 1758740929.009929: "simply can't even play it"; "something in our FTUE system that's breaking the game, and restarting the app doesn't seem to help" | Yes | Claimed | None; levels 3 to 5 | Not a beat. Not proved either: Oliver "maybe the FTUE system is ok and the problem is elsewhere"; Robert later finds bots |
| Robert, ts 1758738754.255909: friend's Endless freeze | Yes | No | Endless | Fails: restart cleared it |
| Vincent, ts 1758903616.346579: Zombie Lane claim after skip | Not stated | Not stated | Zombie Lane | Off calendar; fix sent |

## Limits

- **Public channels Julia is not in.** I treated these as not visible, as the platform's P2-DR6 does, but `Ask_Carriers.md` marks non-member read access unknown. If they are readable, these join the candidates:
  - #zm-collect-win, Brian, Sep 26 15:10Z: "@Douglas I Also changed 1 reward in each of the two reward tables. Could you update them?" This is a Collect & Win config item with no closure in the window.
  - Collect&Win canvas, Sep 26: "it first shows placeholder icon", "shows placeholder images at first".
  - On the other side, Vincent, Sep 30 16:47Z: "none of them blockers and doesn't affect the submission".
  - I read #zm-collect-win (27), Bug Checklist (38), Collect&Win issues (18) and #gpt (26) in full. For #zombie-prs (193) I read a filtered view that dropped CodeRabbit, merge, review-request and approval rows; GitHub itself is unscoped.
- **Not read:** other people's DMs, mpims and private channels, except targeted greps used only to check wording against the base (marked as not Julia-visible above).
- **Not available:** Slack images and videos carry no content, including the Sep 30 box image.
- **Date edge:** the brief text says only "Frederick, Sep 24". The 73 Julia-visible Slack rows from Sep 24 00:00Z to 17:40:52Z hold no beat flag, so the cutoff instant changes nothing in Slack. Linear does have Sep 24 rows just before it; that is outside this file.
