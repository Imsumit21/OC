# rev1_run_sim: adversary simulation on the seeded text, Leonard Hayes stockholder close-out

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal). Written 2026-11-08. Read: `seed_snapshot.md`, `01_Gradable_Surface.json` (99 slots, weight 245), `01_Hardness_Manifest.draft.json`, `run_sim.md`, `delta_review.md`, `plan/policy_scores_output.txt`, `13_Hardness_v2_Opus55.md`, plus census C5 and design §2, §7, §10, §11 for calibration and truth.

Labels. **M** = measured here through `hg.py` on base data. **R** = reasoned about a seed, since seeds are not in the base (position comes from its date and newest-first search). **J** = my judgement. All catch rates are J and UNCALIBRATED. `hg.py` is a substring scan with no persona filter, so I limited mail to Leonard's thread files. Live ranking and word matching will differ. Prompt assumed: names the holder project, the #winddown draft and KPMG's request, and nothing else. Linear comments are not seeded and are assumed neutral.

## 0. Verdict

- **Expected six-run mean: 75.5 % on the surface as written, 77.6 % once one unfair row group is fixed, about 81 % after /rubric adds rows.**
- **The author's 78 % is right by accident.** Trap-tied loss is 16.5 points, not 21.1. The author is about 4.6 points too hard on traps, and that is offset by plain-row slips and an unrequested row group the model never priced.
- **Under 85 %: .88 on 99 slots, .79 at +25 % rows. Under 70 %: .13 and .03.** If Opus is sharper than my central rates, under 85 % falls to .53 and .39.
- **Every rule is now pointed.** H1, the hub, Sunset's list, KPMG's items and the DM between them tell a run what to check for each of the eight mechanisms. C5 says pointer decides: named and pointed is 97 %, named and unpointed is 40 %. What is left is the hop from a pointed rule to an unnamed record.
- **Only three mechanisms still bite:** ADV, TOLD on Segerstråle, SIDE. ASOF is ADV's shadow. ASK is nearly free. BOARD is one row. FAM is weaker than §2 thinks because the address lookup returns the family link.
- **New leak, not in any earlier review:** the issue titles "Nebojsa" and "Deepak" are not owner-list forms, and the record that bridges each title to its owner-list line is an Advisor Agreement notice.
- **Unfair as it stands:** NC_* and F2 (18 weight, 7.3 %) grade a share figure in the notes. No seeded sentence asks for one.
- **Nothing is out of reach.** One link is thin: Segerstråle's DM has no named partner (section 5).

## 1. Route: how each deciding record is reached

Hops count calls from the nearest entry point. Entry points: E1 the project, E2 #winddown, E3 KPMG.

