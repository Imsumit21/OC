OE 1  Read Arthur's DM from Thursday in Slack (Owen's DM with Arthur Blake, his message of Thu Feb 12 2026)
Expected: Arthur, Thu Feb 12 2026 3:10 PM PT, message ts 1770937805.214409: "I want the whole list moved over, the fixed ones too, that's the only record of what was done." "How we call each one is in the carry-over notes doc I shared with you." "While you're in there bring the UI Changes tree up to date, it never got closed out, and leave a line on every child saying where it landed." "Put a sheet in your DD bug carry-over folder so I can look things up, and share it with everyone on Sunday's bug review." "Then tell me here how many are still broken, how many new tickets you filed and how many of the 28 UI children are Done."

OE 2  Find and read the carry-over notes doc in Drive (search "carry-over notes", named in OE 1; the Doc Arthur shared with Owen)
Expected: Doc "DD bug carry-over notes", owner arthur.blake@harmonygames.co, created Thu Feb 12 2026 2:48 PM PT. Scope: "every ticked or unticked line in the comment channel of Vincent's Android canvas, and every bug posted in the bug channel after the last line in that comment channel." "A comment whose line was deleted has nothing to carry over." "In the bug channel a follow-up on a bug already posted is part of that bug, and a design question for Leonard or a post that points at a QA doc isn't a bug post." "Robert's reports in the sub-250 channel aren't part of this" Outcomes: "Take the first outcome that fits." "Fixed: the tick stands, or a later record says it was fixed. File it as Done." "Gone: it isn't fixed and it's a bug in something the build players have no longer has. File it as Canceled." "Covered: it isn't fixed and an open ticket already covers it. Don't file a new one, add a note on that ticket with the canvas wording." "Vincent tied a few lines to tickets before he left." "Broken: anything else. File it as Bugs." What counts: "we go by the Android build players have, 0.3.310, which came off the economy line, not by develop." "A tick on the canvas stands unless a later record about that bug says otherwise." "An unticked line, or a bug nobody closed, stays open unless a later record says it was fixed, and a commit named for the bug counts as that record if nothing later says otherwise." "A fix only counts once it is in that build." "A PR that never made it into that build doesn't count." New tickets: "Engineering team, Bug label, parent ENG-2401, title is the line without its tick box, or the first line of the post, as it was written, no assignee, nothing in the description." "If anything changes after this I'll put it on the master ticket." UI tree: "every open child goes Done unless a record shows a piece of its UI work never made it into that build or the screen is switched off there. Then it stays where it is." "Children already Done stay Done and the masters stay as they are." "A bug on a screen doesn't hold its child, that's what the bug ticket is for." "Brian and Oliver left notes on some of the open children." "Brian's closing rule from the UI work applies to the line on every child, Done or not." "Sheet columns: Bug, Outcome, Ticket, Why." "When you report back, Covered ones count as still broken."

OE 3  Read the comments on the UI Changes master ticket in Linear (ENG-2401 "UI Changes Master Ticket", named in the prompt; OE 2 says changes go on it)
Expected: Arthur, Thu Feb 12 2026 4:40 PM PT (Fri Feb 13 00:40 UTC): "For the carry-over: put [2231] at the front of every title you file so I can filter them."

OE 4  Find Brian's closing rule in Trello (search "UI Changes", the master's name from the prompt; the card "UI optimization pass" on the DD Product Roadmap board; read its comments and its checklist)
Expected: Card description: "Tickets are under the UI Changes master." Brian Foster, Wed Nov 5 2025 2:41 AM PT: "When we close these UI tickets out every one gets a note naming the current public build, otherwise nobody can tell later what players actually had." The card's checklist has 28 screens, 27 complete and Daily Gift incomplete.

OE 5  Find Owen's DD bug carry-over folder in Drive (search the folder name from the prompt)
Expected: Folder "DD bug carry-over", id d_9b41e7c2a05d36f8e1c7a4, owner owen.baker@harmonygames.co, created Thu Feb 12 2026 3:00 PM PT.

OE 6  Read Sunday's bug review on Owen's calendar (list his events for Sun Feb 15 2026; "Sunday's bug review" from the prompt and OE 1)
Expected: Event "DD bug review", organizer arthur.blake@harmonygames.co, starts Sun Feb 15 2026 9:00 AM PT (not yet held). Attendees: arthur.blake@harmonygames.co, robert@harmonygames.co, oliver.brooks@harmonygames.co, owen.baker@harmonygames.co.

OE 7  Find the comment channel of Vincent's Android canvas in Slack (search channels "Android", from OE 2's "Vincent's Android canvas")
Expected: Channel "FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025", id CE156FDFB428.

OE 8  Read every root comment in that channel in Slack (channel from OE 7; page through the whole history)
Expected: 69 root comments posted Thu Nov 13 2025 5:38 AM PT to Fri Nov 21 2025 7:04 AM PT. 6 are empty (their lines were deleted): ts 1763042124.247899, 1763046620.138349, 1763394484.266469, 1763394870.543909, 1763394900.834239, 1763548828.843199. The other 63 are the lines, 55 with a ticked box and 8 unticked; each line's text is in its ticket event below (OEs 32 to 92; lines 3 and 29, which get no ticket, in OEs 100 and 101). The last line is ts 1763737449.845379.

