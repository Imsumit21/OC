#!/usr/bin/env python3
"""Compare recorded semantic-review judgments with held-out case expectations.

No model is invoked here. Save actual judgments before opening the expectations.
This comparator is a maintenance aid, not a task publication prerequisite.
"""

import argparse
import json
from pathlib import Path

from hg_preflight import unique_object, reject_constant


def compare(expected, actual):
    if not isinstance(expected, dict) or not expected:
        raise ValueError("Expected judgments must be a nonempty object.")
    if not isinstance(actual, list):
        raise ValueError("Actual judgments must be an array.")
    seen, failures = set(), []
    for row in actual:
        if not isinstance(row, dict) or not isinstance(row.get("id"), str):
            raise ValueError("Each actual judgment needs a case id.")
        key = row["id"]
        if key in seen:
            raise ValueError("Duplicate actual case " + key)
        seen.add(key)
        if row.get("verdict") not in {"PASS", "ISSUE", "UNRESOLVED"}:
            raise ValueError("Invalid judgment for " + key)
        if not isinstance(row.get("reason"), str) or not row["reason"].strip():
            raise ValueError("Actual judgment needs a reason: " + key)
        if key not in expected or row["verdict"] != expected[key]:
            failures.append(dict(id=key, expected=expected.get(key), actual=row["verdict"]))
    failures.extend(dict(id=key, expected=expected[key], actual="MISSING")
                    for key in sorted(set(expected) - seen))
    return dict(cases=len(expected), matches=len(expected) - sum(x["id"] in expected for x in failures),
                passed=not failures, failures=failures)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("actual", type=Path)
    parser.add_argument("--expected", type=Path,
                        default=Path(__file__).parent / "tests/fixtures/rubric_case_expectations.json")
    args = parser.parse_args()
    def read(path):
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object,
                          parse_constant=reject_constant)
    try:
        result = compare(read(args.expected)["expected"], read(args.actual))
    except (ValueError, OSError, KeyError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
