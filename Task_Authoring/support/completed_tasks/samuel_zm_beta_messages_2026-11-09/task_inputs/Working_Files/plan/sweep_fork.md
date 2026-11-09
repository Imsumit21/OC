# Blind fork sweep: beta phone messages

Reviewer inputs: `01_Universe_Inject.sql` and the base universe through `hg.py search`. No author files were read. Clock: Oct 1, 2025 (synth-cut).

**Bottom line.** My reading gives 35 rows: Go 3, Hold 25, Drop 7. The Go count is not stable. Three unsettled forks each flip Go rows, so a careful reader can land on Go 0, 1, 2 or 3. All three can be fixed with a one-line change to an injected record.

Fork count: **3 High, 8 Medium, 12 Low.**

Severity:
- **High:** flips a Go row or the Go/Hold/Drop totals, and no dated record settles it.
- **Medium:** changes the row count, a required write, a graded column or the note, with no record to settle it.
- **Low:** no effect on the totals, or the records lean strongly one way, but rubric wording should still tolerate it.

## Record legend

| Short name | Record |
|---|---|
| RULE | gdocs `f_dc45e0e5a8b8635c1b82b2` (Beta message rule, Sep 26) |
| DM | slack `46cad8c0cdfa6806c71380a551781a19` (Leonard to Samuel, Sep 30) |
| QA | gmail `<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com>` (Vincent, Sep 15) |
| CHK | gsheets `f_8eb8c04713ff6a6ef4a265`, tab Beta |
| PERM | slack `5e163a235a6d9c1e6c3fc12bb26dfac5` (Robert, zombie-match3d, Sep 29) |
| LINE | slack `af1431994a864fec66ca83f08f73aa30` (Leonard, zombie-art thread, Sep 29) |
| RACE | slack `f2a3e88857f4c6a50274b3dfedbae6fb` (Vincent, DM thread, Sep 29) |
| WEEK | gcal `evt_b56d5b19baa0a573da4553` (cancel note, Sep 25) and its Gmail copy |
| RC18 | github `harmonygames-Games/match3d#248#rc_18` (body and diff_hunk) |
| CONST | github `/review_comments/609` (FirstTutorialFinished 20, LeaderboardsUnlockLevel 22, PlagueRaceUnlockLevel 25) |
| CAL | confluence `page_liveops_calendar` |
| TODO | trello action `68dae8c4d95e24b55b69bf80` (Leonard, Sep 29, on card Fix TECH ISSUES) |

## 1. My calls

Tab rows are 1 to 14, asks are 15 to 35. Headline and string columns are only meaningful for Go rows (see M6). "Emoji only" means the sheet and client differ only by emoji.

