"""Validate v10 records against the saved rubric and evidence ledger.

QC percentages determine the score. Static checks track suggested repairs;
the helper does not independently judge arbitrary facts or generate rubrics.
"""

import argparse
import hashlib
import json
from pathlib import Path

from hg_rubric_qc import DIMENSIONS, GATES, FORMAT_VERSION

SCORE_PATH = Path("Task_Authoring/support/local_search/NO_EVAL_TASK_INPUTS/reports/drafts/rubric_score_record.json")


def calculate(record, rubric, check_result=None):
    from hg_rubric_qc import calculate as qc_calculate
    return qc_calculate(record, rubric, check_result)


def validate_score(root, content):
    from hg_rubric_loop import load_json, local, review_context
    from hg_preflight import reject_constant, unique_object

    record = json.loads(content, object_pairs_hook=unique_object, parse_constant=reject_constant)
    if not isinstance(record, dict) or not isinstance(record.get("rubric_path"), str):
        raise ValueError("Rubric scoring record needs rubric_path")
    if type(record.get("format_version")) is not int or record["format_version"] != FORMAT_VERSION:
        raise ValueError("Unsupported rubric scoring record format_version; rubric-revision-v10 uses format 5 with evidence-linked checks")
    if record.get("review_mode") != "AUDIT":
        raise ValueError("Rubric is evaluation-only; scoring review_mode must be AUDIT")
    path = local(root, Path(record["rubric_path"]))
    if hashlib.sha256(path.read_bytes()).hexdigest() != record.get("reviewed_json_sha256"):
        raise ValueError("Scoring record differs from the actual rubric bytes")
    context = review_context(root)
    if record.get("review_context_sha256") != context["sha256"]:
        raise ValueError("Scoring context changed; recalculate using current inputs/rules")
    states = context["manifest"]["inputs"]
    allowed = [item["path"] for key in ("rubric", "source:rubric") for item in states.get(key, {}).get("files", [])]
    if "rubric" not in states:
        allowed.append("Task_Authoring/support/local_search/NO_EVAL_TASK_INPUTS/09_Rubrics.json")
    if path.resolve() not in {local(root, Path(p)).resolve() for p in allowed}:
        raise ValueError("Score the actual saved rubric input in AUDIT; generated drafts are not inputs")
    try:
        rubric = load_json(path)
    except ValueError:
        rubric = None
    if not isinstance(rubric, list) or not rubric or any(not isinstance(row, dict) or
            not isinstance(row.get("title"), str) or not row["title"].strip() for row in rubric):
        if (record.get("schema_only") is not True or record.get("issues") != [] or
                record.get("hard_gates", {}).get("schema", {}).get("result") != "FAIL" or
                type(record.get("hard_gate_score")) is not int or record["hard_gate_score"] not in {1, 2} or
                not isinstance(record.get("unresolved"), list) or not record["unresolved"]):
            raise ValueError("Unusable criterion array needs an explicit schema-only FAIL with its review limits; no invented denominator")
        computed = dict(criterion_count=len(rubric) if isinstance(rubric, list) else None,
                        severity_counts=None, counted_rows=[], fractions=None, overall_quality_band=None,
                        gate_tier="catastrophic", coverage_ratio=None,
                        verdict="FAIL", verdict_score=record["hard_gate_score"], execution_status="PARTIAL")
    else:
        if record.get("schema_only"):
            raise ValueError("A usable criterion array requires the ordinary scoring review")
        # Validate basic scoring structure before the evidence reconciler reads
        # issue fields. Public save/report paths always run both validations.
        calculate(record, rubric)
        from hg_rubric_checks import validate_checks
        checked = validate_checks(record.get("checks"), rubric, record.get("issues", []),
                                  root=root, context=context["manifest"])
        expected_coverage = {k: checked[k] for k in ("required_outcomes", "covered_outcomes")}
        missing_count = sum(i["type"] == "missing_coverage" for i in record.get("issues", []))
        pending_count = checked["required_outcomes"] - checked["covered_outcomes"] - missing_count
        if pending_count:
            expected_coverage["unresolved_outcomes"] = pending_count
        if record.get("coverage") != expected_coverage:
            raise ValueError("Rubric coverage counts contradict the evidence-linked outcome checks")
        computed = calculate(record, rubric, checked)
    from hg_eval_release import require_binding
    release = require_binding(record, 'rubric')
    if not record.get("schema_only"):
        known = {s["id"] for s in record["checks"]["sources"]}
        for weight in record["weight_reviews"]:
            if not set(weight["source_ids"]) <= known:
                raise ValueError("Weight evidence must use the verified source ledger")
        check_oe_binding(root, record["oe_cross_check"], states, known)
    return {**computed, "eval_release": release, "review_mode": "AUDIT", "reviewed_json_sha256": record["reviewed_json_sha256"],
            "review_context_sha256": context["sha256"],
            "scoring_record_sha256": hashlib.sha256(content.encode("utf-8")).hexdigest()}


