OE 1  Read Leonard's DM from Thursday night in Slack (Robert's DM with Leonard Hayes, his message of Thu Feb 12 2026)
Expected: Leonard, Thu Feb 12 2026 9:40 PM PT (Fri Feb 13 05:40 UTC), message ts 1770961200.890407: "if you really want to keep combo fighter going, let's set the LLC up properly." "I put everything we might need from HG into the LLC project in linear, one issue each." "go through them and make the call on each one: what the LLC takes if Sunset can't sell it, what it costs us March through May, and who pays what." "the ground rules doc has how we decide." "lay the sheet out like my draft from Tuesday, keep it in your drive and share it with Blake and me." "leave your call on each issue too so we can see it there." "I'll email you how we split the money." "then tell me here what you'd do and what it costs each of us a month." "we decide on Monday's call"

OE 2  Find the LLC project in Linear (search the projects for "LLC", named in OE 1; it has one match)
Expected: Project "LLC take-over", team ENG, created Thu Feb 12 2026 3:24 PM PT. Its description: "One issue per thing the LLC might take from HG or pay for." "Leave your call on each one as a comment and move it: to Done if one of us pays it himself through May (even if HG still owns it) or if the LLC takes it and nothing is left to do on it; to Todo if the LLC takes it and something is still to do, and assign whoever moves it; to Canceled if it stays with HG."

OE 3  List the issues in the LLC take-over project in Linear (project from OE 2)
Expected: 37 issues, all in Backlog with no assignee: ENG-2438 Combo Fighter; ENG-2439 Domino Delights; ENG-2440 Zombie Match; ENG-2441 Domino Delights production account (AWS); ENG-2442 Domino Delights dev account (AWS); ENG-2443 Zombie Match account (AWS); ENG-2444 Analytics pipeline account (AWS); ENG-2445 Combo Fighter backend and auth stacks (AWS); ENG-2446 Build machines; ENG-2447 Metabase; ENG-2448 dbt; ENG-2449 GitHub; ENG-2450 Singular; ENG-2451 AppsFlyer; ENG-2452 Google Analytics; ENG-2453 Figma; ENG-2454 layer.ai; ENG-2455 Soundly; ENG-2456 Kapwing; ENG-2457 Cursor; ENG-2458 CodeRabbit; ENG-2459 Unity Pro; ENG-2460 Zapier; ENG-2461 Helpshift; ENG-2462 Domino Delights player support; ENG-2463 Slack; ENG-2464 Google Workspace; ENG-2465 Linear; ENG-2466 Deel; ENG-2467 Gusto; ENG-2468 Intuit; ENG-2469 Carta; ENG-2470 Apple developer account; ENG-2471 Google Play developer account; ENG-2472 Calm Play LLC; ENG-2473 Unity Ads balance; ENG-2474 Playable vendor.

