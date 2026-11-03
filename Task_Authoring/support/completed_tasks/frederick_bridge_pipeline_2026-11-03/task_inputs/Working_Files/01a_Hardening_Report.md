# 01a Hardening Report: frederick_bridge_pipeline rev5 (platform Opus pre-check)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Universe: `Universe_SynthCut/`, manifest `Evals/references/universes/synthcut/universe_manifest.json`.

## 1 Mode, inputs and run validity

MODE B (pre-check). One unhinted Opus 5.5 run on the platform, plus the platform `/hardness` report on it (`Platform_Report/hardness_report1`, FAIL, score 1, "Too easy", Gate HOLD, INSUFFICIENT_DIFFICULTY).

- Inputs read: `04_Prompt.txt` (sha `cecfad824fd8`), `01_Universe_Inject.sql` rev5 (sha `3ba2b413458f`), `01_Grounding_Dossier.md`, `01_Scenario_Design.md`, `01_Hardness_Manifest.json`, `Working_Files/01_Gradable_Surface.json`, `Working_Files/solver/solver.py`, `03_Error_Async_Config.txt` (Friction: none), `06_PreCheck_Trajectory/trajectory.json` (sha `885ed68d96e2`, copied unchanged from `Run1_trajectory.json`) and the platform `/hardness` report.
- Inputs missing (not applicable to a pre-check): `07_Baseline_Trajectories/`, `10_Baseline_Verifier_Results.md`, `12_Difficulty_Stats.txt`, `08_Oracle_Events.md`, `09_Rubrics.json`.
- Run validity (`trajectory_ledger.py`, five stored revisions passed with `--sql`): `binding=BOUND:['rev5']` on discriminating content, `v3_valid=True`, `mixed=False`, `fallbacks=[]`, completed (`terminal_reason: completed`, 108 turns, one final result event 411, no compaction, no events after the result). Harness `claude-code@2.1.280`. 107 tool calls: 95 MCP calls counted plus 12 Bash. One Bash error (event 61, `jq` not installed) that the run worked around at once with python (Opus call 24).
- Proposals: `node_verdicts.py` proposed 7 verdicts (DONE1, INPUT, CORR, FILT BYPASSED; DONE2, ALIAS, FOLLOW LEAKED). I dispositioned all 7 as LEAKED. The four BYPASSED proposals come from the register decoder: it did not match the suffixed firm names ("Paul Heydon (angel)", "Homa (not on list)") or the suffixed header ("Status (as of EOD Tue Sep 30 PT)"). The write payload (Opus call 101, event 388) shows the correct value for every rule. Review coverage: I read the input of all 107 calls (`run_forensics/rev5/precheck/calls.jsonl`) and the outputs of the deciding calls 1, 3, 11, 14, 17, 18, 25, 26, 27, 30-34, 35, 40, 41-55, 56-59, 61, 62-67, 94, 97, 98 and 99-107. Calls 68-90 (status reads for list firms with no designed trap) were checked only for the thread each one opened.
- Deliverable diff (`surface_grader.py`): it scored 26.1% with failed slots V1, ST1-ST5, AC1, AC2, M1-M3, RP1, DL1. Every failed slot is a decoder miss, not a wrong value. `classes` came back all zero because the Status header carries a suffix. In the payload: SciPlay Passed, Hiro Capital Passed, Homa and Brightwater In talks, LVP Passed, Dentsu "iOS only", T-Accelerate "iOS and Android", Paul soft-circled 50000, Anton committed 25000, totals 79 / 25000 / 50000 (call 102 read-back). Reply (call 107) gives 79, $25,000 and $50,000. The sheet was created in folder `d_5e8a1c3f9b07d2e64a1b93` named "Fundraising - Oct 14 board" (call 99). The corrected surface result is every slot met, which matches the platform's requirement map R1-R13 all MET.
- Ledger: dispositioned records `hev_7f44d83eaad625e9` (DONE1), `hev_e61e07235eadbd24` (INPUT), `hev_522f1ca2bc9062de` (DONE2), `hev_1ceea0e7e912f48b` (CORR), `hev_ab2508cad060b0ac` (ALIAS), `hev_9c403cae42eb4df8` (FILT), `hev_d17e4abe74f0e7e0` (FOLLOW), all LEAKED, source `independent-harness`, model `claude-opus-5-5`.
- Posterior forecast (pre-registered, UNCALIBRATED): `hev_7b7855d894bf400b`, P(all four V3 gates) 0.023-0.184 across scenarios, E[avg] 0.830-0.855 against the Medium cap 0.85. Channel rates CH-FILT-HOMA / CH-FILT-BRIGHT set to 0.0, disclosed (this run found both).
- **Go / no-go: NO-GO.** The platform `/hardness` score is 1, there are 0 landed mechanisms and 0 failed channels (`go_rule`: 0 independent loss channels), and P(all gates) is far below 0.8. Do not spend the six-run baseline on rev5. Route to `/create-scenario --revise`. This is the first platform pre-check on this scenario; the stop rule allows one more before the scenario must change.

