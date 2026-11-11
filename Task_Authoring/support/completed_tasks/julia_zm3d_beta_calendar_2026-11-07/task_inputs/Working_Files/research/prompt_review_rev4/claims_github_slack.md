# Claim audit: injected GitHub notes and Slack messages vs base (SynthCut, clock 2025-10-01 07:00 UTC)

Scope: slice (a) the four GitHub notes with timeline events, PR bumps and four #zombie-prs mirrors; slice (b) the five injected Slack messages. The SQL was read only, never executed. Nothing was written except this file.

Path shorthand
- `$OS` = `/Users/sumit/Source/OC/Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data`
- `$GH` = `/Users/sumit/Source/OC/Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github`
- `$GM` = `/Users/sumit/Source/OC/Universe_SynthCut/SynthCut_HarmonyGames_Gmail/Services_Data/gmail`
- Slack locators are `<channel>/<YYYY-MM>.json[index]` under `$OS/slack/messages/`.

## Bottom line

No injected record is flatly contradicted by an explicit base statement, but two are exposed enough that a strict reviewer could fail them, and there are seven convention breaches.

1. **#470 rc_10 has a timing conflict.** Base records a prod environment update by Douglas at 18:16:33Z on Sep 30, 2h12m after the comment says Collect & Win "reaches prod with the next backend release". Base also has a Sep 29 action item to deploy Win and Collect to prod servers.
2. **#468 rc_38 misattributes the owner.** Base says Martin Walsh does the Collect & Win bottle UI icons and Claire edits the 3D object. The PR also already ships vial sprites in all five colours, so "missing" collides with the files.
3. **Seven convention breaches**, the two most visible being the #zombie-art parent left with `reply_count = 1` and a NULL thread key, and `#471#c_18` being the only non-contiguous PR comment id in the universe.

Everything else is confirmed or uncontradicted.

## Verdict table

