#!/usr/bin/env python3
"""Write task_inputs/08_Oracle_Events.md. Every double-quoted span on an Expected line must be a substring of a record
(injection SQL, or a record re-read through hg.py into oe_cache.json); every figure must be in a record or in the derived
list below. Em dashes are refused, so the file carries none."""
import json
import os
import re

import oe_data as D
import oe_lib as L

n = D.n
T = D.TRUTH
EV = []
# spans added after the blind review: each is asserted against its own record
for svc, f, p, q in [
    ("slack", "messages/D05SDEQEK61/2026-02.json", "/1/text", "I have some announcements to make"),
    ("gdocs", "data.json", "/docs_documents/262/title", "Due Diligence Disclosures"),
    ("gdocs", "data.json", "/docs_documents/160/title", "Harmony Games Advisor Agreement - [PERSON_NAME_0127]"),
    ("gdocs", "data.json", "/docs_documents/160/body_text", "All shares shall vest on a pro rata basis monthly over a 2-year period."),
    ("gdocs", "data.json", "/docs_documents/160/body_text", "Total Number of Shares of Common Stock: 6,104"),
    ("gmail", "threads/leonard@harmonygames.co_1767980387254277674.json", "/messages/21/body", "vesting over 2 years with standard advisory shares"),
    ("gmail", "threads/leonard@harmonygames.co_1855133803855213163.json", "/messages/2/body", "we see only two realistic paths"),
    ("gmail", "threads/leonard@harmonygames.co_1855133803855213163.json", "/messages/2/subject", "recap option, cap table reset, and next steps"),
    ("gmail", "threads/leonard@harmonygames.co_1856688113228112603.json", "/messages/8/body", "We have preferred stock from a seed round (no SAFEs)."),
    ("gmail", "threads/leonard@harmonygames.co_1856688113228112603.json", "/messages/8/body", "We are out of funds"),
    ("gmail", "threads/leonard@harmonygames.co_1856688113228112603.json", "/messages/8/subject", "wind-down support request"),
    ("gmail", "threads/leonard@harmonygames.co_1773160163779741845.json", "/messages/1/body", "From the disclosure schedule."),
    ("gmail", "threads/leonard@harmonygames.co_1773160163779741845.json", "/messages/1/body", "Board member"),
    ("slack", "messages/C04UTBZL6AX/2023-06.json", "/1550/text", "so Akin, 1% - Kris 0.5%, Deepak 0.1%, [PERSON_NAME_0112] 0.1%, total 1.7%"),
    ("gmail", "threads/leonard@harmonygames.co_1767980387254277674.json", "/messages/21/body", "both [PERSON_NAME_6550] and Akin are happy with 0.5% each vesting over 2 years with standard advisory shares"),
    ("slack", "messages/C0ADGSZKR3R/2026-02.json", "/57/text", "We gotta move domino delights and zombie match off Helpshift before Feb 28th."),
    ("slack", "messages/C0ADGSZKR3R/2026-02.json", "/163/text", "instead of just selling the data we’ll do data licensing agreeement so that we can liquify we can own the entire IP"),
    ("slack", "messages/C0ADGSZKR3R/2026-02.json", "/172/text", "wind down agreement and data agreement reviewed and signed with [USERNAME_26907]"),
    ("slack", "messages/C0ADGSZKR3R/2026-02.json", "/174/text", "the company is insolvent and we have no cash reserves left"),
    ("slack", "messages/C0ADGSZKR3R/2026-02.json", "/7/text", "Given our current runway of less than a month"),
    ("slack", "messages/C0ADGSZKR3R/2026-02.json", "/7/text", "We are initiating an orderly wind-down process and preparing the required board resolutions and documentation."),
    ("slack", "messages/C0ADGSZKR3R/2026-02.json", "/7/text", "Our priorities are to handle employee and contractor obligations properly, meet tax and compliance requirements, close out vendor commitments, and Sunset the products in a controlled way."),
    ("slack", "messages/C0ADGSZKR3R/2026-02.json", "/57/text", "Looks like Helpshift is gonna cancel our subscription"),
    ("slack", "messages/C0ADGSZKR3R/2026-02.json", "/174/text", "we are terminating our Unity Pro licensing agreement effective immediately"),
    ("slack", "messages/C0ADGSZKR3R/2026-02.json", "/197/text", "onboarding with [USERNAME_26907] and giving them the data"),
    ("gmail", "threads/leonard@harmonygames.co_1767980387254277674.json", "/messages/50/date", "7 Jun 2023"),
    ("gmail", "threads/leonard@harmonygames.co_1767980387254277674.json", "/messages/50/body", "both [PERSON_NAME_6550] and Matthew Collins are happy with 0.5% each vesting over 2 years with standard advisory shares"),
    ("slack", "messages/C0ADGSZKR3R/2026-02.json", "/7/text", "Our priorities are to handle employee and contractor obligations properly"),
    ("slack", "messages/C0ADGSZKR3R/2026-02.json", "/7/text", "We will also evaluate what to do with the remaining IP and codebase (archive, sale, or other disposition)"),
    ("gmail", "threads/leonard@harmonygames.co_1847333990408253969.json", "/messages/1/body", "says I cannot exercise online"),
    ("gmail", "threads/leonard@harmonygames.co_1847333990408253969.json", "/messages/0/body", "Ok, let me know how Carta exploration goes."),
]:
    L.assert_quote(L.hg_get(svc, f, p), q, f"{svc}:{f}{p}")
for t in ("1856858053929740799", "1856860994291529096", "1856861229984402233", "1856861323365646598", "1856861400116562076", "1856861462411533365"):
    L.assert_quote(L.hg_get("gmail", f"threads/leonard@harmonygames.co_{t}.json", "/messages/0/body"), "exercising is not recommended because the shares are expected to have no value", t)
