#!/usr/bin/env python3
"""Parse a V6 stage report without guessing verdicts or borrowing other scores."""

import argparse
import json
from pathlib import Path
import re


STAGES = ("injection", "prompt", "hardness", "golden", "oe", "rubric")
SCORED = {"prompt", "hardness", "rubric"}
HARDNESS_VERSION = "model-aware-v3"
HARDNESS_FIELDS = ("Difficulty", "Gate decision", "Gate reason", "Assessment version", "Assessed model", "Assessment mode")
HARDNESS_MODES = {"Opus": "OPUS_OBSERVED", "Haiku": "HAIKU_TO_OPUS", "Unconfirmed": "UNCONFIRMED"}
RUBRIC_FIELDS = ("Review policy", "Review mode", "Review iteration", "Reviewed JSON SHA-256",
                 "Review context SHA-256", "Ready for prefill", "Open substantive defects", "Unresolved checks")
RECORD_FIELD = "Review record SHA-256"
# Model that produced the report; distinct from hardness "Assessed model" (the run under review).
EVALUATOR_FIELD = "Evaluator model"
CLOCK_FIELD = "Clock"
GOLDEN_FIELDS = ("Review policy", "Review mode", "Review iteration", "Reviewed golden SHA-256",
                 "Review context SHA-256", RECORD_FIELD)
RUBRIC_V8_FIELDS = ("Gate tier", "Golden verified", "Coverage ratio", "Repairs")
GOLDEN_V4_FIELDS = ("Finding classes", "Repair owners", "Integrity")
HISTORICAL_GOLDEN = {"golden-audit-v1", "golden-audit-v2", "golden-audit-v3"}
HISTORICAL_RUBRIC = {"rubric-revision-v3", "rubric-revision-v4", "rubric-revision-v5", "rubric-revision-v6", "rubric-revision-v7", "rubric-revision-v8", "rubric-revision-v9"}


def visible_lines(content):
    """Ignore fenced examples; allow Markdown bold around displayed fields."""
    fence = None
    for raw in content.splitlines():
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", raw)
        if match:
            marker, rest = match.groups()
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence) and not rest.strip():
                fence = None
            continue
        if fence is None:
            yield raw.replace("**", "").strip()


