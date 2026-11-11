# 01a Hardening Report: Robert seed bets (task_inputsS2)

## 1. Mode, inputs and run validity

**MODE B (pre-check intake).** One Opus 5.5 run, SQL rev6, prompt sha `d0cb08476d23`, assessed 2026-11-08.

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal). Universe manifest: `Evals/references/universes/normal/universe_manifest.json`.

Assignment: Robert, Co-founder & Creative Director; Executive; Finance; Analysis and synthesis; Long Horizon; Easy.

**Inputs read:** `00_Assigments.md`, `01_Universe_Inject.sql` (rev6), `01_Grounding_Dossier.md`, `01_Hardness_Manifest.json`, `01_Gradable_Surface.json`, `03_Error_Async_Config.txt` (Friction: none), `04_Prompt.txt`, `06_PreCheck_Trajectory/trajectory.json`, `solver/truth.json`, and the platform reports in `plateform_reports/`.
**Not present (expected before the baseline):** `07_Baseline_Trajectories` runs, `08_Oracle_Events.md`, `09_Rubrics.json`, `10_Baseline_Verifier_Results.md`, `12_Difficulty_Stats.txt`. No prior hardening report exists.

| Intake result | Finding | Pointer |
|---|---|---|
| Binding | BOUND to rev6 by discriminating content | `run_forensics/rev6/summary.json` |
| SQL identity | Platform hash `a52191c3` is local `ad50f039` with the first six header lines removed | `tail -n +7` of the SQL |
| Export identity | sha256 `fc4e4ed2…`, the same export the platform /hardness report reviewed | `plateform_reports/…_1a_hardness (1).md` §1 |
| Model | Every message `claude-opus-5-5`; no fallback; no subagents; `v3_valid` true | `summary.json` provenance |
| Completeness | Final `result` at event 535; no compaction; nothing after the result | `summary.json` validity |
| Source | Platform pre-check (attempt 6aeed82596dcfe103f9f74d9), harness claude-code 2.1.280 | export init event |
| Counted calls | 133 (156 raw, less 16 Bash and 7 blocked) | `summary.json` counts |
| Proposals and dispositions | 7 proposed, 7 overruled by hand; all 7 tool verdicts were BYPASSED, caused by a register join failure on labelled payee rows. A normalized replay corroborates the hand verdicts | `precheck.proposals.jsonl`, `precheck.dispositioned.jsonl`, `replay_normalized/` |
| Review coverage | All 156 calls read; review queue events [463] reviewed; limits in section 5 | `review/calls_part1.md`, `review/calls_part2.md` |
| Deliverable diff | One wrong figure: MotMot DD 32,160 against 28,128, which carries into the DD total and reply | `review/surface_adjudication.md` |
| Ledger | `hev_efbca5607a047ac2`, `hev_e65926c500198d3c`, `hev_33741eaee49bfa4a`, `hev_138abfcae201ca13`, `hev_9a41d9388bc84c5b`, `hev_5500eb7aeca7ff2a`, `hev_6d4d83dd1e3c4878` | `support/hardness_ledger/ledger.jsonl` |
| Control and channel records | 14 records in the ledger: 7 controls HELD; CH-RET FAILED, the other 6 channels HELD | `precheck.controls_channels.jsonl` |
| Posterior forecast | `hev_643bd103399a65fc`: E[avg] about 0.89, P(all gates) 0.002 to 0.163, UNCALIBRATED. The tool labelled the record `rev1`; its SQL sha is rev6 | `precheck.posterior_forecast.json` |
| Structured diagnosis | `mode_b_report` PASS, `PROVISIONAL_SINGLE_PRECHECK` | `Working_Files/Mode_B_Diagnosis.json` |

**Go / no-go: NO-GO for the six-run baseline (advisory, UNCALIBRATED).**

| Go rule | Needed | This run | Result |
|---|---|---|---|
| /hardness | 3 or more | 1 of record (platform); 2 on a corrected reading | Not met |
| Corrected proxy | At most cap − 5 = 85% | 82.42% | Met |
| Independent loss channels in Opus's own decisions | At least 2 | 1 (RET) | Not met |
| Run valid | Yes | Yes | Met |
| Posterior P(all gates) | At least 0.8 | 0.002 to 0.163 | Not met |

