# Hardening Report — samuel_zm_beta_messages · rev5 · MODE B (pre-check intake)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Universe manifest: Evals/references/universes/synthcut/universe_manifest.json. Platform reports quoted: run_forensics/rev5/hardness_report_FAIL_2.md (FINAL VERDICT: FAIL, Score 2, HOLD), prompt_report_NONFAIL_3.md (NON-FAIL 3) and injection_report_PASS.md (PASS). Each carries the Clock line above.

## 1. Mode, inputs and run validity

MODE B (pre-check). One Opus 5.5 trajectory from the platform pre-check, stored at 06_PreCheck_Trajectory/trajectory.json (sha256 d0dfd1e26bf1, session e0cfa0c6-c82d-4993-be4c-0ca672fa5311; ledgers in run_forensics/rev5/precheck/). The platform's copy hashed 36dde045066c. The file differs by bytes, not content: the session id, 188 calls and 189 turns all match the report.

- **Inputs read:** 00_Assigments.md, 01_Universe_Inject.sql (rev5, c40a78a9db79), 01_Grounding_Dossier.md, 01_Hardness_Manifest.json, 01_Scenario_Design.md, 04_Prompt.txt (22df2abfec65), 03_Error_Async_Config.txt (Friction: none), 01_Gradable_Surface.json, solver/solver.py, the five stored revisions, and the three platform reports.
- **Inputs missing:** none for a pre-check intake. There are no baseline files yet, so no gate statistics.
- **Validity** (trajectory_ledger.py): stream-json, completed (subtype success, 189 turns), no compaction, no events after the result, no unpaired calls.
- **Models:** claude-opus-5-5 on every message (init label claude-opus-5-5[1m]). mixed_model false, v3_valid true, no fallback, no subagents (briefs 0).
- **Binding:** BOUND to rev5 on discriminating content. Leonard's rev5 line "No bonus ad is live today" came back at opus · event 95, read through linear_list_comments on DES-346.
- **Prompt match:** by content. The run opened Leonard's DM D06L58XCVKK at opus · event 6.
- **Counted calls:** 185 (raw 188: 2 harness Bash calls, 1 blocked call, 0 repeats). The requester asked why "23" appeared: 23 is the run's Hold count, not its call count.

Pre-check intake results:
1. **Binding:** BOUND rev5, valid for claude-opus-5-5. Mixed-model flags: none.
2. **Proposals:** node_verdicts gave 18 proposals (8 verdicts, 5 controls, 5 channels). All 18 were dispositioned in run_forensics/rev5/precheck.dispositioned.jsonl. The review queue was empty. Three proposals were corrected: DEP and ALIAS read BYPASSED only because the run named its rows "Finish first mission (FTUE)" and "Win & Collect / Collect & Win window opens"; FILT read BYPASSED because its rows are absent, which is the designed miss.
3. **Deliverable diff** (surface_grader): raw 75.4%. Confirmed against the write at opus · event 335, only X11, X12, X13 and V1 are genuine, so the corrected surface score is 91.3% (16 of 183 weight lost). The other 7 failed slots are decoder strictness (§6). The platform's own estimate is about 90%.
4. **Ledger:** 18 records appended (added 18, rejected 0).
5. **Posterior forecast** (pre-registered, UNCALIBRATED): hev_385994d021e60318. With rates taken from this run, E[avg] 0.886 [0.855, 0.914], P(all gates) 0.00–0.02 across dependence scenarios. Rev5 cannot clear the requester's 80% bar or the 85% cap.
6. **Go / no-go: NO-GO.**
   - /hardness is 2 (needs 3 or more).
   - One independent loss channel failed in Opus's own decisions (FILT), against a need of 2.
   - The tool's CH-SLIP count was representational and is dispositioned HELD.
   - Route: /create-scenario --revise. This was pre-check 1 of the 2 allowed for this scenario (stop rule).

## 3. Predicted /hardness band (B3c)

