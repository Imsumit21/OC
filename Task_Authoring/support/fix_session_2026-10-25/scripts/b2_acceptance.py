#!/usr/bin/env python3
"""B2 acceptance: bind every Season Pass run (7 revision-13, 5 revision-14; frozen copies, read-only) under several
candidate sets with the pending trajectory_ledger.binding, and print verdict, bound revision and evidence counts.

  A  [rev14]                          a rev13 run must be INSUFFICIENT or UNBOUND, never BOUND
  B  [rev14, rev13]                   a rev13 run is never BOUND to rev14; a rev14 run BOUND to rev14
  C  every stored revision (10-14)    each run BOUND to its own revision, or INSUFFICIENT
  D  [own revision] + sole_revision   the content check still runs: BOUND (sole revision) on hits
Usage: python3 -B b2_acceptance.py [--json OUT]
"""
import json
import sys
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(BUNDLE / "support" / "pending_tools"))
import trajectory_ledger as tl  # noqa: E402

S = BUNDLE / "support" / "backtests" / "season_pass"
SQL = {"rev14": S / "rev14/sql/01_Universe_Inject.comment-free.sql",
       "rev13": S / "rev13/sql/01_Universe_Inject.comment-free.sql",
       "rev12": S / "rev13/working_files/injection_fix_20261024/before/01_Universe_Inject.comment-free.sql",
       "rev11": S / "rev13/working_files/hardening_rev12/before/01_Universe_Inject.comment-free.sql",
       "rev10": S / "rev13/working_files/hardening_rev11/before/01_Universe_Inject.comment-free.sql"}
RUNS = [("rev13", "precheck", S / "rev13/runs/06_PreCheck_Trajectory/trajectory-run-1.json")] + \
       [("rev13", f"run-{i}", S / f"rev13/runs/07_Baseline_Trajectories/trajectory-run-{i}.json") for i in range(1, 7)] + \
       [("rev14", "precheck", S / "rev14/runs/06_PreCheck_Trajectory/trajectory-run-1.json")] + \
       [("rev14", f"run-{i}", S / f"rev14/runs/07_Baseline_Trajectories/trajectory-run-{i}.json") for i in (1, 2, 3, 6)]


def main(argv):
    text = {k: p.read_text() for k, p in SQL.items()}
    sets = {"A": ["rev14"], "B": ["rev14", "rev13"], "C": ["rev14", "rev13", "rev12", "rev11", "rev10"]}
    rows, ok = [], True
    for rev, lab, path in RUNS:
        run = tl.load(path, lab)
        row = {"revision": rev, "run": lab}
        for name, cands in sets.items():
            b = tl.binding(run, [(c, text[c]) for c in cands])
            row[name] = {"verdict": b["verdict"], "bound_to": b["bound_to"], "evidence": b["evidence"],
                         "per_candidate": {c["labels"][0]: [c["discriminating_seen"], c["shared_seen"]]
                                           for c in b["candidates"]}}
        b = tl.binding(run, [(rev, text[rev])], sole_revision="frozen fixture: its own revision only")
        row["D"] = {"verdict": b["verdict"], "bound_to": b["bound_to"], "evidence": b["evidence"]}
        a_, b_, c_ = row["A"], row["B"], row["C"]
        if rev == "rev13":
            good = (a_["verdict"] in ("INSUFFICIENT", "UNBOUND") and b_["bound_to"] != ["rev14"]
                    and c_["bound_to"] != ["rev14"])
        else:
            good = (a_["verdict"] == "INSUFFICIENT" and b_["bound_to"] == ["rev14"] and c_["bound_to"] == ["rev14"])
        good = good and row["D"]["verdict"] in ("BOUND", "UNBOUND")
        ok = ok and good
        rows.append(row)
        print(f"{'ok  ' if good else 'FAIL'} {rev} {lab:9} A[rev14]={a_['verdict']:12} "
              f"B[rev14,rev13]={b_['verdict']}:{b_['bound_to']} {b_['per_candidate']}  "
              f"C[10-14]={c_['verdict']}:{c_['bound_to']} disc={c_['evidence']['discriminating_seen']}  "
              f"D[{rev}+sole]={row['D']['verdict']} hits={row['D']['evidence']['sole_revision_hits']}", flush=True)
    if "--json" in argv:
        Path(argv[argv.index("--json") + 1]).write_text(json.dumps(rows, indent=1) + "\n")
    print("B2 ACCEPTANCE " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
