## Scope and overall assessment

This audit covers the three supplied playbooks. The gate implementations, upstream playbooks, and referenced eval files were not supplied, so I distinguish **explicit acceptance loopholes** from **missing enforcement requirements**. I do not assume an external gate closes an undocumented gap.

“Accepted” below includes **scored NON-FAIL**, which `09_Rubric_Coverage_Plan.md → Deliver` expressly permits.

The central problem is that the harness measures **documented effort, declared dependencies, and largely static consistency** more strongly than it establishes **necessary effort, executable solvability, and complete grading**.

---

# Critical

## 1. Observed call counts can certify an easy task as extremely hard

**Location**
- `08_Evidence_Ledger.md → Purpose`: minimum measured on a 100%-scoring golden run, otherwise the six-rollout average.
- `08_Evidence_Ledger.md → Check report → Reminders`.
- `04_Prompt_Brief.md → Procedure → Assignment / Breadth for the tier`.

**Exploit or gap**

A task with a short valid solution can qualify through a successful but inefficient run. Redundant searches, small pagination choices, failure loops, and failure to use bulk operations increase observed calls without increasing necessary calls.

The fallback is worse: six unsuccessful, wandering runs can establish the call-count statistic without establishing any successful solution.

**Why the gates miss it**

A long successful trace proves that a long solution exists—not that a short solution does not. The documents prohibit obvious inflation choreography, but do not require minimization or shortcut testing against the actual tool capabilities.

**Mechanical fix**

Add a separate difficulty certificate containing:

- `shortest_verified_successful_trace`
- `admissible_bulk_operations`
- `necessary_evidence_dependencies`
- `conservative_call_lower_bound`
- `shortcut_test_results`

Do not classify a task as **500+ necessary calls** using an average or a single observed trace. Require a defensible lower-bound certificate under the actual catalog; otherwise label it only “observed long-horizon.”

---

## 2. The rubric acceptance policy explicitly tolerates correctness defects

**Location**
- `09_Rubric_Coverage_Plan.md → Severity table`.
- `09_Rubric_Coverage_Plan.md → Dimension table → Overall Rubric Quality`.
- Same table → `Repair gates (no score)` and `Predicted all-fail gate`.
- `09_Rubric_Coverage_Plan.md → Deliver`: “PASS or a scored NON-FAIL proceeds.”

**Exploit or gap**

Consider 20 authored criteria with one source-incorrect acceptance value. The check can correctly report that criterion as Major, yet:

- Major rate: 5%.
- Major + Moderate rate: 5%.
- Overall result: NON-FAIL, not FAIL.
- Final handoff: permitted.

The resulting rubric can reward a wrong result or reject a correct result while the authoring model faithfully reports the defect and follows the delivery policy.

The allowance of one predicted all-fail row creates a related problem: a task can proceed with a criterion already known to be impossible.

**Why the gates miss it**

Validity defects are treated as a percentage-quality budget. The apparent “repair gates” do not clearly override that budget; the table says their tally issue carries the score.

**Mechanical fix**

Separate acceptance into:

1. **Binary validity gates:** zero incorrect, unauthorized, unobservable, contradictory, missing-core-coverage, or impossible requirements.
2. **Quality scoring:** cosmetic and non-material issues may retain percentage tolerances.

Use zero, not one, as the allowed predicted-impossible count.

---

## 3. Final release does not clearly require an established executable solution

**Location**
- `08_Evidence_Ledger.md → Purpose`: OEs prove solvability.
- `08_Evidence_Ledger.md → Inputs → Tools`: catalog contains “names and parameters only.”
- `08_Evidence_Ledger.md → Check procedure → Predict and report`: distinguishes `SUPPORTED_BY_OE` from `NOT_ESTABLISHED`.
- `09_Rubric_Coverage_Plan.md → Prep inputs`: a PROVISIONAL plan may proceed when the OE check has no BLOCKING finding.
- `09_Rubric_Coverage_Plan.md → Deliver`: rubric acceptance proceeds to `/create-allfail`.

**Exploit or gap**

An OE check can contain OPEN/UNRESOLVED items without BLOCKING findings. That permits a provisional rubric plan. The supplied release sequence does not explicitly require promotion out of PROVISIONAL or require `Task solvability = SUPPORTED_BY_OE`.

Separately, a catalog-compatible sequence is not an executed sequence. Runtime validation, intermediate state changes, returned identifiers, serialization limits, and friction interactions can invalidate a statically plausible route.

