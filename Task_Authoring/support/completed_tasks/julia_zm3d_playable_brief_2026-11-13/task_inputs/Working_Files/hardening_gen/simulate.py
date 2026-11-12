#!/usr/bin/env python3
"""UNCALIBRATED what-if for the proposed rebuilds: six-run gates on the gradable surface when each designed unit is found
with a given probability, independently per run. A slot passes when every unit it depends on was found (slots with no
mechanism always pass). The find rates are counts from the seven rev1 runs (hardening_gen/out/reach.json) or, for a moved
record, the share of runs that showed the habit that would reach it; they are stated with every result, never fitted.
Writes hardening_gen/out/simulate.json and prints one line per scenario. Usage: python3 -B simulate.py [N]"""
import json, random, statistics, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; WF = HERE.parent
S = json.loads((WF / "01_Gradable_Surface.json").read_text())
SLOTS = S["slots"] if isinstance(S, dict) else S
W = {s["id"]: s["weight"] for s in SLOTS}; TOTAL = sum(W.values())
N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
def deps(slot, remap):
    return {remap.get(m, m) for m in (slot.get("mechanisms") or [])}
def run_once(p, remap, rng):
    found = {u: rng.random() < q for u, q in p.items()}
    failed = [s["id"] for s in SLOTS if not all(found[u] for u in deps(s, remap))]
    return 1 - sum(W[i] for i in failed) / TOTAL, frozenset(failed)
def patterns(fails):
    """Distinct failure patterns: two failing runs share a pattern unless they differ on two or more slots (transitive)."""
    f = [x for x in fails if x]
    groups = []
    for x in f:
        hit = [g for g in groups if any(len(x ^ y) < 2 for y in g)]
        merged = [x] + [y for g in hit for y in g]
        groups = [g for g in groups if g not in hit] + [merged]
    return len(groups), (max(map(len, groups)) / len(f) if f else 0)
def scenario(name, p, remap, rng):
    avgs, sds, ok_all, all_fail_log = [], [], 0, 0
    for _ in range(N):
        runs = [run_once(p, remap, rng) for _ in range(6)]
        sc = [r[0] for r in runs]; a = sum(sc) / 6; sd = statistics.pstdev(sc)
        n_pat, largest = patterns([r[1] for r in runs])
        full = sum(1 for r in runs if not r[1])
        gates = a < 0.70 and 0.1 <= sd <= 0.3 and full < 5 and n_pat >= 2 and largest <= 0.5
        avgs.append(a); sds.append(sd); ok_all += gates
        all_fail_log += all("X4" in r[1] for r in runs)
    q = lambda xs, k: sorted(xs)[int(k * (len(xs) - 1))]
    res = {"name": name, "p": p, "remap": remap, "runs": N,
           "avg_mean": sum(avgs) / N, "avg_p10": q(avgs, 0.1), "avg_p90": q(avgs, 0.9), "p_avg_below_70": sum(a < 0.70 for a in avgs) / N,
           "sd_mean": sum(sds) / N, "p_sd_in_band": sum(0.1 <= s <= 0.3 for s in sds) / N, "p_all_gates": ok_all / N, "p_log_rows_all_fail": all_fail_log / N}
    print(f"{name:34} avg {res['avg_mean']:.3f} [{res['avg_p10']:.3f}, {res['avg_p90']:.3f}] P(avg<70%) {res['p_avg_below_70']:.2f} "
          f"SD {res['sd_mean']:.3f} P(SD in band) {res['p_sd_in_band']:.2f} P(all gates) {res['p_all_gates']:.2f} P(log rows fail in all 6) {res['p_log_rows_all_fail']:.2f}")
    return res
rng = random.Random(20261112)
r7 = lambda k: round(k / 7, 3)
OUT = []
# rev1 as it is, with the seven runs' find rates (the check: should land near the observed 82%)
OUT.append(scenario("rev1 as measured", {"EXPORT": r7(4), "ARTHOLD": r7(6), "REVISED": 1.0, "AUDIO": r7(6), "PICKS": r7(3), "ZIP": r7(5)}, {}, rng))
# the four rebuilds: ZIP and REVISED both decided by the folder log (one unit, LOG)
LOG = {"REVISED": "LOG", "ZIP": "LOG"}
for tag, e, a, l in (("central", r7(3), 0.30, 0.20), ("finds more", r7(4), 0.43, 0.40), ("finds less", 0.30, 0.15, 0.10)):
    OUT.append(scenario(f"rebuilt, {tag}", {"EXPORT": e, "ARTHOLD": a, "LOG": l, "AUDIO": r7(6), "PICKS": r7(3)}, LOG, rng))
# three moves without the REVISED completion note: ZIP alone rides on the log, REVISED stays as measured (found by all)
for tag, e, a, l in (("central", r7(3), 0.30, 0.20), ("finds more", r7(4), 0.43, 0.40), ("finds less", 0.30, 0.15, 0.10)):
    OUT.append(scenario(f"three moves, {tag}", {"EXPORT": e, "ARTHOLD": a, "ZIP": l, "REVISED": 1.0, "AUDIO": r7(6), "PICKS": r7(3)}, {}, rng))
# one relocation only (ARTHOLD), everything else as measured
OUT.append(scenario("ARTHOLD relocation only", {"EXPORT": r7(4), "ARTHOLD": 0.30, "REVISED": 1.0, "AUDIO": r7(6), "PICKS": r7(3), "ZIP": r7(5)}, {}, rng))
(HERE / "out" / "simulate.json").write_text(json.dumps(OUT, indent=1) + "\n")
