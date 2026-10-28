#!/usr/bin/env python3
"""Exact P1 diffs for the independent verification: every file changed since the move, against its post-move content.

A baseline is accepted only when its sha256 equals the post-move fingerprint (logs/fp_11_postmove.tsv). Candidates:
  - the 11 moved tools: support/pending_edits/.rollback/<id>/pending_tools/ (copied verbatim by the move);
  - MANIFEST targets: their staged copies in support/pending_edits/ (the move copied them, sha256 verified);
  - other files: the audit sandbox copy support/audit/phase0_1/sandbox/TA/<path> (when unchanged before P1).
Files added in P1 diff against nothing. Read-only on the bundle; writes logs/verify/ only.

Usage (workspace root): python3 -B Task_Authoring/support/fix_session_2026-10-25/scripts/build_verify_diffs.py
"""
import difflib
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESSION = HERE.parent
BUNDLE = SESSION.parents[1]
OUT = SESSION / "logs" / "verify"
ROLLBACK = BUNDLE / "support" / "pending_edits" / ".rollback" / "20261025T123100Z_ao36cyhg"


def tsv(path: Path) -> dict:
    rows = {}
    for line in path.read_text().splitlines()[1:]:
        parts = line.split("\t")
        if len(parts) >= 4 and parts[1] == "file":
            rows[parts[0]] = parts[3]
    return rows


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> int:
    post = tsv(SESSION / "logs" / "fp_11_postmove.tsv")
    diff_path = Path(sys.argv[1]) if len(sys.argv) > 1 else SESSION / "logs" / "fp_diff_11_30_p1.txt"
    changed = []
    skip_prefixes = ("support/local_search/", "task_inputs/", "plans/", "support/fix_session_2026-10-25/",
                     "support/scratch/", ".rollback/")
    for line in diff_path.read_text().splitlines():
        parts = line.split("\t")
        if len(parts) >= 2 and parts[0] in ("CHANGED", "ADDED") and not parts[1].startswith(skip_prefixes) \
                and "__pycache__" not in parts[1]:
            changed.append((parts[0], parts[1]))
    staged = {e["target"]: BUNDLE / "support" / "pending_edits" / e["staged"]
              for e in json.loads((BUNDLE / "support" / "pending_edits" / "MANIFEST.json").read_text())["files"]}
    OUT.mkdir(parents=True, exist_ok=True)
    index = []
    special = {"references/mechanism_priors.json":
               "GENERATED: no archived post-move copy of this tool output; the current file is included in the bundle"}
    for kind, rel in changed:
        now = BUNDLE / rel
        if rel in special:
            index.append({"path": rel, "kind": kind, "baseline": special[rel], "diff": None,
                          "diff_lines": 0, "diff_bytes": 0, "added": 0, "removed": 0})
            continue
        base, source = None, None
        if kind == "CHANGED":
            cands = [ROLLBACK / "pending_tools" / Path(rel).name] if rel.startswith("tools/") else []
            cands += [staged[rel]] if rel in staged else []
            cands += [OUT / "baselines" / rel,
                      BUNDLE / "support" / "audit" / "phase0_1" / "sandbox" / "TA" / rel]
            for c in cands:
                if c.is_file() and sha(c) == post.get(rel):
                    base, source = c, str(c.relative_to(BUNDLE))
                    break
            if base is None:
                index.append({"path": rel, "kind": kind, "baseline": "NONE MATCHES the post-move sha256"})
                continue
        old = base.read_text().splitlines(keepends=True) if base else []
        new = now.read_text().splitlines(keepends=True)
        diff = "".join(difflib.unified_diff(old, new, f"a/{rel}", f"b/{rel}", n=3))
        name = rel.replace("/", "__") + ".diff"
        (OUT / name).write_text(diff)
        index.append({"path": rel, "kind": kind, "baseline": source or "(added in P1)", "diff": name,
                      "diff_lines": diff.count("\n"), "diff_bytes": len(diff.encode()),
                      "added": sum(1 for x in diff.splitlines() if x.startswith("+") and not x.startswith("+++")),
                      "removed": sum(1 for x in diff.splitlines() if x.startswith("-") and not x.startswith("---"))})
    (OUT / "INDEX.json").write_text(json.dumps(index, indent=1) + "\n")
    for x in index:
        print(f"{x['path']:70} {x.get('diff_bytes', '-'):>8} B  +{x.get('added', '-')} -{x.get('removed', '-')}  "
              f"base {x['baseline'][:60]}")
    return 1 if any("NONE MATCHES" in x["baseline"] for x in index) else 0


if __name__ == "__main__":
    raise SystemExit(main())
