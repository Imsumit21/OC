# Pipeline, provenance and release forensics

Audit date: 2026-10-28. Scope: read-only inspection of the create wrappers, shared contract, current validators, batch execution records, five named task histories, completed-task archives and the older `archived task/task_inputs-n` history. Only this new report and audit scratch files were written. No SQL, evaluator run, paid model run, email, Portal action, source mutation or original-artifact edit was performed.

## Finding in one paragraph

The evidence does **not** support “the create skills were never run” or “there are no gates.” It supports a more specific failure chain: the batch deliberately stopped at four local authoring gates; the local gates verify many bindings and mechanical properties but still depend on the author's semantic judgments; some declared difficulty floors were vulnerable to bulk/short-circuit routes; later repairs changed the artifact being certified or evaluated; and external returns sometimes describe different input bytes, clocks, sources or even scenarios. A local PASS, a Portal report PASS, a completed trajectory, and a submitted task are distinct states. Several later task histories preserve that distinction correctly. Collapsing those states into a single CLEAN/PASS label creates the apparent contradiction and makes retries hard to diagnose.

## Confidence and evidence rules

- **Proven in this audit:** directly read code behavior, literal saved command/output blocks, exact file sizes/hashes, or contradictions between identified saved records.
- **Recorded historical claim:** batch event or author/reviewer narrative. It is evidence that the claim was recorded; it is not a recovered shell transcript or a fresh semantic validation.
- **Inference:** a causal explanation consistent with code and observed reports, explicitly identified below.
- **Unknown:** original command transcripts, exact historical executable versions, unseen remote context, or missing raw trajectories. Absence of a local record does not prove an action never happened.

The audit's reproducible inventories are `scratch/pipeline_slot_and_run_inventory.json` and `scratch/pipeline_certificate_integrity.json`. The latter compares saved certificate digests with current files using the unchanged digest functions, without running gates or querying the base. Context JSON is read as saved rather than regenerated. Thus “digest-current” below is narrower than a fresh gate PASS.

The parent audit's wider imported-report census is 91 saved report paths / 84 unique report documents, not 84 proven independent review executions (`evidence/report_manifest.json:3–8`; `TASK_VERDICT_HISTORY.md:3–5`). Its mailbox-qualified finding is three distinct sent canonical tasks with attributable returned FAILs—Reviewer A, Reviewer B and Reviewer C—while Reviewer D is unbound and Reviewer E has no preserved return (`evidence/MAILBOX_PROVENANCE.md:7–19`). Those mailbox facts were independently inspected by the parent; this sub-audit did not access or send email. The older archived/completed report groups remain useful causal evidence without being counted as additional verified contributor-delivery failures.

## 1. What the actual create pipeline promises, and what the batch actually completed

### The wrappers are procedural contracts

`Task_Authoring/skills/create-injection/SKILL.md:8–12` tells the agent to read `GEN_EXECUTION.md` and the playbook. It is Markdown guidance, not an executable wrapper that proves those reads happened. Its actual handoff command is `stage_gate.py injection ... --paste` (`:31–35`). The other wrappers use the same pattern: scenario `:40–43`; prompt writing `:36–40`; hardening `:35–39`; OE writing `:33–37`; rubric writing `:36–40` in their respective `SKILL.md` files.

The shared contract requires source validation, actual source grounding, mechanical checks, adversarial self-review and a PASS gate before handoff (`Task_Authoring/setup/GEN_EXECUTION.md:359–412`). It explicitly says the evidence sidecar supports review rather than proving semantics (`:79–83`, `:468–475`). Consequently, an artifact bearing a correct skill filename or a saved PASS block is not complete evidence that every playbook instruction was followed. Recovering the original tool transcript would be needed to authenticate that stronger claim.

### The batch had an explicitly reduced finish line

This is a **proven scope distinction**, not evidence of an unauthorized gate bypass:

- `Task_Authoring/batch/TASK_RUNBOOK.md:5–7` defines the goal as SQL + prompt with scenario/injection/prompt-writing/prompt-check PASS, and says `/injection` and `/prompt` reviews are not run in that batch.
- `:81–119` says guide steps 0 through 5e only, records the two reviews as skipped, and places human time, precheck, hardness, baseline, OE and rubric outside scope.
- `Task_Authoring/batch/ORCH_STATE.md:83–88` records the 13:36Z decision to drop the paired reviews to save tokens and modify verification/package/dashboard behavior accordingly.
- `Task_Authoring/batch/verify_task.py:8`, `:20–38` reruns exactly four gates and packages assignment, SQL, prompt and prompt-check. It does not run release or assert Portal clearance.
- `Task_Authoring/batch/audit_sweep.py:33–75` subsequently adds inexpensive lexical/preflight screening to the same four gates. Its CLEAR status cannot establish source semantics, UGT, real difficulty or Portal acceptance. Reviewer D's phase-1 and phase-2 CLEAR claims are visible in `Task_Authoring/batch/audit/TASK_D.json:1–14` and `.phase2.json:1`.