## 2 Gate status

No baseline exists (pre-check only), so there are no gate statistics. Corrected pre-check proxy: 100% (every slot met once the decoder misses are corrected), against the Medium cap of 85%.

## 3 Predicted /hardness band

Observed, not predicted: platform `/hardness` score 1, Too easy. The requirement map in the platform report agrees with my own read: R1-R13 all MET (template, population of 77 list rows plus Homa and Brightwater, statuses, money, build access, totals, sheet name and folder, Keep warm checklist, reply, no board mail, final answer).

Neighbouring band (2): it would need a minor defect against an authorized requirement. The only candidates are the "Basis / source" extra column and the default tab name "Sheet1", and neither the template nor the README restricts them. So band 1 stands.

## 4 Designed-difficulty register

| Rule | Mechanism · trap | Verdict | Run evidence | Deciding record | Why it did not land |
|---|---|---|---|---|---|
| DONE1 | A24 · T1 | LEAKED | Opus call 11 read the template ("Committed: signed SAFE only, meaning the DocuSign Completed notice is in"); call 35 `docusign after:2025/09/01` returned both notices; call 101 wrote Paul soft-circled | `frederick.stone@harmonygames.co/1844610859008000037` (Paul nudge) | the rule and its check sit in the record the hub points to first (template); one search returns all signing notices |
| INPUT | A11 · T4 | LEAKED | Opus call 40 listed every Fred thread Sep 2-Oct 2; call 61 opened Anton's "SAFE amount" thread; call 101 wrote 25000 | `frederick.stone@harmonygames.co/1844162278195200023` | the correction is a top-level mail in Fred's inbox inside the window the run sweeps; the template also said "use the latest amount" |
| DONE2 | A24 · T2 | LEAKED | Opus call 93 `linear_list_issues "tester TestFlight internal test"`, call 94 read the ZOM-567 comments; call 101 wrote Dentsu "iOS only" | ZOM-567 comment `lc_b549f3057640a5eb08f7581e` | the caveat ("Play internal track not added yet") is written in the done source itself, so there is no gap to find |
| CORR | A14 · T3 | LEAKED | Opus call 34 `slack_conversations_search_messages filter_in_channel #bridge-pitch filter_threads_only` returned Robert's reply; call 101 wrote SciPlay Passed; call 106 added the item | `C096HFA5Z8W/1759184040.552871` | the template named #bridge-pitch as the place phone passes are written; Robert's root message (`C096HFA5Z8W/1759161600.226431`) said the same |
| ALIAS | A7 · T5 | LEAKED | Opus call 55 read Edith Vane's mail, call 56 `contacts_search_contacts "Edith Vane"`; call 105 added Hiro Capital | contact `e3a91c07d5b48f26a0c7e314` | the template said "If the name doesn't ring a bell, check contacts"; the run did exactly that |
| FILT | A17 · T6, T7 | LEAKED | Opus call 27 listed all 190 events Sep 3-30 with attendees and descriptions; call 59 `contacts_search_contacts "Ilse"`; call 96 Slack "Homa" | `evt_2f86b0d4c9e17a35b64e0d`, `evt_89381fe5a15b802c5652a9` | one calendar listing returns every call; each person-titled event was resolved through Contacts |
| FOLLOW | A15 · T8 | LEAKED | Opus call 17 `trello_get_card actions=all` returned the rule comment; calls 103-106 wrote the checklist | Trello comment `68c64270d660c977c4696986` | the rule is on the card the hub names; it is followed once read |

