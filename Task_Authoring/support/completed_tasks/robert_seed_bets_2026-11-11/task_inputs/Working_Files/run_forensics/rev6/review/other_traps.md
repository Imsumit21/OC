# Forensics: traps T2-T9, T11-T17 and mechanisms OFF, ORPH, CORR, ALIAS, CLASS, CURR

Run: `06_PreCheck_Trajectory/trajectory.json` (536 events, 0-based, Opus 5.5). SQL is rev6 (75,303 B; same bytes as `run_forensics/rev6/01_Universe_Inject.sql`). Universe normal, clock 2026-02-14 00:00 UTC, persona Robert.

Grading note: the `surface_grader` reds on X3-X9 and the `node_verdicts` BYPASSED verdicts come from a register-join failure on free-text payee labels, not from wrong values (see `surface_adjudication.md`, sections 1 and 6). Every verdict below is read from the sheet write at event 463, the reply at 532, and the four Linear comments at 473-479. RET (T1, T10) is out of scope; only its control is noted.

Sources re-verified directly: hg.py for every base record cited, the rev6 SQL for every seeded record. Where a design note disagreed with the source, the source wins and the disagreement is listed in section 5.

## 1. Result at a glance

| Trap | Mechanism | Verdict | v2 kind (actual call path) | Deciding text is pre-solved at first read? |
|---|---|---|---|---|
| T2 Lucas off-bank | OFF | LEAKED | bulk call carried the answer | Rule yes (doc); fact no |
| T3 Leapblock orphan | ORPH | LEAKED | on_delegation_path | Rule yes (doc); fact no |
| T4 JPMorgan $4,000 | CORR | LEAKED | volume brute-forced, then token join | Rule yes (doc); fact no |
| T5 Node Media alias | ALIAS | LEAKED | first_read (key in the note) | No, but the search key is in the note |
| T6 Lauren Brooks | CLASS | FALSE | same_container | **Yes, conclusion in the note** |
| T7 Martin BGN | CURR | FALSE | first_read, bulk call carried the field | Yes |
| T8 quick numbers | - | FALSE | first_read | Yes |
| T9 Trello plan | - | FALSE | on_delegation_path, decoy never on path | Yes |
| T11 two $3,700 wires | - | LEAKED (no pull) | bulk call carried the answer | n/a |
| T12 Awaiting/Scheduled | ORPH over | FALSE | decoy never on path | Yes |
| T13 card-paid animator | OFF over | FALSE (also not reached) | decoy never on path | n/a |
| T14 4X helper | - | FALSE | same_container | **Yes, conclusion in the note** |
| T15 P&L note | - | FALSE | decoy never on path | Yes |
| T16 Deel spellings | - | FALSE | same_container | **Yes, conclusion in the note** |
| T17 store transactions | - | FALSE | first_read | Yes |

Counts: 5 LEAKED, 10 FALSE, 0 LANDED among the 15 reviewed. All four LEAKED cross-service traps (T2, T3, T4, T5) still needed real work (6 to 15 calls each) and are the only ones that did. T11 passed by default.

Why the platform called it too easy, in one line: of the seven weight-5 slots that passed, X8 was stated outright in a note, X3/X4/X5 are in effect "go find the record this rule describes", and X6 is one hop from a word in the note. See sections 3 and 4.

## 2. Trap by trap

Each entry: what it is, where the run met it, verdict, v2 kind, the pre-solved text, the counter-reading and how it was resolved.

### T2 - Lucas's Western Union payments (OFF, X3, C2, weight 5)