This is the first platform pre-check on this scenario (the stop rule allows two).

## 2. Gate status and fit with the assignment and goal

Baseline gates do not apply yet: there is one run and no verifier. Mechanism weight share: 16 of 91 (17.6%) depends on the one designed failure that bit.

| Bar | Source | Status | Evidence |
|---|---|---|---|
| Role, function, competency, skill | Assignment | Fits: /prompt 5 on Business Function, Competency and Task Skill | `…_1_prompt-1.md` lines 74-78 |
| /injection and /prompt | Goal | PASS and 5 on rev6 | `…_0_injection-1.md`, `…_1_prompt-1.md` |
| /hardness 3 or more | Goal | **Band 1, HOLD** | `…_1a_hardness (1).md` |
| At least 3 independent loss channels | Goal rule 4 | **1 observed** | section 4 |
| Two cross-source decisions on distinct named trap types | Goal rule 4 | **1 observed** (RET) | section 4 |
| Corrected average under 90% | Assignment | One run at 82.42%, conditional on the MotMot row being graded | section 7 |
| User target under 80%, ideally under 70% | Standing target | Not shown: the one run is 82.42% | section 7 |
| At least 100 calls; user target 130+ | Assignment and standing target | 133 counted, a margin of 3 | section 6 |
| Human time about 12 to 24 hours | V3 | 14.25 hours | `05_Human_Time.md` |
| Spread and failure patterns | Six-run gates | Not measurable from one run | n/a |

## 3. Predicted /hardness band

**Of record: band 1, FAIL, HOLD** (`…_1a_hardness (1).md`, Clock line as above). **Corrected reading: band 2, neighbour 3.**

The platform's requirement map is sound except R11. It expected DD 963,374.64, while the records give 959,342.64.

| Requirement | Result | Pointer |
|---|---|---|
| Processed notices, windows, merged spellings (platform R1-R3) | MET | events 151, 159, 434 |
| Close-out, own-account transfer, Oleg, receipts (R4-R7) | MET | events 244, 387, 76, 321 |
| Buckets, currency, 22 lines (R8-R10) | MET | event 463 |
| Money that came back, applied to MotMot | **MATERIAL_FAIL** | event 463: 32,160 and "none reported back" |
| Cost per bet (R11) | **MATERIAL_FAIL**, cascade of the row above | events 463, 532: $963,374.64 |
| Revenue, layout, delivery, Linear follow-through, reply (R12-R16) | MET, except the DD figure and deck line in the reply, same cascade | events 463-532 |

One root cause, with no CONFOUNDED failure in the map.

