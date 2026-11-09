# run_sim: cold adversary simulation, Leonard Hayes stockholder close-out

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal). Written 2026-11-07. Design read: `01_Scenario_Design.md` §2, 4, 5, 6, 7, 9, 10, 11; `01_Gradable_Surface.json` (98 slots, weight 262); `plan/build_scenario.py`; census C5 sections D to G; `research/s4_carrier_formats.md`.

Labels used below. **M** = measured here, through `hg.py` or `persona_view.py search --no-hidden leonard_hayes` (the second is scoped to his view). **R** = reasoned from §11 about a planned seed, which is not in the base. **J** = my judgement. No prompt, H1 text or SQL exists yet, so every statement about them comes from the design's own quotes.

## 0. Verdict

- **The 72 % is right on the 98-row surface and wrong for the task.** My row model gives 72.5 % at catch rates well above the author's. About 2 of those lost points come from two row defects and 1.5 from plain rows I set below C5's rate; correct both and it is 75.9 %. The design has not priced /rubric either: on final rows it is 79 to 82 %.
- **First baseline forecast: 76 to 82 %, central 79 %, SD 0.07 to 0.10.** Under 85 % is likely. Under 70 % is near zero without changes.
- **SD is the gate at risk, not the average.** P(SD at or above 0.10) is about 0.5 on this surface and about 0.2 after 25 % more rows (0.47 if rho is 0.35).
- **Biggest single leak: H1 is a trap index.** Five sentences of the closed rule each name one trap's shape, and every run reads H1.
- **Traps that are real:** ES-18's letter join, Segerstrale under the side letter, Patrick Lewis as the third brother, and ADV to a degree. ASOF's difficulty is mostly ADV's shadow.
- **Traps that are thin:** ASK (rows pass on a plain date note), Tor (default reading is right), most of BOARD's Matthew half, and Deepak under the design's own call plan.
- **Nothing is unreachable.** ES-14's identity, the letter join and the family link all resolve from records Leonard can read (measured). Two rows are unfair as written: AL_ES-16 and the AL line rows.

## 1. First 40 calls of a strong run

Prompt assumed: names the investor draft, the Linear holder project and KPMG's request, the deliverable kinds and the Tuesday date. It names no rule.