OE 9  Read the thread under each line in Slack (the roots from OE 8 that have replies; read each thread to its last reply)
Expected: Line 57 (Tavern buttons): Brian, Thu Nov 20 2025 11:47 AM PT: "I send the fix". Line 40 (navigation bar tooltips), last reply, Vincent, Sat Nov 22 2025 1:05 PM PT: "checked Brian's second fix, the 1 pixel gap is gone and the tooltips look right on my android now". Line 34 (train level backgrounds): Arthur, Thu Nov 20 2025 12:44 PM PT: "fixed"; then Vincent, Sat Nov 22 2025 1:00 PM PT: "better but the snow train is still off and the green shows, leaving this one open". Line 51 (team quit): Vincent, Fri Nov 21 2025 8:20 AM PT: "the leave team popup is fine now but the navigation bar still goes after quitting". Line 42 (lives not decreased after a loss): Vincent, Sat Nov 22 2025 1:10 PM PT: "same after Oliver's change, a loss still doesn't take a life". Line 54 (lives only decreased after losing twice): Vincent, Sat Nov 22 2025 1:11 PM PT: "same here, it still only drops on the second loss".

OE 10  Read the bug channel #god-bugs in Slack from just after the last canvas line (ts 1763737449.845379, OE 8) to the clock (the bug channel from OE 2)
Expected: Seven bug posts: Thu Nov 27 2025 7:09 AM PT "<@EMPLOYEE_0025_SLACK_ID> i was playing trough the levels with …"; Thu Nov 27 2025 10:00 AM PT "the tile dozer game background out of the window, went small, that …"; Mon Dec 1 2025 11:12 PM PT (Tue Dec 2 07:12 UTC) "Any idea what might cause this flickering?"; Mon Dec 1 2025 11:22 PM PT (Tue Dec 2 07:22 UTC) "My game started out without music, and suddenly at chapter 2 level 2, …"; Mon Dec 1 2025 11:41 PM PT (Tue Dec 2 07:41 UTC) "Animation is delayed for [PERSON_NAME_1711]'s acid. I hear the sound, …"; Mon Dec 1 2025 11:52 PM PT (Tue Dec 2 07:52 UTC) "After getting to stage 2 if [PERSON_NAME_1711]'s treasure, the button …"; Mon Dec 22 2025 6:53 AM PT "Hey <@EMPLOYEE_0002_SLACK_ID>! We currently have an issue on the DD …". The bottom bar bug is one post in two messages (1766415211.386389 and 1766415326.501939; the replies sit under the second). Not bug posts: Arthur's "is this related to the new symbols?" (a follow-up on the mega tile post), Robert's "Happened twice in the video" (a follow-up on the flickering post), Robert's "tested your build for the most part" with a Google Doc link (points at a QA doc), Arthur's question to Leonard "is purchasing no-ads supposed to turn off rewarded video ads too?" and Leonard's two answers (a design question for Leonard), five Nov 25 chat messages (where the canvases are, asking for a build to test), and canvas, leave and join notices.

OE 11  Read the thread under each of the seven posts in Slack (posts from OE 10; read each thread to its last reply)
Expected: Mega tile, last reply, Marcus, Fri Nov 28 2025 4:10 AM PT: "still happens on today's build". Tile dozer window, the only reply, Marcus, Fri Nov 28 2025 3:26 AM PT: "Ok i fixed it and did a PR". Flickering, last reply, Owen, Tue Dec 2 2025 9:15 AM PT: "testing a fix now, I'll let you guys know how it goes.". Music, last reply, Owen, Tue Dec 2 2025 9:15 AM PT: "thanks for the info, I'll check this issue next.". Acid, last reply, Brian, Tue Dec 2 2025 8:57 AM PT: "I'm checking". Treasure button, Brian, Tue Dec 2 2025 8:56 AM PT: "I send the fix", then Robert: "Thanks". Bottom bar, reply 61 and last, Brian, Mon Dec 29 2025 7:15 AM PT: "the new camera setup fixed it, the bottom bar and the top panel both show on the devices I have here, closing this one".

OE 12  Find and read Marcus's window PR in GitHub (search pull requests "tile dozer" in harmonygames-Games/GameOfDominoes, from the post and Marcus's "did a PR" in OE 11)
Expected: PR #1913 "Fixing window in tile dozer scene", state open, not merged, base develop, head Marcus/TileDozer_WindowFix, created Fri Nov 28 2025 3:25 AM PT.

