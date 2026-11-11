# Census A: close-out cash plan (Feb 14, 2026 normal universe, persona Robert)

Facts and locators only. No task text. Clock 2026-02-14 00:00 UTC.

## 0. Method, scope, locator key

Locator key
- `G:00016827#6` = Gmail `threads/00016827.json`, message index 6 (Robert's mailbox).
- `L:1856956473569789052` = Gmail `threads/leonard@harmonygames.co_<id>.json` (Leonard's own mailbox, not Robert's).
- Slack: WD = #winddown C0ADGSZKR3R, EX = #executives C07C2866011, AD = #admin_foundersonly C04UEQVDVB7, LB = #leapblock C05URGU759U, PR = #prototype C09UHHN6PFZ, followed by ts.
- SF = FINANCE.EXPENSES: `/tables/15` MONTHLY_BURN, `/tables/16` CASH_BALANCE, `/tables/38` FINANCE_LEDGER (FIN-nnnnnn), `/tables/39` PAYROLL_ROSTER.
- PL = sheet "Harmony Games P&L and forecast - Jan 2026", gsheets `/sheets_spreadsheets/141`, id f_605121f4a36752645e0ac3, tabs HG P&L, HG Salary & Benefits, HG Costs.
- TL = sheet "Task List", gsheets `/sheets_spreadsheets/76`, id f_31115ddb6ed866f2b10d60.

Reach checked with `persona_view.py can-see`
- YES: WD, EX, AD, LB, PR; PL; TL; 13 Robert-mailbox threads spot-checked (00016827, 16883, 16902, 16879, 15367, 16283, 16690, 16872, 16852, 16397, 16885, 15129, 16704). Other `G:` rows are in the same mailbox, so the same rule applies, but they were not run one by one.
- NO: DM D04UC0UEN2V, DM D04UGG61DUM, AWS channel C05TNSRRLLW, Gdoc f_0c37bb7235683d73569903 (Sunset call notes, gdocs `/docs_documents/26`), Drive SVB csv f_e4998ea972c2b14a7a9d9f, and all 5 `L:` threads tested.
- Snowflake is unscoped.

Coverage limits
- Gmail Jan-Feb 2026 list: `date` key search on both date formats. ISO dates give 289 Feb and 476 Jan thread files (Robert plus 5 other mailboxes). RFC dates give 904 Feb and 1,668 Jan matched messages (Leonard, Arthur, staff). Finance filtering was by subject and sender keywords, so a finance mail with a bland subject could be missed.
- Slack: full reads of WD Feb, EX Feb, LB Feb, AD Jan-Feb, EX Jan by money regex. All other channels by keyword over 2025-2026 only.
- Snowflake: only the four finance tables above. A listing of all tables was stopped unfinished, so other tables are not checked.
- Linear, Confluence: "wind down", "shutdown", "sunset", "P&L", "burn rate" returned nothing relevant. Trello "wind down" 0; "budget" and "invoice" hit the 10-match limit and show old cards only. GitHub, Contacts, Calendar not swept for this.
- NOT READ: every PDF/xlsx/docx attachment, and every Slack image. `hg.py` does not extract them and raw reads were barred. That includes the Sunset SOW and proposals, Singular and Unity invoices, and the screenshots of the Feb 2 card balance and the subscription list. Slack canvas "Shut Down List" (files.json `/24557`, WD 1770663250.160009) has no content in the export.

## 1. Money-line table

Status means status at the clock. "Settles?" means whether the base settles the line for a Robert-reach reader.

### Inflows

| # | Line | Amounts quoted | Sources | Author, date | Robert | Status | NB | Settles? |
|---|---|---|---|---|---|---|---|---|
| I1 | Data license cash from Sunset | $22,500 all cash | G:00016827#6 offer; #7, #8 licence with s1.5 IP and s7.9; #9 ready to sign; #11 "Once we've received the data, we'll initiate the payment". WD 1770911000.728559, 1770924424.711879, 1770927223.969899, 1770931777.561519 | Sunset CEO, Leonard, Feb 12 | YES | Signed, NOT received; paid only after data delivery | none | Amount settled, timing open |
| I2 | R&D credit (Fondo) | $24,275; "$25K"; PL forecast row $6,250 in Feb and May 2026 | G:00015367#0, #1, #2. EX 1770765242.026329, 1770765443.359489, 1770780604.709459, 1770780769.446499 (Robert: "a credit, not a rebate"). PL HG P&L "The Federal R&D tax credit". DM D04UGG61DUM 1770769559.553059 "spent $4K to get nothing" (NO) | Fondo, Leonard, Feb 10-11 | YES | Cash value about nil: payroll offset, carries forward only if payroll resumes | NB-2 adjacent (PL) | Settled: $0 |
| I3 | AppLovin via Tipalti | $107.75 Jan 16; $143.08 Dec 16; $411.98 Nov 20. Ledger +107.46, +90.14 | G:00016397, 00016385, 00016188, 00016038. FIN-000686, FIN-000697 | Tipalti, ledger | YES | Monthly trickle; no Feb mail at clock | NB-4 for Feb row | Open, small |
| I4 | Unity Ads payout via Tipalti | USD 124.56 Jan 30 | L:1855753379735725968, L:1855734865618898957 | Tipalti | NO | Paid to company | none | Out of reach |
| I5 | Meta Audience Network | Amounts in PDFs only | Remittances to G:00016222 (Dec 21). Self-billing docs G:00016323 (Jan 9), G:00016816 (Feb 9) | Meta | YES | Unknown | none | Open |
| I6 | Apple / Google payouts | +118.81 Dec, +78.27 Jan, +48.19 Feb | FIN-000685, 696, 704. No payout mail found ("payment on its way" 0 hits, all Gmail) | Ledger | YES | Ledger only | NB-4 (Feb); NB-9, NB-26 adjacent | Open, small |
| I7 | "Stuck" ad revenue, publisher ID 568361 | No amount | G:00016852, 00016887 (vendor says the pub ID is not created in its system, try a new account), 00016894 (no body) | Ticket mails to Robert, vendor masked as SVC_*, Feb 11-12 | YES | Open ticket | NB-12 type | Open |
| I8 | Laptops, build machines | "a few thousand dollars" for Leonard's own laptop | EX 1770836773.353839, 1770836799.890919, 1770839126.382429, 1770850852.708789, 1770852377.756689. TL row "Get list of assets" unticked | Leonard, Feb 11 | YES | No list, no valuation, hoped not to sell | none | Open |
| I9 | IP auction | No amount | EX 1770839149.629569, 1770850800.723979. G:00016883#0. G:00016827#8 s1.5. Asset-offer detail only in Gdoc 26 (NO). G:00016834 is a broker cold mail, not a bid | Leonard, Sunset, Feb 11-12 | YES | Not started | none | Open |
| I10 | Founder cash injection | $25K each, $50K total, $75K, $15K (all plans) | EX 1767730784.379929, 1768592753.738159, 1769106292.270979. Robert 1768513529.450809 | Jan 2026 | YES | No record it happened | none | Implied none |

### Outflows

| # | Line | Amounts quoted | Sources | Author, date | Robert | Status | NB | Settles? |
|---|---|---|---|---|---|---|---|---|
| O1 | Sunset wind-down fee | $13-15K; ~$15K; 20% off if both deals; $11,700; "$12K"; "slightly higher" with CA. Implied base $14,625 is derived, not stated | G:00016883#0; G:00016827#4, #6, #7, #10, #11; G:00016902#0 (signed SOW, PDFs unread). EX 1770850852.708789. WD 1770911000.728559, 1770924465.624129. FIN-000702 -11,700 dated Feb 12. BURN legal 12,480. DM D04UC0UEN2V 1770927719.631589 (NO). L:1856956473569789052 "time to make your payment" (NO) | Sunset, Leonard, Feb 11-12 | YES except the two marked | Signed. Paid or not disputed by systems | NB-4 | Amount near-settled (PDF unread). Paid state must stay out |
| O2 | SVB card balance | $10K Oct, $10K and ~$9K Nov, $5K Jan 6, $6K Jan 12, $8.5K Jan 22, $8K Jan 23. No Feb figure | EX 1759700922.740289, 1762543717.491809, 1763584485.506759, 1767729443.014589, 1768248003.017699, 1769106738.535749, 1769193734.450429. Feb 2 "can't pay our credit card debts" EX 1770068165.918699 (image unread). WD 1770860000.975869, 1770911000.728559, 1770927223.969899, 1770927475.589379, 1770931801.955279. Statement mails G:00016274 carry no amount, and none found for Feb. L:1845454913903205585 #1, #2 (NO) | Leonard | YES except L: | Owed, unpaid, card being closed | none | Payoff amount OPEN |
| O3 | SVB loan or other bank debt | None found | AD 1754445622.992119 (officer loan repaid Sept 2023), AD 1754444610.360899 "$40K credit card liability" (QBO mismatch). PL "Loans repayable" blank. Slack "loan": 19 hits 2025-26, none a bank loan | Leonard | YES | None on record (keyword scope) | none | Implied none |
| O4 | Chase | Closed; cashier's check into SVB | AD 1761866217.159599, 1761954952.006759. WD 1770932925.126829 (Carta still points at it) | Leonard, Oct 2025, Feb 12 | YES | Closed | none | Settled |
| O5 | Singular | $6,250 overdue (presumably INVSINC23580 of Dec 1, PDF unread; due extended to Mar 15); $18,750 "to pay" | G:00016283#0-#4, 00016373, 00016086, 00014699, 00014704. WD 1770674268.840059, 1770932503.543519. EX 1770765511.243329. Sunset template G:00016885 | Singular, Leonard, Jan-Feb 12 | YES | Termination ask sent Feb 12 21:43Z; no reply | NB-23 (INVSINC22671: G:00015167, 00015243) | OPEN |
| O6 | Unity Pro licence | "~2.348*9 months" (unit unstated; 21.132); PL Unity License $1,200/mo | EX 1770765511.243329. WD 1770680635.748589 (no contract found), 1770932147.282819 (draft), 1770933903.645709. Invoices to G:00015915 (Nov 10, last found), PDFs unread. PL HG Costs. AD 1754605999.487199 (Leonard's own cards) | Leonard, Arthur | YES | Arthur tasked to email; no sent copy or reply found | NB-2 (PL) | OPEN |
| O7 | Helpshift | $150*10=$1,500; $150*8; $300 late dues paid personally; INV/HSUS9879 $150 | WD 1770673467.186629, 1770673717.808759, 1770789534.434749. EX 1770765511.243329. AD 1768333539.052869, 1770765910.100299, 1770766119.978069. L:1856273045304945702 (NO) | Leonard, Feb 9-11 | YES except L: | Back dues paid by Leonard; cancel accepted | NB-5, NB-8 | Settled only as "agreed to cancel" |
| O8 | Deel pro rata requests | $4,500 and $5,100 ("22 Working days pay", submission date 2026-01-01) | G:00016872#0, #1 | Deel to Robert, Feb 11 | YES | Awaiting Robert's approval; no disposition in base | NB-12 (names masked) | OPEN (see H6) |
| O9 | Contractors' final pay, 30-day notice | "entitled to receive fund" and 30 days heads-up; no Feb pay; letters say all earned amounts paid | EX 1770827301.625889, 1770827329.952369, 1770837154.629869, 1770837388.620769, 1770837415.345289. WD 1770665404.785659, 1770841239.761999. G:00016873-78. ROSTER-0043, 0077, 0111, 0145 = $0 for Feb | Leonard, Feb 9-11 | YES | No claim recorded; notice exposure unquantified | NB-15, NB-22, NB-1 | OPEN (contingent) |
| O10 | Leapblock / Martin | ~$600 optional gesture | WD 1770922666.421089, 1770922695.044319, 1770922731.444009, 1770922747.152399. LB 1770842824.806309, 1770843210.089359, 1770843315.839239. G:00016875, 00016690#2 ($3,700) | Leonard, Feb 11-12 | YES | Not owed; undecided | NB-29 (LB says "yesterday") | Open, discretionary |
| O11 | Deel, Gusto, Intuit kept | PL: Deel $250, Gusto $128, QuickBooks $115 per month | WD 1770839688.408909, 1770839729.441789, 1770933601.686309. PL HG Costs. G:00016688 ($5 fee overdue) | Leonard | YES | Running | NB-2 (PL) | Open, small |
| O12 | Carta | No amount | WD 1770932858.658179, 1770932925.126829, 1770935621.095649 | Leonard, Feb 12 | YES | Terminations done, renewal later | none | Open, small |
| O13 | Other subscriptions | Metabase + dbt ~$300/mo; ledger SaaS $786/mo | WD 1770837766.132019, 1770839322.836779 (Soundly), 1770837793.168589 (layer), 1770839715.391309, 1770933903.645709, 1770936655.574079, 1770937188.477219, 1770937232.664809 (moved to Arthur's KubLLC card). Figma WD 1770859313.592649. G:00016704 Google Workspace (PDF). FIN-000703 | Leonard, Arthur, Robert | YES | Mostly cancelled or moved | NB-2, NB-12 ("cursor and [PERSON_NAME_20852]") | Mostly settled, amounts not |
| O14 | AWS bills and credits | ~$1K/mo DD prod, "easy to get to 300"; ledger $1,485; PL $0; credits $84,230.12 at Apr 2025 | WD 1770680900.228399, 1770680984.725779, 1770682219.100789, 1770686219.875929. FIN-000687, 698. PL Hosting row. C05TNSRRLLW 1744735421.558919 (NO) | Arthur, Leonard | YES except channel | No Jan-Feb AWS invoice in Robert's mailbox; credit balance unknown | NB-2, NB-4 | OPEN |
| O15 | Delaware franchise tax | No amount. Due Mar 1. Gross assets given as $52,686.59. Last year $1,022,847 | G:00016879#0-#5, G:00011034. L:1854402939785612241 (Fondo will email tax due first; NO) | Fondo, Leonard, Feb 11 | YES | Being prepared, unpaid | NB-3 on the $52,686.59 | Amount OPEN |
| O16 | CA and NC withdrawals, registered agent | CA added to proposal; PL "State Franchise Taxes"; agent is Cogency Global | G:00016827#7. WD 1770675894.906889, 1770924465.624129. G:00003620, 00006197, 00006235, 00014608. DM D04UGG61DUM 1752173795.897819, 1752173881.001499 (NO) | Leonard, Sunset | YES except DM | Inside Sunset scope per quote; state tax owed unknown; no FTB mail in Robert's mailbox | none | Open |
| O17 | Accountant, final return | Fondo auto-renew Nov 26; bookkeeping quote offered; Sunset quote with and without tax work | WD 1770933903.645709 ("[ORG_NAME_0304]" = Fondo by subject-line pairing in 00015367). G:00016879#4, #5. G:00016827#4 | Leonard, Fondo | YES | Fee inside Sunset if tax option bought (PDF unread) | NB-12 | Open |
| O18 | Law firm (ESG) | $715 waived; ledger legal $780 | EX 1770835673.016869, 1770835751.750039, 1770838470.719169. G:00015129#15-#19. FIN-000701. L:1856854433653763620 Clio Bill 3973 (NO) | ESG, Leonard, Feb 11 | YES except L: | Waived 100%, relationship ended | NB-4 (the $780) | Settled: $0 |
| O19 | Sherwood | No fee | WD 1770911035.362569, 1770915455.765029. G:00016832, 00016854. "too small for them" only in DM D04UC0UEN2V 1770919996.740719, 1770920027.472019 (NO) | Leonard | YES except DM | Not engaged (implied by Sunset signing) | none | Settled by implication |
| O20 | Refunds, deposits, chargebacks | Reserve asked, no figure | WD 1770664094.831769, 1770675894.906889 | Leonard, Feb 9 | YES | No record of any item | none | Open |
| O21 | AppLovin UA debt | "$4K outstanding" Oct 2025 | EX 1759700922.740289. FIN-000688, 699 (-$9.80, -$9.83) | Leonard | YES | Unknown | NB-4 (Feb) | Open |
| O22 | Founder reimbursements | $300 Helpshift; Meta ads on Leonard's own card; Unity on his cards | AD 1770765910.100299. PR 1766643244.446779. AD 1754605999.487199. FIN-000689, 700 book Meta as company cash | Leonard | YES | No claim recorded | NB-4 (Feb) | Open |
| O23 | Domain renewals | Mar 7, 2026 renewal; others | L:1856970093879434499, L:1856998630106852519 | Registrars | NO | Out of reach | none | Out of reach |

Arithmetic sketch (derived, every input soft): 22,500 in, less Sunset 11,700, less card about 8,500 = about +2,300 before bank cash, DE tax, Singular and Unity. If Singular 18,750 and Unity 21,132 (reading 2.348 as thousands) stood in full, that becomes about -37,582. So the out-of-pocket question cannot be answered from the base at the clock: it turns on two open vendor replies.

Also useful: TL rows "Get list of liabilities", "Get list of income", "Get list of assets", "Cancel Credit Card" and the R&D row are all unticked with empty Owner cells (modified Feb 10). Leonard's Feb 12 note says he "looked at the P&L and I think this covers everything": WD 1770933999.157259.

## 2. Cash in the bank at the clock

No record states a February bank balance. SVB statement mails (G:00016273, 00016687) have no figures.

| Source | Figure | As of | Reviewer view |
|---|---|---|---|
| Leonard to Fondo, G:00016879#2 | $52,686.59 | Dec 31 | Blocked, NB-3 |
| PL Ending Balance | 52,686 | Dec 31 | Blocked, NB-3 |
| CASH_BALANCE | $25,031 | Dec 31 | Blocked, NB-3 |
| EX 1767729443.014589 and later to 1769193734.450429 | "$25K" | Jan 6-23, before Feb 2 run | Quote only; not a month-end |
| CASH_BALANCE | $8,096 | Jan 31 | Blocked, NB-3 |
| PL Ending Balance | $1,653.84 (sheet last modified Jan 12, so a forecast) | Jan 31 | Blocked, NB-3 |
| SVB notices, derived | $7,800.66 = 52,686.59 - 27,076.03 (Jan 2 run) - 500 - 17,309.90 (Feb 2 run). Ignores all other flows | Feb 3 | Rests on a blocked base number. Not gradable |
| CASH_BALANCE + ledger Feb rows, derived | -$7,482.95 = 8,096 - 15,578.95 | Feb 13 | Blocked, NB-3 and NB-4 |
| Leonard's statements | "no cash reserves left" WD 1770932147.282819, G:00016283#4; "we are in debt" LB 1770843340.964829; "no money right now" WD 1770922695.044319 | Feb 11-12 | Acceptable only as what he said |

Payment notices used: G:00016267, 00016268, 00016275 (Deel $19,656.03, Eveline $3,720, Leapblock $3,700); G:00016299, 00016300 ($500); G:00016669, 00016671, 00016690 (Deel $9,889.90, Eveline $3,720, Leapblock $3,700). These individual payments are the safest cash facts in Robert's reach: they are the bank's own processed notices.

Accepted by a reviewer: only the processed payments above, and "no February close exists" (SF `/tables/16` comment). Any bank balance needs a seeded record.

Observation (derived): CASH_BALANCE seems to run one payroll early. Nov 30 $52,965 sits next to Leonard's Dec 31 $52,686.59; Dec 31 $25,031 next to his Jan 6 $25K; Jan 31 $8,096 next to the $7,800.66 Feb 3 figure. That would explain NB-3 but does not lift it.

## 3. Coherence hazards

- H1 Cash: three month-end series disagree (Section 2), and PL does not roll: Dec Ending 52,686, Jan Beginning 29,636.
- H2 Paid vs accrued: FINANCE_LEDGER books Feb items as signed cash moves; MONTHLY_BURN comment calls Feb accrued and never closed. Sunset -11,700 dated Feb 12 vs pandadoc "time to make your payment" the same day (Leonard only). G:00016827#10 says the invite follows the executed invoice; #11 says the invite went out. Paid state cannot be fixed from Robert's reach.
- H3 Timing: Sunset's fee is invoiced at signing, the $22,500 pays after data delivery. On any cash estimate above, the fee exceeds cash on hand until the data money lands. No record addresses the order.
- H4 Sunset fee: $11,700 was stated 15:43Z; CA was added at 19:27Z with "quote is gonna go slightly higher"; ledger still says $11,700; DM says $12K. The signed PDF decides and was not read.
- H5 January pay: ledger salaries $9,895.88 (Marcus, Oliver, Julia, Claire) vs SVB $17,309.90 and Leonard's "$17K to 4 people" vs PL $17,000 (NB-2). The ledger total is near the Deel run alone ($9,889.90). Leapblock $3,700 and Eveline $3,720 have no matching ledger rows in the Feb pull. Martin has no roster or ledger row in the Dec-Feb pull.
- H6 Deel pro rata: $4,500 + $5,100 = $9,600 arrives Feb 11, with a 2026-01-01 submission date, after the Feb 2 Deel run. It may be Deel re-stating January on contract closure, or a new claim. The letters say nothing is owed and Slack says no February pay. The base does not resolve this. (Interpretation, not a stated fact.)
- H7 Deel arithmetic: overdue $9,717.90 + $5.00 (G:00016688) vs $9,889.90 paid (G:00016690#0), $167.00 apart.
- H8 Unity: $1,200/mo (PL) vs "~2.348*9" with no unit, no contract found, and ledger SaaS total $786. The last invoice found is Nov 10, though Leonard says money is still owed.
- H9 AWS: PL $0, ledger $1,485, Arthur ~$1K for one account. The credit pool is only in a channel Robert cannot see.
- H10 Legal: ledger Feb $780 "Legal & accounting" vs ESG bill $715, waived. The $780 also appears in Dec.
- H11 R&D: PL still forecasts $6,250 inflows; Fondo says no cash without payroll.
- H12 Helpshift: x10 vs x8 (NB-8), $0 after cancel, $300 paid personally. Leonard's "no out of pocket" hope already sits beside his own $300.
- H13 Card limit: Slack says $150K to $25K (EX 1755063600.665359); bank thread says $150K to $75K to $38K (Leonard only).
- H14 Insolvency letters vs plan: Singular was told no funds exist (the Unity draft says the same) on the same day as the $22,500 deal and the plan to pay SVB in full. Any plan showing a surplus sits against those letters. Gdoc 26 (NO) also says the aim of settling is to return more to investors.
- H15 People count: "4 international contractors" (G:00016832#0), 6 letters (G:00016873-78), 8 Carta termination mails (Leonard only, Feb 12).
- H16 Books: Leonard says QBO balances are wrong (G:00016879#4). The Fondo "Shadow account" issue is open.
- H17 Ad revenue: Tipalti $107.75 (Jan 16) vs ledger +107.46 (Jan 31); Tipalti $143.08 (Dec 16) vs ledger +129.13 (Dec 31). Small, but no pair ties exactly.
- H18 Personal liability: "liable as bod members" (WD 1770674426.735229) vs board of Leonard plus Griffin (G:00016883#0). Griffin resigned Feb 12 (G:00016903). Robert's board status is unconfirmed by these records.

## 4. What a seed can settle, what must stay out

Can be settled by a later record without contradicting the base (date after the last base record; Gmail or Drive, since Slack ends Feb 13 10:03 UTC; Robert on To or CC):
- Singular reply in thread 00016283 after #4. Keep the arithmetic: $6,250 overdue, $18,750 total.
- Unity reply. State dollars plainly so the "2.348" unit stops mattering. Needs a new thread with Robert on it.
- SVB payoff figure from startup banking support (promised within 24 hours, WD 1770931801.955279). Should sit near or above the last $8.5K.
- Fondo's DE tax amount in thread 00016879 after #5. Do not make the answer depend on the $52,686.59.
- Sunset final fee and payment confirmation. Read the signed PDF first. A figure other than $11,700 is fine against NB-4 but reads against FIN-000702.
- Sunset data delivery and payment date, from their CTO (G:00016827#11, #12).
- Deel pro rata disposition (Arthur or Leonard to Robert).
- Leapblock gesture yes or no.
- Founder note giving the SVB balance on or after Feb 13. Must not restate Dec 31 or Jan 31, and must sit with "no cash reserves left" (a small figure fits).
- Sunset scope note: what the fee includes for CA, NC, DE, and what taxes owed are excluded. The exclusion is only in Gdoc 26 (NO) today.

Must stay out of the graded answer:
- Dec 31 and Jan 31 cash (NB-3); any Feb "paid" from the ledger (NB-4).
- PL costs for AWS, Unity, UA, salaries (NB-2).
- Helpshift date (NB-5) and months left (NB-8). Grade only that Helpshift agreed to cancel, and note the ack itself is outside Robert's reach.
- INVSINC22671 total (NB-23); letter 00016874 date (NB-22); employee vs contractor (NB-15).
- Unity Ads from AD_SPEND_DAILY (NB-19); monthly_net_burn comment (NB-10).
- Slack after Feb 13 10:03 UTC (NB-6); decision date as a window start (NB-29).
- Anything only in `L:` threads, DMs D04UC0UEN2V and D04UGG61DUM, Gdoc 26, C05TNSRRLLW.
- Token-only vendors (NB-12); contents of screenshots and unread PDFs until someone has opened them.

## 5. Natural per-record volume

Estimates, not measurements. A call = one search or one record read, with no batching, on the Robert-reach path.

| Line | Search | Thread/doc | Sheet | Warehouse | Total |
|---|---|---|---|---|---|
| I1 data license | 2 | 2 | 0 | 0 | 4 |
| O1 Sunset fee | 2 | 4 | 0 | 2 | 8 |
| O2-O4 SVB, Chase | 3 | 5 | 1 | 0 | 9 |
| Section 2 bank cash | 2 | 8 (SVB notice threads) | 1 | 2 | 13 |
| O5 Singular | 2 | 6 | 1 | 0 | 9 |
| O6 Unity | 3 | 4 | 1 | 1 | 9 |
| O7 Helpshift | 1 | 3 | 1 | 0 | 5 |
| I2 R&D | 1 | 2 | 1 | 0 | 4 |
| O15-O17 tax, states, accountant | 3 | 5 | 1 | 0 | 9 |
| O8-O10 contractors, Deel, Leapblock | 3 | 11 (6 letters, Deel, LB, EX) | 1 | 2 | 17 |
| I3-I7 ad and store payouts | 3 | 6 | 0 | 2 | 11 |
| O11-O14 subscriptions, AWS | 3 | 4 | 1 | 2 | 10 |
| O18-O22, I8-I10 | 3 | 5 | 1 | 1 | 10 |
| **Total** | | | | | **about 118** |

Caveat: a diligent agent reading whole Slack channel-months and batching lands nearer 50-70. WD, EX and AD Feb are three reads that replace about 25 of the above. The per-record weight sits in SVB notices, the six letters, Deel mails and vendor invoices, which are real but repetitive. Whether these count toward the 100+ target depends on the counted-call rule, which I did not check.

## 6. Robert doing finance work

Direct records
- Payment approver: G:00016300 (Jan 6 $500 approved by [PERSON_NAME_0054], the token Robert's mail greeting uses; inferred). EX 1767727583.081359 asks "one of you guys" to approve.
- Deel asks Robert to approve: G:00016872#0, #1 (Feb 11). Deel dues reach him: G:00016600, 00016626, 00016670, 00016685, 00016688.
- SVB notices and statements reach him: G:00016267 onward, 00016273, 00016274, 00016687.
- Soundly: asked to cancel or move to a personal card, done: WD 1770837766.132019, 1770837782.425649, 1770839322.836779.
- Sunset data prep: Figma credentials and counts: WD 1770857725.385499, 1770858495.115779, 1770859161.847129.
- Ad revenue ticket mails addressed to him: G:00016852, 00016887. The sender of the original request is not shown.
- Cc'd on Fondo, Sunset, Singular, termination threads throughout.

Opinions, not work
- EX 1767729274.157799 "able to pay the core crew for Jan?", 1767155838.423719 told staff pay extended, 1766082441.390179 "I can find money to front", 1768513529.450809 round math, 1770780769.446499, 1770835892.136369, 1770836408.471439.

Not found
- No record of Robert building or editing a budget, forecast or P&L. Leonard owns these (WD 1770933999.157259, AD Aug 2025, G:00016879#4). No mail sent by Robert appears in the Jan-Feb Robert-mailbox set.
- Nobody asks Robert for a cash plan. Leonard's own list (WD 1770934638.035469) and split with Arthur (WD 1770935695.500189) leave Robert out.
