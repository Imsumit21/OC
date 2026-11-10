# SC1 truth table: per-payee truth under the planned method (storyline A)

Universe Normal, clock 2026-02-14 00:00 UTC, persona Robert. Facts and locators only. No prompt, OE or rubric text.

Pointer forms follow census D: AD = C04UEQVDVB7, FO = C04UTBZL6AX, EX = C07C2866011, LB = C05URGU759U, ART = C08FG9924R2, WD = C0ADGSZKR3R, `AD 2024-04/71` = messages/C04UEQVDVB7/2024-04.json idx 71. `G:00004088#0` = gmail threads/00004088.json message 0.

## Task 1. Off-bank census

**Scope.** Gmail: all 21,192 `threads/0*.json` (holds every Robert thread; Robert's mail is numeric files only; other boxes are `threads/<user>@..._<id>.json`, 88,726 thread files in all), complete scans on `subject`/`body` for: western union, westernunion, money transfer, transfer, wise.com, transferwise, remitly, moneygram, worldremit, xoom, zelle, venmo, cash app, usdt, usdc, bitcoin, crypto, paypal, payoneer, revolut, company card, via card, paid him/her/them, upwork, fiverr, toptal. `usdt` body scan was capped (substring noise) and is not a clean negative; no crypto payment appeared anywhere else. Slack: all 5,353 message files, complete for western union, transferwise, wise.com, via wise, on wise, paypal, payoneer, remitly, revolut, moneygram, xoom, zelle, venmo, usdt, usdc, company card, company credit card, via card, by card, paid him/her/them, I paid, deel direct, direct payment, sending it, my own pocket, my card, out of pocket, upwork, fiverr, freelanc. `rigging` and `animator` were capped, so those were re-done by channel-month.

**Are Lucas's five receipts the complete set? For Western Union, yes. For "contractors paid another way", no.**
- Western Union: every transactional WU mail in the universe is in Robert's box. Five "ready for pickup" receipts plus five matching "been received": 00005184/00005198 (2024-06-03, $1,075, fee 0), 00005350/00005351 (06-17, $1,075, fee 0.99), 00005489/00005490 (06-29, $1,075, 0.99), 00005962/00005963 (07-23, $2,150, 0.99), 00006329/00006330 (08-23, $2,150, 0.99). Total received $7,525.00; fees $3.96.
- WU's own monthly summaries close the set: G:00005579 June 2024 "Total amount sent: 3225.00 USD", 3 transfers; G:00006117 July 2150.00; G:00006592 August 2150.00, 1 transfer. No summary or receipt after that. The "didn't finish your transfer" mails (00005182, 00005352, 00005491, 00005964, 00006331) are marketing nudges, always about an hour after a completed send, not separate attempts.
- First transfer is Jun 3, 2024, not May. HG Costs books it in May-24 (row 4: 24-05 1,075, then 2,150 x 6 = 13,975). `build_sketch.py` T_OFF says "May-Aug 2024": the receipts are Jun 3 to Aug 23.
- Route proof, Robert-readable: AD 2024-05/133 Robert "I will attempt to create Western Union using our debit card", /136 "using Harmony Games"; AD 2024-06/113-114 "I've been sending it" "via company card"; FO 2024-06/248-249 "$1075 half a month" "$2150 a month"; D04UP2L3E3S 2024-10/132-134 Leonard in QuickBooks "WU is Western Union, right?" "this looks like Lucas's fees". G:00005350#1 Robert forwards a receipt to lucas@ "Invoice paid". Lucas switches to IBAN: D07G4LK8DV0 2024-10/610-611.
- No Lucas payment after Nov 2024: HG Costs row 4 ends 24-11; Lucas DM last pay talk 2024-11/105-106. AD 2024-10/119 "extended until Dec" and calendar "PAY DAY FOR Lucas" Dec 26 (G:00010101) exist, but no record of a December payment.

| # | Who | Route | Amount | Work | Robert-readable proof | Status under "contractors paid another way count when a record shows the payment" |
|---|---|---|---|---|---|---|
| O1 | Lucas | WU on company card | $7,525 | DD mini games | Above | Intended |
| **O2** | **Unnamed 3D animator, 9 characters** | **"it's on credit card"** | **$5,400 agreed; $600 "ish" paid by 2025-07-07; HG Costs row 2 shows 25-06 600, 25-07 4,800** | **ZM monsters** | D04UP2L3E3S 2025-07/656 Leonard "how much are we gonna pay to the animator?", /658 Robert "$5400 for 9 characters", /662 "We paid little, $600 ish so far", /663 "it's on credit card"; EX 2025-06/552 Robert "finding Marcus some contractor to help him animate/rig the monsters"; AD 2025-07/20 | **NEW. Same pattern as Lucas, in ZM. Counts on the plain sentence. Not in the sketch.** No name, no receipt, no record that the last $4,800 was paid other than the sheet row. Moves ZM by up to $5,400 |
| **O3** | **Two hourly Unity devs on Gusto: [PERSON_NAME_0063] (PERSON_3060) and [PERSON_NAME_61253] / Kam (PERSON_3233)** | **Gusto** | **HG Costs row 5 $11,361.10 (24-06 to 25-03); row 6 $23,336.20 (24-07 to 24-11). $34,697.30** | **DD: "Mini Game Unity Developer", "Temp Game Unity Developer"; AD 2024-07/69 "Plinko and UI bug fix"** | AD 2024-06/83 "Set him up in gusto"; 2024-07/117 "gusto, including [0063] and [0077] done"; 2024-08/134, 152; 2024-09/87 "2 part-time, temp, seasonal"; 2024-09/150; 2024-10/227 | **NEW. PERSON_3060 = [0063] by G:00004692#7; PERSON_3233 = [61253]/Kam is inferred from dates and AD 2024-07/42. They built a game and were paid another way. The planned sentence "founders' pay is out (Gusto)" does not cover them. Deel wires exclude them: wires track the Deel people on the salary tab within a few hundred dollars while these rows are unmatched (24-07 wire 29,202.96 vs tab 28,523)** |
| O4 | Oleg (Dixelar) | Payoneer ACH debit | $126.25 May 7, 2024; $126.25 Oct 4, 2024 (= $125 + 1%) | UA videos, trailer | Requests only: G:00004614, G:00007150; C06MXPL9536 2024-05/40-41; AD 2024-10/0-39. Receipts are Leonard's only (`leonard@..._1798426229536387534`, `_1812016089445671988`, can-see NO) | UA bucket, no build effect |
| O5 | Oleg | Upwork, Robert's card | "$150 total" / "~$160 including fees" Jan 2024 | 2 UA videos | D056Y4K3H7Z 2024-01/223; FO 2024-01/1620-1630, 1755; AD 2024-04/179 | UA bucket, no build effect |
| O6 | Victor, before SVB | Deel, funded from Chase | $4,000 (May 24 and Jul 5, 2023) | Saga map start | D04UP2L3E3S 2023-09/224; AD 2023-08/12, 772, 819 | Pre-notice. Counts on the plain sentence unless bounded |
| O7 | UX contractor, first half | Deel, funded from Chase | $600, May 2023 | UX milestone | AD 2023-05/360, 865-874 | Pre-notice. Doubles his line to $1,200 unless bounded |
| O8 | Deel runs Apr-Aug 2023 | Chase | Amounts only in images; salary tab Deel people 23-07 $12,000, 23-08 $13,500 | Team | AD 2023-08/982-983 "With Deel we only had 1 transfer per month from Chase" | Pre-notice. No readable amount |
| O9 | Part-time artist, 2023 | Leonard's own money, $15/hour | Not stated | Art | AD 2023-05/70, 107, 140 | Pre-company |
| O10 | SFX freelancer, Georgia | Not stated | "$8/hr", "paid him $40" | Sound for MVP | C461E67A0163 2023-10/0-9 (Robert) | $40; a record shows it |
| O11 | Seller of Match-3D source | PayPal, Arthur | No amount | ZM prototype purchase | C03AEB306685 2025-01/14-21 | Purchase, not a contractor; no figure |

**Rails with nothing:** Wise/TransferWise appear only as Mar-Apr 2023 chatter (AD 2023-03/72-97, 2023-04/81, 1111-1113). Gmail wise.com hits are getclockwise/tellwise links. Remitly 0, MoneyGram 0, Revolut only VC newsletters, Zelle and Venmo no contractor use, crypto no payment (EX 2025-10/612 is a planned raffle), Deel direct 0 (after Sep 2023 Deel is wire-funded: AD 2023-09/67, 436). Fiverr 0 payments.

**Lead, unproven.** HG Salary tab row 14 "MotMot + Blake LLC" shows $6,000 for Apr-Jun 2025 and $3,000 Jul 2025 ($21,000) with no BANCO wire after 2025-02-27 and no room in Deel wires. Row 14 also misses the 2025 wires in timing. Treat it as a sheet row, not a payment (NB-2 family). EX 2025-05/241-243 is a separate proposed deal.

## Task 2. Second-return census

**Scope.** All 88,726 thread files, every mailbox: subject "wire return" (2 hits), body "has been returned by the beneficiary" (1), "wire transfer detailed below has been returned" (1), "Returned Reason" (1), "Return Reason" (1). Complete. Plus Robert's numeric files: subject return, fail, rejected, reversal, recall, payment cancel, wire; body wire return, returned wire, was returned, funds returned, ACH return. Slack: AD, FO, EX, D04UP2L3E3S, D04V95AAAHW, LB, each complete for wire, fail, reject, sent back, bounce, refund, not eligible, credited, wrong account (closes census D's gap on FO and EX "wire").

