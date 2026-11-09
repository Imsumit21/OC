# Census C3: wind-down sources and uses from LEONARD's view

Persona leonard_hayes. Universe normal, clock 2026-02-14 00:00 UTC. Facts and locators only. No task text.
Question: can a wind-down budget (sources and uses of cash through dissolution, with a priority-of-payment decision) be built with a closed answer per line?

**Short answer: not from the base. One non-zero line closes (the $22,500). Everything that moves the bottom line needs a seed, and no base record gives a rule for order of payment. See section F.**

## 0. Scope, locators, what was read and not read

Locator key
- `L:<id>` = `threads/leonard@harmonygames.co_<id>.json` (Leonard's mailbox). `#n` = message index.
- `G:<n>` = `threads/<n>.json` (Robert's mailbox). `A:<id>` = `threads/blake@harmonygames.co_<id>.json` (Arthur's mailbox).
- Slack: WD #winddown C0ADGSZKR3R, EX #executives C07C2866011, AD #admin_foundersonly C04UEQVDVB7, PR #prototype C09UHHN6PFZ, DM-S D04UC0UEN2V (Leonard and an outside adviser), DM-A D04UGG61DUM (Leonard and Arthur), AWS C05TNSRRLLW.
- FIN-nnnnnn = FINANCE.EXPENSES.FINANCE_LEDGER (`/tables/38`). PL = sheet f_605121f4a36752645e0ac3. TL = Task List f_31115ddb6ed866f2b10d60.
- GEM = Gemini notes f_0c37bb7235683d73569903. TRANS = Sunset call captions f_caf8854ecee9e636b67169 (`Meet Recordings/harmonygames Wind Down - 2026_02_11 14_28 PST .txt`, 143 KB WebVTT, Leonard-owned, private). New lead: the Robert census did not know this file.

Reach (persona_view can-see, run this session)
- YES: GEM, TRANS, DM-S, DM-A, AWS, SVB csv, WD, EX, AD, PR, PL, TL, and L: threads 1856956473569789052, 1847493986103224582, 1848436124467937694, 1841635707568607753, 1846148320251001978, 1843611181307573177. All other `L:` rows sit in the same mailbox, same rule, not run one by one.
- NO: A:1842380364650812223 (Unity Pro 2025 renewal notice), G:00016887 (Feb 12 ironSource reply).

Read
- Whole channel-months: WD Feb (206), DM-S Feb, DM-A Feb, AD Feb. EX Feb by money regex plus context; EX Jan by context around cash lines. PR Feb by Unity/money regex. AWS channel by credit/bill regex, 2025 only (no file after 2025-10).
- Leonard's mailbox: all subjects on threads rooted from 185* (late Nov 2025 on; 1,348 threads), filtered by a finance regex to 215, then about 60 read. A `date_parsed` scan found 10 older-rooted threads with Jan-Feb messages; 3 of them matter and were read. Subject search used the letter "e", so a subject without an "e" could be missed.
- TRANS: all of it, rendered to plain text in memory (about 15K characters).
- SVB csv: `hg.py get` cannot parse CSV, so I read that one located Drive file and TRANS directly, read-only, using the route SEARCH.md gives for located non-JSON files.

NOT read
- All PDFs and Gmail attachments, including the signed Sunset SOW, the three Sunset proposal versions, `Harmony Games, Inc-dissolution-proposal (1).pdf` (EX 1770852126.205579), the data licence, Singular and Unity invoices, Meta self-billing and remittances, the Cogency Excel.
- All Slack images, including EX 1770068148.910109 (Feb 2 bank or card screenshot), EX 1769106675.507529 and 1769106840.164259 (Jan 22), WD 1770670533.759769, 1770674426.735229, 1770934041.066969 (the adviser's and Griffin's guidance arrive as images).
- Shut_Down_List canvas (no content in the export). Confluence, Linear, Trello, GitHub, Contacts, Calendar not swept for this question. Arthur's AWS statement mails not opened. PL re-read only for spot rows.

## A. Line table

"Settle" means Leonard can reach a closed figure from records he can read, with no NB in the way. Y = yes, P = partly, N = no.

### A1. Inflows

| # | Line | Amount variants, locators | Status at clock | Settle | NB | What a seed must say |
|---|---|---|---|---|---|---|
| I1 | Data licence | $22,500 all cash L:1856675475513544349 #6. "$25K", "$50K", "mid-to-high five figures" are earlier hopes (EX 1770765443.359489, EX 1770852347.971239, GEM). DM-S 1770927601.474289 | Signed L:1856956325151717005. Paid only after delivery: "Once we've received the data, we'll initiate the payment" #1. Arthur has the export job, WD 1770935695.500189 | Y amount, N date | none | Expected pay date from Sunset's CTO, if the budget is dated |
| I2 | Federal R&D credit | $24,275 L:1843345377879232069. "$25K" EX 1770765443.359489. PL row $6,250 Feb and May. "a check of $10k last year" EX 1770770814.337959 | Cash nil: offset only, needs payroll tax, L:1843611181307573177 #0, EX 1770780604.709459. Q4 payroll about $4, #1 | Y: $0 | NB-2 adjacent (PL) | Nothing |
| I2b | CA R&D credit (new) | $8,831 carry-forward, L:1843345377879232069 | Reduces future CA income tax only | Y: $0 | none | Nothing |
| I3 | AppLovin via Tipalti | $143.08 L:1851678451672054518 (Dec). $107.75 L:1854475066032742268 (Jan). Ledger +107.46, +90.14 | Monthly trickle, no Feb mail | P | NB-4 on Feb row | One Feb remittance if the line is graded |
| I4 | Unity Ads payout | USD 124.56 = 48.04 + 46.48 + 30.79 less 0.75 fee, L:1855753379735725968 | Paid Jan 30 by ACH, already inside any Feb balance | Y | none | Nothing |
| I5 | Meta Audience Network | L:1852151312464988239 and "RE: meta Invoice" L:1851036645583518746, L:1853846395654085668, L:1856653582887507612 | Body says only "self accounted document" (L:1856653582887507612); amounts in attachments | N (UNREAD) | none | Drop the line or state a figure |
| I6 | Store payouts | Google Play "sent a payment" Dec 15 L:1851587743339629469, Jan 15 L:1854395829714787224, no amount. Apple reports L:1856281529719854322, no amount. Ledger +118.81, +78.27, +48.19 | Monthly, tiny | P | NB-4 on Feb row; NB-9, NB-26 adjacent | Drop, or treat as noise under a stated floor |
| I7 | ironSource stuck balance | $520.82 vendor, Nov 24 L:1847493986103224582 #5 (and #1). "$500" AD 1764902459.815949. "$800" DM-A 1768433438.135929 | Unpaid. Wrong publisher account. Leonard passed it to Robert Feb 10 (#0). Feb 12 reply says pub ID not synced, G:00016887 (Leonard NO) | N | NB-12 risk (token) | Vendor reply on payable balance and whether it can pay a dissolving company |
| I8 | Laptops, build machines | "a few thousand dollars" EX 1770836799.890919 | No list, no valuation; TL row unticked; hoped not to sell, EX 1770852377.756689 | N | none | Asset list with values, or a founder call to exclude |
| I9 | IP and non-cash assets | No amount. Asset offer to investors, assign to co-founder if no bid: GEM, TRANS 00:04-00:05. "buy with our own money" EX 1770839149.629569 | Not started | Y as $0 at clock | none | Nothing, unless a bid is seeded |
| I10 | Founder cash | "collectively putting $50K" was tied to the reset path, L:1855133803855213163 #2. "personal cash injection" DM-S 1770672600.468329. "without using our own funds" EX 1770672708.713099 | None made. This is the decision output, not an input | Y: $0 today | none | Nothing; it is what the paper must size |
| I11 | Unity Ads prepaid balance (new) | $1,000 receipts, last L:1846032977773320100 (Oct 15). "$100 we have" PR 1770845002.610529. "don't let Unity just confiscate it" PR 1770845938.977699. Campaign live, EX 1770952992.131649 | Being spent. Not cash | Y: $0 | NB-19 (never use AD_SPEND_DAILY) | Nothing |
| I12 | AWS credits (new reach) | $84,230.12 at Apr 15 2025, AWS 1744735421.558919. Hope to move them to a new LLC, WD 1770680900.228399 | No later balance. Non-cash | Y: $0 cash | none | Nothing for cash. Current balance only if the AWS line needs it |
| I13 | Insurance refund (new) | Commercial and D&O expired 11/10/2025, L:1848436097230453079; "We will not renew" L:1848436124467937694 #1 | No premium, no refund | Y: $0 | none | Nothing |
| I14 | Google Ads refund (new) | Account closed 10/16/25; "refundable credit... refund within 4 weeks" is boilerplate, L:1846207913782531477 | No amount, no refund mail found | P: treat as nil | none | Nothing |

Deposits and other prepayments: "security deposit", "prepaid", "unused credit", "credit balance", "account credit" give 0 hits in Leonard's mail rooted 184-185*. Positive control: "prepay" gives 16 hits, the Unity Ads receipts among them. The string "deposit" alone was not swept.

Decoys in his inbox, not lines: Amex "disputed amount of $1218.16" L:1854334448179053772 and Cintas $32,215.50 L:1854120519158693562 read as spoofed (sender equals recipient, and the company card is SVB; INFERENCE). "Payment Notification Ref:WIRE34592924567" L:1856134735161815941 has no amount and went to three mailboxes. "ERC Payment" L:1855490609602553419 is a cold pitch; I found no ERC filing (keyword scope).

### A2. Outflows

| # | Line | Amount variants, locators | Status at clock | Settle | NB | What a seed must say |
|---|---|---|---|---|---|---|
| O1 | Sunset fee | "$13,000 to $15,000" GEM. "13 14K... maybe 15K with tax work" TRANS 00:09-00:10. 20% off for both deals L:1856675475513544349 #6. $11,700 WD 1770911000.728559 and FIN-000702. "slightly higher" WD 1770924465.624129. "$12K" DM-S 1770927719.631589 | Signed. Pay link L:1856956473569789052 (Feb 12 21:28Z). Sunset's rule: platform invite follows an executed contract and invoice (#2), and the invite came at 22:21Z, L:1856959810650143006. No receipt found | N: PDF decides, unread | NB-4 | Final fee, tax option, paid or not, and how (section F, risk 2) |
| O2 | SVB card | "$5k" EX 1767729443.014589, "$6K" EX 1768248003.017699, "$8.5K" EX 1769106738.535749, "$8K" L:1855133803855213163 #2. "can't pay our credit card debts this month" EX 1770068165.918699. Limit $150K to $75K to $38K: L:1845454913903205585 #7, #5, L:1852497440283663074. Slack says $25K (EX 1755063600.665359) | Owed. Cancel request Feb 12; "We plan to deposit cash to cover the outstanding balance" L:1845454913903205585 #2. Support replies within 1 business day, L:1856956277591180405. No reply at clock | N | none | Payoff figure from SVB support, in that thread |
| O3 | Bank loan | None. Officer note repaid 2023 (FIN-000004; AD 1754445622.992119) | None on record (keyword scope) | Y: $0 | none | Nothing |
| O4 | Chase | Closed. WD 1770932925.126829 | Closed | Y: $0 | none | Nothing |
| O5 | Singular | $6,250 overdue, due date moved to Mar 15, L:1853470742168514419 #2, #4. $18,750 EX 1770765511.243329 | Termination sent Feb 12 21:43Z, #0. No reply. "We know their CEO" TRANS 00:14 | N | NB-23 on INVSINC22671 | Reply: released, settled at $X, or refused |
| O6 | Unity Pro | "~2.348*9 months" EX 1770765511.243329. "$2K/month" DM-A 1768524765.835479. 2024 notice $2,172.36 for 11 seats L:1809312755180705364. PL $1,200 (NB-2). $2,348.50 term to 2026-09-19 is A:1842380364650812223 (Leonard NO). Seats removed Oct 27 (Arthur's mail). CINV mails in Leonard's box are the Unity Ads series, not Pro (learnings §15); Pro bills as INZ invoices: 12 monthly mails in Arthur's box, last A:1854822027634725037 (about Jan 20 by thread id), PDFs, Leonard NO | Arthur tasked, WD 1770933903.645709; no sent copy or reply. "we signed the contract so they will come after us" DM-A 1768524815.335379. No contract found, WD 1770680635.748589 | N | NB-2 | Dollar balance and outcome, in plain dollars |
| O7 | Helpshift | $150x10 WD, $150x8 EX, "$300 total" paid by Leonard AD 1770765910.100299. INV/HSUS9879 $150 L:1856273045304945702 #3 | Arrears paid; Helpshift acknowledged, #0 | Y as "no further company cash" | NB-5, NB-8 | Nothing |
| O8 | Deel pro rata | $4,500 and $5,100, "22 Working days pay" L:1856858277487884047; also G:00016872 | Awaiting approval. "we can backdate" EX 1770827616.441769, "close everyone out" EX 1770837154.629869 | N | NB-12 (names masked) | Declined or paid |
| O9 | Contractor notice | "entitled to receive fund... 30 days heads up" EX 1770827329.952369. "no payment in February" WD 1770665404.785659 | No claim recorded | N | NB-1, NB-15, NB-22 | That nobody claims, or a figure |
| O10 | Leapblock gesture | "~$600" WD 1770922731.444009, "we don't have to" WD 1770922747.152399 | Optional | Y: optional, not owed | NB-29 | Nothing; a decision item |
| O11 | Deel, Gusto, Intuit | Kept, WD 1770933601.686309. Intuit $115.00 on MASTER 5348 L:1856211152930380063 | Running | P | NB-2 for PL prices | Monthly prices through dissolution, or use receipts |
| O12 | Carta | "we have time for Carta renewal" WD 1770932858.658179 | Renewal later | N (image) | none | Renewal date and amount, or out of scope |
| O13 | Other subscriptions | Slack $87.22 L:1856103558554635848, next 3/3. dbt $100 L:1855983949220444975. Metabase $148 L:1854931586274739046. Google Cloud $4.97 L:1855947447689851459 | Mostly cancelled; GitHub, Metabase moved to Arthur's KubLLC card, WD 1770937232.664809 | P | NB-12 | Nothing if a floor is set |
| O14 | AWS | "~$1k a month", "easy to get to 300" WD 1770680984.725779, 1770682219.100789. Ledger -1,485. PL 0 | No invoice in Leonard's mail; cash vs credit unknown | N | NB-2, NB-4 | Whether AWS bills cash at all, and the final bill |
| O15 | Delaware franchise tax | 2023 $1,283.97 L:1791558449734120301. 2024 $850 L:1824509105148886763. 2025 unknown. Late: $200 plus 1.5% a month L:1851692412866877715. Files unprompted unless over $5,000 L:1854402939785612241 | Fondo preparing; amount mail not sent. Its input is a Dec 31 figure | N | NB-3 on the input | Fondo's amount, without restating the input |
| O16 | States and agent | CA $800 minimum L:1828237204553547675. CA added to Sunset scope L:1856675475513544349 #5. NC active L:1854453381163140942. Cogency renewal April 2026, invoice due about six weeks after Jan 16 (same mail). NC report reminder is a third-party nudge L:1855839987122289046. Lookalike: Cogency's "CALM PLAY LLC" renewal L:1844954159551858098 is another entity | No 2026 CA or NC amount. "only exclusion being taxes owed" GEM, TRANS 00:09 | N | none | State taxes owed, and what Sunset's scope covers |
| O16b | Washington (new) | WA DOR letter L:1850743982891899038. L&I Q4 2025 filed, EFT Jan 13 L:1854234072734812004 | His wind-down request lists "North Carolina and California" only, WD 1770675894.906889. No exit or scope record for WA. CalSavers registration exists too, L:1854305035576891971 | N | none | Whether WA is in scope, and any fee |
| O17 | Final returns | Sunset price includes prep and filing, GEM, TRANS 00:09. With and without tax option L:1856675475513544349 #8 | Inside Sunset if taken; PDF decides | N (UNREAD) | NB-12 | Which option was signed |
| O18 | ESG law bill | $715 due Feb 27, Clio Bill 3973 L:1856854433653763620. Ledger legal $780 | Waived 100%: L:1841635707568607753 #3, #2, #0; EX 1770838470.719169 | Y: $0 | NB-4 on $780 | Nothing |
| O19 | Sherwood | "too small for them", "$25K-$50K range" DM-S 1770919996.740719, 1770920027.472019 | Not engaged | Y: $0 | none | Nothing |
| O20 | Refund, chargeback reserve | Asked Griffin for "reserves... for taxes, payroll, and chargebacks" L:1856675475513544349 #13. No figure, no answer found | Open | N | none | A reserve rule, or a statement that none is needed |
| O21 | AppLovin UA | "$4K outstanding" Oct 2025, EX 1759700922.740289. Ledger small | Unknown | N | NB-4 on Feb row | Settled or owed |
| O22 | Founder-paid items | $300 Helpshift AD 1770765910.100299. "stop paying Unity out of my own credit cards" AD 1754605999.487199. Meta: see below | No claim recorded | P | none | Waive or claim, per item |
| O23 | Domain | Auto-renew Mar 7 L:1856970093879434499; expiry Mar 14 L:1856998630106852519. No amount | Falls before dissolution. Charges Google's payment method | P (no $) | none | Amount, or decision to let it renew |
| O24 | 1099s (new) | Due Feb 2, self-serve free L:1852256892664243082 | No filing record (keyword scope) | N | NB-15 adjacent | Filed or not needed |
| O25 | D&O tail (new) | Policy lapsed, not renewed, L:1848436124467937694 #1 | No cover while "personally liable" | Y as a fact: no budget line unless chosen | none | Nothing; a risk to state |

Meta, O22 detail: 52 receipt messages in 28 threads, Dec 26 to Feb 9, total $4,559.79, new ad account ID (5351 against 3125 before). Leonard: "FB didn't accept SVB credit card so I sacrificed my own" PR 1766643244.446779. But the receipts show card token `[CREDIT_CARD_NUMBER_0126]`, and SVB's own alert names that token as the "Silicon Valley Bank MasterCard" L:1846148320251001978; dbt and Metabase use it too. Other cards exist with no owner on record: x-2758 (Google Cloud), 5348 (Intuit), 0785 (learnings §23). learnings §12 records Meta as on Leonard's own card. The ledger books it as company cash (FIN-000674, 689, 700). **The base does not settle this.** It decides whether $4,559.79 is a founder claim or sits inside the O2 payoff (of it, $2,234.12 is billed on or after Jan 23, after the last card quote).

## B. Bank cash

**No Leonard-readable record states a usable February balance.** The SVB csv does not help.

- SVB csv f_e4998ea972c2b14a7a9d9f: a QuickBooks bank-feed export, 50 rows, dates redacted, Mar 12 to Apr 10 2025, columns DATE, DESCRIPTION, AMOUNT, From/To, Assigned To, Rule. No balance column. Created 2025-04-12. Useful only as colour: Unity -$1,000 on 04/04/2025, "SHADOW ACCOUNT-ICS (5727)" transfers.
- SVB statement mails carry no figures: L:1855912810932894143 (deposit), L:1853191697078540284 (card).
- Blocked: $52,686.59 (L:1856861681308161749 #3), PL, CASH_BALANCE (NB-3); ledger Feb rows (NB-4).
- Best natural record: **"we'll have 4K left in the bank I think more or less", EX 1769802855.352309, Jan 30**, said about the Feb 2 run. It is not a Dec 31 or Jan 31 figure and not from the three NB-3 sources. It is still a forecast, three days early, and a strict reviewer may call it NB-3 adjacent. Earlier: "$25K" EX 1769106725.611309 (Jan 22), same in L:1855133803855213163 #2.
- Bank-processed facts: Feb 2 Deel $9,889.90, Eveline $3,720, Leapblock $3,700 (L:1856009252762511347); Jan 2 $19,656.03, $3,720, $3,700 (L:1853201370591737665); Jan 6 $500 (L:1853597716190441992).
- INFERENCE: $25K less $17,309.90 is about $7,690, not $4K. Something near $3.7K between Jan 22 and Jan 30 is unexplained. The Feb 2 screenshot probably shows it. UNREAD.
- Statements: "no cash reserves left" L:1853470742168514419 #0; "we have no money right now" WD 1770922695.044319; "plan to deposit cash to cover the outstanding balance" L:1845454913903205585 #2.

**Smallest seed: one Gmail reply from SVB Startup Banking Support in L:1845454913903205585, dated Feb 13 PT, before the clock.** It answers Leonard's open ask and the promised 24-hour contact (WD 1770931801.955279; L:1856956277591180405). It should say:
- Card closed to new charges, payoff $X including pending items.
- Analysis Checking ***0100 available balance $Y as of Feb 13.

Constraints so nothing is contradicted:
- Y below X, so "deposit cash to cover" stays true.
- Y near the $4K quote, and low enough for "no cash reserves left". Not zero: Leonard says "no money right now" but the budget needs a real opening.
- X at or above the last quote. Roll-forward from $8K (Jan 23) plus known later charges gives about $8.2K to $10.4K before any Unity charge, depending on Meta (INFERENCE). Whichever way Meta is settled must be stated.
- No Dec 31 or Jan 31 figure, and no restated "paid" claim for February rows.
- Bank reps do not normally email a balance; a reviewer may ask for realism. A fallback is a Leonard mail to Robert and Arthur saying what SVB Go shows that day. Gmail only, since Slack ends Feb 13 10:03 UTC. Date it Friday Feb 13; "today" for the persona is Saturday Feb 14 (learnings §20).

- INFERENCE: with about $4K in checking, an $11,700-plus Sunset fee cannot have cleared from checking. Only the card could carry it, and Leonard asked SVB to stop new charges an hour before signing. The seed has to pick: unpaid, or on the card (then inside X).

This one record closes B and O2 together.

## C. Base-native decision traps

"Separate" means wrong source and correction do not arrive in one call. Same-container traps are worthless (learnings §28).

| # | Type | Convincing wrong source | Record that beats it | Containers | Verdict |
|---|---|---|---|---|---|
| T1 | Credit not cash | PL "Federal R&D tax credit" $6,250 in Feb and May; L:1843345377879232069 "used to refund"; EX 1770765443.359489 "This $25K is great" | L:1843611181307573177 #0, also EX 1770780604.709459 | PL and Sept mail are separate. EX carries hope and correction about 4 hours apart | **Live only via PL.** WD 1770933999.157259 ("I looked at the P&L... covers everything") pushes readers there. Worthless for anyone reading EX Feb first |
| T2 | Credit not cash | Unity Ads $1,000 receipt L:1846032977773320100 | PR 1770845002.610529, 1770845938.977699 | Separate: Gmail vs a long #prototype month | **Live, but about $100** |
| T3 | Credit not cash | AWS $84,230.12, AWS channel | WD 1770680900.228399 shows it is tied to the account; nothing says non-refundable | Separate | Weak: the beat is implied, the number is stale |
| T4 | Waived bill | Clio Bill 3973 $715 due Feb 27, a separate thread, L:1856854433653763620; FIN-000701 $780 (NB-4); EX 1770835751.750039 "pay this out of my own pocket" | L:1841635707568607753 #3, #2; EX 1770838470.719169 | Clio thread vs ESG thread: separate. EX has pledge and waiver together | **Best trap in the set.** Live through Gmail. The bill came 18:26Z, the waiver about an hour later in another thread. Nothing in the bill's thread cancels it, and its due date is after the clock |
| T5 | Signed, money later | L:1856956325151717005 "completed by all participants"; WD 1770931777.561519 "signed"; WD 1770911000.728559 "$22500" | L:1856675475513544349 #1 "Once we've received the data"; WD 1770927223.969899 | Offer and pay rule share one thread | **Partly worthless:** that thread returns both. The value is in sequencing: fee is due now, cash lands later (H3), which is a real decision |
| T6 | Fee that moved | GEM $13-15K; EX 1770850852.708789 "~$15K"; FIN-000702 $11,700 | WD 1770924465.624129 "slightly higher"; DM-S "$12K"; signed PDF | Separate | **Not closable.** Truth is in an unread PDF. Needs a seed checked against that PDF |
| T7 | Paid personally | WD 1770673467.186629 $1,500; EX 1770765511.243329 $150x8 | AD 1770765910.100299 $300 by Leonard; L:1856273045304945702 #1 | Separate | Live, but NB-5 and NB-8 bar the count. Grade only "no further company cash" and the $300 quote |
| T8 | Paid personally, reversed | PR 1766643244.446779 "sacrificed my own" | Receipts plus L:1846148320251001978 | Separate | **Do not build unseeded.** Two sides, a platform-recorded reading against a token match. $4,559.79 swings |
| T9 | Amount vs balance | DM-A "$800" | L:1847493986103224582 #5 $520.82 | Separate | Vendor figure is older than the $800, and it is stuck anyway. Needs a seed |
| T10 | Limit read as debt | $38,000 L:1852497440283663074; AD 1754444610.360899 "$40K credit card liability" | EX 1769106738.535749 $8.5K | Separate | Mild. Opus unlikely to fall |
| T11 | Unit trap | PL $1,200; 2024 notice $2,172.36; "$2K/month" | EX "~2.348*9" | Separate; the deciding notice is out of reach | Weak unless seeded in dollars. Also 9 months does not fit monthly billing from Feb to Aug (7 payments, about $16,440) on a Sept 19 term (INFERENCE) |
| T12 | Double count | Unity line and SVB payoff both counted | INFERENCE: Unity charged a card on file (DM-A 1768524780.676819, EX 1769106672.381349); no statement line readable | n/a | Only a seed can make this real |

Strongest natural set: T4, T1 via PL, T2, T5's sequencing, T7. All but T5 are worth under about $1,000 of cash, or $0 lines.

## R. Rules on priority and who pays (asked for in step 3)

| Rule | Locator | Who | Strength |
|---|---|---|---|
| Singular and Unity are unsecured, no liens, no personal guarantees | GEM; TRANS 00:13-00:14 | Leonard asks, Sunset assents; Sunset repeats "don't have any actual liens" at 00:14. GEM says "confirmed" | Usable, informal |
| Delaware "typically recommends two or three attempts" to get a release | GEM; TRANS 00:13 | Sunset sales lead | Practice, not law |
| Only "taxes owed by the business" sit outside Sunset's fee | GEM; TRANS 00:09 | Sunset | Clear |
| Data money is commonly used to cover wind-down costs or "pay down the SVB credit" | TRANS 00:06-00:07 | Sunset | Practice |
| Pay debts, then return capital to the fund | TRANS 00:10 | Sunset | Order implied |
| Settlement template: partial offer, card payment only, lapse deadline | L:1856872398290956689 #0, #2 | Sunset | Mechanism, no amount |
| Sunset will not negotiate releases | same; TRANS 00:13 | Sunset | Clear |
| Directors "usually personally liable that everything is done correctly" | DM-S 1770674164.307049; WD 1770674426.735229 | Adviser, not counsel | Opinion. He then disclaims US knowledge, DM-S 1770703411.978309 |
| "Singular/Unity won't come after us" | DM-S 1770927785.541319 | Leonard reporting Sunset and Sherwood | Hearsay |
| Pay SVB in full first, then close the card | WD 1770927223.969899, 1770860000.975869 | Leonard's plan | A plan, not a rule |
| Leftover goes to "SVB and cover taxes or other unexpected stuff" | DM-S 1770927719.631589 | Leonard | Plan |
| ESG: none. Griffin: no reply on reserves found (image at WD 1770934041 unread). Fondo: filing and penalty only | L:1841635707568607753 | | Silence |

**Nobody states an order of payment.** No counsel text ranks taxes, wages, card and vendors. No record says SVB is secured or personally guaranteed; "guarantor", "personally guarantee" and "secured creditor" give 0 relevant hits in Leonard's mail, and the card terms are not in the base. No agreement among founders on what they carry. The nearest are "without using our own funds" EX 1770672708.713099, "I don't want anyone to come after our families" WD 1770675724.781109, and Leonard's own $300.

Live conflict for any priority paper (H14 in the Robert census, now sharper): on Feb 12 Leonard told Singular and drafted for Unity "no cash reserves left", the same day he planned to pay SVB in full and hold money for taxes, with a $22,500 licence signed. Every plan with a surplus sits against those letters. D&O lapsed Nov 10.

Who asked for this work: unlike Robert, Leonard is the natural owner. He asked Griffin for a "Cash and liabilities snapshot, plus what reserves we should hold" (L:1856675475513544349 #13), offered Sherwood "current cash position, liabilities list" (L:1856688113228112603), and TL has unticked liabilities, income and assets rows. So "nobody asked him" is solved. He still has no one asking; a prompt can have him do it for the investor or Sunset onboarding step.

## D. Distinct-from-prior-tasks check

Read: robert_winddown_closeout README and prompt; learnings §10-44 (§10-23, 27-28, 39, 41-43 read; the rest by heading and first lines).

Reused from robert_winddown_closeout (register of 25 accounts, keep or hold, Linear issues, two monthly totals, thread reply):
- The same universe week, #winddown, Sunset, Deel, Unity, Helpshift, Singular names. Subscriptions O11-O13 overlap almost fully; keep them as one summed line or drop them.

Reused from robert-vendor-schedule (Finance, creditor schedule, "9 creditors, $12,820.45", notice list to Sunset; §39):
- The creditor-by-creditor idea overlaps O2, O5, O6, O7, O8, O18. This is the main duplicate risk.

Differs: output is a decision paper for a founder, not a register. It adds inflows, timing, non-cash assets, a sequencing problem, a pay-order decision, and founder exposure (how much to put in, what to offer Singular and Unity, what returns to investors). None of the Robert tasks has inflows or a recommendation. It does not touch Linear or account status.

Estimate, judgement only, I have no access to the gate: about 0.45-0.55 against robert_winddown_closeout. **About 0.65-0.75 against robert-vendor-schedule if the sheet is a line list of what is owed; about 0.5-0.6 if the headline ask is the decision (out-of-pocket number, order, settlement offers).** Keep the ask off "list what we owe". The 0.80 gate is passable, not comfortably. Note robert-vendor-schedule has no folder under completed_tasks, so I judged from learnings only.

Also keep clear of the sibling build-cost account (no per-game costs here) and robert_llc_takeover (I9 stays a $0 line).

## E. Per-line surfaces and call count

Counts are estimates. One call = one search or one record read, no batching, on the Leonard path.

| Group | Surface | Search | Reads | Total |
|---|---|---|---|---|
| Sunset, data deal (I1, O1, O17) | Gmail, Docs, Drive text | 2 | 9 | 11 |
| SVB, bank cash (O2-O4, B) | Gmail, Slack | 2 | 11 | 13 |
| Singular (O5) | Gmail | 2 | 5 | 7 |
| Unity Pro and Ads (O6, I4, I11) | Gmail, Slack | 3 | 9 | 12 |
| Helpshift, ESG, Clio (O7, O18) | Gmail, Slack | 3 | 6 | 9 |
| R&D (I2) | Gmail, Sheets | 2 | 3 | 5 |
| DE, CA, NC, WA, agent (O15-O16b, O24) | Gmail | 5 | 12 | 17 |
| Deel, contractors, Leapblock (O8-O10) | Gmail, Slack | 3 | 8 | 11 |
| Ad and store payouts, ironSource (I3, I5-I7) | Gmail | 3 | 9 | 12 |
| Meta receipts (O22) | Gmail | 2 | 28 | 30 |
| Subscriptions, AWS, domain (O11-O14, O23) | Gmail, Slack | 4 | 9 | 13 |
| Insurance, founders, rules | Gmail, Slack, DMs | 3 | 6 | 9 |
| Channel pages | WD 3, EX Feb 5, AD 2, DM-S 1, DM-A 3, PR 2 | 0 | 16 | 16 |
| P&L, Task List, warehouse | Sheets, Snowflake | 0 | 7 | 7 |
| Writes | Doc or sheet, email | 0 | 3 | 3 |
| **Total** | | | | **about 175** |

Collapse: WD, EX and AD pages replace most per-line Slack lookups and about 15-20 of the searches above. Without the Meta cohort a thorough run is about 125-145 unbatched, and a diligent batching run about 85-110. Natural services are Gmail, Slack, Docs, Drive, Sheets, Snowflake, plus Calendar marginally: about 6-7. The local 500-call profile is out of reach without a large seeded cohort. The only natural per-record bulk is Meta (28 threads) and SVB notices, and Meta only counts if the card question is seeded so the receipts matter.

## F. Verdict

**Lines.** 41 table lines (15 in, 26 out, counting I2b and O16b), plus opening bank cash.
- Close from the base: 16 (I1 amount, I2, I2b, I4, I9, I10, I11, I12, I13, O3, O4, O7, O10, O18, O19, O25). I4 is history already inside the balance, O10 is optional, the rest are $0. **Exactly one non-zero forward line closes: $22,500.**
- Partly: 7 (I3, I6, I14, O11, O13, O22, O23): mostly small, need a floor rule. O22 carries the Meta fork.
- Need a seed, or must be scoped out: 18. Eight facts move the answer: bank cash, SVB payoff, Sunset final fee and paid state, DE tax, Singular outcome, Unity outcome, Deel $9,600, state taxes and scope. Add the order-of-payment rule: nine seeded facts in about eight records.

**Does Leonard's reach change the Robert result?** Half. "Nobody asked him" is fixed. Reach adds real value: TRANS and GEM (unsecured, tax exclusion), the D&O lapse, ironSource $520.82, Clio vs ESG, Unity Ads, WA. But the deciding records (bank balance, card payoff, DE tax, vendor replies, Sunset's price) are not outside Robert's reach: **they are not in the base for anyone.** The SVB csv is a dead end.

**Can the answer be unique?** Yes, but only if seeds carry it. Order of payment has no base rule, so uniqueness rests on one seeded legal note, and the base's own plan (SVB first, "no funds" to vendors) is the thing that note would have to judge. The line set is open (learnings §23: any completeness claim is a claim about the whole base; Miro, BrowserStack and others were found late there), so it needs a closed rule: which lines count, and a floor for small items.

Rough shape, INFERENCE, every input soft: in about $26.5K ($22.5K plus about $4K). Out about $21K-$25.5K (Sunset $11.7K-$12.5K, card $8.2K-$10.4K, DE and state tax about $1K-$2.5K, agent and domain small). Result about +$1K to +$5.5K before Deel ($9,600), Singular ($6,250 to $18,750) and Unity (up to about $21K). The decision is what to offer those three from that remainder, and whether founders top it up. A real founder question.

**Biggest risks, in order**
1. **Seed-carried answer.** Nine seeds decide the output; the base supplies only colour and $0 lines. Opus will find seeds and add them. Expect a high score unless the traps bite, and the live ones are worth about $1,000 in total. Difficulty rests on judgement rows, which graders handle badly.
2. **Unread PDFs.** The signed SOW and proposals fix the fee and scope. Platform contradiction checks cover PDF attachments (learnings §10). A seeded fee that disagrees fails /injection, and I cannot read them. Also, if Sunset was paid by card link, its fee sits inside the card payoff: the seed must pick one.
3. **Bank seed realism** and NB-3 and NB-4 fences. Any budget invites Dec 31 and ledger figures.
4. **Duplicate gate** against robert-vendor-schedule if the deliverable drifts to a liabilities list.
5. **Bookkeeping shape.** Fit needs the headline to be the founder's decision, not the table.
6. **Meta card fork** ($4,559.79): must be seeded or kept out.
7. **Legal advice realism:** a priority answer may read as the agent giving legal advice unless Sunset's counsel states the rule in a record.

**Blunt call:** it fails as a base-grounded task and survives only as a heavily seeded decision paper. Worth pursuing only if a person can open the signed SOW first, and if the design target accepts that the discriminating work is sequencing and the settlement offer rather than retrieval. If either fails, reject it as the Robert census did.

## G. Could not do

- PDFs, attachments, Slack images: unread by rule. The Feb 2 screenshot and signed SOW are the two that matter most.
- Dataset-duplicate score: estimated, not measured.
- Line-count and call-count figures are my estimates.