| # | Call | Returns | Source |
|---|---|---|---|
| 1 | `slack_search_channels("winddown")` | C0ADGSZKR3R | M |
| 2 | `slack_read_channel(C0ADGSZKR3R)` page 1 | Newest 100 of 206 records, idx 205 to 106. Holds the Feb 12 list (197), "Carta terminations are done" (198), "I accepted his resignation from the board" (195), "you guys are CCed" (196) | M |
| 3 | same, cursor, page 2 | idx 105 to 6. Holds "All termination letters are sent" (81), "you guys are CCed" (82), "bod members" (25), "one by one" (8), the draft (7) | M |
| 4 | `linear_list_projects("holder")` | Hub text: "one issue per holder on Carta, live or lapsed", "my close-out notes have how each holder gets handled", "what Sunset asked for", "as I said in #winddown" | R |
| 5 | `linear_list_issues(project)` | 26 titles and states. "Enes Disli" and "Eren Disli" sit two rows apart | R |
| 6 | `linear_list_issue_statuses(ENG)` | ten states | M via s4 |
| 7 | `gdrive_search("close-out")` | Folder and both notes docs | R |
| 8 | `gdocs_get_document_text(H1)` | The whole closed rule, plus pointers to Trello, GCal, Slides, the folder and the DM | R |
| 9 | same, earlier notes | Decoy, older date: read and set aside | R |
| 10 | `gmail_search "Audit Request"` | Base has 2 threads; the seed is newest, so it is the first id | M, R |
| 11 | `gmail_get_thread(KPMG FY25)` | As-of date, items, "reflected" rule, reply to all | R |
| 12 | `gmail_get_thread(FY24)` | Numbered reply, no holder list, cap table attached | M |
| 13 | `gmail_search "Sunset after:2026/02/01"` | Base has 26 hits all time, the newest seven all Feb 12; the seed sorts first | M, R |
| 14 | `gmail_get_thread(Sunset request)` | "any side letter terms", per-holder route, directors | R |
| 15 | `gmail_get_thread(1856675475513544349)` | Sunset main thread | M |
| 16 | `gmail_search "Termination details"` | Exactly 14 threads | M |
| 17-18 | `gmail_get_messages_batch(full)` x2 | All 14 notices: ES-1 to 7 and 12 to 18, so ES-8 to 11 visibly absent | M |
| 19 | `gmail_search "(Termination of Independent Contractor OR Notice of Involuntary Termination) after:2026/02/01"` | Exactly 6 letters, all cc the founders | M |
| 20 | `gmail_get_messages_batch(full)` | 6 letters: 3 say Dec 31, 3 say Jan 31; Carta has 3 at Dec 31, 4 at Jan 30, 1 at Nov 21 | M |
| 21 | `gmail_search "PERSON_3140_EMAIL"` | 1789011705438137160: "[0068]'s email address is PERSON_3140_EMAIL" | M |
| 22 | `gmail_get_thread(1782034095239486005)` | Staff addresses and grants; "Oliver Brooks ... 15,259 ... PERSON_1174_EMAIL" | M |
| 23 | `slack_search("angel")` | February has three real hits: #winddown/197, D04UC0UEN2V/1770665186.368229, and an #executives "friends/family/angels" line | M |
| 24 | `slack_read_channel(D04UC0UEN2V, oldest Feb 9)` | 29 messages. First is "shut down the company we decided"; second is the promise | M |
| 25 | `slack_search("Segerstrale")` | **0 hits** in ASCII | M |
| 26 | `slack_search("Segerstråle")` | 5 hits; one is D04UC0UEN2V/1693245806 "Harmony Games Advisor Agreement - Segerstråle" | M |
| 27 | `slack_search("equity")` | The only February hit is Claire's question in C51ECE5102ED | M |
| 28 | `slack_read_channel(C51ECE5102ED)` | 7 messages; Julia confirms mail arrived | M |
| 29 | `gmail_search "from:robert after:2026/02/09"` | Accepted invites plus the Deepak seed | M, R |
| 30 | `gmail_get_thread(1857000911304835072)` | Robert told Deepak | R |
| 31 | `gmail_search "resign"` | 11 threads: Matthew's, Phil's and Vincent's among them | M |
| 32 | `gmail_get_thread(1849344928983425627)` | vincent.parker@ resigns, last day Nov 21, signed [0051] | M |
| 33 | `gmail_search "Disli"` | One real thread among 13 substring hits: "all three Disli brothers" | M |
| 34 | `gmail_search "Patrick Lewis"` | 5 threads, including Enes's list 1770141224265557526 | M |
| 35 | `gdocs_search "Series Seed"` | Term sheet among 22 hits | M |
| 36 | `gdocs_get_document_text(term sheet)` | 3,051,879 and 268,772 | M |
| 37 | `gdrive_search "side letter"` | Two "TLAS draft 28 August" copies | M |
| 38 | `gmail_search "side letter"` | 22 threads | M |
| 39 | `gmail_get_thread(1777052222643175480)` | "includes [0090] as a party"; "has [6550]' signature as well"; BCC PERSON_3336 | M |
| 40 | `linear_list_comments(ENG-2438)` | Start of the 26-call loop | R |

By call 40 a strong run has H1, all 14 notices, all 6 letters, the recipient key, the DM, the family thread and the resignations. Order will vary; C5 section D says everything named in the prompt or hub opens in the first 20 calls.

Hit counts in Leonard's view, all time (M; `persona_view` is substring, so live counts will be lower):

| Term | Gmail | Note |
|---|---|---|
| KPMG / Audit Request | 6 / 2 | FY23 and FY24; the seed adds one to each |
| Sunset | 26 | |
| investor | 652 | Newest real hit is the Sunset thread; noise otherwise |
| angel | 2,000+ | Mostly "Los Angeles"; useless in Gmail, sharp in Slack |
| holder / stockholder | 251 / 7 | No record lists holders; 0 subjects say stockholder (s4) |
| Carta | 182 | Newest 14 are the notices; older ones are digests with SSP and ES ids |
| option grant | 26 | Digests name ES-16, ES-18, ES-9, ES-11 and more |
| side letter | 22 | |
| advisor | 298 | With "Agreement": 17 threads, four naming holders |
| board | 1,531 | "board position" cuts it to 3 |
| equity | 312 | Newest are the notices; "Equity awards" is notice boilerplate |

## 2. Rule by rule

