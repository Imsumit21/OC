## Scope and verdict

The largest weakness is that the harness checks **the author’s declarations and supporting paperwork more strongly than the task’s actual dependency structure**. It can establish that records, citations, budgets, and reviews exist without establishing that:

- all requirements are jointly satisfiable;
- every graded requirement is authorized;
- 500 calls and 10 services are actually necessary;
- the rubric distinguishes complete solutions from convincing partial artifacts.

I reviewed the four supplied documents, not the referenced tool implementations or Eval files. Consequently, these are **documented gate gaps and contradictions**, not experimentally confirmed end-to-end bypasses. An independent semantic Eval might catch some; the advertised mechanical checks do not establish that it will.

Below, findings are ranked by severity. “Miss” identifies the specific missing or insufficient enforcement.

---

# Critical

## 1. No terminal gate binds all Eval results and trajectories to one task revision

**Location:**  
`GEN_EXECUTION.md` §5, “Stage gates per slot”; §6b, `chain`; §7, especially “copy each downloaded report … **if you want it beside the task**.”

**Exploit / gap:**  
Obtain Eval passes, then change SQL, references, server configuration, or human artifacts and regenerate the local check reports. The local stage chain can become current while previously passing sandbox reports or baseline trajectories describe a different task. There is no documented final-release gate requiring all five current Eval verdicts and current baseline statistics together.

This is especially significant because `/hardness`, `/oe`, and `/rubric` handoff lists omit the error/async configuration.

**Why gates miss it:**  
Local digests bind local artifacts and check reports. They do not establish a shared platform execution identity covering the universe, tool behavior, configuration, submissions, verifiers, and trajectories. Downloaded Eval reports are optional local inputs.

**Mechanical fix:**  
Require a terminal `release` gate and platform-issued `task_revision_id`. Bind every report and trajectory to hashes of:

- universe snapshot and applied SQL;
- tool catalog/runtime version and ACL snapshot;
- error/async configuration and references;
- prompt, OE, rubric, and verifier version.

Any change invalidates dependent results. Missing, unresolved, fallback-only, or mismatched results block release.

---

## 2. Joint solvability is never demonstrated by a successful execution

**Location:**  
`GEN_EXECUTION.md` §3, “Tool-call basis”: golden run “**if one exists, else the rollout average**”; “All-fail denominator.”  
`01_Scenario_Design.md` S8, “Feasibility.”  
`01_Universe_Injection.md` S6, “Platform follow-ups.”

**Exploit / gap:**  
A task can have individually plausible requirements that cannot all be satisfied together—for example, incompatible final-state expectations for one reused artifact, an unavailable write shape, or a later write that destroys an earlier required state.

All six agents can fail different subsets. No individual criterion needs to fail every run, so the all-fail checks need not expose the impossibility. A golden run is explicitly optional.

**Why gates miss it:**  
Read ACL checks, catalog existence, narrative feasibility review, and per-criterion failure statistics are not a constructive proof of simultaneous satisfiability. Rendering and regeneration follow-ups may also remain open at injection handoff.

**Mechanical fix:**  
Require a successful reference execution in an isolated platform clone, separate from difficulty baselines. It must:

1. execute the human-approved solution;
2. perform all required writes under the assigned persona and configuration;
3. pass the complete final-state verifier;
4. validate write permissions, output shapes, recipient access, and unintended side effects.

This is a solvability certificate, not a baseline success requirement.

---

## 3. Load-bearing base records can bypass the reach requirement with a reason string

**Location:**  
`GEN_EXECUTION.md` §6b, row markers: `DENIAL-INTENDED` and `UNVERIFIED-OK`.  
`01_Scenario_Design.md` S8, “Reach.”  
`01_Universe_Injection.md` S1, “1.E Persona reach.”  
Contrast: `Hardness_Manifest_Spec.md`, `persona`, requiring cited seeded records to be `YES`.

**Exploit / gap:**  
Mark a necessary base record as intentionally denied or accept unverified visibility. The stage gate expressly accepts the exception even though the row remains load-bearing. The stricter manifest reach rule covers specified seeded IDs, leaving an asymmetric escape for base evidence.

