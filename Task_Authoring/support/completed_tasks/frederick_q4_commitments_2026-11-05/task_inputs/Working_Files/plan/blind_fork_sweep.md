# Blind fork sweep: Frederick Corp Ops vendor/partner backlog (clock Wed Oct 1, 2025)

I worked read-only and did not open any answer files. Sources were the three plan dumps, plus Frederick-scoped base reads: Gmail threads in his mailbox, the Slack channels and DMs he belongs to (each checked with `persona_view can-see`), gdocs shared with him, his gcal, and the Trello and Contacts exports. One check did not finish: the full-Gmail grep for the seeded vendor names timed out. The non-Gmail grep found no base mention of any seeded vendor name.

## 0. Summary

- **Forks found: 41. 18 are UNSETTLED and 23 are settled or settled-lean** (settled-lean means a record points one way but a strict reader could still argue the other).
- **Highest-risk items:**
  1. **PlayableX is missing from the dumps but very live in base.** Frederick himself paused it on Sep 29, and PlayableX re-scheduled the start for Nov 3, which puts the cost inside the cash window. Whether it is in scope depends on whether "ad networks and Singular (they stay on the UA budget call)" also covers playable vendors.
  2. **Balancy is missing from the dumps and fits Leonard's scope literally.** It had a call, a trial and pricing offer, and Leonard's "we'll circle back" reply.
  3. **Nintendo.** It is unclear whether it belongs in the log, and whether its decision is Sign or End (on the dev-kit cost).
  4. **Framewell.** Leonard's "treat them like the other free ones" fits both Park and Sign.
  5. **Brightlane and Ascendo Next date.** The only date on either is the Oct 1 start.
  6. **Playfuse date.** The paper says "before the Oct 8 call".
  7. **Motive Forge "pass for now" and Spotlight Fest "maybe next year".** It is unclear whether these are "later" answers, which would change the Next date and the January reminder.
  8. **Pay-when-you-order quotes** (Soundvault, Lingora, Glyphworks, Driftwood, Pressbeam, Echohall). No guardrail sentence says whether these fall under the cash test or Park.

## 1. Forks table

U = UNSETTLED, S = settled, S-lean = settled-lean.

