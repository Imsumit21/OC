# Red team of repairs_draft.md (M1-M5), rev7 candidates

Task: task_inputsS2. Universe normal, clock 2026-02-14 00:00 UTC, persona Robert. All record text below is quoted evidence.
Separated throughout: FINDING (verified against records) and JUDGMENT (mine).

Sources checked: SQL (read only), repairs_draft, the rev6 forensics (calls_part1/2, other_traps, ret_motmot, surface_adjudication), the current platform /prompt and /injection reports, the rev4 /prompt FAIL (lines 98-118, 219, 280), and the base universe through hg.py and persona_view as Robert.

Headline: of the five moves, one is a real hardening (M2, with two conditions), one is a reviewer-visibility fix that should not be counted as hardening (M1), one is cheap and marginal (M5), one is inert (M4), and one reopens the exact rev4 /prompt failure (M3).

## M1 RET (MotMot return): seed a founder record near the clock

**1. Premise.** True. The base evidence is in C04UEQVDVB7 only: /1712331142.975829 "This wire didn't go through", /1712331718.859679 "I think I messed up the bank account number. Fixed up and resubmitted the payment.", /1712901800.684259 "this is money returned to us because Blake put the wrong account number to pay up [PERSON_NAME_24716] and bank returned our money". The /hardness report's section 5 confirms its reviewer checked Gmail and Linear only ("no SVB return or reversal notice and no returned-wire message in Robert's mail"). Contradiction in the draft: its header says "No new payees, issues, rows", but M1 inserts a row.

**2. Unique ground truth.** No new fork on the number. 28,128 and 959,342.64 still follow. Census: "motmot" 34 Slack hits visible to Robert, 3 Gmail, 2 Drive names, 0 contacts; "4032" and "BANCO DE AMERICA" have no Slack hits on the return; nothing in the base contradicts the return.

FINDING, the real defect: "using the engineer's name" has no clean referent. The engineer exists only as tokens: [PERSON_NAME_24716] (113 Slack hits for Robert; the Apr 12 message; Arthur's Jan 15, 2025 C04UEQVDVB7/1736978214.260099 "Just put the MotMot payment into SVB... [PERSON_NAME_24716] worked 4 extra days OT for us in Dec thus the $4032"), [PERSON_NAME_0550] (C04UTBZL6AX/1709066364.748849 "The MotMot guys want to know if we are ok if [PERSON_NAME_0550] only does 3 days a week"; C04UEQVDVB7/1735240619.835039), and [PERSON_NAME_1900] on the invoice mail. ENG-2442 names no one ("one of their engineers on our team"). A seed naming a token depends on a single base join (/1736978214). NB-12 ("Don't grade a vendor or tool that a record names only as [PERSON_NAME_...]... Safer: use a record that spells out the name") applies by analogy, and Clarity is exposed if the reviewer can't resolve the token.

**3. Coherence, and placement.** Thread-parent census for near-clock founder threads:
- #winddown C0ADGSZKR3R has exactly one replied thread in the last days: 1770922731.444009 (Leapblock ~$600 goodwill, 1 reply). Unrelated to MotMot.
- Leonard's seeded asks 1770945821.640039 and 1770945859.212469 have reply_count 0. A reply there is a same-thread correction on the delegation path (goal rule 4 says same-thread corrections don't work) and would be read, plus it needs reply_count handling on the seed.
- C04UEQVDVB7's Feb 2026 tail is Helpshift (top-level, no threads). No related parent exists anywhere.

So the "thread reply under a related existing post" candidate has no valid parent. Do not use it.

Named placement that passes: a **top-level message in #admin_foundersonly C04UEQVDVB7, author EMPLOYEE_0025 (Arthur) or EMPLOYEE_0038 (Leonard), dated between 2026-02-13 00:05Z and 09:00Z**. It passes because:
- members include EMPLOYEE_0016/0025/0038 (channel listing checked), and the three founders are not among the Feb 11 leavers (NB-1);
- the channel's last base message is 2026-02-11T00:41Z, and any time before 2026-02-13T10:03Z is inside the Slack export window (NB-6);
- it is the same channel as the Apr 2024 exchange, so the "came back" statement is not a new location;
- it is not in #winddown, and the run's reads of this channel were Aug 2024 windows only.

