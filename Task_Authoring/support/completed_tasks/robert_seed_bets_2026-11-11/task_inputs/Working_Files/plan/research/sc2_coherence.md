# SC2 coherence audit: storyline A "The seed, bet by bet" (normal, clock 2026-02-14 00:00 UTC)

Facts and locators only. No prompt, Oracle Event or rubric text. Written 2026-11-07.

**Locator key.** AD = #admin_foundersonly C04UEQVDVB7 · LB = #leapblock C05URGU759U · WD = #winddown C0ADGSZKR3R · EX = #executives C07C2866011 · FO = #founders C04UTBZL6AX · OV = #video_editing_oleg C06MXPL9536 · RM = Robert-Marcus DM D05UDNCCFEW · LR = Leonard-Robert DM D04UP2L3E3S · G:n = gmail threads/n.json · LEO:n = threads/leonard@harmonygames.co_n.json. Slack pointers are channel/ts. P&L = f_605121f4a36752645e0ac3.

**Reach.** `can-see robert`: AD, LB, WD, EX, OV, RM, LR, P&L = YES. LEO:1795505181532693167 and LEO:1798427314394417287 = NO. Leonard's and Arthur's mail was read evaluator-wide, for contradiction checks only.

**Checks I re-ran myself (not taken from the census).**
- Awaiting vs Processed, matched on suffix + amount: 1 orphan of 130, which is $33,290. Processed with no Awaiting in Robert's box: 3.
- Processed multiset across mailboxes: Robert 132 = Leonard 132 exactly. Arthur 65 is a subset. No Processed for $33,290 in any box.
- Western Union census: 68 thread files, exactly 5 MTCNs, and WU's own monthly summaries (3,225 / 2,150 / 2,150) sum to $7,525.
- "wire return" over all 88,728 gmail files, scan complete: exactly 2 return records, both in Leonard's box.
- HG Costs by position, and all 241 of Robert's SVB thread files checked for message order.

---

## Task 1. Coherence audit table

Disposition codes: **AVOID** · **FOLD** (into design) · **CLAIM** (designed claim + overturning record).

### Temporal

| # | Record | Fields | Evidence pointer | Hazard | Disposition |
|---|---|---|---|---|---|
| T1 | $4,032 to ***8605 | Analysis §5 says "Apr 3, 2024"; notice Transaction Date is **Apr 02 2024**, Delivery Apr 03, sent 2024-04-03T03:32Z | G:00004088#0; LEO:1795505181532693167 "Wire Date: 4/2/2024" | none | FOLD: use Apr 2 everywhere; the method fixes Transaction Date |
| T2 | 4 notices whose sent date (UTC) is a day after Transaction Date | sent vs Transaction Date | G:00004088#0, 00005609#0, 00006104#0, 00010556#0 | none | FOLD: never date from the Date header |
| T3 | 86 of 132 notices have Delivery ≠ Transaction Date | Transaction vs Delivery | svb_rows | none | FOLD: no boundary effect (T5), but the method must name Transaction Date |
| T4 | Leapblock in arrears: bank month ≠ P&L work month | wire date vs HG month | LB 1715666841.334859 "APRIL invoices"; Task 4 row 3 | none | FOLD: by-date rule, no work-month reading |
| T5 | Bet boundaries | ZM: spine 2025-01-10 vs #zombie-match3d first record 2025-01-09 13:11Z. CF: spine kick-off 2025-11-12 vs Arthur "Combo Fighter work started on Monday" = Nov 24 | timeline.md rows 2025-01-10, 2025-11-12; EX/1764171306.893909 (Nov 26) | none | FOLD. No wire falls Jan 3-14, 2025. Only AppLovin $4,144.22 falls Nov 12-23 (Nov 12, UA, out). The method still has to state one date per bet |
| T6 | Leapblock MSA vs first booked work | MSA effective Aug 7, 2023; HG Costs Saga Jul-23 12,000 and Salary tab Victor Jul-23 4,000 pre-date it | /docs_documents/123; P&L | none | AVOID: no run needs Jul-23 P&L cells |
| T7 | CORR seed vs Carta timing | Carta renewal Aug 15, 2024 on "Bank account ending in 3203"; wire Aug 19, four days **after** | LEO:1805941771379637048 (Leonard only); G:00006272 | none | FOLD: the seed may say replenished after the charge, never pre-funded |
| T8 | $125 sequence | Slack "I re-sent" 20:16Z **precedes** Processed 20:17:53Z and return 20:32:17Z, all May 7, 2024 | OV/1715113013.494939; G:00004648#0; LEO:1798427314394417287 | none | FOLD: see Task 3a |
| T9 | Seed windows | WD last record 2026-02-12 23:04Z; LB last 18:50Z; export ends Feb 13 10:03Z | NB-6; dump | none | FOLD: ask between Feb 12 23:05Z and Feb 13 10:03Z; statement after WD/1770922747.152399 |