Counts: LANDED 0 · CONFOUNDED 0 · LEAKED 7 · BYPASSED 0 (after disposition) · NOT-REACHED 0. Channels CH-FILT-HOMA and CH-FILT-BRIGHT: HELD (both members found; the tool printed UNOBSERVED because the decoder missed the suffixed names). Reach node never read: K12 review event `evt_9c41e7a2d05b38f6e1a7c4`. It decides nothing and the prompt names the Oct 6 date.

## 5 Per-rollout ledgers

`run_forensics/rev5/precheck/calls.jsonl` (calls), `ledger.json`, `writes.json`, `briefs.json` (no subagents). Sweep pattern, which decides where rev6 must not put a correction:
- Gmail: everything in Fred's mailbox from Sep 2 to Oct 2 (Opus calls 37 and 40, 275 messages), then thread reads by subject (calls 41-86). Nothing before Sep 2 was listed.
- Calendar: one listing of every event from Sep 3 to Sep 30 with attendees and the first 150 characters of each description (calls 27-29).
- Slack: #bridge-pitch history in full plus a threads-only search of that channel (calls 30-34); #executives history in concise form, which has no thread replies (call 97), plus a search for "invest" (call 98); keyword searches for Paul, angel, Kevin, Demetri, Fischer, iamgaming and Homa (calls 63-67, 95, 96). There were no searches for Sciplay, Anton, TestFlight or Play, and no DM was read.
- Drive and Docs: the template, the README, the list, the deck and the angels sheet (calls 7-26); "tester" and "TestFlight" searches (calls 91 and 92).
- Linear: one issue search plus the ZOM-567 comments (calls 93 and 94). Trello: the two named cards (calls 15-18). Contacts: five name lookups (calls 56-59, 88).

## 6 Friction, tool-defect and horizon checks

Friction: none (`03_Error_Async_Config.txt`). No tool defects affected the run: every write returned success (calls 99, 101, 103-107). Horizon: 107 tool calls, which just clears the Long Horizon 100+ tier. The margin is thin. rev6 must keep the call need at least as high, and moving deciding facts to services the run did not sweep raises it rather than lowering it. Call count is not hardness evidence.

## 7 Verifier sanity findings

There are no verifier results for a pre-check. The platform `/hardness` reviewer's requirement map agrees with the write payloads. Its "Unassessed" note (the 48 Not contacted rows, which were not independently re-derived) does not change the band.

## 8 Why Opus passed

```
ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md

  CLEAN      SAME_PLACE      4 trap(s) with two or more version records; 0 flagged, 0 unresolved  [Part 7 same-place check / trap 2]
  CLEAN      DONE_CHECK      an A24 / done_gap node exists  [Part 7 done check / trap 1]
  CLEAN      TWO_DECISIONS   cross-source rules decide 5 requirements: {'R3': ['DONE1', 'INPUT'], 'R4': ['DONE2'], 'R2': ['CORR', 'ALIAS'], 'R1': ['FILT'], 'R6': ['FOLLOW']}  [Part 5 rule 1]
  CLEAN      DECISION_FLIP   7 of 7 rules can flip a weight-5 slot  [Part 7 decision flip / Part 5 rule 3]
  CLEAN      INPUT_CHECK     0 weight-5 total(s); 0 with an input a rule can change  [Part 7 input check / trap 8]
  CLEAN      FILTER_CHECK    an in-scope item sits outside the obvious filter  [Part 7 filter check / trap 7]
  CLEAN      RULE_IN_PROMPT  no run of 8 resolver words in the prompt  [Part 8 / Appendix 'don't rely on rules spelled out in the prompt']
```