| Record | Route | Hops | Pointed or initiative | Search test |
|---|---|---|---|---|
| H1 | E1 hub says "my close-out notes"; `gdrive_search close-out`; read | 3 | Pointed | `close-out` has 0 base hits in Drive and Docs, so only the seeds return (M) |
| Sunset's mail | Hub "what Sunset asked for", Trello comment; `gmail Sunset`; top hit | 3 | Pointed twice | Seed is newest of 27 (R, base count from run_sim) |
| DM to Arthur | H1 last bullet names Arthur; `slack_search_users`; read the DM | H1 + 2 | Pointed, person named | One Arthur in Slack users. Base DM ends Feb 12 01:13 UTC, so the 4 seeds are the newest rows (M) |
| Robert's reply | No pointer to the record. H1 Told sentence supplies `from:robert after:2026/02/01`, the word `closing`, or the holder's address | H1 + 2 | Initiative, but H1 hands over the query | Threads since Feb 2: 1 base mail from Robert, 0 from Arthur. `closing`: 8 threads, none tells a holder. `closing the company`: 0. So the seed is 1st or 2nd on all three (M, R) |
| Advisor table | Four triggers, then `advisor` in Docs or Gmail (see below) | 3 to 5 | Initiative with four triggers | Docs titles `advisor`: 5. `61,038` in mail: 1 thread, 1773160163779741845, with the whole table and names (M) |
| Side letter chain | Sunset "any special terms"; `side letter`; read top threads | 3 to 4 | Half pointed | 22 threads. 2nd newest: "has [6550]' signature as well". 5th: "[0089] Segerstråle opened and viewed ... Side Letter TLAS(final) (1).pdf". Subject search: that mail is 2nd (M) |
| Phil's resignation | #winddown page 1, H1 "board thread"; `subject:board` | 2 | Pointed | "Re: Board position" is the newest of 279 subject hits (M) |
| Matthew's resignation | `resign` or `board position` | 2 | Initiative, one word | `resign`: 11 threads, Matthew's is 6th, Vincent's 3rd. The search that finds Phil's mail also finds this (M) |
| Claire's question | H1 "anything they asked"; Slack `equity`; read | 2 | Rule pointed, word not | Feb Slack `equity`: 1 hit, the question. `exercise`, `vesting`, `last day`: 0. `option`: 30, noise. `shares`: 2, noise (M) |
| Family link | Address lookup for the note: `[PERSON_NAME_52949]` | 2 | Forced by the write | 2 threads: the owner list and 1770141224265557526, which lists all three lines. `[PERSON_NAME_27652]` returns the same two. `Patrick Lewis`: 6 threads, both family threads among them (M) |
| Segerstråle's DM | Three routes: `Segerstråle` in Slack, then open the DM; `shut down` in Feb; `angel` in Feb | 3 | Initiative | `Segerstråle`: 6 rows, one is the DM's 2023 file. `shut down` Feb: 12 rows, one is the deciding message. `angel` Feb: 6 rows, 4 real, one is the message 198 s later. `holding`, H1's own word: 2 rows, one in this DM (M) |
| Fund split | ENG-2439 title; `Side Fund` | 2 | Title gives the word | 4 threads; 1771880236343640719 has 2,662,255 and 84,438 (M) |

**The four ADV triggers, ranked.**
1. **Alias bridge (new).** `Nebojsa` in Leonard's mail has exactly 1 hit: "Nebojsa [0127] viewed ... Advisor Agreement - [0127].pdf". That is the only mail bridge from ENG-2446 to the owner-list line, and the run needs it for the address. `Deepak` returns "Advisor Agreement - Deepak Gupta" among 23 threads; Slack `Deepak` returns "Deepak just signed the contract and the advisorship". `Segerstråle` returns "world-class advisors" and the Advisor Agreement (M).
2. **Deck line.** "268,772 options outstanding (Jan 22 term sheet)" is the only seeded route to the term sheet. `268,772` has 0 hits in mail and Slack, 1 in Docs. `term sheet` is 2 Docs titles (M). Once read, 268,772 against the notices leaves 103,764.
3. **Series Seed tie.** 3,155,643 from the owner list against 3,051,879. The tie needs the term sheet or Aug 2023 mail 1773160052067710033.
4. **Id gap.** ES-8 to ES-11 are absent. `ES-9` and `ES-11` reach Carta digest 1782897835407336831 (M).

**Budget.** About 85 unbatchable writes and comment reads leave 45 to 85 calls. This route needs 35 to 45. Budget does not bind. What decides is whether a run opens a hit: C5 says a search hit is not a read.

## 2. Mechanisms

"Lands" means the run gets it wrong.

