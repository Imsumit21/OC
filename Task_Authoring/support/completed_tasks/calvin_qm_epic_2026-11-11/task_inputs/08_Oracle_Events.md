OE 1  Read Brian's message from yesterday in Slack (Calvin's DM with Brian Foster, his message of Tue Sep 30 2025)
Expected: Brian, Tue Sep 30 2025 1:40 PM PT (Sep 30 20:40 UTC), message ts 1759264805.214409: "Before Thursday's flow review I want the queue manager to be a real epic." "I left a note on the ticket about how I want it." "One child for each area, and every report gets its line under the right child." "Please also put a stock-take sheet in your ZM queue manager folder and share it with everyone on the review invite, Leonard too, and add one slide with the numbers to your queue manager deck." "When it is done tell me here how many reports are passed, how many wait on QA, how many wait on a fix, how many areas are clear and how many reports are on the review list."

OE 2  Find the Queue Manager ticket in Linear and read its comments (the ticket named in the prompt; OE 1 says Brian left a note on it)
Expected: ZOM-543 "Queue Manager", team ZOM, state In Progress, no parent. Brian's comment, Tue Sep 30 2025 1:25 PM PT (Sep 30 20:25 UTC): "Children: Tutorials, Level-end rewards, Daily Gift, Season Pass, Collect & Win, Win Streak, Zombie Lane, Boss Arena, Endless Mode, Card packs. One child each, same team, no assignee." "Reports: the rows of Vincent's flow pass sheet, all of them." "so don't add new reports from his chats" "Plus any bug somebody else on the team saw in a build and told you about in a DM since Vincent started his pass on the 26th, about the home screen after a level." "If it is already a row, don't count it twice." "Passed: Vincent's ok or nr on a build that counts under Arthur's rule for QA passes, as long as that pass still stands under his rule." "Waiting on QA: not passed, and a fix for it is in main that QA has not tried on a main build yet." "Waiting on a fix: everything else." "if a ticket already has the report, move that ticket under the child and leave a note with the status and why." "If its state does not match the status, put Done for Passed, In Validation for Waiting on QA, Todo for Waiting on a fix." "If no ticket has it, make a sub-issue under the child with the report as the title and the state the same way." "No priority and no assignee on the new ones" "A child is Clear when all its reports are Passed, otherwise Open. Set the child to Done if it is Clear and to Todo if it is Open." "Review list: a report that is not Passed, in an area on the agenda of Thursday's review." "Sheet: tab Reports with Report, Area, Status, Ticket, Review list, Why. Tab Areas with Area, Status, Open reports. Slide: the five numbers I asked you for."

