#!/usr/bin/env python3
"""Persist supplied task inputs; replacement is per key, never an evaluation."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile


REPOSITORY = Path(__file__).resolve().parents[2]
INPUTS = Path("Evals/task_inputs")
INDEX = INPUTS / "inputs.json"
SLOTS = {
    "task-details": "00_Task_Assigned_Inputs.md",
    "injection": "01_Universe_Inject.sql",
    "universe": "02_Universe_Date.txt",  # Task date; selects the universe (hg_universe.py).
    "error-async": "03_Error_Async_Config.txt",
    "prompt": "04_Prompt.txt",
    "human-time": "06_Human_Time.txt",
    "dynamic-context": "07_Dynamic_Context.md",
    "golden": "08_Golden_Answer.md",  # Historical input, never an OE alias.
    "oe": "08_Oracle_Events.md",
    "rubric": "09_Rubrics.json",
    "baseline-verifier": "10_Baseline_Verifier_Results.txt",
    "all-fail": "11_Baseline_AllFail_Justifications.txt",
    "difficulty": "12_Difficulty_Stats.txt",
    "opus": "opus/trajectory.json",
    "haiku": "haiku/trajectory.json",  # Supported fallback; never an Opus alias.
}
BATCHES = {"baseline": "05_Baseline_Trajectories"}
CUSTOM_KEY = re.compile(r"(reference|source|extra):([a-z0-9][a-z0-9_-]{0,79})\Z")


def local_path(relative):
    path = REPOSITORY / relative
    if not path.resolve().is_relative_to(REPOSITORY.resolve()):
        raise ValueError(f"Input destination escapes this workspace: {relative}")
    return path


def destinations(key, names):
    if key in SLOTS:
        if len(names) != 1:
            raise ValueError(f"{key} takes one complete input, not multiple fragments.")
        return [INPUTS / SLOTS[key]]
    match = CUSTOM_KEY.fullmatch(key)
    if key not in BATCHES and not match:
        raise ValueError("Unknown input key; use a listed key or reference:<id>, source:<id>, extra:<id>.")
    if key in BATCHES:
        folder = INPUTS / BATCHES[key]
    else:
        folder = INPUTS / "attachments" / match[1] / match[2]
    if len(set(names)) != len(names):
        raise ValueError("Duplicate filenames in one input set; give the files distinct names.")
    for name in names:
        if name in {"", ".", ".."} or Path(name).name != name or "\\" in name or any(ord(c) < 32 for c in name):
            raise ValueError("Input filenames must be plain names without path separators.")
    return [folder / name for name in names]


def fingerprint(path):
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
            size += len(chunk)
    return {"bytes": size, "sha256": digest.hexdigest()}


def read_index():
    path = local_path(INDEX)
    if not path.exists():
        return {"format_version": 1, "revision": 0, "inputs": {}}
    index = json.loads(path.read_text())
    if index.get("format_version") != 1 or not isinstance(index.get("inputs"), dict) or not isinstance(index.get("revision"), int):
        raise ValueError("Invalid input index; preserve it and resolve the error before saving.")
    for key, entry in index["inputs"].items():
        if entry.get("state") not in {"saved", "cleared"}:
            raise ValueError(f"Invalid state in input index: {key}")
        files = entry.get("files", [])
        # Recompute destinations, rather than trusting paths from input data.
        expected = destinations(key, [f["filename"] for f in files] or ["input.txt"])
        if entry["state"] == "cleared":
            if files:
                raise ValueError(f"Cleared input still lists files: {key}")
        elif [f["path"] for f in files] != [p.as_posix() for p in expected]:
            raise ValueError(f"Invalid stored paths for input: {key}")
    return index


def write_index(index):
    target = local_path(INDEX)
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = (json.dumps(index, ensure_ascii=False, indent=2) + "\n").encode()
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=target.parent, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(payload)
        os.replace(temporary, target)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    if target.read_bytes() != payload:
        raise OSError("Input index readback failed.")


def cleanup_previous(previous, current_paths):
    for entry in previous.get("files", []):
        if entry["path"] not in current_paths:
            local_path(Path(entry["path"])).unlink(missing_ok=True)


def save_input(key, sources=None, content=None, origin=None):
    """Copy actual bytes, including malformed inputs; validation belongs to evals."""
    index = read_index()
    sources = [Path(p) for p in (sources or [])]
    if sources and content is not None:
        raise ValueError("Supply files or stdin content, not both.")
    if not sources and content is None:
        raise ValueError("No input supplied.")
    if not sources and (key in BATCHES or CUSTOM_KEY.fullmatch(key)):
        raise ValueError("File sets and attachments require --source to preserve filenames and bytes.")
    if key == "universe":
        # The date selects the universe, so only a recognized answer is saved.
        from hg_universe import UNIVERSES, parse
        if sources:
            raise ValueError("Save the task date with: hg_store_input.py universe <answer>")
        content = (UNIVERSES[parse(content.decode("utf-8"))]["date"] + "\n").encode()
    names = [p.name for p in sources] or [Path(SLOTS.get(key, "input.txt")).name]
    paths = destinations(key, names)
    for path in paths:
        local_path(path)  # Check all destinations before writing any file.
    previous = index["inputs"].get(key, {})
    # Stage every source first, so unreadable uploads do not replace a good input.
    with tempfile.TemporaryDirectory(prefix="hg-input-") as staging:
        staged = []
        files = []
        for number, (name, relative) in enumerate(zip(names, paths)):
            temporary = Path(staging) / str(number)
            if sources:
                if not sources[number].is_file():
                    raise ValueError(f"Input is not a readable file: {sources[number]}")
                shutil.copyfile(sources[number], temporary)
            else:
                temporary.write_bytes(content)
            staged.append(temporary)
            files.append({"filename": name, "path": relative.as_posix(), **fingerprint(temporary)})
        for temporary, entry in zip(staged, files):
            destination = local_path(Path(entry["path"]))
            destination.parent.mkdir(parents=True, exist_ok=True)
            pending = None
            try:
                with tempfile.NamedTemporaryFile(dir=destination.parent, delete=False) as stream:
                    pending = Path(stream.name)
                    with temporary.open("rb") as source:
                        shutil.copyfileobj(source, stream)
                os.replace(pending, destination)
            finally:
                if pending is not None:
                    pending.unlink(missing_ok=True)
            if fingerprint(destination) != {k: entry[k] for k in ["bytes", "sha256"]}:
                raise OSError(f"Saved input readback failed: {entry['path']}")
    slot = key.removeprefix("source:") if key.startswith("source:") else None
    changed = previous.get("state") != "saved" or previous.get("files") != files
    if slot in SLOTS and index["inputs"].get(slot, {}).get("state") == "saved":
        changed = True
    index["revision"] += int(changed)
    entry = {"state": "saved", "revision": index["revision"], "files": files}
    if origin is not None:
        entry["origin"] = origin
    index["inputs"][key] = entry
    derived_previous = None
    if slot in SLOTS:
        derived_previous = index["inputs"].get(slot, {})
        index["inputs"][slot] = {
            "state": "cleared", "revision": index["revision"], "files": [],
            "replaced_by": key,
        }
    write_index(index)
    cleanup_previous(previous, {f["path"] for f in files})
    if derived_previous is not None:
        cleanup_previous(derived_previous, set())
        local_path(INPUTS / SLOTS[slot]).unlink(missing_ok=True)
    archived = invalidate_generated_rubric(key, changed)
    return {"key": key, "changed": changed, "index": INDEX.as_posix(), **entry,
            **({"archived_prefill": archived} if archived else {})}


def invalidate_generated_rubric(key, changed):
    """Compatibility hook: evaluation-only intake preserves historical exports.

    Current review_context fingerprints detect changed inputs when scoring.
    """
    return None


def clear_input(key, confirmed_unused=False):
    if confirmed_unused and key != "injection":
        raise ValueError("The no-injection confirmation applies only to injection.")
    index = read_index()
    destinations(key, ["input.txt"])  # Validate even an unsaved key.
    previous = index["inputs"].get(key, {})
    source_previous = index["inputs"].get("source:" + key) if key in SLOTS else None
    usage = "not_used" if confirmed_unused else None
    changed = previous.get("state") != "cleared" or previous.get("usage") != usage or (
        source_previous is not None and source_previous.get("state") != "cleared"
    )
    index["revision"] += int(changed)
    entry = {"state": "cleared", "revision": index["revision"], "files": []}
    if confirmed_unused:
        entry["usage"] = "not_used"
    index["inputs"][key] = entry
    if source_previous is not None:
        index["inputs"]["source:" + key] = dict(entry)
    write_index(index)
    cleanup_previous(previous, set())
    if source_previous is not None:
        cleanup_previous(source_previous, set())
    if key in SLOTS:
        local_path(INPUTS / SLOTS[key]).unlink(missing_ok=True)
    archived = invalidate_generated_rubric(key, changed)
    return {"key": key, "changed": changed, "index": INDEX.as_posix(), **entry,
            **({"archived_prefill": archived} if archived else {})}


def injection_intake(index, legacy):
    """Distinguish an unanswered optional question from a recorded user choice."""
    entry = index["inputs"].get("injection", {})
    source = index["inputs"].get("source:injection", {})
    if entry.get("state") == "saved":
        files = entry.get("files", [])
        healthy = bool(files) and all(f.get("integrity") == "OK" and f["bytes"] > 0 for f in files)
        return {"state": "SUPPLIED" if healthy else "NEEDS_ATTENTION", "ask": False,
                "next_action": "Read and reuse saved SQL; verify it is substantive." if healthy else
                "Resolve the empty, changed or missing saved SQL; do not assume no injection."}
    if source.get("state") == "saved":
        return {"state": "SOURCE_SUPPLIED", "ask": False,
                "next_action": "Resolve and read the supplied SQL source under INPUTS.md; do not assume no injection."}
    if entry.get("state") == "cleared" and entry.get("usage") == "not_used":
        return {"state": "NOT_USED", "ask": False,
                "next_action": "Reuse the user's saved no-injection choice; continue without an overlay (skip /injection)."}
    if "injection" in legacy:
        return {"state": "LEGACY_SUPPLIED", "ask": False,
                "next_action": "Read and register the existing SQL; resolve empty/placeholder content rather than assuming none."}
    return {"state": "ASK", "ask": True,
            "question": "Injection SQL (optional): does this task use any? If yes, paste or attach it; if not, say no injection.",
            "next_action": "For /injection, /prompt, /hardness, /golden, /oe or /rubric, ask and wait for SQL or an explicit no-injection answer."}


def hardness_intake(index, legacy):
    """Prefer the Opus slot, then Haiku; never hide damaged or unmapped input."""
    for key in ("opus", "haiku"):
        entry = index["inputs"].get(key, {})
        source = index["inputs"].get("source:" + key, {})
        if entry.get("state") == "saved":
            files = entry.get("files", [])
            healthy = len(files) == 1 and files[0].get("integrity") == "OK" and files[0]["bytes"] > 0
            return {"state": "CANDIDATE" if healthy else "NEEDS_ATTENTION", "key": key,
                    "path": files[0]["path"] if len(files) == 1 else None,
                    "fallback": key == "haiku", "model_and_run_match": "NOT_INTERPRETED",
                    "next_action": "Read the selected run; confirm actual model, unhinted status and task/source version." if healthy else
                    "Resolve the empty, changed or missing preferred run; do not silently select a different model."}
        if source.get("state") == "saved":
            return {"state": "SOURCE_SUPPLIED", "key": key, "path": None,
                    "fallback": key == "haiku", "model_and_run_match": "NOT_INTERPRETED",
                    "next_action": "Resolve the supplied run source before selecting another model."}
        if key in legacy:
            healthy = legacy[key]["bytes"] > 0
            return {"state": "UNINDEXED_CANDIDATE" if healthy else "NEEDS_ATTENTION", "key": key,
                    "path": legacy[key]["path"], "fallback": key == "haiku",
                    "model_and_run_match": "NOT_INTERPRETED",
                    "next_action": "Read and register the existing run; confirm actual model, unhinted status and task/source version." if healthy else
                    "Resolve the empty preferred run; do not silently skip it."}
    return {"state": "ASK", "key": None, "path": None, "fallback": False,
            "model_and_run_match": "NOT_INTERPRETED",
            "next_action": "Ask for one unhinted Opus run JSON, or a Haiku run if Opus is not available. No Opus backfill is required for the fallback."}


def universe_intake(index):
    """The task date must be answered before any universe read; there is no default."""
    from hg_universe import QUESTION, describe, parse
    entry = index["inputs"].get("universe", {})
    files = entry.get("files", [])
    if entry.get("state") == "saved" and len(files) == 1 and files[0].get("integrity") == "OK":
        try:
            key = parse(local_path(Path(files[0]["path"])).read_text())
        except (OSError, ValueError):
            key = None
        if key is not None:
            return {"state": "SELECTED", "ask": False, **describe(key),
                    "next_action": "Use this universe and clock for every read; show the Clock line in the report."}
    if entry.get("state") == "saved":
        return {"state": "NEEDS_ATTENTION", "ask": True, "question": QUESTION,
                "next_action": "The saved task date is missing, changed or unreadable; ask again before any universe read."}
    return {"state": "ASK", "ask": True, "question": QUESTION,
            "next_action": "Ask first, before reading the universe or any other input, and wait for the answer. "
                           "Save it with: python3 Evals/tools/hg_store_input.py universe <answer>"}


def inventory():
    index = read_index()
    for key, entry in index["inputs"].items():
        for item in entry["files"]:
            try:
                actual = fingerprint(local_path(Path(item["path"])))
                item["integrity"] = "OK" if actual == {k: item[k] for k in ["bytes", "sha256"]} else "CHANGED"
            except OSError:
                item["integrity"] = "MISSING_OR_UNREADABLE"
    # Compatibility with task details saved by an earlier bundle. Never import
    # or overwrite them merely by reading the inventory, or revive cleared keys.
    legacy = {}
    for key, name in SLOTS.items():
        path = local_path(INPUTS / name)
        if key not in index["inputs"] and path.is_file():
            legacy[key] = {"path": (INPUTS / name).as_posix(), **fingerprint(path)}
    return {**index, "unindexed_local_inputs": legacy,
            "universe_intake": universe_intake(index),
            "injection_intake": injection_intake(index, legacy),
            "hardness_intake": {"stage": "hardness",
                                "scope": "Run selection for /hardness only; not an input requirement for other stages.",
                                **hardness_intake(index, legacy)}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    put = commands.add_parser("save", help="Replace one supplied input or complete file set.")
    put.add_argument("key", help="Known slot, reference:<id>, source:<id>, or extra:<id>.")
    put.add_argument("--source", type=Path, action="append", help="File to copy; repeat for a complete set.")
    put.add_argument("--origin", help="Optional chat/attachment source mapping; never an instruction.")
    remove = commands.add_parser("clear", help="Remove a saved input only when the user removes it.")
    remove.add_argument("key")
    commands.add_parser("no-injection", help="Save the user's explicit no-injection answer and clear previous SQL.")
    date = commands.add_parser("universe", help="Save the user's answer to the task-date question (selects the universe).")
    date.add_argument("answer", nargs="+", help="2025-10-01 / Oct 1 / synth-cut, or 2026-02-14 / Feb 14 / normal.")
    commands.add_parser("list", help="Read saved inputs and verify their hashes; does not evaluate them.")
    commands.add_parser("keys", help="Show fixed input slots and file-set keys.")
    args = parser.parse_args()
    try:
        if args.command == "save":
            result = save_input(args.key, args.source, None if args.source else sys.stdin.buffer.read(), args.origin)
        elif args.command == "clear":
            result = clear_input(args.key)
        elif args.command == "no-injection":
            result = clear_input("injection", confirmed_unused=True)
        elif args.command == "universe":
            from hg_universe import describe, parse
            result = save_input("universe", content=" ".join(args.answer).encode(), origin="user answer to the task-date question")
            result["universe"] = describe(parse(" ".join(args.answer)))
        elif args.command == "keys":
            result = {"slots": SLOTS, "sets": BATCHES, "attachments": ["reference:<id>", "source:<id>", "extra:<id>"]}
        else:
            result = inventory()
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