Catch is the chance one run reads the deciding record and applies it, shown out of 6. All catch rates are J.

| Rule | Author miss | My miss | Catch /6 | Pointed? |
|---|---|---|---|---|
| ADV | .40 | .30 | 4.2 | Partly: H1 sentence, ES gap, tie-out |
| LETTER, ES-14 | .50 | .125 | 5.3 | Yes: H1 class, earliest date |
| LETTER, ES-18 | .50 | .225 | 4.7 | Yes, but needs the recipient key |
| TOLD, Segerstrale | .45 | .30 | 4.2 | Yes: K3 quote names the DM's sentence |
| TOLD, Deepak | .45 | .22 | 4.7 | Yes: newest-first, tiny Feb 13 bin |
| TOLD, Tor | .45 | .08 | 5.5 | Default reading is right |
| ASOF logic alone | .45 | .25 | 4.5 | Yes: rule is in the KPMG body |
| ASOF totals (needs ADV) | | .475 | 3.1 | |
| FAM | .50 | .25 | 4.5 | Yes: H1 sentence, shared surname on Linear |
| FAM, Patrick Lewis | | .40 | 3.6 | Partly |
| SIDE, S3 only | .50 | .45 | 3.3 | Partly: "any side letter terms" |
| BOARD, B1 | .50 | .35 | 3.9 | Partly: 3-hit search |
| ASK, reads the question | .55 | .35 | 3.9 | Yes: H1 uses the search word |
| ASK, rows pass | | .15 | 5.1 | Rows pass without the read |
| CH-LIVE | | .05 | 5.7 | Fully: one search |

**ADV.** Reach is not one carrier; I count six routes.
- The term sheet's 3,051,879 against the owner list's 12 lines, gap exactly 103,764.
- Its 268,772 against the notices, same gap.
- `Advisor Agreement` in Gmail returns 17 threads, four naming the holders: Segerstråle, Babayigit, [0127], Deepak Gupta (M).
- `f_3ee38465decc57e61df6e5` "Advisor Agreement - [0127]" is shared with Leonard and states 6,104 (M).
- Carta digest 1782897835407336831: "option grant ES-9 ... for Husnu Matthew Collins" and "ES-11" (M).
- The Slack DM with Segerstrale has the agreement's file name (M).

0/6 would need nobody to sum the lines and nobody to look at ES-8 to 11. 6/6 would follow if H1 keeps "A grant with no Carta termination is still open", because the notices skip exactly four ids. C5 has no case of a run chasing a broken total, so this is the widest uncertainty in the model.

**LETTER.** Deciding records are the 6 letters against 8 Feb 12 entries, reached by "All termination letters are sent" plus "you guys are CCed". H1 forces a Told cell per line and names a Full note class, so every run asks who is untold. ES-14 stands out by itself: earliest date, Nov 21 effective, resigned. ES-18 is the real work: Carta has four Jan 30 entries and the letters have three Jan 31s, so one of Oliver and Owen has none, and only the key in 1782034095239486005 or 1789011705438137160 settles it. 6/6 if H1 keeps its classes as drafted. 0/6 only if H1 says nothing of an untold class, which would break closure.

**TOLD.** Segerstrale needs the DM. `every angel investor` returns exactly one Slack message (M), and H1 must contain those words because K3's delegation quote is checked against the delegating record. That message is 198 seconds after the deciding one, in the same DM. What keeps this off 6/6 is identity: PERSON_3335 is not in `users.json`, so the DM partner has no name, and the ASCII name returns 0 hits. Deepak: see LEAK-3. Tor: H1's "about the closing" settles it.

**ASOF.** The KPMG seed states the rule, so logic is not the difficulty. A1 and A2 need 243,757, which includes 103,764, so a run that misses ADV fails them at 139,993. Author's ASOF channel is therefore correlated with ADV, not independent as §6 says. The real extra traps are the Dec 31 boundary and counting Oct leavers' vested lines.

**FAM.** H1 names the family rule and Linear shows two Dislis. "Disli" and "brothers" each surface thread 1774211155651873582 (M). T13's discovery note, "the owner list shows no shared surname", stops being true the moment the issue titles say Disli. Patrick Lewis is the part that splits runs. He needs Enes's list or the wire thread body. 6/6 on F5, about 3.6/6 on F4.

