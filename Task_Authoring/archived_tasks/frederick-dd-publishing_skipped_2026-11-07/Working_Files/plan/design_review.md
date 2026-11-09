# Fresh-agent design review (frederick_dd_publishing, design-1)

Reviewer: fresh agent. Base read only through hg.py and persona_view.py. Every base quote below was read from the record.

Counts: **2 BLOCKER, 5 MAJOR, 17 MINOR.** Until F1 to F5 close, §10's line "No decision forks on a reported figure; one reading per point" is not true.

## Forks

### BLOCKER

**F1. Pinegrove status (flips the first pick).**
- Item: Status of Pinegrove Games. Slots S_out_PJ, R_top, K_r_top, K_r_value, K_r_q4, T_chk_live, T_cards, M_vol.
- Reading A (design): "full source code and build pipeline delivered to Pinegrove at signature" takes the code, so Out on rights.
- Reading B: "delivered" is a handover of a copy, not a transfer. Leonard wants to "retain code", and a publisher that holds a copy to run the game doesn't take ownership. The grant is "mobile stores", so it's Live.
- Why it matters: reading B makes Pinegrove the top Live offer. 0.30 x 45,000 x 12 x $0.50 = $81,000, above Copperleaf's $67,200, with Q4 cash $40,000. The pick and all three figures in the reply flip.
- Why no record settles it: the rule says "take something we keep", the sheet says "delivered", and nothing says who owns the code afterwards.
- Fix (wording, TERM_DOCS): "ownership of the full source code and build pipeline passes to Pinegrove at signature".

**F2. Redwood status: its terms match none of the Live forms.**
- Item: Status of Redwood Arcade. Slots S_in_PI, A_adv_PI, V12_Redwood, T_item_PI, T_chk_live, T_cards, M_vol, C_vol.
- Rule: "Live: terms in writing from them, whether that's a term sheet, an email, or their note pasted in by one of us."
- Planned text: "asked about deep links while they look at DD. Her terms for the record: 24% of net to HG..."
- Reading A (design): Arthur recorded her terms, so Live.
- Reading B: that's Arthur's own summary of something she "asked", not writing from them, and not "their note pasted in", so the Live rule isn't met. No other status fits, so the row has no rule answer.
- Same gap in Contacts: the hub says "has written to one of us", and Mei only "asked".
- Why no record settles it: Copperleaf's relay was built with a quoted note for this reason. Redwood's wasn't. §10's resolver, "Arthur records her terms", isn't one of the rule's three forms.
- Fix (wording, ENG_COMMENT): `Redwood Arcade's tech lead, Mei Tanaka (mei@redwoodarcade.com), emailed me about deep links while they look at DD. Pasting her note here for the record: "We'd do 24% of net to HG, a $25,000 advance net 45 from signature, 40,000 installs a month for 12 months, mobile stores only, open to Oct 31. Mei Tanaka, Redwood Arcade"`

### MAJOR

**F3. Rayking status: the base says Frederick planned another route.**
- Item: Rayking Game, Waiting on us or No reply. Slots S_wait_1, T_chk_wait, T_chk_silent.
- Reading A (design): his message is an unsent draft, so "we haven't answered".
- Reading B: about 25 minutes after the draft, in `D05S58U4SAK/1757009185.631739`, Frederick wrote: "No worries. I'll reach out to someone over There on linkedin." If he did, the rule gives No reply ("nothing back from them").
- Why no record settles it: `1757009028.543439` ("So you don't have an email address for...?", answered "no") explains the unsent draft. Nothing says whether the LinkedIn outreach happened. Gmail "Rayking" has one thread, and Slack has no hit for the name or any later LinkedIn line from him. T12 and §10 don't mention this DM.
- Fix (dated record): a seeded Frederick DM in `D05S58U4SAK`, Sep 5, between 1757009185 and 1757132623: "Couldn't find anyone from Rayking on LinkedIn. Parking it for now, we still owe them an answer."