The static check is clean, but the run shows three v2 failure kinds the check cannot see. The rules sit in a record on the delegation path, and the corrections sit inside the containers the run sweeps whole:
- **Rulebook on the delegation path (`on_delegation_path`).** The Oct 14 template (`f_3b9e61c04d7a52e8f1a6c2`, read at Opus call 11) names the resolver of five traps: the Completed notice (DONE1), "latest amount" (INPUT), "#bridge-pitch" for phone passes (CORR), "check contacts" (ALIAS), and the speedrun, advisor and Griffin rules. One read hands Opus the checklist.
- **Corrections inside swept containers.**
  - INPUT: Anton's trim is a top-level Sep mail, returned by the mailbox listing at Opus call 40.
  - CORR: Robert's thread reply came back from the threads-only search at call 34.
  - DONE2: the Play gap is written in the done source itself (call 94), which is `same_container` in effect.
- **Bulk calls carried the population (FILT).** One calendar listing (call 27) returned every call. Contacts resolved each person-titled event.

Heavy rows (weight 5) that passed: V1 (79 firms), ST1 SciPlay, ST2 Hiro, ST3 Homa, ST4 Brightwater, M1-M3 (money), AC1 Dentsu, KW1/KW2 (Keep warm), RP2/RP3 (reply numbers). The rebuilds below must not add more rows of these kinds. They move the deciding facts instead.

## 9 Purge list (proposed; S0r decides)

- P1: the template's resolver sentences: "A pass one of us heard by phone counts once it is written in #bridge-pitch", "A partner writing from their own address counts for their firm. If the name doesn't ring a bell, check contacts and the earlier threads.", "For both, use the latest amount the investor gave us." Also drop "in writing" from Passed and trim the speedrun tail ("that has to come on our bridge thread with them or in #bridge-pitch").
- P2: Robert's #bridge-pitch root `C096HFA5Z8W/1759161600.226431` ("going to drop notes from my phone calls in the firm threads here"). It is a signpost to the CORR resolver.
- P3: Anton's top-level mail `frederick.stone@harmonygames.co/1844162278195200023` ("SAFE amount"). It is the INPUT resolver, sitting in the swept window.
- P4: the "not added yet" caveat inside ZOM-567 comment `lc_b549f3057640a5eb08f7581e`. It is the done source carrying its own missing piece.

## 10 Proposed rebuilds (Hardness v2 moves; no rows, items or steps added)

- RB1, INPUT → trap 2 + trap 8 (correction somewhere else feeding a total). Anton's change to $25K moves to Leonard's 1:1 DM with Fred (`D05S58U4SAK`, active through 2025-09-29). Two lines: Sep 24, he is voiding and resending at 25; Sep 26, Anton signed the 25 one. The #executives post (`C07C2866011/1758303600.418207`, $40K) and the Bridge angels sheet (`f_6e1d93a0c4b72f85d39a0e`, $40K) stay as the convincing stale sources. The Completed notice keeps no amount. Flips M3, M2 and RP2.
- RB2, CORR → trap 2 (correction in another service and container). SciPlay's phone pass moves from the #bridge-pitch thread to Robert's 1:1 DM with Fred (`D05SD5QSAES`). The base SciPlay thread (`frederick.stone@harmonygames.co/1842285743246816270`, last message Sep 18, friendly playtest notes) stays as the wrong source. Flips ST1, KW1 and AC (blank vs none).
- RB3, DONE2 → trap 1 (done across services). ZOM-567 becomes the believable done source: TestFlight and Play adds logged for both T-Accelerate and Dentsu. Arthur's Sep 30 message in #zombie-match3d (`C0880U9751A`, where he posts builds) supplies the missing piece: the Investor testers list was never attached to the Play internal track, and he lacks the role to attach it. A thread reply from Leonard says he'll do it from LA on Oct 1. Both firms are iOS only. Flips AC1 and AC2. The build-access definition becomes "whether they can get the current internal build".
- RB4, ALIAS → trap 6 with the hint removed. The "check contacts" sentence goes (P1). Contacts still map Edith Vane to Hiro Capital.

Each corrected fact stays settled by one dated, persona-visible record, so the platform UGT review is not reopened. That is the lesson recorded in memory `prompt-ugt-forks-need-records`.

## 11 Routing (proposed; S0r decides)