OE 3  Find and read Vincent's flow pass sheet in Drive (search "flow pass", named in OE 2; the sheet Vincent shared with Calvin, tab Flow pass)
Expected: Sheet "ZM home screen flow pass", owner vincent.parker@harmonygames.co, columns #, Area, What happens, Found on, Ticket, Fix, Re-test. 38 rows: [1] Tutorials | Back to back tutorials at level 16-17 only play the first one | found iOS Internal #1698 | ticket (blank) | fix #465 | re-test ok, chat. [2] Tutorials | Card upgrade tutorial never shows after the Zombie Lane one | found iOS Internal #1698 | ticket (blank) | fix #465 | re-test ok, chat. [3] Tutorials | Quest tutorial arrow points at the wrong tab after the last panel closes | found iOS Internal #1713 | ticket (blank) | fix (blank) | re-test nr iOS Internal #1745. [4] Tutorials | Win streak tutorial at level 20 freezes the home screen | found Android #1974 | ticket ZOM-567 | fix (blank) | re-test (blank). [5] Level-end rewards | Coin animation plays again after killing and reopening the app | found iOS Internal #1713 | ticket (blank) | fix #465 | re-test ok iOS Internal #1745. [6] Level-end rewards | Level-end coins fly while the pre-level panel is already open | found Android #1974 | ticket ZOM-568 | fix (blank) | re-test (blank). [7] Level-end rewards | Reward count-up is skipped when tapping fast on play | found iOS Internal #1727 | ticket (blank) | fix (blank) | re-test nr iOS Internal #1745. [8] Level-end rewards | Stars from the level fly to the wrong corner on tablets | found Android Submission #129 | ticket ZOM-569 | fix (blank) | re-test (blank). [9] Daily Gift | Season pass popup comes up on top of the daily gift when both are due | found iOS Internal #1727 | ticket (blank) | fix (blank) | re-test nr iOS Internal #1745. [10] Daily Gift | Daily gift calendar opens before the level-end coins finish | found Android #1984 | ticket ZOM-570 | fix (blank) | re-test again Android #2013. [11] Daily Gift | Daily gift day counter keeps going after a skipped day | found iOS Internal #1727 | ticket (blank) | fix (blank) | re-test (blank). [12] Season Pass | Season pass icon animation restarts every time a panel closes | found Android #1984 | ticket ZOM-571 | fix #472 | re-test (blank). [13] Season Pass | Season pass start popup shows again after every level until it is claimed | found iOS Internal #1727 | ticket ZOM-572 | fix (blank) | re-test (blank). [14] Season Pass | Season pass reward claim animation plays twice when coming back from the shop | found iOS Internal #1745 | ticket ZOM-573 | fix (blank) | re-test (blank). [15] Collect & Win | Event bar starts filling while the daily gift popup is still open | found Android #2013 | ticket ZOM-574 | fix #472 | re-test (blank). [16] Endless Mode | Endless unlock banner shows again after coming back from a level | found Android #2006 | ticket ZOM-575 | fix (blank) | re-test (blank). [17] Collect & Win | Reward animation waits too long before the event bar fills | found iOS Internal #1750 | ticket ZOM-585 | fix #472 | re-test ok iOS Internal #1757. [18] Collect & Win | Event panel opens over the level-end rewards on first unlock | found Android #2010 | ticket ZOM-576 | fix #472 | re-test again Android #2013. [19] Collect & Win | Event progress popup opens before the level-end coins finish | found Android #2013 | ticket ZOM-577 | fix (blank) | re-test (blank). [20] Win Streak | Win streak freezer from the abandoned pack never shows up on the home screen | found Android #1984 | ticket (blank) | fix (blank) | re-test (blank). [21] Win Streak | Streak counter jumps by two after a win when other panels are waiting | found iOS Internal #1745 | ticket ZOM-578 | fix (blank) | re-test (blank). [22] Zombie Lane | Zombie Lane reward animation plays under the home buttons | found iOS Internal #1727 | ticket (blank) | fix (blank) | re-test nr Android #2006. [23] Zombie Lane | Zombie Lane panel opens twice after claiming | found Android #1984 | ticket (blank) | fix (blank) | re-test ok Android #2006. [24] Zombie Lane | Lane progress bar animates from zero every time | found iOS Internal #1750 | ticket ZOM-586 | fix (blank) | re-test nr iOS Internal #1757. [25] Boss Arena | Boss arena tutorial does not play when another tutorial is queued before it | found iOS Internal #1713 | ticket (blank) | fix #465 | re-test ok, chat. [26] Boss Arena | Boss arena unlock popup shows behind the level-end rewards | found Android #1984 | ticket (blank) | fix (blank) | re-test nr Android #2006. [27] Boss Arena | Arena entry button can be tapped during the reward animation | found iOS Internal #1727 | ticket (blank) | fix (blank) | re-test nr iOS Internal #1745. [28] Endless Mode | Endless unlock banner overlaps the daily gift | found Android #1984 | ticket ZOM-579 | fix (blank) | re-test (blank). [29] Endless Mode | Coming back from Endless replays the home intro animation | found iOS Internal #1745 | ticket (blank) | fix (blank) | re-test ok iOS Internal #1750. [30] Endless Mode | Endless reward chest opens before the coins land | found Android #2006 | ticket ZOM-580 | fix (blank) | re-test (blank). [31] Card packs | Tap to collect prompt is missing when a pack opens after a level | found iOS Internal #1746 | ticket (blank) | fix #475 | re-test ok iOS Internal #1757. [32] Card packs | Pack opening sound keeps playing on the home screen after the pack closes | found iOS Internal #1746 | ticket ZOM-581 | fix #475 | re-test (blank). [33] Card packs | Last pack does not show its cards before closing | found iOS Internal #1746 | ticket (blank) | fix #475 | re-test ok iOS Internal #1757. [34] Card packs | Pack count on the home button only updates after a restart | found Android #2006 | ticket ZOM-582 | fix #475 | re-test again iOS Internal #1757. [35] Tutorials | Tutorial hand stays on screen after the last panel closes | found iOS Internal #1727 | ticket (blank) | fix (blank) | re-test nr iOS Internal #1745. [36] Level-end rewards | Level-end rewards do not show at all right after an app update | found Android Submission #129 | ticket ZOM-583 | fix (blank) | re-test (blank). [37] Win Streak | Win streak freezer popup opens behind the season pass popup | found iOS Internal #1745 | ticket ZOM-584 | fix (blank) | re-test (blank). [38] Season Pass | Pass progress bar fills before the tokens arrive | found Android #1984 | ticket (blank) | fix (blank) | re-test (blank). Note under the table: "The codes are in my pass sheet legend doc."

OE 4  Find and read the legend of Vincent's pass sheets in Drive (the note in OE 3 names it; list the Drive folder that holds the flow pass sheet)
Expected: Doc "How to read my pass sheets": "Fix: the PR the dev told me it went into. Blank if nobody told me." "Re-test: ok and a build means it is fine on that build." "nr and a build means I could not make it happen on that build." "again and a build means it still happens." "ok, chat means I told the dev ok in our chat, the build is there." "Blank means not re-tested yet."

OE 5  Find and read Arthur's rule for QA passes in Drive (search "QA passes", the rule OE 2 names; Arthur Blake's doc shared with Calvin)
Expected: Doc "ZM builds and QA passes": "For ZM a QA pass only counts on a build of the main branch." "A build of a feature branch is for the dev to check their own work, so a pass there has to be done again once the branch is merged." "A pass stands until somebody sees the bug again on a main build made after the one it passed on. Then it is open again, whoever saw it." "Which branch a build came from is in its #builds post."

OE 6  Read Calvin's DM with Vincent Parker in Slack around Sep 25 2025 for the ok behind the three "ok, chat" rows (rows 1, 2 and 25 in OE 3; OE 4 says the build is in the chat)
Expected: Calvin, Thu Sep 25 2025 9:29 AM PT (Sep 25 16:29 UTC): "Match 3D iOS Internal - #1718 already tested" Vincent, Thu Sep 25 2025 10:15 AM PT (Sep 25 17:15 UTC): "Looks ok to me" and, Thu Sep 25 2025 10:15 AM PT (Sep 25 17:15 UTC): "Boss arena as well"