| Record | Claim | Verdict | Evidence locator |
|---|---|---|---|
| #470 rev_10 / rc_10 | C&W server windows still on DEV stack only (as of Sep 30 16:04:12Z) | TIMING CONFLICT | True through Sep 29: Confluence `page_liveops_calendar` ("not yet live"), gdocs `f_b7aae618602a7ccc0cc9a7` ("needs to be deployed to production servers"), Slack `D05SG9H1CFM/2025-09.json[405-408]`. Later base event: `D079SNE2TL4/2025-09.json[263]` prod update 18:16:33Z |
| #470 rc_10 | "they reach prod with the next backend release" | TIMING CONFLICT | Same as above |
| #470 rc_10 | Plague Race, leagues, Endless, Season Pass schedules already on prod | CONFIRMED | Confluence `page_liveops_calendar`, `page_season_pass_spec`; Slack `D07GY332589/2025-09.json[311]`; CDK stack lines 139-189 |
| #470 rc_10 | Client side of this PR is fine | CONFIRMED | `$GH/data.json` reviews[2176] `#470#rev_9` APPROVED 15:51:06Z by Arthur; merged 15:51:15Z |
| #468 rev_3 / rc_38 | Final vial sprites still missing for the C&W set | UNCONTRADICTED, wording exposed | PR #468 merge commit `8ce4379821` adds `icn - poison - {blue,green,orange,purple,red}.png` and `img - {same five}.png`; nothing in base calls them placeholders |
| #468 rc_38 | Claire has those on her list | CONTRADICTED (ownership) | `D05PV7UMRUL/2025-08.json[1]`, `[10]`; `D076V3NEA7P/2025-08.json[77]`, `[81]`, `[86]` |
| #468 rc_38 | Everything else on the art side of this PR is settled | UNCONTRADICTED, mild tension | Open C&W art/UI items: `CF4EDAF93359/2025-09.json[91]` (Sep 29), `D076V3NB6P7/2025-09.json[70]` (Sep 30 16:33Z) |
| #473 c_2 | Season Pass premium strip must move to the November range | UNCONTRADICTED | No "premium strip" or date range anywhere in base; nearest assets are `Assets/Sprites/Season Pass/bg - golden stripe.png` |
| #473 c_2 | Oliver is taking the date change | UNCONTRADICTED, fits | Oliver authored #473; Trello card "Season Pass - (Brian/Oliver)"; his later commits do not mention it |
| #471 c_18 | The daily-gift frame went out with this PR | UNCONTRADICTED, weak support | `$GH/data.json` pull_request_commits[12599] "Fixing UI Elements on Daily Gift ... update header image"; merge diff touches `Assets/Sprites/Daily Gift/img - DailyGift.png` |
| #471 c_18 | In both submission builds from today, iOS 50 and Android 135 | CONFIRMED | `C05433XK267/2025-09.json[1120]`, `[1123]`, `[1122]`, `[1124]`; Gmail "Zombie Match 3D 0.3.50 (50) for iOS is now available to test" 19:26:04Z |
| #471 c_18 | Nothing left on it, that one can be closed | UNCONTRADICTED | Linear ZOM-432 is Todo in base, assignee Calvin (`$OS/linear/data.json` issues[3499]) |
| Four #zombie-prs mirrors | Format, thread parent, reply counts, GitHub comment ids | CONFIRMED, with three format deviations | Parents at `C093LEZGF6J/2025-09.json[579]`, `[530]`, `[605]`, `[583]` |
| Frederick ask `8b090dec…` | Mon Oct 6 and Sun Nov 2 weekdays | CONFIRMED | Calendar arithmetic |
| Frederick ask | Beta buy starts Oct 6 | UNCONTRADICTED, soft tension | Trello list `6851a674975da1fe76e70d93` is named "BETA: Oct 10"; `D04UP2L3E3S/2025-09.json[775]` "barely get the beta out by mid october" |
| Frederick ask | Frederick asks Julia for the live-ops calendar; pivot call | CONFIRMED fit | Confluence `page_liveops_calendar` (owner Frederick, design led by Julia); `C090N54TG79/2025-09.json[537]` |
| Frederick reply `097c95c6…` | PNs Beta tab has the four named rows | CONFIRMED | `$OS/gsheets/data.json` sheets_spreadsheets[220] tab 1, rows R3, R9, R11, R12 |
| Frederick reply | Those four are not in the beta, and just those four | CONFIRMED | See S2 below |
| Frederick reply | Copy with no game name is fine; rule is about wrong names | UNCONTRADICTED | Rule is injected; base sheet rows R5 and R7 name "Puzzles vs Zombies", the pre-rename store name |
| Frederick reply | Zombie Lane is a permanent track with no window or reset | CONFIRMED | Confluence `page_liveops_calendar`, `page_live_ops_engine`; backend `lib/zombies_game/leaderboards.ex` lines 309-312 |
| Robert approval `2e75e232…` | Halloween one-off approved, may take a recurring slot | UNCONTRADICTED, fits | Parent `C08R8CHB0QL/2025-09.json[121]`; Confluence rule on documented Product approval; Robert is "Owner: Robert (Product)" |
| Robert retraction `58d06bd5…` | Pulling the ok, take it off the beta calendar | UNCONTRADICTED, mild tension | Robert suggested A/B testing a desert theme on Sep 29 (gdocs `f_b7aae618602a7ccc0cc9a7`) |
| Vincent retest `fa3eee2c…` | Weekly leaderboard still does not start a new week after two restarts, two devices | UNCONTRADICTED | ZOM-429 open in Backlog; no base statement on Sep 29-30 either way |

## Slice (a): GitHub notes

### G1. match3d#470 review rev_10 and inline rc_10 (Arthur, 2025-09-30T16:04:12Z)

Base record: PR #470 "Collect And Win minor bugs fixes", author Owen Baker, created 2025-09-29T21:22:50Z, merged by Arthur at 15:51:15Z on Sep 30. Base has rev_1 to rev_9, rc_1 to rc_9, ev_1 to ev_8. The injected ids rev_10, rc_10 and ev_9 are the next free ones. The path `Assets/Scripts/UI/CollectAndWin/CollectAndWinMainScreenController.cs` is in the PR.

**Claim: C&W server windows are still on the DEV stack only, and reach prod with the next backend release.**

