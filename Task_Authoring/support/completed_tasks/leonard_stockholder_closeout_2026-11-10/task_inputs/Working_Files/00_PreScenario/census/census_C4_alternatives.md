# Census C4: alternative Finance authoring jobs for Leonard Hayes (Feb 14, 2026)

Status: COMPLETE. Facts and locators only, no task text. Clock 2026-02-14 00:00 UTC. Persona `leonard_hayes`.

## 0. Scope, locators, what was not read

Locator key
- `L:<id>` = Gmail `threads/leonard@harmonygames.co_<id>.json` (Leonard's mailbox, so Leonard can read it).
- `G:<n>` = low-numbered Robert-mailbox thread, cited only as a lead from census A/B.
- Slack: WD = #winddown C0ADGSZKR3R, EX = #executives C07C2866011, AD = #admin_foundersonly C04UEQVDVB7, BP = #bridge-pitch C096HFA5Z8W, PR = #prototype C09UHHN6PFZ. `idx` = position in that month file.
- SF = snowflake.json `/tables/n`: 0 AD_SPEND_DAILY, 4 IAP_TRANSACTIONS, 11 DIM_PLAYER, 12 REVENUE_DAILY, 15 MONTHLY_BURN, 16 CASH_BALANCE, 35 AD_REVENUE, 38 FINANCE_LEDGER. There are 40 tables (0 to 39); asking for `/tables/40` triggers a full 2.6 GB scan.

Reach run with `persona_view can-see`
- YES: BP, EX, AD, WD. Sheets f_48247af79428823c3cac92, f_28ecc492b19f3696a19a97, f_605121f4a36752645e0ac3, f_31115ddb6ed866f2b10d60. Decks f_868157b0665dcb6c16153a, f_7793bb93e59e9c0dee5129, f_0421912301531f11c54686, f_d03044b385b94f24b21ff4, f_65ada5e24989d256cabdfa. Docs f_17e6175e84e745f92b3415, f_0c37bb7235683d73569903, f_af99b76ff4da59a710edba, f_63c1d2616497b46c667bef.
- NO ("visible to no persona"): f_efaec72066ee44e5888bd7 Bridge Round, f_846ac36bcfd5d2fb5be232 P&L Jun, f_a5e9fc9c8a3188faf66784 P&L Jul, f_dd0ba4f44cacbb5941d82e P&L Sep 30.

NOT read
- Every PDF, xlsx and Slack image, including the Long Form PDF, the Sunset SOW, and the image in WD idx25. Canvas "REACHOUT LIST - LATEST AND GREATEST" (F09D26U61GB, files.json /23266, 3,196 bytes) has no content in the export.
- DMs and mpdms, including C7442B7CD94B. #investors. The 11 publisher decks. Publisher Slack channels (publishing-ext, udo, telegram-dd, dd-road). The Internal Jul 16 deck beyond its reach check.
- HEADCOUNT, PAYROLL_ROSTER, MONTHLY_BURN rows. Meta, Google and AppLovin receipt counts are Atlas figures, not recounted.
- census_C and census_D in task_inputsS2 (barred by the brief).

Corrections to the leads given
1. Bridge Round sheet: the Atlas lists it as Leonard-readable. It is NOT, and its content is the 2023 seed tracker (Total committed 280,000) plus 2021 hiring tabs. It is not a bridge record.
2. Three of the five P&L versions are unreadable by Leonard. Only Oct 2025 and Jan 2026 are in reach.
3. DocSend cannot be joined to firms (Section 4).
4. NB-20 has a third value: Jan 14 deck slide 11 as stored in Drive reads "$140K Marketing Budget" ($210K + $150K + $140K = $500K). EX 2026-01 idx623, 628, 633 drafts say $170K. EX idx615-616 ("let me call it $210") shows the founder line moved. The card says the attached deck says $170K; that attachment is unread. Still do not grade it.
5. Atlas "1AM" rejection: 6 substring hits in EX, all before Sep 2025, none read. Treat as unverified.

---

## 1. Candidate 1: sell-side IP or asset-sale memo

**Real need.** FACT, and the best-grounded need of the five.
- Task List f_31115ddb6ed866f2b10d60 (modified Feb 10): "Get list of assets (IP, Hardware)" False, "[PERSON_NAME_2000], ask about IP rights" False.
- Investor letter draft WD idx7 ts1770664700.848759: "We will also evaluate what to do with the remaining IP and codebase (archive, sale, or other disposition) and will keep you informed."
- EX 2026-02 idx411 ts1770850800.723979: "we wil put our IP to auction and if no one buys it we can buy via our LLC".
- Gemini notes f_0c37bb7235683d73569903 (Leonard-owned): "the legal team runs a short asset offer to investors, and if no bids are received, the assets can be assigned to a co-founder to ensure a clean paper trail and maintain fiduciary responsibility."

So the "auction" is a short offer to existing investors run by Sunset legal, not a banker sale. A teaser to outside buyers is not the base job. The base job is a schedule of what is on offer.

**Cohort, real count: about 25, not 30.**
| Class | Count | Locator |
|---|---|---|
| GitHub repos | 16, all archived:false | github `/repositories` |
| US trademark applications | 2 | L:1783431962497000185 (No. 98283298, classes 9, 42), L:1783432448141550015 (No. 98283293, classes 9, 41), filed 2023-11-23 |
| Domain | 1 found, Squarespace, renews Mar 7 2026 | L:1856970093879434499, L:1856998630106852519 |
| Store listings | about 5 (DD, ZM3D iOS and Android; CF iOS; CF Android blocked by NB-9) | INFERENCE from Slack and warehouse; not censused |
| Hardware | unknown | No register. Ledger has no equipment category. Leonard mailbox "MacBook" 4 false hits, "Mac mini" and "Mac Studio" 0. Slack only: EX 2026-02 idx366 "buy my own laptop for a few thousand dollars" |
| Encumbering contracts | about 4 | Sunset data licence, CrazyGames, BoomBit, Toon Boom co-existence |

The only route past 30 is a contributor chain-of-title list (37 gdocs titled Consulting Agreement, with duplicates and templates; 22 people on the roster per the HEADCOUNT comment). That is legal work, not Finance.

**Per-record surfaces.** Repos come from one read. Trademarks, the domain and contracts are each a thread. No bulk alternative for those, but there are few of them.

**Money: mostly not provable.** A buyer wants per-title revenue, UA, CPI, retention and funnel.
| Title | Lifetime revenue (SF 12) | UA recorded (SF 0) | Paid installs | Blocks |
|---|---|---|---|---|
| Domino Delights | $12,331.25 | $83,359.74 | 11,328 | NB-17 (Jan-Feb 2026 paid and Brazil), NB-18 (Sep 2025), NB-19 (979 Unity installs at $0) |
| Zombie Match 3D | $11.99 | $2,187.41 | 3,657, of which 3,481 Unity at $0 | NB-19 makes real CPI unknowable |
| Combo Fighter | $11.75 | $4,510.33 | 615 | NB-7 (level funnel), NB-9 (Android), NB-26 (any sale) |

Totals tie: UA $90,057.48 equals ledger marketing_ua. Lifetime revenue is $12,354.99. NB-21 blocks any version join and NB-33 blocks the December DAU story. Only DD gives a gradable story, and the honest headline is that $3.0M produced about $12K of revenue. No asset has a stated value; "$25K" and "$22,500" are data figures, not IP.

**Base-native traps.**
- Applicant name: "Harmony Games Inc." on one application, "Harmony Game Inc." on the other (L:1783432448141550015).
- Mark limits: AD 2025-08 idx40 ts1755063509.040609, Toon Boom co-existence, HG agrees "not to use 'Harmony Games' standing alone". Beats the plain filing mail.
- Data licence: L:1856675475513544349 "Section 1.5 re: IP ownership" and "7.9 ... this license would still survive upon a transfer of the assets". Beats WD idx163 "we can own the entire IP" as a clean-title claim.
- Exclusivity: "exclusive launch period" (Atlas: dd-road 1762361357.317589, not re-read) against the signed non-exclusive licence (Atlas); EX 2025-11 idx559 ts1763421018.863089 (pasted analysis, not the contract) discusses a right of first refusal on sequels that applies only where a game is exclusive.
- Spam lookalike: L:1856312668581747657 "3 million for tiles delight" is a sales pitch.

**Originality.** Medium risk. robert_llc_takeover built the take-over plan for Combo Fighter, the same outcome of the same process (README has no IP or auction text). The stay-away creditor schedules are the mirror image.

**Fit.** Good for a founder, weak for Finance: the numbers are trivial and the substance is legal.

**Honest calls (estimate).** 60 to 70. **Verdict: reject as a whole task.** Worth keeping as one section of a larger memo.

---

## 2. Candidate 2: final board or investor financial review

**Real need.** Weak. FACT: no record asks for it. The director seat is gone: WD idx195 "I accepted his resignation from the board", L:1856958794180374704. INFERENCE: the board is then Leonard and Robert (census B), so a board review has no outside reader. Investors are the only audience, and WD idx7 only promises updates on liabilities and remaining assets.

**Cohort: about 48 checkable claims** (my reading count, plus or minus 5): Apr 16 about 12, Jul 16 about 11, Oct 14 about 12, Jan 14 about 13. About 38 survive the NB cards.

Examples and outcomes (CASH_BALANCE, SF 16):
| Claim | Source | Outcome |
|---|---|---|
| ~$670K, ~$365K, ~$157K in bank | decks Apr s3, Jul s3, Oct s3 | Equal Mar 31 669,997, Jun 30 365,165, Sep 30 157,538: quarter-end, already stale on board day |
| Burn after freeze ~$57K | Apr s25 | Jul 79,058, Aug 70,399, Sep 58,170 |
| Year-end cash ~$100K | Apr s25 | Missed under either Dec figure; the exact figure is NB-3 |
| Apple Arcade $3-4M at ~25%; 4X $1.5-2M at ~40% | Apr s20, s21 | Stalled, did not materialise (Jul s21) |
| ZM beta late May, then "next month" | Apr s15, Jul s3 | "this week" at Oct 14 (Oct s3) |
| Bridge $1.5-2M in Q3 | Jul s21 | $2.5M asked Sep 3 (L:1842219327413774622), nothing closed |
| New burn ~$25K | Oct s3 | Nov 46,736; Dec 27,934 (Dec derives from an NB-3 month) |
| CPI ~$3.90 on ~500 installs | Jan s7 | SF 0 cumulative: Jan 8 $4.87 on 266; Jan 22 $6.42 on 362. Jan monthly $7.02 |
| Female character cuts CPI 20-30% | Jan s3 | Feb $12.75 (Atlas), worse |

**Per-record surfaces: thin, and this is the fatal point.** All claims come from 4 decks plus 2 speaker-note docs. Money outcomes come from about 5 table reads. No per-claim write is natural: a sheet row is one batch call.

**Money.**
- NB-2 blocks Jan-sheet AWS, hosting, Unity, UA and salary lines.
- NB-3 blocks Dec 31 and Jan 31 cash, so the two most important forecast checks cannot be exact.
- NB-20 blocks the $500K marketing slice.
- Jun, Jul and Sep P&L are out of reach, so "what each forecast promised" is 2 of 5 versions.

**Traps (real, but few).**
- Sep 30 cash: both reachable P&Ls say 194,133; deck and CASH_BALANCE say about 157.5K. Not NB-blocked. Oct: 139,654 (Oct sheet) or 137,855 (Jan sheet) against 99,701. Nov: 98,181 or 85,868 against 52,965.
- Oct deck contradicts itself: "Runway ~2.5 months" (s3), "~5 Months of runway" (s18), "extends runway to March" (s3). Oct sheet goes negative in April (Mar 8,996, Apr -16,428).
- Jan sheet Feb -18,949 against Oct sheet Feb +28,170.

**Originality.** High. No completed task does this. **Fit.** Very good: board, forecast, founder voice.

**Honest calls (estimate).** 50 to 60. **Verdict: reject as a whole task, keep as a section.** It reads best and scales worst.

---

## 3. Candidate 3: 2025 UA payback by channel

**Real need.** None found. No Feb 2026 record asks for it. The Jul deck already gave the answer: s10 "we may recover only an estimated of ~30% of ad spend over 12 months".

**Cohort.** 2025 only: 9 title-channel lines, 37 title-channel-month cells, 24 non-zero, $62,621.73. One read of SF 0 returns it all, so the 2,590 rows are not a per-record surface. Under 30 at any honest grain.

**Money.**
- IAP joins exactly: all 977 IAP rows match DIM_PLAYER. 2025 IAP by channel: adjoe $2,310.27 on $46,201.54 (5.0%), AppLovin $114.77 on $6,086.03 (1.9%), Meta $50.87 on $7,330.72 for DD (0.7%), organic $2,078.79.
- Ad revenue cannot join: SF 35 has network and placement, no player or channel. 2025 DD ad revenue is $7,197.84, more than IAP, and the only per-player route is the 1:16 sample. Full payback by channel is therefore not computable.
- NB-19 removes all Unity dollars (ZM3D's main channel). NB-18 removes the adjoe Sep credit, so the one live dispute cannot be graded. NB-17 removes DD Jan-Feb. NB-28 removes the ZM3D Meta end date.

**Traps.** "$50K Adjoe, ~10K installs" against $46,202 and 8,730 (Atlas); Jul deck ROAS 15-17% against IAP-only 5%. Meta receipts against ledger would be real, but see below.

**Originality.** Low to medium. frederick_card_spend_q3 used card and receipt records for Standard Metrics. **Fit.** Marketing analytics, not founder Finance.

**Honest calls (estimate).** 20 to 40 unless receipts are forced. **Verdict: reject.**

---

## 4. Candidate 4: the fundraising record, widened to every funding path

**Real need.** Real in substance, not written as an ask.
- WD idx7: "We also explored partnerships and other paths to scale distribution and improve outcomes, but none changed the trajectory enough."
- WD idx5 ts1770664094.831769: "We don't believe we are VC-investable in our current form".
- WD idx25 ts1770674426.735229: "we are personally liable as bod members and we have to do it correctly".
- WD idx197 ts1770934638.035469: "Reaching out to our angels properly" still open.
- Gemini notes: board and stockholder consents are coming; Leonard wants to avoid "a bad record for future companies".

INFERENCE: directors approving dissolution would want an alternatives-considered record. No base record says so. Searches of Leonard's mail from about Jan 21 to Feb 13 (thread ids 1855 to 1857) for "alternatives" (1 unrelated hit), "explored" (0), "asset offer" (0), "fiduciary" (0) are all empty. The ask must be seeded.

**Is it different enough from the Oct 2025 send list?**
- VC-only, no. frederick_bridge_pipeline holds 25 firms at Sep 30. About 23 recur here; Anton Bernstein is a likely exception, and Brightwater has 0 hits in EX, BP, AD. It is the same spine with the same evidence, and the completed-tasks README bars reusing a cohort.
- Widened to every funding path, yes, with care. Its outcomes all fall after Sep 30, so none exists in that task's universe, and roughly half the cohort (publishers, co-dev, strategic) was never on that list. Publisher canvass is Atlas rank 4 and no completed task uses it.
- The VC rows must stay a minority and must not be the graded core.

**Cohort, real count by reading: about 60 named, 35 to 40 engaged, about 20 with a dollar figure.** Token collisions may merge a few, so treat 50 to 60 as the range.

Sources of the count
- Investor List f_48247af79428823c3cac92 (/sheets_spreadsheets/108): 80 numbered rows, 77 distinct, only 24 carry any status, 5 say Rejected. Last modified 2025-09-15, so nothing later.
- BP ts1756941551.539229 and ts1757345124.546449: about 40 names.
- EX 2025-10 idx1463 ts1760952786.839299: 17 publisher-side names. idx2204 ts1761701557.000479 and idx2454 ts1761861758.158519: status lists.
- Leonard calendar: 198 live events Jul 2025 to Feb 14, 115 distinct titles, about 38 external-party meetings by title. Attendee lists show internal addresses only, so title reading is the only route.
- Leonard mailbox: 98 threads since Aug 2025 where he wrote and a PERSON_ token appears, about 45 to 50 of them fundraising or publishing by subject.

**Dollar paths on record**
| Path | Figure | Locator |
|---|---|---|
| Apple Arcade | $3-4M, ~25% | Apr deck s20 |
| 4X crypto | $1.5-2M, ~40% | Apr deck s21 |
| Bridge | $1.5-2M, then $2.5M | Jul s21; L:1842219327413774622 |
| a16z Speedrun | "up to $1M" | BP ts1758162614.001869 (firm link is INFERENCE) |
| Revo | $250K, 51% tech team in Turkey | AD 2025-10 idx27 ts1760560371.047209; tab "Revo of HG Salary & Benefits" in f_28ecc492b19f3696a19a97 |
| Rollic | $25K | EX idx2204, idx2454 (token pairing), EX 2025-11 idx836 |
| Supercent | PPP terms, team of six at stated rates | L:1847274510773446727 |
| YouTube | "$20K-$100K sign-up", web $5K-$25K/month | EX 2025-11 idx836 |
| Mattel | "$50M+ title" | EX idx2454 |
| Combo Clash | about $25K | EX 2025-11 idx836 |
| Griffin pay-to-play | $500K | Jan deck s11 |
| Recap | up to $250K, $2.25M pre | f_11040fe5d66821bd6951aa (Atlas, census B) |

**Per-record surfaces.** This is the only candidate with them. The closing record sits in per-firm Gmail threads, often with a masked subject, some in Turkish, and no sheet holds them after Sep 15. Read this session:
- Closed with a reason: 212 L:1845179658048412162 (Oct 14, Turkish); General Catalyst L:1845324849163852511 (Oct 8); Revo L:1845592798281477351 (Nov 18, Turkish, subject masked); [USERNAME_21452] L:1847431502574984008 (Nov 25, DD pass); [PERSON_NAME_0854] contact L:1848571293398223317 (Nov 18); Initial Capital L:1853682990477206418 (Jan 15); Speedrun L:1844744869261506242.
- Silent endings: T-Accelerate L:1842282783388831849 (Leonard's unanswered Oct 4 chaser); Dentsu L:1843440066457827450 (Leonard's Oct 4); GFR L:1843544442107619617 (Oct 3 "I will let you know"); Metis L:1848151902253331437 (ends Dec 2, deck sent); Kwalee L:1847447348399982364 (ends Jan 12, scheduling); Scopely L:1844840821922174730 (Leonard's Oct 4).

Bulk alternative: EX and BP month reads give statuses through Nov, but not the closers. EX 2025-11 idx836 ts1763584485.506759 gives a good summary, which is a shortcut to watch.

DocSend: 37 view notices, Sep 7 to Nov 7 2025. Every visitor is masked: Windows 14, Mac 8, iOS 4, one token 8, internal 3. Visit detail sits behind a web link. No join to a firm is honest, so use counts only. A Sep 3 tracker "sent" also has no Gmail copy for most firms (about 5 outreach threads): those rows rest on the Slack post alone.

**Money.** Provable from Leonard's reach, and almost no NB card touches it. Rule out: NB-20 (marketing slice of the $500K), NB-3 (any Jan cash figure in a Griffin ask), NB-17 and NB-6 (BoomBit Brazil result and last reply), NB-12 (a firm known only by token), NB-29 (decision date as a window edge), NB-31 (DM lists).

**Base-native traps** (wrong source, then what beats it)
1. Oct deck s6 "In progress: 7 (Makers Fund, Revo...)" is beaten by Revo's Nov 18 pass, L:1845592798281477351.
2. Revo's reason: AD idx27 (51% tech team in Turkey) looks decisive; the actual reason is CPI and category, EX 2025-11 idx608 ts1763493570.617729.
3. Play Ventures row: Latest Status "Reached out - no response as of 09/11" is beaten by Status Rejected and BP ts1757955553.793529.
4. a16z row "Waiting to hear back" is beaten by L:1844744869261506242.
5. General Catalyst row "email bounced" is beaten by the Oct 7-8 re-intro and pass, L:1845324849163852511.
6. NCsoft row "First pitch went well" is beaten by Oct deck s6 (chose a more established live-ops engine).
7. Scopely: BP Sep 8 "not investing", then Oct deck "some interest". Needs L:1844840821922174730; no close found.
8. Rollic: Oct status "third meeting ... deal size $25K" is beaten by EX 2025-11 idx836 "fell apart" (reorg, nothing before end of Q1).
9. Bridge Round sheet "Total 280000 committed" is a 2023 lookalike, and unreadable. Also Internal and Copy Game Investor Lists (/sheets_spreadsheets/18, 200, 211).
10. Oct deck totals (30+, 10, 7, 7) can be tested against the threads.
11. Token pairing: idx2204 [ORG_NAME_0355] = Mattel in idx2454; [PERSON_NAME_0449] = CrazyGames by position (INFERENCE).
12. Cold-mail lookalikes: L:1856312668581747657, "Interested in HG" L:1855778154621935748, "Capital Raise Inquiry" L:1856470805696920716 (subjects read only).

**Fit.** Strongest of the five. Leonard ran every conversation himself. Fundraising is named in the Finance scope. Output reads as a founder's account to his board and investors, not a register of bookkeeping.

**Honest calls (estimate, not measured).** 130 to 170: about 15 bulk reads, 45 per-firm searches, 30 to 40 thread reads, 10 calendar, then one sheet, one memo, and a per-firm close-the-loop draft for each still-open party (about 25 to 30). Leonard's real habit supports those drafts: he answers each pass (L:1845324849163852511, L:1847431502574984008). A strong solver batching Slack could land nearer 100.

**Risks.**
- Open set: "everyone we approached" is exactly what failed cold reviewers before. It needs a closed rule (for example a two-way exchange or meeting about money between two dates) and a census. About 15 rows will be token-only and must stay out.
- Thin arithmetic: this is mostly judgement and status. The Finance weight must come from dollar paths and the scenario tabs.
- Need must be seeded.
- Silent endings need a stated rule, or graders will argue over them.

**Verdict: keep, widened.** VC-only "what the market told us": reject.

---

## 5. Candidate 5: founder exposure

**Real need.** Small but real: WD idx25; WD idx40 "I don't want anyone to come after our families"; WD idx151 hope of no cash out of pocket.

**Cohort: 3 founders, about 10 to 12 items.** Far below 30.
| Item | Fact | Locator |
|---|---|---|
| Stock | $200 each | census B, G:00001412 (lead) |
| Notes | 21,000 + 2,500 + 12,000 = 35,500 in; repaid 2023-09-13 | FIN-000004, 10, 16, 61; AD 2025-08 idx24, 26, 33 |
| Salary freeze | Leonard $0 from April, others June and July | Apr deck s25 |
| Meta on Leonard's card | "FB didn't accept SVB credit card so I sacrificed my own" | PR ts1766643244.446779 |
| Helpshift $300, Unity on his cards | leads | AD 1770765910.100299, AD 1754605999.487199 (census A, not re-read) |
| Arthur's card | GitHub, Metabase and one other moved to KubLLC | WD idx204 ts1770937232.664809 |
| Robert | Soundly option | WD idx63 |
| Guarantees | Singular and Unity unsecured, "no liens or personal guarantees" | Gemini notes |
| D&O | Commercial and D&O expired 11/10/2025; Leonard declined renewal Nov 17 | L:1848436124467937694 |

Liability split: nothing found in WD, EX, AD across 21 terms; "split" itself was not a search term. EX 2026-01 idx615 "reimbursements" concerns a pay budget, not a claim. Amounts on Leonard's card overlap receipts booked as company cash (FIN-000689, 700; NB-4 for Feb).

**Traps.** AD 2025-08 idx24-33 (QBO still shows the repaid loan) is the only real one. D&O lapse against WD idx25 is a good finding, but it is one fact.

**Originality.** High. **Fit.** Personal, not company Finance; awkward as a deliverable.

**Honest calls (estimate).** 20 to 30. **Verdict: reject.** Fold the D&O lapse into another job as a trap.

---

## 6. Other candidates found

| Job | Finding | Verdict |
|---|---|---|
| Lifetime use-of-proceeds statement | Ledger: financing 3,035,500, repayment -35,500, salaries -1,932,761.23, "Unreconciled operating expenses" -672,374.58 over 29 rows. One table read; MONTHLY_BURN is bulk. Overlaps investor close-out; NB-3, NB-4, NB-10 near | Reject; the $672K line is a useful fact |
| Option-holder exercise notices | 14 named holders (census B), Carta mail in Leonard's box | Belongs to investor close-out |
| Income schedule ("Get list of income") | About 10 lines (census A I1-I7) | Belongs to wind-down budget |
| Data-sale delivery schedule | $22,500; Arthur owns it (WD idx200) | Not Finance, not Leonard |
| 1099 and final tax package | Bookkeeping-shaped, overlaps the sibling bank-notice task | Reject |

---

## 7. Ranked table

| Rank | Job | Base need | True cohort | Per-record reads, no bulk route | Money provable | Traps | Originality | Fit | Honest calls | Call |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Every funding path (C4 widened), alternatives-considered memo plus register | Implied; ask must be seeded | 50-60 named, 35-40 engaged, ~20 with dollars | Yes, per-firm threads | Yes, few NB | 12, deep | Medium: ~23 firms shared | Best | 130-170 | Keep |
| 2 | Asset offer schedule (C1) | Strongest, in the base | ~25 | Few | No for 2 of 3 titles | 5, good | Medium | Good, legal-leaning | 60-70 | Section only |
| 3 | Promise against outcome (C2) | Weak, no board left | ~48 claims, ~38 usable | No | Partly: NB-2, 3, 20; 3 of 5 P&Ls unreadable | 3-4 | High | Very good | 50-60 | Section only |
| 4 | Founder exposure (C5) | Small | 10-12 items | No | Partly | 1-2 | High | Awkward | 20-30 | Reject |
| 5 | UA payback (C3) | None | 9 lines, 24 cells | No | No: ad revenue unjoinable, NB-19 | 2 | Low-medium | Weak | 20-40 | Reject |

## 8. Verdict

Yes, one job beats both on cohort and on provability, but only in its widened form, and it is not a clean win.

The funding-paths record has a 35 to 40 party engaged cohort, per-firm closers with no sheet or table behind them, and money facts almost untouched by NB cards. Census B put investor close-out at 28 to 31 holders with 12 to 17 provable from Robert's view (Leonard's reach is wider, so that figure is a floor), and census A left most large wind-down lines open at the clock. It has an honest route past 130 calls; on these numbers neither C1, C2, C3 nor C5 does.

Its three real weaknesses:
1. No base record asks for it, so the ask is seeded.
2. About 23 firms overlap frederick_bridge_pipeline, so publishers and co-dev must lead and the VC rows stay a minority.
3. It is an open set until a closed rule and census exist, and it is light on arithmetic.

Best shape: one founder memo built on the funding-paths register, with the asset offer (C1) and the promise-against-outcome check (C2) as sections. Both add Finance weight and traps without having to carry the horizon. If the requester will not accept the originality risk, stay with investor close-out: nothing else here clears 130 calls honestly.