L._save()


def add(title, expected):
    EV.append((title, expected))
    return len(EV)


# ---------------------------------------------------------------- reads
OE_PROJECT = add('Find the holder project in Linear (search the projects for "holder", the word in the request)',
    'One project, "Holder records", team ENG, state started, created Thu Feb 12 2026 3:24 PM PT (23:24 UTC). Description: '
    '"The holders, as I said in #winddown: one issue per holder on Carta, live or lapsed, the three of us aside." '
    '"my close-out notes have how each holder gets handled, and the sheet is what Sunset asked for." '
    '"I\'ll pass it to Sunset myself." "Send KPMG\'s confirmation as a reply to all once the sheet is done." '
    '"States once the sheet is done: Canceled where the line holds nothing; otherwise Todo where its own note is waiting for me, and Done where it isn\'t." '
    '"On every issue with no note of its own, Canceled included, say why."')

rows = "; ".join(f"{k} {D.TITLE[k]}, Email: {D.EMAIL[k]}" for k in D.ISSUES)
OE_ISSUES = add(f'List the issues in the Holder records project in Linear (project from OE {OE_PROJECT})',
    f'26 issues, all in Backlog with no assignee, each description one "Email:" line: {rows}.')

figs = "; ".join(f"{k} \"Nov 2024 owner list: {D.LIST_FIG[k]}\"" for k in D.ISSUES if k in D.LIST_FIG)
OE_COMMENTS = add(f'Read the comments on each of the 26 issues in Linear (one call per issue, list from OE {OE_ISSUES})',
    'Two comments on each issue, 52 in all. One is a last-mail line, such as ENG-2441 "Last mail with that address before Feb: May 18, 2024" '
    f'or ENG-2452 "No mail with that address before Feb". The other is the owner-list line: {figs}; ENG-2451 "Not on the Nov 2024 owner list".')

OE_NOTES = add('Find Leonard\'s close-out notes in Drive and read the doc (search Drive for "close-out", the words in the request)',
    'Doc "Stockholder close-out notes", created Thu Feb 12 2026 5:05 PM PT (Fri Feb 13 01:05 UTC), in the folder "Stockholder close-out". It says: '
    '"These replace my earlier outreach notes." "where I left things today in #winddown: the angels are what\'s open from my list, besides the Sunset onboarding" '
    '"the investor email on the Task List: take my draft from #winddown and bring it up to date as a letter I can send. the update outline has the sections" '
    '"the holder sheet comes first, the notes and everything else run off it. Finish my draft one in the folder rather than starting another. Share it and the letter with Robert" '
    '"notes ready for me by Tuesday, as Gmail drafts." "I read and send each note myself" '
    '"everything goes in the close-out folder, not the Wind Down one, that one is the vendor and termination papers" '
    '"Griffin\'s partner gets a heads-up as a reply to all on their own Board position mail from Feb 12, asking for their vote as preferred holders on the dissolution. That one can go out once the sheet is done" '
    '"when the sheet is ready, reply under my list in #winddown and say who goes first" '
    '"Carta is the record, over any date in the letters. If a line\'s last day has passed, it holds nothing." '
    '"One row per issue on the sheet, and the counts go by rows. At most one note per person. The three of us get no row, only the totals." '
    '"Told means a written message about the closing, sent to them directly and delivered, from one of the three of us (a post in a channel doesn\'t count); for a fund, its partner." '
    '"Everyone still holding something gets what they are owed: the closing if they have not been told, their last day if they have one. Whoever\'s last day comes first goes first." '
    '"Each note says what they hold." '
    '"Anything they asked about their holding that we never answered gets answered in their note, if they get one." '
    '"Messages go to the email on each holder\'s issue." '
    '"Labels for the sheet: Nothing, Already told, Closing, Last day, Closing and last day."')

OE_FOLDER = add(f'List the close-out folder in Drive (the folder that holds the notes, OE {OE_NOTES})',
    'Folder "Stockholder close-out" (d_601064334a0b493022fe83) holds three files: the notes, the spreadsheet "Holder list (draft)" (f_5ecaa967db3adcfa440b09) '
    'and the presentation "Harmony Games February 26 Update" (f_75dddccabb26eeea4842c8).')

OE_DRAFT = add(f'Read the draft holder sheet in Sheets ("Holder list (draft)" from OE {OE_FOLDER}, tab Sheet1)',
    'Header Holder, Shares, Notes, then seven holder rows: GRIFFIN GAMING PARTNERS 2,746,693; [PERSON_NAME_0038] 127,162; [PERSON_NAME_11362] 86,470; '
    '[PERSON_NAME_0089] [PERSON_NAME_25152] 81,383; TOR Capital Limited 50,865; PERSON_3941_NAME [PERSON_NAME_0127] 31,536; PERSON_1287_NAME 31,536, '
    'each with the note "copied from the Nov 2024 list", then a last row: "the list\'s percentages leave out the option pool, so they only add to about 94%".')

OE_OUTLINE = add(f'Read the update outline in Slides ("Harmony Games February 26 Update" from OE {OE_FOLDER})',
    'Five slides: "Harmony Games February 26 Update" / "Outline"; "What happened" / "Why we are closing"; "Where things stand" / "Holders, per the Nov 2024 owner list" / '
    '"Board, process, who is running the close"; "What it means for you" / "Distributions, tax papers, your options"; "What happens to the games and the IP" / "Thank you".')