Alternate: DM D04UP2L3E3S (Leonard and Robert, last base message 2026-02-12T16:36Z). Thread placement: none passes.

**4. Harder?** FINDING: The run never reached the return by any path: 12 Slack searches, none on MotMot, wire or return. Gmail `MotMot` (193) and `returned` (205) missed. The move does not touch this. It adds a carrier. It can only make the trap equal or easier to find. A near-clock date is the risky dimension: the run's Slack hunt used date-filtered queries `received after:2026-01-01` (243, limit 50) and `total after:2026-01-15` (269, limit 50), and that recency is how it found the Leapblock close-out at 243. Whether the seed surfaces depends on wording; the draft's phrase "wire... came back" would not match `received`, `wires` or `total`, but a fresh run that searches Slack for recent "wire" or "came back" text will float it to the top.

JUDGMENT: M1 is a reviewer-visibility fix for a band-1 scoring error, not hardening. Label it so. The stated catch-rate target ("a third to two thirds rather than about zero") has no data behind it: n=1, and the run shows no searches at all in the relevant direction.

**5. Fairness.** Rule incorporated: doc "Take a notice as paid unless one of us has said the money came back." The seed improves fairness. Reachable as named above.

**6. /prompt risk.** Medium if a token is used (Clarity); low if the record lets a reader connect it to the MotMot line without a token, as Arthur's existing Jan 2025 style does. Cross-service coherence is fine if not threaded. Add a reason for the timing or it reads as authoring.

Verdict: **KEEP as a visibility fix, modify placement and identity.** Not a hardening move; do not count it as one.

## M2 CORR (JPMorgan $4,000): hedged wrong recollection

**1. Premise.** True. comment_10121682aae484f81a11f3f8b3e0ee94 is the only unknown note among 22; all others state a role. Arthur's "Chase records" mail (2026-02-13T16:26:44Z) is unchanged.

**2. UGT.** Arthur's mail is decisive. It is not a two-founders standoff:
- the mail states the fact and the actor: "the $4,000 to JPMorgan ***3203 on the SVB notices in Aug 2024 was me. That was our own Chase account, I sent it over to put the money back after Carta's renewal came out of Chase. So it never left the company.";
- it is later than the note and Leonard answers it: "ah that's the one I couldn't place, thanks";
- independent base corroboration in Robert's mail: Recipient Created robert@harmonygames.co/1807850387608462682 "Recipient Name: [ORG_NAME_2452] ***3203 Created by: Arthur", Aug 19, 2024 20:48:01Z, then Slack C04UEQVDVB7/1724100562.903529 Arthur "payment started in SVB. Please approve"; Leonard's "done" 1724100962.787409 matches the note's "I approved this one".

Census: any record of a contractor advance in Aug 2024? `advance` in Slack: 351 Robert-visible hits; every hit dated Jul-Sep 2024 is game text ("advanced tile") or "in advance", none about money. No Gmail or Drive record of an advance. The recollection is uncontradicted by the base except by Arthur, and unsupported by it. It holds only because it is hedged and framed as memory.

The note fits a pattern that makes it convincing: ENG-2442 says "SVB shows their bank's name" for a contractor, so "JPMorgan ***3203 is a contractor's bank" is plausible.

**3. Coherence.** Timeline holds: note 2026-02-13T00:26Z, Arthur 16:26Z, Leonard 17:08Z, all before the clock. Condition: Leonard's reply "the one I couldn't place" only stays true if his note is genuinely uncertain. A flatly stated advance breaks it.

**4. Harder?** Yes, but less than the draft suggests. In the run, "can't remember" caused about 15 calls and a late token join (`3203` at 378). With a plausible account, some runs will stop; that is a real change in pull. The same search still gets there: `3203`, `JPMorgan`, `Chase`, or the OR query at 305 that already surfaced the thread. Keep the note's date honest: "Aug 2024" stays in the note and is the window that swept in the Western Union receipt at event 291, so the note does not close the OFF leak and, if it names "a contractor", may send a run into contractor Gmail searches that find Lucas directly.