**Why the gates miss it**

The described gates verify tables, pointers, catalog mappings, visibility, and reported judgments. No final conjunction requires both fully established OE support and a successful end-to-end replay.

Provisional planning is reasonable; allowing provisional status to survive release is the gap.

**Mechanical fix**

Add a terminal release gate requiring:

- No provisional artifacts.
- No unresolved load-bearing evidence.
- A supported OE route.
- At least one successful sandbox replay against the release bundle, using the assigned persona and configured friction.
- Verified final-state assertions from that replay.

The replay must occur outside the authoring workspace’s no-write/no-SQL boundary, through an authorized sandbox runner.

---

# High

## 4. The extreme breadth target is advisory, not an acceptance condition

**Location**
- `04_Prompt_Brief.md → Procedure → Breadth for the tier`: QC floor of two services; extreme target of ten.
- `04_Prompt_Brief.md → C12`: the ≥10/≥7 design target is Advisory.
- `04_Prompt_Brief.md → Assignment`: Normal and Long-Horizon tiers remain permitted.

**Exploit or gap**

An ordinary two-service task can satisfy the documented blocking complexity floor. Nothing in these supplied gates requires it to meet the stated harness objective of ten genuinely necessary services.

Even a declared ten-service design can count services that merely repeat information available elsewhere.

**Why the gates miss it**

The acceptance threshold and the harness objective are different. Service counts also lack a counterfactual definition of “carries weight.”

**Mechanical fix**

Make `profile` mandatory and enforce profile-specific minimums at release.

For each counted service, require a capability-aware necessity witness: removing that service must eliminate a required evidence distinction or authorized completion capability, considering equivalent information and alternate tools.

---

## 5. A cheap answer source can collapse the task without violating the incorporation check

**Location**
- `04_Prompt_Brief.md → C8`: instructions-not-answer restriction applies to incorporated sources.
- `04_Prompt_Brief.md → C9`: pre-solving in the prompt.
- `04_Prompt_Brief.md → C10`: discovery collapse is Advisory.
- `09_Rubric_Coverage_Plan.md → Prep procedure → Step 2`: acknowledges that the right answer may also sit in a shallow source.

**Exploit or gap**

The intended route may span many services, while an accessible summary, export, cached analysis, or alternate table already contains most of the answer.

If that shortcut is not the incorporated instruction source and is not named in the prompt, C8 and C9 do not prohibit it. A small remaining reconciliation can still satisfy the load-bearing-complexity floor.

**Why the gates miss it**

The playbooks validate the intended route, not the cheapest valid route through the whole accessible universe.

**Mechanical fix**

Add an adversarial shortcut audit over all persona-accessible surfaces:

- Search for answer-bearing summaries and distinctive result combinations.
- Test bulk joins and exports.
- Examine alternate-source coverage of the rubric’s acceptance values.
- Recompute the cheapest known route after every injection change.

A load-bearing process condition is not a substitute for removing an unintended precomputed answer.

---

## 6. Fixed spot checks plus a count permit mostly wrong bulk artifacts

**Location**
- `09_Rubric_Coverage_Plan.md → Prep procedure → Spot-check`.
- `09_Rubric_Coverage_Plan.md → Plan §D`.
- `09_Rubric_Coverage_Plan.md → Set-level checks → Spot checks / Mutation test`.

**Exploit or gap**

For a large repetitive output, an artifact can contain the correct total number of entries and correct values for the five sampled entries, while most unsampled entries are wrong.

The author can classify the repeated population as non-core; “core requirement” is not operationally defined. The mutation-test instruction is not reconciled with the explicit permission to leave most items ungraded.

**Why the gates miss it**

Cardinality does not establish membership, uniqueness, mappings, or per-item correctness. A fixed sample does not establish population correctness.

**Mechanical fix**

For machine-readable populations, require a complete population verifier:

- Exact key set or multiset.
- Duplicate detection.
- Required field comparisons.
- Tolerances where applicable.
- Verified joins and aggregate invariants.

Keep spot checks for explanation quality or diagnostics, not as the sole correctness test of a required population. Define “core” from prompt requirements, not author-selected labels.

---

## 7. Certificates are not bound to one immutable task bundle

