"""Draft criterion text per plan row (draft mode): title, justification, the evidence's Source line, sources (catalog keys
for the V3 evidence), accepted outcomes and the alternatives review. The evidence's Accept line is generated from the title."""

T = {}


def t(p, title, just, src, srcs, acc, alt):
    T[p] = dict(title=title, just=just, src=src, srcs=srcs, acc=acc, alt=alt)


DM = "the thread under Leonard's Thursday-night DM to Robert"
HG = "HG (Harmony Games)"

# ---------------------------------------------------------------- Linear: the VO line
t("P1", "The Agent creates a new issue in the LLC take-over project in Linear for Combo Fighter's VO campaign on Meta (its title names the VO, video, Meta or ads campaign)",
  "Multi-source: the project has no issue for it; Leonard's #prototype reply says to count it as its own line in what they pay each month, and the split mail counts what one of them already pays.",
  "Leonard's reply C09UHHN6PFZ/1770938400.370665 ('so count it as its own line in what we pay each month'); project LLC take-over 0fa95761-d59b-4ff4-a8a3-15df3210ca6e ('One issue per thing the LLC might take from HG or pay for').",
  ["HUB", "VO"], ["a new issue in the LLC take-over project whose title names Combo Fighter's VO / video / Meta / ads campaign"],
  "Any title naming that campaign passes (risk 1). An issue for another campaign, or a mention only in a comment, fails.")
t("P2", "The Agent puts the new Combo Fighter VO campaign issue in the LLC take-over project in the Todo state",
  "Interpretation: the project rule puts an item the LLC takes with a step still to do in Todo; the campaign moves to the new company's card from March.",
  "Project rule (0fa95761-d59b-4ff4-a8a3-15df3210ca6e): 'to Todo if the LLC takes it and something is still to do'; reply C09UHHN6PFZ/1770938400.370665 ('moves to our new company's card from March').",
  ["VO"], ["the new VO campaign issue in Todo"], "Backlog or Done fail: the card still has to move from March.")
t("P3", "The Agent assigns the new Combo Fighter VO campaign issue in the LLC take-over project to Leonard Hayes",
  "Lookup: the campaign is on Leonard's card and he moves it.",
  "Reply C09UHHN6PFZ/1770938400.370665 ('it's on my card till the end of Feb'); Leonard Hayes = leonard.hayes@harmonygames.co (Contacts), usr_63fffeb4fab5233e (Linear).",
  ["VO", "CL"], ["assignee Leonard Hayes (name, email or usr_63fffeb4fab5233e)"], "Robert or Arthur as assignee fails; naming Leonard only in a comment fails.")
t("P4", "The Agent comments on the new Combo Fighter VO campaign issue in the LLC take-over project that the LLC takes it (pays for it)",
  "Interpretation: the call on a monthly line that is not from HG but bills the plan.",
  "Reply C09UHHN6PFZ/1770938400.370665 ('count it as its own line in what we pay each month'); project rule 'Leave your call on each one as a comment'.",
  ["VO"], ["a comment on the new VO campaign issue giving the LLC as its call (any wording)"], "A call written only in the description fails; an HG call fails.")
# ---------------------------------------------------------------- Linear: comments
t("P5", "The Agent adds a comment to every one of the 37 existing issues in the LLC take-over project in Linear",
  "Comparison: coverage of the whole project list; the count is the output volume of the comments (rubric-sampling-v1).",
  "Leonard's DM D04UP2L3E3S/1770961200.890407 ('leave your call on each issue too'); the 37 issues ENG-2438 to ENG-2474 of project 0fa95761-d59b-4ff4-a8a3-15df3210ca6e.",
  ["HUB"], ["a new comment from the Agent on each of the 37 existing issues"], "36 or fewer commented issues fail; one project-level update fails.")
t("P6", "The Agent comments on ENG-2462 (Domino Delights player support) that the LLC takes it",
  "Interpretation: the ground rules bring a game's player support with the game, and Domino Delights comes over.",
  "Ground rules f_1e468a9d69ea0f0a2001f5 ('A game that comes over brings what it needs to keep running, its accounts and its player support'); App Review mail robert@harmonygames.co/<136285951.151027292.1770967800000@email.apple.com>; ENG-2462.",
  ["RULES", "ASC"], ["a comment on ENG-2462 giving the LLC as its call (any wording)"], "An HG call fails. The state (Todo vs Done) is graded on its own row.")
t("P7", f"The Agent comments on ENG-2453 (Figma) that it stays with {HG}",
  "Interpretation: Figma is prepaid to Sep 11 and stays HG's, against the draft's LLC row.",
  "Robert's #winddown post C0ADGSZKR3R/1770859313.592649 ('Our Figma is good until September 11th'); ENG-2453 comment ('HG prepaid it to Sep 11, it stays HG's'); draft f_d996e4c434ce160dc52596 row 'Figma, CF, LLC'.",
  ["WD134"], ["a comment on ENG-2453 that it stays with HG (or lapses with nothing for the LLC to take)"], "An LLC call (the draft's) fails.")
t("P8", f"The Agent comments on ENG-2472 (Calm Play LLC) that it stays with {HG}",
  "Interpretation: the ground rules, written after Leonard's comment, say the LLC is the new one; Calm Play is HG's subsidiary.",
  "Ground rules f_1e468a9d69ea0f0a2001f5 ('The LLC is the new one Blake and I are setting up'); C04UEQVDVB7/1703492127.063049 ('make calm play full subsidiary of Harmony Games'); ENG-2472.",
  ["RULES", "CALM"], ["a comment on ENG-2472 that it stays with HG (or is not used, the LLC being a new company)"], "Making Calm Play the LLC fails.")
t("P9", "The Agent comments on ENG-2449 (GitHub) that Arthur Blake pays for it himself",
  "Interpretation: Arthur's mail counts GitHub as his against the comment that HG keeps the org.",
  "Arthur's mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> ('so count it as mine like the other two'); ENG-2449.",
  ["BILL"], ["a comment on ENG-2449 that Arthur (Blake) pays it himself (the org may stay HG's)"], "An HG-only or LLC call fails.")
t("P10", "The Agent comments on ENG-2474 (Playable vendor) that it stays off the LLC's monthly plan as a one-off (or stays with HG)",
  "Interpretation: the ground rules count only what bills every month; the vendor's $3,750 is a one-off.",
  "Ground rules f_1e468a9d69ea0f0a2001f5 ('this plan is only what bills us every month, no one-offs or yearly fees'); ENG-2474 comment ('$3,750 for the first playable, one-off'); #prototype C09UHHN6PFZ/1770845002.610529.",
  ["RULES", "P672"], ["a comment on ENG-2474 keeping it off the monthly plan as a one-off, or leaving it with HG"], "Taking it as an LLC monthly cost fails.")
t("P11", f"The Agent comments on ENG-2457 (Cursor) that it stays with {HG}",
  "Lookup: Arthur cancels the Cursor seats.",
  "#winddown action items C0ADGSZKR3R/1770933903.645709 ('to cancel ..., coderabbit, cursor'); ENG-2457 comment ('cancelled the seats on the 12th').",
  ["WD190"], ["a comment on ENG-2457 that it stays with HG (or is cancelled)"], "An LLC call fails.")
# ---------------------------------------------------------------- Linear: states and assignees
t("P12", "The Agent moves ENG-2438 (Combo Fighter) to Todo",
  "Interpretation: the LLC takes it and it still moves through Sunset's sale.",
  "Ground rules f_1e468a9d69ea0f0a2001f5 ('Combo Fighter comes over either way'; 'comes to it only through Sunset's sale'); project rule ('to Todo if the LLC takes it and something is still to do').",
  ["RULES"], ["ENG-2438 in Todo"], "Backlog, Done or Canceled fail.")
t("P13", "The Agent assigns ENG-2438 (Combo Fighter) to Robert",
  "Lookup: Combo Fighter is Robert's game and whoever runs an item moves it.",
  "Leonard's DM D04UP2L3E3S/1770961200.890407 ('if you really want to keep combo fighter going'); ENG-2438 comment ('robert's game'); the LLC card ('Whoever runs an item today moves it').",
  ["HUB"], ["ENG-2438 assigned to Robert (name, 'me' or usr_Robert)"], "Leonard or no assignee fails.")