**Why not 3.** It is one bounded correction: $4,032 on one row. The platform report applies a narrow-miss rule (one cause under Easy's 10% loss). That rule is not in the local bundle, so it could not be checked. On rows, the cause is 17.6% of the surface, above that line. On dollars, it is 0.4% of DD cost.
**Why not 1.** A real, fair failure occurred. The platform reviewer checked Gmail and Linear for returns and did not open the founders' channel (its section 5).

## 4. Designed-difficulty register

| Node (trap) | Verdict | Count of 1 | Run evidence | v2 kind |
|---|---|---|---|---|
| RET (T1, T10) MotMot return | LANDED | 1 | opus · event 463 wrote 32,160; opus · event 205 searched Gmail only | off-path correction |
| OFF (T2) Lucas, Western Union | LEAKED | 1 | opus · event 321 read receipts; hunt at event 177 missed | bulk call carried it |
| ORPH (T3) Leapblock wire | LEAKED | 1 | opus · event 244 returned the close-out post | on_delegation_path |
| CORR (T4) JPMorgan $4,000 | LEAKED | 1 | opus · event 387 read Arthur's mail after about 8 misses | volume, then token join |
| ALIAS (T5) Node Media | LEAKED | 1 | opus · event 400 returned the name from a note's word | first_read |
| CLASS (T6) Lauren Brooks | FALSE | 1 | opus · event 68 returned the conclusion in the note | same_container |
| CURR (T7) Martin BGN | FALSE | 1 | opus · event 159 parsed the currency after reading the rule | first_read, bulk field |
| T8 quick numbers | FALSE | 1 | opus · event 435 used them as a free checksum | first_read |
| T9 Trello plan | FALSE | 1 | opus · event 18 doc retires it; no Trello call in the run | never on path |
| T11 two $3,700 wires (RET control) | LEAKED | 1 | opus · event 256 year totals confirm both | bulk call, no pull |
| T12 Awaiting / Scheduled | FALSE | 1 | opus · event 89 query excludes them | never on path |
| T13 card-paid animator | FALSE | 1 | opus · event 463 no such payment; the DM was never returned | never on path |
| T14 4X helper | FALSE | 1 | opus · event 74 note states it | same_container |
| T15 P&L note | FALSE | 1 | opus · event 247 file seen, not opened | never on path |
| T16 Deel spellings | FALSE | 1 | opus · event 34 note states it | same_container |
| T17 store transactions | FALSE | 1 | opus · event 18 doc names the revenue table | first_read |

Reach nodes the run never read: `C04UEQVDVB7/1712901800.684259`, `f_20a0df3860bb5731d22f07`, `698e55f9af74d68d679de7b3`, `564155d70112411151e512a6`.

Controls and channels are in the next section.

## 4a. Controls and channels

These were read from a normalized replay of the run (`run_forensics/rev6/replay_normalized/README.md`) and checked against the event 463 write. The replay joins labelled payee rows to the surface keys and compares amounts as numbers; it changes nothing else. On that replay the tool itself gives RET a landing on MotMot, CH-RET failed and a go-rule count of 1, which matches the hand verdicts. The tool calls CLASS and CURR leaks; the hand verdict is FALSE because the correction was met before any claim.

| Rule | Control member | Outcome | Evidence |
|---|---|---|---|
| RET | Leapblock (two $3,700 wires kept) | HELD | event 463; event 256 year totals |
| OFF | Graham Porter (no card-paid animator added) | HELD | event 463 |
| ORPH | Eveline Art (no Awaiting notices added) | HELD | event 463, 93,171.50 |
| CORR | Singular (no other one-off dropped) | HELD | event 463, 31,250 Company |
| ALIAS | Adjoe, Leapblock (bucket unchanged) | HELD | event 463 |
| CLASS | Graham Porter (stays Build) | HELD | event 463 |
| CURR | Lauren Brooks (dollars stay dollars) | HELD | event 463 |

No over-application occurred. Control records never enter the priors.

| Channel | Member | Outcome | Deciding event |
|---|---|---|---|
| CH-RET | MotMot | **FAILED** | 463 |
| CH-OFF | Lucas | HELD | 463 |
| CH-ORPH | Leapblock | HELD | 463 |
| CH-CORR | JPMorgan | HELD | 463 |
| CH-ALIAS | Node Media | HELD | 463 |
| CH-CLASS | Lauren Brooks | HELD | 463 |
| CH-CURR | Martin Walsh | HELD | 463 |

The replay's `slip` items on Company payees are representation only: truth keeps a by-bet allocation for them, and the run correctly used the Company column.

## 5. Per-rollout ledgers

Full call tables are in `run_forensics/rev6/review/calls_part1.md` (events 2-245, 80 rows) and `calls_part2.md` (events 246-535, 76 rows). Decoded writes are in `run_forensics/rev6/precheck/writes.json`.

- **Discovery.** #winddown (event 2), profile, method doc (17), sheet and deck (19-25), 22 issues and every comment list (27-75), then the 132 notices (79-158).
- **Close-out and receipts.** Gmail sweeps (177-238). The first Slack search, at event 243, found the Leapblock post.
- **Founders' channel.** Read at events 348, 357 and 370, for Aug 2024 only.
- **Where it committed.** Event 151 fixed the population at 132 Processed notices. Event 333 printed the April BANCO pair and nothing later touched it.
- **Writes.** Sheet (463), two shares, four comments (473-479), 22 Done updates (483-525), reply (532). Comment-before-Done holds. ENG-2442 went Done at event 491 with no comment.

**Not fully read:** 16 spilled payloads are stubs in the export, so the raw notice bodies are visible only through the run's own extraction at event 158. Six id-only Gmail searches were aggregated by sender domain. Long Slack pastes were grepped in full and read in part. Thinking blocks are empty, so motives are inferred from calls.

## 6. Friction, tool-defect and horizon checks

- **Friction:** none configured; none expected.
- **Unconfigured defects, no outcome changed:** six `format=full` batch errors (events 103-113, a documented 10-id limit, recovered with smaller batches); one ECONNRESET at event 384, retried at 386; `jq` missing at event 6 (environment).
- **Horizon:** 133 counted calls, Long Horizon floor 100. The margin against the user's 130+ target is 3. The platform counted 156 raw.

## 7. Verifier sanity

No verifier or rubric exists yet. Two grader problems matter.

**Proxy decoders.** `surface_grader` reported 38.46%. By hand the score is **75/91 = 82.42%** (79.12% if R2 must carry all three cost figures). The failed slots are X1, B1, C1 and R1, one root cause. There were 16 disagreements:
- labelled payee rows never join the surface keys (X3, X5, X6, X8, X9, S1, S4, S5);
- commas drop labels (X1, X4, S2, S3, S6);
- total rows count as payees (S6);
- an explicit parent is required although `gsheets_create_spreadsheet` cannot take one (D1);
- C1 falsely passed on Oleg's comment.

Surface defects are in section 11.

The normalized replay scores 82.4% through the unmodified grader, failing X1, B1, R1 and the pinned D1, D2, D4, and still false-passing C1.

**New-release FAIL classes (B3f).**

| Class | Finding | Pointer |
|---|---|---|
| `overly_broad` | Risk on the surface only: R2 accepts any "deck", C1-C4 accept matching words on any issue. Fix at the rubric stage | `review/surface_adjudication.md` section 5 |
| Idle agent passes a row | None: an empty run scores 0/91. X5 accepts a blank bucket only on a row that is written | `review/surface_adjudication.md` section 5 |
| Prompt Contrived | None. No staged typos, trap hints, hidden destination, audit wording or if-chains; /prompt scored 5 | `…_1_prompt-1.md` |
| False premise for this universe | None raised on rev6: seeded activity by Leonard and Arthur on Feb 12-13 passed /injection and /prompt | `…_0_injection-1.md` |
| Trash, attachment-only or unlinked evidence | Not relied on: RET's deciding records are Slack message text; the images in that thread are not needed | `review/ret_motmot.md` section A |
| Stale reviews | No OE or rubric exists yet. Any rev7 SQL change means a FULL /prompt re-review | GEN_EXECUTION §3 re-run matrix |

**Platform reviewer.** It accepted $963,374.64. If that total were right the run would score 91/91. Every other figure agrees with ours, and the deciding records are `C04UEQVDVB7/1712331718.859679` and `C04UEQVDVB7/1712901800.684259`. Details are in `review/ret_motmot.md`. Its band therefore understates this run, but it does not change the conclusion: one landing is not enough.

## 8. Why Opus passed

Three causes, all confirming the platform's advice with one correction.

1. **Conclusions sit in the notes.** ENG-2455: "her contract had her running our paid UA on telegram, so she's marketing, not build" (`comment_990674712ad0127e26f780eadb5418ea`). ENG-2458: "not one of the three games". ENG-2459: "that wire came back the same day".
2. **Rule sentences match the deciding record one to one.** "If someone we paid closes out their file with us and tells us what they received, that beats the notices for them." pairs with `C05URGU759U/1770971846.479179`, which is also dated the day before the clock and states the missing wire.
3. **A self-reconciling total.** Leonard's quick numbers gave the run a free checksum of its parse (event 435), and the close-out's year split gave another (events 255-256).

Heavy rows that passed: X3, X4, X5, X6, X8, B2, B3. B2 and B3 have only CLASS on them, so ZM and Combo Fighter totals were effectively free.

| Passed slots | Why it passed | Class |
|---|---|---|
| X3, C2 | Rule read first; a date window for another trap found the first receipt | Universe leak, partly capability |
| X4, C3 | Rule names the situation; the close-out post gives the answer | Universe leak |
| X5, C4 | About 15 calls of persistence, then a token join | Genuine capability |
| X6 | Note supplied the search word and window | Universe leak |
| X8, B2, B3, S6 | Conclusion stated in the ENG-2455 note | Universe leak |
| X9 | Currency rule read before the parser was written | Universe leak |
| B4, V1, V2, S1-S5 | Clean sums over bulk reads | Genuine capability; Opus finds this easy |
| R2, D1-D4 | Routine delivery | Genuine capability |

No pass is attributed to a prompt leak.

`hardness_v2_check` on rev6 (advisory; these checks read CLEAN on a band 1 run):

```text
FLAG       SAME_PLACE      5 trap(s) with two or more version records; 1 flagged, 0 unresolved
CLEAN      DONE_CHECK      an A24 / done_gap node exists
CLEAN      TWO_DECISIONS   cross-source rules decide 5 requirements
CLEAN      DECISION_FLIP   7 of 7 rules can flip a weight-5 slot
CLEAN      INPUT_CHECK     0 weight-5 total(s); 0 with an input a rule can change
CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter
CLEAN      RULE_IN_PROMPT  no run of 8 resolver words in the prompt
SAME_PLACE T9 (on_delegation_path): the correction sits in file:f_6feda53b2382c63bf47b25
```

## 9. Purge list (proposed; S0r decides)

- **Do not count as difficulty:** CLASS, CURR, T8, T9, T12, T13, T14, T15, T16, T17. They added no failure pressure in this run.
- **Keep as correctness rows,** since removing them risks forks or breaks the design's incorporation links (for example the doc's reference to the board plan): CURR, T9, T16.
- **T13** was never reachable from any natural query; it can go if the distractor count allows.

