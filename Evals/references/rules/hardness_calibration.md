> **Historical reference — retired for current scoring.** This document records
> the former Haiku screen and its rules. Its instructions and score interpretations
> are not active. Use [Eval 1A](../../1A_Hardness_Eval.md), `model-aware-v3`, for
> observed Opus assessment or [Haiku-to-Opus prediction](../../1B_Haiku_Prediction_Eval.md).
> This historical text is not the active prediction procedure; do not load it to score a task.

# Hardness calibration record

Paired outcomes from hardness screens already issued in this workspace, kept so
that [Eval 1A](../../1A_Hardness_Eval.md)'s transfer classes can be reviewed
against what later strong-model runs actually did.

## Purpose and limits

This file exists to review the rules, not to score a task. It is **not** a
predictor, a requirement source, a calibrated transfer rate or an input to any
live screen. Reading it must not change the score of the task under review.
Eval 1A's prohibitions still hold in full: do not request Opus runs, grades,
rubrics or a golden answer for the task being screened, and do not state a
predicted percentage or failure probability for it.

Entries are added only after a gate decision was already issued and strong-model
runs happened to become available for other reasons. Absence of an entry means
nothing about a task. The sample is small, unbalanced and opportunistic.

Use it in two supported ways:

- as worked examples of `CAPABILITY_FLOOR` versus `JUDGMENT_AMBIGUITY`;
- as evidence when proposing a change to these rules.

## Entry: `6aa8272b1b7a2df0fc0fea8d` (store-cut RC flag gate)

**Screen as issued.** `observed-run-v5`, Hard / 4 / NON-FAIL / PROCEED /
`QUALIFYING_FAILURE_PATTERN`, on one `claude-haiku-4-5` run (33 tool calls, 34
turns). Four chains were credited as qualifying.

**Observed later.** Six `claude-opus-4-8` runs on the same prompt and injection,
graded against the task's own golden and the 40 criteria of
`09_Rubrics.json` (total weight 110) in a separate grading pass: four runs at
100% and two at 86.4% (95 of 110, losing the same 15-weight chain), averaging
**95.5%** against the below-75% target. The screen was a false positive.

**Per-chain transfer.**

| Chain | Haiku | Opus, 6 runs | Would-be `transfer_class` |
|---|---|---|---|
| `RateUsPopup` stays PROMOTE because the kill request came from engineering, not a founder | `KILL`, never checked the roster for the requester's seniority | 6/6 `PROMOTE` | `CAPABILITY_FLOOR` |
| `InterstitialsEnabled` HOLD on a founder's do-not-flip message | `PROMOTE`, the message was in a channel the run had already read | 6/6 `HOLD` | `CAPABILITY_FLOOR` |
| `MagicalWingsVariant` HOLD because a Regression ticket names the surface | `PROMOTE`, never searched the tracker for Regression state | 6/6 `HOLD` | `CAPABILITY_FLOOR` |
| January figures copied into the memo | omitted, saw the filename and never opened the document | 6/6 copied them exactly | `CAPABILITY_FLOOR` |
| `CollectAndWinEnabled` HOLD because a Regression ticket names `win&collect` | `PROMOTE`, same unissued search | 4/6 `HOLD`, 2/6 `PROMOTE` | `JUDGMENT_AMBIGUITY` |

**What the case shows.** Every credited chain matched a pattern ID by shape and
four of them had no observed strong-model failure at all. In each of those four,
the decisive step was issuing a search, opening a named file, reading a record
already returned, or applying a clause the run already held. Retrieval breadth
and careful reading of returned records are the widest capability gap between
the screening model and Opus, so those chains described the run rather than the
task.

The one chain that did transfer was not one the screen examined. Haiku failed it
by never searching the tracker, the same capability-floor mechanism as the
others. The two Opus runs that failed it retrieved the ticket and then decided
the surface alias `win&collect` did not bind `CollectAndWinEnabled`. That scope
boundary is what survives complete retrieval, and it is the only part of this
task with observed strong-model disagreement. A screen aimed at it would have to
show the alias question itself, not the missing search.

The task shape reinforces this. The governing clauses, their order and their
tie-breaks are enumerated in a single ticket comment the prompt points at, over
a cohort of twelve named keys, which is `enumerated_single_source`: a compliance
checklist that a strong model executes reliably at any length.

**Rule changes made in response.** `observed-run-v6` added the thorough-reader
counterfactual as promotion check 4 with the required `transfer_class` field,
restricted scores of 3 to 5 to `JUDGMENT_AMBIGUITY` chains, retied 3 versus 4 to
independent root causes rather than chain count, and added the
`decision_rule_source` task-shape cap. Under v6 this screen scores Easy / 2 /
FAIL / HOLD / `INSUFFICIENT_DIFFICULTY`, with the alias chain recorded as the
only `JUDGMENT_AMBIGUITY` candidate and too narrow to carry the gate alone.

