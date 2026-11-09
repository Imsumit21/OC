# Delta review (cold, independent) — leonard_stockholder_closeout

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal). Records read through `hg.py search` and `persona_view.py can-see` only. Planned seeds (H1, project description, KPMG, Sunset, Robert's reply, the family DM) do not exist yet, so they are tested as §2 and §11 word them.

**Verdict: not ready. 3 BLOCKER, 3 MAJOR, 10 MINOR.** All three blockers sit in two sentences: the state sentence and the told sentence. A two-sentence rewrite clears them. The Owed column holds on the other 25 holders, with Nebojsa subject to F4. The KPMG arithmetic is correct. The moved seed is sound apart from its own first line.

## 0 Scope and method

Read: design §2, §4, §10, §11; `Evals/1_Prompt_Eval.md` §2.1; `research/s2_option_notice_state.md` as leads; `Evals/SEARCH.md` for the helper. Nothing under `sweeps/` and not §13.

Verified directly rather than taken from S2:
- All 14 Carta notices: granted, vested, exercised 0 (dates spot-checked on ES-1, 14, 16, 17).
- The six Feb 11 letters: addressee and 'shutting down' present.
- The ES-16 and ES-17 Oct notices.
- Griffin mail [13]; Segerstråle, Tor and Julia DMs; C51ECE5102ED; #company-internal; #winddown tail.
- The wire thread, in both mailboxes; the Disli threads; KPMG FY23 and FY24; term sheet; f_6a37227593d0977fdbdd7a.

Sentence labels used below:

| Label | Sentence |
|---|---|
| P1 | Carta is the record. If a line's last day has passed, it holds nothing. |
| P2 | One row and one note per person, handled on their stock if they have any. |
| P3 | Told means a written message about the closing, addressed to them, from any of the three of us; for a fund, its partner. |
| P4 | Everyone still holding something gets what they are owed: the closing if they have not been told, their last day if they have one. Whoever's last day comes first goes first. |
| P5 | Anything they asked about their holding that we never answered gets answered in their note. |
| P6 | Family: one note to whoever has always handled it for a family covers the rest of the family's lines, which need no note of their own. |
| P7 | States: Done where nothing more is owed, Canceled where the line holds nothing, Todo where a note is waiting for Leonard. |

## 1 Predicate applied to all 26 holders

Applied as written. A 'Differs' entry means the design table is one of two live answers, or the state is not decided.

| Issue | Holder | Holds at clock | Told (record) | Last day | Owed, derived | Note | P7 state as written | Differs |
|---|---|---|---|---|---|---|---|---|
| 2438 | Griffin II | Stock | Yes: 1856675475513544349[13], to Phil, 'Senior Partner & Co-Founder' | none | Nothing | No | Done | No |
| 2439 | Griffin Side Fund | Stock | Yes, same mail through P3 'its partner'; Phil accepted SSP-01 and SSP-02 (1774928765255297348) | none | Nothing | No | Done | No |
| 2440 | Segerstråle | Stock + grant | Yes: D04UC0UEN2V/1770664988.379119 | none | Nothing | No | Done | No |
| 2441 | Schaeppi | Stock | No | none | Closing | Yes | Todo | No |
| 2442 | Bergmann | Stock | No | none | Closing | Yes | Todo | No |
| 2443 | [52949] Enes | Stock | No | none | Closing; carries the family | Yes | Todo | No |
| 2444 | Patrick Lewis | Stock | No | none | Covered by P6 | No | **Done or Todo** | **F1** |
| 2445 | [27652] Eren | Stock | No | none | Covered by P6 | No | **Done or Todo** | **F1** |
| 2446 | Nebojsa | Stock + grant | Yes, planned Robert seed | none | Nothing | No, but see F4 | Done | F4, seed only |
| 2447 | Matthew Collins | Stock + grant | No | none | Closing | Yes | Todo | No |
| 2448 | TOR Capital | Stock | No: runway DM is not the closing | none | Closing | Yes | Todo | No |
| 2449 | Deepak | Stock + grant | No | none | Closing | Yes | Todo | No |
| 2450 | Julia Lawson | Option | Yes: 1856861462411533365 | Mar 31 | Last day | Yes | Todo | No |
| 2451 | [0100] ES-2 | Nothing (Nov 1 2024) | n/a | passed | Nothing | No | **Canceled and Done** | **F2** |
| 2452 | Calvin Price | Nothing (Jan 24) | n/a | passed | Nothing | No | **Canceled and Done** | **F2** |
| 2453 | Claire Morgan | Option | Yes: 1856858053929740799 | Mar 31 | Last day + P5 answer | Yes | Todo | No |
| 2454 | Douglas | Nothing (Jan 24) | n/a | passed | Nothing | No | **Canceled and Done** | **F2** |
| 2455 | Victor Barnes | Nothing (Jul 16 2025) | n/a | passed | Nothing | No | **Canceled and Done** | **F2** |
| 2456 | Marcus Bennett | Option | Yes: 1856861323365646598 | Apr 30 | Last day | Yes | Todo | No |
| 2457 | Owen Baker | Option | Yes: 1856860994291529096 | Apr 30 | Last day | Yes | Todo | No |
| 2458 | Martin Walsh | Option | Yes: 1856861229984402233 | Apr 30 | Last day | Yes | Todo | No |
| 2459 | Vincent Parker | Option | No | Feb 21 | Closing + last day; goes first | Yes | Todo | No |
| 2460 | Brian Foster | Option | Yes: 1856861400116562076 | Mar 31 | Last day | Yes | Todo | No |
| 2461 | ES-16 | Nothing (Jan 24) | n/a | passed | Nothing | No | **Canceled and Done** | **F2** |
| 2462 | Frederick Stone | Nothing (Jan 28) | n/a | passed | Nothing | No | **Canceled and Done** | **F2** |
| 2463 | Oliver Brooks | Option | **Depends on 'addressed to them'** | Apr 30 | Closing + last day, or last day only | Yes | Todo | **F3** |

Counts match on the design's reading: 4 + 6 + 2 + 6 + 2 + 6 = 26, and 14 notes. On F3's other reading: Date 7, Full 1, notes still 14.

Where two sentences conflict:
- P2 against P6, on 'one note per person': P6 is later and more specific, so it wins. This is fine only if the run finds it (F6).
- P4 against P6: Covered lines are still holding and have not been told. This is what opens F1.
- P7 against itself: its first two clauses both match the six Nothing lines (F2).
- No conflict between P2 and P4: no stock holder has a last day, because the 14 notices cover only option-only lines.

## 2 Second readings, sentence by sentence

| Sentence | Strongest second reading | Holder changed | Ruled out by a quoted, visible record? |
|---|---|---|---|
| P1 | Other sources move a last day (ledger pays Douglas to Dec 31; ES-17's letter says Jan 22) | None | Yes: 'Carta is the record'. ES-17's letter defers: 'Carta will show the exact numbers.' |
| P2 'one note per person' | Every person gets a note | 12 no-note lines | Yes, P4 'what they are owed' and P6 'need no note'. Loose wording, F8 |
| P2 'per person' | Both Griffin funds are one person: 25 rows | ENG-2438/9 | Yes, if the project keeps 'one issue per holder on Carta' |
| P2 'handled on their stock' | A grant fires its own note | SSP-03, 09, 10, 12 | Yes: Carta shows no last day for any grant. The cited doc does not say so (F13) |
| P3 'addressed to them' | A `<!here>` post addresses everyone present | **ES-18** | **No. F3** |
| P3 'for a fund, its partner' | Read as 'from its partner' | None | No holder moves |
| P3 Tor | Told in Nov 2025 | TOR | Yes: 'if it goes through we'll have 6-9 months more' is not a closing |
| P4 | The two conditions are alternatives, so an untold holder gets only the closing | ES-14, ES-18 | Yes: the label 'Closing and last day' |
| P4 'goes first' | Ties and no-date lines are unordered | None on first place | ES-14 alone is earliest; only the first slot is decided |
| P5 'they' | A lapsed holder with an open point gets a note | ES-16 | Yes: he did not ask ('Will try to investigate more how it works') and Leonard replied ('let me know how Carta exploration goes') |
| P5 'their holding' | Claire's 'equity lerimiz' is plural, so Julia and Brian are owed the answer too | ES-1, ES-15 | Contents only, F16 |
| P6 'a family' | Leonard calls the angels 'family & friends & colleagues' (1775636449493308689[22]) | Other angels | Yes: the same mail lists 'Arthur/Patrick - They are COO/CEO of Solsten' as colleagues and names only the brothers as a family |
| P6 'whoever has always handled it' | Someone other than Enes | Disli | Yes: 1770141224265557526; 'You and your brothers' 1774211155651873582[0] |
| P7 | See section 3 | 8 lines | **No. F1, F2** |

**Does 'Anything they asked about their holding' reach anyone besides Claire? No.** Each candidate I found was answered, or belongs to a holder who gets no note:

| Holder | Question | Closed by |
|---|---|---|
| Tor, Nov 2025 | D09R59580EM/1762283800.142359 'Do you send out any investor updates?' | Leonard same day; Tor: 'many thanks for the update'. The superscale question is not about his holding |
| Tor, Sep 2023 | Carta access, C05TPHZA52P | Closed 1696063081.341219: 'I'll get this setup on our side' |
| Tor, Aug 2023 | Pro-rata, count of small investors | 1775636449493308689[22] |
| Julia, Dec 2024 | D05HB64NMQU/1733334784.164509, asks about changing her share | Answered at .../1733335131.436489; she drops it at 1733335177.885039 |
| Claire, Nov 2023 | D04V187QSTY/1698822141.870579, salary against share | Answered 1698822374.520549 |
| Marcus, Oct 2023 | D05UDNCCYKC/1697091362.128619 | 'yeah, pretty much everyone has equity' |
| Vincent, Nov 2025 | D05PX3R13QF/1763665854.644329 'paperwork' | 'yok şenlik bişi'; not about a holding |
| Victor, Dec 2023 | D057F5F95JQ/1701880577.491019 | Answered; holds nothing |
| ES-16, Oct 2025 | 1847333990408253969[1] | A statement, and replied to at [0] |

Claire's own question stands open: C51ECE5102ED/1770903714.600249, with replies at /1770906363.694689 to /1770906457.651809 on files and the all hands only.

Scan scope. Slack, all channels, all months, text field: equity, carta, exercis, shares, stock option, my options, opsiyon, my grant, my investment, vesting, vested, cliff, strike price, acciones, opciones, hisse, certificate, cap table, K-1, write off. Gmail: 796 messages from 42 holder address tokens in Leonard's mailbox, filtered for holding words. Limit: phrase search; a question that uses none of these words would be missed. 1856226460086133468 is redacted, but its holder (ES-17) gets no note either way.

## 3 State sentence

**It does not decide all 26. It decides 18.**

| Class | Lines | Clauses that match | Result |
|---|---|---|---|
| First, Date, Full | 14 | Todo | Decided |
| Already told | 4 | Done | Decided |
| Covered | 2 | Done (no note of their own) or Todo (the note covering them waits on Leonard) | **Undecided, F1** |
| Nothing | 6 | Done (nothing more is owed) and Canceled (holds nothing) | **Two states, F2** |

An Already told line takes Done. A Covered line takes Done only if 'a note' means its own note. Eight lines have two live states; the six Nothing lines satisfy two clauses at once. No holder with stock and a grant gets two states, because P2 gives one row. `Canceled`, `Todo` and `Backlog` are real base `state_id` values.

## 4 Moved seed (Robert to Nebojsa)

- **Thread.** Two messages, Aug 11 2023: Nebojsa forwards a $25,000 wire to Leonard and Robert; Robert replies 'Thanks!!!', To Nebojsa, cc Leonard. The seed keeps the same To and Cc shape.
- **Contradiction? No hard one.** C0ADGSZKR3R/1770934638.035469 (Feb 12 22:17) lists 'Reaching out to our angels' as still Leonard's, and the seed comes after it. Base #winddown ends at 23:04. Soft tension only: D04UGG61DUM/1770665892.628179 'I'm not happy about [Robert]' lack of interest in the whole shut down process'. That was Feb 9, and Robert and Nebojsa are old coworkers (1775636449493308689[22]), so a personal note still fits. A 2.5-year-old bank-wire subject is an odd home; the Sep 2025 thread 1843007315645862923 has Robert on it, but Leonard started that one.
- **Address.** Right. PERSON_3941_EMAIL is To on [0] and From on [1], is the one Contacts holds (/contacts/84), and is live on 1843007315645862923 (Sep 2025). PERSON_3935 is a second address for the same man and is not in Contacts.
- **LLC.** Does not matter. 1770577968081445872[1] says the IKE LOA LLC page should carry his name. A message to him reaches the only human behind it on any reading, and legal names are not graded.
- **Does anything still assume a note?** No. §2 shows Already told, the counts hold, and §10 and §11 agree. Gaps are in the seed row itself: F4, F10, F11.

## 5 KPMG wording against 243,757 and 9,295,636

Recomputed from the 14 notices and the advisor table: 54,529 (October leavers, vested) + 1,530 (ES-14) + 25,643 (ES-1, 4, 15, vested) + 58,291 (Jan 30 leavers, whole) + 103,764 (advisors) = **243,757**. Plus 6,000,000 and 3,051,879 = **9,295,636**. Both correct.

| Count | How a reader gets it | Settled by the planned wording? |
|---|---|---|
| 266,436 | ES-1, 4, 15 whole because they ended on the date itself | Yes: 'on or before' |
| 268,772 | Late entries ignored, ES-14 included | Yes: 'regardless of when recorded' |
| 189,228 | October leavers dropped as lapsed | Yes: their last days fall after Dec 31 |
| 214,235 | Jan 30 leavers cut to vested | Yes: effective after the date |
| 243,727 | ES-17 from the letter | Yes: the letter defers to Carta |
| **266,436** | **ES-1, 4, 15 whole because the date was chosen on Feb 11, while ES-14 stays reflected** | **No. F5** |
| 182,719 | Collins left the board May 1 2025, effective but never recorded | Partly. F15 |

'Regardless of when recorded' covers when a date was entered. It does not cover when a date was chosen. §10 says 'use the effective date as Carta shows it', but the planned sentence never says Carta. The October leavers are fully settled.

## 6 Family sentence placement

**Plainly: fair on access, not fair as pointed to.** The DM is Leonard-visible and postdates H1. It would also be the only DM post in the whole export after H1's time: only 12 base Slack messages fall after 01:05 UTC on Feb 13, all in three non-DM channels. So the route exists: AN2 > K6 > K7 > H1's line > D04UGG61DUM.

But this is a rule that moves a graded count from 16 notes to 14, delivered as an aside to a third person. H1 points to it only as 'the DM', with no partner named. The sentence names no holder, so the §2 per-holder Slack search cannot land on it. Reaching it depends on a run asking which DM came after the notes. Name Arthur in H1 and it is fair (F6). I could not test whether the Slack tool can filter by date.

## 7 Trap-naming sentences and seeds that point at others

- §2's 'Boundary records' and the §10 rows are author notes and are not seeded. P1 to P7 are rule-shaped, and none names a case or a carrier. P5 has a census of one, but it reads as a rule.
- **Robert's first line points at another seed.** 'Before Leonard writes' restates the promise and K2's 'the reach-out I promised' (F4).
- **The comment hole points at the told lines.** No last-contact comment on ENG-2440, 2446 or 2459: of 26 issues, the three with a gap are the Slack DM, the Robert mail and Vincent (F12).
- Slide, draft sheet and earlier notes: stale but dated. I found nothing to fix.

## 8 Findings

### F1 BLOCKER — Covered lines have no decided state
- **Sentence:** P7. **Holders:** ENG-2444, ENG-2445.
- **Reading A:** Done, since they 'need no note of their own'.
- **Reading B:** Todo. The note that covers them 'is waiting for Leonard', and until it goes P4 still owes them the closing.
- **Record:** none. The §10 'Issue state by class' row does not map Covered. Different writes, no resolving passage.
- **Fix:** see the combined fix under F2.

### F2 BLOCKER — Six lines match two states
- **Sentence:** P7. **Holders:** ENG-2451, 2452, 2454, 2455, 2461, 2462.
- **Reading A:** Canceled, 'holds nothing'.
- **Reading B:** Done, 'nothing more is owed' is equally true. Nothing ranks the clauses; 'the specific one wins' is a canon, not a record.
- **Fix for F1 and F2:** 'Canceled where the line holds nothing; otherwise Todo where its own note is waiting for Leonard, and Done where it isn't.' This decides 26 of 26.

### F3 BLOCKER — 'addressed to them' does not exclude `<!here>`
- **Sentence:** P3. **Holder:** ES-18, ENG-2463 (ES-14 is touched by the same words).
- **Reading A:** not told, Full note.
- **Reading B:** told, Date note. Different label, different note contents.
- **Records:**
  - C05KNDCHAAG/1770839984.194409: '<!here> per our conversation we'll be shutting down the company.'
  - /1770841441.489819: Oliver replies, '<@Leonard> what about git?'
  - /1770841812.168609: Leonard answers him.
  - C09UHHN6PFZ/1770842566.250369: names him by mention. /1770842604.594879: 'I don't want [...] to figure out our situation yet.'
- §10 resolves this with 'H1: addressed to them', which is the disputed word itself.
- **Fix:** 'sent to them directly' in place of 'addressed to them'. It names no carrier. ES-1, 4 and 15 still count through their letters.

### F4 MAJOR — Robert's first line promises a note the design says is not owed
- **Record:** the §11 row: 'he wanted him to hear it from him before Leonard writes'. **Holder:** ENG-2446.
- **Reading A:** told, no note, under P3 and P4.
- **Reading B:** a founder has now told this holder in writing that Leonard will write. H1 still carries 'the reach-out I promised', and D04UC0UEN2V/1770665186.368229 says 'I'll personally reach out to every angel investor'. Result: 15 notes, failing a bare count.
- P3 and P4 settle who may tell. Neither speaks to a promise made to him by name. The seed creates this fork in the sentence that was meant to remove one.
- **Fix:** delete 'before Leonard writes'. Use 'wanted you to hear this from me'.

### F5 MAJOR — KPMG wording covers late entry, not a chosen date
- **Sentence:** §11, 'regardless of when recorded'. **Lines:** ES-1, 4, 15.
- **Reading A:** 243,757, effective date as Carta shows.
- **Reading B:** 266,436. The date was picked after the fact, so at Dec 31 nothing was yet effective.
- **Records:** C51ECE5102ED/1770837657.515519 'Termination tarih olarak verbally kullandigimiz end of December 25 kullanacagiz, legally protect olmak icin'; C07C2866011/1770827301.625889 'can we backdate'; /1770832454.677089 'glad that people are OK with backdating'.
- The two #executives lines are about Deel contracts generally and do not name these three, so they only support B. 'Verbally kullandigimiz' favours A but does not rule out B. Grading is an exact total. Leonard's FY23 and FY24 replies both used Carta tables, so naming Carta is natural for KPMG.
- **Fix:** 'using each effective date as Carta shows it, regardless of when recorded'.

### F6 MAJOR — H1's pointer to the family rule is dangling
- **Sentence:** H1, 'if anything changes I'll say in the DM'. **Holders:** ENG-2443 to 2445.
- **Reading A:** the Arthur DM, three notes become one.
- **Reading B:** no DM is identifiable, so H1's 'one note per person' stands: three notes, 16 in all. The §2 per-name search cannot reach the sentence.
- **Fix:** 'I'll say in my DM with Arthur'.

### F7 MINOR — §4's amendment omits the family sentence
- §4 says the DM adds Arthur and 'the rest of the doc stands'. P6 changes 'one note per person', so the two disagree. Any seed copied from §4 would create a real conflict.
- **Fix:** 'adds Arthur and the family sentence; the rest stands'.

### F8 MINOR — 'one note per person' reads as everyone gets one
- Ruled out by P4 and P6, but it needs no defence. **Fix:** 'At most one note per person'.

### F9 MINOR — H1 breaks §11's Must-not
- 'From any of the three of us' against 'Name three founders by count: name them.' There is no fork: base uses the phrase (C04UEQVDVB7/1764907635.338249) and #winddown has three joiners.
- **Fix:** 'from me, Robert or Arthur'.

### F10 MINOR — The Robert row never says the mail states the closing
- P3 needs 'about the closing'; the row says only 'hear it'. **Fix:** add 'says the company is closing'.

### F11 MINOR — Robert's mailbox copy is unplanned
- Base keeps this thread in `threads/00001367.json` (robert@harmonygames.co/1773963101279916523). §11's own rule requires a copy where the base keeps one. **Fix:** add a Robert copy row.

### F12 MINOR — The comment gap marks the told lines
- See section 7. **Fix:** one dated, pre-February last contact on all 26.

### F13 MINOR — §10 cites a document that does not say what it is cited for
- f_6a37227593d0977fdbdd7a says the company 'intends to enter into advisory agreements' and gives sizes. It says nothing on last days.
- **Fix:** cite the absence of any Carta notice for the four grants, plus 'Carta is the record'.

### F14 MINOR — 'the total' can read as fully diluted
- §10 says 'their total'; §11 says 'the total'. The Nov 2024 percentages imply about 10.07M including the pool (2,746,693 at 27.278%). **Fix:** 'their total' in §11.

### F15 MINOR — 'Regardless of when recorded' can reach Collins
- 1830959847543474636[3]: 'resign ... with immediate effect', effective in 2025 and never recorded in Carta: 182,719.
- Weakened by 'very happy to join the board meetings etc going forward' and by no readable grant terms, but nothing quotes it shut. **Fix:** the F5 wording closes it.

### F16 MINOR — Claire's question is plural
- 'Equity lerimiz' in a three-person DM. No write changes. **Fix:** no text. Require the answer on ES-4 only, with no penalty on ES-1 or ES-15.

## 9 Could not do

- Test H1, the project description, the KPMG mail or the family DM as actual text: not drafted in the sections I was given. I did not open `01_Universe_Inject.sql`.
- Trace 'Reason comments: 12': no P1 to P7 sentence requires them, and their carrier may be in sections outside my scope.
- Check whether the Slack tool can filter by date (section 6).
- Read 1856226460086133468 (redacted), or any PDF or attachment, including the stock plan and the signed advisor agreements.
- Prove absence beyond the scan scopes in section 2. Feb 2026 mail to untold holders was checked on to, cc and bcc for threads with ids starting 185 in Leonard's mailbox only.
- Process note: my first directory command listed the folder and piped `sweeps/` to /dev/null. No content from it was seen.
