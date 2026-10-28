#!/usr/bin/env python3
"""Compact round-4 verification artifacts: the exact delta from the tree the round-3 verifier reviewed, plus the raw
acceptance outputs. The verifier cannot fetch URLs, so each artifact is a self-contained inline file (~10-30 KB).

Baselines are the pre-round-4 copies the session's own rollback folders hold (each sha256 printed in the artifact).
Usage (workspace root): python3 -B build_round4_artifacts.py
"""
import difflib
import hashlib
from pathlib import Path

B = Path(__file__).resolve().parents[3]
ROOT = B.parent
S = B / "support" / "fix_session_2026-10-25"
OUT = S / "logs" / "verify" / "round4_current" / "artifacts"
R1, R2, R3, R4 = (ROOT / ".rollback" / n for n in ("20261028T_g1", "20261028T_g2", "20261028T_g3",
                                                   "20261028T_g1"))
G4 = B / "support" / ".rollback" / "20261028T_g4"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def delta(old: Path, new: Path, label: str) -> str:
    a = old.read_text().splitlines(keepends=True)
    b = new.read_text().splitlines(keepends=True)
    d = "".join(difflib.unified_diff(a, b, f"a/{label}", f"b/{label}", n=3))
    return f"===== ROUND-4 DELTA {label} (pre-round-4 sha {sha(old)[:16]} -> now {sha(new)[:16]}) =====\n{d}"


def doc(rel: str) -> str:
    return f"===== FILE {rel} =====\n" + (B / rel).read_text()


def log(rel: str, tail: int | None = None, grep=None) -> str:
    import re
    p = S / "logs" / rel
    text = p.read_text() if p.is_file() else "(missing)"
    lines = text.splitlines()
    if grep:
        pats = [re.compile(g) for g in grep]
        lines = [x for x in lines if any(p_.search(x) for p_ in pats)]
    if tail:
        lines = lines[-tail:]
    return f"===== OUTPUT logs/{rel} =====\n" + "\n".join(lines)


HEAD = """CONTEXT
P1 remediation of Task_Authoring (stdlib-only tools that author/check HarmonyGames V3 tasks). The round-3 independent
verification failed 8 bundles; this artifact contains the ROUND-4 DELTA against the exact tree that verifier reviewed
(the pre-round-4 copies are the session's own rollback files, sha256 in each delta header) plus the raw acceptance
outputs. Rounds 1-3 reviewed the rest of the full P1 diff; nothing outside the deltas below changed in round 4 except
the new F1 acceptance files (shown in full). Hard rules: SQL is parsed, never executed; the frozen backtests
(support/backtests/season_pass/rev13|rev14) are read-only and verified by SHA256SUMS; self-tests run in a sandbox and
write no shared cache; each fix carries a planted case and a falsification undo.
"""


def summary_extract() -> str:
    import json
    d = json.loads((S / "f1_acceptance/summary.json").read_text())
    keep = {"protocol": d.get("protocol"), "gate": d.get("gate"), "statuses": d.get("statuses"),
            "overall": d.get("overall"),
            "pooled": {k: {x: v.get(x) for x in ("status", "statistic", "target", "n", "z", "se", "pass", "reason",
                                                 "per_seed")} for k, v in d.get("pooled", {}).items()},
            "seed1_f9_f5_f7": {k: d["seeds"]["1"]["assertions"][k] for k in
                               ("f5_joint", "f7_e2e", "f7_sd", "f7_shared", "f9_mechanisms", "f10_fail_closed")}}
    return "===== FILE f1_acceptance/summary.json (key fields; full file is in the bundle) =====\n" + json.dumps(
        keep, indent=1, default=str)


def write(name: str, parts: list) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    text = HEAD + "\n" + "\n\n".join(parts) + "\n"
    (OUT / name).write_text(text)
    print(f"{name:34} {len(text) // 1024:4} KB")