OE 4  Read the comments on each of the 37 issues in Linear (one call per issue, list from OE 3)
Expected: One comment on each. ENG-2438 Leonard: "robert's game. all of it is HG's IP today"; ENG-2439 Leonard: "boombit's test doesn't change anything, the game is ours. I'll handle it with Sunset"; ENG-2440 Leonard: "both store listings moved over to HG's accounts in july"; ENG-2441 Leonard, Thu Feb 12 2026 4:48 PM PT (Fri Feb 13 00:48 UTC): "about $1k a month, Blake thinks he can get it to $300"; ENG-2442 Arthur: "nothing runs on dev anymore, shutting it down"; ENG-2443 Arthur: "ZM's account still runs phoenix, its nakama and the aurora cluster, nobody trimmed it. it bills every month on HG's AWS bill"; ENG-2444 Arthur: "kinesis and glue only ever carried DD and ZM events, CF's go through firebase. shutting it down"; ENG-2445 Arthur, Thu Feb 12 2026 4:58 PM PT (Fri Feb 13 00:58 UTC): "Combo Fighter's own account (its auth and backend stacks) runs about $95 a month on HG's AWS bill. CF stopped calling ZM's phoenix api, it doesn't need ZM's account. I keep an eye on them"; ENG-2446 Arthur: "the build boxes at my place are HG's, they go with the laptops in Sunset's sale. I'll move our jenkins jobs to my own machine before then, so the LLC doesn't need them"; ENG-2447 Leonard, Thu Feb 12 2026 4:52 PM PT (Fri Feb 13 00:52 UTC): "about $300 a month with dbt, more or less"; ENG-2448 Leonard: "same as metabase, the two go together"; ENG-2449 Leonard: "we keep it under HG until the data is sold, then the repos transfer"; ENG-2450 Leonard: "termination letter is the one in #winddown. they deferred our last quarterly payment, still waiting on them"; ENG-2451 Leonard: "singular is getting terminated, so CF goes on appsflyer's free tier from March. free up to 15K installs, no cost aggregation or user level data. I'll set CF up on it"; ENG-2452 Leonard: "stays under HG until the data is extracted, nothing for the LLC to take or pay"; ENG-2453 Leonard: "HG prepaid it to Sep 11, it stays HG's and just lapses then. nothing for the LLC to take or pay"; ENG-2454 Leonard: "cancelled it on the 11th"; ENG-2455 Leonard: "robert cancelled it on the 11th"; ENG-2456 Arthur: "cancelled, Pro runs to Feb 25"; ENG-2457 Arthur: "cancelled the seats on the 12th"; ENG-2458 Arthur: "cancelled on the 12th"; ENG-2459 Arthur: "termination note to unity goes out from me, leonard's draft from #winddown. CF is fine on unity personal"; ENG-2460 Leonard: "cancelled"; ENG-2461 Leonard: "they're cancelling without a hassle. DD and ZM have to be off it before Feb 28th. CF was never on it, its support is the contact on its store listing and that moves with the game"; ENG-2462 Arthur, Thu Feb 12 2026 5:30 PM PT (Fri Feb 13 01:30 UTC): "done, support goes to the email address now and Helpshift is out of DD (merged in #1917)"; ENG-2463 Leonard: "down to the three of us as paid members, everyone else is a single channel guest. we keep it for the data"; ENG-2464 Leonard: "archiving the unused accounts after Feb 15"; ENG-2465 Leonard: "keeping it during the transition"; ENG-2466 Leonard: "keeping it during the shutdown"; ENG-2467 Leonard: "keeping it during the shutdown, we need it for the docs"; ENG-2468 Leonard: "keeping it for the next two months"; ENG-2469 Leonard: "renewal is 8/15 and it's tied to the closed chase account, no rush"; ENG-2470 Leonard: "HG's account. CF's listing sits in it and moves with the game"; ENG-2471 Leonard: "HG's account, one-time fee, nothing monthly"; ENG-2472 Leonard, Thu Feb 12 2026 3:41 PM PT: "Calm Play could just be our LLC, it already has the Singular org and its own Apple team"; ENG-2473 Leonard: "the $100 left on it goes on this week's playable test, then nothing"; ENG-2474 Leonard: "$3,750 for the first playable, one-off".

OE 5  Read the ground rules doc in Drive/Docs (search "ground rules"; doc "LLC ground rules (Combo Fighter and whatever else we take)", from OE 1)
Expected: Leonard's doc, last changed Thu Feb 12 2026 3:46 PM PT. "The LLC is the new one Blake and I are setting up for the three of us, and anything Harmony Games owns (the games with their art and listings, and the equipment) comes to it only through Sunset's sale, the way I wrote after the call on Wednesday." "Services we keep running just move their billing to the LLC." "The plan runs March 1 to May 31." "Domino Delights and Zombie Match come over only if what each made in January, going by the warehouse's daily revenue table, covers what its own hosting bills now, whatever we said about them before." "Combo Fighter comes over either way, it's the reason we're doing this." "A game that comes over brings what it needs to keep running, its accounts and its player support." "Cost every item at what it bills now, going by whoever runs it, not by what HG used to pay." "What we already decided to keep or cancel for the shutdown in #winddown stays decided." "this plan is only what bills us every month, no one-offs or yearly fees." "How things move is on the LLC card on our board."

OE 6  Read the LLC card on the Harmony Games board in Trello (search "LLC", named in OE 5; the open card "LLC: what we take from HG", not the archived 2024 card "Follow up with Michelle on LLC")
Expected: "Robert makes the call on each item in the Linear project." "Whoever runs an item today moves it." "Anything that comes through Sunset's sale moves when the sale closes." "Anything that already has its own deadline keeps it; everything else moves by March 1."