t("P14", "The Agent moves ENG-2439 (Domino Delights) to Todo",
  "Multi-source: January revenue in the warehouse ($183.11) against what its hosting bills now ($140, Arthur's DM) under the ground rules' take test.",
  "Ground rules f_1e468a9d69ea0f0a2001f5 (the January take test); Arthur's DM reply D04V95AAAHW/1770952200.665739 ('$140 a month now'); ANALYTICS.MONETIZATION.REVENUE_DAILY January sum 183.11 (REVENUE_DAILY_V2 gives the same).",
  ["RULES", "DD140"], ["ENG-2439 in Todo"], "Canceled on the stale ~$1k fails; Done fails (it still moves through the sale).")
t("P15", "The Agent assigns ENG-2439 (Domino Delights) to Leonard Hayes",
  "Lookup: Leonard handles Domino Delights with Sunset.",
  "ENG-2439 comment ('I'll handle it with Sunset'); Leonard's #executives post C07C2866011/1770850800.723979 on the IP auction; Leonard Hayes = leonard.hayes@harmonygames.co.",
  ["EX411", "CL"], ["ENG-2439 assigned to Leonard Hayes (name, email or usr_63fffeb4fab5233e)"], "Arthur, Robert or no assignee fails.")
t("P16", "The Agent moves ENG-2441 (Domino Delights production account (AWS)) to Todo",
  "Interpretation: the LLC takes it and its billing still has to move off HG's AWS bill.",
  "Arthur's DM reply D04V95AAAHW/1770952200.665739 ('that's what it bills from March. it's still on HG's AWS bill till then').",
  ["DD140"], ["ENG-2441 in Todo"], "Done or Canceled fail.")
t("P17", "The Agent assigns ENG-2441 (Domino Delights production account (AWS)) to Arthur Blake",
  "Lookup: Arthur runs the account and reports its bill.",
  "Arthur's DM reply D04V95AAAHW/1770952200.665739; Arthur Blake = arthur.blake@harmonygames.co (Contacts), usr_cc3e90160f490686 (Linear).",
  ["DD140", "CA"], ["ENG-2441 assigned to Arthur Blake (name, email or usr_cc3e90160f490686)"], "Leonard, Robert or no assignee fails.")
t("P18", "The Agent moves ENG-2445 (Combo Fighter backend and auth stacks (AWS)) to Todo",
  "Interpretation: the LLC takes it and its billing still moves off HG's AWS bill in March.",
  "Arthur's mail robert@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com> ('still on HG's AWS bill till March like Domino's').",
  ["JENK"], ["ENG-2445 in Todo"], "Done or Canceled fail.")
t("P19", "The Agent assigns ENG-2445 (Combo Fighter backend and auth stacks (AWS)) to Arthur Blake",
  "Lookup: Arthur runs the stacks.",
  "Arthur's mail robert@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com>; ENG-2445 comment ('I keep an eye on them'); arthur.blake@harmonygames.co.",
  ["JENK", "CA"], ["ENG-2445 assigned to Arthur Blake (name, email or usr_cc3e90160f490686)"], "Robert or no assignee fails.")
t("P20", "The Agent moves ENG-2451 (AppsFlyer) to Todo",
  "Interpretation: the LLC takes it and Combo Fighter still has to be set up on the free tier from March.",
  "Leonard's #winddown post C0ADGSZKR3R/1770932709.222409 ('data for free up to 15K installs'); ENG-2451 comment ('I'll set CF up on it').",
  ["WD179"], ["ENG-2451 in Todo"], "Done (because it is free) or Canceled fail.")
t("P21", "The Agent assigns ENG-2451 (AppsFlyer) to Leonard Hayes",
  "Lookup: Leonard sets Combo Fighter up on it.",
  "Leonard's #winddown post C0ADGSZKR3R/1770932709.222409; ENG-2451 comment ('I'll set CF up on it'); leonard.hayes@harmonygames.co.",
  ["WD179", "CL"], ["ENG-2451 assigned to Leonard Hayes (name, email or usr_63fffeb4fab5233e)"], "Arthur, Robert or no assignee fails.")
t("P22", "The Agent moves ENG-2462 (Domino Delights player support) to Todo",
  "Multi-source: App Review's rejection (Fri Feb 13 07:30 UTC) is later than Arthur's 'done' note and the merged PR, so a step is still to do.",
  "App Review mail robert@harmonygames.co/<136285951.151027292.1770967800000@email.apple.com> ('The support option in the app only opens an email draft'); ENG-2462 comment at 01:30 UTC ('done, support goes to the email address now').",
  ["ASC"], ["ENG-2462 in Todo"], "Done (Arthur's note) or Canceled fail.")
t("P23", "The Agent assigns ENG-2462 (Domino Delights player support) to Arthur Blake",
  "Lookup: the support change is Arthur's.",
  "ENG-2462 comment by Arthur; PR harmonygames-Games/GameOfDominoes#1917 by Arthur; App Review mail robert@harmonygames.co/<136285951.151027292.1770967800000@email.apple.com>; arthur.blake@harmonygames.co.",
  ["ASC", "CA"], ["ENG-2462 assigned to Arthur Blake (name, email or usr_cc3e90160f490686)"], "Leonard, Robert or no assignee fails.")
t("P24", "The Agent moves ENG-2447 (Metabase) to Done",
  "Interpretation: the project rule puts an item one of them pays himself through May in Done; Arthur carries Metabase.",
  "Arthur's mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> ('I'll carry those through May as my part'); project rule ('to Done if one of us pays it himself through May').",
  ["BILL"], ["ENG-2447 in Done"], "Todo or Canceled fail.")
t("P25", "The Agent moves ENG-2448 (dbt) to Done",
  "Interpretation: the same rule; Arthur carries dbt.",
  "Arthur's mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> ('dbt is $100'; 'I'll carry those through May').",
  ["BILL"], ["ENG-2448 in Done"], "Todo or Canceled fail.")
t("P26", "The Agent moves ENG-2449 (GitHub) to Done",
  "Interpretation: the rule's 'even if HG still owns it' settles GitHub as Done, though HG keeps the org.",
  "Arthur's mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> ('the github org itself stays HG's ... so count it as mine'); project rule ('even if HG still owns it').",
  ["BILL"], ["ENG-2449 in Done"], "Canceled or Todo fail.")
t("P27", "The Agent moves exactly 28 of the 37 existing issues in the LLC take-over project to Canceled",
  "Multi-source: the count only the full audit of all 37 calls produces (output volume of the Canceled moves).",
  "Ground rules f_1e468a9d69ea0f0a2001f5; project rule ('to Canceled if it stays with HG'); calls per issue ENG-2438 to ENG-2474 (28 stay with HG).",
  ["RULES"], ["exactly 28 of the 37 existing issues moved to Canceled"], "27, 29 or 31 (Domino Delights dropped) fail; leaving HG items in Backlog fails.")
t("P28", "The Agent moves ENG-2440 (Zombie Match) to Canceled",
  "Comparison: Zombie Match made $0.00 in January, which covers none of its hosting, under the take test.",
  "Ground rules f_1e468a9d69ea0f0a2001f5 (the January take test; 'whatever we said about them before'); REVENUE_DAILY January sum 0.00; ENG-2443 ('it bills every month on HG's AWS bill').",
  ["RULES"], ["ENG-2440 in Canceled"], "Todo (the Monday notes' 'DD and ZM both come with CF') fails.")
t("P29", "The Agent moves ENG-2453 (Figma) to Canceled",
  "Interpretation: Figma stays HG's, against the draft.",
  "#winddown C0ADGSZKR3R/1770859313.592649 ('Our Figma is good until September 11th'); ENG-2453 comment.",
  ["WD134"], ["ENG-2453 in Canceled"], "Todo (the draft's LLC row) or Done fail.")
t("P30", "The Agent moves ENG-2472 (Calm Play LLC) to Canceled",
  "Interpretation: Calm Play stays HG's subsidiary; the LLC is the new one.",
  "Ground rules f_1e468a9d69ea0f0a2001f5 ('The LLC is the new one'); C04UEQVDVB7/1703492127.063049.",
  ["RULES", "CALM"], ["ENG-2472 in Canceled"], "Todo or Done fail.")
t("P31", "The Agent moves ENG-2457 (Cursor) to Canceled",
  "Lookup: the seats are cancelled; it stays with HG.",
  "#winddown action items C0ADGSZKR3R/1770933903.645709 ('to cancel ..., coderabbit, cursor').",
  ["WD190"], ["ENG-2457 in Canceled"], "Backlog or Done fail.")