What supports it, up to Sep 29:
- Confluence `page_liveops_calendar` (updated 2025-09-29T17:00:00Z): "Collect & Win | Zombie Match 3D | ... Built for the end-of-September beta submission (QA blockers cleared 26 Sep 2025); not yet live."
- gdocs `f_b7aae618602a7ccc0cc9a7` ("POD_ PROTOTYPE - 2025_09_29 08_56 PDT - Notes"): "the 'Win and Collect' feature needs to be deployed to production servers."
- Slack `D05SG9H1CFM/2025-09.json[405-408]`, Sep 26 20:48-21:00Z. Douglas: "Ese merge con main significa que debo deployar a prod?" Owen: "Igual no va para release ahora / asi que creeria que no."

What conflicts with it:
- The same pod notes carry an action item: "[Douglas] will help [Leonard] to deploy the win and collect to pro servers and complete the configuration for Google Play login." The transcript has Leonard saying "maybe that's something Douglas can help me with today."
- Slack `D079SNE2TL4/2025-09.json[263]`, ts 1759256193.859279, 2025-09-30T18:16:33Z. Douglas: "Ok, I updated the prod environment with the latest teams/social changes, let me know if you are still getting those issues."
- Linear ZOM-563 moved to In Progress at 18:14:25Z the same day.

Base never says Collect & Win went to prod, and the Sep 30 update is described as teams/social. But the comment is timestamped before a base prod update, and base planned a prod deploy of this exact feature the day before. A reviewer can read 18:16:33Z as "the next backend release". This also bears on the injected Oct 8 calendar deploy, which is outside my slice.

**Claim: Plague Race, leagues, Endless and Season Pass schedules already run on prod.** Confirmed.
- Confluence `page_liveops_calendar`: "Zombie Match 3D overlaps Plague Race, Leagues and both Endless Monster resets"; Plague Race, Endless Monster Mode and Weekly Leaderboards are all marked Live.
- Confluence `page_season_pass_spec`: "Reached production in the week of September 22-29, 2025 - Android 0.3.127 published Sep 22, iOS 0.3.49 released Sep 29."
- Slack `D07GY332589/2025-09.json[311]`: "The event resets the very first day of the month in prod."
- `$GH/root/harmonygames-Games/match3d-backend/zombies-game-cdk/lib/zombies-game-cdk-stack.ts` lines 139, 143, 147, 153, 189 hold the prod crons.

I found no base statement that any of the four is not on prod.

Structure: the `reviewed` event shape matches base (empty actor, null `created_at`, `commit_id` equal to head sha `4935e948…`). The `updated_at` bump is correct. `diff_hunk` is empty, which base has in only 53 of 1,387 review comments and in none of Arthur's on match3d.

### G2. match3d#468 review rev_3 and inline rc_38 (Arthur, 2025-09-29T15:36:41Z)

Base record: PR #468 "Collect And Win", author Owen, created 2025-09-26T20:16:25Z, merged by EMPLOYEE_0032 at 2025-09-29T16:13:50Z during the pod meeting. Base has rev_1 and rev_2, rc_1 to rc_37, ev_1 to ev_5. The path `Assets/Sprites/CollectAndWin/icn - poison - red.png.meta` is in the PR (base rc_32). No `updated_at` bump is needed because the review predates the merge.

**Claim: the final vial sprites are still missing.** The PR itself adds the full sprite set in five colours, and no base record calls them placeholders. The word "final" keeps this from being a flat contradiction, but "missing" sits on a file that exists.

**Claim: Claire has those on her list.** Contradicted on ownership.
- `D05PV7UMRUL/2025-08.json[1]`, Claire to Martin, Aug 5: "I think you can work this for ui, and decide the colors and I will edit the 3d object according to your ui."
- `D076V3NEA7P/2025-08.json[86]`, Martin, Aug 5: "I did all the bottles vector so I can touch it all the time." Index [81]: "It means that we will need 5 different images... I can do it no problem."
- `D05PV7UMRUL/2025-08.json[10]`, Claire, Aug 7: "can you send me the new potion stuff you make so I can model it."

So in base the 2D bottle sprites are Martin's and the 3D object is Claire's. Claire's Sep 19-30 messages are all about board objects, with nothing on vials.

**Claim: everything else on the art side is settled.** Hedged by "of this PR" and "from my side", but base has open C&W art/UI items after it: Brian's tablet UI list in the Bug Checklist canvas on Sep 29, and his request to Marcus on Sep 30 16:33Z to "polish the bottle vfx for Collect&win".

Author fit: Arthur never reviewed #468 in base, and he is the CTO speaking for "the art side". That is weak but not contradictory.

