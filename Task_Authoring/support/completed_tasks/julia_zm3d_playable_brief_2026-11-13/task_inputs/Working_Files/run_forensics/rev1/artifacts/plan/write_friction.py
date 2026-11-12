#!/usr/bin/env python3
"""Write 03_Error_Async_Config.txt for the current SQL: Friction: none (the design uses no forced error and no wait).
Run before `stage_gate.py error-async --paste`; the pasted gate block of an earlier run is dropped."""
import hashlib, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
TASK = HERE.parents[1]
sys.path.insert(0, str(HERE))
import design_model as M
sha = hashlib.sha256((TASK / "01_Universe_Inject.sql").read_bytes()).hexdigest()[:12]
S = M.SEED
def tk(n): return M.BY_NAME[n]["ticket"]
text = f"""# Error Injection & Async Wait (screen 16) — optional

Decision for {M.SLUG} (injection rev1, SQL sha256 {sha}): no forced errors and no async waits.
Reason: the scenario is a hand-off brief and the standing of an asset pack, not an outage story, and friction is never a
hardness or horizon lever (playbooks/03_Error_Async_Config.md hard gate 1). Applies to the baseline run and the verifier;
nothing is configured, so this file is not supplied to /prompt.

```
Friction:          none

error_functions:
error_mode:
error_rate:

wait_functions:
wait_min_seconds:
wait_max_seconds:
```

On screen 16, leave every field empty.

## Facts for the human (feeds `/create-oe-writing`)

- No forced errors and no async waits, so the Oracle Events need no recovery or wait steps.

## Post-baseline checks

- Forced error fired: n/a (none configured)
- Async submit, check, get appeared: n/a (none configured)
- Non-default values confirmed: n/a

## Self-review

Checked against playbook 03 gates 1 to 4 and GEN_EXECUTION §6a.

| Area | Counter-reading (strongest argument against Friction: none) | Evidence that resolves it | Verdict |
|---|---|---|---|
| Is the scenario about an outage? | A zip that was cut off on upload and will not unpack (Brian's log {S['c4_log']['id']}) reads like a failure a forced error could mirror | That is a fact about one archive in the task's records, not an outage of any tool Julia uses; no seeded or base record in the task's window says a service was down | none stands |
| Horizon and difficulty | Waits on the per-ticket reads would lengthen every run past the call floor | Waits and retries are not counted toward the horizon and are not a lever (playbook gate 1); the call budget comes from one note read per line of the pack ({tk(M.LINES[0]['name'])} to {M.LAST_CHILD}) and the ticket follow-through (01_Hardness_Manifest.json call_budget) | none stands |
| Verifier and Oracle Events | A configured error would change what /oe and /rubric can require | With nothing configured every step uses the plain read path, e.g. the note on {tk('Refrigerator')} and Marcus's post {S['a1_post']['id']} | none stands |

Unresolved: none. Every deciding record is persona-readable (dossier 1.E, check-sql PASS on the SQL above).
"""
(TASK / "03_Error_Async_Config.txt").write_text(text)
print("wrote 03_Error_Async_Config.txt for sql", sha)
