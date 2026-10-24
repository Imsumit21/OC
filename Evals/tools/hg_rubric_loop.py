"""Bind rubric evaluations to saved inputs. Legacy creation entry points are retired."""

import hashlib
import json
from pathlib import Path

from hg_preflight import reject_constant, unique_object


POLICY = "rubric-revision-v10"
WORKFLOW_POLICY = "rubric-eval-only-v1"
DRAFT = Path("Evals/task_inputs/reports/drafts/5_Rubric.proposal.json")
CONTEXT = DRAFT.with_name("rubric_review_context.json")
FINAL = Path("Evals/task_inputs/5_Rubric.json")
REPORT = Path("Evals/task_inputs/reports/3_rubric.md")
REVIEW_RECORD = DRAFT.with_name("rubric_review_record.json")
HISTORY = DRAFT.parent / "rubric_history"
INPUT_KEYS = frozenset({
    "task-details", "prompt", "oe", "golden", "injection", "error-async",
    "dynamic-context", "rubric",
})
REFERENCES = (
    "Evals/3_Rubrics_Eval.md", "Evals/Authoring_Workflow.md", "Evals/WORKFLOW.md",
    "Evals/INPUTS.md", "Evals/EXECUTION.md", "Evals/ENVIRONMENT.md",
    "Evals/UNIVERSE_MAP.md", "claude/skills/rubric/SKILL.md",
    "Evals/references/rules/scoring.json", "Evals/references/rules/scoring_notes.md",
    "Evals/references/rules/long_horizon.md",
    "Evals/references/persona/roster.json", "Evals/references/persona/acl.md",
    "Evals/references/tools/catalog.json", "Evals/references/tools/manifest.json",
    "Evals/references/universe_manifest.json", "Evals/references/source_layout.json",
    "Evals/references/schema/manifest.json",
    "Evals/references/rules/rubric_review_record.md",
    "Evals/references/rules/review_scoring.md", "Evals/references/rules/qc_rubric_v10.md",
    "Evals/tools/hg_review_evidence.py", "Evals/tools/hg_rubric_acceptance.py",
    "Evals/tools/hg_rubric_qc.py", "Evals/tools/hg_review_score.py", "Evals/tools/hg_rubric_checks.py",
    "Evals/tools/hg_rubric_sampling.py", "Evals/references/rules/rubric_sampling.md",
    "Evals/tools/hg_source_checks.py", "Evals/tools/hg_eval_release.py",
    "Evals/references/rules/prompt_rubric_reliability.md",
    "Evals/tools/hg_rubric_facts.py", "Evals/tools/hg_rubric_fact_binding.py",
    "Evals/references/rules/rubric_factual_checks.md",
    "Evals/references/rules/rubric_checks.md",
    "Evals/tools/hg_rubric_assertions.py",
    "Evals/tools/hg_coherent_record.py", "Evals/references/rules/coherent_record.md",
    "Evals/tools/hg_rubric_review.py", "Evals/tools/hg_rubric_loop.py",
    "Evals/tools/hg_report_contract.py", "Evals/tools/hg_write_output.py",
)


def relevant_input(key):
    if key.removeprefix("source:") in {"baseline", "baseline-verifier", "all-fail"}:
        return False
    return key in INPUT_KEYS or key.startswith(("reference:", "source:", "extra:"))


def digest(payload):
    return hashlib.sha256(payload).hexdigest()


def local(root, relative):
    path = root / relative
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Rubric path escapes this workspace: {relative}")
    return path


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"),
                      object_pairs_hook=unique_object, parse_constant=reject_constant)


def fingerprint(path):
    if not path.exists():
        return None
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def review_context(root, *, input_filter=relevant_input, reference_paths=REFERENCES, policy=POLICY):
    # Import lazily: input saving also calls invalidate_prefill below.
    from hg_store_input import SLOTS, BATCHES, destinations

    index_path = local(root, Path("Evals/task_inputs/inputs.json"))
    index = load_json(index_path) if index_path.exists() else {"inputs": {}}
    entries = index.get("inputs")
    if not isinstance(entries, dict):
        raise ValueError("Invalid saved-input index; resolve it before rubric review.")
    states, files = {}, {}
    for key, entry in entries.items():
        if not input_filter(key):
            continue
        listed = entry.get("files", [])
        state = entry.get("state")
        if state not in {"saved", "cleared"}:
            raise ValueError(f"Invalid saved input state: {key}")
        expected = destinations(key, [f["filename"] for f in listed] or ["input.txt"])
        if (state == "cleared" and listed) or (state == "saved" and
                [f["path"] for f in listed] != [p.as_posix() for p in expected]):
            raise ValueError(f"Invalid stored input paths: {key}")
        states[key] = {k: v for k, v in entry.items() if k not in {"revision", "origin"}}
        for item in listed:
            path = local(root, Path(item["path"]))
            actual = fingerprint(path)
            if actual is None or actual != item["sha256"]:
                raise ValueError(f"Saved input changed or missing: {item['path']}; resave and review it.")
            files[item["path"]] = actual
    # Legacy canonical inputs are still fingerprinted; they cannot bypass binding.
    for key, name in {**SLOTS, **BATCHES}.items():
        if input_filter(key) and key not in entries:
            path = local(root, Path("Evals/task_inputs") / name)
            candidates = sorted(path.rglob("*")) if path.is_dir() else [path]
            for candidate in candidates:
                if candidate.is_file():
                    relative = candidate.relative_to(root).as_posix()
                    files[relative] = fingerprint(local(root, Path(relative)))
    references = {name: fingerprint(local(root, Path(name))) for name in reference_paths}
    manifest = {"review_policy": policy, "inputs": states, "files": files,
                "references": references}
    raw = json.dumps(manifest, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return {"sha256": digest(raw), "manifest": manifest}


def archive(root, relative):
    path = local(root, relative)
    if not path.exists():
        return None
    content = path.read_bytes()
    destination = HISTORY / f"{path.stem}-{digest(content)}{path.suffix}"
    saved = local(root, destination)
    saved.parent.mkdir(parents=True, exist_ok=True)
    if saved.exists():
        if saved.read_bytes() != content:
            raise ValueError("Rubric history collision; preserve files and investigate.")
        path.unlink()
    else:
        path.replace(saved)
    return destination.as_posix()


def invalidate_prefill(root):
    """Historical exports are preserved; input/context hashes invalidate old reviews."""
    return None


def prepare_draft(root, content, golden_verified=False, golden_reason=None):
    raise ValueError("Rubric is evaluation-only; draft generation is retired.")


def review_record(root, content, publication=False):
    """Validate the evidence record against saved bytes and current dependencies."""
    from hg_rubric_review import validate_record

    receipt = load_json(local(root, CONTEXT))
    draft_path = local(root, DRAFT)
    if (receipt.get("review_policy") != POLICY or
            receipt.get("reviewed_json_sha256") != fingerprint(draft_path) or
            receipt.get("review_context_sha256") != review_context(root)["sha256"]):
        raise ValueError("Stale rubric proposal/context; stage and review the current version.")
    record = json.loads(content, object_pairs_hook=unique_object, parse_constant=reject_constant)
    result = validate_record(record, load_json(draft_path), receipt, publication=publication, root=root)
    return {**result, "review_record_sha256": digest(content.encode("utf-8"))}


def approve_publication(root, content, parsed_report):
    raise ValueError("Rubric is evaluation-only; prefill publication is retired.")
