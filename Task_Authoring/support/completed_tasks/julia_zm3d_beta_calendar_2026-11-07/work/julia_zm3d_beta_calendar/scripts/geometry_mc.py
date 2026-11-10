#!/usr/bin/env python3
"""Pre-scenario geometry model (UNCALIBRATED, advisory) for the Julia Lawson task (task_inputsS).

Adapted from task_inputsH/Working_Files/research/geometry_mc.py (read-only copy of its logic). Scores whole policies
and single misses on the *planned* gradable surface in a sketch JSON, then simulates six-run baselines and grades each
simulated baseline with the bundle's own gate math (Task_Authoring/tools/difficulty_stats._gates) at the assigned mode
(medium: average weighted pass rate strictly below 85 %) and the long-horizon tier. Every landing rate is an
assumption: the Opus 5.5 ledger holds almost no records for the mechanisms used (see the analysis §7.4), so the rates
are design targets that /create-scenario replaces with hardness_forecast.py on the real surface.

Sketch format: {"channels": {CH: {"miss": p, "members": [..optional sub-ids..], "rho": r}},
                "slots": [[slot_id, weight, flip]], "policies": {name: [missed ids]}}
flip = null (ordinary row, fails only at a slip rate) | "CH" | "any:CH1,CH2" | "all:CH1,CH2".

Run:  python3 -B Task_Authoring/task_inputsS/Working_Files/research/scripts/geometry_mc.py --sketch <json>
      [--draws 20000] [--seed 7] [--mode medium] [--scales 1.0,0.75,0.6,0.5,0.35]
Read-only; imports difficulty_stats without writing bytecode.
"""
from __future__ import annotations

import argparse
import json
import random
import statistics
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "Task_Authoring" / "tools"))
import difficulty_stats as ds  # noqa: E402  (gate math has one owner)

SLIP = {1: 0.03, 3: 0.06, 5: 0.06}
THOROUGHNESS = 0.5  # per-run latent loading: a thorough run catches more traps (positive correlation)
GATES = ("avg_weighted_pass_rate", "pass_at_1", "per_rollout_sd", "failure_patterns")
CAP = {"easy": 0.90, "medium": 0.85, "hard": 0.70}


def load(path: Path):
    g = json.loads(path.read_text())
    return g["channels"], [tuple(s) for s in g["slots"]], g.get("policies", {})


def hit(flip, missed):
    if flip is None:
        return False
    if flip.startswith("any:"):
        return any(x in missed for x in flip[4:].split(","))
    if flip.startswith("all:"):
        return all(x in missed for x in flip[4:].split(","))
    return flip in missed


def score(slots, missed):
    total = sum(w for _, w, _ in slots)
    return 1 - sum(w for _, w, f in slots if hit(f, missed)) / total


def expand(channels, ids):
    out = set()
    for c in ids:
        out |= set(channels[c].get("members") or [c]) if c in channels else {c}
    return out


def draw_missed(rng, channels, scale):
    nd = statistics.NormalDist()
    theta = rng.gauss(0, 1)
    missed = set()
    for c, spec in channels.items():
        p = min(0.97, spec["miss"] * scale)
        p_run = nd.cdf(nd.inv_cdf(min(max(p, 1e-9), 1 - 1e-9)) - THOROUGHNESS * theta)
        members = spec.get("members")
        if members:
            shared = rng.random() < p_run
            for m in members:
                own = rng.random() < p_run
                if shared if rng.random() < spec.get("rho", 0.0) else own:
                    missed.add(m)
        elif rng.random() < p_run:
            missed.add(c)
    return missed