t("P32", "The Agent moves ENG-2442 (Domino Delights dev account (AWS)) to Canceled",
  "Interpretation: Domino Delights comes over with what it needs to keep running, and nothing runs on its dev account.",
  "Ground rules f_1e468a9d69ea0f0a2001f5 ('brings what it needs to keep running, its accounts'); ENG-2442 comment ('nothing runs on dev anymore, shutting it down').",
  ["RULES"], ["ENG-2442 in Canceled"], "Todo (taken with the game) fails.")
t("P33", "The Agent moves ENG-2470 (Apple developer account) to Canceled",
  "Interpretation: Combo Fighter's listing moves with the game; the account itself stays HG's.",
  "Ground rules f_1e468a9d69ea0f0a2001f5 ('the games with their art and listings ... only through Sunset's sale'); ENG-2470 comment ('HG's account. CF's listing sits in it and moves with the game').",
  ["RULES"], ["ENG-2470 in Canceled"], "Todo (taking the account for the listing) fails.")
# ---------------------------------------------------------------- Sheet
t("P34", "The Agent creates the plan sheet as a new spreadsheet in Robert's own Google Drive (its top level or any folder he owns)",
  "Lookup: the prompt and the DM put it in Robert's Drive.",
  "Leonard's DM D04UP2L3E3S/1770961200.890407 ('keep it in your drive'); Robert's Drive root d_9f7ba94f7526d54d8482ba.",
  ["HUB"], ["a new spreadsheet owned by Robert, at the top of his Drive or in a folder he owns"], "Editing Leonard's draft in place fails; a sheet outside Robert's Drive fails (/oe note 1: the top level is not required).")
t("P35", "The Agent gives its plan sheet the eight columns of Leonard's draft: Item, Game, Decision, Monthly cost, Paid by, Next step, Owner and By (in any order)",
  "Lookup: one header row copied off the draft.",
  "Leonard's draft f_d996e4c434ce160dc52596 'LLC 90 days (draft)', header row (Item, Game, Decision, Monthly cost, Paid by, Next step, Owner, By).",
  ["DRAFT"], ["the eight headers in any order; extra columns allowed"], "A sheet missing any of the eight headers fails.")
t("P36", "The Agent marks exactly 7 rows of its plan sheet as taken by the LLC (Decision LLC)",
  "Multi-source: the count only the full audit produces (6 issues plus the VO campaign); the output volume of the sheet.",
  "Ground rules f_1e468a9d69ea0f0a2001f5; Arthur's DM D04V95AAAHW/1770952200.665739; Leonard's reply C09UHHN6PFZ/1770938400.370665; the 37 issues.",
  ["RULES"], ["exactly 7 rows whose decision is the LLC's (LLC, LLC takes it, take)"], "6 (no VO row) or 8 or more fail.")
t("P37", "The Agent marks the Combo Fighter row of its plan sheet as taken by the LLC",
  "Lookup: the ground rules say Combo Fighter comes over either way.",
  "Ground rules f_1e468a9d69ea0f0a2001f5 ('Combo Fighter comes over either way, it's the reason we're doing this').",
  ["RULES"], ["Combo Fighter row: LLC (any LLC label)"], "HG fails.")
t("P38", "The Agent marks the Domino Delights row of its plan sheet as taken by the LLC",
  "Multi-source: January revenue $183.11 (warehouse) covers its $140 hosting (Arthur's DM) under the take test.",
  "Ground rules f_1e468a9d69ea0f0a2001f5; D04V95AAAHW/1770952200.665739 ('$140 a month now'); REVENUE_DAILY January sum 183.11.",
  ["RULES", "DD140"], ["Domino Delights row: LLC (any LLC label)"], "HG on the stale ~$1k fails.")
t("P39", f"The Agent marks the Zombie Match row of its plan sheet as staying with {HG} or going in Sunset's sale",
  "Comparison: $0.00 January revenue covers none of its hosting.",
  "Ground rules f_1e468a9d69ea0f0a2001f5; REVENUE_DAILY January sum 0.00.",
  ["RULES"], ["Zombie Match row: HG, stays with HG or Sunset's sale"], "LLC fails.")
t("P40", "The Agent marks the Metabase row of its plan sheet (alone or combined with dbt) as paid by Arthur Blake himself",
  "Interpretation: Arthur's mail settles the draft's open '?' for Metabase + dbt.",
  "Arthur's mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> ('github, dbt and metabase bill to my Kub card'); draft row 'Metabase + dbt, ?, ~300'.",
  ["BILL"], ["Metabase (or Metabase + dbt) paid by Arthur / Blake (Kub card)"], "Paid by the LLC or HG fails.")
t("P41", f"The Agent marks the Calm Play LLC row of its plan sheet as staying with {HG}",
  "Interpretation: Calm Play is HG's subsidiary; the LLC is the new one.",
  "C04UEQVDVB7/1703492127.063049; ground rules f_1e468a9d69ea0f0a2001f5.",
  ["CALM"], ["Calm Play LLC row: HG, stays with HG or not used"], "LLC fails.")
t("P42", f"The Agent marks the Figma row of its plan sheet as staying with {HG}",
  "Interpretation: the item's own record overrules the draft's LLC row.",
  "#winddown C0ADGSZKR3R/1770859313.592649; draft f_d996e4c434ce160dc52596 row 'Figma, CF, LLC, 0'.",
  ["WD134"], ["Figma row: HG, stays with HG or lapses Sep 11"], "LLC (the draft's) fails.")
t("P43", f"The Agent marks the Helpshift row of its plan sheet as staying with {HG}",
  "Lookup: Helpshift is being cancelled.",
  "#winddown C0ADGSZKR3R/1770789534.434749 ('Looks like Helpshift is gonna cancel our subscription'); ENG-2461 comment.",
  ["WD57"], ["Helpshift row: HG, stays with HG or cancelling"], "LLC fails.")
t("P44", f"The Agent marks the Cursor row of its plan sheet as staying with {HG}",
  "Lookup: the seats are cancelled.",
  "#winddown action items C0ADGSZKR3R/1770933903.645709.",
  ["WD190"], ["Cursor row: HG, stays with HG or cancelled"], "LLC fails.")
t("P45", "The Agent puts the Combo Fighter VO campaign on its plan sheet at $3,000 a month (3000 or 3,000)",
  "Multi-source: the monthly cap from the #prototype thread, outside the Linear project.",
  "Leonard's reply C09UHHN6PFZ/1770938400.370665 ('it's set to $100/day capped at $3,000 a month, and that's what it runs at from March').",
  ["VO"], ["the VO campaign row at 3,000 a month"], "$100/day without the monthly figure, 3,100 or 0 fail.")
t("P46", "The Agent puts the Domino Delights production account (AWS) on its plan sheet at $140 a month",
  "Multi-source: Arthur's later DM supersedes the ~$1k and 300 in #winddown, on ENG-2441 and in the draft.",
  "Arthur's DM reply D04V95AAAHW/1770952200.665739 ('down to $140 a month now'); superseded C0ADGSZKR3R/1770680984.725779 ('~$1k'), C0ADGSZKR3R/1770682219.100789 ('300').",
  ["DD140"], ["the Domino Delights production account row at 140 a month"], "1,000, 300 or 1,300 fail.")
t("P47", "The Agent puts a step on the Domino Delights player support row of its plan sheet to get a support build (with a support URL or another in-app contact) through App Review",
  "Multi-source: App Review's later rejection overrules Arthur's 'done' and the merged PR.",
  "App Review mail robert@harmonygames.co/<136285951.151027292.1770967800000@email.apple.com> ('Please add a support URL or another way to contact you in the app').",
  ["ASC"], ["a next step to build, resubmit or release Domino Delights with a support URL or another in-app contact and get it through App Review"], "'done' or no step fails.")
t("P66", "The Agent dates the Domino Delights player support row of its plan sheet no later than Feb 28 (a date from Feb 15 to Feb 28, 'by Feb 28' or 'before Feb 28', in its By or its step)",
  "Interpretation: the card keeps an item's own deadline, and DD has to be off Helpshift before Feb 28.",
  "#winddown C0ADGSZKR3R/1770789534.434749 ('We gotta move domino delights and zombie match off Helpshift before Feb 28th'); LLC card ('Anything that already has its own deadline keeps it').",
  ["WD57"], ["a date from Feb 15 to Feb 28, 'by Feb 28' or 'before Feb 28', in the By cell or the step text"], "Mar 1 (the card's default) or a later date fails.")
