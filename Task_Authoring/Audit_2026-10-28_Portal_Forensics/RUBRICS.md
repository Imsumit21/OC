# Rubric semantics, facts, scoring and repair forensics

Audit date label: 2026-10-28. Scope: preserved external rubric reports, their exact reviewed JSONs, source evidence, repair histories, authoring instructions and actual validator code. This audit ran no evaluation, stage gate, SQL, browser, mailbox operation or outreach; it changed only this new report and its scratch inventory. Reading SQL below means reading its text, never executing it.

## Findings that explain the repeated failures

1. **The initial failures were substantial artifact defects, not merely evaluator noise.** Reviewer A's first 41-row export bundled actions and facts, omitted two outcomes, graded a distractor and contained 18 preserved-state/exclusion rows that passed an idle agent. Oliver's first 41-row export missed 26 outcomes. Douglas's first 52-row export missed 18 per-ticket results. All three reports provide concrete incorrect/omitted-result witnesses. Later versions closed most of these defects. Sources: `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_12_rubric_portal_20261025/6ad90e93a2c3542255f64fbf_3_rubric.md:39`, `Task_Authoring/task_inputs-skipped/Plateform_reports/01_Rubrics.md:55`, `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_3_rubric.md:61`.
2. **Narrow repairs repeatedly created new acceptance defects in the same field.** Reviewer A R22 moved from bundled conditions to a semantic payment need, then a $25K-payable hole, then an annual/full-year synonym split. Reviewer B R27/R29 repeatedly mixed current status with history, aliases, headings, count units and layout. Those are real distinct predicates, and a correct source fact does not make their wording deterministic. The report histories explicitly distinguish fixed old defects from newly introduced ones.
3. **One recurrence is a proven incomplete repair.** Reviewer B's Brian mention was fixed only in `evidence`, leaving the defective `title` and weight untouched. The next report says exactly this; it is not an evaluator moving its target. Source: `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_26_latest_rubric_repair/received/6ad90e9449d1194f4e538cdf_3_rubric (7).md:128`.
4. **The evaluator also caused repair churn.** Its latest Reviewer B external report explicitly admits that its previous instruction to accept any name/paraphrase caused the next self-containment failure: “That was my error in last run's guidance, not yours.” This is unusually strong direct evidence of a bad repair recommendation. Source: `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_30_rubric_alias_repair/received/6ad90e9449d1194f4e538cdf_3_rubric (11).md:134`.
5. **Authoring policy, local gates and external review do not describe the same acceptance contract.** The local playbook still predicts QC percentage bands, while the actual evaluator entrypoint says any Major or Moderate fails. Reports also use sibling-title acceptance and Minor overly-broad findings contrary to the local title-only/Moderate rules. Different release hashes and review contexts make some discrepancies version drift rather than a proven same-version evaluator bug. Sources and distinctions are detailed below.
6. **More independent reviewers alone has not solved this.** The external reports already claim R1–R7, multiple fix-check rounds and, on first runs, three independent full reviews. Later local repairs also preserve independent reviewers and dozens of manual cases. What is missing is a stable, source-bound acceptance contract with frozen counterexamples and field-level repair closure, rather than another unstructured review pass.

Confidence: high on exact bytes, report verdicts, static code behavior and explicit admissions; medium on why model reviewers failed to anticipate a new wording case; unresolved on unseen Portal state or unpreserved reports.

| Attribution | Established cause | Confidence / contrary evidence |
|---|---|---|
| Artifact | Missing per-target outcomes, non-atomic bundles, conflicting alias/count/status clauses | High: exact exported rows and concrete report witnesses; substantial repairs later close them. |
| Workflow | Reviewer B R44 repaired in wrong field; report-only proposals continue with unresolved formal prep/bindings | High: explicit diffs/reports and real failed gate logs; handoffs disclose the limits rather than fabricating a PASS. |
| Pipeline | Policy bands/context, canonical slot and reviewed candidate are separate or stale | High: implementation, contexts and hashes; no proof that a historical local certificate falsely passed bad semantics. |
| Evaluator | Bad alias advice and same-line/scope restrictions introduce later defects | High for quoted recommendations/admission; medium for broader unfairness because versions and witness layouts differ. |
| Hypothesis | Correlated reviewers or case overfitting explain missed new ambiguities | Plausible, unproved: independent traces and judge executions are not preserved. |

## Corpus, bindings and limits

The filesystem scan found **18 unique genuine external rubric reports, 19 copies — 15 FAIL and 3 PASS, zero overall NON-FAIL**: Reviewer A/Frederick admin cleanup 6, Reviewer B/Brian Collect & Win 6, skipped Oliver/Season Pass transfer 4, completed Douglas/server beta sign-off 2. The two copies of Reviewer B's `(10) (1).md` are one report. All 18 reviewed SHA-256 values have an exact retained JSON match; the appendix records the complete report SHA, reviewed SHA and shortest exact matching path. No verdict is inferred from a filename or an authoring memo.

No genuine external rubric report was found in `Task_Authoring/task_inputs/plateform_reports` (only injection), the other current numbered task directories, `archived task/task_inputs-{n,p,h,s}`, or the other two `completed_tasks` cases. Archived task-n has injection/prompt/hardness reports, but no preserved rubric report. Empty rubric slots and local `09_Rubric_Check.md` files are not external reviews and cannot establish a rubric PASS/FAIL. This is a bounded corpus finding, not a claim that those tasks were never reviewed elsewhere.

The Reviewer B `Audit-Report/iteration_32_rubric_eval_audit/Rubric_Audit.md` is **local evaluation-only analysis**, not a returned Portal report. It reports PASS on later `34d1d4f1…` while the latest preserved external FAIL binds `ea7292a8…`; these are different artifacts. See `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_32_rubric_eval_audit/Rubric_Audit.md:12` and `:23`. The local Audit32 result must not be counted as a new Portal PASS.

**Snapshot caveat:** the Reviewer B task root's `09_Rubrics.json` is absent in this audit's filesystem inventory. Audit31 records a prior successful copy to that path at 2026-10-28T17:32:54Z, and r30.v5 remains retained. Audit32 describes having audited that copy. This audit cannot establish when or why the root file later disappeared. Do not import it or reconstruct it as part of an audit. Evidence: `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_31_canonical_rubric_fill/copy_verification.json:2`.

The histories below use report ordering, named run modes and intake records. Filename suffixes are not assumed to enumerate every run: Reviewer A run 6 and several Reviewer B intermediate report numbers are referenced but their original rubric reports are not preserved here. Reviewer A's run-7 report says the previous titles passed, which is **secondary evidence of a prior PASS**, not a substitute for an original run-6 report.

## Reviewer A — task …TASK_A, Frederick's admin cleanup

### Exact preserved verdict sequence

