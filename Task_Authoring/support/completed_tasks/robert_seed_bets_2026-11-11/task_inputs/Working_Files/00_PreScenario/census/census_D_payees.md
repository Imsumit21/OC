# Census D: SVB payees, adjustments, era boundaries

Universe Normal, clock 2026-02-14 00:00 UTC, persona Robert. Facts and locators only.

Pointer forms. AD = #admin_foundersonly C04UEQVDVB7, FO = #founders C04UTBZL6AX, EX = #executives C07C2866011, LB = #leapblock C05URGU759U, ART = #art_outsourcing C08FG9924R2, WD = #winddown C0ADGSZKR3R. `AD 2023-10/586` = messages/C04UEQVDVB7/2023-10.json index 586. `G:00004088#0` = gmail threads/00004088.json message 0. P&L = "Harmony Games P&L and forecast - Jan 2026", f_605121f4a36752645e0ac3, shared with Robert, Leonard, Arthur.

## 0. Scope and counts

- Channel check, persona_view can-see robert: AD, FO, EX, LB, ART all YES. Also YES: #video_editing_oleg C06MXPL9536, #adjoe C07UCC631A6, #telegram-dd C09KU8U4DPF, #playablex C08H78VJG80, #zombie-match3d C0880U9751A, #company-internal C05KNDCHAAG, DMs D04UP2L3E3S (Leonard-Robert) and D05GU6L0XFH.
- Processed scope: Robert's 132 notices in svb_rows.json, all with id owner robert@harmonygames.co. 131 are USD, sum $1,667,394.32. One is 1,999.00 BGN. Census C's $1,669,393.32 adds the BGN figure as if USD.
- 24 notice spellings plus the Martin row collapse to 22 real payees (Deel 2 spellings, Singular 2, BANCO 2 accounts).
- Slack adjustment terms: all 5,353 message files. Complete for returned, refund, double pa, overpaid, reimburs, chargeback, wrong account, reversal, reversed, resend, re-send, bounced, pay back, paid back, loan, advance pay. Capped and so not complete: wire, svb, recall. For those, AD alone was rescanned for wire, sent back, failed, rejected, wrong, mistake, accident, owe, underpaid, adjust (complete). FO and EX were not rescanned for "wire".
- Gmail terms: `threads/0*.json`, 21,192 files. Capped: trademark, solsten, tyz, chase, duplicate, applovin, singular.
- `threads/0*.json` is NOT all Robert's. Low-numbered files belong to other mailboxes: G:00000047 (EMPLOYEE_0011) and G:00000403 (SVC_0019 group) are can-see NO. Check the id prefix. Every other thread cited below was checked or carries a robert@ row, except where marked.
- PDFs in Drive and Slack were not opened (raw-file rule). Screenshots are image.png only: several payment approvals show amounts only in the image.

## 1. Payee identity table

Totals are Processed notices only. "Era" game means no record names the game; the payment date is the only link.