`Task_Authoring/batch/ORCH_STATE.md:92–99` records that the later first four audited prompts failed their first `/prompt` review while Eval0 passed. That is useful contemporary evidence of screening weakness, but it is a summary of those reviews, not a statistically representative failure rate for all tasks or independent authentication of every original report.

**Root cause:** the delivery vocabulary did not travel with a machine-readable stage scope. “CLEAN” was valid for the reduced batch definition, but it was unsuitable as a blanket readiness claim for Portal, difficulty or submission. Do not characterize the deliberate review omission as a failure to follow the then-recorded scope.

## 2. Evidence of skill generation versus evidence of command execution

Path convention: a code basename always denotes `Task_Authoring/tools/<basename>`. In each task subsection, a relative `Audit-Report/` or `Working_Files/` path is rooted at the exact `Task_Authoring/task_inputs_<full task ID>/` named in its heading; audit evidence paths are rooted at this report's directory.

The following records establish stage activity and saved gate outputs. They do not recover an unabridged command-by-command transcript of the original skill invocations.

| Task / person label | Historical execution evidence | What it establishes / what remains unknown |
|---|---|---|
| Reviewer A `...TASK_A` | `Task_Authoring/batch/events.log:105–107`, `:190–194`, `:280–291`; saved design/dossier/brief/check files | Recorded scenario → injection → prompt stages, including a recheck after an SQL revision. The four current core certificate bindings match current file/virtual digests in this audit. It does not prove every wrapper/playbook read. |
| Reviewer D `...TASK_D` | `Task_Authoring/batch/events.log:95–98`, `:177–181`, `:233–234`; sent snapshot prompt-check `Task_Authoring/task_inputs_TASK_D/Audit-Report/20261024T165457Z_email_1a16ed677b050dd3/sent_snapshot/04_Prompt_Check.md:148–161` | Recorded generation and driver recheck for the **PlayableX** pair; the current four saved core certificates are digest-current. It does not certify the materially different returned screenshot task. |
| Reviewer B `...TASK_B` | `Task_Authoring/batch/events.log:132–135`, `:145`, `:195–196`; many preserved actual gate logs in iterations 1–18 | Recorded create pipeline and later actual validation attempts. Current core, OE-writing and OE-check certificate bindings match. Historical/current nested hardening logs must be distinguished. The human-time certificate is now stale on OE bytes. |
| Reviewer C `...TASK_C` | `Task_Authoring/batch/events.log:129–131`, `:230–231`, `:302–307`; iteration-6 actual FAIL logs | Recorded original PASS followed by a later blocked revision. Current old PASS blocks are stale; the current status already records failure. This is not current gate clearance. |
| Reviewer E `...TASK_E` | `Task_Authoring/batch/events.log:330–338`; `Task_Authoring/batch/reviewer_handoffs/TASK_E/20261024T092358Z/stage_inventory.json:19–43` | Recorded scenario/injection/prompt stages plus saved bindings; the handoff explicitly says no gate rerun occurred during that inspection. Current four core bindings match. No returned Portal review evidence is established by that handoff. |

### Version qualification is material

The current SHA256 of the sorted concatenation of `Task_Authoring/tools/*.py` is:

`4459b8bdd4decccf64864a4fa2e52c9906544d40ade65c7bf4e12550b3d35991`.

All four named core stage certificates for each of the five target tasks record `__gate_policy__#4459b8bdd4de`, matching the current implementation's fingerprint convention (`Task_Authoring/tools/stage_gate.py:482–491`). This makes current tool behavior relevant to those certificate claims. It does **not** preserve an entire historical environment: the fingerprint covers those Python files, not all skill Markdown, playbooks, guidelines, catalog/schema/ACL text or an external evaluator package. A hash claim is also not a command transcript.