OE_WIND = add('Read #winddown in Slack for Leonard\'s investor email draft and his list (channel named in the request; the posts of Feb 9 to Feb 12 2026)',
    'Leonard\'s draft, Mon Feb 9 2026 11:18 AM PT (19:18 UTC), ts 1770664700.848759: "Hi everyone," "I’m writing to share a difficult update: we have decided to wind down harmonygames." '
    'with the parts "What we did and what we learned", "Financial context", "What happens next" and "Timeline and updates", with the sentence "we do not have the funding to continue operating", ending "If you would like to talk 1:1 this week, reply here and I will make time." '
    'Leonard, Wed Feb 11 2026 12:20 PM PT (20:20 UTC): "All termination letters are sent". '
    'Also in the draft: "Given our current runway of less than a month", "We are initiating an orderly wind-down process and preparing the required board resolutions and documentation.", "Our priorities are to handle employee and contractor obligations properly, meet tax and compliance requirements, close out vendor commitments, and Sunset the products in a controlled way." and "We will also evaluate what to do with the remaining IP and codebase (archive, sale, or other disposition)". '
    'Leonard, Tue Feb 10 2026 9:58 PM PT (Wed Feb 11 05:58 UTC): "Looks like Helpshift is gonna cancel our subscription" and "We gotta move domino delights and zombie match off Helpshift before Feb 28th." '
    'Leonard, Thu Feb 12 2026 11:27 AM PT (19:27 UTC): "instead of just selling the data we’ll do data licensing agreeement so that we can liquify we can own the entire IP". '
    'Leonard, 1:29 PM PT (21:29 UTC): "wind down agreement and data agreement reviewed and signed with [USERNAME_26907]". '
    'Leonard\'s vendor note, 1:35 PM PT (21:35 UTC): "we are terminating our Unity Pro licensing agreement effective immediately" and "the company is insolvent and we have no cash reserves left". '
    'Leonard\'s list, Thu Feb 12 2026 2:17 PM PT (22:17 UTC), ts 1770934638.035469: "next things for me are" with "Reaching out to our angels properly and let them know about the situation" and "onboarding with [USERNAME_26907] and giving them the data". '
    'Leonard, Thu Feb 12 2026 2:33 PM PT (22:33 UTC): "Carta terminations are done". The list post shows four replies.')

OE_THREAD = add(f'Read the replies under Leonard\'s list in #winddown in Slack (thread of ts 1770934638.035469 from OE {OE_WIND})',
    'Four replies, Thu Feb 12 2026 6:21 PM to 6:23 PM PT (Fri Feb 13 02:21 to 02:23 UTC). Leonard: '
    '"One thing on the angels: one note to whoever has always handled it for a family covers the rest of the family\'s lines, which need no note of their own, and that note says what each of them holds" '
    '"Mark those lines Covered on the sheet in place of a label, and count them that way" '
    '"the sheet goes to you as well as Robert, the rest of my notes stands" (addressed to Arthur Blake). Arthur Blake: "sounds good".')

OE_SUNSET = add(f'Read what Sunset asked for in Gmail (search "Sunset stockholder"; the project in OE {OE_PROJECT} says the sheet is what Sunset asked for)',
    'PERSON_2888_NAME (Sunset) to Leonard, Fri Feb 13 2026 10:06 AM PT (18:06 UTC), subject "Sunset: stockholder info for intake": '
    '"One line per holder of stock or options, with what each holds today (for options, what\'s vested) and any last day" '
    '"Total shares and options outstanding" "A count of holders by what each still needs to hear from you" "Directors in office, and who holds the preferred vote".')

OE_KPMG = add('Read KPMG\'s audit request thread in Gmail (search "Audit Request", the words in the request; the thread for the year ended December 31, 2025)',
    'Thread leonard.hayes@harmonygames.co/1857029474983245439, three messages. PERSON_3088_NAME (KPMG) to Leonard, cc PERSON_4416_EMAIL, PERSON_2322_EMAIL and PERSON_2847_EMAIL, '
    'Fri Feb 13 2026 8:48 AM PT (16:48 UTC), subject "GRIFFIN GAMING PARTNERS 2025 Audit Request [SOURCE_ORG_0001], Inc.": '
    '"please confirm the below as of December 31, 2025 and return directly to us via email by replying to all Recipients herein:" '
    '"1. Shares outstanding by class, showing what each fund holds." '
    '"2. Each outstanding option line by holder, and their total, using each effective date as Carta shows it, regardless of when recorded." '
    '"3. Shares outstanding plus those options, as one figure." "4. Any financing or other significant event since that date." "We appreciate your response by 2/27/2026." '
    'Leonard, 9:12 AM PT (17:12 UTC): "Thanks, got it. I\'ll get this to you before the 27th." '
    'KPMG, 9:37 AM PT (17:37 UTC), same recipients: "For item 2, a line terminated on or before the as-of date counts only what had vested by its termination date." '
    '"For item 4, we need any new financing and whether the company is winding down."')

notices = "; ".join(f"{r[3]} {r[5]}: granted {n(r[6])}, vested {n(r[7])}, terminated as of {r[8]}, last day to exercise {r[9]}" for r in D.OPTION)
OE_CARTA = add(f'Read Carta\'s termination notices in Gmail (search "has been terminated", after "Carta terminations are done" in OE {OE_WIND}; 14 threads, one per option line)',
    f'14 notices from Carta to Leonard, each with "Exercised 0": {notices}. The ES-3 notice dates from Wed Oct 29 2025. Each holder name matches an issue title in OE {OE_ISSUES}, '
    'except ES-15, whose name is tied to ENG-2460 in the next step.')

OE_ES15 = add(f'Tie the ES-15 name to ENG-2460 in Gmail (search the address on ENG-2460, from OE {OE_ISSUES})',
    'Leonard\'s option list of Fri Oct 18 2024 (23:32 UTC) has "Full Legal Name: [PERSON_NAME_2769] [PERSON_NAME_0093]" with "Email: PERSON_4243_EMAIL", the address on ENG-2460 (Brian Foster). So ES-15 is the ENG-2460 line.')