### Semantic

| # | Record | Fields | Evidence pointer | Hazard | Disposition |
|---|---|---|---|---|---|
| S1 | "Payment Processed" on a returned wire | status label vs outcome | G:00004088#0 vs AD/1712331142.975829-1712331718.859679, AD/1712901800.684259 | none | CLAIM: Processed is overturned by the Apr 5 and Apr 12 founder records |
| S2 | Same defect on $125 | status label vs outcome | G:00004648#0 vs LEO:1798427314394417287 (Robert NO) | none | **Unresolved in the design, see Task 3a** |
| S3 | "Founders' pay out, Gusto" scope assumes only founders are off-notice | HG Costs rows 5-6 hourly devs | AD/1730393083.619159 "gusto is done (with [..]'s and [..]'s hours in)"; AD/1724352440.699199 "Deel for both of the new guys" | none | **FOLD, see Task 3b2**: route not closed |
| S4 | HG Salary row "MotMot + Blake LLC" mixes the contractor with Arthur's own company | row label | P&L HG Salary row 14; FO/2023-06 /1294 "Arthur Blake owns 100%" | none | AVOID: never cite this row as MotMot's identity proof |
| S5 | MotMot Technologies vs MotMot Studios | entity names | FO 2024-05 /1723 | none | FOLD: say MotMot Technologies only if a proof uses it; AD uses "MotMot" |
| S6 | "4 payments" vs one notice | Leonard's count vs a single Awaiting | AD/1694616691.082479; G:00001577#0; 4 PDFs at AD/1694616734.891689, two named invoice 33 with identical size 1,050,897 | none | FOLD: statement says one wire, no per-invoice split |
| S7 | Dated cost claims near the design's DD total | "so this game costs about $1M to make" (2024-09-05); "For art we spent over $250K alone for our first game" (2024-05-29) | AD/1725515162.252689; FO/1717020444.608159 | none | FOLD as decoys: the first is total cash used, not build cost. A correct run does not need them; a reviewer will see them on a "cost" search |
| S8 | Product names | Game of Dominoes / GoD / Domino Delights; Puzzles vs Zombies / ZM; Combo Clash vs Combo Fighter | MSA SOW; EX/1763001258.337789; trap K02 | none | FOLD: the method uses DD, ZM, Combo Fighter only |
| S9 | Greeting token = $500 payee token | `[PERSON_NAME_0054]` greets Robert and heads ***3139 | G:00013840; census D | none | FOLD: seeded note on that issue spells the helper, as §4 plans |
| S10 | Job titles | Robert "Chief Product Officer" in Contacts vs Creative Director persona | entity_robert.txt | S06 | AVOID: no title in any graded fact |
| S11 | "contractor" wording | PAYROLL_ROSTER full_time vs "only international contractors" | WD/1770675894.906889; NB-15 | S05 | FOLD: OFF rule must not rest on roster status |

### Cross-service referential

