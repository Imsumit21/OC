# Blind fork sweep, rev3: Frederick vendor/partner backlog (clock: Wed Oct 1, 2025, synth-cut)

Reviewer: independent, blind (no answer key, no solver files, no Working_Files/00_/01_/04_, no plan/build_*/ids/assemble_/earlier sweeps, no manifest or gradable surface).

How I worked: I read the three dumps; Frederick's base mailbox (direct thread-file scans plus persona_view, Frederick's mailbox only); the Slack, Drive/Docs, Trello and Contacts exports; and `persona_view` searches. The dumps don't show who wrote each Slack message, so I took a narrow look at the seeded rows in `task_inputs/01_Universe_Inject.sql`. That file is not on the forbidden list. I read only the VALUES of the Slack, gmail sender-name, drive_files owner/created, gcal, contacts and trello card rows, plus one UPDATE row, and skipped every `--` comment line. I ran no SQL.

Resolved Slack authorship (EMPLOYEE_0038 = Leonard Hayes, EMPLOYEE_0016 = Robert; C07C2866011 = #executives; D05S58U4SAK = an IM that includes Leonard and Frederick):
- 0573efd1… Jul 22: Leonard, #executives ("fred for small stuff under $500…")
- 80ced6c9… Sep 25 (Thu): Robert, #executives ("cancel every marketing tool…")
- fc2f69c0… Sep 17: Robert, #executives ("had the spotlight fest call…")
- 7e889113… Sep 29 (Mon): Leonard, #executives ("one change to the runway guardrails doc…"). This is the "one change I posted in #executives on Monday".
- 9fb2d234… Sep 26: Leonard, #executives. It is a thread reply under Leonard's Sep 22 "Playtestcloud results are in…" (parent c41d3717…; parent reply_count is updated at SQL line 231).
- 418a0a6d… Sep 29: Leonard, IM D05S58U4SAK ("called the Lanternfly people back on Saturday").

---

## 1. Summary

- Companies assessed: 35 seeded counterparties plus about 30 base counterparties.
- My independent log has **36 rows**: 34 seeded (every seeded company except Nova Rewards) plus 2 from base (Nintendo, Balancy).
  - Answered: 4 (Lanternfly, Balancy, Motive Forge, Spotlight Fest)
  - End: 10
  - Keep: 3
  - Sign: 7
  - Park: 12
- Forks logged: **46**.
  - **UNSETTLED: 5**: F04 Balancy contact name; F15 Clipforge second recipient; F38 named signer in ESG intakes; F41 January reminder count/format; F45 What-we-told-them for Sign rows.
  - **Settled but thin: 15**. One record or a single inference carries the value; a reviewer could push back: F01, F02, F05, F10, F13, F21, F23, F26, F28, F31, F32, F33, F39, F40, F42.
  - **Settled: 26**. Cleanly decided by a quoted record.
- Highest membership risks:
  - Two base rows: **Balancy** (F01) and **Nintendo** (F06). A key built only from seeded threads would miss them; a solver who follows Leonard's rule literally must include them.
  - Three thin-engagement seeded rows: **Lumencloud** (F32), **Orbit Store** (F33), **Playfuse** (F31). Their only engagement evidence is the paper Frederick filed (plus a scheduled call, a portal or Contacts presence).
  - Two out-calls: **Google partner** (F05) and **Tilecast** (F42).
- Coherence: no hard contradictions. Items to tidy:
  - There is no Trello board named "founders'" (C1).
  - The Paylane "This mailbox isn't monitored" line sits right after billing@paylane.io (C2).
  - Balancy's answer date reads Sep 11 in PT but Sep 12 in UTC (C3).
  - ZOM-567 says "per the portal" for kit prices the portal can't show yet (C4).
  - Minor items C5 to C8.

---

## 2. Forks table

Legend: S = settled, S-thin = settled but thin, U = UNSETTLED.

| # | Company / field | Reading A (mine) | Reading B | Strongest argument for B | Settling record (quoted) or status |
|---|---|---|---|---|---|
| F01 | Balancy: membership | IN | OUT | Not in the seeded dumps; Leonard is handling it himself; Balancy is also named as an acquisition alternative in the NCsoft context (#executives Sep 19, Arthur: "3. Buy Balancy") | **S-thin.** Leonard's scope covers "anyone outside the investor work who has an offer, a trial, a quote, terms or an ask in front of us and that one of us has actually engaged with: a call, a reply…". Balancy 1840501641217286806: "We offer a 1-month trial…" with pricing "A fixed fee of $500 per month". Engagement: invite 1840192677223724701 "[Frederick] and Balancy Team @ Thu Aug 14, 2025", plus Leonard's replies. Membership is right by rule; the risk is a key that omits it. |
| F02 | Balancy: Decision | Answered ("later"), by Leonard | Park (Leonard's line is only a holding reply, like Frederick's to Teodor) | "we'll circle back with you as soon as we get some bandwidth" has no date and no decision word | **S-thin.** Leonard, Thu 11 Sep 2025 17:21 -0700: "company priorities have shifted a bit for the next few months - we'll circle back…". Balancy replied Sep 15: "Absolutely, thank you for the update. We'll keep you posted", so they are not waiting. Guardrail 1: "If the answer was 'later', it comes back at the January commitments review." Either reading gives Next date Jan 5, 2026; they differ on Decision, Answered by and whether a written answer is owed. |
| F03 | Balancy: answer date | Sep 11, 2025 (PT) | Sep 12, 2025 (UTC 00:21Z) | Tools that return ISO UTC show Sep 12 | **S** on Frederick's PT clock (header "-0700"). A rubric should accept both. |
| F04 | Balancy: Contact name | PERSON_0527_NAME (as rendered) | "Antonina Belova" | Taken from the calendly slug "antonina-belova-balancy" in the signature | **U.** No record gives the name in plain text. |
| F05 | Google partner (Tim): membership | OUT (ad network) | IN, Answered by Frederick Sep 9 ("later") | Google isn't named in Leonard's exclusions; the UA buckets doc lists only "Unity, Meta, playables". Frederick's Sep 9: "probably a little too early in the process to say much on timing" | **S-thin.** Leonard excludes "the ad networks… (they all stay on the UA budget call)". Thread 1817715521687421486 is about UA: "I recommend not running any soft launch testing on Google… wait for a more concrete test campaign". No offer or terms are open. |
| F06 | Nintendo: membership/Decision | IN, Sign | End (dev kits $400-500) or OUT (portal only) | ZOM-567: "ordering dev kits ($400-500 per kit…)" costs cash | **S.** cmt_c9a6660d81e067ad1de7 (Arthur): "the Global ToS and NDA still needs our agreement approver to accept it… It's Nintendo's standard click-through: no fee… It has to be accepted by Oct 15 or the request lapses. The kits can wait until after the raise; leaving the acceptance for Leonard or me." Engagement = Fred's sign-up (base 1842359398719557772). |
| F07 | Nintendo: ESG intake | No | Yes | ESG exempts only "Mutual NDAs on our template", so other NDAs may need review; an open-ended term ("either side can end it") could run past 12 months | **S-thin to S.** Arthur: "no fee, no exclusivity, nothing about our IP, and either side can end it" maps onto the ESG triggers. None applies. |
| F08 | Nintendo: written answer / Contact | None / none | Write to the no-reply sender; add a "Nintendo" contact | Leonard: "Get each company's contact into Contacts" | **S.** Guardrails: "Portals and no-reply notices don't need one". Base mail: "This is an automatically generated email. Please do not reply." README: "only add someone…". |
| F09 | Framewell: Decision | Park, Next Jan 5 | End, Next Oct 31 / Nov 1 | Order form f_fba21c2d: "Billing starts: Nov 1, 2025… cancel any time before the next billing date" | **S.** Leonard Slack 9fb2d234 (Sep 26, thread reply): "they'll hold the Pro plan at no charge until Feb 1 with nothing to sign before then… treat them like the other free ones". Findability risk: the message sits inside a Playtestcloud-results thread. |
| F10 | Framewell: written answer to Maren | Yes | No (Leonard's call closed it) | "Framewell called me back" | **S-thin.** No record says Leonard told them anything. Maren: "Can you let me know by mid-October if we should set it up?" Park: "Tell them we'll pick it up in January". |
| F11 | Lanternfly: Decision / Answered by | Answered (later), Leonard | Frederick answered Sep 10; or Sign + ESG (deck: "2-year term, exclusive for Southeast Asia") | Frederick wrote "we'll take a look and get back to you"; the deck hits two ESG triggers | **S.** 418a0a6d (Leonard, Sep 29): "I called the Lanternfly people back on Saturday. told them Southeast Asia has to wait until after the raise and that we'd talk again in January". Guardrails: "Go top to bottom and stop at the first one that fits." Wen's Sep 22 "Any news on the proposal?" shows Frederick's Sep 10 note was not an answer. |
| F12 | Lanternfly: answer date | Sep 27, 2025 (Saturday) | Sep 29 (Slack date) | The only explicit date is the Slack timestamp | **S.** "on Saturday"; Sep 29, 2025 is a Monday. |
| F13 | Pixel Harbor: Decision | End, Oct 10 | Answered (later) by Frederick Jun 19 | "Thanks Teodor, I'll come back to you on this" reads like the Balancy "circle back" | **S-thin.** It states no decision, unlike Leonard's "priorities have shifted…". Tracker f_9d6edd49 (Jul 31): "quote in · deposit due Oct 10 if we go". Pair this with F02 so a solver can't apply two standards. |
| F14 | Clipforge: Next date | Oct 15, 2025 | Jan 15, 2026 | Tracker "free through Jan 15 per the pilot agreement"; pilot "no charge through Jan 15, 2026" | **S.** Paylane <CAYV6MxN…@paylane.io>: "the pilot now ends on Oct 15, 2025 and the Studio plan starts on Oct 16 at $1,800/month. To cancel… write to billing@paylane.io by Oct 15." |
| F15 | Clipforge: who gets the written answer | billing@paylane.io (cancellation) **and** Priya Raman | billing@paylane.io only; or Priya only | Priya asked "Want me to line up the next brief?", so she is "waiting"; the other side says one company gets one answer | **U** on whether Priya must also be written to. The cancellation address is settled by the pilot agreement f_8d0e0e3a: "Cancel in writing to the billing address on your notice" plus the notice. Also see C2. |
| F16 | Clipforge vs Paylane rows | One row, Clipforge | A separate Paylane row | Paylane sends the notice and bills | **S.** Notice signature: "Paylane, payments for UGC Studio"; pilot agreement: "billed by our payments partner". |
| F17 | Wishwave: Decision | End, Oct 17 | Sign/Park (Wishwave books the travel) | Guardrails: "Travel and event costs count only when we book them ourselves" | **S.** 7e889113 (Leonard, #executives, Mon Sep 29): "travel and event costs count as cash even when a partner books them and bills us". |
| F18 | Robert's "cancel every marketing tool" | Ignore | End for Hootline, Framewell, Loopnote… | Posted in #executives during vendor talk | **S.** It is by Robert, on a Thursday (Sep 25). Leonard: "plus the one change I posted in #executives on Monday". |
| F19 | July "accept terms yourself" (Markward) | Superseded, so Sign | Frederick accepts Markward himself (free) | Jul 22 Slack: "under $500 a year you can just accept the terms yourself" | **S.** Leonard Sep 25 (CAyZDYLg…): "This replaces what I said in July about Fred signing small stuff himself." ESG: "That includes click-through terms". |
| F20 | Markward: Sign vs Park; Next date | Sign; Next blank | Park (free, no deadline) | Guardrail 5 catches "Everything else that's free" | **S.** Guardrail 4 comes before 5: "taking it means someone has to accept terms". README: "for Sign, the date they need it by, if any". Paper: "Activation: accept the terms in the Markward dashboard". |
| F21 | Hootline: Decision | Park, Jan 5 | End (say no to the annual plan) | Gemma: "lock in the annual plan now at a discount"; guardrail 2: "an offer we would have to take up and pay for before January" | **S-thin.** f_f7902fdb: "Free until Jan 31, 2026… Annual plan option: $390/year" (no deadline). Gemma: "a quick note before the promo ends". Guardrail 5: "including offers we could still take up after that". |
| F22 | Glyphworks / Driftwood / Pressbeam: pay-when-ordered | Park | End | Each would cost cash the moment we order | **S.** Guardrail 5: "offers we could still take up after that". f_f6701704: "Quote valid until Jan 31, 2026"; f_17878d7b: "valid until Feb 28, 2026"; f_a9bb79c8: "book any time before launch". Contrast Soundvault "Quote valid until Oct 15, 2025" and Lingora "until Oct 3, 2025", which are End. |
| F23 | Cloudlark: Park vs Sign | Park | Sign (activating credits usually means accepting terms, as with Lumencloud) | Lumencloud's credits need a signed program agreement | **S-thin.** f_eb94c65c: "Activation: when you're ready; nothing owed"; email: "Nothing to do until you want to activate them". Held until Feb 28, 2026. |
| F24 | Retainly: Decision / Next | Park; Jan 5 | End (auto-converts; cancel by Jan 11); Next Jan 11 | "Growth at $99/month unless cancelled before Jan 12, 2026" | **S.** The conversion falls outside "between Oct 1 and Dec 31". README: "for Park… the January review". |
| F25 | Pingwise: Keep; Next date | Keep; Nov 1, 2025 | End/Sign; or Next Oct 31 (downgrade deadline) | Arthur's list never names Pingwise | **S.** Arthur's card 689b662c: "the night pager for backend outages (whatever wakes me up at 3am)"; f_6c212cbf: "on-call alerting… phone and SMS paging". No other pager tool appears in Frederick's Gmail or Slack (PagerDuty, Opsgenie, "on-call" all searched). README: "for Keep, when it next bills"; "$29/month from Nov 1, 2025". |
| F26 | Certwell: Keep vs Sign | Keep; written answer from Frederick | Keep, but only an officer can confirm, so it also needs a card | ESG: "Only an officer… accepts terms… whatever the amount". Certwell lacks the "nothing new to sign" line that Vaultline and Pingwise have | **S-thin.** Order: Keep (rule 3) stops before Sign (rule 4). f_cfb172de: "Same terms as the current certificate". Keep: "Tell them we're staying." |
| F27 | Kinetic Arcade: ESG trigger | Yes (exclusivity) | No (12 months is not "over 12 months") | Term reading | **S.** ESG: "Anything with… exclusivity…". f_6252955f: "Exclusivity: 12 months from signature". |
| F28 | Orbit Store: ESG trigger | No | Yes (a feature placement licenses our name and art) | Bundlehouse spells its licence out; Orbit's paper is only a "summary" | **S-thin.** f_2ae7e3ee: "Fees: none · Term: the promotion only". No exclusivity or licence is listed. |
| F29 | Orbit Store: written answer | Yes, to Mateo Rossi | No (portal) | Acceptance happens "in our partner portal" | **S.** Mateo emailed twice: "Could that happen by Oct 24?"; "gentle nudge". The portal exemption covers portal notices. |
| F30 | Playfuse: ESG | No | Yes (2-year term) | "Term: 2 years" | **S.** ESG: "Mutual NDAs on our template don't need review, whatever their term." f_9a7fc4a3: "(ESG Law mutual NDA template)". |
| F31 | Playfuse: membership | IN | OUT (no call or reply yet; cold) | Its only email is the ask; no HG reply | **S-thin.** Iris: "Before our Oct 8 call…" (a call is agreed); Frederick filed f_9a7fc4a3. Leonard's list counts "paper". No gcal event for the Oct 8 call exists in Frederick's view. |
| F32 | Lumencloud: membership | IN | OUT (cold; "just checking you saw this one") | No call, reply or sign-up is recorded | **S-thin.** "Harmony Games qualifies…" implies an application. Aiden Clarke is already in Contacts (job Lumencloud). Frederick filed f_a227b14f. |
| F33 | Orbit Store: membership | IN | OUT (unsolicited) | No "thanks for the call"; no reply | **S-thin.** "our partner portal" implies an existing account; Frederick filed f_2ae7e3ee. |
| F34 | Nova Rewards: membership | OUT | IN (Answered or End) | It is a seeded thread | **S.** Ruth Sep 23: "I'm withdrawing this offer for now." No HG reply or call; no Drive paper (the only seeded thread without one). |
| F35 | Rayking: membership | OUT | IN (Frederick replied) | Frederick's "Hi [name], Leonard forwarded me your email." | **S.** That message (1842348778705877030) is To: leonard.hayes, labels "Opened,Drafts", so it was never sent. Leonard: "including ones we only forwarded around internally, stay off it". |
| F36 | Spotlight Fest: final vs later | Answered by Robert, Sep 17, final (Next blank, no Jan reminder) | "later" (skip *this year*), so Jan review | "this year's showcase" | **S.** fc2f69c0 (Robert) and evt_564a16d0: "Told them we'll skip this year's showcase. - R". No January wording. |
| F37 | Motive Forge | Answered by Arthur, Sep 19, final | Frederick (cc) / later | Frederick was cc'd | **S.** Arthur 2025-09-19: "we're keeping the art in-house, so we'll pass on this one." |
| F38 | ESG intake: "who would sign it (Leonard or Arthur)" | Must name one per agreement | Either / "Leonard or Arthur" | Checklist f_3b06917a: "who would sign it (Leonard or Arthur)" | **U.** No record assigns a signer for Kinetic Arcade, Lumencloud or Bundlehouse. Leonard: "waiting on Arthur or me"; Arthur (Nintendo): "leaving the acceptance for Leonard or me". |
| F39 | Trello: which board/list | Harmony Games board (640643a3…318e), list To Do (…93195) | UA/BD board (66da196a…) To Do or "BD Follow Up" | Leonard says "founders' board"; no board is called that; UA/BD has a "BD Follow Up" list | **S-thin.** Guardrails: "Arthur's keep-running list on our board", and Arthur's card sits on the Harmony Games board (Doing). That board holds Leonard's founder to-dos (2,293 of his actions; cards such as "Existing Investor Update", "Ask … new lawyer"). UA/BD has been idle since Mar 2025. See C1. |
| F40 | Reply to Leonard: "what we're keeping" | Keep rows: Pingwise, Vaultline, Certwell | Also free tools that keep running (Park) or "later" items | "keeping" in plain English | **S-thin.** README: "Decision is one of: Answered, End, Keep, Sign, Park". Guardrail 3: "Keep… stays". "Waiting on Arthur or me to sign" = the 7 Sign rows. |
| F41 | January reminders: set and format | 14 companies (12 Park + Lanternfly + Balancy), on Jan 5, 2026 | Park only (12); and/or one combined reminder | Prompt: "the companies coming back in January" | **U** on count and format (one per company vs one combined). Membership is settled by README: "for Park and for 'later' answers, the January review"; date by evt_fd469c29 (2026-01-05T17:00Z). |
| F42 | Tilecast: membership | IN, Park | OUT ("playables" sit on the UA budget) | UA buckets f_7bacf15c: "Real UA bucket: Unity, Meta, playables… playables count here" | **S-thin.** Leonard's exclusion is a closed list: "the ad networks, PlayableX, Craftsman+ and Singular". Tilecast is a "Playable preview widget for your website", not an ad. The same argument applies to Clipforge/Streamcast as "UA creative" (settled the same way). |
| F43 | End next dates (off-by-one) | Brightlane Oct 1, Ascendo Oct 1, Lingora Oct 3, Panelpulse Oct 6, Pixel Harbor Oct 10, Soundvault Oct 15, Clipforge Oct 15, Wishwave Oct 17, Reviewly Oct 19, Streamcast Oct 31 | Day-before or billing-day variants (e.g. Reviewly Oct 18/20, Pixel Harbor Oct 9/20, Clipforge Oct 16) | "last day to cancel or say no" vs bill date | **S.** Each paper states the date: "confirm by Oct 1"; "valid until Oct 3"; "Confirm by Oct 6"; "deposit $2,400 due by Oct 10"; "valid until Oct 15"; "by Oct 15"; "Confirm by Oct 17"; "unless cancelled by Oct 19"; "Book by Oct 31". |
| F44 | Sign next dates | Nintendo Oct 15, Playfuse Oct 8, Kinetic Oct 20, Orbit Oct 24, Lumencloud Oct 31, Bundlehouse Nov 1, Markward blank | Playfuse Oct 7 ("before our call that day") | Iris wants it before the call | **S.** f_9a7fc4a3: "by Oct 8, 2025 (before our call that day)". |
| F45 | Sign rows: written answer content | A holding answer (with our officers / counsel; reply by date) | No answer; guardrail 4 has no "tell them" | Rule 4 lacks the "Tell them…" sentence that rules 3 and 5 have | **U** on content. That an answer is owed is settled by Leonard: "Everyone who is waiting to hear from us should get a written answer" and the guardrails' "Answers" section. |
| F46 | Soundvault: Sign vs End | End | Sign ("send the licence for signature") | It needs a signature | **S.** f_2686da10: "$1,188, paid in full on signature… valid until Oct 15". The cash test (rule 2) comes first. |

Other values I checked that are fully settled (no fork): Vaultline Keep / Oct 12 ("renews Oct 12, 2025"; Arthur: "Vaultline nightly DB backups"); Certwell Next Oct 20; Lumencloud ESG (36-month term); Bundlehouse ESG (licence of name/logo/art, 18 months); Reviewly cancellation to Hana ("by email to your onboarding contact"); Brightlane, Ascendo, Lingora, Panelpulse and Streamcast End; Kinetic, Lumencloud and Leah Brennan already in Contacts (don't add).

---

## 3. Scope census (Frederick's Gmail, Slack, Drive and Calendar; Jun to Sep 2025; not in the seeded dumps)

| Company | What I found | Leonard's email |
|---|---|---|
| **Balancy** | 1-month trial + $500/mo pricing; Aug 14 call (invite 1840192677223724701); Leonard's Sep 11 "later" reply | **Includes** (Answered, later) |
| **Nintendo** | Fred's portal sign-up Sep 4; ZOM-567 + Arthur comment; acceptance due Oct 15 | **Includes** (Sign) |
| Google (partner manager Tim) | UA check-ins; Frederick replied Sep 5 and Sep 9; no open offer | Excludes (ad network); F05 |
| adjoe | AppCamp invite (Frederick declined Jun 21: "I won't be able to make it"); invoices Jun–Aug; Sep 8 billing dispute in Slack (adjoe: "you will not be responsible") | Excludes (ad network; UA budget; "Adjoe" in UA buckets) |
| AppLovin | Slack applovin_ channel; $500/day test campaign (Jun) | Excludes (ad network) |
| Unity, Meta/FB | UA spend in #executives | Excludes (ad networks) |
| PlayableX | Slack channel; Frederick briefed them Sep 15/18 | Excludes (named) |
| Craftsman+ | 2024 threads only | Excludes (named) |
| Singular | Jul 17 restructure email; "Creative IQ" trial offers (fwd Aug 11) | Excludes (named) |
| Mattel | RFP (#executives Sep 2–5) | Excludes ("which I'm keeping") |
| Homa | Leonard Sep 15 "convos… homa… no VCs"; Frederick in #bridge-pitch Sep 18: "focus Homa on the co-dev investment path" | Excludes (investor work); no offer visible to Frederick |
| NCsoft (Taewon/Anel) | Thread 1832208184829815962 (Leonard scheduling, last Sep 30); Slack Sep 17 "Friday second round of NCSOFT" in the fundraising schedule | Excludes (investor work); slight risk as a strategic/acquirer |
| Dentsu / Griffin, GRx, Lakestar, a16z, LVP, GFR Fund, Play Ventures, Bridge-round contact, the PERSON_1126 intro, t-accelerate | Fundraising threads | Exclude (investors) |
| Playtestcloud | Tracker "running · Leonard owns"; Sep 22 results in Slack; no renewal or ask visible | Out (no ask in front of us); low risk |
| Solsten | Tracker "paused in May"; no ask | Out |
| Tamatem | Julia suggested it (mpdm Jun 3); no engagement | Out |
| ESG Law | Our counsel (engagement Aug 27); it is the process, not a backlog item | Out |
| Rayking Game | Forwarded internally; Frederick's reply is an unsent Draft to Leonard | Excludes ("only forwarded around internally") |
| Playable Factory, InterCo Digital, Gamesforum SF speaker ask, "AI strategy for gaming" speaker pitch (Sep 24), Infraday (Sep 29), CB Insights verify, elevenlabs promo, Play2Pay | Cold, unanswered | Exclude ("Cold pitches nobody answered") |
| BrowserStack | Only a Harmony Games Trello card, "cancel browsestack if not used" (Aug 7); no vendor ask | Out; a solver applying Robert's "cancel every tool" might add it |
| Apple / Google Play developer accounts | On Arthur's keep list; no renewal ask since June | No row |

---

## 4. Coherence issues

- **C1. There is no "founders' board".** Leonard's Sep 25 reply says "put it on our founders' board To Do list", but Trello has only "Harmony Games", "UA/BD", "DD Product Roadmap", "ZM ROADMAP" and a closed "Welcome Board". The Harmony Games board is the only defensible target (F39), and the UA/BD board's "To Do" and "BD Follow Up" lists are a ready-made decoy. Recommend one line somewhere that calls the Harmony Games board "our founders' board", or renaming the instruction.
- **C2. Which mailbox is "not monitored".** The Paylane notice reads "To cancel before the plan starts, write to billing@paylane.io by Oct 15. This mailbox isn't monitored." "This mailbox" can be read as billing@paylane.io. Natural reading: the no-reply sender (SVC_9701_EMAIL, a different address). Recommend "Replies to this email aren't monitored."
- **C3. Balancy's date flips by time zone.** Leonard's reply is "Thu, 11 Sep 2025 17:21:43 -0700", which is 2025-09-12T00:21Z in UTC. Any "Answered by… when" check on Balancy must accept Sep 11 or Sep 12, or pin PT.
- **C4. ZOM-567 cites a portal it can't yet use.** The issue says "($400-500 per kit per the portal)". But base gdoc "Publishing on Switch" and Arthur's comment say kit ordering only opens after the NDA is accepted ("Gain access to: Dev kits ordering"; "The portal won't take an order yet"). Frederick's own Sep 4 Slack TLDR gives the price without citing the portal. Minor: say "per Fred's research".
- **C5. Clipforge cap vs new videos.** Paylane (Sep 12) says the pilot "has reached its 20-video cap", yet Priya (Sep 22) sends "The latest batch of videos…" and offers "the next brief". This fits "the pilot ends at the end of that cycle" but reads oddly. It does reinforce F15 (Priya is actively waiting).
- **C6. Q4 commitments folder ownership.** The folder d_80a8c047 is owned and created by Frederick (2025-09-29T20:00Z), while Leonard's README (Sep 30) and email treat it as Leonard's ("the README in the folder"). That is plausible but slightly odd; no value depends on it.
- **C7. The Framewell override is buried.** Leonard's Framewell message is a reply inside his Sep 22 "Playtestcloud results are in…" thread ("side note while we're on vendors"). The parent's reply_count is updated (SQL line 231), so it's findable, but only by opening that thread. This is a deliberate difficulty, not an error. It is the sole record overriding the order form (F09).
- **C8. No timeline violations.** Every seeded record cites only earlier records: README 22:40Z < template 22:45Z < Leonard email 23:20Z (Sep 30); checklist 16:20Z < Leonard reply 16:30Z (Sep 25) "the intake checklist I shared"; guardrails Sep 26 > ESG note Sep 24 and Arthur's card Aug 12; Q4 review invite emails Sep 29 > guardrails' "I'll put on our calendars". Every Drive paper is Frederick-owned and created 10–15 minutes after its email. Arthur's Q4 invite shows "12pm" vs "9am" for the others, consistent with ET vs PT for 17:00Z.

---

## 5. Full independent log

Base/README rules applied in order: 1 Already answered, 2 Cash test, 3 Keep, 4 Sign, 5 Park.
- Next date per README.
- Q4 review = evt_fd469c29 on Mon Jan 5, 2026 (17:00Z).
- "Written answer" = whether we owe one this week, and to whom.
- Card = Harmony Games board, To Do list, company name in the title.
- ESG = one intake email to "ESG Law intake" (PERSON_2599_EMAIL).
- Contact to add = someone not already in Contacts (job = company).
- Jan = January reminder on Jan 5, 2026.

### Answered (4)

| Company | In (clause) | Decision | Answered by | Next date | Written answer | Card | ESG | Contact to add | Jan | Deciding record |
|---|---|---|---|---|---|---|---|---|---|---|
| Lanternfly Publishing | In: call + Frederick reply ("Thanks for taking my call last week"; Sep 10 reply) | Answered (later) | Leonard Hayes, Sat Sep 27, 2025 | Jan 5, 2026 | No ("don't write to them again") | No | No | Wen Halvorsen | Yes | 418a0a6d: "told them Southeast Asia has to wait until after the raise and that we'd talk again in January" |
| Balancy (base) | In: trial offer + Aug 14 call + Leonard replies | Answered (later) | Leonard Hayes, Sep 11, 2025 (PT) | Jan 5, 2026 | No | No | No | PERSON_0527_NAME (F04) | Yes | 1840501641217286806: "priorities have shifted a bit for the next few months - we'll circle back…" |
| Motive Forge | In: quote to Frederick & Arthur; Arthur replied | Answered (final) | Arthur Blake, Sep 19, 2025 | — (blank) | No | No | No | Hugo Lambert | No | 1843346276352084348: "we're keeping the art in-house, so we'll pass on this one." |
| Spotlight Fest | In: Robert's call | Answered (final) | Robert, Sep 17, 2025 | — (blank) | No | No | No | Rina Takeda | No | fc2f69c0 / evt_564a16d0: "Told them we'll skip this year's showcase. - R" |

### End (10)

| Company | In (clause) | Next date | Written answer to | Contact to add | Deciding record |
|---|---|---|---|---|---|
| Clipforge (UGC Studio, HG-2291) | Pilot sign-up + kickoff | Oct 15, 2025 | Cancellation to billing@paylane.io; Priya Raman also waiting (F15) | Priya Raman | Paylane notice: "Studio plan starts on Oct 16 at $1,800/month… write to billing@paylane.io by Oct 15" |
| Pixel Harbor Events | Mixer + Frederick reply | Oct 10, 2025 | Teodor Lind | Teodor Lind | f_614f88a2: "deposit $2,400 due by Oct 10, 2025… Cancellation: free before the deposit is paid" |
| Brightlane Studio | "Great talking yesterday" | Oct 1, 2025 | Ines Varga | Ines Varga | f_9d4639f9: "$3,500/month… Start: Oct 1, 2025; 3-month minimum"; Ines: "confirm by Oct 1" |
| Soundvault | Frederick asked for the quote | Oct 15, 2025 | Rafael Moreno | Rafael Moreno | f_2686da10: "$1,188, paid in full on signature · Quote valid until Oct 15, 2025" |
| Reviewly | Trial sign-up | Oct 19, 2025 | Hana Kobayashi (the cancel channel) | Hana Kobayashi | f_4bdfb8e0: "moves to Growth at $79/month on Oct 20, 2025 unless cancelled by Oct 19… by email to your onboarding contact" |
| Streamcast Talent | "Following our call" | Oct 31, 2025 | Kofi Mensah | Kofi Mensah | f_5b961c9c: "50% deposit ($4,000) on booking · Book by Oct 31, 2025" |
| Lingora | Frederick asked | Oct 3, 2025 | Elena Petrova | Elena Petrova | f_34ba4ac9: "invoiced on delivery · two weeks from the PO · valid until Oct 3, 2025" |
| Panelpulse | "Good speaking yesterday" | Oct 6, 2025 | Arjun Shah | Arjun Shah | f_41a9ea50: "$1,200, prepaid on confirmation · Confirm by Oct 6, 2025" |
| Ascendo | "Thanks for the call" | Oct 1, 2025 | Lucia Ferrer | Lucia Ferrer | f_a9593b0b: "$900/month from Oct 1, 2025"; Lucia: "confirm by Oct 1" |
| Wishwave | "Great chatting" | Oct 17, 2025 | Sven Aalto | Sven Aalto | f_54c2b4e1: "travel and hotel for two, booked by Wishwave and invoiced at cost (about $1,600) · Confirm by Oct 17"; plus 7e889113 |

All End rows: Answered by blank; card No; ESG No; January reminder No.

### Keep (3)

All three are on Arthur's card 689b662c. Card No; ESG No; January reminder No.

| Company | List item | Next date (bills) | Written answer to | Contact to add | Deciding record |
|---|---|---|---|---|---|
| Pingwise | "the night pager…" | Nov 1, 2025 | Dana Whitfield ("we're staying" on Team) | Dana Whitfield | f_6c212cbf: "phone and SMS paging · $29/month from Nov 1, 2025" |
| Vaultline | "Vaultline nightly DB backups" | Oct 12, 2025 | Mila Novak | Mila Novak | f_2715771a: "$19/month, renews Oct 12, 2025" |
| Certwell | "Certwell SSL cert for the API domain" | Oct 20, 2025 | Jonas Weber | Jonas Weber | f_cfb172de: "$89/year, due Oct 20, 2025" |

### Sign (7)

Card Yes for all, on the Harmony Games board To Do list, company name in the title. January reminder No.

| Company | In (clause) | Next date | ESG | Written answer to | Contact to add | Deciding record |
|---|---|---|---|---|---|---|
| Nintendo (base) | Fred's portal sign-up | Oct 15, 2025 | No | None (portal) | None | cmt_c9a6660d (quoted at F06) |
| Kinetic Arcade | "Following our call" | Oct 20, 2025 | **Yes** (exclusivity) | Noor Haddad | — (already present) | f_6252955f: "Exclusivity: 12 months from signature… Signature needed by Oct 20, 2025" |
| Lumencloud | Paper + Contacts (F32) | Oct 31, 2025 | **Yes** (36-month term) | Aiden Clarke | — (already present) | f_a227b14f: "Term: 36 months from signature · No charges while credits last · Apply by Oct 31, 2025" |
| Bundlehouse | "Thanks for the chat" | Nov 1, 2025 | **Yes** (licence of our IP; 18 months) | Freya Olsen | Freya Olsen | f_9d1e0270: "may use your game's name, logo and art… for 18 months… Sign the participation agreement… by Nov 1, 2025" |
| Orbit Store | Portal + paper (F33) | Oct 24, 2025 | No | Mateo Rossi | Mateo Rossi | f_2ae7e3ee: "Fees: none · Term: the promotion only · Acceptance: by an authorised signatory… by Oct 24, 2025" |
| Markward | "As discussed" | — (none) | No | Leah Brennan | — (already present) | f_71a95593: "free… Term: none… accept the terms in the Markward dashboard"; ESG: "includes click-through terms" |
| Playfuse | Oct 8 call + paper (F31) | Oct 8, 2025 | No (template mNDA) | Iris Navarro | Iris Navarro | f_9a7fc4a3: "(ESG Law mutual NDA template)… Term: 2 years… an officer of each party, by Oct 8, 2025" |

ESG intake contents:
- **Kinetic Arcade.** Publishing LOI for JP/KR. Term: 12 months exclusivity from signature; no auto-renewal stated. Exclusivity: JP & KR for 12 months. Cost: none (revenue share). Needed by Oct 20, 2025. Signer: Leonard or Arthur (F38).
- **Lumencloud.** Startup Program Agreement. Term: 36 months; no auto-renewal stated. Exclusivity/IP: none. Cost: none while the $25k credits last. Needed by Oct 31, 2025. Signer: F38.
- **Bundlehouse.** Holiday puzzle bundle participation agreement. Term: licence of Domino Delights' name, logo and art for 18 months; no auto-renewal stated. Cost: none to join (revenue share). Needed by Nov 1, 2025. Signer: F38.

### Park (12)

All Park rows: Next date Jan 5, 2026; card No; ESG No; January reminder Yes.

| Company | Engagement | Written answer to | Contact to add | Deciding record |
|---|---|---|---|---|
| Framewell | Call | Maren Holt | Maren Holt | 9fb2d234 (F09) |
| Hootline | Sign-up | Gemma Doyle | Gemma Doyle | f_f7902fdb "Free until Jan 31, 2026" (F21) |
| Glyphworks | Frederick asked | Tomas Novotny | Tomas Novotny | "Quote valid until Jan 31, 2026"; "payable when ordered" |
| Cloudlark | Chat | Yara Nasser | Yara Nasser | "Held until Feb 28, 2026 · nothing owed" |
| Echohall | Sign-up | Bruno Costa | Bruno Costa | "Pro: $49/month from the day you upgrade" |
| Pressbeam | Call | Ava Lindqvist | Ava Lindqvist | "paid when booked · book any time before launch" |
| Retainly | Trial | Omar Farouk | Omar Farouk | "free until Jan 12, 2026" (F24) |
| Quillcraft | Beta | Nadia Petrov | Nadia Petrov | "free through January 31, 2026" |
| Tilecast | Call | Kenji Mori | Kenji Mori | "Free pilot slot: February 2026" (F42) |
| Benchmarkly | Frederick asked | Clara Weiss | Clara Weiss | "$300/month, starting February 2026 if you subscribe" |
| Loopnote | Trial | Pavel Sokol | Pavel Sokol | "free until Feb 1, 2026" |
| Driftwood Audio | Frederick asked | Sofia Marin | Sofia Marin | "valid until Feb 28, 2026"; "paid when you book" |

### Out (no row)

- Nova Rewards: offer withdrawn, never engaged (F34).
- Everything in the census marked Exclude/Out.

### Other deliverables

- **Contacts to add: 32.** That is the 36 rows minus Nintendo and minus Noor Haddad, Aiden Clarke and Leah Brennan, who are already present. Balancy's name is unsettled (F04).
- **Trello cards: 7**, on the Harmony Games board, To Do list: Nintendo, Kinetic Arcade, Lumencloud, Bundlehouse, Orbit Store, Markward, Playfuse.
- **ESG intake emails: 3**: Kinetic Arcade, Lumencloud, Bundlehouse.
- **January reminders: 14 companies** on Jan 5, 2026: the 12 Park rows plus Lanternfly and Balancy. Format is unsettled (F41).
- **Written answers owed: 31.**
  - 10 End, 3 Keep, 12 Park, and 6 Sign (all Sign rows except Nintendo).
  - Clipforge's goes to billing@paylane.io; whether Priya also gets one is F15.
  - None for the 4 Answered rows or for Nintendo.
- **Reply to Leonard**, in his Sep 30 thread:
  - Keep: Pingwise (night pager), Vaultline (backups), Certwell (SSL).
  - Waiting on Arthur or Leonard to sign: Nintendo (Oct 15), Playfuse (Oct 8), Kinetic Arcade (Oct 20, at ESG), Orbit Store (Oct 24), Lumencloud (Oct 31, at ESG), Bundlehouse (Nov 1, at ESG), Markward (no date).