## Entry: `6aa8272b1b7a2df0fc0fea91` (backend and live-ops PR residue register)

**Screen as issued.** `observed-run-v5`, Hard / 3 / NON-FAIL / PROCEED /
`QUALIFYING_FAILURE_PATTERN`, on one `claude-haiku-4-5` run (19 tool calls, 20
turns, 82 seconds). One chain was credited: Arthur's `ignore leonard on the
cohort. all PRs. no drafts. main only.` was returned in the thread the run
read, and the run inventoried two open PRs and attributed Leonard's open-only
scope to Arthur.

**Re-screened under `observed-run-v6`.** Easy / 2 / FAIL / HOLD /
`INSUFFICIENT_DIFFICULTY`. Every chain screened `CAPABILITY_FLOOR`, because the
`#engineering` thread states each governing rule verbatim, including the
supersessions (`ignore leonard on the cohort`, `token is out of HOT_PATH. add
nakama dynamodb dynamo and streak`). The `decision_rule_source` cap reached the
same 2 independently.

**Observed later.** Six `claude-opus-4-8` runs on the same prompt and
injection, 306 to 949 tool calls each, 17 to 38 minutes. Graded by the
**baseline verifier** (weighted, 30 criteria): average weighted rubric pass
rate **70.2%** against the below-75% target, pass@1 **0%** (0 of 6 all-pass),
6 of 6 rollouts failing, 5 distinct failure signatures, largest signature share
33.3%. Every hardness requirement passed. The v6 re-screen was a false
negative on difficulty.

**Grading provenance and an unresolved mismatch.** The verifier scored 30
criteria (`criterion-0` through `criterion-29`). The rubric saved at
`Created_Tasks/6aa8272b1b7a2df0fc0fea91/09_Rubrics.json` holds 40 criteria
(total weight 124), and no 30-criterion rubric exists in this workspace. An
independent pass over those 40 criteria put the same six runs at 75.1% average
weighted (range 67.7% to 87.1%). The two figures agree on the shape of the
result and disagree on the margin. The verifier figure governs here; the
criterion-count mismatch is a delivery question, not a rules question.

**Per-chain transfer.**

| Chain | Haiku | Opus, 6 runs | `transfer_class` |
|---|---|---|---|
| Cohort authority: Arthur supersedes Leonard's open-only scope | applied open-only, called it Arthur's | 6/6 applied the full non-draft `main` cohort and wrote 133 rows | `CAPABILITY_FLOOR` |
| `HOT_PATH` count over the cohort | never reached, 2 rows written | **0/6**: 42, 44, 44, 44, 45, 46 against 47 | `SCALE_COMPLETENESS` |
| `NONE` count over the cohort | never reached | **0/6**: 77, 79, 80, 81, 81, 82 against 78 | `SCALE_COMPLETENESS` |
| Those two totals restated on the brief | never reached | 0/6 | same chain, delivery of it |
| Thread reply and `ENG-2440` comment | both skipped | 3/6 skipped the thread reply | execution, cannot qualify |

**What the case shows.** The task's difficulty is not an unsettled question.
Every rule is stated, so under v6 every chain is `CAPABILITY_FLOOR` and the
gate must score it 2. The difficulty is that the golden requires per-record
evidence on 133 pull requests across four surfaces, roughly 540 retrievals, and
then exact totals derived by applying a twelve-word whole-word predicate with
stated exclusions to every title, body and commit message. No bulk view holds
that answer. All six strong-model runs performed the sweep and all six still
got the two derived counts wrong, which is a 16-of-124 weight loss that no run
avoided.

Two structural limits in v6 produced the false negative:

- Check 4 asks what an agent that retrieves every discoverable source and
  reads every returned record would still get wrong. Where the cohort sweep
  *is* the task, that counterfactual assumes away the thing being tested, so no
  cohort-audit task can ever clear it.
- Check 2 requires the failure to be observed in the screening run. The
  screening model abandoned the inventory after 19 calls and never reached the
  predicate arithmetic, so a weak-model screen cannot exhibit scale difficulty
  at all. Weak models quit before the hard part.

Contrast with `6aa8272b1b7a2df0fc0fea8d`, where the cohort was twelve named
keys, no per-record surface sweep was required, and 6 of 6 strong-model runs
averaged 95.5%. Volume alone did not make fea91 hard; per-record evidence that
no bulk call contains, plus exact derived totals, did. That distinction is the
one the rules now turn on.

