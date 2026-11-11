# P2 deep recheck (second sample): truth of injected claims

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
SQL sha256: ffbac4586fb91842ca16263c2b76987c26623c7ed689e00d33886c63f9331bdc (matches the setup; `hg.py lint` returns 0 FAIL, 0 CHECK)

## Result

I checked all 52 injected records and the 5 ticket state or description UPDATEs against the base, including records Julia cannot see. **No injected claim is false on the record, so I have no outright fail-level finding.** There are 3 low-impact findings and 6 advisories.

**Main session must decide two things:**
- DR1 and DR2 sit in the State / Lifecycle row of Eval 1 §3.2, and that row has no low-impact band. I rate them low-impact for the reasons given in each. If you confirm either one as a true status contradiction, §3.2 scores Cross-Service Coherence as FAIL.
- §3.2 allows NON-FAIL only for a *single* low-impact inconsistency. If two or more of DR1 to DR3 are confirmed, that band no longer fits.

Paths: `OS` = `Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data`. `GH` = `Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github`. Slack messages are in `OS/slack/messages/<channel>/2025-09.json`. All times are UTC.

## Findings

Format: DR# | pass | checklist section | injected record quote | record path, id and quoted value | Eval dimension or issue type | severity

**DR1** | P2 | §3.2 State / Lifecycle | SQL `cmt_zom542_1`, Samuel, 2025-09-22: "Picking this up after the bug list." | `OS/linear/data.json` ZOM-542: `state_id` "Regression", `started_at` null, `updated_at` = `created_at` 2025-09-14T22:59:17Z, and the SQL changes only `updated_at` | Cross-Service Coherence (State / Lifecycle) | **Low-impact**
- A ticket never started sits in "Regression", and the injected comment now shows it as not begun. The SQL aligned status on ZOM-432, 344, 566 and 563 but not here.
- Why low-impact: the state is base data, Linear has no definition of it, ZOM-359 is the only other ticket in it, and no graded value reads it.

**DR2** | P2 | §3.2 State / Lifecycle, SC-15 | SQL UPDATE of ZOM-521 (`updated_at` 2025-09-30T16:27:38Z) keeps "- [X] Live-ops icons appearing on the screen and animations on these icons" | SQL `cmt_zom465_2`, Marcus, 2025-09-30T18:05:02Z: "Collect & Win came in after my note above, so its event icon is not animated yet." | Cross-Service Coherence (State / Lifecycle) | **Low-impact**
- The SQL rewrites this checklist to untick two stale rows but leaves this one ticked. A later dated comment says one icon animation is still open.
- Why low-impact: the tick dates from Sep 17, before #468 merged, the later comment names the gap, and a careful reader takes the later record.

**DR3** | P2 | §3.2 Other | SQL deck slide `slide_b83e51a09d72`: "Small scale at first, scaled up week by week if the cohorts hold." | Same deck, slide `slide_0c47d2e81b6f`: "Once the stores approve we start buying users at small scale and hold the spend there until the pivot call." | Cross-Service Coherence (Other) | **Low-impact**
- The two slides disagree on spend across the four weeks unless the undated pivot call falls early. The title slide adds "Scaled beta-cohort buy".
- Why low-impact: windows, holds and pushes do not read it. It can only colour the trade-offs in the recommendation.

**DR4** | P2 | §3.2 State / Lifecycle | SQL `cmt_zom344_1`, Marcus, 2025-09-16, with the state set to Done: "Quest box open and close animation reuses the endless chest curve and reads well on the quest screen." | Slack `CF4EDAF93359`, Vincent, 2025-09-30 13:29:35: "and the timing is off. Especially in the quest chests. It should be opened first, then the reward should be visible." Also `C08R27X0EAH`, Marcus, 2025-08-11 15:50:26: "some chest quest animations show the reward before the chest open" | Cross-Service Coherence | **Advisory**
- `git log --author=marcus` shows no Quest-named file touched between 2025-07-03 and 2025-09-17, so nothing in git backs the Done. The later bug concerns reward timing rather than the box animation, so this is unsupported, not contradicted.

**DR5** | P2 | §3.2 Temporal | SQL `#470#rc_10`, Arthur, 2025-09-30T15:51:06Z: "they reach prod with the next backend release" | Slack `D079SNE2TL4`, Douglas, 2025-09-30 18:16:33: "Ok, I updated the prod environment with the latest teams/social changes" | Cross-Service Coherence | **Advisory**
- Literally, the next prod update after Arthur's note is this one, not Oct 8. The reading that windows went live Sep 30 is ruled out by Douglas's own scope ("teams/social") and by the Oct 8 calendar text: "The server windows that are still on the DEV stack go live with this release".