**SIDE.** Reached by `side letter` because the Sunset seed quotes those words. The Drive copy is titled "draft 28 August", which invites a check. The deciding text is in thread bodies, quoted through most of both side letter threads ("as a party": 45 message hits, M), but under tokens [0090] and [6550]. Mapping them runs through BCC PERSON_3336 and "segerstråle <PERSON_3336_EMAIL>". S1 and S2 are about Tor and pass on the Drive draft alone, as s1 line 149 admits, so only S3 is a trap. Nearest thing to a true mid-rate trap.

**BOARD.** Phil is free: hub page 1. Matthew: `board position` returns 3 Gmail threads, 2 relevant, one being his (M). `resign` also finds it. Carta consent 1838216168984971198 went to Phil, Leonard and Robert only, a third proof. B2 and L6 depend on what the Sunset seed asks.

**ASK.** One search, the only February hit, and H1 uses the word. It also barely matters: see LEAK-6.

**CH-LIVE.** Leonard's list names Carta; one search returns all 14. 20 weight, always passes. P_FRED is weight 5 for a one-search lookup.

## 3. Leak findings

**LEAK-1 · LEAK · ADV, LETTER, FAM, ASK · H1 reads as a trap index.** Evidence, §2 predicate:
- "A grant with no Carta termination is still open" points at ES-8 to 11.
- "A post in a channel does not count" names Oliver's case.
- "A live option line not told gets a Full note" tells the run someone is untold.
- "One note to the person who has always handled a family" names FAM.
- "An open written question about equity" names ASK and supplies the search word.

C5 failure mode 6: a rule naming the carrier moves p from 0 to about 0.8. Fix: keep closure, cut examples. Delete the post sentence, since "addressed to that person" already closes it. Delete the grant sentence and settle "are advisor grants live" through the 268,772 tie. Move the family sentence out of H1 (see change list).

**LEAK-2 · LEAK · TOLD · A planned seed points at the deciding record's neighbour.** Evidence: K3 in `plan/build_scenario.py` makes H1 carry "every angel investor". `slack 'every angel investor'`: visible=1, D04UC0UEN2V/1770665186.368229. S_SEG is D04UC0UEN2V/1770664988.379119. T6's claim that "the DM is off every channel listing" does not survive this. Fix: drop K3 so H1 quotes no base sentence. K2's phrase is H1's own and still chains R6; fragments fall to 14 against the floor of 12.

**LEAK-3 · LEAK · TOLD · T7 is caught by the plan's own calls.** Evidence: §9 counts 26 per-address Gmail searches to reach the floor, and T7's discovery note says the mail is found by "searching his address". Search is newest first, so the seed is the top id. Leonard's mailbox has only 5 base messages dated Feb 13 (M), so a sweep sees about 8, three of them seeds. Fix: date the mail late on Feb 12, after the 22:17 UTC list, among that day's 45 base messages; make it a reply on an old thread Leonard is already on, with Deepak only as an address token. That lowers the sweep and name routes, not the address route, so §9 must stop counting on 26 address searches.

**LEAK-4 · LEAK · BOARD · One search returns both resignations.** Evidence: `gmail 'board position'`: 3 hits, 1830959847543474636 and 1856958794180374704 beside a Duolingo newsletter. Both base records; nothing to change in them. Fix: none in records. Accept 3.9/6 and do not count BOARD as a hard trap.

**LEAK-5 · LEAK · FAM · Linear titles give the surname the trap hides.** Evidence: §2 ENG-2443 "Enes Disli", ENG-2445 "Eren Disli"; the §11 contact seed adds Eren's name; T13 relies on no shared surname. Fix: title both with the owner-list forms, [PERSON_NAME_52949] and [PERSON_NAME_27652], as ENG-2451 and ENG-2461 already do. Name the Eren contact row by address only.

**LEAK-6 · LEAK · ASK · The rows pass without the trap.** Evidence: Q1 selector `(Claire)...(exercise|equity|option)` and Q2 `(Claire)...Mar 31` both match a plain Date note, and a Date note with her last day substantially answers "do we need to do anything for our equity". Q2 is simply ND_ES-4. Fix: Q2 to weight 1 as a date sample. Q1 needs a condition the plain note lacks, or accept that ASK adds no spread.

