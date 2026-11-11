# 01a Hardening Report: Robert seed bets (task_inputsS2)

## 1. Mode, inputs and run validity

**MODE B (baseline).** Six Opus 5.5 rollouts on SQL rev7 (`40f90385e31e`), prompt sha `d0cb08476d23`, rubric `923f89f3ac9c` (73 rows, weight 165), assessed 2026-11-10. This is the second six-run batch on rev7; the first batch's exports and verifier copy were replaced by this one.

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal). Universe manifest: `Evals/references/universes/normal/universe_manifest.json`.

Assignment: Robert, Co-founder & Creative Director; Executive; Finance; Analysis and synthesis; Long Horizon; Easy (cap under 90%).

**Inputs read:** `00_Assigments.md`, `01_Universe_Inject.sql` (rev7) and the five stored earlier revisions, `01_Grounding_Dossier.md`, `01_Hardness_Manifest.json`, `01_Gradable_Surface.json`, `03_Error_Async_Config.txt` (Friction: none), `04_Prompt.txt`, the six exports in `07_Baseline_Trajectories/`, `08_Oracle_Events.md`, `09_Rubrics.json`, `10_Baseline_Verifier_Results.md`, `solver/truth.json`, the platform reports in `plateform_reports/`, and the earlier report (rev6 pre-check, kept as `run_forensics/rev6/01a_Hardening_Report.precheck.md`).
**Missing:** `12_Difficulty_Stats.txt` (no file exists; the gates are recomputed in section 2). `11_AF_Justification.md` is empty. No reference files.

