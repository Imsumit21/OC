# Hardening Report — frederick_q4_commitments · rev3 · MODE B (pre-check intake)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Universe manifest: Evals/references/universes/synthcut/universe_manifest.json. Platform report quoted: run_forensics/rev3/platform_hardness_review.md (FINAL VERDICT: FAIL, Score 2, HOLD; its Clock line: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)).

## 1. Mode, inputs and run validity

MODE B (pre-check). One Opus 5.5 trajectory from the platform pre-check, stored at 06_PreCheck_Trajectory/trajectory.json (sha256 d5dc726b6150; copy in run_forensics/rev3/precheck/trajectory.json).

- **Inputs read:**
  - 00_Assigments.md, 01_Universe_Inject.sql (rev3, 2176eb708f74), 01_Grounding_Dossier.md, 01_Hardness_Manifest.json, 01_Scenario_Design.md;
  - 04_Prompt.txt (32f7ab0cabd6), 03_Error_Async_Config.txt (Friction: none);
  - Working_Files/01_Gradable_Surface.json, Working_Files/solver/solver.py;
  - the three stored revisions (run_forensics/rev1, rev2 and rev3 SQL);
  - the platform /injection, /prompt and /hardness reports for rev3.
- **Inputs missing:** none for a pre-check intake. There are no baseline files (07, 10 or 12) yet, so there are no gate statistics.
- **Validity** (trajectory_ledger.py): stream-json, completed (subtype success, 266 turns), with no compaction, no events after the result and no unpaired calls. Two results spilled to files (the DM history at event 428 and the contacts list at event 496); the run read both back with Bash.
- **Models:** claude-opus-5-5 on every message (init label claude-opus-5-5[1m]). mixed_model false, v3_valid true, no fallback, no subagents (briefs 0).
- **Binding:** BOUND to rev3 on discriminating content. The rev3 seeded texts appear in the results, e.g. Leonard's waiver reply returned at opus · event 444.
- **Prompt match:** by content. The hub thread was opened at event 13, which matches the prompt's "Leonard's email yesterday".
- **Counted calls:** 260 (raw 265: 4 harness Bash calls, 1 repeat).