A legitimate access-denial trap does not justify inaccessible decisive evidence.

**Why gates miss it:**  
The exception requires a reason, not a reachable substitute providing equivalent information. No documented check proves the task remains solvable after removing the inaccessible record.

**Mechanical fix:**  
Separate:

- `required_evidence`;
- `optional_evidence`;
- `denied_probe`.

Require `YES` for every required record. A denied probe must identify reachable `alternate_evidence_ids` and a verified substitute dependency path. Unverified visibility must never satisfy a necessary dependency. Blocked probes must not contribute to the necessary-call floor.

---

## 4. Hazard acknowledgements convert hard coherence failures into warnings

**Location:**  
`Hardness_Manifest_Spec.md`, `hazard_acknowledgements`: “**An acknowledged hazard the SQL modifies is downgraded from a base_check FAIL to a warning**.”  
Contrast: `01_Scenario_Design.md` S1 and S8; `01_Universe_Injection.md` S7.3–4: coherence fails on the inconsistency itself.

**Exploit / gap:**  
Touch an existing silent system-state contradiction, acknowledge it, and describe intended reconciliation without actually repairing the inconsistent fields or establishing the permitted dated-claim interpretation.

The manifest explicitly supplies a warning downgrade; injection warnings can then receive narrative dispositions.

**Why gates miss it:**  
`why_safe` is explanatory text and `requirement` is optional. Neither demonstrates that the inconsistency has ceased to exist. This directly conflicts with the stated presence-based QC rule.

**Mechanical fix:**  
Remove acknowledgement-based severity downgrades. Allow only verified resolution types:

- inconsistent fields repaired;
- record excluded by an executable scope rule;
- disagreement classified as an attributed, dated claim with a valid superseding claim.

Require before/after field assertions and a mandatory requirement/scope mapping. An acknowledgement alone must never alter the verdict.

---

## 5. The incorporation graph does not connect every requirement to authoritative source text

**Location:**  
`Hardness_Manifest_Spec.md`, `requirements`, `ask_fragments`, `authorities`.  
Specifically: requirements need only be declared; fragments have no required `requirement_ids`; `delegated_by_record` is checked for membership in the immediate delegator’s records.  
`01_Scenario_Design.md` hard gates 6–7 and S4/S8.

**Exploit / gap:**  
Construct a valid-looking anchor/fragment graph while leaving a graded requirement supported only by:

- an authority absent from the delegation chain;
- a general reference that does not delegate the relevant scope;
- an amendment whose precedence is unresolved.

Every referenced R-ID can be declared, every fragment can reach an anchor, and the delegating record can exist without the requirement actually being incorporated.

**Why gates miss it:**  
The documented graph validates record linkage, not semantic authorization or complete requirement coverage. The two-reading table is likewise author-enumerated.

**Mechanical fix:**  
Add mandatory mappings:

- requirement → source record and exact span;
- source → explicit delegation edge and delegated scope;
- requirement → applicable version/effective interval;
- rubric row → authorized requirement.

Reject orphan requirements and authorities. Resolve precedence at the requirement level, not just by record age. Require semantic verification of each delegation edge against the actual record content.

---

# High

## 6. The 500-call floor is an additive estimate, not a necessity check

**Location:**  
`Hardness_Manifest_Spec.md`, `cohort.evidence_surfaces`, `call_budget`; extreme thresholds “Cohort” and “Call budget.”  
`01_Scenario_Design.md` S2 and S7.

**Exploit / gap:**  
Count the same response more than once:

- several fields from one per-record comment response;
- enumeration also counted as discovery;
- one read serving several chains;
- an already-returned record counted again during reconciliation.

`size`, `records`, fractional `per_record_calls`, and budget rows are declarations. A reason per row does not establish additive costs. Checking that one named bulk call omits a field also does not eliminate other batching or cross-surface shortcuts.

**Why gates miss it:**  
The documented gate sums numbers and checks explanations. It has no canonical request/response coverage model or demonstrated connection between cohort membership and charged calls.

**Mechanical fix:**  
Require:

- a frozen cohort membership commitment derived from an executable selector;
- required fact IDs per member;
- canonical retrieval operations, page limits, and response coverage;
- deduplication across phases and chains.