def parse_result(stage, content):
    if stage not in STAGES:
        raise ValueError(f"Unknown evaluation stage: {stage}")
    lines = list(visible_lines(content))
    headings = [i for i, line in enumerate(lines) if line.startswith("### FINAL VERDICT")]
    if len(headings) != 1:
        raise ValueError("Expected exactly one rendered ### FINAL VERDICT: heading.")
    start = headings[0]
    match = re.fullmatch(r"### FINAL VERDICT:[ \t]*(PASS|NON-FAIL|FAIL)", lines[start])
    if not match:
        raise ValueError("Verdict must be PASS, NON-FAIL or FAIL; put any score on its own line.")
    verdict = match.group(1)
    fields = {}
    names = ("Score", "Execution status", "Next action", "Evidence limits", EVALUATOR_FIELD, CLOCK_FIELD)
    if stage == "hardness":
        names += HARDNESS_FIELDS + ("Prediction basis",)
    if stage == "rubric":
        names += RUBRIC_FIELDS + (RECORD_FIELD, "Scoring record SHA-256") + RUBRIC_V8_FIELDS
    if stage == "golden":
        names += GOLDEN_FIELDS + GOLDEN_V4_FIELDS
    if stage in {"prompt", "rubric", "oe"}:
        names += ("Eval version", "Eval release SHA-256")
    if stage == "prompt":
        names += ("Reviewed prompt SHA-256", "Review context SHA-256", "Prompt record SHA-256")
    if stage == "oe":
        names += ("Review policy", "Completeness score", "Accuracy score", "Reviewed OE SHA-256",
                  "Review context SHA-256", "OE record SHA-256", "Path feasibility", "Task solvability", "Prompt follow-up")
    for line in lines[start + 1:]:
        if re.match(r"^#{1,6}\s", line):
            break
        for name in names:
            prefix = name + ":"
            if line.startswith(prefix):
                if name in fields:
                    raise ValueError(f"Duplicate {name} field in verdict block.")
                fields[name] = line[len(prefix):].strip()
    required = {"Execution status", "Next action", "Evidence limits"}
    if stage == "hardness":
        required.update(HARDNESS_FIELDS)
    if not required.issubset(fields) or any(not value for value in fields.values()):
        raise ValueError("Verdict block needs nonempty " + ", ".join(sorted(required)) + ".")
    # Unscored reports omit Score; accept an explicit null for existing writers.
    raw_score = fields.get("Score", "null")
    if not re.fullmatch(r"null|[1-5]", raw_score):
        raise ValueError("Score must be one integer from 1 to 5 or null.")
    score = None if raw_score == "null" else int(raw_score)
    status = fields["Execution status"]
    if status not in {"COMPLETE", "PARTIAL", "BLOCKED"}:
        raise ValueError("Execution status must be COMPLETE, PARTIAL or BLOCKED.")
    if stage == "hardness" and score is not None and status != "COMPLETE":
        raise ValueError("Scored hardness requires a COMPLETE review; incomplete evidence is unscored provisional NON-FAIL.")
    if verdict == "NON-FAIL" and status in {"PARTIAL", "BLOCKED"}:
        if score is not None:
            raise ValueError("Provisional NON-FAIL must remain unscored; incomplete checks do not establish a scoring band.")
        if fields["Evidence limits"].lower() == "none":
            raise ValueError("Provisional NON-FAIL must identify unresolved evidence or checks.")
    else:
        if status == "BLOCKED" or (verdict != "FAIL" and status != "COMPLETE"):
            raise ValueError("PASS requires COMPLETE; a demonstrated FAIL uses COMPLETE or PARTIAL.")
        if stage == "oe":
            if (verdict, score) not in {("PASS", 5), ("NON-FAIL", 3), ("FAIL", 2)}:
                raise ValueError("OE scores are PASS 5, NON-FAIL 3 or FAIL 2.")
        elif stage in SCORED:
            allowed = {"PASS": {5}, "NON-FAIL": {3, 4}, "FAIL": {1, 2}}
            if score not in allowed[verdict]:
                raise ValueError(f"{verdict} has an incompatible score for {stage}.")
        else:
            if verdict == "NON-FAIL":
                raise ValueError(f"{stage} uses NON-FAIL for PARTIAL/BLOCKED reviews, not a completed scoring band.")
            expected = 5 if stage == "golden" and verdict == "PASS" else None
            if score != expected:
                raise ValueError(f"{stage} requires {'Score: ' + str(expected) if expected is not None else 'no numeric score'} for {verdict}.")
    result = {"verdict": verdict, "verdict_score": score, "execution_status": status}
    if EVALUATOR_FIELD in fields:
        result["evaluator_model"] = fields[EVALUATOR_FIELD]
    if CLOCK_FIELD in fields:
        result["clock"] = fields[CLOCK_FIELD]
    if stage in {"prompt", "rubric", "oe"}:
        for label, key in (("Eval version", "eval_version"), ("Eval release SHA-256", "eval_release_sha256"),
                           ("Reviewed prompt SHA-256", "reviewed_prompt_sha256"),
                           ("Prompt record SHA-256", "prompt_record_sha256")):
            if label in fields:
                if label.endswith('SHA-256') and not re.fullmatch(r'[a-f0-9]{64}', fields[label]):
                    raise ValueError(label + ' must be a lowercase SHA-256 fingerprint')
                result[key] = fields[label]
        if stage == 'prompt' and 'Review context SHA-256' in fields:
            if not re.fullmatch(r'[a-f0-9]{64}', fields['Review context SHA-256']):
                raise ValueError('Review context SHA-256 must be a lowercase SHA-256 fingerprint')
            result['review_context_sha256'] = fields['Review context SHA-256']
    if stage == "oe":
        labels = {"Reviewed OE SHA-256": "reviewed_oe_sha256", "Review context SHA-256": "review_context_sha256",
                  "OE record SHA-256": "oe_record_sha256"}
        bound = score is not None or any(label in fields for label in labels)
        if bound:
            needed = set(labels) | {"Review policy", "Eval version", "Eval release SHA-256"}
            if not needed <= fields.keys() or fields["Review policy"] not in {"oracle-events-v1", "oracle-events-v2"}:
                raise ValueError("OE report requires a recognized policy, source and release bindings")
            result["review_policy"] = fields["Review policy"]
            for label, key in labels.items():
                if not re.fullmatch(r"[a-f0-9]{64}", fields[label]):
                    raise ValueError(label + " must be a lowercase SHA-256 fingerprint")
                result[key] = fields[label]
            if fields['Review policy'] == 'oracle-events-v2':
                for label, key, allowed in (
                    ('Path feasibility', 'path_feasibility', {'SUPPORTED','INCOMPLETE','BROKEN','UNRESOLVED'}),
                    ('Task solvability', 'task_solvability', {'SUPPORTED_BY_OE','NOT_ESTABLISHED','UPSTREAM_BLOCKER'}),
                    ('Prompt follow-up', 'prompt_follow_up', {'REQUIRED','NONE'})):
                    if fields.get(label) not in allowed:
                        raise ValueError('OE report needs a valid ' + label)
                    result[key] = fields[label]
                if ((result['task_solvability'] == 'SUPPORTED_BY_OE') != (result['path_feasibility'] == 'SUPPORTED') or
                        (result['task_solvability'] == 'UPSTREAM_BLOCKER') != (result['prompt_follow_up'] == 'REQUIRED')):
                    raise ValueError('OE feasibility diagnostics contradict each other')
        for label, key in (("Completeness score", "completeness_score"), ("Accuracy score", "accuracy_score")):
            value = fields.get(label, "null")
            if value not in {"2", "3", "5", "null"}:
                raise ValueError(label + " must be 2, 3, 5 or null")
            result[key] = None if value == "null" else int(value)
        components = [result["completeness_score"], result["accuracy_score"]]
        if score is not None and (None in components or min(components) != score):
            raise ValueError("OE overall score must match the minimum of both component scores")
        if score is None and any(c is not None for c in components):
            raise ValueError("Unresolved OE reviews omit numeric scores; preserve confirmed findings separately")
    if stage == "golden" and any(name in fields for name in GOLDEN_FIELDS):
        from hg_golden_review import POLICY

        if fields.get("Review policy") not in HISTORICAL_GOLDEN | {POLICY}:
            raise ValueError("Golden review needs a recognized review policy.")
        if fields["Review policy"] == POLICY and verdict == "PASS" and not set(GOLDEN_FIELDS) <= fields.keys():
            raise ValueError("Golden PASS needs the current answer, context and record hashes and audit iteration.")
        if "Review mode" in fields and fields["Review mode"] not in {"AUDIT", "DRAFT"}:
            raise ValueError("Golden review mode must be AUDIT or explicit DRAFT.")
        for name in ("Reviewed golden SHA-256", "Review context SHA-256", RECORD_FIELD):
            if name in fields and not re.fullmatch(r"[a-f0-9]{64}", fields[name]):
                raise ValueError(name + " must be a lowercase SHA-256 fingerprint.")
        if "Review iteration" in fields and not re.fullmatch(r"[1-9][0-9]*", fields["Review iteration"]):
            raise ValueError("Golden review iteration must be a positive integer.")
        for name, key in zip(GOLDEN_FIELDS, ("review_policy", "review_mode", "review_iteration",
                                             "reviewed_golden_sha256", "review_context_sha256", "review_record_sha256")):
            if name in fields:
                result[key] = int(fields[name]) if name == "Review iteration" else fields[name]
        for name, key in zip(GOLDEN_V4_FIELDS, ("finding_classes", "repair_owners", "integrity")):
            if name in fields:
                result[key] = fields[name]
    if stage == "rubric" and any(name in fields for name in RUBRIC_FIELDS + (RECORD_FIELD,)):
        from hg_rubric_loop import POLICY

        current_audit = fields.get("Review policy") == POLICY and fields.get("Review mode") == "AUDIT"
        required_review = {"Review policy", "Review mode", "Reviewed JSON SHA-256"}
        if not current_audit:
            required_review.add("Ready for prefill")
        if fields.get("Review mode") == "CREATE":
            required_review.update(RUBRIC_FIELDS)
        if not required_review.issubset(fields):
            raise ValueError("Rubric review needs explicit policy, mode and JSON hash. Historical CREATE records also need their legacy readiness fields.")
        if fields["Review policy"] not in HISTORICAL_RUBRIC | {POLICY} or fields["Review mode"] not in {"CREATE", "AUDIT"}:
            raise ValueError("Rubric review needs a recognized policy and CREATE or AUDIT mode.")
        if "Ready for prefill" in fields and fields["Ready for prefill"] not in {"Yes", "No"}:
            raise ValueError("Ready for prefill must be Yes or No.")
        for name in ("Reviewed JSON SHA-256", "Review context SHA-256", RECORD_FIELD):
            if name in fields and not re.fullmatch(r"[a-f0-9]{64}", fields[name]):
                raise ValueError(f"{name} must be a lowercase SHA-256 fingerprint.")
        for name in ("Review iteration", "Open substantive defects", "Unresolved checks"):
            if name in fields and not re.fullmatch(r"0|[1-9][0-9]*", fields[name]):
                raise ValueError(f"{name} must be a nonnegative integer.")
        ready = fields.get("Ready for prefill") == "Yes"
        if fields["Review mode"] == "CREATE":
            if int(fields["Review iteration"]) < 1:
                raise ValueError("CREATE review iteration must start at 1.")
            cleared = verdict == "PASS" and score == 5 and status == "COMPLETE"
            if cleared and fields["Review policy"] == POLICY and RECORD_FIELD not in fields:
                raise ValueError("Ready CREATE reviews require Review record SHA-256 from rubric-review.")
            if ready != cleared or (cleared and any(int(fields[n]) for n in
                                                   ("Open substantive defects", "Unresolved checks"))):
                raise ValueError("CREATE readiness must match a complete PASS with zero substantive defects and unresolved checks.")
        elif ready:
            raise ValueError("AUDIT reviews do not publish a prefill; readiness must be No.")
        result.update(review_policy=fields["Review policy"], review_mode=fields["Review mode"],
                      reviewed_json_sha256=fields["Reviewed JSON SHA-256"])
        if "Ready for prefill" in fields:
            result["ready_for_prefill"] = ready
        for name, key in (("Review iteration", "review_iteration"),
                          ("Open substantive defects", "open_substantive_defects"),
                          ("Unresolved checks", "unresolved_checks")):
            if name in fields:
                result[key] = int(fields[name])
        if "Review context SHA-256" in fields:
            result["review_context_sha256"] = fields["Review context SHA-256"]
        if RECORD_FIELD in fields:
            result["review_record_sha256"] = fields[RECORD_FIELD]
        if "Scoring record SHA-256" in fields:
            if not re.fullmatch(r"[a-f0-9]{64}", fields["Scoring record SHA-256"]):
                raise ValueError("Scoring record SHA-256 must be a lowercase SHA-256 fingerprint.")
            result["scoring_record_sha256"] = fields["Scoring record SHA-256"]
            if fields["Review policy"] == POLICY and not {"Gate tier", "Coverage ratio"} <= fields.keys():
                raise ValueError("A scored rubric-revision-v10 report needs Gate tier and Coverage ratio in the verdict block.")
        if "Gate tier" in fields:
            if fields["Gate tier"] not in {"catastrophic", "localized", "none"}:
                raise ValueError("Gate tier must be catastrophic, localized or none.")
            result["gate_tier"] = fields["Gate tier"]
        if "Golden verified" in fields:
            if fields["Golden verified"] not in {"Yes", "No"}:
                raise ValueError("Golden verified must be Yes or No.")
            result["golden_verified"] = fields["Golden verified"] == "Yes"
        if "Coverage ratio" in fields:
            ratio = re.fullmatch(r"(0|[1-9][0-9]*)/([1-9][0-9]*)", fields["Coverage ratio"])
            if fields["Coverage ratio"] == "N/A":
                ratio = None
            elif not ratio or int(ratio.group(1)) > int(ratio.group(2)):
                raise ValueError("Coverage ratio must be covered/required outcomes or N/A for unusable input.")
            result["coverage_ratio"] = [int(ratio.group(1)), int(ratio.group(2))] if ratio else None
        if "Repairs" in fields:
            result["repairs"] = fields["Repairs"]
    if stage == "hardness":
        difficulty = {None: "unassigned", 1: "Too easy", 2: "Easy", 3: "Hard", 4: "Hard", 5: "Really hard"}[score]
        gate = "PROCEED" if score is not None and score >= 3 else "HOLD"
        assessed_model = fields["Assessed model"]
        if assessed_model not in {"Opus", "Haiku", "Unconfirmed"} or (score is not None and assessed_model == "Unconfirmed"):
            raise ValueError("Assessed model must be Opus or Haiku for a score; Unconfirmed is allowed only for unscored reviews.")
        mode = fields["Assessment mode"]
        if mode != HARDNESS_MODES[assessed_model]:
            raise ValueError(f"{assessed_model} requires Assessment mode: {HARDNESS_MODES[assessed_model]}.")
        if assessed_model == "Haiku":
            if fields.get("Prediction basis", "").lower() in {"", "none", "null", "n/a"}:
                raise ValueError("A Haiku prediction needs Prediction basis describing its transfer evidence or unresolved gap.")
            if fields["Evidence limits"].lower() == "none":
                raise ValueError("A Haiku prediction must disclose that Opus performance was not observed.")
        elif "Prediction basis" in fields:
            raise ValueError("Prediction basis belongs only to HAIKU_TO_OPUS reports; Opus is assessed directly.")
        # A Haiku result is a prediction about Opus, not observed Opus failure.
        reasons = ({"INSUFFICIENT_EVIDENCE"} if score is None else
                   {"OBSERVED_OPUS_FAILURE" if assessed_model == "Opus" else "PREDICTED_OPUS_DIFFICULTY"}
                   if gate == "PROCEED" else {"INSUFFICIENT_DIFFICULTY"})
        difficulty_field, gate_field, reason_field, version_field = HARDNESS_FIELDS[:4]
        expected = {difficulty_field: difficulty, gate_field: gate, version_field: HARDNESS_VERSION}
        if any(fields[name] != value for name, value in expected.items()) or fields[reason_field] not in reasons:
            details = ", ".join(f"{name}: {value}" for name, value in expected.items())
            details += f", {reason_field}: " + " or ".join(sorted(reasons))
            raise ValueError(f"Hardness score {score} requires {details}.")
        result.update(difficulty=None if score is None else difficulty,
                      gate_decision=gate, gate_reason=fields[reason_field],
                      assessment_version=fields[version_field], assessed_model=assessed_model,
                      assessment_mode=mode)
        if assessed_model == "Haiku":
            result["prediction_basis"] = fields["Prediction basis"]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", required=True, choices=STAGES)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    try:
        result = parse_result(args.stage, args.report.read_text(encoding="utf-8-sig"))
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result))


if __name__ == "__main__":
    main()
