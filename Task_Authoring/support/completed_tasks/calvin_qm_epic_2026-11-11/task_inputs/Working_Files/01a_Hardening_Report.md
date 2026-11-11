# Hardening Report — calvin_qm_epic · rev1

## 1 · Mode, inputs and run validity

MODE B (pre-check). Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Universe manifest: `Evals/references/universes/synthcut/universe_manifest.json`.

Inputs read: 04_Prompt.txt (sha256 edefd55c0ff5), 01_Universe_Inject.sql (rev1, sha256 d39581558af4), 01_Hardness_Manifest.json, 01_Gradable_Surface.json, solver/solver.py, 06_PreCheck_Trajectory/trajectory.json (sha256 7276d2d934af), the platform /hardness report (Working_Files/platform_reports/hardness_rev1_FAIL2.md). Inputs missing: 07_Baseline_Trajectories, 10 and 12 (no baseline yet), so there are no gate statistics.

- Binding: `precheck: ... valid_for_claude-opus-5-5=VALID table=NATIVE_SHEET:40 binding=BOUND:['rev1']` (sole revision). Every message is Opus 5.5 (`claude-opus-5-5`, `claude-opus-5-5[1m]`), no fallback, not mixed, 0 subagent briefs. The export has a final result event and no compaction gap.
- Counted calls: 172 by `difficulty_stats` (the platform report counts 180 with shell calls). Over the 100-call tier floor and the requester's 130.
- Proposals: 8 rule verdicts, 11 control records and 6 channel records. Dispositions: FILT changed from BYPASSED to LEAKED (the run reworded the report's title; the payload at event 469 has it); ALIAS's pending key disposed as a representation difference (a new sub-issue's key in the Ticket cell). All 25 appended to the ledger (`added 25 · already present 0 · rejected 0`).
- Review coverage: every call of the run was read (180 calls in `precheck/calls.jsonl`) and every write payload (81 writes in `precheck/writes.json`). Calls not reviewed: none.
- Deliverable diff: the local surface grader printed 62.0 % with 21 failed slots. Checked against the payloads, all 21 are decoder defects (it read only the last sheet update, the Areas tab, it keys the DM report by the solver's wording, and it expects the reply as a thread reply). Hand-reviewed result: 51 of 51 slots met, 171 of 171 weight (100 %).
- Posterior forecast: `hev_4ac7c77531cdb2e4`, pre-registered, UNCALIBRATED. E[average] 0.82 to 0.89, P(all four gates) 0.000 to 0.008.
- Call: NO-GO. The platform /hardness is 2 (needs 3 or more), 0 independent loss channels failed in Opus 5.5's own decisions (needs 2), and the corrected proxy is 100 % against a cap of 70 %. Do not spend the six-run baseline on rev1.
- Mode B diagnosis: `Working_Files/Mode_B_Diagnosis.json`, verdict PASS, evidence scope PROVISIONAL_SINGLE_PRECHECK.

## 2 · Gate status

Not applicable: no baseline exists for rev1.

## 3 · Predicted /hardness band

Observed, not predicted: the platform returned FAIL, score 2 (Easy, HOLD, INSUFFICIENT_DIFFICULTY). The requirement map there has 17 of 18 requirements MET and one MINOR_GAP (Tutorials open reports written as 4, should be 3; the same figure in child ZOM-585's description). No MATERIAL_FAIL, so 0 independent causes. Why not band 3: there is no consequential failure needing a bounded correction; why not band 1: one minor count is wrong in a secondary column.

## 4 · Designed-difficulty register

| Node | Family | Verdict | Run and step | What happened |
|---|---|---|---|---|
| BRANCH | done_gap | LEAKED | Opus pre-check · event 219; Opus pre-check · event 116 | The note names Arthur's rule; the run searched Confluence, Slack, Gmail and Drive for it over about 60 calls and read the doc at call 74. One PR listing gave #465's head branch and the chat names #1718. Rows 1, 2, 25 written Waiting on QA. |
| INLINE | done_gap | LEAKED | Opus pre-check · event 129; event 131 | The note says to check the PR and its review. The run read reviews, then review comments, of #472 and #475 at calls 41 to 44. ZOM-571 and ZOM-581 set back to Todo. |
| REOPEN | superseding | LEAKED | Opus pre-check · event 85 | The run read #zombie-bugs history since Sep 23 and opened the Sep 30 thread at call 32. Row 9 written Waiting on a fix with build 135 in the Why. |
| BACK | superseding | LEAKED | Opus pre-check · event 75 | Robert's post came back in the #zombie-match3d history read at call 29. Row 29 written Waiting on a fix. |
| ELSE | completion_elsewhere | LEAKED | Opus pre-check · event 154 | The note's sentence about a dev's own merged PR sent the run through the comments of every PR from #465 to #477 (calls 45 to 68). ZOM-572 set to In Validation, row 38 filed In Validation. |
| FILT | exact_predicate | LEAKED | Opus pre-check · event 102 | One search of every DM after Sep 25 returned Marcus's line at call 37. The report is in the sheet, filed and counted. |
| ALIAS | scope_alias | LEAKED | Opus pre-check · event 295 | A listing of ZOM tickets since Sep 10 and two issue reads (calls 91 to 94) matched ZOM-556 and ZOM-560 by title. Vincent's tying comments were never read. |
| GATE | authority | LEAKED | Opus pre-check · event 278 | One Trello search for 'review' at call 89 returned the changed card. Review list written with Level-end rewards. |

Counts over 1 completed run: LANDED 0 · CONFOUNDED 0 · LEAKED 8 · BYPASSED 0 · NOT-REACHED 0. Controls: 11 HELD, 0 OVER-APPLIED. Channels: 6 HELD, 2 UNOBSERVED (CH-REOPEN, CH-FILT; the tool could not key them, the payloads show both held).

## 5 · Per-rollout ledger

Full ledger: `run_forensics/rev1/precheck/calls.jsonl` (180 calls), `writes.json` (81 writes), `briefs.json` (0). Shape of the run:

| Calls | What it did | Result |
|---|---|---|
| 1–7 | profile, Slack search 'Queue Manager', Brian's DM, ZOM-543 and its comments | the note read at call 7 (event 15) |
| 8–27 | pass sheet, legend, and a hunt for Arthur's rule through Confluence, Slack, Gmail, Drive | sheet and legend read; rule not yet found |
| 28–38 | history of #zombie-bugs, #zombie-match3d and one more ZM channel since Sep 23, the Sep 30 thread, all DMs after Sep 25, the QA chat | both come-backs, Marcus's report and the #1718 line |
| 39–68 | one PR listing, then reviews, review comments and conversation comments of #465 to #477 | Arthur's two comments and Oliver's comment |
| 69–88 | more searches for the rule, Arthur's Drive files, the rule doc, #builds history in three pages | the rule and every build's branch and time |
| 89–96 | Trello search, calendar search, ZOM tickets since Sep 10, ZOM-555/556/560, states | the card, the attendees, the two older tickets |
| 97–180 | 10 children, 20 moves, 20 notes, 19 sub-issues, sheet with two tabs, 5 shares, slide, DM | every write succeeded |

## 6 · Friction, tool defects and horizon

Friction: none configured (03_Error_Async_Config.txt). Unconfigured tool errors: oversize tool outputs spilled to files and were read back with shell calls; one `user_not_found` search; none changed an outcome. Horizon: 172 counted calls, above the Long-Horizon floor of 100 and the requester's 130. About 84 calls are writes.

## 7 · Verifier sanity

No rubric or verifier exists yet, so there is nothing to check.

## 8 · Why Opus passed

`hardness_v2_check` on rev1: SAME_PLACE CLEAN (4 traps with two or more version records; 0 flagged), DONE_CHECK CLEAN, TWO_DECISIONS CLEAN, DECISION_FLIP CLEAN (8 of 8 rules), INPUT_CHECK CLEAN, FILTER_CHECK CLEAN, RULE_IN_PROMPT CLEAN. The tool reads the prompt, not the delegated note, so it could not see the cause below.

- **Rules written into the request's delegate.** Brian's note states each resolver as a check: 'check the PR ... if the review on it says a fix is not in there', 'if the dev wrote on a merged PR of theirs', 'unless somebody says later, on a build made after that one, that it is back', 'a ticket under another name', 'told you about in a DM since ... the 26th', 'Leonard's review card'. Each trap became a lookup the run was told to make (INLINE, ELSE, REOPEN, BACK, ALIAS, FILT, GATE). This is the Part 8 pattern, one hop away from the prompt. The sentences were added to close forks for /prompt; they closed the difficulty too.
- **Swept containers.** Both come-backs and the DM report were dated Sep 30 in places the run read whole (`first_read` in effect): two channel histories, one thread, every DM.
- **Bulk calls.** One PR listing with head branches, one Trello search, one ticket listing.
- **Genuine capability.** Finding Arthur's rule took about 60 calls with no pointer beyond his name. Persistence is not a weakness to design against.
- **What the run never opened:** the comments of any ticket other than ZOM-543 (26 seeded notes unread), any Trello action history, any mail thread beyond a sender search.

Heavy rows (weight 5) that passed: all 21 (V1 to V4, V7, B1 to B3, B5, R1, K1B, K3B, I1, I4, E1, E2, F1, A1, A2, G1, G2). Status lookups on signposted checks and the five totals are what Opus found easy; a rebuild must not add more of them.

## 9 · Purge list (proposed; S0r decides)

| Item | Proposal | Evidence |
|---|---|---|
| Resolver sentences in Brian's note | purge (keep plain definitions) | event 15; platform /hardness score rationale |
| Come-backs as a Sep 30 channel post and thread reply | rebuild off the swept path | events 75, 85 |
| ALIAS as a title match | rebuild or demote to weight 3 | event 295: matched without the tying comments |

## 10 · Proposed rebuilds (Hardness v2 moves only)

Ledger evidence for Opus 5.5 before this run: superseding 0 landed of 10, authority 0 of 3, completion_elsewhere 0 of 3, scope_alias 0 of 2; done_gap 2 of 5, exact_predicate 1 of 5, boundary_date 1 of 1. rev1 leaned on the families that do not land.

1. **RP1, placement.** Cut the resolver sentences from the note. The facts already settle rows 12, 32, 13 and 38; nothing should tell the reader to go and check them.
2. **RP2, placement and a control.** Record one come-back as a comment on the report's own ticket, where this run never read, and add one 'it is back' on a build older than the pass, which leaves the pass standing (the platform report's suggestion 2: Android #2006 is older than iOS Internal #1745).
3. **RP3, done source with a missing piece (A24).** Make 'merged' and 'on a main build' two separate checks per row: a re-test recorded before the fix merged, or a fix merged into a branch that is not main.
4. **RP4, placement.** The note names the review's agenda, not Leonard's card; the updated invitation leads to the card.

None adds rows, items, steps or prompt rules. Each changes which records decide existing weight-5 rows.

## 11 · Routing (proposed; S0r decides)

- Universe: RP1 to RP4 go to `/create-scenario --revise` from S5a, then `/create-injection` as rev2, then `/injection` and `/prompt` again. Facts that would change: the text of Brian's note, where and on which build the two come-backs are reported, one or two rows' re-test and fix cells, and possibly the five totals.
- Prompt: no prompt-side defect. The prompt can stay as it is unless rev2 changes a deliverable phrase.
- Rubric: accept the reply as a new DM message or a thread reply; accept a count or a list in 'Open reports' and any share role (platform /prompt notes).
- Fork risk: every sentence cut from the note must leave its row settled by a dated record, or /prompt will reopen the fork. A blind fork sweep on rev2 is required before /injection.

## 12 · Self-review

| Verdict | Counter-reading (was the trap ever live?) | Resolution | Result |
|---|---|---|---|
| BRANCH leaked | The rule doc was the first hit, so nothing was hidden. | It took until call 74 (event 219), after Confluence, Slack and Gmail searches; the claim 'ok, chat' was met at call 12, long before. Live, and beaten by persistence. Re-verified through hg.py: C05433XK267/1758817549.151639 names the QueueManager branch. | stands |
| INLINE leaked | The review comment came back in the same call as the approval. | The approval (get_reviews, calls 41 and 42) has an empty body; the comment needed a second call per PR (event 129). Live; the note's sentence caused the second call. Record: harmonygames-Games/match3d#472#rc_1. | stands |
| REOPEN leaked | The reply was in an anchor's thread. | It is under a Sep 30 shader thread in #zombie-bugs, not an anchor; the run opened it because it read the whole channel window (event 85). Live, on a swept path. Record: C08R27X0EAH/1759267212.418339. | stands |
| BACK leaked | A bulk read carried it. | Yes: the #zombie-match3d history at call 29 (event 75). The claim (ok on #1750, sheet at call 12) was met first. Live but first-read in effect. Record: C0880U9751A/1759268652.552719. | stands |
| ELSE leaked | The comment was on a PR the sheet names. | The sheet names no PR for rows 13 and 38; the run reached #473 only by reading every recent PR's comments (event 154). Record: harmonygames-Games/match3d#473#c_2. | stands |
| FILT leaked | The tool said BYPASSED. | The payload at event 469 lists the report under Season Pass, Waiting on a fix; found at event 102. Disposed as leaked. Record: D05U73FNDDL/1759252212.611349. | changed from the proposal |
| ALIAS leaked | The tying comments were never read, so the trap was not traversed. | The run reused ZOM-556 and ZOM-560 on titles alone (event 295); the outcome is right, so it is a leak through a title match, not a bypass of the outcome. Records: ZOM-556, ZOM-560. | stands |
| GATE leaked | The older agenda was never met. | Brian's Sep 29 line is in the DM read at call 5, before the card at call 89 (event 278). Live. Records: D0770ET6WBW/1759164072.337219, 68daad83bacf52c6ea7e1593. | stands |
| 0 landed overall | A landing could hide in a payload the tools misread, as the 21 decoder failures suggest. | Each of the 21 was opened in writes.json: the Reports tab at event 469 has all 39 statuses right, ZOM-571 and ZOM-581 are set to Todo at events 351 and 375, ZOM-572 to In Validation at event 353. | stands |
| Controls held | A control could have been over-applied without the tool keying it. | Rows 17, 18, 31 and 33, which share #472 and #475 with the two held rows, are written Passed, Waiting on QA, Passed, Passed; ZOM-576 keeps In Validation. | stands |
| Band 2 | Band 3: the wrong Tutorials count is a consequential failure. | It is one cell in a secondary column; the five numbers, every status and every state are right, and the platform scored 2. Neighbouring band 1 would also be defensible. The wrong figure is also in child ZOM-585. | stands |

Re-verified through hg.py in this task: the #1718 build post and the persona's visibility of the deciding base records (persona_view can-see YES). No CONFOUNDED verdict: no tool, fairness, verifier or run cause was found. Unresolved: one run is an observation, not a rate; the redesign is unproven until a new pre-check.

```
STAGE GATE hardening: PASS — Task_Authoring/task_inputs · 01a_Hardening_Report.md#35ccd8634d0f · 01_Universe_Inject.sql#d39581558af4 · 01_Hardness_Manifest.json#2804c8e07613 · 00_Assigments.md#a8cc00ce24ff · 01_Grounding_Dossier.md#e0d911e3041d · 06_PreCheck_Trajectory#8d14f0f32fa6 · 07_Baseline_Trajectories#ad7848c1ad99 · 10_Baseline_Verifier_Results.md#e3b0c44298fc · __context__#7be566a0936c · __assignment__#d644f7ef43f6 · __policy__#dc4ab5df3cdd · __gate_policy__#a392988e72d3 · __review__#15d71f843716 · blocking 0 · warnings 0 · checks 19
[PASS] assignment.v3_context: Calvin Price / Game Engineer (Unity VFX); hard cap <70%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 01a_Hardening_Report.md
[PASS] structure.inputs: 2 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 06_PreCheck_Trajectory, 07_Baseline_Trajectories, 10_Baseline_Verifier_Results.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#d39581558af4, 01_Hardness_Manifest.json#2804c8e07613, 01_Grounding_Dossier.md#e0d911e3041d, solver/solver.py#bb49c8c092af, 01c_Dispositions.json#74ef4a68f46d, 01c_Preflight_Report.json#68e06e62c1f7, 00_Assigments.md#a8cc00ce24ff, 01_Scenario_Design.md#758a7ae97892, 01_Hardness_Manifest.draft.json#96e1b33608ff, 01_Gradable_Surface.json#8ddf2179ea1c, __context__#7be566a0936c, __assignment__#d644f7ef43f6, __policy__#dc4ab5df3cdd, __gate_policy__#5b7d4d20094d, __review__#2f0bc48e3642)
[PASS] structure.sections: 6 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] structure.placeholders: no placeholders in 01a_Hardening_Report.md
[PASS] structure.mode: MODE B declared
[PASS] evidence.register_run_step: 8/8 items carry a source pointer (min 100%)
[PASS] structure.sections: 4 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] revision.injection: injection checks re-run on revision N+1 (current SQL + manifest + dossier): PASS
[PASS] review.counter_readings: 11 evidenced counter-readings (of 11 found; need ≥ 11) in 01a_Hardening_Report.md
[PASS] review.coverage: self-review addresses all 2 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] readiness.context: explicit task/revision and current upstream evidence verified
[PASS] readiness.mode_b: PROVISIONAL_SINGLE_PRECHECK: current structured diagnosis
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## 13 · Next steps

1. `/create-scenario --revise` to disposition these verdicts and decide RP1 to RP4.
2. `/create-injection` for rev2, with a blind fork sweep and a blind coherence sweep before the gate.
3. Platform `/injection`, then `/prompt`, on rev2.
4. A new Opus pre-check and `/hardness`. Stop rule: at most two platform pre-checks per scenario; this was the first.