def saved_oe_text(root, states):
    """Text of the saved Oracle Events input, or None when the task has no OE."""
    from hg_rubric_loop import local
    entry = states.get("oe")
    if entry is not None:
        files = entry.get("files", []) if entry.get("state") == "saved" else []
    else:
        legacy = Path("Task_Authoring/support/local_search/NO_EVAL_TASK_INPUTS/08_Oracle_Events.md")
        files = [{"path": legacy.as_posix()}] if local(root, legacy).is_file() else []
    if not files:
        return None
    return "\n".join(local(root, Path(item["path"])).read_text(encoding="utf-8") for item in files)


def check_oe_binding(root, cross, states, known):
    """Bind the OE cross-check to the saved OE: presence, step labels and quoted text."""
    text = saved_oe_text(root, states)
    if (text is not None) != cross["oe_present"]:
        raise ValueError("oe_cross_check.oe_present contradicts the saved OE input; map every row to its OE steps when the task has OEs")
    if text is None:
        return
    flat = " ".join(text.split())
    for step in cross["steps"]:
        if " ".join(step.split()) not in flat:
            raise ValueError("OE step label is absent from the saved OE: " + step)
    for conflict in cross["conflicts"]:
        if " ".join(conflict["oe_quote"].split()) not in flat:
            raise ValueError("OE conflict oe_quote is absent from the saved OE: " + conflict["oe_quote"][:60])
        if not set(conflict.get("source_ids") or []) <= known:
            raise ValueError("OE conflict evidence must use the verified source ledger")


def approve_score(root, parsed):
    from hg_rubric_loop import local, POLICY

    if parsed.get("review_policy") != POLICY:
        raise ValueError("New scored rubric reports require the current review policy and scoring record")
    path = local(root, SCORE_PATH)
    if not path.is_file():
        raise ValueError("Save rubric-score before the scored rubric report")
    computed = validate_score(root, path.read_text(encoding="utf-8"))
    if parsed.get("ready_for_prefill") or parsed.get("review_mode") != "AUDIT":
        raise ValueError("Rubric is evaluation-only; prefill readiness is unsupported")
    for key in ("scoring_record_sha256", "reviewed_json_sha256", "review_context_sha256", "review_mode", "verdict", "verdict_score", "execution_status"):
        if parsed.get(key) != computed[key]:
            raise ValueError("Rubric report contradicts the computed scoring record: " + key)
    for key, label in (("gate_tier", "Gate tier"),):
        if key in parsed and parsed[key] != computed.get(key):
            raise ValueError("Rubric report contradicts the computed scoring record: " + label)
    if "coverage_ratio" in parsed and parsed["coverage_ratio"] != computed.get("coverage_ratio"):
        raise ValueError("Rubric report contradicts the computed scoring record: Coverage ratio")
    from hg_eval_release import report_binding
    return {**computed, **report_binding(parsed, computed['eval_release'])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(validate_score(Path(__file__).resolve().parents[4], args.record.read_text(encoding="utf-8"))))
    except (OSError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