def main() -> int:
    g1 = [delta(R1 / "Task_Authoring/tools/surface_grader.py", B / "tools/surface_grader.py", "tools/surface_grader.py"),
          delta(R1 / "Task_Authoring/tools/gradable_surface.py", B / "tools/gradable_surface.py",
                "tools/gradable_surface.py"),
          delta(R1 / "Task_Authoring/support/fix_session_2026-10-25/scripts/falsify_g1.py",
                S / "scripts/falsify_g1.py", "scripts/falsify_g1.py"),
          log("final4/rev13_truth.txt"), log("final4/rev13_solver.txt"), log("final4/rev14_grades.txt"),
          log("final4/build_fixtures_check.txt"), log("final4/task1_surface_gradeable.txt"),
          log("g1/falsify_g1.round16.txt", grep=["R8", "G1 FALSIFICATION", "control:"]),
          log("p1_suite_round16.log", grep=["^  ok ", "^exit=", "sandbox"]),
          log("e2e/e2e_round22.log", tail=4)]
    write("A_code_g1.txt", g1)

    h1 = [delta(R2 / "Task_Authoring/tools/node_verdicts.py", B / "tools/node_verdicts.py", "tools/node_verdicts.py"),
          delta(R2 / "Task_Authoring/tools/hardness_ledger.py", B / "tools/hardness_ledger.py", "tools/hardness_ledger.py"),
          delta(R2 / "Task_Authoring/support/fix_session_2026-10-25/scripts/falsify_h1.py",
                S / "scripts/falsify_h1.py", "scripts/falsify_h1.py"),
          log("final4/c05.txt"), log("h1/falsify_h1.round39.txt"),
          log("final4/v1_acceptance.txt", tail=3),
          log("p1_suite_round16.log", grep=["^  ok ", "^exit="])]
    write("A_code_h1.txt", h1)

    f1 = [delta(R3 / "Task_Authoring/tools/hardness_forecast.py", B / "tools/hardness_forecast.py",
                "tools/hardness_forecast.py"),
          doc("support/fix_session_2026-10-25/scripts/f1_protocol.py"),
          summary_extract(),
          log("f1/f1_protocol4_summary.txt"),
          log("e2e/e2e_round22.log", grep=["hardness_forecast"]),
          log("p1_suite_round16.log", grep=["hardness_forecast", "^exit="])]
    write("A_code_f1.txt", f1)

    misc = [delta(R1 / "Task_Authoring/tools/gradable_surface.py", B / "tools/gradable_surface.py",
                  "tools/gradable_surface.py"),
            log("final4/v1_acceptance.txt"), log("final4/task1_surface_gradeable.txt"),
            log("final4/rev14_grades.txt"), log("final4/build_fixtures_check.txt"),
            log("p1_suite_round16.log", grep=["^  ok ", "^exit="]), log("e2e/e2e_round22.log", tail=16)]
    write("A_code_misc.txt", misc)

    write("A_redteam_grading.txt", g1 + [log("g1/falsify_g1.round16.txt", tail=6)])
    write("A_redteam_attribution.txt", h1 + [log("h1/falsify_h1.round39.txt")])
    write("A_redteam_forecast.txt", f1 + [doc("support/fix_session_2026-10-25/f1_acceptance/F1_PROVENANCE_AUDIT.txt")])

    meth = [doc("support/fix_session_2026-10-25/f1_acceptance/F1_STATUS.md"),
            doc("support/fix_session_2026-10-25/f1_acceptance/F1_PROTOCOL_MANIFEST.json"),
            doc("support/fix_session_2026-10-25/f1_acceptance/F1_ACCEPTANCE_AMENDMENT.md"),
            doc("support/fix_session_2026-10-25/logs/verify/claims_methodology.md"),
            doc("support/fix_session_2026-10-25/scripts/f1_protocol.py"),
            summary_extract(),
            log("f1/f1_protocol4_summary.txt"), log("f1/protocol4_seed1.out", tail=22),
            log("p1_suite_round16.log", grep=["^  ok ", "^exit="])]
    write("A_methodology.txt", meth)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