t("P48", "The Agent puts a step on its plan sheet to pull Combo Fighter's concept art out of layer.ai (export, download or save it; on the layer.ai row or the Combo Fighter row)",
  "Multi-source: Leonard's thread reply asks Robert to pull the art out; ENG-2454 only says it was cancelled.",
  "Leonard's reply C09UHHN6PFZ/1770923700.470906 ('the CF character concept art is only in layer.ai, can you pull it out yourself before then?'); ENG-2454 ('cancelled it on the 11th').",
  ["LAYER"], ["a step to export, download or save Combo Fighter's concept art from layer.ai, on the layer.ai or Combo Fighter row"], "'cancelled, nothing to do' fails.")
t("P67", "The Agent dates the layer.ai concept-art step on its plan sheet by Mar 3 (Mar 3 or an earlier date, in its By or its step)",
  "Interpretation: access ends March 3rd, so the step is due by then.",
  "Leonard's post C09UHHN6PFZ/1770837702.167889 ('we have access until March 3rd'); reply C09UHHN6PFZ/1770923700.470906 ('before then').",
  ["P575"], ["Mar 3 or an earlier date, in the By cell or the step text"], "A later date or no date fails.")
t("P49", "The Agent puts a step on the GitHub row of its plan sheet for the repos to transfer once the data is sold or delivered",
  "Interpretation: two records name the same step.",
  "Arthur's mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> ('the github org itself stays HG's till the data's delivered'); ENG-2449 ('then the repos transfer').",
  ["BILL"], ["a step that the repos transfer, or the org stays HG's, until the data is sold or delivered"], "Moving the repos now fails.")
t("P50", "The Agent puts the Combo Fighter backend and auth stacks (AWS) on its plan sheet at $62 a month",
  "Multi-source: Arthur's later mail supersedes his 'about $95' on ENG-2445.",
  "Arthur's mail robert@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com> ('so CF's own account bills $62 a month now'); ENG-2445 comment ('about $95').",
  ["JENK"], ["the Combo Fighter backend and auth stacks row at 62 a month"], "95 fails.")
t("P51", "The Agent puts AppsFlyer on its plan sheet at $0 a month (0, free or the free tier)",
  "Lookup: Combo Fighter goes on AppsFlyer's free tier.",
  "Leonard's #winddown post C0ADGSZKR3R/1770932709.222409 ('data for free up to 15K installs'); ENG-2451.",
  ["WD179"], ["the AppsFlyer row at 0 a month (or free)"], "A paid amount fails.")
t("P52", "The Agent puts Metabase and dbt on its plan sheet at $100 a month each (or $200 a month on one combined row)",
  "Multi-source: Arthur's later mail supersedes the ~$300 on ENG-2447 and in the draft.",
  "Arthur's mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> ('it's the $100 base now, dbt is $100'); ENG-2447 ('about $300 a month with dbt'); draft row 'Metabase + dbt, ~300'.",
  ["BILL"], ["Metabase 100 and dbt 100, or one Metabase + dbt row at 200"], "300 fails.")
t("P53", "The Agent puts GitHub on its plan sheet at $48 a month",
  "Lookup: one record gives it.",
  "Arthur's mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> ('github is back to the $48 team plan').",
  ["BILL"], ["the GitHub row at 48 a month"], "0 or no GitHub row fails.")
t("P54", "The Agent marks the GitHub row of its plan sheet as paid by Arthur Blake himself",
  "Interpretation: the org stays HG's but Arthur pays the bill.",
  "Arthur's mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> ('I'm just paying the bill, so count it as mine').",
  ["BILL"], ["GitHub paid by Arthur / Blake"], "Paid by HG or the LLC fails.")
t("P55", "The Agent puts the Playable vendor on its plan sheet at $0 a month (0, or a blank cost marked as a one-off)",
  "Interpretation: the ground rules leave one-offs out of the monthly plan.",
  "Ground rules f_1e468a9d69ea0f0a2001f5 ('no one-offs or yearly fees'); ENG-2474 ('$3,750 for the first playable, one-off'); C09UHHN6PFZ/1770845002.610529.",
  ["RULES", "P672"], ["the Playable vendor row at 0 a month, or blank and marked one-off"], "3,750 or any monthly share of it fails; no Playable vendor row fails.")
t("P56", "The Agent dates the Combo Fighter row of its plan sheet to when Sunset's sale closes (its By)",
  "Interpretation: the card moves anything that comes through Sunset's sale when the sale closes.",
  "Ground rules f_1e468a9d69ea0f0a2001f5 ('comes to it only through Sunset's sale'); LLC card ('Anything that comes through Sunset's sale moves when the sale closes').",
  ["RULES"], ["Combo Fighter By: when Sunset's sale closes (at the sale, on close)"], "Mar 1 fails.")
t("P57", "The Agent dates the Domino Delights production account (AWS) row of its plan sheet by March 1 (Mar 1, 3/1, 2026-03-01 or the end of February)",
  "Interpretation: everything else moves by March 1, and the account bills the LLC from March.",
  "Arthur's DM reply D04V95AAAHW/1770952200.665739 ('that's what it bills from March'); LLC card ('everything else moves by March 1').",
  ["DD140"], ["By: Mar 1, 3/1, 2026-03-01 or the end of February"], "'when the sale closes' or a later date fails.")
t("P58", "The Agent puts the three monthly shares on its plan sheet at $1,150 each (Arthur Blake's may read $902 in cash plus the $248 he already pays)",
  "Multi-source: every cost line, the VO line and the split rule (a third each of $3,450; carried costs count toward a third).",
  "Leonard's mail robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com> ('each of the three of us carries a third'; 'put the three shares on the sheet per month').",
  ["SPLIT"], ["1,150 a month for each of the three; Arthur's as 902 cash plus his 248"], "$150 (no VO), 1,067 (on 3,202) or Arthur paying 1,150 cash on top of 248 fails.")
# ---------------------------------------------------------------- Shares
t("P59", "The Agent shares its plan sheet with leonard.hayes@harmonygames.co (Leonard Hayes; writer, commenter or reader)",
  "Lookup: the DM asks to share it with Leonard.",
  "Leonard's DM D04UP2L3E3S/1770961200.890407 ('share it with Blake and me'); Contacts leonard.hayes@harmonygames.co.",
  ["CL", "HUB"], ["the new plan sheet shared with leonard.hayes@harmonygames.co in any role"], "Sharing only Leonard's draft fails.")
t("P60", "The Agent shares its plan sheet with arthur.blake@harmonygames.co (Arthur Blake; writer, commenter or reader)",
  "Lookup: 'Blake' in the prompt and the DM is Arthur Blake.",
  "Leonard's DM D04UP2L3E3S/1770961200.890407 ('share it with Blake and me'); Contacts arthur.blake@harmonygames.co.",
  ["CA", "HUB"], ["the new plan sheet shared with arthur.blake@harmonygames.co in any role"], "Sharing with another address fails.")
# ---------------------------------------------------------------- Reply
t("P61", f"The Agent links its plan sheet (a Google Sheets or Drive URL of it) in its reply in {DM}",
  "Lookup: the prompt asks for the link in that DM thread.",
  "Leonard's DM D04UP2L3E3S/1770961200.890407 (thread_ts 1770961200.890407).",
  ["HUB"], ["a thread reply under 1770961200.890407 holding the new sheet's Sheets or Drive URL"], "Linking Leonard's draft, or a reply outside that thread, fails.")
t("P62", f"The Agent says in its reply in {DM} that the LLC takes Domino Delights",
  "Interpretation: the reply states the Domino Delights call ('what I'd do').",
  "Ground rules f_1e468a9d69ea0f0a2001f5 (the take test); Arthur's DM D04V95AAAHW/1770952200.665739 ($140); REVENUE_DAILY January 183.11.",
  ["RULES", "DD140"], ["the reply says Domino Delights comes over, is taken or is kept by the LLC"], "A reply taking only Combo Fighter fails.")