- **What it is.** Natural wrong reading: the notices are every payment, so Lucas cost $6,450. Deciding records: five "your money transfer's been received" mails, threads 00005198, 00005351, 00005490, 00005963, 00006330 (verified: "Lucas received the money you sent"; $1,075 x3, $2,150 x2 = $7,525, picked up Jun 3 to Aug 23, 2024). Decoy: three SVB notices to [PERSON_NAME_36400] ***6577, Sep to Nov 2024 ($2,150 x3) as the whole story.
- **Events.** Doc rule read at 18. Linear note read at 52 ("the bank has him from Sep 2024"). Three SVB wires parsed at 159 and 435 (`[PERSON_NAME_36400] 3 {'DD': 6450.0}`). First deliberate off-bank hunt at 177 (`payoneer OR wise OR paypal OR transferwise OR remitly`) returned noise and did **not** name Western Union; 184 and 191 repeated Payoneer. The break came at 291/292, a search aimed at T4: `after:2024/08/10 before:2024/08/25 (chase OR jpmorgan OR transfer OR wire OR invoice)` returned thread 1808201559428745555, a Western Union pickup notice for Aug 23. It read the receipt at 298/299, then 303: "Found a Western Union receipt", then 304-321 pulled all five. Comment at 475 and sheet row at 463 both give 13,975. It excluded the fee, as the doc said. The founders' "via company card" message (C04UEQVDVB7/1719603595.852129) was never read.
- **Verdict: LEAKED.** Passed because the doc primed the hunt and the T4 date window swept up the Aug 23 receipt.
- **v2 kind: bulk call carried the answer.** A date-window search for another trap carried this trap's first receipt. Lucas's last transfer (Aug 23, 2024) and the JPMorgan wire (Aug 19, 2024) sit in the same two-week window.
- **Pre-solved text.** Doc (f_6feda53b2382c63bf47b25): "If we paid a contractor some other way, it goes in only if a receipt for it reached your mail, at the amount sent, not the fee." ENG-2447 (comment_b13f790bb95e249b8d3a48b1881c0e3a): "that's Lucas, mini games dev. the bank has him from Sep 2024". Both precede any mail search; the rule also pre-resolves the fee question. The run's own comment repeats the note ("Before the bank had him (Sep 2024)").
- **Counter-reading.** "This was luck, so the trap is alive." Partly accepted: the deliberate hunt at 177 missed Western Union, and this was the only collateral hit. It stays LEAKED for this run but is the weakest leak of the four; a baseline run that does T4 differently could plausibly land here. Pointer: 177 vs 291.

### T3 - Leapblock's $33,290 orphan wire (ORPH, X4, C3, weight 5)

