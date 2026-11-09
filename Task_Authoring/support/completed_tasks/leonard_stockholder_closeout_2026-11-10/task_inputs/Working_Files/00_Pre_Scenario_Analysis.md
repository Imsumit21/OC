# Pre-scenario analysis: Leonard Hayes · Executive · Finance · Authoring (analysis only)

Contains no prompt, Oracle Event or criterion text. Written 2026-11-07 for `/create-scenario`. Probabilistic numbers are labelled **UNCALIBRATED**: they are design aids, not measured rates (learnings §9).

**Recommendation.** Build storyline A, "The stockholder close-out": the investor letter Leonard drafted but never sent, the one-to-one outreach he promised every angel, and the holder schedule underneath them, plus KPMG's yearly confirmation for Griffin. The need is real in the base. Nine angel lines have not been told, by any record. The answer set is closed: 29 holders keyed by certificate or award id, tying exactly to three figures nobody can guess.

**On your hard target, plainly.** The assignment stays medium, so the platform gate stays < 85 %. You asked me to aim at the Hard bar (< 70 %, design target E[avg] ≤ 62 %).

| Sketch | Model E[avg] | P(< 70) | P(≤ 62) | P(all gates, platform < 85) | P(all gates, hard bar) |
|---|---|---|---|---|---|
| Base design | 74.1 % | 0.24 | 0.03 | 0.76 | 0.20 |
| Variant H (hard-leaning, recommended) | 70.4 % | 0.47 | 0.10 | 0.82 | 0.40 |

All UNCALIBRATED, at design rates, rho 0.15. Past proxies ran 5–10 points optimistic even before `/rubric` added rows. So my honest central read for Variant H is **a first baseline around 72–80 %**. That is safe for the platform and likely meets your standing target of under 80 %. It probably misses 70 % on the first try, and **62 % is not supported by this evidence**. Of the ten completed tasks with a baseline, only Douglas got under 70 % with a passing SD (56.3 %), after three hardening rounds. §6 shows what would have to be true, and decision 2 asks what you want to count as success.

**Biggest open risks.** The SD gate (it binds before the average does); an owner list that hands 27 lines in one read; every legal clause Leonard can read being a June 2023 draft; and a write path no run has ever used (§9).

**Your decisions are in §10.**

Evidence is in `Working_Files/00_PreScenario/`:

| File | Contents |
|---|---|
| `census/census_C1_open_asks.md` | What anyone actually expects from Leonard at the clock |
| `census/census_C2_holders.md` | Holder table, tie-outs, rights, traps |
| `census/census_C3_sources_uses.md` | Wind-down budget census (the negative result) |
| `census/census_C4_alternatives.md` | Five other Finance jobs, ranked |
| `census/census_C5_run_habits.md` | 78 traps from real baselines: catch rates by carrier |
| `verified_anchors.txt`, `cansee_anchors.txt` | Records I re-read myself, and reach proofs |
| `reach_leonard.txt`, `entity_leonard.txt` | Reach and identity |
| `sketch_manifest.json`, `sketch_surface*.json`, `build_sketch.py` | The sketch (not the `/create-scenario` manifest or surface) |
| `policy_model.py`, `volume_model.py` and outputs, `hardness_v2_check_output.txt` | Scoring, calls, Part 7 |

## 0. Assignment and context (verified)