| Requirement | Outcome | Citation |
|---|---|---|
| R1 population (35 messages) | MATERIAL_FAIL: 33 written, ZOM-542 and ZOM-556 asks missing | ZOM-556 returned at opus · event 137 (linear_list_issues), its comments never read; ZOM-542 never returned; sheet at opus · event 335 |
| R2, R3 calls on the 33 covered | MET | sheet at opus · event 335, comments from opus · event 373 |
| R4 headline and string | MET | Leonard's reply opened at opus · event 231, ticket DES-347 at opus · event 328 |
| R5 note | MET | D1 and D7 from opus · event 308, schedule from opus · event 165 |
| R6 comments, R7 states | MET for 33, two tickets absent | Backlog moves from opus · event 456 |
| R9 delivery | MET with a knock-on: Hold 23 in the DM, two emails short | DM at opus · event 520 |

Observed band: **2, Easy.** The band table alone gives 3, but the platform's narrow-miss rule caps it: one independent cause and a failed share (about 10%) under Medium's 15% loss. That rule is in the report, not in the local Evals text. Neighbour 3 needs a second independent cause or a share of 15% or more. Neighbour 1 does not fit, because the miss is real and consequential.

## 4. Designed-difficulty register (per-node counts out of 1 run)

| Node | Mechanism | Verdict | Counts (landed · confounded · leaked · bypassed · not-reached) | Evidence (opus · event) | v2 failure kind |
|---|---|---|---|---|---|
| FILT ZOM comment asks | A17 exact predicate | LANDED | 1 · 0 · 0 · 0 · 0 | ZOM-556 listed at opus · event 137, no linear_list_comments on any ZOM ticket; sheet at opus · event 335 has 33 rows | landed as an omission outside the DES-314 filter |
| DONE Weekly Leaderboard | A24 done gap | LEAKED | 0 · 0 · 1 · 0 · 0 | NotificationManager.cs read at opus · event 165; rc_18 never returned | a bulk read carried the answer: the source shows i * 7 days from today |
| CORR Lapsed 7 headline | A11 superseding | LEAKED | 0 · 0 · 1 · 0 · 0 | from: search at opus · event 226, thread at opus · event 231 | on_delegation_path: the rule says "the latest line I've called", so the run searched Leonard's posts |
| DEP Finish first mission | A4 join | LEAKED | 0 · 0 · 1 · 0 · 0 | search "permission ask" at opus · event 161, source at opus · event 165, requester at event 166, threshold at event 269 | on_delegation_path plus source: the rule's own words found the post, and the code alone shows ask after 20, message below 20 |
| QA Plague Race | A14 superseding | LEAKED | 0 · 0 · 1 · 0 · 0 | "iPhone" cell at opus · event 202, search "store build" at opus · event 207 | a visible caveat: the one row without a build number sent the run looking |
| ALIAS Win & Collect | A7 scope alias | LEAKED | 0 · 0 · 1 · 0 · 0 | search "Win Collect" at opus · event 142, DES-313 read at opus · event 150 | the name search found it |
| BUILT Lapsed 14 days | A25 completion elsewhere | LEAKED | 0 · 0 · 1 · 0 · 0 | source at opus · event 165; the calendar note never read | a bulk read carried the answer |
| FOLLOW Hold to Backlog | A15 amendment | LEAKED | 0 · 0 · 1 · 0 · 0 | commentCard listing at opus · event 113, applied from opus · event 456 | on_delegation_path: "unless the roadmap says otherwise", and one call lists every comment on the board |

**Controls** are all HELD. **Channels:** CH-DONE, CH-CORR, CH-QA and CH-BUILT HELD; CH-SLIP proposed FAILED, dispositioned HELD (§6).

## 5. Per-rollout ledger (precheck)

Stored per call in run_forensics/rev5/precheck/calls.jsonl. Summary of 188 calls:

