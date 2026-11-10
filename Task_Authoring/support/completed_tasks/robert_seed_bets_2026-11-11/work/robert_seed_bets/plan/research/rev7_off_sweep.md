# Rev7 OFF sweep: remove "the bank has him from Sep 2024" from ENG-2447

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal). Persona Robert. SQL read only, never run.
Edit tested: comment_b13f790bb95e249b8d3a48b1881c0e3a to "that's Lucas, mini games dev". Doc f_6feda53b2382c63bf47b25 unchanged.

## Verdict: SAFE WITH A SPECIFIC CONDITION

The note was a hint, not a resolver. Truth stays 13,975 on the doc sentence plus base-data receipts, and the set closes: one payee, five transfers, $7,525.

Condition: the doc sentence stays verbatim, and two Grounding Dossier rows must stop using the deleted clause as their resolver (lines 696 and 1150: "and the Leonard note says the bank has him only from Sep 2024"). Rebuild from `plan/assemble_dossier.py` and `plan/assemble_brief.py`, which hold the same text. No OE or rubric text may cite the clause. Then `/injection` + `/prompt` on the new SQL bytes, as the hardening report already requires.

Honest cost: this makes OFF much harder, and the realistic failure is real. The only run's rail-list hunt missed Western Union (trajectory event 177: `payoneer OR wise OR paypal OR transferwise OR remitly`). It reached the receipts only through a date-window search for another trap (event 291). With the clause gone, a run that does not name-search or rail-search correctly reports 6,450. That is a miss, not a second valid answer.

## 1. Does a careful reader still land on 13,975 and nothing else?

Yes. Every fork, with what closes it:

| # | Fork | Closed by | Touched by edit? |
|---|---|---|---|
| F1 | Notices only, 6,450 | Doc: "If we paid a contractor some other way, it goes in only if a receipt for it reached your mail". Five receipts are in Robert's INBOX | No. Stopping at the notices is a miss |
| F2 | Sent vs charged (7,525 vs 7,528.96) | Doc: "at the amount sent, not the fee". 00005350: Transfer Amount 1,075.00, Fees + 0.99, Total 1,075.99 | No |
| F3 | Double count (ten WU mails) | Five MTCNs, each with a "ready for pickup" and a "received" mail. Pairs share MTCN 6439829180, 2738632179, 8848946467, 4008433088, 2223294319. WU monthly summaries give an independent total: 3,225 + 2,150 + 2,150 = 7,525 (00005579, 00006117, 00006592) | No |
| F4 | Which bet | Doc: "Domino Delights up to Jan 8, 2025". All five dates fall Jun 3 to Aug 23, 2024 | No |
| F5 | Window | Doc: Sep 2023 to Feb 2. All inside | No |
| F6 | Out of Chase, so excluded ("Anything paid out of Chase isn't in here") | Card 4655 is SVB: 00002502 "MasterCard account ending in 4655 ... Sincerely, SVB Card Services"; Slack C04UEQVDVB7/1719603595.852129 "via company card"; C04UTBZL6AX/1717436652.663349 "yeah, it's credit". Only pull toward Chase: C04UEQVDVB7/1717090779.821489 "using our debit card" | No |
| F7 | Robert's personal money (receipt sender is Robert, home address) | Rule says "we paid". Slack: "via company card" and "I will attempt to create account using Harmony Games" (C04UEQVDVB7/1717090822.933189). No reimbursement record | No |
| F8 | Not a contractor | C04UTBZL6AX/1717622560.592789 "Can you also send Lucas a contractor contract?"; invoices to the Billing list (00005084, 00005340, 00005947 body "WU") | No |
| F9 | A December payment | Calendar "PAY DAY FOR Lucas" Dec 26, 2024 (evt_a99029c9d7175df03f69e6) and invoice 00009022, but no notice after Nov 21 and no WU receipt after Aug. No receipt, so out | No |
| F10 | Already inside Deel | C04UTBZL6AX/1717622581.489819 "we need to set him on Deel I think"; no Deel record of Lucas in Robert's mail; WU is cash outside Deel funding | No |
| F11 | Salience: with the clause gone, the only seeded note naming another route is ENG-2459 "re-sent it through payoneer" | The rule is not limited to noted payees. A run stopping at Payoneer gets 6,450 by not searching | Yes, this is the intended hardening |

The dropped clause carries no fact that decides anything. The Sep 2024 start stays visible in the notices (00007151, Sep 25) and in C04UEQVDVB7/1727147072.731139 "setup IBAN for Lucas, he has to show some 'real' income via bank transfer".

## 2. Identity: unambiguous

The ties are independent:
- Same literal token: ENG-2447 title `[PERSON_NAME_36400]` = SVB "To: [PERSON_NAME_36400] ***6577" (00007151, 00008235, 00009058) = WU "Final Receiver Details / Name [PERSON_NAME_36400]" (00005184, 00005350, 00005489, 00005962, 00006329).
- Name in the mail: "Lucas can now pick up the money" (00005350); "All set. Lucas received the money you sent" (00005198, and the other four received mails).
- Robert forwarded a receipt to the person: 00005350 message 2, robert to lucas@harmonygames.co, body "Invoice paid".
- Slack: C04UEQVDVB7/1717090813.205739 "PERSON_R001 is Western Union"; /1719603220.131689 "2nd half of June's payment to Lucas OK to go?"; /1719603590.685019 "I've been sending it [USERNAME_31819]"; /1719603595.852129 "via company card"; /1719603614.600759 "and he's been sending us invoices", followed by /1719604436.950659 "There is a separate mini game build now".
- Amounts: C04UTBZL6AX/1717622565.116899 "$1075 half a month", /1717622566.922609 "$2150 a month". Same-day: C04UEQVDVB7/1721776655.058739 "I paid Lucas for July" is Jul 23, MTCN 4008433088.
- Payee setup: D04UP2L3E3S/1727215247.242819 "Receiver Name: [PERSON_NAME_36400] ... UKRAINE"; WU receiver address is Ukraine; C076DECEJ90/1717458646.797399 "we can go to Ukraine and visit Lucas".

