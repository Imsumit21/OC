# Coherence sweep (cold /injection + Cross-Service Coherence review) — leonard_stockholder_closeout

Status: COMPLETE. Reviewer: cold subagent, no stake in the design. Clock 2026-02-14 00:00 UTC, normal universe. Reviewed: `Working_Files/01_Scenario_Design.md` (sections 1, 1a, 1b, 3, 4, 5, 11, Must-not), the draft manifest, `plan/build_scenario.py`, Evals 0 (Check A, C) and 1 (§3.2), `known_data_issues/normal.md`. `01_Universe_Inject.sql` is a 616-byte stub and `04_Prompt.txt` is empty, so this reviews planned records, not seed text.

Gmail ids are Leonard's threads and `[n]` is the message index. Slack is channel + month + idx. Severity: BLOCKER = fails coherence as planned. MAJOR = likely flagged, or a planned record can fail depending on how it is written. MINOR = low impact or a design-document defect.

## 0 Verdict

**FAIL as planned, on one blocker. It is a one-field fix.** The project description is stamped before both records it points to. Seven MAJOR findings need settling before `/create-injection`. No planned seed is contradicted outright by a base record: KPMG's request, Sunset's request and Robert's mail can all exist. Share totals held up: 268,772, 159,706, 243,757, 266,436 and 9,295,636 all recomputed. Of 33 locators and claims spot-checked, 29 are clean and 4 carry a defect (§7); one pointer, `/contacts/170`, does not exist.

| Id | Sev | One line |
|---|---|---|
| CS-01 | BLOCKER | Project description (Feb 12 23:24Z) cites notes (Feb 13 01:05Z) and Sunset's request (Feb 13 18:06Z) |
| CS-02 | MAJOR | "Share counts only" against KPMG's own FY24 chase for financial statements |
| CS-03 | MAJOR | Comments restating owner-list figures are a Quantitative fail unless attributed and dated |
| CS-04 | MAJOR | "Last contact" comments: order against Robert's mail, and stale values in s2 |
| CS-05 | MAJOR | Tuesday Feb 17 deadline and hold against "archive everyone's Google Accounts by Feb 15" |
| CS-06 | MAJOR | Robert is the least plausible sender: "lack of interest", zero mail ever sent to Deepak |
| CS-07 | MAJOR | T3 resolver is false: the Feb 12 entries move only half the gap, so the deck is stale on its own date |
| CS-08 | MAJOR | Arthur has zero Trello actions in the export; nothing happened in Trello after Nov 13, 2025 |
| CS-09 to CS-22 | MINOR | Id, wording, pointer and document defects (§1 to §8) |

## 1 KPMG FY25 request

**Does anything contradict an FY25 request reaching Leonard in Feb 2026? No.**
- Auditor: KPMG audits Griffin for FY23 and FY24 (1788910618703813283[1], 1817557789846606177[6]). Nothing changes that. "Audit Request" scan over all 88,726 thread files: 33 hits in 4 files, FY23 and FY24 only, `scan_complete` true.
- Timing: FY23 came after year-end (Jan 23, 2024, due 2/2, as of Dec 31, 2023). FY24 came before year-end (Dec 5, 2024, due 12/20, as of Sep 30, 2024). A Feb 13 request as of Dec 31, 2025 follows the FY23 shape, three weeks later in the calendar. The FY24 process implies nothing against it.
- Griffin footprint: Phil's Feb 12 resignation and Leonard's reply do not touch the audit. Slack 2026-02 has 0 hits for "kpmg" or "audit" (complete).
- People: PERSON_3088 was Audit Associate at KPMG in Dec 2024. PERSON_4416 sent FY23. PERSON_2847 is on Feb 12, 2026 mail. No record shows the KPMG people after Dec 18, 2024, either way. PERSON_3077 is correctly dropped ("[Deactivated]", 1817557789846606177[3]).