OE_CALVIN = add(f'Read Calvin Price\'s forward in Gmail (search the mailbox for the address on ENG-2452, from OE {OE_ISSUES})',
    'Calvin Price to Leonard, Tue Feb 3 2026 8:20 AM PT (16:20 UTC), subject "Fwd: Your option grant at [SOURCE_ORG_0001] Games Inc. has been updated": '
    '"Thanks for sorting out the extra weeks I asked for." and the forwarded Carta update dated Jan 23, 2026: '
    '"ID ES-3" "Vested 4,408" "Last day to exercise Feb. 20, 2026 (previously Jan. 24, 2026)". This is later than the ES-3 notice in OE '
    f'{OE_CARTA}, so ES-3\'s last day is Feb. 20, 2026 and the line is live.')

OE_LETTERS = add(f'Search Gmail and Leonard\'s Slack DMs for what the founders sent the nine holders of live noticed lines since Feb 1 2026 (each address from OE {OE_ISSUES}; live lines from OE {OE_CARTA} and OE {OE_CALVIN}; the issue comments in OE {OE_COMMENTS} count the last mail before Feb)',
    'Six letters from Leonard, Wed Feb 11 2026, cc Robert and Arthur Blake, each saying "The company is shutting down": 12:10 PM PT (20:10 UTC) to PERSON_2360_EMAIL (Claire Morgan, ES-4); '
    '12:13 PM PT to PERSON_3140_EMAIL (ES-12); 12:15 PM PT to PERSON_4363_EMAIL (ES-13); 12:16 PM PT to marcus.bennett@harmonygames.co (ES-7); '
    '12:17 PM PT to PERSON_4243_EMAIL (ES-15); 12:18 PM PT to PERSON_2361_EMAIL (ES-1). Each says "If you have any equity, options, or other grants, you should receive a" separate email and "exercising is not recommended because the shares are expected to have no value", and none gives a last day. '
    'No message since Feb 1 2026 from a founder to [EMAIL_0801] (ES-3), PERSON_2684_EMAIL (ES-14) or PERSON_1174_EMAIL (ES-18). '
    'Among Leonard\'s Slack DMs with the ES-3, ES-12, ES-14 and ES-18 holders, only the ES-12 holder\'s has messages in February 2026: "I have some announcements to make", and it does not say the company is closing.')

OE_BOUNCE = add(f'Read the thread of the letter to PERSON_3140_EMAIL in Gmail (the ES-12 letter from OE {OE_LETTERS})',
    f'A second message in that thread, Wed Feb 11 2026 12:13 PM PT (20:13 UTC), subject "Delivery Status Notification (Failure)": '
    f'"Your message wasn\'t delivered to PERSON_3140_EMAIL because the address couldn\'t be found, or is unable to receive mail." So the ES-12 letter was not delivered and, with OE {OE_LETTERS}, the ES-12 holder has not been told. No delivery failure for the other five letters is in the mailbox.')

OE_CLAIRE = add(f'Find any question a holder asked about their holding that nobody answered: search Leonard\'s Gmail for mail from each of the 26 issue addresses (OE {OE_ISSUES}) about options, shares, equity, vesting or exercise, and search Leonard\'s Slack DMs and group DMs for the same words, with no date limit',
    'One unanswered question for a holder who gets a note. In group DM C51ECE5102ED, Claire Morgan, Thu Feb 12 2026 5:41 AM PT (13:41 UTC), ts 1770903714.600249: "Bir de equity lerimiz için birşey yapmamız gerekiyor mu prosedür olarak?" '
    '(whether they need to do anything about their equity). Leonard\'s reply at 6:26 AM PT (14:26 UTC), "öyle yazıldı.", answers the other question, about deleting work, and no message in the DM answers this one. '
    'The ENG-2461 holder\'s Gmail reply of Wed Oct 29 2025, that Carta "says I cannot exercise online", was answered by Leonard on Oct 30 ("Ok, let me know how Carta exploration goes."), and that line holds nothing today, so it needs no note.')

OE_GRANTS = add(f'Find the option grants the notices skip in Gmail (search "ES-8", "ES-9", "ES-10" and "ES-11", the numbers missing from the 14 notices in OE {OE_CARTA})',
    'Carta activity digests to Leonard. Sat Nov 18 2023 (10:37 UTC): "ES-9" "for Husnu" "Matthew Collins" and "option grant ES-11" "for PERSON_3941_NAME". '
    'Tue Nov 21 2023 (10:36 UTC), subject "Carta activity for Nov. 20, 2023": "[PERSON_NAME_0089] [PERSON_NAME_25152]" "accepted  option grant ES-8" and "PERSON_1287_NAME" "accepted  option grant ES-10".')

OE_DM = add(f'Find and read the Slack DM with the ENG-2440 holder (search Slack for the address on ENG-2440, from OE {OE_ISSUES}; both hits are in one DM)',
    'DM D04UC0UEN2V. The other person gives PERSON_3336_EMAIL there twice (Wed Sep 13 2023 PT, Sep 14 UTC, and Wed Jan 24 2024). Leonard, Aug 28 2023: "Here is the advisor contract draft", file "Harmony Games Advisor Agreement - Segerstråle", and '
    '"pre-money percent is as promised 0.5% (30518 shares / 103764 shares for advisors + 6 million shares for cofounders = 0.5%)." '
    'Leonard, Mon Feb 9 2026 11:23 AM PT (19:23 UTC), ts 1770664988.379119: "Metrics didn’t improve. The most reasonable thing to do right now is to shut down the company we decided." '
    'The other person, 12:43 PM PT (20:43 UTC): "Heyo sorry to hear". So the ENG-2440 holder has been told, and ES-8 is the 30,518 grant.')