**Result: exactly two bank returns exist in the universe, both notices in Leonard's box only. Robert has neither notice.**

| # | Wire | Bank's return record | can-see robert | What Robert can read |
|---|---|---|---|---|
| R1 | BANCO ***8605 $4,032, Processed G:00004088#0, notice Transaction Date Apr 2, 2024 in parsed JSON | `threads/leonard@harmonygames.co_1795505181532693167.json`, Apr 5, 2024, case 386307: "Returned Amount: 4,032 USD", "Return Reason: BENEFICIARY ACCOUNT INVALID", "The returned funds will be credited to your account today" | NO | AD 2024-04/19-22 Leonard "This wire didn't go through", Arthur "thats the motmot one?", "I think I messed up the bank account number. Fixed up and resubmitted the payment."; AD 2024-04/71 Leonard "this is money returned to us because Blake put the wrong account number..."; /77-100 book categories; G:00004120 Recipient Modified; G:00004124 re-paid. Note: AD 2024-04/19-21 is an earlier and plainer Robert-readable anchor than the Apr 12 note, and it names MotMot |
| **R2** | **Oleg ***9368 $125, Processed G:00004648#0, May 7, 2024 20:17 UTC** | `threads/leonard@harmonygames.co_1798427314394417287.json`, May 7, 2024 20:32 UTC, case 390393: "The following wire transfer has been returned by the beneficiary bank", "Amount: 125.00 USD", "Wire Date: May 07 2024", "Returned Reason: ACCOUNT NOT ELIGIBLE FOR WIRE TRANSFERS", "Returned funds will be credited to your account today" | NO | No return notice. C06MXPL9536 2024-05/8 "we sent the payment today directly to your bank account", /23 "maybe we can ask for a refund", /40 Leonard "I re-sent the wire this time with payoneer's traditional methods", /41 Oleg "Yes, I receive this email. It says I will get it in 7 days"; FO 2024-05/366-369 "Just the tracking is broken when you do direct wire to his intermediary bank" |

