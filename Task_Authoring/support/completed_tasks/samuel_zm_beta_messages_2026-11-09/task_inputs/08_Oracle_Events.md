OE 1  Read Leonard's DM from yesterday in Slack (Samuel's DM with Leonard Hayes, his message of Tue Sep 30 2025)
Expected: Leonard, Tue Sep 30 2025 1:40 PM PT: "The PN sheet says six are Ready and I don't trust that." "Take every row on the PNs Beta tab plus every ask for a new phone message that's been filed on a ticket or a card up to today, and make a call on each one using the message rule doc." "Put it in one sheet in your Drive folder, one row per message: Message, Ticket, Call, What's missing, Audience, Final headline, String change." "Next to it a one-page note for the team: start with D1 and D7 for the Sep 15 cohort week from the warehouse, iOS and Android separately, then the lapsed reminders the client schedules day by day, and anything the client already schedules that's still a Hold and why." "I made tickets for the sheet rows under DES-314 and people added their asks there." "Leave the call as a comment on each ticket and move the ticket to match." "Anything with no ticket gets one, but don't make a second one for something that already has a ticket under whatever name." "Every Go goes on a checklist on our push notifications card so Vincent can tick it off." "Email each person who asked for something, apart from me, to say what happened to their asks." "When it's done tell me here how many Go, Hold and Drop."

OE 2  Read the message rule doc in Drive/Docs (search "rule"; doc "Beta message rule")
Expected: Leonard's doc, last changed Fri Sep 26 2025 10:10 AM PT. "A message is anything the game puts on a player's phone while the game is closed." "Run these tests in order and stop at the first one that fails." "1. The feature behind it is in the beta." "2. The client can send it without a server." "3. The client already schedules it." "4. It can reach the players it is written for. A player only counts once our own permission ask has happened, the settings toggle doesn't count. It fails only if none of them count." "5. It fires on the right day. The hour doesn't matter for beta, the day does." "6. Vincent has seen it arrive on both iOS and Android." "Go: it passes all six. Drop: it fails test 1, or the client already covers it under another message, then name that message. Hold: anything else, and name the test it failed." "In the beta means live in Zombie Match today or on the BETA list of the ZM ROADMAP board." "Neither status column on the sheet decides anything." "What Vincent counts as seen is in his QA note. The permission ask is Robert's call." "The final headline is the latest line I've called." "A line that differs from what the client ships needs a string ticket under DES-314, because the strings are hard-coded, so open one when you make the call." "Emoji don't count as a different line. Final headline and String change are only for Go rows. Audience is who the ask says it's for." "Drop tickets go to Canceled, Go tickets stay as they are, Hold tickets go back to Todo unless the roadmap says otherwise."

OE 3  Read the PNs Beta tab of the Zombie Match PN sheet in Sheets (search "Push Notifications"; sheet "Push Notifications Zombie Match", tab "PNs Beta", second tab)
Expected: Last changed Mon Jun 23 2025 12:02 AM PT. 14 rows, shown here as row, Details, Status, Headline: 1 "Revisit once new quests roll out.", Not Ready, "New Quests Await! 🌟"; 2 "When Hourly Coins are ready to be collected", Not Ready, "Your Hourly Coins Are Ready! ⏰💰"; 3 "When lives are recharged", Ready, "Full Ammo Reloaded! 🔫"; 4 "Has not played in 24 hours", Ready, "The Horde Is Growing… 🧟‍♂️"; 5 "Has not played in seven days.", Ready, "They’ve Taken Over… Can You Stop Them? 😱"; 6 "Finish first tutorial", Ready, "Finish Your First Mission! 🎯"; 7 "Win & Collect event start", Not Ready, "Win Big, Collect More! 🎁"; 8 "Nathan’s Treasure Hunt event start", Not Ready, "Treasure Hunt Begins! 🗺️💎"; 9 "Plague Race", Ready, "Plague Race Is On! 🌊🚣"; 10 "Streak Fever event start", Not Ready, "Keep the Streak Alive! 🔥"; 11 "Axe Arena event start", Not Ready, "Enter the Axe Arena! ⚔️"; 12 "Login Calendar update", Not Ready, "New Rewards Await! 🎉"; 13 "Season Pass activation or reward unlock", Not Ready, "Season Pass Is Live! 🎟️✨"; 14 "Weekly Leaderboard reset", Ready, "Weekly Rankings Reset! 🧟‍♀️📈". Six say Ready. Row 6 Segmentation: "Level 20 not completed and it's been 12 hours since first session".

OE 4  List the children of DES-314 in Linear (parent DES-314, from OE 1)
Expected: 31 tickets. 13 for sheet rows: DES-315 Lives recharged; DES-316 Lapsed 1 day; DES-317 Lapsed 7 days; DES-318 Finish first mission; DES-319 Plague Race; DES-320 Weekly Leaderboard reset; DES-321 Quests rollover; DES-322 Login Calendar update; DES-323 Season Pass start or reward; DES-324 Hourly Coins; DES-325 Nathan's Treasure Hunt start; DES-326 Streak Fever start; DES-327 Axe Arena start. 18 asks, with who filed each: DES-328 Endless entries are back (Brian Foster); DES-329 Endless weekly result (Brian Foster); DES-330 Boss Arena is open (Robert); DES-331 Boss Arena last hours (Robert); DES-332 Season Pass last 48 hours (Oliver Brooks); DES-333 Season Pass premium nudge (Brian Foster); DES-334 Plague Race last hour (Julia Lawson); DES-335 Plague Race result (Julia Lawson); DES-336 Zombie Lane reward ready (Owen Baker); DES-337 Achievement reward waiting (Owen Baker); DES-338 Daily chest ready (Calvin Price); DES-339 Free shop coins ready (Martin Walsh); DES-340 Support reply waiting (Owen Baker); DES-341 New levels added (Julia Lawson); DES-342 Lapsed 3 days (Leonard Hayes); DES-343 Lapsed 30 days (Leonard Hayes); DES-344 Lapsed 14 days (Robert); DES-345 Comeback gift on tap (Brian Foster). States: DES-315, DES-316, DES-317, DES-318, DES-319, DES-320 Done; the rest In Review. Descriptions: DES-315 to DES-320 each end "Built in match3d #248."; DES-321 "Quests are already in production."; DES-322 "Daily login is already in the game."; DES-339 "We already give free coins in the shop.".