**DR6** | P2 | §3.2 Referential, SC-13 | SQL Slack `bca784379e7dbca9e64e79a64dfefbba`, Frederick: "the beta buy we start Mon Oct 6 through Sun Nov 2" | Slack `D04UP2L3E3S`, Leonard, 2025-09-25 05:15:22: "We can barely get the beta out by mid october"; `OS/trello/data.json` list `6851a674975da1fe76e70d93` name "BETA: Oct 10" | Cross-Service Coherence | **Advisory**
- Leonard's line is in a DM Julia cannot read. The list name is known base issue SC-13, and its advice is to settle the date in task data, which Frederick's message and deck do. The injected Trello action correctly uses "BETA: Sep 30", matching the action stream.

**DR7** | P2 | §3.2 Temporal (phrase before its source) | SQL `933cee9f6464a80e4b1f05259b595b20`, Robert, 2025-09-18: "approved from my side for one of the beta weeks" and "if it lands before the cut" | Deck dated 2025-09-23 first lists "The four buy weeks". "the cut" has no meaning anywhere in the Slack I searched | Cross-Service Coherence | **Advisory**
- Related: "has to land" or "not needed for the beta" appears in 8 records by 5 authors from Sep 17 on (ZOM-471, 534, 526, 565 twice, 566, 542, and the Slack lightSweep reply). The first predates the brief's Sep 24 "what still has to land". It reads as seeded wording but changes no fact.

**DR8** | P2 | §3.2 Temporal | SQL `#468#ev_6` "reviewed", `created_at` NULL, added after base `#468#ev_4` merged and `ev_5` closed | `GH/data.json`: merged 2025-09-29T16:13:50Z; injected `#468#rev_3` submitted 2025-09-29T15:36:41Z | Cross-Service Coherence | **Advisory**
- By id order the review follows the close, though its dates put it before the merge. Base "reviewed" rows also have NULL times, so only id order shows this.

**DR9** | P2 | §3.2 Referential | SQL `#472#rc_1`: "the Season Pass premium strip is still set to the October range ... Oliver is taking the date change"; SQL `#468#rc_38`: "Claire has those on her list" | `GH/root/harmonygames-Games/match3d/Assets/Scripts/LiveOps/SeasonPass/SeasonPassResponse.cs`: `[JsonProperty("end_time")] public DateTime EndDate;` | Data support | **Advisory**
- Both are third-party owner claims that feed owner cells, and nothing from Claire or Oliver backs them. "premium strip" appears nowhere else, the nearest asset is `bg - golden stripe.png`, and no October or November string exists in the Season Pass scripts or prefabs. Client season dates are server-driven. The date could be in art, so this is unsupported, not contradicted.

## P2 lines

| Line | Result |
|---|---|
| Services change a graded fact | Yes. GCal gives the Oct 8 release. Gmail gives Oct 31 10:00 Istanbul against the Confluence 24h lock. GitHub gives DEV-only windows, vials and strip. Sheets gives the push rows. Slack gives the leaderboard failure and Robert's retraction. Trello gives Oct 13 quests. Linear gives the ticket notes. |
| Hidden record | None. Julia is on the event, in all three Slack channels and both DMs with no leave events, has the mails, and has the brief, deck, sheet and PNs sheet shared. `#zombie-prs` excludes her, but GitHub is unscoped. |
| Writes doable | Yes: `gsheets_values_update`, `linear_create_comment`, `gmail_reply_to_message`, `slack_send_message`. |
| Derived columns | N/A, no Snowflake read. |
| Open-instruction scope | N/A. "Every beat" is bounded by the brief's Scope section. |
| Date slips | None. All records are before the clock, and every stated weekday and the Istanbul-to-UTC conversions are correct. |
| Platform defects | None tagged. Known issues touched: SC-13, SC-15 and SC-16 (the SQL repairs ZOM-521 and ZOM-563), SC-38, SC-71. |

## Per-record claim table

"Holds" means I tried to contradict it and the record agrees. "Single source" means nothing contradicts it and nothing else confirms it.

### Slack and mail