OE_ADVISOR = add(f'Find the size of each of the four grants in Gmail (search "103,764", the advisor total in OE {OE_DM})',
    'A thread in Leonard\'s mailbox, Thu Aug 10 2023 (18:33 UTC), quoting the disclosure schedule ("From the disclosure schedule."): [PERSON_NAME_0090], Advisor, 0.5%, "30,518 shares"; Matthew Collins, Board member, 1%, "61,038 shares"; '
    'PERSON_1287_NAME, Advisor, 0.1%, "6,104 shares"; PERSON_3941_NAME [PERSON_NAME_0127], Advisor, 0.1%, "6,104 shares"; total "103,764 shares". '
    f'So ES-9 (Husnu Matthew Collins) is 61,038, ES-10 (PERSON_1287_NAME) is 6,104, ES-11 (PERSON_3941_NAME) is 6,104, and ES-8 is the 30,518 that OE {OE_DM} ties to ENG-2440.')

OE_VEST = add('Work out how the four grants vest. Open the board consent attached to michelle\'s Fri Nov 10 2023 message in Leonard\'s "RE: [SOURCE_ORG_0001]- Option Issuances" thread in Gmail ("please see execution copy of Board Consent") and read its Exhibit A; check Contacts for the address on ENG-2447.',
    'The consent is dated November 10, 2023. Exhibit A lists 30,518, 61,038, 6,104 and 6,104 (ES-8, ES-9, ES-10 and ES-11 by size, OE ' + str(OE_DM) + ' and OE ' + str(OE_ADVISOR) + '), each "1/24th monthly/no cliff", under "See Specific Vesting Start Dates in Carta". '
    'Contacts, matthew.collins@harmonygames.co: "Investor and advisor (left the board May 2025)", so the ES-9 holder stayed in service, and none of the four has a termination notice (OE ' + str(OE_CARTA) + '). '
    'Counted from the Nov 2023 grants (OE ' + str(OE_GRANTS) + '), the 24 monthly steps end by Nov 2025, so all four are fully vested at Dec 31, 2025 and at the clock: 103,764 options.')

OE_LEDGER = add('Find the share ledger figures in Docs (search "ledger"; the doc "Reset Financing Term Sheet (Washout Recap + Pay-to")',
    'Created Thu Jan 22 2026 3:43 PM PT (23:43 UTC). "Inputs from ledger (pre-recap)" "Founder common: 6,000,000" "Series Seed Preferred (all non-founder investors): 3,051,879". '
    'It also lists "Options outstanding: 268,772", dated before the Carta entries of Feb 12, so that figure is out of date.')

OE_RECAP = add(f'Check whether the reset in OE {OE_LEDGER} closed, in Gmail (search "recap", a word in that doc\'s title; then Leonard\'s wind-down support request, search "out of funds")',
    'Leonard to Griffin\'s partner, Fri Jan 23 2026 11:29 AM PT (19:29 UTC), subject "[SOURCE_ORG_0001]: recap option, cap table reset, and next steps": "we see only two realistic paths". '
    'Leonard, Mon Feb 9 2026 2:44 PM PT (22:44 UTC), subject "[SOURCE_ORG_0001] wind-down support request": "We have preferred stock from a seed round (no SAFEs)." and "We are out of funds". So the reset did not close, and no new financing came in after December 31, 2025.')

OE_SPLIT = add('Find how Griffin\'s two funds split their shares in Gmail (search "Series Seed Preferred Shares", the class named in OE ' + str(OE_LEDGER) + ')',
    'Mail of Thu Jul 20 2023 (16:51 UTC) quoting the purchaser schedule: "2,662,255" for [ORGANIZATION_NAME_0151] II, L.P. and "84,438" for "GRIFFIN GAMING PARTNERS II Side Fund, L.P.". '
    'Together 2,746,693, the merged figure on the owner-list comments of ENG-2438 and ENG-2439.')

OE_BOARD = add(f'Read the Board position thread in Gmail (search "Board position", the name in the notes, OE {OE_NOTES})',
    'Thread leonard.hayes@harmonygames.co/1856958794180374704, subject "Board position". PERSON_4337_NAME (Griffin\'s partner) to Leonard, cc PERSON_2847_EMAIL, Thu Feb 12 2026 2:05 PM PT (22:05 UTC), '
    'message <BYAPR02MB435880CCF501BE0AE906AFFDC460A@BYAPR02MB4358.namprd02.prod.outlook.com>: "Hi Leonard, I would formally like to leave the Board of [SOURCE_ORG_0001]." '
    'Leonard, 2:14 PM PT (22:14 UTC), to the partner, cc PERSON_2847_EMAIL, robert@harmonygames.co and arthur.blake@harmonygames.co: "Understood and thank you." and "We signed up with [ORGANIZATION_2601] Inc. to properly wind down the operations as well." '
    'Robert, 2:38 PM PT (22:38 UTC): "That leaves Leonard and me on the board to see the close through."')

OE_CHARTER = add('Find who votes on a dissolution in Docs (search "dissolve"; the doc "Harmony Games Inc. - Amended and Restated Cert")',
    'The protective provisions need the consent of "the holders of a majority of the outstanding shares of Preferred Stock" to "liquidate, dissolve or wind-up the business and affairs of the Corporation".')

OE_GTOLD = add(f'Search Gmail for what the founders sent Griffin\'s partner since Feb 1 2026 (the address on ENG-2438 and ENG-2439, from OE {OE_ISSUES})',
    'Leonard to PERSON_4337_EMAIL, Mon Feb 9 2026 11:12 AM PT (19:12 UTC), in the thread "Combo Fighter Data and [SOURCE_ORG_0001] Shut-Down": "decided to shut the company down". '
    'The partner answers in that thread on Wed Feb 11 2026: "They are in a wind down process and they are interested in speaking with you." So Griffin\'s partner has been told, for both funds.')