OE 5  Read the comments on each of those 31 tickets in Linear (one call per ticket, list from OE 4)
Expected: Who it's for, then Arthur's note where there is one. DES-315: "Who it's for: everyone. Rollover on the sheet is wrong for this one, it goes when lives are full" "arrived on both on store builds, Android 0.3.127 and iOS 0.3.40". DES-316: "Who it's for: everyone who has stopped" "arrived on both on store builds, Android 0.3.127 and iOS 0.3.40". DES-317: "Who it's for: everyone who has stopped" "arrived on both on store builds, Android 0.3.127 and iOS 0.3.40". DES-318: "Who it's for: new players below level 20" "arrives on both when notifications are switched on from settings". DES-319: "Who it's for: players past the race unlock" "arrived on both on store builds, Android 0.3.127 and iOS 0.3.40" "Daily is fine for this one, there's always a race on.". DES-320: "Who it's for: players past the leaderboard unlock" "arrived on both on store builds, Android 0.3.127 and iOS 0.3.40". DES-321: "Who it's for: everyone" "not in NotificationManager yet. client knows the rollover time, local timer is enough". DES-322: "Who it's for: everyone" "nothing for this in NotificationManager. it's just the daily reset, local timer works". DES-323: "Who it's for: players past the pass unlock" "not scheduled anywhere yet. client has the season dates so a local timer can do it". DES-324: "Who it's for: everyone" "not in NotificationManager". DES-325: "Who it's for: everyone" "nothing in NotificationManager for this". DES-326: "Who it's for: everyone" "nothing in NotificationManager for this one either". DES-327: "Who it's for: everyone" "not in NotificationManager". DES-328: "for players who used all their entries" "not in NotificationManager yet. entries come back on a timer so local works". DES-329: "for players who ranked that week" "not in NotificationManager. this needs a server send, the phone doesn't know the final standings". DES-330: "players past the arena unlock" "not scheduled yet. client has the board times, local timer can do it". DES-331: "players who started the arena" "not in NotificationManager yet, local timer off the end time". DES-332: "who it's for: players with unclaimed tiers" "not in NotificationManager yet. client has the end date, local timer". DES-333: "for free-track players near a premium reward" "not in NotificationManager. needs a server send, it's picked per player from server data". DES-334: "this is for players in a race" "not in NotificationManager yet. race end is known, local timer is fine". DES-335: "this is for players in a race" "needs a server send, the final placing only exists on the server". DES-336: "for players with a reward to claim" "not in NotificationManager yet. client knows what's unclaimed when the game closes, local timer can do it". DES-337: "for players with a reward to claim" "same as the lane one, not scheduled, local timer is enough". DES-338: "for everyone" "not in NotificationManager yet. the chest timer is local". DES-339: "it's for everyone" "not scheduled yet, local timer is enough". DES-340: "for players with an open support thread" "needs a server send, the reply comes from Helpshift". DES-341: "this is for players past the hand-made levels" "needs a server send, nothing on the phone knows we shipped levels". DES-342: "Who it's for: everyone who has stopped" "not in NotificationManager yet. local timer, same as the other lapsed ones". DES-343: "Who it's for: everyone who has stopped" "not in NotificationManager yet. local timer can do it". DES-344: "everyone who has stopped". DES-345: "for everyone who has stopped" "A reward on tap is a version 2 idea, it isn't in the beta.". On DES-319 and DES-345 the last comment is Leonard's. On DES-315 to DES-320 the second comment is Vincent's, from Wed Sep 24 2025.

OE 6  Find the live-ops page in Confluence (search "Live-Ops"; page "Live-Ops Event Calendar & Planning")
Expected: Among the event rows, game then status: Plague Race, Zombie Match 3D, "Live; algo bug Aug 2025". Zombie Lane, Zombie Match 3D, Live. Endless Monster Mode, Zombie Match 3D, "Live; also one of the three permanent board modes". Weekly Leaderboards, Domino Delights / Zombie Match 3D, Live. Nathan's Treasure Hunt, Axe Arena and Streak Fever are on Domino Delights. Collect & Win, Zombie Match 3D: "Built for the end-of-September beta submission (QA blockers cleared 26 Sep 2025); not yet live." It is the same feature as Win & Collect, "under a different name".

OE 7  Find the Collect & Win ticket in Linear (query "Collect")
Expected: DES-313 "Ping when a Collect & Win window opens", filed by Calvin Price, created Wed Sep 17 2025 8:20 AM PT, state In Review, no parent. "Three windows a week." This is the ticket for the Win & Collect row (OE 6).