| Field | Value |
|---|---|
| Persona | Leonard Hayes, Co-founder & Creative Director, `leonard.hayes@harmonygames.co` (roster `leonard_hayes`, both rosters agree) |
| Function / competency / skill | Executive · Finance · **Authoring** |
| Horizon / mode | Long Horizon (`effective_profile: extreme`, GEN §3a) · **medium**: platform cap < 85 %. Requester's aim: Hard bar, < 70 %, E[avg] ≤ 62 % |
| Universe | `normal`, hg4-2026-08-31 v37. Eval clock and seed bound both 2026-02-14 00:00 UTC (Fri Feb 13, 4:00 PM PT). Shutdown rules apply |
| Persona today | Saturday, February 14, 2026; "yesterday" is Fri Feb 13 |
| Source | `task_context.py --write --require-source`: `ready`, KB `bound`, context_hash `1280066650a1…` |
| Tools | Last `Task_Authoring/tools` commit c16c7a1 (2026-11-05). The Evals input store was not touched (it holds Claire's task, Oct 1) |
| Red team | `REDTEAM_*` is unset (0 variables), so `redteam_review.py --dual` cannot run (§10, decision 5) |

**Clock limits on every seed.**
- The Slack export stops at Feb 13 10:03 UTC (NB-6). Leonard's last mail is Feb 13 11:35 UTC.
- After Feb 11 20:40 UTC most staff are single-channel guests (NB-1). The founders still post.
- Any seed about outreach state must come after Leonard's Feb 12 22:17 UTC list, which says the angels are still to do.

**Role note.** The roster says Creative Director; every record in the universe shows Leonard running the company, and Contacts says CEO. `references/Persona_Briefs.md` calls him the primary operator who owns the financial model and runway narrative. The assigned role stands. The prompt should simply not lean on a title.

**What I could not do.**
- STEP 0.6 (dataset duplicate) can't be measured locally. Closeness to earlier tasks here is judgement.
- PDFs, Gmail attachments and Slack images were not read. That covers the signed side letter, the signed Sunset SOW and the closing binder, all of which matter (§8, decision 6).
- Records I re-read are in `verified_anchors.txt`. Everything else is "census" and gets checked at `/create-scenario`.

### 0a. Lessons that shape this design

| Source | What happened | What this design does |
|---|---|---|
| `julia_zm3d_beta_calendar` | 14 revisions, no `/prompt` pass: an open set with about 90 candidates | **This is why A beats the funding-paths record.** A's set is closed by Carta ids |
| `douglas_beta_server_signoff` | The only task under 70 % with a passing SD (56.3 %, SD 0.117). Its horizon came from reads, 19–29 writes | Variant H cuts writes that only dilute, and leans on forced per-holder reads |
| `robert_llc_takeover` | Proxy 67–72 %, SD 0.17; real 83.6 %, SD 0.103. `/rubric` took 73 rows to 130 | Model on the final row set. Read every figure here as optimistic |
| `frederick_q4_commitments` | 71 % but SD 0.016: de-naming sent five traps to 0/6 together | Keep traps reachable at different rates; no heavy all-fail floor |
| `claire_zm3d_halloween` | Four rev3 records were read by 0 of 7 runs. Only mid-findability traps split runs | Plan at least two traps near 50 % |
| `robert_winddown_closeout` | `/prompt` Business Function 3 for bookkeeping; average 85.7 %, SD 0.034 | Founder deliverables lead; the schedule sits underneath |
| census C5 | Runs read a hidden record 183 times and applied it 178: **reading decides it**. Pointers beat carriers: PR inline 0/18 unpointed, 6/6 when named | Keep every carrier unpointed. No rule names where its fact lives |
| census C5 | A fact that changes an item's call flips 4–13 rows; one that changes a cell flips 1–2 | The FAM channel changes three holders' calls at once |
| census C5 | Any trap under about 10 % of final weight adds no spread | Five of nine channels are still under 10 % (§6): the top design task |
| learnings §26, §32 | Rules only on injected Confluence pages are unsafe | No Confluence in the seed plan |
| learnings §63–66 | A rule's open set can't be patched item by item; each clarifying sentence spends difficulty | Closed rules from the start (§4) |

## 1. What a 5 needs at each gate

| Gate | What a 5 / PASS needs | Risks specific to this task |
|---|---|---|
| `/injection` | Every seed checked against the whole universe; dated after the base events it relies on; schema, id contracts and companions right | Seeds must not move any share figure, or the three tie-outs break. Side-letter and SOW text can't be checked without opening their PDFs |
| `/prompt` | Every sub-dimension 5: fit, UGT two-reading table, feasibility, ACL reach, truthfulness, naturalness, coherence on task-touched data | Fit, if the schedule reads as bookkeeping. UGT on "fully diluted" and the Dec 31 boundary (§4). Don't assert angels were told. Don't state Leonard's title |
| `/hardness` | Score 5 means real failures defeat much of the core result; 3–4 still PROCEED, 1–2 HOLD | A thorough run that finds the owner list gets most lines right. Difficulty must sit in status, rights and dates, not in the census |
| `/oe` | Every step discoverable from the prompt or an earlier Expected value, with accurate tools and values; no attachment reads | Search terms can't come from a target's own title. Token-only holders are enumerated by id, never "the rest" |
| `/rubric` | Atomic "The Agent …" rows; weight by kind of work; ≤ 5 samples per group plus a volume row; no count bundled with an identity; no do-nothing rows; one row per write | Holder rows multiply. Every accepted name form goes in the title, tokens included. Never grade an address |
| `/create-difficulty` | Six Opus 5.5 slots; corrected average < 85 %; < 5 full passes; SD 0.1–0.3; ≥ 2 patterns, largest ≤ 50 %; ≥ 100 counted calls | SD is the binding gate. One builder weight typo took a passing SD to a failing one on the bridge task, so aim above 0.12 |

## 2. Leonard's reach at the clock

Census in `reach_leonard.txt`, identity in `entity_leonard.txt`, per-record proofs in `cansee_anchors.txt`.

- **Slack.** 293 visible channels. YES: `#winddown` `C0ADGSZKR3R`, `#admin_foundersonly` `C04UEQVDVB7`, DM `D04UC0UEN2V` (Segerstrale).
- **Gmail.** 17,635 threads, 22,648 messages. 75 Carta notices sit here, and the 14 termination notices are in his mailbox only.
- **Drive family.** Owns 817 items; 413 more are shared with him. Root `d_63fffeb4fab5233ed5bb73` is the write home. YES: Reset term sheet, Due Diligence Disclosures, Tor side letter drafts, charter drafts, Task List, Gemini notes.
- **Unscoped.** Linear, GitHub, Trello, Contacts, Confluence, Snowflake.
- **Not visible, even to Leonard.** The three advisor agreements (Collins `f_c2c881ccc407fbdaeaa362` re-checked: NO; owned by a Resource account with empty sharing), nine later consulting agreements, the Bridge Round sheet, and the Jun, Jul and Sep 30 P&L versions. The Atlas is wrong on the last two.

**Remit.**
- His promise, Feb 9: "I'll personally reach out to every angel investor of the company before I send out 'winding down' email" (`D04UC0UEN2V` idx 1).
- His Feb 12 list: "Reaching out to our angels properly and let them know about the situation" (`C0ADGSZKR3R` idx 197).
- Task List row "Send email to investors", unticked (`/sheets_spreadsheets/76`).
- The investor draft is in `#winddown` (ts `1770664700.848759`), unsent. None of his 39 February sent messages goes to an angel.
- He sent the only investor update ever (May 18, 2024) and answered KPMG in Feb 2024 and Dec 2024.

## 3. Storylines and choice

| # | Storyline | Fit (Exec inside Finance) | Reach and data | Originality | Hardness and volume | Verdict |
|---|---|---|---|---|---|---|
| **A** | **The stockholder close-out.** Letter, one-to-one notes, holder schedule, KPMG confirmation for Griffin | Strong: cap table is named in Finance; investor coordination is core founder work. Risk: the schedule alone reads as bookkeeping | Strong. 29 holders provable by id, no seed needed for identity or shares; exact tie-outs | Good. Nearest is Frederick's prospect send list: a different cohort and job | Eight channels plus FAM. About 145 calls in Variant H | **Recommended** |
| B | **Every funding path.** Alternatives-considered memo over 35–40 engaged parties | Strongest on voice | Good on money, few NB cards. About 15 rows token-only; closers in per-firm threads, some Turkish | Medium: about 23 firms overlap the bridge task | Naturally mid-catch, 130–170 calls. **But an open set, no record asks for it, silent endings need a rule** | Runner-up |
| C | **Wind-down budget.** Sources and uses with priority of payment | Good on paper | **Fails.** Of 41 lines 16 close, most at $0; only one non-zero forward line. Nine seeded facts would carry the answer; no record states an order of payment | Weak: judged 0.65–0.75 against the Sunset schedule | About 85–145 calls; traps total about $1,000 | Reject |

Also rejected as whole tasks: asset offer (about 25 items, 60–70 calls, money unprovable for 2 of 3 titles), promise against outcome (about 48 claims but 50–60 calls, NB-2/3/20), UA payback (9 lines, ad revenue can't join to channel), founder exposure (10–12 items).

**Why A over B.** B has better natural catch rates, and on hardness alone it might be the stronger candidate. But it is exactly the shape that ate 14 revisions on the Julia task: "everyone we approached" is an open set, and its ask would have to be invented. A's need is in the base and its set is closed by ids. Fixing A's difficulty is a design problem; fixing B's UGT has historically not converged.

**Why the Robert census rejection no longer applies.** It rejected this job on reach. From Leonard's view:

| Robert census said | Leonard's view shows |
|---|---|
| "No record lists them"; about 12 holders provable | An owner list exists: 27 lines, sum 9,477,719 (re-computed). Its home is a Nov 26, 2024 workers'-comp email (subject has no investor word), also in `#admin_foundersonly` |
| Segerstrale $75,000; "Enes family" one holder | $50,000; three holders at $25,000 ("they are holding shares individually", re-read) |
| Option gap of 65,512 unexplained | Closes exactly (below) |
| Matthew's board exit not found | He resigned May 1, 2025 (re-read) |

**Tie-outs, re-computed by me from the raw figures.**

| Check | Result |
|---|---|
| 12 Series Seed lines sum | 3,051,879 = term sheet |
| sum(floor(line/40)) × 10 | 762,880 = term sheet |
| Griffin floor test | 686,660 only with two fund lines (one line gives 686,670) |
| Options, Jan 22 snapshot | 110,479 + 54,529 + 103,764 = 268,772 = term sheet |
| Options live at the clock | 55,942 + 103,764 = 159,706 |

**How A keeps Founders/Exec fit.** The deliverables that lead are the letter, the one-to-one notes and the consent ask. The schedule is the working underneath. If `/prompt` scores Business Function 3, the fix is a stronger judgment ask, not more figures.

**Scope that keeps it clean.** No dollar waterfall (NB-3, NB-4 block any residual). Percentages of preferred are fine. Sunset's fee and the creditor side stay out; they belong to other tasks.

## 4. UGT plan (rule 1)

1. **One closed method record.** A seeded notice list from Sunset's legal or customer-success side, a non-owner voice, dated after its Feb 12 mail. It sets who counts as a record holder, how option awards are treated, what a holder's line must show, and the notice route. It holds rules only, with no item-level resolver. Every sentence is applied to all 29 holders before SQL (learnings §21, §63).
2. **Closed rules, from census C2.**
   - Record holder: has a CS or SSP certificate. An option line is not stock. 15 and 14.
   - Option state at the clock: last day to exercise after Feb 14, 2026. 8 live, 6 lapsed, plus 4 advisor grants with no notice.
   - Told state: a written record of the shutdown reaching that holder before the clock.
   - Notice route: Tor by email or courier with a TLAS copy, never post; others electronic.
   - Consent: dissolution needs the preferred majority; Griffin alone carries it at 90.0 %.
3. **Completeness rests on a census.** 15 + 14 lines, all keyed by id, with three tie-outs as the check.
4. **Forks to settle before `/prompt`:**

   | Fork | Settled by |
   |---|---|
   | "Fully diluted": issued plus options gives Griffin II 28.6 %; with the unissued pool, 26.2 %; the owner list says 27.278 % combined | KPMG's request defines it. Without that this is a real fork |
   | Awards ended exactly Dec 31 (ES-1, 4, 15): 266,436 or 243,757 options at Dec 31 | The request's as-of wording, stated. Otherwise pick a date that avoids the tie |
   | The term sheet's 268,772 gives 28.563 %, within 0.007 of one correct reading | Grade the **count**, not the percent; a percent row can pass with wrong inputs |
   | Every clause is a June 2023 draft; the filed versions are PDFs or missing | The method record states what it relies on, or a seed supplies executed text |
   | Major Investor threshold is blank | Keep it off the graded path, or seed one above 50,865 and at or below 84,438 |
   | Final side letter text is a PDF | Decision 6. Otherwise grade only that Segerstrale is a party and the Drive copy is a draft |
   | Family contact: three record holders, one acting contact | Needs a stated rule; the base shows the habit but no rule |
   | Nebojsa's holder of record: person or LLC | Keep it off the graded path, or settle it with a record |
   | SSP-06/08 and ES-8/10 assignment by elimination only | Never grade which is which |
   | Patrick: two people; `patrick@` collides | Never grade an address |
5. **Keep off the graded path:** NB-1, NB-3, NB-4, NB-6, NB-12 (token-only names, key by id), NB-15, NB-20 (now with a third value, $140K in the Drive deck), NB-22, NB-29, NB-31; wire dates; any dollar distribution; DocSend joins.
6. **Two blind sweeps before `/injection`** by fresh `hg.py`-only agents: a fork sweep, then a seeded-versus-base coherence sweep across all mailboxes. Cold reviewers are the bar.

## 5. Hardness plan (rule 4, Hardness v2)

Nine channels. `NEW` marks a planned seed not yet checked against the universe; everything else is base. Miss rates are my judgement from census C5's unpointed carriers (n = 6 per trap, other personas).

| Channel | v2 trap | Convincing wrong source | Record that beats it | Rows it moves | Placement | Miss |
|---|---|---|---|---|---|---|
| ADV | 7 · outside the filter, and 8 · wrong input (A17) | Owner list: 86,470, 81,383, 31,536 ×2 read as stock; termination notices read as every option holder | Due Diligence Disclosures advisor table: 103,764 across four angels, on no notice; only the subtraction ties to 3,051,879 | Four stock lines, totals, notes, advisor options | Drive doc | 0.40 |
| TOLD | 9 · work already done (A25) | Leonard's Feb 12 list says angels are still to do, so every angel gets a first notice | His Feb 9 DM to Segerstrale; NEW a founder DM that one more holder heard by phone | Status, count, follow-up notes, comments, reply | DM, off the list | 0.45 |
| SIDE | 5 · hidden exception (A15) | Side letter in Drive: Aug 28 draft, Tor only | 2023 mail chain: a later draft adds Segerstrale and it was signed; notices carry a TLAS copy, never post | Route for two holders, party status, copy on the note | Old mail | 0.50 |
| BOARD | 2 · correction elsewhere (A11) | Document board lists still show Matthew; Griffin's director resigned, so Griffin need not sign | Matthew's May 1, 2025 mail; the charter's preferred vote survives a director's resignation | Directors, letter, consent ask, who signs | Mail | 0.50 |
| ASOF | 4 · dates, and 8 · changed input (A16) | KPMG answered from today's holdings or the term sheet | NEW KPMG FY25 request on the base pattern fixes an as-of date; Carta entries made in February carry earlier effective dates (ES-14: Nov 21, entered Feb 12) | Options and count at that date, each fund's share | Same mail, needs a computation | 0.45 |
| FAM | 6 · different names (A8) | Three record holders means three first-contact notes | Enes acts for the family throughout (re-read: supplies all three addresses, "me and my brothers"); Eren has no mail at all. **Rule needs a seed** | Three notes, count, comments | Mail, partly Turkish | 0.50 |
| OPT | 1 · proving done (A24) | Term sheet 268,772; grant sizes on the owner list | 14 Carta notices: exercised 0, six lapsed, vested only | Live total, lapsed rows | Mail. **Pointed:** his list says "Carta terminations", so it is low-miss | 0.20 |
| ALIAS | 6 · different names (A7) | "Patrick" as one person | Wires and the owner list separate Bergmann from the Disli line | Bergmann rows | Mail, Slack | 0.25 |
| CAP | 3 · follow-through (A14) | Tor's counsel gets the same note as everyone | NEW request deep in an old thread under the cap-table-on-request term | Tor's note | Reply-all in a thread | 0.80 |

**Follow-through (trap 3).** Issue comments carry the differences from the owner list, so each trap moves more than one row without repeating a fact.

**Controls and decoys.**
- Owner list (A1 summary, met early); the 334,284 grant sum; the 2023 Bridge Round sheet's "Total committed 280,000", though it's unreadable; Leonard's "$100K" and "$75K" angel commitments.
- Drag-along, which does not reach a dissolution. Founder notes, repaid Sep 2023, so no founder is a creditor.
- Option holders who were told by letter, against leavers who were not.

**Independence.**
- Root causes are distinct across A17, A25, A15, A11, A16, A8, A24.
- Largest unit of discovery: ADV, 20.8 % of weight in Variant H. None is near half.
- Shared rows: live total (OPT, ADV). Tor (SIDE, CAP). Collins (ADV, BOARD).
- No correction sits in a hub, an anchor or a superseded record's container.

**Survives complete retrieval.** ADV needs a subtraction a reader must think to do. ASOF needs an as-of computation after everything is found. BOARD needs a rule read correctly. TOLD, SIDE and FAM are retrieval-shaped, so their rates depend on placement. **Caution:** C5 found every applied trap was a read trap. ASOF's 0.45 is the least evidenced number here, because no past run shows what Opus does with a total that won't tie.

### Part 7 checks: `hardness_v2_check.py --design` on Variant H

Output, verbatim (`hardness_v2_check_output.txt`, lines trimmed at the right):

```
  CLEAN      SAME_PLACE      4 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 9 requirements  [Part 5 rule 1]
  FLAG       DECISION_FLIP   7 of 9 rules can flip a weight-5 slot; not: ['ALIAS', 'CAP']  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     4 weight-5 total(s); 4 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  SKIP       RULE_IN_PROMPT  no prompt (04_Prompt.txt) yet  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

**Disposition of the FLAG.** ALIAS and CAP are complexity channels, not counted v2 decisions. Their rows are weight 3 by kind of work, and no weight is raised. They stay only if they earn their rows.

**How far CLEAN goes.** SAME_PLACE covers the four traps with declared version records (OPT, TOLD, SIDE, BOARD). The check re-runs on the real manifest and on the SQL. RULE_IN_PROMPT runs once a prompt exists.

## 6. Spread and score plan (rule 5, UNCALIBRATED)

`policy_model.py` scores the sketch on the planning shape: one row per write, because `/rubric` asked for that wherever it was tested. A landed trap fails each of its rows with chance 0.8, because real misses are partial; non-trap rows slip 5 %. Single-miss and whole-policy rows below take every row of a landed trap.

My first pass said 65.9 %. I threw that out: it treated misses as all-or-nothing, gave OPT a 0.35 miss despite the pointer, and left always-pass at an unrealistic 23 %.

**Base design, 134 rows, weight 290.**

| Whole policy | Score |
|---|---|
| Perfect | 100 % |
| Owner list and Carta search only, trusts the Feb 12 list | 35.9 % |
| Thorough, never opens Carta | 74.8 % |
| Thorough, trusts the owner list's share column | 80.0 % |
| Thorough except mail older than 2025 | 81.7 % |
| Thorough except DMs | 90.7 % |
| Thorough, answers KPMG with today's holdings | 92.8 % |

| Single miss | OPT | ADV | TOLD | SIDE | BOARD | ASOF | ALIAS | CAP |
|---|---|---|---|---|---|---|---|---|
| Score | 82.1 % | 80.0 % | 90.7 % | 92.1 % | 90.7 % | 92.8 % | 91.7 % | 97.9 % |

**Why the base design misses.** 62 % needs about 38 points of expected miss weight. The base design has about 25: OPT is 18 % of the weight but rarely misses, and TOLD, SIDE, BOARD and ASOF are each under the 10 % a spread trap needs.

**Variant H (hard-leaning).** 115 rows, weight 279. It cuts the per-option notices, keeps comments only where a holder's answer differs from the owner list, and adds FAM.

| Scale × rho | E[avg] | P(< 70) | P(≤ 62) | P(< 85) | P(SD) | P(all, platform) | P(all, hard bar) |
|---|---|---|---|---|---|---|---|
| 1.00 × 0.15 | 70.4 % | 0.47 | 0.10 | 0.99 | 0.83 | 0.82 | 0.40 |
| 1.00 × 0.35 | 70.6 % | 0.46 | 0.13 | 0.97 | 0.93 | 0.91 | 0.44 |
| 0.85 × 0.15 | 74.8 % | 0.22 | 0.02 | 0.96 | 0.80 | 0.78 | 0.19 |
| 0.70 × 0.15 | 79.1 % | 0.07 | 0.00 | 0.83 | 0.73 | 0.67 | 0.06 |

**Against the goal's bars.** Medium target E[avg] ≤ 77 % and P(all gates) ≥ 0.5: **met** at scale 1.0 and 0.85. Hard target E[avg] ≤ 62 %: **not met**. Expected miss weight is 0.289 against the 0.38 it needs.

**Row dilution (base design).**

| Rubric shape | Rows | Weight | Scale 1.0: E[avg] / P(all, hard) / P(all, platform) | Scale 0.7 |
|---|---|---|---|---|
| Comments sampled | 114 | 270 | 73.6 % / 0.23 / 0.77 | 81.0 % / 0.03 / 0.59 |
| One row per comment | 134 | 290 | 74.1 % / 0.20 / 0.76 | 81.4 % / 0.02 / 0.55 |
| One row per comment and state move | 154 | 310 | 74.8 % / 0.17 / 0.74 | 81.9 % / 0.02 / 0.52 |

**The honest read.**
- The always-pass figure is flattering. The tag says 15.4 % in Variant H because OPT's rows are tagged, but at a 0.20 miss they behave as near-passes, so call it about 30 %. The lowest ever observed is 44.6 %. No task here has gone below that.
- Past proxies ran 5–10 points optimistic before `/rubric`. So 70.4 % reads as **about 72–80 %** in practice.
- All rates come from other personas. Leonard's larger mailbox may push mail traps toward 1 of 6, which would lower the average and hurt spread.
- Aiming at 50 % and landing at 0 or 5 of 6 is the normal result: only 3 in 10 unpointed traps land at 2 to 4 of 6.
- **SD binds first.** More, smaller traps make it worse.

**What getting to 62 % would take.** About nine more points of miss weight, with three or four traps each carrying 12–16 %. Each of TOLD, SIDE, BOARD and ASOF needs to reach about 12 % by changing more holders' calls, not by raising weights. That is `/create-scenario`'s first job. I can't promise it exists without forcing facts onto holders that the base doesn't support. The real test is the pre-check, not more modelling: it should read each trap's catch against these rates, and C5's advice is to prove catch rates before the baseline.

## 7. Volume plan

`volume_model.py`, UNCALIBRATED. No Leonard run exists, so habits come by analogy from Robert and Frederick. A doc or sheet adds almost nothing: one to five calls whatever its size, and `gmail_get_messages_batch` collapses the Carta notices. So the horizon has to come from per-target calls, about 45 discovery plus at least 85 unbatchable.

| Phase | Calls per run |
|---|---|
| Slack: list, draft, founder channels, DMs, name searches | 12–24 |
| Gmail: Carta, wires, per-holder last contact, side letter chain, audit thread | 14–34 |
| Docs and Drive: term sheet, Due Diligence, charter, IRA, side letter, consents | 8–16 |
| Sheets, Snowflake (financing rows) | 3–8 |
| Linear meta | 2–4 |
| **Per holder (26 issues): read comments** | **22–26** |
| **Per holder: state move** | **18–26** |
| Exception comments (14) | 12–14 |
| Personal notes | 7–9 |
| Calls to book, contacts, Trello | 1–13 |
| Doc, sheet, shares, consent ask, KPMG reply, thread reply | 6–10 |
| **Modelled total, Variant H** | **mean 145, p5 130, p95 159; P(run < 130) 0.047; median six-run minimum 133** |

The base design runs higher (mean 166), but those extra calls are the easy rows that lift the average. **Your 130+ target and the 62 % aim pull against each other:** every write removed for difficulty costs calls. Variant H sits just above 130.

**No padding.** Each issue is one real holder. Each comment read must answer that holder's own question, so seeded comments need real content, with no bulk alternative (`linear_list_comments` is per issue). `Evals/references/rules/long_horizon.md` applies.

**The ≥ 500 floor is not reachable honestly.** There are 29 holders and 33 instruments. A volume and a cohort exception are needed (§10).

**Floors the exceptions don't lower:**

| Target | Plan | Status |
|---|---|---|
| ≥ 10 injected schemas, no Confluence or Snowflake | slack, gmail, gcal, linear, gdocs, gdrive, gsheets, gslides, contacts, trello | Exactly 10: tight, and every schema needs a real job |
| ≥ 10 services carrying weight | The above minus any carrying no fact, plus snowflake | Tight |
| ≥ 120 INSERTs | About 26 issues, their comments, lifecycle rows, Slack, mail, calendar copies, docs | Reachable |
| ≥ 12 fragments, ≥ 7 services, ≥ 10 containers | Sunset list, project, issues, KPMG mail, side letter, notes | Reachable; 7 services is tight |
| 2–4 authorities, ≥ 3 chains, ≥ 12 traps in ≥ 7 families, ≥ 4 supersessions, ≥ 6 distractors | Nine channels plus §5 controls | Reachable; 12 traps needs sub-traps per channel |

## 8. Injection plan (rule 3)

- **Never move a share figure, a Carta notice date, or the two historic mailings.** The tie-outs are the spine.
- **Do not** seed a Carta export or a full stakeholder list: it removes the work and risks contradicting the ties. **Do not** say Leonard already told the angels.
- **Census every seeded entity** across all mailboxes: KPMG's two associates (PERSON_3088, PERSON_4416; roles confirmed from signatures), Sunset's people, TLAS, each holder token. Give every absence check a positive control.
- **Date each seed after what it relies on.**
  - KPMG's FY25 request: on pattern, since FY23 came Jan 23, 2024 and FY24 came Dec 4, 2024. "Audit Request" subject search shows nothing for FY25.
  - Sunset's list: after Feb 12 22:22 UTC.
  - The second told record: after Feb 12 22:17 UTC and before Slack ends.
- **PDFs.** `/injection` contradiction checks cover them. A seeded side-letter text must match the signed PDF, and any Sunset seed must match the signed SOW. Neither has been read (decision 6).
- **Carriers.** No fact only on Confluence, in a GCal description or in an attachment. Snowflake stays base-only.
- **Companions.** Linear project, issue and comment stamps; GCal copies per attendee; Drive rows for injected Docs and Sheets; no activity on closed records. Trello `/cards/801` is closed, so nothing goes on it.
- **Theme.** Holders and money, so the bio-adjacent theme risk is low. Seeded text says "ZM".
- **Confirm in the pre-check** that the agent's tools return every seed, and whether Gmail search reaches BCC: the two historic mailings are BCC only.

## 9. Writes (rule 6)

No completed task used Leonard as the persona, so **none of these is proven as Leonard**. Run counts are from the 60 stored baseline runs.

| Write | Authorized trigger | Access proof |
|---|---|---|
| Letter doc in Leonard's Drive | His own ask and draft | `gdocs_create_document` in 6 of 60 runs. Leonard must own it; confirm in the pre-check |
| Holder sheet in Leonard's Drive | Sunset's list | `gsheets_create_spreadsheet` in 40 of 60, then a move into his root |
| Share with Robert and Arthur | His ask | `gdrive_share_file` in 50 of 60 |
| **Personal notes** | His promise, recorded in the DM and his list | **`gmail_create_draft` in 0 of 60: never exercised, and the verifier's view of drafts is unknown.** `gmail_send_message` is in 12 of 60. See decision 4 |
| Consent ask to Griffin | Sunset's list | Same as the notes |
| KPMG reply | KPMG's request | `gmail_reply_to_message` in 17 of 60. Reply-all is needed |
| Holder issue state, exception comments | The project's rule | `linear_update_issue` in 30 of 60, `linear_create_comment` in 36 of 60 |
| Thread reply to the founders | His ask | `slack_send_message`. Check `#winddown` posting as Leonard |

Every graded write ties to Leonard's ask or a seeded rule, so prompt, method and rows trace to the same incorporated facts (rule 7).

## 10. Your decisions

1. **Storyline.** I recommend **A**. B is the fallback if you would rather take UGT risk for stronger natural difficulty. C fails.
2. **What counts as success on hard.** The platform gate stays < 85 %. I recommend building Variant H and treating under 70 % as the aim, with 62 % as a stretch, then letting the pre-check drive hardening. If you need ≤ 62 % as a hard requirement, say so: it means more `/create-scenario` work, likely more rounds, and it pushes against your 130+ calls.
3. **Volume and cohort exceptions (GEN §3a).** Both are needed.
   - Proposed `volume_exception {call_budget_floor: 130, per_record_floor: 85}`. Reason: 29 holders, and mail reads batch, so about 145 honest calls; 500 would need padding.
   - Proposed `cohort_exception {cohort_floor: 26}` on the non-founder holders. No honest ≥ 40-record cohort exists.
   - Each needs your confirmation.
4. **Notes as drafts or sends.** Leonard's promise is personal, so drafts fit better, but `gmail_create_draft` has never run in a baseline. I recommend drafts, proven in the pre-check first, with sends as the fallback.
5. **Review waiver.** `REDTEAM_*` is unset, so the dual red team can't run. Either set it before `/create-scenario`, or confirm a `RED TEAM FALLBACK:` using the two blind sweeps in §4 plus the census and models. It stays in every Unresolved line until something covers it (learnings §44).
6. **May I read named attachments directly?** The goal says search only through `hg.py`, which can't open PDFs.
   - I would need the signed side letter, the signed Sunset SOW and the closing binder, read-only, for contradiction checks. Without them, SIDE shrinks and any Sunset seed carries unknown risk.
   - One census agent already read two Drive text files directly, outside that rule (see the notes below). Please say whether that stands.

**Next step:** once you've decided, run `/create-scenario`. It will turn this sketch into the draft manifest, the gradable surface and the design dossier, then run the blind sweeps before any SQL.

## Notes on the census work

- **Write-boundary slip.** The C5 agent's first scripts used relative paths and wrote `matrix.json`, `counted.json` and `calls/` to the repo root, then moved them to the scratchpad. I checked: none remain, none appear in my session-start listing of the root, so nothing was overwritten, and git status is unchanged.
- **Direct file reads.** The C3 agent read two located Drive text files directly, read-only, because `hg.py get` can't parse non-JSON: the SVB csv and a Sunset call transcript (`f_caf8854ecee9e636b67169`). That's outside "search only through `hg.py`". Nothing in storyline A relies on either.
- **Atlas slips to carry forward (census C4, C2; not all re-checked):** the Bridge Round sheet is 2023 content and unreadable; three P&L versions are unreadable; the advisor agreements are visible to no persona; all 37 DocSend notices are masked; NB-20 has a third value.
- **Census C1 corrections to census A:** Arthur agreed the Leapblock gesture; the SVB $38K notice is dated Jan 28; a "4K left in the bank" quote (Jan 30) sits near NB-3.
- The census agents read other mailboxes through `hg.py`, which is evaluator-wide. That is right for contradiction checks; those records are marked and never used as Leonard-reachable evidence.
- `00_Session_Goal.md` carries your two notes. Its one `WARN` refers to the `00_PreScenario/` folder this session created.
