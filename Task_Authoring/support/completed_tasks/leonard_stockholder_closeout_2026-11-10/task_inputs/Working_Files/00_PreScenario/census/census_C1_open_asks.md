# Census C1: open finance/investor asks on Leonard at the clock

Status: COMPLETE. Facts and locators only; no task text. Clock 2026-02-14 00:00 UTC, Universe_Normal, persona leonard_hayes.
Question: at the clock, what finance or investor document does somebody actually expect from Leonard, and what would make it natural for him to hand that work off?

## 0. Short answer

- FACT: nobody outside the company is waiting on a finance document from Leonard with a date on it. Griffin, Fondo, ESG and Sherwood have all stopped asking or been answered. Sunset is waiting on an onboarding intake (no date).
- FACT: the strongest live expectation is one Leonard created himself: the investor wind-down notice. It is drafted, unsent, and it promises two follow-ups (a detailed plan and timeline; updates on final liabilities and remaining assets). Angels have not been told by any record.
- FACT: the numbers behind that notice do not exist as a document. Leonard put a "cash and liabilities snapshot, plus reserves" on Griffin's agenda and offered Sherwood a "cash position, liabilities list". The Task List rows for liabilities, income and assets are all unticked.
- INFERENCE: the natural hand-off is to an assistant, not a person. Robert has disengaged, Arthur is on the data export, the terminated contractors must delete company data by Feb 15, and Leonard already drafts this kind of document with ChatGPT.

## Locator key

