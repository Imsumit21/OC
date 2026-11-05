# Blind fork sweep, rev4 (Frederick Stone view, synth-cut, today Wed Oct 1, 2025 PT)

Sources read: `record_dump_rules.md`, `record_dump_members_rev4.md`, `record_dump_base.md`, plus Frederick-scoped base checks (his mailbox thread files, Slack via `persona_view.py`, unscoped Trello/Contacts/Linear/Calendar). Nothing else under Working_Files was opened.

Base checks run, with results:
- Slack/Gmail "Maren", "Halvorsen", "Rina", "Pro plan", "pager", "PagerDuty", "on-call", "Spotlight", "indie showcase". There is no second Maren, Wen, Rina or paging vendor in Frederick's view.
- Aug–Sep 2025 mailbox threads with offer/terms language. Only cold pitches, investors, ad networks and named exclusions turned up.
- Base Contacts (170 entries). None of the backlog people are present, Balancy included.
- Trello boards: Harmony Games (`640643a3fd8f3ca308d9318e`, To Do list `640643a3fd8f3ca308d93195`) and UA/BD (`66da196af476ab78deaa0cef`, To Do and BD Follow Up lists, last activity 2024).
- Linear Jul–Sep 2025. No vendor issues besides ZOM-567.
- Frederick's calendar Aug 2025–Feb 2026. Only the Aug 14 Balancy call is relevant.

---

## 1. Independent log (36 rows)

Decision set is from README f_846ddc38b2aab3d2ed3fcb and guardrails f_b98287f6f80fe431a71209: Answered · End · Keep · Sign · Park.
Next date follows the README: End = last day to cancel or say no; Park and "later" answers = January review; Keep = when it next bills; Sign = needed-by date, if any.