| Notice payee (suffix) | Who | Robert-readable proof | Paid for | Game, and record | First | Last | n | Total |
|---|---|---|---|---|---|---|---|---|
| Deel, Inc. + [ORG_NAME_0057], Inc. (8380) | Deel, one payee. 24 + 11 rows, $714,059.38 + $301,287.81 | Same suffix. G:00001049 "your account to Deel– ... As soon as [ORG_NAME_0057] receives the funds"; AD 2023-05/263; AD 2024-02/273 "we paid $30K on [ORG_NAME_0057]" vs $30,570.32 on 2024-02-28; Recipient Created G:00001516 | Monthly contractor payroll, all staff on Deel | No per-game record. Era only. Person rows in P&L tab HG Salary & Benefits | 2023-09-05 | 2026-02-02 | 35 | $1,015,347.19 |
| Leapblock LTD (1359) | Bulgarian outsourcing studio under MSA (Docs /docs_documents/123, 464, 553) | AD 2023-09/554, AD 2023-11/35, LB throughout | Saga map crew, Victor art direction, Martin, animator | Saga map = DD: AD 2023-11/35, LB 2023-10/4-7. After 2024-06 Victor and Martin only. EX 2025-11/979 Martin on Combo Fighter UI. Otherwise era | 2023-10-02 | 2026-02-02 | 29 | $374,654.00 |
| Eveline Art S.R.L. (8501); created under token [PERSON_NAME_8401] | Marcus Bennett's company | AD 2023-10/586 "direct bank transfer to his company", recipient created same day G:00001856; AD 2023-12/129 "direct deposit to Marcus's company"; AD 2024-05/6 "Marcus's invoice" Factura_EVE0008.pdf; AD 2024-06/102 | Art, monthly fixed | EX 2025-11/972 VFX for Combo Fighter. Otherwise era | 2023-10-27 | 2026-02-02 | 28 | $93,171.50 |
| Adjoe GMBH (5000) | adjoe, incentivized UA | #adjoe 2025-04/9-10, 2025-05/69 | iOS US UA, three wires | Domino Delights: #adjoe 2025-09/4; G:00015531#0; EX 2024-10/3724 IO | 2025-05-05 | 2025-08-29 | 3 | $46,201.50 |
| BANCO DE AMERICA (3341) | MotMot Technologies, engineer [PERSON_NAME_24716] / [PERSON_NAME_0550] by the day | AD 2025-01/112 Arthur "Just put the MotMot payment into SVB ... 4 extra days OT ... thus the $4032"; AD 2024-06/53-58, 2024-10/227, 2024-12/5, 124 | Day-rate engineering | Era (DD). FO 2024-02/3657 | 2024-04-05 | 2025-02-27 | 10 | $37,056.00 |
| BANCO DE AMERICA (8605) | Same payee, wrong account | AD 2024-04/71 | Returned, see 2 | None | 2024-04-03 | same | 1 | $4,032.00, net 0 |
| [SOURCE_ORG_0351] Labs Inc + Singular Labs Inc (4015) | Singular, MMP | Same suffix; AD 2024-09/29-33 invoice INVSINC19046; Scheduled G:00007132#1 spells Singular for the $25,000 | $25,000 annual, $6,250 quarterly | Shared, no split. NB-23 on INVSINC22671 | 2024-09-25 | 2025-09-26 | 2 | $31,250.00 |
| PERSON_4419_NAME LLC (0115) | Node Media LLC | AD 2025-01/0-2 "closing our account with Node Media LLC", "3+ months payment"; G:00008689#0 (nodemedia.co): Sept $1,428.57, Oct $5,000, Nov $5,000 (+ Dec $5,000 = exact) | UA creative and media agency, MSA Sept 2024 (AD 2024-09/48) | DD: Meta campaigns Node_ and NM_DominoDelights; EX 2024-12/760 | 2025-01-02 | same | 1 | $16,428.57 |
| TYZ Law Group (7534) | Patent counsel | G:00002505 #1, #6; FO 2024-01/527-542, 2024-02/490-501 | $7,500 retainer, Superplay domino-tile patent opinion | DD: FO 2024-01/529, G:00002505#1 | 2024-02-06 | same | 1 | $7,500.00 |
| [PERSON_NAME_7200] (7393) | Trademark lawyer; firm Eldib & Co in G:00014372 | EX 2024-09/954-956 "$1575", "we paid $4500 previously for 2 trademark applications"; AD 2024-09/26-28; AD 2023-10/704, 710-711 | HG logo and DOMINO DELIGHTS marks. 2,250 x 2, 1,575, 1,100 | Company + DD (G:00014372). $1,100 purpose inferred from same-day mail | 2023-11-01 | 2025-03-12 | 4 | $7,175.00 |
| [PERSON_NAME_36400] (6577) | Lucas = PERSON_R001, Ukraine | AD 2024-09/63-84; AD 2024-10/211 Robert "payment for Lucas"; G:00005184 "PERSON_R001 can now pick up ... Lucas's digital wallet", receiver [PERSON_NAME_36400] | Mini-game Unity dev, $2,150 a month | DD mini games: HG Costs row 4, FO 2024-06/1092 | 2024-09-25 | 2024-11-21 | 3 | $6,450.00 |
| AppLovin Corporation (2532), tokens in two pending rows | AppLovin, UA network | AD 2025-08/57-58; AD 2025-11/38 "about to hit 90 days past due"; EX 2025-10/205 "$4K outstanding debt" | Past-due UA bills | DD per census C warehouse match (6,086.03); no Slack record seen naming the game on these two wires | 2025-08-29 | 2025-11-12 | 2 | $6,085.56 |
| Graham Porter (1794) | Art director, one-month consultant | D04UP2L3E3S 2025-05/26 "not happy about spending $5K ... true Art Director"; 2025-04/1293, 1346, 1357; G:00013367 | Art direction, 3 bosses + 9 minions | ZM3D: D04UP2L3E3S 2025-05/26 "the zombie shit", 2025-05/396 | 2025-05-29 | same | 1 | $5,000.00 |
| JPMorgan [PERSON_NAME_4503] (3203); created as [ORG_NAME_2452] by Arthur | JPMorgan Chase account. Holder NOT established | Token = Chase: G:00001114#16, G:00001373#0. Only other trace AD 2024-08/37-38 Arthur "payment started in SVB" | Unknown. See 2 | No record | 2024-08-19 | same | 1 | $4,000.00 |
| CREATIVE X TEKNOLOJi (5660) | PlayableX | Census C: C08H78VJG80 2025-03/10, EX 2026-02/24 | First playable | DD (census C) | 2025-05-16 | same | 1 | $3,750.00 |
| M [PERSON_NAME_0056] (4020) | JP, Jean Philippe Demaison | AD 2023-10/432-433, 569-571 (iban_M_JEAN_PHILIPPE_DEMAISON file), 586 | Company website | None, company. HG Costs Website Oct-23 4,200 (other $1,000 not traced) | 2023-10-27 | same | 1 | $3,200.00 |
| Nathan Price [PERSON_NAME_0047] (0148) | Short contract animator | AD 2024-07/55-59, 138-144, 2024-08/0, 24 | Coin, exclamation, chest animation; hours invoice | Era (DD). AD 2024-07/58 | 2024-08-03 | same | 1 | $2,368.00 |
| Martin [PERSON_NAME_7250] Walsh (3801) | Martin, personal Postbank account | AD 2025-10/500, 522, 529 | Laptop reimbursement | None, equipment | 2025-10-30 | same | 1 | 1,999.00 BGN |
| [PERSON_NAME_7249] Brooks (5384) | Lauren Brooks = "Silje Molna" in P&L | EX 2025-10/630 (file "Consulting Agreement Lauren Brooks.pdf", permalink consulting_agreement_silje_molna.pdf); AD 2025-10/520-521; EX 2025-10/526, 535; HG Costs row 7 | Telegram port, $500 monthly minimum | DD Telegram port, not one of the three named bets as such | 2025-10-30 | 2026-01-06 | 3 | $1,500.00 |
| PERSON_6074_NAME [PERSON_NAME_16238] (3307) | Ozhan, 2D animator | ART 2025-02/9-17; census C EX ts 1740691596.526029 | One week zombie animation | ZM3D | 2025-03-21 | same | 1 | $1,000.00 |
| [PERSON_NAME_9100] (1876) | UX contractor, = [PERSON_NAME_2349] | AD 2023-05/360 "$600 after the project, $600 more if we get funded"; AD 2023-05/865; AD 2023-10/586, 716-717; AD 2023-11/4-11; G:00001029#0 | Success half of a UX milestone | Era (DD, pre-seed work) | 2023-11-01 | same | 1 | $600.00 |
| [PERSON_NAME_0054] [PERSON_NAME_0131] (3139) | PERSON_5360, 4X proposal helper. NOT Robert, though [PERSON_NAME_0054] is the token SVB uses to greet Robert | Identity only in NO records, see 4. Robert side shows only the 4X proposal: EX 2025-05/207, 264 | "$500 for the help" | A fourth, unfunded bet: 4X crypto proposal | 2025-05-29 | same | 1 | $500.00 |
| Private Entrepreneur [PERSON_NAME_43315] [PERSON_NAME_0120] (9368) | Oleg, Ukrainian video editor (Dixelar) | #video_editing_oleg 2024-03/40, 2024-05/8-41; HG Costs UA Assets May-24 125 | First of four UA videos ($500 for 4) | Era (DD) | 2024-05-07 | same | 1 | $125.00 |