| Mechanism | Lands per run | Range | Author | Why |
|---|---|---|---|---|
| ADV | .25 | .12 to .45 | .35 | Four triggers above. Widest uncertainty: C5 has no case of a run chasing a broken total. Bimodal, expect 1/6 or 5/6 before 3/6 |
| LETTER, ES-14 | .09 | .04 to .14 | .30 | Six letters come back from one search. The Told column forces the join and the resignation stands out |
| LETTER, ES-18 | .18 | .08 to .28 | .30 | Same join, but needs the recipient key. Elimination works: six letters, eight lines |
| TOLD, Segerstråle | .32 | .16 to .45 | .40 | C5 unpointed DM is .67. Three routes, but the Feb message carries no name and the partner is unnamed. Name search alone shows only old hits |
| TOLD, Nebojsa | .22 | .10 to .35 | .40 | H1's "Robert" is a query. Seed is 1st or 2nd on three query shapes |
| TOLD, Tor | .07 | .03 to .12 | .40 | "about the closing" decides it |
| ASOF alone | .15 | .08 to .22 | .35 | The KPMG sentence states the method. Left: ES-2 and ES-6 counted as vested (259,525) |
| ASOF totals A1, A2 | .36 | .22 to .55 | | Almost all ADV |
| FAM, any line | .19 | .08 to .30 | .45 | DM pointed and read. Address lookup returns the link |
| FAM, Patrick Lewis | .29 | .15 to .40 | | Needs the wire thread or a read of the Turkish list |
| SIDE, S3 | .44 | .30 to .55 | .45 | The real mid-rate trap. Word "special terms" is indirect, and top side-letter hits are DocuSign mails a run may skip |
| BOARD, B1 | .30 | .18 to .40 | .35 | Matthew only. Phil is free |
| BOARD, T11 (B2, G2) | .07 | .03 to .12 | .35 | H1 orders the heads-up, so the wrong reading cannot occur |
| ASK, reads the question | .30 | .15 to .45 | .30 | `equity` is 1 hit, but H1 no longer supplies the word |
| ASK, Q1 row fails | .20 | .10 to .30 | | See below. A plain date note often passes |

Traps landing per run: 2.6 (author 2.95). Chance one run catches all: .15 (author .024). So expect some runs at 90 % or more.

### The named sentences

| Sentence | What it hands over | Verdict |
|---|---|---|
| KPMG item 2: "For anyone whose service ended on or before that date, count what had vested; for anyone still in service, the full grant." | The whole ASOF method and the boundary case. A KPMG associate would not write this. The earlier clause, "using each effective date as Carta shows it, regardless of when recorded", was the F5 fix; this sentence goes further than that fix. It states outright what delta section 5 left to the run's reading (214,235 and 189,228), so those honest errors go. One cost it adds: read mechanically it pulls in ES-2 and ES-6 (3,052 and 12,716). "outstanding" guards that | **Gives away ASOF.** Only 266,436 needs closing. Cut to the boundary (section 4) |
| H1: "Told means a written message about the closing, sent to them directly, from me, Robert or Arthur; for a fund, its partner." | "Robert" is a working Gmail query with 2 results. "about the closing" is the seed's word. "written ... directly" tells the run a Slack DM counts. "for a fund, its partner" settles Griffin | **Names TOLD's route.** "sent to them directly" must stay (F3). Names can go: "from a founder" still closes who may tell |
| H1: "the angels are what's open from my list" | A real wrong source: Leonard's own doc, dated after the DM. It repeats the base list, so it adds no search word. It also draws the T6 and T7 set in one line, right above the rule that tests it | **Keep.** It is the convincing wrong source the guide asks for. No fairness issue: the Told rule outranks it |
| Labels: "Nothing, Already told, Closing, Last day, Closing and last day." | "Closing and last day" can only fit an option-only line with no letter, so it announces LETTER exists. "Already told" says someone is | **Names LETTER's existence, but cheap.** The Told column forces the join anyway. Worth .2 of a point, and it closes delta P4's fork. Leave it |
| H1: "Griffin's partner gets a heads-up on the board thread once the sheet shows who holds the preferred vote" | T11 entirely. It says Griffin still matters and why, and leads to Phil's thread. G2's selector matches H1's own words. 6 of BOARD's 14 weight is free, and L6 nearly | **Gives away T11.** Say what is needed, not what it is (section 4) |
| Sunset's list | A 1:1 skeleton of the graded summary. No answers. "any special terms" and "who holds the preferred vote" name the questions. Removes every omission failure. "your own notes ... don't need to double as notices" closes a real fork | **Fair.** Asks must live somewhere. Keep |
| Family DM: "one note to whoever has always handled it for a family ... Mark those lines Covered" | The rule and the label. It names no holder, which is right. But H1 points at it by person, and it is the top of a newest-first read | **Pointed, so reliably read.** §2's "no shared surname" hiding does not bind, because the address lookup returns the family list. Move it (section 4) |

### Other seeded text that gives something away

