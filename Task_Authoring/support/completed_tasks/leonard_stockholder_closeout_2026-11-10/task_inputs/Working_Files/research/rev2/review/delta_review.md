# Delta review rev1 -> rev2 (cold)

Status: complete. Scope: the six changed texts in delta_rev1_rev2.diff, checked against the full rev2 SQL and the base (normal universe, Feb 14 2026). No SQL executed.

Base facts used (all in Leonard's reach):
- Owen Baker = [PERSON_NAME_0068] (Dec 2025 invite accepts from owen.baker@ render as "[PERSON_NAME_0068] has accepted"). His Feb 11 letter, thread 1856860994291529096, went To PERSON_3140_EMAIL only (CC Robert, Arthur) at 20:13:48Z. This is the NB-22 letter (Jan 31, 2025 typo).
- Calvin Price: the base Carta notice "Termination details for Calvin Price" (Oct 29 2025, thread 1847333347700620793) says ES-3, granted 8,138, vested 4,408, exercised 0, grant date Nov 10 2023, terminated Oct 24 2025, last day Jan 24 2026. The only other last day in Feb is [PERSON_NAME_0051], ES-14, Feb 21 2026.
- "Akin" = Husnu Matthew Collins (ENG-2447, matthew.collins@). The pseudonymisation left traces in the base: the Oct 28 2025 reply from matthew.collins@ is signed "best akin" (that is the same date as ENG-2447's "Last mail ... Oct 28, 2025"); the DocuSign header reads "Akin Babayigit viewed ... Advisor Agreement" while the subject field shows "Matthew Collins"; and the 2023 invite headers read "Akin <> Leonard". PERSON_8862_EMAIL appears nowhere in the base, in any mailbox or in contacts. Contact 159 (Matthew) is updated to "Investor and advisor (left the board May 2025)".
- Seed total candidates in the base: 3,051,879 (the Aug 2023 disclosure schedule; Leonard's Jan 2026 "Reset Financing Term Sheet" doc says "Inputs from ledger ... 3,051,879"), 3,051,882 (counsel's June 2023 "corrected cap table", and the per-investor sum per Leonard's Aug 2023 note) and 3,051,881 (the ChatGPT text in #executives /727 and /728). 305,188 "Other Seed investors" appears only in /728 (id b658ec71107dd059e03ea425728ba3b3), not in /727.
- Leonard's mailbox has no other bounce since about Nov 2025 (threads 185*). The earlier DisabledUser bounces (for example victor.barnes@, rachel@) all predate the closing.

## 1. Close-out notes doc: told rule ("sent to them directly and delivered")
- Fork: none found. "Delivered" flips only Owen, whose only written closing message bounced. His Feb 11 Slack DM from Leonard only asks him to join "some announcements" (spoken), so the written+delivered test leaves him untold. No other closing message to any holder has a bounce. The style-run end is updated correctly (+14).
- Residual: delivery of messages that Robert or Arthur sent can't be positively checked from Leonard's mailbox; the natural reading is "no bounce = delivered".
- Hint: mild. It reads as tailored to one bounce, but it is natural for someone who just got one.
- Verdict: clean (minor hint).

## 2. KPMG follow-up (item-1 clarification removed)
- Text: "Three" became "Two", and the snippet and size were updated consistently. Nothing in the SQL still refers to the removed text.
- What the removal broke: this sentence and the old Slack line were the two explicit pins for Series Seed = 3,051,879 (needed for KPMG items 1 and 3). The pin now rests on: Slack "go by the ledger" -> Leonard's term-sheet doc "Inputs from ledger: 3,051,879", plus the Aug 2023 email that calls 3,051,882 a rounding error. That is still resolvable, but counsel's "corrected cap table" (3,051,882) is now a credible competitor.
- Verdict: minor. Fix: make sure the OE and rubric cite the term-sheet/disclosure-schedule path. Optionally have the Slack line say "ledger seed total" so it points to the class total, not only the residual.

## 3. Leonard's #executives line as a thread reply under the Jan 14 ChatGPT post (/727)
- Facts: 3,051,879 - 2,746,693 = 305,186, against ChatGPT's 305,188, so "a couple of shares off" is true. The threading fields and the parent UPDATE are correct, and /727 had no existing replies.
- Misplacement: the "other seed investors" figure is in /728, not /727, which only has the seed total of 3,051,881. A reply under /727 about "the other seed investors ... in these" reads slightly off. It also no longer flags that the seed total itself is 2 high; the agent has to infer that from the arithmetic.
- Ambiguity: "the ledger" is unanchored. FINANCE_LEDGER is a decoy, though harmless since it has no share counts.
- Removed text: "the owner list counts the advisor options in with the stock" was the only explicit warning I found that owner-list figures blend options with stock. That matters for the advisor holders, for example Matthew Collins at 86,470 (advisor agreement, contact now "Investor and advisor") and [PERSON_NAME_0127]. If any graded row depends on splitting such a figure, confirm that another reachable record gives the split.
- Verdict: minor. Fix: thread the reply under /728 (b658ec71107dd059e03ea425728ba3b3, ts 1768417784.194359), or say "the seed numbers" so it covers both posts.

## 4. Gmail delivery-failure notice in Owen's Feb 11 letter thread
- Format: matches base DisabledUser bounces exactly (same from, labels, Auto-Submitted, X-Failed-Recipients, the 550 5.2.1 "is disabled" wording). The hex in the Message-ID decodes to 2026-02-11 20:13:57Z, the same as the date. It arrives 9 s after the letter, In-Reply-To is correct, and threading a bounce into the original thread has precedent in the base (thread 1780212325934678890).
- Fork (minor): ENG-2457's email is this same disabled address, and the rule says "Messages go to the email on each holder's issue". So Owen's note must go to an address the persona's own inbox shows is dead. The explicit rule settles which address to use, but an agent choosing owen.baker@ instead, or flagging the problem, is reasonable. Leonard's Feb 12 comment "No mail with that address before Feb", written after the bounce, is mildly unrealistic.
- Verdict: minor. Fix: the rubric should grade Owen's draft on the issue address and accept a flag; do not penalise mentioning the bounce.

## 5. Feb 3 mail from Calvin Price forwarding a Carta notice
- Facts: every figure matches the base Carta record (ES-3, 8,138 / 4,408 / 0, Nov 10 2023, Oct 24 2025, previously Jan 24 2026). Jan 23 2026 is a Friday and Feb 3 a Tuesday. The format mirrors base Carta mails, and the sender [EMAIL_0801] is his issue email. ENG-2452's comment "No mail with that address before Feb" still holds.
- Supersession: clean. Both notices are Carta, and the later one moves his last day to Feb 20, which now beats Feb 21 for "goes first".
- KPMG: no effect. His line was outstanding at Dec 31 under either last day, and it counts 4,408 vested.
- Residual: a skeptic may doubt a holder-forwarded copy. Mild realism gap: there is no admin-side record of the extension.
- Verdict: clean.

## 6. Feb 12 mail from Leonard to "Akin"
- Facts: the date, Leonard's style, the Message-ID prefix and the thread-id timestamp (+0.3 s) all check out. "Told the team yesterday" matches the Feb 11 announcement and letters.
- Link to the holder: Akin to ENG-2447 is reachable only through pseudonymisation traces ("best akin" on Oct 28 2025, which ENG-2447's own comment points to, and the "Akin Babayigit" DocuSign header). The address is used nowhere else in the base. An agent that can't make the link labels Matthew "Closing". That is defensible if the rubric expects "Already told", and wrong if the design meant Akin as a decoy, so confirm the intent.
- Style: the wording ("hear this from me", "backing us from the start") echoes Robert's Feb 12 mail to PERSON_3941, so the two read as templated.
- Verdict: minor. Fix: vary the wording. Make sure the OE cites the "best akin" mail. Optionally give PERSON_8862_EMAIL one more natural anchor, for example an earlier personal mail from it signed "akin".

## Summary
No fail-level item. Clean: 1, 5. Minor: 2 (seed total less pinned), 3 (wrong parent post, lost advisor-options warning), 4 (note forced to a dead address), 6 (identity rests on pseudonymisation traces; echoes Robert's wording).