**F4. Contacts count: the two base people can't be written cleanly.**
- Item: "Everyone at a publisher who has written to one of us". Budget says 17 adds (19 people minus 2). Slot C_vol.
- Rayking: the sender is a masked token, `[PERSON_NAME_49709]`, and the address is the jobs group (`'Ren}*洋_洋*~' via jobs <SVC_0331_EMAIL>`). The base says no address exists (`D05S58U4SAK/1757009159.871119`: "no"). That address is already in Contacts as `SVC_0331` (`/contacts/119`), so "Skip anyone who's already there" also reads as a skip. `contacts_add_new_contact` requires first_name and last_name.
- Appodeal: two addresses and several name tokens. `1829687508014442264` has `PERSON_5858_NAME <PERSON_5817_EMAIL>` and "I'm [PERSON_NAME_6155]". `1829689338387596598` has `PERSON_5817_NAME`, signed `[PERSON_NAME_46149]`. `1830012626042968381` has `PERSON_5858_EMAIL`, signed Victoria Huz. That's one person or two.
- Readings: 15, 16, 17 or 18 adds, all defensible. Summit's acknowledgement sender is one more edge.
- Why no record settles it: only the 17 seeded people have clean names and addresses.
- Fix (wording, HUB): "Everyone at a publisher who has given us terms or told us no should be in Contacts..." That gives 16 people, 14 adds, with no masked names. It costs three writes against the 130-call target. Otherwise drop the exact count from C_vol and grade named seeded people only.

**F5. Appodeal status: two rule words misfit.**
- Item: Appodeal. Slots S_wait_2, T_chk_wait, T_chk_live, T_cards, M_vol.
- Reading A (design): Waiting on us.
- Reading B1: Live. Their own May 21 mail says "consider our proposal" (`1830012626042968381`), the Apr 17 mail lists "Unlimited UA funding", and the Live rule accepts "an email" with no minimum content.
- Reading B2: "we haven't answered" is false as written. Frederick answered on Apr 29 and May 14. Only their May 15 and May 21 mails are open. On a literal read, no status fits.
- Why no record settles it: the rule doesn't define "terms" and doesn't say "last message".
- Fix (wording, RULES): "Live: a rev share and an advance in writing from them, whether that's a term sheet, an email, or their note pasted in by one of us." and "Waiting on us: they wrote to us, there are no terms, and the last message is theirs." The second line also firms up Rayking and Kitebridge.

### MINOR

**F6. Oakline "on acceptance of this sheet".** The Sep 26 wire implies someone accepted the sheet. Yet it stays "open to Oct 24" and Leonard is still choosing which offer goes first. Reading A: open and Live. Reading B: accepted, so the Oct 24 reminder is moot and the pick is compromised. No record shows an acceptance. Fix (wording): "$10,000 first-look payment within 3 days of this sheet, credited to the advance".

**F7. "open to" against the signing date.** All seven offers close by Oct 31, and the rule already signs on Oct 31 or later. Copperleaf, the pick, is "open to Oct 17" with signature on Nov 14. Reading B: it lapses before signature, so no Q4 cash. The rule's formula points the other way, so this is minor. Fix (wording): "respond by Oct 17" in every sheet and note, matching the rule's "response date".

**F8. Direction of the rev share.** Relay says "to you" and ENG comment says "to HG", but TERM_DOCS say only "30% of net". The rule says "their rev share". Reading B: 30% is the publisher's cut, so ours is 70%. Fix (wording): "30% of net to Harmony Games" in all eight sheets, and "Our share is the rev share they offer us times the gross."

**F9. Tamatem isn't dispositioned.** `C48D58CD7FBD/1748974617.722599`, Jun 3: "Tamatem is a very good publisher... a contact worth exploring", and Frederick: "I'll look into it!" It's visible to Frederick, inside the window, off the sheet, and absent from §10. "however it reached us" invites adding it, which moves S_total. Fix: add a §10 row, and to RULES: "A name someone passed along doesn't count unless they came to us."

**F10. Tallwater "handover".** PB_NOTE says "who runs live ops after the handover". In a rights test that reads as a transfer, beside Pinegrove's clause. Fix (wording): "who runs live ops after launch".

**F11. Records the sweep can't reach yet.**
- All 22 seeded publisher threads are planned as a status line only ("Passed; sent: ..."). Only Oakline's Sep 26 message and Moonrail's signature have wording, so Kitebridge, the six passes and the term-sheet covering mails can't be swept.
- §1a and the portfolio rely on control calls ("Harbor Lane and Wavecrest have calls with no change"). §11 plans neither event.
- The sheet's 24 rows include Appodeal and Rayking only by inference (M has tranche=0 for both, the same value as the two off-sheet offers). State their rows, or population loses its anchor.
- Fix: plan this wording before injection.