Structure: `#468#ev_6` is a `reviewed` event numbered after `merged` (ev_4) and `closed` (ev_5), although the review predates the merge. Base has this ordering in 4 of 2,116 reviewed events.

### G3. match3d#473 conversation comment c_2 (Arthur, 2025-09-30T16:16:33Z)

Base record: PR #473 "Addressables/sp", author and merger Oliver, created 15:41:05Z, merged 15:41:20Z, base `updated_at` 15:43:58Z. Base has c_1 and ev_1 to ev_4, so c_2 and ev_5 are correct.

Both claims are uncontradicted. Base has no "premium strip" and no client-side date range. Seasons reset monthly on the 1st at 00:00 UTC per the Season Pass spec. Oliver's later Season Pass commits (21:20Z, 21:36Z, Oct 1 05:44Z) do not mention a date change, so the to-do is still open at the clock.

Structure: `updated_at` is set on the comment, where base has NULL on all 687 PR comments. Base also sends GitHub notification mails to the PR author (`$GM/threads/oliver@harmonygames.co_1844704072865400613.json`), and there is no mail for this comment. The integration notes mark that companion optional.

### G4. match3d#471 conversation comment c_18 (Samuel, 2025-09-30T21:07:26Z)

Base record: PR #471 "Samuel/zom 498 536", author Samuel, merged by Arthur at 15:52:24Z on Sep 30. Base has c_1 and c_2, and ev_1 to ev_7.

**Builds claim confirmed.**
- `C05433XK267/2025-09.json[1120]`: "Match 3D iOS Submission - #50 Started by user Arthur Blake" at 18:43:32Z; `[1123]` success at 19:15:49Z.
- `[1122]`: "Match3D Android Submission - #135 Started" at 18:45:34Z; `[1124]` success at 20:13:09Z, with "Fixing UI Elements on Daily Gift [Samuel Turner]" in the change list.
- Both were built from main after the #471 merge, and the comment postdates both.

**Frame claim uncontradicted.** Base says "update header image" for the Daily Gift commit, and Samuel's own change list (`D06UFE81RF0/2025-09.json[31]`) lists only font size and alignment. The image is an LFS pointer, so I could not check whether it has a frame.

Structure: the id should be `#471#c_3`. All 630 base PRs with comments number them contiguously from c_1; c_18 would be the only gap. It looks like it was chosen to avoid the commit ids c_0 to c_17, but those live in a different table and base already has `#471#c_1` in both.

### Mirrors in #zombie-prs (C093LEZGF6J)

Parent reply counts and `latest_reply` values are all correct against base: #470 16 to 17, #468 41 to 42 with `latest_reply` unchanged, #473 2 to 3, #471 7 to 8. Attachment key set, colour, fallback, pretext logins and titles match base. The four GitHub comment ids are unique and fall in the right order between neighbouring base ids.

Three deviations:
- **Lag.** Injected mirrors land 0.16-0.27 s after the GitHub event. Across 956 base comment mirrors the minimum is 1.9 s and the median 4.3 s.
- **Ampersand.** The #470 and #468 mirror text has a raw "Collect & Win". Base bot attachments escape it as `&amp;` (651 escaped, 1 raw).
- **Fractional seconds** repeat the epoch digits (`.248252`, `.160201`), which is a synthetic pattern.

## Slice (b): Slack messages

### S1. Frederick's ask, D05SD5QLG94, 2025-09-30T20:20:00Z

Placement fits. The last base message in this DM is Sep 18. Frederick posts in #executives at 20:27:30Z the same day. The parent carries its own ts as thread key with `reply_count` 1.

The Oct 6 start is uncontradicted, but note three base records: the Trello ZM ROADMAP list is now named "BETA: Oct 10" (the last action record, Sep 30 17:09Z, still shows "BETA: Sep 30"); Leonard on Sep 25 says "We can barely get the beta out by mid october"; and Frederick on Sep 30 16:04Z says "We are only running the retention campaigns."

### S2. Frederick's thread reply, 2025-09-30T20:24:38Z

