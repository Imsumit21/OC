# Rev1 fork sweep: stockholder close-out (cold reviewer, no answer key)

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal). Task files read: `seed_snapshot.md` only. Everything else came through `hg.py search`.

Result: 3 BLOCKER, 8 MAJOR, 12 MINOR. The holder labels mostly hold up. The blockers are about what goes on the sheet and whether one message is sent or drafted, not about the facts. Two findings (M1, M2) can each change a graded figure or row even though a record does settle them, because the settling record takes several hops to reach.

## 1. Totals

| Figure | Value | How it was reached |
|---|---|---|
| Series Seed outstanding | **3,051,879** | Griffin 2,746,693 + 10 others 305,186. Term sheet "Inputs from ledger" says the same (gdocs 40) |
| Griffin split | II 2,662,255; Side Fund 84,438 | One record only: #executives Jan 14 (`C07C2866011/2026-01 /727`) |
| Common | 6,000,000 | Founders, 2,000,000 each |
| Shares outstanding | **9,051,879** | |
| Live options today | **159,706** | 8 lines with a last day = 55,942; 4 advisor lines = 103,764 |
| Shares plus options today | **9,211,585** | |
| Options at Dec 31, 2025 | **243,757** | 16 lines: 8 at vested = 81,702; 4 staff at full grant = 58,291; 4 advisors = 103,764 |
| Shares plus options at Dec 31, 2025 | **9,295,636** | |
| Directors in office | **Leonard Hayes, Robert** | Collins resigned May 1, 2025; PERSON_4337 resigned Feb 12, 2026 |
| Preferred vote | **Griffin**, 90.0% of Series Seed | II alone 87.2%. Charter "Requisite Holders" is a majority of Preferred (gdocs 312) |
| Goes first | **Vincent Parker**, Feb 21, 2026 | Earliest live last day |

Labels: Nothing 6, Already told 4, Closing 6, Covered 2, Last day 6, Closing and last day 2 (total 26). Issue states: Canceled 6, Done 6, Todo 14. Notes: 14.

Reconciliation check: rebuilding the ledger with only the terminations recorded by Jan 22 gives exactly 268,772, the term sheet's figure. That confirms the four advisor lines at full grant, and it confirms that ES-14 and the Feb 12 terminations were not yet recorded then.

## 2. The 26 rows

"Told" lists the first direct written message found. Carta mail IDs are in `threads/leonard@harmonygames.co_<id>.json`.

