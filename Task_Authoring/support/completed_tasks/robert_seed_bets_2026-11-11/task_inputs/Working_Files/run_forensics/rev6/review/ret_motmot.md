# RET review: MotMot returned wire, Opus 5.5 pre-check (rev6)

Run: `06_PreCheck_Trajectory/trajectory.json` (536 events, 0-based). Universe: normal, clock 2026-02-14 00:00 UTC. Persona: Robert.
Sources are the records unless marked otherwise. Design notes were used only to find the records. They are not evidence.

## Verdict

**LANDED (genuine, fair).** The run's MotMot 32,160 is wrong and our 28,128 is right. The platform's 963,374.64 is wrong and our 959,342.64 is right.

Parts 1 to 3 of the test hold. Part 4 holds against our key, but it failed in practice against the platform's `/hardness` evaluator, which took the wrong total as correct. That exposure is on the evaluator's side and is not a confound of the run's error (see F).

## A. Evidence chain

Every record below is base data. The SQL adds no Slack or mail text on this point. In `01_Universe_Inject.sql`, "returned", "wrong account" and "resubmit" have no hits, "came back" appears only in the ENG-2459 note, and "motmot" appears only in the ENG-2442 comment.

| When (UTC) | Record | Text | Robert sees it |
|---|---|---|---|
| Apr 1, 2024 | Gmail `robert@.../1795166906688019939` | "Invoice: Contractor [PERSON_NAME_1900] March 2024", one invoice, Beneficiary Bank "BANCO DE AMERICA CENTRAL,S.A." | yes |
| Apr 1 | Gmail `robert@.../1795182296548841984` | "Recipient Created", "BANCO DE AMERICA ***8605", created by Arthur | yes |
| Apr 2 (Apr 3 03:32Z) | Gmail `robert@.../1795282860741136988` | "Payment Processed", "To: BANCO DE AMERICA ***8605 Amount: 4,032.00 USD Transaction Date: Apr 02 2024", Ref 20240930265900 | yes |
| Apr 5 14:26 | Gmail `leonard.hayes@.../1795505181532693167`, "SVB Go ... Wire return", to Leonard only | "the wire transfer detailed below has been returned. Your case reference number is (386307)... Beneficiary Name: BANCO DE AMERICA ... Wire Date: 4/2/2024 ... Returned Amount: 4,032 USD ... Return Reason: BENEFICIARY ACCOUNT INVALID ... The returned funds will be credited to your account today." | **no** |
| Apr 5 15:32 | Slack `C04UEQVDVB7/1712331142.975829` (Leonard, image IMG_5948) | "This wire didn't go through" | yes |
| Apr 5 15:36 | `C04UEQVDVB7/1712331372.614469` (Arthur, +1 from Leonard) | "thats the motmot one?" | yes |
| Apr 5 15:40 | Gmail `robert@.../1795509850966005840` | "Recipient Modified", "BANCO DE AMERICA ***3341" | yes |
| Apr 5 15:41 | `C04UEQVDVB7/1712331718.859679` (Arthur, +1 from Leonard) | "I think I messed up the bank account number. Fixed up and resubmitted the payment." | yes |
| Apr 5 16:02 | Gmail `robert@.../1795511257876658998` | "Payment Processed", ***3341, 4,032.00 USD, Transaction Date Apr 05 2024, Ref 20240960894200 | yes |
| Apr 12 06:03 | `C04UEQVDVB7/1712901800.684259` (Leonard) | "this is money returned to us because Blake put the wrong account number to pay up [PERSON_NAME_24716] and bank returned our money" | yes |
| Apr 12 06:03 | `C04UEQVDVB7/1712901837.860709` (Robert) | "should be an expense reimbursement" | yes |
| Apr 12 06:09 | `C04UEQVDVB7/1712902156.421669` (Robert) | "When you categorize the returned wire transfer, you'll want to select the expense account you used when you recorded the expense transaction. This will reduce the balance of the expense account in your P&L..." | yes |
| Jan 15, 2025 | `C04UEQVDVB7/1736978214.260099` (Arthur) | "Just put the MotMot payment into SVB. Needs approval. [PERSON_NAME_24716] worked 4 extra days OT for us in Dec thus the $4032" | yes |