**Oleg line.** Under "money must have left and stayed out", the Processed $125 did not stay out. The real payment is the Payoneer ACH debit of $126.25 at 20:15 UTC the same day (`leonard@..._1798426229536387534`, NO). So the wire row nets to $0 and the payee received $125 by another route. Robert-readable records prove only a re-send, not a return. HG Costs UA Assets 24-05 = 125. The net to Oleg is $125 either way for that invoice, plus a second $125 via Payoneer in Oct 2024 (G:00007150 request, AD 2024-10/0-39; HG Costs 24-10 5,125 = Node 5,000 + 125), plus Upwork Jan 2024. **Effect on build: none, Oleg is UA. Effect on the sketch: the RET trap is not unique.** A reviewer with full reach sees two Processed wires that came back, and the method's "stayed out" sentence is false for a row the plan leaves as $125.

**Other failures.** None in money terms: AD 2023-09/223-225 is a wire Leonard could not start ("they never gave us iban or swift"), not a return. Leonard's and Arthur's Processed sets add nothing: Leonard's 132 match Robert's 132 on amount and date with no differences; Arthur has 65 of them. No Processed notice for $33,290 exists in any box.

## Task 3. Payee table and forks

**Planned sentences, numbered for this table.** S1 source of record = Processed notices. S2 money left and stayed out. S3 contractors paid another way count when a record shows the payment. S4 BUILD = team on Deel, studios, freelancers who built a game. S5 UA / AD CREATIVE = anything made to buy installs, out. S6 COMPANY = legal, tools, website, equipment, proposals, not a bet. S7 calendar by notice Transaction Date. S8 work a record ties to one game goes to that game. S9 founders out (Gusto); revenue from REVENUE_DAILY.