**Location**
- `04_Prompt_Brief.md → Check procedure / Self-review`: prompt hash and within-run immutability.
- `04_Prompt_Brief.md → C22`: reuse a “matching” injection PASS.
- `08_Evidence_Ledger.md → Check Self-review`: counts, quoted spans, sign-off pointers.
- `09_Rubric_Coverage_Plan.md → Check Self-review`: criterion counts, quoted spans, issue tables.

**Exploit or gap**

An injection, reference file, friction configuration, rubric field, or universe record can change after an earlier stage passes. Reports may retain valid quoted spans and unchanged counts while their substantive conclusions are stale.

Live Confluence and Snowflake verification also allows different stages to reason over different data versions.

**Why the gates miss it**

Only the prompt has an explicit content hash, and that does not bind all dependent artifacts or the universe snapshot. Record pointers identify locations, not immutable versions.

**Mechanical fix**

Compute a full release-bundle digest over:

- Prompt, OEs, rubric JSON.
- SQL overlay and reference-file bytes.
- Friction configuration.
- Universe snapshot/version.
- Persona, ACL, catalog, clock, and rule versions.

Every gate certificate must include its input digest. Changing any dependency invalidates downstream certificates. Compare platform exports with the same bundle at submission.

---

## 8. Per-fact searchability can conceal oracle knowledge in the route

**Location**
- `04_Prompt_Brief.md → §5a Search-as-persona proof`.
- `08_Evidence_Ledger.md → Facts → Depends on`.
- `08_Evidence_Ledger.md → Completeness`: permits a value not previously produced when an event’s own pointer finds it uniquely.

**Exploit or gap**

An author who knows a hidden record can supply a unique query or direct locator for it and prove that the persona can retrieve it. The proof does not establish how the agent could obtain that locator from its initial information.

The first search can therefore contain author-only knowledge while still looking natural and returning a unique visible result.

**Why the gates miss it**

Visibility, uniqueness, and discoverability are different properties. The search proof is conducted by the person who already knows the answer. Dependency edges are largely self-declared.

**Mechanical fix**

Require locator provenance:

- Every opaque identifier and high-information exact locator must come from the prompt or an earlier tool result.
- Each evidence dependency must be topologically executable.
- Free-form hypotheses may introduce ordinary search concepts, but cannot silently introduce hidden IDs.
- Run a cold-start discovery replay with the agent given no ledger, manifest, or answer-bearing metadata.

---

## 9. Failure diversity is vulnerable to graph-labeling and packaging tricks

**Location**
- `09_Rubric_Coverage_Plan.md → Hard gate 12`.
- `09_Rubric_Coverage_Plan.md → A2 → Decided by`.
- `09_Rubric_Coverage_Plan.md → Summary → largest single-discovery share`.
- `09_Rubric_Coverage_Plan.md → Set-level checks`: sharing a likely root cause is not necessarily a cascade group.

**Exploit or gap**

Several declared chains can depend on the same decisive authority or be resolved by one tool result containing many fact rows. Dividing that result into separate F-IDs and chain IDs can keep each declared discovery below 50% while one real observation settles nearly everything.

Conversely, separate rubric rows do not establish that failing runs will exhibit different failure patterns.

**Why the gates miss it**

The metric operates on declared chains and discoveries without defining the unit of discovery or requiring transitive dependency analysis. Static row separation is used as a proxy for empirical diversity.

**Mechanical fix**

Construct a dependency graph from actual observations and transformations. Compute weight impact over transitive prerequisite cuts, including shared authorities and single tool responses.

Then perform controlled ablations: remove or corrupt each independent evidence source and measure which rubric results change. Require demonstrated separation, not just different labels.

---

## 10. “Exactly one final state” conflicts with expressly permitted alternative outcomes

**Location**
- `04_Prompt_Brief.md → Hard gate 5`.
- `04_Prompt_Brief.md → C7`: unpinned channel, time, or form can be Minor.
- `04_Prompt_Brief.md → UGT procedure, step 3`: delegated choices and objectively bounded open-ended work pass.
- `09_Rubric_Coverage_Plan.md → Hard gate 10`.
- `09_Rubric_Coverage_Plan.md → Atomicity / Specificity`: closed sets of accepted channels or alternatives can be valid.

**Exploit or gap**

The same task can be rejected for multiple final states under the hard gates and accepted under the delegated-choice or valid-alternative provisions.

Different calendar times or delivery systems are materially different states under the literal hard-gate definition, even when both are acceptable to the requester.

**Why the gates miss it**

The documents lack a common definition of final-state equivalence. Evaluators can silently switch between exact state equality and satisfaction of acceptance boundaries.

