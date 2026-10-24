#!/usr/bin/env python3
"""Read-only inventory and structural checks; never an evaluation verdict."""

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


ARTIFACTS = (
    "00_Task_Assigned_Inputs.md",
    "01_Universe_Inject.sql",
    "03_Error_Async_Config.txt",
    "04_Prompt.txt",
    "06_Human_Time.txt",
    "07_Dynamic_Context.md",
    "08_Golden_Answer.md",
    "08_Oracle_Events.md",
    "09_Rubrics.json",
    "10_Baseline_Verifier_Results.txt",
    "11_Baseline_AllFail_Justifications.txt",
    "12_Difficulty_Stats.txt",
)
BATCHES = {
    "baseline": "05_Baseline_Trajectories",
}
ASSIGNMENT = {"00_Task_Assigned_Inputs.md"}
INJECTION = {"01_Universe_Inject.sql"}
PROMPT = {"04_Prompt.txt"}
GOLDEN = PROMPT | {"08_Golden_Answer.md"}
OE = PROMPT | {"08_Oracle_Events.md"}
RUBRIC = OE | {"09_Rubrics.json"}
REQUIRED = {
    "injection": INJECTION,
    "prompt": ASSIGNMENT | PROMPT,
    "hardness": PROMPT,
    "golden": ASSIGNMENT | GOLDEN,  # Historical task-folder review.
    "oe": ASSIGNMENT | OE,
    "rubric": ASSIGNMENT | PROMPT | {"09_Rubrics.json"},
    "all": ASSIGNMENT | RUBRIC,
}
OPTIONAL = {
    "prompt": INJECTION | {"03_Error_Async_Config.txt", "07_Dynamic_Context.md"},
    "hardness": INJECTION,
    "golden": INJECTION,
    "oe": INJECTION,
    "rubric": INJECTION | {"08_Oracle_Events.md"},
}
OPTIONAL["all"] = set().union(*OPTIONAL.values())
REQUIRED_BATCHES = {}
RUBRIC_KEYS = {"title", "category", "weight", "justification", "evidence"}
RUN_NAME = re.compile(r"(?:trajectory-run-([1-9][0-9]*)|Run([1-9][0-9]*)_Trajectory)\.json$")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError(f"Non-standard JSON constant: {value}")


def read_artifact(path, template):
    entry = {"path": path.name, "status": "MISSING", "sha256": None}
    if not path.exists():
        return entry, None
    if not path.is_file():
        entry.update(status="NOT_A_FILE", detail="Expected a regular file.")
        return entry, None
    try:
        content = path.read_bytes()
        entry.update(bytes=len(content), sha256=hashlib.sha256(content).hexdigest())
        text = content.decode("utf-8-sig")
        entry["status"] = "PRESENT" if text.strip() else "EMPTY"
        if entry["status"] == "EMPTY":
            return entry, None
        if template.is_file():
            entry["matches_template"] = content == template.read_bytes()
        value = None
        if path.suffix == ".json":
            value = json.loads(text, object_pairs_hook=unique_object, parse_constant=reject_constant)
            entry["json_type"] = type(value).__name__
            if isinstance(value, (list, dict)):
                entry["json_items"] = len(value)
            if value is None or value == [] or value == {}:
                entry["status"] = "EMPTY_JSON"
        if entry.get("matches_template"):
            entry["status"] = "UNFILLED_TEMPLATE"
        return entry, value
    except (UnicodeError, ValueError) as error:
        entry.update(status="INVALID_CONTENT", detail=str(error))
    except OSError as error:
        entry.update(status="UNREADABLE", detail=str(error))
    return entry, None


def rubric_issues(value):
    if not isinstance(value, list) or not value:
        return ["Rubrics must be a non-empty JSON array."]
    findings = []
    for index, criterion in enumerate(value, start=1):
        label = f"R{index}"
        if not isinstance(criterion, dict):
            findings.append(f"{label}: expected an object.")
            continue
        if set(criterion) != RUBRIC_KEYS:
            findings.append(f"{label}: expected exactly {', '.join(sorted(RUBRIC_KEYS))}.")
        for field in ("title", "category", "justification", "evidence"):
            if not isinstance(criterion.get(field), str) or not criterion[field].strip():
                findings.append(f"{label}: {field} must be a non-blank string.")
        if criterion.get("category") not in ("Outcome", "Process"):
            findings.append(f"{label}: category must be Outcome or Process.")
        weight = criterion.get("weight")
        if type(weight) is not int or weight not in (1, 3, 5):
            findings.append(f"{label}: weight must be the integer 1, 3, or 5.")
    return findings