Figures assume S3 is limited to Western Union and the $33,290 is admitted by the planned statement. By-bet split is S7 unless stated. All pointers Robert-readable unless marked NO.

| # | Payee (suffix) | Bucket | DD | ZM | CF | Net | Record proving the bucket | Reading a careful reviewer could defend instead |
|---|---|---|---|---|---|---|---|---|
| 1 | Deel, 2 spellings (8380), 35 wires | BUILD | 530,736.14 | 434,185.44 | 50,425.61 | 1,015,347.19 | AD 2023-04/46 "for contractors we start with Deel"; G:00001516#0; AD 2024-02/273 | Whole wire is not all pay: $285 device (AD 2024-05/130-132 = HG Costs Equipment 24-05 285), reimbursements (AD 2023-09/414), Deel fee (HG Costs row 60, $7,350 from 24-10). S8 could reach people tied to DD after Jan 9 (EX 2025-01/442 live ops; EX 2025-11/979). F9, F4 |
| 2 | Leapblock (1359), 29 wires + $33,290 | BUILD | 304,304.00 + 33,290.00 = 337,594.00 | 59,250.00 | 11,100.00 | 407,944.00 | AD 2023-09/554, AD 2023-11/35, LB throughout | $374,654 if S1 is read strictly: no Processed notice for $33,290 in any box. Martin and Victor rows below sit inside this line. F6 |
| 2a | Martin via Leapblock | inside row 2 | | | | no separate figure | LB 2025-04/1, 2025-05/9 ($3,700); LB 2026-02/4 "We paid him until end of January" | From 2025-11-27 he is on two projects: EX 2025-11/971 "UI for 2nd prototype", /979 "UI for proto #2 and also proto #1 combo fighters". Census D's "Martin on Combo Fighter UI" is half the record. He also made UA video assets: C06MXPL9536 2024-05/48. No effect if monthly pay stays BUILD by date. F11 |
| 2b | Victor via Leapblock | inside row 2 | | | | no separate figure | LB 2025-05/2, /9: last pay $2,350 inside $6,050 on 2025-05-07; AD 2025-05/20-24 | Last day Apr 16 2025 (LB 2025-05/2); wire falls in ZM by date; nothing ties it elsewhere. Earlier $4,000 pre-SVB is O6. The $33,290 is his invoices: AD 2023-09/202 |
| 3 | Eveline Art (8501), 28 wires | BUILD | 45,941.50 | 36,070.00 | 11,160.00 | 93,171.50 | AD 2023-10/586; AD 2023-12/129; AD 2024-05/6 Factura_EVE0008.pdf; G:00001856 | None on the bucket. Tie to Marcus is by date plus file name; the contract naming Eveline is in a NO DM. CF share agrees with record: EX 2025-11/972 |
| 4 | MotMot, BANCO 3341, 10 wires | BUILD | 28,128.00 | 8,928.00 | 0 | 37,056.00 | AD 2025-01/112; AD 2024-04/20; FO 2024-02/3657-3662 | **S8 moves the two 2025 wires to DD**: see Task 4. DD 37,056.00, ZM 0. F4 |
| 4a | MotMot, BANCO 8605 | excluded (S2) | -4,032 | | | 0 | AD 2024-04/19-21, /71; G:00004120; G:00004124 | None. Note notice Transaction Date is Apr 2, not Apr 3 |
| 5 | Lucas (6577) 3 wires + 5 WU | BUILD | 13,975.00 | | | 13,975.00 | FO 2024-06/247-249; AD 2024-06/113-114; HG Costs row 4; FO 2024-06/1092 per census | $3.96 more if WU fees count (paid $7,528.96, received $7,525.00) |
| 6 | Graham Porter (1794) G:00013842#0 | BUILD | | 5,000.00 | | 5,000.00 | D04UP2L3E3S 2025-04/1299, 1346; 2025-05/26 "true Art Director who would understand the zombie shit"; 2025-05/396 | None |
| 7 | Ozhan (3307) G:00012291#0 | BUILD | | 1,000.00 | | 1,000.00 | ART 2025-02/4-7, 21, 33 "for the prototype those zombies"; EX 2025-02/1286-1287 | None. Game assets, not ads |
| 8 | Nathan Price (0148) G:00006104#0 | BUILD | 2,368.00 | | | 2,368.00 | AD 2024-07/55-58, 138-143; G:00005635 ART-506 Chest animations | None. Transaction Date Aug 2, 2024 |
| 9 | UX contractor (1876) G:00001901#0 | BUILD | 600.00 | | | 600.00 | AD 2023-05/360, 865; AD 2023-11/4-11; FO 2023-06/1520 "$1200 on [him]" | $1,200 if first half counts (O7). Pre-seed work but date decides. F7 |
| 10 | Lauren Brooks (5384) G:00015809#1, 00016090#1, 00016300#0 | **UA by contract** (sketch: BUILD, DD) | (sketch 1,500.00) | | | 1,500.00 | Agreement f_20a0df3860bb5731d22f07 (can-see YES), Exhibit A: "plan, launch, and scale Telegram distribution"; "run and optimize paid UA for Telegram, manage budgets, creatives, and funnels". C09KU8U4DPF 2025-10/29, /48 "GMT / Marketing plan" | BUILD and DD on the "Telegram port" reading. She did not port it: Arthur does (EX 2025-10/612, C09KU8U4DPF 2025-10/139). F2 |
| 11 | Adjoe (5000) | UA | | (46,201.50 by date) | | 46,201.50 out | #adjoe 2025-04/9-10; G:00015531#0 | None |
| 12 | Node Media (0115) G:00010284#0 | UA | (16,428.57 by date) | | | 16,428.57 out | AD 2025-01/0-2; G:00008689#0; EX 2024-09/1399 | Agency versus creative makes no difference: both are S5 |
| 13 | AppLovin (2532) | UA | | (6,085.56) | | 6,085.56 out | AD 2025-08/57-58; AD 2025-11/38 | None |
| 14 | Creative X (5660) G:00013667#0 | UA | | (3,750.00) | | 3,750.00 out | C08H78VJG80 2025-03/10 "good looking playables"; AD 2025-05/116 "playable invoice"; EX 2026-02/25 "we did it for $3750" | "Playable" misread as a game build. Amount ties by EX 2026-02/25 |
| 15 | Oleg (9368) G:00004648#0 | UA | (125.00) | | | wire 0 net; $125 received via Payoneer | C06MXPL9536 2024-03/40, 2024-05/8-41 | Task 2 R2. F5 |
| 16 | Singular (4015) | COMPANY | (25,000.00) | (6,250.00) | | 31,250.00 | AD 2024-09/29-33; AD 2025-07/25; EX 2024-09/1428-1473 | UA: an attribution tool for paid installs. Out of build either way; company line swings $31,250. F8 |
| 17 | TYZ Law (7534) G:00003134#0 | COMPANY | (7,500.00) | | | 7,500.00 | FO 2024-01/529; G:00002505 | S8 puts it in DD: tied to Domino Delights by record. F3 |
| 18 | Trademark lawyer (7393) | COMPANY | (6,075.00) | (1,100.00) | | 7,175.00 | EX 2024-09/954-956; AD 2024-09/26-28 | S8 for the DOMINO DELIGHTS mark share. F3 |
| 19 | JP website (4020) G:00001860#0 | COMPANY | (3,200.00) | | | 3,200.00 | AD 2023-10/432-433, 586 | None |
| 20 | $500 helper (3139) G:00013842#1 | COMPANY | | (500.00) | | 500.00 | Identity only in NO DM D08RQSCFKJ9; Robert sees EX 2025-05/207, 264 only | Payee's first name token is Robert's own ([PERSON_NAME_0054]): reads as a founder payment. Needs the seed |
| 21 | Martin laptop (3801) G:00015809#2 | COMPANY | | (1,999 BGN) | | 1,999 BGN; $1,209.89 by sheet | AD 2025-10/500, 522, 529 | Task 6. F10 |
| 22 | JPMorgan (3203) G:00006272#0 | excluded by seed | (4,000.00) | | | 0 | G:00006270 created by Arthur 2024-08-19 20:48; AD 2024-08/37-38 | Base gives no purpose. Carta 24-08 3,600 fits, nothing links them. If the seed says "for Carta", a reviewer can put $3,600 in COMPANY as a tool. F8b |

