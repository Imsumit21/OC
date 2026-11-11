# Pre-scenario analysis: Robert · Executive · Finance · Analysis and synthesis (analysis only)

Contains no prompt, Oracle Event or criterion text. Written 2026-11-07 for `/create-scenario`. Probabilistic numbers are labelled **UNCALIBRATED**: they are design aids, not measured rates (learnings §9).

**Recommendation.** Build storyline A, "The seed, bet by bet": the founders' account of what it cost to build each of the three games and what each returned, for Leonard's one-by-one angel outreach. It rests on 132 "Payment Processed" bank notices in Robert's own mailbox, and the base already holds several traps nobody seeded: a wire the bank marks processed that came back, a contractor Robert paid himself outside the bank notices, and a payment with no processed notice at all.

**Sketch results, all UNCALIBRATED.** E[avg] 66.6 % at design rates, and ≤ 82 % down to a 0.5 landing scale. P(all gates) 0.93, and ≥ 0.5 down to a 0.30 scale. Counted calls: mean 125, p5 110. The six `hardness_v2_check` checks that can run are CLEAN; the seventh needs a prompt.

**Biggest open risks.** Business Function fit (§3), and the SD gate, because real runs have come in flatter than proxies (§6).

**Your decisions are in §10:** the storyline, a volume exception, a cohort exception, and the review waiver.

Evidence is in `Working_Files/00_PreScenario/`:

| File | Contents |
|---|---|
| `census/census_A…D` | Four census reports (cash plan, cap table, per-game spend, payees) |
| `svb_processed_robert.json` | The 132 notices, parsed |
| `verified_anchors.txt` | Records I re-read myself |
| `cansee_anchors.txt`, `reach_robert.txt`, `entity_robert.txt` | Reach and identity proofs |
| `sketch_manifest.json`, `sketch_surface.json`, `build_sketch.py` | The sketch (not the `/create-scenario` manifest or surface) |
| `hardness_v2_check_output.txt` | Part 7 output |
| `policy_model.py`, `policy_sensitivity.py`, `volume_model.py` and outputs | The scoring and call models |

## 0. Assignment and context (verified)

| Field | Value |
|---|---|
| Persona | Robert, Co-Founder & Creative Director, `robert@harmonygames.co` (roster `robert`) |
| Function / competency / skill | Executive · Finance · **Analysis and synthesis** |
| Horizon / mode | Long Horizon (`effective_profile: extreme`, GEN §3a) · **easy**: cap < 90 %, design target E[avg] ≤ 82 % |
| Universe | `normal`, hg4-2026-08-31 v37. Eval clock and seed bound both 2026-02-14 00:00 UTC (Fri Feb 13, 4:00 PM PT). Shutdown rules apply |
| Persona today | Saturday, February 14, 2026; "yesterday" is Fri Feb 13 (learnings §20) |
| Source | `task_context.py --task-dir Task_Authoring/task_inputsS2 --write --require-source`: `ready`, KB `bound`, context_hash `4ae6fe0e2394…` |
| Tools | Last `Task_Authoring/tools` commit c16c7a1 (2026-11-04). All universe content was read through `hg.py` or `persona_view.py`. The Evals input store was not touched |
| Red team | `REDTEAM_*` is unset (0 variables), so `redteam_review.py --dual` cannot run (§10, decision 4) |

**Clock limits on every seed.**
- The Slack export stops at Feb 13 10:03 UTC (NB-6), so seeded Slack goes before it.
- After Feb 11 20:40 UTC most staff are single-channel guests (NB-1). The founders and the Leapblock contact still post.
- Google accounts are archived after Feb 15.

**What I could not do.**
- STEP 0.6 (dataset duplicate) can't be measured locally: no similarity tool is in `Evals/tools`.
- PDFs, Slack images and Gmail attachments were not read. That covers the Sunset papers, Leapblock's invoices and the Carta xlsx in `threads/00003071.json`.
- Agent findings are leads until re-read. I re-read the load-bearing ones below (`verified_anchors.txt`). The rest are marked "census" and get checked at `/create-scenario`.