- Universe changes (to `/create-injection` rev6). Facts each change touches:
  - RB1: Anton's amount source moves (the $25K value is unchanged).
  - RB2: SciPlay's pass source moves (the Passed status is unchanged).
  - RB3: T-Accelerate build access changes from "iOS and Android" to "iOS only"; Dentsu stays "iOS only" with a new deciding record.
  - P1-P4: wording and record removals.

  Slide numbers stay 79 / $25,000 / $50,000. The Keep warm set (LVP, Hiro Capital, SciPlay) is unchanged.
- Prompt-side defects: none. The prompt does not need to change (sha `cecfad824fd8`). `/injection` and `/prompt` must still run again because the SQL sha changes.
- OE / rubric: T-Accelerate build access changes to "iOS only". Rubric and OE rows for build access, angels' amounts and SciPlay must cite the new deciding records. The downstream_notes in `run_forensics/rev5/platform/` still apply.

## 12 Self-review

| Item | Counter-reading | Resolution (evidence) |
|---|---|---|
| DONE1 LEAKED | Strongest argument that the trap was never live: the template stated the Completed-notice test, so it was solved by reading a rule rather than by discovery. | Confirmed (Opus call 11 read `f_3b9e61c04d7a52e8f1a6c2`; call 35 returned the notices). The trap was live but disarmed by the rule, so it stays LEAKED and goes to the purge list (P1). |
| INPUT LEAKED | Could it count as BYPASSED (never reached)? | No: Opus call 61 opened thread `frederick.stone@harmonygames.co/1844162278195200023` and call 101 wrote 25000. The trap was reached and settled, so LEAKED. |
| DONE2 LEAKED | Argument that it was never live: the done source carried its own caveat. | Yes (ZOM-567 comment `lc_b549f3057640a5eb08f7581e`, read at Opus call 94), so it was FALSE as a done-gap. Rebuild RB3; it is on the purge list (P4). |
| CORR LEAKED | Argument that the run met SciPlay's claim before the correction. | The run read the base thread `frederick.stone@harmonygames.co/1842285743246816270` (call 48) after the threads-only search at call 34 had already returned Robert's reply. So both orders were seen, and the template's "#bridge-pitch" pointer made the reply a first-read. LEAKED; rebuild RB2. |
| ALIAS LEAKED | Argument that Contacts were an unnatural place to look. | The template sent the run there; call 56 found contact `e3a91c07d5b48f26a0c7e314`. Natural and fair. The hint goes (P1); the alias stays. |
| FILT LEAKED | Argument that the CH-FILT channels failed (the tool printed UNOBSERVED). | The write payload (event 388) has "Homa (not on list)" and "Brightwater Games Fund (not on list)". UNOBSERVED is a decoder miss on the suffixes, so the channels HELD. |
| FOLLOW LEAKED | Argument that the checklist was wrong: SciPlay is spelled "SciPlay", not "Sciplay". | A case difference only, which the grader normalises. The items in calls 104-106 match truth `keepwarm`. |
| Band (neighbouring band 2) | Argue for score 2: the extra "Basis / source" column or the default "Sheet1" tab name. | Neither is restricted by README f_c61a0e93b7d24f58a2e917 or the template f_3b9e61c04d7a52e8f1a6c2, and the platform reviewer (hardness_report1, R8 and R9) reached the same view. Band 1 stands. No CONFOUNDED failure exists to count, and no cascade is counted twice. |
| Surface failures | Argue that the 13 failed slots are real failures. | Re-checked against the payload of Opus call 101 (event 388) in precheck.surface_grades.json and calls.jsonl, slot by slot. Every value matches solver truth.json (digest 33d88dacdb04ab89). They are decoder misses and are counted as met. |
| Run validity | Argue that the run is not valid evidence for rev5 (a mixed model, or bound to another revision). | trajectory_ledger summary.json: BOUND:['rev5'] on discriminating content (template f_3b9e61c04d7a52e8f1a6c2 and contact e3a91c07d5b48f26a0c7e314 seen); v3_valid True; no fallback or compaction. Valid. |
| Channels CH-FILT | Argue that a CH-FILT channel failed because node_verdicts printed UNOBSERVED. | The payload in writes.json has the Homa row (evt_89381fe5a15b802c5652a9) and the Brightwater row (evt_2f86b0d4c9e17a35b64e0d). Both channels HELD; UNOBSERVED comes from the decoder. |
| Harness fidelity | Argue that the platform tool surface differs from the run and would have hidden the corrections. | The run is the platform's own Opus run (hardness_report1, section 1), so the tool surface is the platform's. The deciding records came back from ordinary calls: Slack search C096HFA5Z8W (call 34) and gmail_list_threads (call 40). |