- `L:<id>` = Gmail `threads/leonard@harmonygames.co_<id>.json` (Leonard's mailbox). `#n` = position in `messages`, which runs newest-first in most threads.
- Slack: WD #winddown C0ADGSZKR3R; EX #executives C07C2866011; AD #admin_foundersonly C04UEQVDVB7; PR #prototype C09UHHN6PFZ; CI #company-internal C05KNDCHAAG; LB #leapblock C05URGU759U; DM-Seg D04UC0UEN2V (Segerstrale, PERSON_3335); DM-AB D04UGG61DUM (Arthur); DM-RB D04UP2L3E3S (Robert); DM-Tor D09R59580EM; DM-BF D076PSEBC4D (Brian); MP-4 C51ECE5102ED (Julia, Claire, Brian). Followed by ts.
- TL = Task List sheet f_31115ddb6ed866f2b10d60 (gsheets /sheets_spreadsheets/76). GN = Gemini notes doc f_0c37bb7235683d73569903 (gdocs /docs_documents/26).
- People: PERSON_4337 / [PERSON_NAME_1999] = Griffin senior partner and director. PERSON_2717 = Griffin investor. PERSON_2847 = Griffin VP Finance. PERSON_0767 = Sunset CEO. PERSON_2888 (Jackie Alfenas in GN) = Sunset Head of Partnerships. PERSON_2694 = ESG partner. SVC_5635 = Fondo.

## Coverage log

Read in full, every message:
- WD Feb 2026, 206 of 206. EX Feb 2026, 457 of 457. AD Jan 20 of 20 and Feb 7 of 7.
- DM-Seg 29, DM-AB 146, DM-RB 220 (Feb). **D08RQSCFKJ9 has no Feb 2026 file**; its only export month is 2025-05.
- MP-4, LB, DM-BF, D05Q3QAH2QZ (Martin), D05SDEQEK61 (Owen) for Feb. CI from Feb 9. PR from Feb 11 (idx 516-726).

Mailbox, Feb 1-13: all 335 threads classified by subject and sender (count matches reach_leonard.txt).
- 43 read in body: every thread on Sunset, Sherwood, Griffin, Fondo, SVB, Deel, ESG, Clio, Singular, Helpshift, CrazyGames, Standard Metrics.
- 24 more screened on their first message: cold outreach, no finance ask. One exception: L:1855403930517654215, a second counsel contact Arthur brought in.
- Of the 8 Carta mails I read 1. Of the 6 termination letters I read 2.
- All 39 messages Leonard sent in Feb 1-13 within these threads were listed by recipient. None goes to an angel. No thread carries a DRAFT label.

Also read:
- Jan 2026 mailbox: all 656 subjects indexed, 275 non-noise subjects scanned, 17 read in body.
- EX Jan by keyword filter only (116 lines), plus the full Griffin call transcript EX 1769450453.756929.
- TL, GN, Leonard's calendar Jan-Mar, Trello board (449 cards; the 7 open cards named below), all 31 Confluence page titles with term hits, 8 pages read in context, BoD Jan 14 2026 slides.
- Earlier mail by subject: about 67 threads matching BoD, board or "Materials for" (the "board" query hit its 100-match limit, so this is not exhaustive), the "Audit Request" threads, and 127 threads with Griffin, Tor, Segerstrale, Deepak or Matthew addresses.

Reach:
- `persona_view can-see leonard_hayes` = YES for WD, EX, AD, PR, DM-Seg, DM-AB, DM-RB, DM-Tor, TL, GN, P&L sheet, Reset term sheet, Reset framework, BoD Jan deck.
- Gmail `can-see` = YES on spot checks (L:1856675475513544349, L:1854160003253530566: "thread is in the persona's own mailbox"). The tool needs the id form `leonard.hayes@harmonygames.co/<id>`; the filename form returns UNVERIFIED. All other `L:` threads follow the same mailbox rule and were not run one by one.
- Snowflake was not queried for this census.

NOT read, marked UNREAD wherever they matter:
- Every PDF and attachment: the signed Sunset SOW, both Sunset proposals, the data licence, BoD PDFs, the Jan 23 memo PDF, bill 3973.
- Every Slack image, including WD 1770670533.759769, WD 1770674426.735229 (Segerstrale's liability advice) and WD 1770934041.066969 (Griffin, then "I guess they have to do it this way"). Also EX 1770848472.726979 and AD 1770770480.877399.
- The Shut_Down_List canvas (no content in export). The Sunset, Fondo, QBO, Carta and Standard Metrics apps. Standard Metrics mails have empty bodies.
- Other channels in Feb, including BoomBit C09SWTHEMEW and #zombie-*. #investors and #bridge-pitch.

Hard limit: Slack ends Feb 13 10:03 UTC (NB-6) and the last Leonard mail is Feb 13 11:35 UTC. A call, text or Sunset-platform action leaves no record, so "not done" below always means "no record of it".

## A. Open asks and promises at the clock

"Owes" = does Leonard personally owe it. "Satisfied" = does anything in the record already meet it.

### A1. Investors and board

| # | Who asked / was promised | Document or number | By when | Locator | Owes | Satisfied? |
|---|---|---|---|---|---|---|
| 1 | All investors; self-set | Wind-down announcement email, drafted with "Financial context" section | After 1:1 outreach; no date | WD 1770664700.848759, 1770664924.520089; TL "Send email to investors" False | Yes | **No.** Draft only. Not in the 39 sent messages |
| 2 | Each angel; self-set | "personally reach out to every angel investor ... before I send out 'winding down' email" | Before #1 | DM-Seg 1770665186.368229; WD 1770934638.035469 "Reaching out to our angels properly" (Feb 12 22:17Z, listed as still to do) | Yes | **No**, except Segerstrale (DM-Seg 1770664988.379119) and Griffin. No Feb mail or DM to Tor, Matthew, Deepak |
| 3 | Investors, via draft | "a more detailed wind-down plan and timeline shortly, including key dates for operational shutdown" | "shortly" | WD 1770664700.848759 | Yes, if #1 goes out as drafted | No. Source would be Sunset's Plan of Dissolution, not yet produced |
| 4 | Investors, via draft | "periodic updates ... once we have clarity on final liabilities and any remaining assets" | No date | same | Yes, if #1 goes out | No |
| 5 | Griffin, Leonard's own agenda | "Cash and liabilities snapshot, plus what reserves we should hold for taxes, payroll, and chargebacks" | Call held Feb 11 by phone | L:1856675475513544349 #13 (Feb 9); EX 1770838886.766449 | Self-set; Griffin never asked in writing | No document. TL "Get list of liabilities", "income", "assets" all False |
| 6 | Sherwood, Leonard's offer | "I can share our current cash position, liabilities list, and key contracts in advance" | Before Feb 12 call | L:1856688113228112603 #8 | Lapsed: Sherwood not engaged (DM-Seg 1770919996.740719) | No record it was sent. Need survives as Sunset input |
| 7 | Griffin, after resigning | "They will share the necessary paperwork as it becomes available over the next 30-45 days" | About Mar 14-29 (derived from Feb 12) | L:1856958794180374704 #0 | Sunset produces; Leonard relays | Not yet |
| 8 | Investors, Leonard's stated aim | "I want [1999] and other investors to feel good and get their docs for tax write-offs etc." | None | EX 1770848514.434209; GN "ensure investors secure their tax write-offs" | Sunset issues (GN); holder inputs presumably from Leonard (INFERENCE) | Not yet |
| 9 | Griffin, Jan 26 call | Pro forma cap table at 2.5 cap: "send like a pro forma cap table"; Leonard: "put them like a pro forma together" | Jan | EX 1769450453.756929 | Superseded by Feb 9 decision | Not found sent. Moot |
| 10 | Griffin, Standard Metrics Q4 | Quarterly metrics and documents | Reminder Feb 3 | L:1855429523880965666; L:1856116678494354384; L:1856787396431935562; AD 1770770470.281349 | Was owed | **Yes**, submitted Feb 10-11. Contents UNREAD |
| 11 | Tor (PERSON_5275), Nov 4 2025 | "Do you send out any investor updates? ... I don't think I am on the mail list" | TOR end-of-year sync | DM-Tor 1762283800.142359, 1762285888.654689 | Answered then | Answered with Oct deck and Weekly Update. Tor has not heard of the shutdown by any record |
| 12 | Griffin, TL row | "[Griffin], ask about IP rights" | None | TL | Leonard | Unticked; answer given orally (EX 1770839126.382429, 1770839149.629569) |

### A2. Sunset

| # | Ask | By when | Locator | Owes | Satisfied? |
|---|---|---|---|---|---|
| 13 | Onboarding intake, "~30-60 minutes"; "initial documents and information" | None stated | L:1856675475513544349 #1; L:1856959810650143006; WD 1770934638.035469, 1770935695.500189 | Yes | No record. Platform UNREAD |
| 14 | Kickoff call with legal and customer success manager | After intake | same #1 | Yes | No calendar event after Feb 12 |
| 15 | Data delivery; pays out $22,500 after | "Once we've received the data, we'll initiate the payment" | same #1; WD 1770935695.500189 | Arthur | Not delivered. CTO instructions not in the mailbox at clock |
| 16 | SOW fee: "it's time to make your payment" | Due on signing | L:1856956473569789052 | Yes | Unknown; NB-4 bars grading paid state |
| 17 | Board and stockholder consents; asset offer to investors | After Plan of Dissolution | GN | Signers | Not started. Griffin no longer a director |

### A3. Fondo, tax, bank

| # | Ask | By when | Locator | Owes | Satisfied? |
|---|---|---|---|---|---|
| 18 | DE franchise tax: gross assets | Fondo's Feb 1, then Feb 6; filing deadline Mar 1 | L:1855588237464451707; L:1856041213967112448; L:1856403583413868285; L:1856861681308161749 | Was owed | **Answered** Feb 11: 52,686.59 "as of 12/31/2025" (NB-3). Fondo: "Great, thank you Leonard!" |
| 19 | DE tax amount: Fondo emails amount, inputs and filing date first | Before Mar 1 | L:1854402939785612241 | Fondo owes Leonard | Not received at clock |
| 20 | Fondo "action items" in app | "as soon as possible" | L:1856581006621649557; L:1856762188001356499 | Leonard; items UNREAD | Unknown. Automated, may be the same DE form |
| 21 | Corrected books: "we will be seeking professional assistance to correct the records"; Fondo offers bookkeeping pricing | None | L:1856861681308161749 #1, #0 | Self-set promise | No reply on record |
| 22 | Final return provider: Fondo or Sunset | "around March 15th" per GN | GN; EX 1770852109.891589, 1770852126.205579; WD 1770933903.645709 | Leonard decides | Unknown; which proposal was signed is in UNREAD PDFs |
| 23 | Fondo auto-renew stop: "I'll contact [ORG_NAME_0304]" | Nov 26 | WD 1770933903.645709 | Yes | No, not urgent |
| 24 | SVB card close and payoff | "next 24 hours" from Feb 12 21:30Z | L:1845454913903205585 #1, #2; L:1856956277591180405; WD 1770931801.955279, 1770927223.969899 | Payoff yes; SVB owes next step | SVB reply not in record. Balance not stated anywhere |
| 25 | Gusto address for IRS checks | None | EX 1770765363.959899, 1770770890.452559 | Arthur | No confirmation; value near nil after Fondo's Feb 10-11 answer |

### A4. Vendors, staff, partners (not finance documents; listed for completeness)

| # | Ask | Locator | Status |
|---|---|---|---|
| 26 | Singular written cancellation | L:1853470742168514419 #0 | Sent Feb 12 21:43Z. No reply |
| 27 | Unity note from Arthur, Leonard on CC | WD 1770932147.282819, 1770932572.935779 | No copy in Leonard's mailbox |
| 28 | Helpshift: move DD and ZM off "before Feb 28th" | WD 1770789534.434749; L:1856273045304945702 | Open. NB-5, NB-8 |
| 29 | Deel pro rata $4,500 and $5,100, also sent to Leonard | L:1856858277487884047 | No disposition |
| 30 | Leapblock ~$600 gesture | WD 1770922731.444009; **Arthur: "yeah lets do that"** WD 1770936725.388049 | Agreed by two founders, cash-dependent. Corrects Census A row O10 "undecided" |
| 31 | Claire: closing meeting and equity question | MP-4 1770903714.600249 | Equity not answered in chat; the letter's Equity paragraph covers it (L:1856858053929740799) |
| 32 | ironSource ~$800 owed to company | DM-RB 1770766636.224479, 1770766696.145039 | Handed to Robert Feb 10; no outcome |
| 33 | CrazyGames: "a more concrete update ... by next week" | L:1847443396264475348 #1 (Feb 10) | Open. Leonard told them results "look promising" the day after deciding to shut down |
| 34 | BoomBit not told | PR 1770842604.594879; WD 1770842057.356439 ("[USERNAME_48456]", by context BoomBit, INFERENCE) | Deliberate |

### A5. Latent, not an ask at the clock

Griffin's KPMG audit confirmation comes yearly and goes to Leonard:
- FY2023 arrived Jan 23 2024 (L:1788910618703813283). FY2024 arrived Dec 4 2024 (L:1817557789846606177).
- Subject search "Audit Request" over all `threads/*.json`: 11 matches, scan complete, nothing for FY2025.
- A request would be on pattern, but it would have to be seeded. It is not a base need.

## B. What each party still needs from Leonard

### Sunset (engaged; SOW signed Feb 12)

Words, all L:1856675475513544349 unless noted:
- #1 Feb 12 22:22Z, CEO: "You should have just received an invite to the Sunset platform. After logging in, the onboarding intake usually takes ~30-60 minutes. Once submitted, the legal team will review all the docs, prepare your Plan of Dissolution, and you'll set up a kickoff call with legal + your dedicated customer success manager."
- #1 on data: "He'll provide data export instructions based on the apps you have. Once we've received the data, we'll initiate the payment and start the cleaning/scrubbing process."
- L:1856959810650143006 Feb 12: "To get started, we'll need you to provide some initial documents and information."
- #6 Feb 12: offer of $22,500, all cash; "a 20% discount if you work with us on both the wind-down and data purchase together".
- L:1856872398290956689 Feb 11: "Sunset cannot support negotiating the release of claims." The V1 template offers "a partial settlement of {AMOUNT}", with "Payment will be made by credit card only; wire or ACH is not available."

What the engagement requires of the company, from readable bodies only (the signed SOW is UNREAD):
- Intake, then Plan of Dissolution, then kickoff (mail).
- From GN (Leonard reach only; AI-generated notes that misname the entity):
  - "The board ... will receive board and stockholder consents to formally approve the wind down."
  - "the legal team runs a short asset offer to investors, and if no bids are received, the assets can be assigned to a co-founder".
  - "If capital is available for redistribution ... [Sunset] will manage the wires; if not, they will provide investor notices and necessary tax write-off documentation."
  - One-time fee, "with the only exclusion being taxes owed by the business".
  - On creditor releases, "Delaware typically recommends two or three attempts to prove the company has tried to obtain the release."
  - "about four to six weeks" overall.
- INFERENCE: Sunset sends the formal investor notices, so Leonard's own email is a founder courtesy on top of them. That matches his plan to go 1:1 first (WD 1770664924.520089).

### Griffin

Nothing in writing is outstanding.
- Last words: Feb 12 22:05Z, "I would formally like to leave the Board of [HG]." L:1856958794180374704 #1, PERSON_2847 on copy.
- Earlier oral advice, Feb 11: "work with Sunset or sherwood ... Don't do it yourlsef" (EX 1770839105.706739).
- FACT: no written reply to the Feb 9 agenda exists. Griffin's image at WD 1770934041.066969 is UNREAD.
- INFERENCE: Griffin's stockholder consent is still needed if the charter tracks the term sheet (Census B: about 90% of preferred).

### Fondo

- Jan 15: "Before filing, we'll email you: The tax amount due, The inputs used in the calculation, The date we plan to file"; files "after 5 business days" unless tax exceeds $5,000 (L:1854402939785612241).
- Feb 11: "I would not postpone this submission because if you do not file by the filing deadline of March 1st then you will incur penalties & interest charges." (L:1856861681308161749 #4)
- Feb 11: "If you would like our support for bookkeeping we would be more than happy to help you." (#0)
- Feb 10-11 on R&D: "The credit can only be used to offset actual employer payroll taxes owed." (L:1843611181307573177 #0)
- Leonard owes Fondo nothing dated. He owes himself the books fix (#21) and the final-return choice (#22).

### Counsel

- ESG closed Feb 11: "we should consider the attorney-client relationship formally terminated" (L:1841635707568607753 #0). Bill waived: "happy to remove that bill and discount 100%" (#3).
- The Clio notice for $715, due Feb 27, predates the waiver and is dead (L:1856854433653763620).
- Arthur's second contact [PERSON_NAME_46450] received the seed docs Feb 3 (L:1855403930517654215 #0; EX 1770127278.779219). TL row "Talk to [46450] ... nominal fee" unticked; overtaken by Sunset.
- Rimon, 2023 counsel: no Feb 2026 thread in the index.
- Sunset's legal team now holds this role (GN).

## C. Precedents

Cadence, FACT:
- Ten quarterly board packs by subject "Materials for the [HG] BoD meet ...": Oct 2023, Jan, Apr, Jul, Oct 2024, Jan, Apr, Jul, Oct 2025, Jan 2026.
- Standard Metrics quarterly from Nov 2023 (Census B: 33 mails).
- **No recurring investor letter.** Leonard to Tor, Nov 4 2025: "I haven't sent any investor updates recently" (DM-Tor 1762285888.654689). Search "investor update" in his mailbox subjects: 0 hits, scan complete, with 18 "Materials for" subject hits as positive control.
- Trello "Existing Investor Update" is Done (Nov 12 2025) with no description.

| # | Locator | Date | Recipients | Structure | Use |
|---|---|---|---|---|---|
| P1 | L:1845817502803740951; L:1837676721477425972; L:1829439993308534910 | Oct 12, Jul 14, Apr 14 2025 | To Griffin partner and PERSON_2717 (Matthew until May 2025); cc Robert, Arthur, Frederick | "Attached please find the materials ... Ahead of the meeting, I wanted to provide a brief update". Then **What's Been Good** (Company Building, Product), **Challenges** (Company Building, Product & Marketing). Cash and runway stated plainly: "We have about $157K. Runway about 2.5 months". Close: "Best regards" | The house style for a financial narrative |
| P2 | L:1854160003253530566; slides f_65ada5e24989d256cabdfa | Jan 12 2026 | Griffin partner; cc Arthur, Robert | Shorter: **Game Progress**, **Company Building**. Ends in a binary ask: "$500K ... If There's no appetite ... we'd like to discuss winding down". Deck: State of the Union, Studio Update, Financials; slide 12 "~$25K in Bank — ~15 Days of Runway" | Decision-ask form |
| P3 | L:1855133803855213163 #2; memo f_f09041fe1e83ead96b3d09 (Slack link EX 1769193780.837769) | Jan 23 2026 | Griffin partner; cc founders | "Quick update since we last spoke." Metrics, one cash sentence, numbered "two realistic paths", memo attached. Drafted in EX first (1769193734.450429) | Short email plus memo pattern |
| P4 | WD 1770664700.848759 | Feb 9 2026 | Draft to all investors | Headed sections: What we did and what we learned, Financial context, What happens next, Timeline and updates; 1:1 offer. Reads AI-assisted (INFERENCE); he calls it "pretty good" | The base draft of the live deliverable |
| P5 | L:1849251423278993052 #1 | Nov 19 2025 | PERSON_2717 alone | Plain narrative by channel: VC, publishers, web, big bets, with dollar ranges | Informal investor update |
| P6 | L:1817557789846606177 #2 | Dec 17 2024 | KPMG, Griffin VP Finance on copy | Numbered 1-4 mirroring the request: investment confirmation, statements, Carta cap table, charter | How he answers a finance request |

Also: L:1830881190622782585 "Board Follow-Up", Apr 30 2025 ("Dear Board Members", "three quick updates", Runway section). Decks: "March 25 Investor Update" (EX 1742234155.910679, used at GDC), f_84a3fffd6ba30c9bcfee07 "August 25 Update", f_ccd36b8c7ef6c6f9f6a38a "Weekly Update Oct 24".

He owns the numbers: "I still need to do all P&L and shit since it's our responsibility and I can't handwave it." (EX 1768165430.803379).

## D. Who could take work; which channels stay usable

### People

| Person | Active after Feb 11? | Fit | Evidence |
|---|---|---|---|
| Arthur | Yes, through Feb 12 23:00Z | Real partner; already loaded | "I guess it's gonna be you and me mostly" DM-AB 1770665930.873519. Holds data export, Unity, cancellations, repo and Metabase moves (WD 1770935695.500189, 1770933903.645709, 1770937232.664809). Co-approves SVB payments (L:1856009252762511347) |
| Robert | Yes, on Combo Fighter | Weak for finance | "not happy about [0054]' lack of interest in the whole shut down process" DM-AB 1770665892.628179. Takes small errands (WD 1770837766.132019, DM-RB 1770766636.224479). Census A: no budget work |
| Marcus, Oliver, Owen, Martin | Yes, single-channel guests in PR | No | PR 1770842566.250369. Terminated; must delete company data |
| Julia, Claire, Brian | In MP-4 and DMs Feb 12 | No, though Brian offered: "Yardım edebileceğim bir şey olursa" | DM-BF 1770912440.990399; MP-4 |
| Frederick | No posts in EX Feb | No | Gone since Oct 2025; on EX member list |

FACT that blocks non-founders: the termination letters say "By February 15, 2026, please return all company property and permanently delete all company data" (L:1856858053929740799, L:1856860994291529096; 2 of 6 read, the other 4 are the same length). Handing one of them investor or cash data contradicts the base.

Outside help is scoped out:
- Sunset will not negotiate releases.
- Fondo offers paid bookkeeping.
- Segerstrale: "Sorry I can't do more on this" (DM-Seg 1770707438.993359).

### Why a hand-off reads naturally (all FACT unless marked)

- Pressure: "so many admin things to Chase suddenly" (EX 1770672735.574319); "I really want this torture to be over" (EX 1770836875.109429); "as quickly and cleanly as possible so that I can move on" (DM-Seg 1770672443.634259).
- Absence: "Next week I may work from Tahoe ... Fam is going for school's ski break" (EX 1770602563.693639); undecided.
- Deadline: "archieve account on google after Feb 15" (WD 1770933903.645709) and "I'll archive everyone's Google Account's by Feb 15" (CI 1770839984.194409). INFERENCE: mail and Drive sources are about to close, so Feb 14 is the last quiet weekend to pull them together.
- Habit: ChatGPT output pasted into WD 1770673284.408569 and EX 1768415499.678309. But he also doubts it: "I don't know if it's smart to rely on AI" (WD 1770674933.263759).
- Counter-signal, keep the prompt honest: "Nothing urgent is left on my plate as of now" (WD 1770934638.035469). The work is important, not urgent.
- Role mismatch: the assignment says Creative Director; every record shows CEO (letters, Sherwood mail, deck slide 13, contacts). He runs all finance. This helps Fit but the prompt should not lean on a creative title.

### Channels given NB-1

- Safest for any new record: Gmail and Drive. Slack ends Feb 13 10:03Z (NB-6).
- Founders: WD and AD. Listed members are Leonard, Robert, Arthur plus system-style ids. EX also lists E07 and E08 (Frederick), so do not call it founders-only.
- Non-founders after Feb 11 20:40Z: PR or DMs only (NB-1). Not grading who can read. Do not argue from DM member lists (NB-31).
- Slack stays paid for now: "keep all comms here for the next week or 2" (PR 1770842590.881439).

## E. Ranked: three most natural authored finance deliverables

Ranked by how real the need is in the base.

### 1. Investor wind-down letter, with a cash-and-liabilities financial context, plus angel 1:1 notes

- Need:
  - Rows 1-4. Leonard wrote the draft and the sequence himself. TL "Send email to investors" False. "Reaching out to our angels properly" is on his Feb 12 list.
  - Tor already said he is not on any list.
- Why it is executive work: it is the founder's own voice to his cap table, it carries the numbers, and Leonard said he cares about how investors end up (EX 1770848514.434209).
- Precedents: P4 is the base draft; P1 gives the numbers style.
- What moved since the draft:
  - "evaluate what to do with the remaining IP" is now the Sunset asset offer.
  - $22,500 licence, Sunset, Griffin's exit.
  - R&D credit gone.
  - "runway of less than a month" is stale.
  - The draft's promises (rows 3-4) must be honest against Sunset's 4-6 weeks.
- Risks:
  - Holder list is soft (Census B: 28-31 holders, angel dollars partly inferred).
  - Cash figures sit under NB-3 and NB-4, so a Feb cash number needs a seed.
  - Pure letter risks reading as communications rather than Finance unless the numbers carry weight.

### 2. Board-level wind-down cash, liabilities and reserves paper (sources and uses, decision memo)

- Need:
  - Row 5 ("Cash and liabilities snapshot, plus what reserves we should hold"), row 6.
  - TL "Get list of liabilities / income / assets" all False. Row 13 intake inputs.
  - Leonard's stated test is "without cash out of pocket" (WD 1770911000.728559).
  - Personal liability worry (WD 1770674426.735229, 1770675724.781109).
  - Readers are the remaining directors. Note L:1856873135836972939: "reduce the debt and return more money back to investors".
- Why it is executive work: it decides order of payment and reserves, not just lists. Real tension: the fee is due now, the data cash arrives only after delivery (Census A H3), and vendors were told "no funds" on the day the $22,500 deal was signed (H14).
- Precedents: P3 (email plus memo), P2 slide 12.
- Risks:
  - **Closest to the stay-away list** (close-out registers, Sunset creditor schedules). It must be a decision paper, not a register, or it collides and may score Bookkeeping.
  - Bank balance, paid state and two vendor outcomes are open in the base, so it needs seeds (Census A Section 4). NB-2, NB-3, NB-4, NB-8 fence the numbers.

### 3. Liquidation waterfall and holder schedule for the investor notices and write-off documents

- Need:
  - Leonard asked for it: "Guidance on reserves and any final distributions consistent with preferred stock terms" (L:1856688113228112603 #8).
  - Row 8. GN: "manage the wires; if not ... investor notices and necessary tax write-off documentation". Row 17 asset offer.
  - Competency fit is direct (cap table).
- Why third: nobody has asked for the schedule itself. Sunset may pull it from Carta. Any residual is likely small or nil. If so the schedule mainly feeds notices, and 1x preference means the answer may be "preferred takes it all" (INFERENCE from Census B term sheet reading).
- Leonard's reach beats Robert's here: he can read the Reset term sheet (Exhibit A), SPA and IRA copies, and the Carta "Termination details" mails (8 on Feb 12, at least 4 from Oct per the Atlas) with granted, vested, exercised and last-exercise dates (e.g. L:1856960351896429942: 22,889 / 12,875 / 0 / April 30, 2026). I did not re-read the Series Seed documents for this census.
- Risks: register shape; Series Seed count conflict (3,051,882 / 881 / 879); options 334,284 vs 268,772 (Census B); NB-15.

### Considered and ranked lower

- FY2025 KPMG/Griffin confirmation: strong precedent (P6), but needs seeding (A5).
- Corrected FY2025 books or final-year P&L (row 21): real, but bookkeeping-shaped.
- IP asset valuation or LLC bid: stay-away (robert_llc_takeover).
- Pro forma cap table (row 9): dead since Feb 9.

## Corrections and additions to prior census (facts to carry forward)

- **Matthew Collins resigned from the board May 1 2025**, "with immediate effect" (L:1830959847543474636). This closes the "No resignation record found" gap in Census B Section 5.
- Leapblock gesture: Arthur agreed (row 30). Census A row O10 said undecided.
- SVB's own notice confirms the card line reduced to $38,000 on Jan 28 (L:1855578032517361688), which bears on Census A H13.
- New Leonard cash statement: "we'll have 4K left in the bank I think more or less" (EX 1769802855.352309, Jan 30). A quote only; it sits next to NB-3's Jan 31 and must not be graded.
- NB-20 adjacency: Drive slide 10 of the BoD Jan 14 deck reads "$140K Marketing Budget" with $210K founders and $150K team, not the $170K NB-20 cites and not the email's ~$150K. The sent PDF is UNREAD and may differ. Do not grade.
- Sent Sherwood mail differs from its Slack draft: "no US employees other than ourselves and only 4 international contractors" (L:1856688113228112603 #8) vs "no US employees, only international contractors" (WD 1770675894.906889). NB-15 applies.
- Trello: 7 open cards, none finance-live (latest activity Nov 2025). "[PERSON_NAME_2950] transfer of shares back to the company" (652f0ef8a506e9409d66c70d, Backlog, 2024) is a loose cap-table end; no description. "Paperwork for the Board" (680ee5d709c2d601148c25ff) has no description.
- Confluence: 31 pages, no finance, investor or wind-down document. "wind-down" appears only as staff-tenure notes and a Domino Delights title trend.
- Calendar: no event after Feb 12 16:30Z. No Sunset kickoff scheduled.
