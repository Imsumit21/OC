OE 1  Read Leonard's ask in #winddown, the newest message before the clock (Slack: find the channel "winddown", read its latest messages)
        Expected: Leonard, Fri Feb 13 2026 17:21 UTC (Fri Feb 13, 9:21 AM PT): "<@EMPLOYEE_0016_SLACK_ID> can you own the account close-out register before I archive anything on Google? Arthur put our accounts into the Linear shutdown project yesterday. I need one sheet with every account: what we do with it, where it stands, by when, who does it and what it costs us a month - share it with me and Arthur as editors. Go by my keep list from yesterday and the reply under it, Arthur's moves to his LLC card, Sunset's data checklist, SVB's card terms and the conventions doc I just put in the Wind Down folder. Settle each Linear issue as you go and leave a line on each, then reply here with the two monthly totals and anything in the plan that clashes with what we already decided." It has no replies yet.

OE 2  Page back through #winddown to Leonard's keep list from Feb 12 and read its thread (Slack: the same #winddown history OE 1 reads; the keep list is a few messages back on that first page; then open its thread replies)
        Expected: Leonard, Thu Feb 12 2026 22:00 UTC: "During shutdown, let's keep Deel, gusto, Intuit. I canceled other subscriptions under mine. ..." One reply, Arthur, Fri Feb 13 2026 02:14 UTC: "gusto pulls its invoice from the bank on the 3rd. i pulled every doc and 1099 out of it tonight so we don't need it anymore - let's cancel before mar 3" So Gusto comes off the keep list: Cancel (its by-when comes from the SVB card comment, OE 11).