Unresolved rows: JPMorgan $4,000 (holder and purpose). Partly resolved: $500 payee (identity readable only in a Leonard DM). Nothing else stays unidentified.

Collision to avoid: AD 2023-11/26 "Payment on Dec 1st will be the normal 2250" is [PERSON_NAME_0040]'s Deel pay, not the 2 x $2,250 trademark wires.

## 2. Adjustments to Processed payments

| # | Payee | Amount | Record (author, date) | Effect |
|---|---|---|---|---|
| A1 | BANCO 8605 | -$4,032 | AD 2024-04/71, Leonard, 2024-04-12 "Blake put the wrong account number ... bank returned our money"; AD 2024-04/77-100 Robert and Leonard on how to categorize it; Recipient Modified G:00004120; re-paid G:00004124 | MotMot $41,088 to $37,056 |
| A2 | Martin | 1,999 BGN, not USD | Notice G:00015809#2; HG Costs Equipment Oct-25 = 1,209.89 (match inferred) | Sum is $1,667,394.32 + about $1,209.89. Equipment, not a game |
| A3 | Lucas | +$7,525 outside SVB | 5 Western Union receipts G:00005184, 00005350, 00005489 ($1,075 each), 00005962, 00006329 ($2,150 each); AD 2024-06/54, 111-114 "via company card"; AD 2024-07/54 | SVB $6,450 + $7,525 = $13,975 = HG Costs row 4 exactly |
| A4 | TYZ | Bill $12,240 vs wire $7,500 | G:00002505 #6-30 "These funds will be returned to you at the end of our engagement"; G:00003549#0 invoice 2334 $12,240.00 (2024-03-01); AD 2024-03/4-17 Leonard "We wasted $12K on lawyers", "paying up", "done"; P&L Legal 24-02 -7,500, 24-03 -13,002 | Balance paid off-wire. No record of the retainer being applied or returned. Patent cost is $12,240 if applied, $19,740 if kept |
| A5 | Deel 2024-09-27 | $50,244.96 includes Douglas Sep 2023 back pay | AD 2024-09/23, 40-45, 128, 149 Leonard "so 43K for Deel (we have Douglas twice, I subtracted him)". Salary tab rate $7,583 | Period shift about $7.6K into Sep 2023. Exact figure not stated |
| A6 | BANCO 2024-10-01 | $5,184 is August | AD 2024-09/156-157 Arthur "I forgot to run ... payment for August" | Period only |
| A7 | Eveline 2024-06-28 | +$160 | AD 2024-06/102 Leonard: bank cut $20 per wire, one-time 6-month retro; $3,020 after | Inside total; not a duplicate |
| A8 | Leapblock | -$300 book; January animator invoice waived | LB 2024-01/11-12; LB 2024-02/0, 14-18 | Inside 2024-01-18 $21,018 and 2024-02-07 $23,190 |
| A9 | Leapblock 2025-05-07 | $6,050 = $3,700 + $2,350 | LB 2025-05/2, 9, Leonard: Victor last day April 16 | Composition |
| A10 | Oleg | $125 re-sent | #video_editing_oleg 2024-05/8, 23, 40-41 | One Processed row, one HG Costs 125. No doubled cost shown; the route of the first attempt is not closed by a record |
| A11 | Adjoe Sept 2025 | About $4K credit, against an UNPAID invoice | #adjoe 2025-09/4-5, 2025-10/0; G:00015531#0 Leonard "credited back" | No effect on the three wires. NB-18 |
| A12 | Founders' loans | $35,500 repaid Sep 2023 | AD 2023-08/1227; AD 2025-08/24-33; P&L Loans repayable 23-09 | Not in Processed. Not bet spending |
| A13 | Deel overpayments kept | $250, about $500 | AD 2023-11/13-16 "Nah, it's fine"; AD 2023-09/544 | Not recovered, no adjustment |
| A14 | Deel 2025-08-29 | $1,505 likely $1,500 bonus | AD 2025-08/70 | Lead only |