def inventory_batch(task, template_root, directory):
    folder = task / directory
    output = {"directory": directory, "exists": folder.is_dir(), "runs": [], "issues": []}
    if folder.exists() and not folder.is_dir():
        output["issues"].append(f"{directory}: expected a directory.")
        return output
    if not folder.is_dir():
        return output
    seen = {}
    for path in sorted(folder.glob("*.json")):
        match = RUN_NAME.fullmatch(path.name)
        run_id = int(match.group(1) or match.group(2)) if match else None
        entry, value = read_artifact(path, template_root / directory / path.name)
        entry.update(path=f"{directory}/{path.name}", run_id=run_id)
        if entry["status"] == "PRESENT" and not isinstance(value, (dict, list)):
            entry.update(status="INVALID_SHAPE", detail="Trajectory JSON must be an object or array.")
        output["runs"].append(entry)
        if run_id is None:
            output["issues"].append(f"{entry['path']}: unrecognized run filename; mapping needed.")
        elif run_id in seen:
            output["issues"].append(f"Run {run_id}: duplicate exports {seen[run_id]} and {path.name}.")
        else:
            seen[run_id] = path.name
    output["recognized_run_ids"] = sorted(seen)
    output["nonempty_json_exports"] = sum(entry["status"] == "PRESENT" for entry in output["runs"])
    output["completion_status"] = "NOT_INTERPRETED"
    return output