OE 13  Search Slack for later records on the shop icons line (search "Memory Tile", from the line "shops from rivertile and memory tile has weird shop icons" in OE 8; open the hit's thread)
Expected: Brian's reply in #dd-road-to-sub-250mb, Mon Dec 1 2025 8:35 AM PT, the 8th reply under Robert's post "Are these the right asset for the gems?" (Mon Nov 24 2025 7:47 PM PT (Tue Nov 25 03:47 UTC)): "I was back in the shop prefabs today, the round icons on the River Tile and Memory Tile shops are there again on the current build, so don't trust that tick". Later than the line itself (posted Wed Nov 19 2025 2:50 AM PT).

OE 14  Search Slack for later records on the Tavern line (search "Tavern", from the line "Tavern buttons lost its frame" in OE 8)
Expected: Marcus's DM to Owen, Thu Dec 11 2025 3:20 AM PT: "the Tavern buttons lost their frame again on last night's Android build, I looked at the prefab and Brian's fix didn't hold". Later than the line (posted Thu Nov 20 2025 4:47 AM PT) and Brian's fix in its thread (OE 9).

OE 15  Search Slack for the lives change (search "lives", from the three lives lines in OE 8; look from Nov 22 2025 on)
Expected: Leonard Hayes in the shared publishing channel, Mon Dec 1 2025 11:13 PM PT (Tue Dec 2 07:13 UTC): "We are removing lives feature from the game and replacing it with a ticket system similar to Domino Dreams." Other hits include Dec 2 and Dec 3 posts in the group DM with Leonard, Brian and Arthur, where the economy-line work is discussed.

OE 16  Read the December posts in the group DM with Leonard, Brian and Arthur in Slack (the channel from OE 15's hits)
Expected: Owen, Tue Dec 2 2025 4:29 PM PT (Wed Dec 3 00:29 UTC): "I suggest we all work on a feature branch, and once the economy changes are completed we can move it to develop if need it." "Working branch is `EconomyChanges`". Arthur, Tue Dec 16 2025 3:22 PM PT: "can you disable WC and I'll start deploying stuff to prod"; Owen, Tue Dec 16 2025 3:31 PM PT: "event disabled"; Owen: "pushed to EconomyChanges branch". Leonard's update notes, Tue Dec 16 2025 4:59 PM PT (Wed Dec 17 00:59 UTC): "Lives are out, now you can enter using" "the lives counter is removed". Win & Collect is the Collect&win screen of ENG-2424.

OE 17  Read the Android EconomyChanges build lines in #builds in Slack (search "EconomyChanges", the branch named in OE 16; Dec 2025)
Expected: Tue Dec 9 2025 12:00 PM PT: "DD Android - #2297 - EconomyChanges - (?MB) Still Failing after 15 min" (the build failed; its list shows what is on the branch) with changes "Fix for EndLevelPopup flickering on Tap Anywhere clicked [Arthur Blake]" "Nathan Animation Fix [Arthur Blake]" "Updated URLAudioPlayer to fully download clip if needed [Arthur Blake]". Wed Dec 10 2025 12:12 PM PT: "DD Android - #2299 - EconomyChanges - (220MB) Success" with changes "Removed life pop-up from end screen".

OE 18  Search Slack for later records on the flickering post (search "flickering", from the post in OE 10; open the hit's thread)
Expected: Robert's reply in #dd-road-to-sub-250mb, Fri Dec 19 2025 9:10 AM PT, under his own report "Not game breaker, but some flickering when I hit play button or when I exit a level": "the flickering is gone on this week's build, both on the play button and coming out of a level". Later than the thread's last reply (OE 11).

OE 19  Search Slack for the treasure button fix (search "Treasure button", from the post in OE 10)
Expected: #engineering-bots, Tue Dec 2 2025 8:56 AM PT: a commit pushed to develop by brian.foster, "fbe7bdea" "Fix issue opening Axe Arena panel from Nate Treasure button", earlier the same day than Owen's post starting the EconomyChanges branch (4:29 PM PT, OE 16).

OE 20  Search GitHub commits for develop merged into EconomyChanges (search commits "into EconomyChanges" in harmonygames-Games/GameOfDominoes, the branch from OE 16)
Expected: Commit 04d3118d by Arthur Blake, Wed Dec 17 2025 6:20 AM PT: "Merge remote-tracking branch 'origin/develop' into EconomyChanges". It brings develop, which has the Dec 2 treasure button fix (OE 19), into EconomyChanges.

OE 21  Find and read the camera PR in GitHub (search pull requests "camera" in harmonygames-Games/GameOfDominoes, from Brian's "the new camera setup fixed it" in OE 11; the one merged in Dec 2025)
Expected: PR #1916 "New core game camera config", base EconomyChanges, head EconomyChangesOverlayCameras, merged Fri Dec 26 2025 11:05 AM PT; Arthur's comment, Fri Dec 26 2025 10:50 AM PT: "Same here, into EconomyChanges for the next BoomBit drop."

OE 22  Read Owen's DM with Brian Foster in Slack from Nov 19 2025 on (Brian owns the UI card in OE 4, and the acid post's last reply is his "I'm checking" in OE 11)
Expected: Brian, Wed Nov 19 2025 12:57 PM PT: "I just need to go over the Daily Gift one more time. I’ll finish that tomorrow morning, so it’ll be done before the meeting." Brian, Mon Dec 8 2025 7:10 AM PT: "music plays normally on my side since your audio player change, and Nate's acid throw lines up again after my animation fix, Robert's two are sorted". Brian, Thu Dec 11 2025 8:46 AM PT: "I never got back to the two popups from Arthur's reviews: the Axe Arena info popup still has the old frame and the Tile Dozer how-to-play popup still points at the old sprites." Brian, Thu Dec 11 2025 8:47 AM PT: "Daily Gift isn't finished either, the panel never got its last pass."

OE 23  Search Owen's mail for messages from Vincent Parker about signing in, in Gmail (OE 2 says Vincent tied lines to tickets; the unticked Apple and manual sign-in lines read in OE 8 are about signing in) and read his "sign in lines on my list"
Expected: Vincent to Owen, Thu Nov 20 2025 10:12 AM PT, subject "sign in lines on my list", in the inbox: "The Apple sync line on my Android list comes down to the same sync problem as ENG-2073, no need for anything new."

OE 24  Read ENG-2073 in Linear (named in OE 23)
Expected: ENG-2073 "Sign-In Account Synchronization Issues", state Bugs (open).

OE 25  Search Linear issues for "signing" (the manual sign-in line in OE 8 is about signing in) and read the comments on ENG-2363
Expected: ENG-2363 "After signing-in, the game stuck at splash screen-", state In Progress (open). Vincent, Thu Nov 20 2025 10:20 AM PT: "Android still hits this: the manual sign-in line on my list gets stuck on loading after signing in, same thing as here."

OE 26  Check whether an open ticket covers any item that isn't fixed: list the open ENG tickets in Linear (any open state: Bugs, Todo, In Progress, PR, Validation, Regression, Backlog) and read the comments on the ones that read like a canvas line or a bug post (the Covered test in OE 2)
Expected: Six open tickets each carry a Nov 20 2025 comment from Arthur that narrows them: ENG-2406 "Input is not registered for tile dozer and lucky drop" (Bugs), Arthur, Thu Nov 20 2025 2:33 PM PT: "Taps during play, nothing to do with how the scene looks."; ENG-2181 "Leaderboard profile frames are visually different at first" (Bugs), Arthur, Thu Nov 20 2025 2:24 PM PT: "Bots' frames on the weekly leaderboard only."; ENG-2351 "Missing Translation on shop offers after visiting language section" (Bugs), Arthur, Thu Nov 20 2025 2:29 PM PT: "Text only, after opening the language screen."; ENG-2280 "Sign in Issues for loading a prior data" (Bugs), Arthur, Thu Nov 20 2025 2:10 PM PT: "This one is the ios case where a returning player loads old data and the HUD and avatar don't come up."; ENG-2281 "After signing in to load prior data, puzzles might be broken" (Bugs), Arthur, Thu Nov 20 2025 2:14 PM PT: "Only the first puzzle after loading old data, on ios."; ENG-2398 "show pop up to kill the app and restart" (Todo), Arthur, Thu Nov 20 2025 2:18 PM PT: "Stopgap for the relogin problems, this only adds the restart pop up.". Each comment limits its ticket to something other than the shop icons, Tavern, train backgrounds, team-quit, backend-errors, mega tile and tile dozer window items, so none of those seven is Covered; the two covering tickets are ENG-2073 and ENG-2363 (OEs 23 to 25).

OE 27  List the UI tree under the master ticket in Linear (children of ENG-2401, then the children of each group)
Expected: Groups ENG-2403 Core Game, ENG-2404 Live-Ops, ENG-2405 Mini-Games, all Todo; ENG-2401 Todo. 28 children: ENG-2403: ENG-2409 Splash Screen (Done), ENG-2410 Shop (Validation), ENG-2411 Character Section (Done), ENG-2412 Saga map (Done), ENG-2413 Teams (Done), ENG-2414 Leaderboard (PR), ENG-2415 Quest (PR), ENG-2416 Profile Page (Done), ENG-2417 Settings (PR), ENG-2418 Level - win (PR), ENG-2419 Level Lose - Out-of-moves Screens (PR), ENG-2420 Chapter Section (Done), ENG-2421 Tavern (Done), ENG-2422 Pre-game Panel (Done), ENG-2423 Transition Screens (Done); ENG-2404: ENG-2424 Collect&win - Magical Wings (PR), ENG-2425 Nathan's Treasure (PR), ENG-2426 Axe Arena (PR), ENG-2427 River Rush (PR), ENG-2428 Season Pass (Validation), ENG-2429 Remove Ad (Validation), ENG-2430 Offers (Validation), ENG-2431 Rate-us Pop-ups (PR), ENG-2437 Daily Gift (In Progress); ENG-2405: ENG-2432 River Tile (PR), ENG-2433 Memory Tile (PR), ENG-2434 Tile Dozer (PR), ENG-2435 Lucky Drop (PR). 9 Done, 19 open.

OE 28  Read the comments on each of the 19 open children in Linear (list from OE 27)
Expected: Four comments in all. ENG-2428, Oliver Brooks, Fri Dec 5 2025 4:30 AM PT: "The illustrations went in but the reward track still uses the old frames, this isn't finished." ENG-2410, Brian, Fri Nov 21 2025 7:05 AM PT: "Checked the Shop screen after the merge, looks right on android." ENG-2429, Brian: "Checked the Remove Ad pop up on today's build, looks right on android." ENG-2430, Brian: "Checked the Offers on today's build, looks right on android."

OE 29  Read the review comments on the UI optimization PRs in GitHub (search pull requests "UI Optimization" in harmonygames-Games/GameOfDominoes, the children's titles from OE 27)
Expected: PR #1905 "ENG-2405: Mini-Games UI Optimization", merged Wed Nov 19 2025 5:05 AM PT; Arthur's review comment, Wed Nov 19 2025 5:05 AM PT: "the Tile Dozer how-to-play popup still points at the old sprites in this PR. That has to be swapped before the Tile Dozer ticket can close." PR #1908 "ENG-2426: Axe Arena - UI Optimization", merged Wed Nov 19 2025 5:51 PM PT (Thu Nov 20 01:51 UTC); Arthur's review comment, Wed Nov 19 2025 5:51 PM PT (Thu Nov 20 01:51 UTC): "the Axe Arena info popup keeps the old frame here. Needs doing before the Axe Arena ticket can close."

OE 30  Take the first outcome that fits for each of the 70 bugs (rules in OEs 2 and 3; records in OEs 8 to 29)
Expected: Fixed 58: the 53 ticked lines other than the shop icons and the Tavern line (the tick stands; for the tooltips line Vincent also confirmed the second fix, OE 9), the flickering post (Robert's reply, OE 18; the fix is on EconomyChanges, listed in build #2297's changes: that build failed, and #2299 on the same branch succeeded on Dec 10, OE 17), the music and acid posts (Brian's Dec 8 line, OE 22; both fixes are on EconomyChanges, listed in build #2297's changes, OE 17), the treasure button post (Brian's fix, OE 11; the commit went to develop, and develop was merged into EconomyChanges on Dec 17, OEs 19 and 20) and the bottom bar post (Brian closed it, OE 11; the camera PR merged into EconomyChanges, OE 21). Gone 3: the three lives lines, the two with Vincent's later replies (OE 9) and "When I change the character, it just adds 1 life back or reduced the timer by 20 min.", since lives are removed on the economy line (OE 15; build #2299 and Leonard's Dec 16 update notes, OEs 17 and 16). Covered 2: the Apple sync line (ENG-2073, OEs 23 and 24) and the manual sign-in line (ENG-2363, OE 25). Broken 7: the shop icons line (OE 13), the Tavern line (OE 14), the train backgrounds line and the team-quit line (Vincent's replies, OE 9), the unticked backend-errors line (it stays open), the mega tile post (OE 11) and the tile dozer window post (PR #1913 is still open, not merged, OE 12); no open ticket covers any of the seven (OE 26). So 68 new tickets (58 Done, 7 Bugs, 3 Canceled), each in team Engineering with label Bug, parent ENG-2401, no assignee, empty description, and title "[2231] " plus the line without its box or the post's first line as written (a Slack mention or emoji code may stay as written or show as a name).

OE 31  Decide each UI child under the tree rule (OE 2; tree from OE 27, records from OEs 16, 22, 28 and 29)
Expected: Stay where they are: ENG-2424 (PR): Win & Collect is switched off on the economy line (OE 16); ENG-2426 (PR): the Axe Arena info popup never got its pass (OEs 29 and 22); ENG-2428 (Validation): the reward track still uses the old frames (OE 28); ENG-2434 (PR): the Tile Dozer how-to-play popup never got swapped (OEs 29 and 22); ENG-2437 (In Progress): the Daily Gift panel never got its last pass (OE 22, later than Brian's Nov 19 plan). Move to Done: ENG-2410, ENG-2414, ENG-2415, ENG-2417, ENG-2418, ENG-2419, ENG-2425, ENG-2427, ENG-2429, ENG-2430, ENG-2431, ENG-2432, ENG-2433, ENG-2435 (the shop icons regression on the River Tile and Memory Tile shops is a bug with its own ticket, and a bug on a screen doesn't hold its child, OE 2). 23 of 28 end Done: the 9 already Done and these 14. Every one of the 28 gets a line naming the public build 0.3.310 (OEs 2 and 4).

OE 32  Create the ticket for canvas line 1 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] When I start the game on ios, I got the error about the cache.".

OE 33  Create the ticket for canvas line 2 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] When I start the game on android, it gives google sign in issue where I cannot sign in to my account. :warning:".

OE 34  Create the ticket for canvas line 4 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] The game waits too long in the first splash screen because I think it waits for downloading unnecessary addressable to start off.  :warning:".

OE 35  Create the ticket for canvas line 5 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] After season pass is unlocked, it gives many different errors.  :warning: :warning: :warning:".

OE 36  Create the ticket for canvas line 6 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] Its pop up cannot be closed,".

