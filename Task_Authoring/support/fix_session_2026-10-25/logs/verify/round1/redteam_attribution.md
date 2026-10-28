## Result

**The change is falsifiable.** There are material counterexamples involving slots-only channels, revision-scoped seeded landings, and overlapping aggregate observations.

I used no tools. Results below are source-level traces through the supplied code, not claims of executed tests.

## 1. A valid slots-only channel can never count toward the go rule

**Input**

A declared channel supported explicitly by `channel_reports`:

```python
channels = {
    "tool_surface:notes": {
        "kind": "tool_surface",
        "slots": ["S01"],
        "source": "notes",
        "preregistered": True,
    }
}
graded = {"S01": False}
```

The run is valid, and every decision and artifact write is by the expected model, `claude-opus-5-5`. There are no other loss channels.

**Code path**

The `if not c.get("degrade")` branch of `channel_reports` produces:

```python
{
    "verdict": "FAILED",
    "failed_slots": ["S01"],
    "failed_members": [],
    "deciding_models": [],
    "preregistered": True,
    ...
}
```

That branch never determines who decided the failed slot.

`go_rule` then evaluates:

```python
own([])  # False
```

and puts the channel under `off_model_or_unregistered`.

**Result: counterexample.**

`independent_channels` is **0**, although this is a pre-registered failed channel in the expected model’s own decisions. This is not merely conservative handling of an actually unknown writer: the implementation discards the provenance for **every** slots-only channel, including a fully attributable one.

---

## 2. Seeded-landings comparison can silently compare the wrong revision

**Input**

A ledger contains these two current, non-superseding records. Other required fields are valid:

| ID | Task | Revision | Run | Node | Verdict | Keys |
|---|---|---|---|---|---|---|
| `seed13` | `T` | `rev13` | `run-1` | `R` | LANDED | `["K-01", "K-02"]` |
| `seed14` | `T` | `rev14` | `run-1` | `R` | LANDED | `["K-01"]` |

`seed14` occurs later in the file.

The evaluated report is bound to **rev13**, and its `R.landed_keys` is `["K-01"]`. The reference items also imply only `K-01`.

**Code path**

`seeded_landings` ignores both revision and SQL hash:

```python
out[(x.get("run"), x.get("node"))] = ...
```

Consequently, `seed14` overwrites `seed13`.

`compare_attribution` looks up only:

```python
seeds.get(("run-1", "R"))
```

It compares the rev13 result against the **rev14** seed, finds both equal to `["K-01"]`, and emits no landed-key difference.

**Result: counterexample.**

The actual rev13 disagreement—its seed also claims `K-02`—is missed. A cross-revision ledger is a normal input for this project; it is not a malformed-ledger attack.

### Separate silent path: `--seed-ledger` without `--reference`

The CLI accepts `--seed-ledger`, but the only call to `seeded_landings` is inside:

```python
if a.reference:
```

With a contradictory seed ledger but no `--reference`, there is no seed comparison or diagnostic. Absent another error, the command can return success. The option’s help does not state that it requires `--reference`.

---

## 3. Aggregate observations bypass the one-trial-per-run-family rule

**Input**

Two ordinary per-rule library aggregates describe the **same six runs** of the same task and revision.

Common fields:

```python
{
    "kind": "observation",
    "task": "T",
    "revision": "r1",
    "source": "platform-baseline",
    "model": "claude-opus-4-8",
    "harness": {"name": "h", "version": "1"},
    "epistemic": "derived",
    "family": "A17",
    "weight": 0.5,
    "evidence": {
        "run_ids": [
            "run-1", "run-2", "run-3",
            "run-4", "run-5", "run-6"
        ]
    }
}
```

The two records differ as follows:

```python
# Rule N1 lands in all six runs.
{"node": "N1", "counts": {"runs": 6, "landed": 6, "leaked": 0}}

# Rule N2 leaks in those same six runs.
{"node": "N2", "counts": {"runs": 6, "landed": 0, "leaked": 6}}
```