**LEAK-7 · LEAK · TOLD · Linear "last contact" comments cannot be honest and neutral.** Evidence: §11 plans "last contact" on about 52 comments, and "must not say Leonard told an angel". The true last contact for Segerstrale is Feb 12 (DM), so ENG-2440 either hands TOLD over or states a falsehood a coherence reviewer will catch. Same for ENG-2459 if it says when Vincent left. Fix: no last-contact field on ENG-2440, ENG-2449 or ENG-2459; use neutral text that is true of every issue.

**LEAK-8 · MINOR · SIDE · Hub word names the search.** Evidence: K8 quote "any side letter terms". Needed for the route column, but it pins runs to the right query. Fix: "any special terms".

**LEAK-9 · MINOR · ASOF · T22 is inert.** Evidence: FY25 is the newest hit of any KPMG search, and the prompt names it. Fix: none; do not count it.

**LEAK-10 · MINOR · sharing · K14 is a pointed amendment with no row.** Evidence: H1 quote "if the sharing changes I'll say in the DM"; D2 grades Robert only. Fix: add a weight-1 Arthur row, or drop K14.

**LEAK-11 · MINOR · selectors.** NC_Nebojsa and NC_Collins accept the word "shares", so a wrong figure passes. S1 accepts "email". Fix: require the figure; drop "email".

## 4. Over-hardness findings

**OH-1 · OVER-HARD · ASOF · AL_ES-16 will land 0/6.** Evidence: selector `(ENG-2461)...10,?384` in the KPMG reply. No run puts a Linear key in a mail to auditors, and the holder has only a token name. Fix: match `10,?384` near `ES-16` or `35,?605`, or drop the row. Weight 3.

**OH-2 · OVER-HARD · ASOF · AL rows assume a per-line listing nothing asks for.** Evidence: §11 says "share counts only". Leonard's FY24 reply is four numbered items with the cap table attached and no holder lines (M). 16 weight, 6.1 % of the surface, losing 4.1 points, of which about 2 have nothing to do with the as-of date. Fix: the FY25 seed asks for options outstanding by grant at the as-of date, or the rows move to a schedule tab. Fair fix raises the average about 2 points.

**OH-3 · OVER-HARD · TOLD, SIDE · ASCII "Segerstrale" matches nothing.** Evidence: `slack 'Segerstrale'` visible=0, `gmail 'Segerstrale'` visible=0; with å, 5 and 12. A spelling trick by accident, which Part 3 item 6 of the guide warns against. It also protects ADV, since the å search shows the Advisor Agreement. Fix: title ENG-2440 with the base spelling. Decide it on purpose; expect SEG up about .05, ADV up about .03.

**OH-4 · OVER-HARD (risk) · all note rows · 48 weight rests on a tool no baseline has run.** Evidence: 18 slots read `gmail_create_draft` output, 18.3 % of weight; s4 records 0 draft calls in stored runs and no `gmail_get_draft`. If drafts do not reach the grader, this is fake difficulty. Fix: prove it in the pre-check before any row depends on it.

**OH-5 · MINOR · BOARD · B1 selector is order-bound.** Evidence: `director...Leonard...Robert`. "Robert and Leonard" fails. Fix: either order.

**OH-6 · MINOR · board wrong source not priced.** Evidence: Feb 11 Gemini mail 1856873135836972939: "whose board consists of themselves and [2000]". It is a Leonard-readable mail; s3 only says avoid citing it. A run reading it may drop Robert. Fix: acknowledge in the two-reading table.

**Checked and fair (M):**
- **ES-14 identity.** Carta shows [0051]. Mail 1849344928983425627 is from vincent.parker@, last day Nov 21, signed [0051]; DM D05PX3R13QF has the same text. `resign` finds it.
- **Letter join.** 1782034095239486005 and 1789011705438137160 give every recipient's address; token joins token. Oliver's personal address appears there and on no Feb letter.
- **Family link.** 1770141224265557526, 1774211155651873582.
- **Segerstrale's party status.** In thread text, despite the unreadable PDF.

C_FIRST and N_COUNT land near 2/6 because each needs five traps right. That is fair, but they are not independent spread.

## 5. Re-estimate on 01_Gradable_Surface.json

Method: each run draws trap states (Gaussian copula, rho .15), each slot gets a pass probability by state, 3,000 six-run batches. Scripts: `/private/tmp/claude-501/-Users-sumit-Source-OC/46989a83-cbdb-4145-86b5-605b4a19b678/scratchpad/sw3/model.py` and `model2.py`. UNCALIBRATED.

