## Major findings

1. **Library observations bypass the one-trial-per-run/family rule.**  
   **File:** `tools/hardness_ledger.py:263–281`  
   **Hunk:** `@@ -221,31 +252,51 @@`

   Verdicts are collapsed by `(task, revision, run, family)`, but observations are simply added as `landed + not_landed` trials. Two library rules in the same family describing the same six runs therefore contribute twelve trials. If one rule landed in every run and the other leaked, this also produces mixed successes/failures instead of six family-level landings. Applying the task design effect afterward does not repair either error.

   **Fix:** Import overlapping library evidence with run identities and the portfolio rule’s family, then apply the same family/run collapse. Accept aggregate observations only when they represent already-collapsed, non-overlapping family trials; otherwise reject or exclude them explicitly. Plant overlapping same-family library records and verify both the trial count and family-level OR outcome.

2. **The go tally can count an explicitly identified control error through a complexity channel.**  
   **File:** `tools/node_verdicts.py:332–351`  
   **Hunk:** `@@ -197,6 +212,155 @@`

   Channel eligibility considers only `FAILED`, model ownership and preregistration. Controls are consulted afterward, solely for reporting and removing duplicate slip labels. If a failed channel reproduces the same field error already recorded as an `OVER-APPLIED` control trial, that error still contributes an independent loss channel. It can appear simultaneously under `channels` and `not_counted.control_over_applications`.

   **Fix:** Remove control-explained field evidence before constructing eligible mechanism/channel evidence. Count a channel only if eligible evidence remains, preserving legitimate scope landings beside control records. Plant an expected-model run where the sole channel failure is the same error as an over-applied control; its tally must be zero.

3. **Unknown deciding models are discarded before the “every decision belongs to the expected model” check.**  
   **File:** `tools/node_verdicts.py:322, 330–339, 530–531`  
   **Hunks:** `@@ -197,6 +212,155 @@`, `@@ -337,13 +516,21 @@`

   Both mechanism and channel model sets omit falsy `deciding_model` values. Consequently, evidence with one expected-model decision and one unidentified decision becomes a model set containing only the expected model and passes `own()`. That does not establish that all counted decisions were the expected model’s own decisions.

   **Fix:** Preserve unknown-decision status and require a known, matching model for every counted landing/member. Add mechanism and channel cases containing one expected-model decision and one unknown decision; neither aggregate should qualify as entirely expected-model evidence.

4. **Decision attribution uses the last write anywhere in the register, not the write that supplied the key’s final value.**  
   **File:** `tools/node_verdicts.py:227–235`  
   **Hunk:** `@@ -197,6 +212,155 @@`

   `before` is bounded by `max(table_events)` before the key-specific writes are considered. With an appended or incrementally updated register, key A can be written at event 10, receive another naming brief at event 15, and remain unchanged while key B is written at event 20. The function then attributes A’s existing value to the event-15 brief—even though that brief occurred after A’s value was written. This can change model ownership and the go tally.

   **Fix:** Determine the write that actually supplied the final value for that key first, and bound its candidate briefs by that event. Plant the earlier-key-write/later-unrelated-append case with different brief models.

5. **Missing columns can turn a class cascade or partial match into an operator’s own change.**  
   **File:** `tools/node_verdicts.py:266–269, 313–317`  
   **Hunk:** `@@ -197,6 +212,155 @@`

   Both control and channel matching calculate `changed` only over fields present in the submitted row. If an operator changes a non-class field and the class, but the non-class column is absent, `own` falls back to the class. A matching class is then accepted despite the operator having changed another field. Similarly, omitting one of several changed fields allows an incomplete reproduction to pass the all-fields check.

   **Fix:** Calculate the operator’s delta from truth independently of submitted-field availability. Only use class-only matching when the operator changes no relevant non-class field at all; require the necessary fields to be observed before declaring reproduction. Plant missing-column cases, not just present-but-wrong values.

6. **Channel reporting does not implement surface-only channels or held-channel provenance completely.**  
   **File:** `tools/node_verdicts.py:291–306, 318–322`  
   **Hunk:** `@@ -197,6 +212,155 @@`

   There are three observable gaps:

   - A slots-only channel can be `FAILED`, but always has `deciding_models: []` and no deciding event. `go_rule()` therefore excludes every such failure, including an expected-model-owned failure.
   - A channel whose degrade changes only surface data returns `UNOBSERVED` without consulting supplied slot grades. The E2E output’s unparameterized `scale:groups` is not a completed failed/held channel assessment.
   - Register-channel provenance exists only for failed members. A `HELD` channel has no held-member decisions or deciding events/models, contrary to the reporting decision.

   **Fix:** Record observed channel trials and their provenance for both held and failed outcomes. Evaluate declared surface slots when the degrade has no register-observable delta, and identify the surface decision’s event/model. Add expected-model and off-model surface failures, a held channel, and a surface-only degrade case.

7. **Unobserved channel members are recorded as held trials.**  
   **File:** `tools/node_verdicts.py:299–322, 769–777`  
   **Hunks:** `@@ -197,6 +212,155 @@`, `@@ -486,14 +740,45 @@`

   Register-channel members absent from `rows` are skipped when finding failures, but remain in `members = len(moved)`. A run writing none of those members therefore produces `HELD` with a positive trial denominator, and the ledger proposal records those missing observations as non-failures. Slots-only channels likewise treat missing/`None` grades as held. This silently supplies favorable channel evidence to forecasting.

   **Fix:** Track observed, failed, held and unobserved trials separately. Do not put unobserved members into the held denominator; skip wholly unobserved channel proposals unless absence is itself an explicitly registered failure condition. Plant a missing register and ungraded surface slots.

8. **Seed comparison ignores supersession and conflates revisions.**  
   **File:** `tools/node_verdicts.py:715–719, 723–732`  
   **Hunk:** `@@ -475,7 +705,31 @@`

   `seeded_landings()` scans raw historical lines rather than current ledger records. A superseded `LANDED` record remains selected when its correction is `LEAKED`, because the correction is filtered out. The documented planned correction of run-3 `snapshot_labels` would therefore leave the obsolete landing in future comparisons.

   The lookup also uses only `(run, node)`. Records for different revisions of the same task can overwrite each other and then be compared against a run bound to the wrong revision.

   **Fix:** Read the ledger’s current, supersession-resolved records and key comparisons by the bound revision as well as run and node. Plant both `LANDED → LEAKED` supersession and identical run/node labels across two revisions.

## Minor findings

9. **The rho override is not validated.**  
   **File:** `tools/hardness_ledger.py:229–234, 286`  
   **Hunks:** `@@ -200,10 +223,18 @@`, `@@ -221,31 +252,51 @@`

   The API and CLI accept negative, out-of-range and non-finite values. For example, three trials with `rho=-0.5` produce a zero design effect; other values can produce negative effective evidence or NaN priors.

   **Fix:** Validate rho at the `priors()` boundary, including finiteness and the supported correlation range, and issue a clear CLI error. Plant invalid numeric and non-finite overrides.

10. **`--seed-ledger` alone is silently ignored.**  
    **File:** `tools/node_verdicts.py:1120–1123`  
    **Hunk:** `@@ -731,10 +1109,18 @@`

    Seed loading and comparison occur only inside `if a.reference`, although the new option does not declare that dependency. A caller requesting seed comparison alone can receive a successful exit without any comparison.

    **Fix:** Run seed comparison independently, or reject `--seed-ledger` without `--reference` explicitly. Add a CLI test with a deliberately mismatched seed and no reference argument.

VERDICT: FAIL