# SC3 record plan (storyline A, "The seed, bet by bet")
Status: complete. Normal universe. Seed bound 2026-02-14T00:00:00Z. Slack export stops Feb 13 10:03 UTC.

## Blockers
Blocking before SQL:
1. **Volume: 87-97 INSERTs against the floor of 120.** The count is in Task 4: the seeds as listed fall 23-33 short. The pre-scenario called this "reachable". Honest ways to close it: more comments only where each answers its payee's own question, or more real mail copies; otherwise an exception. Needs a decision.
2. **Drive PDFs unread.** `0000000029`, `0000000032`, `0000000033` in Invoices/Leapblock should total $33,290, and the agent may be able to read them. The access rule stops me. Someone allowed must confirm before the statement is seeded.
3. **Off-bank rule is not closed.** The census found Payoneer as a second route: Oleg's two $125 requests (G:00004614, G:00007150), and the books show more than his one notice. The method must make the UA bucket override the off-bank clause, or the rule leaves an open set.

Corrections to carry into the design (not blocking):
4. **The January 2024 animator invoice was not waived** (LB 2024-02/15-21). Pre-scenario §8 and census D A8 say waived. It was reissued as invoice 59 and paid in the $23,190 wire.
5. **Statement scope.** Victor had $4K through Deel, May-Jul 2023 (AD 2023-05/733-735, AD 2023-08/819-821). "Everything we ever got" would be false, so scope it to wires from Sep 2023. Total $407,944 over 30 wires.
6. The notice Transaction Date for ***8605 is Apr 2, 2024, and for Nathan Aug 2, 2024. The pre-scenario and census D use the sent date.
7. Leonard approved the JPMorgan wire (G:00006272), so a seeded line can only say he does not remember it.
8. The $500 helper can only be a token in any seed. His email is on the share list of f_88afa082cb45da18d348e5, which Robert can read, so "identity only in a Leonard DM" is slightly too strong.
9. gcal holds no graded fact (Task 7).

Supported, no fallback needed: the Chase top-up. $2,500 + $4,000 - $3,600 = $2,900 fits "Chase account = $3K" (Task 3.2). P&L lines match 22 of 29 Leapblock wires exactly (Task 2.5).

## Task 1. Per-seed constraints

V = verified in base. I = invented by the seed, consistent with base. X = may not be claimed. Leapblock and Chase detail is in Tasks 2 and 3.

### a. Leonard's ask (#winddown)
Must agree with:
- WD 2026-02/197 (ts 1770934638.035469) "Reaching out to our angels properly"; WD/8 "reach out to investors one by one before sending out the email"; D04UC0UEN2V 2026-02/1 "personally reach out to every angel investor" (Robert cannot read that DM).
- WD/7 draft mail: three games, "frugal operation", "once we have clarity on final liabilities". EX 2026-02/402 "I want [..] other investors to feel good and get their docs".
- Channel state: last root is WD/205 (Feb 12 23:04:20 UTC); thread pattern is WD/158 and /202 only. Parent /197 has reply_count 0, thread_ts null.

| Claim | Status |
|---|---|
| Leonard will call the angels one at a time | V |
| Three bets are DD, ZM, Combo Fighter | V (WD/7) |
| He wants what each cost and earned, from Robert | I |
| Robert approved payments, paid one contractor, knows who worked on what | V (AD 2023-09/203, AD 2024-08/6, AD 2024-06/54, /111-114) |
| Any angel's name, amount or reaction | X, keep out: Griffin director resignation and the "$3M from Griffin" conflict (census B items 5, 7) |
| That the mail in WD/7 has gone out | X: base does not settle it |
| Google accounts closing as a deadline | X: WD/190 "archieve account on google after Feb 15" is ambiguous with the next bullet; do not cite |

Window: after the method and project exist, before Feb 13 10:03 UTC. Leonard core hours 07:00-18:00 PT, so Feb 13 about 01:20 UTC.

### b. Method doc (Leonard, gdocs + gdrive)
| Sentence topic | Must agree with | Status |
|---|---|---|
| Source of record = bank notices | Ledger has no vendor names (census C line 76, 226); AD 2025-08/34 "matching what banks say so that's the ground source of truth" | V, and AD 2025-08/34 is a usable base anchor in his voice |
| What counts: money that left and stayed out | Returned wire AD 2024-04/71; Chase transfer | I as a rule |
| Off-bank contractors | Western Union census below; **Payoneer is a second route** | Rule must close both |
| Buckets: build, UA/ad creative, company | Census D rows; AD 2024-09/48 Node; #video_editing_oleg | I as a rule |
| Bet calendar | ZM channel opened 2025-01-09 (C0880U9751A 2025-01/0), prototype talk from 2025-01-03 (EX 2025-01/184). The only notices Jan 1-16, 2025 are $16,428.57 on Jan 2 and Leapblock $7,750 on Jan 15, so either start date gives the same figures; CF "started on Monday" = 2025-11-24 (EX 2025-11/955). Only notice Nov 12-23, 2025: AppLovin $4,144.22 on Nov 12 (G:00015934), UA, so out of build | V, checked on `svb_processed_robert.json` |
| One-game exception | EX 2025-10/526, /535, /630; #telegram-dd; AD 2025-10/520-521 | V facts, I rule |
| Revenue source | REVENUE_DAILY lifetime (pre-scenario §3): keep Snowflake unseeded | V |
| Follow-through on issues | Project rows | I |