| Preserved review | Reviewed JSON prefix | Rows | Exact verdict/status | What the report establishes |
|---|---|---:|---|---|
| First, iteration 12 | `81ba510a1f5e` | 41 | FAIL 1 / COMPLETE | 9 Major rows + 2 missing outcomes; 3 reported overlap groups; Negative FAIL; seven weight disagreements. |
| Run 2, iteration 13 | `2aa2bd5cceae` | 28 | FAIL 1 / COMPLETE | Old structural defects largely fixed; Washington wording rejects CorpNet-only name; Singular creation row reintroduces overlap with list/date rows. |
| Run 3, iteration 14 | `66dff6d07925` | 27 | FAIL 1 / COMPLETE | Two Major rows: R5 wording/support mismatch, R22 four-condition bundle. Pre-recheck PASS became FAIL within this report. |
| Run 4, iteration 15 | `f00c616333c9` | 27 | **PASS 5 / COMPLETE** | One R22 overly-broad Minor, 1/27 = 3.7%, with a separately failed localized accuracy gate. |
| Run 5, iteration 16 | `bd66f3c18ac5` | 27 | **FAIL 2 / PARTIAL** | R22's full-year tie-break creates new annual/yearly ambiguity; the previous $25K-payable hole is fixed. |
| Run 7, iteration 18 | `56afe66ca2a3` | 27 | **PASS 5 / COMPLETE** | Only evidence on R1–R22/R27 changed; accepted prior titles retained; no scored defect remains. |

Exact final-block sources, respectively: `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_12_rubric_portal_20261025/6ad90e93a2c3542255f64fbf_3_rubric.md:187`; `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_13_rubric_portal_r2_20261025/6ad90e93a2c3542255f64fbf_3_rubric (1).md:143`; `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_14_rubric_portal_r3_20261025/6ad90e93a2c3542255f64fbf_3_rubric (2).md:124`; `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_15_rubric_portal_r4_pass_20261025/6ad90e93a2c3542255f64fbf_3_rubric (3).md:131`; `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_16_rubric_portal_r5_20261026/6ad90e93a2c3542255f64fbf_3_rubric (4).md:120`; `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_18_verifier_intake_20261027/6ad90e93a2c3542255f64fbf_3_rubric (6).md:117`.

**This is a changed-artifact PASS reversal, not a same-input contradiction.** The R4 PASS hash differs from R5 FAIL. R5's PARTIAL does not turn its recorded FAIL into NON-FAIL: the report explains that an open valid-alternative check caused PARTIAL, while the proven Major independently caused FAIL. Source: iteration16 report `:116`.

### Defects, source truth and repairs

**Initial design decomposition was wrong.** R2 combined payment fact and one-line formatting; R5/R37 combined counterparty and need; R28 graded an out-of-scope corporate-document review; R38 bundled/vacuously ordered two service writes. The 18 idle-pass exclusion rows were replaced by three write-kind count guards. Insurance recap and the superseded week-before WA hold were missing. This is direct evidence of deficient prompt-to-artifact coverage and row decomposition. It does not show that the rubric skill was not invoked. Sources: iteration12 report `:45`–`:69`, especially `:64`–`:67`.

**The first repair diverged from a checked fix.** Run 2 says R5 used new Washington-locking wording rather than the checked wording and R9 was a new creation row not present in the checked candidate. Its own row ledger records the recurrence: old R8's Singular overlap returned through new R9. Counterevidence against “nothing was fixed”: run 2 explicitly confirms the idle-pass rows, bundles, insurance omission and weight errors were closed. Sources: iteration13 report `:69`–`:78`.

**The hard part was denotation, not the payment arithmetic.** Static SQL confirms the relevant sources:

- Aug 18: holds use the Friday before the due date, not one week before. `Task_Authoring/task_inputs_TASK_A/01_Universe_Inject.sql:22`.
- Sep 8: one card/hold for the next unpaid installment; no later ones yet. Same SQL `:24`.
- Leonard's forward in Frederick's mailbox: ignore the 2 × $12.5K plan, replace the $25K invoice with quarterly $6,250; Q1 Oct 1, Q2 Dec 31, Q3 Mar 31, Q4 Jul 1. Sender is Leonard, not Frederick. Same SQL `:90`.
- Sep 26: first quarterly payment went out. Same SQL `:38`.

Thus Q2/Dec31 is next unpaid, the Friday-before hold is Dec26, and 4 × $6,250 = $25,000. The wrong bill is one full $25K payable; $25K as annual context is valid. The old plan's $12.5K, Q1 invoice payable now and Q3/Q4 as next need are wrong. **A bare renewal/payment name is still permitted**: the incorporated naming rule does not require the name to encode the installment/date/amount. The due-date field independently identifies the obligation.

Run 3 tried to test too much inside R22. Run 4 converted it to one semantic need but allowed a name presenting the obsolete $25K bill as payable. Run 5 closed that hole with “An unqualified full-year renewal payment names that superseded bill”, which created a synonym split: annual/yearly/full-year can describe the contract rather than the amount due. The report's strongest valid alternative is an annual renewal payment card due Dec31. It also describes four attempted keyword rewrites that repeatedly passed one contextual name and rejected its synonym. Sources: iteration15 report `:14`, `:29`–`:35`, `:98`–`:101`; iteration16 report `:14`–`:17`, `:88`–`:93`.

The R6 handoff's principle is materially better: term/recurrence words alone are neutral; grade what the name presents as payment to make. It records 67 reassessed semantic cases (36 accepted, 31 rejected), zero lint findings, and no local gate PASS. These are preserved manual judgments, not empirical agent/verifier results. Source: `Task_Authoring/task_inputs_TASK_A/Working_Files/09_Rubric_R6_Handoff.md:11`–`:28`.

**Source attribution defects were real but usually not wrong expected values.** Earlier evidence attributed July's one-time-yearly phrase and a computed annual total to September's forward, and called Leonard's forward Frederick's. The reports mostly classify them as non-scored wording/locator repairs; the R6 handoff distinguishes derivation from verbatim source wording. Do not count these as extra incorrect title facts or extra Major rows. Sources: iteration16 report `:17`, `:75`–`:79`; R6 handoff `:12`.

### Local/Portal mismatch and contrary evidence

- R4's Portal PASS coexists with `accuracy_acceptance FAIL`; the local repair gate explicitly blocks failed accuracy dimensions. The R5 handoff preserves both facts and records three local blockers after R4, then two after the residual was repaired. This is a **different release criterion**, not an invented reason to discard the external PASS. Sources: iteration15 report `:65`; `Task_Authoring/task_inputs_TASK_A/Working_Files/09_Rubric_R5_Handoff.md:7`–`:9`; `Task_Authoring/tools/stage_gate.py:1671`.
- Final run7 external PASS binds `56afe66c…`, which matches the retained/canonical export. Its 23 changes were evidence-only. Local R7 gate evidence still records missing upstream prep PASS and unmatched V3 sidecar binding, so external semantic acceptance did not clear local release. Source: `Task_Authoring/task_inputs_TASK_A/Working_Files/09_Rubric_R7_Parent_Handoff.json:84` and the exact failures in that object; iteration18 report `:18`.
- The final Portal report explicitly permits acceptance values from prompt/sibling titles when dismissing R12/R19/R13 challenges. The current local playbook and evaluator entrypoint forbid this. This is **proven policy divergence**; the report's release hash changed between R5 and run7, so it is not enough to prove nondeterminism under identical evaluator code. Source: iteration18 report `:104`–`:108`; `Task_Authoring/playbooks/09_Rubric_Writing.md:66`; `Evals/3_Rubrics_Eval.md:15`.
- Initial Moderate overlap counting should be treated cautiously. Its three groups contain rows already counted Major, whereas the stated rule removes higher-severity members. The raw scoring record would be needed to prove the exact residual group numerator. The FAIL does not depend on that discrepancy because 11 Major issues already remain. Sources: iteration12 report `:67`, `:74`–`:75`; `Evals/references/rules/qc_rubric_v10.md:108`–`:121`.