OE 37  Create the ticket for canvas line 7 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] after completing a level, the game stuck before win screen".

OE 38  Create the ticket for canvas line 8 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] the event page is empty with lots of null ref".

OE 39  Create the ticket for canvas line 9 in Linear (fields from OE 30)
Expected: A new issue in state Bugs, title "[2231] When I lost a level, I got some backend errors but I don't think it affects something.".

OE 40  Create the ticket for canvas line 10 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] offers has no visuals.".

OE 41  Create the ticket for canvas line 11 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] level completed text has no outline".

OE 42  Create the ticket for canvas line 12 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] bottom part of the top HUD has a minor gap.".

OE 43  Create the ticket for canvas line 13 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] life balance timer in top HUD".

OE 44  Create the ticket for canvas line 14 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] sides of event icons".

OE 45  Create the ticket for canvas line 15 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] appointment mechanic button".

OE 46  Create the ticket for canvas line 16 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] bottom HUD, selected tab has sides that are visible, other navigation bar split in the middle.".

OE 47  Create the ticket for canvas line 17 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] chapter selection button split".

OE 48  Create the ticket for canvas line 18 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] In profile,".

OE 49  Create the ticket for canvas line 19 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] every character page has a split in the middle of select and upgrade button.".

OE 50  Create the ticket for canvas line 20 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] character names on top of single character pages has the frame issue.".