**Rule changes made in response.** `observed-run-v7` added the
`SCALE_COMPLETENESS` transfer class and the long-horizon cohort-sweep route,
which can carry the gate only on the task-design conditions in Eval 1A and only
with paired strong-model evidence recorded, or else as an explicitly provisional
advance. The `decision_rule_source` cap now yields to a credited
`SCALE_COMPLETENESS` chain, while the bar against volume, clause count and
service count as difficulty is unchanged.

## Entry: art-canon handoff control (task id unassigned)

**Screen as issued.** `observed-run-v7`, Easy / 2 / FAIL / HOLD /
`INSUFFICIENT_DIFFICULTY`, on one `claude-haiku-4-5` run (38 tool calls, session
`51748fb7`). No chain was credited. The run made zero Trello calls and never
retrieved the governing control card, so thirteen of fourteen requirements were
`UNASSESSED`. The cohort-sweep route was considered and rejected on conditions 1
and 2, and the `enumerated_single_source` cap reached the same 2 independently.

**Observed later.** Average weighted rubric pass rate **44.1%** against the
below-75% target, reported by the task author. Run count, model string, rubric
and grading pass are **not recorded here**: they were not supplied, and this
entry should be completed when they are. The screen was a false negative on
difficulty, by the widest margin in this record.

**Root cause: the cohort was measured against the store, not the tool surface.**
The screen's three decisive figures came from grouping the universe archive's
Slack message files by `thread_ts`. Those files interleave thread replies with
their parents — 1,541 replies against 2,262 parents in `god-gameart` alone — so
the resulting view belongs to no available call. The catalog's
`slack_read_channel` returns thread parents only, confirmed in the run's own
call 20: 50 messages returned, zero of them replies.

| Screen's claim | Measured on the tool surface |
|---|---|
| 195 of 260 scoped roots are NO_REPLY from the bulk listing, so three quarters of the cohort needs no retrieval | 50 of the 260 (19%) carry no file on the root at all and qualify on a file in a reply, invisible to channel history. `reply_count` cannot settle NO_REPLY either, because the control excludes seven reply classes and a count does not distinguish them |
| About 65 core record-level calls, an order of magnitude below the 500–1,000 band | 29,333 roots at or before the cutoff need roughly 587 paginated reads at the observed ~50-message ceiling, plus 4,172 roots carrying replies that must each be opened to scope and to classify: a floor near 4,769 |
| File metadata arrives inline, so the dual-ownership retention predicate resolves from the bulk view | True for root-carried files only, which is the 81% the listing can see at all |
| The top-three channel set is fixed by bulk-visible counts, so the derivation is not load-bearing | Arithmetically correct and beside the point. The five status totals, ten channel open counts, per-root human reply counts and the exact 15 + 3 rows are all per-record, and one misread root changes required cells |

The 100-message channel read overflowed at 71,224 characters and spilled to a
file, which the screen discounted as pagination volume. On this task the
enumeration is necessary dependent retrieval, not one useful query split up.

**Unresolved measurement.** `slack_list_files` takes `user`, `channel` and a
cursor, so a cheaper cohort route may exist if its file objects resolve a share
back to the thread root. No run in evidence called it. Even on that path the 260
scoped roots still need thread opens for the substantive-reply filter and the
human reply counts, so condition 2 does not turn on it.

**What the case shows.** The route introduced after `...fea91` was sound; its
application was not. Both recorded errors before this one were about *which
chain* transfers. This one is about *what the numbers describe*, and it produced
a 2 on a task the rules would have scored 4 had the same conditions been checked
against the calls instead of the archive. Note also that the screen stamped a
difficulty label on a run that never opened the governing source — coverage of
the run's conduct was complete, coverage of the task was nil.

**Rule changes made in response.** Eval 1A now requires conditions 1 to 3 to be
measured against the tool surface, with the store explicitly excluded; condition
2 now defines bulk-call cover as returning every predicate-read field for every
record and rejects summary pointers as cover for filtered content; the
task-shape screen states that enumeration makes a predicate checkable but not a
cohort; and a run that stopped before reaching the governing source now yields
`INSUFFICIENT_EVIDENCE` rather than any difficulty label, with measured
strong-model averages outranking both screens.

**Open rules question, not yet changed.** A `SCALE_COMPLETENESS` chain cannot
reach 5 under v7, because 5 requires `JUDGMENT_AMBIGUITY`, and the 3–4 band's
"substantial core work remains correct" sits awkwardly against 44.1%. Flagged
for the next revision rather than decided here.

## Adding an entry

Record the task ID, the screen as issued (version, difficulty, score, gate,
credited chains), the later observed runs with their model string and how they
were graded, per-chain transfer, and the retrospective `transfer_class` for each
credited chain. State the grading provenance and keep the run count visible.
Do not add an entry for a task whose screen has not been issued yet, and do not
turn any figure here into a threshold, weight or forecast.