## Reviewer B — task …TASK_B, Brian's Collect & Win hand-off

### Exact preserved verdict sequence

All six preserved external reports have 45 rows, 44 Outcome and one Process, and end **FAIL 1 / COMPLETE**. This is not a run of preserved NON-FAILs or PASSes.

| File suffix / intake | Reviewed JSON prefix | Principal scored change |
|---|---|---|
| `(3)`, Audit23 | `e9f951da8014` | R27 source-attribution Major plus a missing-pending hole; R29 contradictory counting sentences. |
| `(6)`, Audit26 | `09d99391c98a` | R29 bundles pending status with count, rejects correct summaries/history/contrasts, and omits eventLifecycleV2 in title; R44 lacks Brian's accepted Slack ID and is underweighted. |
| `(7)`, Audit26 | `648d9874e341` | R29 made status-neutral but remains ambiguous/over-specific; R44 title/weight repair not applied; R27 develops undated-live hole. |
| `(8)`, Audit27 | `e40ae9310e01` | R44 exact checked fix now closes; R27 unscoped fail clause/heading/history ambiguity; R29 conflicting count exceptions and same-name restatement failure. |
| `(10) (1)`, Audit28/root copy | `ebf793bb6fbd` | R27 same-line clearing rule rejects valid multiline history and leaves deployed/on-prod ambiguous; R29 plan/alias rules conflict. |
| `(11)`, Audit30 | `ea7292a8fb9a` | R27/R29 open alias rule flagged; R27 heading override, Live-heading escape and external-clock attribution defect; evaluator admits prior alias advice error. |

The full final blocks and hashes are in the appendix. Most reports say “both rewrites fix last run's specific problems” or equivalent; unchanged FAIL does not mean the same exact issue was never fixed. Conversely R44 in `(7)` is explicitly **not fixed**, so it is a true recurrence.

### Ground truth is simpler than the ever-growing textual rules

Static source text establishes:

1. Amended rule 4: server-only changes get their own section; mark each live only if the backend owner confirms behavior serving production traffic, otherwise pending; installed disabled/bypassed code is pending. `Task_Authoring/task_inputs_TASK_B/01_Universe_Inject.sql:65`.
2. Douglas's receipt: prod eventLifecycleV2=0, dev=1; installed handler packages the restart fix; the route selects **the same fix, not another backend change**; previous “on prod” meant installed, not serving; after rollback production uses the old route; the first-token/token-count/Day3-reward changes remain live; next enable attempt Oct2. Same SQL `:174`.
3. The 09:55 temporary production enable is real; the 10:40 rollback ends it; dev remains enabled. Same SQL `:194`, `:200`; request traces distinguish prod old route from dev new route at `:191`.

The intended predicates are therefore (a) pending current serving status for this implementation, and (b) one listed change for its handler/route aliases. They must remain independent: one entry incorrectly live should fail status only; two distinct listed entries for the same implementation should fail count only; missing the entry can fail both because the required artifact item is missing. Historical service, installed code and dev-on are compatible with pending production service.

The sources establish physical identity and status, **not every possible prose layout's count semantics**. The report eventually acknowledges “One layout question the records can't settle, and you have to pick a side.” That is a representational policy choice and must be frozen once; it is not a newly discovered universe fact. Source: `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_27_rubric_scope_repair/received/6ad90e9449d1194f4e538cdf_3_rubric (8).md:44`.

### Proven content and workflow causes

**Reviewer B's repaired row repeatedly encoded competing exceptions.** Examples are concrete:

- `(3)` sentence 2 merges an alias unless explicitly separate, while sentence 3 counts an untied top-level pending alias; the same restart/eventLifecycleV2/Day2 list gets two counts. Report `(3):15`.
- `(6)` “one pending change” grades both status and count; the same live mislabel fails R27 and R29. Report `(6):12`.
- `(7)` malformed second-item and history sentences, summaries and “separate from the first-token fix” produce incorrect rejections. Report `(7):24`–`:35`.
- `(8)` “history/plans do not add changes regardless of layout” competes with “independently status-bearing entries count separately”; same-name table-plus-detail restatement counts twice. Report `(8):28`–`:34`.
- `(10) (1)` same-line resolution rejects a valid two-line enable/rollback timeline; deployed-to-prod can be installed or live under a Pending heading. Root report `:13`–`:26`.

These are high-confidence artifact problems even though all material message IDs, status facts and timestamps can be correct. The local repairs focused on narrow rows and documented counterexamples, but the growing lexical grammar carried unresolved precedence rules forward.

**R44's incomplete repair is unusually clear.** `(6)` provided a checked title with Brian's `EMPLOYEE_0026_SLACK_ID` and weight 5 for template + correct invite + Slack identity join. `(7)` says only evidence changed, so the title still lacks the accepted self-tag ID and weight remains 3. `(8)` confirms the exact checked fix was copied and both findings closed. Sources: `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_26_latest_rubric_repair/received/6ad90e9449d1194f4e538cdf_3_rubric (6).md:35`; the `(7)` report `:128`; the `(8)` report `:124`. This is a field-target/repair-closure failure, not a source retrieval failure.

**Earlier rubric provenance was contaminated by OE wording.** `(3)` records “restart/reconnect-state implementation” as OE wording, not a verbatim source name, and “flag” as an accepted synonym rather than a native record term. The replacement separates provenance from semantic equivalence. It is fair to accept a paraphrase without falsely attributing it to a record. The report scores this as an incorrect supporting claim; it does not prove that eventLifecycleV2 was a different implementation. Source: `(3)` report `:11`–`:14`, `:40`.

**Local and external clocks are unbound.** Canonical context says `freeze_utc = 2025-10-01T00:00:00Z`, and explicitly retains displayed 07:00 without inferring a timezone. Latest external report says synth-cut cutoff 06:59:59Z and task clock 07:00Z, and flags the rubric's stored-00Z source assertion. These can both describe their respective systems; the error was representing local authoring context as an external universe record. Source: `Task_Authoring/task_inputs_TASK_B/Working_Files/00_Task_Context.json:10`–`:17`; `(11)` report `:16`, `:54`, `:58`. The repaired handoff removes that unsupported rubric evidence assertion without changing local context (`Audit30/DELIVERY_HANDOFF.md:31`). All deciding R27/R29 records above precede both freezes; **no status/count verdict change from the seven-hour mismatch is proved**.

### Proven evaluator contribution, and what is only a hypothesis

**Explicit admitted bad guidance — high confidence.** The `(11)` report itself says the previous “Any name or paraphrase counts” advice is now what QC B3 flags, and calls the advice its own error. This directly supports evaluator-caused repair churn. It should not be diluted into a generic claim that the contributor failed to follow instructions.

**Other guidance changes — high confidence as text, medium as unfairness.** `(3)` rejects an alias-only self-containment challenge because the title's objective semantic rule can accept paraphrases (`:113`). `(7)` again accepts that semantic rule (`:145`). `(11)` instead requires closed source-backed name families. Likewise `(6):25` says a separate status-bearing entry fails even if labelled the same fix; `(11):34` says entries sharing a name or explicitly saying same change count once. Some witnesses differ, and changes of evaluator release hash occur, so this audit does not claim an identical-input regression test proves random grading. These are nevertheless changed acceptance-policy instructions that a future contract must resolve before repair.