OE_ROBERT = add(f'Search Gmail for what the founders sent the ENG-2446 holder since Feb 1 2026 (the address on ENG-2446, from OE {OE_ISSUES})',
    'Robert to "PERSON_3941_NAME <PERSON_3941_EMAIL>", cc Leonard, Thu Feb 12 2026 3:41 PM PT (23:41 UTC), subject "Re: Funds Transfer Request #450904566 Has Been Scheduled": '
    '"Wanted you to hear this from me: we\'re closing the company." So the ENG-2446 holder has been told.')

OE_AKIN = add('Search Leonard\'s sent Gmail since Feb 1 2026 for the closing (search "shutting down")',
    f'Among the hits, apart from the six letters in OE {OE_LETTERS}: Leonard to "Husnu Akin <PERSON_8862_EMAIL>", Thu Feb 12 2026 2:52 PM PT (22:52 UTC), subject "Harmony": '
    '"Harmony is shutting down: we let the team know yesterday, and Robert and I are handling the wind-down from here." "Thank you for everything, on the board and since."')

OE_AKIN2 = add('Tie Akin to the ENG-2447 holder in Gmail (search "and Akin")',
    'A mail in Leonard\'s mailbox from Matthew Collins <matthew.collins@harmonygames.co> (the address on ENG-2447), Sat Sep 9 2023, is signed "best akin" and replies to a note that opens "Hi PERSON_4337_NAME and Akin,". '
    f'ENG-2447 is titled "Husnu Matthew Collins". So the Feb 12 mail in OE {OE_AKIN} told the ENG-2447 holder, and no delivery failure came back for it.')

OE_FAM = add(f'Find who handles the family lines in Gmail (search the address on ENG-2445, from OE {OE_ISSUES})',
    'A mail in Leonard\'s mailbox from PERSON_2260_NAME (the address on ENG-2443), Fri Jun 30 2023, lists all three investors with their addresses: "Patrick Lewis" "patrick@harmonygames.co", "[PERSON_NAME_52949]" "PERSON_2260_EMAIL" and "[PERSON_NAME_27652]" "PERSON_2275_EMAIL". '
    'In the wire thread, "we(me and my brothers)" and "We are confirming we received the wire transfer for all three Disli brothers!". So [PERSON_NAME_52949] handles it for the family, and ENG-2444 and ENG-2445 are Covered '
    f'under the rule in OE {OE_THREAD}.')

OE_TOR = add('Read Leonard\'s Slack DM with TOR Capital\'s partner (search Slack for "months of runway")',
    'DM D09R59580EM, Tue Nov 4 2025 11:51 AM PT (19:51 UTC), Leonard: "Short story is we are running very low on cash and seed extension type of VC deals are hard to come by without strong metrics." '
    '"Currently, we have about ~3 months of runway, assuming no deals gets done." The DM says the company is short of cash and does not say it is closing, so TOR Capital has not been told.')

OE_ABS = add(f'Search Gmail and Slack for any closing message to the other angels (the addresses on ENG-2441, ENG-2442, ENG-2443, ENG-2444, ENG-2445, ENG-2448 and ENG-2449, from OE {OE_ISSUES}, since Feb 1 2026)',
    'None. No message in Leonard\'s mailbox dated in February 2026 has any of these addresses in to, cc or bcc, and none of Leonard\'s Slack DMs with messages in February 2026 is with these holders. '
    f'The Feb 12 list in OE {OE_WIND} also shows the angels as still open.')

# ---------------------------------------------------------------- decision steps
stock_rows = "; ".join(f"{k} {D.holds_text(k)}" for k in D.ISSUES[:12])
OE_CALC1 = add(f'Work out what each stock line holds (no tool; owner-list figures from OE {OE_COMMENTS}, grants from OE {OE_GRANTS}, OE {OE_ADVISOR} and OE {OE_VEST}, split from OE {OE_SPLIT})',
    f'An owner-list figure that merges one of the four grants is the shares less the grant: 81,383 less 30,518 is 50,865; 31,536 less 6,104 is 25,432; 86,470 less 61,038 is 25,432. {stock_rows}. '
    f'The 12 lines add up to {n(T["SUMMARY"]["Series Seed total"])} Series Seed shares, the ledger total in OE {OE_LEDGER}. With founder common of 6,000,000, shares outstanding are 9,051,879.')

live = [r for r in D.OPTION if T[r[0]]["Options now"]]
opt_rows = "; ".join(f"{r[3]} {D.TITLE[r[0]]}: {n(T[r[0]]['Options now'])} vested, last day {D.LAST[r[0]]}" for r in live)
OE_CALC2 = add(f'Work out which option lines are live at the clock, Feb 14 2026 00:00 UTC (no tool; OE {OE_CARTA}, OE {OE_CALVIN} and OE {OE_VEST}; rule from OE {OE_NOTES})',
    f'Nine of the 14 lines with a Carta notice are live: {opt_rows}. Five lines whose last day has passed hold nothing: ES-2 (Nov. 1, 2024), ES-5 (Jan. 24, 2026), ES-6 (July 16, 2025), ES-16 (Jan. 24, 2026), ES-17 (Jan. 28, 2026). '
    f'Options outstanding today: 60,350 vested on the live lines plus the 103,764 of the four grants ES-8 to ES-11, fully vested per OE {OE_VEST} and with no termination notice, {n(T["SUMMARY"]["Options outstanding now"])}.')