## 10. Proposed rebuilds (candidates for S0r)

Lessons applied (`review/lessons.md`): in every past task where /hardness rose from band 1-2 to 3+, a deciding fact moved off the swept path, usually with a byte-identical prompt. Readable rule layers did not move the band. Spread comes from heavy traps caught by a third to two thirds of runs. Every proposal was attacked against the records (`review/repairs_redteam.md`). None adds a payee, issue, step or write.

| Rank | Move | v2 type | Change | Facts it changes | Slots |
|---|---|---|---|---|---|
| 1 | **P-CORR** | Correction elsewhere with a convincing wrong source | ENG-2450 note gives a hedged wrong recollection that puts the money in Build; Arthur's later "Chase records" mail still beats it | One Linear comment | X5, B1, R1, C4 |
| 2 | **P-OFF** | Item outside the obvious filter | Remove "the bank has him from Sep 2024" from ENG-2447; test fairness first | One Linear comment | X3, B1, R1, C2 |
| 3 | **P-RET** | Reviewer visibility, not hardening | One top-level founder message in `C04UEQVDVB7`, 2026-02-13 00:05Z to 09:00Z | One Slack row (rows +1) | X1, B1, R1, C1 |
| 4 | **P-ALIAS** | Lower cost | Take the search key out of the ENG-2444 note; not a loss channel | One Linear comment | X6, B1, R1 |