Inputs: ADV .70, letter join .75 (L14 .875, L18 .775), SEG .70, DEEP .78, ASOF logic .75, by-line KPMG reply .50, FAM .75, Patrick given FAM .80, SIDE .55, BOARD .65, ASK read .65, Griffin split .88.

| Group | Weight | Share | Mean pass | Points lost |
|---|---|---|---|---|
| ADV rows that flip (K1, K4-7, K8, P1) | 33 | 12.6 % | .66 | 4.3 |
| ADV tag, Griffin split (K2, K3, A3) | 9 | 3.4 % | .83 | 0.6 |
| ADV tag, note holding | 6 | 2.3 % | .63 | 0.8 |
| LETTER (C, TC, N, C_DATE, D6) | 30 | 11.5 % | .78 | 2.5 |
| TOLD Segerstrale | 11 | 4.2 % | .67 | 1.4 |
| TOLD Deepak | 11 | 4.2 % | .74 | 1.1 |
| TOLD Tor rows | 9 | 3.4 % | .89 | 0.4 |
| C_FIRST, N_COUNT | 6 | 2.3 % | .37 | 1.4 |
| ASOF totals A1, A2 | 10 | 3.8 % | .51 | 1.9 |
| ASOF lines AL | 16 | 6.1 % | .32 | 4.1 |
| FAM F1-F5 | 17 | 6.5 % | .64 | 2.3 |
| SIDE S3 | 5 | 1.9 % | .53 | 0.9 |
| SIDE tag S1, S2 | 6 | 2.3 % | .80 | 0.5 |
| BOARD | 14 | 5.3 % | .59 | 2.2 |
| ASK | 8 | 3.1 % | .82 | 0.5 |
| CH-LIVE | 20 | 7.6 % | .94 | 0.5 |
| All other rows | 51 | 19.5 % | .89 | 2.1 |
| **Total** | 262 | | | **27.5** |

E[avg] = 100 - 27.5 = **72.5 %**.

The author's §6 tags 72.5 % of weight to rules and fails each at Q. About 27 of that tagged weight does not flip when the trap lands: K2, K3, A3, S1, S2, Q2, C_TOR, TC_TOR, NC_Tor. So the author reaches 72 % by overcounting flips at low catch; I reach it with higher catch plus defect rows. Same number, different cause, and only one survives the fixes.

| Scenario | E[avg] | SD | P(<70) | P(<85) | P(SD ok) |
|---|---|---|---|---|---|
| Surface as written | 72.5 | .101 | .29 | 1.00 | .51 |
| Same, rho .35 | 72.9 | .120 | .31 | .99 | .70 |
| Plain rows lifted to C5's .93 | 74.0 | .101 | .20 | .99 | .51 |
| OH-1 and OH-2 fixed too (base F) | 75.9 | .103 | .11 | .97 | .53 |
| F, +25 % rows at .93 | 79.4 | .082 | .01 | .94 | .22 |
| F, +25 % rows, rho .35 | 79.7 | .097 | .02 | .88 | .47 |
| F, +50 % rows at .93 | 81.6 | .068 | .00 | .86 | .07 |
| Everything caught more (ADV .85, join .85, others up), as written | 78.9 | .084 | .02 | .95 | .28 |

C5 section F puts row multiplication at 6.5 to 15 points and .03 to .05 of SD, so the +25 % and +50 % rows are the honest ones. **Always-pass share:** only 28.6 % of weight is at or above .85 pass on this surface, which looks healthy, but that is before multiplication.

## 6. Three changes, ranked

All measured from base F, 75.9 %. Post-fix catch rates are J, so treat differences under 0.5 as a tie.

1. **De-point TOLD: 75.9 to 73.7, about -2.2.**
   - H1 `f_a37b403d5200d4f0a31d31`: remove the K3 quote.
   - Seed 1857000911304835072: move to late Feb 12 after the 22:17 UTC list, as a reply on an old thread, address token only.
   - ENG-2440 and ENG-2449 comments: no last-contact field.
   - Assumes SEG .45, DEEP .55. This also needs §9 to stop counting 26 per-address searches.