## Base contradictions

**B1. MAJOR. Term sheets against Frederick's Sep 24 words.**
- Seeded claim: term sheets from Moonrail (Sep 18), Sunfold (Sep 19), Tallwater (Sep 22) and Oakline (Sep 23), and the May one-pager already mailed with paid numbers.
- Base: `D05S58U4SAK/1758735819.982259`, Sep 24: "I image we can get someone interested if they think LTV of $7." That reads as if nobody is interested yet, one day after the fourth term sheet. `D05S58U4SAK/1758735778.095599`: "Are you cool with me quoting our incent numbers" reads as a first-time question, four months after a mailing of the same class of numbers. `C07C2866011/1758739523.734689`, same day: "if There are no other offers, we have no other option but to shut down".
- Judgment: `1758736827.548589` ("a new tranche") and the Apr 28 template in `f_0d17fc08eddaf231cf7f28` ("a brief one-pager and some early performance data") support earlier outreach, so this is tension, not impossibility. The standing line reads well as Leonard's follow-up to this DM.
- Fix (dated record): a seeded Frederick DM between 1758735819 and 1758736058: "I mean someone bigger. The earlier tranches have only come back with small offers." Or move the four term sheets to Sep 25 or later, keeping Oakline's before its Sep 26 wire.

**B2. MINOR. "the beneficiary name still said Calm Play".**
- Base: Calm Play never had an account. `C07C2866011/1727980540.831209`: "not for calm play", then "we used [SOURCE_ORG_0001] bank accounts". SVB's name is on `D05S58U4SAK/1738003879.776129`: "Name on the account: Harmony Games GAMES INC." No name change exists, so "still" implies a history the base denies.
- The design's anchor is wrong too. `C07C2866011/1752726128.862409` is Zombie Match's Android transfer (`1752548116.304169`), not DD. DD left Calm Play in Oct 2024 (`D05S58U4SAK/1727971721.374409`).
- A mismatch bounce itself is coherent, and no deliverable asks the reason.
- Fix (wording): "Their bank sent it back because they put Calm Play as the beneficiary and the account is in Harmony Games Inc.'s name."

**B3. MINOR. "Co-dev or investment talks about Zombie Match... That covers Homa and NCsoft".**
- Base: Leonard's Sep 17 mail on `1843552279434086285` says "We are also considering publishing opportunities" and lists Domino Delights first. `C096HFA5Z8W/1758210943.211579`: "path 1- co-dev / publishing". `C07C2866011/1759182723.694969`: "an engine deal with NCsoft". Neither talk is Zombie Match-specific.
- The exclusion by name holds, so no status moves.
- Fix (wording): "Co-dev, engine or investment talks aren't part of this, even where DD came up. That covers Homa and NCsoft..."

**B4. MINOR. Robert's relay under the 70% D1 root reads badly.** `C07C2866011/1758736960.824899` is about a competitor's retention, and Robert's eight replies are on its forced ads. "pasting it here so it doesn't get lost" is the opposite of what a dead thread does. Fix (wording): open with "Off topic but I'm in here anyway:" and drop "so it doesn't get lost".

**B5. MINOR. Arthur's cash note: root and author.** Root `1757345405.134829` means an investment banker, so the link is a pun, though Sep 29 is the "2-3 weeks" it named, so it passes. The author is the larger issue. Leonard is the bank voice (`C096HFA5Z8W/1757548092.670219`, `D05S58U4SAK/1751935004.944189`) and my searches found no banking post from Arthur. Fix (wording): "Checked SVB with Leonard this morning: that $10K..."

**B6. MINOR. Matthew root.** `C096HFA5Z8W/1758147530.732569` passes: its replies are about metrics. But the line reaches publishers from a fundraising thread eight days later. Fix: none required. An opener such as "Same problem on the publisher side:" would help.

**B7. MINOR. SC-6 thread on the path.** §1a says "no vendor mail is on the path", but the Tilting row cites `1823332883409810377`, the Brian Cooper thread. Fix: drop that citation. The rule doc already settles Tilting Point.

**B8. MINOR. Same-day list mismatch.** `f_10dfa1b4236a7c35dcb632` (created Sep 24 17:08Z) lists Tilting Point, Jam City and others, and the Sep 24 tranche contains none of them. Fix: a sheet note, "Partners doc names not approached yet".