| # | Company / field | Reading A | Reading B | Strongest argument for B | Settling record (quote) or status |
|---|---|---|---|---|---|
| 1 | **Framewell: Decision** | Park (Next date Jan 5 2026) | Sign (taking Pro means accepting the order form; card; maybe ESG) | Rule 4 is checked before rule 5: "If it costs nothing before January but taking it means someone has to accept terms or sign for the company". Framewell sent an **order form** (f_fba21c2d5d4bbb02983961) and asked "let me know by mid-October if we should set it up". Leonard's "treat them like the other free ones" (Slack 9fb2d23420c7e01ca163571f4129c912) covers both the free Sign rows (Markward, Lumencloud, Orbit) and the Park rows. | **U.** Nothing says whether the hold needs the order form signed. If Sign, the Next date is "mid-October", which is itself undefined. |
| 2 | Framewell: Answered vs Park | Park | Answered by Leonard (his call) | "Framewell called me back" means Leonard spoke to them. | **S-lean.** The Slack message reports Framewell's offer ("they'll hold the Pro plan at no charge until Feb 1"), not an answer from us, and then tells Frederick how to treat them. |
| 3 | Framewell: ESG trigger | No ESG | ESG (Pro auto-bills $149/month from Feb 1, "month to month") | "then $X/month unless you cancel" counts as automatic renewal | **U, but only if #1 resolves to Sign.** If Park, nobody signs, so no ESG. |
| 4 | Lanternfly: "later" vs final | Answered, "later", Next date Jan 5 2026 | Final no, blank Next date | "no new publishing deals before the raise" reads as a refusal | **S.** DM 418a0a6d6c29b7b67ce0ffb270c78c1e: "told them no new publishing deals before the raise and that we'd talk again in January". |
| 5 | Lanternfly: Answered by / when | Leonard, phone call, Sat Sep 27 | Frederick, Sep 10; or Sep 29 as the date | Frederick replied first: "we'll take a look and get back to you" | **S.** That reply was a holding note; Wen chased again on Sep 22. Leonard's DM (sent Mon Sep 29) says "on Saturday", which is Sep 27. |
| 6 | Lanternfly: Sign/ESG | No card, no ESG | Sign plus ESG (deck f_5dbbaf5b251d5261427eb1: "2-year term, exclusive") | The triggers are real | **S.** Guardrails: "stop at the first one that fits". Rule 1 (Already answered) fits first. |
| 7 | Kinetic Arcade: Decision | Sign, card and ESG | Park/End under Leonard's "no new publishing deals before the raise" | Leonard stated that publishing policy to Lanternfly (DM 418a0a…); Kinetic's paper is a publishing LOI | **S-lean.** Leonard's email limits the rules to "the runway guardrails doc … plus the one change I posted in #executives on Monday". The Lanternfly DM is neither. |
| 8 | Kinetic: ESG trigger | Yes (exclusivity) | — | The term is "12 months", which is not *over* 12 | **S.** Exclusivity triggers by itself: "Exclusivity: 12 months from signature" (f_6252955f500f81e3aacbef). |
| 9 | Pingwise: Keep vs End | Keep (the night pager), Next date Nov 1 | End: drop back to the free email-only tier before Oct 31 | Arthur's list doesn't name Pingwise | **S.** Card 689b662c…: "the night pager for backend outages (whatever wakes me up at 3am)". Pingwise paper: "on-call alerting … phone and SMS paging". Searches of Frederick's Gmail/Slack/Docs for PagerDuty, Opsgenie, pager and on-call found no competing pager. |
| 10 | **Clipforge: who gets the written answer** | Cancellation in writing to **billing@paylane.io** | Also (or only) Priya, PERSON_9704_EMAIL | Leonard: "Everyone who is waiting to hear from us should get a written answer." Priya asked on Sep 22: "Want me to line up the next brief?" | **U for Priya.** The cancellation address is settled by the Paylane notice ("write to billing@paylane.io by Oct 15") and the paper ("Cancel in writing to the billing address on your notice"). Nothing says whether Priya is owed a separate reply. |
| 11 | Clipforge vs a separate Paylane row | One row: Clipforge | Add a Paylane row | Paylane is a different company and sent its own notice | **S-lean.** Paper: "billed by our payments partner"; notice signed "Paylane, payments for UGC Studio". |
| 12 | Clipforge: Next date | Oct 15, 2025 | Jan 15, 2026 (July tracker: "free through Jan 15") | The tracker and the pilot paper both say Jan 15 | **S.** The later Paylane notice (Sep 12) says the cap was reached: "pilot now ends on Oct 15 … cancel … by Oct 15". |
| 13 | Pixel Harbor: Next date | Oct 10 | Oct 9 | "free before the deposit is paid" | **S-lean.** Quote f_614f88…: "deposit $2,400 due by Oct 10, 2025 to hold the booth". |
| 14 | **Brightlane: Next date** | Oct 1 (start date) | Sep 30 (day before start), Sep 26–28 ("book the team this week", already past), or blank | The only dates are "Start: Oct 1, 2025" and "this week" in an email sent Fri Sep 26 | **U.** There is no cancellation or deadline clause; the paper says only "To start: reply to confirm". |
| 15 | **Ascendo: Next date** | Oct 1 | Sep 30 / blank | Only "$900/month from Oct 1" and "kick off on Oct 1" | **U.** |
| 16 | **Pay-when-you-order quotes** (Soundvault, Lingora vs Glyphworks, Driftwood, Pressbeam, Echohall) | End when the offer can only be taken inside Q4 (Soundvault quote ends Oct 15, Lingora Oct 3); Park when the offer survives into 2026 (Glyphworks Jan 31, Driftwood Feb 28, Pressbeam "any time before launch", Echohall "whenever") | (a) Everything with a price is End (Glyphworks "$640, payable when ordered" would cost cash if accepted; "say no"); or (b) everything is Park (nothing is owed unless we order, so it is "free until January") | The cash test says "would cost us cash", with no tie to when we accept. Park says "Everything else that's free until January". Neither defines quote expiry. | **U as a class.** The A split is the most natural reading, but no guardrail text addresses it. |
| 17 | Reviewly: Next date | Oct 19 | Oct 20 | Oct 20 is the only printed date | **S.** f_4bdfb8…: "moves to Growth at $79/month on Oct 20, 2025 unless cancelled before then". |
| 18 | Reviewly: how to cancel | Email to Hana (in writing) | In the app, with no email | Paper: "Cancel: in the app or by email to your onboarding contact" | **S-lean.** Guardrails: "cancel it in writing". |
| 19 | Wishwave: Decision | End (Next date Oct 17) | Park (partner books the travel) | Guardrails: "Travel and event costs count only when we book them ourselves" | **S.** Slack 7e88911…, Mon Sep 29: "travel and event costs count as cash even when a partner books them and bills us"; Leonard's email adopts that change. |
| 20 | Certwell: Keep vs Sign | Keep (Next date Oct 20) | Sign (confirming the renewal accepts terms) | "Reply to confirm" | **S.** Rule order puts Keep (3) before Sign (4); the card lists "Certwell SSL cert for the API domain". |
| 21 | **Bundlehouse: Decision** | Sign (card, ESG for IP licence and 18 months; Next date Nov 1) | Park (no signature or terms requirement anywhere) | The email says only "no cost to join … includes a licence"; Freya asks "do you want me to hold a spot?" | **U-lean-A.** Granting an IP licence implies accepting terms, but no record says sign/accept. A secondary fork: "Submissions close Nov 1" gives Nov 1 vs Oct 31. |
| 22 | Orbit Store: written answer | Yes, to Mateo | No (guardrails: "Portals and no-reply notices don't need one") | Acceptance happens in the partner portal | **S-lean.** Mateo writes personally and nudged on Sep 30. |
| 23 | Orbit: ESG | No | Yes (featuring implies an implied licence of our game's name/art) | — | **S-lean.** Summary f_2ae7e3…: "Fees: none / Term: the promotion only"; no IP or exclusivity terms. |
| 24 | **Markward: ESG** | No | Yes ("Term: month to month" is a rolling automatic renewal) | ESG: "Anything with an automatic renewal" | **U-lean-A.** |
| 25 | **Markward: written answer owed?** | Yes, to Leah | No (she isn't asking anything: "ready whenever you accept the terms") | Guardrails limit replies to "Everyone who is waiting to hear from us" | **U.** |
| 26 | Markward: Next date | Blank | — | — | **S.** README: "for Sign, the date they need it by, if any"; no date in thread or paper. The July "$500 a year" Slack is superseded: "This replaces what I said in July about Fred signing small stuff himself." |
| 27 | **Playfuse: Next date** | Oct 8 | Oct 7 | Paper: "before the Oct 8, 2025 call" | **U.** No call time in Frederick's calendar or the dumps. |
| 28 | Playfuse: ESG | No (mutual NDA on template) | Yes (2-year term) | The base HG MNDA template (gdocs f_449c3c155fd6963c4c63de) dates from 2023-04-21, before ESG was engaged on Aug 27, 2025, so "our template" may not mean ESG's | **S-lean.** Paper: "Mutual NDA (Harmony Games template, ESG Law)"; ESG: "Mutual NDAs on our template don't need review, whatever their term". |
| 29 | Hootline: Park vs Sign/ESG | Park | Sign plus ESG ("then $39/month unless you cancel") | Matches the auto-renewal trigger | **S-lean.** Staying on the promo needs no new acceptance, and ESG review applies "before anyone signs". The $390 annual plan would cost cash, so it is not an option. |
| 30 | **Written answer owed: Retainly, Benchmarkly** (also softer: Echohall, Pressbeam, Driftwood) | Yes (Park says "Tell them we'll pick it up in January") | No (nobody is waiting) | Retainly: "Reply if you want help connecting your events." Benchmarkly: "if you want it." Driftwood only sent the quote. | **U.** The two guardrail sentences pull opposite ways. |
| 31 | **Echohall: Decision** | Park | End (say no to Pro) | Pro costs "$49/month from the day you upgrade" | **U-lean-A.** "The free plan carries on as it is until then." |
| 32 | Cloudlark, Tilecast: Park vs Sign | Park | Sign (activation or pilot needs terms) | Credits and pilots usually carry terms | **S-lean.** Papers: "Activation: when you're ready; nothing owed" and "No cost during the pilot". Neither mentions terms. |
| 33 | **Motive Forge: "later"?** | Final no, blank Next date, no reminder | "Later": Next date Jan 5, reminder | Arthur: "we're keeping art in-house **this quarter**, so we'll pass **for now**" | **U.** |
| 34 | Motive Forge: Answered by | Arthur (email, Sep 19) | Arthur and Frederick | Hugo wrote "Hi Frederick, hi Arthur"; Frederick was cc'd | **S.** The reply is from arthur.blake@ only. |
| 35 | **Spotlight Fest: "later"?** | Final no for the Dec 5 showcase, blank Next date | "Later" (Jan 5, reminder) | Robert: "told them we'll skip this year's showcase, **maybe next year**" (Slack 80ced6c9…; evt_564a16…) | **U.** |
| 36 | Spotlight Fest: Answered by | Robert (call, Sep 17) | Robert and Frederick (Frederick was invited to the call) | evt_564a16…: "organizer Robert; Frederick invited" | **S-lean.** Robert's Slack is first person ("told them"); calendar note "- R". |
| 37 | **Nintendo: in log, and Decision** | In scope; Sign (an officer must accept the Global ToS and NDA; card; Next date Oct 15) | (a) End: the point is "order dev kits ($400–500 per kit)", which is Q4 cash; or (b) not a log row, since it is a portal | ZOM-567 title: "Switch: order dev kits" | **U.** Arthur's comment cmt_c9a666…: "stays limited until a company officer accepts the Global ToS and NDA … The request lapses Oct 15". Side forks: Next date Oct 15 vs Oct 14; no human contact (sender SVC_0208 is no-reply). |
| 38 | **Nintendo: ESG intake** | No | Yes (third-party NDA and ToS, not our template; terms unknown) | The ESG template carve-out doesn't apply | **U.** No visible record states the ToS term, renewal, exclusivity or licence. |
| 39 | Nova Rewards: in or out | Out | In ("Sorry for the back and forth" suggests engagement) | — | **S-lean.** Sep 23: "I'm withdrawing this offer for now", so nothing is in front of us. |
| 40 | **Balancy (base): in or out** | In: Answered, Leonard, Sep 11, "later", Jan 5 | Out (not in dumps) | Call Aug 14 with Leonard and Frederick, 1-month trial, $500/month pricing (#executives Aug 14). Leonard Sep 11: "we'll circle back with you as soon as we get some bandwidth" | **U.** It meets every clause of Leonard's scope; nothing excludes it. "Later" vs final is a sub-fork. |
| 41 | **PlayableX (base): in or out, and Decision** | Out (playables are UA spend that "stay on the UA budget call") | In: Answered by Frederick, Sep 29 (later); or End (restart Nov 3 costs about $4K inside the window) | Leonard excludes only "the ad networks and Singular", and PlayableX is neither | **U.** UA spend buckets f_7bacf15c…: "Real UA bucket: Unity, Meta, playables … playables count here". Leonard (#executives Sep 15): "rather than spending 4K on a playable". Frederick in #HG-playablex Sep 29 19:42Z: "pause development of the playable for a month or so". PlayableX Sep 30: "We're planning the new start date … November 3rd." |

## 2. Scope census (base records not in the dumps)

| Candidate | Evidence (Frederick-visible) | Fits scope? |
|---|---|---|
| **PlayableX** (playable ad vendor) | Slack channel C08H78VJG80 (Frederick is a member). Aug 26 Leonard kicks off the Zombie Match 3D playable; Sep 15 Frederick: "lets go with Scenario 1"; kickoff moved to Oct 6; **Sep 29 Frederick: "pause development of the playable for a month or so"**; Sep 30 PlayableX: "new start date … November 3rd". Cost about $4K (#executives 2025-09-15T18:31). | **Ambiguous (fork #41).** Literal clause: in (not an ad network, and engaged). Bucket doc: playables are UA-budget items. If in, Frederick's own Sep 29 message is an "Answered (later)" whose restart lands in Q4. |
| **Balancy** (LiveOps tool) | Thread 1840501641217286806: Aug 15 demo recap to Leonard and Frederick; 1-month trial offer; Leonard Sep 11: "company priorities have shifted … we'll circle back"; Balancy Sep 15: "We'll keep you posted". #executives Aug 14: "$500/month up to 10K DAU … I'm super inclined to use them". | **Yes by the literal definition** (offer and trial, call and reply, not excluded). It would be an Answered row: Leonard, Sep 11; "later" plausibly gives Jan 5. Contact: PERSON_0527 (Growth & Partnerships Manager). |
| Craftsman+ (Brian Cooper; his address appears as brian.foster@harmonygames.co) | Thread 1823332883409810377: Sep 9 "Would love to touch base"; Frederick replied Sep 9: "We aren't spending on UA at the moment." | Weak. It is a UA creative agency with a vague ask, not an ad network. If included, Answered by Frederick on Sep 9. Low risk. |
| Playtestcloud | July tracker: "player tests / running / Leonard owns"; Sep 22 results post | No ask or offer in front of us. Low risk, but it appears in a seeded decoy tracker. |
| Rayking Game | Thread 1842348778705877030: Leonard "Fwd … Should we explore for DD?" Frederick's message went **to Leonard** (no SENT label). DM Sep 4: Frederick "I'll reach out to someone over There on linkedin". | Out: "cold pitches … including ones we only forwarded around internally". No record of the LinkedIn contact happening. |
| Google (Tim, Ads partner) | Thread 1817715521687421486, Frederick's Sep 5 deferral | Out: ad network. |
| Adjoe (AppCamp invite, payment reminder, spend) | 1833464394449700499 (Frederick declined Jun 21); DM Sep 6 "I'll ping them" | Out: ad network. |
| Unity, Meta, AppLovin | #executives, applovin channel | Out: ad networks. |
| Singular | 1837914783244638008 | Out: named. |
| Mattel (RFP, NDA) | #executives Sep 2 and Sep 4; 1841567055589252118 | Out: named. |
| NCsoft, Dentsu, [PERSON_NAME_0854] co-dev, GRx, Makers, LVP, GFR, SEMC, a16z speedrun, SVB | Bridge-round threads | Out: investor work (NCsoft and [0854] are strategic or acquirer talks Leonard is driving, and we are the ones waiting). |
| Playable Factory, InterCo, Gamesforum SF, Solsten/Elaris, Creative IQ, "Re: influencers" | No Harmony Games reply in any Jun–Sep thread (sender census of Frederick's mailbox) | Out: cold. |
| ESG Law | Engagement letter signed Aug 27 | Out: counsel, nothing pending. |
| Nintendo (base portal emails plus seeded ZOM-567) | 1842358947604469113 and 1842359398719557772; Slack Sep 4 "I registered an account" | Probably in (terms in front of us, Frederick's sign-up), but see forks #37–38. |
| Nova Rewards | Seeded; withdrawn | Out (#39). |

Method: I listed every thread in Frederick's mailbox with a message dated Jun 1–Oct 1, 2025 that had a Harmony Games sender (79 threads) and checked the non-calendar ones. I also ran a call/trial phrase sweep over externally-sent mail, a keyword sweep of Frederick's Slack (#executives in full, his DMs, the external channels he belongs to), and checked open Trello cards. The leapblock channel is not visible to Frederick (can-see: NO).

## 3. Coherence issues

1. **The UA spend buckets doc (seeded, "Fred, Sep 16") conflicts with base Slack.** The doc says "Real UA bucket: Unity, Meta, playables. Paused until we know about the raise … Adjoe … the only UA spend that runs". But on Sep 29 Leonard writes "I set budget to $150/campaign/day on IOS" (#executives 22:48Z), and on Sep 30 Frederick writes "clicks are up 5x … I can juice it more". Unity was live after the "pause".
2. **Lanternfly policy vs base publishing posture.** Leonard's DM (Sep 29) says "no new publishing deals before the raise". In base, Leonard pushes Domino Delights publishing (Exec Sync doc Aug 28: "should we consider giving up global publishing rights?"; GRx Sep 3: "Domino Delights is pursuing a publisher"). Frederick also asked about "publishing outreach" on Sep 24 (DM D05S58U4SAK). The DM also invites the #7 Kinetic Arcade fork.
3. **Nintendo NDA status.** The base "Registration Completed" email (Sep 4) shows "NDA Effective: 09/04/2025". Arthur's seeded comment says the account "stays limited until a company officer accepts the Global ToS and NDA". These are reconcilable (the approver step is separate) but they read as a conflict.
4. **Playfuse paper vs base template.** The paper calls the NDA "Harmony Games template, ESG Law". The base "Harmony Games mnda copy" (f_449c3c…) was created 2023-04-21, before ESG's Aug 27, 2025 engagement.
5. **Framewell and Lanternfly cite calls with no other trace.** "Framewell called me back" and "I called the Lanternfly people back" imply Leonard had made earlier calls, but neither thread shows Leonard. This is minor.
6. **Clipforge timing.** Paylane says the cap was reached on Sep 12, yet Priya on Sep 22 delivers "the latest batch" and offers "the next brief". This is minor tension.
7. **Playtestcloud post date.** The seeded Framewell reply sits under "his Sep 22 Playtestcloud results post". The base post is 2025-09-22T03:53Z, which is Sep 21 evening PT.
8. **Hootline timing.** On Sep 24 Gemma writes "a quick note before the promo ends", but the promo runs to Jan 31. This is minor.
9. **Nova Rewards.** "Sorry for the back and forth" has no visible back-and-forth.
10. **Base address collision.** An external Craftsman+ CEO, "Brian Cooper", uses brian.foster@harmonygames.co, which is an internal-looking address (internal Brian Foster is an HG artist active in the PlayableX channel). This is a base anonymisation artifact.
11. **Records that cite later records.** I found none: the ESG note (Sep 24), Leonard's reply (Sep 25), the guardrails (Sep 26), the Monday change (Sep 29), the DM (Sep 29), the README and Leonard's email (Sep 30, 23:20Z, before the 17:00 PT cutoff), and the ZOM-567 comment (Sep 25, after the Sep 23 issue) are all in order. I could not verify three creation times, which the dumps don't show: the checklist doc (it must exist by Sep 25), the README (it must exist before Leonard's Sep 30 email), and the Trello keep card (it must exist by Sep 26).

## 4. Independent log

Abbreviations used in the table below:
- **WA**: written answer, with recipient.
- **Card**: Trello card on the founders' board To Do list.
- **ESG**: ESG Law intake email.
- **Jan**: calendar reminder on Jan 5, 2026 (evt_fd469c29811879519c2c96).
- **"Engaged"** means the scope clause "call / reply / sign-up / paper".

| Company | Scope | Decision | Answered by | Next date | WA → address | Card | ESG | Contact to add | Jan |
|---|---|---|---|---|---|---|---|---|---|
| Framewell | In (call "Tuesday" plus order form) | Park (fork #1) | — | 2026-01-05 | Maren, PERSON_9701_EMAIL | No | No | Maren (Framewell) | Yes |
| Lanternfly Publishing | In (call plus Frederick's reply) | Answered (later) | Leonard, call Sat Sep 27 | 2026-01-05 | No | No | No | Wen Halvorsen, PERSON_9702 | Yes |
| Pingwise | In (existing agreement) | Keep (night pager) | — | 2025-11-01 | Dana Whitfield, PERSON_9703 ("staying") | No | No | Dana Whitfield | No |
| Clipforge | In (pilot sign-up, agreement, kickoff) | End | — | 2025-10-15 | Cancel to billing@paylane.io (fork #10: plus Priya, PERSON_9704) | No | No | Priya Raman | No |
| Pixel Harbor Events | In (mixer, reply, quote) | End | — | 2025-10-10 | Teodor Lind, PERSON_9705 | No | No | Teodor Lind | No |
| Brightlane Studio | In (call plus proposal) | End | — | 2025-10-01 (fork #14) | Ines, PERSON_9706 | No | No | Ines | No |
| Soundvault | In (Frederick requested quote) | End (fork #16) | — | 2025-10-15 | Rafael Moreno, PERSON_9707 | No | No | Rafael Moreno | No |
| Reviewly | In (trial sign-up) | End (trial turns paid Oct 20) | — | 2025-10-19 | Cancel in writing to Hana, PERSON_9708 | No | No | Hana | No |
| Streamcast Talent | In (call) | End | — | 2025-10-31 | Kofi, PERSON_9709 | No | No | Kofi | No |
| Lingora | In (Frederick requested quote) | End (fork #16) | — | 2025-10-03 | Elena Petrova, PERSON_9710 | No | No | Elena Petrova | No |
| Panelpulse | In (call) | End | — | 2025-10-06 | Arjun, PERSON_9711 | No | No | Arjun | No |
| Ascendo | In (call) | End | — | 2025-10-01 (fork #15) | Lucia, PERSON_9712 | No | No | Lucia | No |
| Wishwave | In ("Great chatting") | End (Monday change) | — | 2025-10-17 | Sven, PERSON_9713 | No | No | Sven | No |
| Vaultline | In (existing service) | Keep (on list) | — | 2025-10-12 | Mila, PERSON_9714 ("keep running") | No | No | Mila | No |
| Certwell | In (existing cert) | Keep (on list) | — | 2025-10-20 | Jonas, PERSON_9715 ("renew") | No | No | Jonas | No |
| Kinetic Arcade | In (call plus LOI) | Sign | — | 2025-10-20 | Noor, PERSON_9716 | Yes | Yes (exclusivity) | None (Noor already in Contacts) | No |
| Lumencloud | In (paper) | Sign | — | 2025-10-31 | Aiden, PERSON_9717 | Yes | Yes (36-month term) | None (Aiden already in Contacts) | No |
| Bundlehouse | In (chat plus deck) | Sign (fork #21) | — | 2025-11-01 | Freya, PERSON_9718 | Yes | Yes (IP licence; 18 months) | Freya | No |
| Orbit Store | In (paper) | Sign | — | 2025-10-24 | Mateo, PERSON_9719 | Yes | No | Mateo | No |
| Markward | In ("As discussed" plus click-through terms) | Sign (officer only; July rule replaced) | — | (none) | Fork #25 (Leah, PERSON_9720) | Yes | No (fork #24) | None (Leah already in Contacts) | No |
| Playfuse | In (paper) | Sign | — | 2025-10-08 (fork #27) | Iris, PERSON_9721 | Yes | No (template carve-out) | Iris | No |
| Hootline | In (sign-up) | Park | — | 2026-01-05 | Gemma, PERSON_9722 ("stay on promo") | No | No | Gemma | Yes |
| Glyphworks | In (Frederick requested quote) | Park (fork #16) | — | 2026-01-05 | Tomas Novotny, PERSON_9723 | No | No | Tomas Novotny | Yes |
| Cloudlark | In (chat) | Park | — | 2026-01-05 | Yara, PERSON_9724 | No | No | Yara | Yes |
| Echohall | In (community sign-up) | Park (fork #31) | — | 2026-01-05 | Bruno, PERSON_9725 (soft) | No | No | Bruno | Yes |
| Pressbeam | In (call) | Park | — | 2026-01-05 | Ava, PERSON_9726 | No | No | Ava | Yes |
| Retainly | In (trial sign-up) | Park (turns paid Jan 12, outside window) | — | 2026-01-05 | Fork #30 (Omar, PERSON_9727) | No | No | Omar | Yes |
| Quillcraft | In (beta sign-up) | Park | — | 2026-01-05 | Nadia, PERSON_9728 | No | No | Nadia | Yes |
| Tilecast | In (call) | Park | — | 2026-01-05 | Kenji, PERSON_9729 | No | No | Kenji | Yes |
| Benchmarkly | In (Frederick's request) | Park | — | 2026-01-05 | Fork #30 (Clara Weiss, PERSON_9730) | No | No | Clara Weiss | Yes |
| Loopnote | In (trial sign-up) | Park | — | 2026-01-05 | Pavel, PERSON_9731 | No | No | Pavel | Yes |
| Driftwood Audio | In (Frederick's request) | Park | — | 2026-01-05 | Sofia Marin, PERSON_9732 (soft) | No | No | Sofia Marin | Yes |
| Motive Forge | In (quote plus reply) | Answered | Arthur, email Sep 19 | blank (fork #33: Jan 5) | No | No | No | Hugo Lambert, PERSON_9733 | Fork |
| Spotlight Fest | In (call) | Answered | Robert, call Sep 17 | blank (fork #35: Jan 5) | No | No | No | Rina, PERSON_9734 | Fork |
| Nintendo | In? (fork #37) | Sign (fork) | — | 2025-10-15 | No (portal) | Yes | Fork #38 | None (no person) | No |
| Nova Rewards | Out (withdrawn Sep 23) | — | — | — | — | — | — | — | — |
| *Balancy (base)* | Fork #40 | Answered (later) | Leonard, email Sep 11 | 2026-01-05 | No | No | No | PERSON_0527 | Yes |
| *PlayableX (base)* | Fork #41 | Answered (later) or End | Frederick, Slack Sep 29 | ? | ? | No | No | PERSON_6078 (Slack only) | ? |

**Totals on the dump-only reading (35 rows):**
- Decisions: Keep 3, Sign 7 (including Nintendo), End 10, Park 12, Answered 3.
- Actions: 3 ESG intakes, 7 cards, 13 January reminders (12 Park plus Lanternfly).

**Reply to Leonard:**
- **Keep:** Vaultline, Certwell, Pingwise.
- **Waiting on signature:** Kinetic Arcade, Lumencloud and Bundlehouse (all three also going to ESG), plus Orbit Store, Markward, Playfuse, and Nintendo.

Name forms: about 20 contacts appear only by first name in the dump, because the From display names were not extracted. The values cannot be pinned beyond that.