### 0a. Lessons that shape this design

| Source | What happened | What this design does |
|---|---|---|
| `robert_winddown_closeout` | `/prompt` Business Function 3: "bookkeeping fits Finance / Legal / HR / Ops". Average 85.7 %, SD 0.034: about 100 of 136 rows passed every run | The job is an investor-facing account of three strategic bets. Few easy rows |
| `robert_llc_takeover` | Proxy 67–72 % and SD 0.17 became **83.6 % and SD 0.103** once `/rubric` required a row per comment and state move (73 → 130 rows). One missed record failed 14 rows | Read-heavy work with few per-target writes. §6 models the dilution |
| `frederick_q4_commitments` | 71 % but SD 0.016: de-named corrections were missed 6/6 | Each correction keeps a name or amount an ordinary search can reach. Catch rates vary by channel |
| `frederick_card_spend_q3` | SD 0.054 | Same warning: spend tasks flatten unless traps split the runs |
| `frederick_bridge_pipeline` | Passed at 77.7 %, SD 0.106, from three traps each missed 3 of 6 | Target that shape: several traps near 50 % |
| learnings §45, §46 | Corrections on the first-read path were settled at once; brute force beat per-record sampling | Corrections sit off the swept path; volume is never counted as difficulty |
| learnings §63–66 | An open set in a rule can't be patched item by item | Closed rule plus a full payee census (§4) |
| learnings §26, §32 | Rules or facts only on injected Confluence pages are unsafe | No Confluence in the seed plan |

## 1. What a 5 needs at each gate

| Gate | What a 5 / PASS needs | Risks specific to this task |
|---|---|---|
| `/injection` | Every seed checked against the whole universe, including Leonard's and Arthur's mail; dated after the base events it relies on; schema, id contracts and companions right | The Leapblock statement must agree with all 29 wires and the Sep 2023 thread. Arthur's Chase note must agree with Carta debits and the Oct 2025 Chase closure |
| `/prompt` | Every sub-dimension 5: fit, UGT two-reading table, feasibility, ACL reach, truthfulness, naturalness, coherence on task-touched data | Business Function is the main risk (§3). UGT depends on the closed method (§4). Coherence: a correct run must never need the ledger or P&L totals, because they disagree with the bank |
| `/hardness` | Score 5 means real failures defeat much of the core result; 3–4 still PROCEED, 1–2 HOLD | A run that misses two or three channels leaves bet totals wrong. A run that catches everything scores 1–2 and sends us back to revise |
| `/oe` | Every step discoverable from the prompt or an earlier Expected value, with accurate tools, parameters and values; no attachment reads | The notice search and the payee lookups must be enumerated, never "the rest". Search terms can't come from a target's own title |
| `/rubric` | Atomic "The Agent …" rows; weight by kind of work; ≤ 5 samples per group plus a volume row; no count bundled with an identity; no do-nothing rows; one row per write | Platform has asked for a row per write, including state moves. §6 models that case |
| `/create-difficulty` | Six Opus 5.5 slots; corrected average < 90 %; < 5 full passes; SD 0.1–0.3; ≥ 2 patterns, largest ≤ 50 %; ≥ 100 counted calls | SD is the hard one on this persona (0.034 and 0.103 on the two Robert tasks) |

## 2. Robert's reach at the clock

Census in `reach_robert.txt`, identity in `entity_robert.txt`, per-record proofs in `cansee_anchors.txt`. Every record below is YES.

