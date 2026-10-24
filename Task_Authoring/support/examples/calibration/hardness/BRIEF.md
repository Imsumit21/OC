# Calibration brief — /create-hardening MODE B against V1 tasks (read-only)

Evidence base: completed V1 tasks that carry a prompt, a rubric, verifier results and six
baseline trajectories. No in-progress review material is read or used.

Method per task:
1. Blind: read the prompt, the injection/OE (design register) and ONE baseline run as the
   stand-in for the `/hardness` pre-check (V1 had no separate Opus pre-check). Predict the
   1A band and the mechanism verdicts before opening verifier results or difficulty stats.
2. Unblind: verifier results → per-run weighted rates (`verifier_matrix.py` →
   `tools/difficulty_stats.py`), mechanism × run verdicts from targeted reads of the other
   five runs, confound attribution (tool / fairness-UGT / verifier / run-validity).
3. Record agreement and the disagreement class; fix the playbook where the method missed.

Scratch only in this folder. Never run `Evals/tools/*.py`; never execute SQL.