Compute the floor from distinct necessary retrievals, not independent estimates. Add a shortcut challenge: any verified correct execution below 500 calls invalidates the extreme claim. A slow golden run alone is not proof of necessity.

---

## 7. The playbook explicitly permits manufacturing “necessary” work through extra output columns

**Location:**  
`01_Scenario_Design.md` S2, “Short-circuit and sweep audit”: “**Fix by making each surface’s value an output per record**.”  
`GEN_EXECUTION.md` §3a, anti-inflation requirement.

**Exploit / gap:**  
When a surface is unnecessary to the decision, make its raw value mandatory in the output. This converts optional reads into formally necessary calls without increasing reasoning depth or business necessity.

An author can build a long transcription exercise plus a few brittle authority discoveries, while satisfying the distinct-question test.

**Why gates miss it:**  
The necessity test is circular: the author creates an output obligation, then cites that obligation as the reason the read is necessary. No gate independently tests whether the additional output serves a grounded task objective.

**Mechanical fix:**  
Require every output field to map to a source-grounded business decision, audit obligation, or downstream operation. Add a deletion test: removing a field must break a substantive required use, not merely the author-added completeness condition.

Track retrieval volume and reasoning depth separately; neither may substitute for the other.

---

## 8. Service breadth and injection volume can be supplied by redundant wrappers and companions

**Location:**  
`Hardness_Manifest_Spec.md`, `services`; “Orphan injection”: “**every injected schema appears in services**”; “Seeded ids”: exact tokens outside comments.  
Contrast: `01_Universe_Injection.md` hard gate 1 and S2, claiming record-level no-orphan enforcement.

**Exploit / gap:**  
Use Drive/Docs wrappers, mirrored GitHub/Slack activity, calendar/mail copies, and other companions to meet service and INSERT thresholds. Assign each a plausible `weight_reason` even where an agent can obtain the same decisive information elsewhere.

The documented orphan check is schema-level, whereas the playbook promises record-level mapping. Exact-token presence also does not, by itself, establish that an ID is an inserted row key in the declared service.

**Why gates miss it:**  
Physical rows, schemas, and provenance copies are not equivalent to independent information dependencies. The two documents describe different orphan-check granularity.

**Mechanical fix:**  
Parse SQL into a typed mutation inventory. Require exact `(service, table, primary_key)` mappings for every row. Distinguish semantic records from companions.

Count a service as necessary only if removing its available operations makes a required result unattainable—not merely because it stores a copy or metadata wrapper.

---

## 9. Sparse rubric checks can make the expensive part optional for passing

**Location:**  
`GEN_EXECUTION.md` §3, “Rubric set”: at most five spot checks per group plus one volume criterion.  
`01_Scenario_Design.md` S8, “Grading devices”: exact cohort multisets, aggregate invariants, spot checks, and volume.

**Exploit / gap:**  
Produce the correct membership and row count, satisfy checked examples and totals, but leave many untested per-record fields wrong. Swapping values between unchecked rows can preserve aggregate invariants.

Thus the design may require hundreds of reads, while the actual verifier rewards a much cheaper partial solution.

**Why gates miss it:**  
Membership, volume, and aggregate totals do not determine the full relation. No documented gate measures how much required output remains unverified.

**Mechanical fix:**  
Require a complete machine-checkable expected relation for objectively determined fields. Use spot checks only where full semantic checking is genuinely unavailable.

Mutation-test the verifier with:

- unchecked-row corruption;
- value swaps preserving totals;
- missing joins;
- correct counts with wrong assignments;
- incomplete dependent writes.

Every substantive output mutation must be detected by an appropriate verification component.

---

## 10. Fact checking is key-triggered and supersession exemptions are too broad

**Location:**  
`Hardness_Manifest_Spec.md`, `facts`: checking occurs where a key or alias appears in the same sentence/line; `must_appear_in` is optional; all but the newest `version_records` are exempt.

**Exploit / gap:**  
Two routes exist:

1. A fact is written without its declared key/alias, so the check never associates the value with that fact.
2. A record is listed as superseded because one clause changed, exempting unrelated still-operative facts in the same record.