**Dropped after review.**
- *Delete the ENG-2455 conclusion:* a direct regression of the rev4 /prompt FAIL. Exhibit A lists five services, and "advise on what growth features to implement" leaves a Build argument.
- *Strip the Leapblock year split:* inert, because a run that puts the gap under DD passes by default.
- *Cut the doc rule sentences:* blind reviewers forced those to close forks.

**Open need for S0r.** With CLASS unchanged, ZM and Combo Fighter have no live trap, so B2 and B3 (10 of 91) stay free, and all three channels share the DD headline (B1, R1). RET and CORR are the same named type, so two distinct types needs P-OFF to hold. A hidden input to a ZM or Combo Fighter figure, using a payee already in the cohort, is the gap to fill; no specific record is proposed because it needs a census first.

**Effect if adopted (arithmetic only, single runs on the current surface):** RET missed 82.4%; RET and CORR 73.6%; RET, CORR and OFF 64.8%. Catch rates are unknown. Author estimates have been wrong in both directions.

## 11. Routing (proposed; S0r decides)

**Universe:** P-CORR, P-OFF, P-RET and P-ALIAS through `/create-scenario --revise`, then `/create-injection`, then `/injection`.

**Prompt-side defects:** none found.

| # | Quoted span | Rule | Defect | Evidence |
|---|---|---|---|---|
| none | none | none | Keep `04_Prompt.txt` byte-identical | /prompt 5 on rev6; run events 2-532 |