Pre-check intake results:
1. **Binding:** BOUND rev3, valid for claude-opus-5-5. Mixed-model flags: none.
2. **Proposals:** node_verdicts gave 21 proposals (8 verdicts, 7 controls, 6 channels). All 21 were dispositioned (run_forensics/rev3/precheck.dispositioned.jsonl). The review queue was empty; I reviewed every deciding-record call listed in §5 myself.
3. **Deliverable diff** (surface_grader): raw 58.4%. Confirmed against the write payloads, only X1, X2, X17 and V1 (all Nintendo) are genuine, so the corrected surface score is 85.6%. The other 10 failed slots are decoder strictness (§6).
4. **Ledger:** 21 records appended (added 21, rejected 0). Record ids run from hev_b8f28a892a74b855 to the last of the 21 appended on 2026-11-04; the forecast record is separate.
5. **Posterior forecast** (pre-registered): hev_0da57c866a323beb. V3 E[avg] 0.78 [0.70, 0.87], P(all four gates) 0.12–0.53 across dependence scenarios. UNCALIBRATED; the CH-SLIP rate is disclosed (0.02, from this run's zero substantive slips).
6. **Go / no-go: NO-GO.**
   - /hardness is 2 (needs 3 or more).
   - Only one independent loss channel failed in Opus's own decisions (DONE / Nintendo), against a need of 2.
   - The tool's CH-SLIP count was representational and is dispositioned HELD.
   - Route: /create-scenario --revise. This was pre-check 1 of the 2 allowed for this scenario (stop rule).

## 3. Predicted /hardness band (B3c)

| Requirement | Outcome | Citation |
|---|---|---|
| R1 scope (36 companies) | MATERIAL_FAIL: 35 logged, Nintendo never considered | Nintendo threads listed at opus · event 66 (gmail_list_threads), never opened; no Linear call in 265 calls |
| R2 Answered (4) | MET | register write opus · event 533 |
| R3 End (10) | MET (including the Clipforge cancel to billing@paylane.io) | opus · event 610 |
| R4 Keep (3) | MET (Pingwise by night pager) | keep card read at opus · event 50 |
| R5–R6 Sign (7) | MET 6 of 7; Nintendo missing | cards at events 540 onward; reply at opus · event 767 omits Nintendo |
| R7 Park (12) | MET (Framewell from the thread reply) | opus · event 455 |
| R8–R14 log, cards, reminders, ESG, answers, contacts, reply | MET, except the Nintendo row, card and reply line | events 528–767 |

- **Band 2, which is what the platform scored.** There is one root cause and its share is about 5%, below Easy's 10% loss, so the narrow-miss rule applies.
- **Why not 3:** a second independent cause would remove the narrow-miss rule. None exists; the run caught every other trap.

## 4. Designed-difficulty register (per-node counts out of 1 run)

| Node | Mechanism | Verdict | Counts (landed · confounded · leaked · bypassed · not-reached) | Evidence (opus · event) | v2 failure kind |
|---|---|---|---|---|---|
| DONE Nintendo | A24 done gap | LANDED | 1 · 0 · 0 · 0 · 0 | portal mails listed at opus · event 66, never opened; Linear never called; register opus · event 533 has no Nintendo row | landed as a cohort omission (outside the inbox-and-folder filter) |
| CORR Framewell | A11 superseding | LEAKED | 0 · 0 · 1 · 0 · 0 | Slack search 'Framewell' at opus · event 444, 'vendor after:2025-09-01' at event 480, thread opened at opus · event 455 | the correction names its company, so the name search returned it |
| COMPL Lanternfly | A25 completion elsewhere | LEAKED | 0 · 0 · 1 · 0 · 0 | Slack search 'Lanternfly' at opus · event 387, 'told after:2025-09-01' at event 426, DM history newest message at opus · event 428/430 | named, uses the word 'told', and sits as the newest DM root |
| EXC Pingwise | A15 authority exception | LEAKED | 0 · 0 · 1 · 0 · 0 | keep-running card opened directly at opus · event 50 (the guardrails name it) | on_delegation_path |
| DATE Clipforge | A4 superseding notice | LEAKED | 0 · 0 · 1 · 0 · 0 | Paylane HG-2291 notice in the Aug 15+ listing at opus · event 66, opened at event 187 | first_read (inbox sweep) |
| FILT Pixel Harbor | A17 exact predicate | LEAKED | 0 · 0 · 1 · 0 · 0 | July tracker at opus · event 284, paper at event 296, name search at opus · event 309 | decoy led to the answer; no date filter was used |
| SIGN ESG routing | A12 | LEAKED | 0 · 0 · 1 · 0 · 0 | ESG thread with Leonard's reply opened at opus · event 43 | same_container (SAME_PLACE flag T7) |
| AMEND Monday change | A15 | LEAKED | 0 · 0 · 1 · 0 · 0 | #executives history from Sep 29 at opus · event 35 | on_delegation_path (the hub names it) |

**Controls (Retainly, Glyphworks, Playable Factory, Hootline, and the rest)** are all HELD. The only flagged differences are same-day date suffixes. Every channel is HELD, apart from CH-DONE, which is UNOBSERVED because Nintendo is absent.

## 5. Per-rollout ledger (precheck)

Full ledgers: run_forensics/rev3/precheck/calls.jsonl (265 calls), writes.json (91 writes), ledger.json.

How the run searched and read (its exposure map; scratchpad expo.py over the trajectory):

| Step | Tool | Input | What came back | Decision |
|---|---|---|---|---|
| opus · event 13 | gmail_get_thread | hub thread | the job, the scope and every pointer | starts from the hub |
| opus · event 30 / 35 | slack_conversations_history | #executives from Sep 27, then Sep 29–30 (roots only) | the Monday change | applies it |
| opus · event 45 / 50 | trello_get_lists / get_card | Harmony Games board, keep-running card | night pager item | Pingwise Keep |
| opus · event 66 / 79 | gmail_list_threads | after:2025/08/15, two pages | every Sep cohort thread, the Paylane notice, Nintendo portal mails | opens 49 threads, skips the Nintendo notices |
| opus · event 282 | gdrive_list_folder | paperwork folder | all 34 papers | reads every paper (35 doc reads) |
| opus · event 284 | gdrive_read_sheet_range | July tracker | Pixel Harbor 'quote in' | searches 'Pixel Harbor' at event 309 |
| opus · event 386–480 | slack_search_public_and_private | each company name, plus 'trial', 'quote', 'told', 'vendor', 'booth', 'retainer' | Framewell reply, Lanternfly DM, Spotlight note | all three corrections caught by name or by 'told' |
| opus · event 428 / 430 | slack_conversations_history + Bash | DM D05S58U4SAK, newest 100 | the Lanternfly DM is the newest root | caught again |
| opus · event 488 | gcal_search_events | 'commitments' | the Jan 5 review | the only calendar read |

**Never opened:**
- Linear;
- any Trello card except the keep-running card;
- calendar events other than the review;
- Slack threads it did not land on through a search (one thread opened in total);
- #executives roots before Sep 27, unless a search returned them;
- Gmail threads before Aug 15, except name searches seeded by a paper or the tracker.

## 6. Friction, tool-defect and horizon checks

- **Friction:** none configured (03_Error_Async_Config.txt). No forced error and no async function fired.
- **Tool defects:** none changed an outcome. The two spills (events 428 and 496) were read back.
- **Surface decoder strictness** (confirmed against the write payloads; not run failures):
  - X6, X14, C1, C2 and C3 are written with a date or full name, e.g. 'Leonard Hayes, Sep 27 (call)' and '2026-01-05 (January commitments review)'.
  - X13, C5 and C11 are written as 'No: …' or 'won't', which the told regexes miss.
  - D1: the sheet was made with gdrive_copy_file plus a parentId at event 528, which `_register_parent` does not read.
  - D2: the reply call does not set reply_all to false.
  - Route: the rubric must accept the brief §4b classes. The surface's matchers are scenario-owned, so S0r should loosen them in rev4.
- **Horizon:** 260 counted calls. The Long Horizon minimum is 100 and the requester's target is more than 130 per run, so this clears both by about 2×.

## 7. Verifier sanity

Not applicable: no verifier or rubric has run yet. The platform /hardness requirement map (§3) agrees with the corrected surface diff: only the Nintendo outputs fail.

## 8. Why Opus passed

`hardness_v2_check.py` on rev3 (pasted):

```
FLAG       SAME_PLACE      5 trap(s) with two or more version records; 1 flagged, 0 unresolved
CLEAN      DONE_CHECK      an A24 / done_gap node exists
CLEAN      TWO_DECISIONS   cross-source rules decide 5 requirements: {'R6': ['DONE', 'SIGN'], 'R2': ['CORR', 'DATE', 'AMEND'], 'R4': ['COMPL'], 'R3': ['EXC'], 'R1': ['FILT']}
FLAG       DECISION_FLIP   6 of 8 rules can flip a weight-5 slot; not: ['SIGN', 'AMEND']
CLEAN      INPUT_CHECK     0 weight-5 total(s); 0 with an input a rule can change
CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter
CLEAN      RULE_IN_PROMPT  no run of 8 resolver words in the prompt
SAME_PLACE T7 (same_container): the correction and a superseded version share gmail:1844177063117059830
DECISION_FLIP SIGN: rule SIGN (A12) can flip slots of weight [3], no weight-5 slot
DECISION_FLIP AMEND: rule AMEND (A15) can flip slots of weight [3], no weight-5 slot
```

- **Universe leak: every correction carries its company's name.** The run searched Slack for all 36 company names (opus · event 386–480). That search also reaches DMs, so Framewell's waiver, Lanternfly's call-back and Robert's Spotlight answer each came straight back. The generic searches 'told' and 'vendor' returned them a second time, because the records use those words.
- **Universe leak: newest-root placement.** Lanternfly's answer is the newest root in the DM, so any history read shows it first.
- **On the delegation path (genuine capability, kept):** the keep-running card, the Monday change and ESG's note are named by the hub or the guardrails. They are incorporated rules, so they cannot move without breaking incorporation.
- **Inbox sweep:** the Paylane notice sits in the swept Aug 15+ listing. The June Pixel Harbor quote was reached through the July tracker decoy and its filed paper.
- **What worked:** Nintendo is the only in-scope item outside the inbox-and-folder filter, and it lives in a service the run never opened.
- **Heavy rows that passed** (weight 5): X3 Framewell decision, X5 Lanternfly decision, X6 and C3 answered-by, X7, X9, X12, X14 and X16. Do not add more weight-5 rows of these kinds; move their corrections instead.

## 9. Purge list (proposed; S0r decides)

- **No purge.** Every LEAKED node is either an incorporated rule (EXC, SIGN, AMEND, DATE), which is genuine capability and needed for correct decisions, or repairable by moving its correction (CORR, COMPL, the Spotlight answer, FILT).
- **The SAME_PLACE flag on T7 stays.** Leonard's Sep 25 reply supersedes the July note inside the thread the hub names. Moving it would cut the incorporation chain the /prompt review relied on (platform_prompt_review.md F9).

## 10. Proposed rebuilds (Hardness v2 moves; no added rows, items, steps or volume)

Each move reworks or relocates a record that already exists, keeps truth.json unchanged, and lands on at least two graded outputs. Catch rates are UNCALIBRATED estimates. They come from this run plus measured analogues in the bridge task: a reply under an unrelated root was caught about 20–30% of the time, and the DM read rate was 1 in 6 to 6 in 15.

| # | Node | Move (v2 kind) | Why this run would miss it | Outputs a miss changes | Est. catch |
|---|---|---|---|---|---|
| M1 | CORR Framewell | **De-name the correction.** Leonard's Sep 26 reply under the Playtestcloud root (C07C2866011/1758920520.674991) drops 'Framewell' and 'vendors' and names Maren, Framewell's account manager (Maren Holt on the Sep 18 order form), and 'the Pro plan'. 'Maren' has no person match in the base data (its only hits are inside 'gsmarena'). | The 'Framewell' and 'vendor' searches (opus · event 444, 480) no longer return it. It is a thread reply from before the run's Sep 27 history window. | Decision Park becomes End (the order form bills Nov 1), Next date, the written answer (cancel instead of January), the Jan 5 reminder | 0.3 |
| M2 | COMPL Lanternfly | **Move the answer into a thread under an unrelated root, de-named.** Leonard's note becomes a thread reply in DM D05S58U4SAK under an existing earlier root, and refers to Wen (Wen Halvorsen, Lanternfly Publishing) and 'the Southeast Asia deal', with no 'Lanternfly' and no 'told'. Keep the phrase 'Southeast Asia has to wait until after the raise' (the solver and the X15 regex key on it). | DM history shows roots only, and the note is no longer the newest root (opus · event 428). The name search and the 'told' search miss it. | Decision Answered becomes Sign (2-year exclusivity, so ESG), Answered by, What we told them (X15), the Jan 5 reminder, plus a wrong card, a wrong ESG email and a wrong answer to Wen | 0.35 |
| M3 | Answered Spotlight Fest | **De-name Robert's Sep 17 note** (C07C2866011/1758134460.899858): 'had the call about the Dec 5 indie showcase, we're sitting this one out and I let them know'. No 'spotlight', 'told' or 'booth'; 'indie showcase' has 0 base hits. Remove the answer from the ○ calendar description of evt_564a16d0f5f6598d0360d5 so the ● Slack note is the only carrier. | The 'Spotlight' and 'told' searches (opus · event 386, 426) miss it. It is a root from before the Sep 27 history window. The run's only calendar search was 'commitments'. | Decision Answered becomes End ($750 stand fee in the window), Answered by (C3), plus an extra email to Rina that the guardrails forbid ('don't write to them again') | 0.4 |
| M4 | FILT (membership) Hootline | **Move one in-scope item outside the obvious filter.** Gemma's follow-up ask moves from Sep 24 to before Aug 15 (thread frederick.stone@harmonygames.co/1839631800730308867 then has messages on Aug 5 and Aug 12 only). Drop the filed paper f_f7902fdbb11a8bbd623959; the terms stay in the email body. It is still in scope: Frederick signed up (engaged), and Gemma's 'would you like to keep the scheduler after that?' is waiting. Hootline is not in the July tracker. | The run built the cohort from the after:2025/08/15 listing (opus · event 66/79), the paperwork folder (event 282) and the tracker (event 284). Hootline would appear in none of them. | Membership (V1), the log row, the written answer, the contact, the Jan 5 reminder | 0.45 |
| M5 | DONE Nintendo | **Keep as is** (landed) | portal notices skipped, Linear never read | Decision, card, Next date, the reply's sign list, V1 | 0.4 |