OE 51  Create the ticket for canvas line 21 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] in, character selection screen (all 4 visible as windows), the characters frames has gaps on top.".

OE 52  Create the ticket for canvas line 22 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] In character screens,".

OE 53  Create the ticket for canvas line 23 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] In chapter selection".

OE 54  Create the ticket for canvas line 24 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] Win & Collect Pop Up".

OE 55  Create the ticket for canvas line 25 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] initial reward of infinite lives beneath the overlay".

OE 56  Create the ticket for canvas line 26 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] stage complete reward of coins beneath the overlay".

OE 57  Create the ticket for canvas line 27 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] [PERSON_NAME_1711]'s treasure hunt pop up banner looks weird compared to the mockup.".

OE 58  Create the ticket for canvas line 28 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] memory game, streak texts are transparent.".

OE 59  Create the ticket for canvas line 30 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] Teams addressable doesn't work".

OE 60  Create the ticket for canvas line 31 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] Purple bg visual issues".

OE 61  Create the ticket for canvas line 32 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] some banners are lost.".

OE 62  Create the ticket for canvas line 33 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] Lucky drop and tile dozer quit pop up alignment problem".

OE 63  Create the ticket for canvas line 34 in Linear (fields from OE 30)
Expected: A new issue in state Bugs, title "[2231] train level backgrounds are broken".

