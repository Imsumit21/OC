# Oracle adjudication of the deep-recheck rejections (2026-11-05)

Verifier: `verify` tier `oracle`, verified_by `openai/gpt-6.1-sol#max`, no fallbacks. Two rounds.

| Finding | Round 1 | Round 2 (with the authority contract) | Final |
|---|---|---|---|
| DR1 (O1, OE 9 double space) | rejection correct | — | REJECTED |
| DR2 (O1, matrix "green" = fresh installs) | rejection correct | — | REJECTED |
| DR3 (O2, link the bug in the runbook page) | rejection wrong → MISSING | rejection holds | REJECTED |
| DR4 (O2, mirror to the Customer Support Playbook) | rejection wrong → MISSING | rejection holds | REJECTED |
| DR5 (O3, ZOM-506 NO CALL vs FIXED) | rejection correct | — | REJECTED |

Round 1 FAIL had no copy of the authority contract. Round 2 got:

- `Evals/WORKFLOW.md` "Task requirement authority" (`prompt-incorporation-v1`), L275–L343: "a reference used for facts does not incorporate all its rules"; "/oe must not present unincorporated rules as required outcomes".
- The platform `/prompt` report for this prompt + SQL (`plateform_report/6ae9909f7b5249d3148f3707_1_prompt-4.md` L31): "The QA Regression Runbook's checks are incorporated only for the new-ticket ask."

Round 2 verdict PASS. The oracle's reasoning: the prompt incorporates the runbook's checks to find unfiled findings, and it names the action for them itself (file a new Linear ticket). Linking the bug in the runbook or writing to the support playbook is not incorporated. Making either one a required OE outcome would impose an unincorporated rule. The oracle also withdrew its round-1 demand for an explicit exclusion: the contract needs a write to be incorporated before it can be required, and the prompt does not have to forbid every other step.

Effect on the OE set: none. No event is added or changed.