**Also:** F3 and F4 are base conflicts, counted once above.

## Leaks and unfair traps

**L1. MAJOR (balance). Copperleaf is one needle under the whole reply.** RELAY has no "publisher", "publishing", "offer" or "terms". A natural Slack "publisher" sweep finds Arthur's pointer and misses this, leaving only "advance", "installs" or "DD". R_top, K_r_top, K_r_value, K_r_q4, S_in_PH, A_adv_PH, V12_Copperleaf and T_item_PH all hang on it, so runs would fail together, and a platform reviewer may call that thin. Fix (wording): "Someone I know at Copperleaf Games, a small publisher, saw DD...", keeping it a reply.

**L2. MINOR. T1 is a named correction.** "that Oakline $10K" is hit by any per-publisher Slack search, and "actually banked" plus "actually in the SVB account" point at it. Fix: "that $10K first-look never hit SVB".

**L3. MINOR. T3 leaks through her first name.** The sheet's Contact column and her mail give "Anika", and the post opens "Anika called me". Fix: "Got a call from Kestrel:", so the signature or Contacts join is needed.

**L4. MINOR. T9 names its source.** "If ESG gives us a later date" is one Gmail search, so the 0.45 miss rate looks high. Fix: "If our lawyers give us a later date".

**L5. MINOR. Read-and-done items counted as traps.** T11, T13, T15, T16 and T20 are stated outright in RULES or HUB, and T10 is settled by reading the list. Keep them as controls and don't count them toward the trap total.

**L6. Route to prove (no severity).** T2 rests on a calendar description, a ○ carrier. §10 already sends this to the pre-check. If `gcal_search_events` doesn't return it, T2 becomes unfair.

Fair as designed: T4 (subject to L1), T5, T6, T7, T8. T12's draft shows To: Leonard, so it doesn't depend on label visibility.

## Checked and clean

- **Arithmetic:** all seven 12-month values and Q4 dates recomputed (Nov 14 +30 = Dec 14, +45 = Dec 29, +60 = Jan 13). Order: Copperleaf 67,200, Redwood 57,600, Sunfold 54,000, Tallwater 45,000, Oakline 36,000, Harbor Lane 30,000, Wavecrest 19,800.
- **Keep value:** `REVENUE_DAILY` (/tables/12) gives 2,078.33, 721.55 and 381.11, all 30 Sep days present, so 12,723.96.
- **May one-pager:** matches `1830890312657338682` ("D1 Retention: 50%+", "D7 Retention: 20%+", "ARPDAU averaging ~$0.13", "acquiring users through incentivized channels").
- **$0.50 figure:** `D05S58U4SAK/1758736747.409459`, by Leonard, so "my Sep 24 note" is right.
- **Rights line:** `f_26e1f9a86761e35049192a` and `C07C2866011/1756140953.197759` carry "retain code, IP and non-mobile distribution rights". Caveat: the sync doc is an agenda with no recorded decision, so "agreed" is a seeded claim, not contradicted.
- **Hub claims:** a16z `C07C2866011/1759196260.965849` ("we didn't get in"); Turkish fund `1759182620.491829` ("this is gonna be a no"); Sep 24 lead `D05S58U4SAK/1758736842.534589`; Oct 6 is a Monday with no base event.
- **ESG:** partner confirmed on `1841636073974841484`. In Frederick's view, no base record on arbitration or ESG's availability (one unrelated 2023 Slack hit).
- **ENG-2362:** Singular deep links, assignee Arthur, project GoD - Beta, Todo. Fits.
- **Trello:** board UA/BD; BD Follow Up holds Netflix, Mattel and two cards with masked names, all from Oct 2024. The masked names can't be read, and none of the readable ones is a cohort name.
- **Population census:** Frederick's mail since Apr 1 ("Domino Delights", publish, publisher, publishing) shows inbound publishers Appodeal and Rayking only. Prodege (`1839023475874420216`) is a UA vendor. Mattel (`1841567055589252118`) is a co-dev pilot and investment, Leonard's approach. Apple Arcade is pre-window.
- **Tilting Point:** `1842443183462721250` is an automatic ack and names no game. The rule doc settles it.
- **Contacts:** no Appodeal, Rayking, or `PERSON_5858`/`5817` rows.
- **Thread counters:** roots show reply_count 2, 8 and 4 as the plan assumes.
