# Blind rubric-check calibration protocol (scratch input for calibration agents)

Workspace root: the folder that holds `Evals/` and `Task_Authoring/`.
Scratch dir: `Task_Authoring/support/examples/calibration/rubric/` (CAL below).

## Rules
- READ-ONLY everywhere except your own output file(s) under CAL/pred_<pass>/. Never write elsewhere.
- BLIND: never open `Evals/references/rules/rubric_qc_cases.json`, `rubric_qc_examples.md`,
  `rubric_review_record.md`, or any other file in CAL except your assigned inputs and the playbook
  copy named in your prompt.
- Never run `Evals/tools/*.py`; never execute SQL; no universe search is needed (other universes).
- Human-only rule: you JUDGE criteria. Never write replacement wording, never propose criterion text.
- Apply ONLY the check mode of the playbook copy named in your prompt, as written: its check-mode
  checklist, its severity table, its dimension table, and the files it tells you to consult.
  Do not import checks or severities the playbook does not state. Doc-name aliases (paths in the
  playbook that do not exist): `07_Rubric_Writing.md` = `Task_Authoring/references/Docs/8_Rubric Writing - V2.md`;
  `06_Oracle_Events.md` = `7_Oracle Events V2.md`; `10_Common_Errors_and_PreQC.md` = `9_Common Errors & Pre-QC - V2.md`;
  `09_Long_Horizon_Task.md` = `10_Long Horizon Guidelines - V2.md`; `QC_Spec_V2.csv` = `QC_Spec_Doc_Latest.csv`.
- No coverage plan or evidence ledger exists for these cases: derive the requirement list
  directly from the prompt (as the plan would) and use it for coverage. Universe facts are not
  available for historical cards (other universes): do not guess `incorrect`; only flag a value
  when the prompt/criteria themselves contradict it. Cards carry no weight field: Criteria
  Weights = N/A. Categories may be lowercase ("outcome"); treat case as cosmetic.

## Output — one JSON file per card/task: CAL/pred_<pass>/card_NN.json
{
 "id": "card_NN",
 "n_criteria": int,
 "requirements": ["R1: short noun phrase", ...],
 "findings": [ {"c": "C3", "defect": "short label from the playbook", "severity": "Major|Moderate|Minor|dimension-only|note",
                "quote": "offending span", "why": "one line"} ],
 "missing_coverage": [ {"req": "R4", "why": "..."} ],
 "overlap_groups": [ {"rows": ["C2","C5"], "condition": "..."} ],
 "predicted_all_fail_rows": [ {"c": "C7", "basis": "..."} ],
 "tally": {"rows_major": int, "rows_moderate": int, "rows_minor": int, "missing_outcomes": int,
           "pct_major": float, "pct_moderate_or_worse": float, "pct_any": float},
 "dimensions": {"overall_quality": "FAIL|NON-FAIL|PASS", "criteria_weights": "N/A|FAIL|NON-FAIL|PASS",
                "category_balance": "FAIL|PASS", "process": "FAIL|NON-FAIL|PASS",
                "agent_centric": "FAIL|NON-FAIL|PASS", "negative": "FAIL|PASS",
                "predicted_all_fail": "FAIL|PASS", "other": "any other playbook dimension: name=status"},
 "readiness": "FAIL-RISK|NON-FAIL-RISK|CLEAN",
 "confidence": "high|medium|low",
 "limits": "what could not be checked"
}
Count each criterion once at its highest severity; missing outcomes add to the numerator only;
the denominator is the authored criterion count. Readiness = FAIL-RISK if any dimension FAILs,
NON-FAIL-RISK if any is NON-FAIL, else CLEAN. Keep `why` lines short. Write valid JSON
(check with `python3 -m json.tool <file>`).