| Issue | Holder | Holds today | Last day | Told? | Label | State | Decided by |
|---|---|---|---|---|---|---|---|
| 2438 | Griffin II | 2,662,255 SS | none | Yes, Feb 9 to PERSON_4337 | Already told | Done | Mail 1856675475513544349 /messages/13 |
| 2439 | Griffin Side Fund | 84,438 SS | none | Yes, same mail | Already told | Done | Same; "for a fund, its partner" |
| 2440 | Segerstråle | 50,865 SS + 30,518 opt | none | Yes, Slack DM Feb 9 (see M1) | Already told | Done | `D04UC0UEN2V/2026-02 /0`; gdocs 262, 570 |
| 2441 | Schaeppi | 25,432 SS | none | No | Closing | Todo | Nov 2024 list; no Feb message found |
| 2442 | Bergmann | 25,432 SS | none | No | Closing | Todo | SSP-05; seeded contact PERSON_0693 |
| 2443 | [PERSON_NAME_52949] (PERSON_2260) | 25,432 SS | none | No | Closing (note covers the brothers) | Todo | Mails 1770141224265557526, 1774211155651873582 |
| 2444 | Patrick Lewis | 25,432 SS | none | No | Covered | Done | Same; seeded DM |
| 2445 | [PERSON_NAME_27652] | 25,432 SS | none | No | Covered | Done | Same; seeded DM |
| 2446 | Nebojsa | 25,432 SS + 6,104 opt | none | Yes, Robert Feb 12 | Already told | Done | Seeded mail; ES-11; wire 1773963101399472184 |
| 2447 | Matthew Collins | 25,432 SS + 61,038 opt | none | No | Closing | Todo | SSP-10, ES-9; no Feb message; no Slack DM exists |
| 2448 | TOR Capital Limited | 50,865 SS | none | No | Closing | Todo | SSP-11; Nov 2024 list |
| 2449 | Deepak | 25,432 SS + 6,104 opt | none | No | Closing | Todo | SSP-12; gdocs 262, 295 |
| 2450 | Julia Lawson | 17,802 opt (ES-1) | Mar 31, 2026 | Yes, letter Feb 11 + group DM | Last day | Todo | Carta 1856960433624350836; letter 1856861462411533365 |
| 2451 | [PERSON_NAME_0100] | Nothing (ES-2) | Nov 1, 2024 passed | n/a | Nothing | Canceled | Carta 1808666480668498098 |
| 2452 | Calvin Price | Nothing (ES-3) | Jan 24, 2026 passed | n/a | Nothing | Canceled | Carta 1847333347700620793 |
| 2453 | Claire Morgan | 4,450 opt (ES-4) | Mar 31, 2026 | Yes, letter Feb 11 + group DM | Last day, plus open equity question | Todo | Carta 1856960410709778333; `C51ECE5102ED/2026-02 /1` |
| 2454 | Douglas | Nothing (ES-5, by elimination) | Jan 24, 2026 passed | n/a | Nothing | Canceled | Carta 1847333395311994879 |
| 2455 | Victor Barnes | Nothing (ES-6) | Jul 16, 2025 passed | n/a | Nothing | Canceled | Carta 1830952527208439510 |
| 2456 | Marcus Bennett | 12,875 opt (ES-7) | Apr 30, 2026 | Yes, letter Feb 11 | Last day | Todo | Carta 1856960351896429942; letter 1856861323365646598 |
| 2457 | Owen Baker | 8,477 opt (ES-12) | Apr 30, 2026 | Yes, letter Feb 11 | Last day | Todo | Carta 1856960504234892536; letter 1856860994291529096 |
| 2458 | Martin Walsh | 2,013 opt (ES-13) | Apr 30, 2026 | Yes, DM + letter Feb 11 | Last day | Todo | Carta 1856960563574318616; `D05Q3QAH2QZ/2026-02` |
| 2459 | Vincent Parker | 1,530 opt (ES-14) | **Feb 21, 2026** | No direct message | Closing and last day | Todo, first | Carta 1856960478782792748; resignation 1849344928983425627 |
| 2460 | Brian Foster | 3,391 opt (ES-15) | Mar 31, 2026 | Yes, letter Feb 11 + group DM | Last day | Todo | Carta 1856960532806250145; letter 1856861400116562076 |
| 2461 | [PERSON_NAME_2768] [PERSON_NAME_0011] | Nothing (ES-16) | Jan 24, 2026 passed | n/a | Nothing | Canceled | Carta 1847333318158821452 |
| 2462 | Frederick Stone | Nothing (ES-17) | Jan 28, 2026 passed | n/a | Nothing | Canceled | Carta 1847333272519888206 |
| 2463 | Oliver Brooks | 5,404 opt (ES-18) | Apr 30, 2026 | No direct message | Closing and last day | Todo | Carta 1856960382677662910 |

SS = Series Seed. Per-holder stock for the four advisors is the Nov 2024 figure minus their advisor grant (for example 31,536 − 6,104 = 25,432). The result sums exactly to 3,051,879.

## 3. Findings

### BLOCKER (no record settles it and a graded write differs)

**B1. Do founders go on the sheet?**
- Sunset: "One line per holder of stock or options, with what each holds today and any last day"
- Linear: "one issue per holder on Carta, live or lapsed, founders aside." and "the sheet is what Sunset asked for."
- Reading A: "founders aside" limits Linear only. The sheet is Sunset's list, so it has 29 lines, and the count of holders changes.
- Reading B: the sheet mirrors the 26 issues, and founders appear only in the totals.
- Also undecided under A: which label founders get. None fits, and "Already told" would rise from 4 to 7.
- Moves: row set and "A count of holders by what is owed to them".
- Fix: add to the notes "Founders go on the sheet for the totals only, no label, not in the count."