**A directly contradictory repair step — high confidence.** `(8):20` recommends clearing a production claim on that same line. The later `(10) (1):13` flags that same-line requirement as overly specific for a correct multiline timeline. The source supports a complete chronological account; it never requires the rollback on the same physical line. This is a concrete bad recommended restriction, independently of who first drafted the latest sentence.

**Blindness claims are not independently verified.** Reports say R1–R7 were blind and local handoffs claim independent reviewers. Those are provenance statements, not supplied per-agent traces of independence. No claim is made that any named skill failed to run; the Audit30 handoff expressly says the actual skill/playbook portions were applied (`Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_30_rubric_alias_repair/DELIVERY_HANDOFF.md:42`).

### Why local “PASS” did not settle external status

Audit29's real local gate returned FAIL because `09_Rubric_Check.md` was missing and the prep PASS was absent; its input was the canonical `[]` placeholder, **not external r28**. That cannot be reported as a semantic FAIL of the 45-row proposal. Source: `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_29_command_preflight/COMMAND_OUTCOME.md:11`–`:21`; raw output `rubric_check_gate.stdout.txt:1`–`:6`.

Later r30.v5 has SHA `34d1d4f1…`, 45 rows/total weight149, target titles95/110 words and only six strings changed from r28 (R27/R29 title/justification/evidence). Local reviewers recorded 131 frozen cases +10 supplemental probes, zero remaining targeted findings and zero title/support acceptance differences. Thirteen old expectations were transparently corrected to the new report's rules. **Changing expected outcomes is evidence of contract evolution, not an independent 131-case proof of invariant correctness.** Sources: `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_30_rubric_alias_repair/DELIVERY_HANDOFF.md:33`–`:46`.

Audit32's local PASS is for that later version. It explicitly locks 43 rows and labels remaining known breadth/coverage concerns QM notes under DELTA. It also says R29's opening clause is literally false for a correct list containing other changes, then treats parenthetical scope/manual readings as resolving it. This is a residual wording concern, not proof of a new external FAIL. Source: `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_32_rubric_eval_audit/Rubric_Audit.md:141`–`:144`, `:215`–`:221`. **Fresh external acceptance for `34d1d4f1…` is unpreserved/pending in this corpus.**

## Skipped Oliver — Season Pass engineering-transfer task

### Exact verdict history

| Report | Reviewed JSON prefix | Rows | Verdict/status | What changed |
|---|---|---:|---|---|
| `01_Rubrics.md` | `434aac768505` | 41 | FAIL 1 / COMPLETE | 27 Major rows +26 missing outcomes; weights FAIL; all lower-case Agent titles fail format dimension; two idle-pass preservation rows. |
| `02_Rubric.md` | `5e1c2b9d6939` | 59 | FAIL 2 / COMPLETE | Old 26 omissions fixed; new scope guards over-tight, filename cascade, vague exemplars and two weight disagreements. |
| `03_Rubric.md` | `593ad6176309` | 59 | FAIL 2 / COMPLETE | Prior eight issues fixed; R31/R33 fail to distinguish same-subject email and competing Slack thread. |
| `04_Rubric.md` | `830a0a999571` | 59 | FAIL 2 / COMPLETE | Those identities now fixed; same two rows develop narrower “the handoff” and “class total” ambiguities. |

Primary sources: `Task_Authoring/task_inputs-skipped/Plateform_reports/01_Rubrics.md:328`; `02_Rubric.md:189`; `03_Rubric.md:169`; `04_Rubric.md:153` (all under that exact same directory). No external rubric PASS is preserved for this task.

**The initial missing coverage was substantive.** Three class totals and register link were ungraded on each of slide and ZOM-801; nine register columns had no value check; no-attachment requirement, scope guards, listed-key volume controls and extra Linear writes were uncovered. A bundled header row did not grade populated cell values. Totals 68/16/44, blocker groups11/0/25/12/0 and historical six events/754 participants were explicitly recomputed by the report; their factual correctness did not cure omission or wrong-grain coverage. Source: `Task_Authoring/task_inputs-skipped/Plateform_reports/01_Rubrics.md:55`–`:104`.

**The repair advice created new scope lock-ins.** First report recommends “as the only email it sends about the handoff” and “as its only Slack post about the handoff” (`:32`, `:34`). The second report then flags a second valid Arthur-only email or second same-thread reply as rejected. It admits several new defects came from the previous Fix List's wording (`02_Rubric.md:94`). The right constraint is destination/content/target scope, not an unauthorized message-count ceiling. R1 likewise needed to count retained CSVs, accepting trash-and-recreate. This is proven evaluator-assisted over-specificity, not mere contributor deviation.

**The next cycle was under-specified identity.** The 16:00Z Zombie Match3D and 16:20Z Domino Delights emails share a subject; #builds has both the hub and older circulation thread. R31/R33 originally did not name the actual record. The contributor copied the prior titles exactly, but custom supporting fields changed object hashes and forced full review; old wording defects then became scored. Source: `Task_Authoring/task_inputs-skipped/Plateform_reports/03_Rubric.md:14`–`:20`, `:108`–`:116`.

**Run4 repeats that mechanism with new words, not the same unresolved record ID.** The email/thread identity findings are closed. “The handoff” still matches the planted Domino case, and “class total” can mean blocker/event totals rather than READY/WATCH/HOLD. The report says titles copy the previous fix exactly but justification/evidence differ; those were enough to unlock the rows again (`04_Rubric.md:104`). This explains why repeatedly applying a recommended title can still fail: exact checked-row locking covers the full row, and it does not guarantee all future semantic ambiguities were found.

**Policy tension remains.** The reports keep “leave all PRs alone” ungraded because no GitHub write is required and a standalone no-op prohibition fails Negative Criteria. They call this a QM note, not scored coverage. They also allow ordering as Outcome R33, whereas Douglas/Reviewer B use Process for related sequencing. These are not automatically contradictions: inspect whether the exact observable end state records the sequence, and preserve the local exclusion rule's structural limitation. Sources: `04_Rubric.md:51`–`:56`, `:114`; `Evals/references/rules/rubric_flow_v2.md:96`–`:109`. Do not invent a required GitHub write merely to attach a prohibition.

**Capitalization is mechanical, not semantic.** The initial report fails 41 lower-case “The agent” titles as off-pattern, and the actual checker has a case-insensitive Agent identity detector plus a case-sensitive standard-pattern detector. Thus this seemingly cosmetic finding has a code basis. Source: `01_Rubrics.md:120`; `Evals/tools/hg_rubric_checks.py:21`–`:23`, `:217`. It should be surfaced by preflight rather than discovered after substantive review.

## Completed Douglas — server-side beta sign-off

Two originals show a successful repair, which is important contrary evidence to a theory that the evaluator always invents another blocker:

- First report, SHA `1394b532…`, reviewed `1244870f…`, **52 rows, FAIL1 / COMPLETE**. Three Major rows +18 missing outcomes; two overlap groups; 19/52 weight disagreements; one missing ordering check is **Process NON-FAIL3**, while the overall verdict is FAIL1. Source: `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_3_rubric.md:76`–`:92`.
- Second report, SHA `d440a207…`, reviewed/canonical `880f59b9…`, **76 rows, PASS5 / COMPLETE**, zero issues; 20 locked,26 checked fixes,4 evidence-pointer edits,24 new,2 rechecked rows. Source: `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_3_rubric (1).md:8`, `:151`–`:167`.

The missing outcomes were six DM ticket identities, six Todo moves and six per-ticket comments. A count of15 did not cover which tickets or each distinct change. R43 bundled15 comments, content and a Todo prerequisite. R1 locked the register to Google Sheets although a Doc table is valid. R52's justification widened a title. The repair split per-target writes/content, added bare wrong-target guards, completed the on-prod register column and added the share-after-folder order. Sources: first report `:14`, `:20`–`:34`, `:61`–`:69`; second `:43`–`:57`.

Weight changes are source-work based: R15's PR#52 is directly quoted in the ticket comment (3→1); rollback/redeploy/Approve/freeze/import joins justify5. The second review also explains why some simpler one-PR cases remain3. This is an example of an auditable explanation rather than uniform weight inflation. Sources: first report `:16`–`:19`, `:131`–`:136`; second `:55`–`:57`.

A policy ambiguity remains around the five-sample cap: first review calls12/17 on-prod cells excessive sampling and recommends exhaustive17/17 coverage, then second accepts it as direct coverage. It consistently treats distinct DM facts, comments and state changes as direct, unsampleable results. The local playbook's broader population-sampling language should explicitly distinguish those cases. Sources: first report `:63`–`:67`, `:128`–`:129`; second `:43`, `:53`; `Task_Authoring/playbooks/09_Rubric_Writing.md:70`.

The final PASS does not mean every known issue disappeared. R76 can pass a never-moved root file, but R1 catches folder placement; a stricter candidate created a cascade and was dropped. The report explicitly rejected the stricter row and records the residual decomposition. That is an evaluator design choice, not proof all isolated-title breadth checks were uniformly applied. Source: second report `:107`–`:117`. This is relevant when comparing Reviewer B/Reviewer A findings that insist each title alone reject a plausible wrong result.

## Scoring, rule drift and actual gate capability

### Arithmetic audit

Reported ratios are arithmetically consistent after rounding:

| Case | Numerator / authored rows | Exact percentage | Reported | Interpretation |
|---|---:|---:|---:|---|
| Reviewer A first Major | 11/41 | 26.829% |26.8% | Missing outcomes add only numerator. |
| Reviewer A run2 Major |1/28 |3.571% |3.6% | Any-Major Portal rule fails despite low ratio. |
| Reviewer A run3 Major |2/27 |7.407% |7.4% | Count rows once at highest severity. |
| Reviewer A R4 Minor / R5 Major |1/27 |3.704% |3.7% | Same percentage, different severity and different artifact. |
| Reviewer B repeated Major |2/45 |4.444% |4.4% | Both rows counted once despite multiple types. |
| Reviewer B R27 Minor |1/45 |2.222% |2.2% | Not an additional row when same row already Major. |
| Oliver first Major |53/41 |129.268% |129% |27 affected rows +26 missing outcomes; >100% is allowed. |
| Oliver second Major |3/59 |5.085% |5.1% | Correctly not diluted by new rows. |
| Oliver later Major |2/59 |3.390% |3.4% | Correct external any-Major FAIL. |
| Douglas first Major |21/52 |40.385% |40.4% |3 affected rows +18 omissions. |
| Douglas first weights |19/52 |36.538% |37% |Separate dimension. |

The dispute is primarily **which defects and severity count**, not basic division. Reported quality scores1 versus2 for similarly small Major counts are not derivable solely from these percentages; preserve the original score and avoid reverse-engineering an unstated scoring formula.

### Multiple policy contracts coexist

| Topic | Local authoring text | Actual evaluator entrypoint / observed reports | Consequence |
|---|---|---|---|
| Quality FAIL threshold | Major>10%, Major+Moderate>15%, all>20%; otherwise NON-FAIL possible | `Evals/3_Rubrics_Eval.md:36`: any Major/Moderate FAIL; Minor5–10% NON-FAIL3, >10% FAIL |Local prediction bands are stale relative to entrypoint. |
| Weights |Two-level≥15% /one-level≥30% FAIL |Entrypoint:≤10% one-level only may be NON-FAIL4; any two-level or larger disagreement FAIL |A small two-level defect can fail externally. |
| Supporting acceptance |Title-only |Reviewer A reports explicitly permit sibling titles for accepted values |Hash/version-bound policy reconciliation required; cannot assume title-only matches the Portal release. |
| Overly broad severity |Moderate (`09` playbook and Evals strict table) |Reviewer A R4 and several Reviewer B reports use Minor; Oliver first uses Major for broad acceptance failures |Observed taxonomy/impact calibration differs; not a math error. |
| Process |Local exactly1 invalid=>NON-FAIL |Entrypoint says any invalid Process FAIL; only one missing ordering check may be NON-FAIL3 |Do not add Process rows solely for balance. |
| Same fact across artifacts |V3 same fact in≥3 rows FAIL |Oliver reports accept totals in4 prompt-required deliverables and reject cascade finding |V3/global-fact policy differs from older output-specific review. |

Exact local anchors: `Task_Authoring/playbooks/09_Rubric_Writing.md:61`, `:196`, `:203`–`:211`; `Task_Authoring/setup/GEN_EXECUTION.md:159` (rubric policy table; search the “Rubric quality” row). Exact external anchors: `Evals/3_Rubrics_Eval.md:32`–`:48`; Reviewer A final report `:104`–`:108`; Reviewer A R4 report `:27`; Oliver first report `:67` and `:258`.

There is drift **inside the evaluator documentation too**: `Evals/references/rules/qc_rubric_v10.md:129` says no quality NON-FAIL and Minor≥5% FAIL, and `:138` says any weight disagreement fails, while the entrypoint's later dated October9 override permits narrow NON-FAIL bands. Apply the dated overriding entrypoint for current predictions; preserve report-specific release hashes for historical claims. Reading just one “v10” reference file is insufficient.

### What the actual authoring gate proves

`Task_Authoring/tools/stage_gate.py:2360`–`:2386` parses the rubric/check report, checks declared criteria count, exact quoted spans, recognized issue types, presence of at least7 dimension rows, readiness-line syntax and a self-review with each C-ID. `rubric_validity` (`:1642`–`:1679`) blocks recorded incorrect/unauthorized/unobservable/contradiction/missing-coverage/all-fail items and selected failed repair dimensions. The V3 sidecar adds hash/source/temporal/declared fact checks; it is not a substitute for semantic review.

**The code does not recompute quality percentages, recompute the weight-disagreement dimension, or reject a generic Overall Quality FAIL/NON-FAIL readiness solely from that status.** It checks the dimensions table's size, not its numerical consistency. This is proven from the implementation, not a claim that a historical failing artifact actually obtained PASS. Other prerequisite checks can and did block it. A claim that the gate itself “verifies the dimension table” should be narrowed to its implemented checks or supported by added arithmetic checks.