OE 7  Read Leonard's draft from Tuesday in Sheets (search Drive for "LLC"; of the three LLC files shared with Robert, the sheet "LLC 90 days (draft)", from OE 1)
Expected: Created Tue Feb 10 2026 10:30 AM PT. Header: Item, Game, Decision, Monthly cost, Paid by, Next step, Owner, By. Rows: Combo Fighter, CF, LLC, 0, Owner Robert; DD servers, DD, ?, "~1000 (Blake: maybe 300)", Owner Blake; Metabase + dbt, Game blank, ?, "~300"; Figma, CF, LLC, 0, Owner Robert.

OE 8  Read Leonard's email on the split in Gmail (search "split", from "how we split the money" in OE 1; the newest hit, the full message)
Expected: Leonard to Robert, cc Arthur, Thu Feb 12 2026 10:10 PM PT (Fri Feb 13 06:10 UTC), subject "LLC money": "each of the three of us carries a third of what the LLC costs a month, March through May." "that's everything on the plan that bills monthly, including what one of us already pays for it." "whatever one of us already pays personally counts toward his third, and he puts the difference in as cash." "put the three shares on the sheet per month."

OE 9  Read the February posts in #winddown in Slack (named in OE 5; page through the whole month)
Expected: Arthur, Mon Feb 9 2026 3:49 PM PT: "Looks like DD production account costs ~$1k a month" and Mon Feb 9 2026 4:10 PM PT (Tue Feb 10 00:10 UTC): "Might be easy to get to 300". Leonard, Tue Feb 10 2026 9:58 PM PT (Wed Feb 11 05:58 UTC): "We gotta move domino delights and zombie match off Helpshift before Feb 28th." Robert, Wed Feb 11 2026 5:21 PM PT (Thu Feb 12 01:21 UTC): "Our Figma is good until September 11th". Leonard, Thu Feb 12 2026 1:45 PM PT: "if Singular shuts down our access we may need to move to another solution provider that offers data for free up to 15K installs". Leonard, Thu Feb 12 2026 2:00 PM PT: "During shutdown, let’s keep Deel, gusto, Intuit. I canceled other subscriptions under mine." "linear we keep during transition". Leonard's action items, Thu Feb 12 2026 2:05 PM PT: "We keep accounts that has our data such as Slack, google, google analytics, github under Harmony Games until the data is extracted". Arthur, Thu Feb 12 2026 3:00 PM PT: "I'll be moving github," "and Metabase to my KubLLC card."

OE 10  Sum each game's January revenue in Snowflake (table ANALYTICS.MONETIZATION.REVENUE_DAILY, named in OE 5: SUM(total_revenue_usd) and COUNT(*) by game_id for date 2026-01-01 to 2026-01-31)
Expected: Three rows: domino_delights 183.11, zombie_match_3d 0.00, combo_fighter 7.36, each over 62 daily rows.

OE 11  Search Slack for what the Domino Delights production account bills now (search "AWS bill", from the ENG-2443 and ENG-2445 comments in OE 4; its only hit is Arthur's thread reply in Robert's DM with Arthur Blake)
Expected: Arthur, Thu Feb 12 2026 7:10 PM PT (Fri Feb 13 03:10 UTC): "fyi Domino's prod account is down to $140 a month now, one small task and the db at its floor. that's what it bills from March. it's still on HG's AWS bill till then".

OE 12  Read Arthur's email on the Metabase, dbt and GitHub billing in Gmail (search "metabase", from ENG-2447 in OE 3 and Arthur's #winddown post in OE 9; the newest hit, subject "billing moved to my card", the full message)
Expected: Arthur to Robert and Leonard, Thu Feb 12 2026 6:35 PM PT (Fri Feb 13 02:35 UTC): "github, dbt and metabase bill to my Kub card from the next bill." "it's the $100 base now, dbt is $100 and github is back to the $48 team plan" "so $248 a month. I'll carry those through May as my part." "the github org itself stays HG's till the data's delivered, I'm just paying the bill, so count it as mine like the other two.".