- **Reads, calls 1 to 102:** Slack 16 (3 threads, 7 searches, 1 channel read); Linear 36 (33 linear_list_comments); Trello 11 (4 trello_get_board_actions, 4 trello_search); GitHub 16; Drive 8; Sheets 4; Gmail 3; Docs 1; Slides 1; Snowflake 3; Confluence 1; Bash 2.
- **Writes, calls 103 to 188:** 84 named writes: 33 comments, 31 ticket updates, 7 emails, 4 checklist calls, 1 ticket, the sheet, the note, the DM.
- **Slack search terms:** "permission ask", "from:Leonard headline", "QA note", "store build", "headline", "from:Leonard" (limit 100), "push". No search for any message name, and none for Vincent's posts.
- **Never touched:** gcal (0 calls), trello_get_board, comments on any ZOM ticket, GitHub review comments, Slack channel history other than the DM.

## 6. Friction, tool-defect and horizon checks

- **Friction:** none configured. One blocked call: trello_get_card with attachments "true" at opus · event 107 returned invalid_value. The run did not retry and moved on, so it never read the push card's checklists.
- **Horizon:** 185 counted, above 130 and above the 100 floor. This is one run; the six-run minimum is unproven. The write floor alone is about 85.
- **Decoder strictness, confirmed against opus · event 335 and not counted as failures:** X5 and X6 (row "Finish first mission (FTUE)"), X9 and X10 (row "Win & Collect / Collect & Win window opens", ticket on DES-313), K3 (row "Axe Arena start"), K14 (row "Boss Arena is open"), X16 ("Yes - DES-347 ..." in String change). Routed to S0r: the surface key matcher should take the sheet's row names.

## 7. Verifier sanity

No verifier run exists at pre-check. Nothing to route.

## 8. Why Opus passed

```
hardness_v2_check (advisory): SAME_PLACE, DONE_CHECK, TWO_DECISIONS, DECISION_FLIP, INPUT_CHECK, FILTER_CHECK, RULE_IN_PROMPT all CLEAN
```

The tool passed every check, and the run still solved 8 of 9 traps, so the tool's clean table is not evidence of difficulty. The real causes, from the call ledger:

1. **The rule doc says where to look.** "The permission ask is Robert's call", "the latest line I've called" and "unless the roadmap says otherwise" each became a search or a read at opus · event 161, opus · event 188 and opus · event 113.
2. **The client source answers three traps by itself.** One read at opus · event 165 settled DONE, DEP and BUILT. The seeded notes behind them (rc_18, the calendar note) were never opened.
3. **One visible caveat.** "iPhone" in place of a build number at opus · event 202 pointed straight at the Plague Race correction.
4. **A found answer stops the search, but only one existed.** The run hunted the headline until it found the Sep 29 reply. Nothing later overrode it.
5. **Board-wide reads.** trello_get_board_actions with filter commentCard returned every roadmap comment at opus · event 113, so a card comment is effectively on the path. The platform's suggestion of a card-comment ask would have been caught here.

Heavy rows that passed, so do not add more of them: every per-ticket call decided by Arthur's comments, every rule the doc names, the note's figures, the checklist, the 33 comments and 30 moves.

Across 54 stored Opus runs on all tasks: trello_get_board 4 of 54, gcal at least once 35 of 54 (0 in this run), slack from: searches 9 of 54, linear_get_issue 22 of 54. Runs asked for card desc when listing cards.

## 9. Purge list (proposed; S0r decides)

None. Every node stays. FOLLOW, QA and CORR are rebuilt rather than purged. DONE, DEP, ALIAS and BUILT stay as honest decisions that do not count as difficulty.

## 10. Proposed rebuilds (Hardness v2 moves)

Each move relocates or deepens a correction, or moves an item outside the filter. Delegated by the requester ("you can choose from your self which option is best fit").

| Move | Change | v2 move | Reach used | Estimated catch (UNCALIBRATED) |
|---|---|---|---|---|
| M1 QA | Plague Race reads like every other pass on the sheet and ticket; Vincent's reply drops "store build" | removes a visible caveat, moves the correction off the search path | no caveat, so no reason to hunt | 0.25–0.50 |
| M2 PULL | Vincent takes his tick off Lives recharged after the 0.3.49 iOS release, in a #zombie-match3d post | a correction elsewhere that flips a Go; Part 3 trap 2 | no search for Vincent's Slack posts or message names at opus · event 207 or later | 0.30–0.55 |
| M3 CORR | A later calendar note replaces the Sep 29 line, so the found answer is stale | a correction of a correction in a service the run skipped | 0 gcal calls | 0.30–0.60 |
| M4 FOLLOW | The Hold rule moves from a card comment to card 79's description | moves a correction out of the bulk comment listing | card desc is read only if the run asks for it and notices the sentence | 0.45–0.75 |
| M5 FILT | Two more comment asks outside the filter, on ZOM-563 and ZOM-483, one from a new asker | the one mechanism that landed, made heavy enough that this exact miss clears the 15% line | no ZOM comment read at opus · event 137 | 0.25–0.55 |