JUDGMENT: M2 is the only move that creates a real wrong source that a run can follow. Part 4 of the guide ("a caveat Opus can see") is the risk: a hedge reads as a caveat, so word the pull as memory, not as a flagged question.

**5. Fairness.** Yes. Rule in the doc; correction is in Robert's inbox, one day before the clock, reachable three ways.

**6. /prompt risk.** Low. Likely finding if any: Clarity (founders disagree). Covered by Arthur's authority and Leonard's reply. Surface issue: X5's accepted values include "" and "-", so a row can pass with the bucket left blank, against goal rule 4 ("no row may pass by doing nothing"). The draft's "accept a none/own-accounts bucket" fix widens this; it needs to exclude blanks.

Verdict: **KEEP, modify.** Keep the hedge and Leonard's reply consistent, and close the do-nothing pass on X5.

## M3 CLASS (Lauren Brooks): delete the comment, leave the contract to settle it

**1. Premise.** True. comment_990674712ad0127e26f780eadb5418ea states the conclusion. Rev6 added it after the rev4 fail. The contract was never opened in the run.

**2. UGT.** Contract f_20a0df3860bb5731d22f07 is Robert-visible (shared_with). Exhibit A in full: "plan, launch, and scale Telegram distribution for [ORG]... Strategy: define growth plan, target segments, positioning, and monthly goals. work with the product team to advise on what growth features to implement. Setup: create and optimize Telegram channels, bots, flows, and link tracking. Content and community: own the content calendar, post cadence, moderation, AMAs, and retention loops. Creator and partner ops: source, brief, and manage creators and affiliates. user acquisition: run and optimize paid UA for Telegram, manage budgets, creatives, and funnels."

Doc Marketing sentence: "Marketing is anything made or bought to get installs (ad networks, agencies, ad creative, playables, trailers)"; Build: "the team on Deel plus the studios and freelancers who made the games".

Fork, with each side's text:
- Marketing: "distribution", "growth plan", "user acquisition: run and optimize paid UA for Telegram". #company-internal C05KNDCHAAG/1760125440.959149: "lead our Telegram distribution strategy... There is some technical work to enable this, which [Arthur] and a few folks will handle". Oct offer thread C07C2866011/1760054286.937029: Telegram-only profit share, "generating revenue for us", "Direct costs: UA on Telegram".
- Build: "bots, flows", "work with the product team to advise on what growth features to implement"; a monthly contractor on a contract, like the freelancers Build names.
- Company: excluded; she worked on Domino Delights. Only 1 of 5 services is UA by name; "Content and community... retention loops" is not installs.

FINDING: the census adds no other deciding text; [PERSON_NAME_0133] messages in Slack (21 total) are about the deal and the payment, and a 2024 job post "Reports into: Lauren Brooks" (C04UTBZL6AX/1723144462.387499) is a known name collision the platform already dismissed.

JUDGMENT: Marketing is the better reading and a careful human reaches it. But "best reading among five service lines" is a contestable bucket, and it is exactly what the rev4 reviewer ruled "UNRESOLVED_MATERIAL_DIFFERENCE". Rev4's note already said "the contract I sent out in Oct, $500 a month" and that reviewer did not open the contract. Adding the word "Telegram" changes nothing about that failure mode. The current /prompt report states F14 "Settled by: her contract had her running our paid UA on telegram, so she's marketing, not build". M3 removes the settling record.

**3. Coherence.** Fine. Deletion and note edit are clean.