lab = lambda name: ", ".join(k for k in D.ISSUES if D.label(k) == name)
OE_CALC3 = add(f'Work out each line\'s label, whether it gets a note, and its Linear state (no tool; rules from OE {OE_PROJECT}, OE {OE_NOTES} and OE {OE_THREAD}; told from OE {OE_LETTERS} to OE {OE_ABS})',
    f'Nothing, state Canceled, no note: {lab("Nothing")}. Already told, state Done, no note: {lab("Already told")}. Covered, state Done, no note: {lab("Covered")}. '
    f'Closing, state Todo, a note: {lab("Closing")}. Last day, state Todo, a note: {lab("Last day")}. Closing and last day, state Todo, a note: {lab("Closing and last day")}. '
    'Counts by rows: Nothing 5, Already told 5, Covered 2, Closing 5, Last day 5, Closing and last day 4. 14 notes, 12 issues with no note of their own.')

OE_CALC4 = add(f'Work out the board, the preferred vote and who goes first (no tool; OE {OE_BOARD}, OE {OE_CHARTER}, OE {OE_SPLIT}, OE {OE_CALC2} and OE {OE_CALC3})',
    'Directors in office: Leonard Hayes and Robert. Preferred vote: Griffin, whose two funds hold 2,746,693 of the 3,051,879 Series Seed shares (90.0%). '
    'Who goes first: Calvin Price (ES-3, last day Feb. 20, 2026), then [PERSON_NAME_0051] (ES-14, last day Feb. 21, 2026).')

kp = "; ".join(f"{c} {t} {n(v)}" for c, t, v in D.dec31_lines())
OE_CALC5 = add(f'Work out KPMG\'s figures as of December 31, 2025 (no tool; rules from OE {OE_KPMG}, effective dates from OE {OE_CARTA}, grants from OE {OE_ADVISOR})',
    'A line terminated on or before Dec 31, 2025 counts what had vested; a line terminated later (Jan. 30, 2026) counts its full grant; ES-2 and ES-6 had lapsed before Dec 31, 2025 and are left out; the four grants ES-8 to ES-11, fully vested, count in full. '
    f'Sixteen lines: {kp}. Total 243,757. Shares outstanding plus those options: 9,051,879 plus 243,757 is 9,295,636.')

# ---------------------------------------------------------------- the sheet
sheet = []
for k in D.ISSUES:
    bit = f"{k} {D.TITLE[k]}: {D.holds_text(k)}"
    if k in D.LAST and T[k]["Options now"]:
        bit += f", last day {D.LAST[k]}"
    sheet.append(bit + f", {D.label(k)}")
OE_SHEET = add(f'Write the holder sheet into "Holder list (draft)" in Sheets (the file from OE {OE_FOLDER}, over its old rows, as the notes in OE {OE_NOTES} ask; figures from OE {OE_CALC1} to OE {OE_CALC4})',
    'The sheet has one row per issue, 26 rows, with holder, what the holder holds today, any last day and the label: ' + "; ".join(sheet) + '. '
    'It also shows the totals: common 6,000,000 (the three founders appear only here), Series Seed 3,051,879, shares 9,051,879, options outstanding today 164,114; the counts by label (Nothing 5, Already told 5, Covered 2, Closing 5, Last day 5, Closing and last day 4); '
    'directors in office Leonard Hayes and Robert; and the preferred vote held by Griffin. The old figures copied from the Nov 2024 list are gone.')
OE_SHARE1 = add(f'Share the holder sheet with Robert in Drive (address from OE {OE_BOARD}; rule from OE {OE_NOTES})', 'robert@harmonygames.co can open the sheet.')
OE_SHARE2 = add(f'Share the holder sheet with Arthur Blake in Drive (address from OE {OE_BOARD}; rule from OE {OE_THREAD})', 'arthur.blake@harmonygames.co can open the sheet.')

# ---------------------------------------------------------------- drafts
for k in D.ISSUES:
    lb = D.label(k)
    if lb in ("Nothing", "Already told", "Covered"):
        continue
    parts = []
    if "Closing" in lb:
        parts.append("says the company is closing")
    if k == "ENG-2443":
        parts.append("says what each of the three family lines holds: [PERSON_NAME_52949] 25,432, Patrick Lewis 25,432 and [PERSON_NAME_27652] 25,432 Series Seed shares")
    else:
        parts.append(f"says the holder holds {D.holds_text(k)}")
    if "ast day" in lb:
        parts.append(f"gives the last day to exercise, {D.LAST[k]}")
    if k == "ENG-2453":
        parts.append(f"answers the equity question from OE {OE_CLAIRE} (what, if anything, has to be done about the options before that date)")
    add(f'Save the note for {k} {D.TITLE[k]} as a draft in Gmail (address from OE {OE_ISSUES}; left unsent)',
        f'A Gmail draft to {D.EMAIL[k]}, not sent, that ' + ", ".join(parts[:-1]) + (" and " if len(parts) > 1 else "") + parts[-1] + '.')