OE 64  Create the ticket for canvas line 35 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] River [USERNAME_20421], sail images are broken when animating".

OE 65  Create the ticket for canvas line 36 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] chapter 2 saga map [USERNAME_20422] has a weird artifact".

OE 66  Create the ticket for canvas line 37 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] top hud".

OE 67  Create the ticket for canvas line 38 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] prelevel dialogue".

OE 68  Create the ticket for canvas line 39 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] profile pop ups".

OE 69  Create the ticket for canvas line 40 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] navigation bar tooltips".

OE 70  Create the ticket for canvas line 41 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] Avatar frame is missing".

OE 71  Create the ticket for canvas line 42 in Linear (fields from OE 30)
Expected: A new issue in state Canceled, title "[2231] P.S I found the issue, lives are not decreased after a loss.  <@EMPLOYEE_0025_SLACK_ID>".

OE 72  Create the ticket for canvas line 43 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] Win & Collect gives a null ref every time chapter scenes are loaded.".

OE 73  Create the ticket for canvas line 44 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] avatar frame is not missing anymore but avatar images are too small.".

OE 74  Create the ticket for canvas line 45 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] some offers have too white background".

OE 75  Create the ticket for canvas line 46 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] don't show 24 hours checkbox visual is missing and it doesn't change with the input.".

OE 76  Create the ticket for canvas line 47 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] offer price tag and button is not a rectangular anymore.".

OE 77  Create the ticket for canvas line 48 in Linear (fields from OE 30)
Expected: A new issue in state Bugs, title "[2231] shops from rivertile and memory tile has weird shop icons (circular shapes entirely)".

OE 78  Create the ticket for canvas line 49 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] in tile dozer, reward screen is weird - the header and buttons don't stretch".

OE 79  Create the ticket for canvas line 50 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] After losing a level, retry prelevel dialogue is broken - doesn't show the correct info, all place holders, and throws a null ref.".

OE 80  Create the ticket for canvas line 51 in Linear (fields from OE 30)
Expected: A new issue in state Bugs, title "[2231] When I created a team and quitted it, the navigation bar disappears, the only way to see that is to have a pop up in the teams section.".

OE 81  Create the ticket for canvas line 52 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] [PERSON_NAME_1711]'s treasure hunt's stage text is misaligned.".

OE 82  Create the ticket for canvas line 53 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] Chapter 4 couldn't load due to addressable issues.  :warning: :warning:".

OE 83  Create the ticket for canvas line 54 in Linear (fields from OE 30)
Expected: A new issue in state Canceled, title "[2231] Lives are only decreased after losing twice in a row from the retry prelevel dialogue.".

OE 84  Create the ticket for canvas line 55 in Linear (fields from OE 30)
Expected: A new issue in state Canceled, title "[2231] When I change the character, it just adds 1 life back or reduced the timer by 20 min.".

OE 85  Create the ticket for canvas line 56 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] Core game music couldn't play.".

OE 86  Create the ticket for canvas line 57 in Linear (fields from OE 30)
Expected: A new issue in state Bugs, title "[2231] Tavern buttons lost its frame. <@EMPLOYEE_0021_SLACK_ID>".

OE 87  Create the ticket for canvas line 58 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] character frames in char selection looks like it doesn't fit".

OE 88  Create the ticket for canvas line 59 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] Axe Arena window in lose flow has overflowing text.".