OE 7  Read the 20 tickets in the sheet's Ticket column in Linear, each with its comments (ZOM-567 to ZOM-586, OE 3)
Expected: State as found: ZOM-567 Todo; ZOM-568 Todo; ZOM-569 Todo; ZOM-570 Todo; ZOM-571 In Validation; ZOM-572 Todo; ZOM-573 Todo; ZOM-574 In Validation; ZOM-575 Todo; ZOM-576 In Validation; ZOM-577 Todo; ZOM-578 Todo; ZOM-579 Todo; ZOM-580 Todo; ZOM-581 In Validation; ZOM-582 Todo; ZOM-583 Todo; ZOM-584 Todo; ZOM-585 In Validation; ZOM-586 Todo. Later notes: on ZOM-585, Samuel Turner, Tue Sep 30 2025 2:52 PM PT (Sep 30 21:52 UTC): "Got this again on Android Submission 135, so #472 did not sort it." On ZOM-586, Owen Baker, Tue Sep 30 2025 3:07 PM PT (Sep 30 22:07 UTC): "Android Submission 135: the lane bar starts from zero again every time I open home." On ZOM-576, Vincent: "I was told #472 has this. My last try was Android 2013, still there." On ZOM-582, Vincent: "I was told #475 has this. Still the same on iOS Internal 1757." On ZOM-577, Owen Baker, Tue Sep 30 2025 11:26 AM PT (Sep 30 18:26 UTC): "I have a fix locally, need to test it before I open the PR" That fix is not in main.

OE 8  Read the #builds history in Slack from Sep 24 to Sep 30 2025 and pick out the post of every build the sheet names (OE 3), of #1718, the build Calvin names just before Vincent's ok (OE 6), and of Android Submission 135, the build the ticket notes name (OE 7); OE 5 says the branch is in the build's post
Expected: Fifteen result posts (the Success post of each build, which carries the branch), oldest first: "Match 3D iOS Internal - #1698 - [PERSON_NAME_0029]/QueueManager" posted Wed Sep 24 2025 11:07 AM PT (Sep 24 18:07 UTC); "Match3D Android - #1974 - main" posted Wed Sep 24 2025 4:13 PM PT (Sep 24 23:13 UTC); "Match 3D iOS Internal - #1713 - main" posted Thu Sep 25 2025 4:27 AM PT (Sep 25 11:27 UTC); "Match 3D iOS Internal - #1718 - [PERSON_NAME_0029]/QueueManager" posted Thu Sep 25 2025 9:25 AM PT (Sep 25 16:25 UTC); "Match 3D iOS Internal - #1727 - main" posted Thu Sep 25 2025 3:21 PM PT (Sep 25 22:21 UTC); "Match3D Android - #1984 - main" posted Thu Sep 25 2025 3:21 PM PT (Sep 25 22:21 UTC); "Match3D Android Submission - #129 - main" posted Thu Sep 25 2025 7:39 PM PT (Sep 26 02:39 UTC); "Match3D Android - #2006 - main" posted Mon Sep 29 2025 8:39 AM PT (Sep 29 15:39 UTC); "Match 3D iOS Internal - #1745 - main" posted Mon Sep 29 2025 9:19 AM PT (Sep 29 16:19 UTC); "Match 3D iOS Internal - #1746 - [PERSON_NAME_0029]/AnimatedIcons" posted Mon Sep 29 2025 12:24 PM PT (Sep 29 19:24 UTC); "Match3D Android - #2010 - main" posted Mon Sep 29 2025 12:26 PM PT (Sep 29 19:26 UTC); "Match3D Android - #2013 - main" posted Mon Sep 29 2025 4:34 PM PT (Sep 29 23:34 UTC); "Match 3D iOS Internal - #1750 - main" posted Mon Sep 29 2025 6:55 PM PT (Sep 30 01:55 UTC); "Match 3D iOS Internal - #1757 - main" posted Tue Sep 30 2025 11:43 AM PT (Sep 30 18:43 UTC); "Match3D Android Submission - #135 - main" posted Tue Sep 30 2025 1:13 PM PT (Sep 30 20:13 UTC). Twelve are builds of main. iOS Internal #1698, #1718 and #1746 are builds of feature branches, so the ok on #1718 (rows 1, 2 and 25) does not count. Android Submission #135 is a main build posted after iOS Internal #1745, #1750 and #1757.

OE 9  Read pull requests #465, #472 and #475 of match3d in GitHub (the PRs in the sheet's Fix column, OE 3)
Expected: #465 "[PERSON_NAME_0029]/queue manager", base main, merged Thu Sep 25 2025 3:15 PM PT (Sep 25 22:15 UTC); #472 "Implement Win&Collect into Queue Manager", base main, merged Tue Sep 30 2025 8:53 AM PT (Sep 30 15:53 UTC); #475 "[PERSON_NAME_0029]/animated icons", base main, merged Tue Sep 30 2025 9:09 AM PT (Sep 30 16:09 UTC). The description of #472 starts: "Implement Win&Collect into Queue Manager (this also holds the pre-level panel until the level-end coins have landed)" That is row 6's bug.

OE 10  Read the review comments on pull request #472 in GitHub (OE 9; the same text is in the #zombie-prs thread under the PR's post and in Calvin's GitHub mail)
Expected: Login EMPLOYEE_0025_GITHUB_USERNAME (Arthur Blake in the GitHub user record), Tue Sep 30 2025 8:53 AM PT (Sep 30 15:53 UTC): "Flow sheet has the season pass icon restart and the event bar starting under the gift popup against this PR. Neither is in this diff. The other two Collect & Win ones are. Those two need their own PR." Rows 12 and 15 are not fixed by #472; rows 17 and 18 are in it.