**CS-02 · MAJOR · planned:** gmail 1857029474983245439, "items in the body; share counts only".
**Contradicting:** KPMG treats the financial statements as a required item and chased them. 1817557789846606177[1], PERSON_3088, Dec 18, 2024: "Regarding item 2 of the Financial Statements, could you please provide the most recent audited/unaudited statements." FY24 has four items (1817557789846606177[2]). FY23 also needed a form: "the signed and filled Griffin_Confirmation_Harmony Games.pdf" (1788910618703813283[0]). An unexplained "share counts only" with no form departs from both years. Restoring the item would pull in NB-3 (Dec 31 cash), so the narrow ask has to stay and needs a reason.
**Smallest fix:** give the base's own reason in the body. Griffin already has the Q4 pack: 1856787396431935562, Feb 11, 2026 00:40Z, "Thank you for submitting your quarterly metrics and documents to GRIFFIN GAMING PARTNERS"; and Leonard told KPMG in FY24 that Griffin sees the books through "the Standard metrics tool" (1817557789846606177[2]). So: financials are covered by the Standard Metrics submission, articles unchanged, please confirm these share counts in your reply. Also say the form is replaced by a reply this year.

**CS-10 · MINOR · planned:** "terminations effective by then reflected". Is it plausible auditor wording? As an audit cut-off, yes; as a sentence about terminations, no. KPMG cannot know Harmony has late entries, and the word points straight at the trap.
**Smallest fix:** a generic cut-off, e.g. "as of December 31, 2025, reflecting all issuances, exercises, cancellations and terminations effective on or before that date, regardless of when they were recorded". That still decides ES-1, 4, 15 at 243,757.

PERSON_3088 as sender is a mild departure, not a defect: the sender rotated between years (4416 in FY23, 3088 in FY24, with 4416 moved to Cc). Reusing the token avoids a new identity.

## 2 Sunset Company Information request

**Should it not exist yet? It can exist.** Sender, timing and content fit, with one wording fix.
- Sender: PERSON_2888 signs "Head of Partnerships" (1856675475513544349[10], [8]). She stated the sequence herself in [8] and sent how-to material directly to Leonard (1856872398290956689[2]).
- Order, stated three times ([8], [2], [1]) plus the welcome mail: contract, invite, intake, legal reviews and prepares the Plan, kickoff. The invite landed Feb 12 22:21Z (1856959810650143006). The seed comes after it, and nothing shows intake submitted.
- Agreement: s1 section C, DSA Section 2 has the Company supply information "in the form Sunset specifies". A request fits; a ruling or a list would not. The design's "not a ruling, not a list" is right.

**CS-11 · MINOR · planned:** gmail 1857034369525983506, "a request for Company Information before intake".
**Contradicting:** intake is itself the collection step. 1856959810650143006: "To get started, we'll need you to provide some initial documents and information." A pre-intake step appears in none of the four statements of the order.
**Smallest fix:** "for the intake", not "before intake": what the intake will need on stockholders, so he can gather it. No legal review, kickoff or Plan may be implied.

The timing problem with this seed belongs to the project that cites it: see CS-01.

## 3 Robert to Deepak, Feb 13