Parentheses: not in any bet; shown where the date would have put it.

**Deel: who is on it.** No UA manager or founder is in the Deel wires. Evidence: the Deel people on HG Salary & Benefits (Claire, Calvin, Douglas, Owen, Samuel, Felix, Simon, EMPLOYEE_0028, EMPLOYEE_0032, Oliver, [PERSON_NAME_0754], Vincent, Brian) reconcile to the wires to within small amounts in steady months: 24-10 wire 43,366.45 vs tab 42,691.76; 25-02 42,472.43 vs 41,841.76; 25-06 44,737.07 vs 44,201.76. Frederick's row ($5,846.16 then $6,666.67, Sep-24 to May-25) does not fit: 24-09 wire minus tab is +596, not +5,846. AD 2024-09/87 "4 full time employees" and AD 2025-01/122 put US staff on Gusto. Non-build-looking Deel people: Simon, a data analyst on hours (AD 2024-08/153; Persona_Briefs), and three Product-department rows. NB-15 means no "employee" wording.

**Fork list, ranked.** Tighten the named sentence before `/prompt`.

| ID | Severity | Sentence | Fork | Size |
|---|---|---|---|---|
| F1 | Critical | S3 | Open set. Animator O2 and Gusto devs O3 qualify on plain words, and neither is in the sketch | ZM up to +$5,400; DD +$31,546.30 and ZM +$3,151.00 by month, or DD +$34,697.30 |
| F2 | Critical | S4/S5 | Brooks is a Telegram growth and paid-UA contractor by her own contract. The OVR channel's only target row is not BUILD | DD -$1,500; OVR row X8, part of B1, B2, B3 logic |
| F3 | High | S6 vs S8 | Order of sentences. TYZ, trademark, Adjoe, Node, Creative X, AppLovin are all tied to DD by record | DD up to +$13,575 if legal follows S8 (trademark wires also cover the HG logo mark) |
| F4 | High | S8 | MotMot's two 2025 wires are DD by record, in ZM by date. Sketch leaves them in ZM. Same sentence is arguable for Deel people | DD +$8,928, ZM -$8,928 |
| F5 | High | S2 | A second Processed wire came back (Oleg). RET is not unique; Robert cannot read the proof | $125 in UA only; zero on build |
| F6 | High | S1 | $33,290 has no Processed notice in any box. S3 "paid another way" does not describe an SVB wire. Needs its own clause. Statement must match invoices 29, 32, 33, 33 (PDFs unread) | DD and Leapblock $33,290 |
| F7 | Medium | S7 | No start date. Pre-SVB payments with readable records: Victor $4,000, UX $600 | DD +$4,600 |
| F8 | Medium | S5/S6 | Singular: tool or UA | Company line $31,250 |
| F8b | Medium | S2/S6 | JPMorgan seed wording can pull Carta $3,600 onto the company line | Company line $3,600 |
| F9 | Medium | S4 | Deel wires include device, reimbursement and fee money | $285 proven; fee about $7,350 by sheet, inside the wires by inference only |
| F10 | Medium | S6 | BGN conversion rests on one sheet cell | About $1,209.89 |
| F11 | Low | S5/S7 | Monthly people who also made ad art or a second prototype | None if "no split" is stated |
| F12 | Low | S3 | WU fees $3.96; Payoneer $1.25 x 2 | Under $7 |
| F13 | Low | text | Slips to fix: BANCO 8605 Transaction Date is Apr 2 (analysis says Apr 3); WU is Jun 3 to Aug 23 (sketch says May-Aug); Nathan's Transaction Date is Aug 2 | None |