The "PNs Beta" tab of "Push Notifications Zombie Match" (`f_a325dd4af80afc5994d5dc`) has 14 data rows. The four named rows are R3 (Hourly Coins), R9 (Nathan's Treasure Hunt), R11 (Streak Fever) and R12 (Axe Arena).

All four are off-beta in base:
- **Axe Arena:** "We've decided to postpone Axe Arena for the beta release" (`C05KNDCHAAG/2025-09.json[31]`); the Trello card sits in the "Oct 21" list.
- **Hourly Coins:** Trello card "Hourly Collection" moved to Backlog on Sep 23.
- **Nathan's Treasure Hunt and Streak Fever:** Domino Delights events per Confluence `page_liveops_calendar`.
- None of the four has any code in the match3d client or backend trees.

The other ten rows all map to things in the beta: quests, lives, two lapsed-player rows, first-session, Win & Collect, Plague Race, Login Calendar, Season Pass and Weekly Leaderboard. So "just those four" holds.

Zombie Lane is confirmed permanent: Confluence lists it as "Permanent (level-gated reward track)", the backend gives it no schedule, and Leonard wrote on Jul 12 "I thought it was never gonna end" (`C08R6BF4ENN/2025-07.json[124]`).

### S3. Robert's Halloween approval, #zombie-art thread reply, 2025-09-18T16:40:00Z

The parent is Martin's post "*Halloween theme* for an app icon or an event" tagging Robert, Leonard and Julia. Robert is active in the channel at 16:25Z and 16:49Z. "Beta" was a live term by then (Leonard's Sep 12 note: "Beta target: Sep 30"). Julia relayed on Aug 27 that `[PERSON_NAME_0054]` wanted seasonal themes, Halloween first (`D05QESBD4HW/2025-08.json[128]`); that placeholder appears to be Robert. I found no Halloween statement by Robert or anyone else after Sep 18.

Structure breach: the base parent has `thread_ts` null and zero replies. The UPDATE sets `reply_count`, `reply_users_count` and `latest_reply` but not `thread_ts_legacy`. All 15,204 base parents with replies have `thread_ts` equal to their own ts.

### S4. Robert's retraction, D05GU6L0XFH, 2025-09-30T22:10:00Z

It sits between Julia's 20:46:05Z message and Robert's Oct 1 03:32:57Z message. Robert is active at 22:25Z in #zm-animations. The "may not ship at all" rationale fits the base pivot talk. The "not spending art time on a theme" rationale is in mild tension with base: on Sep 29 Robert suggested A/B testing Martin's desert theme, and Martin posted a port theme on Sep 30.

### S5. Vincent's weekly-leaderboard retest, #zombie-match3d, 2025-09-30T20:50:12Z

- ZOM-429 (Backlog, assignee Douglas, last updated Sep 22) says in July that the leaderboard "can only proceed to next leaderboard if the app is killed". The injected message is a later, worse observation, not a contradiction.
- On Monday Sep 22 base has a precedent: `C08R27X0EAH/2025-09.json[902]` "I cannot participate in leaderboard. Killing the app doesn't help", then `[904]` twelve minutes later "after a moment, I am now in the weekly leaderboard."
- I found no base statement on Sep 29-30 that the rollover was fixed or works after restart.
- "Current prod build" fits: Leonard released iOS 0.3.49 on Sep 29 21:55Z. Vincent was testing prod that evening (21:58:44Z).

Placement is atypical. Vincent's bug posts go to #zombie-bugs (21 top-level in September) rather than #zombie-match3d (4). Julia is in both.

## Ranked findings and fixes

**1. #470 rc_10 timing conflict (highest risk).** Move the review, inline comment, PR bump and mirror to after Douglas's update, and reconcile it in the text:
- `submitted_at` / `created_at` / PR `updated_at`: `2025-09-30T18:41:19Z`. Arthur is active then (commit at 18:37Z, submission builds started 18:43Z).
- Text: "Server-side windows for Collect & Win are still on the DEV stack only. Today's prod update carried the teams/social changes only, the windows reach prod with the next backend release. …" with the rest unchanged.
- Mirror: attachment ts 1759257679, message ts about 3 s later, a discussion id between r2389766458 and r2392548744, and the parent `latest_reply` to match.

**2. #468 rc_38 owner and wording.** Two options:
- Smallest edit: change the owner to Martin ("Martin has those on his list"), and soften "missing" to "not in yet".
- If the answer key needs Claire: make it the 3D vial variants ("The final vial models are still missing … Claire has those on her list") and re-anchor the path to `Assets/Match3D/Game/Levels/GameLoader.cs`, which is in the PR.
Either way, apply the same text to the mirror.