**Mechanical fix**

Introduce a canonical outcome specification with:

- Fixed fields.
- Explicitly delegated fields.
- Allowed equivalence classes.
- Material versus representational differences.

Either require one canonical state or explicitly define UGT over one acceptance class. Apply that definition consistently across prompt, OE, and rubric checks.

---

## 11. Bounded searches can incorrectly clear absence and act-versus-defer decisions

**Location**
- `04_Prompt_Brief.md → Absence rule`.
- `08_Evidence_Ledger.md → Prep procedure → Writes`: bounded defer search in persona channels/DMs and mailbox using listed phrases.
- `08_Evidence_Ledger.md → Accuracy → Act-vs-defer`.

**Exploit or gap**

An authoritative hold decision can exist in Linear, Confluence, a document, or a differently worded message. The prescribed search can return no result despite an accessible decision that makes the planned write wrong.

Likewise, a positive control demonstrates that a search works, not that it searched the complete relevant population.

**Why the gates miss it**

Search scope is documented, but completeness of that scope is not established. The OE act-versus-defer check specifically relies on what the ledger’s bounded search recorded.

**Mechanical fix**

Require an authority-aware decision search across every service governing the affected entity. Store:

- Candidate record population.
- Pagination completion.
- Authority links.
- Version resolution.
- Search coverage limitations.

A negative result is conclusive only over a complete relevant population. Otherwise the decision remains UNRESOLVED.

---

## 12. The ban on negative criteria leaves some real prohibitions ungradeable

**Location**
- `09_Rubric_Coverage_Plan.md → Hard gate 7`: prohibition-only/absence-only acceptance always fails; exclusions become preserved states or scope boundaries.
- `09_Rubric_Coverage_Plan.md → Agent-centric and negative`.
- `09_Rubric_Coverage_Plan.md → Process candidates`: focused on ordering and rare source verification.

**Exploit or gap**

Some prohibited behavior cannot be detected from the final state. A transient unauthorized mutation followed by restoration can leave the required preserved state intact. A forbidden communication may have occurred even if a later snapshot no longer contains it.

Recasting the prohibition as a positive state does not make the two properties equivalent.

**Why the gates miss it**

The policy treats grammatical positivity as a validity requirement and emphasizes final-state evidence. It lacks an explicit class for authorized behavioral invariants over execution.

**Mechanical fix**

Permit prompt-authorized constraint predicates in a typed schema. Evaluate side-effect constraints against an append-only execution audit, using fields such as:

- `authorized_effect_scope`
- `protected_state`
- `execution_interval`
- `audit_evidence`

Judge semantic authorization and observability, not whether the wording contains a negation.

---

# Medium

## 13. Fact deduplication conflicts with coverage on every required artifact

**Location**
- `09_Rubric_Coverage_Plan.md → Hard gate 6`: each fact graded once.
- `09_Rubric_Coverage_Plan.md → Prep procedure → Duplicate risk`: select one row for a value appearing in multiple deliverables.
- `09_Rubric_Coverage_Plan.md → Coverage`: record/post coverage does not cover the final reply.
- `09_Rubric_Coverage_Plan.md → Set-level checks`: the same fact in two prompt-specified deliverables is not duplicate grading.

**Exploit or gap**

Following prep literally can leave a required destination unchecked. Following check mode literally can require the very repeated grading prep prohibits.

An agent can get the fact right in one artifact and omit or corrupt it in another.

**Why the gates miss it**

“Fact” is used both as an informational value and as an obligation to communicate that value somewhere.

**Mechanical fix**

Key coverage by an obligation tuple:

`(requirement, artifact, recipient, phase, fact)`

Deduplicate identical obligations—not every occurrence of the same F-ID.

---

## 14. Atomicity can be changed merely by repackaging tool output

**Location**
- `09_Rubric_Coverage_Plan.md → Hard gate 6`: exception for “components of one evidenced tool output.”
- `09_Rubric_Coverage_Plan.md → Per-row lint → Atomicity`: exceptions apply first.

**Exploit or gap**

Independent results can be placed in one query result, document, or tool response and then treated as components of one evidenced output. The same facts would be non-atomic if returned separately.

This permits coarse all-or-nothing grading driven by response packaging rather than independent correctness.

**Why the gates miss it**

A transport-level unit is accepted as a semantic unit. A single Snowflake result can contain arbitrarily many independent claims.

**Mechanical fix**