OE 89  Create the ticket for canvas line 60 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] Streak Fever has overflowing text on its pop up.".

OE 90  Create the ticket for canvas line 61 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] continue button has a shadow as "continuar"".

OE 91  Create the ticket for canvas line 62 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] activate button pop up has also different shadow text than the original".

OE 92  Create the ticket for canvas line 63 in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] and activate pop up has the wrong price tage, and every other price tag is converted to the local currency except that one.".

OE 93  Create the ticket for the mega tile post in Linear (fields from OE 30)
Expected: A new issue in state Bugs, title "[2231] <@EMPLOYEE_0025_SLACK_ID> i was playing trough the levels with [USERNAME_2665] and he gave me a megatile like this and when i look at the megatile one tile its not visibile and in the element 3 its like nothing its There, basically nothing its active There".

OE 94  Create the ticket for the tile dozer window post in Linear (fields from OE 30)
Expected: A new issue in state Bugs, title "[2231] the tile dozer game background out of the window, went small, that plane should have been big to fill the window!".

OE 95  Create the ticket for the flickering post in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] Any idea what might cause this flickering?".

OE 96  Create the ticket for the music post in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] My game started out without music, and suddenly at chapter 2 level 2, music started out of nowhere, intended?".

OE 97  Create the ticket for the acid post in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] Animation is delayed for [PERSON_NAME_1711]'s acid. I hear the sound, and the tile disappears, and then 2 seconds later [PERSON_NAME_1711] throws it lol, at what is now already a blank spot".

OE 98  Create the ticket for the treasure button post in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] After getting to stage 2 if [PERSON_NAME_1711]'s treasure, the button on home screen is bugged and I cant click into it. It gives me axe arena instead".

OE 99  Create the ticket for the bottom bar post in Linear (fields from OE 30)
Expected: A new issue in state Done, title "[2231] Hey <@EMPLOYEE_0002_SLACK_ID>! We currently have an issue on the DD side. on some Android devices, the bottom bar is not visible, as shown in the example. We are trying different methods to resolve this. After checking the builds, we noticed that the issue occurs exactly when shadows and lighting settings are disabled. This could be related either to lighting itself or to GPU-related behavior on certain devices".

OE 100  Add the canvas wording on ENG-2073 in Linear (Covered, OE 30)
Expected: A comment on ENG-2073 carrying the line "In general, I cannot sync and sign in with my Apple account. :warning: :warning:".

OE 101  Add the canvas wording on ENG-2363 in Linear (Covered, OE 30)
Expected: A comment on ENG-2363 carrying the line "On android, manual sign-in has an issue after the sign-in. The game stuck at loading screen with an addressable error. :warning:".

OE 102  Move ENG-2410 (Shop UI Optimization) to Done in Linear (OE 31)
Expected: ENG-2410 state Validation → Done.

OE 103  Move ENG-2414 (Leaderboard UI Optimization) to Done in Linear (OE 31)
Expected: ENG-2414 state PR → Done.

OE 104  Move ENG-2415 (Quest UI Optimization) to Done in Linear (OE 31)
Expected: ENG-2415 state PR → Done.

OE 105  Move ENG-2417 (Settings UI Optimization) to Done in Linear (OE 31)
Expected: ENG-2417 state PR → Done.

OE 106  Move ENG-2418 (Level - win UI Optimization) to Done in Linear (OE 31)
Expected: ENG-2418 state PR → Done.

OE 107  Move ENG-2419 (Level Lose - Out-of-moves Screens UI Optimization) to Done in Linear (OE 31)
Expected: ENG-2419 state PR → Done.