Searched and not found: a duplicate wire, chargeback on a wire, credit note, recall, or a loan booked as a wire. Same-payee same-amount pairs (Leapblock $3,700 on 2025-08-01 and 08-29, BANCO $2,688 on 2024-07-19 and 07-29) are separate months: AD 2023-11/266 explains two in one month. Inflows that are not refunds of wires: R&D credit P&L 25-07 +10,938; AD 2024-10/197 option exercise. Off-wire refund effort: Lufthansa AD 2024-01/135, FO 2023-12/1730.

## 3. Awaiting or Scheduled with no Processed

Matched one to one on suffix and amount (Processed within -3..+21 days of Awaiting, -3..+40 of Scheduled): 1 of 130 Awaiting rows unmatched, 0 of 40 Scheduled unmatched. The BGN Awaiting G:00015811 pairs with Processed by eye.

- **Leapblock $33,290**, G:00001577#0, 2023-09-13. The only orphan. AD 2023-09/202-204 "4 different invoices from the past"; 2023-09/223-225 first wire failed, "they never gave us iban or swift"; 2023-09/230-235 Leonard "[PERSON_NAME_22849]'s 4 payments", invoices 29, 32, 33, 33; Arthur "Done!". The string 33,290 occurs in no other message in any of the 88,728 gmail files. Next Leapblock invoice is September, $22,260 (AD 2023-09/554), and nobody chases the earlier money. P&L books Jul-Sep saga map and Victor as cost. So the record says approved, and no bank notice says paid. Probable cash out, unproven. The invoices are in Drive `Invoices/Leapblock/` (0000000029, 32, 33; shared with Robert, f_06f42106818045db3b7d0d), PDFs not read.
- Singular $25,000: paid, Processed under token G:00007151#0. Deel amounts: all matched. AppLovin token rows: matched.
- Processed with no Awaiting in Robert's box: $125 Oleg; Lucas $2,150 x 2 (Robert initiated: AD 2024-10/211, so he got no approval mail).
- Later unpaid, no wire at all: Singular $6,250 past due, G:00016283, INVSINC23580.

## 4. Readable only by Leonard or Arthur (Robert NO)

| Fact | Record | Robert alternative |
|---|---|---|
| $500 payee's identity and purpose | D08RQSCFKJ9 2025-05/6, 9, 96, 104 (can-see NO); #4xgame C08JFCBMP4M, #4xgameproposal C08RD0HP7QX not his | None. Token name and amount only |
| Graham pay detail: Wells Fargo, $2,500 bonus refused, invoice, goodbye | D08QN2UDJCB 2025-05/543-577 NO | $5K and scope in D04UP2L3E3S YES |
| Martin $ = laptop, receipt, 2 x $350 grievance | C6CA6B9D1D97 2025-10/0-14 NO | AD 2025-10/500, 522, 529 say laptop only |
| Eveline named in the contract | D05UDNCCYKC 2023-10/101, 118 NO | AD tie YES, by Marcus + date + EVE file name |
| BANCO "Jan & Feb", "owe motmot 4 days" | D04UGG61DUM 2025-02/557, 2025-05/931 NO | AD 2025-01/112 for identity |
| R&D credit letter | D04UGG61DUM 2025-07/54 NO | P&L row YES, AD 2024-08/36 |
| Nathan's invoice | G:00000403 (SVC_0019 group) NO | AD 2024-07 |
| Chase wiring address | G:00000047 NO | G:00001114#16 YES |

## 5. Spending outside SVB wires