Older evidence differs. `archived task/task_inputs-n/Working_Files/04_Prompt_Check.md:108–113` records an older UFL/CODE/CHECKS/KB digest format and an actual FAIL with two upstream failures. Completed Douglas files identify `Task_Authoring-2/task_inputs` and `--profile long`, whereas current code uses the current profile vocabulary (`completed_tasks/douglas_beta_server_signoff_2026-10-28/task_inputs/Working_Files/04_Prompt_Check.md:98–113`). Their historical gate implementation cannot be reconstructed just by reading today's code.

## 3. What current code already protects

These are existing controls and should not be proposed as absent features:

| Existing protection | Exact implementation | Practical limit |
|---|---|---|
| Explicit V3 assignment/persona/source context | `Task_Authoring/tools/stage_gate.py:455–478`; `Task_Authoring/tools/task_context.py:230–246` | A ready registered source is not proof of all historical facts or the remote runtime's identical source. |
| Required inputs/outputs, sections, placeholders and input/output freshness | `Task_Authoring/tools/stage_gate.py:524–593` | Presence, source pointers and mtimes do not prove a statement is true. |
| Artifact, context, assignment, local policy, tool policy and per-stage review bindings | `Task_Authoring/tools/stage_gate.py:482–519` | Many digests are 12-hex prefixes. Markdown/text digests normalize whitespace and exclude pasted output. |
| Upstream current PASS, fail-closed crashes and no success after a blocking finding | `Task_Authoring/tools/stage_gate.py:2550–2584` | The authoritative state must actually be checked at handoff; a stale dashboard label can survive later edits. |
| Tool reruns and rejection of unsupported shortcuts/conditional floors | `Task_Authoring/setup/GEN_EXECUTION.md:425–448`; `Task_Authoring/tools/hardness_gate.py:339–395` | Whether declared calls are truly necessary still depends on correct claims about tool behavior and short circuits. |
| Persona visibility and denied/unverified probes needing visible alternate evidence | `Task_Authoring/tools/stage_gate.py:679–753` | Current visibility alone does not prove channel membership at a historical freeze; runbook explicitly recognizes this at `Task_Authoring/batch/TASK_RUNBOOK.md:157–160`. |
| Rubric source values actually reread, exact prompt spans, paths, temporal and Pacific/UTC evidence | `Task_Authoring/tools/v3_artifact_checks.py:97–131`, `:265–366` | Path linkage, source interpretation and semantic duplicate facts remain reviewer judgments, as the code explicitly says. |
| Release current-certificate/bundle checks, unresolved markers, OE solvability and recalculated difficulty | `Task_Authoring/tools/stage_gate.py:1683–1722`, `:1783–1852` | Static release does not replay the task, certify Portal inputs, or prove actual submission. |
| No PASS by skipping expensive reruns | `Task_Authoring/setup/GEN_EXECUTION.md:445–447`; `Task_Authoring/tools/stage_gate.py:2579–2584` | `--rerun lint` can only reach PARTIAL under ordinary final verdict handling. There is no evidence here that it was used to mint the cited core PASS blocks. |

Current release requires the core later stages and optional stages when their artifacts exist. The 29-root inventory found **no primary `13_Release_Gate.txt` certificate** among the canonical task roots inspected, while 25 verifier slots were zero bytes. This does not prove nobody submitted remotely; it proves the preserved local folders do not establish formal current release completion. Zero-byte scaffolds and `[]` are not completed later-stage artifacts.

## 4. Why mechanically valid authoring can still fail review

### Semantic checks are partly attestations

`Task_Authoring/tools/v3_artifact_checks.py:134–152` checks that the recorded reviewer/rationale exist, artifact hash matches, role matches, source IDs exist, and accepted-outcome/alternative arrays are nonempty. It does not independently decide whether the alternatives are the strongest plausible ones. `:283–291` explicitly describes semantic role judgment as belonging to the reviewer. Rubric checks are stronger: they reread literal source values and check each evidence-path node, but `:365–366` still states that path linkage remains review judgment. `Task_Authoring/tools/stage_gate.py:618–641` counts evidenced counter-readings and required topic mentions; it cannot establish that the counter-reading actually defeats the current reasoning.

Therefore, “add more self-review rows” would not address the core gap. The existing system already requires many rows. An independently derived output/authority model and adversarial alternative cases would test the judgment itself.

### Difficulty declarations can overstate unavoidable work

`Task_Authoring/tools/hardness_gate.py:343–370` multiplies declared per-record calls by declared record counts. It requires `why_no_bulk`, `short_circuit`, incorporated requirements and decisions. `:372–392` counts budget rows as verified-floor work when they lack `conditional_on`, and requires a nonempty necessity reason. These are useful controls, but the code does not prove a nonempty reason or the absence of `conditional_on` is true.

