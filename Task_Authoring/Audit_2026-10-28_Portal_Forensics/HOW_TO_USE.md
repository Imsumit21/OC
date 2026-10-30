# How to use this audit to improve the pipeline

Entry point for engineering work. [README.md](README.md) is the audit's own report; this page is the
navigation and action guide.

**What this folder is:** a forensic read-only study of 84 imported Portal reports (34 PASS / 13 NON-FAIL /
37 FAIL), the code and rules behind them, and a prioritized change list. **Nothing here is implemented.**

**What it is not:** a fix, a gate rerun, a model evaluation, or a failure-rate statistic. Report counts are
document counts, not independent trials.

---

## 1. Read in this order (~40 min)

| # | File | Why |
|---|---|---|
| 1 | [README.md](README.md) | The claim: no single skill fails; LOOP = scope + semantics + hardening + clocks + provenance |
| 2 | [PIPELINE_ROOT_CAUSES.md](PIPELINE_ROOT_CAUSES.md) | Causal chain from invocation to release boundary |
| 3 | [RECOMMENDATIONS.md](RECOMMENDATIONS.md) | P0/P1 changes with acceptance tests and regression cases |
| 4 | [FINAL_PRE_IMPLEMENTATION_REVIEW.md](FINAL_PRE_IMPLEMENTATION_REVIEW.md) | WP0–WP6 work packages and prerequisites |
| 5 | Stage detail as needed | [INJECTION](INJECTION.md) · [PROMPT](PROMPT.md) · [OE](OE.md) · [RUBRICS](RUBRICS.md) |

Read (5) only for the stage you are changing.

## 2. Start here: the seven work packages

| WP | Goal | Primary evidence |
|---|---|---|
| WP0 | Freeze the acceptance matrix and regression controls | [FINAL…:67](FINAL_PRE_IMPLEMENTATION_REVIEW.md) |
| WP1 | Fix the narrow model-label incompatibility | [PIPELINE_ROOT_CAUSES.md](PIPELINE_ROOT_CAUSES.md) |
| WP2 | Reconcile declared results with stage readiness | [RUBRICS.md](RUBRICS.md) |
| WP3 | Add a versioned handoff/promotion inspector | [expert_reviews/INDEPENDENT_COUNT.md](expert_reviews/INDEPENDENT_COUNT.md) |
| WP4 | Add predicate examples and source-change regression checks | [RUBRICS.md](RUBRICS.md) · [PROMPT.md](PROMPT.md) |
| WP5 | Strengthen run binding before baseline promotion | [PIPELINE_ROOT_CAUSES.md](PIPELINE_ROOT_CAUSES.md) |
| WP6 | Plan migration and one controlled local canary | [RECOMMENDATIONS.md](RECOMMENDATIONS.md) |

WP0 is a prerequisite: without a frozen acceptance matrix the later work packages cannot be shown to help.

## 3. Turn a finding into a change

Each recommendation names **evidence → proposed change → acceptance test**. Work it that way round:

1. Open the cited section in the stage report; read the *contrary* evidence too — several reports contain
   PASS results that undercut a naive fix.
2. Confirm the current behaviour in code before editing. The audit names the exact lines:
   `Task_Authoring/tools/stage_gate.py:609`, `:618`, `:2085`, `:2285`, `:2360`;
   `v3_artifact_checks.py:134`; `Evals/3_Rubrics_Eval.md:36`;
   `Task_Authoring/playbooks/09_Rubric_Writing.md:205`.
3. Implement to the acceptance test, not to the prose. The tests are written to fail a plausible-but-wrong fix.
4. Re-run the named regression case from
   [RECOMMENDATIONS.md](RECOMMENDATIONS.md) — e.g. zero lint flags with a duplicate Transcend identity must
   still be rejected semantically; a 27-row rubric with one Major must follow the *selected* profile.

**Do not** resolve a policy conflict by silently editing a clock, a difficulty assignment, an authorship rule
or a Portal document. Three subsystems genuinely disagree today (00:00Z vs 07:00Z freeze; percentage bands vs
fail-any-Major; local CLEAN vs external PASS). Choosing between them is a decision, not a cleanup.

## 4. Preserve the evidence while you change code

- Old PASS blocks are **historical evidence** — never re-stamp or backfill them (WP6).
- A pasted new certificate must not invalidate itself.
- Rubric-only edit → regrade affected rows. SQL/source edit → invalidate dependent run applicability and
  semantic checks. OE edit → refresh affected human-time and review dependencies.
- One observed failure propagating to three outputs is **one** root pattern, not three failures.

## 5. Verifying this audit

```bash
python3 evidence/verify_audit.py     # re-hashes originals, checks verdict lines, counts, links
```

The verifier resolves paths relative to the repo root and needs **667 files / 52.4 MB** — the 91 report
originals, 446 artifact versions and 130 rule/tool sources. It does not run gates, SQL or models.

## 6. ⚠️ This copy is redacted

- Task containers are `TASK_A`…`TASK_W`; reviewers are `Reviewer A`…`Reviewer I`. Pairing is preserved.
- Consequence: **553 of 886 file citations no longer resolve**, and `verify_audit.py` reports `passed: false`
  with 435 errors. That is expected, not corruption.
- Use the unredacted original + separate redaction key to verify. Keep the key outside this folder.
- Citations are **repo-root relative** (`Task_Authoring/...`), not relative to this directory.

## 7. Scope limits to respect

Three confirmed sent-task FAILs (Reviewer A/B/C). Reviewer D's FAIL is real but **unbound** to the sent task;
Reviewer E has a verified send and no return. Do not upgrade either into a fourth failure. Zero preserved OE
FAILs. Missing reports are coverage gaps, not inferred passes or failures.