| Channel | What | Reaches Robert's mailbox? |
|---|---|---|
| Gusto | Founders' pay and US staff, tax. P&L Salary tab: Robert, Leonard, Arthur $10,416.67 a month while paid | No. 3 calendar mails only, no payroll mail |
| SVB card | Solsten $30,000 AD 2024-01/7 "with the MASTERCARD to get points" (HG Costs Jan-24); Unity licences AD 2023-09/308; Lucas Western Union; balance EX 2025-10/205 | 12 "SVB Credit Card - Statement ... Ready to View" mails, amounts not read |
| Meta | 108 receipts in 59 files, $29,827.71, 2024-01-27 to 2025-11-06. By campaign name: DD or pre-ZM $19,891.35, ZM3D (PvZ_, ZM_, ZombieTest) $9,920.15, Creative_AB_Test $16.21 | Yes, and this is the only per-game cost series found. Cards: MasterCard 4655 $2,295.96 (same last four as Robert's Western Union "company card" receipts), masked MasterCard $27,505.22, 5348 $16.21. I found no record that Meta sat on Leonard's own card |
| Unity Ads | 7 receipts x $1,000 = $7,000: G:00002874, 00003209, 00003348, 00003439, 00003851, 00007783, 00014282 (prepayment 2025-06-21) | Yes, those 7 only. Top-ups on Leonard's own cards do not reach him as receipts: EX 2025-07/1262, 2025-08/9, 185; AD 2025-08/38. CalmPlay Unity account: EX 2025-05/477, 2025-07/732, 1259 |
| Google Ads | No receipts by subject (45 subject hits, all admin or marketing) | No |
| Deel direct | Deel draws only by SVB wire after 2023-09. Fees: HG Costs Deel Processing Fee | Deel subject mails 22, not payment detail |
| Chase | Company account until 2025-10-31 (AD 2025-10/563). Pre-SVB costs: FO 2023-09/1263. Carta stayed tied to it (WD 2026-02/183). Statements zip AD 2025-11/2 | Only as a Slack file name. Contents not seen |

JPMorgan $4,000 lead: the only known Chase account is the company's own, and Carta $3,600 (HG Costs Aug-24) debits Chase, so the wire may be a top-up, an internal transfer and not a cost. No record links them.

The full list: P&L tabs HG Costs and HG Salary & Benefits, fed from QuickBooks (AD 2023-10/120 both banks connected; AD 2024-10/135 "quickbooks is just pulling data from SVB"; AD 2023-11/265 "QuickBooks only considers actual payout dates"). AD 2025-08/33 says "The P&L forecast, including starting and ending balances ... are accurate" while QuickBooks was not. No title column. NB-2 and census C's header-date warning apply. AD 2023-10/177 gives one category roll-up.

## 6. Era boundaries and payment lag

| Bet | Start | End | Records |
|---|---|---|---|
| Domino Delights | Saga map contracts Aug 2023; pre-alpha 2023-10-20 | Core team moved 2025-01; UA continued to 2025-08; Sept 2025 Adjoe dispute; Telegram port from Oct 2025 | AD 2023-08/176, 513; AD 2023-10/457; EX 2025-01/442; #adjoe. No single stop record found |
| Zombie Match 3D | Prototype talk 2025-01-03; channel 2025-01-09 | Layoffs 2025-10-24. NB-28: no end date from Meta | EX 2025-01/184, 276, 442; C0880U9751A 2025-01/0; EX 2025-03/304-344; EX 2025-10/1716 |
| Combo Fighter | Monday 2025-11-24 | Shutdown Feb 2026. NB-29 | EX 2025-11/955, 630, 972, 979 |

Processed by era (payment date; lag not corrected): to 2025-01-08 $984,888.21; 2025-01-09 to 2025-10-24 $557,471.22; from 2025-10-25 $125,034.89, plus 1,999 BGN.

Lag.
- Leapblock, in arrears, invoice at month end, paid days to weeks later: AD 2023-09/554 Leonard 2023-09-29 "leapblock's invoices for September: $15K for Saga map + $3260 for Martin ... + $4K ... -> $22,260", paid 2023-10-02. LB 2024-05/34 "APRIL invoices here" 05-14, /35 "payment initiated", paid 2024-05-14. LB 2024-06/7 "May + first week of June", paid 2024-06-20 $33,895. LB 2024-01/10 December invoices 01-17, paid 01-18. So a 2nd-of-month Leapblock wire pays the prior month.
- Eveline and Deel fixed rate, same month: AD 2023-10/634 Arthur "for the fixed rate people we have to send the payment out like 2 days before the end of the month". AD 2023-12/111, 129 "we missed Marcus indeed!" explains 2023-12-04. So a 1st-to-2nd Eveline wire usually pays the month just ended, and a 27th-31st wire the same month.
- Node: charged at start of month, billed late, paid 2025-01-02 for Sept-Dec 2024 (G:00008689#0).
- AppLovin: 90 days past due, AD 2025-11/38. BANCO: AD 2024-06/53 "pay motmot for May".

## 7. Risks

1. Deel is 61% of Processed dollars and has no per-game record. Any by-bet figure for it is an era allocation, and the task must say so.
2. Three items cannot be closed from Robert's records: Leapblock $33,290, JPMorgan $4,000, TYZ retainer. A closed answer needs a stated rule or a seeded record.
3. Tokens (NB-12): Deel, Chase, Singular, AppLovin rows rest on suffix or token decoding, and the $500 payee looks like Robert.
4. Wires are a partial list. Gusto, card, Chase and Leonard's cards are missing, and P&L cannot be graded on NB-2 lines.
5. NB-18 blocks the Adjoe September credit. NB-23 blocks the Singular invoice total. NB-15 blocks employee or contractor wording.

## Appendix: working notes in the order found (sections 0-6 above supersede them)

Channel confirmations (persona_view can-see robert): #admin_foundersonly C04UEQVDVB7 YES, #founders C04UTBZL6AX YES, #executives C07C2866011 YES, #leapblock C05URGU759U YES, #art_outsourcing C08FG9924R2 YES.

Abbreviations: AD = C04UEQVDVB7, FO = C04UTBZL6AX, EX = C07C2866011, LB = C05URGU759U, ART = C08FG9924R2. `AD 2023-10/586` means messages/C04UEQVDVB7/2023-10.json index 586.

Notice matching (scope: Robert's 350 SVB rows in svb_rows.json, matched one to one on account suffix + amount, Processed within -3..+21 days of Awaiting, -3..+40 of Scheduled, except the Martin BGN row checked by eye):
- Awaiting Approval rows with no Processed: 1 (Leapblock $33,290, threads/00001577.json#0, 2023-09-13).
- Scheduled rows with no Processed: 0. Singular $25,000 matches `[SOURCE_ORG_0351] Labs Inc ***4015` Processed 2024-09-25 (token row, same suffix 4015). Deel amounts all match.
- Processed rows with no Awaiting: 3 ($125 Private Entrepreneur 2024-05-07; [PERSON_NAME_36400] $2,150 on 2024-10-23 and 2024-11-21).

Early finds:
- M [PERSON_NAME_0056] ***4020 $3,200 (2023-10-27) = JP, website: AD 2023-10/432-433 Leonard "invoice from JP for the website" (F2300002.pdf), "great work for $3.2K"; AD 2023-10/571 bank info file "iban_M_JEAN_PHILIPPE_DEMAISON_00080258740.pdf"; AD 2023-10/586 "Need to pay JP".
- Eveline: AD 2023-10/586 "Marcus wanted to skip Deel and use a direct bank transfer to his company", same day recipient ***8501 was created (threads/00001856.json) and $2,400 paid.
- [PERSON_NAME_9100] ***1876 $600 (2023-11-01): AD 2023-10/586, 2023-10/716-717, 2023-11/4-5, 2023-11/9-11: "[PERSON_NAME_2349]'s other $600", the remaining $600 "now our raise is officially out There"; a contract honoured after the raise.
- BANCO DE AMERICA = MotMot: AD 2025-01/112 Arthur "Just put the MotMot payment into SVB. Needs approval. [PERSON_NAME_24716] worked 4 extra days OT for us in Dec thus the $4032".
- Graham Porter: art director / AI art consultant, FO 2023-05/196; harmonygames.co mail in Robert's box (threads/00013367.json, 00013640.json).
- Founders' loan: AD 2025-08/24 "That $35K loan we gave to the company was paid back to us" (to check).
- PERSON_4419_NAME LLC ***0115 $16,428.57 (2025-01-02) = Node Media LLC: AD 2025-01/0-2 Leonard "can one of you guys approve?" / "This is for closing our account with Node Media LLC" / "3+ months payment". Node MSA signed AD 2024-09/48, EX 2024-09/1507 (Harmony Games Inc MSA_September2024.pdf). Fee: EX 2024-09/1399 Frederick "Up to $100k: Fee = Greater of $5,000 or 10% of MAS". Creatives ownership same message.
- Graham Porter ***1794 $5,000 (2025-05-29): D04UP2L3E3S 2025-05/26 (Robert's DM with Leonard, YES) Leonard "I'm not happy about spending $5K but we will get shit done plus we have a true Art Director who would understand the zombie shit"; deliverables D04UP2L3E3S 2025-04/1346 (3 bosses, 9 minions) and 2025-04/1357; end D04UP2L3E3S 2025-05/396 "all the deliveries of the zombies are There". Pay detail only in D08QN2UDJCB 2025-05/543-577 (Leonard-Graham DM, NO): bank details, "$2,500 bonus" refused, invoice requested, goodbye.
- [PERSON_NAME_0054] [PERSON_NAME_0131] ***3139 $500 (2025-05-29): D08RQSCFKJ9 2025-05/6,9,96,104 (Leonard DM, NO) "you good with that $500 for the help?", "I will take care of the $500 at the end of month along with everyone else"; subject is the 4X crypto proposal ("Big Time"), not DD, ZM3D or CF. Robert side: EX 2025-05/207, 2025-05/264 show the 4X proposal exists; #4xgame C08JFCBMP4M and #4xgameproposal C08RD0HP7QX are not in Robert's membership (chmap); the helper's identity does not appear in a Robert-readable record found so far.
- [PERSON_NAME_7200] ***7393 = trademark lawyer: EX 2024-09/954-956 Leonard "The lawyer says There are no additional expected fees on top $1575", "we paid $4500 previously for 2 trademark applications" (= 2 x $2,250 on 2023-11-01, 2023-11-30); AD 2024-09/26-28 "trademark follow up lawyer work ... invoice ED02024000000016.pdf"; AD 2023-10/704, 710-711. Firm in mail: Eldib & Co (threads/00014372.json). Applies to HG logo + DOMINO DELIGHTS marks.
- [PERSON_NAME_36400] ***6577 3 x $2,150: AD 2024-09/63-84. Robert: "setup IBAN for Lucas, he has to show some 'real' income via bank transfer"; Leonard "ok, I added him to the system", "We need to pay up PERSON_R001 now because he is paying taxes on the 25th every month", "can you go ahead and approve please?", "now you have SVB access". P&L HG Costs row "Mini Game Unity Developer PERSON_R001" 13,975 = 6.5 x $2,150 (from census C). Needs one more tie.
- Robert got SVB access 2024-09-24: AD 2024-09/84.
- Deel 2024-09-27 $50,244.96 carries Douglas back pay: AD 2024-09/23, 40, 45, 128, 149 "so 43K for Deel (we have Douglas twice, I subtracted him)". 
- BANCO $5,184 on 2024-10-01 is August arrears: AD 2024-09/156-157 Arthur "I forgot to run [USERNAME_1052]'s payment for August ... Total $5184".
- Token decode: [ORG_NAME_0057] = Deel. threads/00001049.json: "your account to Deel– ... As soon as [ORG_NAME_0057] receives the funds" (same sentence, Robert's box); AD 2023-05/263 "login to [ORG_NAME_0057] and approve"; AD 2024-02/273 "we paid $30K on [ORG_NAME_0057]" against $30,570.32 Processed 2024-02-28. Same recipient suffix 8380.
- Token decode: [PERSON_NAME_4503] = Chase. threads/00001114.json#16 "our [PERSON_NAME_4503] biz account"; threads/00000047.json#1 "The address for the [PERSON_NAME_4503] account: Harmony Games GAMES INC."; threads/00001373.json#0 "move our cash from [PERSON_NAME_4503] into SVB". AD 2025-10/551 "close Chase", AD 2025-10/563 "Chase account closed. Cashiers check deposited into SVB", AD 2025-11/2 "Chase_HarmonyGames_Alllstatements_2023-2025.zip".
- Node: threads/00008689.json#0 (Robert is a recipient) Node's account manager: Sept $1,428.57 prorated (kickoff Sept 22), Oct $5,000, Nov $5,000; plus Dec $5,000 = $16,428.57 exactly. "W: nodemedia.co". Frederick #1 "That amount lines up with our MSA" (#1, #2 are between Leonard and Frederick but the thread file is in Robert's box).
- Lucas = PERSON_R001 = [PERSON_NAME_36400]: threads/00005184.json etc. Western Union receipts, "PERSON_R001 can now pick up the money ... Lucas's digital wallet", Final Receiver Details Name [PERSON_NAME_36400]; AD 2024-10/211 Robert "I initiated a payment for Lucas so he can pay his taxes on the 25th" (explains no Awaiting mail in Robert's box: he initiated). AD 2024-07/54 Robert "I paid Lucas for July, FYI".
- Robert's personal Western Union transfers to Lucas, sender Lake Oswego OR: threads/00005184 (2024-06-03), 00005350 (06-17), 00005489 (06-29), 00005962 (07-23), 00006329 (08-23). Off-SVB.
- Oleg: #video_editing_oleg C06MXPL9536 (YES). 4 videos $500 total (2024-03/40); $125 first video; 2024-05/8 Leonard "we sent the payment today directly to your bank account"; 2024-05/11 Oleg objects; 2024-05/23 "maybe we can ask for a refund"; 2024-05/40 Leonard "I re-sent the wire this time with payoneer's traditional methods"; 2024-05/41 Oleg "Yes, I receive this email. It says I will get it in 7 days". Only one SVB Processed $125 (threads/00004648.json#0, 2024-05-07 20:17 UTC, one minute after that message).
- Nathan Price: threads/00000403.json INVOICE_01 (2024-07-25, hours), Leonard's reply "helping us out with the build"; AD 2024-07/55 Robert "I ended Nathan's contract", 2024-07/58 "$2500 for one coin animation, one larger exclamation point and exploration of chest animations", 2024-07/143 approve, 2024-08/0 still not approved; 2024-08/24 "money we wasted" list. Paid 2024-08-03 $2,368.
- TYZ Law Group $7,500 (2024-02-06) = retainer on the Superplay domino-tile patent opinion for Domino Delights. threads/00002505.json (Robert cc'd): #1 Leonard on Superplay, #6 engagement terms, "We require a retainer of $7,500 ... These funds will be returned to you at the end of our engagement". FO 2024-01/527-542 patent thread; FO 2024-02/490-501 "I'm ok with their retainer policy"; AD 2024-03/4 "closed the loop with the patent lawyers - let's see the damage". threads/00003549.json#0 (Leonard fwd, TO SVC_0019_EMAIL; thread file in Robert's box): Tyz invoice 2334 Feb 2024, $12,240.00. Bank shows $7,500 only.
- Founders' loan: AD 2023-08/1227 "We are gonna get back $35,500 total for the loans"; AD 2023-09/140 awaiting Matthew's signature; AD 2025-08/24, 26, 33 "The loan from officers to the company was repaid in September 2023". Payment not in SVB Processed notices (Sep 2023 rows are Deel only). Route unknown; Chase likely (AD 2023-09/146-154 "do we want to do it via ... or SVB", "Chase is probably easier", "so you will move $7K").
- Martin 1,999 BGN (2025-10-30) = laptop reimbursement. C6CA6B9D1D97 2025-10/0-14 (mpdm Leonard, Arthur, Martin: NO) receipt invoice_9100017320.pdf, personal Postbank account; Robert side AD 2025-10/500, 522, 529 "Martin's is ready for approval". HG Costs Equipment Oct-25 = 1,209.89 (candidate USD value of 1,999 BGN). Not a game cost; not USD $1,999.
- Brooks: AD 2025-10/520-521 Leonard "Let me do [PERSON_NAME_0133] as a direct payment", "$500 I'll do a wire"; EX 2025-10/526, 535 Telegram profit-share terms attributable to [PERSON_NAME_0133].
- P&L Jan 2026 (f_605121f4a36752645e0ac3, Robert shared) tab HG P&L rows: Legal (row 19) 24-02 -7,500, 24-03 -13,002 ... 25-10 +5,355; "Loans repayable (one-time)" 23-09 -35,500 (row 20); "The Federal R&D tax credit" 25-07 +10,938, forecasts 26-02/26-05 +6,250 (row 21). Salary tab row 14 "MotMot + Blake LLC" 51,912, does not match SVB month by month.
- HG Costs row 37 "UA Assets": 24-05 125 (Oleg), 24-06 250, 24-10 5,125, 24-11 5,000, 24-12 6,429 (Node 16,428.57 sits here; 5,000+5,000+6,429 = 16,429).
- Meta receipts, Robert's box: 108 messages in 59 thread files, "Your meta ads receipt", $29,827.71 billed, 2024-01-27 to 2025-11-06, scan complete. Billed lines = campaign lines exactly. By campaign name: DD or pre-ZM (Node_, NM_DominoDelights, Android/iOS tests) $19,891.35 (2024-01-27 to 2025-05-03); ZM3D (PvZ_, ZM_, ZombieTest) $9,920.15 (2025-04-26 to 2025-11-06); Creative_AB_Test $16.21. Payment methods: MasterCard 4655 $2,295.96 (14), MasterCard token $25,993.24 (82), MasterCard 5348 $16.21, MasterCard token $1,511.98 (2), Advertising credit $10.32 (9).
- Unity Ads receipts, Robert's box: 7 ("Receipt from Unity Ads"): $1,000 each at 00002874 (2024-01-25), 00003209 (02-10), 00003348 (02-20), 00003439 (02-25), 00007783 (2024-10-09), 00014282 (2025-06-21 "Ads Prepayment" $1,000, Organization Harmony Games Inc.) + one more to read.
- Leonard own cards: EX 2025-07/1262 "I'm gonna use my own credit card"; EX 2025-08/9 "I also added $1K out of my own pocket as usual lol to Unity"; EX 2025-08/185 "added another $1K to Unity"; AD 2025-08/38 "I gotta stop paying Unity out of my own credit cards"; EX 2025-08/380 "this time I'm gonna add it via company credit card rather than my own"; AD 2023-09/303.
- CalmPlay Unity account: EX 2025-05/477 Frederick "another $1k on the CalmPlay Unity account for the next round of ZM UA. Note this is not our Harmony Games account"; EX 2025-03/703 "$1,673 in a Unity account that cannot be used for Domino Delights. Might as well use that for the CalmPlay version of ZM3D"; EX 2025-07/732 "They refused to refund our calm play money, or transfer it to HG"; EX 2025-07/1259 "these campaigns will run out of the Calm Play account".
- Adjoe = Domino Delights incentivized UA, iOS US: #adjoe C07UCC631A6 (YES) 2025-04/9-10 $15k test iOS US; 2025-04/105-106 "$10K spend", "commit to another $30K"; 2025-05/69 Leonard "spent $30K today to make $10K back"; IO EX 2024-10/3724 file "[completed] Harmony Games adjoe IO - Oct 2024". C09SWTHEMEW 2025-11/72 "We spent about $50K on Adjoe, drove about 10K installs in the US".
- Adjoe Sept 2025 dispute: C07UCC631A6 2025-09/4 Leonard "we will not accept billing for these installs"; 2025-09/5 adjoe "you will not be responsible"; 2025-10/0 adjoe "the invoice got sent out (automated system)... likely be a credit issued for the amount on the invoice". threads/00015531.json#0 (2025-10-05, Leonard to a publisher, Robert's box) "About $4K AppLovin spend is missing. The report also shows about $4K on Adjoe that was later credited back." Last Adjoe wire is 2025-08-29, so this credit offsets an unpaid invoice, not a Processed wire. NB-18 covers Sept 2025 adjoe credits: do not grade.
- Era: ZM3D prototype EX 2025-01/184 (2025-01-03), 2025-01/276, 2025-01/442 ("rest of the team works on the prototype for next 2 weeks"), #zombie-match3d C0880U9751A opened 2025-01-09 (2025-01/0). Name chosen EX 2025-03/304-344. Layoffs EX 2025-10/523, 2025-10/1716 (2025-10-24). CF: EX 2025-11/955 Arthur 2025-11-26 "Combo Fighter work started on Monday" (= 2025-11-24), EX 2025-11/630 2025-11-18 first mention in EX, EX 2025-11/972 Marcus VFX, EX 2025-11/979 Martin UI.
- Leapblock adjustments in #leapblock: 2024-01/11-12 Robert "deduct $300 for the book" / "yes its in the biggest invoice"; 2024-01/16 "saga map team and the animator's last week of December is off"; 2024-02/0, 2024-02/14-18 animator invoice mistake, "I offer to skip this month's invoice"; 2024-06/0-7 "May + first week of June" (last broader-team payment).
- Leapblock timeline in #leapblock: 2024-06/13 "no further payments for the broader saga map team"; 2024-06/14-16 [PERSON_NAME_0034] $3,500/month separate; 2024-09/5 new rates $4,400 and Martin $3,350; 2025-04/1 Martin $3,700; 2025-05/2 "[PERSON_NAME_0116]'s last pay check. His last day was April 16th so 4400/30*16 = $2346 ... invoice for Art direction for $2350" (so 2025-05-07 $6,050 = $3,700 + $2,350; 2025-05/9); 2025-12/8 euro switch; 2026-02/0 Leonard "last month's payment was our last payment"; 2026-02/4 "We paid him until end of January".