Other Lucases: one Slack user (U7CADAB457A), one Linear user, one contact, all lucas@harmonygames.co. The rest are not people paid: "Lucas Venture Group" and "Sarah Lucas" on a conference list (00015389, 00015428), Lucasfilm and LucasArts, "Lucas the Spider" (00015581). The receipts cannot be read as someone else's.

Oddity, no effect: the receipts' mobile block shows `[PERSON_NAME_55462]`; the main block has 36400.

## 3. Closed set: yes, one payee

Census over all 16,233 Robert threads (subject, from, body):

| Rail | Result |
|---|---|
| Western Union | 40 threads: 5 transfers, 1 receiver; the rest registration, fraud-review, promo, 3 monthly summaries |
| Payoneer | 2 mails, both "Dixelar sent you a payment request" (00004614, 00007150). Requests, not receipts. Leonard-only receipts are outside "your mail" |
| PayPal, Zelle, Wise | No payment mail (newsletters, the word "wise", getclockwise links) |
| Skrill | Skrillex |
| Remitly, MoneyGram, Xoom, WorldRemit, Venmo, Cash App | 0 |
| Upwork, Fiverr | Mentions only |
| Revolut, Stripe, SWIFT, crypto | No payment to a contractor (subject/sender census, newsletters) |
| Deel | Stated bucket, not a per-person rail |
| Card receipts | Meta ads 63, Unity Ads 7, Google Play 18, ElevenLabs, Notarize, Cogency Global (00003620, $225.31), subscriptions, meals. Vendors, no issue |

Slack-only off-bank items, no receipt in Robert's mail, so out by the rule: ZM animator on card ($5,400, D04UP2L3E3S/1751915734.739489, "it's on credit card" /1751918374.530789, not on the 22 issues); Oleg's Payoneer re-send (C06MXPL9536/1715113013.494939, ENG-2459, stays $0); "I had to paypal a guy" (C03AEB306685/1736370060.277799, not on the 22 issues).

No other contractor has a receipt in Robert's mail. The rule's set is defined by a property of one mailbox, and it has one member. The edit does not open it.

Residual, not new: "contractor" is the only boundary keeping vendor card receipts out. The earlier platform report (`..._1_prompt.md` F17) already settled it ("the other-route receipt rule (contractors only)").

## 4. Findability: reasonable, hard, not a riddle

The doc gives the test: "A notice is where you start, not the last word" plus a rule whose condition is a mail search.
- R1, name in mail, most natural: `[PERSON_NAME_36400]` returns 12 Robert threads including all five receipts. `Lucas` returns 106. The issue title and note hand over both strings. Not tested live: the one run never name-searched a payee, so the tool's handling of a bracketed token is unproven. Body search is proven (event 191 `payoneer` hit Dixelar bodies). Page size is 100, so `Lucas` may need page 2.
- R2, Slack: `Lucas` returns 184 visible hits; the earliest payment hits include "2nd half of June's payment to Lucas OK to go?" and "I paid Lucas for July", and the same result set holds the IBAN message.
- R3, rail list: `"Western Union"` returns 40 threads, but only if the rail is named. Event 177 shows runs can omit it.
- R4, date window: how the run actually got there.

Not a riddle, because the receipts contain the payee's own name and token and 22 payee lookups are what the task already asks for. It is a real population check, and that is the point of the edit.

## 5. Platform /prompt risk

UGT: low. The earlier report (`..._1_prompt.md` F6) settled Lucas as "doc ... + five receipts 'Lucas received the money you sent'", and the latest report (`..._1_prompt-1.md` lines 62, 312) keeps "Lucas +7,525" among traps with a deciding record. The phrase "bank has him" appears in neither report, so no platform reviewer relied on the clause.

Clarity: low. A reviewer may still raise population wording.

Most likely finding, if any: "ENG-2447's notes no longer indicate any payment outside SVB, and the method names no payee or route for 'some other way', so an agent may treat the three notices as complete and report 6,450; the task does not tell it where to look."

Answer: strong on UGT (one rule, one mailbox, one receipt set, no second valid figure). Moderate only if a reviewer treats findability as clarity. The strongest reply is the census above, with the token match and Robert's own Slack.

## 6. Verdict reason

SAFE WITH A SPECIFIC CONDITION. The rule and receipts determine 13,975 without the clause. The census closes the set to one payee; identity is settled several ways. The condition is the dossier and generator cleanup, verbatim doc sentence, no citation of the clause downstream, and a fresh `/injection` + `/prompt` pair.

## Notes for the record

- Brief's five threads (00005198, 00005351, 00005490, 00005963, 00006330) are the "received" mails. They carry the amount (1,075 x3, 2,150 x2) and "Status: Picked up". The fee line is only in the paired "ready for pickup" mails (00005184, 00005350, 00005489, 00005962, 00006329), which are the design's cited receipts. Both are correct.
- Design pointer D04UP2L3E3S/1752481205.011839 does not resolve. The animator is at /1751915734.739489 and /1751918374.530789 (the hardening report already flags T13 pointers).
- Base searches only; WU receipts are base, not seeded, so they survive the SQL change.