| # | Company | Contact | What's waiting | Decision | Answered by | What we told them / should tell them | Next date |
|---|---|---|---|---|---|---|---|
| 1 | Spotlight Fest | Rina Takeda (PERSON_9734_EMAIL) | Dec 5 indie showcase slot, $750 stand fee (thr 1842712097588195482; f_9d9cf4e53b1c8607f9c869) | Answered | Robert, Sep 17, 2025 (call; Slack fc2f69c06b333f6c54dfd63d455c3958) | "We're sitting this one out this year" (no) | none (answer was no, not "later") |
| 2 | Motive Forge | Hugo Lambert (PERSON_9733_EMAIL) | 3D art quote $6,400 (thr 1843346276352084348; f_e81c6ef89513cac632700a) | Answered | Arthur, Sep 19, 2025 (email) | "We're keeping the art in-house, so we'll pass" | none |
| 3 | Lanternfly Publishing | Wen Halvorsen (PERSON_9702_EMAIL) | SE Asia publishing deal for Domino Delights, rev share, 2-yr exclusive (thr 1842800807116855774; slides f_5dbbaf5b251d5261427eb1) | Answered (see fork F4) | Leonard, Sat Sep 27, 2025 (phone; DM 418a0a6d6c29b7b67ce0ffb270c78c1e) | "SE Asia waits until after the raise; we'll pick it up in January" ("later") | Jan 5, 2026 |
| 4 | Balancy | PERSON_0527_NAME (PERSON_0527_EMAIL), Growth & Partnerships Mgr | LiveOps platform, 1-month trial offer; Aug 14 call (thr 1840501641217286806; cal "Frederick and Balancy Team" Aug 14) | Answered | Leonard, Sep 11, 2025 PT (email; Sep 12 00:21 UTC) | "Still interested, priorities shifted for the next few months, we'll circle back when we have bandwidth" ("later") | Jan 5, 2026 |
| 5 | Pixel Harbor Events | Teodor Lind (PERSON_9705_EMAIL) | 10x10 booth hold, Bay Area Indie Showcase Oct 24, $4,800; $2,400 deposit by Oct 10 (thr 1835288808653226583; f_614f88a28a2f0cf1b88408; tracker f_9d6edd4922d8130ccd272e) | End | — (Fred's Jun 19 "I'll come back to you" is a holding reply) | No, release the hold | Oct 10, 2025 |
| 6 | Clipforge | Priya Raman (PERSON_9704_EMAIL) | UGC Studio pilot HG-2291 hit its 20-video cap; pilot ends Oct 15, Studio plan $1,800/mo from Oct 16 (Paylane notice thr 1843067564852153540; f_8d0e0e3ae076b2f745e7e2; thr 1837102635418059486) | End | — | Cancel in writing to billing@paylane.io by Oct 15 (the notice's channel); tell Priya no next brief (fork F13) | Oct 15, 2025 |
| 7 | Ascendo | Lucia Ferrer (PERSON_9712_EMAIL) | ASO retainer $900/mo from Oct 1, confirm by Oct 1 (thr 1841081352192260725; f_a9593b0bf23b760e2972c7) | End | — | No | Oct 1, 2025 |
| 8 | Brightlane Studio | Ines Varga (PERSON_9706_EMAIL) | Creative retainer $3,500/mo from Oct 1, 3-mo min, confirm by Oct 1 (thr 1841809902797646290; f_9d4639f91c93478d888f4b) | End | — | No | Oct 1, 2025 |
| 9 | Lingora | Elena Petrova (PERSON_9710_EMAIL) | Store-listing localization $2,640 invoiced on delivery, price holds to Oct 3 (thr 1842168515789422611; f_34ba4ac9a0f0fa4fd34e9e) | End | — | No | Oct 3, 2025 |
| 10 | Panelpulse | Arjun Shah (PERSON_9711_EMAIL) | 12-player panel Oct 14, $1,200 prepaid, confirm by Oct 6 (thr 1842353484595925809; f_41a9ea5036a231989745b2) | End | — | No | Oct 6, 2025 |
| 11 | Soundvault | Rafael Moreno (PERSON_9707_EMAIL) | Trailer music annual licence $1,188 on signature, quote to Oct 15 (thr 1842719647334876669; f_2686da1086bfcc2fba3f57) | End | — | No | Oct 15, 2025 |
| 12 | Streamcast Talent | Kofi Mensah (PERSON_9709_EMAIL) | Nov creator campaign $8,000, 50% deposit on booking, book by Oct 31 (thr 1842998987980893279; f_5b961c9c6887d31dcd2ee2) | End | — | No | Oct 31, 2025 |
| 13 | Wishwave | Sven Aalto (PERSON_9713_EMAIL) | Seattle Indie Expo Nov 7 push; we cover ~$1,600 travel, booked by Wishwave and invoiced (thr 1843538794906427760; f_54c2b4e172bb73a4a19845) | End (Monday change 7e88911312fa9a969f0659a105af59a3) | — | No | Oct 17, 2025 |
| 14 | Reviewly | Hana Kobayashi (PERSON_9708_EMAIL) | 30-day trial from Sep 19, then Growth $79/mo on Oct 20 unless cancelled by Oct 19 (thr 1843712439092112354; f_4bdfb8e0c47288087c7bba) | End | — | Cancel the trial (by email to the onboarding contact, i.e. reply to Hana) | Oct 19, 2025 |
| 15 | Vaultline | Mila Novak (PERSON_9714_EMAIL) | Nightly DB backups move to Standard $19/mo at the Oct 12 renewal (thr 1843980455117084538; f_2715771ae5f0358ad39aa9) | Keep (keep-running card 689b662c60cbe40b9f4a97ae) | — | We're staying; keep the backups running | Oct 12, 2025 |
| 16 | Certwell | Jonas Weber (PERSON_9715_EMAIL) | API-domain SSL renewal $89/yr, due Oct 20 (thr 1844067277209770126; f_cfb172dea30b9f6ac8a340) | Keep | — | We're staying; please reissue | Oct 20, 2025 |
| 17 | Pingwise | Dana Whitfield (PERSON_9703_EMAIL) | Starter ends Oct 31; Team $29/mo from Nov 1 keeps phone/SMS paging (thr 1844157874176168845; f_6c212cbfb31c3ded44ef8a) | Keep ("night pager" item) | — | We're staying on Team; don't downgrade | Nov 1, 2025 |
| 18 | Markward | Leah Brennan (exists in Contacts) | Free-tier click-through terms in the dashboard, no term (thr 1842802694553769659; f_71a95593c736b3baf45f91) | Sign (no ESG) | — | It's with Leonard or Arthur to accept | none (no needed-by date) |
| 19 | Kinetic Arcade | Noor Haddad (exists) | JP/KR publishing LOI, rev share, 12-mo exclusivity (thr 1842895178957083445; f_6252955f500f81e3aacbef) | Sign + ESG (exclusivity) | — | With our lawyers first, then Leonard or Arthur to sign | Oct 20, 2025 |
| 20 | Lumencloud | Aiden Clarke (exists) | Startup Program Agreement, $25k credits, 36-mo term (thr 1842991438234544282; f_a227b14f03e12005fe8324) | Sign + ESG (term >12 mo) | — | With our lawyers first, then Leonard or Arthur | Oct 31, 2025 |
| 21 | Bundlehouse | Freya Olsen (PERSON_9718_EMAIL) | Holiday bundle participation agreement; 18-mo licence of Domino Delights name/logo/art (thr 1843442535629243130; slides f_9d1e0270574584de0eb92c) | Sign + ESG (IP licence; also >12 mo) | — | With our lawyers first, then Leonard or Arthur | Nov 1, 2025 |
| 22 | Orbit Store | Mateo Rossi (PERSON_9719_EMAIL) | Nov puzzle-week featuring agreement, accept in partner portal by authorised signatory, no fees (thr 1843708664218314020; f_2ae7e3ee3220b628391234) | Sign (no ESG) | — | It's with Leonard or Arthur to accept | Oct 24, 2025 |
| 23 | Playfuse | Iris Navarro (PERSON_9721_EMAIL) | Mutual NDA on ESG template, 2-yr term, before the Oct 8 call (thr 1844256020889910750; f_9a7fc4a3e45e4394227fa5) | Sign (template NDA, so no ESG) | — | It's with Leonard or Arthur to sign | Oct 8, 2025 |
| 24 | Nintendo | none (portal no-reply SVC_0208_EMAIL) | Developer Portal Global ToS & NDA needs an officer's acceptance (base thr 1842358947604469113 / 1842359398719557772; ZOM-567 + cmt_c9a6660d81e067ad1de7) | Sign (no ESG) | — | No written answer (portal) | Oct 15, 2025 |
| 25 | Hootline | Gemma Doyle (PERSON_9722_EMAIL) | Startup promo free to Jan 31, 2026, then $39/mo; "keep the scheduler after?" (thr 1839631800730308867; no filed paper) | Park | — | We'll pick it up in January | Jan 5, 2026 |
| 26 | Echohall | Bruno Costa (PERSON_9725_EMAIL) | Pro $49/mo from the day we upgrade; free plan continues (thr 1841538111898044975; f_68e288146ba0eee9fc17fa) | Park | — | We'll pick it up in January | Jan 5, 2026 |
| 27 | Quillcraft | Nadia Petrov (PERSON_9728_EMAIL) | Beta free through Jan 31, 2026; asks for a feedback call (thr 1842262887629456494; f_af809bf6325b452edc8476) | Park | — | We'll pick it up in January | Jan 5, 2026 |
| 28 | Loopnote | Pavel Sokol (PERSON_9731_EMAIL) | Team trial free to Feb 1, 2026; "add the rest of the team?" (thr 1842712097587609477; f_6963d4d30aceef4f88966a) | Park | — | We'll pick it up in January | Jan 5, 2026 |
| 29 | Pressbeam | Ava Lindqvist (PERSON_9726_EMAIL) | Launch package $1,200 when booked, any time before the 2026 launch (thr 1842983888486665921; f_a9bb79c86b8b7b92083785) | Park | — | We'll pick it up in January | Jan 5, 2026 |
| 30 | Cloudlark | Yara Nasser (PERSON_9724_EMAIL) | $10k credits held to Feb 28, 2026; "activate now or later?" (thr 1843078260327282996; f_eb94c65ce9f273c6b5a579) | Park | — | We'll pick it up in January | Jan 5, 2026 |
| 31 | Retainly | Omar Farouk (PERSON_9727_EMAIL) | Trial free to Jan 12, 2026, then Growth $99/mo; "stay on?" (thr 1843346276352069546; f_be21bac5d50e291ebfbe2b) | Park | — | We'll pick it up in January | Jan 5, 2026 |
| 32 | Glyphworks | Tomas Novotny (PERSON_9723_EMAIL) | Font embedding licence $640 when ordered, quote to Jan 31, 2026 (thr 1843350051225919345; f_f6701704e5659b05d9530f) | Park | — | We'll pick it up in January | Jan 5, 2026 |
| 33 | Framewell | Maren Holt (PERSON_9701_EMAIL) | Pro order form ($149/mo from Nov 1 on paper), now held at no charge until Feb 1 with nothing to sign (thr 1843618067251203081; f_fba21c2d5d4bbb02983961; Slack 9fb2d23420c7e01ca163571f4129c912) | Park | — | We'll pick it up in January | Jan 5, 2026 |
| 34 | Tilecast | Kenji Mori (PERSON_9729_EMAIL) | Free website demo-widget pilot slot, Feb 2026; "hold it?" (thr 1843708664217753499; f_6d13a63be892a29f796b78) | Park | — | We'll pick it up in January | Jan 5, 2026 |
| 35 | Benchmarkly | Clara Weiss (PERSON_9730_EMAIL) | Full benchmark set $300/mo from Feb 2026 if we subscribe (thr 1843984229991264696; f_e916ab7563891481ab3b16) | Park | — | We'll pick it up in January | Jan 5, 2026 |
| 36 | Driftwood Audio | Sofia Marin (PERSON_9732_EMAIL) | Trailer VO $950 when booked, quote to Feb 28, 2026 (thr 1844165423924029064; f_17878d7b82fafcee79bfe7) | Park | — | We'll pick it up in January | Jan 5, 2026 |

Counts: Answered 4 · End 10 · Keep 3 · Sign 7 (3 of them through ESG) · Park 12 = 36.

### Considered and left off

| Company | Excluding record |
|---|---|
| Nova Rewards (Ruth Calloway) | Offer withdrawn Sep 23 ("withdrawing this offer for now", thr 1842255337882328812). No call, reply or paper on record either. |
| Paylane | Clipforge's billing partner ("Paylane, payments for UGC Studio", thr 1843067564852153540; agreement "billed by our payments partner"). Folded into the Clipforge row. |
| Rayking Game | Cold pitch Leonard forwarded internally (base thr 1842348778705877030). Frederick's Sep 4 message is labelled `Drafts` and addressed only to Leonard, so it was never sent to Rayking. Leonard: "Cold pitches nobody answered, including ones we only forwarded around internally, stay off it." |
| Playable Factory | Cold, unanswered (base thr 1843000993076735547). |
| Gamesforum SF, InterCo Digital, Bay Area Times, Tru Art HR, Outbound Solutions, VERV Design, GPT Trainer, visitor-ID tool, "quick question" | Cold, unanswered (1842890197572292911, 1841620870486605150, 1837086359940231442, 1841186624540452648, 1841082415390712120, 1841005754425433303, 1841080575152316598, 1841624521129878378, 1841457242812522049). |
| DocuSign-style "Access & Approve Document" | Company-less notification (1841180415606843201). |
| Google (Tim) | Ad network; stays on the UA budget call (base thr 1817715521687421486; Leonard's email). |
| Craftsman+ | Named exclusion; Sep 9 "Checking in" (1823332883409810377). |
| Singular | Named exclusion (1837914783244638008; tracker row). |
| PlayableX | Named exclusion (base 1825682411726311950, Mar 2025). |
| Adjoe, Unity, Meta, AdMob/ironSource | Ad networks (UA buckets doc f_7bacf15c4e8eea1a52dcd4). |
| Mattel | "Mattel, which I'm keeping" (Leonard; base 1841567055589252118). |
| Dentsu, NCsoft, SciPlay, GRx, SVB, Griffin and other intros | Investor work. #bridge-pitch C096HFA5Z8W lists Mattel/NCsoft/SciPlay/Dentsu as raise outreach; threads 1843473831194478743, 1832208184829815962, 1842285743246816270, 1842278603974731778. |
| ESG Law | Our counsel, not a vendor with an offer. |
| Playtestcloud | Tracker "running, Leonard owns". No offer or ask in Frederick's view. |
| Solsten | Tracker "paused in May". Only newsletters since. |
| App Store / Google Play developer accounts | On the keep-running list, but no renewal or ask in front of us (mailbox search). |

---

## 2. Writes implied

**Written answers (31 companies, 32 emails if Priya also gets one).** All reply on the vendor's own thread unless noted.
- **End (10):** Pixel Harbor/Teodor (1835288808653226583), Ascendo/Lucia (1841081352192260725), Brightlane/Ines (1841809902797646290), Lingora/Elena (1842168515789422611), Panelpulse/Arjun (1842353484595925809), Soundvault/Rafael (1842719647334876669), Streamcast/Kofi (1842998987980893279), Wishwave/Sven (1843538794906427760), Reviewly/Hana (1843712439092112354, cancellation).
  - Clipforge is a new email to **billing@paylane.io**: written cancellation by Oct 15. Do not reply to the no-reply notice.
  - Possibly also a reply to Priya on 1837102635418059486 (fork F13).
- **Keep (3):** Vaultline/Mila (1843980455117084538), Certwell/Jonas (1844067277209770126), Pingwise/Dana (1844157874176168845). Message: "we're staying".
- **Sign (6):** Markward/Leah, Orbit/Mateo, Playfuse/Iris get "with Leonard or Arthur to sign". Kinetic/Noor, Lumencloud/Aiden, Bundlehouse/Freya get "with our lawyers first, then Leonard or Arthur". Nintendo gets none (portal).
- **Park (12):** Hootline, Echohall, Quillcraft, Loopnote, Pressbeam, Cloudlark, Retainly, Glyphworks, Framewell, Tilecast, Benchmarkly, Driftwood. Message: "we'll pick it up in January".
- **No writes:** the 4 Answered rows (Spotlight Fest, Motive Forge, Lanternfly, Balancy) and Nintendo.

**ESG Law intake emails (3).** Send to the "ESG Law intake" contact 9b0185e445572aeee9f27d35 (PERSON_2599_EMAIL), one per agreement. Contents follow checklist f_3b06917a41dd59308d890b: company and agreement, term and any auto-renewal, exclusivity or IP licence, cost, needed-by date, signer (Leonard or Arthur).
- Kinetic Arcade: LOI, JP/KR, rev share, no cost, 12-mo exclusivity from signature, no auto-renewal stated, by Oct 20.
- Lumencloud: Startup Program Agreement, $25k credits, 36-mo term, no charges while credits last, by Oct 31.
- Bundlehouse: participation agreement, no cost, rev share, 18-mo licence of Domino Delights name/logo/art, by Nov 1.

Why only these three: they are the only Sign items that trip ESG's triggers (exclusivity, IP licence, term over 12 months) in ESG note thr 1844177063117059830. Playfuse is exempt as a template mutual NDA. Lanternfly would have qualified but is Answered.

**Signing cards (7).** Harmony Games board 640643a3fd8f3ca308d9318e, To Do list 640643a3fd8f3ca308d93195, company name in each title (Leonard, Sep 25): Markward, Kinetic Arcade, Lumencloud, Bundlehouse, Orbit Store, Playfuse, Nintendo.

**Contacts to add (32), job = company.** Noor Haddad, Aiden Clarke and Leah Brennan already exist; Nintendo has no person (fork F23).
- Teodor Lind (Pixel Harbor Events), Priya Raman (Clipforge), Gemma Doyle (Hootline), Lucia Ferrer (Ascendo), Bruno Costa (Echohall), Ines Varga (Brightlane Studio), Elena Petrova (Lingora), Nadia Petrov (Quillcraft)
- Arjun Shah (Panelpulse), Pavel Sokol (Loopnote), Rina Takeda (Spotlight Fest), Rafael Moreno (Soundvault), Wen Halvorsen (Lanternfly Publishing), Ava Lindqvist (Pressbeam), Kofi Mensah (Streamcast Talent), Yara Nasser (Cloudlark)
- Omar Farouk (Retainly), Hugo Lambert (Motive Forge), Tomas Novotny (Glyphworks), Freya Olsen (Bundlehouse), Sven Aalto (Wishwave), Maren Holt (Framewell), Mateo Rossi (Orbit Store), Kenji Mori (Tilecast)
- Hana Kobayashi (Reviewly), Mila Novak (Vaultline), Clara Weiss (Benchmarkly), Jonas Weber (Certwell), Dana Whitfield (Pingwise), Sofia Marin (Driftwood Audio), Iris Navarro (Playfuse), PERSON_0527_NAME (Balancy)

**January-review reminders (14).** One per company on **Mon Jan 5, 2026**, the day of evt_fd469c29811879519c2c96 (17:00Z = 9:00 PST).
- The 12 Park rows: Hootline, Echohall, Quillcraft, Loopnote, Pressbeam, Cloudlark, Retainly, Glyphworks, Framewell, Tilecast, Benchmarkly, Driftwood Audio.
- The 2 "later" Answered rows: Lanternfly, Balancy.
- Spotlight Fest and Motive Forge get none (answer was "no").

**Log.** New sheet "Q4 commitments log" in the Q4 commitments folder d_80a8c04753ba82ba4ba6a5, with the template f_05f0a451b29b19a1c0b90f header and 36 rows.

**Reply to Leonard** on thr 1844732913254784171:
- Keeping: Vaultline ($19/mo from Oct 12), Certwell ($89, Oct 20), Pingwise ($29/mo from Nov 1).
- Waiting on Arthur or Leonard to sign: Markward (no deadline), Playfuse (Oct 8), Nintendo portal ToS & NDA (Oct 15), Kinetic Arcade (Oct 20, at ESG first), Orbit Store (Oct 24, portal), Lumencloud (Oct 31, at ESG first), Bundlehouse (Nov 1, at ESG first).

---

## 3. Fork table

| # | Decision point | Reading A | Reading B | Settling record(s) | Status |
|---|---|---|---|---|---|
| F1 | Leonard's "Maren called me back about the Pro plan…" is a thread reply under his Sep 22 "Playtestcloud results are in" post (C07C2866011, parent ts 1758513190.847889) | Framewell | Playtestcloud (thread parent) or Echohall (also has a "Pro") | Maren Holt signs thr 1843618067251203081 "Framewell Pro for Harmony Games"; no other Maren in Frederick's Slack/mail; Echohall's contact is Bruno; Playtestcloud has no Pro offer | SETTLED (A) |
| F2 | Framewell decision | Park (Leonard: "they'll hold it at no charge until Feb 1 with nothing to sign … treat them like the other free ones", 9fb2d234…, 2025-09-26T21:02Z) | End per order form f_fba21c2d5d4bbb02983961 ($149/mo from Nov 1), or Answered (Leonard spoke to Maren) | "treat them like the other free ones" is an explicit instruction; the note records no answer given to Maren | SETTLED (A) |
| F3 | DM "on localization: I rang Wen back on Saturday about their Southeast Asia deal" (D05S58U4SAK, 2025-09-29T19:31Z, under parent "we have no localization though") | Lanternfly | Lingora (the localization quote) | "Wen" = Wen Halvorsen, Lanternfly; "Southeast Asia" = the Lanternfly deck. Lingora's contact is Elena; no other Wen/Halvorsen in Frederick's view | SETTLED (A) |
| F4 | Lanternfly: was Wen given the answer? | Answered by Leonard Sat Sep 27, "later": don't write, Jan reminder | Leonard only relayed the decision to Fred. Treat as Park and write to Wen "we'll pick it up in January" (Wen's Sep 22 "any news?" still open) | 418a0a6d… says Leonard "rang Wen back … Southeast Asia has to wait … we'll pick it up again in January". It never says he told Wen, unlike Robert's explicit "I let Rina know" (fc2f69c0…). Both readings give a Jan 5 reminder; they differ on decision label, Answered by, and whether to email Wen | **UNSETTLED** (natural reading leans A) |
| F5 | Robert: "had the call about the Dec 5 indie showcase. we're sitting this one out this year, I let Rina know" (fc2f69c0…, 2025-09-17T18:41Z) | Spotlight Fest | Pixel Harbor (Bay Area *Indie Showcase*) | Dec 5 + Rina match thr 1842712097588195482 and f_9d9cf4e53b1c8607f9c869; call evt_564a16d0f5f6598d0360d5 (Robert + Rina, 18:00–18:30Z the same day). Pixel Harbor is Oct 24, Teodor | SETTLED (A) |
| F6 | Spotlight Fest: "no" or "later"? | No: Answered, no Next date, no reminder | "this year" implies later, so a Jan reminder | "sitting this one out this year" declines this year's event; no revisit promised | SETTLED (A) |
| F7 | Keep-list item "the night pager for backend outages (whatever wakes me up at 3am)" (card 689b662c…) | Pingwise | Some other vendor, or nobody | Pingwise terms f_6c212cbfb31c3ded44ef8a: "on-call alerting for your API and backend endpoints … phone and SMS paging". No other pager/on-call vendor in Frederick's Slack/mail | SETTLED (A) |
| F8 | Jonas Weber's SSL email doesn't name the company | Certwell (keep list) | Unknown vendor, so the cash test gives End | f_cfb172dea30b9f6ac8a340 "Certwell - Renewal Notice", API domain, $89, Oct 20 | SETTLED (A) |
| F9 | Keep-list "App Store and Google Play developer accounts" | No row (nothing in front of us) | Add Keep rows for Apple/Google | No renewal or ask in Frederick's mailbox for Sep 2025 | SETTLED (A) |
| F10 | Pixel Harbor: Fred's Jun 19 "I'll come back to you on this" | Holding reply, so End, Oct 10 | A "later" answer: Answered by Fred, Jan review | The wording promises an answer rather than giving one; tracker f_9d6edd49… "quote in / deposit due Oct 10 if we go" shows it still open | SETTLED (A), weak |
| F11 | Pixel Harbor in scope with only June records? | In | Stale, off | Quote still live (deposit Oct 10, f_614f88a2…); engaged (mixer + reply); July tracker row | SETTLED (A) |
| F12 | Clipforge end date | Oct 15 (Paylane notice) | Jan 15 (tracker "free through Jan 15"), so Park | Pilot agreement f_8d0e0e3a… cap clause; Paylane 1843067564852153540 "pilot now ends on Oct 15" | SETTLED (A) |
| F13 | Clipforge: second written answer owed to Priya ("Want me to line up the next brief?", Sep 22)? | Yes: cancel to billing@paylane.io and also reply to Priya | No: the written cancellation is Clipforge's answer | Guardrails "Everyone who is waiting to hear from us gets a written answer" (leans A); rule 2 "cancel it in writing the way their paper or notice asks" (satisfied by Paylane alone). No record says which | **UNSETTLED** (leans A) |
| F14 | Paylane its own row? | No, folded into Clipforge | Separate row and contact | "Paylane, payments for UGC Studio"; agreement "billed by our payments partner"; README "one row per company" | SETTLED (A) |
| F15 | Wishwave travel (partner books and bills us) | Cash, so End | Not cash under the original guardrails, so Park | Monday change 7e88911312fa9a969f0659a105af59a3 (2025-09-29, #executives) = "the one change I posted in #executives on Monday" | SETTLED (A) |
| F16 | Can Fred accept small terms himself? | No, officers only | Yes for under $500/yr (Slack 0573efd1…, Jul 22) | ESG note bullet 1; Leonard Sep 25 "This replaces what I said in July" | SETTLED (A) |
| F17 | Nintendo portal NDA: does ESG review it? | No | Yes, because it's not ESG's template NDA | ESG triggers are auto-renewal, exclusivity, IP licence, term >12 mo; Arthur cmt_c9a6660d…: "no fee, no exclusivity, nothing about our IP, and either side can end it". The template bullet is an exemption, not an extra trigger | SETTLED (A), weak |
| F18 | Orbit Store featuring: implied IP licence, so ESG? | No ESG | ESG (featuring uses our game) | f_2ae7e3ee… lists no licence; "Term: the promotion only". By contrast Bundlehouse spells its licence out | SETTLED (A), weak |
| F19 | Playfuse 2-yr NDA: ESG (term >12 mo)? | No | Yes | ESG bullet 3: "Mutual NDAs on our template don't need review, whatever their term"; doc is "(ESG Law mutual NDA template)" | SETTLED (A) |
| F20 | Nintendo: Sign or End (dev kits $400–500 each) | Sign (acceptance is free, by Oct 15) | End (kits cost cash) | Arthur: "The kits can wait until after the raise; leaving the acceptance for Leonard or me" | SETTLED (A) |
| F21 | Nintendo already accepted ("NDA Effective 09/04")? | Not accepted | Accepted, so off | cmt_c9a6660d…: "just the start date it will carry" | SETTLED (A) |
| F22 | Nintendo written answer | None | Write to the portal | Guardrails "Portals and no-reply notices don't need one"; sender is no-reply | SETTLED (A) |
| F23 | Nintendo contact | Add none (no person) | Add the portal address with job "Nintendo" | Leonard: "Get each company's contact into Contacts". Records don't say what to do when the only correspondent is a no-reply portal | **UNSETTLED** |
| F24 | Orbit Store: "accepted in our partner portal", so is no answer needed? | Write to Mateo | None (portal) | The portal exemption covers portal notices; Mateo is a person asking "Could that happen by Oct 24?" | SETTLED (A) |
| F25 | Balancy (base only, no filed paper; Leonard deferred it himself) | In, as Answered-later + reminder | Off (not "in front of us"; nobody waiting) | Leonard's definition covers trials engaged by call (Aug 14 cal); guardrails rule 1 handles "later" answers; README sends them to the January review | SETTLED (A), weak |
| F26 | Balancy answer date | Sep 11 (PT, 17:21 −0700) | Sep 12 (UTC 00:21) | Task clock is Pacific | SETTLED (A) |
| F27 | Already-declined Motive Forge on the log? | In (Answered) | Off | Guardrails rule 1 "Note who answered and when"; README "Answered by … for Answered rows" | SETTLED (A) |
| F28 | Nova Rewards | Off | Answered row, or write back | Withdrawn Sep 23; no engagement on record | SETTLED (A) |
| F29 | Rayking | Off | In (Fred wrote "Hi … Leonard forwarded me your email") | That message is a Draft addressed To Leonard only (X-Gmail-Labels "Opened,Drafts") | SETTLED (A) |
| F30 | Google partner check-in (Fred replied) | Off (ad network) | In (engaged partner) | Leonard: "the ad networks … stay on the UA budget call" | SETTLED (A) |
| F31 | Creative/UGC vendors (Clipforge, Streamcast, Brightlane) count as "UA" and stay on the UA call? | In | Off | Leonard's exclusion list is closed ("the ad networks, PlayableX, Craftsman+ and Singular"); none of them is an ad network | SETTLED (A), weak |
| F32 | Playfuse engagement: only an inbound email referring to "our Oct 8 call" | In | Cold, off | NDA paper filed in Frederick's paperwork folder (f_9a7fc4a3…, owner Frederick); call already arranged | SETTLED (A), weak |
| F33 | Hootline: no filed paper | In (sign-up) | Off | Gemma: "Your three social profiles are connected" (sign-up counts) | SETTLED (A) |
| F34 | Which board/list for cards | Harmony Games / To Do | UA/BD board (BD Follow Up / To Do) | Prompt "our Harmony Games board"; Leonard "founders' board To Do list"; Harmony Games board holds founder/board/investor cards | SETTLED (A) |
| F35 | January review date | Mon Jan 5, 2026 | Another "first week of January" date | evt_fd469c29811879519c2c96 (2026-01-05T17:00Z = 9:00 PST); invite thr 1844622183629433486 | SETTLED (A) |
| F36 | Reminder timing | Timed (e.g. 9:00 PT, matching the review) | All-day on Jan 5 | Prompt says only "for that day" | **UNSETTLED** (cosmetic) |
| F37 | Retainly Next date | Jan 5 (review) | Jan 12 (trial ends / cancel deadline) | README: Park gets the January review | SETTLED (A) |
| F38 | Pingwise Next date | Nov 1 (first bill) | Oct 31 (Starter ends) | README Keep = "when it next bills"; terms "$29/month from Nov 1" | SETTLED (A) |
| F39 | End Next date for unaccepted offers (Ascendo, Brightlane, Lingora, Panelpulse, Soundvault, Streamcast, Wishwave, Pixel Harbor) | The offer's own deadline (confirm-by / quote valid / deposit) | Blank (nothing to cancel) | README "the last day to cancel or say no" | SETTLED (A), weak |
| F40 | Markward Next date | None | A date | README "for Sign, the date they need it by, if any"; Markward gives none | SETTLED (A) |
| F41 | Intake email "who would sign it" | "Leonard or Arthur" | Name one officer | Checklist literally says "(Leonard or Arthur)"; no record picks one | **UNSETTLED** (writing both is safe) |
| F42 | Reply to Leonard: "what we're keeping" | Keep rows (Vaultline, Certwell, Pingwise) | Keep plus Park rows | Guardrails rule 3 "Keep … Tell them we're staying" | SETTLED (A), weak |
| F43 | Robert: "cancel every marketing tool we pay for" (80ced6c9…, Sep 25) | Ignore | Apply (End any paid marketing tool) | Leonard names only his own Monday change; Robert's post is opinion | SETTLED (A) |
| F44 | Robert counts as "one of us" for Answered | Yes | No, so write to Rina | Robert is internal, organised the call, and is invited to the review | SETTLED (A) |

**44 forks in total; 5 UNSETTLED:**
- F4 Lanternfly: Answered-later vs Park-and-write.
- F13 Clipforge: is a second answer owed to Priya?
- F23 Nintendo: is a contact added?
- F36 Reminder: timed vs all-day.
- F41 Intake email: who is named as signer.

F4 and F13 are the ones that can change graded writes. F23 changes the contact count (32 vs 33). F36 and F41 are cosmetic.

---

## 4. Coherence issues

1. **Board name mismatch (minor).** Leonard (ESG thread 1844177063117059830, Sep 25) says "our founders' board To Do list", but the Trello board is named "Harmony Games" (640643a3fd8f3ca308d9318e). The prompt bridges the two.
2. **Framewell note placement.** The Framewell side note (9fb2d234…) is threaded under a Playtestcloud post (parent 1758513190.847889). "side note" and "Maren" carry it, but it's an odd home.
3. **Lumencloud deadline wording.** Aiden says "Thanks for applying … qualifies" yet also "Applications for this cohort close Oct 31", and the doc says "Apply by Oct 31". If we've already applied, it's unclear whether Oct 31 is the signing deadline. The Next date is Oct 31 either way.
4. **Nintendo job title (base).** The registration mail (1842359398719557772) lists Frederick's Job Title as "VP of Marketing", while the persona is Co-founder. It doesn't affect officer status, since ESG names only Leonard and Arthur.
5. **Craftsman+ address (base artefact).** Craftsman+'s "Brian Cooper" mails from brian.foster@harmonygames.co (1823332883409810377), an internal-looking address for an external vendor. Excluded by name anyway.
6. **"First week of January" (minor).** The guardrails say the review is in the "first week of January"; the event is Mon Jan 5, 2026. That's inside Jan 1–7, but not inside the calendar week that contains Jan 1 (Mon Dec 29–Sun Jan 4). The event settles it.
7. **Stale tracker is deliberate, not incoherent.** The tracker f_9d6edd49… says Clipforge is "free through Jan 15", which conflicts with Paylane's Oct 15. The pilot agreement's 20-video cap clause reconciles them.