**Confirmed safe.** No build payment falls within Jan 3-14, 2025 or Nov 13-30, 2025, so neither start date, nor sent-date versus Transaction Date, changes a figure. Deel carries no founder. Same-amount pairs are separate months.

## Task 4. Tied-to-one-game census

Every Processed payment was checked against the census D proof records and the reads above. "Build effect" means it moves a bet total.

| Payment | Date | Amount | Game by date | Game by record | Bucket | Build effect | Record |
|---|---|---|---|---|---|---|---|
| **MotMot G:00010777#0** | 2025-01-21 | 4,032.00 | ZM | **DD** | BUILD | **Yes** | AD 2025-01/112 "worked 4 extra days OT for us in Dec"; EX 2024-12/962, 1014 pity mechanic; EX 2024-12/1222 |
| **MotMot G:00011701#0** | 2025-02-27 | 4,896.00 | ZM | **DD** | BUILD | **Yes** | EX 2025-01/789 "on DD side ... we assigned [PERSON_NAME_24716]"; EX 2025-01/867 "We are in pretty good shape for DD"; EX 2025-02/934 |
| Lauren Brooks x3 | 2025-10-30, 12-01, 2026-01-06 | 1,500.00 | ZM 500, CF 1,000 | DD | Contested (F2) | Only if BUILD | EX 2025-10/610 "she is in for DD on Telegram"; EX 2025-10/1310; C09KU8U4DPF 2025-10/10, /57-58 |
| Adjoe x3 | 2025 | 46,201.50 | ZM | DD | UA | No | #adjoe 2025-09/4; G:00015531#0 |
| Creative X | 2025-05-16 | 3,750.00 | ZM | DD | UA | No | C08H78VJG80 2025-03/10 |
| AppLovin x2 | 2025 | 6,085.56 | ZM | DD by warehouse only | UA | No | Census C; no Slack tie |
| Trademark $1,100 | 2025-03-12 | 1,100.00 | ZM | DD mark, inferred | COMPANY | No | G:00014372; census D |
| $500 helper | 2025-05-29 | 500.00 | ZM | 4X proposal, not one of three | COMPANY | No | NO DM; EX 2025-05/207, 264 |
| Singular $6,250 | 2025-09-26 | 6,250.00 | ZM | Shared | COMPANY | No | NB-23 note in census D |
| Martin laptop | 2025-10-30 | 1,999 BGN | ZM | None | COMPANY | No | AD 2025-10/522 |