| Validity item | Finding | Pointer |
|---|---|---|
| Binding | All six exports BOUND to rev7 by discriminating content | `run_forensics/rev7/baseline2/summary.json` |
| SQL identity | Platform hash `8293d811` (/injection PASS, /prompt 5, /hardness 3 on rev7) is local `40f90385` with the first six header lines removed | `tail -n +7` of the SQL |
| Model | Every message `claude-opus-5-5`, subagents included; no fallback; `v3_valid` true in all six | `summary.json` provenance |
| Completeness | Each export ends in a successful `result`; no main-thread compaction; nothing after the result | `summary.json` validity |
| Subagent compaction | 19 subagent briefs across runs 1, 2, 4 and 6, 54 continuations; every subagent failed and none made a decision | `review/run-1.md`, `run-2.md`, `run-4.md`, `run-6.md` |
| File mapping | Verifier Run #N is export run-N for all six, bound on the spreadsheet id each run created | `run_forensics/rev7/baseline2/verifier_binding.json` |
| Hint status | No user turn in the exports; each run starts by reading #winddown | events 2 to 5 of each export |
| Injection applied | Seeded rev7 records appear in results (Leonard's 8605 message, the Chase records mail, the close-out post) | `review/run-3.md` section 3 |
| Counted calls | 125, 125, 123, 116, 132, 140; mean 127 | `summary.json` counts |
| Proposals and dispositions | `node_verdicts` proposed BYPASSED for all 42 node-by-run cells because it cannot join the runs' free-text payee labels; all 42 overruled by hand | `proposals.jsonl`, `dispositioned.jsonl` |
| Review coverage | Every call of every run read by one reviewer per run; review queue events (575, 413, 346, 393, 377, 678) reviewed; calls not read in full are listed in section 9 of each `review/run-N.md` | `review/run-1.md` to `run-6.md` |
| Ledger | 42 verdict records `hev_1448535b1df89e52` to `hev_449e70e0351d50f5`; 90 control and channel records | `ledger_record_ids.json` |
| Structured diagnosis | `mode_b_report` PASS, `SIX_SLOT_BASELINE`, after the title-binding fix in section 6 | `Working_Files/Mode_B_Diagnosis.json` |

Paths without a folder are under `Working_Files/run_forensics/rev7/baseline2/`.

## 2. Gate status

`12_Difficulty_Stats.txt` does not exist, so nothing is copied from it. The table is `difficulty_stats.py` on the bound verifier results (`difficulty_stats.txt`).

| Run | Counted calls | Weighted pass | Failed rows |
|---|---|---|---|
| run-1 | 125 | 87.3% | R7, R25, R32, R58, R68 |
| run-2 | 125 | 80.6% | R7, R8, R25, R32, R33, R58, R68, R69 |
| run-3 | 123 | 87.3% | R8, R25, R33, R58, R69 |
| run-4 | 116 | 87.3% | R8, R25, R33, R58, R69 |
| run-5 | 132 | 84.2% | R8, R12, R25, R33, R58, R69 |
| run-6 | 140 | 87.3% | R8, R25, R33, R58, R69 |

| Gate | Value | Rule | Verdict |
|---|---|---|---|
| Errored runs | 0 of 6 | at most 2 | PASS |
| Full passes | 0 of 6 | fewer than 5 | PASS |
| Average weighted pass | 85.7% | Easy: under 90% | PASS |
| Spread | 0.025 | 0.1 to 0.3 | **FAIL** |
| Failure patterns | 3 patterns; largest 4 of 6 failing runs (67%) | at least 2; largest at most 50% | **FAIL** |
| Horizon | mean 127 counted calls, no 100% run | at least 100 | PASS |
| Model | Opus 5.5 in all six | Opus 5.5 | PASS |

- **Clean average:** 85.7%, the same as raw. No failed row is confounded (section 7), so nothing is removed or corrected.
- **Mechanism weight share:** 37 of 165 (22.4%) depends on a decision that caught at least one run: Lucas 11, MotMot 11, Node Media 5, and the two shared total rows 10.
- **Concentration:** one decision, Lucas, fails in five of six runs. Runs 3, 4 and 6 fail the same five rows; run-5 adds one row and stays in their pattern.
- **Spread is out of reach for these failure modes.** With Lucas, MotMot and Node Media all missed a run scores 77.6%; the widest spread possible between 77.6% and 100% is 0.112. The pattern rule is the platform's Rule 2; the spread band is the retained local check that the platform's V3 screens do not restate.
- **Against the user's standing targets:** the average is above the 80% target; four of six runs are under 130 calls.

The first batch on rev7, read by hand from its stored sheet writes, failed the pattern rule the same way: four of six runs in the Lucas pattern (`review/rates_and_gates.md` section 4).

## 3. Predicted /hardness band

**Band 3 for the median run** (runs 3, 4 and 6 are identical at 87.3%; run-3 is used). This is the same failure the platform scored 3, PROCEED, on the rev7 pre-check (`plateform_reports/6aeed82596dcfe103f9f74d9_1a_hardness-5.md`, Clock line as above).

| Requirement (run-3) | Result | Pointer |
|---|---|---|
| Processed notices by Transaction Date, windows, merged spellings | MET | events 40, 85 |
| Leapblock close-out, own-account transfer, Oleg, MotMot return | MET | events 181, 302, 141, 259 |
| Contractor paid another way counts with a receipt (Lucas) | **MATERIAL_FAIL** | event 346: 6450 and "Sep to Nov 2024." |
| Buckets, currency, 22 lines, layout, sharing | MET | events 346, 364, 366 |
| Cost per bet | **MATERIAL_FAIL** for Domino Delights only, cascade of the Lucas row | event 363: 951817.64 |
| Linear comments and Done | MINOR_GAP, cascade: no comment on ENG-2447 | events 372 to 423 |
| Reply with costs, revenue, deck changes, link | **MATERIAL_FAIL** on the Domino Delights figure only, cascade | event 426: $951,818 |

One root cause; no confounded failure in the map.

**Why not 4.** One bounded correction, $7,525 on one line, carried to one total. **Why not 2.** The headline Domino Delights figure is wrong on the sheet, in the reply and in the deck change, and the platform scored the same profile 3.

## 4. Designed-difficulty register

| Node | Verdict counts over 6 runs | Run evidence | v2 kind |
|---|---|---|---|
| OFF (T2) Lucas, Western Union receipts | LANDED 5 · LEAKED 1 | run-3 · event 346 wrote 6450; run-6 · event 678 wrote 6450; run-1 · event 575 wrote 13975 | item outside the obvious filter |
| RET (T1, T10) MotMot returned wire | LANDED 2 · LEAKED 4 | run-1 · event 575 wrote 32160; run-2 · event 413 wrote 32160; run-3 · event 259 returned Leonard's message | off-path correction; where found, one search on the rule's own words |
| ALIAS (T5) Node Media | LANDED 1 · LEAKED 5 | run-5 · event 377 wrote Company; run-1 · event 524 returned the invoice thread | alias behind one token search |
| CORR (T4) JPMorgan $4,000 | LEAKED 6 | run-2 · event 154 searched 3203; run-4 · event 136 searched JPMorgan OR Chase 3203; run-6 · event 247 met the mail in a sweep | token join |
| ORPH (T3) Leapblock wire | LEAKED 6 | run-1 · event 402 and run-5 · event 257 returned the close-out post first | on_delegation_path |
| CLASS (T6) Lauren Brooks | FALSE 6 | run-4 · event 61 and run-2 · event 113 read the conclusion in the note | same_container |
| CURR (T7) Martin BGN | FALSE 6 | run-5 · event 130 and run-6 · event 591 parsed the currency from the notice | first_read, bulk field |
| Oleg returned wire | FALSE 6 | run-1 · event 75 and run-3 · event 141 read it in the note | same_container |
| T8 quick numbers | FALSE 6 | run-2 · event 392 and run-1 · event 552 used them as a checksum | first_read |
| T12 Awaiting and Scheduled notices | FALSE 6 | run-3 · event 40 filtered them out by subject | never on path |

## 4a. Verdicts by run, controls and channels

| Node | run-1 | run-2 | run-3 | run-4 | run-5 | run-6 |
|---|---|---|---|---|---|---|
| OFF | found | missed | missed | missed | missed | missed |
| RET | missed | missed | found | found | found | found |
| ALIAS | found | found | found | found | missed | found |
| CORR, ORPH | found | found | found | found | found | found |
| CLASS, CURR, Oleg | stated where first read | same | same | same | same | same |

No run got both OFF and RET right, which is why the two total rows fail six times.

**Controls.** The bank-name diff of all 22 payees in every run against `truth.json` (`review/register_diff.txt`) shows the misses above and nothing else. Every control member held in every run: Leapblock (RET, ALIAS), Graham Porter (OFF, CLASS), Eveline Art (ORPH), Singular (CORR), Adjoe (ALIAS), Lauren Brooks (CURR). No over-application.

**Channels.** CH-OFF failed in runs 2 to 6, CH-RET in runs 1 and 2, CH-ALIAS in run-5; CH-ORPH, CH-CORR, CH-CLASS and CH-CURR held in all six. Every decision was made by the main thread on `claude-opus-5-5`.

**Miss rates on rev7 over 13 runs** (this batch, the first batch read by hand, and the pre-check): OFF 10 of 13, RET 3 of 13, ALIAS 4 of 13, CORR 1 of 13, ORPH 0 of 13 (`review/rates_and_gates.md`).

## 5. Per-rollout ledgers

Full call tables, decision tables and verified quotes are in `review/run-1.md` to `review/run-6.md`; decoded writes in `run-N/writes.json`.

- **run-1 (654 events, 125 counted).** Never opened the founders' channel; its only returns search was Gmail (event 205, 19 bare ids, none opened). Found the Western Union receipts through a bulk fetch: a failed subagent left one receipt on disk, the main thread listed it (event 440) and then searched by name (465 to 511). Committed at event 543.
- **run-2 (485 events, 125 counted).** No Slack search for returns; three Gmail searches naming Lucas or receipts (169, 171, 338) returned capped pages of bare ids, none opened. Stopped when its totals tied to Leonard's quick pass (392). All research after the notices took about 93 seconds.
- **run-3 (430 events, 123 counted).** Found the 8605 message with one Slack search (257). Receipt searches (153, 171, 276) returned bare ids, none opened; never searched Lucas alone. Caught `SUMIF` returning `#NAME?` on read-back (354) and switched formulas.
- **run-4 (458 events, 116 counted).** Found the 8605 message with a Slack search for "wires" (343). The same result held Robert's own line "Western Union? Or wire?" (344); the run did not follow it.
- **run-5 (449 events, 132 counted).** Same "wires" result with the Western Union line (267), not followed; no search aimed at Lucas. Searched the Node Media token in Linear (294) and Drive (322), never in Gmail or Slack, and wrote Company. Sent a second Slack message (445) correcting a company subtotal.
- **run-6 (751 events, 140 counted).** Twelve subagents, none completed. Found the 8605 message as the first hit of a "came back" search (456). Four Gmail searches toward receipts (157, 189, 351, 388) returned first pages of bare ids, none opened.

Where they committed: each run fixed its notice set when its sums matched Leonard's quick row to the cent, and treated that match as proof of completeness. The match cannot show a payment that never had a notice.

**Not fully read:** raw bodies of the notice batches (the runs' parsed tables were read instead), most of the 22 status-move results per run, bare id lists, and subagent continuation summaries. Thinking blocks are empty in all six exports, so motives are read from calls and status lines.

## 6. Friction, tool-defect and horizon checks

- **Friction:** none configured; none expected.
- **Horizon:** 125, 125, 123, 116, 132, 140 counted calls; mean 127; no run under 100; no padding seen. Raw counts 167, 163, 138, 142, 147, 196. No 100% run, so the average governs.
- **Unconfigured behaviour, outcome unchanged:**
  - Gmail full-format batches are limited to 10 ids (run-2 events 191 to 205, run-5 event 95, run-1 event 112); re-chunked.
  - `SUMIF` evaluates to `#NAME?` in Sheets (run-3 event 354); the run switched to `SUM`. A run that left it in would lose R25 to R27 for a tool reason; none did.
  - Snowflake column-name errors (run-2 event 145, run-3 event 317, run-6 event 148), corrected on the next call. `jq` is not installed.
- **Tool traits that shaped the Lucas miss, not defects:** `gmail_search_messages` returns ids only, 100 a page, newest first, so a broad query cannot be triaged without opening messages. The wide notice search matched 434 messages, the five receipts among them; the result spilled to a file and the model saw a stub. The export keeps the spilled copy, so a text match on that event does not show the model read it.
- **Subagents:** every subagent ran on a 200K window, exceeded it on its first call and died ("Autocompact is thrashing"). None carried a method rule or made a decision. In run-1 the leftover batch file supplied the first Western Union receipt, so the only Lucas pass in this batch owes something to that accident.
- **Authoring tool defect, fixed during this stage:** `difficulty_stats.py` did not strip the platform copy's escaped brackets in titles, so 23 of 73 verifier rows did not bind and the stock `mode_b_report.py` refused the baseline. With the user's approval on 2026-11-10, `norm_title` now strips `\[` and `\]` (two added lines). The tool's self-test and the 21 unit tests of `test_difficulty_v3` and `test_mode_b_report` pass; the rebuilt matrix and gate table equal the first, in-memory computation. Other tasks' hardening, all-fail and difficulty certificates are bound to the old tool hash and need re-issuing when next used.

## 7. Verifier sanity

All 34 failed results were opened beside the write payloads. Each is genuine: the judge names the value the run wrote, and it matches the payload. No judge concedes a fact and fails it.

| Check | Finding | Pointer |
|---|---|---|
| All-fail rows R25, R58 | Valid; a cascade of two different root causes; each written total is off by exactly 4,032.00, 7,525.00 or both | `review/all_fail_R25_R58.md` |
| Collapsed runs | None; the lowest run is 6.7 points under the median | section 2 |
| Rows failed with the write present | R7, R8, R12, R25, R58: wrong value in the cell or reply, genuine | `review/register_diff.txt` |
| Rows failed with the write absent | R32, R33, R68, R69: no comment was posted on the issue | each `review/run-N.md` section 4 |

**New-release FAIL classes (B3f).**

| Class | Finding | Pointer |
|---|---|---|
| `overly_broad` | None seen in the failed or passed rows read; R64 passes with a wrong new figure because it grades only that the slide changes, as its title says | run-3 · event 426 |
| Idle agent passes a row | None of the 34 failures or the heavy passes depends on an absent write passing | `09_Rubrics.json` |
| Prompt Contrived | None; prompt unchanged since /prompt scored it 5 | `plateform_reports/6aeed82596dcfe103f9f74d9_1_prompt-5.md` |
| False premise for this universe | None raised on rev7 | `plateform_reports/6aeed82596dcfe103f9f74d9_0_injection-5.md` |
| Trash, attachment-only or unlinked evidence | Not relied on: the receipts are inbox mail, Leonard's message is channel text | `review/all_fail_R25_R58.md` |
| Stale reviews | The last stored /rubric report is round 3, FAIL 2 on `ba1f9ca2ee1c`; none is on file for `923f89f3ac9c`, the version the verifier graded | `plateform_reports/` |

Observation for the rubric stage, not a defect: R68 and R69 cannot pass when the comment is missing, so a missed adjustment costs its comment row and its order row together.

## 8. Why Opus passed

1. **A note that flags doubt sends every run to search, and the correction answers to the issue's own tokens.** ENG-2450 says Leonard cannot place the payment; Arthur's mail names JPMorgan and 3203. Four runs joined them in one Gmail search (run-2 event 154, run-3 event 297, run-4 event 136, run-5 event 224).
2. **Corrections that carry the method's own words fall to one short search.** The close-out post was the first hit of a Slack search for "received" in all six runs. Leonard's 8605 message says "came back", the doc's phrase; four runs found it with "came back" or "wires".
3. **Conclusions sit in the notes.** Brooks, Oleg's return and the laptop are stated on their issues.
4. **A free checksum.** Every run tied its parse to Leonard's quick row to the cent.
5. **No missed decision touches ZM or Combo Fighter.** Both adjustments that caught runs fall in the Domino Delights window.

Heavy rows (weight 5) that passed six of six: R6, R9, R10, R11, R26, R27, R31, R34, R59, R60. That is 50 of the 85 weight-5 points.

| Passed rows | Why | Class |
|---|---|---|
| R9, R10, R34 | Token join after a note that flags doubt | Universe leak |
| R6, R31 | The rule's word finds the record; first hit | Universe leak |
| R11, R13, R14, R15, R20, R35 | Stated where first read | Universe leak |
| R26, R27, R59, R60 | Sums of notices by date; nothing in doubt | Genuine capability; Opus finds this easy |
| R7, R32 in runs 3 to 6 | One Slack search on the rule's phrase | Universe leak, partly capability |
| R12 in five runs | Payee token searched in Gmail | Genuine capability |
| R16 to R19, R21 to R24, R28 to R30, R61 to R65 | Clean sums over bulk reads, labels from the notes, revenue from one table | Genuine capability |
| R1 to R5, R36 to R57, R66, R67, R70 to R73 | Routine delivery | Genuine capability |

No pass is attributed to a prompt leak.

`hardness_v2_check` on rev7 (advisory):

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

The checks read clean while two six-run batches fail the pattern rule: they test that the decisions exist, not how often each is missed.

## 9. Purge list (proposed; S0r decides)

- **Do not count as difficulty:** CLASS, CURR, the Oleg return, T8, T12. None caught a run in 13.
- **Keep as correctness rows:** all of the above; removing them risks forks the /prompt rounds closed.
- **ORPH and CORR:** live in design, never or almost never missed. ORPH stays as it is (its wording took three revisions to pass /prompt). CORR is the candidate for a rebuild (section 10).
- Nothing is proposed for deletion from the SQL.

## 10. Proposed rebuilds (candidates for S0r)

The gate that must change is the pattern rule. Lucas is missed in about three runs of four and nothing else splits those runs. Making Lucas easier is the wrong lever: at a 50% miss rate the average clears the 90% cap in only about half of simulated batches. What helps is a second decision that fails often enough on rows of its own. Both proposals were attacked against the records (`review/repairs.md`). Neither adds a payee, issue, step, write or prompt rule.

| Rank | Move | Type | Change | Facts it changes | Rows |
|---|---|---|---|---|---|
| 1 | **P-NODE** | Outcome coverage (rubric stage) | Grade where the Node Media dollars sit, as the rubric already does for JPMorgan, Brooks, Martin and Adjoe | None in the universe; one rubric row | R12 and the new row |
| 2 | **P-CORR2** | v2: deciding fact behind an alias | Arthur's Chase records mail states the amount, month and "our Chase account" without "JPMorgan" or "3203" | Body of one seeded mail; Oracle Event 19; evidence text of R9, R10, R34 | R9, R10, R34, R70, R25, R58 |

**Effect on this batch.** With P-NODE, run-5 fails two rows the others pass and becomes its own pattern: the largest pattern is runs 3, 4 and 6, three of six, exactly 50%, which passes. It needs /rubric and a verifier re-run on the same six exports, not a new baseline.

**Odds for a fresh batch (advisory, UNCALIBRATED; `review/gate_odds.py`).** Pattern, average and full-pass gates together: 32% as is; 65% with P-NODE; 58% with CORR missed one run in four; 81% with both. Catch rates for P-CORR2 are unmeasured.

**Considered and not proposed:** rewording Leonard's 8605 message (most runs would then miss both Lucas and MotMot, a new dominant pattern); restoring a pointer on ENG-2447 (pushes the average to the cap); moving the Leapblock close-out; re-weighting or dropping the total rows or the order rows; more payees or notices.

**Spread.** No proposal reaches the 0.1 band; the best simulated case reaches it in 9% of batches.

## 11. Routing (proposed; S0r decides)

**Rubric stage (`/create-rubric-writing check`, then /rubric and a verifier re-run):** P-NODE. It is proposed after the baseline and its effect on the gate is known, so it stands only if the rubric stage accepts it as coverage on its merits.

**Universe (`/create-scenario --revise`, then `/create-injection`, then /injection):** P-CORR2, if the user chooses a new revision. It re-opens /prompt, the Opus pre-check with /hardness, /oe, /rubric and the baseline.

**Prompt-side defects:** none found.

| # | Quoted span | Rule | Defect | Evidence |
|---|---|---|---|---|
| none | none | none | Keep `04_Prompt.txt` byte-identical | /prompt 5 on rev7; run-3 events 2 to 426 |

**Other stages:**
- `/create-allfail`: R25 and R58 failed all six runs and are valid (`review/all_fail_R25_R58.md`).
- `/create-difficulty`: the title-binding defect that stopped its build is fixed; it will report the two failing gates in section 2 until the pattern rule is addressed.
- OE and rubric observations: R68 and R69 are entailed by R32 and R33 when the comment is absent; the Node Media thread's subject reads "Fwd: Node Media Invoices for Sept, Oct, and Nov" in the tool result, with the masked name only in the forwarded body.

## 12. Self-review

| Item | Counter-reading | Resolution |
|---|---|---|
| OFF LANDED (5 runs) | Strongest argument for a tool cause: the receipts' ids came back in the run's first Gmail search and in later broad searches, so the tool hid them in spills and id-only pages | The spilled result was a wide body search the run chose to narrow; the later searches returned a first page with a next-page token that no run followed. A name search was open and run-1 read all five through ordinary calls (run-1 events 465 to 500). Receipts re-verified through hg.py in Robert's mailbox: `robert@harmonygames.co/1800906573953663690`, `robert@harmonygames.co/1808201960854294221` |
| OFF LANDED, fairness | Best argument that the rule is not incorporated for Lucas: ENG-2447 names no other way of paying, unlike ENG-2459, which names Payoneer | The rule is general in the doc the prompt delegates to, and every run read it (run-4 event 14, run-6 event 18) and applied it to Oleg. The platform /prompt scored rev7 5 and /hardness scored this miss as genuine. ENG-2447 |
| OFF LEAKED (run-1) | Argue the trap was not live in run-1: the receipt arrived by accident | Live: run-1's own money-service search missed it; the receipt surfaced from a failed subagent's leftover batch (run-1 event 440). Recorded as a bulk-call leak, and flagged as luck. ENG-2447 |
| RET LANDED (runs 1, 2) | Strongest argument for unfairness: Leonard said he left what they remember on the issues, and ENG-2442's notes say nothing of a return | The doc says "unless one of us has said the money came back" with no location limit; both runs left Linear for close-outs. Message re-verified at SQL line 52, `C04UEQVDVB7/1770947533.284619`; Robert is a member (run-1 event 413 returned messages from that channel) |
| RET LEAKED (runs 3 to 6) | Best argument it was never live: the rule's phrase finds the message as the first hit | Live but cheap: it needs a Slack search for returns, which two runs never made. Runs 3 and 6 used the doc's own phrase (run-3 event 257, run-6 event 456). `C04UEQVDVB7/1770947533.284619` |
| ALIAS LANDED (run-5) | Argue a tool cause: the Slack search for LLC was capped at 40 hits and missed Leonard's Node Media line | The run never searched the payee token in Gmail, where five other runs found the thread in one call (run-4 event 327). ENG-2444 |
| ALIAS LEAKED (5 runs) | Could be FALSE: is the alias resolved where the run first reads? | No: the ENG-2444 notes do not name the agency; each run needed a Gmail search on the token (run-2 event 365). ENG-2444 |
| CORR LEAKED | Argue FALSE: the note's doubt hands the run the search | The wrong recollection is on the issue and one batch-1 run took it at face value, so it is live; in this batch one token search settled it (run-2 event 154). ENG-2450, SQL line 69 |
| ORPH LEAKED | Could be FALSE, since the post is the first hit of the rule's word | The run has to leave the notices and search Slack; all six did, as the first search after the notices (run-5 event 256). `C05URGU759U/1770971846.479179`, SQL line 50 |
| All-fail R25, R58 | Argue a rubric defect: one fact graded in the cell, the total and the reply | The total is a requested output and fails on two different root causes; each row accepts any label and rounding. ENG-2442 and ENG-2447 adjustments are separate facts from the sum. `review/all_fail_R25_R58.md` |
| Band (neighbouring) | Argue for 2: 0.8% of the Domino Delights figure; argue for 4: three deliverables carry it | One root cause with a bounded correction; the platform scored the same profile 3. No confounded failure is counted and the cascade is counted once. ENG-2447 |
| P-NODE | Strongest argument against: it is a rubric change made after seeing the baseline, and it is known to flip the gate | Disclosed in sections 10 and 11 and in `review/repairs.md`; it would fail the tuning rule unless the rubric stage accepts it as coverage. The two-cell pattern already exists for ENG-2450 and ENG-2455 |
| P-CORR2 | Argue it changes nothing: queries with Chase, or a sweep of recent mail, still find the mail | True for four of six runs in this batch; the move aims at about one miss in four. Catch rate unmeasured. ENG-2450 |
| Proxy tools | Argue the 20 to 36% surface grades are right | They are join failures on free-text payee labels; the bank-name diff matches the verifier on every row. `review/register_diff.txt`, ENG-2438 to ENG-2459 |

Records re-verified, not carried from notes: the five receipt threads through `hg.py search get gmail` (base, Robert's mailbox, Jun 3 to Aug 23 2024); Leonard's 8605 message, the Chase records mail and the close-out post in `01_Universe_Inject.sql` (lines 52, 65 to 75, 50); the base Slack lines about Western Union in the founders' channel and Robert's DM through `hg.py search search-many`. The Western Union amounts were read from run-1's tool results and the verifier's pass, not from the base export.

Mechanical re-runs: `trajectory_ledger.py`, `node_verdicts.py`, `surface_grader.py`, `hardness_v2_check.py` on the six exports; `difficulty_stats.py` and `mode_b_report.py` on the fixed tool (PASS). Every quote in `mode_b_request.json` was checked against its export.

Stage gate history, 2026-11-10: before the tool fix the gate failed on one check, `readiness.evidence` (verifier rows did not bind to `09_Rubrics.json`), with the other 17 passing. The block pasted below is from the gate run after the fix.

**Unresolved:**
1. The tool fix changes the tool hash that hardening, all-fail and difficulty certificates record, so those certificates in other task folders are stale until re-issued. `stage_gate.py --self-test` was not re-run after the fix.
2. Whether the spread band is enforced under V3. It cannot be met by this design.
3. Catch rates for P-CORR2, and the fresh-batch odds in general, are simulated from 13 runs and uncalibrated.
4. The first batch's rates are a hand reading of stored sheet writes; its exports and verifier copy no longer exist.
5. Whether any other record ties account 3203 to Chase was not censused.
6. No stored /rubric report covers `923f89f3ac9c`.

```
STAGE GATE hardening: PASS — Task_Authoring/task_inputsS2 · 01a_Hardening_Report.md#f7e355d175a2 · 01_Universe_Inject.sql#40f90385e31e · 01_Hardness_Manifest.json#5fc94e51431e · 00_Assigments.md#1555ee0dca48 · 01_Grounding_Dossier.md#7973cba43933 · 06_PreCheck_Trajectory#5846a6c8442b · 07_Baseline_Trajectories#d42f90ce272f · 10_Baseline_Verifier_Results.md#62e1a5af1ee3 · __context__#f24f2cf97f30 · __assignment__#a525bbe797a2 · __policy__#dc4ab5df3cdd · __gate_policy__#a392988e72d3 · __review__#0a90407fb37a · blocking 0 · warnings 0 · checks 19
[PASS] assignment.v3_context: Robert / Co-founder & Creative Director; easy cap <90%; freeze 2026-02-14T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe normal; KB bound; clock Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
[PASS] structure.outputs: 1 output(s) present: 01a_Hardening_Report.md
[PASS] structure.inputs: 2 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 06_PreCheck_Trajectory, 07_Baseline_Trajectories, 10_Baseline_Verifier_Results.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#40f90385e31e, 01_Hardness_Manifest.json#5fc94e51431e, 01_Grounding_Dossier.md#7973cba43933, solver/solver.py#4c9f139f4940, 01c_Dispositions.json#b1277995c8e8, 01c_Preflight_Report.json#3cb202c824eb, 00_Assigments.md#1555ee0dca48, 01_Scenario_Design.md#c8d2df78fd47, 01_Hardness_Manifest.draft.json#6f37313201ce, 01_Gradable_Surface.json#32bb28690128, __context__#f24f2cf97f30, __assignment__#a525bbe797a2, __policy__#dc4ab5df3cdd, __gate_policy__#5b7d4d20094d, __review__#0a90407fb37a)
[PASS] structure.sections: 6 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] structure.placeholders: no placeholders in 01a_Hardening_Report.md
[PASS] structure.mode: MODE B declared
[PASS] evidence.register_run_step: 10/10 items carry a source pointer (min 100%)
[PASS] structure.sections: 4 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] revision.injection: injection checks re-run on revision N+1 (current SQL + manifest + dossier): PASS
[PASS] review.counter_readings: 14 evidenced counter-readings (of 14 found; need ≥ 9) in 01a_Hardening_Report.md
[PASS] review.coverage: self-review addresses all 2 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] readiness.context: explicit task/revision and current upstream evidence verified
[PASS] readiness.mode_b: SIX_SLOT_BASELINE: current structured diagnosis
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## 13. Next steps

1. Run `/create-allfail` for R25 and R58 (both valid), then `/create-difficulty`; it will show the spread and pattern failures of section 2.
2. Choose the route for the pattern rule: P-NODE alone (rubric stage, /rubric, verifier re-run on the same exports), or a new revision with P-CORR2 through `/create-scenario --revise` and `/create-injection`, with P-NODE alongside.
3. Decide whether the spread band blocks submission.