- **What it is.** Natural wrong reading: no Processed notice, so the $33,290 never left and Leapblock is $374,654. Deciding record: seeded #leapblock post, C05URGU759U/1770971846.479179 (SQL line 50): "Total 407,944 over 30 wires", "2023 (from 13 Sep, the first one 33,290) 104,868". Corroboration the design expected: Awaiting notice thread 00001577 (verified $33,290, Sep 13, 2023) and Arthur's "Done!" C04UEQVDVB7/1694616951.239909 (verified). Decoy: the Awaiting notice.
- **Events.** Doc rule at 18. About a dozen Gmail calls (nine searches at 178, 186, 192, 193, 200, 205, 212, 226, 238, plus thread reads at 214, 221, 231, 233) found nothing. The run's **first** Slack keyword search, at 243: `received after:2026-01-01`, returned the statement as the top hit (244). Text at 254: "Found a key source". Reconciled by year at 255/256 (2024, 2025, 2026 match the statement; 2023 short by exactly 33,290). Sheet 463, comment 473. The Awaiting notice and Arthur's Done were never read (no event contains that notice id or "33,290" before 244).
- **Verdict: LEAKED.** The trap was live until a Slack search, but the doc told the run to look for this message.
- **v2 kind: on_delegation_path.** The override rule sits in the method doc that delegates to the notices. The fact is in another service and cost about a dozen failed Gmail calls, but the search word `received` is the doc's own word, and the statement is dated the day before the clock, so a recency-sorted Slack search floats it to the top.
- **Pre-solved text.** Doc: "If someone we paid closes out their file with us and tells us what they received, that beats the notices for them." Platform report: "the close-out rule names the exact situation the #leapblock message fills". The statement also names the amount and date of the missing wire, so no reconciliation is needed and the C3 chain (Awaiting notice, Arthur's Done) is decorative.
- **Counter-reading.** "FALSE, because the statement arrived before any Leapblock total was computed (244 before 255)." Rejected: the run could have stopped at the notices, and the Gmail misses show the record was not on the path. The rule pre-solves the logic but not the location.

### T4 - JPMorgan $4,000 is own-account (CORR, X5, C4, weight 5)

- **What it is.** Natural wrong reading: a $4,000 wire in Aug 2024 is a cost. Deciding record: Arthur's mail "Chase records", robert@harmonygames.co/<CAOOpSqA2MTKGlKETvkoKqFfq1MaIktcGcH9cj21BJMAMN4Ok00@mail.gmail.com> (SQL line 67). Decoy: the notice plus Leonard's "can't remember" note.
- **Events.** ENG-2450 note at 58. Notice at 333. Eight searches and channel reads at 287, 289, 291, 337, 338, 348, 357, 370 (`chase`, `4000`, a date window, `chase account`, `JPMorgan`, channel files and history) found nothing. Then 377-379 searched the three services for `3203`; Gmail returned the mail (381); read at 386/387 after one ECONNRESET at 384. Text at 391, sheet 463, comment 479.
- **Verdict: LEAKED.** Correct on persistence: the account suffix was the join key and the run got to it last.
- **v2 kind: volume brute-forced, ending in a token join.** Not same_container (Linear vs Gmail). The `***3203` token is in the notice, in the issue description ("account ending 3203"), and in Arthur's mail.
- **Pre-solved text.** Doc: "Money we moved between our own accounts isn't spending, no bucket for that." ENG-2450 (comment_10121682aae484f81a11f3f8b3e0ee94): "I approved this one in Aug 2024 but I can't remember what it was for", the only "unknown" note of the 22, so it acts as a beacon. Arthur's mail states the conclusion: "That was our own Chase account, I sent it over to put the money back after Carta's renewal came out of Chase. So it never left the company." The platform quoted this as "Blake's email names the account and amount".
- **Counter-reading.** "This is the one correction in another service, so it bit." Rejected as a miss: it cost about 15 calls but the run reached it and the wrong answer never reached the sheet.

### T5 - PERSON_4419 LLC is Node Media (ALIAS, X6, weight 5)

- **What it is.** Natural wrong reading: a token LLC on the bank is a build vendor. Deciding records: C04UEQVDVB7/1735854841.070019 "This is for closing our account with Node Media LLC" (verified) and the invite text "Harmony Games <> Node Media UA Sync". Invoice mail (verified, thread 00008689) carries "Sept - $1,428.57". Decoy: the Build-by-date default.
- **Events.** Note at 46. Text at 391: "Now identifying PERSON_4419 LLC". 392 (`16,428.57`) and 393 (`invoices`) found nothing naming the LLC; 399 (`close after:2024-12-01 before:2025-01-20`) returned the Node Media line at 400. 407/409 got the UA Sync invite. Text at 406 and 414. Sheet 463 as Marketing with the correct DD amount. The invoice mail was never opened.
- **Verdict: LEAKED.**
- **v2 kind: first_read (key in the note).** Note ENG-2444 (comment_7453d8e60a3625923294c54e36a8667d): "one payment when we closed the account, Jan 2025" supplies the search word `close` and the window. The decider is one hop away. The pseudonym token in the issue title announces that the name is unresolved, so the decoy never exerted any pull.
- **Pre-solved text.** Doc's bucket line: "Marketing is anything made or bought to get installs (ad networks, agencies, ad creative, playables, trailers)". The fact that Node Media is an agency is not pre-solved but is one calendar title away.
- **Counter-reading.** "It's an alias trap that held, since the run had to search." Rejected as a miss: the alias took two searches, both built from words in the note.

### T6 - Lauren Brooks is Marketing (CLASS, X8, weight 5; feeds B2, B3)

- **What it is.** Natural wrong reading: a monthly contractor is build cost. Designed decider: contract f_20a0df3860bb5731d22f07, Exhibit A (verified Robert-visible; "user acquisition: run and optimize paid UA for Telegram, manage budgets, creatives, and funnels", one of five listed services).
- **Events.** All three notes returned in one call at 67/68. Sheet row 463, Marketing, 500 ZM and 1,000 CF. **The contract and contact row were never touched** (no event contains either id).
- **Verdict: FALSE.** The conclusion is in the note at first read.
- **v2 kind: same_container.** The contractor reading ("the contract I sent out in Oct, $500 a month") and the conclusion come back in the same `linear_list_comments` call.
- **Pre-solved text.** ENG-2455, comment_990674712ad0127e26f780eadb5418ea: "her contract had her running our paid UA on telegram, so she's marketing, not build". Rev6 added this comment; it is absent from rev4. It answered a /prompt finding that no persona-visible record decided her bucket (`1_prompt.md` lines 98-118). The manifest still says "only the contract says what the work was".
- **Counter-reading.** "The note is not the resolver, the contract is." Rejected: the run never opened the contract and used the note verbatim.

### T7 - Martin's BGN 1,999 (CURR, X9, weight 3)

- **What it is.** Natural wrong reading: every notice is USD, so $1,999 is build cost. Deciding records: the notice "Amount: 1,999.00 BGN" (verified, thread 00015809 message 2) and "did you handle Martin's laptop?" C04UEQVDVB7/1761844454.096829 (verified, never read).
- **Events.** Doc at 18 and note at 66 were read before the parser was written at 151 with a currency group `([A-Z]{3})`. Printed at 159. Filtered USD at 434. Sheet 463: Company column "BGN 1,999".
- **Verdict: FALSE.** Rule and bucket were read before the data.
- **v2 kind: first_read; bulk call carried the field.** "A parser built for USD drops or mis-adds it" never happened because the parser was written after the rule.
- **Pre-solved text.** Doc: "Anything not paid in dollars stays in its own currency next to the line. Don't add it to a dollar total." ENG-2454 (comment_e89f05a3984064bdb00bc2b1fe6ffee2): "paid him direct for his laptop, not through Leapblock". Rev6 changed this note from "for this one" to "for his laptop"; with the doc's word "equipment" it settles the Company bucket.
- **Counter-reading.** "A careless parser would still miss it." True but untestable here: the parser came after the rule.

### T8 - Leonard's quick numbers (stale summary)

- **What it is.** Natural wrong reading: $985K/$609K/$74K are build cost. Records: sheet f_3304033843904a426f3c00 row "All USD notices, by date ... quick pass", deck f_a4b3c4287a4314d8e532e1. Both verified in the run and the SQL.
- **Events.** Ask read at 9. Doc read at 18, before deck 22 and sheet 26. At 434/435 the run used the quick numbers as a checksum on its 132-notice parse; 446 records the exact match. Reply at 532 gives the change.
- **Verdict: FALSE.** The correction was met before the claim. The ask itself asks "what changes on the deck", and the record is self-labelled as a quick pass.
- **v2 kind: first_read.** Side effect worth noting: the stale figures gave the run a free validation of its parse.
- **Pre-solved text.** Slack ask 1770945859.212469: "my quick numbers are on that sheet and on the draft deck". Doc: "A notice is where you start, not the last word."
- **Counter-reading.** None held up: nothing in the run treated these as the answer.

### T9 - Trello quick plan

- **What it is.** Natural wrong reading: the board's plan is the method. Record: Trello card 698e55f9af74d68d679de7b3 (SQL line 53).
- **Events.** Doc at 18. No Trello tool was called in the run.
- **Verdict: FALSE.** The decoy was never on the path; the doc retires it in its opening.
- **v2 kind: on_delegation_path, decoy never on path.** This is the `hardness_v2_check` SAME_PLACE flag, confirmed from the run.
- **Pre-solved text.** Doc: "It replaces the quick plan I left on our board."
- **Counter-reading.** "Fairness needs the doc to name what it replaces." Accepted as the reason it exists, not as evidence the trap works.

### T11 - two $3,700 Leapblock wires, Aug 2025 (RET's control)

- **What it is.** Natural wrong reading: 2025-08-01 and 2025-08-29, both $3,700, are duplicates. Records: both in the notice list at event 159.
- **Events.** Parsed at 159; year totals at 255/256 show 2025 = 62,950, the statement's figure. Both kept (sheet 463). Nothing in the run flagged them.
- **Verdict: LEAKED, with no pull.** The decoy is on the path but summing is the default, and the statement independently confirms the year.
- **v2 kind: bulk call carried the answer.** Note for the RET analysis: this is the control, and it passed.
- **Pre-solved text.** None. Nothing needs saying because no one is tempted.
- **Counter-reading.** "Passed by accident, not by judgment." Agreed, and that is the point: a duplicate-looking pair with no reason to doubt it measures nothing.

### T12 - Awaiting and Scheduled notices (ORPH over-application)

- **What it is.** Natural wrong reading: they are payments. Records: Awaiting and Scheduled notices (130 and 40 in Robert's mail per the design and platform report section 5; hg.py's 672/312 are all-mailbox hits).
- **Events.** Query at 79/89 was `subject:"Payment Processed"`, the doc's phrase. At 200/208 the run counted 306 non-Processed SVB ids and read none. Awaiting snippets appeared incidentally at 222 and 294.
- **Verdict: FALSE.** The natural query excludes the decoy.
- **v2 kind: decoy never on path.**
- **Pre-solved text.** Doc: "SVB's Payment Processed notices are the one place I know with a line per payment".
- **Counter-reading.** "Run 200 could have mis-added them." It read none of them.

### T13 - the card-paid ZM animator (OFF over-application)

- **What it is.** Natural wrong reading: the $5,400 agreed for the animator goes in like Lucas. Actual records: DM D04UP2L3E3S 2025-07 lines 656 and 658 ("$5400 for 9 characters", verified) and later lines; "it's on credit card" per `plan/research/sc1_truth_table.md`. No receipt exists.
- **Events.** None. No event contains "5,400", "5400" or the DM.
- **Verdict: FALSE.** The decoy sits in a DM that no natural query reaches. It is also NOT-REACHED as an over-application check: the run gives no signal either way.
- **v2 kind: decoy never on path.**
- **Pre-solved text.** The doc's "only if a receipt for it reached your mail" would have decided it.
- **Counter-reading.** "Not reached, not false." Both apply; recorded as FALSE per the definition (the natural query never returned it) with the not-reached note kept for scoring.

### T14 - 4X proposal helper

- **What it is.** Natural wrong reading: the $500 is a ZM cost by date. Record: ENG-2458, Company.
- **Events.** Note at 74; sheet 463 Company 500.
- **Verdict: FALSE.**
- **v2 kind: same_container.**
- **Pre-solved text.** ENG-2458 (comment_c9765430979a8f4c6c99220e84e8c72c): "$500 for help on the 4X proposal, not one of the three games". The doc's Company sentence uses the same phrase: "anything else that wasn't for one of the three games".
- **Counter-reading.** "It still took reading the note." One call, and the note uses the doc's own words.

### T15 - Leonard's "P&L is accurate" note

- **What it is.** Natural wrong reading: use the P&L. Record: C04UEQVDVB7/1754445622.992119 (verified: "The P&L forecast, including starting and ending balances, as well as the latest figures, are accurate.").
- **Events.** That message was never read. The P&L file appeared in a Drive search result at 247 (for "MotMot") and was not opened.
- **Verdict: FALSE.**
- **v2 kind: decoy never on path.**
- **Pre-solved text.** Doc: "Go by the bank. SVB's Payment Processed notices are the one place I know with a line per payment, and what the banks say is our ground source of truth." That phrase comes from Leonard's real message at 1754445718.724799, so the base-data decoy and the seeded rule cite the same conversation.
- **Counter-reading.** None held up.

### T16 - second Deel spelling

- **What it is.** Natural wrong reading: `[ORG_NAME_0057], Inc.` on ***8380 is another payee. Records: notices (both spellings on ***8380); ENG-2438.
- **Events.** Note at 34, before the notices. Map at 434: `'Deel, Inc.':'Deel','[ORG_NAME_0057], Inc.':'Deel'`. Sheet row 463, Deel summed.
- **Verdict: FALSE.**
- **v2 kind: same_container.**
- **Pre-solved text.** ENG-2438 (comment_4b5619299256933257ec311bccab35d3): "SVB shows it under two spellings, same account".
- **Counter-reading.** "The shared account number would have settled it anyway." Yes, so it would be an easy call even without the note.

### T17 - store transactions vs daily revenue

- **What it is.** Natural wrong reading: store transactions are revenue. Records: REVENUE_DAILY vs STORE_TRANSACTIONS.
- **Events.** Catalog at 416, describe at 421, sum at 423.
- **Verdict: FALSE.**
- **v2 kind: first_read.**
- **Pre-solved text.** Doc: "What each game brought in is its lifetime revenue from the warehouse's daily revenue table, as recorded."
- **Counter-reading.** None held up.

## 3. Mechanisms

| Mechanism | Nodes | Run outcome | Rule's control and result | Over-application probe | Verdict |
|---|---|---|---|---|---|
| OFF (A17) | T2, C2, T13 | Lucas 13,975 | Graham Porter ZM 5,000 Build, correct | off_over (animator): not reached | LEAKED via T2 |
| ORPH (A13) | T3, C3, T12 | Leapblock 407,944 | Eveline Art 93,171.50 by notice, correct | orph_over (Awaiting): decoy never read | LEAKED via T3 |
| CORR (A11) | T4, C4 | JPMorgan $0, no bucket | Singular kept at Company 31,250, correct | corr_over: did not fire | LEAKED via T4 |
| ALIAS (A7) | T5, C5 | Node Media Marketing | Adjoe Marketing, Leapblock Build, correct | alias_over: did not fire | LEAKED via T5 |
| CLASS (A15) | T6, C6 | Brooks Marketing | Graham Porter Build, correct | class_over: did not fire | FALSE (note states it) |
| CURR (A10) | T7 | Martin BGN 1,999 Company | Lauren Brooks $500 USD, correct | curr_over: did not fire | FALSE (rule in doc) |

RET's control: Leapblock's two $3,700 wires (Aug 1 and Aug 29, 2025) were kept, and 2025 reconciled to the statement's 62,950 at events 255-256.

All controls passed and no over-application fired, but these controls were easy: each is an unremarkable row with nothing that would invite the wrong move.

## 4. Weight-5 surface slots that passed

Values checked against event 463; B1 and X1 failed through RET and are out of scope here.

| Slot | Passed value | Hand check | What made it easy |
|---|---|---|---|
| X3 Lucas | DD 13,975 | Yes | Doc rule named the exception and the fee handling; note marked the gap ("the bank has him from Sep 2024"); the first receipt came from the T4 date window (291) |
| X4 Leapblock | DD 337,594 | Yes | Doc rule named the situation; first Slack keyword search hit it; the statement carries total, amount and date |
| X5 JPMorgan | None/no cost | Yes | Doc rule; note was a beacon; token `3203` joins notice to Arthur's mail, which states the conclusion |
| X6 Node Media | Marketing | Yes | Note's word "closed" plus the date gave the search; "UA Sync" title; bucket line lists "agencies" |
| X8 Brooks | Marketing | Yes | Note states "so she's marketing, not build" |
| B2 ZM build | 544,433.44 | Yes | Notice sum by date with the doc's windows, minus Marketing and Company; only CLASS touches it, and that was pre-solved |
| B3 CF build | 72,685.61 | Yes | Same; only CLASS touches it |

The arithmetic slots pass whenever the classification slots do, so none of them adds independent difficulty.

## 5. Discrepancies between design notes and the source

| Item | Design says | Source says |
|---|---|---|
| T6 discovery_order | "only the contract says what the work was" | Rev6 comment_990674712ad0127e26f780eadb5418ea states the bucket |
| T13 base_pointer | C04UEQVDVB7/1719603590.685019 | That message is Robert in the Lucas thread ("I've been sending it [USERNAME_31819]"). The animator is D04UP2L3E3S 2025-07 lines 656-663 |
| T11 base_pointer | robert@harmonygames.co/1795282860741136988 | That is a MotMot notice. The T11 pair is two Leapblock notices (Aug 1 and Aug 29, 2025) |
| T3 discovery_order | "channel runs read only by name" | The run found it by keyword search, via the doc's verb |
| v2 tool SAME_PLACE | 1 flag (T9) | Only traps with `version_records` are checked, so T6, T14 and T16 (same_container in practice) cannot be flagged |

## 6. Ten places where a conclusion is stated instead of left to be derived

Ranked by weight-5 impact, then by how early the agent reads it. "Reads at" is the first event.

| # | Where | Exact text | Reads at | Decides |
|---|---|---|---|---|
| 1 | ENG-2455, comment_990674712ad0127e26f780eadb5418ea | "her contract had her running our paid UA on telegram, so she's marketing, not build" | 68 | X8; moves $1,500 out of B2 and B3 |
| 2 | Doc f_6feda53b2382c63bf47b25 | "If someone we paid closes out their file with us and tells us what they received, that beats the notices for them." | 18 | X4, B1; its verb is the search word that found the statement |
| 3 | Doc | "If we paid a contractor some other way, it goes in only if a receipt for it reached your mail, at the amount sent, not the fee." | 18 | X3, B1; also settles the fee |
| 4 | ENG-2447, comment_b13f790bb95e249b8d3a48b1881c0e3a | "that's Lucas, mini games dev. the bank has him from Sep 2024" | 52 | X3; states the off-bank gap |
| 5 | Doc | "Money we moved between our own accounts isn't spending, no bucket for that." | 18 | X5, B1 |
| 6 | Doc, bucket sentence | "Marketing is anything made or bought to get installs (ad networks, agencies, ad creative, playables, trailers)" | 18 | X6 once the alias resolves |
| 7 | ENG-2459, comment_3906b5b40dfcdabdc83381f0060bac82 | "that wire came back the same day, I'd already re-sent it through payoneer" | 76 | Oleg $0; with the doc's "unless one of us has said the money came back" |
| 8 | ENG-2454, comment_e89f05a3984064bdb00bc2b1fe6ffee2 | "paid him direct for his laptop, not through Leapblock" | 66 | X9 Company bucket |
| 9 | ENG-2458, comment_c9765430979a8f4c6c99220e84e8c72c | "$500 for help on the 4X proposal, not one of the three games" | 74 | T14, B4 |
| 10 | ENG-2443, comment_7599b70122403a49a2c3a5539bbd36e6 | "attribution tool, not one game" | 44 | Singular on the Company line, B4 |

Also pre-solved, lower impact: ENG-2438 "SVB shows it under two spellings, same account" (S1); doc "Anything not paid in dollars stays in its own currency next to the line." (X9); doc "It replaces the quick plan I left on our board." (T9).

Reading for the rework: items 1, 4, 7, 8, 9, 10 and the ENG-2438 line are person-level conclusions in notes (Linear comments read in bulk at 33-76). These can be taken out of notes without touching the method. Items 2, 3, 5, 6 are the doc's rules and are prompt-incorporated: they are the method, so the question there is how much of the case they spell out, not whether they stay. Item 1 was added in rev6 to answer a /prompt finding; any rework must keep a persona-visible record that decides Brooks, or that finding returns.