| # | Record | Fields | Evidence pointer | Hazard | Disposition |
|---|---|---|---|---|---|
| X1 | Return notices exist only in Leonard's box | Robert's mailbox has none | LEO:1795505181532693167, LEO:1798427314394417287; can-see NO | none | FOLD: Robert's proof for RET is AD only |
| X2 | Silje Molna (sheet) vs Lauren Brooks (contract, Slack, bank) | payee name | HG Costs row 7; EX 2025-10 /630 file "Consulting Agreement Lauren Brooks.pdf", permalink consulting_agreement_silje_molna.pdf | none | AVOID row 7. A real base name defect, not a designed alias |
| X3 | Slack Drive links never resolve by id | Leonard's invoice folder link | AD/1696031140.431969 | R04 | AVOID |
| X4 | Invoice PDFs not readable through hg.py | Sep 2023 amounts | Drive `Invoices/Leapblock/0000000029…33` | none | FOLD: statement states only the $33,290 that the notice shows |
| X5 | $33,290 Awaiting sits only in Robert's box | Leonard and Arthur have no copy | re-run multiset | none | FOLD: fine, he is an approver; not a conflict |
| X6 | ***3203 holder | Census D said unknown. Now tied: Carta "Bank account ending in 3203" + "tied to our Chase account" | LEO:1805941771379637048, LEO:1837797395593354171; WD/2026-02 /183; WD/2026-02 /187 canvas | none | FOLD: base **supports** the CORR seed. Only the WD half is Robert-readable |
| X7 | Leapblock contact identity | Slack id is a token; Contacts "scott", Art Studio Principal (Contract Vendor); MSA notice mail scott@…; Slack name token [PERSON_NAME_0083] | entity_resolve; /docs_documents/123 | none | FOLD: statement must name Leapblock in its text |
| X8 | Node Dec $5,000 | Mail covers Sept-Nov = $11,428.57; wire $16,428.57; "3+ months payment"; no Dec invoice record | G:00008689#0; AD/1735854852.066529 | none | FOLD: the mail explains $11,428.57, not all of it. Node's bucket does not need the Dec fact |
| X9 | Martin's USD | 1,999.00 BGN; Equipment Oct-25 = 1,209.89, confirmed positionally (column Oct-25, sole cell that month) | G:00015809#2; HG Costs row 62 | none | FOLD: month match is now positional; link to the laptop stays inferred |

### Quantitative

| # | Record | Fields | Evidence pointer | Hazard | Disposition |
|---|---|---|---|---|---|
| Q1 | Ledger vs bank vendors | see Task 4 rows 1-2 | FINANCE_LEDGER | Q05 | AVOID: no ledger read on the path |
| Q2 | MotMot: P&L 51,912 vs bank net 37,056 | see Task 4 row 4 | HG Salary row 14 | none | AVOID |
| Q3 | Leapblock lines vs wires | 14 work months tie exactly, the rest do not | Task 4 row 3 | none | AVOID |
| Q4 | Creative X 3,750 vs 3,500 | Task 4 row 5 | G:00013667; HG Costs row 37 Apr-25 | none | AVOID sheet |
| Q5 | Revenue basis | 12,354.99 gross vs P&L cash 9,859.36 to Dec-25 vs ledger 9,693.55 | census C | Q09 | FOLD: method names REVENUE_DAILY total only |
| Q6 | TYZ | wire 7,500 vs invoice 12,240; P&L 24-02 -7,500, 24-03 -13,002 | G:00002505, G:00003549#0 | none | FOLD: company line at bank amount; never state "patent cost" |
| Q7 | Analysis total | Census C's 1,669,393.32 adds BGN as USD; 1,667,394.32 + 1,999 BGN is right | census D §0 | none | FOLD |
| Q8 | Deel Sep 27, 2024 | 50,244.96 vs "43K" | AD/1727451647.872599 | none | No defect: 50,244.96 - 7,583 = 42,661.96 |
| Q9 | BANCO Jul pair | P&L has one 2,688 and Aug-24 = 0; bank has two | AD/1721407009.185549 "for June"; AD/1722277723.552349 | none | Fair control. Two real payments; P&L row short by 2,688 |
| Q10 | Lucas | 6,450 + 7,525 = 13,975 = HG Costs row 4 | census; WU summaries | none | No defect |
| Q11 | Sep 2023 burn | MONTHLY_BURN 99,107 vs ledger 134,607; the gap is 35,500, the founder loan, **not** 33,290 | coherence_hazards Q05 | Q05 | AVOID: same month as ORPH, an easy false link |

### State / lifecycle

| # | Record | Fields | Evidence pointer | Hazard | Disposition |
|---|---|---|---|---|---|
| L1 | $33,290 | Awaiting, Arthur "Done!", no Processed; Arthur had an open approval fault five days earlier | G:00001577#0; AD/1694616951.239909; AD/1694203166.604079 "that stupid approval problem"; Recipient Created G:00001576 same day | none | CLAIM: NEW statement overturns the silence. Base supports it: no chasing in LB Oct 2023 |
| L2 | ***8605 lifecycle | Created Apr 2 (Arthur), return mail Apr 5 14:26Z, Modified 15:40:27Z, "resubmitted" 15:41Z, Processed 16:02:49Z | G:00004078, G:00004120, G:00004124 | none | Coherent. No defect |
| L3 | Leapblock end | "last month's payment was our last payment" vs Feb 2 wire | LB/1770832312.713589; G:00016690#2 | none | Coherent |
| L4 | Chase | closed Oct 31, 2025, cashier's check into SVB; Carta still tied | AD/1761954952.006759; WD/2026-02 /183 | none | Coherent; supports an internal-transfer reading |
| L5 | Feb 1-12 Martin cost | Leapblock paid him and let him go; ~$600 optional gesture, unpaid | WD/1770922666.421089 to /1770922747.152399 | none | FOLD: statement closes with no balance claimed and must not count $600 |
| L6 | Lauren Brooks | last Slack 2026-01-06, same day as her last wire | activity; G:00016300#0 | none | Coherent |

