#!/usr/bin/env python3
"""Save eval outputs or supplied task details at fixed repository-relative paths."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile

from hg_report_contract import parse_result
from hg_rubric_loop import REPORT, archive, local
import hg_golden_review as golden_review
import hg_review_score as rubric_score
import hg_prompt_checks as prompt_checks
import hg_oe_review as oe_review


REPOSITORY = Path(__file__).resolve().parents[2]
REPORTS = Path("Evals/task_inputs/reports")
OUTPUTS = {
    "injection": REPORTS / "0_injection.md",
    "prompt": REPORTS / "1_prompt.md",
    "hardness": REPORTS / "1a_hardness.md",
    "golden": REPORTS / "2_golden.md",  # Legacy compatibility only.
    "oe": oe_review.REPORT,
    "oe-review": oe_review.RECORD,
    "rubric": REPORTS / "3_rubric.md",
    "rubric-score": rubric_score.SCORE_PATH,
    "prompt-checks": prompt_checks.RECORD,
    "golden-review": golden_review.RECORD,
    "task-details": Path("Evals/task_inputs/00_Task_Assigned_Inputs.md"),
}


def save_output(kind, content, golden_unverified=False):
    if kind in {"rubric-json", "rubric-draft", "rubric-review"} or golden_unverified:
        raise ValueError("Rubric is evaluation-only. Supply the existing rubric with hg_store_input.py save rubric; save rubric-score and the rubric report. Prefill routes are retired.")
    if kind not in OUTPUTS:
        raise ValueError("Unknown output kind: " + kind)
    if kind == "task-details":
        from hg_store_input import save_input

        result = save_input(kind, content=content.encode("utf-8"))
        saved = result["files"][0]
        return {**result, **saved, "absolute_path": str(REPOSITORY / saved["path"])}
    if not content.strip():
        raise ValueError("Output is empty; supply the actual content to save.")
    result = {}
    if kind == "prompt-checks":
        result = prompt_checks.validate_record(REPOSITORY, content)
        previous = local(REPOSITORY, prompt_checks.RECORD)
        if previous.is_file() and previous.read_text() != content:
            for relative in (OUTPUTS['prompt'], prompt_checks.RECORD):
                path = local(REPOSITORY, relative)
                if path.exists():
                    saved = local(REPOSITORY, REPORTS / 'drafts/prompt_history' / (path.stem + '-' + hashlib.sha256(path.read_bytes()).hexdigest() + path.suffix))
                    saved.parent.mkdir(parents=True, exist_ok=True)
                    saved.write_bytes(path.read_bytes())
    elif kind == "oe-review":
        result = oe_review.validate_record(REPOSITORY, content)
        previous = local(REPOSITORY, oe_review.RECORD)
        if previous.is_file() and previous.read_text() != content:
            for relative in (oe_review.REPORT, oe_review.RECORD):
                path = local(REPOSITORY, relative)
                if path.exists():
                    saved = local(REPOSITORY, REPORTS / 'drafts/oe_history' / (path.stem + '-' + hashlib.sha256(path.read_bytes()).hexdigest() + path.suffix))
                    saved.parent.mkdir(parents=True, exist_ok=True)
                    path.replace(saved)
    elif kind == "rubric-score":
        result = rubric_score.validate_score(REPOSITORY, content)
        previous = local(REPOSITORY, rubric_score.SCORE_PATH)
        if previous.is_file() and previous.read_text(encoding="utf-8") != content:
            for relative in (REPORT, rubric_score.SCORE_PATH):
                archive(REPOSITORY, relative)
    elif kind == "golden-review":
        result = golden_review.validate_record(REPOSITORY, content)
        previous = local(REPOSITORY, golden_review.RECORD)
        if previous.is_file() and previous.read_text(encoding="utf-8") != content:
            for relative in (golden_review.REPORT, golden_review.RECORD):
                golden_review.archive(REPOSITORY, relative)
    else:
        result = parse_result(kind, content)
        if kind != "golden" and "evaluator_model" not in result:
            raise ValueError("Verdict block needs an Evaluator model line naming the model and effort that produced this report.")
        if kind == "rubric" and (result.get("review_mode") not in {None, "AUDIT"} or result.get("ready_for_prefill")):
            raise ValueError("Rubric is evaluation-only; CREATE and prefill reports cannot be saved.")
        if kind == "golden" and (result["verdict"] == "PASS" or "review_record_sha256" in result):
            result.update(golden_review.approve_report(REPOSITORY, result))
        if kind == "rubric" and (result.get("verdict_score") is not None or "scoring_record_sha256" in result):
            result.update(rubric_score.approve_score(REPOSITORY, result))
        if kind == "oe" and (result.get("verdict_score") is not None or "oe_record_sha256" in result):
            result.update(oe_review.approve_report(REPOSITORY, result))
        if kind == "prompt" and (result.get("verdict_score") is not None or "prompt_record_sha256" in result
                                 or prompt_checks.ugt.has_scored_ugt(content)):
            result.update(prompt_checks.approve_report(REPOSITORY, result, content))

    relative = OUTPUTS[kind]
    destination = local(REPOSITORY, relative)
    destination.parent.mkdir(parents=True, exist_ok=True)
    payload = content.encode("utf-8")
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=destination.parent, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(payload)
        os.replace(temporary, destination)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    if destination.read_bytes() != payload:
        raise OSError(f"Saved output did not match supplied content: {destination}")
    return {
        **result,
        "path": relative.as_posix(),
        "absolute_path": str(destination),
        "bytes": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=tuple(OUTPUTS))
    parser.add_argument("--source", type=Path, help="Completed UTF-8 output file; defaults to stdin.")
    args = parser.parse_args()
    try:
        content = args.source.read_text(encoding="utf-8-sig") if args.source else sys.stdin.read()
        result = save_output(args.kind, content)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
