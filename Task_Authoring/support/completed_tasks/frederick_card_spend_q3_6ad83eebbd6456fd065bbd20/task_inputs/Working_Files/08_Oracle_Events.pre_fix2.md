OE 1  Find Leonard's request email in Frederick's Gmail and open its thread (search: subject "Card spend breakdown for Q3 Standard Metrics", from Leonard Hayes, Sep 29 2025)
        Expected: One message from Leonard Hayes, sent Mon Sep 29 2025 3:47 PM PT (22:47 UTC), to Frederick, cc Arthur Blake. It asks Frederick to: break the ledger line "Unreconciled operating expenses" down for January to September by vendor and by Griffin's categories, month by month, from the card feed folder, and tie each month to the ledger; give the Q4 monthly run-rate by vendor and anything cancelled but still charged; follow the card close notes tab in the QuickBooks close workbook; use Griffin's categories from the forwarded note; update the cut-list card on his Trello board, not a new card; put anything of Arthur's still being charged on Arthur's seat cleanup ticket; save the workbook in the Q3 2025 investor reporting folder; reply on this thread with the totals by category, the monthly run-rate and the disputed charges. It ends with "I'll tell you who else needs the reply."

OE 2  Read Griffin's category list in the note Leonard forwarded, in Frederick's Gmail (subject "Fwd: Q2 metrics - opex categories", sent Sep 29 2025 3:41 PM PT)
        Expected: Eight 2025 categories for non-payroll opex: Software & subscriptions; Hosting & infrastructure; Research & user testing; Marketing (non-UA); Travel & events; Hardware & equipment; Professional & admin (includes registered agent, filings, payroll/HR, equity and accounting platforms); Other G&A (bank fees not tied to a purchase, shipping, coworking, team meals). Paid user acquisition is reported separately, not in opex. "These replace the 2024 list."

OE 3  Read the booking rules in Drive/Sheets (spreadsheet "QuickBooks close 2025", tab "Card close notes", all rows)
        Expected: 12 rules. 1: cards 0417 (Leonard) and 2208 (Arthur, closed Jul 31). 2: the line holds rows no bank rule matches and ties to FINANCE.EXPENSES.FINANCE_LEDGER; payments are not spend. 3: posted-date statement cycles; 25th close through May (January = Dec 26 to Jan 25); June cycle May 26 to Jun 25; July cycle Jun 26 to Jul 28; then the 29th to the 28th. 4: no June ledger line, July carries both cycles. 5: a refund reduces the cycle it posts in. 6: only Jan to Sep 2025 cycles. 7: an ad-network charge is a reclass in the tie-out, not a category. 8: status lives on the Trello list "Subscriptions (card)"; a cancellation or downgrade counts once confirmed; a charge after a confirmed cancellation is disputed unless the feed shows it refunded; an annual plan is charged until it lapses. 9: run-rate covers only Unreconciled-line vendors (Bank rules vendors out), plans only; monthly plans at the latest-cycle purchase amount, annual plans at 1/12 of the last annual charge, registered-agent (COGENCY GLOBAL INC) renewals are annual plans, confirmed cancellation 0, confirmed downgrade at the new price, fee rows count with the plan. 11: tabs By vendor, Category by month, Ledger tie-out, Q4 run-rate; USD to the cent; months YYYY-MM. 12: one vendor per brand; Apple Developer Program separate from Apple Store; Unity seats separate from Unity Ads.

OE 4  Read the vendors booked outside the line (same spreadsheet, tab "Bank rules")
        Expected: Seven patterns: AMAZON WEB SERVICES, GOOGLE *GSUITE, SLACK T, LINEAR, GITHUB, FIGMA, ATLASSIAN.

OE 5  Read how the feed works in Drive/Docs (Doc "SVB card feed - how it works" in folder "SVB card feed 2025")
        Expected: Columns posted_date, txn_date, card, cardholder, descriptor, amount_usd, original_amount, original_currency, type. Refunds are negative; payment rows are the autopay, not spend. A FOREIGN TRANSACTION FEE row is a 3% fee on the charge directly above it and counts with that vendor. Late reversals and credits sit on a second tab named "adjustments". Card 2208 closed Jul 31 and Arthur's subscriptions bill to 0417 from August.

OE 6  List the feed sheets in Drive (folder "SVB card feed 2025", follow page tokens to the end)
        Expected: 496 daily sheets named card_0417_YYYY-MM-DD and card_2208_YYYY-MM-DD, Dec 26 2024 to Sep 29 2025, plus the feed Doc.