The latter is especially dangerous for partial amendments retaining the rest of a document.

**Why gates miss it:**  
The checker is described as lexical and record-exempting, not entity-, predicate-, or version-scoped. It also cannot prove that the author declared every load-bearing fact.

**Mechanical fix:**  
Represent facts as scoped assertions: entity, predicate, value, unit, source span, authority, and validity interval.

Require explicit source occurrences for each decisive fact. Supersession must name exactly which predicates or spans cease to govern. Never exempt an entire record merely because one fact became stale.

---

## 11. “Independent failures” can be manufactured through labels and rubric partitioning

**Location:**  
`Hardness_Manifest_Spec.md`, `chains.root_cause` and independent-chain threshold.  
`01_Scenario_Design.md` S5, “Failure-diversity plan” and “Trap independence.”  
`GEN_EXECUTION.md` §3, “Failure patterns.”

**Exploit / gap:**  
Give three chains different root-cause strings even though one mistaken authority choice causes all three failures. Alternatively, split consequences of one error across several rubric rows so trajectories differ on enough results to count as distinct patterns.

**Why gates miss it:**  
Distinct strings and rubric-result distances do not establish causal independence. The required counterfactual—defeating all other traps while still failing this one—is prose, not an exercised test.

**Mechanical fix:**  
Add explicit dependency and root-cause graphs. Run intervention tests that independently neutralize each trap while holding others fixed. Require surviving failure mechanisms, not merely different labels.

Classify observed failures by causally supported error events; use rubric vectors as evidence, not the definition of independence.

---

## 12. Failure-pattern equivalence is non-transitive, and run denominators are underspecified

**Location:**  
`GEN_EXECUTION.md` §3, “Failure patterns,” “pass@1 gate,” “Errored runs,” and “Per-rollout spread.”

**Exploit / gap:**  
The pattern rule is mathematically ambiguous. For result vectors:

- `0000` and `1000` differ on one result;
- `1000` and `1100` differ on one result;
- `0000` and `1100` differ on two.

The first two pairs are “the same pattern” under the stated rule, but the last pair is not. Cluster order can therefore change the largest-pattern percentage.

Separately, “≤3 of 6 completed rollouts” and “≤2 of 6 errored” do not unambiguously specify launched versus completed denominators. Spread also lacks a stated population/sample convention.

**Why gates miss it:**  
Different reasonable implementations can produce different release decisions from the same six trajectories.

**Mechanical fix:**  
Specify:

- exact run accounting and pass-rate denominator;
- treatment of errors and incomplete runs;
- weighted versus unweighted per-run scores;
- standard-deviation convention;
- deterministic clustering algorithm and tie-breaking.

Prefer causal pattern labels. Publish golden test vectors at all threshold boundaries.

---

## 13. Seeded-record findability proofs cannot be obtained through the prescribed local search path

**Location:**  
`GEN_EXECUTION.md` §§1 and 4: never execute SQL; search immutable exports through `hg.py`.  
`01_Universe_Injection.md` S1.F: minted IDs must have zero hits.  
S3: per-seeded-record search proofs.  
S7.5: re-read each load-bearing value through `hg.py`.

**Exploit / gap:**  
A new injected record is absent from the base exports by construction. The prescribed search cannot demonstrate its rendered contents, search ranking, or name-based discoverability.

A broad search may return an existing similarly named record, letting the dossier mistake base findability for seeded findability. Otherwise the workflow asks for evidence its allowed tools cannot produce.

**Why gates miss it:**  
Static SQL presence and ACL overlays are not live indexing/rendering tests. No supplied contract describes an `hg.py` overlay implementing all agent-facing search semantics.

**Mechanical fix:**  
Separate base-grounding evidence from injected-runtime evidence. After platform application, require persona-scoped retrieval receipts for each necessary surface and first-link query.

Capture returned record IDs, tool/runtime version, query, pagination, and rendered fields. Until then, mark seeded findability unverified and block any downstream claim depending on it.

---

## 14. Linear comments are simultaneously the preferred decisive surface and forbidden as load-bearing evidence

