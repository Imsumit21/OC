OE 1  Read Leonard's handover ask in Slack (Frederick's DM with Leonard, latest messages before Oct 1 2025)
        Expected: Leonard, Tue Sep 30 2025 3:40 PM PT (22:40 UTC): "ok after the tiktok/youtube mess I want every marketing + UA account you're on sorted before we start letting people go. one row per account: who actually holds it, whether money is still moving on it, and what we do with it. arthur's handover rules are on the Harmony Games board, they decide the action. arthur's sweep from today is the list. save the register in the Company Ops folder and reply here with how many you've marked TRANSFER and anything an outsider still has access to". The message has one thread reply.

OE 2  Open the thread under that message (Slack, same DM, thread of Sep 30 3:40 PM PT)
        Expected: Leonard's reply, Sep 30 2025 3:48 PM PT (22:48 UTC): "oh and for money moving, ad revenue under $100 for september doesn't count, it's just the trickle from old installs. rest of the cash notes stands"

OE 3  Find Arthur's handover rules for marketing on the Harmony Games Trello board and open the card (search "handover rules", or the board's To Do list)
        Expected: Card "Account handover rules - marketing, UA & socials" (#456), created by Arthur Sep 30 2025 1:41 PM PT (20:41 UTC). It says it replaces the old Company Accounts & Access page on Confluence for marketing. Rule 1: every marketing, UA, ad-monetization and social account in today's sweep folder that has Fred on it in any role; App Store Connect, Play Console, Singular and Metabase are on the engineering card; MAX bidders are not accounts; an account deleted or deactivated before the sweep is off the list. Rule 2: holder = Owner, Admin or Super admin (Managers, users, analysts, pending invites and shared logins don't count). Rule 3: a company holder logs in with a person's harmonygames.co address; a personal address is neither a company holder nor outside access. Rule 4: OUTSIDE ACCESS if an agency, contractor or partner still has admin or partner admin; otherwise SINGLE with fewer than two company holders, COMPANY-HELD with two or more. Rule 5: OUTSIDE ACCESS -> REVOKE; otherwise no money moving -> CLOSE; otherwise SINGLE -> TRANSFER (Leonard added as an owner), COMPANY-HELD -> KEEP; money moving is Leonard's definition for the cuts. Rule 6: columns account, company holders, class, money moving (Y/N), action. Rule 7: socials marked TRANSFER go as a checklist on Fred's "Lock up social handles and domain?" card on the UA/BD board; no new card. The card has one comment. Trap: the engineering card "Account handover rules - engineering, stores & data tools" on the same list ("My list, not Fred's", KEEP or MOVE only) and the 2024 Confluence page "Company Accounts & Access" (don't close accounts) do not govern Fred's accounts.

OE 4  Read the comment on that card (Trello card actions)
        Expected: Arthur, Sep 30 2025 2:58 PM PT (21:58 UTC): "socials (YouTube, TikTok, Instagram, X, LinkedIn, Discord) never get CLOSE, even with no money moving. Where the card would close a social, it goes TRANSFER or KEEP by its class instead. Rest of the card stands."

OE 5  Find Arthur's follow-up email in Frederick's Gmail (search "Account handover rules")
        Expected: From Arthur Blake to Frederick, cc Leonard, Sep 30 2025 4:21 PM PT (23:21 UTC), subject "Account handover rules - marketing, UA & socials": keep the Harmony Games, Inc. Google Ads account 569-350-5790 open in case a publisher takes Domino Delights; "Mark it KEEP on the register. The Calm Play one (449-481-1590) still follows the card. Everything else on the card stands." Trap: without this email, rule 5 closes 569 (no money moving).

OE 6  Read Leonard's money-moving definition in Google Docs (search Drive for "cash notes" or "money still moving"; doc "Runway & shutdown cash notes", section "Money still moving (for the cuts)")
        Expected: Doc owned by Leonard, last modified Sep 30 2025 10:48 AM PT. An account has money moving if anything was spent, billed or paid out on it in September 2025, or a campaign on it is still switched on. Ad revenue paid to us counts (the warehouse has it by network and month). A charge the vendor agreed in writing to drop doesn't count. The spend tables have no Meta spend after April and no Unity cost, so spend goes by receipts and whether the campaign is on; for revenue use ad revenue by network, not the finance ledger. Trap: Leonard's older #executives remark of Sep 24 ("keep anything we've paid in the last 90 days") is superseded by this doc and his Sep 30 reply.

OE 7  Find Arthur's sweep in Drive and list its files (search "sweep"; folder "Admin sweep - Sep 30")
        Expected: Folder owned by Arthur, shared with Frederick, created Sep 30 2025 12:50 PM PT, 17 spreadsheets: Meta Business - Domino Delights ad account - people; Google Ads 569-350-5790 - access; Google Ads 449-481-1590 - access; Unity - Harmony Games Inc org - owners and managers; AppLovin - Harmony Games - account users; adjoe advertiser dashboard - users; AdMob pub-3556282811018998 - users; AdMob pub-2341961509332343 - users; TikTok - harmonygames - access; YouTube - Harmony Games channel - permissions; LinkedIn - Harmony Games page - admins; X - harmonygames - access; Instagram - harmonygames - access; Discord - Harmony Games server - admin roles; Google Play Console - Harmony Games, Inc. developer account - users; App Store Connect - Harmony Games, Inc. team - users; Singular - users. Under rule 1, Play Console, App Store Connect and Singular are on the engineering card. Trap: Fred's March "Marketing & UA logins" sheet is not the list; Leonard's DM names the sweep.

OE 8  Check the status of AdMob pub-2341961509332343 in Frederick's Gmail (search "AdMob account has been deactivated")
        Expected: Google AdMob email, Sun Aug 24 2025 8:07 AM PT: "Your AdMob account (pub-2341961509332343) has been deactivated because it hasn't served ads for at least 6 months." Deactivated before the sweep, so rule 1 takes it off the list. 13 accounts remain. Trap: its export sits in the sweep folder with Fred as Admin.

OE 9  Read every tab of the Meta export (spreadsheet "Meta Business - Domino Delights ad account - people", tabs People and Partners)
        Expected: Ad account Domino Delights, 907669287942378. People: Frederick Stone Admin (created the ad account), Robert (robert@harmonygames.co) Admin, Leonard Hayes Admin (business portfolio admin), Arthur Blake Admin. Partners: Node Media LLC, Partner admin (manage campaigns, billing view), shared by Frederick 2024-10-07. Four company holders; a partner still has partner admin, so OUTSIDE ACCESS. Trap: the People tab alone, and Leonard's Sep 29 DM "i'm admin on meta, google ads and unity already so those are covered", read as COMPANY-HELD.

OE 10  Check Meta money in Frederick's Gmail (search "meta ads receipt", September 2025)
        Expected: "Your meta ads receipt", Tue Sep 16 2025 6:40 AM PT: $0.05 billed for ad costs on Sep 15 2025, campaign ZM_UK_CPE_CopyAds. Billed in September, so money moving Y.

OE 11  Read both tabs of the Google Ads 569-350-5790 export (tabs Access and Linked managers)
        Expected: Account Harmony Games, Inc.; Enabled campaigns 0; Leonard Hayes Admin (added 2024-09-20) and Frederick Stone Admin (2024-10-07). Linked managers: Node Media LLC 645-364-1205, Unlinked 2024-12-20. Two company holders, no outside access: COMPANY-HELD.

OE 12  Read both tabs of the Google Ads 449-481-1590 export (tabs Access and Linked managers)
        Expected: Account Calm Play LLC; Enabled campaigns 0; Robert, Leonard Hayes, Arthur Blake and Frederick Stone all Admin. Node Media LLC 645-364-1205 Unlinked 2024-12-20. Four company holders: COMPANY-HELD.

OE 13  Read both tabs of the Unity export (tabs Members and Unity Ads advertiser)
        Expected: Members (org Harmony Games Inc, 20067043314233, owners and managers only): Arthur Blake Owner, Robert Owner, Leonard Hayes Owner, Frederick Stone Manager. Unity Ads advertiser: Arthur, Robert and Leonard Admin (2024-08-02); Node Media LLC Admin since 2024-12-05. Company holders Arthur, Robert, Leonard (Fred is a Manager, so not a holder); an agency is Admin, so OUTSIDE ACCESS. Trap: the Members tab alone shows no outsider.

OE 14  Check whether Unity campaigns are on in Slack (#executives, Sep 29 to 30 2025)
        Expected: Leonard, Mon Sep 29 2025 3:48 PM PT: "I set budget to $150/campaign/day on IOS (it was set to $1 to effectively pause)". Fred, Sep 30: clicks up 5x on iOS. A campaign is switched on, so money moving Y.

OE 15  Read the AppLovin export (tab Users)
        Expected: Frederick Stone Admin, Leonard Hayes Admin; Arthur Blake, Brian Foster and one unnamed account as User. Two company holders: COMPANY-HELD.

OE 16  Check AppLovin money in Frederick's Gmail (search "AppLovin submitted a payment")
        Expected: Email via the ads group, Sun Sep 14 2025 12:33 AM PT: "we have initiated a ACH payment to you", Ref Pub1020673667. Paid out in September, so money moving Y.

OE 17  Read the adjoe export (tab Users)
        Expected: Frederick Stone Admin, Leonard Hayes Admin. Two company holders: COMPANY-HELD.

OE 18  Read the adjoe thread in Slack (adjoe shared channel, Leonard's message of Sep 8 2025 "looks like it got turned on Sep 1st", all replies)
        Expected: adjoe rep, Sep 8 2025 9:06 AM PT: paused the campaign (backend error). Leonard: the September installs are not attributable and won't be accepted for billing. adjoe rep, Sep 8 9:41 AM PT: "I can confirm you will not be responsible for the cost of those installs." The vendor agreed in writing to drop the charge, so money moving N. Trap: the campaign did run in September (turned on Sep 1).

OE 19  Read the AdMob pub-3556282811018998 export (tab Users)
        Expected: Leonard Hayes Admin (account owner) since 2025-03-03; Frederick Stone Admin since 2025-08-25. Two company holders: COMPANY-HELD.

OE 20  Query September 2025 ad revenue paid to us in Snowflake (ANALYTICS.MONETIZATION.AD_REVENUE, date in September 2025, sum revenue_usd by network and accrued_vs_paid)
        Expected: admob paid $38.70; applovin paid $136.33; meta_audience paid $26.15; unity accrued_unpaid $43.26; ironsource accrued_unpaid $27.08. AdMob's $38.70 is under Leonard's $100, so AdMob money moving N. Trap: under the cash notes alone it is paid out (Y); Leonard's Aug 25 DM "It's active and a working account" is about this account, not the deactivated one.

OE 21  Read the TikTok export (tab Access)
        Expected: Scope "Account logins". @harmonygames: login frederick.stone@harmonygames.co, Admin, Active, "recovered 2025-09-29; Leonard signs in with this login". @harmonygames.app deactivated 2025-09-29 (off the list). The export only covers logins: one company holder (Fred). Trap: read alone this is SINGLE -> TRANSFER; Leonard using Fred's login does not make him a holder.

OE 22  Search Frederick's Gmail for partners on TikTok (search "Node Media" or "TikTok partner")
        Expected: TikTok for Business, Thu Sep 18 2025 10:12 AM PT, "Partner reminder: Node Media LLC can manage @harmonygames": partner Node Media LLC, permission Admin (manage account, post videos, run ads), shared Oct 8, 2024. An agency still has admin: TikTok is OUTSIDE ACCESS.

OE 23  Read both tabs of the YouTube export (tabs Permissions and Removed users)
        Expected: Scope "Studio channel permissions": Frederick Stone Owner (created the channel), Leonard Hayes Manager. Removed users: Node Media LLC, [EMAIL_126620], Manager, removed 2024-12-20 by Frederick. Trap: the export covers Studio permissions only; read alone YouTube is SINGLE with the agency gone.

OE 24  Search Frederick's Gmail for the channel's Brand Account owners (search "Brand Account" or "Review who can manage Harmony Games")
        Expected: Google, Tue Sep 9 2025 8:42 AM PT, "Review who can manage Harmony Games": Brand Account for the YouTube channel; Frederick Stone Primary owner; [EMAIL_126620] Owner; people added in YouTube Studio are listed in Studio, not here. [EMAIL_126620] is Node Media LLC (OE 23), so an agency is still an Owner: YouTube is OUTSIDE ACCESS.

OE 25  Read the LinkedIn export (tab Page admins)
        Expected: Leonard Hayes, Robert, Arthur Blake and Frederick Stone, all Super admin. Four company holders: COMPANY-HELD.

OE 26  Read the X export (tab Access)
        Expected: @harmonygames, login frederick.stone@harmonygames.co, Owner, "no delegates set up". One company holder: SINGLE. Trap: Arthur's #executives summary says only YouTube and TikTok are on Fred alone; X is.

OE 27  Read the Instagram export (tab Access)
        Expected: @harmonygames, Frederick Stone, login is Fred's personal gmail, Owner (account login), note "Fred's personal gmail, not harmonygames.co. Login only". Trap: read alone, this has no company holder under rule 3 and looks SINGLE -> TRANSFER. OE 28 shows the real holders.

OE 28  Search Frederick's Gmail for who controls the Instagram account (search "full control" or "instagram")
        Expected: Meta Business Suite, Mon Sep 15 2025 7:05 AM PT, "People with full control of @harmonygames": full control (admin) Leonard Hayes (leonard.hayes@harmonygames.co, added Jan 22, 2024) and Frederick Stone (frederick.stone@harmonygames.co, added Sep 5, 2024); partners none. Two company holders: COMPANY-HELD.

OE 29  Read the Discord export (tab Admins)
        Expected: Leonard Hayes Owner, Frederick Stone Admin, Robert Admin. Three company holders: COMPANY-HELD.

OE 30  Check Frederick's Gmail for September 2025 billing or payouts on the remaining accounts (Google Ads, TikTok, YouTube, LinkedIn, X, Instagram, Discord; searches such as receipt, invoice, payment, billing, after:2025/09/01 before:2025/10/01)
        Expected: No receipt, invoice or payout for any of them in September 2025. TikTok mail that month is TikTok Shop marketing, the Sep 18 Node Media partner reminder (OE 22), two Sep 29 account verification codes and a Sep 29 "You have 50 new followers" notice, and none is a bill. Both Google Ads exports show 0 enabled campaigns. Money moving N on all eight.

OE 31  Apply the card's rules, the comment and Arthur's email to the 13 accounts (analysis, no tool)
        Expected: Meta: Fred, Robert, Leonard, Arthur; OUTSIDE ACCESS; Y; REVOKE. Google Ads 569-350-5790: Leonard, Fred; COMPANY-HELD; N; KEEP (Arthur's email). Google Ads 449-481-1590: Robert, Leonard, Arthur, Fred; COMPANY-HELD; N; CLOSE. Unity: Arthur, Robert, Leonard; OUTSIDE ACCESS; Y; REVOKE. AppLovin: Fred, Leonard; COMPANY-HELD; Y; KEEP. adjoe: Fred, Leonard; COMPANY-HELD; N; CLOSE. AdMob pub-3556282811018998: Leonard, Fred; COMPANY-HELD; N; CLOSE. TikTok: Fred; OUTSIDE ACCESS; N; REVOKE. YouTube: Fred; OUTSIDE ACCESS; N; REVOKE. LinkedIn: Leonard, Robert, Arthur, Fred; COMPANY-HELD; N; KEEP (social). X: Fred; SINGLE; N; TRANSFER (social). Instagram: Leonard, Fred; COMPANY-HELD; N; KEEP (social). Discord: Leonard, Fred, Robert; COMPANY-HELD; N; KEEP (social). Totals: REVOKE 4, TRANSFER 1, KEEP 5, CLOSE 3.

OE 32  Find the Company Ops folder in Drive (search "Company Ops")
        Expected: One folder "Company Ops", owned by Leonard, created Sep 30 2025 3:31 PM PT; Frederick has write access.

OE 33  Create the register as a new Google Sheet (Sheets; title of the agent's choosing)
        Expected: A new spreadsheet exists (title is up to the agent, e.g. "Account handover register").

OE 34  Move the new spreadsheet into the Company Ops folder (Drive, new parent = the Company Ops folder from OE 32)
        Expected: The register's parent folder is Company Ops.

OE 35  Write the register into the sheet (header plus one row per account)
        Expected: Columns account, company holders, class, money moving (Y/N), action, and the 13 rows from OE 31 with those values; holders may be names or harmonygames.co addresses.

OE 36  Reply to Leonard in the DM (Slack, Frederick's DM with Leonard; in the thread of OE 1 or as a new message)
        Expected: Message sent in the DM saying 1 account is marked TRANSFER (X @harmonygames) and that Node Media LLC still has access to 4 accounts: the Meta Domino Delights ad account (partner admin), the Unity Ads advertiser (Admin), the YouTube Brand Account (Owner) and TikTok @harmonygames (Business Center partner, Admin). A link to the register may be included.

OE 37  Find Fred's "Lock up social handles and domain?" card on the UA/BD Trello board (search "Lock up social handles")
        Expected: Card #40 in list "ZM 3d Technical Launch / Alpha", created Mar 10 2025, no description and no checklist.

OE 38  Add a checklist to that card (Trello, card from OE 37)
        Expected: A checklist exists on the "Lock up social handles and domain?" card (name is up to the agent, e.g. "Socials to transfer").

OE 39  Add the X account as an item on that checklist (Trello; the checklist from OE 38, item name naming X @harmonygames)
        Expected: One check item for X @harmonygames (Leonard to be added as an owner). X is the only social marked TRANSFER.