Reviewer C's history supplies a concrete example: `Task_Authoring/batch/events.log:129–130` recorded a 502-call floor while flagging a date-sweep shortcut; `:230–231` passed the original injection while disclosing an open approximately 160–260-call route. Later truthful accounting leaves 0 per-record calls and only 3 unconditional calls under the extreme thresholds, recorded in current `Working_Files/BATCH_STATUS.json:1`. The iteration-6 actual gate log `Audit-Report/iteration_06_mode_b_precheck/validation/stage_gate_injection.txt:14–22` has lint/base/fact/reach clean but the hardness tool FAIL; `:31–33` identifies the old PASS as stale and refuses to paste a new one. This shows both an earlier semantic budget weakness and the later gate functioning correctly once inputs were corrected.

**Inference:** the incentive to hit a fixed service/volume/call floor encourages long declared work and extra carriers before the shortest correct execution route is established. The source-backed anti-inflation rule already exists (`Task_Authoring/setup/GEN_EXECUTION.md:216–225`); enforcement needs a real shortest-path/bulk-route challenge, not another version of the same prose declaration.

### Content and presentation fixes have different dependency costs

Changing SQL, a governing source, requester identity or task meaning can invalidate a previous run even if the visible prompt is unchanged. Changing only criteria requires regrading rather than claiming new model behavior. These are existing rules: `Evals/WORKFLOW.md:907–926` requires fresh matching runs after task/environment changes and new verifiers after rubric changes; it warns that matching manifests alone do not prove freshness. `Task_Authoring/setup/GEN_EXECUTION.md:348–356` requires downstream gates after hardening revision N+1.

The remaining operational weakness is maintaining current applicability across many iteration folders and independently returned files. A report-backed fix can be correct locally while its prior Portal PASS is no longer applicable. The solution is an explicit dependency/applicability state, not silently “carrying forward” a verdict.

## 5. Task-by-task provenance and current applicability

### Reviewer A `TASK_A`

The current SQL is `66d4dde4161e0627…`, prompt `cdf0185da882a7b7…`, OE `49a674c1a82f6801…`, rubric `56afe66ca2a3c90e…` (full hashes in scratch inventory). The seven saved local certificates through OE-check are digest-current under the audit method; the rubric-writing saved result is FAIL and the plan has changed after that result. The current zero-byte human-entered human-time/verifier slots prevent claiming a completed platform workflow.

The Portal clock is demonstrably different from the local assigned freeze. The original OE report `Audit-Report/iteration_09_oe_portal/6ad90e93a2c3542255f64fbf_2_oe.md:47`, `:101–106` calls 00:00 UTC an error and demands 00:00 PT / 07:00 UTC; it grades the actual seven-hour difference as Minor because no relevant record changes the outcome. This is a real review finding, but not proof the local V3 mapping should silently be changed. That authority conflict requires the actual external context, as discussed below.

The canonical precheck and six baseline JSONs contain actual runtime model labels, including init `claude-opus-5-5[1m]` and assistant `claude-opus-5-5`; the scratch inventory records distinct sessions and terminal results. They do not by themselves authenticate the SQL/prompt/reset configuration used. Do not infer six-run difficulty from their mere presence, especially with an empty verifier slot.

### Reviewer D `TASK_D`

This is the strongest example of a **version attribution failure**, not an established failure of the sent create artifact. The local/sent PlayableX pair remains SQL `2decd123d847b5a8…` and prompt `177495c38f62720e…`. The received report matches a different screenshot-refresh pair, SQL `4e4b5243e220b9e5…`, prompt `527690cbc023ad5d…`.

The original returned hardness report `Audit-Report/20261024T165457Z_email_1a16ed677b050dd3/originals/6ad90e94adb09db24624b216_1a_hardness fail report current injection.md:5`, `:18–21` calls `6ad90e94adb09db24624b216` an **attempt**, with task ID withheld; it does not identify a second known task. `:28–31` records model/run/source claims, `:107–109` discloses no opening user turn and only one reviewed run, and `:113–133` concludes Too easy / FAIL 1 / HOLD. Those findings apply to the returned bytes, not the sent PlayableX pair.

The preserved reconciliation is explicit: `version_reconciliation.md:9–11`, `:15–39` establishes a changed scenario, different requester and outputs, zero overlap of parsed inserted record identities, Hard-versus-Medium assignment difference, and a UTC-versus-PT clock difference. `:43–53` says the raw trajectory and matching injection/prompt reviews are missing, evaluator snapshot is unverified, attribution is pending, and no Mode B edits began. That restraint is correct. A count of “Reviewer D create output failed hardness” would be unsupported until task identity and redesign provenance are resolved.