Likewise `Task_Authoring/support/local_search/tools/hg_rubric_lint.py:41`–`:68` is a lexical/schema checker. It detects exemplars, tool identifiers, empty fields, weight/category domains, whitespace and leading prohibition syntax. It does not establish factual accuracy, counterexample completeness, count-unit semantics, causal overlap or correct work-kind weights. Reviewer B's malformed/ambiguous rows repeatedly had zero lint hits; Reviewer A's idle-pass formulations escaped its word list, which the first external report explicitly discloses. Therefore “lint clean” must not be equated with “rubric ready”.

### Local check failure is not non-use of the skill

The skill requires prep/draft/check and a passed gate, but later bounded report-only proposals explicitly document the subset applied and remaining formal blockers. Reviewer B Audit29 even executed the real gate and documented why it did not inspect the external proposal. Reviewer A R4–R7 handoffs record real gates failing prep/binding checks. The preserved evidence does not justify “the author never used the skill” or “the gates passed bad semantics” without a corresponding invocation/actual certificate. The supported causal statement is that report-only revisions and external retests continued while formal canonical prerequisite/binding work remained unresolved, with disclosure in the handoffs.

## Prioritized changes: specific skills, gates and tests

These are recommendations only; no original skill, validator or task was changed.

**P0 — Bind one executable rubric policy to every proposal and review.** Add a policy manifest naming evaluator release, clock, title-context rule, broadness severity, weight/quality bands, duplicate-across-artifacts rule, allowed coherent-record exceptions and DELTA policy. Store its digest beside the prompt/injection/rubric digests. Reject a comparison as “policy mismatch” before calling it a content regression. Add fixtures for: 1 Major/27=>FAIL under external flow;1 Minor/27=>PASS with outstanding repair;5% and10% Minor band edges;1 two-level weight defect;11% one-level disagreement; title-only versus sibling-permitted context. These target the actual observed drift, not implementation-mirroring tests.

**P0 — Make repair closure field-aware and case-bound.** Every external finding needs stable ID, source pointer, exact affected JSON field(s), old/new quote and the original correct/wrong witness. A “fixed” status requires a diff covering that field and replay of its witness. This would have caught Reviewer B R44's evidence-only repair instantly. Preserve the original Brian/self-mention and3→5 weight case as a regression fixture. Do not count editing evidence as fixing a title.

**P0 — Freeze semantic acceptance before another R27/R29 rewrite.** In the rubric-writing skill, require a compact decision table for current production service versus installation/history/dev/plan, and a separate table for listed-change identity versus explanatory detail. Decide once how same-name restatements, alias-only siblings, nested timelines, Pending/Live headings, values-only rows and explicit “separate change” claims count. Source uncertainty should remain uncertainty; layout choices should be explicit policy. Build paraphrase/layout-invariance pairs from all six preserved Reviewer B reports. Preserve the sources and chosen expected outcomes with versioned change reasons; an evaluator's new convention cannot silently rewrite the suite.

**P0 — Separate payment amount denotation from token matching.** Add the Reviewer A R22 regression family: bare renewal/payment; annual/yearly/full-year renewal;Q2 payment with paid-Q1 history; $6,250 of$25K/year; paid INVSINC22671 as context; invoice explicitly payable now; wrong Q1/Q3/Q4; superseded $12.5K; full$25K as payable. Require the title-alone and all-fields readings to agree, with an explicit tie-break principle. Do not add mandatory quarter/amount fields the prompt does not require.

**P1 — Implement actual scoring reconciliation in `st_rubric_check`.** Derive authored denominator from JSON, highest severity per affected row, overlap-group de-duplication, missing-outcome numerator-only contributions and separate weight disagreements; compute expected dimension/verdict under the pinned manifest. Reject contradictory report math or an OverallQuality FAIL presented as readiness. Maintain two explicit outputs: semantic prediction and structural/source certificate. Fixture the observed53/41 case so >100% is not wrongly rejected; fixture overlapping Major/group members so they are not counted twice.

**P1 — Add wrong-target and valid-extra-action coverage fixtures.** In rubric prep, walk each artifact/audience with independent required result + content + authorized scope. Carry Oliver's two same-subject emails, two Slack threads, Domino handoff decoys, trash-and-recreate CSV, second Arthur-only email, early acknowledgement and READY/WATCH/HOLD versus blocker counts. A count guard must be justified by an actual target population; it must not reject valid additional actions at the same target.

**P1 — Stabilize DELTA reviews and checked fixes.** Preserve an entire checked row with its policy/source digest and counterexample suite. Report whether the contributor copied the title only or all5 fields, because custom evidence edits currently unlock previously accepted titles. Every newly scored old phrase should identify the earlier review that missed it and whether it is a policy change, fresh source fact or new witness. Keep known non-scored gaps separate from “all clean”: Reviewer B's membership/build/after-cut guards and Oliver's PR prohibition remain disclosed residuals.

**P1 — Require complete per-target coverage for distinct writes.** Use Douglas's successful52→76 repair as the positive control:15 different Todo moves,15 comments with different changes and15 told identities need direct target coverage. Sampling may cover comparable repetitive table cells, with explicit volume/exception rows, but not substitute for distinct required writes or content facts. State exactly when exhaustive coverage ceases to be a sampling group so12/17 versus17/17 does not become an accidental loophole.

**P2 — Improve lint without overclaiming it.** Add standard Agent capitalization checks and flag possible idle-pass predicates (“preserves…unchanged”,“keeps…outside”,“limits…to”) for required human/model semantic review. These should be warnings requiring a do-nothing witness check, not automatic Major classifiers. Display lint capability limits in handoffs. Add source-attribution checks separating verbatim source strings, derived values and accepted paraphrases; portable record IDs should replace machine-local evidence paths without silently changing acceptance.

**P2 — Preserve the actual latest deliverable pointer.** Store a task-level manifest identifying canonical export, exact externally reviewed export, retained candidate and latest external report independently. Assert existence/hash match at handoff, and never transfer a Portal PASS to a later JSON. The Reviewer B missing root slot and Audit32-versus-external discrepancy show why an audit title or copy receipt is insufficient current-state proof.

## Remaining blockers and evidence limits

- No fresh external report for Reviewer B r30.v5 (`34d1d4f1…`) is preserved. Latest external result remains FAIL on r28 (`ea7292a8…`); local Audit32 PASS is separately preserved.
- Reviewer A run6 PASS is referenced by run7 and a handoff, but its original rubric report is not preserved in this corpus. The genuine latest run7 PASS is preserved and exact-bound.
- The current Reviewer B canonical rubric slot is absent; only the retained candidate and historical copy/audit records establish its contents. Cause and timing of absence are unknown.
- External review contexts use a synth-cut07Z source while local contexts use canonical00Z. No external source-manifest bytes for that exact context were established here, and no clock was changed. The decisive facts checked above are before both freezes.
- Per-agent execution traces and the original machine scoring records behind most reports are not preserved here. Independence, scan completeness and source recomputation claims remain report assertions unless corroborated by retained artifacts. Arithmetic and exact JSON bindings were independently checked; full128-key source recomputation and live Portal configuration were not rerun.

## Appendix — exact report and artifact binding inventory

Each reviewed JSON hash below was independently matched to retained bytes. Report line numbers point to the original final verdict block; full context/release hashes are retained in scratch `rubric_report_bindings.json`. Duplicate report copies are not separate verdicts.