**B2. Is Covered a sixth label, or a flag on top of Closing?**
- Notes: "Labels for the sheet: Nothing, Already told, Closing, Last day, Closing and last day."
- DM: "Mark those lines Covered on the sheet"
- Sunset: "A count of holders by what is owed to them"
- Reading A: Covered replaces the label, giving Closing 6, Covered 2.
- Reading B: the brothers are still owed the closing. Only the note is shared, giving Closing 8 with a Covered flag.
- Moves: Patrick Lewis, [PERSON_NAME_27652], and the count.
- Fix: "Mark those lines Covered on the sheet in place of a label, and count them as Covered."

**B3. Is the Griffin heads-up sent or drafted, and on which thread?**
- Notes: "Griffin's partner gets a heads-up on the board thread once the sheet shows who holds the preferred vote"
- Set against: "I read and send each note myself" and Trello "Nothing goes out until the sheet is right."
- Reading A: the heads-up is not a holder note. Griffin has none, so the assistant replies once the sheet is right.
- Reading B: nothing goes to an investor unread, so it is a Gmail draft.
- Thread: two exist with the same partner, "board position w/ ..." (May 2025, 1830959847543474636) and "Board position" (Feb 12, 2026, 1856958794180374704). Recency points to the second, and the Feb 9 shut-down thread is a third candidate.
- Moves: sent mail versus draft.
- Fix: "Griffin's partner gets a heads-up, drafted for me on the Feb 12 Board position thread, once the sheet shows who holds the preferred vote".

### MAJOR

**M1. Segerstråle's "told" rests on an unlabelled Slack ID.**
- Sentence: "Told means a written message about the closing, sent to them directly, from me, Robert or Arthur; for a fund, its partner."
- The Feb 9 DM says "Metrics didn’t improve. The most reasonable thing to do right now is to shut down the company we decided." The other party shows only as `PERSON_3335_SLACK_ID`.
- The link takes three hops:
  1. #winddown at 19:26: "pinged [PERSON_NAME_6550] to get guidance on how to wind down properly"
  2. The DM asks exactly that, at the same minute.
  3. The 2023 note ties [PERSON_NAME_6550] to [PERSON_NAME_0090] and Super Evil Megacorp (`C04UTBZL6AX/2023-06 /486`); the DM says "SEMC".
- Reading A: Already told, Done. Reading B: Closing, Todo, and a 15th note.
- Fix: use ENG-2440's planned last-contact comment to say "Slack DM Feb 9". That stays neutral and closes the link.

**M2. Matthew Collins: did their service end?**
- KPMG: "For anyone whose service ended on or before that date, count what had vested; for anyone still in service, the full grant."
- Notes: "If a line's last day has passed, it holds nothing."
- Collins resigned from the board "with immediate effect" on May 1, 2025 (1830959847543474636).
- Reading A (records support it): no Carta termination exists for ES-9; the Advisor Agreement runs until 30 days' notice (gdocs 490); the Jan 22 ledger only reconciles with the full 61,038.
- Reading B: service ended. If counted at vested, about 53,408 (21/24 on the 2-year schedule, from the Jul 21, 2023 agreement date), giving 236,127 and 9,288,006. If treated as lapsed, live options 98,668, today's total 9,150,547, KPMG options 182,719, KPMG total 9,234,598.
- The label does not move; three graded totals do.
- Fix: "For anyone Carta shows as terminated on or before that date, count what had vested; for everyone else, the full grant."

**M3. Does an @here channel post count as told?**
- Sentence: "Told means a written message about the closing, sent to them directly, from me, Robert or Arthur; for a fund, its partner."
- `C05KNDCHAAG/2026-02 /40`, Feb 11: "<!here> per our conversation we’ll be shutting down the company." Oliver Brooks replied in the channel; Vincent Parker is a member.
- Reading A: a channel post is not direct, so both are Closing and last day.
- Reading B: it reached them and Oliver visibly knows, so Oliver is Last day. A note announcing the closing to Oliver would read oddly.
- Moves: Oliver, possibly Vincent, the count, and the note text.
- Fix: "sent to them directly (a channel post or a call doesn't count)".