OE 108  Move ENG-2425 (Nathan's Treasure - UI Optimization) to Done in Linear (OE 31)
Expected: ENG-2425 state PR → Done.

OE 109  Move ENG-2427 (River Rush - UI Optimization) to Done in Linear (OE 31)
Expected: ENG-2427 state PR → Done.

OE 110  Move ENG-2429 (Remove Ad - UI Optimization) to Done in Linear (OE 31)
Expected: ENG-2429 state Validation → Done.

OE 111  Move ENG-2430 (Offers - UI Optimization) to Done in Linear (OE 31)
Expected: ENG-2430 state Validation → Done.

OE 112  Move ENG-2431 (Rate-us Pop-ups - UI Optimization) to Done in Linear (OE 31)
Expected: ENG-2431 state PR → Done.

OE 113  Move ENG-2432 (River Tile - UI Optimization) to Done in Linear (OE 31)
Expected: ENG-2432 state PR → Done.

OE 114  Move ENG-2433 (Memory Tile - UI Optimization) to Done in Linear (OE 31)
Expected: ENG-2433 state PR → Done.

OE 115  Move ENG-2435 (Lucky Drop - UI Optimization) to Done in Linear (OE 31)
Expected: ENG-2435 state PR → Done.

OE 116  Leave a line on ENG-2409 (Splash Screen UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2409 saying it is Done and landed in Android 0.3.310.

OE 117  Leave a line on ENG-2410 (Shop UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2410 saying it is Done and landed in Android 0.3.310.

OE 118  Leave a line on ENG-2411 (Character Section UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2411 saying it is Done and landed in Android 0.3.310.

OE 119  Leave a line on ENG-2412 (Saga map UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2412 saying it is Done and landed in Android 0.3.310.

OE 120  Leave a line on ENG-2413 (Teams UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2413 saying it is Done and landed in Android 0.3.310.

OE 121  Leave a line on ENG-2414 (Leaderboard UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2414 saying it is Done and landed in Android 0.3.310.

OE 122  Leave a line on ENG-2415 (Quest UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2415 saying it is Done and landed in Android 0.3.310.

OE 123  Leave a line on ENG-2416 (Profile Page UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2416 saying it is Done and landed in Android 0.3.310.

OE 124  Leave a line on ENG-2417 (Settings UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2417 saying it is Done and landed in Android 0.3.310.

OE 125  Leave a line on ENG-2418 (Level - win UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2418 saying it is Done and landed in Android 0.3.310.

OE 126  Leave a line on ENG-2419 (Level Lose - Out-of-moves Screens UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2419 saying it is Done and landed in Android 0.3.310.

OE 127  Leave a line on ENG-2420 (Chapter Section UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2420 saying it is Done and landed in Android 0.3.310.

OE 128  Leave a line on ENG-2421 (Tavern UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2421 saying it is Done and landed in Android 0.3.310.

OE 129  Leave a line on ENG-2422 (Pre-game Panel UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2422 saying it is Done and landed in Android 0.3.310.

OE 130  Leave a line on ENG-2423 (Transition Screens) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2423 saying it is Done and landed in Android 0.3.310.

OE 131  Leave a line on ENG-2424 (Collect&win - Magical Wings - UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2424 saying it stays PR because Win & Collect is switched off on the economy line; public build 0.3.310.

OE 132  Leave a line on ENG-2425 (Nathan's Treasure - UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2425 saying it is Done and landed in Android 0.3.310.

OE 133  Leave a line on ENG-2426 (Axe Arena - UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2426 saying it stays PR because the Axe Arena info popup never got its pass; public build 0.3.310.

OE 134  Leave a line on ENG-2427 (River Rush - UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2427 saying it is Done and landed in Android 0.3.310.

OE 135  Leave a line on ENG-2428 (Season Pass - UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2428 saying it stays Validation because the reward track still uses the old frames; public build 0.3.310.

OE 136  Leave a line on ENG-2429 (Remove Ad - UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2429 saying it is Done and landed in Android 0.3.310.

OE 137  Leave a line on ENG-2430 (Offers - UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2430 saying it is Done and landed in Android 0.3.310.

OE 138  Leave a line on ENG-2431 (Rate-us Pop-ups - UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2431 saying it is Done and landed in Android 0.3.310.

OE 139  Leave a line on ENG-2432 (River Tile - UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2432 saying it is Done and landed in Android 0.3.310.

OE 140  Leave a line on ENG-2433 (Memory Tile - UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2433 saying it is Done and landed in Android 0.3.310.

OE 141  Leave a line on ENG-2434 (Tile Dozer - UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2434 saying it stays PR because the Tile Dozer how-to-play popup never got swapped; public build 0.3.310.

OE 142  Leave a line on ENG-2435 (Lucky Drop - UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2435 saying it is Done and landed in Android 0.3.310.

OE 143  Leave a line on ENG-2437 (Daily Gift UI Optimization) in Linear (OE 31, Brian's rule in OE 4)
Expected: A comment on ENG-2437 saying it stays In Progress because the Daily Gift panel never got its last pass; public build 0.3.310.

OE 144  Create the sheet in Sheets (title free; it is for the folder from OE 5)
Expected: A new Google Sheet in Owen's Drive.

OE 145  Move the sheet into the DD bug carry-over folder in Drive (sheet from OE 144, folder from OE 5)
Expected: The sheet's parent is d_9b41e7c2a05d36f8e1c7a4 (DD bug carry-over).

OE 146  Write the rows to the sheet in Sheets (sheet from OE 144; outcomes from OE 30, tickets from OEs 32 to 99)
Expected: Header Bug, Outcome, Ticket, Why (OE 2), then 70 rows, one per bug: its line or post, its outcome (58 Fixed, 7 Broken, 3 Gone, 2 Covered), its ticket (the new issue's key, or ENG-2073 and ENG-2363 for the two Covered lines) and why (the record from OEs 8 to 29).

OE 147  Share the sheet with Arthur Blake in Drive (address from OE 6)
Expected: arthur.blake@harmonygames.co can open the sheet (writer, commenter or reader).

OE 148  Share the sheet with Robert in Drive (address from OE 6)
Expected: robert@harmonygames.co can open the sheet (writer, commenter or reader).

OE 149  Share the sheet with Oliver Brooks in Drive (address from OE 6)
Expected: oliver.brooks@harmonygames.co can open the sheet (writer, commenter or reader).

OE 150  Reply to Arthur in the thread of his DM in Slack (the DM and message from OE 1, after every other write)
Expected: A reply in that thread (thread_ts 1770937805.214409) with the numbers he asked for: 9 still broken (7 Broken plus 2 Covered, OE 2's report-back rule), 68 new tickets filed, 23 of the 28 UI children Done.
