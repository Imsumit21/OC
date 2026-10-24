#!/usr/bin/env python3
"""Report whether the saved injection SQL has a current /injection review.

/prompt runs this before Phase 1. It compares the hash of the saved SQL with
the hash the last /injection review recorded in input_manifest.json and prints
one JSON object. It never runs SQL and never writes files.

States:
  NOT_USED        the user chose no injection; nothing to gate
  ASK             the injection question is unanswered; follow INPUTS.md
  CURRENT         the saved SQL is the one /injection last reviewed
  STALE           /injection reviewed a different SQL version
  NEVER_REVIEWED  no /injection review is recorded for this task
  NEEDS_ATTENTION the saved SQL is empty, changed or missing
"""
import hashlib
import json
from pathlib import Path
import re
import sys

import hg_store_input as store

MANIFEST = store.INPUTS / "reports/input_manifest.json"
REPORT = store.INPUTS / "reports/0_injection.md"
VERDICT = re.compile(r"^#{2,3}\s*FINAL VERDICT:\s*\**\s*(PASS|NON-FAIL|FAIL)\b", re.M)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reviewed_injection():
    """The SQL hash and review details recorded by the last /injection run."""
    path = store.local_path(MANIFEST)
    if not path.is_file():
        return None
    try:
        stage = json.loads(path.read_text(encoding="utf-8")).get("stages", {}).get("injection")
    except (OSError, ValueError):
        return None
    if not isinstance(stage, dict):
        return None
    sql = stage.get("inputs", {}).get("injection", {})
    if not sql.get("sha256"):
        return None
    return {"sha256": sql["sha256"], "review_version": stage.get("review_version"),
            "reviewed_at": stage.get("reviewed_at")}


def report_verdict():
    path = store.local_path(REPORT)
    if not path.is_file():
        return None
    found = VERDICT.findall(path.read_text(encoding="utf-8", errors="replace"))
    return found[-1] if found else None


def gate():
    intake = store.inventory()["injection_intake"]
    if intake["state"] == "NOT_USED":
        return {"state": "NOT_USED", "next_action": "No overlay; continue to Phase 1."}
    if intake["state"] == "ASK":
        return {"state": "ASK", "next_action": intake["next_action"]}
    sql = store.local_path(store.INPUTS / store.SLOTS["injection"])
    if intake["state"] == "NEEDS_ATTENTION" or not sql.is_file() or sql.stat().st_size == 0:
        return {"state": "NEEDS_ATTENTION",
                "next_action": "Resolve the empty, changed or missing saved SQL before grading."}
    current = sha256(sql)
    reviewed = reviewed_injection()
    result = {"current_sha256": current}
    if reviewed is None:
        result.update(state="NEVER_REVIEWED", next_action=(
            "Run Eval 0 on the saved SQL before Phase 1 and put its result in the report's "
            "Injection Gate section."))
        return result
    result.update(reviewed=reviewed, injection_verdict=report_verdict())
    if reviewed["sha256"] != current:
        result.update(state="STALE", next_action=(
            "The SQL changed since the last /injection review. Run Eval 0 on the saved SQL "
            "before Phase 1 and put its result in the report's Injection Gate section."))
        return result
    result.update(state="CURRENT", next_action=(
        "Reuse the /injection result; cite its verdict in the Injection Gate section."))
    return result


def main():
    try:
        print(json.dumps(gate(), ensure_ascii=False))
    except (OSError, ValueError) as error:
        print(json.dumps({"state": "ERROR", "error": str(error)}))
        sys.exit(1)


if __name__ == "__main__":
    main()