| # | Message | Ticket | Call | First failed test | Final headline | String change | Deciding records |
|---|---|---|---|---|---|---|---|
| 1 | Quests rollover | DES-321 | Hold | 3 | - | n/a, not in client | `cmt_7b184259cfbb33052325`, RC18 hunk |
| 2 | Hourly Coins | DES-324 | Drop | 1 | - | - | trello card `68c45bba5d2c25a3a5c26a8c` (Backlog since Sep 23), RULE status line, `page_economy_design` (hourly collection is Domino) |
| 3 | Lives recharged | DES-315 | **Go** | none | Full Ammo Reloaded! 🔫 | No | `cmt_51e018b23e18c2f680cd`, CHK, RC18 hunk |
| 4 | Lapsed 1 day | DES-316 | **Go** | none | The Horde Is Growing… 🧟‍♂️ | No | `cmt_5ab75e0ee96e70745960`, CHK, RC18 hunk |
| 5 | Lapsed 7 days | DES-317 | **Go** | none | Your Squad Needs You Back | **Yes** | LINE, `cmt_e4bb9fe925b86f52cf55`, CHK, RC18 hunk |
| 6 | Finish first mission | DES-318 | Hold | 4 | - | No, emoji only | `cmt_886fb8b04e3b6ba66b57`, `cmt_f4960d3c073493b6bfc6`, CHK, PERM |
| 7 | Win & Collect event start | DES-313 | Hold | 3 | - | n/a | CAL (same feature as Collect & Win), card `6851a7abf7876721472dba99`, `cmt_cb634ee40df2ae6c6022` |
| 8 | Nathan's Treasure Hunt | DES-325 | Drop | 1 | - | - | CAL (Domino only), no ZM card or ZOM ticket |
| 9 | Plague Race | DES-319 | Hold | 6 | - | No | RACE, `cmt_9338bb2c286a6c207792` (test 5 passes), CONST |
| 10 | Streak Fever | DES-326 | Drop | 1 | - | - | CAL (Domino only), no ZM card |
| 11 | Axe Arena | DES-327 | Drop | 1 | - | - | card `6851a7a6c31a93809acded72` (Oct 21), CAL |
| 12 | Login Calendar update | DES-322 | Hold | 3 | - | n/a | `cmt_5acbc1a3f111af34e7ac`, ZOM-299 |
| 13 | Season Pass start or reward | DES-323 | Hold | 3 | - | n/a | `cmt_181bcd11a979359893fb`, card `6851ab766fcaf894d0c0048b` |
| 14 | Weekly Leaderboard reset | DES-320 | Hold | 5 | - | No, emoji only | RC18, CONST, `cmt_f76672cf21387ec1eeab` |
| 15 | Endless entries are back | DES-328 | Hold | 3 | - | - | `cmt_c6f09d1660c6a174811f`, CAL |
| 16 | Endless weekly result | DES-329 | Hold | 2 | - | - | `cmt_9d5748e1540a9588ceb9` |
| 17 | Boss Arena is open | DES-330 | Hold | 3 | - | - | `cmt_e4ac33987005778b372e`, card `6851ab7090e82351a14e7837`, ZOM-487 |
| 18 | Boss Arena last hours | DES-331 | Hold | 3 | - | - | `cmt_e1c7ebcf5aa9ee4b4a8c` |
| 19 | Season Pass last 48 hours | DES-332 | Hold | 3 | - | - | `cmt_44a1117f30fbb476c28c` |
| 20 | Season Pass premium nudge | DES-333 | Hold | 2 | - | - | `cmt_ff7c43f0633261872ec7` |
| 21 | Plague Race last hour | DES-334 | Hold | 3 | - | - | `cmt_521d7e03d14d535f1d5b` |
| 22 | Plague Race result | DES-335 | Hold | 2 | - | - | `cmt_fda157bae8336585356a` |
| 23 | Zombie Lane reward ready | DES-336 | Hold | 3 | - | - | `cmt_b55d6a0b35ae5242ffd4`, CAL |
| 24 | Trophy Path reward waiting | DES-337 | Hold | 3 | - | - | `cmt_4feec391e19bb4a4a16a` (see M1) |
| 25 | Daily chest ready | DES-338 | Hold | 3 | - | - | `cmt_32da06fe646ada57c7fa` (see M2) |
| 26 | Free shop coins ready | DES-339 | Hold | 3 | - | - | `cmt_aa68a0b0ee32e8e24c58` |
| 27 | Support reply waiting | DES-340 | Hold | 2 | - | - | `cmt_31db977b4adf091259da` |
| 28 | New levels added | DES-341 | Hold | 2 | - | - | `cmt_96b8c0e10b3d2b20a982` |
| 29 | Lapsed 3 days | DES-342 | Hold | 3 | - | - | `cmt_af799d5941e425ad3e53`, RC18 hunk (DailyNotifications fires once) |
| 30 | Lapsed 30 days | DES-343 | Hold | 3 | - | - | `cmt_58672546fb6435495753`, RC18 hunk (4 weeks ends day 28) |
| 31 | Lapsed 14 days | DES-344 | Drop | covered by Lapsed 7 days | - | - | WEEK, RC18 hunk |
| 32 | Comeback gift on tap | DES-345 | Drop | 1 | - | - | `cmt_13477aa8d1468ae11c9d` |
| 33 | Rewarded ad ready | DES-346 | Drop | 1 | - | - | card `68af7645b20c96f21f108ad7` (moved off BETA to Oct 21 on Sep 23) |
| 34 | Boss Arena attempts refill | new ticket | Hold | 3 | - | - | `cmt_f1b8a109dfa70cdc4565` on ZOM-542 (see M3) |
| 35 | Daily gift, evening before reset | new ticket | Hold | 3 | - | - | `cmt_2b519285937e7fa79453` on ZOM-556 |