M2 changes truth: Go 2, not 3. M5 adds two rows and one asker. Totals become 37 messages, Go 2, Hold 28, Drop 7, 8 askers, 5 new tickets. The prompt and Leonard's DM do not change.

## 11. Routing (proposed; S0r decides)

- **Universe changes:** M1 to M5, plus SC-13: one Trello updateList action renaming the list to "BETA: Oct 10", from the /prompt report's Recommended Improvement 1. It lifts Cross-Service Coherence from 3.
- **Prompt-side defects:** none. The prompt stays 22df2abfec65.
- **Surface:** the key matcher fix from §6.
- **OE and rubric:** keep the carried limits (no server-push claim, no D14 or later, no beta date, no card completion flags). The rubric should put weight 5 on the rows a miss decides, including the Go list, and treat the two Vincent corrections as separate rows.

## 12. Self-review

Walked Evals/1A_Hardness_Eval.md §3–§5 against this report. Re-verified through tools/hg.py in this run: "0.3.49" (slack, 3 hits: Leonard's posts in C0880U9751A and C07C2866011, a dashboard link), "Full Ammo" (slack, 0 hits, scan complete), "Your Squad" and "Squad Is Waiting" (slack, 0 hits), "Squad" (gcal, 0 hits), "Infinite lives from new-install" (linear /issues/3554), "Teams' lives" (linear /issues/3640). Seeded texts were read from 01_Universe_Inject.sql.

| Verdict | Counter-reading | Evidence that resolves it | Result |
|---|---|---|---|
| FILT LANDED | Strongest tool case: the asks never reached the run | ZOM-556 was returned at opus · event 137. Comments need linear_list_comments, which the run called 33 times on other tickets. The platform calls it discoverable (hardness_report_FAIL_2.md, Task/environment defects) | stays LANDED |
| FILT LANDED | Fairness: a comment on a bug is not an ask "filed on a ticket" | /prompt settled it at F4 in prompt_report_NONFAIL_3.md, and the DM says "a ticket or a card" | stays LANDED |
| DONE LEAKED | The trap was never live, so it is FALSE | It was live against the sheet and DES-320, but the source read at opus · event 165 settles it, and harmonygames-Games/match3d#248#rc_18 was never opened. Kept as an honest decision, not counted as difficulty | LEAKED, keep |
| CORR LEAKED | The Sep 29 reply was on the delegation path, so a stronger hiding place only hides it | Confirmed by the from: search at opus · event 226, which returned C08R8CHB0QL/1759169129.445834. M3 keeps the reply as the found answer and adds a later record, which is v2 trap 2 | LEAKED, rebuild M3 |
| DEP LEAKED | Rewording Robert's post would hide it | No: the run read the join from code at opus · event 165, opus · event 166 and opus · event 269, so rewording C0880U9751A/1759167608.326578 does nothing. Left alone | LEAKED, keep |
| QA LEAKED | It leaked through search, so only wording matters | The search at opus · event 207, which returned D06UFE81RF0/1759174846.723833, came right after the "iPhone" cell at opus · event 202. The caveat caused the search, so M1 changes both | LEAKED, rebuild M1 |
| ALIAS LEAKED | A bulk call carried it | Search at opus · event 142 returned DES-313 by name. Kept as a decision row | LEAKED, keep |
| BUILT LEAKED | It is FALSE because the code shows it | DES-344 still reads as new work and the rule needs the Drop. Settled by source at opus · event 165, kept, not counted as difficulty | LEAKED, keep |
| FOLLOW LEAKED | The doc's clause is the leak, so remove it | The clause in f_dc45e0e5a8b8635c1b82b2 carries the authority chain /prompt relies on (prompt_report_NONFAIL_3.md, Compared alternative B). Removing it would risk UGT, so M4 moves the record and keeps the clause | LEAKED, rebuild M4 |
| Band | Neighbouring band 3: the wrong Hold count, the two emails and the two tickets are more causes | All trace to one cause, ZOM-542 and ZOM-556, at opus · event 335. The platform counts one independent cause and I agree: no cascade counted as several | stays 2 |
| Rebuild risk | M5 adds rows, which Part 8 warns against | Part 8 warns against rows that add no decision. These sit outside the filter and carry their own call, and the platform's own advice asks for an item outside the filter. Counted as one cause, not four | accepted, watch /hardness wording |
| Rebuild risk | M2 could fail /prompt UGT because older passes on 0.3.40 might also be in doubt | Vincent's post says the lapsed ones still come through, and the rule's test is his own record, as in F12 of prompt_report_NONFAIL_3.md | accepted, blind sweep before sealing |

Unresolved:
- The catch rates in §10 are estimates (UNCALIBRATED). My rev5 forecast of 0.82 missed the observed 0.90 by more than its stated band, so treat them as weak.
- The stop rule allows one more pre-check for this scenario. If rev6 also scores 1 or 2, the scenario changes.
- The surface key matcher fix is routed to S0r.

```
STAGE GATE hardening: PASS — Task_Authoring/task_inputsK · 01a_Hardening_Report.md#78482c593d15 · 01_Universe_Inject.sql#c40a78a9db79 · 01_Hardness_Manifest.json#76e3b7b1f42f · 00_Assigments.md#55f6d8057880 · 01_Grounding_Dossier.md#f5bb7a893f35 · 06_PreCheck_Trajectory#c872ed1a1685 · 07_Baseline_Trajectories#ad7848c1ad99 · 10_Baseline_Verifier_Results.md#e3b0c44298fc · __context__#72168f70a409 · __assignment__#3adec6ac02d7 · __policy__#dc4ab5df3cdd · __gate_policy__#115714063000 · __review__#95f1481dfb3c · blocking 0 · warnings 0 · checks 17
[PASS] assignment.v3_context: Samuel Turner / Game Designer; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 01a_Hardening_Report.md
[PASS] structure.inputs: 2 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 06_PreCheck_Trajectory, 07_Baseline_Trajectories, 10_Baseline_Verifier_Results.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#c40a78a9db79, 01_Hardness_Manifest.json#76e3b7b1f42f, 01_Grounding_Dossier.md#f5bb7a893f35, solver/solver.py#bbbfd7b46935, 01c_Dispositions.json#5ed896e5a280, 01c_Preflight_Report.json#2ff52ae9114a, 00_Assigments.md#55f6d8057880, 01_Scenario_Design.md#5875dab9e40a, 01_Hardness_Manifest.draft.json#f99a946ff76f, 01_Gradable_Surface.json#f3e17a36d4e1, __context__#72168f70a409, __assignment__#3adec6ac02d7, __policy__#dc4ab5df3cdd, __gate_policy__#115714063000, __review__#95f1481dfb3c)
[PASS] structure.sections: 6 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] structure.placeholders: no placeholders in 01a_Hardening_Report.md
[PASS] structure.mode: MODE B declared
[PASS] evidence.register_run_step: 8/8 items carry a source pointer (min 100%)
[PASS] structure.sections: 4 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] revision.injection: injection checks re-run on revision N+1 (current SQL + manifest + dossier): PASS
[PASS] review.counter_readings: 11 evidenced counter-readings (of 12 found; need ≥ 9) in 01a_Hardening_Report.md
[PASS] review.coverage: self-review addresses all 2 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## 13. Next steps

1. /create-scenario --revise takes in these verdicts and applies M1 to M5 and the SC-13 action.
2. /create-injection rebuilds the SQL as rev6, with a blind fork sweep before sealing.
3. The requester re-runs /injection, /prompt, one new Opus pre-check and /hardness.