**4. Harder?** No. One Drive search (`Brooks` or `Lauren`, as Robert's Drive has "Consulting Agreement Lauren Brooks.docx") opens the contract and the UA line decides. A run that skips it can guess Marketing from "Telegram deal". X8 stays a pass-by-default either way.

**5. Fairness.** Reachable. Fairness is not the problem.

**6. /prompt risk.** High. Direct regression of the rev4 finding (UGT 2, Clarity 1). This matches the known pattern: repairs failed review on the moved records themselves.

Verdict: **DROP.** Keep the comment. ZM/CF will then have no live trap; accept that rather than reopening a known FAIL.

## M4 ORPH (Leapblock): drop the year split

**1. Premise.** True. Current post C05URGU759U/1770971846.479179 hands the split. FINDING: Leapblock in Robert's mail: 30 Awaiting vs 29 Processed; exactly one Awaiting has no Processed: robert@harmonygames.co/1776934359028762037, 33,290.00 USD, Sep 13, 2023. `33,290` has exactly one hit across Robert's Slack, Gmail, Drive and contacts. Arthur's "Done!" is C04UEQVDVB7/1694616951.239909, in reply to Leonard "I need approval on [PERSON_NAME_22849]'s 4 payments... invoices are here" (Awaiting at 14:50:58Z).

**2. UGT.** One answer: 407,944 - 374,654 = 33,290 and 30 - 29 = 1 wire, matched to the sole orphan Awaiting, dated inside the DD window. No other gap exists. No Chase-paid first wire fork: the count matches exactly, and Slack Sep 12, 2023 shows the wire had not yet happened ("I couldn't do this wire transfer btw lol").

Would a guess pass? Yes. A run that writes 337,594 by putting the gap under DD passes X4, B1, R1 (DD sum), and C3 (regex takes "33,290" or "statement"). DD is the obvious home: notes "the saga map crew early on", "wider saga map team wrapped in Jun 2024", DD dollar weight 304,304 of 374,654. The bet is not decided by retrieval.

**3. Coherence.** Fine. Wording only. Note the post's phrase "by date of your wire" stops making sense without a split.

**4. Harder?** No. The run's reconciliation at 255 was done by year, but the gap is computed the same way from the totals. Removing the split removes a checksum, not a search.

**5. Fairness.** Fine, but the correct answer is reachable by a guess the rubric can't distinguish.

**6. /prompt risk.** Low, but any edit to a record the platform lists as a passing decider is not free.

Verdict: **DROP.** Inert; do not count it.

## M5 ALIAS (Node Media): take the key out of the note

**1. Premise.** True. comment_7453d8e60a3625923294c54e36a8667d supplies "closed the account"; event 399 `close` found C04UEQVDVB7/1735854841.070019.

**2. UGT.** Unique. Identity chain: Recipient Created robert@.../1820175611244310641 (Jan 2, 2025 21:52Z, by Leonard) to Awaiting 21:53:42Z to Slack 21:53 "can one of you guys approve?" to /1735854841.070019 "This is for closing our account with Node Media LLC" and "3+ months payment" to Processed 22:23Z 16,428.57.

FINDING: Robert's own mail thread 00008689 (robert@.../1815095592611804295) "PERSON_4419_NAME Invoices for Sept, Oct, and Nov" has "W: nodemedia.co", "Sept - $1,428.57 (prorated...)", "Oct - $5000", "Nov - $5000", "ad spend exceeds $100,000", and Frederick's "Nov creative concepts". 1,428.57 + 3 x 5,000 = 16,428.57 (one more month's invoice). The draft does not mention this route.

**3. Coherence.** Fine. "UA Sync invite" is a Slack DM (D04UP2L3E3S/1732210494.264549), not a calendar event; the wording in the draft is loose.

**4. Harder?** Marginal. `PERSON_4419` in Gmail returns six Robert-visible hits, including the invoice thread and Google Ads "manager account (PERSON_4419_NAME)" mails, all without the note's word. The run also reads founders' channel by date (357, 370); Jan 2, 2025 is still in the note. The surviving note "they were late with invoices so several months of 2024 went out at once" points at the invoice mail. M5 removes one of at least three routes. It costs a run one to three calls.

**5. Fairness.** Fine.

**6. /prompt risk.** Low.

Verdict: **KEEP, cheap, do not count it** as a loss channel.

## 7. Double count

Slot map: B1 (5) and R1 (3) are shared by M1, M2, M4, M5 (and OFF). One miss loses them once; a second DD miss loses only its own row plus comment.

Own weight per channel: RET X1+C1 = 8; CORR X5+C4 = 8; ORPH X4+C3 = 8; ALIAS X6 = 5; OFF X3+C2 = 8; CLASS X8+B2+B3+S6 = 16. Shared DD headline B1+R1 = 8.

Runs scores (total 91): RET only 75/91 = 82.4% (the corrected rev6 score); RET + CORR 67/91 = 73.6%.

Independence: two single omissions defeat several moves at once:
- Stopping at Linear notes and not searching beyond the note defeats M1 (RET), M2 (CORR), M3 (CLASS).
- Not running Slack keyword searches defeats M1 (RET) and the Slack route of M5, and ORPH's post (also Slack).

These are fewer independent routes than the five moves imply. The real independent decisions are RET, CORR and OFF.

## 8. Ranked keep / modify / drop, and left-alone

1. **KEEP, modify: M2.** Hedge consistent with Leonard's reply; fix X5's blank-pass.
2. **KEEP as a visibility fix, modify: M1.** Top-level in #admin_foundersonly, no thread, resolve the token dependency, drop the catch-rate claim, fix the draft's "no new rows" contradiction. Not hardening.
3. **KEEP, cheap, uncounted: M5.**
4. **DROP: M4.** Inert; passes by guess.
5. **DROP: M3.** Reopens rev4 /prompt FAIL.

Reconsider from "left alone": **OFF (Lucas).** Its directing pointer is ENG-2447 comment_b13f790bb95e249b8d3a48b1881c0e3a "the bank has him from Sep 2024"; the rule sentence is in the doc already. The run's deliberate hunt failed (177, no Western Union term); the receipts came as collateral of the JPMorgan date window (291). Without the pointer, OFF is a genuine Part 3 #7 item (outside the filter), reachable from Robert's mail (`Lucas` in Gmail shows the five "your money transfer's been received" mails) and C04UEQVDVB7/1719603595.852129 "via company card". A careful human still gets there under the doc's receipt sentence. This is the move most likely to add a distinct trap type. Test it for fairness before committing. Do not touch the doc's rule sentences.

## 9. Against the goal (00_Session_Goal.md rules 1, 4, 5)

Candidate set after this review: RET, CORR, OFF (pointer removed), with ALIAS and ORPH as non-channels.

- **≥ 3 independent loss channels:** RET, CORR, OFF plausibly, but only if OFF is reworked. On the draft as written, RET and CORR only.
- **None over half the weight:** met. Largest own-weight channel is CLASS at 16/91 (17.6%), which you would drop; the DD channels are 8/91 each plus the shared 8.
- **Two or more cross-source decisions on distinct named trap types:** **Not met by the draft.** RET and CORR are both Part 3 #2 "a correction somewhere else". ALIAS is #6 but has no convincing wrong source (a token LLC defaulting to Build). A distinct second type requires OFF as #7 (wrong source: the notices and the note's "the bank has him from Sep 2024"; record that beats: the five Western Union receipts in Robert's mail) or a #8 input built on ORPH that a guess cannot pass.
- **Each naming the wrong source and the beating record:** RET yes (Processed notice vs Apr 2024 founders' messages). CORR yes after M2 (Leonard's hedged note vs Arthur's mail). OFF yes after the rework.
- **Rule 1 UGT:** M1, M2, M5 fine. M3 is not.
- **Rule 5 spread:** unverified. The forecast has to be re-run on the final surface; E[avg] ≤ 82% needs RET plus another live miss in a typical run. M4 and M5 will not supply that. All channels are DD; ZM and CF will have no live trap once M3 is dropped (X8/B2/B3 pass every run).
- **Rubric-stage, needed for these to count:** X5 blank-pass; C1 regex false-pass on Oleg's "came back" (already listed); bind C-rows to their issues.

## Limits

- Warehouse census (complete scans of Snowflake): "33,290", "Node Media", "MotMot" and "Lauren" have zero hits. "Brooks" hits are Oliver Brooks, a different person (FINANCE_LEDGER salaries, e.g. FIN-000019). FINANCE_LEDGER (table 38) has zero hits for "33290" and "Leapblock". Across all tables "33290" does match other columns; the two matches inspected are unrelated (resource_event_id, balance_after), and the rest were not read. The warehouse adds no fork to any move. gsheets "Lauren Brooks": zero Robert-visible hits.
- Slack ranks are not recomputed; search behaviour is inferred from run results and the retrieval tools' descriptions.
- Catch-rate and pass-by-guess statements are judgment from one run.