2. **Re-aim and reweight always-pass rows: to 74.1, about -1.8, SD +.009.** No record changes.
   - S2 graded on Segerstrale's line (s1 line 108: the TLAS copy applies to notices to any Investor), so it flips with SIDE.
   - P_lapsed x5 to weight 1 and P_FRED to 3: they are lookups, per the weight bands.
   - Q2, L2, L8 to 1.
3. **Cut ADV's pointers: to 74.2, about -1.7, SD +.004.**
   - H1: remove "Stock is a certificate" and "A grant with no Carta termination is still open".
   - Keep stock or option class off ENG-2438 to ENG-2463 titles and descriptions, so the 12 lines are not pre-grouped for a sum.
   - Keep the word "advisor" out of seed 1857034369525983506.
   - Assumes ADV .58.

Runner-up: FAM, -1.5. Retitle ENG-2443 and ENG-2445 (LEAK-5) and move the family sentence out of H1 into a reply under #winddown C0ADGSZKR3R/1770664924.520089. Note that a `reply_count` update would be needed on that parent, and C5 puts thread replies at 3/6 to 4/6.

**Combined 1+2+3:** 69.8 %, SD .116 on the surface; 74.8 %, SD .091 at +25 % rows; 77.9 %, SD .075 at +50 %. With FAM too: 68.3 % on the surface, 76.9 % at +50 %.

**What this means.** De-leaking gets the surface under 70 but not the final rows. Row multiplication is worth more than any record change. The strongest lever left is writing the surface at final row shape now and making added rows depend on a trap (C5 section F, rule 4).

## 7. Call count

§9's plan of 187 over-counts by about 48. Without the 14 notes, the same low run is about 125 against the 173 floor.

| Line | §9 | Realistic low run | Why |
|---|---|---|---|
| Gmail per address | 26 | 8 | OR-lists were 62 to 69 % of item-shaped queries (C5) |
| Gmail notices and letters | 14 | 3 | `format=full` takes 10 ids: 14 notices are 2 calls, not 14. §2 itself says the batch collapses them |
| Slack per holder | 13 | 4 | one `angel` search plus 3 DM reads |
| Discovery and rules | 34 | 28 | deck and second sheet often skipped; C5: LLC's deck had 0 reads |
| Linear comments | 26 | 26 | every LLC run did this |
| Reconciliation | 8 | 6 | |
| Writes | 66 | 64 | |
| **Total** | **187** | **about 139** | |

- **Unbatchable calls:** 26 comment reads, 26 moves, 10 reason comments, 14 notes, 2 mails, 1 Slack, 6 Drive = 85. By C5's rule, 45 + 85 = 130. That is on the line, with none of the 100 it advises to clear the lowest run.
- **Where a run falls below 130:** notes in one Doc instead of 14 drafts (-13); only 10 issues moved (-16).
- **Would every run clear 130?** Median 165 to 185 (J). P(all six) about 0.4 (J). The platform's 100 is safe unless both fall-offs happen together.
- **Subagents.** They read, and their MCP calls count, so fan-out pushes runs up (Julia up to 17). Leonard's mailbox suits it, but that adds reads, not spread, and those are the calls that catch T7.
- **The contradiction.** The horizon plan and T7 want opposite things: if runs make the 26 searches, Deepak is 6/6; if they don't, the count is about 18 lower.

## 8. Measured against inferred, and limits

**Measured:**
- Every base hit count and quote above; the Feb 9 to 13 mail census (181 messages, 5 on Feb 13).
- #winddown's 206 records and page split (top-level pages are my reconstruction of limit 100).
- The Carta table and A1, A2 arithmetic: 139,993 + 103,764 = 243,757, plus 9,051,879 = 9,295,636. All tie.
- The DM census for the 13 holders Slack can identify, Nov to Feb: Oliver has no DM with Leonard in Feb, Vincent none after Nov 20.

**Inferred:** every catch rate, all pass probabilities, post-fix deltas, the median call count, and all seed behaviour.

**Could not do:**
- Run the live tools. Search ranking, Slack word matching and `persona_view` substring matching differ. `persona_view` returned "dislike" for "Disli"; live Gmail will not.
- Read H1, the hub, the Sunset seed or any Linear comment: none exist. If they differ from the design's quotes, several findings shift.
- Read PDFs or attachments.
- Test whether Opus chases a broken total. C5 has no case, and ADV's .70 rests on it. One pre-check with a read-scan would settle more than this whole file.
- Check any catch rate on Leonard. All priors are from other personas.