These are distinct per-node observations, not conflicting versions of one record.

**Required H2 result**

There are six `(task, revision, run, family)` trials. Every trial includes a LANDED verdict for N1, so all six are family landings.

At weight `0.5` and `rho = 0.5`:

```text
trials = 6
deff = 3.5
landed evidence = 3 / 3.5
Beta = (1.8571, 1.0000)
mean = 0.65
n_eff = 0.8571
```

**Actual code path**

Verdict records go through the trial dictionary. Observation records do not:

```python
f["obs"].append({
    "landed": w * landed,
    "not_landed": w * not_landed,
    "trials": landed + not_landed,
    ...
})
```

Both observations are subsequently summed:

```text
trials = 12
weighted landed = 3
weighted non-landed = 3
deff = 6.5
Beta = (1.4615, 1.4615)
mean = 0.50
n_eff = 0.9231
```

**Result: material counterexample.**

This both double counts the same family/run trials and misclassifies six family landings as a mixture of landings and non-landings. The task-level design effect does not repair the erroneous outcome mixture.

If aggregate records cannot establish run overlap, the implementation cannot safely promise one trial per tuple for them. It currently neither reconciles nor refuses this input.

### What the supplied A17 output establishes

Its displayed effective-sample arithmetic is internally consistent:

```text
15/15.5 + 3/3.5 + 4/2.5 = 3.4249
```

But the final excerpt does not expose the underlying records’ run cohorts. It therefore does not establish that its 30 library trials are non-overlapping family/run trials. I am **not** asserting that the displayed A17 dataset necessarily contains the overlap above.

---

## 4. Any non-class error suppresses an independently reproducible class-rule failure

**Input**

A complete register row:

```python
truth = {
    "K-01": {"key": "K-01", "count": "2", "class": "HOLD"}
}
rows = {
    "K-01": {"key": "K-01", "count": "3", "class": "READY"}
}
rules = {
    "class_rule": {"decides": ["class"]}
}
touched = {"class_rule": {"K-01"}}
abl = {
    "class_rule": {
        "K-01": {"key": "K-01", "count": "2", "class": "READY"}
    }
}
```

The correct class rule is “positive count means HOLD.” Its designed natural misreading produces READY at both counts 2 and 3.

Thus:

- `2 → 3` is an unrelated count slip.
- Correctly classifying the written count `3` still gives HOLD.
- READY is reproduced by the class-rule ablation, not explained by the count slip.

**Code path**

`classify` finds a non-class difference, so:

```python
if f == class_field and own:
    d["classification"] = "cascade"
```

It never evaluates the class rule’s candidates or ablation match. No key is attributed to `class_rule`.

`reference_landed` repeats this assumption by skipping every class item whose key has another wrong field.

**Result: counterexample to the causal attribution claim.**

An independent class-rule failure is erased as a cascade, and the mechanism has no landed key. The implementation tests **coexistence of differences**, not whether the field differences explain the class.

If this is intended as a conservative grading convention, it needs to be described as such; the stronger claim that the class “follows” those errors is unsupported on this input.

---

## 5. Missing columns reopen the class-only coincidence bug at the helper boundary

**Input to `control_trials` / `channel_reports`**

```python
truth = {
    "K-01": {"key": "K-01", "count": "0", "class": "READY"}
}
degraded = {
    "K-01": {"key": "K-01", "count": "1", "class": "HOLD"}
}
rows = {
    "K-01": {"key": "K-01", "class": "HOLD"}  # count absent
}
```

Use columns `["key", "count", "class"]`. For the control test, the rule decides `count`, declares K-01 as a control, and its over-application returns `degraded`. For the channel test, the channel’s degrade returns `degraded`.

**Code path**

Both functions compute changed fields only after filtering for fields present in the written row:

```python
changed = [... if f in rows[k] and dg[k].get(f) != truth[k].get(f)]
own = [f for f in changed if f != class_field] or changed
```