**Not exceptions, but a reviewer will ask.**
- Leapblock 2025-01-15 $7,750: invoices dated 31.12.2024 (LB 2025-01/4). Arrears, no game named; S7 keeps it in ZM. Same for Deel 2025-12-01 $20,879.68, which pays November.
- Leapblock CF wires ($11,100): Martin on proto #2 and CF (EX 2025-11/979). Two projects, so not "one game".
- Off-bank: HG Costs row 5 25-01 2,323 and 25-03 828 are ZM by month, DD by "Mini Game" row label.

**Direction check.** No payment dated DD is tied to ZM, none dated ZM is tied to CF, and none dated CF is tied to ZM by a record. Graham, Ozhan and the animator agree on both tests.

**So:** with Brooks out of BUILD, the MotMot pair is the only BUILD payment set found where record and date disagree. Neither wire names a game: the tie runs through the engineer's name in #executives, which is the same shape as the RET and ALIAS channels.

## Task 5. Sketch totals recomputed

Recomputed from `svb_processed_robert.json`. 132 notices, 131 USD. Sum $1,667,394.32 + 1,999 BGN: **agrees with the analysis.** Plain sums by date DD 984,888.21, ZM 608,820.50, CF 73,685.61: **agree.** Sketch build totals reproduce exactly, with Brooks in DD: DD 960,842.64, ZM 544,433.44, CF 72,685.61, sum 1,577,961.69.

**Bridge from plain sum to sketch**

| | DD | ZM | CF |
|---|---|---|---|
| Plain sum by date | 984,888.21 | 608,820.50 | 73,685.61 |
| Returned wire 8605 | -4,032.00 | | |
| JPMorgan | -4,000.00 | | |
| Node | -16,428.57 | | |
| Oleg | -125.00 | | |
| Singular | -25,000.00 | -6,250.00 | |
| TYZ | -7,500.00 | | |
| Trademark | -6,075.00 | -1,100.00 | |
| JP | -3,200.00 | | |
| Adjoe | | -46,201.50 | |
| AppLovin | | -6,085.56 | |
| Creative X | | -3,750.00 | |
| $500 helper | | -500.00 | |
| Brooks out of date slots | | -500.00 | -1,000.00 |
| **Notices in BUILD** | **918,527.64** | **544,433.44** | **72,685.61** |
| Lucas WU | +7,525.00 | | |
| Leapblock $33,290 | +33,290.00 | | |
| **Strict truth, Brooks in UA** | **959,342.64** | **544,433.44** | **72,685.61** |
| Brooks to DD (sketch) | +1,500.00 | | |
| **Sketch** | **960,842.64** | **544,433.44** | **72,685.61** |

Martin's BGN adds nothing in any USD sum above. A run reading it as $1,999 adds that to ZM.