### B01 — FAIL 1 / COMPLETE — 41 (Outcome: 40, Process: 1)

- Original report: `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_12_rubric_portal_20261025/6ad90e93a2c3542255f64fbf_3_rubric.md:187`.
- Report SHA-256: `f83fa6e15837b08fdf316a4c18a674ffd26185a22d6fa9780edd15ecdd92ce2e`.
- Reviewed JSON SHA-256: `81ba510a1f5ed0c7a49def3573b674ba226aecc3d1f9258f35f799edf8bdb484`.
- Exact retained JSON: `Task_Authoring/task_inputs_TASK_A/Working_Files/09_Rubrics.candidate.json:1`.
- Evaluator release: `ec8197a417f29f96bfbbd36e9f6ae918e7ddd5763219bde7cba6bf45707cdbab`.

### B02 — FAIL 1 / COMPLETE — 28 (Outcome: 27, Process: 1)

- Original report: `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_13_rubric_portal_r2_20261025/6ad90e93a2c3542255f64fbf_3_rubric (1).md:143`.
- Report SHA-256: `3fd0e213042a0515d21a02393105875c6c1e94d24f5cb2d7dd480d41f609a9b2`.
- Reviewed JSON SHA-256: `2aa2bd5cceae7ac475b56ac4c06c008d5b40f426cf67ada0b0f7a056e78fba3d`.
- Exact retained JSON: `Task_Authoring/task_inputs_TASK_A/Working_Files/09_Rubrics.r2.report_candidate.json:1`.
- Evaluator release: `ec8197a417f29f96bfbbd36e9f6ae918e7ddd5763219bde7cba6bf45707cdbab`.

### B03 — FAIL 1 / COMPLETE — 27 (Outcome: 26, Process: 1)

- Original report: `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_14_rubric_portal_r3_20261025/6ad90e93a2c3542255f64fbf_3_rubric (2).md:124`.
- Report SHA-256: `07da306f688a5dc630a1f08c5876aee6125c40599283095e050b1bc725ab48a9`.
- Reviewed JSON SHA-256: `66dff6d079259bf7878edf783206b14e05c6263751657b3a7f9c0b03a667ee16`.
- Exact retained JSON: `Task_Authoring/task_inputs_TASK_A/Working_Files/09_Rubrics.r3.report_candidate.json:1`.
- Evaluator release: `ec8197a417f29f96bfbbd36e9f6ae918e7ddd5763219bde7cba6bf45707cdbab`.

### B04 — PASS 5 / COMPLETE — 27 (Outcome: 26, Process: 1)

- Original report: `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_15_rubric_portal_r4_pass_20261025/6ad90e93a2c3542255f64fbf_3_rubric (3).md:131`.
- Report SHA-256: `d8542cdd1ec26287278041bcf7ff4ef3464c6e6182b77164068b0d437bd45f1a`.
- Reviewed JSON SHA-256: `f00c616333c935ed9475e60ccd5c26db54f49ae176a07f098f2decabe19a1524`.
- Exact retained JSON: `Task_Authoring/task_inputs_TASK_A/Working_Files/09_Rubrics.r4.report_candidate.json:1`.
- Evaluator release: `ec8197a417f29f96bfbbd36e9f6ae918e7ddd5763219bde7cba6bf45707cdbab`.

### B05 — FAIL 2 / PARTIAL — 27 (Outcome: 26, Process: 1)

- Original report: `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_16_rubric_portal_r5_20261026/6ad90e93a2c3542255f64fbf_3_rubric (4).md:120`.
- Report SHA-256: `3d55dcfdf711cfc5c33203f250e31852a1fa7303176d41d2727df6589b9f0bcd`.
- Reviewed JSON SHA-256: `bd66f3c18ac59ebc73c7530be6d69992ad6cf045b82c269bbd49c4ab6ed3f9b0`.
- Exact retained JSON: `Task_Authoring/task_inputs_TASK_A/Working_Files/09_Rubrics.r5.report_candidate.json:1`.
- Evaluator release: `ec8197a417f29f96bfbbd36e9f6ae918e7ddd5763219bde7cba6bf45707cdbab`.

### B06 — PASS 5 / COMPLETE — 27 (Outcome: 26, Process: 1)

- Original report: `Task_Authoring/task_inputs_TASK_A/Audit-Report/iteration_18_verifier_intake_20261027/6ad90e93a2c3542255f64fbf_3_rubric (6).md:117`.
- Report SHA-256: `4fd8cddfc60bfd6b0075c1d9315f50c584dba40a17f363243fa209a3392292df`.
- Reviewed JSON SHA-256: `56afe66ca2a3c90e9a994affcc10a7af9a60100db946f62ee82415a14971990a`.
- Exact retained JSON: `Task_Authoring/task_inputs_TASK_A/09_Rubrics.json:1`.
- Evaluator release: `633dfebccbcb03e248f19b8115a04a1c41d0059abccdb332a1cb20957b2b3ddc`.

### B07 — FAIL 1 / COMPLETE — 45 (Outcome: 44, Process: 1)

- Original report: `Task_Authoring/task_inputs_TASK_B/6ad90e9449d1194f4e538cdf_3_rubric (10) (1).md:182`.
- Report SHA-256: `dd432e1e52675c560071c21e05b9a7c4a53b2ef85415e722afa4f4b287ca7894`.
- Reviewed JSON SHA-256: `ebf793bb6fbddc2baec70b85f88b44149b5dd6c2d762c27ab9485be99c3fc129`.
- Exact retained JSON: `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_27_rubric_scope_repair/candidate/09_Rubrics.external_review.r27.v4.json:1`.
- Evaluator release: `6478616fae461adfff81f45b2a523017b7a8e042bf02b6afc8c113d659886b8f`.

### B08 — FAIL 1 / COMPLETE — 45 (Outcome: 44, Process: 1)

- Original report: `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_23_external_rubric_intake/received/6ad90e9449d1194f4e538cdf_3_rubric (3).md:149`.
- Report SHA-256: `2fcf37e70c368c2d703697759a37cdb48bd076ea07bb9c680c1d3604fd4b70f8`.
- Reviewed JSON SHA-256: `e9f951da8014f468fd798968fedde4dd48169c7ec207aa7b3f995e4305dc22af`.
- Exact retained JSON: `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_23_external_rubric_intake/received/09_Rubrics (1).json:1`.
- Evaluator release: `633dfebccbcb03e248f19b8115a04a1c41d0059abccdb332a1cb20957b2b3ddc`.

### B09 — FAIL 1 / COMPLETE — 45 (Outcome: 44, Process: 1)

- Original report: `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_26_latest_rubric_repair/received/6ad90e9449d1194f4e538cdf_3_rubric (6).md:180`.
- Report SHA-256: `0a26ffd2d199befab06b8ce1b0292cc68bb6ef0ef765bc0d383e625f8a8c23bd`.
- Reviewed JSON SHA-256: `09d99391c98a0f81ba6c98a2ed8dd7b1b06eb3865f84ba4f9d9d6e3405d9d2fc`.
- Exact retained JSON: `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_25_external_rubric_capitalization/candidate/09_Rubrics_external_review_proposal.json:1`.
- Evaluator release: `633dfebccbcb03e248f19b8115a04a1c41d0059abccdb332a1cb20957b2b3ddc`.