**Location:**  
`01_Scenario_Design.md` S2: seed per-record decisive evidence into Linear comments.  
`01_Universe_Injection.md` hard gate 7: Linear comments are `○`, “**supporting detail only**.”  
Same playbook S4, “Linear”: comments render and are “**the strongest per-record surface**.”  
`Hardness_Manifest_Spec.md`, call-budget threshold note: at scale only Linear comments are honestly per-record.

**Exploit / gap:**  
An author following the scenario procedure builds its 300-call spine around decisive comments, then either violates the injection precedence rule or downgrades the comments to supporting detail—making the charged calls unnecessary.

The documents provide no unambiguous promotion rule after rendering verification.

**Why gates miss it:**  
The hardness budget and carrier-precedence rules encode incompatible assumptions. Numeric checks can accept a budget whose decisive surfaces another hard rule disallows.

**Mechanical fix:**  
Create one versioned carrier registry with separate fields for:

- base precedent;
- runtime rendering support;
- search/bulk behavior;
- `may_be_load_bearing`;
- verification receipt.

All playbooks and gates must use the same eligibility decision.

---

## 15. Conditional behavior and open platform follow-ups do not have a mandatory closure gate

**Location:**  
`Hardness_Manifest_Spec.md`, `call_budget.conditional_on`: gate “**reports the floor without those rows**.”  
`GEN_EXECUTION.md` §3, “Async wait.”  
`01_Universe_Injection.md` S6, “Platform follow-ups,” and Deliver.

**Exploit / gap:**  
Reach the nominal 500-call threshold using unverified behavior while the unconditional floor is lower. Carry unresolved rendering or post-regeneration checks forward as “platform follow-ups.”

A later human rubric can then depend on evidence or costs that were never confirmed.

**Why gates miss it:**  
Reporting a lower floor is not described as blocking. Injection delivery explicitly permits open follow-ups, but no supplied downstream gate requires each to be discharged.

**Mechanical fix:**  
Make `verified_necessary_call_floor ≥ profile_minimum` blocking. Conditional rows contribute zero until verified.

Store follow-ups as typed obligations with owning stage, affected requirements, required receipt, and status. Prompt/rubric/release gates must reject any unresolved obligation affecting validity or hardness.

---

# Moderate

## 16. “Task-touched data” is neither computably bounded nor independently enumerated

**Location:**  
`01_Scenario_Design.md` S1, “Scope = everything a correct run opens,” including queues/channels/folders.  
`01_Universe_Injection.md` S7.3, “Touched-data census.”  
`Hardness_Manifest_Spec.md`, `hazard_acknowledgements`, limited automatic treatment of L/R hazards.

**Exploit / gap:**  
List only clean, intended records in the census while legitimate searches return other inconsistent records in the named queues or channels. The author can satisfy category tables and cite known hazards without proving census completeness.

Conversely, literally including everything any correct run might open makes the scope unbounded by the design and can make harmless search variation change task validity.

**Why gates miss it:**  
The scope is author-declared, while the QC claim is universal. Known-hazard coverage is not full coherence coverage.

**Mechanical fix:**  
Define “touched” precisely. Require an executable task-scope selector, reference closure, and instrumentation of records returned/opened during validation runs.

Check all applicable QC categories against that inventory. Keep the six-category hazard registry and seven-category QC audit as explicitly separate coverage matrices.

---

## 17. Normal-profile selection is inconsistent and is not persisted as an effective contract

**Location:**  
`GEN_EXECUTION.md` §3a, “Horizon fit.”  
`01_Scenario_Design.md` hard gates 2–9 and S0/S9.  
`01_Universe_Injection.md` hard gate 2.  
`Hardness_Manifest_Spec.md`, normal-profile paragraph.

**Exploit / gap:**  
Scenario allows a requester-confirmed extreme design on a Normal assignment, while injection says Normal assignments use `--profile normal`. Scenario’s numeric hard gates and shown commands remain extreme.

The manifest records `horizon`, but not the selected design profile. The manifest gate merely adds a note for some profile/horizon mismatches, including one described as Wrong Horizon.