Therefore:

```text
changed = ["class"]
own = ["class"]
```

The matching HOLD yields:

- **OVER-APPLIED** for the control;
- **FAILED** for the channel.

But the operator actually changes `count`; the row supplies no evidence of its changed value `1`. The class fallback should not become eligible merely because the operator’s primary field was omitted.

**Result:** deterministic helper-level failure. The existing planted tests cover a **present** count with a wrong or missing-value spelling, not an **absent column**.

The excerpts do not show whether `tl.table` always fills omitted columns, so I do not claim end-to-end CSV reachability from these artifacts alone. The overall FAIL does not depend on this boundary finding.

---

## 6. Accepted `rho` overrides can crash prior construction

**Input**

Two counted verdict trials in one task, and:

```text
priors --model claude-opus-4-8 --rho -1
```

**Code path**

The CLI accepts any float, and `priors` supplies no range or finiteness check:

```python
design_effect(2, -1) == 0
```

The subsequent evidence division raises `ZeroDivisionError`.

Likewise, `--rho nan` propagates NaNs into the prior.

**Result:** an unhandled public-input error path. This is secondary to the material attribution and counting failures above.

## Obvious attacks that the shown change does block

These results are supported by the displayed conditions and supplied planted-test outputs; I did not rerun them.

| Attack | Result |
|---|---|
| In-cohort count `7` where no ablation reproduces it | `mechanism?`, pending review, no landed key. Ledger append refuses it without `disposed_by`. |
| Pure control over-application in the planted K-04 run | Separate control record; no mechanism landing. |
| A run with both an in-scope landing and a control over-application | Both records are retained; the control itself is not added to the go tally. |
| Class matches a control/channel degrade, but the present primary field does not | Blocked by the own-field matching check. The supplied `7,READY` control case exercises this. |
| Explicit off-model deciding model | Excluded by `own`; rev13 run-4’s Opus 5 validation landing demonstrates this. |
| Explicit Boolean `preregistered=False` | Excluded by the go-rule condition. |
| Two eligible losses sharing a key or source | Merged. The grouping also merges a new item that bridges two existing groups. |
| Multiple verdict nodes in one run/family | Collapsed into one trial, with “any LANDED” determining the outcome. This protection does not extend to observations. |
| Properly typed control/channel records entering mechanism priors | Blocked by the initial kind filter. |
| Same-revision seed/reference disagreement for an existing compared rule | Detected in the supplied planted cases. The revision collision above is outside that coverage. |

## Revision-13 adjudication

### Run-4: SP-039 / SP-091 / SP-079

The displayed output is internally consistent with the stated adjudication:

- Validation has the eight reference-implied landings:  
  `003, 019, 035, 051, 067, 083, 099, 115`.
- SP-039 and SP-091 remain **pending review**, not landed.
- SP-079 has receipt-field slips; its class coincidence does not add a validation landing.
- The seeded validation record’s extra keys are **SP-039 and SP-079**, not SP-091. That matches the reported seed comparison.

The notes’ values—written `2`, truth `0`, natural-reading values `3/0`—would justify rejecting the designed validation attribution for SP-039/091. However, the SQL rows and trajectory excerpts establishing those values are not supplied here.

### Run-3: SP-091 / SP-106 / SP-112

The output correctly exposes a disagreement:

- `snapshot_labels` has no landings;
- all three keys are pending;
- the seed claims all three landed.

The later single-key re-extraction explanation is consistent with transcription slips, but its detailed chronology and content are asserted in the notes rather than demonstrated by the supplied trajectory excerpts.

**Importantly, the tool has not finalized these cases as slips.** They remain pending, and the notes explicitly defer seed correction to P2. That is not itself a contradiction.

Finally, rev13 run-6 reporting one loss channel while `run_valid=False` is not evidence of a V3 pass: validity is separately and visibly false.

VERDICT: FAIL