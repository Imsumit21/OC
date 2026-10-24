> **Historical reference — retired for current scoring.** This document records
> the former Haiku screen and its rules. Its instructions and score interpretations
> are not active. Use [Eval 1A](../../1A_Hardness_Eval.md), `model-aware-v3`, for
> observed Opus assessment or [Haiku-to-Opus prediction](../../1B_Haiku_Prediction_Eval.md).
> This historical text is not the active prediction procedure; do not load it to score a task.

# Opus failure patterns for the Haiku hardness gate

Use this reference with [Eval 1A](../../1A_Hardness_Eval.md) to compare observed
Haiku failures with the author's reported Opus examples. It is empirical
guidance, not a replacement for QC policy, a rubric, or a calibrated predictor.
The official average weighted rubric pass-rate target is **below 75%**.
Examples near 80% are comparison data; 80% is not a second target.

## Provenance and limits

Adapted from the user-supplied note **“How baseline runs miss — and how to land
under 80%”**, referencing `Task_Examples/`, unhinted Opus BASELINE verifiers,
and six completed rollouts per example. Original attachment SHA-256:
`9a37b14836f3e309e7f0e4b3fbe63f5cb6bdbc97e141ec3fa4d49a71f5788029`.
The note was supplied in this workspace's authoring discussion; the original
attachment and example folders are not runtime prerequisites for `/hardness`.

The values below are reported by that note, not independently recomputed from
raw Opus rollouts here. No paired Haiku/Opus results or validated transfer rate
were supplied with it. These selected examples do not establish universal
behavior, causation, a required number of failed facts, or a predicted score.
Paired outcomes observed later in this workspace are kept separately in
[hardness calibration](hardness_calibration.md), which is a rules-review record
and still not a transfer rate.

| Reported example | Average weighted pass rate | What the note reports |
|---|---|---|
| Marcus Bennett | 47% | Completed artifacts but repeatedly omitted decisive facts distributed across messages. |
| Martin Walsh | 52% | Missed corrections, alternative-eliminating evidence and an existing ticket despite substantial investigation. |
| Julia Lawson | 77% | Count/unit errors; below 80% but above the official cutoff. |
| Claire Morgan | 79.5% | Five strong runs plus one refusal; a low aggregate driven by collapse provides weak task-hardness evidence. |
| Brian Foster | 80.5% | One bundled-PR discovery separated strong and weak runs; downstream count errors shared that cause. |

## Pattern shape is not transfer evidence

Each pattern below describes the **shape of the evidence** in a failure: a fact
that eliminates an alternative, a later correction, a decisive fact absent from
a deliverable, a record that should have been reused. Shape does not identify
the mechanism that makes a capable agent fail. Every pattern here can equally
describe a weak run that simply did not look: a search never issued, a file
never opened, a returned record never read, or a rule stated verbatim in a
source the run already held. Those are the capability floor of the screening
model, and a stronger model routinely clears them.

So a match is a candidate signal and never a qualifying one. Eval 1A's
promotion check 4 decides transfer by asking what the chain still turns on
after complete retrieval and careful reading, and records the answer in
`transfer_class`. Only `JUDGMENT_AMBIGUITY` chains can qualify. Do not restate
a retrieval or reading miss in reconciliation or synthesis language to reach a
pattern name; `hardness_calibration.md` records a screen where four chains
matched patterns by shape and none of them transferred.

The pattern IDs remain useful for exactly what they are: naming the evidence
structure, connecting a chain to reported comparison cases, and making the
differences from those cases explicit.

The converse also holds: absence of a pattern is not absence of difficulty.
These patterns all describe a decision going wrong on evidence the run held,
so none of them names the failure mode of a large cohort audit, where the
rules are plain and the difficulty is holding a stated predicate exactly
across every record. `hardness_calibration.md` records a task where six
strong-model runs each swept 133 pull requests and all six still missed the
same two derived totals, with no pattern here matching. Eval 1A's cohort-sweep
route covers that shape; do not force it into a pattern ID, and do not read a
clean pattern screen as evidence that such a task is easy.

## Patterns to compare

**Eliminating evidence (`ELIMINATING_EVIDENCE`).** Required facts rule out the
obvious alternative, but the output retains it or fails to justify excluding
it. Examples: availability in all 177 countries helps eliminate store
geo-blocking; publisher-verified settings address campaign misconfiguration;
three Slack notes rule out an instrumentation fault. Establish the actual
logical role of the fact in the current task, not just its presence in a source.

**Later corrections (`LATER_CORRECTION`).** Evidence changes over time and the
run carries an earlier claim into its decision. The Martin notes describe a
withdrawn claim that 1.25× battle speed had shipped. Other source changes may
alter scope, status or counting units. A later message is not automatically
authoritative: check what it corrects and why it governs the requested decision.
An isolated arithmetic error after applying the correct unit is weaker evidence.

**Decisive facts lost in synthesis (`SYNTHESIS_OMISSION`).** The model creates
the requested report, sheet or message but omits evidence needed to substantiate
the requested conclusion. The reported Marcus/Martin failures concerned facts
such as the affected Android version, intended rewarded-video configuration,
build 1.0.88 closing the level cap, and the retracted speed claim. An exact
detail qualifies only when the current prompt or incorporated assignment needs
it; a valid equivalent explanation need not repeat a particular phrase or number.

**Required reuse or exclusions (`REUSE_OR_EXCLUSION`).** A rule must be connected
to a discoverable record or event. The Martin note reports opening DES-315
instead of reusing DES-313. The Marcus note describes missing a second item
covered by the publisher-opened-and-closed exclusion. Show identity/scope,
applicable authority and a normal discovery path. An inaccessible record or a
search-tool fault is a confound, not proof of hardness. A returned empty search
alone does not establish that the task offered no discoverable route.

These mechanisms can overlap. Missing one retraction and repeating the wrong
claim in three artifacts is one cause. Several independent consequential
failures are stronger screening evidence than many consequences of one mistake.
Other substantive reasoning mechanisms can be evaluated under Eval 1A, with
the absence of a matching empirical example stated explicitly.

## Weaker signals and use boundaries

- Isolated counting, copy, literal-predicate, destination or formatting errors
  do not qualify on their own. A late source change may qualify when the
  material failure is in finding or reconciling that evidence, not just arithmetic.
- A refusal, missing artifact or tool failure alone does not demonstrate the
  intended task difficulty. Artifact completion alone does not establish success.
- One binary discovery that fixes nearly everything is weaker support than
  several independent chains. A large set of repeated output failures does
  not change that causal structure.
- The note's reported always-failing weights describe its Opus batches. Do not
  label a failure in one Haiku run “always-failing,” import those weights into
  a new task, infer weighted score loss, or require a quota of facts or timestamps.
- Derive requirements before grading. Do not hide arbitrary trivia or tune
  later rubrics to the misses. Use the complete task scope, including correct
  work and valid alternative answers, when deciding whether the gate can clear.

A matched pattern is a candidate signal. Apply Eval 1A's source, consequence,
observed-failure, transfer and task-level checks before assigning 3–5. The gate
remains mandatory: scores 1–2 or insufficient evidence HOLD Opus; supported
scores 3–5 permit progression once other prerequisites are met. A run that
fails many chains for one retrieval reason supports a low score, not a high
one. This review launches no models and does not certify later baseline QC
metrics.
