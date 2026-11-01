OE 1  Find Leonard's request email in Frederick's Gmail and open its thread (search: subject "Card spend breakdown for Q3 Standard Metrics", from Leonard Hayes, Sep 29 2025)
        Expected: One message from Leonard Hayes, sent Mon Sep 29 2025 3:47 PM PT (22:47 UTC), to Frederick, cc Arthur Blake. It asks Frederick to: break the ledger line "Unreconciled operating expenses" down for January to September by vendor and by Griffin's categories, month by month, from the card feed folder, and tie each month to the ledger; give the Q4 monthly run-rate by vendor and anything cancelled but still charged; follow the card close notes tab in the QuickBooks close workbook; use Griffin's categories from the forwarded note; update the cut-list card on his Trello board, not a new card; put anything of Arthur's still being charged on Arthur's seat cleanup ticket; save the workbook in the Q3 2025 investor reporting folder; reply on this thread with the totals by category, the monthly run-rate and the disputed charges. It ends with "I'll tell you who else needs the reply."

OE 2  Read Griffin's category list in the note Leonard forwarded, in Frederick's Gmail (subject "Fwd: Q2 metrics - opex categories", sent Sep 29 2025 3:41 PM PT)
        Expected: Eight 2025 categories for non-payroll opex: Software & subscriptions (all SaaS and app subscriptions, including app store developer program fees); Hosting & infrastructure (cloud, backend-as-a-service, domains, and website builders and hosting); Research & user testing; Marketing (non-UA); Travel & events; Hardware & equipment; Professional & admin (includes registered agent, filings, payroll/HR, equity and accounting platforms); Other G&A (bank fees not tied to a purchase, shipping, coworking, team meals). Paid user acquisition is reported separately, not in opex. Two items left open: "I will confirm where conference passes and engine licences (Unity seats) go before your Q3 submission." "These replace the 2024 list."