**M4. "Where no note of its own goes" scope.**
- Sentence: "Where no note of its own goes, say why on the issue."
- Reading A: all 12 issues without a note, including the 6 Canceled.
- Reading B: only the 6 Done, since the sentence echoes "Done where it isn't".
- Moves: 6 Linear comments.
- Fix: "On every issue without its own note, Canceled included, say why."

**M5. Does the sheet go to Sunset?**
- "Share it and the letter with Robert"; "And the sheet goes to you as well as Robert, the rest stands"; "Sunset wants the same sheet for the intake, so nothing changes on order"
- No record says who hands it over.
- Reading A: reply to or share with Sunset. Reading B: Robert and Arthur only.
- This is a BLOCKER if the share list or a Sunset reply is graded.
- Fix: add to the Trello comment "I'll pass it to them myself."

**M6. The KPMG reply has no owner.**
- "Please reply to all by 2/27/2026." and "Thanks, got it. I'll get this to you before the 27th."
- Neither the notes' "What needs doing" nor the Trello card mentions it.
- Reading A: draft it. Reading B: send it. Reading C: out of scope, because "I'll get this to you" is Leonard's own promise.
- This is a BLOCKER unless the prompt names it and says draft or send. I could not see the prompt.
- Fix: one notes line, "KPMG's confirmation too, as a draft reply-all on their thread".

**M7. Formal notice has no source for most rows.**
- Sunset: "How each holder gets formal notice, including any special terms"
- Investors: IRA Notices clause (gdocs 90), with addresses on Schedule A, which I could not read.
- TOR: no post, email fine, two days for overnight courier, copy to Thompson Legal (gdocs 238; 1773160052067710033 /messages/2).
- Option-only holders: I found no notice term.
- The TOR document is titled a draft and ends on "liquidation, dissolution, or winding-up". Leonard calls it the letter "drafted and ... approved" (1775602109531090463). I found no signed copy, so "TOR terms apply" and "lapsed or unsigned" are both honest.
- Fix: give the column a default in the notes, for example "email on file unless a document says otherwise", and add one sentence confirming the TOR letter was signed.

**M8. The notes rely on Carta, but no Carta holdings view exists for stock or advisors.**
- Sentence: "Carta is the record."
- Visible Carta material is 14 termination mails and activity digests. Stock counts and the four advisor lines exist only in the Nov 2024 list, the term sheet, and 2023 documents.
- The Nov 2024 list is the one the superseded notes pointed to ("take the names and numbers from the Nov 2024 owner list"), and its "shares" column mixes stock and options.
- Reading A: reconstruct, as above. Reading B: treat 31,536 as stock, or refuse the list and leave lines blank.
- The sum to 3,051,879 catches A versus B, but only for a reader who checks.
- Fix: add one seeded Carta digest or a Feb 2026 ledger line for ES-8 to ES-11 and the Series Seed total. If that is too revealing, accept this as intended difficulty.

### MINOR