### Identifier / format

| # | Record | Fields | Evidence pointer | Hazard | Disposition |
|---|---|---|---|---|---|
| F1 | Payment Reference | four shapes: yyyymmddL1B77D1C… 44, yyyy+day-of-year… 33, UUID 53, none 2 (both Singular) | svb_processed_robert.json | none | No defect. Checked: 20240930265900 = 2024 day 093 = Apr 2 |
| F2 | From line | "Harmony Games GAMES INC." 122, "Harmony Games Inc." 10; copies differ by token across mailboxes | svb_rows | Q10, trap X04 | FOLD: quote-free, Robert's copy only |
| F3 | Mixed mailboxes in `threads/0*` | 00000394 is SVC_0019, 00004614 is Robert's, same mail | ids | I05 | FOLD: check the id prefix |
| F4 | Date formats | ISO-Z vs RFC-2822 | I04 sample LEO:1798427314394417287 "-0600 (MDT)" | I04 | FOLD |
| F5 | Linear user ids | `usr_Robert`, `usr_EMPLOYEE_0024` not usr_<16hex> | entity output | I10 | FOLD: quote exactly |

### Other

| # | Record | Fields | Evidence pointer | Hazard | Disposition |
|---|---|---|---|---|---|
| O1 | Facts locked in images or PDFs | AD/1712901773.229139 image before the return note; AD/1694616672.499829 image; Leapblock invoices | files arrays | none | FOLD: no fact may need them |
| O2 | DM member lists | reach argued from lists | NB-31 | none | FOLD: use persona_view verdicts |

---

## Task 2. Coherence hazards

| KB category | Ids touched | Why / how kept clean |
|---|---|---|
| temporal | **T06** (only if a Trello card is seeded) | T02 checked: 0 of 241 SVB thread files out of order, so not touched. T03, T04, T05, T07, T08 not in scope |
| semantic_category | **S05, S06** | Roster status and titles stay off every graded fact. S03 if Linear labels are seeded: define them. S07 (doc f_0c37…) stays unopened |
| cross_service_referential | **R04, R08** | see resolutions below |
| quantitative | **Q04, Q05, Q06, Q07, Q09, Q10** | Q04: new Slack replies count from replies, parents here have counters at 0 (WD/1770934638.035469 reply_count 0). Q05, Q06, Q07: keep ledger, cash and vendor-quote fields off. Q09: count 0, revenue mirrors agree, nothing seeded to Snowflake. Q10: Robert's copy only |
| state_lifecycle | **L08, L13** | see resolutions below. L01-L07 not touched: no base Linear issue is modified |
| identifier_format | **I01, I03, I04, I05, I06, I10, I14, I15, I17, I18** | I01 collision-check (channel, ts). I06 seeded replies carry in_reply_to + references. I14: P&L and MSA are Resource-owned but shared with Robert, readable. I17 if Trello. I18: the AD example 1698436632.335299 strikes a reimbursement line, not a wire |

**L/R resolutions.**

| Hazard | Resolution | Basis |
|---|---|---|
| R04 | `excluded` | No Slack Drive link is cited; files are named by title |
| R08 | `excluded` | No invitation mail is relied on. A seeded meeting needs no invite (INT-11) |
| L08 | `excluded` | No base open issue is modified or cited. Seeded payee issues go to active people only |
| L13 | `excluded` | The design never asserts that work stopped at the shutdown |

No hazard qualifies for `repaired` (Linear L01-L07 only) and none needs `dated_claim`: the designed disagreements (S1, L1) are not KB hazards.

---

## Task 3. Sibling-defect sweep

### 3a. Processed notice for a returned wire