**OE and rubric observations (for their own stages):**
- D1, D2 and D4 pin a folder, a role and a thread the prompt does not ask for;
- X5 accepts a blank bucket, so a do-nothing row passes;
- C1 to C4 are not bound to their issue;
- S6 must exclude total rows;
- OE must route MotMot through the founders' channel.

**Manifest errors for S0r:** T13 and T11 `base_pointers` name the wrong records; T6 still says only the contract decides, which rev6's note made untrue; the writes count says 4 reason comments while truth has 5 (Leapblock, Lucas, JPMorgan, Oleg, MotMot).

## 12. Self-review

| Item | Counter-reading | Resolution |
|---|---|---|
| RET LANDED | Strongest argument for CONFOUNDED: the notes are where founders said what came back, and nobody noted MotMot | The doc says "unless one of us has said", with no location limit; the run looked in Gmail (events 193, 205) and wrote a negative. `review/ret_motmot.md` section F. Re-verified with hg.py: `C04UEQVDVB7/1712901800.684259` and `C04UEQVDVB7/1712331718.859679` |
| OFF LEAKED | Best argument it was never live: the doc primes the hunt | Live: the deliberate search at event 177 missed; the receipts came collaterally. `review/other_traps.md` T2 |
| ORPH LEAKED | Could be FALSE, since the post arrived before any total | The run could have stopped at the notices; about a dozen Gmail calls failed first. `C05URGU759U/1770971846.479179` |
| CORR LEAKED | Argue it was a real struggle, so nearly landed | About 15 calls, but the wrong figure never reached the sheet. `ENG-2450`, `review/other_traps.md` T4 |
| ALIAS LEAKED | Argue the alias held, since it needed searches | Two searches, built from words in the note. `ENG-2444`, event 399 |
| T11 LEAKED | Could be FALSE: nobody was tempted | Decoy is on the path, but the pull is nil; recorded as no pull. `review/other_traps.md` T11 |
| CLASS FALSE | Best reading against: the contract is the real resolver | The run never opened `f_20a0df3860bb5731d22f07` and used the note. Re-verified in SQL `comment_990674712ad0127e26f780eadb5418ea` |
| Band (neighbouring) | Argue for 3: 17.6% of the surface; argue for 1: the platform's score of record | One root cause; bounded correction; the narrow-miss rule is not locally checkable. Argue 1 fails on `review/ret_motmot.md` section A. No CONFOUNDED failure counted; cascade counted once |
| Proxy | Argue the 38.46% is right | Hand-checked per slot in `review/surface_adjudication.md`; idle agent scores 0/91 |
| Repairs | Argue a repair repeats past failures | Attacked in `review/repairs_redteam.md`; two dropped, one downgraded |

Mechanical re-runs after the source tag correction: `trajectory_ledger.py` and `node_verdicts.py` (platform-precheck), `surface_grader.py`, `hardness_v2_check.py`, `mode_b_report.py` PASS.

**Re-certification of unchanged rev6 (2026-11-09).** The readiness framework committed on 2026-11-08 moved the context and gate-policy hashes, so the scenario and injection certificates were re-issued. `01_Universe_Inject.sql` (`ad50f039b5c2`) and `04_Prompt.txt` (`d0cb08476d23`) are byte-identical, so the platform /injection and /prompt results still apply.
- Changed: `context_hash` in both manifests and the V3 evidence file; `incorporating_span` on six surface slots; a Revision intake section in the design that takes in these verdicts and makes no design change; the role review re-bound to the new design hash; `hardness_reviews/scenario.json` and `injection.json`; `00_Readiness_Config.json`.
- Re-run: preflight (`hev_3f28212dd431c97c`, the design forecast with its disclosed rate overrides; truth and solver unchanged); SQL and dossier regenerated from their builders (SQL byte-identical; dossier changed only in the pasted gate block and the surface hash).
- `solver/solver.py` has no builder: its modification time was refreshed after preflight validated it unchanged against the current inputs.
- The red-team step was skipped at the requester's direction; the scenario's recorded fallback stands (design section 13).