t("P63", f"The Agent says in its reply in {DM} that Zombie Match stays with HG (or names Combo Fighter and Domino Delights as the only games the LLC takes)",
  "Interpretation: the reply states the Zombie Match call ('what I'd do').",
  "Ground rules f_1e468a9d69ea0f0a2001f5 (the take test); REVENUE_DAILY January 0.00.",
  ["RULES"], ["Zombie Match stays with HG / Sunset, or the LLC takes only Combo Fighter and Domino Delights"], "A reply taking all three games fails.")
t("P64", f"The Agent gives $1,150 a month as what it costs each of the three in its reply in {DM} (Arthur Blake's may read $902 in cash plus the $248 he already pays; a reply that has Arthur put in $1,150 cash on top of his $248 fails)",
  "Multi-source: every cost line, the VO line and the split rule.",
  "Leonard's mail robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com> ('whatever one of us already pays personally counts toward his third, and he puts the difference in as cash').",
  ["SPLIT"], ["1,150 a month each; Arthur's may read 902 cash plus his 248"], "$150, 1,067, or Arthur at 1,150 cash plus 248 fails.")
# ---------------------------------------------------------------- Process
t("P65", f"The Agent posts its reply in {DM} only after its Linear, plan-sheet and sharing writes are finished (none of them after the reply)",
  "Lookup: the prompt orders the reply last ('When you're done ... Then reply'); no Outcome row can show the order.",
  "Prompt; Leonard's DM D04UP2L3E3S/1770961200.890407 ('then tell me here what you'd do').",
  ["HUB"], ["the thread reply comes after every Linear, sheet and Drive-share write"], "Any of those writes after the reply fails.")

# ------------------------------------------------------------------ check-mode revision 1 (2026-11-06)
T.pop("P10")
REPLY = "in its reply to Leonard Hayes in his DM with Robert"
HGL = "HG (Harmony Games, stays with HG, Canceled or cancelled)"
HGC = "HG (Harmony Games, HG keeps it, or cancelled)"


def retitle(p, title, **k):
    T[p].update(title=title, **k)


retitle("P1", "The Agent creates a new issue in the LLC take-over project in Linear for Combo Fighter's VO campaign on Meta (its title names the VO campaign, the Meta campaign or Combo Fighter's ads)",
        acc=["a new issue in the LLC take-over project whose title names Combo Fighter's VO / Meta / ads campaign"])
retitle("P2", "The Agent puts its new Combo Fighter VO campaign issue in the Todo state")
retitle("P3", "The Agent assigns its new Combo Fighter VO campaign issue to Leonard Hayes")
retitle("P4", "The Agent comments on its new Combo Fighter VO campaign issue that the LLC takes it (pays for it)")
retitle("P5", "The Agent adds a comment stating its call (the LLC takes it, it stays with HG, or one of the three pays for it himself) to every one of the 37 existing issues in the LLC take-over project in Linear",
        acc=["a new comment stating a call on each of the 37 existing issues"], alt="36 or fewer issues with a call, or comments that give no call ('see sheet'), fail.")
retitle("P7", f"The Agent comments on ENG-2453 (Figma) that it stays with {HGC}")
retitle("P8", f"The Agent comments on ENG-2472 (Calm Play LLC) that it stays with {HGC}")
retitle("P11", f"The Agent comments on ENG-2457 (Cursor) that it stays with {HGC}")
retitle("P15", "The Agent assigns ENG-2439 (Domino Delights) to Leonard Hayes",
        src="ENG-2439 comment by Leonard ('I'll handle it with Sunset'); Leonard's #prototype post C09UHHN6PFZ/1770844309.583109 ('Domino Delights is with boombit'); Leonard Hayes = leonard.hayes@harmonygames.co.",
        srcs=["DDB", "CL"])
retitle("P36", "The Agent marks exactly 7 rows of its plan sheet as the LLC's (taken or paid by the LLC), apart from the Metabase, dbt and GitHub rows that Arthur Blake pays himself",
        acc=["exactly 7 LLC rows, the founder-paid Metabase, dbt and GitHub rows not counted"], alt="6 (no VO row) or 8 or more LLC rows besides the founder-paid ones fail.")
retitle("P39", f"The Agent marks the Zombie Match row of its plan sheet as staying with HG (Harmony Games, stays with HG, Sunset's sale, Canceled or cancelled)")
retitle("P41", f"The Agent marks the Calm Play LLC row of its plan sheet as staying with {HGL}")
retitle("P42", f"The Agent marks the Figma row of its plan sheet as staying with {HGL}")
retitle("P43", f"The Agent marks the Helpshift row of its plan sheet as staying with {HGL}")
retitle("P44", f"The Agent marks the Cursor row of its plan sheet as staying with {HGL}")
retitle("P52", "The Agent puts Metabase on its plan sheet at $100 a month (or Metabase and dbt together at $200 on one combined row)",
        acc=["Metabase at 100, or one Metabase + dbt row at 200"], alt="300 (the draft and ENG-2447) fails.")
retitle("P55", "The Agent puts the Playable vendor on its plan sheet at $0 a month (0, or a blank cost marked as a one-off)",
        src="Ground rules f_1e468a9d69ea0f0a2001f5 ('this plan is only what bills us every month, no one-offs or yearly fees'); ENG-2474 comment ('$3,750 for the first playable, one-off').",
        srcs=["RULES"])
retitle("P56", "The Agent dates the Combo Fighter row of its plan sheet to when Sunset's sale closes (in its By or its step)")
retitle("P57", "The Agent dates the Domino Delights production account (AWS) row of its plan sheet by March 1 (Mar 1, 3/1, 2026-03-01 or the end of February, in its By or its step)")
retitle("P58", "The Agent puts the three monthly shares on its plan sheet at $1,150 each, Arthur Blake's counting the $248 he already pays (or shown as $902 in cash plus that $248; a sheet that has Arthur put in $1,150 cash on top of his $248 fails)",
        acc=["1,150 a month each; Arthur's as 1,150 counting his 248 or as 902 cash plus 248"])
retitle("P61", f"The Agent links its plan sheet (a Google Sheets or Drive URL of it) {REPLY}",
        acc=["a reply to Leonard in D04UP2L3E3S holding the new sheet's Sheets or Drive URL"], alt="Linking Leonard's draft fails.")
retitle("P62", f"The Agent says {REPLY} that the LLC takes Domino Delights")
retitle("P63", f"The Agent says {REPLY} that Zombie Match stays with HG (or names Combo Fighter and Domino Delights as the only games the LLC takes)")
retitle("P64", f"The Agent gives $1,150 a month as what it costs each of the three {REPLY} (Arthur Blake's may read $902 in cash plus the $248 he already pays; a reply that has Arthur put in $1,150 cash on top of his $248 fails)")
retitle("P65", f"The Agent posts its reply to Leonard Hayes in his DM with Robert only after its Linear, plan-sheet and sharing writes are finished (none of them after the reply)",
        acc=["the reply to Leonard comes after every Linear, sheet and Drive-share write"])
t("P68", "The Agent gives its plan sheet exactly 38 item rows, one per issue in the LLC take-over project plus the Combo Fighter VO campaign (37 if Metabase and dbt share a row as on the draft), besides any header, total or share lines",
  "Comparison: the whole item list against the sheet; the output volume of the plan sheet (rubric-sampling-v1).",
  "Project LLC take-over 0fa95761-d59b-4ff4-a8a3-15df3210ca6e (37 issues ENG-2438 to ENG-2474); the VO line C09UHHN6PFZ/1770938400.370665; draft f_d996e4c434ce160dc52596 ('Metabase + dbt' on one row).",
  ["HUB", "VO"], ["38 item rows, or 37 with Metabase and dbt combined"], "A sheet listing only the LLC rows, or dropping items, fails.")
t("P69", "The Agent comments on ENG-2439 (Domino Delights) that the LLC takes it",
  "Multi-source: January revenue $183.11 (warehouse) covers the $140 its hosting bills now (Arthur's DM) under the ground rules' take test.",
  "Ground rules f_1e468a9d69ea0f0a2001f5 (the January take test); Arthur's DM reply D04V95AAAHW/1770952200.665739 ('$140 a month now'); REVENUE_DAILY January sum 183.11; ENG-2439.",
  ["RULES", "DD140"], ["a comment on ENG-2439 giving the LLC as its call (any wording)"], "An HG call (the stale ~$1k) fails.")