**Is it really a return?** Yes. The bank's own notice names this wire, this date and this amount, and gives an invalid account as the reason. Leonard said the same in Slack a week later, in his own words. Arthur admitted the cause within minutes of the alert.

**Identity.** The Apr 12 message uses a redacted name, not "MotMot". Three things tie it to MotMot:
- the same token [PERSON_NAME_24716] appears in Arthur's Jan 2025 MotMot payment message;
- the "thats the motmot one?" exchange of Apr 5, which Leonard +1'd;
- across all 132 Processed notices in Robert's mail, BANCO DE AMERICA is the only payee with two account suffixes.

**Was it re-sent as a separate notice?** Yes. The Apr 5 notice has its own reference, its own date and the corrected account. Keeping both counts the March 2024 pay twice. The notices run monthly after that: May 1 (paid for April), Jun 20 ("pay motmot for May", Slack Jun 16 and 17). There was one March invoice.

**Arithmetic.** Recomputed from the 11 Processed notices in Robert's mail:

| Transaction Date | Account | Amount | Bet |
|---|---|---|---|
| Apr 02 2024 | 8605 | 4,032 | DD (returned) |
| Apr 05 2024 | 3341 | 4,032 | DD |
| May 01 2024 | 3341 | 4,032 | DD |
| Jun 20 2024 | 3341 | 4,032 | DD |
| Jul 19 2024 | 3341 | 2,688 | DD |
| Jul 29 2024 | 3341 | 2,688 | DD |
| Oct 01 2024 | 3341 | 5,184 | DD |
| Oct 31 2024 | 3341 | 3,168 | DD |
| Dec 02 2024 | 3341 | 2,304 | DD |
| Jan 21 2025 | 3341 | 4,032 | ZM |
| Feb 27 2025 | 3341 | 4,896 | ZM |

DD gross 32,160, less 4,032 = **28,128**. ZM 8,928. Net total 37,056. 963,374.64 − 4,032 = **959,342.64**. Our truth holds.

## B. Reach

- `C04UEQVDVB7` is **#admin_foundersonly**: private, not archived, 7 members, including `EMPLOYEE_0016_SLACK_ID` (Robert). It is not the separate #founders channel.
- `persona_view can-see robert` returns YES for all six Slack records and the four Robert Gmail records checked, and **NO** for Leonard's wire-return notice.
- The run read this channel without error: events 357 and 370 (`slack_conversations_history`), result at 371. So the tool reaches the channel.
- Robert was in the Apr 12 conversation himself.

## C. Incorporation

Delegation:
1. Prompt: "He laid out how he wants it counted and how it should look."
2. #winddown `C0ADGSZKR3R/1770945821.640039` (Leonard): "how I want it counted is in the doc I just wrote, Angel note: how to count the money."
3. Doc `f_6feda53b2382c63bf47b25` (shared with Robert; read by the run at event 17, result 18): "What counts is money that left the company and stayed out. A notice is where you start, not the last word. Take a notice as paid unless one of us has said the money came back."

The doc has no time limit and names no channel. Leonard's Apr 12 message is literally one of them saying the money came back. The doc's opening paragraph ("Go by the bank... what the banks say is our ground source of truth") is the general rule. The second paragraph limits it for this exact case.

**ENG-2442.** Nothing in the issue points to the return.
- Description: "On the SVB notices as BANCO DE AMERICA, accounts ending 3341, 8605."
- Comments: Arthur "that's MotMot, paid by the day. SVB shows their bank's name"; Leonard "I always just approved what Blake put in"; Arthur "one of their engineers on our team, I set it up with them in early 2024"; Arthur "I waited for his day count each month before running it...".
- Only the two account suffixes are a cue, and only indirectly. Contrast ENG-2459, where Leonard wrote "that wire came back the same day, I'd already re-sent it through payoneer".

## D. Findability