OE 13  Read Arthur's "jenkins" email in Gmail (search "jenkins", from the ENG-2446 comment in OE 4; the newest hit, the full message; the figure is in its second paragraph)
Expected: Arthur to Robert, cc Leonard, Thu Feb 12 2026 8:20 PM PT (Fri Feb 13 04:20 UTC): "the build boxes are HG's, they can go with the laptops whenever the sale needs them." "so CF's own account bills $62 a month now, just its live stacks. still on HG's AWS bill till March like Domino's.".

OE 14  Search Slack for anything else one of them already pays himself (search "my card": OE 8 counts what one of them already pays, and OE 12 is Arthur's "billing moved to my card"; the newest hit is Leonard's reply in a #prototype thread), then read that thread and Leonard's budget post in the channel that morning
Expected: Leonard's reply, Thu Feb 12 2026 3:20 PM PT: "of the meta campaigns only the VO one is still on" "it's set to $100/day capped at $3,000 a month, and that's what it runs at from March" "it's on my card till the end of Feb and moves to our new company's card from March if we keep CF going, so count it as its own line in what we pay each month". The thread's root, Leonard, Fri Feb 6 2026 10:59 AM PT: "VO campaign is created and will go live in the next few hours"; his channel post at Fri Feb 6 2026 11:00 AM PT: "Budget is $100/day".

OE 15  Search Slack for layer.ai and read the thread under Leonard's post in #prototype (search "layer.ai")
Expected: Leonard, Wed Feb 11 2026 11:21 AM PT: "we have access until March 3rd". His reply in that thread, to Robert, Thu Feb 12 2026 11:15 AM PT: "the CF character concept art is only in layer.ai, can you pull it out yourself before then?" "the art goes with CF, there's nothing on the layer account for our new company to take, it just lapses".

OE 16  Search Robert's Gmail for Domino Delights, whose player support is ENG-2462 in OE 3 (search "Domino Delights"; the newest hit is App Review's mail, subject "We noticed an issue with your submission."; the full message)
Expected: Thu Feb 12 2026 11:30 PM PT (Fri Feb 13 07:30 UTC), signed App Review: "App Name: Domino Delights" "Guideline 1.5 - Safety - Developer Information" "The support option in the app only opens an email draft, and on a device without a mail account set up it does nothing, so users can't reach you from the app." "Please add a support URL or another way to contact you in the app." It comes after Arthur's "done" on ENG-2462 (OE 4).