- **Slack.** 224 visible channels. YES: `#winddown` `C0ADGSZKR3R`, `#executives` `C07C2866011`, `#admin_foundersonly` `C04UEQVDVB7`, `#leapblock` `C05URGU759U`, `#art_outsourcing` `C08FG9924R2`, `#telegram-dd` `C09KU8U4DPF`, `#playablex` `C08H78VJG80`, DMs `D04UP2L3E3S` (Leonard) and `D04V95AAAHW` (Arthur).
- **Gmail.** 16,233 threads. All 132 Processed notices sit here, with 130 Awaiting Approval, 40 Scheduled, 22 Recipient Created and 2 Recipient Modified. Also the five Western Union receipts, the Node Media mail and the Deel notices.
- **Drive family.** He owns 223 items, and his root `d_9f7ba94f7526d54d8482ba` is the proven write home. He can read the Jan 2026 P&L `f_605121f4a36752645e0ac3`, the Leapblock MSA `f_322bbfdb37d253aa8624b9` and Marcus's consulting agreement.
- **Unscoped.** Linear, GitHub, Trello, Contacts, Confluence, Snowflake.
- **Not visible.** Leonard's mailbox, including Carta mail, Sunset's payment link and the $125 return notice; the reset term sheet; every SPA, IRA and Voting copy; DMs `D04UC0UEN2V`, `D04UGG61DUM`, `D08RQSCFKJ9`; the Sunset call notes.

**Remit: records showing Robert in the money.**
- He worked through the book categories with Leonard on the returned wire itself (`C04UEQVDVB7/1712901837.860709` onward, Apr 12, 2024).
- He paid the mini-game developer himself: "I've been sending it" … "via company card" (`C04UEQVDVB7/1719603590.685019`, `/1719603595.852129`, Jun 2024).
- He and Leonard approved Leapblock's invoices (`C04UEQVDVB7/1694447284.697869`; the token mapping to Robert is inferred).
- Deel asks him to approve pro-rata requests (`threads/00016872.json`, census).
- "Co-drove the seed fundraise" (`references/Persona_Briefs.md`).
- Leonard's next steps include "Reaching out to our angels properly" (`C0ADGSZKR3R/1770934638.035469`) and he promised updates "once we have clarity" (`/1770664700.848759`).

## 3. Storylines and choice

| # | Storyline | Fit (Exec inside Finance) | Reach and data | Originality | Hardness and volume | Verdict |
|---|---|---|---|---|---|---|
| **A** | **The seed, bet by bet.** What it cost to build Domino Delights, Zombie Match and Combo Fighter, what each returned, for the angel outreach | Good: investor accountability for three strategic bets, built on fundraising proceeds. Risk: can read as reconciliation | Strong. 132 notices and 22 real payees, all but two identified from Robert-readable records; JPMorgan and the $500 helper each need a seed | Good: no earlier prompt asks for this. The nearest overlap is the LLC task's January revenue by game; lifetime build cost is new | Traps are base-native, each on a different surface. Calls need a per-payee Linear surface | **Recommended** |
| B | Holder-by-holder investor close-out | Good on paper (cap table) | Weak. No Carta record, a dead cap-table link, a blank SPA exhibit; about 12 holders provable with real names; Robert can't read the charter, IRA or term sheet (census B) | Close to Frederick's investor send lists | 28–29 holders; 40–50 calls after search collapse. "Who was told" rests on absence | Reject |
| C | Close-out cash plan: can the wind-down finish with no founder money? | Good on paper | Weak. Nobody asks Robert; every cash figure hits NB-3 or NB-4; Singular, Unity and Sunset's final fee are open at the clock, and deciding records sit outside his reach (census A) | Lowest: the vendor-list neighbours | About 50–70 calls after batching; would need ten or more seeded settlements | Reject |

**Why A, and how it keeps Founders/Exec fit.** The closeout task scored 3 on Business Function for bookkeeping, so the framing matters. The deliverable is a founder's read on three strategic bets: what each took to build, what it earned, and what the angels should hear, used by Leonard in his calls. The payee list is working, not the point. Robert is the right person because he approved these payments, paid one contractor himself, and knows which outside people worked on what. If `/prompt` still scores Business Function 3, the fix is a stronger judgment ask in the hub, not more figures.

**Scope that keeps it clean.** Build cost only: the team on Deel plus studios and freelancers.
- UA and ad creative stay out, so the warehouse-versus-Meta-receipts split never matters (receipts say ZM $9,920, the warehouse $1,937).
- Legal, tools and the website go to a company line.
- Founders' pay is out: it runs through Gusto and is not in the notices.
- Revenue per game comes from `REVENUE_DAILY`, lifetime: Domino Delights $12,331.25, Zombie Match $11.99, Combo Fighter $11.75 (I re-summed it).