Re-verified records through `tools/hg.py` (base): SciPlay thread `frederick.stone@harmonygames.co/1842285743246816270` (7 messages, last one Sep 18 03:27Z, no pass); LVP call `evt_e59dc0a675d0c407b79acf`; SciPlay call `evt_25c9ee60d4b6c8f6d39a74`; T-Accelerate thread `frederick.stone@harmonygames.co/1842283406259093714`; LVP thread `frederick.stone@harmonygames.co/1842277743427687737`. Seeded records were re-read from the rev5 SQL text (`run_forensics/rev5/01_Universe_Inject.sql`). Calls 68-90 were reviewed only at thread level (they decide no trap).

Unresolved: none. Not reviewed in full: the outputs of calls 68-90 (status reads for list firms with no designed trap).

```
STAGE GATE hardening: PASS — Task_Authoring/task_inputs · 01a_Hardening_Report.md#d004fd076cf8 · 01_Universe_Inject.sql#3ba2b413458f · 01_Hardness_Manifest.json#310cf1471b6b · 00_Assigments.md#8ae66b700bc2 · 01_Grounding_Dossier.md#53e3be20bb54 · 06_PreCheck_Trajectory#0e517722ba45 · 07_Baseline_Trajectories#ad7848c1ad99 · 10_Baseline_Verifier_Results.md#e3b0c44298fc · __context__#f1f763cb8cb4 · __assignment__#827e8afa884d · __policy__#dc4ab5df3cdd · __gate_policy__#0fc4bb90877f · __review__#724c5240bc3b · blocking 0 · warnings 0 · checks 17
[PASS] assignment.v3_context: Frederick Stone / Co-founder; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 01a_Hardening_Report.md
[PASS] structure.inputs: 2 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 06_PreCheck_Trajectory, 07_Baseline_Trajectories, 10_Baseline_Verifier_Results.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#3ba2b413458f, 01_Hardness_Manifest.json#310cf1471b6b, 01_Grounding_Dossier.md#53e3be20bb54, solver/solver.py#181bf69d6fac, 01c_Dispositions.json#189e9a7d4b76, 01c_Preflight_Report.json#0b9187aeb605, 00_Assigments.md#8ae66b700bc2, 01_Scenario_Design.md#3d0a8e257730, 01_Hardness_Manifest.draft.json#dc72a8f7e6aa, 01_Gradable_Surface.json#3435f76f2995, __context__#f1f763cb8cb4, __assignment__#827e8afa884d, __policy__#dc4ab5df3cdd, __gate_policy__#0fc4bb90877f, __review__#724c5240bc3b)
[PASS] structure.sections: 6 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] structure.placeholders: no placeholders in 01a_Hardening_Report.md
[PASS] structure.mode: MODE B declared
[PASS] evidence.register_run_step: 7/7 items carry a source pointer (min 100%)
[PASS] structure.sections: 4 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] revision.injection: injection checks re-run on revision N+1 (current SQL + manifest + dossier): PASS
[PASS] review.counter_readings: 10 evidenced counter-readings (of 12 found; need ≥ 10) in 01a_Hardening_Report.md
[PASS] review.coverage: self-review addresses all 2 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## 13 Next steps

1. `/create-scenario --revise` takes in this report (S0r: dispositions the 7 verdicts, decides P1-P4 and RB1-RB4).
2. `/create-injection` builds rev6 with a new solver, dossier and preflight.
3. Prompt check with the brief's §4b updated; then the two blind sweeps (forks, and seeded-vs-base coherence).
4. Platform `/injection` and `/prompt` on rev6, then a new Opus pre-check run, then `/hardness`.

<!-- STAGE GATE -->