### Reviewer B `TASK_B`

Current SQL `cb99b9c076cdc456…` and prompt `9d9735b4cb1493d4…` are bound by the iteration-17 returned reports to injection PASS, prompt PASS 5 and hardness NON-FAIL 3 / Hard / PROCEED. The evidence handoff states this precisely at `Audit-Report/iteration_17_report_baseline_intake/OC_TASK_B_iteration_17_evidence_handoff.md:3–5`, `:16–34`. It separately discloses external SynthCut/local-source/clock differences.

The accepted current-pair hardness trace is `3ce363081b9be573…`, while canonical `06_PreCheck_Trajectory/trajectory.json` remains historical `765f4052113afdcc…` from SQL `35296a98…`. The same handoff `:36–59` and `trace_review/trace_session_input_provenance_review.json:95–129` document seven distinct completed sessions, absent initial prompt/batch/revision/reset metadata and candidate-baseline nonpromotion. Observed matching source locators and absence of cross-session echoes are useful bounded evidence, not authenticated full runtime input/reset proof. Retaining the old canonical file is safe preservation, but it must not be mistaken for current precheck applicability.

The human-time saved PASS is **currently stale**: `Working_Files/05_Human_Time_Worksheet.md:177` certifies OE digest `e6161c0a9e2f`, while the current gate-normalized OE digest is `a752fc82666b`. The worksheet's other recorded digests match. `Working_Files/BATCH_STATUS.json:17` still presents its prior validated human-time state. This is a concrete status-refresh gap after later OE changes, not a new finding about the arithmetic or a new gate run.

A later external OE PASS also initially did not belong to the canonical local OE: iteration-21 `report_binding_comparison.json:8–35` records reviewed hash `b8972076…37dd6fa`, local hash `2a1e6416…d9a74fe8`, a 139-byte difference and `same_artifact: false`; `:58–74` refuses to reconstruct or apply that PASS locally. Preserve subsequent exact-artifact reconciliation separately; a PASS heading alone must never close this identity check.

The canonical rubric is **absent at audit time**, not a currently populated or passing artifact (`evidence/canonical_slot_snapshot.json:71–74`, independently consistent with the scratch filesystem inventory). Historical iteration-31 `copy_verification.json:2–15` records `copied_and_verified` for a 36,928-byte, 45-row rubric with SHA256 `34d1d4f11d0182d7f4cf61f3b751b5f04beae354e8bab6b78662334af6df5042`; `:19–23` expressly says no validator rerun, formal PASS or Portal PASS claim. These are different observations at different times. The audit did not delete, restore or fill the slot, and the records do not establish why the canonical file is absent now. Review candidates/history must not silently substitute for the missing canonical slot.

### Reviewer C `TASK_C`

Current SQL is `8b23be8069b40c68…`, prompt `3715dc04349170ed…`. The original saved injection PASS certifies SQL `3a5adccd5061…`; prompt-writing/check have changed report/brief/review bindings. All are now stale in the independent digest comparison. Current `Working_Files/BATCH_STATUS.json:1` correctly records BLOCKED / injection/prompt/hardening FAIL and says no empirical success or certified release. It retains prior CLEAN only as history and describes prior Portal injection PASS as applying to the earlier input only.

The actual iteration-6 injection log has 1 blocker and identifies the stale old PASS (`:1`, `:17`, `:31–33`). Therefore it is inaccurate to count an old pasted PASS as proof the new candidate was allowed through current gates. The unresolved work is substantive profile feasibility and current-run applicability, with the separate model-label issue below.

### Reviewer E `TASK_E`

Current/sent SQL `72ca392990bab978…` and prompt `3ffe1dd19aac1be3…` have digest-current core certificates. `Task_Authoring/batch/reviewer_handoffs/TASK_E/20261024T092358Z/stage_inventory.json:8–43` records matching sent bytes, saved-pass integrity and no gate rerun during inspection. `:57–75` records empty human-time/OE/verifier slots and a three-byte rubric scaffold.

The handoff's `next_stage_handoff.txt:126–133` explicitly lists complete initial `/injection` and `/prompt` reports as pending and says no Portal-pass evidence exists in that folder. It does not establish a Portal failure or a returned current task. “No returned review established” is the supported classification; “Reviewer E's artifact failed” is not.

## 6. Run provenance is a separate unclosed mechanical requirement