t("P70", f"The Agent comments on ENG-2440 (Zombie Match) that it stays with {HGC}",
  "Multi-source: Zombie Match made $0.00 in January (warehouse), which covers none of its hosting, under the take test; the Monday notes' 'DD and ZM both come with CF' is overruled.",
  "Ground rules f_1e468a9d69ea0f0a2001f5 ('whatever we said about them before'); REVENUE_DAILY January sum 0.00; ENG-2443 ('it bills every month on HG's AWS bill').",
  ["RULES"], ["a comment on ENG-2440 that it stays with HG (or goes in Sunset's sale)"], "An LLC call fails.")
t("P71", "The Agent posts its reply to Leonard Hayes in the thread under his Thursday-night DM to Robert (thread_ts 1770961200.890407)",
  "Lookup: the prompt asks for the reply in that DM thread.",
  "Leonard's DM D04UP2L3E3S/1770961200.890407 (thread_ts 1770961200.890407).",
  ["HUB"], ["a reply in D04UP2L3E3S with thread_ts 1770961200.890407"], "A new top-level message in the DM fails.")
t("P72", "The Agent names Arthur Blake as the Owner of the Domino Delights production account (AWS) row of its plan sheet",
  "Lookup: Arthur runs the account.",
  "Arthur's DM reply D04V95AAAHW/1770952200.665739; draft f_d996e4c434ce160dc52596 Owner column ('Blake'); arthur.blake@harmonygames.co.",
  ["DD140", "CA"], ["Owner: Arthur, Blake or Arthur Blake"], "Leonard, Robert or a blank Owner fails.")
t("P73", "The Agent names Leonard Hayes as the Owner of the Combo Fighter VO campaign row of its plan sheet",
  "Lookup: the campaign is on Leonard's card.",
  "Leonard's reply C09UHHN6PFZ/1770938400.370665 ('it's on my card till the end of Feb'); leonard.hayes@harmonygames.co.",
  ["VO", "CL"], ["Owner: Leonard or Leonard Hayes"], "Robert, Arthur or a blank Owner fails.")
t("P76", "The Agent puts dbt on its plan sheet at $100 a month (or Metabase and dbt together at $200 on one combined row)",
  "Multi-source: Arthur's later mail supersedes the ~$300 on ENG-2447 and in the draft.",
  "Arthur's mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> ('dbt is $100'); ENG-2448 ('same as metabase, the two go together'); draft row 'Metabase + dbt, ~300'.",
  ["BILL"], ["dbt at 100, or one Metabase + dbt row at 200"], "300 or 0 fails.")

# ------------------------------------------------------------------ /rubric round 1 Fix List (exact titles; 2026-11-06)
import json as _json, os as _os
_IT = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "issue_titles.json")))
for _p in ("P5", "P27", "P36", "P49", "P76", "P71"):
    T.pop(_p)
THREAD = "in its reply in the thread under Leonard Hayes's Thursday-night DM to Robert"
HGC2 = "HG (Harmony Games, HG keeps it, or cancelled)"
retitle("P1", "The Agent creates a new issue in the LLC take-over project in Linear for Combo Fighter's VO campaign on Meta (its title or description names the VO campaign)",
        acc=["a new issue in the LLC take-over project whose title or description names Combo Fighter's VO campaign"],
        acc_note="any title or description naming that campaign passes (risk 1)", alt="An issue for another campaign (the paused install campaign), or a mention only in a comment, fails.")
retitle("P6", T["P6"]["title"], just="Multi-source: the ground rules bring a game's player support with the game, and Domino Delights comes over on the take test (January revenue $183.11 in the warehouse against the $140 its hosting bills now).")
retitle("P15", T["P15"]["title"], src="ENG-2439 comment by Leonard ('I'll handle it with Sunset'); Leonard Hayes = leonard.hayes@harmonygames.co.", srcs=["CL"])
retitle("P16", T["P16"]["title"], just="Multi-source: Domino Delights comes over on the take test (January revenue $183.11 against the $140 hosting), and the account's billing still has to move off HG's AWS bill.")
retitle("P28", T["P28"]["title"], just="Multi-source: Zombie Match made $0.00 in January (warehouse), which covers none of its hosting, under the ground rules' take test.")
retitle("P34", T["P34"]["title"], alt="Editing Leonard's draft in place fails; a sheet outside Robert's Drive fails.")
retitle("P68", "The Agent gives its plan sheet exactly 38 item rows (37 if Metabase and dbt share one row as on the draft), besides any header, total or share lines",
        acc=["38 item rows, or 37 with Metabase and dbt combined"])
retitle("P39", "The Agent marks the Zombie Match row of its plan sheet as staying with HG (Harmony Games, stays with HG, Canceled or cancelled)",
        just="Multi-source: $0.00 January revenue (warehouse) covers none of its hosting under the ground rules' take test.", acc=["Zombie Match row: HG, stays with HG, Canceled or cancelled"])
retitle("P40", T["P40"]["title"], just="Interpretation: Arthur's mail settles the draft's open '?' and #winddown's '$300/month' for Metabase + dbt.")
retitle("P43", T["P43"]["title"], just="Interpretation: the ground rules bring Domino Delights' player support with it, but Helpshift itself is being cancelled.")
retitle("P45", T["P45"]["title"], just="Interpretation: the $3,000 monthly cap over the $100/day budget, from the #prototype thread outside the Linear project.")
retitle("P66", "The Agent dates the support-build step on the Domino Delights player support row of its plan sheet due from Feb 13 to Feb 28 (a due date in that range, 'by Feb 28' or 'before Feb 28', in its By or its step)",
        acc=["a due date from Feb 13 to Feb 28, 'by Feb 28' or 'before Feb 28', in the By cell or the step text"], alt="Mar 1 (the card's default), a later date or a past date fails.")
retitle("P48", T["P48"]["title"], just="Interpretation: Leonard's thread reply asks Robert to pull the art out; ENG-2454 only says it was cancelled.")
retitle("P67", "The Agent dates the layer.ai concept-art step on its plan sheet from Feb 13 to Mar 3 (a date in that range, 'by Mar 3' or 'before Mar 3', in its By or its step)",
        acc=["a date from Feb 13 to Mar 3, 'by Mar 3' or 'before Mar 3', in the By cell or the step text"], alt="A past date (the Feb 11 cancellation), a later date or no date fails.")
retitle("P50", T["P50"]["title"], just="Interpretation: Arthur's later mail ($62) supersedes his 'about $95' on ENG-2445.")
retitle("P52", "The Agent puts Metabase on its plan sheet at $100 a month on a row of its own, or Metabase and dbt together at $200 a month on one combined row as on the draft",
        acc=["Metabase at 100 on its own row, or one Metabase + dbt row at 200"])
retitle("P55", "The Agent puts the Playable vendor on its plan sheet at $0 a month (0 or a blank monthly cost; a note beside it that the $3,750 is a one-off is fine)",
        acc=["the Playable vendor row at 0 or a blank monthly cost"])
retitle("P57", "The Agent dates the Domino Delights production account (AWS) row of its plan sheet from Feb 13 to Mar 1 (a date in that range, 'by Mar 1' or 'before Mar 1', in its By or its step)",
        acc=["a date from Feb 13 to Mar 1, 'by Mar 1' or 'before Mar 1', in the By cell or the step text"], alt="'when the sale closes', a later date or a past date fails.")
retitle("P72", "The Agent names Arthur Blake (Arthur Blake, Arthur or Blake) as the Owner of the Domino Delights production account (AWS) row of its plan sheet")
retitle("P58", "The Agent puts the per-person monthly share on its plan sheet at $1,150 (a third of the $3,450 monthly total; Arthur Blake's line may read $902 cash, with or without the $248 he already pays beside it, but not $1,150 cash on top of that $248)",
        acc=["1,150 per person a month; Arthur's line may read 902 cash, with or without his 248 beside it"], alt="$150 (no VO), 1,067 (on 3,202) or Arthur at 1,150 cash on top of 248 fails.")
retitle("P61", f"The Agent links its plan sheet (a Google Sheets or Drive URL of it) {THREAD}",
        acc=["a thread reply under 1770961200.890407 holding the new sheet's Sheets or Drive URL"], alt="Linking Leonard's draft, or a reply outside that thread, fails.")