| Item | Finding | Verdict |
|---|---|---|
| $4,032 ***8605 | The designed RET defect | Fair, designed |
| **$125 ***9368 Oleg, May 7, 2024** | **Second case.** Recipient Created G:00004628 May 6 23:00Z · Scheduled G:00004629 · Processed G:00004648 20:17:53Z · SVB "Wire Returned" LEO:1798427314394417287 20:32:17Z "ACCOUNT NOT ELIGIBLE FOR WIRE TRANSFERS", case 390393. Re-sent another way: OV/1715113013.494939 "I re-sent the wire this time with payoneer's traditional methods"; OV/1715163809.708419 "Yes, I receive this email" | **Not a data defect (Processed then Returned is ordinary) but a design defect.** The analysis calls RET's kind unique, and the "stayed out" clause applied to all 22 payees gives Oleg's only notice $0 while he was paid $125. Robert cannot see the return mail |
| Others | "wire return" full scan: 2 records. Slack census: no third | Closed |

Oleg's lifetime is also not $125. HG Costs UA Assets shows May-24 125, Jun-24 250, Oct-24 125 inside 5,125 (the split from Node's 5,000 is inferred); census D gives $500 for four videos. Robert's mail holds two Payoneer requests of $125 (G:00004614, G:00007150). AD/1727899814.819219 "we need to pay him and I don't remember our payoneer credentials" (Oct 2024, identity inferred). Any graded Oleg dollar figure is contestable. Options: take Oleg's amount off graded rows and keep only the bucket, or give the row an incorporated rule.

### 3b. Payment outside the Processed set (the OFF and ORPH kind)

**3b1. Awaiting or Scheduled with no Processed.** Only $33,290. 0 Scheduled orphans. Fair, designed.

**Processed with no Awaiting in Robert's box.** $125 and Lucas $2,150 x 2. Lucas's two: Robert initiated them (AD 2024-10 "I initiated a payment for Lucas"), and the Awaiting copies sit in Leonard's and Arthur's boxes (verified). Fair.

**3b2. Contractors paid off the notices. The analysis calls Lucas "a contractor Robert paid himself". He is not the only one.**

| Route | Who | Amount and record | Game | Reach | Verdict |
|---|---|---|---|---|---|
| Western Union | Lucas | $7,525, closed census | DD | YES | Fair, designed |
| **Upwork, Robert released payment** | ZM 2D animators | RM/1752481205.011839 Robert "K payment released"; RM/1753283145.037509 "approve so I can just send payment?"; RM/1750754723.620479 "each zombies one by one"; G:00014303 job post. Amount only as HG Costs "3D Animator" Jun-25 600 + Jul-25 4,800 (match inferred). No Upwork receipt in his mail | ZM | YES | **Fair item the rule must close.** It is the same behaviour as OFF, on a graded weight-5 total |
| Payoneer | Oleg | see 3a | UA | YES | Closed by the bucket only |
| Hourly, Gusto or Deel | HG Costs rows 5-6 "Mini Game Unity Developer" 11,361.10, "Temp Game Unity Developer" 23,336.20, sitting next to Lucas's row | AD/1724804799.197539; AD/1730393083.619159; AD/1724352440.699199 | DD (mini games lead) | YES | **Route unresolved.** If Gusto, $34,697.30 of build cost sits outside "team on Deel" |
| Unknown | "MotMot + Blake LLC" Apr-Jul 2025 6,000 x 3 + 3,000 = $21,000, no BANCO wire after Feb 27, 2025 | HG Salary row 14 | era ZM | YES | Route unknown; base has no record of it. Blake LLC is Arthur's company |
| Card | Unity Assets (Zombie Match) 946.80, 12 order mails | HG Costs row 15 | ZM | YES | Vendor, not a contractor, but names the game outright |

**Consequence.** "Contractors paid another way" (§4 fork 3) is an open set. A rule that closes on the WU route or on receipts in Robert's mailbox admits exactly Lucas. A rule that closes on "contractor paid off-bank" pulls in Upwork and possibly $34.7K with no receipt. A cold reviewer will find the Upwork thread: Robert is on it.

### 3c. One payee under two names