### Current code authenticates model/structure, not exact runtime task inputs

`Task_Authoring/tools/stage_gate.py:1730–1745` reads a nonempty precheck, structural completion and extracted model strings. It does not compare the trace to prompt/SQL hashes, a task revision, universe ID, applied-injection receipt or reset receipt. Release's trajectory test at `:1846–1852` adds parseable nonempty JSON, not those associations.

`Task_Authoring/tools/difficulty_stats.py:644–665` obtains run numbers from filenames, rejects duplicate/missing run-number slots, requires six slots for V3 and records model provenance. `:675–688` binds verifier titles to rubric rows and rejects missing/unbound rows. Those protections are real. But neither filename mapping nor recorded model family proves a platform baseline slot, common batch/revision, input pair or reset. An authenticated run manifest should supplement, rather than replace, these checks.

`Evals/WORKFLOW.md:757–765` already warns that an input manifest fingerprints reviewed inputs, not trajectory-generation provenance; `:923–926` warns that a matching manifest does not prove freshness. The Reviewer B evidence demonstrates this is a practical issue rather than a hypothetical one.

### Proven parser compatibility failure: `[1m]`

`Task_Authoring/tools/difficulty_stats.py:165–170` normalizes `claude-` and periods/spaces, then permits only a `-`/`@` alphanumeric suffix. `claude-opus-5-5[1m]` therefore fails while `claude-opus-5-5` passes. `trajectory_models():173–187` collects both init and assistant labels; `v3_precheck()` requires all of them to pass. The Reviewer B trace review `:105–106` confirms canonical terminal/model-usage and raw label distinctions, and its handoff `:55–57` records the actual formal hardening hold caused by this matcher.

This is a specific local false negative and can prolong a repair cycle despite a real Opus 5.5 run. It is **not** evidence that every failed task was merely a parser problem. Reviewer C also has genuine hardness/profile and stale-chain failures; Reviewer B has independent run-binding and downstream-completion gaps. Preserve raw evidence. Any separately authorized maintenance should recognize only the documented variant, retain wrong-family/mixed-model rejection, and test raw labels without rewriting trajectories.

## 7. Three authority/source seams need explicit reconciliation

### Clock: local V3 UTC, older Evals fixed February, returned Portal October PT

1. Current authoring explicitly maps October/February assigned dates to 00:00 UTC (`Task_Authoring/setup/GEN_EXECUTION.md:60–73`; `Task_Authoring/references/v3_policy.json:5–8`). The V3 course note says both freezes are 00:00 UTC (`Task_Authoring/references/Docs/11_V3_Changes.md:40–49`).
2. Current local `Evals/EXECUTION.md:81–84` still states its fixed `2026-02-14 00:00 UTC` clock remains authoritative. Create-side authority says changed V3 topics supersede conflicting older Evals text (`Task_Authoring/setup/GEN_EXECUTION.md:23–31`). A reviewer running Evals without the create-side mapping can consequently apply a different rule.
3. Returned Reviewer A/Reviewer B/Reviewer D reports repeatedly declare October 1 at **00:00 PT / 07:00 UTC**, and Reviewer A/Reviewer B OE reviews flag local UTC wording as Minor. Reviewer B iteration-20 `report_binding_and_intake.json:14–31`, `:41–57` records the absent external context preimages. Iteration-21 `report_binding_comparison.json:58–69` preserves the unresolved context evidence rather than inferring clock from hashes.

This is a **proven authority inconsistency** with a concrete reported review cost. It is not enough to infer which external code/configuration was wrong. Require the actual assignment/display mapping, external `ENVIRONMENT.md`, source/runtime version and report context preimage before changing a task clock. The seven-hour boundary needs explicit outcome-delta analysis. Some reviews found no material change; that does not establish all tasks are unaffected.

### Source identity: shared local universe versus external SynthCut

`Task_Authoring/references/universe_sources.json:3–17` deliberately maps both local dates to one shared source and treats archive clock as metadata. `Task_Authoring/tools/task_context.py:150–200` validates paths/source manifests and, in shared mode, that source metadata is not earlier than the freeze. It fingerprints cheap service manifests rather than all source-body bytes (`:186–200`). This is a sensible local source registry, not an attestation of the remote Portal dataset.

The batch itself warns that live `hg4-synth-sep30cut` may differ from the local copy extending to February (`Task_Authoring/batch/TASK_RUNBOOK.md:147–163`). External reports cite SynthCut manifests; Reviewer B handoff `:32` preserves that difference. Local search/ACL/KB proof must therefore be scoped to the local source and dated state. A ready context does not establish external source equivalence, mutable earlier content or historical membership. The shared-source choice is recorded policy, not proof it caused any particular unseen Portal failure.