| Record | Claims tested | Base check | Result |
|---|---|---|---|
| Frederick ask, DM, 09-30 20:20 | Oct 6 to Nov 2 buy, sheet, ticket, brief, pivot call | Deck W1 to W4; ZOM-78; pivot in Leonard's note, `#executives` 09-22 05:03; he posts `#executives` 20:27 | Holds; DR6 |
| Frederick reply, 09-30 20:24 | Four rows not in beta; local rows; Zombie Lane permanent | PNs Beta rows 3, 9, 11, 12 of 14; Trello "Hourly Collection" Backlog, Axe Arena moved to Oct 21 list 09-23; Confluence lists the others on Domino Delights, Zombie Lane "Permanent" | Holds |
| Robert approval, 09-18 16:40 | Parent thread; Product authority | Martin's thread 09-17 15:10 exists; Confluence "Owner: Robert (Product)", "recurring slot" wording; Robert active both sides | Holds; DR7 |
| Robert retraction, DM, 09-30 22:10 | Refers to Martin's thread; later than approval | Order correct; pivot doubts match Sep 29 to 30 threads; active 22:25 | Holds |
| Vincent leaderboard, 09-30 20:50 | Still fails on prod after restart | No base record of rollover working; the 09-22 leaderboard error was a different bug, reverted; he is ZOM-429's reporter; active to 21:58 | Holds, single source |
| Leonard S23 Ultra, 09-29 23:17 | Device, device farm, airstrike | His report 09-21 02:08; friend's S23 Ultra 09-21 05:13; AWS Device Farm in Slack, "cloud device farm" in Confluence; "airstrike freeze" Vincent 09-22; airstrike is in `EndlessModeBar.cs`, not a pre-level booster | Holds |
| Vincent lightSweep, 09-30 21:46 | Oliver pushed; rides next build | Commit 25c6c66b6b at 21:20 edits `lightSweep Box Variant.mat`; it is after the submission tags on 3f5352a5b5 | Holds |
| Robert themes, 09-30 16:41 | Desert and port | Port post 16:27:07 precedes it; thread reply users 3 to 4 | Holds |
| `#zombie-prs` mirrors x3 | Text, time, counts | Format matches base; reply counts 41 to 42, 16 to 17, 3 to 4; discussion ids rise in order | Holds |
| Brian mail, 09-22 | Oct 29 Wed, Nov 1 Sat, contents, owner | Dates correct; Trello's Season Pass card carries Brian's token `[PERSON_NAME_0092]`; Confluence "tiers, rewards, theme"; +0300 matches | Holds |
| Brian mail, 09-26 | Oct 31 10:00 Istanbul, two extra days | Fri correct; 07:00 UTC; Confluence lock "24h before each season opens" | Holds |

### Calendar, Drive and GitHub

| Record | Claims tested | Base check | Result |
|---|---|---|---|
| GCal Oct 8 x4 | 18:00 to 19:00 Istanbul; windows go live | 15:00 to 16:00 UTC correct; Wednesday; Owen 09-26 21:00 "no va para release ahora"; Confluence C&W "not yet live" | Holds; DR5 |
| ZM Live Ops folder, calendar sheet | Owner, parent, timing | Root `d_8140f09bf9f1b94cb8ee2d` is Julia's; sheet predates the ask, and Frederick's ask names it | Holds |
| Brief, 09-24 | C&W windows; season on the 1st; Login Calendar; translated tab | Confluence, Brian's C&W doc and CDK agree; Douglas 09-30 23:01 "very first day of the month in prod"; row 13 exists; translated tab has Tiledozer and Domino text; UK buys `#executives` 09-12 | Holds |
| Deck, 09-23 | Weeks, Sep 30 builds, Unity separate, UK and US | Weekdays correct; "Beta target: Sep 30"; Frederick 09-30 16:04 "only running the retention campaigns" | Holds; DR3 |
| `#470#rc_10`, 09-30 15:51:06 | C&W DEV-only; others on prod | Rides on `rev_9`, 9s before merge; CDK prod schedules; Confluence; Douglas and Owen 09-26 | Holds; DR5 |
| `#468#rev_3`, `rc_38`, `ev_6`, 09-29 15:36 | Vials first-pass; Claire owns | Before merge; `collectAndWinVial` exists; `ev_6` commit is PR head | Single source; DR8, DR9 |
| `#472#rc_1`, 09-30 15:52:58 | Strip range; Oliver owns | Rides on `rev_1`, before merge | Single source; DR9 |

### Linear and Trello