**Totals.** Go 3, Hold 25, Drop 7. Hold by failed test: test 2 has 5, test 3 has 17, test 4 has 1, test 5 has 1, test 6 has 1.

**Ticket states.** Go stays as it is (DES-315, 316, 317 stay Done). Drop goes to Canceled. Hold goes to Backlog, unassigned, under TODO.

**Asks with no ticket.** Rows 34 and 35 need new tickets. ZOM-542 and ZOM-556 themselves must not move.

**Askers to email.** Calvin (DES-313, 338), Brian (DES-328, 329, 333, 345, ZOM-542 comment), Robert (DES-330, 331, 344, 346), Oliver (DES-332), Julia (DES-334, 335, 341, ZOM-556 comment), Owen (DES-336, 337, 340), Martin (DES-339), and possibly Leonard (DES-342, 343; see M7).

## 2. Forks

### High

**H1. Test 4: does partial reach pass?** Rows 3, 4, 5 (all three Go rows).
- **Reading A (mine):** the test passes if the message can reach some of its audience. The Audience column then narrows it to past level 20.
- **Reading B:** these are written for "everyone" or "everyone who has stopped". Everyone below level 20 cannot be reached, and those are the early churners D1 is about. So it "can't reach the players it is written for". Hold, test 4. **Go becomes 0.**
- **Records:** RULE test 4 ("It can reach the players it is written for. A player only counts once the permission ask has happened"), `cmt_2395189dfd5e7d5c1e88`, `cmt_d6bf99cc8b3e926c2569`, `cmt_f64ebdf08bef6b136513`, PERM.
- **Why it's unsettled:** Finish first mission fails because none of its audience counts, but the rule never says "none" as opposed to "not all". The DM's "who actually hears from us" leans towards A without saying so.
- **Settle with:** add to RULE test 4: "It fails only if none of the players it's written for have had the ask. If some have, it passes and Audience says who."