### Difficulty/authorship/local overrides

- `Task_Authoring/setup/GEN_EXECUTION.md:108–136` explicitly allows Claude/Codex authorship as a local exception while recording that official V3 requires human authorship. This is a compliance divergence, but no reviewed evidence here proves it caused an AI-detector rejection.
- `:186–225` preserves Long → extreme, ≥500 necessary calls, ≥300 per-record calls and broad schema/row floors, including Easy assignments. Empirical V3 Long-Horizon basis is ≥100 calls and the assigned score cap is separate (`:148–151`). Local design floors can therefore fail a task that meets Portal's horizon/difficulty rule, or pass a declared design that is empirically easy.
- `:155`, `:436–437` enforces zero **predicted** all-fail rows and discovery-authority share ≤50%, stricter or additional to Portal quality scoring. Do not confuse predicted impossible/unsupported all-fails with valid observed model failures. Completed Douglas records 17 observed VALID all-fails, while the local plan flags a common authority at 100% (`completed_tasks/douglas_beta_server_signoff_2026-10-28/README.md:12`, `:24`; its plan `Working_Files/09_Rubric_Writing_Plan.md:210`, `:348`).
- The batch also records changing all tasks to Hard regardless of CSV (`Task_Authoring/batch/TASK_RUNBOOK.md:121–128`; `Task_Authoring/batch/ORCH_STATE.md:13–14`). The sent/local assignment and external original assignment must be compared, not silently assumed equivalent. Reviewer D's returned report specifically says Medium.

These choices should remain visible as local design constraints, official acceptance constraints, or unresolved conflicts. They are not interchangeable verdicts.

## 8. Wider corpus: success, stale certificates and historical tool limits

The wider corpus contradicts a universal claim that create outputs cannot pass:

- `completed_tasks/frederick_account_handover_2026-10-26/README.md:8–12` records three hardening rounds, OE PASS after Minor repairs and accepted V3 Medium average 80.8% despite missing the author's older <75% target. This is an archive's acceptance claim; without submission proof it is not an independently verified Portal acceptance event. Its rubric check `Working_Files/09_Rubric_Check.md:96` openly retains a local authority-share plan failure as a design issue.
- `completed_tasks/douglas_beta_server_signoff_2026-10-28/README.md:8–12` records three earlier difficulty misses, OE NON-FAIL→PASS and rubric FAIL→PASS. `:20–24` says grouped-rubric projections were wrong across three rounds and the local authority-share failure did not affect the platform. Its current saved prompt-check header is `a0414d89216a` while the embedded PASS block binds prompt digest `f5f6a459f6df` (`Working_Files/04_Prompt_Check.md:98–105`). This is preserved revision history/staleness, not a current certificate or evidence of fabrication.
- `completed_tasks/frederick_card_spend_q3_TASK_U/README.md:8–12` records injection/prompt/OE clean reviews, hardness PROCEED and four rubric rounds. Its final SD 0.054 also illustrates why a claimed completed/submitted workflow must not be equated with all current local gates passing.
- `archived task/task_inputs-n/Working_Files/04_Prompt_Check.md:8–10`, `:108–113` says READY for prompt in the content review while **handoff remains blocked** by stale upstream gates. Its Portal prompt report `(3).md:19–24`, `:531–551` binds a particular older SQL/prompt/evaluator release and records NON-FAIL 3 / COMPLETE. Its hardness report `:13–26`, `:140–158` records PROCEED 4 for an observed **claude-opus-4-8** run, evaluated by Opus 5.5; assessed-model and evaluator-model are different fields. Today's Opus-5.5-only authoring rule cannot be retroactively substituted for that historical review.

Task names, file names, report numbers and inherited PASS prose are weak provenance. Exact artifact version, selected evaluation policy, assessed model, source/clock and applicability determine whether evidence transfers.

## 9. Prioritized improvements, without implementation

### P0: Make handoff identity and stage scope mandatory

Produce a single immutable handoff manifest for each candidate, with full SHA256/bytes for assignment, SQL, prompt, OE, rubric, reference files and friction; stable local task ID **and separate attempt ID**; candidate revision; persona/mode/freeze/timezone; source/runtime ID; local gate state and Portal stage state separately; and pending evidence. Include it in every returned-review intake. Reject automatic adoption on mismatch, preserving both versions. This generalizes the strong Reviewer D/Reviewer B reconciliation already practiced; it does not require redoing their completed acquisition work.