| # | Sentence | Fork and who moves | Smallest fix |
|---|---|---|---|
| m1 | "One row and at most one note per person, handled on their stock if they have any." | Griffin's two funds as one person (25 rows, Already told 3) versus two (Linear, KPMG). "Handled on their stock" could also drop options from the four advisor rows; live options summed from rows would be 55,942 | "One row per Carta holder; show stock and options on it" |
| m2 | "One line per holder of stock or options, with what each holds today" | Vested versus granted for terminated staff, for example Marcus 12,875 or 22,889. Ledger behaviour points to vested | "what each can still exercise" |
| m3 | "a written message about the closing" | Termination letters ("The company is shutting down") as told or not. Only Marcus and Owen depend on the letter alone | "any written message saying we are closing" |
| m4 | "Anything they asked about their holding that we never answered gets answered in their note." | Claire asked Feb 12; Leonard's replies skip it, but the Feb 11 letter's Equity paragraph covers it. Separately, [PERSON_NAME_2768] [PERSON_NAME_0011] raised a Carta exercise problem (1847333990408253969) and now holds nothing, so "their note" does not exist | Add "if they get a note" |
| m5 | "Numbers on there are just what I pasted in, the sheet is the real thing" | "The sheet" could mean Holder list (draft), which is itself copied from Nov 2024. Later notes override | "the sheet will be the real thing" |
| m6 | "the holder sheet comes first" | Edit Holder list (draft) or create a new sheet | Name the file to build in |
| m7 | "the investor email on the Task List" | No Task List found; the Shut Down List canvas body is not readable. The draft itself is findable, so low risk | "the investor email: take my draft..." |
| m8 | "268,772 options outstanding (Jan 22 term sheet)" | Update to 159,706 (today) or 243,757 (KPMG date); "Feb 26" reads as a date or as Feb 2026 | "Feb 2026 Update" |
| m9 | "for a fund, its partner" | TOR's recipient: PERSON_5275 (active contact) or PERSON_0711 (accepted SSP-11). Griffin also has a second Partner, PERSON_4351. "Family" could stretch to the two Griffin funds | Name TOR's contact on ENG-2448 |
| m10 | Sunset: "Directors in office, and who holds the preferred vote" | Decoys: contact card "Independent Director", Q4 2024 consent, Feb 11 notes "consists of themself and" Griffin. Preferred vote could mean the Preferred Director's vote; that seat has been vacant since Feb 12 | Leave as difficulty, or "which stockholder holds" |
| m11 | Term sheet "3,051,879" against Slack "3,051,881 seed preferred issued at closing" | Moves every total by 2; holder lines and "Carta is the record" settle it | None needed |
| m12 | "Order: holder sheet, then the notes, then the letter." | Trello card state afterwards is unstated; Bergmann's address collides, because Solsten COO mail comes from patrick@, which is also Patrick Lewis's address, and the seeded contact settles it | State the card's end state |

## 4. Checked, no fork

- Vincent goes first; "Griffin first" is superseded by "These replace my earlier outreach notes."
- "my list" is the Feb 12 22:17 message (`1770934638.035469`), because it is the one naming the angels.
- Letter dates (Jan 31, and Owen's "January 31, 2025") do not fight Carta's Jan 30, 2026: "as Carta shows it" decides.
- ES-14's Nov 21 date, recorded Feb 12, is covered by "regardless of when recorded".
- Nebojsa = PERSON_3941 = PERSON_3935: ES-11, the wire, and shared threads agree.
- Robert's old-thread reply is the only closing message to an angel in mail. A date scan of Leonard's and Arthur's Feb mail found no other on old threads.
- The sheet goes to Arthur and Robert; the letter to Robert only.
- Vincent's Feb 21 is live at the clock; Frederick's Jan 28 is passed.

## 5. What I could not read or settle

- Binary attachments do not open through the tool. That includes the Dec 17, 2024 Carta cap table xlsx, the Jan 23, 2026 memo, the Nov 2023 board consent PDF, the seed closing set and any signed side letter. Any of these could confirm or contradict my reconstruction.
- Images are unread, including the Carta screenshots in #winddown, as is the Shut Down List canvas body.
- `<REDACTED_FLAGGED_CONTENT>` hides the Feb 4 thread with Frederick and #winddown message 68. Frederick holds nothing, so I expect no effect.
- ES-8 (Segerstråle) and ES-10 (Deepak) IDs are inferred. Digests name only ES-9 and ES-11; amounts come from gdocs 262 and the Advisor Agreements.
- The Griffin split has one source, a pasted summary in #executives.
- "Not told" means no record found. My coverage was Feb 2026 mail by date for Leonard, Arthur and Robert, and all Jan-Feb 2026 Slack. Calls and WhatsApp are outside the records. Robert's Feb file showed no sent mail at all, which I could not explain.
- The hunt for unanswered questions was keyword-based, in English and some Turkish. It cannot prove there are no others.
- The 26 Linear comments and the prompt were not available, so M1, M5 and M6 may already be handled there.