**Sketch truth** (`svb_processed_robert.json`, UNCALIBRATED until the method is final). Dates are the notice's Transaction Date. ZM starts Jan 9, 2025, Combo Fighter Nov 24, 2025.

| Bet | Plain sum of notices by date | Correct build cost in the sketch |
|---|---|---|
| Domino Delights | $984,888.21 | $960,842.64 |
| Zombie Match | $608,820.50 | $544,433.44 |
| Combo Fighter | $73,685.61 | $72,685.61 |

The notices total $1,667,394.32 in USD plus 1,999 BGN. Deel is $1,015,347.19 across two spellings of one account.

## 4. UGT plan (rule 1)

1. **One closed method record.** A seeded record in Leonard's voice, delegated to by his ask. It sets:
   - the source of record (the bank's notices, because the books have no vendor names);
   - what counts (money that left and stayed out);
   - which off-bank contractor payments count;
   - the three buckets;
   - the bet calendar with exact dates;
   - the "tied to one game" exception;
   - the revenue source;
   - the follow-through on the payee issues.

   It holds no item-level resolver. Every sentence is applied to all 22 payees before SQL (learnings §21, §63).
2. **Completeness rests on a census.** All 24 notice spellings collapse to 22 real payees, each with a proof record (census D). The notices are scanned in full, and I parsed all 132 myself.
3. **Forks to settle before `/prompt`:**

   | Fork | Settled by |
   |---|---|
   | Is a Processed notice money gone? | The method's "stayed out" clause, plus the base Apr 2024 note |
   | Does $33,290 count (Awaiting, no Processed anywhere; Arthur "Done!")? | NEW Leapblock statement. Without it the amount can't be closed |
   | Which off-bank payments count | A closed rule covering contractors paid another way. Must census Western Union and any similar route first |
   | Western Union $0.99 fees | The method counts what the payee received |
   | Date used, and arrears (Leapblock pays a month late) | Transaction Date, stated. No work-month reading |
   | Combo Fighter start: Nov 12 kick-off or Nov 24 | The method states the date. No build payment falls between them, so neither changes a figure |
   | Deel allocation by game (no record exists) | By date, as the founders' stated rule. This is a stated boundary, not a finding |
   | Build vs ad creative: Node Media, Creative X, Oleg | One bucket sentence on work made to buy installs |
   | Lauren Brooks / Telegram | The exception sentence, plus records tying the contract to the Domino Delights port |
   | JPMorgan $4,000 (holder unknown in base) | NEW Arthur note. Without it this is `SILENCE` |
   | Martin 1,999 BGN | A company line. The USD value must be settled: the P&L equipment row ends 1,209.89, but the month match is inferred, so seed or restate it |
   | $500 helper (identity only in a Leonard DM) | NEW note on its issue; a company line |
   | TYZ $7,500 wire vs $12,240 bill | Legal stays at the bank amount on the company line, so the retainer question feeds no figure |
   | Deel 2024-09-27 back pay, BANCO Oct 2024 for August | By-date rule makes both moot |
4. **Keep off the graded path:** NB-2 (P&L cost lines), NB-3, NB-4, NB-5, NB-8, NB-10, NB-15, NB-17 to NB-20, NB-22, NB-23, NB-26, NB-29, NB-33; the `FINANCE_LEDGER` art and operations lines; Dec 31 and Jan 31 cash; Meta receipt splits; Unity Ads dollars.
5. **Tokens (NB-12).** Deel and Singular resolve by account suffix and a spelled Recipient or Scheduled notice. Node Media resolves by the exact amounts in its own mail. A seed spells the name wherever only a token exists.
6. **Two blind sweeps before `/injection`** by fresh `hg.py`-only agents: a fork sweep, then a seeded-versus-base coherence sweep across all mailboxes. Cold reviewers are the bar.

## 5. Hardness plan (rule 4, Hardness v2)

Seven channels. Six are cross-source decisions; each has a named wrong source and the record that beats it, and each moves at least two rows including a weight-5 row. `NEW` marks a planned seed not yet checked against the universe; everything else is base.

| Channel | v2 trap | Convincing wrong source | Record that beats it (who, when, authority) | Rows it moves | Placement | Prior |
|---|---|---|---|---|---|---|
| RET | 1 · proving done (A24) | SVB "Payment Processed", $4,032 to ***8605, Apr 3, 2024 (`threads/00004088.json`) | Leonard, who keeps the books, Apr 12, 2024: wrong account, "bank returned our money" (`C04UEQVDVB7/1712901800.684259`). Recipient Modified Apr 5 (`00004120`); re-sent (`00004124`) | MotMot net, comment, DD total, reply | Founder channel, two years back; the note names neither BANCO nor MotMot | 0.45 |
| OFF | 7 · outside the filter (A17) | Notices show Lucas at $6,450 | Five Western Union receipts, $7,525, in Robert's mailbox (`00005184`, `00005350`, `00005489`, `00005962`, `00006329`), tied by Robert's own "via company card" note | Lucas total, comment, DD total | Mail no notice search returns | 0.50 |
| ORPH | 7 · outside the filter (A13) | No Processed notice, so $33,290 never left; Leapblock is $374,654 | NEW Leapblock's closing statement in `#leapblock`, from the payee, Feb 13; agrees with Arthur's "Done!" (`C04UEQVDVB7/1694616951.239909`) | Leapblock total, comment, DD total, reply | `#leapblock`, Feb | 0.40 |
| CORR | 2 · correction elsewhere (A11) | The $4,000 wire of Aug 19, 2024 reads as a cost; its issue says so | NEW Arthur, who created that recipient and ran the wire: it topped up the company's Chase account for Carta. Mail to the founders | JPMorgan row, comment, DD total, company line | Mail, off the issue | 0.45 |
| ALIAS | 6 · different names (A7) | "BANCO DE AMERICA" and a token LLC tell you nothing about the payee | Arthur Jan 2025 ties MotMot to the $4,032 (`C04UEQVDVB7/1736978214.260099`); Node Media's own mail gives the amounts behind $16,428.57 (`00008689`), so that spend is UA, not build | Node row, Creative X row, MotMot name, DD and ZM totals | Slack and mail, by amount | 0.40 |
| OVR | 5 · hidden exception (A15) | The date puts the Telegram contractor's $1,500 in ZM and Combo Fighter | The method's exception, plus `#executives` Oct 2025 and `#telegram-dd`: the Domino Delights port | Brooks row, ZM and CF totals | Slack, Oct 2025 | 0.45 |
| CURR | 8 · wrong input (A10) | Notice read as $1,999 of build cost | The notice's own "BGN"; `#admin_foundersonly` Oct 2025 says laptop | Laptop row, company line, ZM total | Visible in the notice | 0.25 |

**Follow-through (trap 3).** A rule on the payee project asks for a reason on any issue whose figure differs from the bank's sum. Those comment rows sit inside RET, OFF, ORPH and CORR, so each trap moves more than one row without repeating a fact.

**Controls and decoys.**
- Same-amount pairs that are genuinely two payments: Leapblock $3,700 on Aug 1 and Aug 29, 2025; BANCO $2,688 on Jul 19 and Jul 29, 2024.
- Eveline's +$160 retro payment, and the Leapblock $300 book entry.
- 18 Awaiting rows that only look unmatched because the bank spelled the name differently.
- Leonard's working sheet of plain bank sums, as an A1 wrong summary.

**Independence.**
- Root causes are distinct: A24, A17, A13, A11, A7, A15, A10.
- Largest unit of discovery: ALIAS, 19.4 % of the weight.
- The three bet totals are the only rows several channels share, so the per-payee rows carry the spread.
- No correction sits in the hub, an anchor, or a superseded record's container.

**Survives complete retrieval.** RET needs a two-year-old note connected to a wire it doesn't name. CORR, ALIAS and OVR need a rule applied after the record is found. OFF and ORPH are retrieval-shaped, which is why their priors depend on placement.

### Part 7 checks: `hardness_v2_check.py --design` on the sketch

Output, verbatim (`hardness_v2_check_output.txt`):

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      3 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 7 requirements: {'R2': ['RET'], 'R3': ['OFF'], 'R3b': ['ORPH'], 'R4': ['CORR'], 'R3c': ['ALIAS'], 'R5': ['OVR'], 'R6': ['CURR']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   7 of 7 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     3 weight-5 total(s); 3 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  SKIP       RULE_IN_PROMPT  no prompt (04_Prompt.txt) yet  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

**How far CLEAN goes.**
- SAME_PLACE covers only the three traps with two declared version records (RET, ORPH, CORR). OFF, ALIAS, OVR and CURR declare none.
- CURR passes DECISION_FLIP only through the Zombie Match total; its own rows are weight 3. It is a complexity channel, not one of the counted v2 decisions.
- The check re-runs on the real manifest and on the SQL. RULE_IN_PROMPT runs once a prompt exists.

## 6. Spread and score plan (rule 5, UNCALIBRATED)

`policy_model.py` scores the sketch surface: 38 slots, weight 108, 66.7 % flippable, nine weight-5 slots. It uses a run-level thoroughness latent and 3 % base slips.

| Whole policy | Score |
|---|---|
| Perfect | 100 % |
| Adds up the Processed notices by date, reads nothing else | 33.3 % |
| Notices, the method and the payee project; no older Slack, no other mail | 36.1 % |
| Thorough except mail beyond the notices | 63.0 % |
| Thorough except older founder-channel history | 71.3 % |
| Thorough except `#leapblock` | 85.2 % |
| Thorough, lets the payment date decide every game | 86.1 % |

| Single miss | RET | OFF | ORPH | CORR | ALIAS | OVR | CURR |
|---|---|---|---|---|---|---|---|
| Score | 85.2 % | 88.0 % | 85.2 % | 85.2 % | 80.6 % | 86.1 % | 89.8 % |

Every single miss takes a run under the 90 % cap. The highest pair of misses scores 80.6 %. P(one run catches everything) ≈ 0.02, so E[full passes of 6] ≈ 0.13.

Six-run Monte Carlo at design landing rates (mean 0.41, 2.9 traps per run):

| Landing scale × rho | E[avg] | P(< 90 %) | P(SD in band) | P(all gates) |
|---|---|---|---|---|
| 1.00 × 0.30 | 66.4 % | 1.00 | 0.91 | 0.91 |
| 0.70 × 0.35 | 75.4 % | 0.98 | 0.92 | 0.91 |
| 0.50 × 0.35 | 81.6 % | 0.89 | 0.85 | 0.80 |
| 0.40 × 0.35 | 84.8 % | 0.78 | 0.77 | 0.69 |
| 0.30 × 0.35 | 88.1 % | 0.60 | 0.65 | 0.52 |
| 0.25 × 0.35 | 89.8 % | 0.48 | 0.56 | 0.41 |

**Against your targets.** E[avg] ≤ 82 % holds down to a 0.5 scale. P(all gates) ≥ 0.5 holds down to a 0.30 scale.

**Row dilution** (`policy_sensitivity.py`), because the platform has required a row per write:

| Rubric shape | Weight | At scale 1.0: E[avg] / P(all) | At 0.5: E[avg] / P(all) | At 0.3: P(all) |
|---|---|---|---|---|
| Closes sampled (5 + volume) | 108 | 66.6 % / 0.93 | 81.6 % / 0.80 | 0.52 |
| One row per close | 124 | 70.6 % / 0.88 | 83.6 % / 0.71 | 0.41 |
| One row per close and per comment on every issue | 146 | 74.5 % / 0.78 | 85.6 % / 0.57 | 0.28 |

With one row per close, the ≤ 82 % target needs a scale of about 0.56 (interpolated, not a model run).

**The honest read.**
- Comparable tasks landed about 0.5 per trap: Robert's wind-down 2.67 of 5, the LLC baselines, Frederick's bridge. That sits above my design mean of 0.41, so the central case is comfortable on the average.
- Proxies have flattered both numbers. The LLC proxy said 67–72 % and SD 0.17; the real result was 83.6 % and SD 0.103. Carrying that gap over gives about 78–83 % here, still under the cap, with **SD near the 0.1 floor**. Treat P(SD) above as optimistic.
- Hedges for `/create-scenario`: keep per-target rows to a minimum, keep every trap at two or more rows, keep catch rates near 50 % on different habits, and read the pre-check against these priors.
- **All-fail watch.** The DD total passes only when none of RET, OFF, ORPH, CORR and ALIAS lands, so it is close to an all-fail row. That is legal with a justification but adds no spread. Keep the near-certain aggregates to three.
- Ledger priors are thin: every Opus 5.5 family here has `n_eff` 1 (mean 0.33). The S9b pre-registered forecast replaces this sketch.

## 7. Volume plan

`volume_model.py`, from measured Opus 5.5 habits on Robert's two Feb 14 tasks (UNCALIBRATED). `gmail_get_messages_batch` takes up to 100 ids, so the 132 notices buy few calls. The per-record work has to come from somewhere else.

| Phase | Services | Calls per run |
|---|---|---|
| Ask, `#winddown` pages, founder channels, `#leapblock`, name searches | slack | 14–26 |
| Notice search pages and batches | gmail | 5–12 |
| Per-payee lookups: receipts, invoices, agency mail, Chase | gmail | 10–28 |
| Method doc, MSA and agreements, Drive listing | gdocs, gdrive | 6–14 |
| P&L costs tab | gsheets | 2–6 |
| Revenue | snowflake | 3–8 |
| Payee project meta | linear | 2–4 |
| **Per payee (22–24): read comments, close the issue** | linear | **~35–48** |
| Reason comments on exception payees | linear | 1–6 |
| Contacts, calendar, Trello | mixed | 1–6 |
| Sheet create, move, shares, values, read-back, reply | gsheets, gdrive, slack | 5–9 |
| **Modelled total** | 10+ services | **mean 125, p5 110, p95 139**; P(run < 100) 0.001; median six-run minimum 114 |

Without the issue closes the mean drops to 105 and P(run < 100) rises to 0.26, so the closes matter.

**No padding.** Each issue is one real payee. Each comment read answers that payee's own question with no bulk alternative (`linear_list_comments` is per issue). Each close is a write the hub asks for.

**The ≥ 500 floor is not reachable honestly.** There are 22 payees. The 132 payments collapse in two batch calls. Reaching 500 would need padding, which fails on its own. A volume exception and a cohort exception are needed (§10).

**Floors the exceptions don't lower:**

| Target | Plan | Status |
|---|---|---|
| ≥ 10 injected schemas, no Confluence or Snowflake | slack, gmail, gcal, linear, gdocs, gdrive, gsheets, gslides, contacts, trello | Reachable but tight: every schema needs a real job |
| ≥ 10 services carrying weight | The above minus any that carry no fact, plus snowflake | Tight |
| ≥ 120 INSERTs | About 22 issues, 35–45 comments, lifecycle rows, Slack, mail, calendar copies, docs | Reachable |
| ≥ 12 fragments, ≥ 7 services, ≥ 10 containers | Ask, method, project, issues, statement, Arthur's mail, notes | Reachable; fragments over 7 services is tight |
| 2–4 authorities, ≥ 3 chains, ≥ 12 traps in ≥ 7 families, ≥ 4 supersessions, ≥ 6 distractors | Seven channels plus the controls in §5 | Reachable; supersessions need care |

## 8. Injection plan (rule 3)

- **Census every seeded entity** across all mailboxes and channels: Leapblock, Chase, Carta, MotMot, Node Media, Lucas, Lauren Brooks, the Telegram port, and the rest. Read every hit; give every absence check a positive control (learnings §10, §35).
- **Date each seed after what it relies on**, and Slack before Feb 13 10:03 UTC:
  - the ask after `C0ADGSZKR3R/1770934638.035469`;
  - the project after "linear we keep during transition" (`/1770933601.686309`);
  - Arthur's Chase note after the Chase closure and Carta records;
  - the Leapblock statement after the Feb 12 `#leapblock` exchange.
- **Leapblock statement check.** Every line must match the 29 wires, the Sep 2023 invoices and the January waived animator invoice. No figure may conflict with `#leapblock` history.
- **Carriers.** No fact only on Confluence, in a GCal description or in an attachment. Snowflake stays base-only.
- **Companions.** Linear project, issue and comment stamps; GCal copies per attendee; Drive rows for injected Docs and Sheets; no activity on closed records.
- **Theme.** Seeded text says "ZM" and keeps zombie and outbreak words out. A prior check of 12 stored ZM baselines found no refusal fallbacks; read the pre-check for fallback events.
- **Confirm in the pre-check** that the agent's tools return every seed and all 132 notices.

## 9. Writes (rule 6)

| Write | Authorized trigger | Access proof |
|---|---|---|
| New sheet in Robert's Drive | Leonard's ask | Robert owns the new file; `gsheets_create_spreadsheet` then a move into his root, never a Resource folder. Worked in both Robert tasks |
| Share with Leonard and Arthur | Leonard's ask | `gdrive_share_file` proven 6/6 as Robert |
| Close each payee issue | The project's rule | `linear_update_issue` proven as Robert |
| Reason comment on each differing payee | The project's rule | `linear_create_comment` proven 6/6 |
| Reply to Leonard in his thread | Leonard's ask | `C0ADGSZKR3R` YES; `slack_send_message` proven 6/6 |

No Trello writes: Robert has none on record. Every graded write stays tied to Leonard's ask or the project rule, so prompt, method and rows trace to the same incorporated facts (rule 7).

## 10. Your decisions

1. **Storyline.** I recommend **A**. B and C fail on reach and on known data issues.
2. **Volume exception (GEN §3a).** Needed. Proposed `volume_exception {call_budget_floor: 120, per_record_floor: 40}`. Reason: 22 real payees, and the 132 notices collapse in batch reads, so about 125 honest calls per run; 500 would need padding. It needs your confirmation.
3. **Cohort exception (GEN §3a).** Also needed, and not in your list. No honest ≥ 40-record cohort has three no-bulk surfaces. Proposed `cohort_exception {cohort_floor: 22}` on the payees. It needs your confirmation.
4. **Review waiver.** `REDTEAM_*` is unset, so the dual red team can't run. Either set it before `/create-scenario`, or confirm a `RED TEAM FALLBACK:` using the two blind sweeps in §4 plus the census and models. It stays in every Unresolved line until something covers it (learnings §44).
5. **130+ calls per run.** Your goal says ≥ 100, which the model meets. An earlier standing target was 130+ in every run, which this design does not meet (P(run ≤ 130) = 0.73). A comment on every issue would add about 22 calls but cost spread (last row of the dilution table). I recommend staying at ≥ 100 unless you say otherwise.

**Next step:** once you've decided, run `/create-scenario`. It will turn this sketch into the draft manifest, the gradable surface and the design dossier, then run the blind sweeps before any SQL.

## Notes on the census work

- The four census agents read Leonard's and Arthur's mail through `hg.py`, which is evaluator-wide. That is right for contradiction checks. Those records are marked and are never used as Robert-reachable evidence.
- Two agents wrote helper files in the scratchpad beyond their brief, then deleted them; one had dumped an 82 MB mail copy there. One stuck Snowflake job was stopped. Nothing was written to the universe, Evals or tools.
- Census C reports two Atlas slips to carry forward (unverified by me): the HG Costs "Sep–Dec 2025" values are 2026 forecast columns, and Census B says `/contacts/160` is Brian Foster, with Matthew Collins at `/contacts/159`.
- `threads/0*.json` is not all Robert's: low-numbered files belong to other mailboxes, so check the id prefix.