- **"handled on their stock if they have any" (H1).** Says some people hold more than stock. Redundant: "their last day if they have one" already decides the stock-plus-grant case.
- **Titles.** §2 says titles use the forms the owner list shows. ENG-2440, 2441, 2442, 2446 and 2449 do not, and three of them feed ADV, SIDE or TOLD.
- **"Numbers on there are just what I pasted in, the sheet is the real thing" (#winddown).** Disarms the Linear figures before they exist, so T2's "wrong source met first" will not work.
- **"These replace my earlier outreach notes" and "copied from the Nov 2024 list".** T18 and T20 are dead on arrival. Harmless, no weight. T19 and T22 are the same. Do not count them as live.
- **The letters' own line, "exercising is not recommended".** Q1's selector matches that phrase, and a run will copy it into a date note. ASK adds little spread (run_sim LEAK-6 stands, for a new reason).
- **Hub, "Where no note of its own goes, say why on the issue".** Follow-through is on the page every run reads. Reason comments are near free. This is the rule's right home; just do not count it as a trap.

**ASK.** Reaching the question and the row passing are different events. Rows pass about .4 of the time without the read.

**Linear comments, still to come.** A last contact "before February" cannot be honest on ENG-2440 if written Feb 12, because the DM is Feb 9. Phrase it as a last investor update, true of all 26. An "old quoted figure" of 31,536 on ENG-2446 and 2449 lets a run skip the alias, which helps ADV's hardness a little.

## 3. Score distribution

**Method.** 99 slots. Each run draws catch states; each slot gets a pass probability given those states (plain rows .90 to .97, per C5's .93). Per six-run batch, each catch rate is itself drawn from a Beta around its centre, because C5 shows unpointed traps pile at 0 to 1 and 5 to 6 of 6. Gaussian copula rho .2, 3,000 batches. Scripts: `/private/tmp/claude-501/-Users-sumit-Source-OC/46989a83-cbdb-4145-86b5-605b4a19b678/scratchpad/sweepC/model.py`, `model2.py`, `model3.py`, `model4.py`. UNCALIBRATED.

Central rates (catch): ADV .75, L14 .91, L18 .82, SEG .68, NEB .78, TOR .93, ASOF .85, per-line reply .86, DM .95, link .85, Patrick .88, side letter found .82 and applied .68, BOARD .70, ASK .70, Griffin split .86, reply-all .80, run does not tire .95, note states a figure .55.

**By slot group, surface as written:**

| Group | Weight | Share | Mean pass | Points lost |
|---|---|---|---|---|
| ADV rows that flip (K1, K4-8, P1) | 33 | 13.5 % | .73 | 3.6 |
| KPMG totals (A1, A2) | 10 | 4.1 % | .63 | 1.5 |
| LETTER (C, TC, C_DATE, N) | 27 | 11.0 % | .81 | 2.1 |
| TOLD Segerstråle and Nebojsa (C, TC, LC) | 22 | 9.0 % | .70 | 2.7 |
| Tor rows | 6 | 2.4 % | .90 | 0.2 |
| Conjunctive counts (C_FIRST, N_COUNT) | 6 | 2.4 % | .40 | 1.5 |
| FAM (F1, F3, F4, F5) | 14 | 5.7 % | .73 | 1.5 |
| SIDE (S1, S2, S3) | 11 | 4.5 % | .65 | 1.6 |
| BOARD (B1, B2, L6, G2) | 14 | 5.7 % | .78 | 1.3 |
| ASK (Q1) | 5 | 2.0 % | .77 | 0.5 |
| **Trap-tied subtotal** | 148 | 60.4 % | | **16.5** |
| Note states a figure (NC x5, F2) | 18 | 7.3 % | .46 | 4.0 |
| KPMG lines (AL) | 16 | 6.5 % | .76 | 1.6 |
| Griffin split (K2, K3, A3) | 9 | 3.7 % | .82 | 0.7 |
| Lapsed and live lookups | 16 | 6.5 % | .95 | 0.4 |
| All other rows | 38 | 15.5 % | .90 | 1.5 |
| **Total (groups round)** | 245 | | | **24.5** |

E[avg] = 100 - 24.5 = 75.5 %.

**Scenarios:**

| Scenario | Mean | SD of six-run mean | SD across runs | P(<85) | P(<70) | P(SD at or above .10) |
|---|---|---|---|---|---|---|
| As written | 75.5 | 6.4 | .112 | .95 | .19 | .60 |
| Fair: H1 asks for the figure | 77.6 | 6.4 | .109 | .88 | .13 | .56 |
| Fair, +25 % plain rows | 80.6 | 5.2 | .089 | .79 | .03 | .35 |
| Fair, +50 % plain rows | 82.6 | 4.4 | .075 | .68 | .01 | .18 |
| Opus sharper than central, fair | 83.7 | 5.2 | .086 | .53 | .02 | .33 |
| Opus sharper, fair, +25 % | 85.5 | 4.1 | .069 | .39 | .00 | .15 |
| Opus weaker than central, fair | 71.2 | 7.1 | .123 | .98 | .42 | .70 |
| Opus weaker, fair, +25 % | 75.5 | 5.6 | .099 | .96 | .17 | .48 |

Weighting these 60/25/15 at +25 % rows gives P(<85) about .71 and P(<70) about .05 (J).

**Run spread.** Single runs on the fair surface: 5th percentile 54, median 80, 95th 94. A run that catches everything scores about 93, because plain rows slip. Missing ADV alone costs about 17, to 76. Missing Segerstråle's DM alone costs about 7.

**Against the author's model.** The policy table's single-miss cost for ADV, 20 points, agrees with mine at 17 to 19. The Monte Carlo's 78 % comes from design miss rates 1.2 to 2.3 times mine on most traps (1.3 by weight), with no plain-row slips. Same number, different cause, and row multiplication eats the author's version first. SD holds on 99 slots and falls below .10 by +25 % rows. That is now the gate at risk, as run_sim said.

## 4. Changes

Measured from the fair surface, 77.6 %. Post-change rates are J. Treat gaps under .5 as ties.

### Fix first (raises the mean, fairness only)

1. **NC_* and F2, 18 weight.** No seeded sentence asks a note to state a figure. As written this is an added condition. Add a clause to H1's handling list, or drop the rows. Either gives about +2. Keeping the rows makes NC_Deepak and NC_Collins honest ADV rows.
2. **Reply or draft, 39 weight.** `kpmg` (35) and `griffin` (4) read `gmail_reply_to_message` only. The seeds say "Nothing goes out until the sheet is right", and H1 keeps sending with Leonard for notes. A careful run may leave a draft on the thread. Accept a draft on the thread, or have the prompt settle it. If not, this is fake difficulty far larger than any trap.

### Three changes that move the mean

| # | Change | Mean | Delta | SD |
|---|---|---|---|---|
| 1 | Cut ADV's last pointers | 74.2 | -3.4 | .119 |
| 2 | Move the family sentence to a reply under the Feb 12 list | 76.1 | -1.5 | .113 |
| 3 | Trim three rule sentences | 76.3 | -1.3 | .111 |
| | **All three** | **71.2** | **-6.4** | **.124** |
| | All three, +25 % rows | 75.2 | | .100 |
| | All three, +50 % rows | 78.1 | | .085 |

All three: P(<70) .43 on 99 slots, .19 at +25 %, .04 at +50 %. P(<85) .98, .96, .93.

**1. Cut ADV's last pointers (ADV catch .75 to .56; K1 on a miss .70 to .35).**
- Deck: drop "268,772 options outstanding (Jan 22 term sheet)". Keep the section heading. C5: where nothing challenged a total, five of six LLC runs stated a wrong one unchecked.
- H1: end the line at "One row and at most one note per person."
- Titles: ENG-2440, 2446, 2449 to the owner-list forms §2 already claims. This also costs SEG .06 and SIDE .06, since the one-step name searches go.
- Reach afterwards (M): ES-9 and ES-11 in the Carta digest, 5 Advisor Agreement titles, the `61,038` mail, the term sheet by `Series Seed` or `term sheet`, the Aug 2023 tie mail, `9,051,879` in tax mail 1824509105148886763, and #executives "world-class advisors like". No deciding record is lost.
- Follow-ups: add token forms to S3, NC_Deepak, LC_Seg and LC_Neb. Retire T19. With a token title the Nebojsa address gets easier, so NEB rises about .02.

**2. Move the family sentence (read .95 to .70).**
- Carrier: a reply in the thread under C0ADGSZKR3R/1770934638.035469, keeping Arthur's sheet line with it. Change H1's last bullet so it no longer names a DM.
- Fair because H1 names that message twice ("where I left things today", "reply under my list"), and every run must write there. It is also what guide trap 2 asks for: a correction in another place, tied to the same item, changing a count.
- C5: channel thread reply .31 unpointed, DM .67, named and pointed .97.
- A run may reach it only when replying, after the notes. That is honest pressure.
- Needs `reply_count` and `latest_reply` on the parent, inside the Slack window. Confirm `slack_read_channel` shows `reply_count`.

**3. Trim three sentences.**
- KPMG item 2: replace the last sentence with one that closes only the boundary, such as a termination effective on that date counting as done. A1 and A2 then test ASOF on their own. Keep "as Carta shows it, regardless of when recorded".
- H1 Told: "from a founder" for "from me, Robert or Arthur". Keep "sent to them directly".
- H1 Griffin: a heads-up "with what we still need from Griffin". G2 then needs Sunset's line and the charter, and T11 becomes live.
- Each is under .5 alone, so these are a tie. Together they are worth doing as one pass.

### What would hurt fairness

| Do not | Why |
|---|---|
| Keep NC rows with no ask | Added condition |
| Drop "sent to them directly" | Reopens F3 on ES-18 |
| Drop "as Carta shows it, regardless of when recorded" | Reopens F5, with exact-total rows |
| Cut KPMG's last sentence with no boundary clause | 266,436 against 243,757 is a live fork |
| Move the family sentence anywhere not on the path H1 names, or leave it in the DM with no pointer | F6: a count moves 16 to 14 on an unreachable aside |
| Drop the labels line without changing P4 to "and" | Reopens delta P4 on ES-14 and ES-18, for .2 of a point |
| Take Leonard off Robert's cc | Out of the persona's view |
| Use an ASCII or altered spelling on a title | Spelling trick, guide Part 3 item 6 |
| Drop Sunset's "formal notices are a separate step" | Reopens the TLAS copy fork |
| Reword Robert's seed away from "closing" | Not unfair, but no gain: it would be newest on `wind down` and `shutting down` too (base lists M, seed position R) |

## 5. Reach and surface checks

**Out of reach: none.** Every deciding record resolves from Leonard's view. Thin links:
- **Segerstråle's DM partner.** `users.json` row 34 has only the id as name, email null (M), so it is not missing as run_sim said, but it is blank. Identity rests on the 2023 message's file name "Harmony Games Advisor Agreement - Segerstråle" and "Hi [PERSON_NAME_6550]" in the same month (M). If live Slack search does not match file names, a run must read back 2.5 years, and C5's windows run 5 to 9 days. SEG would fall to about .35. **Test this in the pre-check.**
- **[PERSON_NAME_0090] and [6550].** S3 needs a token join, but the DocuSign mail names Segerstråle outright, so a run has an easier route.

**Surface defects:**
- **B2** depends on ADV: a run dividing by its own sum gets 87.0 %. Not tagged.
- **D6** is tagged LETTER, but the earliest date comes straight from the notices, with or without the letter join.
- **F1** selector needs "Enes". The list mail shows only tokens. "Sadık Enes Dişli" is in the wire thread (M), but a run may write the token. Accept it and ENG-2443.
- **L3** says "from the draft". I read the draft: it says nothing on distributions. Support is the deck heading and the letters' "no value" line.
- **C_FIRST and C_DATE** match any 6 within 160 characters of the label, so a summary line for another class can pass.
- **Design §10** says the advisor agreements are visible to no persona; run_sim measured one shared with Leonard. I did not settle this.

## 6. Limits

- **Measured:** every hit count, quote and date marked M. Sum checks follow run_sim and delta_review.
- **Inferred:** all catch rates, post-change deltas and seed positions. No Leonard run exists.
- **Could not do:** run live tools; test whether Slack search matches file names; test snippet behaviour; read any PDF or attachment; read Linear comments, which do not exist.
- **Biggest unknown:** whether Opus chases a broken total. ADV carries 20 % of weight and its range is .12 to .45. One pre-check settles more than this file.