OE 8  Read the comments on DES-313 in Linear (ticket from OE 7)
Expected: "for players on the event" "not in NotificationManager yet. windows are fixed so a local timer can do it"

OE 9  List the Linear tickets updated since the day DES-314 opened, to find asks filed outside its children (updatedAt 2025-09-23, limit 100, or orderBy updatedAt on team Zombie Match 3D)
Expected: Besides DES-313, DES-314 and its 31 children, 20 tickets, all Zombie Match 3D: ZOM-112, ZOM-465, ZOM-483, ZOM-498, ZOM-536, ZOM-538, ZOM-541, ZOM-542, ZOM-543, ZOM-551, ZOM-553, ZOM-555, ZOM-556, ZOM-557, ZOM-558, ZOM-561, ZOM-563, ZOM-564, ZOM-565, ZOM-566.

OE 10  Read the comments on ZOM-542 in Linear (list from OE 9)
Expected: Ticket "Update home screen and victory score screen for game modes". Brian Foster, Fri Sep 26 2025 6:27 AM PT: "while someone's in here, can we get a phone reminder once the daily Boss Arena attempts refill? separate from the weekly board ping Robert filed, this is for players who used their attempts. Arthur says a local timer is enough." An ask for a new phone message with no ticket of its own; call it Boss Arena attempts refilled.

OE 11  Read the comments on ZOM-556 in Linear (list from OE 9)
Expected: Ticket "When the daily gift is skipped, it doesn't reset to 0.". Julia Lawson, Fri Sep 26 2025 7:08 AM PT: "the gift streak itself is live, this only breaks the skip case. could we also send a phone reminder the evening before the daily gift streak resets? separate from the chest ping Calvin filed, this is for players on a gift streak. local timer per Arthur." An ask for a new phone message with no ticket of its own; call it Daily gift about to reset.

OE 12  Read the comments on ZOM-563 in Linear (list from OE 9)
Expected: Ticket "Teams' lives, golden frames and names not working on prod env". Douglas, Tue Sep 30 2025 11:22 AM PT: "prod has the latest teams changes now. while I'm in here, could we get a phone message when a teammate sends you lives? for players on a team. it would have to go out from the server, the phone has no way of knowing." An ask for a new phone message with no ticket of its own; call it Teammate sent lives.

OE 13  Read the comments on ZOM-483 in Linear (list from OE 9)
Expected: Ticket "Infinite lives from new-install are not granted, rewards 30 min in the next session start.". Calvin Price, Fri Sep 26 2025 9:41 AM PT: "we do hand out infinite lives, just not on the first session. could we also remind players on their phone when their infinite lives are about to run out? not the lives recharged one, this is for players with infinite lives running. local timer per Arthur." An ask for a new phone message with no ticket of its own; call it Infinite lives ending.

OE 14  Read the comments on the other 16 tickets from OE 9 in Linear (one call per ticket)
Expected: Each returns an empty comment list.

OE 15  Search Linear for any other ticket about phone messages (queries "notification", "push", "remind")
Expected: "notification" hits in Zombie Match 3D, all permission, settings, red dot or analytics work: ZOM-314 "Adding new buttons to settings Panel", ZOM-320 "Notification pop up on android breaks the level 1 tutorial highlight.", ZOM-366 "Notification permission pops up twice after declining", ZOM-385 "Zombie Lane Polish", ZOM-387 "Giant Analytics Ticket". In Design: DES-9, a Backlog idea from 2023, and DES-283 "Implement Chapter Full Star Rewards". The other "notification" hits are older ENG and ART tickets. Besides those and the tickets from OEs 4 and 7, the "push" and "remind" hits are about other things, among them ZOM-295 "Refill health and push monster back should reset ALL enrage status." None asks for a new phone message for beta.

OE 16  List the ZM ROADMAP board's lists and their cards in Trello
Expected: Lists include "BETA: Oct 10", "Oct 21" and "Backlog". On BETA: Oct 10, among others: "Win and Collect", "Season Pass", "Infinite HP Boss Mode", "300 Levels Manmade", "Add more quests and balance quest rewards", "Shop Inventory Review and Additions", "Fix TECH ISSUES". On Oct 21, among others: "Axe Arena (Win streak multiplier scoring)". On Backlog, among others: "Hourly Collection".

OE 17  Tie Boss Arena to the BETA list in Linear (query "Boss Arena")
Expected: ZOM-487 "Infinite HP Boss Arena", Done: this is the BETA list's Infinite HP Boss Mode.

OE 18  Check that achievements and support have shipped in Linear (queries "Achievements" and "Helpshift")
Expected: ZOM-116 "Quest and Achievements UI", Done. ZOM-363 "Achievements are claimable twice even though they shouldn't", Done. ZOM-301 "Helpshift Implementation", Done.