**Unresolved:**
1. How the platform verifier will score 959,342.64: no rubric or OE exists yet.
2. Catch rates for every proposed move: unmeasured.
3. Fairness of P-OFF: needs a fork sweep before adoption.
4. Slack search ranks in the red team's review are inferred from run results and tool descriptions, not recomputed. Its warehouse census finished: "33,290", "Node Media", "MotMot" and "Lauren" have zero hits, and "Brooks" hits are a different person (`review/repairs_redteam.md`, Limits).

```
STAGE GATE hardening: PASS — Task_Authoring/task_inputsS2 · 01a_Hardening_Report.md#dfec70276bb4 · 01_Universe_Inject.sql#ad50f039b5c2 · 01_Hardness_Manifest.json#c72e4fa5529e · 00_Assigments.md#1555ee0dca48 · 01_Grounding_Dossier.md#d43bc618a2d2 · 06_PreCheck_Trajectory#130bb236b0e5 · 07_Baseline_Trajectories#ad7848c1ad99 · 10_Baseline_Verifier_Results.md#e3b0c44298fc · __context__#f24f2cf97f30 · __assignment__#a525bbe797a2 · __policy__#dc4ab5df3cdd · __gate_policy__#a392988e72d3 · __review__#0a90407fb37a · blocking 0 · warnings 0 · checks 19
[PASS] assignment.v3_context: Robert / Co-founder & Creative Director; easy cap <90%; freeze 2026-02-14T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe normal; KB bound; clock Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
[PASS] structure.outputs: 1 output(s) present: 01a_Hardening_Report.md
[PASS] structure.inputs: 2 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 06_PreCheck_Trajectory, 07_Baseline_Trajectories, 10_Baseline_Verifier_Results.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#ad50f039b5c2, 01_Hardness_Manifest.json#c72e4fa5529e, 01_Grounding_Dossier.md#d43bc618a2d2, solver/solver.py#4c9f139f4940, 01c_Dispositions.json#b1277995c8e8, 01c_Preflight_Report.json#fc59d75e7ceb, 00_Assigments.md#1555ee0dca48, 01_Scenario_Design.md#c72ef1de7aa8, 01_Hardness_Manifest.draft.json#55fa3467530a, 01_Gradable_Surface.json#32bb28690128, __context__#f24f2cf97f30, __assignment__#a525bbe797a2, __policy__#dc4ab5df3cdd, __gate_policy__#5b7d4d20094d, __review__#0a90407fb37a)
[PASS] structure.sections: 6 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] structure.placeholders: no placeholders in 01a_Hardening_Report.md
[PASS] structure.mode: MODE B declared
[PASS] evidence.register_run_step: 16/16 items carry a source pointer (min 100%)
[PASS] structure.sections: 4 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] revision.injection: injection checks re-run on revision N+1 (current SQL + manifest + dossier): PASS
[PASS] review.counter_readings: 10 evidenced counter-readings (of 10 found; need ≥ 7) in 01a_Hardening_Report.md
[PASS] review.coverage: self-review addresses all 2 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] readiness.context: explicit task/revision and current upstream evidence verified
[PASS] readiness.mode_b: PROVISIONAL_SINGLE_PRECHECK: current structured diagnosis
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## 13. Next steps

1. `/create-scenario --revise` dispositions these verdicts and decides P-CORR, P-OFF, P-RET and P-ALIAS, plus the ZM/Combo Fighter gap.
2. `/create-injection` implements rev7; then `/injection` and `/prompt` as a pair, with the prompt unchanged.
3. Re-apply the SQL, run a new Opus pre-check, send /hardness, and repeat this intake. Stop rule: one platform pre-check of two is used.