# ---------------------------------------------------------------- the letter
OE_DOC = add(f'Write the investor letter as a new Doc in Google Docs (from the draft in OE {OE_WIND} and the outline in OE {OE_OUTLINE})',
    f'A new Google Doc with the letter to the investors, worked up from the Feb 9 draft and following the outline\'s five slides, with each stale line of the draft brought up to date. The runway line ("Given our current runway of less than a month") now says the company is insolvent ("the company is insolvent and we have no cash reserves left"). '
    f'The line "We are initiating an orderly wind-down process and preparing the required board resolutions and documentation." now says the wind-down is under way, with the wind-down agreement signed on Feb 12 ("wind down agreement and data agreement reviewed and signed with [USERNAME_26907]") and Griffin\'s vote on the dissolution still to come (OE {OE_NOTES}). '
    'The IP line ("We will also evaluate what to do with the remaining IP and codebase (archive, sale, or other disposition)") now says the data agreement signed that day is a license rather than a sale, so ownership of the IP stays with the company ("we can own the entire IP"), and that Domino Delights and Zombie Match are to move off Helpshift before Feb 28. '
    f'The priorities line ("Our priorities are to handle employee and contractor obligations properly") now says the termination letters went out on Feb 11, the Carta terminations were done on Feb 12 and vendors are being closed out, with Helpshift cancelling and Unity being terminated (OE {OE_WIND}). '
    f'The slide on distributions, tax papers and options reflects the insolvency and the Feb 11 letters\' advice that "exercising is not recommended because the shares are expected to have no value" (OE {OE_LETTERS}), and says tax papers are still to come from the wind-down. '
    f'The board is Leonard and Robert after Griffin\'s partner left on Feb 12 (OE {OE_BOARD}), with Sunset engaged for the dissolution under the Feb 12 agreement (OE {OE_NOTES}, OE {OE_WIND} and OE {OE_BOARD}), and the holders are those on the new sheet (OE {OE_SHEET}), not the Nov 2024 owner list.')
OE_MOVE = add(f'Move the letter into the close-out folder in Drive (folder from OE {OE_FOLDER}; the Doc from OE {OE_DOC})', 'The letter is in "Stockholder close-out" (d_601064334a0b493022fe83).')
OE_SHARE3 = add(f'Share the letter with Robert in Drive (address from OE {OE_BOARD}; rule from OE {OE_NOTES})', 'robert@harmonygames.co can open the letter.')

# ---------------------------------------------------------------- Linear
for k in D.ISSUES:
    st = T[k]["State"]
    add(f'Move {k} to {st} in Linear (state from OE {OE_CALC3})', f'{k} state {st}.')
    if k in D.WHY:
        add(f'Comment on {k} in Linear saying why it has no note of its own (rule from OE {OE_PROJECT})', f'A comment on {k} giving the reason: {D.WHY[k]}.')

# ---------------------------------------------------------------- sends
OE_KSEND = add(f'Send the confirmation to KPMG in Gmail as a reply to all: a message in the thread from OE {OE_KPMG}, with the To and Cc addresses set explicitly to everyone on KPMG\'s last message (after the sheet, OE {OE_SHEET}; figures from OE {OE_CALC1} and OE {OE_CALC5}; item 4 from OE {OE_RECAP})',
    'A sent reply in that thread to PERSON_3088_EMAIL, with PERSON_4416_EMAIL, PERSON_2322_EMAIL and PERSON_2847_EMAIL on copy, as of December 31, 2025. '
    '1. Common 6,000,000; Series Seed 3,051,879, of which GRIFFIN GAMING PARTNERS II, L.P. 2,662,255 and GRIFFIN GAMING PARTNERS II SIDE FUND, L.P. 84,438. '
    f'2. The sixteen option lines by holder ({kp}), total 243,757. 3. 9,295,636. 4. No new financing since that date, and the company is winding down.')
OE_GSEND = add(f'Send the heads-up to Griffin\'s partner in Gmail, as a reply to all on the partner\'s own Board position mail from OE {OE_BOARD} (after the sheet, OE {OE_SHEET})',
    'A sent reply on message <BYAPR02MB435880CCF501BE0AE906AFFDC460A@BYAPR02MB4358.namprd02.prod.outlook.com> to PERSON_4337_EMAIL, with PERSON_2847_EMAIL on copy, asking for Griffin\'s vote as preferred holders on the dissolution.')
OE_SSEND = add(f'Reply under Leonard\'s list in #winddown in Slack (thread of ts 1770934638.035469 from OE {OE_WIND}; after the sheet, OE {OE_SHEET})',
    'A reply in that thread saying the sheet is ready and that Calvin Price goes first, with a last day of Feb. 20, 2026.')


# ---------------------------------------------------------------- render + lint
def render():
    out = []
    for i, (t, e) in enumerate(EV, 1):
        e = e.replace("{DM}", str(OE_DM))
        out.append(f"OE {i}  {t}\nExpected: {e}\n")
    return "\n".join(out)


DERIVED = {"9,051,879", "164,114", "243,757", "9,295,636", "60,350", "90.0"}


def corpus():
    parts = [L.norm(L.SQL.replace("''", "'"))]
    parts += [str(v) for k, v in L._cache.items() if not k.startswith("cansee|")]
    parts += json.load(open(os.path.join(L.HERE, "verified_corpus.json")))
    parts.append(open(os.path.join(L.HERE, "consent_nov10_2023_exhibit_a.txt"), encoding="utf-8").read())
    return L.squash(" \n ".join(parts))


def lint(text):
    bad = []
    if "—" in text or "–" in text:
        bad.append("dash character present")
    C = corpus()
    CD = re.sub(r"[,\s]", "", C)
    for line in text.splitlines():
        if not line.startswith("Expected:"):
            continue
        for q in re.findall(r'"([^"]+)"', line):
            if L.squash(q) not in C:
                bad.append(f"quote not in records: {q[:110]}")
        for num in re.findall(r"\d{1,3}(?:,\d{3})+", line):
            if num not in DERIVED and num not in C and num.replace(",", "") not in CD:
                bad.append(f"figure not in records: {num}")
    return bad


if __name__ == "__main__":
    text = render()
    bad = lint(text)
    for b in bad[:60]:
        print("LINT", b)
    open(os.path.join(L.TI, "08_Oracle_Events.md"), "w").write(text)
    json.dump({"OE_NUM": {k: v for k, v in globals().items() if k.startswith("OE_") and isinstance(v, int)}}, open(os.path.join(L.HERE, "event_numbers.json"), "w"), indent=0)
    print("events", len(EV), "chars", len(text), "lint", len(bad))