retitle("P62", f"The Agent says {THREAD} that the LLC takes Domino Delights",
        just="Multi-source: the reply states the take-test call (January revenue in the warehouse, Arthur's $140 DM, the ground rules).")
retitle("P63", f"The Agent says {THREAD} that Zombie Match stays with HG (or names Combo Fighter and Domino Delights as the only games the LLC takes)",
        just="Multi-source: the reply states the take-test call (January revenue in the warehouse, the ground rules).")
retitle("P64", f"The Agent gives $1,150 a month as each of the three's total monthly cost (Robert, Leonard Hayes and Arthur Blake, Arthur's total counting the $248 he already pays; his may be given as $902 cash plus that $248) {THREAD}",
        acc=["1,150 a month each as each one's total; Arthur's may read 902 cash plus his 248"], alt="$150, 1,067, or Arthur at 1,150 cash plus 248 fails; a reply outside that thread fails.")

# ---- new rows from the Fix List (exact titles)
SRC = {  # deciding records per issue: (catalog keys, evidence text)
    "ENG-2438": (["RULES"], "Ground rules f_1e468a9d69ea0f0a2001f5 ('Combo Fighter comes over either way'); ENG-2438 comment ('robert's game. all of it is HG's IP today')."),
    "ENG-2441": (["RULES", "DD140"], "Ground rules f_1e468a9d69ea0f0a2001f5 (the take test; 'brings what it needs to keep running, its accounts'); Arthur's DM reply D04V95AAAHW/1770952200.665739 ('down to $140 a month now'); REVENUE_DAILY January sum 183.11."),
    "ENG-2442": (["RULES"], "Ground rules f_1e468a9d69ea0f0a2001f5 ('brings what it needs to keep running'); ENG-2442 comment ('nothing runs on dev anymore, shutting it down')."),
    "ENG-2443": (["RULES"], "Ground rules f_1e468a9d69ea0f0a2001f5 (the take test); REVENUE_DAILY January sum 0.00 for zombie_match_3d; ENG-2443 comment ('it bills every month on HG's AWS bill')."),
    "ENG-2444": (["RULES"], "Ground rules f_1e468a9d69ea0f0a2001f5; ENG-2444 comment ('kinesis and glue only ever carried DD and ZM events, CF's go through firebase. shutting it down')."),
    "ENG-2445": (["JENK"], "Arthur's mail robert@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com> ('so CF's own account bills $62 a month now, just its live stacks'); ENG-2445 comment."),
    "ENG-2446": (["JENK"], "Arthur's mail robert@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com> ('the build boxes are HG's, they can go with the laptops'); ENG-2446 comment."),
    "ENG-2447": (["BILL"], "Arthur's mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> ('github, dbt and metabase bill to my Kub card'; 'I'll carry those through May as my part'); ENG-2447."),
    "ENG-2448": (["BILL"], "Arthur's mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> ('dbt is $100'; 'I'll carry those through May as my part'); ENG-2448."),
    "ENG-2449": (["BILL"], "Arthur's mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> ('github is back to the $48 team plan'); ENG-2449."),
    "ENG-2450": (["WD179"], "#winddown C0ADGSZKR3R/1770932709.222409 ('if Singular shuts down our access'); ENG-2450 comment ('termination letter is the one in #winddown')."),
    "ENG-2451": (["WD179"], "#winddown C0ADGSZKR3R/1770932709.222409 ('data for free up to 15K installs'); ENG-2451 comment ('CF goes on appsflyer's free tier from March')."),
    "ENG-2452": (["WD190"], "#winddown action items C0ADGSZKR3R/1770933903.645709 ('We keep accounts that has our data ... Slack, google, google analytics, github under Harmony Games'); ENG-2452."),
    "ENG-2454": (["LAYER"], "Leonard's reply C09UHHN6PFZ/1770923700.470906 ('there's nothing on the layer account for our new company to take, it just lapses'); ENG-2454."),
    "ENG-2455": (["WD188"], "#winddown C0ADGSZKR3R/1770933601.686309 ('I canceled other subscriptions under mine'); ENG-2455 comment ('robert cancelled it on the 11th')."),
    "ENG-2456": (["WD190"], "#winddown action items C0ADGSZKR3R/1770933903.645709 (Arthur to cancel subscriptions); ENG-2456 comment ('cancelled, Pro runs to Feb 25')."),
    "ENG-2458": (["WD190"], "#winddown action items C0ADGSZKR3R/1770933903.645709 ('to cancel ..., coderabbit, cursor'); ENG-2458 comment ('cancelled on the 12th')."),
    "ENG-2459": (["WD190"], "#winddown action items C0ADGSZKR3R/1770933903.645709 ('to email Unity with the email template'); ENG-2459 comment ('CF is fine on unity personal')."),
    "ENG-2460": (["WD188"], "#winddown C0ADGSZKR3R/1770933601.686309 ('I canceled other subscriptions under mine'); ENG-2460 comment ('cancelled')."),
    "ENG-2461": (["WD57"], "#winddown C0ADGSZKR3R/1770789534.434749 ('Looks like Helpshift is gonna cancel our subscription'); ENG-2461 comment ('they're cancelling without a hassle')."),
    "ENG-2463": (["WD190"], "#winddown action items C0ADGSZKR3R/1770933903.645709 ('We keep accounts that has our data ... Slack, google ... under Harmony Games'); ENG-2463."),
    "ENG-2464": (["WD190"], "#winddown action items C0ADGSZKR3R/1770933903.645709 ('We keep accounts that has our data ... Slack, google ... under Harmony Games'); ENG-2464."),
    "ENG-2465": (["WD188"], "#winddown C0ADGSZKR3R/1770933601.686309 ('linear we keep during transition'); ENG-2465."),
    "ENG-2466": (["WD188"], "#winddown C0ADGSZKR3R/1770933601.686309 ('During shutdown, let’s keep Deel, gusto, Intuit'); ENG-2466."),
    "ENG-2467": (["WD188"], "#winddown C0ADGSZKR3R/1770933601.686309 ('During shutdown, let’s keep Deel, gusto, Intuit'); ENG-2467."),
    "ENG-2468": (["WD188"], "#winddown C0ADGSZKR3R/1770933601.686309 ('During shutdown, let’s keep Deel, gusto, Intuit'); ENG-2468."),
    "ENG-2469": (["RULES"], "Ground rules f_1e468a9d69ea0f0a2001f5 ('this plan is only what bills us every month, no one-offs or yearly fees'); ENG-2469 comment ('renewal is 8/15')."),
    "ENG-2470": (["RULES"], "Ground rules f_1e468a9d69ea0f0a2001f5 ('the games with their art and listings ... only through Sunset's sale'); ENG-2470 comment ('HG's account. CF's listing sits in it and moves with the game')."),
    "ENG-2471": (["RULES"], "Ground rules f_1e468a9d69ea0f0a2001f5 ('no one-offs or yearly fees'); ENG-2471 comment ('HG's account, one-time fee, nothing monthly')."),
    "ENG-2473": (["RULES", "P672"], "Ground rules f_1e468a9d69ea0f0a2001f5 ('no one-offs'); #prototype C09UHHN6PFZ/1770845002.610529 ('happy to spend $100 we have on this'); ENG-2473 comment ('goes on this week's playable test, then nothing')."),
    "ENG-2474": (["RULES"], "Ground rules f_1e468a9d69ea0f0a2001f5 ('no one-offs or yearly fees'); ENG-2474 comment ('$3,750 for the first playable, one-off')."),
}
LABEL = {1: "Lookup", 3: "Interpretation", 5: "Multi-source"}
_CALLS = [("ENG-2438", "LLC", 1), ("ENG-2441", "LLC", 5), ("ENG-2442", "HG", 3), ("ENG-2443", "HG", 5), ("ENG-2444", "HG", 3), ("ENG-2445", "LLC", 3),
          ("ENG-2446", "HG", 3), ("ENG-2447", "AB", 3), ("ENG-2448", "AB", 3), ("ENG-2450", "HG", 1), ("ENG-2451", "LLC", 3), ("ENG-2452", "HG", 1),
          ("ENG-2454", "HG", 1), ("ENG-2455", "HG", 1), ("ENG-2456", "HG", 1), ("ENG-2458", "HG", 1), ("ENG-2459", "HG", 1), ("ENG-2460", "HG", 1),
          ("ENG-2461", "HG", 3), ("ENG-2463", "HG", 1), ("ENG-2464", "HG", 1), ("ENG-2465", "HG", 1), ("ENG-2466", "HG", 1), ("ENG-2467", "HG", 1),
          ("ENG-2468", "HG", 1), ("ENG-2469", "HG", 3), ("ENG-2470", "HG", 3), ("ENG-2471", "HG", 3), ("ENG-2473", "HG", 3), ("ENG-2474", "HG", 3)]