def build_report(repo, task, stage, trajectory=None):
    template_root = repo / "Tasks_Template"
    required = REQUIRED[stage]
    artifacts = []
    issues = []
    selected_artifacts = [name for name in ARTIFACTS if name in required | OPTIONAL.get(stage, set())]
    for name in selected_artifacts:
        entry, value = read_artifact(task / name, template_root / name)
        entry["required_for_selected_stage"] = name in required
        if name == "09_Rubrics.json" and entry["status"] == "PRESENT":
            entry["schema_issues"] = rubric_issues(value)
            if entry["schema_issues"]:
                entry["status"] = "INVALID_SCHEMA"
        artifacts.append(entry)
        if name in required and entry["status"] != "PRESENT":
            issues.append(f"{name}: {entry['status']}")
            issues.extend(entry.get("schema_issues", []))

    batches = {
        batch: inventory_batch(task, template_root, directory)
        for batch, directory in BATCHES.items()
        if batch in REQUIRED_BATCHES.get(stage, set())
        or (stage == "all" and (task / directory).exists())
    }
    for batch in REQUIRED_BATCHES.get(stage, set()):
        inventory = batches[batch]
        issues.extend(inventory["issues"])
        if not inventory.get("nonempty_json_exports", 0):
            issues.append(f"{inventory['directory']}: no non-empty trajectory JSON to inspect.")
        for entry in inventory["runs"]:
            if entry["status"] in ("INVALID_CONTENT", "INVALID_SHAPE", "UNREADABLE", "NOT_A_FILE"):
                issues.append(f"{entry['path']}: {entry['status']}")

    scope = "working-task"
    screening = None
    if stage in {"hardness", "all"}:
        saved = None
        if trajectory is None and task.resolve() == (repo / "Evals/task_inputs").resolve():
            import hg_store_input as store
            previous_root = store.REPOSITORY
            try:
                store.REPOSITORY = repo
                saved = store.inventory()["hardness_intake"]
            finally:
                store.REPOSITORY = previous_root
        selection = "EXPLICIT" if trajectory is not None else "OPUS_PRIMARY"
        selected = Path(trajectory).expanduser() if trajectory is not None else task / "opus/trajectory.json"
        if saved is not None:
            selection = "HAIKU_FALLBACK" if saved["key"] == "haiku" else "OPUS_PRIMARY"
            selected = repo / saved["path"] if saved["path"] else task / (saved["key"] or "opus") / "trajectory.json"
        # File existence determines only structural routing. Do not skip an
        # empty, malformed, unreadable or broken-link Opus candidate, and do
        # not revive a cleared/missing indexed input through file-only routing.
        if saved is None and trajectory is None and not selected.exists() and not selected.is_symlink():
            fallback = task / "haiku/trajectory.json"
            if fallback.exists() or fallback.is_symlink():
                selected, selection = fallback, "HAIKU_FALLBACK"
        selected = (selected if selected.is_absolute() else repo / selected).resolve()
        template = template_root / ("haiku/trajectory.json" if selection == "HAIKU_FALLBACK" else "opus/trajectory.json")
        if saved is not None and saved["state"] not in {"CANDIDATE", "UNINDEXED_CANDIDATE"}:
            status = {"ASK": "MISSING", "NEEDS_ATTENTION": "INPUT_INTEGRITY_ISSUE", "SOURCE_SUPPLIED": "UNMAPPED_SOURCE"}[saved["state"]]
            screening, value = {"status": status, "sha256": None, "detail": saved["next_action"]}, None
        else:
            screening, value = read_artifact(selected, template)
        screening.update(
            path=str(selected),
            selection=selection,
            saved_intake_state=saved["state"] if saved is not None else None,
            required_for_selected_stage=True,
            model_and_completion="NOT_INTERPRETED",
        )
        if screening["status"] == "PRESENT" and not isinstance(value, (dict, list)):
            screening.update(status="INVALID_SHAPE", detail="Trajectory JSON must be an object or array.")
        if screening["status"] != "PRESENT":
            issues.append(f"Hardness trajectory ({selection}): {screening['status']} ({selected})")

    if task == template_root.resolve():
        scope = "template"
    elif task.is_relative_to((repo / "QC_Tasks").resolve()):
        scope = "historical-calibration"
    return {
        "kind": "INPUT_PREFLIGHT_NOT_EVAL",
        "reviewed_at_utc": datetime.now(timezone.utc).isoformat(),
        "repository": str(repo),
        "task": str(task),
        "scope": scope,
        "stage": stage,
        "structural_input_issues": issues,
        "artifacts": artifacts,
        "batches": batches,
        "screening_trajectory": screening,
        "limitations": [
            "No SQL execution, tool calls, grounding, persona/ACL certification, semantic scoring, or run execution.",
            "PRESENT means inspectable content, not correctness, completion, or freshness.",
            "Only exact template copies are detected; edited placeholders still need human review.",
            "An empty or missing export alone does not establish why a platform run lacks evidence.",
            "Run completion, model identity, criterion mapping, exclusions and difficulty are not inferred.",
            "Injection SQL is optional except for the standalone injection audit; omission does not prove unchanged runtime state.",
            "Prompt error/async configuration and dynamic context are required only when applicable; the evaluator determines applicability.",
            "Hashes cover listed task inputs and direct trajectory JSON only, not universe state or run-time provenance.",
            "Read Evals/WORKFLOW.md for inherited persona, model and run-count conflicts.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("task", help="Task directory, absolute or relative to the repository.")
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--stage", choices=tuple(REQUIRED), default="all")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--trajectory", type=Path, help="Explicit unhinted Opus or Haiku export for hardness/all; relative to the repository.")
    args = parser.parse_args()
    if args.trajectory is not None and args.stage not in {"hardness", "all"}:
        parser.error("--trajectory is supported only with --stage hardness or all.")
    repo = args.repo.expanduser().resolve()
    task = Path(args.task).expanduser()
    task = (task if task.is_absolute() else repo / task).resolve()
    if not task.is_dir():
        parser.error(f"Task directory does not exist: {task}")
    if not all((repo / name).is_dir() for name in ("Evals", "claude")):
        parser.error(f"Not an Evals/claude workspace root: {repo}")
    try:
        report = build_report(repo, task, args.stage, args.trajectory)
    except OSError as error:
        parser.error(str(error))
    if args.format == "json":
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(f"INPUT PREFLIGHT ONLY — {task} [{args.stage}; {report['scope']}]")
        for entry in report["artifacts"]:
            required = "required" if entry["required_for_selected_stage"] else "conditional/later"
            print(f"{entry['status']:20} {entry['path']} ({required})")
        for batch, inventory in report["batches"].items():
            print(f"{batch}: run IDs {inventory.get('recognized_run_ids', [])}; completion NOT INTERPRETED")
            for entry in inventory["runs"]:
                print(f"  {entry['status']:18} {entry['path']}")
        if report["screening_trajectory"] is not None:
            screening = report["screening_trajectory"]
            print(f"Hardness run ({screening['selection']}): {screening['status']} {screening['path']}; model/completion NOT INTERPRETED")
        print("\nSelected structural input issues:")
        for issue in report["structural_input_issues"]:
            print(f"- {issue}")
        if not report["structural_input_issues"]:
            print("- None detected. This is not an evaluation PASS.")
        for limitation in report["limitations"]:
            print(f"Note: {limitation}")
    return 1 if report["structural_input_issues"] else 0


if __name__ == "__main__":
    sys.exit(main())