OE 11  Read the review comments on pull request #475 in GitHub (OE 9; the same text is in the #zombie-prs thread under the PR's post and in Calvin's GitHub mail)
Expected: Login EMPLOYEE_0025_GITHUB_USERNAME (Arthur Blake), Tue Sep 30 2025 9:09 AM PT (Sep 30 16:09 UTC): "Don't see the pack sound stop anywhere in here. Still needs doing." Row 32 is not fixed by #475.

OE 12  List the match3d pull requests merged since Vincent started his sheet (created Fri Sep 26 2025 3:12 AM PT, 10:12 UTC, OE 3) and read the conversation of each one the sheet does not name (OE 2: a fix that is in main)
Expected: Eight merged pull requests are not on the sheet: #466 (merged Sep 26 15:14 UTC), #467 (Sep 26 18:58 UTC), #468 (Sep 29 16:13 UTC), #469 (Sep 30 01:50 UTC), #470 (Sep 30 15:51 UTC), #471 (Sep 30 15:52 UTC), #473 (Sep 30 15:41 UTC) and #474 (Sep 30 15:48 UTC). #463 merged Sep 25 5:08 PM PT (Sep 26 00:08 UTC), before the sheet was started, and is not one of them. One of them speaks about the flow list: #473 "Addressables/sp", base main, merged Tue Sep 30 2025 8:41 AM PT (Sep 30 15:41 UTC). The comment on it by login EMPLOYEE_0003_GITHUB_USERNAME (Oliver Brooks in the GitHub user record), Tue Sep 30 2025 8:42 AM PT (Sep 30 15:42 UTC): "For the flow list, this also has four fixes: the pass start popup coming back after every level, the pass bar filling before the tokens land, the claim animation playing twice after the shop, and the freezer popup opening behind the pass popup." Those are rows 13, 38, 14 and 37.

OE 13  Search the ZM tickets in Linear, by each row's wording, for a ticket that already holds a row whose Ticket cell is blank in OE 3 (rows 1, 2, 3, 5, 7, 9, 11, 20, 22, 23, 25, 26, 27, 29, 31, 33, 35, 38), and read the comments of the candidates
Expected: ZOM-556 "When the daily gift is skipped, it doesn't reset to 0.", state Todo; Vincent's comment, Tue Sep 30 2025 11:05 AM PT (Sep 30 18:05 UTC): "Saw this one myself in my home screen pass on 1727, the day counter keeps going after a skipped day. Same thing." ZOM-560 "The abandoned pack win streak freezer reward is not granted.", state Todo; Vincent's comment, Tue Sep 30 2025 11:08 AM PT (Sep 30 18:08 UTC): "Still there on Android 1984 in my home screen pass, the freezer from the abandoned pack never shows up on home." Row 11 is held by ZOM-556 and row 20 by ZOM-560. The searches return no ticket for the other sixteen rows.

OE 14  Search Slack for other sightings on Android Submission 135, the build Samuel and Owen name in OE 7 (search "Submission 135"), and open the threads of the hits
Expected: In #zombie-bugs, Vincent Parker's reply under his thread of Mon Sep 15 2025, Tue Sep 30 2025 2:20 PM PT (Sep 30 21:20 UTC): "from Android Submission 135 today: with a gift and a new pass stage both due after a level, the pass popup came up on top of the gift again" That is row 9. Robert's reply under his thread of Tue Sep 9 2025 PT (Sep 10 UTC), Tue Sep 30 2025 2:44 PM PT (Sep 30 21:44 UTC): "Played Android Submission 135 for an hour." "coming back from endless the home intro animation played again every single time" That is row 29.

OE 15  Search Slack for other sightings of the ten rows that still read as passed, by each row's wording in OE 3 (rows 3, 5, 7, 22, 23, 26, 27, 31, 33, 35; for row 27 search "arena entry button")
Expected: In #zombie-match3d, Robert, Mon Sep 29 2025 3:40 PM PT (Sep 29 22:40 UTC): "Android 2006: I could tap the arena entry button while the reward animation was playing, and it went through" That is row 27. Android #2006 was posted before iOS Internal #1745 (OE 8), the build row 27 passed on, so that pass stands. The searches return no later sighting for the other nine rows.

OE 16  Read Calvin's other DMs in Slack since Sep 26 2025 for a bug somebody told him about (OE 2's rule; the DM with Marcus Bennett)
Expected: Marcus Bennett, Tue Sep 30 2025 10:10 AM PT (Sep 30 17:10 UTC): "yo on today's main build the pass icon glow stays on after i claimed everything" and, in his next message, "saw it 3 levels in a row. its not the vfx, the animation itself is fine, its just the glow" No sheet row has it and a search of the ZM tickets for "icon glow" (as in OE 13) returns no ticket; it is a 39th report, in Season Pass. Calvin's four other DMs with messages since Sep 26 (Brian, Vincent, Owen Baker and one more colleague) carry no other bug seen in a build; Owen's Sep 29 remark that everything looks a little slower is about Calvin's video, not a build.

OE 17  Find the review invite in Gmail (search "flow review", the review named in the prompt and OE 1)
Expected: From leonard.hayes@harmonygames.co, Tue Sep 30 2025 10:24 AM PT (Sep 30 17:24 UTC), subject starts "Updated invitation with note: ZM home screen flow review @ Thu Oct 2, 2025" Note: "Moved up a day. Agenda is on the roadmap card, I changed it, daily gift waits until next week." The Sep 29 invitation for Fri Oct 3 ("Collect & Win and Daily Gift this time") is the earlier version.