OE 19  Read the card "Fix TECH ISSUES" on the BETA list in Trello (its description and last activity, from the board's lists)
Expected: Description: "Until the beta build is out nothing that isn't beta work lands in anyone's Todo. Held tickets sit in Backlog, unassigned." Last activity Mon Sep 29 2025 1:15 PM PT. This is later than the rule doc (OE 2), whose Todo clause gives way to what the roadmap says.

OE 20  Read the card comments on ZM ROADMAP in Trello (board actions, filter commentCard)
Expected: 13 comments: estimates and art notes from June and July, Leonard's note on the push notifications card, and "Samuel says 3 days.". None is an ask for a phone message.

OE 21  Search Trello for cards about phone messages (searches "notification" and "reminder", cards_filter all)
Expected: On ZM ROADMAP the one hit is "[Feature] Push Notifications - Samuel + Leonard". The other six are on the boards "DD Product Roadmap" and "Harmony Games", last active by May 2025: "Expand notifications", "local Push Notification", "Appointment Mechanic v1 Basic", "Make mini-games accessible via saga map nodes", "Push-notification boost", "(Blake/Samuel) Hooking up Notifications to One Signal (1 week)". The search for "reminder" returns no cards. None asks for a new phone message for beta.

OE 22  Find the push notifications card on ZM ROADMAP in Trello (search "Push Notifications")
Expected: Card "[Feature] Push Notifications - Samuel + Leonard", id 6851a769c65dc0017a227bb7, on the Jun 30th list. Leonard's comment, Wed Sep 24 2025 9:00 AM PT: "The beta list goes on this card as a checklist. Vincent ticks these as he checks them on the store builds."

OE 23  Read the client's notification code in GitHub (repo match3d, main, path Assets/Scripts/Notifications/NotificationManager.cs)
Expected: The scheduling method makes six calls, for lives recharged, the first tutorial, the one-day reminder, the weekly batch, the weekly leaderboard batch and Plague Race. "DailyNotifications(OneDayLapsedTitle, OneDayLapsedMessage, serverToday);" "BatchScheduleWeeklyNotifications(WeeklyReminderTitle, WeeklyReminderMessage, 4, serverToday);" "BatchScheduleWeeklyLeaderboardNotifications(WeeklyLeaderboardTitle, WeeklyLeaderboardMessage, 4, serverToday);" "BatchSchedulePlagueRace(PlagueRaceTitle, PlagueRaceMessage, 5, serverToday);" "DateTime date = serverToday.AddDays(1);" "DateTime fireTime = referenceDate.AddDays(i * 7);" So the lapsed reminders go on day 1, then days 7, 14, 21 and 28 after the last session, and the weekly leaderboard one counts the same way. Titles include "The Horde Is Growing… 🧟‍♂️" "They’ve Taken Over… Can You Stop Them? 😱" "Full Ammo Reloaded! 🔫" "Plague Race Is On! 🌊🚣".

OE 24  Read the review comments on PR #248 in GitHub (repo match3d, PR number from OE 4), or the same comment in Samuel's Gmail (search "PR #248")
Expected: Arthur Blake, Thu Jun 26 2025 1:58 PM PT: "This counts seven days from the day they last left the game, so it isn't tied to the rollover. Fine to merge, but it isn't a reset message until it's anchored to the real reset." On GitHub the comment sits on the fireTime line of BatchScheduleWeeklyLeaderboardNotifications.

OE 25  Read Vincent's QA note in Gmail (search "Phone messages for beta")
Expected: Vincent Parker, Mon Sep 15 2025 6:05 AM PT: "Seen only counts on a store build, on a real iOS device and a real Android device." "A build with shortened timers doesn't count, it only proves the code path." "Moving the phone date forward on a store build is fine." "Passes go in the Phone message checks sheet."

OE 26  Read Vincent's checks log in Sheets (search "Phone message checks"; tab "Beta")
Expected: Six rows, each with Android 0.3.127, iOS 0.3.40, Checked Sep 24: Lives recharged; Lapsed 1 day ("phone date moved forward"); Lapsed 7 days ("phone date moved forward"); Finish first mission ("notifications switched on from settings"); Plague Race; Weekly Leaderboard reset ("phone date moved forward").

OE 27  Find Vincent Parker's Slack user (search users "Vincent")
Expected: Vincent Parker, user id EMPLOYEE_0012_SLACK_ID.

OE 28  Search Slack for what Vincent Parker has posted since Sep 1 (query from the user id in OE 27) for his Sep 30 post in #zombie-match3d
Expected: Tue Sep 30 2025 8:12 AM PT: "on 0.3.49 the Full Ammo one didn't show up after a full refill, tried it twice on the iPhone this morning. the lapsed ones are still coming through. taking my tick off Full Ammo until I've seen it land" Full Ammo Reloaded! is the Lives recharged headline, so his tick on Lives recharged is off. It is later than the Sep 24 pass.

OE 29  Read Vincent's Sep 29 reply in Samuel's DM with him in Slack (in the results of OE 28)
Expected: Mon Sep 29 2025 12:40 PM PT: "also on the race one I passed: that iPhone was still on the 5-minute timers build when I ticked it, so scratch iOS. put the real 0.3.40 on it after and it never showed up. Android is fine." The race one is Plague Race, so its iOS pass is withdrawn. It is later than the Sep 24 pass.

OE 30  Search Slack for Robert's permission ask call (search "permission ask")
Expected: Robert in #zombie-match3d, Mon Sep 29 2025 10:40 AM PT: "Permission ask for beta: leaving our own ask after level 20, not pushing it further, Leonard's right that we need PNs for retention. The Unity popup at launch on iOS stays as it is."

OE 31  Read the replies under Robert's post in Slack (thread from OE 30)
Expected: Arthur Blake, Mon Sep 29 2025 11:21 AM PT: "that popup doesn't switch anything on btw. NotificationManager only schedules once our own ask has run or they switch it on from settings, on both platforms"

OE 32  Search Slack for Leonard's change to the seven-day line (search "taken over")
Expected: Leonard in #zombie-art, Mon Sep 29 2025 11:05 AM PT: "random one while I'm here: the 'taken over' push reads like we've given up. make it "Your Squad Needs You Back", body stays."

OE 33  Search Samuel's Google Calendar for the lapsed copy check (search "Lapsed"; event "Lapsed copy check")
Expected: Event by Leonard, created Mon Sep 29 2025 3:14 PM PT, updated Tue Sep 30 2025 10:02 AM PT. Description: "Went through the lapsed lines with Martin Walsh after this. Final for the 7 day one is "Your Squad Is Waiting", body stays. That replaces what I said in the art thread."

OE 34  Read the cancelled ladder review in Gmail (search "lapsed"; subject "Canceled event with note: Lapsed ladder review")
Expected: Leonard, Thu Sep 25 2025 8:00 AM PT: "Cancelled, no need. The weekly one repeats for four weeks, so day 14 is already covered."

OE 35  Search Slack for the Axe Arena decision (search "Axe Arena"; #company-internal)
Expected: Brian Foster, Mon Sep 22 2025 9:22 AM PT: "We’ve decided to postpone Axe Arena for the beta release."

OE 36  Read the retention table's columns in Snowflake (describe ANALYTICS.GAME_EVENTS.USER_COHORT_RETENTION)
Expected: Column d1_ret: "% returning on Day 1". Column d7_ret: "NULL until the 7-day window closes".

OE 37  Query D1 and D7 for the Sep 15 cohort week in Snowflake (ANALYTICS.GAME_EVENTS.USER_COHORT_RETENTION, game_id zombie_match_3d, cohort_week 2025-09-15)
Expected: Two rows. ios: installs 237, d1_ret 31.65, d7_ret 9.28. android: installs 103, d1_ret 37.86, d7_ret 10.68.

OE 38  Find Samuel's Drive folder in Drive (list the root)
Expected: Folder "samuel.turner@harmonygames.co", id d_caafeec2804b3a67ce46aa, owner samuel.turner@harmonygames.co.

OE 39  Look up each asker in Contacts (names from OEs 4, 7, 10, 11, 12, 13)
Expected: Brian Foster: brian.foster@harmonygames.co; Calvin Price: calvin.price@harmonygames.co; Douglas: douglas@harmonygames.co; Julia Lawson: julia.lawson@harmonygames.co; Martin Walsh: martin.walsh@harmonygames.co; Oliver Brooks: oliver.brooks@harmonygames.co; Owen Baker: owen.baker@harmonygames.co; Robert: robert@harmonygames.co.

OE 40  Apply test 1 to all 36 messages: 14 sheet rows, 18 asks under DES-314 and 4 comment asks (the Docs rule from OE 2, with Linear in OEs 4, 5, 11, 12, 13, 17, 18, Trello in OE 16, Confluence in OE 6, GitHub in OE 23, Slack in OE 35)
Expected: Five fail, so Drop: Hourly Coins (Hourly Collection is on the Backlog list); Nathan's Treasure Hunt and Streak Fever (live-ops page: Domino Delights); Axe Arena (Oct 21 list, postponed for the beta); Comeback gift (Leonard on DES-345: "A reward on tap is a version 2 idea, it isn't in the beta."). The other 31 pass. In the client: Lives recharged, Finish first mission, Lapsed 1 day, Lapsed 7 days. The same lapsed feature: Lapsed 3 days, Lapsed 14 days, Lapsed 30 days. Live on the live-ops page: Plague Race and its two asks, Zombie Lane, both Endless asks, Weekly Leaderboard reset. On the BETA list: Win & Collect, Season Pass and its two asks, the three Boss Arena messages, New levels added. Live by their ticket text: Quests rollover, Login Calendar update, Free shop coins ready. Shipped: Achievement reward waiting, Support reply waiting. Live by their own comments: Daily chest ready (Arthur: "the chest timer is local"), Daily gift about to reset ("the gift streak itself is live"), Teammate sent lives ("prod has the latest teams changes now"), Infinite lives ending ("we do hand out infinite lives").

OE 41  Apply test 2 to the 31 left (Arthur's Linear notes in OE 5, Douglas's Linear comment in OE 12)
Expected: Six need a server send, so Hold, test 2: Endless weekly result (DES-329); Season Pass premium nudge (DES-333); Plague Race result (DES-335); Support reply waiting (DES-340); New levels added (DES-341); Teammate sent lives.

OE 42  Apply test 3 to the 25 left (the six GitHub scheduling calls in OE 23, Arthur's Linear notes in OE 5, the Linear comment asks, and the Gmail note in OE 34)
Expected: The client schedules six: Lives recharged, Finish first mission, Lapsed 1 day, Lapsed 7 days, Weekly Leaderboard reset, Plague Race. Lapsed 14 days is covered by Lapsed 7 days, because the weekly batch fires on day 14, so Drop, naming Lapsed 7 days. The other 18 are not scheduled, so Hold, test 3: Win & Collect start (DES-313); Quests rollover (DES-321); Login Calendar update (DES-322); Season Pass start (DES-323); Endless entries back (DES-328); Boss Arena open (DES-330); Boss Arena last hours (DES-331); Season Pass last 48 hours (DES-332); Plague Race last hour (DES-334); Zombie Lane reward ready (DES-336); Achievement reward waiting (DES-337); Daily chest ready (DES-338); Free shop coins ready (DES-339); Lapsed 3 days (DES-342); Lapsed 30 days (DES-343); Boss Arena attempts refilled; Daily gift about to reset; Infinite lives ending.

OE 43  Apply test 4 to the six the client schedules (Slack in OEs 30 and 31, Linear in OE 5, Sheets in OE 3)
Expected: Finish first mission fails, so Hold, test 4: it is written for new players below level 20 (DES-318, and the sheet's "Level 20 not completed"), our own ask runs after level 20, and the settings toggle doesn't count, so none of its players count. The other five reach players who have had our ask.

OE 44  Apply test 5 to the five left (GitHub in OEs 23 and 24, Linear in OE 5)
Expected: Weekly Leaderboard reset fails, so Hold, test 5: it counts from the last session, not the weekly reset, so it fires on the wrong day. Plague Race passes (Leonard on DES-319: "Daily is fine for this one, there's always a race on."), and so do Lives recharged, Lapsed 1 day and Lapsed 7 days.

OE 45  Apply test 6 to the four left (Gmail in OE 25, Sheets in OE 26, Slack in OEs 28 and 29)
Expected: Lives recharged and Plague Race fail, so Hold, test 6, not seen on both platforms. Lapsed 1 day and Lapsed 7 days pass: both were seen on store builds with the phone date moved forward, and Vincent says "the lapsed ones are still coming through".

OE 46  Settle the Go rows' headlines (GitHub in OE 23, Slack in OE 32, Calendar in OE 33)
Expected: Lapsed 1 day: Final headline "The Horde Is Growing…", String change No. Lapsed 7 days: Final headline "Your Squad Is Waiting" (the latest line, replacing "Your Squad Needs You Back"), String change Yes, because the client ships "They’ve Taken Over… Can You Stop Them? 😱".

OE 47  Count the calls across the Sheets rows and Linear tickets (OEs 40 to 45)
Expected: 36 messages: Go 2, Hold 28, Drop 6.

OE 48  Create the string ticket in Linear (team Design, parent DES-314)
Expected: A new ticket under DES-314 carrying the line "Your Squad Is Waiting" for Lapsed 7 days.

OE 49  Create the ticket for Boss Arena attempts refilled in Linear (team Design, parent DES-314, state Backlog, no assignee)
Expected: A new ticket for Boss Arena attempts refilled, for players who used their attempts, naming the ask on ZOM-542.

OE 50  Comment the call on the new Boss Arena attempts refilled ticket in Linear
Expected: A comment saying Hold, test 3: the client doesn't schedule it yet.

OE 51  Create the ticket for Daily gift about to reset in Linear (team Design, parent DES-314, state Backlog, no assignee)
Expected: A new ticket for Daily gift about to reset, for players on a gift streak, naming the ask on ZOM-556.

OE 52  Comment the call on the new Daily gift about to reset ticket in Linear
Expected: A comment saying Hold, test 3: the client doesn't schedule it yet.

OE 53  Create the ticket for Teammate sent lives in Linear (team Design, parent DES-314, state Backlog, no assignee)
Expected: A new ticket for Teammate sent lives, for players on a team, naming the ask on ZOM-563.

OE 54  Comment the call on the new Teammate sent lives ticket in Linear
Expected: A comment saying Hold, test 2: it needs a server send.

OE 55  Create the ticket for Infinite lives ending in Linear (team Design, parent DES-314, state Backlog, no assignee)
Expected: A new ticket for Infinite lives ending, for players with infinite lives running, naming the ask on ZOM-483.

OE 56  Comment the call on the new Infinite lives ending ticket in Linear
Expected: A comment saying Hold, test 3: the client doesn't schedule it yet.

OE 57  Create the calls sheet in Sheets
Expected: A new native spreadsheet with a name about the beta messages.

OE 58  Write the rows to the calls sheet in Sheets (calls from OEs 40 to 46)
Expected: Header Message, Ticket, Call, What's missing, Audience, Final headline, String change, then 36 rows, one per message. Message uses the sheet's or the ticket's name, or an obvious short form. Ticket holds the row's ticket: DES-313 for Win & Collect start, the new keys for the four comment asks. What's missing names the failed test on Hold rows, names Lapsed 7 days on Lapsed 14 days, is blank or a short reason on the other Drop rows, and is blank on the Go rows. Audience comes from each ask (OEs 5, 8, 10 to 13). Final headline and String change are filled on the two Go rows only.

OE 59  Move the calls sheet into Samuel's Drive folder in Drive (folder from OE 38)
Expected: The sheet's parent is d_caafeec2804b3a67ce46aa.

OE 60  Create the one-page team note in Docs
Expected: A Doc that opens with D1 and D7 for the Sep 15 cohort week: iOS D1 31.65%, D7 9.28%; Android D1 37.86%, D7 10.68%. Then the lapsed reminders the client schedules by day: day 1, then days 7, 14, 21 and 28. Then the Holds the client already schedules and why: Lives recharged and Plague Race (not seen on both platforms), Finish first mission (can't reach its players), Weekly Leaderboard reset (fires on the wrong day).

OE 61  Move the note into Samuel's Drive folder in Drive (folder from OE 38)
Expected: The Doc's parent is d_caafeec2804b3a67ce46aa.

OE 62  Create a checklist on the push notifications card in Trello (card from OE 22)
Expected: A new checklist on card 6851a769c65dc0017a227bb7.

OE 63  Add Lapsed 1 day to the checklist in Trello (OE 62)
Expected: A check item naming Lapsed 1 day.

OE 64  Add Lapsed 7 days to the checklist in Trello (OE 62)
Expected: A check item naming Lapsed 7 days.

OE 65  Comment the call on DES-313 in Linear
Expected: A comment on DES-313 (Win & Collect start) saying Hold, test 3: the client doesn't schedule it yet.

OE 66  Comment the call on DES-315 in Linear
Expected: A comment on DES-315 (Lives recharged) saying Hold, test 6: Vincent's tick is off after 0.3.49.

OE 67  Comment the call on DES-316 in Linear
Expected: A comment on DES-316 (Lapsed 1 day) saying Go.

OE 68  Comment the call on DES-317 in Linear
Expected: A comment on DES-317 (Lapsed 7 days) saying Go, with the final headline "Your Squad Is Waiting" and the string ticket.

OE 69  Comment the call on DES-318 in Linear
Expected: A comment on DES-318 (Finish first mission) saying Hold, test 4: it can't reach its players.

OE 70  Comment the call on DES-319 in Linear
Expected: A comment on DES-319 (Plague Race) saying Hold, test 6: the iOS pass was on the 5-minute timers build.

OE 71  Comment the call on DES-320 in Linear
Expected: A comment on DES-320 (Weekly Leaderboard reset) saying Hold, test 5: it fires on the wrong day.

OE 72  Comment the call on DES-321 in Linear
Expected: A comment on DES-321 (Quests rollover) saying Hold, test 3: the client doesn't schedule it yet.

OE 73  Comment the call on DES-322 in Linear
Expected: A comment on DES-322 (Login Calendar update) saying Hold, test 3: the client doesn't schedule it yet.

OE 74  Comment the call on DES-323 in Linear
Expected: A comment on DES-323 (Season Pass start) saying Hold, test 3: the client doesn't schedule it yet.

OE 75  Comment the call on DES-324 in Linear
Expected: A comment on DES-324 (Hourly Coins) saying Drop, test 1: it isn't in the beta.

OE 76  Comment the call on DES-325 in Linear
Expected: A comment on DES-325 (Nathan's Treasure Hunt) saying Drop, test 1: it isn't in the beta.

OE 77  Comment the call on DES-326 in Linear
Expected: A comment on DES-326 (Streak Fever) saying Drop, test 1: it isn't in the beta.

OE 78  Comment the call on DES-327 in Linear
Expected: A comment on DES-327 (Axe Arena) saying Drop, test 1: it isn't in the beta.

OE 79  Comment the call on DES-328 in Linear
Expected: A comment on DES-328 (Endless entries back) saying Hold, test 3: the client doesn't schedule it yet.

OE 80  Comment the call on DES-329 in Linear
Expected: A comment on DES-329 (Endless weekly result) saying Hold, test 2: it needs a server send.

OE 81  Comment the call on DES-330 in Linear
Expected: A comment on DES-330 (Boss Arena open) saying Hold, test 3: the client doesn't schedule it yet.

OE 82  Comment the call on DES-331 in Linear
Expected: A comment on DES-331 (Boss Arena last hours) saying Hold, test 3: the client doesn't schedule it yet.

OE 83  Comment the call on DES-332 in Linear
Expected: A comment on DES-332 (Season Pass last 48 hours) saying Hold, test 3: the client doesn't schedule it yet.

OE 84  Comment the call on DES-333 in Linear
Expected: A comment on DES-333 (Season Pass premium nudge) saying Hold, test 2: it needs a server send.

OE 85  Comment the call on DES-334 in Linear
Expected: A comment on DES-334 (Plague Race last hour) saying Hold, test 3: the client doesn't schedule it yet.

OE 86  Comment the call on DES-335 in Linear
Expected: A comment on DES-335 (Plague Race result) saying Hold, test 2: it needs a server send.

OE 87  Comment the call on DES-336 in Linear
Expected: A comment on DES-336 (Zombie Lane reward ready) saying Hold, test 3: the client doesn't schedule it yet.

OE 88  Comment the call on DES-337 in Linear
Expected: A comment on DES-337 (Achievement reward waiting) saying Hold, test 3: the client doesn't schedule it yet.

OE 89  Comment the call on DES-338 in Linear
Expected: A comment on DES-338 (Daily chest ready) saying Hold, test 3: the client doesn't schedule it yet.

OE 90  Comment the call on DES-339 in Linear
Expected: A comment on DES-339 (Free shop coins ready) saying Hold, test 3: the client doesn't schedule it yet.

OE 91  Comment the call on DES-340 in Linear
Expected: A comment on DES-340 (Support reply waiting) saying Hold, test 2: it needs a server send.

OE 92  Comment the call on DES-341 in Linear
Expected: A comment on DES-341 (New levels added) saying Hold, test 2: it needs a server send.

OE 93  Comment the call on DES-342 in Linear
Expected: A comment on DES-342 (Lapsed 3 days) saying Hold, test 3: the client doesn't schedule it yet.

OE 94  Comment the call on DES-343 in Linear
Expected: A comment on DES-343 (Lapsed 30 days) saying Hold, test 3: the client doesn't schedule it yet.

OE 95  Comment the call on DES-344 in Linear
Expected: A comment on DES-344 (Lapsed 14 days) saying Drop: Lapsed 7 days already covers it.

OE 96  Comment the call on DES-345 in Linear
Expected: A comment on DES-345 (Comeback gift) saying Drop, test 1: it isn't in the beta.

OE 97  Move DES-313 to Backlog with no assignee in Linear (OE 19)
Expected: DES-313 state Backlog, assignee empty.

OE 98  Move DES-315 to Backlog with no assignee in Linear (OE 19)
Expected: DES-315 state Backlog, assignee empty.

OE 99  Move DES-318 to Backlog with no assignee in Linear (OE 19)
Expected: DES-318 state Backlog, assignee empty.

OE 100  Move DES-319 to Backlog with no assignee in Linear (OE 19)
Expected: DES-319 state Backlog, assignee empty.

OE 101  Move DES-320 to Backlog with no assignee in Linear (OE 19)
Expected: DES-320 state Backlog, assignee empty.

OE 102  Move DES-321 to Backlog with no assignee in Linear (OE 19)
Expected: DES-321 state Backlog, assignee empty.

OE 103  Move DES-322 to Backlog with no assignee in Linear (OE 19)
Expected: DES-322 state Backlog, assignee empty.

OE 104  Move DES-323 to Backlog with no assignee in Linear (OE 19)
Expected: DES-323 state Backlog, assignee empty.

OE 105  Move DES-324 to Canceled in Linear
Expected: DES-324 state Canceled.

OE 106  Move DES-325 to Canceled in Linear
Expected: DES-325 state Canceled.

OE 107  Move DES-326 to Canceled in Linear
Expected: DES-326 state Canceled.

OE 108  Move DES-327 to Canceled in Linear
Expected: DES-327 state Canceled.

OE 109  Move DES-328 to Backlog with no assignee in Linear (OE 19)
Expected: DES-328 state Backlog, assignee empty.

OE 110  Move DES-329 to Backlog with no assignee in Linear (OE 19)
Expected: DES-329 state Backlog, assignee empty.

OE 111  Move DES-330 to Backlog with no assignee in Linear (OE 19)
Expected: DES-330 state Backlog, assignee empty.

OE 112  Move DES-331 to Backlog with no assignee in Linear (OE 19)
Expected: DES-331 state Backlog, assignee empty.

OE 113  Move DES-332 to Backlog with no assignee in Linear (OE 19)
Expected: DES-332 state Backlog, assignee empty.

OE 114  Move DES-333 to Backlog with no assignee in Linear (OE 19)
Expected: DES-333 state Backlog, assignee empty.

OE 115  Move DES-334 to Backlog with no assignee in Linear (OE 19)
Expected: DES-334 state Backlog, assignee empty.

OE 116  Move DES-335 to Backlog with no assignee in Linear (OE 19)
Expected: DES-335 state Backlog, assignee empty.

OE 117  Move DES-336 to Backlog with no assignee in Linear (OE 19)
Expected: DES-336 state Backlog, assignee empty.

OE 118  Move DES-337 to Backlog with no assignee in Linear (OE 19)
Expected: DES-337 state Backlog, assignee empty.

OE 119  Move DES-338 to Backlog with no assignee in Linear (OE 19)
Expected: DES-338 state Backlog, assignee empty.

OE 120  Move DES-339 to Backlog with no assignee in Linear (OE 19)
Expected: DES-339 state Backlog, assignee empty.

OE 121  Move DES-340 to Backlog with no assignee in Linear (OE 19)
Expected: DES-340 state Backlog, assignee empty.

OE 122  Move DES-341 to Backlog with no assignee in Linear (OE 19)
Expected: DES-341 state Backlog, assignee empty.

OE 123  Move DES-342 to Backlog with no assignee in Linear (OE 19)
Expected: DES-342 state Backlog, assignee empty.

OE 124  Move DES-343 to Backlog with no assignee in Linear (OE 19)
Expected: DES-343 state Backlog, assignee empty.

OE 125  Move DES-344 to Canceled in Linear
Expected: DES-344 state Canceled.

OE 126  Move DES-345 to Canceled in Linear
Expected: DES-345 state Canceled.

OE 127  Email Brian Foster in Gmail (address from OE 39)
Expected: A sent email to brian.foster@harmonygames.co saying what happened to their asks: Endless entries back: Hold; Endless weekly result: Hold; Season Pass premium nudge: Hold; Comeback gift: Drop; Boss Arena attempts refilled: Hold.

OE 128  Email Calvin Price in Gmail (address from OE 39)
Expected: A sent email to calvin.price@harmonygames.co saying what happened to their asks: Daily chest ready: Hold; Infinite lives ending: Hold; Win & Collect start: Hold.

OE 129  Email Douglas in Gmail (address from OE 39)
Expected: A sent email to douglas@harmonygames.co saying what happened to their asks: Teammate sent lives: Hold.

OE 130  Email Julia Lawson in Gmail (address from OE 39)
Expected: A sent email to julia.lawson@harmonygames.co saying what happened to their asks: Plague Race last hour: Hold; Plague Race result: Hold; New levels added: Hold; Daily gift about to reset: Hold.

OE 131  Email Martin Walsh in Gmail (address from OE 39)
Expected: A sent email to martin.walsh@harmonygames.co saying what happened to their asks: Free shop coins ready: Hold.

OE 132  Email Oliver Brooks in Gmail (address from OE 39)
Expected: A sent email to oliver.brooks@harmonygames.co saying what happened to their asks: Season Pass last 48 hours: Hold.

OE 133  Email Owen Baker in Gmail (address from OE 39)
Expected: A sent email to owen.baker@harmonygames.co saying what happened to their asks: Zombie Lane reward ready: Hold; Achievement reward waiting: Hold; Support reply waiting: Hold.

OE 134  Email Robert in Gmail (address from OE 39)
Expected: A sent email to robert@harmonygames.co saying what happened to their asks: Boss Arena open: Hold; Boss Arena last hours: Hold; Lapsed 14 days: Drop.

OE 135  Post the counts in Leonard's DM in Slack (the DM from OE 1, after every other write)
Expected: A message in that DM saying Go 2, Hold 28, Drop 6.