**Impossible? No. Contradicts idx 197? No.** idx 197 ("Reaching out to our angels properly") is a to-do, and Robert's mail follows it.
- Address: PERSON_1287 is right. Deepak's own mail, the DocuSign "Advisor Agreement - Deepak Gupta.pdf" notices, and the owner list line agree. Contacts row /contacts/25 exists. No bounce among the messages on that address; last used as a BCC May 18, 2024 (1799418746420547240[2]).
- Relationship: real. "Deepak - [PERSON_NAME_0054] and mine ex boss from Machine Zone days" (1775636449493308689[20]). [0054] is Robert.
- That evening: Robert is on Slack at 04:19Z Feb 13 (#executives 2026-02 idx 454-456), 52 minutes before the planned 05:12Z.

**CS-06 · MAJOR · planned:** gmail 1857000911304835072, Robert to Deepak, Leonard copied.
**Contradicting (plausibility, not a hard conflict, so under Check C it cannot fail alone):**
- D04UGG61DUM 2026-02 idx 44, Leonard, Feb 9: "I'm not happy about [PERSON_NAME_0054]' lack of interest in the whole shut down process"; idx 45 "I guess it's gonna be you and me mostly"; idx 49 "hopefully he will come around". **This is the DM where K14 is seeded**, so a run reads it beside the seed.
- #executives 2026-02 idx 397, Feb 11: Robert asks "who's [PERSON_NAME_27770]?" about Sunset; idx 407-408, called to the Sunset meeting, "i had to step out the house for a sec, sorry".
- Evaluator-only, D07H86MV4DN 2026-02 idx 343, 431, Feb 12 05:01Z: "I am in 100%" on continuing; "the resentful undertone I have to hear from Leonard".
- Complete list of messages touching PERSON_1287's address: **Robert has never sent mail to it.** Every sender is Leonard or Arthur; Robert appears only on Cc or as an invite guest. Last personal mail to him is Oct 17, 2023 (Leonard).

**Smallest fix, keeping the design:** give the mail a reason in its first line, using the ex-boss link, e.g. Leonard will write formally but Robert wanted him to hear it from him first. Keep it free of figures and of any wish to continue.
**Better alternatives:**
- Better holder: **Nebojsa** (SSP-09). "[PERSON_NAME_0112] - [PERSON_NAME_0054] and mine ex coworker from Machine Zone days" (same message). Robert has real traffic with him: direct mail Aug 11, 2023 (1773963101399472184), invites Jan 2024, Apr 2024 and Jan 2025, Slack mpdm C7442B7CD94B to Oct 24, 2025. Swapping keeps every count (Already told 4, First note 6) and the advisor mechanics. Cost: he has two addresses, and rows ENG-2446, ENG-2449, C_DEEPAK, TC_DEEPAK and LC_Deepak move.
- Better sender: **Arthur**. He wrote to Deepak directly (Mar 28-29 and Jun 19, 2023) and is engaged in the close. Weaker personal link.

**CS-09 · MINOR · planned:** id 1857000911304835072 with date 2026-02-13T05:12:00Z.
**Contradicting:** the id does not follow the base rule the design claims ("Id schemes follow the base"). `id >> 20` gives 2026-02-13T09:14:34Z, 4h02m off. Three base threads decode within 2 s of their first message, and the KPMG and Sunset seeds within about 2 s. Also, 05:12Z renders as Thu Feb 12 21:12 -0800, while T7 and C3 say "Feb 13".
**Smallest fix:** re-time to Friday morning PT and re-mint: 2026-02-13T17:12:00Z (09:12 PT), id **1857030948126720000** (0 file matches). That makes "Feb 13" true in both zones and clears the order problem in CS-04. If 05:12Z stays, the id is 1856985649643520000 (0 file matches) and labels should say Feb 12 PT.

Companion: base keeps a copy in sender and Cc mailboxes (Leonard's Feb 12 mail exists in all three). §11 lists only Leonard's id. The row count of 8 implies Robert's SENT copy; state it.

**CS-22 · MINOR · planned:** Deepak "Already told" against K3's quote.
**Contradicting:** D04UC0UEN2V idx 1: "I'll personally reach out to every angel investor". Robert telling him is not Leonard personally, so the closed rule has to carry it.
**Smallest fix:** H1's Told line says "from any of the three of us".

## 4 Linear project and 26 issues

**Clean:** origin line is real (#winddown idx 188 "linear we keep during transition"). team_ENG fits: Leonard, Robert and Arthur belong to all five teams, Leonard created 284 ENG issues, and ENG-392 "Contact Gusto About tax reporting" is admin precedent. Numbering holds: max ENG-2437, 0 collisions on ENG-2438 to 2463 and the project id. Author ids resolve. Title forms exist in base: "Segerstrale" in gslides and gsheets, "Segerstråle" in gdocs and Slack; the other holder names and tokens also appear in records read. Listing Frederick Stone and Victor Barnes is coherent: Carta ES-17 (127,162, last day Jan 28, 2026; Robert's copy 00015796 shows `"ryan" <frederick.stone@...>`) and ES-6. They lapsed, and the description says "live or lapsed". Base gap to note, not a defect: the last issue created anywhere is ENG-2437, Nov 7, 2025, and the last update is Jan 28, 2026.

**CS-01 · BLOCKER · planned:** linear project ec2ea957-fc8e-4958-b809-0fb735b1e916, stamped 2026-02-12T23:24:00Z. Its description is the hub: K7 quotes "my close-out notes have how each holder gets handled" and K8 quotes "what Sunset asked for".
**Contradicting (seed against seed):** f_a37b403d5200d4f0a31d31 is 2026-02-13T01:05:00Z, 1h41m later. Gmail 1857034369525983506 is 2026-02-13T18:06:21Z, **18h42m later**. The description cites two records that do not exist at its own timestamp. This is the "dated before the event it cites" failure. 3.2: Temporal Field Inconsistency; Check C: incompatible chronology. The same stamp is listed for the LLC task's project (s4 section A, "Stamps: project Feb 12 23:24Z"), so it may have been carried over.
**Smallest fix:** keep `created_at`; set project `updated_at` after Sunset's mail, e.g. 2026-02-13T18:20:00Z, so the description is an edit made after both exist. `linear_list_projects` returns both stamps. Alternative with no edit: restamp folder, Sunset, notes and K15 all ahead of 23:24Z. Either way, no issue description or comment dated earlier may cite the notes' rule or Sunset's list.

**CS-03 · MAJOR · planned:** about 52 comments, "last contact, owner-list figure".
**Contradicting:** a bare figure in a founder's voice on Feb 13 is false against Carta on the same day. ENG-2462: 127,162 against 1847333272519888206 (vested 34,439, last day Jan 28, 2026). ENG-2447: 86,470 against 25,432 stock + 61,038 options. Leonard ran those terminations himself (#winddown idx 198). Check C: "An author merely calling something a decoy does not resolve an actual contradiction." 3.2: Quantitative inconsistencies always fail, with no NON-FAIL.
**Answer to the brief's question: yes, they do, if unattributed.**
**Smallest fix:** every such comment is a quoted, dated source: "Nov 2024 owner list: 127,162". No figure in the present tense. Add that as a rule in §11; it exists in §1a but does not bind the row.

**CS-04 · MAJOR · planned:** same comments, "last contact", stamped only "Feb 13".
**Contradicting:**
- Order: a Leonard comment on ENG-2449 dated after 05:12Z saying no contact since 2024 is false against the mail he is copied on.
- Values: s2 section A gives Tor's last contact as May 19, 2024; D09R59580EM 2025-11 idx 0-2 is Nov 4, 2025. s2 gives Nebojsa's as Sep 15, 2025; C7442B7CD94B 2025-10 idx 141 is Oct 24, 2025 (design §1a already corrects both, s2 does not).
**Smallest fix:** all contact comments stamped before Robert's mail (automatic with the CS-09 re-time). Take values from §1a, not s2. Give dates only where a record backs them.

**CS-16 · MINOR · planned:** the Must-not "Seed a Carta export or a full holder list", against 26 issues titled by holder. Clarify: no list with figures or states. Also note team ENG includes Frederick, Victor, Vincent, Claire, Julia, Oliver and others, and Linear is unscoped, so a project about what is owed sits in a team its subjects belong to, including Vincent, who must stay untold. The project name and issue titles should say nothing about the closing.

**CS-21 · MINOR:** "the three founders" against roster `frederick_stone`, role "Co-founder", Executive. T15 covers it, but seeded text should name the three rather than count them.

## 5 Notes docs, draft sheet, deck, hold, Trello card, contacts rows

| Record | Real job? | Dates after what it relies on? |
|---|---|---|
| Close-out notes f_a37b... | Yes: H1, the closed rule | Yes for base. See CS-12, CS-05 |
| Earlier notes f_762c... | Yes: T18 decoy | Feb 10 is before Sunset's first mention in chat (Feb 11 19:45Z, #executives idx 388) and Phil's intro (1856675475513544349[12]), so it must not name Sunset, letters or Carta entries |
| Draft sheet f_5ecaa... | Weak but real: T20 and layout | OK. Stale figures must read as copied from the Nov 2024 list (CS-03) |
| Deck f_75ddd... | Weak: T19, K12. Habit is real: "board deck outline" (#executives 2026-01 idx 587) | Before Feb 12, but after the Jan 24-28 lapses: CS-07. Must not name Sunset |
| Hold evt_6f1a... | Padding: CS-15 | CS-05 |
| Trello card | Padding: CS-08 | OK |
| Contacts rows | Padding: CS-14 | No date field |

**CS-05 · MAJOR · planned:** gcal hold on Tuesday Feb 17, "notes ready for me by Tuesday", drafts and shares in Leonard's Google account.
**Contradicting:** #company-internal 2026-02 idx 40, Leonard, Feb 11: "I'll archive everyone's Google Account's by Feb 15 - please save all your personal files / emails etc. on your local before you lose access." All six letters: "contact me directly at PERSON_5885_EMAIL or via linkedin after the email accounts are gone." The design handles this only for ES-7's route.
**Reconcilable:** #winddown idx 190, Feb 12: "to archieve account on google after Feb 15" and "We keep accounts that has our data such as Slack, google ... until the data is extracted".
**Smallest fix:** one line in H1 tying Tuesday to idx 190: the Google accounts stay up until Sunset has the data. Acknowledge it in §1a.

**CS-07 · MAJOR · planned:** T3 resolver, "Carta's Feb 12 entries move the count after the Jan 22 snapshot: 159,706 live at the clock"; T19, deck "dated before the Feb 12 entries".
**Falsified:** 268,772 − 159,706 = 109,066. Of that, **54,529** is the four October leavers' vested options lapsing Jan 24-28, 2026 (34,439 + 10,384 + 4,408 + 5,298; 1847333272519888206, 1847333318158821452, 1847333347700620793, 1847333395311994879). Only **54,537** is the Feb 12 entries (110,479 grants to 55,942 vested). CALC: Carta's count on Feb 10 was 214,243. So the deck's 268,772 is stale **on its own date**, not overturned afterward. The stale claim is still coherent, because the term sheet says "Inputs from ledger (pre-recap)" at Jan 22, but only if attributed.
**Smallest fix:** deck reads "268,772 options outstanding (Jan 22 term sheet)". Rewrite T3: "the October windows closed Jan 24-28 and the Feb 12 entries cut unvested". Do not carry the old wording into Oracle Events.

**CS-08 · MAJOR · planned:** trello 698e5a10c3f24b7e9d16a0e4, "one Arthur comment", 2026-02-13T02:40:00Z.
**Contradicting:** Arthur's member row (2162c1ba310341bf318f48b7) has **0 of 5,294 actions** and no card membership. Leonard has 4,061. The last action in the export is Nov 13, 2025, and the last card activity Nov 12, 2025. The seed would be Arthur's first Trello action ever. §11 also says "To Do card on 640643a3fd8f3ca308d9318e", which is the **board** id; the To Do list is 640643a3fd8f3ca308d93195.
**Job:** the design itself says Trello "risks being padding". "The holder sheet comes first" is already in H1.
**Smallest fix:** Leonard writes the card and any comment, correct list id, bump card and board `dateLastActivity`. Give it a fact nothing else holds, or accept it as a schema filler knowingly.

**CS-12 · MINOR · planned:** K4 "where I left things on Thursday" in notes stamped 01:05Z. **Contradicting:** that is Thu Feb 12, 17:05 PT, so the notes speak of Thursday in the past on Thursday. Persona-written times mean PT (Check C). **Fix:** "where I left things today", or stamp the notes Friday.

**CS-13 · MINOR · planned:** K14 DM, 02:21:50Z. **Contradicting:** #executives 2026-02 idx 448, 02:50Z: "Not in front of a computer right now." **Fix:** K14 states an intent ("I'll add you"), not a completed Drive change.

**CS-14 · MINOR · planned:** Contacts rows for Bergmann and Eren. **Contradicting:** design §1a: "No row for Sunset, KPMG, TLAS, Bergmann, Eren ... a Contacts seed must not imply these exist"; §11 then seeds two of them. Jobs are thin: Eren is Covered and gets no note; his address is in 1770141224265557526[1], and Bergmann's in 1773213846196143460[0] ("via email: PERSON_0693_EMAIL"). `contacts.json` has no date column, so §11's 2026-02-13 cannot be stored. **Fix:** keep Bergmann only, or both as known filler; reword §1a; drop the date.

**CS-15 · MINOR · planned:** the hold, whose stated job is "the date the notes are due". **Contradicting:** §10: "The prompt will name ... the Tuesday date." **Fix:** leave Tuesday out of the prompt, or give the hold a job.

**CS-20 · MINOR · planned:** close-out folder d_6010... **Note:** base already has "Wind Down" d_e5caf6a8c630421942ee59 (Feb 9, Task List inside, #winddown idx 22). Two correctly named folders are not a defect. One line in H1 saying why a separate folder removes the question.

## 6 Ids and tokens reused

| Token | Role, from the record that introduces it | Verdict |
|---|---|---|
| PERSON_3088 | "Audit Associate", KPMG LLP, 55 Second Street (1817557789846606177[6]) | Confirmed to Dec 18, 2024 |
| PERSON_4416 | "Audit Associate \| Alternative Investments \| KPMG LLP" (1788910618703813283[1]); Cc in FY24 | Confirmed to Dec 2024 |
| PERSON_2322 | **No role evidence.** Cc only on FY24; sends nothing, no signature | Keep as Cc; never give a title |
| PERSON_2847 | "Vice President of Finance", Griffin (1817557789846606177[3]); "Isaac" in 2023 invites | Confirmed; Cc on Feb 12, 2026 |
| PERSON_2888 | "Head of Partnerships", Sunset (1856675475513544349[10]) | Confirmed; last authored Feb 11, 2026 |
| PERSON_1287 | Deepak: "Deepak, let us know..." (1761665866565990705), DocuSign, LIST line | Confirmed |
| PERSON_0693 | Bergmann, own signature | Confirmed |
| usr_63fffeb4fab5233e, usr_Robert, usr_cc3e90160f490686 | Leonard, Robert, Arthur | Confirmed, all in team_ENG |

New ids: 0 collisions for two gdocs, five gdrive, one gcal, one trello card, the project, ENG-2438/2449/2463, all three thread numbers. Leonard's root d_63fffeb4fab5233ed5bb73 exists. Slack ts decode to the planned times; authors are channel members.

## 7 Locator spot checks

33 locators and claims. 29 clean; four defective (rows 15, 26, 32, 33, marked ✗), and row 32 includes a pointer that does not exist. The unnumbered last row is an extra claim. All through `hg.py` or `persona_view.py`.

| # | Locator | Claim | Result |
|---|---|---|---|
| 1 | `<CAPBs_a6zM...>` | owner list | ✓ 1816809274978043917[0], Nov 26, 2024 |
| 2 | gdocs f_6a372..., /262 | 61,038, 30,518, 6,104, 6,104; 103,764 | ✓ |
| 3 | gdocs f_11040..., /40 | 3,051,879; 268,772; at 2026-01-23T00:09:05Z | ✓ |
| 4 | `<CAPBs_a68Agj...>` | a Feb 11 letter | ✓ ES-15's |
| 5 | "terminating our independent" | six letters | ✓ 18 hits = 6 × 3, complete |
| 6 | `<177093551461...>` | ES-14 Nov 21, last day Feb 21 | ✓ at 22:31:54Z |
| 7 | `<177093559600...>` | effective Jan 30 | ✓ ES-13 |
| 8 | Feb 12 Carta mails | eight entries | ✓ |
| 9 | `<CAEH8bLx...>` | ES-14 resigned | ✓ last day Nov 21, 2025 |
| 10 | `<CAMy0Hx1...>` | Matthew resigned, 2025-05-01T22:42:49Z | ✓ |
| 11 | `<BYAPR02MB4358...>` | Phil, 2026-02-12T22:05:07Z | ✓ |
| 12 | `<BY3PR13MB...>` 2023-09-11T22:49:35Z | version record | ✓ |
| 13 | `<BL0PR1501...>` 2023-09-14T18:56:10Z | revised letter | ✓ |
| 14 | `<CAPBs_a46H9SCR...>` 2023-09-20T20:03:08Z | signed with Segerstrale's | ✓ |
| 15 | /238, /381 version dates | 2023-08-28T22:12:51Z, 2023-06-21T15:53:29Z | ✗ dates match but see CS-18 |
| 16 | /381 | board of four | ✓ "shall be 4" |
| 17 | `<A658306E...>` | Enes supplies three addresses | ✓ |
| 18 | `<0CDD5A07...>` | all three brothers wired | ✓ quoted in Enes's reply |
| 19 | `<176175429549...>` | ES-17 34,439, Jan 28 | ✓ |
| 20 | `<CAPBs_a6mwZj...>` | ES-17 letter | ✓ |
| 21 | `<LV3PR19MB8524...>` | 2024-12-05T00:22:55Z | ✓ |
| 22 | C0ADGSZKR3R idx 7, 8, 81, 188, 197, 198 | as cited | ✓ |
| 23 | D04UC0UEN2V/1770664988.379119, /1770665186.368229 | told, promise | ✓ |
| 24 | D09R59580EM/1762285888.654689 | ~3 months, no closing | ✓ |
| 25 | C04UEQVDVB7/1732646280.941869 | Nov 26 18:38Z | ✓ |
| 26 | C51ECE5102ED/1770903714.600249 | Claire's question | ✓; second hop ✗ CS-17 |
| 27 | 1838216168984971198, 1808816811200364470 | consent recipients | ✓ |
| 28 | f_414596b0..., /167 | Owen Baker 0.162%, 5.874% | ✓ |
| 29 | Task List, row 2 | "Send email to investors" | ✓ |
| 30 | /cards/801, /actions/5221, /5282 | open, Done, Nov 12 | ✓ |
| 31 | `/comments` | empty | ✓ 0 |
| 32 | `/contacts/170`, `/108`, `/139` | S06 | ✗ CS-19 |
| 33 | T3 resolver | Feb 12 entries move the count | ✗ CS-07 |
| – | §1a "Not touched: NB-32" | | ✗ CS-19 |

FIN-000041 and FIN-000061: entry ids exist in FINANCE_LEDGER; amounts not re-read.

**CS-17 · MINOR:** C8's second hop repeats Claire's ts. Leonard's replies are 1770906363.694689, 1770906384.346369, 1770906457.651809.

**CS-18 · MINOR:** T9's first version record uses /238's `modified_time`, though §1a says "Avoid: no row on its timestamps". /381 has the same oddity, unflagged (created 16:07:01Z after modified 15:53:29Z). Use the mail dates, or note that these are manifest-only.

**CS-19 · MINOR:** S06's pointers are dead, inherited from the hazard file. `contacts.json` has 170 rows, so `/contacts/170` does not exist; /108 is SVC_0011 and /139 is graham@. The real rows are /169 (Leonard) and /138 (Frederick). And §1a lists NB-32 as "Not touched" while ENG-2454 is Douglas and §10 resolves NB-32; move it to touched.

**Design-document defects (not coherence failures, but /create-injection reads them):** §1a cites "§0 item 1, 2, 5, 6, 7, 8" and "§3 B, §3 D"; §0 has no numbered items and those letters live in §1a. §11's estimate says Slack 8 and GCal 3, but it lists 2 Slack records and one sole-attendee event; name the rest.

## 8 Sibling defects

Traps tested for a second record with the same defect, which would change the stated answer. **None found that changes an answer.**
- T4 and ES-18: no seventh letter (18 hits, complete). No 2026 mail to PERSON_2684 or PERSON_1174 in any mailbox (9 and 16 hits, complete). Robert's DM with Oliver does not tell him of the closing; it says "restructuring" (D07H86MV4DN idx 320, evaluator-only). Slack 2026-02 sweep for shut, kapat, closing, wind down, terminat, letter: nothing new addressed to Vincent or Oliver.
- T7 and T8: Enes (1850625296912603629), Schaeppi (1847629332615617366) and Matthew (1847258343060233599) late-2025 mail is introductions only, nothing on closing. Slack 2026-02 has no message from Matthew, Tor, Nebojsa, Vincent or Frederick.
- T3: 268,772 ties exactly: 110,479 + 54,529 + 103,764. 243,757 and 266,436 tie too.
- T5: all notices go to Leonard alone (s2, not re-run).
- T21: the Nov 12 move was a bulk sweep of several cards within seconds, which supports "no update followed", as does Leonard's Nov 4 "I haven't sent any investor updates recently".
- T10: consent recipients confirm Phil, Leonard, Robert. Design's Arthur note stands.
- Termination Notices f_105b... reads `<REDACTED_FILE>`, so it cannot carry a seventh letter in readable form.

## 9 Not checked

- Seed text. There is no SQL or body text, so wording findings are about planned fields.
- PDFs, images and xlsx: read none. #winddown idx 192 ("from [Phil]", an image) stays unread and sits beside idx 194 "We don't have to Chase anyone I guess". Signed-agreement claims rest on s1 as a lead.
- FINANCE_LEDGER amounts; Snowflake generally; Confluence beyond name searches.
- Whether the last base mail differs by mailbox: Leonard's ends Feb 13 11:35:57Z, so the KPMG and Sunset seeds are the only mail in his final 12 hours. No rule forbids it; other mailboxes not measured.
- `vincent.parker@` as a recipient: that query hit its 2,500 limit (incomplete). His personal address was complete.
- The 14 "Termination details" threads: 8 read in full against s2 (ES-2, 3, 5, 6, 13, 14, 16, 17); the other six Feb 12 entries were seen by subject and date only, and their figures come from s2. The sums tie exactly.
- Sections 2, 6, 8 to 10 and 12 to 13 of the design beyond what the findings needed. Rubric and OE effects of the fixes.
- Method note: the first Gmail and Slack reads used a read-only script on the export. Every record quoted from those reads was re-read through `hg.py` before writing this. All later reads went through `hg.py`. Nothing was written outside this file and the scratchpad.