**Why gates miss it:**  
Profile is an invocation parameter rather than an immutable task property. Different stages can validate the same files under different thresholds.

**Mechanical fix:**  
Add `effective_profile`, `assigned_horizon`, and any authorized exception to the manifest. Resolve them once. Every gate reads the same values; mismatched CLI overrides fail. Generate all profile-specific requirements and commands from the single profile registry.

---

## 18. Mutable shared artifacts and backward inputs create freshness cycles

**Location:**  
`GEN_EXECUTION.md` §5, stage graph; §6b, stale-output checks.  
`01_Scenario_Design.md`, Outputs versus S2 “Mint ids now.”  
`01_Universe_Injection.md`, Inputs and final-manifest output.

**Exploit / gap:**  
The scenario PASS covers a draft manifest that injection later overwrites. Injection also consumes optional reference/configuration/hardening outputs whose stages themselves require an injection PASS.

A strictly enforced freshness model therefore creates invalidation cycles. Authors are encouraged toward same-file regeneration and procedural workarounds rather than clear revision lineage.

There is also a direct mismatch between permitting draft placeholders, forbidding template slots in gates, and requiring IDs to be minted during scenario design.

**Why gates miss it:**  
The stage model is a DAG, but actual revision dependencies contain cycles and shared mutable outputs.

**Mechanical fix:**  
Use immutable revision directories and distinct draft/final manifests. Model hardening as revision N+1 consuming revision N’s outputs. Keep intended configuration in the design revision; bind the final tested configuration at release. Define one placeholder policy per stage.

---

## 19. Human-authorship enforcement is syntactic, while required quoting can trigger its own prohibition

**Location:**  
`GEN_EXECUTION.md` §2, prep and report-only boundaries.  
§6b, `boundary`: criterion-shaped sentences in “prep or check artifacts,” replacement-wording patterns, and transcribable prompt heuristics.

**Exploit / gap:**  
Equivalent model-authored content can be distributed across cells, fragments, or different grammatical forms without matching the advertised patterns. Thus structural compliance does not establish human authorship.

In the opposite direction, a check report must quote an offending human span exactly, but that quotation can itself match a prohibited criterion shape or replacement-wording phrase.

**Why gates miss it:**  
Text shape is not provenance. The supplied rules do not describe quotation exemptions that reconcile report-only quoting with boundary scans.

**Mechanical fix:**  
Treat these scans as warnings, not authorship proof. Enforce authorship through platform provenance and input-channel restrictions. Use typed quotation blocks bound to exact source offsets; exclude verified quotations from generation-boundary heuristics.

Restrict prep artifacts to a schema of facts, locators, values, and issue codes rather than relying on sentence-pattern bans.

---

## 20. The required independent red team fails open

**Location:**  
`GEN_EXECUTION.md` §6a: scenario review “required” and gate blocks without both files.  
`01_Scenario_Design.md` S9: `RED TEAM UNAVAILABLE` causes a warning instead of blocking.

**Exploit / gap:**  
A genuine proxy outage permits release of the scenario without either independent review, despite the earlier hard-gate statement. Once network failure occurs, proceeding is explicitly permitted.

Even when available, reviewers receive the author’s design/manifest summaries, so omitted evidence or shared framing can survive both reviews.

**Why gates miss it:**  
Availability is accepted as a waiver of a required control. File presence and dispositions do not prove independent investigation of the relevant universe records.

**Mechanical fix:**  
Make unavailable review a HOLD or require an explicitly authorized equivalent reviewer. Bind review receipts to artifact hashes and require independent source checks for critical findings—not only review of the author’s summaries.

---

## Recommended fix order

1. **Add revision-bound final release and positive solvability gates.**
2. **Remove reach and coherence waivers that accept reasons instead of evidence.**
3. **Connect every graded requirement to scoped authoritative source text.**
4. **Replace declared call/service totals with deduplicated dependency evidence.**
5. **Mutation-test rubric coverage against complete expected outputs.**
6. **Unify carrier eligibility, profiles, and revision handling.**

More citations, longer self-reviews, or additional model reviewers will not close the central gap: **the harness needs independently checked task dependencies and executable witnesses, not merely better-supported author assertions.**