OE 3  Find Leonard's later instructions in Slack: who else gets the reply and Griffin's answers on the open items (Frederick's DM with Leonard, Sep 30 2025)
        Expected: Leonard, Sep 30 2025 9:05 AM PT: "for the card breakdown reply, add Robert, he needs the Q3 numbers for the investor update. Arthur stays on." Next message, 9:07 AM PT: "and Griffin answered his two open items on the categories: conference passes go under Marketing (non-UA), not Travel & events, and Unity seats go under Hosting & infrastructure, not Software & subscriptions. Use those for the Q3 numbers"

OE 4  Look up Robert's address in Contacts (search "Robert")
        Expected: robert@harmonygames.co.

OE 5  Read the booking rules in Drive/Sheets (spreadsheet "QuickBooks close 2025", tab "Card close notes", all rows)
        Expected: 12 rules. 1: cards 0417 (Leonard) and 2208 (Arthur, closed Jul 31). 2: the line holds rows no bank rule matches and ties to FINANCE.EXPENSES.FINANCE_LEDGER; payments are not spend. 3: posted-date statement cycles; 25th close through May (January = Dec 26 to Jan 25); June cycle May 26 to Jun 25; July cycle Jun 26 to Jul 28; then the 29th to the 28th. 4: no June ledger line, July carries both cycles; in the By vendor and Category by month tabs the June cycle stays its own month (2025-06), only the Ledger tie-out puts it under the July line. 5: a refund reduces the cycle it posts in. 6: only Jan to Sep 2025 cycles. 7: an ad-network charge is a reclass in the tie-out, not a category. 8: status lives on the Trello list "Subscriptions (card)"; a cancellation or downgrade counts once confirmed, even before it is on the board; a charge after a confirmed cancellation is disputed unless the feed shows it refunded; an annual plan is charged until it lapses. 9: run-rate covers only Unreconciled-line vendors (Bank rules vendors out), plans only; monthly plans at the latest-cycle purchase amount, annual plans at 1/12 of the last annual charge, registered-agent (COGENCY GLOBAL INC) renewals are annual plans, confirmed cancellation 0, confirmed downgrade at the new price, fee rows count with the plan. 10: the feed notes doc explains the columns, the fee rows and the adjustments tab. 11: tabs By vendor, Category by month, Ledger tie-out, Q4 run-rate; USD to the cent; months YYYY-MM. 12: one vendor per brand; Apple Developer Program separate from Apple Store; Unity seats separate from Unity Ads.

OE 6  Read the vendors booked outside the line (same spreadsheet, tab "Bank rules")
        Expected: Seven patterns: AMAZON WEB SERVICES, GOOGLE *GSUITE, SLACK T, LINEAR, GITHUB, FIGMA, ATLASSIAN.

OE 7  Read how the feed works in Drive/Docs (Doc "SVB card feed - how it works" in folder "SVB card feed 2025")
        Expected: Columns posted_date, txn_date, card, cardholder, descriptor, amount_usd, original_amount, original_currency, type. Refunds are negative; payment rows are the autopay, not spend. A FOREIGN TRANSACTION FEE row is a 3% fee on the charge directly above it and counts with that vendor. Late reversals and credits sit on a second tab named "adjustments". Card 2208 closed Jul 31 and Arthur's subscriptions bill to 0417 from August.

OE 8  List the feed sheets in Drive (folder "SVB card feed 2025", follow page tokens to the end)
        Expected: 496 daily sheets named card_0417_YYYY-MM-DD and card_2208_YYYY-MM-DD, Dec 26 2024 to Sep 29 2025, plus the feed Doc.

OE 9  Read every feed sheet from OE 8 in Sheets (tab Sheet1 on all 496, plus the "adjustments" tab on the 7 sheets that have one)
        Expected: 653 rows: 343 purchase, 12 fee, 7 refund, 15 payment, 276 "no postings". Includes UNITY ADS 1,000.00 (Aug 20); COGENCY GLOBAL INC 300.00 (May 16); MIDJOURNEY INC. 60.00 (Aug 2), -60.00 on the Aug 25 adjustments tab, and 60.00 (Sep 2); LOOM 75.00 (Jul 9), -75.00 on the Jul 15 adjustments tab; SENSOR TOWER -106.67 (Sep 8 adjustments) and 250.00 (Sep 24); UNITY TECHNOLOGIES 10,200.00 (Aug 8); HEROIC LABS 600.00 (Sep 10).

OE 10  Total the unmatched card spend per statement cycle (rows from OE 9; posted-date cycles from OE 5; drop the seven Bank rules patterns from OE 6 and payments; keep fees and refunds)
        Expected: 2025-01 7,759.99; 2025-02 8,914.76; 2025-03 12,214.05; 2025-04 6,268.22; 2025-05 5,928.41; 2025-06 12,222.02; 2025-07 12,132.35; 2025-08 22,090.21; 2025-09 10,438.20; Jan to Sep 97,968.21 (trap: the Sep 29 rows, United 312.40 and DoorDash 96.18, belong to the October cycle and are left out).

OE 11  Read the ledger lines in Snowflake (FINANCE.EXPENSES.FINANCE_LEDGER, COUNTERPARTY = "Unreconciled operating expenses", DATE Jan 1 to Sep 30 2025)
        Expected: Eight rows, amounts negative: 2025-01-31 7,759.99; 2025-02-28 8,914.76; 2025-03-31 12,214.05; 2025-04-30 6,268.22; 2025-05-31 5,928.41; no June row; 2025-07-31 24,354.37; 2025-08-31 22,090.21; 2025-09-30 10,438.20.

OE 12  Tie each cycle to the ledger (OE 10 cycle totals against OE 11 ledger lines, rules 4 and 7 from OE 5)
        Expected: Jan to May, Aug and Sep match one to one. June cycle 12,222.02 + July cycle 12,132.35 = July line 24,354.37. August includes UNITY ADS 1,000.00, shown as a reclass to paid UA, so categorized August opex is 21,090.21. Categorized Jan to Sep opex 96,968.21 + 1,000.00 reclass = 97,968.21.

OE 13  Total the spend by vendor for Jan to Sep (rows from OE 10; brands merged per rule 12; fee rows with their vendor)
        Expected: 43 vendors: Unity Technologies 17,970.00; United Airlines 12,971.12; Apple Store 11,866.87; Marriott 8,624.71; Best Buy 7,337.00; Heroic Labs 5,400.00; Google Cloud 3,587.96; DoorDash 3,022.87; Carta 2,760.00; WeWork 2,691.00; PlaytestCloud 2,086.46; Informa (GDC) 1,999.00; Uber 1,447.80; Gusto 1,326.00; AppMagic 1,293.46; Deel 1,127.00; OpenAI ChatGPT 1,050.00; Sensor Tower 1,043.33; Fiverr 1,020.00; Unity Ads 1,000.00 (reclass); LinkedIn Sales Navigator 899.91; QuickBooks Online 810.00; FedEx 761.90; USPTO 700.00; Zapier 661.50; Midjourney 480.00; Loom 450.00; DE Div of Corporations 450.00; DocuSign 405.00; Notion 360.00; 1Password 359.55; Envato Elements 324.42; Canva 315.00; Cogency Global 300.00; Webflow 261.00; Mailchimp 180.00; Calendly 144.00; Backtrace 118.00; Apple Developer Program 99.00; Namecheap 86.40; Zoom 79.95; Supernormal 54.00; ElevenLabs 44.00.

OE 14  Total by Griffin category and month (vendors from OE 13 mapped to the categories from OE 2; months 2025-01 to 2025-09)
        Expected (with Griffin's answers from OE 3: conference passes in Marketing (non-UA), Unity seats in Hosting & infrastructure): Software & subscriptions 682.43 / 1,155.92 / 778.56 / 826.04 / 872.27 / 868.38 / 1,236.85 / 1,107.91 / 832.76 = 8,361.12; Travel & events 1,191.91 / 1,574.15 / 3,378.42 / 600.95 / 0 / 3,265.46 / 2,819.87 / 4,241.59 / 5,971.28 = 23,043.63; Hardware & equipment 2,824.05 / 710.85 / 1,522.08 / 1,224.90 / 1,651.95 / 4,974.24 / 3,506.75 / 2,400.22 / 388.83 = 19,203.87; Hosting & infrastructure 2,127.12 / 2,141.57 / 2,154.90 / 2,256.46 / 2,116.48 / 2,053.13 / 2,191.71 / 11,238.15 / 1,025.84 = 27,305.36; Professional & admin 342 / 342 / 3,552 / 342 / 679 / 379 / 1,079 / 379 / 379 = 7,473.00; Other G&A 592.48 / 592.27 / 730.47 / 503.69 / 608.71 / 681.81 / 958.17 / 1,043.34 / 764.83 = 6,475.77; Research & user testing 496.62 (Mar), 514.18 (Apr), 1,075.66 (Sep) = 2,086.46; Marketing (non-UA) 2,398.00 (Feb, GDC passes), -399.00 (Mar, GDC refund), 340 (Jul), 680 (Aug) = 3,019.00. Opex total 96,968.21 (trap: without Griffin's answers Software is 26,331.12, Hosting 9,335.36, Travel 25,042.63 and Marketing 1,020.00).

OE 15  Read subscription status in Trello (board "Harmony Games", list "Subscriptions (card)", every card with its plan, billing and comments)
        Expected: 24 cards, 13 with a comment. Status changes: ChatGPT Team down to 2 seats from the Sep 26 bill; Midjourney cancelled Jul 3 (conf MJ-77k2); Supernormal cancelled Mar 31; Notion cancelled Sep 25; Loom cancelled Jun 20; Zoom downgraded to Basic Jun 12, no more charges; Unity Pro annual prepay from Aug 8 for 5 seats; Backtrace cancelled Feb 28; Heroic Labs: smaller plan asked for, "waiting on their confirmation - see ENG-2370" (not a confirmed downgrade); 1Password: Leonard, Sep 29, "3 seats, not 4 - the QA vault login goes too. Confirmed in the admin console: 3 x $7.99 from the Oct bill"; AppMagic cancelled Sep 27 by Fred (email); Sensor Tower downgraded Sep 5 by Fred (email). Annual plans: Envato (renews Feb 11), Carta (Mar 3), Namecheap (Apr 17), Apple Developer Program (Jun 6). Canva's comment ("Fred: price goes up from the Jul 14 renewal (email)") is a price rise, not a status change, so Canva stays active at its latest-cycle 45.00. The other 11 cards (Apple Developer Program, Carta, Deel, DocuSign, Envato Elements, Google Cloud, Gusto, LinkedIn Sales Navigator, Namecheap, QuickBooks Online, Webflow) have no comment and are still active.

OE 16  Read the cut-list card in Trello (card "Q4 cost cuts - card subscriptions" #481, its "To cut" checklist and comments)
        Expected: Scope "anything billed to the two SVB operating cards"; context Leonard's #executives thread of 9/23. Checklist: Sensor Tower - cancel (Fred) incomplete; Notion - cancel (Leonard) complete; ChatGPT - down to 2 seats (Leonard) complete; LinkedIn Sales Navigator - cancel (Fred) incomplete; 1Password - down to 4 seats (Arthur) complete; Unity Pro - down to 4 seats (Arthur, ENG-2370) incomplete; Heroic Labs - downgrade plan (Arthur, ENG-2370) incomplete; Zoom - close the account (Leonard) incomplete. Arthur's comment of Sep 25: 1Password down to 4 seats at $7.99 each from the Oct bill (superseded by Leonard's Sep 29 comment on the 1Password card in OE 15: 3 seats); Unity Pro on the annual prepay since Aug 8, so the seat drop only happens at the Aug 2026 renewal.

OE 17  Read Leonard's cut-list thread in Slack (channel #executives, thread started Sep 23 2025)
        Expected: Leonard's reply of Sep 26 2025 11:20 AM PT: keep Sensor Tower through the bridge, cancel AppMagic instead (Fred), the rest of the list stands (trap: this supersedes the checklist item "Sensor Tower - cancel (Fred)").

OE 18  Confirm the Sensor Tower downgrade in Frederick's Gmail (subject "Your Sensor Tower plan has been changed", Sep 5 2025)
        Expected: Market Intelligence Pro $450.00/month to Lite $250.00/month, effective Sep 5. The feed bills 250.00 on Sep 24.

OE 19  Confirm the AppMagic cancellation in Frederick's Gmail (subject "Your AppMagic subscription has been cancelled", Sep 27 2025)
        Expected: Cancelled, no further charges, access until Oct 13 2025. Last charge Sep 14: 163.10 plus a 4.89 FX fee.

OE 20  Check whether LinkedIn Sales Navigator was cancelled (Frederick's Gmail search "Sales Navigator"; the #481 checklist item; the LinkedIn card)
        Expected: LinkedIn's email of Aug 21 2025, "Your Sales Navigator subscription has been canceled": access until Sep 2, "You won't be charged again." So the cancellation is confirmed (rule 8, vendor email to the owner, Fred). The feed still bills 99.99 on Sep 3 with no refund (trap: the #481 item "LinkedIn Sales Navigator - cancel (Fred)" is still unticked and the card has no comment, which makes it look active).

OE 21  Read the Envato annual plan in Frederick's Gmail (subject "Your Envato Elements receipt", Feb 11 2025)
        Expected: Teams, 2 seats, annual, A$499.00, renews Feb 11 2026. The feed posts 314.97 plus a 9.45 FX fee on Feb 11.

OE 22  Read Arthur's seat cleanup ticket in Linear (issue ENG-2370 "Seat cleanup (Unity, 1Password) + Heroic plan" and its comments)
        Expected: Unity Pro, 1Password, Heroic Labs and Google Cloud bill to Leonard's card since August. Sep 3 comment: Unity Pro moved to an annual prepay for 5 seats on Aug 8 (feed 10,200.00 on Aug 8). Sep 24 comment: asked Heroic Labs for the smaller plan at $420.00/month; "They still have to confirm it and which invoice it would start from". Arthur has not posted a confirmation on the ticket; Heroic's own confirmation is in Frederick's Gmail, read next.

OE 23  Check Heroic Labs' plan email in Frederick's Gmail (Frederick is cc'd on Heroic's mail to Arthur; subject "Your Heroic Cloud plan change is confirmed", Sep 29 2025)
        Expected: To arthur.blake@harmonygames.co, cc Frederick, Sep 29 2025 10:10 AM PT: previous plan Heroic Cloud Pro ($600.00/month), new plan Heroic Cloud Starter ($420.00/month), effective from the Oct 10, 2025 invoice. A vendor email to the account owner, so under rule 8 (OE 5) the downgrade is confirmed (trap: ENG-2370 in OE 22, the Heroic card and the open #481 item still say it is waiting).

OE 24  Read Leonard's vendor forwards in Frederick's Gmail (search each Leonard-owned subscription and plan billed on 0417, for example Webflow and WeWork)
        Expected: Two forwards from Leonard of vendor emails to him as account owner (rule 8 in OE 5: a vendor-confirmed change counts even before it is on the board), each noting it is not on the board yet. Sep 8: WeWork membership (2 dedicated desks) ends Sep 30 2025, "The Sep 1 charge was the last one; nothing more will be billed to your card." Sep 12: Webflow moves to Basic hosting, $18.00/month from the Oct 19 charge (was $29.00) (trap: the Trello list shows no change for Webflow and has no WeWork card, so the September amounts look current).

OE 25  Work out the Q4 monthly run-rate by vendor (rule 9 from OE 5; statuses from OE 15 to OE 24; Sep-cycle charges from OE 9)
        Expected: Unity Pro 850.00 (10,200/12); Heroic Labs 420.00 (downgrade confirmed by Heroic's Sep 29 email, from the Oct 10 invoice); Google Cloud 396.84; Sensor Tower 250.00; Carta 230.00 (2,760/12); Deel 147.00; Gusto 142.00; QuickBooks Online 90.00; Zapier 73.50; ChatGPT 60.00; Canva 45.00; DocuSign 45.00; Webflow 18.00 (Basic hosting from the Oct 19 charge); Envato 27.04 ((314.97+9.45)/12); Cogency Global 25.00 (300/12); 1Password 23.97 (3 x 7.99); ElevenLabs 22.00; Mailchimp 20.00; Calendly 16.00; Apple Developer Program 8.25; Namecheap 7.20; LinkedIn Sales Navigator, WeWork, AppMagic, Notion, Midjourney, Zoom, Loom, Supernormal and Backtrace 0. Total 2,916.80 per month (traps: the seven Bank rules vendors, such as AWS 2,325.00, stay out; Heroic at 600.00, LinkedIn at 99.99, 1Password at 31.96, WeWork at 299.00 or Webflow at 29.00 gives a wrong total).

OE 26  Find the disputed charges (charges after a confirmed cancellation from OE 15, OE 19, OE 20 and OE 24, against the refunds on the adjustments tabs from OE 9)
        Expected: Two disputed charges, both on card 0417 and not refunded by Sep 28: Midjourney 60.00 posted Sep 2 2025 (cancelled Jul 3); LinkedIn Sales Navigator 99.99 posted Sep 3 2025 (cancellation confirmed Aug 21). WeWork has no charge after Sep 1, so nothing to dispute there (traps: Midjourney Aug 2 was refunded Aug 25 and Loom Jul 9 was refunded Jul 15, so neither is disputed).

OE 27  Find the destination folder in Drive (search folder name "Q3 2025 investor reporting")
        Expected: One folder, owned by Leonard, Frederick a writer.

OE 28  Create the workbook in Sheets (new spreadsheet; title free)
        Expected: A new spreadsheet exists.

OE 29  Move the workbook into the destination folder in Drive (file from OE 28; new parent the folder from OE 27)
        Expected: The spreadsheet's parent is the Q3 2025 investor reporting folder.

OE 30  Set up the workbook tabs in Sheets (spreadsheet from OE 28; tab names from rule 11 in OE 5)
        Expected: Tabs By vendor, Category by month, Ledger tie-out, Q4 run-rate.

OE 31  Write the By vendor tab in Sheets (tab By vendor; values from OE 13)
        Expected: One row per vendor from OE 13 with its Griffin category, its 2025-01 to 2025-09 amounts (the vendor-by-cycle sums OE 14 adds up) and its Jan to Sep total, USD to the cent. Software & subscriptions: 1Password, AppMagic, Apple Developer Program, Backtrace, Calendly, Canva, DocuSign, ElevenLabs, Envato Elements, LinkedIn Sales Navigator, Loom, Mailchimp, Midjourney, Notion, OpenAI ChatGPT, Sensor Tower, Supernormal, Zapier, Zoom. Hosting & infrastructure: Google Cloud, Heroic Labs, Namecheap, Unity Technologies, Webflow. Research & user testing: PlaytestCloud. Marketing (non-UA): Fiverr, Informa (GDC). Travel & events: United Airlines, Marriott, Uber. Hardware & equipment: Apple Store, Best Buy. Professional & admin: Carta, Gusto, Deel, QuickBooks Online, USPTO, DE Div of Corporations, Cogency Global. Other G&A: DoorDash, FedEx, WeWork. Unity Ads 1,000.00 (2025-08) is the UA reclass and has no category (traps: Unity Technologies and Informa (GDC) follow Griffin's answers in OE 3; Heroic Labs is backend-as-a-service and Webflow a website builder, so both go under Hosting; Apple Developer Program fees go under Software, not Professional & admin).

OE 32  Write the Category by month tab in Sheets (tab Category by month; values from OE 14)
        Expected: The eight categories by month from OE 14, months 2025-01 to 2025-09 as YYYY-MM with the June cycle under 2025-06 (rule 4), opex total 96,968.21.

OE 33  Write the Ledger tie-out tab in Sheets (tab Ledger tie-out; values from OE 10 to OE 12)
        Expected: Each cycle against its ledger line, June and July both under the July line 24,354.37, UNITY ADS 1,000.00 as the August reclass; every month ties.

OE 34  Write the Q4 run-rate tab in Sheets (tab Q4 run-rate; values from OE 25 and OE 26)
        Expected: The vendor rows and the 2,916.80 total from OE 25, and the two disputed charges from OE 26.

OE 35  Record the findings on the cut-list card in Trello (card #481 from OE 16; new comment)
        Expected: A new comment on card #481 stating Sensor Tower kept on Lite at $250/month per Leonard's Sep 26 change; AppMagic cancelled Sep 27; LinkedIn Sales Navigator canceled Aug 21 but billed $99.99 on Sep 3, a charge to dispute; Heroic Labs downgrade confirmed at $420.00/month from the Oct invoice; the Unity seat drop waiting for the Aug 2026 renewal; the Midjourney $60.00 charge of Sep 2 to dispute.

OE 36  Comment on Arthur's seat cleanup ticket in Linear (issue ENG-2370 from OE 22; new comment)
        Expected: A new comment on ENG-2370 naming Arthur's subscriptions still charged on Leonard's card: Unity Pro (annual 10,200.00 from Aug 8, charged until it lapses, 850.00/month); 1Password (3 seats at $7.99, 23.97 from Oct); Google Cloud (396.84 in Sep); Heroic Labs (600.00 in Sep, 420.00/month from the Oct 10 invoice per Heroic's Sep 29 email).

OE 37  Send the reply on Leonard's thread in Gmail (send a message with the thread ID from OE 1; to Leonard; Arthur and Robert from OE 3 and OE 4 as recipients)
        Expected: A sent message in the thread "Card spend breakdown for Q3 Standard Metrics" to leonard.hayes@harmonygames.co, arthur.blake@harmonygames.co and robert@harmonygames.co. It gives the Jan to Sep totals by Griffin category from OE 14, the monthly run-rate 2,916.80 from OE 25 and the two disputed charges (Midjourney 60.00, LinkedIn 99.99) from OE 26; the by-vendor run-rate rows are on the Q4 run-rate tab from OE 34 (trap: reply-all on the original message reaches only Leonard and Arthur, not Robert).