Off-bank census, Robert's box, complete scans:
- Western Union: 50 hits in 36 threads, exactly five "ready for pickup" receipts (00005184, 00005350, 00005489, 00005962, 00006329), all to [PERSON_NAME_36400]. Lucas $7,525 stands; with SVB $6,450 it equals HG Costs row 4, $13,975.
- **Payoneer: two Dixelar (Oleg) payment requests, $125 "Video 1 of 4" 2024-05-05 (G:00004614) and $125 "Video Game Trailer" 2024-09-25 (G:00007150).** Requests, no receipt. Plan was 4 videos for $500 (#video_editing_oleg 2024-03/40); HG Costs UA Assets carries 125, 250, and 5,125 in Oct-24 (5,000 Node + 125). So Oleg was paid beyond the single notice. The method must make the UA bucket win over the off-bank clause, or name Lucas's route only, otherwise a run could add Oleg money nobody can total.
- PayPal, Wise, TransferWise, Remitly, Zelle, Venmo, MoneyGram: no payee hits.

May not say: any per-game Deel split (no record); that Leonard "reviewed every line"; a work-month rule; a resolver naming MotMot, Node, Lucas or JPMorgan (pre-scenario §4). Spell "ZM", no zombie words. BGN value must be stated or the row kept off a USD figure: HG Costs Equipment Oct-25 1,209.89 is an inferred match only.

Date fix for the method's "Transaction Date": the notice for BANCO ***8605 says Apr 2, 2024 (sent Apr 3 03:32Z, G:00004088), Nathan Price says Aug 2, 2024 (sent Aug 3). Pre-scenario §5 and census D use the sent date.

### c. Linear project and 22 issues
One issue per census D row. All comments are I unless a pointer backs them; each must repeat only what the cited record says.

| Key | Issue | Notice spelling, suffix | Base record the text must fit | May not say |
|---|---|---|---|---|
| ENG-2438 | Deel | Deel, Inc. / [ORG_NAME_0057] ***8380 | G:00001049; AD 2024-02/273 | Per-game split |
| ENG-2439 | Leapblock | Leapblock LTD ***1359 | Task 2 | Waiver; $374,654 as final |
| ENG-2440 | Eveline Art | ***8501 | AD 2023-10/586; AD 2024-06/102 (+$160 retro) | That Eveline is anyone but Marcus's company |
| ENG-2441 | adjoe | Adjoe GMBH ***5000 | #adjoe 2025-04/9-10, 2025-09/4 | Sept credit (NB-18) |
| ENG-2442 | BANCO DE AMERICA (two accounts) | ***3341, ***8605 | AD 2024-04/71, /77-100; AD 2025-01/112 | "All ten paid" without the return; a MotMot name if ALIAS is to stand |
| ENG-2443 | Singular | ***4015 | AD 2024-09/29-33; G:00007132#1 | Invoice total (NB-23); the unpaid $6,250 |
| ENG-2444 | PERSON_4419_NAME LLC | ***0115 | AD 2025-01/0-2; G:00008689#0 | Node name if ALIAS is to stand |
| ENG-2445 | TYZ Law Group | ***7534 | G:00002505; G:00003549 | Retainer returned or applied (open in base) |
| ENG-2446 | Trademark lawyer | [PERSON_NAME_7200] ***7393 | EX 2024-09/954-956; AD 2024-09/26-28 | Purpose of the $1,100 (inferred) |
| ENG-2447 | Lucas | [PERSON_NAME_36400] ***6577 | AD 2024-09/63-84; AD 2024-10/211; G:00005184 | Total; the WU figure |
| ENG-2448 | AppLovin | ***2532 | AD 2025-08/57-58; AD 2025-11/38 | Game named on the wires |
| ENG-2449 | Graham Porter | ***1794 | D04UP2L3E3S 2025-05/26 | The refused bonus (Leonard DM only) |
| ENG-2450 | JPMorgan | JPMorgan [PERSON_NAME_4503] ***3203 | Task 3 | Any purpose stated as fact; "never saw it" (Leonard approved it); **no Arthur comment here** |
| ENG-2451 | Creative X | ***5660 | C08H78VJG80 2025-03/10; EX 2026-02/24 | |
| ENG-2452 | JP website | M [PERSON_NAME_0056] ***4020 | AD 2023-10/432-433, /569-571 | The other $1,000 |
| ENG-2453 | Nathan Price | ***0148 | AD 2024-07/55-59, /143; AD 2024-08/0, /24 | |
| ENG-2454 | Martin laptop | Martin Walsh ***3801 | AD 2025-10/500, /522, /529 | USD value unless settled; "$1,999" |
| ENG-2455 | Lauren Brooks | [PERSON_NAME_7249] Brooks ***5384 | EX 2025-10/630; AD 2025-10/520-521 | |
| ENG-2456 | Ozhan | PERSON_6074_NAME [PERSON_NAME_16238] ***3307 | C08FG9924R2 2025-02/9-17 | |
| ENG-2457 | UX contractor | [PERSON_NAME_9100] ***1876 | AD 2023-05/360, /865; AD 2023-11/4-11 | |
| ENG-2458 | $500 helper | [PERSON_NAME_0054] [PERSON_NAME_0131] ***3139 | D08RQSCFKJ9 2025-05/6, 9, 96, 104 (Robert NO); EX 2025-05/207, /264; share list of f_88afa082cb45da18d348e5 carries PERSON_5360_EMAIL and Robert | A real name (base has only tokens); that he is Robert |
| ENG-2459 | Oleg | Private Entrepreneur … ***9368 | #video_editing_oleg 2024-05/8, /23, /40-41 | Which of two routes paid; a total |

Date rule: project after WD/188 (Feb 12 22:00:01 UTC, "linear we keep during transition"). All state `Backlog` so no close-out contradiction.

### d. Leapblock statement
See 2.7-2.9. Slack window Feb 13 07:30-09:45 UTC. Must not be a reply (no thread parent exists) and must carry the word "Leapblock".

### e. Arthur's mail
See 3.4. To Leonard and Robert. After WD/183. Must not reply to a Linear note. Must spell "Chase" and "$4,000".

### f. Decoys and controls
| Seed | Must agree with | Status of its claims | May not |
|---|---|---|---|
| Working sheet (gsheets + gdrive) | `svb_processed_robert.json`: by date DD $984,888.21, ZM $608,820.50, CF $73,685.61, total $1,667,394.32 + 1,999 BGN; per-payee sums census D | V arithmetic, wrong by design only against the method | Be labelled final; include a figure not derivable from notices; add BGN as USD unless that is the intended CURR decoy (then ZM reads $610,819.50, say which) |
| Draft deck (gslides + gdrive) | WD/7; P&L funding $3,000,000 over Jul-Oct 2023 (census B line 13); revenue DD $12,331.25, ZM $11.99, CF $11.75 | Stale claims must be plain-sum figures or earlier-dated numbers with a date on the slide | Name an investor; say "$3M from Griffin"; use warehouse UA dollars (NB-19); Dec or Jan cash (NB-3) |
| Calendar hold | Leonard's calendar and Robert's; base sample `/events/3452` | Plan date only | Mon Feb 16 is Presidents' Day, use Tue Feb 17. `description` stays NULL (absent on all base events). No fact only here |
| Contact rows | `contacts.json`: no Lauren Brooks row, no PERSON_5360 row; `job` set on 36, `description` on none | V from EX 2025-10/630 | Put a game in `job` if OVR is to stand; a real surname for the helper |
| Trello card | Founders' board 640643a3fd8f3ca308d9318e, Leonard's admin list; last idShort 455; card #455 "Existing Investor Update" exists | I, older quick plan the method replaces | Comment on a closed card; a figure |

Base controls that need no seed: Leapblock $3,700 Aug 1 and Aug 29, 2025; BANCO $2,688 Jul 19 and Jul 29, 2024; Eveline +$160; $300 book.

## Task 2. Leapblock

Pointer forms follow census D: AD = C04UEQVDVB7, FO = C04UTBZL6AX, EX = C07C2866011, LB = C05URGU759U, WD = C0ADGSZKR3R; `LB 2024-02/15` = messages/C05URGU759U/2024-02.json index 15; `G:00001577#0` = gmail threads/00001577.json message 0. "HG Costs", "HG Salary" = tabs of f_605121f4a36752645e0ac3.

### 2.1 Who the contact is
- EMPLOYEE_0024 is the contact row `contacts/147`: contact_id `7e103a10a99b3f78e4ea8d0c`, first_name `scott`, job "Art Studio Principal (Contract Vendor)", email `employee_0024@harmonygames.co` (`entity.py resolve scott`). Slack text calls him `[PERSON_NAME_0083]` (LB 2026-02/9). G:00002127#0: "he is the one managing the external art studio called LeapBlock".
- Second Leapblock person: EMPLOYEE_0030 = Victor Barnes (art direction, paid through Leapblock, last day Apr 16, 2025: LB 2025-05/2). He cannot post the statement.
- Slack `users.json` gives him real_name `EMPLOYEE_0024_SLACK_ID`, email null. Linear has `usr_EMPLOYEE_0024`. Entity tool reports token_link UNRESOLVED; do not build a claim on joining those records. The statement should name the studio in its own text, because the tool will show a token as author.
- Member of #leapblock (channels.json) and posting at the clock: LB 2026-02/3, 11-16 (Feb 12 18:50 UTC). Not one of the NB-1 people.

### 2.2 How he writes
- Warm, informal, "Hey guys!", light typos, emoticons `:slightly_smiling_face:`, `:wink:`, `;)`. LB 2024-01/10, 2025-07/1, 2026-02/3 are the best samples. Most posts are 1-2 lines; the long ones are 300-500 chars (LB 2024-07/8, 2026-02/3). A 30-line list would be his longest message by far, so the text must say the accountant made it.
- Sofia time; base posts run about 06:00-22:00 UTC.
- Money words: "invoice", "the payment arrived" (LB 2024-06/19), "it is in already" (LB 2024-02/23). He mentions an accountant (LB 2025-05/0, 2025-05/4, 2026-02/3).

### 2.3 Currency and invoice numbering
- Every wire is USD (all 29 notices). All figures in Slack are USD (AD 2023-09/554, AD 2023-11/35, LB 2024-09/5, LB 2025-05/2). His local side is lev/euro only for salaries: LB 2025-05/4 ("with the current USD exchange rate"), LB 2025-12/8 (euro from Jan 1, 2026), AD 2025-05/89. The statement is USD.
- Invoice file names: `0000000193 23.01.2026 EN.pdf`: 10-digit number, DD.MM.YYYY, "EN". One running series that is not HG-only (gaps; `0000000014 17.05.2023 EN.pdf` at AD 2023-05/734 was Victor's first invoice, paid through Deel).
- Sep 2023 batch: files 0000000029 01.09.2023, 0000000032 05.09.2023, 0000000033 07.09.2023 and a second 0000000033 07.09.2023 (1) (AD 2023-09/233). Leonard says "4 different invoices" and "4 payments" (AD 2023-09/203, /231); Drive holds 29, 32, 33 only (`Invoices/Leapblock/`). So do not state a count of invoices or list numbers beyond "the invoices up to September".

### 2.4 Full payment history (29 wires + the orphan)
Wire date = the notice's Transaction Date. Base = Processed notice, except row 1.

| # | Wire date | USD | Running | Record | Pays | Base note |
|---|---|---|---|---|---|---|
| 1 | 2023-09-13 | 33,290 | 33,290 | G:00001577#0 Awaiting only; AD 2023-09/230-235 | "up-to-date until September" (AD 2023-09/203) | Orphan |
| 2 | 2023-10-02 | 22,260 | 55,550 | G:00001695 | Sep invoices 34, 35, 37 | AD 2023-09/554 "$15K + $3260 + $4K" |
| 3 | 2023-11-02 | 25,000 | 80,550 | G:00001910 | Oct | AD 2023-11/35 "$15K + $4K + $3K + $3K"; equals P&L Oct-23 |
| 4 | 2023-11-30 | 24,318 | 104,868 | G:00002092#1 | Nov, invoices 45-48 | LB 2023-11/11-22; $1,282 under P&L |
| 5 | 2024-01-18 | 21,018 | 125,886 | G:00002676 | Dec, invoices 51-54 | Net of the $300 book, inside invoice 54 (LB 2024-01/11-13, 21-22); equals P&L Dec-23 exactly |
| 6 | 2024-02-07 | 23,190 | 149,076 | G:00003152 | Jan, invoices 58, 60, 61 + reissued 59 | See 2.6; $1,910 under P&L Jan-24 |
| 7 | 2024-03-13 | 29,243 | 178,319 | G:00003754 | Feb, 63-66 | $4,143 over P&L (two extra artists from Feb 5, LB 2024-02/11) |
| 8 | 2024-04-11 | 31,100 | 209,419 | G:00004183 | Mar, 68-71 | $6,000 over P&L |
| 9 | 2024-05-14 | 29,880 | 239,299 | G:00004752 | Apr, 73-76 | Equals P&L |
| 10 | 2024-06-20 | 33,895 | 273,194 | G:00005392 | May + first week of June, 78-81 | LB 2024-06/7, /12; equals P&L; "The payment arrived" Jun 21 |
| 11 | 2024-07-05 | 10,925 | 284,119 | G:00005609 | Jun, 85-88 | $25 under P&L |
| 12 | 2024-08-06 | 10,875 | 294,994 | G:00006132 | Jul, 90-93 | Equals P&L |
| 13 | 2024-09-05 | 10,600 | 305,594 | G:00006595 | Aug, 95-97 | Equals P&L |
| 14 | 2024-10-01 | 11,250 | 316,844 | G:00007499#1 | Sep, 100-102 | New rates, LB 2024-09/5 |
| 15 | 2024-11-06 | 11,250 | 328,094 | G:00008633 | Oct, 108-110 | |
| 16 | 2024-12-19 | 9,500 | 337,594 | G:00009868 | Nov, 115-117 | |
| 17 | 2025-01-15 | 7,750 | 345,344 | G:00010556 | Dec, 123-124 | |
| 18 | 2025-02-07 | 7,750 | 353,094 | G:00011122 | Jan, 127-128 | |
| 19 | 2025-03-04 | 7,750 | 360,844 | G:00011765 | Feb, 135-136 | |
| 20 | 2025-04-10 | 7,750 | 368,594 | G:00012909 | Mar, 141-142 | |
| 21 | 2025-05-07 | 6,050 | 374,644 | G:00013497 | $3,700 + Victor's last $2,350, 150-151 | LB 2025-05/2, /9 |
| 22 | 2025-06-02 | 3,700 | 378,344 | G:00013892 | May, 154 | |
| 23 | 2025-06-30 | 3,700 | 382,044 | G:00014406 | Jun, 163 | |
| 24 | 2025-08-01 | 3,700 | 385,744 | G:00014865 | Jul, 167 | Same-amount control |
| 25 | 2025-08-29 | 3,700 | 389,444 | G:00015146#5 | Aug, 172 | Same-amount control |
| 26 | 2025-09-30 | 3,700 | 393,144 | G:00015481 | Sep, 177 | |
| 27 | 2025-10-31 | 3,700 | 396,844 | G:00015828#1 | Oct, 181 | |
| 28 | 2025-12-11 | 3,700 | 400,544 | G:00016139 | Nov, 185 | LB 2025-12/3-7 |
| 29 | 2026-01-02 | 3,700 | 404,244 | G:00016275 | Dec, 192 | LB 2025-12/8-9 |
| 30 | 2026-02-02 | 3,700 | 407,944 | G:00016690#2 | Jan, 193 | LB 2026-01/2; "our last payment" LB 2026-02/0 |

Totals: 29 notices $374,654. With the orphan, 30 wires **$407,944**. By calendar year: 2023 $104,868; 2024 $232,726; 2025 $62,950; 2026 $7,400.

Invoice numbers in column "Pays" are file names read from Slack; the PDFs were not read, and amounts are not per-invoice facts.

### 2.5 Is the $33,290 real? Base check
Supports it:
- Leonard created the recipient at 14:46 UTC (G:00001576), submitted, "I need approval", Arthur "Done!" 14:55 (AD 2023-09/229-235).
- P&L carries Jul-Sep 2023 Leapblock lines as cost. Nobody chases the money afterwards in AD, LB, D05LS4L9W8K or CF7DABF95AFF: the next ask is the September invoices (D05LS4L9W8K 2023-09/41-59).
- **New reconciliation (mine):** HG Costs Saga Map + 3D Animator (to Jul-24) + HG Salary Victor + Martin rows, month by month, match the wire exactly for 22 of the 29 months from Sep-23 to Jan-26 (one wire per month, in order, counting Martin's $260 in September). The other seven differ by -$1,282, -$1,910, +$4,143, +$6,000, -$25, +$200, +$350 (Nov-23, Jan-24, Feb-24, Mar-24, Jun-24, Apr-25, May-25), net +$7,476. P&L Jul+Aug 2023 Leapblock lines are $35,000 ($12,000 + $15,000 saga, 2 x $4,000 Victor), so the Sep 13 wire is $1,710 under them. So the founders' own books treat those months as paid.

Does not exist: a Processed notice in any mailbox ("33,290" one hit in all 88,728 files, G:00001577 only; "33290" hits are other strings). Leonard's box has no copy of the Awaiting mail.

Nothing found that contradicts receipt. The "cash in the envelope" line (AD 2023-09/227) is a joke made before the IBAN arrived; it is a mild decoy.

### 2.6 January animator invoice and the $300 book
- **Correction to the pre-scenario wording: the January invoice was not waived.** He offered to skip it (LB 2024-02/15, /17). Leonard said he was "happy to pay for the animator's time" (/18). He then posted invoice `0000000059 31.01.2024 EN.pdf`, "the current one for January's work" (/19), and Leonard: "This sounds about right. I will take care of it today" (/20). "The wire is on its way" (/21). FO 2024-02/355 calls it "the correction of the animator's time". Census D A8 ("waived") and §8 of the pre-scenario should change.
- The Feb 7 wire is $23,190, $1,910 under the P&L's $25,100 for Jan-24. That reads as a reduced animator invoice of about $1,090 (inference: $23,190 - $15,000 - $4,000 - $3,100). The amount is only in the PDF and image. Statement must not state a waiver or a credit.
- $300 book: inside invoice 54, wire 5, already net (LB 2024-01/11-13, /21-22; FO 2024-01/1639-1640 "discounted from the leapblock invoice"). Statement lists $21,018 with no separate line. It is a control: nothing is added or taken off.

### 2.7 Is a statement plausible?
Yes.
- LB 2026-02/3 (Feb 11 20:47): "I will check with him and our accountant tomorrow, and then we can schedule a call". LB 2026-02/9-17: call on Feb 12 about 18:50 UTC. So an accountant's close-out list the next morning follows from the base. Last base post in the channel is Feb 12 18:50:xx UTC.
- Window: after Feb 12 18:51 UTC, before Feb 13 10:03 UTC. Sofia working hours give Feb 13 about 07:30-09:45 UTC.
- It needs a reason other than Leonard's task: closing the client file and Martin's contract. Leonard's own Feb 11 message says money is over.

### 2.8 Facts a statement must list (no wording)
- Scope line: USD received on Leapblock's bank account from Harmony Games by wire, from the first invoices paid in Sep 2023 to the last payment, 30 payments, total $407,944.
- Rows 1-30 above, each with wire date and amount; row 1 is 13 Sep 2023 $33,290.
- Dates: use the wire date, not arrival. Arrival is 0-3 days later (LB 2024-01/35, 2024-02/23, 2024-06/19), and arrival dates cannot be verified for 30 rows. A label such as "date of your wire" keeps it true.
- Alternative if the full list reads wrong in Slack: year totals plus total, and the first line named. That makes ORPH a diff against $374,654 rather than a visible row. Year totals above.

### 2.9 Claims it may not make
| Claim | Why not |
|---|---|
| "Everything HG ever paid us" with no scope | Victor's own first contract: $4K via Deel, May-Jul 2023 (AD 2023-05/733-735, AD 2023-08/819-821), invoice 0000000014. Not a Leapblock wire. Scope to the wires from Sep 2023 |
| A breakdown of the $33,290 | No text record; Jul+Aug P&L lines give $35,000; PDFs unread. Invented |
| Invoice count, or "four invoices" | Two files share number 33; Drive has three names |
| Any waiver or credit for January 2024 | LB 2024-02/18-20 |
| Any figure in EUR or BGN | All wires USD |
| Any balance owed, unpaid invoice, or a February 2026 invoice | LB 2026-02/5 "no invoice coming"; LB 2026-02/3 mentions Martin's notice only; keeps NB-4 out |
| Martin's severance or notice amount | Not settled in base at the clock; keep off |
| Arrival dates | Unverifiable |

### 2.10 Limit
The Drive PDFs `0000000029 01.09.2023 EN (1).pdf`, `0000000032 05.09.2023 EN (2).pdf`, `0000000033 07.09.2023 EN (2).pdf` (Resource: 7240535625619857401/Invoices/Leapblock/) are readable by the agent with `gdrive_read_file` if shared with Robert, and they were not read here (raw-file rule). Their sum should equal $33,290. Someone allowed to open them should confirm that before SQL. A reader of those PDFs is also a route to the orphan amount.

## Task 3. Chase

### 3.1 Every base record on the company's Chase account
| When | Record | Fact |
|---|---|---|
| 2023-04 | AD 2023-04/256, /301, /1081; AD 2024-01/36 | Company opens Chase; "when he started the account" = Arthur ("Blake") |
| 2023-07 | FO 2023-07/764; G:00003071#0; leonard@…_1773214172892638586 | Wire details, "Bank name: Chase, Account Name: Harmony Games GAMES INC." (number masked); seed wires land Jul 21, 2023 |
| 2023-07 | AD 2023-07/886-954 | Two-approval setup problems |
| 2023-08 | AD 2023-08/640-641, /708-720, /910-913, /966 | Cash moves to SVB; online wire limit |
| 2023-08 | AD 2023-08/980-987 | "we are keeping Chase", "we won't use Chase really" (two-bank advice) |
| 2023-08 | AD 2023-08/660 | Carta "$3600/year. With SVB discount we'll pay $2880" |
| 2023-09 | AD 2023-09/146-154, /179 | Founder loans discussion, "Chase is probably easier" |
| 2024-01-06 | AD 2024-01/32 ("Just went to [ORG_NAME_0002]") | Min balance for no monthly fee is $2K; "leave There $2500 just in case for any future wiring fees etc and move the rest to SVB". Token: `JPMorgan [ORG_NAME_0002] Binghamton` in leonard@…_1851692412866877715 |
| 2024-01-07/08 | AD 2024-01/33, /37 | $75 wire fee out; ACH attempt to SVB |
| 2024-02 | Trello #258 "move money from [BANK_NAME_0001] into SVB", closed | Same move |
| 2024-08-19 | G:00006270 (Recipient, created by Arthur 20:48:01Z), G:00006271, G:00006272 (Processed 20:58:27Z, approved by Leonard); Leonard copies …1807850387661290089, …1807850432488968709, …1807851044272471527; AD 2024-08/37-38 | The wire |
| 2025-07-03 | AD 2025-07/9 Arthur | ~$11K IRS cheque: "Going to deposit in Chase then transfer over" |
| 2025-08-06 | AD 2025-08/23 Leonard | Statements at the report date (about Jun 30, 2025): "Chase account = $3K" |
| 2025-10-30/31 | AD 2025-10/551, /563 | "close Chase"; "Chase account closed. Cashiers check deposited into SVB" |
| 2025-11-01 | AD 2025-11/2 | Statements zip (file only, contents not readable) |
| 2026-02-12 | WD 2026-02/182-183 | "I can't remove the bank account from Carta but they are tied to our Chase account which is closed" |

Mail from `SVC_4127` in Robert's box (00000989, 00001374, 00002192, 00007096, 00014690, 00014867, 00015160) is Chase Credit Journey and card marketing on his personal card, not this account. Arthur's mailbox holds no SVB notices at all ("***3203" 0 hits under threads/blake*).

Carta debits (HG Costs row 48, no other Carta money record in any mailbox): Aug-23 $2,880, Aug-24 $3,600, Aug-25 $3,852. Annual.

### 3.2 Was $4,000 plausible as a top-up? Yes, and the arithmetic fits
- Balance kept at Chase from Jan 2024: about $2,500 (AD 2024-01/32).
- Carta's Aug-24 charge: $3,600, full price after the first-year 20% discount (AD 2023-08/660, HG Costs row 48). That is more than the balance.
- $2,500 + $4,000 - $3,600 = $2,900, which is Leonard's "Chase account = $3K" a year later (AD 2025-08/23). **This is the strongest single fit and no census had it.**
- It sits above the $2K no-fee floor; a smaller wire would not.
- HG Costs Aug-24 has no $4,000 line of any kind: the founders' own cost tab does not treat it as spend. Banking Expenses Aug-24 $30 fits one wire fee (inference).
- The recipient is named after the bank, not a person (G:00006270), and Arthur created it minutes before the wire, which fits a move between own accounts.
- Arthur started the account and ran the wire. Leonard approved it (G:00006272), so he knew of it at the time. Any seeded line by Leonard saying it is unknown must be "don't remember", not "never saw".

### 3.3 Anything contradicting it?
None found. Checks:
- `Chase` and `Carta` across all of EX, FO, D04UP2L3E3S, D04UGG61DUM, D04V95AAAHW from 2024 on (complete scans, nothing on the wire); AD read through the all-Slack `chase` scan (capped at 400 but AD sorts first, so AD is complete).
- Aug 2024 terms across all channels and DMs: chase, carta, $4K, 4,000, reimburs, top up, transfer, personal account: nothing else explains $4,000 (D04UP2L3E3S and AD read Aug 18-20).
- $4,122.74 CA EDD on Aug 7 is an ACH from SVB by routing number (AD 2024-08/7-32): a near-amount decoy, but a different date, amount and route. Keep it out of Arthur's note.
- Nothing names the ***3203 holder. The account number is masked everywhere, so nobody can prove ***3203 is the company account either; that one link is the seed's own contribution.
- AD 2025-07/9 leaves open whether the ~$11K moved over before closure; the note should not state the closing amount.

### 3.4 What the note may and may not say
| Claim | Status |
|---|---|
| Chase was the company's own account, closed Oct 31, 2025, cheque into SVB | Verified |
| Carta bills from Chase | Verified for Feb 2026 (WD/183); consistent earlier |
| Carta renewal Aug 2024 was $3,600 | Verified (HG Costs, AD 2023-08/660) |
| About $2.5K left there since Jan 2024 | Verified as intent (AD 2024-01/32) |
| ***3203 is that account; the $4,000 was a top-up from SVB for the renewal; it is not a cost | **Invented by the seed, fits everything** |
| Exact Chase balance on Aug 19, 2024; date Carta debited; a failed or bounced debit; a fee charged | Invented with no support: do not state |
| Amount of the closing cheque; what happened to the ~$11K | Unknown: do not state |
| Linking the wire to CA EDD, Fondo or reimbursements | Contradicted or unsupported |

Dating: after WD/183 (Feb 12 21:48 UTC). Arthur's window 10:00-20:00 New York, so Feb 13 about 15:00-23:00 UTC. Natural reason: Chase records for the dissolution paperwork.

### 3.5 Safer story?
The top-up is well supported, so no alternative is needed. Fallback, if a reviewer rejects the Carta link: the same mail says only that ***3203 is the company's own Chase account and the $4,000 stayed in the company; it drops the Carta sentence. That still resolves the row under "money that left and stayed out" and needs no base change.

## Task 4. Id plan

All ids below were minted with salt `hg-robert-seed-bets|` by /private/tmp/claude-501/-Users-sumit-Source-OC/291ff662-f24b-4f22-9fb7-b1cecbd8895a/scratchpad/sc3/mint.py, output in /private/tmp/claude-501/-Users-sumit-Source-OC/291ff662-f24b-4f22-9fb7-b1cecbd8895a/scratchpad/sc3/ids.json. Collision results, `hg.py search lookup` unless noted, every scan complete, 0 hits:

| Collection | Key | Records checked |
|---|---|---|
| slack messages/*.json (5,353 files) | id, ts | 687,230 |
| gdrive /drive_files | id | 53,866 |
| gdocs /docs_documents | document_id | 633 |
| gsheets /sheets_spreadsheets | spreadsheet_id | 398 |
| gslides /slides_presentations | presentation_id | 164 |
| linear /issues | id, identifier (ENG-2438..2469) | 3,852 |
| linear /projects | id | 2 |
| gcal /events | event_id, ical_uid | 11,130 |
| trello /cards, /actions | id | 803, 5,294 |
| contacts | contact_id | 170 |
| gmail, all 88,728 files (search-many; lookup cannot read Gmail) | 4 thread numbers, 2 Message-IDs | 0 hits each |

Times are proposals, chosen off the whole minute and inside each author's hours.

| Key | UTC | Note |
|---|---|---|
| deck | 2026-02-12T19:21:37Z | |
| sheet | 2026-02-12T19:48:12Z | |
| trello | 2026-02-12T20:14:26Z | |
| project | 2026-02-12T23:12:43Z | After WD/188 22:00:01 |
| issue0 | 2026-02-12T23:13:29Z | Then +20-70 s each |
| method / modified | 2026-02-12T23:52:18Z / 2026-02-13T00:41:06Z | |
| contact | 2026-02-13T00:58:51Z | |
| ask | 2026-02-13T01:23:41Z | |
| hold created | 2026-02-13T01:31:17Z | Start 2026-02-17T17:00:00Z, end 18:30:00Z |
| statement | 2026-02-13T08:37:26Z | Slack stop is 10:03:26 |
| Arthur mail | 2026-02-13T16:26:44Z | Robert's last base mail is Feb 13 02:29Z (00016906); later is allowed, under the bound |

### slack.slack_messages
Columns: id!, ts!, channel_id!, type!, user_id, text!, thread_parent_id, thread_ts_legacy, reply_count!, reply_users_count!, latest_reply, is_activity_message!, subtype, reactions_json!, files_json!, attachments_json!, created_at!, edited_ts, edited_user, bot_id, client_msg_id, permalink, metadata_json!, text_fts[generated].

Convention: ts ends in 9 (all sampled; precedent did not, memory says that failed elsewhere). id = sha256("<channel>|<ts>")[:32]. created_at = ts as ISO.

| Seed | channel | ts | id | user_id |
|---|---|---|---|---|
| ask | C0ADGSZKR3R | 1770945821.640039 | fa707da5679e86fd88f6638bd1828bfe | EMPLOYEE_0038_SLACK_ID |
| statement | C05URGU759U | 1770971846.479179 | 6312d121675119df7a441f9ca5c6b4cb | EMPLOYEE_0024_SLACK_ID |

Ask placement. Root (recommended): thread fields NULL, reply_count 0, no UPDATE on base. Reply variant: thread_parent_id `e3e198cc6e3f866a032d34c5f69e39f9`, thread_ts_legacy `1770934638.035469`, plus UPDATE on that parent: thread_ts_legacy = its own ts, reply_count 1, reply_users_count 1, latest_reply `1770945821.640039`. Same id and ts either way. Base shape: WD/158 (reply_count 1, thread_ts = own ts), WD/202 (thread_ts = parent ts).

### gmail
gmail_threads: id!, user_email!, snippet, history_id (NULL). gmail_messages: id!, thread_id!, user_email!, label_ids_json, trash_removed_labels_json, snippet, history_id, internal_date, date, size_estimate, subject, from_email, from_name, to_json, cc_json, bcc_json, reply_to_json, body_text, body_html, headers_json, payload_json, in_reply_to, references, mbox_from, date_parsed_source, attachments_meta_json, body_text_fts[generated].

Mailbox ids are the full addresses (`arthur.blake@…`, `leonard.hayes@…`), although file names say `blake@`, `leonard@`. Message id = `<mailbox>/<RFC id>`, same RFC id in every copy. Thread id is 19 digits, `>>20` = ms, differs per mailbox. Snippet = first 175 chars of the collapsed body. Bodies use \r\n. No Reply-To on internal mail. Arthur's Message-ID prefix `CAOOpSq` (G:00016564), local part 51 chars. Labels: sender `["SENT"]`; recipients `["INBOX","IMPORTANT","CATEGORY_PERSONAL"]` (G:00016902). 2 INSERT per mailbox.

| Mail | RFC id | Threads |
|---|---|---|
| Arthur on Chase | `<CAOOpSqA2MTKGlKETvkoKqFfq1MaIktcGcH9cj21BJMAMN4Ok00@mail.gmail.com>` | arthur.blake@harmonygames.co/1857028101192329480; robert@harmonygames.co/1857028101191819317; leonard.hayes@harmonygames.co/1857028101191912856 |
| Hold invitation to Robert | `<calendar-ed5dffa0-659a-e7c0-dbf0-ca152bb44ed9@google.com>` | robert@harmonygames.co/1856971763554571125 |

Invitation companion (INT-11): subject `Invitation: <summary> @ Tue Feb 17, 2026 9am - 10:30am (PST) ([PERSON_NAME_0055])`, attachment meta as precedent `invite|robert` (build_sql.py).

### linear
linear_projects: id!, team_id!, name!, summary, description, lead_id, priority!, state, start_date, target_date, uuid, icon, color, started_at, completed_at, canceled_at, start_date_resolution, target_date_resolution, labels_json!, links_json!, is_archived!, created_at!, updated_at!.
linear_issues: id!, uuid, project_id, team_id, parent_id, assignee_id, creator_id, state_id, cycle_id, identifier, number, title!, description, priority!, estimate, due_date, started_at, completed_at, canceled_at, archived_at, time_in_status_minutes, labels_json!, links_json!, relations_json!, state_history_json!, is_archived!, created_at!, updated_at!.
linear_comments: id!, issue_id!, author_id!, parent_id, body!, is_edited!, created_at!, updated_at!, sequence.

- Team: `team_ENG`. It is the only team with a working precedent (LLC task, 37 issues, passed /injection), has Backlog, Todo, Done, Canceled in use, and no finance team exists. Max base ENG number 2437.
- Project id `0742c172-85de-47ed-a111-316e5c8cb187`, lead `usr_63fffeb4fab5233e`, priority 0, state `started`, start_date `2026-02-12`, labels `[]`, links `[]`. linear_project_teams and linear_project_members: do not write (build_sql.py line "not writable", guideline 2026-10-22).
- Issues ENG-2438..ENG-2459: id = identifier, number int, state_id the state NAME `Backlog`, creator `usr_63fffeb4fab5233e`, assignee NULL, priority 0, all lifecycle stamps NULL, labels `[]`, links `[]` (keep empty: NB-24), relations `[]`, state_history `[]`, is_archived false, updated_at = last comment time.
- Labels: linear_issue_labels is not exported and not in injection.json. Use labels_json `[]`. No label rows.
- `linear_teams.issue_counter`: precedent did not bump it and passed; mark optional [U].
- Comments: base has none (NB-24), id format free. Rule `"comment_" + sha256(SALT+"note|"+<issue key>+"|"+<n>)[:32]`, sample `comment_4b5619299256933257ec311bccab35d3`. Authors `usr_63fffeb4fab5233e`, `usr_cc3e90160f490686`. is_edited false, parent_id NULL, updated_at = created_at, created_at after the issue's. Robert `usr_Robert` is the writer in the run. The `sequence` column stays unset as in the precedent.

### gdrive.drive_files (+ mirrors)
Columns: id!, name!, mime_type!, parents_json, owner_email, shared_with_emails_json, shared_roles_json, visibility_role, shared_groups_json, visibility, owners_json, modified_time, created_time, size, trashed, starred, content_path, web_view_link, icon_link, description, drive_id, content_text.

| Seed | id | mime | Owner, parent |
|---|---|---|---|
| Method | f_6feda53b2382c63bf47b25 | application/vnd.google-apps.document | Leonard, d_63fffeb4fab5233ed5bb73 |
| Working sheet | f_3304033843904a426f3c00 | application/vnd.google-apps.spreadsheet | same |
| Draft deck | f_a4b3c4287a4314d8e532e1 | application/vnd.google-apps.presentation | same |

`size` and `content_path` NULL (id_contracts: NULL means no bytes; these are served from their native rows). visibility `private`. Native row id = drive id; same sharing on both rows. Folder modified_time: if a reviewer applies the "folder at or after newest child" rule, UPDATE Leonard's root modified_time to the latest child (precedent did not; base root value not read).

gdocs.docs_documents: document_id!, title!, owner_email, shared_with_emails_json, visibility, body_text, style_runs_json, revision_id, drive_file_id, created_time, modified_time, text_style_runs_json. revision_id `a7f6f837df`; style runs TITLE + NORMAL_TEXT as precedent `gdoc()`; body_text non-empty.

gsheets.sheets_spreadsheets: spreadsheet_id!, title!, owner_email, shared_with_emails_json, visibility, drive_file_id, created_time, modified_time. sheets_sheets: spreadsheet_id!, sheet_id!, title!, index, row_count, column_count, grid_json. One tab sheet_id 0, 1000 x 26 as precedent.

gslides.slides_presentations: presentation_id!, title!, owner_email, shared_with_emails_json, visibility, drive_file_id, revision_id, created_time, modified_time. slides_pages: presentation_id!, object_id!, index, layout, notes. slides_page_elements: presentation_id!, page_object_id!, object_id!, kind, text, placeholder_type, x_emu, y_emu, width_emu, height_emu, table_json, ordinal.
revision `d4ea3db1db`; pages slide_876d3aebf1e5, slide_541fd17875ce, slide_09f12ee6f24d; elements el_6b8f1c138f0c, el_15b213cdfaa1, el_0e414d770865 (kind TEXT_BOX, 0, 0, 9144000, 5143500, notes NULL: base notes are empty).

### gcal.gcal_events
Columns: event_id!, calendar_id!, summary, description, location, start_ts, end_ts, start_json, end_json, organizer_email, creator_email, attendees_json, status, visibility, transparency, rrule_json, recurring_event_id, original_start_json, sequence, created, updated, hangout_link, ical_uid, extras_json.

One row per attendee calendar, `self:true` moves with the calendar (base `/events/3452`).
- evt_cdc76b69e93767407fb591 on leonard.hayes@harmonygames.co
- evt_f21476dc404329f67fd60d on robert@harmonygames.co
- ical `9cded1c61115ffa1113c5b85d382d773@hg4`, hangout `https://meet.google.com/jig-ieee-bne?hs=224`
- status confirmed, transparency opaque, rrule `[]`, sequence 0, description, location, visibility NULL.
- Add Arthur only with a third copy (mint `evt_` + hx("hold|arthur…")) and his invitation mail.

### contacts.contacts
Columns: contact_id!, first_name!, last_name!, is_user, gender, age, nationality, city_living, country, status, job, description, phone, email, address, created_at, updated_at, source. last_name '' allowed; gender and status 'Unknown'; is_user false; description NULL. Export has no created_at or updated_at values.
- cnt_df6a482c50c0 Lauren Brooks
- cnt_7f7ab446e59c helper (only if kept; first_name must be a token such as `PERSON_5360`, email `PERSON_5360_EMAIL`)

### trello
trello_cards: id!, name!, idBoard!, idList!, desc, pos, closed, due, dueComplete, idMembers_json, idLabels_json, idShort, shortLink, shortUrl, url, dateLastActivity, cover_json, badges_json, start, idAttachmentCover.
trello_actions: id!, type!, date!, idMemberCreator, idBoard, idCard, data_json.

- Card 698e34a2af74d68d679de7b3, action 698e34a21614e56f8af58d35 (`createCard`). First 8 hex = 2026-02-12T20:14:26Z.
- Board 640643a3fd8f3ca308d9318e, list To Do 640643a3fd8f3ca308d93195, idShort 456, pos 3.0 (To Do has no open base card), shortLink NULL, shortUrl NULL, url `https://PERSON_6092_TRELLO_USERNAME.com/c/RnNfAVAl/456-<slug>`, creator `PERSON_6094_TRELLO_USER_ID` (Leonard), badges as `build_sql.py` with `description:true`, comments 0. A comment adds a commentCard action and badges.comments 1. Data block `{"board":{"id":…,"name":"Harmony Games","shortLink":"f4LGcmuh"},"card":{…},"list":{"id":…,"name":"To Do"}}`.

Row estimate: 1 project + 22 issues + 35-45 comments + 2 slack + 8 mail rows (Arthur 3 x 2, invite 1 x 2) + 3 drive + 1 doc + 1 + 1 sheet rows + 1 + 3 + 3 slide rows + 2 gcal + 2 contacts + 2 trello = 87-97. **Short of the ≥ 120 INSERT floor by 23-33.** See Blockers.

## Task 5. Robert ownership

- Base proof of the sharing pattern: f_94a6cc2d20a06079f294f9 "Harmony Games Long Form", owner Leonard, shared_with robert, frederick, arthur, visibility private. `persona_view.py can-see robert gdrive` and `gdocs`: YES, reason "file is shared with the persona (shared_with_emails)". Other Leonard-owned examples: f_64e832f6ab61eb09e6ccd0, f_88afa082cb45da18d348e5.
- Seeds b and f (sheet, deck): owner_email and owners_json Leonard; shared_with_emails_json `["robert@harmonygames.co","arthur.blake@harmonygames.co"]` on the Drive row and the same on the native row; visibility `private`.
- shared_roles_json `[{"email":…,"role":"reader"}…]`. The precedent used `writer`; base export has no roles, shape [U]. Reader states the intent: Robert reads, never edits.
- Nothing in a seed asks Robert to change a seeded file. His Drive target is the new sheet, in d_9f7ba94f7526d54d8482ba, which needs no seed. Other writes are Linear and Slack, which are not Drive-family.
- Check before SQL: `persona_view.py check-sql` for the three ids; not run, no SQL exists.

## Task 6. Findability

| Seed | Natural route | Caveat |
|---|---|---|
| Ask | `slack_read_channel`/`slack_conversations_history` on #winddown; `slack_conversations_search_messages` "angels" | As a root it is the newest message. As a reply, history shows only parent with reply_count 1; needs `slack_read_thread`/`slack_conversations_replies`, though search returns replies (§6b) |
| Method | `gdrive_search` on the title word the ask gives, or `gdrive_list_recent_files`; `gdocs_get_document` | The ask must name the title. Slack links in base use Google's long ids, which `f_` ids are not; precedent referred by title. /oe bars search terms drawn only from the target's own title |
| Project | `linear_list_projects`, `linear_list_issues(project=…)` | `query` matches any word; use project or team + createdAt. Issue items show description, **no comments** |
| Comments | `linear_list_comments(issueId)` per issue | Only reader; no bulk route. `linear_show_data` is a possible bulk shortcut [U]: test in the pre-check |
| Statement | History of #leapblock (top-level, newest); search "33,290", "Leapblock" | Author shows as a token, so the text must carry the studio name. Use `33,290` with the comma to match the notice. Search needs the channel filter or the amount |
| Arthur's mail | `gmail_search_messages` "Chase", "JPMorgan", "4,000", "3203", then `gmail_get_message`/`gmail_get_messages_batch` | Search returns ids only. "Chase" also hits Robert's personal Chase mail (7 threads). A "JPMorgan" query also hits newsletters; "3203" hits the three notices plus this mail only if the body has it |
| Working sheet | `gdrive_search`, `gsheets_values_get` | Leonard's sheet is not under Robert's root: list-folder on his root misses it; use search or shared listing |
| Deck | `gdrive_search` mimeType, `gslides_get_presentation_text` | Text on elements, not notes |
| Hold | `gcal_list_events` with timeMin after the clock, `gcal_search_events` | Future-dated; many runs won't look. Keep it off any graded path |
| Contacts | `contacts_search_contacts` "Brooks" | Whole set dumps in a few pages; a weak surface |
| Trello | `trello_search` (all words required, matches comments), `trello_get_cards_in_list` | Unscoped; To Do has no other open card, so it is easy to see |

Confirm all in the pre-check, plus all 132 notices through the tools.

## Task 7. Ten schemas

| Schema | Job | Verdict |
|---|---|---|
| slack | Ask, Leapblock statement | Needed |
| gmail | Arthur's correction; invitation | Needed |
| linear | Project, 22 issues, per-issue comments, closes | Needed; carries the call volume |
| gdocs | Method | Needed |
| gdrive | Parent rows for the three native files | Needed as a companion; also Robert's listing surface |
| gsheets | Leonard's plain-sum sheet, the A1 wrong summary | Needed as a decoy |
| gslides | Draft deck with stale claims | Real if the ask has Robert say which lines no longer hold. Otherwise decoy only |
| trello | Older quick plan the method replaces | Thin. Honest job: a supersession (the manifest needs ≥ 4). The method must say it replaces it |
| contacts | Lauren Brooks row `job`; helper row optional | Thin. Honest job: a name the notices token out. Facts are base-verified. Does not settle any row alone |
| gcal | Date of the first calls | **Holds no graded fact.** Only sets when the figures are needed, which the ask could say itself. It is in the ten only because the floor is ten |

Can gcal carry something real? Not safely: description is not a permitted sole carrier and base has none. A summary could name the date only. If the floor allows nine injected schemas plus Snowflake's read, drop gcal. Otherwise keep it, and disclose in the dossier that it is context. GitHub has no honest fact in this story, and Confluence is ruled out (learnings §26, §32), so no swap is available.

Services carrying weight: slack, gmail, linear, gdocs, gdrive, gsheets, gslides, trello, contacts, snowflake (read only) = 10 without gcal, but trello and contacts are thin.