OE 18  Read the review event on Calvin's calendar (search "flow review", OE 17)
Expected: "ZM home screen flow review", starts Thu Oct 2 2025 11:00 AM PT (18:00 UTC). Attendees besides Calvin: arthur.blake@harmonygames.co, brian.foster@harmonygames.co, julia.lawson@harmonygames.co, leonard.hayes@harmonygames.co, vincent.parker@harmonygames.co.

OE 19  Find the review's card on the ZM ROADMAP board in Trello and read its history (search "flow review"; OE 17 says the agenda is on the roadmap card)
Expected: Card "ZM home screen flow review - Thu Oct 2", description: "Walk through what is still not passed in: Collect & Win, Level-end rewards." Leonard Hayes changed the name and description on Tue Sep 30 2025 10:22 AM PT (Sep 30 17:22 UTC); the earlier description listed Collect & Win, Daily Gift.

OE 20  Find Calvin's ZM queue manager folder and deck in Drive (search "ZM queue manager", named in the prompt)
Expected: Folder "ZM queue manager", owner calvin.price@harmonygames.co. In it, the presentation "ZM queue manager", owner calvin.price@harmonygames.co.

OE 21  Work out each report's status, ticket and review-list flag from the note's rules (OE 2) and the records in OE 3 to OE 19
Expected: 39 reports (38 rows plus Marcus's, numbered 39). [1] Waiting on QA, new. [2] Waiting on QA, new. [3] Passed, new. [4] Waiting on a fix, ZOM-567. [5] Passed, new. [6] Waiting on QA, ZOM-568, review list. [7] Passed, new. [8] Waiting on a fix, ZOM-569, review list. [9] Waiting on a fix, new. [10] Waiting on a fix, ZOM-570. [11] Waiting on a fix, ZOM-556. [12] Waiting on a fix, ZOM-571. [13] Waiting on QA, ZOM-572. [14] Waiting on QA, ZOM-573. [15] Waiting on a fix, ZOM-574, review list. [16] Waiting on a fix, ZOM-575. [17] Waiting on a fix, ZOM-585, review list. [18] Waiting on QA, ZOM-576, review list. [19] Waiting on a fix, ZOM-577, review list. [20] Waiting on a fix, ZOM-560. [21] Waiting on a fix, ZOM-578. [22] Passed, new. [23] Passed, new. [24] Waiting on a fix, ZOM-586. [25] Waiting on QA, new. [26] Passed, new. [27] Passed, new. [28] Waiting on a fix, ZOM-579. [29] Waiting on a fix, new. [30] Waiting on a fix, ZOM-580. [31] Passed, new. [32] Waiting on a fix, ZOM-581. [33] Passed, new. [34] Waiting on a fix, ZOM-582. [35] Passed, new. [36] Waiting on a fix, ZOM-583, review list. [37] Waiting on QA, ZOM-584. [38] Waiting on QA, new. [39] Waiting on a fix, new. Totals: 10 Passed, 9 Waiting on QA, 20 Waiting on a fix. Areas, open of total: Tutorials 3 of 5, Level-end rewards 3 of 5, Daily Gift 3 of 3, Season Pass 5 of 5, Collect & Win 4 of 4, Win Streak 3 of 3, Zombie Lane 1 of 3, Boss Arena 1 of 3, Endless Mode 4 of 4, Card packs 2 of 4. Every area is Open, so 0 areas are Clear. Review list (not Passed, in Collect & Win or Level-end rewards, OE 19): 7 reports, rows 6, 8, 15, 17, 18, 19, 36.

OE 22  Create the Tutorials child under the Queue Manager ticket in Linear (fields from OE 2)
Expected: A new ZOM issue titled "Tutorials", parent ZOM-543, state Todo, no assignee.

OE 23  Create the Level-end rewards child under the Queue Manager ticket in Linear (fields from OE 2)
Expected: A new ZOM issue titled "Level-end rewards", parent ZOM-543, state Todo, no assignee.

OE 24  Create the Daily Gift child under the Queue Manager ticket in Linear (fields from OE 2)
Expected: A new ZOM issue titled "Daily Gift", parent ZOM-543, state Todo, no assignee.

OE 25  Create the Season Pass child under the Queue Manager ticket in Linear (fields from OE 2)
Expected: A new ZOM issue titled "Season Pass", parent ZOM-543, state Todo, no assignee.

OE 26  Create the Collect & Win child under the Queue Manager ticket in Linear (fields from OE 2)
Expected: A new ZOM issue titled "Collect & Win", parent ZOM-543, state Todo, no assignee.

OE 27  Create the Win Streak child under the Queue Manager ticket in Linear (fields from OE 2)
Expected: A new ZOM issue titled "Win Streak", parent ZOM-543, state Todo, no assignee.

OE 28  Create the Zombie Lane child under the Queue Manager ticket in Linear (fields from OE 2)
Expected: A new ZOM issue titled "Zombie Lane", parent ZOM-543, state Todo, no assignee.

OE 29  Create the Boss Arena child under the Queue Manager ticket in Linear (fields from OE 2)
Expected: A new ZOM issue titled "Boss Arena", parent ZOM-543, state Todo, no assignee.

OE 30  Create the Endless Mode child under the Queue Manager ticket in Linear (fields from OE 2)
Expected: A new ZOM issue titled "Endless Mode", parent ZOM-543, state Todo, no assignee.

OE 31  Create the Card packs child under the Queue Manager ticket in Linear (fields from OE 2)
Expected: A new ZOM issue titled "Card packs", parent ZOM-543, state Todo, no assignee.

OE 32  Create the sub-issue for report 1 under the Tutorials child in Linear (OE 21)
Expected: A new ZOM issue titled "Back to back tutorials at level 16-17 only play the first one", parent the Tutorials child, state In Validation, no priority, no assignee.

OE 33  Create the sub-issue for report 2 under the Tutorials child in Linear (OE 21)
Expected: A new ZOM issue titled "Card upgrade tutorial never shows after the Zombie Lane one", parent the Tutorials child, state In Validation, no priority, no assignee.

OE 34  Create the sub-issue for report 3 under the Tutorials child in Linear (OE 21)
Expected: A new ZOM issue titled "Quest tutorial arrow points at the wrong tab after the last panel closes", parent the Tutorials child, state Done, no priority, no assignee.

OE 35  Create the sub-issue for report 5 under the Level-end rewards child in Linear (OE 21)
Expected: A new ZOM issue titled "Coin animation plays again after killing and reopening the app", parent the Level-end rewards child, state Done, no priority, no assignee.

OE 36  Create the sub-issue for report 7 under the Level-end rewards child in Linear (OE 21)
Expected: A new ZOM issue titled "Reward count-up is skipped when tapping fast on play", parent the Level-end rewards child, state Done, no priority, no assignee.

OE 37  Create the sub-issue for report 9 under the Daily Gift child in Linear (OE 21)
Expected: A new ZOM issue titled "Season pass popup comes up on top of the daily gift when both are due", parent the Daily Gift child, state Todo, no priority, no assignee.

OE 38  Create the sub-issue for report 22 under the Zombie Lane child in Linear (OE 21)
Expected: A new ZOM issue titled "Zombie Lane reward animation plays under the home buttons", parent the Zombie Lane child, state Done, no priority, no assignee.

OE 39  Create the sub-issue for report 23 under the Zombie Lane child in Linear (OE 21)
Expected: A new ZOM issue titled "Zombie Lane panel opens twice after claiming", parent the Zombie Lane child, state Done, no priority, no assignee.

OE 40  Create the sub-issue for report 25 under the Boss Arena child in Linear (OE 21)
Expected: A new ZOM issue titled "Boss arena tutorial does not play when another tutorial is queued before it", parent the Boss Arena child, state In Validation, no priority, no assignee.

OE 41  Create the sub-issue for report 26 under the Boss Arena child in Linear (OE 21)
Expected: A new ZOM issue titled "Boss arena unlock popup shows behind the level-end rewards", parent the Boss Arena child, state Done, no priority, no assignee.

OE 42  Create the sub-issue for report 27 under the Boss Arena child in Linear (OE 21)
Expected: A new ZOM issue titled "Arena entry button can be tapped during the reward animation", parent the Boss Arena child, state Done, no priority, no assignee.

OE 43  Create the sub-issue for report 29 under the Endless Mode child in Linear (OE 21)
Expected: A new ZOM issue titled "Coming back from Endless replays the home intro animation", parent the Endless Mode child, state Todo, no priority, no assignee.

OE 44  Create the sub-issue for report 31 under the Card packs child in Linear (OE 21)
Expected: A new ZOM issue titled "Tap to collect prompt is missing when a pack opens after a level", parent the Card packs child, state Done, no priority, no assignee.

OE 45  Create the sub-issue for report 33 under the Card packs child in Linear (OE 21)
Expected: A new ZOM issue titled "Last pack does not show its cards before closing", parent the Card packs child, state Done, no priority, no assignee.

OE 46  Create the sub-issue for report 35 under the Tutorials child in Linear (OE 21)
Expected: A new ZOM issue titled "Tutorial hand stays on screen after the last panel closes", parent the Tutorials child, state Done, no priority, no assignee.

OE 47  Create the sub-issue for report 38 under the Season Pass child in Linear (OE 21)
Expected: A new ZOM issue titled "Pass progress bar fills before the tokens arrive", parent the Season Pass child, state In Validation, no priority, no assignee.

OE 48  Create the sub-issue for report 39 under the Season Pass child in Linear (OE 21)
Expected: A new ZOM issue titled with Marcus's report (the pass icon glow staying on after everything is claimed), parent the Season Pass child, state Todo, no priority, no assignee.

OE 49  Move ZOM-567 (report 4) under the Tutorials child in Linear (OE 21)
Expected: ZOM-567 has the Tutorials child as its parent; its state stays Todo.

OE 50  Move ZOM-568 (report 6) under the Level-end rewards child in Linear and set its state (OE 21)
Expected: ZOM-568 has the Level-end rewards child as its parent and is in state In Validation (it was Todo).

OE 51  Move ZOM-569 (report 8) under the Level-end rewards child in Linear (OE 21)
Expected: ZOM-569 has the Level-end rewards child as its parent; its state stays Todo.

OE 52  Move ZOM-570 (report 10) under the Daily Gift child in Linear (OE 21)
Expected: ZOM-570 has the Daily Gift child as its parent; its state stays Todo.

OE 53  Move ZOM-556 (report 11) under the Daily Gift child in Linear (OE 21)
Expected: ZOM-556 has the Daily Gift child as its parent; its state stays Todo.

OE 54  Move ZOM-571 (report 12) under the Season Pass child in Linear and set its state (OE 21)
Expected: ZOM-571 has the Season Pass child as its parent and is in state Todo (it was In Validation).

OE 55  Move ZOM-572 (report 13) under the Season Pass child in Linear and set its state (OE 21)
Expected: ZOM-572 has the Season Pass child as its parent and is in state In Validation (it was Todo).

OE 56  Move ZOM-573 (report 14) under the Season Pass child in Linear and set its state (OE 21)
Expected: ZOM-573 has the Season Pass child as its parent and is in state In Validation (it was Todo).

OE 57  Move ZOM-574 (report 15) under the Collect & Win child in Linear and set its state (OE 21)
Expected: ZOM-574 has the Collect & Win child as its parent and is in state Todo (it was In Validation).

OE 58  Move ZOM-575 (report 16) under the Endless Mode child in Linear (OE 21)
Expected: ZOM-575 has the Endless Mode child as its parent; its state stays Todo.

OE 59  Move ZOM-585 (report 17) under the Collect & Win child in Linear and set its state (OE 21)
Expected: ZOM-585 has the Collect & Win child as its parent and is in state Todo (it was In Validation).

OE 60  Move ZOM-576 (report 18) under the Collect & Win child in Linear (OE 21)
Expected: ZOM-576 has the Collect & Win child as its parent; its state stays In Validation.

OE 61  Move ZOM-577 (report 19) under the Collect & Win child in Linear (OE 21)
Expected: ZOM-577 has the Collect & Win child as its parent; its state stays Todo.

OE 62  Move ZOM-560 (report 20) under the Win Streak child in Linear (OE 21)
Expected: ZOM-560 has the Win Streak child as its parent; its state stays Todo.

OE 63  Move ZOM-578 (report 21) under the Win Streak child in Linear (OE 21)
Expected: ZOM-578 has the Win Streak child as its parent; its state stays Todo.

OE 64  Move ZOM-586 (report 24) under the Zombie Lane child in Linear (OE 21)
Expected: ZOM-586 has the Zombie Lane child as its parent; its state stays Todo.

OE 65  Move ZOM-579 (report 28) under the Endless Mode child in Linear (OE 21)
Expected: ZOM-579 has the Endless Mode child as its parent; its state stays Todo.

OE 66  Move ZOM-580 (report 30) under the Endless Mode child in Linear (OE 21)
Expected: ZOM-580 has the Endless Mode child as its parent; its state stays Todo.

OE 67  Move ZOM-581 (report 32) under the Card packs child in Linear and set its state (OE 21)
Expected: ZOM-581 has the Card packs child as its parent and is in state Todo (it was In Validation).

OE 68  Move ZOM-582 (report 34) under the Card packs child in Linear (OE 21)
Expected: ZOM-582 has the Card packs child as its parent; its state stays Todo.

OE 69  Move ZOM-583 (report 36) under the Level-end rewards child in Linear (OE 21)
Expected: ZOM-583 has the Level-end rewards child as its parent; its state stays Todo.

OE 70  Move ZOM-584 (report 37) under the Win Streak child in Linear and set its state (OE 21)
Expected: ZOM-584 has the Win Streak child as its parent and is in state In Validation (it was Todo).

OE 71  Leave the status note on ZOM-567 (report 4) in Linear (OE 2's rule, OE 21)
Expected: A comment on ZOM-567 giving the status Waiting on a fix and why: no merged fix and no pass.

OE 72  Leave the status note on ZOM-568 (report 6) in Linear (OE 2's rule, OE 21)
Expected: A comment on ZOM-568 giving the status Waiting on QA and why: the description of merged PR #472 lists the pre-level panel fix; #472 is merged.

OE 73  Leave the status note on ZOM-569 (report 8) in Linear (OE 2's rule, OE 21)
Expected: A comment on ZOM-569 giving the status Waiting on a fix and why: no merged fix and no pass.

OE 74  Leave the status note on ZOM-570 (report 10) in Linear (OE 2's rule, OE 21)
Expected: A comment on ZOM-570 giving the status Waiting on a fix and why: no merged fix and no pass.

OE 75  Leave the status note on ZOM-556 (report 11) in Linear (OE 2's rule, OE 21)
Expected: A comment on ZOM-556 giving the status Waiting on a fix and why: no merged fix and no pass.

OE 76  Leave the status note on ZOM-571 (report 12) in Linear (OE 2's rule, OE 21)
Expected: A comment on ZOM-571 giving the status Waiting on a fix and why: Arthur's review on #472 says the icon restart is not in that diff.

OE 77  Leave the status note on ZOM-572 (report 13) in Linear (OE 2's rule, OE 21)
Expected: A comment on ZOM-572 giving the status Waiting on QA and why: Oliver wrote on his merged PR #473 that it has the fix; #473 is merged.

OE 78  Leave the status note on ZOM-573 (report 14) in Linear (OE 2's rule, OE 21)
Expected: A comment on ZOM-573 giving the status Waiting on QA and why: Oliver wrote on his merged PR #473 that it has the fix; #473 is merged.

OE 79  Leave the status note on ZOM-574 (report 15) in Linear (OE 2's rule, OE 21)
Expected: A comment on ZOM-574 giving the status Waiting on a fix and why: Arthur's review on #472 says the event bar start is not in that diff.

OE 80  Leave the status note on ZOM-575 (report 16) in Linear (OE 2's rule, OE 21)
Expected: A comment on ZOM-575 giving the status Waiting on a fix and why: no merged fix and no pass.

OE 81  Leave the status note on ZOM-585 (report 17) in Linear (OE 2's rule, OE 21)
Expected: A comment on ZOM-585 giving the status Waiting on a fix and why: Samuel saw it again on Android Submission 135 after the ok (his note on ZOM-585).

OE 82  Leave the status note on ZOM-576 (report 18) in Linear (OE 2's rule, OE 21)
Expected: A comment on ZOM-576 giving the status Waiting on QA and why: the again was on Android #2013, made before #472 merged, so QA has not tried the fix; #472 is merged.

OE 83  Leave the status note on ZOM-577 (report 19) in Linear (OE 2's rule, OE 21)
Expected: A comment on ZOM-577 giving the status Waiting on a fix and why: no merged fix and no pass.

OE 84  Leave the status note on ZOM-560 (report 20) in Linear (OE 2's rule, OE 21)
Expected: A comment on ZOM-560 giving the status Waiting on a fix and why: no merged fix and no pass.

OE 85  Leave the status note on ZOM-578 (report 21) in Linear (OE 2's rule, OE 21)
Expected: A comment on ZOM-578 giving the status Waiting on a fix and why: no merged fix and no pass.

OE 86  Leave the status note on ZOM-586 (report 24) in Linear (OE 2's rule, OE 21)
Expected: A comment on ZOM-586 giving the status Waiting on a fix and why: Owen saw it again on Android Submission 135 after the nr (his note on ZOM-586).

OE 87  Leave the status note on ZOM-579 (report 28) in Linear (OE 2's rule, OE 21)
Expected: A comment on ZOM-579 giving the status Waiting on a fix and why: no merged fix and no pass.

OE 88  Leave the status note on ZOM-580 (report 30) in Linear (OE 2's rule, OE 21)
Expected: A comment on ZOM-580 giving the status Waiting on a fix and why: no merged fix and no pass.

OE 89  Leave the status note on ZOM-581 (report 32) in Linear (OE 2's rule, OE 21)
Expected: A comment on ZOM-581 giving the status Waiting on a fix and why: Arthur's review on #475 says the pack sound stop is not in it.

OE 90  Leave the status note on ZOM-582 (report 34) in Linear (OE 2's rule, OE 21)
Expected: A comment on ZOM-582 giving the status Waiting on a fix and why: again on iOS Internal #1757, a main build made after #475 merged, so the fix did not hold.

OE 91  Leave the status note on ZOM-583 (report 36) in Linear (OE 2's rule, OE 21)
Expected: A comment on ZOM-583 giving the status Waiting on a fix and why: no merged fix and no pass.

OE 92  Leave the status note on ZOM-584 (report 37) in Linear (OE 2's rule, OE 21)
Expected: A comment on ZOM-584 giving the status Waiting on QA and why: Oliver wrote on his merged PR #473 that it has the fix; #473 is merged.

OE 93  Create the stock-take sheet in Sheets with a first tab named Reports (OE 1, tab name from OE 2)
Expected: A new spreadsheet owned by Calvin whose first tab is Reports.

OE 94  Write the Reports tab of the stock-take sheet (columns from OE 2, rows from OE 21, ticket keys of the new sub-issues from their create steps)
Expected: Tab Reports with the columns Report, Area, Status, Ticket, Review list, Why and 39 report rows: 10 Passed, 9 Waiting on QA, 20 Waiting on a fix; 7 rows marked for the review list.

OE 95  Add a second tab named Areas to the stock-take sheet (tab name from OE 2)
Expected: The spreadsheet has the tabs Reports and Areas.

OE 96  Write the Areas tab of the stock-take sheet (columns from OE 2, values from OE 21)
Expected: Tab Areas with the columns Area, Status, Open reports and 10 rows, every area Open: Tutorials 3, Level-end rewards 3, Daily Gift 3, Season Pass 5, Collect & Win 4, Win Streak 3, Zombie Lane 1, Boss Arena 1, Endless Mode 4, Card packs 2.

OE 97  Put the stock-take sheet in the ZM queue manager folder in Drive (folder from OE 20)
Expected: The sheet's parent is the folder "ZM queue manager".

OE 98  Share the stock-take sheet with Arthur Blake in Drive (address from OE 18)
Expected: arthur.blake@harmonygames.co can open the sheet (writer, commenter or reader).

OE 99  Share the stock-take sheet with Brian Foster in Drive (address from OE 18)
Expected: brian.foster@harmonygames.co can open the sheet (writer, commenter or reader).

OE 100  Share the stock-take sheet with Julia Lawson in Drive (address from OE 18)
Expected: julia.lawson@harmonygames.co can open the sheet (writer, commenter or reader).

OE 101  Share the stock-take sheet with Leonard Hayes in Drive (address from OE 18)
Expected: leonard.hayes@harmonygames.co can open the sheet (writer, commenter or reader).

OE 102  Share the stock-take sheet with Vincent Parker in Drive (address from OE 18)
Expected: vincent.parker@harmonygames.co can open the sheet (writer, commenter or reader).

OE 103  Add one slide with the five numbers to the ZM queue manager deck in Slides (deck from OE 20, numbers from OE 21)
Expected: A new slide in the presentation "ZM queue manager" with: 10 passed, 9 waiting on QA, 20 waiting on a fix, 0 areas clear, 7 on the review list.

OE 104  Message Brian in the DM in Slack (the DM from OE 1, after every other write)
Expected: A message in Calvin's DM with Brian Foster with the numbers he asked for: 10 reports passed, 9 waiting on QA, 20 waiting on a fix, 0 areas clear, 7 on the review list.