**Ordinary searches.** I replicated the live `slack_search_public_and_private` rules from its description (bare words ANDed as substrings, newest first, default limit 20) over the ~404,500 messages Robert can see. The SQL adds no hits. Ranks are approximate (see Limits).

| Query | Hits | Deciding record, rank | Page 1 at default limit? |
|---|---|---|---|
| `motmot` | 32 | "thats the motmot one?" rank 26 | **No** (needs limit ≥ 26 or a date or channel filter) |
| `motmot in:admin_foundersonly` | 8 | same, rank 8 | yes |
| `wrong account` | 9 | Apr 12 message, rank 7 | yes |
| `bank returned` | 1 | Apr 12 message, rank 1 | yes |
| `returned wire` | 1 | Robert's Apr 12 message, rank 1 | yes |
| `resubmitted` | 14 | Apr 5 message, rank 14 | yes |
| `account number` | 48 | ranks 18 and 20 | yes |
| `returned` | 49 | ranks 36 and 37 | **No** (limit 50 yes) |
| `4032` | 22 by `persona_view` | not the return messages; the amount is not in them | no |
| `4,032` | 0 | none | no |
| `BANCO DE AMERICA` | 0 | none | no |

The amount route and the bank-name route cannot reach the return, because Slack states neither. The payee-name route on its own finds only "thats the motmot one?", and page 1 does not show it. The return's own words ("returned", "wrong account", "resubmitted", "bank returned") do reach it, and a channel-history read for Apr 5 to 12, 2024 reaches it too. Lookup by a word for a return, or by opening the channel, is ordinary work. It is not trivial.

**This run.**
- Slack: 12 searches, 1 replies read, 1 file list, 2 history reads.
  - Searches: events 243 `received after:2026-01-01`, 265 `"for your records"`, 267 `wires after:2025-12-01`, 269 `total after:2026-01-15`, 287 `chase after:2024-08-01 before:2024-09-15`, 289 `4000 ...`, 337 `chase account`, 338 `JPMorgan`, 379 `3203`, 393 `invoices ...`, 399 `close ...`, 407 `"Node Media"`.
  - Founders' channel reads: events 357 and 370, both Aug 2024 windows, for the JPMorgan question.
  - No Slack search names MotMot, the bank, a return or a wrong account.
- Gmail on this question: event 178 `leapblock OR motmot OR ...`, 186 `subject:(leapblock OR motmot OR ...)`, 193 `MotMot` (3 unrelated hits), 205 `subject:SVB (subject:returned OR ...)` (1 unrelated hit).
- Did a result contain a deciding record? No. Grepping the visible results for the deciding text and ts values finds nothing. For spilled results I tested each Slack query's terms and date filters against the four Apr 2024 messages, and none can match. Gmail cannot match because no deciding record is in Robert's Gmail.
- Near miss: event 332 filters the decoded notices for the April BANCO wires, and event 333 prints the Apr 2 ***8605 and Apr 5 ***3341 pair. The issue description already told it "accounts ending 3341, 8605". So the run saw the unexplained pair, and then wrote at event 463 "11 wires across two accounts; none reported back."
- First query that would have found it: at event 193 or 205, the same term in Slack. `motmot in:admin_foundersonly`, or `returned` with the limit 50 it used at 243, 269 and 399. Best single query: `wrong account`, page 1.

## E. Why the platform reviewer missed it

Its text: "Returned payments: no SVB return or reversal notice and no returned-wire message in Robert's mail." That is under section 5, "I streamed all Robert-mailbox Gmail threads". Its R6 rule cites the doc plus the ENG-2459 Linear note, and only for Oleg. Its source list includes #winddown and #leapblock but no founders' channel.

So, by its own report, it checked for returns in Gmail and Linear only. The statement about Robert's mail is accurate. Its conclusion is not, because the doc's test is "one of us has said", not "the bank told Robert".

The evidence is in Slack, which the doc does not name but its words ("one of us has said") point to. The miss is real data: a capable reviewer reading the same doc did not look in the founders' channel. It shows the retrieval is non-trivial. It does not show unreachability, because the reviewer never ran the query. The reviewer's own suggestion (a correction "in another channel saying one Deel or MotMot run bounced") describes what already exists.