Make atomicity invariant under tool-output packaging. Permit the exception only for semantically coupled attributes of one entity, metric, comparison, or causal claim—not merely values returned by one call.

---

## 15. Temporal rules confuse future scheduling with future occurrence

**Location**
- `04_Prompt_Brief.md → Hard gate 4`: later dates may appear as unhappened deadlines.
- `08_Evidence_Ledger.md → Hard gate 4`: a record dated on or after the clock is a universe defect.
- `08_Evidence_Ledger.md → Accuracy → Expected data`: nothing on or after the clock expected as done.
- `09_Rubric_Coverage_Plan.md → Clock`.

**Exploit or gap**

A record created before the clock can legitimately contain a future deadline, scheduled event, or future effective date. The ledger’s blanket “record dated” rule can reject that valid record.

Alternatively, an author can characterize a future timestamp as scheduling and miss that it actually represents creation or completion.

**Why the gates miss it**

Timestamp fields are not typed by meaning. This is not a problem with the fixed task clock itself; it is a problem with applying one predicate to different temporal semantics.

**Mechanical fix**

Require typed temporal fields:

- `recorded_at`
- `occurred_at`
- `effective_at`
- `scheduled_for`
- `deadline`

Apply clock rules by field type, including version visibility and effective-state resolution.

---

## 16. Human-only authorship is not established by the lexical scans

**Location**
- All three files → `The authorship boundary`.
- `04_Prompt_Brief.md → Self-review 4`.
- `08_Evidence_Ledger.md → Self-review → No event text`.
- `09_Rubric_Coverage_Plan.md → Self-review → No criterion text`.

**Exploit or gap**

Noun-phrase tables can encode virtually all semantic content needed for the final human artifact while avoiding prohibited sentence forms. Verbatim quotation exceptions provide another channel for transcribable material.

Separately, an artifact generated elsewhere can pass every local lexical check. The checks establish surface form, not authorship provenance.

**Why the gates miss it**

“No first-person sentence” and “no cell beginning with Agent” are not reliable proxies for “not drafted by a model.”

**Mechanical fix**

Treat authorship as a provenance control:

- Separate model and human write channels.
- Record authenticated editor provenance and artifact hashes.
- Require equality between reviewed local artifacts and platform exports.
- Track whether quoted source material was newly authored in the same task-authoring run.
- Audit prep outputs for semantic precomposition, not only lexical forms.

Be explicit that this proves controlled-channel provenance, not the impossibility of outside assistance.

---

## 17. Mandatory templates conflict with mandatory output scans

**Location**
- `04_Prompt_Brief.md → Brief template`: human-directed instruction in the required header.
- `04_Prompt_Brief.md → Check report template`: remarks about typos, capitalization, and AI-likeness.
- `04_Prompt_Brief.md → Self-review 4 / stage-gate description`: forbids second-person sentences and those remarks.
- `08_Evidence_Ledger.md → Ledger §D`: required `Alternative path` column.
- `08_Evidence_Ledger.md → Self-review → No event text`: forbids “path.”
- `04_Prompt_Brief.md → Must-not-appear list / Self-review 5`: root cause belongs in the list, but may appear only in §5.

**Exploit or gap**

A literal scanner rejects correctly filled templates. A scanner with broad, undocumented exceptions becomes easy to evade through headers, quotes, or table cells.

Authors must guess whether the template or the scan governs.

**Why the gates miss it**

The rules mix semantic prohibitions with unrestricted lexical bans and do not define machine-readable exemption scopes.

**Mechanical fix**

Publish a structured output schema with:

- Fixed boilerplate explicitly exempted.
- Exact boundaries for verified quotations.
- Separate fields for prohibited-content identifiers versus their values.
- Context-aware scans restricted to authored content.

Add a fixture test requiring every official template, minimally completed, to pass its own validator.

---

## Highest-priority repairs

1. **Make validity binary:** correctness and feasibility defects cannot be spent from a percentage budget.
2. **Add one immutable release bundle and terminal release gate:** no stale certificates, provisional evidence, or unresolved solvability.
3. **Certify necessary difficulty:** distinguish long observed traces from unavoidable work and test bulk/summary shortcuts.
4. **Strengthen semantic coverage:** complete population verification, obligation-based deduplication, and execution-audit support for real prohibitions.

These changes address the largest gap: the current documents can produce a thoroughly checked authoring packet without establishing that the released task is hard, executable, and graded completely.