| Names | Kind | Verdict |
|---|---|---|
| Deel / [ORG_NAME_0057] (8380); Singular / [SOURCE_ORG_0351] (4015); AppLovin / [SOURCE_ORG_0651], [ORG_NAME_6051] (2532); [PERSON_NAME_7200] / [ORG_NAME_3801] (7393); Eveline / [PERSON_NAME_8401] (8501); JPMorgan / [ORG_NAME_2452] (3203) | Redaction, same suffix | Fair, NB-12 pattern; suffix proves it |
| BANCO DE AMERICA (3341, 8605) / MotMot; PERSON_4419 LLC / Node Media; [PERSON_NAME_36400] / Lucas / PERSON_R001; Private Entrepreneur … / Oleg / Dixelar; PERSON_6074 / Ozhan; M … / JP | Real alias | Fair |
| **Lauren Brooks / Silje Molna / [PERSON_NAME_0133]** | **Base de-identification slip**: two human names for one person | **Coherence defect.** Keep HG Costs row 7 off the path |
| Eveline / Marcus Bennett | Real | Fair; Robert-side proof is AD only |
| Brooks: Lauren vs Oliver Brooks | Lookalike, trap P02 | Fair trap on "[PERSON_NAME_7249] Brooks" |

---

## Task 4. Bank vs ledger, P&L, decks