**By bucket, notices only**

| Bucket | Amount |
|---|---|
| BUILD (nine payees) | 1,535,646.69 |
| UA, Brooks in | 74,090.63 |
| UA, Brooks out | 72,590.63 |
| COMPANY, USD | 49,625.00 (+1,999 BGN, $50,834.89 at $1,209.89) |
| Excluded (8605, JPMorgan) | 8,032.00 |
| Check: BUILD + UA with Brooks + COMPANY + excluded | 1,667,394.32 |

BUILD after off-bank adds: 1,576,461.69 with Brooks out, 1,577,961.69 with Brooks in.

**Which payments move under each trap**

| Trap | Payment | Wrong | Right | Bet effect |
|---|---|---|---|---|
| Returned wire | G:00004088#0 | MotMot 41,088 | 37,056 | DD -4,032 |
| Lucas | G:00005184, 05350, 05489, 05962, 06329 | Lucas 6,450 | 13,975 | DD +7,525 |
| Leapblock | G:00001577#0, Awaiting only | 374,654 | 407,944 | DD +33,290 |
| JPMorgan | G:00006272#0 | Cost | Excluded | DD -4,000 |
| Node | G:00010284#0 | Build | UA | DD -16,428.57 |
| Creative X | G:00013667#0 | Build | UA | ZM -3,750 |
| Oleg | G:00004648#0 | Build | UA | DD -125 |
| Brooks | G:00015809#1, 00016090#1, 00016300#0 | Date slots | Sketch: DD. Contract: UA | Sketch ZM -500, CF -1,000, DD +1,500. Contract ZM -500, CF -1,000 |
| Martin laptop | G:00015809#2 | $1,999 in ZM | Company | ZM -1,999 against the misread |

**If forks resolve the other way**

| Case | DD | ZM | CF |
|---|---|---|---|
| Strict truth | 959,342.64 | 544,433.44 | 72,685.61 |
| + MotMot by record (F4) | 968,270.64 | 535,505.44 | 72,685.61 |
| + Animator (F1) | 959,342.64 | 549,833.44 | 72,685.61 |
| + Gusto devs by month (F1) | 990,888.94 | 547,584.44 | 72,685.61 |
| + Victor and UX pre-SVB (F7) | 963,942.64 | 544,433.44 | 72,685.61 |

## Task 6. Martin BGN

- **1,209.89 sits in Oct-25.** HG Costs (`/sheets_spreadsheets/141/sheets/2`, can-see YES) row "Equipment", grid row 62, column index 29. Position count: index 2 = Jul-23, so index 29 = Oct-25. Its garbled header is `2024-10-25T00:00:00`, consistent with census C hazard 1. Row by position: 23-07 3,250; 23-08 234; 23-10 250; 23-11 3,751.13; 23-12 2,589.27; 24-03 77.41; 24-05 285; 24-06 1,831.91; 24-08 470.85; 24-10 818.77; 25-10 1,209.89. It is the only equipment entry after Oct-24 and the only one in Oct-25.
- **It is the only Robert-readable USD figure.** Gmail `threads/0*.json` complete scans: "1,209.89" 0, "1209.89" 0; "1,999.00" hits only the two notices G:00015809#2 and G:00015811#1, each "Amount: 1,999.00 BGN" with no USD equivalent. BGN in Robert's box otherwise is an Apple notice and URL noise. Slack 2025-1x: "1,209" 0, "1,999" 0, "BGN" no payment text. AD 2025-10/500, 522, 529 say laptop, no amount.
- **The match is still inferred.** No record joins the cell to the wire. Implied rate 1,209.89 / 1,999 = 0.60525 USD per BGN. The receipt is in C6CA6B9D1D97 2025-10/10, can-see NO.

## Limits

- Not read: PDFs (Leapblock invoices, Dixelar and animator invoices, Slack image approvals). Deel run composition is inferred from the salary tab against wires, not from Deel invoices, which are images.
- Task 4 rests on census D's proof records plus the reads above. It is not a month-by-month read of all 35 Deel runs.
- The $4,800 of the animator's $5,400 has only the HG Costs cell behind it. NB-2 covers P&L cost lines, so grading it needs a seed or a decision.
- HG Salary tab rows and HG Costs rows are used for routing and reconciliation only, not as graded values.
- Leonard's and Arthur's mail was read for contradiction checks only. Those records are marked NO above.