## F. Four-part test

| Part | Result | Basis |
|---|---|---|
| 1. Incorporated | PASS | Prompt → #winddown ask → doc sentence (C). Requirement names the class of statement, not the location. |
| 2. Reachable | PASS, with a caveat | Robert is a member; tool works on this channel (event 371); several ordinary searches reach it. Caveat: the bare payee name misses page 1, and amount or bank-name searches miss entirely. |
| 3. Fair readings | PASS | Only 28,128 fits once the record is read; dropping the Apr 5 wire instead of Apr 2 gives the same number; dropping both (24,096) has no support. |
| 4. Grader | **Split** | Our key (X1 28,128; B1 959,342; C1 comment; R1 reply) scores it right. The platform's `/hardness` evaluator used 963,374.64. |

Subclasses:
- **Tool:** no. No error on this path; the search and channel reads worked.
- **Run:** no. Run completed normally, 156 calls, no cut-off.
- **Fairness:** no, but this is the closest challenge (below).
- **Verifier:** real exposure, but not a confound of the run's error. The run got the wrong answer whoever graded it. The evaluator's total is wrong, so the band-1 scoring should be re-examined.

**Strongest case for CONFOUNDED (fairness).** Leonard said he "left what we remember on them" on the issues. Oleg's return is flagged exactly there. Arthur, who made the mistake, wrote three notes on ENG-2442 and did not mention it. A reasonable agent could treat the notes as where founders said what came back, conclude nobody said so for MotMot, and hold that a two-year-old chat aside is not what "go by the bank" meant.

Resolution:
- The doc says "unless one of us has said", not "unless it's on the issue".
- It also says "a notice is where you start, not the last word". "What we remember" is a memory aid, and nothing says it is complete.
- The run did not act as if the notes were complete. It ran Gmail searches for `MotMot` and `returned` (events 193, 205), and it printed the April pair at event 333. It knew to look, it looked in one place, and it wrote a negative ("none reported back") that a Slack check would have disproved.
- "No bank notice means a chat remark isn't enough" fails on the doc's own text: the stated test is a founder's word.

**Strongest case for LANDED, tested.** The run read the rule, applied it to Oleg, and saw the pair. That shows the cue worked. Against it: Oleg's note did the work for Oleg, and the run may simply follow notes rather than the rule. Thinking blocks are empty, so motive can't be proved, but the calls support the conclusion either way: it asserted a negative after searching only Gmail.

Note: the proposed `RET: BYPASSED` in `precheck.proposals.jsonl` ("the register has none of the components") is wrong as a fact. The MotMot row is in the event 463 write. This matches the known tracker-decoder problem.

## G. Is the Unique Ground Truth safe?

Yes, conditional on one judgment the doc itself makes. A careful human, knowing nothing of the design, sees two accounts on one payee and the Apr 2/Apr 5 same-amount pair with "Recipient Modified" between them. They follow "one of us has said" into the founders' channel, find "This wire didn't go through", "Fixed up and resubmitted" and "bank returned our money", and subtract once. They reach 28,128 and 959,342.64. Nothing in reach supports another number.

Residual risk: someone who stops at the Linear notes gets 32,160. That is a retrieval miss, not a second valid answer. The amount of the return is stated only in Leonard's notice, so Robert infers it from the wire. Only the full $4,032 fits.

## Limits

- The image contents (IMG_5948, IMG_5949, the Apr 12 screenshot) are not in the export, so I could not read them.
- I did not run the live Slack backend. Ranks are my replication of its description over base message text. Attachment text can add hits (`persona_view` shows 34 for "motmot" against my 32), so ranks could shift by a few. Curly and straight apostrophes differ for "didn't go through"; that query is not relied on.
- Spilled tool results are not in the export. I tested those queries against the records instead.
- The run's thinking blocks have no text, so its reasons are inferred from its calls and notes.
- I could not establish whether the platform evaluator checked anything beyond what its report states.
- `09_Rubrics.json` and `08_Oracle_Events.md` are empty, so there is no rubric yet to confirm how the platform's verifier would score 959,342.64.