| # | Bank says | Other side says | How a correct run stays off |
|---|---|---|---|
| 1 | Leapblock LTD 29 wires $374,654.00 | FINANCE_LEDGER `art_outsourcing` -86,000, "External art studio" | Snowflake read limited to REVENUE_DAILY |
| 2 | Deel 35 wires $1,015,347.19 | `operations` -672,374.58, "Unreconciled operating expenses"; `salaries` -1,932,761.23 | Same |
| 3 | Wires, by month paid | HG lines by work month. Saga + Victor + Martin + Animator tie exactly for Oct-23, Dec-23, Apr-24, May-24, Jul-24 to Mar-25 (Sep-23 ties with Aug's 260). Off: Nov-23 25,600 vs 24,318; Jan-24 25,100 vs 23,190; Feb-24 25,100 vs 29,243; Mar-24 25,100 vs 31,100; Jun-24 10,950 vs 10,925; Apr-25 5,850 vs 6,050. Jul+Aug-23 = 35,000 vs $33,290 | No run totals P&L rows. Note the sheet books the Jul-Aug 2023 work and nothing but $33,290 could have paid it, which supports ORPH but differs by $1,710 |
| 4 | BANCO net $37,056; last wire Feb 27, 2025 | HG Salary "MotMot + Blake LLC" 51,912: Jan-Mar 25 1,824 each vs wires 4,032, 4,896; Apr-Jul 25 21,000 with no wire | Never use this row |
| 5 | CREATIVE X "3,750.00 USD" | HG UA Assets Apr-25 3,500; EX "we did it for $3750" (census) agrees with the bank | Slack proof only |
| 6 | "[PERSON_NAME_7249] Brooks" 500 x 3, last Jan 6, 2026 | "Silje Molna" Oct, Nov, Dec-25 500; BoD Oct 14 p9 "No fixed fee or salary" (census) vs contract $500 minimum | Row and deck stay off; contract and EX carry OVR |
| 7 | "1,999.00 BGN" | Equipment Oct-25 1,209.89 | Stated company-line rule; do not grade a USD conversion without a seed |
| 8 | TYZ 7,500 | Invoice 12,240; P&L -7,500, -13,002 | Bank amount, company line |
| 9 | None | Revenue: REVENUE_DAILY 12,354.99 vs P&L "Mobile revenue (cash in)" 9,859.36 vs ledger 9,693.55 | Method names the table |
| 10 | DD by date $984,888.21 | Leonard "so this game costs about $1M to make" (2024-09-05); Internal BoD Jul 2025 p21 "$1.5M dev + $0.5M UA" (census, plan) | Dated human remarks; not the method's basis |
| 11 | All | Leonard "The P&L forecast, including starting and ending balances, as well as the latest figures, are accurate" (AD/1754445622.992119) | **This is the one a reviewer will quote against the bank.** It speaks to balances vs QuickBooks, not per-payee detail |

**Is a seeded source statement needed? Yes.** No base record declares the bank the source for per-payee cost.
- Base gives only support: "after all quickbooks is just pulling data from SVB" (AD/1728847327.191969) and "QuickBooks only considers actual payout dates" (AD/1700232359.999729).
- **The planned reason is false as written.** §4 item 1 says "the books have no vendor names". That holds for FINANCE_LEDGER only. The Robert-readable P&L names payees: PERSON_R001, Silje Molna, Solsten, Figma, MotMot + Blake LLC, Victor Barnes, Marcus Bennett. A cold reviewer will fail that sentence.
- A true reason: the notices are the only record with one row per payment and payee; the sheet is by month and line. It must not call the P&L wrong (row 11).
- The clause must also explain why a non-bank source (Western Union) enters a bank-sourced total.

---

## Task 5. Active speakers

| Person | Email / Slack | status_at_clock | Seeding role |
|---|---|---|---|
| Leonard Hayes | leonard.hayes@ / EMPLOYEE_0038 | active_feb_2026 (Slack 2026-02-13) | Ask, method. Safe before Feb 13 10:03Z |
| Arthur Blake | arthur.blake@ / EMPLOYEE_0025 | active_feb_2026 (Slack 02-12, mail 02-04 sent) | CORR mail. Safe. Not a member of LB under EMPLOYEE_0025 |
| Robert | robert@ / EMPLOYEE_0016 | active_feb_2026 | Persona |
| Marcus Bennett | marcus.bennett@ / EMPLOYEE_0002 | active_feb_2026 | NB-1: no channel post after Feb 11 20:40Z. Do not seed |
| Martin Walsh | martin.walsh@ / EMPLOYEE_0033 | active_feb_2026 | NB-1, let go Feb 12. Do not seed |
| Oliver Brooks | oliver.brooks@ / EMPLOYEE_0003 | active_feb_2026 | NB-1. Do not seed |
| Lauren Brooks | lauren@ / EMPLOYEE_0035 | active_jan_2026_quiet_in_feb | No seeded voice |
| Graham Porter | none | `no exact match` in entity.py | Bank payee only; never create an account |
| EMPLOYEE_0024 | employee_0024@ ≠ joined; slack_only_ids | email entity quiet_since_2024-01 (gcal/linear). **Slack id last post 2026-02-12T18:50:09Z, 5 messages in Feb** | Leapblock statement |

**Who EMPLOYEE_0024 is.** Slack id is unjoined (`token_link` UNRESOLVED). Contacts: "scott", Art Studio Principal (Contract Vendor). Slack name token [PERSON_NAME_0083] (LB/1770922108.887399 "Hi [PERSON_NAME_0083]"; WD/1770922647.735569 "talked to [PERSON_NAME_0083]"). MSA notice mail includes scott@harmonygames.co. The KB's quiet status is the email entity; the Slack record is live.

**Seeded post Feb 12-13 before 10:03Z: safe, with limits.**
- Member of C05URGU759U. Members: Robert, EMPLOYEE_0024, Victor Barnes (EMPLOYEE_0030), Leonard, PERSON_6089, U04TWDMDT0V, U04UP2L1RUY, U05LP9W2RSR.
- Not on NB-1's list. He left #engineering-bots on Feb 11 (ts 1770842236.455329), yet posted in LB at 20:47Z Feb 11 and 18:48-18:50Z Feb 12, after the 20:40Z cut. Only his LB posts are proven.
- Habit: peak 06-09Z, Friday normal. Feb 13 07:00-10:00Z fits.
- Must fall after WD/1770922747.152399 and fit it: "[PERSON_NAME_0083] said don't worry".
- His display name is the bare token, so the text must say it is from Leapblock. Victor stays silent.

Verbatim outputs: `/private/tmp/claude-501/-Users-sumit-Source-OC/291ff662-f24b-4f22-9fb7-b1cecbd8895a/scratchpad/sc2/entity_collisions.txt` and `/private/tmp/claude-501/-Users-sumit-Source-OC/291ff662-f24b-4f22-9fb7-b1cecbd8895a/scratchpad/sc2/entity_resolve.txt`.

---

## Task 6. Known-issue cards

| Card | Touch | Disposition |
|---|---|---|
| NB-1 | Seeded Slack after Feb 11 20:40Z | Founders and EMPLOYEE_0024 only |
| NB-2 | HG Costs rows on the OFF cross-check and Martin's USD | Keep cost lines off graded rows. Equipment is not a named line, but it is the same sheet |
| NB-3, NB-10 | Cash | Off path |
| NB-4 | Feb 2, 2026 wires | Bar is on FINANCE_LEDGER; Processed notices are the safer source. Keep ledger off |
| NB-5, NB-8 | Helpshift in WD and EX | Off path |
| NB-6 | Seeds | Before Feb 13 10:03Z |
| NB-9, NB-7 | CF | No Android or level facts |
| NB-11 | CF GDD | Off path |
| NB-12 | Node, Deel, Singular, Lucas, JPMorgan tokens | Each needs a spelled record: AD/1735854841.070019 spells Node Media LLC; suffix for the rest; seeds spell where only a token exists |
| NB-15 | "contractor" wording | No roster reliance |
| NB-17, NB-18, NB-19, NB-28 | UA facts | UA scoped out |
| NB-20, NB-33 | Board, DAU | Off path |
| NB-22 | Letter 00016874 | Off path |
| NB-23 | Singular INVSINC22671 | Bank amounts only, company line |
| NB-24 | Linear comments | Only seeded comments exist; never imply base ones |
| NB-25 | DD store history | Off path |
| **NB-26** | **CF revenue $11.75 is all ads; Robert said "2 people bought rotation pack"** | **Keep only the REVENUE_DAILY total, stated as warehouse-recorded. Never grade an IAP split or "no sales"** |
| NB-29 | Shutdown date | Not a window boundary here |
| NB-31 | DMs | Reach by persona_view |
| NB-32 | Douglas | By-date rule, no end date |

**Does a card bar a channel?** None bars one outright.

| Channel | Constraint |
|---|---|
| RET | NB-12 lightly: Apr 12 names a token. Apr 5 "motmot" removes the problem |
| OFF | NB-2 on the P&L tie, NB-15 on wording |
| ORPH | NB-1 and NB-6, both satisfied by EMPLOYEE_0024 before 10:03Z |
| CORR | NB-12: seed spells Chase |
| ALIAS | NB-12: Node needs AD/1735854841.070019 + amounts |
| OVR | none |
| CURR | NB-2 if a USD figure is graded |

---

## Task 7. KB citations

**Timeline spine.** Prelude (2023 seed close); 2025-01-10 ZM development; 2025-03-21 Puzzles vs Zombies builds; 2025-04-15 Victor quiet; 2025-10-10 Telegram DD; 2025-10-24 layoffs; 2025-11-12 CF kick-off (#prototype Nov 24); 2026-02-09 wind-down; 2026-02-09 vendor terminations; 2026-02-11 contractor letters; 2026-02-12 agreements; 2026-02-13 work continues. Beats: 2024-04-25 Leapblock wind-down, keeping Martin; 2024-10-01 Deel scale-up; 2025-10-24 Telegram master ticket. The spine starts 2024, so Sep 2023 and Apr 2024 facts have no spine row.

**Cohort.** `cohorts.json: no fit — no cohort covers bank notices or payees; nearest SF-LEDGER (704 rows, hazards_inside Q05) has no vendor names and one query returns it; the 132 notices collapse in batch reads; 22 payees is under the 40 floor, so cohort_exception is needed.`

**Trap precedent.** C02 (parent says done, later fails: Arthur "Done!", Processed), C01 (correction in a later message), C04 (human claim vs record), D04, D08 (P&L versions), X03 (HG Costs redacted lines), X04 (masked company name), X02 (EMPLOYEE tokens), B02 (SVB sender), P01, P02, P03 (Marcus, Martin, Brooks), K02 (product names).

**Integrations.**

| Service | INT | Decision |
|---|---|---|
| slack | INT-22 | Optional mail, never load-bearing. No seeded bot posts |
| gmail | INT-22, INT-11, INT-05 | Founder mail needs none; seeded replies need headers (I06) |
| gcal | INT-11 | One copy per attendee calendar; invite mail optional |
| linear | INT-04, INT-05 | Notices optional; if seeded they must match the issue. INT-03 n/a, no PR |
| gdocs, gdrive, gsheets, gslides | INT-13 | DM-only, optional. Drive rows and sharing mirrored per S8 |
| contacts | no INT | None mirrors contacts |
| trello | INT-21 | No Trello bot exists; bump dateLastActivity (T06) |

---

## Corrections for the analysis

1. RET date Apr 2, not Apr 3.
2. RET placement: "names neither BANCO nor MotMot" misses AD Apr 5, 2024. A "motmot" search returns "thats the motmot one?" next to "This wire didn't go through" and "I messed up the bank account number". The 0.45 landing prior is likely too high: more runs will catch this than §5 assumes, so re-forecast RET.
3. ALIAS: AD/1736978214.260099 ties MotMot to the Jan 21, 2025 $4,032, not the returned one.
4. "Wire that came back" and "contractor Robert paid himself" are not unique (Task 3).
5. Census D: JPMorgan holder is now established as the Chase account Carta debits.