OE 7  Read every feed sheet from OE 6 in Sheets (tab Sheet1 on all 496, plus the "adjustments" tab on the 7 sheets that have one)
        Expected: 653 rows: 343 purchase, 12 fee, 7 refund, 15 payment, 276 "no postings". Includes UNITY ADS 1,000.00 (Aug 20); COGENCY GLOBAL INC 300.00 (May 16); MIDJOURNEY INC. 60.00 (Aug 2), -60.00 on the Aug 25 adjustments tab, and 60.00 (Sep 2); LOOM 75.00 (Jul 9), -75.00 on the Jul 15 adjustments tab; SENSOR TOWER -106.67 (Sep 8 adjustments) and 250.00 (Sep 24); UNITY TECHNOLOGIES 10,200.00 (Aug 8); HEROIC LABS 600.00 (Sep 10).

OE 8  Total the unmatched card spend per statement cycle (rows from OE 7; posted-date cycles from OE 3; drop the seven Bank rules patterns from OE 4 and payments; keep fees and refunds)
        Expected: 2025-01 7,759.99; 2025-02 8,914.76; 2025-03 12,214.05; 2025-04 6,268.22; 2025-05 5,928.41; 2025-06 12,222.02; 2025-07 12,132.35; 2025-08 22,090.21; 2025-09 10,438.20; Jan to Sep 97,968.21 (trap: the Sep 29 rows, United 312.40 and DoorDash 96.18, belong to the October cycle and are left out).

OE 9  Read the ledger lines in Snowflake (FINANCE.EXPENSES.FINANCE_LEDGER, COUNTERPARTY = "Unreconciled operating expenses", DATE Jan 1 to Sep 30 2025)
        Expected: Eight rows, amounts negative: 2025-01-31 7,759.99; 2025-02-28 8,914.76; 2025-03-31 12,214.05; 2025-04-30 6,268.22; 2025-05-31 5,928.41; no June row; 2025-07-31 24,354.37; 2025-08-31 22,090.21; 2025-09-30 10,438.20.

OE 10  Tie each cycle to the ledger (OE 8 cycle totals against OE 9 ledger lines, rules 4 and 7 from OE 3)
        Expected: Jan to May, Aug and Sep match one to one. June cycle 12,222.02 + July cycle 12,132.35 = July line 24,354.37. August includes UNITY ADS 1,000.00, shown as a reclass to paid UA, so categorized August opex is 21,090.21. Categorized Jan to Sep opex 96,968.21 + 1,000.00 reclass = 97,968.21.

OE 11  Total the spend by vendor for Jan to Sep (rows from OE 8; brands merged per rule 12; fee rows with their vendor)
        Expected: 43 vendors: Unity Technologies 17,970.00; United Airlines 12,971.12; Apple Store 11,866.87; Marriott 8,624.71; Best Buy 7,337.00; Heroic Labs 5,400.00; Google Cloud 3,587.96; DoorDash 3,022.87; Carta 2,760.00; WeWork 2,691.00; PlaytestCloud 2,086.46; Informa (GDC) 1,999.00; Uber 1,447.80; Gusto 1,326.00; AppMagic 1,293.46; Deel 1,127.00; OpenAI ChatGPT 1,050.00; Sensor Tower 1,043.33; Fiverr 1,020.00; Unity Ads 1,000.00 (reclass); LinkedIn Sales Navigator 899.91; QuickBooks Online 810.00; FedEx 761.90; USPTO 700.00; Zapier 661.50; Midjourney 480.00; Loom 450.00; DE Div of Corporations 450.00; DocuSign 405.00; Notion 360.00; 1Password 359.55; Envato Elements 324.42; Canva 315.00; Cogency Global 300.00; Webflow 261.00; Mailchimp 180.00; Calendly 144.00; Backtrace 118.00; Apple Developer Program 99.00; Namecheap 86.40; Zoom 79.95; Supernormal 54.00; ElevenLabs 44.00.

OE 12  Total by Griffin category and month (vendors from OE 11 mapped to the categories from OE 2; months 2025-01 to 2025-09)
        Expected: Software & subscriptions 1,792.43 / 2,265.92 / 1,888.56 / 1,936.04 / 1,982.27 / 1,978.38 / 2,346.85 / 11,307.91 / 832.76 = 26,331.12; Travel & events 1,191.91 / 3,972.15 / 2,979.42 / 600.95 / 0 / 3,265.46 / 2,819.87 / 4,241.59 / 5,971.28 = 25,042.63; Hardware & equipment 2,824.05 / 710.85 / 1,522.08 / 1,224.90 / 1,651.95 / 4,974.24 / 3,506.75 / 2,400.22 / 388.83 = 19,203.87; Hosting & infrastructure 1,017.12 / 1,031.57 / 1,044.90 / 1,146.46 / 1,006.48 / 943.13 / 1,081.71 / 1,038.15 / 1,025.84 = 9,335.36; Professional & admin 342 / 342 / 3,552 / 342 / 679 / 379 / 1,079 / 379 / 379 = 7,473.00; Other G&A 592.48 / 592.27 / 730.47 / 503.69 / 608.71 / 681.81 / 958.17 / 1,043.34 / 764.83 = 6,475.77; Research & user testing 496.62 (Mar), 514.18 (Apr), 1,075.66 (Sep) = 2,086.46; Marketing (non-UA) 340 (Jul), 680 (Aug) = 1,020.00. Opex total 96,968.21.