**H2. Test 6: does "phone date moved forward" count as seen?** Rows 4, 5 (also 14, where it doesn't matter because test 5 fails first).
- **Reading A (mine):** yes. It's a store build on real devices, QA excludes only "a build with shortened timers", and Vincent's comments say "arrived on both on store builds".
- **Reading B:** moving the clock is the same shortcut as a shortened timer and also "only proves the code path". Hold, test 6. **Go becomes 1**, Lives recharged alone.
- **Records:** QA, CHK notes on Lapsed 1 day, Lapsed 7 days and Weekly Leaderboard reset, `cmt_5ab75e0ee96e70745960`, `cmt_e4bb9fe925b86f52cf55`.
- **Why it's unsettled:** the rule says Vincent's note defines "seen", and the note doesn't mention the phone clock. The Notes column looks like a flagged caveat, the same way "notifications switched on from settings" does on a row that fails.
- **Settle with:** one sentence in QA ("Moving the phone's date forward on a store build is fine, the build's schedule is real"), or drop the note from CHK if it isn't meant as a test.

**H3. Test 5: Lives recharged "Fires: Rollover".** Row 3.
- **Reading A (mine):** the Details cell ("When lives are recharged") defines it, and "Rollover" is loose sheet wording. Pass.
- **Reading B:** a solver checks each ticket's "Fires:" field against the client, which is how Weekly Leaderboard fails. The client fires at `DateTime.Now.AddSeconds(allLivesTimeRemaining)`, which isn't tied to any rollover. Same wording, same mismatch, same result. Hold, test 5. **Go becomes 2.**
- **Records:** DES-315 description, PNs Beta row 3 column When, RC18 hunk, RC18 body ("isn't tied to the rollover").
- **Why it's unsettled:** Leonard resolved exactly this mismatch for Plague Race (`cmt_9338bb2c286a6c207792`) but left it open here. That silence reads as meaningful.
- **Settle with:** edit the DES-315 description to "Fires: when lives are full", or add a Leonard comment like the one on DES-319.

### Medium

**M1. Zombie Lane and Trophy Path are one feature.** Rows 23, 24.
- **Reading A (mine):** different triggers (ready, sitting unclaimed), so two messages and two rows.
- **Reading B:** same feature, same asker, same "go claim your reward" ping. One message filed twice, so 34 rows and Hold 24. The rule has no outcome for a duplicate ask, so DES-337's state is undefined.
- **Records:** slack `54591cf3cf2250a4c49c4269c5108920` (Robert, Sep 17: "trophy path (AKA Zombie Lane)"), DES-336, DES-337, DM ("under whatever name"), ZOM-385.
- **Settle with:** add a line on DES-337 separating it from DES-336, or swap one ask for another feature.

**M2. Login Calendar and Daily chest are one feature.** Rows 12, 25.
- **Reading A (mine):** two rows, both Hold 3.
- **Reading B:** both are daily pings for the same daily gift system, so one message.
- **Records:** DES-322, DES-338, ZOM-299, match3d#317 ("Daily Gift system, including daily login rewards, chest rewards").
- **Settle with:** state on DES-338 how it differs from DES-322.

**M3. Does the ZOM-542 ask already have a ticket?** Rows 17, 34.
- **Reading A (mine):** different trigger and audience, so a new ticket.
- **Reading B:** DES-330 and ZOM-542 are linked as `relates`. Boss Arena is a permanent mode with daily entries, so "open" and "attempts refill" can only be the same daily reset. The DM forbids a second ticket "under whatever name". No new ticket, one row.
- **Records:** `cmt_f1b8a109dfa70cdc4565`, the DES-330 and ZOM-542 `relations_json`, slack zombie-ops `messages/C08R6BF4ENN/2025-09.json` item 0 (daily entries), CAL (Endless is "one of the three permanent board modes"), `page_zm3d_gdd` (Modes lists Campaign, Endless, Infinite-HP Boss).
- **Also:** the same pattern applies, more weakly, to ZOM-556 and DES-338. Rows 25 and 35 have different timing, so they should stay separate.
- **Settle with:** have Brian's comment say what's different, or give DES-330 a real window.

**M4. What goes in Audience?** All rows, especially 3, 4, 5.
- **Readings:** the ticket's "who it's for" verbatim; narrowed to past level 20; or narrowed further to past level 20 and accepted the ask.
- **Records:** RULE says a player counts once the ask "has happened", and says nothing about accepting. The DM asks who "actually hears". Sheet Segmentation disagrees with ticket comments on 7, 9, 14 (`cmt_7c6c022293a0505fbf85` says "players on the event", DES-313 says "same for everyone").
- **Settle with:** one line defining Audience, or a rubric that accepts both narrowed forms.

**M5. Is the string ticket created, and where?** Row 5.
- **Reading A:** RULE says the line "needs a string ticket", so create it.
- **Reading B:** the DM's "Anything with no ticket gets one" covers messages. DES-317 has one and "Go tickets stay as they are", so put Yes in the column and stop.
- **Also:** TODO says nothing new lands in Todo, and its Backlog line covers held work only. A string ticket is neither, so its state and owner are undefined.
- **Settle with:** add to RULE: "Open the string ticket in Backlog under DES-314."

**M6. Final headline and String change on non-Go rows.** All 32 non-Go rows.
- **Readings:** blank, or the sheet line. For messages not in the client, String change could be No, n/a, or Yes (the sheet line "differs from what the client ships"). The 21 asks have no headline at all.
- **Records:** DM column list, RULE final paragraph.
- **Settle with:** add to RULE: "Headline and String change only apply to Go rows."

**M7. Does Leonard get an email?** Rows 29, 30.
- **Reading A:** he filed DES-342 and DES-343, so he's a person who asked.
- **Reading B:** he's the requester and gets the reply on Slack, which the DM limits to counts.
- **Settle with:** say "everyone else who asked" in the DM, or don't grade him either way.

**M8. Scope of "who actually hears from us" and "day by day".** The note.
- **Reading A (mine):** Go lapsed ladder only: days 1, 7, 14, 21, 28.
- **Reading B:** a Hold is a call, not a code change. Plague Race (daily, days 1 to 5, level 25 and up) and Weekly Leaderboard (days 7 to 28, level 22 and up) are still in the client, so lapsed players still get them.
- **Records:** RC18 hunk, DM.
- **Settle with:** add to the DM: "the lapsed reminders from the Go list".

### Low

**L1. Lapsed 30 and day 28, row 30.** One could call day 28 the "last reminder", so Drop as covered. But "the day does" matter in RULE, and `cmt_58672546fb6435495753` says it's not in NotificationManager. Strong lean to Hold 3.

**L2. Hearsay on test 2, rows 34, 35.** "Arthur says a local timer is enough" and "local timer per Arthur" are second-hand, with no Arthur record. Hold 2 versus Hold 3 is arguable. An Arthur comment on each would settle it.

**L3. Where the "covered" check sits, row 31.** It isn't a numbered test, so a strict run gives Hold 6 or Hold 3. RULE's Drop clause and WEEK settle the call, but "first failed test" has no value here. The rubric should expect the named message.

**L4. Stale store build, rows 3, 4, 5.** Vincent's passes are on iOS 0.3.40, and 0.3.49 replaced it on Sep 29 (slack `c891232a8b395a701268cff14cffd883`, `page_season_pass_spec`). QA only requires a store build. The Sep 23 required-version bump to 0.3.40 (slack `dbb84b5845444b06aa5d652bb51420a4`) supports it being one, but no record says so outright.

**L5. Seen after a copy change, row 5.** The old headline is what Vincent saw. Go plus String change is the natural read.

**L6. "Until the beta build is out", TODO.** iOS 0.3.49 shipped under two hours after that comment, and CAL says "end-of-September beta submission". One could argue the Todo freeze has lapsed. The DM ("about to") and the list name "BETA: Oct 10" lean against that.

**L7. Population boundary.** "Every ask up to today" has no game or date limit. DES-9 is an open Backlog ticket in project "GoD - Beta", labelled Notifications. The Trello cards "Push-notification boost" (closed) and "local Push Notification" are Domino history. I excluded all of them. No asks exist on any ZM ROADMAP card, comment or checklist, so "or a card" is an empty branch, and the rubric must not require one.

**L8. Streak Fever versus win streak, row 10.** Collect & Win proved Domino events can have ZM aliases, and ZM does have a live win streak mechanic. But there is no ZM event, card or ticket, and CAL is Domino only. Drop 1 holds.

**L9. New levels, row 28.** Levels above 100 are generated, so nobody is ever "at the last level". A reader could fail test 1. Most land on Hold 2.

**L10. Client code date.** Tests 3 and 5 and the string check all rest on a Jun 26 diff hunk. Commits "Update Notification Manager" and its revert have no readable content or dates in the export. Nothing says the code is unchanged, and DES-315 to 320's "Built in match3d #248" is the only support.

**L11. Emoji on the new headline, row 5.** Leonard's line has no emoji and the client's has 😱. Harmless under "Emoji don't count", but rubric matching should ignore it.

**L12. Assignee on Drop and on new tickets.** TODO only unassigns held work. Whether Drop tickets keep Samuel, and whether rows 34 and 35 start unassigned, is inferred.

### Looked like forks, but a record settles them

- **Permission timing.** Base Slack conflicts: Vincent and Leonard on Sep 19 say iOS asks at app start (`272c3bf3bb5ac118c783b99cbe629724`, `2ffa97bfac3b7e217987e8ce4c5c9837`), and Robert on Sep 18 wants to punt it further (`822a509887ddd2bdd4724a6593f561fc`). PERM is later, comes from the owner RULE names, and speaks about the beta build.
- **Hold state.** RULE says Todo, TODO says Backlog, and RULE's own "unless the roadmap says otherwise" plus Leonard's authorship make TODO the winner.
- **Plague Race.** The ticket's iPhone pass loses to RACE, a later correction by the same person. Test 5 passes on `cmt_9338bb2c286a6c207792`.
- **Row and ticket mapping.** DES-313 is the Win & Collect ticket despite the DM's "ticket for each sheet row" (13 children for 14 rows). CAL states the alias.
- **Reach on rows 9 and 14.** CONST puts both unlocks above level 20, so test 4 passes.
- **Test order.** Arthur's "needs a server send" comments fail test 2, not 3. Row 6 fails test 4 before its test 6 problem.
- **Sheet status and the slide.** RULE's status line voids "Ready", "LIVE" and the slide's "6 Ready".
- **Reach of the records.** Samuel can open all of them: both DMs, zombie-match3d, zombie-art, ZOM and DES teams (DES by the injected membership), his folder `d_caafeec2804b3a67ce46aa`.

## 3. Records that state the conclusion

Nothing injected is addressed to a solver or grader. These read as answers rather than as workplace records:

| Severity | Record | Problem |
|---|---|---|
| High | Arthur's 24 comments (DES-313, DES-321 to 343), Sep 25 20:30 to 21:16 UTC, one every 2 minutes | A bulk answer column for tests 2 and 3, in four rotating phrasings, including on tickets that fail test 1. This is the most synthetic thing in the set. |
| High | "X is live." in 11 ticket descriptions (DES-321, 322, 328, 329, 334 to 340) | Answers test 1 in a fixed phrase. No ticket that fails test 1 carries it, so the phrase works as an answer key. |
| Medium | "Built in match3d #248." on exactly DES-315 to 320 | States test 3 for the six client rows. |
| Medium | WEEK: "The weekly one repeats for four weeks, so day 14 is already covered." | Near-verbatim Drop clause, and it predates the DES-344 ask by a day. |
| Medium | `cmt_13477aa8d1468ae11c9d`: "it isn't in the beta" | Uses test 1's exact wording. |
| Low | RC18 body: "it isn't a reset message until it's anchored to the real reset" | States the test 5 failure, though it reads like a natural review note. |
| Low | PERM: "Nothing asks before that in the beta build." | Worded to fit test 4. |
| Low | RACE | States the test 6 failure, but it's a plausible correction. |
| Low | RULE: "Neither status column...", "What Vincent counts as seen is in his QA note", "Emoji don't count..." | Each line maps to one trap. Acceptable in voice, but it's a routing table. |
| Low | DM: "under whatever name" | Pre-announces the DES-313 alias. |

Base records, not injected:
- CAL says outright "Same feature as Win & Collect on Domino Delights, under a different name" and "do not quote a duration".
- The warehouse table comment says "Do not synthesise a ZM3D DAU series".
- These read as addressed to an analyst. No action is possible from the SQL.

Lines 1 to 4 of the SQL are author notes in comments. They aren't records, but they shouldn't reach a solver.

**Fairness note, not a fork.** TODO sits on Fix TECH ISSUES, a card with no topical link to phone messages. RULE's "unless the roadmap says otherwise" gives no pointer to it, so every Hold state depends on opening an unrelated card.

## 4. Limits of this sweep

- **Warehouse not checked.** Searching and pointer reads on the 2.2 GB `snowflake.json` timed out, so I could not test the D1 and D7 read or any fork in it. Whether "Sep 15 cohort week" resolves to one value per platform is unverified.
- **Repo blobs not read,** as instructed. Client behaviour is from PR hunks only.
- **Slack coverage.** I read zombie-match3d and zombie-bugs for Jun to Sep, plus the Sep months of zombie-art and the Vincent DM. Other channels had keyword searches only, and several of those hit their match limits ("permission", "notification", "boss arena", "zombie lane"). A contrary message elsewhere is possible.
- **Linear comments.** The base export has no comments, so all comment evidence is injected.
- **Scratchpad.** Listing the shared scratchpad showed file names from earlier work. I didn't open them. My `pn.json` and `trello.json` were written to its root before I moved them into `fork/`. If files with those names already existed, they were overwritten.
