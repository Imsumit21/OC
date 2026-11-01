OE 1  Read Arthur's sign-off ask in Douglas's Slack DM with Arthur (latest messages before Oct 1 2025)
        Expected: Arthur, Tue Sep 30 2025 2:12 PM PT (21:12 UTC): "for thursday's go/no-go i need the server side of the beta sign-off from you. the rules are on the beta card on the roadmap board. reply here when it's done with how many tickets are on prod and which ones aren't". It is the newest message in the DM.

OE 2  Find the beta card on the ZM ROADMAP Trello board and open it (Trello search "Beta sign-off")
        Expected: Card "Beta sign-off - server side" in the list "BETA: Oct 10": "For the Oct 10 beta. Douglas owns this one." Rule 1: ZOM tickets moved to Done after the beta prod cut (the first row of Douglas's deploy log) through Sep 30 whose fix needed a server change; a server change is a match3d-backend PR, or a change made straight in the Nakama console and logged in the deploy log; client-only fixes are out; parent tickets don't get a row. Rule 2: one row per ticket: ticket, server change(s), on prod (Y/N). Rule 3: on prod means what the match3d-backend prod deploys doc says; merged is not on prod. Rule 4: a ticket with more than one server change is on prod only if all of them are. Rule 5: anything not on prod goes back to Todo with a comment saying which change still has to go out; same ticket, no new ones. Rule 6: the register goes in the sign-off folder named on the ZM Beta page in Confluence. The card has 1 comment. Trap: "Beta sign-off - client side" on the same list is Oliver's card (In Validation, client QA folder) and does not govern the server side.

OE 3  Read the comment on that card (Trello card actions / comments of "Beta sign-off - server side")
        Expected: One comment, Tue Sep 30 2025 8:05 AM PT (15:05 UTC): "adding to rule 1: spreadsheet imports on the backend count as server changes too, same as console changes. they're in the deploy log. rest of the card stands."

OE 4  Open the ZM Beta page in Confluence named by rule 6 (Confluence text search "beta")
        Expected: Page "Zombie Match 3D beta - Oct 10" (space OPS, author user_EMPLOYEE_0025), created Mon Sep 29 2025 10:15 AM PT (17:15 UTC): "Beta on Oct 10. Go/no-go on Thursday Oct 2." "Sign-off: client side (Oliver) and server side (Douglas), rules on the ZM ROADMAP board, BETA: Oct 10 list." "Sign-off folder: ZM Beta sign-off (Drive, Arthur's). Client QA keeps its own folder."

OE 5  Read the comments on that page (Confluence page comments of "Zombie Match 3D beta - Oct 10")
        Expected: Comment by user_EMPLOYEE_0003, Tue Sep 30 2025 3:12 AM PT (10:12 UTC): "QA on prod this morning: the infinite HP boss still runs on the old HP values. Is the server side of ZOM-487 out?" Reply to it by user_EMPLOYEE_0025 (the page's author), 4:03 AM PT (11:03 UTC): "#48 is on prod, but the boss HP values come from the boss arena HP table, and that import is part of ZOM-487's server change too. Douglas has it in the deploy log."

OE 6  Find Arthur's sign-off folder in Drive (Drive search "ZM Beta sign-off")
        Expected: Folder "ZM Beta sign-off", owner arthur.blake@harmonygames.co, Douglas, Oliver and Vincent are writers. Trap: "ZM Beta sign-off - client QA" is Oliver's client QA folder (Douglas is only a reader) and is not the sign-off folder the page names.

OE 7  Read the match3d-backend prod deploys doc named by rule 3 (Drive search "prod deploys", then read the Google Doc "match3d-backend - prod deploys")
        Expected: Douglas's own doc. Merging doesn't deploy anything; prod runs from the prod branch and only the PRs picked onto prod are on prod. Whoever deploys a PR to prod comments on it with a line starting "prod:", the time in UTC and the task definition; that comment is what puts the PR on prod, not the merge and not a Slack message. A prod deploy only counts if the PR already had an Approve review from someone other than its author when it went out; approving afterwards doesn't fix it, redeploy. A "rollback:" comment takes the PR off prod, freeze or not, until a newer "prod:" comment. Console changes and spreadsheet imports have no PR: they go in the deploy log, Console & imports tab, with the target (dev or prod) and the time. Freezes: from the server freeze on the calendar until the beta ships, the Approve review has to be Arthur's; anything else deployed during the freeze gets rolled back at go/no-go. The Prod deploys tab of the deploy log is only a quick list.

OE 8  Find the server freeze on Douglas's calendar (Google Calendar search "server freeze")
        Expected: Event "ZM beta - server freeze", organizer arthur.blake@harmonygames.co, starts Fri Sep 26 2025 3:00 PM PT (22:00 UTC), ends 3:30 PM PT. Description: "Pulled in from Monday so QA gets the weekend on a frozen prod." So the freeze runs from Sep 26 22:00 UTC.

OE 9  Read both tabs of Douglas's deploy log (Drive search "deploy log", then the spreadsheet "match3d-backend deploy log", tabs "Prod deploys" and "Console & imports")
        Expected: Prod deploys, first row: 2025-08-25 11:52 UTC, "beta prod cut: prod branch from main (#37, #38)", zm-api:41; this is the beta prod cut (Mon Aug 25 2025 4:52 AM PT). The tab's last row is 2025-09-10 18:20 (#45). Console & imports (UTC, type, what, target): 2025-08-26 10:30 import plague race table dev; 2025-08-28 17:05 console plague race bot names prod; 2025-09-02 18:05 import trophy path copy table dev; 2025-09-08 16:45 import Zombie Lane rewards prod; 2025-09-10 17:40 import loadout table dev; 2025-09-11 16:30 import algo levels 2.0 level pack dev; 2025-09-12 19:20 import analytics events table dev; 2025-09-16 14:20 import economy table dev; 2025-09-17 15:50 import boss arena HP table dev.

OE 10  Find Leonard's go/no-go email in Douglas's Gmail (Gmail search "from:leonard")
        Expected: The results include Leonard's Sep 30 message, in thread douglas@harmonygames.co/1844721277206562572.

OE 11  Open that whole thread (Gmail thread douglas@harmonygames.co/1844721277206562572)
        Expected: The thread holds 2 messages. The first: Leonard Hayes (leonard.hayes@harmonygames.co) to Douglas, cc Arthur, Tue Sep 30 2025 1:15 PM PT (20:15 UTC), subject "beta go/no-go thursday": "For Thursday's go/no-go: once your server register is in the beta folder, please share it with me directly. Comment access please, I don't need to edit, I'll leave my notes on it before the call." The second is Arthur's reply-all to Douglas, cc Leonard, Tue Sep 30 2025 1:41 PM PT (20:41 UTC), subject "Re: beta go/no-go thursday": "Two things for the register before Leonard gets it. First, leave ZOM-547 and ZOM-553 off. The boss arena balance and refill/nuke values players get come from the client's balance sheet; the backend copies (match3d-backend#49 and #53) are only mirrors. They're not part of the count either way. Second, two of the imports in your deploy log are server changes for tickets whose comments don't say so: the analytics events table import is part of the server change for ZOM-444 and ZOM-436, and the loadout table import is part of ZOM-531's. Both are still only on dev. Rest of the card stands."

OE 12  List the ZOM team's Done tickets in Linear and keep those completed after the beta prod cut (2025-08-25 11:52 UTC) through Sep 30 (Linear issues, team ZOM, state Done, paging through all results; the list call has no completion-date filter, so filter the listed results on completedAt)
        Expected: 73 tickets: ZOM-459, ZOM-457, ZOM-447, ZOM-474, ZOM-470, ZOM-464, ZOM-497, ZOM-486, ZOM-495, ZOM-496, ZOM-501, ZOM-485, ZOM-466, ZOM-332, ZOM-127, ZOM-265, ZOM-338, ZOM-340, ZOM-335, ZOM-336, ZOM-331, ZOM-339, ZOM-337, ZOM-502, ZOM-476, ZOM-392, ZOM-509, ZOM-518, ZOM-510, ZOM-519, ZOM-256, ZOM-540, ZOM-531, ZOM-512, ZOM-537, ZOM-444, ZOM-515, ZOM-493, ZOM-491, ZOM-463, ZOM-383, ZOM-436, ZOM-421, ZOM-525, ZOM-523, ZOM-524, ZOM-499, ZOM-478, ZOM-547, ZOM-511, ZOM-487, ZOM-530, ZOM-500, ZOM-527, ZOM-550, ZOM-435, ZOM-434, ZOM-507, ZOM-169, ZOM-503, ZOM-473, ZOM-419, ZOM-239, ZOM-506, ZOM-538, ZOM-112, ZOM-558, ZOM-536, ZOM-498, ZOM-555, ZOM-553, ZOM-557, ZOM-561. Boundary: ZOM-459 completed 2025-08-25 11:53:11 UTC (in); ZOM-461 completed 11:51:48 UTC, before the cut (out). ZOM-457 "Algo Level Issues" is a parent ticket (it is ZOM-459's parent), so it gets no row (rule 1).

OE 13  Read the comments on each of the 73 tickets to find which fixes needed a server change (Linear comments, one ticket at a time)
        Expected: Each ticket has one comment. A server change is named on 18 of them: ZOM-459 "backend part is match3d-backend#38"; ZOM-509 "backend part is match3d-backend#39"; ZOM-336 "needs a catalog entry on the backend too: match3d-backend#40"; ZOM-392 "backend part match3d-backend#41"; ZOM-503 "backend parts are match3d-backend#42 (ack) and match3d-backend#52 (refresh push)"; ZOM-518 "backend part is match3d-backend#43"; ZOM-499 "that part is match3d-backend#44"; ZOM-531 "backend part match3d-backend#45"; ZOM-537 "new values are in match3d-backend#46"; ZOM-444 "the backend logs endless_start too now: match3d-backend#47"; ZOM-487 "served by the backend: match3d-backend#48"; ZOM-550 "backend part match3d-backend#50"; ZOM-435 "backend part is match3d-backend#51"; ZOM-557 "the streak count itself is on the backend: match3d-backend#54"; ZOM-510 "fix is the Zombie Lane rewards import on the backend"; ZOM-256 "needs the level pack imported on the backend"; ZOM-547 "backend copy in match3d-backend#49"; ZOM-553 "backend copy in match3d-backend#53". ZOM-436's comment is "tested on device with 0.3.122, looks good"; ZOM-457's is "parent for the algo level bugs, the fixes are on the child tickets". The other 53 comments name no match3d-backend PR, console change or import (client, art, VFX, editor, tool or device-test notes such as "client only, checked on 0.3.103" and "vfx done, nothing needed in match3d-backend").

OE 14  Work out the register's ticket set from rule 1, the card comment and Arthur's reply-all (calculation over the results of OE 2, 3, 11, 12 and 13)
        Expected: 17 tickets: ZOM-459, ZOM-509, ZOM-336, ZOM-392, ZOM-503, ZOM-518, ZOM-499, ZOM-531, ZOM-537, ZOM-444, ZOM-487, ZOM-550, ZOM-435, ZOM-557, ZOM-510 and ZOM-256 (server change named in the comment; ZOM-510 and ZOM-256 by import, counted through the card comment), plus ZOM-436 (the analytics events table import, from the reply-all). Left out: ZOM-547 and ZOM-553 (reply-all), ZOM-457 (parent), and the 53 client-only tickets.

OE 15  Find the backend repository in GitHub (repository search "match3d-backend")
        Expected: harmonygames-Games/match3d-backend.

OE 16  Check whether match3d-backend#38 (ZOM-459) is on prod: read its conversation comments, its reviews and its inline review comments (GitHub, harmonygames-Games/match3d-backend, PR #38)
        Expected: "Plague race: count algo levels", author PERSON_5760_GITHUB_USERNAME. Reviews: APPROVED by PERSON_2967_GITHUB_USERNAME 2025-08-25 09:20 UTC. Comments: "prod: 2025-08-25 11:52 UTC, zm-api:41". Inline review comment by PERSON_2967_GITHUB_USERNAME on lib/zombies_game/plague_race.ex, 2025-08-25 09:20 UTC: "looks right. one thing: standings come from the plague race table now, so 459 also needs the plague race table import on the backend. that import is part of 459's server change, the count won't change on prod without it". #38 is on prod; the plague race table import is only on dev (deploy log 2025-08-26 10:30), so ZOM-459 is not on prod.

OE 17  Check whether match3d-backend#39 (ZOM-509) is on prod: read its conversation comments, its reviews and its inline review comments (GitHub, harmonygames-Games/match3d-backend, PR #39)
        Expected: "Trophy path: container headlines config", author PERSON_2967_GITHUB_USERNAME. Reviews: APPROVED by PERSON_5760_GITHUB_USERNAME 2025-09-02 15:20 UTC. Comments: "prod: 2025-09-02 17:30 UTC, zm-api:42". Inline review comment by PERSON_5760_GITHUB_USERNAME on lib/zombies_game/trophy_path.ex, 2025-09-02 15:20 UTC: "approving. note for whoever ships it: the headlines and subtext come from the trophy path copy table now, so 509 needs that table imported on the backend too. the import is part of 509's server change". #39 is on prod; the trophy path copy table import is only on dev (2025-09-02 18:05), so ZOM-509 is not on prod.

OE 18  Check whether match3d-backend#40 (ZOM-336) is on prod: read its conversation comments, its reviews and its inline review comments (GitHub, harmonygames-Games/match3d-backend, PR #40)
        Expected: "Catalog: add usable item entries", author PERSON_2967_GITHUB_USERNAME. Reviews: only an automated COMMENTED review by PERSON_6026_GITHUB_USERNAME ("Actionable comments posted: 0"), no Approve. Comments: "on dev for Vincent to try (2025-09-02 18:40 UTC)"; no "prod:" comment. No inline review comments. Not on prod.

OE 19  Check whether match3d-backend#41 (ZOM-392) is on prod: read its conversation comments, its reviews and its inline review comments (GitHub, harmonygames-Games/match3d-backend, PR #41)
        Expected: "Algo levels 100+: seed endpoint", author PERSON_5760_GITHUB_USERNAME. Comments: "prod: 2025-09-03 16:30 UTC, zm-api:43". Reviews: APPROVED by PERSON_2967_GITHUB_USERNAME 2025-09-03 18:05 UTC, after the prod deploy. No inline review comments. The deploy does not count; not on prod.

OE 20  Check whether match3d-backend#42 (ZOM-503 (first change)) is on prod: read its conversation comments, its reviews and its inline review comments (GitHub, harmonygames-Games/match3d-backend, PR #42)
        Expected: "Teams: ack lives gift", author PERSON_5760_GITHUB_USERNAME. Reviews: APPROVED by PERSON_2967_GITHUB_USERNAME 2025-09-05 15:30 UTC. Comments: "prod: 2025-09-08 17:18 UTC, zm-api:45". No inline review comments. On prod.

OE 21  Check whether match3d-backend#43 (ZOM-518) is on prod: read its conversation comments, its reviews and its inline review comments (GitHub, harmonygames-Games/match3d-backend, PR #43)
        Expected: "Inventory: drop non-card items from equipped", author PERSON_2967_GITHUB_USERNAME. Comments: "prod: 2025-09-04 12:50 UTC, zm-api:44". Reviews: only an automated COMMENTED review by PERSON_6026_GITHUB_USERNAME ("Actionable comments posted: 0"), no Approve from anyone. No inline review comments. The deploy does not count; not on prod.

OE 22  Check whether match3d-backend#44 (ZOM-499) is on prod: read its conversation comments, its reviews and its inline review comments (GitHub, harmonygames-Games/match3d-backend, PR #44)
        Expected: "Profile: other players profile v2", author PERSON_2967_GITHUB_USERNAME. Reviews: CHANGES_REQUESTED by PERSON_5760_GITHUB_USERNAME 2025-09-05 16:00 UTC, then APPROVED by PERSON_5760_GITHUB_USERNAME 2025-09-08 15:10 UTC. Comments: "prod: 2025-09-08 17:18 UTC, zm-api:45"; "rollback: 2025-09-20 02:00 UTC, pick reverted, zm-api:50. profile endpoint 500s for players on old clients"; "prod: 2025-09-22 17:30 UTC, zm-api:51" (before the freeze). No inline review comments. On prod.

OE 23  Check whether match3d-backend#45 (ZOM-531) is on prod: read its conversation comments, its reviews and its inline review comments (GitHub, harmonygames-Games/match3d-backend, PR #45)
        Expected: "Inventory: keep equipped slots across sessions", author PERSON_5760_GITHUB_USERNAME. Reviews: CHANGES_REQUESTED by PERSON_2967_GITHUB_USERNAME 2025-09-09 17:00 UTC, then APPROVED by PERSON_2967_GITHUB_USERNAME 2025-09-10 15:10 UTC. Comments: "prod: 2025-09-10 18:20 UTC, zm-api:47". No inline review comments. #45 is on prod; ZOM-531's loadout table import is only on dev (reply-all; deploy log 2025-09-10 17:40), so ZOM-531 is not on prod.

OE 24  Check whether match3d-backend#46 (ZOM-537) is on prod: read its conversation comments, its reviews and its inline review comments (GitHub, harmonygames-Games/match3d-backend, PR #46)
        Expected: "Economy: September adjustments", author PERSON_5760_GITHUB_USERNAME. Reviews: APPROVED by EMPLOYEE_0025_GITHUB_USERNAME 2025-09-09 19:40 UTC. Comments: "prod: 2025-09-09 20:29 UTC, zm-api:46". Inline review comment by EMPLOYEE_0025_GITHUB_USERNAME on lib/zombies_game/economy.ex, 2025-09-09 19:40 UTC: "code's fine. heads up though, these now read from the economy table, so 537 also needs the economy table import on the backend. that import is part of 537's server change, the values aren't live without it". #46 is on prod; the economy table import is only on dev (2025-09-16 14:20), so ZOM-537 is not on prod.

OE 25  Check whether match3d-backend#47 (ZOM-444) is on prod: read its conversation comments, its reviews and its inline review comments (GitHub, harmonygames-Games/match3d-backend, PR #47)
        Expected: "Analytics: log endless_start on the server", author PERSON_2967_GITHUB_USERNAME. Reviews: APPROVED by EMPLOYEE_0025_GITHUB_USERNAME 2025-09-27 16:05 UTC. Comments: "prod: 2025-09-27 16:20 UTC, zm-api:55" (inside the freeze, after that Approve). No inline review comments. Whether #47 counts turns on who EMPLOYEE_0025_GITHUB_USERNAME is (OE 31). ZOM-444 is not on prod either way, because its analytics events table import is only on dev (reply-all; 2025-09-12 19:20).

OE 26  Check whether match3d-backend#48 (ZOM-487) is on prod: read its conversation comments, its reviews and its inline review comments (GitHub, harmonygames-Games/match3d-backend, PR #48)
        Expected: "Boss arena: infinite HP event config", author PERSON_2967_GITHUB_USERNAME. Reviews: APPROVED by PERSON_5760_GITHUB_USERNAME 2025-09-16 15:20 UTC. Comments: "prod: 2025-09-16 16:35 UTC, zm-api:48". No inline review comments. #48 is on prod; ZOM-487's boss arena HP table import is only on dev (page reply; 2025-09-17 15:50), so ZOM-487 is not on prod.

OE 27  Check whether match3d-backend#50 (ZOM-550) is on prod: read its conversation comments, its reviews and its inline review comments (GitHub, harmonygames-Games/match3d-backend, PR #50)
        Expected: "Boss arena: don't take a life on a win", author PERSON_2967_GITHUB_USERNAME. Reviews: APPROVED by PERSON_5760_GITHUB_USERNAME 2025-09-19 15:10 UTC; COMMENTED by EMPLOYEE_0025_GITHUB_USERNAME 2025-09-29 14:50 UTC: "looks fine, ship it after go/no-go" (not an Approve). Comments: "prod: 2025-09-27 14:30 UTC, zm-api:54", inside the freeze; the only Approve is by PERSON_5760_GITHUB_USERNAME. No inline review comments. Not on prod.

OE 28  Check whether match3d-backend#51 (ZOM-435) is on prod: read its conversation comments, its reviews and its inline review comments (GitHub, harmonygames-Games/match3d-backend, PR #51)
        Expected: "Trophy path: ignore duplicate claim requests", author PERSON_5760_GITHUB_USERNAME. Reviews: APPROVED by PERSON_2967_GITHUB_USERNAME 2025-09-19 21:30 UTC. Comments: "on dev for Vincent to try (2025-09-19 22:20 UTC)" and "works on dev, double tapping claim only counts once now"; no "prod:" comment. No inline review comments. Not on prod.

OE 29  Check whether match3d-backend#52 (ZOM-503 (second change)) is on prod: read its conversation comments, its reviews and its inline review comments (GitHub, harmonygames-Games/match3d-backend, PR #52)
        Expected: "Teams: push lives refresh to client", author PERSON_5760_GITHUB_USERNAME. Reviews: APPROVED by PERSON_2967_GITHUB_USERNAME 2025-09-22 14:50 UTC (the only Approve). Comments: "prod: 2025-09-30 18:16 UTC, zm-api:57", inside the freeze; the only Approve is by PERSON_2967_GITHUB_USERNAME. No inline review comments. Not on prod, so ZOM-503 is not on prod (rule 4; #42 alone is not enough).

OE 30  Check whether match3d-backend#54 (ZOM-557) is on prod: read its conversation comments, its reviews and its inline review comments (GitHub, harmonygames-Games/match3d-backend, PR #54)
        Expected: "Login streak: count days in player timezone", author PERSON_5760_GITHUB_USERNAME. Reviews: APPROVED by PERSON_2967_GITHUB_USERNAME 2025-09-23 15:20 UTC. Comments: "prod: 2025-09-24 19:00 UTC, zm-api:53"; "rollback: 2025-09-28 03:10 UTC, pick reverted, zm-api:56. streak resets for players east of UTC"; no later "prod:" comment. No inline review comments. Not on prod.

OE 31  Check who the reviewer EMPLOYEE_0025_GITHUB_USERNAME is, for the freeze rule (GitHub user lookup of EMPLOYEE_0025_GITHUB_USERNAME, the reviewer on #46, #47 and #50)
        Expected: EMPLOYEE_0025_GITHUB_USERNAME is Arthur Blake, arthur.blake@harmonygames.co. So #47's in-freeze deploy has Arthur's Approve and counts; #50 and #52 went out in the freeze without Arthur's Approve and do not count.

OE 32  Decide each register row from rules 2 to 4, the doc, the freeze, the deploy log and the amendments (calculation over OE 5, 7 to 9, 11, 13, 14 and 16 to 31)
        Expected: 17 rows (ticket, server change(s), on prod): ZOM-459, #38 + plague race table import, N. ZOM-509, #39 + trophy path copy table import, N. ZOM-336, #40, N. ZOM-392, #41, N. ZOM-503, #42 + #52, N. ZOM-518, #43, N. ZOM-499, #44, Y. ZOM-531, #45 + loadout table import, N. ZOM-537, #46 + economy table import, N. ZOM-444, #47 + analytics events table import, N. ZOM-487, #48 + boss arena HP table import, N. ZOM-550, #50, N. ZOM-435, #51, N. ZOM-557, #54, N. ZOM-510, Zombie Lane rewards import (prod 2025-09-08 16:45), Y. ZOM-256, algo levels 2.0 level pack import, N. ZOM-436, analytics events table import, N. On prod: 2 (ZOM-499, ZOM-510). Not on prod: 15.

OE 33  Create the register as a Google Sheet inside the "ZM Beta sign-off" folder (Drive: create one Google Sheets file with the "ZM Beta sign-off" folder as its parent and the 17 rows as its content; any title)
        Expected: A new Google Sheet in "ZM Beta sign-off" with the columns ticket, server change(s), on prod (Y/N) and the 17 rows of OE 32.

OE 34  Share the register with Leonard, as his email asked (Drive share of the register file: leonard.hayes@harmonygames.co, role commenter, type user)
        Expected: Leonard has comment access on the register file itself.

OE 35  Check that the ZOM team has a Todo state to move the tickets back to (Linear issue statuses, team ZOM)
        Expected: "Todo" exists for team ZOM, beside Backlog, In Progress, In Validation, Regression, Done, Canceled and Duplicate.

OE 36  Move ZOM-336 back to Todo, per rule 5 (Linear update of ZOM-336: state Todo)
        Expected: ZOM-336 moves from Done to Todo.

OE 37  Comment on ZOM-336 with the change still to go out, per rule 5 (Linear comment on ZOM-336)
        Expected: A new comment on ZOM-336 saying #40 (only on dev) still has to go out to prod.

OE 38  Move ZOM-392 back to Todo, per rule 5 (Linear update of ZOM-392: state Todo)
        Expected: ZOM-392 moves from Done to Todo.

OE 39  Comment on ZOM-392 with the change still to go out, per rule 5 (Linear comment on ZOM-392)
        Expected: A new comment on ZOM-392 saying #41 has to be redeployed to prod, because its Approve came after the Sep 3 deploy.

OE 40  Move ZOM-503 back to Todo, per rule 5 (Linear update of ZOM-503: state Todo)
        Expected: ZOM-503 moves from Done to Todo.

OE 41  Comment on ZOM-503 with the change still to go out, per rule 5 (Linear comment on ZOM-503)
        Expected: A new comment on ZOM-503 saying #52 still has to go out with Arthur's Approve (it went out during the freeze without one).

OE 42  Move ZOM-518 back to Todo, per rule 5 (Linear update of ZOM-518: state Todo)
        Expected: ZOM-518 moves from Done to Todo.

OE 43  Comment on ZOM-518 with the change still to go out, per rule 5 (Linear comment on ZOM-518)
        Expected: A new comment on ZOM-518 saying #43 still has to go out to prod: its 2025-09-04 12:50 UTC deploy had no Approve review, and with the server freeze on it now needs Arthur's Approve before it is redeployed.

OE 44  Move ZOM-550 back to Todo, per rule 5 (Linear update of ZOM-550: state Todo)
        Expected: ZOM-550 moves from Done to Todo.

OE 45  Comment on ZOM-550 with the change still to go out, per rule 5 (Linear comment on ZOM-550)
        Expected: A new comment on ZOM-550 saying #50 still has to go out with Arthur's Approve (it went out during the freeze without one).

OE 46  Move ZOM-435 back to Todo, per rule 5 (Linear update of ZOM-435: state Todo)
        Expected: ZOM-435 moves from Done to Todo.

OE 47  Comment on ZOM-435 with the change still to go out, per rule 5 (Linear comment on ZOM-435)
        Expected: A new comment on ZOM-435 saying #51 (only on dev) still has to go out to prod.

OE 48  Move ZOM-557 back to Todo, per rule 5 (Linear update of ZOM-557: state Todo)
        Expected: ZOM-557 moves from Done to Todo.

OE 49  Comment on ZOM-557 with the change still to go out, per rule 5 (Linear comment on ZOM-557)
        Expected: A new comment on ZOM-557 saying #54 was rolled back (2025-09-28 03:10 UTC) and still has to go out to prod again.

OE 50  Move ZOM-256 back to Todo, per rule 5 (Linear update of ZOM-256: state Todo)
        Expected: ZOM-256 moves from Done to Todo.

OE 51  Comment on ZOM-256 with the change still to go out, per rule 5 (Linear comment on ZOM-256)
        Expected: A new comment on ZOM-256 saying the algo levels 2.0 level pack import (only on dev) still has to go out to prod.

OE 52  Move ZOM-487 back to Todo, per rule 5 (Linear update of ZOM-487: state Todo)
        Expected: ZOM-487 moves from Done to Todo.

OE 53  Comment on ZOM-487 with the change still to go out, per rule 5 (Linear comment on ZOM-487)
        Expected: A new comment on ZOM-487 saying the boss arena HP table import (only on dev) still has to go out to prod.

OE 54  Move ZOM-537 back to Todo, per rule 5 (Linear update of ZOM-537: state Todo)
        Expected: ZOM-537 moves from Done to Todo.

OE 55  Comment on ZOM-537 with the change still to go out, per rule 5 (Linear comment on ZOM-537)
        Expected: A new comment on ZOM-537 saying the economy table import (only on dev) still has to go out to prod.

OE 56  Move ZOM-444 back to Todo, per rule 5 (Linear update of ZOM-444: state Todo)
        Expected: ZOM-444 moves from Done to Todo.

OE 57  Comment on ZOM-444 with the change still to go out, per rule 5 (Linear comment on ZOM-444)
        Expected: A new comment on ZOM-444 saying the analytics events table import (only on dev) still has to go out to prod.

OE 58  Move ZOM-531 back to Todo, per rule 5 (Linear update of ZOM-531: state Todo)
        Expected: ZOM-531 moves from Done to Todo.

OE 59  Comment on ZOM-531 with the change still to go out, per rule 5 (Linear comment on ZOM-531)
        Expected: A new comment on ZOM-531 saying the loadout table import (only on dev) still has to go out to prod.

OE 60  Move ZOM-459 back to Todo, per rule 5 (Linear update of ZOM-459: state Todo)
        Expected: ZOM-459 moves from Done to Todo.

OE 61  Comment on ZOM-459 with the change still to go out, per rule 5 (Linear comment on ZOM-459)
        Expected: A new comment on ZOM-459 saying the plague race table import (only on dev) still has to go out to prod.

OE 62  Move ZOM-509 back to Todo, per rule 5 (Linear update of ZOM-509: state Todo)
        Expected: ZOM-509 moves from Done to Todo.

OE 63  Comment on ZOM-509 with the change still to go out, per rule 5 (Linear comment on ZOM-509)
        Expected: A new comment on ZOM-509 saying the trophy path copy table import (only on dev) still has to go out to prod.

OE 64  Move ZOM-436 back to Todo, per rule 5 (Linear update of ZOM-436: state Todo)
        Expected: ZOM-436 moves from Done to Todo.

OE 65  Comment on ZOM-436 with the change still to go out, per rule 5 (Linear comment on ZOM-436)
        Expected: A new comment on ZOM-436 saying the analytics events table import (only on dev) still has to go out to prod.

OE 66  Reply to Arthur in Douglas's DM with Arthur with what he asked for (Slack message in that DM, as a new message or under his Sep 30 ask)
        Expected: Message posted in the DM: 2 of the 17 tickets are on prod (ZOM-499, ZOM-510), and the 15 not on prod are ZOM-336, ZOM-392, ZOM-503, ZOM-518, ZOM-550, ZOM-435, ZOM-557, ZOM-256, ZOM-487, ZOM-537, ZOM-444, ZOM-531, ZOM-459, ZOM-509 and ZOM-436.