OE 13  Read subscription status in Trello (board "Harmony Games", list "Subscriptions (card)", every card with its plan, billing and comments)
        Expected: 24 cards. Status comments: ChatGPT Team down to 2 seats from the Sep 26 bill; Midjourney cancelled Jul 3 (conf MJ-77k2); Supernormal cancelled Mar 31; Notion cancelled Sep 25; Loom cancelled Jun 20; Zoom downgraded to Basic Jun 12, no more charges; Unity Pro annual prepay from Aug 8 for 5 seats; Backtrace cancelled Feb 28; Heroic Labs downgraded, details on ENG-2370; AppMagic cancelled Sep 27 by Fred (email); Sensor Tower downgraded Sep 5 by Fred (email). Annual plans: Envato (renews Feb 11), Carta (Mar 3), Namecheap (Apr 17), Apple Developer Program (Jun 6). Every other plan has no change recorded and is still active.

OE 14  Read the cut-list card in Trello (card "Q4 cost cuts - card subscriptions" #481, its "To cut" checklist and comments)
        Expected: Scope "anything billed to the two SVB operating cards"; context Leonard's #executives thread of 9/23. Checklist: Sensor Tower - cancel (Fred) incomplete; Notion - cancel (Leonard) complete; ChatGPT - down to 2 seats (Leonard) complete; LinkedIn Sales Navigator - cancel (Fred) incomplete; 1Password - down to 4 seats (Arthur) complete; Unity Pro - down to 4 seats (Arthur, ENG-2370) incomplete; Heroic Labs - downgrade plan (Arthur, ENG-2370) complete; Zoom - close the account (Leonard) incomplete. Arthur's comment of Sep 25: 1Password down to 4 seats at $7.99 each from the Oct bill; Unity Pro on the annual prepay since Aug 8, so the seat drop only happens at the Aug 2026 renewal.

OE 15  Read Leonard's cut-list thread in Slack (channel #executives, thread started Sep 23 2025)
        Expected: Leonard's reply of Sep 26 2025 11:20 AM PT: keep Sensor Tower through the bridge, cancel AppMagic instead (Fred), the rest of the list stands (trap: this supersedes the checklist item "Sensor Tower - cancel (Fred)").

OE 16  Confirm the Sensor Tower downgrade in Frederick's Gmail (subject "Your Sensor Tower plan has been changed", Sep 5 2025)
        Expected: Market Intelligence Pro $450.00/month to Lite $250.00/month, effective Sep 5. The feed bills 250.00 on Sep 24.

OE 17  Confirm the AppMagic cancellation in Frederick's Gmail (subject "Your AppMagic subscription has been cancelled", Sep 27 2025)
        Expected: Cancelled, no further charges, access until Oct 13 2025. Last charge Sep 14: 163.10 plus a 4.89 FX fee.

OE 18  Check whether LinkedIn Sales Navigator was cancelled (Frederick's Gmail search "Sales Navigator"; the #481 checklist item; the LinkedIn card)
        Expected: No LinkedIn cancellation in Frederick's Gmail, only the monthly receipt of Apr 3 2025 ($99.99). The checklist item is still incomplete and the card has no comment. The feed bills 99.99 on Sep 3, so the plan is still billing.

OE 19  Read the Envato annual plan in Frederick's Gmail (subject "Your Envato Elements receipt", Feb 11 2025)
        Expected: Teams, 2 seats, annual, A$499.00, renews Feb 11 2026. The feed posts 314.97 plus a 9.45 FX fee on Feb 11.

OE 20  Read Arthur's seat cleanup ticket in Linear (issue ENG-2370 "Seat cleanup (Unity, 1Password) + Heroic plan" and its comments)
        Expected: Unity Pro, 1Password, Heroic Labs and Google Cloud bill to Leonard's card since August. Sep 3 comment: Unity Pro moved to an annual prepay for 5 seats on Aug 8 (feed 10,200.00 on Aug 8). Sep 24 comment: Heroic Labs downgraded, $420.00/month from the Oct invoice (trap: the feed's Sep 10 charge is still 600.00).

OE 21  Work out the Q4 monthly run-rate by vendor (rule 9 from OE 3; statuses from OE 13 to OE 20; Sep-cycle charges from OE 7)
        Expected: Unity Pro 850.00 (10,200/12); Heroic Labs 420.00; Google Cloud 396.84; WeWork 299.00; Sensor Tower 250.00; Carta 230.00 (2,760/12); Deel 147.00; Gusto 142.00; LinkedIn Sales Navigator 99.99; QuickBooks Online 90.00; Zapier 73.50; ChatGPT 60.00; Canva 45.00; DocuSign 45.00; 1Password 31.96 (4 x 7.99); Webflow 29.00; Envato 27.04 ((314.97+9.45)/12); Cogency Global 25.00 (300/12); ElevenLabs 22.00; Mailchimp 20.00; Calendly 16.00; Apple Developer Program 8.25; Namecheap 7.20; AppMagic, Notion, Midjourney, Zoom, Loom, Supernormal and Backtrace 0. Total 3,334.78 per month (trap: the seven Bank rules vendors, such as AWS 2,325.00, stay out).

OE 22  Find the disputed charges (charges after a confirmed cancellation from OE 13 and OE 17, against the refunds on the adjustments tabs from OE 7)
        Expected: One disputed charge: Midjourney 60.00 posted Sep 2 2025 on card 0417 (trap: Midjourney Aug 2 was refunded Aug 25 and Loom Jul 9 was refunded Jul 15, so neither is disputed).

OE 23  Find who else gets the reply in Slack (Frederick's DM with Leonard, Sep 30 2025)
        Expected: Leonard, Sep 30 2025 9:05 AM PT: "for the card breakdown reply, add Robert, he needs the Q3 numbers for the investor update. Arthur stays on."

OE 24  Look up Robert's address in Contacts (search "Robert")
        Expected: robert@harmonygames.co.

OE 25  Find the destination folder in Drive (search folder name "Q3 2025 investor reporting")
        Expected: One folder, owned by Leonard, Frederick a writer.

OE 26  Create the workbook in Sheets (new spreadsheet; title free)
        Expected: A new spreadsheet exists.

OE 27  Move the workbook into the destination folder in Drive (file from OE 26; new parent the folder from OE 25)
        Expected: The spreadsheet's parent is the Q3 2025 investor reporting folder.

OE 28  Set up the workbook tabs in Sheets (spreadsheet from OE 26; tab names from rule 11 in OE 3)
        Expected: Tabs By vendor, Category by month, Ledger tie-out, Q4 run-rate.

OE 29  Write the By vendor tab in Sheets (tab By vendor; values from OE 11)
        Expected: The 43 vendors from OE 11, each with its Griffin category, months 2025-01 to 2025-09 and a Jan to Sep total, USD to the cent.

OE 30  Write the Category by month tab in Sheets (tab Category by month; values from OE 12)
        Expected: The eight categories by month from OE 12, months as YYYY-MM, opex total 96,968.21.

OE 31  Write the Ledger tie-out tab in Sheets (tab Ledger tie-out; values from OE 8 to OE 10)
        Expected: Each cycle against its ledger line, June and July both under the July line 24,354.37, UNITY ADS 1,000.00 as the August reclass; every month ties.

OE 32  Write the Q4 run-rate tab in Sheets (tab Q4 run-rate; values from OE 21 and OE 22)
        Expected: The vendor rows and the 3,334.78 total from OE 21, and the disputed Midjourney 60.00 from OE 22.

OE 33  Record the findings on the cut-list card in Trello (card #481 from OE 14; new comment)
        Expected: A new comment on card #481 stating Sensor Tower kept on Lite at $250/month per Leonard's Sep 26 change; AppMagic cancelled Sep 27; LinkedIn Sales Navigator still billing $99.99; the Unity seat drop waiting for the Aug 2026 renewal; the Midjourney $60.00 charge of Sep 2 disputed.

OE 34  Comment on Arthur's seat cleanup ticket in Linear (issue ENG-2370 from OE 20; new comment)
        Expected: A new comment on ENG-2370 naming Arthur's subscriptions still charged on Leonard's card: Unity Pro (annual 10,200.00 from Aug 8, charged until it lapses, 850.00/month); 1Password (4 seats at $7.99 from Oct); Google Cloud (396.84 in Sep); Heroic Labs ($420.00/month from Oct).

OE 35  Send the reply on Leonard's thread in Gmail (send a message with the thread ID from OE 1; to Leonard; Arthur and Robert from OE 23 and OE 24 as recipients)
        Expected: A sent message in the thread "Card spend breakdown for Q3 Standard Metrics" to leonard.hayes@harmonygames.co, arthur.blake@harmonygames.co and robert@harmonygames.co. It gives the Jan to Sep totals by Griffin category from OE 12, the monthly run-rate 3,334.78 from OE 21 and the disputed Midjourney 60.00 from OE 22 (trap: reply-all on the original message reaches only Leonard and Arthur, not Robert).