for i, (k, call, w) in enumerate(_CALLS):
    end = {"LLC": "that the LLC takes it", "AB": "that Arthur Blake pays for it himself", "HG": f"that it stays with {HGC2}"}[call]
    srcs, ev = SRC[k]
    t(f"P{101 + i}", f"The Agent comments on {k} ({_IT[k]}) {end}",
      f"{LABEL[w]}: the call on {_IT[k]} from its own records under the project rule ('Leave your call on each one as a comment').",
      ev, srcs, [f"a comment on {k} giving that call (any wording)"],
      {"LLC": "An HG call fails.", "AB": "An LLC or HG call fails.", "HG": "An LLC call fails."}[call])
t("P131", "The Agent gives the VO campaign's cost as $3,000 a month (or $9,000 for March through May) in its comment on its new Combo Fighter VO campaign issue",
  "Interpretation: the $3,000 monthly cap over the $100/day budget; the DM makes the cost part of the call.",
  "Leonard's reply C09UHHN6PFZ/1770938400.370665 ('capped at $3,000 a month, and that's what it runs at from March'); Leonard's DM D04UP2L3E3S/1770961200.890407 ('what it costs us March through May').",
  ["VO"], ["3,000 a month or 9,000 for March through May, in the comment on the new VO issue"], "$100/day without the monthly figure, 3,100 or no cost fails.")
t("P132", "The Agent gives Combo Fighter's cost as $0 (0, nothing or no cost) in its comment on ENG-2438 (Combo Fighter)",
  "Lookup: the draft's Combo Fighter row is 0; the DM makes the cost part of the call.",
  "Leonard's draft f_d996e4c434ce160dc52596 (row 'Combo Fighter, CF, LLC, 0'); Leonard's DM D04UP2L3E3S/1770961200.890407 ('what it costs us March through May').",
  ["DRAFT"], ["0, nothing or no cost, in the comment on ENG-2438"], "A positive monthly cost fails.")
t("P133", "The Agent gives the account's cost as $140 a month (or $420 for March through May) in its comment on ENG-2441 (Domino Delights production account (AWS))",
  "Multi-source: Arthur's later DM supersedes the ~$1k and 300 in #winddown, on ENG-2441 and in the draft.",
  "Arthur's DM reply D04V95AAAHW/1770952200.665739 ('down to $140 a month now'); superseded C0ADGSZKR3R/1770680984.725779 ('~$1k').",
  ["DD140"], ["140 a month or 420 for March through May, in the comment on ENG-2441"], "1,000, 300 or no cost fails.")
t("P134", "The Agent gives the stacks' cost as $62 a month (or $186 for March through May) in its comment on ENG-2445 (Combo Fighter backend and auth stacks (AWS))",
  "Interpretation: Arthur's later mail ($62) supersedes his 'about $95' on ENG-2445.",
  "Arthur's mail robert@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com> ('bills $62 a month now'); ENG-2445 comment ('about $95').",
  ["JENK"], ["62 a month or 186 for March through May, in the comment on ENG-2445"], "95 or no cost fails.")
t("P135", "The Agent gives Metabase's cost in its comment on ENG-2447 (Metabase) as $100 a month or $300 for March through May (or Metabase and dbt together as $200 a month or $600 for March through May; or Metabase, dbt and GitHub together as $248 a month or $744 for March through May)",
  "Multi-source: Arthur's later mail supersedes the ~$300 on ENG-2447, in #winddown and in the draft.",
  "Arthur's mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> ('it's the $100 base now, dbt is $100 and github is back to the $48 team plan'; 'so $248 a month').",
  ["BILL"], ["the Metabase cost in one of the listed forms, in the comment on ENG-2447"], "~300 a month (the stale figure) or no cost fails.")
t("P136", "The Agent gives dbt's cost in its comment on ENG-2448 (dbt) as $100 a month or $300 for March through May (or Metabase and dbt together as $200 a month or $600 for March through May; or Metabase, dbt and GitHub together as $248 a month or $744 for March through May)",
  "Multi-source: Arthur's later mail supersedes the ~$300 figures.",
  "Arthur's mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> ('dbt is $100'; 'so $248 a month').",
  ["BILL"], ["the dbt cost in one of the listed forms, in the comment on ENG-2448"], "~300 a month or no cost fails.")
t("P137", "The Agent gives GitHub's cost in its comment on ENG-2449 (GitHub) as $48 a month or $144 for March through May (or Metabase, dbt and GitHub together as $248 a month or $744 for March through May)",
  "Lookup: one mail gives it.",
  "Arthur's mail robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com> ('github is back to the $48 team plan').",
  ["BILL"], ["the GitHub cost in one of the listed forms, in the comment on ENG-2449"], "No cost or another figure fails.")
t("P138", "The Agent gives AppsFlyer's cost as $0 (0, free, the free tier, nothing or no cost) in its comment on ENG-2451 (AppsFlyer)",
  "Lookup: Combo Fighter goes on AppsFlyer's free tier.",
  "#winddown C0ADGSZKR3R/1770932709.222409 ('data for free up to 15K installs'); ENG-2451 comment ('free up to 15K installs').",
  ["WD179"], ["0, free, the free tier, nothing or no cost, in the comment on ENG-2451"], "A paid amount fails.")
_MOVES = [("ENG-2443", 5), ("ENG-2444", 3), ("ENG-2446", 3), ("ENG-2450", 1), ("ENG-2452", 1), ("ENG-2454", 1), ("ENG-2455", 1), ("ENG-2456", 1),
          ("ENG-2458", 1), ("ENG-2459", 1), ("ENG-2460", 1), ("ENG-2461", 3), ("ENG-2463", 1), ("ENG-2464", 1), ("ENG-2465", 1), ("ENG-2466", 1),
          ("ENG-2467", 1), ("ENG-2468", 1), ("ENG-2469", 3), ("ENG-2471", 3), ("ENG-2473", 3), ("ENG-2474", 3)]
for i, (k, w) in enumerate(_MOVES):
    srcs, ev = SRC[k]
    t(f"P{141 + i}", f"The Agent moves {k} ({_IT[k]}) to Canceled",
      f"{LABEL[w]}: the project rule puts an item that stays with HG in Canceled ('to Canceled if it stays with HG'), and its records keep {_IT[k]} with HG.",
      ev + " Project rule (0fa95761-d59b-4ff4-a8a3-15df3210ca6e): 'to Canceled if it stays with HG'.", srcs, [f"{k} in Canceled"], "Backlog, Todo or Done fail.")
t("P171", "The Agent creates exactly one new issue in the LLC take-over project in Linear",
  "Interpretation: one plan line is missing from the project (the VO campaign); the thread and Arthur's mail name decoys that need no issue.",
  "Leonard's reply C09UHHN6PFZ/1770938400.370665 ('of the meta campaigns only the VO one is still on (I paused the install one'); Arthur's mail robert@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com>.",
  ["VO", "HUB"], ["exactly one new issue in the LLC take-over project"], "No new issue, or extra issues (the paused install campaign, firebase, bigquery), fail.")
t("P172", "The Agent puts DD (or Domino Delights) in the Game column of the Domino Delights production account (AWS) row of its plan sheet",
  "Lookup: the draft's DD row carries Game DD.",
  "Leonard's draft f_d996e4c434ce160dc52596 (row 'DD servers, DD').",
  ["DRAFT"], ["Game: DD or Domino Delights on the DD production account row"], "CF, ZM or a blank Game fails.")
t("P173", "The Agent marks the Combo Fighter VO campaign row of its plan sheet as paid by the LLC (the new company's card from March)",
  "Interpretation: the campaign is on Leonard's card only through February and moves to the new company's card from March.",
  "Leonard's reply C09UHHN6PFZ/1770938400.370665 ('it's on my card till the end of Feb and moves to our new company's card from March').",
  ["VO"], ["Paid by: the LLC, the new company or its card"], "Paid by Leonard (his card till February) or HG fails.")