Use explicit statuses such as `LOCAL_CORE_GATES_CURRENT`, `PORTAL_PROMPT_CURRENT`, `HARDNESS_CURRENT_RUN`, `BASELINES_BOUND`, `RELEASE_CURRENT`, `SUBMITTED_WITH_PROOF`. Compute applicability from hashes rather than inheriting a CLEAN/PASS label. The Reviewer B human-time stale certificate should surface automatically as a dependent refresh requirement after OE edits.

### P0: Close run-to-input provenance, preserving raw traces

Require a platform/runner receipt associating each run hash/session with exact task revision, prompt/SQL/configuration, universe snapshot and reset/isolation identity, and its actual baseline slot/batch. Keep model and completion checks, filename/run-count checks and verifier/rubric binding checks. Do not “fix” evidence by renaming files, injecting missing initial prompts, normalizing raw models or treating attachment download order as run slots. Where authenticated runtime evidence is unavailable, mark that exact applicability gap instead of running more paid trials without knowing what they certify.

### P0: Reconcile clock/source/policy before further content repair

Resolve the local V3 UTC / returned PT / older Evals clock and source mapping with actual configuration evidence. Record a task-specific boundary delta and accepted policy version. Avoid changing correct source values merely to make an unverified external context hash or clock claim agree. Package the authority mapping for external review so V3 fair outcomes, role/date rules and preserved local exceptions cannot be silently replaced by older overrides.

### P1: Test semantic acceptance independently of author attestations

For each request, independently derive the incorporated authority chain, valid outputs, recipients/destinations, cutoff state and strongest materially different fair alternative. Review actual source fields and all affected sibling cases after a report fix. Require examples that would pass under each valid interpretation and counterexamples that must fail. Use the existing sidecar/source reread machinery as evidence binding; add substantive adversarial cases rather than more checklist prose or source-ID counts. Do not repair a rubric solely to depress model scores.

### P1: Validate shortest correct routes before expensive hardening

For every high-cost phase, challenge bulk APIs, complete list/search responses, server-side filtering, newest governing source, conditional work and stop rules. Preserve a measured call-cost evidence table keyed to real response shapes. Make conditional assumptions explicit; the existing `conditional_on` behavior correctly excludes unverified work. A discovered cheap route must invalidate the declared floor even if the prose necessity reason is nonempty. Separate the optional extreme-design constraint from empirical V3 difficulty so a structural floor failure is not mistaken for a Portal failure.

### P1: Repair model-label compatibility as separate validator maintenance

Recognize the documented `[1m]` Opus-5.5 variant without accepting arbitrary bracket text or wrong/mixed models. Test raw init/assistant/terminal combinations. Preserve all original labels and old FAIL logs; record the validator version at rerun. This is a concrete improvement to existing checks, not permission to claim baseline provenance or current-input applicability is resolved.

### P2: Strengthen version fingerprints and reporting discipline

Include resolved skill/playbook/contract/guideline/catalog/schema/ACL/source-registry versions in the execution receipt, alongside the current Python-policy fingerprint. Keep raw byte SHA256 and semantic normalized digests distinct. Current text digesting strips blank lines/edge whitespace and excludes gate output (`Task_Authoring/tools/stage_gate.py:352–373`); directory digesting uses basename+bytes (`:365–370`), so it does not fully encode reference-file relative paths. Use full relative paths and full raw-byte digests for portable exact delivery identity. There is no evidence these digest details caused the observed Portal findings; they are hardening opportunities.

Preserve the evaluator's actual report/record/release package where possible. `Evals/WORKFLOW.md:693–765` already mandates verified writer receipts, fixed output paths, per-stage fingerprints and no fabricated reports; `Evals/tools/hg_eval_release.py:33–67` rejects current-release relabeling of old/unbound reports. Apply those controls at handoff and summarize historical-version reports separately. A passing report with no matching artifact or context preimage should remain a report about its stated input, not become the canonical candidate's certificate.

## 10. Remaining limits

This audit does not rerun original gates, assess every corpus report semantically, authenticate remote submission, recover the original CLI histories, or establish external universe/configuration equivalence. The audit contains a 29-root structural/hash inventory and targeted evidence-based pipeline analysis, not a population-level failure-rate estimate. Original records may contain truthful historical PASS results that are no longer applicable after edits. Missing evidence is labeled unknown/pending, not treated as an execution failure or denial. No action was denied and no external mutation has an uncertain outcome.