### B10 — FAIL 1 / COMPLETE — 45 (Outcome: 44, Process: 1)

- Original report: `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_26_latest_rubric_repair/received/6ad90e9449d1194f4e538cdf_3_rubric (7).md:194`.
- Report SHA-256: `d7ef5a30f900b5cb0dbde3bd3a15f6efa7faedd91ddd94763a1e3521b5c0a12c`.
- Reviewed JSON SHA-256: `648d9874e3414f95bc98b7f53ba5f92840a7e66fcdfbde9e5f0dc35911874deb`.
- Exact retained JSON: `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_26_latest_rubric_repair/received/09_Rubrics (3).json:1`.
- Evaluator release: `633dfebccbcb03e248f19b8115a04a1c41d0059abccdb332a1cb20957b2b3ddc`.

### B11 — FAIL 1 / COMPLETE — 45 (Outcome: 44, Process: 1)

- Original report: `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_27_rubric_scope_repair/received/6ad90e9449d1194f4e538cdf_3_rubric (8).md:192`.
- Report SHA-256: `1df8947d7f77835e2845855cc8d182cda939c054a565b3ed9535fae76ff4a045`.
- Reviewed JSON SHA-256: `e40ae9310e0178d924b597f2be8564d3f98038267c1f1c6996d34600641d6d81`.
- Exact retained JSON: `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_26_latest_rubric_repair/candidate/09_Rubrics.external_review.r26.v1.json:1`.
- Evaluator release: `6478616fae461adfff81f45b2a523017b7a8e042bf02b6afc8c113d659886b8f`.

### B12 — FAIL 1 / COMPLETE — 45 (Outcome: 44, Process: 1)

- Original report: `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_30_rubric_alias_repair/received/6ad90e9449d1194f4e538cdf_3_rubric (11).md:180`.
- Report SHA-256: `934e103b9a0e8597306a98db7ef5691aa1545bb9bfa209bafd89677a15a9d1fa`.
- Reviewed JSON SHA-256: `ea7292a8fb9ae62a740b98744151efde71c776622e5d9b480014b2e7292db106`.
- Exact retained JSON: `Task_Authoring/task_inputs_TASK_B/Audit-Report/iteration_28_rubric_semantic_repair/candidate/09_Rubrics.external_review.r28.v2.json:1`.
- Evaluator release: `6478616fae461adfff81f45b2a523017b7a8e042bf02b6afc8c113d659886b8f`.

### B13 — FAIL 1 / COMPLETE — 41 (Outcome: 41, Process: 0)

- Original report: `Task_Authoring/task_inputs-skipped/Plateform_reports/01_Rubrics.md:328`.
- Report SHA-256: `67f08b2a1175f3e6b906c71860a0135566f2eca33139bd03be2adcca7622b380`.
- Reviewed JSON SHA-256: `434aac768505ec76c0c206b02fcf4a21e5d3234282097aa88ac64b60a852f192`.
- Exact retained JSON: `Task_Authoring/task_inputs-skipped/Audit-Report/Working_Files/09_Rubrics.before_platform_fix.json:1`.
- Evaluator release: `27c17cabd1bc400559798bcd275e114cbe69bb46eabd21f278183ec9f5ad3b93`.

### B14 — FAIL 2 / COMPLETE — 59 (Outcome: 59, Process: 0)

- Original report: `Task_Authoring/task_inputs-skipped/Plateform_reports/02_Rubric.md:189`.
- Report SHA-256: `14548b65e5625ed53146a3f30725cd1165bb02de04e4337b1d6527775d2d222f`.
- Reviewed JSON SHA-256: `5e1c2b9d69393f1a3841b003b6b0cb354c60a73213da582991f27c1db5a8048a`.
- Exact retained JSON: `Task_Authoring/task_inputs-skipped/Audit-Report/Working_Files/09_Rubrics.before_run2_fix.json:1`.
- Evaluator release: `f3c101b3d2271b0217501d8ccde6b7d2f0646522d71892fd93c7c627dff46a4e`.

### B15 — FAIL 2 / COMPLETE — 59 (Outcome: 59, Process: 0)

- Original report: `Task_Authoring/task_inputs-skipped/Plateform_reports/03_Rubric.md:169`.
- Report SHA-256: `bfbc3ac6d62df41a5e5f06683e7808c680e9d01ec3692277a90b5d52b3833e08`.
- Reviewed JSON SHA-256: `593ad617630993da1738995675ea6e50ef41dab69fd4f8494eccc415ac802e5d`.
- Exact retained JSON: `Task_Authoring/task_inputs-skipped/Audit-Report/Working_Files/09_Rubrics.before_run3_fix.json:1`.
- Evaluator release: `f3c101b3d2271b0217501d8ccde6b7d2f0646522d71892fd93c7c627dff46a4e`.

### B16 — FAIL 2 / COMPLETE — 59 (Outcome: 59, Process: 0)

- Original report: `Task_Authoring/task_inputs-skipped/Plateform_reports/04_Rubric.md:153`.
- Report SHA-256: `aaf1e863f891c8bdae884aafc258221fe98797c6166de71f2ad47d28d5955dcb`.
- Reviewed JSON SHA-256: `830a0a999571a8c9bd78ee785f4c49f657fce56f8a9e330443c2d8a94d4c1070`.
- Exact retained JSON: `Task_Authoring/task_inputs-skipped/Audit-Report/Working_Files/09_Rubrics.before_run4_fix.json:1`.
- Evaluator release: `f3c101b3d2271b0217501d8ccde6b7d2f0646522d71892fd93c7c627dff46a4e`.

### B17 — PASS 5 / COMPLETE — 76 (Outcome: 75, Process: 1)

- Original report: `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_3_rubric (1).md:151`.
- Report SHA-256: `d440a207c6227bd6cf6f39e36f83da7bed92c36bb1b3edad077f3a0364d6b36a`.
- Reviewed JSON SHA-256: `880f59b9298d1339c0243c510e17b03e62ae37b55a7f8b7ba6a179dcd2871248`.
- Exact retained JSON: `completed_tasks/douglas_beta_server_signoff_2026-10-28/task_inputs/09_Rubrics.json:1`.
- Evaluator release: `633dfebccbcb03e248f19b8115a04a1c41d0059abccdb332a1cb20957b2b3ddc`.

### B18 — FAIL 1 / COMPLETE — 52 (Outcome: 52, Process: 0)

- Original report: `completed_tasks/douglas_beta_server_signoff_2026-10-28/eval_reports/6ad90ea979eb9e5d89f8879f_3_rubric.md:223`.
- Report SHA-256: `1394b532749316979b2c86a879e8532675c8f5a3dc0414e6e9d7c4e1b464a75d`.
- Reviewed JSON SHA-256: `1244870fbf2ce40fa9482abaef1f9c8db43458b115fb5d2e78edc0885a290d93`.
- Exact retained JSON: `completed_tasks/douglas_beta_server_signoff_2026-10-28/work/scratch_scoring/rub/09_Rubrics.v1.json:1`.
- Evaluator release: `633dfebccbcb03e248f19b8115a04a1c41d0059abccdb332a1cb20957b2b3ddc`.