| Record | Claims tested | Base check | Result |
|---|---|---|---|
| ZOM-429 Douglas 09-16 | Restart reaches new week | Matches ticket text; he is assignee; superseded by Vincent 09-30 by design | Holds |
| ZOM-556 Vincent 09-24 | Submission build; claim works | Android 128 and iOS 45 tags exist by 09-23; he filed it 09-22 | Holds |
| ZOM-565 Marcus 09-29 | Pushed prefab, branch, P1/P2 | Commit 44988da015 14:33; DM 14:34:06 and 14:34:25 "i wrote a comment"; Brian's list 09-12 | Holds |
| ZOM-565 Brian 09-30 | Core VFX, refill timer are P1/P2 | Same list; ZOM-465 "Refill Timer" section | Holds |
| ZOM-543 Calvin 09-30 | Queue flow | `QueueManager.cs` at c22b1c8434 has the same four entries; #472. Trello marks it complete 20 min later (base) | Holds |
| ZOM-526 Brian 09-24 | SP tokens fly; C&W trigger on branch | 7f4e8b30be; e8aa8b39ec 09-23 | Holds |
| ZOM-526 Brian 09-26 | Unticked; Axe Arena out | Calvin updated the master ticket 09-17; Axe postponed 09-22 | Holds |
| ZOM-526 Calvin 09-30 | C&W via #472 | Merged 15:53:04 | Holds |
| ZOM-552 Oliver 09-26 | Redeem, left, premium sent | daeea991ce, ba194fd16b; `SeasonPass_redeem` in code | Holds |
| ZOM-534 Douglas 09-25 | Sync shipped in client builds | 47c65623e7 "sync quests end with client", tags iOS 36, Android 119. Oliver did the commit; Douglas is assignee | Holds |
| ZOM-534 Leonard 09-30 | Good on store build | He reported it 09-08; iOS 0.3.49 released 09-29 21:55; "my quest points are reset" 09-11 | Holds |
| ZOM-432 Calvin 09-24 | Frame still needed | Nothing contradicts | Single source |
| ZOM-432 Samuel 09-30, Done | Frame in #471; iOS 50, Android 135 | 41a0d814ed and `img - DailyGift.png` in #471; tags on 3f5352a5b5; builds done 19:15 and 20:13 | Holds |
| ZOM-78 Frederick 09-30 | Use this ticket | Title "Event Calendar For Zombie Match 3D"; he is free after 18:09 | Holds |
| ZOM-465 Marcus 09-26 | Icons animated | #454, #456, #458 merged by 09-24 | Holds |
| ZOM-465 Marcus 09-30 | C&W icon not animated | No C&W entry under `Assets/Animations/mainMenu/icons` | Holds; DR2 |
| ZOM-344 Marcus 09-16, Done | Box animation done | No backing commit found | DR4 |
| ZOM-442 Oliver 09-19 | Params present | `ZombieLaneCellBase.cs` lines 226 to 227 | Holds |
| ZOM-471 Samuel 09-17 | Leonard said no; Start button | Thread 08-13: Leonard "we don't need it"; Vincent "already has start button" | Holds; "Parking it" while Todo is harmless |
| ZOM-504 Vincent 09-22 | Bot-only | His DM 09-03 14:33 "couldn't repro without bots" | Holds |
| ZOM-517 Robert 09-18 | Enrage held | He reported it; nothing contradicts | Single source |
| ZOM-521 Calvin 09-26 | Last two items | ZOM-528 and 541 In Progress | Holds |
| ZOM-521 Calvin 09-30 | #475 card animation | Merged 16:09:14; 90e10bc821; Brian "I'll test it tomorrow" | Holds; DR2 |
| ZOM-542 Samuel 09-22 | Layout refresh, not needed | Robert's ask is real; status mismatch | DR1 |
| ZOM-544 Vincent 09-29 | Sign-in works, no restore | His 09-25 14:52 stored-data list | Holds |
| ZOM-546 Owen 09-24 | Refill holds | He is assignee; nothing contradicts | Single source |
| ZOM-549 Vincent 09-26 | Endless fields in; left_level lacks one | `AnalyticsManager.cs` lines 508 to 510; none in `left_level` | Holds |
| ZOM-566 Brian 09-30 | Not a blocker | Vincent 16:47 "none of them blockers"; Brian 16:50 "Analytics and name changes first" | Holds |
| ZOM-566 Owen 09-30, In Progress | Two events, wiring now | 16:29 "only see two events"; 17:13 asks about analytics manager; 22:08 still adding | Holds |
| ZOM-563 Vincent 09-30, Done | Works on prod | Douglas 18:16; Vincent 21:58 "Yep it works as expected" | Holds |
| Trello Leonard 09-29 | Oct 13 rollover; weekly reset | Monday correct; `quests-stack.ts` `weekDay: 'MON'`; card is his; list name matches action stream | Holds |

## Checks that found nothing

- Every author was active near their record, and all posted in channels they belong to.
- No injected comment contradicts its author's own nearby base message. Vincent's "squeeze in" at 16:24 and "rides the next build" at 21:46 fit, because the submission builds went out between them.
- ZOM-566 and the Sep 30 rename talk ("Energy Raid", Brian and Vincent, 15:21 to 15:24) are consistent: the injected comment defers the text, and no record shows a new name shipped.