- **Independence:** each move is caught by a different behaviour.
  - M1: opening #executives thread replies, or searching the contact's name.
  - M2: opening DM threads.
  - M3: reading all of September's #executives roots, or searching the calendar by name.
  - M4: listing the inbox from before mid-August.
  - M5: opening portal mail, or searching Linear.

  M1 and M2 both reward opening threads, but they sit in different containers.
- **Single-run odds:** with these rates, P(two or more independent misses in one Opus run) ≈ 0.9 (UNCALIBRATED; product over the five estimated rates). Two causes remove the narrow-miss rule, which predicts /hardness 3, or 4 if a heavy cascade (M2) lands.
- **Requester's under-80% average:** each miss changes 3 to 6 graded outputs. To keep the corrected average below 80%, the rubric stage has to weight the decision, membership and wrong-write rows of these five items, and grade the negative writes in M2 and M3.
- **Surface matchers (route to S0r):** loosen the told regexes ('no', 'won't', 'said no', 'passed'), the Next date comparator (same-day annotations), the answered-by comparator (full name plus date), register_parent (also gdrive_copy_file with parentId) and email_reply (reply_all unset). Today the local proxy under-reports a correct run by 27 points.

## 11. Routing (proposed; S0r decides)

- **Universe changes** (/create-scenario --revise from S5a with a design_delta, then /create-injection rev4, then /injection):
  - M1–M4 as above.
  - Facts they would change:
    - the text of C07C2866011/1758920520.674991 (Framewell waiver);
    - the Lanternfly answer's container and text (D05S58U4SAK/1759174260.052645 becomes a thread reply);
    - the text of C07C2866011/1758134460.899858 and the description of evt_564a16d0f5f6598d0360d5;
    - the date of Hootline's second message, and removal of f_f7902fdbb11a8bbd623959 (its doc and Drive rows).
  - truth.json values are unchanged. The dossier's fact_check entries for the Lanternfly call-back and the Spotlight answer, the brief §5 locators, and the manifest seeded_ids for T2, T3 and FILT change.
- **Prompt-side defects:** none. /prompt rev3 scored 5 on every dimension, and the /hardness reviewer proposed universe changes only. 04_Prompt.txt (32f7ab0cabd6) can stay, but /prompt must re-run on the rev4 SQL.

| # | Quoted span | Rule (doc §) | Defect | Evidence (rollout · step) |
|---|---|---|---|---|
| — | none | — | no prompt-side defect found | opus · event 13 started from the named hub as intended |

- **OE / rubric observations** (route to /create-oe-writing and /create-rubric-writing):
  - accept the §4b representational classes;
  - grade the negative writes: no email to Answered companies, no ESG email or card for non-ESG rows;
  - require the Priya note (platform_prompt_review.md F5).

## 12. Self-review

Walked Evals/1A_Hardness_Eval.md §3–§5 against this report. Every deciding record behind a LANDED or LEAKED verdict was re-verified in this run:
- hg.py search gmail 'NDA Effective' → threads/frederick@harmonygames.co_1842359398719557772.json;
- cmt_c9a6660d81e067ad1de7 in 01_Universe_Inject.sql ('agreement approver … company officer');
- the Slack texts of the six seeded messages read from the SQL;
- the alias names checked with hg.py: 'Maren' slack 6 / gmail 20 hits, all inside 'gsmarena'; 'Halvorsen' 0; 'SEA deal' 0; 'indie showcase' 0; 'asset library' slack 3 / gmail 6, so it is rejected as an alias.

| Verdict | Counter-reading | Evidence that resolves it | Result |
|---|---|---|---|
| DONE LANDED | Strongest case for a tool cause: the Nintendo mails never reached the run | They were returned at opus · event 66 (gmail_list_threads) and simply not opened. Linear is unscoped (Evals/references/persona/acl.md). The platform calls it a genuine retrieval failure (platform_hardness_review.md F1) | stays LANDED |
| DONE LANDED | Fairness: Nintendo is a platform, not a 'vendor or partner' | The hub defines scope by engagement and terms, not vendor type (frederick.stone@harmonygames.co/1844732913254784171). The /prompt review settled Nintendo as in scope (platform_prompt_review.md F20/F21) | stays LANDED |
| CORR LEAKED | The trap was never live (FALSE) | It was live by design: the order form (f_fba21c2d5d4bbb02983961) says Nov 1 billing. The leak is the company name in the reply, returned by the 'Framewell' search at opus · event 444 | LEAKED, rebuild M1 |
| COMPL LEAKED | It was never live, because any DM read shows it | The DM history at opus · event 428 is roots only. The note leaked because it is the newest root and carries 'Lanternfly' and 'told' (event 387, 426) | LEAKED, rebuild M2 |
| EXC LEAKED | It should be FALSE: the guardrails name the card | The card is an incorporated authority (f_b98287f6f80fe431a71209 step 3). The alias still needed a function match at opus · event 50, so it is genuine capability, kept as a decision step | LEAKED, keep |
| DATE LEAKED | A bulk call carried the answer | Yes: the Aug 15+ listing at opus · event 66 surfaced the HG-2291 subject. It stays as an incorporated cash-test decision, not counted as difficulty | LEAKED, keep |
| FILT LEAKED | It was never live, because the paper names Pixel Harbor | Confirmed: the paper (f_614f88a28a2f0cf1b88408) and the July tracker (opus · event 284) both lead to the June thread. The filter move goes to Hootline instead (M4) | LEAKED, rebuild via M4 |
| SIGN LEAKED | The superseded July note shares a container with the correction (verbatim supersession) | The SAME_PLACE flag on T7 is accepted. The supersession sits in the thread the hub names (frederick.stone@harmonygames.co/1844177063117059830), which is incorporation the /prompt review relies on | LEAKED, keep |
| AMEND LEAKED | It was stated where the agent reads first | Yes: the hub names the Monday post and the run read it at opus · event 35. It is on the delegation path by design (R2) | LEAKED, keep |
| Band | Neighbouring band 3: Framewell's annotated Next date and the 'No:' told texts are failures, so there are more causes | They are representational, the same day and the same meaning, confirmed against the payload at opus · event 533 (§6). The platform found no other failure. One cause below 10% gives the narrow-miss score of 2 | band 2 |
| Rebuild risk | De-named corrections could fail /prompt UGT (the reviewer can't tie 'Maren' or 'Wen' to the company) | Both names sign their company's own thread (Maren Holt on Framewell's order form email, Wen Halvorsen 'Lanternfly Publishing'). The /prompt review accepted the alias-by-function night pager (platform_prompt_review.md F7) | holds; re-check at /prompt |

Unresolved:
- The catch rates in §10 are estimates (UNCALIBRATED), and one run cannot confirm them.
- The stop rule allows one more pre-check for this scenario. If rev4 also scores 1–2, the scenario changes.
- The surface matcher fixes are routed to S0r.

```
STAGE GATE hardening: PASS — Task_Authoring/task_inputs · 01a_Hardening_Report.md#44ec9d231b56 · 01_Universe_Inject.sql#2176eb708f74 · 01_Hardness_Manifest.json#b421fd17be6c · 00_Assigments.md#5418f950517f · 01_Grounding_Dossier.md#39850b36d43c · 06_PreCheck_Trajectory#a5c3c224ab88 · 07_Baseline_Trajectories#ad7848c1ad99 · 10_Baseline_Verifier_Results.md#e3b0c44298fc · __context__#db8af19cc1c3 · __assignment__#b196657eace0 · __policy__#dc4ab5df3cdd · __gate_policy__#115714063000 · __review__#d1d08c1c8c7d · blocking 0 · warnings 0 · checks 17
[PASS] assignment.v3_context: Frederick Stone / Co-founder; easy cap <90%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 01a_Hardening_Report.md
[PASS] structure.inputs: 2 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 06_PreCheck_Trajectory, 07_Baseline_Trajectories, 10_Baseline_Verifier_Results.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#2176eb708f74, 01_Hardness_Manifest.json#b421fd17be6c, 01_Grounding_Dossier.md#39850b36d43c, solver/solver.py#499c42dc489b, 01c_Dispositions.json#4cd7244b387c, 01c_Preflight_Report.json#0d4a59c702c8, 00_Assigments.md#5418f950517f, 01_Scenario_Design.md#bb54cb161530, 01_Hardness_Manifest.draft.json#db7e2c16e5a8, 01_Gradable_Surface.json#3f1a7f7485cc, __context__#db8af19cc1c3, __assignment__#b196657eace0, __policy__#dc4ab5df3cdd, __gate_policy__#115714063000, __review__#d1d08c1c8c7d)
[PASS] structure.sections: 6 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] structure.placeholders: no placeholders in 01a_Hardening_Report.md
[PASS] structure.mode: MODE B declared
[PASS] evidence.register_run_step: 8/8 items carry a source pointer (min 100%)
[PASS] structure.sections: 4 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] revision.injection: injection checks re-run on revision N+1 (current SQL + manifest + dossier): PASS
[PASS] review.counter_readings: 9 evidenced counter-readings (of 11 found; need ≥ 9) in 01a_Hardening_Report.md
[PASS] review.coverage: self-review addresses all 2 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## 13. Next steps

1. /create-scenario --revise: disposition this register; adopt M1–M4 (or alternatives) with a design_delta; loosen the surface matchers.
2. /create-injection rev4: implement the moves, store run_forensics/rev4, re-run every gate, and run the blind fork sweep before /injection.
3. Platform: /injection on rev4, then /prompt with the same 04_Prompt.txt and the rev4 SQL, then a new Opus pre-check, then /hardness.