def simulate(channels, slots, draws, seed, scale, mode):
    rng = random.Random(seed)
    rubrics = [{"id": s, "weight": w} for s, w, _ in slots]
    avg, sds, pats, ok_all, full = [], [], [], 0, 0
    gate_ok = {g: 0 for g in GATES}
    allfail = {s: 0 for s, _, _ in slots}
    for _ in range(draws):
        runs = []
        for i in range(1, 7):
            missed = draw_missed(rng, channels, scale)
            res = {}
            for sid, w, f in slots:
                res[sid] = (rng.random() >= SLIP[w]) if f is None else not hit(f, missed)
            runs.append({"id": f"R{i}", "status": "completed", "tool_calls": 300, "results": res})
        out = ds._gates(runs, [], 6, rubrics, "long-horizon", mode)
        rates = [r["weighted_pass_rate"] for r in out["per_rollout"]]
        avg.append(sum(rates) / 6)
        sds.append(statistics.pstdev(rates))
        pats.append(len(out["patterns"]))
        full += len(out["golden_runs"])
        ok = True
        for g in GATES:
            p = out["gates"][g]["verdict"] == "PASS"
            gate_ok[g] += p
            ok &= p
        ok_all += ok
        for s in out["all_fail_rubrics"]:
            allfail[s] += 1
    a = sorted(avg)
    return {
        "scale": scale, "E_avg": statistics.mean(a), "p10": a[int(0.1 * draws)], "p90": a[int(0.9 * draws)],
        "E_sd": statistics.mean(sds), "P_gate": {g: v / draws for g, v in gate_ok.items()},
        "P_all": ok_all / draws, "E_full": full / draws, "E_patterns": statistics.mean(pats),
        "allfail": {s: round(v / draws, 3) for s, v in allfail.items() if v / draws >= 0.01},
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sketch", required=True)
    ap.add_argument("--draws", type=int, default=20000)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--mode", default="medium", choices=sorted(CAP))
    ap.add_argument("--scales", default="1.0,0.75,0.6,0.5,0.35")
    a = ap.parse_args()
    channels, slots, policies = load(Path(a.sketch))
    cap = CAP[a.mode]
    total = sum(w for _, w, _ in slots)
    print(f"PLANNED SURFACE (pre-scenario sketch, UNCALIBRATED; mode {a.mode}, cap < {cap:.0%})")
    print(f"  slots {len(slots)}  total weight {total}  weight-5 slots {sum(1 for _, w, _ in slots if w == 5)}")
    share = {}
    for _, w, f in slots:
        key = f or "ordinary"
        share[key] = share.get(key, 0) + w
    print("  weight by flip:", {k: f"{v}/{total}={v / total:.0%}" for k, v in sorted(share.items())})
    print("\nWHOLE POLICIES (deterministic, no slips)")
    for name, ids in policies.items():
        print(f"  {score(slots, expand(channels, ids)):6.1%}  {name}")
    print("\nSINGLE MISSES (everything else right)")
    for c, spec in channels.items():
        tag = f" (all {len(spec['members'])} members)" if spec.get("members") else ""
        print(f"  {score(slots, expand(channels, [c])):6.1%}  miss {c}{tag}")
        for m in spec.get("members") or []:
            print(f"  {score(slots, {m}):6.1%}    miss member {m} only")
    print(f"\nSIX-RUN BASELINES ({a.draws} draws per scale; gate math = difficulty_stats._gates, {a.mode}, long-horizon)")
    print("  scale = multiplier on every design miss rate (1.0 = design rates; <1 = a stronger Opus)")
    for scale in [float(x) for x in a.scales.split(",")]:
        r = simulate(channels, slots, a.draws, a.seed, scale, a.mode)
        g = r["P_gate"]
        print(f"  scale {scale:4.2f}: E[avg] {r['E_avg']:.1%} (p10-p90 {r['p10']:.1%}-{r['p90']:.1%})  E[SD] {r['E_sd']:.3f}"
              f"  P(avg<{cap:.0%}) {g['avg_weighted_pass_rate']:.2f}  P(<5 full) {g['pass_at_1']:.2f}"
              f"  P(SD band) {g['per_rollout_sd']:.2f}  P(patterns) {g['failure_patterns']:.2f}"
              f"  P(all four) {r['P_all']:.2f}  E[full passes] {r['E_full']:.2f}")
        if r["allfail"]:
            print(f"           P(row fails all six) >= 1%: {r['allfail']}")


if __name__ == "__main__":
    main()