OE 3  Read Arthur's card-move message and Leonard's Feb 12 action items in #winddown (same channel history)
        Expected: Arthur, Thu Feb 12 2026 23:00 UTC: "I'll be moving github, [USERNAME_30019], and Metabase to my KubLLC card." Leonard, Thu Feb 12 2026 22:05 UTC: action items including "archieve account on google after Feb 15" and "I think we keep Metabase and dbt" (so the redacted name in Arthur's message is dbt).

OE 4  Read the Feb 11 Slack plan and Leonard's Feb 12 subscriptions checklist in #winddown, including the table inside the message's attachment (channel history paged back to Feb 11; read attachments, not only text)
        Expected: Leonard Wed Feb 11 2026 19:57 UTC: "For Slack, should I just go back to free version with no history?" Arthur Wed Feb 11 2026 20:00 UTC: "yeah free version". Leonard Wed Feb 11 2026 20:34 UTC: "I guess I'll keep only a few accounts active and turn people into guest accounts", then Wed Feb 11 2026 20:40 UTC: "let me do that". Leonard Thu Feb 12 2026 21:57 UTC, "latest and greatest on subscriptions": the attached checklist table marks "[x] Slack (down to 3 FT members)" done. These are decisions on record about Slack's plan and users.

OE 5  Find and read the conventions doc Leonard names (Drive search "Close-out register conventions", then read the Google Doc)
        Expected: Doc "Close-out register conventions" in the Wind Down folder, shared with Leonard, Arthur and Robert, modified Feb 13 2026 16:58 UTC: "Close-out register conventions 1. One row per vendor account. If the same vendor shows up twice (two issues, two names), it's one row under the name on its invoice, and the newer issue is the duplicate. 2. Leave out people, contractors and professional firms (legal, accounting, Sunset), taxes and filing services, insurance, bank fees, one-off purchases, anything the company itself never paid for, and anything cancelled before Feb 9. Exception: anything on Sunset's list goes on the register whatever else applies. 3. Arthur's project came from the P&L and our lists; he skipped one-off, filing and insurance lines and ones long gone. AWS and the ad accounts in the UA line stay off the register: he and I are closing those out ourselves. Before you call it complete, add what it misses inside any other costs-tab line that covers several vendors - each account there gets its own row. 4. What we do: Cancel, Keep (my keep list, as amended in the thread), Move to Arthur's LLC (his card), or Hold for Sunset. Sunset's list wins over everything above. 5. Where it stands, for Cancel rows only: Closed = the vendor itself has confirmed (their email, an in-app or bot notice, a final invoice) - say where. Requested = one of us has cancelled or asked but nothing has come back from the vendor. Open = nobody has done anything yet. Leave it blank on the other rows. 6. By when: for Cancel rows that aren't Closed, the day before the next charge (for accounts billed on usage - ads, cloud - use Feb 28), or the SVB card on the founders' board if it sets an earlier date. For Keep and Hold rows still charging the SVB card while we need them, follow SVB's card terms. Hold rows already off that card, or that won't charge it again before Sunset's review call, stay until the review call; Keep rows that aren't on the SVB card get a dash. Moved and Closed rows get a dash, unless an export or a switch-over still has to happen before the access ends - then the day before it ends. 7. Owner: the Linear assignee unless the issue hands it to someone else. Anything you add is yours. 8. Monthly cost, rounded to cents: the monthly figure its owner gives in its Linear issue, or else its own last invoice or receipt brought to a month (annual / 12, quarterly / 3). Free plans and accounts that have never charged us are 0. 9. Two totals at the bottom: the sum of the monthly cost column over every row (what it all costs us today), and the same sum over the Keep and Hold rows only (what's left after the plan). 10. A clash is a decision one of us already posted in #winddown that Sunset's list or SVB's card terms would undo. Moving who pays for an account isn't one (it closes nothing), and requests or suggestions aren't decisions."

OE 6  Find the Linear project Leonard's ask points to and read its description (Linear: list projects, open the one named Shutdown, en dash, accounts)
        Expected: The project named "Shutdown", an en dash, then "accounts" (team ENG, lead Arthur, created Feb 12 2026 23:24 UTC): "One issue per vendor we still pay or only recently stopped, taken from the January P&L costs tab, old receipts and the #winddown lists. I skipped the costs-tab lines that were one-off buys, filings and insurance, or already dead. This replaces my subscriptions sheet from Tuesday. A few costs-tab lines are filed under other names: the $6,250 one is Singular and the hosting one is GitHub; the two $30 game-ops lines I'm handling myself, so they're not in here. AWS and the ad accounts in the UA line aren't in here either: I'm shutting AWS down myself once the store transfer is done, and Leonard is closing the ad networks directly. Settle them as you go: Done once the account counts as closed in the register (access can run out later), Canceled if it doesn't belong on the list, everything else stays open - and leave a comment on each with what happens and by when."

OE 7  List the project's issues (Linear issues filtered to the project)
        Expected: 28 issues, ENG-2438 to ENG-2466 (there is no ENG-2445), all in Todo, created Feb 12 2026 by Arthur: ENG-2438 Unity (Arthur); ENG-2439 Helpshift (Leonard); ENG-2440 Soundly (Robert); ENG-2441 Linear (Arthur); ENG-2442 Figma (Robert); ENG-2443 Trello (Leonard); ENG-2444 Singular (Leonard); ENG-2446 Metabase (Arthur); ENG-2447 dbt (Arthur); ENG-2448 BigQuery (Arthur); ENG-2449 QuickBooks (Leonard); ENG-2450 Intuit (Leonard); ENG-2451 Carta (Leonard); ENG-2452 Google Workspace (Leonard); ENG-2453 Slack (Leonard); ENG-2454 iPostal (Leonard); ENG-2455 Gusto (Leonard); ENG-2456 Deel (Leonard); ENG-2457 Docusign (Leonard); ENG-2458 Layer (Leonard); ENG-2459 CodeRabbit (Arthur); ENG-2460 Cursor (Arthur); ENG-2461 Zapier (Leonard); ENG-2462 GitHub (Arthur); ENG-2463 Kapwing (Arthur); ENG-2464 1Password (Arthur); ENG-2465 Lucidchart (Arthur); ENG-2466 Google Ads (Leonard).

OE 8  Read the comments on every one of the 28 issues (Linear comments, one issue at a time; the issue list does not include comments)
        Expected: ENG-2438 Unity - Arthur: "sent unity the termination this morning, cc leonard. unity pro is 11 seats at $2,348.50 a month with tax, next invoice is the 19th"; ENG-2439 Helpshift - Oliver: "exported the full helpshift ticket history to the wind down folder today, it's helpshift_export_2026-02-13.zip. both games' support buttons now open email instead of helpshift" / Leonard: "helpshift wrote back that they're discontinuing us at the end of february. it's $150 a month"; ENG-2440 Soundly - Arthur: "robert cancelled this on the 11th per #winddown"; ENG-2441 Linear - Arthur: "linear is on standard, paid yearly. we paid $1,832.65 last august for the year to aug 21, it moves to basic at that renewal. the p&l stops after the 2024 payment"; ENG-2442 Figma - no comment; ENG-2443 Trello - no comment; ENG-2444 Singular - Leonard: "sent the termination on the singular billing thread yesterday. the next quarterly invoice is mar 1; mar 15 is only their extension on the old one"; ENG-2446 Metabase - Arthur: "metabase billing switched to the kubllc card, it's $148 a month"; ENG-2447 dbt - Arthur: "dbt is on the kubllc card now, same as github and metabase. $100 a month"; ENG-2448 BigQuery - Arthur: "google cloud charges my card on the 1st, not the svb one. it was $4.97 this month"; ENG-2449 QuickBooks - Leonard: "intuit takes the $115 off the svb card on the 4th"; ENG-2450 Intuit - Leonard: "same account as the quickbooks issue"; ENG-2451 Carta - Leonard: "the carta terminations this week were the contractor grants, the subscription itself is untouched. annual, $3,852 last august, renews aug 15"; ENG-2452 Google Workspace - Leonard: "workspace is on the svb card, this month's invoice was $298.13"; ENG-2453 Slack - Leonard: "slack renews on the 3rd, it's on the svb card. it was $87.22 this month"; ENG-2454 iPostal - no comment; ENG-2455 Gusto - Leonard: "gusto's january invoice was $116, they take it on the 3rd"; ENG-2456 Deel - Leonard: "deel gets paid by transfer from the bank account, nothing on a card. it's $300 a month"; ENG-2457 Docusign - Leonard: "docusign goes to robert from here. annual, $300, renews apr 20 (the p&l missed last april's charge)"; ENG-2458 Layer - Leonard: "cancelled it in the app on the 11th"; ENG-2459 CodeRabbit - Arthur: "cancelled. lite plan, 3 seats at $15"; ENG-2460 Cursor - Arthur: "cancelled in the dashboard. $40/mo, renews on the 5th"; ENG-2461 Zapier - Leonard: "cancelled zapier yesterday, their email says the plan runs until feb 27. it was $73.50 a month"; ENG-2462 GitHub - Arthur: "github is on the kubllc card now. it was $90 this month all in"; ENG-2463 Kapwing - Arthur: "cancelled with cursor. kapwing emailed to confirm, pro runs out later this month. it was $24 a month"; ENG-2464 1Password - Arthur: "everyone's logins live here, cancel it last. $19.95 a month, renews on the 8th"; ENG-2465 Lucidchart - no comment; ENG-2466 Google Ads - no comment.

OE 9  Find Sunset's data checklist in Robert's Gmail and read the whole thread (Gmail search "data delivery checklist", then the thread)
        Expected: Thread whose subject is "Harmony Games", an en dash, then "data delivery checklist", from Maya at Sunset to Leonard, Robert and Arthur. First message Feb 12 2026 23:58 UTC: "Hi Leonard, Robert, Arthur, Thanks for signing today. Before we can deliver the licensed data set, these accounts need to stay active with their full history and every user in place until we confirm delivery: Slack (stay on the paid plan - the free plan hides history older than 90 days), Google Workspace (every user account, including former staff - please don't archive or delete any), Figma, Linear, GitHub and Metabase. Nothing on this list should be closed, downgraded or archived before the delivery review call Leonard booked with us. Accounts that aren't on the list aren't part of the licensed bundle, so close them whenever suits you. For Helpshift, please export the full ticket history to Drive before your subscription ends. If our engineers change anything on this list, we'll reply on this thread. Best, Maya Client onboarding, Sunset" Second message, Feb 13 2026 18:20 UTC: "Hi all - one change after our engineers walked through your data map today: Trello is part of the bundle too, and Metabase isn't (it only reads from BigQuery), so please keep BigQuery and dbt instead. The rest of the list stands. Maya" So the hold list is Slack (paid plan, every user), Google Workspace (every user, nothing archived or deleted), Figma, Linear, GitHub, Trello, BigQuery and dbt; Metabase is out. Trap: Sherwood Partners' Feb 12 "Wind-down checklist" (cancel everything except payroll and accounting) is from a firm that was not engaged and does not govern.

OE 10  Find SVB's card terms on the founders' Trello board (Trello search "SVB card", open the card)
        Expected: Card "SVB card payoff + closure" in To Do, created Feb 13 2026 15:52 UTC by Leonard: "From the call with SVB today: once the payoff from the data deal posts, they close the card on Feb 20. Any charge after that is declined. Anything we keep that will charge the card again while we still need it has to move to Arthur's KubLLC card or one of our personal cards by end of day Feb 19. Whatever we're cancelling can stay on the card until it ends." The card shows 2 comments. Trap: the Done card "move subscriptions to SVB credit card" (2023-24) is the old move onto the card, not these terms.

OE 11  Read the two comments on the SVB card (Trello: the card's comment actions; the description alone is out of date)
        Expected: Leonard, Feb 13 2026 22:47 UTC: "Bank called back: the payoff posted early, so they close the card on the 18th, not the 20th. Anything we keep has to be off it by end of day the 17th. And let's not drag the cancellations out either: everything we're cancelling gets cancelled by end of day the 17th, wherever it bills. Only exception is carta, that renewal is in august and stays as I said." Arthur, Feb 13 2026 23:12 UTC: "ok. aws and 1password go by the 17th too then, the store transfer is done by then and I'll keep the logins we still need in my own vault" These supersede the description: the card closes Feb 18, so Keep and Hold rows still charging it must be off by Feb 17, and every Cancel row that is not Closed is due by Feb 17 (the earlier date under rule 6), except Carta, which keeps its August date (Aug 14, 2026, the day before the Aug 15 renewal). AWS in Arthur's reply is not a register row (rule 3 keeps AWS off).

OE 12  Find the delivery review call Sunset's mail refers to on Robert's calendar (Calendar search "data delivery review")
        Expected: Event titled "Sunset", an en dash, then "data delivery review", organizer Leonard, starts Thu Mar 12 2026 17:00 UTC (a future meeting). Hold rows that won't charge the SVB card again before it stay until Mar 12.

OE 13  Find the Cursor reply in #prototype (Slack search "cursor", then the thread under Oliver's Feb 13 message)
        Expected: Oliver, Fri Feb 13 2026 10:02 UTC: "if cursor is getting cut can we keep it till the last combo fighter build? it's doing half my refactors" Arthur's thread reply, Fri Feb 13 2026 14:07 UTC: "sorry, it's already gone. cursor sent the confirmation on the team plan cancellation this morning, seats keep working until mar 5 so you have it till then" Cursor itself confirmed, so Cursor is Closed (say where: Arthur's #prototype reply), by-when a dash, ENG-2460 Done.

OE 14  Find Arthur's Unity note in #executives (Slack search "unity termination")
        Expected: Arthur, Fri Feb 13 2026 21:18 UTC: "unity's account manager wrote back on the termination: it's confirmed, the pro seats stop at the end of the month and there's no invoice on the 19th" Unity's account manager confirmed, so Unity is Closed (say where: Arthur's #executives note), by-when a dash, ENG-2438 Done; the ENG-2438 comment only says the termination was sent.

OE 15  Read the HG Costs tab of the January P&L for the lines Arthur's project came from (Drive search "P&L and forecast", spreadsheet "Harmony Games P&L and forecast - Jan 2026", tab HG Costs)
        Expected: 75 rows. Shared lines: "Sound (Pond5, Soundly,Elevenlabs)" (three accounts in one line) and "UA" (ad networks, which rule 3 and the project keep off the register). The $6,250 line is Singular and the hosting line is GitHub (per the project description). Pond5, Soundly and ElevenLabs each count as an account under rule 3.

OE 16  Find the Figma billing email in Robert's Gmail (Gmail search "Figma")
        Expected: "Figma Professional (annual) - $1,212.00. Charged to the card on file. Your plan renews on September 11, 2026." - Figma Professional (annual) - $1,212.00, renews Sep 11, 2026, so 101.00 a month; it won't charge again before the review call.

OE 17  Find the Layer billing email in Robert's Gmail (Gmail search "Layer")
        Expected: "Layer Pro (monthly) - $49.00. Paid with the card on file. Your next payment is on March 3, 2026." - Layer Pro (monthly) - $49.00, next payment Mar 3, 2026; the SVB comment's Feb 17 is earlier, so by Feb 17. Leonard cancelled in the app but Layer has not confirmed: Requested.

OE 18  Find the Pond5 billing email in Robert's Gmail (Gmail search "Pond5")
        Expected: "Your Pond5 Annual Membership was not renewed and ended on September 8, 2025. Your licensed downloads stay yours; renew any time to download again." - the Pond5 Annual Membership was not renewed and ended Sep 8, 2025, so cancelled before Feb 9, left off (rule 2).

OE 19  Find the Soundly billing email in Robert's Gmail (Gmail search "Soundly")
        Expected: "Your Soundly Pro (monthly, $10.00) subscription has been cancelled. You'll keep access until March 3, 2026 and won't be charged again." - Soundly Pro (monthly, $10.00) cancelled, access until Mar 3, 2026, no further charge, so Closed (Soundly's email).

OE 20  Find ElevenLabs' receipt in Robert's Gmail (Gmail search "ElevenLabs")
        Expected: Receipt Jul 9 2025, annual $50 plan: 4.17 a month; renews Jul 9, 2026, but the SVB comment's Feb 17 is earlier, so by Feb 17, 2026. ElevenLabs sits in the Sound line and has no issue, so rule 3 adds it.

OE 21  Work out Singular's monthly cost and by-when from its billing mail in Robert's Gmail (Gmail search "Singular invoice", then read the "Singular - Past Due Invoices" thread)
        Expected: Robert's mailbox holds four Singular invoice mails: "Singular Labs Inc: Invoice #INVSINC19046" (Sep 2 2024), "Singular Labs Inc: Invoice #INVSINC22671" (Sep 1 2025, sent again Sep 8 2025) and "Singular Labs Inc: Invoice #INVSINC23580" (Dec 1 2025); their amounts sit only in PDF attachments the Agent can't open, so don't rely on them. The past-due thread's Jan 5 reminder: "There is an outstanding balance of $6,250.00 on your account". With Leonard's ENG-2444 comment ("the next quarterly invoice is mar 1") and the project's "the $6,250 one is Singular", the quarterly charge is $6,250.00: 6,250 / 3 = 2,083.33 a month. Next charge Mar 1 (day before: Feb 28), but the SVB comment's Feb 17 is earlier, so by Feb 17. The Mar 15 date in Singular's Jan 15 reply is only the extension on the past-due $6,250.00 balance. Leonard's Feb 12 termination is the last message in the thread, and Singular hasn't answered: Requested.

OE 22  Check iPostal and Trello in Robert's Gmail (Gmail searches "iPostal" and "Changes to your Trello subscription")
        Expected: iPostal: mailbox cancelled Jan 16 2026, so cancelled before Feb 9, left off. Trello: Nov 21 2025 "You still have access to Trello Free", so free plan, 0.00, but Sunset's correction holds it.

OE 23  Check whether the two "From old receipts" issues, Lucidchart and Google Ads, are still live; neither has a comment or a costs-tab line (Gmail searches "Lucidchart" and "Google Ads account was canceled")
        Expected: "Your Lucidchart subscription has been canceled", Oct 10 2025 16:11 UTC: "Your Lucidchart subscription has been canceled and will expire on Nov 4, 2025." "Your Google Ads account was canceled (449-481-1590)", Oct 17 2025 06:04 UTC: the account "was canceled on 10/16/25." Both were cancelled before Feb 9, so both stay off the register (rule 2) and ENG-2465 and ENG-2466 go to Canceled.

OE 24  Look for CodeRabbit's own word on GitHub (GitHub: the bot's comment on pull request 38 "Final build settings" in harmonygames-Games/Combo-Fighters)
        Expected: CodeRabbit bot comment, Feb 13 2026 09:41 UTC: "The CodeRabbit subscription for harmonygames-Games was canceled on Feb 12, 2026, so this pull request was not reviewed." A bot notice counts as the vendor's confirmation (rule 5), so CodeRabbit is Closed (say where: this PR notice), by-when a dash, ENG-2459 Done.

OE 25  Work out the register from the rules and the records above (calculation)
        Expected: 25 rows (account: action, status for Cancel rows, by when, owner, monthly cost): Unity: Cancel, Closed (Unity's reply, per Arthur's #executives note), a dash, Arthur, 2,348.50; Helpshift: Cancel, Closed (Helpshift's reply, per Leonard's ENG-2439 comment), a dash, Leonard, 150.00; Soundly: Cancel, Closed (Soundly's cancellation email), a dash, Robert, 10.00; Linear: Hold for Sunset, Mar 12, 2026, Arthur, 152.72; Figma: Hold for Sunset, Mar 12, 2026, Robert, 101.00; Trello: Hold for Sunset, Mar 12, 2026, Leonard, 0.00; Singular: Cancel, Requested, Feb 17, 2026, Leonard, 2,083.33; Metabase: Move to Arthur's LLC, a dash, Arthur, 148.00; dbt: Hold for Sunset, Mar 12, 2026, Arthur, 100.00; BigQuery: Hold for Sunset, Mar 12, 2026, Arthur, 4.97; Intuit QuickBooks: Keep, Feb 17, 2026, Leonard, 115.00; Carta: Cancel, Open, Aug 14, 2026, Leonard, 321.00; Google Workspace: Hold for Sunset, Feb 17, 2026, Leonard, 298.13; Slack: Hold for Sunset, Feb 17, 2026, Leonard, 87.22; Gusto: Cancel, Open, Feb 17, 2026, Leonard, 116.00; Deel: Keep, a dash, Leonard, 300.00; Docusign: Cancel, Open, Feb 17, 2026, Robert, 25.00; Layer: Cancel, Requested, Feb 17, 2026, Leonard, 49.00; CodeRabbit: Cancel, Closed (CodeRabbit bot notice on PR 38), a dash, Arthur, 45.00; Cursor: Cancel, Closed (Cursor's confirmation, per Arthur's #prototype reply), a dash, Arthur, 40.00; Zapier: Cancel, Closed (Zapier's email, per Leonard's ENG-2461 comment), a dash, Leonard, 73.50; GitHub: Hold for Sunset, Mar 12, 2026, Arthur, 90.00; Kapwing: Cancel, Closed (Kapwing's confirmation email, per Arthur's ENG-2463 comment), a dash, Arthur, 24.00; 1Password: Cancel, Open, Feb 17, 2026, Arthur, 19.95; ElevenLabs: Cancel, Open, Feb 17, 2026, Robert, 4.17. Left off: Intuit, the duplicate of the QuickBooks issue (rule 1); iPostal, Lucidchart and Google Ads, cancelled before Feb 9 (rule 2); Pond5, ended Sep 2025 (rule 2); AWS and the UA line's ad accounts (meta, applovin, the Unity ads), which rule 3 and the project keep off; and the two $30 game-ops lines: Arthur's project description says "the two $30 game-ops lines I'm handling myself, so they're not in here", and rule 3 only adds accounts from costs-tab lines that cover several vendors.

OE 26  Add up the two monthly totals (calculation, rule 9)
        Expected: Every row: 6,706.49. Keep and Hold for Sunset rows only: 1,249.04.

OE 27  Create the register as a new Google Sheet in Robert's Drive (Sheets: create a spreadsheet)
        Expected: A new spreadsheet exists, owned by Robert.

OE 28  Write the 25 rows and the two totals into the sheet (Sheets: update values)
        Expected: The sheet holds the 25 rows of the register (account, what we do, where it stands, by when, owner, monthly cost) and the two totals 6,706.49 and 1,249.04.

OE 29  Share the register with Leonard as an editor (Drive: share file, leonard.hayes@harmonygames.co, role writer)
        Expected: Leonard has edit access.

OE 30  Share the register with Arthur as an editor (Drive: share file, arthur.blake@harmonygames.co, role writer)
        Expected: Arthur has edit access.

OE 31  Set ENG-2438 Unity to Done, per the project rule (Linear update of ENG-2438: state Done)
        Expected: ENG-2438 moves from Todo to Done.

OE 32  Comment on ENG-2438 Unity with what happens and by when (Linear comment on ENG-2438)
        Expected: A new comment on ENG-2438 saying Cancel (Closed), nothing left to do by a date.

OE 33  Set ENG-2439 Helpshift to Done, per the project rule (Linear update of ENG-2439: state Done)
        Expected: ENG-2439 moves from Todo to Done.

OE 34  Comment on ENG-2439 Helpshift with what happens and by when (Linear comment on ENG-2439)
        Expected: A new comment on ENG-2439 saying Cancel (Closed), nothing left to do by a date.

OE 35  Set ENG-2440 Soundly to Done, per the project rule (Linear update of ENG-2440: state Done)
        Expected: ENG-2440 moves from Todo to Done.

OE 36  Comment on ENG-2440 Soundly with what happens and by when (Linear comment on ENG-2440)
        Expected: A new comment on ENG-2440 saying Cancel (Closed), nothing left to do by a date.

OE 37  Comment on ENG-2441 Linear with what happens and by when (Linear comment on ENG-2441)
        Expected: A new comment on ENG-2441 saying Hold for Sunset, by Mar 12, 2026.

OE 38  Comment on ENG-2442 Figma with what happens and by when (Linear comment on ENG-2442)
        Expected: A new comment on ENG-2442 saying Hold for Sunset, by Mar 12, 2026.

OE 39  Comment on ENG-2443 Trello with what happens and by when (Linear comment on ENG-2443)
        Expected: A new comment on ENG-2443 saying Hold for Sunset, by Mar 12, 2026.

OE 40  Comment on ENG-2444 Singular with what happens and by when (Linear comment on ENG-2444)
        Expected: A new comment on ENG-2444 saying Cancel (Requested), by Feb 17, 2026.

OE 41  Comment on ENG-2446 Metabase with what happens and by when (Linear comment on ENG-2446)
        Expected: A new comment on ENG-2446 saying Move to Arthur's LLC, nothing left to do by a date.

OE 42  Comment on ENG-2447 dbt with what happens and by when (Linear comment on ENG-2447)
        Expected: A new comment on ENG-2447 saying Hold for Sunset, by Mar 12, 2026.

OE 43  Comment on ENG-2448 BigQuery with what happens and by when (Linear comment on ENG-2448)
        Expected: A new comment on ENG-2448 saying Hold for Sunset, by Mar 12, 2026.

OE 44  Comment on ENG-2449 QuickBooks with what happens and by when (Linear comment on ENG-2449)
        Expected: A new comment on ENG-2449 saying Keep, by Feb 17, 2026.

OE 45  Set ENG-2450 Intuit to Canceled, per the project rule (Linear update of ENG-2450: state Canceled)
        Expected: ENG-2450 moves from Todo to Canceled.

OE 46  Comment on ENG-2450 Intuit with what happens and by when (Linear comment on ENG-2450)
        Expected: A new comment on ENG-2450 saying it is a duplicate of ENG-2449 QuickBooks, which carries the row.

OE 47  Comment on ENG-2451 Carta with what happens and by when (Linear comment on ENG-2451)
        Expected: A new comment on ENG-2451 saying Cancel (Open), by Aug 14, 2026.

OE 48  Comment on ENG-2452 Google Workspace with what happens and by when (Linear comment on ENG-2452)
        Expected: A new comment on ENG-2452 saying Hold for Sunset, by Feb 17, 2026.

OE 49  Comment on ENG-2453 Slack with what happens and by when (Linear comment on ENG-2453)
        Expected: A new comment on ENG-2453 saying Hold for Sunset, by Feb 17, 2026.

OE 50  Set ENG-2454 iPostal to Canceled, per the project rule (Linear update of ENG-2454: state Canceled)
        Expected: ENG-2454 moves from Todo to Canceled.

OE 51  Comment on ENG-2454 iPostal with what happens and by when (Linear comment on ENG-2454)
        Expected: A new comment on ENG-2454 saying it is off the register: cancelled before Feb 9 (mailbox closed Jan 16, 2026).

OE 52  Comment on ENG-2455 Gusto with what happens and by when (Linear comment on ENG-2455)
        Expected: A new comment on ENG-2455 saying Cancel (Open), by Feb 17, 2026.

OE 53  Comment on ENG-2456 Deel with what happens and by when (Linear comment on ENG-2456)
        Expected: A new comment on ENG-2456 saying Keep, nothing left to do by a date.

OE 54  Comment on ENG-2457 Docusign with what happens and by when (Linear comment on ENG-2457)
        Expected: A new comment on ENG-2457 saying Cancel (Open), by Feb 17, 2026.

OE 55  Comment on ENG-2458 Layer with what happens and by when (Linear comment on ENG-2458)
        Expected: A new comment on ENG-2458 saying Cancel (Requested), by Feb 17, 2026.

OE 56  Set ENG-2459 CodeRabbit to Done, per the project rule (Linear update of ENG-2459: state Done)
        Expected: ENG-2459 moves from Todo to Done.

OE 57  Comment on ENG-2459 CodeRabbit with what happens and by when (Linear comment on ENG-2459)
        Expected: A new comment on ENG-2459 saying Cancel (Closed), nothing left to do by a date.

OE 58  Set ENG-2460 Cursor to Done, per the project rule (Linear update of ENG-2460: state Done)
        Expected: ENG-2460 moves from Todo to Done.

OE 59  Comment on ENG-2460 Cursor with what happens and by when (Linear comment on ENG-2460)
        Expected: A new comment on ENG-2460 saying Cancel (Closed), nothing left to do by a date.

OE 60  Set ENG-2461 Zapier to Done, per the project rule (Linear update of ENG-2461: state Done)
        Expected: ENG-2461 moves from Todo to Done.

OE 61  Comment on ENG-2461 Zapier with what happens and by when (Linear comment on ENG-2461)
        Expected: A new comment on ENG-2461 saying Cancel (Closed), nothing left to do by a date.

OE 62  Comment on ENG-2462 GitHub with what happens and by when (Linear comment on ENG-2462)
        Expected: A new comment on ENG-2462 saying Hold for Sunset, by Mar 12, 2026.

OE 63  Set ENG-2463 Kapwing to Done, per the project rule (Linear update of ENG-2463: state Done)
        Expected: ENG-2463 moves from Todo to Done.

OE 64  Comment on ENG-2463 Kapwing with what happens and by when (Linear comment on ENG-2463)
        Expected: A new comment on ENG-2463 saying Cancel (Closed), nothing left to do by a date.

OE 65  Comment on ENG-2464 1Password with what happens and by when (Linear comment on ENG-2464)
        Expected: A new comment on ENG-2464 saying Cancel (Open), by Feb 17, 2026.

OE 66  Set ENG-2465 Lucidchart to Canceled, per the project rule (Linear update of ENG-2465: state Canceled)
        Expected: ENG-2465 moves from Todo to Canceled.

OE 67  Comment on ENG-2465 Lucidchart with what happens and by when (Linear comment on ENG-2465)
        Expected: A new comment on ENG-2465 saying it is off the register: cancelled before Feb 9 (subscription canceled Oct 10, 2025, expired Nov 4, 2025).

OE 68  Set ENG-2466 Google Ads to Canceled, per the project rule (Linear update of ENG-2466: state Canceled)
        Expected: ENG-2466 moves from Todo to Canceled.

OE 69  Comment on ENG-2466 Google Ads with what happens and by when (Linear comment on ENG-2466)
        Expected: A new comment on ENG-2466 saying it is off the register: cancelled before Feb 9 (account canceled Oct 16, 2025).

OE 70  Reply to Leonard in his thread with the two totals and the clashes (Slack message in #winddown under his Feb 13 ask)
        Expected: A reply in the thread of Leonard's ask stating: every row 6,706.49 a month; Keep and Hold rows 1,249.04 a month; two clashes with what was already decided: (1) Slack going to the free version / a few accounts with everyone else as guests, against Sunset's paid plan with every user in place until the review call; (2) archiving Google accounts after Feb 15, against Sunset's "please don't archive or delete any" until the review call.