**3. Convention breaches.**
- Add `thread_ts_legacy = '1758121809.236839'` to the UPDATE on `9025d428af1f551a20e303c3acbc545b`.
- Rename `#471#c_18` to `#471#c_3`.
- Set `updated_at` to NULL on both injected PR comments.
- Shift the four mirror `ts` / `created_at` values by 2-5 s and update the three `latest_reply` values that point at them.
- Write `Collect &amp; Win` in the #470 and #468 mirror attachment text.
- Optional: give the two inline comments a `diff_hunk`; accept or avoid the `#468#ev_6` ordering.

**4. Soft tensions, no edit strictly needed.**
- Beta buy from Oct 6 vs Trello "BETA: Oct 10".
- "Everything else on the art side is settled" vs open C&W art items; dropping that sentence removes it.
- Robert's "art time on a theme" rationale vs his Sep 29 support for theme work.
- Vincent's channel; #zombie-bugs is his usual place.

## Searches run

All records: full-text scans of every Slack channel and DM for September and October 2025 (21,689 messages), plus all-2025 or all-time scans where noted. Full recursive string scans of Confluence, Trello, Linear, GCal, GSlides, GDocs and GDrive metadata. grep over all 81,404 Gmail thread files. ripgrep keyword counts over the Snowflake export (zero hits for every feature keyword). The GitHub export tables and the match3d, match3d-backend and ZM-Liveops-Docs repo trees with read-only git log and diff.

- **#470 rc_10:** Slack for prod, production, dev, deploy, backend release and CDK from Sep 22; every Douglas message from Sep 26; the Owen/Douglas, Oliver/Douglas and Vincent/Douglas DMs in full; #zm-collect-win in full; both C&W canvases; every Collect & Win mention from Sep 29; backend config, CDK stack and git log; the Sep 29 pod notes; Confluence calendar, Season Pass spec, GDD and engine pages.
- **#468 rc_38:** Slack for vial, bottle, potion, antidote, poison and token from Aug 1; every Claire message, DM and mention from Sep 19; the Brian/Martin and Claire/Martin August DMs in full; PR #468 file list and sprite directory; GitHub text for "vial".
- **#473 c_2:** Slack for premium, season pass, strip, stripe, banner, November, range and date from Sep 8; the Oliver/Arthur DM; Season Pass assets and scripts in the client tree; the Season Pass spec; Oliver's commits after the comment.
- **#471 c_18:** #builds from Sep 29 12:00Z to the clock; Gmail for 0.3.50 and 0.3.135; Slack and Gmail for daily gift with frame; Linear ZOM-432, ZOM-498, ZOM-536, ZOM-556; PR #471 merge diff; the Samuel/Vincent DM.
- **Mirrors:** all replies in the four threads; lag and ampersand statistics over the whole channel; id and ts collision checks; GitHub comment-id ordering.
- **Frederick's messages:** the DM since March; every Frederick message from Sep 14 on UA, beta, pushes and live ops; Slack for beta, pivot and launch in September; #executives from Sep 29 to the clock; the push sheet row by row; Trello ZM ROADMAP lists, cards and list-rename history; Slack, Trello, Linear, GCal and code for the four feature names; Zombie Lane timing terms across all 2025 Slack, Confluence, Linear and the backend.
- **Robert's messages:** Slack for Halloween, pumpkin, spooky, one-off, themed and seasonal since June 2025; #zombie-art from Sep 15 with thread fields; the Marcus/Martin and Julia/Martin DMs; the Julia/Robert DM from Sep 29; Robert's activity around both timestamps; Gmail, GDocs, GDrive and GSlides for Halloween (no relevant hits).
- **Vincent's message:** Slack for weekly, leaderboard, league, rollover, reset and restart from Sep 8, including Turkish terms from Sep 28; #zombie-match3d from Sep 24; Linear leaderboard tickets; the ZM-Liveops-Docs repo; Vincent's activity that evening.

Limits: sprite and artwork images are LFS pointers, so content could not be inspected. Turkish and Spanish DMs were read through keyword hits plus the surrounding messages, not exhaustively.