OE 17  Search Slack for what Calm Play LLC is (search "calm play", from ENG-2472 in OE 3; page to Leonard's December 2023 post in #admin_foundersonly)
Expected: Leonard, Mon Dec 25 2023 12:15 AM PT: "we had to do a couple more things on top of the regular LLC setup to make calm play full subsidiary of Harmony Games".

OE 18  List the Linear users for the assignees (Robert, Leonard Hayes, Arthur Blake)
Expected: Robert: usr_Robert, robert@harmonygames.co. Leonard: usr_63fffeb4fab5233e, leonard.hayes@harmonygames.co. Arthur: usr_cc3e90160f490686, arthur.blake@harmonygames.co.

OE 19  Look up Leonard Hayes and Arthur Blake in Contacts ("Blake" in the prompt and the DM)
Expected: leonard.hayes@harmonygames.co (Co-founder & CEO); arthur.blake@harmonygames.co (Co-founder & CTO).

OE 20  Apply the take test to Domino Delights and Zombie Match (Docs rule in OE 5, Snowflake in OE 10, Slack in OE 11, Linear in OE 4)
Expected: Domino Delights made 183.11 in January, which covers the $140 a month its prod account bills now; the ~$1k and 300 in #winddown, ENG-2441's note and the draft are earlier figures. So Domino Delights comes over with its accounts and its player support. Zombie Match made 0.00, which covers none of its account's bill (ENG-2443: "it bills every month on HG's AWS bill"), so Zombie Match and its account stay with HG. Combo Fighter comes over either way.

OE 21  Set each item's monthly cost at what it bills now (OEs 11, 12, 13, 14, 4)
Expected: Domino Delights production account: 140. Combo Fighter backend and auth stacks: 62 (Arthur's email of Thu 8:20 PM PT is later than his "about $95" on ENG-2445 at 4:58 PM PT and says why it fell). Metabase 100, dbt 100, GitHub 48: 248 a month on Arthur's card through May (later than Leonard's "about $300" on ENG-2447). The VO campaign: 3,000 a month from March, its own line. AppsFlyer: 0 (free tier). Not monthly, so off the plan: the playable vendor's $3,750 ("one-off"), the Unity Ads $100, Carta's renewal ("renewal is 8/15") and Google Play's "one-time fee". Every other item costs the LLC 0.

OE 22  Make the call on each of the 37 issues and on the VO campaign (rules in OEs 5, 6, 2, findings in OEs 4, 9, 14, 15, 16, 17, 20, 21)
Expected: The LLC takes 7, each with a step left and the person who moves it: Combo Fighter (comes through Sunset's sale; Robert; when the sale closes); Domino Delights (through Sunset's sale; Leonard, "I'll handle it with Sunset"; when the sale closes); Domino Delights production account (billing moves to the LLC; Arthur; by Mar 1, "still on HG's AWS bill till then"); Combo Fighter backend and auth stacks (billing moves to the LLC; Arthur; by Mar 1, "still on HG's AWS bill till March"); AppsFlyer (set CF up on the free tier; Leonard, "I'll set CF up on it"; by Mar 1); Domino Delights player support (a build with a support URL or another in-app contact, past App Review, before Helpshift stops; Arthur; before Feb 28); the VO campaign (moves to the new company's card from March; Leonard; by Mar 1). Arthur pays himself through May, 3: Metabase, dbt, GitHub (the org stays HG's till the data's delivered). HG keeps 28: Zombie Match, Domino Delights dev account (AWS), Zombie Match account (AWS), Analytics pipeline account (AWS), Build machines, Singular, Google Analytics, Figma, layer.ai, Soundly, Kapwing, Cursor, CodeRabbit, Unity Pro, Zapier, Helpshift, Slack, Google Workspace, Linear, Deel, Gusto, Intuit, Carta, Apple developer account, Google Play developer account, Calm Play LLC, Unity Ads balance, Playable vendor. Among them, Figma stays HG's (prepaid to Sep 11), not LLC as on the draft; layer.ai lapses, with nothing on the account for the new company, and Robert pulls CF's concept art out before access ends Mar 3; Calm Play LLC is HG's subsidiary, and the LLC is the new one Leonard and Arthur are setting up.

OE 23  Work out the monthly total and the three shares (the split in OE 8, costs in OE 21)
Expected: 140 + 62 + 3,000 + 100 + 100 + 48 = 3,450 a month, March through May. A third each: 1,150. Arthur already pays 248, which counts toward his third, so he puts in 902 cash; Leonard and Robert put in 1,150 cash each. The LLC itself pays 3,202 a month (140 + 62 + 3,000).

OE 24  Create an issue for the VO campaign in the LLC take-over project in Linear (team ENG, project from OE 2, state Todo, assignee Leonard from OE 18)
Expected: A new issue in the LLC take-over project naming Combo Fighter's VO (Meta) campaign, state Todo, assigned to Leonard Hayes.

OE 25  Comment the call on the new VO campaign issue in Linear
Expected: A comment saying the LLC takes it: 3,000 a month from March, its own line; Leonard moves it from his card to the new company's card by Mar 1.

OE 26  Comment the call on ENG-2438 in Linear
Expected: A comment on ENG-2438 (Combo Fighter) saying LLC: it comes through Sunset's sale; Robert moves it when the sale closes.

OE 27  Comment the call on ENG-2439 in Linear
Expected: A comment on ENG-2439 (Domino Delights) saying LLC: January's 183.11 covers its $140 hosting; it comes through Sunset's sale, Leonard moves it when the sale closes.

OE 28  Comment the call on ENG-2440 in Linear
Expected: A comment on ENG-2440 (Zombie Match) saying stays with HG: January's 0.00 doesn't cover its hosting.

OE 29  Comment the call on ENG-2441 in Linear
Expected: A comment on ENG-2441 (Domino Delights production account (AWS)) saying LLC at $140 a month; Arthur moves the billing off HG's AWS bill by Mar 1.

OE 30  Comment the call on ENG-2442 in Linear
Expected: A comment on ENG-2442 (Domino Delights dev account (AWS)) saying stays with HG: nothing runs on it, Arthur is shutting it down.

OE 31  Comment the call on ENG-2443 in Linear
Expected: A comment on ENG-2443 (Zombie Match account (AWS)) saying stays with HG with Zombie Match; Combo Fighter doesn't need it.

OE 32  Comment the call on ENG-2444 in Linear
Expected: A comment on ENG-2444 (Analytics pipeline account (AWS)) saying stays with HG: it only carried DD and ZM events, Arthur is shutting it down.

OE 33  Comment the call on ENG-2445 in Linear
Expected: A comment on ENG-2445 (Combo Fighter backend and auth stacks (AWS)) saying LLC at $62 a month; Arthur moves the billing off HG's AWS bill by Mar 1.

OE 34  Comment the call on ENG-2446 in Linear
Expected: A comment on ENG-2446 (Build machines) saying stays with HG: the build boxes go with the laptops in Sunset's sale.

OE 35  Comment the call on ENG-2447 in Linear
Expected: A comment on ENG-2447 (Metabase) saying Arthur pays it himself through May, $100 a month.

OE 36  Comment the call on ENG-2448 in Linear
Expected: A comment on ENG-2448 (dbt) saying Arthur pays it himself through May, $100 a month.

OE 37  Comment the call on ENG-2449 in Linear
Expected: A comment on ENG-2449 (GitHub) saying Arthur pays it himself through May, $48 a month; the org stays HG's till the data's delivered.

OE 38  Comment the call on ENG-2450 in Linear
Expected: A comment on ENG-2450 (Singular) saying stays with HG: Singular is being terminated.

OE 39  Comment the call on ENG-2451 in Linear
Expected: A comment on ENG-2451 (AppsFlyer) saying LLC at $0: Combo Fighter goes on AppsFlyer's free tier, Leonard sets it up by Mar 1.

OE 40  Comment the call on ENG-2452 in Linear
Expected: A comment on ENG-2452 (Google Analytics) saying stays with HG until the data is extracted.

OE 41  Comment the call on ENG-2453 in Linear
Expected: A comment on ENG-2453 (Figma) saying stays with HG: prepaid to Sep 11, then it lapses.

OE 42  Comment the call on ENG-2454 in Linear
Expected: A comment on ENG-2454 (layer.ai) saying stays with HG and lapses, nothing on the account for the new company to take; Robert pulls CF's concept art out before access ends Mar 3.

OE 43  Comment the call on ENG-2455 in Linear
Expected: A comment on ENG-2455 (Soundly) saying stays with HG: cancelled.

OE 44  Comment the call on ENG-2456 in Linear
Expected: A comment on ENG-2456 (Kapwing) saying stays with HG: cancelled, Pro runs to Feb 25.

OE 45  Comment the call on ENG-2457 in Linear
Expected: A comment on ENG-2457 (Cursor) saying stays with HG: cancelled.

OE 46  Comment the call on ENG-2458 in Linear
Expected: A comment on ENG-2458 (CodeRabbit) saying stays with HG: cancelled.

OE 47  Comment the call on ENG-2459 in Linear
Expected: A comment on ENG-2459 (Unity Pro) saying stays with HG: being terminated; Combo Fighter is fine on Unity Personal.

OE 48  Comment the call on ENG-2460 in Linear
Expected: A comment on ENG-2460 (Zapier) saying stays with HG: cancelled.

OE 49  Comment the call on ENG-2461 in Linear
Expected: A comment on ENG-2461 (Helpshift) saying stays with HG: cancelling; Combo Fighter was never on it.

OE 50  Comment the call on ENG-2462 in Linear
Expected: A comment on ENG-2462 (Domino Delights player support) saying LLC: App Review rejected the email-only support, so a build with a support URL or another in-app contact still has to pass review before Helpshift stops; Arthur, before Feb 28.

OE 51  Comment the call on ENG-2463 in Linear
Expected: A comment on ENG-2463 (Slack) saying stays with HG, kept for the data.

OE 52  Comment the call on ENG-2464 in Linear
Expected: A comment on ENG-2464 (Google Workspace) saying stays with HG, kept for the data.

OE 53  Comment the call on ENG-2465 in Linear
Expected: A comment on ENG-2465 (Linear) saying stays with HG, kept during the transition.

OE 54  Comment the call on ENG-2466 in Linear
Expected: A comment on ENG-2466 (Deel) saying stays with HG, kept during the shutdown.

OE 55  Comment the call on ENG-2467 in Linear
Expected: A comment on ENG-2467 (Gusto) saying stays with HG, kept during the shutdown.

OE 56  Comment the call on ENG-2468 in Linear
Expected: A comment on ENG-2468 (Intuit) saying stays with HG, kept during the shutdown.

OE 57  Comment the call on ENG-2469 in Linear
Expected: A comment on ENG-2469 (Carta) saying stays with HG: its renewal isn't a monthly bill.

OE 58  Comment the call on ENG-2470 in Linear
Expected: A comment on ENG-2470 (Apple developer account) saying stays with HG; Combo Fighter's listing moves with the game.

OE 59  Comment the call on ENG-2471 in Linear
Expected: A comment on ENG-2471 (Google Play developer account) saying stays with HG: a one-time fee, nothing monthly.

OE 60  Comment the call on ENG-2472 in Linear
Expected: A comment on ENG-2472 (Calm Play LLC) saying stays with HG: Calm Play is HG's subsidiary, and the LLC is the new one Leonard and Arthur are setting up.

OE 61  Comment the call on ENG-2473 in Linear
Expected: A comment on ENG-2473 (Unity Ads balance) saying stays with HG: the $100 is a one-off for this week's playable test.

OE 62  Comment the call on ENG-2474 in Linear
Expected: A comment on ENG-2474 (Playable vendor) saying stays with HG: the $3,750 is a one-off, not a monthly bill.

OE 63  Move ENG-2438 to Todo, assigned to Robert, in Linear (user from OE 18)
Expected: ENG-2438 state Todo, assignee Robert.

OE 64  Move ENG-2439 to Todo, assigned to Leonard, in Linear (user from OE 18)
Expected: ENG-2439 state Todo, assignee Leonard.

OE 65  Move ENG-2440 to Canceled in Linear
Expected: ENG-2440 state Canceled.

OE 66  Move ENG-2441 to Todo, assigned to Arthur, in Linear (user from OE 18)
Expected: ENG-2441 state Todo, assignee Arthur.

OE 67  Move ENG-2442 to Canceled in Linear
Expected: ENG-2442 state Canceled.

OE 68  Move ENG-2443 to Canceled in Linear
Expected: ENG-2443 state Canceled.

OE 69  Move ENG-2444 to Canceled in Linear
Expected: ENG-2444 state Canceled.

OE 70  Move ENG-2445 to Todo, assigned to Arthur, in Linear (user from OE 18)
Expected: ENG-2445 state Todo, assignee Arthur.

OE 71  Move ENG-2446 to Canceled in Linear
Expected: ENG-2446 state Canceled.

OE 72  Move ENG-2447 to Done in Linear
Expected: ENG-2447 state Done.

OE 73  Move ENG-2448 to Done in Linear
Expected: ENG-2448 state Done.

OE 74  Move ENG-2449 to Done in Linear
Expected: ENG-2449 state Done.

OE 75  Move ENG-2450 to Canceled in Linear
Expected: ENG-2450 state Canceled.

OE 76  Move ENG-2451 to Todo, assigned to Leonard, in Linear (user from OE 18)
Expected: ENG-2451 state Todo, assignee Leonard.

OE 77  Move ENG-2452 to Canceled in Linear
Expected: ENG-2452 state Canceled.

OE 78  Move ENG-2453 to Canceled in Linear
Expected: ENG-2453 state Canceled.

OE 79  Move ENG-2454 to Canceled in Linear
Expected: ENG-2454 state Canceled.

OE 80  Move ENG-2455 to Canceled in Linear
Expected: ENG-2455 state Canceled.

OE 81  Move ENG-2456 to Canceled in Linear
Expected: ENG-2456 state Canceled.

OE 82  Move ENG-2457 to Canceled in Linear
Expected: ENG-2457 state Canceled.

OE 83  Move ENG-2458 to Canceled in Linear
Expected: ENG-2458 state Canceled.

OE 84  Move ENG-2459 to Canceled in Linear
Expected: ENG-2459 state Canceled.

OE 85  Move ENG-2460 to Canceled in Linear
Expected: ENG-2460 state Canceled.

OE 86  Move ENG-2461 to Canceled in Linear
Expected: ENG-2461 state Canceled.

OE 87  Move ENG-2462 to Todo, assigned to Arthur, in Linear (user from OE 18)
Expected: ENG-2462 state Todo, assignee Arthur.

OE 88  Move ENG-2463 to Canceled in Linear
Expected: ENG-2463 state Canceled.

OE 89  Move ENG-2464 to Canceled in Linear
Expected: ENG-2464 state Canceled.

OE 90  Move ENG-2465 to Canceled in Linear
Expected: ENG-2465 state Canceled.

OE 91  Move ENG-2466 to Canceled in Linear
Expected: ENG-2466 state Canceled.

OE 92  Move ENG-2467 to Canceled in Linear
Expected: ENG-2467 state Canceled.

OE 93  Move ENG-2468 to Canceled in Linear
Expected: ENG-2468 state Canceled.

OE 94  Move ENG-2469 to Canceled in Linear
Expected: ENG-2469 state Canceled.

OE 95  Move ENG-2470 to Canceled in Linear
Expected: ENG-2470 state Canceled.

OE 96  Move ENG-2471 to Canceled in Linear
Expected: ENG-2471 state Canceled.

OE 97  Move ENG-2472 to Canceled in Linear
Expected: ENG-2472 state Canceled.

OE 98  Move ENG-2473 to Canceled in Linear
Expected: ENG-2473 state Canceled.

OE 99  Move ENG-2474 to Canceled in Linear
Expected: ENG-2474 state Canceled.

OE 100  Create the plan sheet in Sheets (in Robert's own Drive)
Expected: A new native spreadsheet in Robert's Drive, at the top level of his own Drive; any title.

OE 101  Write the plan to the sheet in Sheets (sheet from OE 100; calls, costs and shares from OEs 22, 21, 23)
Expected: Header Item, Game, Decision, Monthly cost, Paid by, Next step, Owner, By (the draft's columns, OE 7), then one row per item: the 37 issues and the VO campaign (Metabase and dbt may share one row as on the draft). LLC rows: Combo Fighter, 0, Owner Robert, by when the sale closes; Domino Delights, 0, Owner Leonard, by when the sale closes; Domino Delights production account, 140, paid by the LLC, Owner Arthur, by Mar 1; Combo Fighter backend and auth stacks, 62, paid by the LLC, Owner Arthur, by Mar 1; AppsFlyer, 0, Owner Leonard, by Mar 1; Domino Delights player support, 0, next step the support build past App Review, Owner Arthur, before Feb 28; the VO campaign, 3,000, paid by the LLC (the new company's card from March), Owner Leonard, by Mar 1. Metabase 100, dbt 100, GitHub 48: Arthur pays them himself, paid by Arthur. The other 28 rows: stay with HG, 0, paid by HG or blank. Robert pulls Combo Fighter's concept art out of layer.ai before Mar 3, on the layer.ai row (Owner Robert) or the Combo Fighter row. Shares per month: total 3,450; a third each 1,150; Robert 1,150 cash, Leonard 1,150 cash, Arthur 902 cash on top of the 248 he already pays.

OE 102  Share the sheet with Leonard Hayes in Drive (address from OE 19)
Expected: leonard.hayes@harmonygames.co can open the sheet (writer, commenter or reader).

OE 103  Share the sheet with Arthur Blake in Drive (address from OE 19)
Expected: arthur.blake@harmonygames.co can open the sheet (writer, commenter or reader).

OE 104  Reply to Leonard in the thread of his DM in Slack (the DM and message from OE 1, after every other write)
Expected: A reply in that thread (thread_ts 1770961200.890407) saying what Robert would do: take Combo Fighter and Domino Delights into the LLC and leave Zombie Match with HG; the plan costs 3,450 a month, 3,000 of it the VO campaign; Domino Delights' support build still has to pass App Review before Feb 28. What it costs each of them a month: 1,150 each (Arthur puts in 902 cash on top of the 248 he already pays). The link to the sheet.
